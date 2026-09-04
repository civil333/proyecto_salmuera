"""
agregar_comentarios_static_mixer.py
Anota Datasheet of Static Mixer Rev C (TM N22 / E49). Code 2.
len(COMENTARIOS) = 3 (OBS-01, OBS-02, NOTE-01), espejo 1:1 del transmittal 2.5.
Code 2 SIEMPRE lleva CC_ADASA (CLAUDE.md 3.8). Texto sin etiqueta de criticidad.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-009-012_C_Static_Mixer.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-009-012_C_Static_Mixer_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MENOR,
        "search": "1150", "page_fallback": 2,
        "text": (
            "OBS-01: The vendor technical data sheet (1150 kg/m3, 35 C, fluid "
            "labelled \"Antiscalant\") contradicts the ADASA front sheet (feed "
            "brine, specific gravity 1.05, 19 to 24 C). Both agree the main "
            "stream is 49 m3/h, so the sizing is unaffected.\n"
            "Correct: reconcile both pages at Rev 0, or add a remark that "
            "1150 kg/m3 / 35 C is a conservative design envelope."
        ),
    },
    {
        "id": "OBS-02", "fill": MENOR,
        "search": "Injection", "page_fallback": 2, "page_min": 2,
        "text": (
            "OBS-02: The antiscalant injection rate is stated with different "
            "values across the sheets.\n"
            "Correct: align to a single value and unit matching the accepted "
            "Antiscalant Dosing Pump duty."
        ),
    },
    {
        "id": "NOTE-01", "fill": NOTE,
        "search": "MZE-09-001", "page_fallback": 1,
        "text": (
            "NOTE-01: Tag MZE-09-001 reconciled with the P&ID. Duty, sizing "
            "and connections (49 m3/h main stream, FRP, ANSI 150 RF, four "
            "elements) accepted as-is."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
