#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del Transmittal N36 (P22-TM-09-000-036-0), submittals
25007-0082, 25007-0083, 25007-0084 y 25007-0085 (ENTREGAS 82 a 85). Cadena de
los transmittals.

**EL PROJECT SCHEDULE REV B QUEDA FUERA DEL TRANSMITTAL** por decision del
usuario del 26-Ago-2026: su seguimiento se lleva por la reunion semanal de
coordinacion. El transmittal lo declara en una linea y no le asigna codigo, de
modo que el correo dice lo mismo en su primer parrafo. El correo contractual
sobre el mismo documento (`crear_correo_programa_revB.py`, misma carpeta) sigue
en borrador y su envio esta por decidir.

CUERPO: veredicto, que vuelve a revision, que se reitera y el plazo. **No
detalla el adjunto.**

LO UNICO QUE VA EN EL CUERPO Y NO ESTA EN EL TRANSMITTAL: la advertencia de que
la fecha de devolucion pedida para el 25007-0085 cae en sabado. Se dice porque
condiciona la coordinacion de la proxima entrega y no puede esperar a que
alguien abra el adjunto.

FUERA DEL CORREO, a proposito: el desplazamiento del cronograma y el plazo de
entrega vencido, que van por la otra cadena; y el detalle tecnico de cada
observacion, que es contenido del transmittal y de los cuatro `CC_ADASA`.

Ingles. Document() directo, sin template ADASA. Estado: ENVIADO el 26-Ago-2026
a las 18:08 (hora de Chile). Respaldo del enviado en `envio transmittal 36.pdf`,
misma carpeta; la distribucion real y las dos diferencias contra este borrador
estan en el `*_Descripcion.md`.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-26_Transmittal-N36.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace de descarga de la carpeta del N36. Pegar el enlace publicado y
# REGENERAR. Verificar SIEMPRE sobre el .docx emitido, no sobre este script.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19dMoFG6j2lfmhv8nD87B2xwNe8vqKSA/Iz1GrP4ez1f-thJcQYsIuJ7I0Qfwb2sS-D7yAe18rdQ0"
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
        ("Date:", "August 26, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi, Allan Valentos - BW Water"),
        ("CC:", "Fitri Indriyani, Stephane Gehant, Jeryl F. Regulacion, Andrew Sia - "
                "BW Water; Victor Gutierrez, Jorge Guevara, Ronald Pellejero - ADASA"),
        ("Subject:", "TALTAL - Transmittal N36 - submittals 25007-0082 to 25007-0085"),
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
        ("Attached is ", False),
        ("Transmittal N36 (P22-TM-09-000-036-0)", True),
        (", on submittals 25007-0082 to 25007-0085, eight of their nine documents; the "
         "Project Schedule Rev B carries no code here and is followed through the "
         "weekly coordination. ", False),
        ("Verdict: 2 — Approved as noted. Three Code 1, five Code 2, and no document "
         "returns to revision.", True),
    ])
    blank(doc)

    add_segments(doc, [
        ("The three Fedco datasheets have to close.", True),
        (" The pump and the two turbochargers were approved at Rev D at Transmittal "
         "N11. The equipment was bought and built on that basis, it is now due at the "
         "workshop, and the pump is programmed for installation within days. Their "
         "datasheets still reach us as approval revisions. Please issue the three at "
         "Rev 0 for construction before the Factory Acceptance Test opens on 7 "
         "September.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("One point needs saying plainly.", True),
        (" The GA of SWRO System Skid Rev 0 is the only document here issued for "
         "construction: of its three pending references, one was corrected. Note 8 "
         "still cites a code that does not exist in the project numbering. The correct "
         "code is P22-ET-09-006-001, which is how the snapshot you attached to defend "
         "the reply writes it. We are not holding the drawing. Both corrections "
         "stand.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("On dates.", True),
        (" The four Submittal Forms asked for return three calendar days after issue, "
         "one of them on a Saturday. Under Clause 37.2 our review period runs to 1, 2 "
         "and 4 September.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the four annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Piping Layout Rev D",
                    " — P22-DWG-09-005-004_D_Piping_Layout_CC_ADASA.pdf")
    add_bullet_lead(doc, "GA of Antiscalant Dosing Tank Rev C",
                    " — P22-DWG-09-005-015_C_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf")
    add_bullet_lead(doc, "Datasheet of Feed Turbocharger Rev E",
                    " — P22-ET-09-009-007_E_Datasheet_Feed_Turbocharger_CC_ADASA.pdf")
    add_bullet_lead(doc, "Datasheet of Interstage Turbocharger Rev E",
                    " — P22-ET-09-009-008_E_Datasheet_Interstage_Turbocharger_CC_ADASA.pdf")
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
        title="TALTAL - Transmittal N36 - submittals 25007-0082 to 25007-0085",
        author="Luis Rivera Gonzalez",
        language="en-US",
        comments="Correo de cobertura del Transmittal N36. Cadena de los transmittals.",
    )
    doc.save(OUTPUT_FILE)
    print("Correo generado:", OUTPUT_FILE)
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")


if __name__ == "__main__":
    crear_correo()
