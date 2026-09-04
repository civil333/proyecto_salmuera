"""
agregar_comentarios_control_arch.py
Agrega anotaciones FreeText del TM N10 al PDF Control Architecture Rev C.
Observaciones:
  OBS-04 (MAYOR): Autonomia UPS 8 horas no confirmada textualmente — TM N7 OBS-01 abierta
  NOTE-05 (NOTE): HMI Display Screenshots P22-BREAD-09-008-001 comprometido, no entregado
"""
import sys, os, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-CD-09-004-01_REV.C CONTROL ARCHITECTURE.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-CD-09-004-01_REV.C CONTROL ARCHITECTURE_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18",
        "P22-CD-09-004-01_REV.C CONTROL ARCHITECTURE.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": "UPS",
        "page_fallback": 3,
        "text": (
            "OBS-04: UPS — 8-hour autonomy not textually\n"
            "confirmed in this document.\n"
            "Provide written confirmation and UPS capacity\n"
            "calculation demonstrating 8-hour runtime\n"
            "for full module load.\n"
            "TM N7 OBS-01 remains open."
        ),
    },
    {
        "id": "NOTE-05",
        "fill": NOTE,
        "search": "HMI",
        "page_fallback": 3,
        "text": (
            "NOTE-05: HMI Display Screenshots\n"
            "P22-BREAD-09-008-001 committed\n"
            "in CCS Item 4 (response to TM N4)\n"
            "but not yet submitted.\n"
            "Required: Submit with Entrega 19."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
