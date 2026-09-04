"""
agregar_comentarios_io_list.py
Anota PDF IO List Rev 3 (TM N24). len(COMENTARIOS) = 4 (OBS-01 + OBS-02 + NOTE-01 + NOTE-02).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_3_IO_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_3_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 53",
        "P22-LI-09-008-001_3 IO List.pdf",
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
        "fill": NOTE,
        "search": "SYSTEM ENABLE COMMAND FROM DCS",
        "page_fallback": 2,
        "text": (
            "OBS-01: module-to-external-PLC interface\n"
            "= 4 relay-contact signals.\n"
            "Present (keep):\n"
            "1) ENABLE from DCS - XA005 (DI)\n"
            "2) RUNNING to DCS - YA001 (DO)\n"
            "Add (new ADASA requirement):\n"
            "3) FAULT STATUS to DCS (DO)\n"
            "4) LOCAL/REMOTE STATUS to DCS (DO)"
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "MOTORIZED VALVE",
        "page_min": 3,
        "page_fallback": 3,
        "text": (
            "NOTE-02: the Valve List and the P&ID needed\n"
            "to cross-check the VE-09 motorized-valve\n"
            "I/O are not part of this submittal; the\n"
            "cross-check is tracked."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 3,
        "text": (
            "OBS-02: items 130 and 135 (dosing-pump\n"
            "RUNNING) are missing the signal-type count\n"
            "cell carried by every other point.\n"
            "Correct: complete the count cell at IFC\n"
            "Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 3,
        "text": (
            "NOTE-01: the soft-I/O scheme over\n"
            "Ethernet/IP (DI relabelled BOOL) was\n"
            "accepted at Transmittal N20 and is not\n"
            "reopened; the hardwired relay interface\n"
            "applies to the external-PLC signals only."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
