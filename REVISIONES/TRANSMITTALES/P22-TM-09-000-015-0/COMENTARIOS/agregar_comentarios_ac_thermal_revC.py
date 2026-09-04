"""
agregar_comentarios_ac_thermal_revC.py
Anota PDF AC Thermal Calculation Rev C (E31 / submittal 25007-0031).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-02 (capacity margin + n+1 confirmation)
  2. PDFs en submittal 25007-0031: 3 (AC Thermal C, Grounding C, LCP A)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden: NOTE-02

Veredicto: 2 - Approved as Noted (cierra parcialmente TM N2 OBS-02 desde 180+ dias)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-005-002_C_AC_Thermal_Calc.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 31",
        "P22-CD-09-005-002_C AC Thermal Calculation.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Two items to resolve prior to IFC (Rev 0):\n"
            "1) Selected capacity 2.5 HP = 2.01 TR is\n"
            "   0.03 TR below the calculated demand\n"
            "   with 15% margin (2.04 TR). Demonstrate\n"
            "   the gap is absorbed by control logic\n"
            "   or upsize to next standard increment.\n"
            "2) Specify each A/C unit individually as\n"
            "   2.5 HP capable of holding 100% of the\n"
            "   calculated load with the partner in\n"
            "   standby ('1 Duty + 1 Standby, each\n"
            "   rated at full load').\n"
            "Closes TM N2 OBS-02 partially (180+ days)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
