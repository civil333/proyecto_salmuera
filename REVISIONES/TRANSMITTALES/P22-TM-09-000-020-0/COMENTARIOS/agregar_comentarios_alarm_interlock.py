"""
agregar_comentarios_alarm_interlock.py
Anota PDF Alarm & Interlock List Rev B (TM N20).
len(COMENTARIOS) = 5 (OBS-01 + OBS-02 + OBS-03 + NOTE-01 + NOTE-02).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-015_B_Alarm_Interlock_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-015_B_Alarm_Interlock_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 46",
        "P22-LI-09-008-015_B Alarm & Interlock List.pdf",
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
        "search": "RO HP Pump Bearing Temperature Sensor",
        "page_fallback": 4,
        "text": (
            "OBS-01: TE-09-001/002 winding-bearing\n"
            "assignment is swapped against Instrument\n"
            "List Rev E (IL: TE-09-001=Winding,\n"
            "TE-09-002=Bearing); same swap on\n"
            "TE-09-003/004. Trip setpoints differ per\n"
            "sensor (90 C vs 140 C), so the interlock\n"
            "acts on the wrong element. Correct:\n"
            "reconcile tags across Instrument List,\n"
            "I/O List and motor vendor documentation\n"
            "in Rev C."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "90.0",
        "page_min": 4,
        "page_fallback": 4,
        "text": (
            "OBS-02: CCS records motor vendor\n"
            "confirmation to raise bearing AHH to\n"
            "95 C, yet item 27.1 retains 90.0 C.\n"
            "Correct: apply the confirmed 95 C\n"
            "setpoint in Rev C."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "RO CIP/Flush pH analyzer",
        "page_fallback": 4,
        "text": (
            "OBS-03: pH analyzer tagged PHIT-09-001;\n"
            "Instrument List Rev E and Data Transfer\n"
            "List tag it PHIT-09-006. Correct: align\n"
            "to PHIT-09-006 in Rev C."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "TIT-09-005",
        "page_fallback": 4,
        "text": (
            "NOTE-01: CIP Tank temperature transmitter\n"
            "tagged TIT-09-005 here, TIT-09-006 in\n"
            "Instrument List Rev E. Correct: align\n"
            "tag in Rev C."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "LIT-09-002",
        "page_fallback": 4,
        "text": (
            "NOTE-02: instrument range 0-10 m with\n"
            "setpoints in percent (95/90/30/15).\n"
            "Correct: declare the percent-of-span\n"
            "basis or use one unit."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
