#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N2 ADASA-BW_WATER
Basado en la estructura aprobada del TM N1, adaptado para Entregas 3-6
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


# Funciones set_table_borders, set_repeat_table_header, set_updatefields_true
# importadas de table_utils via ejemplo_documento.


def crear_transmittal():
    """Genera el Transmittal N2 en formato ADASA"""

    output_file = "TRANSMITTAL N2 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N2 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-002-0",
        output_filename=output_file,
    )

    # Abrir documento y agregar contenido traducido
    doc = Document(output_file)

    # Limpiar contenido de ejemplo generado
    paragraphs_to_remove = []
    for i, para in enumerate(doc.paragraphs):
        if "RESUMEN EJECUTIVO" in para.text or "INTRODUCCIÓN" in para.text:
            paragraphs_to_remove.append(para)
        elif (
            "Este documento ha sido generado" in para.text
            or "Agregue aquí el contenido" in para.text
        ):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== CONTENIDO DEL TRANSMITTAL N2 EN INGLES =====

    # EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("January 26, 2026")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Project: ").bold = True
    para.add_run("BAE 12803 - Brine Module Taltal")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Review by: ").bold = True
    para.add_run("ADASA")
    aplicar_arial_12(para)

    # GENERAL INFORMATION
    doc.add_heading("GENERAL INFORMATION", level=1)

    table = doc.add_table(rows=7, cols=2)
    set_table_borders(table)

    data = [
        ("Field", "Value"),
        ("Submittal 0003", "25007-0003 (Dec-16-2025) - 1 document"),
        ("Submittal 0004", "25007-0004 (Dec-24-2025) - 1 document"),
        ("Submittal 0005", "25007-0005 (Jan-06-2026) - 2 documents"),
        ("Submittal 0006", "25007-0006 (Jan-08-2026) - 3 documents"),
        ("Submittal 0007", "25007-0007 (Jan-14-2026) - 1 document"),
        ("Total Documents", "8"),
    ]

    for i, (field, value) in enumerate(data):
        row = table.rows[i]
        row.cells[0].text = field
        row.cells[1].text = value
        if i == 0:
            set_repeat_table_header(row)
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True

    para = doc.add_paragraph()
    para.add_run("\nResponse Codes: ").bold = True
    para.add_run(
        "1=Approved, 2=Approved as noted, 3=To be revised as noted, 4=Rejected, 5=For Information"
    )
    aplicar_arial_12(para)

    # CRITICAL OBSERVATIONS
    doc.add_heading("CRITICAL OBSERVATIONS", level=1)

    table5 = doc.add_table(rows=4, cols=4)
    set_table_borders(table5)

    observations = [
        ("#", "Observation", "Document", "Severity"),
        (
            "1",
            "A/C thermal load undersized: Calculated 5.96 kW vs estimated real load ~11-15 kW. Missing VFDs, lighting, instruments in calculation.",
            "A/C Thermal Calculation",
            "HIGH",
        ),
        (
            "2",
            "Missing n+1 A/C configuration: Required per ET 5.1.11 and Technical Offer (2 units). Current calculation shows only 1 unit.",
            "A/C Thermal Calculation",
            "HIGH",
        ),
        (
            "3",
            "Material change FRP to PVC: Static Mixer proposed in PVC instead of FRP per Technical Offer. Dimensions also differ, resulting in 71% lower velocity.",
            "Static Mixer",
            "MEDIUM",
        ),
    ]

    for i, row_data in enumerate(observations):
        row = table5.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # CONSOLIDATED DOCUMENT TABLE
    doc.add_heading("CONSOLIDATED DOCUMENT TABLE", level=1)

    doc.add_heading("Delivery 3 - Submittal 25007-0003", level=2)

    table6 = doc.add_table(rows=2, cols=5)
    set_table_borders(table6)

    delivery3 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-DWG-09-009-002-A",
            "P&ID",
            "Design pressures validated per Process Calc Rev B. Minor observations pending (TAGs, battery limits).",
            "2 - Approved as noted",
        ),
    ]

    for i, row_data in enumerate(delivery3):
        row = table6.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Delivery 4 - Submittal 25007-0004", level=2)

    table7 = doc.add_table(rows=2, cols=5)
    set_table_borders(table7)

    delivery4 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-CD-09-004-001-A",
            "Control Architecture",
            "Acceptable. Pending PLC DS and I/O List (received in Submittal 0008).",
            "2 - Approved as noted",
        ),
    ]

    for i, row_data in enumerate(delivery4):
        row = table7.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Delivery 5 - Submittal 25007-0005", level=2)

    table8 = doc.add_table(rows=3, cols=5)
    set_table_borders(table8)

    delivery5 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-CD-09-005-002-A",
            "A/C Thermal Calculation",
            "Thermal load undersized (5.96 kW vs ~11-15 kW real). Missing n+1 config per ET 5.1.11 and Offer.",
            "3 - To be revised",
        ),
        (
            "2",
            "P22-ITEM-09-009-012-A",
            "Static Mixer",
            "Material FRP to PVC requires justification. Dimensions differ from offer (71% lower velocity).",
            "3 - To be revised",
        ),
    ]

    for i, row_data in enumerate(delivery5):
        row = table8.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Delivery 6 - Submittal 25007-0006", level=2)

    table9 = doc.add_table(rows=4, cols=5)
    set_table_borders(table9)

    delivery6 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-ET-09-009-001-B",
            "UHPRO System",
            "Configuration validated per Process Calc. 42 SR + 28 UHP = 70 elements confirmed.",
            "1 - Approved",
        ),
        (
            "2",
            "P22-ET-09-009-003-B",
            "CIP Pump",
            "VFD to Direct start acceptable for CIP application. Motor compatibility noted.",
            "2 - Approved as noted",
        ),
        (
            "3",
            "P22-ET-09-009-006-B",
            "CIP Cartridge Filter",
            "17 cartridges validated per Process Calc (57 m3/hr @ 16.5 m3/hr/m2). Closure type noted.",
            "2 - Approved as noted",
        ),
    ]

    for i, row_data in enumerate(delivery6):
        row = table9.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Delivery 7 - Submittal 25007-0007", level=2)

    table10_d7 = doc.add_table(rows=2, cols=5)
    set_table_borders(table10_d7)

    delivery7 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-CD-09-009-001-B",
            "Process Calculation",
            "Turbocharger modeling validated. Design pressures with 10% margin confirmed. Membrane configuration 6x7 SR + 4x7 UHP = 70 elements. Recovery 42.86%. Minor: summary table recommended.",
            "2 - Approved as noted",
        ),
    ]

    for i, row_data in enumerate(delivery7):
        row = table10_d7.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # DETAILED OBSERVATIONS BY DOCUMENT
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- P&ID ---
    doc.add_heading("P&ID (P22-DWG-09-009-002-A) - APPROVED AS NOTED", level=2)

    para = doc.add_paragraph()
    para.add_run("Status Change: ").bold = True
    para.add_run("Design pressure validation completed. OBS-09 CLOSED.")
    aplicar_arial_12(para)

    table_pid = doc.add_table(rows=15, cols=4)
    set_table_borders(table_pid)

    obs_pid = [
        ("#", "Code", "Observation", "Status"),
        (
            "OBS-01",
            "Battery limits",
            "Indicate ADASA/BW Water supply limit with flange",
            "OPEN",
        ),
        (
            "OBS-02",
            "PVC in SDSS zone",
            "PVC lines found within SDSS zone rectangle",
            "OPEN",
        ),
        ("OBS-03", "Line TAGs", "Indicate line TAG with diameter", "OPEN"),
        ("OBS-04", "Drainage", "This stream should go to drainage", "OPEN"),
        (
            "OBS-05",
            "Battery limit",
            "Indicate BW/ADASA supply limit with flange + TAG + diameter",
            "OPEN",
        ),
        ("OBS-06", "CIP connection", "Goes to CIP TANK TK-09-001", "OPEN"),
        ("OBS-07", "HP Pump", "Include pump characteristics", "OPEN"),
        ("OBS-08", "Stage connection", "Comes from 1st and 2nd stage", "OPEN"),
        (
            "OBS-09",
            "Design pressures",
            "Verify 10% margin vs current ~4%",
            "CLOSED - Process Calc validates 70/85 bar",
        ),
        ("OBS-10", "Super Duplex", "Confirm SDSS material in HP lines", "OPEN"),
        ("OBS-11", "Valve TAGs", "Add valve identification", "OPEN"),
        ("OBS-12", "Instrument TAGs", "Complete instrumentation TAGs", "OPEN"),
        ("OBS-13", "Flow directions", "Verify flow arrows consistency", "OPEN"),
        ("OBS-14", "Legend", "Update legend with all symbols used", "OPEN"),
    ]

    for i, row_data in enumerate(obs_pid):
        row = table_pid.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # --- Control Architecture ---
    doc.add_paragraph()
    doc.add_heading(
        "Control Architecture (P22-CD-09-004-001-A) - APPROVED AS NOTED", level=2
    )

    table_ctrl = doc.add_table(rows=11, cols=4)
    set_table_borders(table_ctrl)

    obs_ctrl = [
        ("#", "Code", "Observation", "Status"),
        ("OBS-01", "PLC Datasheet", "Pending PLC detailed specifications", "OPEN"),
        ("OBS-02", "Communication", "Confirm Modbus TCP/RTU availability", "OPEN"),
        (
            "OBS-03",
            "Ethernet ports",
            "Indicate available Ethernet ports in LCP",
            "OPEN",
        ),
        (
            "OBS-04",
            "I/O count",
            "Verify I/O count vs instrument list",
            "CLOSED - I/O List received",
        ),
        ("OBS-05", "Redundancy", "Confirm controller redundancy if applicable", "OPEN"),
        ("OBS-06", "HMI screens", "Pending HMI screen layout", "OPEN"),
        ("OBS-07", "I/O Signals", "Indicate all IN/OUT signals with P&ID TAGs", "OPEN"),
        (
            "OBS-08",
            "Modbus TCP Map",
            "Provide Modbus TCP memory map and PLC programming specs for DCS integration",
            "OPEN",
        ),
        (
            "OBS-09",
            "VFD Fieldbus",
            "Implement fieldbus communication between VFDs and SCADA for HP Pump and CIP Pump",
            "OPEN",
        ),
        (
            "OBS-10",
            "Power Metering",
            "Clarify total module power consumption metering: via fieldbus or analyzer SAI-09-001?",
            "OPEN",
        ),
    ]

    for i, row_data in enumerate(obs_ctrl):
        row = table_ctrl.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # --- A/C Thermal Calculation ---
    doc.add_paragraph()
    doc.add_heading(
        "A/C Thermal Calculation (P22-CD-09-005-002-A) - TO BE REVISED", level=2
    )

    table_ac = doc.add_table(rows=9, cols=4)
    set_table_borders(table_ac)

    obs_ac = [
        ("#", "Code", "Observation", "Impact"),
        (
            "OBS-01",
            "Thermal load",
            "Calculated 5.96 kW vs estimated real ~10-12 kW",
            "HIGH",
        ),
        (
            "OBS-02",
            "Missing loads",
            "PLC + Instrumentation (2.0 kW), Indoor Lighting (0.16 kW) not included",
            "HIGH",
        ),
        (
            "OBS-03",
            "n+1 config",
            "Missing redundant A/C unit per ET 5.1.11 and Offer (2 A/C 1W+1S)",
            "HIGH",
        ),
        (
            "OBS-04",
            "Load List",
            "Update Electrical Load List with 2x A/C units",
            "MEDIUM",
        ),
        (
            "OBS-05",
            "Heat transmission",
            "Container envelope heat transfer not considered (T_ext=28C, T_int<25C)",
            "MEDIUM",
        ),
        (
            "OBS-06",
            "Solar radiation",
            "Solar heat gain not considered - Taltal is desert coastal zone",
            "MEDIUM",
        ),
        (
            "OBS-07",
            "Safety margin",
            "No contingency factor included (typical 10-15% for HVAC)",
            "LOW",
        ),
        (
            "OBS-08",
            "Design conditions",
            "Design conditions not specified (summer peak vs annual average)",
            "LOW",
        ),
    ]

    for i, row_data in enumerate(obs_ac):
        row = table_ac.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # Detailed Heat Load Analysis table
    para = doc.add_paragraph()
    para.add_run("\nDetailed Heat Load Analysis:").bold = True
    aplicar_arial_12(para)

    table_heat = doc.add_table(rows=8, cols=3)
    set_table_borders(table_heat)

    heat_data = [
        ("Heat Source", "Value (kW)", "Status"),
        ("HP Pump motor losses", "4.26", "Included"),
        ("HP Pump VFD losses", "1.70", "Included"),
        ("PLC + Instrumentation", "2.00", "MISSING"),
        ("Indoor lighting", "0.16", "MISSING"),
        ("Container wall transmission", "~1.0-1.5", "MISSING"),
        ("Solar radiation (desert)", "~0.5-1.0", "MISSING"),
        ("TOTAL ESTIMATED", "~10-12 kW", ""),
    ]

    for i, row_data in enumerate(heat_data):
        row = table_heat.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0 or i == 7:  # Header and total row
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    para = doc.add_paragraph()
    para.add_run("\nAction Required: ").bold = True
    para.add_run(
        "Complete thermal calculation with ALL heat sources (per Load List and environmental conditions), include heat transmission through container walls, consider solar radiation for Taltal location, add safety margin, and include n+1 configuration as required by ET 5.1.11."
    )
    aplicar_arial_12(para)

    # --- Static Mixer ---
    doc.add_paragraph()
    doc.add_heading("Static Mixer (P22-ITEM-09-009-012-A) - TO BE REVISED", level=2)

    table_mixer = doc.add_table(rows=5, cols=4)
    set_table_borders(table_mixer)

    obs_mixer = [
        ("#", "Code", "Observation", "Impact"),
        ("OBS-01", "Material", "Proposed PVC vs FRP in Technical Offer", "MEDIUM"),
        (
            "OBS-02",
            "Dimensions",
            "Different L/D ratio affects mixing efficiency",
            "MEDIUM",
        ),
        ("OBS-03", "Velocity", "71% lower velocity (0.17 vs 0.59 m/s)", "MEDIUM"),
        ("OBS-04", "Brand", "Confirm Koflo equivalence to KOMAX", "LOW"),
    ]

    for i, row_data in enumerate(obs_mixer):
        row = table_mixer.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    para = doc.add_paragraph()
    para.add_run("Action Required: ").bold = True
    para.add_run(
        "Provide technical justification for material change and mixing efficiency validation."
    )
    aplicar_arial_12(para)

    # --- UHPRO System ---
    doc.add_paragraph()
    doc.add_heading("UHPRO System (P22-ET-09-009-001-B) - APPROVED", level=2)

    para = doc.add_paragraph()
    para.add_run("Status Change: ").bold = True
    para.add_run('Upgraded from "Approved as noted" to "Approved".')
    aplicar_arial_12(para)

    table_uhpro = doc.add_table(rows=3, cols=4)
    set_table_borders(table_uhpro)

    obs_uhpro = [
        ("#", "Code", "Observation", "Status"),
        (
            "OBS-01",
            "Membrane table",
            "Include clear table with quantities per model/stage",
            "CLOSED - Process Calc confirms 42 SR + 28 UHP",
        ),
        ("OBS-02", "Code correction", "ITEM to ET corrected in Rev B", "CLOSED"),
    ]

    for i, row_data in enumerate(obs_uhpro):
        row = table_uhpro.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    para = doc.add_paragraph()
    para.add_run("\nValidation Summary from Process Calculation Rev B:")
    aplicar_arial_12(para)
    para = doc.add_paragraph("• Stage 1: 6 vessels × 7 elements = 42 LG SW 400 SR")
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• Stage 2: 4 vessels × 7 elements = 28 LG SW 400 R G2 UHP"
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• Total: 70 membrane elements | Recovery: 42.86% | Capacity: 504 m³/day"
    )
    aplicar_arial_12(para)

    # --- CIP Pump ---
    doc.add_paragraph()
    doc.add_heading("CIP Pump (P22-ET-09-009-003-B) - APPROVED AS NOTED", level=2)

    table_cip_pump = doc.add_table(rows=4, cols=4)
    set_table_borders(table_cip_pump)

    obs_cip_pump = [
        ("#", "Code", "Observation", "Status"),
        (
            "OBS-01",
            "Start type",
            "VFD to Direct start - acceptable for CIP application",
            "CLOSED",
        ),
        ("OBS-02", "Motor", "Different motor specs - verify compatibility", "OPEN"),
        ("OBS-03", "Code correction", "ITEM to ET corrected in Rev B", "CLOSED"),
    ]

    for i, row_data in enumerate(obs_cip_pump):
        row = table_cip_pump.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # --- CIP Cartridge Filter ---
    doc.add_paragraph()
    doc.add_heading(
        "CIP Cartridge Filter (P22-ET-09-009-006-B) - APPROVED AS NOTED", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Status Change: ").bold = True
    para.add_run('Upgraded from "To be revised" to "Approved as noted".')
    aplicar_arial_12(para)

    table_cip_filter = doc.add_table(rows=4, cols=4)
    set_table_borders(table_cip_filter)

    obs_cip_filter = [
        ("#", "Code", "Observation", "Status"),
        (
            "OBS-01",
            "Cartridge count",
            "19 to 17 cartridges - justify capacity",
            "CLOSED - Process Calc validates 17 @ 3.45 m²",
        ),
        (
            "OBS-02",
            "Closure type",
            "Swing Bolts vs Quick Opening - noted",
            "OPEN (minor)",
        ),
        ("OBS-03", "Orientation", "Vertical to Horizontal - noted", "OPEN (minor)"),
    ]

    for i, row_data in enumerate(obs_cip_filter):
        row = table_cip_filter.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # --- Process Calculation ---
    doc.add_paragraph()
    doc.add_heading(
        "Process Calculation (P22-CD-09-009-001-B) - APPROVED AS NOTED", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Status: ").bold = True
    para.add_run(
        "Critical document that validates design parameters. Closes blocking observations."
    )
    aplicar_arial_12(para)

    table_proc_calc = doc.add_table(rows=2, cols=4)
    set_table_borders(table_proc_calc)

    obs_proc_calc = [
        ("#", "Code", "Observation", "Status"),
        (
            "OBS-01",
            "Summary table",
            "Recommend adding summary table at document start",
            "OPEN (minor)",
        ),
    ]

    for i, row_data in enumerate(obs_proc_calc):
        row = table_proc_calc.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    para = doc.add_paragraph()
    para.add_run("\nKey Validations Provided:")
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• Design pressures: Stage 1 = 70 barg, Stage 2 = 85 barg (10% margin confirmed)"
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• Turbocharger modeling: BiTurbo analysis for 43k and 53k TDS - 10 scenarios"
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• HP Pump TDH: 49.4 barg consistent with energy recovery modeling"
    )
    aplicar_arial_12(para)
    para = doc.add_paragraph(
        "• Permeate quality: TDS < 500 mg/L guaranteed in all scenarios"
    )
    aplicar_arial_12(para)

    # REQUIRED ACTIONS
    doc.add_heading("REQUIRED ACTIONS", level=1)

    doc.add_heading("Critical Actions (HIGH Priority)", level=2)

    table12 = doc.add_table(rows=4, cols=4)
    set_table_borders(table12)

    critical_actions = [
        ("#", "Action", "Document", "Status"),
        (
            "1",
            "Provide Process Calculation with turbocharger modeling",
            "Process Calc",
            "RECEIVED & VALIDATED",
        ),
        (
            "2",
            "Complete A/C thermal calculation with ALL loads (~11-15 kW vs 5.96 kW)",
            "A/C Thermal Calc",
            "PENDING",
        ),
        (
            "3",
            "Include n+1 configuration (2x A/C units per ET 5.1.11 and Offer)",
            "A/C Thermal Calc",
            "PENDING",
        ),
    ]

    for i, row_data in enumerate(critical_actions):
        row = table12.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Technical Actions (MEDIUM Priority)", level=2)

    table13 = doc.add_table(rows=9, cols=4)
    set_table_borders(table13)

    tech_actions = [
        ("#", "Action", "Document", "Status"),
        ("4", "Justify material change FRP to PVC", "Static Mixer", "PENDING"),
        (
            "5",
            "Confirm mixing efficiency with new dimensions",
            "Static Mixer",
            "PENDING",
        ),
        (
            "6",
            "Indicate battery limits with flanges at all connection points",
            "P&ID",
            "PENDING",
        ),
        ("7", "Add line TAGs with diameters", "P&ID", "PENDING"),
        ("8", "Review PVC lines within SDSS zone", "P&ID", "PENDING"),
        (
            "9",
            "Provide Modbus TCP memory map for DCS integration",
            "Control Architecture",
            "PENDING",
        ),
        (
            "10",
            "Implement VFD fieldbus for SCADA electrical monitoring",
            "Control Architecture",
            "PENDING",
        ),
        (
            "11",
            "Clarify power consumption metering configuration",
            "Control Architecture",
            "PENDING",
        ),
    ]

    for i, row_data in enumerate(tech_actions):
        row = table13.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Completed Actions", level=2)

    table14 = doc.add_table(rows=6, cols=4)
    set_table_borders(table14)

    completed_actions = [
        ("#", "Action", "Document", "Completion"),
        (
            "A",
            "Process Calculation with turbocharger modeling",
            "P22-CD-09-009-001-B",
            "Jan-14-2026",
        ),
        ("B", "Design pressure validation (10% margin)", "Process Calc", "Jan-26-2026"),
        ("C", "Membrane configuration validation", "Process Calc", "Jan-26-2026"),
        ("D", "CIP Filter capacity justification", "Process Calc", "Jan-26-2026"),
        ("E", "I/O List delivery", "P22-LI-09-008-001-A", "Jan-23-2026"),
    ]

    for i, row_data in enumerate(completed_actions):
        row = table14.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "All reviewed documents with ADASA review comments can be downloaded from the following link:"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Download Link: ").bold = True
    aplicar_arial_12(para)

    # Agregar link Dropbox
    para = doc.add_paragraph()
    run = para.add_run("https://www.dropbox.com/t/INLfLK7p4ISQiAnz")
    run.font.underline = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "\nThis link contains all PDFs with ADASA review comments and annotations."
    )
    aplicar_arial_12(para)

    # Tabla de anexos
    doc.add_paragraph()
    table_attach = doc.add_table(rows=7, cols=3)
    set_table_borders(table_attach)

    attachments = [
        ("#", "Attachment", "Description"),
        (
            "A",
            "P22-DWG-09-009-002_A - P&ID Coment LH.pdf",
            "P&ID with ADASA review comments",
        ),
        (
            "B",
            "P22-ET-09-009-001-B Datasheet of UHPRO System Coment LH.pdf",
            "UHPRO System with annotations",
        ),
        (
            "C",
            "P22-ET-09-009-003-B_Datasheet of RO CIP Pump Coment LH.pdf",
            "CIP Pump with annotations",
        ),
        (
            "D",
            "P22-ITEM-09-009-012-A_Datasheet of Static Mixer Coment LH.pdf",
            "Static Mixer with annotations",
        ),
        (
            "E",
            "P22-CD-09-009-001-B_Process Calculation.pdf",
            "Process Calculation Rev B",
        ),
        (
            "F",
            "CC P22-CD-09-004-001_A CONTROL ARCHITECTURE.pdf",
            "Control Architecture with ADASA review comments",
        ),
    ]

    for i, row_data in enumerate(attachments):
        row = table_attach.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # FOOTER
    doc.add_paragraph()
    para = doc.add_paragraph()
    para.add_run("Document prepared by: ").bold = True
    para.add_run("ADASA")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("January 26, 2026")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Contract: ").bold = True
    para.add_run("C-4300 BW Water - BAE 12803")
    aplicar_arial_12(para)

    # Configurar actualizacion automatica del TOC al abrir
    set_updatefields_true(doc)

    # Guardar documento
    doc.save(output_file)
    print(f"Document generated: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_transmittal()
