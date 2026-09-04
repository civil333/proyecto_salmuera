#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - ADASA Evaluation of March 4 Responses
Fecha: 04 de marzo de 2026
Asunto: RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses

Version 4.0 — Versión alternativa en prosa narrativa por ítem.
Estructura: Items with Response Received | Items Not Addressed
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn

OUTPUT_FILE = "2026-03-05_RE-CatchUp-Prose.docx"


# ─────────────────────────── helpers ────────────────────────────────────────

def add_para(doc, text, size=11, bold=False, space_before=0, space_after=6):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(space_before)
    para.paragraph_format.space_after = Pt(space_after)
    run = para.add_run(text)
    run.bold = bold
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_separator(doc):
    para = doc.add_paragraph()
    run = para.add_run("\u2014" * 60)
    run.font.name = "Arial"
    run.font.size = Pt(9)
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after = Pt(4)
    return para


def set_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else tbl.makeelement(qn("w:tblPr"), {})
    borders = tblPr.makeelement(qn("w:tblBorders"), {})
    for border_name in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = borders.makeelement(
            qn(f"w:{border_name}"),
            {
                qn("w:val"): "single",
                qn("w:sz"): "4",
                qn("w:space"): "0",
                qn("w:color"): "000000",
            },
        )
        borders.append(border)
    tblPr.append(borders)
    if tbl.tblPr is None:
        tbl.insert(0, tblPr)


def set_cell_text(cell, text, size=10, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    run = p.add_run(text)
    run.bold = bold
    run.font.name = "Arial"
    run.font.size = Pt(size)


def add_info_table(doc, rows, col_widths, size=10):
    """Tabla 2 columnas: Label | Value."""
    table = doc.add_table(rows=len(rows), cols=2)
    table.autofit = False
    set_table_borders(table)
    for row in table.rows:
        row.cells[0].width = Inches(col_widths[0])
        row.cells[1].width = Inches(col_widths[1])
    for r_idx, (label, value) in enumerate(rows):
        set_cell_text(table.rows[r_idx].cells[0], label, size=size, bold=True)
        set_cell_text(table.rows[r_idx].cells[1], value, size=size)
    doc.add_paragraph()
    return table


def add_section_heading(doc, text):
    """Encabezado de sección en negrita, separado."""
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(10)
    para.paragraph_format.space_after = Pt(6)
    run = para.add_run(text)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)
    return para


def add_item(doc, number, title, body):
    """
    Ítem de prosa: título en negrita seguido de párrafo narrativo.
    Ej: "1. HP Pump Power Rating — Conditional Acceptance (TM N4 OBS-08)"
    """
    # Título del ítem
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(3)
    r = p_title.add_run(f"{number}. {title}")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)

    # Cuerpo en prosa
    p_body = doc.add_paragraph()
    p_body.paragraph_format.space_before = Pt(0)
    p_body.paragraph_format.space_after = Pt(8)
    r2 = p_body.add_run(body)
    r2.font.name = "Arial"
    r2.font.size = Pt(11)


# ─────────────────────────── documento ──────────────────────────────────────

def main():
    doc = Document()

    # Márgenes
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.2)

    # ── Header del correo ──────────────────────────────────────────────────
    header_rows = [
        ("Date:",    "March 5, 2026"),
        ("From:",    "Luis Rivera Gonzalez \u2014 Leader, Infrastructure Engineering (ADASA)"),
        ("To:",      "Eduardo Yamauchi \u2014 Operations Director Americas (BW Water)"),
        ("CC:",      "Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) / "
                     "Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)"),
        ("Subject:", "RE: Catch-Up Schedule Request \u2014 ADASA Evaluation of March 4 Responses"),
        ("Ref:",     "Contract C-4300 / BAE 12803 / "
                     "TM N3 (P22-TM-09-000-003-0) / TM N4 (P22-TM-09-000-004-0)"),
    ]
    add_info_table(doc, header_rows, col_widths=[1.0, 5.3], size=10)

    add_separator(doc)

    # ── Apertura ───────────────────────────────────────────────────────────
    add_para(doc, "Eduardo,", size=11, space_after=6)

    add_para(doc,
        "Regarding your comments in blue in the batch email, we have reviewed each item "
        "against the project technical requirements and the six transmittals issued to date. "
        "Our evaluation is set out below, ordered by urgency.",
        size=11, space_after=10)

    add_separator(doc)

    # ── Sección 1: Items with Response Received ────────────────────────────
    add_section_heading(doc, "Items with Response Received")

    add_item(doc,
        number=1,
        title="HP Pump Power Rating \u2014 Conditional Acceptance (TM N4 OBS-08)",
        body=(
            "CONDITIONAL. Technical Offer Rev1 \u2014 Equipment List states 86\u202fkW; the "
            "confirmed 93\u202fkW creates an 8% discrepancy that bears on the guaranteed SEC of "
            "4.71\u202fkWh/m\u00b3 under the Technical Offer Rev1 \u2014 Guaranteed Performance "
            "and the BAE \u2014 Garant\u00eda de Consumo Energ\u00e9tico. All project documents "
            "must be unified to 93\u202fkW and an updated SEC calculation submitted."
        ),
    )

    add_item(doc,
        number=2,
        title="VM-09-015 Valve Actuation \u2014 Observation Withdrawn (TM N3 OBS-11)",
        body=(
            "OBS-11 WITHDRAWN \u2014 VM-09-015 accepted as a manual isolation valve not subject "
            "to ET \u2014 Actuadores. Note: Valve List Rev B item 18 lists it as ON/OFF MOTORIZED "
            "(Ethernet IP, 380/220\u202fVAC), contradicting your response. Rev C must resolve "
            "the discrepancy."
        ),
    )

    add_item(doc,
        number=3,
        title="IO MODBUS List \u2014 Commitment Registered (TM N4 OBS-04)",
        body=(
            "REGISTERED \u2014 March 6 delivery. List must cover all Modbus TCP/IP data points "
            "per ET \u2014 Communication and Control System."
        ),
    )

    add_item(doc,
        number=4,
        title="Control System Architecture Rev C + UPS \u2014 Commitment Registered (TM N4 OBS-09)",
        body=(
            "REGISTERED \u2014 Rev C due March 6. The document must explicitly state UPS autonomy "
            "\u2265 8\u202fhours; a general reference to UPS inclusion is not sufficient."
        ),
    )

    add_item(doc,
        number=5,
        title="VFD Electrical Variables as AI Signals \u2014 Commitment Registered (TM N3 OBS-15)",
        body=(
            "REGISTERED \u2014 March 6 delivery. AI signals required for HP Pump VFD (Fedco) "
            "and CIP Pump VFD (Grundfos) per ET \u2014 Energy Metering and SEC Verification."
        ),
    )

    add_item(doc,
        number=6,
        title="Container Layout \u2014 Accepted (TM N4 OBS-10)",
        body=(
            "ACCEPTED. Formal document revision required to reflect the confirmed layout."
        ),
    )

    add_separator(doc)

    # ── Sección 2: Items Not Addressed ─────────────────────────────────────
    add_section_heading(doc, "Items Not Addressed in Today\u2019s Response")

    add_item(doc,
        number=7,
        title="SEC Calculation Incorporating Turbocharger Energy Recovery (TM N3 OBS-02)",
        body=(
            "No response received. The guaranteed 4.71\u202fkWh/m\u00b3 (\u00b15%) cannot be "
            "verified without an explicit SEC calculation accounting for turbocharger energy "
            "recovery. A substantive technical response is required \u2014 not a delivery date."
        ),
    )

    add_item(doc,
        number=8,
        title="IO MODBUS External Interface Signals \u2014 Overdue (TM N3 OBS-04/05)",
        body=(
            "OVERDUE. Committed March 3; not delivered, not mentioned today. DO module status "
            "and DI external enable are required for external SCADA integration per "
            "ET \u2014 Communication and Control System."
        ),
    )

    add_item(doc,
        number=9,
        title="A/C Thermal Calculation \u2014 Overdue 15 Days (TM N4 OBS-03)",
        body=(
            "OVERDUE 15 DAYS. Committed February 18; not submitted, not referenced today. "
            "Required by ET \u2014 Air Conditioning System."
        ),
    )

    add_separator(doc)

    # ── Cierre ──────────────────────────────────────────────────────────────
    add_para(doc,
        "Overdue items 8 and 9 must be delivered before the March 9 meeting, together with the "
        "March 6 commitments (items 3, 4, and 5). Formal written responses to TM N3 and TM N4 "
        "\u2014 with documents at incremented revision numbers \u2014 remain due under "
        "Contract C-4300.",
        size=11, space_after=12)

    add_para(doc, "Best regards,", size=11, space_after=6)

    # Firma
    firma = doc.add_paragraph()
    firma.paragraph_format.space_before = Pt(6)
    firma.paragraph_format.space_after = Pt(2)
    r = firma.add_run("Luis Rivera Gonzalez")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)

    for linea in [
        "Leader, Infrastructure Engineering",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
        "BAE 12803 \u2014 Second Stage RO Brine Module Taltal",
    ]:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(linea)
        run.font.name = "Arial"
        run.font.size = Pt(10)

    doc.save(OUTPUT_FILE)
    print(f"Documento generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
