"""
agregar_comentarios_cip_cartridge.py
Anota PDF Datasheet of CIP Cartridge Filter Rev C (E45 / 25007-0045).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.13: OBS-01 + OBS-02 + OBS-03 + OBS-04 = 4
  2. PDFs en submittal 25007-0045: 2 (este es 1 de 2 Code 3)
  3. Cross-cutting: OBS-01/02/04 = mismas que Section 2.12; OBS-03 propia CIP pH
  4. len(COMENTARIOS) = 4
  5. IDs coinciden: Section 2.13 del transmittal TM N19

Veredicto: 3 - To be revised (CRITICAL cambio H-V pre-NT-001 + gasket pH 2-12)
Colores: fill transmite severidad (CRITICAL rojo / MAYOR naranja).
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-ET-09-009-006_C_CIP_Cartridge_Filter.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-009-006_C_CIP_Cartridge_Filter_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 45",
        "P22-ET-09-009-006-C_Datasheet of CIP Cartridge Filter.pdf",
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
        "fill": CRITICAL,
        "search": "Vertical",
        "page_fallback": 0,
        "text": (
            "OBS-01: Horizontal-to-vertical change.\n"
            "Same condition as Section 2.12 OBS-01\n"
            "(RO Cartridge Filter). Item under ADASA\n"
            "review in Technical Note\n"
            "P22-NT-09-000-001-0, issued in parallel.\n"
            "Note clarification 5.E requires written\n"
            "confirmation that container tie-in\n"
            "positions remain identical to the\n"
            "approved design after the change. Rev C\n"
            "materialises the change before ADASA's\n"
            "formal position is issued. Re-issue as\n"
            "Rev D once ADASA responds; procurement\n"
            "action on the alternative configuration\n"
            "remains at BW Water's risk under the\n"
            "Technical Offer Rev1 vendor list."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Sysflo",
        "page_fallback": 0,
        "text": (
            "OBS-02: Vendor change Filtrek -> Sysflo.\n"
            "Same condition as Section 2.12 OBS-02.\n"
            "Provide the technical equivalence\n"
            "document and pre-approval request per\n"
            "Technical Note clarification 5.D before\n"
            "any commitment to Sysflo, covering\n"
            "filtration performance, housing\n"
            "pressure rating, gasket compatibility\n"
            "with CIP fluids, lead time and after-\n"
            "sales support comparable to or\n"
            "exceeding the Filtrek baseline."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-03: FRP housing and gasket\n"
            "compatibility with CIP cycle pH 2-12.\n"
            "CIP cycle uses acidic cleaning (citric\n"
            "acid pH 2-3) and basic cleaning (NaOH\n"
            "pH 11-12). FRP housings and elastomer\n"
            "gaskets have well-known compatibility\n"
            "envelopes; the datasheet should declare\n"
            "explicitly the gasket material selected\n"
            "(EPDM, FKM, NBR or equivalent) and its\n"
            "compatibility with the pH range and\n"
            "with the planned commercial cleaning\n"
            "chemicals. Add the gasket material and\n"
            "the chemical compatibility statement\n"
            "in Rev D."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-04: Updated as-built drawing of\n"
            "the container not delivered. Same\n"
            "condition as Section 2.12 OBS-03;\n"
            "shared deliverable for both cartridge\n"
            "filter datasheets. Submit the updated\n"
            "drawing as a separate deliverable\n"
            "showing the vertical configuration\n"
            "(footprint, operator access, vertical\n"
            "clearance for cartridge removal) and\n"
            "confirming tie-in positions remain at\n"
            "the same locations as the approved\n"
            "design."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
