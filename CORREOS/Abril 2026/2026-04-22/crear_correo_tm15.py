#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N15 (P22-TM-09-000-015-0)
Submittals 25007-0030 (E30) + 25007-0031 (E31) + 25007-0032 (E32) + 25007-0033 (E33)
Fecha: 22 de Abril de 2026
Veredicto: Code 3 - To be Revised
10 documentos, 4 entregas. Tally: 1 Code 1 + 6 Code 2 + 3 Code 3.
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-04-22_Transmittal-N15.docx"
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # HEADER
    fields = [
        ("Date:", "April 22, 2026"),
        ("From:", f"{CONTACTO} — Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc."),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, "
            "Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "ADASA – Taltal Brine Module: Technical Review Transmittal N15 "
            "— Submittals 25007-0030 / 25007-0031 /"
            " 25007-0032 / 25007-0033",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-015-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # BODY
    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)
    doc.add_paragraph()

    # Apertura + veredicto
    para = doc.add_paragraph(
        "Attached is Transmittal N15 (P22-TM-09-000-015-0) covering "
        "Submittals 25007-0030 to 25007-0033 — ten documents from "
        "deliveries E30 to E33 (April 16–22)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Overall verdict: ")
    para.add_run("Code 3 — TO BE REVISED").bold = True
    para.add_run(". Tally: 1 Code 1, 6 Code 2, 3 Code 3.")
    aplicar_arial(para)
    doc.add_paragraph()

    # Code 3 docs
    para = doc.add_paragraph("Three documents require formal resubmittal:")
    aplicar_arial(para)

    code3_items = [
        (
            "LCP Datasheet Rev A:",
            " cover sheet incomplete (IP rating, RTD count, dimensions, "
            "weight blank).",
        ),
        (
            "Cable Tray Layout Rev B:",
            " five new ADASA observations plus two inherited from "
            "Transmittal N4 (78 days outstanding).",
        ),
        (
            "Plant Control Philosophy Rev B:",
            " 17 notes including one CRITICAL (HP Pump permissive contains "
            "erroneous TAGs) following an independent multi-disciplinary audit.",
        ),
    ]
    for label, text in code3_items:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run(label).bold = True
        para.add_run(text)
        aplicar_arial(para)

    doc.add_paragraph()

    # Cierres
    para = doc.add_paragraph("Key closures and ADASA-side decisions:")
    aplicar_arial(para)

    closures = [
        (
            "",
            "The 3,500 mm CIP/dosing footprint constraint "
            "(Transmittal N5/N7) is ",
            "withdrawn",
            " — superseded by ADASA-side perimeter interconnection "
            "drawing P22-DWG-06-006-101.",
        ),
        (
            "",
            "Equipment Layout Rev B accepted as noted; the Operating "
            "Weight table is to be embedded in Rev 0 (IFC). The Civil "
            "Loading drawing committed for April 23 is accepted as a "
            "separate supporting deliverable.",
            "",
            "",
        ),
        (
            "",
            "AC Thermal Calculation Rev C closes Transmittal N2 "
            "OBS-02 (180+ days).",
            "",
            "",
        ),
    ]
    for _, pre, bold, post in closures:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run(pre)
        if bold:
            para.add_run(bold).bold = True
        if post:
            para.add_run(post)
        aplicar_arial(para)

    doc.add_paragraph()

    # Adjuntos
    para = doc.add_paragraph(
        "Detailed per-document comments are in the ten annotated CC_ADASA "
        "PDFs referenced in Section 4 of the attached transmittal."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Cierre
    para = doc.add_paragraph(
        "Please confirm receipt and advise on the expected resubmittal date "
        "for the three Code 3 documents."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # FIRMA
    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Project Engineer",
        "ADASA — Aguas de Antofagasta S.A.",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
