"""
agregar_comentarios_turbo1.py
Agrega anotaciones FreeText del TM N11 al PDF Datasheet Feed Turbocharger Rev D — P22-ET-09-009-007.
Nota: TM N6 OBS-01 (coupling pressure) CERRADO — Style S/X 1800 psi confirmado.
      TM N10 OBS-06 (vibration mounting) CERRADO — row 38 confirma mounting surface.
Observaciones:
  NOTE-03 (NOTE): Etiqueta "STYLE 77" en plano outline inconsistente con datasheet Style S/X aceptado
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-ET-09-009-007_REV.D Datasheet of Feed Turbocharger.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-ET-09-009-007_REV.D Datasheet of Feed Turbocharger_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_20 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 20"))
    matches = glob_module.glob(os.path.join(entrega_20, "P22-ET-09-009-007*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 20 con patron P22-ET-09-009-007*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": "GROOVE",
        "page_fallback": 5,
        "text": (
            "NOTE-03: Outline drawing HPB-60 labels\n"
            "connections as 'CUT GROOVE STYLE 77'.\n"
            "Accepted coupling is Style S/X at\n"
            "1800 psi (datasheet attached).\n"
            "Style 77 is a different product with\n"
            "a different pressure rating.\n"
            "Update outline drawing label to\n"
            "'Style S' in next revision to prevent\n"
            "field installation errors."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
