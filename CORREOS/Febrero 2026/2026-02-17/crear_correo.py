#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Acknowledgment of Responses
Fecha: 17 de febrero de 2026
Asunto: Acknowledgment of Responses - Transmittals N3, N4 and Schedule (C-4300)

Correo tipo profesional sin template ADASA (como todos los correos del proyecto).
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn

CONTACTO = {
    "nombre": "Luis Rivera Gonzalez",
    "cargo": "Leader, Infrastructure Engineering",
    "empresa": "ADASA - Aguas de Antofagasta S.A.",
    "proyecto": "BAE 12803 - Second Stage RO Brine Module Taltal",
}


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_bold_label(doc, label, size=11):
    para = doc.add_paragraph()
    run = para.add_run(label)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para_mixed(doc, fragments, size=11):
    para = doc.add_paragraph()
    for text, bold in fragments:
        run = para.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(size)
        run.bold = bold
    return para


def add_bullet(doc, text, size=11, bold_prefix=None):
    para = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        run = para.add_run(bold_prefix)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(size)
        run = para.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(size)
    else:
        run = para.add_run(text)
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


def add_table_simple(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.autofit = True
    set_table_borders(table)

    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(9)
        shading = cell._element.get_or_add_tcPr()
        shd = shading.makeelement(
            qn("w:shd"),
            {qn("w:val"): "clear", qn("w:color"): "auto", qn("w:fill"): "D9E2F3"},
        )
        shading.append(shd)

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
    output_file = "2026-02-17_Acuse-Recibo-Respuestas-BWW.docx"
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ============ HEADER ============
    header_fields = [
        ("Date:", "February 17, 2026"),
        (
            "From:",
            f"{CONTACTO['nombre']} - {CONTACTO['cargo']} ({CONTACTO['empresa']})",
        ),
        ("To:", "Eduardo Yamauchi - Operations Director Americas (BW Water)"),
        ("CC:", "ADASA Technical Management; BW Water Engineering Team"),
        (
            "Subject:",
            "Acknowledgment of Responses \u2014 Transmittals N3, N4 and "
            "Schedule (C-4300)",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803"),
    ]
    for label, value in header_fields:
        para = doc.add_paragraph()
        para.add_run(label + " ").bold = True
        para.add_run(value)
        aplicar_arial(para)

    doc.add_paragraph()

    # ============ OPENING ============
    add_para(doc, "Dear Eduardo,")
    doc.add_paragraph()

    add_para(
        doc,
        "We acknowledge receipt of your three responses dated February 16, 2026, "
        "covering Transmittal N3 (P22-TM-09-000-003-0), Transmittal N4 "
        "(P22-TM-09-000-004-0), and schedule-related items. Six items are accepted, "
        "but two critical items remain without acceptable resolution, and several "
        "others need clarification. Our full evaluation follows.",
    )

    # ============ ITEMS ACCEPTED ============
    doc.add_paragraph()
    add_bold_label(doc, "Items Accepted")

    add_para(doc, "We confirm the following items as resolved:")

    add_bullet(
        doc,
        " Pt-100 for windings and bearings confirmed per ET 5.3. Accepted.",
        bold_prefix="Pt-100 motor windings (TM N3 OBS-06 to OBS-09):",
    )
    add_bullet(
        doc,
        " Transmitters for HP Pump and Turbochargers confirmed per ET 5.5.7. Accepted.",
        bold_prefix="Vibration transmitters (TM N3 OBS-01):",
    )
    add_bullet(
        doc,
        " Renumbered to FIT-09-002. Accepted.",
        bold_prefix="Duplicate TAG FIT-09-001 (TM N3 OBS-05, TM N4 OBS-05):",
    )
    add_bullet(
        doc,
        " Second A/C unit confirmed per ET 5.1.11. Accepted.",
        bold_prefix="A/C n+1 configuration (TM N4 OBS-02):",
    )
    add_bullet(
        doc,
        " EXW Penang confirmed, shipping estimated August 3, 2026. Noted.",
        bold_prefix="EXW Penang basis (Schedule):",
    )
    add_bullet(
        doc,
        " POs will not be issued before ADASA approval. Recorded as formal commitment.",
        bold_prefix="No POs before datasheet approval (Schedule):",
    )

    # ============ CRITICAL ITEMS ============
    doc.add_paragraph()
    add_bold_label(doc, "Critical Items Requiring Immediate Resolution")

    add_para(
        doc,
        "These two items have been open for an unacceptable period and must be "
        "resolved at the February 18 meeting:",
    )

    add_table_simple(
        doc,
        ["Item", "Issue", "Required Action", "Open Since"],
        [
            [
                "Modbus TCP Memory Map\n(TM N4 OBS-04)",
                'Program "has not yet started" \u2014 42 days after '
                "commitment (TM N2, Jan 6). Prerequisite for "
                "PLC-to-PLC interface design.",
                "Concrete delivery date required. Discuss at Feb 18 meeting.",
                "42 days",
            ],
            [
                "Container 60ft\n(TM N4 OBS-10)",
                '"Still under review" \u2014 ADASA formally rejected '
                "the 60ft proposal on November 17, 2025 "
                "(+USD $67,208, +5 weeks) and confirmed this "
                "decision on December 17, 2025. The 40ft "
                "configuration is the approved basis.",
                "Engineering drawings must reflect the approved "
                "40ft configuration. Documents showing an enlarged "
                "container do not correspond to the communicated "
                "decision.",
                "92 days",
            ],
        ],
    )

    # ============ ITEMS REQUIRING CLARIFICATION ============
    add_bold_label(doc, "Items Requiring Clarification")

    add_bullet(
        doc,
        " Response does not explicitly confirm change to electric actuation. "
        "ET 5.2.3 requires electric for DN100 ANSI 900#. Please confirm: yes or no.",
        bold_prefix="VM-09-015 actuation (TM N3 OBS-03):",
    )
    add_bullet(
        doc,
        " Response addresses communication protocol, but our requirement is "
        "the data content \u2014 voltage, current, power, frequency, temperature "
        "from both VFDs as AI signals in the IO List for SEC calculation.",
        bold_prefix="VFD electrical variables (TM N3 OBS-15):",
    )
    add_bullet(
        doc,
        " Not addressed. Four values exist (83/86/92/93 kW). A single correct "
        "value must be established before procurement.",
        bold_prefix="HP Pump power (TM N4 OBS-08):",
    )
    add_bullet(
        doc,
        " Not addressed. ET 5.4 requires UPS with 8h autonomy for the control "
        "system. Must be added to BOM.",
        bold_prefix="UPS in BOM (TM N4 OBS-09):",
    )
    add_bullet(
        doc,
        " Responses cover 6/17 from TM N3 and 5/10 from TM N4. The remaining "
        "observations were not mentioned. Please confirm all are being tracked.",
        bold_prefix="Partial coverage (16 of 27 observations):",
    )

    # ============ EXTERNAL SIGNALS CLARIFICATION ============
    doc.add_paragraph()
    add_bold_label(doc, "Regarding OBS-04 and OBS-05 TM N3 (External Coordination Signals)")

    add_para(
        doc,
        "To provide the context you requested: the \u201cexternal system\u201d "
        "referred to in these observations is a PLC external to the BW Water "
        "module, part of the broader ADASA plant control architecture but outside "
        "BW Water\u2019s supply scope. This external PLC is currently in "
        "development. The coordination signals required between the two systems are:",
    )

    add_bullet(
        doc,
        " A digital output from the BW Water PLC indicating module running "
        "status (0 = stopped, 1 = running). This allows the external PLC to "
        "coordinate feed supply and reject disposal.",
        bold_prefix="DO \u2014 Module Status:",
    )
    add_bullet(
        doc,
        " A digital input to the BW Water PLC from the external system "
        "(1 = module authorized to operate, 0 = module must stop). This allows "
        "plant-level control over module operation.",
        bold_prefix="DI \u2014 External Enable:",
    )

    add_para(
        doc,
        "These are standard interface signals between independent control systems. "
        "They should be included in the IO List as hardwired signals (not via Modbus).",
    )

    # ============ MEETING ============
    doc.add_paragraph()
    add_bold_label(doc, "Coordination Meeting \u2014 February 18, 2026")

    add_para_mixed(
        doc,
        [
            (
                "We confirm the coordination meeting for tomorrow, ",
                False,
            ),
            ("Wednesday February 18, 9:00 AM EST (11:00 AM Chile)", True),
            (
                ". As discussed, we expect to receive before or during the meeting:",
                False,
            ),
        ],
    )

    add_bullet(doc, "Delivery plan with engineering milestones")
    add_bullet(doc, "Updated schedule showing document delivery dates")
    add_bullet(
        doc,
        "Document delivery schedule for the 14 pending documents and 16 "
        "currently under revision",
    )

    doc.add_paragraph()
    add_bold_label(doc, "Proposed Agenda (1 hour)")

    # Agenda table
    add_table_simple(
        doc,
        ["#", "Topic", "Time", "Key Items"],
        [
            [
                "1",
                "Engineering Recovery Plan",
                "15 min",
                "Delivery plan, Apr 24 baseline confirmation, mitigation actions",
            ],
            [
                "2",
                "Document Delivery Schedule",
                "10 min",
                "Dates for 14 pending + 16 under revision; priorities: MCC DS, "
                "CIP Pump DS, PIE Detallado",
            ],
            [
                "3",
                "Critical Open Items",
                "20 min",
                "Modbus Map (42d), Container 60ft (3 mo), HP Pump power (4 values), "
                "VM-09-015, VFD variables, UPS",
            ],
            [
                "4",
                "Procurement Alignment",
                "10 min",
                "No POs before approval, HP Pump PR/PO status, Antiscalant (CT-001 "
                "pending, deadline Feb 20)",
            ],
            [
                "5",
                "Next Steps & Follow-up",
                "5 min",
                "Action items, deadlines, next meeting",
            ],
        ],
    )

    add_para(doc, "Please confirm the agenda or propose modifications.")

    # ============ SIGNATURE ============
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
    add_para(doc, f"Project: {CONTACTO['proyecto']}")

    doc.save(output_file)
    print(f"Correo generado exitosamente: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_correo()
