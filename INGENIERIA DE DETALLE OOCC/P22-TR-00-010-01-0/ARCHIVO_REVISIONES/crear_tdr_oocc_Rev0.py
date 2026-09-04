#!/usr/bin/env python3
"""
Genera el DOCX del TdR de Obras Civiles y Estructuras Metálicas
usando la skill template-adasa.

Código: P22-TR-00-010-01-0
"""
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Skill GLOBAL (path absoluto) - per CLAUDE.md v6.3, no usar .claude/skills/ del proyecto
skill_path = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, skill_path)

from ejemplo_documento import crear_documento_adasa, aplicar_arial_12, add_simple_table, add_bullet
from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT = os.path.join(SCRIPT_DIR, "P22-TR-00-010-01-0(Ingenieria OOCC Modulo Taltal).docx")
IMAGENES = os.path.join(SCRIPT_DIR, "IMAGENES")
ANTECEDENTES_URL = "https://lrg.synology.me:6501/d/s/17sRrBhRSKQWNvHdLwinKlyG5jDvc8h0/x-5SxL-c027D6fS9uQIIRYAwj3o81TSi-lrSg4eM1Iw0"


def p(doc, text, size=11, bold=False, align=None):
    """Add a paragraph with Arial formatting."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.bold = bold
    if align:
        para.alignment = align
    return para


def add_img(doc, filename, caption, width=Inches(5.5)):
    """Add image with caption."""
    img_path = os.path.join(IMAGENES, filename)
    if os.path.exists(img_path):
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run()
        run.add_picture(img_path, width=width)
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cap.add_run(caption)
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.italic = True
    else:
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = para.add_run(f"[{caption} — imagen no disponible: {filename}]")
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.italic = True


def placeholder_img(doc, caption):
    """Add placeholder text for unavailable image."""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = para.add_run(f"[{caption}]")
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.italic = True


def bullet(doc, text, size=11):
    """Add native Word bullet '•' (delegates to skill helper add_bullet)."""
    return add_bullet(doc, text, size=size)


def add_hyperlink(paragraph, url, text, size=11):
    """Append an external hyperlink run to an existing paragraph."""
    r_id = paragraph.part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Arial")
    rFonts.set(qn("w:hAnsi"), "Arial")
    rPr.append(rFonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(size * 2))
    rPr.append(sz)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rPr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink


# =============================================================================
# 1. CREATE BASE DOCUMENT
# =============================================================================
print("Generando documento base con template ADASA...")
crear_documento_adasa(
    titulo="TÉRMINOS DE REFERENCIA\nINGENIERÍA DE DETALLE\nOBRAS CIVILES Y ESTRUCTURAS METÁLICAS\nMÓDULO RO SEGUNDA ETAPA PARA SALMUERA — PD TALTAL",
    codigo="P22-TR-00-010-01-0",
    preparado_por="Luis Rivera",
    revisado_por="Luis Rivera",
    aprobado_por="Víctor Gutiérrez",
    nombre_planta="TALTAL",
    cliente="ADASA",
    output_filename=OUTPUT,
    incluir_toc=True,
)

# =============================================================================
# 2. OPEN AND ADD CONTENT
# =============================================================================
# NOTA: la skill template-adasa ya gestiona portada, cajetin, limpieza del template
# y TOC (ver CLAUDE.md §3.3). No duplicar cleanup aqui: al hacerlo se rompe la
# portada y el TOC.
print("Agregando contenido...")
doc = Document(OUTPUT)

# Post-proceso fixes sobre lo que entrega la skill template-adasa:
# (a) cantSplit en cada fila del cajetin: evita que Word parta la tabla entre
#     paginas (actualmente las 2 filas vacias superiores y las 2 con contenido
#     quedan en paginas distintas).
# (b) Colapsar el padding vertical de parrafos vacios entre "Antofagasta, ..."
#     y el cajetin, para que el cajetin completo quepa en la portada.
# (c) Traducir titulo del TOC ("TABLE OF CONTENTS" -> "TABLA DE CONTENIDO") y
#     eliminar el pagebreak explicito que la skill agrega antes del TOC.
from docx.oxml.ns import qn as _qn
from docx.oxml import OxmlElement as _OxmlElement

# (a)
if len(doc.tables) > 0:
    cajetin = doc.tables[0]
    for row in cajetin.rows:
        trPr = row._tr.get_or_add_trPr()
        trPr.append(_OxmlElement("w:cantSplit"))

# (b)
_body = doc.element.body
_encontro_fecha = False
for _child in list(_body):
    _tag = _child.tag.split("}")[-1]
    if _tag == "p":
        _text = "".join(_child.itertext()).strip()
        if "Antofagasta," in _text:
            _encontro_fecha = True
            continue
        if _encontro_fecha and not _text:
            _pPr = _child.find(_qn("w:pPr"))
            if _pPr is None:
                _pPr = _OxmlElement("w:pPr")
                _child.insert(0, _pPr)
            for _sp in _pPr.findall(_qn("w:spacing")):
                _pPr.remove(_sp)
            _spacing = _OxmlElement("w:spacing")
            _spacing.set(_qn("w:before"), "0")
            _spacing.set(_qn("w:after"), "0")
            _spacing.set(_qn("w:line"), "240")
            _spacing.set(_qn("w:lineRule"), "auto")
            _pPr.append(_spacing)
    elif _tag == "tbl":
        break

# (c)
for para in doc.paragraphs:
    if para.text.strip() == "TABLE OF CONTENTS":
        for run in para.runs:
            if "TABLE OF CONTENTS" in run.text:
                run.text = run.text.replace("TABLE OF CONTENTS", "TABLA DE CONTENIDO")
        titulo_elem = para._element
        prev = titulo_elem.getprevious()
        if prev is not None and prev.tag == _qn("w:p"):
            has_break = any(br.get(_qn("w:type")) == "page"
                            for br in prev.iter(_qn("w:br")))
            tiene_texto = bool("".join(prev.itertext()).strip())
            if has_break and not tiene_texto:
                prev.getparent().remove(prev)
        break


# --- SECTION 1: INTRODUCCIÓN ---
doc.add_heading("INTRODUCCIÓN", level=1)

p(doc, "Este documento establece los términos de referencia para la contratación del servicio de ingeniería de detalle de obras civiles y estructuras metálicas del Módulo RO Segunda Etapa para Salmuera, Planta Desaladora Taltal (ADASA). El alcance comprende fundaciones de equipos exteriores, fundación compartida del contenedor RO y sistema CIP, fosa de drenajes TK-06-002, red de cámaras intermedias, pavimentos y la cubierta metálica del sistema CIP exterior.")
p(doc, "El módulo, de suministro ADASA, aumenta la capacidad de producción al tratar la salmuera residual del módulo 3 existente. La ingeniería de detalle mecánica y de interconexiones es desarrollada por ADASA; este servicio cubre exclusivamente las disciplinas civil y estructural.")
p(doc, "El emplazamiento es un recinto costero en Taltal, Región de Antofagasta, con ambiente marino corrosivo (exposición directa a brisa salina).")
add_img(doc, "IMG-01_Vista_Aerea_Recinto.jpg",
        "Figura 1-1: Vista aérea del recinto PD Taltal.")

# --- SECTION 2: ALCANCE DE LA CONSULTORÍA ---
doc.add_heading("ALCANCE DE LA CONSULTORÍA", level=1)

doc.add_heading("Alcance Ingeniería de Detalle de Obras Civiles", level=2)

doc.add_heading("Fundaciones para equipos exteriores", level=3)
p(doc, "El consultor deberá diseñar las fundaciones de hormigón armado para los siguientes equipos de suministro ADASA, de acuerdo con las cargas, dimensiones y requerimientos de anclaje indicados en las hojas de datos y planos del proveedor:")

p(doc, "Estanque de salmuera TK-06-001:", bold=True)
p(doc, "Estanque vertical de PRFV (Exfibro), Ø2.600 mm × H2.570 mm, volumen útil 10 m³. Peso vacío aproximado 586 kg; en operación con fluido alcanza 12.572 kg (gravedad específica 1,05). La fundación debe incorporar las llaves de corte y topes sísmicos definidos en el plano EX-26005-F01 Rev C, que restringen el desplazamiento lateral del estanque durante un evento sísmico. Los 8 pernos de anclaje de 1\" se disponen según la planta de anclajes del mismo plano (B.C.D.= Ø2.755 mm). Las cargas basales sísmicas están documentadas en la Memoria de Cálculo Exfibro (página 18): fuerzas horizontales Ex/Ey de ±4.617 kg y momentos Mx/My de ±431.846 kg·cm.")

p(doc, "Bomba de alimentación BH-06-001:", bold=True)
p(doc, "Bomba centrífuga horizontal KSB modelo KNCPP 11/050+160M, motor de 11 kW. Peso estimado en operación de 400 kg. Esta fundación requiere un diseño dinámico considerando las vibraciones generadas por el equipo rotatorio, conforme a los criterios de ACI 351. Las dimensiones del baseplate y puntos de anclaje se obtienen del plano general de arreglo del proveedor (KSB-AAF-KNCPP11-050+160M Rev A).")

doc.add_heading("Fundación compartida contenedor y sistema CIP", level=3)
p(doc, "Los equipos del sistema CIP (limpieza química) quedan inmediatamente adyacentes al contenedor del módulo RO. Por su proximidad, se diseñará una fundación única que soporte tanto el contenedor como los equipos CIP exteriores. Los equipos que comparten esta fundación son:")

add_simple_table(doc, [
    ("TAG", "Equipo", "Peso op. (kg)", "Suministro"),
    ("—", "Contenedor Módulo RO 40ft HC (12.192×2.438×2.896 mm)", "~17.334", "ADASA"),
    ("TK-09-001", "Estanque CIP HDPE 6.800 L (per P&ID P22-DWG-06-009-104)", "~8.140", "ADASA"),
    ("BH-09-002", "Bomba CIP (per P&ID)", "~385", "ADASA"),
    ("REL-09-001", "Calentador CIP 16 kW (per P&ID)", "~220", "ADASA"),
    ("FIL-09-002", "Filtro Cartucho CIP (12 elem. 2,5×40 in)", "~880", "ADASA"),
])

p(doc, "La fundación debe diseñarse con armaduras y recubrimientos de hormigón que permitan la instalación posterior de pernos químicos post-instalados para los soportes de tuberías y bandejas portacables del sistema CIP, cuya soportación queda fuera del alcance del consultor. El consultor deberá coordinar con ADASA los puntos de anclaje previstos antes de emitir la Revisión 0 de los planos.")

doc.add_heading("Fosa de drenajes (TK-06-002)", level=3)
p(doc, "La fosa de drenajes TK-06-002 se construirá en hormigón armado, con capacidad útil de 2.000 litros y dimensiones interiores referenciales de aproximadamente 1,5 × 1,5 × 1,0 m (a precisar por el consultor en función del dimensionamiento hidráulico). La cota de fondo se referirá al NPT definido en los planos de montaje Van Doorn. El diseño debe considerar impermeabilización interior y pendientes adecuadas para la evacuación de líquidos. La evacuación de la fosa es por gravedad a través de la línea SA-CPVC-DN200-PN10-001, definida en los planos de piping P22-DWG-06-006-103 (planta) y P22-DWG-06-006-104 (cortes y detalles); el alcance no incluye bomba sumergible en la fosa.")
p(doc, "El caudal de diseño para el dimensionamiento hidráulico se derivará de los drenajes de equipos listados en el P&ID P22-DWG-06-009-104 y en los planos de piping Van Doorn, y se documentará en la memoria P22-MC-00-002-003.")

doc.add_heading("Obras de canalización y drenajes", level=3)
p(doc, "El sistema de drenajes del proyecto está compuesto por la fosa principal TK-06-002 descrita en la subsección anterior y por una red de cámaras intermedias de hormigón prefabricado que recolectan drenajes por gravedad desde los distintos puntos de captación y los conducen hasta la fosa. La cantidad, ubicación y cotas de tapa y fondo de las cámaras son las indicadas en el plano de Van Doorn P22-DWG-06-005-104 (PL. DRENAJES) provisto como antecedente, que identifica tres cámaras intermedias en el recorrido principal, designadas CD-06-001, CD-06-002 y CD-06-003 según el orden indicado en el plano. Si una revisión posterior de Van Doorn modifica la cantidad de cámaras, el ajuste del entregable (planos y memoria) se tramitará como orden de cambio con precio unitario por cámara adicional.")
p(doc, "El consultor incorporará la nomenclatura CD-06-00N (CD = Cámara Drenaje, área 06) en los planos de construcción. El diseño civil adopta un detalle típico único de cámara prefabricada de hormigón (dimensiones, armaduras de tapa y cuerpo, y sellos de ingreso y salida de tuberías), escalado según la profundidad variable de cada cámara. El perfil longitudinal del sistema debe garantizar pendientes mínimas hacia la fosa, usando como base las cotas del plano de Van Doorn.")

doc.add_heading("Pavimentos y terminaciones", level=3)
p(doc, "Comprende losas de hormigón y/o radieres en las zonas de emplazamiento de equipos, y terminaciones de base compactada en áreas circundantes según los requerimientos de acceso y operación.")

# --- 2.2 Estructuras Metálicas ---
doc.add_heading("Alcance Ingeniería de Detalle de Estructuras Metálicas", level=2)

doc.add_heading("Cubierta metálica para sistema CIP exterior", level=3)
p(doc, "Diseño de una estructura metálica tipo cobertizo o techo que proteja los equipos del sistema CIP que quedan fuera del contenedor. Esta cubierta constituye la estructura metálica principal del presente alcance. Los criterios de diseño incluyen:")
bullet(doc, "Protección contra lluvia, radiación solar directa y viento")
bullet(doc, "Material estructural ASTM A-36 con sistema de protección superficial conforme a los criterios indicados en la sección de criterios de diseño de este documento")
bullet(doc, "Techado con planchas prepintadas o material equivalente")
bullet(doc, "Diseño para cargas de viento, peso propio y solicitaciones sísmicas según NCh 2369:2025 Zona 3")
bullet(doc, "Accesibilidad para mantenimiento de los equipos CIP protegidos")

p(doc, "La cubierta metálica protege exclusivamente los equipos CIP ubicados fuera del contenedor (zona remarcada en la Figura 2-1); el contenedor del módulo RO no requiere cubierta adicional.")
add_img(doc, "IMG-08_Area_Cubierta_CIP.png",
        "Figura 2-1: Zona del sistema CIP exterior al contenedor (destacada en rojo sobre el Piping Layout ISO de BW Water) sobre la cual el consultor deberá proyectar la cubierta metálica. El contenedor RO y sus equipos interiores quedan fuera del alcance de estructuras metálicas.",
        width=Inches(6))


# --- 2.3 Exclusiones ---
doc.add_heading("Exclusiones del Alcance", level=2)
p(doc, "Las siguientes actividades quedan fuera del presente servicio:")
bullet(doc, "Soportación de bandejas portacables y tuberías del sistema CIP — fuera del alcance del consultor (lo resuelve ADASA con el montaje del módulo)")
bullet(doc, "Ingeniería mecánica de piping (trazados, isométricos, materiales de cañerías)")
bullet(doc, "Ingeniería eléctrica e instrumentación")
bullet(doc, "Ingeniería interior del contenedor del módulo RO — fuera del alcance del consultor")
bullet(doc, "Pipe racks y soportación de tuberías en zona TK-06-001 / BH-06-001")
bullet(doc, "Plataformas de acceso, escaleras y barandas del estanque TK-06-001")

# --- SECTION 3: CRITERIOS DE DISEÑO ---
doc.add_heading("CRITERIOS DE DISEÑO", level=1)

doc.add_heading("Normativa y Códigos Aplicables", level=2)
add_simple_table(doc, [
    ("Código", "Descripción", "Aplicación"),
    ("NCh 2369:2025", "Diseño sísmico de estructuras e instalaciones industriales", "Todas las estructuras y fundaciones (obligatoria)"),
    ("NCh 432", "Cálculo de la acción del viento sobre las construcciones", "Cubierta CIP y elementos expuestos"),
    ("NCh 1537", "Cargas permanentes y sobrecargas de uso", "Todas las estructuras"),
    ("NCh 3171", "Disposiciones generales y combinaciones de cargas", "Complemento a ACI 318"),
    ("NCh 170:2016", "Hormigón — Requisitos generales", "Clasificación por clase de exposición"),
    ("NCh 204", "Barras laminadas en caliente para hormigón armado", "Acero A630-420H"),
    ("ACI 318-19", "Requisitos para concreto estructural", "Hormigón armado y anclajes (Cap. 17)"),
    ("ACI 351.3R", "Fundaciones para equipos dinámicos", "Fundación bomba BH-06-001"),
    ("ACI 355.4", "Calificación de anclajes adhesivos post-instalados", "Pernos químicos zona CIP"),
    ("AISC 360-22", "Especificación acero estructural (LRFD)", "Estructuras metálicas"),
    ("AWS D1.1", "Código de soldadura estructural — Acero", "Soldaduras"),
    ("ASTM A-36", "Acero al carbono estructural", "Material base estructuras metálicas"),
    ("ASTM A1064", "Malla electrosoldada (reemplaza ASTM A185)", "Refuerzo secundario"),
    ("SSPC-SP10 / ISO 8501-1 Sa 2½", "Preparación de superficie metal casi blanco", "Protección superficial acero"),
    ("ISO 12944-2", "Corrosividad atmosférica", "Clasificación C5-M"),
    ("ISO 12944-5", "Sistemas de pintura protectora", "Selección C5-M Alta durabilidad"),
    ("ISO 10816 / 20816", "Vibración mecánica en máquinas", "Verificación dinámica en operación"),
])

doc.add_heading("Condiciones Sísmicas", level=2)
p(doc, "El emplazamiento se ubica en Zona Sísmica 3 según la clasificación de NCh 2369:2025. Todas las fundaciones y estructuras metálicas deberán diseñarse para resistir las solicitaciones sísmicas correspondientes a esta zona, aplicando las fuerzas al centro de gravedad de los equipos y considerando el peso en condición de operación (equipos llenos).")
p(doc, "El informe sísmico del sitio (LNS-ADASA-INF-040 Rev 0) contiene los parámetros específicos del emplazamiento que el consultor deberá utilizar como base para el diseño.")

doc.add_heading("Criterios de Diseño de Obras Civiles", level=2)

doc.add_heading("Nivel de Piso Terminado (NPT)", level=3)
p(doc, "El NPT aplicable a todos los equipos del proyecto (contenedor RO, equipos exteriores del área 06 y equipos CIP) se define en los planos de montaje mecánicos de Van Doorn (P22-DWG-06-005-103 y los cortes de los planos de cañerías P22-DWG-06-006-101 a -104). El consultor incorporará este NPT como dato de entrada en el diseño de fundaciones, pedestales y estructuras metálicas, y lo reflejará en la implantación general P22-DWG-00-002-001. Cualquier desviación requerida por condiciones del sitio se resolverá con ADASA antes de la Revisión A.")

doc.add_heading("Estimación de capacidad de soporte del suelo", level=3)
p(doc, "Para el diseño de fundaciones, el consultor asumirá una capacidad admisible de suelo σ_adm ≤ 1,0 kg/cm² (100 kPa). ADASA considera que no es necesario ejecutar un estudio geotécnico adicional dentro del alcance de este servicio, dado que el emplazamiento está dentro del recinto industrial en operación. ADASA proveerá el informe sísmico del sitio (LNS-ADASA-INF-040 Rev 0) y las detecciones de georadar como antecedentes complementarios.")

doc.add_heading("Método de diseño", level=3)
p(doc, "Para hormigón armado se aplicará el método de resistencia última según ACI 318-19 (LRFD). Para estructuras metálicas se aplicará AISC 360-22 en formato LRFD. Todas las combinaciones de carga se armonizarán conforme a NCh 3171 y NCh 2369:2025 Zona 3.")

doc.add_heading("Materiales", level=3)
add_simple_table(doc, [
    ("Elemento", "Material", "Grado / Especificación"),
    ("Hormigón estructural", "Hormigón armado", "G-25 (NCh 170:2016), a/c ≤ 0,50, cemento ≥ 340 kg/m³, clase exposición M2/C4"),
    ("Acero de refuerzo", "Barras laminadas en caliente", "A630-420H (NCh 204)"),
    ("Malla electrosoldada", "Según cálculo", "ASTM A1064"),
])

doc.add_heading("Recubrimientos de hormigón", level=3)
p(doc, "Los recubrimientos mínimos para elementos de hormigón armado en ambiente marino corrosivo serán de 50 mm para elementos expuestos. En elementos en contacto con el terreno, el recubrimiento mínimo será de 70 mm. El consultor podrá proponer recubrimientos mayores cuando las condiciones de exposición lo ameriten.")

doc.add_heading("Factores de seguridad y combinaciones de carga", level=3)
p(doc, "Las combinaciones de carga se definirán según ACI 318-19 y NCh 3171 e incluirán como mínimo: peso propio (D), sobrecarga de uso (L) según NCh 1537, peso del equipo en operación (lleno), cargas de viento (W) según NCh 432 con velocidad básica de zona costera Taltal, cargas sísmicas (E) según NCh 2369:2025 Zona 3 con factor de importancia y amortiguamiento según tipo estructural, cargas térmicas (T) por delta ambiental, y empujes de suelo donde corresponda. El consultor documentará todas las combinaciones utilizadas en las memorias de cálculo.")

doc.add_heading("Fundaciones para equipos con vibración", level=3)
p(doc, "La fundación de la bomba de alimentación BH-06-001 deberá diseñarse según ACI 351.3R (Foundations for Dynamic Equipment). Criterios mínimos:")
bullet(doc, "Razón masa-fundación / masa-equipo ≥ 3 para bombas centrífugas horizontales")
bullet(doc, "Frecuencia natural de la fundación fuera de ±20% de la frecuencia de operación de la bomba")
bullet(doc, "Amplitudes de vibración dentro de las categorías Very Good o Good del gráfico Blake/Baxter (ACI 351.3R)")
bullet(doc, "Verificación en operación conforme a ISO 10816 / 20816 como criterio de aceptación en puesta en marcha")
add_img(doc, "IMG-07_ACI351_Vibraciones.png", "Figura 3-2: Clasificación de severidad de vibraciones para fundaciones de equipos dinámicos (ACI 351).", width=Inches(3.5))

# --- 3.4 Criterios Estructuras Metálicas ---
doc.add_heading("Criterios de Diseño de Estructuras Metálicas", level=2)

doc.add_heading("Materiales", level=3)
p(doc, "El acero estructural para perfiles, chapas y placas base será ASTM A-36. Los pernos de conexión en ambiente expuesto serán galvanizados en caliente o de acero inoxidable. Las soldaduras se ejecutarán según AWS D1.1.")

doc.add_heading("Sistema de protección superficial", level=3)
p(doc, "Clasificación de corrosividad según ISO 12944-2: C5-M (costa marina) con durabilidad requerida Alta (>15 años) conforme ISO 12944-5. El revestimiento deberá cumplir con el siguiente sistema mínimo:")
add_simple_table(doc, [
    ("Capa", "Producto (referencia)", "Espesor DFT (µm)"),
    ("Preparación de superficie", "SSPC-SP10 / Sa 2½ (ISO 8501-1). Perfil de anclaje 50 µm", "—"),
    ("Imprimación (primer)", "Zinc Clad II — Epóxico rico en zinc (SW o equivalente)", "80"),
    ("Capa intermedia", "Macropoxy 646 — Epóxico de alto espesor (SW o equivalente)", "200"),
    ("Capa de acabado", "Acrolon 218 HS — Poliuretano alifático acrílico (SW o equiv.)", "75"),
    ("Total sistema", "", "≥ 355"),
])
p(doc, "Color de acabado: RAL 5012 (Azul Luminoso). La aplicación de cada capa deberá realizarse según las recomendaciones del fabricante, con inspecciones de calidad en cada etapa.")

doc.add_heading("Tensiones y deformaciones admisibles", level=3)
p(doc, "Las tensiones admisibles de trabajo se determinarán según AISC 360. Las deformaciones máximas admisibles serán L/240 para elementos que soportan equipos y L/180 para elementos secundarios (barandas, plataformas de acceso). El consultor verificará que las frecuencias naturales de las estructuras no coincidan con las frecuencias de operación de los equipos soportados.")

# --- 3.5 Condiciones Ambientales ---
doc.add_heading("Condiciones Ambientales del Sitio", level=2)
add_simple_table(doc, [
    ("Parámetro", "Valor"),
    ("Temperatura mínima", "8 °C"),
    ("Temperatura máxima", "28 °C"),
    ("Humedad relativa promedio", "72% (costa Pacífico, registros Taltal)"),
    ("Presión atmosférica promedio", "101,3 kPa (nivel del mar)"),
    ("Altitud", "~5 m s.n.m."),
    ("Sistema de coordenadas", "UTM WGS84 Huso 19 Sur"),
    ("Zona sísmica NCh 2369:2025", "Zona 3"),
    ("Clase de exposición NCh 170:2016", "M2 / C4 (ambiente marino con niebla salina)"),
    ("Corrosividad atmosférica ISO 12944-2", "C5-M"),
    ("Clasificación ambiental", "Marino corrosivo — exposición directa a brisa salina"),
])

# --- SECTION 4: DESARROLLO DE IMPLANTACIÓN ---
doc.add_heading("DESARROLLO DE IMPLANTACIÓN DEL PROYECTO", level=1)

doc.add_heading("Layout General", level=2)
p(doc, "La base de implantación del proyecto es el Levantamiento DIO Abr-2026 (DESALADORA 050326_mod 3.dwg), provisto como antecedente en la carpeta 01_SITIO/LEVANTAMIENTO_DIO_2026/. Este plano contiene la situación actual del recinto con cotas topográficas, instalaciones existentes y bancos de ductos subterráneos.")
p(doc, "El consultor deberá georreferenciar sobre esta base DIO el plano de montaje del módulo (P22-DWG-06-005-103) y los planos de piping de interconexiones (P22-DWG-06-006-101 a -104), provistos por ADASA en el paquete de antecedentes.")
p(doc, "El Nivel de Piso Terminado (NPT) aplicable a todos los equipos del proyecto (contenedor RO, equipos exteriores del área 06 y equipos CIP) es el indicado en los planos de montaje mecánicos de Van Doorn (P22-DWG-06-005-103 y los cortes de los planos de cañerías P22-DWG-06-006-101 a -104). Este nivel es dato fijo y no puede ser modificado por el consultor: condiciona las cotas de fundación, las alturas de pedestales y las pendientes del sistema de drenajes. El consultor verificará el NPT contra el Levantamiento DIO Abr-2026 y reportará cualquier incompatibilidad antes de la Revisión A.")

doc.add_heading("Equipos Exteriores Área 06", level=2)
p(doc, "Los equipos exteriores de suministro ADASA que requieren fundaciones independientes son:")
add_simple_table(doc, [
    ("TAG", "Equipo", "Material", "Dimensiones", "Peso oper. (kg)", "Observación"),
    ("TK-06-001", "Estanque Salmuera", "PRFV", "Ø2.600×H2.570 mm", "12.572", "Topes sísmicos per Exfibro p.18"),
    ("TK-06-002", "Fosa Drenajes", "Hormigón armado", "V=2.000 L; ~1,5×1,5×1,0 m", "N/A", "Impermeabilización; cota fondo ref. NPT; evacuación por gravedad"),
    ("BH-06-001", "Bomba Alimentación", "Inox PREN≥40", "Per plano KSB", "~400", "Fundación dinámica ACI 351"),
])

add_img(doc, "IMG-02_GA_Estanque_TK-06-001.png",
        "Figura 4-1: Plano general de arreglo del estanque de salmuera TK-06-001 (Exfibro EX-26005-F01 Rev C).",
        width=Inches(6))
add_img(doc, "IMG-03_Topes_Sismicos_Exfibro.png",
        "Figura 4-2: Detalle de planta de anclajes, sillas de anclaje, tope sísmico y orejas de izaje — TK-06-001.",
        width=Inches(5.5))
add_img(doc, "IMG-04_GA_Bomba_BH-06-001.png",
        "Figura 4-3: Plano general de arreglo de la bomba de alimentación BH-06-001 (KSB KNCPP 11/050+160M Rev A).",
        width=Inches(5.5))

doc.add_heading("Módulo RO Contenedor (Área 09)", level=2)
p(doc, "El módulo RO se aloja en un contenedor de 40 pies High Cube con las siguientes características principales:")
bullet(doc, "Dimensiones exteriores: 12.192 mm (L) × 2.438 mm (A) × 2.896 mm (H)")
bullet(doc, "Peso en operación estimado: 17.334 kg")
bullet(doc, "Suministro del módulo: ADASA (cadena de suministro propia)")
p(doc, "Los planos de Layout del módulo — P22-DWG-09-005-003 Rev B (Equipment Layout, planta y elevaciones) y P22-DWG-09-005-004 Rev B (Piping Layout) — son provistos como antecedentes en 04_PLANOS_BW_WATER_VIGENTES/, para la verificación de huellas de equipos, cargas distribuidas sobre la fundación y requerimientos de interfaz estructural. Se incluye además el Tie-In Point Layout Rev C en versión preliminar y el Cable Tray Layout Rev B con detalles de soportes relevantes para la estructura metálica.")

doc.add_heading("Equipos CIP Exteriores al Contenedor", level=2)
p(doc, "Los equipos del sistema CIP (Clean-In-Place) que se ubican fuera del contenedor comparten la fundación con el módulo y quedan protegidos por la cubierta metálica descrita en el alcance de estructuras metálicas. Son suministro ADASA y los TAGs corresponden al P&ID P22-DWG-06-009-104: estanque TK-09-001 (HDPE, 6.800 L), bomba BH-09-002, calentador REL-09-001 (16 kW) y filtro FIL-09-002 (12 elementos 2,5 × 40 in). El peso combinado en operación es de aproximadamente 9.625 kg.")

doc.add_heading("Interferencias con Instalaciones Existentes", level=2)
p(doc, "El recinto de la planta desaladora cuenta con instalaciones existentes (módulos de desalación, cañerías, tendidos eléctricos) cuya presencia deberá verificarse durante el diseño. Se dispone de un levantamiento topográfico del recinto con detecciones de georadar que identifica elementos subterráneos.")
add_img(doc, "IMG-05_Georadar_Recinto.png",
        "Figura 4-4: Ortofoto DIO Abr-2026 del recinto PD Taltal con levantamiento topográfico y puntos de referencia.",
        width=Inches(6))

doc.add_heading("Bancos de Ductos Subterráneos", level=2)
p(doc, "El levantamiento DIO Abr-2026 (DESALADORA 050326_mod 3.dwg), entregado como antecedente en la carpeta 01_SITIO/LEVANTAMIENTO_DIO_2026/, indica los bancos de ductos subterráneos que deben respetarse o integrarse en el diseño de fundaciones. Los bancos se ubican en dos zonas principales:")
bullet(doc, "Bajo la fundación del módulo completo (contenedor RO 40ft HC y equipos CIP exteriores).")
bullet(doc, "Bajo la fundación del estanque de salmuera TK-06-001 y de la bomba de alimentación BH-06-001.")
p(doc, "El consultor deberá verificar las interferencias con los bancos de ductos al definir las profundidades de fundación, las pasadas de armaduras y los detalles de anclaje, y compatibilizar el diseño con la ubicación y cota de los bancos indicados en el plano de levantamiento.")

doc.add_heading("Modelo 3D del Proyecto", level=2)
p(doc, "ADASA pone a disposición del consultor el modelo 3D consolidado del proyecto (Maqueta Gral.nwd, formato Navisworks), que integra el contenedor RO, los equipos exteriores del área 06, las cañerías de interconexiones y los bancos de ductos subterráneos. El modelo se entrega en la carpeta 05_MAQUETA_3D/ como apoyo visual para el entendimiento del proyecto y para la verificación tridimensional de interferencias entre fundaciones, estructuras metálicas y componentes mecánicos durante el desarrollo de la ingeniería de detalle. El modelo es de consulta y no reemplaza a los planos 2D vigentes, que prevalecen en caso de discrepancia.")

# --- SECTION 5: ANTECEDENTES ---
doc.add_heading("ANTECEDENTES", level=1)
p(doc, "ADASA pondrá a disposición del consultor un paquete único de antecedentes con la información necesaria para el desarrollo del servicio. Las especificaciones técnicas de obras civiles son entregables del consultor y no forman parte de este paquete.")

_link_para = doc.add_paragraph()
_link_run = _link_para.add_run("El paquete completo está disponible para descarga en línea: ")
_link_run.font.name = "Arial"
_link_run.font.size = Pt(11)
add_hyperlink(_link_para, ANTECEDENTES_URL, "Paquete ANTECEDENTES — Synology Drive", size=11)
_link_tail = _link_para.add_run(".")
_link_tail.font.name = "Arial"
_link_tail.font.size = Pt(11)

p(doc, "El paquete se organiza en cinco grupos de información:")
bullet(doc, "Planos de sitio y estudios topográficos — informe sísmico del emplazamiento, planos del recinto, detecciones de georadar y Levantamiento DIO Abr-2026.")
bullet(doc, "Planos mecánicos y de piping del módulo (Van Doorn) — plano de montaje del módulo de desalación y planos de cañerías de interconexiones y del estanque con bomba de alimentación.")
bullet(doc, "Planos y memorias de equipos con impacto civil — documentación de los equipos cuyas cargas influyen en el diseño de fundaciones.")
bullet(doc, "Planos BW Water vigentes — Equipment Layout, Piping Layout, Cable Tray Layout (detalles de soportes) y Tie-In Point Layout preliminar. Define cargas, huellas e interfaces estructurales del contenedor y equipos CIP.")
bullet(doc, "Modelo 3D del proyecto — maqueta consolidada en formato Navisworks como apoyo al entendimiento global y a la verificación tridimensional de interferencias.")

doc.add_heading("Planos de Sitio y Estudios Topográficos", level=2)
add_simple_table(doc, [
    ("Documento", "Descripción"),
    ("LNS-ADASA-INF-040 Rev 0", "Informe sísmico del emplazamiento (Zona 3 NCh 2369:2025)"),
    ("Plano del recinto PD Taltal Rev 2", "Plano topográfico del recinto (DWG)"),
    ("Plano del recinto PD Taltal con ortofoto Rev 0", "Plano del recinto con ortofoto (PDF)"),
    ("Plano del recinto PD Taltal con georadar Rev 1", "Detecciones de instalaciones subterráneas"),
    ("Levantamiento DIO Abr-2026 (DESALADORA 050326_mod 3.dwg + Layout PDF)", "Situación actual con cotas y bancos de ductos"),
    ("Ortomosaico DES TALTAL_transparent_mosaic_group1.tif", "Ortomosaico aéreo georeferenciado"),
])

doc.add_heading("Planos Mecánicos y de Piping del Módulo", level=2)
p(doc, "Revisiones vigentes al momento de la adjudicación, utilizadas como base para definir cargas, huellas y tie-in points hacia las estructuras civiles.")
add_simple_table(doc, [
    ("Código", "Título"),
    ("P22-DWG-06-005-103", "Plano de Montaje — Módulo de Desalación"),
    ("P22-DWG-06-006-101", "Cañerías Interconexiones — Planta"),
    ("P22-DWG-06-006-102", "Cañerías Interconexiones — Cortes y Detalles"),
    ("P22-DWG-06-006-103", "Cañerías TK Salmuera y Bomba Alimentación — Planta"),
    ("P22-DWG-06-006-104", "Cañerías TK Salmuera y Bomba Alimentación — Cortes y Detalles"),
    ("P22-DWG-06-005-104", "Drenajes — trazado, cámaras y cotas"),
])

doc.add_heading("Planos y Memorias de Equipos con Impacto Civil", level=2)
p(doc, "Se incluyen únicamente los equipos cuyos datos son necesarios para el diseño de fundaciones. Otros equipos del proyecto (válvulas, instrumentación, equipos dentro del contenedor) no influyen en el alcance civil.")
add_simple_table(doc, [
    ("Equipo", "Documentos"),
    ("Estanque TK-06-001 (Exfibro)", "Plano GA EX-26005-F01 Rev C (anclajes y topes sísmicos); Memoria de Cálculo AFTA Taltal"),
    ("Bomba BH-06-001 (KSB)", "Plano GA KSB-AAF-KNCPP11-050+160M Rev A (baseplate y anclajes); Datasheet CV406762 Rev 02"),
])

doc.add_heading("Planos BW Water Vigentes", level=2)
p(doc, "Entregas formales BW Water incorporadas al paquete (ENTREGA 32, 20-Abr-2026, salvo donde se indique).")
add_simple_table(doc, [
    ("Código", "Rev", "Título"),
    ("P22-DWG-09-005-003", "B", "Equipment Layout — cargas y huella del contenedor y equipos CIP; tabla de pesos en operación incorporada"),
    ("P22-DWG-09-005-004", "B", "Piping Layout del módulo"),
    ("P22-DWG-09-007-004", "B", "Cable Tray Layout and Support Details — soportes con impacto estructural"),
    ("P22-DWG-09-005-005", "C", "Tie-In Point Layout"),
])

doc.add_heading("Modelo 3D del Proyecto", level=2)
add_simple_table(doc, [
    ("Documento", "Descripción"),
    ("Maqueta Gral.nwd (Navisworks)", "Modelo 3D consolidado del proyecto — contenedor RO, equipos área 06, cañerías de interconexiones y bancos de ductos. Apoyo al entendimiento global y a la verificación tridimensional de interferencias. Prevalecen los planos 2D vigentes en caso de discrepancia."),
])


# --- SECTION 6: ENTREGABLES ---
doc.add_heading("ENTREGABLES POR PARTE DEL CONSULTOR", level=1)
p(doc, "El consultor deberá entregar los siguientes documentos como resultado del servicio de ingeniería de detalle:")

doc.add_heading("Memorias de Cálculo", level=2)
p(doc, "Los documentos se codifican según P00-IT-00-000-101. El cálculo de anclajes de equipos a fundaciones conforme a ACI 318-19 se incorpora en cada memoria de cálculo correspondiente y no constituye un documento separado.")
add_simple_table(doc, [
    ("Código", "Título", "Contenido principal"),
    ("P22-MC-00-002-001", "Fundación estanque TK-06-001", "Diseño de fundación incluyendo llaves de corte y topes sísmicos per Exfibro"),
    ("P22-MC-00-002-002", "Fundación bomba BH-06-001", "Diseño dinámico por vibración conforme ACI 351 — categorías Very Good/Good"),
    ("P22-MC-00-002-003", "Sistema de drenajes — fosa TK-06-002 y red de cámaras CD-06-00N", "Diseño estructural e impermeabilización de la fosa principal; diseño de cámaras prefabricadas (detalle típico, cargas, armaduras); perfil longitudinal con pendientes y cotas; dimensionamiento hidráulico básico"),
    ("P22-MC-00-002-004", "Fundación compartida contenedor + CIP", "Cargas combinadas, diseño sísmico, previsión para pernos químicos"),
    ("P22-MC-00-003-001", "Cubierta metálica CIP", "Diseño para viento, sismo y peso propio"),
])

doc.add_heading("Planos de Construcción", level=2)
p(doc, "Los planos se codifican según P00-IT-00-000-101 (entregado por ADASA como antecedente). El ciclo de revisiones es: Rev A (revisión interna del consultor), Rev B (para revisión del cliente ADASA) y Rev 0 (emitido para construcción).")
p(doc, "Cada entregable será calificado por ADASA con uno de los siguientes códigos:")
bullet(doc, "Code 1 — Approved: aprobado sin observaciones. Avance hacia Rev 0.")
bullet(doc, "Code 2 — Approved as Noted: aprobado con notas menores a incorporar directamente en Rev 0 (sin nueva Rev B).")
bullet(doc, "Code 3 — To Be Revised: requiere nueva Rev B incorporando observaciones antes de Rev 0.")
bullet(doc, "Code 4 — Rejected: entregable rechazado; requiere rehacer.")
p(doc, "El ciclo admite un máximo de dos iteraciones Rev B (Rev B / Rev B.1). Una tercera iteración se trata como incumplimiento de control de calidad interno del consultor y podrá dar lugar a las consecuencias establecidas en la Sección 9 — Condiciones Comerciales y Contractuales.")
add_simple_table(doc, [
    ("Código", "Título"),
    ("P22-DWG-00-001-001", "Excavaciones y movimiento de tierras — planta general y cortes"),
    ("P22-DWG-00-002-001", "Implantación general OOCC — planta georeferenciada con coordenadas y cortes"),
    ("P22-DWG-00-002-002", "Fundaciones equipos exteriores área 06 — planta, armaduras y detalles"),
    ("P22-DWG-00-002-003", "Fundación compartida contenedor + CIP — planta, armaduras y anclajes"),
    ("P22-DWG-00-002-004", "Fosa de drenajes TK-06-002 — planta, cortes, armaduras e impermeabilización"),
    ("P22-DWG-00-003-001", "Cubierta metálica sistema CIP — planta, elevaciones, cortes y detalles de conexión"),
    ("P22-DWG-00-002-005", "Detalles de anclaje y conexiones — incluye previsión pernos químicos zona CIP"),
    ("P22-DWG-00-002-006", "Canalizaciones y red de drenajes — tres láminas: L1 planta general y trazado; L2 cámaras CD-06-00N (detalle típico prefabricado, armaduras, tapa y sellos); L3 perfil longitudinal con cotas y pendientes"),
])

doc.add_heading("Especificaciones Técnicas", level=2)
p(doc, "El consultor deberá elaborar tres especificaciones técnicas:")
p(doc, "La codificación final se confirmará contra P00-IT-00-000-101 al inicio del contrato.")
p(doc, "P22-ET-00-010-101-0 — Especificación Técnica de Movimiento de Tierras y Excavaciones", bold=True)
bullet(doc, "Excavación con taludes admisibles; rellenos granulares en capas ≤30 cm compactadas al 95% Proctor Modificado")
bullet(doc, "Sin explosivos — fracturadores no explosivos ante roca (instalaciones operativas en el recinto)")
bullet(doc, "Sales solubles <3% en rellenos (ambiente marino)")
bullet(doc, "Verificación previa de interferencias subterráneas con plano georadar disponible como antecedente")
bullet(doc, "Ensayos de compactación en laboratorio acreditado; documentos de cierre")
p(doc, "P22-ET-00-010-102-0 — Especificación Técnica de Hormigón Armado", bold=True)
bullet(doc, "Hormigón G-25 mínimo (NCh 170:2016); armadura A630-420H; recubrimientos ≥50 mm en elementos expuestos, ≥70 mm en contacto con terreno")
bullet(doc, "Tolerancias de armado; ensayos de resistencia en obra; documentos de cierre")
p(doc, "P22-ET-00-010-103-0 — Especificación Técnica de Estructura Metálica", bold=True)
bullet(doc, "Acero ASTM A-36; soldaduras AWS D1.1; pernos galvanizados en caliente o inoxidable en ambiente expuesto")
bullet(doc, "Sistema de protección: SSPC-SP10 + imprimación zinc epóxico 80 µm + epóxico alto espesor 200 µm + poliuretano alifático 75 µm (RAL 5012)")
bullet(doc, "Fabricación en taller con inspección por capas; documentos de cierre")

doc.add_heading("Cubicaciones y Presupuesto", level=2)
p(doc, "El consultor entregará cubicaciones detalladas por partida y un presupuesto de construcción con los siguientes criterios:")
bullet(doc, "Nivel de estimación: Clase 1 AACE International (estimación definitiva, precisión ±3% a ±15%, apropiada para ingeniería de detalle).")
bullet(doc, "Partidas mínimas requeridas: movimiento de tierras y rellenos; hormigón armado por elemento (fundaciones por equipo, fosa, cámaras, pavimentos); acero de refuerzo; acero estructural (perfiles, chapas, conexiones); soldadura; sistema de protección superficial por m²; techado por m²; impermeabilización por m².")
bullet(doc, "Formato de entrega: planilla Excel estructurada por partida, con vínculos a los planos de construcción y a las memorias correspondientes.")

# --- SECTION 7: FORMATO DE DOCUMENTOS ---
doc.add_heading("FORMATO DE DOCUMENTOS Y PLANOS", level=1)

doc.add_heading("Codificación", level=2)
p(doc, "Todos los documentos y planos generados por el consultor deberán codificarse según el sistema establecido en el documento P00-IT-00-000-101 (Codificación General del Proyecto), que será entregado como antecedente.")

doc.add_heading("Formatos de Entrega", level=2)
add_simple_table(doc, [
    ("Tipo de documento", "Formato nativo", "Formato adicional", "Software"),
    ("Planos", "DWG", "PDF", "AutoCAD 2025 o superior"),
    ("Memorias de cálculo", "DOCX", "PDF", "Microsoft Word"),
    ("Cubicaciones y listas", "XLSX", "PDF", "Microsoft Excel"),
    ("Especificaciones técnicas", "DOCX", "PDF", "Microsoft Word"),
])
p(doc, "Los planos se entregarán en tamaño A1 (841 × 594 mm) con escalas apropiadas: 1:50 para plantas generales, 1:25 para detalles constructivos.")

doc.add_heading("Software y Plataforma", level=2)
p(doc, "La documentación se entregará en formato digital mediante los medios que ADASA determine. El consultor deberá mantener la compatibilidad con AutoCAD 2025 para archivos DWG y con Microsoft Office para documentos escritos y planillas.")

# --- SECTION 8: PLAZOS ---
doc.add_heading("PLAZOS DE EJECUCIÓN", level=1)
p(doc, "El plazo total para el desarrollo del servicio es de cuatro (4) semanas corridas contadas desde la fecha de adjudicación del contrato y recepción formal del paquete completo de antecedentes. El consultor deberá presentar un programa detallado de trabajo dentro de los primeros 3 días hábiles.", bold=False)
add_simple_table(doc, [
    ("Hito", "Semana", "Entregables"),
    ("H0 — Inicio", "0", "Programa detallado de trabajo"),
    ("H1 — Revisión A", "1", "Memorias borrador + planos preliminares"),
    ("H2 — Revisión B", "2", "Documentos para revisión ADASA (5 días hábiles)"),
    ("H3 — Comentarios", "3", "Documentos corregidos según comentarios ADASA"),
    ("H4 — Revisión 0", "3.5", "Documentos para construcción"),
    ("H5 — Cierre", "4", "Cubicaciones finales y presupuesto"),
])

# --- SECTION 8.5: CONDICIONES COMERCIALES ---
doc.add_heading("CONDICIONES COMERCIALES Y CONTRACTUALES", level=1)
p(doc, "El presente servicio se contrata bajo la modalidad de trato directo, en el marco del contrato marco suscrito entre ADASA y el consultor. Las condiciones comerciales que se detallan a continuación se rigen por dicho contrato marco; este TdR no introduce exigencias adicionales más allá de los hitos técnicos definidos en la Sección 8 — Plazos de Ejecución.")

doc.add_heading("Moneda, Forma de Pago y Reajustes", level=2)
p(doc, "La moneda, los reajustes, la forma de pago y los plazos de pago se rigen por el contrato marco suscrito entre ADASA (a través del Departamento de Ingeniería y Optimización, DIO) y el consultor. Los hitos técnicos H1 a H5 definidos en la Sección 8 — Plazos de Ejecución sirven de referencia para la emisión de estados de pago conforme al mecanismo establecido en ese contrato.")

doc.add_heading("Garantías y Seguros", level=2)
p(doc, "Las garantías, retenciones y seguros se rigen por las condiciones del contrato marco suscrito entre ADASA y el consultor. Este TdR no introduce exigencias adicionales.")

doc.add_heading("Multas por Atraso", level=2)
p(doc, "Las multas por atraso en la entrega de hitos se aplican conforme a lo establecido en el contrato marco suscrito entre ADASA y el consultor.")

doc.add_heading("Término Anticipado", level=2)
p(doc, "Las causales y el procedimiento de término anticipado del servicio se rigen por las condiciones del contrato marco suscrito entre ADASA y el consultor.")

doc.add_heading("Propiedad Intelectual y Confidencialidad", level=2)
p(doc, "Todos los entregables (DWG, DOCX, XLSX, PDF) generados en cumplimiento del servicio son de propiedad exclusiva de ADASA. El consultor podrá conservar copias para su archivo técnico interno y reutilizar detalles tipo no específicos del proyecto sin restricción.")
p(doc, "El consultor y su personal se obligan a confidencialidad respecto de toda la información del proyecto durante el contrato y por cinco (5) años posteriores a su término.")

doc.add_heading("Resolución de Controversias", level=2)
p(doc, "La resolución de controversias se rige por el mecanismo establecido en el contrato marco suscrito entre ADASA y el consultor.")

# --- SECTION 8.7: MATRIZ RACI ---
doc.add_heading("MATRIZ DE RESPONSABILIDADES (RACI)", level=1)
add_simple_table(doc, [
    ("Actividad", "Consultor", "ADASA"),
    ("Diseño OOCC (memorias, planos, ET)", "R", "A"),
    ("Validación normativa", "R", "A"),
    ("Entrega antecedentes del sitio", "I", "R"),
    ("Entrega planos mecánicos área 06", "C", "R"),
    ("Entrega planos módulo área 09", "C", "R"),
    ("Aprobación formal Rev 0", "—", "R"),
    ("Coordinación pernos químicos CIP", "R", "A"),
    ("Verificación de suelo en obra", "C", "R"),
])
p(doc, "R = Responsable | A = Aprobador | C = Consultado | I = Informado. Los RFI del consultor se canalizarán siempre a través de ADASA como único interlocutor contractual. ADASA consolida internamente la información técnica requerida y la comunica formalmente al consultor.")

# --- SECTION 9: COMUNICACIÓN ---
doc.add_heading("COMUNICACIÓN Y ESTADOS DE AVANCE", level=1)

doc.add_heading("Informes de Avance", level=2)
p(doc, "El consultor presentará informes semanales de avance que incluyan: porcentaje de avance por entregable, desviaciones respecto al programa, consultas técnicas pendientes y plan de trabajo para la semana siguiente.")

doc.add_heading("Reuniones de Coordinación", level=2)
p(doc, "Se programarán reuniones semanales de coordinación entre el consultor y ADASA por videoconferencia. El servicio se desarrolla completamente de forma remota; no se considera presencialidad en sitio.")

doc.add_heading("Mecanismo de Revisiones", level=2)
p(doc, "Las revisiones seguirán el ciclo Revisión A → Revisión B → Revisión 0 con códigos de aceptación Code 1 a Code 4 definidos en la Sección 6 — Entregables por parte del Consultor. ADASA dispondrá de 7 días hábiles para revisar cada entrega y emitir sus comentarios mediante transmittal formal.")

# =============================================================================
# 3. SAVE
# =============================================================================
doc.save(OUTPUT)
print(f"\nDocumento generado exitosamente: {OUTPUT}")
print(f"Tamaño: {os.path.getsize(OUTPUT):,} bytes")
