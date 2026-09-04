"""
agregar_comentarios_data_transfer.py
Agrega anotaciones FreeText del TM N10 al PDF Data Transfer List Rev A.
Observaciones:
  OBS-01 (MENOR): Inconsistencia tags TIT09-xxx vs TE09-xxx (IO List Rev B)
  OBS-02 (MAYOR): Rangos conductividad incorrectos para servicio salmuera concentrada
  OBS-03 (MAYOR): Direcciones Modbus 10002.5-10002.6 reasignadas incorrectamente
"""
import sys, os, shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-LI-09-008-004_REV.A Data Transfer List (Modbus TCPIP).pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-LI-09-008-004_REV.A Data Transfer List (Modbus TCPIP)_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 18",
        "P22-LI-09-008-004_REV.A Data Transfer List (Modbus TCPIP).pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MENOR,
        "search": "TIT09-002",
        "page_fallback": 2,
        "text": (
            "OBS-01: Tag inconsistency — DTL uses\n"
            "TIT09-002/003/004/005; IO List Rev B uses\n"
            "TE09-002/003/004/005 for same instruments.\n"
            "Resolve and standardize tags in Rev B."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "CIT-09-001",
        "page_fallback": 2,
        "text": (
            "OBS-02: CIT-09-001/004/005 — Range 0-20 mS/cm\n"
            "incorrect for concentrated brine service.\n"
            "Required: CIT-09-001: 65-80 mS/cm,\n"
            "CIT-09-004: 85-108 mS/cm,\n"
            "CIT-09-005: 108-133 mS/cm.\n"
            "Toroidal transmitter (Rosemount 228) mandatory.\n"
            "ET — Conductivity Transmitters."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "VE09-014",
        "page_fallback": 3,
        "text": (
            "OBS-03: Modbus addresses 10002.5-10002.6\n"
            "misassigned to VE09-014 position signals.\n"
            "These addresses should be: LS09-001\n"
            "(HIGH level alarm) and LS09-002 (LOW level\n"
            "alarm), currently absent from Modbus map.\n"
            "Reassign and add missing level alarms."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
