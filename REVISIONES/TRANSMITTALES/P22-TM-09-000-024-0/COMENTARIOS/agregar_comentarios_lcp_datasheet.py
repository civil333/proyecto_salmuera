"""
agregar_comentarios_lcp_datasheet.py
Anota PDF Datasheet of Local Control Panel (LCP) Rev 0 (TM N24).
len(COMENTARIOS) = 3 (NOTE-01 enclosure + OBS-01 power + OBS-02 code). HART retirado (over-reach).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-007-005_0_LCP_Datasheet.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-ET-09-007-005_0_LCP_Datasheet_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 53",
        "P22-ET-09-007-005_0 Datasheet of Local Control Panel (LCP).pdf",
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
        "search": "NEMA 4X",
        "page_min": 3,
        "page_fallback": 3,
        "text": (
            "NOTE-01: the enclosure (SS316L, NEMA 4X /\n"
            "IP66) reconfirms the correct marine\n"
            "specification; the contradiction tracked\n"
            "since Transmittal N20 resides in the\n"
            "Outline Panel Drawing, not this datasheet."
        ),
    },
    {
        "id": "OBS-01",
        "fill": MENOR,
        "search": "FEEDER",
        "page_min": 114,
        "page_fallback": 114,
        "text": (
            "OBS-01: the aggregated power list covers\n"
            "only the thirteen valve feeders, not the\n"
            "panel's own internal consumption; the\n"
            "2.0 kW figure is not tied to the UPS\n"
            "SAI-09-001 sizing. Correct: reconcile at\n"
            "IFC Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "P22-DWG-09-007",
        "page_min": 115,
        "page_fallback": 115,
        "text": (
            "OBS-02: code-type inconsistency - the cover\n"
            "page carries the ET code P22-ET-09-007-005\n"
            "while these sheets carry a DWG code.\n"
            "Correct: unify to P22-ET-09-007-005 across\n"
            "the body."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
