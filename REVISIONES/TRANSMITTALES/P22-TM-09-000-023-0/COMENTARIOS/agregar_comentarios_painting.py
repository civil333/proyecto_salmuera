"""
agregar_comentarios_painting.py
Anota Painting Procedure Rev A (TM N23 / E51). Code 3.
len(COMENTARIOS) = 7 (OBS-01..06, NOTE-01), espejo 1:1 del transmittal 2.5.
Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-011_A_Painting_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-011_A_Painting_Procedure_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "BARRIER 80", "page_fallback": 8,
        "text": (
            "OBS-01: The procedure proposes a Jotun system (Barrier 80, "
            "Penguard Midcoat, Hardtop XP) in place of the Sherwin-Williams "
            "system (Zinc Clad II, Macropoxy 646, Acrolon 218 HS) fixed in the "
            "Painting Specifications Rev B (approved Code 1 at TM N11), with no "
            "equivalence justification; the ET conditions any equivalent on "
            "ADASA approval.\n"
            "Correct: attach a product-to-product equivalence table (generic "
            "chemistry, % solids by volume, ISO 12944-6 class, DFT range) and "
            "obtain ADASA approval of the Jotun system, or adopt the "
            "Sherwin-Williams system; reconcile both documents."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "C5-I", "page_fallback": 11,
        "text": (
            "OBS-02: Marine durability is not demonstrated: the body declares "
            "no target corrosivity category, and the Barrier 80 primer is "
            "certified for C5-I (industrial), not C5-M (marine), where coastal "
            "Taltal and the ET require C5-M with high durability.\n"
            "Correct: declare the target category C5-M (or CX) and high "
            "durability, and provide the ISO 12944-6 evidence for the complete "
            "system."
        ),
    },
    {
        "id": "OBS-03", "fill": MAYOR,
        "search": "ROUGHNESS", "page_fallback": 10,
        "text": (
            "OBS-03: The anchor profile is contradictory and below the ET: the "
            "body fixes 50-80 microns while this inspection form fixes 40-75 "
            "microns; the 40 micron lower bound is below the 50 micron ET "
            "minimum, so a non-conforming profile could be recorded as "
            "conforming.\n"
            "Correct: unify the anchor profile to a single range with a lower "
            "bound of at least 50 microns."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": "HARDTOP", "page_fallback": 8,
        "text": (
            "OBS-04: The finish-coat colour RAL 5012 (Luminous Blue) required "
            "by the ET and confirmed in the Painting Specifications Rev B is "
            "not stated in the painting scheme or the inspection form (Colour "
            "field left blank).\n"
            "Correct: state the RAL 5012 finish colour in the scheme and the "
            "inspection form."
        ),
    },
    {
        "id": "OBS-05", "fill": MENOR,
        "search": "SKIDS", "page_fallback": 7,
        "text": (
            "OBS-05: The scope is generic and does not limit the coating to "
            "the ASTM A-36 structural carbon steel nor exclude stainless steel "
            "and non-metallic surfaces (FRP, HDPE), which are not painted.\n"
            "Correct: bound the scope to the ASTM A-36 carbon steel and "
            "exclude stainless steel and non-metallic surfaces."
        ),
    },
    {
        "id": "OBS-06", "fill": MENOR,
        "search": "Specified DFT", "page_fallback": 10,
        "text": (
            "OBS-06: QC lacks an adhesion test (pull-off ISO 4624 or cross-cut "
            "ISO 2409), the nominal DFT per coat/total is not pre-loaded in the "
            "form (left as xxx microns), ISO 2808 is not cited as the DFT "
            "method, and SSPC-SP10 / NACE No. 2 is not listed among the "
            "references.\n"
            "Correct: add an adhesion test, the nominal DFT per coat (80/200/75 "
            "= 355 microns), and the ISO 2808 and SSPC-SP10 references."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": "PAINTING SYSTEM", "page_fallback": 8,
        "text": (
            "NOTE-01: The layer architecture (80 / 200 / 75 = 355 microns) and "
            "the Sa 2 1/2 preparation match the ET and the approved Painting "
            "Specifications Rev B; the rejection concerns brand equivalence, "
            "C5-M durability, colour and anchor profile, not the scheme "
            "concept - recoverable by revision without redesigning the system."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
