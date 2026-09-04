# TECHNICAL REVIEW TRANSMITTAL N12 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-012-0
**Date:** 30-Mar-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0022 / 25007-0023

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Deliveries 22 and 23 (25007-0022 / 25007-0023, received March 19 and 26, 2026) submit two documents. One MAJOR observation is raised on the Vibration Transmitter, plus two notation notes on the Line List.

Key findings:

- **Datasheet of Vibration Transmitter Rev A (Code 3 — To be Revised):** IFM VTV122 model proposed for VT-09-001, VT-09-002, and VT-09-003. The submitted datasheet specifies a single 4–20 mA analog output; HART communication capability is not documented. The Technical Specification — Instrumentation requires 4–20 mA + HART for all field instruments. BW Water must confirm whether the VTV122 model proposed supports HART and provide evidence in Rev B. If HART is not supported, BW Water must either propose a HART-capable alternative or submit a formal deviation with technical justification.

- **Line List Rev B (Code 2 — Approved as Noted):** Transmittal N3 OBS-01 is confirmed closed — line DA-SSD-DN80-09-005 (1st Stage RO Reject) design pressure updated to 80 bar (margin 17.6%). Two notation notes raised on pipe schedule designation and one unassigned line identifier.

---

## 2. DETAILED OBSERVATIONS BY DOCUMENT

### 2.1 Datasheet of Vibration Transmitter — P22-LI-09-008-014 Rev A

**Response Code: 3 — To be Revised**

The IFM VTV122 covers all three required measurement points (VT-09-001 at the RO HP Feed Pump BH-09-001, VT-09-002 at the Feed Turbocharger SIP-09-001, and VT-09-003 at the Interstage Turbocharger SIP-09-002). The MEMS technology, 0–25 mm/s RMS measurement range with 10–1000 Hz frequency band, and ISO 10816 compliance are noted. IP67/68/69K protection and SS316L housing are consistent with project requirements.

#### OBS-01 (MAJOR): HART Protocol Not Specified

**Document:** Datasheet of Vibration Transmitter — P22-LI-09-008-014 Rev A
**Severity:** Major

The VTV122 component datasheet (Section "Outputs Communication", Section "Inputs/outputs") specifies a single 4–20 mA analog current output. HART communication capability is not listed in the datasheet or in the manufacturer technical data pages.

The Technical Specification — Instrumentation states: *"El protocolo de la instrumentación deberá ser 4-20 mA + HART"* (4–20 mA + HART is required for all field instruments). No exception is provided in the Technical Specification — Vibration Transmitters section for vibration sensing devices.

**Required Action:** BW Water must address this item in Rev B with one of the following:
- Confirm that the VTV122 model proposed supports HART communication and provide manufacturer documentation as evidence, or
- Propose a HART-capable vibration transmitter meeting the measurement requirements (0–25 mm/s RMS, 10–1000 Hz, ISO 10816, IP67, SS316L housing), or
- Submit a formal deviation document citing the specific clause in the Technical Specification that permits omission of HART for vibration transmitters, with ADASA approval prior to procurement.

#### NOTE-01: Quantity Field Inconsistency

**Document:** Datasheet of Vibration Transmitter — P22-LI-09-008-014 Rev A
**Severity:** Informational

The datasheet header lists three component TAGs (VT-09-001/002/003), while the "Quantity - Duty" field on the same document reads 1. The project requires three physical units: one at the HP Feed Pump (BH-09-001), one at the Feed Turbocharger (SIP-09-001), and one at the Interstage Turbocharger (SIP-09-002). Confirm actual procurement quantity = 3 and update the field in Rev B.

---

### 2.2 Line List — P22-LI-09-009-003 Rev B

**Response Code: 2 — Approved as Noted**

**Transmittal N3 OBS-01 — CLOSED:** Line DA-SSD-DN80-09-005 (1st Stage RO Reject) design pressure increased from 70 bar to 80 bar. Operating pressure 68 bar, design pressure 80 bar: margin 17.6%. Consolidated Comment Sheet Page 4 confirms: "BW has revised accordingly." Observation closed.

CIP system lines are included in Rev B (lines CP-SSD-DN100-09-014 through CP-PVC-DN65-09-042), consistent with the CIP system scope. All high-pressure lines use Super Duplex Steel material and wall thicknesses consistent with the Technical Specification — High Pressure Piping requirements. Low-pressure lines are PVC Schedule 80.

#### NOTE-01: Unassigned Line Identifier — Make-Up for CIP

**Document:** Line List — P22-LI-09-009-003 Rev B
**Severity:** Informational

One line entry — "MAKE-UP FOR CIP" (PVC Schedule 80, DN80, 7.62 mm wall, P&ID Sheet P9) — has no LINE NO. assigned. All other lines in the document carry a unique identifier. Assign a line number consistent with the project numbering convention prior to IFC (Rev 0).

#### NOTE-02: Schedule Designation for Super Duplex Steel Lines

**Document:** Line List — P22-LI-09-009-003 Rev B
**Severity:** Informational

All Super Duplex Steel lines are designated "SUPER DUPLEX STEEL, SCH80" without the "S" suffix. Per ASME B36.19M, pipe schedules for stainless and duplex steel should be designated "Schedule 80S" to distinguish from carbon steel Schedule 80. The wall thicknesses listed are consistent with Schedule 80S values (DN100: 8.56 mm; DN80: 7.62 mm; DN65: 6.02 mm), confirming the intended specification. Correct the piping class designation to "SCH 80S" prior to IFC (Rev 0).

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

The following observations from Transmittals N10 and N11 remain open. No documents addressing these items have been received to date.

| Transmittal | OBS/NOTE | Document | Description | Status |
|-------------|----------|----------|-------------|--------|
| N10 | OBS-01 | I/O List Rev B | TAG inconsistency TE vs TIT for motor RTDs; TIT-09-003 service conflict (CIP Tank vs HP Pump Bearing) | OPEN — I/O List Rev C not received |
| N10 | OBS-02 | Data Transfer List Rev A | Conductivity scaling 0–20 mS/cm for brine lines (CIT-09-001/004/005); expected range 65–133 mS/cm | OPEN — Data Transfer List Rev B not received |
| N10 | OBS-03 | Data Transfer List Rev A | VE-09-014 duplicated in Modbus DI block; LS-09-001 and LS-09-002 absent from Modbus map | OPEN — Data Transfer List Rev B not received |
| N10 | OBS-04 | Control System Architecture Rev C | UPS 8-hour autonomy not confirmed — no load list or battery calculation provided | OPEN — Confirmation not received |
| N10 | OBS-05 | GA Antiscalant Dosing Tank Rev A | Effective working volume, body material, and seismic anchor data (NCh 2369 Zone 3) absent | OPEN — GA Rev B not received |
| N10 | NOTE-05 | Control System Architecture | HMI display screenshots P22-BREAD-09-008-001 committed at Transmittal N4; not yet submitted | OPEN |
| N11 | OBS-01 | Valve List Rev C | Duplicate TAG VE-09-007 — Items 44 and 64 | OPEN — Valve List Rev D not received |
| N11 | OBS-02 | Valve List Rev C | Duplicate TAG PSV-09-002 — Items 105 and 112 | OPEN — Valve List Rev D not received |
| N11 | OBS-03 | Grounding Point & Power Panel Location Layout Rev B | Equipment positions derived from Piping Layout Rev A, rejected in Transmittal N7 | OPEN — pending acceptance of Equipment Layout Rev B |
| N11 | OBS-04 | Instrument Location Layout Rev B | Same basis as OBS-03 | OPEN — pending acceptance of Equipment Layout Rev B |

ADASA requests BW Water to confirm the expected submission dates for I/O List Rev C, Data Transfer List Rev B, and Valve List Rev D, as these documents carry multiple Major open observations.

---

## 4. ATTACHMENTS

| Attachment | Document | Description |
|------------|----------|-------------|
| A | P22-LI-09-008-014_A_Datasheet of Vibration Transmitter_CC_ADASA.pdf | Annotated datasheet — OBS-01, NOTE-01 |
| B | P22-LI-09-009-003_B_Line List_CC_ADASA.pdf | Annotated Line List — NOTE-01, NOTE-02 |

---

## 5. RESPONSE SUMMARY

| Submittal No. | Document No. | Document Description | Rev | Response Code |
|---------------|-------------|---------------------|-----|---------------|
| 25007-0022 | P22-LI-09-008-014 | Datasheet of Vibration Transmitter | A | **3 — To be Revised** |
| 25007-0023 | P22-LI-09-009-003 | Line List | B | **2 — Approved as Noted** |
