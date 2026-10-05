#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_yoke_drawing_revA.py
Anota el plano del yugo P22-DWG-09-005-019 Rev A, GA of Module Lifting from Top, hoja 1
de 3, que BW Water mando como pagina 13 del UHPRO Structural Calculation Report -
Addendum Rev A (submittal 25007-0099, ENTREGA 99, 29-Sep-2026) y no declaro en el
formulario. Veredicto del TM N42: Code 3 - To be revised, reemitir como Rev B completo.

Se codifica y se anota como documento propio a pedido de Luis (5-Oct): el reclamo del
plano de detalle del yugo, pedido en el correo de ADASA del 15-Sep, tiene que verse en
el transmittal y no quedar escondido dentro del addendum.

len(COMENTARIOS) = 6, espejo 1:1 del bloque Action de la subseccion 2.1 (un ID por
clausula). Detalle y evidencia en ENTREGAS_BWWATER/ENTREGA 99/_LEDGER_COMENTARIOS.md.

Eslingas: se pide tension de diseno por ramal y largo, no WLL. El correo del 11-Sep dejo
la seleccion de grua, eslingas y grilletes al method statement del contratista de izaje.

Perfiles (Luis, 5-Oct): el W10x49 es laminado importado; se pide el equivalente soldado de
fabricacion nacional, IN o HN (NCh 730), con calidad segun NCh203 como exige el Criterio de
Diseno aprobado. Empalme y esquinas: los largueros miden 12.776 mm y el
plano no muestra ninguno. No se afirma que el perfil nacional se venda en 12 m: Cintac y
Prodalam declaran largo variable a pedido. Fuentes en BASES TECNICAS/REFERENCIAS ACERO CHILE/.

Viga intermedia (Luis, 5-Oct): cuadro propio sobre la vista en planta, con flecha al punto
medio del larguero inferior. Sin vigas intermedias no hay certeza del comportamiento
torsional de la maniobra ni del pandeo de los largueros de 12.776 mm, que las eslingas
superiores comprimen. Se pide al menos una viga a medio largo y su verificacion de
torsion, desangulacion y pandeo en el addendum. Va primero en la lista para que
`preparar()` le de la zona libre mas cercana a la planta.
"""
import os
import sys

import fitz  # PyMuPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-019_A_GA_Module_Lifting_from_Top.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-019_A_GA_Module_Lifting_from_Top_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 99",
    "P22-CD-09-005-003_A UHPRO Structural Calculation Report - Addendum.pdf"))
PAGINA_DEL_PLANO = 12  # 0-based: pagina 13 del addendum

# Vista en planta: larguero inferior entre y 307,7 y 325,7 pt, de x 112 a 1017 pt
# (get_drawings). La flecha termina en su punto medio.
MEDIO_LARGUERO = (564.5, 317.0)

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": None, "page_fallback": 0, "page_min": 0,
        # ancho 295 (590 pt): el hueco bajo la planta, a la derecha del titulo PLAN VIEW,
        # mide unos 590 x 167 pt; con el ancho base el cuadro no cabe y cae lejos.
        "ancla_pantalla": (540, 300, 590, 330), "flecha_a": MEDIO_LARGUERO, "ancho": 295,
        "text": "{ID}: The frame has no intermediate beam. The torsion of the frame during "
                "the lift and the buckling of the 12,776 mm long members, compressed by the "
                "inclined slings, are not verified. Correct: add at least one intermediate "
                "beam at mid-length of the yoke, with its connections and welds, and verify "
                "the frame against torsion, racking and buckling in the calculation addendum.",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "1 OF 3", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: Sheet 1 of 3. Sheets 2 and 3 were not received, and the drawing "
                "is not on submittal form 25007-0099. Correct: submit it complete as a "
                "document of its own. It is the yoke drawing requested for fabrication in "
                "ADASA's e-mail of 15 September 2026.",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "CHECK COMPATIBILITY", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: Note 2 leaves the connection at the ISO corner fittings open. "
                "Correct: show how each sling connects to its corner fitting, as requested "
                "in ADASA's e-mail of 15 September 2026.",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "DIMENSIONS ARE IN MILLIMETERS", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: No weight is stated, and slings 4 and 8 carry neither design "
                "tension nor length. Correct: state the lifted weight of the module, the "
                "weight of the frame and rigging, the total load on the hook and the "
                "design tension and length of each sling leg (Technical Specification, "
                "Section 7, page 29).",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "I-BEAM - W10 x 49", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: W10x49 is an imported rolled section, and ADASA fabricates the "
                "yoke in Chile. Correct: replace each member with its national welded "
                "equivalent, IN or HN series, and state its steel grade to NCh203, as the "
                "approved Design Criteria require.",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "STEEL STRUCTURE", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: The long members are 12,776 mm, and the drawing shows no splice and "
                "no corner joint detail. Correct: detail the splice of the long members and "
                "the corner joints of the frame, with their welds.",
    },
]

def flechas(pdf_out, comentarios, rects):
    """Flecha nativa (anotacion Line) desde el borde del cuadro mas cercano al objetivo
    hasta el punto `flecha_a`, en coordenadas de pantalla (la lamina no esta rotada)."""
    doc = fitz.open(pdf_out)
    for c in comentarios:
        if not c.get("flecha_a"):
            continue
        page = doc[c.get("page_min", c.get("page_fallback", 0))]
        r = rects[c["text"]]
        tx, ty = c["flecha_a"]
        inicio = fitz.Point(min(max(tx, r.x0), r.x1), min(max(ty, r.y0), r.y1))
        a = page.add_line_annot(inicio, fitz.Point(tx, ty))
        a.set_line_ends(fitz.PDF_ANNOT_LE_NONE, fitz.PDF_ANNOT_LE_CLOSED_ARROW)
        a.set_colors(stroke=(0, 0, 0), fill=(0, 0, 0))
        a.set_border(width=2)
        a.set_info(title="ADASA", content=c["id"])
        a.update()
        print(f"  [{c['id']}] flecha ({inicio.x:.0f},{inicio.y:.0f}) -> ({tx:.0f},{ty:.0f})")
    tmp = pdf_out + ".tmp"
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    os.replace(tmp, pdf_out)


if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        src = fitz.open(SRC)
        solo = fitz.open()
        solo.insert_pdf(src, from_page=PAGINA_DEL_PLANO, to_page=PAGINA_DEL_PLANO)
        solo.save(PDF_LOCAL, garbage=3, deflate=True)
        print("Plano extraido de la pagina 13 del addendum.")
    assert len(COMENTARIOS) == 6, len(COMENTARIOS)
    _, rects, _ = correr(PDF_LOCAL, PDF_OUT, COMENTARIOS,
                         prohibidas_por_pagina={0: cajetin_bw_a1()})
    flechas(PDF_OUT, COMENTARIOS, rects)
