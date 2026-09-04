"""
agregar_comentarios_turbo1.py
Agrega anotaciones FreeText del TM N10 al PDF GA SIP-09-001 (1st Stage Turbocharger) Rev A.
Nota: El archivo en ENTREGA 18 puede tener un zero-width space en el nombre.
      Se usa glob para encontrarlo y se guarda con nombre normalizado.
Observaciones:
  OBS-06 (MAYOR): Previsiones para transductor de vibracion VT09-002
  NOTE-03 (NOTE): Coupling pressure rating — Style 77 certificate + deviation disposition
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-012_REV.A GA of 1st Stage Turbo.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-012_REV.A GA of 1st Stage Turbo_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_18 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18"))
    matches = glob_module.glob(os.path.join(entrega_18, "P22-DWG-09-005-012*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS (normalizado sin zero-width space).")
    else:
        print(f"ERROR: PDF no encontrado en ENTREGA 18 con patron P22-DWG-09-005-012*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-06",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-06 (MAJOR): This drawing does not show\n"
            "where vibration sensor VT09-002 will be\n"
            "installed on the unit. Rev B must add a\n"
            "mounting point on the casing (threaded boss\n"
            "or bracket) for the vibration transducer."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": "GROOVE",
        "page_fallback": 0,
        "text": (
            "NOTE-03: Coupling pressure rating — All\n"
            "nozzles use CUT GROOVE STYLE 77.\n"
            "Provide working pressure rating certificate\n"
            "for Style 77 at 1.5\" and 2\" bore.\n"
            "Also provide deviation disposition\n"
            "resolving TM N6 OBS-01 (coupling\n"
            "previously rejected at 1,200 psi;\n"
            "operating pressure ~1,008 psi)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
