"""
agregar_comentarios_io_list_rev0.py
Anota PDF IO List Rev 0 (E35 / submittal 25007-0035).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-01, NOTE-02, NOTE-03
  2. PDFs en submittal 25007-0035: 4 (este script cubre IO List)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 3
  5. IDs coinciden con .md transmittal: NOTE-01 / NOTE-02 / NOTE-03

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_0_IO_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_0_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 35",
        "P22-LI-09-008-001_0 IO List.pdf",
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
        "search": "ANTISCALANT DOS. PUMP 1 START COMMAND",
        "page_fallback": 3,
        "text": (
            "NOTE-01: Antiscalant Dosing\n"
            "Pumps BDS-09-001/002 (items 124-131)\n"
            "lack IN REMOTE digital input.\n"
            "HP Pump (item 28) and CIP Pump\n"
            "(item 104) include this status.\n"
            "Add IN REMOTE DI on Rev 0\n"
            "operational baseline so DCS applies\n"
            "consistent permissive logic across\n"
            "all pumps."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": "RO HP PUMP WINDING TEMPERATURE ELEMENT",
        "page_fallback": 1,
        "text": (
            "NOTE-02: RTD range declared\n"
            "as '0 - 100 dOhm' in items 39, 40,\n"
            "114, 115. Restate in degrees C with\n"
            "Pt-100 reference (60 C / 138 Ohm to\n"
            "180 C / 168 Ohm) so operator and\n"
            "DCS engineer read the physical\n"
            "magnitude directly. Coherent with\n"
            "Alarm and Interlock List which uses\n"
            "degrees C for the same instruments."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": MENOR,
        "search": "CIP PUMP WINDING TEMPERATURE ELEMENT",
        "page_fallback": 3,
        "text": (
            "NOTE-03: Items 114 and 115\n"
            "(CIP Pump RTDs) reference P&ID page\n"
            "P9 (HP Pump section). CIP Pump is\n"
            "on page P10. Correct on Rev 0\n"
            "operational baseline."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
