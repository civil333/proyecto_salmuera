#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N21 (P22-TM-09-000-021-0). Submittal 25007-0048 (E48).
Fecha: 11 de Junio de 2026.
Veredicto TM N21: 3 - TO BE REVISED. Tally 1 Code 2 + 1 Code 3 (2 documentos).
Driver Code 3: Datasheet of PLC and HMI Panel Component Rev B (Section 2.2, HART).
Cierre positivo: Grounding Layout Rev F (schedule embebido, ~88 dias) Code 2.
2 CC_ADASA adjuntos (1 Code 3 + 1 Code 2). English, BW Water.
"""

import os
from docx import Document
from docx.shared import Pt, Inches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-06-11_Transmittal-N21.docx")
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

    fields = [
        ("Date:", "June 11, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, "
            "Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, "
            "Andrew Zaske, Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "ADASA – Taltal Brine Module: Technical Review Transmittal N21 "
            "(25007-0048)",
        ),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / P22-TM-09-000-021-0",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Attached: ")
    para.add_run("Transmittal N21").bold = True
    para.add_run(
        " (P22-TM-09-000-021-0) covering submittal 25007-0048 — the "
        "Grounding Point & Power Panel Location Layout Rev F and the "
        "Datasheet of PLC and HMI Panel Component Rev B — for ADASA's "
        "technical review."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Verdict: 3 — To Be Revised.").bold = True
    para.add_run(
        " Tally: 1 Code 1, 1 Code 3. The verdict is driven by the Datasheet "
        "of PLC and HMI Panel Component Rev B (Section 2.2)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Positive closure in this cycle: ").bold = True
    para.add_run("Grounding Point & Power Panel Location Layout Rev F").bold = True
    para.add_run(
        " is Code 1 — Approved. The drawing was returned ahead of its "
        "17-Jun commitment with the grounding schedule now embedded as a "
        "complete 48-conductor table, closing the schedule item carried open "
        "since Transmittal N11 (about 88 days, the longest-standing item of "
        "the electrical package). Note 5 has been removed, the conductor "
        "sizing is unified to IEC 60364-5-54, and the Comment Sheet is "
        "legible. It issues directly at IFC Rev 0, with the revision-history "
        "descriptions completed as part of that issuance."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Driver requiring action by BW Water:").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    para.add_run("• ")
    para.add_run(
        "Datasheet of PLC and HMI Panel Component Rev B (Section 2.2)."
    ).bold = True
    para.add_run(
        " The CompactLogix 5380 controller, the PanelView Plus 7 HMI and the "
        "discrete and analog I/O selections are accepted, and the Modbus "
        "query of Transmittal N1 is answered by the Control System "
        "Architecture Rev B gateway. Re-issue as Rev C to: (a) provide a "
        "HART acquisition path for the 4-20 mA + HART instrumentation "
        "required by the Technical Specification — the committed 5069-IF8 "
        "analog input reads 4-20 mA only and the rack carries no "
        "HART-capable input nor a HART multiplexer — or submit the "
        "engineering justification for its omission; (b) incorporate the two "
        "5069-IY4 RTD modules so the module list matches the project rack "
        "declared in the Local Control Panel Datasheet Rev B and the "
        "Schematic; and (c) correct the \"PD Tattal\" cover typo."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "One annotated PDF is attached, for the Code 3 datasheet. The "
        "Grounding Layout Rev F is Code 1 — Approved and carries no "
        "annotation."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "We also remain awaiting the Section 3 items: Plant Control "
        "Philosophy Rev D (now a fifth consecutive cycle), the PLC-LCP "
        "Outline Panel Drawing Rev B, the ITP Rev C with the RO pressure "
        "vessel test scope, and the Cartridge Filters with the FAT/SAT table "
        "due 15-Jun."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt and the target date for the Datasheet Rev C."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("We look forward to your comments.")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA — Aguas de Antofagasta S.A."]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
