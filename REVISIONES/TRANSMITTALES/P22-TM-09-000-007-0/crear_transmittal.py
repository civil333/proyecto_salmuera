#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N7 ADASA-BW_WATER
Entrega 14 (Submittal 25007-0014) - 4 documentos
Fecha: 08-Mar-2026

Veredicto: 3 - TO BE REVISED
Documentos:
  - P22-CD-09-005-002 A/C Thermal Calculation Rev B → 3 - To be Revised
  - P22-DWG-09-005-004 Piping Layout Rev A          → 3 - To be Revised
  - P22-DWG-09-005-005 Tie-In Point Rev A           → 3 - To be Revised
  - P22-BT-09-009-001 Control Philosophy Rev A      → 3 - To be Revised
"""

import sys
import os

# Agregar la ruta del skill template-adasa
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    "..",
    ".claude",
    "skills",
    "template-adasa",
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
    """Genera el Transmittal N7 en formato ADASA"""

    output_file = "TRANSMITTAL N7 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N7 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-007-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    # Abrir documento y agregar contenido
    doc = Document(output_file)

    # Limpiar contenido de ejemplo generado por template ADASA
    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(
            x in texto
            for x in [
                "RESUMEN EJECUTIVO",
                "INTRODUCCION",
                "INTRODUCCIÓN",
                "1. INTRO",
                "ESTE DOCUMENTO HA SIDO GENERADO",
                "AGREGUE AQUI EL CONTENIDO",
                "AGREGUE AQUÍ EL CONTENIDO",
            ]
        ):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== 1. EXECUTIVE SUMMARY =====
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 3 — TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water Delivery 14 (Submittal 25007-0014) contains four documents: the "
        "A/C Thermal Calculation, two mechanical layout drawings, and the first "
        "Control Philosophy submission. All four require revision."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy specifies 30-minute UPS autonomy. The Technical "
        "Specification \u2014 Control and Automation System \u2014 requires a "
        "minimum 8 hours after a power interruption. This is a direct contractual "
        "non-conformance that must be corrected in Rev B."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The A/C Thermal Calculation omits control panel, instrumentation, and "
        "dosing equipment from the thermal load. The n+1 configuration confirmed "
        "physically in the Piping Layout is not stated in the calculation document."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Piping Layout shows CIP and antiscalant dosing at opposite ends of the "
        "module, separated by 11,150 mm. Transmittal N5 OBS-01 required consolidation "
        "within a single 3.5-meter external footprint. The Tie-In Point document is "
        "drawn over this non-conforming layout and must be redrawn after the Piping "
        "Layout is corrected. Additionally, the Piping Layout shows a single hinged "
        "personnel door on the lateral face; the required lateral sliding door and the "
        "equipment access door (sized for the largest installed item, 110\u00b0 outward "
        "opening) are absent \u2014 two distinct ET \u00a75.1.10 requirements not addressed. "
        "Two prior items related to this delivery remain open: "
        "Modbus TCP Memory Map (65 days, TM N2) and IO List update (44 days, TM N3)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy contains no description of energy consumption metering "
        "(CEE/MVE). The Specific Energy Consumption is a contractual performance "
        "guarantee under ET \u00a710.1.3 and the basis for commissioning acceptance \u2014 "
        "it cannot be verified without the instrument described in this document."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy declares 4-20mA as the sole field communication "
        "protocol. Control Architecture Rev B (P22-CD-09-004-001) includes an "
        "Ethernet/IP gateway (PLX32-EIP-MBTCP) and Ethernet/IP field cabling that "
        "are not acknowledged in the Philosophy. HART protocol, required by "
        "ET \u2014 Instrumentation Specification for all field transmitters, is "
        "also absent."
    )
    aplicar_arial_12(para)

    # ===== 2. GENERAL INFORMATION =====
    doc.add_heading("GENERAL INFORMATION", level=1)

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Submittal", "25007-0014"),
            ("Delivery date", "06-Mar-2026"),
            ("Review completion", "08-Mar-2026"),
            ("Total documents reviewed", "4"),
            ("Response code summary", "4\u00d7 Code 3 (To be Revised), 0\u00d7 Code 2"),
            ("Contract", "C-4300 BW WATER SUPPLY-12803 V2"),
        ],
    )

    # ===== 3. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 3.1 A/C Thermal Calculation ---
    doc.add_heading("3.1 A/C Thermal Calculation Rev B \u2014 P22-CD-09-005-002", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B adds VFD losses (absent in Rev A) and confirms the recommended "
        "unit size at 2.5 HP. Two issues prevent acceptance."
    )
    aplicar_arial_12(para)

    doc.add_heading("Observation 1 \u2014 Incomplete thermal load inventory", level=3)
    para = doc.add_paragraph()
    para.add_run(
        "The calculation covers HP pump motor losses (4.26 kW) and VFD losses "
        "(1.70 kW) only. Control panel/PLC, instrumentation, antiscalant dosing "
        "equipment, and lighting are excluded without basis. Rev C must itemize "
        "all heat-generating equipment inside the container."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "Technical Offer Rev1 \u2014 A/C System, Sizing Methodology; "
        "ET \u2014 Air Conditioning System"
    )
    aplicar_arial_12(para)

    doc.add_heading("Observation 2 \u2014 n+1 configuration not established in the calculation", level=3)
    para = doc.add_paragraph()
    para.add_run(
        "The calculation recommends \u201ca 2.5 HP air-conditioning unit.\u201d "
        "The Piping Layout shows two external A/C units. The calculation must explicitly "
        "state that the two-unit configuration is n+1 and that each 2.5 HP unit "
        "independently covers 100% of the verified load."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Air Conditioning System (n+1 requirement)")
    aplicar_arial_12(para)

    doc.add_heading("Required actions:", level=3)
    actions_ac = [
        "Provide a complete thermal load table that includes all heat-generating "
        "equipment inside the container: HP pump motor, VFD, local control panel/PLC, "
        "instruments and analyzers, lighting, and any other electrical equipment.",
        "Explicitly state the n+1 configuration: two units, each rated \u22652.5 HP, "
        "each capable of independently handling 100% of the total verified thermal load.",
    ]
    for i, action in enumerate(actions_ac, 1):
        para = doc.add_paragraph(f"{i}. {action}")
        aplicar_arial_12(para)

    # --- 3.2 Piping Layout ---
    doc.add_heading("3.2 Piping Layout Rev A \u2014 P22-DWG-09-005-004", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Two major non-conformances prevent acceptance.")
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 CIP and dosing equipment not consolidated in a single external footprint (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "Transmittal N5 (OBS-01) established as a condition for acceptance that all "
        "CIP and dosing equipment \u2014 CIP tank, CIP pump, CIP cartridge filter, "
        "and antiscalant injection unit \u2014 must be arranged within a single external "
        "footprint with a maximum length of 3.5 meters, aligned to the side of the "
        "module indicated in ADASA\u2019s review markup."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Piping Layout Rev A does not meet this requirement. The CIP system "
        "(TK-09-001, BH-09-002, REL-09-001, FIL-09-002) is shown in Section 2-2 "
        "at one end of the module. The antiscalant dosing system "
        "(TK-09-002, BDS-09-001/002) is shown in Section 3-3 at the opposite end. "
        "The separation between the two sections corresponds to the full module length "
        "of 11,150 mm, which exceeds the 3.5-meter consolidated footprint limit "
        "by a factor of more than three."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Required action: Piping Layout Rev B must consolidate all external CIP and "
        "dosing equipment (CIP tank, CIP pump, CIP cartridge filter, antiscalant "
        "dosing tank, antiscalant dosing pump skid) within a single external sector, "
        "with footprint not exceeding container width \u00d7 3.5 m, aligned to the "
        "side of the module specified in ADASA\u2019s Transmittal N5 markup."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("Transmittal N5 Rev 1 \u2014 OBS-01 (CIP and Anti-Scalant Dosing External Footprint)")
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 3 \u2014 Container lateral access: sliding door not shown; equipment access door absent (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The lateral view of the container shows a single hinged door at 900\u00a0mm \u00d7 2,200\u00a0mm \u2014 "
        "adequate only for personnel access. Two additional door requirements from ET \u00a75.1.10 "
        "are not addressed in the current revision."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("(a) Equipment access door missing. ").bold = True
    para.add_run(
        "ET \u00a75.1.10 requires a dedicated door with dimensions sufficient to allow entry and removal "
        "of the largest equipment installed inside the container. This door must open at a minimum "
        "angle of 110\u00b0 toward the exterior. No such door appears in the Piping Layout."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("(b) Lateral sliding door not shown. ").bold = True
    para.add_run(
        "ET \u00a75.1.10 states that the container must guarantee lateral access by means of a sliding door. "
        "The door shown in the lateral view is a conventional hinged door, not a sliding door. "
        "This is a distinct requirement from the personnel, equipment, and emergency doors."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Required action: ").bold = True
    para.add_run(
        "Piping Layout Rev B must show all four required door types \u2014 personnel (900\u00d72,200\u00a0mm), "
        "equipment (dimensioned to largest installed item, 110\u00b0 outward opening), emergency, and "
        "lateral sliding \u2014 with their respective positions on the container perimeter."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Container (ET \u00a75.1.10) \u2014 Access doors and lateral sliding door requirement")
    aplicar_arial_12(para)

    notes_piping = [
        (
            "High-pressure lines in SSD material",
            "Process lines at elevated pressure (DA-SSD-DN100-09-003, "
            "DA-SSD-DN100-09-004/006) are in stainless steel duplex, consistent "
            "with high-pressure service requirements.",
        ),
        (
            "Cross-reference with P&ID pending",
            "Detailed verification of valve tag positions and instrument locations "
            "requires cross-reference with the approved P&ID (P22-DWG-09-009-0002). "
            "This cross-reference should be confirmed when the P&ID is submitted "
            "in its next approved revision.",
        ),
        (
            "n+1 A/C configuration physically confirmed",
            "Two external A/C units are clearly shown in Sheet 4 (Section 3-3). "
            "Each unit is labeled EXT. AC. UNIT 1 and EXT. AC. UNIT 2.",
        ),
        (
            "Equipment Layout Rev B remains outstanding",
            "This Piping Layout does not replace the Equipment Layout "
            "(P22-DWG-09-005-003 Rev B) required in Transmittal N5 to show the "
            "dimensioned external CIP footprint. That document remains pending "
            "independently of this submittal.",
        ),
        (
            "Local Control Panel must be positioned adjacent to the container",
            "The Piping Layout shows the Local Control Panel (LCP) as a separate "
            "item external to the module. As established in Transmittal N5 OBS-01, "
            "the LCP must be positioned immediately adjacent to the container. "
            "BW Water must confirm that the electrical and control interconnection "
            "between the LCP and the container module is documented in the layout "
            "and that the LCP is included within the Factory Acceptance Test (FAT) scope.",
        ),
        (
            "Antiscalant and CIP connections at module boundary must be flanged for transport",
            "The antiscalant supply and injection connections (AS-PVC-DN25-09-031 "
            "and AS-PVC-DN15-09-035) shown in the Piping Layout are module boundary "
            "interfaces and are therefore tie-in points. As established in Transmittal N5, "
            "all process connections at the module boundary must be terminated with flanges "
            "to allow disconnection during transport and reconnection at site. BW Water must "
            "confirm flanged termination for all antiscalant and CIP make-up connections "
            "at the module boundary in Piping Layout Rev B.",
        ),
        (
            "Missing elevation view showing process connection positions",
            "No elevation or dedicated section (Section 4-4) is included to show the "
            "position of all process tie-in points (entries and exits) along the module "
            "perimeter. An elevation view identifying all process connections \u2014 "
            "including antiscalant, feed, permeate, concentrate, and CIP \u2014 with "
            "their relative positions is required for field installation planning. "
            "Piping Layout Rev B should include this view.",
        ),
    ]
    for i, (title, desc) in enumerate(notes_piping, 1):
        para = doc.add_paragraph()
        para.add_run(f"Note {i} \u2014 {title}: ").bold = True
        para.add_run(desc)
        aplicar_arial_12(para)

    # --- 3.3 Tie-In Point ---
    doc.add_heading("3.3 Tie-In Point Layout Rev A \u2014 P22-DWG-09-005-005", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "This document cannot be accepted in its current revision. Its content is "
        "directly dependent on the Piping Layout Rev A, which does not conform to "
        "the layout requirement established in Transmittal N5 OBS-01."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("N\u00b0", "Tag", "Fluid", "DN", "Rating", "Standard"),
            ("1", "N/A", "ANTISCALANT", "DN15", "\u2014", "\u2014"),
            ("2", "TP-AS P11-001", "ANTISCALANT", "DN25", "ANSI 150#", "ASME B16.5"),
            ("3", "TP-DA P8-001", "FEED", "DN100", "ANSI 150#", "ASME B16.5"),
            ("4", "TP-PE P9-001", "PERMEATE", "DN80", "ANSI 150#", "ASME B16.5"),
            ("5", "TP-PE P9-002", "CONCENTRATE", "DN80", "ANSI 150#", "ASME B16.5"),
            ("6", "TP-DA P9-003", "CONCENTRATE", "DN65", "ANSI 150#", "ASME B16.5"),
        ],
    )

    doc.add_heading(
        "Observation 1 \u2014 Tie-In Point has a direct dependency on the non-conforming Piping Layout (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The antiscalant tie-in points (N\u00b01 and N\u00b02) reflect the position "
        "of the dosing system in the non-conforming Piping Layout Rev A. Once the "
        "Piping Layout consolidates CIP and antiscalant dosing within a single "
        "footprint, these tie-in positions will change. Tie-In Point Rev B must be "
        "redrawn over the corrected Piping Layout Rev B."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Required action: ").bold = True
    para.add_run(
        "Submit Tie-In Point Rev B after Piping Layout Rev B is accepted. Rev B must "
        "reflect the consolidated layout and provide complete data for all tie-in points."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 2 \u2014 Make-up water connection for external CIP not shown (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Piping Layout shows a Make-up CIP line (CP-PVC-DN80-09-019) with no "
        "corresponding battery-limit tie-in. BW Water must confirm whether CIP "
        "make-up water is supplied from an external source or from the module\u2019s "
        "own permeate stream."
    )
    aplicar_arial_12(para)

    notes_tiein = [
        (
            "Tie-in N\u00b01 incomplete",
            "The DN15 antiscalant connection has no tag, no P&ID reference, and "
            "no flange standard. These fields must be completed in the next revision.",
        ),
        (
            "Design pressure at brine feed tie-in",
            "Tie-in N\u00b03 (TP-DA P8-001, Feed DN100, ANSI 150#) requires confirmation "
            "that the SWRO brine arrives at the module battery limit at a pressure "
            "compatible with ANSI 150# rating (\u226419.6 bar at operating temperature). "
            "BW Water should state the design pressure at this interface.",
        ),
        (
            "BW Water internal line identifiers",
            "Line references P8-001, P9-001, P9-002, P9-003, and P11-001 appear to be "
            "BW Water internal identifiers. Cross-reference against ADASA P&ID line "
            "numbering is required for traceability.",
        ),
        (
            "Missing elevation view with flange positions and elevations",
            "The Tie-In Point Layout provides a plan view only. No elevation view is "
            "included to indicate the height, elevation, and exact position of each "
            "connection flange. This information is required for the civil/structural "
            "interface at the battery limit. Tie-In Point Rev B must include an "
            "elevation view showing the position, elevation, and height of all "
            "connection flanges listed in the tie-in table.",
        ),
    ]
    for i, (title, desc) in enumerate(notes_tiein, 1):
        para = doc.add_paragraph()
        para.add_run(f"Note {i} \u2014 {title}: ").bold = True
        para.add_run(desc)
        aplicar_arial_12(para)

    # --- 3.4 Control Philosophy ---
    doc.add_heading("3.4 Control Philosophy Rev A \u2014 P22-BT-09-009-001", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "First submission of the Control Philosophy for the Second Stage RO Module. "
        "Twelve issues require revision before acceptance. Three trace directly to "
        "the IO List review in Transmittal N3, pending 44 days without a revised "
        "IO List being submitted."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 UPS autonomy: 30 minutes specified vs. 8 hours required (CRITICAL)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The document states: \u201cThe UPS will provide 30 minutes of power to ensure "
        "the controls and instrumentation do not shutdown.\u201d "
        "The Technical Specification \u2014 Control and Automation System \u2014 "
        "requires a minimum 8 hours of UPS autonomy after a grid power interruption. "
        "The 30-minute figure is a 16-fold shortfall against this contractual "
        "requirement. BW Water must confirm an 8-hour UPS in Rev B and provide "
        "the supporting capacity calculation."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Control and Automation System (UPS minimum 8-hour autonomy requirement)")
    aplicar_arial_12(para)

    doc.add_heading("Observation 2 \u2014 Instrument tag discrepancy (VE-07-014 vs. VE-09-014)", level=3)
    para = doc.add_paragraph()
    para.add_run(
        "The Feed Preparation System Instruments table lists the antiscalant tank "
        "inlet motorized valve as VE-07-014 and the antiscalant pump downstream valve "
        "as VE-07-016. The Feed Preparation System Process Description references the "
        "same valves as VE-09-014 and VE-09-016. Area codes 07 and 09 represent "
        "distinct project areas and cannot both be correct for the same equipment. "
        "This must be resolved consistently with the Valve List and the P&ID."
    )
    aplicar_arial_12(para)

    doc.add_heading("Observation 3 \u2014 Modbus TCP/IP interface not addressed", level=3)
    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy contains no reference to the Modbus TCP/IP interface "
        "required for integration with the plant SCADA system. The Technical "
        "Specification \u2014 Communication and Control System (Modbus TCP/IP) \u2014 "
        "requires a complete memory map defining all variables to be exchanged between "
        "the module PLC and the plant SCADA. As a minimum, the revised Control "
        "Philosophy should include a section describing the Modbus TCP/IP "
        "communication architecture and confirming the list of variables to be mapped. "
        "The detailed memory map has been outstanding since Transmittal N2 (65 days)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Communication and Control System (Modbus TCP/IP)")
    aplicar_arial_12(para)

    doc.add_heading("Observation 4 \u2014 \u201cBT\u201d document type code not defined", level=3)
    para = doc.add_paragraph()
    para.add_run(
        "The document code P22-BT-09-009-001 uses the type code \u201cBT,\u201d "
        "which is not defined in the project document coding standard "
        "(P22-TT-AA-DDD-NNN-R). BW Water should either assign a standard type code "
        "or formally define \u201cBT\u201d in the project document register."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 5 \u2014 Motor temperature monitoring not described (CRITICAL)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "No continuous motor temperature monitoring is described for the HP Pump "
        "or CIP Pump motors. The only temperature signals referenced are CIP fluid "
        "measurements \u2014 process-side, not motor protection inputs. The signals "
        "TE09-001-XB001 and TE09-002-XB001 are temperature switches (DI), not "
        "Pt-100 transmitters (AI). ET \u00a75.3 requires Pt-100 sensors in the "
        "windings and bearings of all motors. Rev B must describe the AI motor "
        "temperature inputs, their alarm setpoints, and their role in motor "
        "protection logic."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Motors and Electrical Equipment (Pt-100 in windings and bearings, "
        "all motors); Transmittal N3 OBS-01 \u2014 IO List Rev A received in "
        "BW Water Delivery 8 (Submittal 25007-0008), pending 39 days"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 6 \u2014 DO Module Status output absent",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "No discrete output (DO) reporting the operational state of the module to "
        "external systems is defined. Transmittal N3 OBS-04 requested this signal "
        "(0 = module stopped; 1 = module in operation) \u2014 pending 39 days "
        "without incorporation. Rev B must describe this DO, its triggering "
        "conditions, and its inclusion in IO List Rev B."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "Transmittal N3 OBS-04 \u2014 IO List Rev A received in "
        "BW Water Delivery 8 (Submittal 25007-0008), pending 39 days; "
        "ET \u2014 Communication and Control System"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 7 \u2014 General module enable DI incomplete",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy describes two discrete inputs from the client as "
        "external permissives: permeate tank permissive and off-spec tank permissive. "
        "These are product-specific signals that condition tank filling \u2014 they "
        "are not a general module enable."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal N3 OBS-05 requested a dedicated DI for general module enable "
        "from the plant (logic: 1 = module may operate; 0 = module must stop), "
        "allowing the SWRO plant to inhibit module start-up or force a controlled "
        "shutdown independently of tank levels. This signal is absent from the "
        "Control Philosophy. Rev B must distinguish between the product permissives "
        "already described in the Control Philosophy (permeate tank permissive and "
        "off-spec tank permissive) and the operational enable of the module, "
        "and must incorporate the latter in the control logic and in the IO List Rev B."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "Transmittal N3 OBS-05 \u2014 IO List Rev A received in "
        "BW Water Delivery 8 (Submittal 25007-0008), pending 39 days"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Note \u2014 UPS scope confirmed: ").bold = True
    para.add_run(
        "Section 1.3 confirms that a UPS is included in the module scope, "
        "partially closing the pending item from Transmittal N4. The required "
        "correction is the capacity specification (8 hours, not 30 minutes)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Note \u2014 Companion documents not yet submitted: ").bold = True
    para.add_run(
        "The Control Philosophy explicitly references the Operating Sequence Chart "
        "and the Alarm and Control Setpoint List as \u201cSEPARATE DOCUMENT.\u201d "
        "BW Water should provide committed delivery dates for both."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 8 \u2014 HMI screen design standard not declared (ISA 101) (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The document establishes an internal color coding scheme for equipment states "
        "and measured values. The scheme is broadly consistent with conventional practice "
        "but is presented without reference to a normative standard. "
        "ET \u2014 Control and Automation System requires HMI screens to comply with "
        "ISA 101 as the design standard, a requirement reiterated in the FAT inspection "
        "protocol. Rev B must formally declare ISA 101 compliance and confirm that screen "
        "layout, alarm presentation, navigation hierarchy, and color conventions all "
        "conform to that standard."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Control and Automation System (HMI ISA 101 requirement)")
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 9 \u2014 Energy consumption metering absent: CEE indicator and MVE not described (CRITICAL)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy contains no reference to energy metering. "
        "ET \u2014 Control and Automation System requires an Electrical Variables Meter "
        "(MVE) \u2014 connected to the PLC and accessible from the HMI \u2014 that "
        "continuously displays voltage, current, and power, and from which the Specific "
        "Energy Consumption (CEE, in kWh/m\u00b3) is derived as total electrical "
        "consumption divided by net permeate volume produced. The CEE is a contractual "
        "performance guarantee (< 4.8 kWh/m\u00b3 for TDS 43,000\u201348,000 mg/l; "
        "< 5.0 kWh/m\u00b3 for TDS 48,000\u201353,000 mg/l per ET \u00a710.1.3) and "
        "the basis for acceptance of the Performance Test. Without this instrument, the "
        "performance guarantee cannot be verified during commissioning. Rev B must describe "
        "the MVE, its PLC integration, the CEE calculation, the HMI display screen, and "
        "any alarm setpoints associated with energy performance."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Control and Automation System (MVE and CEE display); "
        "ET \u2014 Performance Guarantees \u00a710.1.3 (CEE contractual limit)"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 10 \u2014 Communication protocol inconsistency: 4-20mA only vs. "
        "Ethernet/IP in Architecture; HART not declared (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run("Two protocol gaps require resolution:")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "(a) Ethernet/IP field network undeclared in Control Philosophy. "
    ).bold = True
    para.add_run(
        "Control Architecture Rev B (P22-CD-09-004-001) includes a PROSOFT "
        "PLX32-EIP-MBTCP gateway and Ethernet/IP cabling to field devices, indicating "
        "that at least some field devices communicate via Ethernet/IP rather than "
        "hardwired 4-20mA or discrete I/O. The Control Philosophy describes only "
        "4-20mA analog inputs and 24 VDC discrete I/O \u2014 no Ethernet/IP field "
        "network is mentioned. Rev B must include a complete signal philosophy table "
        "that identifies, for each device type, the physical communication medium "
        "(hardwired 4-20mA, 24 VDC DI/DO, or Ethernet/IP) and reconcile this with "
        "the Control Architecture drawing."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "(b) HART protocol not declared despite ET requirement. "
    ).bold = True
    para.add_run(
        "ET \u2014 Instrumentation Specification requires 4-20mA + HART for all field "
        "instrumentation. The Control Philosophy specifies 4-20mA only, with no "
        "reference to HART. BW Water must confirm that all analog transmitters are "
        "HART-capable and state how the HART channel is used (diagnostics only, or "
        "active device management via the PLC or a HART multiplexer)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Instrumentation Specification (4-20mA + HART protocol); "
        "Control Architecture Rev B \u2014 P22-CD-09-004-001 (Ethernet/IP gateway "
        "and field cabling)"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 11 \u2014 Client-side start permissive interface incorrectly defined (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "Control Philosophy \u2014 Client Interface Permissive defines two hardwired DI signals: "
        "\u201cPermissive to fill Permeate Tank\u201d and \u201cPermissive to fill Off-Spec Tank.\u201d "
        "These are product-routing signals that condition tank filling; they do not constitute "
        "a general module enable from the plant control system."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The correct interface between the ADASA plant and the BW Water module requires "
        "two dedicated signals: (1) one DI from ADASA to the BW Water PLC (general module "
        "enable: 1\u202f=\u202fmodule may operate; 0\u202f=\u202fmodule must stop), "
        "and (2) one DO from the BW Water PLC to ADASA (module status: 1\u202f=\u202fmodule "
        "in operation; 0\u202f=\u202fmodule stopped). Rev B must replace the two individual "
        "tank permissive DIs with this single general enable DI, and must "
        "describe the companion module status DO. IO List Rev B must assign both signals "
        "with IO tags, terminal references, and signal specifications (24\u202fVDC dry contact)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Communication and Control System; IO List Rev A"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 12 \u2014 HP pump start permissive incomplete \u2014 minimum feed pressure not defined (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Control Philosophy does not define a minimum feed pressure threshold as a "
        "mandatory start permissive for the HP pump. Without this condition, the PLC "
        "could start the pump with insufficient inlet pressure from the ADASA feed system, "
        "creating a cavitation risk that could damage the pump impeller and cause "
        "unplanned shutdown."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B must add minimum inlet pressure (PSL) as a mandatory start permissive "
        "condition for the HP pump: the pump may only start when the feed pressure measured "
        "at the module inlet exceeds the defined minimum threshold. The threshold value, "
        "the associated pressure instrument tag, and the permissive logic must be stated "
        "explicitly in the Control Philosophy."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 HP Pump (start permissive and cavitation protection); Process Design"
    )
    aplicar_arial_12(para)

    # ===== 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "The following items from prior transmittals remain unresolved and have "
        "direct bearing on the documents reviewed in this transmittal."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Item", "Origin", "Days Open", "Status", "Action Required"),
            (
                "Modbus TCP Memory Map",
                "TM N2",
                "65",
                "STILL PENDING",
                "Immediate delivery required. Integration planning is blocked.",
            ),
            (
                "IO List update \u2014 Ethernet IP and digital stop signals",
                "TM N3",
                "44",
                "STILL PENDING",
                "Include in next IO List revision.",
            ),
        ],
    )

    # ===== 5. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph(
        "The following BW Water documents were reviewed as part of this transmittal. "
        "ADASA-annotated copies are attached."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Attachment", "Document Code", "Title", "Rev"),
            ("1", "P22-CD-09-005-002", "A/C Thermal Calculation", "B"),
            ("2", "P22-DWG-09-005-004", "Piping Layout", "A"),
            ("3", "P22-DWG-09-005-005", "Tie-In Point Layout", "A"),
            ("4", "P22-BT-09-009-001", "Control Philosophy", "A"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Documents available for download at: ").bold = False
    para.add_run("http://gofile.me/7k8qL/RHWabtKCE")
    aplicar_arial_12(para)

    # ===== 6. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            ("P22-CD-09-005-002", "A/C Thermal Calculation", "B", "3 \u2014 To be Revised"),
            ("P22-DWG-09-005-004", "Piping Layout", "A", "3 \u2014 To be Revised"),
            ("P22-DWG-09-005-005", "Tie-In Point Layout", "A", "3 \u2014 To be Revised"),
            ("P22-BT-09-009-001", "Control Philosophy", "A", "3 \u2014 To be Revised"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
