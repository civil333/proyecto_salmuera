"""
Correo: RE: URGENT — Layout Submittals & Operating Weight Data Required
Fecha: 14-Apr-2026
Codigo: CORREO-2026-04-14-FOLLOWUP-LAYOUTS-WEIGHT
Version: 1
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-04-14_Follow-Up-Layouts-Weight-Table.docx")


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

    # --- SUBJECT / FROM / TO / CC / DATE ---
    subj = add_para(doc, space_before=0, space_after=4)
    r = subj.add_run("Subject: ")
    set_font(r, bold=True, size=11)
    r2 = subj.add_run(
        "RE: URGENT: Project 12803 \u2014 Taltal SWRO | "
        "Layout Submittals & Operating Weight Data Required"
    )
    set_font(r2, size=11)

    for label, value in [
        ("Date: ", "April 14, 2026"),
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
    add_para(doc, "Dear Eduardo,", size=11, space_after=10)

    # --- OPENING ---
    p = add_para(doc, space_before=0, space_after=10)
    r = p.add_run(
        "This is our fifth communication regarding the outstanding layout "
        "revisions and procurement log, following our emails of April\u00a01, "
        "April\u00a06, April\u00a010 and April\u00a013. We have not received "
        "a response to any of these communications."
    )
    set_font(r, size=11)

    # --- OPERATING WEIGHT SECTION ---
    add_para(
        doc,
        "Operating Weight Data Missing from Equipment Layout Rev\u00a0C",
        bold=True, size=11, space_before=4, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=8)
    parts = [
        (
            "While reviewing the advance copies received on April\u00a02, we "
            "noted that the Equipment Layout Rev\u00a0C ",
            False,
        ),
        ("no longer includes the Operating Weight table", True),
        (
            ". Rev\u00a0A contained a detailed breakdown of seven equipment "
            "items with a total operating weight of 34,739\u00a0lb "
            "(15,758\u00a0kg). This information has been removed from the "
            "Rev\u00a0C drawing without replacement.",
            False,
        ),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        set_font(r, bold=bold, size=11)

    p = add_para(doc, space_before=0, space_after=6)
    r = p.add_run(
        "ADASA requires updated operating weights \u2014 including the CIP "
        "Heater (REL-09-001) and any equipment added or modified since "
        "Rev\u00a0A \u2014 for three concurrent engineering activities:"
    )
    set_font(r, size=11)

    weight_items = [
        "Foundation and civil works design, currently in progress.",
        "Seismic verification per NCh\u00a02369, Zone\u00a03, as required "
        "by the Technical Specification.",
        "Module lifting plan, a contractual deliverable per the Technical "
        "Specification \u2014 Engineering Documentation.",
    ]
    for item in weight_items:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(1.0)
        r = p.add_run("\u2013 " + item)
        set_font(r, size=11)

    p = add_para(doc, space_before=6, space_after=10)
    r = p.add_run(
        "We request that the formal Equipment Layout Rev\u00a0C submittal "
        "restore the Operating Weight table with current values for all "
        "equipment inside and outside the container."
    )
    set_font(r, size=11)

    # --- PENDING ITEMS ---
    add_para(
        doc,
        "Pending Items \u2014 No Change from April\u00a013",
        bold=True, size=11, space_before=4, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=6)
    r = p.add_run(
        "The two items requested on April\u00a013 remain outstanding:"
    )
    set_font(r, size=11)

    pending = [
        (
            "a) ",
            "Confirmed delivery date for the six layout documents "
            "(PDF\u00a0+\u00a0DWG, plus STEP/IGES for the 3D model).",
        ),
        (
            "b) ",
            "Updated Procurement Log against Baseline Schedule "
            "05-Mar-2026, covering all 16 lines with current PO status.",
        ),
    ]
    for label, body in pending:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(1.0)
        r_label = p.add_run(label)
        set_font(r_label, bold=True, size=11)
        r_body = p.add_run(body)
        set_font(r_body, size=11)

    p = add_para(doc, space_before=6, space_after=10)
    r = p.add_run(
        "The advance copies received on April\u00a02 are appreciated as "
        "working drafts but do not replace a formal submittal through the "
        "established review process."
    )
    set_font(r, size=11)

    # --- DEADLINE ---
    add_para(
        doc, "Deadline", bold=True, size=11, space_before=4, space_after=6,
    )

    p = add_para(doc, space_before=0, space_after=16)
    parts_dl = [
        (
            "ADASA requests a written response by ",
            False,
        ),
        ("end of business April\u00a015, 2026", True),
        (
            ". In the absence of a response, we will proceed with the "
            "formal delay notification process communicated on April\u00a013.",
            False,
        ),
    ]
    for text, bold in parts_dl:
        r = p.add_run(text)
        set_font(r, bold=bold, size=11)

    # --- SIGNATURE ---
    add_para(doc, "Best regards,", size=11, space_after=8)
    add_para(doc, "Luis Rivera", bold=True, size=11, space_after=2)
    add_para(doc, "Project Engineer | Contract Administrator", size=11, space_after=2)
    add_para(doc, "ADASA \u2014 Aguas de Antofagasta S.A.", size=11, space_after=2)
    add_para(doc, "Contract C-4300 | Project 12803 \u2014 Taltal SWRO", size=11, space_after=0)

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    main()
