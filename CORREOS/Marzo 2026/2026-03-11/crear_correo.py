#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N7 (P22-TM-09-000-007-0) — Submittal 25007-0014
Fecha: 11 de Marzo de 2026
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import set_table_borders, calcular_anchos_columnas

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-11_Transmittal-N7.docx"
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
        ("Date:", "March 11, 2026"),
        ("From:", f"{CONTACTO} \u2014 Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        ("CC:", "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim"),
        ("Subject:", "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N7 \u2014 Submittal 25007-0014"),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-007-0"),
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
        "Please find attached Transmittal N7 (P22-TM-09-000-007-0), corresponding to your "
        "Submittal 25007-0014 (4 documents). All four documents received a verdict of "
    )
    para.add_run("Code 3 \u2014 To Be Revised").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # Control Philosophy findings
    para = doc.add_paragraph()
    para.add_run("Control Philosophy Rev A \u2014 12 observations, 3 priority findings:\n").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("UPS Backup Duration: ").bold = True
    para.add_run(
        "The Control Philosophy specifies a 30-minute UPS backup for the module control system. "
        "ET \u2014 Communication and Control System requires a minimum of 8 hours of uninterrupted operation. "
        "This is a direct non-conformance with the contractual baseline and must be corrected in Rev B."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("CEE/MVE Not Described: ").bold = True
    para.add_run(
        "The Energy Efficiency Control (CEE) and Energy Recovery Verification (MVE) functions are listed in "
        "ET \u2014 Communication and Control System as contractual guarantees, but are absent from the Control Philosophy. "
        "Without a documented description of these functions, ADASA cannot verify contractual compliance during commissioning."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Enable Permissive Interface: ").bold = True
    para.add_run(
        "The Control Philosophy defines two individual DI signals (tank level high, tank level low) as the module "
        "start permissive. The correct interface, as confirmed by both parties, is: one DI relay contact "
        "(ADASA \u2192 module: general enable) and one DO relay contact (module \u2192 ADASA: operational status). "
        "The current definition does not match the agreed signal interface per "
        "ET \u2014 Communication and Control System and IO List Rev A."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Piping Layout
    para = doc.add_paragraph()
    para.add_run("Piping Layout \u2014 distance non-conformance:\n").bold = True
    para.add_run(
        "CIP connections and dosing points are located at 11,150 mm from the module boundary \u2014 "
        "more than three times the 3.5 m limit established in Transmittal N5. "
        "Additionally, sliding door access and equipment maintenance clearances are not shown on the layout."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Overdue items
    para = doc.add_paragraph()
    para.add_run("Overdue items from previous transmittals:\n").bold = True
    para.add_run("\u2022 Modbus Memory Map (TM N2): ")
    para.add_run("65 days overdue").bold = True
    para.add_run(" \u2014 no response received.\n")
    para.add_run("\u2022 IO List (TM N3): ")
    para.add_run("44 days overdue").bold = True
    para.add_run(" \u2014 no response received.")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Annotated PDFs are available at: http://gofile.me/7k8qL/RHWabtKCE"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt of this transmittal and provide a response schedule for Rev B submissions."
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
