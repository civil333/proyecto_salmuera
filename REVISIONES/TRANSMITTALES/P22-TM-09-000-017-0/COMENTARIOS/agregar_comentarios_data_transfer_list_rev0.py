"""
agregar_comentarios_data_transfer_list_rev0.py
Anota PDF Data Transfer List Modbus TCP/IP Rev 0 (E35 / submittal 25007-0035).

Checklist (CLAUDE.md §3.10):
  1. Tabla NOTE del transmittal: NOTE-01, NOTE-02
  2. PDFs en submittal 25007-0035: 4 (este script cubre Data Transfer List)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 2
  5. IDs coinciden con .md transmittal: NOTE-01 / NOTE-02

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-004_0_Data_Transfer_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-004_0_Data_Transfer_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 35",
        "P22-LI-09-008-004_0 Data Transfer List (Modbus TCPIP).pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "DATA TRANSFER LIST (MODBUS TCP/IP)",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Modbus integration\n"
            "parameters not declared. Add header\n"
            "note covering: (a) PLC role\n"
            "(master/slave) toward ADASA DCS,\n"
            "(b) byte order for REAL/INT\n"
            "registers (Big-Endian vs\n"
            "Little-Endian, AB-CD vs CD-AB),\n"
            "(c) word swap configuration.\n"
            "From CONNECT column the convention\n"
            "reads PLC -> DCS (PLC as slave),\n"
            "but the document should state this\n"
            "explicitly so DCS engineer can\n"
            "configure the master driver without\n"
            "trial and error during commissioning."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "30007",
        "page_fallback": 3,
        "text": (
            "NOTE-02: Vibration scaling\n"
            "0-8.9 mm/s on registers 30007,\n"
            "30011 and 30016 (VT-09-001/002/003)\n"
            "sits below the Wilcoxon PCH420V-M12\n"
            "minimum programmable full-scale of\n"
            "12.7 mm/s declared in Instrument\n"
            "List Rev C (TM N14 NOTE-03 ref).\n"
            "Either confirm the actual model and\n"
            "full-scale setting against the\n"
            "manufacturer datasheet (model\n"
            "substitution undocumented?) or\n"
            "revise the scaling to a value\n"
            "within the supported range. Resolve\n"
            "before commissioning since the\n"
            "scaling sets the engineering units\n"
            "displayed at DCS and the alarm\n"
            "setpoints depend on it."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
