#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recorta del PDF de la propuesta de repuestos las dos regiones que se insertan en
el correo del 11-Ago-2026:

  fig1 — pagina 1, bloque de condiciones comerciales (forma de pago, Incoterms
         "EXW Penang, Malaysia", validez hasta el 28-Ago-2026)
  fig2 — pagina 3, cabecera del Anexo A + primeras lineas, donde conviven
         DDP Penang / EXW Hengshui / EXW Mungia / EXW Michigan y la columna
         contigua "Estimated Transit Time"

Recortes CRUDOS: sin resaltados ni marcas anadidas. La evidencia debe ser un
extracto intacto del documento de BW Water.

Las coordenadas se resuelven con page.search_for() en vez de hardcodearse, para
que el script sobreviva a una reemision del PDF. Solo lee el PDF fuente.

Nota del PDF: la pagina 1 usa una fuente con codificacion desplazada en ASCII,
de modo que get_text() devuelve los encabezados ilegibles aunque el render se ve
correcto. Por eso la validacion de estas figuras es visual, abriendo el PNG.

Idempotente: re-correrlo regenera los mismos PNG.
"""

import os

import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PDF_FUENTE = os.path.join(
    PROYECTO,
    "PROGRAMA y CONTRATO",
    "REPUESTOS DE 2 AÑOS",
    "propuesta formal",
    "Proposal 25007-PL-0002_rev.0 - 2y spare parts_s.pdf",
)
FIG_DIR = os.path.join(SCRIPT_DIR, "figuras")
DPI = 300


def render(page, clip, destino):
    zoom = DPI / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(destino)
    print(f"  {os.path.basename(destino)}  {pix.width}x{pix.height} px  clip={clip}")


def bbox_condiciones_comerciales(page):
    """Desde el primer '50%' de payment terms hasta la linea de validez."""
    pago = page.search_for("50%")
    validez = page.search_for("August 28")
    if not pago or not validez:
        raise SystemExit("No se ubico el bloque de condiciones comerciales en la pagina 1")
    y0 = min(r.y0 for r in pago) - 28
    y1 = max(r.y1 for r in validez) + 14
    return fitz.Rect(30, y0, 430, y1)


def bbox_anexo_a(page):
    """Desde la fila de encabezado hasta el kit de bombas dosificadoras.

    Ese corte ya contiene las cinco variantes de la columna Incoterms (DDP
    Penang, EXW Hengshui, EXW Mungia, EXW Michigan y de vuelta DDP Penang) con
    su tiempo de transito al lado, que es todo el argumento. Bajar mas solo
    agrega filas de instrumentos que repiten DDP Penang y alargan la imagen.
    """
    encabezado = page.search_for("Estimated")
    # BDS-09-002 es la ultima linea de la fila del kit de dosificacion; cortar
    # ahi deja el borde de la fila completo sin invadir la siguiente.
    ultima = page.search_for("BDS-09-002")
    if not encabezado or not ultima:
        raise SystemExit("No se ubico la tabla del Anexo A en la pagina 3")
    y0 = min(r.y0 for r in encabezado) - 10
    y1 = max(r.y1 for r in ultima) + 3
    return fitz.Rect(15, y0, 600, y1)


def main():
    os.makedirs(FIG_DIR, exist_ok=True)
    doc = fitz.open(PDF_FUENTE)
    print(f"Fuente: {os.path.basename(PDF_FUENTE)} ({doc.page_count} paginas)")

    render(
        doc[0],
        bbox_condiciones_comerciales(doc[0]),
        os.path.join(FIG_DIR, "fig1_commercial_conditions.png"),
    )
    render(
        doc[2],
        bbox_anexo_a(doc[2]),
        os.path.join(FIG_DIR, "fig2_annexA_incoterms.png"),
    )
    doc.close()


if __name__ == "__main__":
    main()
