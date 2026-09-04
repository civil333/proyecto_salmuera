"""
agregar_comentarios_control_philosophy.py
Agrega 12 anotaciones FreeText del TM N7 al PDF Control Philosophy Rev A.
Tecnologia: PyMuPDF (fitz). Fill color distingue severidad.
"""
import fitz  # PyMuPDF
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_IN  = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_Rev A.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_Rev A_CC_ADASA.pdf")

# Fill colors por severidad (FreeText no admite border_color separado)
CRITICAL = (1.0, 0.80, 0.80)   # rojo claro
MAYOR    = (1.0, 0.90, 0.75)   # naranja claro
MENOR    = (1.0, 1.00, 0.70)   # amarillo claro

ANNOT_WIDTH  = 200
LINE_HEIGHT  = 11   # pts estimados por linea a fontsize 8
FONTSIZE     = 8
MARGIN       = 10   # margen interior de pagina


COMENTARIOS = [
    {
        "id": "OBS-1",
        "fill": CRITICAL,
        "search": "30 minutes",
        "page_fallback": None,
        "text": (
            "UPS: 30 min especificados vs. 8 horas\n"
            "requeridas por ET.\n"
            "Rev B debe confirmar UPS >=8 h\n"
            "con calculo de capacidad."
        ),
    },
    {
        "id": "OBS-2",
        "fill": MAYOR,
        "search": "Flow-paced",
        "page_fallback": 18,
        "text": (
            "Discrepancia de tags: tabla usa\n"
            "VE-07-014/016, descripcion usa\n"
            "VE-09-014/016.\n"
            "Resolver con Valve List y P&ID."
        ),
    },
    {
        "id": "OBS-3",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 16,
        "text": (
            "Interfaz Modbus TCP/IP no descrita.\n"
            "Rev B debe incluir: arquitectura de\n"
            "comunicacion PLC-SCADA, variables\n"
            "a intercambiar y referencia al\n"
            "Memory Map de direcciones Modbus.\n"
            "ET \u2014 Communication and Control\n"
            "System (Modbus TCP/IP)."
        ),
    },
    {
        "id": "OBS-4",
        "fill": MENOR,
        "search": "P22-BT-09-009-001",
        "page_fallback": 0,
        "text": (
            "Codigo 'BT' no definido en P22.\n"
            "Validos: ET, DWG, LI, CD, TM, CT, IT.\n"
            "Asignar codigo valido o formalizar\n"
            "'BT' en registro de documentos."
        ),
    },
    {
        "id": "OBS-5",
        "fill": CRITICAL,
        "search": "BH-09-001",
        "page_fallback": 31,
        "text": (
            "Monitoreo continuo de temp. motores\n"
            "no descrito. ET \u2014 Motors and Electrical Equipment:\n"
            "Pt-100 devanados y rodamientos (AI, no DI).\n"
            "PT-100 puede conectarse a entradas\n"
            "RTD o AI del PLC — ambas cumplen ET.\n"
            "Rev B: entradas AI + setpoints alarma."
        ),
    },
    {
        "id": "OBS-6",
        "fill": MAYOR,
        "search": "free contact",
        "page_fallback": 40,
        "text": (
            "DO estado modulo ausente.\n"
            "CP Rev A describe permisos de\n"
            "producto (cliente->modulo),\n"
            "pero no hay salida DO del modulo\n"
            "al cliente (0=det.; 1=operacion).\n"
            "Rev B: incluir en IO List."
        ),
    },
    {
        "id": "OBS-7",
        "fill": MAYOR,
        "search": "permeate tank",
        "page_fallback": None,
        "text": (
            "Habilitacion general DI ausente.\n"
            "CP incluye 2 permisos de producto\n"
            "(permeato/off-spec), pero no DI\n"
            "distinta para habilitar/detener\n"
            "modulo desde planta SWRO.\n"
            "Rev B: incluir en logica + IO List."
        ),
    },
    {
        "id": "OBS-8",
        "fill": MAYOR,
        "search": "colour",
        "page_fallback": 3,
        "text": (
            "ISA 101 no declarado (MAJOR).\n"
            "Sec 1.5 define colores propios\n"
            "sin referenciar ISA 101.\n"
            "ET: HMI debe cumplir ISA 101.\n"
            "Rev B: declarar conformidad ISA 101."
        ),
    },
    {
        "id": "OBS-9",
        "fill": CRITICAL,
        "search": "HMI",
        "page_min": 5,
        "page_fallback": 6,
        "text": (
            "Medicion de energia no descrita.\n"
            "VFDs: senales digital/4-20mA —\n"
            "sin V/I/P individual por carga.\n"
            "ET — Medicion Electrica: MVE\n"
            "al PLC; CEE (kWh/m3) visible en HMI.\n"
            "ET — Garantias Rendimiento: CEE\n"
            "contractual — sin MVE no se puede\n"
            "verificar en comisionamiento."
        ),
    },
    {
        "id": "OBS-10",
        "fill": MAYOR,
        "search": "4-20",
        "page_fallback": 1,
        "text": (
            "Protocolo incompleto (MAJOR).\n"
            "(a) Sec 2.2.1: solo 4-20mA.\n"
            "P22-CD-09-004-001 Rev B muestra\n"
            "gateway EtherNet/IP (PLX32-EIP-MBTCP)\n"
            "no mencionado aqui.\n"
            "(b) HART obligatorio por ET \u2014\n"
            "Instrumentation Specification (HART)\n"
            "no declarado en este documento."
        ),
    },
    {
        "id": "OBS-11",
        "fill": MAYOR,
        "search": "permeate tank",
        "page_fallback": 43,
        "text": (
            "Interfaz permisivo cliente (MAJOR).\n"
            "Client Interface Permissive: 2 DI separadas (incorrecto).\n"
            "Correcto: 1 DI habilitacion ADASA->modulo\n"
            "(rele DO PLC ADASA) + 1 DO estado\n"
            "modulo->ADASA (rele DO PLC BW Water).\n"
            "ADASA consolida condiciones externas\n"
            "con su propia instrumentacion.\n"
            "Rev B: corregir Sec 3.3.3 y asignar\n"
            "ambas senales en IO List."
        ),
    },
    {
        "id": "OBS-12",
        "fill": MAYOR,
        "search": "PIT-09-001",
        "page_fallback": 37,
        "text": (
            "Permisivo HP incompleto (MAJOR).\n"
            "HP Pump Permissive:\n"
            "verifica PIT-09-001 NOT FAULT\n"
            "pero no valor minimo de proceso.\n"
            "Si ADASA entrega presion baja,\n"
            "PLC arranca BH-09-001 igual\n"
            "(riesgo de cavitacion).\n"
            "Rev B: definir setpoint PSL con\n"
            "presion minima de alimentacion."
        ),
    },
]


def calc_height(text):
    nlines = text.count("\n") + 1
    return max(70, nlines * LINE_HEIGHT + 18)


def buscar_en_paginas(doc, search_text, min_page=0):
    """Retorna (page_idx, primer_rect) o (None, None).
    min_page: índice 0-based; páginas anteriores se omiten."""
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
            # OBS-8: si "colour" no se encuentra, intentar "color"
            if page_idx is None and search == "colour":
                page_idx, found_rect = buscar_en_paginas(doc, "color", min_page=min_page)
            if page_idx is None:
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

    doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print(f"\nPDF guardado: {PDF_OUT}")


if __name__ == "__main__":
    main()
