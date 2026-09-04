"""
agregar_comentarios_ac_thermal.py
Anota PDF AC Thermal Calculation Rev C (E40 / submittal 25007-0040, 19 paginas).

NOTA (re-disposicion 18-May-2026): AC Thermal Calc Rev C = Code 1 - Approved
(calculo correcto; solo se pide indicar el margen efectivo explicito). Code 1
NO lleva CC_ADASA (regla CLAUDE.md section 3.8). Este script y su _CC_ADASA.pdf
NO se emiten; traza interna. El entregable residual (declarar margen efectivo
+13.3% en IFC Rev 0) se trackea en la Seccion 3 del transmittal.

Checklist (CLAUDE.md section 3.8):
  1. Tabla NOTE del transmittal Section 2.4: NOTE-01 = 1
  2. PDFs en submittal 25007-0040: 1
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden: Section 2.4 del transmittal TM N18

Veredicto: 2 - Approved as Noted (cierra TM N15 NOTE-02: n+1 confirmado +
margen justificado). Calculo en pagina 2; CCS en pagina 3.
Texto sin etiqueta de criticidad; fill transmite severidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-005-002_C_AC_Thermal_Calc.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 40",
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
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "2.5 HP air-conditioning",
        "page_fallback": 2,
        "text": (
            "NOTE-01: n+1 confirmed; capacity margin\n"
            "justified -- closes TM N15 NOTE-02. The\n"
            "CCS confirms each 2.5 HP unit carries\n"
            "100% load (1 duty + 1 standby). Selected\n"
            "2.01 TR exceeds the un-margined peak\n"
            "1.774 TR by +13.3%; the 'within the\n"
            "applied design margin' wording is\n"
            "imprecise (the 0.03 TR is the erosion\n"
            "of that margin).\n"
            "\n"
            "Action to issue at IFC Rev 0 -- no new\n"
            "AC Thermal Calculation revision\n"
            "required:\n"
            "1) State the effective post-selection\n"
            "   margin explicitly (2.01 TR vs\n"
            "   computed peak 1.774 TR = +13.3%)\n"
            "   instead of the imprecise wording.\n"
            "n+1 is confirmed; ADASA accepts the\n"
            "calculation at IFC Rev 0 once item 1\n"
            "is incorporated."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
