#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ejecutivo a BW Water: que quedo levantado y que no, de los comentarios
con que ADASA aprobo cada documento de la ENTREGA 71 (submittal 25007-0071).

Cinco documentos, todos recibidos en Rev 0 IFC. Cuatro conservan comentarios sin
incorporar; el informe de calculo estructural incorporo los dos suyos.

Criterio de redaccion:
  - SIN codigos de respuesta. Los codigos son instrumento del transmittal;
    comunicarlos por correo sin transmittal deja la disposicion sin respaldo
    formal y sube el tono sin necesidad. El correo dice que falta, no que nota
    saca cada documento.
  - Cada bloque reconoce primero lo que si se cerro y luego enuncia lo que
    queda. Solo se menciona lo que era condicion de la aprobacion previa; NO se
    levantan hallazgos nuevos sobre documentos que ADASA ya aprobo.
  - Referencias a la ET por codigo + "Section N - Nombre" deletreado (nunca el
    simbolo de seccion), per CLAUDE.md Seccion 2.4.
  - Sin referencias internas (IDs OBS/NOTE, transmittals, Van Doorn).
  - Los dos items operativos previos a la inspeccion del 13-14 de agosto van
    como confirmaciones, no como imputacion de falta.

Formato: parrafo simple con bullets, sin tablas (patron de notificacion de la
Seccion 3.4). Una pagina. Document() directo, sin template ADASA.

Estado: BORRADOR, pendiente de revision y envio.
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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-06_Submittal-25007-0071-Outstanding-Items.docx")
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


def add_segments(doc, segs, size=11, indent=None):
    p = doc.add_paragraph()
    if indent is not None:
        p.paragraph_format.left_indent = Inches(indent)
    for text, bold in segs:
        r = p.add_run(text)
        r.bold = bold
        r.font.name = "Arial"
        r.font.size = Pt(size)
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
        ("Date:", "August 6, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Andrew Sia, Magdier Arias, Victor Gutierrez, Jorge Guevara, "
                "Ronald Pellejero"),
        ("Subject:", "25007 Taltal - Submittal 25007-0071: outstanding items"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_para(doc, "We have reviewed submittal 25007-0071 against the comments noted "
                  "when each of these documents was approved. On the points below we "
                  "would ask you to review or clarify.")
    blank(doc)

    add_segments(doc, [
        ("PMI Procedure. ", True),
        ("The ten per cent scope on the Super Duplex high-pressure circuit and "
         "ADASA's witness right are correctly declared. Please clarify which document "
         "fixes the acceptance basis. The acceptance section refers approval and "
         "rejection to third-party refinery standards, while the Technical "
         "Specification (P22-ET-09-000-001-0), Section 8 - Inspections During "
         "Manufacturing and row 2.4 of the Inspection and Test Plan both name "
         "UNS S32750. Please also review the subcontractor appendix, which states "
         "five per cent per lot for bolts and nuts against the minimum ten per cent "
         "of that same row, and is not bounded to this project.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Visual Procedure. ", True),
        ("The VT qualification is now stated, which closes that point. Please clarify "
         "the form on which the visual examination is recorded, stating its number and "
         "revision. The procedure no longer identifies one, and row 3.2 of the "
         "Inspection and Test Plan requires a visual report as the certificate at a "
         "witness point.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Painting Procedure. ", True),
        ("The anchor profile now reads 50 to 80 micrometres throughout, which closes "
         "that point. Please review the inspection form, which carries neither the "
         "finish colour RAL 5012 nor the product per coat.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("HP and LP Pressure Test Procedure. ", True),
        ("Sections 3.1 and 3.2 now fix ASME Section V 2025 and ASME B31.3 2024. "
         "Please review clauses 5.5.2 and 5.6.3, which still require the latest "
         "edition and addenda, so that the edition is not fixed for the tests "
         "themselves; and please state the applicable addenda.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("UHPRO Structural Calculation Report. ", True),
        ("Both noted items are incorporated. Nothing outstanding.", False),
    ])
    blank(doc)

    p = doc.add_paragraph()
    p.add_run("Two confirmations ahead of the 13 and 14 August inspection:").bold = True
    aplicar_arial(p)
    blank(doc)

    add_para(doc, "Please confirm the form on which the high-pressure hydrostatic test "
                  "will be recorded. Section 5.8 refers to a Pressure Test Report that "
                  "is not part of the submittal, and the test is a hold point.")
    blank(doc)

    add_para(doc, "Please confirm that Rev 0 of the Painting Procedure governs the "
                  "painting preparation inspection. The copy held in the third-party "
                  "inspection package is Rev B, and the two revisions state different "
                  "blast profile criteria.")
    blank(doc)

    add_para(doc, "Best regards,")
    blank(doc)
    p = doc.add_paragraph()
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in ["Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
                 "lrivera@aguasantofagasta.cl"]:
        add_para(doc, line)

    fijar_idioma(doc, LANG)
    docx_metadata.apply_core_properties(
        doc, title="Taltal - Submittal 25007-0071 outstanding items",
        author="Luis Rivera Gonzalez", last_modified_by="Luis Rivera Gonzalez",
        subject="Outstanding items on submittal 25007-0071",
        comments="Correo ejecutivo a BW Water con los comentarios aun no incorporados.",
        language="en-US")
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas de Antofagasta S.A.")
    print("Correo generado: " + OUTPUT_FILE)


if __name__ == "__main__":
    crear_correo()
