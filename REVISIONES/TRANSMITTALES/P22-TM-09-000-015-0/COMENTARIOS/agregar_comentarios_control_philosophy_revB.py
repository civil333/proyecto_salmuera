"""
agregar_comentarios_control_philosophy_revB.py
Anota PDF Plant Control Philosophy Rev B (E33 / submittal 25007-0033, 51 paginas).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-13..29 = 17 totales
  2. PDFs en submittal 25007-0033: 2
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 17
  5. IDs coinciden: NOTE-13..NOTE-29 (Section 2.10 del transmittal)

Veredicto: 3 - To be revised
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_B_Control_Philosophy.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_B_Control_Philosophy_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 33",
        "P22-BT-09-009-001_B Plant Control Philosophy.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    # ==================================================================
    # NOTE-13..19 — INITIAL REVIEW (v1)
    # ==================================================================
    {
        "id": "NOTE-13",
        "fill": MAYOR,
        "search": "Cost of Energy",
        "page_fallback": 5,
        "text": (
            "Section 1.4: 4.8 kWh/m3 (TDS 43-48k),\n"
            "5.0 kWh/m3 (TDS 48-53k).\n"
            "Tech Offer Rev1 Performance: single SEC\n"
            "guarantee 4.71 kWh/m3 +/-5% with no\n"
            "TDS band differentiation.\n"
            "Clarify if Section 1.4 values are HMI\n"
            "alarm setpoints (operational) or\n"
            "performance targets (contractual).\n"
            "Align wording with Tech Offer Rev1."
        ),
    },
    {
        "id": "NOTE-14",
        "fill": MAYOR,
        "search": "high vibration",
        "page_fallback": 30,
        "text": (
            "Section 3.2.2 references 'high' and\n"
            "'high-high vibration' for VT-09-001/2/3\n"
            "without mm/s RMS values.\n"
            "Wilcoxon PCH420V-M12 supports 0-127 mm/s.\n"
            "Either incorporate ISO 10816-3 values\n"
            "(typ. 4.5 mm/s alarm, 7.1 mm/s trip,\n"
            "Class III rigid foundation) or reference\n"
            "an Alarm and Interlock Setpoints\n"
            "deliverable with formal commitment date."
        ),
    },
    {
        "id": "NOTE-15",
        "fill": MAYOR,
        "search": "antiscalant",
        "page_fallback": 25,
        "text": (
            "Section 2.3.3: ratio calculated from\n"
            "FIT-09-001 (named as 'RO inlet flow').\n"
            "P&ID Rev C and IO List Rev C identify\n"
            "FIT-09-001 as cartridge filter discharge\n"
            "(upstream of HP Pump).\n"
            "Confirm intended source (cartridge filter\n"
            "vs downstream measurement) and update."
        ),
    },
    {
        "id": "NOTE-16",
        "fill": MAYOR,
        "search": "progressively opens the brine bypass",
        "page_fallback": 36,
        "text": (
            "Section 3.2.3 states valve is\n"
            "'progressively closed to restore maximum\n"
            "energy recovery' without algorithm.\n"
            "Valve List Rev D classifies VE-09-002 as\n"
            "MODULATING ON/OFF, DN25, SDSS.\n"
            "Specify loop type (PI/PID), manipulated\n"
            "and controlled variables, gain limits,\n"
            "time response target."
        ),
    },
    {
        "id": "NOTE-17",
        "fill": MAYOR,
        "search": "CIP interface valves",
        "page_fallback": 49,
        "text": (
            "Section 4 lists CIP interface valves\n"
            "(VE-09-005/007/008/009/010/012/013) but\n"
            "open/close sequence per phase (filling,\n"
            "dosing, recirculation, drain), interlock\n"
            "matrix and hold times absent.\n"
            "Include a phase-by-phase valve state\n"
            "table cross-referenced against P&ID Rev C."
        ),
    },
    {
        "id": "NOTE-18",
        "fill": MENOR,
        "search": "Motor is protected by temperature sensor",
        "page_fallback": 33,
        "text": (
            "Section 3.2.2 defers motor temperature\n"
            "thresholds to a separate document.\n"
            "Suggest stating commissioning baseline:\n"
            "- Winding 130 C alarm / 155 C trip\n"
            "  (IEC 60034-1 Class B insulation).\n"
            "- Bearing 80 C alarm / 95 C trip.\n"
            "Reference manufacturer protection if\n"
            "different."
        ),
    },
    {
        "id": "NOTE-19",
        "fill": MENOR,
        "search": "Feed Turbocharger",
        "page_fallback": 31,
        "text": (
            "Section 3.2.2 describes SIP-09-001 in\n"
            "passive operation but does not mention\n"
            "an isolation valve before the turbo.\n"
            "Valve List Rev D does not list an\n"
            "isolation tag for SIP-09-001.\n"
            "Confirm against P&ID Rev C and document\n"
            "the isolation/shutdown approach."
        ),
    },
    # ==================================================================
    # NOTE-20..29 — Cross-check vs P&ID, Valve List, IO List, Offer Rev1.
    # Search strings anclan al parrafo correspondiente (CLAUDE.md §3.10).
    # ==================================================================
    {
        "id": "NOTE-20",
        "fill": CRITICAL,
        "search": "Turbocharger isolation valve VE-09-007",
        "page_fallback": 38,
        "text": (
            "Two issues in this permissive list:\n"
            "1) 'VE-09-007 and VE-09-007' duplicated\n"
            "   -- second entry should be another\n"
            "   valve (likely VE-09-008).\n"
            "2) 'VE-09-014 fully CLOSED' does not\n"
            "   apply -- VE-09-014 is the antiscalant\n"
            "   tank inlet (Sec 3.1.2). Interpreted\n"
            "   literally by the PLC, this blocks\n"
            "   HP Pump start whenever the tank is\n"
            "   being refilled.\n"
            "Reconcile permissive against P&ID Rev C\n"
            "and Valve List Rev D in Rev C."
        ),
    },
    {
        "id": "NOTE-21",
        "fill": MAYOR,
        "search": "(FIT-09-001) installed at the RO Stage 2",
        "page_fallback": 43,
        "text": (
            "Sec 3.1.2 defines FIT-09-001 as the\n"
            "flowmeter downstream of the cartridge\n"
            "filter (feed side, for antiscalant\n"
            "ratio). This paragraph names it as\n"
            "'Stage 2 permeate outlet' -- contradicts\n"
            "Sec 3.3.2 which identifies FIT-09-002\n"
            "as the Stage 2 Permeate Flow Transmitter.\n"
            "Correct to FIT-09-002 in Rev C or the\n"
            "PLC will read feed flow when it should\n"
            "read Stage 2 permeate, distorting\n"
            "recovery and rejection metrics."
        ),
    },
    {
        "id": "NOTE-22",
        "fill": MAYOR,
        "search": "Overall Salt Rejection",
        "page_fallback": 44,
        "text": (
            "Current formula:\n"
            "[1 - (CIT-09-002 / CIT-09-005)] * 100\n"
            "where CIT-09-005 is the Stage 2 reject.\n"
            "Per ASTM D4516 / Hydranautics /\n"
            "DuPont-Filmtec definition, salt rejection\n"
            "uses feed conductivity (CIT-09-001B) in\n"
            "the denominator, NOT reject.\n"
            "Replace CIT-09-005 with CIT-09-001B and\n"
            "recompute stage-level rejection\n"
            "consistently in Rev C."
        ),
    },
    {
        "id": "NOTE-23",
        "fill": MAYOR,
        "search": "TE-09-005",
        "page_fallback": 49,
        "text": (
            "Three TAGs appear in narrative or\n"
            "permissives but are absent from the\n"
            "instrumentation/equipment tables of the\n"
            "same group:\n"
            "- TE-09-005 (heater high-T protection,\n"
            "  Sec 3.6.4) not in Sec 3.6.2 table.\n"
            "- VE-09-006 only in HP Pump permissive\n"
            "  (Sec 3.2.2) without description.\n"
            "- VE-09-008 only in CIP return path\n"
            "  (Sec 3.6.4) not listed in Sec 3.6.2.\n"
            "Restore the TAGs to the tables or remove\n"
            "the references in Rev C."
        ),
    },
    {
        "id": "NOTE-24",
        "fill": MAYOR,
        "search": "RO Control / Sequence Chart",
        "page_fallback": 40,
        "text": (
            "Referenced as 'separate document':\n"
            "- Alarm and Control Setpoint List\n"
            "  (Sec 1.7.4, 2.2.1, 3.2.2 vibration,\n"
            "  3.2.2 motor RTD)\n"
            "- RO Control / Sequence Chart (Sec 3.3.4)\n"
            "- RO Flushing Sequence Chart (Sec 3.6.6)\n"
            "- CIP Sequence Chart (Sec 3.6.6)\n"
            "- Control Matrix (Sec 1.5.3)\n"
            "None submitted with Rev B nor committed\n"
            "with contractual delivery date.\n"
            "Provide delivery schedule for the four\n"
            "child documents against the IFC milestone,\n"
            "with document codes and revisions, in Rev C."
        ),
    },
    {
        "id": "NOTE-25",
        "fill": MAYOR,
        "search": "Total Energy Consumed",
        "page_fallback": 5,
        "text": (
            "metodologia mide el bus electrico\n"
            "equivocado.\n"
            "Sec 1.4 takes 'Total Energy' from the\n"
            "'RO PLC panel power meter' -- this meter\n"
            "only measures PLC + UPS + control gear\n"
            "(low hundreds of watts), NOT the HP Pump\n"
            "motor (~85 kW, dominant for SEC).\n"
            "The HMI will show values ~2 orders of\n"
            "magnitude off the contractual SEC of\n"
            "4.71 kWh/m3 +/-5%.\n"
            "Relocate the measurement to the MCC main\n"
            "breaker (captures loads in the SEC scope\n"
            "of Offer Rev1) or specify the meters\n"
            "whose sum is divided by the FIT-09-003\n"
            "totalizer. Complements NOTE-13 (numerical)\n"
            "with methodological correction."
        ),
    },
    {
        "id": "NOTE-26",
        "fill": MAYOR,
        "search": "PLX32-EIP-MBTCP",
        "page_fallback": 4,
        "text": (
            "Sec 1.1 describes:\n"
            "- 2 unmanaged switches 1783-USP16T\n"
            "  (star topology) -- SPoF:\n"
            "  * Switch 1 loss = HMI + VFD down\n"
            "  * Switch 2 loss = all motorized\n"
            "    valves down\n"
            "- Modbus gateway PLX32-EIP-MBTCP SPoF\n"
            "  without watchdog or fault behaviour.\n"
            "Define in Rev C:\n"
            "- Fault response of each switch\n"
            "- Gateway timeout to safe state\n"
            "- Hardwired vs Modbus prioritization\n"
            "- Consider HW redundancy if applicable."
        ),
    },
    {
        "id": "NOTE-27",
        "fill": MAYOR,
        "search": "POWER INTERRUPTION",
        "page_fallback": 5,
        "text": (
            "1) Manual mode without PLC (ET Sec 5.4):\n"
            "   plant must operate manually with the\n"
            "   PLC powered off. Sec 1.3 only describes\n"
            "   OFFLINE state under operational PLC.\n"
            "2) VFD ramp justification (ET Sec 5.4.6):\n"
            "   ramp soft-start/stop parameters must\n"
            "   be quantified and justified. Sec 3.2.2\n"
            "   only states 'ramp-up rate is limited'\n"
            "   without values or engineering basis.\n"
            "3) Sustained low pressure = rupture\n"
            "   (ET Sec 7): the philosophy must detect\n"
            "   sustained low pressure (indicative of\n"
            "   rupture) and response to failure of\n"
            "   the principal instrument (e.g. fallback\n"
            "   when PIT-09-002 fails).\n"
            "Add the three items in Rev C with\n"
            "numerical setpoints."
        ),
    },
    {
        "id": "NOTE-28",
        "fill": MAYOR,
        "search": "VE-09-003 is closed and VE-09-004",
        "page_fallback": 42,
        "text": (
            "1) Off-spec routing (Sec 3.3.4):\n"
            "   VE-09-003 closes / VE-09-004 opens\n"
            "   without 'VE-09-003 confirmed closed'\n"
            "   interlock. If VE-09-003 sticks open,\n"
            "   off-spec permeate contaminates the\n"
            "   product header while VE-09-004 routes\n"
            "   to drain -- both paths contaminated.\n"
            "2) Interstage turbo bypass (Sec 3.2.2):\n"
            "   OR trigger on PIT-09-007 without\n"
            "   cross-check vs PIT-09-008. High-fail\n"
            "   of PIT-09-007 makes both branches of\n"
            "   the OR appear normal -- bypass does\n"
            "   not open when the turbocharger needs\n"
            "   to unload.\n"
            "Add position-confirmation interlock and\n"
            "cross-check / voting in Rev C."
        ),
    },
    {
        "id": "NOTE-29",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "- TAG format: 'TE-009-001..004' and\n"
            "  'VT-009-001..003' (4-digit area) vs\n"
            "  project standard 3-digit (IO List\n"
            "  Rev C, IL Rev C use TE-09-001).\n"
            "- Triple nomenclature: AIT-09-002 /\n"
            "  CIT-09-002 / AE-09-002 used\n"
            "  interchangeably in Sec 3.3.\n"
            "- Template residue: 'blower' (Sec 2.1),\n"
            "  'Flocculation mixers' (Sec 2.1.3),\n"
            "  'Coagulant pumps' (Sec 3) -- not\n"
            "  applicable to this brine SWRO module.\n"
            "- Page numbering: cover '1 of 51' vs\n"
            "  footers 'X of 53'; pages 5 and 8\n"
            "  missing in numbering.\n"
            "- Item 8 duplicated in Sec 3.2.2 table\n"
            "  (PIT-09-008 + FIT-09-003).\n"
            "- Consolidated Comment Sheet absent.\n"
            "Restore CCS in Rev C and resolve\n"
            "documentary quality items."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
