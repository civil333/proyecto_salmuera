# TECHNICAL REVIEW TRANSMITTAL N17 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-017-0
**Date:** 05-May-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0035, 25007-0036, 25007-0037

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Nine documents across submittals 25007-0035, 25007-0036 and 25007-0037. Tally: 7 Code 2, 2 Code 3 (Alarm & Interlock List Rev A and Project Quality Plan Rev A — Rev B required for both before IFC).

Critical findings driving the verdict:

- **Alarm & Interlock List Rev A — unit error in permeate conductivity setpoints.** Items CIT-09-002 and CIT-09-003 declare operating range 0–20 mS/cm and setpoints AHH/AH/AL/ALL at 100–900 with units "mS/cm" — two orders of magnitude above the physical operating range. Values match a µS/cm reading. Rev B must reconcile units across operating range and setpoints before IFC.
- **Project Quality Plan Rev A — corporate template that does not close PIE Base.** Document carries form QAM-PQP-001 with inherited dates Issue 16-JUN-2025 / Effective 17-JUL-2025. No inspection matrix with numerical acceptance values, no Hold Points, no procedure codes for welding/NDT/PMI/hydrostatic/preservation/FAT, no FAT section, single placeholder ITP. PIE Base (P22-IT-09-000-001-0) is the minimum contractual baseline ADASA issued for this exact purpose. Rev B must close the matrix before any Hold Point of fabrication.
- **Pressure Transmitter Rev B — Hastelloy C extended to PIT-09-001/002/003/004/005/006/008** beyond the original PIT-09-007 reply on Rev A. PIT-09-009 remains SS316L. Confirm cost and lead-time impact on the Procurement Schedule in writing.
- **Grounding Layout Rev D — wrong Consolidated Comment Sheet embedded** (belongs to Cable Tray Layout P22-DWG-09-007-004). Replace and populate the revision history block.

Eleven observations from prior transmittals remain open as of 05-May-2026 — most critical: Plant Control Philosophy Rev C (TM N15, 1 CRITICAL on HP Pump permissive), Cable Tray Layout Rev C (TM N15, two items inherited from TM N4 outstanding 88 days), HMI Screenshots committed at TM N4 (89 days outstanding). Section 3 details the inventory.

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 IO List Rev 0 — P22-LI-09-008-001

**Response Code: 2 — Approved as Noted**

Issued for IFC. 135 IO points. Detailed comments: `P22-LI-09-008-001_0_IO_List_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MAJOR | Antiscalant Dosing Pumps (items 124–131) lack IN REMOTE DI — HP Pump (28) and CIP Pump (104) include it |
| NOTE-02 | MINOR | RTD range on items 39, 40, 114, 115 declared as "0–100 ΔΩ" — restate in °C |
| NOTE-03 | MINOR | Items 114 and 115 (CIP Pump RTDs) reference P&ID page P9 — should be P10 |

**NOTE-01 — Dosing Pumps remote status.** Add IN REMOTE DI to items 124–131 (BDS-09-001/002) so DCS applies uniform permissive logic across pumps.

**NOTE-02 — RTD range notation.** Restate items 39, 40, 114, 115 in °C with Pt-100 reference (60 °C → 138 Ω, 180 °C → 168 Ω). The Alarm & Interlock List already uses °C for the same instruments.

**NOTE-03 — CIP Pump P&ID page.** Items 114 and 115 (CIP Pump WTE/BTE) point to P9 (HP Pump page); correct to P10.

---

### 2.2 Data Transfer List (Modbus TCP/IP) Rev 0 — P22-LI-09-008-004

**Response Code: 2 — Approved as Noted**

Issued for IFC. 185 Modbus mappings (Coils, DI, Input/Holding Registers); ~28 spare slots. Detailed comments: `P22-LI-09-008-004_0_Data_Transfer_List_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MAJOR | PLC role (master/slave), byte order and endianness not declared |
| NOTE-02 | MAJOR | Vibration scaling 0–8.9 mm/s on registers 30007/30011/30016 below Wilcoxon PCH420V-M12 minimum full-scale 12.7 mm/s |

**NOTE-01 — Modbus integration parameters.** Add header note declaring PLC role (master/slave toward DCS), byte order for REAL/INT registers (AB-CD vs CD-AB) and word swap. CONNECT column suggests PLC as slave, but it must be stated explicitly to avoid commissioning trial-and-error.

**NOTE-02 — Vibration scaling vs Wilcoxon model.** Registers 30007/30011/30016 scaled 0–8.9 mm/s sit below the PCH420V-M12 datasheet minimum full-scale of 12.7 mm/s. Confirm actual transmitter model and full-scale setting, or revise scaling. Same physical question raised in Section 2.9 OBS-01.

---

### 2.3 Pressure Transmitter Datasheet Rev B — P22-LI-09-008-012

**Response Code: 2 — Approved as Noted**

Schneider Foxboro IGP05S, 4–20 mA HART, IP66/IP67, NEMA 4X, TÜV SIL3, accuracy ±0.075 % span. Detailed comments: `P22-LI-09-008-012_B_DS_Pressure_Transmitter_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Hastelloy C extended to PIT-09-001/002/003/004/005/006/008 — confirm procurement impact |
| NOTE-01 | MINOR | Page 2 declares "Material - Sealing: Aluminium" for PIT-09-009 — likely typo |

**OBS-01 — Hastelloy C material extension.** Hastelloy C is ~3× SS316L cost with longer lead time in the IGP05S configurator. Confirm in writing the impact on the Pressure Transmitter line item of the Procurement Schedule and confirm that turbocharger and feed equipment delivery dates do not extend. PIT-09-009 (low-TDS Combined Permeate) remains SS316L.

**NOTE-01 — Sealing material.** Aluminium is implausible for a brine module sealing material. Correct page 2 entry (typically Viton, EPDM or PTFE for the SS316L low-pressure unit) on the IFC issue.

---

### 2.4 Grounding Point & Power Panel Location Layout Rev D — P22-DWG-09-007-003

**Response Code: 2 — Approved as Noted**

Rev D (30-Apr) follows Rev C approved as Code 2 in TM N15 (17-Apr). Detailed comments: `P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Embedded Consolidated Comment Sheet belongs to Cable Tray Layout (P22-DWG-09-007-004), not to this drawing |
| NOTE-01 | MINOR | Revision history block on title block has letters and dates but no change description |
| NOTE-02 | MAJOR | Detail referenced from this drawing is missing — confirm presence in Typical Installation Details of Power Works (P22-DWG-09-007-005) |

**OBS-01 — Wrong Consolidated Comment Sheet.** Page 2 contains the comment-closure sheet for P22-DWG-09-007-004 (Cable Tray Layout), not for this drawing. Replace with the correct sheet documenting how the TM N15 NOTE on Rev C was incorporated into Rev D.

**NOTE-01 — Empty revision description.** Fill in the description column for rows A, B, C, D so revision intent is auditable on the drawing.

**NOTE-02 — Missing detail cross-reference.** Page 3 references a typical detail that is not included in this drawing. Confirm that the detail is provided in the Typical Installation Details of Power Works drawing (P22-DWG-09-007-005); if it is not, issue the detail in the next revision so the cross-reference resolves.

---

### 2.5 Typical Installation Details of Power Works Rev 0 — P22-DWG-09-007-005

**Response Code: 2 — Approved as Noted**

Issued for IFC after Rev A (02-Mar) and Rev B (19-Mar). Eight typical detail sections plus seven grounding-link methods. Detailed comments: `P22-DWG-09-007-005_0_Typical_Power_Works_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MAJOR | All notes cite NEC (US) — confirm SEC / NCh Eléct. 4/2003 as governing standard |
| NOTE-02 | MAJOR | Page 10 note 5 leaves two alternative methods for pump motor grounding open |
| NOTE-03 | MAJOR | Page 6 typical detail — feed direction unclear; module is on the opposite side of the diagram |
| NOTE-04 | MAJOR | Page 6 — incoming feed actually arrives via duct bank from electrical room (ADASA scope); update typical detail to reflect interface boundary |

**NOTE-01 — Chilean electrical regulation.** Notes cite NEC Articles 392.30(B), 352 and Table 250.122. The applicable regulation for installation in Chile is SEC and NCh Eléctrica 4/2003 / IEC 60364 (basis for the SEC compliance Hold Point in ITP Offsite item 7.7). Confirm in writing that SEC/NCh governs and NEC is cited as supplementary practice; where the standards diverge (e.g. ground wire cross-section), the Chilean regulation prevails.

**NOTE-02 — Pump grounding method.** Page 10 note 5 lists two alternative methods (motor structure → tray/skid; motor cable ground terminal). Select one standard method for the project and document it in the installation procedure before site works.

**NOTE-03 — Feed direction on typical detail.** Page 6 shows the feed routed towards the module as the supply to downstream consumers, but the module is on the opposite side of the diagram. The orientation reads inverted relative to the actual physical layout. Reorient the typical detail or annotate the flow direction explicitly so the construction contractor does not mirror the installation by mistake.

**NOTE-04 — Incoming feed via duct bank from electrical room.** The main incoming feed will be routed via duct bank from the electrical room, which is part of ADASA scope. The typical detail should reflect this interface boundary — the BW Water side of the diagram should show the termination point of the ADASA duct bank and the cable entry to the LCP, not a generic incoming line. Update the detail before IFC.

---

### 2.6 Project Quality Plan Rev A — P22-BA-09-000-003

**Response Code: 3 — To Be Revised**

Document is a BW Water corporate template (form QAM-PQP-001, inherited dates Issue 16-JUN-2025 / Effective 17-JUL-2025) with six generic sections and a single placeholder ITP. ADASA issued P22-IT-09-000-001-0 (PIE Base) as the minimum contractual baseline that the supplier's Quality Plan must close: an inspection matrix with source document, numerical acceptance value, tolerance, frequency, intervention type (H/W/S/R) and documentary evidence per item. Rev A does not close any cell of that matrix. Detailed comments: `P22-BA-09-000-003_A_PQP_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | Inspection matrix absent — PQP Section 6.1 lists four generic objectives that do not close PIE Base Sections 5–11 |
| OBS-02 | CRITICAL | FAT scope absent — no FAT section, no FAT procedure, no Acta de Aprobación FAT (BAE: 40% payment milestone) |
| OBS-03 | MAJOR | Procedure codes absent — Welding (ASME IX), NDT, PMI, Hydrostatic LP/HP, Preservation, FAT, Painting |
| OBS-04 | MAJOR | Hold and Witness Points not defined — PIE Base matrix has 12+ Hold Points; PQP defines no notification scheme |
| NOTE-01 | MAJOR | Document control: Cover Rev A vs internal Rev 0; code P22-BA-09-000-003 vs QAM-PQP-001; inherited template dates; cover signatures as initials |
| NOTE-02 | MAJOR | Section 7.1 lists single BWW-ITP-002 Offsite; row 2 truncated; Onsite/FAT/Commissioning ITPs missing |
| NOTE-03 | MAJOR | PMI commitment absent — PIE Base requires min 10% on Super Duplex UNS S32750 by XRF |
| NOTE-04 | MAJOR | Personnel certification not addressed — welders ASME IX, NDT inspectors ASNT, QA Manager qualification |
| NOTE-05 | MINOR | No organisation chart, no RACI, no NCR flow detail; ISO 9001:2015 cited without certificate attached |

**OBS-01 — Inspection matrix absent.** PIE Base Sections 5–11 require, per inspection item, the source reference, numerical acceptance value, tolerance, frequency, procedure code and intervention type. PIE Base is explicit: generic references ("según ET", "según plano", "práctica estándar") are not acceptable. PQP Section 6.1 lists four generic objectives that close no PIE cell. Issue Rev B with the PIE Detallado that closes each cell with project-specific values and procedure codes.

**OBS-02 — FAT scope absent.** PIE Base Section 7 defines nine FAT items, seven as Hold Points (procedure approval, visual, dimensional, PLC/HMI, SEC compliance, FAT Approval Certificate). BAE ties 40% of contract value to the Acta de Aprobación FAT. PQP Rev A has no FAT section, no procedure reference, no Hold Point scheme and no commitment to issue the Acta. Rev B must add a dedicated FAT section closing the nine PIE Base items.

**OBS-03 — Procedure codes absent.** ET — Supplier Responsibilities and PIE Base Section 6 require approved procedures for welding (ASME IX WPS/PQR), NDT, PMI, hydrostatic LP/HP, preservation, FAT and painting. Technical Offer Rev1 left these as "Manufacturer Standard Procedure" placeholders. Assign final codes per P00-IT-00-000-101 and submit each procedure for ADASA review before the first Hold Point of each activity.

**OBS-04 — Hold and Witness Points not defined.** PIE Base Section 4 sets H/W/S/R interventions with mandatory prior notification for H. The PIE Base matrix lists 12+ Hold Points (high-pressure hydrostatic, FAT 7.1/7.2/7.3/7.5/7.7/7.9, dossier final, release for shipment). PQP defines no taxonomy and no notification scheme. Rev B must adopt H/W/S/R and identify the Hold Points already declared in PIE Base.

**NOTE-01 — Document control inconsistencies.** Cover declares Rev A and code P22-BA-09-000-003. Page 2 internal header declares Rev 0 and code QAM-PQP-001 (BW Water corporate form) with inherited template dates Issue 16-JUN-2025 / Effective 17-JUL-2025. Cover signatures only as initials (MF, MZ, MAZ, AAR). Reconcile revision label, code, signatures and dates on Rev B.

**NOTE-02 — ITP coverage.** Section 7.1 lists single BWW-ITP-002 Offsite; row 2 truncated. Add Onsite, FAT and Commissioning ITPs aligned to PIE Base Sections 9 (site reception), 10 (installation) and 11 (performance tests), under codes per P00-IT-00-000-101.

**NOTE-03 — PMI commitment absent.** PIE Base Section 6 requires min 10% PMI on Super Duplex UNS S32750 by XRF; ET specifies the spectrometric method. Technical Offer Rev1 only commits MTR per EN 10204. The PQP must declare PMI procedure code, sampling percentage and matrix position. ADASA may require 100% on critical high-pressure welds.

**NOTE-04 — Personnel certification.** PIE Base requires welder qualification per ASME IX with 100% WPS/PQR verification and NDT inspectors per ASNT level. PQP Section 5 lists managerial roles only. Rev B must add a personnel qualification section listing welder, NDT inspector and QA Manager certifications.

**NOTE-05 — Organisation and ISO 9001.** Section 5 has no organisation chart and no RACI; Section 6.4 declares NCR control in a single sentence; Section 4.0 cites ISO 9001:2015 without certificate of compliance attached. Rev B should attach the certificate (with scope), add the chart and detail the NCR escalation path.

---

### 2.7 Inspection and Test Plan Offsite Rev A — P22-BA-09-000-004

**Response Code: 2 — Approved as Noted**

Structured ITP with 34 activities across eight sections covering 100% of PIE Base Sections 6, 7 and 8 (document review, workshop fabrication, pre-shipment). Nine Hold Points correctly placed (engineering review 1.1; FAT procedure approval 7.1; FAT visual and dimensional 7.2 and 7.3; PLC/HMI 7.5; SEC compliance 7.7; FAT Approval Certificate 7.9; final dossier 8.3; release for dispatch 8.4). Section 7 replicates the nine FAT items of PIE Base and lists the Acta de Aprobación FAT as a project deliverable, aligned with the BAE 40% payment milestone. Detailed comments: `P22-BA-09-000-004_A_ITP_Offsite_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Hydrostatic test pressures left as placeholders ("X bar", "Y bar") — items 5.1 and 5.2 |
| OBS-02 | MAJOR | Document control inconsistencies — code P22-BA-09-000-004 (cover) vs P22-BA-09-000-003 (page 2); Cover Rev A vs internal Rev 0; inherited template AQ-QAM-F017 Rev.3 Effective 23.06.2023; cover signatures as initials only (MF, MZ, MAZ, AAR) |
| OBS-03 | MAJOR | Procedure references — 22 placeholder codes across PROV-PROC, PROV-PLAN, PROV-CHK, PROV-LIST, PROV-DWG, PROV-CALC; PROV-PLAN-NDE-XXX (item 3.3) carries literal "XXX"; the NDE Plan itself is not delivered |
| NOTE-01 | MAJOR | PMI frequency on item 2.3 reads "Min. 10% or per Approved Quality Plan"; ASME B31.3 Chapter X typically requires 100% on welded Super Duplex HP joints — assign value |
| NOTE-02 | MAJOR | Personnel certification and NCR procedure not addressed as dedicated items — welder ASME IX, NDT inspector ASNT, QA Manager qualification missing; only "Closure of FAT NCRs" in item 7.9 without fabrication-wide NCR flow with escalation to ADASA |
| NOTE-03 | MINOR | Project Number "20.25.6501" (BW Water internal); add cross-reference to ADASA contract C-4300 / Project P22 |

**OBS-01 — Hydrostatic test pressures.** Items 5.1 (LP PVC) and 5.2 (HP Super Duplex) read "X bar" and "1.5 × Design Pressure = Y bar". Assign numerical values before the first hydrostatic Hold Point. For HP with design pressure ~83 bar (Stage 2 reject per Pressure Transmitter Datasheet Rev B), test pressure 125–150 bar; for LP, ≥1.5× max operating pressure of the section.

**OBS-02 — Document control inconsistencies.** Cover declares code P22-BA-09-000-004 with Revision A and date 30-Apr-2026; the page 2 internal header declares code P22-BA-09-000-003 (the PQP code) and Revision 0. The footer is built on the inherited template form AQ-QAM-F017 Rev.3 Effective 23.06.2023, evidence that the document was not regenerated for this project. Cover signatures appear as initials only (MF, MZ, MAZ, AAR) without legible names. Reconcile code, revision, signatures and template metadata on the IFC issue.

**OBS-03 — Placeholder procedure codes and missing NDE Plan.** The matrix references 22 placeholder codes spread across PROV-PROC (recepción, PMI, soldadura, VT, hidrostática LP/HP, eléctrica, FAT, preservación, embalaje), PROV-PLAN (NDE, fabricación, montaje), PROV-CHK (FAT visual/dimensional), PROV-LIST (dossier preliminar/final), PROV-DWG (UT plan), PROV-CALC (flexibilidad). Item 3.3 cites PROV-PLAN-NDE-XXX with the literal "XXX" sequence — the NDE Plan that PIE Base Section 6 mandates (RT/UT/PT with minimum percentages by joint type) is not delivered with this submittal. Assign final codes per P00-IT-00-000-101 and submit each procedure for ADASA review before the first Hold Point of each activity. The closure of these placeholders is contingent on the emission of the PQP Rev B, where the procedure register should be assigned.

**NOTE-01 — PMI frequency on item 2.3.** Reads "Min. 10% or per Approved Quality Plan" with reference to procedure XESSB/PMI/026-A. ASME B31.3 Chapter X and the project SCD specification typically require 100% PMI verification on welded Super Duplex joints for high-pressure service. Confirm final acceptance criterion in writing on the IFC issue.

**NOTE-02 — Personnel certification and NCR procedure.** PIE Base — Welding (Section 6) requires welder qualification per ASME IX with 100% verification of WPS/PQR before any production weld; the NDE Plan implies inspector qualification per ASNT (Levels II and III for VT, RT, UT, PT). Item 3.1 covers welder qualification implicitly within the WPS/PQR review, but no dedicated items exist for ASME IX welder certificate verification, ASNT NDT inspector qualification, or QA Manager qualification (the role expected to co-sign the FAT Approval Certificate with ADASA). Separately, item 7.9 mentions "Closure of FAT NCRs" only — there is no dedicated item for the fabrication-wide NCR procedure with the escalation path to ADASA that BAE — Inspection Procedures requires. Add personnel certification items and a NCR procedure item on the IFC issue.

**NOTE-03 — Project Number cross-reference.** Header lists Project Number 20.25.6501 (BW Water internal) and Document No. BWW-ITP-002 Rev. 0. Add cross-reference to ADASA contract C-4300 / Project P22 so the document is traceable across both numbering systems.

---

### 2.8 Alarm and Interlock List Rev A — P22-LI-09-008-015

**Response Code: 3 — To Be Revised**

First revision covering 33 instruments with up to four alarm levels each (AHH/AH/AL/ALL); severity 1 = trip / 2 = HMI alarm; time delays 1–10 s. Detailed comments: `P22-LI-09-008-015_A_Alarm_Interlock_List_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | Permeate conductivity setpoints two orders of magnitude above operating range — unit error mS/cm vs µS/cm |
| OBS-02 | CRITICAL | LS-09-002 declared as "Alarm High Alarm Low" — IO List has it as LSL |
| OBS-03 | MAJOR | Feed Turbo AHH triggers HMI only; Interstage Turbo AHH stops HP Pump — harmonise |
| NOTE-01 | MAJOR | Digital alarms (FAULT, MCCB trip) not tabulated — clarify HMI mapping |
| NOTE-02 | MINOR | HP Pump bearing AHH 90 °C — confirm against motor datasheet (typical 95–110 °C) |

**OBS-01 — Permeate conductivity unit error.** Items 11 (CIT-09-002) and 19 (CIT-09-003) declare operating range 0–20 mS/cm and setpoints ALL/AL/AH/AHH at 100/200/600/800 (item 11) and 100/200/700/900 (item 19) with units "mS/cm" — values match a µS/cm reading. SWRO permeate is 200–1 000 µS/cm typical. Reconcile units across operating range, instrument range and setpoint columns on Rev B.

**OBS-02 — Antiscalant Level Switch logic.** IO List declares LS-09-001 as LSH (item 122) and LS-09-002 as LSL (item 123). Item 33 of the A&I List describes LS-09-002 as "Alarm High Alarm Low" with action "Alarm + Stop Dosing Pump" (consistent with LSL dry-running protection but contradicts "Alarm High" wording). Reconcile description with LSH/LSL convention on Rev B.

**OBS-03 — Turbocharger vibration asymmetry.** Item 14 (VT-09-002 Feed Turbo AHH = 6.0 mm/s) action: "HMI Alarm Triggered". Item 15 (VT-09-003 Interstage Turbo AHH = 6.0 mm/s) action: "Alarm + Stop HP Pump". Same incipient-failure threshold should trigger same protective action. Harmonise to "Alarm + Stop HP Pump" on both, or document the engineering basis in the Notes column.

**NOTE-01 — Digital alarms not tabulated.** Pump/valve FAULT, MCCB trip and Antiscalant Tank LSH/LSL are present in the IO List but not tabulated here (only analog instruments with setpoints covered). Either extend with a digital-alarms section (alarm message, severity, action) or document that digital faults map directly to HMI without setpoint configuration.

**NOTE-02 — HP Pump bearing AHH setpoint.** Item 27 (TE-09-001) declares AHH = 90 °C with action "Alarm + Trip HP Pump". Typical AHH for a ~100 kW motor with anti-friction bearings is 95–110 °C; 90 °C may cause nuisance trips. Confirm against motor manufacturer datasheet on Rev B.

---

### 2.9 Instrument List Rev D — P22-LI-09-008-003

**Response Code: 2 — Approved as Noted**

Issued for Approval, submittal 25007-0037. 38 instruments. Detailed comments: `P22-LI-09-008-003_D_Instrument_List_CC_ADASA.pdf`.

**Material upgrades for high-TDS service introduced on Rev D**

| Tag (item) | Rev D material | Driver |
|------------|----------------|--------|
| DPS-09-001 (1) | Monel | High TDS |
| FIT-09-001 (4) | Nickel Alloy 276 + PTFE Lining | High TDS |
| PI-09-001 (10), PI-09-002 (24) | Superduplex 2507 diaphragm seal | High TDS |
| PIT-09-001/002/003/004/005 (5, 6, 11, 13, 20) | Hastelloy C | High TDS — also Section 2.3 OBS-01 |

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Wilcoxon PCH420V-M12 declared range 0–8.9 mm/s — below datasheet minimum 12.7 mm/s |
| NOTE-01 | MAJOR | Material upgrades (Monel, Nickel 276, Superduplex 2507) — confirm procurement impact |
| NOTE-02 | MINOR | VT-09-002 and VT-09-003 declare Working Medium "Filtered Water"; VT-09-001 declares "-" |
| NOTE-03 | MINOR | Consolidated Comment Sheet header references wrong project (25006 BWRO instead of 25007 Taltal) |

**OBS-01 — Wilcoxon model range coherence.** Items 7, 18 and 19 declare 0–8.9 mm/s rms with model PCH420V-M12, but the datasheet minimum programmable full-scale is 12.7 mm/s. Either confirm the model variant supports 0–8.9 mm/s with vendor citation, or revise the model on the IFC issue. Same question raised in Section 2.2 NOTE-02; single resolution covers both documents.

**NOTE-01 — Procurement impact.** Monel, Nickel 276 and Superduplex 2507 typically carry longer lead times and higher unit cost than SS316L. Confirm in writing the impact on the Equipment Procurement Schedule, in conjunction with the Hastelloy C confirmation under Section 2.3 OBS-01.

**NOTE-02 — Working medium on vibration transmitters.** Items 18 and 19 list "Filtered Water"; item 7 leaves "-". Vibration transmitters are mounted on motor casings and do not contact process fluid — column should read "-" for all three.

**NOTE-03 — Consolidated Comment Sheet header.** Pages 3–4 reference "Brackish Water Reverse Osmosis Project / 25006 / 25006-WTP-000-IC-LST-00002". Correct project is "P22-LI-09-008-003 / Second Stage RO Module for Brine – PD Taltal / 25007". Replace header before next revision; comment rows 1–7 remain valid.

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

Items open as of 05-May-2026.

| Origin TM | Document | Observation | Outstanding | Status |
|-----------|----------|-------------|-------------|--------|
| TM N4 OBS-06 | Cable Tray Layout (P22-DWG-09-007-004) | Vibration transmitter locations missing | 88 days | OPEN — awaiting Rev C, also subject of TM N15 |
| TM N4 OBS-07 | Cable Tray Layout (P22-DWG-09-007-004) | Pt-100 motor sensor locations missing | 88 days | OPEN — awaiting Rev C, also subject of TM N15 |
| TM N4 NOTE-05 | HMI Screenshots (P22-BREAD-09-008-001) | Committed at TM N4 — never submitted | 89 days | OPEN — formal commitment outstanding |
| TM N5 OBS-02 | Equipment Layout (P22-DWG-09-005-003) | Imperial dimensions retained as primary on Rev 0 | 70 days | PARTIALLY OPEN |
| TM N10 OBS-05 | GA Antiscalant Dosing Tank | Working volume, body material, seismic anchor data | 53 days | OPEN — GA Rev B still required |
| TM N11 OBS-03 | Grounding Layout (P22-DWG-09-007-003) | Grounding schedule completeness (PE identifiers, conductor cross-section, ring main topology, equipotential bonding per NCh Eléct. 4/2003 Section 10.0) | 48 days | OPEN — Rev D received in this transmittal does not include the schedule |
| TM N13 NOTE-02 | Cable Tray Layout drawings | Internal cable routing not submitted | 28 days | OPEN — tracked in ADASA email 10-Apr-2026 |
| TM N15 Section 2.4 | LCP Datasheet Rev A (P22-ET-09-007-005) | Code 3 — three OBS open (I/O modules + RTD channel count, IP rating, power consumption inconsistency) | 12 days | OPEN — Rev B awaited |
| TM N15 Section 2.8 | Cable Tray Layout Rev B (P22-DWG-09-007-004) | Code 3 — five new OBS plus two from TM N4 | 12 days new / 88 days inherited | OPEN — Rev C awaited |
| TM N15 Section 2.10 | Plant Control Philosophy Rev B (P22-BT-09-009-001) | Code 3 — 17 notes including NOTE-20 CRITICAL (HP Pump permissive TAG errors VE-09-007 / VE-09-014) | 12 days | OPEN — Rev C resubmittal awaited |
| TM N16 NOTE-01 | Civil and Loading Drawing Rev A (P22-DWG-09-005-001) | Modified container weight + RO Skid weight breakdown disclosure | 10 days | TRACKED for Rev 0 IFC (Code 2 — no new revision required) |

**Tracked for IFC Rev 0** (incorporate at IFC, no separate revision required):
- TM N12 NOTE-02 — Line List SCH 80S confirmation
- TM N13 NOTE-01 — P&ID CIP Tank capacity (6.81 vs 6.10 m³)


---

## 4. ATTACHMENTS

| Document | Annotated File | Annotations |
|----------|---------------|-------------|
| IO List Rev 0 | P22-LI-09-008-001_0_IO_List_CC_ADASA.pdf | NOTE-01, NOTE-02, NOTE-03 |
| Data Transfer List Rev 0 | P22-LI-09-008-004_0_Data_Transfer_List_CC_ADASA.pdf | NOTE-01, NOTE-02 |
| Pressure Transmitter Datasheet Rev B | P22-LI-09-008-012_B_DS_Pressure_Transmitter_CC_ADASA.pdf | OBS-01, NOTE-01 |
| Grounding Layout Rev D | P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf | OBS-01, NOTE-01, NOTE-02 |
| Typical Power Works Rev 0 | P22-DWG-09-007-005_0_Typical_Power_Works_CC_ADASA.pdf | NOTE-01, NOTE-02, NOTE-03, NOTE-04 |
| Project Quality Plan Rev A | P22-BA-09-000-003_A_PQP_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01, NOTE-02, NOTE-03, NOTE-04, NOTE-05 |
| ITP Offsite Rev A | P22-BA-09-000-004_A_ITP_Offsite_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02, NOTE-03 |
| Alarm & Interlock List Rev A | P22-LI-09-008-015_A_Alarm_Interlock_List_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02 |
| Instrument List Rev D | P22-LI-09-008-003_D_Instrument_List_CC_ADASA.pdf | OBS-01, NOTE-01, NOTE-02, NOTE-03 |

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-LI-09-008-001 | IO List | 0 | 2 — Approved as Noted |
| P22-LI-09-008-004 | Data Transfer List (Modbus TCP/IP) | 0 | 2 — Approved as Noted |
| P22-LI-09-008-012 | Datasheet — Pressure Transmitter | B | 2 — Approved as Noted |
| P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | D | 2 — Approved as Noted |
| P22-DWG-09-007-005 | Typical Installation Details of Power Works | 0 | 2 — Approved as Noted |
| P22-BA-09-000-003 | Project Quality Plan | A | 3 — To Be Revised |
| P22-BA-09-000-004 | Inspection and Test Plan Offsite | A | 2 — Approved as Noted |
| P22-LI-09-008-015 | Alarm and Interlock List | A | 3 — To Be Revised |
| P22-LI-09-008-003 | Instrument List | D | 2 — Approved as Noted |

**Overall Transmittal Verdict: 3 — TO BE REVISED** (driven by Alarm & Interlock List Rev A and Project Quality Plan Rev A — the remaining seven documents in this transmittal are Code 2)
