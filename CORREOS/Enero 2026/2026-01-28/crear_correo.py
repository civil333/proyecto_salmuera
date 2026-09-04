#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Technical Review Transmittal N3 + Engineering Status + Catch-Up Schedule Request
Fecha: 28 de enero de 2026
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


def aplicar_arial(paragraph, size=11):
    """Aplica formato Arial al parrafo"""
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def crear_correo():
    """Genera el correo en formato DOCX"""

    output_file = "2026-01-28_Transmittal-N3-Estado-Entregables-BW-Water.docx"

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
    para.add_run("January 28, 2026")
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
        "Technical Review Transmittal N3 (P22-TM-09-000-003-0) + Engineering Deliverables Status + Catch-Up Schedule Request"
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Ref: ").bold = True
    para.add_run("Contract C-4300 / BAE 12803 / Baseline Schedule")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ INTRO ============
    para = doc.add_paragraph("Dear BW Water Team,")
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "We submit Technical Review Transmittal N3 (P22-TM-09-000-003-0) along with an updated Engineering Deliverables Status for the Second Stage RO Brine Module project. We also request a catch-up schedule to support project recovery planning."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 1: TRANSMITTAL N3 ============
    para = doc.add_paragraph()
    run = para.add_run("1. TRANSMITTAL N3 - TECHNICAL REVIEW")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph(
        "Attached: Technical Review Transmittal N3 covering the latest submittals received."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # 1.1 Submittal Coverage
    para = doc.add_paragraph()
    para.add_run("1.1 Submittal Coverage").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=5, cols=4)
    set_table_borders(table)

    submittals = [
        ("Submittal", "Date Received", "Documents", "Topics"),
        (
            "25007-0007",
            "Jan-12-2026",
            "6",
            "Process Calc Rev.B, HP Pump, CIP Tank, Chemical List, Line List",
        ),
        (
            "25007-0008",
            "Jan-20-2026",
            "12",
            "PFD Rev.B, Container, Turbochargers, Equipment List, Valve List, IO List, Instrument List",
        ),
        (
            "25007-0009",
            "Jan-20-2026",
            "5",
            "Electrical Cables DS, Cable Tray, Conduit, Instrument Layout, Power Cable Schedule",
        ),
        ("TOTAL", "", "23", ""),
    ]

    for i, row_data in enumerate(submittals):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    if i == 0 or i == 4:
                        run.bold = True

    doc.add_paragraph()

    # 1.2 Review Statistics
    para = doc.add_paragraph()
    para.add_run("1.2 Review Statistics").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=5, cols=3)
    set_table_borders(table)

    stats = [
        ("Verdict", "Quantity", "%"),
        ("1 - Approved", "13", "57%"),
        ("2 - Approved as noted", "5", "22%"),
        ("3 - To be revised", "5", "22%"),
        ("TOTAL", "23", "100%"),
    ]

    for i, row_data in enumerate(stats):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    if i == 0 or i == 4:
                        run.bold = True

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Transmittal Verdict: 3 - TO BE REVISED").bold = True
    aplicar_arial(para)

    doc.add_paragraph()

    # 1.3 Key Observations - REFORMATEADO con variacion estructural
    para = doc.add_paragraph()
    para.add_run("1.3 Key Observations Requiring Immediate Attention").bold = True
    aplicar_arial(para)

    doc.add_paragraph()

    # Subseccion: Instrumentation Issues (narrativa)
    para = doc.add_paragraph()
    para.add_run(
        "Instrumentation Issues (Instrument List P22-LI-09-008-003-A)"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "The most critical finding is a duplicate TAG assignment: FIT-09-001 appears both for Cartridge Filter DN100 (Line 4) and 2nd Stage Permeate DN50 (Line 13). This makes PLC addressing impossible and must be corrected before control system programming."
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "Additionally, vibration transmitters for HP Pump, Feed Turbocharger, and Interstage Turbocharger are not included per ET Section 5.5.7 requirements."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # Subseccion: Pump Temperature (narrativa con apertura)
    para = doc.add_paragraph()
    para.add_run("Pump Temperature Protection (HP Pump Datasheet)").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "The datasheet specifies RTDs for bearing temperature but does not include Pt-100 sensors for motor windings. ET Section 5.3 (L1032-1033) requires both. The 87 kW motor with VFD needs winding thermal protection - unless an alternative protection method is documented."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # Subseccion: Valve Actuation (narrativa con apertura)
    para = doc.add_paragraph()
    para.add_run("Valve Actuation (Valve List P22-LI-09-005-002-A)").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "VM-09-015 (DN100 Butterfly, ANSI 900#) on HP Pump discharge is specified MANUAL. ET Section 5.2.3 requires electric actuation for relevant process valves. BW Water should either change to motorized actuation or provide technical justification for the manual configuration."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    # Subseccion: Control System (tabla pequena - variacion)
    para = doc.add_paragraph()
    para.add_run("Control System Integration (IO List P22-LI-09-008-001-A)").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=3, cols=3)
    set_table_borders(table)

    io_issues = [
        ("Issue", "Description", "Severity"),
        (
            "VFD variables",
            "Missing electrical parameters (V, I, P, Hz) for SEC verification per ET 5.6",
            "CRITICAL",
        ),
        (
            "Coordination signals",
            "System needs DO (module status) and DI (external enable) for plant integration",
            "CRITICAL",
        ),
    ]

    for i, row_data in enumerate(io_issues):
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

    doc.add_paragraph()

    # 1.4 Validated Items
    para = doc.add_paragraph()
    para.add_run("1.4 Validated Items (Positive Findings)").bold = True
    aplicar_arial(para)

    validated = [
        "Process Calculation - Design Basis: All parameters per ET",
        "BiTurbo modeling (43k & 53k TDS) - 10 scenarios included",
        "HP Pump operating point - 49 m³/h @ 49.4 bar DP",
        "Permeate TDS < 500 mg/L guarantee - < 248 mg/L worst case",
        "Permeate chlorides < 400 mg/L - < 146 mg/L worst case",
        "Super Duplex material (PREN > 40) - PREN 42.5 confirmed",
        "HART protocol on all transmitters - 4-20mA + HART",
        "Conductivity instrumentation (5 locations) - ET 5.5.5 fully covered",
    ]
    for item in validated:
        para = doc.add_paragraph(item, style="List Bullet")
        aplicar_arial(para, 10)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Download Link: ").bold = True
    run = para.add_run("https://www.dropbox.com/t/tDInLROUqCSiQlYM")
    run.font.underline = True
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 2: ENGINEERING STATUS ============
    para = doc.add_paragraph()
    run = para.add_run("2. ENGINEERING DELIVERABLES STATUS")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Per the Baseline Schedule, Engineering was scheduled to complete on ")
    run = para.add_run("January 5, 2026")
    run.bold = True
    para.add_run(" (65 days from NTP). Current status as of January 28, 2026:")
    aplicar_arial(para)

    doc.add_paragraph()

    # 2.1 Overall Status
    para = doc.add_paragraph()
    para.add_run("2.1 Overall Status Summary").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=7, cols=3)
    set_table_borders(table)

    status_data = [
        ("Status", "Quantity", "% of Eng. Phase"),
        ("1 - Approved", "21", "33%"),
        ("2 - Approved as noted", "13", "20%"),
        ("3 - To be revised", "9", "14%"),
        ("4 - Rejected", "3", "5%"),
        ("Not delivered", "14", "22%"),
        ("TOTAL ENGINEERING PHASE", "64", "100%"),
    ]

    for i, row_data in enumerate(status_data):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    if i == 0 or i == 6:
                        run.bold = True

    doc.add_paragraph()

    # 2.2 KPIs
    para = doc.add_paragraph()
    para.add_run("2.2 Key Performance Indicators").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=5, cols=4)
    set_table_borders(table)

    kpis = [
        ("Indicator", "Value", "Target", "Status"),
        ("Documents delivered", "38 of 52", "52", "73%"),
        ("Ready for fabrication (1+2)", "29 of 52", "52", "56%"),
        ("Requiring correction (3+4)", "9 of 38", "0", "24% of delivered"),
        ("Days since Eng. Complete deadline", "23 days", "0", "DELAYED"),
    ]

    for i, row_data in enumerate(kpis):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
                    if i == 0:
                        run.bold = True
                    if j == 3 and value == "DELAYED":
                        run.bold = True
                        run.font.color.rgb = RGBColor(192, 0, 0)

    doc.add_paragraph()

    # 2.3 Critical Pending Documents
    para = doc.add_paragraph()
    para.add_run("2.3 Critical Pending Documents (14 documents)").bold = True
    aplicar_arial(para)

    table = doc.add_table(rows=11, cols=4)
    set_table_borders(table)

    pending = [
        ("#", "Document", "Baseline Date", "Days Delayed"),
        ("1", "PIE Detallado (ITP)", "Dec-31-2025", "28"),
        ("2", "Equipment Layout", "Dec-05-2025", "54"),
        ("3", "DS MCC", "Nov-19-2025", "70"),
        ("4", "CIP Pump Datasheet (complete)", "Nov-13-2025", "76"),
        ("5", "Plant Control Philosophy", "Dec-23-2025", "36"),
        ("6", "3D Model", "Dec-29-2025", "30"),
        ("7", "Piping Layout", "Dec-30-2025", "29"),
        ("8", "Stress & Flexibility Analysis", "Dec-29-2025", "30"),
        ("9", "Utility Consumption List", "Nov-04-2025", "85"),
        ("10", "Seismic Calculation", "Dec-29-2025", "30"),
    ]

    for i, row_data in enumerate(pending):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            for para in row.cells[j].paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    if i == 0:
                        run.bold = True

    doc.add_paragraph()

    # ============ SECTION 3: CATCH-UP SCHEDULE REQUEST ============
    para = doc.add_paragraph()
    run = para.add_run("3. CATCH-UP SCHEDULE REQUEST")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(
        "The engineering phase currently shows a 23-day delay from baseline. A catch-up schedule will help both parties coordinate recovery efforts and maintain alignment with contracted milestones."
    )
    aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("3.1 Requested Information").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph("Please provide a recovery plan that includes:")
    aplicar_arial(para)

    requests = [
        "Pending Documents Plan: Proposed delivery dates for the 14 outstanding engineering documents",
        'Revision Plan: Re-submission dates for the 9 documents marked "To be revised"',
        "Milestone Impact Assessment: Updated dates for key milestones (Engineering Complete, FAT, Ready to Ship)",
        "Mitigation Actions: Specific measures to recover the current 23-day delay",
    ]
    for i, req in enumerate(requests, 1):
        para = doc.add_paragraph(f"{i}. {req}")
        aplicar_arial(para, 10)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("3.2 Timeline").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Please provide the catch-up schedule within ")
    run = para.add_run("7 business days")
    run.bold = True
    para.add_run(" (by ")
    run = para.add_run("February 6, 2026")
    run.bold = True
    para.add_run(") to allow proper coordination and support from ADASA.")
    aplicar_arial(para)

    doc.add_paragraph()

    # ============ SECTION 4: NEXT STEPS ============
    para = doc.add_paragraph()
    run = para.add_run("4. NEXT STEPS")
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = "Arial"

    doc.add_paragraph()

    next_steps = [
        "Please confirm receipt of this transmittal",
        "Provide the requested catch-up schedule by February 6, 2026",
        "Address the critical observations identified in Transmittal N3",
        "Schedule a coordination meeting to review recovery plan if needed",
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
        "P22-TM-09-000-003-0 - TRANSMITTAL N3 ADASA-BW_WATER.docx",
        "Annotated documents: https://www.dropbox.com/t/tDInLROUqCSiQlYM",
        "Attachment A: Instrument List with ADASA comments",
        "Attachment B: Process Calculation with ADASA annotations",
        "Attachment G: Cross-reference analysis Instrument List vs P&ID vs IO List",
        "Attachment H: Pump temperature measurement cross-reference",
        "Attachment I: Layout cross-reference analysis",
        "Attachment J: Valve List and Equipment List cross-reference",
        "Attachment K: Conductivity and Flow instrumentation compliance (P22-CD-09-008-001-0)",
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
