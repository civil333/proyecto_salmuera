#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo interno a Victor Gutierrez (Jefe Depto. Proyectos Desalacion, ADASA) con
el estado de las jornadas de inspeccion de Bureau Veritas en el taller de Penang:
la de hoy viernes 7 de agosto y las dos del jueves 13 y viernes 14.

Criterio de redaccion:
  - Correo INTERNO, 100% espanol (CLAUDE.md Seccion 3.4). Idioma del Word fijado
    en es-CL como ultima operacion antes de guardar.
  - Ejecutivo y directo, sin proponer reunion (memoria feedback_correos_ejecutivos).
  - Una tabla compacta con el alcance de cada jornada + bullets con los cuatro
    puntos abiertos. Una pagina.
  - Sin el simbolo de seccion: "seccion 3.2", "Clausula 37" deletreado
    (CLAUDE.md Secciones 2.4 y 2.5).
  - Document() directo, sin template ADASA. Metadatos limpios con comments=
    explicito (memoria feedback_metadatos_correos_python_docx).

Estado: BORRADOR, pendiente de revision y envio.
"""
import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-07_BV-Jornadas-Inspeccion.docx")
CONTACTO = "Luis Rivera González"
LANG = "es-CL"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
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


def _set_lang(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    """Fija es-CL en el estilo Normal y en todos los runs, incluidos los de tabla."""
    try:
        _set_lang(doc.styles["Normal"].element.get_or_add_rPr(), lang)
    except KeyError:
        pass
    for para in doc.paragraphs:
        for run in para.runs:
            _set_lang(run._element.get_or_add_rPr(), lang)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        _set_lang(run._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11):
    para = doc.add_paragraph(text)
    aplicar_arial(para, size)
    return para


def add_segments(doc, segs, size=11, indent=None):
    para = doc.add_paragraph()
    if indent is not None:
        para.paragraph_format.left_indent = Inches(indent)
    for text, bold in segs:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def add_bullet(doc, segs, size=11):
    return add_segments(doc, [("• ", False)] + list(segs), size=size, indent=0.25)


def blank(doc):
    doc.add_paragraph()


def add_table_with_header(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = header
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True
    for i, row_data in enumerate(rows, start=1):
        for j, value in enumerate(row_data):
            table.rows[i].cells[j].text = str(value)
    if widths:
        for row in table.rows:
            for j, width in enumerate(widths):
                row.cells[j].width = Inches(width)
    aplicar_arial_table(table, size=10)
    return table


# ---------------------------------------------------------------------------
# Cuerpo del correo
# ---------------------------------------------------------------------------
def crear_correo():
    doc = Document()
    fmt = doc.styles["Normal"].paragraph_format
    fmt.space_after = Pt(0)
    fmt.line_spacing = 1.0
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ---------------------------------------------------------------- header
    fields = [
        ("Fecha:", "7 de agosto de 2026"),
        ("De:", CONTACTO + " — Departamento de Ingeniería y Optimización, ADASA"),
        ("Para:", "Víctor Gutiérrez Aqueveque — Jefe Depto. Proyectos Desalación, ADASA"),
        ("Asunto:", "PD Taltal — Inspección Bureau Veritas en Penang: jornada de hoy "
                    "y jornadas del 13 y 14 de agosto"),
        ("Ref:", "BAE 12803 Cláusula 37 / Nota Técnica P22-NT-09-000-002-0 / "
                 "ITP P22-BA-09-000-004 Rev 0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        run = para.add_run(label)
        run.bold = True
        para.add_run(" " + value)
        aplicar_arial(para)

    blank(doc)
    add_para(doc, "Estimado Víctor:")
    blank(doc)

    add_para(
        doc,
        "Bureau Veritas está ejecutando hoy la segunda jornada de vigilancia en el "
        "taller de Penang, y BW Water notificó dos jornadas más para el jueves 13 y "
        "el viernes 14 de agosto. Te resumo el alcance de cada una y los cuatro "
        "puntos que quedan abiertos, uno de los cuales es acción nuestra.",
    )
    blank(doc)

    # ------------------------------------------------------- tabla de alcance
    add_segments(doc, [("Alcance declarado por el taller", True)])
    blank(doc)
    add_table_with_header(
        doc,
        headers=["Jornada", "Fecha", "Actividades de inspección"],
        rows=[
            (
                "Segunda",
                "Viernes 7 de agosto\n09:00 a 17:00",
                "Fabricación de los spools de super dúplex; ensayo de líquidos "
                "penetrantes de raíz y capping de la soldadura; fabricación del "
                "marco del skid; revisión de las especificaciones de soldadura y "
                "de la calificación de los soldadores.",
            ),
            (
                "Tercera y cuarta",
                "Jueves 13 y viernes 14 de agosto\n09:00 a 17:00",
                "Ensayo de presión de la tubería de alta (punto de detención, "
                "135 bar); inspección de la preparación de superficie para pintura.",
            ),
        ],
        widths=[1.1, 1.6, 4.3],
    )
    blank(doc)

    add_para(
        doc,
        "La jornada de hoy cierra el punto que quedó pendiente de la primera visita "
        "del 28 de julio: la revisión de las especificaciones de soldadura y de la "
        "calificación de los soldadores, que el taller movió a esta fecha. Los "
        "documentos de referencia que acompañan la solicitud son esta vez las "
        "revisiones vigentes aprobadas, verificadas por hash.",
    )
    blank(doc)

    # ------------------------------------------------------- puntos abiertos
    add_segments(doc, [("Puntos abiertos", True)])
    blank(doc)

    add_bullet(doc, [
        ("El alcance del 13 y 14 quedó corto. ", True),
        ("El formulario de solicitud declara únicamente el ensayo de alta presión. "
         "La minuta del 4 de agosto ofrecía también el de baja presión, y el del "
         "RO Vessel no aparece en ninguna de las dos versiones. La Nota Técnica "
         "P22-NT-09-000-002-0, sección 3.2, exige los tres: baja a 7,5 bar como "
         "punto de testificación, alta a 135 bar y RO Vessel como puntos de "
         "detención. Los dos que faltan hay que reprogramarlos o quedan sin "
         "testificar.", False),
    ])
    blank(doc)

    add_bullet(doc, [
        ("Acción nuestra antes del 14. ", True),
        ("El inspector tiene el procedimiento de pintura en la revisión B, "
         "superada. Su formulario de registro fija el perfil de anclaje en 40 a "
         "75 micrones, mientras el criterio de aceptación de la revisión 0 lo deja "
         "en 50 a 80. Con esa copia puede firmar como conforme un perfil bajo el "
         "mínimo. La revisión 0 ya llegó con el submittal 25007-0071 y corrige el "
         "valor en los dos lugares; corresponde hacérsela llegar a Bureau Veritas "
         "antes de la inspección de pintura.", False),
    ])
    blank(doc)

    add_bullet(doc, [
        ("El aviso fue de ocho días. ", True),
        ("La Cláusula 37 de las BAE exige treinta días de antelación para "
         "inspección con tercero en suministros internacionales. Es la segunda "
         "notificación consecutiva fuera de plazo, después de los nueve días de la "
         "jornada de hoy y los cuatro de la primera visita. El taller propuso por "
         "escrito reemplazar el plazo contractual por uno de tres a cinco días; "
         "ADASA no lo ha aceptado, y conviene dejar constancia de que aceptar cada "
         "jornada puntual no constituye precedente.", False),
    ])
    blank(doc)

    add_bullet(doc, [
        ("Falta definir dónde se registra el ensayo hidrostático. ", True),
        ("El procedimiento remite a un formulario de reporte de presión que el "
         "paquete entregado ya no contiene. El ensayo es punto de detención y "
         "encadena con la liberación para despacho, de la que depende el 40 % del "
         "pago. Se pidió la aclaración en el correo del 6 de agosto y sigue sin "
         "respuesta.", False),
    ])
    blank(doc)

    add_para(
        doc,
        "El informe de Bureau Veritas de la jornada de hoy debería llegar dentro de "
        "los próximos días, igual que el de la primera visita, que cerró sin no "
        "conformidades con 31 lecturas de identificación de material conformes.",
    )
    blank(doc)

    add_para(doc, "Quedo atento a tus comentarios.")
    blank(doc)
    add_para(doc, "Saludos cordiales,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Departamento de Ingeniería y Optimización (DIO)",
        "ADASA — Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line)

    # ------------------------------------------- idioma y metadatos, al final
    fijar_idioma_documento(doc, LANG)
    docx_metadata.apply_core_properties(
        doc,
        title="PD Taltal - Jornadas de inspeccion Bureau Veritas 7 y 13-14 de agosto",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Estado de las jornadas de inspeccion de taller en Penang",
        comments="Correo interno a Victor Gutierrez - Proyecto Taltal BAE 12803.",
        language=LANG,
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas de Antofagasta S.A.")
    print("Correo generado: " + OUTPUT_FILE)
    print("Idioma del documento: " + LANG)


if __name__ == "__main__":
    crear_correo()
