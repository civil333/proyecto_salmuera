"""
agregar_comentarios_power_cable.py
Anota PDF Power Cable Schedule Rev B (E42 / 25007-0042).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.2: OBS-01 = 1
  2. PDFs en submittal 25007-0042: 7 (este es 1 de los Code 2)
  3. Cross-cutting: vincula con Single Line Diagram Rev B (Section 2.4)
  4. len(COMENTARIOS) = 1
  5. ID coincide: Section 2.2 del transmittal TM N19

Veredicto: 2 - Approved as noted (resubmittal Rev A Code 1 TM N3)
Color: fill MENOR (amarillo) — OBS-01 severidad MINOR.
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-007-002_B_Power_Cable_Schedule.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-007-002_B_Power_Cable_Schedule_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 42",
        "P22-LI-09-007-02_B Power Cable Schedule.pdf",
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
        "fill": MENOR,
        "search": "REL-001",
        "page_fallback": 0,
        "text": (
            "OBS-01: REL-001 CIP Heater two-cable\n"
            "arrangement not aligned with the Single\n"
            "Line Diagram Rev B. Clarify in Rev 0 the\n"
            "REL-001 topology consistently across the\n"
            "Single Line Diagram and the Cable\n"
            "Schedule — either one feed via VFD with\n"
            "control signals on a separate row, or a\n"
            "dedicated control panel drawn explicitly.\n"
            "No new Cable Schedule revision required;\n"
            "address at IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
