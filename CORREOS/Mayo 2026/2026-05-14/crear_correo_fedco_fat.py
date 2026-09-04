#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Fedco EAP Penang 03-Aug-2026 coincides with EXW Shipping date — FAT
mitigation plan requested for Monday 18-May meeting.

Fecha: 14 de mayo de 2026.

Escalation a Eduardo Yamauchi (BW Water) tras la auditoria multi-audit del
correo bundle EP-1 + EP-2 v2.1, donde se detecto que las tres POs Fedco
(BH-09-001 HP Pump, SIP-09-001 Feed Turbo, SIP-09-002 Interstage Turbo) tienen
EAP Penang 03-Aug-2026 = misma fecha que el Shipment EXW del baseline.

Idioma: ingles (BW Water). No aplicar fijar_idioma_documento (default English).
"""

import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-05-14_Fedco-FAT-Conflict.docx")
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
    """Tabla con header en negrita y bordes Table Grid."""
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

    # =========================================================================
    # HEADER
    # =========================================================================
    fields = [
        ("Date:", "May 14, 2026"),
        ("From:", f"{CONTACTO} — Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc."),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, "
            "Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, "
            "Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "ADASA – Taltal: Fedco EAP vs EXW Shipping conflict — "
            "Mitigation plan requested for 18-May (C-4300)",
        ),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / Baseline Schedule 05-Mar-2026 / "
            "Tracker SEMANA 11-05-26",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # SALUDO Y OPENING
    # =========================================================================
    para = doc.add_paragraph("Dear Eduardo,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Following the detailed review of the SEMANA 11-05-26 tracker you "
        "shared on 12-May-2026, ADASA has identified an operational conflict "
        "on the Fedco scope that requires attention before the Monday 18-May "
        "meeting."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # CRITICAL FINDING — FEDCO EAP VS BASELINE EXW
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "Critical finding — Fedco EAP Penang coincides with EXW Shipping"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "The three Fedco items share the same Estimated Arrival Penang as the "
        "baseline EXW Shipping date:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    add_table_with_header(
        doc,
        headers=[
            "Equipment",
            "TAG",
            "PO Date (tracker 11-05)",
            "EAP Penang (tracker 11-05)",
            "Baseline EXW Shipping",
            "Conflict",
        ],
        rows=[
            (
                "RO High Feed Pump",
                "BH-09-001",
                "15-May-2026",
                "03-Aug-2026",
                "03-Aug-2026",
                "Same day",
            ),
            (
                "Feed Turbocharger",
                "SIP-09-001",
                "15-May-2026",
                "03-Aug-2026",
                "03-Aug-2026",
                "Same day",
            ),
            (
                "Interstage Turbocharger",
                "SIP-09-002",
                "15-May-2026",
                "03-Aug-2026",
                "03-Aug-2026",
                "Same day",
            ),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "The baseline FAT window (25-Jul to 01-Aug-2026) closes two days "
        "before the Fedco arrival. The tracker comment “Technical discussion "
        "with supplier took longer than expected” explains the slip but does "
        "not address the FAT/shipping conflict."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SLIP CONTEXT — COMPARISON BETWEEN TRACKERS
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "Slip context — comparison between consecutive trackers"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "Comparing the tracker SEMANA 04-05-26 with SEMANA 11-05-26, the three "
        "Fedco items moved as follows:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    add_table_with_header(
        doc,
        headers=[
            "Field",
            "Tracker SEMANA 04-05-26",
            "Tracker SEMANA 11-05-26",
            "Slip",
        ],
        rows=[
            (
                "PO Date (all three Fedco items)",
                "20-Apr-2026",
                "15-May-2026",
                "+25 days",
            ),
            (
                "EAP Penang (all three Fedco items)",
                "18-Jul-2026",
                "03-Aug-2026",
                "+16 days",
            ),
            (
                "Status RO High Feed Pump BH-09-001",
                "C – Committed",
                "D – Delayed",
                "Reclassified",
            ),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Feed and Interstage Turbochargers carry the same slip but remain "
        "classified as C; ADASA requests classification alignment with the "
        "HP Pump status."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # MITIGATION PLAN REQUEST
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "Mitigation plan requested for Monday 18-May-2026 meeting"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "BW Water is requested to present at the Monday 18-May meeting a "
        "mitigation plan covering:"
    )
    aplicar_arial(para)

    bullets = [
        "FAT execution plan for Fedco (delayed, partial, individual or "
        "alternative arrangement).",
        "Whether EXW Shipping 03-Aug-2026 will be deferred and, if so, the "
        "new window.",
        "Vendor expedite efforts and recovery options.",
        "Impact on downstream milestones (Site Supervision 18-Sep, Training "
        "09-Oct, Close-out 18-Oct) if shipping is deferred.",
    ]
    for texto in bullets:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(texto)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "Written confirmation expected by EOB Friday 22-May-2026."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # DECOUPLING CLAUSE — EP-2 BUNDLE
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "Relationship with the EP-1 + EP-2 bundle proposal"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "For clarity, this FAT clarification request runs in parallel with the "
        "EP-1 + EP-2 bundle proposal sent on 12-May-2026 under Clause 31 BAE "
        "12803, with both tracks proceeding independently."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # CIERRE
    # =========================================================================
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
