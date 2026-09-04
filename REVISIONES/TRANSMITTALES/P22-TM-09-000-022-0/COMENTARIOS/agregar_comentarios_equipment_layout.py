"""
agregar_comentarios_equipment_layout.py
Anota Equipment Layout Rev C (TM N22 / E49). Code 3.
len(COMENTARIOS) = 3 (OBS-01..03), espejo 1:1 del transmittal 2.2.
Plano A1 rotado 270 grados (PDF idx 3). doc-annotator maneja la rotacion
automaticamente (dibuja en raw coords, text_rotate = page.rotation).
Verificar por render PNG tras correr.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-003_C_Equipment_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-003_C_Equipment_Layout_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "FIL-09-001", "page_fallback": 3,
        "text": (
            "OBS-01: RO Cartridge Filter (FIL-09-001, item 2) drawn "
            "horizontal. Its Datasheet Rev E declares the filter vertical "
            "(horizontal-to-vertical change of Technical Note "
            "P22-NT-09-000-001-0); the layout does not reflect it. The CIP "
            "filter (item 11) is correctly vertical.\n"
            "Correct: redraw the RO cartridge filter vertical, with footprint, "
            "operator access and 2000 mm clear headroom for cartridge "
            "withdrawal."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "EQUIPMENT LAYOUT", "page_fallback": 3, "page_min": 3,
        "text": (
            "OBS-02: Operating Weight table not embedded. Transmittal N15 "
            "NOTE-04 instructed embedding it in the Rev 0 issue; it is again "
            "deferred to a separate Civil and Loading drawing not yet "
            "submitted.\n"
            "Correct: embed the Operating Weight table, or obtain ADASA's "
            "written acceptance to keep it only in the Civil and Loading "
            "drawing, and deliver that drawing."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR,
        "search": "LOCAL CONTROL PANEL", "page_fallback": 3,
        "text": (
            "OBS-03: The legend labels no main or power panel; the Grounding "
            "Layout Rev F is anchored to the main panel fixed in the approved "
            "Equipment Layout position.\n"
            "Correct: label the main panel and unify its name and position "
            "between both drawings, and make the title-block revision field "
            "legible."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
