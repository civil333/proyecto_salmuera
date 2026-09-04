#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento ADASA: Document Status Register - BW Water.
Fecha: 27 de febrero de 2026 (actualizado con E13 - Submittal 25007-0013)
Codigo: P22-IT-06-000-002-0

Usa template ADASA con portada, cajetin, TOC y contenido programatico.

CAMBIOS 27-Feb-2026 (E13 - Submittal 25007-0013):
- HP Pump (P22-ET-09-009-002): Rev B → Rev C, 3-To be revised → 2-AN
- Feed Turbocharger (P22-ET-09-009-007): Rev B → Rev C, 1-Approved → 4-Rejected
- Interstage Turbocharger (P22-ET-09-009-008): Rev B → Rev C, 1-Approved → 2-AN
- Cartridge Filter (P22-ET-09-009-005): Rev B → Rev C, 2-AN (mantiene)
- Static Mixer (P22-ET-09-009-012): Rev A → Rev B, 3-To be revised → 2-AN
- Valve List (P22-LI-09-005-002): Rev A → Rev B, 3-To be revised → 4-Rejected (nuevos duplicados, CCS falso)
- Utility Consumption List (P22-LI-09-009-001): Rev A → Rev B, 3-To be revised → 2-AN
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    set_updatefields_true,
)
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn


OUTPUT = "P22-IT-06-000-002-0_Document-Status-Register_ADASA.docx"


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_para_bold(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.bold = True
    return para


def crear_registro():
    # 1. Crear documento base
    crear_documento_adasa(
        titulo="DOCUMENT STATUS REGISTER - BW WATER ENGINEERING DELIVERABLES",
        codigo="P22-IT-06-000-002-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
    )

    # 2. Abrir y eliminar placeholders
    doc = Document(OUTPUT)
    elementos_a_eliminar = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos_a_eliminar.append(para)
    for para in elementos_a_eliminar:
        para._element.getparent().remove(para._element)

    # ============================================================
    # EXECUTIVE SUMMARY
    # ============================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(
        doc,
        "This register is a standalone document providing the complete status of all "
        "BW Water engineering deliverables for the Taltal Brine Module. It covers 64 "
        "documents received across deliveries E1-E13 (representing 39 unique documents "
        "at their latest revision), plus 15 contractual deliverables not yet submitted. "
        "Updated 27-Feb-2026 with Entrega 13 (Submittal 25007-0013): 9 documents "
        "reviewed per Transmittal N6."
    )

    doc.add_heading("Delivered Documents - Inventory by Latest Version (39 unique documents, updated E13)", level=2)
    add_simple_table(doc, [
        ("Verdict", "Count", "%", "Description"),
        ("V1 - Approved", "15", "38%", "No further action required"),
        ("V2-AN - Approved as Noted", "14", "36%", "9 clean + 5 with significant observations"),
        ("V3 - To be Revised", "6", "15%", "Resubmission with corrections required"),
        ("V4 - Rejected", "3", "8%", "Complete resubmission required"),
        ("Under review", "1", "3%", "Program/Schedule"),
        ("Total unique documents", "39", "100%", "E13 updated revisions for 7 documents"),
    ])

    doc.add_heading("Not Delivered (15 documents)", level=2)
    add_simple_table(doc, [
        ("Category", "Count", "Details"),
        ("ET Section 7 deliverables not delivered", "12", "Listed in ET pp. 27-29"),
        ("Additional (other ET sections)", "3", "MCC DS, Modbus Map, A/C Thermal Calc"),
        ("ET Section 7 partially delivered", "2", "Layouts, Valve/Instrument specs"),
    ])

    doc.add_heading("Overall Gap", level=2)
    add_simple_table(doc, [
        ("Metric", "Value"),
        ("Documents requiring correction (V3+V4+V2-AN significant)", "14"),
        ("Documents not delivered", "15"),
        ("Total action items", "29"),
    ])

    add_para(
        doc,
        "Contractual basis: ET P22-ET-09-000-001-0, Section 7 (pp. 27-29) establishes "
        "the complete list of engineering deliverables required within 90 days of NTP. "
        "As of 17-Feb-2026, approximately 135 days after NTP, multiple items remain "
        "undelivered with no submission date communicated by BW Water."
    )

    # ============================================================
    # COMPLETE DOCUMENT INVENTORY
    # ============================================================
    doc.add_heading("COMPLETE DOCUMENT INVENTORY", level=1)

    add_para(
        doc,
        "The following tables list every unique document received from BW Water at its "
        "latest revision only. Documents with multiple revisions (e.g., Rev A in E1 "
        "superseded by Rev C in E13) appear once with the most recent verdict."
    )
    add_para(
        doc,
        "For documents requiring correction, detailed observations are provided in "
        "DOCUMENTS REQUIRING CORRECTION and in the corresponding transmittals N1-N6."
    )

    # --- Process ---
    doc.add_heading("Process", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("1", "P22-DWG-09-009-001", "PFD", "B", "E8", "N3", "1-Approved", "Rev A (E1) superseded"),
        ("2", "P22-DWG-09-009-002", "P&ID", "A", "E3", "N3", "2-AN", "Requires update after valve/instrument corrections"),
        ("3", "P22-CD-09-009-001", "Process Calculation", "B", "E7", "N3", "2-AN", "SEC calc incomplete, recovery rate verification"),
        ("4", "P22-ET-09-009-001", "DS UHPRO System", "B", "E6", "N2", "1-Approved", "Rev A (E2) superseded"),
    ])

    # --- Mechanical / Equipment ---
    doc.add_heading("Mechanical / Equipment", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("5", "P22-ET-09-009-002", "DS HP Pump", "C", "E13", "N6", "2-AN", "Pt-100 windings/bearings CLOSED. Note: FEDCO power values clarification pending"),
        ("6", "P22-ITEM-09-009-003", "DS CIP Pump", "A", "E1", "N1", "4-Rejected", "No Rev B after 63+ days"),
        ("7", "P22-ET-09-009-004", "DS Antiscalant Pump", "B", "E7", "N3", "1-Approved", "Rev A (E1) superseded"),
        ("8", "P22-ET-09-009-005", "DS RO Container", "B", "E8", "N3", "1-Approved", "Was V4 in E1, resolved in Rev B"),
        ("9", "P22-ET-09-009-005", "DS RO Cartridge Filter", "C", "E13", "N6", "2-AN", "12 cartridges justified. Note piping isometrics"),
        ("10", "P22-ET-09-009-007", "DS CIP Cartridge Filter", "B", "E6", "N2", "2-AN", "Minor notes"),
        ("11", "P22-ET-09-009-007", "DS Feed Turbocharger", "C", "E13", "N6", "4-Rejected", "Coupling 1200 psi insuf. Rev D req."),
        ("12", "P22-ET-09-009-008", "DS Interstage Turbocharger", "C", "E13", "N6", "2-AN", "Coupling 1800 psi: margin 1.46x acceptable. Vibration mounting to confirm in Rev D"),
        ("13", "P22-ET-09-009-010", "DS CIP Tank", "B", "E7", "N3", "1-Approved", "Rev A (E1) superseded"),
        ("14", "P22-ET-09-009-011", "DS Antiscalant Dosing Tank", "B", "E10", "N4", "2-AN", "Minor notes"),
        ("15", "P22-ET-09-009-014", "DS CIP Tank Heater", "B", "E8", "N3", "1-Approved", "Rev A (E5) superseded"),
        ("16", "P22-ET-09-009-012", "DS Air Conditioning", "A", "E5", "N2", "3-To be revised", "Thermal calculation missing"),
        ("17", "P22-ET-09-009-012", "DS Static Mixer", "B", "E13", "N6", "2-AN", "FRP confirmed, L/D improved. TAG MZE-09-001 vs P&ID to confirm"),
    ])

    # --- Piping ---
    doc.add_heading("Piping", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("18", "P22-ET-09-005-001", "Piping Specifications", "A", "E1", "N1", "1-Approved", ""),
        ("19", "P22-ET-09-005-002", "Painting Specifications", "A", "E1", "N1", "2-AN", "Minor notes"),
    ])

    # --- Electrical ---
    doc.add_heading("Electrical", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("20", "P22-CD-09-007-001", "Single Line Diagram", "A", "E1", "N1", "1-Approved", ""),
        ("21", "P22-LI-09-007-001", "Electrical Load List", "A", "E1", "N1", "1-Approved", ""),
        ("22", "P22-ET-09-007-001", "DS Electrical Auxiliaries", "A", "E1", "N1", "1-Approved", ""),
        ("23", "P22-ET-09-007-002", "DS Power & Control Cable", "A", "E9", "N3", "1-Approved", ""),
        ("24", "P22-ET-09-007-003", "DS Cable Tray", "A", "E9", "N3", "1-Approved", ""),
        ("25", "P22-ET-09-007-004", "DS Conduit & Flexible", "A", "E9", "N3", "1-Approved", ""),
        ("26", "P22-LI-09-007-002", "Power Cable Schedule", "A", "E9", "N3", "1-Approved", ""),
        ("27", "P22-DWG-09-007-003", "Grounding Layout", "A", "E8", "N3", "2-AN", "Minor notes"),
        ("28", "P22-DWG-09-007-004", "Cable Tray Layout", "A", "E11", "N4", "3-To be revised", "Routing concerns, sizing verification"),
    ])

    # --- Instrumentation & Control ---
    doc.add_heading("Instrumentation & Control", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("29", "P22-ET-09-008-001", "DS PLC & HMI", "A", "E1", "N1", "2-AN", "Minor notes"),
        ("30", "P22-CD-09-004-001", "Control Architecture", "B", "E11", "N4", "2-AN", "UPS not included, Modbus Map pending"),
        ("31", "P22-LI-09-008-001", "IO List", "A", "E8", "N3", "3-To be revised", "Missing signals, TAG inconsistencies"),
        ("32", "P22-LI-09-008-003", "Instrument List", "A", "E8", "N3", "3-To be revised", "Missing instruments, range discrepancies"),
        ("33", "P22-LI-09-005-002", "Valve List", "B", "E13", "N6", "4-Rejected", "4 duplicate TAGs + false CCS. Rev C urgente"),
        ("34", "P22-LI-09-005-001", "Equipment List", "A", "E8", "N3", "2-AN", "Discrepancies vs P&ID"),
        ("35", "P22-DWG-09-008-001", "Instrument Location Layout", "A", "E9", "N3", "3-To be revised", "Incomplete, missing instruments"),
        ("36", "P22-LI-09-008-002", "I&C Cable Schedule", "A", "E8", "N3", "1-Approved", ""),
    ])

    # --- Lists ---
    doc.add_heading("Lists", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Del.", "TM", "Verdict", "Notes"),
        ("37", "P22-LI-09-009-002", "Chemical Consumption List", "A", "E7", "N3", "1-Approved", ""),
        ("38", "P22-LI-09-009-003", "Line List", "A", "E7", "N3", "2-AN", "Minor notes"),
        ("39", "P22-LI-09-009-001", "Utility Consumption List", "B", "E13", "N6", "2-AN", "PLC 50Hz CLOSED, A/C n+1 CLOSED, HP Pump power CLOSED. A/C thermal calc still pending"),
    ])

    # --- Inventory Summary ---
    doc.add_heading("Inventory Summary", level=2)
    add_simple_table(doc, [
        ("Verdict", "Count", "Documents"),
        ("1-Approved", "15", "#1, 4, 7, 8, 13, 15, 18, 20, 21, 22, 23, 24, 25, 26, 36, 37"),
        ("2-AN (clean)", "9", "#9, 10, 12, 14, 17, 19, 27, 29, 38"),
        ("2-AN (significant obs.)", "5", "#2, 3, 5, 30, 39"),
        ("3-To be revised", "6", "#16, 28, 31, 32, 35"),
        ("4-Rejected", "3", "#6, 11, 33"),
        ("Under review", "1", "Program/Schedule"),
        ("Total", "39", ""),
    ])

    add_para(
        doc,
        "Note: This inventory covers documents received through E1-E13. Updated 27-Feb-2026 "
        "with Entrega 13 (Submittal 25007-0013). For the 15 contractual deliverables not yet "
        "submitted, see the following section.",
        size=10,
    )

    # ============================================================
    # DOCUMENTS NOT YET DELIVERED
    # ============================================================
    doc.add_heading("DOCUMENTS NOT YET DELIVERED", level=1)

    doc.add_heading("ET Section 7 Deliverables", level=2)
    add_para(
        doc,
        "ET Section 7 organizes deliverables by two contractual deadlines: items #40-57 "
        "(maximum 90 days from NTP, ET pp. 27-29) and items #58-62 (one month before "
        "end of contract, ET pp. 29-30). The following tables cross-reference each "
        "deliverable against documents received in deliveries E1-E11. Note: without "
        "written approval of items #58-62, BW Water cannot release equipment for "
        "transport to site (ET Sec.7 p.30)."
    )

    doc.add_heading("Critical - Block Fabrication or Procurement", level=3)
    add_simple_table(doc, [
        ("#", "ET Section 7 Deliverable", "ET Ref", "Status", "Impact"),
        ("6", "Equipment and piping arrangement drawings (plan + elevation)", "Sec 7 p.28", "NOT DELIVERED", "Blocks civil design, piping procurement"),
        ("12", "Manufacturing and testing dossier", "Sec 7 p.28", "NOT DELIVERED", "Prerequisite for factory acceptance"),
        ("18", "Isometric drawings - high pressure lines", "Sec 7 p.28", "NOT DELIVERED", "Blocks piping fabrication"),
        ("20", "Detailed PIE (Plan de Inspeccion y Ensayos)", "Sec 7 pp.28-29", "NOT DELIVERED", "Manufacturing prerequisite per contract"),
    ])

    doc.add_heading("Major - Block Detailed Engineering or Integration", level=3)
    add_simple_table(doc, [
        ("#", "ET Section 7 Deliverable", "ET Ref", "Status", "Impact"),
        ("7", "Seismic calculation (NCh 2369 Zone 3)", "Sec 7 p.28", "NOT DELIVERED", "Structural design cannot proceed"),
        ("8", "High-pressure line flexibility analysis", "Sec 7 p.28", "NOT DELIVERED", "Piping stress verification pending"),
        ("9", "Civil requirements drawings (dimensions, loads, anchors)", "Sec 7 p.28", "NOT DELIVERED", "Foundations design blocked"),
        ("14", "Control Philosophy (P&ID TAGs, interlocks, sequences)", "Sec 7 p.28", "NOT DELIVERED", "Control Architecture (E11) does not replace this"),
        ("15", "HMI screen design", "Sec 7 p.28", "NOT DELIVERED", "Operator interface undefined"),
        ("19", "Lifting beams and crane rail design", "Sec 7 p.28", "NOT DELIVERED", "Structural/mechanical integration"),
    ])

    doc.add_heading("Other - Contractual Requirements", level=3)
    add_simple_table(doc, [
        ("#", "ET Section 7 Deliverable", "ET Ref", "Status", "Impact"),
        ("16", "Detailed deliverables list (brands + models for all equipment)", "Sec 7 p.28", "NOT DELIVERED", "Cannot verify scope compliance"),
        ("17", "3D Model (Autodesk-interoperable)", "Sec 7 p.28", "NOT DELIVERED", "Clash detection, integration review"),
    ])

    doc.add_heading("Pre-Completion Deliverables — 1 month before end of contract (Items #58-62)", level=3)
    add_para(
        doc,
        "These 5 documents have a different contractual deadline: 1 month before project "
        "completion (ET Sec.7 pp.29-30). ET states explicitly: 'Without written approval "
        "of all documentation, BW Water cannot release equipment for transport to site.' "
        "None have been delivered or partially addressed as of 17-Feb-2026.",
        size=10,
    )
    add_simple_table(doc, [
        ("#", "ET Section 7 Deliverable", "ET Ref", "Status", "Impact"),
        ("58", "Installation manual (lifting calc, plan, yoke design)", "Sec 7 p.29", "NOT DELIVERED", "Required for site mobilization planning"),
        ("59", "Commissioning manual", "Sec 7 p.29", "NOT DELIVERED", "Prerequisite for startup planning"),
        ("60", "O&M manual (PLC screens, TAGs, procedures, emergency response)", "Sec 7 p.29", "NOT DELIVERED", "Required for operator training and handover"),
        ("61", "Final software package and licenses (PLC/HMI source code)", "Sec 7 p.29", "NOT DELIVERED", "Contractual requirement per ET 5.4"),
        ("62", "Preservation, packaging and maritime transport procedure", "Sec 7 p.30", "NOT DELIVERED", "Must be approved before shipping (BAE Cl. 41)"),
    ])

    doc.add_heading("Partially Delivered (Ambiguous)", level=3)
    add_simple_table(doc, [
        ("#", "ET Sec 7 Deliverable", "Status", "Received", "Missing"),
        ("5", "General layouts", "PARTIAL", "Instrument Layout (E9), Cable Tray Layout (E11), Grounding Layout (E8)", "Equipment Layout, General Arrangement"),
        ("13", "Valve/instrument specifications (brands + models)", "PARTIAL", "Valve List (E8), Instrument List (E8)", "Brands and models incomplete for several items"),
    ])

    add_para(
        doc,
        'Note on items #5 and #6: "Layouts" (p.27) and "Planos de arreglo de equipos '
        'y canerias" (p.28) appear as separate items in the ET. Partial coverage from '
        "discipline-specific layouts (instrument, cable tray, grounding) does NOT satisfy "
        "the general equipment/piping arrangement requirement.",
        size=10,
    )

    # --- Additional from other ET sections ---
    doc.add_heading("Additional Deliverables from Other ET Sections", level=2)
    add_para(
        doc,
        "These items are required by specific ET sections or contractual commitments "
        "but are not explicitly listed in ET Section 7:"
    )
    add_simple_table(doc, [
        ("#", "Deliverable", "ET Reference", "Status", "Notes"),
        ("21", "MCC Datasheet (Motor Control Center)", 'ET 5.4 + Sec 7 "equipment datasheets"', "NOT DELIVERED", "Pending since Dec-2025. MCC reportedly in fabrication without approved DS"),
        ("22", "Modbus TCP Memory Map", "ET 5.4 + TM N2 commitment", "NOT DELIVERED", "42+ days with no evidence of progress"),
        ("23", "A/C Thermal Calculation (complete)", "ET 5.1.11", "NOT DELIVERED", "A/C DS delivered (E5) but thermal calculation not included"),
    ])

    doc.add_heading("Summary: Not Delivered", level=2)
    add_simple_table(doc, [
        ("Category", "Count"),
        ("ET Section 7 - not delivered (90-day items)", "12"),
        ("ET Section 7 - not delivered (pre-completion #21-25)", "5"),
        ("Other ET sections - not delivered", "3"),
        ("ET Section 7 - partially delivered", "2"),
        ("Total not delivered", "20"),
    ])

    # ============================================================
    # DOCUMENTS REQUIRING CORRECTION
    # ============================================================
    doc.add_heading("DOCUMENTS REQUIRING CORRECTION", level=1)

    add_para(
        doc,
        "Documents delivered by BW Water that received adverse review verdicts and "
        "require resubmission or correction. Only the latest version of each document "
        "is counted."
    )

    doc.add_heading("Verdict 3 - To Be Revised (9 documents)", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Del.", "TM", "Key Issue"),
        ("1", "P22-ET-09-009-002-B", "DS HP Pump Rev B", "E7", "N3", "Materials, seals, RTDs, performance curve issues"),
        ("2", "P22-ET-09-009-012-A", "DS Air Conditioning", "E5", "N2", "Thermal calculation missing, capacity verification"),
        ("3", "P22-ET-09-009-013-A", "DS Static Mixer", "E5", "N2", "Material compatibility, pressure rating"),
        ("4", "P22-LI-09-005-002-A", "Valve List", "E8", "N3", "Actuator sizing, rating inconsistencies vs P&ID"),
        ("5", "P22-LI-09-008-001-A", "IO List", "E8", "N3", "Missing signals, TAG inconsistencies"),
        ("6", "P22-LI-09-008-003-A", "Instrument List", "E8", "N3", "Missing instruments, range discrepancies"),
        ("7", "P22-DWG-09-008-001-A", "Instrument Location Layout", "E9", "N3", "Incomplete, missing instruments from list"),
        ("8", "P22-LI-09-009-001-A", "Utility Consumption List", "E10", "N4", "Incomplete data, missing consumption figures"),
        ("9", "P22-DWG-09-007-004-A", "Cable Tray Layout", "E11", "N4", "Routing concerns, sizing verification pending"),
    ])

    doc.add_heading("Verdict 4 - Rejected, No Corrected Version Submitted (1 document)", level=2)
    add_simple_table(doc, [
        ("#", "Code", "Document", "Del.", "TM", "Key Issue"),
        ("10", "P22-ITEM-09-009-003-A", "DS CIP Pump", "E1", "N1", "Rejected in TM N1. No Rev B submitted after 63 days"),
    ])

    add_para(
        doc,
        "Resolved rejections: DS RO Container (V4 in E1) was resubmitted as Rev B in "
        "E8 and approved (V1). DS HP Pump (V4 in E1) was resubmitted as Rev B in E7 "
        "but received V3 (counted in table above, item #1).",
        size=10,
    )

    doc.add_heading("Verdict 2-AN with Significant Open Observations (4 documents)", level=2)
    add_para(
        doc,
        "These documents were approved as noted but carry observations that require "
        "action before detailed engineering can proceed:"
    )
    add_simple_table(doc, [
        ("#", "Code", "Document", "Del.", "TM", "Open Observation"),
        ("11", "P22-LI-09-005-001-A", "Equipment List", "E8", "N3", "Discrepancies vs P&ID (missing equipment, capacity mismatches)"),
        ("12", "P22-CD-09-004-001-B", "Control Architecture Rev B", "E11", "N4", "UPS not included, Modbus TCP Map not delivered"),
        ("13", "P22-DWG-09-009-002-A", "P&ID", "E3", "N3", "Requires update after valve list, instrument list corrections"),
        ("14", "P22-CD-09-009-001-B", "Process Calculation Rev B", "E7", "N3", "SEC calculation incomplete, recovery rate verification"),
    ])

    doc.add_heading("Summary: Requiring Correction", level=2)
    add_simple_table(doc, [
        ("Verdict", "Count", "Action Required"),
        ("V3 - To be revised", "9", "Resubmission with corrections mandatory"),
        ("V4 - Rejected (no Rev B)", "1", "Complete resubmission required"),
        ("V2-AN with significant observations", "4", "Corrections expected before detailed engineering"),
        ("Total", "14", ""),
    ])

    # ============================================================
    # CROSS-REFERENCE: ET SECTION 7 vs DELIVERED
    # ============================================================
    doc.add_heading("CROSS-REFERENCE: ET SECTION 7 vs DELIVERED", level=1)

    add_para(doc, "Complete status of all ET Section 7 deliverables:")

    add_simple_table(doc, [
        ("#", "ET Sec 7 Deliverable", "Status", "Document Received", "Verdict"),
        ("1", "Detailed schedule (15 days from NTP)", "Delivered (deficient)", "Program Oct-2025, updated Feb-2026", "Under review - incomplete"),
        ("2", "P&ID", "Delivered", "P22-DWG-09-009-002-A (E3)", "2-AN"),
        ("3", "PFD", "Delivered", "P22-DWG-09-009-001 Rev B (E8)", "1-Approved"),
        ("4", "Process calculation (53k TDS)", "Delivered", "P22-CD-09-009-001-B (E7)", "2-AN (SEC incomplete)"),
        ("5", "General layouts", "PARTIAL", "Instrument Layout (E9), Cable Tray (E11), Grounding (E8)", "V3 / V2-AN"),
        ("6", "Equipment/piping arrangement", "NOT DELIVERED", "--", "--"),
        ("7", "Seismic calculation", "NOT DELIVERED", "--", "--"),
        ("8", "HP line flexibility analysis", "NOT DELIVERED", "--", "--"),
        ("9", "Civil requirements drawings", "NOT DELIVERED", "--", "--"),
        ("10", "Single-line diagrams", "Delivered", "P22-CD-09-007-001-A (E1)", "1-Approved"),
        ("11", "Equipment datasheets (Sec 5.1)", "Delivered (majority)", "Multiple E1-E10", "Mixed (V1 to V4)"),
        ("12", "Manufacturing and testing dossier", "NOT DELIVERED", "--", "--"),
        ("13", "Valve/instrument specs (brands+models)", "PARTIAL", "Valve List (E8), Instrument List (E8)", "V3"),
        ("14", "Control Philosophy", "NOT DELIVERED", "Control Architecture (E11) not equivalent", "--"),
        ("15", "HMI screen design", "NOT DELIVERED", "--", "--"),
        ("16", "Detailed deliverables list", "NOT DELIVERED", "--", "--"),
        ("17", "3D Model (Autodesk interoperable)", "NOT DELIVERED", "--", "--"),
        ("18", "HP line isometric drawings", "NOT DELIVERED", "--", "--"),
        ("19", "Lifting beams and crane rails", "NOT DELIVERED", "--", "--"),
        ("20", "Detailed PIE", "NOT DELIVERED", "--", "--"),
        ("21 → #58", "Installation manual (lifting calc, plan, yoke)", "NOT DELIVERED", "--", "1 month before end of contract"),
        ("22 → #59", "Commissioning manual", "NOT DELIVERED", "--", "1 month before end of contract"),
        ("23 → #60", "O&M manual (PLC screens, TAGs, procedures)", "NOT DELIVERED", "--", "1 month before end of contract"),
        ("24 → #61", "Final software package and licenses", "NOT DELIVERED", "--", "1 month before end of contract"),
        ("25 → #62", "Preservation, packaging and transport procedure", "NOT DELIVERED", "--", "1 month before end of contract"),
    ])

    add_para(
        doc,
        "Items #21-25 (ET Sec.7 numbering) correspond to Master Register items #58-62. "
        "Deadline: 1 month before end of contract (not 90 days from NTP). "
        "ET condition: written approval of all 5 documents is required before "
        "BW Water can release equipment for transport to site.",
        size=10,
    )

    # ============================================================
    # MASTER DELIVERABLE STATUS
    # ============================================================
    doc.add_heading("MASTER DELIVERABLE STATUS", level=1)

    add_para(
        doc,
        "Consolidated view of every BW Water deliverable obligation \u2014 delivered "
        "documents (latest revision) and contractual items not yet submitted \u2014 "
        "in a single table."
    )

    # Review Verdict Nomenclature
    doc.add_heading("Review Verdict Nomenclature", level=2)
    add_simple_table(doc, [
        ("Code", "Verdict", "Description"),
        ("1", "Approved", "Document accepted. No further action required"),
        ("2-AN", "Approved as Noted", "Accepted with observations (minor notes or significant pending items)"),
        ("3", "To be Revised", "Document requires corrections and resubmission"),
        ("4", "Rejected", "Document rejected. Complete resubmission required"),
        ("--", "Not applicable", "Document not yet delivered. No verdict assigned"),
    ])

    # Split into two sub-tables for readability (7 cols is wide)
    doc.add_heading("Delivered Documents (39)", level=2)
    add_simple_table(doc, [
        ("#", "Document", "Code", "Rev", "Status", "Verdict", "Action Required"),
        ("1", "PFD", "P22-DWG-09-009-001", "B", "Delivered (E8)", "1-Approved", "None"),
        ("2", "P&ID", "P22-DWG-09-009-002", "A", "Delivered (E3)", "2-AN", "Update after valve/instrument corrections"),
        ("3", "Process Calculation", "P22-CD-09-009-001", "B", "Delivered (E7)", "2-AN", "Complete SEC calc, verify recovery rate"),
        ("4", "DS UHPRO System", "P22-ET-09-009-001", "B", "Delivered (E6)", "1-Approved", "None"),
        ("5", "DS HP Pump", "P22-ET-09-009-002", "B", "Delivered (E7)", "3-To be revised", "Materials, seals, RTDs, unify power"),
        ("6", "DS CIP Pump", "P22-ITEM-09-009-003", "A", "Delivered (E1)", "4-Rejected", "Resubmit Rev B (63+ days overdue)"),
        ("7", "DS Antiscalant Pump", "P22-ET-09-009-004", "B", "Delivered (E7)", "1-Approved", "None"),
        ("8", "DS RO Container", "P22-ET-09-009-005", "B", "Delivered (E8)", "1-Approved", "None"),
        ("9", "DS RO Cartridge Filter", "P22-ET-09-009-006", "B", "Delivered (E8)", "2-AN", "Minor notes"),
        ("10", "DS CIP Cartridge Filter", "P22-ET-09-009-007", "B", "Delivered (E6)", "2-AN", "Minor notes"),
        ("11", "DS Feed Turbocharger", "P22-ET-09-009-008", "B", "Delivered (E8)", "1-Approved", "None"),
        ("12", "DS Interstage Turbo.", "P22-ET-09-009-009", "B", "Delivered (E8)", "1-Approved", "None"),
        ("13", "DS CIP Tank", "P22-ET-09-009-010", "B", "Delivered (E7)", "1-Approved", "None"),
        ("14", "DS Antisc. Dosing Tank", "P22-ET-09-009-011", "B", "Delivered (E10)", "2-AN", "Minor notes"),
        ("15", "DS CIP Tank Heater", "P22-ET-09-009-014", "B", "Delivered (E8)", "1-Approved", "None"),
        ("16", "DS Air Conditioning", "P22-ET-09-009-012", "A", "Delivered (E5)", "3-To be revised", "Thermal calculation missing"),
        ("17", "DS Static Mixer", "P22-ET-09-009-013", "A", "Delivered (E5)", "3-To be revised", "Material compat., pressure rating"),
        ("18", "Piping Specifications", "P22-ET-09-005-001", "A", "Delivered (E1)", "1-Approved", "None"),
        ("19", "Painting Specifications", "P22-ET-09-005-002", "A", "Delivered (E1)", "2-AN", "Minor notes"),
        ("20", "Single Line Diagram", "P22-CD-09-007-001", "A", "Delivered (E1)", "1-Approved", "None"),
        ("21", "Electrical Load List", "P22-LI-09-007-001", "A", "Delivered (E1)", "1-Approved", "None"),
        ("22", "DS Electrical Aux.", "P22-ET-09-007-001", "A", "Delivered (E1)", "1-Approved", "None"),
        ("23", "DS Power & Ctrl Cable", "P22-ET-09-007-002", "A", "Delivered (E9)", "1-Approved", "None"),
        ("24", "DS Cable Tray", "P22-ET-09-007-003", "A", "Delivered (E9)", "1-Approved", "None"),
        ("25", "DS Conduit & Flexible", "P22-ET-09-007-004", "A", "Delivered (E9)", "1-Approved", "None"),
        ("26", "Power Cable Schedule", "P22-LI-09-007-002", "A", "Delivered (E9)", "1-Approved", "None"),
        ("27", "Grounding Layout", "P22-DWG-09-007-003", "A", "Delivered (E8)", "2-AN", "Minor notes"),
        ("28", "Cable Tray Layout", "P22-DWG-09-007-004", "A", "Delivered (E11)", "3-To be revised", "Routing, sizing verification"),
        ("29", "DS PLC & HMI", "P22-ET-09-008-001", "A", "Delivered (E1)", "2-AN", "Minor notes"),
        ("30", "Control Architecture", "P22-CD-09-004-001", "B", "Delivered (E11)", "2-AN", "UPS missing, Modbus Map pending"),
        ("31", "IO List", "P22-LI-09-008-001", "A", "Delivered (E8)", "3-To be revised", "Missing signals, TAG issues"),
        ("32", "Instrument List", "P22-LI-09-008-003", "A", "Delivered (E8)", "3-To be revised", "Missing instruments, ranges"),
        ("33", "Valve List", "P22-LI-09-005-002", "A", "Delivered (E8)", "3-To be revised", "Actuator sizing, rating vs P&ID"),
        ("34", "Equipment List", "P22-LI-09-005-001", "A", "Delivered (E8)", "2-AN", "Discrepancies vs P&ID"),
        ("35", "Instrument Loc. Layout", "P22-DWG-09-008-001", "A", "Delivered (E9)", "3-To be revised", "Incomplete, missing instruments"),
        ("36", "I&C Cable Schedule", "P22-LI-09-008-002", "A", "Delivered (E8)", "1-Approved", "None"),
        ("37", "Chemical Consumption", "P22-LI-09-009-002", "A", "Delivered (E7)", "1-Approved", "None"),
        ("38", "Line List", "P22-LI-09-009-003", "A", "Delivered (E7)", "2-AN", "Minor notes"),
        ("39", "Utility Consumption", "P22-LI-09-009-001", "A", "Delivered (E10)", "3-To be revised", "Incomplete data"),
    ])

    doc.add_heading("Not Delivered / Partial (23 items)", level=2)
    add_para(
        doc,
        "(*) Items #58-62: deadline is 1 month before end of contract (ET Sec.7 pp.29-30). "
        "Without written approval of these documents, BW Water cannot release equipment for transport to site.",
        size=10,
    )
    add_simple_table(doc, [
        ("#", "Document", "Reference", "Status", "Action Required", "ET Deadline"),
        ("40", "Detailed Schedule", "ET Sec 7, p.27", "Delivered (deficient)", "Missing FAT, commissioning, document schedule", "Max. 15 days from NTP"),
        ("41", "General Layouts (Equipment, GA)", "ET Sec 7, p.27", "PARTIAL", "Only discipline-specific layouts received", "Max. 90 days from NTP"),
        ("42", "Equipment/Piping Arrangement Drawings", "ET Sec 7, p.28", "NOT DELIVERED", "Blocks civil design, piping procurement", "Max. 90 days from NTP"),
        ("43", "Seismic Calculation (NCh 2369)", "ET Sec 7, p.28", "NOT DELIVERED", "Structural design blocked", "Max. 90 days from NTP"),
        ("44", "HP Line Flexibility Analysis", "ET Sec 7, p.28", "NOT DELIVERED", "Piping stress verification pending", "Max. 90 days from NTP"),
        ("45", "Civil Requirements Drawings", "ET Sec 7, p.28", "NOT DELIVERED", "Foundations design blocked", "Max. 90 days from NTP"),
        ("46", "Manufacturing and Testing Dossier", "ET Sec 7, p.28", "NOT DELIVERED", "Prerequisite for factory acceptance", "Max. 90 days from NTP"),
        ("47", "Valve/Instrument Specs (brands+models)", "ET Sec 7, p.28", "PARTIAL", "Lists delivered but brands/models incomplete", "Max. 90 days from NTP"),
        ("48", "Control Philosophy", "ET Sec 7, p.28", "NOT DELIVERED", "Control Architecture is not equivalent", "Max. 90 days from NTP"),
        ("49", "HMI Screen Design", "ET Sec 7, p.28", "NOT DELIVERED", "Operator interface undefined", "Max. 90 days from NTP"),
        ("50", "Detailed Deliverables List", "ET Sec 7, p.28", "NOT DELIVERED", "Cannot verify scope compliance", "Max. 90 days from NTP"),
        ("51", "3D Model (Autodesk interoperable)", "ET Sec 7, p.28", "NOT DELIVERED", "Clash detection blocked", "Max. 90 days from NTP"),
        ("52", "HP Line Isometric Drawings", "ET Sec 7, p.28", "NOT DELIVERED", "Blocks piping fabrication", "Max. 90 days from NTP"),
        ("53", "Lifting Beams and Crane Rails", "ET Sec 7, p.28", "NOT DELIVERED", "Structural/mechanical integration", "Max. 90 days from NTP"),
        ("54", "Detailed PIE", "ET Sec 7, pp.28-29", "NOT DELIVERED", "Manufacturing prerequisite per contract", "Max. 90 days from NTP (*)"),
        ("55", "MCC Datasheet", "ET 5.4", "NOT DELIVERED", "MCC reportedly in fabrication without DS", "Max. 90 days from NTP"),
        ("56", "Modbus TCP Memory Map", "ET 5.4 + TM N2", "NOT DELIVERED", "42+ days, program not started", "Max. 90 days from NTP"),
        ("57", "A/C Thermal Calculation", "ET 5.1.11", "NOT DELIVERED", "A/C DS delivered but no thermal calc", "Max. 90 days from NTP"),
        ("58 (*)", "Installation Manual (lifting calc, plan, yoke)", "ET Sec 7, p.29", "NOT DELIVERED", "Required for site mobilization planning", "1 MONTH BEFORE END OF CONTRACT"),
        ("59 (*)", "Commissioning Manual", "ET Sec 7, p.29", "NOT DELIVERED", "Prerequisite for startup planning", "1 MONTH BEFORE END OF CONTRACT"),
        ("60 (*)", "O&M Manual (PLC screens, TAGs, procedures)", "ET Sec 7, p.29", "NOT DELIVERED", "Required for operator training and handover", "1 MONTH BEFORE END OF CONTRACT"),
        ("61 (*)", "Final Software Package and Licenses", "ET Sec 7, p.29", "NOT DELIVERED", "PLC/HMI source code, perpetual licenses", "1 MONTH BEFORE END OF CONTRACT"),
        ("62 (*)", "Preservation, Packaging and Transport Proc.", "ET Sec 7, p.30", "NOT DELIVERED", "Must be approved before shipping (BAE Cl. 41)", "1 MONTH BEFORE END OF CONTRACT"),
    ])

    doc.add_heading("Master Summary", level=2)
    add_simple_table(doc, [
        ("Status", "Count", "%"),
        ("Approved (V1)", "15", "25%"),
        ("Approved as Noted (V2-AN clean)", "9", "15%"),
        ("Approved as Noted (V2-AN significant)", "5", "8%"),
        ("To be Revised (V3)", "6", "10%"),
        ("Rejected (V4)", "3", "5%"),
        ("Under review", "1", "2%"),
        ("Partially delivered", "2", "3%"),
        ("Not delivered", "19", "32%"),
        ("Total BW Water obligations", "60", "100%"),
    ])

    add_para_bold(
        doc,
        "Bottom line: Of 60 identifiable BW Water deliverable obligations, only 24 "
        "(40%) are fully resolved (V1 or V2-AN clean). The remaining 36 items (60%) "
        "require action: 14 corrections/resubmissions, 19 not yet delivered, 2 partial."
    )

    # ============================================================
    # STATISTICS
    # ============================================================
    doc.add_heading("STATISTICS", level=1)

    doc.add_heading("Complete Inventory (delivered documents, latest version only)", level=2)
    add_simple_table(doc, [
        ("Verdict", "Count", "% of delivered"),
        ("V1 - Approved", "15", "38%"),
        ("V2-AN - Approved as Noted (clean)", "9", "23%"),
        ("V2-AN - Approved as Noted (significant obs.)", "5", "13%"),
        ("V3 - To be Revised", "6", "15%"),
        ("V4 - Rejected (no resubmission)", "3", "8%"),
        ("Under review (Program)", "1", "3%"),
        ("Total unique documents delivered", "39", "100%"),
    ])

    doc.add_heading("Not Delivered", level=2)
    add_simple_table(doc, [
        ("Category", "Count"),
        ("ET Section 7 - not delivered (90-day items)", "12"),
        ("ET Section 7 - not delivered (pre-completion #21-25)", "5"),
        ("ET Section 7 - partially delivered", "2"),
        ("Other ET sections - not delivered", "3"),
        ("Total not delivered", "20"),
    ])

    doc.add_heading("Overall Project Metrics", level=2)
    add_simple_table(doc, [
        ("Metric", "Value"),
        ("Total raw documents received (E1-E11)", "54"),
        ("Unique documents at latest revision", "39"),
        ("Documents requiring correction (V3+V4+V2-AN significant)", "14"),
        ("Documents not delivered (incl. ET Sec 7 pp.29-30)", "20"),
        ("Total action items (corrections + missing)", "34"),
        ("Total BW Water obligations identified", "60"),
        ("Days since NTP (approx.)", "~135 days (vs 90-day contractual deadline)"),
        ("BW Water schedule extension (self-declared)", "+109 days (engineering to 24-Apr-2026)"),
    ])

    # Set TOC update on open
    set_updatefields_true(doc)

    doc.save(OUTPUT)
    print(f"Registro generado exitosamente: {OUTPUT}")
    return OUTPUT


if __name__ == "__main__":
    crear_registro()
