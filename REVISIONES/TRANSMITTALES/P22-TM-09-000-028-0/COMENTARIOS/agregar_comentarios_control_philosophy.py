"""
agregar_comentarios_control_philosophy.py
Plant Control Philosophy Rev E (TM N28, Code 2). len = 5
(OBS-01/02/03/04 MAYOR + NOTE-01). Documento de texto (61 pags, rot=0).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_E_Plant_Control_Philosophy.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_E_Plant_Control_Philosophy_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 65",
        "P22-BT-09-009-001_E Plant Control Philospphy.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL); print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}"); sys.exit(1)

COMENTARIOS = [
    {"id": "OBS-01", "fill": MAYOR,
     "search": "RO HP Pump Bearing Temperature Sensor", "page_fallback": 37,
     "text": ("OBS-01: this table tags TE-09-001 as\n"
              "Bearing and TE-09-002 as Winding (and\n"
              "TE-09-003/004 for the CIP pump) - the reverse\n"
              "of the Alarm and Interlock List Rev C, the IO\n"
              "List Rev 5 and the Instrument List, which set\n"
              "winding = TE-09-001 (trip 140C) and bearing =\n"
              "TE-09-002 (trip 95C). Mislabels a safety\n"
              "sensor. Correct: mirror the Instrument List -\n"
              "winding TE-09-001/003, bearing TE-09-002/004.")},
    {"id": "OBS-02", "fill": MAYOR,
     "search": "Class B insulation", "page_fallback": 40,
     "text": ("OBS-02: motor winding Alarm 130 / Trip 155C\n"
              "and bearing 80 / 95C do not match the governing\n"
              "Alarm and Interlock List (winding 120/140,\n"
              "bearing 90/95). A 155C winding trip is a Class\n"
              "F value, inconsistent with the 'Class B\n"
              "insulation' cited here (limit ~130C).\n"
              "Correct: reconcile the values to the Alarm\n"
              "List and confirm the winding trip against the\n"
              "motor insulation class.")},
    {"id": "OBS-03", "fill": MAYOR,
     "search": "High-high trip: 7.1 mm/s", "page_fallback": 41,
     "text": ("OBS-03: HP pump vibration High 4.5 / trip\n"
              "7.1 mm/s stated here differs from the governing\n"
              "Alarm and Interlock List (VIT-09-001 AH 7.0 /\n"
              "AHH 10.0); the turbo trips also differ (7.1 vs\n"
              "6.0). Correct: reconcile the vibration alarm\n"
              "and trip pairs to a single vendor-confirmed\n"
              "basis, aligned to the Alarm List (see the\n"
              "Alarm List OBS-01: its 10.0 mm/s trip is above\n"
              "the transmitter's 8.9 range).")},
    {"id": "OBS-04", "fill": MAYOR,
     "search": "discharge pressure below 45 bar", "page_fallback": 42,
     "text": ("OBS-04: the sustained low-pressure protection\n"
              "described here (discharge < 45 bar for > 5 s\n"
              "trips BH-09-001; < 50 bar for > 3 s early\n"
              "warning) is not reflected in the Alarm and\n"
              "Interlock List (PIT-09-002 carries only AL 40 /\n"
              "ALL 34). Correct: add the 45 bar/5 s trip and\n"
              "50 bar/3 s warning to the Alarm List, or remove\n"
              "them here if superseded by ALL 34.")},
    {"id": "NOTE-01", "fill": NOTE,
     "search": "Table of Reference Documents", "page_fallback": 7,
     "text": ("NOTE-01: pin the now-issued children by code\n"
              "and rev in this table (Control and Sequence\n"
              "Chart P22-LI-09-008-017 Rev A, Alarm and\n"
              "Interlock List P22-LI-09-008-015 Rev C). Tag\n"
              "typos elsewhere: FIT-09-003 cited for the RO\n"
              "Stage 2 permeate flow (should be FIT-09-002),\n"
              "and antiscalant valves VE-09-014/010 (should\n"
              "be VE-09-014/016).")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
