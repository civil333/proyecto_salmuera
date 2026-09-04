#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar punteo de reunion de coordinacion ADASA / BW Water.
Fecha: 18 de febrero de 2026
Codigo: P22-IT-06-000-003-0

Documento interno ADASA. Resume estado de observaciones por transmittal
y puntos criticos a resolver en la reunion de coordinacion del 18-Feb-2026.
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
from docx.shared import Pt, RGBColor

OUTPUT = "2026-02-18_Punteo-Reunion-BW-Water_ADASA.docx"


def add_para(doc, text, size=11, bold=False, color=None):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)
    return para


def add_para_mixed(doc, fragments, size=11):
    para = doc.add_paragraph()
    for text, bold in fragments:
        run = para.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(size)
        run.bold = bold
    return para


def crear_punteo():
    # 1. Crear documento base
    crear_documento_adasa(
        titulo="COORDINATION MEETING — BRIEFING DOCUMENT\nBW WATER / ADASA — FEBRUARY 18, 2026",
        codigo="P22-IT-06-000-003-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
    )

    doc = Document(OUTPUT)

    # Eliminar placeholder de la skill
    elementos_a_eliminar = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos_a_eliminar.append(para)
    for para in elementos_a_eliminar:
        p = para._element
        p.getparent().remove(p)

    # ============================================================
    # MEETING CONTEXT
    # ============================================================
    doc.add_heading("MEETING CONTEXT", level=1)

    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Date / Time", "February 18, 2026 — 9:00 AM EST | 11:00 AM Chile"),
        ("Participants", "ADASA + BW Water Americas (Eduardo Yamauchi)"),
        ("Format", "Video conference — 1 hour"),
        ("Risk", "BWW engineering team in Asia may be absent (Chinese New Year)"),
    ])

    add_para(doc, "")
    add_para(doc,
        "BW Water responded inline on February 17 covering 6 of 27 observations from "
        "Transmittals N3 and N4. Multiple observations from Transmittals N1 and N2 remain "
        "unresolved. The following sections consolidate the full picture across all four "
        "transmittals and identify the items requiring resolution at today's meeting.",
    )

    add_para(doc, "")
    add_simple_table(doc, [
        ("Key commitment recorded 17-Feb", "Status"),
        ("No POs before ADASA datasheet approval", "CONFIRMED — Formal commitment on record"),
        ("EXW Penang — Ready to ship August 3, 2026", "CONFIRMED — Noted"),
        ("Engineering completion date: April 24, 2026", "ACKNOWLEDGED — 109-day delay from baseline"),
        ("Delivery plan + document schedule", "PROMISED for February 18 meeting"),
    ])

    doc.add_page_break()

    # ============================================================
    # BLOQUE 1 — ESTADO POR TRANSMITTAL
    # ============================================================
    doc.add_heading("TRANSMITTAL STATUS — ALL OBSERVATIONS", level=1)

    # ---- TM N1 ----
    doc.add_heading("Transmittal N1 — E1 + E2 | Issued December 16, 2025", level=2)

    add_para(doc, "20 documents reviewed. Most observations resolved in subsequent submissions. Two items remain open.", bold=False)
    add_para(doc, "")

    add_simple_table(doc, [
        ("Document", "TM N1 Verdict", "Re-submission", "Current Status"),
        ("DS Container (P22-ET-09-000-01)", "4 - Rejected", "Rev B / TM N3", "CLOSED — Approved"),
        ("PFD (P22-DWG-09-009-001)", "4 - Rejected", "Rev B / TM N3", "CLOSED — Approved"),
        ("Process Calculation", "4 - Rejected", "Rev B / TM N2", "CLOSED — Approved"),
        ("DS HP Pump (P22-ET-09-009-002)", "4 - Rejected", "Rev B / TM N3", "OPEN — Pt-100 committed Feb 17 but Rev C not yet submitted"),
        ("DS CIP Pump (P22-ET-09-009-003)", "4 - Rejected", "Rev B partial / TM N2", "OPEN — Complete DS with temperature sensors never delivered"),
        ("DS RO Cartridge Filter", "3 - To be revised", "Rev B / TM N2", "CLOSED — Approved"),
        ("DS Feed Turbocharger", "3 - To be revised", "Rev B / TM N3", "CLOSED — Approved"),
        ("DS Antiscalant Tank", "3 - To be revised", "Rev B / TM N4", "CLOSED — Approved as noted"),
        ("Remaining E2 documents (5)", "3 - To be revised", "Re-submitted", "CLOSED — Approved"),
    ])

    add_para(doc, "")
    add_simple_table(doc, [
        ("TM N1 Summary", "Count"),
        ("Closed", "18"),
        ("Still open", "2  (DS HP Pump Rev C + DS CIP Pump complete)"),
    ])

    # ---- TM N2 ----
    doc.add_heading("Transmittal N2 — E3–E7 | Issued January 26, 2026", level=2)

    add_para(doc, "8 documents reviewed. Critical open items from this transmittal are the oldest unresolved issues in the project.", bold=False)
    add_para(doc, "")

    doc.add_heading("P&ID — Approved as noted | 13 observations open", level=3)
    add_simple_table(doc, [
        ("OBS", "Subject", "Current Status"),
        ("01", "Battery limits ADASA/BWW — indicate with flange", "No revision since TM N2"),
        ("02", "PVC lines within SDSS zone", "No revision since TM N2"),
        ("03–08", "Line TAGs, drains, connections, HP Pump characteristics", "No revision since TM N2"),
        ("10", "Super Duplex material in HP lines", "No revision since TM N2"),
        ("11–14", "Valve TAGs, instrument TAGs, flow direction, legend", "No revision since TM N2"),
    ])

    add_para(doc, "")
    doc.add_heading("Control Architecture — Approved as noted", level=3)
    add_simple_table(doc, [
        ("OBS", "Subject", "Current Status"),
        ("01–07", "PLC datasheet, Ethernet ports, I/O count, HMI screens", "Partially covered in Rev B (TM N4)"),
        ("08", "Modbus TCP Memory Map for DCS integration", "CRITICAL — 42 days since commitment. Program not started."),
        ("09", "VFD electrical variables as individual AI signals for SEC", "INSUFFICIENT — BWW offers total system metrics only"),
        ("10", "Total power metering configuration (fieldbus vs SAI-09-001)", "No response"),
    ])

    add_para(doc, "")
    doc.add_heading("A/C Thermal Calculation — To be revised", level=3)
    add_simple_table(doc, [
        ("OBS", "Subject", "Current Status"),
        ("01", "Thermal load undersized: 5.96 kW calculated vs ~11-15 kW real", "Conditionally accepted — corrected calculation not yet delivered"),
        ("02", "n+1 configuration — minimum 2 A/C units per ET 5.1.11", "CLOSED — BWW confirmed 2nd unit (Feb 17)"),
        ("05/06", "Container wall heat transfer + solar radiation (Taltal desert) not included", "Pending in corrected calculation"),
    ])

    add_para(doc, "")
    doc.add_heading("Static Mixer — To be revised", level=3)
    add_simple_table(doc, [
        ("OBS", "Subject", "Current Status"),
        ("01", "Material: PVC proposed vs FRP in Technical Offer", "No formal justification delivered"),
        ("02/03", "Mixing velocity 71% lower — efficiency not validated", "No validation delivered"),
        ("04", "Koflo equivalence to KOMAX not confirmed", "No response"),
    ])
    add_para(doc,
        "WARNING: BWW schedule shows Static Mixer manufacturing completed October–November 2025. "
        "If already fabricated in PVC without ADASA approval, this constitutes an active contractual non-compliance.",
        bold=True,
    )

    add_para(doc, "")
    add_simple_table(doc, [
        ("TM N2 Summary", "Count"),
        ("Closed", "3  (n+1 A/C, Process Calc unblocked items)"),
        ("Still open", "~20 observations  (including the 2 oldest critical items of the project)"),
    ])

    # ---- TM N3 ----
    doc.add_heading("Transmittal N3 — E7–E9 | Issued January 28, 2026", level=2)
    add_para(doc, "17 observations. BWW responded to 6 on February 16, and provided additional inline responses on February 17.", bold=False)
    add_para(doc, "")

    add_simple_table(doc, [
        ("OBS", "Subject", "BWW Response", "Status"),
        ("01", "Vibration transmitters — HP Pump + Turbochargers", "Confirmed per ET 5.5.7", "CLOSED"),
        ("02", "SEC calculation with energy recovery", "Not addressed", "Pending"),
        ("03", "VM-09-015 DN100 ANSI 900# manual actuation", "'Not a process relevant valve — ET 5.2.3 not applicable'", "TECHNICAL DISPUTE"),
        ("04", "DO — Module status signal (external)", "Requested clarification", "Clarification sent Feb 17 — BWW pending"),
        ("05", "DI — External enable signal", "Requested clarification", "Clarification sent Feb 17 — BWW pending"),
        ("06", "Pt-100 in HP Pump motor windings", "Confirmed per ET 5.3", "CLOSED"),
        ("07", "RTDs in CIP Pump bearings", "Confirmed per ET 5.1.4", "CLOSED"),
        ("08", "Pt-100 in CIP Pump motor", "Confirmed per ET 5.3", "CLOSED"),
        ("09", "Temperature switches (TSH) instead of 4-20mA+HART transmitters", "Not addressed", "Pending"),
        ("10", "Layout inherits duplicate TAG FIT", "Will correct when IL corrected", "Accepted (conditional)"),
        ("11", "Duplicate TAG FIT-09-001 in Instrument List", "Renumbered to FIT-09-002", "CLOSED"),
        ("12", "Duplicate TAGs in Valve List (3 valves)", "Not addressed", "Pending"),
        ("13", "Incorrect area codes in Valve List (VM/VE-07-xxx)", "Not addressed", "Pending"),
        ("14", "Equipment List vs P&ID discrepancies", "Not addressed", "Pending"),
        ("15", "VFD electrical variables as individual AI signals for SEC", "'Total system variables, not per individual VFD'", "INSUFFICIENT"),
        ("16", "DO module status in IO List", "See OBS-04", "Pending BWW"),
        ("17", "DI external enable in IO List", "See OBS-05", "Pending BWW"),
    ])

    add_para(doc, "")
    add_simple_table(doc, [
        ("TM N3 Summary", "Count", "Items"),
        ("Closed", "6", "OBS-01, 06, 07, 08, 10, 11"),
        ("Technical dispute", "1", "OBS-03 (VM-09-015)"),
        ("Insufficient", "1", "OBS-15 (VFD variables)"),
        ("Pending BWW (clarification sent)", "3", "OBS-04, 05, 16/17"),
        ("Not addressed", "6", "OBS-02, 09, 12, 13, 14"),
    ])

    # ---- TM N4 ----
    doc.add_heading("Transmittal N4 — E10–E11 | Issued February 5, 2026", level=2)
    add_para(doc, "10 observations. BWW responded to 5 on February 16.", bold=False)
    add_para(doc, "")

    add_simple_table(doc, [
        ("OBS", "Subject", "BWW Response", "Status"),
        ("01", "PLC specified at 60Hz (Chile = 50Hz)", "'PLC is dual-frequency 50/60Hz'", "Accepted (conditional) — requires updated document"),
        ("02", "A/C without n+1 configuration", "Will confirm 2nd unit per ET 5.1.11", "CLOSED"),
        ("03", "Missing A/C thermal calculation", "Will deliver document", "Accepted (conditional) — no delivery date"),
        ("04", "Modbus TCP Memory Map — 42 days overdue", "'Will review and address later'", "CRITICAL — no date, no commitment"),
        ("05", "Duplicate TAG FIT-09-001 in Cable Tray Layout", "Will correct when IL updated", "Accepted (conditional)"),
        ("06", "Missing vibration TX locations in Layout", "Refers to TM N3 OBS-01", "Accepted (conditional)"),
        ("07", "Missing Pt-100 motor locations in Layout", "Refers to TM N3 OBS-06/07/08", "Accepted (conditional)"),
        ("08", "HP Pump — 4 inconsistent power values (83/86/92/93 kW)", "'Will review and address later'", "DEFERRED — active procurement risk"),
        ("09", "UPS not in Control Architecture BOM", "'In deliverables, next revision'", "Committed — no date"),
        ("10", "Container 60ft — rejected Nov 2025, 92 days open", "'Current docs show 40ft for RO; CIP/chemicals outside'", "PARTIAL — no corrected documents"),
    ])

    add_para(doc, "")
    add_simple_table(doc, [
        ("TM N4 Summary", "Count", "Items"),
        ("Closed", "2", "OBS-02, (OBS-03 conditional)"),
        ("Accepted conditional", "4", "OBS-01, 05, 06, 07"),
        ("Critical / Deferred", "2", "OBS-04 (Modbus), OBS-08 (HP Pump power)"),
        ("Partial", "1", "OBS-10 (Container)"),
        ("Committed, no date", "1", "OBS-09 (UPS)"),
    ])

    # ---- Global summary ----
    doc.add_heading("Overall Summary — All Four Transmittals", level=2)
    add_simple_table(doc, [
        ("Status", "TM N1", "TM N2", "TM N3", "TM N4", "Total"),
        ("Closed / Approved", "18", "3", "6", "2", "29"),
        ("Accepted conditional", "—", "—", "1", "4", "5"),
        ("Technical dispute / Partial", "—", "—", "1", "1", "2"),
        ("Critical / Insufficient / Deferred", "2", "2", "1", "2", "7"),
        ("Pending BWW (clarification sent)", "—", "—", "3", "1", "4"),
        ("Not addressed / No revision since TM N2", "—", "~18", "5", "—", "~23"),
        ("TOTAL", "20", "~25", "17", "10", "~72"),
    ])

    doc.add_page_break()

    # ============================================================
    # BLOQUE 2 — PUNTOS A RESOLVER HOY
    # ============================================================
    doc.add_heading("ITEMS REQUIRING RESOLUTION TODAY", level=1)

    add_para(doc,
        "The following items are ordered by priority. Items P1 through P5 must be resolved "
        "or formally committed at this meeting. Items P6 through P11 require a concrete "
        "response before the next submittal cycle.",
    )
    add_para(doc, "")

    # P1
    doc.add_heading("P1 — Modbus TCP Memory Map", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N2 OBS-08 / TM N4 OBS-04"),
        ("Priority", "CRITICAL"),
        ("Days open", "42 days since commitment in TM N2 (January 6, 2026)"),
        ("BWW response Feb 17", "'We will review and address later'"),
        ("ADASA position",
         "Program has not started. This is the longest-standing unresolved commitment "
         "in the project. The Modbus Map is a prerequisite for ADASA's PLC-to-PLC interface design."),
        ("Required today", "Firm delivery date. No further deferral accepted."),
    ])

    add_para(doc, "")

    # P2
    doc.add_heading("P2 — Container 40ft Configuration", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N4 OBS-10"),
        ("Priority", "CRITICAL"),
        ("Days open", "92 days since ADASA formal rejection of 60ft proposal (November 17, 2025)"),
        ("BWW response Feb 17",
         "Technical position stated: RO system in 40ft; CIP and chemical dosing located outside. "
         "No corrected documents delivered."),
        ("ADASA position",
         "Technical position acknowledged as partial progress. However, no corrected engineering "
         "documents have been submitted since the rejection three months ago."),
        ("Required today", "Written confirmation of 40ft configuration + updated Container DS reflecting the approved design."),
    ])

    add_para(doc, "")

    # P3
    doc.add_heading("P3 — VM-09-015 Technical Dispute", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N3 OBS-03"),
        ("Priority", "CRITICAL"),
        ("Technical basis",
         "Valve DN100, ANSI 900#, located at HP Pump discharge. ET Section 5.2.3 requires "
         "electric actuation for process valves DN50+ at ANSI 900#."),
        ("BWW position Feb 17", "'Not a process relevant valve — ET 5.2.3 is not applicable.'"),
        ("ADASA position",
         "The valve is at HP Pump discharge. ADASA does not accept the exemption without "
         "written technical justification signed by BWW engineering."),
        ("Required today",
         "Confirmed answer: YES (change to electric) or NO (written technical justification "
         "per ET 5.2.3 submitted before next transmittal). Verbal responses are not sufficient."),
    ])

    add_para(doc, "")

    # P4
    doc.add_heading("P4 — DS HP Pump Rev C", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N1 (original rejection) / TM N3 OBS-06"),
        ("Priority", "CRITICAL"),
        ("History",
         "Originally rejected December 2025. Rev B submitted, verdict '3 - To be revised' "
         "due to missing Pt-100. BWW committed Pt-100 on February 17 but no Rev C submitted."),
        ("Required today", "Delivery date for Rev C including Pt-100 for motor windings and bearings per ET 5.3."),
    ])

    add_para(doc, "")

    # P5
    doc.add_heading("P5 — DS CIP Pump (Complete)", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N1 (original rejection)"),
        ("Priority", "CRITICAL"),
        ("History",
         "Originally rejected December 2025. Rev B submitted with partial corrections — "
         "approved with notes but without temperature instrumentation. "
         "A complete datasheet with Pt-100 (motor windings and bearings per ET 5.3) and "
         "RTDs (bearings per ET 5.1.4) has never been delivered."),
        ("BWW commitment Feb 17", "Verbally confirmed Pt-100 and RTDs. No document or date provided."),
        ("Required today", "Delivery date for complete CIP Pump datasheet with all temperature sensors specified."),
    ])

    add_para(doc, "")

    # P6
    doc.add_heading("P6 — HP Pump Power — 4 Inconsistent Values", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N4 OBS-08"),
        ("Priority", "MAJOR"),
        ("Values", "83 kW (Load List) / 86 kW (Technical Offer) / 92 kW (Equipment List) / 93 kW (Utility List)"),
        ("BWW response Feb 17", "'We will review and address later'"),
        ("ADASA position",
         "The motor power specification directly affects VFD sizing, cable dimensioning, "
         "and protection settings. PR/PO was scheduled for February 16 per BWW schedule. "
         "A single correct value must be established before procurement."),
        ("Required today", "Single unified value confirmed at this meeting."),
    ])

    add_para(doc, "")

    # P7
    doc.add_heading("P7 — VFD Electrical Variables as Individual AI Signals", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N2 OBS-09 / TM N3 OBS-15"),
        ("Priority", "MAJOR"),
        ("ADASA requirement",
         "Voltage, current, power, frequency and temperature from each VFD individually "
         "as AI signals in the IO List — required for SEC disaggregation and individual drive monitoring."),
        ("BWW response Feb 17",
         "'Will display SEC and total system electrical variables, not for individual consumers.'"),
        ("ADASA position",
         "Total system metrics do not satisfy individual VFD monitoring requirements. "
         "ADASA needs per-drive data to verify SEC calculation and diagnose performance deviations."),
        ("Required today", "Commitment to include individual AI signals per VFD in the revised IO List."),
    ])

    add_para(doc, "")

    # P8
    doc.add_heading("P8 — Static Mixer Material — PVC vs FRP", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N2 OBS-01"),
        ("Priority", "MAJOR"),
        ("Status",
         "Technical Offer specifies FRP. BWW proposed PVC without formal justification. "
         "BWW schedule shows manufacturing completed October–November 2025."),
        ("Risk",
         "If the mixer was manufactured in PVC without ADASA approval, this constitutes "
         "an active contractual non-compliance under Contract C-4300."),
        ("Required today",
         "Confirm material used. If PVC: written technical justification and mixing "
         "efficiency validation required immediately."),
    ])

    add_para(doc, "")

    # P9
    doc.add_heading("P9 — P&ID Revision B — 13 Observations Open Since TM N2", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "TM N2 — P&ID OBS-01 to 14 (except OBS-09 closed)"),
        ("Priority", "MAJOR"),
        ("Status",
         "No P&ID revision received since the document was submitted in December 2025. "
         "13 observations covering battery limits, material zones, line TAGs, "
         "instrumentation tags, flow directions and legend remain open."),
        ("Required today", "Inclusion of P&ID Rev B in the document delivery schedule with a specific date."),
    ])

    add_para(doc, "")

    # P10
    doc.add_heading("P10 — Document Delivery Schedule (30 Documents Pending)", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Priority", "HIGH"),
        ("Status", "BWW committed to deliver this schedule at today's meeting."),
        ("Scope",
         "15 documents not yet submitted + 14 requiring revision + DS HP Pump Rev C "
         "+ DS CIP Pump complete. Total: approximately 30 documents."),
        ("Required today", "Document-by-document schedule with specific delivery dates. No schedule = no coordination possible."),
    ])

    add_para(doc, "")

    # P11
    doc.add_heading("P11 — CT-001 Antiscalant — Response Deadline February 20", level=2)
    add_simple_table(doc, [
        ("Field", "Detail"),
        ("Reference", "P22-CT-09-000-001-1 — Issued February 16, 2026"),
        ("Priority", "HIGH — Deadline in 2 days"),
        ("Open observations (4)",
         "OBS-1: AWC projection at 19°C, worst-case is 24°C per ET Table 4-1. "
         "OBS-2: Chemical Consumption List volumetric inconsistency (0.02 vs 0.024 L/h). "
         "OBS-3: CREST Water denies heavy metals; ANAM Lab confirms Sr 10-11 mg/L. "
         "OBS-4: Contradictory conclusions between AWC and CREST Water assessments."),
        ("Required today",
         "Confirm BWW will respond before February 20. "
         "If not met: formal escalation per Plan Phase 2 (BAE Clause 49)."),
    ])

    doc.add_page_break()

    # ============================================================
    # BLOQUE 3 — COMPROMISOS A REGISTRAR
    # ============================================================
    doc.add_heading("COMMITMENTS TO BE RECORDED TODAY", level=1)

    add_para(doc,
        "The following table summarizes all commitments to be formally recorded at this meeting. "
        "Each item must be confirmed with a specific date or explicit written commitment.",
    )
    add_para(doc, "")

    add_simple_table(doc, [
        ("#", "Commitment", "Deadline", "Record As"),
        ("1", "Firm delivery date — Modbus TCP Memory Map", "To define today", "Formal written commitment"),
        ("2", "Updated Container DS confirming 40ft configuration", "To define today", "Formal written commitment"),
        ("3", "VM-09-015: electric actuation or written technical justification", "Next submittal", "Formal written commitment"),
        ("4", "DS HP Pump Rev C with Pt-100 (windings + bearings)", "To define today", "Formal written commitment"),
        ("5", "DS CIP Pump complete with Pt-100 + RTDs", "To define today", "Formal written commitment"),
        ("6", "Single unified HP Pump power value", "Next submittal", "Formal written commitment"),
        ("7", "VFD individual AI signals per drive in IO List", "Next submittal", "Formal written commitment"),
        ("8", "Static Mixer material confirmation + justification if PVC", "To define today", "Formal written commitment"),
        ("9", "P&ID Rev B delivery date (13 obs open since TM N2)", "Include in document schedule", "Formal written commitment"),
        ("10", "Document delivery schedule — all ~30 pending documents", "Today / by Friday at latest", "Formal written commitment"),
        ("11", "CT-001 — Response to 4 open observations", "February 20, 2026", "Contractual deadline"),
        ("12", "No POs before ADASA datasheet approval", "Permanent", "Already recorded February 17"),
    ])

    doc.add_page_break()

    # ============================================================
    # BLOQUE 4 — RIESGO DE LA REUNION
    # ============================================================
    doc.add_heading("MEETING RISK", level=1)

    add_para(doc,
        "BW Water confirmed the February 18 meeting but noted that the engineering team "
        "in Asia may not be available due to the Chinese New Year holiday. Eduardo Yamauchi "
        "indicated this could delay their participation by one day.",
        bold=False,
    )
    add_para(doc, "")
    add_para(doc,
        "If the meeting proceeds without direct technical representation from the Asia team: "
        "ADASA should request a second session this week with all responsible parties present. "
        "Items P1, P3, P7, and P9 cannot be resolved without the engineering team directly responsible.",
        bold=True,
    )
    add_para(doc, "")
    add_para(doc,
        "If no delivery plan or document schedule is presented at this meeting — as committed — "
        "ADASA should formally note the failure to deliver and initiate formal escalation procedures "
        "per BAE Clause 49 without further delay.",
    )

    # ============================================================
    # SAVE
    # ============================================================
    doc.save(OUTPUT)
    print(f"Documento generado exitosamente: {OUTPUT}")
    return OUTPUT


if __name__ == "__main__":
    crear_punteo()
