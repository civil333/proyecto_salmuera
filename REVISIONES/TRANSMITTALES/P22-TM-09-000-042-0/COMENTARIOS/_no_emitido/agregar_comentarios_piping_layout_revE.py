#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_piping_layout_revE.py
Anota el Piping Layout Rev E (P22-DWG-09-005-004) del submittal 25007-0096 (ENTREGA 96,
22-Sep-2026). Viene de Code 2 en el TM N36; las tres condiciones cerraron.
Veredicto del TM N42: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.4
("OBS-01 on the annotated PDF"). Detalle y evidencia en ENTREGAS_BWWATER/ENTREGA 96/_LEDGER_COMENTARIOS.md.
Hallazgo de la verificacion de lo agregado: rotulo de la linea 09-022 contra la
Line List Rev 2 (alinear a otro documento = Code 2). Lamina A1 rotada 270.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402,F401

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_E_Piping_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_E_Piping_Layout_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 96",
    "P22-DWG-09-005-004_E Piping Layout.pdf"))

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": 'CP-PVC-DN150-09-022', "page_fallback": 1, "page_min": 1,
        "text": (
            '{ID}: The CIP pump suction line is labelled CP-PVC-DN150-09-022 here and on '
            'page 4 of this file; the approved Line List Rev 2 carries it as CP-'
            'SS316-DN150-09-022, in 316L. Correct: relabel it at Rev 0.'
        ),
    },
]

if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        shutil.copy2(SRC, PDF_LOCAL)
    assert len(COMENTARIOS) == 1, len(COMENTARIOS)
    correr(PDF_LOCAL, PDF_OUT, COMENTARIOS, prohibidas_por_pagina={1: cajetin_bw_a1()})
