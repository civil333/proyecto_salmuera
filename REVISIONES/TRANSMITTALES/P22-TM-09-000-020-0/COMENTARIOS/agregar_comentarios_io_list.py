"""
agregar_comentarios_io_list.py
Anota PDF IO List Rev 2 (TM N20).
len(COMENTARIOS) = 3 (OBS-01 + NOTE-01 + NOTE-02).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-001_2_IO_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-001_2_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-LI-09-008-001_2 IO List.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "Noted",
        "page_fallback": 1,
        "text": (
            "OBS-01: the TM N19 conditional acceptance\n"
            "was contingent on Plant Control Philosophy\n"
            "Rev D, not delivered within the fourteen-\n"
            "day window - acceptance reverts to Code 3\n"
            "by its own terms. Correct: deliver Rev D\n"
            "and confirm signal consistency (re-issue\n"
            "or confirm Rev 2 unchanged)."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "127",
        "page_fallback": 4,
        "text": (
            "NOTE-01: item numbering gaps (127 to 129;\n"
            "133 to 135). Correct: renumber\n"
            "contiguously or confirm no signal was\n"
            "dropped."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "Issued for Construction",
        "page_fallback": 2,
        "text": (
            "NOTE-02: revision-history lists Rev 0 and\n"
            "Rev 1 only - add the Rev 2 row. Dosing\n"
            "pump RUNNING (items 131/137) is labelled\n"
            "DI while routed over Ethernet/IP - flag as\n"
            "soft I/O."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
