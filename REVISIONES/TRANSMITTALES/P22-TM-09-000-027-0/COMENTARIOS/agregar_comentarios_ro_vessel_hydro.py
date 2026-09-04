"""
agregar_comentarios_ro_vessel_hydro.py
Anota RO Vessel Hydrostatic Test Procedure Rev C (TM N27, Code 2). len = 3
(OBS-01 MENOR + OBS-02 MENOR + NOTE-01). Documento de texto -> search directo.

Paginas 1-based del PDF Rev C (22 pags):
  OBS-01 = pag 9 (cuerpo: regla generica 1.1x sin presion numerica vinculante)
  OBS-02 = pag 8 (ventana de seleccion de manometro que el propio proc. enuncia)
  NOTE-01 = pag 11 (test report real 17-Jun: 91,01 / 136,52 bar = 1.1x diseno)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-009_C_RO_Vessel_Hydrostatic.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-009_C_RO_Vessel_Hydrostatic_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 64",
        "P22-BA-09-000-009_C RO Vessel Hydrostatic Test Procedure.pdf",
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
        "fill": MENOR,
        "search": "design pressure for ASME certified vessels",
        "page_fallback": 8,
        "text": (
            "OBS-01: the body states only the generic\n"
            "1.1x design-pressure rule and writes no\n"
            "binding numeric test pressure, though the\n"
            "attached report fixes the values.\n"
            "Correct: state the governing pressures on\n"
            "the face - 1,320 psi (91.0 bar) for the\n"
            "BPV81200SP7 and 1,980 psi (136.5 bar) for\n"
            "the BPV81800SP7. The attached report already\n"
            "evidences compliance; no re-test is required."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "not exceeding four times nor less than 1.5 times",
        "page_fallback": 7,
        "text": (
            "OBS-02: the procedure requires the test gauge\n"
            "to read 1.5 to 4 times the test pressure. For\n"
            "the 136.5 bar test (BPV81800SP7 vessels) that\n"
            "is a 205-546 bar gauge. Neither attached\n"
            "certificate fits: the 0-160 bar gauge (cert\n"
            "27258) is below the 1.5x minimum (full scale\n"
            "1.17x the test) and the 0-2500 bar gauge (cert\n"
            "27249) is above the 4x maximum. Correct:\n"
            "confirm which gauge was used for the 136.5 bar\n"
            "test and attach its certificate, within the\n"
            "1.5-to-4x range."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "DIMENSIONAL AND HYDROSTATIC TEST REPORT",
        "page_fallback": 10,
        "text": (
            "NOTE-01: this report closes the critical\n"
            "observation carried since Transmittal N23\n"
            "and re-stated at N26 - the vessels were\n"
            "tested at 1.1x their design pressures. The\n"
            "ASME stamp waiver of 02-Jun is not reopened,\n"
            "and a single calibrated gauge is accepted\n"
            "for the vessel hydrostatic test."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
