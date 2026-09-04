# TECHNICAL REVIEW TRANSMITTAL N37 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-037-0 · **Submittals:** 25007-0086, 25007-0087, 25007-0088 · **Date:** 01-Sep-2026
**Source-of-record (English) for the generated DOCX. Run `anti-ia revisar` before issue.**

---

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To be revised.** Submittals 25007-0086 to 25007-0088, seven documents. Tally: 2 Code 1, 4 Code 2, 1 Code 3. One document sets the code: the PLC/LCP FAT Procedure Rev B, submitted for approval as the completed record of a test already run.

**Disposition at a glance:**

- **Liquid Penetrant Examination Procedure Rev C — Code 2.** Correct the report form, which still carries another contract.
- **Radiography Examination Procedure Rev C — Code 2.** Name the material and the wall range actually radiographed.
- **PLC/LCP Schematic Diagram Rev B — Code 2.** Add the CIP heater running feedback terminal; close the operator terminal catalogue number.
- **Instrument Location Layout Rev D — Code 2.** Fill the revision block; state the Equipment Layout revision on the drawing.
- **I/O List Rev 6 — Code 1.** No action.
- **Tie-In Point Layout Rev 0 — Code 1.** Not held; two notes stand.
- **PLC/LCP FAT Procedure - Hardware Rev B — Code 3.** Re-issue as Rev C.

**Why Code 3 — PLC/LCP FAT Procedure Rev B.** The hardware test of the control panel was run on 3 to 5 August at the panel builder in Ningbo. ADASA received no notice and no witness attended, against row 6.2 of the approved Inspection and Test Plan, which assigns ADASA a witness point on that test, and against row 7.1, which is a hold point on ADASA approval of the detailed test procedure. The document submitted now is the completed record of that test, signed as *Witnessed by (Client / Third-Party Inspector)* by BW Water personnel. Its punch list marks ten items category A, defined in the document itself as *"Must be resolved BEFORE panel dispatch"*, and eight of them carry target date, actual date and status blank. Three of the five points ADASA raised at Transmittal N27 remain open.

**Two documents close long-standing items.** The Instrument Location Layout clears the Code 3 it has carried since Transmittal N23, and the Tie-In Point Layout reaches Rev 0 with the brine feed design pressure declared at 5 barG, consistent with the approved Line List. Two of the three non-destructive testing procedures also clear the acceptance criterion that returned them at Code 3.

**Return date.** Clause 37.2 gives seven working days: 7 September for 25007-0086 and 25007-0087, 8 September for 25007-0088. This transmittal is issued within all three. The forms asked for return three calendar days after issue, two of them on a Sunday.

**The consolidated close-out of all outstanding documentation, and its date, are set out under Pending Observations from Previous Transmittals.**

---

## 2. Observations by Document

### 2.1 Liquid Penetrant Examination Procedure Rev C — P22-BA-09-000-014

**Response Code: 2 — Approved as noted**

**Status.** The determinant closed. Clause 13.0 now offers a single acceptance criterion, ASME B31.3 paragraph 341.3.2 with its thresholds, and the Section VIII Division 1 Appendix 6 block is gone; the form the examiner signs declares that same criterion. What did not close is the report form itself, which still carries the report number and the job number of another contract, three consumable batch numbers, and an observations column pre-written with the result. That form is the sheet that enters the quality dossier, and this is the second time it is raised. Itemised in P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new procedure revision required:** clear the report form of the identifiers of another contract and of the pre-written result, and align the procedure revision it cites with the revision of the document (OBS-01 to OBS-03 and NOTE-01 on the annotated PDF). The comment sheet answers *"Revised as per comment"* to a block that names the report form data of another contract; that reply does not match the document.

### 2.2 Radiography Examination Procedure Rev C — P22-BA-09-000-015

**Response Code: 2 — Approved as noted**

**Status.** The determinant closed in both halves. The five acceptance codes of clause 23.0 came down to one, and the geometric unsharpness limit of 1.8 mm, which is the Section I dispensation for power piping and which B31.3 does not grant, was replaced by the 0.020 in. of Table T-274 with its text reproduced. What remains is scope: clause 1.0 still reads generically and names neither the ASTM A790 UNS S32750 nor the 6.02 to 8.56 mm wall range actually radiographed on this module, and the cover still carries the document number of a positive material identification procedure. Itemised in P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new procedure revision required:** state the material and the wall thickness range of this module in the scope, and correct the document number on the cover (OBS-01 and NOTE-01 to NOTE-03 on the annotated PDF).

### 2.3 PLC/LCP Schematic Diagram Rev B — P22-CD-09-008-002

**Response Code: 2 — Approved as noted**

**Status.** Second cycle on the condition of Transmittal N20. The reconciliation of inputs and outputs against the approved I/O List is nearly complete: the CIP heater output is wired on sheet 39 through relay KA8, the four spare inputs on sheet 35 match the three rows the I/O List deleted at Rev 6, and the air conditioning signals are on sheets 37 and 38. One terminal is missing: **CIP HEATER RUNNING**, item 109 of the I/O List Rev 6, has no terminal on any of the four digital input sheets, nineteen assigned against twenty active in the list, with thirteen free terminals available. The heater output was wired and its running feedback was not. Separately, the bill of materials on sheet 28 still lists the operator terminal as 2711P-T10C21D8S. Itemised in P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new schematic revision required:** assign a digital input terminal to CIP HEATER RUNNING and cite the I/O List by its code and its numeric revision, since the comment sheet answers against an *"I/O List Rev B"* that does not exist. On the operator terminal, ADASA declared the 2711P-T10C22D9P binding at Transmittal N30 and the record of the panel test now shows the 2711P-T10C21D8S installed: state in writing how BW Water proposes to close that gap, together with the two Ethernet ports the approved datasheet requires (OBS-01 to OBS-02 and NOTE-01 on the annotated PDF).

### 2.4 Instrument Location Layout Rev D — P22-DWG-09-008-001

**Response Code: 2 — Approved as noted**

**Status.** The determinant closed. The geometry is now drawn against the Equipment Layout Rev D, which reached Code 1 at Transmittal N33, so the dependency on a superseded drawing is lifted, and the title block code and the issue date are correct. Two changes to the drawing itself remain, both verified by render of the title block. The revision block carries four rows, D, C, B and A, and all four repeat the same description, ISSUED FOR APPROVAL, with the change notice column blank, so no row states what changed at its issue; and the row of Rev C, which reads APR.17.26 on the drawing issued at Rev C, now reads JUN.16.26, so the April issue was overwritten instead of a row being added and the two Rev C issues that the original observation was about are still not distinguishable. And the declaration that the drawing follows the Equipment Layout Rev D lives only on the reply sheet: the note box of both sheets is empty and there is no reference document list. Itemised in P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new drawing revision required:** fill the revision block with what changed at each issue instead of repeating the same description, and restore the April issue date on the row of Rev C so the two issues that carried that letter are distinguishable. The note box is to state the Equipment Layout revision the drawing is built on (OBS-01 to OBS-02 on the annotated PDF). The change notice column is not required: it is empty on the Equipment Layout as well, so it is a project convention and not an omission.

### 2.5 I/O List Rev 6 — P22-LI-09-008-001

**Response Code: 1 — Approved**

**Status.** The single action of Transmittal N28 closed, and it was verified on the list and not on the declaration: row 108 carries REL-09-001, HS001, CIP HEATER ON/OFF COMMAND as a dry contact output, and row 109 carries REL-09-001, XB002, CIP HEATER RUNNING as the input in the opposite direction, both at revision 6. The list is issued for construction, so the condition fell due at this issue and there is no substantive defect against it.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverable tracked under Pending Observations from Previous Transmittals: the running feedback that this list now defines still has no terminal on the schematic diagram, and the four digital inputs signed off on the panel test record are not the four this revision carries.

### 2.6 Tie-In Point Layout Rev 0 — P22-DWG-09-005-005

**Response Code: 1 — Approved**

**Status.** The oldest open document of the package reaches Rev 0 with its substantive point closed. The tie-in schedule now carries a complete DESIGN PRESSURE column and the brine feed point TP-DA P8-001, 4 inch, class 150 to ASME B16.5, is declared at 5 barG, which matches the line DA-PVC-DN100-09-001 of the Line List Rev 0 approved at Code 1: the ADASA acceptance of the ANSI 150 class is satisfied. The drawing is issued for construction and is not held.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Two notes to fold into the next natural issue, neither of which holds a drawing that already governs construction. First, the reply states that TP-AS P11-001 is not a flanged connection and that the termination is the valve itself; the two cells still read as a dash and the drawing does not say it, so the sheet should carry what the reply says. Second, the DRAWING STATUS field of the title block reads ISSUED FOR APPROVAL while the revision row of the same title block and the submittal form both read ISSUED FOR CONSTRUCTION, and the cover still carries Revision A dated 02/04/2026.

### 2.7 PLC/LCP FAT Procedure - Hardware Rev B — P22-PP-09-000-001

**Response Code: 3 — To be revised**

**Status.** This revision is not a procedure. It is the completed record of the hardware test of the control panel, run on 3 to 5 August at the panel builder in Ningbo, submitted as an approval revision three weeks later. The condition of its Code 2 at Transmittal N27 was tied to a milestone that was not Rev 0: it read *before witnessing*, and that milestone passed. Three of the five points remain open. Eight of the ten category A punch list items, all raised by the BW Water engineer, have target date, actual date and status blank, and the closing block of the punch list is empty; an attached rectification report declares them executed with photographs, unsigned, undated and unwitnessed. Six of the eight are signals the approved I/O List has carried since revisions 3 and 4. The document is photographed rather than issued, and eleven of its sixteen pages return no readable text. Itemised in P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf.

**Action — re-issue as Rev C:** submit the procedure as a procedure, separate from any record, citing the schematic diagram and the I/O List by code and by issued revision; close the eight open category A punch list items with target date, actual date, status and signature, and have the closure witnessed; reconcile the four digital inputs and the output relay map signed off on the record against the I/O List Rev 6 and the schematic Rev B, which today state three different things; and list the model, serial number and calibration certificate of each test instrument, as safety requirement 3 of the document itself requires (OBS-01 to OBS-05 and NOTE-01 to NOTE-02 on the annotated PDF).

---

## 3. Pending Observations from Previous Transmittals

**BW Water is to stop submitting documents one at a time as construction proceeds, and is to deliver every outstanding engineering document, drawing and procedure in a single consolidated submission, no later than Thursday 3 September 2026.**

Three facts make this necessary, and none of them is a matter of opinion. Documents are arriving after the thing they describe exists: the record of the panel test arrives now and the test was run on 3 to 5 August; the Tie-In Point Layout arrives at Rev 0 with fabrication under way; the I/O List arrives issued for construction. The review cycle has stopped serving its purpose: the review period of 25007-0088 under Clause 37.2 expires after the Factory Acceptance Test opens, so ADASA is asked to review the gate document of a test that has already started. And this is the fifth consecutive batch whose forms ask for return inside three calendar days against the seven working days of Clause 37.2, twice falling on a weekend.

**What arrives after Thursday 3 September no longer fits a review cycle before the Factory Acceptance Test opens, and passes to the final dossier.** ADASA is stating a fact about the calendar, not a position.

The three most serious items carried forward:

| Origin TM | Document | Observation | Status |
|---|---|---|---|
| N30 | Shop fabrication set 25007-ME-PI-0901-0006 to -0016 | Eleven drawings across seventeen sheets, stamped for construction, removed from the Piping Layout at Rev D and never submitted as a deliverable of their own with an ADASA code and revision index. Their two pressure-containment findings are unanswered: threaded austenitic instrument branches on super duplex lines rated 60 to 90 barG design, and an undeclared specification break between the super duplex and PVC systems | Open, aggravated by the withdrawal without re-submission |
| N25, N29, N30 | Fabrication and testing dossier | Item 65 remains NOT DELIVERED. The index has reached Rev B and returned at Code 3; no record has followed it. It sustains rows 8.3 and 8.4 of the Inspection and Test Plan, on which 40 per cent of payment depends | Open, overdue |
| N26, N30 | Endorsed structural calculation report P22-CD-09-005-001 | Issued at Rev 0 for construction carrying internal initials only. It has yet to be issued with the endorsement of a professional engineer registered in Chile, undertaken in writing three times | Open, overdue |

The consolidated submission of Thursday 3 September is to contain, at minimum:

| Document | Required | Origin |
|---|---|---|
| P22-BA-09-000-016 Ultrasonic Thickness Procedure | Rev C. The only one of the three non-destructive testing procedures that has not returned | Code 3 since N35 |
| P22-ET-09-009-002, -007 and -008 Fedco datasheets | Rev 0 for construction, deleting STYLE 77 from the four connection callouts | N36 |
| P22-LI-09-008-003 Instrument List | Re-issue with VT-09-001 ranged at 0 to 12 mm/s rms | N34 |
| 25007-ME-PI-0901-0006 to -0016 | Eleven shop fabrication drawings across seventeen sheets, submitted as a deliverable of their own with code and revision | N30 |
| P22-CD-09-005-001 Structural Calculation Report | With the endorsement of a professional engineer registered in Chile | N26, N30 |
| P22-DWG-09-009-002, P22-LI-09-009-003 and the fabrication drawings | Line numbering unified against the approved Line List | Coordination meeting of 26 August |
| P22-BA-09-000-012 Operating and Maintenance Manual | Rev B | Code 3 since N27 |
| P22-BA-09-000-013 Fabrication and Testing Dossier Index | Rev C | Code 3 since N34 |
| P22-LI-09-008-016 HMI Display Screenshot | Rev 0 with the six tags reconciled | Code 2 since N31 |
| Factory Acceptance Test procedure of the module | Never delivered. Required by Section 8.1 of the Technical Specification | ET Section 8.1 |
| Preservation, Packaging and Transport Procedure | Hold point for approval prior to shipment | BAE Clause 41 |
| P22-LI-09-005-001 Equipment List and P22-LI-09-005-002 Valve List | Re-issue, undertaken in writing on the 3D Model comment sheet | N36 |

**On the Operating and Maintenance Manual there is no dependency left.** It was returned at Code 3 at Transmittal N27 because sections 4.4 and 4.5 reproduced logic assigned to control documents that were then open. Those documents have closed: the Alarm and Interlock List and the Control and Sequence Chart were both issued at Rev 0 and approved at Code 1 at Transmittal N34. Nothing now holds the manual.

**The fabrication and testing dossier is treated separately, and is not part of the Thursday submission.** It depends on records generated during fabrication. What ADASA requires by Thursday 3 September is the delivery plan of the dossier, with dates by section, against the index at Rev C.

**Also open:** the liquid penetrant records of 7 August, examined five days before their procedure was submitted; the measurement point drawing required by row 7.8 of the Inspection and Test Plan; and the Pressure Test Record Chart as a controlled form. Entering the list with this transmittal: the reconciliation of the four digital inputs and of the output relay map between the panel test record, the I/O List Rev 6 and the schematic Rev B, which today state three different things. Closing with this transmittal, and leaving the list: the design pressure at the brine feed tie-in point.

---

## 4. Attachments

| Document | Code | Annotated PDF |
|---|---|---|
| Liquid Penetrant Examination Procedure Rev C | 2 | P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf |
| Radiography Examination Procedure Rev C | 2 | P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf |
| PLC/LCP Schematic Diagram Rev B | 2 | P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf |
| Instrument Location Layout Rev D | 2 | P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf |
| PLC/LCP FAT Procedure - Hardware Rev B | 3 | P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf |

All documents with open observations or notes carry annotated PDFs, four Code 2 and one Code 3. Only the two Code 1 — Approved documents carry none.

**The annotated PDFs are available at the following download link:** [LINK]

---

## 5. Response Summary

| Document Code | Title | Rev | Submittal | Response Code |
|---|---|---|---|---|
| P22-BA-09-000-014 | Liquid Penetrant Examination Procedure | C | 25007-0086 | 2 — Approved as noted |
| P22-BA-09-000-015 | Radiography Examination Procedure | C | 25007-0086 | 2 — Approved as noted |
| P22-CD-09-008-002 | PLC/LCP Schematic Diagram | B | 25007-0086 | 2 — Approved as noted |
| P22-DWG-09-008-001 | Instrument Location Layout | D | 25007-0086 | 2 — Approved as noted |
| P22-LI-09-008-001 | I/O List | 6 | 25007-0086 | 1 — Approved |
| P22-DWG-09-005-005 | Tie-In Point Layout | 0 | 25007-0087 | 1 — Approved |
| P22-PP-09-000-001 | PLC/LCP FAT Procedure - Hardware | B | 25007-0088 | 3 — To be revised |
