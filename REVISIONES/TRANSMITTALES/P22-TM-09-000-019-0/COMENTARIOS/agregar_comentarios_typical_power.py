"""
agregar_comentarios_typical_power.py
Anota PDF Typical Installation Details of Power Works Rev C (E42 / 25007-0042).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.7: NOTE-01 = 1
  2. PDFs en submittal 25007-0042: 7 (este es 1 de los Code 2)
  3. Cross-cutting: cierra los 4 NOTEs TM N17 Section 2.5
  4. len(COMENTARIOS) = 1
  5. ID coincide: Section 2.7 del transmittal TM N19

Veredicto: 2 - Approved as noted (Rev C cierra los 4 NOTEs TM N17)
Color: fill MENOR (amarillo) — NOTE-01 severidad MINOR.
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-005_C_Typical_Power_Works.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-005_C_Typical_Power_Works_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 42",
        "P22-DWG-09-007-005_C Typical Installation Details of Power Works.pdf",
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
        "fill": MENOR,
        "search": None,
        "page_fallback": 9,
        "text": (
            "NOTE-01: Designate explicitly which of\n"
            "the seven grounding methods shown on\n"
            "this page applies as the typical\n"
            "solution for each load type per\n"
            "IEC 60364-5-54 (METHOD 1 to METHOD 7).\n"
            "Add the mapping at IFC Rev 0 — no new\n"
            "revision required."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
