"""
agregar_comentarios_io_list.py
IO List Rev 5 (TM N28, Code 2). len = 1 (OBS-01 MAYOR).
Tabla alta A3, rot=0. NOTE cross-doc (tags, Valve List) van a Seccion 3, no se anotan.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_5_IO_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_5_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 66",
        "P22-LI-09-008-001_5 IO List.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL); print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}"); sys.exit(1)

COMENTARIOS = [
    {"id": "OBS-01", "fill": MAYOR,
     "search": "CIP TANK", "page_fallback": 2,
     "text": ("OBS-01: the Alarm and Interlock List commands\n"
              "a 'Stop heater' interlock on the CIP tank\n"
              "heater (REL-09-001) and controls its\n"
              "temperature to 30-35C, but this list carries\n"
              "no output channel (DO/BOOL) for the heater.\n"
              "Correct: add the CIP heater start/stop output\n"
              "(and run/fault feedback if applicable), or\n"
              "confirm in writing that the heater is\n"
              "controlled outside the module PLC - in which\n"
              "case this list is correct as issued and the\n"
              "item transfers to the Alarm and Interlock List.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
