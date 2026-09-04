#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Respuesta al Schedule BW Water
Fecha: 10 de febrero de 2026
Asunto: RE: Catch-Up Schedule Request - Schedule Review and Outstanding Requirements

Version 2: Estructura fluida tipo correo profesional (sin numeracion de secciones).
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn

CONTACTO = {
    "nombre": "Luis Rivera",
    "cargo": "Leader, Infrastructure Engineering",
    "empresa": "ADASA - Aguas de Antofagasta S.A.",
}


def aplicar_arial(paragraph, size=11):
    """Aplica formato Arial al parrafo"""
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_bold_label(doc, label, size=11):
    """Agrega un parrafo con texto en bold como etiqueta de seccion inline"""
    para = doc.add_paragraph()
    run = para.add_run(label)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para(doc, text, size=11):
    """Agrega un parrafo normal con formato Arial"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para_mixed(doc, fragments, size=11):
    """Agrega un parrafo con fragmentos de texto (bold/normal mezclados).
    fragments: lista de tuplas (text, bold)
    """
    para = doc.add_paragraph()
    for text, bold in fragments:
        run = para.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(size)
        run.bold = bold
    return para


def set_table_borders(table):
    """Aplica bordes a toda la tabla via XML"""
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


def add_table_simple(doc, headers, rows):
    """Agrega tabla con bordes, header en negrita y formato Arial"""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.autofit = True
    set_table_borders(table)

    # Header row
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(9)
        # Fondo azul claro
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
            run = cell.paragraphs[0].add_run(str(val))
            run.font.name = "Arial"
            run.font.size = Pt(9)

    doc.add_paragraph()
    return table


def crear_correo():
    """Genera el correo en formato DOCX"""

    output_file = "2026-02-10_Respuesta-Schedule-BW-Water.docx"
    doc = Document()

    # Margenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ============ HEADER ============
    header_fields = [
        ("Date:", "February 10, 2026"),
        (
            "From:",
            f"{CONTACTO['nombre']} - {CONTACTO['cargo']} ({CONTACTO['empresa']})",
        ),
        ("To:", "Eduardo Yamauchi - Operations Director Americas (BW Water)"),
        ("CC:", "ADASA Technical Management; BW Water Engineering Team"),
        (
            "Subject:",
            "RE: Catch-Up Schedule Request - Schedule Review and "
            "Outstanding Requirements",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / Schedule 090226 / TM N3 & N4"),
    ]
    for label, value in header_fields:
        para = doc.add_paragraph()
        para.add_run(label + " ").bold = True
        para.add_run(value)
        aplicar_arial(para)

    doc.add_paragraph()

    # ============ SALUDO + APERTURA ============
    add_para(doc, "Dear Eduardo,")

    doc.add_paragraph()

    add_para(
        doc,
        "Thank you for your response of February 9 and for the updated project schedule "
        "(Taltal water treatment plant base schedule 090226). We have reviewed the document "
        "in detail against the October 2025 baseline and our internal ADASA program, and "
        "need to share our observations.",
    )

    # ============ ENGINEERING DELAY (con contractual organico) ============
    doc.add_paragraph()
    add_bold_label(doc, "Engineering Delay")

    add_para(
        doc,
        "The most significant finding is the engineering phase extension. The original "
        "baseline established 65 days for engineering, completing on January 5, 2026. The "
        "updated schedule now shows 139 days, extending to April 24, 2026 \u2014 a 109-day "
        "delay from the original completion date, well beyond the 35 days we reported on "
        "February 9.",
    )

    # Contractual woven in organically
    para = doc.add_paragraph()
    run = para.add_run(
        "We need to be transparent about the contractual implications of this situation. "
        "Under ET Section 7, engineering documentation was due within 90 days of the award "
        "notification. BAE Clause 43.1.a establishes automatic penalties for delays in "
        "engineering delivery (0.05% of the net contract value per calendar day), which "
        "apply from the first day the deadline is exceeded without need for prior notice. "
        "As of today, that deadline has been exceeded by 36 calendar days, and your updated "
        "schedule projects an additional 73 days. We raise this not to escalate the "
        "situation, but so that both parties have a clear and shared understanding of the "
        "contractual position. "
    )
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run2 = para.add_run(
        "ADASA reserves all rights under the Contract, including the application of "
        "penalties per BAE Clause 43 and the provisions established in BAE Clauses 49 "
        "and 50."
    )
    run2.font.name = "Arial"
    run2.font.size = Pt(11)
    run2.bold = True

    add_para(
        doc,
        "We need confirmation that the April 24 date is the revised baseline for "
        "engineering and what specific measures are being implemented to prevent "
        "further extension.",
    )

    # ============ SCHEDULE GAPS (FAT + EXW merged) ============
    doc.add_paragraph()
    add_bold_label(doc, "Schedule Gaps")

    add_para(
        doc,
        "Beyond the engineering timeline, the updated schedule presents several gaps "
        "relative to the contract scope. It ends at Shipping (September 16, 2026) and "
        "omits four contractual milestones: Factory Acceptance Test (previously July "
        "30\u201331), Site Supervision and Commissioning (21 days), Operator Training "
        "(9 days), and Final Documentation and Close-out (30 days). These must be "
        "incorporated into the schedule.",
    )

    add_para(
        doc,
        "There is also a question about the delivery point. The schedule shows "
        '"Shipment from Penang to Florida" (45 days), but under Contract C-4300 the '
        "delivery term is EXW from Malaysia \u2014 ADASA arranges transportation from the "
        "manufacturing facility to Chile. We need to understand why the schedule routes "
        "the module to Florida instead of making it available EXW at Penang. Does this "
        "reflect a change in the assembly or consolidation process? What is the actual "
        "date when the module will be available for ADASA pickup under EXW terms?",
    )

    # ============ DOCUMENT SCHEDULE ============
    doc.add_paragraph()
    add_bold_label(doc, "Document Delivery Schedule")

    add_para(
        doc,
        "The schedule does not contain any breakdown of engineering deliverable dates. As "
        "of today, 14 documents remain undelivered and 16 require revision. Your note that "
        '"the team is still working on the schedule of documents" is acknowledged, but this '
        "was the most critical component of our original request dated January 28. Without "
        "this schedule, neither party can effectively plan procurement, fabrication, or "
        "construction activities.",
    )

    # ============ PROCUREMENT (2 parrafos fluidos, sin sub-encabezados) ============
    doc.add_paragraph()
    add_bold_label(doc, "Procurement and Engineering Approval")

    add_para(
        doc,
        "Our review identified a concerning pattern in the schedule: procurement activities "
        "(PR/PO) are programmed for several equipment items before their datasheets have "
        "been approved by ADASA. This creates a concrete risk of purchasing equipment that "
        "does not meet the project specifications, leading to costly rework or delays.",
    )

    add_para(doc, "Specifically:")

    # 5 equipos como bullet list
    equipment_items = [
        (
            "RO High Pressure Feed Pump",
            " \u2014 PR/PO starting February 16, with 135 days of manufacturing ahead. "
            'Datasheet Rev B carries a "To be revised" verdict: missing Pt-100 sensors in '
            "motor windings, four inconsistent power values across documents "
            "(83/86/92/93 kW), and missing vibration transmitters. The motor power "
            "specification alone affects VFD sizing, cable dimensioning, and protection "
            "settings.",
        ),
        (
            "Instrument Set and Valve Set",
            ' \u2014 PR/PO starting March 11. Both lists carry "To be revised" verdicts '
            "with known errors: duplicate TAG FIT-09-001, missing sensors, and a DN100 "
            "ANSI 900# valve with manual actuation where the ET requires electric.",
        ),
        (
            "Antiscalant Dosing System",
            " \u2014 PR/PO starting February 25\u201326. Subject to our open Technical "
            "Query CT-001 questioning whether the 0.5 ppm dosing rate is adequate. If "
            "revised upward, the current pump capacity (2.3 L/h) and tank volume (340L) "
            "may be insufficient.",
        ),
        (
            "Static Mixer",
            " \u2014 Schedule shows manufacturing completed October\u2013November 2025, "
            "while the datasheet is still under review for a PVC vs. FRP material question. "
            "If already manufactured, we need confirmation of the material used.",
        ),
        (
            "Electrical Panel / MCC",
            " \u2014 Schedule shows delivery completed January 2026, yet the MCC Datasheet "
            "has never been submitted to ADASA (83 days overdue from baseline). We request "
            "it be submitted immediately for retroactive verification.",
        ),
    ]
    for equip_name, equip_text in equipment_items:
        para = doc.add_paragraph()
        from docx.shared import Cm

        para.paragraph_format.left_indent = Cm(1.27)
        para.paragraph_format.first_line_indent = Cm(-0.63)
        run = para.add_run("\u2022 ")
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run = para.add_run(equip_name)
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.bold = True
        run = para.add_run(equip_text)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    # Recomendacion en bold
    add_para_mixed(
        doc,
        [
            (
                "We recommend that no purchase orders be issued for equipment whose datasheets "
                'carry a "To be revised" verdict until ADASA\u2019s observations are resolved.',
                True,
            ),
        ],
    )

    # ============ OUTSTANDING REQUIREMENTS (tabla) ============
    doc.add_paragraph()
    add_bold_label(doc, "Outstanding Requirements")

    add_para(
        doc,
        "The following items from our communications of January 28 and February 9 "
        "remain pending:",
    )

    add_table_simple(
        doc,
        ["#", "Requirement", "Original Deadline", "Status"],
        [
            [
                "1",
                "Document delivery schedule\n(14 pending + 16 requiring revision)",
                "Feb 6, 2026",
                "Overdue",
            ],
            [
                "2",
                "Mitigation plan for engineering delay",
                "Feb 6, 2026",
                "Not received",
            ],
            ["3", "Updated milestones (incl. FAT, RTS)", "Feb 6, 2026", "Partial"],
            [
                "4",
                "Response to TM N3 (P22-TM-09-000-003-0)",
                "Jan 28, 2026",
                "13 days pending",
            ],
            [
                "5",
                "Response to TM N4 (P22-TM-09-000-004-0)",
                "Feb 3, 2026",
                "7 days pending",
            ],
            ["6", "Response to CT-001 (Antiscalant dosing)", "Feb 10, 2026", "Overdue"],
            ["7", "Modbus TCP Memory Map delivery", "Dec 2025", "45+ days overdue"],
            [
                "8",
                "A/C n+1 configuration & thermal calc.",
                "Dec 2025",
                "45+ days overdue",
            ],
        ],
    )

    # ============ WHAT WE NEED BY FEB 13 ============
    add_bold_label(doc, "What We Need by February 13, 2026")

    actions = [
        "Document delivery schedule with specific dates for all 14 pending documents "
        "and all 16 documents requiring revision.",
        "Clarification on EXW delivery point (Penang vs. Florida) and the actual date "
        "when the module will be available under EXW terms.",
        "Updated project schedule including FAT, Commissioning Supervision, Operator "
        "Training and Close-out activities.",
        "Confirmation that no purchase orders will be issued for equipment with "
        'datasheets marked "To be revised" until ADASA observations are resolved.',
        "Formal responses to Transmittals N3 and N4.",
    ]
    for i, action in enumerate(actions, 1):
        para = doc.add_paragraph()
        run_num = para.add_run(f"{i}. ")
        run_num.bold = True
        run_num.font.name = "Arial"
        run_num.font.size = Pt(11)
        run_text = para.add_run(action)
        run_text.font.name = "Arial"
        run_text.font.size = Pt(11)

    doc.add_paragraph()

    add_para(
        doc,
        "Additionally, we request a coordination meeting (video conference) within the "
        "next two weeks to review the schedule alignment between BW Water and ADASA and "
        "to discuss the engineering recovery plan. Please propose available dates.",
    )

    # ============ CIERRE ============
    doc.add_paragraph()
    add_para(
        doc,
        "We remain committed to supporting the project\u2019s success and stand ready to "
        "coordinate on any of these matters.",
    )

    # ============ FIRMA ============
    doc.add_paragraph()
    add_para(doc, "Best regards,")
    doc.add_paragraph()

    para = doc.add_paragraph()
    run = para.add_run(CONTACTO["nombre"])
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(11)

    add_para(doc, CONTACTO["cargo"])
    add_para(doc, CONTACTO["empresa"])

    # Save
    doc.save(output_file)
    print(f"Correo generado exitosamente: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_correo()
