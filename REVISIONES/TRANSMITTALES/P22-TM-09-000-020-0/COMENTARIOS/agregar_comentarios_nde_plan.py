"""
agregar_comentarios_nde_plan.py
Anota PDF NDE Plan Rev A (TM N20).
len(COMENTARIOS) = 3 (OBS-01 + OBS-02 + OBS-03).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-005_A_NDE_Plan.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-005_A_NDE_Plan_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-BA-09-000-005_A NDE Plan.pdf",
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
        "fill": CRITICAL,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: no RO pressure vessel scope -\n"
            "factory hydrostatic test at rating\n"
            "(1800 psi x 1.1 per Protec Arisawa\n"
            "letter), the certification basis agreed\n"
            "in the ADASA waiver of 02-Jun-2026, the\n"
            "documentation dossier and witness\n"
            "arrangement are absent. Correct:\n"
            "incorporate the vessel test scope (or\n"
            "reference the dedicated hydrostatic\n"
            "procedure) in Rev B."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: no ADASA witness or hold points\n"
            "declared; the Technical Specification\n"
            "(Inspections During Manufacturing)\n"
            "reserves ADASA right to witness PMI and\n"
            "key tests (Punto W). Correct: add W/H\n"
            "point column in Rev B."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Edition",
        "page_fallback": 3,
        "text": (
            "OBS-03: governing code editions left as\n"
            "placeholders and plan titled general.\n"
            "Correct: state editions and confirm\n"
            "project-specific coverage, including\n"
            "UT/RT acceptance basis for Super Duplex\n"
            "butt welds, in Rev B."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
