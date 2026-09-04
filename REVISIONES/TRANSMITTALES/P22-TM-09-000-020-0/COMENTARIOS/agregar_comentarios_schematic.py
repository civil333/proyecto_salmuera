"""
agregar_comentarios_schematic.py
Anota PDF PLC-LCP Schematic Diagram Rev A (TM N20). Plano 71 paginas.
len(COMENTARIOS) = 1 (NOTE-01 en portada).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-CD-09-008-002_A_Schematic.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-CD-09-008-002_A_Schematic_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 46",
        "P22-CD-09-008-002_A PLC-LCP Schematic Diagram.pdf",
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
            "NOTE-01: acceptance conditional on Plant\n"
            "Control Philosophy Rev D - any signal\n"
            "divergence introduced by Rev D propagates\n"
            "to panel wiring and terminal assignments.\n"
            "Correct: confirm the I/O assignment\n"
            "against Rev D once delivered; spare I/O\n"
            "capacity should absorb signal-level\n"
            "changes."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
