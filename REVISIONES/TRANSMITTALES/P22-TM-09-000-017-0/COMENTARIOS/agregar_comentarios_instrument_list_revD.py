"""
agregar_comentarios_instrument_list_revD.py
Anota PDF Instrument List Rev D (E37 / submittal 25007-0037).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01, NOTE-01, NOTE-02, NOTE-03
  2. PDFs en submittal 25007-0037: 1 (este script lo cubre)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 4
  5. IDs coinciden con .md transmittal: OBS-01 / NOTE-01 / NOTE-02 / NOTE-03

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-003_D_Instrument_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-003_D_Instrument_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 37",
        "P22-LI-09-008-003_D Instrument List.pdf",
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
        "search": "PCH420V-M12",
        "page_fallback": 1,
        "text": (
            "OBS-01: Wilcoxon model\n"
            "PCH420V-M12 declared range\n"
            "0-8.9 mm/s rms for VT-09-001\n"
            "(item 7), VT-09-002 (item 18) and\n"
            "VT-09-003 (item 19). Standard\n"
            "PCH420V-M12 datasheet shows\n"
            "programmable full-scale 12.7-127\n"
            "mm/s. Confirm model variant\n"
            "supports 0-8.9 mm/s scaling with\n"
            "vendor citation, or revise model\n"
            "selection. Mirrors Section 2.2\n"
            "NOTE-02 on Data Transfer List."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "Monel",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Rev D introduces\n"
            "material upgrades for high-TDS\n"
            "service: DPS-09-001 -> Monel;\n"
            "FIT-09-001 -> Nickel Alloy 276 +\n"
            "PTFE Lining; PI-09-001/002 ->\n"
            "Superduplex 2507 diaphragm seal.\n"
            "Hastelloy C extension for PIT-001\n"
            "to 005 already covered by\n"
            "Section 2.3 OBS-01. Confirm cost\n"
            "and lead-time impact on\n"
            "Equipment Procurement Schedule\n"
            "in writing."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": "Feed Turbocharger",
        "page_fallback": 1,
        "text": (
            "NOTE-02: VT-09-002 (item\n"
            "18, Feed Turbocharger) and\n"
            "VT-09-003 (item 19, Interstage\n"
            "Turbocharger) declare Working\n"
            "Medium 'Filtered Water'.\n"
            "VT-09-001 (item 7, HP Pump)\n"
            "leaves the column as '-'.\n"
            "Vibration sensors are mounted on\n"
            "the motor casing and do not\n"
            "contact a process fluid - column\n"
            "should read '-' for all three.\n"
            "Harmonise on IFC."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": MENOR,
        "search": "Brackish Water Reverse Osmosis Project",
        "page_fallback": 2,
        "text": (
            "NOTE-03: Consolidated\n"
            "Comment Sheet header (pages 3-4)\n"
            "references 'Brackish Water Reverse\n"
            "Osmosis Project / 25006 /\n"
            "25006-WTP-000-IC-LST-00002'.\n"
            "Cover sheet and page 2 correctly\n"
            "identify the document as\n"
            "P22-LI-09-008-003 / Second Stage\n"
            "RO Module for Brine - PD Taltal /\n"
            "25007. Replace comment-sheet\n"
            "header before next revision."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
