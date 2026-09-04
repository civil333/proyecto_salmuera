#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: EP-1 + EP-2 Bundle Proposal — Closing pending POs by 31-May-2026
Fecha: 12 de Mayo de 2026 (v2.0 — re-enfoque colaborativo)
Propuesta para presentar EP-1 (10%) + EP-2 (15%) en bundle la primera semana
de Junio, condicionado a cierre de POs Fil-Trek y LG antes de 31-May-2026.
"""

import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.table import WD_TABLE_ALIGNMENT

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-05-12_Procurement-Backup-Request.docx")
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def aplicar_arial_table(table, size=10):
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)


def add_table_with_header(doc, headers, rows):
    """Tabla con header en negrita y bordes (Table Grid)."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = header
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True

    for i, row_data in enumerate(rows, start=1):
        for j, value in enumerate(row_data):
            table.rows[i].cells[j].text = str(value)

    aplicar_arial_table(table, size=10)
    return table


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # HEADER
    fields = [
        ("Date:", "May 12, 2026"),
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
            "ADASA – Taltal Brine Module: Proposal to bundle EP-1 + EP-2 "
            "milestones — closing pending POs by 31-May-2026",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803, Clause 31"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # OPENING
    para = doc.add_paragraph("Dear Eduardo,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Following the Procurement Review of 05-May-2026 and the tracker "
        "shared for the week ending 11-May-2026, we have audited the "
        "documentary coverage of the seven main equipment categories listed "
        "in BAE Clause 31, which together gate Payment Milestone EP-2 (15% "
        "of contract). At the same time, BW Water has flagged the upcoming "
        "request for EP-1 (10%, formal engineering approval). This note "
        "proposes a coordinated approach to present both milestones together "
        "in the first week of June."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # AUDIT TABLE
    para = doc.add_paragraph()
    para.add_run(
        "Audit summary — EP-2 documentary coverage (BAE Clause 31)"
    ).bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=["#", "Equipment", "Coverage", "Source"],
        rows=[
            ("1", "High Pressure Pump", "OK",
             "Fedco package (PO M183, delivered 08-May)"),
            ("2", "Energy Recovery (ERD)", "OK",
             "Fedco package (PO M183, delivered 08-May)"),
            ("3", "Cartridge Filters", "Pending",
             "Fil-Trek — tracker items 8 and 18 in status E"),
            ("4", "Pressure Vessels", "OK",
             "Protec Arisawa (PO M184, delivered 20-Apr)"),
            ("5", "RO Membranes", "Pending",
             "LG — tracker item 19 in status E, no PO date"),
            ("6", "Dosing System", "OK",
             "ProMinent (PO M089) + Promatics (PO M074)"),
            ("7", "CIP System", "OK",
             "Quantic Logic heater (PO M062) + Dayamas tank (PO M073)"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Five categories are fully covered with unpriced PO PDFs already on "
        "file. Two categories remain open: Cartridge Filters (Fil-Trek) and "
        "RO Membranes (LG)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # PROPOSAL
    para = doc.add_paragraph()
    para.add_run("Proposal").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "If BW Water can secure the two pending POs and share the "
        "corresponding unpriced PDFs before 31-May-2026, both milestones "
        "could be presented in bundle the first week of June:"
    )
    aplicar_arial(para)

    bullets_proposal = [
        ("EP-1 (10%) — ",
         "formal engineering approval, currently being closed by ADASA in "
         "parallel with the open technical observations."),
        ("EP-2 (15%) — ",
         "triggered by the seven PO confirmations once EP-1 is signed."),
    ]
    for bold_part, normal_part in bullets_proposal:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(bold_part).bold = True
        para.add_run(normal_part)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "A single bundled presentation streamlines BW Water's cash flow on "
        "the contract (25% released in one administrative cycle) and gives "
        "ADASA a clean compliance closure on both milestones."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # SPECIFIC QUESTIONS
    para = doc.add_paragraph()
    para.add_run(
        "Specific questions on the two pending items (tracker SEMANA "
        "11-May-2026)"
    ).bold = True
    aplicar_arial(para)

    questions = [
        ("Cartridge Filters — Fil-Trek (items 8 and 18): ",
         "the tracker shows PO dates 14-May-2026 (CIP) and 05-May-2026 (RO) "
         "with status E and the remark \"Nego on leadtime with vendor still "
         "ongoing\". Could you confirm whether these POs will be issued and "
         "the unpriced PDFs shared with ADASA before 31-May-2026?"),
        ("RO Membranes — LG (item 19): ",
         "the tracker shows status E with no PO date. Given that the "
         "baseline window closed on 27-Apr-2026, this is the critical item "
         "for the bundle. Could you provide a target PO date from LG and "
         "indicate whether 31-May-2026 is achievable?"),
    ]
    for bold_part, normal_part in questions:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(bold_part).bold = True
        para.add_run(normal_part)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "If either vendor cannot commit to the May deadline, please "
        "indicate the realistic target so we can plan the EP-2 presentation "
        "accordingly."
    )
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
