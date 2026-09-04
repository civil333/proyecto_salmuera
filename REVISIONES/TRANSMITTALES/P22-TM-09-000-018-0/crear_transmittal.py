#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N18 ADASA-BW_WATER.
Submittals 25007-0038 (Entrega 38), 25007-0039 (Entrega 39),
25007-0040 (Entrega 40) y 25007-0041 (Entrega 41).
Fecha: 18-May-2026

Veredicto global: 3 - TO BE REVISED (driven by Plant Control
Philosophy Rev C only — remaining 4 documents Code 1, sin
modificacion a si mismos; entregables residuales en Section 3)
Tally: 4 Code 1 + 0 Code 2 + 1 Code 3

Scope: 5 documentos
  E38 (25007-0038): Valve List Rev D, Line List Rev C
  E39 (25007-0039): Plant Control Philosophy Rev C
  E40 (25007-0040): AC Thermal Calculation Rev C
  E41 (25007-0041): Piping and Instrumentation Diagram Rev D

Adjuntos: 1 PDF CC_ADASA (solo Control Philosophy Rev C, Code 3).
Los 4 docs Code 1 no llevan CC_ADASA (regla section 3.8); sus entregables
residuales se trackean en Section 3.
"""

import sys
import os

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N18 ADASA-BW_WATER.docx")


def add_para(doc, runs):
    """runs es lista de (texto, kwargs) con kwargs en {'bold', 'italic'}."""
    para = doc.add_paragraph()
    for item in runs:
        text = item[0]
        attrs = item[1] if len(item) > 1 else {}
        run = para.add_run(text)
        if attrs.get("bold"):
            run.bold = True
        if attrs.get("italic"):
            run.italic = True
    aplicar_arial_12(para)
    return para


def add_bullet(doc, text):
    # Bullet nativo de Word con circulo negro, hanging indent
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


def main() -> None:
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N18 — SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-018-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # =========================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================
    doc.add_heading("1. EXECUTIVE SUMMARY", level=1)

    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — TO BE REVISED.", {"bold": True}),
        (" Five documents (submittals 25007-0038 to 25007-0041). Tally: "
         "4 Code 1, 1 Code 3. Driven solely by Plant Control Philosophy "
         "Rev C; the other four are approved as-is, residual deliverables "
         "tracked in Section 3.",),
    ])

    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    add_bullet(doc, (
        "Plant Control Philosophy Rev C — Code 3. Re-issue as Rev D — "
        "the only document requiring a new revision."
    ))
    add_bullet(doc, (
        "Valve List Rev D — Code 1. Table accepted; PSV-09-002 "
        "overpressure analysis tracked in Section 3."
    ))
    add_bullet(doc, (
        "Line List Rev C — Code 1. Closes the two outstanding "
        "Transmittal N12 notes."
    ))
    add_bullet(doc, (
        "AC Thermal Calculation Rev C — Code 1. Closes Transmittal N15 "
        "NOTE-02; explicit effective-margin statement tracked in "
        "Section 3."
    ))
    add_bullet(doc, (
        "P&ID Rev D — Code 1. Closes Transmittal N13 NOTE-01; CIT-09-004 "
        "change tracked as Instrument List / Line List deliverables "
        "(Section 3)."
    ))

    add_para(doc, [(
        "Why Code 3 — Plant Control Philosophy Rev C:", {"bold": True})])
    add_bullet(doc, (
        "HP Pump start permissive still defective (repeat CRITICAL). "
        "Still reads 'VE-09-007 and VE-09-007' (not corrected to "
        "VE-09-008) and requires 'VE-09-014 fully CLOSED'; VE-09-014 is "
        "the antiscalant tank inlet valve, so the PLC inhibits HP Pump "
        "start during routine refill. Same defect as Transmittal N15 "
        "NOTE-20 — second consecutive transmittal. Blocking condition "
        "for closure; recorded for contractual follow-up under Contract "
        "C-4300."
    ))
    add_bullet(doc, (
        "Core control logic in undelivered child documents. Sequence "
        "Charts, Alarm & Control Setpoint List and Control Matrix remain "
        "'SEPARATE DOCUMENT'; the tentative 13-May-2026 date passed. "
        "Deliver them with formal codes, revisions and a binding date "
        "prior to IFC."
    ))

    add_para(doc, [(
        "Eleven prior-transmittal observations remain open (LCP "
        "Datasheet Rev A, Cable Tray Rev C, HMI Screenshots) — Section 3 "
        "details the inventory.",
    )])

    # =========================================================
    # 2. OBSERVATIONS BY DOCUMENT
    # =========================================================
    doc.add_heading("2. OBSERVATIONS BY DOCUMENT", level=1)

    # ---------- 2.1 Plant Control Philosophy Rev C ----------
    doc.add_heading(
        "2.1 Plant Control Philosophy Rev C — P22-BT-09-009-001", level=2)
    add_para(doc, [("Response Code: 3 — To be revised", {"bold": True})])
    add_para(doc, [(
        "Resubmittal against Transmittal N15 Section 2.10 (Rev B, "
        "Code 3, seventeen findings including one CRITICAL). The "
        "document now includes a Consolidated Comment Sheet and grew to "
        "59 pages. Six findings are closed and several substantially "
        "addressed, but the CRITICAL permissive defect persists and core "
        "control logic remains deferred to child documents not delivered "
        "with this submittal. Detailed comments: "
        "P22-BT-09-009-001_C_Control_Philosophy_CC_ADASA.pdf.",
    )])
    add_simple_table(doc, [
        ("ID", "Severity", "Topic"),
        ("OBS-01", "CRITICAL",
         "HP Pump start permissive uncorrected — VE-09-007 still "
         "duplicated; VE-09-014 (antiscalant tank inlet) still required "
         "CLOSED"),
        ("OBS-02", "MAJOR",
         "Core control logic deferred to undelivered child documents "
         "(Sequence Charts, Alarm & Control Setpoint List, Control "
         "Matrix)"),
        ("OBS-03", "MAJOR",
         "Salt Rejection formula still references Stage-2 reject "
         "conductivity instead of feed conductivity"),
        ("NOTE-01", "MAJOR",
         "SEC energy measured at the RO PLC panel power meter — wrong "
         "electrical bus, not corrected"),
        ("NOTE-02", "MAJOR",
         "SEC contractual value misaligned — two-band 4.8/5.0 kWh/m³ vs "
         "Technical Offer Rev1 single 4.71 kWh/m³ ±5%"),
        ("NOTE-03", "MINOR",
         "Documentary — duplicate group-table row '11' (VE-09-006 / "
         "VE-09-007); VE-09-007 described inconsistently"),
    ])
    add_para(doc, [
        ("OBS-01 — HP Pump start permissive uncorrected. ",
         {"bold": True}),
        ("The High-Pressure Pump start permissive list still reads "
         "'Turbocharger isolation valve VE-09-007 and VE-09-007 "
         "AVAILABLE and NOT FAULT' — the duplicated TAG flagged in "
         "Transmittal N15 NOTE-20 has not been corrected to the second "
         "isolation valve (VE-09-008). The list also still requires "
         "'VE-09-014 is fully CLOSED'. Rev C's own text defines "
         "VE-09-014 as the antiscalant dosing tank inlet motorized "
         "valve that 'opens when the tank level reaches a low-level "
         "condition' for automatic refill. Used literally by the PLC, "
         "the permissive prevents the HP Pump from starting whenever "
         "the antiscalant tank is refilling — a routine operating "
         "condition. This is the same defect raised as CRITICAL in "
         "Transmittal N15 (NOTE-20), now in its second consecutive "
         "transmittal. Correct the duplicated TAG and remove the "
         "antiscalant tank inlet valve from the HP Pump permissive, "
         "reconciling the full permissive against P&ID Rev D "
         "(Section 2.5) and Valve List Rev D in Rev D. Because the same "
         "defect was raised as "
         "CRITICAL in Transmittal N15 (NOTE-20) and remains uncorrected "
         "one revision later, its resolution in Rev D is a blocking "
         "condition for closure of the Plant Control Philosophy; the "
         "repeated CRITICAL is recorded for contractual follow-up under "
         "Contract C-4300.",),
    ])
    add_para(doc, [
        ("OBS-02 — Core control logic deferred to undelivered child "
         "documents. ", {"bold": True}),
        ("Section 1.5/3.3/3.6 reference the RO Control & Sequence "
         "Chart, RO Flushing Sequence Chart, CIP Sequence Chart, Alarm "
         "& Control Setpoint List and Control Matrix as 'SEPARATE "
         "DOCUMENT'. The Consolidated Comment Sheet answers several "
         "findings with 'to submit along with sequence chart (May 13 - "
         "Tentative) for review', but submittal 25007-0039 contains the "
         "Control Philosophy alone and the tentative date has passed. "
         "As a consequence the salt-rejection formula (OBS-03), the CIP "
         "interface valve phase sequence, the VE-09-002 modulating "
         "algorithm finalisation, the off-spec routing "
         "position-confirmation interlock and the turbocharger-bypass "
         "cross-check are all described in narrative form only and "
         "their numerical implementation is deferred. Provide the "
         "Sequence Charts, the Alarm & Control Setpoint List and the "
         "Control Matrix with formal document codes, revisions and a "
         "binding delivery date prior to IFC; the Control Philosophy "
         "cannot be closed while its operative logic resides in "
         "undelivered documents.",),
    ])
    add_para(doc, [
        ("OBS-03 — Salt Rejection formula. ", {"bold": True}),
        ("The overall salt-rejection expression still divides by the "
         "Stage-2 reject conductivity rather than the feed "
         "conductivity. Per ASTM D4516 and standard membrane-projection "
         "practice, salt rejection uses feed conductivity (CIT-09-001B) "
         "in the denominator. The Consolidated Comment Sheet defers "
         "correction to the sequence chart; the formula must be "
         "corrected in the Control Philosophy body in Rev D, since it "
         "defines the performance metric displayed on the HMI.",),
    ])
    add_para(doc, [
        ("NOTE-01 — SEC energy measurement bus. ", {"bold": True}),
        ("Section 1.4 still takes Total Energy Consumed as a 'Parameter "
         "from RO PLC panel power meter'. That meter measures the PLC, "
         "UPS and control gear only, not the ~85 kW HP Pump motor that "
         "dominates specific energy consumption. The Consolidated "
         "Comment Sheet adds the assertion that the value 'represents "
         "the total RO system energy consumption within the defined "
         "battery limits' but the metering point is not relocated. "
         "Either move the measurement to the MCC main breaker "
         "(capturing the loads within the SEC scope of Technical Offer "
         "Rev1) or specify explicitly the set of meters whose sum is "
         "divided by the FIT-09-003 totalizer.",),
    ])
    add_para(doc, [
        ("NOTE-02 — SEC contractual value. ", {"bold": True}),
        ("Section 1.4 retains two TDS-banded targets (< 4.8 kWh/m³ for "
         "TDS 43,000–48,000 mg/L; < 5.0 kWh/m³ for TDS 48,000–53,000 "
         "mg/L). Technical Offer Rev1 guarantees a single SEC of 4.71 "
         "kWh/m³ ±5% with no TDS banding. The clarification that these "
         "are performance targets and not trip setpoints is "
         "acknowledged, but the numerical divergence from the "
         "contractual guarantee remains. Reconcile the displayed/"
         "evaluated value with the Technical Offer Rev1 guarantee in "
         "Rev D.",),
    ])
    add_para(doc, [
        ("NOTE-03 — Documentary quality. ", {"bold": True}),
        ("The group instrument table carries two rows numbered '11' "
         "(VE-09-006 RO Reject Flow Control Valve and VE-09-007), and "
         "VE-09-007 is described both as 'Turbocharger Isolation Valve' "
         "and elsewhere as 'Interstage Isolation Valve'. Resolve the "
         "numbering and use one consistent description per TAG in Rev D. "
         "Closure of Transmittal N15 NOTE-14 (vibration setpoints "
         "4.5/7.1 mm/s RMS), NOTE-15 (antiscalant flow reference "
         "FIT-09-001), NOTE-18 (motor RTD thresholds), NOTE-19 (feed "
         "turbocharger isolation), NOTE-21 (Stage-2 permeate "
         "FIT-09-002), NOTE-23 (orphan TAGs restored to the tables) and "
         "the Consolidated Comment Sheet inclusion is acknowledged.",),
    ])

    # ---------- 2.2 Valve List Rev D ----------
    doc.add_heading(
        "2.2 Valve List Rev D — P22-LI-09-005-002", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [(
        "The valve table is the same Rev D (dated 18-Mar-2026, 111 "
        "items) approved as Code 2 in Transmittal N14, where TAG "
        "uniqueness was verified across all items against P&ID Rev C. "
        "The submittal adds a Consolidated Comment Sheet (dated "
        "27-Apr-2026) responding to Transmittal N14. The table content "
        "is unchanged and requires no modification; the Valve List is "
        "approved as-is. The only open item is a separate process-safety "
        "deliverable, not a change to this list.",
    )])
    add_para(doc, [(
        "Transmittal N14 raised that the second PSV-09-002 was removed "
        "(item count 112 → 111) rather than assigned a unique TAG, and "
        "requested an overpressure protection analysis confirming the "
        "remaining PSV configuration is adequate. The Consolidated "
        "Comment Sheet states only that 'PSV-09-002 is already included "
        "in Revision C of the list under Item 104' — this confirms a "
        "single device exists but does not demonstrate adequacy. Because "
        "the relief-sizing analysis is a separate deliverable (not a "
        "modification of the Valve List), it is tracked in Section 3 for "
        "IFC Rev 0; it does not hold the Valve List in Code 2. For the "
        "record: Transmittal N14 comments were answered by re-issuing "
        "the same Rev D with an appended Consolidated Comment Sheet — "
        "future responses should advance the revision letter when "
        "content changes rather than re-issue the same revision.",
    )])
    add_para(doc, [
        ("Action: none on this document — accepted; issue directly at "
         "IFC Rev 0. ", {"bold": True}),
        ("Related deliverables tracked in Section 3: PSV-09-002 "
         "overpressure / relief sizing analysis (protected volume, "
         "relief scenario, set pressure, required vs installed relief "
         "capacity).",),
    ])

    # ---------- 2.3 Line List Rev C ----------
    doc.add_heading(
        "2.3 Line List Rev C — P22-LI-09-009-003", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [(
        "Rev C (dated 5-May-2026) closes both outstanding Transmittal "
        "N12 notes. No new observations. No annotated PDF is issued for "
        "this document.",
    )])
    add_bullet(doc, (
        "Transmittal N12 NOTE-01 — CLOSED. The 'MAKE-UP FOR CIP' line, "
        "previously without identifier, is assigned PE-PVC-DN80-09-019, "
        "consistent with the project numbering convention. The "
        "Consolidated Comment Sheet confirms 'BW has revised "
        "accordingly'."
    ))
    add_bullet(doc, (
        "Transmittal N12 NOTE-02 — CLOSED. All Super Duplex Steel lines "
        "are now designated 'SUPER DUPLEX STEEL, SCH80S' per ASME "
        "B36.19M; PVC lines remain Schedule 80 (correct). This note was "
        "tracked for IFC Rev 0 and has been corrected ahead of IFC at "
        "Rev C."
    ))
    add_para(doc, [(
        "Pressures are internally consistent (e.g. DA-SSD-DN80-09-005, "
        "1st Stage RO Reject: operating 68 bar, design 80 bar — margin "
        "17.6%). High-pressure lines are Super Duplex SCH80S; "
        "low-pressure lines are PVC SCH80.",
    )])
    add_para(doc, [(
        "Action: none — accepted; issue directly at IFC Rev 0.",
        {"bold": True})])

    # ---------- 2.4 AC Thermal Calculation Rev C ----------
    doc.add_heading(
        "2.4 AC Thermal Calculation Rev C — P22-CD-09-005-002", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [(
        "The calculation is the same Rev C approved as Code 2 in "
        "Transmittal N15 (which closed Transmittal N2 OBS-02). The "
        "submittal adds a Consolidated Comment Sheet responding to "
        "Transmittal N15 NOTE-02. The heat-load calculation (6.24 kW = "
        "1.774 TR), the 15% design margin (→ 2.04 TR) and the selected "
        "unit (2.5 HP ≈ 2.01 TR) are correct, and the Consolidated "
        "Comment Sheet confirms each unit carries 100% of the load with "
        "the partner in standby (1 duty + 1 standby). The selected "
        "2.01 TR unit exceeds the un-margined computed peak demand "
        "(1.774 TR) by 13.3%, so the calculation is adequate and "
        "requires no modification — the document is approved as-is. n+1 "
        "is confirmed.",
    )])
    add_para(doc, [(
        "The Consolidated Comment Sheet phrase 'this 0.03 TR difference "
        "is within the applied design margin' is imprecise — the 0.03 "
        "TR is the erosion of the 15% target margin, not a quantity "
        "within it — but it does not change the result. So that the "
        "design basis is auditable, the effective post-selection margin "
        "should be stated explicitly at IFC Rev 0 (selected 2.01 TR vs "
        "computed peak 1.774 TR = +13.3%). This is a traceability "
        "statement, not a calculation error, and is tracked in "
        "Section 3.",
    )])
    add_para(doc, [
        ("Action: none on this document — accepted; issue directly at "
         "IFC Rev 0. ", {"bold": True}),
        ("Related deliverables tracked in Section 3: state the effective "
         "post-selection margin explicitly (2.01 TR vs 1.774 TR = "
         "+13.3%) at IFC Rev 0.",),
    ])

    # ---------- 2.5 P&ID Rev D ----------
    doc.add_heading(
        "2.5 Piping and Instrumentation Diagram Rev D — "
        "P22-DWG-09-009-002", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [(
        "Rev D follows Rev C (Code 2 in Transmittal N13). It closes the "
        "single outstanding ADASA observation on the P&ID and the "
        "drawing itself requires no modification — the P&ID is approved "
        "as-is.",
    )])
    add_para(doc, [
        ("Transmittal N13 NOTE-01 — CLOSED. ", {"bold": True}),
        ("The CIP Tank TK-09-001 6.81 m³ / 6.1 m³ discrepancy is "
         "resolved: the two figures are the total geometric volume "
         "(6.8 m³, from tank dimensions) and the effective usable "
         "volume (6.1 m³, the Equipment List value); the same "
         "distinction applies to the Antiscalant Dosing Tank "
         "(0.34 / 0.27 m³). Rev D annotates both values. The "
         "explanation is technically consistent for the HDPE tank "
         "geometry and no Equipment List Rev C is required.",),
    ])
    add_para(doc, [(
        "The Consolidated Comment Sheet records a BW Water-initiated "
        "change: an orifice plate and a needle valve added upstream of "
        "the interstage conductivity analyzer CIT-09-004 to reduce line "
        "pressure and protect the sensor. The protection intent is "
        "sound. The change does not bear on the P&ID's acceptance — it "
        "is reflected on the supporting lists. Because it affects an "
        "instrument feeding the interstage salt-rejection indicator "
        "(see Section 2.1 OBS-03), it is tracked in Section 3 as a "
        "deliverable on the Instrument List and Line List, not as a "
        "P&ID note. The remaining Consolidated Comment Sheet entries "
        "(pressure-gauge diaphragm seals, container area limits, CIP "
        "Tank manhole size) are accepted as documented.",
    )])
    add_para(doc, [
        ("Action: none on this document — accepted; issue directly at "
         "IFC Rev 0. ", {"bold": True}),
        ("Related deliverables tracked in Section 3: dual-value "
         "annotation consistency with the CIP Tank datasheet and "
         "Equipment List; CIT-09-004 reflected in Instrument List Rev D "
         "and Line List Rev C, plus a short engineering note on loop "
         "response.",),
    ])

    # =========================================================
    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    # =========================================================
    doc.add_heading(
        "3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    add_para(doc, [(
        "Items open as of 18-May-2026. Transmittal N15 Section 2.10 "
        "(Plant Control Philosophy Rev B) is no longer listed here — it "
        "is re-dispositioned in Section 2.1 of this transmittal "
        "following the Rev C resubmittal.",
    )])

    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Outstanding", "Status"),
        ("TM N4 OBS-06",
         "Cable Tray Layout (P22-DWG-09-007-004)",
         "Vibration transmitter locations missing",
         "101 days",
         "OPEN — awaiting Rev C, also subject of TM N15"),
        ("TM N4 OBS-07",
         "Cable Tray Layout (P22-DWG-09-007-004)",
         "Pt-100 motor sensor locations missing",
         "101 days",
         "OPEN — awaiting Rev C, also subject of TM N15"),
        ("TM N4 NOTE-05",
         "HMI Screenshots (P22-BREAD-09-008-001)",
         "Committed at TM N4 — never submitted",
         "102 days",
         "OPEN — formal commitment outstanding"),
        ("TM N5 OBS-02",
         "Equipment Layout (P22-DWG-09-005-003)",
         "Imperial dimensions retained as primary on Rev 0",
         "83 days",
         "PARTIALLY OPEN"),
        ("TM N10 OBS-05",
         "GA Antiscalant Dosing Tank",
         "Working volume, body material, seismic anchor data",
         "66 days",
         "OPEN — GA Rev B still required"),
        ("TM N11 OBS-03",
         "Grounding Layout (P22-DWG-09-007-003)",
         "Grounding schedule completeness (PE identifiers, conductor "
         "cross-section, ring main topology, equipotential bonding per "
         "NCh Eléct. 4/2003 Section 10.0)",
         "61 days",
         "OPEN — Rev D does not include the schedule"),
        ("TM N13 NOTE-02",
         "Cable Tray Layout drawings",
         "Internal cable routing not submitted",
         "41 days",
         "OPEN — tracked in ADASA email 10-Apr-2026"),
        ("TM N15 Section 2.4",
         "LCP Datasheet Rev A (P22-ET-09-007-005)",
         "Code 3 — three OBS open (I/O modules + RTD channel count, IP "
         "rating, power consumption inconsistency)",
         "25 days",
         "OPEN — Rev B awaited"),
        ("TM N15 Section 2.8",
         "Cable Tray Layout Rev B (P22-DWG-09-007-004)",
         "Code 3 — five new OBS plus two from TM N4",
         "25 days new / 101 days inherited",
         "OPEN — Rev C awaited"),
        ("TM N16 NOTE-01",
         "Civil and Loading Drawing Rev A (P22-DWG-09-005-001)",
         "Modified container weight + RO Skid weight breakdown "
         "disclosure",
         "23 days",
         "TRACKED for Rev 0 IFC (Code 2 — no new revision required)"),
    ])

    add_para(doc, [("Closed in this transmittal:", {"bold": True})])
    add_bullet(doc,
               "TM N12 NOTE-01 — Line List unassigned line identifier "
               "(closed by Line List Rev C, Section 2.3)")
    add_bullet(doc,
               "TM N12 NOTE-02 — Line List SCH 80S designation (closed "
               "by Line List Rev C, Section 2.3; previously tracked for "
               "IFC Rev 0)")
    add_bullet(doc,
               "TM N15 NOTE-02 — AC Thermal capacity margin and n+1 "
               "(closed by AC Thermal Calculation Rev C, Section 2.4)")
    add_bullet(doc,
               "TM N13 NOTE-01 — P&ID CIP Tank capacity (closed by "
               "P&ID Rev D, Section 2.5: resolved as total 6.8 m³ vs "
               "effective 6.1 m³, both annotated; the dual-value "
               "consistency check is carried to IFC Rev 0, see the "
               "tracked list below)")

    add_para(doc, [(
        "Tracked for IFC Rev 0 (incorporate at IFC; the documents "
        "reviewed in this transmittal require no further revision — "
        "these are deliverables on related documents or separate "
        "analyses):", {"bold": True})])
    add_bullet(doc,
               "TM N16 NOTE-01 — Civil and Loading Drawing Rev A: "
               "modified container weight + RO Skid weight breakdown "
               "disclosure")
    add_bullet(doc,
               "Valve List residual — PSV-09-002 overpressure / relief "
               "sizing analysis (protected volume, relief scenario, set "
               "pressure, required vs installed relief capacity) for the "
               "removed second PSV-09-002")
    add_bullet(doc,
               "P&ID residual — CIT-09-004 orifice plate + needle valve "
               "reflected in Instrument List Rev D and Line List Rev C, "
               "plus a short engineering note confirming no measurement "
               "lag or dead-leg on the interstage salt-rejection "
               "indicator")
    add_bullet(doc,
               "P&ID CIP Tank dual-value convention — confirm the P&ID "
               "dual annotation (6.8 m³ total / 6.1 m³ effective; "
               "Antiscalant Dosing Tank 0.34 / 0.27 m³) is consistent "
               "with the CIP Tank datasheet and the Equipment List "
               "(residual of TM N13 NOTE-01)")
    add_bullet(doc,
               "AC Thermal Calculation — state the effective "
               "post-selection margin explicitly (selected 2.01 TR vs "
               "computed peak 1.774 TR = +13.3%) for design-basis "
               "traceability")

    # =========================================================
    # 4. ATTACHMENTS
    # =========================================================
    doc.add_heading("4. ATTACHMENTS", level=1)

    add_simple_table(doc, [
        ("Document", "Annotated File", "Annotations"),
        ("Plant Control Philosophy Rev C",
         "P22-BT-09-009-001_C_Control_Philosophy_CC_ADASA.pdf",
         "OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02, NOTE-03"),
    ])

    add_para(doc, [(
        "Only the Code 3 document carries an annotated PDF. The four "
        "Code 1 — Approved documents (Valve List Rev D, Line List Rev C, "
        "AC Thermal Calculation Rev C, P&ID Rev D) require no "
        "modification to themselves and carry no annotated PDF; their "
        "residual deliverables are listed in Section 3.",
    )])

    # =========================================================
    # 5. RESPONSE SUMMARY
    # =========================================================
    doc.add_heading("5. RESPONSE SUMMARY", level=1)

    add_simple_table(doc, [
        ("Document Code", "Title", "Rev", "Response Code"),
        ("P22-BT-09-009-001", "Plant Control Philosophy", "C",
         "3 — To Be Revised"),
        ("P22-LI-09-005-002", "Valve List", "D",
         "1 — Approved"),
        ("P22-LI-09-009-003", "Line List", "C",
         "1 — Approved"),
        ("P22-CD-09-005-002", "AC Thermal Calculation", "C",
         "1 — Approved"),
        ("P22-DWG-09-009-002", "Piping and Instrumentation Diagram", "D",
         "1 — Approved"),
    ])

    add_para(doc, [(
        "Overall Transmittal Verdict: 3 — TO BE REVISED (driven by "
        "Plant Control Philosophy Rev C — the remaining four documents "
        "are Code 1 — Approved, requiring no modification to themselves; "
        "their residual deliverables for IFC Rev 0 are tracked in "
        "Section 3)",
        {"bold": True})])

    doc.save(OUTPUT)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
