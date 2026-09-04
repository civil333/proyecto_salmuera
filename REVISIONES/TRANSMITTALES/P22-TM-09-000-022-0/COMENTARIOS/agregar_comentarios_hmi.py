"""
agregar_comentarios_hmi.py
Anota HMI Display Screenshot Rev A (TM N22 / E50). Code 3.
len(COMENTARIOS) = 5 (OBS-01..05), espejo 1:1 del transmittal 2.7.
Documento image-based; anotaciones sobre la pagina de indice (TOC, PDF idx 1).
Texto sin etiqueta de criticidad. Verificacion visual interna ADASA aparte.
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-016_A_HMI_Display_Screenshot.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-016_A_HMI_Display_Screenshot_CC_ADASA.pdf")

assert os.path.exists(PDF_LOCAL), f"source missing: {PDF_LOCAL}"

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR,
        "search": "RO Feed", "page_min": 6, "page_fallback": 6,
        "text": (
            "OBS-01: No screen for the electrical-variables meter (MVE) with "
            "the specific energy consumption in kWh/m3, which the Technical "
            "Specification - Control and Automation System requires.\n"
            "Correct: add the screen, or document the existing screen where "
            "these variables are presented."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR,
        "search": "Alarm History", "page_min": 8, "page_fallback": 8,
        "text": (
            "OBS-02: No process-variable trending screen (the alarm history "
            "present is a different requirement).\n"
            "Correct: add at least one trending screen for the key process "
            "variables (flow, pressure, conductivity, levels)."
        ),
    },
    {
        "id": "OBS-03", "fill": MAYOR,
        "search": "Analog Transmitter", "page_min": 4, "page_fallback": 4,
        "text": (
            "OBS-03: No setpoint and parameterization screen with safe "
            "operating limits, which the Technical Specification requires.\n"
            "Correct: add it, or document the faceplate path by which the "
            "operator sets values and safe limits."
        ),
    },
    {
        "id": "OBS-04", "fill": MAYOR,
        "search": "RO Cartridge Filter", "page_min": 5, "page_fallback": 5,
        "text": (
            "OBS-04: Only two process screens are delivered (RO Cartridge "
            "Filter, RO Feed/HP Pump).\n"
            "Correct: add an overview screen and screens for second-stage RO, "
            "CIP, dosing, energy recovery and brine, with tags consistent "
            "with the approved P&ID and the Instrument List."
        ),
    },
    {
        "id": "OBS-05", "fill": MENOR,
        "search": "ISA-101", "page_min": 2, "page_fallback": 2,
        "text": (
            "OBS-05: ISA-101 conformance (screen hierarchy, state "
            "colour-coding, alarm prioritization) is declared but not "
            "evidenced.\n"
            "Correct: demonstrate it in the next revision; the full visual "
            "verification is reserved for the Factory Acceptance Test."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
