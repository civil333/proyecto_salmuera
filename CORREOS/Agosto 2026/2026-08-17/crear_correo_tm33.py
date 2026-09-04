#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del TRANSMITTAL N33, submittals 25007-0076, 25007-0078 y
25007-0079. Ejecutivo, sobre el hilo de los submittals.

Cuatro cosas y nada mas: el veredicto con el adjunto, el enlace de descarga del
CC_ADASA EN EL CUERPO (se cayo en el N30, el N31 y el N32), la
ausencia del submittal 25007-0077 como pregunta, y el plazo real de la Clausula
37.2 frente a las fechas de retorno que pidio el proveedor, una de ellas en
domingo.

NO repite la sustancia del transmittal: el detalle de cada documento vive en el
adjunto. Lo unico que el cuerpo nombra es que el plano civil es el unico con
observaciones, y cuales son las dos, porque es lo que el proveedor tiene que
hacer.

RE-ALCANCE del 17-Ago: el correo ya NO adelanta el diametro de los pernos de
anclaje. Ese punto, como todo lo que salia de contenido nuevo de los planos, se
ve con L&A y no con BW Water (compromiso INT-11).

Ingles. Document() directo, sin template ADASA. Estado: ENVIADO el 17-Ago-2026,
registrado a las 12:17 de Chile (16:17 en Penang). Con esto queda emitido el
Transmittal N33, dentro de los plazos de la Clausula 37.2 (24 y 26 de agosto).

VERSION EJECUTIVA (pedido del usuario del 17-Ago): 199 palabras, oracion maxima
de 32. Cuatro parrafos: veredicto en dos frases; las dos acciones, ambas sobre el
plano civil, con la frase explicita de que los otros cuatro documentos no
requieren accion; la alerta del submittal 25007-0077 con su consecuencia
contractual; y el plazo de la Clausula 37.2 en una linea.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-17_Transmittal-N33.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace publicado el 17-Ago-2026. Va EN EL CUERPO: se cayo en el N30, N31 y N32.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19Vh5BdPy7Bawfney5aMrUV8sZlaFy99/"
    "hGVtoOjNlRe8KS3GBP2Ek-22F4fX0UUP-4rJA83s3bw0"
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
        ("Date:", "August 17, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Allan Valentos, Eduardo Yamauchi - BW Water"),
        ("CC:", "Fitri Indriyani, Stephane Gehant, Magdier Arias, Muhammad Fadhil Bin "
                "Abdul Wahid - BW Water; Victor Gutierrez, Jorge Guevara, Ronald "
                "Pellejero - ADASA"),
        ("Subject:", "TALTAL - Transmittal N33 - submittals 25007-0076, 25007-0078 and "
                     "25007-0079"),
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
        ("Transmittal N33 (P22-TM-09-000-033-0)", True),
        (", on submittals 25007-0076, 25007-0078 and 25007-0079, five documents. ", False),
        ("Verdict: 2 — Approved as noted. Four Code 1, one Code 2, none returned to "
         "revision.", True),
    ])
    blank(doc)

    add_segments(doc, [
        ("Two actions, both on the ", False),
        ("Civil and Loading Layout Rev B", True),
        (", from the Transmittal N16 note: state the weight of the empty modified "
         "container, and the row carrying the RO Skid frame. Both incorporate at Rev 0, "
         "with no new drawing revision. The other four documents need no action.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Submittal 25007-0077 has not reached ADASA", True),
        (". The series runs 0076, 0078, 0079. Please confirm whether it was issued and to "
         "whom. If it was and did not reach us, formal receipt never took place, so the "
         "seven working days of Clause 37.2 have not started for it.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Our review period under Clause 37.2 runs to Monday 24 August for 25007-0076 and "
         "Wednesday 26 August for the other two, and this transmittal is issued within all "
         "three.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the annotated PDF are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Civil and Loading Layout Rev B",
                    " — P22-DWG-09-005-001_B_Civil_Loading_Layout_CC_ADASA.pdf")
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
        title="Taltal - Transmittal N33 - submittals 25007-0076, 25007-0078 and 25007-0079",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Technical review transmittal N33, cover email",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
