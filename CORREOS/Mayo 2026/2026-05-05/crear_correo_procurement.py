#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Procurement Review — Critical alerts for Shipment 03-Aug-2026
Fecha: 5 de Mayo de 2026 (v1.1 — formato tablas)
Cross-check tracker SEMANA 04-05-26 vs baseline 05-Mar-2026.
Status: 5 OK, 5 warning, 7 critical / 17 line items.
3 POs criticas sin emitir + bottleneck Fedco.
Reunion programada 06-May-2026 — correo enviado hoy para revision previa.
"""

import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.table import WD_TABLE_ALIGNMENT

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-05-05_Procurement-Review.docx")
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
    """Crea tabla con header en negrita y bordes (style Table Grid)."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header
    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = header
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True

    # Body
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
        ("Date:", "May 5, 2026"),
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
            "ADASA – Taltal Brine Module: Procurement Review — Critical "
            "alerts for Shipment 03-Aug-2026",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / Baseline Schedule 05-Mar-2026"),
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
        "Procurement review against the 05-Mar-2026 baseline, based on "
        "the week ending 04-May-2026 tracker shared by your team. 90 "
        "days remain to Shipment EXW Penang (03-Aug); 81 days to FAT "
        "(25-Jul)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # STATUS LINE
    para = doc.add_paragraph()
    para.add_run("Status: ").bold = True
    para.add_run("5 OK, 5 warning, 7 critical out of 17 line items.")
    aplicar_arial(para)
    doc.add_paragraph()

    # CRITICAL TABLE
    para = doc.add_paragraph()
    para.add_run("Critical — block baseline shipment").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=["#", "Equipment", "Vendor", "Status", "Action"],
        rows=[
            ("3", "All Valve Set", "Belven",
             "No PO, 11 d past window",
             "Issue PO or change vendor by EOB 12-May"),
            ("6", "CIP Cartridge Filter", "Fil-trek",
             "PO 05-May, 39 d past window",
             "Confirm lead time and Penang arrival ≤17-Jul"),
            ("7", "CIP / Flushing Pumps", "Grundfos",
             "No PO, 35 d past window",
             "Issue PO by EOB 12-May"),
            ("10", "Feed Turbocharger", "Fedco",
             "EAP 18-Jul, slip 46 d",
             "Weekly progress letter; drawing target 08-May"),
            ("11", "Structural Frames", "BW Water",
             "No PO, slip 57 d",
             "Confirm internal MFG status by EOB 08-May"),
            ("16", "RO Cartridge Filter", "Fil-trek",
             "PO 05-May, lead time TBC",
             "Confirm arrival ≤17-Jul"),
            ("17", "RO Membranes", "LG",
             "No PO, 8 d past window",
             "PO + LG lead-time letter (≤11 weeks) by EOB 12-May"),
        ],
    )
    doc.add_paragraph()

    # WARNING TABLE
    para = doc.add_paragraph()
    para.add_run("Warning — slip 10–30 d, recoverable").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=["#", "Equipment", "Vendor", "Status", "Comment"],
        rows=[
            ("1", "RO High Feed Pump", "Fedco",
             "PO 20-Apr, EAP 18-Jul",
             "41 d late on PO; tight margin vs baseline 28-Jul"),
            ("2", "Instrument Set", "Emerson / IFM",
             "PO 29-Apr, EAP 16-Jul",
             "8 d late; slip ~7 d"),
            ("8", "CIP / Flushing Tank", "Dayamas",
             "PO 25-Feb, EAP 19-Jun",
             "Slip 22 d; awaiting drawing approval (nozzle orientation)"),
            ("14", "Interstage Turbocharger", "Fedco",
             "PO 20-Apr, EAP 18-Jul",
             "Slip 23 d; same vendor as HP Pump and Feed Turbo"),
            ("15", "Static Mixer", "N-Spindle",
             "PO 06-May (within window)",
             "EAP TBC; PO date typo '2025-05-06' to correct"),
        ],
    )
    doc.add_paragraph()

    # OK TABLE
    para = doc.add_paragraph()
    para.add_run("OK — aligned with baseline").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=["#", "Equipment", "Vendor", "Status"],
        rows=[
            ("4", "CIP Heater", "Quantic Logic",
             "PO 26-Mar, EAP 26-May (3 d buffer)"),
            ("5", "Container 40' + AC", "Pacific",
             "Arrived 30-Mar (advanced vs baseline 28-Apr)"),
            ("9", "RO Pressure Vessel / Tubes", "Protec Ariswara",
             "PO 20-Apr, EAP 29-May (advanced vs baseline 15-Jun)"),
            ("12", "Antiscalant Dosing Tank", "Promatics",
             "PO 27-Feb, waiting for collection (pickup date pending)"),
            ("13", "Antiscalant Dosing Pumps Skid", "Prominent",
             "PO 16-Mar, waiting for collection (pickup date pending)"),
        ],
    )
    doc.add_paragraph()

    # FEDCO RISK
    para = doc.add_paragraph()
    para.add_run(
        "Concentration risk on Fedco (single vendor for three critical "
        "items): "
    ).bold = True
    para.add_run(
        "RO HP Pump, Feed Turbocharger and Interstage Turbocharger all "
        "carry EAP Penang 18-Jul, leaving 7 days before FAT. Drawing "
        "target 08-May is committed; any slip over 5 days must be "
        "escalated immediately."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # OPERATIONAL NOTES
    para = doc.add_paragraph()
    para.add_run("Operational notes:").bold = True
    aplicar_arial(para)

    notes = [
        "Antiscalant Tank and Antiscalant Dosing Pumps Skid are flagged "
        "'waiting for collection only' — please share the confirmed "
        "pickup date and Penang arrival.",
        "Static Mixer PO date in the tracker reads '2025-05-06'; likely "
        "a typo for 2026-05-06.",
        "Change Log on the tracker has not been updated since 28-Apr; "
        "the three POs issued 5–6 May (CIP Cartridge, RO Cartridge, "
        "Static Mixer) should be logged.",
    ]
    for note in notes:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(note)
        aplicar_arial(para)

    doc.add_paragraph()

    # CLOSING
    para = doc.add_paragraph(
        "We have a meeting scheduled tomorrow (06-May-2026) covering "
        "this scope. Please review this note ahead of the meeting and "
        "come prepared to confirm target dates for the seven critical "
        "items. Written confirmation expected by EOB Friday 08-May-2026."
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
