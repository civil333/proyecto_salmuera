# TECHNICAL REVIEW TRANSMITTAL N15 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-015-0
**Date:** 22-Apr-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0030, 25007-0031, 25007-0032, 25007-0033

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Ten documents reviewed from four deliveries (E30 to E33, April 16–22). Tally: 1 Code 1, 6 Code 2, 3 Code 3 (LCP Datasheet Rev A, Cable Tray Rev B, Plant Control Philosophy Rev B require formal resubmittal). Detailed per-document comments in the attached CC_ADASA PDFs.

Key findings:

- 3,500 mm CIP/dosing footprint constraint (TM N5/N7) — WITHDRAWN by ADASA, superseded by ADASA-side drawing P22-DWG-06-006-101.
- Equipment Layout Rev B: Operating Weight table to be embedded in Rev 0; BW Water Civil Loading drawing committed for 23-Apr-2026.
- Cable Tray Rev B requires Rev C — 5 new observations (support interferences and routing errors) plus 2 inherited from TM N4, 78 days outstanding.
- Plant Control Philosophy Rev B elevated to Code 3 after detailed cross-check vs P&ID Rev C, Valve List Rev D, IO List Rev C and Technical Offer Rev1: 17 notes including 1 CRITICAL (HP Pump permissive TAG errors).
- LCP Datasheet Rev A requires Rev B: cover sheet incomplete (IP rating, RTD channel count, dimensions, weight blank) preventing validation against Control System Architecture Rev D.

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 Datasheet of Level Switch Rev B — P22-LI-09-008-008

**Response Code: 1 — Approved**

Capacitive level switch IFM KQ6005 for LS-09-001 and LS-09-002, consistent with Instrument List Rev C and IO List Rev C. Detailed comments: `P22-LI-09-008-008_B_Level_Switch_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MINOR | Communication interface label inconsistency (4-20 mA HART vs IO-Link per IFM KQ6005 PNP discrete) |

---

### 2.2 AC Thermal Calculation Rev C — P22-CD-09-005-002

**Response Code: 2 — Approved as Noted**

Closes Transmittal N2 OBS-02 (180+ days) by consolidating all container loads in the heat balance. Selected unit 2.5 HP / 2.01 TR is marginal vs calculated 2.04 TR. Detailed comments: `P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-02 | MAJOR | Unit capacity margin (0.03 TR deficit vs calculated demand) and n+1 confirmation (each unit at 100% load independently) |

---

### 2.3 Grounding Point & Power Panel Location Layout Rev C — P22-DWG-09-007-003

**Response Code: 2 — Approved as Noted**

Rev C aligned to the Piping Layout Rev B in this submittal, closing Transmittal N11 OBS-03 basis. Detailed comments: `P22-DWG-09-007-003_C_Grounding_Layout_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-03 | MAJOR | Grounding schedule completeness (PE identifiers, conductor cross-section, ring main topology, equipotential bonding) per NCh Elec 4/2003 §10.0 |

---

### 2.4 Datasheet of Local Control Panel (LCP) Rev A — P22-ET-09-007-005

**Response Code: 3 — To be revised**

First revision. Vendor catalog cuts (ABB, Phoenix Contact, Allen-Bradley, Mean Well, ProSoft) are reasonable, but the panel-level datasheet header is not populated, preventing validation against Control System Architecture Rev D. Detailed comments: `P22-ET-09-007-005_A_LCP_Datasheet_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | I/O module configuration and motor RTD channel count not declared (8 Pt-100 channels required per Instrument List Rev C) |
| OBS-02 | MAJOR | Panel IP rating and ambient class not declared (IP54 minimum expected) |
| OBS-03 | MINOR | Power consumption inconsistency: Load List Rev A 1.0 kW vs AC Thermal Calc Rev C 0.14 kW; LCP datasheet not declared |

---

### 2.5 Equipment Layout Rev B — P22-DWG-09-005-003

**Response Code: 2 — Approved as Noted**

Container 40 ft within ET envelope. 16-item equipment list consistent with P&ID Rev C. Section views confirm doors (pedestrian, equipment access, emergency, lateral sliding). Closes Transmittal N5 OBS-03/04/05. Detailed comments: `P22-DWG-09-005-003_B_Equipment_Layout_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-04 | MAJOR | Operating Weight table to be embedded in Rev 0 (IFC); BW Water Civil Loading drawing committed for 23-Apr-2026 and accepted as separate supporting deliverable |

**Items carried forward from Transmittal N5:** OBS-01 (CIP numbering) and OBS-02 (imperial dimensions) remain partially open.

---

### 2.6 Piping Layout Rev B — P22-DWG-09-005-004

**Response Code: 2 — Approved as Noted**

Five-sheet set coordinated with Equipment Layout Rev B. Detailed comments: `P22-DWG-09-005-004_B_Piping_Layout_CC_ADASA.pdf`.

**Transmittal N7 OBS-01 / Transmittal N5 OBS-01 — WITHDRAWN by ADASA:** The 3,500 mm CIP/dosing footprint constraint is hereby withdrawn. The CIP-to-dosing separation is resolved on the ADASA side through the perimeter interconnection drawing P22-DWG-06-006-101. The 11,150 mm separation in Piping Layout Rev B is acceptable as drawn.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-06 | MAJOR | Equipment access door (110° outward) and lateral sliding door not represented in piping views |
| NOTE-07 | MAJOR | Cabinet integration and FAT scope unclear (LCP shown as separate unit without cable routing and conduit penetrations) |
| NOTE-08 | MAJOR | Antiscalant and CIP module-boundary connections not confirmed as flanged |
| NOTE-09 | MINOR | Elevation view for tie-in points missing |

---

### 2.7 Instrument Location Layout Rev C — P22-DWG-09-008-001

**Response Code: 2 — Approved as Noted**

Four-sheet drawing aligned with Piping Layout Rev B. Closes Transmittal N3 OBS-01/02/03 and Transmittal N11 OBS-04. Detailed comments: `P22-DWG-09-008-001_C_Instrument_Location_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-10 | MINOR | Dependency on Equipment Layout Rev B and Piping Layout Rev B acceptance (no action if both are accepted as currently configured) |

---

### 2.8 Cable Tray Layout and Support Details Rev B — P22-DWG-09-007-004

**Response Code: 3 — To be revised**

Five-sheet drawing with tray routing and support zones S1–S6. Five ADASA review findings plus two from Transmittal N4 (78 days outstanding; consolidated comment sheet on Page 5 replies "has been revised" without itemizing closure). Detailed comments: `P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-04 | MAJOR | Support S4 conflicts with antiscalant dosing tank TK-09-002 and adjacent components |
| OBS-05 | MAJOR | UNISTRUT anchoring to container steel not detailed (BW Water container scope) |
| OBS-06 | MAJOR | MAIN PANEL incoming routing not indicated |
| OBS-07 | MAJOR | S3/S4 zoning ambiguous between dosing skid and main panel |
| OBS-08 | MAJOR | Cable tray run conflicts with CIP system |

**Items remaining open from Transmittal N4:** OBS-05 (FIT-09-001 duplicate, to verify in Rev C instrument schedule), OBS-06 (VT-09-001/002/003 missing), OBS-07 (TE-09-001..004 missing). Itemize closure on Rev C consolidated comment sheet.

---

### 2.9 GA of SWRO System Skid Rev A — P22-DWG-09-005-008

**Response Code: 2 — Approved as Noted**

Two-sheet GA showing skid envelope, pressure vessel groupings, HP Pump, turbochargers, PSV, and process valves. Consistent with Equipment Layout Rev B and Valve List Rev D. First revision. Detailed comments: `P22-DWG-09-005-008_A_GA_SWRO_Skid_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-11 | MAJOR | Equipment and valve schedule not provided (vessels per stage, elements per vessel, manifold material/pressure rating, function-vs-tag matrix) |
| NOTE-12 | MAJOR | Design pressure and material schedule for skid piping not summarized (ANSI class per service, pressure-temperature ratings, wall thickness) |

---

### 2.10 Plant Control Philosophy Rev B — P22-BT-09-009-001

**Response Code: 3 — To be revised**

51-page document covering PLC platform, HMI, operator privileges, equipment-group control functions, and standardized control templates. Detailed cross-check against P&ID Rev C, Valve List Rev D, IO List Rev C, Instrument List Rev C and Technical Offer Rev1 raised seventeen findings (NOTE-13 to NOTE-29), one of them CRITICAL. Detailed comments: `P22-BT-09-009-001_B_Control_Philosophy_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-13 | MAJOR | SEC formula and contractual guarantee not aligned (4.8/5.0 kWh/m³ vs Offer Rev1 4.71 kWh/m³ ±5%) |
| NOTE-14 | MAJOR | Vibration trip and alarm setpoints not numerical |
| NOTE-15 | MAJOR | Antiscalant dosing ratio source flow not aligned with P&ID Rev C |
| NOTE-16 | MAJOR | VE-09-002 modulating algorithm not defined |
| NOTE-17 | MAJOR | CIP cycle valve sequence not mapped to P&ID |
| NOTE-18 | MINOR | Motor RTD trip thresholds not stated |
| NOTE-19 | MINOR | Feed turbocharger isolation status not documented |
| NOTE-20 | CRITICAL | HP Pump start permissive contains erroneous TAGs (VE-09-007 duplicated; VE-09-014 antiscalant tank inlet wrongly included) |
| NOTE-21 | MAJOR | TAG FIT-09-001 reused between Section 3.1 (feed flow) and Section 3.3.4 (Stage 2 permeate) |
| NOTE-22 | MAJOR | Salt Rejection formula uses Stage 2 reject conductivity instead of feed conductivity |
| NOTE-23 | MAJOR | Orphan instruments and valves referenced without definition (TE-09-005, VE-09-006, VE-09-008) |
| NOTE-24 | MAJOR | Child documents referenced without formal delivery commitment (Alarm Setpoint List, RO/CIP Sequence Charts, Control Matrix) |
| NOTE-25 | MAJOR | SEC monitoring methodology measures wrong energy bus (RO PLC panel meter, not MCC main breaker) |
| NOTE-26 | MAJOR | Network architecture lacks redundancy and gateway fault management (unmanaged switches, PLX32 SPoF) |
| NOTE-27 | MAJOR | Three ET requirements unmet (manual mode without PLC §5.4, VFD ramp justification §5.4.6, low-pressure rupture interlock §7) |
| NOTE-28 | MAJOR | Off-spec routing without confirmed-closed interlock; bypass turbocharger OR-logic without cross-check |
| NOTE-29 | MINOR | Documentary quality: TAG format inconsistencies, triple AIT/CIT/AE nomenclature, template residue, page numbering, missing Consolidated Comment Sheet |

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

Eight prior observations resolved: six closed (TM N3 OBS-01/02/03, TM N5 OBS-03/04/05, TM N11 OBS-04), two withdrawn by ADASA (TM N5 OBS-01, TM N7 OBS-01), and two from Transmittal N7 (OBS-03, OBS-04) incorporated as Rev 0 notes in Section 2.6. Items below remain open.

| Obs | Document | Description | Outstanding Since | Status |
|-----|----------|-------------|-------------------|--------|
| TM N5 OBS-01 | Equipment / Piping Layout | 3,500 mm CIP/dosing footprint constraint | TM N5 (23-Feb-2026) | WITHDRAWN by ADASA — superseded by P22-DWG-06-006-101 |
| TM N7 OBS-01 | Piping Layout | CIP/dosing footprint 11,150 mm vs 3,500 mm | TM N7 (08-Mar-2026) | WITHDRAWN by ADASA — superseded by P22-DWG-06-006-101 |
| TM N5 OBS-02 | Equipment Layout | Imperial dimensions retained as primary | TM N5 (23-Feb-2026) | PARTIALLY OPEN — see Section 2.5 |
| TM N7 OBS-03 | Piping Layout | Equipment access door + lateral sliding door not represented | TM N7 (08-Mar-2026) | INCORPORATED as Section 2.6 NOTE-06 for Rev 0 |
| TM N7 OBS-04 | Piping Layout | Cabinet integration unclear | TM N7 (08-Mar-2026) | INCORPORATED as Section 2.6 NOTE-07 for Rev 0 |
| TM N4 OBS-06 | Cable Tray Layout | Vibration transmitter locations missing | TM N4 (05-Feb-2026) | OPEN — 78 days outstanding |
| TM N4 OBS-07 | Cable Tray Layout | Pt-100 motor sensor locations missing | TM N4 (05-Feb-2026) | OPEN — 78 days outstanding |
| TM N11 OBS-03 | Grounding Layout | Grounding schedule completeness | TM N11 (17-Mar-2026) | PARTIALLY OPEN — see Section 2.3 NOTE-03 |
| TM N10 OBS-05 | GA Antiscalant Dosing Tank | Working volume, body material, seismic anchor data | TM N10 (12-Mar-2026) | OPEN — GA Rev B still required |
| TM N10 NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | Committed at TM N4 — not submitted | TM N4 (03-Feb-2026) | OPEN — 79 days outstanding |
| TM N13 NOTE-02 | Cable Tray Layout drawings | Internal cable routing not submitted | TM N13 (06-Apr-2026) | OPEN — tracked in ADASA email 10-Apr-2026 |

Tracked for IFC Rev 0: TM N12 NOTE-02 (Line List SCH 80S), TM N13 NOTE-01 (P&ID CIP Tank capacity), TM N8 OBS-04 (vibration setpoints).

---

## 4. ATTACHMENTS

**Download annotated PDFs (Synology Drive):** [https://lrg.synology.me:6501/d/s/17wnt7QrL3VJiw8tuKFZGva6q0ObmRAa/Yts9vGN_FJNnNnqy_yJKIaCINKKRJwlf-yruAehkPJA0](https://lrg.synology.me:6501/d/s/17wnt7QrL3VJiw8tuKFZGva6q0ObmRAa/Yts9vGN_FJNnNnqy_yJKIaCINKKRJwlf-yruAehkPJA0)

| Document | Annotated File | Annotations |
|----------|---------------|-------------|
| Datasheet of Level Switch Rev B | P22-LI-09-008-008_B_Level_Switch_CC_ADASA.pdf | NOTE-01 |
| AC Thermal Calculation Rev C | P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf | NOTE-02 |
| Grounding Layout Rev C | P22-DWG-09-007-003_C_Grounding_Layout_CC_ADASA.pdf | NOTE-03 |
| LCP Datasheet Rev A | P22-ET-09-007-005_A_LCP_Datasheet_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03 |
| Equipment Layout Rev B | P22-DWG-09-005-003_B_Equipment_Layout_CC_ADASA.pdf | NOTE-04 |
| Piping Layout Rev B | P22-DWG-09-005-004_B_Piping_Layout_CC_ADASA.pdf | NOTE-06, NOTE-07, NOTE-08, NOTE-09 |
| Instrument Location Layout Rev C | P22-DWG-09-008-001_C_Instrument_Location_CC_ADASA.pdf | NOTE-10 |
| Cable Tray Layout Rev B | P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf | OBS-04, OBS-05, OBS-06, OBS-07, OBS-08 |
| GA SWRO System Skid Rev A | P22-DWG-09-005-008_A_GA_SWRO_Skid_CC_ADASA.pdf | NOTE-11, NOTE-12 |
| Plant Control Philosophy Rev B | P22-BT-09-009-001_B_Control_Philosophy_CC_ADASA.pdf | NOTE-13 to NOTE-29 (17 annotations) |

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|-------------|-------|-----|---------------|
| P22-LI-09-008-008 | Datasheet of Level Switch | B | 1 — Approved |
| P22-CD-09-005-002 | AC Thermal Calculation | C | 2 — Approved as Noted |
| P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | C | 2 — Approved as Noted |
| P22-ET-09-007-005 | Datasheet of Local Control Panel (LCP) | A | 3 — To be revised |
| P22-DWG-09-005-003 | Equipment Layout | B | 2 — Approved as Noted |
| P22-DWG-09-005-004 | Piping Layout | B | 2 — Approved as Noted |
| P22-DWG-09-008-001 | Instrument Location Layout | C | 2 — Approved as Noted |
| P22-DWG-09-007-004 | Cable Tray Layout and Support Details | B | 3 — To be revised |
| P22-DWG-09-005-008 | GA of SWRO System Skid | A | 2 — Approved as Noted |
| P22-BT-09-009-001 | Plant Control Philosophy | B | 3 — To be revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED**

- Tally: 1 Code 1 + 6 Code 2 + 3 Code 3.
- Closures: 6 OBS closed, 2 withdrawn by ADASA, 2 incorporated as Rev 0 notes.
- New findings: 28 notes and observations raised — breakdown per document in Section 2 tables; detail in attached CC_ADASA PDFs.
- Outstanding: 5 inherited from previous transmittals; TM N4 OBS-06/07 at 78 days require itemized closure on Cable Tray Rev C consolidated comment sheet.
