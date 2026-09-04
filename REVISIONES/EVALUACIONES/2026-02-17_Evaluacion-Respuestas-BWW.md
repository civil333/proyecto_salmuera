---
titulo: "Evaluation of BW Water Responses to Transmittals N3, N4 and Schedule"
codigo: "P22-IT-06-000-001-0"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
nombre_planta: "TALTAL"
cliente: "ADASA"
---

# EXECUTIVE SUMMARY

On February 16, 2026, BW Water submitted responses to three pending items: Transmittal N3 (P22-TM-09-000-003-0), Transmittal N4 (P22-TM-09-000-004-0), and schedule-related requests from ADASA's February 10 email. This document presents ADASA's formal evaluation of each response and serves as preparation material for the coordination meeting scheduled for February 18, 2026.

The responses are partial. BW Water addressed 6 of 17 observations from TM N3 and 5 of 10 from TM N4. Several accepted items (Pt-100 sensors, vibration transmitters, duplicate TAG correction, A/C n+1) represent meaningful progress. However, two items stand out as critically deficient: the Modbus TCP Memory Map (program not started after 42 days) and the Container 60ft configuration (under review for three months after formal rejection).

The schedule response includes a significant commitment: BW Water confirmed that no purchase orders will be issued before ADASA approves the relevant datasheets. This addresses one of ADASA's principal concerns regarding procurement sequencing.

| Category | Count | Percentage |
|----------|-------|------------|
| Accepted | 6 | 22% |
| Insufficient | 4 | 15% |
| Not Addressed | 7 | 26% |
| Remaining (TM N3) | 11 | 37% (minor/medium observations) |
| **Total Observations** | **27** | |

# EVALUATION OF TM N3 RESPONSES

## Response Coverage

BW Water responded to 6 of 17 observations from Transmittal N3 (P22-TM-09-000-003-0), submitted January 28, 2026. The response was received 19 days after transmittal issuance.

## Evaluation Table

| OBS | Subject | BW Water Response | ADASA Evaluation | Status |
|-----|---------|-------------------|------------------|--------|
| OBS-01 | Missing vibration transmitters (IL) | Will include VT for HP Pump, Feed TC, Interstage TC per ET 5.5.7 | Commitment accepted. Pending inclusion in revised Instrument List and Layout. | **Accepted** |
| OBS-02 | SEC calculation incomplete | Not addressed | Remains open. SEC calculation with turbocharger energy recovery needed. | **Pending** |
| OBS-03 | VM-09-015 manual DN100 ANSI 900# | Referenced but no explicit confirmation of actuation change | Insufficient. Must explicitly confirm electric actuation per ET 5.2.3. | **Insufficient** |
| OBS-04 | Missing DO for module status | Requested clarification on external system | ADASA has clarified: external PLC outside BWW scope, standard DO signal (0=stopped, 1=running). | **Pending BWW** |
| OBS-05 | Missing DI for external enable | Requested clarification on external system | ADASA has clarified: standard DI signal (1=authorized, 0=must stop). Hardwired, not Modbus. | **Pending BWW** |
| OBS-06 | Missing Pt-100 HP Pump motor windings | Will include Pt-100 for windings and bearings per ET 5.3 | Commitment accepted. Pending inclusion in revised HP Pump datasheet. | **Accepted** |
| OBS-07 | CIP Pump missing RTDs bearings | Will include RTDs per ET 5.1.4 | Commitment accepted. CIP Pump datasheet still required. | **Accepted** |
| OBS-08 | CIP Pump missing Pt-100 motor | Will include Pt-100 per ET 5.3 | Commitment accepted. Pending in CIP Pump datasheet delivery. | **Accepted** |
| OBS-09 | Temperature switches vs transmitters | Not addressed | Remains open. TSH (DI) should be replaced or supplemented with TIT (AI, 4-20mA+HART). | **Pending** |
| OBS-10 | Layout inherits duplicate TAG | Will be corrected when FIT-09-001 is resolved | Accepted as dependency. Layout revision follows IL correction. | **Accepted (conditional)** |
| OBS-11 | Duplicate TAG FIT-09-001 (IL) | Will renumber 2nd Stage Permeate to FIT-09-002 | Accepted. Standard correction, aligns with IO List. | **Accepted** |
| OBS-12 | Duplicate TAGs in Valve List | Not addressed | VM-09-015, VE-09-008, VE-09-010 duplicates remain open. | **Pending** |
| OBS-13 | TAGs with incorrect area code | Not addressed | VM-07-005, VM-07-031, VE-07-009 corrections remain open. | **Pending** |
| OBS-14 | Equipment List vs P&ID discrepancies | Not addressed | Static Mixer TAG, CIP Tank capacity, Antiscalant Tank, Dosing Pump discrepancies remain. | **Pending** |
| OBS-15 | Missing VFD electrical variables (IO List) | Responded about VFD communication protocol | Insufficient. Requirement is for electrical variables (V, A, kW, Hz, T) as AI signals for SEC calculation, not protocol. | **Insufficient** |
| OBS-16 | Missing DO module status (IO List) | See OBS-04 | Clarification provided. Awaiting BWW confirmation of inclusion. | **Pending BWW** |
| OBS-17 | Missing DI external enable (IO List) | See OBS-05 | Clarification provided. Awaiting BWW confirmation of inclusion. | **Pending BWW** |

## Summary TM N3

| Status | Count | Observations |
|--------|-------|--------------|
| Accepted | 6 | OBS-01, 06, 07, 08, 10, 11 |
| Insufficient | 2 | OBS-03, 15 |
| Pending BWW (clarification provided) | 3 | OBS-04, 05, 16/17 |
| Pending (not addressed) | 6 | OBS-02, 09, 12, 13, 14 |
| **Total** | **17** | |

# EVALUATION OF TM N4 RESPONSES

## Response Coverage

BW Water responded to 5 of 10 observations from Transmittal N4 (P22-TM-09-000-004-0), submitted February 5, 2026. The response was received 11 days after transmittal issuance.

## Evaluation Table

| OBS | Subject | BW Water Response | ADASA Evaluation | Status |
|-----|---------|-------------------|------------------|--------|
| OBS-01 | PLC specified at 60 Hz | PLC is dual-frequency (50/60 Hz auto-ranging) | Requires documentation. If confirmed in revised datasheet, observation can be closed. | **Accepted (conditional)** |
| OBS-02 | A/C without n+1 configuration | Will add 2nd A/C unit per ET 5.1.11 and Technical Offer | Commitment accepted. Pending updated Utility List and thermal calculation. | **Accepted** |
| OBS-03 | Missing A/C thermal calculation | Will deliver thermal calculation document | Commitment noted. No delivery date provided. | **Accepted (conditional)** |
| OBS-04 | Modbus TCP Memory Map not delivered | Program has not yet started | Unacceptable. 42 days since commitment (TM N2, Jan 6). Prerequisite for PLC-to-PLC interface design. Concrete delivery date required. | **Insufficient** |
| OBS-05 | Duplicate TAG FIT-09-001 (Layout) | Will correct when IL is updated | Accepted as dependency on IL correction (TM N3 OBS-11). | **Accepted (conditional)** |
| OBS-06 | Missing vibration transmitters (Layout) | See TM N3 OBS-01 | Accepted. Layout update follows IL update. | **Accepted (conditional)** |
| OBS-07 | Missing Pt-100 motor sensors (Layout) | See TM N3 OBS-06/07/08 | Accepted. Layout update follows datasheet updates. | **Accepted (conditional)** |
| OBS-08 | HP Pump power inconsistency | Not addressed | Four values (83/86/92/93 kW) across documents. Unification required before procurement. | **Pending** |
| OBS-09 | UPS not included in BOM | Not addressed | ET 5.4 requires UPS with 8h autonomy. Must be added to Control Architecture BOM. | **Pending** |
| OBS-10 | Container 60ft configuration | Still under review | Unacceptable. Rejected Nov 17, 2025 (+USD $67,208, +5 weeks). Three months without resolution. Definitive answer required. | **Insufficient** |

## Summary TM N4

| Status | Count | Observations |
|--------|-------|--------------|
| Accepted | 2 | OBS-02, 03 |
| Accepted (conditional) | 4 | OBS-01, 05, 06, 07 |
| Insufficient | 2 | OBS-04, 10 |
| Pending (not addressed) | 2 | OBS-08, 09 |
| **Total** | **10** | |

# EVALUATION OF SCHEDULE RESPONSE

## Items Confirmed

BW Water's schedule response included the following confirmations:

| Item | BW Water Statement | ADASA Evaluation |
|------|-------------------|------------------|
| Equipment basis | EXW Penang, Malaysia | Noted. Consistent with contract terms. Shipping to Florida noted (not Chile). |
| Shipping date | Estimated August 3, 2026 | Noted. Subject to engineering completion timeline. |
| No POs before approval | POs will not be issued before ADASA approves datasheets | Contractually significant. Recorded as formal commitment. Addresses ADASA concern about procurement before technical approval. |
| Engineering completion | April 24, 2026 | Extended from original 65-day baseline. Represents 139 calendar days. To be discussed in Feb 18 meeting. |

## Items Pending for February 18 Meeting

| Item | Requested | Status |
|------|-----------|--------|
| Delivery plan with milestones | Feb 10 email | Not yet received |
| Updated schedule with document dates | Feb 10 email | Not yet received |
| Document delivery schedule (14 pending + 16 in revision) | Jan 28 (TM N3) | Not yet received |

## Procurement Sequencing Analysis

The commitment to not issue POs before datasheet approval is particularly relevant for:

- **HP Pump:** Datasheet carries "To be revised" verdict. PR/PO was programmed for Feb 16 in BW Water's schedule. Power value must be unified (83/86/92/93 kW) and Pt-100 sensors confirmed before procurement.
- **Antiscalant system:** CT-001 evaluation issued Feb 16 with 4 pending observations (deadline Feb 20). Procurement was programmed for Feb 25-26.
- **Instruments:** Vibration transmitters and Pt-100 sensors now confirmed but not yet in datasheets or Instrument List.

# CT-001 STATUS

Technical Query CT-001 (Antiscalant Dosing Justification) was evaluated separately. The evaluation document (P22-CT-09-000-001-1) was issued on February 16, 2026, with a cover email to BW Water.

**Key findings from CT-001 evaluation:**

- 0.5 ppm dosing rate accepted in principle (AWC PROTON confirms positive safety margins)
- 4 observations pending (3 Major, 1 Minor):
  - Temperature basis: AWC projection at 19 degrees C, not 24 degrees C worst-case per ET Table 4-1
  - Strontium omitted from AWC input (0.00 vs measured 10-11 mg/L)
  - Silica input uses first sampling only (2.1 vs worst-case 6.4 mg/L)
  - Contradictory conclusions between AWC and CREST Water assessments
- Response deadline: February 20, 2026

CT-001 is tracked separately from transmittal observations and does not affect the evaluation in this document.

# CONSOLIDATED OUTSTANDING ITEMS

The following table consolidates all outstanding items requiring BW Water action, ordered by priority and age.

| # | Item | Source | Days Open | Priority | Status |
|---|------|--------|-----------|----------|--------|
| 1 | Modbus TCP Memory Map | TM N2/N4 OBS-04 | 42 | Critical | Program not started |
| 2 | Container 40ft confirmation | TM N4 OBS-10 | 92 (since rejection) | Critical | Under review |
| 3 | HP Pump power unification | TM N4 OBS-08 | 12 | Major | Not addressed |
| 4 | UPS in Control Architecture BOM | TM N4 OBS-09 | 12 | Major | Not addressed |
| 5 | VM-09-015 electric actuation | TM N3 OBS-03 | 20 | Critical | Response insufficient |
| 6 | VFD electrical variables for SEC | TM N3 OBS-15 | 20 | Critical | Response insufficient |
| 7 | Duplicate TAGs Valve List (3) | TM N3 OBS-12 | 20 | Major | Not addressed |
| 8 | Area code corrections Valve List | TM N3 OBS-13 | 20 | Minor | Not addressed |
| 9 | Equipment List vs P&ID discrepancies | TM N3 OBS-14 | 20 | Minor | Not addressed |
| 10 | Temperature switches vs transmitters | TM N3 OBS-09 | 20 | Major | Not addressed |
| 11 | SEC calculation with energy recovery | TM N3 OBS-02 | 20 | Medium | Not addressed |
| 12 | DO/DI external coordination signals | TM N3 OBS-04/05 | 20 | Critical | Clarification provided Feb 17 |
| 13 | Delivery plan with milestones | Feb 10 email | 7 | High | Expected Feb 18 |
| 14 | Document delivery schedule | TM N3 (Jan 28) | 20 | High | Expected Feb 18 |
| 15 | CT-001 pending observations (4) | CT-001 eval | 1 | High | Deadline Feb 20 |
| 16 | A/C thermal calculation | TM N2/N4 OBS-03 | 42 | Critical | Committed, no date |

# RISK ASSESSMENT

| Risk | Probability | Impact | Trigger | Mitigation |
|------|-------------|--------|---------|------------|
| Modbus Map delays PLC interface design | High | High | If not delivered by end of February, ADASA cannot complete PLC-to-PLC communication design | Escalate at Feb 18 meeting. Request firm deadline with weekly progress updates. |
| Container 60ft imposed without approval | Medium | Very High | If BW Water proceeds with 60ft without ADASA approval, cost and schedule impact apply to BW Water per contract | Require written confirmation at Feb 18 meeting. If 60ft is needed, formal change request is mandatory. |
| HP Pump procured with wrong power rating | Low (reduced) | High | With BWW commitment to not issue POs before approval, risk is reduced but not eliminated if approval process is slow | Track datasheet revision. Power value must be unified before approval can be granted. |
| Antiscalant system sized incorrectly | Medium | Medium | If CT-001 observations not resolved by Feb 20, procurement (Feb 25-26) may proceed on incomplete basis | CT-001 deadline is Feb 20. If not met, ADASA should formally object to antiscalant procurement. |
| Engineering timeline not recoverable | Medium | Very High | If delivery plan on Feb 18 does not show credible recovery path, Apr 24 baseline may slip further | Review delivery plan critically at meeting. Compare against remaining document volume (30 documents). |
