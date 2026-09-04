#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N16 (P22-TM-09-000-016-0)
Submittal 25007-0034 (Entrega 34) - Civil and Loading Drawing Rev A
Fecha: 24 de Abril de 2026
Veredicto: Code 2 - Approved as Noted
1 documento, 1 NOTE (MAJOR).
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-04-24_Transmittal-N16.docx"
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
        ("Date:", "April 24, 2026"),
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
            "ADASA – Taltal Brine Module: Technical Review Transmittal N16 "
            "— Submittal 25007-0034 (Civil and Loading Drawing Rev A)",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-016-0"),
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

    para = doc.add_paragraph(
        "Attached: Transmittal N16 (P22-TM-09-000-016-0) — Civil and "
        "Loading Drawing Rev A (Submittal 25007-0034, first submission)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Verdict: Code 2 — Approved as Noted.").bold = True
    para.add_run(
        " Rev 0 (IFC) to include: (a) total weight of the modified 40 ft "
        "container; (b) confirmation that the RO Skid operating weight "
        "(8,058 kg) covers all interior piping, fluid inventory, skid "
        "frame, pressure vessels and wet membranes — declare any mass "
        "excluded. Detail on the attached CC_ADASA PDF."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and target IFC date."
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
