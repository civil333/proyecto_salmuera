"""
agregar_comentarios_control_philosophy.py
Anota PDF Plant Control Philosophy Rev C (E39 / submittal 25007-0039, 75 paginas).

Checklist (CLAUDE.md section 3.8):
  1. Tabla OBS/NOTE del transmittal Section 2.1: OBS-01/02/03 + NOTE-01/02/03 = 6
  2. PDFs en submittal 25007-0039: 1
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 6
  5. IDs coinciden: Section 2.1 del transmittal TM N18

Veredicto: 3 - To be revised (CRITICAL repetido NOTE-20 de TM N15 sin cerrar)
Colores: fill transmite severidad (CRITICAL rojo / MAYOR naranja / MENOR amarillo).
Texto sin etiqueta de criticidad (CLAUDE.md section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_C_Control_Philosophy.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BT-09-009-001_C_Control_Philosophy_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 39",
        "P22-BT-09-009-001_C Plant Control Philosophy.pdf",
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
        "search": "Turbocharger isolation valve VE-09-007",
        "page_fallback": 62,
        "text": (
            "OBS-01: HP Pump start permissive uncorrected.\n"
            "Still reads 'VE-09-007 and VE-09-007'\n"
            "(duplicated TAG, not corrected to\n"
            "VE-09-008) and still requires\n"
            "'VE-09-014 fully CLOSED'. VE-09-014 is\n"
            "the antiscalant tank inlet valve that\n"
            "opens automatically to refill the tank\n"
            "on low level -- the PLC, read literally,\n"
            "inhibits HP Pump start during routine\n"
            "antiscalant refill. Same defect as\n"
            "Transmittal N15 NOTE-20 (CRITICAL),\n"
            "2nd consecutive transmittal.\n"
            "Reconcile permissive vs P&ID Rev C and\n"
            "Valve List Rev D in Rev D. Resolution in\n"
            "Rev D is a blocking condition for closing\n"
            "the Control Philosophy; repeated CRITICAL\n"
            "recorded for contractual follow-up\n"
            "(Contract C-4300)."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Controls & Sequence Chart",
        "page_fallback": 21,
        "text": (
            "OBS-02: Core control logic deferred to\n"
            "undelivered child documents.\n"
            "RO/CIP Sequence Charts, Alarm & Control\n"
            "Setpoint List and Control Matrix remain\n"
            "'SEPARATE DOCUMENT'. Tentative date\n"
            "13-May-2026 passed; submittal 25007-0039\n"
            "carries the Control Philosophy only.\n"
            "Salt-rejection formula, CIP valve phase\n"
            "sequence, VE-09-002 algorithm and\n"
            "off-spec routing interlock are deferred\n"
            "to these documents. Provide them with\n"
            "formal codes, revisions and a binding\n"
            "date prior to IFC."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "Overall Salt Rejection",
        "page_fallback": 69,
        "text": (
            "OBS-03: Salt Rejection formula still\n"
            "divides by Stage-2 reject conductivity\n"
            "(CIT-09-005) instead of feed\n"
            "conductivity. Per ASTM D4516 and\n"
            "standard membrane-projection practice,\n"
            "use feed conductivity (CIT-09-001B) in\n"
            "the denominator. Correct in the Control\n"
            "Philosophy body in Rev D -- it defines\n"
            "the performance metric shown on the HMI."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "RO PLC panel power meter",
        "page_fallback": 24,
        "text": (
            "NOTE-01: SEC energy still measured at\n"
            "the RO PLC panel power meter -- wrong\n"
            "bus. That meter reads PLC + UPS +\n"
            "control gear only, not the ~85 kW HP\n"
            "Pump motor that dominates SEC. The\n"
            "added assertion does not relocate the\n"
            "metering point. Move the measurement\n"
            "to the MCC main breaker, or specify\n"
            "explicitly the meters whose sum is\n"
            "divided by the FIT-09-003 totalizer."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "4.8 kWh",
        "page_fallback": 24,
        "text": (
            "NOTE-02: SEC contractual value\n"
            "misaligned. Two TDS-banded targets\n"
            "(< 4.8 for 43-48k; < 5.0 for 48-53k\n"
            "kWh/m3) retained vs Technical Offer\n"
            "Rev1 single 4.71 kWh/m3 +/-5% with no\n"
            "TDS banding. Target-vs-setpoint\n"
            "clarification acknowledged, but the\n"
            "numerical divergence from the\n"
            "contractual guarantee remains.\n"
            "Reconcile in Rev D."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": MENOR,
        "search": "Turbocharger Isolation Valve with Limit Switches",
        "page_fallback": 51,
        "text": (
            "NOTE-03: Documentary quality.\n"
            "Two group-table rows numbered '11'\n"
            "(VE-09-006 RO Reject Flow Control Valve\n"
            "and VE-09-007); VE-09-007 described\n"
            "both as 'Turbocharger Isolation Valve'\n"
            "and 'Interstage Isolation Valve'.\n"
            "Resolve numbering and use one\n"
            "consistent description per TAG in Rev D.\n"
            "Closure of TM N15 NOTE-14/15/18/19/21/23\n"
            "and CCS inclusion acknowledged."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
