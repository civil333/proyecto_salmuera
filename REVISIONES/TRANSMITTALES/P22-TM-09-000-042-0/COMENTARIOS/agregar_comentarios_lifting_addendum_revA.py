#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_lifting_addendum_revA.py
Anota el UHPRO Structural Calculation Report - Addendum Rev A (P22-CD-09-005-003) del
submittal 25007-0099 (ENTREGA 99, 29-Sep-2026), Veredicto del TM N42: Code 3 -
To be revised, reemitir con codigo propio. El plano del yugo de su pagina 13
(P22-DWG-09-005-019 Rev A) se anota aparte en agregar_comentarios_yoke_drawing_revA.py.

len(COMENTARIOS) = 4, espejo 1:1 del bloque Action de la subseccion 2.2 (un ID por
clausula). Detalle y evidencia en
ENTREGAS_BWWATER/ENTREGA 99/_LEDGER_COMENTARIOS.md.

Estandar de revision: ET Seccion 7 pag. 29 y los correos de ADASA del 11 y del 15-Sep
(plano de fabricacion del yugo). Pedido de Luis del 5-Oct: el reclamo del plano del yugo
cita el correo del 15-Sep.

Torsion, desangulacion y pandeo (Luis, 5-Oct): el STAAD se usa solo para la tension
critica de eslinga. Sin vigas intermedias no hay certeza del comportamiento torsional de
la maniobra ni del pandeo de los largueros de 12.776 mm; se pide modelar el marco con al
menos una viga intermedia y demostrarlo. Espejo del cuadro de la planta del plano del yugo.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-005-003_A_Lifting_Addendum.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-005-003_A_Lifting_Addendum_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 99",
    "P22-CD-09-005-003_A UHPRO Structural Calculation Report - Addendum.pdf"))

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": "ADASACode", "page_fallback": 0, "page_min": 0,
        "text": "{ID}: This code belongs to the UHPRO Structural Design Criteria, approved "
                "at Rev 0, and the file carries three revision marks: Rev A of 22 September "
                "2026 here, Rev A of 29 June 2026 on the Aulem cover and Rev B of "
                "18 September 2026 in the header of Aulem page 6. Correct: issue the "
                "addendum under its own ADASA code, with one revision and one date.",
    },
    {
        # pagina de imagen, sin capa de texto: ancla fijada en pantalla junto al titulo
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": None, "page_fallback": 2, "page_min": 2,
        "ancla_pantalla": (300, 110, 420, 125),
        "text": "{ID}: Only the lugs are checked, in allowable stress design with the "
                "shackle working load and no stated load combination. The frame members, "
                "splices and joints carry no design check. Correct: design them with the "
                "national IN or HN section, stating the method, under the NCh3171 "
                "combinations of Section D of the approved Design Criteria as a minimum and "
                "the 1.35D and 2.0D lifting factors of its Section F.",
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": None, "page_fallback": 2, "page_min": 2,
        "ancla_pantalla": (300, 300, 420, 315),
        "text": "{ID}: The ISO corner fittings and corner posts that take the sling loads "
                "are not checked. Correct: add their local check with the factor of "
                "safety of 2.0 and the 5 per cent lateral load, as requested in ADASA's "
                "e-mail of 11 September 2026.",
    },
    {
        # La pagina 3 ya no tiene zona libre; va al pie de la pagina 4 (Aulem "Page 3 of
        # 11", geometria de las orejas), ancho 380 para caber en el hueco de 380 x 70 pt.
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": None, "page_fallback": 3, "page_min": 3,
        "ancla_pantalla": (300, 630, 320, 640), "ancho": 380,
        "text": "{ID}: The STAAD model of the frame is used only for the critical sling "
                "tension of the design load (page 2 of 11). No check covers the torsion of "
                "the frame, its racking or the buckling of the 12,776 mm long members under "
                "the compression from the inclined slings. Correct: model the frame with at "
                "least one intermediate beam at mid-length and show that torsion, racking "
                "and buckling stay within the limits of the method used, under the "
                "combinations and lifting factors of the approved Design Criteria.",
    },
]

if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        shutil.copy2(SRC, PDF_LOCAL)
    assert len(COMENTARIOS) == 4, len(COMENTARIOS)
    correr(PDF_LOCAL, PDF_OUT, COMENTARIOS)
