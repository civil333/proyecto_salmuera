#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de seguimiento ADASA -> BW Water + Bureau Veritas por el silencio de tres
dias al reclamo del 14 de agosto de 2026 sobre el Request to witness inspection
004. Reply-all al MISMO hilo del Request 004: cadena de las jornadas, SEPARADA
de la de transmittals.

ESCALADA A DIRECCION DE PROYECTO. To: Eduardo Yamauchi y Stephane Gehant, mas el
equipo QAQC de Penang y Bureau Veritas. Es el curso de accion que el registro de
compromisos ya habia fijado en el campo accion_adasa de PRG-28: "si el formulario
revisado no llega, escalar a Yamauchi y Gehant y dejar constancia de la segunda
semana perdida".

TRES DECISIONES DEL USUARIO QUE GOBIERNAN EL CUERPO:
  1. FIRMEZA: reserva de no aceptacion mas constancia de Clausula 37. Una prueba
     de punto Hold ejecutada sin aviso escrito y sin inspector presente no se
     acepta como evidencia y se repite.
  2. ALCANCE: todo lo que no se reporte del jueves 13 y del viernes 14. Lo que no
     tenga registro firmado ni informe de Bureau Veritas de esos dos dias se
     tiene por no ejecutado y vuelve a notificarse para testificacion.
  3. FECHA: el ensayo de alta se exige HOY, dentro de la ventana que sigue
     abierta en Penang, con Bureau Veritas notificado ahora.

LA CONSTANCIA SE ACOTA AL AVISO POSTERIOR AL CIERRE DE LA VENTANA, no al deficit
contra los treinta dias. El correo del 14-Ago declaro que ADASA acepto avisos de
cuatro y de ocho dias para no frenar la fabricacion; reclamar ahora los treinta
se contradiria con eso y seria refutable.

FUERA DEL CORREO, a proposito:
  - La hidrostatica de BAJA presion y la del RO Vessel, que el Request 003
    recorto, siguen trackeadas en PRG-13. El eje de este correo son los dos dias
    sin reportar.
  - El plazo de entrega vencido el 03-Ago y la multa de la Clausula 43.1 letra b:
    otro eje y otra cadena, con el inspector entre los destinatarios.
  - La tarifa de Bureau Veritas y el saldo de jornadas contratadas: informacion
    interna de ADASA.
  - No se afirma que se ejecuto cada dia ni si el inspector asistio: se pregunta.

Excepcion de correo conjunto: se nombra a BW Water aunque Bureau Veritas este
entre los destinatarios.

Ingles. Document() directo, sin template ADASA. Estado: ENVIADO el 17-Ago-2026,
registrado a las 09:07 de Chile (13:07 en Penang), con la ventana de inspeccion aun
abierta. Se envio con la vinieta del tope del miercoles 19 incluida.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-17_BV-Inspection-004-Follow-Up.docx")
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
        ("Date:", "August 17, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi, Stephane Gehant, Mohd Adnin Bin Zulkaflee, "
                "Muhammad Fadhil Bin Abdul Wahid - BW Water; Ahmad Hazwan, "
                "Carlo Montecinos, Wan Mohd Adli W Yahya, Emylia Rosli - Bureau Veritas"),
        ("CC:", "Magdier Arias, Lokman Hakim Bin Mat - BW Water; Victor Gutierrez, "
                "Jorge Guevara, Ronald Pellejero - ADASA"),
        ("Subject:", "RE: 25007 TALTAL - Request to witness inspection 004 - rescheduling"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo, Stephane,")
    blank(doc)

    add_segments(doc, [
        ("Our email of Friday 14 August is unanswered. The revised Inspection Request "
         "fell due on Saturday 15 and has not arrived. ", False),
        ("The Monday window in Penang is running with no notice of the high-pressure "
         "test", True),
        (", so the first of the two dates ADASA offered is being lost as well. We ask "
         "you both to take this over.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("ADASA records the notice of 14 August, issued once the window had closed, as ",
         False),
        ("a failure to comply with Clause 37 of the BAE", True),
        (", which requires each inspection to be confirmed in writing to the Buyer in "
         "advance. What ADASA objects to is a notice given after the fact, and that "
         "objection holds whatever the technical cause was. The record stands as a "
         "precedent for the hold and witness points that remain.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("The hold point under row 5.2 of the Inspection and Test Plan "
         "(P22-BA-09-000-004) remains in force. ", False),
        ("A pressure test carried out without written notice and without the inspector "
         "present will not be accepted as evidence of that hold point", True),
        (", and ADASA will require it to be repeated.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Thursday 13 and Friday 14 remain undocumented. ", False),
        ("Any activity of those two days for which no signed record and no Bureau "
         "Veritas report is produced is treated as not executed", True),
        (", and is to be re-notified for witnessing. This covers the high-pressure "
         "test, the piping spool visual and dimensional inspection that replaced it, "
         "and the painting preparation.", False),
    ])
    blank(doc)

    add_para(doc, "What ADASA requires today:")
    add_bullet_lead(
        doc, "The high-pressure hydrostatic test today",
        ", within the window still open in Penang, with Bureau Veritas notified now.")
    add_bullet_lead(
        doc, "A written statement before the window closes if it cannot run today",
        ", with the reason, and the test placed no later than Wednesday 19 August.")
    add_bullet_lead(
        doc, "A revised Inspection Request",
        ", one form and one result per inspection, superseding Inspection Request 004.")
    add_bullet_lead(
        doc, "The signed records of 13 and 14 August",
        ", today, with a written statement of what was executed on each day.")
    add_bullet_lead(
        doc, "The records of the 7 August inspection",
        ", outstanding for ten days.")
    add_bullet_lead(
        doc, "Bureau Veritas, confirmation of whether the inspector attended on 13 and "
             "on 14 August",
        ", and the report of each day.")
    blank(doc)

    add_para(doc, "Please reply today.")
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
        title="Taltal - Request to witness inspection 004 - follow up",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Third-party shop inspection, hold point reservation and "
                "outstanding records",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
