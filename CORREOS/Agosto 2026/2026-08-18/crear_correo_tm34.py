#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del TRANSMITTAL N34, submittals 25007-0073, 25007-0077 y
25007-0080. Ejecutivo y directo, sobre el hilo de los submittals.

Cuatro cosas y nada mas. El pedido del usuario del 18-Ago fue que el correo NO
detalle el documento adjunto:

  1. Veredicto con el adjunto.
  2. Que solo UN documento vuelve a revision, y que el transmittal dice lo que cada
     uno requiere. Sin enumerar los capitulos ni las cifras: eso vive en el adjunto.
  3. Lo unico que cae FUERA del transmittal y por eso si va en el cuerpo: el rango
     vinculante de VT-09-001 que ADASA declara y la reemision de la Instrument List.
  4. La recepcion de las submittals 0073 y 0077 y el plazo de la Clausula 37.2.

NO repite la sustancia del transmittal: el detalle de cada documento vive en el
adjunto y en los tres CC_ADASA.

El enlace de descarga va EN EL CUERPO y verificado sobre el .docx emitido, no
sobre este script: ese fue el modo de falla del N30, el N31 y el N32.

Sin em dash en la prosa (U-10 / CL-13). Ingles. Document() directo, sin template
ADASA. Estado: BORRADOR.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-18_Transmittal-N34.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace publicado el 18-Ago-2026. Va EN EL CUERPO.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19WVqhVU8zwy31naz76IwRhUhCks28r6/"
    "tA3kHXW9cHDSvxetipsYW9ruR-Mk9hrr-9LBA_RPabw0"
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
        ("Date:", "August 18, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Allan Valentos, Eduardo Yamauchi - BW Water"),
        ("CC:", "Fitri Indriyani, Stephane Gehant, Magdier Arias, Muhammad Fadhil Bin "
                "Abdul Wahid - BW Water; Victor Gutierrez, Jorge Guevara, Ronald "
                "Pellejero - ADASA"),
        ("Subject:", "TALTAL - Transmittal N34 - submittals 25007-0073, 25007-0077 and "
                     "25007-0080"),
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
        ("Transmittal N34 (P22-TM-09-000-034-0)", True),
        (", on submittals 25007-0073, 25007-0077 and 25007-0080, five documents. ", False),
        ("Verdict: 3 — To be revised. Two Code 1, two Code 2, one Code 3.", True),
    ])
    blank(doc)

    add_segments(doc, [
        ("Only the Quality Dossier Index Rev B returns to revision.", True),
        (" The two general arrangement drawings are Code 2 and incorporate their "
         "remaining item at Rev 0, with no new revision. The two documents issued at Rev "
         "0 need no action. The transmittal states what each one requires.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("One item falls outside the transmittal: ADASA declares the binding range of "
         "VT-09-001 to be 0 to 12 mm/s rms.", True),
        (" Please re-issue the Instrument List to that value, so that the vibration stop "
         "of the high-pressure pump can act.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Submittals 25007-0073 and 25007-0077 both reached us, and Transmittal N33 "
         "reported them missing. Under Clause 37.2 our review runs to Thursday 20 August "
         "for the 0073 and Thursday 27 August for the other two.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the three annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Quality Dossier Index Rev B",
                    " — P22-BA-09-000-013_B_Quality_Dossier_Index_CC_ADASA.pdf")
    add_bullet_lead(doc, "GA of Antiscalant Dosing Pump Skid Rev C",
                    " — P22-DWG-09-005-011_C_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf")
    add_bullet_lead(doc, "GA of CIP / Flushing Tank Rev B",
                    " — P22-DWG-09-005-014_B_GA_CIP_Flushing_Tank_CC_ADASA.pdf")
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
        title="Taltal - Transmittal N34 - submittals 25007-0073, 25007-0077 and 25007-0080",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Technical review transmittal N34, cover email",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
