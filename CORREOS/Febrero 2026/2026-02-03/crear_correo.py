#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Technical Review Transmittal N4
Fecha: 03 de febrero de 2026
Entregas: E10 + E11 (4 documentos)
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
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml

# set_table_borders importada de table_utils (incluye centrado automatico)


def aplicar_anchos_tabla(table, data):
    """Aplica anchos de columna dinamicos a una tabla existente."""
    anchos = calcular_anchos_columnas(data)
    if anchos:
        for row in table.rows:
            for j, cell in enumerate(row.cells):
                if j < len(anchos):
                    cell.width = anchos[j]


def aplicar_arial(paragraph, size=11):
    """Aplica formato Arial al parrafo"""
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def crear_correo():
    """Genera el correo en formato DOCX"""

    output_file = "2026-02-03_Transmittal-N4-Revision-Tecnica-E10-E11.docx"

    doc = Document()

    # Configurar margenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ============ HEADER ============
    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("February 03, 2026")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("From: ").bold = True
    para.add_run(
        f"{DEFAULTS['contacto_nombre']} - {DEFAULTS['contacto_cargo']} ({DEFAULTS['contacto_empresa']})"
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("To: ").bold = True
    para.add_run("BW Water Americas Inc. (Marjan Fariborz / Logan Maroney)")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("CC: ").bold = True
    para.add_run("ADASA Technical Management")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Subject: ").bold = True
    para.add_run(
        "Technical Review Transmittal N4 (P22-TM-09-000-004-0) - Submittals 0010, 0011 Review"
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Ref: ").bold = True
    para.add_run("Contract C-4300 / BAE 12803 / Transmittals N2, N3")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ INTRO ============
    para = doc.add_paragraph("Dear BW Water Team,")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "We submit Technical Review Transmittal N4 (P22-TM-09-000-004-0) covering the review of Submittal 0010 (received January 30, 2026) and Submittal 0011 (received February 3, 2026)."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 1: TRANSMITTAL N4 SUMMARY ============
    para = doc.add_paragraph()
    run = para.add_run("1. TRANSMITTAL N4 - TECHNICAL REVIEW SUMMARY")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    # 1.1 Documents Reviewed
    para = doc.add_paragraph()
    para.add_run("1.1 Documents Reviewed").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=5, cols=5)
    set_table_borders(table)

    docs = [
        ("#", "Code", "Title", "Rev", "Verdict"),
        (
            "1",
            "P22-LI-09-009-001",
            "Utility Consumption List",
            "A",
            "3 - To be revised",
        ),
        (
            "2",
            "P22-ET-09-009-010",
            "Antiscalant Dosing Tank DS",
            "B",
            "2 - Approved as noted",
        ),
        (
            "3",
            "P22-CD-09-004-001",
            "Control System Architecture",
            "B",
            "2 - Approved as noted",
        ),
        ("4", "P22-DWG-09-007-004", "Cable Tray Layout", "A", "3 - To be revised"),
    ]

    aplicar_anchos_tabla(table, docs)

    for i, row_data in enumerate(docs):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    if i == 0:
                        run.bold = True
                    if j == 4 and "3 - To be revised" in value:
                        run.bold = True
                        run.font.color.rgb = RGBColor(192, 0, 0)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Transmittal Verdict: 3 - TO BE REVISED").bold = True
    for run in para.runs:
        run.font.color.rgb = RGBColor(192, 0, 0)
    aplicar_arial(para)

    doc.add_paragraph()

    # 1.2 Key Findings
    para = doc.add_paragraph()
    para.add_run("1.2 Key Findings").bold = True
    aplicar_arial(para)

    doc.add_paragraph()

    # Positive findings (narrativo)
    para = doc.add_paragraph()
    para.add_run("Positive Findings:").bold = True
    aplicar_arial(para)

    positives = [
        "SEC (Specific Energy Consumption) validated at 3.98 kWh/m3 vs 4.71 kWh/m3 guaranteed (15% favorable margin)",
        "Antiscalant Tank material change HDPE to LMDPE accepted (justified by dimensional constraints)",
        "Control System Architecture meets ET 5.4 requirements (Allen Bradley PLC, HMI, Modbus Gateway)",
        "Production rate 21 m3/h validated",
    ]
    for item in positives:
        para = doc.add_paragraph(item, style="List Bullet")
        aplicar_arial(para, 10)

    doc.add_paragraph()

    # Critical Issues (tabla)
    para = doc.add_paragraph()
    para.add_run("Critical Issues:").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=9, cols=4)
    set_table_borders(table)

    issues = [
        ("#", "Observation", "Severity", "Status"),
        (
            "OBS-01",
            "PLC specified at 60 Hz - ET 5.4.7 requires 50 Hz",
            "CRITICAL",
            "NEW",
        ),
        (
            "OBS-02",
            "Only 1 A/C unit - ET 5.1.11 requires n+1",
            "CRITICAL",
            "29 DAYS PENDING",
        ),
        (
            "OBS-03",
            "A/C thermal calculation not delivered",
            "CRITICAL",
            "29 DAYS PENDING",
        ),
        (
            "OBS-04",
            "Modbus TCP Memory Map not delivered",
            "CRITICAL",
            "38 DAYS PENDING",
        ),
        ("OBS-05", "Duplicate TAG FIT-09-001 in Layout", "CRITICAL", "7 DAYS PENDING"),
        (
            "OBS-06",
            "Missing vibration transmitters - ET 5.5.7",
            "CRITICAL",
            "7 DAYS PENDING",
        ),
        (
            "OBS-07",
            "Missing Pt-100 motor sensors - ET 5.3",
            "CRITICAL",
            "7 DAYS PENDING",
        ),
        ("OBS-10", "Container >40ft - Rejected Nov-17-2025", "CRITICAL", "NEW"),
    ]

    aplicar_anchos_tabla(table, issues)

    for i, row_data in enumerate(issues):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    if i == 0:
                        run.bold = True
                    if j == 2 and value == "CRITICAL":
                        run.bold = True
                        run.font.color.rgb = RGBColor(192, 0, 0)
                    if j == 3 and "PENDING" in value:
                        run.bold = True
                        run.font.color.rgb = RGBColor(192, 0, 0)

    doc.add_paragraph()

    # 1.3 PLC Frequency Observation
    para = doc.add_paragraph()
    para.add_run("1.3 PLC Frequency Observation").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Utility Consumption List specifies PLC power supply as 220V/1PH/60Hz. ET Section 5.4.7 states equipment operating at frequencies other than 50 Hz will not be accepted. "
    )
    run = para.add_run(
        "If the PLC power supply is dual-frequency (50/60 Hz auto-ranging), please confirm this specification explicitly."
    )
    run.italic = True
    para.add_run(
        " If the PLC operates only at 60 Hz, replacement with 50 Hz compatible equipment is required."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # 1.4 Control System Positive
    para = doc.add_paragraph()
    para.add_run("1.4 Control System - Positive Findings").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "Control System Architecture Rev.B demonstrates compliance with ET 5.4:"
    )
    aplicar_arial(para)

    ctrl_items = [
        "PLC Allen Bradley 5069-L320ER CompactLogix",
        'HMI PanelView Plus 7 10" color touch',
        "Modbus TCP/IP Gateway PLX32-EIP-MBTCP",
        "Software licenses (Studio 5000 + FactoryTalk)",
    ]
    for item in ctrl_items:
        para = doc.add_paragraph(item, style="List Bullet")
        aplicar_arial(para, 10)

    para = doc.add_paragraph()
    para.add_run(
        "However, UPS with 8-hour autonomy (ET 5.4 L1088-1089) is not included in BOM. Please add to equipment list."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # 1.5 Container Dimensions - Critical
    para = doc.add_paragraph()
    para.add_run("1.5 Container Dimensions - Critical Observation").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    run = para.add_run(
        "The Cable Tray Layout shows an elongated container configuration suggesting 60ft (40ft + 20ft extension)."
    )
    run.bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "ADASA formally rejected the 60ft container proposal on November 17, 2025 due to:"
    )
    aplicar_arial(para)

    container_reasons = [
        "Budget impact: +USD $67,208",
        "Schedule impact: +5 weeks",
    ]
    for item in container_reasons:
        para = doc.add_paragraph(item, style="List Bullet")
        aplicar_arial(para, 10)

    para = doc.add_paragraph()
    para.add_run(
        "The container must conform to the approved 40ft standard. Please confirm the layout uses approved dimensions, or provide clarification if an alternative is being proposed."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 2: PENDING OBSERVATIONS STATUS ============
    para = doc.add_paragraph()
    run = para.add_run("2. PENDING OBSERVATIONS STATUS")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "This transmittal consolidates observations from previous reviews. Critical items pending resolution:"
    )
    aplicar_arial(para)

    table = doc.add_table(rows=3, cols=3)
    set_table_borders(table)

    pending_obs = [
        ("Origin", "Days Pending", "Key Items"),
        (
            "TM N2 (Jan-06)",
            "29-38 days",
            "A/C n+1 configuration, A/C thermal calculation, Modbus TCP Map",
        ),
        (
            "TM N3 (Jan-28)",
            "7 days",
            "Duplicate TAG FIT-09-001, Vibration transmitters, Pt-100 motor sensors",
        ),
    ]

    aplicar_anchos_tabla(table, pending_obs)

    for i, row_data in enumerate(pending_obs):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    if i == 0:
                        run.bold = True
                    if j == 1 and ("29" in value or "38" in value):
                        run.bold = True
                        run.font.color.rgb = RGBColor(192, 0, 0)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "The A/C observations were first raised in Transmittal N2 on January 6, 2026. The Utility Consumption List in Submittal 0010 still shows only 1 A/C unit (2.64 kW), confirming this non-compliance persists."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        'The Modbus TCP Memory Map was committed by BW Water in response to TM N2 comments ("WILL SUBMIT I/O MODBUS LIST SEPARATELY"). This document has '
    )
    run = para.add_run("NOT been delivered after 38 days")
    run.bold = True
    run.font.color.rgb = RGBColor(192, 0, 0)
    para.add_run(" and is critical for DCS integration planning.")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 3: CATCH-UP SCHEDULE REMINDER ============
    para = doc.add_paragraph()
    run = para.add_run("3. CATCH-UP SCHEDULE REMINDER")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "Per our request dated January 28, 2026, we are awaiting the catch-up schedule by "
    )
    run = para.add_run("February 6, 2026")
    run.bold = True
    para.add_run(" (3 days remaining).")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph("The current status shows 54 documents delivered with:")
    aplicar_arial(para)

    stats = [
        "36 approved/approved as noted (67%)",
        "15 requiring revision (28%)",
        "3 rejected (5%)",
    ]
    for item in stats:
        para = doc.add_paragraph(item, style="List Bullet")
        aplicar_arial(para, 10)

    doc.add_paragraph()

    # ============ SECTION 4: REQUIRED ACTIONS ============
    para = doc.add_paragraph()
    run = para.add_run("4. REQUIRED ACTIONS")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("4.1 Critical Actions (Immediate)").bold = True
    aplicar_arial(para)

    critical_actions = [
        "PLC Frequency: Confirm dual-frequency compatibility OR replace with 50 Hz equipment",
        "A/C Configuration: Add 2nd A/C unit per ET 5.1.11 and Technical Offer (29 days pending)",
        "A/C Thermal Calculation: Deliver thermal load document (29 days pending)",
        "Modbus TCP Memory Map: Deliver document as committed (38 days pending)",
        "Duplicate TAG FIT-09-001: Correct in Instrument List and Cable Tray Layout (7 days pending)",
        "Vibration Transmitters: Add to Instrument List and Layout per ET 5.5.7 (7 days pending)",
        "Pt-100 Motor Sensors: Add to pump datasheets and Layout per ET 5.3 (7 days pending)",
        "Container Dimensions: Confirm layout uses approved 40ft standard (60ft rejected Nov-17-2025)",
    ]
    for i, action in enumerate(critical_actions, 1):
        para = doc.add_paragraph(f"{i}. {action}")
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("4.2 Major Actions").bold = True
    aplicar_arial(para)

    major_actions = [
        "HP Pump Power: Unify values across all documents (83/86/92/93 kW discrepancy)",
        "UPS: Include in Control System BOM per ET 5.4 (8-hour autonomy)",
        "CIP Pump Power: Clarify correct value (11 kW vs 15 kW Technical Offer)",
    ]
    for i, action in enumerate(major_actions, 9):
        para = doc.add_paragraph(f"{i}. {action}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 5: NEXT STEPS ============
    para = doc.add_paragraph()
    run = para.add_run("5. NEXT STEPS")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    next_steps = [
        "Please confirm receipt of Transmittal N4",
        "Provide the catch-up schedule by February 6, 2026 (as previously requested)",
        "Prioritize A/C and Modbus Map observations (29-38 days pending)",
        "Address duplicate TAG FIT-09-001 affecting Cable Tray Layout",
        "Coordinate on PLC frequency confirmation",
        "Clarify container dimensions - confirm 40ft standard or justify deviation",
    ]
    for i, step in enumerate(next_steps, 1):
        para = doc.add_paragraph(f"{i}. {step}")
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph("Available for coordination as needed.")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SIGNATURE ============
    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(DEFAULTS["contacto_nombre"]).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph("Contract Administrator")
    aplicar_arial(para)

    para = doc.add_paragraph("ADASA - Aguas de Antofagasta S.A.")
    aplicar_arial(para)

    para = doc.add_paragraph("Project: BAE 12803 - Second Stage RO Brine Module Taltal")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ ATTACHMENTS ============
    para = doc.add_paragraph()
    para.add_run("Attachments:").bold = True
    aplicar_arial(para)

    attachments = [
        "P22-TM-09-000-004-0 - TRANSMITTAL N4 ADASA-BW_WATER.docx",
        "Attachment L: P22-LI-09-009-001-A_Utility_Consumption_List_Comments.pdf",
        "Attachment M: P22-ET-09-009-010-B_Antiscalant_Tank_Comments.pdf",
        "Attachment N: P22-CD-09-004-001-B_Control_Architecture_Comments.pdf",
        "Attachment O: P22-DWG-09-007-004-A_Cable_Tray_Layout_Comments.pdf",
    ]
    for att in attachments:
        para = doc.add_paragraph(att, style="List Bullet")
        aplicar_arial(para, 10)

    # Save document
    doc.save(output_file)
    print(f"Correo generado exitosamente: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_correo()
