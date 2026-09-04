"""
agregar_comentarios_ga_antiscalant_tank.py
Anota el GA of Antiscalant Dosing Tank Rev B (TM N26, Code 3). len = 4
(OBS-01 + OBS-02 + NOTE-01 + NOTE-02).

Es un PLANO (general arrangement). La lamina del GA es la pagina 0-based = 1
(hoja A1 con NOZZLE SPECIFICATIONS + NOTES + ANCHORING DETAILS Detail 3).
Su texto es CAD vectorizado -> search=None + page_fallback=1.

Pagina ROTADA: page.rotation = 270. add_pdf_comments (v1.6) maneja la rotacion
automaticamente (text_rotate = page.rotation); NO se hardcodea 270.

Colocacion 2D: el default (search=None) cae en la esquina superior derecha
VISUAL (sobre NOTES). Se parchea _calcular_rect (sin tocar el archivo de la
skill) para posicionar cada caja en coordenadas de DISPLAY explicitas. El
circulo (NOZZLE ORIENTATION), el bloque NOTES, la tabla NOZZLE SPECIFICATIONS y
el cajetin fragmentan el espacio, asi que las cajas se reparten en dos zonas
libres: OBS-01/OBS-02 arriba-derecha (a la derecha del circulo, bajo NOTES,
sobre la tabla) y NOTE-01/NOTE-02 abajo-centro (bajo el circulo, a la derecha
del detalle de anclaje, a la izquierda del cajetin). Verificacion OBLIGATORIA
por render PNG (regla CLAUDE.md 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
import doc_annotator as da
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_B_GA_Antiscalant_Tank.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_B_GA_Antiscalant_Tank_CC_ADASA.pdf")

# Pagina 0-based de la lamina del GA (hoja A1).
GA_PAGE = 1

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 60",
        "P22-DWG-09-005-015_B GA of Antiscalant Dosing Tank.pdf",
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
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "OBS-01: Detail 3 shows only the anchor-lug\n"
            "geometry; the NCh 2369 seismic reaction\n"
            "loads and the anchor-bolt pattern (Zone 3,\n"
            "operating weight at the C.O.G.) are absent\n"
            "and BW Water's comment sheet defers them,\n"
            "leaving the OOCC foundation without input.\n"
            "Correct: add the anchor pattern and the\n"
            "seismic reaction loads, or reference the\n"
            "endorsed Seismic Calculation Report."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "OBS-02: the Notes state the total capacity\n"
            "(335 L) but omit the effective working\n"
            "volume (0.27 m3); the LEVEL MARKING row is\n"
            "blank. Correct: state the effective working\n"
            "volume and its level mark."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-01: the requirement that the P&ID Rev C\n"
            "annotate TK-09-002 with 0.34 m3 is an action\n"
            "on the P&ID, not this GA; tracked separately."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-02: the equipment tag TK-09-002 is not\n"
            "labelled on the GA; add it at re-issue."
        ),
    },
]

# ---------------------------------------------------------------------------
# Posicionamiento 2D explicito (DISPLAY coords; page.rect = 2384x1684 landscape,
# origen arriba-izquierda). Parche local de _calcular_rect.
# ---------------------------------------------------------------------------
SCALE = 2.0
GAP_Y = 12

h_obs01 = da._calc_height(COMENTARIOS[0]["text"], SCALE)
h_obs02 = da._calc_height(COMENTARIOS[1]["text"], SCALE)
h_note01 = da._calc_height(COMENTARIOS[2]["text"], SCALE)
h_note02 = da._calc_height(COMENTARIOS[3]["text"], SCALE)

# Zona arriba-derecha (a la derecha del circulo, bajo NOTES, sobre la tabla)
OBS_X = 1690
OBS_Y = 350
# Zona abajo-centro (bajo el circulo y bajo el rotulo NOZZLE ORIENTATION,
# a la derecha del detalle de anclaje, a la izquierda del cajetin)
NOTE_X = 1340
NOTE_Y = 1140

POSITIONS = [
    (OBS_X, OBS_Y),                              # OBS-01
    (OBS_X, OBS_Y + h_obs01 + GAP_Y),            # OBS-02
    (NOTE_X, NOTE_Y),                            # NOTE-01
    (NOTE_X, NOTE_Y + h_note01 + GAP_Y),         # NOTE-02
]

_pos_iter = iter(POSITIONS)

def _calcular_rect_fixed(page, found_rect, text):
    scale = da._scale_for_page(page)
    w = da._ANNOT_WIDTH * scale
    h = da._calc_height(text, scale)
    x0, y0 = next(_pos_iter)
    return da.fitz.Rect(x0, y0, x0 + w, y0 + h)

da._calcular_rect = _calcular_rect_fixed

if __name__ == "__main__":
    print("Heights:", h_obs01, h_obs02, h_note01, h_note02)
    print("Positions:", POSITIONS)
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
