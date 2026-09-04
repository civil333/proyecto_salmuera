---
codigo: P22-TM-09-000-008-0
tipo: Transmittal Tecnico ADASA → BW Water
idioma: English
fecha: 09-Mar-2026
revision: 0
submittal_E15: 25007-0015
submittal_E16: 25007-0016
fecha_entrega: 09-Mar-2026
fecha_revision: 09-Mar-2026
veredicto: 3 — TO BE REVISED
preparado_por: Luis Rivera
revisado_por: Luis Rivera
aprobado_por: Victor Gutierrez
---

# TECHNICAL REVIEW TRANSMITTAL N8 — SECOND STAGE RO BRINE MODULE
## P22-TM-09-000-008-0

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Eleven documents reviewed across Deliveries 15 and 16. Four approved; four approved as noted; three to be revised. Instrument List Rev B incorporates the vibration transmitters and motor RTDs requested in previous transmittals — two long-standing technical gaps now closed.

Three issues require revision. CIT-09-005 in the Instrument List specifies 120VAC — every other instrument operates at 24VDC. The Power Works Installation Drawing (P22-DWG-09-007-005) contains no grounding or earthing specifications. The Temperature Transmitter datasheet covers TIT-09-003, a tag absent from Instrument List Rev B with no IO point assigned. IO List Rev B must be submitted incorporating the seven new instruments from this revision.

The three brine-side conductivity transmitters (CIT-09-001, CIT-09-004, CIT-09-005) specify a 20 mS/cm maximum range. Design feed TDS of 43,000–53,000 mg/L implies expected conductivities well above this limit. BW Water must provide measured conductivity values for the Taltal brine and correct ranges in Rev C if the 20 mS/cm limit is insufficient.

---

## 2. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| Submittal 1 | 25007-0015 |
| Submittal 2 | 25007-0016 |
| Delivery date | 09-Mar-2026 |
| Review completion | 09-Mar-2026 |
| Total documents in submittal | 11 |
| Response code summary | 4× Code 1 (Approved), 4× Code 2 (Approved as Noted), 3× Code 3 (To be Revised) |
| Contract | C-4300 BW WATER SUPPLY-12803 V2 |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 Instrument List Rev B — P22-LI-09-008-003

**Response Code: 3 — To be Revised**

Rev B adds seven instruments addressing previous ADASA observations. Two anomalies prevent acceptance.

**Key additions confirmed in Rev B:**
- VT-09-001/002/003 (ifm VTV122, 4-20mA): Vibration monitoring — HP Pump, Feed Turbocharger, Interstage Turbocharger
- TE-09-001/002 (Fedco Pt-100, 3-wire): Bearing and winding temperature — HP Pump motor
- TE-09-003/004 (Grundfos Pt-100, 3-wire): Bearing and winding temperature — CIP Pump motor
- Conductivity and flow coverage confirmed at all five required locations. FIT-09-001 duplicate TAG corrected to FIT-09-002.

**Observation 1 — CIT-09-005 power supply inconsistency (MAJOR)**
Item 25 (CIT-09-005) specifies 120VAC; every other instrument in the list operates on 24VDC. The transmitter part number 1056-02-21-31-HT-UL confirms a deliberate AC-supply selection — the '-02-' position identifies the AC-powered variant. BW Water must confirm whether 220VAC was the intended supply voltage (correct the Instrument List accordingly) or provide the single-line diagram for a 120VAC distribution circuit within the module. Note: ADASA supplies 380VAC at the module terminals; 120VAC requires an additional step-down transformation not reflected in any submitted electrical drawing.
*Basis: ET — Voltages and Frequencies*

**Observation 2 — IO List must be updated to reflect Rev B additions (MINOR)**
Rev B adds seven instrument points absent from IO List Rev A (VT-09-001, VT-09-002, VT-09-003, TE-09-001, TE-09-002, TE-09-003, TE-09-004) and revises two TAGs (FIT-09-002, LIT-09-002). IO List Rev B must be submitted incorporating all changes.
*Basis: ET — Communication and Control System*

**Observation 3 — Brine-side conductivity transmitters: calibrated ranges incompatible with process conditions at three of five measurement points (MAJOR)**

ET Section 5.5.5 requires five conductivity transmitters covering the full process (feed, combined permeate, Stage 2 permeate, Stage 1 reject, and train reject). All five are present in Instrument List Rev B. Cross-referencing the calibrated ranges against Process Calculation P22-CD-09-009-001 Rev B reveals that three instruments — all on brine streams — carry ranges that are incompatible with their operating conditions. The two permeate-side instruments are adequate.

**CIT-09-001 — Feed brine (RO Cartridge Filter Discharge; ET §5.5.5 — feed to module):**
Calibrated range 0–2000 µS/cm (2 mS/cm). This point is on the feed brine line at the same TDS as the module inlet: 43,000–53,000 mg/L (ET — Feed Brine Quality). Expected conductivity is approximately 65–80 mS/cm — 33 to 40× the specified range.

**CIT-09-004 — Stage 1 reject (RO Skid; ET §5.5.5 — Stage 1 reject):**
Calibrated range 0–2000 µS/cm (2 mS/cm). The Instrument List describes the working medium as "Filtered Water" — incorrect; this instrument is on the Stage 1 concentrated brine reject line. Based on the overall recovery of 42.86% and Stage 1 configuration (6 vessels × 7 elements, Stage 1 reject flow ≈ 36 m³/h per Feed Turbocharger data in Process Calculation Rev B), Stage 1 reject TDS is estimated at 58,000–74,000 mg/L. Expected conductivity is approximately 85–108 mS/cm — 43 to 54× the specified range. Note — Instrument List must correct the working medium from "Filtered Water" to "Concentrated Brine" for this instrument in Rev C. BW Water should also confirm that the contacting Rosemount 400 with SS316L wetted parts is compatible with concentrated brine service at this concentration level.

**CIT-09-005 — Train reject (RO Skid; ET §5.5.5 — reject outlet):**
Calibrated range 0–20 mS/cm. Train reject TDS is approximately 75,500 mg/L at 43,000 mg/L feed and approximately 93,000 mg/L at 53,000 mg/L feed (Process Calculation P22-CD-09-009-001 Rev B). Expected conductivity is approximately 108–133 mS/cm — 5.4 to 6.7× the 20 mS/cm range. The Instrument List also incorrectly lists "Filtered Water" as working medium — correct to "Concentrated Brine" in Rev C.

**CIT-09-002 and CIT-09-003 — Permeate streams:**
Ranges 0–2000 µS/cm are adequate. Process Calculation gives combined permeate TDS of 165–360 mg/L (≈240–560 µS/cm) under all modelled scenarios; the ET guarantee limit of ≤500 mg/L TDS corresponds to approximately 700–800 µS/cm, within the specified range with margin.

BW Water must revise Instrument List Rev C with correct calibrated ranges for CIT-09-001, CIT-09-004, and CIT-09-005 that cover the full operating window at each measurement point. Note: ET §4.1 states that the TDS-to-conductivity relationship is to be formally agreed during detailed engineering. If measured conductivity values from actual Taltal brine samples differ materially from the TDS-based estimates above, BW Water must provide the measured data as the basis for range selection.

*Basis: ET — Conductivity Transmitters (§5.5.5); ET — Feed Brine Quality (§4.1); Process Calculation P22-CD-09-009-001 Rev B*

**Observation 4 — Vibration transmitters: alarm and trip setpoints not defined (MINOR)**
VT-09-001/002/003 (ifm VTV122, 0–25 mm/s RMS) are correctly listed; however, no alarm (high) or trip (high-high) thresholds are defined for any of the three points. BW Water must define and submit setpoints per ISO 10816-3 before Control Philosophy can incorporate vibration protection logic.
*Basis: ET — Vibration Transmitters: HP Pump and ERD units*

---

### 3.2 Datasheet of Conductivity Analyzer Rev A — P22-LI-09-008-005

**Response Code: 2 — Approved as Noted**

Rosemount 400 contacting sensor (CIT-09-001 through CIT-09-004) and Rosemount 228 toroidal sensor (CIT-09-005, concentrated brine reject) with 1056 transmitters; both 4-20mA HART. The toroidal sensor for the concentrated brine reject is technically appropriate. Note: the transmitter part number for CIT-09-005 (1056-02-21-31-HT-UL vs. 1056-03-20-30-HT-UL for the other four) confirms the AC-supply selection — this is the basis for §3.1 Observation 1. Cover page also shows incorrect document code P22-LI-09-008-003 — correct code is P22-LI-09-008-005. No additional action required on this document beyond these corrections.

---

### 3.3 Datasheet of Differential Pressure Switch Rev A — P22-LI-09-008-006

**Response Code: 1 — Approved.** Ashcroft 1132 (DPS-09-001), SPDT dry contact, SS316L, NEMA 4X. Consistent with DI assignment in the Instrument List. No observations.

*Note — Contractual basis: DPS-09-001 does not appear in ET Section 5.5 or Technical Offer Rev1. It was introduced by BW Water in Instrument List Rev B for cartridge filter differential pressure monitoring. This is a voluntary scope addition by BW Water; confirm scope in future submittals.*

---

### 3.4 Datasheet of Flow Transmitter Rev A — P22-LI-09-008-007

**Response Code: 2 — Approved as Noted**

Rosemount 8750W electromagnetic flowmeters (FIT-09-001 through 005), 4-20mA HART, 24VDC — consistent with ET — Flowmeters requirements. Note: FIT-09-004 specifies Hastelloy C-276 electrodes vs. SS316L for the other four. FIT-09-004 is the train reject flow transmitter (RO Skid, P22-DWG-09-02-P9); its Hastelloy C-276 electrodes are appropriate for concentrated brine service at estimated TDS of 75,000–93,000 mg/L (Process Calculation P22-CD-09-009-001 Rev B). The FIT-09-004 specification form (this datasheet, page 3, row 10) lists "Filtered/CIP Water" as the Fluid/Medium — the same incorrect value carried in Instrument List Rev B. Correct to "Concentrated Brine" in Rev B of this datasheet and in IL Rev C (addressed in Section 3.1, Observation 3).

---

### 3.5 Datasheet of Level Switch Rev A — P22-LI-09-008-008

**Response Code: 2 — Approved as Noted**

IFM KQ6005 capacitive proximity switches (LS-09-001/002), PNP digital output, consistent with DI assignment for antiscalant dosing tank level alarm. Note: datasheet cover sheet incorrectly states output as "4-20mA HART" — the KQ6005 is a discrete PNP/IO-Link device; the Instrument List Rev B correctly assigns DI. Correct the field in the next revision to prevent loop documentation errors.

---

### 3.6 Datasheet of Level Transmitter (Pressure Type) Rev A — P22-LI-09-008-009

**Response Code: 1 — Approved.** VEGA VEGABAR 82, CERTEC ceramic cell, 4-20mA HART, FFKM seal (LIT-09-002). Satisfies ET requirement for continuous CIP tank level measurement. No observations.

---

### 3.7 Datasheet of pH/ORP Analyzer Rev A — P22-LI-09-008-010

**Response Code: 1 — Approved.** Rosemount 3900 / 1056 dual-channel, covering PHIT-09-001 (pH) and ORPIT-09-001 (ORP) with two independent 4-20mA HART outputs. Consistent with Instrument List Rev B and adequate for CIP water service. No observations.

*Note — Contractual basis: pH and ORP measurement is not specified in ET Section 5.5. The basis for these instruments is Technical Offer Rev1 — Instrument List (Items 1 and 32: ORP at RO CF Discharge and pH at CIP Pump Discharge).*

---

### 3.8 Datasheet of Pressure Gauge Rev A — P22-LI-09-008-011

**Response Code: 1 — Approved.** Wika 233.50 Bourdon tube (PI-09-001 through 006); PI-09-003 through PI-09-006 include Wika 990.10 diaphragm seal with PTFE-lined wetted parts, appropriate for CIP and antiscalant service. No observations.

---

### 3.9 Datasheet of Pressure Transmitter Rev A — P22-LI-09-008-012

**Response Code: 2 — Approved as Noted**

Schneider Foxboro IGP05S (2-wire, 4-20mA HART), nine pressure points (PIT-09-001 through 009). SS316L for lower-pressure/permeate service; Hastelloy C for PIT-09-006/007/008. Note: PIT-09-006 (Stage 2 Reject) and PIT-09-008 (Train Reject) justify Hastelloy C for brine service; BW Water should confirm the process fluid at PIT-09-007 (Interstage Turbo to Feed Turbocharger) to document the material selection basis.

---

### 3.10 Typical Installation Details of Power Works Rev A — P22-DWG-09-007-005

**Response Code: 3 — To be Revised**

Seven standard installation details (centrifugal pump motor wiring, dosing pump, heater panel, PLC/LCP panel, three cable tray configurations). Cable type and tray segregation are adequate.

**Observation 1 — No grounding or earthing specifications (MAJOR)**
The document contains no grounding or earthing specifications for any installation scenario — no equipment earth conductors, no tray bonding, and no shield termination guidance for instrument cables. Rev B must include: (1) equipment grounding conductor sizing and termination for motors and panels; (2) cable tray bonding continuity requirements; (3) analog/instrument cable shield termination method and grounding point.
*Basis: ET — Motors and Electrical Equipment; ET — Electrical and Control Systems*

**Observation 2 — No electrical installation standard cited (MINOR)**
No applicable installation code is referenced. BW Water must state the governing standard (IEC 60364, IEC 61439, NFPA 70, or applicable Chilean standard) in the revision block or general notes of Rev B.

---

### 3.11 Datasheet of Temperature Transmitter Rev A — P22-LI-09-008-013

**Response Code: 3 — To be Revised**

The datasheet covers TIT-09-003 (CIP Tank Temperature Transmitter): Rosemount 214C RTD (Pt-100, 3-wire, SS316 sheath), Rosemount 114C thermowell (SS316/316L, tapered stem), and Rosemount 644H transmitter (4-20mA HART, 24VDC, IP66). All three components satisfy ET — Instrumentation requirements for 4-20mA HART protocol and recognized manufacturers.

**Note 1 — Document header carries incorrect type designation**
The cover page header reads "Datasheet of Pressure Transmitter" while the document is a Temperature Transmitter datasheet. Technical content is not affected. Correct in next revision.

**Observation 2 — TIT-09-003 not listed in Instrument List Rev B (MAJOR)**
TIT-09-003 (this datasheet) is not in Instrument List Rev B and has no IO assignment. IL Rev B item 28 lists TIT-09-001 as the only CIP Tank temperature transmitter. BW Water must: (1) add TIT-09-003 to the next IL revision with its AI input point; (2) confirm whether TIT-09-001 and TIT-09-003 are distinct instruments at different locations, or whether one supersedes the other, and submit the datasheet for whichever tag remains unsubmitted.
*Basis: ET — Instrumentation; Instrument List Rev B item 28*

**Note 3 — Sensor accuracy class not specified**
The Rosemount 214C is available in standard (Class B) and Class A accuracy variants. The specification form does not indicate which accuracy class is required for TIT-09-003. BW Water should specify the required accuracy class for CIP process temperature measurement in the next datasheet revision.
*Basis: ET — Instrumentation (complete specification of instrument parameters)*

**Observation 3 — Temperature TAG inconsistency across documents (MAJOR)**
Cross-referencing this submittal against P&ID Rev B and Instrument List Rev B reveals three distinct temperature TAGs for what appear to be related instruments:
- **TIT-09-001**: Instrument List Rev B item 28 (CIP Tank Temperature Transmitter, Rosemount 644)
- **TIT-09-002**: P&ID Rev B sheet P10, HP Pump / Feed Turbocharger area — absent from IL Rev B
- **TIT-09-003**: This datasheet (CIP Tank Temperature Transmitter, Rosemount 644 + RTD 214C)

TIT-09-002 appears in P&ID Rev B but is not registered in IL Rev B and has no datasheet. TIT-09-001 and TIT-09-003 reference the same equipment description but carry different TAGs. BW Water must submit a consolidated resolution in Instrument List Rev C and P&ID Rev B: (1) confirm the definitive TAG for the CIP Tank temperature transmitter (TIT-09-001 or TIT-09-003); (2) confirm whether TIT-09-002 is a distinct instrument at the HP Pump or an error in P&ID Rev B; (3) if TIT-09-002 is a real instrument, add it to IL Rev C with an AI IO point assignment.
*Basis: ET — Instrumentation; P&ID Rev B; Instrument List Rev B item 28*

---

## 4. ATTACHMENTS

The following BW Water documents were reviewed as part of this transmittal.

| Attachment | Document Code | Title | Rev |
|------------|---------------|-------|-----|
| 1 | P22-LI-09-008-003 | Instrument List | B |
| 2 | P22-LI-09-008-005 | Datasheet of Conductivity Analyzer | A |
| 3 | P22-LI-09-008-006 | Datasheet of Differential Pressure Switch | A |
| 4 | P22-LI-09-008-007 | Datasheet of Flow Transmitter | A |
| 5 | P22-LI-09-008-008 | Datasheet of Level Switch | A |
| 6 | P22-LI-09-008-009 | Datasheet of Level Transmitter (Pressure Type) | A |
| 7 | P22-LI-09-008-010 | Datasheet of pH/ORP Analyzer | A |
| 8 | P22-LI-09-008-011 | Datasheet of Pressure Gauge | A |
| 9 | P22-LI-09-008-012 | Datasheet of Pressure Transmitter | A |
| 10 | P22-DWG-09-007-005 | Typical Installation Details of Power Works | A |
| 11 | P22-LI-09-008-013 | Datasheet of Temperature Transmitter | A |

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-LI-09-008-003 | Instrument List | B | 3 — To be Revised |
| P22-LI-09-008-005 | Datasheet of Conductivity Analyzer | A | 2 — Approved as Noted |
| P22-LI-09-008-006 | Datasheet of Differential Pressure Switch | A | 1 — Approved |
| P22-LI-09-008-007 | Datasheet of Flow Transmitter | A | 2 — Approved as Noted |
| P22-LI-09-008-008 | Datasheet of Level Switch | A | 2 — Approved as Noted |
| P22-LI-09-008-009 | Datasheet of Level Transmitter (Pressure Type) | A | 1 — Approved |
| P22-LI-09-008-010 | Datasheet of pH/ORP Analyzer | A | 1 — Approved |
| P22-LI-09-008-011 | Datasheet of Pressure Gauge | A | 1 — Approved |
| P22-LI-09-008-012 | Datasheet of Pressure Transmitter | A | 2 — Approved as Noted |
| P22-DWG-09-007-005 | Typical Installation Details of Power Works | A | 3 — To be Revised |
| P22-LI-09-008-013 | Datasheet of Temperature Transmitter | A | 3 — To be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED**
