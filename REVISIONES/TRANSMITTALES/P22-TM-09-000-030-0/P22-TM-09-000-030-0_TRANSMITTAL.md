# TECHNICAL REVIEW TRANSMITTAL N30 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-030-0 · **Submittals:** 25007-0068 (E68), 25007-0069 (E69), 25007-0070 (E70) · **Date:** 05-Aug-2026
**Source-of-record (English) for the generated DOCX. Run `anti-ia revisar` before issue.**

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To be revised.** Five documents across three submittals. Tally: 2 Code 1, 2 Code 2, 1 Code 3, plus one uncoded set returned as not received. The Dossier Index fixes the verdict: it omits four chapters its own governing documents require and carries no document number or revision against any of its 27 lines, so it cannot serve as the checklist ADASA uses to review the dossier. Two pressure-containment items on the shop fabrication set require correction before those spools are built.

Disposition at a glance:
- **Datasheet of PLC and HMI Panel Component Rev 0 — Code 1.** Align the four documents carrying the other terminal catalogue number.
- **Fabrication and Testing Dossier Index Rev A — Code 3.** Re-issue as Rev B with the missing chapters and full traceability per line.
- **Piping Layout Rev C — Code 2.** Add the tie-in schedule and the battery-limit flange class at Rev 0.
- **Shop fabrication set 25007-ME-PI-0901-0006 to -0016 — not received.** Submit as a deliverable in its own right and correct the two pressure-containment items.
- **3D Model Rev A — Code 2.** Identify the file by its code and revision and reconcile its tags with the approved lists.
- **Datasheet of Differential Pressure Switch Rev B — Code 1.** Issue directly at IFC Rev 0.

Section 3 lists the pending observations from previous transmittals.

## 2. Observations by Document

### 2.1 Datasheet of PLC and HMI Panel Component Rev 0 — P22-ET-09-008-001 — Code 1

**Status.** Rev 0 closes the Transmittal N26 cycle. The document code is aligned to P22-ET-09-008-001 on the cover and on all seven component headers, and the RTD-module quantity is confirmed as two 5069-IY4 units on the Control System Architecture Rev D, covering the four temperature elements of the I/O List Rev 5. No technical content changed between Rev C and Rev 0 and the datasheet requires no modification to itself.

**Binding declaration — operator terminal.** The catalogue number of the operator terminal has differed between this datasheet and the control set since the first issue of both. ADASA declares the binding catalogue number to be **2711P-T10C22D9P**, stated in this datasheet since Rev A and fixed at Transmittal N22 as the hardware basis for the HMI screen design. Per the manufacturer's technical data, catalogue number 2711P-T10C21D8S provides one 10/100Base-T Ethernet port and 512 MB of RAM and therefore does not meet the two Ethernet RJ45 ports and 1 GB stated in the requirement rows of this datasheet. Should BW Water intend to supply the Standard terminal instead, state so in writing before procurement, demonstrating that it meets the requirement of the Technical Specification (P22-ET-09-000-001-0), Section 5.4 - Control System, to store historical data and display trends of the main process variables. The point is time-critical because the panel enters fabrication before the next document cycle.

**Action: none on this document — accepted; the datasheet stands as issued at Rev 0.** Related deliverables tracked in Section 3: alignment of the PLC/LCP Outline Panel Drawing Rev 0, the PLC/LCP Schematic Diagram Rev A, the PLC/LCP FAT Procedure Rev A and the Control System Architecture Rev D to the binding catalogue number. Six documentation items are to be corrected at the next natural issue of this datasheet, none of them affecting its technical content: the consolidated comment sheet no longer carries the closure record of the three Transmittal N21 items and cites a revision that does not exist; the cover states 49 pages against the 50 issued; the seven component headers keep the "Issued for Approval" stamp on a submission for construction; the analog-output sheet carries the design intent of a digital output and leaves its model as 5069-OF4/OF8 where the Control System Architecture fixes two 5069-OF4; and the component headers carry no revision index.

### 2.2 Fabrication and Testing Dossier Index Rev A — P22-BA-09-000-013 — Code 3

**Status.** First issue of the index requested in ADASA's letter of 25-Jul. It arrived on Monday 27-Jul; the records that were to accompany it did not. As a document it cannot yet perform its function: it lists 27 chapters with no traceability and omits several chapters that its own governing documents require. Itemised in P22-BA-09-000-013_A_CC_ADASA.pdf.

**Action — re-issue as Rev B:** add the document number, revision and inclusion status to every line with a cross-reference to the row of the Inspection and Test Plan that generates each record, and add the chapters for dispatch preparation, the FAT Approval Certificate, inspection personnel qualifications and test equipment calibration, main equipment manufacturer certificates, and the non-conformance and weld repair register (OBS-01 to OBS-06 and NOTE-01 to NOTE-04 on the annotated PDF). The three non-destructive testing procedures listed in chapters B3, B4 and B6 are to be submitted for ADASA review before welding starts, since records produced under procedures not yet approved are not admissible into the dossier.

**This code applies to the index as a document.** The dossier as a deliverable of the Technical Specification (P22-ET-09-000-001-0), Section 7, has not been delivered and is unaffected by it: it remains outstanding and continues to gate items 8.3 and 8.4 of the Inspection and Testing Base Plan (P22-IT-09-000-001-0).

### 2.3 Piping Layout Rev C — P22-DWG-09-005-004 — Code 2

**Status.** The document declares itself as four pages and those four are in order: the general arrangement, the two sections and the isometric views are consistent with the approved Line List and resolve the equipment access and lateral openings and the antiscalant and CIP battery-limit terminations carried from Transmittal N15. Two of the four items carried from Rev B remain partly open and are incorporable at IFC Rev 0 without a further revision. The file also contains eighteen pages that do not belong to this document; those are dealt with in Section 2.4. Itemised in P22-DWG-09-005-004_C_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new drawing revision required:** add a tie-in schedule listing, for every battery-limit connection, the line tag, nominal diameter, connection type and elevation referred to a datum declared on the drawing, covering the permeate and CIP supply and return lines; annotate the flange class against the CIP and antiscalant battery-limit terminations consistent with the approved Line List; and state whether the module carries one or two local control panels, tagging each enclosure consistently with the approved Local Control Panel datasheet and the Single Line Diagram (OBS-02, OBS-03 and NOTE-01 to NOTE-03 on the annotated PDF). ADASA accepts the drawing on the basis that these are annotations and schedules added to the existing geometry, with no change to the arrangement.

**Tracked as a cross-document deliverable, with no modification to this drawing:** confirmation that the anchorage of the container and of the external CIP and dosing area, with the corresponding loads and bolt layout for the ADASA concrete bases, is covered by the seismic calculation report and the civil requirements drawing, stating the code and issue date of both. The holding-down bolts for the externally mounted equipment are to be defined and supplied by the equipment manufacturer.

### 2.4 Shop fabrication set 25007-ME-PI-0901-0006 to -0016 — returned as not received

**Status.** Pages 5 to 21 of the file submitted under P22-DWG-09-005-004 Rev C are eleven shop fabrication drawings under BW Water's own numbering, with their own revision index, spool titles instead of a drawing title, and a FOR CONSTRUCTION stamp on all seventeen pages. They carry no ADASA document code, they are not listed in the Submittal Form, and the cover sheet of the document containing them declares "Page 1 of 4". ADASA cannot approve or reject what was not submitted, so this set is returned as not received and carries no response code. Itemised in 25007-ME-PI-0901_CC_ADASA.pdf.

**Two items require correction before any of these spools is built.** They are issued now, ahead of the formal submission, because the sheets are stamped for construction and dated 23-Jul:

- **Threaded austenitic branch connections on the highest-pressure super duplex lines.** The half-inch instrument tappings on sheets 11, 12, 14, 16, 17, 18 and 20 are resolved with ANSI 150# threaded half couplings in ASTM A182 Gr. F304 and F316L, on lines that the approved Line List rates at 60 to 90 barG design and 90 to 135 barG hydrotest, in brine of 45,000 to 55,000 ppm chloride. The Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure Piping, requires super duplex ASTM A182 F53 UNS S32750 with PREN above 40 and Class 900 rating for high-pressure components. The same sheets already use the correct detail on other half-inch branches, in super duplex sockolets to MSS SP 97.
- **Undeclared specification break between the super duplex and PVC systems.** On sheets 5, 6, 7 and 9 the boundary between the two systems sits at an ANSI 150# flanged joint adjacent to a single motorised butterfly valve, with no specification break symbol and no line number split. The spools titled CP-SSD-DN65-09-045 and CP-SSD-DN80-09-044 incorporate PVC SCH 80 pipe while the approved Line List classifies both lines as super duplex at 80 to 90 barG design and 120 to 135 barG hydrotest, and rates the PVC lines at 5 barG design and 7.5 barG hydrotest.

**Action:** either remove the shop fabrication set from P22-DWG-09-005-004 and submit it as a separate deliverable with its own ADASA code and revision index, or extend the cover sheet and the Submittal Form to declare it, stating in both cases the review status expected from ADASA. Replace the threaded austenitic couplings with welded super duplex branch fittings and confirm in writing that no austenitic, threaded or Class 150 pressure-retaining component remains anywhere in the super duplex system, stating whether any of these branches has already been fabricated. Show the specification break explicitly, split the line numbers at that joint so the PVC segments carry their own line number, piping class, design pressure and hydrotest pressure, issue the corresponding addition to the Line List, and state how the PVC side is protected from the high-pressure side with the motorised valve closed (OBS-01, OBS-04, OBS-05 and OBS-06 on the annotated PDF).

### 2.5 3D Model Rev A — P22-DWG-09-005-007 — Code 2

**Status.** First issue of the model, submitted for approval. It is a federated Navisworks file built from a single AutoCAD Plant 3D source, in millimetres, with typed objects that carry engineering properties: line numbers, tags, classes, sizes and specifications. ADASA reviewed it against the approved Equipment, Valve, Instrument and Line Lists using those object properties. The model is coherent with the approved lists in the large majority of its content, and what requires correction are the identification of the file and a defined set of tag divergences.

**Action to issue at IFC Rev 0 — no new model revision required:**

- Identify the file by its document code P22-DWG-09-005-007 and its revision index in the document properties, and issue the final revision under that identity. The file as received is titled "V14 Taltal.nwd".
- Correct the malformed tags: BH-009-002, which carries three digits in the area segment where the approved Equipment List states BH-09-002; and VM-09-094, which carries a trailing question mark.
- Resolve the fifty-seven objects whose tag property is set to a question mark.
- Reconcile with the approved lists: DPS-09-002 in the model against DPS-09-001 in the Instrument List Rev E and in the datasheet issued in this same submittal; BOI-09-006 and the valves VM-09-131, VM-09-132, VM-09-133 and VRP-09-001, which do not appear in the approved Equipment and Valve Lists; the reverse osmosis vessels, modelled as BOI-09-001-1 to -5 and BOI-09-002-1 to -4 where the Equipment List declares BOI-09-001 and BOI-09-002.
- Reconcile four line numbers where the model and the approved Line List disagree on an attribute while sharing the sequential number: 09-042 as DN80 against DN50, 09-015 as DN100 against DN80, 09-044 as DN65 against DN80, and 09-026 as antiscalant service against CIP service. Resolve the reuse of sequential number 09-001 by both DA-PVC-DN100-09-001 and RD-PVC-DN15-09-001, the latter not appearing in the approved Line List.

Where a divergence reflects a change of engineering rather than a modelling error, issue the corresponding revision of the affected list so that the model and the lists state the same thing.

**No annotated PDF accompanies this document.** A Navisworks file cannot carry the annotation format used for drawings, so the observations above are stated in full here.

### 2.6 Datasheet of Differential Pressure Switch Rev B — P22-LI-09-008-006 — Code 1

**Status.** Rev B of a datasheet that ADASA approved at Rev A in Transmittal N8. The consolidated comment sheet declares the reason for the revision: the vendor could not pass the quality test for Monel wetted parts, so a diaphragm seal is added as the alternative, and the datasheet is extended with its information. ADASA accepts the change as declared.

**Action: none — accepted; issue directly at IFC Rev 0.**

## 3. Pending Observations from Previous Transmittals

| Origin TM | Document | Observation | Status |
|---|---|---|---|
| N28 | Control family (Control Philosophy Rev E, Alarm & Interlock List Rev C, Control & Sequence Chart Rev A) | each correct in what it governs, but the three disagree on tags and setpoints (winding and bearing mapping, HP pump vibration trip) | **OVERDUE**: the coordinated re-issue at Rev 0 was due Friday 31 July and no revision has been received |
| N22 | HMI Display Screenshot (P22-LI-09-008-016 Rev A) | the electrical-variables and energy screen, the trending screen, the setpoint screen and several process zones are still missing | OPEN: re-issue as Rev B. Oldest open commitment in the project |
| N27 | Operating and Maintenance Manual (P22-BA-09-000-012 Rev A) | governed by the Control family; cannot close until that set issues at Rev 0 and the HMI screenshots issue | OPEN: Rev B after the Control family closes |

**Also open:** the fabrication and testing dossier itself, outstanding against the Technical Specification, Section 7, and gating items 8.3 and 8.4 of the Inspection and Testing Base Plan; Equipment Layout Rev C (Code 3, RO cartridge filter orientation); GA of the Antiscalant Dosing Tank Rev B (Code 3, seismic anchor loads); Instrument Location Layout Rev C (Code 3, from Transmittal N23); Tie-In Point Layout Rev A (Code 3, from Transmittal N7, the longest-standing open item); and the FAT Procedure RTD protection sign-off, held from Transmittal N27 until the Control Philosophy issues at Rev 0.

**Cross-document reconciliation carried from Section 2.1:** the operator-terminal catalogue number in the PLC/LCP Outline Panel Drawing Rev 0, the PLC/LCP Schematic Diagram Rev A, the PLC/LCP FAT Procedure Rev A and the Control System Architecture Rev D, to be corrected to 2711P-T10C22D9P.

**Review period.** The Submittal Form of 25007-0070 requests return by Saturday 8 August, three calendar days from issue. The standard documentary review period of the Special Administrative Conditions (BAE 12803), Clause 37.2, is seven working days, which for this submittal ends on Friday 14 August. This transmittal is issued within that period.

## 4. Attachments

| Attachment | Covers |
|---|---|
| P22-BA-09-000-013_A_CC_ADASA.pdf | Fabrication and Testing Dossier Index Rev A — OBS-01 to OBS-06 and NOTE-01 to NOTE-04 |
| P22-DWG-09-005-004_C_CC_ADASA.pdf | Piping Layout Rev C, all 22 pages — the four pages of the document and the seventeen shop fabrication sheets bundled with them |

Two annotated PDFs, not three: the shop fabrication sheets are pages 5 to 21 of the same file as the Piping Layout, so a single annotated PDF carries the observations of both subsections. Its identifiers run consecutively across the whole file — OBS-01 to OBS-06 and NOTE-01 to NOTE-03 — because two different observations cannot share an identifier within one document.

All documents with open observations carry an annotated PDF, with two exceptions stated here rather than left unexplained. The two Code 1 documents require no modification and carry none. The 3D Model is a Navisworks file that cannot carry the annotation format used for drawings, so its observations are stated in full in Section 2.5.

**Download — this transmittal and the annotated PDFs:** https://lrg.synology.me:6501/d/s/19Llot7JjfVf8lcyurHIZDfL6nZ13HIC/V4Ej-jY6AOk8cbU29kS4w7Z3SD8wrWSB-4r-gvdeEZw0

## 5. Response Summary

| Document Code | Title | Rev | Submittal | Response Code |
|---|---|---|---|---|
| P22-ET-09-008-001 | Datasheet of PLC and HMI Panel Component (Major Component) | 0 | 25007-0068 | 1 — Approved |
| P22-BA-09-000-013 | Fabrication and Testing Dossier Index | A | 25007-0069 | 3 — To be revised |
| P22-DWG-09-005-004 | Piping Layout | C | 25007-0070 | 2 — Approved as noted |
| P22-DWG-09-005-007 | 3D Model | A | 25007-0070 | 2 — Approved as noted |
| P22-LI-09-008-006 | Datasheet of Differential Pressure Switch | B | 25007-0070 | 1 — Approved |
| 25007-ME-PI-0901-0006 to -0016 | Shop fabrication set (17 sheets) | 1 | not submitted | returned — not received as a deliverable |

**Overall Transmittal Verdict: 3 — To be revised.** The Fabrication and Testing Dossier Index fixes the verdict and is to be re-issued as Rev B. The two pressure-containment items of the shop fabrication set are to be corrected before those spools are built, and that set is to be submitted as a deliverable in its own right.
