#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N13 ADASA-BW_WATER
Entregas E24 (25007-0024) + E25 (25007-0025)
Fecha: 06-Apr-2026

Veredicto global: 2 - APPROVED AS NOTED

Documentos:
  - P22-DWG-09-009-002 Rev C   P&ID                         -> 2 - Approved as Noted
  - P22-DWG-09-007-005 Rev B   Power Works Inst. Details     -> 2 - Approved as Noted

Observaciones cerradas por E24 (P&ID Rev C):
  - TM N9 NOTE-01: Title block codigo P22-DWG-09-009-002 corregido
  - TM N9 NOTE-02: TK-09-002 volumen 0.34 m3 (TOTAL) corregido
  - TM N10 OBS-05: PARTIALLY ADDRESSED -- P&ID ahora muestra 0.34 m3 para TK-09-002

Observaciones nuevas E24:
  - NOTE-01 (MINOR): TK-09-001 (CIP Tank) = 6.81 m3 vs 6.1 m3 en Equipment List Rev B

Observaciones cerradas por E25 (Power Works Rev B):
  - TM N8 OBS-01: Grounding/earthing specs ahora presentes (pagina 9, 7 metodos)
  - TM N8 OBS-02: Estandar de instalacion citado (NEMA VE-2, NEC 392.30(B), NEC 352)

Observaciones nuevas E25:
  - NOTE-01 (MINOR): Sizing basis de conductores de tierra no citada (NEC 250.122)
  - NOTE-02 (INFO): Cable Tray Layout drawings no recibidos
  - NOTE-03 (INFO): Interface banco de ducto ADASA -> tablero principal

Observaciones previas aun abiertas:
  - TM N10: OBS-01 a OBS-05, NOTE-05 (6 items)
  - TM N11: OBS-01 a OBS-04 (4 items)
  - TM N12: OBS-01, NOTE-01, NOTE-02 (3 items)
  Total heredadas: 13 items
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
    output_file = "TRANSMITTAL N13 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N13 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-013-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    doc = Document(output_file)

    # Limpiar contenido de ejemplo del template
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
    para.add_run("TRANSMITTAL VERDICT: 2 \u2014 APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Delivery\u00a024 (25007-0024, received March\u00a031, 2026) submits the Piping and "
        "Instrumentation Diagram Revision\u00a0C. Both open notes from Transmittal\u00a0N9 are "
        "confirmed closed. One informational note is raised on the CIP Tank capacity annotation."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Key findings:").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\u2022  ")
    run = para.add_run("Piping and Instrumentation Diagram Rev\u00a0C (Code\u00a02 \u2014 Approved as Noted):")
    run.bold = True
    para.add_run(
        " Delivery\u00a024 (25007-0024, received March\u00a031, 2026). "
        "Transmittal\u00a0N9 NOTE-01 (title block code) and NOTE-02 (antiscalant tank "
        "volume) are confirmed closed in Rev\u00a0C, as documented in the Consolidated "
        "Comment Sheet. One notation note is raised regarding a discrepancy between the "
        "CIP Tank (TK-09-001) capacity annotated in Rev\u00a0C (6.81\u00a0m\u00b3) and the "
        "value established in the accepted Equipment List Rev\u00a0B (6.1\u00a0m\u00b3). "
        "Clarification is requested prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("\u2022  ")
    run = para.add_run(
        "Typical Installation Details of Power Works Rev\u00a0B (Code\u00a02 \u2014 Approved as Noted):"
    )
    run.bold = True
    para.add_run(
        " Delivery\u00a025 (25007-0025, received April\u00a06, 2026). "
        "Both observations from Transmittal\u00a0N8 are closed: OBS-01 (grounding/earthing "
        "specifications) is addressed by the new grounding detail page covering seven "
        "installation methods; OBS-02 (installation standard) is addressed by citation of "
        "NEMA\u00a0VE-2, NEC Article\u00a0392.30(B), and NEC Article\u00a0352 throughout. "
        "Three informational notes are raised: grounding conductor sizing basis not cited, "
        "Cable Tray Layout drawings not yet submitted, and ADASA duct bank interface data "
        "required."
    )
    aplicar_arial_12(para)

    # ===== 2. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 2.1 P&ID Rev C ---
    doc.add_heading(
        "Piping and Instrumentation Diagram Rev\u00a0C \u2014 P22-DWG-09-009-002",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Consolidated Comment Sheet (CCS) included in Rev\u00a0C addresses both notes "
        "from Transmittal\u00a0N9:"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N9 NOTE-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "The document code in the title block has been corrected to P22-DWG-09-009-002 "
        "(three-digit correlativo). BW Water response in CCS: \u201cBW has revised accordingly.\u201d"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N9 NOTE-02 \u2014 CLOSED: ").bold = True
    para.add_run(
        "TK-09-002 (Antiscalant Dosing Tank) is now annotated as VOL: 0.34\u00a0m\u00b3 "
        "(TOTAL), consistent with the total installed capacity of the accepted datasheet "
        "(P22-ET-09-009-010 Rev\u00a0B). BW Water response in CCS: \u201cBW has revised accordingly.\u201d"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The P&ID continues to show all principal process equipment correctly identified "
        "and tagged: HP Feed Pump (BH-09-001), Feed Turbocharger (SIP-09-001), Interstage "
        "Turbocharger (SIP-09-002), 1st and 2nd Stage RO Racks (BOI-09-001\u00a0/\u00a0002), "
        "Static Mixer (MZE-09-001), Cartridge Filters (FIL-09-001\u00a0/\u00a0002), CIP Tank "
        "(TK-09-001), and Antiscalant Dosing Skid (BDS-09-001\u00a0/\u00a0002). High-pressure "
        "lines are shown in Super Duplex Stainless Steel consistent with previous reviews."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 CIP Tank capacity annotation inconsistency (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Rev\u00a0C annotates TK-09-001 (CIP Tank) with a capacity of 6.81\u00a0m\u00b3. "
        "The accepted Equipment List Rev\u00a0B (P22-LI-09-005-001, Delivery\u00a019) specifies "
        "the CIP Tank (Dayamas DYM\u00a06800, HDPE, 1800\u00a0mm diameter \u00d7 2950\u00a0mm "
        "height) with a working volume of 6.1\u00a0m\u00b3, consistent with the Process "
        "Calculation Rev\u00a0B selected volume. Revision\u00a0B of this P&ID showed 6.1\u00a0m\u00b3."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The 0.71\u00a0m\u00b3 increase between Rev\u00a0B and Rev\u00a0C has no supporting "
        "documentation in any submittal received to date. Confirm the correct installed "
        "capacity of TK-09-001 and update the P&ID annotation consistent with the Equipment "
        "List prior to IFC (Rev\u00a00). If the CIP Tank specification was revised, submit an "
        "updated Equipment List Rev\u00a0C with justification."
    )
    aplicar_arial_12(para)

    # ===== 2.2 POWER WORKS REV B =====
    doc.add_heading(
        "Typical Installation Details of Power Works Rev\u00a0B \u2014 P22-DWG-09-007-005",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev\u00a0B was submitted in response to Transmittal\u00a0N8, which issued "
        "Code\u00a03 \u2014 To Be Revised on Rev\u00a0A for two observations. Both are "
        "addressed in Rev\u00a0B."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Rev\u00a0B adds a dedicated grounding page (Page\u00a09: Grounding Link \u2014 "
        "Electrical Installation Details) specifying seven grounding methods: cable tray "
        "bonding via copper earth link bar, Cu/PVC green wire, and Cu tinned flexible "
        "braided conductor (all bonded to container structure); skid structure grounding; "
        "motor grounding via two methods (cable tray bonding to motor frame or motor "
        "terminal box ground terminal); panel grounding; and analog instrument cable shield "
        "termination to a grounded terminal block. Conductor sizes are specified: "
        "16\u00a0mm\u00b2 for main bonding conductors, 4\u00a0mm\u00b2 for instrument "
        "grounding wires."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Rev\u00a0B cites applicable installation standards throughout all pages: "
        "NEMA\u00a0VE-2 (cable tray installation and bonding), NEC Article\u00a0392.30(B) "
        "(cable tray support spacing), and NEC Article\u00a0352 (conduit installation)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 Grounding conductor sizing basis not cited (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Rev\u00a0B specifies bonding and grounding conductor sizes (16\u00a0mm\u00b2 for "
        "main conductors, 4\u00a0mm\u00b2 for instrument grounds) but does not cite the "
        "NEC table or design calculation used to establish these values. BW Water should "
        "confirm the sizing basis \u2014 for example, NEC\u00a0250.122 for equipment "
        "grounding conductor sizing \u2014 in the next revision of this drawing or in a "
        "supporting design calculation. No further review cycle is required for this "
        "document on this point; sizing basis may be incorporated in IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-02 \u2014 Cable Tray Layout drawings not yet submitted (INFORMATIONAL)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The installation details in Rev\u00a0B define standard assembly configurations "
        "for cable trays, conduits, and grounding connections. The complete internal cable "
        "routing from the main panel (LCP/MCC) to each load endpoint \u2014 including "
        "BH-09-001 (HP Pump motor), BH-09-002 (CIP Pump motor), antiscalant dosing pump, "
        "CIP heater, and instrumentation panels \u2014 has not been submitted. This routing "
        "information falls within the scope of the Cable Tray Layout drawing(s), which are "
        "a distinct deliverable and have not been received. BW Water must submit the Cable "
        "Tray Layout drawing(s) showing the complete routing path and cable segregation "
        "(power\u00a0/\u00a0control\u00a0/\u00a0analog) throughout the module prior to "
        "IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Basis: ET \u2014 Electrical and Control Systems; ET \u2014 Scope of Supply "
        "(all internal wiring, interconnection of equipment, and internal conduit/cable "
        "tray routing is provider scope)."
    )
    run = para.runs[0]
    run.italic = True
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-03 \u2014 ADASA incoming power connection via duct bank (INFORMATIONAL)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "ADASA confirms that the incoming power supply from the ADASA electrical room to "
        "the BW Water main panel will be routed via underground duct bank. To allow ADASA "
        "to finalize the duct bank civil design, BW Water must confirm: (a)\u00a0the number "
        "and diameter of incoming conduits required at the main panel entry point; "
        "(b)\u00a0the terminal block or busbar arrangement for incoming power conductors; "
        "(c)\u00a0the conductor count and cross-section per circuit (main feeder, control "
        "power supply, UPS input). This information must be included in the next revision "
        "of this drawing or submitted as a dedicated Interface Document prior to "
        "commencement of duct bank civil works."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Basis: ET \u2014 Electrical Supply Limit (incoming connection to panel terminals "
        "= ADASA scope; BW Water scope begins at panel incoming terminals)."
    )
    run = para.runs[0]
    run.italic = True
    aplicar_arial_12(para)

    # ===== 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "The following observations from Transmittals N10, N11, and N12 remain open. "
        "No documents addressing these items have been received since Transmittal\u00a0N12 "
        "(issued March\u00a030, 2026)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Status update for TM\u00a0N10 OBS-05: ").bold = True
    para.add_run(
        "P&ID Rev\u00a0C confirms TK-09-002\u00a0=\u00a00.34\u00a0m\u00b3 total volume, "
        "partially addressing this observation. GA Antiscalant Tank Rev\u00a0B is still "
        "required for seismic anchor data and body material confirmation."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "ADASA requests BW Water to confirm expected submission dates for I/O List Rev\u00a0C, "
        "Data Transfer List Rev\u00a0B, and Valve List Rev\u00a0D, as these carry multiple "
        "Major open observations outstanding for more than 18\u00a0days."
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
                "PARTIALLY ADDRESSED \u2014 P&ID Rev\u00a0C shows TK-09-002 as "
                "0.34\u00a0m\u00b3 total. GA Rev\u00a0B still required for remaining items",
            ),
            (
                "TM\u00a0N10\nNOTE-05",
                "HMI Screenshots\nP22-BREAD-09-008-001",
                "HMI display screenshots committed at Transmittal\u00a0N4 \u2014 not yet submitted",
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
                "Grounding Point and Power Panel Location Layout Rev\u00a0B",
                "Equipment positions derived from Piping Layout Rev\u00a0A, rejected in "
                "Transmittal\u00a0N7",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending acceptance of Equipment Layout Rev\u00a0B",
            ),
            (
                "TM\u00a0N11\nOBS-04",
                "Instrument Location Layout Rev\u00a0B",
                "Same basis as OBS-03",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending acceptance of Equipment Layout Rev\u00a0B",
            ),
            (
                "TM\u00a0N12\nOBS-01",
                "Datasheet of Vibration Transmitter Rev\u00a0A",
                "HART protocol not specified for IFM VTV122 \u2014 Technical Specification "
                "\u2014 Instrumentation requires 4\u201320\u00a0mA + HART for all field instruments",
                "TM\u00a0N12\n(30-Mar-2026)",
                "OPEN \u2014 Datasheet Rev B not received",
            ),
            (
                "TM\u00a0N12\nNOTE-01",
                "Datasheet of Vibration Transmitter Rev\u00a0A",
                "Quantity field reads 1 for three TAGs (VT-09-001\u00a0/\u00a0002\u00a0/\u00a0003)",
                "TM\u00a0N12\n(30-Mar-2026)",
                "OPEN \u2014 Datasheet Rev B not received",
            ),
            (
                "TM\u00a0N12\nNOTE-02",
                "Line List Rev\u00a0B",
                "Super Duplex Steel lines designated SCH80 without S suffix; "
                "correct designation is SCH\u00a080S per ASME B36.19M",
                "TM\u00a0N12\n(30-Mar-2026)",
                "OPEN \u2014 to be incorporated in IFC (Rev\u00a00)",
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
                "P22-DWG-09-009-002",
                "Piping and Instrumentation Diagram",
                "C",
                "NOTE-01",
            ),
            (
                "B",
                "P22-DWG-09-007-005",
                "Typical Installation Details of Power Works",
                "B",
                "NOTE-01, NOTE-02, NOTE-03",
            ),
        ],
    )

    # ===== 5. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Submittal No.", "Document Code", "Title", "Rev", "Response Code"),
            (
                "25007-0024",
                "P22-DWG-09-009-002",
                "Piping and Instrumentation Diagram",
                "C",
                "2 \u2014 Approved as Noted",
            ),
            (
                "25007-0025",
                "P22-DWG-09-007-005",
                "Typical Installation Details of Power Works",
                "B",
                "2 \u2014 Approved as Noted",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 2 \u2014 APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Both documents are accepted. The P&ID Rev\u00a0C NOTE-01 (CIP Tank capacity "
        "annotation) and the Power Works Rev\u00a0B NOTE-01 (grounding sizing basis) are "
        "to be resolved prior to IFC (Rev\u00a00). NOTE-02 (Cable Tray Layout) and "
        "NOTE-03 (duct bank interface data) require dedicated submittals from BW Water "
        "prior to IFC."
    )
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
