#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_equipment_layout_revD.py
Anota el Equipment Layout Rev D (P22-DWG-09-005-003), submittal 25007-0078
(E78). Veredicto del TM N33: Code 2 - Approved as noted.

len(COMENTARIOS) = 4, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. La Rev D cerro las TRES observaciones que devolvieron la Rev C en el
TM N22, y ninguna de las tres se anota:
  - OBS-01 filtro de cartucho RO vertical: CERRADA, verificada por render a 500
    dpi (en planta es circunferencia sobre base cuadrada = recipiente vertical).
  - OBS-02 tabla de pesos: CERRADA por empotramiento, que era una de las dos
    vias ofrecidas.
  - OBS-03 rotulo del panel: la mitad del rotulo cerro; lo que falta va en
    OBS-04.
Lo que se anota es contenido nuevo de la Rev D y consistencia con documentos
aprobados. NO se imputa falta por haber empotrado la tabla: ADASA ejerce ahora
la segunda via que su propio TM N22 ofrecio.

Estructura del archivo (indices 0-based):
    0   caratula A4
    1   lamina A1 apaisada, rotation 0, planta + tabla de 17 filas
    2   Consolidated Comment Sheet (hoja 1)
    3   Consolidated Comment Sheet (hoja 2)
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

# --- Fast-save guard: 13.834 vectores en la lamina A1 ----------------------
import fitz  # noqa: E402
_orig_save = fitz.Document.save


def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)


fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-003_D_Equipment_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-003_D_Equipment_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 78",
        "P22-DWG-09-005-003_Equipment Layout_Rev.D.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: this table and the one in the Civil and\n"
            "Loading Layout P22-DWG-09-005-001 Rev B are both\n"
            "live and they do not agree. ADASA has accepted\n"
            "in writing the second route offered at\n"
            "Transmittal N22: that drawing is the single\n"
            "source of equipment weights, being the one that\n"
            "dimensions the foundations and the only one\n"
            "separating dry from operating weight.\n"
            "Correct: replace this table with a reference to\n"
            "P22-DWG-09-005-001. No fault is attributed for\n"
            "having embedded it."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: row 1 of the table tags the static mixer\n"
            "MZE-09-009. The binding tag is MZE-09-001, as\n"
            "the Equipment List P22-LI-09-005-001 Rev B\n"
            "carries it and as BW Water confirmed in writing\n"
            "in the comment sheet of that list: \"Static mixer\n"
            "tag is MZE-09-001\". The Process Flow Diagram of\n"
            "this same submittal also uses MZE-09-001.\n"
            "Correct: adopt MZE-09-001."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-03: row 14 states 989.2 kg as LCP Panel and\n"
            "Instrumentation, where the Civil and Loading\n"
            "Layout Rev B of four days earlier states 800.0 kg\n"
            "as Local Control Panel. The 189.2 kg increment is\n"
            "not the instruments row of that drawing, which is\n"
            "182.9 kg, and row 17 here, Instrument Panels,\n"
            "carries no weight, so those panels may be counted\n"
            "in row 14, in the empty row 17, or twice.\n"
            "Correct: state the figure that governs and what\n"
            "it includes, so the single source carries it."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-04: the main panel is now labelled, which\n"
            "closes half of the point raised at Transmittal\n"
            "N22. The other half was to unify its name and\n"
            "position with the Grounding Point and Power Panel\n"
            "Location Layout P22-DWG-09-007-003 Rev F, which\n"
            "identifies it as P22-LCP-01, LCP / Main\n"
            "Switchboard. Row 14 here reads LCP Panel and\n"
            "Instrumentation with the TAG column at N/A, and\n"
            "Rev F was prepared on the Equipment Layout Rev B\n"
            "at ADASA's instruction, two revisions back.\n"
            "Correct: unify the name and tag with those of\n"
            "Rev F, and confirm that the panel position is\n"
            "unchanged from the Rev B baseline."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
