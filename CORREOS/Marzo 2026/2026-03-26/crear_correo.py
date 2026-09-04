"""
Correo: Respuesta a Procurement Log BW Waters y Seguimiento Propuesta Layout
Fecha: 26-Mar-2026
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "2026-03-26_Respuesta-Procurement-Layout-Proposal.docx")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def set_font(run, name="Arial", size=10, bold=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)

def add_para(doc, text="", size=10, bold=False, space_after=4, color=None,
             align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    if text:
        run = p.add_run(text)
        set_font(run, size=size, bold=bold, color=color)
    return p

def add_header_line(doc, label, value, size=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run(label)
    set_font(r1, size=size, bold=True)
    r2 = p.add_run(value)
    set_font(r2, size=size)
    return p

def add_section_title(doc, text, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    set_font(run, size=size, bold=True)
    run.font.underline = True
    return p

def add_shading(cell, fill_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_hex)
    tcPr.append(shd)

def build_table(doc, headers, rows, col_widths_cm, highlight_col=None, highlight_color=(255, 230, 153)):
    """Build a styled table. highlight_col=index of column to apply conditional highlighting."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    # Header row
    hdr = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.width = Cm(col_widths_cm[i])
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font(run, size=9, bold=True, color=(31, 56, 100))
        add_shading(cell, "D9E1F2")
    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = Cm(col_widths_cm[c_idx])
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            # Highlight última columna si contiene urgencia
            urgent = (c_idx == len(headers) - 1 and
                      any(kw in cell_text.lower() for kw in
                          ["passed", "immediately", "closes march 31", "required immediately"]))
            run = p.add_run(cell_text)
            if urgent:
                set_font(run, size=9, bold=True, color=(192, 0, 0))
            else:
                set_font(run, size=9)
    doc.add_paragraph()  # espacio post-tabla

def add_numbered_item(doc, prefix, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.8)
    r1 = p.add_run(prefix + "  ")
    set_font(r1, bold=True)
    r2 = p.add_run(text)
    set_font(r2)

# ---------------------------------------------------------------------------
# Documento
# ---------------------------------------------------------------------------
doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

style = doc.styles["Normal"]
style.font.name = "Arial"
style.font.size = Pt(10)

# ---------------------------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------------------------
add_para(doc, "CORREO ELECTR\u00d3NICO", size=12, bold=True,
         color=(31, 56, 100), align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

add_header_line(doc, "Fecha:   ", "26 de Marzo de 2026")
add_header_line(doc, "De:      ", "Luis Rivera \u2014 Contract Administrator (ADASA)")
add_header_line(doc, "Para:    ", "Eduardo Yamauchi \u2014 BW Water Americas Inc.")
add_header_line(doc, "CC:      ",
    "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, "
    "Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, "
    "Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, "
    "Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim")
add_header_line(doc, "Asunto:  ",
    "Project 12803 \u2014 Taltal SWRO | Re: Procurement Status & Proposal 25007-PL-0001 "
    "| March 26, 2026")

doc.add_paragraph()

# ---------------------------------------------------------------------------
# SALUDO + ACKNOWLEDGMENT
# ---------------------------------------------------------------------------
add_para(doc, "Dear Eduardo,", bold=True, space_after=6)
add_para(doc,
    "Thank you for your response of March\u00a026, 2026. We acknowledge the following "
    "purchase orders:",
    space_after=8)

build_table(doc,
    headers=["Equipment", "PO Reference", "Status"],
    col_widths_cm=[6.5, 5.0, 7.0],
    rows=[
        ("CIP Tank Heater", "BW-PO-2026M062", "Confirmed"),
        ("Container (40\u2019)", "Malaysia workshop", "In production"),
        ("CIP / Flushing Tank", "BW-PO-2026M073", "Confirmed"),
        ("Antiscalant Dosing Pump", "BW-PO-2026M089", "Confirmed"),
    ]
)

add_para(doc,
    "We note four items that require BW Water\u2019s immediate attention.",
    space_after=4)

# ---------------------------------------------------------------------------
# SECCIÓN 1 — Code 2 Policy
# ---------------------------------------------------------------------------
add_section_title(doc, "1. Code 2 \u2014 \u201cApproved as Noted\u201d: Procurement Clarification")

add_para(doc,
    "BW Water\u2019s response indicates that POs for Code\u00a02 items are on hold pending Code\u00a01. "
    "This is not consistent with the project\u2019s review code system.",
    space_after=6)

add_para(doc, "Under the applicable review codes:", space_after=3)
for line in [
    "Code 1 \u2014 Approved: PO may proceed.",
    "Code 2 \u2014 Approved as Noted: PO may proceed. Observations are minor and will be "
    "incorporated in the next document revision.",
    "Code 3 \u2014 To Be Revised: PO on hold. Revision required before procurement.",
]:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.8)
    run = p.add_run(line)
    set_font(run, size=10)

add_para(doc,
    "Code\u00a02 does not constitute a procurement hold. The following items are affected:",
    space_after=6)

build_table(doc,
    headers=["Equipment", "PO Window", "Review Code", "Required Action"],
    col_widths_cm=[4.8, 2.8, 3.2, 7.7],
    rows=[
        ("CIP / Flushing Cartridge Filter", "23\u201327 Mar",
         "Code 2 (TM\u00a0N11)",
         "Window has passed \u2014 PO required immediately"),
        ("CIP / Flushing Pumps", "25\u201331 Mar",
         "Code 2 (TM\u00a0N11)",
         "Window closes March 31"),
        ("Feed Turbocharger\n(SIP-09-001)", "1\u20137 Apr",
         "Code 2 (TM\u00a0N11)",
         "Window opens April 1"),
    ]
)

add_para(doc,
    "Please confirm that BW Water will issue POs for the above items without further delay. "
    "For the CIP/Flushing Cartridge Filter, ADASA requires confirmation by EOB "
    "March\u00a027, 2026 given the expired procurement window.",
    space_after=4)

# ---------------------------------------------------------------------------
# SECCIÓN 2 — RO Pressure Vessel
# ---------------------------------------------------------------------------
add_section_title(doc, "2. RO Pressure Vessel / Tubes \u2014 Open Question")

add_para(doc,
    "BW Water\u2019s response (\u201cOn going for the PO\u201d) does not address ADASA\u2019s question "
    "from March\u00a023: whether the vessel housing is covered by the existing UHPRO "
    "purchase order or requires a separate procurement action. Please provide a "
    "clear answer on this point.",
    space_after=4)

# ---------------------------------------------------------------------------
# SECCIÓN 3 — Structural Frames
# ---------------------------------------------------------------------------
add_section_title(doc, "3. Structural Frames / Supports \u2014 Commitment Required")

add_para(doc,
    "The procurement window for Structural Frames / Supports opens April\u00a06, 2026 \u2014 "
    "eleven days from today. No datasheet has been submitted. \u201cTBC\u201d does not "
    "constitute a scheduled commitment.",
    space_after=8)

add_para(doc, "ADASA requires, by March\u00a031, 2026:", space_after=4)
add_numbered_item(doc, "a)", "Confirmed date for datasheet submission; and")
add_numbered_item(doc, "b)", "Confirmed date for PO issuance.")

add_para(doc,
    "Failure to submit the datasheet before the window opens will result in a schedule "
    "impact attributable to BW Water.",
    space_after=4)

# ---------------------------------------------------------------------------
# SECCIÓN 4 — Layout Proposal (no respondida)
# ---------------------------------------------------------------------------
add_section_title(doc, "4. Proposal 25007-PL-0001 Rev.2 \u2014 Unanswered Section")

add_para(doc,
    "ADASA\u2019s March\u00a023 email included a Section\u00a04 requesting three items from "
    "BW Water by EOB March\u00a025, 2026. That section was not addressed in "
    "BW Water\u2019s March\u00a026 response.",
    space_after=6)

add_para(doc, "For the record:", bold=True, space_after=3)
for line in [
    "Deadline communicated: EOB March 25, 2026.",
    "Response received: March 26, 2026 \u2014 procurement tables only.",
    "Section 4 items: unanswered.",
]:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.8)
    run = p.add_run(line)
    set_font(run, size=10)

add_para(doc, "ADASA restates its requirements:", space_after=4)

add_numbered_item(doc, "a)",
    "Confirmed delivery date for Piping Layout Rev\u00a0B and 3D Model (Phase\u00a01);")
add_numbered_item(doc, "b)",
    "Expected delivery date for Instrument Layout Rev\u00a0B and Grounding Layout "
    "Rev\u00a0B (Phase\u00a02); and")
add_numbered_item(doc, "c)",
    "BW Water\u2019s commercial close confirmation for both phases.")

add_para(doc,
    "Please provide this information by EOB March\u00a027, 2026. If ADASA does not receive "
    "a response by that date, it will proceed to close the proposal on Phase\u00a01 "
    "documents only, and its position on Phase\u00a02 will remain open pending delivery "
    "of Piping Layout Rev\u00a0B.",
    space_after=4)

# ---------------------------------------------------------------------------
# CIERRE
# ---------------------------------------------------------------------------
add_para(doc, "Please confirm receipt of this message.", space_after=10)
add_para(doc, "Best regards,", space_after=4)
add_para(doc, "Luis Rivera", bold=True, space_after=2)
add_para(doc, "Project Engineer | Contract Administrator", space_after=2)
add_para(doc, "ADASA \u2014 Aguas de Antofagasta S.A.", space_after=2)
add_para(doc, "Contract C-4300 | Project 12803 \u2014 Taltal SWRO", space_after=0)

# ---------------------------------------------------------------------------
# GUARDAR
# ---------------------------------------------------------------------------
doc.save(OUTPUT)
print(f"Generado: {OUTPUT}")
