"""
agregar_comentarios_outline_panel.py
Anota PLC/LCP Outline Panel Drawing Rev C (TM N27, Code 2). len = 4
(OBS-01 MENOR + OBS-02 MENOR + OBS-03 MENOR + NOTE-01).

Es un PLANO A3 apaisado (page.rect = 1191x842 pt, rotation = 0). La lamina de
notas/materialidad es la pagina 0-based = 2 (impresa 3): la tabla de 16 notas
llena la mitad izquierda; el cajetin esta abajo-derecha (y > ~560). El espacio
libre util es la franja arriba-derecha, x=[946,1178] (a la derecha de la tabla,
sobre el cajetin).

Posicionamiento 2D explicito: se parchea _calcular_rect para apilar las 4 cajas
en esa franja. La franja es angosta (~232 pt), asi que se reduce el fontsize a 6
(render 12 pt en A3, legible) para que las 4 cajas quepan sin invadir la tabla ni
el cajetin. rotation=0 -> sin transformacion de rotacion (mas simple que un plano
rotado). Verificacion OBLIGATORIA por render PNG (CLAUDE.md 3.8).
"""
import sys
import os
import shutil
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
import doc_annotator as da
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-008-001_C_Outline_Panel.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-008-001_C_Outline_Panel_CC_ADASA.pdf")

NOTES_PAGE = 2  # 0-based (impresa 3)

# Fontsize reducido para este plano (franja libre angosta). El render = _FONTSIZE*scale.
da._FONTSIZE = 6  # -> 12 pt en A3 (scale 2.0)

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 64",
        "P22-CD-09-008-001_C PLC-LCP Outline Panel Drawing.pdf",
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
        "page_fallback": NOTES_PAGE,
        "text": (
            "OBS-01: note 14 leaves the 30-34 mm\n"
            "cable-clamp diameter as 'TBC'.\n"
            "Correct: finalise it at Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": NOTES_PAGE,
        "text": (
            "OBS-02: note 7 puts the exterior\n"
            "frame/roof/panel/door under 'sheet\n"
            "steel (interior only)', but the COLOR\n"
            "row and sheet 5 make them SS316L.\n"
            "Correct: reword to split the exterior\n"
            "SS316L from the interior sheet steel."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": None,
        "page_fallback": NOTES_PAGE,
        "text": (
            "OBS-03: 'CABLE DNRY' (note 12), and TP1\n"
            "called 'Profibus-DP' vs its model\n"
            "PLX32-EIP-MBTCP (EtherNet/IP-Modbus\n"
            "gateway). Correct: fix the labels."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": NOTES_PAGE,
        "text": (
            "NOTE-01: the enclosure gate (TM N20)\n"
            "is closed - SS316L exterior, NEMA\n"
            "4X/IP66, galvanised/CRS internals per\n"
            "the RFI-002 reply, accepted. BW commits\n"
            "to re-issue the SLD to 'SS316L Panel,\n"
            "NEMA 4X/IP66' (tracked in Section 3)."
        ),
    },
]

# ---------------------------------------------------------------------------
# Posicionamiento 2D explicito. Franja libre arriba-derecha: x=[946,1178].
# ---------------------------------------------------------------------------
BOX_W = 230.0
X0 = 946.0
Y_TOP = 40.0
GAP_Y = 12.0
RENDER_FS = da._FONTSIZE * 2.0  # 12 pt


def _box_height(text):
    # cpl conservador para BOX_W a 12 pt (~0.55 em glyph)
    cpl = max(1, int((BOX_W - 8) / (RENDER_FS * 0.55)))
    vlines = 0
    for logical in text.split("\n"):
        n = len(logical)
        vlines += 1 if n == 0 else math.ceil(n / cpl)
    return vlines * (RENDER_FS * 1.35) + 14.0


_POS = []
_y = Y_TOP
for c in COMENTARIOS:
    h = _box_height(c["text"])
    _POS.append((X0, _y, h))
    _y += h + GAP_Y

_pos_iter = iter(_POS)


def _calcular_rect_fixed(page, found_rect, text):
    x0, y0, h = next(_pos_iter)
    return da.fitz.Rect(x0, y0, x0 + BOX_W, y0 + h)


da._calcular_rect = _calcular_rect_fixed

if __name__ == "__main__":
    print("Bottom of last box:", _POS[-1][1] + _POS[-1][2], "(page height 842)")
    print("Positions (x0,y0,h):", [(round(x), round(y), round(h)) for x, y, h in _POS])
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
