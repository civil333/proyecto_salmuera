"""
agregar_comentarios_io_list.py
Agrega anotaciones FreeText del TM N10 al PDF IO List Rev B.
Observaciones:
  OBS-01 (MAYOR): Inconsistencia de tags TE09-xxx vs TIT09-xxx entre IO List y DTL
  NOTE-01 (NOTE): Senales DI de habilitacion — especificar tipo relay contact
"""
import sys, os, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_REV.B IO List.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_REV.B IO List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18", "P22-LI-09-008-001_REV.B IO List.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "TE09-002",
        "page_fallback": 2,
        "text": (
            "OBS-01: Tag inconsistency — IO List uses\n"
            "TE09-002/003/004/005; Data Transfer List\n"
            "Rev A uses TIT09-002/003/004/005 for same\n"
            "instruments. Unified tag convention required.\n"
            "Resolve in Rev C."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "24VDC",
        "page_fallback": 1,
        "text": (
            "NOTE-01: DI enable signals (items 19 and 21)\n"
            "— Specify relay contact output type.\n"
            "Do not use generic '24VDC dry contact'.\n"
            "Required: relay contact output from ADASA PLC.\n"
            "Confirmed per TM N10 Section 3."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
