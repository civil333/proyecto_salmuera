"""
agregar_comentarios_alarm_interlock.py
Alarm and Interlock List Rev C (TM N28, Code 2). len = 4
(OBS-01/02 MAYOR + NOTE-01/02). Tablas anchas A3, rot=0.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-015_C_Alarm_Interlock_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-015_C_Alarm_Interlock_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 65",
        "P22-LI-09-008-015_C Alarm and Interlock List.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL); print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}"); sys.exit(1)

COMENTARIOS = [
    {"id": "OBS-01", "fill": MAYOR,
     "search": "RO HP Pump Vibration Transmitter", "page_fallback": 2,
     "text": ("OBS-01: VIT-09-001 high-high trip is set at\n"
              "10.0 mm/s on a transmitter ranged 0 to 8.9\n"
              "mm/s rms, so it saturates at 8.9 and the trip\n"
              "'Stop HP Pump' can never fire. The Control\n"
              "Philosophy requires a high-high vibration trip\n"
              "of the HP pump. Correct: bring the high-high\n"
              "trip within the transmitter range (e.g. per\n"
              "ISO 20816), or re-range the transmitter in the\n"
              "Instrument List and confirm the value.")},
    {"id": "OBS-02", "fill": MAYOR,
     "search": "MCCB", "page_fallback": 6,
     "text": ("OBS-02: the incoming-breaker alarm is tagged\n"
              "P22-PLC01-XT001 'MCCB Tripped' (action: RO\n"
              "System Stop), but the IO List Rev 5 has no\n"
              "XT001 - the point is P22-PLC01-XA001 'MCCB\n"
              "Close States'. The tag does not resolve\n"
              "against the IO List in a system-stop interlock.\n"
              "Correct: align the tag and description to the\n"
              "IO List (breaker open contact = tripped).")},
    {"id": "NOTE-01", "fill": NOTE,
     "search": "RO HP Pump Vibration Transmitter", "page_fallback": 2,
     "text": ("NOTE-01: tag and completeness alignments -\n"
              "the HP pump vibration tag reads VIT-09-001 here\n"
              "but VT-09-001 in the IO List and Control\n"
              "Philosophy (unify to the Instrument List); and\n"
              "the IO List has FAULT points for VE-09-014,\n"
              "VE-09-016 and the two dosing pumps that are not\n"
              "alarmed here - confirm whether those faults\n"
              "should be announced.")},
    {"id": "NOTE-02", "fill": NOTE,
     "search": "Turbocharger", "page_fallback": 5,
     "text": ("NOTE-02: declare the numeric setpoint of the\n"
              "turbocharger boost-failure differential\n"
              "((PIT-09-007 - PIT-09-005), the Sequence Chart\n"
              "uses a 10 bar jump); unify the FIT-09-005\n"
              "sub-tags (.FAHH/.FAH vs the .AHH/.AH pattern);\n"
              "renumber the duplicated item numbers (5.7,\n"
              "13.4); and confirm the TIT-09-006 range (0-600C\n"
              "for a 0-100C tank service).")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
