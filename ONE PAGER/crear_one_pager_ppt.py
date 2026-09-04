"""
One Pager Portfolio - Proyectos ADASA
4 diapositivas: UHPRO Taltal · PDT Fase 2 Tocopilla · PDA Fase 2 Antofagasta · Portfolio Histórico
Autor: Luis Rivera González / ADASA
Fecha: Febrero 2026
"""

import os
from pptx import Presentation
from pptx.util import Pt, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── Rutas ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR        = os.path.dirname(os.path.abspath(__file__))
IMG_DIR           = os.path.join(SCRIPT_DIR, "INFORMACION ADICIONAL")
OUTPUT_PORTFOLIO  = os.path.join(SCRIPT_DIR, "ONE_PAGER_PORTFOLIO_ADASA.pptx")
OUTPUT_TALTAL     = os.path.join(SCRIPT_DIR, "ONE_PAGER_UHPRO_TALTAL.pptx")

# ── Paleta ────────────────────────────────────────────────────────────────────
AZUL_OSCURO = RGBColor(0x00, 0x2B, 0x55)
AZUL_MEDIO  = RGBColor(0x00, 0x5B, 0x9E)
CIAN_AGUA   = RGBColor(0x00, 0xB4, 0xD8)
VERDE_BRINE = RGBColor(0x00, 0xA8, 0x50)
NARANJA     = RGBColor(0xE8, 0x6B, 0x00)
GRIS_CARD   = RGBColor(0xF4, 0xF7, 0xFB)
GRIS_BORDE  = RGBColor(0xC8, 0xD4, 0xE0)
GRIS_TEXTO  = RGBColor(0x33, 0x33, 0x44)
BLANCO      = RGBColor(0xFF, 0xFF, 0xFF)
FONDO_SLIDE = RGBColor(0xEC, 0xF0, 0xF5)
GRIS_IMG    = RGBColor(0xC0, 0xCE, 0xDB)
AMARILLO    = RGBColor(0xF5, 0xC5, 0x18)

# ── Dimensiones slide 16:9 ────────────────────────────────────────────────────
SW = Cm(33.87)
SH = Cm(19.05)

# ── Layout columnas ───────────────────────────────────────────────────────────
HDR_H  = Cm(3.5)
IMG_L  = Cm(0.0)
IMG_W  = Cm(20.2)
IMG_T  = HDR_H
IMG_H  = SH - HDR_H - Cm(0.35)
CAP_H  = Cm(0.35)
COL_L  = IMG_L + IMG_W + Cm(0.25)
COL_W  = SW - COL_L - Cm(0.2)
COL_T  = HDR_H + Cm(0.25)


# ── Configuraciones de proyectos ───────────────────────────────────────────────

CONF_TALTAL = {
    "img_path": os.path.join(SCRIPT_DIR, "GENERAL TALTAL MODULO RO.jpg"),
    "titulo":   "MÓDULO UHPRO — RECUPERACIÓN DE SALMUERA · TALTAL",
    "subtitulo": "Planta Desaladora Taltal  ·  Región de Antofagasta, Chile  ·"
                 "  Contrato C-4300  ·  BW Water Americas Inc. para ADASA",
    "tagline":  "Brine Positive — Transformando residuo hídrico en recurso estratégico",
    "ref_code": "BAE 12803\nFeb 2026",
    "caption":  "▲  Modelo BIM (nube de puntos) — Planta Desaladora Taltal. "
                "El módulo UHPRO se indica en verde.",
    "desc": (
        "Sistema modular de Ósmosis Inversa de Ultra Alta Presión (UHPRO) "
        "para tratamiento de salmuera proveniente del módulo RO existente. "
        "Solución contenerizada «Brine Positive» que convierte el efluente "
        "en agua de alta calidad, incrementando la recuperación total de la "
        "planta sin aumentar la extracción de agua cruda."
    ),
    "pills": [
        ("MODULAR · PLUG & PLAY",       AZUL_MEDIO),
        ("SUPER DUPLEX · Alta Presión",  AZUL_OSCURO),
        ("TURBOCHARGERS · Recuperación", VERDE_BRINE),
    ],
    "metrics": [
        ("480–504",  "m³/día",       "Producción Permeado",       CIAN_AGUA),
        ("42.85%",   "",             "Recuperación del Sistema",   VERDE_BRINE),
        ("< 500",    "mg/L TDS",     "Calidad Agua Producto",      AZUL_MEDIO),
        ("4.71",     "kWh/m³  ±5%", "Consumo Energético (SEC)",   NARANJA),
    ],
    "accent": CIAN_AGUA,
}

CONF_PDT = {
    "img_path": os.path.join(SCRIPT_DIR, "GENERAL TOCOPILLA CUARTO MODULO.jpg"),
    "titulo":   "PDT FASE 2 — AMPLIACIÓN PLANTA DESALADORA · TOCOPILLA",
    "subtitulo": "Caleta Vieja, Tocopilla  ·  Región de Antofagasta, Chile  ·"
                 "  Contrato PDT Fase 2  ·  Vandoorn Ingeniería para ADASA",
    "tagline":  "4° Tren OI — Incrementando capacidad de 75 L/s a 100 L/s",
    "ref_code": "PDT F2\nFeb 2026",
    "caption":  "▲  Vista general — Planta Desaladora de Tocopilla (PDT). "
                "4° tren de Ósmosis Inversa en construcción.",
    "desc": (
        "Etapa final de crecimiento de la Planta Desaladora de Tocopilla, "
        "incorporando un cuarto tren de Ósmosis Inversa de Agua de Mar (+25 L/s). "
        "Incluye ingeniería de detalle, suministro de equipos, cañerías en "
        "Super Duplex SAF2507 y SS316L, y 21 nuevas válvulas en sectores "
        "de captación, ósmosis e impulsión. Planta original ampliable a 100 L/s."
    ),
    "pills": [
        ("SWRO · Agua de Mar",       AZUL_MEDIO),
        ("SAF2507 · Super Duplex",   AZUL_OSCURO),
        ("4° Tren OI · +25 L/s",    VERDE_BRINE),
    ],
    "metrics": [
        ("100",     "L/s",       "Capacidad Total Planta",    CIAN_AGUA),
        ("+25",     "L/s",       "Incremento Fase 2",         VERDE_BRINE),
        ("USD 2.6", "MM CAPEX",  "Inversión Fase 2",          AZUL_MEDIO),
        ("Ene",     "2027",      "Inicio Operación",          NARANJA),
    ],
    "accent": AZUL_MEDIO,
}

CONF_PDA = {
    "img_path": os.path.join(SCRIPT_DIR, "GENERAL 4 MODULO PDA.jpg"),
    "titulo":   "PDA FASE 2 — AMPLIACIÓN PLANTA DESALADORA · ANTOFAGASTA",
    "subtitulo": "Antofagasta  ·  Región de Antofagasta, Chile  ·"
                 "  Contrato PDA Fase 2  ·  ADASA",
    "tagline":  "4° Tren OI — Ampliando la nueva planta para cubrir demanda creciente",
    "ref_code": "PDA F2\nFeb 2026",
    "caption":  "▲  Vista general — Planta Desaladora de Antofagasta (PDA). "
                "Ampliación proyectada con 4° tren de Ósmosis Inversa.",
    "desc": (
        "Ampliación proyectada de la Planta Desaladora de Antofagasta, "
        "incorporando un cuarto tren de Ósmosis Inversa de Agua de Mar (+127 L/s). "
        "Complementa la PDA construida en 2025 (380 L/s, ampliable a 634 L/s). "
        "Incluye 2da impulsión de agua desalada (DIO). CAPEX estimado incluye "
        "infraestructura de distribución."
    ),
    "pills": [
        ("SWRO · Agua de Mar",        AZUL_MEDIO),
        ("4° Tren OI · Antofagasta",  AZUL_OSCURO),
        ("2da Impulsión · DIO",       VERDE_BRINE),
    ],
    "metrics": [
        ("+127",    "L/s",        "Incremento Fase 2",         CIAN_AGUA),
        ("380",     "L/s base",   "Capacidad Fase 1 (2025)",   VERDE_BRINE),
        ("USD 8.3+","MM CAPEX*",  "Inversión estimada",        AZUL_MEDIO),
        ("Ene",     "2028",       "Inicio Operación",          NARANJA),
    ],
    "accent": VERDE_BRINE,
}

# ── Datos Portfolio Histórico ──────────────────────────────────────────────────
PORTFOLIO_HISTORY = [
    {
        "year": "2009",
        "nombre": "PDN\nOperación",
        "lugar": "Antofagasta",
        "cap": "450 L/s",
        "capex": "—",
        "desc": "ADASA asume operación de planta construida por terceros (2003). 450 L/s instalados.",
        "color": AZUL_OSCURO,
        "img": os.path.join(IMG_DIR, "pasado_ALL_s0_0_Imagen_139.png"),
    },
    {
        "year": "2011",
        "nombre": "PDN\nEtapa IV",
        "lugar": "Antofagasta",
        "cap": "150 L/s",
        "capex": "USD 12 MM",
        "desc": "Última etapa de crecimiento para alcanzar capacidad de diseño de 600 L/s.",
        "color": AZUL_MEDIO,
        "img": os.path.join(IMG_DIR, "pasado_ALL_s1_1_Imagen_6.jpg"),
    },
    {
        "year": "2013–15",
        "nombre": "PDN\nModular",
        "lugar": "Antofagasta",
        "cap": "106 L/s",
        "capex": "USD 8.5 MM",
        "desc": "Módulos prefabricados para alcanzar capacidad total de 706 L/s.",
        "color": AZUL_MEDIO,
        "img": os.path.join(IMG_DIR, "pasado_ALL_s1_2_Imagen_3.png"),
    },
    {
        "year": "2016–18",
        "nombre": "PDN\nAmpliaciones",
        "lugar": "Antofagasta",
        "cap": "300 L/s",
        "capex": "USD 32 MM",
        "desc": "Ampliaciones mayores en PDN para alcanzar 1.006 L/s totales.",
        "color": CIAN_AGUA,
        "img": os.path.join(IMG_DIR, "pasado_ALL_s1_3_Imagen_21.jpg"),
    },
    {
        "year": "2020",
        "nombre": "PDT\nTocopilla",
        "lugar": "Tocopilla",
        "cap": "75 L/s",
        "capex": "USD 45 MM",
        "desc": "Planta desaladora nueva. Ampliable a 100 L/s.",
        "color": VERDE_BRINE,
        "img": os.path.join(IMG_DIR, "dev_ALL_s0_2_Imagen_15.png"),
    },
    {
        "year": "2020",
        "nombre": "Taltal\nAmpliación",
        "lugar": "Taltal",
        "cap": "11 L/s",
        "capex": "USD 1.5 MM",
        "desc": "Módulo de desalación prefabricado. Capacidad total 21 L/s en Taltal.",
        "color": NARANJA,
        "img": os.path.join(SCRIPT_DIR, "GENERAL TALTAL.jpg"),
    },
    {
        "year": "2022",
        "nombre": "PDN\nBastidor 50",
        "lugar": "Antofagasta",
        "cap": "50 L/s",
        "capex": "USD 3.7 MM",
        "desc": "Nuevo módulo de OI moderno para alcanzar 1.056 L/s totales en PDN.",
        "color": AZUL_OSCURO,
        "img": os.path.join(IMG_DIR, "pasado_ALL_s1_3_Imagen_21.jpg"),
    },
    {
        "year": "2025",
        "nombre": "PDA\nAntofagasta",
        "lugar": "Antofagasta",
        "cap": "380 L/s",
        "capex": "USD 128 MM",
        "desc": "Planta desaladora nueva que complementa PDN. Ampliable a 634 L/s.",
        "color": VERDE_BRINE,
        "img": os.path.join(IMG_DIR, "img_1_Imagen 16.png"),
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def fill_solid(shape, rgb):
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb


def add_rect(slide, l, t, w, h, rgb, border_rgb=None, border_pt=0.5):
    shp = slide.shapes.add_shape(1, l, t, w, h)
    fill_solid(shp, rgb)
    if border_rgb:
        shp.line.color.rgb = border_rgb
        shp.line.width = Pt(border_pt)
    else:
        shp.line.fill.background()
    return shp


def add_tb(slide, text, l, t, w, h,
           size=11, bold=False, italic=False,
           color=RGBColor(0, 0, 0), align=PP_ALIGN.LEFT,
           font="Calibri"):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font
    return tb


def add_metric_card(slide, l, t, w, h, value, unit, label, accent):
    BAR = Cm(0.4)
    add_rect(slide, l, t, w, h, GRIS_CARD, GRIS_BORDE, 0.75)
    add_rect(slide, l, t, w, BAR, accent)
    add_tb(slide, value,
           l + Cm(0.15), t + BAR + Cm(0.1),
           w - Cm(0.3), Cm(2.0),
           size=40, bold=True, color=accent, align=PP_ALIGN.CENTER)
    if unit:
        add_tb(slide, unit,
               l + Cm(0.15), t + BAR + Cm(2.1),
               w - Cm(0.3), Cm(0.55),
               size=11, bold=True, color=AZUL_MEDIO, align=PP_ALIGN.CENTER)
    label_t = t + BAR + Cm(2.65) if unit else t + BAR + Cm(2.1)
    add_tb(slide, label,
           l + Cm(0.1), label_t,
           w - Cm(0.2), Cm(0.7),
           size=12, bold=False, color=GRIS_TEXTO, align=PP_ALIGN.CENTER)


def add_pill(slide, l, t, w, h, text, bg):
    add_rect(slide, l, t, w, h, bg)
    add_tb(slide, text,
           l + Cm(0.1), t + Cm(0.08),
           w - Cm(0.2), h - Cm(0.08),
           size=9, bold=True, color=BLANCO, align=PP_ALIGN.CENTER)


def add_img_placeholder(slide, l, t, w, h, accent):
    """Placeholder para cuando no hay imagen disponible."""
    add_rect(slide, l, t, w, h, GRIS_IMG)
    add_rect(slide, l + w/2 - Cm(0.05), t + Cm(1.0),
             Cm(0.1), h - Cm(2.0),
             RGBColor(0xA0, 0xB5, 0xC5))
    add_rect(slide, l + Cm(1.0), t + h/2 - Cm(0.05),
             w - Cm(2.0), Cm(0.1),
             RGBColor(0xA0, 0xB5, 0xC5))
    add_tb(slide, "IMAGEN PENDIENTE",
           l + Cm(1.0), t + h/2 - Cm(0.8),
           w - Cm(2.0), Cm(0.7),
           size=14, bold=True,
           color=RGBColor(0x70, 0x90, 0xAA),
           align=PP_ALIGN.CENTER)
    add_tb(slide, "Incorporar fotografía del sitio",
           l + Cm(1.0), t + h/2 + Cm(0.0),
           w - Cm(2.0), Cm(0.6),
           size=10, bold=False, italic=True,
           color=RGBColor(0x80, 0xA0, 0xB8),
           align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# Build slide parametrizado (proyectos en curso)
# ─────────────────────────────────────────────────────────────────────────────

def build_slide(prs, cfg):
    """Construye una diapositiva de proyecto a partir de un dict de configuración."""
    slide  = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    accent = cfg.get("accent", CIAN_AGUA)

    # ── 1. Fondo ──────────────────────────────────────────────────────────────
    add_rect(slide, 0, 0, SW, SH, FONDO_SLIDE)

    # ── 2. Header ─────────────────────────────────────────────────────────────
    add_rect(slide, 0, 0, SW, HDR_H, AZUL_OSCURO)
    add_rect(slide, 0, HDR_H - Cm(0.15), SW, Cm(0.15), accent)

    add_tb(slide, cfg["titulo"],
           Cm(0.6), Cm(0.2), Cm(26.0), Cm(1.4),
           size=20, bold=True, color=BLANCO, align=PP_ALIGN.LEFT)

    add_tb(slide, cfg["subtitulo"],
           Cm(0.6), Cm(1.65), Cm(26.0), Cm(0.8),
           size=11, bold=False, color=accent, align=PP_ALIGN.LEFT)

    add_tb(slide, cfg["tagline"],
           Cm(0.6), Cm(2.5), Cm(24.0), Cm(0.75),
           size=10, bold=True, italic=True, color=BLANCO, align=PP_ALIGN.LEFT)

    add_tb(slide, cfg["ref_code"],
           Cm(28.5), Cm(0.3), Cm(5.0), Cm(1.8),
           size=11, bold=True, color=BLANCO, align=PP_ALIGN.RIGHT)

    # ── 3. Imagen o placeholder ───────────────────────────────────────────────
    img_path = cfg.get("img_path")
    if img_path and os.path.exists(img_path):
        slide.shapes.add_picture(img_path, IMG_L, IMG_T, IMG_W, IMG_H)
    else:
        add_img_placeholder(slide, IMG_L, IMG_T, IMG_W, IMG_H, accent)

    # Caption imagen
    add_rect(slide, IMG_L, IMG_T + IMG_H, IMG_W, CAP_H, AZUL_OSCURO)
    add_tb(slide, cfg["caption"],
           IMG_L + Cm(0.3), IMG_T + IMG_H + Cm(0.04),
           IMG_W - Cm(0.5), CAP_H - Cm(0.04),
           size=8, bold=False, color=accent, align=PP_ALIGN.LEFT)

    # ── 4. Columna derecha ────────────────────────────────────────────────────
    add_rect(slide, COL_L - Cm(0.1), IMG_T, COL_W + Cm(0.3), SH - IMG_T,
             RGBColor(0xF8, 0xFA, 0xFD))

    y = COL_T

    # 4.1 Etiqueta descripción
    add_rect(slide, COL_L, y, COL_W, Cm(0.5), accent)
    add_tb(slide, "  DESCRIPCIÓN DEL SISTEMA",
           COL_L, y, COL_W, Cm(0.5),
           size=10, bold=True, color=AZUL_OSCURO, align=PP_ALIGN.LEFT)
    y += Cm(0.5)

    # 4.2 Texto descriptivo
    add_tb(slide, cfg["desc"],
           COL_L + Cm(0.15), y + Cm(0.15),
           COL_W - Cm(0.2), Cm(3.0),
           size=10, color=GRIS_TEXTO, align=PP_ALIGN.JUSTIFY)
    y += Cm(3.2)

    # 4.3 Pills
    PILL_H   = Cm(0.75)
    PILL_GAP = Cm(0.15)
    pill_w   = (COL_W - PILL_GAP * 2) / 3
    for i, (txt, bg) in enumerate(cfg["pills"]):
        add_pill(slide,
                 COL_L + i * (pill_w + PILL_GAP), y,
                 pill_w, PILL_H, txt, bg)
    y += PILL_H + Cm(0.3)

    # 4.4 Separador
    add_rect(slide, COL_L, y, COL_W, Cm(0.08), accent)
    y += Cm(0.2)

    # 4.5 Etiqueta garantías / métricas
    add_rect(slide, COL_L, y, COL_W, Cm(0.55), AZUL_MEDIO)
    add_tb(slide, "  GARANTÍAS DE DESEMPEÑO",
           COL_L, y, COL_W, Cm(0.55),
           size=11, bold=True, color=BLANCO, align=PP_ALIGN.LEFT)
    y += Cm(0.55) + Cm(0.2)

    # 4.6 Grid 2×2 métricas — altura dinámica hasta fondo del slide
    available = SH - y - Cm(0.2)
    CARD_GAP  = Cm(0.2)
    CARD_W    = (COL_W - CARD_GAP) / 2
    CARD_H    = (available - CARD_GAP) / 2

    for idx, (val, unit, lbl, acc) in enumerate(cfg["metrics"]):
        col = idx % 2
        row = idx // 2
        cx  = COL_L + col * (CARD_W + CARD_GAP)
        cy  = y + row * (CARD_H + CARD_GAP)
        add_metric_card(slide, cx, cy, CARD_W, CARD_H, val, unit, lbl, acc)

    return slide


# ─────────────────────────────────────────────────────────────────────────────
# Build slide Portfolio Histórico (slide 4)
# ─────────────────────────────────────────────────────────────────────────────

def build_portfolio_slide(prs):
    """Slide 4: Portfolio histórico ADASA — timeline horizontal con 8 proyectos."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # ── Fondo ─────────────────────────────────────────────────────────────────
    add_rect(slide, 0, 0, SW, SH, RGBColor(0xE8, 0xEE, 0xF5))

    # ── Header ────────────────────────────────────────────────────────────────
    HDR = Cm(2.8)
    add_rect(slide, 0, 0, SW, HDR, AZUL_OSCURO)
    add_rect(slide, 0, HDR - Cm(0.12), SW, Cm(0.12), CIAN_AGUA)

    add_tb(slide, "EXPERIENCIA EN DESALACIÓN — AGUAS ANTOFAGASTA",
           Cm(0.6), Cm(0.2), Cm(24.0), Cm(1.2),
           size=20, bold=True, color=BLANCO, align=PP_ALIGN.LEFT)

    add_tb(slide, "Proyectos ejecutados bajo autogestión ADASA  ·  Región de Antofagasta, Chile",
           Cm(0.6), Cm(1.45), Cm(24.0), Cm(0.7),
           size=11, color=CIAN_AGUA, align=PP_ALIGN.LEFT)

    add_tb(slide, "2009 – 2025",
           Cm(29.0), Cm(0.3), Cm(4.5), Cm(1.0),
           size=14, bold=True, color=BLANCO, align=PP_ALIGN.RIGHT)

    # ── Totales destacados (banda debajo del header) ───────────────────────────
    BAND_T = HDR
    BAND_H = Cm(1.4)
    add_rect(slide, 0, BAND_T, SW, BAND_H, RGBColor(0x00, 0x44, 0x80))

    add_tb(slide, "TOTAL INVERTIDO",
           Cm(1.0), BAND_T + Cm(0.08), Cm(5.0), Cm(0.6),
           size=9, color=RGBColor(0x90, 0xBE, 0xE0), align=PP_ALIGN.LEFT)
    add_tb(slide, "USD 230 MM",
           Cm(1.0), BAND_T + Cm(0.6), Cm(5.5), Cm(0.7),
           size=16, bold=True, color=AMARILLO, align=PP_ALIGN.LEFT)

    add_tb(slide, "CAPACIDAD TOTAL",
           Cm(8.0), BAND_T + Cm(0.08), Cm(5.0), Cm(0.6),
           size=9, color=RGBColor(0x90, 0xBE, 0xE0), align=PP_ALIGN.LEFT)
    add_tb(slide, "92.620 m³/día",
           Cm(8.0), BAND_T + Cm(0.6), Cm(6.0), Cm(0.7),
           size=16, bold=True, color=AMARILLO, align=PP_ALIGN.LEFT)

    add_tb(slide, "PROYECTOS EJECUTADOS",
           Cm(17.0), BAND_T + Cm(0.08), Cm(6.0), Cm(0.6),
           size=9, color=RGBColor(0x90, 0xBE, 0xE0), align=PP_ALIGN.LEFT)
    add_tb(slide, "8 proyectos",
           Cm(17.0), BAND_T + Cm(0.6), Cm(5.0), Cm(0.7),
           size=16, bold=True, color=AMARILLO, align=PP_ALIGN.LEFT)

    add_tb(slide, "AUTOGESTIÓN ADASA",
           Cm(25.5), BAND_T + Cm(0.08), Cm(8.0), Cm(0.6),
           size=9, color=RGBColor(0x90, 0xBE, 0xE0), align=PP_ALIGN.LEFT)
    add_tb(slide, "Diseño · Abast. · Construcción",
           Cm(25.5), BAND_T + Cm(0.6), Cm(8.0), Cm(0.7),
           size=11, bold=True, color=BLANCO, align=PP_ALIGN.LEFT)

    # ── Línea de tiempo ────────────────────────────────────────────────────────
    N       = len(PORTFOLIO_HISTORY)
    MARGIN  = Cm(0.6)
    TL_T    = BAND_T + BAND_H + Cm(0.5)   # top de la zona de tarjetas
    TL_H    = SH - TL_T - Cm(0.3)         # altura disponible para tarjetas
    CARD_W  = (SW - 2 * MARGIN - Cm(0.2) * (N - 1)) / N
    CARD_GAP = Cm(0.2)

    # Línea horizontal central del timeline
    LINE_Y = TL_T + Cm(1.05)
    add_rect(slide, MARGIN, LINE_Y, SW - 2 * MARGIN, Cm(0.08), AZUL_MEDIO)

    for i, proj in enumerate(PORTFOLIO_HISTORY):
        cx = MARGIN + i * (CARD_W + CARD_GAP)
        cy = TL_T

        col = proj["color"]

        # Punto del timeline
        DOT = Cm(0.28)
        dot_x = cx + CARD_W / 2 - DOT / 2
        add_rect(slide, dot_x, LINE_Y - DOT / 2, DOT, DOT, col)

        # Año
        add_tb(slide, proj["year"],
               cx, cy, CARD_W, Cm(0.85),
               size=11, bold=True, color=col, align=PP_ALIGN.CENTER)

        card_t = cy + Cm(1.0)
        card_h = TL_H - Cm(1.0)

        # Tarjeta de fondo
        add_rect(slide, cx, card_t, CARD_W, card_h,
                 RGBColor(0xF4, 0xF7, 0xFB), GRIS_BORDE, 0.5)

        # Barra de color superior
        add_rect(slide, cx, card_t, CARD_W, Cm(0.3), col)

        # Imagen pequeña (si existe)
        IMG_CARD_H = Cm(2.4)
        img_p = proj.get("img")
        if img_p and os.path.exists(img_p):
            try:
                slide.shapes.add_picture(
                    img_p,
                    cx, card_t + Cm(0.3),
                    CARD_W, IMG_CARD_H
                )
            except Exception:
                add_rect(slide, cx, card_t + Cm(0.3), CARD_W, IMG_CARD_H, GRIS_IMG)
        else:
            add_rect(slide, cx, card_t + Cm(0.3), CARD_W, IMG_CARD_H, GRIS_IMG)

        y_text = card_t + Cm(0.3) + IMG_CARD_H + Cm(0.1)

        # Nombre proyecto
        add_tb(slide, proj["nombre"],
               cx + Cm(0.1), y_text,
               CARD_W - Cm(0.2), Cm(0.9),
               size=9, bold=True, color=col, align=PP_ALIGN.CENTER)
        y_text += Cm(0.9)

        # Lugar
        add_tb(slide, proj["lugar"],
               cx + Cm(0.1), y_text,
               CARD_W - Cm(0.2), Cm(0.45),
               size=8, color=GRIS_TEXTO, align=PP_ALIGN.CENTER)
        y_text += Cm(0.45)

        # Separador
        add_rect(slide, cx + Cm(0.2), y_text, CARD_W - Cm(0.4), Cm(0.04), col)
        y_text += Cm(0.1)

        # Capacidad
        add_tb(slide, proj["cap"],
               cx + Cm(0.1), y_text,
               CARD_W - Cm(0.2), Cm(0.5),
               size=9, bold=True, color=AZUL_OSCURO, align=PP_ALIGN.CENTER)
        y_text += Cm(0.5)

        # CAPEX
        if proj["capex"] != "—":
            add_tb(slide, proj["capex"],
                   cx + Cm(0.1), y_text,
                   CARD_W - Cm(0.2), Cm(0.45),
                   size=8, color=NARANJA, align=PP_ALIGN.CENTER)
            y_text += Cm(0.45)

        # Descripción
        remaining = card_t + card_h - y_text - Cm(0.1)
        if remaining > Cm(0.3):
            add_tb(slide, proj["desc"],
                   cx + Cm(0.1), y_text + Cm(0.05),
                   CARD_W - Cm(0.2), remaining,
                   size=7, italic=True, color=GRIS_TEXTO, align=PP_ALIGN.JUSTIFY)

    return slide


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def build_prs(configs, include_portfolio=False):
    prs = Presentation()
    prs.slide_width  = SW
    prs.slide_height = SH
    for cfg in configs:
        build_slide(prs, cfg)
    if include_portfolio:
        build_portfolio_slide(prs)
    return prs


def main():
    # ── Portfolio: 3 slides proyecto + 1 slide histórico ─────────────────────
    portfolio = build_prs([CONF_TALTAL, CONF_PDT, CONF_PDA], include_portfolio=True)
    portfolio.save(OUTPUT_PORTFOLIO)
    print(f"Portfolio (4 slides): {OUTPUT_PORTFOLIO}")

    # ── Individual Taltal (retrocompatibilidad) ───────────────────────────────
    taltal = build_prs([CONF_TALTAL])
    taltal.save(OUTPUT_TALTAL)
    print(f"Taltal individual:    {OUTPUT_TALTAL}")


if __name__ == "__main__":
    main()
