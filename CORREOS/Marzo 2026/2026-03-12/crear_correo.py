#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Escalacion Multas Engineering Delay — Contract C-4300
Fecha: 12 de Marzo de 2026
Destinatario: Eduardo Yamauchi (BW Water)
CC: Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske / Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import set_table_borders, calcular_anchos_columnas

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_FILE = "2026-03-12_Escalacion-Multas-Engineering.docx"
REMITENTE = "Luis Rivera Gonzalez"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_heading_paragraph(doc, text, level=1, size=12):
    """Agrega heading sin numeracion automatica del template."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_table(doc, data, col_widths=None):
    """
    Agrega tabla con bordes y encabezado en negrita.
    data: lista de tuplas [(col1, col2, ...), ...] — primera fila = encabezado
    col_widths: lista de anchos en Inches (opcional)
    """
    if not data:
        return

    num_cols = len(data[0])
    table = doc.add_table(rows=len(data), cols=num_cols)

    # Aplicar anchos si se especifican
    if col_widths:
        for row in table.rows:
            for i, cell in enumerate(row.cells):
                if i < len(col_widths):
                    cell.width = Inches(col_widths[i])

    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx]
        for col_idx, cell_text in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.text = ""
            para = cell.paragraphs[0]
            run = para.add_run(str(cell_text))
            run.font.name = "Arial"
            run.font.size = Pt(10)
            if row_idx == 0:
                run.bold = True

    set_table_borders(table)
    return table


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(1.1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "March 12, 2026"),
        ("From:", f"{REMITENTE} \u2014 Leader, Infrastructure Engineering (ADASA)"),
        ("To:", "Eduardo Yamauchi \u2014 Operations Director Americas (BW Water)"),
        ("CC:", (
            "Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) / "
            "Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)"
        )),
        ("Subject:", (
            "Contract C-4300 \u2014 Engineering Delay and Accumulated "
            "Contractual Penalties (BAE Cl. 43.1.a)"
        )),
        ("Ref:", "Contract C-4300 / BAE 12803 / ET Sec. 7 / TM N1\u2013TM N9"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        run_val = para.add_run(f" {value}")
        run_val.font.name = "Arial"
        run_val.font.size = Pt(11)
        aplicar_arial(para)

    doc.add_paragraph()

    # ── SALUDO ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear Mr. Yamauchi,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "This communication formally quantifies the contractual penalties accrued to date "
        "under Contract C-4300, resulting from BW Water\u2019s continued failure to complete "
        "the engineering deliverable program within the contractually established timeframe."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── SECCIÓN 1: ACCUMULATED DELAY ─────────────────────────────────────────
    add_heading_paragraph(doc, "1.  Accumulated Engineering Delay", size=12)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "ET \u2014 Engineering Schedule and Deliverables establishes a 90-calendar-day engineering "
        "period from Notice to Proceed. With NTP effective October 7, 2025, the contractual "
        "engineering completion deadline was January 5, 2026. BW Water\u2019s engineering program "
        "remains incomplete as of this date, placing BW Water in breach of this obligation "
        "for "
    )
    para.add_run("65 consecutive calendar days").bold = True
    para.add_run(" (January 6 \u2014 March 12, 2026).")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Under BAE Cl. 43 (p. 72), default is constituted automatically upon expiration "
        "of the agreed term, without prior notice, demand, or notification of any kind:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Cita BAE (bloque indentado)
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.5)
    para.paragraph_format.right_indent = Inches(0.5)
    run = para.add_run(
        "\u201cEl Proveedor quedar\u00e1 constituido en mora del cumplimiento de sus "
        "obligaciones por el solo hecho de exceder los plazos estipulados, sin necesidad "
        "de requerimiento, intimaci\u00f3n o notificaci\u00f3n alguna.\u201d"
    )
    run.italic = True
    run.font.name = "Arial"
    run.font.size = Pt(11)

    doc.add_paragraph()
    para = doc.add_paragraph(
        "BAE Cl. 43 (p. 72): The Supplier shall be in default of its obligations by the "
        "sole fact of exceeding the agreed deadlines, without any prior notice, demand, or "
        "notification being required."
    )
    para.paragraph_format.left_indent = Inches(0.5)
    para.paragraph_format.right_indent = Inches(0.5)
    para.runs[0].italic = True
    para.runs[0].font.name = "Arial"
    para.runs[0].font.size = Pt(10)
    doc.add_paragraph()

    # ── SECCIÓN 2: PENALTY CALCULATION ───────────────────────────────────────
    add_heading_paragraph(
        doc,
        "2.  Contractual Penalty Calculation (BAE Cl. 43.1.a \u2014 Engineering Delay)",
        size=12
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "BAE Cl. 43.1.a establishes a daily penalty of 0.05% of the net contract value for "
        "delay in engineering deliverables. Applied to Contract C-4300:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Daily penalty: ").bold = True
    para.add_run("0.05% \u00d7 USD 613,991.00 = ")
    para.add_run("USD 307.00 per calendar day").bold = True
    aplicar_arial(para)
    doc.add_paragraph()

    penalty_data = [
        ("Reference Date", "Days in Default", "Accumulated Penalty", "% of Cap (BAE 43.4)"),
        ("January 6, 2026 (start of default)", "1", "USD 307", "0.3%"),
        ("March 12, 2026 (today)", "65", "USD 19,955", "21.7%"),
        (
            "July 9, 2026\n(per BW Water Catch-Up Schedule Mar-2026)",
            "184",
            "USD 56,488",
            "61.3%"
        ),
    ]
    add_table(doc, penalty_data, col_widths=[2.6, 1.2, 1.5, 1.4])
    doc.add_paragraph()

    para = doc.add_paragraph(
        "BAE Cl. 43.4 establishes a total penalty cap of 15% of the net contract value: "
    )
    para.add_run("USD 92,098.65").bold = True
    para.add_run(
        ". At the current rate of accumulation, BW Water\u2019s own projected engineering "
        "completion date (July 9, 2026) would consume "
    )
    para.add_run("61.3% of that cap").bold = True
    para.add_run(
        " on engineering delay penalties alone \u2014 before any EXW delivery penalties are considered."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── SECCIÓN 3: DOCUMENT STATUS ────────────────────────────────────────────
    add_heading_paragraph(doc, "3.  Engineering Document Status", size=12)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "The following table summarizes the critical engineering deliverables that remain "
        "unresolved as of March 12, 2026:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    status_data = [
        ("Document", "Contractual Deadline", "Current Status", "Delay (days)"),
        (
            "Valve List Rev C",
            "January 5, 2026",
            "Code 4 Rejected \u2014 Rev C not submitted",
            "65+"
        ),
        (
            "Feed Turbocharger Datasheet Rev D",
            "January 5, 2026",
            "Code 4 Rejected \u2014 Rev D not submitted",
            "65+"
        ),
        (
            "Control Philosophy Rev B",
            "January 5, 2026",
            "Code 3 To Be Revised \u2014 Rev B not submitted (UPS 30 min vs. 8 h per ET)",
            "65+"
        ),
        (
            "P&ID Rev B \u2014 Corrective Resubmission",
            "January 5, 2026",
            "Code 3 To Be Revised (TM N9, March 11) \u2014 corrections pending",
            "65+"
        ),
        (
            "Modbus TCP Memory Map",
            "January 5, 2026",
            "Not submitted \u2014 committed in TM N2, now 75+ days overdue",
            "75+"
        ),
        (
            "IO List \u2014 Modbus signals update",
            "January 5, 2026",
            "Overdue since TM N3",
            "65+"
        ),
    ]
    add_table(doc, status_data, col_widths=[1.9, 1.4, 2.5, 0.9])
    doc.add_paragraph()

    para = doc.add_paragraph(
        "30 of approximately 55 engineering deliverables have received a final approval "
        "verdict (Code 1 or Code 2). Critical procurement-path documents remain unresolved, "
        "directly blocking ADASA\u2019s procurement activities and downstream engineering."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── SECCIÓN 4: CONTRACTUAL IMPLICATIONS ──────────────────────────────────
    add_heading_paragraph(doc, "4.  Contractual Implications", size=12)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("BAE Cl. 43.4 \u2014 Penalty Cap: ").bold = True
    para.add_run(
        "The total penalty ceiling is USD 92,098.65. As of today, USD 19,955 has accrued "
        "\u2014 21.7% of the cap. This figure increases by USD 307 for each additional "
        "calendar day of non-compliance."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("BAE Cl. 49 \u2014 Formal Non-Compliance Notice: ").bold = True
    para.add_run(
        "ADASA has not issued a formal non-compliance notice under BAE Cl. 49 at this stage. "
        "This letter constitutes an executive-level warning. Should the current situation not "
        "be corrected through specific, verifiable actions within the deadlines set forth in "
        "Section 5 below, ADASA will proceed with formal notification under BAE Cl. 49."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("BAE Cl. 50 \u2014 Contract Termination: ").bold = True
    para.add_run(
        "BAE Cl. 50 allows ADASA to terminate the contract if accumulated penalties reach or "
        "are reasonably projected to reach the 15% cap. BW Water\u2019s own Catch-Up Schedule "
        "(March 2026) projects engineering completion on July 9, 2026 \u2014 which would result "
        "in penalties of USD 56,488 from engineering delay alone, equivalent to 61.3% of the "
        "total cap. ADASA reserves all rights under BAE Cl. 50 should projected penalties "
        "approach this threshold."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "ADASA reserves all contractual rights under Contract C-4300, including the right "
        "to apply, offset, or enforce accumulated and future penalties in accordance with "
        "BAE Cl. 43, 49, and 50."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── SECCIÓN 5: REQUIRED ACTIONS ───────────────────────────────────────────
    add_heading_paragraph(doc, "5.  Required Actions", size=12)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "ADASA requires the following actions to be completed by the dates indicated:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    actions = [
        (
            "Valve List Rev C",
            "Submit corrected revision addressing all Code 4 observations "
            "(duplicate TAGs, incorrect actuation classification).",
            "March 16, 2026"
        ),
        (
            "Feed Turbocharger Datasheet Rev D",
            "Submit revision addressing coupling pressure rating (minimum 2,000 psi) "
            "and product class upgrade (Style H).",
            "March 25, 2026"
        ),
        (
            "Control Philosophy Rev B",
            "Submit corrected revision addressing: UPS backup duration (minimum 8 hours), "
            "CEE/MVE control function descriptions, and enable permissive interface "
            "(1 DI relay contact ADASA\u2192module, 1 DO relay contact module\u2192ADASA).",
            "March 20, 2026"
        ),
        (
            "Modbus TCP Memory Map",
            "Committed in TM N2, now 75+ days overdue. Submit immediately.",
            "March 14, 2026"
        ),
        (
            "Written Schedule Explanation",
            "Provide a written explanation, signed by BW Water management, of how the "
            "projected engineering completion date (July 9, 2026) is compatible with the "
            "EXW delivery obligation of August 3, 2026 and the contractual FAT, "
            "commissioning, and training program.",
            "March 16, 2026"
        ),
    ]

    for title, desc, deadline in actions:
        para = doc.add_paragraph(style="List Bullet")
        run_title = para.add_run(f"{title}: ")
        run_title.bold = True
        run_title.font.name = "Arial"
        run_title.font.size = Pt(11)
        run_desc = para.add_run(f"{desc} ")
        run_desc.font.name = "Arial"
        run_desc.font.size = Pt(11)
        run_dl = para.add_run(f"Deadline: {deadline}.")
        run_dl.bold = True
        run_dl.font.name = "Arial"
        run_dl.font.size = Pt(11)

    doc.add_paragraph()
    para = doc.add_paragraph(
        "Please confirm receipt of this communication and provide written acknowledgment "
        "of the required actions and their completion dates."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ────────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Sincerely,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(REMITENTE).bold = True
    aplicar_arial(para)
    for line in [
        "Leader, Infrastructure Engineering",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
