"""
Correo: ADASA Response to BW Water Meeting Minute of 20-Apr-2026
Fecha: 20-Apr-2026
Codigo: CORREO-2026-04-20-RESPONSE-BWW-MEETING-MINUTE
Version: 4 (ejecutiva, §3 solo cita ETE sin interpretacion)
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-04-20_Response-BWW-Meeting-Minute.docx")


def set_font(run, name="Arial", size=11, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_para(doc, text="", bold=False, italic=False, size=11, space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if text:
        run = p.add_run(text)
        set_font(run, bold=bold, italic=italic, size=size)
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


def add_numbered_para(doc, number_text, body_parts):
    """
    Parrafo con numero bold al inicio (p.ej. "1. Valve procurement.") seguido
    de cuerpo con runs bold/regular. body_parts = [(text, bold), ...].
    """
    p = add_para(doc, space_before=0, space_after=10)
    # numero y titulo en bold
    r = p.add_run(number_text + " ")
    set_font(r, size=11, bold=True)
    for text, bold in body_parts:
        r = p.add_run(text)
        set_font(r, size=11, bold=bold)


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

    # --- SUBJECT / TO / CC / FROM / DATE ---
    subj = add_para(doc, space_before=0, space_after=4)
    r = subj.add_run("Subject: ")
    set_font(r, bold=True, size=11)
    r2 = subj.add_run(
        "Project 12803 \u2014 Taltal SWRO | "
        "ADASA Response to BW Water Meeting Minute of 20-Apr-2026"
    )
    set_font(r2, size=11)

    for label, value in [
        ("Date: ", "April 20, 2026"),
        ("To: ", "Eduardo Yamauchi \u2014 BW Water Americas Inc."),
        ("CC: ",
         "Adzlan Bin Abd Rahim; Jeryl F. Regulacion; Sadeep Irugalbandara; "
         "Nick Huta; Shane Banks; Muhammad Farih Awang; Fadey Kassim; "
         "Andrew J. Zaske; Victor Gutierrez"),
        ("From: ", "Luis Rivera \u2014 Contract Administrator (ADASA)"),
    ]:
        p = add_para(doc, space_before=0, space_after=2)
        r = p.add_run(label)
        set_font(r, bold=True, size=11)
        r2 = p.add_run(value)
        set_font(r2, size=11)

    add_separator(doc)

    # --- SALUTATION ---
    add_para(doc, "Eduardo,", size=11, space_after=10)

    # --- OPENING (1 oracion) ---
    p = add_para(doc, space_before=0, space_after=10)
    r = p.add_run(
        "Thank you for today's meeting minute. Three points need a formal ADASA "
        "position before BW Water advances on the outstanding decisions."
    )
    set_font(r, size=11)

    # --- §1 VALVE PROCUREMENT ---
    add_numbered_para(doc, "1. Valve procurement.", [
        ("No restriction on supplier nationality exists in the BAE or in the "
         "ET \u2014 Chinese, European or any international origin is acceptable. "
         "Compliance is measured against the ET Piping and Valves specification: "
         "body material ", False),
        ("ASTM A182 F53 (UNS S32750, PREN > 40)", True),
        (", ", False),
        ("ANSI/ASME B16.5 Class 900", True),
        (" for the high-pressure circuit, ", False),
        ("PMI on 10% of Super Duplex components", True),
        (", ", False),
        ("NDE per ASME B31.3", True),
        (", and ADASA witness point at factory. Practical note: the Valve List "
         "Rev D of 18 March 2026 lists every brand, make and model as ", False),
        ("TBA", True),
        (" \u2014 no supplier is formally declared yet. Once BW Water identifies "
         "the supplier, submit the manufacturer's datasheet, material "
         "certificates and inspection plan, and ADASA will evaluate within the "
         "standard contractual review.", False),
    ])

    # --- §2 OPERATING WEIGHTS ---
    add_numbered_para(doc, "2. Operating Weights.", [
        ("The table removed from the Equipment Layout Rev C advance copy (", False),
        ("seven items, 34,739 lb / 15,758 kg", True),
        (" in Rev A) must be restored in the next formal submittal. It is "
         "required for foundation design, ", False),
        ("NCh 2369 Zone 3", True),
        (" seismic verification and the module lifting plan. Deliver together "
         "with the Piping Layout final committed in your minute for the next "
         "24 hours.", False),
    ])

    # --- §3 CONTAINER DOORS ---
    add_numbered_para(doc, "3. Container doors.", [
        ("The ET Container section requires four door provisions: a personnel "
         "door of ", False),
        ("900 \u00d7 2,200 mm", True),
        (", an equipment door sized to the largest installed equipment "
         "(110\u00b0 opening, outward-swinging), an emergency door, and a ", False),
        ("lateral sliding door", True),
        (". Please confirm each of the four provisions in the Equipment Layout "
         "formal submittal, with dimensions per ET.", False),
    ])

    # --- CLOSING (1 parrafo breve) ---
    p = add_para(doc, space_before=0, space_after=12)
    parts = [
        ("This note complements the Weekly Procurement Reporting Protocol sent "
         "earlier today. Any difference of interpretation, please flag it by "
         "return email before the first weekly tracker on ", False),
        ("Monday, 27 April 2026", True),
        (".", False),
    ]
    for text, bold in parts:
        r = p.add_run(text)
        set_font(r, size=11, bold=bold)

    add_para(doc, "Best regards,", size=11, space_before=6, space_after=12)

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
