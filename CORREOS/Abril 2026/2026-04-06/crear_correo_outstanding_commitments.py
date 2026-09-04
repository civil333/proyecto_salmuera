"""
Correo: Outstanding Commitments — Layout Revisions & Procurement Log
Fecha: 06-Apr-2026
Codigo: CORREO-2026-04-06-OUTSTANDING-COMMITMENTS
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-04-06_Outstanding-Commitments-Layouts-PO-Log.docx")


def set_font(run, name="Arial", size=11, bold=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_para(doc, text="", bold=False, size=11, space_before=0, space_after=6, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align:
        p.alignment = align
    if text:
        run = p.add_run(text)
        set_font(run, bold=bold, size=size)
    return p


def add_table(doc, headers, rows, col_widths=None, font_size=10):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"

    # Header row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        for run in hdr_cells[i].paragraphs[0].runs:
            set_font(run, bold=True, size=font_size)
        tc = hdr_cells[i]._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "D9D9D9")
        tcPr.append(shd)

    # Data rows
    for ri, row_data in enumerate(rows):
        cells = table.rows[ri + 1].cells
        for ci, val in enumerate(row_data):
            cells[ci].text = val
            for run in cells[ci].paragraphs[0].runs:
                set_font(run, size=font_size)

    # Column widths
    if col_widths:
        for row in table.rows:
            for ci, width in enumerate(col_widths):
                row.cells[ci].width = Cm(width)

    return table


def add_separator(doc):
    sep = doc.add_paragraph()
    sep.paragraph_format.space_before = Pt(0)
    sep.paragraph_format.space_after = Pt(10)
    pPr = sep._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "999999")
    pBdr.append(bottom)
    pPr.append(pBdr)


def main():
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.0)

    # --- HEADER ---
    add_para(doc, "ADASA — Aguas de Antofagasta S.A.", bold=True, size=12, space_after=2)
    add_para(doc, "Contract C-4300 | Project 12803 — Taltal SWRO", size=10, space_after=8)

    # --- SUBJECT BLOCK ---
    subj = add_para(doc, space_before=0, space_after=4)
    r = subj.add_run("Subject: ")
    set_font(r, bold=True, size=11)
    r2 = subj.add_run(
        "Project 12803 — Taltal SWRO | Outstanding Commitments — "
        "Layout Revisions & Procurement Log | April 6, 2026"
    )
    set_font(r2, size=11)

    for label, value in [
        ("Date: ", "April 6, 2026"),
        ("To: ", "Eduardo Yamauchi — BW Water Americas Inc."),
        (
            "CC: ",
            "Jeryl F. Regulacion, Adzlan Bin Abd Rahim, Sadeep Irugalbandara, Nick Huta; "
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes",
        ),
        ("From: ", "Luis Rivera — Contract Administrator (ADASA)"),
    ]:
        p = add_para(doc, space_before=0, space_after=2)
        r = p.add_run(label)
        set_font(r, bold=True, size=11)
        r2 = p.add_run(value)
        set_font(r2, size=11)

    add_separator(doc)

    # --- SALUTATION ---
    add_para(doc, "Dear Eduardo,", size=11, space_after=8)
    add_para(
        doc,
        "We are following up on two commitments from BW Water that remain outstanding "
        "as of today.",
        size=11,
        space_after=12,
    )

    # =================================================================
    # SECTION 1 — LAYOUT REVISIONS & CHANGE ORDER
    # =================================================================
    add_para(
        doc,
        "1. Layout Revisions & Change Order 25007-PL-0001 — Pending Formal Submittals",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "Our email of April 1 requested delivery of three revised drawings by "
        "April 3, 2026. ADASA has reviewed preliminary versions of the documents "
        "listed below (items 1\u20134), however the formal submittal has not been "
        "received. All deliverables are required in PDF and native format (DWG), "
        "with STEP/IGES additionally for the 3D model.",
        size=11, space_after=8,
    )

    add_table(
        doc,
        headers=["#", "Document", "Drawing No.", "Rev.", "Format", "Status"],
        rows=[
            ["1", "Equipment Layout", "P22-DWG-09-005-003", "C", "PDF + DWG", "Reviewed \u2014 formal submittal pending"],
            ["2", "Piping Layout", "P22-DWG-09-005-004", "B", "PDF + DWG", "Reviewed \u2014 formal submittal pending"],
            ["3", "Tie-In Point Layout", "P22-DWG-09-005-005", "C", "PDF + DWG", "Reviewed \u2014 formal submittal pending"],
            ["4", "3D Model \u2014 CIP Area", "per CO 25007-PL-0001", "\u2014", "DWG + STEP/IGES", "Reviewed \u2014 formal submittal pending"],
        ],
        col_widths=[0.7, 3.2, 3.5, 0.7, 2.8, 4.3],
    )
    add_para(doc, space_after=6)

    add_para(
        doc,
        "Additionally, two documents included in Change Order 25007-PL-0001 rev.2 "
        "have not been received in any form:",
        size=11, space_after=8,
    )

    add_table(
        doc,
        headers=["#", "Document", "Drawing No.", "Format", "Status"],
        rows=[
            ["5", "Instrument Layout", "P22-DWG-09-008-001", "PDF + DWG", "Not received"],
            ["6", "Grounding Point & Power Panel Layout", "P22-DWG-09-007-003", "PDF + DWG", "Not received"],
        ],
        col_widths=[0.7, 5.5, 3.5, 2.5, 2.8],
    )
    add_para(doc, space_after=10)

    # =================================================================
    # SECTION 2 — PROCUREMENT LOG
    # =================================================================
    add_para(
        doc,
        "2. Procurement Log — April 2 Meeting Commitment Not Met",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "During our meeting of April 2, 2026, BW Water committed to provide an updated "
        "Procurement Log reflecting the current status of all purchase orders against the "
        "Baseline Schedule (05-Mar-2026). This document has not been received.",
        size=11, space_after=12,
    )

    # =================================================================
    # SECTION 3 — PROCUREMENT STATUS REVIEW
    # =================================================================
    add_para(
        doc,
        "3. Procurement Status Review — Baseline Schedule Compliance",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "ADASA has reviewed the current procurement status against the Baseline Schedule. "
        "The tables below summarize the position of each procurement line as of April 6, 2026.",
        size=11, space_after=10,
    )

    # --- 3a: POs Confirmed ---
    add_para(doc, "POs Confirmed (4 items):", bold=True, size=10, space_after=6)
    add_table(
        doc,
        headers=["Equipment", "PO Reference", "PR/PO Window", "Status"],
        rows=[
            ["CIP Tank Heater", "BW-PO-2026M062", "Mar 16 – 20", "Confirmed"],
            ["Container (40')", "Penang workshop", "Mar 18 – 24", "In production"],
            ["CIP / Flushing Tank", "BW-PO-2026M073", "Mar 27 – Apr 2", "Confirmed"],
            ["Antiscalant Dosing Pump", "BW-PO-2026M089", "Apr 10 – 16", "Confirmed (early)"],
        ],
        col_widths=[4.5, 3.5, 3.0, 3.0],
        font_size=9,
    )
    add_para(doc, space_after=10)

    # --- 3b: PO Windows Overdue ---
    add_para(
        doc,
        "PO Windows Overdue — No Confirmation Received (5 items):",
        bold=True, size=10, space_after=6,
    )
    add_table(
        doc,
        headers=["Equipment", "PR/PO Window", "Days Overdue", "Eng. Status", "Remarks"],
        rows=[
            [
                "RO High Feed Pump",
                "Mar 4 – 10",
                "27",
                "Code 2 (TM N6)",
                'Last status "in progress" (Mar 9)',
            ],
            [
                "Instrument Set",
                "Mar 11 – 17",
                "20",
                "Code 3 (TM N10)",
                "IO List Rev C not received",
            ],
            [
                "All Valve Set",
                "Mar 11 – 17",
                "20",
                "Code 3 (TM N11)",
                "Valve List Rev D not received",
            ],
            [
                "CIP/Flush. Cartridge Filter",
                "Mar 23 – 27",
                "10",
                "Code 2 (TM N11)",
                "PO enabled — clarification sent Mar 26",
            ],
            [
                "CIP / Flushing Pumps",
                "Mar 25 – 31",
                "6",
                "Code 2 (TM N11)",
                "PO enabled — same as above",
            ],
        ],
        col_widths=[3.5, 2.5, 1.8, 2.8, 4.5],
        font_size=9,
    )
    add_para(doc, space_after=10)

    # --- 3c: PO Windows Active This Week ---
    add_para(
        doc,
        "PO Windows Active This Week (3 items):",
        bold=True, size=10, space_after=6,
    )
    add_table(
        doc,
        headers=["Equipment", "PR/PO Window", "Closes", "Engineering Constraint"],
        rows=[
            [
                "RO Pressure Vessel / Tubes",
                "Mar 31 – Apr 6",
                "Today",
                "Code 1 — open question on UHPRO scope (since Mar 23)",
            ],
            [
                "Feed Turbocharger (SIP-09-001)",
                "Apr 1 – 7",
                "Tomorrow",
                "Code 2 (TM N11) — PO enabled",
            ],
            [
                "Structural Frames / Supports",
                "Apr 6 – 10",
                "Friday",
                "No datasheet. Layouts pending (geometry dependency)",
            ],
        ],
        col_widths=[4.0, 2.8, 2.0, 6.5],
        font_size=9,
    )
    add_para(doc, space_after=10)

    # --- 3d: Next Week ---
    add_para(
        doc,
        "PO Windows Opening Next Week (1 item):",
        bold=True, size=10, space_after=6,
    )
    add_table(
        doc,
        headers=["Equipment", "PR/PO Window", "Engineering Status"],
        rows=[
            ["Antiscalant Dosing Tank", "Apr 7 – 13", "Code 2 (TM N13) — PO enabled"],
        ],
        col_widths=[5.0, 3.5, 6.5],
        font_size=9,
    )
    add_para(doc, space_after=10)

    # --- Summary paragraph ---
    add_para(
        doc,
        "Of the 16 procurement lines in the Baseline Schedule, only four have confirmed POs "
        "(25%). Five PO windows are overdue without confirmation. Three PO windows are active "
        "this week, of which the Structural Frames / Supports line is conditioned by the "
        "layout revisions requested in Section 1 above.",
        size=11, space_after=8,
    )
    add_para(
        doc,
        "ADASA requires the updated Procurement Log to verify schedule compliance across "
        "all these lines. Instrument Set and All Valve manufacturing deadlines "
        "(July 9, 2026) coincide with the engineering completion milestone — "
        "there is zero schedule float on these items.",
        size=11, space_after=14,
    )

    # =================================================================
    # ACTION REQUIRED
    # =================================================================
    add_para(
        doc,
        "Action Required by April 7, 2026",
        bold=True, size=11, space_after=6,
    )
    add_para(doc, "Please provide:", size=11, space_after=4)

    items = [
        "a) Formal submittals for items 1\u20134, and first delivery of items 5\u20136, "
        "all in PDF + DWG (plus STEP/IGES for the 3D model).",
        "b) The updated Procurement Log against the Baseline Schedule 05-Mar-2026, "
        "covering all 16 procurement lines with PO status, PO references, "
        "and confirmed or expected PO dates.",
        "c) Confirmation of receipt of this email.",
    ]
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(1.0)
        run = p.add_run(item)
        set_font(run, size=11)

    add_para(doc, space_before=6, space_after=14)
    add_para(
        doc,
        "Please confirm your revised delivery dates by return.",
        size=11, space_after=16,
    )

    # --- SIGNATURE ---
    add_para(doc, "Best regards,", size=11, space_after=8)
    add_para(doc, "Luis Rivera", bold=True, size=11, space_after=2)
    add_para(
        doc,
        "Project Engineer | Contract Administrator",
        size=11, space_after=2,
    )
    add_para(doc, "ADASA — Aguas de Antofagasta S.A.", size=11, space_after=2)
    add_para(
        doc,
        "Contract C-4300 | Project 12803 — Taltal SWRO",
        size=11, space_after=0,
    )

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    main()
