#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N9 (P22-TM-09-000-009-0) — Submittal 25007-0017 (P&ID Rev B)
Fecha: 13 de Marzo de 2026
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

OUTPUT_FILE = "2026-03-13_Transmittal-N9.docx"
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
        ("Date:", "March 13, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N9 "
            "\u2014 Submittal 25007-0017",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-009-0"),
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
        "Please find attached Transmittal N9 (P22-TM-09-000-009-0), covering "
        "Submittal 25007-0017 (1 document: P&ID Rev B). Transmittal verdict: "
    )
    para.add_run("Code 2 \u2014 Approved as Noted").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # P&ID Rev B — progress acknowledged
    para = doc.add_paragraph()
    para.add_run(
        "P&ID Rev B \u2014 substantive progress acknowledged:\n"
    ).bold = True
    para.add_run(
        "Rev B closes all 13 observations raised in TM N2: HP lines confirmed in "
        "Super Duplex SS, battery limits now include flanges, TAGs, and pipe diameters, "
        "1st/2nd stage labels are clearly differentiated, valve and instrument TAGs are "
        "consistent with the lists, and the legend has been revised. Static Mixer tag "
        "MZE-09-001 is now coherent with the accepted datasheet."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # NOTE-01
    para = doc.add_paragraph()
    para.add_run(
        "NOTE-01 \u2014 Document code in title block \u2014 correction required (MINOR):\n"
    ).bold = True
    para.add_run(
        "The title block shows P22-DWG-09-009-02 (2-digit correlative). The P22 coding "
        "system requires 3 digits: P22-DWG-09-009-002. Please correct in Rev C."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # NOTE-02
    para = doc.add_paragraph()
    para.add_run(
        "NOTE-02 \u2014 Antiscalant Tank TK-09-002 \u2014 volume annotation (MINOR):\n"
    ).bold = True
    para.add_run(
        "P&ID Rev B annotates 0.27\u00a0m\u00b3 (effective volume). The accepted datasheet "
        "(TM N4) specifies 0.34\u00a0m\u00b3 total capacity. P&ID convention is to annotate "
        "the total installed volume. Please correct to 0.34\u00a0m\u00b3 in Rev C."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # VM-09-015 residual
    para = doc.add_paragraph()
    para.add_run(
        "VM-09-015 \u2014 Valve List residual inconsistency:\n"
    ).bold = True
    para.add_run(
        "P&ID Rev B shows VM-09-015 (HP Pump to Feed Turbocharger isolation) correctly "
        "as a manual valve \u2014 ADASA formally withdrew TM N3 OBS-11 in the communication "
        "of March\u00a05, 2026. One residual inconsistency remains: Valve List Rev B item\u00a018 "
        "registers VM-09-015 as ON/OFF MOTORIZED, contradicting the confirmed manual function. "
        "Valve List Rev C must resolve this inconsistency."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Link y cierre
    para = doc.add_paragraph("Annotated PDF available at: [LINK_PLACEHOLDER]")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and address the two minor notes in the next P&ID revision."
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
