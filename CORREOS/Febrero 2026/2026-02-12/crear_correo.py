#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar correo DOCX - Reminder: Response Deadline Tomorrow
Fecha: 12 de febrero de 2026
Asunto: RE: Catch-Up Schedule Request - Reminder: Response Deadline Tomorrow (C-4300)

Estructura fluida tipo correo profesional (sin numeracion de secciones).
Sigue el estilo del correo 2026-02-10.
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

    output_file = "2026-02-12_Reminder-Deadline-TM-N3-N4-CT001.docx"
    doc = Document()

    # Margenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ============ HEADER ============
    header_fields = [
        ("Date:", "February 12, 2026"),
        (
            "From:",
            f"{CONTACTO['nombre']} - {CONTACTO['cargo']} ({CONTACTO['empresa']})",
        ),
        ("To:", "Eduardo Yamauchi - Operations Director Americas (BW Water)"),
        ("CC:", "ADASA Technical Management; BW Water Engineering Team"),
        (
            "Subject:",
            "Outstanding Responses Required - Transmittals N3, N4 and "
            "Technical Query CT-001 (C-4300)",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803"),
        (
            "Attachments:",
            "P22-TM-09-000-003-0 (TM N3), P22-TM-09-000-004-0 (TM N4), "
            "P22-CT-09-000-001-0 (CT-001)",
        ),
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

    add_para_mixed(
        doc,
        [
            (
                "We are writing regarding several outstanding items that require "
                "BW Water\u2019s response. Our email of February 10 set a deadline of ",
                False,
            ),
            ("February 13, 2026", True),
            (
                " \u2014 tomorrow \u2014 and we have not received a reply. "
                "The original transmittals and technical query are attached "
                "for reference.",
                False,
            ),
        ],
    )

    # ============ TRANSMITTAL RESPONSES ============
    doc.add_paragraph()
    add_bold_label(doc, "Transmittal Responses")

    add_para_mixed(
        doc,
        [
            (
                "Transmittal N3 (P22-TM-09-000-003-0), submitted January 28, contains "
                "17 technical observations across 23 documents. It has been ",
                False,
            ),
            ("15 days", True),
            (
                " without a formal response. Transmittal N4 (P22-TM-09-000-004-0), "
                "submitted February 5, addresses the PLC frequency specification, "
                "the A/C redundancy configuration, and the Modbus TCP Memory Map "
                "\u2014 ",
                False,
            ),
            ("7 days", True),
            (" pending.", False),
        ],
    )

    add_para(
        doc,
        "Several of these observations directly affect procurement activities "
        "already programmed in your updated schedule. "
        "The HP Pump datasheet carries a \u201cTo be revised\u201d verdict due to "
        "missing Pt-100 sensors and inconsistent power values (83/86/92/93 kW), "
        "yet PR/PO activity is scheduled to begin February 16. Purchasing equipment "
        "against unresolved datasheets creates a real risk of non-compliance with "
        "the project specifications.",
    )

    # ============ CT-001 ANTISCALANT ============
    doc.add_paragraph()
    add_bold_label(doc, "Technical Query CT-001 \u2014 Antiscalant Dosing")

    add_para_mixed(
        doc,
        [
            (
                "Technical Query CT-001 (P22-CT-09-000-001-0), requesting manufacturer "
                "documentation to support the 0.5 ppm antiscalant dosing rate, was "
                "submitted on February 5 with a response deadline of ",
                False,
            ),
            ("February 10", True),
            (". That deadline has passed.", False),
        ],
    )

    add_para(
        doc,
        "Your schedule shows antiscalant system procurement starting "
        "February 25\u201326, which leaves very little margin. If the "
        "manufacturer\u2019s scaling projection shows the dosing rate needs "
        "to be revised upward for concentrate conditions with LSI above 2.0, "
        "equipment sizing may need to change. We need this resolved before "
        "the purchase order is placed.",
    )

    # ============ OUTSTANDING ITEMS TABLE ============
    doc.add_paragraph()
    add_bold_label(doc, "Summary of Outstanding Items")

    add_table_simple(
        doc,
        ["#", "Item", "Submitted", "Deadline", "Status"],
        [
            [
                "1",
                "Document delivery schedule",
                "Jan 28, 2026",
                "Feb 6",
                "Overdue (6 days)",
            ],
            [
                "2",
                "Formal response to Transmittal N3",
                "Jan 28, 2026",
                "-",
                "15 days without response",
            ],
            [
                "3",
                "Formal response to Transmittal N4",
                "Feb 5, 2026",
                "-",
                "7 days without response",
            ],
            [
                "4",
                "Technical Query CT-001\n(Antiscalant dosing)",
                "Feb 5, 2026",
                "Feb 10",
                "Overdue (2 days)",
            ],
            [
                "5",
                "Schedule review + requirements\n(Feb 10 email)",
                "Feb 10, 2026",
                "Feb 13",
                "Deadline: tomorrow",
            ],
        ],
    )

    # ============ CIERRE ============
    add_para(
        doc,
        "We remain available for a coordination call if that helps move these "
        "items forward. That said, we do need the response by the agreed date "
        "\u2014 without it, ADASA cannot align its own planning and procurement "
        "activities with BW Water\u2019s schedule.",
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
    add_para(doc, f"Project: {CONTACTO['proyecto']}")

    # Save
    doc.save(output_file)
    print(f"Correo generado exitosamente: {output_file}")
    return output_file


if __name__ == "__main__":
    crear_correo()
