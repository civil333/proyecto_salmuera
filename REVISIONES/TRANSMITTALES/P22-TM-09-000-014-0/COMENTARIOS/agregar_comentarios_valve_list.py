"""
agregar_comentarios_valve_list.py
Agrega anotaciones FreeText del TM N14 al PDF Valve List Rev D.

Checklist pre-creacion (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: NOTE-01 (item 112 removal)
  2. PDFs en submittal 25007-0027: 2 (Valve List Rev D + Pressure Gauge DS Rev B)
  3. Cross-cutting NOTEs: ninguna
  4. len(COMENTARIOS) = 1 == notes aplicables a este PDF
  5. IDs coinciden: NOTE-01

Anotaciones:
  NOTE-01 (MAYOR/naranja): Safety relief valve item 112 removal — near PSV-09-001 (last item)
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

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_D_Valve_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_D_Valve_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            "..", "..", "..", "..",
            "ENTREGAS_BWWATER",
            "ENTREGA 27",
            "P22-LI-09-005-002_D Valve List.pdf",
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
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "PSV-09-001",
        "page_fallback": 1,
        "text": (
            "NOTE-01 (MAJOR): Item 112 removed.\n"
            "Rev C contained 112 items.\n"
            "Rev D contains 111 items.\n"
            "Item 112 (second PSV-09-002, safety\n"
            "relief valve) removed rather than\n"
            "assigned a unique TAG.\n"
            "Provide overpressure protection\n"
            "analysis confirming remaining PSV\n"
            "configuration is adequate, or\n"
            "reinstate with unique TAG."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
