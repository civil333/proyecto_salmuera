"""
agregar_comentarios_instrument_layout.py
Anota Instrument Location Layout Rev C (TM N23 / E52). Code 3.
len(COMENTARIOS) = 4 (OBS-01..04), espejo 1:1 del transmittal 2.6.
Es un PLANO (4 paginas): search casi nunca encuentra texto -> search=None +
page_fallback (0-based). Verificar SIEMPRE por render PNG (paginas rotadas).
OBS-03/04 en caratula (pag 1, idx 0); OBS-01/02 en CCS (pag 4, idx 3).
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-008-001_C_Instrument_Location_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR,
    "P22-DWG-09-008-001_C_Instrument_Location_Layout_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": None, "page_fallback": 3,
        "text": (
            "OBS-01: Re-issued on 16-Jun-2026 with content changes (item 8, 9, "
            "31, 32 descriptions and the CIP relocation) but the revision "
            "letter stays C with no new revision-history row and an empty ECN "
            "column; two physically different drawings share the identifier "
            "Rev C.\n"
            "Correct: re-issue as Rev D with a new revision-history row (date, "
            "ECN, description of the edits, initials); do not reuse the C "
            "identifier for changed content."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": None, "page_fallback": 3,
        "text": (
            "OBS-02: Instrument positions are aligned to Equipment Layout Rev "
            "B, which has advanced to Rev C and is open at Code 3 (RO Cartridge "
            "Filter still horizontal); BW Water's own reply concedes it cannot "
            "be issued for construction until the upstream layouts are approved "
            "with no comment.\n"
            "Correct: hold for Rev D and re-align all instrument positions to "
            "the approved Equipment Layout revision (not Rev B) once it is "
            "resolved to Code 1/2 with the RO Cartridge Filter vertical."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR,
        "search": None, "page_fallback": 0,
        "text": (
            "OBS-03: The front title-block code reads P22-DWG-09-008-01 (a "
            "two-digit correlative) where the file name and the sheet cajetin "
            "correctly use the three-digit P22-DWG-09-008-001.\n"
            "Correct: correct the front title-block code to the three-digit "
            "correlative so it matches every block."
        ),
    },
    {
        "id": "OBS-04", "fill": MENOR,
        "search": None, "page_fallback": 0,
        "text": (
            "OBS-04: The Rev C date is inconsistent - the front header dates "
            "Revision C 16/6/2026 while the revision-history block on the "
            "sheets dates Revision C in April; a single revision cannot carry "
            "two issue dates.\n"
            "Correct: on the Rev D re-issue set one consistent issue date in "
            "the header and the new revision-history row, leaving the "
            "historical Rev C date unchanged."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
