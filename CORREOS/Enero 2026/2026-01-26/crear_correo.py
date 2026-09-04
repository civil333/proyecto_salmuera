#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Technical Review Transmittal N2
"""

import sys
from pathlib import Path

# Agregar skill template-adasa al path
skill_path = str(
    Path(__file__).resolve().parent.parent.parent
    / ".claude"
    / "skills"
    / "template-adasa"
)
sys.path.insert(0, skill_path)

from config_defaults import DEFAULTS
from table_utils import set_table_borders, calcular_anchos_columnas, add_simple_table

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


# set_table_borders importada de table_utils (incluye centrado automatico)


def aplicar_arial(paragraph, size=11):
    """Aplica formato Arial al parrafo"""
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def crear_correo():
    """Genera el correo en formato DOCX"""

    output_file = "2026-01-26_Technical-Review-Transmittal-N2.docx"

    doc = Document()

    # Configurar margenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Header
    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("January 27, 2026")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("From: ").bold = True
    para.add_run(f"{DEFAULTS['contacto_nombre']} ({DEFAULTS['contacto_empresa']})")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("To: ").bold = True
    para.add_run("BW Water Team")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Subject: ").bold = True
    para.add_run(
        "P22-TM-09-000-002-0 | Technical Review Transmittal N2 - Submittals 0003-0007"
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # Body
    para = doc.add_paragraph("Dear BW Water Team,")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "Please find attached the Technical Review Transmittal N2 (P22-TM-09-000-002-0) covering Submittals 0003 through 0007."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Key Highlights:").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "Process Calculation Rev B (P22-CD-09-009-001-B) has been reviewed and "
    )
    run = para.add_run("validates critical design parameters")
    run.bold = True
    para.add_run(", including:")
    aplicar_arial(para)

    bullets = [
        "Design pressures with 10% margin (Stage 1: 70 bar, Stage 2: 85 bar)",
        "Turbocharger modeling for 43k and 53k TDS scenarios",
        "Membrane configuration (70 elements total)",
        "Permeate quality guarantee (TDS < 500 mg/L)",
    ]
    for bullet in bullets:
        para = doc.add_paragraph(bullet, style="List Bullet")
        aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "This validation allows closure of previously blocking observations on P&ID and equipment datasheets."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Pending Critical Actions:").bold = True
    aplicar_arial(para)

    # Table
    table = doc.add_table(rows=6, cols=4)
    set_table_borders(table)

    actions = [
        ("#", "Document", "Issue", "Severity"),
        (
            "1",
            "A/C Thermal Calc",
            "Heat load 5.96 kW vs ~10-12 kW (missing PLC, lighting, wall transmission, solar)",
            "HIGH",
        ),
        (
            "2",
            "A/C Thermal Calc",
            "Missing n+1 redundant unit per ET 5.1.11 and Offer (2 A/C 1W+1S)",
            "HIGH",
        ),
        (
            "3",
            "A/C Thermal Calc",
            "No safety margin included (typical 10-15%)",
            "MEDIUM",
        ),
        (
            "4",
            "Static Mixer",
            "Material change FRP to PVC requires justification",
            "MEDIUM",
        ),
        (
            "5",
            "Control Architecture",
            "Provide Modbus TCP memory map for DCS integration",
            "MEDIUM",
        ),
    ]

    for i, row_data in enumerate(actions):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    if i == 0:
                        run.bold = True

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("A detailed heat load analysis has been included in the transmittal.")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Download Link for Reviewed Documents:").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    run = para.add_run("https://www.dropbox.com/t/INLfLK7p4ISQiAnz")
    run.font.underline = True
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please do not hesitate to contact us should you have any questions."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(DEFAULTS["contacto_nombre"]).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph("ADASA - Aguas de Antofagasta S.A.")
    aplicar_arial(para)

    para = doc.add_paragraph("Project: BAE 12803 - Second Stage RO Brine Module")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Attachments:").bold = True
    aplicar_arial(para)

    attachments = [
        "TRANSMITTAL N2 ADASA-BW_WATER.docx",
        "P22-DWG-09-009-002_A - P&ID Coment LH.pdf",
        "P22-ET-09-009-001-B Datasheet of UHPRO System Coment LH.pdf",
        "P22-ET-09-009-003-B_Datasheet of RO CIP Pump Coment LH.pdf",
        "P22-ITEM-09-009-012-A_Datasheet of Static Mixer Coment LH.pdf",
        "P22-CD-09-009-001-B_Process Calculation.pdf",
        "CC P22-CD-09-004-001_A CONTROL ARCHITECTURE.pdf",
    ]
    for att in attachments:
        para = doc.add_paragraph(att, style="List Bullet")
        aplicar_arial(para, 10)

    doc.save(output_file)
    print(f"Correo generado: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_correo()
