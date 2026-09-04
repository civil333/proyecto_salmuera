#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> Bureau Veritas Chile del 31-Ago-2026.

CADENA PROPIA: RE: 25007 TALTAL - Request to witness inspection 006, que es la del
reporte y por donde llego el set completo el 31-Ago a las 14:47. Separada de la
cadena tecnica con el fabricante.

REGLA DURA: no se nombra al fabricante. Se escribe "el taller". Barrido pre-emision:
grep -i "bw.water" -> 0. La municion es la oferta 600049 Rev.3 contratada por la
Orden de Compra 836492 y la Nota Tecnica de designacion, no la BAE ni la ET, que
obligan al proveedor y no al tercero inspector.

EL EQUILIBRIO DEL CORREO: cuatro de los seis puntos del 21-Ago se cerraron y eso se
dice primero, porque es cierto y verificado documento por documento. Queda uno,
la No Conformidad, y la reemision lo dejo CONTRADICTORIO: los dos informes marcan
la casilla "Not Satisfactory (NCR raised during the inspection)" y tres lineas mas
abajo marcan "Open Non Conformities: No", con la seccion G en N/A. Ese es el
argumento, y no se puede refutar porque sale del propio formulario reemitido.

SEGUNDO PUNTO: el BVM-IR007 del 24-Ago repite el defecto exacto que se objeto el
21-Ago sobre el BVM-IR005. Marca Satisfactorio sin comentarios mientras su resumen
declara el resultado no satisfactorio.

TERCERO: la fila de la visita 4 del cuadro resumen declara ensayo de alta
satisfactorio; el BVM-IR004 dice que ese ensayo no pudo ejecutarse. Y el control de
revisiones: las dos reemisiones conservan Revision N 0 en su campo de revision.

Se cierra pidiendo la movilizacion del inspector para el 2, 3 y 4 de septiembre, que
es lo operativo y urgente, y reconociendo el desempeno en terreno, que no esta en
cuestion.

ADJUNTO: Anexo_Registro_Inspecciones_IR001_IR009.docx, generado por
crear_anexo_registro_inspecciones.py en esta misma carpeta.

Espanol de Chile. Document() directo, sin template ADASA. Estado: BORRADOR.
"""
import os
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-31_BV-Set-Informes-IR001-IR009.docx")
CONTACTO = "Luis Rivera González"
LANG = "es-CL"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def _set_lang(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    for p in doc.paragraphs:
        for r in p.runs:
            _set_lang(r._element.get_or_add_rPr(), lang)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        _set_lang(r._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11, space=6):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(space)
    aplicar_arial(p, size)
    return p


def add_segments(doc, segs, size=11, space=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space)
    for text, bold in segs:
        r = p.add_run(text)
        r.bold = bold
        r.font.name = "Arial"
        r.font.size = Pt(size)
    return p


def add_bullet_lead(doc, lead, rest, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    p.paragraph_format.space_after = Pt(3)
    r0 = p.add_run("•  " + lead)
    r0.bold = True
    r0.font.name = "Arial"
    r0.font.size = Pt(size)
    r1 = p.add_run(rest)
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    return p


def espaciador(doc):
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def crear_correo():
    doc = Document()
    fmt = doc.styles["Normal"].paragraph_format
    fmt.space_after = Pt(6)
    fmt.line_spacing = 1.0
    for s in doc.sections:
        s.top_margin = Inches(0.6)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    fields = [
        ("Fecha:", "31 de agosto de 2026"),
        ("De:", CONTACTO + " - Líder de Ingeniería de Infraestructura (ADASA)"),
        ("Para:", "Carlo Montecinos - Bureau Veritas Chile"),
        ("CC:", "Jaime Martínez - Bureau Veritas; Victor Gutierrez - ADASA"),
        ("Asunto:", "RE: 25007 TALTAL - Request to witness inspection 006 - "
                    "registro consolidado de inspecciones"),
        ("Adjunto:", "Anexo — Registro de inspecciones de taller BVM-IR001 a BVM-IR009"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    espaciador(doc)

    add_para(doc, "Estimado Carlo:")

    # 1. ACUSE Y RECONOCIMIENTO. Primero porque es verificado y es la mitad del asunto.
    add_segments(doc, [
        ("Recibimos el set completo y cuatro de los seis puntos del 21 de agosto "
         "quedaron cerrados.", True),
        (" Los dos informes se reemitieron con la presión de la Line List y pasaron a No "
         "Satisfactorio; el P&ID (P22-DWG-09-009-002 Rev D) y la Line List "
         "(P22-LI-09-009-003 Rev 0) entraron a la documentación de referencia; y desde "
         "el BVM-IR008 el registro fotográfico incorpora la marca de identificación del "
         "carrete.", False),
    ])

    # 2. EL PUNTO ABIERTO, con el argumento sacado del propio formulario reemitido.
    add_segments(doc, [
        ("Queda la No Conformidad, y la reemisión la dejó contradictoria.", True),
        (" Los dos informes marcan No Satisfactorio, que el formulario define como No "
         "Conformidad levantada durante la inspección, y tres líneas más abajo marcan No "
         "en la casilla de No Conformidades abiertas, con la sección G en N/A. Sin "
         "conciliarlas, el dossier de fabricación no llevará registro de la desviación "
         "de los tres ensayos, que la sección 3.2 de tu oferta obliga a informar en la "
         "misma visita.", False),
    ])

    # 3. EL IR007, mismo defecto tres dias despues del reclamo.
    add_segments(doc, [
        ("El BVM-IR007 del 24 de agosto repite el defecto:", True),
        (" marca Satisfactorio sin comentarios mientras su resumen declara el resultado "
         "no satisfactorio, sobre un hallazgo real, que la parte inferior del marco no "
         "alcanza los 355 micrones exigidos.", False),
    ])

    add_segments(doc, [
        ("Lo que te pedimos:", True),
    ], space=3)
    add_bullet_lead(
        doc, "Al martes 1 de septiembre",
        ": confirmación de la movilización del inspector para el miércoles 2, jueves 3 y "
        "viernes 4, y copia a ADASA de la solicitud de atestiguamiento de esos tres días.")
    add_bullet_lead(
        doc, "Al viernes 4 de septiembre",
        ": la No Conformidad referenciada en la sección G, la reemisión del BVM-IR007, y "
        "la corrección de la fila de la visita 4 de tu cuadro, que declara ensayo de alta "
        "satisfactorio cuando el BVM-IR004 dice que no pudo ejecutarse.")
    add_bullet_lead(
        doc, "En la próxima emisión",
        ": el campo de revisión con el número que corresponde. Los dos informes "
        "reemitidos conservan Revisión N° 0.")
    espaciador(doc)

    # 4. EL ANEXO Y EL CONTEXTO OPERATIVO, en una sola frase.
    add_segments(doc, [
        ("Adjunto el registro consolidado de las nueve jornadas", True),
        (", con el detalle de cada punto. De las once líneas de super dúplex, una tiene "
         "ensayo conforme, tres deben repetirse y siete no se han ensayado: las tres "
         "jornadas de esta semana son las que empiezan a descargar el Punto de Detención "
         "de la fila 5.2 del Plan de Inspección y Ensayos (P22-BA-09-000-004 Rev 0).",
         False),
    ])

    # 5. CIERRE EN EL TRABAJO CONJUNTO.
    add_segments(doc, [
        ("El desempeño en terreno no está en cuestión.", True),
        (" El inspector asistió a las nueve jornadas, firmó los registros y revisó los "
         "certificados de calibración. Quedamos disponibles para responder consultas de "
         "ingeniería el mismo día.", False),
    ])

    add_para(doc, "Saludos cordiales,", space=0)
    espaciador(doc)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in [
        "Líder de Ingeniería de Infraestructura - ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line, space=0)

    fijar_idioma_documento(doc, LANG)

    docx_metadata.apply_core_properties(
        doc,
        title="Taltal - registro consolidado de inspecciones de taller",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Módulo RO Segunda Etapa - Taltal - set de informes BVM-IR001 a "
                "BVM-IR009 y puntos abiertos",
        comments="Aguas de Antofagasta S.A.",
        language="es-CL",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas de Antofagasta S.A.")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
