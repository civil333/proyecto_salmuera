#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del Transmittal N32 (P22-TM-09-000-032-0) a BW Water.
Cadena regular de transmittals. Ingles. Document() directo, sin template ADASA.

Cubre el submittal 25007-0075 (ENTREGA 75), siete documentos. Veredicto global
3 - To be revised: 2 Code 1, 3 Code 3 y 2 documentos devueltos SIN CODIGO.

Decision del usuario: no se codifica 3 un documento que ADASA ya habia dispuesto
Codigo 2 y que el proveedor ya emitio a Rev 0 para construccion. Los tres que no
cerraron su condicion vuelven sin codigo, como la Plant Control Philosophy del
N31, y sin PDF anotado.

CORREO EJECUTIVO, UNA PAGINA. Una linea de veredicto, la disposicion por
documento en una clausula cada uno, el hincapie -los tres procedimientos de
ensayos no destructivos llegan con el criterio de aceptacion del codigo
equivocado, y bajo procedimiento no aprobado los registros no entran al dossier-
y los dos puntos operativos que vencen antes de la jornada de inspeccion del 13
y 14 de agosto. El detalle documentado vive en el transmittal y no se repite.
No propone reunion.

LOS DOS PUNTOS OPERATIVOS son los que no esperan al ciclo de revision:
  1. Cual revision del procedimiento de pintura gobierna la inspeccion de
     preparacion, porque hay dos documentos distintos identificados como Rev 0
     y el tercero inspector tiene una copia anterior.
  2. El formulario en que se registrara el ensayo hidrostatico de alta presion,
     pedido el 06-Ago y todavia sin respuesta, con el ensayo como punto de
     detencion del ITP.

El PDF del transmittal va ADJUNTO; los tres PDF anotados, por ENLACE de
descarga. El enlace queda ademas impreso en la Seccion 4 del transmittal, de
modo que sobrevive al reenvio del adjunto sin el correo: en el N30 y en el N31
el parrafo del enlace no salio en el cuerpo del correo.

Estado: BORRADOR, pendiente de revision y envio.
"""
import os
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-12_Transmittal-N32.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"
# REEMPLAZAR por el enlace Synology real antes de enviar. Debe coincidir con el
# DOWNLOAD_LINK de crear_transmittal.py del TM N32.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19RfyvmUCVljlSVMK7cE99bMNzRFanZn/"
    "7ZHTbwNjM-UohAkFjug-WoQAaZDT994X-gryAOZ8ZbA0"
)


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


def add_hyperlink(paragraph, url, text):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink")
    h.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    rf.set(qn("w:ascii"), "Arial")
    rf.set(qn("w:hAnsi"), "Arial")
    rpr.append(rf)
    c = OxmlElement("w:color")
    c.set(qn("w:val"), "0563C1")
    rpr.append(c)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    h.append(run)
    paragraph._p.append(h)


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
        ("Date:", "August 12, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Andrew Sia, Magdier Arias, Victor Gutierrez, Jeryl F. Regulacion, "
                "Jorge Guevara, Ronald Pellejero, Stephane Gehant"),
        ("Subject:", "25007 Taltal - Technical Review Transmittal N32 - submittal "
                     "25007-0075"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_segments(doc, [
        ("Transmittal N32 (", False), ("P22-TM-09-000-032-0", True),
        (") is attached. It responds to submittal 25007-0075, seven documents. Tally: "
         "2 Code 1, 3 Code 3, and two documents returned without a response code. Overall "
         "verdict: ", False),
        ("3 - To be revised", True), (".", False),
    ])
    blank(doc)

    add_para(doc, "Disposition:")
    add_bullet_lead(doc, "PMI Procedure Rev 0 - Code 1. ", "No action.")
    add_bullet_lead(doc, "Visual Procedure Rev 0 - Code 1. ", "No action.")
    add_bullet_lead(doc, "HP and LP Pressure Test Procedure Rev 0 - no response code. ",
                    "Identify the pressure test record.")
    add_bullet_lead(doc, "Painting Procedure Rev 0 - no response code. ",
                    "Correct the finish colour on the inspection form to RAL 5012.")
    add_bullet_lead(doc, "Liquid Penetrant Examination Procedure Rev A - Code 3. ",
                    "State the piping acceptance criteria.")
    add_bullet_lead(doc, "Radiography Examination Procedure Rev A - Code 3. ",
                    "State the acceptance criteria and the geometric unsharpness limit.")
    add_bullet_lead(doc, "Ultrasonic Thickness Procedure Rev A - Code 3. ",
                    "State an acceptance criterion and write the technique for UNS S32750.")
    blank(doc)

    add_segments(doc, [
        ("Each action in Section 2 separates what has to change before the procedure is "
         "used from what is to be tidied at the same issue, so that a Rev B need not wait "
         "for a full cycle.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("One point is not in the documents. ", True),
        ("Penetrant testing was carried out on 7 August under a procedure that reaches "
         "ADASA in this submittal. Please state which penetrant records exist to date and "
         "under which acceptance criteria they were evaluated.", False),
    ])
    blank(doc)

    add_para(doc, "Review period: Friday 21 August, per Clause 37.2.")
    blank(doc)

    add_para(doc, "Attached: TRANSMITTAL N32 ADASA-BW_WATER.pdf")
    p = add_segments(doc, [
        ("The three annotated PDFs, listed in Section 4 of the transmittal, are available "
         "here: ", False)])
    add_hyperlink(p, DOWNLOAD_LINK, DOWNLOAD_LINK)
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
        title="Taltal - Technical Review Transmittal N32 - submittal 25007-0075",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Transmittal N32 cover email",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: reemplazar DOWNLOAD_LINK antes de enviar, y que coincida "
              "con el del transmittal.")


if __name__ == "__main__":
    crear_correo()
