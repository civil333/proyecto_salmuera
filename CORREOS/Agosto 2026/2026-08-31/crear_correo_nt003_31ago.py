#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de remision de la Nota Tecnica P22-NT-09-000-003-0 a BW Water.

Reply al hilo de Eduardo Yamauchi del 31-Ago-2026 15:29 hora de Chile,
"FW: 20.25.6501 Taltal - Weekly Progress Update", que avisa el corrimiento de la
System Readiness Shipping Date del 21 al 28 de septiembre por clima.

=======================================================================
VERSION SUAVE. Decision del usuario, 31-Ago: NO COMPROMETER LA ENTREGA DEL 28.
=======================================================================

Una primera version decia "ADASA does not accept the move to 28 September", daba
los 44 dias de desviacion contra la linea base del proveedor y fijaba plazo al
viernes 4. NO SE EMITIO. El objetivo pasa a ser ASEGURAR el 28, no disputarlo.

EL CORREO PIDE SOLO LO QUE PROTEGE LA FECHA, tres cosas, una linea cada una:
  1. Que ventana del FAT gobierna. El Rev B la pone del 7 al 18 de septiembre y
     el Progress Update del 15 al 25. Los inspectores son de Bureau Veritas
     Malasia y atienden en Penang; la coordinacion pasa por Bureau Veritas
     Chile, de modo que una fecha flotante impide comprometer al inspector.
  2. La llegada de la bomba de alta el 11 contra su instalacion programada el 9
     y 10. Si eso no se reconcilia, el 28 se cae solo.
  3. El loading schedule y el vessel closing date, que ADASA necesita para tener
     nave reservada esa semana.

LO UNICO CON EFECTO CONTRACTUAL es la frase neutra del segundo parrafo: tomar
nota de la fecha revisada no constituye aceptacion de una nueva fecha contractual
ni renuncia a los derechos del Contrato. SIN numeros de clausula, SIN la palabra
multa, SIN mencionar el 21 de septiembre. Sin ella, el 21 y el 28 se consolidan
por silencio y se pierde la posicion de PRG-07 y PRG-08.

FUERA a proposito: "does not accept", los 44 dias, las Clausulas 27, 43 y 44, el
punto del pintado del contenedor y el plazo de ultimatum. Todo eso queda en el
registro interno, disponible si la fecha vuelve a moverse.

SIN PLAZO IMPUESTO: la respuesta se pide con el proximo reporte semanal.

ADJUNTO: P22-NT-09-000-003-0_Ex-Works-Date-Non-Acceptance_ADASA.pdf, cuatro
paginas, exportado desde Word real para que el indice quede resuelto.

Ingles. Document() directo, sin template ADASA. Estado: BORRADOR.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-31_NT003-Ex-Works-Date.docx")
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
        ("Date:", "August 31, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi, Stephane Gehant - BW Water"),
        ("CC:", "Lokman Hakim Bin Mat, Elaine May Torres, David Chee Keat Swee, "
                "Sadeep Irugalbandara, Nick Huta - BW Water; "
                "Victor Gutierrez, Jorge Guevara, Ronald Pellejero - ADASA"),
        ("Subject:", "RE: 20.25.6501 Taltal - Weekly Progress Update - securing "
                     "the 28 September ex-works date"),
        ("Attachment:", "P22-NT-09-000-003-0 - Technical Note"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    espaciador(doc)

    add_para(doc, "Dear Eduardo,")

    # Parrafo 1: el objetivo compartido y los tres puntos que protegen la fecha.
    add_segments(doc, [
        ("Thank you for the update. ", False),
        ("We are working with you so that the 28 September holds", True),
        (", and three points in the attached schedule need closing to protect it: "
         "which Factory Acceptance Test window governs, since Rev B and the Progress "
         "Update differ and the inspector has to be booked for the whole window; the "
         "high pressure pump "
         "arriving on 11 September against installation programmed for 9 and 10; and "
         "the loading schedule and vessel closing date, which we need to book the "
         "vessel.", False),
    ])

    # Parrafo 2: el adjunto, la frase neutra de reserva y la respuesta sin plazo.
    add_segments(doc, [
        ("Technical Note P22-NT-09-000-003-0 is attached", True),
        (" with the five items. Taking note of the revised date does not "
         "constitute acceptance of a new contractual date, nor a waiver of any right "
         "under the Contract. We would appreciate your answers with the next weekly "
         "update.", False),
    ])

    add_para(doc, "Best regards,", space=0)
    espaciador(doc)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in [
        "Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line, space=0)

    fijar_idioma(doc, LANG)

    docx_metadata.apply_core_properties(
        doc,
        title="Taltal - securing the 28 September ex-works date",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Second Stage RO Brine Module - Taltal - transmittal of Technical "
                "Note P22-NT-09-000-003-0",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
