#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N18 (P22-TM-09-000-018-0)
Submittals 25007-0038 (E38), 25007-0039 (E39), 25007-0040 (E40)
Fecha: 18 de Mayo de 2026
Veredicto: 3 - TO BE REVISED (driven by Plant Control Philosophy Rev C)
5 documentos. Re-disposicion 18-May: 4 Code 1 + 1 Code 3 (solo
Control Philosophy Code 3). 1 CC_ADASA adjunto. Estado: BORRADOR.
"""

import os
from docx import Document
from docx.shared import Pt, Inches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-05-18_Transmittal-N18.docx")
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
        ("Date:", "May 18, 2026"),
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
            "ADASA – Taltal Brine Module: Technical Review Transmittal N18 "
            "— Submittals 25007-0038 to 25007-0041",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-018-0"),
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
        "Attached: Transmittal N18 (P22-TM-09-000-018-0), submittals "
        "25007-0038 to 25007-0041 — five documents."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Verdict: 3 — To Be Revised.").bold = True
    para.add_run(" Tally: 4 Code 1, 1 Code 3. Only ")
    para.add_run("Plant Control Philosophy Rev C").bold = True
    para.add_run(
        " requires a new revision (Rev D); the other four documents are "
        "approved as-is, with residual deliverables listed in Section 3 "
        "of the transmittal."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "Plant Control Philosophy Rev C — re-issue as Rev D:"
    ).bold = True
    aplicar_arial(para)

    cp_bullets = [
        (
            "HP Pump start permissive (repeat CRITICAL).",
            " Still \"VE-09-007 and VE-09-007\" (not corrected to "
            "VE-09-008) and requires \"VE-09-014 fully CLOSED\" — "
            "VE-09-014 is the antiscalant tank inlet valve, so the PLC "
            "blocks HP Pump start during routine refill. Same defect as "
            "Transmittal N15 NOTE-20, second consecutive transmittal; "
            "recorded for contractual follow-up under Contract C-4300.",
        ),
        (
            "Core control logic in undelivered child documents.",
            " Sequence Charts, Alarm & Control Setpoint List and "
            "Control Matrix remain \"SEPARATE DOCUMENT\"; the "
            "13-May-2026 tentative date passed. Deliver them with "
            "formal codes, revisions and a binding date.",
        ),
    ]
    for bold_part, rest in cp_bullets:
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(bold_part).bold = True
        para.add_run(rest)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "Approved as-is (Code 1) — deliverables tracked in Section 3:"
    ).bold = True
    para.add_run(
        " Valve List Rev D (PSV-09-002 overpressure analysis); P&ID "
        "Rev D (closes TM N13 NOTE-01; CIT-09-004 → Instrument List / "
        "Line List + loop-response note); AC Thermal Calculation Rev C "
        "(closes TM N15 NOTE-02; explicit margin statement); Line List "
        "Rev C (closes the two TM N12 notes)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "One annotated PDF is attached (Plant Control Philosophy "
        "Rev C); the four Code 1 documents carry none."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and the target dates for Plant Control "
        "Philosophy Rev D and the Section 3 deliverables."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("We look forward to your comments.")
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
