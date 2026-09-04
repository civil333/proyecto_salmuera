#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar Notificacion Formal de Incumplimiento BAE 49
Formato ADASA con portada, cajetin y TOC
Se activa solo si BW Water no responde a Fase 1 (20-Feb-2026)

IMPORTANTE: Ajustar NOTIFICATION_DATE antes de ejecutar.
"""

import sys
import os
from datetime import date, timedelta

# Path a la skill template-adasa
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    ".claude",
    "skills",
    "template-adasa",
)
sys.path.insert(0, skill_path)

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn

from ejemplo_documento import crear_documento_adasa


# --- CONFIGURACION ---
TITULO = "FORMAL NON-COMPLIANCE NOTIFICATION"
CODIGO = "P22-CT-09-000-002-0"
OUTPUT = "P22-CT-09-000-002-0_Notificacion-Incumplimiento-BAE49_ADASA.docx"

# Datos del proyecto
CONTRACT_VALUE = 613991.00
DAILY_PENALTY_ENG = CONTRACT_VALUE * 0.0005  # 0.05%
DAILY_PENALTY_EXW = CONTRACT_VALUE * 0.002  # 0.20%
PENALTY_CAP = CONTRACT_VALUE * 0.15  # 15%
ENGINEERING_DEADLINE = date(2026, 1, 5)

# Fecha de emision (AJUSTAR cuando se active)
NOTIFICATION_DATE = date(2026, 2, 20)
DAYS_OVERDUE = (NOTIFICATION_DATE - ENGINEERING_DEADLINE).days
ACCUMULATED_PENALTY = DAYS_OVERDUE * DAILY_PENALTY_ENG
PROJECTED_DAYS = 109  # Hasta 24-Abr-2026
PROJECTED_PENALTY = PROJECTED_DAYS * DAILY_PENALTY_ENG
CURE_DEADLINE = NOTIFICATION_DATE + timedelta(days=10)


def set_updatefields_true(doc):
    """Configura el documento para actualizar campos (TOC) al abrir"""
    from docx.oxml.ns import qn as _qn

    settings = doc.settings.element
    update = settings.makeelement(_qn("w:updateFields"), {_qn("w:val"): "true"})
    settings.append(update)


def set_table_borders(table):
    """Apply borders to all cells in a table via XML"""
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


def set_repeat_table_header(row):
    """Configura una fila para repetirse como header en cada pagina"""
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    tblHeader = trPr.makeelement(qn('w:tblHeader'), {qn('w:val'): 'true'})
    trPr.append(tblHeader)


def add_table_with_borders(doc, headers, rows):
    """Agrega tabla con bordes, header en negrita/azul, formato Arial 9pt y repeat header"""
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

    # Repeat header row en cada pagina
    set_repeat_table_header(table.rows[0])

    doc.add_paragraph()
    return table


def add_section(doc, title, level=1):
    """Agrega heading con formato Arial"""
    h = doc.add_heading(title, level=level)
    for run in h.runs:
        run.font.name = "Arial"
    return h


def add_para(doc, text, bold=False, size=11):
    """Agrega parrafo con formato Arial"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    if bold:
        run.bold = True
    return para


def add_bullet(doc, text, size=11):
    """Agrega bullet point con prefijo manual"""
    para = doc.add_paragraph()
    run = para.add_run(f"\u2022 {text}")
    run.font.name = "Arial"
    run.font.size = Pt(size)
    from docx.shared import Cm

    para.paragraph_format.left_indent = Cm(1.27)
    para.paragraph_format.first_line_indent = Cm(-0.63)
    return para


def crear_notificacion():
    """Genera la notificacion formal BAE 49 en formato ADASA"""

    # 1. Crear documento base con portada y cajetin
    crear_documento_adasa(
        titulo=TITULO,
        codigo=CODIGO,
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
    )

    # 2. Abrir documento generado - limpiar contenido ejemplo y agregar real
    doc = Document(OUTPUT)

    # Eliminar contenido de ejemplo generado por crear_documento_adasa
    # (RESUMEN EJECUTIVO y 1. INTRODUCCION con textos placeholder)
    elements_to_remove = []
    body = doc.element.body
    # Buscar desde el final: los ultimos parrafos y headings son el contenido ejemplo
    found_heading = False
    for elem in reversed(list(body)):
        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        if tag == "p":
            # Check if it's a heading or normal paragraph
            text = elem.text if elem.text else ""
            # Get all text from element
            all_text = "".join(
                t.text or "" for t in elem.iter() if t.text and t.tag.endswith("}t")
            )
            if "RESUMEN EJECUTIVO" in all_text or "INTRODUCCIÓN" in all_text:
                elements_to_remove.append(elem)
                found_heading = True
            elif "Template ADASA" in all_text or "Reemplace este contenido" in all_text:
                elements_to_remove.append(elem)
            elif "Agregue aquí" in all_text:
                elements_to_remove.append(elem)
            elif found_heading and not all_text.strip():
                # Empty paragraphs near the headings
                elements_to_remove.append(elem)
            else:
                break
        else:
            break

    for elem in elements_to_remove:
        body.remove(elem)

    # === SUBTITLE ===
    add_para(
        doc,
        "Contract C-4300 / BAE 12803 - Second Stage RO Brine Module - PD Taltal",
        bold=True,
        size=12,
    )
    doc.add_paragraph()

    # === HEADER INFORMATION ===
    add_para(
        doc,
        "To: Andrew J. Zaske, Vice President Americas - BW Water Americas Inc.",
        bold=True,
    )
    add_para(
        doc,
        "CC: Eduardo Yamauchi, Operations Director Americas - BW Water Americas Inc.",
    )
    add_para(doc, "From: ADASA - Aguas de Antofagasta S.A.")
    add_para(doc, f"Date: {NOTIFICATION_DATE.strftime('%B %d, %Y')}")
    add_para(
        doc,
        "Ref: Contract C-4300 / BAE 12803 / BAE Clause 49 - Non-Compliance by Supplier",
    )
    doc.add_paragraph()

    # === SECTION 1: PURPOSE ===
    add_section(doc, "1. PURPOSE")
    add_para(
        doc,
        "In accordance with Clause 49 of the Bases Administrativas Especiales (BAE) for "
        "Public Tender 12803, ADASA hereby formally notifies BW Water Americas Inc. of the "
        "non-compliance situations described below, and requests that BW Water remedy the "
        f"identified breaches within ten (10) calendar days from receipt of this notification "
        f"(i.e., by {CURE_DEADLINE.strftime('%B %d, %Y')}).",
    )
    doc.add_paragraph()
    add_para(
        doc,
        "This notification is issued without prejudice to the automatic application of delay "
        "penalties under BAE Clause 43.1, which have been accruing since the engineering "
        "delivery deadline was exceeded on January 5, 2026.",
    )

    # === SECTION 2: CONTRACTUAL FRAMEWORK ===
    add_section(doc, "2. CONTRACTUAL FRAMEWORK")
    add_table_with_borders(
        doc,
        ["Reference", "Description"],
        [
            ("BAE Clause 27", "Delivery deadlines: 300 days (EXW) / 510 days (total)"),
            ("BAE Clause 31", "Engineering documentation per ET Section 7"),
            (
                "BAE Clause 43.1.a",
                "Penalty for engineering delay: 0.05% of net value per calendar day",
            ),
            (
                "BAE Clause 43.1 (Auto)",
                "Penalties apply automatically upon exceeding deadlines, "
                "without need for prior notice or demand",
            ),
            ("BAE Clause 49", "Non-compliance notification: 10-day cure period"),
            (
                "BAE Clause 50",
                "Termination triggers: >30 days delay in delivery, "
                "penalties >15% of net value",
            ),
            (
                "ET Section 7",
                "Engineering deliverables within 90 days of award notification",
            ),
        ],
    )

    # === SECTION 3: IDENTIFIED NON-COMPLIANCE ===
    add_section(doc, "3. IDENTIFIED NON-COMPLIANCE")

    # 3.1
    add_section(doc, "3.1 Engineering Delay (BAE 43.1.a / ET Section 7)", level=2)
    add_para(
        doc,
        "The Technical Specifications (ET P22-ET-09-000-001-0, Section 7) require that all "
        "engineering documentation be submitted within 90 calendar days of the award notification. "
        "BW Water's own baseline schedule (October 2025) established the engineering completion "
        "date as January 5, 2026.",
    )
    doc.add_paragraph()
    add_para(
        doc,
        f"As of {NOTIFICATION_DATE.strftime('%B %d, %Y')}, BW Water has not completed the "
        "engineering phase. BW Water's updated schedule (February 9, 2026) acknowledges that "
        "engineering will extend to April 24, 2026, representing a delay of 109 calendar days "
        "beyond the original baseline.",
    )
    doc.add_paragraph()
    add_para(doc, "Current status of engineering deliverables:", bold=True)

    add_table_with_borders(
        doc,
        ["Category", "Count"],
        [
            ("Documents delivered and approved (verdict 1)", "21"),
            ("Documents approved with notes (verdict 2)", "14"),
            ("Documents requiring revision (verdict 3)", "13"),
            ("Documents rejected (verdict 4)", "3"),
            ("Documents never delivered", "14"),
            ("Total identified in ET Section 7", "~65"),
        ],
    )

    add_para(doc, "Key undelivered documents include:", bold=True)
    undelivered = [
        "MCC Datasheet (83+ days overdue from baseline)",
        "Modbus TCP Memory Map (committed in Transmittal N2 response, 45+ days overdue)",
        "A/C system n+1 configuration and thermal calculation (45+ days overdue)",
        "CIP Pump Datasheet (BH-09-002)",
        "Seismic Calculation Report",
        "Piping Flexibility Analysis",
    ]
    for item in undelivered:
        add_bullet(doc, item)

    # 3.2
    add_section(doc, "3.2 Equipment Procured Without ADASA Approval", level=2)
    add_para(
        doc,
        "BW Water has procured, manufactured, or delivered equipment without obtaining ADASA "
        "approval of the corresponding datasheets, in violation of the review process established "
        "in ET Section 7:",
    )
    add_table_with_borders(
        doc,
        ["Equipment", "Status", "Non-Compliance"],
        [
            (
                "Static Mixer",
                "Manufactured Oct-Nov 2025",
                'DS Rev A verdict "3 - To be revised" (PVC vs FRP). '
                "Equipment manufactured before resolution.",
            ),
            (
                "Electrical Panel / MCC",
                "Delivered Jan 2026",
                "MCC Datasheet never submitted to ADASA. "
                "Equipment fabricated and delivered without any ADASA review.",
            ),
            (
                "HP Pump",
                "PR/PO scheduled Feb 16, 2026",
                'DS Rev B verdict "3 - To be revised". Missing Pt-100 sensors, '
                "inconsistent power ratings (83/86/92/93 kW).",
            ),
        ],
    )

    # 3.3
    add_section(doc, "3.3 Failure to Respond to Formal Communications", level=2)
    add_para(
        doc,
        "ADASA has issued multiple formal communications to BW Water that remain unanswered:",
    )
    add_table_with_borders(
        doc,
        ["Communication", "Date Sent", "Days Without Response"],
        [
            (
                "Transmittal N3 (P22-TM-09-000-003-0)",
                "Jan 28, 2026",
                f"{(NOTIFICATION_DATE - date(2026, 1, 28)).days} days",
            ),
            (
                "Transmittal N4 (P22-TM-09-000-004-0)",
                "Feb 5, 2026",
                f"{(NOTIFICATION_DATE - date(2026, 2, 5)).days} days",
            ),
            (
                "Technical Query CT-001 (Antiscalant dosing)",
                "Feb 5, 2026",
                "Partial response Feb 13 (3 days late). "
                "Evaluation issued Feb 16 with 4 pending observations. "
                "Response deadline: Feb 20.",
            ),
            (
                "Schedule Review + Requirements",
                "Feb 10, 2026",
                f"{(NOTIFICATION_DATE - date(2026, 2, 10)).days} days",
            ),
            (
                "Escalation Follow-up",
                "Feb 14, 2026",
                f"{(NOTIFICATION_DATE - date(2026, 2, 14)).days} days",
            ),
        ],
    )

    # 3.4
    add_section(doc, "3.4 Missing Contractual Activities in Schedule", level=2)
    add_para(
        doc,
        "BW Water's updated schedule (February 2026) omits the following contractual obligations:",
    )
    missing = [
        "Factory Acceptance Test (FAT)",
        "Site Supervision and Commissioning",
        "Operator Training",
        "Final Documentation and Close-out",
        "Document delivery schedule (the most critical component requested by ADASA)",
    ]
    for item in missing:
        add_bullet(doc, item)

    add_para(
        doc,
        'Additionally, the schedule shows "Shipping from Penang to Florida" instead of '
        "making the module available EXW at the manufacturing facility in Malaysia, which is "
        "inconsistent with the EXW delivery term under Contract C-4300.",
    )

    # === SECTION 4: PENALTY CALCULATION ===
    add_section(doc, "4. PENALTY CALCULATION")
    add_para(
        doc,
        "Pursuant to BAE Clause 43.1.a, engineering delay penalties have been accruing "
        'automatically since January 6, 2026 (BAE Clause 43.1: "the Supplier shall be in '
        "default by the mere fact of exceeding the stipulated deadlines, without need for "
        'demand, notice, or notification of any kind"):',
    )
    add_table_with_borders(
        doc,
        ["Parameter", "Value"],
        [
            ("Net Contract Value", f"USD {CONTRACT_VALUE:,.2f}"),
            (
                "Daily Penalty Rate (BAE 43.1.a)",
                f"0.05% = USD {DAILY_PENALTY_ENG:,.2f}/day",
            ),
            ("Engineering Deadline (ET Sec 7 / BW Water baseline)", "January 5, 2026"),
            (
                f"Days of Delay (as of {NOTIFICATION_DATE.strftime('%b %d, %Y')})",
                f"{DAYS_OVERDUE} calendar days",
            ),
            ("Accumulated Penalty to Date", f"USD {ACCUMULATED_PENALTY:,.2f}"),
            (
                "Projected Penalty to April 24, 2026 (109 days per BW Water schedule)",
                f"USD {PROJECTED_PENALTY:,.2f}",
            ),
            ("Penalty Cap (BAE 43.4)", f"15% = USD {PENALTY_CAP:,.2f}"),
        ],
    )

    # === SECTION 5: REQUIRED REMEDIATION ACTIONS ===
    add_section(doc, "5. REQUIRED REMEDIATION ACTIONS")
    add_para(
        doc,
        f"In accordance with BAE Clause 49, BW Water is required to remedy the identified "
        f"non-compliance within ten (10) calendar days from receipt of this notification "
        f"(by {CURE_DEADLINE.strftime('%B %d, %Y')}). Specifically, ADASA requires:",
        bold=True,
    )
    doc.add_paragraph()

    actions = [
        "Immediate submission of a document delivery schedule with specific dates for all "
        "14 undelivered documents and all 16 documents requiring revision.",
        "Immediate submission of the MCC Datasheet for retroactive verification of the "
        "electrical panel already fabricated and delivered.",
        "Formal responses to Transmittals N3 and N4, including action plans for all "
        'observations marked as "To be revised."',
        "Response to Technical Query CT-001 (antiscalant dosing rate adequacy).",
        "Updated project schedule incorporating all contractual milestones (FAT, "
        "Commissioning Supervision, Operator Training, and Close-out), with clarification "
        "of the EXW delivery point and date.",
        "Written confirmation that no purchase orders will be issued for equipment whose "
        "datasheets have not been approved by ADASA.",
        "Submission of the Modbus TCP Memory Map and the A/C n+1 thermal calculation, "
        "both committed in the response to ADASA's Transmittal N2 (January 26, 2026).",
        "Engineering recovery plan demonstrating how BW Water intends to minimize the "
        "projected 109-day delay and recover toward the original schedule.",
    ]
    for i, action in enumerate(actions, 1):
        add_para(doc, f"{i}. {action}")

    # === SECTION 6: CONSEQUENCES ===
    add_section(doc, "6. CONSEQUENCES OF NON-REMEDIATION")
    add_para(
        doc,
        "BW Water is required to acknowledge receipt of this notification and inform ADASA "
        "without delay regarding the effects of the identified non-compliance and the "
        "corrective measures to be implemented (BAE Clause 49).",
    )
    doc.add_paragraph()
    add_para(
        doc,
        "If BW Water fails to remedy the identified non-compliance within the 10-day cure "
        "period, ADASA may exercise any or all of the following rights under the Contract:",
    )
    doc.add_paragraph()

    add_para(doc, "Under BAE Clause 49:", bold=True)
    add_bullet(
        doc,
        "Impose ADASA's technical assistance on BW Water, without relieving BW Water of "
        "its obligations and responsibilities, at BW Water's cost",
    )
    add_bullet(
        doc,
        "Substitute BW Water, in whole or in part, at BW Water's risk and expense "
        "(including a 15% surcharge for administrative costs per BAE Clause 49)",
    )
    doc.add_paragraph()

    add_para(doc, "Under BAE Clause 50:", bold=True)
    add_bullet(
        doc,
        "Early termination of the Contract, without incurring additional costs, on the "
        "grounds of contractual non-compliance as established in Clause 49 and/or manifest "
        "inability of the Supplier to deliver according to specifications and schedule",
    )
    doc.add_paragraph()

    add_para(doc, "Under BAE Clause 43:", bold=True)
    add_bullet(doc, "Continued automatic accrual of delay penalties")
    add_bullet(
        doc,
        "Deduction of accumulated penalties from pending payments or execution of the "
        f"Performance Bond (Boleta de Fiel Cumplimiento, USD {PENALTY_CAP:,.2f})",
    )

    # === SECTION 7: RESERVATION OF RIGHTS ===
    add_section(doc, "7. RESERVATION OF RIGHTS")
    add_para(
        doc,
        "This notification constitutes the formal notice required under BAE Clause 49. "
        "ADASA reserves all rights under the Contract, the BAE, and applicable law, "
        "including but not limited to:",
        bold=True,
    )
    doc.add_paragraph()
    rights = [
        "The right to apply all accumulated and future delay penalties under BAE Clause 43",
        "The right to terminate the Contract under BAE Clause 50",
        "The right to claim full indemnification for damages and losses",
        f"The right to execute the Performance Bond "
        f"(USD {PENALTY_CAP:,.2f}) under BAE Clause 29.2",
    ]
    for r in rights:
        add_bullet(doc, r)

    doc.add_paragraph()
    add_para(
        doc,
        "Nothing in this notification shall be construed as a waiver of any right or remedy "
        "available to ADASA.",
    )

    # === SIGNATURE ===
    doc.add_paragraph()
    doc.add_paragraph()
    add_para(doc, "For ADASA - Aguas de Antofagasta S.A.", bold=True, size=12)
    doc.add_paragraph()
    doc.add_paragraph()

    add_para(doc, "Luis Rivera Gonzalez", bold=True)
    add_para(doc, "Leader, Infrastructure Engineering")
    add_para(doc, "Project BAE 12803 - Second Stage RO Brine Module Taltal")
    doc.add_paragraph()

    add_para(doc, "Victor Gutierrez", bold=True)
    add_para(doc, "[Cargo]")
    add_para(doc, "ADASA - Aguas de Antofagasta S.A.")

    # Configure TOC update
    set_updatefields_true(doc)

    # Save
    doc.save(OUTPUT)
    print(f"\nNotificacion formal generada: {OUTPUT}")
    print(f"  Fecha notificacion: {NOTIFICATION_DATE.strftime('%d-%b-%Y')}")
    print(f"  Dias atraso ingenieria: {DAYS_OVERDUE}")
    print(f"  Multa acumulada: USD {ACCUMULATED_PENALTY:,.2f}")
    print(f"  Multa proyectada (109 dias): USD {PROJECTED_PENALTY:,.2f}")
    print(f"  Deadline cure period: {CURE_DEADLINE.strftime('%d-%b-%Y')}")
    print(
        f"\nNOTA: Ajustar NOTIFICATION_DATE en el script antes de generar version final."
    )
    return OUTPUT


if __name__ == "__main__":
    crear_notificacion()
