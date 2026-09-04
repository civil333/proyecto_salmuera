"""
agregar_comentarios_hp_lp_pressure.py
Anota PDF HP and LP Pressure Test Procedure Rev B (TM N26, Code 3). len(COMENTARIOS) = 3
(OBS-01 MAYOR + OBS-02 MENOR + NOTE-01). Colores: fill transmite severidad; el texto
FreeText arranca directo con "OBS-XX:" / "NOTE-01:" sin etiqueta de criticidad.
Paginas 0-based: OBS-01=6 (impresa 7, 5.5.12 defiere al line list), OBS-02=7
(impresa 8, 5.6.5 faltante), NOTE-01=8 (impresa 9, report form ausente).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-010_B_HP_LP_Pressure_Test.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-010_B_HP_LP_Pressure_Test_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 61",
        "P22-BA-09-000-010_B HP and LP Pressure Test Procedure.pdf",
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
        "search": "Minimum test pressure 1.5 X design pressure",
        "page_fallback": 6,
        "text": (
            "OBS-01: the body omits the numeric test\n"
            "pressure (135 bar HP / 7.5 bar LP fixed by\n"
            "the ITP) and does not reconcile the HP design\n"
            "pressure (90 bar ITP vs up to 120 bar ET);\n"
            "both steps defer to the line list, leaving the\n"
            "result indeterminate.\n"
            "Correct: state the design pressure per\n"
            "subsystem with a cited source and write the\n"
            "resulting numeric test pressure in the body."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "Prior to commencement of pneumatic testing",
        "page_fallback": 7,
        "text": (
            "OBS-02: the reversion was corrected but step\n"
            "5.6.5 is still missing (5.6.4 jumps to 5.6.6)\n"
            "and subsection 5.7.2 skips 5.7.2.2.\n"
            "Correct: renumber contiguously."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 8,
        "text": (
            "NOTE-01: the Pressure Test Report form is not\n"
            "in this delivery; attach it at the next\n"
            "submittal so any pre-printed pressure\n"
            "matches 135 bar HP / 7.5 bar LP."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
