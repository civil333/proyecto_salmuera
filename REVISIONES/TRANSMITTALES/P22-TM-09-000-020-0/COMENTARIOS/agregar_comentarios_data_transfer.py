"""
agregar_comentarios_data_transfer.py
Anota PDF Data Transfer List (Modbus TCP/IP) Rev 1 (TM N20).
len(COMENTARIOS) = 2 (OBS-01 + NOTE-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-004_1_Data_Transfer_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-004_1_Data_Transfer_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 46",
        "P22-LI-09-008-004_1 Data Transfer List (Modbus TCPIP).pdf",
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
        "search": "30019",
        "page_fallback": 4,
        "text": (
            "OBS-01: register 30019 (CIT09-002)\n"
            "declares scale 0-20 uS/cm - cannot\n"
            "represent the 200-1000 uS/cm permeate\n"
            "service nor the Alarm List AHH 800 uS/cm;\n"
            "instrument span is 0-20000 uS/cm\n"
            "(0-20 mS/cm). Register 30021 (CIT09-003,\n"
            "0-20 mS/cm) uses a different unit\n"
            "convention. Correct: harmonise both\n"
            "registers to one declared span and unit\n"
            "at IFC Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "TIT09-006",
        "page_fallback": 4,
        "text": (
            "NOTE-01: TIT09-006 register declares\n"
            "0-600 C. Correct: confirm the intended\n"
            "span at IFC Rev 0 (Pt100 element range\n"
            "vs CIP service)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
