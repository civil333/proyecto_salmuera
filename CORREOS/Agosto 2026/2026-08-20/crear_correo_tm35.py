#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del Transmittal N35 (P22-TM-09-000-035-0), submittal
25007-0081 (ENTREGA 81). Cadena de los transmittals.

**CORREO SEPARADO, por decision del usuario.** El mismo dia sale por la cadena de
inspecciones el correo sobre el informe de ensayo hidrostatico del 20-Ago
(`crear_correo_hidrostatica_20ago.py`, misma carpeta). Los dos ejes no se mezclan:
uno responde documentos, el otro responde una jornada de inspeccion. La
cross-reference se neutraliza enviando ambos el mismo dia con los codigos ADASA
explicitos.

CUERPO: veredicto, que vuelve a revision, y el plazo. **No detalla el adjunto.**

LO UNICO QUE VA EN EL CUERPO Y NO ESTA EN EL TRANSMITTAL: nada. A diferencia del
N34, aca no hay un item que caiga fuera del documento adjunto, de modo que el
correo se limita a la cobertura.

FUERA DEL CORREO, a proposito: el ensayo del 20-Ago y el TAG del Spool 1, que van
en el correo de la otra cadena; el plazo de entrega vencido el 03-Ago; y el
detalle tecnico de cada Codigo 3, que es contenido del transmittal y de los tres
`CC_ADASA`.

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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-20_Transmittal-N35.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace de descarga de la carpeta del N35, publicado el 20-Ago-2026.
# Verificar SIEMPRE sobre el .docx emitido, no sobre este script.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19YAtLM7VpZHgw8EqV1StbIjc46CGmqy/"
    "FRH14L__RLZ3Y-BIAYpwIZHqO5Q90IUV-Z7KA1hokcQ0"
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
        ("Date:", "August 20, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Allan Valentos, Eduardo Yamauchi - BW Water"),
        ("CC:", "Fitri Indriyani, Stephane Gehant, Magdier Arias, Muhammad Fadhil Bin "
                "Abdul Wahid - BW Water; Victor Gutierrez, Jorge Guevara, Ronald "
                "Pellejero - ADASA"),
        ("Subject:", "TALTAL - Transmittal N35 - submittal 25007-0081"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Allan,")
    blank(doc)

    add_segments(doc, [
        ("Attached is ", False),
        ("Transmittal N35 (P22-TM-09-000-035-0)", True),
        (", on submittal 25007-0081, five documents. ", False),
        ("Verdict: 3 — To be revised. Two Code 1, three Code 3.", True),
    ])
    blank(doc)

    add_segments(doc, [
        ("The three non-destructive testing procedures return to revision", True),
        (", for the same point as Transmittal N32: none states the acceptance criterion "
         "that the Technical Specification and the approved NDE Plan require for this "
         "scope. All three were re-issued without a consolidated comment sheet; Rev C "
         "should carry it. The two procedures issued above Rev 0, the pressure test and "
         "the painting procedure, are Code 1 and need no action.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("One item needs attention before the next test.", True),
        (" The transmittal states the test pressure of each super duplex line, 1.5 "
         "times its design pressure per the approved Line List, and asks that no "
         "further test of that circuit be run until you confirm those values in "
         "writing. We have raised it in parallel through the inspection channel.",
         False),
    ])
    blank(doc)

    add_segments(doc, [
        ("The Submittal Form requests a response by Sunday 23 August. Under Clause "
         "37.2 our review period runs to Monday 31 August.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the three annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Liquid Penetrant Examination Procedure Rev B",
                    " — P22-BA-09-000-014_B_Liquid_Penetrant_Procedure_CC_ADASA.pdf")
    add_bullet_lead(doc, "Radiography Examination Procedure Rev B",
                    " — P22-BA-09-000-015_B_Radiography_Procedure_CC_ADASA.pdf")
    add_bullet_lead(doc, "Ultrasonic Thickness Procedure Rev B",
                    " — P22-BA-09-000-016_B_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf")
    blank(doc)

    add_para(doc, "We remain at your disposal for any clarification.")
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
        title="Taltal - Transmittal N35 - submittal 25007-0081",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Technical review transmittal, quality and fabrication "
                "procedures",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: enlace en placeholder. Publicar la carpeta, pegar el enlace y "
              "REGENERAR antes de emitir. Verificar sobre el .docx, no sobre el script.")


if __name__ == "__main__":
    crear_correo()
