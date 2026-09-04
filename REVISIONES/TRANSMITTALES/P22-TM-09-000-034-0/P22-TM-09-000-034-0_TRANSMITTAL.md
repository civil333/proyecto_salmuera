# TECHNICAL REVIEW TRANSMITTAL N34 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-034-0 · **Submittals:** 25007-0073, 25007-0077, 25007-0080 · **Date:** 18-Aug-2026
**Source-of-record (English) for the generated DOCX. Run `anti-ia revisar` before issue.**

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To be revised.** Five documents from submittals **25007-0073** of 11 August, **25007-0077** of 14 August and **25007-0080** of 18 August. Tally: 2 Code 1, 2 Code 2, 1 Code 3.

**Disposition at a glance:**

- **Alarm and Interlock List Rev 0 — Code 1.** Re-issue the Instrument List at the binding vibration range ADASA declares below.
- **Control and Sequence Chart Rev 0 — Code 1.** No action.
- **Quality Dossier Index Rev B — Code 3.** Add the chapter for ADASA's FAT Approval Certificate, complete the revision and inclusion status of every line, and state which of the two dossier indices this document is.
- **GA of Antiscalant Dosing Pump Skid Rev C — Code 2.** Reconcile the per-bolt Fz with the total reaction block at Rev 0.
- **GA of CIP / Flushing Tank Rev B — Code 2.** State which document governs the top opening and the two side connections, and align the losing one.

**Why Code 3 — Quality Dossier Index.** The chapter reported as the FAT Approval Certificate is the release for dispatch, a different record; the certificate the Technical Specification calls indispensable to the final dossier has no chapter. And the observation that set the previous code is not materially closed: the new columns are largely empty and no line carries an inclusion status, so the index still cannot work as a checklist. It is the only document that fixes the transmittal code.

**Binding vibration range.** The Alarm and Interlock List Rev 0 ranges VT-09-001 at 0 to 12 mm/s rms with the high-high trip at 10, while the Instrument List Rev E, approved at Code 1, still ranges the same tag at 0 to 8.9 mm/s rms. ADASA declares the binding range to be **0 to 12 mm/s rms** and requires the Instrument List to be re-issued to it, so that the vibration stop of a 93 kW pump can act. Tracked in Section 3.

**Receipt of submittals 25007-0073 and 25007-0077.** Transmittal N33 reported both numbers as missing from the series. Both exist: the 0073 reached ADASA on 11 August and the 0077 on the morning of 18 August, one day after the return date printed on its own form. Under Clause 37.2 the review period runs from formal and complete receipt, which sets the deadlines at Thursday 20 August for 25007-0073 and Thursday 27 August for the other two. This transmittal is issued within all three. Please route future submittals so that the issue date and the receipt date coincide.

Section 3 lists the items open from previous transmittals.

## 2. Observations by Document

### 2.1 Alarm and Interlock List Rev 0 — P22-LI-09-008-015

**Response Code: 1 — Approved**

**Status.** Reviewed against the four points Transmittal N28 set for this issue, and against nothing else. All four are answered in the body of the document. The breaker alarm resolves as P22-PLC01-XA001 on the breaker open contact. The vibration tag is unified to VT-09-001 and the four fault alarms of the note are added, for the two valves and the two dosing pumps. The four housekeeping items are corrected, including the turbocharger boost-failure differential now stated at 10 bar and the CIP tank temperature range at 0 to 100 degrees Celsius.

**On the vibration trip, this list is internally coherent:** item 6.0 ranges VT-09-001 at 0 to 12 mm/s rms and item 6.1 sets the high-high trip at 10, inside that range. What remains is on another document, and it is tracked in Section 3.

**Action: none on this document — accepted.** Related deliverable tracked in Section 3: re-issue of the Instrument List (P22-LI-09-008-003) at the binding range of 0 to 12 mm/s rms for VT-09-001. Two of the added fault tags read VE09-014 and VE09-016, without the hyphen the IO List Rev 5 and the thirteen other valve rows of this list both use; that is housekeeping for the next natural issue and affects no setpoint.

### 2.2 Control and Sequence Chart Rev 0 — P22-LI-09-008-017

**Response Code: 1 — Approved**

**Status.** The seven points Transmittal N28 set for this issue are closed, each verified against the document that governs it. Note 5 now assigns the turbocharger bypass to the pressure control loop on PIT-09-005, with TDS selecting only the setpoint. The second-stage abort reads 93 bar and the high-pressure pump ramps read 0.1 to 0.3 Hz per second. The new Note 9 states the flushing setpoints per stage, 48 and 36 cubic metres per hour under FIT-09-005, and the CIP return valves carry the stage assignment of the IO List. The setpoint and formula corrections are in place, including the brine flow expression, which the comment sheet does not claim.

**Action: none — accepted.** ADASA notes that the two 1 Hz per second ramps remaining in the CIP operation sequence belong to the CIP and flushing pumps, for which the Control Philosophy sets no ramp limit; the 0.1 to 0.3 Hz per second range applies to the high-pressure feed pump and is correctly reflected.

### 2.3 Quality Dossier Index Rev B — P22-BA-09-000-013

**Response Code: 3 — To be revised**

**Status.** The index grows from 27 chapters to 49 and closes five of the ten points. Three are claimed: the dispatch chapters against rows 8.1 and 8.2, the RO pressure vessel package at D6, and the equipment-by-equipment vendor records across Sections D and E. Two are not: the inspection personnel qualifications folded into B3 to B6 with the calibration certificate at C18, and the non-conformance and weld repair chapters at C19 and C20. What remains is set out above. Itemised in `P22-BA-09-000-013_B_Quality_Dossier_Index_CC_ADASA.pdf`.

**The index is not the dossier.** The Fabrication and Testing Dossier required by the Technical Specification (P22-ET-09-000-001-0), Section 7 - Documentation, has not been delivered. This code does not reach it, and it continues to gate items 8.3 and 8.4 of the Inspection and Testing Base Plan.

**Action — re-issue as Rev C.** Three items govern. Add a chapter for the FAT Approval Certificate issued by ADASA, distinct from the release for dispatch already at C21. Complete the document number, revision and inclusion status on every line, and the Inspection and Test Plan row on Sections A, B, D and E. State whether this document is the preliminary index of row 7.6 or the final index of row 8.3, which the plan names separately and holds at different levels. Two further items: add the packing list to the dispatch chapter, and identify in C1, spool by spool, the mill certificates of the super duplex material with the PREN verification of row 2.1 (OBS-01 to OBS-03 and NOTE-01 to NOTE-02 on the annotated PDF).

### 2.4 GA of Antiscalant Dosing Pump Skid Rev C — P22-DWG-09-005-011

**Response Code: 2 — Approved as noted**

**Status.** Rev C answers at an intermediate revision Transmittal N26 had not required. The labelling half of the item closes: Fx and Fy now equal the totals over the ten bolts and each block is identified as a total or a per-bolt value. The reconciliation half does not, for the second consecutive issue and against a comment sheet that reports the forces as updated: the sheet states a total Fz of 1.0242 kN over ten bolts and a per-bolt Fz of 0.205 kN, twice the quotient, where at Rev B the same pair differed by a factor of ten. Itemised in `P22-DWG-09-005-011_C_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf`.

**The reference this item points to does not yet exist in endorsed form.** The note calls the forces "as per calculation report" and Note 5 of the sheet still reads that the bolting details are to be finalised and endorsed. ADASA's letter of 18 August addresses the professional endorsement of the structural calculation report and sets a date for it; this item closes against that report.

**Action to issue at IFC Rev 0 — no new drawing revision required:** state which of the two Fz figures governs and reconcile the per-bolt value with the total over the ten bolts, keeping the axis of each figure explicit (OBS-01 on the annotated PDF). ADASA accepts the drawing on the basis that this is a figure and its label, with no change to the anchorage arrangement.

### 2.5 GA of CIP / Flushing Tank Rev B — P22-DWG-09-005-014

**Response Code: 2 — Approved as noted**

**Status.** Of the two items carried from Transmittal N26 the equipment tag closes: Rev A carried TK-09-001 nowhere on the sheet and Rev B carries it. The nozzle schedule does not. The comment sheet reports it reconciled with the datasheet, and the three entries in dispute are unchanged from Rev A: the top opening reads MH Manhole 533 mm internal diameter where the approved Datasheet of the CIP Tank (P22-ET-09-009-009) Rev B lists HH Handhole DN300, and the side connections N42 and N97 have no counterpart there. Neither document was re-issued; the twelve remaining nozzles agree. Itemised in `P22-DWG-09-005-014_B_GA_CIP_Flushing_Tank_CC_ADASA.pdf`.

The request was to state which document governs, and it stands: the datasheet is not self-consistent either, since its tank construction description calls for a welded conical cover with a manhole cover while its nozzle schedule lists a handhole.

**Action to issue at IFC Rev 0 — no new drawing revision required:** state in writing whether the general arrangement or the datasheet governs the top opening and the two side connections, and align the other document accordingly, re-issuing the Datasheet of the CIP Tank if that is the one that changes (OBS-01 on the annotated PDF).

## 3. Pending Observations from Previous Transmittals

| Origin TM | Document | Observation | Status |
|---|---|---|---|
| N25, N29, N30 | Fabrication and testing dossier | Item 65 remains NOT DELIVERED. The index has now reached Rev B; no record has followed it. It sustains items 8.3 and 8.4 of the Inspection and Testing Base Plan, on which 40 per cent of payment depends | Open, overdue |
| N26, N30 | Endorsed structural calculation report | The report governs the anchorage figures of two general arrangement drawings and the foundations already built at site. Addressed in ADASA's letter of 18 August | Open, overdue |
| N32 | Three non-destructive testing procedures Rev A | None states the ASME B31.3 acceptance criteria required by the Technical Specification (P22-ET-09-000-001-0), Section 8 - Inspections During Manufacturing | Open, Code 3 |
| N28, N34 | Instrument List (P22-LI-09-008-003) Rev E | Re-issue with VT-09-001 ranged at the binding 0 to 12 mm/s rms, so that the high-pressure pump vibration trip of 10 mm/s carried by the Alarm and Interlock List Rev 0 can act. Rev E still reads 0 to 8.9 mm/s rms | Open, raised here |

**Also open:** the liquid penetrant records of 7 August, examined five days before their procedure was submitted, and the six tag reconciliation of the HMI Display Screenshot Rev B, which carries the temperature sensor mapping of the high-pressure pump. Also the design pressure at the brine feed tie-in point, and the calibration validity of certificate 26993 at the date of the pressure test.

## 4. Attachments

| Document | Code | Annotated PDF |
|---|---|---|
| Quality Dossier Index Rev B | 3 | `P22-BA-09-000-013_B_Quality_Dossier_Index_CC_ADASA.pdf` |
| GA of Antiscalant Dosing Pump Skid Rev C | 2 | `P22-DWG-09-005-011_C_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf` |
| GA of CIP / Flushing Tank Rev B | 2 | `P22-DWG-09-005-014_B_GA_CIP_Flushing_Tank_CC_ADASA.pdf` |

All documents with open observations carry annotated PDFs, one Code 3 and two Code 2. The two Code 1 documents, the Alarm and Interlock List and the Control and Sequence Chart, carry none.

## 5. Response Summary

| Document Code | Description | Rev | Submittal | Response |
|---|---|---|---|---|
| P22-LI-09-008-015 | Alarm and Interlock List | 0 | 25007-0073 | 1 — Approved |
| P22-LI-09-008-017 | Control and Sequence Chart | 0 | 25007-0073 | 1 — Approved |
| P22-BA-09-000-013 | Quality Dossier Index | B | 25007-0077 | 3 — To be revised |
| P22-DWG-09-005-011 | GA of Antiscalant Dosing Pump Skid | C | 25007-0080 | 2 — Approved as noted |
| P22-DWG-09-005-014 | GA of CIP / Flushing Tank | B | 25007-0080 | 2 — Approved as noted |

**Overall verdict: 3 — To be revised.** The code is set by one document. The Quality Dossier Index needs the chapter for ADASA's FAT Approval Certificate, the inclusion status of its lines, and a statement of which of the two dossier indices it is. The two documents issued at Rev 0 are approved as they stand; what remains on them lives in other documents and is tracked in Section 3.
