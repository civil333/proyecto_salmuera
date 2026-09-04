#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N10 (P22-TM-09-000-010-0) — Submittal 25007-0018
Fecha: 16 de Marzo de 2026
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-16_Transmittal-N10.docx"
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
        ("Date:", "March 16, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N10 "
            "\u2014 Submittal 25007-0018",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-010-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ── SALUDO ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)
    doc.add_paragraph()

    # ── APERTURA ─────────────────────────────────────────────────────────────
    para = doc.add_paragraph(
        "Please find attached Transmittal N10 (P22-TM-09-000-010-0), covering "
        "Submittal\u00a025007-0018 (6\u00a0documents: I/O List Rev\u00a0B, Data Transfer List Rev\u00a0A, "
        "Control System Architecture Rev\u00a0C, GA Antiscalant Dosing Tank Rev\u00a0A, "
        "GA SIP-09-001 Rev\u00a0A, GA SIP-09-002 Rev\u00a0A). Transmittal verdict: "
    )
    para.add_run("Code\u00a03 \u2014 To Be Revised").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # ── PROGRESO ─────────────────────────────────────────────────────────────
    para = doc.add_paragraph()
    para.add_run("Progress acknowledged: ").bold = True
    para.add_run(
        "The Data Transfer List Rev\u00a0A delivers the complete Modbus TCP/IP memory map, "
        "closing TM\u00a0N7 OBS-03 outstanding since Transmittal\u00a0N3. I/O List Rev\u00a0B "
        "incorporates vibration transmitters, motor RTDs, and the ADASA\u2013module interface "
        "signals. Control System Architecture Rev\u00a0C confirms Ethernet/IP topology and "
        "Digital Power Meter integration."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── OBS LIST ─────────────────────────────────────────────────────────────
    para = doc.add_paragraph()
    para.add_run("Seven MAJOR observations require resolution:").bold = True
    aplicar_arial(para)

    obs_list = [
        (
            "OBS-01 \u2014 Motor temperature tag conflict: ",
            "I/O List uses TE09-002/003/004/005; Data Transfer List maps the same instruments "
            "as TIT09-002/003/004/005. Conflicting assignment of TIT-09-003 between HP\u00a0Pump "
            "bearing and CIP\u00a0Tank. Single tag per instrument required across all documents."
        ),
        (
            "OBS-02 \u2014 Conductivity ranges incompatible with brine: ",
            "CIT-09-001/004/005 remain at 0\u201320\u00a0mS/cm. Expected service conductivities are "
            "65\u2013133\u00a0mS/cm. Raised in TM\u00a0N8; uncorrected in this submittal."
        ),
        (
            "OBS-03 \u2014 DI block error and missing level alarms: ",
            "VE09-014 position feedback appears in DI block (addresses 10002.5\u201310002.6) \u2014 "
            "it is an analog signal already mapped correctly. LS09-001/002 (Antiscalant Tank "
            "Level High/Low) are in the I/O List but absent from the Modbus map."
        ),
        (
            "OBS-04 \u2014 UPS 8-hour autonomy not confirmed: ",
            "Control System Architecture Rev\u00a0C does not confirm the upgrade from 30\u00a0min to "
            "8\u00a0h required in TM\u00a0N7 OBS-01. Written confirmation with capacity calculation required."
        ),
        (
            "OBS-05 \u2014 GA Antiscalant Tank: volume and material absent: ",
            "Notes section empty. Total installed volume, effective volume, and body material "
            "must be specified per accepted datasheet (0.34\u00a0m\u00b3 total)."
        ),
        (
            "OBS-06 \u2014 GA SIP-09-001: monitoring provisions absent: ",
            "No vibration transducer mounting point and no Pt-100 RTD connection on bearing "
            "housing shown on the GA."
        ),
        (
            "OBS-07 \u2014 GA SIP-09-002: same as OBS-06 for the second unit.",
            None
        ),
    ]

    for bold_text, normal_text in obs_list:
        para = doc.add_paragraph(style="List Bullet")
        para.add_run(bold_text).bold = True
        if normal_text:
            para.add_run(normal_text)
        aplicar_arial(para)

    doc.add_paragraph()

    # ── CIERRE ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph(
        "Please confirm receipt and provide a revised submission schedule "
        "covering all open items."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ────────────────────────────────────────────────────────────────
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
