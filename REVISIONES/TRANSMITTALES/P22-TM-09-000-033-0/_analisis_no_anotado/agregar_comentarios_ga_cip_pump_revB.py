#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_cip_pump_revB.py
Anota el GA of CIP Flushing Skid Pump Rev B (P22-DWG-09-005-010), submittal
25007-0076 (E76). Veredicto del TM N33: Code 2 - Approved as noted.

len(COMENTARIOS) = 5, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Las TRES partes de la NOTE-05 del TM N11 CIERRAN y no se anotan:
plano de disposicion de pernos con diametro, separacion y empotramiento;
reacciones sismicas de base; y masa del equipo con centro de gravedad. El
documento entrega ademas mas de lo que su propia hoja de comentarios reclama:
la respuesta escrita solo cuenta dos de las tres. Lo que se anota es la
coherencia interna de esas cifras, todo incorporable al emitir Rev 0.

PAGINA ROTADA: la lamina tiene rotation 270. La skill v1.6 resuelve el caso con
text_rotate = original_rotation, de modo que NO se hardcodea 270. Cierre
obligatorio: verificar por render PNG que el ID y el texto se leen completos y
de izquierda a derecha, porque en paginas rotadas page.annots() devuelve 0
aunque la anotacion exista.

Estructura del archivo (indices 0-based):
    0   caratula A4
    1   lamina A1, rotation 270, GA con notas, bolting layout y embedment
    2   Consolidated Comment Sheet
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-010_B_GA_CIP_Flushing_Skid_Pump.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-010_B_GA_CIP_Flushing_Skid_Pump_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 76",
        "P22-DWG-09-005-010_GA of CIP Flushing Skid Pump_Rev.B-001.pdf",
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
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: Note 4.1 and the bolting layout call M14\n"
            "threaded rod anchor bolts. The bolting layout of\n"
            "this sheet dimensions the base plate hole at 14\n"
            "mm, the clearance hole of an M12, which does not\n"
            "admit an M14. Detail 4 of the Civil and Loading\n"
            "Layout Rev B fixes M12 on the same pattern.\n"
            "Correct: adopt M12."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: Note 6 states the design load as 180 kg\n"
            "pump plus seismic force 0.3 g. Fy is 1.7652 kN,\n"
            "which is 180 kg times 9.81, so Fy is the self\n"
            "weight. Fx is 1.2356 kN, which is 0.70 of that\n"
            "weight and not 0.30. The factor applied is more\n"
            "demanding than the one declared, so the reactions\n"
            "are not short; the label is what fails.\n"
            "Correct: state the factor actually used."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-03: the block is titled TOTAL SEISMIC REACTION\n"
            "FORCES and Fz, 0.6178 kN, is Fx divided by two\n"
            "over four bolts, so the value is per pair of bolts\n"
            "and not a total. The same defect was raised as\n"
            "OBS-01 on the sibling drawing at Transmittal N26.\n"
            "Correct: retitle the block and state the vertical\n"
            "tension and compression per bolt, which is what\n"
            "governs a post-installed chemical anchor."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-04: the EMBEDMENT DEPTH view dimensions 149 mm\n"
            "from the top of the nut to the lower end of the\n"
            "rod, which is the total rod length. Net of the base\n"
            "plate and nut, the embedded part falls below the\n"
            "120 mm that Note 4.3 requires.\n"
            "Correct: dimension the embedded length."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-05: Note 9 refers the reactions to AS PER\n"
            "CALCULATION REPORT, with no code or revision. The\n"
            "candidate is the UHPRO Structural Calculation\n"
            "Report P22-CD-09-005-001, at Rev 0 in submittal\n"
            "25007-0071.\n"
            "Correct: identify the report by code and revision,\n"
            "so the figures are traceable."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
