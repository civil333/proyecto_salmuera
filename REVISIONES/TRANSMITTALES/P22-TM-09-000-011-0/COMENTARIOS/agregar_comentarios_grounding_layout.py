"""
agregar_comentarios_grounding_layout.py
Agrega anotaciones FreeText del TM N11 al PDF Grounding Point & Power Panel Location Layout Rev B.
Observaciones:
  OBS-03 (MAYOR): Posiciones de panel/grounding derivan de Piping Layout rechazado en TM N7
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-007-003_Rev.B_Grounding_Layout.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-007-003_Rev.B_Grounding_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 21",
        "P22-DWG-09-007-003_Rev.B Grounding Point & Power Panel Location Layout.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 21.")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "GROUNDING",
        "page_fallback": 2,
        "text": (
            "OBS-03 (MAJOR): Panel and grounding point\n"
            "positions reflect a non-conforming equipment\n"
            "arrangement. Rev B is derived from Piping\n"
            "Layout Rev A (P22-DWG-09-005-004), rejected\n"
            "in Transmittal N7 (11,150 mm submitted vs.\n"
            "<=3,500 mm required per TM N5).\n"
            "Resubmit as Rev C after Equipment Layout\n"
            "and Piping Layout are accepted by ADASA."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
