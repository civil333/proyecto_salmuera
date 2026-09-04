#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_antiscalant_tank_revC.py
Anota el GA of Antiscalant Dosing Tank Rev C (P22-DWG-09-005-015) del submittal
25007-0084 (ENTREGA 84). Veredicto del TM N36: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N26, subseccion 2.8, Code 3. Es el unico
documento del lote que venia de Code 3 y lo sustantivo cerro.
  OBS-01 del N26, cargas sismicas y patron de pernos -> CERRADA con residuo:
      llegaron la nota 16, la nota 15 y el Detalle 4 nuevo, pero la cota del
      agujero no cuadra con el perno declarado -> OBS-01
  OBS-02 del N26, volumen util efectivo -> CERRADA. No se anota.
  OBS-02 del N26, fila LEVEL MARKING    -> CIERRE PARCIAL -> NOTE-01
  NOTE-02 del N26, TAG TK-09-002        -> CERRADA. No se anota.
  NOTE-01 del N26 era accion sobre el P&ID, no sobre este plano.

Verificar que lo agregado es correcto forma parte de verificar el cierre: por
eso la cota del agujero entra dentro de la OBS-01 y no es observacion nueva.

NO SE ANOTA, per la regla de alcance:
  - El cajetin declara ISSUED FOR APPROVAL con fechas de firma de mayo.
  - El volumen total instalado de 0,34 m3, que se pidio en el ciclo de la Rev A
    y el TM N26 no repitio en su accion sobre la Rev B.

DEPENDENCIA QUE NO DEGRADA: la nota 16 declara las cargas "as per calculation
report" sin citar codigo ni revision, y ese informe sigue sin endoso de
ingeniero profesional habilitado en Chile. Va a la Seccion 3 del transmittal,
no a este PDF.

Reparto por pagina (indices 0-based):
    1   lamina unica, rotacion 270 -> OBS-01 y NOTE-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_C_GA_Antiscalant_Dosing_Tank.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_C_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 84", "25007-0084",
        "P22-DWG-09-005-015_C GA of Antiscalant Dosing Tank.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MENOR,
        "search": "ANCHORING DETAILS",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-01: the anchorage is delivered, and two\n"
            "dimensions in it do not reconcile.\n"
            "ADASA acknowledges the closure: note 16 states\n"
            "the seismic reactions, note 15 the centre of\n"
            "gravity, and Detail 4 is new and gives the bolt,\n"
            "the load per bolt and the embedment. The loads\n"
            "are consistent with the three lugs of this\n"
            "detail.\n"
            "What does not reconcile is on this detail. The\n"
            "hole is labelled 14 mm and half an inch, which\n"
            "are not the same dimension: half an inch is\n"
            "12.7 mm. Rev B labelled the same hole 10 mm and\n"
            "half an inch, so the metric value changed and\n"
            "the imperial one did not. The bolt declared in\n"
            "Detail 4 is M12, which takes the normal\n"
            "clearance in a 14 mm hole and sits in a tight\n"
            "fit in a 12.7 mm one.\n"
            "Correct: reconcile the two values of this\n"
            "dimension against the M12 bolt when the drawing\n"
            "is issued at Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "LEVEL MARKING",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "NOTE-01: the level marking row is still\n"
            "incomplete.\n"
            "Transmittal N26 recorded this row as blank. It\n"
            "now carries its location, SIDE, and leaves size\n"
            "and elevation as dashes.\n"
            "Note 8 declares an effective working volume of\n"
            "0.27 cubic metres. Without an elevation on this\n"
            "row there is no mark on the tank that\n"
            "materialises that volume, so the figure cannot\n"
            "be verified in the field or used to set the\n"
            "level instrument.\n"
            "Correct: state the elevation of the level mark\n"
            "corresponding to the effective working volume\n"
            "when the drawing is issued at Rev 0."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
