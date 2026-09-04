#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Follow-Up — Propuesta 25007-PL-0001 rev.1 sin respuesta
Fecha: 17 de Marzo de 2026
Destinatario: Eduardo Yamauchi — BW Water Americas Inc.
"""

import sys
import os

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_FILE = "2026-03-17_Followup-Layout-Proposal.docx"
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11, bold=False, italic=False):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
        if bold:
            run.bold = True
        if italic:
            run.italic = True


def agregar_campo_header(doc, label, value):
    para = doc.add_paragraph()
    run_label = para.add_run(label)
    run_label.bold = True
    run_label.font.name = "Arial"
    run_label.font.size = Pt(11)
    run_value = para.add_run(f" {value}")
    run_value.font.name = "Arial"
    run_value.font.size = Pt(11)
    return para


def agregar_parrafo(doc, texto, size=11):
    para = doc.add_paragraph(texto)
    for run in para.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(1.1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "March 17, 2026"),
        ("From:", f"{CONTACTO} \u2014 Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, "
            "Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "RE: 25007 Taltal \u2013 Proposal for Layout Changes (25007-PL-0001 rev.1)",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803"),
    ]
    for label, value in fields:
        agregar_campo_header(doc, label, value)

    doc.add_paragraph()

    # ── SALUDO ───────────────────────────────────────────────────────────────
    agregar_parrafo(doc, "Dear Eduardo,")
    doc.add_paragraph()

    # ── PARRAFO 1: Referencia al compromiso incumplido ───────────────────────
    agregar_parrafo(
        doc,
        "Yesterday, March\u00a016, you confirmed receipt of our response to Proposal "
        "25007-PL-0001 rev.1 and committed to providing BW Water\u2019s reply by end of "
        "business. We did not receive it.",
    )
    doc.add_paragraph()

    # ── PARRAFO 2: Dos requerimientos concretos ───────────────────────────────
    agregar_parrafo(
        doc,
        "We require two things from BW Water today:",
    )
    doc.add_paragraph()

    items = [
        (
            "1.",
            "Confirmation that BW Water has started work on the revised drawings "
            "(Piping Layout, Tie-In Points, Equipment Layout, 3D Model) under the "
            "scope ADASA accepted in our March\u00a016 response.",
        ),
        (
            "2.",
            "The updated commercial proposal by end of business today, March\u00a017,\u00a02026, "
            "addressing: (a) technical justification or removal of the three internal-module "
            "drawings (Instrument Layout, Grounding Layout, Cable Tray Layout); "
            "(b) explicit confirmation that the module EX Works date is not affected by this change; "
            "and (c) commercial terms consistent with the delivery history on record.",
        ),
    ]
    for label, text in items:
        para = doc.add_paragraph()
        run_label = para.add_run(label)
        run_label.bold = True
        run_label.font.name = "Arial"
        run_label.font.size = Pt(11)
        run_text = para.add_run(f"  {text}")
        run_text.font.name = "Arial"
        run_text.font.size = Pt(11)
        para.paragraph_format.left_indent = Inches(0.25)

    doc.add_paragraph()

    # ── PARRAFO 3: Consecuencia clara ────────────────────────────────────────
    para = doc.add_paragraph()
    run = para.add_run(
        "If we do not receive the updated proposal today, ADASA will proceed on "
        "Monday, March\u00a020, with a conditional commercial acceptance covering only "
        "the four documents with evident technical dependency. The three internal-module "
        "documents will remain on hold."
    )
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)
    doc.add_paragraph()

    # ── CIERRE ────────────────────────────────────────────────────────────────
    agregar_parrafo(doc, "Please confirm receipt and your availability to respond today.")
    doc.add_paragraph()

    agregar_parrafo(doc, "Best regards,")
    doc.add_paragraph()

    para = doc.add_paragraph()
    run = para.add_run(CONTACTO)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)

    for line in [
        "Project Engineer",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
    ]:
        agregar_parrafo(doc, line)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
