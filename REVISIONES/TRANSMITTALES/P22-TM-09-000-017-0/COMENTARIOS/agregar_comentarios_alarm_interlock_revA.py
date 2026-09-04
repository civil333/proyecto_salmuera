"""
agregar_comentarios_alarm_interlock_revA.py
Anota PDF Alarm and Interlock List Rev A (E36 / submittal 25007-0036).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02
  2. PDFs en submittal 25007-0036: 4 (este script cubre Alarm & Interlock)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 5
  5. IDs coinciden con .md transmittal: OBS-01/02/03 / NOTE-01/02

Veredicto: 3 - To Be Revised (CRITICAL setpoint unit error en permeate
conductivity y inconsistencia LSL/LSH en LS-09-002)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-015_A_Alarm_Interlock_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-015_A_Alarm_Interlock_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 36",
        "P22-LI-09-008-015_A Alarm & Interlock List.pdf",
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
        "fill": CRITICAL,
        "search": "RO Train Permeate Conductivity",
        "page_fallback": 2,
        "text": (
            "OBS-01: Permeate\n"
            "conductivity setpoints two orders\n"
            "of magnitude above operating range.\n"
            "Item 11 (CIT-09-002) operating\n"
            "range 0-20 mS/cm but setpoints ALL=\n"
            "100, AL=200, AH=600, AHH=800 with\n"
            "units 'mS/cm'. SWRO permeate\n"
            "conductivity is typically 200-1000\n"
            "uS/cm (= 0.2-1.0 mS/cm). Same\n"
            "error in item 19 (CIT-09-003).\n"
            "Either divide setpoints by 1000\n"
            "(if mS/cm is intended) or change\n"
            "units column to uS/cm and adjust\n"
            "operating range accordingly."
        ),
    },
    {
        "id": "OBS-02",
        "fill": CRITICAL,
        "search": "LS-09-002",
        "page_fallback": 4,
        "text": (
            "OBS-02: Antiscalant\n"
            "Dosing Tank Level Switch logic\n"
            "inconsistent with IO List. IO List\n"
            "Rev 0 declares LS-09-001 as LSH\n"
            "(item 122) and LS-09-002 as LSL\n"
            "(item 123). This A&I List item 33\n"
            "describes LS-09-002 as 'Alarm High\n"
            "Alarm Low' with action 'Alarm +\n"
            "Stop Dosing Pump' (consistent with\n"
            "LSL dry-running protection but\n"
            "contradicts 'Alarm High' wording).\n"
            "Reconcile description with LSH/LSL\n"
            "convention of IO List on Rev B."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "Feed Turbocharger Vibration",
        "page_fallback": 2,
        "text": (
            "OBS-03: Turbocharger\n"
            "vibration action asymmetry. Item 14\n"
            "(VT-09-002 Feed Turbo AHH = 6.0\n"
            "mm/s) action: 'HMI Alarm Triggered'\n"
            "only. Item 15 (VT-09-003 Interstage\n"
            "Turbo AHH = 6.0 mm/s) action:\n"
            "'Alarm + Stop HP Pump'. Vibration\n"
            "above 6.0 mm/s on either turbo\n"
            "indicates incipient mechanical\n"
            "failure that warrants the same\n"
            "protective action; treating them\n"
            "differently can leave the Feed\n"
            "Turbo running into damage. Either\n"
            "harmonise to 'Alarm + Stop HP Pump'\n"
            "on both AHH or document engineering\n"
            "basis for the asymmetry."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "ALARM AND INTERLOCK LIST",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Digital alarms\n"
            "not tabulated. Pump and valve FAULT\n"
            "DI, MCCB trip status and\n"
            "Antiscalant Tank LSH/LSL are\n"
            "present in IO List but no alarm\n"
            "message and severity classification\n"
            "in this A&I List, which only covers\n"
            "analog instruments with setpoints.\n"
            "Either extend the list with a\n"
            "digital-alarms section (alarm\n"
            "message, severity, action) or\n"
            "document explicitly that all\n"
            "digital faults map directly to HMI\n"
            "without setpoint configuration."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": "RO HP Pump Bearing Temperature",
        "page_fallback": 3,
        "text": (
            "NOTE-02: Item 27 (TE-09-001\n"
            "RO HP Pump Bearing) declares AHH =\n"
            "90 C with action 'Alarm + Trip HP\n"
            "Pump'. For a ~100 kW HP Pump motor\n"
            "with anti-friction bearings the\n"
            "typical AHH setpoint is 95-110 C;\n"
            "90 C may be restrictive and could\n"
            "cause nuisance trips during\n"
            "sustained operation. Confirm\n"
            "against HP Pump motor manufacturer\n"
            "datasheet on Rev B."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
