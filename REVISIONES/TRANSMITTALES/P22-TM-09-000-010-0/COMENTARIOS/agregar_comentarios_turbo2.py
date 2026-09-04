"""
agregar_comentarios_turbo2.py
Agrega anotaciones FreeText del TM N10 al PDF GA SIP-09-002 (2nd Stage Turbocharger) Rev A.
Observaciones:
  OBS-07 (MAYOR): Previsiones para transductor de vibracion VT09-003
  NOTE-04 (NOTE): Coupling pressure rating — identico a SIP-09-001 (NOTE-03), certificate debe cubrir ambas unidades
"""
import sys, os, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-013_GA of 2nd Stage Turbo.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-013_GA of 2nd Stage Turbo_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18",
        "P22-DWG-09-005-013_GA of 2nd Stage Turbo.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-07",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-07 (MAJOR): This drawing does not show\n"
            "where vibration sensor VT09-003 will be\n"
            "installed on the unit. Rev B must add a\n"
            "mounting point on the casing (threaded boss\n"
            "or bracket) for the vibration transducer."
        ),
    },
    {
        "id": "NOTE-04",
        "fill": NOTE,
        "search": "GROOVE",
        "page_fallback": 0,
        "text": (
            "NOTE-04: Coupling pressure rating — All\n"
            "nozzles use CUT GROOVE STYLE 77.\n"
            "Provide working pressure rating certificate\n"
            "for Style 77 at 1.5\" and 2\" bore.\n"
            "Requirement identical to SIP-09-001\n"
            "(NOTE-03). Certificate must cover both units."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
