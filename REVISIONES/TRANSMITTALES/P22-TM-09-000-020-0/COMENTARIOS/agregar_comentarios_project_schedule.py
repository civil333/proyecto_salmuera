"""
agregar_comentarios_project_schedule.py
Anota PDF Project Schedule Rev A (TM N20). Gantt: pag 1 portada (rot 0),
pag 2+ gantt (rot 90). El skill normaliza la rotacion automaticamente.
len(COMENTARIOS) = 2 (OBS-01 portada + OBS-02 fase fabricacion/test).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-001_A_Project_Schedule.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-001_A_Project_Schedule_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-BA-09-000-001_A Project Schedule.pdf",
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
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-01: the programme is silent on the RO\n"
            "pressure vessel certification basis - the\n"
            "23-Jun ex-works date is the non-stamped\n"
            "route under the ADASA waiver of\n"
            "02-Jun-2026 and must be stated. Correct:\n"
            "declare the certification basis at IFC\n"
            "Rev 0; the 09-Jun baseline adoption is\n"
            "not re-opened."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: no vessel pressure-test activity\n"
            "visible - factory hydrostatic (1800 psi\n"
            "x 1.1 per Protec letter) and pre-FAT\n"
            "system hydrostatic tests are required as\n"
            "dated activities. Correct: add both at\n"
            "IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
