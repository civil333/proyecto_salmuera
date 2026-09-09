#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Nota Tecnica P22-NT-06-000-002-0 con la skill template-adasa.

Documento: Ingenieria del modulo RO de segunda etapa de salmuera desarrollada por
           BW Water, en la ultima revision aprobada por ADASA.
Destinatario: equipo de proyecto de Aguas Antofagasta. Idioma espanol (es-CL).
Fuente del texto: P22-NT-06-000-002-0_Ingenieria-Modulo-BW-Water.md

Path del skill: absoluto via ~/.claude/skills/template-adasa (Synology no soporta
symlinks, ver CLAUDE.md Seccion 3). La skill pone portada, cajetin, TOC embebido,
estilos Arial y encabezado. NO se duplica nada de eso a mano.

Los encabezados NO llevan numeros: el template numera H1/H2/H3 solo (numId=1).
"""
import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    add_simple_table,
)
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# La tabla de vigencia se IMPORTA del catalogo, que es donde ya vive. Lo produce
# catalogar_ingenieria_bw.py desde el Registro Maestro y alimenta ademas al
# constructor del dossier y a su gate, de modo que hay una sola fuente y no tres.
sys.path.insert(0, os.path.abspath(os.path.join(
    SCRIPT_DIR, "..", "..", "BORRADOR_REV0", "script")))
from vigencia_bw import VIGENCIA_BW  # noqa: E402

OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-NT-06-000-002-0_Ingenieria-Modulo-BW-Water_ADASA.docx",
)
LANG = "es-CL"


# --------------------------------------------------------------------- helpers
def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para_bold_lead(doc, lead, body, size=11):
    """Parrafo que abre con un rotulo en negrita y sigue en redonda."""
    para = doc.add_paragraph()
    run_lead = para.add_run(lead)
    run_lead.bold = True
    run_lead.font.name = "Arial"
    run_lead.font.size = Pt(size)
    run_body = para.add_run(body)
    run_body.font.name = "Arial"
    run_body.font.size = Pt(size)
    return para


def _set_lang_in_rPr(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    """Sin esto Word subraya tildes y enes en rojo (CLAUDE.md Seccion 3.4)."""
    try:
        _set_lang_in_rPr(doc.styles["Normal"].element.get_or_add_rPr(), lang)
    except KeyError:
        pass
    for p in doc.paragraphs:
        for r in p.runs:
            _set_lang_in_rPr(r._element.get_or_add_rPr(), lang)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        _set_lang_in_rPr(r._element.get_or_add_rPr(), lang)


MESES_EN_ES = {
    "January": "enero", "February": "febrero", "March": "marzo", "April": "abril",
    "May": "mayo", "June": "junio", "July": "julio", "August": "agosto",
    "September": "septiembre", "October": "octubre", "November": "noviembre",
    "December": "diciembre",
}


def traducir_mes_portada(doc):
    """La skill escribe el mes de la portada con el locale del sistema (ingles)."""
    for para in doc.paragraphs:
        if "Antofagasta," not in para.text:
            continue
        for run in para.runs:
            for en, es in MESES_EN_ES.items():
                if en in run.text:
                    run.text = run.text.replace(en, es)


def limpiar_placeholder(doc):
    """Elimina el contenido de ejemplo del template desde el primer Heading 1."""
    borrar, encontrado = [], False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            borrar.append(para)
    for para in borrar:
        para._element.getparent().remove(para._element)


# ------------------------------------------------------------------- contenido
# El titulo del Registro Maestro esta en ingles abreviado, que es como lo rotula
# el proveedor. La nota va en espanol, de modo que la tabla lleva el titulo
# traducido y el codigo permite dar con el archivo en el dossier.
TITULOS_ES = {
    "P22-ET-09-000-001": "Hoja de datos del contenedor del módulo",
    "P22-BT-09-009-001": "Filosofía de control",
    "P22-CD-09-009-001": "Memoria de cálculo de proceso",
    "P22-DWG-09-009-002": "P&ID, diagrama de cañerías e instrumentación",
    "P22-DWG-09-009-01": "PFD, diagrama de flujo de proceso",
    "P22-ET-09-009-001": "Hoja de datos del sistema UHPRO (membranas y portamembranas)",
    "P22-ET-09-009-002": "Hoja de datos de la bomba de alta presión",
    "P22-ET-09-009-003": "Hoja de datos de la bomba CIP",
    "P22-ET-09-009-004": "Hoja de datos de la bomba dosificadora de antiescalante",
    "P22-ET-09-009-005": "Hoja de datos del filtro de cartucho de la osmosis",
    "P22-ET-09-009-006": "Hoja de datos del filtro de cartucho del sistema CIP",
    "P22-ET-09-009-007": "Hoja de datos del turbocargador de alimentación",
    "P22-ET-09-009-008": "Hoja de datos del turbocargador interetapa",
    "P22-ET-09-009-009": "Hoja de datos del estanque CIP",
    "P22-ET-09-009-010": "Hoja de datos del estanque de antiescalante",
    "P22-ET-09-009-011": "Hoja de datos del calentador del estanque CIP",
    "P22-ET-09-009-012": "Hoja de datos del mezclador estático",
    "P22-LI-09-009-001": "Listado de consumos de utilidades",
    "P22-LI-09-009-002": "Listado de consumos de químicos",
    "P22-LI-09-009-003": "Listado de líneas",
    "P22-CD-09-005-001": "Informe de cálculo estructural del bastidor UHPRO",
    "P22-CD-09-005-002": "Memoria de cálculo térmico del aire acondicionado",
    "P22-CD-09-005-003": "Criterios de diseño estructural del bastidor UHPRO",
    "P22-DWG-09-005-001": "Plano de necesidades civiles y cargas",
    "P22-DWG-09-005-003": "Plano de disposición de equipos",
    "P22-DWG-09-005-004": "Plano de disposición de cañerías",
    "P22-DWG-09-005-005": "Plano de puntos de conexión",
    "P22-DWG-09-005-008": "Plano general del skid del sistema SWRO",
    "P22-DWG-09-005-010": "Plano general de la bomba de lavado CIP",
    "P22-DWG-09-005-011": "Plano general de la bomba dosificadora de antiescalante",
    "P22-DWG-09-005-012": "Plano general del turbocargador de alimentación (SIP-09-001)",
    "P22-DWG-09-005-013": "Plano general del turbocargador interetapa (SIP-09-002)",
    "P22-DWG-09-005-014": "Plano general del estanque de lavado CIP",
    "P22-DWG-09-005-015": "Plano general del estanque de antiescalante",
    "P22-LI-09-005-001": "Listado de equipos",
    "P22-LI-09-005-002": "Listado de válvulas",
    "P22-ET-09-006-001": "Especificación de cañerías",
    "P22-ET-09-006-002": "Especificación de pintura",
    "P22-CD-09-007-001": "Diagrama unifilar",
    "P22-DWG-09-007-003": "Plano de puesta a tierra y ubicación del tablero de poder",
    "P22-DWG-09-007-004": "Plano de bandejas portacables y detalles de soporte",
    "P22-DWG-09-007-005": "Plano de detalles típicos de obras de poder",
    "P22-ET-09-007-001": "Hoja de datos de los auxiliares eléctricos",
    "P22-ET-09-007-002": "Hoja de datos de los cables de poder y de control",
    "P22-ET-09-007-003": "Hoja de datos de la bandeja portacables",
    "P22-ET-09-007-004": "Hoja de datos de la canalización y el flexible",
    "P22-ET-09-007-005": "Hoja de datos del tablero local de control (LCP)",
    "P22-LI-09-007-001": "Listado de cargas eléctricas",
    "P22-LI-09-007-002": "Programa de cables de poder",
    "P22-CD-09-004-001": "Arquitectura del sistema de control",
    "P22-CD-09-008-001": "Plano exterior del tablero PLC-LCP",
    "P22-CD-09-008-002": "Esquemático del tablero PLC-LCP",
    "P22-DWG-09-008-001": "Plano de ubicación de instrumentos",
    "P22-ET-09-008-001": "Hoja de datos del PLC y la interfaz de operación",
    "P22-LI-09-008-001": "Listado de entradas y salidas",
    "P22-LI-09-008-002": "Programa de cables de instrumentación y control",
    "P22-LI-09-008-003": "Listado de instrumentos",
    "P22-LI-09-008-004": "Listado de transferencia de datos (Modbus TCP)",
    "P22-LI-09-008-005": "Hoja de datos del analizador de conductividad",
    "P22-LI-09-008-006": "Hoja de datos del presostato diferencial",
    "P22-LI-09-008-007": "Hoja de datos del transmisor de caudal",
    "P22-LI-09-008-008": "Hoja de datos del interruptor de nivel",
    "P22-LI-09-008-009": "Hoja de datos del transmisor de nivel",
    "P22-LI-09-008-010": "Hoja de datos del analizador de pH y ORP",
    "P22-LI-09-008-011": "Hoja de datos del manómetro",
    "P22-LI-09-008-012": "Hoja de datos del transmisor de presión",
    "P22-LI-09-008-013": "Hoja de datos del transmisor de temperatura",
    "P22-LI-09-008-014": "Hoja de datos del transmisor de vibración",
    "P22-LI-09-008-015": "Listado de alarmas y enclavamientos",
    "P22-LI-09-008-016": "Pantallas de la interfaz de operación",
    "P22-LI-09-008-017": "Carta de control y secuencias",
}

# Que queda abierto en cada documento aprobado con observaciones, tomado del
# transmittal que lo dispuso.
CONDICIONES = {
    "P22-CD-09-009-001":
        "Completar el cálculo de consumo específico de energía y verificar la tasa de "
        "recuperación.",
    "P22-ET-09-009-003":
        "Se aceptó el cambio de variador a partida directa, y queda pendiente la "
        "compatibilidad del motor.",
    "P22-ET-09-009-010":
        "Observaciones menores de la hoja.",
    "P22-CD-09-005-001":
        "El cálculo se acepta. El PDF es una concatenación duplicada de unos 58 megabytes "
        "y la hoja de comentarios omite el texto original de ADASA.",
    "P22-DWG-09-005-001":
        "Las dos partes de la observación del transmittal N16 siguen abiertas: el peso "
        "total del contenedor modificado, y la composición del peso de operación del "
        "bastidor, donde el marco no aparece en ninguna fila.",
    "P22-DWG-09-005-004":
        "Tres puntos por segundo ciclo: el cuadro de conexiones no cubre las siete líneas "
        "del sistema CIP y sus cotas no declaran nivel de referencia, falta la clase de "
        "brida en las terminaciones de antiescalante y CIP, y la lámina muestra dos "
        "gabinetes rotulados LCP sin TAG.",
    "P22-DWG-09-005-011":
        "La reconciliación de las reacciones de anclaje no cierra por segundo ciclo: la "
        "fuerza vertical por perno es el doble del cociente de la fuerza total entre los "
        "diez pernos.",
    "P22-DWG-09-005-014":
        "El cuadro de boquillas no concuerda con la hoja de datos del estanque CIP: la "
        "abertura superior figura como manhole de 533 milímetros donde la hoja de datos "
        "declara handhole DN300, y dos boquillas no tienen equivalente.",
    "P22-DWG-09-005-015":
        "Dos puntos menores del detalle nuevo: el agujero de anclaje está acotado en 14 "
        "milímetros y media pulgada para un perno M12, y la fila de marcación de nivel no "
        "lleva tamaño ni cota.",
    "P22-CD-09-008-002":
        "La señal de marcha del calentador CIP no tiene borne en ninguna lámina de entradas "
        "digitales, y la lista de materiales sigue nombrando el terminal de operador "
        "2711P-T10C21D8S en lugar del modelo que ADASA declaró vinculante.",
    "P22-DWG-09-008-001":
        "El bloque de revisiones repite la misma descripción en sus cuatro filas y la fila "
        "de la revisión C fue sobrescrita, de modo que no se distingue qué cambió en cada "
        "emisión.",
    "P22-LI-09-008-016":
        "Dos transmisores de presión quedaron cruzados entre la pantalla de primera y de "
        "segunda etapa, y se invierten al emitir la revisión 0.",
}

NO_ENTREGADOS = [
    ("Memoria de cálculo sísmico según NCh 2369", "Sección 7, página 28"),
    ("Análisis de flexibilidad de líneas de alta presión", "Sección 7, página 28"),
    ("Maqueta 3D interoperable con la suite de Autodesk", "Sección 7, página 28"),
    ("Isometrías de líneas de alta presión", "Sección 7, página 28"),
    ("Vigas carrileras y puntos de izaje internos", "Sección 7, página 28"),
    ("Sistema de comunicación Modbus TCP y mapa de memoria", "Sección 5.4"),
]

DISCREPANCIAS = [
    ("Especificación de cañerías", "P22-ET-09-005-001", "P22-ET-09-006-001"),
    ("Especificación de pintura", "P22-ET-09-005-002", "P22-ET-09-006-002"),
    ("Hoja de datos del estanque CIP", "P22-ET-09-009-010", "P22-ET-09-009-009"),
    ("Hoja de datos del estanque de antiescalante", "P22-ET-09-009-011",
     "P22-ET-09-009-010"),
    ("Hoja de datos del calentador del estanque CIP", "P22-ET-09-009-014",
     "P22-ET-09-009-011"),
]


def titulo_es(codigo, fallback):
    return TITULOS_ES.get(codigo, fallback)


# ----------------------------------------------------------------- documento
def crear_documento():
    crear_documento_adasa(
        titulo="INGENIERÍA DEL MÓDULO RO DE BW WATER",
        codigo="P22-NT-06-000-002-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)
    limpiar_placeholder(doc)

    total = len(VIGENCIA_BW)
    c1 = sum(1 for f in VIGENCIA_BW if f[5] == "1")
    c2 = total - c1

    # ---------------------------------------------------------- 1. Objeto
    doc.add_heading("OBJETO DE ESTA NOTA", level=1)
    add_para(doc,
        "Esta nota acompaña al dossier Ingeniería Módulo BW Water y explica qué contiene, "
        "con qué criterio se eligió la revisión de cada documento y qué queda abierto. Se "
        "dirige al equipo de proyecto de Aguas Antofagasta.")
    add_para(doc,
        f"El dossier reúne {total} documentos de ingeniería del módulo de osmosis inversa, "
        "todos en la última revisión que ADASA aprobó, repartidos en seis carpetas por "
        "especialidad. Ocupa 340 megabytes.")
    add_para(doc,
        "Esta nota no modifica el Contrato ni ninguno de sus anexos, y tampoco constituye "
        "una emisión de ingeniería. Es un instrumento de trabajo interno: pone en una sola "
        "carpeta lo que hoy vive repartido en noventa carpetas de entrega.")

    # ------------------------------------------------------- 2. Contenido
    doc.add_heading("CONTENIDO DEL DOSSIER", level=1)
    add_para_bold_lead(doc, "0. CONTROL DE CAMBIOS. ",
        "Una copia de esta misma nota en PDF, de modo que el dossier viaje siempre con el "
        "documento que lo explica.")
    add_para_bold_lead(doc, "1. GENERAL, un documento. ",
        "La hoja de datos del contenedor del módulo, que fija sus dimensiones y su peso de "
        "operación.")
    add_para_bold_lead(doc, "2. PROCESO, diecinueve documentos. ",
        "El diagrama de flujo y el P&ID, el cálculo de proceso, la filosofía de control, "
        "los listados de líneas y de consumos, y las trece hojas de datos de los equipos: "
        "el sistema UHPRO, la bomba de alta presión, la bomba CIP, la dosificadora de "
        "antiescalante, los dos filtros de cartucho, los dos turbocargadores, los estanques "
        "CIP y de antiescalante, el calentador del estanque CIP y el mezclador estático.")
    add_para_bold_lead(doc, "3. MECANICA, dieciséis documentos. ",
        "El cálculo estructural del bastidor con sus criterios de diseño, el cálculo "
        "térmico del aire acondicionado, el plano de necesidades civiles y cargas, los "
        "planos de disposición de equipos y de cañerías, los puntos de conexión, los siete "
        "planos generales de los skids y estanques, y los listados de equipos y de "
        "válvulas.")
    add_para_bold_lead(doc, "4. CANERIAS, dos documentos. ",
        "Las especificaciones de cañerías y de pintura.")
    add_para_bold_lead(doc, "5. ELECTRICIDAD, once documentos. ",
        "El diagrama unifilar, los planos de puesta a tierra, de bandejas portacables y de "
        "obras de poder, las hojas de datos de los auxiliares eléctricos, los cables, la "
        "bandeja, la canalización y el tablero local, y los listados de cargas y de cables "
        "de poder.")
    add_para_bold_lead(doc, "6. CONTROL E INSTRUMENTACION, veintidós documentos. ",
        "La arquitectura del sistema de control, el plano exterior y el esquemático del "
        "tablero PLC, el plano de ubicación de instrumentos, la hoja de datos del PLC y la "
        "interfaz, los listados de entradas y salidas, de instrumentos, de cables, de "
        "transferencia Modbus, de alarmas y enclavamientos, las diez hojas de datos de "
        "instrumentos, las pantallas de la interfaz y la carta de secuencias.")
    add_para(doc,
        "Cada carpeta lleva un archivo LEEME con su listado y lo que conviene mirar de esa "
        "especialidad.")
    add_para(doc,
        "Todo el dossier es PDF. BW Water no ha entregado ningún listado en formato "
        "editable, de modo que los listados de instrumentos, de líneas, de válvulas, de "
        "equipos y de entradas y salidas están en PDF y no hay otra versión disponible. Los "
        "archivos nativos de AutoCAD que el proveedor sí entregó de algunos planos quedan "
        "en su carpeta de entrega y no viajan en este dossier.")
    add_para(doc,
        "Los nombres de archivo se uniformaron a código, revisión y título. El proveedor "
        "usa seis grafías distintas para la revisión, que van desde el guion bajo con la "
        "letra hasta la abreviatura en mayúsculas con punto, y con ellas el dossier no se "
        "puede ordenar. El código y la revisión de cada archivo son los del cajetín del "
        "documento.")

    # ---------------------------------------------------------- 3. Criterio
    doc.add_heading("CÓMO SE ELIGIÓ LA REVISIÓN DE CADA DOCUMENTO", level=1)
    add_para(doc,
        "El dossier lleva, para cada documento, la última revisión que ADASA aprobó en "
        "Código 1 o en Código 2. La fuente es el Registro Maestro de Entregables "
        "P22-IT-06-000-002-0, que es donde vive el estado de cada entregable al cierre del "
        "último transmittal, el N38 del 3 de septiembre de 2026.")
    add_para(doc,
        f"De los {total} documentos, {c1} están en Código 1 y {c2} en Código 2. En "
        "ingeniería no hay ningún documento en Código 3 ni en Código 4, de modo que no hubo "
        "que elegir entre una revisión aprobada y una posterior rechazada.")
    add_para(doc,
        "Un documento en Código 2 rige, y hay que leerlo entendiendo que va a cambiar en el "
        "detalle que se indica. La sección siguiente los lista uno por uno.")

    doc.add_heading("Cinco documentos donde el registro y el documento no coinciden",
                    level=2)
    add_para(doc,
        "Al armar el dossier aparecieron cinco discrepancias entre el Registro Maestro y el "
        "documento emitido. En todas manda el documento, que es el que el equipo va a tener "
        "en la mano, y el registro se corrige por separado.")
    add_simple_table(doc,
        [("Documento", "El registro dice", "El documento dice")] + DISCREPANCIAS)
    add_para(doc,
        "Las dos especificaciones están codificadas en la disciplina de cañerías y el "
        "registro las anota en la de mecánica. Las tres hojas de datos de estanques llevan "
        "el correlativo corrido en uno: el título y la entrega del registro calzan exactos "
        "con el archivo, y lo único desplazado es el número.")
    add_para(doc,
        "Los dos planos generales de los turbocargadores son revisión A. El registro los "
        "anota en revisión B. Llegaron una sola vez, en la entrega 14, y su cajetín dice "
        "Revision No.: A. No existe una revisión B en el repositorio, de modo que el dossier "
        "lleva la única que hay.")
    add_para(doc,
        "El plano de puntos de conexión aparece bajo una entrega que no existe. El registro "
        "lo declara en la entrega 87, que es el hueco de la serie del proveedor, y el "
        "archivo está en la entrega 88.")

    # ------------------------------------------------------- 4. Los Codigo 2
    doc.add_heading("LOS DOCUMENTOS APROBADOS CON OBSERVACIONES", level=1)
    add_para(doc,
        "Estos son los documentos que rigen y que todavía van a cambiar. Se indica qué "
        "queda abierto en cada uno, tal como quedó en el transmittal que lo dispuso.")
    filas_c2 = [(titulo_es(f[0], f[1]), f[2], CONDICIONES.get(f[0], "Por precisar"))
                for f in VIGENCIA_BW if f[5] == "2"]
    add_simple_table(doc,
        [("Documento", "Rev.", "Qué queda abierto")] + filas_c2)
    add_para(doc,
        "Hay un punto que no es una observación del documento y conviene tener presente al "
        "leer el cálculo estructural: el informe no lleva endoso de un profesional inscrito "
        "en Chile. BW Water lo comprometió por escrito el 20 de mayo, el 16 de junio y el "
        "30 de junio, y el 17 de agosto informó que el ingeniero que lo certificaba no está "
        "disponible. La revisión 0 del informe lleva solo iniciales internas.")

    # ------------------------------------------------------ 5. No entregado
    doc.add_heading("LO QUE BW WATER AÚN NO ENTREGA", level=1)
    add_para(doc,
        "El Registro Maestro marca seis entregables de ingeniería de la Sección 7 de la "
        "Especificación Técnica como no recibidos. No están en el dossier porque no "
        "existen.")
    add_simple_table(doc,
        [("Entregable", "Referencia en la Especificación Técnica")] + NO_ENTREGADOS)
    add_para(doc,
        "La especificación de válvulas e instrumentos con marca y modelo figura como "
        "entrega parcial: las hojas de datos individuales están en el dossier y el "
        "documento consolidado que pide la Sección 7 no se ha emitido.")

    # ---------------------------------------------------------- 6. El modelo
    doc.add_heading("EL MODELO TRIDIMENSIONAL", level=1)
    add_para(doc,
        "El modelo federado del módulo existe, es el P22-DWG-09-005-007 en revisión B, y "
        "está aprobado en Código 2. No viaja en este dossier porque es un archivo de "
        "Navisworks y el dossier lleva solo formatos de lectura. Se entrega por enlace a "
        "quien lo pida.")
    add_para(doc,
        "Sobre ese modelo hay un punto abierto que conviene conocer antes de usarlo para "
        "coordinación: la hoja de comentarios de su última revisión declaró corregidos "
        "cincuenta y siete TAG de soportes de cañería que no se tocaron, y hoy son setenta "
        "y dos. Los TAG de válvula sí cerraron.")

    # -------------------------------------------------------- 7. La vigencia
    doc.add_heading("VIGENCIA DE LA DOCUMENTACIÓN", level=1)
    add_para(doc,
        f"La tabla siguiente lista los {total} documentos del dossier, uno por fila, con la "
        "revisión que rige, la entrega en que llegó, el transmittal que la dispuso, el "
        "código de respuesta de ADASA y la carpeta donde se encuentra. Ante cualquier duda "
        "de vigencia prevalece esta tabla.")
    add_simple_table(doc,
        [("Código", "Documento", "Rev.", "Entrega", "TM", "Cód.", "Carpeta")]
        + [(f[0], titulo_es(f[0], f[1]), f[2], f[3], f[4], f[5], f[6])
           for f in VIGENCIA_BW])
    add_para(doc,
        "Esta nota refleja el estado al cierre del transmittal N38, del 3 de septiembre de "
        "2026. Cada transmittal nuevo puede mover la revisión de uno o más documentos, y "
        "entonces el dossier se reconstruye corriendo los dos scripts que lo componen.")

    doc.core_properties.author = "Luis Rivera Gonzalez"
    doc.core_properties.company = "Aguas Antofagasta"
    doc.core_properties.comments = (
        "Nota tecnica del dossier de ingenieria del modulo RO de BW Water, ultima revision "
        "aprobada por ADASA, Planta Desaladora Taltal")
    traducir_mes_portada(doc)
    fijar_idioma_documento(doc)
    doc.save(OUTPUT)
    print(f"Documento generado: {os.path.basename(OUTPUT)}")


if __name__ == "__main__":
    crear_documento()
