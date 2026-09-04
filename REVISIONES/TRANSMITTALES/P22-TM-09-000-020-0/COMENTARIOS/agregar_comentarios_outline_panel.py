"""
agregar_comentarios_outline_panel.py
Anota PDF PLC-LCP Outline Panel Drawing Rev A (TM N20).
len(COMENTARIOS) = 4 (OBS-01 + OBS-02 + OBS-03 en pag 2 spec sheet,
NOTE-01 en portada). Pagina 2 con texto extraible escaso -> search=None
+ page_fallback=1; el skill auto-evita colision entre las 3 cajas.
Colores: fill transmite severidad. Texto sin etiqueta de criticidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-CD-09-008-001_A_Outline_Panel.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-CD-09-008-001_A_Outline_Panel_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 46",
        "P22-CD-09-008-001_A PLC-LCP Outline Panel Drawing.pdf",
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
        "page_fallback": 1,
        "text": (
            "OBS-01: Panel Specification Sheet\n"
            "declares SHEET STEEL painted RAL 7035,\n"
            "zinc-plated plates, CRS hinges and IP55\n"
            "- contradicting LCP Datasheet Rev B\n"
            "(nVent FS66S, SS316L unpainted,\n"
            "NEMA 4X/IP66, highly corrosive ambient),\n"
            "the IFC Single Line Diagram label and the\n"
            "Technical Specification (NEMA 4X or IP\n"
            "equivalent). Correct: align this sheet to\n"
            "the LCP Datasheet Rev B enclosure in\n"
            "Rev B; enclosure fabrication release is\n"
            "gated on this decision."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: forced-air cooling (intake/\n"
            "exhaust fans + filter) is incompatible\n"
            "with NEMA 4X/IP66 unless rated filter-fan\n"
            "assemblies are specified; sheet declares\n"
            "For Outdoor Use while the panel installs\n"
            "inside the air-conditioned container.\n"
            "Correct: reconcile cooling design with\n"
            "protection class and installation\n"
            "environment in Rev B."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-03: PANEL WEIGHT row is a template\n"
            "placeholder (Insert actual panel weight\n"
            "here / TBD). Correct: declare actual\n"
            "weight for lifting and container floor\n"
            "loading in Rev B."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: cover shows project name typo\n"
            "PD Tattal and ADASA code\n"
            "P22-ET-09-008-001; correct code is\n"
            "P22-CD-09-008-001. Correct: fix title\n"
            "block in Rev B."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
