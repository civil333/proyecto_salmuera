"""
agregar_comentarios_grounding.py
Anota PDF Grounding & Power Panel Location Layout Rev E (E42 / 25007-0042).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.5: OBS-01 + OBS-02 + NOTE-01 = 3
  2. PDFs en submittal 25007-0042: 7 (este es 1 de 3 Code 3 documents)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 3
  5. IDs coinciden: Section 2.5 del transmittal TM N19

Veredicto: 3 - To be revised (legacy items TM N11 / N15 / N17 no respondidos)
Colores: fill transmite severidad (MAYOR naranja / MENOR amarillo).
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-003_E_Grounding.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 42",
        "P22-DWG-09-007-003_E Grounding Point & Power Panel "
        "Location Layout.pdf",
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
            "OBS-01: Grounding schedule completeness.\n"
            "TM N11 OBS-03 (~70 days) and TM N15\n"
            "NOTE-03 required a complete grounding\n"
            "schedule: PE identifiers, conductor\n"
            "cross-section per load, ring-main\n"
            "topology and equipotential bonding per\n"
            "NCh Elect. 4/2003 Section 10.0. Rev E\n"
            "Consolidated Comment Sheet does not\n"
            "include it. Provide complete schedule\n"
            "in Rev F, integrated on the drawing or\n"
            "as a referenced annex.\n"
            "Third consecutive transmittal carrying\n"
            "the schedule open."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-02: Revision history block content.\n"
            "Rev E lists revision dates (Rev B\n"
            "2-Mar-2026, C 17-Apr-2026, D 30-Apr-2026,\n"
            "E 12-May-2026) but omits the description\n"
            "of changes and the ECN reference per\n"
            "revision. Add description of changes\n"
            "and ECN (if applicable) for each Rev\n"
            "from B to E in Rev F."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "NOTE-01: Consolidated Comment Sheet\n"
            "legibility. The CCS on Rev E is\n"
            "partially illegible on the version\n"
            "received (table fragmented in\n"
            "extraction). Re-issue the PDF from the\n"
            "electronic source so the CCS reads in\n"
            "full; export future CCS as searchable\n"
            "text rather than rasterised scans."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
