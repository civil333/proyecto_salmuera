#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N12 ADASA-BW_WATER
Entregas E22 (25007-0022) / E23 (25007-0023): 2 documentos tecnicos
Fecha: 30-Mar-2026

Veredicto: 3 - TO BE REVISED

Documentos:
  - P22-LI-09-008-014 Rev A   Datasheet of Vibration Transmitter   -> 3 - To be Revised
  - P22-LI-09-009-003 Rev B   Line List                             -> 2 - Approved as Noted

Observaciones cerradas en esta entrega:
  - TM N3 OBS-01: Line DA-SSD-DN80-09-005 design pressure -- actualizada a 80 bar (era 70 bar)

Observaciones nuevas:
  - OBS-01 (MAJOR): Vibration Transmitter -- HART no documentado en datasheet
  - NOTE-01 (MINOR): Vibration Transmitter -- Quantity "1 duty" para 3 TAGs VT-09-001/002/003
  - NOTE-01 (MINOR): Line List -- Linea Make-Up for CIP sin LINE NO.
  - NOTE-02 (MINOR): Line List -- "SCH80" debe ser "SCH 80S" para lineas SSD

Observaciones previas aun abiertas:
  - TM N10: OBS-01 a OBS-05, NOTE-05 (6 items)
  - TM N11: OBS-01 a OBS-04 (4 items)
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..", ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt


def crear_transmittal():
    output_file = "TRANSMITTAL N12 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N12 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-012-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    doc = Document(output_file)

    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(
            x in texto
            for x in [
                "RESUMEN EJECUTIVO",
                "INTRODUCCION",
                "INTRODUCCI\u00d3N",
                "1. INTRO",
                "ESTE DOCUMENTO HA SIDO GENERADO",
                "AGREGUE AQUI EL CONTENIDO",
                "AGREGUE AQU\u00cd EL CONTENIDO",
            ]
        ):
            paragraphs_to_remove.append(para)
    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== 1. EXECUTIVE SUMMARY =====
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Deliveries 22 and 23 (25007-0022\u00a0/\u00a025007-0023, received March\u00a019 and 26, "
        "2026) submit two documents. Two observations are raised \u2014 one MAJOR, one "
        "informational \u2014 plus three notes on the Line List."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Key findings:").bold = True
    aplicar_arial_12(para)

    bullets = [
        (
            "Datasheet of Vibration Transmitter Rev\u00a0A (Code\u00a03 \u2014 To be Revised):",
            " IFM VTV122 proposed for VT-09-001, VT-09-002, and VT-09-003. The submitted "
            "datasheet specifies a single 4\u201320\u00a0mA analog output; HART communication "
            "capability is not documented. The Technical Specification \u2014 Instrumentation "
            "requires 4\u201320\u00a0mA\u00a0+\u00a0HART for all field instruments. BW Water must "
            "confirm whether the VTV122 model proposed supports HART and provide evidence in "
            "Rev\u00a0B, or propose a HART-capable alternative or formal deviation.",
        ),
        (
            "Line List Rev\u00a0B (Code\u00a02 \u2014 Approved as Noted):",
            " Transmittal N3 OBS-01 confirmed closed \u2014 line DA-SSD-DN80-09-005 design "
            "pressure updated to 80\u00a0bar (margin\u00a017.6\u00a0%). Two notation notes raised "
            "on pipe schedule designation and one unassigned line identifier.",
        ),
    ]
    for bold_part, normal_part in bullets:
        para = doc.add_paragraph()
        para.add_run("\u2022  ")
        run = para.add_run(bold_part)
        run.bold = True
        para.add_run(normal_part)
        aplicar_arial_12(para)

    # ===== 2. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 2.1 Vibration Transmitter Datasheet Rev A ---
    doc.add_heading(
        "Datasheet of Vibration Transmitter Rev\u00a0A \u2014 P22-LI-09-008-014", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The IFM VTV122 covers all three required measurement points: VT-09-001 at the RO HP "
        "Feed Pump (BH-09-001), VT-09-002 at the Feed Turbocharger (SIP-09-001), and VT-09-003 "
        "at the Interstage Turbocharger (SIP-09-002). The MEMS technology, 0\u201325\u00a0mm/s "
        "RMS measurement range with 10\u20131000\u00a0Hz frequency band, and ISO\u00a010816 "
        "compliance are noted. IP67/68/69K ingress protection and SS316L housing are consistent "
        "with project installation requirements."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-01 \u2014 HART protocol not specified (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The VTV122 component datasheet (Section \u201cOutputs Communication\u201d, page\u00a02) "
        "specifies a single 4\u201320\u00a0mA analog current output. HART communication capability "
        "is not listed in the datasheet or in the manufacturer technical data pages."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Technical Specification \u2014 Instrumentation states that the instrumentation "
        "protocol for all field instruments shall be 4\u201320\u00a0mA + HART. No exception is "
        "provided in the Technical Specification \u2014 Vibration Transmitters section for "
        "vibration sensing devices."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must address this item in Rev\u00a0B with one of the following: (1) confirm "
        "that the VTV122 model proposed supports HART communication and provide manufacturer "
        "documentation as evidence; (2) propose a HART-capable vibration transmitter meeting "
        "the measurement requirements (0\u201325\u00a0mm/s RMS, 10\u20131000\u00a0Hz, "
        "ISO\u00a010816, IP67, SS316L housing); or (3) submit a formal deviation document "
        "citing the specific clause in the Technical Specification that permits omission of "
        "HART for vibration transmitters, with ADASA approval prior to procurement."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 Quantity field inconsistency (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The datasheet header lists three component TAGs (VT-09-001\u00a0/\u00a0002\u00a0/\u00a0003), "
        "while the \u201cQuantity\u00a0\u2014\u00a0Duty\u201d field reads\u00a01. The project "
        "requires three physical units: one at the HP Feed Pump (BH-09-001), one at the Feed "
        "Turbocharger (SIP-09-001), and one at the Interstage Turbocharger (SIP-09-002). Confirm "
        "procurement quantity\u00a0=\u00a03 and update the field in Rev\u00a0B."
    )
    aplicar_arial_12(para)

    # --- 2.2 Line List Rev B ---
    doc.add_heading("Line List Rev\u00a0B \u2014 P22-LI-09-009-003", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal N3 OBS-01 \u2014 CLOSED: Line DA-SSD-DN80-09-005 (1st Stage RO Reject) "
        "design pressure increased from 70\u00a0bar to 80\u00a0bar. Operating pressure "
        "68\u00a0bar, design pressure 80\u00a0bar: margin 17.6\u00a0%. Consolidated Comment "
        "Sheet confirms: \u201cBW has revised accordingly.\u201d Observation closed."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "CIP system lines are included in Rev\u00a0B, consistent with the CIP system scope. "
        "All high-pressure lines use Super Duplex Steel material with wall thicknesses consistent "
        "with the Technical Specification \u2014 High Pressure Piping requirements. "
        "Low-pressure lines are PVC Schedule 80."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 Unassigned line identifier (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "One line entry \u2014 \u201cMAKE-UP FOR CIP\u201d (PVC Schedule 80, DN80, 7.62\u00a0mm "
        "wall, P&ID Sheet P9) \u2014 has no LINE NO. assigned. All other lines carry a unique "
        "identifier. Assign a line number consistent with the project numbering convention "
        "prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-02 \u2014 Schedule designation for Super Duplex Steel lines (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "All Super Duplex Steel lines are designated \u201cSUPER DUPLEX STEEL, SCH80\u201d "
        "without the \u201cS\u201d suffix. Per ASME B36.19M, pipe schedules for duplex and "
        "stainless steel should be designated \u201cSchedule 80S\u201d to distinguish from "
        "carbon steel Schedule 80. The wall thicknesses listed are consistent with "
        "Schedule\u00a080S values (DN100: 8.56\u00a0mm; DN80: 7.62\u00a0mm; DN65: 6.02\u00a0mm), "
        "confirming the intended specification. Correct the piping class designation to "
        "\u201cSCH\u00a080S\u201d prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    # ===== 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "The following observations from Transmittals N10 and N11 remain open. No documents "
        "addressing these items have been received to date. ADASA requests BW Water to confirm "
        "expected submission dates for I/O List Rev\u00a0C, Data Transfer List Rev\u00a0B, and "
        "Valve List Rev\u00a0D, as these carry multiple Major open observations."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Obs", "Document", "Description", "Outstanding Since", "Status"),
            (
                "TM\u00a0N10\nOBS-01",
                "I/O List / Data Transfer List",
                "Motor temperature TAG inconsistency (TE vs TIT); TIT-09-003 service conflict "
                "(CIP Tank vs HP Pump Bearing)",
                "TM\u00a0N10\n(12-Mar-2026)",
                "OPEN \u2014 I/O List Rev C and Data Transfer List Rev B not received",
            ),
            (
                "TM\u00a0N10\nOBS-02",
                "Data Transfer List",
                "Conductivity scaling 0\u201320\u00a0mS/cm for brine lines CIT-09-001/004/005; "
                "expected 65\u2013133\u00a0mS/cm",
                "TM\u00a0N10\n(12-Mar-2026)",
                "OPEN \u2014 Data Transfer List Rev B not received",
            ),
            (
                "TM\u00a0N10\nOBS-03",
                "Data Transfer List",
                "VE-09-014 duplicated in DI Modbus block; LS-09-001 and LS-09-002 absent "
                "from Modbus map",
                "TM\u00a0N10\n(12-Mar-2026)",
                "OPEN \u2014 Data Transfer List Rev B not received",
            ),
            (
                "TM\u00a0N10\nOBS-04",
                "Control System Architecture",
                "UPS 8-hour autonomy not confirmed \u2014 no load list or battery calculation "
                "provided",
                "TM\u00a0N10\n(12-Mar-2026)",
                "OPEN \u2014 Confirmation not received",
            ),
            (
                "TM\u00a0N10\nOBS-05",
                "GA Antiscalant Dosing Tank",
                "Effective working volume, body material, and seismic anchor data "
                "(NCh\u00a02369 Zone\u00a03) absent",
                "TM\u00a0N10\n(12-Mar-2026)",
                "OPEN \u2014 GA Rev B not received",
            ),
            (
                "TM\u00a0N10\nNOTE-05",
                "HMI Screenshots\nP22-BREAD-09-008-001",
                "HMI display screenshots committed at Transmittal N4 \u2014 not yet submitted",
                "TM\u00a0N4",
                "OPEN \u2014 Document not received",
            ),
            (
                "TM\u00a0N11\nOBS-01",
                "Valve List Rev C",
                "Duplicate TAG VE-09-007 \u2014 Items 44 and 64",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 Valve List Rev D not received",
            ),
            (
                "TM\u00a0N11\nOBS-02",
                "Valve List Rev C",
                "Duplicate TAG PSV-09-002 \u2014 Items 105 and 112",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 Valve List Rev D not received",
            ),
            (
                "TM\u00a0N11\nOBS-03",
                "Grounding Layout Rev B",
                "Equipment positions derived from Piping Layout Rev A, rejected in "
                "Transmittal N7",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending acceptance of Equipment Layout Rev B",
            ),
            (
                "TM\u00a0N11\nOBS-04",
                "Instrument Location Layout Rev B",
                "Same basis as OBS-03",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending acceptance of Equipment Layout Rev B",
            ),
        ],
    )

    # ===== 4. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph(
        "The following BW Water documents were reviewed and annotated by ADASA:"
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("#", "Document Code", "Title", "Rev", "Annotations"),
            (
                "A",
                "P22-LI-09-008-014",
                "Datasheet of Vibration Transmitter",
                "A",
                "OBS-01, NOTE-01",
            ),
            (
                "B",
                "P22-LI-09-009-003",
                "Line List",
                "B",
                "NOTE-01, NOTE-02",
            ),
        ],
    )

    # ===== 5. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            (
                "P22-LI-09-008-014",
                "Datasheet of Vibration Transmitter",
                "A",
                "3 \u2014 To be Revised",
            ),
            (
                "P22-LI-09-009-003",
                "Line List",
                "B",
                "2 \u2014 Approved as Noted",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Datasheet of Vibration Transmitter Rev\u00a0B is required to address OBS-01 (HART "
        "protocol documentation) and NOTE-01 (quantity confirmation). Line List Rev\u00a0B is "
        "accepted; NOTE-01 (missing line number) and NOTE-02 (SCH\u00a080S notation) are to be "
        "incorporated prior to IFC (Rev\u00a00), with no further review cycle required."
    )
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
