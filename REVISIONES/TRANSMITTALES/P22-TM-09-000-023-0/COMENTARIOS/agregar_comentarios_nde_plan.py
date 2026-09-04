"""
agregar_comentarios_nde_plan.py
Anota NDE Plan Rev B (TM N23 / E51). Code 3.
len(COMENTARIOS) = 2 (OBS-01, OBS-02), espejo 1:1 del transmittal 2.4.
Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-005_B_NDE_Plan.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-005_B_NDE_Plan_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "Applicable Edition", "page_fallback": 3,
        "text": (
            "OBS-01: Every code (ASME Sec. V Art. 9, Sec. II, B31.3, AWS D1.1, "
            "DVS 2202-1) is listed as Applicable Edition/Addenda without a "
            "controlling year; the inspection plan basis rejects generic "
            "references, and the Rev A comment on this point was not closed in "
            "Rev B.\n"
            "Correct: state the governing year/addenda for each referenced "
            "code (e.g. ASME B31.3-2022, ASME BPVC Sec. V-2023).\n"
            "Requirement: ET Section 8; PIE Base."
        ),
    },
    {
        "id": "OBS-02", "fill": MENOR,
        "search": "ACCEPTANCE CRITERIA", "page_fallback": 5, "page_min": 4,
        "text": (
            "OBS-02: The acceptance criteria mix AWS D1.1 (structural) and DVS "
            "2202-1 (thermoplastic) with the high-pressure Super Duplex circuit "
            "governed by ASME B31.3 without mapping each code to its joints; "
            "the UT column reads pipe thicknesses (a baseline measurement, not "
            "weld-NDE extent).\n"
            "Correct: state that the HP Super Duplex circuit is evaluated to "
            "ASME B31.3 (AWS D1.1 for support structure, DVS 2202-1 for LP "
            "thermoplastic joints), clarify the UT thickness column, and cite "
            "the B31.3 acceptance paragraph with the fluid-service category."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
