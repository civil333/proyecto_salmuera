"""
agregar_comentarios_grounding_revD.py
Anota PDF Grounding Layout Rev D (E36 / submittal 25007-0036).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01, NOTE-01
  2. PDFs en submittal 25007-0036: 4 (este script cubre Grounding Layout)
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

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-003_D_Grounding_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 36",
        "P22-DWG-09-007-003_D Grounding Point & Power Panel Location Layout.pdf",
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
        "search": "CONSOLIDATED COMMENT SHEET",
        "page_fallback": 1,
        "text": (
            "OBS-01: The embedded\n"
            "Consolidated Comment Sheet refers\n"
            "to TRANSMITTAL N15 / P22-DWG-09-\n"
            "007-004 / Cable Tray Layout and\n"
            "Support Details. This is the\n"
            "comment-closure sheet for the Cable\n"
            "Tray Layout drawing (-004), NOT for\n"
            "the Grounding Layout (-003).\n"
            "Replace with the correct comment-\n"
            "closure sheet documenting how the\n"
            "TM N15 NOTE on Rev C was\n"
            "incorporated into Rev D."
        ),
    },
]

# NOTE-01 se coloca directamente con PyMuPDF — la página 3 del plano tiene
# rotation=270 (landscape AutoCAD) y doc-annotator no preserva FreeText con
# rotación; usar add_freetext_annot con rotate=270 para que el texto quede
# visible sobre el cajetín revisions table del plano principal.
import fitz

NOTE_01_TEXT = (
    "NOTE-01: Title block REVISIONS table lists rows A, B, C, D "
    "with dates but no description column populated. Fill in the description "
    "for the change from Rev C to Rev D so revision intent is auditable on "
    "the drawing itself."
)

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)

    # Post-process: agregar NOTE-01 directamente con fitz sobre la pagina 3
    # rotada (rotation=270). Ubicacion sobre el cajetin (esquina derecha-
    # inferior cuando rotated, esquina izquierda-superior en mediabox crudo).
    doc = fitz.open(PDF_OUT)
    page = doc[2]
    # Mediabox 1684 x 2384, rotation 270 -> visible 2384 x 1684
    # Ubicar sobre franja derecha del cajetin visible (zona REVISIONS).
    rect = fitz.Rect(120, 1740, 540, 1940)
    annot = page.add_freetext_annot(
        rect,
        NOTE_01_TEXT,
        fontsize=11,
        fontname="helv",
        text_color=(0, 0, 0),
        fill_color=(1.0, 1.0, 0.7),
        align=fitz.TEXT_ALIGN_LEFT,
        rotate=270,
    )
    annot.set_border(width=1.2)
    annot.set_info(title="ADASA - Luis Rivera", subject="NOTE-01")
    annot.update()
    doc.saveIncr()
    doc.close()
    print(f"  [NOTE-01] pag 3 (rotated 270) -> rect 120,1740-540,1940")
