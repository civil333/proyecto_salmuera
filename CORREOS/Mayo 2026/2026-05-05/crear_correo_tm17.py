#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N17 (P22-TM-09-000-017-0)
Submittals 25007-0035 (E35), 25007-0036 (E36), 25007-0037 (E37)
Fecha: 5 de Mayo de 2026
Veredicto: 3 - TO BE REVISED (driven by Alarm List Rev A + PQP Rev A)
9 documentos revisados.
"""

import os
from docx import Document
from docx.shared import Pt, Inches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-05-05_Transmittal-N17.docx")
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
        ("Date:", "May 5, 2026"),
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
            "ADASA – Taltal Brine Module: Technical Review Transmittal N17 "
            "— Submittals 25007-0035, 25007-0036 and 25007-0037",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-017-0"),
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
        "Attached: Transmittal N17 (P22-TM-09-000-017-0) covering "
        "submittals 25007-0035, 25007-0036 and 25007-0037 — nine "
        "documents reviewed."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Verdict: 3 — To Be Revised.").bold = True
    para.add_run(
        " Tally: 7 Code 2, 2 Code 3 (Alarm & Interlock List Rev A and "
        "Project Quality Plan Rev A — Rev B required for both before IFC)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Critical findings:")
    aplicar_arial(para)

    bullets = [
        (
            "Alarm & Interlock List Rev A",
            " — permeate conductivity setpoints on CIT-09-002 and "
            "CIT-09-003 sit two orders of magnitude above the operating "
            "range; unit error mS/cm vs µS/cm.",
        ),
        (
            "Project Quality Plan Rev A",
            " — corporate template (form QAM-PQP-001, inherited dates "
            "Issue 16-JUN-2025 / Effective 17-JUL-2025) does not close "
            "the PIE Base inspection matrix; no procedure codes, no "
            "Hold Points, no FAT section.",
        ),
        (
            "Pressure Transmitter Datasheet Rev B",
            " — Hastelloy C extended to PIT-09-001/002/003/004/005/006/008. "
            "Confirm cost and lead-time impact on the Procurement Schedule "
            "in writing.",
        ),
        (
            "Grounding Layout Rev D",
            " — embedded Consolidated Comment Sheet belongs to Cable Tray "
            "Layout (P22-DWG-09-007-004); replace and populate the "
            "revision history block.",
        ),
    ]
    for bold_part, rest in bullets:
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(bold_part).bold = True
        para.add_run(rest)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "Detailed observations on the transmittal and the nine attached "
        "CC_ADASA PDFs."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and target dates for the two Rev B "
        "submissions (Alarm & Interlock List and PQP)."
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
