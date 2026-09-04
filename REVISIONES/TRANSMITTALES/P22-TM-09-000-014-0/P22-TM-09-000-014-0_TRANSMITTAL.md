# TECHNICAL REVIEW TRANSMITTAL N14 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-014-0
**Date:** 15-Apr-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0026, 25007-0027, 25007-0028, 25007-0029

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 2 — APPROVED AS NOTED**

Eleven documents reviewed from four deliveries (E26 April 8, E27 April 10, E28 April 13, E29 April 15). Seven approved without observations, four approved as noted. Twelve previous observations closed. Five remain open. Five notes raised — two major, three minor.

Key findings:
- Vibration transmitters changed from IFM VTV122 to Wilcoxon PCH420V-M12; HART 7.0 deficiency from Transmittal N12 resolved.
- Conductivity sensor technology split confirmed: toroidal (Rosemount 228) for brine, contacting (Rosemount 400) for permeate.
- Valve List TAG uniqueness verified across 111 items; all previous duplicates resolved.
- Flow transmitter FIT-09-004 fluid medium corrected to "Concentrated Brine"; power supply aligned to 12-42 VDC. Both Transmittal N8 notes resolved.
- Analyzer power supply voltage discrepancy (220VAC vs 24VDC) requires alignment before IFC.
- Five previous observations remain open, three dependent on pending Equipment Layout Rev B.

---

## 2. DETAILED OBSERVATIONS BY DOCUMENT

### 2.1 Control System Architecture Rev D — P22-CD-09-004-001

**Response Code: 1 — Approved**

**Transmittal N10 OBS-04 — CLOSED:** UPS battery module UPS-BAT B/PU/FF/24DC/40AH confirmed, two units, 8-hour runtime at 4.35 A full load. Calculation: 40 Ah / 4.35 A = 9.2 hours, exceeding the 8-hour ET requirement. UPS load breakdown should be documented in Control Philosophy Rev B for commissioning reference.

---

### 2.2 Valve List Rev D — P22-LI-09-005-002

**Response Code: 2 — Approved as Noted**

111 items verified for TAG uniqueness, area-code correctness, and actuation compliance.

**Transmittal N11 OBS-01 — CLOSED:** VE-09-007 no longer duplicated. Item 44 retains VE-09-007 (DN80 butterfly, motorized, SWRO Reject 1st Stage). Former item 64 reassigned to VM-09-120 (DN15 ball valve, manual, SWRO 2nd Stage Reject). Both verified against P&ID Rev C.

**Transmittal N11 OBS-02 — CLOSED:** PSV-09-002 no longer duplicated. Item 104 retains PSV-09-002. Item 112 removed — list reduced from 112 to 111 items. See NOTE-01.

**Transmittal N11 NOTE-01 — CLOSED:** Area-07 TAGs corrected. VM-07-005 → VM-09-005, VM-07-031 → VM-09-031, VE-07-009 → VE-09-009. No area-07 TAGs remain.

**Transmittal N6 Duplicate TAGs — CLOSED:** Four original duplicates (VM-09-015, VE-09-008, VE-09-009, VM-09-065) fully resolved. Renamed TAGs verified against P&ID Rev C.

#### NOTE-01 — Safety relief valve item 112 removal requires justification (MAJOR)

Item 112 (second PSV-09-002, safety relief valve) removed rather than assigned a unique TAG. BW Water must provide the overpressure protection analysis confirming that the remaining PSV configuration is adequate for the antiscalant system, or reinstate the valve with a unique TAG prior to IFC (Rev 0).

*Technical Basis: ET — Safety and Relief Valves*

---

### 2.3 Datasheet of Pressure Gauge Rev B — P22-LI-09-008-011

**Response Code: 1 — Approved**

Diaphragm seal changed from Wika 990.10 (SS lower body) to Wika 990.31 (polypropylene, EPDM/PTFE) for PI-09-003 through PI-09-006, for PVC piping compatibility in CIP and antiscalant service. Technically appropriate.

---

### 2.4 I/O List Rev C — P22-LI-09-008-001

**Response Code: 2 — Approved as Noted**

141 items (was 112 in Rev B). New additions: VE-09-015 (Feed TC Isolation, Ethernet/IP), TIT-09-006 (CIP Tank Temperature, AI), PHIT-09-006 (CIP pH Analyzer, AI).

**Transmittal N10 OBS-01 — CLOSED:** Motor temperature tags remain TE, not TIT. BW Water's justification accepted: the 5069-IY4 universal input module reads RTD resistance directly without a 4-20mA transmitter loop, making TE (Temperature Element) the correct ISA designation. TIT-09-003 service conflict resolved — CIP Pump motor temperatures are now TE-09-003 (winding) and TE-09-004 (bearing); CIP Tank process temperature is TIT-09-006 (Rosemount 644 transmitter, 4-20mA on 5069-IF8). All motor sensors specified as Pt-100, 3-wire RTD per ET — Motors and Electrical Equipment.

**Transmittal N10 OBS-02 — CLOSED:** Verified in Data Transfer List Rev B (Section 2.6).

**Transmittal N10 OBS-03 — CLOSED:** Verified in Data Transfer List Rev B (Section 2.6).

#### NOTE-02 — Analyzer power supply voltage discrepancy (MAJOR)

IO List REMARKS specifies "220VAC Supply" for ORPIT-09-001A, CIT-09-001B, CIT-09-004, CIT-09-005, and PHIT-09-006. Instrument List Rev C specifies 24VDC for all instruments, confirmed by CCS. These five analyzers handle brine quality and pH monitoring — an incorrect voltage specification in either document will result in equipment damage or interface circuit redesign during commissioning. BW Water must resolve this discrepancy and confirm the definitive supply voltage prior to IFC (Rev 0).

*Technical Basis: ET — Instrumentation*

---

### 2.5 Instrument List Rev C — P22-LI-09-008-003

**Response Code: 2 — Approved as Noted**

39 instruments. Vibration transmitters changed to Wilcoxon PCH420V-M12 (was IFM VTV122), HART 7.0 confirmed. Motor temperature sensors registered: TE-09-001/002 (Fedco PT100, HP Pump), TE-09-003/004 (Grundfos PT100, CIP Pump), TIT-09-006 (Rosemount 214C+644, CIP Tank).

**Transmittal N8 OBS-01 — CLOSED:** CIT-09-005 power supply corrected to 24VDC.

**Transmittal N8 OBS-02 — CLOSED:** IO List and Instrument List aligned.

**Transmittal N8 OBS-03 — CLOSED:** Conductivity ranges corrected. CIT-09-001B, CIT-09-004, CIT-09-005 now 0-200 mS/cm with Rosemount 228 toroidal sensors. CIT-09-002 and CIT-09-003 (permeate) retain 0-20 mS/cm with Rosemount 400 contacting sensors. Technology split is appropriate: toroidal for brine above 20 mS/cm, contacting for permeate.

**Transmittal N8 OBS-04 — OPEN:** Vibration alarm setpoints deferred to separate "Alarm and Interlock Setpoints" document, not yet submitted. Tracked for IFC, not carried forward in Section 3.

#### NOTE-03 — Vibration transmitter calibrated range (MINOR)

Instrument List shows 0-127 mm/s for VT-09-001/002/003. Data Transfer List uses 0-25 mm/s. Wilcoxon PCH420V-M12 supports programmable full-scale from 12.7 to 127 mm/s. BW Water should confirm the intended PLC scaling and align both documents prior to IFC (Rev 0).

*Technical Basis: ET — Vibration Transmitters*

#### NOTE-04 — Working medium label for brine-side instruments (MINOR)

"Working Medium" column shows "Filtered Water" for CIT-09-001B, CIT-09-004, CIT-09-005, PIT-09-007, PIT-09-006, FIT-09-004, and PIT-09-008. These instruments operate in concentrated brine service (TDS > 43,000 mg/L). Working medium designation should reflect actual service conditions prior to IFC (Rev 0).

*Technical Basis: ET — Feed Brine Quality*

---

### 2.6 Data Transfer List (Modbus TCP/IP) Rev B — P22-LI-09-008-004

**Response Code: 2 — Approved as Noted**

189 Modbus entries (digital + analog). New entries: VE-09-015 (Feed TC Isolation, 6 entries), TIT-09-006 (register 30028), PHIT-09-006 (register 30031), TE-09-003/004 (registers 40077/40078).

**Transmittal N10 OBS-01 — CLOSED:** Motor temperature tags consistent with IO List Rev C. TE-09-001/002 (HP Pump) mapped to 5069-IY4 at holding registers 40075-40076, REAL data type (direct RTD reading). TE-09-003/004 (CIP Pump) at registers 40077-40078, same architecture. TIT-09-006 (CIP Tank) mapped to 5069-IF8 at input register 30028, 4000-20000 scaling (4-20mA transmitter). The TE/TIT distinction is architecturally consistent across all three instrumentation documents.

**Transmittal N10 OBS-02 — CLOSED:** Conductivity scaling corrected. CIT-09-001B (register 30004): 0-200 mS/cm. CIT-09-004 (register 30015): 0-200 mS/cm. CIT-09-005 (register 30023): 0-200 mS/cm. Permeate instruments CIT-09-002 (register 30019) and CIT-09-003 (register 30021): 0-200 uS/cm — microsiemens, appropriate for low-conductivity permeate.

**Transmittal N10 OBS-03 — CLOSED:** VE-09-014 has four entries (DI: 10004.6 IN REMOTE, 10004.7 FAULT; Analog: 40039 feedback, 40071 control) — duplication resolved. LS-09-001 present at 10002.5, LS-09-002 at 10002.6 — omissions resolved.

#### NOTE-05 — Vibration transmitter Modbus scaling (MINOR)

VT-09-001/002/003 Modbus scaled range shows 0-25 mm/s (registers 30007, 30011, 30016). Consistent with previous IFM VTV122 specification but may need updating for Wilcoxon PCH420V-M12. Align with Instrument List calibrated range (see NOTE-03) prior to IFC (Rev 0).

*Technical Basis: ET — Instrumentation*

---

### 2.7 Datasheet of Conductivity Analyzer Rev B — P22-LI-09-008-005

**Response Code: 1 — Approved**

Two sensor technologies properly specified:
- **CIT-09-002/003 (permeate):** Rosemount 400, contacting electrode, SS316/titanium, 0.1 uS/cm to 2,000 uS/cm.
- **CIT-09-001B/004/005 (brine):** Rosemount 228, toroidal non-contacting, Tefzel, 0.1 uS/cm to 2,000,000 uS/cm. Fluid medium identified as "RO Stage 1 & 2 Reject."

The contacting-to-toroidal technology change for brine service addresses the concern raised in Transmittal N8 OBS-03 and Transmittal N10 OBS-02. Tefzel provides adequate resistance to concentrated chloride solutions (45,000-55,000 ppm Cl- in second stage reject).

---

### 2.8 Datasheet of pH/ORP Analyzer Rev B — P22-LI-09-008-010

**Response Code: 1 — Approved**

TAG alignment changes only: ORPIT-09-001 renamed to ORPIT-09-001A, PHIT-09-001 renamed to PHIT-09-006, per P&ID Rev C. Rosemount 3900/1056 configuration unchanged.

---

### 2.9 Datasheet of Temperature Transmitter Rev B — P22-LI-09-008-013

**Response Code: 1 — Approved**

TIT-09-006 (CIP Tank): Rosemount 214C RTD (PT100, Class A, wire-wound RW) with 644 head-mount transmitter, 4-20mA + HART, flange DN40.

**Transmittal N8 OBS-01 — CLOSED:** Header corrected from "Pressure Transmitter" to "Temperature Transmitter."

**Transmittal N8 OBS-02 — CLOSED:** TAG corrected from TIT-09-003 to TIT-09-006 per P&ID Rev C. Aligned with Instrument List Rev C and IO List Rev C.

**Transmittal N8 OBS-03 — CLOSED:** Accuracy Class A specified. Part number in CCS indicates 214CRWSSA1S3E0100SL (wire-wound RW, Class A). Note: Instrument List Rev C shows 214CRWSSA1S3E0120SL — the positional difference (0100 vs 0120) corresponds to sensor length (10" vs 12"). BW Water should confirm the definitive part number before procurement.

---

### 2.10 Datasheet of Vibration Transmitter Rev B — P22-LI-09-008-014

**Response Code: 1 — Approved**

Model changed from IFM VTV122 to **Wilcoxon PCH420V-M12**. Quantity corrected to 3 units.

**Transmittal N12 OBS-01 — CLOSED:** Wilcoxon PCH420V-M12 provides 4-20mA + HART 7.0 as native capability. Three programmable analysis bands (PV, SV, TV). HART deficiency that caused Code 3 in Transmittal N12 is resolved.

**Transmittal N12 NOTE-01 — CLOSED:** Quantity field corrected from 1 to 3. Matches VT-09-001 (HP Pump), VT-09-002 (Feed Turbocharger), VT-09-003 (Interstage Turbocharger).

ET compliance verified: 0-127 mm/s programmable, 10-1000 Hz, +/-5% accuracy, PZT shear, SS316L, IP67, 12-30 VDC.

---

### 2.11 Datasheet of Flow Transmitter Rev B — P22-LI-09-008-007

**Response Code: 1 — Approved**

Five Rosemount 8750W electromagnetic flowmeters (FIT-09-001 through 005). Two specification sheets: page 2 covers FIT-09-001/002/003/005 (filtered water and CIP service), page 3 covers FIT-09-004 (train reject, concentrated brine service).

**Transmittal N8 Fluid/Medium note — RESOLVED:** FIT-09-004 specification sheet now correctly identifies "Concentrated Brine" as the fluid medium. Rev A carried "Filtered/CIP Water," which was inconsistent with the actual service conditions (TDS 75,000-93,000 mg/L at second stage reject). The Nickel alloy 276 (Hastelloy C-276) electrode selection for FIT-09-004 remains appropriate for this service. The four remaining flowmeters retain "Filtered/CIP Water" and SS316L electrodes, consistent with their actual service.

**Transmittal N8 Power Supply note — RESOLVED:** Power supply field corrected from "90 to 250 VDC" (Rev A) to "12 to 42 VDC" (Rev B) on both specification sheets. Now aligned with IO List Rev C (24VDC, 4-wire) and the ordered variant prefix 'D' (low-power DC model).

ET compliance confirmed: electromagnetic measurement, 4-20mA with HART, Rosemount (recognized manufacturer), PTFE lining, IP66, flanged process connections.

Note: Instrument List Rev C still carries "Filtered Water" as Working Medium for FIT-09-004 — this is addressed in NOTE-04 (Section 2.5) and remains applicable for the next IL revision.

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

Twelve observations closed in this transmittal: TM N10 OBS-01/02/03/04, TM N11 OBS-01/02/NOTE-01, TM N12 OBS-01/NOTE-01, TM N8 OBS-01/02/03. Five remain open.

| Obs | Document | Description | Outstanding Since | Status |
|-----|----------|-------------|-------------------|--------|
| TM N10 OBS-05 | GA Antiscalant Dosing Tank | Working volume, body material, seismic anchor data (NCh 2369 Zone 3) absent | TM N10 (12-Mar-2026) | PARTIALLY ADDRESSED — P&ID Rev C shows 0.34 m3. GA Rev B still required |
| TM N10 NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | Committed at Transmittal N4 — not submitted | TM N4 (03-Feb-2026) | OPEN — 69 days outstanding |
| TM N11 OBS-03 | Grounding Point Layout Rev B | Equipment positions from rejected Piping Layout Rev A | TM N11 (17-Mar-2026) | OPEN — pending Equipment Layout Rev B |
| TM N11 OBS-04 | Instrument Location Layout Rev B | Same basis as OBS-03 | TM N11 (17-Mar-2026) | OPEN — pending Equipment Layout Rev B |
| TM N13 NOTE-02 | Cable Tray Layout drawings | Internal cable routing not submitted | TM N13 (06-Apr-2026) | OPEN — tracked in ADASA email 10-Apr-2026 |

Note: TM N12 NOTE-02 (Line List SCH 80S), TM N13 NOTE-01 (P&ID CIP Tank capacity), and TM N8 OBS-04 (vibration setpoints) are tracked for IFC Rev 0.

---

## 4. ATTACHMENTS

| Document | Annotated File | Annotations |
|----------|---------------|-------------|
| Valve List Rev D | P22-LI-09-005-002_D_Valve_List_CC_ADASA.pdf | NOTE-01 |
| I/O List Rev C | P22-LI-09-008-001_C_IO_List_CC_ADASA.pdf | NOTE-02 |
| Instrument List Rev C | P22-LI-09-008-003_C_Instrument_List_CC_ADASA.pdf | NOTE-03, NOTE-04 |
| Data Transfer List Rev B | P22-LI-09-008-004_B_Data_Transfer_List_CC_ADASA.pdf | NOTE-05 |

Control System Architecture Rev D, Datasheet of Pressure Gauge Rev B, Datasheet of Conductivity Analyzer Rev B, Datasheet of pH/ORP Analyzer Rev B, Datasheet of Temperature Transmitter Rev B, Datasheet of Vibration Transmitter Rev B, and Datasheet of Flow Transmitter Rev B are approved without annotations.

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|-------------|-------|-----|---------------|
| P22-CD-09-004-001 | Control System Architecture | D | 1 — Approved |
| P22-LI-09-005-002 | Valve List | D | 2 — Approved as Noted |
| P22-LI-09-008-011 | Datasheet of Pressure Gauge | B | 1 — Approved |
| P22-LI-09-008-001 | I/O List | C | 2 — Approved as Noted |
| P22-LI-09-008-003 | Instrument List | C | 2 — Approved as Noted |
| P22-LI-09-008-004 | Data Transfer List (Modbus TCP/IP) | B | 2 — Approved as Noted |
| P22-LI-09-008-005 | Datasheet of Conductivity Analyzer | B | 1 — Approved |
| P22-LI-09-008-010 | Datasheet of pH/ORP Analyzer | B | 1 — Approved |
| P22-LI-09-008-013 | Datasheet of Temperature Transmitter | B | 1 — Approved |
| P22-LI-09-008-014 | Datasheet of Vibration Transmitter | B | 1 — Approved |
| P22-LI-09-008-007 | Datasheet of Flow Transmitter | B | 1 — Approved |

**Overall Transmittal Verdict: 2 — APPROVED AS NOTED**

Twelve observations closed (TM N10 OBS-01/02/03/04, TM N11 OBS-01/02/NOTE-01, TM N12 OBS-01/NOTE-01, TM N8 OBS-01/02/03). Five notes raised on E26–E28 documents — two major (PSV removal justification, analyzer voltage discrepancy), three minor (vibration scaling, working medium labels, Modbus range alignment). Flow Transmitter Rev B (E29) approved without observations — both Transmittal N8 inline notes resolved. Five observations remain open per Section 3.
