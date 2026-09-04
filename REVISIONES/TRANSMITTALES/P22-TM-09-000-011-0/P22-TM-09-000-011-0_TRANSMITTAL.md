---
titulo: "TECHNICAL REVIEW TRANSMITTAL N11"
subtitulo: "Second Stage RO Brine Module — Deliveries 19, 20, 21 (25007-0019 / 25007-0020 / 25007-0021)"
codigo: "P22-TM-09-000-011-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
fecha: "17-Mar-2026"
veredicto: "3 — TO BE REVISED"
---

# TECHNICAL REVIEW TRANSMITTAL N11

**Date:** March 17, 2026
**Project:** BAE 12803 — Second Stage RO Brine Module
**From:** ADASA — Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** FINAL

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Deliveries 19, 20, and 21 (25007-0019 / 25007-0020 / 25007-0021, received March 13–16, 2026) submit 10 documents. Ten observations are raised — four MAJOR, six informational.

Key findings:

- **Valve List Rev C (Code 3 — To be Revised):** Corrects four prior duplicate TAGs but introduces two new ones (VE-09-007, PSV-09-002). Rev D required. Area-code error VM-07-005 persists.
- **Equipment Datasheets Rev D (Code 2 — Approved as Noted):** TM N6 OBS-01 (coupling pressure) and TM N10 OBS-06/07 (vibration mounting) closed for HP Pump and both Turbochargers.
- **CCS review (17 items):** 13 closed, 3 partial, 1 open. Valve List CCS item 2 remains OPEN.
- **Layout Drawings Rev B — Grounding Layout and Instrument Location Layout (Code 3 — To be Revised):** Rev B reflects an equipment arrangement derived from the Piping Layout Rev A (P22-DWG-09-005-004), which was rejected in Transmittal N7 for exceeding the CIP external footprint limit. Progress on CCS items is acknowledged; revision required after Equipment Layout and Piping Layout are accepted.

---

## 2. DETAILED OBSERVATIONS BY DOCUMENT

### 2.1 Valve List Rev C — P22-LI-09-005-002

**Response Code: 3 — To be Revised**

Rev C corrects the four duplicate TAGs identified in Transmittal N6 OBS-01 (VM-09-015 renumbered to VM-09-151, VE-09-008, VE-09-009, and VM-09-065 each resolved to unique assignments). The consolidated comment sheet item 3 — confirming VM-09-015 item 18 is now MANUALLY ACTUATED VALVE per Transmittal N6 OBS-11 WITHDRAWN — is verified correct. These corrections are acknowledged.

Rev C does not achieve full TAG uniqueness. Two new duplicate TAGs are introduced that were not present in Rev B.

#### OBS-01 — New duplicate TAG: VE-09-007 appears in items 44 and 64 (MAJOR)

Item 44 and item 64 both carry the TAG VE-09-007. These are distinct physical valves with different sizes, materials, and service descriptions. Duplicate TAGs prevent unambiguous valve identification in the PLC and in field documentation. The Consolidated Comment Sheet response "all valves have unique TAGs on Rev. C" is factually incorrect with respect to this item.

BW Water must assign a unique TAG to one of these two valves in Valve List Rev D and update all project documents referencing the affected TAG accordingly (P&ID, Instrument List, I/O List).

*Technical Basis: ET — Valves and Piping (TAG uniqueness is a fundamental QA requirement for PLC addressability)*

#### OBS-02 — New duplicate TAG: PSV-09-002 appears in items 105 and 112 (MAJOR)

Item 105 and item 112 both carry the TAG PSV-09-002. These are distinct safety relief valves at different process locations. As with OBS-01, duplicate TAG assignment creates a safety documentation conflict that cannot be accepted in a submitted document.

BW Water must assign a unique TAG to item 112 in Valve List Rev D (PSV-09-001 is suggested if available, or a new sequential number) and update all referencing documents.

*Technical Basis: ET — Valves and Piping; ET — Safety and Relief Valves*

#### NOTE-01 — Area-code error VM-07-005 persists (MINOR)

Item 7 carries the TAG VM-07-005 (area 07). Area 07 does not correspond to any discipline boundary in this project. The correct area code for BW Water module equipment is 09, giving VM-09-005. This error was first identified in Transmittal N3 OBS-13 and was not corrected in Rev B or Rev C. BW Water should also verify and correct VM-07-031 and VE-07-009 if those TAGs persist in the list.

Correct this item to VM-09-005 (and VM-09-031, VE-09-009 as applicable) in Valve List Rev D.

*Technical Basis: ET — Instrument and Equipment Identification; Project TAG convention area 09 = BW Water module scope*

---

### 2.2 Equipment List Rev B — P22-LI-09-005-001

**Response Code: 2 — Approved as Noted**

Rev B addresses the single CCS item from Transmittal N6: TAG Static Mixer confirmed as MZE-09-001; CIP Tank volume confirmed at 6.1 m³; Antiscalant Tank volume confirmed at 0.27 m³ (effective); Antiscalant Dosing Pump capacity confirmed at 2.3 LPH; and HP Feed Pump shaft power confirmed at 125 hp = 93 kW. All five confirmations are verified in the submitted document. No new observations are raised.

The proactive inclusion of the HP Pump power conversion (125 hp / 93 kW) by BW Water is noted as a value-added clarification, consistent with the Equipment List CCS scope.

---

### 2.3 GA of CIP Flushing Skid Pump Rev A — P22-DWG-09-005-010

**Response Code: 2 — Approved as Noted**

First submission. The general arrangement drawing is accepted for its initial revision.

#### NOTE-05 — Seismic anchor data not included (MINOR)

The GA drawing does not include anchor bolt layout, anchor loads, or seismic reaction forces. The plant site is located in Seismic Zone 3 per NCh 2369. For all skid-mounted equipment, seismic anchor data is required to confirm that the structural interface between the skid base and the building foundation is adequately designed.

BW Water must include anchor bolt layout plan with bolt diameter, spacing, and embedment depth; seismic base reaction forces (Fx, Fy, Fz) per NCh 2369 analysis; and equipment mass for load verification, in GA Rev B.

*Technical Basis: ET — Structural and Civil Requirements; NCh 2369 — Seismic Design for Industrial Structures*

---

### 2.4 GA of Antiscalant Dosing Skid Pump Rev A — P22-DWG-09-005-011

**Response Code: 2 — Approved as Noted**

First submission. The general arrangement drawing is accepted for its initial revision.

#### NOTE-06 — Seismic anchor data not included (MINOR)

Same condition as NOTE-05 for the CIP Pump GA. Anchor bolt layout, seismic reaction forces (Fx, Fy, Fz), and equipment mass must be provided in GA Rev B per NCh 2369 Zone 3 requirements.

*Technical Basis: ET — Structural and Civil Requirements; NCh 2369 — Seismic Design for Industrial Structures*

---

### 2.5 Painting Specifications Rev B — P22-ET-09-006-2

**Response Code: 1 — Approved**

Rev B addresses both CCS items from Transmittal N6: the RAL 5017 / RAL 5012 distinction for container vs. structural steel is correctly maintained in the updated paint schedule; the DFT correction from 350 µm to 355 µm for the container system (item 12) is verified. Structural steel item 4 also correctly shows 355 µm total DFT (80 + 200 + 75 µm per coat). No new observations are raised. Document is approved.

---

### 2.6 Datasheet of RO HP Feed Pump Rev D — P22-ET-09-009-002

**Response Code: 2 — Approved as Noted**

Rev D attaches the Victaulic Coupling Style H datasheet confirming a working pressure rating of 2000 psi for the DN25–DN100 range. The operating discharge pressure of the HP Feed Pump (~710 psi) provides a margin of approximately 280% over the coupling rating, which is accepted. Transmittal N6 OBS-01 (coupling pressure) is closed for this equipment.

Component Datasheet row 55 confirms 3-wire 100 Ohm Platinum RTDs for both bearings and windings, satisfying ET — Motors and Electrical Equipment. Vibration sensor mounting surface is confirmed, satisfying ET — Vibration Monitoring.

#### NOTE-02 — Motor manufacturer field inconsistency (MINOR)

The HP Feed Pump Component Datasheet identifies the motor manufacturer as "GE" in the equipment data block, while the FEDCO pump data section lists "ABB or equivalent." These two fields describe the same motor. The discrepancy introduces uncertainty when procuring spare parts or conducting field maintenance. BW Water must reconcile the motor manufacturer field across both data blocks in Datasheet Rev E and confirm the actual manufacturer once procurement is complete.

*Technical Basis: ET — Motors and Electrical Equipment (Spare Parts and Maintainability)*

---

### 2.7 Datasheet of Feed Turbocharger (SIP-09-001) Rev D — P22-ET-09-009-007

**Response Code: 2 — Approved as Noted**

Rev D attaches the Piedmont Coupling Style S/X datasheet confirming a working pressure rating of 1800 psi for the DN40 (1.5") and DN50 (2") sizes used on SIP-09-001. The maximum operating inlet pressure for the Feed Turbocharger is approximately 1,008 psi, giving a safety margin of approximately 78% above the rated coupling pressure. Transmittal N6 OBS-01 (coupling pressure) is closed for this equipment.

Datasheet row 38 confirms "vibration sensor mounting surface" for SIP-09-001, satisfying Transmittal N10 OBS-06. Transmittal N10 OBS-06 is closed.

#### NOTE-03 — Coupling style label inconsistency in outline drawing (MINOR)

The HPB-60 outline drawing (page 6 of the datasheet package) references "CUT GROOVE STYLE 77" at the inlet and outlet connections. The attached coupling datasheet documents Style S/X at 1800 psi, which is the accepted rating. Style 77 is a different Victaulic product with a different pressure rating. The outline drawing label must be updated to "Style S" (or the appropriate Style S/X designation) in the next datasheet revision to eliminate the discrepancy and prevent field installation errors.

*Technical Basis: ET — Equipment Documentation Requirements; Victaulic product line differentiation Style 77 vs. Style S*

---

### 2.8 Datasheet of Interstage Turbocharger (SIP-09-002) Rev D — P22-ET-09-009-008

**Response Code: 2 — Approved as Noted**

Rev D attaches the same Piedmont Coupling Style S/X datasheet confirming 1800 psi for DN40 and DN50. The maximum operating inlet pressure for the Interstage Turbocharger is approximately 1,208 psi, giving a safety margin of approximately 49% above the rated coupling pressure. Transmittal N6 OBS-01 (coupling pressure) is closed for this equipment.

Datasheet row 38 confirms "vibration sensor mounting surface" for SIP-09-002, satisfying Transmittal N10 OBS-07. Transmittal N10 OBS-07 is closed.

#### NOTE-04 — Coupling style label inconsistency in outline drawing (MINOR)

Identical condition to NOTE-03 for SIP-09-001: the HPB-60 outline drawing references "CUT GROOVE STYLE 77" at process connections while the accepted coupling is Style S/X at 1800 psi. BW Water must update the outline drawing label to "Style S" in the next revision to prevent field installation errors.

*Technical Basis: ET — Equipment Documentation Requirements; Victaulic product line differentiation Style 77 vs. Style S*

---

### 2.9 Grounding Point & Power Panel Location Layout Rev B — P22-DWG-09-007-003

**Response Code: 3 — To Be Revised**

Rev B addresses the TM N3 comments — confirmed by the Consolidated Comment Sheet.
However, Rev B reflects an equipment arrangement that has changed from Rev A and
is derived from the Piping Layout Rev A (P22-DWG-09-005-004), which was rejected
in Transmittal N7 for exceeding the CIP external footprint limit established in
Transmittal N5 (11,150 mm submitted vs. ≤ 3,500 mm required). Panel and grounding
point positions cannot be accepted while the underlying equipment layout remains
non-conforming.

#### OBS-03 — Grounding and panel positions reflect a non-conforming equipment arrangement (MAJOR)

Rev B panel and grounding point positions are derived from an equipment arrangement that has not been accepted by ADASA. The Piping Layout Rev A from which this arrangement originates was rejected in Transmittal N7 for exceeding the 3,500 mm CIP external footprint limit (submitted at 11,150 mm — more than three times the required limit). The same logic applied in Transmittal N7 §3.3 (Tie-In Point Layout rejected for dependency on the non-conforming Piping Layout) applies here.

BW Water must resubmit Grounding Point & Power Panel Location Layout as Rev C after Equipment Layout (P22-DWG-09-005-003) and Piping Layout (P22-DWG-09-005-004) are revised and accepted by ADASA. Update all referencing documents accordingly.

*Technical Basis: Transmittal N5 (P22-TM-09-000-005-1) — CIP external footprint limit ≤ 3,500 mm; Transmittal N7 — Piping Layout Rev A rejected for non-conformance*

---

### 2.10 Instrument Location Layout Rev B — P22-DWG-09-008-001

**Response Code: 3 — To Be Revised**

Rev B addresses all eight CCS items from Transmittal N3 — TAG FIT-09-001 corrected
to FIT-09-002, vibration transmitter locations added (VT-09-001/002/003), motor
RTD elements confirmed, CIT-09-004 corrected, LIT TAG unified. This progress
is acknowledged.

However, Rev B reflects an equipment arrangement derived from the Piping Layout
Rev A (P22-DWG-09-005-004), rejected in Transmittal N7. The external CIP and
antiscalant instrument positions shown in Rev B correspond to the non-conforming
11,150 mm footprint — more than three times the 3,500 mm limit established in
Transmittal N5. These positions cannot be accepted.

#### OBS-04 — Instrument positions in the CIP/antiscalant external area reflect a non-conforming equipment arrangement (MAJOR)

The instrument positions for CIP and antiscalant external equipment shown in Rev B are derived from the non-conforming Piping Layout arrangement (11,150 mm footprint, rejected in Transmittal N7). Acceptance of these positions would imply acceptance of an equipment arrangement that ADASA has not approved.

BW Water must resubmit Instrument Location Layout as Rev C after Equipment Layout (P22-DWG-09-005-003) and Piping Layout (P22-DWG-09-005-004) are revised and accepted. Internal container instrument positions (22 items) may be preserved in Rev C if unchanged.

*Technical Basis: Transmittal N5 (P22-TM-09-000-005-1) — CIP external footprint limit ≤ 3,500 mm; Transmittal N7 — Piping Layout Rev A rejected for non-conformance*

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

The following observations issued in Transmittal N10 remain open pending BW Water response. The required documents — I/O List Rev C, Data Transfer List Rev B, written UPS autonomy confirmation, Antiscalant Tank GA Rev B, and HMI Screenshots — have not been received. Two observations from Transmittal N10 (OBS-06 and OBS-07) are closed in this transmittal and are documented in Sections 2.7 and 2.8 respectively.

| Obs | Document | Description | Outstanding Since | Status |
|-----|----------|-------------|-------------------|--------|
| TM N10 OBS-01 | I/O List / Data Transfer List | Motor temperature TAG inconsistency (TE vs TIT); TIT-09-003 service conflict | TM N10 (16-Mar-2026) | **OPEN** — I/O List Rev C and Data Transfer List Rev B not received |
| TM N10 OBS-02 | Data Transfer List | Conductivity scaling ranges incompatible with brine conditions (CIT-09-001/004/005 at 0–20 mS/cm) | TM N10 (16-Mar-2026) | **OPEN** — Data Transfer List Rev B not received |
| TM N10 OBS-03 | Data Transfer List | Level alarm Modbus addresses missing for LS-09-001 and LS-09-002; VE-09-014 DI confirmation pending | TM N10 (16-Mar-2026) | **OPEN** — Data Transfer List Rev B not received |
| TM N10 OBS-04 | Control Architecture | UPS autonomy confirmation: 8-hour backup required per ET — Uninterruptible Power Supply | TM N10 (16-Mar-2026) | **OPEN** — Written confirmation with calculation not received |
| TM N10 OBS-05 | GA Antiscalant Tank | Seismic anchor data missing for Antiscalant Tank (GA Rev B pending) | TM N10 (16-Mar-2026) | **OPEN** — GA Rev B not received |
| TM N10 NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | HMI display screenshots committed since Transmittal N4 — not yet submitted | TM N4 | **OPEN** — Document not received |

---

## 4. ATTACHMENTS

The following BW Water documents were reviewed and annotated by ADASA:

| # | Document Code | Title | Rev | Annotations |
|---|--------------|-------|-----|-------------|
| 1 | P22-LI-09-005-002 | Valve List | C | OBS-01, OBS-02, NOTE-01 |
| 2 | P22-ET-09-009-002 | Datasheet of RO HP Feed Pump | D | NOTE-02 |
| 3 | P22-ET-09-009-007 | Datasheet of Feed Turbocharger (SIP-09-001) | D | NOTE-03 |
| 4 | P22-ET-09-009-008 | Datasheet of Interstage Turbocharger (SIP-09-002) | D | NOTE-04 |
| 5 | P22-DWG-09-005-010 | GA of CIP Flushing Skid Pump | A | NOTE-05 |
| 6 | P22-DWG-09-005-011 | GA of Antiscalant Dosing Skid Pump | A | NOTE-06 |
| 7 | P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | B | OBS-03 |
| 8 | P22-DWG-09-008-001 | Instrument Location Layout | B | OBS-04 |

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-LI-09-005-002 | Valve List | C | 3 — To be Revised |
| P22-LI-09-005-001 | Equipment List | B | 2 — Approved as Noted |
| P22-DWG-09-005-010 | GA of CIP Flushing Skid Pump | A | 2 — Approved as Noted |
| P22-DWG-09-005-011 | GA of Antiscalant Dosing Skid Pump | A | 2 — Approved as Noted |
| P22-ET-09-006-2 | Painting Specifications | B | 1 — Approved |
| P22-ET-09-009-002 | Datasheet of RO HP Feed Pump | D | 2 — Approved as Noted |
| P22-ET-09-009-007 | Datasheet of Feed Turbocharger (SIP-09-001) | D | 2 — Approved as Noted |
| P22-ET-09-009-008 | Datasheet of Interstage Turbocharger (SIP-09-002) | D | 2 — Approved as Noted |
| P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | B | 3 — To be Revised |
| P22-DWG-09-008-001 | Instrument Location Layout | B | 3 — To be Revised |

**OVERALL TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Valve List Rev D is required to correct duplicate TAGs OBS-01 (VE-09-007) and OBS-02 (PSV-09-002) and to address NOTE-01 (VM-07-005 area code). Grounding Layout Rev C and Instrument Location Layout Rev C must be resubmitted after Equipment Layout and Piping Layout are accepted by ADASA (OBS-03, OBS-04). All other documents are accepted at their submitted revision pending the noted corrections in future revisions.
