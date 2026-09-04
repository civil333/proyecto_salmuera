#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N4 ADASA-BW_WATER
Entregas 10 y 11 (Submittals 25007-0010, 25007-0011) - 4 documentos
Fecha: 05-Feb-2026

ESTRUCTURA:
1. EXECUTIVE SUMMARY (1.1 Key Findings, 1.2 Critical Observations)
2. GENERAL INFORMATION
3. DETAILED OBSERVATIONS BY DOCUMENT (4 documentos)
4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS (TM N2: 31 dias, TM N3: 9 dias)
5. REQUIRED ACTIONS - BW WATER
6. ATTACHMENTS
7. RESPONSE SUMMARY

NOTAS:
- Usa skill template-adasa v6.0
- Estructura basada en TM N2/N3
- Incluye E10 (Utility List, Antiscalant Tank) y E11 (Control Architecture, Cable Tray Layout)
"""

import sys
import os

# Agregar la ruta del skill template-adasa
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    "..",
    ".claude",
    "skills",
    "template-adasa",
)
sys.path.insert(0, skill_path)

from config_defaults import DEFAULTS
from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    calcular_anchos_columnas,
    set_table_borders,
    set_repeat_table_header,
    set_updatefields_true,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt, Inches, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml


# Funciones set_table_borders, set_repeat_table_header, set_updatefields_true,
# calcular_anchos_columnas, add_simple_table importadas de table_utils via ejemplo_documento.


def crear_transmittal():
    """Genera el Transmittal N4 en formato ADASA - E10 + E11 (4 documentos)"""

    output_file = "TRANSMITTAL N4 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA (valores de config_defaults.py)
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N4 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-004-0",
        output_filename=output_file,
    )

    # Abrir documento y agregar contenido
    doc = Document(output_file)

    # Limpiar contenido de ejemplo generado por template ADASA
    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(
            x in texto
            for x in [
                "RESUMEN EJECUTIVO",
                "INTRODUCCION",
                "INTRODUCCIÓN",
                "1. INTRO",
                "ESTE DOCUMENTO HA SIDO GENERADO",
                "AGREGUE AQUI EL CONTENIDO",
                "AGREGUE AQUÍ EL CONTENIDO",
            ]
        ):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== 1. EXECUTIVE SUMMARY =====
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    # 1.1 Key Findings
    doc.add_heading("Key Findings", level=2)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 3 - TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Two submittals reviewed with critical observations requiring immediate attention. The Utility Consumption List (E10) has persistent non-compliance with A/C n+1 requirements (31 days pending). The Cable Tray Layout (E11) inherits duplicate TAG FIT-09-001 from Instrument List and is missing instrument locations required by ET."
    )
    aplicar_arial_12(para)

    doc.add_paragraph()

    add_simple_table(
        doc,
        [
            ("Validation Item", "Status", "Reference"),
            (
                "SEC (Specific Energy Consumption)",
                "VALIDATED",
                "3.98 kWh/m3 vs 4.71 kWh/m3 guaranteed (15% margin)",
            ),
            ("Production rate 21 m3/h", "VALIDATED", "Matches design requirements"),
            (
                "PLC frequency 50 Hz compliance",
                "REQUIRES CONFIRMATION",
                "ET 5.4.7 - Currently specified at 60 Hz",
            ),
            (
                "A/C n+1 configuration",
                "NOT COMPLIANT",
                "ET 5.1.11 - Only 1 unit specified (31 days pending)",
            ),
            (
                "A/C thermal calculation",
                "NOT DELIVERED",
                "ET 5.1.11 - Required document (31 days pending)",
            ),
            ("Antiscalant Tank material change", "ACCEPTED", "HDPE to LMDPE justified"),
            ("PLC Allen Bradley compliance", "VALIDATED", "5069-L320ER meets ET 5.4"),
            ('HMI 10" color touch', "VALIDATED", "PanelView Plus 7 2711P-T10C21D8S"),
            ("Modbus TCP/IP Gateway", "VALIDATED", "PLX32-EIP-MBTCP installed"),
            ("Modbus TCP Memory Map", "NOT DELIVERED", "31 days pending (TM N2)"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nStatistics: ").bold = True
    para.add_run("0 Approved (0%) | 2 Approved as noted (50%) | 2 To be revised (50%)")
    aplicar_arial_12(para)

    # 1.2 Critical Observations
    doc.add_heading("Critical Observations", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Observation", "Document", "Severity", "Status"),
            (
                "OBS-01",
                "PLC specified at 60 Hz: Utility List indicates PLC power supply as 220V/1PH/60Hz. ET Section 5.4.7 states equipment operating at frequencies other than 50 Hz will NOT be accepted.",
                "Utility Consumption List",
                "CRITICAL",
                "NEW",
            ),
            (
                "OBS-02",
                'A/C without n+1 configuration: Only 1 A/C unit (2.64 kW) specified. ET 5.1.11 requires n+1 (minimum 2 units). Technical Offer committed "2 A/C (1W+1S)".',
                "Utility Consumption List",
                "CRITICAL",
                "PENDING 31 DAYS",
            ),
            (
                "OBS-03",
                "Missing A/C thermal calculation: ET 5.1.11 requires thermal calculation document. Not delivered.",
                "Missing document",
                "CRITICAL",
                "PENDING 31 DAYS",
            ),
            (
                "OBS-04",
                "Modbus TCP Memory Map not delivered: BW Water committed delivery 31 days ago. Critical for DCS integration.",
                "Control Architecture",
                "CRITICAL",
                "PENDING 31 DAYS",
            ),
            (
                "OBS-05",
                "Duplicate TAG FIT-09-001: Items 4 and 13 have same TAG for different instruments. PLC addressing impossible.",
                "Cable Tray Layout",
                "CRITICAL",
                "PENDING 9 DAYS",
            ),
            (
                "OBS-06",
                "Missing vibration transmitters: Layout missing locations for HP Pump, Feed Turbo, Interstage Turbo per ET 5.5.7.",
                "Cable Tray Layout",
                "CRITICAL",
                "PENDING 9 DAYS",
            ),
            (
                "OBS-07",
                "Missing Pt-100 motor sensors: Layout missing locations for HP Pump and CIP Pump motor sensors per ET 5.3.",
                "Cable Tray Layout",
                "CRITICAL",
                "PENDING 9 DAYS",
            ),
            (
                "OBS-08",
                "HP Pump power inconsistency: Four different values: 93/86/92/83 kW across documents.",
                "Multiple documents",
                "MAJOR",
                "NEW",
            ),
            (
                "OBS-09",
                "UPS not included in BOM: ET 5.4 requires UPS with 8 hours autonomy for control system.",
                "Control Architecture",
                "MAJOR",
                "NEW",
            ),
            (
                "OBS-10",
                "Container dimensions exceed approved 40ft: Layout shows elongated container suggesting 60ft. ADASA rejected 60ft on Nov-17-2025 (+USD $67,208, +5 weeks). Must use approved 40ft standard.",
                "Cable Tray Layout",
                "CRITICAL",
                "NEW",
            ),
        ],
    )

    # ===== 2. GENERAL INFORMATION =====
    # NOTA: NO incluir Date, Project, From, To - ya estan en header ADASA
    doc.add_heading("GENERAL INFORMATION", level=1)

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Transmittal Code", "P22-TM-09-000-004-0"),
            ("Submittal 0010", "25007-0010 (Jan-30-2026) - 2 documents"),
            ("Submittal 0011", "25007-0011 (Feb-03-2026) - 2 documents"),
            ("Total Documents", "4"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nResponse Codes: ").bold = True
    para.add_run(
        "1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information"
    )
    aplicar_arial_12(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Documents Reviewed:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
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
                "Datasheet of Antiscalant Dosing Tank",
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
            (
                "4",
                "P22-DWG-09-007-004",
                "Cable Tray Layout and Support Details",
                "A",
                "3 - To be revised",
            ),
        ],
    )

    # ===== 3. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 3.1 Utility Consumption List ---
    doc.add_heading(
        "Utility Consumption List (P22-LI-09-009-001-A) - TO BE REVISED", level=2
    )

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Code", "P22-LI-09-009-001-A"),
            ("Title", "Utility Consumption List"),
            ("Date", "21-Jan-2026"),
            ("Revision", "A (First issue)"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Observations:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("#", "Code", "Observation", "Impact"),
            (
                "OBS-01",
                "PLC Frequency",
                'PLC power supply specified as "220V/1PH/60Hz". ET Section 5.4.7 states: "No se aceptaran equipos principales que operen en otros voltajes y frecuencias." Chilean grid operates at 50 Hz.',
                "CRITICAL",
            ),
            (
                "OBS-02",
                "A/C Configuration",
                'Only 1 A/C unit (2.64 kW) specified. ET 5.1.11 requires n+1. Technical Offer committed "2 A/C (1W + 1S)" with 5.28 kW total. Observation raised in TM N2, unresolved after 31 days.',
                "CRITICAL",
            ),
            (
                "OBS-03",
                "Thermal Calculation",
                "ET 5.1.11 requires thermal calculation document for A/C sizing. Not delivered. Observation raised in TM N2, unresolved after 31 days.",
                "CRITICAL",
            ),
            (
                "OBS-08",
                "HP Pump Power",
                "Four different values: 93 kW (Utility), 86 kW (Offer), 92 kW (Equipment List), 83 kW (Load List). Unification required.",
                "MAJOR",
            ),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Positive Findings:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Item", "Status", "Details"),
            (
                "SEC Compliance",
                "VALIDATED",
                "SEC = 3.98 kWh/m3 meets guarantee 4.71 kWh/m3 with 15% margin",
            ),
            (
                "Electrical frequency (most equipment)",
                "COMPLIANT",
                "HP Pump, CIP Pump, CIP Heater, Dosing Pump all at 50 Hz",
            ),
            (
                "Production rate",
                "VALIDATED",
                "21 m3/h meets minimum 20 m3/h requirement",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nVERDICT: 3 - TO BE REVISED").bold = True
    aplicar_arial_12(para)

    # --- 3.2 Antiscalant Dosing Tank ---
    doc.add_paragraph()
    doc.add_heading(
        "Antiscalant Dosing Tank Datasheet (P22-ET-09-009-010-B) - APPROVED AS NOTED",
        level=2,
    )

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Code", "P22-ET-09-009-010-B"),
            ("Title", "Datasheet of Antiscalant Dosing Tank"),
            ("Date", "20-Jan-2026"),
            ("TAG", "TK-09-002"),
            ("Revision", "B (Material change from Rev A)"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Material Change Evaluation:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Parameter", "Technical Offer", "Rev A", "Rev B", "Evaluation"),
            ("Material", "HDPE", "HDPE", "LMDPE", "ACCEPTED"),
            (
                "Capacity",
                "65 gal (246 L)",
                "246 L",
                "340 L (0.34 m3)",
                "EXCEEDS requirement",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nADASA Evaluation: ").bold = True
    para.add_run(
        "Material change from HDPE to LMDPE is technically acceptable. Both are polyethylene with similar chemical resistance. LMDPE compatible with antiscalant (pH > 10). Capacity (340 L) exceeds requirement (246 L). "
    )
    para.add_run("MATERIAL CHANGE ACCEPTED.").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\nMinor Observation: ").bold = True
    para.add_run(
        "Tank capacity in P&ID (0.25 m3) differs from Datasheet (0.34 m3). Update P&ID in next revision."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\nVERDICT: 2 - APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    # --- 3.3 Control System Architecture ---
    doc.add_paragraph()
    doc.add_heading(
        "Control System Architecture (P22-CD-09-004-001-B) - APPROVED AS NOTED", level=2
    )

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Code", "P22-CD-09-004-001-B"),
            ("Title", "Control System Architecture"),
            ("Date", "29-Jan-2026"),
            ("Revision", "B (Response to TM N2 comments)"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Bill of Materials - Control System:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("No.", "Description", "Model", "Manufacturer"),
            ("1", "PLC CPU", "5069-L320ER", "Allen Bradley"),
            ("2", 'HMI 10" Color Touch', "2711P-T10C21D8S", "Allen Bradley"),
            ("3", "Ethernet Switch 8 Ports", "1783-USP8T", "Allen Bradley"),
            ("4", "EtherNet/IP to Modbus TCP Gateway", "PLX32-EIP-MBTCP", "ProSoft"),
            ("5", "Studio 5000 Logix Designer V37", "-", "Allen Bradley"),
            ("6", "FactoryTalk View Studio V15", "-", "Allen Bradley"),
            ("7", "Engineering Laptop", "Latitude 3450", "Dell"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("ET 5.4 Compliance:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("ET Requirement", "Delivered", "Complies"),
            ("PLC Allen Bradley", "5069-L320ER CompactLogix", "YES"),
            ('HMI 10" color touch', 'PanelView Plus 7 10"', "YES"),
            ("Modbus TCP/IP", "PLX32-EIP-MBTCP Gateway", "YES"),
            ("Ethernet Switch 5+ ports", "8 ports (Stratix 2100)", "YES"),
            ("UPS 8 hours autonomy", "NOT IN BOM", "NO"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Observations:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("#", "Code", "Observation", "Impact"),
            (
                "OBS-04",
                "Modbus Map",
                "BW Water committed to deliver Modbus TCP Memory Map separately (TM N2). Document NOT delivered after 31 days. Critical for DCS integration.",
                "CRITICAL",
            ),
            (
                "OBS-09",
                "UPS Missing",
                "ET 5.4 (L1088-1089) requires UPS with 8 hours autonomy for control system. Not included in BOM.",
                "MAJOR",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nResponse to TM N2 Comments:").bold = True
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        '- Modbus TCP Memory Map: "WILL SUBMIT SEPARATELY" - NOT DELIVERED (31 days)'
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        '- VFD Fieldbus: "REVISED IN REVB" - PARTIAL (connection shown, protocol not specified)'
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        '- Power Meter: "LCP includes Digital Power Meter with Modbus TCP/IP" - CLOSED'
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\nVERDICT: 2 - APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    # --- 3.4 Cable Tray Layout ---
    doc.add_paragraph()
    doc.add_heading("Cable Tray Layout (P22-DWG-09-007-004-A) - TO BE REVISED", level=2)

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Code", "P22-DWG-09-007-004-A"),
            ("Title", "Cable Tray Layout and Support Details"),
            ("Date", "27-Jan-2026"),
            ("Revision", "A (First issue)"),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Document Content:").bold = True
    aplicar_arial_12(para)
    para = doc.add_paragraph("- Sheet 1: Plan View - Cable Tray Layout")
    aplicar_arial_12(para)
    para = doc.add_paragraph("- Sheet 2: Instrument Location Schedule (32 instruments)")
    aplicar_arial_12(para)
    para = doc.add_paragraph("- Sheet 3: Installation Details")
    aplicar_arial_12(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Observations:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("#", "Code", "Observation", "Impact"),
            (
                "OBS-05",
                "Duplicate TAG",
                "FIT-09-001 appears in Item 4 (Cartridge Filter DN100) AND Item 13 (2nd Stage Permeate DN50). Two different instruments with same TAG. PLC addressing impossible. Inherited from Instrument List.",
                "CRITICAL",
            ),
            (
                "OBS-06",
                "Missing Vibration",
                "Layout missing locations for vibration transmitters on HP Pump (BH-09-001), Feed Turbo (SIP-09-001), Interstage Turbo (SIP-09-002) per ET 5.5.7. Raised in TM N3, unresolved 9 days.",
                "CRITICAL",
            ),
            (
                "OBS-07",
                "Missing Pt-100",
                "Layout missing locations for Pt-100 temperature sensors in HP Pump (87 kW) and CIP Pump (15 kW) motors per ET 5.3. Raised in TM N3, unresolved 9 days.",
                "CRITICAL",
            ),
            (
                "OBS-10",
                "Container >40ft",
                "Layout shows elongated container suggesting 60ft (40ft + 20ft). ADASA rejected 60ft on Nov-17-2025: +USD $67,208 budget, +5 weeks schedule. Must conform to approved 40ft standard.",
                "CRITICAL",
            ),
        ],
    )

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Positive Findings:").bold = True
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Item", "Status", "Details"),
            ("Cable Tray Material", "COMPLIANT", "Steel Hot Dip Galvanized"),
            ("Fill Maximum", "COMPLIANT", "80% declared"),
            ("Instrument Count", "DOCUMENTED", "32 instruments with locations"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nVERDICT: 3 - TO BE REVISED").bold = True
    para.add_run(
        " (due to duplicate TAG, missing instruments, and container >40ft issue)"
    )
    aplicar_arial_12(para)

    # ===== 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "This section summarizes critical observations raised in previous transmittals that remain unresolved."
    )
    aplicar_arial_12(para)

    doc.add_paragraph()

    # 4.1 From TM N2
    doc.add_heading("From Transmittal N2 (January 6, 2026) - 31 DAYS PENDING", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Observation", "Original Document", "Days Pending", "Impact"),
            (
                "1",
                "A/C n+1 configuration required",
                "E5 - DS Air Conditioning",
                "31",
                "Blocks container thermal compliance",
            ),
            (
                "2",
                "A/C thermal calculation required",
                "New document required",
                "31",
                "Required per ET 5.1.11",
            ),
            (
                "3",
                "Static Mixer material justification",
                "E5 - DS Static Mixer",
                "31",
                "FRP to PVC change",
            ),
            (
                "4",
                "Modbus TCP Memory Map required",
                "Control Architecture",
                "31",
                "Critical for DCS integration",
            ),
        ],
    )

    doc.add_paragraph()

    # 4.2 From TM N3
    doc.add_heading("From Transmittal N3 (January 28, 2026) - 9 DAYS PENDING", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Observation", "Document", "Days Pending", "Severity"),
            ("1", "Vibration transmitters missing", "Instrument List", "9", "CRITICAL"),
            (
                "2",
                "Pt-100 motor windings HP Pump",
                "HP Pump Datasheet",
                "9",
                "CRITICAL",
            ),
            (
                "3",
                "CIP Pump datasheet missing",
                "New document required",
                "9",
                "CRITICAL",
            ),
            ("4", "VM-09-015 manual DN100 ANSI 900#", "Valve List", "9", "CRITICAL"),
            (
                "5",
                "Duplicate TAGs (VM-09-015, VE-09-008, VE-09-010)",
                "Valve List",
                "9",
                "MAJOR",
            ),
            ("6", "Missing VFD electrical variables", "IO List", "9", "CRITICAL"),
            ("7", "Missing DO/DI external coordination", "IO List", "9", "CRITICAL"),
            ("8", "Duplicate TAG FIT-09-001", "Instrument List", "9", "CRITICAL"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nNote: ").bold = True
    para.add_run(
        "Observation #8 (FIT-09-001 duplicate) is inherited by Cable Tray Layout in Submittal 0011."
    )
    aplicar_arial_12(para)

    # ===== 5. REQUIRED ACTIONS - BW WATER =====
    doc.add_heading("REQUIRED ACTIONS - BW WATER", level=1)

    # 5.1 Critical Actions
    doc.add_heading("Critical Actions (HIGH Priority)", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Action", "Document", "Reference", "Status"),
            (
                "1",
                "Confirm PLC frequency compatibility: If dual-frequency (50/60 Hz), document explicitly. If 60 Hz only, replace equipment.",
                "P22-LI-09-009-001-A",
                "OBS-01, ET 5.4.7",
                "PENDING",
            ),
            (
                "2",
                "Add 2nd A/C unit: Include n+1 configuration (2 units) as required by ET 5.1.11 and Technical Offer.",
                "P22-LI-09-009-001-A",
                "OBS-02, ET 5.1.11",
                "PENDING 31 DAYS",
            ),
            (
                "3",
                "Deliver A/C thermal calculation: Provide thermal load calculation considering ALL heat sources per ET 5.1.11.",
                "New document",
                "OBS-03, ET 5.1.11",
                "PENDING 31 DAYS",
            ),
            (
                "4",
                "URGENT: Deliver Modbus TCP Memory Map: Document committed 31 days ago. Critical for DCS integration.",
                "New document",
                "OBS-04, TM N2",
                "PENDING 31 DAYS",
            ),
            (
                "5",
                "Correct duplicate TAG FIT-09-001: Renumber Item 13 as FIT-09-002 in Instrument List and Cable Tray Layout.",
                "P22-LI-09-008-003 + P22-DWG-09-007-004",
                "OBS-05, TM N3",
                "PENDING 9 DAYS",
            ),
            (
                "6",
                "Include vibration transmitter locations: Add VT-09-001/002/003 on HP Pump and Turbochargers in Layout.",
                "P22-DWG-09-007-004 + P22-LI-09-008-003",
                "OBS-06, ET 5.5.7",
                "PENDING 9 DAYS",
            ),
            (
                "7",
                "Include Pt-100 motor sensor locations: Add temperature sensors in HP Pump and CIP Pump motors.",
                "P22-DWG-09-007-004 + Datasheets",
                "OBS-07, ET 5.3",
                "PENDING 9 DAYS",
            ),
            (
                "8",
                "URGENT: Confirm container dimensions: Layout shows 60ft. ADASA rejected 60ft on Nov-17-2025 (+USD $67,208, +5 weeks). Use approved 40ft standard.",
                "P22-DWG-09-007-004",
                "OBS-10",
                "NEW - CRITICAL",
            ),
        ],
    )

    doc.add_paragraph()

    # 5.2 Major Actions
    doc.add_heading("Major Actions (MEDIUM Priority)", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Action", "Document", "Reference", "Status"),
            (
                "9",
                "Unify HP Pump power: Determine correct value (83/86/92/93 kW) and update ALL documents.",
                "Multiple",
                "OBS-08",
                "PENDING",
            ),
            (
                "10",
                "Include UPS in BOM: Add UPS with 8 hours autonomy per ET 5.4.",
                "P22-CD-09-004-001",
                "OBS-09, ET 5.4",
                "PENDING",
            ),
            (
                "11",
                "Clarify CIP Pump power: Confirm correct value (11 kW vs 15 kW).",
                "P22-LI-09-009-001-A",
                "Cross-ref",
                "PENDING",
            ),
            (
                "12",
                "Specify VFD fieldbus explicitly: Document protocol and available electrical variables.",
                "P22-CD-09-004-001",
                "OBS-12",
                "PENDING",
            ),
        ],
    )

    doc.add_paragraph()

    # 5.3 Minor Actions
    doc.add_heading("Minor Actions (LOW Priority)", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Action", "Document", "Reference", "Status"),
            (
                "13",
                "Update P&ID Antiscalant Tank capacity: Change from 0.25 m3 to 0.34 m3.",
                "P22-DWG-09-009-002",
                "OBS-11",
                "PENDING",
            ),
            (
                "14",
                "Unify LIT TAG: Decide between LIT-09-001 or LIT-09-002 for CIP Tank Level.",
                "Multiple",
                "OBS-13",
                "PENDING",
            ),
        ],
    )

    # ===== 6. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    add_simple_table(
        doc,
        [
            ("#", "Attachment", "Description"),
            (
                "L",
                "P22-LI-09-009-001-A_Utility_Consumption_List_Comments.pdf",
                "Utility Consumption List with ADASA review comments",
            ),
            (
                "M",
                "P22-ET-09-009-010-B_Antiscalant_Tank_Comments.pdf",
                "Antiscalant Dosing Tank datasheet with ADASA annotations",
            ),
            (
                "N",
                "P22-CD-09-004-001-B_Control_Architecture_Comments.pdf",
                "Control System Architecture with ADASA review comments",
            ),
            (
                "O",
                "P22-DWG-09-007-004-A_Cable_Tray_Layout_Comments.pdf",
                "Cable Tray Layout with ADASA annotations",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nDownload Link: ").bold = True
    para.add_run("[To be provided]")
    aplicar_arial_12(para)

    # ===== 7. RESPONSE SUMMARY =====
    # NOTA: Solo documentos BW Water revisados, NO incluir submittals (son codigos internos)
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document", "Code", "Verdict"),
            ("Utility Consumption List", "P22-LI-09-009-001-A", "3 - To be revised"),
            (
                "Antiscalant Dosing Tank DS",
                "P22-ET-09-009-010-B",
                "2 - Approved as noted",
            ),
            (
                "Control System Architecture",
                "P22-CD-09-004-001-B",
                "2 - Approved as noted",
            ),
            ("Cable Tray Layout", "P22-DWG-09-007-004-A", "3 - To be revised"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("\nTRANSMITTAL VERDICT: 3 - TO BE REVISED").bold = True
    aplicar_arial_12(para)

    # Configurar actualizacion automatica del TOC al abrir
    set_updatefields_true(doc)

    # Guardar documento
    doc.save(output_file)
    print(f"Document generated: {output_file}")
    print(f"\nEstructura Transmittal N4 (05-Feb-2026):")
    print(f"  1. EXECUTIVE SUMMARY")
    print(f"     1.1 Key Findings (E10 + E11)")
    print(f"     1.2 Critical Observations (10 items: 8 CRITICAL, 2 MAJOR)")
    print(f"  2. GENERAL INFORMATION (Submittal 0010 + 0011, 4 docs)")
    print(f"  3. DETAILED OBSERVATIONS BY DOCUMENT")
    print(f"     3.1 Utility Consumption List - TO BE REVISED")
    print(f"     3.2 Antiscalant Dosing Tank DS - APPROVED AS NOTED")
    print(f"     3.3 Control System Architecture - APPROVED AS NOTED")
    print(f"     3.4 Cable Tray Layout - TO BE REVISED (incl. OBS-10 Container >40ft)")
    print(f"  4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS")
    print(f"     4.1 From TM N2 (31 days pending) - 4 items")
    print(f"     4.2 From TM N3 (9 days pending) - 8 items")
    print(f"  5. REQUIRED ACTIONS - BW WATER")
    print(f"     5.1 Critical (#1-8) - includes OBS-10 Container")
    print(f"     5.2 Major (#9-12)")
    print(f"     5.3 Minor (#13-14)")
    print(f"  6. ATTACHMENTS (4 PDFs)")
    print(f"  7. RESPONSE SUMMARY")
    print(f"\n[OK] Estadisticas: 0 Approved | 2 Approved as noted | 2 To be revised")
    print(f"[OK] Observaciones pendientes TM N2: 31 dias")
    print(f"[OK] Observaciones pendientes TM N3: 9 dias")
    print(f"[OK] Modbus TCP Memory Map: 31 dias pendiente")
    print(f"[!] OBS-10: Container >40ft - rechazado Nov-17-2025 (+USD $67,208, +5 sem)")
    return output_file


if __name__ == "__main__":
    crear_transmittal()
