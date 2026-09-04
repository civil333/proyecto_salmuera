"""
agregar_comentarios_lcp_datasheet.py
Anota PDF Datasheet of Local Control Panel (LCP) Rev B (TM N20).
len(COMENTARIOS) = 1 (OBS-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-ET-09-007-005_B_LCP_Datasheet.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-007-005_B_LCP_Datasheet_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 46",
        "P22-ET-09-007-005_B Datasheet of Local Control Panel (LCP).pdf",
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
        "search": "NEMA 4x",
        "page_min": 2,
        "page_fallback": 2,
        "text": (
            "OBS-01: total panel power consumption not\n"
            "declared at panel level; Electrical Load\n"
            "List Rev 0 carries SAI-09-001 at 2.0 kW.\n"
            "Correct: state the design consumption at\n"
            "IFC Rev 0. This datasheet governs the\n"
            "enclosure specification - the Outline\n"
            "Panel Drawing must align to it."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
