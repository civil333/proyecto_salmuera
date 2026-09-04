"""
agregar_comentarios_io_list.py
Agrega anotaciones FreeText del TM N14 al PDF IO List Rev C.

Checklist pre-creacion (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: NOTE-02 (analyzer power supply voltage)
  2. PDFs en submittal 25007-0028: 7 (IO List, IL, DTL, 4 datasheets)
  3. Cross-cutting NOTEs: ninguna aplica a este PDF
  4. len(COMENTARIOS) = 1 == notes aplicables a este PDF
  5. IDs coinciden: NOTE-02

Anotaciones:
  NOTE-02 (MAYOR/naranja): Analyzer power supply voltage discrepancy — 220VAC vs 24VDC
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(
    os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".claude", "skills", "doc-annotator")
)
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_C_IO_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_C_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            "..", "..", "..", "..",
            "ENTREGAS_BWWATER",
            "ENTREGA 28",
            "25007-0028",
            "P22-LI-09-008-001_C IO List.pdf",
        )
    )
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print(f"ERROR: PDF no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "220VAC",
        "page_fallback": 1,
        "text": (
            "NOTE-02 (MAJOR): Analyzer power\n"
            "supply voltage discrepancy.\n"
            "IO List REMARKS shows '220VAC Supply'\n"
            "for ORPIT-09-001A, CIT-09-001B,\n"
            "CIT-09-004, CIT-09-005, PHIT-09-006.\n"
            "Instrument List Rev C specifies 24VDC.\n"
            "Incorrect voltage will result in\n"
            "equipment damage or interface circuit\n"
            "redesign during commissioning.\n"
            "Resolve and confirm definitive supply\n"
            "voltage prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
