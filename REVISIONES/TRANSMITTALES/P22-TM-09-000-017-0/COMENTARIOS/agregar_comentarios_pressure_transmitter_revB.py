"""
agregar_comentarios_pressure_transmitter_revB.py
Anota PDF Pressure Transmitter Datasheet Rev B (E36 / submittal 25007-0036).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01, NOTE-01
  2. PDFs en submittal 25007-0036: 4 (este script cubre Pressure Transmitter)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 2
  5. IDs coinciden con .md transmittal: OBS-01 / NOTE-01

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-012_B_DS_Pressure_Transmitter.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-012_B_DS_Pressure_Transmitter_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 36",
        "P22-LI-09-008-012_B Datasheet - Pressure Transmitter.pdf",
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
        "search": "Main Wetted Parts",
        "page_fallback": 2,
        "text": (
            "OBS-01: Hastelloy C wetted-\n"
            "parts material extended from PIT-09-\n"
            "007 (Rev A reply) to PIT-09-001/002/\n"
            "003/004/005/006/008 due to high TDS.\n"
            "Hastelloy C is ~3x SS316L unit cost\n"
            "and typically carries longer lead\n"
            "times in the IGP05S configurator.\n"
            "Confirm in writing: (a) impact on\n"
            "the Equipment Procurement Schedule\n"
            "for the Pressure Transmitter line\n"
            "item; (b) that the change does not\n"
            "extend turbocharger and feed\n"
            "equipment delivery dates.\n"
            "PIT-09-009 remains SS316L."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "Aluminium",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Page 2 declares\n"
            "'Material - Sealing: Aluminium' for\n"
            "PIT-09-009; page 3 declares\n"
            "'Hastelloy C' for the other eight\n"
            "PITs. Aluminium as sealing material\n"
            "in a brine module is unlikely;\n"
            "correct page 2 entry to actual\n"
            "sealing material (typically Viton,\n"
            "EPDM or PTFE for the SS316L low-\n"
            "pressure unit) on the IFC issue."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
