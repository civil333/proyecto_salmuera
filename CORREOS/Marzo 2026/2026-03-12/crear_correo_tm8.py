#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N8 (P22-TM-09-000-008-0) — Submittals 25007-0015 / 25007-0016
Fecha: 12 de Marzo de 2026
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

OUTPUT_FILE = "2026-03-12_Transmittal-N8.docx"
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
        ("Date:", "March 12, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N8 "
            "\u2014 Submittals 25007-0015 / 25007-0016",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-008-0"),
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
        "Please find attached Transmittal N8 (P22-TM-09-000-008-0), covering "
        "Submittals 25007-0015 and 25007-0016 (11 documents). Transmittal verdict: "
    )
    para.add_run("Code 3 \u2014 To Be Revised").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # Instrument List — progress acknowledged
    para = doc.add_paragraph()
    para.add_run(
        "Instrument List Rev B \u2014 acknowledged progress:\n"
    ).bold = True
    para.add_run(
        "Rev B adds the three vibration transmitters (VT-09-001/002/003) and four "
        "motor RTDs (TE-09-001/002/003/004) requested in previous transmittals. "
        "These additions close two long-standing technical gaps and are acknowledged."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Instrument List — blocking item
    para = doc.add_paragraph()
    para.add_run(
        "Instrument List Rev B \u2014 blocking item (Code 3):\n"
    ).bold = True
    para.add_run(
        "CIT-09-005 (RO Train Reject Conductivity Analyzer) specifies 120VAC power "
        "supply. Every other instrument in the list operates at 24VDC. BW Water must "
        "confirm whether 220VAC was the intended supply voltage (correct the Instrument "
        "List accordingly) or provide the single-line diagram for the 120VAC distribution "
        "circuit. IO List Rev B must also be submitted incorporating the seven new "
        "instruments added in this revision."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Brine conductivity ranges
    para = doc.add_paragraph()
    para.add_run(
        "Brine-side conductivity ranges \u2014 confirmation required:\n"
    ).bold = True
    para.add_run(
        "CIT-09-001 (module feed), CIT-09-004 (Stage\u00a01 reject), and CIT-09-005 "
        "(train reject) specify a maximum calibrated range of 20\u00a0mS/cm. Based on "
        "the design feed TDS of 43,000\u201353,000\u00a0mg/L, expected conductivities "
        "at these three points exceed 65\u00a0mS/cm. BW Water must provide measured "
        "conductivity values for the Taltal brine and correct the calibrated ranges "
        "in Rev\u00a0C if the 20\u00a0mS/cm limit is insufficient."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Power Works DWG
    para = doc.add_paragraph()
    para.add_run(
        "Power Works Installation Drawing Rev A \u2014 no grounding specifications (Code 3):\n"
    ).bold = True
    para.add_run(
        "The document contains no equipment earth conductors, no cable tray bonding "
        "requirements, and no shield termination guidance for instrument cables. Rev B "
        "must include grounding specifications for motors, panels, cable trays, and "
        "instrument cables."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Temperature Transmitter DS
    para = doc.add_paragraph()
    para.add_run(
        "Temperature Transmitter Datasheet Rev A \u2014 TIT-09-003 absent from "
        "Instrument List (Code 3):\n"
    ).bold = True
    para.add_run(
        "The datasheet covers TIT-09-003, a tag not registered in Instrument List "
        "Rev B and with no IO point assigned. BW Water must add TIT-09-003 to the "
        "next IL revision and confirm whether TIT-09-001 and TIT-09-003 are distinct "
        "instruments or one supersedes the other."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Link y cierre
    para = doc.add_paragraph(
        "Annotated PDFs are available at: "
        "https://lrg.synology.me:6501/d/s/17OYEJDhTny4F9uWYd6uiudSdGkRMl9L/"
        "3pHSj9iAesPp2gfz0AMymx8byh_Rc5vY-CLMApYt-CQ0"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and provide a response schedule for Rev B/C submissions."
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
