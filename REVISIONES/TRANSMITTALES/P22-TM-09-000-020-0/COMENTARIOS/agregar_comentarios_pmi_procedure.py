"""
agregar_comentarios_pmi_procedure.py
Anota PDF PMI Procedure Rev A (TM N20).
len(COMENTARIOS) = 3 (OBS-01 + OBS-02 + NOTE-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-006_A_PMI_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-006_A_PMI_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-BA-09-000-006_A PMI Procedure.pdf",
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
        "search": "EXTENT",
        "page_fallback": 7,
        "text": (
            "OBS-01: ET requirement not declared -\n"
            "PMI on at least 10 percent of the Super\n"
            "Duplex high-pressure circuit components,\n"
            "UNS S32750 conformity as acceptance\n"
            "basis, ADASA witness right (Punto W).\n"
            "Correct: add the project scoping clause\n"
            "at IFC Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "PTS",
        "page_fallback": 8,
        "text": (
            "OBS-02: embedded subcontractor procedure\n"
            "scoped to refinery services (PTS, HF\n"
            "acid, fired heaters) not applicable to\n"
            "this module. Correct: add a project-\n"
            "applicability statement at IFC Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "PERSONAL QUALIFICATIONS",
        "page_fallback": 2,
        "text": (
            "NOTE-01: cover qualification clause is\n"
            "copied from the NDE Plan (refers to non-\n"
            "destructive examination personnel).\n"
            "Correct: replace with the PMI operator\n"
            "qualification defined in the body (OEM\n"
            "training + Owner-approved mock-up)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
