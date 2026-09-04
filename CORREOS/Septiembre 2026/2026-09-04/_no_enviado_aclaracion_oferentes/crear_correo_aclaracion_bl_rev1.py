#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carta de aclaracion a los oferentes de la licitacion de Montaje Mecanico y Obras
Civiles del Modulo de Segunda Etapa de Salmuera, Planta Desaladora Taltal.

Comunica la emision de la revision 1 del paquete P22-BL-06-000-001 y remite la
planilla de control de cambios.

Idioma del documento fijado en es-CL para que Word corrija en espanol.
"""
import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-04_Aclaracion-N1-Licitacion-Montaje-Taltal.docx")
CONTACTO = "Luis Rivera"
LANG = "es-CL"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def aplicar_arial_table(table, size=10):
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)


def _set_lang_in_rPr(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
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


def add_table_with_header(doc, headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(headers):
        c = t.rows[0].cells[j]
        c.text = h
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
    for i, fila in enumerate(rows, start=1):
        for j, v in enumerate(fila):
            t.rows[i].cells[j].text = str(v)
    aplicar_arial_table(t, size=10)
    return t


def parrafo(doc, texto, size=11, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.bold = bold
    aplicar_arial(p, size)
    return p


def crear_correo():
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Inches(0.8)

    campos = [
        ("Fecha:", "4 de septiembre de 2026"),
        ("De:", f"{CONTACTO} — Dirección de Ingeniería y Obras, Aguas Antofagasta S.A."),
        ("Para:", "[COMPLETAR: oferentes invitados a la licitación]"),
        ("CC:", "Víctor Gutiérrez (ADASA)"),
        ("Asunto:", "PD Taltal — Aclaración N°1: se emite la revisión 1 del paquete de licitación de Montaje Mecánico y Obras Civiles"),
        ("Ref:", "P22-BL-06-000-001-1 / BAE 12803"),
    ]
    for etiqueta, valor in campos:
        p = doc.add_paragraph()
        r1 = p.add_run(f"{etiqueta} ")
        r1.bold = True
        p.add_run(valor)
        aplicar_arial(p, 11)

    doc.add_paragraph()
    parrafo(doc, "Estimados señores:")
    doc.add_paragraph()

    parrafo(doc,
        "La ingeniería de detalle que respalda esta licitación se actualizó después de la distribución del "
        "paquete. Aguas Antofagasta emite en consecuencia la revisión 1 de las Bases de Licitación "
        "P22-BL-06-000-001 y del paquete completo que las acompaña. Esta revisión reemplaza íntegramente a "
        "la revisión 0 del 25 de junio de 2026.")
    doc.add_paragraph()

    parrafo(doc, "Lo que cambia", bold=True)
    parrafo(doc,
        "El punto de fondo es que la fundación del contenedor del módulo sube 250 milímetros: su cara "
        "superior pasa de la cota +6,050 a la cota +6,300. Con ella suben las cuatro cotas de conexión con "
        "el módulo, que la Sección 4.3 de las Bases publica actualizadas. Las conexiones con el módulo "
        "existente de 11 litros por segundo no cambian.")
    doc.add_paragraph()

    add_table_with_header(doc,
        ["Punto de conexión", "Cota en la revisión 0", "Cota en la revisión 1"],
        [["P8-001, entrada de salmuera al módulo", "+8,250", "+8,500"],
         ["P9-001, permeado", "+8,593", "+8,850"],
         ["P9-002, permeado fuera de especificación", "+8,593", "+8,850"],
         ["P9-003, salida de salmuera de rechazo", "+8,583", "+8,850"]])
    doc.add_paragraph()

    parrafo(doc,
        "En el Capítulo 4 del Formato de Licitación cambian dos cantidades. La fundación del sistema CIP "
        "baja de 7,36 a 5,80 metros cúbicos de hormigón G25, porque la ingeniería redujo la fundación de "
        "los equipos e incorporó una junta de dilatación entre elementos. La excavación baja de 115,1 a "
        "111,7 metros cúbicos. Las otras doce partidas del capítulo mantienen su cantidad, y el Capítulo 1 "
        "no cambia: las líneas se siguen cotizando de forma global y los soportes por unidad.")
    doc.add_paragraph()

    parrafo(doc, "Lo que se agrega al paquete", bold=True)
    parrafo(doc,
        "El dossier de ingeniería de detalle mecánica se entrega completo. Se incorporan el Cuadernillo de "
        "Soportes, que es el Anexo A3 de las Bases, el Cuadernillo de Isometrías con sus once isometrías en "
        "treinta y una hojas, el diagrama de flujo, los cuatro diagramas de proceso e instrumentación y "
        "seis planos de cañerías y de ubicación de soportes. Son los documentos con los que las Bases piden "
        "cotizar por isometría y no acompañaban a la revisión anterior.")
    doc.add_paragraph()

    parrafo(doc, "El Formato de Licitación se reemplaza", bold=True)
    parrafo(doc,
        "La planilla de oferta económica se entrega nuevamente, con la columna de precio unitario en blanco "
        "y las fórmulas de total, costo directo, gastos generales, utilidades y total general activas. Los "
        "valores son netos y la planilla no incorpora el impuesto al valor agregado. Las ofertas deben "
        "presentarse sobre esta planilla y no sobre la que acompañó a la revisión anterior.")
    doc.add_paragraph()

    parrafo(doc, "Cómo leer los cambios", bold=True)
    parrafo(doc,
        "El paquete incorpora una carpeta nueva, 0. CONTROL DE CAMBIOS, con la planilla "
        "P22-LI-06-000-002-1. Sus cinco hojas indican, documento por documento, qué cambió de revisión, qué "
        "cambió dentro de cada documento, si el cambio afecta a la cotización y a qué partida del Formato "
        "afecta. Es el punto de entrada recomendado para revisar esta revisión.")
    doc.add_paragraph()

    parrafo(doc, "Plazo de presentación de ofertas", bold=True)
    parrafo(doc,
        "[COMPLETAR: confirmar si el plazo de presentación de ofertas se mantiene o se extiende, y la fecha.]")
    doc.add_paragraph()

    parrafo(doc,
        "Las consultas sobre esta aclaración se reciben por esta misma vía. Quedamos atentos.")
    doc.add_paragraph()
    parrafo(doc, "Saludos cordiales,")
    doc.add_paragraph()
    parrafo(doc, CONTACTO)
    parrafo(doc, "Dirección de Ingeniería y Obras")
    parrafo(doc, "Aguas Antofagasta S.A. — Grupo EPM")

    doc.core_properties.author = "Luis Rivera Gonzalez"
    doc.core_properties.company = "Aguas Antofagasta"
    doc.core_properties.comments = "Aclaracion N1 de la licitacion de montaje, revision 1 del paquete"
    fijar_idioma_documento(doc)
    doc.save(OUTPUT_FILE)
    print(f"OK: {os.path.basename(OUTPUT_FILE)}")


if __name__ == "__main__":
    crear_correo()
