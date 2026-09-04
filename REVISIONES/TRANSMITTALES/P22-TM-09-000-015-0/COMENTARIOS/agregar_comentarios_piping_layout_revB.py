"""
agregar_comentarios_piping_layout_revB.py (v2)
Anota PDF Piping Layout Rev B (E32 / submittal 25007-0032).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-06 (doors), NOTE-07 (cabinet),
     NOTE-08 (flanged), NOTE-09 (elevation)
     (OBS-02 footprint WITHDRAWN by ADASA - inline en §2.6, no anotado en PDF)
  2. PDFs en submittal 25007-0032: 4
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 4
  5. IDs coinciden: NOTE-06..09 (Section 2.6 del transmittal)

Veredicto: 2 - Approved as Noted (v2 cambio desde Code 3)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_B_Piping_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_B_Piping_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 32",
        "P22-DWG-09-005-004_B Piping Layout.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-06",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "Sheets 2 and 4 show pedestrian door only.\n"
            "Both doors are mandatory per ET Container\n"
            "Access Requirements; their position\n"
            "constrains piping routing along the\n"
            "corresponding container walls.\n"
            "Add prior to IFC (Rev 0).\n"
            "Outstanding from TM N7 OBS-03."
        ),
    },
    {
        "id": "NOTE-07",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 3,
        "text": (
            "Sheet 4 shows the LCP as a separate unit\n"
            "external to the module envelope.\n"
            "Cable routing, conduit penetrations and\n"
            "FAT scope (panel installed at FAT vs\n"
            "shipped separately) not documented.\n"
            "Confirm prior to IFC (Rev 0).\n"
            "Outstanding from TM N7 OBS-04."
        ),
    },
    {
        "id": "NOTE-08",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "Antiscalant injection (AS-PVC-DN15-09-035)\n"
            "and CIP make-up (CP-PVC-DN80-09-019)\n"
            "should be ANSI-flanged to allow site\n"
            "connection without on-site PVC welding.\n"
            "Confirm flanged terminations or document\n"
            "the alternative prior to IFC (Rev 0)."
        ),
    },
    {
        "id": "NOTE-09",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Tie-in points (feed inlet, permeate,\n"
            "concentrate, CIP supply/return) are\n"
            "dimensioned in plan view; elevation\n"
            "references absent.\n"
            "Add a tie-in elevation summary table\n"
            "or section drawing prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
