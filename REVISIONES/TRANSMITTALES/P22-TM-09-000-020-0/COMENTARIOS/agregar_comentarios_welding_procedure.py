"""
agregar_comentarios_welding_procedure.py
Anota PDF Welding Procedure Rev A (TM N20).
len(COMENTARIOS) = 3 (OBS-01 + OBS-02 + NOTE-01).
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-007_A_Welding_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-007_A_Welding_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 47",
        "P22-BA-09-000-007_A Welding Procedure.pdf",
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
        "search": "14.02",
        "page_fallback": 2,
        "text": (
            "OBS-01: Super Duplex PQR coupon 2.77 mm\n"
            "qualifies up to 5.54 mm per ASME IX\n"
            "QW-451, while the WPS declares a range to\n"
            "14.02 mm. Correct: provide the qualifying\n"
            "coupon for the upper range or restrict\n"
            "the WPS at IFC Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-02: low-pressure thermoplastic joining\n"
            "scope not addressed; the NDE Plan cites\n"
            "DVS 2202-1 acceptance for thermoplastic\n"
            "joints. Correct: state the joining method\n"
            "and its procedure at IFC Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "ER2594",
        "page_fallback": 2,
        "text": (
            "NOTE-01: no heat-input limits or ferrite-\n"
            "number acceptance for the Super Duplex\n"
            "WPS - corrosion-critical for\n"
            "45000-55000 ppm chloride brine. Correct:\n"
            "declare both at IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
