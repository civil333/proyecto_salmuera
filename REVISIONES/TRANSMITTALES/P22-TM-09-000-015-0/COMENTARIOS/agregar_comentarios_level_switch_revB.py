"""
agregar_comentarios_level_switch_revB.py
Anota PDF Datasheet Level Switch Rev B (E30 / submittal 25007-0030).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-01 (4-20mA HART vs IO-Link template error)
  2. PDFs en submittal 25007-0030: 1 (Level Switch DS Rev B)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden con .md transmittal: NOTE-01

Veredicto: 1 - Approved (con NOTE menor)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-008_B_Level_Switch.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-008_B_Level_Switch_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 30",
        "P22-LI-09-008-008_B Datasheet - Level Switch.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "Outputs/Inputs Communication",
        "page_fallback": 0,
        "text": (
            "Cover sheet reads '4-20mA HART'\n"
            "(template default).\n"
            "IFM KQ6005 is a discrete capacitive\n"
            "switch with PNP output / IO-Link, not\n"
            "a HART analog instrument.\n"
            "IO List Rev C correctly classifies\n"
            "LS-09-001 / LS-09-002 as DI.\n"
            "Correct field to 'PNP discrete /\n"
            "IO-Link' prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
