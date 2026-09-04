#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N10 ADASA-BW_WATER
Entrega E18 (25007-0018): 6 documentos tecnicos
Fecha: 12-Mar-2026

Veredicto: 3 - TO BE REVISED

Documentos:
  - P22-LI-09-008-001 Rev B   IO List                     -> 2 - Approved as Noted
  - P22-LI-09-008-004 Rev A   Data Transfer List           -> 2 - Approved as Noted
  - P22-CD-09-004-001 Rev C   Control System Architecture  -> 2 - Approved as Noted
  - P22-DWG-09-005-015 Rev A  GA Antiscalant Dosing Tank   -> 2 - Approved as Noted
  - P22-DWG-09-005-012 Rev A  GA 1st Stage Turbo (SIP-09-001) -> 3 - To be Revised
  - P22-DWG-09-005-013 Rev A  GA 2nd Stage Turbo (SIP-09-002) -> 3 - To be Revised

Observaciones cerradas en esta entrega:
  - TM N7 OBS-03: Data Transfer List (Modbus TCP/IP) -- P22-LI-09-008-004 Rev A
  - TM N8 OBS-2:  IO List update (7 senales faltantes) -- P22-LI-09-008-001 Rev B
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
    output_file = "TRANSMITTAL N10 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N10 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-010-0",
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
        "Delivery 18 (25007-0018, received March 12, 2026) submits six documents: "
        "four approved as noted, two requiring revision. "
        "Seven observations are raised \u2014 six MAJOR, one MINOR. "
        "Required actions are detailed in Section 2."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Consolidated Comment Sheets (I/O List 7 items, Data Transfer List 3 items, "
        "Control Architecture 8 items) are reviewed; all responses are acceptable except "
        "one unfulfilled commitment \u2014 HMI Display Screenshots P22-BREAD-09-008-001 "
        "\u2014 tracked as NOTE-05."
    )
    aplicar_arial_12(para)

    # ===== 2. DETAILED OBSERVATIONS =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 3.1 IO List ---
    doc.add_heading("I/O List Rev B \u2014 P22-LI-09-008-001", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B addresses six groups of prior ADASA observations. Vibration transmitters VT09-001, "
        "VT09-002, and VT09-003 are added (Items 39, 43, 48). Winding and bearing RTDs for the "
        "HP Pump (TE09-002/003, Items 40\u201341) and CIP Pump (TE09-004/005, Items 120\u2013121) "
        "are incorporated as 3-Wire RTD signals to module 5069-IY4, closing the request from "
        "Transmittal N8. The 2nd Stage Inlet Pressure Transmitter PIT09-005 (Item 90), CIP Tank "
        "Temperature Transmitter TIT09-001 (Item 108), and the five new CIP valves (VE09-012 through "
        "VE09-015) are added in Rev B. VFD electrical parameters for HP Pump and CIP Pump are now "
        "provided via Ethernet/IP (Items 34\u201337 and 115\u2013118). Eleven UHPRO LCP Power Meter "
        "readings appear via Modbus TCP/IP (Items 1\u201311). The ADASA\u2013module interface signals "
        "are added: Item 19 (SYSTEM ENABLE COMMAND FROM DCS, DI) and Item 21 "
        "(SYSTEM RUNNING STATUS TO DCS, DO)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-01 \u2014 Motor temperature tag inconsistency (MAJOR)", level=3
    )

    para = doc.add_paragraph()
    para.add_run(
        "Rev B designates TE09-002/003 (HP Pump winding and bearing) and TE09-004/005 (CIP Pump "
        "winding and bearing) as the I/O tags for the four motor RTD inputs. The Data Transfer List "
        "Rev A submitted simultaneously maps the same physical measurements under TIT09-002/003 "
        "and TIT09-004/005, with descriptions \u201cHP Pump Winding Temperature Transmitter,\u201d "
        "\u201cHP Pump Bearing Temperature Transmitter,\u201d etc. A single field device cannot carry "
        "two different instrument tags across project documents. The distinction matters: TE denotes a "
        "sensor-only element, TIT a transmitter with 4-20mA output. The instrument in question is an "
        "RTD connected to a PLC analog input module (5069-IY4) \u2014 it functions as a TIT in the "
        "loop, making TIT the correct functional class."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "A second conflict involves TIT-09-003 specifically. Transmittal N8 reviewed datasheet "
        "P22-LI-09-008-013 Rev A, which covered TIT-09-003 as the CIP Tank Temperature Transmitter "
        "(Rosemount 214C RTD + Rosemount 644H transmitter). The Data Transfer List Rev A now assigns "
        "TIT09-003 to RO HP Pump Bearing Temperature (Modbus address 30009). These two descriptions "
        "are mutually exclusive: TIT-09-003 cannot designate both a CIP Tank instrument and an "
        "HP Pump bearing sensor. "
        "BW Water must issue a consolidated resolution in I/O List Rev C and Data Transfer List Rev B: "
        "(1) adopt a single tag per instrument; (2) confirm whether TIT-09-003 belongs to the CIP Tank "
        "or the HP Pump bearing; (3) update Instrument List Rev C consistently."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 Interface contact type not specified as relay (MINOR)", level=3
    )

    para = doc.add_paragraph()
    para.add_run(
        "Items 19 and 21 specify \u201cDry Contact (N.O) 24VDC\u201d for the ADASA\u2013module "
        "interface. ADASA\u2019s March 11, 2026 internal confirmation established that the ADASA PLC "
        "provides a relay output for the DI enable signal, and the BW Water PLC must provide a relay "
        "output for the DO running status \u2014 not a transistor or solid-state output, which has "
        "different inrush and voltage characteristics. Specify \u201crelay contact\u201d explicitly "
        "in the next revision to complete loop documentation."
    )
    aplicar_arial_12(para)

    # --- 3.2 Data Transfer List ---
    doc.add_heading(
        "Data Transfer List (Modbus TCP/IP) Rev A \u2014 P22-LI-09-008-004", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev A delivers the complete Modbus TCP/IP memory map between the BW Water PLC and the "
        "ADASA DCS: 64 digital inputs across registers 10001\u201310004, 16 digital outputs in "
        "register 00001, and 109 analog points covering power meter variables, VFD parameters, "
        "motorized valve position feedbacks, process instrumentation, and speed/position setpoints. "
        "The ADASA\u2013module interface signals are present: system enable command (DCS\u2192module) "
        "at address 10001.7 and system running status (module\u2192DCS) at 00001.0. "
        "This document closes Transmittal N7 OBS-03, pending since Transmittal N3."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-02 \u2014 Conductivity ranges incompatible with brine process conditions (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Three brine-side conductivity instruments carry Modbus scaling ranges that cannot cover "
        "their operating window. Transmittal N8 raised this observation against the Instrument List; "
        "the Data Transfer List now confirms the calibrated ranges remain uncorrected."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Tag", "Location", "DTL Range", "Expected Range", "Status"),
            (
                "CIT-09-001",
                "RO Cartridge Filter Discharge (feed brine)",
                "0\u201320\u00a0mS/cm",
                "65\u201380\u00a0mS/cm",
                "NOT CORRECTED",
            ),
            (
                "CIT-09-004",
                "Interstage Turbocharger Inlet (Stage 1 reject)",
                "0\u201320\u00a0mS/cm",
                "85\u2013108\u00a0mS/cm",
                "NOT CORRECTED",
            ),
            (
                "CIT-09-005",
                "Concentrate Reject Discharge (train reject)",
                "0\u201320\u00a0mS/cm",
                "108\u2013133\u00a0mS/cm",
                "NOT CORRECTED",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run(
        "Expected conductivities are derived from Process Calculation P22-CD-09-009-001 Rev B "
        "at feed TDS 43,000\u201353,000\u00a0mg/L (ET \u2014 Feed Brine Quality). The Modbus "
        "engineering unit scaling must reflect the instrument\u2019s calibrated range. "
        "BW Water must correct all three entries in Data Transfer List Rev B and in Instrument List "
        "Rev C. Note: ET \u2014 Conductivity Transmitters requires toroidal technology for services "
        "above 20\u00a0mS/cm; this was confirmed by the Rosemount 228 selection for CIT-09-005 in "
        "the conductivity datasheet (Transmittal N8). CIT-09-001 and CIT-09-004 must also be "
        "evaluated for toroidal vs. contacting technology at their respective expected conductivities."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-03 \u2014 VE09-014 misplaced in DI block; level alarms absent from Modbus map (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Items 22\u201323 (Modbus addresses 10002.5\u201310002.6) assign VE09-014-SI001 "
        "(Antiscalant Tank Inlet Motorized Valve Position Feedback) and VE09-014-SIC001 "
        "(Position Control) as single-bit DI signals. These are REAL-type 0\u2013100\u00a0% "
        "signals already correctly mapped in the analog section at addresses 40039 and 40071. "
        "Their presence in the DI block is a copy/paste error; the duplicate digital entries "
        "must be removed."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The external signal descriptors for Items 22\u201323 read \u201cCLOSE=HIGH/OPEN=NORMAL\u201d "
        "and \u201cCLOSE=LOW/OPEN=NORMAL,\u201d which are characteristic of discrete level switch "
        "signals. The intended signals at 10002.5\u201310002.6 are LS09-001-XB001 "
        "(Antiscalant Tank Level High) and LS09-002-XB001 (Antiscalant Tank Level Low), both "
        "discrete DI signals listed in I/O List Rev B (Items 128\u2013129). These two antiscalant "
        "tank level alarm signals are entirely absent from the Modbus map and must be added in Rev B."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation \u2014 Motor temperature tag inconsistency (cross-reference OBS-01)", level=3
    )

    para = doc.add_paragraph()
    para.add_run(
        "Data Transfer List Rev A uses TIT09-002/003 and TIT09-004/005 for HP Pump and CIP Pump "
        "temperature signals. The I/O List uses TE09-002/003/004/005 for the same field devices. "
        "See Section 2.1 OBS-01 for the full description and required resolution. The TIT-09-003 "
        "conflict is particularly critical and must be addressed in the consolidated response."
    )
    aplicar_arial_12(para)

    # --- 3.3 Control Architecture ---
    doc.add_heading(
        "Control System Architecture Rev C \u2014 P22-CD-09-004-001", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev C confirms the network topology: Ethernet/IP for HMI, PLC CPU, VFDs, and motorized "
        "valves; Modbus TCP/IP for DCS and Digital Power Meter; fiber optic between DCS and LCP "
        "Panel (installation by others). The PLC standalone configuration (no CPU redundancy) is "
        "formally confirmed in the comment sheet based on the Tender Proposal. "
        "The Digital Power Meter now appears in the architecture communicating via Modbus TCP/IP, "
        "consistent with Items 1\u201311 in I/O List Rev B and Items 81\u201391 in the Data "
        "Transfer List. This is meaningful progress on the energy metering requirement."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-04 \u2014 UPS autonomy not confirmed in submitted document (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal N7 OBS-01 required the UPS autonomy to be updated from 30 minutes to "
        "8 hours per ET \u2014 Control and Automation System. The comment sheet for Rev C states "
        "the architecture \u201chas been revised.\u201d The architecture diagram is predominantly "
        "graphical, and the submitted document contains no extractable text confirming 8-hour "
        "autonomy or a UPS capacity calculation. "
        "BW Water must provide written confirmation in the comment sheet response or as a "
        "separate technical note: (1) the UPS is now sized for 8-hour autonomy; "
        "(2) the supporting capacity calculation (load list, battery bank specification, "
        "autonomy at expected load) is available on request. Without this, Transmittal N7 OBS-01 "
        "cannot be formally closed."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-02 \u2014 Energy metering progress; CEE calculation pending (informational)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The Digital Power Meter is now integrated. Eleven electrical parameters "
        "(voltage L1/L2/L3, current L1/L2/L3, active power, reactive power, frequency, "
        "power factor, active energy) are documented in both the I/O List and the Data Transfer "
        "List. Transmittal N7 OBS-09 additionally requires the CEE "
        "(Specific Energy Consumption, kWh/m\u00b3) calculation to be executed in the PLC and "
        "displayed on the HMI. That logic remains to be confirmed in Control Philosophy Rev B."
    )
    aplicar_arial_12(para)

    # --- 3.4 GA Antiscalant Tank ---
    doc.add_heading(
        "General Arrangement \u2014 Antiscalant Dosing Tank Rev A \u2014 P22-DWG-09-005-015",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev A is the first submission of the tank General Arrangement. The drawing presents "
        "two views (Nozzle Elevation and Nozzle Orientation, scale 1:2) and a nozzle schedule. "
        "The tank body is cylindrical: OD 630\u00a0mm, body height 880\u00a0mm, "
        "total height 1120\u00a0mm. Eight nozzles are scheduled: N01 inlet (1\u201d, top), "
        "N41 spare (1\u201d, top), N75 vent (1\u201d, top), N80 overflow (2\u201d, side at "
        "1031\u00a0mm), N81 drain (1\u201d, side at 150\u00a0mm), N85 outlet (1/2\u201d, side "
        "at 150\u00a0mm), N90 level gauge high (1\u201d, side at 1031\u00a0mm), N91 level gauge "
        "low (1\u201d, side at 150\u00a0mm)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-05 \u2014 Volume, material and seismic anchor data absent from Notes (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The Notes section in Rev A is empty. Neither total installed volume, effective working "
        "volume, body material, nor anchor data appear anywhere in the drawing. "
        "Transmittal N9 OBS-02 documented a discrepancy between the P&ID annotation "
        "(0.27\u00a0m\u00b3 effective volume) and the accepted Antiscalant Dosing Tank Datasheet "
        "(P22-ET-09-009-010 Rev B, Transmittal N4: 0.34\u00a0m\u00b3 total capacity, "
        "0.27\u00a0m\u00b3 effective). A geometric estimate from the GA dimensions yields "
        "approximately 0.25\u00a0m\u00b3 internal volume \u2014 consistent with neither value. "
        "This GA Rev A does not resolve the discrepancy."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B must populate the Notes section with: (1) total installed volume (0.34\u00a0m\u00b3 "
        "per accepted datasheet); (2) effective working volume (0.27\u00a0m\u00b3); "
        "(3) body and liner material for chemical compatibility verification with antiscalant service; "
        "(4) anchor bolt pattern and seismic reaction loads per ET \u2014 Seismic Conditions "
        "(NCh\u00a02369, Zone\u00a03, 2025 edition). "
        "Simultaneously, the P&ID Rev C must annotate TK-09-002 with the 0.34\u00a0m\u00b3 total "
        "installed volume per P&ID convention (see Transmittal N9 OBS-02)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "ET \u2014 Seismic Conditions (Section 4.4) requires that anchors of all main equipment "
        "installed in or with the module be designed for seismic Zone\u00a03 per NCh\u00a02369. "
        "The GA is the appropriate document to show the anchor bolt layout, bolt size, and "
        "reaction loads that feed the civil foundation design."
    )
    aplicar_arial_12(para)

    # --- 3.5 GA 1st Stage Turbo ---
    doc.add_heading(
        "General Arrangement \u2014 1st Stage Feed Turbocharger Rev A \u2014 "
        "P22-DWG-09-005-012 (SIP-09-001)",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev A is the first submission of the Feed Turbocharger General Arrangement. Four views "
        "(top, front, side, ISO) at 1:2 scale show equipment tag SIP-09-001, four grooved-end "
        "connections (Feed Inlet/Outlet 2\u201d, Brine Inlet/Outlet 1.5\u201d, all CUT GROOVE "
        "STYLE 77), and four mounting holes. Overall envelope: approximately "
        "254\u00a0\u00d7\u00a0229\u00a0\u00d7\u00a0191\u00a0mm."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-06 \u2014 Vibration transducer mounting provision absent (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "ET \u2014 Vibration Transmitters requires continuous vibration monitoring on each Energy "
        "Recovery Device. I/O List Rev B includes VT09-002-XQ001 (Concentrate Reject Feed "
        "Turbocharger Vibration Transmitter, Item 43). GA Rev A shows no mounting bracket, "
        "threaded boss, or transducer connection provision for this instrument."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B must show the vibration transducer mounting location with sensor type reference. "
        "If the FEDCO unit delivers monitoring via internal provisions with pre-wired leads to a "
        "junction box, that configuration must be documented on the GA."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-03 \u2014 Coupling pressure rating \u2014 TM N6 OBS-01 open", level=3
    )

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal N6 OBS-01 rejected the Feed Turbocharger datasheet due to coupling pressure "
        "rating downgraded from 2,000\u00a0psi to 1,200\u00a0psi (Piedmont Style H, 19\u00a0% "
        "margin over the 1,008\u00a0psi operating pressure on the brine inlet and feed outlet "
        "connections). GA Rev A specifies CUT GROOVE STYLE 77 connections on all four nozzles. "
        "BW Water must provide the working pressure rating certificate for Style 77 couplings at "
        "1.5\u201d and 2\u201d nominal bore and a deviation disposition resolving TM N6 OBS-01 "
        "before this document can progress beyond \u201cTo be Revised.\u201d"
    )
    aplicar_arial_12(para)

    # --- 3.6 GA 2nd Stage Turbo ---
    doc.add_heading(
        "General Arrangement \u2014 2nd Stage Interstage Turbocharger Rev A \u2014 "
        "P22-DWG-09-005-013 (SIP-09-002)",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev A presents the Interstage Turbocharger in four views at 1:2 scale, equipment tag "
        "SIP-09-002. Connections are four grooved-end ports (Feed Inlet/Outlet 2\u201d, Brine "
        "Inlet/Outlet 1.5\u201d, CUT GROOVE STYLE 77) with four mounting holes. Overall envelope: "
        "approximately 254\u00a0\u00d7\u00a0229\u00a0\u00d7\u00a0203\u00a0mm."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-07 \u2014 Vibration transducer mounting provision absent (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "ET \u2014 Vibration Transmitters requires monitoring on each Energy Recovery Device. "
        "I/O List Rev B includes VT09-003-XQ001 (Interstage Turbocharger Vibration Transmitter, "
        "Item 48). GA Rev A shows no mounting provision for the vibration transducer on SIP-09-002."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B must document the vibration transducer mounting location, consistent with the "
        "requirements stated for SIP-09-001 in Section 2.5 OBS-06."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-04 \u2014 Coupling pressure rating (same concern as SIP-09-001)", level=3
    )

    para = doc.add_paragraph()
    para.add_run(
        "CUT GROOVE STYLE 77 connections on SIP-09-002 carry the same pressure rating uncertainty "
        "as SIP-09-001 (Section 2.5 NOTE-03). BW Water must provide the coupling pressure rating "
        "certificate covering both units."
    )
    aplicar_arial_12(para)

    # ===== 3. ATTACHMENTS =====
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
            ("1", "P22-LI-09-008-001", "I/O List", "B"),
            ("2", "P22-LI-09-008-004", "Data Transfer List (Modbus TCP/IP)", "A"),
            ("3", "P22-CD-09-004-001", "Control System Architecture", "C"),
            (
                "4",
                "P22-DWG-09-005-015",
                "General Arrangement \u2014 Antiscalant Dosing Tank",
                "A",
            ),
            (
                "5",
                "P22-DWG-09-005-012",
                "General Arrangement \u2014 1st Stage Feed Turbocharger (SIP-09-001)",
                "A",
            ),
            (
                "6",
                "P22-DWG-09-005-013",
                "General Arrangement \u2014 2nd Stage Interstage Turbocharger (SIP-09-002)",
                "A",
            ),
        ],
    )

    # ===== 4. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            ("P22-LI-09-008-001", "I/O List", "B", "2 \u2014 Approved as Noted"),
            (
                "P22-LI-09-008-004",
                "Data Transfer List (Modbus TCP/IP)",
                "A",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-CD-09-004-001",
                "Control System Architecture",
                "C",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-DWG-09-005-015",
                "General Arrangement \u2014 Antiscalant Dosing Tank",
                "A",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-DWG-09-005-012",
                "General Arrangement \u2014 1st Stage Feed Turbocharger (SIP-09-001)",
                "A",
                "3 \u2014 To be Revised",
            ),
            (
                "P22-DWG-09-005-013",
                "General Arrangement \u2014 2nd Stage Interstage Turbocharger (SIP-09-002)",
                "A",
                "3 \u2014 To be Revised",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Seven observations require resolution before the next delivery. "
        "Required actions are detailed in Section 2."
    )
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
