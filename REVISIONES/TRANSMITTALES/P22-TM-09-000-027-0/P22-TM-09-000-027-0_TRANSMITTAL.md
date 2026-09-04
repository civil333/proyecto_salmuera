---
second_brain: capture
type: transmittal
project: salmuera-taltal
date: 2026-07-13
---

# TECHNICAL REVIEW TRANSMITTAL N27 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-027-0 | **Date:** 13-Jul-2026 | **Submittals:** 25007-0063 (E63) and 25007-0064 (E64)

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To Be Revised.** Six documents (submittals 25007-0063 and 25007-0064). Tally: 4 Code 2, 2 Code 3.

**Disposition at a glance:**

- **HP and LP Pressure Test Procedure Rev C — Code 3.** The attached Line List orders 75 bar on a PVC line and carries no approved revision status; re-issue as Rev D.
- **RO Vessel Hydrostatic Test Procedure Rev C — Code 2.** State the binding test pressures on the face of the procedure at Rev 0.
- **Painting Procedure Rev B — Code 2.** Correct the three inspection-form entries at Rev 0.
- **PLC/LCP Outline Panel Drawing Rev C — Code 2.** Confirm the cable-clamp size and reword the material note at Rev 0.
- **PLC/LCP FAT Procedure - Hardware Rev A — Code 2.** Correct the governing-drawing references and the tag entries at Rev 0; the RTD protection sign-off is held until the open Alarm and Interlock List winding and bearing swap (Section 3) is reconciled. No new revision.
- **Operating and Maintenance Manual Rev A — Code 3.** The control sequence, setpoints and HMI reproduce logic from the still-open Control Philosophy documents and contradict the approved bypass logic; re-issue as Rev B.

**Why Code 3 — HP and LP Pressure Test Procedure:** Rev C writes no pressure in the body and attaches a Line List instead, so that table is the executable instruction. It sets line DA-PVC-DN65-09-016 (RO Brine Discharge, PVC Schedule 80, operating at 1 bar) at a 50 bar design pressure, so its hydrostatic column orders 75 bar, a value that would rupture the line. The attachment is also labelled Rev 0, never transmitted, while the approved Line List Rev C has no hydrostatic column. Reconcile the line and re-issue as Rev D (Section 2.1).

Section 3 lists the pending observations from previous transmittals.

## 2. Observations by Document

### 2.1 HP and LP Pressure Test Procedure Rev C — P22-BA-09-000-010

**Response Code: 3 — To Be Revised**

**Status.** Rev C answers the Transmittal N26 observation by attaching the Line List, whose new HYDROTEST PRESS. column becomes the operative test instruction since the body still writes no pressure. Its factors are right (1.5 times design pressure), but the RO Brine Discharge breaks it: line DA-PVC-DN65-09-016 is PVC Schedule 80 yet carries a 50 bar design pressure, so the column orders 75 bar on a plastic line that operates at 1 bar — a shop testing to it would rupture the line. The attachment is also labelled "Rev 0" and has never been transmitted for review. This is a safety item; the requirement is the Technical Specification (P22-ET-09-000-001-0), Section 5.2.1 - Low-Pressure Piping, and ASME B31.3. Itemised in P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf.

**Action — re-issue as Rev D:** reconcile the RO Brine Discharge line so its class, design pressure and test pressure are consistent, and transmit the corrected Line List for record and cite it in the body; state the governing test-pressure envelope per circuit on the face of the procedure; and close the 5.7.2.2 numbering gap (OBS-01 to OBS-04 and NOTE-01 on the annotated PDF). The high-pressure hydrostatic test remains a Hold Point, and no line is to be tested until the governing Line List revision is transmitted.

### 2.2 RO Vessel Hydrostatic Test Procedure Rev C — P22-BA-09-000-009

**Response Code: 2 — Approved as Noted**

**Status.** Rev C closes the critical observation carried since Transmittal N23 and re-stated at N26: the embedded Protec form that printed 45.5 bar is gone, and in its place the actual test report of 17-Jun-2026 records the vessels tested at their required pressures — 91.01 bar on the BPV81200SP7 (1.1 times the 1,200 psi design) and 136.52 bar on the BPV81800SP7 (1.1 times the 1,800 psi design), all passing, with the gauge calibration certificates attached. This is the test for which the ASME stamp was waived; the waiver of 02-Jun-2026 is not reopened. Two minor documentary items remain, itemised in P22-BA-09-000-009_C_RO_Vessel_Hydrostatic_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** state the binding test pressures on the face of the procedure, and confirm which gauge was used for the 136.5 bar test and attach its certificate within the procedure's own 1.5-to-4-times range (OBS-01, OBS-02 and NOTE-01 on the annotated PDF). ADASA's acceptance rests on the attached 17-Jun-2026 report, which already evidences the vessels were tested and passed; no re-test is required.

### 2.3 Painting Procedure Rev B — P22-BA-09-000-011

**Response Code: 2 — Approved as Noted**

**Status.** Rev B meets the two conditions ADASA set at Transmittal N25 for using a system other than Sherwin-Williams: the Jotun letter of 02-Jul-2026 (TSS-DD-MYPC039-26) and three data sheets give the coat-by-coat equivalence against the approved Painting Specification (P22-ET-09-006-002) Rev C (80 + 200 + 75 micrometres, 355 in total) and confirm the ISO 12944 C5-M marine durability the coastal site requires. ADASA raises no further objection to the Jotun system for the ASTM A-36 support frame. Three items remain on the inspection form, the record the quality inspector signs, itemised in P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new procedure revision required:** unify the anchor-profile criterion in the inspection form to the single 50 to 80 micrometre value (removing the 40 to 75 entry), print the nominal dry film thickness and product per coat in place of the "xxx" placeholder, and state RAL 5012 (Luminous Blue) as the finish colour (OBS-01 to OBS-03 and NOTE-01/NOTE-02 on the annotated PDF). ADASA's acceptance is conditioned on the coating actually applied being the C5-M certified Jotun system, not less than 355 micrometres total, RAL 5012, over a 50 to 80 micrometre anchor profile.

### 2.4 PLC/LCP Outline Panel Drawing Rev C — P22-CD-09-008-001

**Response Code: 2 — Approved as Noted**

**Status.** Rev C resolves the enclosure gate opened at Transmittal N20 and carried through N25: the exterior body, door, roof, rear panel, plinth and gland plates are SS316L, the interior mounting components galvanised or cold-rolled steel (RAL 7035), and the protection class NEMA 4X and IP66 — the configuration settled in the RFI-002 reply of 07-Jul-2026, stated on the sheet-5 Hoffman material note and coherent with the approved LCP Datasheet and Single Line Diagram. The internal galvanised components are accepted and not reopened, and the "SECONDE STAGE" typo is corrected. BW Water commits (sheet 14) to re-issuing the Single Line Diagram to "SS316L Panel, NEMA 4X/IP66", tracked in Section 3. Three minor drawing items remain, itemised in P22-CD-09-008-001_C_Outline_Panel_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** confirm the cable-clamp diameter, reword the MATERIAL row so the SS316L exterior is not listed as interior sheet steel, and correct the two label typos (OBS-01 to OBS-03 and NOTE-01 on the annotated PDF). The enclosure specification is accepted as coherent with the approved LCP Datasheet and Single Line Diagram.

### 2.5 PLC/LCP FAT Procedure - Hardware Rev A — P22-PP-09-000-001

**Response Code: 2 — Approved as Noted**

**Status.** This first-issue hardware FAT procedure is complete and correct: its 138 I/O points, the four relay-contact signals to the plant control system, and the Pt-100 winding and bearing channels on both motors trace cleanly to the approved IO List Rev 4 and the Technical Specification (P22-ET-09-000-001-0), Section 5.3 - Electrical Motors. It carries three documentary corrections to incorporate at issue — none touching the test — plus one sign-off condition: the RTD table itself is correct (matching the IO List), but the winding and bearing definition is swapped in the still-open Alarm and Interlock List (Section 3), so the RTD protection sign-off is held until that list is reconciled. Approved as noted, no new revision. Itemised in P22-PP-09-000-001_A_FAT_Procedure_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** correct the governing-drawing references to the issued CD codes (the Outline is cited under an ET code and the Schematic under a Rev B that does not exist), the documentary tags, and the two acceptance criteria to match the approved Outline and IO List (OBS-01 to OBS-03 and NOTE-01 on the annotated PDF). The RTD protection tests are witnessed only after the Alarm and Interlock List (Section 3) is reconciled to the FAT and IO List winding and bearing mapping (NOTE-02); ADASA's acceptance otherwise stands.

### 2.6 Operating and Maintenance Manual Rev A — P22-BA-09-000-012

**Response Code: 3 — To Be Revised**

**Status.** The manual's installation, membrane-loading and cartridge-loading procedures are serviceable and its project data are correct (the six-by-four vessel array, 70 membranes). Its Section 4, however, is not self-contained: the control-sequence matrix (4.4) and the HMI pages (4.5) reproduce the operating sequence, setpoints and operator screens that the Plant Control Philosophy assigns to documents still open (the Operating Sequence Chart, not issued; the Alarm and Control Setpoint List, Rev B; the HMI Screenshots, Rev A), so it states operating logic with no approved source. In one place it also contradicts the approved Control Philosophy Rev D, opening the turbocharger bypass VE-09-002 on a TDS setpoint where the Control Philosophy governs that valve by the pressure control loop. It cannot be approved as an operating manual until that content is reconciled. Itemised in P22-BA-09-000-012_A_OM_Manual_CC_ADASA.pdf.

**Action — re-issue as Rev B:** correct the turbocharger-bypass logic, control basis and tag to the approved Control Philosophy; reconcile the control sequence, setpoints and HMI with the Operating Sequence Chart, the Alarm and Control Setpoint List and the HMI Screenshots once those are issued; and complete the setpoint, HMI-configuration and housekeeping items (OBS-01 to OBS-05 on the annotated PDF). The manual cannot issue at IFC until the governing control documents close.

## 3. Pending Observations from Previous Transmittals

**The three most serious open items:**

| Origin TM | Document | Observation | Status |
|-----------|----------|-------------|--------|
| TM N22 | Plant Control Philosophy children (Operating Sequence Chart P22-LI-09-008-017, Alarm and Control Setpoint List P22-LI-09-008-015, Control Matrix) | The operating logic, setpoints and motor-protection mapping remain in child documents that are open: the Operating Sequence Chart is not issued, and the Alarm and Control Setpoint List (delivered as the Alarm and Interlock List Rev B) still has the RO HP Pump winding and bearing sensors swapped against the IO List. The FAT Procedure (Code 2, correct on this mapping) holds its RTD protection sign-off against this closure, and the Operating and Maintenance Manual (Section 2) reproduces its logic; it also gates the IO List reaching issue for construction | OPEN and overdue: seventh cycle; Sequence Chart not delivered by the 10-Jul-2026 deadline, Alarm and Interlock List at Rev B, Code 3 |
| TM N26 | UHPRO Structural Calculation Report (P22-CD-09-005-001) | The base-bolt design omits the main process equipment (HP pump, turbochargers, RO cartridge filter, RO pressure vessels) carried as seismic mass; it also governs the anchor loads of the Antiscalant Dosing Pump Skid, the CIP Flushing Tank and the Antiscalant Dosing Tank | OPEN: re-issue as Rev B |
| TM N22 | Equipment Layout (P22-DWG-09-005-003) | The RO Cartridge Filter is still drawn horizontal against its own vertical datasheet | OPEN: re-issue as Rev D |

**Also open:** the GA of the Antiscalant Dosing Tank Rev C (NCh 2369 anchor loads, governed by the Structural Calculation Report above) and the HMI Screenshots (P22-LI-09-008-016 Rev A, Code 3, still incomplete — the operator screens the Operating and Maintenance Manual depends on).

**Overdue from the 10-Jul deadline:** the Grounding Layout Rev F, the FAT and SAT comparison table, and the three mechanical installation-route plans.

**Cross-document deliverables:** the Line List reconciled and transmitted (it fixes the HP and LP test pressure, Section 2.1); the Single Line Diagram re-issued to "SS316L Panel, NEMA 4X/IP66" (committed on the Outline comment sheet); the container base-bolt interface (input to the OOCC foundation); and the Module Seismic Calculation Report.

## 4. Attachments

| Document | Verdict | Annotated File | Annotations |
|----------|---------|----------------|-------------|
| HP and LP Pressure Test Procedure Rev C | Code 3 | P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01 |
| RO Vessel Hydrostatic Test Procedure Rev C | Code 2 | P22-BA-09-000-009_C_RO_Vessel_Hydrostatic_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |
| Painting Procedure Rev B | Code 2 | P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02 |
| PLC/LCP Outline Panel Drawing Rev C | Code 2 | P22-CD-09-008-001_C_Outline_Panel_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01 |
| PLC/LCP FAT Procedure - Hardware Rev A | Code 2 | P22-PP-09-000-001_A_FAT_Procedure_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02 |
| Operating and Maintenance Manual Rev A | Code 3 | P22-BA-09-000-012_A_OM_Manual_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05 |

All six documents carry annotated PDFs (2 Code 3 and 4 Code 2). No document in these submittals is Code 1 — Approved.

**Download — this transmittal and the six annotated PDFs:** https://lrg.synology.me:6501/d/s/192lEgkHowre9aB7Xq17uqPalvdU9v5Z/9VEOGTc569y_FeCJGzMrvq-gOm0IEV1o-4rWgl4DGWA0

## 5. Response Summary

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-BA-09-000-010 | HP and LP Pressure Test Procedure | C | 3 — To Be Revised |
| P22-BA-09-000-009 | RO Vessel Hydrostatic Test Procedure | C | 2 — Approved as Noted |
| P22-BA-09-000-011 | Painting Procedure | B | 2 — Approved as Noted |
| P22-CD-09-008-001 | PLC/LCP Outline Panel Drawing | C | 2 — Approved as Noted |
| P22-PP-09-000-001 | PLC/LCP FAT Procedure - Hardware | A | 2 — Approved as Noted |
| P22-BA-09-000-012 | Operating and Maintenance Manual | A | 3 — To Be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Tally: 4 Code 2, 2 Code 3. The two Code 3 documents are the HP and LP Pressure Test Procedure (its attached Line List orders 75 bar on a PVC line with no approved revision status) and the Operating and Maintenance Manual (control sequence, setpoints and HMI governed by still-open documents, and one contradiction with the approved Control Philosophy); each re-issues as a new revision. The four Code 2 documents issue at IFC Rev 0 with the corrections of Section 2 incorporated; the FAT Procedure additionally holds its RTD protection sign-off until the open Alarm and Interlock List is reconciled (Section 3). Documents not appearing in this response are unaffected by this transmittal.
