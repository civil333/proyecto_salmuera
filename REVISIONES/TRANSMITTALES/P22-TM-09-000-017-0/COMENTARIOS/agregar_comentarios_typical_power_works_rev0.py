"""
agregar_comentarios_typical_power_works_rev0.py
Anota PDF Typical Installation Details of Power Works Rev 0 (E36 / submittal 25007-0036).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-01, NOTE-02
  2. PDFs en submittal 25007-0036: 4 (este script cubre Typical Power Works)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 2
  5. IDs coinciden con .md transmittal: NOTE-01 / NOTE-02

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-005_0_Typical_Power_Works.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-005_0_Typical_Power_Works_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 36",
        "P22-DWG-09-007-005_0 Typical Installation Details of Power Works.pdf",
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
        "fill": MAYOR,
        "search": "NEC Article 392.30(B)",
        "page_fallback": 2,
        "text": (
            "NOTE-01: All notes cite the\n"
            "US National Electrical Code (NEC) -\n"
            "Articles 392.30(B), 352, Table\n"
            "250.122. The applicable regulation\n"
            "for installation in Chile is the\n"
            "SEC and NCh Electrica 4/2003 / IEC\n"
            "60364, also basis for the SEC\n"
            "compliance Hold Point in the ITP\n"
            "Offsite (item 7.7). Confirm in\n"
            "writing that design intent is to\n"
            "satisfy SEC/NCh requirements with\n"
            "NEC cited as supplementary good\n"
            "practice, not governing standard.\n"
            "Where standards diverge (e.g.\n"
            "ground wire cross-section sizing),\n"
            "Chilean regulation must prevail."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "Pump motor grounding have 2 method",
        "page_fallback": 9,
        "text": (
            "NOTE-02: Page 10 note 5\n"
            "lists two alternative methods for\n"
            "pump motor grounding: (a) ground\n"
            "wire from motor structure to cable\n"
            "tray / skid; (b) ground wire of the\n"
            "motor power cable terminated in the\n"
            "motor terminal box ground terminal.\n"
            "Leaving both alternatives open lets\n"
            "the electrical subcontractor mix\n"
            "criteria across HP Pump, CIP Pump\n"
            "and Antiscalant Dosing Pumps.\n"
            "Select one standard method for the\n"
            "project and document it in the\n"
            "installation procedure prior to\n"
            "site works."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
