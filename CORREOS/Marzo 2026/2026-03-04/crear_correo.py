#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Clarification of Code 2 Review Comments
Fecha: 04 de marzo de 2026
Asunto: RE: 25007 Project Taltal — Clarification of Code 2 Review Comments

Correo tipo profesional sin template ADASA (correo directo, sin portada).
Responde consulta de Eduardo Yamauchi sobre notas de veredictos Code 2
en 4 documentos: Painting Spec, CIP Pump, CIP Cartridge Filter, Antiscalant Tank.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn

CONTACTO = {
    "nombre": "Luis Rivera Gonzalez",
    "cargo": "Leader, Infrastructure Engineering",
    "empresa": "ADASA \u2014 Aguas de Antofagasta S.A.",
    "proyecto": "BAE 12803 \u2014 Second Stage RO Brine Module Taltal",
}

OUTPUT_FILE = "2026-03-04_Clarification-Code2-Comments.docx"


# ─────────────────────────── helpers ────────────────────────────────────────

def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_bold_label(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_bullet(doc, text, size=11, bold_prefix=None):
    para = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        r = para.add_run(bold_prefix)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(size)
    r = para.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    return para


def add_numbered(doc, text, size=11, bold_prefix=None):
    para = doc.add_paragraph(style="List Number")
    if bold_prefix:
        r = para.add_run(bold_prefix)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(size)
    r = para.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    return para


def add_italic_quote(doc, text, size=10):
    """Cita de nota de revisión — fuente más pequeña, itálica."""
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.4)
    run = para.add_run(text)
    run.italic = True
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def set_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else tbl.makeelement(qn("w:tblPr"), {})
    borders = tblPr.makeelement(qn("w:tblBorders"), {})
    for border_name in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = borders.makeelement(
            qn(f"w:{border_name}"),
            {
                qn("w:val"): "single",
                qn("w:sz"): "4",
                qn("w:space"): "0",
                qn("w:color"): "000000",
            },
        )
        borders.append(border)
    tblPr.append(borders)
    if tbl.tblPr is None:
        tbl.insert(0, tblPr)


def add_info_table(doc, rows, size=9):
    """Tabla de 2 columnas: Campo | Valor. Sin encabezado."""
    table = doc.add_table(rows=len(rows), cols=2)
    table.autofit = True
    set_table_borders(table)
    for r_idx, (label, value) in enumerate(rows):
        cell_l = table.rows[r_idx].cells[0]
        cell_r = table.rows[r_idx].cells[1]
        cell_l.text = ""
        r = cell_l.paragraphs[0].add_run(label)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(size)
        cell_r.text = ""
        r = cell_r.paragraphs[0].add_run(value)
        r.font.name = "Arial"
        r.font.size = Pt(size)
    doc.add_paragraph()
    return table


def add_summary_table(doc, headers, rows, size=9):
    """Tabla general con encabezado sombreado."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.autofit = True
    set_table_borders(table)
    # Header row
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        r = cell.paragraphs[0].add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(size)
        shading = cell._element.get_or_add_tcPr()
        shd = shading.makeelement(
            qn("w:shd"),
            {qn("w:val"): "clear", qn("w:color"): "auto", qn("w:fill"): "D9E2F3"},
        )
        shading.append(shd)
    # Data rows
    for r_idx, row_data in enumerate(rows):
        for c_idx, val in enumerate(row_data):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = ""
            r = cell.paragraphs[0].add_run(str(val))
            r.font.name = "Arial"
            r.font.size = Pt(size)
    doc.add_paragraph()
    return table


def add_section_separator(doc):
    """Línea horizontal como separador entre secciones."""
    para = doc.add_paragraph()
    para.add_run("\u2014" * 60)
    aplicar_arial(para, size=9)
    return para


# ─────────────────────────── item blocks ────────────────────────────────────

def add_item_block(doc, number, title, info_rows, notes, action_text):
    """
    Genera un bloque estándar para cada ítem:
      - Número y título en negrita
      - Tabla de info (transmittal, submittal, verdict)
      - Notas de revisión en estilo cita
      - Acción BW Water requerida
    """
    # Título del ítem
    para = doc.add_paragraph()
    r = para.add_run(f"{number}. {title}")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)

    # Tabla de información del documento
    add_info_table(doc, info_rows, size=9)

    # Encabezado "Review Notes"
    add_para(doc, "Review Notes issued in the transmittal referenced above:", size=10)

    # Cada nota como cita itálica
    for note in notes:
        add_italic_quote(doc, note, size=10)

    # Acción requerida
    doc.add_paragraph()
    para = doc.add_paragraph()
    r = para.add_run("BW Water Action Required: ")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r = para.add_run(action_text)
    r.font.name = "Arial"
    r.font.size = Pt(10)

    doc.add_paragraph()


# ─────────────────────────── main ───────────────────────────────────────────

def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(1.1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    header_fields = [
        ("Date:", "March 4, 2026"),
        (
            "From:",
            f"{CONTACTO['nombre']} \u2014 {CONTACTO['cargo']} ({CONTACTO['empresa']})",
        ),
        (
            "To:",
            "Eduardo Yamauchi \u2014 Operations Director Americas (BW Water Americas Inc.)",
        ),
        (
            "CC:",
            "Jeryl F. Regulacion; Adzlan Bin Abd Rahim (BW Water)",
        ),
        (
            "Subject:",
            "RE: 25007 Project Taltal \u2014 Clarification of Code 2 Review Comments",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803"),
        (
            "Attachments:",
            "ADASA letter dated February 26, 2026 \u2014 Pending Technical Deliverables: "
            "Tie-in Definitions, CIP Footprint & Overdue P&ID Rev B (C-4300)",
        ),
    ]
    for label, value in header_fields:
        para = doc.add_paragraph()
        r = para.add_run(label + "  ")
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r = para.add_run(value)
        r.font.name = "Arial"
        r.font.size = Pt(10)

    doc.add_paragraph()

    # ── OPENING ─────────────────────────────────────────────────────────────
    add_para(doc, "Dear Eduardo,")
    doc.add_paragraph()
    add_para(
        doc,
        "Thank you for your message of March 4, 2026. We have reviewed your "
        "clarification request regarding the \u201cApproved as Noted\u201d (Code 2) "
        "verdicts for the four documents listed below. For each item, we confirm "
        "the transmittal in which the verdict was issued and provide the exact text "
        "of our review notes.",
    )
    doc.add_paragraph()

    # ── SUMMARY TABLE ───────────────────────────────────────────────────────
    add_summary_table(
        doc,
        ["#", "Document", "Code", "Transmittal", "Pending BW Water Action"],
        [
            [
                "1",
                "Painting Specifications\nP22-ET-09-006-002-A",
                "2",
                "TM N1\nP22-TM-09-000-001-0",
                "Correct RAL to 5012 +\nupdate DFT to 355 \u00b5m",
            ],
            [
                "2",
                "Datasheet of RO CIP/Flushing Pump\nP22-ET-09-009-003-B",
                "2",
                "TM N2\nP22-TM-09-000-002-0",
                "None",
            ],
            [
                "3",
                "Datasheet of CIP Cartridge Filter\nP22-ET-09-009-006-B",
                "2",
                "TM N2\nP22-TM-09-000-002-0",
                "Confirm piping/layout updated\n(horizontal orientation)",
            ],
            [
                "4",
                "Datasheet of Antiscalant Dosing Tank\nP22-ET-09-009-010-B",
                "2",
                "TM N4\nP22-TM-09-000-004-0",
                "Update P\u00acID capacity +\nrespond to CT-001",
            ],
        ],
        size=9,
    )

    doc.add_paragraph()

    # ── ITEM 1: PAINTING SPECIFICATIONS ─────────────────────────────────────
    add_item_block(
        doc,
        number=1,
        title="Painting Specifications (P22-ET-09-006-002-A)",
        info_rows=[
            ("Transmittal:", "N1 \u2014 P22-TM-09-000-001-0"),
            ("Verdict:", "2 \u2014 Approved as Noted"),
        ],
        notes=[
            "(a) \u201cColor specified as RAL 5017 (Traffic Blue) does not match "
            "ET Section 5.1.9 requirement of RAL 5012 (Luminous Blue) for the structural "
            "frame. Please confirm whether RAL 5017 is an intentional deviation; if so, "
            "provide technical justification. If not, correct to RAL 5012 and resubmit.\u201d",
            "(b) \u201cMinimum total dry film thickness (DFT) specified as 350 \u00b5m "
            "does not meet the 355 \u00b5m minimum required by ET Section 5.1.9. Update "
            "the specification accordingly.\u201d",
        ],
        action_text=(
            "(1) Confirm whether RAL 5017 (Traffic Blue) is an intentional deviation from "
            "ET 5.1.9 requirement of RAL 5012 (Luminous Blue). If intentional, provide "
            "technical justification; if not, correct to RAL 5012 and resubmit. "
            "(2) Update minimum total DFT from 350 \u00b5m to 355 \u00b5m per ET Section 5.1.9."
        ),
    )

    # ── ITEM 2: CIP PUMP ────────────────────────────────────────────────────
    add_item_block(
        doc,
        number=2,
        title="Datasheet of RO CIP / Flushing Pump (P22-ET-09-009-003-B)",
        info_rows=[
            ("Transmittal:", "N2 \u2014 P22-TM-09-000-002-0"),
            ("Verdict:", "2 \u2014 Approved as Noted"),
        ],
        notes=[
            "(a) \u201cVFD start type accepted as technical improvement over direct-on-line "
            "start specified in ET 5.1.4. No further action required.\u201d [Closed]",
            "(b) \u201cMotor brand change from Grundfos to Innomotics (Siemens) \u2014 "
            "accepted; verify compatibility with pump and system requirements.\u201d "
            "[Subsequently confirmed and accepted]",
        ],
        action_text=(
            "None. In Transmittal N3 we additionally requested confirmation of Pt-100 "
            "sensors in motor windings and bearings per ET Section 5.3. BW Water confirmed "
            "this on February 16, 2026, and ADASA accepted the resolution on February 17, "
            "2026. All observations associated with this Code 2 verdict are now closed."
        ),
    )

    # ── ITEM 3: CIP CARTRIDGE FILTER ────────────────────────────────────────
    add_item_block(
        doc,
        number=3,
        title="Datasheet of CIP Cartridge Filter (P22-ET-09-009-006-B)",
        info_rows=[
            ("Transmittal:", "N2 \u2014 P22-TM-09-000-002-0"),
            ("Verdict:", "2 \u2014 Approved as Noted"),
            (
                "Note:",
                "Upgraded from initial Code 3; upgrade based on Process Calculation "
                "P22-CD-09-009-001-B validating cartridge capacity.",
            ),
        ],
        notes=[
            "(a) \u201cCartridge count reduction from 19 to 17 \u2014 accepted. Process "
            "Calculation P22-CD-09-009-001-B validates capacity: 17 cartridges \u00d7 "
            "3.45 m\u00b2 filter area within manufacturer recommended flux range for "
            "57 m\u00b3/h flow.\u201d [Closed]",
            "(b) \u201cSwing Bolts closure mechanism vs. Quick Opening specified in "
            "ET 5.1.5 \u2014 noted as minor deviation. No revision required; "
            "recorded for reference.\u201d [Open \u2014 minor, no revision required]",
            "(c) \u201cOrientation change from Vertical to Horizontal \u2014 noted. "
            "Confirm that piping and layout drawings are updated to reflect the new "
            "orientation.\u201d [Open \u2014 minor]",
        ],
        action_text=(
            "Confirm that piping isometric and/or equipment layout drawings have been "
            "updated to reflect the horizontal filter orientation (Note c above). This "
            "update should be incorporated in the next layout revision."
        ),
    )

    # ── ITEM 4: ANTISCALANT DOSING TANK ─────────────────────────────────────
    add_item_block(
        doc,
        number=4,
        title="Datasheet of Antiscalant Dosing Tank (P22-ET-09-009-010-B)",
        info_rows=[
            ("Transmittal:", "N4 \u2014 P22-TM-09-000-004-0"),
            ("Verdict:", "2 \u2014 Approved as Noted"),
        ],
        notes=[
            "(a) \u201cMaterial change from HDPE to LMDPE accepted. Justification valid "
            "(dimensional constraints); delivered capacity 340 L exceeds committed "
            "capacity 246 L. No further action required.\u201d [Closed]",
            "(b) OBS-11 (Minor): \u201cTank capacity in P&ID (0.25 m\u00b3) differs "
            "from datasheet (0.34 m\u00b3 total / 0.27 m\u00b3 effective). Update P&ID "
            "in next revision.\u201d [Open \u2014 minor]",
            "(c) OBS-14 (Medium \u2014 Condition for Code 2): \u201cApproval is "
            "conditioned on satisfactory response to Technical Query "
            "P22-CT-09-000-001-0, which requests manufacturer validation of the "
            "0.5 ppm antiscalant dosing rate for concentrate conditions with Langelier "
            "Saturation Index (LSI) 2.0\u20132.11. This condition remains open.\u201d",
            "(d) CT-001 status: BW Water submitted a response on February 13, 2026 "
            "(AWC modeling by Pureflux SW/PROTON, reviewed by CREST Water). ADASA "
            "issued evaluation P22-CT-09-000-001-1 on February 16, 2026, identifying "
            "four open observations. The critical observation (Obs. 3 \u2014 Major): "
            "the AWC modeling did not use the complete brine characterization data "
            "available in the ANAM reports delivered during the tender \u2014 "
            "specifically, strontium was modeled as 0 mg/L while ANAM measured "
            "10\u201311 mg/L, SiO\u2082 worst-case was not applied (2.1 vs. 6.4 mg/L), "
            "and heavy metals data were omitted despite being included in the ANAM "
            "reports. The response deadline of February 20, 2026 has passed. "
            "The Code 2 condition OBS-14 remains open.",
        ],
        action_text=(
            "(1) Update P&ID (P22-DWG-09-009-002) with correct antiscalant tank total "
            "capacity (0.34 m\u00b3) in the next revision. Note that P&ID Rev B, "
            "incorporating all thirteen observations from Transmittal N2 (OBS-01 "
            "through OBS-14, except OBS-09), was formally requested by ADASA in our "
            "February 26, 2026 communication (subject: Pending Technical Deliverables "
            "\u2014 Tie-in Definitions, CIP Footprint & Overdue P&ID Rev B), "
            "as documented in the attached communication, with a "
            "delivery deadline of March 2, 2026. That deadline has now passed without "
            "a response. The tank capacity correction above must be incorporated in "
            "that same revision. "
            "(2) Respond to ADASA evaluation P22-CT-09-000-001-1 (issued February 16, "
            "2026) with revised AWC modeling using the complete ANAM brine "
            "characterization data, including: strontium (10\u201311 mg/L per ANAM "
            "measurements, not 0 mg/L as modeled), SiO\u2082 worst-case (6.4 mg/L, "
            "not 2.1 mg/L), and heavy metals data from the ANAM reports provided "
            "during the tender. The Code 2 condition OBS-14 remains open pending a "
            "satisfactory response to this evaluation."
        ),
    )

    # ── CLOSING ─────────────────────────────────────────────────────────────
    add_para(
        doc,
        "We trust this clarification addresses your request. Please contact us if "
        "additional information is needed on any of these items.",
    )
    doc.add_paragraph()
    add_para(doc, "Best regards,")
    doc.add_paragraph()

    para = doc.add_paragraph()
    r = para.add_run(CONTACTO["nombre"])
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)

    add_para(doc, CONTACTO["cargo"])
    add_para(doc, CONTACTO["empresa"])
    add_para(doc, f"Project: {CONTACTO['proyecto']}")

    doc.save(OUTPUT_FILE)
    print(f"Correo generado exitosamente: {OUTPUT_FILE}")
    return OUTPUT_FILE


if __name__ == "__main__":
    crear_correo()
