"""
agregar_comentarios_ro_hydrostatic.py
Anota PDF RO Vessel Hydrostatic Test Procedure Rev B (TM N26, Code 3). len(COMENTARIOS) = 4
(OBS-01 CRITICAL + OBS-02 MAYOR + OBS-03 MENOR + NOTE-01). Colores: fill transmite
severidad; el texto FreeText arranca directo con "OBS-XX:" / "NOTE-01:" sin etiqueta
de criticidad. Paginas 0-based: OBS-01=8 (impresa 9, rama CE 1.43x), OBS-02=9
(impresa 10, calibracion), OBS-03=6 (impresa 7, index Rev 0), NOTE-01=7 (impresa 8,
RT-5).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-009_B_RO_Vessel_Hydrostatic.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-009_B_RO_Vessel_Hydrostatic_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 61",
        "P22-BA-09-000-009_B RO Vessel Hydrostatic Test Procedure.pdf",
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
        "fill": CRITICAL,
        "search": "1.43 times the design pressure for CE",
        "page_fallback": 8,
        "text": (
            "OBS-01: the body states no binding test\n"
            "pressure and the embedded Protec form still\n"
            "prints 45.5 bar against the required 1,980\n"
            "psi (BPV-8-1800-SP-7) and 1,320 psi\n"
            "(BPV-8-1200-SP-7); the CE 1.43x branch\n"
            "remains.\n"
            "Correct: state the project test pressure by\n"
            "model in the body and the report form, and\n"
            "remove the 45.5 bar default and the CE\n"
            "branch."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Auxiliary pressure gauge will be calibrated",
        "page_fallback": 9,
        "text": (
            "OBS-02: the procedure lists a single\n"
            "calibrated gauge and no certificate review,\n"
            "against the two-gauge, certificate-review\n"
            "traceability its own HP/LP Pressure Test\n"
            "Procedure applies.\n"
            "Correct: require two calibrated gauges and a\n"
            "certificate check before the test."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": None,
        "page_fallback": 6,
        "text": (
            "OBS-03: the embedded Protec procedure keeps\n"
            "'Revision: 0' on one index page after being\n"
            "renumbered to Rev B on the others.\n"
            "Correct: harmonise the revision block on all\n"
            "pages."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "This procedure describes the performance of hydrostatic",
        "page_fallback": 7,
        "text": (
            "NOTE-01: the RT-5 hold time and the\n"
            "acceptance criterion (ASME Section X RT-5,\n"
            "1-minute minimum, reject above a 10% drop)\n"
            "are declared; this folds into the next\n"
            "revision."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
