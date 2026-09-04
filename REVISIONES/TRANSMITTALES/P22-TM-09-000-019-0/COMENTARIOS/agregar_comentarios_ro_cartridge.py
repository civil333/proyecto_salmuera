"""
agregar_comentarios_ro_cartridge.py
Anota PDF Datasheet of RO Cartridge Filter Rev D (E45 / 25007-0045).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.12: OBS-01 + OBS-02 + OBS-03 = 3
  2. PDFs en submittal 25007-0045: 2 (este es 1 de 2 Code 3)
  3. Cross-cutting con NT-001 5.A-5.E (mismas banderas que CIP)
  4. len(COMENTARIOS) = 3
  5. IDs coinciden: Section 2.12 del transmittal TM N19

Veredicto: 3 - To be revised (CRITICAL cambio unilateral H-V pre-NT-001)
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
    SCRIPT_DIR, "P22-ET-09-009-005_D_RO_Cartridge_Filter.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-009-005_D_RO_Cartridge_Filter_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 45",
        "P22-ET-09-009-005_D_Datasheet of RO Cartridge Filter.pdf",
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
            "Item under ADASA review in Technical\n"
            "Note P22-NT-09-000-001-0, issued in\n"
            "parallel with this transmittal. Note\n"
            "clarification 5.E requires written\n"
            "confirmation that the container\n"
            "interface positions (feed brine inlet,\n"
            "permeate outlet, reject outlet,\n"
            "drainages, chemical supply lines and\n"
            "service lines) remain identical to the\n"
            "approved design after the change. Rev D\n"
            "materialises the change before ADASA's\n"
            "formal position on the 22-May\n"
            "Mitigation Plan is issued. Re-issue as\n"
            "Rev E once ADASA responds; procurement\n"
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
            "Technical Offer Rev1 line 619 attached\n"
            "Filtrek as the cartridge filter vendor.\n"
            "Any vendor substitution under an 'or\n"
            "equal' clause requires ADASA written\n"
            "pre-approval before the substitute is\n"
            "committed, with a technical equivalence\n"
            "justification (filtration performance,\n"
            "housing pressure rating, gasket\n"
            "compatibility with brine and CIP, lead\n"
            "time, after-sales support). Provide the\n"
            "equivalence document and pre-approval\n"
            "request per Technical Note clarification\n"
            "5.D before any commitment to Sysflo."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-03: Updated as-built drawing of\n"
            "the container not delivered. Technical\n"
            "Note P22-NT-09-000-001-0 clarification\n"
            "5.C requires the updated as-built\n"
            "drawing of the container showing the\n"
            "new vertical configuration: footprint,\n"
            "operator access for cartridge\n"
            "replacement, vertical clearance for\n"
            "cartridge removal, and confirmation\n"
            "that the container tie-ins remain at\n"
            "the same positions as the approved\n"
            "design. Submit the updated drawing as\n"
            "a separate deliverable referenced by\n"
            "this Datasheet at Rev E."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
