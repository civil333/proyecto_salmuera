"""
agregar_comentarios_hp_lp_pressure.py
Anota HP and LP Pressure Test Procedure Rev A (TM N23 / E51). Code 3.
len(COMENTARIOS) = 2 (OBS-01, OBS-02), espejo 1:1 del transmittal 2.3.
Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR,
    "P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "required test pressure", "page_fallback": 7,
        "text": (
            "OBS-01: The procedure writes no numeric test pressure or the ASME "
            "B31.3 factor, repeating the required test pressure generically. "
            "The ITP fixes 135 bar (1.5 x 90 bar) HP and 7.5 bar LP. The HP "
            "design pressure is also unreconciled (ITP 90 bar vs Technical "
            "Specification up to 120 bar).\n"
            "Correct: declare the design pressure per subsystem, the B31.3 "
            "factor (1.5x), and the resulting test pressure in bar matching the "
            "ITP; reconcile the HP design pressure citing the source.\n"
            "Requirement: ASME B31.3 para. 345.4.2; ITP rows 5.1/5.2."
        ),
    },
    {
        "id": "OBS-02", "fill": MENOR,
        "search": "5.5.17", "page_fallback": 8,
        "text": (
            "OBS-02: In the pneumatic-test section, after step 5.6.16 the "
            "numbering reverts to 5.5.17 and 5.5.18 (duplicating the "
            "hydrostatic-section identifiers) and step 5.6.5 is missing.\n"
            "Correct: renumber section 5.6 consecutively, removing the "
            "duplicates and the gap."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
