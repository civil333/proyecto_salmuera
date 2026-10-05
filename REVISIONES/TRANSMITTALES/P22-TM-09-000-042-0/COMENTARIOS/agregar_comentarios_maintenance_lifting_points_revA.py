#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_maintenance_lifting_points_revA.py
Anota el Maintenance Lifting Points Layout and Details Rev A (P22-DWG-09-005-006) del
submittal 25007-0096 (ENTREGA 96, 22-Sep-2026). Primera emision, contra ET Seccion 7 pag. 28.
Veredicto del TM N42: Code 3 - To be revised.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de la subseccion 2.2
("OBS-01 and OBS-02 on the annotated PDF"). Detalle y evidencia en ENTREGAS_BWWATER/ENTREGA 96/_LEDGER_COMENTARIOS.md.
Lamina A1 rotada 270: la skill dibuja en el contenido de la pagina; la posicion
la fija _cajas_fijas.zona_libre y se verifica por render (CLAUDE.md seccion 3.8).
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402,F401

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-006_A_Maintenance_Lifting_Points.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-006_A_Maintenance_Lifting_Points_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 96",
    "P22-DWG-09-005-006_A Maintenance Lifting Points Layout and Details.pdf"))

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": 'MAINTENANCE LIFTING POINTS LAYOUT', "page_fallback": 1, "page_min": 1,
        "text": (
            "{ID}: Only the motor of the high-pressure pump BH-09-001 is covered. The "
            "pumps and the turbochargers SIP-09-001 and SIP-09-002 have no lifting point "
            "and no route out of the module. Correct: add them (Technical "
            "Specification, Section 7, page 28)."
        ),
    },
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": 'HOOK CRANE', "page_fallback": 1, "page_min": 1,
        "text": (
            '{ID}: The hook hangs with no runway beam or fixed lifting point above it, '
            'and note 2 leaves the method to the lifting contractor. Correct: show the '
            'runway beam or fixed point, its attachment to the module structure and its '
            'working load limit against the heaviest piece it lifts.'
        ),
    },
]

if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        shutil.copy2(SRC, PDF_LOCAL)
    assert len(COMENTARIOS) == 2, len(COMENTARIOS)
    correr(PDF_LOCAL, PDF_OUT, COMENTARIOS, prohibidas_por_pagina={1: cajetin_bw_a1()})
