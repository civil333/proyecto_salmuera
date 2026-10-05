#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_antiscalant_tank_revE.py
Anota el GA of Antiscalant Dosing Tank Rev E (P22-DWG-09-005-015) del submittal
25007-0096 (ENTREGA 96, 22-Sep-2026). Tercer ciclo de la marca de nivel (N36, N39, N42).
Veredicto del TM N42: Code 2 - Approved as noted, reiterado.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.5
("OBS-01 on the annotated PDF"). Detalle y evidencia en ENTREGAS_BWWATER/ENTREGA 96/_LEDGER_COMENTARIOS.md.
ADASA declara el valor vinculante: 864 mm = 34 in. Lamina A1 rotada 270.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402,F401

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_E_GA_Antiscalant_Dosing_Tank.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_E_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 96",
    "P22-DWG-09-005-015_E GA of Antiscalant Dosing Tank.pdf"))

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": 'LEVEL MARKING', "page_fallback": 1, "page_min": 1,
        "text": (
            '{ID}: The LM row reads 3\' 7", the overall height of the tank, above the N80 '
            'overflow at 39 3/8". View 1 places the 0.27 m³ working volume at 864 mm. '
            'Correct: set the LM elevation at 34" (864 mm) at Rev 0.'
        ),
    },
]

if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        shutil.copy2(SRC, PDF_LOCAL)
    assert len(COMENTARIOS) == 1, len(COMENTARIOS)
    correr(PDF_LOCAL, PDF_OUT, COMENTARIOS, prohibidas_por_pagina={1: cajetin_bw_a1()})
