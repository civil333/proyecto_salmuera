# TECHNICAL REVIEW TRANSMITTAL N19 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-019-0
**Date:** 25-May-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0042, 25007-0043, 25007-0044, 25007-0045

---

## 1. EXECUTIVE SUMMARY

This transmittal reviews thirteen documents from BW Water covering the electrical power package, the I/O List IFC submission, the project quality and instrumentation cabling package, and the cartridge filter datasheets for the Second Stage RO Brine Module. ADASA Technical Note P22-NT-09-000-001-0 is issued in parallel and is referenced explicitly in Sections 2.10, 2.12 and 2.13.

**TRANSMITTAL VERDICT: 3 — TO BE REVISED.** Submittals 25007-0042 to 25007-0045. Tally: 3 Code 1, 5 Code 2, 5 Code 3.

**Top 3 critical items to address:**

1. **ITP Offsite Rev B (Section 2.10) — ASME X certification scope.** The Rev B Consolidated Comment Sheet is silent on the "Test certification to ASME X" commitment per BW Water Technical Offer Rev1 ITP (Section 12) for the RO Pressure Vessels. Cross-reference to Technical Note P22-NT-09-000-001-0 clarifications 6.A and 6.C. Re-issue as Rev C with explicit declaration. Detailed annotations on the attached `*_CC_ADASA.pdf`.
2. **Cartridge Filters Rev D / Rev C (Sections 2.12 and 2.13) — H→V change and Sysflo vendor materialised pre-response.** Configuration change and vendor substitution under "or equal" implemented before ADASA's formal position on the 22-May Mitigation Plan. Cross-reference to Technical Note P22-NT-09-000-001-0 clarifications 5.A through 5.E. Re-issue once ADASA responds to the Technical Note. Detailed annotations on the attached `*_CC_ADASA.pdf`.
3. **Plant Control Philosophy Rev D (Section 3 carry-forward) — third consecutive transmittal.** HP Pump permissive CRITICAL reincident from TM N15 NOTE-20 → TM N18 OBS-01 → TM N19 carry-forward. ADASA reserves contractual remedies under Contract C-4300 if Rev D is not delivered within fourteen calendar days.

Notable closures in this cycle: Cable Tray Layout Rev C closes the longest-open inheritance in the project (seven items, 110 days open on the TM N4 entries). Project Quality Plan Rev B closes the two CRITICAL TM N17 observations on inspection matrix and FAT scope — a necessary prerequisite for the 40 percent payment milestone under BAE Clause 31 (release remains gated on the FAT Approval Certificate validation and the signed Acta de Aprobación FAT).

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 Electrical Load List Rev B — P22-LI-09-007-001

**Response Code: 1 — Approved**

Resubmittal of Rev A (Code 1 in TM N3). The Rev B load schedule (23 loads at 380 V 3-phase / 220 V single-phase 50 Hz, 144 kW totalised) matches the Single Line Diagram Rev B and the Datasheet of Power and Control Cable Rev B. Document accepted as-is.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverable tracked in Section 3: Pt-100 motor RTD declaration on the Motor Datasheet when issued.

---

### 2.2 Power Cable Schedule Rev B — P22-LI-09-007-002

**Response Code: 2 — Approved as noted**

Resubmittal of Rev A (Code 1 in TM N3). Rev B maps 26 cable runs with cross-sections from 70 mm² to 2.5 mm²; voltage drop below 3% on every circuit (worst case 1.62%).

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MINOR | REL-001 CIP Heater two-cable arrangement not aligned with the Single Line Diagram Rev B |

**Action to issue at IFC Rev 0 — no new Cable Schedule revision required:** clarify the REL-001 CIP Heater topology consistently across the Single Line Diagram and the Cable Schedule (one feed via VFD with control signals, or a separate control panel explicitly drawn).

---

### 2.3 Datasheet of Power and Control Cable Rev B — P22-ET-09-007-002

**Response Code: 1 — Approved**

Resubmittal of Rev A (Code 1 in TM N3). Rev B extends the specification across five cable families (power, grounding, control, instrument, Ethernet) with IEC 60228 / EN 50525 compliance and UL/CE/RoHS certifications. SEC compatibility supported. Document accepted as-is.

**Action: none — accepted; issue directly at IFC Rev 0.**

---

### 2.4 Single Line Diagram Rev B — P22-CD-09-007-001

**Response Code: 2 — Approved as noted**

First formal submittal. Main supply 400 A 380 V 3-phase 50 Hz; 4-pole MCCB 250 A 25 kA entry protection; 30 mA residual differential on 220 V circuits. Compliant with Technical Specification — Electrical Protections (Section 5.4.4) and Voltages and Frequency to Consider (Section 5.4.7).

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MINOR | Principal enclosure rating NEMA 4X or equivalent IP not declared on the diagram |
| NOTE-01 | MINOR | Surge protection devices on main incoming feeder not visible |

**Action to issue at IFC Rev 0 — no new Single Line Diagram revision required:** add the principal enclosure rating per Technical Specification — Cabinets and the surge protection device location and rating at IFC.

---

### 2.5 Grounding & Power Panel Location Layout Rev E — P22-DWG-09-007-003

**Response Code: 3 — To be revised**

Fifth revision of the layout (Rev A through Rev E). The Consolidated Comment Sheet of Rev E does not address three observations open across previous transmittals. This is the **third consecutive transmittal cycle** (TM N11 OBS-03, TM N15 NOTE-03, TM N17 OBS-01 plus NOTE-02) where the grounding schedule per NCh Eléct. 4/2003 Section 10.0 has not been delivered. ADASA reserves the right to escalate this item under the Contract C-4300 termination clause if Rev F is not delivered within fourteen calendar days. The SEC compliance Hold Point (Technical Specification — Inspections During Manufacturing, Section 8.1) cannot be released without the schedule. Detailed annotations on `P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Grounding schedule completeness (TM N11 OBS-03 reincident, ~70 days open) |
| OBS-02 | MINOR | Revision history block — description of changes missing |
| NOTE-01 | MINOR | Consolidated Comment Sheet of Rev E partially illegible — verify electronic source |

**Action — re-issue as Rev F within fourteen calendar days:** include the complete grounding schedule per NCh Eléct. 4/2003 Section 10.0, complete the revision-history block with descriptions for Revs A through E, and re-issue the PDF from the electronic source. Closure threshold: Rev F is required prior to IFC Rev 0.

---

### 2.6 Cable Tray Layout and Support Details Rev C — P22-DWG-09-007-004

**Response Code: 1 — Approved**

Second revision following Rev A (TM N4, Code 3) and Rev B (TM N15, Code 3). Rev C closes the seven items that had been open across two cycles — two from TM N4 OBS-06/07 (110 days open) and five from TM N15 OBS-04 to OBS-08 (34 days) — with specific evidence on the Consolidated Comment Sheet. The longest-open inheritance in the project is now closed. Drawing accepted as-is.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverable tracked in Section 3: consolidated table of S1 to S7 zone reference positions with minimum separation distances.

---

### 2.7 Typical Installation Details of Power Works Rev C — P22-DWG-09-007-005

**Response Code: 2 — Approved as noted**

Fourth issue of the document following Rev A (TM N8, Code 3), Rev B (TM N13, Code 2) and Rev 0 IFC (TM N17, Code 2). Rev C closes the four TM N17 notes: adopts IEC 60364-5-54 explicitly (replacing NEC), shows the seven grounding methods on page 10, declares feed direction on pages 3 to 7, and reserves a W100 × H100 cable tray space for ADASA on page 6.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MINOR | Designate which of the seven grounding methods (page 10) applies as the typical solution |

**Action to issue at IFC Rev 0 — no new revision required:** designate explicitly which grounding method (METHOD 1 to 7) applies to each load type per IEC 60364-5-54.

---

### 2.8 I/O List Rev 1 — P22-LI-09-008-001

**Response Code: 2 — Approved as noted**

IFC submission. Resubmittal of Rev 0 (Code 2 in TM N17). Rev 1 closes the inherited vibration, VFD-variable and external enable/status items from TM N3 (110 days open), and partially closes the TM N17 dosing IN REMOTE, RTD °C and CIP P&ID page items.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Analyser power-supply voltage discrepancy (TM N14 NOTE-02, ~80 days open) — not addressed in Rev 1 CCS |
| OBS-02 | MAJOR | IFC submission with Plant Control Philosophy Rev D still under Code 3 — conditional acceptance |
| NOTE-01 | MINOR | VFD frequency and accumulated energy variables on HP/CIP Pump Ethernet/IP not explicit |
| NOTE-02 | MINOR | IN REMOTE status bit for dosing pumps not declared (asymmetric with HP/CIP XB001) |

ADASA conditionally accepts the I/O List Rev 1 as Code 2, with acceptance contingent upon (a) approval of Plant Control Philosophy Rev D and (b) an addendum to the I/O List addressing any signal divergence introduced by Rev D ahead of IFC Rev 0. Failure to deliver Rev D, or material divergence in Rev D, reverts this acceptance to Code 3 for the I/O List.

**Action to issue at IFC Rev 0 — no new I/O List revision required if Plant Control Philosophy Rev D introduces no signal changes:** reconcile the analyser power-supply voltage with the Instrument List Rev D, add VFD frequency and accumulated energy variables on Ethernet/IP, and declare the dosing pump IN REMOTE handling explicitly.

---

### 2.9 Project Quality Plan Rev B — P22-BA-09-000-003

**Response Code: 2 — Approved as noted**

Resubmittal of Rev A (Code 3 in TM N17). Rev B closes the two CRITICAL TM N17 observations on inspection matrix and FAT scope — a necessary prerequisite for the 40 percent payment milestone under BAE Clause 31. ITP procedure codes are deferred to the ITP Offsite (Section 2.10).

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | MINOR | FAT Approval Certificate format — confirm specimen template aligned with BAE Clause 31 |

ADASA position on the payment milestone: PQP Rev B closure of the two CRITICAL observations is a necessary prerequisite, but not on its own sufficient. Release of the milestone remains gated on the cumulative satisfaction of (a) ADASA validation of the FAT Approval Certificate format, (b) execution of the FAT and signature of the Acta de Aprobación FAT by ADASA per BAE Clause 31, and (c) no contractual offsets from penalty clauses then in force. The ITP ASME X point detailed in Section 2.10 runs in its own track and does not modify the BAE Clause 31 gate. ADASA reserves all rights under BAE Clause 31 until the Acta de Aprobación FAT is signed.

**Action to issue at IFC Rev 0 — no new PQP revision required:** provide a specimen template of the FAT Approval Certificate aligned with BAE Clause 31 as a tracked deliverable.

---

### 2.10 ITP Offsite Rev B — P22-BA-09-000-004

**Response Code: 3 — To be revised**

Resubmittal of Rev A (Code 2 in TM N17). Rev B closes the operational items (placeholder pressures, document control, PMI frequency) but is silent on the "Test certification to ASME X" commitment of the BW Water Technical Offer Rev1 ITP (Section 12, page 100, line 3905) for the RO Pressure Vessels. The 22-May Mitigation Plan proposed eliminating the stamp; ADASA's position is reserved in Technical Note P22-NT-09-000-001-0 (issued in parallel) clarifications 6.A and 6.C. The contracted scope cannot be revised by omission in the ITP. Detailed annotations on `P22-BA-09-000-004_B_ITP_Offsite_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | Silence on the ASME X certification scope for RO Pressure Vessels per Technical Offer Rev1 ITP (Section 12) |
| NOTE-01 | MAJOR | NDE Plan and other procedures deferred to a separate submittal without delivery dates |

**Action — re-issue as Rev C:** declare explicitly the ASME X certification scope for the RO Pressure Vessels consistent with the BW Water Technical Offer Rev1 ITP (Section 12), or document the formal Change Order if a different scope is proposed; and provide a delivery schedule for the NDE, PMI, Hydrostatic, Preservation and FAT procedures with firm dates prior to IFC Rev 0. Cross-reference to Technical Note P22-NT-09-000-001-0 clarifications 6.A and 6.C remains in effect.

---

### 2.11 Instrumentation & Control Cable Schedule Rev 0 — P22-LI-09-008-002

**Response Code: 3 — To be revised**

First formal submittal. The schedule maps cable types to the signals declared in the I/O List Rev 1; the general assignment scheme is technically reasonable (1.5 mm² Cu/PVC/PVC for discrete signals, 1 mm² shielded for 4–20 mA, RTD pairs, Cat 6+ Ethernet). Detailed annotations on `P22-LI-09-008-002_0_IC_Cable_Schedule_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | VFD communications HP Pump (items 9–14) and CIP Pump (items 66–71) declared as "PANEL INTERIOR WIRE" without specification |
| OBS-02 | MAJOR | Dosing pumps (items 82–85) — cable assignment without IN REMOTE signal coherence with HP/CIP XB001 pattern |
| NOTE-01 | MINOR | Level switch nomenclature inconsistencies (items 80–81 versus I/O List items 122–123) |
| NOTE-02 | MINOR | PHIT09-006 tag identifier incomplete in merged cells (items 74–75) |

**Action — re-issue as Rev 1 (Issued for Approval):** declare the specific cable type, cross-section and shielding for VFD communications (HP Pump and CIP Pump); align dosing pump cable assignments with the I/O List Rev 1 signal map; use LSH and LSL identifiers on level switch cable rows; repeat the full tag on every row. Closure threshold: Rev 1 cannot reach IFC status while Plant Control Philosophy Rev D is still under Code 3, since any signal changes in Rev D would propagate to the cable assignments.

---

### 2.12 Datasheet of RO Cartridge Filter Rev D — P22-ET-09-009-005

**Response Code: 3 — To be revised**

Resubmittal of Rev B (Code 2 OBS-01 in TM N3). Rev D closes the flow-rate observation (22 cartridges at 2.23 m³/h/cartridge, within the recommended envelope) and retains FRP material consistent with the original offer. However, Rev D materialises the horizontal-to-vertical configuration change and the vendor substitution from Filtrek to Sysflo before ADASA's formal position on the 22-May Mitigation Plan is issued. ADASA's position on these changes is reserved in Technical Note P22-NT-09-000-001-0 (issued in parallel) clarifications 5.A through 5.E. Detailed annotations on `P22-ET-09-009-005_D_RO_Cartridge_Filter_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | Horizontal-to-vertical configuration change materialised before ADASA's formal position is issued |
| OBS-02 | MAJOR | Vendor substitution from Filtrek to Sysflo without technical equivalence justification and ADASA pre-approval |
| OBS-03 | MAJOR | Updated as-built drawing of the container with the new configuration not delivered |

**Action — re-issue as Rev E pending response to Technical Note P22-NT-09-000-001-0:** ADASA's formal position on the Sysflo vendor substitution, the H-to-V configuration change and the container tie-in positions is reserved in the Technical Note. Any procurement action taken by BW Water on Sysflo prior to that response remains at BW Water's risk under the Technical Offer Rev1 vendor list. Submit the updated as-built drawing of the container as a separate deliverable. Closure threshold: Rev E with OBS-01 to OBS-03 closed and consistent with the ADASA position on the Technical Note.

---

### 2.13 Datasheet of CIP Cartridge Filter Rev C — P22-ET-09-009-006

**Response Code: 3 — To be revised**

First standalone datasheet for the CIP cartridge filter (previously bundled with the CIP system). Technical content (FRP material, 31 cartridges at 1.84 m³/h/cartridge, DN100 flanged ASME B16.5 Cl 150, 7 bar design) is compliant with Technical Specification — Cartridge Filter (Section 5.1.5). Same horizontal-to-vertical change and Sysflo vendor substitution as Section 2.12, with an additional CIP-specific consideration: the cleaning cycle pH range (2 to 12) requires explicit FRP and gasket material compatibility verification. Detailed annotations on `P22-ET-09-009-006_C_CIP_Cartridge_Filter_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | Horizontal-to-vertical configuration change materialised before ADASA's formal position (same as Section 2.12 OBS-01) |
| OBS-02 | MAJOR | Vendor substitution from Filtrek to Sysflo (same as Section 2.12 OBS-02) |
| OBS-03 | MAJOR | FRP housing and gasket/seal compatibility with CIP cycle pH range (2 to 12) not documented |
| OBS-04 | MAJOR | Updated as-built drawing of the container not delivered (same as Section 2.12 OBS-03) |

**Action — re-issue as Rev D pending response to Technical Note P22-NT-09-000-001-0:** same procurement risk and conditions as Section 2.12; include the gasket material and the chemical compatibility statement for the pH 2 to 12 CIP cycle in Rev D. Submit the updated as-built drawing of the container as a separate deliverable (shared with the RO cartridge filter Section 2.12 OBS-03). Closure threshold: Rev D with OBS-01 to OBS-04 closed and consistent with the ADASA position on the Technical Note.

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

Items open as of 25-May-2026 (table below). Closures and IFC Rev 0 tracking lists follow.

| Origin TM | Document | Observation | Outstanding | Status |
|-----------|----------|-------------|-------------|--------|
| TM N18 Section 2.1 | Plant Control Philosophy Rev C (P22-BT-09-009-001) | OBS-01 CRITICAL HP Pump start permissive; OBS-02 MAJOR Sequence Charts / Alarm & Control Setpoint List / Control Matrix undelivered; OBS-03 MAJOR salt rejection formula | 7 days since TM N18 — third consecutive transmittal carrying the CRITICAL HP Pump permissive open (TM N15 NOTE-20 → TM N18 OBS-01 → TM N19 carry-forward) | OPEN — Rev D not delivered in this cycle. ADASA reserves contractual remedies under Contract C-4300 if Rev D is not delivered within fourteen calendar days from this transmittal |
| TM N11 OBS-03 | Grounding Layout (P22-DWG-09-007-003) | Grounding schedule completeness per NCh Eléct. 4/2003 Section 10.0 | 70 days — third consecutive transmittal (related to Section 2.5 of this transmittal) | OPEN — Rev E does not include the schedule (Section 2.5). Hold Point SEC compliance gated until Rev F |
| TM N4 NOTE-05 | HMI Screenshots (P22-BREAD-09-008-001) | Committed at TM N4 — never submitted | 110 days — oldest open commitment in the project | OPEN — formal commitment outstanding |

**Closed in this transmittal:**

- TM N4 OBS-06 — Cable Tray vibration transmitter locations (closed by Cable Tray Rev C; 110 days open).
- TM N4 OBS-07 — Cable Tray Pt-100 motor sensor locations (closed by Cable Tray Rev C; 110 days open).
- TM N15 Section 2.8 OBS-04 to OBS-08 — Cable Tray five observations (closed by Cable Tray Rev C).
- TM N17 Section 2.5 NOTE-01 to NOTE-04 — Typical Power Works four notes (closed by Typical Installation Details Rev C).
- TM N3 OBS-01 RO Cartridge Filter flow rate — closed by RO Cartridge Filter Rev D (22 cartridges at 2.23 m³/h, within envelope).
- TM N3 OBS-01/03/04/05 I/O List — vibration, VFD variables, external enable, external status (closed or partially closed by I/O List Rev 1).
- TM N17 Section 2.6 OBS-01 and OBS-02 — PQP inspection matrix and FAT scope CRITICALs (closed by PQP Rev B; supports the 40% payment milestone gate as detailed in Section 2.9).
- TM N17 Section 2.6 OBS-03 — PQP procedure codes (deferred to the ITP per BW Water response; ITP Rev B closes placeholders but leaves the ASME X scope open, Section 2.10 OBS-01).
- TM N17 Section 2.6 OBS-04 — PQP Hold/Witness Points (closed by PQP Rev B).
- TM N17 Section 2.7 OBS-01/02/03 — ITP placeholders, document control, procedure codes (closed by ITP Rev B; ASME X scope is a new finding, Section 2.10 OBS-01).
- TM N17 Section 2.8 NOTE-01/02/03 — I/O List dosing IN REMOTE, RTD °C, CIP P&ID page (closed or partially closed by I/O List Rev 1).

**Tracked for IFC Rev 0** (deliverables on related documents or separate analyses; documents reviewed here require no further revision):

- PSV-09-002 overpressure / relief sizing analysis (Valve List residual from TM N18 Section 2.2).
- P&ID CIP Tank dual-value convention consistency with CIP Tank datasheet and Equipment List (carried from TM N18 Section 2.5).
- CIT-09-004 loop response engineering note (P&ID residual; signal-level change closed by I/O List Rev 1).
- AC Thermal Calculation effective post-selection margin statement (selected 2.01 TR vs computed peak 1.774 TR = +13.3%) — carried from TM N18 Section 2.4.
- Motor Datasheet — Pt-100 declaration on motor windings and bearings per Technical Specification — Electrical Motors (Section 5.3) (Section 2.1 cross-document).
- Power Cable Schedule — REL-001 CIP Heater two-cable topology clarification (Section 2.2 OBS-01).
- Single Line Diagram — principal enclosure NEMA 4X/IP66 and SPDs (Section 2.4 OBS-01 and NOTE-01).
- Cable Tray Layout — consolidated table of S1 to S7 zone reference positions with minimum separation distances (Section 2.6).
- Typical Installation Details — designated grounding method (1 to 7) per load type (Section 2.7 NOTE-01).
- I/O List — VFD frequency and accumulated energy, IN REMOTE dosing handling, final consistency with Plant Control Philosophy Rev D (Section 2.8 NOTE-01/02 and OBS-02 condition).
- PQP — FAT Approval Certificate specimen template aligned with BAE Clause 31 (Section 2.9 NOTE-01).

---

## 4. ATTACHMENTS

| Document | Verdict | Annotated File | Annotations |
|----------|---------|---------------|-------------|
| Grounding & Power Panel Location Layout Rev E | Code 3 | P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |
| ITP Offsite Rev B | Code 3 | P22-BA-09-000-004_B_ITP_Offsite_CC_ADASA.pdf | OBS-01, NOTE-01 |
| Instrumentation & Control Cable Schedule Rev 0 | Code 3 | P22-LI-09-008-002_0_IC_Cable_Schedule_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01, NOTE-02 |
| Datasheet of RO Cartridge Filter Rev D | Code 3 | P22-ET-09-009-005_D_RO_Cartridge_Filter_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03 |
| Datasheet of CIP Cartridge Filter Rev C | Code 3 | P22-ET-09-009-006_C_CIP_Cartridge_Filter_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04 |
| Power Cable Schedule Rev B | Code 2 | P22-LI-09-007-002_B_Power_Cable_Schedule_CC_ADASA.pdf | OBS-01 |
| Single Line Diagram Rev B | Code 2 | P22-CD-09-007-001_B_Single_Line_Diagram_CC_ADASA.pdf | OBS-01, NOTE-01 |
| Typical Installation Details of Power Works Rev C | Code 2 | P22-DWG-09-007-005_C_Typical_Power_Works_CC_ADASA.pdf | NOTE-01 |
| I/O List Rev 1 | Code 2 | P22-LI-09-008-001_1_IO_List_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01, NOTE-02 |
| Project Quality Plan Rev B | Code 2 | P22-BA-09-000-003_B_PQP_CC_ADASA.pdf | NOTE-01 |

All ten documents with open observations or notes carry annotated PDFs (five Code 3 and five Code 2). The three Code 1 — Approved documents (Electrical Load List Rev B, Datasheet of Power and Control Cable Rev B, Cable Tray Layout Rev C) require no modification and carry no annotated PDF; the residual deliverables tracked on related documents are listed in Section 3.

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-LI-09-007-001 | Electrical Load List | B | 1 — Approved |
| P22-LI-09-007-002 | Power Cable Schedule | B | 2 — Approved as Noted |
| P22-ET-09-007-002 | Datasheet of Power and Control Cable | B | 1 — Approved |
| P22-CD-09-007-001 | Single Line Diagram | B | 2 — Approved as Noted |
| P22-DWG-09-007-003 | Grounding & Power Panel Location Layout | E | 3 — To Be Revised |
| P22-DWG-09-007-004 | Cable Tray Layout and Support Details | C | 1 — Approved |
| P22-DWG-09-007-005 | Typical Installation Details of Power Works | C | 2 — Approved as Noted |
| P22-LI-09-008-001 | I/O List | 1 | 2 — Approved as Noted |
| P22-BA-09-000-003 | Project Quality Plan | B | 2 — Approved as Noted |
| P22-BA-09-000-004 | ITP Offsite | B | 3 — To Be Revised |
| P22-LI-09-008-002 | Instrumentation & Control Cable Schedule | 0 | 3 — To Be Revised |
| P22-ET-09-009-005 | Datasheet of RO Cartridge Filter | D | 3 — To Be Revised |
| P22-ET-09-009-006 | Datasheet of CIP Cartridge Filter | C | 3 — To Be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Five Code 3 documents drive the verdict (Sections 2.5, 2.10, 2.11, 2.12 and 2.13). The remaining eight documents are Code 1 or Code 2: residual deliverables for IFC Rev 0 are tracked in Section 3. Cable Tray Layout Rev C (Section 2.6) closes the longest-open inheritance in the project. PQP Rev B (Section 2.9) closes the two CRITICAL TM N17 observations on inspection matrix and FAT scope, a necessary prerequisite for the 40 percent payment milestone under BAE Clause 31; release of the milestone remains gated on the cumulative satisfaction of FAT Approval Certificate validation and the signed Acta de Aprobación FAT, with ADASA's rights under BAE Clause 31 reserved until that Acta is signed. Plant Control Philosophy Rev D, expected in this cycle to address the TM N18 Code 3 verdict, was not delivered and is carried forward in Section 3 as a third consecutive transmittal item.
