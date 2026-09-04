#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Nota Tecnica P22-NT-06-000-001-0 con la skill template-adasa.

Documento: Ingenieria vigente para construccion, Montaje Mecanico y Obras Civiles
           del Modulo de Segunda Etapa de Salmuera, Planta Desaladora Taltal.
Destinatario: contratista adjudicado. Idioma espanol (es-CL).
Fuente del texto: P22-NT-06-000-001-0_Ingenieria-Vigente-para-Construccion.md

Path del skill: absoluto via ~/.claude/skills/template-adasa (Synology no soporta
symlinks, ver CLAUDE.md Seccion 3). La skill pone portada, cajetin, TOC embebido,
estilos Arial y encabezado. NO se duplica nada de eso a mano: sin TOC manual, sin
set_updatefields_true, sin saltos de pagina propios.

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
OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-NT-06-000-001-0_Ingenieria-Vigente-para-Construccion_ADASA.docx",
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


def add_bullet(doc, text, size=11):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    run = para.add_run("•  " + text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
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
    """La skill escribe el mes de la portada con el locale del sistema (ingles).

    En un documento en espanol eso deja 'Antofagasta, September 2026'. Se corrige
    run por run para no perder la fuente ni el centrado del parrafo.
    """
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


# ----------------------------------------------------------------- documento
def crear_documento():
    crear_documento_adasa(
        titulo="INGENIERÍA VIGENTE PARA CONSTRUCCIÓN",
        codigo="P22-NT-06-000-001-0",
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

    # ---------------------------------------------------------- 1. Objeto
    doc.add_heading("OBJETO DE ESTA NOTA", level=1)
    add_para(doc,
        "Se remite al contratista el paquete Ingeniería Vigente para Construcción del "
        "Montaje Mecánico y las Obras Civiles del Módulo de Segunda Etapa de Salmuera de "
        "la Planta Desaladora Taltal, y se declara mediante esta nota qué cambió respecto "
        "de la ingeniería que sirvió de base para cotizar, de modo que el contratista "
        "disponga por escrito del alcance de esos cambios antes de iniciar las obras.")
    add_para(doc,
        "El paquete contiene 54 documentos de ingeniería de detalle mecánica, de obras "
        "civiles y de especificaciones de montaje, distribuidos en 88 archivos. Lo acompaña "
        "la planilla de control de cambios P22-LI-06-000-002-1, la cual identifica, "
        "documento por documento, la revisión que rige y aquello que cambió.")
    add_para(doc, "Esta nota no modifica el Contrato ni ninguno de sus anexos.")

    # ------------------------------------------------ 2. Contenido del paquete
    doc.add_heading("CONTENIDO DEL PAQUETE", level=1)
    add_para(doc, "El paquete se organiza en cuatro carpetas.")
    add_para_bold_lead(doc, "0. CONTROL DE CAMBIOS. ",
        "La planilla P22-LI-06-000-002-1, con cinco hojas: Resumen, Vigencia, Mecánica, "
        "Civil y Cubicaciones.")
    add_para_bold_lead(doc, "1. ING. DETALLE MECANICA, 58 archivos en cuatro subcarpetas. ",
        "00_GENERAL lleva el listado de entregables. 01_PROCESOS_E_INSTRUMENTACION lleva el "
        "diagrama de flujo, los cuatro P&ID, las hojas de datos y el listado de instrumentos, "
        "y la lógica de control. 02_MECANICA lleva cinco planos de montaje y el listado de "
        "equipos. 03_CANERIAS lleva seis planos de cañerías y de ubicación de soportes, el "
        "Cuadernillo de Isometrías (once isometrías en 31 hojas), el Cuadernillo de Soportes "
        "(21 páginas), la especificación técnica de cañerías de fabricación "
        "P22-ET-06-006-001 y los listados de líneas, materiales y válvulas. 04_ MODELO lleva "
        "el modelo 3D en Navisworks.")
    add_para_bold_lead(doc, "2. OBRAS CIVILES, 18 láminas y 2 especificaciones técnicas. ",
        "Trece láminas están en revisión 0 apta para construcción y cinco en revisión 1: "
        "P22-DWG-00-002-002 LAM1 y LAM4, P22-DWG-00-002-003 LAM1, y P22-DWG-00-002-007 LAM1 "
        "y LAM2. Las dos especificaciones, de Movimiento de Tierra y de Obras Civiles, van en "
        "revisión 1. Las memorias de cálculo de obras civiles no forman parte del paquete.")
    add_para_bold_lead(doc, "3. ET MONTAJE. ",
        "El anexo A12, de montaje electromecánico del estanque TK-06-001 y la bomba "
        "BH-06-001, con sus anexos. El anexo A13, de montaje de cañerías HDPE PE100 por "
        "electrofusión, cuyo anexo es el Listado de Materiales en revisión 1.")
    add_para(doc,
        "Los documentos van en PDF, los listados en Excel y el modelo en Navisworks. Los "
        "planos editables en formato DWG no se incluyen y se entregan a pedido. Para "
        "distribuir el paquete conviene comprimirlo, dado que algunas rutas internas del "
        "dossier mecánico son largas.")

    # ------------------------------------------------- 2. Doc. de referencia
    doc.add_heading("DOCUMENTOS DE REFERENCIA", level=1)
    add_simple_table(doc, [
        ("Código", "Documento", "Revisión"),
        ("P22-BL-06-000-001-0", "Bases de Licitación del Montaje Mecánico y Obras Civiles", "Contractual"),
        ("Anexo A9", "Formato de Presupuesto de Obras Civiles, Mecánica y Piping", "Contractual"),
        ("P22-LI-06-000-002-1", "Ingeniería vigente y cambios, planilla de control", "1"),
        ("P22-ET-06-007-001-0", "Especificación técnica de montaje electromecánico", "0"),
        ("P22-ET-06-007-002-0", "Especificación técnica de montaje de cañerías HDPE", "0"),
    ])

    # ------------------------------------------------------------ 3. Alcance
    doc.add_heading("QUÉ GOBIERNA EL ALCANCE Y QUÉ GOBIERNA LA CONSTRUCCIÓN", level=1)
    add_para(doc,
        "El alcance contratado se fija en el Formato de Presupuesto (Anexo A9), el cual no "
        "se modifica con esta entrega. Cada partida de dicho Formato define una obra y su "
        "forma de medición y pago.")
    add_para(doc,
        "La ingeniería vigente define cómo se construye ese alcance. Una revisión nueva de "
        "un plano cambia la forma de ejecutar una partida, y en algunos casos su cantidad "
        "de obra, pero no incorpora ni retira partidas.")
    add_para(doc,
        "De lo anterior se desprende el criterio con que se lee esta nota. Toda obra a "
        "ejecutar tiene su partida en el Formato, por lo que un documento de ingeniería sin "
        "partida asociada no constituye alcance contratado ni habilita cobro alguno, sin "
        "perjuicio de su valor como antecedente de coordinación.")

    # ------------------------------------------------------------ 4. Cambios
    doc.add_heading("CAMBIOS DE LA INGENIERÍA RESPECTO DE LA QUE SE COTIZÓ", level=1)

    doc.add_heading("La fundación del contenedor sube 250 milímetros", level=2)
    add_para(doc,
        "La cara superior de la fundación del contenedor del módulo pasa de la cota +6,050 "
        "a la cota +6,300, y el sello de fundación de la +5,150 a la +5,400. La geometría y "
        "la armadura se mantienen: diez pedestales de 1,00 por 1,00 metros dispuestos en "
        "cinco ejes separados 3,00 metros, unidos por vigas de 30 por 30 centímetros.")
    add_para(doc, "Con la fundación suben las cuatro cotas de conexión con el módulo.")
    add_simple_table(doc, [
        ("Punto de conexión", "Cota cotizada", "Cota vigente"),
        ("P8-001, entrada de salmuera al módulo", "+8,250", "+8,500"),
        ("P9-001, permeado", "+8,593", "+8,850"),
        ("P9-002, permeado fuera de especificación", "+8,593", "+8,850"),
        ("P9-003, salida de salmuera de rechazo", "+8,583", "+8,850"),
    ])
    add_para(doc,
        "Las conexiones con el módulo existente de 11 litros por segundo (tie-ins 1, 3 y 6) "
        "mantienen su cota +6,204. Rigen los planos P22-DWG-00-002-003 LAM1, "
        "P22-DWG-06-005-103 y P22-DWG-06-006-102, los tres en revisión 1.")

    doc.add_heading("La fundación del sistema CIP se rediseña", level=2)
    add_para(doc,
        "La fundación de los equipos del sistema CIP se reduce de 4,13 a 2,63 metros "
        "cúbicos de hormigón G25, con lo que el total de hormigón de la zona baja de 7,36 a "
        "5,80 metros cúbicos y la excavación de dicha zona de 5,01 a 1,60 metros cúbicos.")
    add_para(doc,
        "El rediseño incorpora una junta de dilatación entre elementos de fundación. Se "
        "ejecuta con poliestireno expandido de 2,5 centímetros de espesor, sello Sikaflex 1A "
        "y primer VP-215 aplicado en ambas paredes. La disposición y las dimensiones de los "
        "pernos de anclaje quedan definidas en el plano. Rige el P22-DWG-00-002-007 LAM1 en "
        "revisión 1, con su armadura en la LAM2, también en revisión 1.")

    doc.add_heading("El listado de materiales cambia accesorios y material de brida", level=2)
    add_para(doc,
        "El metraje de cañería no cambia y se mantiene en 335 metros, y tampoco cambian "
        "las cantidades de codos, cuplas, tee, reducciones, espárragos y stub end. Los "
        "accesorios sí cambian, según el listado P22-LI-06-006-102 en revisión 1.")
    add_para(doc,
        "Se retiran los dos accesorios de PVC-U, un codo de 90 grados de 4 pulgadas y una "
        "tee reductora de 4 por 2 pulgadas, por lo que la instalación queda íntegramente en "
        "HDPE.")
    add_para(doc,
        "El buje de reducción en Súper Dúplex (UNS S32750) sube de 2 a 5 unidades y el "
        "spigot saddle with cutter de 4 por 1 pulgada, de 2 a 5. Se incorporan tres uniones "
        "adaptador PE100 por Súper Dúplex de 1 pulgada y se retira el back-up flange de 4 "
        "pulgadas. Las empaquetaduras bajan de 45 a 42 unidades.")
    add_para(doc,
        "La brida no cambia de tipo. En las dos revisiones es la misma pieza, un flange "
        "suelto de junta solapada montado sobre stub end (FLANGE LJ, de Lap Joint), con "
        "perforaciones según ASME B16.5 clase 150. Lo que la revisión 1 del listado "
        "incorpora es su material, acero galvanizado por inmersión, y la cantidad de 4 "
        "pulgadas pasa de 22 a 23 unidades. Dado que las isometrías no declaran el material "
        "de la brida, para ese dato rige el listado.")
    add_para(doc,
        "El contratista debe verificar este listado antes de emitir las órdenes de compra "
        "de accesorios y bridas.")

    doc.add_heading("El cuadernillo de isometrías cambia poco y se renumeró", level=2)
    add_para(doc,
        "Siete de las once isometrías son idénticas a las de la revisión con la que se "
        "cotizó. Cambian de revisión únicamente P22-DWG-06-006-005, P22-DWG-06-006-008, "
        "P22-DWG-06-006-009 y P22-DWG-06-006-011, que aportan tres hojas nuevas entre las "
        "tres primeras y la última.")
    add_para(doc,
        "El cotejo contra el juego anterior debe hacerse por contenido y no por número de "
        "hoja. En P22-DWG-06-006-011 entra una hoja nueva en la posición H.2 y las seis "
        "siguientes se desplazan, de modo que la H.2 anterior es ahora la H.3 y la H.7 es "
        "la H.8. En P22-DWG-06-006-008 la antigua H.4 pasa a ser la H.5.")

    doc.add_heading("Documentos que cambian de revisión", level=2)
    add_para(doc,
        "Once documentos del dossier mecánico están en una revisión posterior a la que "
        "sirvió para cotizar. El resto se mantiene en la revisión con la que se cotizó.")
    add_simple_table(doc, [
        ("Código", "Revisión", "Documento"),
        ("P22-DWG-06-005-103", "1", "Plano de montaje del módulo"),
        ("P22-DWG-06-006-101", "1", "Cañerías de interconexiones, planta"),
        ("P22-DWG-06-006-102", "1", "Cañerías de interconexiones, cortes y detalles"),
        ("P22-DWG-06-006-103", "1", "Cañerías TK y bomba, planta"),
        ("P22-DWG-06-006-104", "1", "Cañerías TK y bomba, cortes y detalles"),
        ("P22-DWG-06-006-005", "2", "Isometría SA-HDPE-DN110-PN10-005, cinco hojas"),
        ("P22-DWG-06-006-008", "1", "Isometría PE-HDPE-DN90-PN10-001, cinco hojas"),
        ("P22-DWG-06-006-009", "1", "Isometría PE-HDPE-DN90-PN10-003, dos hojas"),
        ("P22-DWG-06-006-011", "2", "Isometría SA-HDPE-DN110-PN10-007, ocho hojas"),
        ("P22-LI-06-006-102", "1", "Listado de materiales de cañerías"),
        ("P22-LI-06-008-101", "1", "Listado de instrumentos"),
    ])
    add_para(doc,
        "En obras civiles cambian de revisión las cinco láminas ya indicadas y las dos "
        "especificaciones técnicas.")

    # ------------------------------------------------------------ 5. Partidas
    doc.add_heading("EFECTO SOBRE LAS PARTIDAS DEL FORMATO DE PRESUPUESTO", level=1)
    add_para(doc,
        "Dos partidas del Capítulo 4 cambian su cantidad de obra debido a los cambios ya "
        "descritos. Ambas se miden por unidad de obra, por lo que se pagan según la "
        "cubicación realmente ejecutada y verificada en terreno por la inspección técnica "
        "de obra (ITO).")
    add_simple_table(doc, [
        ("Partida", "Cantidad cotizada", "Cantidad vigente"),
        ("4.2 Fundación sistema CIP (F2b)", "7,36 m³", "5,80 m³"),
        ("4.6 Excavación común en fundaciones y zanjas de drenaje", "115,10 m³", "111,70 m³"),
    ])
    add_para(doc,
        "Las demás partidas del Capítulo 4 mantienen su cantidad. Las del Capítulo 1 tampoco "
        "cambian. Los 67 soportes de los once tipos del cuadernillo P22-DWG-06-006-107 se "
        "mantienen, dado que dicho cuadernillo y los planos de ubicación de soportes "
        "P22-DWG-06-006-105 y P22-DWG-06-006-106 conservan su revisión 0.")
    add_para(doc,
        "En el Corte D del plano P22-DWG-06-006-102 deja de aparecer la válvula VM-06-010, "
        "la cual la revisión anterior rotulaba como proyectada y que no tiene partida en el "
        "Formato.")
    add_para(doc,
        "Se hace presente que el Formato de Presupuesto repite dos códigos de partida. "
        "Existen dos partidas numeradas 4.3, correspondientes a la Fundación de la cubierta "
        "metálica del sistema CIP (cobertizo) y a la Fundación dinámica bomba BH-06-001 "
        "(F3), y dos numeradas 4.7, correspondientes a los Dados de hormigón G25 para "
        "pedestales de soportes a piso y al Relleno compactado con material seleccionado y "
        "base estabilizada.")
    add_para(doc,
        "Debido a lo anterior, toda referencia a una partida debe consignar su número y su "
        "nombre completo, tanto en esta nota como en los estados de pago.")

    # ------------------------------------------------------------ 6. Cubierta
    doc.add_heading("LA CUBIERTA METÁLICA DEL SISTEMA CIP", level=1)
    add_para(doc,
        "La fundación de la cubierta se ejecuta íntegra. Corresponde a la partida 4.3 "
        "Fundación de la cubierta metálica del sistema CIP (cobertizo), cotizada en 2,38 "
        "metros cúbicos, la cual incluye los 24 pernos de anclaje F-1554 de 3/4 de pulgada "
        "preinstalados y su protección anticorrosiva interina hasta la recepción de la obra. "
        "Rige el plano P22-DWG-00-002-007 LAM3 en revisión 0.")
    add_para(doc,
        "La estructura metálica no tiene partida en el Formato y no forma parte del alcance "
        "contratado. Aguas Antofagasta la ejecutará en una etapa posterior, sobre la "
        "fundación y los pernos que se dejan preinstalados en esta obra.")
    add_para(doc,
        "Debido a lo anterior, se requiere especial cuidado en la verticalidad, el nivel y "
        "la posición de los 24 pernos, según el plano, y en mantener su protección hasta la "
        "recepción. Un perno fuera de tolerancia obliga a intervenir la fundación en la "
        "etapa posterior.")

    # ------------------------------------------------------------ 7. Vigencia
    doc.add_heading("VIGENCIA DE LA DOCUMENTACIÓN", level=1)
    add_para(doc,
        "Para cada código y lámina rige la revisión que este paquete entrega, por lo que "
        "cualquier revisión anterior del mismo documento, cualquiera sea la vía por la que "
        "el contratista la haya recibido, queda reemplazada por la de esta entrega.")
    add_para(doc,
        "La hoja Vigencia de la planilla P22-LI-06-000-002-1 lista los 54 documentos, uno "
        "por fila, con la revisión que rige y el dossier donde se encuentra. Ante cualquier "
        "duda de vigencia prevalece dicha hoja.")
    add_para(doc,
        "Se exceptúa el P&ID de alimentación P22-DWG-06-009-102, cuya revisión 1 el "
        "proyectista emitió solo en formato editable. El paquete mantiene la revisión 0 y "
        "la revisión 1 se remitirá en cuanto se reciba el ploteo.")

    # ------------------------------------------------------------ 8. Acuse
    doc.add_heading("ACUSE DE RECIBO", level=1)
    add_para(doc,
        "El contratista debe acusar recibo de esta nota y del paquete a más tardar el "
        "viernes 11 de septiembre de 2026.")
    add_para(doc,
        "En dicho acuse debe confirmar que construirá según la ingeniería aquí declarada e "
        "indicar si detecta alguna interferencia con obras ya ejecutadas, con materiales ya "
        "adquiridos o con la programación vigente, en cuyo caso Aguas Antofagasta la "
        "resolverá antes de que la partida afectada entre en ejecución.")

    # ------------------------------------------------------------ 9. Historial
    doc.add_heading("HISTORIAL DEL DOCUMENTO", level=1)
    add_simple_table(doc, [
        ("Revisión", "Fecha", "Descripción"),
        ("0", "04-09-2026", "Emisión original"),
    ])

    doc.core_properties.author = "Luis Rivera Gonzalez"
    doc.core_properties.company = "Aguas Antofagasta"
    doc.core_properties.comments = (
        "Nota tecnica de ingenieria vigente para construccion, montaje mecanico y obras "
        "civiles, Planta Desaladora Taltal")
    traducir_mes_portada(doc)
    fijar_idioma_documento(doc)
    doc.save(OUTPUT)
    print(f"Documento generado: {os.path.basename(OUTPUT)}")


if __name__ == "__main__":
    crear_documento()
