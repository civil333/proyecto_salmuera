#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N11 (P22-TM-09-000-011-0) — Submittals 25007-0019 / 25007-0020 / 25007-0021
Fecha: 17 de Marzo de 2026
"""

import sys
import os

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-17_Transmittal-N11.docx"
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
        ("Date:", "March 17, 2026"),
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
            "ADASA \u2013 Taltal Brine Module: Technical Review Transmittal N11 "
            "\u2014 Submittals 25007-0019 / 25007-0020 / 25007-0021",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-011-0"),
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

    # §1 — Apertura directa
    para = doc.add_paragraph(
        "Attached is Transmittal N11 (P22-TM-09-000-011-0) \u2014 "
        "Submittals 25007-0019/0020/0021, 10 documents received March 13\u201316. "
        "Verdict: "
    )
    para.add_run("Code 3 \u2014 To Be Revised").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    # §2 — Progress acknowledged
    para = doc.add_paragraph()
    para.add_run("Progress acknowledged \u2014\n").bold = True
    para.add_run(
        "\u2022  Coupling pressure (TM N6 OBS-01): closed for HP Feed Pump and both "
        "Turbochargers. Rev D confirms 2,000\u00a0psi (Victaulic/Piedmont Style H) "
        "and 1,800\u00a0psi respectively.\n"
        "\u2022  Vibration mounting (TM N10 OBS-06/07): closed for SIP-09-001 and "
        "SIP-09-002.\n"
        "\u2022  Equipment List Rev B and Painting Specifications Rev B: approved "
        "(Codes 2 and 1).\n"
        "\u2022  Instrument Location Layout Rev B: eight CCS items from TM N3 "
        "addressed \u2014 progress acknowledged."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §3 — Blocking items
    para = doc.add_paragraph()
    para.add_run("Blocking \u2014 Code 3 documents:\n").bold = True
    para.add_run("\u2022  ")
    para.add_run("Valve List Rev D required:").bold = True
    para.add_run(
        " Rev C closes the four TM N6 duplicates but introduces two new ones: "
    )
    para.add_run("VE-09-007").bold = True
    para.add_run(" (items 44 and 64) and ")
    para.add_run("PSV-09-002").bold = True
    para.add_run(
        " (items 105 and 112). Each pair is distinct physical equipment. "
        "Duplicate TAGs are not acceptable \u2014 PLC addressing requires unique "
        "identifiers. Area-code error "
    )
    para.add_run("VM-07-005").bold = True
    para.add_run(
        " (area 07 instead of 09) remains open since TM N3. Verify VM-07-031 "
        "and VE-07-009 as well. Rev D must resolve all three items and update "
        "P&ID and I/O List accordingly.\n"
        "\u2022  "
    )
    para.add_run("Grounding Layout Rev B (OBS-03) and Instrument Location Layout Rev B (OBS-04):").bold = True
    para.add_run(
        " Rev B reflects the non-conforming Piping Layout arrangement "
        "(11,150\u00a0mm, rejected in Transmittal N7 vs. \u22643,500\u00a0mm "
        "required per Transmittal N5). Both must be resubmitted as Rev C after "
        "Piping Layout and Equipment Layout are accepted by ADASA."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §4 — Still open from TM N10
    para = doc.add_paragraph()
    para.add_run("Still open from Transmittal N10 (6 items):\n").bold = True
    para.add_run(
        "\u2022  OBS-01/02/03: I/O List Rev C and Data Transfer List Rev B "
        "not received.\n"
        "\u2022  OBS-04: Written UPS 8-hour autonomy confirmation not received.\n"
        "\u2022  OBS-05: Antiscalant Tank GA Rev B not received.\n"
        "\u2022  NOTE-05: HMI Screenshots (P22-BREAD-09-008-001) outstanding since "
        "Transmittal N4."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §5 — Link
    para = doc.add_paragraph(
        "Annotated PDFs: "
        "https://lrg.synology.me:6501/d/s/17StdrqJS7PBtOzufYhqKIs6s2L0Zbxc/"
        "pgUYS7BQFGa5Ps7o45R4tPehfzJXL1-B-yrBgooDcDA0"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # §6 — Cierre
    para = doc.add_paragraph(
        "Please confirm receipt and provide a schedule for the required resubmittals."
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
