"""
agregar_comentarios_visual_procedure.py
Anota PDF Visual Procedure Rev A (TM N20).
len(COMENTARIOS) = 3 (OBS-01 + OBS-02 + NOTE-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-008_A_Visual_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-008_A_Visual_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-BA-09-000-008_A Visual procedure.pdf",
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
        "fill": MENOR,
        "search": "QC Engineer",
        "page_fallback": 4,
        "text": (
            "OBS-01: VT inspector qualification not\n"
            "stated. Correct: align with the NDE Plan\n"
            "personnel basis (SNT-TC-1A VT Level II or\n"
            "ISO 9712) at IFC Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "thermoplastic",
        "page_fallback": 3,
        "text": (
            "OBS-02: scope includes thermoplastic\n"
            "welds but no thermoplastic acceptance\n"
            "criteria cited. Correct: add DVS 2202-1\n"
            "visual acceptance or exclude\n"
            "thermoplastics at IFC Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "QAM",
        "page_fallback": 3,
        "text": (
            "NOTE-01: referenced QAM forms and\n"
            "procedures not attached. Correct: list\n"
            "them as controlled external references\n"
            "at IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
