"""
agregar_comentarios_itp_offsite.py
Anota PDF ITP Offsite Rev B (E44 / 25007-0044).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.10: OBS-01 + NOTE-01 = 2
  2. PDFs en submittal 25007-0044: 3 (este es 1 de 3 Code 3 docs)
  3. Cross-cutting con NT-001 6.A/6.C ASME X
  4. len(COMENTARIOS) = 2
  5. IDs coinciden: Section 2.10 del transmittal TM N19

Veredicto: 3 - To be revised (CRITICAL silencio sobre ASME X)
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
    SCRIPT_DIR, "P22-BA-09-000-004_B_ITP_Offsite.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-004_B_ITP_Offsite_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 44",
        "P22-BA-09-000-004_B_ITP.pdf",
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
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-01: ASME X certification scope\n"
            "for RO Pressure Vessels.\n"
            "BW Water Technical Offer Rev1 ITP\n"
            "(Section 12, page 100, line 3905)\n"
            "commits 'Test certification to ASME X'\n"
            "with rating '1000 PSI SWRO / 300 PSI\n"
            "BWRO'. Actual system is UHPRO at\n"
            "1800 psi (ET Section 5.1.6). The 22-May\n"
            "Mitigation Plan proposed eliminating\n"
            "the stamp; ADASA position is reserved\n"
            "in Technical Note P22-NT-09-000-001-0\n"
            "(issued in parallel) clarifications\n"
            "6.A and 6.C. The contracted scope\n"
            "cannot be revised by omission in the\n"
            "ITP. Re-issue as Rev C declaring\n"
            "explicitly the ASME X certification\n"
            "scope, unless a formal Change Order\n"
            "modifies it."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: NDE Plan delivery date.\n"
            "Response to TM N17 OBS-03 defers\n"
            "procedure codes (NDE, PMI, Hydrostatic,\n"
            "Preservation, FAT) to a separate\n"
            "submittal. Provide a delivery schedule\n"
            "with firm dates for each procedure,\n"
            "including the NDE Plan, prior to IFC\n"
            "Rev 0. The Hold Point pre-dispatch\n"
            "per ET Section 8.1 cannot be released\n"
            "without these procedures on file."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
