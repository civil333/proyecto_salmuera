#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N12 (P22-TM-09-000-012-0) — Submittals 25007-0022 / 25007-0023
Fecha: 30 de Marzo de 2026
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-30_Transmittal-N12.docx"
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
        ("Date:", "March 30, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N12 "
            "\u2014 Submittals 25007-0022 / 25007-0023",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-012-0"),
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
        "Please find attached Transmittal N12 (P22-TM-09-000-012-0) covering "
        "Submittals 25007-0022 and 25007-0023. Overall verdict: "
    )
    para.add_run("Code 3 \u2014 To Be Revised").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "\u2022  Datasheet of Vibration Transmitter Rev\u00a0A \u2014 "
    ).bold = True
    para.add_run(
        "Code\u00a03. HART communication capability is not documented in the "
        "submitted datasheet. Rev\u00a0B must either confirm HART support with "
        "manufacturer evidence, propose a HART-capable alternative, or submit a "
        "formal deviation prior to procurement.\n"
    )
    para.add_run("\u2022  Line List Rev\u00a0B \u2014 ").bold = True
    para.add_run(
        "Code\u00a02, Approved as Noted. TM\u00a0N3 OBS-01 closed. "
        "Two notation notes to be incorporated prior to IFC."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Annotated PDFs: [ENLACE SYNOLOGY]")
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
