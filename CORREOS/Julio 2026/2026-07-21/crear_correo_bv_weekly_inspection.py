#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo conjunto ADASA -> Bureau Veritas (inspector tercero), copiando a BW Water:
plan de inspeccion de taller (Penang) presentado POR SEMANAS (no por dias).

- To: Luis Rodrigo Arcila Quezada (Bureau Veritas Chile). CC: contactos QAQC de
  Penang que BW Water designo (Mohd Adnin Zulkifli, Lokman Hakim Mat) + Magdier
  Arias / Eduardo Yamauchi / Stephane Gehant (BW Water) + Victor Gutierrez /
  Jorge Guevara / Ronald Pellejero (ADASA).
- Correo NUEVO (asunto propio), no reply al hilo de BW Water. Ingles.
- Hitos por SEMANA: 6 semanas de vigilancia (3 visitas c/u = 18 QAQC) + semana
  de FAT (7 jornadas). Alcance semanal per NT-002 Section 3.2; ventanas ancladas
  al programa fijo del 14-Jul (sin cambios al Week 29, 20-Jul).
- Document() directo, sin template ADASA (CLAUDE.md 3.4). Sin em-dash; sin
  simbolo de seccion; sin IDs internos; sin jornadas/costos de la oferta BV
  (solo la referencia 600049). Metadatos limpios. Estado: BORRADOR.
"""

import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-21_BV-Weekly-Inspection-Plan.docx"
)
CONTACTO = "Luis Rivera González"
LANG = "en-US"
DOWNLOAD_LINK = ("https://lrg.synology.me:6501/d/s/18xc6ezTnrRYrdGebvNUYAYku3fZkKrM/"
                 "mnJb6gJOkpddZgZ2vb2BZd870AMiJ0oo-mLwg5C36XQ0")


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_hyperlink(paragraph, url, text):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), r_id)
    run = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts"); rf.set(qn("w:ascii"), "Arial"); rf.set(qn("w:hAnsi"), "Arial")
    rpr.append(rf)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t"); t.text = text; run.append(t)
    h.append(run); paragraph._p.append(h)


def _set_lang_in_rPr(rPr, lang):
    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = OxmlElement("w:lang")
        rPr.append(lang_el)
    lang_el.set(qn("w:val"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    try:
        rPr = doc.styles["Normal"].element.get_or_add_rPr()
        _set_lang_in_rPr(rPr, lang)
    except KeyError:
        pass
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            _set_lang_in_rPr(run._element.get_or_add_rPr(), lang)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        _set_lang_in_rPr(run._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11):
    para = doc.add_paragraph(text)
    aplicar_arial(para, size)
    return para


def blank(doc):
    doc.add_paragraph()


def add_numbered(doc, number, lead, rest, size=11):
    """Item numerado manual: 'N. ' + lead en negrita + resto normal."""
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    para.paragraph_format.space_after = Pt(6)
    r0 = para.add_run(f"{number}. ")
    r0.font.name = "Arial"
    r0.font.size = Pt(size)
    r1 = para.add_run(lead)
    r1.bold = True
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    r2 = para.add_run(" " + rest)
    r2.font.name = "Arial"
    r2.font.size = Pt(size)
    return para


def aplicar_arial_table(table, size=10):
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)


def add_table_with_header(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = header
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True

    for i, row_data in enumerate(rows, start=1):
        for j, value in enumerate(row_data):
            table.rows[i].cells[j].text = str(value)

    if widths:
        for j, w in enumerate(widths):
            for row in table.rows:
                row.cells[j].width = w

    aplicar_arial_table(table, size=10)
    return table


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ---- HEADER -------------------------------------------------------------
    fields = [
        ("Date:", "July 21, 2026"),
        ("From:",
         f"{CONTACTO} - Infrastructure Engineering Lead (ADASA)"),
        ("To:",
         "Luis Rodrigo Arcila Quezada - Bureau Veritas Chile"),
        ("CC:",
         "Mohd Adnin Zulkifli, Lokman Hakim Mat, Magdier Arias, "
         "Eduardo Yamauchi, Stephane Gehant (BW Water); "
         "Victor Gutierrez, Jorge Guevara, Ronald Pellejero (ADASA)"),
        ("Subject:",
         "Taltal SWRO Module - Weekly Shop Inspection Plan at Penang "
         "(Third-Party Surveillance and FAT)"),
        ("Ref:",
         "Contract C-4300 / BAE 12803 / "
         "Inspection and Test Plan P22-BA-09-000-004 Rev 0 / "
         "Technical Note P22-NT-09-000-002-0 / "
         "Bureau Veritas Quotation 600049"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # ---- CUERPO -------------------------------------------------------------
    add_para(doc, "Dear Luis, dear Mohd Adnin, dear Lokman,")
    blank(doc)

    add_para(
        doc,
        "I am writing to connect Bureau Veritas, ADASA's third-party "
        "inspector, with BW Water's QAQC team at the Penang workshop, so that "
        "you coordinate the shop inspection of the Taltal SWRO module "
        "directly. Below I set out the weekly inspection plan as the common "
        "reference for that coordination. Bureau Veritas acts under the "
        "Inspection and Test Plan (P22-BA-09-000-004, Rev 0) and Technical "
        "Note P22-NT-09-000-002-0; Mohd Adnin Zulkifli (Senior QAQC Engineer) "
        "and Lokman Hakim Mat (Project Engineer) are the points of contact at "
        "Penang, with BW Water's project management on copy.",
    )
    blank(doc)

    add_para(
        doc,
        "The approved Inspection and Test Plan (P22-BA-09-000-004, Rev 0) is "
        "the base document for planning the inspections; the weekly milestones "
        "below map to its Hold (H) and Witness (W) points. The inspection is "
        "organised by weekly milestones: six weekly quality-surveillance weeks "
        "during fabrication, followed by the Factory Acceptance Test week. Each "
        "surveillance week comprises three site visits, timed to that week's "
        "activity. The weekly milestones are:",
    )
    blank(doc)

    add_table_with_header(
        doc,
        ["Week", "Window", "Weekly milestone (scope witnessed)", "Visits"],
        [
            ["1", "27-31 Jul",
             "Super Duplex and SS316 spool fabrication; PMI on Super Duplex; "
             "welder and procedure qualification; visual inspection of SDX "
             "welds; receipt of critical materials", "3"],
            ["2", "3-7 Aug",
             "Spool completion; NDE of high-pressure welds (RT, PT root and "
             "final, UT); skid dimensional control", "3"],
            ["3", "10-14 Aug",
             "Piping hydrostatic tests (LP 7.5 bar and HP Super Duplex 135 "
             "bar, Hold Point); RO vessel hydrostatic test (Hold Point); "
             "surface preparation and coating DFT", "3"],
            ["4", "17-21 Aug",
             "Structure coating completion; final piping and instrument "
             "assembly on the skid; final coating DFT", "3"],
            ["5", "24-28 Aug",
             "Equipment positioning inside the container; high-pressure piping "
             "alignment", "3"],
            ["6", "31 Aug-4 Sep",
             "Container (CSC) inspection; HP pump and turbocharger positioning "
             "and alignment (arrival about 2 September); start of control "
             "panel integration and termination", "3"],
            ["FAT", "approx. 7-12 Sep",
             "System FAT: procedure approval, visual and completeness, final "
             "dimensional, dry functional tests, PLC/HMI test with fault "
             "simulation, Chilean electrical (SEC) compliance, HP piping "
             "thickness UT, ADASA FAT Approval Certificate, preservation and "
             "packing, Dispatch Release", "7 days"],
        ],
        widths=[Inches(0.55), Inches(1.05), Inches(4.55), Inches(0.65)],
    )

    blank(doc)

    add_para(
        doc,
        "The exact days within each week are set by BW Water's formal Hold and "
        "Witness notifications for the Penang workshop, issued in advance under "
        "BAE Clause 37. The windows are anchored to the current fixed "
        "fabrication schedule and, as of this week, none of them has moved. The "
        "high-pressure pump and the two turbochargers arrive at Penang around 2 "
        "September, which governs Week 6 and the start of the FAT.",
    )
    blank(doc)

    add_para(doc, "To finalise the coordination, we ask the following:")
    blank(doc)

    add_numbered(
        doc, 1, "Bureau Veritas to confirm mobilisation for Week 1",
        "(27 to 31 July), which is firm, and availability for the weekly "
        "windows through the FAT week. The working day is Monday to Thursday.",
    )
    add_numbered(
        doc, 2, "The Penang QAQC team (Mohd Adnin Zulkifli and Lokman Hakim "
        "Mat) to confirm readiness week by week",
        "and to issue the Hold and Witness notifications with advance notice, "
        "so Bureau Veritas can schedule the three visits of each week and "
        "witness each Hold and Witness point.",
    )
    add_numbered(
        doc, 3, "A kick-off meeting between Bureau Veritas, ADASA and BW Water "
        "before Week 1,",
        "to align the notification protocol, site access and reporting. Please "
        "propose a date and attendees.",
    )
    blank(doc)

    add_para(
        doc,
        "Any change to the fixed schedule that moves a weekly window must be "
        "notified to ADASA in writing and in advance, stating its cause, so "
        "the affected visits can be rescheduled under the applicable notice "
        "protocol.",
    )
    blank(doc)

    p = doc.add_paragraph()
    r = p.add_run("The current inspection documentation (procedures, drawings "
                  "and datasheets) is available for download at the link below; "
                  "any subsequent update or revision will be delivered through "
                  "this same channel: ")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    add_hyperlink(p, DOWNLOAD_LINK, DOWNLOAD_LINK)
    blank(doc)

    # ---- CIERRE -------------------------------------------------------------
    add_para(doc, "We look forward to confirming the weekly attendance and to "
                  "the kick-off meeting.")
    blank(doc)
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Infrastructure Engineering Lead",
        "Desalination Projects Department",
        "ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line)

    fijar_idioma_documento(doc, LANG)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="Taltal SWRO - Weekly Shop Inspection Plan (Bureau Veritas)",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Weekly shop inspection plan at Penang - third-party "
                "surveillance and FAT",
        comments="Correo conjunto ADASA a Bureau Veritas (CC BW Water) - plan "
                 "de inspeccion de taller por semanas.",
        category="Correspondencia",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas de Antofagasta S.A.")
    print(f"Correo generado: {OUTPUT_FILE}")
    print(f"Idioma del documento: {LANG}")


if __name__ == "__main__":
    crear_correo()
