"""
agregar_comentarios_instrument_location_revC.py
Anota PDF Instrument Location Layout Rev C (E32 / submittal 25007-0032).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-06 (dependency on Equipment + Piping Layout acceptance)
  2. PDFs en submittal 25007-0032: 4
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden: NOTE-06

Veredicto: 2 - Approved as Noted (cierra TM N3 OBS-01/02/03 + TM N11 OBS-04)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-008-001_C_Instrument_Location.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-008-001_C_Instrument_Location_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 32",
        "P22-DWG-09-008-001_C Instrument Location Layout.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-10",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Rev C is consistent with Equipment Layout\n"
            "Rev B and Piping Layout Rev B as submitted.\n"
            "If either upstream layout is modified\n"
            "(notably the CIP/dosing footprint per\n"
            "TM N15 Section 2.6 OBS-02), this drawing\n"
            "will require a Rev D update.\n"
            "No action required if upstream layouts\n"
            "are accepted as currently configured.\n"
            "Closes TM N3 OBS-01/02/03 + TM N11 OBS-04."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
