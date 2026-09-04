"""
agregar_comentarios_ga_pump_skid.py
Anota el GA of Antiscalant Dosing Pump Skid Rev B (TM N26, Code 2). len = 3
(OBS-01 + NOTE-01 + NOTE-02).

Es un PLANO (general arrangement). La lamina del GA es la pagina 0-based = 1
(hoja A1: PLAN VIEW / ISOMETRIC / BOLTING EMBEDMENT / PIPING ARRANGEMENT + NOTES
+ cajetin). Su texto es CAD vectorizado -> search=None + page_fallback=1.

Pagina ROTADA: page.rotation = 270. add_pdf_comments (v1.6) maneja la rotacion
automaticamente (dibuja en el content stream con text_rotate = page.rotation),
por eso NO se hardcodea 270 y NO se pasa parametro de rotacion.

Colocacion 2D: el default de la skill (search=None) cae en la esquina superior
derecha VISUAL = sobre el bloque NOTES; el borde derecho esta totalmente ocupado
(NOTES arriba -> cajetin abajo), y el hueco libre de esa columna (~370 u) no
alcanza para las 3 cajas apiladas (~570 u), asi que offset_y (solo vertical) no
alcanza una zona libre sin tapar el cajetin. Se parchea _calcular_rect (sin tocar
el archivo de la skill) para posicionar cada caja en coordenadas de DISPLAY
explicitas: una columna sobre la vista ISOMETRICA (pictorico de baja informacion),
dejando visibles el patron de pernos del PLAN VIEW, las fuerzas del bloque NOTES,
el detalle BOLTING EMBEDMENT, las bombas del PIPING ARRANGEMENT y el cajetin.
Verificacion OBLIGATORIA por render PNG (regla CLAUDE.md 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
import doc_annotator as da
from doc_annotator import MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-011_B_GA_Antiscalant_Pump_Skid.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-011_B_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf")

# Pagina 0-based de la lamina del GA (hoja A1).
GA_PAGE = 1

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 62",
        "P22-DWG-09-005-011_B GA of Antiscalant Dosing Pump Skid.pdf",
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
            "OBS-01: the per-bolt forces in the\n"
            "Bolting Embedment detail (Fz=0.205 kN)\n"
            "are not consistent with the total\n"
            "reaction block (total Fz=0.2048 kN)\n"
            "over the 10-bolt count - an apparent\n"
            "10x discrepancy - while per-bolt Fx\n"
            "does equal total/10. Correct: label\n"
            "each block as per-bolt or group-total\n"
            "and reconcile the per-bolt Fz with the\n"
            "endorsed calc report."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-01: the reaction forces are 'as\n"
            "per calculation report' and the bolting\n"
            "details are 'to be finalized and\n"
            "endorsed'; the endorsed Module Seismic\n"
            "Calculation Report is a separate\n"
            "deliverable tracked in Section 3."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": GA_PAGE,
        "text": (
            "NOTE-02: positive check - the two\n"
            "dosing pumps BDS-09-001/002 match the\n"
            "Technical Offer Rev.1; the PE cabinet\n"
            "and clear PVC door introduce no\n"
            "material conflict."
        ),
    },
]

# ---------------------------------------------------------------------------
# Posicionamiento 2D explicito en coordenadas de DISPLAY (page.rect = 2384x1684
# landscape; origen arriba-izquierda). Una sola columna sobre la vista ISOMETRICA
# (x aprox 763-1359), fuera del PLAN VIEW, NOTES, BOLTING, PIPING y del cajetin.
# Parche local de _calcular_rect (no toca el archivo de la skill).
# ---------------------------------------------------------------------------
SCALE = 2.0                  # _scale_for_page cap para A1 (2384/595 -> 2.0)
W = da._ANNOT_WIDTH * SCALE   # 420
COL = 820                    # x0 de la columna (centrada sobre el isometrico)
Y_TOP = 175
GAP_Y = 14

# Alto de cada caja segun la skill (word-wrap incluido)
h_obs01 = da._calc_height(COMENTARIOS[0]["text"], SCALE)
h_note01 = da._calc_height(COMENTARIOS[1]["text"], SCALE)
h_note02 = da._calc_height(COMENTARIOS[2]["text"], SCALE)

POSITIONS = [
    (COL, Y_TOP),                                        # OBS-01
    (COL, Y_TOP + h_obs01 + GAP_Y),                      # NOTE-01
    (COL, Y_TOP + h_obs01 + GAP_Y + h_note01 + GAP_Y),   # NOTE-02
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
    print("Heights:", h_obs01, h_note01, h_note02)
    print("Positions:", POSITIONS)
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
