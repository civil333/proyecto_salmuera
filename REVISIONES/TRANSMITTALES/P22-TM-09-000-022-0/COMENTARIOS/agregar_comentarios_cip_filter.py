"""
agregar_comentarios_cip_filter.py
Anota Datasheet of CIP Cartridge Filter Rev D (TM N22 / E49). Code 3.
len(COMENTARIOS) = 5 (OBS-01..04 + NOTE-01), espejo 1:1 del transmittal 2.4.
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-009-006_D_CIP_Cartridge_Filter.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-009-006_D_CIP_Cartridge_Filter_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "Gasket", "page_fallback": 2,
        "text": (
            "OBS-01: Gasket and FRP chemical-compatibility for the pH 2 to 12 "
            "cleaning duty not documented. The default nitrile gasket has "
            "poor high-pH resistance. This is the item Transmittal N19 OBS-03 "
            "asked to close in this revision.\n"
            "Correct: name a gasket suitable across the full pH range "
            "(EPDM/Viton/PTFE) and attach a compatibility statement for the "
            "housing and seal against the cleaning reagents."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "Vertical", "page_fallback": 1,
        "text": (
            "OBS-02: The horizontal-to-vertical change and the "
            "Filtrek-to-Sysflo vendor substitution remain ahead of ADASA's "
            "formal position on the Technical Note.\n"
            "Correct: re-issue only after that position, and hold the Purchase "
            "Order until the formal release. Any earlier purchase is at BW "
            "Water's risk."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR,
        "search": "RO CIP Cartridge Filter", "page_fallback": 1,
        "text": (
            "OBS-03: The Component Name field reads \"RO CIP Cartridge "
            "Filter\", carried over from the sibling datasheet.\n"
            "Correct: \"CIP Cartridge Filter\", consistent with tag "
            "FIL-09-002."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": "Surface Area", "page_fallback": 1,
        "text": (
            "OBS-04: The filter surface-area basis differs from the RO "
            "Cartridge Filter sibling (total versus per-cartridge), and the "
            "filtration rate unit does not allow an area cross-check.\n"
            "Correct: homologate the basis with the RO sibling and express "
            "the filtration rate in m3/h/m2."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": None, "page_fallback": 1,
        "text": (
            "NOTE-01: The container as-built with the vertical configuration "
            "is a separate, shared deliverable, verified through the "
            "Equipment Layout and tracked in the transmittal; not a defect of "
            "this datasheet."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
