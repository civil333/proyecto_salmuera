---
second_brain: capture
type: transmittal
project: salmuera-taltal
date: 2026-07-06
---

# TECHNICAL REVIEW TRANSMITTAL N26 — SECOND STAGE RO BRINE MODULE

**Code:** P22-TM-09-000-026-0 | **Date:** 06-Jul-2026 | **Submittals:** 25007-0057 (E57) to 25007-0062 (E62)

## 1. Executive Summary

**TRANSMITTAL VERDICT: 3 — To Be Revised.** Nine documents (submittals 25007-0057 through 25007-0062). Tally: 2 Code 1, 3 Code 2, 4 Code 3. The verdict rests on the fabrication test procedures and the structural anchoring. The RO Vessel Hydrostatic Test Procedure Rev B — the test for which the ASME code stamp was waived — still declares no binding test pressure, and its embedded form still prints 45.5 bar against the 1,980 psi that the Inspection and Test Plan and the 02-Jun-2026 waiver require; the HP and LP Pressure Test Procedure Rev B adds the ASME B31.3 factor but still omits the numeric test pressure and leaves the high-pressure design value unreconciled. The UHPRO Structural Calculation Report Rev A omits the anchorage of the main process equipment that carries the largest seismic mass, and the GA of the Antiscalant Dosing Tank Rev B still defers its NCh 2369 anchor loads. Against that, the fabrication package advances: the Inspection and Test Plan Rev 0 incorporates both edits required at Transmittal N23 and issues for construction, and the NDE Plan Rev C closes its governing-code and joint-mapping observations — both Approved. The Datasheet of PLC and HMI Panel Component Rev C closes the HART, RTD and title-block items from Transmittal N21 and is Approved as Noted on an internal document-code inconsistency; the GA of the CIP Flushing Tank Rev A and the GA of the Antiscalant Dosing Pump Skid Rev B are Approved as Noted on minor items. Per-document codes and required actions are in Section 2; open and overdue items from previous transmittals are in Section 3.

## 2. Observations by Document

### 2.1 Inspection and Test Plan (ITP) Rev 0 — P22-BA-09-000-004

**Response Code: 1 — Approved**

**Status.** Closes the Transmittal N23 cycle. Rev 0 is the construction issue and incorporates both edits Transmittal N23 required, with no intermediate revision. Row 2.2 now reads "manufacture to ASME Section X, without code stamp" and keeps the binding vessel test pressures (1,800 psi x 1.1 and 1,200 psi x 1.1), and the RO vessel hydrostatic test is raised from Witness to Hold Point on ADASA's responsibility column, consistent with the high-pressure hydrostatic row. ASME Section X is correct for the FRP vessels and the stamp remains waived. No annotated PDF.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | NOTE | Row 2.2 declares "without code stamp" and carries the binding pressures, closing the substance of the Transmittal N23 observation. The cell does not yet cite its authorising basis ("per the ADASA waiver of 02-Jun-2026"); explicit citation strengthens the audit trail for the document that governs the 40% payment milestone (BAE Clause 31), but its absence does not gate the construction issue. |
| NOTE-02 | NOTE | Closure record: the RO vessel hydrostatic test is now a Hold Point on ADASA's column, aligned with the high-pressure hydrostatic row; the vessel test is no longer released without ADASA presence and written approval. |
| NOTE-03 | NOTE | Cross-check: the binding test pressure sits correctly on ITP row 2.2 (1,980 psi), but the RO Vessel Hydrostatic Test Procedure body does not yet carry it (Section 2.3). That gap is a deliverable on the procedure, not on this plan; the ITP is the governing source of the test pressure. |
| NOTE-04 | NOTE | Housekeeping: reconcile the internal issue dates (cover 30/06, matrix header 29-Jun) and correct the recurring matrix typos at a convenient issue. |

**Action: none on this plan — accepted; issue directly at IFC Rev 0,** folding the housekeeping items. The binding-pressure alignment on the RO Vessel Hydrostatic Test Procedure is tracked in Section 2.3 and Section 3.

### 2.2 NDE Plan Rev C — P22-BA-09-000-005

**Response Code: 1 — Approved**

**Status.** Closes the Transmittal N23 cycle (third review cycle). Both Rev B observations are closed: the reference section now fixes the governing code editions (ASME Section V-2025, ASME Section II-2025, ASME B31.3-2024, AWS D1.1-2025, DVS 2202-1), and the acceptance-criteria section maps each code to its joint family — ASME B31.3 to the Super Duplex high-pressure circuit (Normal Fluid Service, paragraph 341.3.2), AWS D1.1 to supports and structure, DVS 2202-1 to the low-pressure thermoplastic piping — with the UT column clarified as a thickness verification. The RO pressure-vessel scope from the original Transmittal N20 comment correctly sits with the Inspection and Test Plan and the RO Vessel Hydrostatic Test Procedure, not here. Coverage matches the Technical Specification. No annotated PDF.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | NOTE | Closure of the Rev B major observation: the governing code editions are now specified, with no remaining placeholders. |
| NOTE-02 | NOTE | Closure of the Rev B minor observation: the joint-to-code mapping, the UT-column clarification and the ASME B31.3 acceptance paragraph are incorporated. |
| NOTE-03 | NOTE | Informative: the DVS 2202-1 mapping to the low-pressure thermoplastic line is consistent with the Technical Specification (PVC low-pressure piping evaluated by visual testing where there is no fusion weld). |

**Action: none on this plan — accepted; issue directly at IFC Rev 0.**

### 2.3 RO Vessel Hydrostatic Test Procedure Rev B — P22-BA-09-000-009

**Response Code: 3 — To Be Revised**

**Status.** Does not close the Transmittal N23 driver. The procedure body still carries only the generic rule ("1.43 times design for CE, 1.1 times design for ASME") and the embedded Protec report form still prints 45.5 bar (about 660 psi) as the hydrostatic test — roughly one third of the 1,980 psi (1,800 psi x 1.1) that ITP row 2.2 and the 02-Jun-2026 waiver require. The witness and notification part is reasonably covered by reference to the Inspection and Test Plan (now a Hold Point), but the traceable instrumentation was not incorporated. This is the test for which the ASME stamp was waived; it must fix the binding pressure before fabrication. Annotations on P22-BA-09-000-009_B_RO_Vessel_Hydrostatic_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | The body states no binding test pressure and the embedded Protec form still prints 45.5 bar against the required 1,980 psi (Model BPV-8-1800-SP-7) and 1,320 psi (Model BPV-8-1200-SP-7); the CE 1.43-times branch remains. A shop following this document literally could test at 45.5 bar and record a pass. The requirement is the Technical Specification — Pressure Vessels (1,800 psi, ASME Section X), Inspection and Test Plan row 2.2, and the 02-Jun-2026 stamp waiver; the Transmittal N23 observation is not closed. |
| OBS-02 | MAJOR | The procedure still lists a single calibrated pressure gauge and no calibration-certificate review, against the two-gauge, certificate-review traceability its own HP and LP Pressure Test Procedure applies. The witness and notification requirement is met by reference to the Inspection and Test Plan Hold Point. |
| OBS-03 | MINOR | The embedded Protec procedure keeps "Revision: 0" on one index page after being renumbered to Revision B on the others — an internal revision inconsistency. |
| NOTE-01 | NOTE | The RT-5 hold time and the acceptance criterion are declared (ASME Section X RT-5, one-minute minimum, reject above a 10% pressure drop); this minor item folds into the next revision. |

**Action — re-issue as Rev C:** state the binding project test pressure by model (1,980 psi for BPV-8-1800-SP-7; 1,320 psi for BPV-8-1200-SP-7) in both the procedure body and the report form, remove the 45.5 bar default and the CE 1.43-times branch, and add the two-gauge, calibration-certificate-review instrumentation.

### 2.4 HP and LP Pressure Test Procedure Rev B — P22-BA-09-000-010

**Response Code: 3 — To Be Revised**

**Status.** Partially closes the Transmittal N23 observation. Rev B adds the correct ASME B31.3 factor (1.5 times for the hydrostatic step, 1.1 times for the pneumatic step), but the body still writes no numeric test pressure — both steps refer to the "design pressure in the approved line list" — and the high-pressure design value stays unreconciled (90 bar per the Inspection and Test Plan versus up to 120 bar per the Technical Specification), so the resulting test pressure is indeterminate between 135 and 180 bar on the Super Duplex high-pressure circuit. The step-numbering reversion was corrected but two gaps remain. Annotations on P22-BA-09-000-010_B_HP_LP_Pressure_Test_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The body still omits the numeric test pressure (135 bar high pressure and 7.5 bar low pressure fixed by the Inspection and Test Plan) and does not reconcile the 90-versus-120-bar high-pressure design value with a cited source; because the test pressure is 1.5 times the design pressure, the result stays indeterminate and a shop cannot run to a single binding pressure from this procedure. The requirement is the Technical Offer Rev.1 — Inspection and Test Plan, the Technical Specification — High-Pressure Piping, and ASME B31.3. |
| OBS-02 | MINOR | The pneumatic-section reversion is corrected, but step 5.6.5 is still missing (5.6.4 jumps to 5.6.6) and subsection 5.7.2 (Weld Joints) skips 5.7.2.2 — the same documentation-hygiene defect the reply reported as resolved. |
| NOTE-01 | NOTE | The Pressure Test Report form is not included in this delivery; attach it at the next submittal so any pre-printed pressure can be checked against 135 bar high pressure and 7.5 bar low pressure. |

**Action — re-issue as Rev C:** state the design pressure per subsystem with a cited source (resolving the 90-versus-120-bar high-pressure conflict), write the resulting numeric test pressure (135 bar high pressure and 7.5 bar low pressure) in the body, and close the step-numbering gaps at 5.6.5 and 5.7.2.2.

### 2.5 Datasheet of PLC and HMI Panel Component Rev C — P22-ET-09-008-01

**Response Code: 2 — Approved as Noted**

**Status.** Closes the three Transmittal N21 items. The HART acquisition path is now provided at the instrument level — both the 5069-IF8 and the added 5069-IY4 carry the external 250-ohm resistor note for handheld HART access, satisfying the 4-20 mA plus HART instrumentation requirement without central HART decoding (the over-reach corrected at Transmittal N24 is not reopened); the 5069-IY4 RTD module for the motor Pt-100 channels is now included; and the title-block typo is corrected in the body. The remaining item is the document code itself. Annotations on P22-ET-09-008-01_C_DS_PLC_HMI_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| NOTE-01 | NOTE | The document identifies itself inconsistently: the cover and most component headers read "P22-ET-09-008-01" (two-digit sequential) while the added analog-module page and the embedded comment sheet read "P22-ET-09-008-001" (three-digit), which is the code carried in the deliverable register and in Rev B. The codification convention uses the three-digit sequential; this is the item that requires touching the datasheet itself. |
| NOTE-02 | NOTE | As a component datasheet, the 5069-IY4 page states the module type once without a quantity; the eight motor Pt-100 channels depend on two 5069-IY4 modules per the approved Datasheet of the Local Control Panel Rev 1. Confirm at issue that the LCP Datasheet governs the quantity. |

**Action to issue at IFC Rev 0 — no new revision required:** align the document code to "P22-ET-09-008-001" on the cover and all component headers, removing the internal inconsistency (NOTE-01), and confirm the RTD-module quantity reference (NOTE-02). The three instrumentation items from Transmittal N21 are closed.

### 2.6 UHPRO Structural Calculation Report Rev A — P22-CD-09-005-001

**Response Code: 3 — To Be Revised**

**Status.** This is the seismic calculation report tracked as a Transmittal N25 deliverable, and it confirms the frame and lifting basis of the approved UHPRO Structural Design Criteria Rev B — the seismic parameters (NCh 2369 Of.2003, Zone 3, R = 3.0, I = 1.0, A0 = 0.40 g), the clause 4.5 combinations, and the lifting case (API RP 2A-WSD factors 1.35 and 2.0). The blocking item is the anchorage scope. Annotations on P22-CD-09-005-001_A_UHPRO_Structural_Calc_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | CRITICAL | The Bolt Design at the Base checks eight ancillary units (container module, CIP tank, CIP pump, CIP cartridge filter, dosing tank, dosing pump and the two panels) but omits the main process equipment — the RO high-pressure pump BH-09-001, the turbochargers SIP-09-001 and SIP-09-002, the RO cartridge filter FIL-09-001 and the RO pressure vessels BOI-09-001 and BOI-09-002 (4,160 kg, the heaviest process item) — all included as seismic mass in the model. The Technical Specification — Seismic Conditions requires these anchors designed for NCh 2369, Zone 3; their integrity is not verifiable unless it is governed by, and documented through, the skid-frame anchorage. |
| OBS-02 | MINOR | Design Results does not consolidate the numerical design seismic weight (operating), the global base shear or the NCh 2369 base-shear check; those values live only inside the seismic-load attachment. The numerical design seismic weight was the tracked deliverable. |
| OBS-03 | MINOR | In the STAAD load-combination list the two minimum-gravity cases 226 and 227 duplicate 224 and 225 (both in the Z direction), while the X-direction minimum-gravity seismic case (0.9(DS+DO+FR) + 1.1 EOX +/- 0.3 EV, NCh 2369 clause 4.5) is absent. |
| OBS-04 | MINOR | The skid-frame utilization is shown only as a colour map (Figure 13) without the governing maximum value; state it and confirm it is below 1.0. |
| OBS-05 | MAJOR | The frame material is Corten A (yield 345 MPa) and S275JR (yield 275 MPa); confirm these grades against the material specification of the approved UHPRO Structural Design Criteria Rev B and reconcile with the ASTM A-36 reference of the Technical Specification. Also unify the revision label (cover Rev A versus body "Rev A1") and the total page count. |
| NOTE-01 | NOTE | The container base bolts to the concrete foundation are deferred "to others"; transmit the governing base-bolt tension and shear demands as an interface table for the OOCC foundation design, and clarify that "concrete by others" applies to the container base, not to the equipment-to-skid anchors. |
| NOTE-02 | NOTE | The soil is labelled "Type E" (NCh 433 nomenclature) while NCh 2369 uses Types I to IV; confirm the soil type against the site geotechnical report and the corresponding T-prime and n parameters. |

**Action — re-issue as Rev B:** add the anchor check (or a documented and certified anchorage route) for BH-09-001, SIP-09-001/002, FIL-09-001 and BOI-09-001/002; consolidate the design seismic weight and the base-shear check in Design Results; correct the load-combination matrix; state the skid-frame utilization; reconcile the frame material against the approved Structural Design Criteria and the Technical Specification; and provide the foundation base-bolt interface table (NOTE-01).

### 2.7 GA of CIP Flushing Tank Rev A — P22-DWG-09-005-014

**Response Code: 2 — Approved as Noted**

**Status.** First issue. The tank capacity (6,800 litres), the dimensions and the HDPE body with PVC flanges and EPDM gaskets are consistent with the approved Datasheet of the CIP Tank, the Equipment List and the P&ID, and are compatible with the CIP solution at pH 2 to 12 — the gasket-compatibility concern that governed the CIP Cartridge Filter does not recur here. Two minor items and the seismic-anchor deliverable remain. Annotations on P22-DWG-09-005-014_A_GA_CIP_Flushing_Tank_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MINOR | The general arrangement does not show the equipment tag TK-09-001 that the Datasheet of the CIP Tank and the Equipment List assign to this vessel. |
| OBS-02 | MINOR | The GA nozzle schedule and the approved Datasheet of the CIP Tank disagree on the top opening ("Manhole 21 inch" on the GA versus "Handhole DN300" in the datasheet) and on two side connections (N42 Spare and N97 Temperature Sensor) not in the datasheet schedule; confirm which document governs and reconcile them. |
| NOTE-01 | NOTE | The GA carries the anchor-lug arrangement and the mass properties (270 kg, centre of gravity 1,475 mm), but the NCh 2369 anchor-bolt loads and the seismic qualification of the tank anchorage belong to the Module Seismic Calculation Report; tracked in Section 3, the drawing itself needs no change for this item. |
| NOTE-02 | NOTE | Positive verification: the HDPE body, the PVC flanges and the EPDM gaskets are fit for the CIP service at pH 2 to 12. |

**Action to issue at IFC Rev 0 — no new revision required:** add the equipment tag TK-09-001 (OBS-01) and reconcile the nozzle schedule and top-opening designation with the datasheet (OBS-02). The tank seismic anchor loads are tracked to the Module Seismic Calculation Report (Section 3).

### 2.8 GA of Antiscalant Dosing Tank Rev B — P22-DWG-09-005-015

**Response Code: 3 — To Be Revised**

**Status.** Partially closes Transmittal N10 (OBS-05). The total capacity (335 litres) and the polyethylene body material are now declared and compatible with the antiscalant service, closing two of the four carried items. The blocking items remain: the effective working volume is still not stated, and the NCh 2369 seismic reaction loads and the anchor-bolt pattern are still absent — BW Water's comment sheet defers them ("seismic data will be furnished once the calculations are verified by a Professional Engineer"). Without the anchor loads the OOCC foundation design has no input. Annotations on P22-DWG-09-005-015_B_GA_Antiscalant_Tank_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Detail 3 shows only the anchor-lug geometry; the seismic reaction loads and the anchor-bolt pattern (NCh 2369, Zone 3, operating weight at the centre of gravity) are not on the GA, and BW Water's comment sheet defers them. This carries Transmittal N10 OBS-05 item 4 and leaves the OOCC foundation design without input, unless the reactions are documented in an approved deliverable the GA references. The requirement is the Technical Specification — Seismic Conditions and the Module Seismic Calculation Report. |
| OBS-02 | MINOR | The Notes declare the total capacity (335 litres) but omit the effective working volume (0.27 cubic metres) requested at Transmittal N10; the LEVEL MARKING row is blank. |
| NOTE-01 | NOTE | The Transmittal N10 requirement that the P&ID Rev C annotate TK-09-002 with the 0.34 cubic metre installed volume is an action on the P&ID, not on this GA; tracked separately. |
| NOTE-02 | NOTE | The equipment tag TK-09-002 is not labelled on the GA; add it at re-issue. |

**Action — re-issue as Rev C:** add the anchor-bolt pattern and the NCh 2369 seismic reaction loads (or reference the endorsed Module Seismic Calculation Report), state the effective working volume, and label the equipment tag TK-09-002.

### 2.9 GA of Antiscalant Dosing Pump Skid Rev B — P22-DWG-09-005-011

**Response Code: 2 — Approved as Noted**

**Status.** Materially closes Transmittal N11 (NOTE-06). Rev B delivers the three required items: the anchor-bolt layout (M10, ten bolts, 120 mm embedment, edge and spacing distances) with a dimensioned plan, the seismic reaction forces per NCh 2369, and the equipment mass (100 kg). One internal-consistency item remains, and the endorsed calculation report is an external deliverable. Annotations on P22-DWG-09-005-011_B_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MINOR | The per-bolt forces in the Bolting Embedment detail (Fz = 0.205 kN) are not consistent with the total reaction block (total Fz = 0.2048 kN) divided by the ten-bolt count — an apparent tenfold discrepancy — while the per-bolt Fx (0.102 kN) does equal the total over ten. Label each block explicitly as per-bolt or group-total and reconcile the per-bolt Fz with the endorsed calculation report. |
| NOTE-01 | NOTE | The reaction forces are stated "as per calculation report" and the bolting details are "to be finalized and endorsed"; the endorsed Module Seismic Calculation Report is a separate deliverable tracked in Section 3. |
| NOTE-02 | NOTE | Positive verification: the two dosing pumps BDS-09-001 and BDS-09-002 match the Technical Offer Rev.1, and the polyethylene cabinet and the clear PVC door introduce no material conflict. |

**Action to issue at IFC Rev 0 — no new revision required:** reconcile the per-bolt seismic forces with the total reaction block and label each block (OBS-01). The endorsed Module Seismic Calculation Report is tracked in Section 3.

## 3. Pending Observations from Previous Transmittals

This submittal delivered E57 through E62.

**Addressed in this transmittal:** The Transmittal N23 fabrication package is dispositioned here: the Inspection and Test Plan Rev 0 and the NDE Plan Rev C close (Section 2), while the RO Vessel Hydrostatic Test Procedure and the HP and LP Pressure Test Procedure return at Rev B and remain Code 3. The Transmittal N21 PLC and HMI instrumentation items (HART acquisition, RTD module, title block) close (Section 2.5). The UHPRO Structural Calculation Report, tracked as a Transmittal N25 deliverable, is delivered and reviewed (Section 2.6). The 4-20 mA plus HART acquisition point stays satisfied at the instrument level and is not reopened; the ASME stamp remains waived; the soft-I/O field scheme over Ethernet/IP accepted at Transmittal N20 is not reopened.

**Open from previous transmittals — the most serious:**

| Origin TM | Document | Observation | Status |
|-----------|----------|-------------|--------|
| TM N23 Section 2 | Painting Procedure (P22-BA-09-000-011) | The fourth quality and fabrication procedure did not arrive with this submittal; it must provide the Jotun product-to-product equivalence and ADASA approval, demonstrate C5-M marine durability, and unify the anchor profile to a single range with a 50-micrometre lower bound | OPEN: not delivered; the only Transmittal N23 procedure not resubmitted |
| TM N22 Section 2.1 | Plant Control Philosophy children: Operating Sequence Charts (P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) and Control Matrix | The operative numerical control logic remains in child documents not delivered; it gates the IO List reaching issue for construction | OPEN and overdue: not delivered; the sixth cycle with that logic outside the package |
| TM N20 Section 2.6 | PLC-LCP Outline Panel Drawing (P22-CD-09-008-001) | Enclosure material contradiction — the drawing must re-issue as Rev C with a coherent SS316L specification consistent with the LCP Datasheet | OPEN: not delivered; panel fabrication release remains gated |
| TM N22 Section 2.2 | Equipment Layout (P22-DWG-09-005-003) | RO Cartridge Filter still drawn horizontal against its own vertical datasheet | OPEN: to re-issue as Rev D; no new revision in this delivery |
| TM N4 NOTE-05 | HMI Screenshots (P22-BREAD-09-008-001) | Committed at Transmittal N4, never submitted — the oldest open commitment in the project | OPEN: not delivered |

**Overdue deliverables (today is 06-Jul-2026):**

- Grounding Point and Power Panel Location Layout Rev F — committed for 17-Jun-2026.
- FAT and SAT comparison table — committed for 15-Jun-2026.
- The three mechanical installation-route plans (Maintenance Lifting Points, 3D Model, GA RO HP Pump) — committed for 26-Jun-2026.
- The four items above and the Plant Control Philosophy children were escalated with a consolidated deadline of 03-Jul-2026 (Transmittal N25 cover email), now passed.

**Cross-document checks raised by this transmittal (not defects of the approved documents):**

- Module Seismic Calculation Report: the endorsed report backing the anchor reaction forces of the Antiscalant Dosing Pump Skid, and the NCh 2369 anchor-bolt loads and qualification for the CIP Flushing Tank and the Antiscalant Dosing Tank, all governed by the Structural Calculation Report (Section 2.6, Code 3).
- RO Vessel Hydrostatic Test Procedure: the binding project test pressure (1,980 psi and 1,320 psi) on the procedure body and report form, aligning it with Inspection and Test Plan row 2.2 (Section 2.3).
- Structural foundation interface: the container base-bolt tension and shear demands for the OOCC foundation design (Section 2.6, NOTE-01).

## 4. Attachments

| Document | Verdict | Annotated File | Annotations |
|----------|---------|----------------|-------------|
| Datasheet of PLC and HMI Panel Component Rev C | Code 2 | P22-ET-09-008-01_C_DS_PLC_HMI_CC_ADASA.pdf | NOTE-01, NOTE-02 |
| UHPRO Structural Calculation Report Rev A | Code 3 | P22-CD-09-005-001_A_UHPRO_Structural_Calc_CC_ADASA.pdf | OBS-01 to OBS-05, NOTE-01, NOTE-02 |
| GA of CIP Flushing Tank Rev A | Code 2 | P22-DWG-09-005-014_A_GA_CIP_Flushing_Tank_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01, NOTE-02 |
| GA of Antiscalant Dosing Tank Rev B | Code 3 | P22-DWG-09-005-015_B_GA_Antiscalant_Tank_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01, NOTE-02 |
| RO Vessel Hydrostatic Test Procedure Rev B | Code 3 | P22-BA-09-000-009_B_RO_Vessel_Hydrostatic_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, NOTE-01 |
| HP and LP Pressure Test Procedure Rev B | Code 3 | P22-BA-09-000-010_B_HP_LP_Pressure_Test_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |
| GA of Antiscalant Dosing Pump Skid Rev B | Code 2 | P22-DWG-09-005-011_B_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf | OBS-01, NOTE-01, NOTE-02 |

All documents with open observations or notes carry annotated PDFs (4 Code 3 + 3 Code 2). Only the two Code 1 — Approved documents (Inspection and Test Plan, NDE Plan) require no modification and carry no annotated PDF.

**Download — this transmittal and the seven annotated PDFs:** https://lrg.synology.me:6501/d/s/18x6gGzUV5gmg0nCp8tMGG5RF2wcjxD0/Dikk5IT6Dqqsuh78ZiYs2JFfpEmvYlwi-Yrxg1S1jVA0

## 5. Response Summary

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-BA-09-000-004 | Inspection and Test Plan (ITP) | 0 | 1 — Approved |
| P22-BA-09-000-005 | NDE Plan | C | 1 — Approved |
| P22-BA-09-000-009 | RO Vessel Hydrostatic Test Procedure | B | 3 — To Be Revised |
| P22-BA-09-000-010 | HP and LP Pressure Test Procedure | B | 3 — To Be Revised |
| P22-ET-09-008-01 | Datasheet of PLC and HMI Panel Component | C | 2 — Approved as Noted |
| P22-CD-09-005-001 | UHPRO Structural Calculation Report | A | 3 — To Be Revised |
| P22-DWG-09-005-014 | GA of CIP Flushing Tank | A | 2 — Approved as Noted |
| P22-DWG-09-005-015 | GA of Antiscalant Dosing Tank | B | 3 — To Be Revised |
| P22-DWG-09-005-011 | GA of Antiscalant Dosing Pump Skid | B | 2 — Approved as Noted |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Tally: 2 Code 1, 3 Code 2, 4 Code 3. The verdict rests on the fabrication test procedures and the structural anchoring: the RO Vessel Hydrostatic and the HP and LP Pressure Test Procedures still carry no binding test pressure, the UHPRO Structural Calculation Report omits the main-equipment anchorage, and the Antiscalant Dosing Tank still defers its seismic anchor loads. The Inspection and Test Plan Rev 0 and the NDE Plan Rev C close their Transmittal N23 observations, and the PLC and HMI, CIP Flushing Tank and Antiscalant Pump Skid documents are Approved as Noted. Documents not appearing in this response are unaffected by this transmittal.
