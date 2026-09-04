#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo conjunto ADASA -> BW Water + Bureau Veritas por el incumplimiento del
aviso de la inspeccion del 14 de agosto de 2026 en Penang y su reprogramacion.

Reply-all al hilo del Request to witness inspection 004. Cadena de las jornadas,
SEPARADA de la de transmittals.

EL PUNTO SUSTANTIVO NO ES EL DESPERFECTO, ES LA HORA DEL AVISO. El correo de
BW Water entro el viernes 14 a las 05:15 de Chile, que en Penang son las 17:15:
la ventana de 09:00 a 17:00 ya estaba cerrada y la jornada, perdida. Un
desperfecto tecnico ocurre; enterarse despues es lo que se objeta.

TRES COSAS QUE NO SE AFIRMAN, a proposito:
  - No se declara que paso cada dia. Se pide a BW Water declararlo por escrito
    y a Bureau Veritas confirmar si asistio los dos dias. No hay evidencia de
    asistencia ni de consumo de jornada.
  - No se exigen los 30 dias de la Clausula 37: pedirlos junto con una
    reprogramacion para el lunes seria contradictorio. Se citan para mostrar la
    flexibilidad ya concedida.
  - No se menciona la tarifa de Bureau Veritas ni el saldo de jornadas
    contratadas. Es informacion interna y el inspector esta entre los
    destinatarios.

EL ENSAYO DE ALTA es Punto de Detencion de la fila 5.2 del ITP
P22-BA-09-000-004 Rev 0, con informe de grafico presion contra tiempo. Una
inspeccion visual y dimensional de spools (filas 3.2 y 3.4 del mismo plan) no
lo libera.

EL REQUEST 004, verificado por render PNG a 200 dpi: resultado, comentarios y
los tres bloques de firma vacios; sin paquete de prueba; sin procedimiento ni
revision. Repite las dos actividades del 003 y vuelve a cubrir dos dias en una
sola casilla de fecha y un solo bloque de resultado, que es lo que ADASA pidio
corregir el 12-Ago.

Excepcion de correo conjunto: se nombra a BW Water aunque Bureau Veritas este
entre los destinatarios.

Ingles. Document() directo, sin template ADASA. Estado: ENVIADO el 14-Ago-2026.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-14_BV-Inspection-004-Rescheduling.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"


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


def fijar_idioma(doc, lang=LANG):
    for p in doc.paragraphs:
        for r in p.runs:
            _set_lang(r._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11):
    p = doc.add_paragraph(text)
    aplicar_arial(p, size)
    return p


def add_segments(doc, segs, size=11):
    p = doc.add_paragraph()
    for text, bold in segs:
        r = p.add_run(text)
        r.bold = bold
        r.font.name = "Arial"
        r.font.size = Pt(size)
    return p


def add_bullet_lead(doc, lead, rest, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    r0 = p.add_run("•  " + lead)
    r0.bold = True
    r0.font.name = "Arial"
    r0.font.size = Pt(size)
    r1 = p.add_run(rest)
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    return p


def blank(doc):
    doc.add_paragraph()


def crear_correo():
    doc = Document()
    fmt = doc.styles["Normal"].paragraph_format
    fmt.space_after = Pt(0)
    fmt.line_spacing = 1.0
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    fields = [
        ("Date:", "August 14, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Mohd Adnin Bin Zulkaflee, Muhammad Fadhil Bin Abdul Wahid - BW Water; "
                "Ahmad Hazwan, Carlo Montecinos, Wan Mohd Adli W Yahya, Emylia Rosli - "
                "Bureau Veritas"),
        ("CC:", "Eduardo Yamauchi, Stephane Gehant, Magdier Arias, Lokman Hakim Bin Mat - "
                "BW Water; Victor Gutierrez, Jorge Guevara, Ronald Pellejero - ADASA"),
        ("Subject:", "RE: 25007 TALTAL - Request to witness inspection 004 - rescheduling"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Adnin,")
    blank(doc)

    add_segments(doc, [
        ("We acknowledge the technical failure that prevented the high-pressure piping "
         "pressure test from being carried out. The problem for ADASA is ", False),
        ("the timing of the notice", True),
        (": your message reached us at 5.15 pm Penang time, once the 9.00 am to 5.00 pm "
         "window had closed and the day had already been lost.", False),
    ])
    blank(doc)

    add_para(doc,
             "ADASA has accepted notices at four and at eight days against the thirty days "
             "of advance notice required by Clause 37, so that fabrication is not held up. "
             "That flexibility does not extend to being told after the fact. From now on, "
             "any cancellation, deferral or change of scope is to be notified in writing to "
             "ADASA and to Bureau Veritas before the window opens.")
    blank(doc)

    add_segments(doc, [
        ("The high-pressure hydrostatic test is a ", False),
        ("hold point under row 5.2 of the Inspection and Test Plan", True),
        (" (P22-BA-09-000-004), and a visual and dimensional inspection of piping spools "
         "does not discharge it. Please state in writing what was executed on Thursday 13 "
         "and what was executed on Friday 14, with the record of each day. Bureau Veritas, "
         "please confirm whether the inspector attended both days.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Inspection Request 004, as attached, ", False),
        ("gives ADASA nothing to act on", True),
        (". The result boxes, the comments field and the three signature blocks are empty, "
         "no test pack is identified, and neither the governing procedure nor its revision "
         "appears in the form; it records nothing that happened. It also carries the same "
         "two activities that did not take place this week, and it again covers two "
         "different days in a single date field and a single result box, which ADASA asked "
         "to correct on 12 August. The covering message transmits it as request 003 while "
         "the subject line and the form itself are 004, which leaves the inspector signing "
         "a document that identifies itself by another number.", False),
    ])
    blank(doc)

    add_para(doc, "What ADASA requires:")
    add_bullet_lead(
        doc, "A revised Inspection Request within the next 24 hours",
        ", with one form per inspection.")
    add_bullet_lead(
        doc, "The high-pressure hydrostatic test rescheduled to Monday 17 or Tuesday 18 "
             "August",
        ", not to Thursday 20.")
    add_bullet_lead(
        doc, "Three inspections next week",
        ", which is the ratio agreed with Bureau Veritas.")
    add_bullet_lead(
        doc, "The request issued on confirmed readiness and not on intent",
        ", so that the inspector is not mobilised again for a test that cannot run.")
    add_bullet_lead(
        doc, "The records of 13 and 14 August",
        ", together with those of the 7 August inspection, which are still outstanding.")
    blank(doc)

    add_para(doc, "Please treat this as a priority. We remain at your disposal to "
                  "coordinate the new dates.")
    blank(doc)

    add_para(doc, "Best regards,")
    blank(doc)

    p = doc.add_paragraph()
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in [
        "Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line)

    fijar_idioma(doc, LANG)

    docx_metadata.apply_core_properties(
        doc,
        title="Taltal - Request to witness inspection 004 - rescheduling",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Third-party shop inspection, notice of cancellation and "
                "rescheduling",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
