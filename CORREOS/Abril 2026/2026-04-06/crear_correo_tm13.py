#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N13 (P22-TM-09-000-013-0)
Submittals 25007-0024 (P&ID Rev C) + 25007-0025 (Power Works Rev B)
Fecha: 06 de Abril de 2026
Veredicto: Code 2 — Approved as Noted
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-04-06_Transmittal-N13.docx"
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
        ("Date:", "April 6, 2026"),
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
            "\u2014 Submittals 25007-0024 / 25007-0025",
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

    # §1 — Apertura
    para = doc.add_paragraph(
        "Attached is Transmittal\u00a0N13 (P22-TM-09-000-013-0) covering "
        "Submittals\u00a025007-0024 (P&ID Rev\u00a0C) and 25007-0025 (Power Works "
        "Installation Details Rev\u00a0B). Overall verdict: "
    )
    para.add_run("Code\u00a02 \u2014 Approved as Noted").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # §2 — Resumen ejecutivo
    para = doc.add_paragraph(
        "Four open observations from previous transmittals are closed: "
        "TM\u00a0N8 OBS-01 and OBS-02 (Power Works grounding specifications and "
        "installation standard), TM\u00a0N9 NOTE-01 and NOTE-02 (P&ID title block "
        "and antiscalant tank volume). Four informational notes are raised in this "
        "transmittal \u2014 details in the attached document."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §3 — Link
    para = doc.add_paragraph("Annotated PDFs: [LINK_PLACEHOLDER]")
    aplicar_arial(para)
    doc.add_paragraph()

    # §4 — Cierre
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
    for line in [
        "Project Engineer",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
