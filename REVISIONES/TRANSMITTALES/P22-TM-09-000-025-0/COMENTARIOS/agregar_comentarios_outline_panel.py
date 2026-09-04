"""
agregar_comentarios_outline_panel.py
Anota el PLC-LCP Outline Panel Drawing Rev B (TM N25, Code 3). len = 4
(OBS-01 + OBS-02 + NOTE-01 + NOTE-02). El cuadro de especificacion vive en la
hoja A1 (pagina 0-based = 1, "SHEET P1"); su texto es CAD vectorizado (search
falla) -> page_fallback=1, search=None. Plano NO rotado (rotation=0). VERIFICAR
SIEMPRE por render PNG (regla CLAUDE.md 3.8). offset_y empuja las cajas a la zona
libre superior-izquierda fuera del cuadro y del cajetin.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-008-001_B_Outline_Panel.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-008-001_B_Outline_Panel_CC_ADASA.pdf")

# Pagina 0-based del cuadro de especificacion (hoja A1 "SHEET P1").
SPEC_PAGE = 1

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 55",
        "P22-CD-09-008-001_B PLC-LCP Outline Panel Drawing.pdf",
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
        "fill": CRITICAL,
        "search": None,
        "page_fallback": SPEC_PAGE,
        "text": (
            "OBS-01: MATERIAL (SHEET STEEL, 'interior\n"
            "only') and FINISHING (RAL 7035) for the\n"
            "frame/roof/rear panel/door contradict the\n"
            "sheet's own 'Exterior SUS316L' and the\n"
            "approved docs that govern the enclosure:\n"
            "LCP Datasheet Rev B (SS316L, NEMA 4X/IP66)\n"
            "and the Single Line Diagram. ET requires\n"
            "NEMA 4X; SS316L is fixed by the datasheet.\n"
            "Correct: align the spec to SS316L on the\n"
            "weather-exposed surfaces."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": SPEC_PAGE,
        "text": (
            "OBS-02: the bottom gland plate is zinc-\n"
            "plated on an outdoor coastal NEMA 4X panel.\n"
            "Correct: specify SS316L for the exterior\n"
            "bottom gland plate, or confirm it is\n"
            "shielded from the weather."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": SPEC_PAGE,
        "text": (
            "NOTE-01: PROTECTION CLASS prints 'Nema 4X'\n"
            "without IP66. Correct: add '/IP66' to match\n"
            "the LCP Datasheet and the Single Line Diagram."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": SPEC_PAGE,
        "text": (
            "NOTE-02: title-block project title misspelled\n"
            "('SECONDE STAGE'); discipline reads 'Process'.\n"
            "Correct: fix at IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
