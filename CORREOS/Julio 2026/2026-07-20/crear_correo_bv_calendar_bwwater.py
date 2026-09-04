#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water: revision del calendario consolidado de Hold/Witness
points recibido de BW Water (Excel "TALTAL Witness and Hold point plan date",
creado por Mohd Adnin Bin Zulkaflee el 15-Jul-2026), en respuesta al thread
"RE: Taltal - Designation of Third-Party Shop Inspector and Inspection Schedule"
(reply de Eduardo Yamauchi del 15-Jul que suma a Magdier Arias, Quality Manager).

Reply-all al thread del RFI/NT-002 (cadena separada de los TM y de la replica a
la minuta 07-Jul). Idioma ingles (BW Water). Document() directo, sin template
ADASA (CLAUDE.md 3.4). Coordinacion: acusa a Magdier + recibe el calendario,
confirma V1-V4, exige reconciliar V5/V6 y el FAT, y reitera Kick-off +
notificaciones formales H/W + 3 procedimientos Codigo 3. Los frentes FAT
(compresion 10->5 dias y sitio del FAT de la bomba Fedco) se encuadran como
preguntas de coordinacion del calendario, no como reapertura de la disputa
contractual (esa vive en la replica a la minuta 07-Jul).

Verificado contra el Recovery Schedule / Progress Update de BW Water del 14-Jul
(SEMANA 13-07-26): bomba HP + turbos EAP Penang ~02-Sep, install bomba 03-04 Sep;
FAT del sistema (tarea 385) 24-Ago a 08-Sep con ready-to-ship (387) 09-10 Sep,
que contradice el FAT 16-18 Sep del calendario H/W. Estado: BORRADOR.
"""

import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-20_BWWater-HW-Calendar-Response.docx"
)
CONTACTO = "Luis Rivera González"
LANG = "en-US"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


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
        ("Date:", "July 20, 2026"),
        ("From:",
         f"{CONTACTO} — Infrastructure Engineering Lead (ADASA)"),
        ("To:",
         "Eduardo Yamauchi, Magdier Arias, Stephane Gehant — BW Water"),
        ("CC:",
         "Victor Gutierrez, Jorge Guevara, Ronald Pellejero — ADASA"),
        ("Subject:",
         "RE: Taltal - Designation of Third-Party Shop Inspector and "
         "Inspection Schedule"),
        ("Ref:",
         "Contract C-4300 / BAE 12803 / Technical Note P22-NT-09-000-002-0 / "
         "ITP P22-BA-09-000-004 Rev 0 / Hold and Witness Point calendar"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # ---- CUERPO -------------------------------------------------------------
    add_para(doc, "Dear Eduardo, dear Magdier,")
    blank(doc)

    add_para(
        doc,
        "Thank you. We welcome Magdier Arias joining the coordination, and we "
        "acknowledge the consolidated Hold Point and Witness Point calendar. We "
        "have cross-checked it against Technical Note P22-NT-09-000-002-0 and "
        "against BW Water's Recovery Schedule and progress report of 14 July. "
        "Visits 1 to 4 align with the indicative windows, and we take them as "
        "the basis to mobilise the inspector.",
    )
    blank(doc)

    add_para(
        doc,
        "We attach BW Water's Recovery Schedule and progress report of 14 July "
        "(25007 Taltal Progress Update). ADASA adopts this schedule as the "
        "fixed and binding reference for the shop inspection: its fabrication, "
        "FAT and dispatch dates are taken as firm and are not to slip further, "
        "and both the Hold and Witness Point calendar and the inspector's "
        "mobilisation are pinned to it. Measured against that fixed schedule, "
        "the following points must be reconciled before we finalise the "
        "inspector's attendance:",
    )
    blank(doc)

    add_table_with_header(
        doc,
        ["Visit", "Scope", "Planned date", "ADASA note"],
        [
            ["V1", "SDX PMI / welding", "28 Jul",
             "Aligned; basis for mobilisation"],
            ["V2", "NDE / dimensional", "06 Aug", "Aligned"],
            ["V3", "Hydrostatic 135 bar (Hold)", "12–13 Aug", "Aligned"],
            ["V4", "Coating / final assembly", "20 Aug", "Aligned"],
            ["V5", "Equipment positioning", "09 Sep",
             "Outside the 24–28 Aug window and same date as V6; "
             "align to the fixed schedule (1)"],
            ["V6", "HP pump/turbo + panel", "09 Sep",
             "Same date as V5; one event or two? (1)"],
            ["FAT", "System FAT to Dispatch Release", "16–18 Sep",
             "Later than the fixed 14 Jul schedule (FAT to 8 Sep; "
             "ready-to-ship 9–10 Sep); align to it (2)"],
        ],
        widths=[Inches(0.5), Inches(1.75), Inches(0.95), Inches(3.6)],
    )

    blank(doc)

    add_para(doc, "Against that fixed schedule, we ask BW Water to:")
    blank(doc)

    add_numbered(
        doc, 1, "Place Visits 5 and 6 on the fixed schedule.",
        "The calendar shows both on 09 September, whereas equipment "
        "positioning runs across the fixed schedule from mid-August (pressure "
        "vessel and cartridge filter) to early September (RO feed pump, on 3 "
        "to 4 September). These are two distinct surveillance events: "
        "equipment positioning and high-pressure alignment (V5), and HP pump "
        "and turbocharger alignment plus the start of panel integration (V6). "
        "Please set V5 and V6 on dates consistent with that positioning "
        "sequence, and confirm whether they are two separate surveillance "
        "dates or one combined event, so the inspector can witness each point.",
    )
    add_numbered(
        doc, 2, "Align the FAT dates to the fixed schedule.",
        "The calendar places the FAT on 16 to 18 September, later than the 14 "
        "July schedule, which shows the system FAT completing on 8 September "
        "and the module ready to ship on 9 to 10 September. Please correct the "
        "calendar so that the FAT date and the Dispatch Release date (a Hold "
        "Point that supports the 40% milestone) match the fixed schedule, and "
        "confirm that the FAT duration (noting the reduction from ten to five "
        "working days previously indicated) preserves the full Minimum Scope "
        "of FAT and the associated ITP Hold and Witness points: procedure "
        "approval, dry functional tests, PLC/HMI test with fault simulation, "
        "SEC compliance verification and Dispatch Release.",
    )
    add_numbered(
        doc, 3, "Witnessing is limited to the Penang workshop.",
        "The RO high-pressure feed pump and the two turbochargers are "
        "manufactured at the FEDCO facility in the United States and "
        "airfreighted to Penang around 2 September. ADASA, through Bureau "
        "Veritas, will witness the tests only at the Penang workshop and will "
        "not attend any pump or turbocharger factory test held at the FEDCO "
        "facility in the United States. Accordingly, please include the "
        "complete FEDCO factory test records and certificates in the "
        "equipment delivery dossier, together with the rest of the "
        "documentation.",
    )
    add_numbered(
        doc, 4, "Confirm the Kick-off Meeting",
        "between BW Water, ADASA and the inspector, ideally before or during "
        "the weekly meeting of Tuesday 21 July, with a proposed date and "
        "attendees.",
    )
    add_numbered(
        doc, 5, "Issue the formal Hold and Witness notifications",
        "under BAE Clause 37, with the applicable advance notice. Visit 1 (28 "
        "July) is already inside the notification window, so the formal "
        "notification for the first visit is needed at the earliest to allow "
        "the inspector to travel.",
    )
    add_numbered(
        doc, 6, "Resubmit the three quality procedures returned Code 3,",
        "required approved ahead of the mid-August pressure and coating "
        "windows: RO Vessel Hydrostatic Test Procedure (P22-BA-09-000-009), HP "
        "and LP Pressure Test Procedure (P22-BA-09-000-010) and Painting "
        "Procedure (P22-BA-09-000-011).",
    )
    blank(doc)

    add_para(
        doc,
        "We will review the alignment against the fixed schedule at the weekly "
        "meeting of Tuesday 21 July and finalise the inspector's mobilisation "
        "on that basis. Any deviation from the fixed schedule must be notified "
        "to ADASA in writing and in advance, stating its cause, so that the "
        "affected Hold and Witness points can be reassessed under the "
        "applicable notice protocol.",
    )
    blank(doc)

    # ---- CIERRE -------------------------------------------------------------
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Infrastructure Engineering Lead",
        "Desalination Projects Department",
        "ADASA — Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line)

    blank(doc)
    para = doc.add_paragraph()
    run = para.add_run(
        "Attachment: BW Water Recovery Schedule and progress report of 14 "
        "July 2026 (25007 Taltal Progress Update), adopted as the fixed "
        "reference for the shop inspection."
    )
    run.italic = True
    run.font.name = "Arial"
    run.font.size = Pt(10)

    fijar_idioma_documento(doc, LANG)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="Third-Party Shop Inspection - Hold and Witness Calendar Review",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Bureau Veritas shop inspection calendar",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")
    print(f"Idioma del documento: {LANG}")


if __name__ == "__main__":
    crear_correo()
