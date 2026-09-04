"""
agregar_comentarios_antiscalant.py
Agrega anotaciones FreeText del TM N10 al PDF GA Antiscalant Dosing Tank Rev A.
Observaciones:
  OBS-05 (MAYOR): Volumen y especificacion de material del estanque no indicados — TM N9 OBS-02 abierta
"""
import sys, os, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-015_REV.A GA of Antiscalant Dosing Tank.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-015_REV.A GA of Antiscalant Dosing Tank_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18",
        "P22-DWG-09-005-015_REV.A GA of Antiscalant Dosing Tank.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-05",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-05 (MAJOR): Notes section is blank.\n"
            "Rev B must add:\n"
            "- Total volume: 0.34 m3 / working: 0.27 m3\n"
            "- Body and liner material\n"
            "- Anchor bolt pattern and seismic loads\n"
            "  (ET Seismic Conditions, NCh 2369\n"
            "  Zone 3, 2025 ed.)\n"
            "(TM N9 OBS-02 still open)"
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
