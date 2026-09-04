"""
agregar_comentarios_data_transfer_list.py
Agrega anotaciones FreeText del TM N14 al PDF Data Transfer List Rev B.

Checklist pre-creacion (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: NOTE-05 (VT Modbus scaling)
  2. PDFs en submittal 25007-0028: 7 (IO List, IL, DTL, 4 datasheets)
  3. Cross-cutting NOTEs: NOTE-05 and NOTE-03 are related (VT range) but apply to
     different documents — NOTE-05 to DTL, NOTE-03 to IL
  4. len(COMENTARIOS) = 1 == notes aplicables a este PDF
  5. IDs coinciden: NOTE-05

Anotaciones:
  NOTE-05 (NOTE/azul): VT Modbus scale 0-25 mm/s may need updating for PCH420V-M12
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

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-004_B_Data_Transfer_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-004_B_Data_Transfer_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            "..", "..", "..", "..",
            "ENTREGAS_BWWATER",
            "ENTREGA 28",
            "25007-0028",
            "P22-LI-09-008-004_B Data Transfer List (Modbus TCPIP).pdf",
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
        "id": "NOTE-05",
        "fill": NOTE,
        "search": "0 - 25",
        "page_fallback": 3,
        "text": (
            "NOTE-05: VT Modbus scaling may\n"
            "need updating.\n"
            "VT-09-001/002/003 show 0-25 mm/s\n"
            "(consistent with previous IFM VTV122).\n"
            "Wilcoxon PCH420V-M12 supports\n"
            "programmable full-scale output.\n"
            "Align Modbus scaling with Instrument\n"
            "List calibrated range (see NOTE-03)\n"
            "prior to IFC (Rev 0)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
