"""
agregar_comentarios_io_list.py
Anota PDF I/O List Rev 1 IFC (E43 / 25007-0043).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.8: OBS-01 + OBS-02 + NOTE-01 + NOTE-02 = 4
  2. PDFs en submittal 25007-0043: 1 (este es Code 2 IFC)
  3. Cross-cutting: OBS-02 depende de Plant Control Philosophy Rev D (Section 3)
  4. len(COMENTARIOS) = 4
  5. IDs coinciden: Section 2.8 del transmittal TM N19

Veredicto: 2 - Approved as noted (aceptacion condicional contingente
en aprobacion Plant Control Philosophy Rev D + addendum si hay divergencia).
Colores: fill MAYOR (naranja) para OBS-01/02 / MENOR (amarillo) para NOTEs.
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-001_1_IO_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-001_1_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 43",
        "P22-LI-09-008-001_1 IO List.pdf",
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
            "OBS-01: Analyser power-supply voltage\n"
            "discrepancy carried from TM N14 NOTE-02\n"
            "(~80 days open). The Rev 1 Consolidated\n"
            "Comment Sheet does not address whether\n"
            "the analysers operate on 220 VAC or\n"
            "24 VDC; the Instrument List Rev D and\n"
            "the Datasheet sheets must agree. Reconcile\n"
            "the analyser power-supply voltage with\n"
            "the Instrument List Rev D at IFC Rev 0\n"
            "— no new I/O List revision required if\n"
            "the change is editorial."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "IFC",
        "page_fallback": 0,
        "text": (
            "OBS-02: IFC submission while Plant\n"
            "Control Philosophy Rev D remains under\n"
            "Code 3 (TM N18 carry-forward). ADASA\n"
            "conditionally accepts the I/O List Rev 1\n"
            "as Code 2 contingent upon (a) approval\n"
            "of Plant Control Philosophy Rev D and\n"
            "(b) an addendum addressing any signal\n"
            "divergence introduced by Rev D before\n"
            "IFC Rev 0. Material divergence in Rev D\n"
            "reverts this acceptance to Code 3."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: VFD frequency and accumulated\n"
            "energy variables on HP Pump and CIP Pump\n"
            "Ethernet/IP interface are not declared\n"
            "explicitly in the Rev 1 register map.\n"
            "Add these two variables to the\n"
            "Ethernet/IP mapping at IFC Rev 0,\n"
            "consistent with the VFD Datasheet."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": "IN REMOTE",
        "page_fallback": 0,
        "text": (
            "NOTE-02: IN REMOTE status bit for dosing\n"
            "pumps not declared in Rev 1 — asymmetric\n"
            "with HP Pump and CIP Pump (XB001).\n"
            "Declare the IN REMOTE status for the\n"
            "dosing pumps at IFC Rev 0, or document\n"
            "the reduced signal set explicitly."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
