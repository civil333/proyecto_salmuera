"""
agregar_comentarios_itp.py
Anota Inspection and Test Plan Rev C (TM N23 / E51). Code 2.
len(COMENTARIOS) = 3 (OBS-01, OBS-02, NOTE-01), espejo 1:1 del transmittal 2.1.
Code 2 SIEMPRE lleva CC_ADASA (CLAUDE.md 3.8). Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-004_C_ITP.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-004_C_ITP_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "Manufacture to ASME X", "page_fallback": 1,
        "text": (
            "OBS-01: Row 2.2 reads only Manufacture to ASME X; it does not "
            "state that the RO pressure vessels are built and tested to ASME "
            "Section X WITHOUT code stamp, which is the negotiated waiver "
            "basis. The ITP governs acceptance and the 40% payment milestone.\n"
            "Correct: add to row 2.2 a note - vessels to ASME Section X without "
            "code stamp per the ADASA waiver of 02-Jun-2026; hydrostatic test "
            "1,800 psi x 1.1 witnessed by ADASA at the vendor; dossier per rows "
            "7.6 and 8.3.\nRequirement: TM N19 / TM N22 carry-forward + waiver."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "1800psi", "page_fallback": 1,
        "text": (
            "OBS-02: The RO Vessel hydrostatic test (row 2.2) is coded W "
            "(Witness) for ADASA, while the high-pressure system test (row 5.2) "
            "is coded H (Hold Point). Under the waiver the vessel test is the "
            "most critical.\n"
            "Correct: raise row 2.2 from Witness (W) to Hold Point (H), "
            "consistent with row 5.2, so the vessel test is not released "
            "without ADASA presence and written approval."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": "PREN", "page_fallback": 1,
        "text": (
            "NOTE-01: The waiver basis is captured for the first time - row "
            "2.2 (1,800 psi x 1.1 vessel test, ADASA Witness), row 2.4 (PMI "
            "Super Duplex, PREN>40), rows 7.6 and 8.3 (production/test dossier, "
            "the latter a Hold Point). ASME Section X is correct for FRP "
            "vessels. This materially closes the oldest open fabrication item; "
            "the ASME stamp remains waived and is not reopened."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
