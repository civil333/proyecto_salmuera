---
titulo: Technical Review Transmittal N38 — Second Stage RO Brine Module
codigo: P22-TM-09-000-038-0
fecha: 2026-09-03
estado: BORRADOR
type: transmittal
project: salmuera-taltal
---

# Technical Review Transmittal N38

## 1. Executive Summary

**TRANSMITTAL VERDICT: 2 — Approved as noted.** Submittals 25007-0089 and 25007-0090, eleven documents. Tally: 8 Code 1, 3 Code 2, no Code 3 and no Code 4.

**Seven of the twelve documents required by Thursday 3 September arrived.** The eleven documents in these two submittals are in good order, and this transmittal closes long-standing items on almost all of them. What is missing is the other five, and they are the ones that carry the fabrication dossier and the dispatch. Section 3 sets out the balance.

Disposition at a glance:

- **Piping and Instrumentation Diagram Rev 0 — Code 1.** Correct on the Line List, not here: ADASA has determined that this drawing carries the right sizes.
- **Liquid Penetrant Examination Procedure Rev 0 — Code 1.** State the document number of the procedure when the file is next touched.
- **Ultrasonic Thickness Procedure Rev C — Code 2.** Cite Article 5, write the two reference designations in full and state the sound velocity at Rev 0.
- **Datasheet of RO High Pressure Pump Rev 0 — Code 1.** Nothing outstanding.
- **Line List Rev 1 — Code 1.** Correct the two inverted sizes of 09-048 and 09-049 before those spools are fabricated, and reflect the CIP suction material in the Valve List.
- **Datasheet of Feed Turbocharger Rev 0 — Code 1.** Nothing outstanding.
- **Datasheet of Interstage Turbocharger Rev 0 — Code 1.** Nothing outstanding.
- **Equipment List Rev 0 — Code 1.** Issue the Valve List, which was undertaken together with this one.
- **Instrument List Rev F — Code 1.** Issue at Rev 0 for construction.
- **HMI Display Screenshot Rev C — Code 2.** Swap PIT-09-003 and PIT-09-005 back between the first-stage and second-stage screens at Rev 0.
- **PLC/LCP FAT Procedure - Hardware Rev C — Code 2.** Correct the KA8 remarks column against the I/O List Rev 6 and write the output tags in full at Rev 0.

**Two documents close the cycles that have run longest.** The PLC/LCP FAT Procedure is now a procedure and no longer the record of a test already run, and BW Water undertakes in writing to hold a further Factory Acceptance Test at Penang witnessed by ADASA and a third party against the approved procedure. The HMI Display Screenshot closes six of the seven tag and instrumentation observations raised at Transmittal N31, including the electrical-variable readings required by the Technical Specification.

Section 3 lists the pending observations from previous transmittals and the balance of the consolidated submission.

---

## 2. Observations by Document

### 2.1 Piping and Instrumentation Diagram Rev 0 — P22-DWG-09-009-002

**Response Code: 1 — Approved**

**Status.** The drawing was approved as-is at Transmittal N18 and carried no open condition, so this issue for construction is accepted. It also closes the cartridge filter orientation, now shown vertical. BW Water declares five changes of its own on the comment sheet, of which one requires attention: the line numbers of the new low-pressure super duplex spools do not agree with the Line List issued two days later. This drawing labels 09-048 as DN65 and 09-049 as DN80; the Line List labels them the other way round. These are spools to be fabricated. ADASA has determined that this drawing carries the correct sizes and the Line List Rev 1 carries them inverted, on the grounds set out in the Line List subsection below. This drawing therefore requires no change on that point.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverables tracked in Section 3: the unified line numbering, which also requires the fabrication drawings; the CIP pump suction material change; and the Valve List re-issue that the change of the orifice plate at CIT-09-004 to a pressure reducing valve makes necessary, as the comment sheet itself states.

### 2.2 Liquid Penetrant Examination Procedure Rev 0 — P22-BA-09-000-014

**Response Code: 1 — Approved**

**Status.** The three actions required at Transmittal N37 are verified as done. The report form of Appendix 1 is now issued blank in every field, so the identifiers of the other contract, the three consumable batch numbers and the pre-written result are gone, and the procedure revision field is left for the examiner to complete. This closes a point that had been raised at Transmittal N32 and again at N35. Two items of document identification remain and neither was part of the condition: the cover page still carries the provisional document number rather than the code of this procedure, and two of the fifteen body pages still carry the previous revision index.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverable tracked in Section 3: state the document number of this procedure when the file is next issued.

### 2.3 Ultrasonic Thickness Procedure Rev C — P22-BA-09-000-016

**Response Code: 2 — Approved as noted**

**Status.** The point that governed the Code 3 of Transmittal N35 is closed: clause 9.0 now refers acceptance to the NDE Plan (P22-BA-09-000-005) Rev C, where Rev B cited the material specification, and the material is written UNS S32750 throughout. The couplant of the report form, the non-existent designation in the reference list and the in-service inspection codes are also gone. Four items of reference remain, and one of them was declared corrected and was not: clause 4.0 still cites Article 9 of ASME Section V, which is visual examination, where ultrasonic thickness measurement is governed by Article 5. This is the second revision in which that reference is declared aligned.

**Action to issue at IFC Rev 0 — no new procedure revision required:** cite Article 5 of ASME Section V in the reference clause; write the two designations of the reference list as SA-790 and SA-790M, as ASME designates that specification. State the sound velocity used for UNS S32750 as a value, and write the acceptance criterion of the NDE Plan in clause 9.0 rather than referring to it (OBS-01 and NOTE-01 on the annotated PDF). ADASA accepts the document on the basis that these are incorporated at Rev 0.

### 2.4 Datasheet of RO High Pressure Pump Rev 0 — P22-ET-09-009-002

**Response Code: 1 — Approved**

**Status.** Transmittal N36 accepted the content and asked only that the datasheet be issued at Rev 0 for construction. It is. The motor manufacturer reads the same in both data blocks and on the outline drawing.

**Action: none — accepted; issue directly at IFC Rev 0.**

### 2.5 Line List Rev 1 — P22-LI-09-009-003

**Response Code: 1 — Approved**

**Status.** The list was approved as-is at Transmittal N29 and carried no open condition. Rev 1 adds eight lines, of which six give the low-pressure super duplex spools their own line numbers and their own hydrotest pressure, which is a genuine improvement to the fabrication and testing basis. The hydrotest column of every line common to Rev 0 is unchanged, so the test pressures ADASA has been requiring remain the approved ones. The CIP pump suction changes from PVC to 316L stainless steel because an eccentric PVC reducer could not be sourced; ADASA accepts this as a minor substitution on grounds of availability, and notes that the non-destructive testing column was correctly adjusted for a metallic line. Two line numbers are inverted. This list gives the first-stage CIP reject 54 cubic metres per hour and the second-stage reject 36, and its own approved Rev 0 sizes those same two services at DN80 and DN65 respectively on the high-pressure spools. On the new low-pressure pair it assigns DN65 to the 54 cubic metre service and DN80 to the 36 cubic metre one, which reverses the correspondence. The P&ID Rev 0 carries them the right way round.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** ADASA declares the binding sizes: the first-stage CIP reject at low pressure is CP-SSD-DN80-09-049 and the second-stage reject is CP-SSD-DN65-09-048, as the P&ID Rev 0 shows and as the flow column of this list requires. Correct these two rows before those spools are fabricated. Related deliverables tracked in Section 3: reflect the CIP suction material in the Valve List and the fabrication drawings, and carry these sizes into the unified line numbering.

### 2.6 Datasheet of Feed Turbocharger Rev 0 — P22-ET-09-009-007

**Response Code: 1 — Approved**

**Status.** The condition of Transmittal N36 is verified as done. The four connection callouts of the outline sheet now read the cut groove designation and PIEDMONT STYLE S alone, and the coupling model that carried a different working pressure has been removed from all four. This closes an item first raised at Transmittal N11.

**Action: none — accepted; issue directly at IFC Rev 0.**

### 2.7 Datasheet of Interstage Turbocharger Rev 0 — P22-ET-09-009-008

**Response Code: 1 — Approved**

**Status.** Same as the Feed Turbocharger. The four connection callouts are clean and the datasheet is issued for construction. With the high pressure pump datasheet, the three Fedco equipment datasheets are now all at Rev 0 for construction, with no intermediate approval revision, which is what ADASA required for equipment already bought and built.

**Action: none — accepted; issue directly at IFC Rev 0.**

### 2.8 Equipment List Rev 0 — P22-LI-09-005-001

**Response Code: 1 — Approved**

**Status.** The re-issue undertaken in writing on the 3D model comment sheet has been made. The reverse osmosis vessels are now broken out individually, six in the first stage and four in the second, and the breakdown is internally consistent with the membrane counts of forty-two and twenty-eight at seven per vessel. The cartridge filter specifications and the high pressure pump motor data are also updated. The 3D model at Rev A showed five vessels in the first stage; the approved list governs, and it is the model that has to follow.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverables tracked in Section 3: the Valve List, which was undertaken together with this list and has not been issued, and the alignment of the 3D model to this vessel breakdown.

### 2.9 Instrument List Rev F — P22-LI-09-008-003

**Response Code: 1 — Approved**

**Status.** VT-09-001 is re-ranged to 0 to 12 mm/s rms, which is the binding value ADASA declared at Transmittal N34. The high-pressure pump vibration trip of 10 mm/s carried by the Alarm and Interlock List Rev 0 now falls inside the range of the approved instrument, so the interlock can act. VT-09-002 and VT-09-003 remain at 0 to 8.9 mm/s rms; ADASA declared only VT-09-001 binding and raises no requirement here, but notes that the three are the same transmitter model in the same service.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** ADASA asks that BW Water confirm in writing whether the ranges of VT-09-002 and VT-09-003 are intended to differ from VT-09-001.

### 2.10 HMI Display Screenshot Rev C — P22-LI-09-008-016

**Response Code: 2 — Approved as noted**

**Status.** Rev C closes six of the seven observations raised at Transmittal N31, and does more than its comment sheet declares. A new screen presents the digital power meter with line and line-to-neutral voltages, current per phase, active power in kilowatts, reactive power, frequency, power factor and active energy, which meets the requirement of the Technical Specification (P22-ET-09-000-001-0), Section 5.4 - Control System. The antiscalant level switches, the high-pressure pump, its two temperature elements, the CIP make-up valve and the reject flow transmitter are all correctly tagged, and PIT-09-008 and FIT-09-002 are now shown. One observation is not closed and has been inverted: the first-stage screen still shows PIT-09-005 upstream of the first-stage vessel, and the second-stage screen has been changed to show PIT-09-003 upstream of the second-stage vessel. The Instrument List Rev F defines PIT-09-003 as the first-stage feed pressure transmitter and PIT-09-005 as the second-stage one, so the two tags are now crossed between the screens.

**Action to issue at IFC Rev 0 — no new revision required:** tag the first-stage feed pressure PIT-09-003 and the second-stage feed pressure PIT-09-005, as the Instrument List Rev F defines them (OBS-01 on the annotated PDF). PIT-09-005 is also the process variable of the pressure control loop that governs the turbocharger bypass VE-09-002 in the Control Narrative Rev 1, so the crossed tag falls on the loop that protects that machine. ADASA accepts the document on that basis. Full visual verification of the screens remains reserved for the Factory Acceptance Test.

### 2.11 PLC/LCP FAT Procedure - Hardware Rev C — P22-PP-09-000-001

**Response Code: 2 — Approved as noted**

**Status.** Rev C answers the point that governed the Code 3 of Transmittal N37. The document is now a procedure: it is issued natively rather than as photographs, the test location and date are blank, the results columns are empty and the punch list is a blank table with its three signature blocks. It cites the schematic diagrams and the I/O List by code and by the revisions actually issued, and it identifies itself by one document number throughout. It also declares channels one to four of the input module as spare, which reconciles it with the I/O List Rev 6 and the schematic Rev B. ADASA also notes BW Water's written undertaking to hold a further Factory Acceptance Test at Penang witnessed by ADASA and a third party against the approved procedure. One row is internally contradictory: channel 7 of the output module describes relay KA8 as the CIP heater command in the test text and marks it spare in the remarks column of the same row, and the same tag is repeated across five output rows.

**Action to issue at IFC Rev 0 — no new procedure revision required:** channel 7 of the output module, relay KA8, is the CIP heater on and off command, item 108 of the I/O List Rev 6 approved at Code 1, where it is a dry-contact digital output and not a spare. Correct the remarks column of that row accordingly. Write each output row with the full tag the I/O List carries, including the equipment prefix, in place of the suffix now repeated on five rows (OBS-01 and OBS-02 on the annotated PDF). ADASA accepts the document on that basis. The closure of the eight open category A punch list items belongs to the record of Rev B, not to this procedure, and is tracked in Section 3; so is the operator terminal, which is answered on the schematic diagram.

---

## 3. Pending Observations from Previous Transmittals

**Of the twelve documents required in a single consolidated submission by Thursday 3 September 2026, seven have been received.** The eleven documents reviewed here are in good order and this transmittal raises no Code 3 on any of them. The balance of the requirement stands as follows.

| Required by Thursday 3 September | Status |
|---|---|
| P22-BA-09-000-016 Ultrasonic Thickness Procedure Rev C | Received |
| P22-ET-09-009-002, -007 and -008 Fedco datasheets at Rev 0 for construction | Received, all three |
| P22-LI-09-008-003 Instrument List with VT-09-001 re-ranged | Received |
| 25007-ME-PI-0901-0006 to -0016, eleven shop fabrication drawings | **Not received** |
| P22-CD-09-005-001 Structural Calculation Report with the endorsement of a professional engineer registered in Chile | **Not received** |
| Line numbering unified across the P&ID, the Line List and the fabrication drawings | Partial. Undertaken by BW Water for Friday 28 August at the meeting of 26 August and again for 2 September at the meeting of 1 September. The P&ID and the Line List were received on separate days and do not agree; the fabrication drawings were not received |
| P22-BA-09-000-012 Operating and Maintenance Manual Rev B | **Not received** |
| P22-BA-09-000-013 Fabrication and Testing Dossier Index Rev C | **Not received** |
| P22-LI-09-008-016 HMI Display Screenshot | Received, as an approval revision |
| Factory Acceptance Test procedure of the module, required by Section 8.1 of the Technical Specification | **Not received** |
| Preservation, Packaging and Transport Procedure | **Not received** |
| P22-LI-09-005-001 Equipment List and P22-LI-09-005-002 Valve List | Partial: the Equipment List was received, the Valve List was not |

The delivery plan of the fabrication and testing dossier, with dates by section, was also not received.

**What has not arrived by Thursday 3 September no longer fits a review cycle before the Factory Acceptance Test opens, and passes to the final dossier.** ADASA stated this at Transmittal N37 and applies it as stated, without extending it.

The three most serious items carried forward, all of them named in that requirement and none of them received:

| Origin TM | Document | Observation | Status |
|---|---|---|---|
| N30 | Shop fabrication set 25007-ME-PI-0901-0006 to -0016 | Eleven drawings across seventeen sheets, stamped for construction, removed from the Piping Layout at Rev D and never submitted as a deliverable of their own with an ADASA code and revision index. Their two pressure-containment findings are unanswered: threaded austenitic instrument branches on super duplex lines rated 60 to 90 barG design, and an undeclared specification break between the super duplex and PVC systems | Open, and overdue against three nominated dates: Friday 28 August and 2 September, both undertaken by BW Water at the meetings of 26 August and 1 September, and Thursday 3 September |
| N25, N29, N30 | Fabrication and testing dossier | Item 65 remains NOT DELIVERED. The index has reached Rev B and returned at Code 3; no record has followed it. It sustains rows 8.3 and 8.4 of the Inspection and Test Plan, on which 40 per cent of payment depends | Open, overdue |
| N26, N30 | Endorsed structural calculation report P22-CD-09-005-001 | Issued at Rev 0 for construction carrying internal initials only. It has yet to be issued with the endorsement of a professional engineer registered in Chile, undertaken in writing three times | Open, overdue |

**Entering the list with this transmittal:** the two inverted sizes of the low-pressure CIP reject spools, which ADASA has determined and states here as binding: CP-SSD-DN80-09-049 for the first stage and CP-SSD-DN65-09-048 for the second, as the P&ID Rev 0 shows and as the flow column of the Line List itself requires, to be corrected on the Line List before those spools are fabricated; the CIP pump suction material change, accepted, to be reflected in the Valve List and the fabrication drawings; the Valve List re-issue that the change of the orifice plate at CIT-09-004 to a pressure reducing valve makes necessary; the signed closure of the eight open category A punch list items of the panel test record; the alignment of the 3D model to the six first-stage vessels of the approved Equipment List; and the document number of the liquid penetrant procedure.

**Also open:** the liquid penetrant records of 7 August, examined five days before their procedure was submitted; the measurement point drawing required by row 7.8 of the Inspection and Test Plan; the Pressure Test Record Chart as a controlled form; and the operator terminal installed on the panel against the model ADASA declared binding, which is answered on the schematic diagram.

**Closing with this transmittal, and leaving the list:** the range of VT-09-001; the coupling designation on the two turbocharger datasheets; the issue of the three Fedco datasheets at Rev 0 for construction; the mapping of the high-pressure pump temperature elements; and the reconciliation of the four digital inputs of the panel.

**On the review periods.** These are the sixth and seventh consecutive submittals whose forms ask for return within three calendar days, against the seven working days of Clause 37.2, and the third time the date requested falls on a weekend. Under that clause the review periods of 25007-0089 and 25007-0090 expire on Thursday 10 and Monday 14 September respectively. ADASA has returned both inside the period requested notwithstanding.

---

## 4. Attachments

| Document | Code | Annotated PDF |
|---|---|---|
| Ultrasonic Thickness Procedure Rev C | 2 | P22-BA-09-000-016_C_Ultrasonic_Thickness_CC_ADASA.pdf |
| HMI Display Screenshot Rev C | 2 | P22-LI-09-008-016_C_HMI_Display_Screenshot_CC_ADASA.pdf |
| PLC/LCP FAT Procedure - Hardware Rev C | 2 | P22-PP-09-000-001_C_PLC_LCP_FAT_Procedure_CC_ADASA.pdf |

All documents with open observations carry annotated PDFs, the three Code 2. The eight Code 1 — Approved documents carry none.

**The annotated PDFs are available at the following download link:** [LINK]

---

## 5. Response Summary

| Document Code | Title | Rev | Submittal | Response Code |
|---|---|---|---|---|
| P22-DWG-09-009-002 | Piping and Instrumentation Diagram | 0 | 25007-0089 | 1 — Approved |
| P22-BA-09-000-014 | Liquid Penetrant Examination Procedure | 0 | 25007-0090 | 1 — Approved |
| P22-BA-09-000-016 | Ultrasonic Thickness Procedure | C | 25007-0090 | 2 — Approved as noted |
| P22-ET-09-009-002 | Datasheet of RO High Pressure Pump | 0 | 25007-0090 | 1 — Approved |
| P22-LI-09-009-003 | Line List | 1 | 25007-0090 | 1 — Approved |
| P22-ET-09-009-007 | Datasheet of Feed Turbocharger | 0 | 25007-0090 | 1 — Approved |
| P22-ET-09-009-008 | Datasheet of Interstage Turbocharger | 0 | 25007-0090 | 1 — Approved |
| P22-LI-09-005-001 | Equipment List | 0 | 25007-0090 | 1 — Approved |
| P22-LI-09-008-003 | Instrument List | F | 25007-0090 | 1 — Approved |
| P22-LI-09-008-016 | HMI Display Screenshot | C | 25007-0090 | 2 — Approved as noted |
| P22-PP-09-000-001 | PLC/LCP FAT Procedure - Hardware | C | 25007-0090 | 2 — Approved as noted |
