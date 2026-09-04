"""
agregar_comentarios_hp_pump.py
Agrega anotaciones FreeText del TM N11 al PDF Datasheet HP Feed Pump Rev D — P22-ET-09-009-002.
Observaciones:
  NOTE-02 (NOTE): Inconsistencia fabricante motor (GE vs ABB or equivalent)
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-ET-09-009-002_REV.D Datasheet of RO HP Feed Pump.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-ET-09-009-002_REV.D Datasheet of RO HP Feed Pump_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_20 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 20"))
    matches = glob_module.glob(os.path.join(entrega_20, "P22-ET-09-009-002*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 20 con patron P22-ET-09-009-002*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "ABB or equivalent",
        "page_fallback": 3,
        "text": (
            "NOTE-02: Motor manufacturer inconsistency.\n"
            "Component Datasheet shows 'GE' while\n"
            "FEDCO pump data shows 'ABB or equivalent'.\n"
            "These fields describe the same motor.\n"
            "Reconcile in Datasheet Rev E and confirm\n"
            "actual manufacturer once procurement\n"
            "is complete."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
