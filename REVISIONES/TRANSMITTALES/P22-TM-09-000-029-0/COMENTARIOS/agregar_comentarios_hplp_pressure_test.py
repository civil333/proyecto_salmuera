"""
agregar_comentarios_hplp_pressure_test.py
HP and LP Pressure Test Procedure Rev D (TM N29, Code 2). len = 1 (NOTE-01).
El error critico de 75 bar/PVC del N27 esta RESUELTO (verificado en el cuerpo y
la Line List embebida); el unico residual es fijar la edicion ASME (Seccion 3.1/
3.2, pagina 4). PDF chico -> run_comentarios estandar.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-010_D_HP_LP_Pressure_Test.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-010_D_HP_LP_Pressure_Test_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 67",
        "25007-0067", "P22-BA-09-000-010_D HP and LP Pressure Test Procedure.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL); print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}"); sys.exit(1)

COMENTARIOS = [
    {"id": "NOTE-01", "fill": NOTE,
     "search": "Applicable Edition", "page_fallback": 3,
     "text": ("NOTE-01: Sections 3.1 and 3.2 cite ASME Section V\n"
              "(Article 1) and ASME B31.3 as 'Applicable\n"
              "Edition/Addenda' without fixing the edition.\n"
              "Correct: state the applicable edition and addenda\n"
              "of ASME Section V and ASME B31.3 to be used for\n"
              "the tests. The critical test-pressure error of\n"
              "Rev C (75 bar on the PVC line) is resolved and\n"
              "verified; the HP hydrostatic test remains a Hold\n"
              "Point.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
