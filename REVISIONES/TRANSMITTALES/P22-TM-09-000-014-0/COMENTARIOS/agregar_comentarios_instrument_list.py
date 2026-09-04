"""
agregar_comentarios_instrument_list.py
Agrega anotaciones FreeText del TM N14 al PDF Instrument List Rev C.

Checklist pre-creacion (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: NOTE-03 (VT calibrated range), NOTE-04 (working medium)
  2. PDFs en submittal 25007-0028: 7 (IO List, IL, DTL, 4 datasheets)
  3. Cross-cutting NOTEs: NOTE-03 and NOTE-05 are related (VT range) but apply to
     different documents — NOTE-03 to IL, NOTE-05 to DTL
  4. len(COMENTARIOS) = 2 == notes aplicables a este PDF
  5. IDs coinciden: NOTE-03, NOTE-04

Anotaciones:
  NOTE-03 (NOTE/azul): VT calibrated range 0-127 mm/s vs DTL 0-25 mm/s
  NOTE-04 (NOTE/azul): Working medium "Filtered Water" for brine-side instruments
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(
    os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".claude", "skills", "doc-annotator")
)
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-003_C_Instrument_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-003_C_Instrument_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            "..", "..", "..", "..",
            "ENTREGAS_BWWATER",
            "ENTREGA 28",
            "25007-0028",
            "P22-LI-09-008-003_C Instrument List.pdf",
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
        "id": "NOTE-03",
        "fill": NOTE,
        "search": "127",
        "page_fallback": 1,
        "text": (
            "NOTE-03: VT calibrated range\n"
            "discrepancy.\n"
            "Instrument List shows 0-127 mm/s.\n"
            "Data Transfer List Rev B uses\n"
            "0-25 mm/s as Modbus scaled range.\n"
            "Wilcoxon PCH420V-M12 supports\n"
            "programmable full-scale 12.7-127 mm/s.\n"
            "Confirm intended PLC 4-20mA scaling\n"
            "and align prior to IFC (Rev 0)."
        ),
    },
    {
        "id": "NOTE-04",
        "fill": NOTE,
        "search": "Filtered Water",
        "page_fallback": 1,
        "text": (
            "NOTE-04: Working medium label\n"
            "for brine-side instruments.\n"
            "CIT-09-001B, CIT-09-004, CIT-09-005,\n"
            "PIT-09-007, PIT-09-006, FIT-09-004,\n"
            "and PIT-09-008 show 'Filtered Water'\n"
            "but are installed in concentrated\n"
            "brine service (TDS >43,000 mg/L).\n"
            "Update working medium designation\n"
            "prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
