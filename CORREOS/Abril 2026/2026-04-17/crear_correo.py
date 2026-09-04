"""
Correo: Seventh Communication Without Response - Request for Executive Meeting
Fecha: 17-Apr-2026
Codigo: CORREO-2026-04-17-SEVENTH-REMINDER-EXEC-MEETING
Version: 1
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-04-17_Seventh-Reminder-Executive-Meeting.docx")


def set_font(run, name="Arial", size=11, bold=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_para(doc, text="", bold=False, size=11, space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if text:
        run = p.add_run(text)
        set_font(run, bold=bold, size=size)
    return p


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


def add_bullet(doc, text, size=11, bold=False, indent_cm=1.27):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(indent_cm)
    p.paragraph_format.first_line_indent = Cm(-0.4)
    r = p.add_run("\u2013  " + text)
    set_font(r, size=size, bold=bold)
    return p


def add_lettered_item(doc, letter, text, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.6)
    r = p.add_run(f"{letter})  ")
    set_font(r, size=size, bold=True)
    r2 = p.add_run(text)
    set_font(r2, size=size)
    return p


def main():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.0)

    # --- HEADER ---
    add_para(doc, "ADASA \u2014 Aguas de Antofagasta S.A.", bold=True, size=12, space_after=2)
    add_para(doc, "Contract C-4300 | Project 12803 \u2014 Taltal SWRO", size=10, space_after=8)

    # --- SUBJECT / FROM / TO / DATE ---
    subj = add_para(doc, space_before=0, space_after=4)
    r = subj.add_run("Subject: ")
    set_font(r, bold=True, size=11)
    r2 = subj.add_run(
        "Project 12803 \u2014 Taltal SWRO | "
        "Seventh Communication Without Response \u2014 Request for Executive Meeting"
    )
    set_font(r2, size=11)

    for label, value in [
        ("Date: ", "April 17, 2026"),
        (
            "To: ",
            "Andrew J. Zaske \u2014 Vice President-Americas, BW Water Americas Inc.; "
            "Eduardo Yamauchi \u2014 BW Water Americas Inc.; "
            "Victor Gutierrez \u2014 ADASA",
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
    add_para(doc, "Andrew, Eduardo, Victor,", size=11, space_after=10)

    # --- OPENING ---
    p = add_para(doc, space_before=0, space_after=10)
    parts = [
        ("This is the ", False),
        ("seventh", True),
        (" communication from ADASA on the same set of outstanding items, and the ", False),
        ("seventh without a reply", True),
        (
            ". Our previous messages of April\u00a01, 6, 10, 13, 14 and 15 have "
            "all gone unanswered \u2014 no acknowledgment, no holding response, "
            "no partial feedback. A sustained silence of 17 calendar days on "
            "engineering and procurement matters that are actively blocking "
            "project progress is no longer an operational issue; it is an "
            "executive one.",
            False,
        ),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        set_font(r, size=11, bold=bold)

    # --- PROCUREMENT SECTION (central concern) ---
    add_para(
        doc,
        "Procurement status \u2014 our central concern, unanswered since April 6",
        bold=True, size=11, space_before=4, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=6)
    r = p.add_run(
        "Our repeated request has been simple: an updated Procurement Log, "
        "reconciled against the Baseline Schedule 05-Mar-2026, showing current "
        "PO status for each of the 16 equipment lines. Twelve days later we "
        "still have no visibility on:"
    )
    set_font(r, size=11)

    add_bullet(doc, "Which purchase orders have been placed, when, and with which supplier.", size=11)
    add_bullet(doc, "Which PO windows remain open and which have closed without commitment.", size=11)
    add_bullet(doc, "What equipment lead times BW Water is currently holding against the Baseline.", size=11)
    add_bullet(doc, "Which lines are already deviating from the committed procurement dates.", size=11)

    p = add_para(doc, space_before=6, space_after=10)
    parts = [
        (
            "The Structural Frames\u00a0/\u00a0Supports window closed on April\u00a010 ",
            False,
        ),
        ("without a confirmed purchase order", True),
        (
            " \u2014 a concrete example of the consequence of operating without "
            "this feedback loop. Without periodic PO status updates, ADASA "
            "cannot verify that critical-path equipment will arrive in time "
            "to support module fabrication.",
            False,
        ),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        set_font(r, size=11, bold=bold)

    # --- OUTSTANDING ENGINEERING ITEMS ---
    add_para(
        doc,
        "Outstanding engineering items (detail in our April 15 communication)",
        bold=True, size=11, space_before=4, space_after=6,
    )

    add_bullet(doc, "Six layout submittals \u2014 16 calendar days overdue.", size=11)
    add_bullet(
        doc,
        "Operating Weight table \u2014 removed from the Equipment Layout "
        "Rev\u00a0C advance copy; restoration pending.",
        size=11,
    )

    # --- RISK SECTION ---
    add_para(
        doc,
        "Risk to the August 2026 milestone",
        bold=True, size=11, space_before=10, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=10)
    parts = [
        ("The Baseline Schedule 05-Mar-2026 (document ", False),
        ("05.03.26_12803_Taltal Water Treatment Plant", False),
        (") commits Factory Acceptance Test between ", False),
        ("July\u00a025 and August\u00a01, 2026", True),
        (", and Ready to Ship to Project Site on ", False),
        ("August\u00a03, 2026", True),
        (
            ". Engineering deliverables are 16 days overdue, procurement "
            "visibility is absent, and PO windows are closing without "
            "confirmation. ADASA requires executive-level assurance from "
            "BW Water that this milestone remains achievable, supported by "
            "evidence \u2014 not a further commitment without follow-through.",
            False,
        ),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        if text == "05.03.26_12803_Taltal Water Treatment Plant":
            r.italic = True
        set_font(r, size=11, bold=bold)

    # --- REQUEST ---
    add_para(
        doc,
        "Request",
        bold=True, size=11, space_before=4, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=6)
    r = p.add_run(
        "We request a 60-minute meeting during the week of April\u00a020,\u00a02026, "
        "restricted to the four addressees of this communication. Proposed agenda:"
    )
    set_font(r, size=11)

    # Agenda item (a) — bold lead
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.6)
    r = p.add_run("a)  ")
    set_font(r, size=11, bold=True)
    r2 = p.add_run("Procurement status walkthrough")
    set_font(r2, size=11, bold=True)
    r3 = p.add_run(
        " \u2014 line-by-line review of the 16 equipment lines against the "
        "Baseline Schedule, with PO dates, suppliers and current status."
    )
    set_font(r3, size=11)

    add_lettered_item(
        doc, "b",
        "Executive status of the six outstanding layouts and the Operating Weight data."
    )
    add_lettered_item(
        doc, "c",
        "Recovery plan to preserve FAT (July\u00a025\u00a0\u2013\u00a0August\u00a01) "
        "and Ready to Ship (August\u00a03)."
    )
    add_lettered_item(
        doc, "d",
        "Standing communication protocol \u2014 weekly PO status reporting and "
        "a standing escalation channel between BW Water and ADASA leadership."
    )

    p = add_para(doc, space_before=8, space_after=10)
    parts = [
        ("Kindly propose two or three time windows by end of business ", False),
        ("Monday, April\u00a020, 2026", True),
        (
            ", and include with your reply, at minimum, a ",
            False,
        ),
        ("preliminary PO status snapshot", True),
        (
            " so that the meeting can be productive from the first minute. "
            "The formal delay notification announced in our April\u00a015 "
            "communication remains on hold pending confirmation of this "
            "meeting and receipt of the procurement information.",
            False,
        ),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        set_font(r, size=11, bold=bold)

    # --- CLOSING ---
    add_para(doc, "Best regards,", size=11, space_before=10, space_after=12)

    sig_lines = [
        ("Luis Rivera", True),
        ("Project Engineer | Contract Administrator", False),
        ("ADASA \u2014 Aguas de Antofagasta S.A.", False),
        ("Contract C-4300 | Project 12803 \u2014 Taltal SWRO", False),
    ]
    for text, bold in sig_lines:
        add_para(doc, text, bold=bold, size=10, space_before=0, space_after=1)

    doc.save(OUTPUT)
    print(f"Correo generado: {OUTPUT}")


if __name__ == "__main__":
    main()
