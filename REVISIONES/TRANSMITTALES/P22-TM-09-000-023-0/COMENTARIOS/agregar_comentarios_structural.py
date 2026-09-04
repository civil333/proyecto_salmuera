"""
agregar_comentarios_structural.py
Anota UHPRO Structural Design Criteria Rev A (TM N23 / E52). Code 3.
len(COMENTARIOS) = 8 (OBS-01..07, NOTE-01), espejo 1:1 del transmittal 2.7.
Texto sin etiqueta de criticidad.
Nota: el PDF tiene fuente cifrada (offset detectado en extraccion); si search
falla, se ancla por page_fallback (0-based). Verificar post-run.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR,
    "P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "NCh2369:2009", "page_fallback": 6, "page_min": 5,
        "text": (
            "OBS-01: The seismic-standard citation is inconsistent: this "
            "parameter table and the load combinations cite NCh 2369:2009 - an "
            "edition that does not exist - while the code list correctly cites "
            "NCh 2369 Of.2003, the edition the ET establishes for this "
            "project.\n"
            "Correct: change every NCh 2369:2009 citation to NCh 2369 Of.2003 "
            "so the seismic basis matches the code list (the parameter values "
            "are already consistent with Of.2003)."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "Cl. 4.5", "page_fallback": 7, "page_min": 6,
        "text": (
            "OBS-02: For allowable-stress design the governing seismic load "
            "combinations are those of NCh 2369 (combinations 11 and 12: D + aL "
            "+ SO + SA +/- Eh +/- Ev and D + SA +/- Eh +/- Ev, clause 4.5); the "
            "base combinations 1-10 are from NCh 3171.\n"
            "Correct: confirm the NCh 2369 Of.2003 clause 4.5 combinations "
            "govern the seismic ASD verification (the generic NCh 3171 "
            "combinations do not replace them) and correct the edition citation "
            "from the non-existent 2009 to Of.2003."
        ),
    },
    {
        "id": "OBS-03", "fill": MAYOR,
        "search": None, "page_fallback": 8,
        "text": (
            "OBS-03: The criteria omit the lifting (transport and erection) "
            "load case and the lifting-point and yoke design criteria. The "
            "module Technical Specification - Final Documentation requires the "
            "module lifting calculation, the lifting plan with lifting points "
            "and weights, and the lifting yoke design and drawing (the lifting "
            "DESIGN is BW Water's scope; the crane and lifting equipment for the "
            "on-site installation are ADASA's scope).\n"
            "Correct: add the lifting/handling load case and the lifting-point "
            "and yoke design basis (incl. the dynamic amplification factor for "
            "the lifting maneuver) so the required lifting deliverables have an "
            "approved design basis."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": "FOR APPROVAL", "page_fallback": 1,
        "text": (
            "OBS-04: The revision identity is inconsistent - the ADASA code "
            "block labels the document Rev A (17-Jun-2026) while the internal "
            "block and every footer label it Rev 00 / FOR APPROVAL "
            "(16-Jun-2026); under the codification standard Rev A and Rev 0 "
            "denote opposite lifecycle stages.\n"
            "Correct: reconcile the ADASA block and the internal block to one "
            "revision and date."
        ),
    },
    {
        "id": "OBS-05", "fill": MENOR,
        "search": "Type of Soil", "page_fallback": 6,
        "text": (
            "OBS-05: Soil Type E (softest class, highest demand) is adopted "
            "without a cited site geotechnical basis.\n"
            "Correct: state Soil Type E as a conservative envelope pending the "
            "project geotechnical report, consistent with the anchor-bolt "
            "validation note already in the design approach."
        ),
    },
    {
        "id": "OBS-06", "fill": MENOR,
        "search": None, "page_fallback": 6,
        "text": (
            "OBS-06: The design seismic weight P in the base-shear equation is "
            "not declared and the established module operating weight is not "
            "cross-referenced.\n"
            "Correct: declare the operating weight used for P (or cross-"
            "reference the Equipment Layout operating-weight table) so the "
            "seismic design weight is traceable."
        ),
    },
    {
        "id": "OBS-07", "fill": MENOR,
        "search": None, "page_fallback": 5,
        "text": (
            "OBS-07: The minimum design wind pressures are written in N/m "
            "(force per length) where the correct unit is N/m2 (pressure).\n"
            "Correct: correct the units to N/m2 and confirm the NCh 432 edition "
            "cited."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": "G25", "page_fallback": 4,
        "text": (
            "NOTE-01: The reinforced-concrete grade and standard label "
            "(NCh1170 / G25, f'c = 24.5 MPa) is to be confirmed (the Chilean "
            "standard is normally NCh 170 and a G25 grade is about 25 MPa). "
            "The concrete applies to the foundations in the civil scope outside "
            "this skid package; coordinate the final grade with the foundation "
            "designer."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
