#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Respuesta a Propuesta 25007-PL-0001 rev.1 — Cambio de Layout CIP
Fecha: 16 de Marzo de 2026
Destinatario: Eduardo Yamauchi — BW Water Americas Inc.
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_FILE = "2026-03-16_Response-Layout-Proposal.docx"
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11, bold=False, italic=False):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
        if bold:
            run.bold = True
        if italic:
            run.italic = True


def agregar_campo_header(doc, label, value):
    para = doc.add_paragraph()
    run_label = para.add_run(label)
    run_label.bold = True
    run_label.font.name = "Arial"
    run_label.font.size = Pt(11)
    run_value = para.add_run(f" {value}")
    run_value.font.name = "Arial"
    run_value.font.size = Pt(11)
    return para


def agregar_seccion(doc, titulo):
    para = doc.add_paragraph()
    run = para.add_run(titulo)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.underline = True
    return para


def agregar_parrafo(doc, texto, size=11):
    para = doc.add_paragraph(texto)
    for run in para.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def agregar_tabla_schedule(doc):
    """Tabla: committed delivery dates per BW Water's own schedule."""
    headers = ["Document Category", "Committed Date"]
    filas = [
        ("Instrument & Control drawings (Instrument Layout)", "Mon Nov 3, 2025"),
        ("Electrical drawings (Cable Tray, Grounding layouts)", "Fri Nov 7, 2025"),
        ("Equipment Layout", "Fri Dec 5, 2025"),
        ("Piping Layout", "Tue Dec 30, 2025"),
        ("3D Model", "Mon Dec 29, 2025"),
    ]

    table = doc.add_table(rows=1 + len(filas), cols=2)
    table.style = "Table Grid"

    # Header
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        run = hdr[i].paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(10)

    # Data
    for r, (doc_cat, date) in enumerate(filas, start=1):
        cells = table.rows[r].cells
        for c, val in enumerate([doc_cat, date]):
            run = cells[c].paragraphs[0].add_run(val)
            run.font.name = "Arial"
            run.font.size = Pt(10)

    # Column widths
    for row in table.rows:
        row.cells[0].width = Inches(4.0)
        row.cells[1].width = Inches(2.0)

    doc.add_paragraph()


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(1.1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "March 16, 2026"),
        ("From:", f"{CONTACTO} \u2014 Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, "
            "Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "RE: 25007 Taltal \u2013 Proposal for Layout Changes (25007-PL-0001 rev.1)",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803"),
    ]
    for label, value in fields:
        agregar_campo_header(doc, label, value)

    doc.add_paragraph()

    # ── SALUDO ───────────────────────────────────────────────────────────────
    agregar_parrafo(doc, "Dear Eduardo,")
    doc.add_paragraph()

    # ── APERTURA ─────────────────────────────────────────────────────────────
    agregar_parrafo(
        doc,
        "We acknowledge receipt of Proposal 25007-PL-0001 rev.1 (March\u00a014,\u00a02026). "
        "This email constitutes ADASA\u2019s acceptance of the proposal. BW Water may proceed "
        "with the work. The following points must be resolved in the updated proposal "
        "before final commercial close.",
    )
    doc.add_paragraph()

    # ── RECORD ───────────────────────────────────────────────────────────────
    agregar_parrafo(doc, "For the record:")
    doc.add_paragraph()

    bullets = [
        (
            "Feb 23, 2026:",
            "Transmittal N5 (P22-TM-09-000-005-1) formally established the maximum CIP "
            "connection distance of 3.5\u00a0m from the module boundary. This constraint was "
            "in writing before BW Water submitted the Piping Layout.",
        ),
        (
            "Mar 6, 2026:",
            "Piping Layout received via Submittal 25007-0014 \u2014 66 calendar days past the "
            "December\u00a030 deadline. CIP connections shown at 11,150\u00a0mm: more than three "
            "times the documented limit.",
        ),
        (
            "Mar 8, 2026:",
            "ADASA issued Transmittal N7 (Code\u00a03) within 48 hours of receipt. "
            "The revisions now required are a direct consequence of a non-conforming "
            "delivery that ignored a written constraint already on record.",
        ),
    ]

    for date_label, description in bullets:
        para = doc.add_paragraph(style="List Bullet")
        run_date = para.add_run(date_label)
        run_date.bold = True
        run_date.font.name = "Arial"
        run_date.font.size = Pt(11)
        run_desc = para.add_run(f" {description}")
        run_desc.font.name = "Arial"
        run_desc.font.size = Pt(11)

    doc.add_paragraph()

    # ── SCOPE ────────────────────────────────────────────────────────────────
    agregar_parrafo(
        doc,
        "On scope: ADASA accepts the four documents where the technical dependency on the "
        "CIP relocation is evident \u2014 Piping Layout (P22-DWG-09-005-004), Tie-In Points "
        "(P22-DWG-09-005-005), Equipment Layout, and 3D Model. For the three documents "
        "below, we cannot confirm the dependency without additional justification. All three "
        "cover systems inside the module container; the CIP relocation is external. Cable "
        "Tray Layout was approved Code\u00a01 in Transmittal N4 with no observations.",
    )
    doc.add_paragraph()

    disputed = [
        "Instrument Layout (P22-DWG-09-008-001)",
        "Grounding Point & Power Panel Layout (P22-DWG-09-007-003)",
        "Cable Tray Layout (P22-DWG-09-007-004)",
    ]
    for item in disputed:
        para = doc.add_paragraph(style="List Number")
        run = para.add_run(item)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    doc.add_paragraph()

    # ── UPDATED PROPOSAL ─────────────────────────────────────────────────────
    agregar_parrafo(
        doc,
        "We ask BW Water to submit an updated proposal today addressing the following:",
    )
    doc.add_paragraph()

    requests = [
        (
            "(a)",
            "For the three internal-module documents: a brief technical justification "
            "tracing the specific dependency on the CIP relocation, or their removal "
            "from the proposal scope.",
        ),
        (
            "(b)",
            "A revised timeline integrated with the overall engineering recovery plan "
            "and the FAT schedule.",
        ),
        (
            "(c)",
            "Commercial terms consistent with the documented delivery history.",
        ),
    ]

    for label, text in requests:
        para = doc.add_paragraph()
        run_label = para.add_run(label)
        run_label.bold = True
        run_label.font.name = "Arial"
        run_label.font.size = Pt(11)
        run_text = para.add_run(f"  {text}")
        run_text.font.name = "Arial"
        run_text.font.size = Pt(11)
        para.paragraph_format.left_indent = Inches(0.25)

    doc.add_paragraph()

    para = doc.add_paragraph()
    run = para.add_run(
        "If we do not receive the updated proposal today, ADASA will close commercially "
        "on the four documents with evident technical dependency only. The three "
        "internal-module documents will remain on hold pending justification."
    )
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)
    doc.add_paragraph()

    agregar_parrafo(doc, "Please confirm receipt of this message. We require BW Water\u2019s response by end of business today, March\u00a016,\u00a02026.")
    doc.add_paragraph()

    # ── FIRMA ────────────────────────────────────────────────────────────────
    agregar_parrafo(doc, "Best regards,")
    doc.add_paragraph()

    para = doc.add_paragraph()
    run = para.add_run(CONTACTO)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)

    for line in [
        "Project Engineer",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
    ]:
        agregar_parrafo(doc, line)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
