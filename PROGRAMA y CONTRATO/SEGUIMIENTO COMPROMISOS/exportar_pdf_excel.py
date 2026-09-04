#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exportar_pdf_excel.py — Gate visual del Registro de Compromisos.

Renderiza el .xlsx a PDF abriendolo en Microsoft Excel real. Es un GATE, no un
entregable: el PDF sirve para comprobar de un vistazo que el semaforo esta
poblado, que los colores concuerdan con las fechas y que las fechas se ven como
`dd-mmm-yyyy` y no como numero de serie.

Por que Excel real y NO LibreOffice: openpyxl escribe las formulas sin valor
cacheado. LibreOffice abre los .xlsx con el recalculo desactivado por defecto,
de modo que mostraria vacias las columnas de Semaforo y de Dias y llevaria a
diagnosticar un defecto que no existe.

Por que late binding (`dynamic.Dispatch`): la interop tipada de este equipo
falla al castear ApplicationClass y deja un EXCEL.EXE huerfano (mismo criterio
que `exportar_pdf_word.py`).

Uso:
    python exportar_pdf_excel.py                 # el registro por defecto
    python exportar_pdf_excel.py <libro.xlsx> [<salida.pdf>]
"""
import os
import sys

from win32com.client import dynamic

XL_TYPE_PDF = 0
XL_LANDSCAPE = 2
XL_PORTRAIT = 1

BASE = os.path.dirname(os.path.abspath(__file__))
DEFECTO = os.path.join(BASE, "P22-IT-06-000-006-0_Registro-de-Compromisos.xlsx")

# Ancho util por hoja. `Compromisos` tiene 23 columnas y no cabe legible en una
# pagina: se deja en varias a lo ancho y se repite la fila de encabezado.
AJUSTE = {
    "Panel":        dict(orient=XL_PORTRAIT,  ancho=1, alto=1),
    "Compromisos":  dict(orient=XL_LANDSCAPE, ancho=0, alto=0),
    "Hitos":        dict(orient=XL_LANDSCAPE, ancho=1, alto=0),
    "Movimientos":  dict(orient=XL_LANDSCAPE, ancho=1, alto=0),
    "Leyenda":      dict(orient=XL_PORTRAIT,  ancho=1, alto=0),
}


def exportar(entrada, salida=None):
    entrada = os.path.abspath(entrada)
    if not os.path.exists(entrada):
        raise SystemExit("ERROR: no existe la entrada: %s" % entrada)
    if not salida:
        salida = os.path.splitext(entrada)[0] + "_VISTA.pdf"
    salida = os.path.abspath(salida)

    lock = os.path.join(os.path.dirname(entrada), "~$" + os.path.basename(entrada))
    if os.path.exists(lock):
        print("AVISO: existe un lock de Excel (%s). Cierra el libro en Excel." % lock)

    xl = dynamic.Dispatch("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    wb = None
    try:
        wb = xl.Workbooks.Open(entrada, UpdateLinks=0, ReadOnly=True)

        # Sin esto las columnas de formula pueden salir sin valor en el render.
        xl.CalculateFullRebuild()

        for ws in wb.Worksheets:
            cfg = AJUSTE.get(ws.Name, dict(orient=XL_LANDSCAPE, ancho=1, alto=0))
            ps = ws.PageSetup
            ps.Orientation = cfg["orient"]
            ps.Zoom = False                     # obligatorio antes de FitToPages
            ps.FitToPagesWide = cfg["ancho"] if cfg["ancho"] else False
            ps.FitToPagesTall = cfg["alto"] if cfg["alto"] else False
            ps.LeftMargin = ps.RightMargin = xl.InchesToPoints(0.3)
            ps.TopMargin = ps.BottomMargin = xl.InchesToPoints(0.4)
            if ws.Name in ("Compromisos", "Hitos", "Movimientos"):
                ps.PrintTitleRows = "$1:$1"     # encabezado repetido por pagina
            ps.CenterHeader = "&\"Arial,Bold\"&11" + ws.Name
            # Solo &P: el codigo de total de paginas se localiza segun la UI de
            # Excel y en un equipo en espanol devuelve el nombre del archivo.
            ps.RightFooter = "Pagina &P"

        wb.ExportAsFixedFormat(XL_TYPE_PDF, salida)
        print("PDF:", salida)
        print("      %.1f KB" % (os.path.getsize(salida) / 1024))
        return salida
    finally:
        if wb is not None:
            wb.Close(SaveChanges=False)
        xl.Quit()


if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else DEFECTO
    salida = sys.argv[2] if len(sys.argv) > 2 else None
    exportar(entrada, salida)
