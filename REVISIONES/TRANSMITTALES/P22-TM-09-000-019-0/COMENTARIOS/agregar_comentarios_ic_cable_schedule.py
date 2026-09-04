"""
agregar_comentarios_ic_cable_schedule.py
Anota PDF Instrumentation & Control Cable Schedule Rev 0 (E44 / 25007-0044).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.11: OBS-01 + OBS-02 + NOTE-01 + NOTE-02 = 4
  2. PDFs en submittal 25007-0044: 3 (este es 1 de 3)
  3. Cross-cutting: dependencia Control Philosophy Rev D (Section 3 carry-fwd)
  4. len(COMENTARIOS) = 4
  5. IDs coinciden: Section 2.11 del transmittal TM N19

Veredicto: 3 - To be revised (primer review, 4 OBS)
Colores: fill transmite severidad (MAYOR naranja / MENOR amarillo).
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-002_0_IC_Cable_Schedule.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-002_0_IC_Cable_Schedule_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 44",
        "P22-LI-09-008-002_0 I&C Cable Schedule.pdf",
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
        "search": "PANEL INTERIOR WIRE",
        "page_fallback": 0,
        "text": (
            "OBS-01: VFD communications internal\n"
            "panel wiring without specification.\n"
            "Items 9-14 (HP Pump VFD comms) and\n"
            "66-71 (CIP Pump VFD comms) are listed\n"
            "as 'PANEL INTERIOR WIRE' without cable\n"
            "type, cross-section or shielding. VFD-\n"
            "PLC bus (Ethernet/IP or Modbus TCP/IP)\n"
            "requires shielded cable (Cat 5e/6 STP)\n"
            "plus twisted-pair signal cables for any\n"
            "auxiliary discrete or analogue signals.\n"
            "Declare in Rev 1 the cable type, cross-\n"
            "section and shielding for VFD comms,\n"
            "consistent with the Datasheet of Power\n"
            "and Control Cable Rev B."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: Dosing pumps cable assignment.\n"
            "Items 82-85 assign cable to dosing\n"
            "pumps BDS09-001/002. HP Pump and CIP\n"
            "Pump each carry an XB001 IN REMOTE\n"
            "status bit on the PLC interface; the\n"
            "dosing pumps in the IO List Rev 1 do\n"
            "not declare an equivalent IN REMOTE\n"
            "status, and the schedule assigns 'CTRL'\n"
            "cable without specifying signals.\n"
            "Align the cable assignment with the IO\n"
            "List Rev 1 signal map, confirming\n"
            "whether IN REMOTE will be added or\n"
            "declaring the reduced signal set."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "NOTE-01: Level switch nomenclature.\n"
            "Items 80 and 81 list 'DI' cables to\n"
            "level switches without distinguishing\n"
            "LSH (level switch high) and LSL (level\n"
            "switch low); the IO List Rev 1 items\n"
            "122 and 123 declare LSH and LSL\n"
            "explicitly. Use the same identifiers\n"
            "(LSH / LSL) on the cable schedule for\n"
            "field cable identification."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "NOTE-02: PHIT09-006 tag identifier.\n"
            "Items 74 and 75 list pH/ORP analyser\n"
            "cables, but the tag identifier is\n"
            "incomplete in some rows due to merged\n"
            "cells. Repeat the full tag on every\n"
            "row so the schedule is field-readable\n"
            "without ambiguity."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
