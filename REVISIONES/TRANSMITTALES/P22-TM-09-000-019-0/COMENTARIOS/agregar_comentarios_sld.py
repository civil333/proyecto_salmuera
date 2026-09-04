"""
agregar_comentarios_sld.py
Anota PDF Single Line Diagram Rev B (E42 / 25007-0042).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.4: OBS-01 + NOTE-01 = 2
  2. PDFs en submittal 25007-0042: 7 (este es 1 de los Code 2)
  3. Cross-cutting: NEMA 4X / IP66 referencia Technical Specification — Cabinets
  4. len(COMENTARIOS) = 2
  5. IDs coinciden: Section 2.4 del transmittal TM N19

Veredicto: 2 - Approved as noted (primer review formal del SLD)
Colores: fill MENOR (amarillo) — ambos items severidad MINOR.
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-CD-09-007-001_B_Single_Line_Diagram.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-CD-09-007-001_B_Single_Line_Diagram_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 42",
        "P22-CD-09-007-01_B Single Line Diagram.pdf",
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
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-01: Principal enclosure rating NEMA\n"
            "4X or equivalent IP not declared on the\n"
            "diagram. Add at IFC Rev 0 the principal\n"
            "enclosure rating per Technical\n"
            "Specification — Cabinets (compatible with\n"
            "outdoor coastal environment, IP66 or\n"
            "NEMA 4X). No new Single Line Diagram\n"
            "revision required."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: Surge protection devices on the\n"
            "main incoming feeder are not visible on\n"
            "the diagram. Add at IFC Rev 0 the SPD\n"
            "location and rating consistent with the\n"
            "incoming-feeder protection coordination\n"
            "(Technical Specification — Electrical\n"
            "Protections, Section 5.4.4)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
