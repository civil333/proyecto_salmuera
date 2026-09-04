"""
agregar_comentarios_plc_hmi_datasheet.py
Anota PDF Datasheet of PLC and HMI Panel Component Rev B (TM N21 / E48).
len(COMENTARIOS) = 3 (OBS-01 HART, OBS-02 RTD, NOTE-01 typo).
Colores: fill transmite severidad (MAYOR naranja / MENOR amarillo / NOTE azul).
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8); directivo.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-ET-09-008-001_B_PLC_HMI_Datasheet.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-ET-09-008-001_B_PLC_HMI_Datasheet_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 48",
        "P22-ET-09-008-001_B Datasheet of PLC and HMI Panel Component "
        "(Major Component).pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 21,
        "text": (
            "OBS-01: No HART acquisition path in the\n"
            "panel. The 5069-IF8 analog input reads\n"
            "4-20 mA only; it does not acquire HART,\n"
            "and the rack has no HART-capable AI nor\n"
            "HART multiplexer.\n"
            "Requisite: the Technical Specification -\n"
            "Instrumentation requires the signal\n"
            "protocol to be 4-20 mA + HART.\n"
            "Correct: provide a HART acquisition path\n"
            "(HART-capable AI or HART multiplexer) or\n"
            "justify the omission in Rev C."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 2,
        "text": (
            "OBS-02: Module list does not match the\n"
            "project rack. This datasheet omits the\n"
            "two 5069-IY4 universal analog modules\n"
            "(8 motor Pt-100 RTD channels) declared in\n"
            "the LCP Datasheet Rev B and the PLC/LCP\n"
            "Schematic Diagram.\n"
            "Correct: incorporate the 5069-IY4 modules,\n"
            "or reference the LCP Datasheet for the\n"
            "project rack, in Rev C."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Tattal",
        "page_fallback": 0,
        "text": (
            "NOTE-01: Cover title block typo\n"
            "\"PD Tattal\".\n"
            "Correct: \"PD Taltal\"."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
