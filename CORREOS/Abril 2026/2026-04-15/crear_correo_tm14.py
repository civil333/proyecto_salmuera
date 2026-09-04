#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N14 (P22-TM-09-000-014-0)
Submittals 25007-0026 (E26) + 25007-0027 (E27) + 25007-0028 (E28) + 25007-0029 (E29)
Fecha: 15 de Abril de 2026
Veredicto: Code 2 — Approved as Noted
11 documentos, 4 entregas.
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-04-15_Transmittal-N14.docx"
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
        ("Date:", "April 15, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal\u00a0N14 "
            "\u2014 Submittals 25007-0026\u00a0/\u00a025007-0027\u00a0/"
            "\u00a025007-0028\u00a0/\u00a025007-0029",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-014-0"),
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
        "Attached is Transmittal\u00a0N14 (P22-TM-09-000-014-0) covering "
        "Submittals 25007-0026\u00a0(E26), 25007-0027\u00a0(E27), "
        "25007-0028\u00a0(E28), and 25007-0029\u00a0(E29) \u2014 "
        "eleven documents reviewed. Overall verdict: "
    )
    para.add_run("Code\u00a02 \u2014 Approved as Noted").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # §2 — Cierres
    para = doc.add_paragraph(
        "Twelve observations from previous transmittals are closed in this "
        "review: TM\u00a0N10 OBS-01/02/03/04, TM\u00a0N11 "
        "OBS-01/02/NOTE-01, TM\u00a0N12 OBS-01/NOTE-01, and "
        "TM\u00a0N8 OBS-01/02/03."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §3 — Notas nuevas
    para = doc.add_paragraph("Five notes are raised:")
    aplicar_arial(para)

    notes = [
        (
            "NOTE-01 (Major):",
            " Safety relief valve item\u00a0112 removed from Valve List "
            "without overpressure protection justification \u2014 "
            "confirmation required prior to IFC.",
        ),
        (
            "NOTE-02 (Major):",
            " Analyzer power supply voltage discrepancy \u2014 IO List "
            "specifies 220\u00a0VAC while Instrument List specifies 24\u00a0VDC "
            "for five analyzers \u2014 alignment required prior to IFC.",
        ),
        (
            "NOTE-03/04/05 (Minor):",
            " Vibration transmitter calibrated range alignment, working medium "
            "labels for brine-side instruments, and Modbus scaling alignment "
            "\u2014 to be addressed prior to IFC.",
        ),
    ]
    for label, text in notes:
        para = doc.add_paragraph(style="List Bullet" if False else None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run(label).bold = True
        para.add_run(text)
        aplicar_arial(para)

    doc.add_paragraph()

    # §4 — Observaciones abiertas
    para = doc.add_paragraph(
        "Five observations from previous transmittals remain open \u2014 "
        "details in Section\u00a03 of the attached document."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §5 — Link adjuntos
    para = doc.add_paragraph("Annotated PDFs: [LINK_PLACEHOLDER]")
    aplicar_arial(para)
    doc.add_paragraph()

    # §6 — Cierre
    para = doc.add_paragraph(
        "Please confirm receipt and advise on the expected response date."
    )
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
