---
second_brain: capture
type: transmittal
project: salmuera-taltal
date: 2026-07-13
---

# TECHNICAL REVIEW TRANSMITTAL N27 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-027-0 | **Date:** 13-Jul-2026 | **Submittal:** 25007-0063 (E63)

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To Be Revised.** Two documents (submittal 25007-0063). Tally: 1 Code 2, 1 Code 3. The Painting Procedure closes; the HP and LP Pressure Test Procedure does not, because the Line List it now attaches orders a 75 bar hydrostatic test on a PVC line rated far below that pressure.

**Disposition at a glance:**

- **Painting Procedure Rev B — Code 2.** Coating system and marine durability substantiated; three entries on the inspection form remain to be corrected at issue.
- **HP and LP Pressure Test Procedure Rev C — Code 3.** The attached Line List carries an unsafe test pressure and no approved revision status.

**Why Code 3 — HP and LP Pressure Test Procedure:** Rev C answers the Transmittal N26 observation by attaching the Line List rather than writing the pressure in the body, so that attachment is now the instruction the shop follows. It sets line DA-PVC-DN65-09-016 (RO Brine Discharge, PVC Schedule 80, DN65, operating at 1 bar) at a 50 bar design pressure, and its hydrostatic column duly orders 75 bar. A PVC Schedule 80 line with Class 150 flanges withstands nothing close to that at the 45 degree Celsius design temperature the same list assigns it: a shop testing to this instruction would rupture the line. The 50 bar design value comes across from Line List Rev C, which ADASA approved at Transmittal N18; the hydrostatic column added in this attachment is the change that converts it into an executable test pressure. The attachment also carries no approved status. It is labelled Rev 0, a revision never transmitted, while the approved Rev C has no hydrostatic column at all, leaving the pressure the inspector would sign against without an approved source.

The Painting Procedure Rev B meets both conditions ADASA set at Transmittal N25 for a system other than Sherwin-Williams, and is Approved as Noted on its inspection form.

Section 3 details the open and overdue inventory, including the RO Vessel Hydrostatic Test Procedure Rev C, which did not arrive.

## 2. Observations by Document

### 2.1 HP and LP Pressure Test Procedure Rev C — P22-BA-09-000-010

**Response Code: 3 — To Be Revised**

**Status.** Rev C keeps the correct ASME B31.3 factors (1.5 times design pressure for the hydrostatic step, 1.1 times for the pneumatic step) and answers the Transmittal N26 observation by attaching the Line List, whose new HYDROTEST PRESS. column gives a value for every line. Since the body still writes no pressure, that column is the operative instruction, and it cannot be executed safely. Each value in it is 1.5 times the design pressure of its line. The arithmetic is right, and so is the result on the Super Duplex circuit (135 bar on the lines designed for 90 bar, 120 bar on those designed for 80 bar) and on the PVC lines designed for 2 and 5 bar (3 and 7.5 bar). The RO Brine Discharge breaks it: the line is PVC Schedule 80 yet carries a 50 bar design pressure, so the column orders 75 bar on a plastic line. The attachment also has no approved revision status. Annotations on P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | The attached Line List sets line DA-PVC-DN65-09-016 (RO Brine Discharge, POLYVINYL CHLORIDE SCH 80, DN65, wall 6.02 mm, operating pressure 1 bar) at a 50 bar design pressure, and its HYDROTEST PRESS. column therefore orders 75 bar. A PVC Schedule 80 DN65 pipe does not withstand 75 bar at the 45 degree Celsius design temperature that the same list assigns to it; a shop testing to this instruction would rupture the line and injure the crew. The 50 bar design value is carried over from Line List Rev C, and ADASA did not raise it when that revision was approved at Transmittal N18 — the hydrostatic column added in this attachment is what turns it into an executable test pressure. Reconcile the line: either the piping class or the design pressure of the RO Brine Discharge is wrong, and the resulting test pressure must be consistent with the class actually installed. The requirement is the Technical Specification (P22-ET-09-000-001-0), Section 5.2.1 - Low-Pressure Piping, which fixes PVC to ASTM D1784 and D1785, Schedule 80, with Class 150 flanges, and ASME B31.3 for the test itself. |
| OBS-02 | MAJOR | The attached Line List is labelled "Rev. No: 0". The revision ADASA approved is Rev C (Code 1 at Transmittal N18, 18-May-2026) and it carries no HYDROTEST PRESS. column, so the pressure the inspector signs against comes from a revision that has never been transmitted for review. Transmit the corrected Line List revision as a submittal, and cite it in the procedure body by document number and revision. |
| OBS-03 | MINOR | The body still writes no numeric test pressure — clauses 5.5.12 and 5.6.12 refer only to "design pressure in the approved line list", and both state it as a minimum rather than the single value to apply. State on the face of the procedure the governing envelope for each circuit (135 bar high pressure and 7.5 bar low pressure, per rows 5.2 and 5.1 of the approved Inspection and Test Plan), naming the Line List revision that fixes the value line by line. |
| OBS-04 | MINOR | Subsection 5.7.2 (Weld Joints) still skips 5.7.2.2 — the sequence runs 5.7.2.1, 5.7.2.3, 5.7.2.4, 5.7.2.5. The pneumatic-section gap at 5.6.5 is corrected, but this is the second consecutive revision in which the reply reports the numbering defect as resolved while the gap survives. |
| NOTE-01 | NOTE | The Pressure and Leak Test Report form (AQ-QAM-F018 Rev 4) is now attached and carries no pre-printed pressure, which closes the Transmittal N26 note. It has no field for the required test pressure, only for the pressure actually applied; add one, referencing the approved Line List revision, so the inspector contrasts the applied value against the specified one. |

**Action — re-issue as Rev D:** correct the RO Brine Discharge line so that its class, design pressure and test pressure are consistent, and re-issue the Line List accordingly (OBS-01); transmit that Line List revision for record and cite it in the body (OBS-02); state the governing test-pressure envelope per circuit on the face of the procedure (OBS-03); close the numbering gap at 5.7.2.2 (OBS-04). The high-pressure hydrostatic test remains a Hold Point, and no line is to be tested until the governing Line List revision is transmitted.

### 2.2 Painting Procedure Rev B — P22-BA-09-000-011

**Response Code: 2 — Approved as Noted**

**Status.** Rev B meets the two conditions ADASA set at Transmittal N25 for using a system other than Sherwin-Williams. The Jotun technical letter of 02-Jul-2026 (TSS-DD-MYPC039-26) and the three product data sheets give the product-to-product equivalence against the architecture fixed by the approved Painting Specification (P22-ET-09-006-002) Rev C. The correspondence holds coat by coat: zinc-rich epoxy primer at 80 micrometres (Barrier 80, compliant with SSPC Paint 20 level 2), micaceous-iron-oxide high-build epoxy midcoat at 200 micrometres (Penguard Midcoat M20), aliphatic polyurethane topcoat at 75 micrometres (Hardtop XP), 355 micrometres in total. The letter also confirms suitability for the ISO 12944 C5-M corrosivity category, which is the marine durability the coastal site requires. The scope is now bounded to ASTM A-36 carbon steel with stainless steel and non-metallic surfaces excluded, and the quality control incorporates the adhesion pull-off test, the ISO 2808 measurement method and the SSPC-SP10 blast reference. The inspection form in Appendix A does not close, and it is the record the quality inspector signs. Annotations on P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The anchor-profile contradiction is half corrected. The procedure body and the acceptance row of the inspection form now read 50 to 80 micrometres, but the BLASTING ACTIVITY criterion in that same form still reads 40 to 75 micrometres, so the inspector works against two incompatible criteria and can accept a 40 micrometre profile. That floor sits below the 50 micrometre lower bound ADASA required at Transmittal N23, and below the 50 micrometre anchor profile of the Technical Specification (P22-ET-09-000-001-0), Section 5.1.9 - Support Frame. Unify the form to the single 50 to 80 micrometre criterion the procedure itself adopts. |
| OBS-02 | MINOR | The inspection form still carries "Specified DFT: xxx µm" as a placeholder and leaves the Type row of the painting system blank, so the nominal dry film thickness per coat appears nowhere on the record. Print the nominal values (80, 200 and 75 micrometres, not less than 355 micrometres in total) and the product per coat. |
| OBS-03 | MINOR | The finish colour is absent from the PAINTING SYSTEM block and from the Colour row of the inspection form. RAL 5012 (Luminous Blue) is fixed for the structural support frame by the approved Painting Specification Rev C and by the Technical Specification, Section 5.1.9 - Support Frame. Referring the inspector to the specification is a valid source, but the record being signed must carry the colour. |
| NOTE-01 | NOTE | Closure of the two Transmittal N23 major observations: the coating-system substitution is now substantiated coat by coat against the approved Painting Specification, and the marine durability is demonstrated. ADASA raises no further objection to the Jotun system for the ASTM A-36 support frame. |
| NOTE-02 | NOTE | SSPC-SP10 and NACE No. 2 are the same standard, so the SSPC-SP10 reference now in the procedure satisfies that item and no separate NACE citation is required. |

**Action to issue at IFC Rev 0 — no new procedure revision required:**

1. Unify the anchor-profile criterion in the inspection form to 50 to 80 micrometres, removing the 40 to 75 micrometre entry (OBS-01).
2. Print the nominal dry film thickness and the product for each coat in the inspection form, replacing the "xxx" placeholder (OBS-02).
3. State RAL 5012 (Luminous Blue) as the finish colour in the painting-system block and in the inspection form (OBS-03).

ADASA's acceptance is conditioned on the coating actually applied being the C5-M certified Jotun system, no less than 355 micrometres total dry film thickness, RAL 5012, over an anchor profile of 50 to 80 micrometres.

## 3. Pending Observations from Previous Transmittals

This submittal delivered E63.

**Addressed in this transmittal:** The Painting Procedure returns at Rev B — the item ADASA escalated to the 10-Jul-2026 deadline and the one open since Transmittal N23 — and closes. Two of the four quality and fabrication procedures opened at Transmittal N23 are now closed to IFC: the NDE Plan at Transmittal N26 and the Painting Procedure here. The HP and LP Pressure Test Procedure and the RO Vessel Hydrostatic Test Procedure remain open. The Jotun make is confirmed as substantiated and is not reopened; the 4-20 mA plus HART acquisition point stays satisfied at the instrument level; the ASME stamp remains waived; the soft-I/O field scheme over Ethernet/IP accepted at Transmittal N20 is not reopened.

**Open from previous transmittals — the most serious:**

| Origin TM | Document | Observation | Status |
|-----------|----------|-------------|--------|
| TM N26 Section 2.3 | RO Vessel Hydrostatic Test Procedure (P22-BA-09-000-009) | The body states no binding test pressure and the embedded report form still prints 45.5 bar against the 1,980 psi and 1,320 psi that the Inspection and Test Plan and the 02-Jun-2026 stamp waiver require; the two-gauge, calibration-certificate-review instrumentation is not incorporated | OPEN: Rev C not delivered; this is the test for which the ASME code stamp was waived |
| TM N22 Section 2.1 | Plant Control Philosophy children: Operating Sequence Charts (P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) and Control Matrix | The operative numerical control logic remains in child documents not delivered; it gates the IO List reaching issue for construction | OPEN and overdue: not delivered by the 10-Jul-2026 deadline; the seventh cycle with that logic outside the package |
| TM N20 Section 2.6 | PLC-LCP Outline Panel Drawing (P22-CD-09-008-001) | The drawing must re-issue as Rev C with an enclosure specification coherent with the approved LCP Datasheet — SS316L unpainted for the exterior body, door, roof, rear panel, plinth and gland plates, NEMA 4X and IP66 — as settled in the RFI-002 reply of 07-Jul-2026, which accepts galvanised or mill-finish internal mounting components | OPEN: not delivered; panel fabrication release remains gated |
| TM N26 Section 2.6 | UHPRO Structural Calculation Report (P22-CD-09-005-001) | The base-bolt design omits the main process equipment — high-pressure pump, turbochargers, RO cartridge filter and RO pressure vessels — all carried as seismic mass in the model. This report also governs the anchor reaction forces of the Antiscalant Dosing Pump Skid and the NCh 2369 anchor loads of the CIP Flushing Tank and the Antiscalant Dosing Tank | OPEN: to re-issue as Rev B; no new revision in this delivery |
| TM N26 Section 2.8 | GA of Antiscalant Dosing Tank (P22-DWG-09-005-015) | The NCh 2369 anchor-bolt loads and qualification are still deferred | OPEN: to re-issue as Rev C; no new revision in this delivery |
| TM N22 Section 2.2 | Equipment Layout (P22-DWG-09-005-003) | The RO Cartridge Filter is still drawn horizontal against its own vertical datasheet | OPEN: to re-issue as Rev D; no new revision in this delivery |
| TM N4 NOTE-05 | HMI Screenshots (P22-BREAD-09-008-001) | Committed at Transmittal N4, never submitted — the oldest open commitment in the project | OPEN: not delivered |

**Overdue deliverables (today is 13-Jul-2026):**

- Grounding Point and Power Panel Location Layout Rev F — committed for 17-Jun-2026, escalated to 10-Jul-2026, not delivered.
- FAT and SAT comparison table — committed for 15-Jun-2026, escalated to 10-Jul-2026, not delivered.
- The three mechanical installation-route plans (Maintenance Lifting Points, 3D Model, GA RO HP Pump) — committed for 26-Jun-2026, escalated to 10-Jul-2026, not delivered.
- The Plant Control Philosophy children — escalated to 10-Jul-2026, not delivered.
- Of the five items carried by that consolidated deadline, only the Painting Procedure arrived.

**Cross-document deliverables:**

- Line List (P22-LI-09-009-003): re-issue with the RO Brine Discharge line reconciled and transmit it for record, since it is the document that fixes the test pressure of the HP and LP Pressure Test Procedure (Section 2.1, OBS-01 and OBS-02).
- Container base-bolt interface: the tension and shear demands at the container base, required as input to the OOCC foundation design, tracked since Transmittal N26 (Section 2.6, NOTE-01) and not delivered.
- Module Seismic Calculation Report: the endorsed report backing the anchor reaction forces used by the equipment general arrangements, governed by the Structural Calculation Report and not delivered.

## 4. Attachments

| Document | Verdict | Annotated File | Annotations |
|----------|---------|----------------|-------------|
| HP and LP Pressure Test Procedure Rev C | Code 3 | P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01 |
| Painting Procedure Rev B | Code 2 | P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02 |

All documents with open observations or notes carry annotated PDFs (1 Code 3 + 1 Code 2). No document in this submittal is Code 1 — Approved.

**Download — this transmittal and the two annotated PDFs:** [SYNOLOGY_LINK]

## 5. Response Summary

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-BA-09-000-010 | HP and LP Pressure Test Procedure | C | 3 — To Be Revised |
| P22-BA-09-000-011 | Painting Procedure | B | 2 — Approved as Noted |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Tally: 1 Code 2, 1 Code 3. The verdict rests on the test pressure the HP and LP Pressure Test Procedure now delegates to its attached Line List, which orders 75 bar on a PVC line and carries no approved revision status. The Painting Procedure Rev B substantiates the Jotun coating system against the approved Painting Specification and issues directly at IFC Rev 0 with the three inspection-form corrections of Section 2 incorporated. Documents not appearing in this response are unaffected by this transmittal.
