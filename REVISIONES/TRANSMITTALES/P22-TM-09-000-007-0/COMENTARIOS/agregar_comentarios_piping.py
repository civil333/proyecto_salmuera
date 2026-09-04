"""
agregar_comentarios_piping.py
Agrega anotacion FreeText del TM N7 al PDF Piping Layout Rev A.
OBS-4 (MAJOR): Gabinete de fuerza/control separado del modulo.
Tecnologia: PyMuPDF (fitz). Fill color distingue severidad.
"""
import fitz  # PyMuPDF
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_IN  = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_Piping Layout_Rev.A (CC ADASA).pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_Piping Layout_Rev.A (CC ADASA).pdf")

# Fill colors por severidad (FreeText no admite border_color separado)
CRITICAL = (1.0, 0.80, 0.80)   # rojo claro
MAYOR    = (1.0, 0.90, 0.75)   # naranja claro
MENOR    = (1.0, 1.00, 0.70)   # amarillo claro

ANNOT_WIDTH  = 210
LINE_HEIGHT  = 11   # pts estimados por linea a fontsize 8
FONTSIZE     = 8
MARGIN       = 10   # margen interior de pagina


COMENTARIOS = [
    {
        "id": "OBS-4",
        "fill": MAYOR,
        "search": "PANEL",
        "search_alt": "ELECTRICAL",
        "page_fallback": 0,
        "text": (
            "Gabinete fuerza/control separado\n"
            "del modulo segun este plano.\n"
            "Aclarar: (a) configuracion de montaje\n"
            "(integrado vs. separado en terreno),\n"
            "(b) tendido de cables fuerza y\n"
            "comunicacion modulo-gabinete,\n"
            "(c) procedimiento FAT con gabinete\n"
            "fisicamente separado.\n"
            "Rev B: mostrar montaje e integracion."
        ),
    },
]


def calc_height(text):
    nlines = text.count("\n") + 1
    return max(70, nlines * LINE_HEIGHT + 18)


def buscar_en_paginas(doc, search_text, min_page=0):
    """Retorna (page_idx, primer_rect) o (None, None).
    min_page: indice 0-based; paginas anteriores se omiten."""
    for idx in range(min_page, len(doc)):
        hits = doc[idx].search_for(search_text)
        if hits:
            return idx, hits[0]
    return None, None


def calcular_rect(page, found_rect, text):
    """Posiciona la caja: a la derecha del texto encontrado, o en margen superior-derecho."""
    pw = page.rect.width
    ph = page.rect.height
    w = ANNOT_WIDTH
    h = calc_height(text)

    if found_rect is not None:
        x0 = found_rect.x1 + 4
        y0 = found_rect.y0
        # Si no cabe a la derecha, poner debajo
        if x0 + w > pw - MARGIN:
            x0 = found_rect.x0
            y0 = found_rect.y1 + 6
        # Clamp
        x0 = min(max(x0, MARGIN), pw - MARGIN - w)
        y0 = min(max(y0, MARGIN), ph - h - MARGIN)
    else:
        # Esquina superior-derecha de la pagina
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
    if not os.path.exists(PDF_IN):
        print(f"ERROR: PDF no encontrado:\n  {PDF_IN}")
        return

    doc = fitz.open(PDF_IN)
    total = len(doc)
    print(f"PDF abierto: {total} paginas\n")

    placed = {}  # page_idx -> [rects]

    for c in COMENTARIOS:
        obs_id   = c["id"]
        fill     = c["fill"]
        text     = c["text"]
        search   = c.get("search")
        search_alt = c.get("search_alt")
        fallback = c.get("page_fallback")

        found_rect = None
        page_idx = None

        if search:
            page_idx, found_rect = buscar_en_paginas(doc, search)
            # Intentar termino alternativo si el primero no aparece
            if page_idx is None and search_alt:
                page_idx, found_rect = buscar_en_paginas(doc, search_alt)
                if page_idx is None:
                    print(f"  [{obs_id}] '{search}'/'{search_alt}' no encontrados -> fallback pag {(fallback or total-1)+1}")
                    page_idx = fallback if fallback is not None else (total - 1)
            elif page_idx is None:
                print(f"  [{obs_id}] '{search}' no encontrado -> fallback pag {(fallback or total-1)+1}")
                page_idx = fallback if fallback is not None else (total - 1)
        else:
            page_idx = fallback if fallback is not None else 0

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

    # Si PDF_IN == PDF_OUT, usar guardado incremental
    if os.path.abspath(PDF_IN) == os.path.abspath(PDF_OUT):
        doc.saveIncr()
    else:
        doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print(f"\nPDF guardado: {PDF_OUT}")


if __name__ == "__main__":
    main()
