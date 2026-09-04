"""
agregar_comentarios_ro_vessel_hydro.py
Anota RO Vessel Hydrostatic Test Procedure Rev A (TM N23 / E51). Code 3.
len(COMENTARIOS) = 4 (OBS-01..04), espejo 1:1 del transmittal 2.2.
OBS-01 = CRITICAL (rojo). Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR,
    "P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": CRITICAL,
        "search": "45,5", "page_fallback": 10,
        "text": (
            "OBS-01: The test pressure is not stated as a binding project "
            "value in the body (only the generic 1.1x ASME / 1.43x CE rule), "
            "and this report form carries 45.5 bar (~660 psi), against the "
            "1,800 psi x 1.1 = 1,980 psi (~136.5 bar) the ITP row 2.2 and the "
            "waiver require.\n"
            "Correct: state the project test value by model - BPV-8-1800-SP-7 "
            "at 1,980 psi (~136.5 bar) and BPV-8-1200-SP-7 at 1,320 psi (~91 "
            "bar) - in the body and on the form; delete the 45.5 bar default "
            "and the unused CE 1.43x branch.\nRequirement: ET 5.1.6 + ASME "
            "waiver; figure must read identically here and in ITP row 2.2."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "Calibrated pressure gauge", "page_fallback": 7,
        "text": (
            "OBS-02: The procedure does not declare the ADASA witness and "
            "prior notification agreed as the counterpart of the waiver, and "
            "its instrumentation is a single calibrated gauge without "
            "certificate review or stated class/uncertainty (the HP/LP "
            "procedure requires QC certificate review and two gauges).\n"
            "Correct: add a notification and witness section (one-month "
            "notice) and specify traceable calibrated instrumentation reviewed "
            "before the test."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR,
        "search": "one (1) minute", "page_fallback": 8,
        "text": (
            "OBS-03: The hold time is at least one minute for an FRP vessel "
            "(the HP/LP procedure holds 30 minutes), and ASME Section X RT-5 "
            "is cited without its hold time and admissible pressure-drop "
            "value.\n"
            "Correct: declare the hold time and acceptance criterion per ASME "
            "Section X RT-5, citing the value."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": None, "page_fallback": 5,
        "text": (
            "OBS-04: The ADASA-coded cover is Rev A (12-Jun-2026) while the "
            "embedded Protec procedure sheet is its own Rev 0 (09-10-2025) with "
            "a separate signatory chain; the relationship is not declared.\n"
            "Correct: tie the ADASA wrapper revision to the embedded vendor "
            "procedure number and revision so a vendor change drives the "
            "wrapper revision."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
