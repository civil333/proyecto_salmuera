"""
agregar_comentarios_ic_cable_schedule.py
Anota PDF Instrumentation & Control Cable Schedule Rev 1 (TM N20).
len(COMENTARIOS) = 4 (OBS-01 + OBS-02 + OBS-03 + NOTE-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-002_1_IC_Cable_Schedule.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-002_1_IC_Cable_Schedule_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-LI-09-008-002_1 Instrumentation & Control Cable Schedule.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "VE09-003-COM",
        "page_fallback": 3,
        "text": (
            "OBS-01: duplicate item numbers on this\n"
            "sheet - 54, 55 and 56 each assigned twice\n"
            "(VE09-006 and VE09-003 rows; PIT09-005-AI\n"
            "and VE09-004-COM). Correct: renumber\n"
            "uniquely and contiguously in Rev 2."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 3,
        "text": (
            "OBS-02: valve POWER row descriptions are\n"
            "copy-pasted - multiple PWR rows read\n"
            "RO 2ND STAGE CIP FEED MOTORIZED VALVE\n"
            "POWER for valves that are not the CIP feed\n"
            "valve (e.g. VE09-006-PWR, VE09-003-PWR).\n"
            "Correct: match every PWR description to\n"
            "its Full Tag in Rev 2."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "LIT09-002",
        "page_fallback": 3,
        "text": (
            "OBS-03: Function column reads PIT on\n"
            "LIT09-002 and TIT09-006 rows (items\n"
            "60/61). Correct: LIT and TIT respectively\n"
            "in Rev 2."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "VT09-001",
        "page_fallback": 2,
        "text": (
            "NOTE-01: RTD cable construction differs\n"
            "between HP (Cu/PE/S/UTP/PUR) and CIP\n"
            "(Cu/PVC/OS/PVC) trains for identical\n"
            "signals; VT09-001 remark 2 Wire, 24VDC\n"
            "conflicts with I/O List loop-powered\n"
            "4-20 mA. Correct: reconcile or justify\n"
            "in Rev 2."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
