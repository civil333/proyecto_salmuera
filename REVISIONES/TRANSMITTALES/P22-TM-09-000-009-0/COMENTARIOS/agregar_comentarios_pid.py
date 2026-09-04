"""
agregar_comentarios_pid.py
Agrega 2 anotaciones FreeText del TM N9 al PDF P&ID Rev B.
Tecnologia: PyMuPDF (fitz). Fill color distingue severidad.

Notas (TM N9 — Veredicto 2, Approved as Noted):
  NOTE-01 (MINOR) : Codigo de documento truncado (-02 vs -002) en title block
  NOTE-02 (MINOR) : TK-09-002 anotado con 0.27 m3 (volumen efectivo); total instalado = 0.34 m3

Nota: VM-09-015 aparece correctamente como VM (manual) en el P&ID.
  TM N3 OBS-11 fue formalmente RETIRADA (correo ADASA 05-Mar-2026):
  la valvula es aislamiento manual entre HP Pump y Feed Turbocharger,
  no es valvula de control de proceso. ET — Valves and Piping no aplica.
  Inconsistencia pendiente en Valve List Rev B item 18 (ON/OFF MOTORIZED) —
  debe corregirse a MANUAL en Rev C.
"""
import fitz  # PyMuPDF
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTREGA_17  = os.path.join(
    SCRIPT_DIR,
    "..", "..", "..", "..",
    "ENTREGAS_BWWATER", "ENTREGA 17",
    "P22-DWG-09-009-02_REV.B Piping & Instrumentation Diagram.pdf",
)
ENTREGA_17 = os.path.normpath(ENTREGA_17)

# Tambien buscar en la misma carpeta COMENTARIOS (copia local)
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-009-02_REV.B P&ID.pdf")

PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-009-02_REV.B_CC_ADASA.pdf")

# Fill colors por severidad
MAYOR  = (1.0, 0.90, 0.75)   # naranja claro
MENOR  = (1.0, 1.00, 0.70)   # amarillo claro

ANNOT_WIDTH = 210
LINE_HEIGHT = 11
FONTSIZE    = 8
MARGIN      = 10


COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "P22-DWG-09-009-02",
        "page_fallback": 0,           # title block, pagina 1
        "text": (
            "NOTE-01 (MINOR): Codigo de documento\n"
            "en title block: P22-DWG-09-009-02\n"
            "El correlativo del proyecto usa\n"
            "3 digitos: P22-DWG-09-009-002.\n"
            "El CCS (paginas 13-17) usa el\n"
            "codigo correcto -002.\n"
            "Corregir title block en Rev C."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": "TK-09-002",
        "page_fallback": 11,          # pagina 12 (0-based=11), area antiscalant
        "text": (
            "NOTE-02 (MINOR): TK-09-002 anotado\n"
            "como VOL: 0.27 m3 (volumen efectivo).\n"
            "Datasheet aceptado (P22-ET-09-009-010\n"
            "Rev B, TM N4): total = 0.34 m3,\n"
            "efectivo = 0.27 m3.\n"
            "TM N4 OBS-11 solicito actualizar a\n"
            "0.34 m3 (capacidad total instalada).\n"
            "Convencion P&ID: anotar volumen total.\n"
            "Actualizar a 0.34 m3 en Rev C."
        ),
    },
]


def calc_height(text):
    nlines = text.count("\n") + 1
    return max(70, nlines * LINE_HEIGHT + 18)


def buscar_en_paginas(doc, search_text, min_page=0):
    """Retorna (page_idx, primer_rect) o (None, None)."""
    for idx in range(min_page, len(doc)):
        hits = doc[idx].search_for(search_text)
        if hits:
            return idx, hits[0]
    return None, None


def calcular_rect(page, found_rect, text):
    """Posiciona la caja a la derecha del texto o en esquina superior-derecha."""
    pw = page.rect.width
    ph = page.rect.height
    w = ANNOT_WIDTH
    h = calc_height(text)

    if found_rect is not None:
        x0 = found_rect.x1 + 4
        y0 = found_rect.y0
        if x0 + w > pw - MARGIN:
            x0 = found_rect.x0
            y0 = found_rect.y1 + 6
        x0 = min(max(x0, MARGIN), pw - MARGIN - w)
        y0 = min(max(y0, MARGIN), ph - h - MARGIN)
    else:
        x0 = pw - MARGIN - w
        y0 = 20

    return fitz.Rect(x0, y0, x0 + w, y0 + h)


def evitar_colision(rect, placed_rects):
    """Desplaza hacia abajo si colisiona con rects ya colocados."""
    for existing in placed_rects:
        if rect.intersects(existing):
            dy = existing.y1 + 8 - rect.y0
            rect = fitz.Rect(rect.x0, rect.y0 + dy,
                             rect.x1, rect.y1 + dy)
    return rect


def main():
    # Copiar PDF fuente limpio a COMENTARIOS si no existe ya
    if not os.path.exists(PDF_LOCAL):
        if os.path.exists(ENTREGA_17):
            shutil.copy2(ENTREGA_17, PDF_LOCAL)
            print(f"PDF fuente copiado a COMENTARIOS.")
        else:
            print(f"ERROR: PDF no encontrado:\n  {ENTREGA_17}")
            print("\nVerifica que la ruta de ENTREGA 17 sea correcta.")
            return

    doc = fitz.open(PDF_LOCAL)
    total = len(doc)
    print(f"PDF abierto: {total} paginas\n")

    placed = {}  # page_idx -> [rects]

    for c in COMENTARIOS:
        obs_id   = c["id"]
        fill     = c["fill"]
        text     = c["text"]
        search   = c.get("search")
        fallback = c.get("page_fallback")

        found_rect = None
        if search:
            page_idx, found_rect = buscar_en_paginas(doc, search)
            if page_idx is None:
                print(f"  [{obs_id}] '{search}' no encontrado -> fallback pag {(fallback or total-1)+1}")
                page_idx = fallback if fallback is not None else (total - 1)
        else:
            page_idx = fallback if fallback is not None else 0

        # Clamp dentro del total de paginas
        page_idx = min(page_idx, total - 1)

        page = doc[page_idx]
        rect = calcular_rect(page, found_rect, text)

        if page_idx not in placed:
            placed[page_idx] = []
        rect = evitar_colision(rect, placed[page_idx])
        placed[page_idx].append(rect)

        annot = page.add_freetext_annot(
            rect,
            text,
            fontsize=FONTSIZE,
            fontname="helv",
            text_color=(0, 0, 0),
            fill_color=fill,
        )
        annot.set_border(width=1.5)
        annot.update()

        print(f"  [{obs_id}] pag {page_idx + 1} -> ({rect.x0:.0f},{rect.y0:.0f})-({rect.x1:.0f},{rect.y1:.0f})")

    doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print(f"\nPDF guardado: {PDF_OUT}")


if __name__ == "__main__":
    main()
