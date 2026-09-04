"""
agregar_comentarios_instrument_layout.py
Agrega anotaciones FreeText del TM N11 al PDF Instrument Location Layout Rev B.
Observaciones:
  OBS-04 (MAYOR): Posiciones de instrumentos CIP/antiscalant derivan de Piping Layout rechazado en TM N7
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-008-001_REV.B_Instrument_Location_Layout.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-008-001_REV.B_Instrument_Location_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 21",
        "P22-DWG-09-008-001_REV.B Instrument Location Layout.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 21.")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": "CIP",
        "page_fallback": 2,
        "text": (
            "OBS-04 (MAJOR): Instrument positions in\n"
            "the CIP/antiscalant external area reflect\n"
            "a non-conforming equipment arrangement.\n"
            "Rev B is derived from Piping Layout Rev A\n"
            "(P22-DWG-09-005-004), rejected in TM N7\n"
            "(11,150 mm vs. <=3,500 mm per TM N5).\n"
            "Resubmit as Rev C after Equipment Layout\n"
            "and Piping Layout are accepted by ADASA.\n"
            "Internal container positions (22 items)\n"
            "may be preserved if unchanged."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
