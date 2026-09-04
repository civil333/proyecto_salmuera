"""
agregar_comentarios_painting.py
Anota PDF Painting Procedure Rev B (TM N27, Code 2). len(COMENTARIOS) = 5
(OBS-01 MAYOR + OBS-02 MENOR + OBS-03 MENOR + NOTE-01 + NOTE-02).
Code 2 SIEMPRE lleva CC_ADASA con sus OBS/NOTE propios (CLAUDE.md 3.8).

Paginas 0-based del PDF Rev B (38 pags):
  OBS-01 = 10 (impresa 11, inspection form: BLASTING ACTIVITY criteria 40-75 um)
  OBS-02 = 10 (impresa 11, mismo form: "Specified DFT: xxx um" + Type en blanco)
  OBS-03 =  8 (impresa 9, bloque PAINTING SYSTEM sin color RAL 5012)
  NOTE-01 = 11 (impresa 12, carta Jotun TSS-DD-MYPC039-26: cierra equivalencia + C5-M)
  NOTE-02 =  7 (impresa 8, seccion 2.0 con las normas: SSPC-SP10 == NACE No. 2)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-011_B_Painting_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 63",
        "P22-BA-09-000-011_B_ Painting Procedure.pdf",
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
        "search": "BLASTING ACTIVITY",
        "page_fallback": 10,
        "text": (
            "OBS-01: this criterion still reads 40-75 um\n"
            "while the procedure body and the acceptance row\n"
            "of this same form read 50-80 um. The inspector\n"
            "works against two incompatible criteria and can\n"
            "accept a 40 um profile, below the 50 um lower\n"
            "bound required at Transmittal N23 and below the\n"
            "anchor profile of ET Section 5.1.9 - Support\n"
            "Frame.\n"
            "Correct: unify the form to a single 50-80 um\n"
            "criterion."
        ),
    },
    {
        "id": "OBS-02",
        # search=None: "specified DFT" tambien aparece en la clausula 6.9 (pag 10),
        # asi que se ancla por pagina al formulario de inspeccion (0-based 10 = impresa 11).
        "search": None,
        "fill": MENOR,
        "page_fallback": 10,
        "text": (
            "OBS-02: the specified DFT is still the\n"
            "placeholder \"xxx um\" and the Type row of the\n"
            "painting system is blank, so the nominal\n"
            "thickness per coat appears nowhere on the record\n"
            "the inspector signs.\n"
            "Correct: print the nominal values (80 / 200 /\n"
            "75 um, not less than 355 um total) and the\n"
            "product per coat."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "3rd COAT",
        "page_fallback": 8,
        "text": (
            "OBS-03: the painting system does not state the\n"
            "finish colour. RAL 5012 (Luminous Blue) is fixed\n"
            "for the structural support frame by the approved\n"
            "Painting Specification Rev C and by ET Section\n"
            "5.1.9 - Support Frame.\n"
            "Correct: state RAL 5012 here and in the Colour\n"
            "row of the inspection form."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "suitable to be used for C5M",
        "page_fallback": 11,
        "text": (
            "NOTE-01: this letter and the attached data\n"
            "sheets close the two Transmittal N23 major\n"
            "observations: the coat-by-coat equivalence\n"
            "against the approved Painting Specification and\n"
            "the C5-M marine durability. ADASA raises no\n"
            "further objection to the Jotun system for the\n"
            "ASTM A-36 support frame."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "SSPC-SP-10",
        "page_fallback": 7,
        "text": (
            "NOTE-02: SSPC-SP10 and NACE No. 2 are the same\n"
            "standard, so this reference satisfies that item\n"
            "and no separate NACE citation is required. The\n"
            "scope bounded to ASTM A36 with stainless steel\n"
            "and non-metallic surfaces excluded is accepted."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
