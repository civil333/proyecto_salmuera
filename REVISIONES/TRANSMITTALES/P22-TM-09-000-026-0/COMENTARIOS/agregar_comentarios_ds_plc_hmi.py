"""
agregar_comentarios_ds_plc_hmi.py
Anota el Datasheet of PLC and HMI Panel Component Rev C (TM N26, Code 2 -
Approved as Noted). len(COMENTARIOS) = 2 (NOTE-01 + NOTE-02). Colores: fill
transmite severidad (NOTE = azul). Texto sin etiqueta de criticidad.

Paginas (0-based) verificadas contra el .md extraido:
  NOTE-01 -> pag 0  (portada; codigo en cajetin 'P22 - ET - 09 - 008 - 01')
  NOTE-02 -> pag 35 (pagina 36 impresa: datasheet de componente anadido, cabecera
             'P22-ET-09-008-001', item '4 Model - 5069-IY4' sin cantidad)
Documento de 50 paginas.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import NOTE, run_comentarios

# --- Fast-save guard -------------------------------------------------------
# run_comentarios() guarda con garbage=4, deflate=True. En este datasheet
# (Rockwell/Allen-Bradley embebido, imagenes ya comprimidas) esa recompresion
# total no converge (>min). Se fuerza un guardado equivalente y valido
# (garbage=1, deflate=False): mismas anotaciones, sin recomprimir streams.
import fitz
_orig_save = fitz.Document.save
def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)
fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-008-01_C_DS_PLC_HMI.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-ET-09-008-01_C_DS_PLC_HMI_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 58",
        "P22-ET-09-008-01_C Datasheet of PLC and HMI Panel Component "
        "(Major Component).pdf",
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
        "fill": NOTE,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: the document code is\n"
            "inconsistent within the file - the cover\n"
            "and most headers read 'P22-ET-09-008-01'\n"
            "while the added analog-module page and\n"
            "the comment sheet read 'P22-ET-09-008-001'\n"
            "(the register code). Correct: align to\n"
            "'P22-ET-09-008-001' on the cover and all\n"
            "headers at IFC Rev 0."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 35,
        "text": (
            "NOTE-02: this component page states the\n"
            "5069-IY4 module type without a quantity;\n"
            "the 8 motor Pt-100 channels need two\n"
            "5069-IY4 modules per the approved LCP\n"
            "Datasheet Rev 1. Confirm the LCP Datasheet\n"
            "governs the quantity at issue."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
