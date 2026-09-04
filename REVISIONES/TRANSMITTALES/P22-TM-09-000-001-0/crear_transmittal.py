#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N°1 ADASA-BW_WATER
Basado en el compilado de revision tecnica, traducido al ingles
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
    """Genera el Transmittal N°1 en formato ADASA"""

    output_file = "TRANSMITTAL N1 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N1 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-001-0",
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

    # ===== CONTENIDO DEL TRANSMITTAL EN INGLES =====

    # EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("December 16, 2025")
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

    table = doc.add_table(rows=4, cols=2)
    set_table_borders(table)

    data = [
        ("Field", "Value"),
        ("Submittal 0001", "25007-0001 (Dec-09-2025) - 13 documents"),
        ("Submittal 0002", "25007-0002 (Dec-15-2025) - 7 documents"),
        ("Total Documents", "20"),
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

    # STATISTICS BY SUBMITTAL
    doc.add_heading("STATISTICS BY SUBMITTAL", level=1)

    doc.add_heading("Submittal 25007-0001 (Delivery 1)", level=2)

    table1 = doc.add_table(rows=6, cols=3)
    set_table_borders(table1)

    data1 = [
        ("Response", "Quantity", "Percentage"),
        ("1 - Approved", "3", "23%"),
        ("2 - Approved as noted", "2", "15%"),
        ("3 - To be revised as noted", "1", "8%"),
        ("4 - Rejected", "3", "23%"),
        ("No response", "4", "31%"),
    ]

    for i, row_data in enumerate(data1):
        row = table1.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Submittal 25007-0002 (Delivery 2)", level=2)

    table2 = doc.add_table(rows=3, cols=3)
    set_table_borders(table2)

    data2 = [
        ("Response", "Quantity", "Percentage"),
        ("1 - Approved", "3", "43%"),
        ("4 - Rejected", "4", "57%"),
    ]

    for i, row_data in enumerate(data2):
        row = table2.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # CRITICAL OBSERVATIONS
    doc.add_heading("CRITICAL OBSERVATIONS", level=1)

    table3 = doc.add_table(rows=5, cols=4)
    set_table_borders(table3)

    observations = [
        ("#", "Observation", "Document", "Severity"),
        (
            "1",
            "CRITICAL: Missing turbocharger modeling to verify HP pump and ERDs",
            "Process Calculation",
            "CRITICAL",
        ),
        (
            "2",
            "IMPORTANT: Design pressures reduced vs proposal (10% margin to ~4%)",
            "PFD, Turbochargers",
            "HIGH",
        ),
        (
            "3",
            "SCOPE CHANGE: Technical proposal specifies LG SW 400 R G2 UHP membranes in BOTH stages (70 units). Now proposed: Stage 1 with CONVENTIONAL membranes LG SW 400 SR (42 units) + Stage 2 with UHP (28 units). Same with vessels (all 1800 PSI in economic proposal). Technically acceptable, but generates ECONOMIC DELTA IN FAVOR OF ADASA. Request price adjustment.",
            "UHPRO System, Process Calc",
            "MEDIUM",
        ),
        (
            "4",
            "Victaulic 2000 PSI coupling not verifiable",
            "Piping Specifications",
            "MEDIUM",
        ),
    ]

    for i, row_data in enumerate(observations):
        row = table3.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # CONSOLIDATED DOCUMENT TABLE
    doc.add_heading("CONSOLIDATED DOCUMENT TABLE", level=1)

    doc.add_heading("Delivery 1 - Submittal 25007-0001", level=2)

    table4 = doc.add_table(rows=14, cols=5)
    set_table_borders(table4)

    delivery1 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-ET-09-000-01",
            "DS Container",
            "5 non-compliances doors/grating, 2-digit coding",
            "4 - Rejected",
        ),
        (
            "2",
            "P22-DWG-09-009-001",
            "PFD",
            "Reduced pressures vs proposal (10% to 4%), indicate TAGs and tie-in N1 pressure",
            "4 - Rejected",
        ),
        ("3", "P22-CD-09-007-001", "Single Line Diagram", "-", "1 - Approved"),
        (
            "4",
            "P22-CD-09-009-001",
            "Process Calculation",
            "CRITICAL: Missing turbocharger modeling to verify HP pump and ERDs",
            "4 - Rejected",
        ),
        (
            "5",
            "P22-ITEM-09-009-001",
            "DS UHPRO System",
            "Indicate membrane/vessel quantities per stage. Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "6",
            "P22-ITEM-09-009-002",
            "DS HP Pump",
            "Material Duplex vs Super Duplex, include RTDs, IP66, pressure rating Cl900",
            "4 - Rejected",
        ),
        (
            "7",
            "P22-ITEM-09-009-003",
            "DS CIP Pump",
            "VFD start vs direct, missing RTDs, IP66, change ITEM to ET",
            "4 - Rejected",
        ),
        (
            "8",
            "P22-ITEM-09-009-004",
            "DS Antiscalant Pump",
            "Frequency must be 50 Hz, change ITEM to ET",
            "2 - Approved as noted",
        ),
        (
            "9",
            "P22-ET-09-006-001",
            "Piping Specification",
            "Verify Victaulic 2000 PSI coupling (brand/model)",
            "1 - Approved",
        ),
        (
            "10",
            "P22-ET-09-006-002",
            "Painting Specification",
            "Verify complete paint system",
            "2 - Approved as noted",
        ),
        (
            "11",
            "P22-ET-09-008-001",
            "DS PLC/HMI",
            "Verify Modbus TCP/RTU availability",
            "2 - Approved as noted",
        ),
        ("12", "P22-LI-09-007-01", "Electrical Load List", "-", "1 - Approved"),
        ("13", "P22-ET-09-007-001", "DS Electrical Aux", "-", "1 - Approved"),
    ]

    for i, row_data in enumerate(delivery1):
        row = table4.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Delivery 2 - Submittal 25007-0002", level=2)

    table5 = doc.add_table(rows=8, cols=5)
    set_table_borders(table5)

    delivery2 = [
        ("#", "Code", "Description", "Comments", "Final Status"),
        (
            "1",
            "P22-ITEM-09-009-005",
            "DS RO Cartridge Filter",
            "Indicate suspended solids, element quantity and area. Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "2",
            "P22-ITEM-09-009-006",
            "DS CIP Cartridge Filter",
            "Indicate element quantity and area. Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "3",
            "P22-ITEM-09-009-007",
            "DS Feed Turbocharger",
            "IMPORTANT: Pressures with 10% margin (not 4%), Cl900 flanges. Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "4",
            "P22-ITEM-09-009-008",
            "DS Interstage Turbocharger",
            "Pressures with 10% margin, Cl900 lb flanges. Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "5",
            "P22-ITEM-09-009-009",
            "DS CIP Tank",
            "Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "6",
            "P22-ITEM-09-009-010",
            "DS Antiscalant Tank",
            "Change ITEM to ET",
            "3 - To be revised",
        ),
        (
            "7",
            "P22-ITEM-09-009-011",
            "DS CIP Tank Heater",
            "Change ITEM to ET",
            "3 - To be revised",
        ),
    ]

    for i, row_data in enumerate(delivery2):
        row = table5.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # CONSOLIDATED STATISTICS
    doc.add_heading("CONSOLIDATED STATISTICS", level=1)

    doc.add_heading("Consolidated Final Status", level=2)

    table6 = doc.add_table(rows=5, cols=5)
    set_table_borders(table6)

    stats = [
        ("Verdict", "Delivery 1", "Delivery 2", "Total", "%"),
        ("1 - Approved", "4", "0", "4", "20%"),
        ("2 - Approved as noted", "3", "0", "3", "15%"),
        ("3 - To be revised", "1", "7", "8", "40%"),
        ("4 - Rejected", "5", "0", "5", "25%"),
    ]

    for i, row_data in enumerate(stats):
        row = table6.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Rejected Documents - Require Re-submission", level=2)

    table7 = doc.add_table(rows=6, cols=4)
    set_table_borders(table7)

    rejected = [
        ("#", "Code", "Description", "Main Reason"),
        (
            "1",
            "P22-ET-09-000-01",
            "DS Container",
            "Doors/grating not specified (ET 5.1.10)",
        ),
        ("2", "P22-DWG-09-009-001", "PFD", "Reduced pressures vs proposal (10% to 4%)"),
        (
            "3",
            "P22-CD-09-009-001",
            "Process Calculation",
            "Missing turbocharger modeling (CRITICAL)",
        ),
        (
            "4",
            "P22-ITEM-09-009-002",
            "DS HP Pump",
            "Material Duplex vs Super Duplex, RTDs, IP rating",
        ),
        (
            "5",
            "P22-ITEM-09-009-003",
            "DS CIP Pump",
            "VFD start vs direct, missing RTDs",
        ),
    ]

    for i, row_data in enumerate(rejected):
        row = table7.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # REQUIRED ACTIONS
    doc.add_heading("REQUIRED ACTIONS", level=1)

    doc.add_heading("Critical Actions (HIGH Priority)", level=2)

    table8 = doc.add_table(rows=6, cols=3)
    set_table_borders(table8)

    critical_actions = [
        ("#", "Action", "Responsible"),
        ("1", "Include turbocharger modeling for both salinities", "BW Water"),
        ("2", "Correct design pressures to 10% margin (83.9 bar)", "BW Water"),
        ("3", "Resize HP pump increasing TDH", "BW Water"),
        ("4", "Deliver DS Container with ET 5.1.10 modifications", "BW Water"),
        ("5", "Clarify HP pump material: Duplex vs Super Duplex", "BW Water"),
    ]

    for i, row_data in enumerate(critical_actions):
        row = table8.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Technical Actions (MEDIUM Priority)", level=2)

    table9 = doc.add_table(rows=8, cols=3)
    set_table_borders(table9)

    tech_actions = [
        ("#", "Action", "Responsible"),
        ("6", "Indicate membrane/vessel quantities per stage", "BW Water"),
        ("7", "Indicate filtration rate and filter elements", "BW Water"),
        ("8", "Specify Victaulic 2000 PSI coupling brand/model", "BW Water"),
        ("9", "Specify Cl 900 lb flanges on turbochargers", "BW Water"),
        ("10", "Confirm 3-wire RTD inclusion in pumps", "BW Water"),
        ("11", "Correct antiscalant pump frequency to 50 Hz", "BW Water"),
        ("12", "Confirm IP66 on HP and CIP pumps", "BW Water"),
    ]

    for i, row_data in enumerate(tech_actions):
        row = table9.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    doc.add_paragraph()
    doc.add_heading("Administrative Actions (LOW Priority)", level=2)

    table10 = doc.add_table(rows=4, cols=3)
    set_table_borders(table10)

    admin_actions = [
        ("#", "Action", "Responsible"),
        ("13", "Correct document coding ITEM to ET (12 documents)", "BW Water"),
        (
            "14",
            "Economic adjustment for conventional Stage 1 membranes",
            "Administrative",
        ),
        ("15", "Verify Modbus availability in PLC", "BW Water"),
    ]

    for i, row_data in enumerate(admin_actions):
        row = table10.rows[i]
        for j, value in enumerate(row_data):
            row.cells[j].text = value
            if i == 0:
                set_repeat_table_header(row)
                for para in row.cells[j].paragraphs:
                    for run in para.runs:
                        run.bold = True

    # PENDING DOCUMENTS
    doc.add_heading("PENDING DOCUMENTS FOR DELIVERY", level=1)

    para = doc.add_paragraph(
        "According to BW Water schedule, the following documents are pending:"
    )
    aplicar_arial_12(para)

    table11 = doc.add_table(rows=9, cols=3)
    set_table_borders(table11)

    pending = [
        ("#", "Document", "Status"),
        ("1", "Control System Architecture", "PENDING"),
        ("2", "Utility Consumption List", "PENDING"),
        ("3", "Chemical and Consumption List", "PENDING"),
        ("4", "Line List", "PENDING"),
        ("5", "Instrument List", "PENDING"),
        ("6", "Valve List", "PENDING"),
        ("7", "DS MCC", "PENDING"),
        ("8", "A/C Thermal Calculation", "PENDING"),
    ]

    for i, row_data in enumerate(pending):
        row = table11.rows[i]
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
        "All reviewed documents with annotations can be downloaded from the following link:"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Download Link: ").bold = True
    aplicar_arial_12(para)

    # Agregar hyperlink
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), "")

    # Crear el run con el texto del link
    run_element = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")

    # Estilo de hyperlink (azul subrayado)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0000FF")
    rPr.append(color)

    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rPr.append(underline)

    run_element.append(rPr)

    text = OxmlElement("w:t")
    text.text = "https://www.dropbox.com/t/XYhHFZ4DFb7D54iG"
    run_element.append(text)

    # Agregar como texto simple con formato de link
    para = doc.add_paragraph()
    run = para.add_run("https://www.dropbox.com/t/XYhHFZ4DFb7D54iG")
    run.font.color.rgb = None  # Reset para usar estilo
    run.font.underline = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\nThis link contains all PDFs with review comments and annotations.")
    aplicar_arial_12(para)

    # FOOTER
    doc.add_paragraph()
    para = doc.add_paragraph()
    para.add_run("Document prepared by: ").bold = True
    para.add_run("ADASA")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Date: ").bold = True
    para.add_run("December 16, 2025")
    aplicar_arial_12(para)

    # Guardar documento
    doc.save(output_file)
    print(f"Document generated: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_transmittal()
