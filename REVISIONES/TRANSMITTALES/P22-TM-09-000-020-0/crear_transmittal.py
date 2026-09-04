#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N20 ADASA-BW_WATER.
Submittals 25007-0046 (E46, 28-May-2026) + 25007-0047 (E47, 09-Jun-2026).
Fecha emision: 10-Jun-2026 (miercoles).

Veredicto global: 3 - TO BE REVISED. Tally: 8 Code 1 + 7 Code 2 +
5 Code 3 = 20 documentos. Drivers Code 3: Section 2.4 Alarm & Interlock
Rev B, Section 2.6 PLC-LCP Outline Rev A (gate fabricacion panel),
Section 2.13 I/O List Rev 2 (reversion contractual), Section 2.14 IC
Cable Schedule Rev 1, Section 2.17 NDE Plan Rev A.

Adjuntos: 12 PDFs CC_ADASA (5 Code 3 + 7 Code 2).

Fuente unica de contenido: P22-TM-09-000-020-0_TRANSMITTAL.md.
Numeracion: SIN numeros manuales en add_heading() — el template ADASA
auto-numera H1 y H2.
"""

import os
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document  # noqa: E402


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N20 ADASA-BW_WATER.docx")


def add_para(doc, runs):
    """runs: lista de (texto,) o (texto, {bold, italic})."""
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
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


# ---------------------------------------------------------------------------
# Section 2 content (data-driven). Cada entrada:
# heading, code_line, paras (lista de str o lista de runs),
# obs (filas tabla ID/Severity/Topic) opcional, action (runs).
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="Instrument List Rev E — P22-LI-09-008-003",
        code="Response Code: 1 — Approved",
        paras=[
            "Resubmittal of Rev D (Code 2 in TM N17). Rev E closes the "
            "four open items. The Wilcoxon range question is resolved "
            "on the rms basis: vendor full-scale 12.7 mm/s peak "
            "converts to 8.9 mm/s rms, consistent with the “mm/s rms” "
            "unit on items 7, 18 and 19. The material-upgrade "
            "procurement impact is confirmed in writing as nil on the "
            "Consolidated Comment Sheet, the vibration transmitter "
            "working-medium cells now read “-”, and the Comment Sheet "
            "header references the correct 25007 Taltal project. "
            "Instrument count unchanged at 38.",
        ],
        action=[
            ("Action: none on this document — accepted; issue directly "
             "at IFC Rev 0.", {"bold": True}),
            (" Related item tracked in Section 3: written confirmation "
             "of the TIT-09-006 span configuration. The declared "
             "instrument range (0 to 600 Celsius, against a CIP "
             "operating range of 0 to 100 Celsius) is plausible as the "
             "Pt100 element range and appears consistently in the Data "
             "Transfer List and the Alarm & Interlock List.",),
        ],
    ),
    dict(
        heading="Data Transfer List (Modbus TCP/IP) Rev 1 — P22-LI-09-008-004",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "Resubmittal of the Rev 0 IFC issue (Code 2 in TM N17). "
            "Rev 1 closes both prior notes. The new Commissioning "
            "Reference header declares ADASA as Modbus master and the "
            "BW RO PLC as slave, floating-point format Big-Endian "
            "(AB-CD), word and byte swap OFF, and the PLC IP address. "
            "The vibration register scaling matches the rms basis "
            "accepted on the Instrument List.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Register 30019 (item 143, CIT09-002) declares scale 0 to "
             "20 uS/cm — a span that cannot represent the 200 to 1000 "
             "uS/cm permeate service nor the Alarm List setpoints (AHH "
             "800 uS/cm). The instrument span is 0 to 20000 uS/cm (0 to "
             "20 mS/cm per Instrument List Rev E). Register 30021 (item "
             "145, CIT09-003, 0 to 20 mS/cm) is numerically consistent "
             "but uses a different unit convention than the Alarm & "
             "Interlock List"),
            ("NOTE-01", "MINOR",
             "Register for TIT09-006 (item 152) declares 0 to 600 "
             "Celsius — confirm the intended span (same question as "
             "Section 2.1 tracked item)"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new Data Transfer List "
             "revision required:", {"bold": True}),
            (" harmonise registers 30019 and 30021 to a single declared "
             "conductivity span and unit (0 to 20000 uS/cm, or 0 to 20 "
             "mS/cm) consistent with the Alarm & Interlock List "
             "setpoint basis, and confirm the TIT09-006 span.",),
        ],
    ),
    dict(
        heading="Pressure Transmitter Datasheet Rev C — P22-LI-09-008-012",
        code="Response Code: 1 — Approved",
        paras=[
            "Resubmittal of Rev B (Code 2 in TM N17). Rev C closes both "
            "items: the Hastelloy C scope is confirmed for PIT-09-001 "
            "through 008 with PIT-09-009 retained in SS316L, the "
            "procurement impact is confirmed in writing as nil, and the "
            "implausible “Sealing: Aluminium” entry is resolved — the "
            "row was mislabelled and now reads “Material - Diaphragm”, "
            "with Aluminium correctly confined to the housing. Ranges "
            "and tags cross-check clean against the Instrument List "
            "Rev E. Schneider Foxboro IGP05S, 4-20 mA HART, IP66/IP67, "
            "NEMA 4X, SIL3 retained.",
        ],
        action=[
            ("Action: none — accepted; issue directly at IFC Rev 0.",
             {"bold": True}),
        ],
    ),
    dict(
        heading="Alarm & Interlock List Rev B — P22-LI-09-008-015",
        code="Response Code: 3 — To be revised",
        paras=[
            "Resubmittal of Rev A (Code 3 in TM N17). Rev B closes the "
            "two CRITICAL observations (permeate conductivity "
            "reconciled to uS/cm with setpoints inside the permeate "
            "band; LS-09-002 corrected to the LSL convention), "
            "harmonises the turbocharger vibration trip actions, and "
            "adds the digital-alarms section (items 34 to 51). The "
            "revision is nevertheless not consistent with the companion "
            "lists of the same deliveries. Detailed annotations on "
            "P22-LI-09-008-015_B_Alarm_Interlock_List_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Winding/bearing sensor assignment swapped against the "
             "Instrument List Rev E on both pump trains: this list "
             "declares TE-09-001 as Bearing (trip 90 C) and TE-09-002 "
             "as Winding (trip 140 C), the Instrument List declares the "
             "inverse — same swap on TE-09-003/004 (CIP). With "
             "different trip setpoints per sensor, the interlock acts "
             "on the wrong element"),
            ("OBS-02", "MAJOR",
             "TM N17 note on the bearing trip setpoint not applied: the "
             "Comment Sheet records the motor vendor confirmation to "
             "raise AHH to 95 C, yet item 27.1 retains 90.0 C"),
            ("OBS-03", "MAJOR",
             "CIP/Flush pH analyzer tagged PHIT-09-001 (item 25); the "
             "Instrument List Rev E and the Data Transfer List tag the "
             "same instrument PHIT-09-006"),
            ("NOTE-01", "MINOR",
             "CIP Tank temperature transmitter tagged TIT-09-005 (item "
             "23) against TIT-09-006 in the Instrument List Rev E"),
            ("NOTE-02", "MINOR",
             "LIT-09-002 instrument range declared 0 to 10 m with "
             "setpoints in percent (95/90/30/15) — declare the basis or "
             "use one unit"),
        ],
        action=[
            ("Action — re-issue as Rev C:", {"bold": True}),
            (" reconcile the TE-09-001/002 and TE-09-003/004 "
             "winding/bearing assignments across the Instrument List, "
             "the I/O List and the motor vendor documentation; apply "
             "the confirmed 95 C bearing AHH setpoint; align the pH and "
             "CIP Tank temperature tags with the Instrument List Rev E; "
             "and declare the level setpoint basis. Closure threshold: "
             "Rev C consistent with the Instrument List Rev E and with "
             "Plant Control Philosophy Rev D once delivered.",),
        ],
    ),
    dict(
        heading="Datasheet of Local Control Panel (LCP) Rev B — P22-ET-09-007-005",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "Resubmittal of Rev A (Code 3 in TM N15). Rev B closes the "
            "two MAJOR observations. The enclosure is now fully "
            "specified at panel level: nVent Hoffman Type FS FS66S, "
            "Stainless Steel 316L, NEMA 4X/IP66, UL508A/IEC 60529, "
            "ambient classification for harsh and highly corrosive "
            "environments. The I/O module configuration is also "
            "declared: two 5069-IY4 universal analog modules provide "
            "the eight RTD-capable channels required for the motor "
            "Pt-100 inputs, wired three-wire on the RTD1/RTD2 terminal "
            "strips per the PLC/LCP Schematic Diagram. Detailed "
            "annotations on "
            "P22-ET-09-007-005_B_LCP_Datasheet_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MINOR",
             "Total panel power consumption still not declared at panel "
             "level (TM N15 third observation, partially closed): the "
             "Electrical Load List Rev 0 carries SAI-09-001 at 2.0 kW; "
             "the datasheet should state the design consumption that "
             "supports it"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new LCP Datasheet "
             "revision required:", {"bold": True}),
            (" declare the total panel power consumption. This "
             "datasheet governs the enclosure specification; the "
             "Outline Panel Drawing must align to it (Section 2.6).",),
        ],
    ),
    dict(
        heading="PLC-LCP Outline Panel Drawing Rev A — P22-CD-09-008-001",
        code="Response Code: 3 — To be revised",
        paras=[
            "First submittal, flagged as fabrication-urgent by BW Water "
            "on 10-Jun-2026. The dimensional definition is complete and "
            "consistent (1000+800 W x 600 D x 2000 H mm, double front "
            "door, verified against the sheet-3 views), and the MCC and "
            "PLC bills of material are sound. The blocking defect is "
            "the Panel Specification Sheet on sheet 2, which specifies "
            "a different enclosure than the LCP Datasheet Rev B of the "
            "same submittal. Detailed annotations on "
            "P22-CD-09-008-001_A_Outline_Panel_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "CRITICAL",
             "Panel Specification Sheet declares MATERIAL “SHEET "
             "STEEL” painted GRAY RAL 7035 with zinc-plated mounting "
             "and gland plates, CRS hinges and SUS316L plinth only, and "
             "PROTECTION CLASS IP55 — contradicting the LCP Datasheet "
             "Rev B (FS66S, Stainless Steel 316L unpainted, NEMA "
             "4X/IP66, highly corrosive ambient), the IFC Single Line "
             "Diagram label (“METAL CLAD, NEMA4X/IP66”) and the "
             "Technical Specification — Constructive Characteristics of "
             "Cabinets (NEMA 4X or IP equivalent)"),
            ("OBS-02", "MAJOR",
             "Forced-air cooling (left-side intake fan, right-side "
             "exhaust fan, filter) is incompatible with NEMA 4X/IP66 "
             "unless rated filter-fan assemblies are specified; the "
             "sheet also declares “For Outdoor Use” while the panel is "
             "installed inside the air-conditioned container (AC "
             "Thermal Calculation carries the LCP at 0.14 kW heat load) "
             "— reconcile the cooling design with the protection class "
             "and the installation environment"),
            ("OBS-03", "MINOR",
             "PANEL WEIGHT row is a template placeholder (“Insert "
             "actual panel weight here / TBD”) — declare the actual "
             "weight for lifting, handling and container floor "
             "loading"),
            ("NOTE-01", "MINOR",
             "Cover title block: project name typo “PD Tattal” and "
             "ADASA code printed “P22-ET-09-008-001” instead of "
             "P22-CD-09-008-001"),
        ],
        action=[
            ("Action — re-issue as Rev B:", {"bold": True}),
            (" align the Panel Specification Sheet with the LCP "
             "Datasheet Rev B enclosure (Stainless Steel 316L, NEMA "
             "4X/IP66) or submit the engineering justification for a "
             "different specification; reconcile the cooling "
             "arrangement with the declared protection class; declare "
             "the actual panel weight; and correct the title block. "
             "Closure threshold: enclosure fabrication release is gated "
             "on Rev B — ADASA's position on the expedited path is "
             "stated in the response to the BW Water email of "
             "10-Jun-2026, issued in parallel with this transmittal.",),
        ],
    ),
    dict(
        heading="PLC/LCP Schematic Diagram Rev A — P22-CD-09-008-002",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "First submittal, 71 sheets. Wiring regulations (380 V "
            "50 Hz 3PH+N+PE, 24 VDC control, 400 A main disconnect, "
            "SCCR 36 kA, 600 V cable rating) are consistent with the "
            "Single Line Diagram and the MCCB selections "
            "(NSX400F/NSX250F). The PLC rack is fully defined — "
            "5069-L320ER CPU, two IB16 discrete-input, one OB16 output, "
            "two IY4 universal analog (the eight RTD-capable channels), "
            "five IF8 analog-input and two OF4 analog-output modules, "
            "with three-wire RTD terminal strips — and the signal "
            "assignments are consistent with the I/O List Rev 2. The HP "
            "Pump drive (PowerFlex 753, 205 A frame) is adequately "
            "sized for the 93 kW motor. Detailed annotations on "
            "P22-CD-09-008-002_A_Schematic_CC_ADASA.pdf.",
        ],
        obs=[
            ("NOTE-01", "MAJOR",
             "Acceptance is conditional on Plant Control Philosophy Rev "
             "D: any signal divergence introduced by Rev D propagates "
             "to the panel wiring and terminal assignments. Spare I/O "
             "capacity should absorb signal-level changes; confirm the "
             "I/O assignment after Rev D issue"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new Schematic revision "
             "required if Plant Control Philosophy Rev D introduces no "
             "signal changes:", {"bold": True}),
            (" confirm the I/O assignment against Rev D once delivered. "
             "This conditional acceptance follows the same mechanism "
             "applied to the I/O List in Transmittal N19.",),
        ],
    ),
    dict(
        heading="Electrical Load List Rev 0 — P22-LI-09-007-001",
        code="Response Code: 1 — Approved",
        paras=[
            "IFC issue of the Rev B accepted as Code 1 in TM N19. "
            "Content reproduced without undeclared change: 23 loads, "
            "380 V three-phase / 220 V single-phase 50 Hz, total 144.00 "
            "kW / 312 A with safety factor. IFC accepted.",
        ],
        action=[("Action: none — IFC Rev 0 accepted.", {"bold": True})],
    ),
    dict(
        heading="Power Cable Schedule Rev 0 — P22-LI-09-007-002",
        code="Response Code: 1 — Approved",
        paras=[
            "IFC issue of the Rev B accepted as Code 2 in TM N19. The "
            "single observation is incorporated: the REL-09-001 CIP "
            "Heater is now defined as two explicit cable runs (feeder "
            "to Heater Control Panel, Heater Control Panel to heater "
            "element, 10 mm2 4G), consistent with the Heater Control "
            "Panel block drawn on the Single Line Diagram Rev 0. IFC "
            "accepted.",
        ],
        action=[
            ("Action: none — IFC Rev 0 accepted; the TM N19 observation "
             "is closed.", {"bold": True}),
        ],
    ),
    dict(
        heading="Datasheet of Power and Control Cable Rev 0 — P22-ET-09-007-002",
        code="Response Code: 1 — Approved",
        paras=[
            "IFC issue of the Rev B accepted as Code 1 in TM N19. Five "
            "cable families with IEC 60228 / EN 50525 compliance and "
            "UL/CE/RoHS certifications, reproduced without undeclared "
            "change. IFC accepted.",
        ],
        action=[("Action: none — IFC Rev 0 accepted.", {"bold": True})],
    ),
    dict(
        heading="Single Line Diagram Rev 0 — P22-CD-09-007-001",
        code="Response Code: 1 — Approved",
        paras=[
            "IFC issue of the Rev B accepted as Code 2 in TM N19. Both "
            "items are incorporated under revision clouds on sheet 3: "
            "the principal enclosure is labelled “P22-LCP-001 (METAL "
            "CLAD, NEMA4X/IP66, FLOOR STANDING TYPE)” and the surge "
            "protection device is shown on the 400 A incoming feeder "
            "with Uc 415 Vac and Imax 50 kA. The CIP Heater branch "
            "reflects the Heater Control Panel arrangement of Section "
            "2.9. IFC accepted.",
        ],
        action=[
            ("Action: none — IFC Rev 0 accepted; both TM N19 items are "
             "closed.", {"bold": True}),
            (" The NEMA 4X/IP66 label on this diagram is part of the "
             "enclosure-consistency basis invoked in Section 2.6.",),
        ],
    ),
    dict(
        heading=("Typical Installation Details of Power Works Rev 0 — "
                 "P22-DWG-09-007-005"),
        code="Response Code: 1 — Approved",
        paras=[
            "IFC issue of the Rev C accepted as Code 2 in TM N19. The "
            "note is incorporated: sheet 8 now carries the load-type to "
            "grounding-method mapping (METHOD 1 to 3 for cable tray "
            "bonding variants, METHOD 4 skid and structural steel, "
            "METHOD 5 pumps and motors, METHOD 6 panels and junction "
            "boxes, METHOD 7 field instruments) with conductor sizing "
            "referenced to IEC 60364-5-54. IFC accepted.",
        ],
        action=[
            ("Action: none — IFC Rev 0 accepted; the TM N19 note is "
             "closed.", {"bold": True}),
        ],
    ),
    dict(
        heading="I/O List Rev 2 — P22-LI-09-008-001",
        code="Response Code: 3 — To be revised",
        paras=[
            "Resubmittal of Rev 1 (Code 2 conditional in TM N19). The "
            "technical items are closed: analyser power supplies "
            "reconciled to 24 VDC against the Instrument List (closing "
            "an item open since TM N14, approximately 96 days), VFD "
            "output frequency and accumulated energy added on "
            "Ethernet/IP for both pumps, and the dosing pump IN REMOTE "
            "handling declared as soft I/O from the HMI faceplate. The "
            "disposition is governed by the TM N19 "
            "conditional-acceptance clause: approval was contingent on "
            "Plant Control Philosophy Rev D, which was not delivered "
            "within the fourteen-day window — the acceptance therefore "
            "reverts to Code 3 by its own terms. Detailed annotations "
            "on P22-LI-09-008-001_2_IO_List_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "TM N19 conditional acceptance lapsed: Plant Control "
             "Philosophy Rev D not delivered — the I/O register cannot "
             "consolidate IFC status until Rev D is issued and any "
             "signal divergence is reconciled"),
            ("NOTE-01", "MINOR",
             "Item numbering gaps (127 to 129 and 133 to 135) — "
             "renumber contiguously or confirm no signal was dropped"),
            ("NOTE-02", "MINOR",
             "Revision-history block lists Rev 0 and Rev 1 only; add "
             "the Rev 2 row. Dosing pump RUNNING (items 131/137) is "
             "labelled DI while routed over Ethernet/IP — flag as soft "
             "I/O"),
        ],
        action=[
            ("Action — deliver Plant Control Philosophy Rev D and "
             "re-issue as Rev 3 (or confirm Rev 2 unchanged) within the "
             "same cycle:", {"bold": True}),
            (" the register itself needs only the minor QA corrections "
             "noted; the reversion clears as soon as Rev D is delivered "
             "and signal consistency is confirmed.",),
        ],
    ),
    dict(
        heading=("Instrumentation & Control Cable Schedule Rev 1 — "
                 "P22-LI-09-008-002"),
        code="Response Code: 3 — To be revised",
        paras=[
            "Resubmittal of Rev 0 (Code 3 in TM N19). The four prior "
            "items are closed: VFD communications for both pumps are "
            "now specified as shielded 4-pair Ethernet/IP cable, the "
            "dosing pump assignments match the I/O List soft-I/O "
            "scheme, the level switch rows use LSH/LSL identifiers, and "
            "a Full Tag column repeats the complete tag on every row. "
            "Rev 1 however introduces new register-integrity defects. "
            "Detailed annotations on "
            "P22-LI-09-008-002_1_IC_Cable_Schedule_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Duplicate item numbers on sheet 4: numbers 54, 55 and 56 "
             "are each assigned twice (VE09-006-COM/VE09-003-COM, "
             "VE09-006-PWR/VE09-003-PWR, PIT09-005-AI/VE09-004-COM) — "
             "unique cable identification is broken for procurement and "
             "field termination"),
            ("OBS-02", "MAJOR",
             "Copy-paste descriptions on valve power rows: multiple PWR "
             "rows (including VE09-006-PWR and VE09-003-PWR) read “RO "
             "2ND STAGE CIP FEED MOTORIZED VALVE POWER” for valves that "
             "are not the CIP feed valve — every PWR row description "
             "must match its Full Tag"),
            ("OBS-03", "MINOR",
             "Function column reads “PIT” on the LIT09-002 and "
             "TIT09-006 rows (items 60/61) — correct to LIT and TIT"),
            ("NOTE-01", "MINOR",
             "RTD cable construction differs between identical signals "
             "on the two pump trains (HP shielded UTP/PUR versus CIP "
             "PVC/OS/PVC) — reconcile or justify; VT09-001 remark “2 "
             "Wire, 24VDC” conflicts with the I/O List loop-powered "
             "4-20 mA declaration"),
        ],
        action=[
            ("Action — re-issue as Rev 2 (Issued for Approval):",
             {"bold": True}),
            (" renumber sheet 4 uniquely, correct every valve power-row "
             "description against its tag, fix the Function column "
             "entries, and reconcile the RTD cable construction and the "
             "VT09-001 remark. Closure threshold: as stated in TM N19, "
             "this schedule cannot reach IFC status while Plant Control "
             "Philosophy Rev D remains undelivered.",),
        ],
    ),
    dict(
        heading="Organization Chart Rev A — P22-MTC-09-000-001",
        code="Response Code: 1 — Approved",
        paras=[
            "First submittal. The chart defines the full project "
            "organisation with named roles across both BW Water "
            "regions: sponsor, project manager and director, "
            "fabrication management, engineering disciplines, supply "
            "chain, quality (Quality Manager and QA/QC Manager), "
            "planning and document control, EHS and project control, "
            "with the communication channels between BW Water Americas "
            "and BW Water Asia declared. Accepted as-is.",
        ],
        action=[
            ("Action: none — accepted; issue directly at IFC Rev 0.",
             {"bold": True}),
        ],
    ),
    dict(
        heading="Project Schedule Rev A — P22-BA-09-000-001",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "Formal submittal of the recovery schedule delivered by "
            "email on 08-Jun-2026 and adopted by ADASA as the recovery "
            "baseline, with reservations, in the letter of 09-Jun-2026. "
            "The anchor milestones verified then remain the binding "
            "basis: vessels ex-works Spain 23-Jun, Penang arrival "
            "02-Aug, module ex-works Penang 15-Aug, finish 19-Nov. This "
            "disposition records that adoption; the reservations stated "
            "in the letter become document actions.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "The programme is silent on the certification basis of the "
             "RO pressure vessels: the 23-Jun ex-works date corresponds "
             "to the non-stamped route accepted under the ADASA waiver "
             "of 02-Jun-2026, and the schedule does not state it"),
            ("OBS-02", "MAJOR",
             "No vessel pressure-test activity is visible: the factory "
             "hydrostatic test (1800 psi x 1.1 per the Protec Arisawa "
             "letter) and the system hydrostatic tests required before "
             "FAT per the Technical Specification — Inspections During "
             "Manufacturing are not shown as dated activities"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new Schedule revision "
             "required:", {"bold": True}),
            (" state the certification basis consistent with the "
             "02-Jun waiver, and add the factory vessel hydrostatic "
             "test and the pre-FAT system hydrostatic tests as "
             "discrete, dated activities. The baseline adoption of "
             "09-Jun-2026 is not re-opened by these actions.",),
        ],
    ),
    dict(
        heading="NDE Plan Rev A — P22-BA-09-000-005",
        code="Response Code: 3 — To be revised",
        paras=[
            "First submittal, partially responding to the procedures "
            "item of Transmittal N19. Weld NDE coverage is adequate for "
            "piping and structural scope: the Super Duplex "
            "high-pressure circuit carries 100 percent visual, 100 "
            "percent penetrant on root and final passes, 10 percent "
            "radiography on butt welds and PMI at 10 percent minimum, "
            "with personnel per SNT-TC-1A / ISO 9712 and acceptance per "
            "ASME B31.3 and AWS D1.1. The plan is silent on the "
            "pressure vessels. Detailed annotations on "
            "P22-BA-09-000-005_A_NDE_Plan_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "CRITICAL",
             "No RO pressure vessel scope: factory hydrostatic test at "
             "rating (1800 psi x 1.1 per the Protec Arisawa letter), "
             "the certification basis agreed in the ADASA waiver of "
             "02-Jun-2026, the documentation dossier and the witness "
             "arrangement are absent — the same gap flagged on the ITP "
             "in Transmittal N19"),
            ("OBS-02", "MAJOR",
             "No ADASA witness or hold points declared: the Technical "
             "Specification — Inspections During Manufacturing reserves "
             "ADASA's right to witness PMI and key tests (Punto W)"),
            ("OBS-03", "MINOR",
             "Governing code editions left as placeholders and the plan "
             "is titled “general” — state editions and confirm the "
             "coverage table is project-specific"),
        ],
        action=[
            ("Action — re-issue as Rev B:", {"bold": True}),
            (" incorporate the vessel test scope (or reference the "
             "dedicated hydrostatic procedure) with the waiver basis, "
             "the dossier and the Protec witness hold point; add the "
             "ADASA witness and hold point column; and state the "
             "governing editions including the UT/RT acceptance basis "
             "for Super Duplex butt welds.",),
        ],
    ),
    dict(
        heading="PMI Procedure Rev A — P22-BA-09-000-006",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "First submittal. The LIBS technique (SciAps Z-200 / "
            "902C+), the API 578/582 basis and the five attached "
            "technician certificates are sound. The procedure is a "
            "generic subcontractor document scoped to refinery service "
            "categories. Detailed annotations on "
            "P22-BA-09-000-006_A_PMI_Procedure_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "The Technical Specification — Inspections During "
             "Manufacturing requirement is not declared: PMI on at "
             "least 10 percent of the Super Duplex high-pressure "
             "circuit components with UNS S32750 conformity as "
             "acceptance basis and the ADASA witness right (Punto W)"),
            ("OBS-02", "MINOR",
             "Project applicability not delimited — the embedded "
             "subcontractor document references refinery clauses (HF "
             "acid, fired heaters) not applicable to this module"),
            ("NOTE-01", "MINOR",
             "The cover qualification clause is copied from the NDE "
             "Plan (refers to non-destructive examination personnel) — "
             "replace with the PMI operator qualification defined in "
             "the body"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new PMI Procedure "
             "revision required:", {"bold": True}),
            (" add the project scoping clause mapping PMI to the Taltal "
             "Super Duplex high-pressure circuit at 10 percent minimum "
             "with UNS S32750 acceptance and the ADASA witness point, "
             "and correct the cover qualification clause.",),
        ],
    ),
    dict(
        heading="Welding Procedure Rev A — P22-BA-09-000-007",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "First submittal. The package qualifies the two relevant "
            "arc-welded base materials per ASME IX: structural carbon "
            "steel (GMAW, S275JR) and the Super Duplex high-pressure "
            "piping (GTAW, SA-790 UNS S32750 with ER2594 and impact "
            "testing), with six welders qualified 6G on Super Duplex. "
            "Detailed annotations on "
            "P22-BA-09-000-007_A_Welding_Procedure_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Thickness-range qualification: the Super Duplex PQR "
             "coupon (2.77 mm) qualifies up to 5.54 mm per ASME IX "
             "QW-451, while the WPS declares a range to 14.02 mm — "
             "provide the qualifying coupon for the upper range or "
             "restrict the WPS"),
            ("OBS-02", "MINOR",
             "The low-pressure thermoplastic joining scope is not "
             "addressed: the NDE Plan cites DVS 2202-1 acceptance for "
             "thermoplastic joints, so the joining method and its "
             "procedure must be stated for scope completeness"),
            ("NOTE-01", "MINOR",
             "No heat-input limits or ferrite-number acceptance "
             "declared for the Super Duplex WPS — corrosion-critical "
             "for the 45000 to 55000 ppm chloride brine service"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new Welding Procedure "
             "revision required:", {"bold": True}),
            (" attach the PQR coverage for the full production "
             "thickness range (or restrict the WPS range), state the "
             "thermoplastic joining method and procedure, and declare "
             "the heat-input and ferrite acceptance for the Super "
             "Duplex WPS.",),
        ],
    ),
    dict(
        heading="Visual Procedure Rev A — P22-BA-09-000-008",
        code="Response Code: 2 — Approved as noted",
        paras=[
            "First submittal. Direct visual technique per ASME Section "
            "V Article 9 (600 mm, 30 degrees, 1000 lux minimum), "
            "acceptance per ASME B31.3 and AWS D1.1, records on "
            "controlled forms. Detailed annotations on "
            "P22-BA-09-000-008_A_Visual_Procedure_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MINOR",
             "VT inspector qualification not stated — align with the "
             "NDE Plan personnel basis (SNT-TC-1A VT Level II or ISO "
             "9712)"),
            ("OBS-02", "MINOR",
             "Scope includes thermoplastic welds but no thermoplastic "
             "acceptance criteria are cited — add DVS 2202-1 visual "
             "acceptance or exclude thermoplastics from this "
             "procedure"),
            ("NOTE-01", "MINOR",
             "Referenced quality forms and procedures (QAM series) are "
             "not attached — list them as controlled external "
             "references"),
        ],
        action=[
            ("Action to issue at IFC Rev 0 — no new Visual Procedure "
             "revision required:", {"bold": True}),
            (" state the inspector qualification, add the thermoplastic "
             "acceptance basis, and list the referenced QAM "
             "documents.",),
        ],
    ),
]


ATTACHMENTS = [
    ("Alarm & Interlock List Rev B", "Code 3",
     "P22-LI-09-008-015_B_Alarm_Interlock_List_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02"),
    ("PLC-LCP Outline Panel Drawing Rev A", "Code 3",
     "P22-CD-09-008-001_A_Outline_Panel_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01"),
    ("I/O List Rev 2", "Code 3",
     "P22-LI-09-008-001_2_IO_List_CC_ADASA.pdf",
     "OBS-01, NOTE-01, NOTE-02"),
    ("Instrumentation & Control Cable Schedule Rev 1", "Code 3",
     "P22-LI-09-008-002_1_IC_Cable_Schedule_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01"),
    ("NDE Plan Rev A", "Code 3",
     "P22-BA-09-000-005_A_NDE_Plan_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03"),
    ("Data Transfer List Rev 1", "Code 2",
     "P22-LI-09-008-004_1_Data_Transfer_List_CC_ADASA.pdf",
     "OBS-01, NOTE-01"),
    ("LCP Datasheet Rev B", "Code 2",
     "P22-ET-09-007-005_B_LCP_Datasheet_CC_ADASA.pdf",
     "OBS-01"),
    ("PLC/LCP Schematic Diagram Rev A", "Code 2",
     "P22-CD-09-008-002_A_Schematic_CC_ADASA.pdf",
     "NOTE-01"),
    ("Project Schedule Rev A", "Code 2",
     "P22-BA-09-000-001_A_Project_Schedule_CC_ADASA.pdf",
     "OBS-01, OBS-02"),
    ("PMI Procedure Rev A", "Code 2",
     "P22-BA-09-000-006_A_PMI_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
    ("Welding Procedure Rev A", "Code 2",
     "P22-BA-09-000-007_A_Welding_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
    ("Visual Procedure Rev A", "Code 2",
     "P22-BA-09-000-008_A_Visual_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
]


RESPONSE_SUMMARY = [
    ("P22-LI-09-008-003", "Instrument List", "E", "1 — Approved"),
    ("P22-LI-09-008-004", "Data Transfer List (Modbus TCP/IP)", "1",
     "2 — Approved as Noted"),
    ("P22-LI-09-008-012", "Datasheet — Pressure Transmitter", "C",
     "1 — Approved"),
    ("P22-LI-09-008-015", "Alarm & Interlock List", "B",
     "3 — To Be Revised"),
    ("P22-ET-09-007-005", "Datasheet of Local Control Panel (LCP)", "B",
     "2 — Approved as Noted"),
    ("P22-CD-09-008-001", "PLC-LCP Outline Panel Drawing", "A",
     "3 — To Be Revised"),
    ("P22-CD-09-008-002", "PLC/LCP Schematic Diagram", "A",
     "2 — Approved as Noted"),
    ("P22-LI-09-007-001", "Electrical Load List", "0", "1 — Approved"),
    ("P22-LI-09-007-002", "Power Cable Schedule", "0", "1 — Approved"),
    ("P22-ET-09-007-002", "Datasheet of Power and Control Cable", "0",
     "1 — Approved"),
    ("P22-CD-09-007-001", "Single Line Diagram", "0", "1 — Approved"),
    ("P22-DWG-09-007-005", "Typical Installation Details of Power Works",
     "0", "1 — Approved"),
    ("P22-LI-09-008-001", "I/O List", "2", "3 — To Be Revised"),
    ("P22-LI-09-008-002", "Instrumentation & Control Cable Schedule", "1",
     "3 — To Be Revised"),
    ("P22-MTC-09-000-001", "Organization Chart", "A", "1 — Approved"),
    ("P22-BA-09-000-001", "Project Schedule", "A",
     "2 — Approved as Noted"),
    ("P22-BA-09-000-005", "NDE Plan", "A", "3 — To Be Revised"),
    ("P22-BA-09-000-006", "PMI Procedure", "A", "2 — Approved as Noted"),
    ("P22-BA-09-000-007", "Welding Procedure", "A",
     "2 — Approved as Noted"),
    ("P22-BA-09-000-008", "Visual Procedure", "A",
     "2 — Approved as Noted"),
]


GLANCE = [
    ("Instrument List Rev E — Code 1.",
     "All four TM N17 items closed; accepted as-is."),
    ("Data Transfer List Rev 1 — Code 2.",
     "Modbus integration parameters declared; one conductivity register "
     "scale to correct at IFC."),
    ("Pressure Transmitter Datasheet Rev C — Code 1.",
     "Hastelloy C split confirmed; diaphragm row relabelled; accepted "
     "as-is."),
    ("Alarm & Interlock List Rev B — Code 3.",
     "Both TM N17 CRITICALs closed, but winding/bearing sensor "
     "assignments are swapped against the Instrument List on both pump "
     "trains."),
    ("LCP Datasheet Rev B — Code 2.",
     "Enclosure now fully specified (SS316L, NEMA 4X/IP66); declare "
     "total panel power consumption at IFC."),
    ("PLC-LCP Outline Panel Drawing Rev A — Code 3.",
     "Panel Specification Sheet contradicts the LCP Datasheet on "
     "enclosure material and protection class; this is the "
     "fabrication-gating decision."),
    ("PLC/LCP Schematic Diagram Rev A — Code 2.",
     "I/O configuration complete and consistent; acceptance conditional "
     "on Plant Control Philosophy Rev D signal stability."),
    ("Electrical Load List Rev 0 — Code 1.", "IFC accepted."),
    ("Power Cable Schedule Rev 0 — Code 1.",
     "REL-09-001 two-cable topology incorporated; IFC accepted."),
    ("Datasheet of Power and Control Cable Rev 0 — Code 1.",
     "IFC accepted."),
    ("Single Line Diagram Rev 0 — Code 1.",
     "Enclosure rating and surge protection device incorporated; IFC "
     "accepted."),
    ("Typical Installation Details Rev 0 — Code 1.",
     "Grounding method per load type incorporated; IFC accepted."),
    ("I/O List Rev 2 — Code 3.",
     "Technical items closed; the TM N19 conditional acceptance reverts "
     "because Plant Control Philosophy Rev D was not delivered."),
    ("Instrumentation & Control Cable Schedule Rev 1 — Code 3.",
     "All four TM N19 items closed; Rev 1 introduces duplicate item "
     "numbers and wrong valve descriptions."),
    ("Organization Chart Rev A — Code 1.",
     "Complete structure with named roles; accepted as-is."),
    ("Project Schedule Rev A — Code 2.",
     "Adopted as recovery baseline per the ADASA letter of 09-Jun-2026; "
     "ASME basis and vessel hydrostatic activity to incorporate at "
     "IFC."),
    ("NDE Plan Rev A — Code 3.",
     "Weld NDE coverage adequate; silent on the RO pressure vessel test "
     "scope and on ADASA witness points."),
    ("PMI Procedure Rev A — Code 2.",
     "Technique and certificates sound; project-specific Super Duplex "
     "scope and ADASA witness point to incorporate."),
    ("Welding Procedure Rev A — Code 2.",
     "ASME IX WPS/PQR qualified; thickness-range qualification and "
     "thermoplastic joining scope to close."),
    ("Visual Procedure Rev A — Code 2.",
     "Method sound; inspector qualification and thermoplastic "
     "acceptance criteria to add."),
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N20 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-020-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # =========================================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(doc, [(
        "This transmittal reviews twenty documents from BW Water: the "
        "control and instrumentation package of submittal 25007-0046 "
        "(including the PLC-LCP panel drawings flagged as urgent in the "
        "BW Water email of 10-Jun-2026) and the electrical IFC Rev 0 "
        "package, instrumentation lists and quality procedures of "
        "submittal 25007-0047.",)])

    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — TO BE REVISED.", {"bold": True}),
        (" Submittals 25007-0046 and 25007-0047. Tally: 8 Code 1, 7 "
         "Code 2, 5 Code 3. The verdict is driven by the PLC-LCP "
         "Outline Panel Drawing enclosure contradiction, the lapsed "
         "Plant Control Philosophy Rev D condition, and the NDE Plan "
         "silence on the RO pressure vessel test scope.",),
    ])

    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for lead, rest in GLANCE:
        add_para(doc, [(lead + " ", {"bold": True}), (rest,)])

    add_para(doc, [
        ("Why Code 3 — PLC-LCP Outline Panel Drawing Rev A (panel "
         "fabrication gate). ", {"bold": True}),
        ("The Panel Specification Sheet declares sheet steel painted "
         "GRAY RAL 7035, protection class IP55 and zinc-plated "
         "internals. The LCP Datasheet Rev B of the same submittal "
         "declares an nVent Hoffman FS66S enclosure in unpainted "
         "Stainless Steel 316L, NEMA 4X/IP66, for highly corrosive "
         "environments, and the IFC Single Line Diagram labels the "
         "panel “METAL CLAD, NEMA4X/IP66”. The Technical "
         "Specification — Constructive Characteristics of Cabinets "
         "requires NEMA 4X or its IP equivalent. Resolution path is "
         "short: confirm in writing that the enclosure to be "
         "fabricated is the one specified in the LCP Datasheet Rev B "
         "and re-issue the Outline Rev B with an aligned Panel "
         "Specification Sheet, actual panel weight, and the cooling "
         "arrangement reconciled with the declared protection "
         "class.",),
    ])

    add_para(doc, [
        ("Why Code 3 — Plant Control Philosophy Rev D (fourth "
         "consecutive transmittal). ", {"bold": True}),
        ("The fourteen-day window stated in Transmittal N19 expired on "
         "08-Jun-2026 with no Rev D delivery. The conditional "
         "acceptance of the I/O List recorded in Transmittal N19 "
         "therefore reverts to Code 3 by its own terms, and the "
         "Instrumentation & Control Cable Schedule and the Alarm & "
         "Interlock List cannot consolidate IFC status while the "
         "governing control narrative remains open. ADASA's "
         "reservation of contractual remedies under Contract C-4300 "
         "stands.",),
    ])

    add_para(doc, [
        ("Why Code 3 — NDE Plan Rev A. ", {"bold": True}),
        ("No activity covers the RO pressure vessels: factory "
         "hydrostatic test, the certification basis agreed in the "
         "ADASA waiver of 02-Jun-2026, the documentation dossier and "
         "the witness points are absent. The Hydrostatic, Preservation "
         "and FAT procedures and the ITP Rev C requested in "
         "Transmittal N19 remain undelivered.",),
    ])

    add_para(doc, [(
        "Open observations from previous transmittals are inventoried "
        "in Section 3.",)])

    # =========================================================================
    # 2. OBSERVATIONS BY DOCUMENT
    # =========================================================================
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        for p in sec["paras"]:
            if isinstance(p, str):
                add_para(doc, [(p,)])
            else:
                add_para(doc, p)
        if sec.get("obs"):
            add_simple_table(
                doc, [("ID", "Severity", "Topic")] + list(sec["obs"]))
        add_para(doc, sec["action"])

    # =========================================================================
    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    # =========================================================================
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    add_para(doc, [("Items open as of 10-Jun-2026.",)])

    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status"),
        ("TM N18 Section 2.1",
         "Plant Control Philosophy Rev C (P22-BT-09-009-001)",
         "OBS-01 CRITICAL HP Pump start permissive; OBS-02 MAJOR "
         "Sequence Charts / Setpoint List / Control Matrix undelivered; "
         "OBS-03 MAJOR salt rejection formula. Fourth consecutive "
         "transmittal; the fourteen-day window stated in TM N19 "
         "expired on 08-Jun-2026",
         "OPEN — Rev D not delivered. The consequence has materialised "
         "in this transmittal: the I/O List conditional acceptance "
         "reverts to Code 3 (Section 2.13), and the Instrumentation & "
         "Control Cable Schedule, the Alarm & Interlock List and the "
         "PLC/LCP Schematic remain gated. ADASA's reservation of "
         "remedies under Contract C-4300 stands"),
        ("TM N11 OBS-03",
         "Grounding Layout (P22-DWG-09-007-003)",
         "Grounding schedule completeness per NCh Elect. 4/2003 "
         "Section 10.0 — approximately 86 days open",
         "OPEN — Rev F committed for Wednesday 17-Jun-2026 per the "
         "clarification exchange of 03-Jun. SEC compliance Hold Point "
         "remains gated"),
        ("TM N4 NOTE-05",
         "HMI Screenshots (P22-BREAD-09-008-001)",
         "Committed at TM N4 — never submitted; approximately 126 "
         "days, oldest open commitment in the project",
         "OPEN"),
        ("TM N19 Section 2.10",
         "ITP Offsite (P22-BA-09-000-004)",
         "OBS-01 CRITICAL ASME X certification scope; NOTE-01 "
         "procedures without delivery dates",
         "PARTIALLY ADVANCED — this delivery provides four of the "
         "procedures (NDE, PMI, Welding, Visual). Still outstanding: "
         "ITP Rev C with the certification scope declared per the "
         "02-Jun waiver, and the Hydrostatic, Preservation and FAT "
         "procedures with firm dates. The vessel test scope is absent "
         "from every document of this set (Section 2.17 OBS-01)"),
        ("TM N19 Sections 2.12/2.13",
         "Cartridge Filters (P22-ET-09-009-005/006)",
         "Rev E / Rev D pending the Technical Note P22-NT-09-000-001-0 "
         "cycle",
         "OPEN — FAT/SAT table and remaining clarifications due "
         "15-Jun-2026"),
    ])

    add_para(doc, [("Closed in this transmittal:", {"bold": True})])
    for txt in [
        "TM N14 NOTE-02 — analyser power-supply voltage (closed by I/O "
        "List Rev 2 reconciliation to 24 VDC; approximately 96 days "
        "open).",
        "TM N15 Section 2.4 OBS-01 and OBS-02 — LCP I/O module "
        "configuration and enclosure rating (closed by LCP Datasheet "
        "Rev B with the Schematic Rev A; OBS-03 power consumption "
        "partially closed, Section 2.5).",
        "TM N17 Section 2.9 OBS-01 and NOTE-01/02/03 — Instrument List "
        "items (closed by Rev E).",
        "TM N17 Section 2.2 NOTE-01/02 — Data Transfer List Modbus "
        "parameters and vibration scaling (closed by Rev 1).",
        "TM N17 Section 2.3 OBS-01 and NOTE-01 — Pressure Transmitter "
        "Hastelloy scope and sealing row (closed by Rev C).",
        "TM N17 Section 2.8 OBS-01/02/03 and NOTE-01 — Alarm & "
        "Interlock CRITICALs, vibration asymmetry and digital section "
        "(closed by Rev B; NOTE-02 not applied, now Section 2.4 "
        "OBS-02).",
        "TM N19 Section 2.2 OBS-01 — Power Cable Schedule REL-09-001 "
        "topology (closed by Rev 0).",
        "TM N19 Section 2.4 OBS-01 and NOTE-01 — Single Line Diagram "
        "enclosure rating and surge protection (closed by Rev 0).",
        "TM N19 Section 2.7 NOTE-01 — Typical Installation grounding "
        "method designation (closed by Rev 0).",
        "TM N19 Section 2.8 OBS-01 and NOTE-01/02 — I/O List analyser "
        "voltage, VFD variables and dosing IN REMOTE (closed by Rev 2; "
        "OBS-02 condition lapsed, Section 2.13).",
        "TM N19 Section 2.11 OBS-01/02 and NOTE-01/02 — "
        "Instrumentation & Control Cable Schedule four items (closed "
        "by Rev 1; new defects in Section 2.14).",
    ]:
        add_bullet(doc, txt)

    add_para(doc, [
        ("Tracked for IFC Rev 0", {"bold": True}),
        (" (deliverables on related documents or separate analyses; no "
         "advance in this delivery unless stated):",),
    ])
    for txt in [
        "PSV-09-002 overpressure / relief sizing analysis (TM N18).",
        "P&ID CIP Tank dual-value convention consistency (TM N18).",
        "CIT-09-004 loop response engineering note (TM N18).",
        "AC Thermal Calculation effective post-selection margin "
        "statement (+13.3 percent) (TM N18).",
        "Motor Datasheet — Pt-100 declaration on motor windings and "
        "bearings per Technical Specification — Electrical Motors.",
        "Cable Tray Layout — consolidated table of S1 to S7 zone "
        "reference positions (TM N19).",
        "PQP — FAT Approval Certificate specimen template per BAE "
        "Clause 31 (TM N19).",
        "TIT-09-006 span configuration confirmation (Sections 2.1 and "
        "2.2, new).",
        "LCP Datasheet — total panel power consumption declaration "
        "(Section 2.5, new).",
    ]:
        add_bullet(doc, txt)

    # =========================================================================
    # 4. ATTACHMENTS
    # =========================================================================
    doc.add_heading("ATTACHMENTS", level=1)

    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)

    add_para(doc, [(
        "All twelve documents with open observations or notes carry "
        "annotated PDFs (five Code 3 and seven Code 2). The eight "
        "Code 1 — Approved documents (Instrument List Rev E, Pressure "
        "Transmitter Datasheet Rev C, Electrical Load List Rev 0, "
        "Power Cable Schedule Rev 0, Datasheet of Power and Control "
        "Cable Rev 0, Single Line Diagram Rev 0, Typical Installation "
        "Details Rev 0, Organization Chart Rev A) require no "
        "modification and carry no annotated PDF; residual "
        "deliverables tracked on related documents are listed in "
        "Section 3.",)])

    # =========================================================================
    # 5. RESPONSE SUMMARY
    # =========================================================================
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)

    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.",
         {"bold": True}),
        (" Five Code 3 documents drive the verdict (Sections 2.4, 2.6, "
         "2.13, 2.14 and 2.17). The five electrical IFC Rev 0 "
         "documents are accepted with every prior condition verified "
         "as incorporated, a complete closure of the TM N19 "
         "electrical package. The PLC-LCP Outline Panel Drawing "
         "carries the single decision gating enclosure fabrication: "
         "alignment of the Panel Specification Sheet with the LCP "
         "Datasheet Rev B enclosure (Stainless Steel 316L, NEMA "
         "4X/IP66); ADASA's expedited-path position is stated in the "
         "parallel response to the BW Water email of 10-Jun-2026. "
         "Plant Control Philosophy Rev D, now absent for a fourth "
         "consecutive cycle with the TM N19 fourteen-day window "
         "expired, has materially reverted the I/O List acceptance and "
         "continues to gate the instrumentation cabling and alarm "
         "documents. The quality procedures advance the Transmittal "
         "N19 request, yet the RO pressure vessel test scope agreed in "
         "the 02-Jun waiver is reflected in none of them.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
