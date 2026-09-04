"""
agregar_comentarios_line_list.py
Agrega anotaciones FreeText del TM N12 al PDF Line List Rev B.
Observaciones:
  NOTE-01 (NOTE): Linea Make-Up for CIP sin LINE NO.
  NOTE-02 (NOTE): Notacion "SCH80" debe ser "SCH 80S" para lineas SSD (ASME B36.19M)
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-LI-09-009-003_B_Line List.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-LI-09-009-003_B_Line List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_23 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 23"))
    matches = glob_module.glob(os.path.join(entrega_23, "P22-LI-09-009-003*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 23 con patron P22-LI-09-009-003*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "MAKE-UP FOR CIP",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Missing LINE NO.\n"
            "'Make-Up for CIP' (PVC SCH80, DN80,\n"
            "P&ID Sheet P9) has no LINE NO. assigned.\n"
            "Assign identifier per project numbering\n"
            "convention prior to IFC (Rev 0)."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "SUPER DUPLEX STEEL",
        "page_fallback": 1,
        "text": (
            "NOTE-02: Schedule designation.\n"
            "SSD lines show 'SCH80' without 'S' suffix.\n"
            "Per ASME B36.19M, duplex/stainless pipe\n"
            "schedule = 'Schedule 80S'.\n"
            "Wall thicknesses (DN100: 8.56mm,\n"
            "DN80: 7.62mm, DN65: 6.02mm) confirm 80S.\n"
            "Correct notation to 'SCH 80S' prior to\n"
            "IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
