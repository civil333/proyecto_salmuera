"""
agregar_comentarios_ga_cip_flushing_tank.py
Anota el GA of CIP Flushing Tank Rev A (TM N26, Code 2). len = 4
(OBS-01 + OBS-02 + NOTE-01 + NOTE-02).

Es un PLANO (general arrangement). La lamina del GA es la pagina 0-based = 1
(hoja A1 con la tabla NOZZLE SPECIFICATIONS + NOTES + DETAIL "X" holding lug).
Su texto es CAD vectorizado -> search=None + page_fallback=1.

Pagina ROTADA: page.rotation = 270. add_pdf_comments (v1.6) maneja la rotacion
automaticamente (dibuja en el content stream con text_rotate = page.rotation),
por eso NO se hardcodea 270 y NO se pasa parametro de rotacion.

Colocacion 2D: el default de la skill (search=None) cae en la esquina superior
derecha VISUAL = sobre el bloque NOTES; el borde derecho esta totalmente ocupado
(NOTES -> NOZZLE SPECIFICATIONS -> cajetin), asi que offset_y (solo vertical) no
alcanza una zona libre. Se parchea _calcular_rect (sin tocar el archivo de la
skill) para posicionar cada caja en coordenadas de DISPLAY explicitas, en la
banda inferior-izquierda libre (fuera del dibujo y del cajetin). Verificacion
OBLIGATORIA por render PNG (regla CLAUDE.md 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
import doc_annotator as da
from doc_annotator import MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-014_A_GA_CIP_Flushing_Tank.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-014_A_GA_CIP_Flushing_Tank_CC_ADASA.pdf")

# Pagina 0-based de la lamina del GA (hoja A1).
GA_PAGE = 1

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 60",
        "P22-DWG-09-005-014_A GA of CIP Flushing Tank.pdf",
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
        "page_fallback": GA_PAGE,
        "text": (
            "OBS-01: the general arrangement does not\n"
            "show the equipment tag TK-09-001 assigned\n"
            "by the datasheet and the Equipment List.\n"
            "Correct: add TK-09-001 at IFC Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "OBS-02: the GA nozzle schedule and the\n"
            "approved CIP Tank Datasheet disagree on the\n"
            "top opening ('Manhole 21in' vs 'Handhole\n"
            "DN300') and on two side connections (N42\n"
            "Spare, N97 Temp Sensor) not in the\n"
            "datasheet. Correct: reconcile and confirm\n"
            "which document governs."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-01: the GA carries the anchor-lug\n"
            "arrangement and mass properties (270 kg,\n"
            "C.O.G. 1475 mm), but the NCh 2369 anchor-\n"
            "bolt loads and seismic qualification belong\n"
            "to the Module Seismic Calculation Report;\n"
            "the drawing needs no change for this item."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-02: positive check - the HDPE body,\n"
            "PVC flanges and EPDM gaskets are fit for\n"
            "the CIP service at pH 2-12."
        ),
    },
]

# ---------------------------------------------------------------------------
# Posicionamiento 2D explicito en coordenadas de DISPLAY (page.rect = 2384x1684
# landscape; origen arriba-izquierda). Banda inferior-izquierda libre, en dos
# columnas para no exceder el alto de pagina. Parche local de _calcular_rect.
# ---------------------------------------------------------------------------
SCALE = 2.0                 # _scale_for_page cap para A1 (2384/595 -> 2.0)
W = da._ANNOT_WIDTH * SCALE  # 420
GAP_X = 30
COL_A = 110
COL_B = COL_A + W + GAP_X   # 560
Y_TOP = 1300
GAP_Y = 12

def _pos_for(text, col, y):
    return (col, y)

# Alto de cada caja segun la skill (word-wrap incluido)
h_obs01 = da._calc_height(COMENTARIOS[0]["text"], SCALE)
h_obs02 = da._calc_height(COMENTARIOS[1]["text"], SCALE)
h_note01 = da._calc_height(COMENTARIOS[2]["text"], SCALE)
h_note02 = da._calc_height(COMENTARIOS[3]["text"], SCALE)

# Columna A: OBS-01 arriba, OBS-02 debajo. Columna B: NOTE-01 arriba, NOTE-02 debajo.
POSITIONS = [
    (COL_A, Y_TOP),                          # OBS-01
    (COL_A, Y_TOP + h_obs01 + GAP_Y),        # OBS-02
    (COL_B, Y_TOP),                          # NOTE-01
    (COL_B, Y_TOP + h_note01 + GAP_Y),       # NOTE-02
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
