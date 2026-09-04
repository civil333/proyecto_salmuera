#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento ADASA de evaluacion de respuestas BWW.
Fecha: 17 de febrero de 2026
Codigo: P22-IT-06-000-001-0

Usa template ADASA con portada, cajetin, TOC y contenido programatico.
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
)
from docx import Document
from docx.shared import Pt


OUTPUT = "2026-02-17_Evaluacion-Respuestas-BWW_ADASA.docx"


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


def crear_evaluacion():
    # 1. Crear documento base con portada + cajetin + TOC
    crear_documento_adasa(
        titulo="EVALUATION OF BW WATER RESPONSES TO TRANSMITTALS N3, N4 AND SCHEDULE",
        codigo="P22-IT-06-000-001-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
    )

    # 2. Abrir documento y eliminar contenido placeholder
    doc = Document(OUTPUT)

    # Eliminar parrafos placeholder generados por crear_documento_adasa
    elementos_a_eliminar = []
    encontrado_placeholder = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado_placeholder:
            encontrado_placeholder = True
        if encontrado_placeholder:
            elementos_a_eliminar.append(para)

    for para in elementos_a_eliminar:
        p = para._element
        p.getparent().remove(p)

    # ============================================================
    # EXECUTIVE SUMMARY
    # ============================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(
        doc,
        "On February 16, 2026, BW Water submitted responses to three pending items: "
        "Transmittal N3 (P22-TM-09-000-003-0), Transmittal N4 (P22-TM-09-000-004-0), "
        "and schedule-related requests from ADASA\u2019s February 10 email. This document "
        "presents ADASA\u2019s formal evaluation of each response and serves as preparation "
        "material for the coordination meeting scheduled for February 18, 2026.",
    )

    add_para(
        doc,
        "The responses are partial. BW Water addressed 6 of 17 observations from TM N3 "
        "and 5 of 10 from TM N4. Several accepted items (Pt-100 sensors, vibration "
        "transmitters, duplicate TAG correction, A/C n+1) represent meaningful progress. "
        "However, two items stand out as critically deficient: the Modbus TCP Memory Map "
        "(program not started after 42 days) and the Container 60ft configuration (under "
        "review for three months after formal rejection).",
    )

    add_para(
        doc,
        "The schedule response includes a significant commitment: BW Water confirmed "
        "that no purchase orders will be issued before ADASA approves the relevant "
        "datasheets. This addresses one of ADASA\u2019s principal concerns regarding "
        "procurement sequencing.",
    )

    add_simple_table(doc, [
        ("Category", "Count", "Percentage"),
        ("Accepted", "6", "22%"),
        ("Insufficient", "4", "15%"),
        ("Not Addressed", "7", "26%"),
        ("Remaining (TM N3 minor/medium)", "10", "37%"),
        ("Total Observations", "27", "100%"),
    ])

    # ============================================================
    # EVALUATION OF TM N3 RESPONSES
    # ============================================================
    doc.add_heading("EVALUATION OF TM N3 RESPONSES", level=1)

    doc.add_heading("Response Coverage", level=2)
    add_para(
        doc,
        "BW Water responded to 6 of 17 observations from Transmittal N3 "
        "(P22-TM-09-000-003-0), submitted January 28, 2026. The response was "
        "received 19 days after transmittal issuance.",
    )

    doc.add_heading("Evaluation Table", level=2)
    add_simple_table(doc, [
        ("OBS", "Subject", "BW Water Response", "ADASA Evaluation", "Status"),
        ("01", "Missing vibration transmitters", "Will include VT per ET 5.5.7", "Commitment accepted. Pending in revised IL/Layout.", "Accepted"),
        ("02", "SEC calculation incomplete", "Not addressed", "Remains open.", "Pending"),
        ("03", "VM-09-015 manual DN100 900#", "Referenced, no explicit confirmation", "Must confirm electric actuation per ET 5.2.3.", "Insufficient"),
        ("04", "Missing DO module status", "Requested clarification", "Clarification provided: external PLC, DO signal (0=stopped, 1=running).", "Pending BWW"),
        ("05", "Missing DI external enable", "Requested clarification", "Clarification provided: DI signal (1=authorized, 0=stop). Hardwired.", "Pending BWW"),
        ("06", "Missing Pt-100 HP Pump windings", "Will include Pt-100 per ET 5.3", "Commitment accepted. Pending in revised datasheet.", "Accepted"),
        ("07", "CIP Pump missing RTDs bearings", "Will include RTDs per ET 5.1.4", "Commitment accepted. CIP Pump DS still required.", "Accepted"),
        ("08", "CIP Pump missing Pt-100 motor", "Will include Pt-100 per ET 5.3", "Commitment accepted. Pending in CIP Pump DS.", "Accepted"),
        ("09", "Temperature switches vs transmitters", "Not addressed", "TSH (DI) should be TIT (AI, 4-20mA+HART).", "Pending"),
        ("10", "Layout inherits duplicate TAG", "Will correct when FIT resolved", "Accepted as dependency on IL correction.", "Accepted (cond.)"),
        ("11", "Duplicate TAG FIT-09-001", "Will renumber to FIT-09-002", "Standard correction. Aligns with IO List.", "Accepted"),
        ("12", "Duplicate TAGs Valve List", "Not addressed", "VM-09-015, VE-09-008, VE-09-010 remain open.", "Pending"),
        ("13", "TAGs with incorrect area code", "Not addressed", "VM-07-005, VM-07-031, VE-07-009 corrections open.", "Pending"),
        ("14", "Equipment List vs P&ID discrepancies", "Not addressed", "Static Mixer TAG, CIP Tank, Dosing Pump remain.", "Pending"),
        ("15", "Missing VFD electrical variables", "Responded about protocol", "Insufficient. Need V, A, kW, Hz, T as AI signals for SEC.", "Insufficient"),
        ("16", "Missing DO module status (IO)", "See OBS-04", "Clarification provided. Awaiting BWW confirmation.", "Pending BWW"),
        ("17", "Missing DI external enable (IO)", "See OBS-05", "Clarification provided. Awaiting BWW confirmation.", "Pending BWW"),
    ])

    doc.add_heading("Summary TM N3", level=2)
    add_simple_table(doc, [
        ("Status", "Count", "Observations"),
        ("Accepted", "6", "OBS-01, 06, 07, 08, 10, 11"),
        ("Insufficient", "2", "OBS-03, 15"),
        ("Pending BWW (clarification provided)", "3", "OBS-04, 05, 16/17"),
        ("Pending (not addressed)", "6", "OBS-02, 09, 12, 13, 14"),
        ("Total", "17", ""),
    ])

    # ============================================================
    # EVALUATION OF TM N4 RESPONSES
    # ============================================================
    doc.add_heading("EVALUATION OF TM N4 RESPONSES", level=1)

    doc.add_heading("Response Coverage", level=2)
    add_para(
        doc,
        "BW Water responded to 5 of 10 observations from Transmittal N4 "
        "(P22-TM-09-000-004-0), submitted February 5, 2026. The response was "
        "received 11 days after transmittal issuance.",
    )

    doc.add_heading("Evaluation Table", level=2)
    add_simple_table(doc, [
        ("OBS", "Subject", "BW Water Response", "ADASA Evaluation", "Status"),
        ("01", "PLC specified at 60 Hz", "PLC is dual-frequency (50/60 Hz)", "Requires documentation in revised datasheet.", "Accepted (cond.)"),
        ("02", "A/C without n+1 configuration", "Will add 2nd A/C unit", "Commitment accepted. Pending updated Utility List.", "Accepted"),
        ("03", "Missing A/C thermal calculation", "Will deliver document", "Commitment noted. No delivery date provided.", "Accepted (cond.)"),
        ("04", "Modbus TCP Memory Map", "Program has not yet started", "Unacceptable. 42 days since commitment. Delivery date required.", "Insufficient"),
        ("05", "Duplicate TAG FIT-09-001 (Layout)", "Will correct when IL updated", "Accepted as dependency.", "Accepted (cond.)"),
        ("06", "Missing vibration transmitters (Layout)", "See TM N3 OBS-01", "Accepted. Layout follows IL update.", "Accepted (cond.)"),
        ("07", "Missing Pt-100 motors (Layout)", "See TM N3 OBS-06/07/08", "Accepted. Layout follows datasheet updates.", "Accepted (cond.)"),
        ("08", "HP Pump power inconsistency", "Not addressed", "Four values (83/86/92/93 kW). Unification required.", "Pending"),
        ("09", "UPS not included in BOM", "Not addressed", "ET 5.4 requires UPS 8h autonomy. Must be added.", "Pending"),
        ("10", "Container 60ft configuration", "Still under review", "Unacceptable. Rejected Nov 17, 2025. 3 months without resolution.", "Insufficient"),
    ])

    doc.add_heading("Summary TM N4", level=2)
    add_simple_table(doc, [
        ("Status", "Count", "Observations"),
        ("Accepted", "2", "OBS-02, 03"),
        ("Accepted (conditional)", "4", "OBS-01, 05, 06, 07"),
        ("Insufficient", "2", "OBS-04, 10"),
        ("Pending (not addressed)", "2", "OBS-08, 09"),
        ("Total", "10", ""),
    ])

    # ============================================================
    # EVALUATION OF SCHEDULE RESPONSE
    # ============================================================
    doc.add_heading("EVALUATION OF SCHEDULE RESPONSE", level=1)

    doc.add_heading("Items Confirmed", level=2)
    add_simple_table(doc, [
        ("Item", "BW Water Statement", "ADASA Evaluation"),
        ("Equipment basis", "EXW Penang, Malaysia", "Consistent with contract. Shipping to Florida noted."),
        ("Shipping date", "Estimated August 3, 2026", "Subject to engineering completion timeline."),
        ("No POs before approval", "POs will not be issued before ADASA approves datasheets", "Contractually significant. Recorded as formal commitment."),
        ("Engineering completion", "April 24, 2026", "Extended from 65-day baseline (139 days). To discuss Feb 18."),
    ])

    doc.add_heading("Items Pending for February 18 Meeting", level=2)
    add_simple_table(doc, [
        ("Item", "Requested", "Status"),
        ("Delivery plan with milestones", "Feb 10 email", "Not yet received"),
        ("Updated schedule with document dates", "Feb 10 email", "Not yet received"),
        ("Document delivery schedule (14 pending + 16 in revision)", "Jan 28 (TM N3)", "Not yet received"),
    ])

    doc.add_heading("Procurement Sequencing Analysis", level=2)
    add_para(
        doc,
        "The commitment to not issue POs before datasheet approval is particularly "
        "relevant for the following items:",
    )

    add_para_mixed(doc, [
        ("HP Pump: ", True),
        ("Datasheet carries \u201cTo be revised\u201d verdict. PR/PO was programmed for "
         "Feb 16 in BW Water\u2019s schedule. Power value must be unified (83/86/92/93 kW) "
         "and Pt-100 sensors confirmed before procurement.", False),
    ])
    add_para_mixed(doc, [
        ("Antiscalant system: ", True),
        ("CT-001 evaluation issued Feb 16 with 4 pending observations (deadline Feb 20). "
         "Procurement was programmed for Feb 25-26.", False),
    ])
    add_para_mixed(doc, [
        ("Instruments: ", True),
        ("Vibration transmitters and Pt-100 sensors now confirmed but not yet in "
         "datasheets or Instrument List.", False),
    ])

    # ============================================================
    # CT-001 STATUS
    # ============================================================
    doc.add_heading("CT-001 STATUS", level=1)

    add_para(
        doc,
        "Technical Query CT-001 (Antiscalant Dosing Justification) was evaluated "
        "separately. The evaluation document (P22-CT-09-000-001-1) was issued on "
        "February 16, 2026, with a cover email to BW Water.",
    )

    doc.add_heading("Key Findings from CT-001 Evaluation", level=2)

    add_para(
        doc,
        "The 0.5 ppm dosing rate was accepted in principle based on AWC PROTON "
        "simulation confirming positive safety margins. However, four observations "
        "remain pending (3 Major, 1 Minor):",
    )

    add_simple_table(doc, [
        ("#", "Observation", "Priority"),
        ("1", "Temperature basis: AWC projection at 19\u00b0C, not 24\u00b0C worst-case per ET Table 4-1", "Major"),
        ("2", "Chemical Consumption List: volumetric flow 0.02 vs calculated 0.024 L/h", "Minor"),
        ("3", "AWC input: Strontium 0.00 (vs measured 10-11 mg/L), Silica 2.1 (vs worst-case 6.4 mg/L)", "Major"),
        ("4", "Contradictory conclusions between AWC and CREST Water assessments", "Major"),
    ])

    add_para_mixed(doc, [
        ("Response deadline: February 20, 2026. ", True),
        ("CT-001 is tracked separately from transmittal observations.", False),
    ])

    # ============================================================
    # BWW RESPONSE TO ADASA EVALUATION — FEB 17, 2026
    # ============================================================
    doc.add_heading("BWW RESPONSE TO ADASA EVALUATION \u2014 FEB 17, 2026", level=1)

    add_para(
        doc,
        "On February 17, 2026, BW Water (Eduardo Yamauchi) responded inline to ADASA\u2019s "
        "email titled \u201cRE: Catch-Up Schedule Request \u2014 Overdue Response Required.\u201d "
        "The response was received the same day ADASA issued its formal evaluation document "
        "(P22-IT-06-000-001-0). This section records each BWW response for formal traceability, "
        "structured by resolution status, and updates the evaluation accordingly.",
    )

    doc.add_heading("Items Accepted \u2014 Confirmed by Both Parties", level=2)
    add_simple_table(doc, [
        ("Item", "Source", "BWW Response", "Final Status"),
        ("Pt-100 motor windings", "TM N3 OBS-06/07/08", "Confirmed per ET 5.3", "CLOSED \u2014 Accepted"),
        ("Vibration transmitters", "TM N3 OBS-01", "Confirmed per ET 5.5.7", "CLOSED \u2014 Accepted"),
        ("Duplicate TAG FIT-09-001", "TM N3/N4 OBS-05/11", "Renumbered to FIT-09-002", "CLOSED \u2014 Accepted"),
        ("A/C n+1 configuration", "TM N4 OBS-02", "Confirmed per ET 5.1.11", "CLOSED \u2014 Accepted"),
        ("EXW Penang basis", "Schedule request", "Equipment ready August 3, 2026", "CLOSED \u2014 Noted"),
        ("No POs before datasheet approval", "Schedule request", "\u201cConfirmed\u201d (verbatim)", "CLOSED \u2014 Formal commitment on record"),
    ])

    doc.add_heading("Critical Items \u2014 BWW Response", level=2)
    add_simple_table(doc, [
        ("Item", "Source", "ADASA Position", "BWW Response (verbatim)", "ADASA Assessment", "Status"),
        (
            "Modbus TCP Memory Map",
            "TM N4 OBS-04",
            "Program not started after 42 days. Firm delivery date required.",
            "\u201cWe will review and address later\u201d",
            "INACEPTABLE. No delivery date and no commitment. Consistent pattern of deferral on the highest-priority deliverable.",
            "OPEN \u2014 Critical",
        ),
        (
            "Container 60ft",
            "TM N4 OBS-10",
            "Rejected Nov 17, 2025. Three months without corrected documentation.",
            "Current docs show 40ft for RO; CIP and chemicals located outside; will be reflected in future documents.",
            "PARTIAL. Technical position acknowledged but no corrected documents delivered. Formal confirmation of 40ft configuration still required.",
            "OPEN \u2014 Partial",
        ),
    ])

    doc.add_heading("Items Requiring Clarification \u2014 BWW Response", level=2)
    add_simple_table(doc, [
        ("Item", "Source", "ADASA Requirement", "BWW Response", "ADASA Assessment", "Status"),
        (
            "VM-09-015 actuation",
            "TM N3 OBS-03",
            "Electric actuation per ET 5.2.3 (DN100, ANSI 900#, HP Pump discharge)",
            "\u201cNot a process relevant valve \u2014 ET 5.2.3 not applicable\u201d",
            "TECHNICAL DISPUTE. Valve is in the HP Pump discharge line. BWW must provide written technical justification for exemption from ET 5.2.3.",
            "OPEN \u2014 Dispute",
        ),
        (
            "VFD electrical variables",
            "TM N3 OBS-15",
            "Individual AI signals per VFD: V, A, kW, Hz, T for SEC calculation",
            "Will show SEC and total system variables, not per individual VFD",
            "INSUFFICIENT. Total system metrics do not satisfy individual VFD monitoring requirements or SEC disaggregation per ADASA standard.",
            "OPEN \u2014 Insufficient",
        ),
        (
            "HP Pump power",
            "TM N4 OBS-08",
            "Unify four conflicting values: 83/86/92/93 kW across documents",
            "\u201cWe will review and address later\u201d",
            "INACEPTABLE. Four inconsistent values remain unresolved. No unification date provided. Procurement risk active.",
            "OPEN \u2014 Deferred",
        ),
        (
            "UPS in BOM",
            "TM N4 OBS-09",
            "UPS with 8h autonomy per ET 5.4. Must appear in Control Architecture BOM.",
            "Not in that document but included in deliverables; will be included in next revision.",
            "COMMITMENT ACCEPTABLE. No specific delivery date provided. To be monitored in next submittal cycle.",
            "OPEN \u2014 Committed",
        ),
        (
            "Partial coverage (16/27 obs)",
            "TM N3 + TM N4",
            "Full response to all transmitted observations is required.",
            "\u201cWe will review and address later\u201d",
            "INACEPTABLE. Eleven observations remain unanswered without any timeline or prioritization.",
            "OPEN \u2014 Deferred",
        ),
        (
            "OBS-04/05 TM N3 (external signals)",
            "TM N3 OBS-04/05",
            "DO/DI coordination signals. Technical clarification provided by ADASA on Feb 17.",
            "\u201cWe will review and address later\u201d",
            "INACEPTABLE. BWW did not engage with the technical context explicitly provided by ADASA. Clarification is already complete on ADASA\u2019s side.",
            "OPEN \u2014 Deferred",
        ),
    ])

    doc.add_heading("Meeting Status \u2014 February 18, 2026", level=2)
    add_para(
        doc,
        "BW Water confirmed the February 18 coordination meeting. Eduardo Yamauchi noted "
        "that the engineering team in Asia may not be available due to the Chinese New Year "
        "holiday period, with a possible one-day delay in their participation. This introduces "
        "a risk that the meeting proceeds without direct technical representation from the "
        "engineering team responsible for the open critical items.",
    )

    doc.add_heading("Updated Status Summary After BWW Response", level=2)
    add_simple_table(doc, [
        ("Status", "Count", "Items"),
        ("Accepted \u2014 Closed", "6", "Pt-100, Vibration TX, FIT-09-002, A/C n+1, EXW Penang, No POs"),
        ("Container \u2014 Partial", "1", "TM N4 OBS-10: technical position stated; corrected docs not yet delivered"),
        ("Technical Dispute", "1", "TM N3 OBS-03: VM-09-015 actuation (written justification required)"),
        ("Committed, no date", "1", "TM N4 OBS-09: UPS in BOM (next revision)"),
        ("Deferred \u2014 \u201cWill address later\u201d", "4", "Modbus Map, HP Pump power, partial coverage, OBS-04/05"),
        ("Not addressed (carried forward)", "11", "Remaining TM N3 and TM N4 observations not covered by BWW response"),
    ])

    # ============================================================
    # CONSOLIDATED OUTSTANDING ITEMS
    # ============================================================
    doc.add_heading("CONSOLIDATED OUTSTANDING ITEMS", level=1)

    add_para(
        doc,
        "The following table consolidates all outstanding items requiring BW Water "
        "action, ordered by priority and age.",
    )

    add_simple_table(doc, [
        ("#", "Item", "Source", "Days Open", "Priority", "Status"),
        ("1", "Modbus TCP Memory Map", "TM N2/N4 OBS-04", "42", "Critical", "Program not started"),
        ("2", "Container 40ft confirmation", "TM N4 OBS-10", "92*", "Critical", "Under review"),
        ("3", "HP Pump power unification", "TM N4 OBS-08", "12", "Major", "Not addressed"),
        ("4", "UPS in Control Architecture BOM", "TM N4 OBS-09", "12", "Major", "Not addressed"),
        ("5", "VM-09-015 electric actuation", "TM N3 OBS-03", "20", "Critical", "Insufficient response"),
        ("6", "VFD electrical variables for SEC", "TM N3 OBS-15", "20", "Critical", "Insufficient response"),
        ("7", "Duplicate TAGs Valve List (3)", "TM N3 OBS-12", "20", "Major", "Not addressed"),
        ("8", "Area code corrections Valve List", "TM N3 OBS-13", "20", "Minor", "Not addressed"),
        ("9", "Equipment List vs P&ID discrepancies", "TM N3 OBS-14", "20", "Minor", "Not addressed"),
        ("10", "Temperature switches vs transmitters", "TM N3 OBS-09", "20", "Major", "Not addressed"),
        ("11", "SEC calculation with energy recovery", "TM N3 OBS-02", "20", "Medium", "Not addressed"),
        ("12", "DO/DI external coordination signals", "TM N3 OBS-04/05", "20", "Critical", "Clarification sent Feb 17"),
        ("13", "Delivery plan with milestones", "Feb 10 email", "7", "High", "Expected Feb 18"),
        ("14", "Document delivery schedule", "TM N3 (Jan 28)", "20", "High", "Expected Feb 18"),
        ("15", "CT-001 pending observations (4)", "CT-001 eval", "1", "High", "Deadline Feb 20"),
        ("16", "A/C thermal calculation", "TM N2/N4 OBS-03", "42", "Critical", "Committed, no date"),
    ])

    add_para(doc, "* Days since ADASA formal rejection of 60ft proposal (Nov 17, 2025).", size=9)

    # ============================================================
    # RISK ASSESSMENT
    # ============================================================
    doc.add_heading("RISK ASSESSMENT", level=1)

    add_simple_table(doc, [
        ("Risk", "Probability", "Impact", "Trigger", "Mitigation"),
        (
            "Modbus Map delays PLC interface design",
            "High", "High",
            "If not delivered by end of February, ADASA cannot complete PLC-to-PLC communication design",
            "Escalate at Feb 18 meeting. Request firm deadline.",
        ),
        (
            "Container 60ft imposed without approval",
            "Medium", "Very High",
            "If BWW proceeds with 60ft without approval, cost/schedule impact applies per contract",
            "Require written confirmation at Feb 18. If 60ft needed, formal change request mandatory.",
        ),
        (
            "HP Pump procured with wrong power rating",
            "Low", "High",
            "BWW committed to no POs before approval (risk reduced), but approval may be slow",
            "Track datasheet revision. Power must be unified first.",
        ),
        (
            "Antiscalant system sized incorrectly",
            "Medium", "Medium",
            "If CT-001 observations not resolved by Feb 20, procurement may proceed on incomplete basis",
            "CT-001 deadline Feb 20. If not met, formally object to procurement.",
        ),
        (
            "Engineering timeline not recoverable",
            "Medium", "Very High",
            "If Feb 18 delivery plan lacks credible recovery path, Apr 24 baseline may slip",
            "Review delivery plan critically. Compare against 30 remaining documents.",
        ),
    ])

    doc.save(OUTPUT)
    print(f"Evaluacion generada exitosamente: {OUTPUT}")
    return OUTPUT


if __name__ == "__main__":
    crear_evaluacion()
