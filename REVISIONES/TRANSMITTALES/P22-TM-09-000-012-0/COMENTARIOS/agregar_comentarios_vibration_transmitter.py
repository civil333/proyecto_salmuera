"""
agregar_comentarios_vibration_transmitter.py
Agrega anotaciones FreeText del TM N12 al PDF Datasheet Vibration Transmitter Rev A.
Observaciones:
  OBS-01 (MAYOR): HART no documentado en datasheet -- confirmar soporte o proveer alternativa
  NOTE-01 (NOTE): Quantity "1 duty" para 3 TAGs VT-09-001/002/003
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-LI-09-008-014_A_Datasheet of Vibration Transmitter.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-LI-09-008-014_A_Datasheet of Vibration Transmitter_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_22 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 22"))
    matches = glob_module.glob(os.path.join(entrega_22, "P22-LI-09-008-014*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 22 con patron P22-LI-09-008-014*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "4 to 20 mA current outputs",
        "page_fallback": 1,
        "text": (
            "OBS-01 (MAJOR): HART not documented.\n"
            "Datasheet shows 4-20 mA output only;\n"
            "HART capability not specified.\n"
            "Technical Specification - Instrumentation\n"
            "requires 4-20 mA + HART for all field\n"
            "instruments. Confirm HART support with\n"
            "evidence in Rev B, or provide HART-\n"
            "capable unit / formal deviation."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Quantity - Duty",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Quantity discrepancy.\n"
            "Field shows 1 duty unit but header\n"
            "lists 3 TAGs (VT-09-001/002/003).\n"
            "Confirm procurement qty = 3 units:\n"
            "1x BH-09-001 (HP Pump),\n"
            "1x SIP-09-001 (Feed TC),\n"
            "1x SIP-09-002 (Interstage TC).\n"
            "Update field in Rev B."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
