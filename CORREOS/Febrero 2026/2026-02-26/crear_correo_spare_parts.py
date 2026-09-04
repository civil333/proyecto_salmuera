#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Spare Parts Quotation — Formal Re-validation & Missing Turbocharger Service Kits
Fecha:  26 de febrero de 2026
Ref:    Contract C-4300 / BAE 12803 / BWWA Ref. 20.24.6501.F Rev.1
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import set_table_borders, calcular_anchos_columnas

from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT_FILE = "2026-02-26_Spare-Parts-Revalidation-Turbocharger-Kits.docx"
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def set_cell_background(cell, hex_color):
    """Sets cell background shading color."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def add_table(doc, data, header_color="D9E2F3"):
    """Crea tabla con anchos dinámicos, bordes y header coloreado."""
    anchos = calcular_anchos_columnas(data, len(data[0]))
    table = doc.add_table(rows=len(data), cols=len(data[0]))
    set_table_borders(table)
    for i, row_data in enumerate(data):
        row = table.rows[i]
        for j, value in enumerate(row_data):
            cell = row.cells[j]
            cell.text = value
            if i == 0:
                set_cell_background(cell, header_color)
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    if i == 0:
                        run.bold = True
    if anchos:
        for row in table.rows:
            for j, cell in enumerate(row.cells):
                if j < len(anchos):
                    cell.width = anchos[j]
    return table


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "February 26, 2026"),
        ("From:", f"{CONTACTO} \u2014 Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        ("To:", "Andrea \u2014 BW Water Americas Inc."),
        (
            "Subject:",
            "Spare Parts Quotation \u2014 Formal Re-validation & Missing Turbocharger Service Kits",
        ),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / BWWA Ref. 20.24.6501.F Rev.1",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ── SALUDO ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear Eduardo and Andrea,")
    aplicar_arial(para)
    doc.add_paragraph()

    # ── PÁRRAFO 1: Contexto y solicitud de re-validación ─────────────────────
    para = doc.add_paragraph(
        "I am writing regarding the spare parts quotation included in the BW Water economic "
        "offer (BWWA Ref. 20.24.6501.F Rev.1, September 2025), specifically Section 3.8 \u2014 "
        "Recommended Two-Year Spare Parts (USD\u00a043,790.00, optional). This quotation was "
        "issued more than five months ago, and ADASA has not yet formally accepted or "
        "rejected this optional line item. Before any procurement decision is made, ADASA "
        "requires a formal re-validation of the pricing, scope, and commercial conditions \u2014 "
        "including confirmation that the quoted prices remain valid and that no scope changes "
        "have occurred since the original submission."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── PÁRRAFO 2: Observación técnica — gap turbocharger ────────────────────
    para = doc.add_paragraph(
        "A review of Section 3.8 / Section 15 of the Technical Offer (\u201cRecommended "
        "Two-Year Spare Parts List\u201d) shows that the list covers the HP pump "
        "(Fedco MSD-130), dosing pumps (Pulsafeeder), RO vessel components, sensors, and "
        "valves. However, the list does not include any service or repair kit, wear parts, or "
        "consumables for the energy recovery turbochargers: SIP-09-001 (Feed Turbocharger) "
        "and SIP-09-002 (Inter-stage Turbocharger). These are critical rotating components of "
        "the UHPRO system, designed for continuous 24/7 operation. Their exclusion from the "
        "two-year spare parts recommendation constitutes a gap that ADASA cannot accept "
        "without a formal technical justification from BW Water."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── PÁRRAFO 3: Acciones requeridas ───────────────────────────────────────
    para = doc.add_paragraph(
        "ADASA requests that BW Water address the following two items:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    items = [
        (
            "1.",
            "Formal re-validation of Section 3.8 spare parts quotation \u2014 "
            "Confirm that the prices listed in BWWA Ref. 20.24.6501.F Rev.1 Section 3.8 "
            "(USD\u00a043,790.00) remain valid, provide an updated validity date, and confirm "
            "that the scope has not changed since September 2025.",
        ),
        (
            "2.",
            "Complement the spare parts list with turbocharger service kits \u2014 "
            "Provide a recommended service/repair kit for SIP-09-001 (Feed Turbocharger) "
            "and SIP-09-002 (Inter-stage Turbocharger), including: part descriptions, "
            "manufacturer part numbers, recommended quantities for two years of operation, "
            "and unit pricing.",
        ),
    ]
    for bullet, text in items:
        para = doc.add_paragraph()
        para.add_run(bullet + " ").bold = True
        para.add_run(text)
        para.paragraph_format.left_indent = Inches(0.3)
        aplicar_arial(para)

    doc.add_paragraph()

    # ── TABLA: Resumen de requerimientos ─────────────────────────────────────
    para = doc.add_paragraph()
    para.add_run("Summary of Requirements:").bold = True
    aplicar_arial(para)
    doc.add_paragraph()

    table_data = [
        ("#", "Requirement", "Reference", "Priority"),
        (
            "1",
            "Formal re-validation of spare parts quotation (Section 3.8)",
            "BWWA Ref. 20.24.6501.F Rev.1",
            "High",
        ),
        (
            "2",
            "Add service/repair kit \u2014 SIP-09-001 Feed Turbocharger",
            "Section 15 OT / Section 3.8 Economic Offer",
            "High",
        ),
        (
            "3",
            "Add service/repair kit \u2014 SIP-09-002 Inter-stage Turbocharger",
            "Section 15 OT / Section 3.8 Economic Offer",
            "High",
        ),
    ]
    add_table(doc, table_data)

    doc.add_paragraph()

    # ── CIERRE ────────────────────────────────────────────────────────────────
    para = doc.add_paragraph(
        "Please provide your response by Friday, March 7, 2026. If a coordination call "
        "would help clarify the scope of what is required, I am available at short notice "
        "\u2014 please propose a time and I will confirm immediately. Please also confirm "
        "receipt of this request."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ─────────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Contract Administrator",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
        "Project: BAE 12803 \u2014 Second Stage RO Brine Module Taltal",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
