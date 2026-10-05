#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_valve_list_rev0.py
Anota la Valve List Rev 0 (P22-LI-09-005-002) del submittal 25007-0100 (ENTREGA 100,
1-Oct-2026). Viene de Code 2 en el TM N39; emitida IFC.
Veredicto del TM N42: Code 3 - To be revised (reemitir como Rev 1).

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.3
("OBS-01 on the annotated PDF"). Detalle y evidencia en ENTREGAS_BWWATER/ENTREGA 100/_LEDGER_COMENTARIOS.md.

"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR  # noqa: E402
from _cajas_fijas import correr, cajetin_bw_a1  # noqa: E402,F401

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_0_Valve_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_0_Valve_List_CC_ADASA.pdf")
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 100",
    "P22-LI-09-005-002_0 Valve List.pdf"))

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR, "zona": True,
        "search": 'VM-09-065', "page_fallback": 1, "page_min": 1,
        "text": (
            "{ID}: VM-09-065 still reads PVC body, trim and disc on line "
            "CP-SS316-DN150-09-022, which the approved Line List Rev 2 carries in "
            "316L. Only the pipe material column changed. Correct: list the body, "
            "trim and disc in SS316L."
        ),
    },
]

if __name__ == "__main__":
    if not os.path.exists(PDF_LOCAL):
        shutil.copy2(SRC, PDF_LOCAL)
    assert len(COMENTARIOS) == 1, len(COMENTARIOS)
    correr(PDF_LOCAL, PDF_OUT, COMENTARIOS)
