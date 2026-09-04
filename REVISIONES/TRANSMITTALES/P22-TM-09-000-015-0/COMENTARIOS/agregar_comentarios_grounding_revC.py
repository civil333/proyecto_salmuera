"""
agregar_comentarios_grounding_revC.py
Anota PDF Grounding Point & Power Panel Location Layout Rev C (E31 / submittal 25007-0031).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-03 (grounding schedule completeness)
  2. PDFs en submittal 25007-0031: 3
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden: NOTE-03

Veredicto: 2 - Approved as Noted (cierra parcialmente TM N11 OBS-03)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-003_C_Grounding_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-003_C_Grounding_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 31",
        "P22-DWG-09-007-003_C Grounding Point & Power Panel Location Layout.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "Drawing shows position layout but lacks\n"
            "a companion grounding schedule.\n"
            "Rev D should include:\n"
            "- PE point identifiers (PE-09-001, etc.)\n"
            "- Conductor cross-section per circuit\n"
            "  (Cu bare, mm-sq).\n"
            "- Ring main interconnection topology.\n"
            "- Equipotential bonding to container\n"
            "  structural steel.\n"
            "- Connection to ADASA external mesh.\n"
            "Required by NCh Elec 4/2003 §10.0.\n"
            "Closes TM N11 OBS-03 partially."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
