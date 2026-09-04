#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exportar_pdf_word.py — equivalente Windows de exportar_pdf_word_mac.sh.

Exporta un .docx a PDF abriendolo en Microsoft Word real y actualizando el TOC y
todos los campos antes de guardar. Word es obligatorio para el PDF que se emite:
LibreOffice headless NO actualiza el campo TOC y deja el placeholder
"Right-click and select 'Update Field'" (CLAUDE.md Seccion 3.13).

Uso:
    python exportar_pdf_word.py "<entrada.docx>" ["<salida.pdf>"]

Por que win32com con LATE BINDING (`dynamic.Dispatch`) y no la PIA tipada:
la interop tipada de este equipo falla al castear ApplicationClass a
_Application (TYPE_E_ELEMENTNOTFOUND) y deja un WINWORD.EXE huerfano. El late
binding resuelve por IDispatch y no depende de la PIA (mismo criterio que la
Seccion 3.12 del CLAUDE.md para los formularios RFI).

Gotchas heredados del flujo macOS:
  - Cerrar el documento en Word antes de reconvertir; un lock ~$*.docx abierto
    hace fallar el Open o lo devuelve en solo lectura.
  - El PDF se genera desde el .docx en disco, no desde el buffer de un Word
    abierto.
  - Se cierra el documento SIN guardar: la actualizacion de campos no debe
    alterar el .docx fuente.
"""
import os
import sys

import win32com.client
from win32com.client import dynamic

WD_FORMAT_PDF = 17
WD_STAT_PAGES = 2
WD_DO_NOT_SAVE = 0


def exportar(entrada: str, salida: str | None = None) -> str:
    entrada = os.path.abspath(entrada)
    if not os.path.exists(entrada):
        raise SystemExit(f"ERROR: no existe la entrada: {entrada}")

    if not salida:
        salida = os.path.splitext(entrada)[0] + ".pdf"
    salida = os.path.abspath(salida)

    lock = os.path.join(os.path.dirname(entrada), "~$" + os.path.basename(entrada))
    if os.path.exists(lock):
        print(f"AVISO: existe un lock de Word ({lock}). Cierra el documento en Word.")

    word = dynamic.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = False
    doc = None
    try:
        doc = word.Documents.Open(entrada, ConfirmConversions=False, ReadOnly=False)

        # 1) Campos del cuerpo.
        doc.Fields.Update()

        # 2) Tablas de contenido: sin esto el PDF sale con el campo sin resolver.
        for i in range(1, doc.TablesOfContents.Count + 1):
            doc.TablesOfContents(i).Update()

        # 3) Campos de encabezado y pie (codigo de documento, fecha, pagina).
        for seccion in doc.Sections:
            for hf in seccion.Headers:
                hf.Range.Fields.Update()
            for hf in seccion.Footers:
                hf.Range.Fields.Update()

        doc.SaveAs(salida, FileFormat=WD_FORMAT_PDF)
        paginas = doc.ComputeStatistics(WD_STAT_PAGES)
        print(f"PDF generado: {salida}")
        print(f"Paginas: {paginas}")
        return salida
    finally:
        if doc is not None:
            doc.Close(WD_DO_NOT_SAVE)
        word.Quit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    exportar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
