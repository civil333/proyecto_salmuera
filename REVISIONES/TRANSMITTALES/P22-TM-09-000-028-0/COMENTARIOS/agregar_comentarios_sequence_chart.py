"""
agregar_comentarios_sequence_chart.py
Control and Sequence Chart Rev A (TM N28, Code 2). len = 7
(OBS-01..05 MAYOR + OBS-06 MENOR + NOTE-01). A4 apaisado, rot=0.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-017_A_Control_Sequence_Chart.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-017_A_Control_Sequence_Chart_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 65",
        "P22-LI-09-008-017_A Control and Sequence Chart.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL); print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}"); sys.exit(1)

COMENTARIOS = [
    {"id": "OBS-01", "fill": MAYOR,
     "search": "Low TDS value", "page_fallback": 6,
     "text": ("OBS-01: Note 5 states the turbocharger bypass\n"
              "VE-09-002 activates on a 'Low TDS value', but\n"
              "the Control Philosophy governs this valve by\n"
              "the pressure control loop ('TDS shall not\n"
              "directly initiate bypass'); the '(SP:62 Bar)'\n"
              "here is already a pressure. Correct: reword the\n"
              "trigger to PIT-09-005 (second-stage feed\n"
              "pressure); TDS only selects the pressure SP.")},
    {"id": "OBS-02", "fill": MAYOR,
     "search": "exceeds 90 bar", "page_fallback": 6,
     "text": ("OBS-02: the Stage-2 over-pressure abort here\n"
              "fires at PIT-09-005 > 90 bar, but the Alarm and\n"
              "Interlock List sets the abort (Stop + open\n"
              "VE-09-002) at AHH 93 bar; 90 bar is only the AH\n"
              "warning. Correct: reconcile to 93 bar and cite\n"
              "the tag/SP.")},
    {"id": "OBS-03", "fill": MAYOR,
     "search": "Ramp Up", "page_fallback": 6,
     "text": ("OBS-03: the VFD ramp is stated as 1 Hz/s,\n"
              "but the Control Philosophy limits it to\n"
              "0.1-0.3 Hz/s (0.1 initial) to avoid hydraulic\n"
              "shock and membrane stress - 3 to 10x faster\n"
              "here. Correct: change to 0.1-0.3 Hz/s or\n"
              "justify the deviation.")},
    {"id": "OBS-04", "fill": MAYOR,
     "search": "SP: 40m3/h", "page_fallback": 8,
     "text": ("OBS-04: flushing uses a fixed 40 m3/h for\n"
              "both stages, but the Alarm and Interlock List\n"
              "sets FIT-09-005 SP1 = 48 (Stage 1) and SP3 =\n"
              "36 (Stage 1+2). Correct: use the per-stage\n"
              "setpoints from the Alarm List and declare the\n"
              "tag.")},
    {"id": "OBS-05", "fill": MAYOR,
     "search": "2nd Stage Reject CIP Return", "page_fallback": 3,
     "text": ("OBS-05: VE-09-010 is described as '2nd Stage\n"
              "Reject CIP Return', but the IO List Rev 5 and\n"
              "Alarm List set VE-09-010 = 1st Stage CIP\n"
              "Return; the Control Philosophy assigns it to\n"
              "Stage 2 - three different stage assignments.\n"
              "Correct: fix the CIP-return valve stage to the\n"
              "IO List (009 = Stage 2, 010 = Stage 1).")},
    {"id": "OBS-06", "fill": MENOR,
     "search": "Brine Flow SP", "page_fallback": 6,
     "text": ("OBS-06: setpoint/formula corrections - the\n"
              "suction step-2 permissive uses 1.5 bar (the AL\n"
              "alarm) vs SP1 1.75 bar; the normal-shutdown\n"
              "step 7 uses 'PIT-09-002 <= 0 bar', a setpoint\n"
              "absent from the Alarm List; and the Brine Flow\n"
              "SP formula carries a spurious '/100' (yields\n"
              "0.28 vs 28 m3/h). Correct: align to real Alarm\n"
              "List setpoints and fix the formula.")},
    {"id": "NOTE-01", "fill": NOTE,
     "search": "Control and Sequence Chart", "page_fallback": 0,
     "text": ("NOTE-01: housekeeping - PHIT-09-006 is\n"
              "labelled 'Temperature Transmitter' in the CIP\n"
              "interlocks (it is the pH analyzer); VE-09-002\n"
              "is called an 'On/Off Valve' though it is a\n"
              "modulating PID valve; renumber the duplicate\n"
              "and run-on item numbers; and correct the cover\n"
              "'Page 1 of 8' to 'of 9'.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
