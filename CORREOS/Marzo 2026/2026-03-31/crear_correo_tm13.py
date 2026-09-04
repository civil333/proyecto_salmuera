#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N13 (P22-TM-09-000-013-0) — Submittal 25007-0024
Fecha: 31 de Marzo de 2026
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-31_Transmittal-N13.docx"
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

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "March 31, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N13 "
            "\u2014 Submittal 25007-0024",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-013-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ── BODY ────────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please find attached Transmittal N13 (P22-TM-09-000-013-0) covering "
        "Submittal 25007-0024. Overall verdict: "
    )
    para.add_run("Code 2 \u2014 Approved as Noted").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "\u2022  Piping and Instrumentation Diagram Rev\u00a0C \u2014 "
    ).bold = True
    para.add_run(
        "Code\u00a02. Transmittal N9 NOTE-01 (title block code) and NOTE-02 "
        "(TK-09-002 antiscalant tank volume) are confirmed closed. "
        "One informational note is raised: TK-09-001 (CIP Tank) is annotated as "
        "6.81\u00a0m\u00b3 in Rev\u00a0C, while Equipment List Rev\u00a0B specifies "
        "6.1\u00a0m\u00b3. Confirmation of the correct installed volume and update "
        "of the P&ID annotation consistent with the Equipment List is requested "
        "prior to IFC (Rev\u00a00)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "ADASA also requests BW Water to confirm expected submission dates for "
        "I/O List Rev\u00a0C, Data Transfer List Rev\u00a0B, and Valve List Rev\u00a0D, "
        "as these carry multiple open Major observations outstanding for more than "
        "18\u00a0days."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Annotated PDF: [ENLACE SYNOLOGY]")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Please confirm receipt.")
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA \u2014 Aguas de Antofagasta S.A."]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
