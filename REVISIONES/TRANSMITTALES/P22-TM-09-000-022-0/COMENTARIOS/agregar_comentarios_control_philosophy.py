"""
agregar_comentarios_control_philosophy.py
Anota Plant Control Philosophy Rev D (TM N22 / E49). Code 3.
len(COMENTARIOS) = 7 (OBS-01..05 + NOTE-01,02), espejo 1:1 del transmittal 2.1.
Colores: fill transmite severidad (MAYOR naranja / MENOR amarillo / NOTE azul).
Texto sin etiqueta de criticidad (CLAUDE.md 3.8); directivo.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_D_Control_Philosophy.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BT-09-009-001_D_Control_Philosophy_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "P22-LI-09-008-017", "page_fallback": 7,
        "text": (
            "OBS-01: Core control logic still in undelivered child documents. "
            "The Controls and Sequence Chart (P22-LI-09-008-017), the Alarm "
            "and Control Setpoint List (P22-LI-09-008-015) and the Control "
            "Matrix are referenced here but were not submitted with the "
            "Control Philosophy.\n"
            "Correct: issue the three documents together with the Control "
            "Philosophy at Rev E, formally coded, revisioned and dated."
        ),
    },
    {
        "id": "OBS-02", "fill": MENOR,
        "search": "CIT-09-005", "page_fallback": 48,
        "text": (
            "OBS-02: Salt-rejection narrative contradicts the corrected "
            "formula. The text states the metric compares permeate "
            "(CIT-09-002) against reject conductivity (CIT-09-005), while the "
            "formula uses feed conductivity (CIT-09-001B).\n"
            "Correct: rewrite the narrative to match the feed-conductivity "
            "formula and confirm the interstage / Stage-2 denominators."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR,
        "search": "Total Energy Consumed", "page_fallback": 10,
        "text": (
            "OBS-03: Guaranteed energy-consumption scope not enumerated. The "
            "section states only total energy without listing the loads the "
            "guaranteed value must include.\n"
            "Correct: enumerate the metered loads (HP pump, dosing pump, CIP "
            "pump, CIP heater, RO PLC power, lighting, air-conditioning) so "
            "the value is traceable to the contractual basis."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": "AIT-09-002", "page_fallback": 50,
        "text": (
            "OBS-04: The permeate conductivity analyzer is tagged AIT-09-002 "
            "here but CIT-09-002 in the equipment table, formulas and "
            "permissives.\n"
            "Correct: use CIT-09-002 throughout (one tag per instrument)."
        ),
    },
    {
        "id": "OBS-05", "fill": MENOR,
        "search": "05/05/2026", "page_fallback": 0,
        "text": (
            "OBS-05: Title-block metadata inconsistent. The cover records "
            "Rev D (28-May-2026) but the header reads Date 05/05/2026 / "
            "Revision No. 5 and the page-count fields disagree.\n"
            "Correct: reconcile the controlling revision, date and page count."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": "VE-09-007 AVAILABLE", "page_fallback": 47,
        "text": (
            "NOTE-01: HP Pump start permissive corrected. VE-09-007 now "
            "appears once and the antiscalant-refill valve VE-09-014 no "
            "longer inhibits HP Pump start. The repeated CRITICAL of "
            "Transmittal N18 is closed. Keep it consistent with the Sequence "
            "Charts and Valve List when those are issued."
        ),
    },
    {
        "id": "NOTE-02", "fill": NOTE,
        "search": "equipped with HART", "page_fallback": 23,
        "text": (
            "NOTE-02: The 4-20 mA + HART protocol and the "
            "instrumentation-failure response are confirmed in the body. The "
            "numerical trip and alarm values remain to be verified against "
            "the Setpoint List and Control Matrix once issued."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
