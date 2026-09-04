# TECHNICAL REVIEW TRANSMITTAL N23 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-023-0
**Date:** 18-Jun-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittal:** 25007-0051 and 25007-0052

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — To Be Revised.** Seven documents, submittals 25007-0051 (quality and fabrication package) and 25007-0052 (instrument layout and structural criteria). Tally: 0 Code 1, 1 Code 2, 6 Code 3. Driver: the RO Vessel Hydrostatic Test Procedure — the single fabrication test the ASME stamp waiver was traded for is internally inconsistent on its test pressure.

**Disposition at a glance:**

- **Inspection and Test Plan Rev C — Code 2.** Materially closes the package's oldest open item: the waiver basis (1,800 psi x 1.1 vessel test, ADASA witness, dossier hold points) is now captured; two edits fold into Rev 0.
- **RO Vessel Hydrostatic Test Procedure Rev A — Code 3.** No binding test pressure in the body and a 45.5 bar value on the report form, against the 1,980 psi the waiver and the ITP require.
- **HP and LP Pressure Test Procedure Rev A — Code 3.** No numeric test pressure stated; HP design pressure (90 versus up to 120 bar) unreconciled.
- **NDE Plan Rev B — Code 3.** Governing code editions still left as placeholders (the Rev A comment not closed) and structural/thermoplastic codes mixed with the high-pressure circuit.
- **Painting Procedure Rev A — Code 3.** Brand system substituted (Jotun for the approved Sherwin-Williams system) without an equivalence justification, and marine C5-M durability not demonstrated.
- **Instrument Location Layout Rev C — Code 3.** Content changed but the revision letter not bumped, and the geometry is aligned to a superseded Equipment Layout that is itself open at Code 3.
- **UHPRO Structural Design Criteria Rev A — Code 3.** Lacks the lifting (transport/erection) load case and yoke design criteria the module Technical Specification requires; the seismic citation must also be aligned to NCh 2369 Of.2003 (the parameter table shows a non-existent 2009 edition).

**Why Code 3 — RO Vessel Hydrostatic Test Procedure Rev A:** the Inspection and Test Plan correctly fixes the RO Vessel hydrostatic test at 1,800 psi x 1.1, but the supporting test procedure delivered in the same package states only a generic rule (1.1 times design pressure for ASME, 1.43 times for CE certified) and its embedded vendor report form carries 45.5 bar, roughly a third of the required 1,980 psi. The witness point and the dossier the stamp waiver was traded for are worthless if the value the inspector signs against is the one printed on that form. The Painting Procedure and the Instrument Location Layout independently sustain the new-revision path. Open items from previous transmittals are inventoried in Section 3.

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 Inspection and Test Plan Rev C — P22-BA-09-000-004

**Response Code: 2 — Approved as Noted**

**Status.** The Inspection and Test Plan Rev C materially closes the package's oldest open fabrication item. It now carries the three elements of the agreed ASME waiver: the RO Vessel hydrostatic test at 1,800 psi x 1.1 (row 2.2), the PMI of Super Duplex as a witness point (row 2.4), and the production and test dossier as a preliminary review and a final Hold Point (rows 7.6 and 8.3). ASME Section X is the correct code basis because the vessels are FRP, not Section VIII steel. What remains is internal to the document and folds into the Rev 0 issue: the no-code-stamp basis is not stated, and the vessel hydrostatic test is coded Witness where the agreed basis and the internal consistency with the high-pressure system test (Hold Point) call for a Hold Point. Annotations on `P22-BA-09-000-004_C_ITP_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The Inspection and Test Plan does not state that the RO pressure vessels are fabricated and tested to ASME Section X without code stamp, which is the negotiated waiver basis; row 2.2 reads only Manufacture to ASME X, and the Consolidated Comment Sheet reply (witness point added, testing pressure added) never declares the stamp position, so the document that governs acceptance and the 40 percent payment milestone is silent on the central concession |
| OBS-02 | MAJOR | The RO Vessel hydrostatic test (row 2.2) is coded W (Witness) for ADASA, where the activity may proceed if ADASA is absent, while the high-pressure system hydrostatic test (row 5.2) is coded H (Hold Point); under a waiver that substitutes the stamp for a documented basis with a witness, the vessel test is the most critical and should be a Hold Point consistent with row 5.2 |
| NOTE-01 | NOTE | The waiver basis is captured for the first time in this revision — row 2.2 (1,800 psi x 1.1 vessel test with ADASA Witness and a testing report), row 2.4 (PMI of Super Duplex, PREN greater than 40), and rows 7.6 and 8.3 (production and test dossier, the latter a Hold Point) — materially closing the Transmittal N19 and Transmittal N22 carry-forward; the ASME stamp remains waived and is not reopened |

**Action to issue at IFC Rev 0 — no new Inspection and Test Plan revision required:**
1. In row 2.2 (Acceptance Criteria), add an explicit note that the RO pressure vessels are fabricated and tested to ASME Section X without code stamp, per the ADASA waiver of 02-Jun-2026, with the hydrostatic test at 1,800 psi x 1.1 witnessed by ADASA at the vendor and the production and test dossier per rows 7.6 and 8.3 (OBS-01).
2. Raise the RO Vessel hydrostatic test (row 2.2) from Witness (W) to Hold Point (H), consistent with the high-pressure system test in row 5.2, so the vessel test is not released without ADASA's presence and written approval (OBS-02).

ADASA accepts the Inspection and Test Plan as noted on the basis that these two edits are folded into the Rev 0 issue and the matrix structure is unchanged; full closure of the fabrication carry-forward also depends on the RO Vessel Hydrostatic Test Procedure being corrected (Section 2.2).

---

### 2.2 RO Vessel Hydrostatic Test Procedure Rev A — P22-BA-09-000-009

**Response Code: 3 — To be revised**

**Status.** The procedure that supports the Inspection and Test Plan undercuts it on the single most critical fabrication test. The body fixes the test pressure only as a generic rule (1.1 times design pressure for ASME certified, 1.43 times for CE certified) without committing the project value, and the embedded vendor report form carries a hydrostatic test value of 45.5 bar (about 660 psi), roughly a third of the 1,980 psi (about 136.5 bar) that 1,800 psi x 1.1 requires and that the Inspection and Test Plan declares. The procedure also lacks a witness and notification section and traceable calibrated instrumentation, both of which the agreed waiver and the companion HP and LP procedure provide for. Annotations on `P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | The test pressure is not stated as a binding project value in the procedure body (only the generic 1.1x ASME / 1.43x CE rule), and the embedded vendor report form carries 45.5 bar (about 660 psi), inconsistent with the 1,800 psi x 1.1 (about 136.5 bar) the Inspection and Test Plan row 2.2 and the waiver require; the CE 1.43x branch also opens a certification path other than the agreed ASME-without-stamp basis |
| OBS-02 | MAJOR | The procedure does not declare the ADASA witness and prior notification agreed as the counterpart of the waiver, and its instrumentation is limited to a single calibrated pressure gauge without certificate review before the test or a stated class and uncertainty, where the companion HP and LP procedure requires the QC Engineer to review the calibration certificate and at least two gauges |
| OBS-03 | MINOR | The hold time is stated as at least one minute for an FRP vessel where the HP and LP procedure holds 30 minutes, and the procedure cites ASME Section X article RT-5 without transcribing the hold time and the admissible pressure-drop criterion; declare the hold time and acceptance criterion with their RT-5 value |
| OBS-04 | MINOR | The ADASA-coded cover is Rev A dated 12-Jun-2026 while the embedded vendor procedure sheet is its own Rev 0 dated 09-10-2025 with a separate signatory chain, and the relationship between the wrapper revision and the embedded vendor-document revision is not declared, so a future change to the vendor sheet would not visibly drive the wrapper revision |

**Action — re-issue as Rev B:** state the project test value by model in the procedure body and on the report form — BPV-8-1800-SP-7 at 1,800 psi x 1.1 = 1,980 psi (about 136.5 bar) and BPV-8-1200-SP-7 at 1,200 psi x 1.1 = 1,320 psi (about 91 bar) — deleting the 45.5 bar default and the unused CE 1.43x branch, so the figure reads identically here and in Inspection and Test Plan row 2.2 (OBS-01). Add a notification and witness section aligned with the one-month notice of the inspection plan and specify traceable calibrated instrumentation reviewed before the test (OBS-02). Declare the hold time and acceptance criterion per ASME Section X RT-5 (OBS-03), and tie the ADASA wrapper revision to the embedded vendor procedure number and revision (OBS-04).

---

### 2.3 HP and LP Pressure Test Procedure Rev A — P22-BA-09-000-010

**Response Code: 3 — To be revised**

**Status.** The methodology is complete (low-point fill, high-point vent, stepped pressurization, 30-minute hold), but the procedure states no binding numeric test pressure, repeating the generic the required test pressure where the Inspection and Test Plan fixes the values (high-pressure system 135 bar = 1.5 times 90 bar; low-pressure 7.5 bar). The high-pressure design-pressure basis is also unreconciled — the Inspection and Test Plan uses 90 bar while the Technical Specification cites up to 120 bar for high-pressure piping. A test procedure without its binding test pressure cannot be executed or witnessed against an objective value. Annotations on `P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The procedure does not write any numeric test pressure or the ASME B31.3 factor applied, repeating the required test pressure generically; declare the design pressure per subsystem (high-pressure Super Duplex and low-pressure PVC), the B31.3 factor (1.5 times design), and the resulting test pressure in bar matching the Inspection and Test Plan (135 bar and 7.5 bar), and reconcile the high-pressure design pressure (90 bar in the Inspection and Test Plan versus up to 120 bar in the Technical Specification) citing the source of the adopted value |
| OBS-02 | MINOR | The internal step numbering breaks in the pneumatic-test section: after step 5.6.16 the numbering reverts to 5.5.17 and 5.5.18 (duplicating identifiers in the hydrostatic section), and step 5.6.5 is missing; renumber the section consecutively and remove the duplicates |

**Action — re-issue as Rev B:** declare the design pressure per subsystem, the ASME B31.3 factor, and the resulting numeric test pressure for each subsystem, coincident with the Inspection and Test Plan, and reconcile the high-pressure design pressure against the Technical Specification with a cited source (OBS-01); renumber the pneumatic-test section consecutively without duplicates or gaps (OBS-02).

---

### 2.4 NDE Plan Rev B — P22-BA-09-000-005

**Response Code: 3 — To be revised**

**Status.** The coverage table is project-specific and consistent with the Technical Specification (100 percent VT, 100 percent PT on root and end pass, 10 percent RT on butt welds, 10 percent PMI), so the content is sound. It does not close because the governing code editions are still left as placeholders — the same point ADASA raised on Rev A, which the Rev B reply did not resolve — and the plan mixes a structural code (AWS D1.1) and a thermoplastic code (DVS 2202-1) with the high-pressure Super Duplex circuit that ASME B31.3 governs, without mapping each code to its joints. Annotations on `P22-BA-09-000-005_B_NDE_Plan_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Every code in the references (ASME Section V Article 9, ASME Section II, ASME B31.3, AWS D1.1, DVS 2202-1) is listed as Applicable Edition/Addenda without a controlling year; the inspection plan basis rejects generic references and requires a fixed document, revision and edition, and the Rev A comment on this point was not closed in Rev B |
| OBS-02 | MINOR | The acceptance-criteria section mixes AWS D1.1 (structural) and DVS 2202-1 (thermoplastic) with the high-pressure Super Duplex circuit governed by ASME B31.3 without declaring which code applies to which joint; the UT column reads High Pressure Pipe Thicknesses, which is a baseline thickness measurement, not a weld-NDE extent; and the B31.3 acceptance paragraph and fluid-service category should be cited |

**Action — re-issue as Rev C:** state the governing year and addenda for each referenced code (OBS-01); declare explicitly that the high-pressure Super Duplex circuit is evaluated to ASME B31.3, reserving AWS D1.1 for the support structure and DVS 2202-1 for the low-pressure thermoplastic joints with the joints each governs identified, clarify that the UT thickness column is the baseline measurement and state any weld-UT extent as a percentage, and cite the B31.3 acceptance paragraph with the fluid-service category (OBS-02).

---

### 2.5 Painting Procedure Rev A — P22-BA-09-000-011

**Response Code: 3 — To be revised**

**Status.** The layer architecture (zinc epoxy 80 micrometres, high-build epoxy 200 micrometres, aliphatic polyurethane 75 micrometres, total 355 micrometres) and the Sa 2½ surface preparation match the Technical Specification and the Painting Specifications Rev B approved at Transmittal N11, so the scheme concept is sound. It does not close because the procedure substitutes a Jotun system for the approved Sherwin-Williams system without a documented technical-equivalence justification, the marine C5-M durability is not demonstrated (the primer is certified only for C5-I), and the anchor profile is internally inconsistent and below the Technical Specification. Annotations on `P22-BA-09-000-011_A_Painting_Procedure_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The procedure proposes a Jotun system (Barrier 80, Penguard Midcoat, Hardtop XP) in place of the Sherwin-Williams system (Zinc Clad II, Macropoxy 646, Acrolon 218 HS) fixed in the Painting Specifications Rev B approved Code 1 at Transmittal N11; the architecture and thicknesses match, but the brand substitution carries no product-to-product equivalence justification, and the Technical Specification conditions any equivalent on ADASA approval, leaving two project documents contradicting each other on the coating products |
| OBS-02 | MAJOR | The marine durability is not demonstrated: the procedure body does not declare the target corrosivity category or durability level, and the Barrier 80 primer data sheet certifies high durability in category C5-I (industrial), not C5-M (marine), where the coastal Taltal site and the Technical Specification require a system qualified for C5-M with high durability |
| OBS-03 | MAJOR | The anchor profile is contradictory within the document and below the Technical Specification: the body fixes 50 to 80 micrometres while the inspection form fixes 40 to 75 micrometres, and the 40 micrometre lower bound is below the 50 micrometre minimum of the Technical Specification, so the inspection form can record a non-conforming profile as conforming |
| OBS-04 | MINOR | The finish-coat colour RAL 5012 (Luminous Blue) required by the Technical Specification and confirmed in the Painting Specifications Rev B is not stated in the painting scheme or the inspection form (the Colour field is left blank) |
| OBS-05 | MINOR | The application scope is generic (minimum requirements for surface blasting and painting of the skids) and does not limit the coating to the ASTM A-36 structural carbon steel nor explicitly exclude stainless steel and non-metallic surfaces (FRP, HDPE), which are not painted |
| OBS-06 | MINOR | The quality control does not include an adhesion test (pull-off per ISO 4624 or cross-cut per ISO 2409), does not pre-load the nominal DFT per coat and total in the inspection form (left as xxx micrometres), does not cite ISO 2808 as the DFT measurement method, and does not list SSPC-SP10 / NACE No. 2 (equivalent to Sa 2½) among the references the Technical Specification cites |
| NOTE-01 | NOTE | The layer architecture (80 / 200 / 75 = 355 micrometres) and the Sa 2½ preparation match the Technical Specification and the approved Painting Specifications Rev B; the rejection concerns the brand equivalence, the C5-M durability, the colour and the anchor profile, not the scheme concept, so the procedure is recoverable by revision without redesigning the system |

**Action — re-issue as Rev B:** attach a product-to-product equivalence table (generic chemistry, percent solids by volume, ISO 12944-6 classification and DFT range) and obtain ADASA's approval of the Jotun system, or adopt the Sherwin-Williams system of the Painting Specifications Rev B, reconciling the two documents (OBS-01); declare the target corrosivity category C5-M (or CX) and high durability and provide the ISO 12944-6 evidence for the complete system (OBS-02); unify the anchor profile to a single range with a lower bound of at least 50 micrometres (OBS-03); state the RAL 5012 finish colour (OBS-04); bound the scope to the ASTM A-36 carbon steel and exclude stainless steel and non-metallic surfaces (OBS-05); and complete the quality control with an adhesion test, nominal DFT per coat, and the ISO 2808 and SSPC-SP10 references (OBS-06).

---

### 2.6 Instrument Location Layout Rev C — P22-DWG-09-008-001

**Response Code: 3 — To be revised**

**Status.** The re-issue carries real content changes but not a new revision letter, and its geometry is tied to a superseded upstream layout. The drawing's own Consolidated Comment Sheet states it revised the descriptions of items 8, 9, 31 and 32 (the HP and CIP pump temperature sensors) and relocated the CIP in line with the Equipment Layout Rev B, yet the revision block still reads C with the April date dispositioned at Transmittal N15. The instrument positions are aligned to Equipment Layout Rev B, which has since advanced to Rev C and is open at Code 3 because the RO Cartridge Filter is still drawn horizontal. Annotations on `P22-DWG-09-008-001_C_Instrument_Location_Layout_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The drawing was re-issued on 16-Jun-2026 with content changes (item 8, 9, 31 and 32 descriptions and the CIP relocation) but the revision letter remains C with no new revision-history row and an empty ECN column, so two physically different drawings now share the identifier Rev C and break the revision trail (the prior Rev C is the one accepted-as-configured at Transmittal N15) |
| OBS-02 | MAJOR | The instrument positions are aligned to the Equipment Layout Rev B, which has advanced to Rev C and is open at Code 3 (RO Cartridge Filter still horizontal against its vertical datasheet); BW Water's own reply concedes the layout cannot be issued for construction until the upstream layouts are approved with no comment, a condition not met, so approving it now would lock instrument positions to a geometry ADASA has not accepted |
| OBS-03 | MINOR | The front title-block code reads P22-DWG-09-008-01 with a two-digit correlative, where the file name and the sheet cajetin correctly use the three-digit P22-DWG-09-008-001; the code must be identical across every block |
| OBS-04 | MINOR | The Rev C date is inconsistent — the front header dates Revision C 16/6/2026 while the revision-history block on the sheets dates Revision C in April; a single revision cannot carry two issue dates |

**Action — re-issue as Rev D:** add a Rev D row to the revision history with date, ECN, a description naming the item 8, 9, 31 and 32 edits and the CIP relocation, and the responsible initials, rather than re-using the C identifier for changed content (OBS-01); re-align all instrument positions to the approved Equipment Layout revision once the Equipment Layout (Section 2.6 of Transmittal N22) is resolved to Code 1 or 2 with the RO Cartridge Filter shown vertical (OBS-02); correct the front title-block code to the three-digit correlative (OBS-03); and set one consistent issue date in the header and the new revision-history row, leaving the historical Rev C date unchanged (OBS-04).

---

### 2.7 UHPRO Structural Design Criteria Rev A — P22-CD-09-005-003

**Response Code: 3 — To be revised**

**Status.** The design approach is methodologically sound (NCh 3171 base load combinations plus the NCh 2369 seismic combinations) and the seismic parameter values are consistent with NCh 2369 Of.2003 — the edition the Technical Specification establishes and under which this engineering was contracted. The criteria must nonetheless be re-issued because they state no lifting (transport and erection) load case or lifting-point and yoke design criteria, which the module Technical Specification requires as a deliverable. In addition, the seismic standard is cited inconsistently — the parameter table and the load combinations cite a non-existent NCh 2369:2009 while the code list correctly cites Of.2003 — and the revision identity is contradictory. Annotations on `P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The seismic-standard citation is inconsistent and partly non-existent: the parameter table (Seismic Zone, importance factor, response-reduction factor, effective acceleration, soil type, damping) and the load combinations cite NCh 2369:2009 — an edition that does not exist — while the code list correctly cites NCh 2369 Of.2003, the edition the Technical Specification — Seismic Conditions establishes for this project. Correct every NCh 2369:2009 citation to NCh 2369 Of.2003 so the seismic basis is internally consistent (the parameter values are already consistent with Of.2003) |
| OBS-02 | MAJOR | For allowable-stress design the governing seismic load combinations are those of NCh 2369 — the document's combinations 11 and 12 (D + aL + SO + SA ± Eh ± Ev and D + SA ± Eh ± Ev, with the allowable-stress increase NCh 2369 permits under seismic) — which it draws from clause 4.5; the base combinations 1 to 10 are taken from NCh 3171. Confirm that the NCh 2369 Of.2003 clause 4.5 combinations govern the seismic ASD verification (the generic NCh 3171 combinations do not replace them) and correct the edition citation from the non-existent 2009 to Of.2003 |
| OBS-03 | MAJOR | The criteria omit the lifting (transport and erection) load case and the lifting-point and yoke design criteria; the module Technical Specification — Final Documentation requires the module lifting calculation, the lifting plan showing the lifting points and weights, and the lifting yoke design and drawing (the lifting design is BW Water's scope; the crane and lifting equipment for the on-site installation are ADASA's scope). Add the lifting and handling load case and the lifting-point and yoke design basis, including the dynamic amplification factor for the lifting maneuver, so the required lifting deliverables have an approved design basis |
| OBS-04 | MINOR | The revision identity is inconsistent: the ADASA code block labels the document Rev A dated 17-Jun-2026 while the internal block and every page footer label it Rev 00 / FOR APPROVAL dated 16-Jun-2026; under the codification standard Rev A and Rev 0 denote opposite lifecycle stages (internal review versus issued for construction), so the labels must be reconciled |
| OBS-05 | MINOR | Soil Type E (the softest class, highest seismic demand) is adopted in the parameter table without a cited site geotechnical basis; state it explicitly as a conservative envelope pending the project geotechnical report, consistent with the anchor-bolt validation note already in the design approach |
| OBS-06 | MINOR | The design seismic weight P in the base-shear equation is not declared and the established module operating weight is not cross-referenced; declare the operating weight used for P so the seismic design weight is traceable to the operating weight the Technical Specification mandates |
| OBS-07 | MINOR | The minimum design wind pressures are written in N/m (force per length) where the correct unit is N/m2 (pressure); correct the units and confirm the NCh 432 edition cited |
| NOTE-01 | NOTE | The reinforced-concrete grade and standard label (NCh1170 / G25, f'c = 24.5 MPa) is to be confirmed (the Chilean concrete standard is normally NCh 170 and a G25 grade is about 25 MPa); the concrete applies to the foundations in the civil scope outside this skid package, so the impact on the steel-skid criteria is marginal |

**Action — re-issue as Rev B:** add the lifting and handling load case and the lifting-point and yoke design criteria — BW Water's design scope, the crane and lifting equipment being ADASA's — so the required lifting deliverables (lifting calculation, lifting plan and yoke design and drawing) have an approved design basis (OBS-03); correct every NCh 2369:2009 citation to NCh 2369 Of.2003 so the seismic basis matches the code list and the Technical Specification (OBS-01); confirm the NCh 2369 Of.2003 clause 4.5 combinations govern the seismic allowable-stress verification (OBS-02); reconcile the revision identity (OBS-04); state Soil Type E as a conservative envelope pending the geotechnical report (OBS-05); declare the design seismic weight P (OBS-06); correct the wind-pressure units to N/m2 and confirm the NCh 432 edition (OBS-07); and confirm the concrete standard label and grade for the foundation scope (NOTE-01).

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

This submittal delivered E51 and E52 only. The status below reflects what those packages resolved and what remains tracked from Transmittal N22 and earlier.

**Addressed in this transmittal (moved into Section 2):**

- Transmittal N19 Section 2.10 / Transmittal N22 Section 3 (Inspection and Test Plan and vessel test procedures — the oldest open fabrication item) — materially closed by the Inspection and Test Plan Rev C, which now carries the vessel hydrostatic test at 1,800 psi x 1.1, the ADASA witness and the production and test dossier Hold Points (Section 2.1 NOTE-01). Full closure remains subject to two Rev 0 edits in the Inspection and Test Plan (declare the no-code-stamp basis; raise the vessel test from Witness to Hold Point — Section 2.1) and to the correction of the RO Vessel Hydrostatic Test Procedure (Section 2.2). The ASME stamp remains waived and is not reopened.

**Open from previous transmittals — the three most serious** (minor open items remain tracked in the Master Deliverable Register):

| Origin TM | Document | Observation | Status |
|-----------|----------|-------------|--------|
| TM N22 Section 2.1 | Plant Control Philosophy children: Operating Sequence Charts (P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) and Control Matrix, with the I/O List Rev 2 and the rest of the control cascade | The operative numerical control logic remains in child documents not delivered | OPEN — not delivered with this submittal; the sixth cycle with that logic outside the package; closure of the control cascade waits on these three documents |
| TM N20 Section 2.6 | PLC-LCP Outline Panel Drawing (P22-CD-09-008-001) | Enclosure contradiction (sheet steel / IP55 versus SS316L / NEMA 4X-IP66) — fabrication gate | OPEN — Outline Rev B with the aligned Panel Specification Sheet, actual panel weight and reconciled cooling awaited; the expedited release path of the response of 10-Jun applies |
| TM N22 Section 2.2 | Equipment Layout (P22-DWG-09-005-003) | RO Cartridge Filter still drawn horizontal against its own vertical datasheet | OPEN — to re-issue as Rev D with the RO Cartridge Filter vertical; this also gates the Instrument Location Layout, whose geometry is aligned to the superseded Equipment Layout Rev B (Section 2.6 OBS-02) |

**Open deliverables and procedural items (not document defects):**

- Grounding Point and Power Panel Location Layout Rev F — due 17-Jun-2026; not received with this submittal; tracked.
- FAT and SAT comparison table requested on 01-Jun and 09-Jun (due 15-Jun-2026) — the FAT scope is now captured in the Inspection and Test Plan (item 7), but the standalone FAT and SAT comparison table is still tracked separately.
- Inspection and Test Plan Rev 0 conditions and RO Vessel Hydrostatic Test Procedure alignment — the two Rev 0 edits of Section 2.1 and the correction of the test procedure of Section 2.2 close the fabrication carry-forward in full.

---

## 4. ATTACHMENTS

| Document | Verdict | Annotated File | Annotations |
|----------|---------|---------------|-------------|
| Inspection and Test Plan Rev C | Code 2 | P22-BA-09-000-004_C_ITP_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |
| RO Vessel Hydrostatic Test Procedure Rev A | Code 3 | P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04 |
| HP and LP Pressure Test Procedure Rev A | Code 3 | P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf | OBS-01, OBS-02 |
| NDE Plan Rev B | Code 3 | P22-BA-09-000-005_B_NDE_Plan_CC_ADASA.pdf | OBS-01, OBS-02 |
| Painting Procedure Rev A | Code 3 | P22-BA-09-000-011_A_Painting_Procedure_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, OBS-06, NOTE-01 |
| Instrument Location Layout Rev C | Code 3 | P22-DWG-09-008-001_C_Instrument_Location_Layout_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04 |
| UHPRO Structural Design Criteria Rev A | Code 3 | P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, OBS-06, OBS-07, NOTE-01 |

All seven documents carry open observations or notes and are returned with annotated PDFs (6 Code 3 + 1 Code 2). No document is Code 1 — Approved in this transmittal.

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-BA-09-000-004 | Inspection and Test Plan | C | 2 — Approved as Noted |
| P22-BA-09-000-009 | RO Vessel Hydrostatic Test Procedure | A | 3 — To Be Revised |
| P22-BA-09-000-010 | HP and LP Pressure Test Procedure | A | 3 — To Be Revised |
| P22-BA-09-000-005 | NDE Plan | B | 3 — To Be Revised |
| P22-BA-09-000-011 | Painting Procedure | A | 3 — To Be Revised |
| P22-DWG-09-008-001 | Instrument Location Layout | C | 3 — To Be Revised |
| P22-CD-09-005-003 | UHPRO Structural Design Criteria | A | 3 — To Be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Tally: 0 Code 1, 1 Code 2, 6 Code 3. The RO Vessel Hydrostatic Test Procedure fixes the verdict: the Inspection and Test Plan correctly captures the agreed waiver basis and materially closes the package's oldest open fabrication item, but the supporting test procedure states no binding test pressure and carries a 45.5 bar value against the required 1,980 psi, so the witness point and the dossier the stamp waiver was traded for rest on an inconsistent figure. The Painting Procedure substitutes the approved coating system without an equivalence justification and does not demonstrate marine durability, and the Instrument Location Layout re-uses the Rev C identifier for changed content while aligned to an Equipment Layout open at Code 3. The Structural Design Criteria omits the lifting load case and design criteria the module Technical Specification requires and must align its seismic citation to NCh 2369 Of.2003 (the parameter table cites a non-existent 2009 edition), which calls for a new revision. The Inspection and Test Plan is Approved as Noted, with its edits folded into the Rev 0 issue. Documents not appearing in this response are unaffected by this transmittal.
