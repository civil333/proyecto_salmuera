#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water en respuesta al correo de Eduardo Yamauchi del 17-Ago-2026
(18:52 de Chile) que reenvia el hilo interno de Stephane Gehant del 16-Ago y pide a
ADASA que recomiende un Professional Engineer chileno para el endoso del calculo
sismico del modulo.

Reply-To al MISMO hilo del correo recibido. Cadena SEPARADA de la de transmittals y
de la del frente Bureau Veritas.

QUE DEJA CONSTANCIA, Y SOBRE QUE SE FUNDA:
  El endoso profesional NO es exigencia de la Especificacion Tecnica, de las Bases
  Administrativas ni del PIE: ninguno de los tres lo pide. La ET solo exige la
  Memoria de Calculo Sismico y su aprobacion por ADASA (Section 7). Por eso el
  correo NO cita la ET como fuente del endoso: seria refutable en una linea
  (regla anti-invencion, CLAUDE.md Seccion 6.2).
  El endoso es un COMPROMISO PROPIO de BW Water, declarado por escrito tres veces:
    - 20-May-2026, Consolidated Comment Sheet del plano P22-DWG-09-005-015 Rev B
      (ENTREGA 60): "Seismic data will be furnished once all the calculations are
      verified by a Professional Engineer."
    - 16-Jun-2026, minuta: "Report to be certified by a PE in Chile."
    - 30-Jun-2026, minuta: "forwarded to the Chilean Professional Engineer (PE) for
      certification and stamping", con la accion tabulada
      "Frame Structure | Submit package to Chilean PE | BW Water | 01-Jul-2026".
  ADASA pidio por escrito la fecha de emision del informe certificado el 17-Jun-2026
  y nunca la recibio.
  Soporte contractual de la obligacion y de la reserva: BAE Clausula 45, Cumplimiento
  de las Leyes, que pone todo permiso, licencia y certificado necesario para el
  cumplimiento del Pedido a cargo y expensas del Proveedor, eximiendo al Comprador de
  responsabilidad.

DECISIONES DEL USUARIO QUE GOBIERNAN EL CUERPO:
  1. El documento esta en Codigo 1, de modo que NO se mencionan los defectos tecnicos
     del informe Rev 0 que ADASA registro y no emitio (combinaciones 224/226 con
     reacciones identicas, pernos de BOI-09-001/002 ausentes, chequeo de la base del
     contenedor con reacciones de la Rev A, suelo Tipo E). Mencionarlos reabriria una
     aprobacion propia.
  2. El asunto debe quedar cerrado al final de esta semana: viernes 22-Ago-2026.
  3. La reserva economica se incluye citando la Clausula 45.

EXPANSION DECLARADA: la fecha tope del miercoles 19 para la declaracion escrita no la
pidio el usuario. Se incluye porque sin fecha de reemplazo el vacio lo llena BW Water
con la suya; se borra si sobra.

BLINDAJE DE LA RECOMENDACION: Thomas Engineers se entrega como referencia y sin
designacion. Sin esa clausula, cualquier atraso del profesional se le atribuye
despues a ADASA, y la gestion del endoso pasaria de obligacion del proveedor a
gestion compartida.

FUERA DEL CORREO, a proposito: el Plazo de Entrega vencido el 03-Ago y la multa de la
Clausula 43.1 letra b (otra cadena); el frente Bureau Veritas; el submittal
25007-0077; y los defectos del punto 1.

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
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-08-18_Seismic-Calculation-PE-Endorsement.docx")
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
    r0 = p.add_run("\u2022  " + lead)
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
        ("Date:", "August 18, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Stephane Gehant, Sadeep Irugalbandara, Marjan Arsovic - BW Water; "
                "Victor Gutierrez - ADASA"),
        ("Subject:", "RE: 25007 Taltal: seismic calculation endorsement by local PE"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # Bloque 1 - el hecho, y las fechas en que BW Water lo dio por encaminado
    add_segments(doc, [
        ("We can recommend someone. What concerns us is that ", False),
        ("the endorsement has not started", True),
        ("; BW Water's own record on this item reads:", False),
    ])
    add_bullet_lead(
        doc, "20 May 2026, comment sheet of drawing P22-DWG-09-005-015 Rev B: ",
        "\"Seismic data will be furnished once all the calculations are verified by "
        "a Professional Engineer.\"")
    add_bullet_lead(
        doc, "16 June 2026, meeting minutes: ",
        "\"Report to be certified by a PE in Chile.\"")
    add_bullet_lead(
        doc, "30 June 2026, meeting minutes: ",
        "the package would be \"forwarded to the Chilean Professional Engineer (PE) "
        "for certification and stamping\". Tabled action: \"Submit package to "
        "Chilean PE\", dated 1 July 2026.")
    add_bullet_lead(
        doc, "23 July 2026: ",
        "the report was issued at Rev 0 for construction (P22-CD-09-005-001), signed "
        "internally and with no endorsement.")
    blank(doc)

    # Bloque 2 - lo que ADASA pidio, y de quien es la obligacion
    add_segments(doc, [
        ("ADASA asked for a committed issue date on 17 June 2026 and never received "
         "one. Forty-eight days after the action dated 1 July, your email of "
         "yesterday confirms there is still no appointed professional. ", False),
        ("The endorsement is BW Water's obligation, at its own cost and expense",
         True),
        (", under Clause 45 of the BAE, and ADASA neither assumes it nor shares its "
         "management. The general arrangement drawings still read \"BOLTING DETAILS "
         "TO BE FINALIZED AND ENDORSED\".", False),
    ])
    blank(doc)

    # Bloque 3 - la recomendacion, con su limite
    add_segments(doc, [
        ("For reference, with no designation implied: Thomas Engineers, a Chilean "
         "civil and structural consultancy in the north of the country; "
         "Tomás Ávila, tavila@thomasengineers.cl, +56 9 3412 6856. ", False),
        ("ADASA has no contractual relationship with this firm", True),
        (" and takes no responsibility for its performance, fees or lead time.",
         False),
    ])
    blank(doc)

    # Bloque 4 - fecha y reserva
    add_segments(doc, [
        ("Please close this item ", False),
        ("by Friday 22 August 2026", True),
        (": the professional confirmed in writing and the endorsed report issued. "
         "If that is not achievable, a written statement is required before close "
         "of business on Wednesday 19 August, with an alternative date supported by "
         "the appointed professional. Under Clause 45, any change to anchorage or "
         "fabricated steel arising from the endorsement is for BW Water's account "
         "and time.", False),
    ])
    blank(doc)

    add_para(doc, "We look forward to your written confirmation.")
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
        title="Taltal - Seismic calculation endorsement by local PE",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Professional endorsement of the module seismic "
                "calculation report",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
