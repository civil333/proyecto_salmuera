"""
agregar_comentarios_lcp_revA.py
Anota PDF Datasheet Local Control Panel (LCP) Rev A (E31 / submittal 25007-0031).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS del transmittal: OBS-01 (I/O modules + RTD), OBS-02 (IP rating), OBS-03 (PLC consumption)
  2. PDFs en submittal 25007-0031: 3
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 3
  5. IDs coinciden: OBS-01, OBS-02, OBS-03 (Section 2.4 del transmittal)

Veredicto: 3 - To be revised
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-007-005_A_LCP_Datasheet.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-ET-09-007-005_A_LCP_Datasheet_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 31",
        "P22-ET-09-007-005_A Datasheet of Local Control Panel (LCP).pdf",
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
            "Required:\n"
            "- Number of CompactLogix RTD modules\n"
            "  (5069-IY4 or equivalent).\n"
            "- Channel allocation per motor:\n"
            "  TE-09-001/002 (HP Pump),\n"
            "  TE-09-003/004 (CIP Pump).\n"
            "- Validate universal-input architecture\n"
            "  closed in TM N14 (TE designation,\n"
            "  no 4-20 mA loop) is in panel BoM.\n"
            "Resolve in Rev B."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Cover sheet leaves both fields blank.\n"
            "ADASA expects IP54 minimum (coastal\n"
            "Taltal, salt deposition, container\n"
            "interior).\n"
            "Specify ambient design temperature\n"
            "consistent with ET Container HVAC\n"
            "(both A/C units operational).\n"
            "Justify any rating below IP54."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Load List Rev A: 1.0 kW.\n"
            "AC Thermal Calc Rev C: 0.14 kW.\n"
            "LCP datasheet: not declared.\n"
            "Confirm actual nominal absorbed power\n"
            "and propagate consistently across the\n"
            "three documents prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
