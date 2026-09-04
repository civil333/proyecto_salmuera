#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water: cobertura de la Nota Tecnica P22-NT-09-000-002-0
(Designation of Third-Party Shop Inspector and Inspection Schedule).

- Hilo NUEVO iniciado por ADASA (no Reply-To) — cadena separada de los TM y del
  thread del Notice of Delay del PLC (ese lo responde el correo D3).
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Transaccional (~110 palabras): transmite la NT, pide el calendario H/W + KoM,
  NO repite la sustancia de la NT.
- Fuente unica del cuerpo: 2026-07-07_Third-Party-Shop-Inspection-Notice_Descripcion.md
"""

import os
import sys

from docx import Document
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-07_Third-Party-Shop-Inspection-Notice.docx"
)
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_para(doc, text, size=11):
    para = doc.add_paragraph(text)
    aplicar_arial(para, size)
    return para


def add_segments(doc, segments, size=11):
    para = doc.add_paragraph()
    for text, bold in segments:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def add_bullet(doc, text, size=11):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    run = para.add_run("•  " + text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def blank(doc):
    doc.add_paragraph()


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ---- HEADER -------------------------------------------------------------
    fields = [
        ("Date:", "July 7, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Andrew Sia, Victor Gutierrez, Jeryl F. Regulacion, "
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, "
            "Tanya Figueroa, Allan Valentos, Sadeep Irugalbandara, "
            "Ghazi Ozair, Nick Huta, Marjan Arsovic, "
            "Adzlan Bin Abd Rahim, Stephane Gehant",
        ),
        ("Subject:",
         "25007 Taltal - Designation of Third-Party Shop Inspector and "
         "Inspection Schedule"),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / "
            "Technical Note P22-NT-09-000-002-0 / "
            "Inspection and Test Plan P22-BA-09-000-004 Rev 0",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # ---- CUERPO -------------------------------------------------------------
    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_segments(
        doc,
        [
            ("Please find attached Technical Note ", False),
            ("P22-NT-09-000-002-0", True),
            (", by which ADASA designates Bureau Veritas as its Third-Party "
             "Inspector for the shop fabrication and Factory Acceptance Test "
             "of the module at Penang, and communicates the planned inspection "
             "schedule (six weekly quality-surveillance visits during "
             "fabrication plus the FAT witnessing), under the Bases "
             "Administrativas Especiales.", False),
        ],
    )
    blank(doc)

    add_segments(
        doc,
        [
            ("To align attendance, we ask BW Water to provide a consolidated "
             "Hold Point and Witness Point notification calendar and to "
             "confirm a Kick-off Meeting with ADASA and the inspector, by ",
             False),
            ("end of business Friday 17 July 2026", True),
            (", so we can review it at the weekly meeting of Tuesday 21 July. "
             "The Note details the scope, the schedule and the notification "
             "protocol.", False),
        ],
    )
    blank(doc)

    add_para(
        doc,
        "Separately, three quality procedures that govern tests the inspector "
        "must witness are currently returned as Code 3 (to be revised) and are "
        "required approved at the earliest, ahead of the pressure and coating "
        "test windows (from mid-August):",
    )
    add_bullet(
        doc,
        "RO Vessel Hydrostatic Test Procedure (P22-BA-09-000-009) — last "
        "returned Code 3 in Transmittal N26 (P22-TM-09-000-026-0).",
    )
    add_bullet(
        doc,
        "HP and LP Pressure Test Procedure (P22-BA-09-000-010) — last returned "
        "Code 3 in Transmittal N26 (P22-TM-09-000-026-0).",
    )
    add_bullet(
        doc,
        "Painting Procedure (P22-BA-09-000-011) — returned Code 3 in "
        "Transmittal N23 (P22-TM-09-000-023-0) and not yet resubmitted.",
    )
    blank(doc)

    add_para(doc, "We look forward to your comments.")
    blank(doc)

    # ---- CIERRE -------------------------------------------------------------
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA — Aguas de Antofagasta S.A."]:
        add_para(doc, line)

    blank(doc)
    para = doc.add_paragraph()
    run = para.add_run(
        "Attachment: Technical Note P22-NT-09-000-002-0 "
        "(Designation of Third-Party Shop Inspector and Inspection Schedule)."
    )
    run.italic = True
    run.font.name = "Arial"
    run.font.size = Pt(10)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="Third-Party Shop Inspection - Designation and Schedule",
        author="ADASA",
        last_modified_by="ADASA",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
