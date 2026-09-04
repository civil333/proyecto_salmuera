"""
Correo: RE: Outstanding Commitments — Layout Revisions & Procurement Log
Fecha: 10-Apr-2026
Codigo: CORREO-2026-04-10-RE-OUTSTANDING-COMMITMENTS
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-04-10_RE-Outstanding-Commitments.docx")


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
    add_para(doc, "ADASA \u2014 Aguas de Antofagasta S.A.", bold=True, size=12, space_after=2)
    add_para(doc, "Contract C-4300 | Project 12803 \u2014 Taltal SWRO", size=10, space_after=8)

    # --- SUBJECT BLOCK ---
    subj = add_para(doc, space_before=0, space_after=4)
    r = subj.add_run("Subject: ")
    set_font(r, bold=True, size=11)
    r2 = subj.add_run(
        "RE: Project 12803 \u2014 Taltal SWRO | Outstanding Commitments \u2014 "
        "Layout Revisions & Procurement Log | April 6, 2026"
    )
    set_font(r2, size=11)

    for label, value in [
        ("Date: ", "April 10, 2026"),
        ("To: ", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        (
            "CC: ",
            "Jeryl F. Regulacion, Adzlan Bin Abd Rahim, Sadeep Irugalbandara, Nick Huta; "
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes",
        ),
        ("From: ", "Luis Rivera \u2014 Contract Administrator (ADASA)"),
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
        "This is a follow-up to our email of April 6, 2026, for which no response "
        "has been received.",
        size=11,
        space_after=12,
    )

    # =================================================================
    # SECTION 1 — APRIL 9 MEETING COMMITMENTS
    # =================================================================
    add_para(
        doc,
        "1. April 9 Meeting \u2014 New Commitments Not Met",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "During our meeting on April 9, BW Water confirmed two deliverables:",
        size=11, space_after=8,
    )

    add_table(
        doc,
        headers=["Commitment", "Agreed Deadline", "Status (April 10)"],
        rows=[
            [
                "Procurement Log (updated against Baseline Schedule 05-Mar-2026)",
                "April 9, 2026",
                "Not received",
            ],
            [
                "Layout revisions (6 documents per April 6 email, items 1\u20136)",
                "April 10, 2026",
                "Not received as of this writing",
            ],
        ],
        col_widths=[6.5, 3.5, 5.0],
    )
    add_para(doc, space_after=6)

    add_para(
        doc,
        "The Procurement Log is now one day past the April 9 commitment. "
        "This is the second commitment for this deliverable \u2014 the first was agreed "
        "during the April 2 meeting and remains unfulfilled.",
        size=11, space_after=12,
    )

    # =================================================================
    # SECTION 2 — LAYOUT COMMITMENT TIMELINE
    # =================================================================
    add_para(
        doc,
        "2. Layout Revisions \u2014 Fourth Consecutive Missed Deadline",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "The layout revisions have been subject to four successive commitments, "
        "none of which has been met:",
        size=11, space_after=8,
    )

    add_table(
        doc,
        headers=["Commitment Source", "Agreed Deadline", "Days Since Deadline"],
        rows=[
            ["Meeting \u2014 March 31, 2026", "April 1", "9"],
            ["ADASA email \u2014 April 1, 2026", "April 3", "7"],
            ["ADASA email \u2014 April 6, 2026", "April 7", "3"],
            ["Meeting \u2014 April 9, 2026", "April 10", "Due today"],
        ],
        col_widths=[6.0, 3.5, 3.5],
    )
    add_para(doc, space_after=6)

    add_para(
        doc,
        "ADASA has not received the formal submittals for items 1\u20134, "
        "nor first delivery of items 5\u20136 (Instrument Layout and Grounding Point "
        "& Power Panel Layout), as detailed in our April 6 communication.",
        size=11, space_after=12,
    )

    # =================================================================
    # SECTION 3 — PROCUREMENT UPDATE
    # =================================================================
    add_para(
        doc,
        "3. Procurement Status \u2014 Update Since April 6",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "Since our April 6 email, three additional PO windows have closed without "
        "confirmation from BW Water. The table below reflects the current position "
        "as of today, April 10:",
        size=11, space_after=10,
    )

    add_para(
        doc,
        "PO Windows Now Closed \u2014 No Confirmation Received (8 items):",
        bold=True, size=10, space_after=6,
    )
    add_table(
        doc,
        headers=["Equipment", "PR/PO Window", "Window Closed", "Days Overdue", "Eng. Status"],
        rows=[
            ["RO High Feed Pump", "Mar 4 \u2013 10", "Mar 10", "31",
             "Code 2 \u2014 PO enabled since TM N6"],
            ["Instrument Set", "Mar 11 \u2013 17", "Mar 17", "24",
             "Code 3 \u2014 IO List Rev C not received"],
            ["All Valve Set", "Mar 11 \u2013 17", "Mar 17", "24",
             "Code 3 \u2014 Valve List Rev D not received"],
            ["CIP/Flush. Cartridge Filter", "Mar 23 \u2013 27", "Mar 27", "14",
             "Code 2 \u2014 PO enabled"],
            ["CIP / Flushing Pumps", "Mar 25 \u2013 31", "Mar 31", "10",
             "Code 2 \u2014 PO enabled"],
            ["RO Pressure Vessel / Tubes", "Mar 31 \u2013 Apr 6", "Apr 6", "4",
             "Code 1 \u2014 PO enabled"],
            ["Feed Turbocharger (SIP-09-001)", "Apr 1 \u2013 7", "Apr 7", "3",
             "Code 2 \u2014 PO enabled"],
            ["Structural Frames / Supports", "Apr 6 \u2013 10", "Today", "0",
             "No datasheet. Layouts pending"],
        ],
        col_widths=[3.8, 2.3, 1.8, 1.5, 5.5],
        font_size=9,
    )
    add_para(doc, space_after=8)

    add_para(
        doc,
        "The Structural Frames / Supports line is the most time-critical item: "
        "manufacturing runs only through May 5, 2026, leaving 25 calendar days "
        "from today with no margin for procurement delays. Without the layout "
        "revisions requested in our April 6 email, the structural frame geometry "
        "cannot be defined and the purchase order cannot proceed.",
        size=11, space_after=8,
    )

    add_para(
        doc,
        "Of the 16 procurement lines in the Baseline Schedule, only four have confirmed "
        "POs (25%). Eight PO windows are now closed without confirmation \u2014 "
        "up from five on April 6.",
        size=11, space_after=14,
    )

    # =================================================================
    # SECTION 4 — ACTION REQUIRED
    # =================================================================
    add_para(
        doc,
        "4. Action Required \u2014 Immediate",
        bold=True, size=11, space_after=6,
    )
    add_para(
        doc,
        "Given that the April 7 deadline from our previous email and the April 9 "
        "meeting commitments have both passed, ADASA requires the following by return:",
        size=11, space_after=6,
    )

    items = [
        "a) Formal submittals for the six layout documents detailed in our April 6 "
        "email (items 1\u20136), in PDF + DWG (plus STEP/IGES for the 3D model).",
        "b) The updated Procurement Log against the Baseline Schedule 05-Mar-2026, "
        "covering all 16 procurement lines with current PO status and confirmed "
        "or expected PO dates.",
        "c) Written confirmation of receipt and revised delivery dates for all "
        "outstanding items.",
    ]
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(1.0)
        run = p.add_run(item)
        set_font(run, size=11)

    add_para(doc, space_before=10, space_after=16)

    # --- SIGNATURE ---
    add_para(doc, "Best regards,", size=11, space_after=8)
    add_para(doc, "Luis Rivera", bold=True, size=11, space_after=2)
    add_para(
        doc,
        "Project Engineer | Contract Administrator",
        size=11, space_after=2,
    )
    add_para(doc, "ADASA \u2014 Aguas de Antofagasta S.A.", size=11, space_after=2)
    add_para(
        doc,
        "Contract C-4300 | Project 12803 \u2014 Taltal SWRO",
        size=11, space_after=0,
    )

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    main()
