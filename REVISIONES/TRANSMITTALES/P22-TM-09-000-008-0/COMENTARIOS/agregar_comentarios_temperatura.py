"""
agregar_comentarios_temperatura.py
Agrega 4 anotaciones FreeText del TM N8 al PDF Datasheet Temperature Transmitter Rev A.
Tecnologia: PyMuPDF (fitz). Fill color distingue severidad.
Response Code: 3 - To be Revised
NOTE-1 NOTE  : portada indica "Pressure Transmitter" (tipo incorrecto)
OBS-2  MAJOR : TIT-09-003 ausente en Instrument List Rev B
NOTE-3 NOTE  : clase de exactitud del sensor RTD no especificada
OBS-3  MAJOR : discrepancia TAGs temperatura entre documentos (TIT-09-001/002/003)
"""
import fitz  # PyMuPDF
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_IN  = os.path.join(SCRIPT_DIR, "P22-LI-09-008-013_A_Datasheet - Temperature Transmitter.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-013_A_Datasheet - Temperature Transmitter_CC_ADASA.pdf")

# Fill colors por severidad (FreeText no admite border_color separado)
CRITICAL = (1.0, 0.80, 0.80)   # rojo claro
MAYOR    = (1.0, 0.90, 0.75)   # naranja claro
MENOR    = (1.0, 1.00, 0.70)   # amarillo claro
NOTE     = (0.85, 0.93, 1.00)  # azul claro

ANNOT_WIDTH  = 210
LINE_HEIGHT  = 11   # pts estimados por linea a fontsize 8
FONTSIZE     = 8
MARGIN       = 10   # margen interior de pagina


COMENTARIOS = [
    {
        "id": "OBS-1",
        "fill": NOTE,          # azul
        "search": "Pressure Transmitter",
        "page_fallback": 0,
        "page_min": 0,
        "text": (
            "Encabezado de portada indica\n"
            "'Pressure Transmitter' — el documento\n"
            "es un Temperature Transmitter DS\n"
            "(TIT-09-003). Corregir en proxima revision."
        ),
    },
    {
        "id": "OBS-2",
        "fill": MAYOR,         # naranja
        "search": "TIT-09-003",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "TIT-09-003 no figura en IL Rev B.\n"
            "IL Rev B item 28: TIT-09-001 como unico\n"
            "transmisor de temperatura CIP Tank.\n"
            "TIT-09-003 sin punto IO asignado.\n"
            "(a) Agregar TIT-09-003 a proxima IL con AI.\n"
            "(b) Confirmar si TIT-09-001 y TIT-09-003\n"
            "son distintos o uno reemplaza al otro."
        ),
    },
    {
        "id": "NOTE-3",
        "fill": NOTE,          # azul
        "search": "Class A",
        "page_fallback": 2,
        "page_min": 2,
        "text": (
            "Clase de exactitud no especificada.\n"
            "Rosemount 214C: Class B (estandar)\n"
            "o Class A disponibles. Especificar\n"
            "clase requerida para TIT-09-003\n"
            "en proxima revision."
        ),
    },
    {
        "id": "OBS-3",
        "fill": MAYOR,
        "search": "TIT-09-001",
        "page_min": 1,
        "page_fallback": 1,
        "text": (
            "OBS-3: Discrepancia TAGs temperatura.\n"
            "TIT-09-001 (IL Rev B item 28),\n"
            "TIT-09-002 (P&ID Rev B area HP Pump),\n"
            "TIT-09-003 (este datasheet):\n"
            "3 TAGs distintos para mismo equipo.\n"
            "BW Water: consolidar en IL Rev C\n"
            "y P&ID Rev B con TAG definitivo."
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
        fallback = c.get("page_fallback")
        min_page = c.get("page_min", 0)

        found_rect = None
        if search:
            page_idx, found_rect = buscar_en_paginas(doc, search, min_page=min_page)
            if page_idx is None:
                print(f"  [{obs_id}] '{search}' no encontrado -> fallback pag {(fallback or 0)+1}")
                page_idx = fallback if fallback is not None else 0
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

    doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print(f"\nPDF guardado: {PDF_OUT}")


if __name__ == "__main__":
    main()
