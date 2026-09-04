# TECHNICAL REVIEW TRANSMITTAL N22 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-022-0
**Date:** 15-Jun-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittal:** 25007-0049 and 25007-0050

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — To Be Revised.** Seven documents, submittals 25007-0049 and 25007-0050. Tally: 2 Code 1, 1 Code 2, 4 Code 3. Driver: the Plant Control Philosophy Rev D — its operative control logic remains in child documents not delivered with this submittal.

**Disposition at a glance:**

- **Plant Control Philosophy Rev D — Code 3.** Repeated CRITICAL permissive closed; Sequence Charts, Setpoint List and Control Matrix still undelivered (sixth cycle).
- **Equipment Layout Rev C — Code 3.** RO Cartridge Filter still drawn horizontal against its own vertical datasheet.
- **RO Cartridge Filter Rev E — Code 1.** FRP housing retained; specification correct as-is (material certificate to the vessel dossier).
- **CIP Cartridge Filter Rev D — Code 3.** Seal/FRP compatibility for the pH 2–12 cleaning duty still undocumented.
- **Static Mixer Rev C — Code 2.** Tag discrepancy closed; two page reconciliations to fold into Rev 0.
- **Utility Consumption List Rev C — Code 1.** 50 Hz and HP Pump power reconciled; accepted as-is.
- **HMI Display Screenshot Rev A — Code 3.** First real screen design (closes the oldest open commitment); screen set still incomplete.

**Why Code 3 — Plant Control Philosophy Rev D:** Rev D closes the repeated CRITICAL permissive and corrects the salt-rejection formula to feed conductivity, but it defers the start/stop/trip step logic, the setpoint register and the cause-and-effect matrix to three child documents absent from this submittal — the sixth review with that logic outside the package. Open items from previous transmittals are inventoried in Section 3.

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 Plant Control Philosophy Rev D — P22-BT-09-009-001

**Response Code: 3 — To be revised**

**Status.** Rev D closes the repeated CRITICAL — the HP Pump start permissive now lists VE-09-007 once and the antiscalant valve VE-09-014 no longer inhibits start — and corrects the salt-rejection formula to feed conductivity (CIT-09-001B); 4-20 mA + HART and the instrumentation-failure response are confirmed. It stays open because the operative numerical logic (sequence charts, setpoint list, control matrix) remains in child documents not delivered with this submittal — the sixth cycle — plus minor body cleanups. Annotations on `P22-BT-09-009-001_D_Control_Philosophy_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | Core control logic still resides in undelivered child documents — the Controls and Sequence Chart (P22-LI-09-008-017), the Alarm and Control Setpoint List (P22-LI-09-008-015) and the Control Matrix are referenced throughout but were not submitted with the Control Philosophy, so the start/stop/normal/trip step logic, the full setpoint register and the cause-and-effect matrix cannot be verified |
| OBS-02 | MINOR | The salt-rejection narrative still states the metric compares permeate conductivity (CIT-09-002) against reject conductivity (CIT-09-005), contradicting the corrected feed-conductivity formula on the facing page; confirm the interstage and Stage-2 indicator denominators reference the intended conductivity tags |
| OBS-03 | MINOR | The power-monitoring section does not enumerate the loads that the Technical Offer requires the guaranteed energy consumption to include (HP pump, dosing pump, CIP pump, CIP heater, RO PLC power, lighting and air-conditioning), so the displayed and tested figure is not traceable to the contractual basis |
| OBS-04 | MINOR | The common-permeate conductivity analyzer is tagged AIT-09-002 in the permeate-monitoring narrative but CIT-09-002 in the equipment table and in every formula and permissive; a single instrument must carry one tag throughout |
| OBS-05 | MINOR | The cover revision block records Rev D dated 28-May-2026, while the page header still reads an earlier date and revision number and the page-count fields disagree; reconcile the controlling revision and date metadata |
| NOTE-01 | NOTE | HP Pump start permissive corrected — the duplicated VE-09-007 and the spurious VE-09-014 are removed; the repeated CRITICAL of Transmittal N15 NOTE-20 / N18 OBS-01 is closed |
| NOTE-02 | NOTE | The 4-20 mA + HART protocol and the instrumentation-failure response are confirmed in the body; the corresponding numerical trip and alarm values remain to be verified against the Setpoint List and Control Matrix once issued |

**Action — re-issue as Rev E:** issue the Operating Sequence Charts (start, stop, normal and trip for RO, CIP and flushing), the consolidated Alarm and Control Setpoint List and the Control Matrix as formally coded and revisioned documents with a binding delivery date, submitted together with the Control Philosophy (OBS-01). In the document itself, rewrite the salt-rejection narrative to match the corrected feed-conductivity formula and confirm the indicator denominators (OBS-02); enumerate the metered load set behind the guaranteed energy consumption (OBS-03); correct AIT-09-002 to CIT-09-002 on the permeate-monitoring narrative (OBS-04); and reconcile the header revision and date with the cover block (OBS-05). The permissive correction and the HART confirmation are accepted. The Plant Control Philosophy cannot be closed until the three child documents are submitted.

---

### 2.2 Equipment Layout Rev C — P22-DWG-09-005-003

**Response Code: 3 — To be revised**

**Status.** The drawing is not consistent with the cartridge filters of its own submittal: the RO Cartridge Filter (item 2) is still drawn horizontal while its Datasheet Rev E declares it vertical (the horizontal-to-vertical change of Technical Note P22-NT-09-000-001-0); the CIP filter (item 11) is correctly vertical. The Operating Weight table is again deferred to a separate Civil and Loading drawing, against the Transmittal N15 instruction to embed it; the container envelope and dimensioning are in order. Annotations on `P22-DWG-09-005-003_C_Equipment_Layout_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The RO Cartridge Filter (FIL-09-001, item 2) is drawn horizontal, inconsistent with the vertical type declared in the RO Cartridge Filter Datasheet Rev E of the same submittal and with the horizontal-to-vertical change of Technical Note P22-NT-09-000-001-0; the layout does not reflect the vertical reconfiguration (footprint, operator access and 2000 mm clear headroom for cartridge withdrawal). The CIP Cartridge Filter (item 11) is shown vertical and is consistent |
| OBS-02 | MAJOR | The Operating Weight table is again deferred to a separate Civil and Loading drawing not yet submitted, against the Transmittal N15 NOTE-04 instruction to embed it in the Rev 0 issue |
| OBS-03 | MINOR | The legend labels no main or power panel; the Grounding Layout Rev F is anchored to "the main panel fixed in the approved Equipment Layout position", so the panel should be labelled and its position unified between both drawings, and the title-block revision field made legible |

**Action — re-issue as Rev D:** update the Equipment Layout to show the RO Cartridge Filter in its vertical configuration consistent with Datasheet Rev E, including the footprint, operator access and the vertical clearance for cartridge removal, which closes the as-built requirement of the Technical Note (OBS-01). Embed the Operating Weight table in the Equipment Layout for Rev 0, or obtain ADASA's written acceptance to keep the weights only in the separate Civil and Loading drawing, and deliver that drawing (OBS-02). Label the main panel consistent with the Grounding Layout Rev F and make the title-block revision legible (OBS-03).

---

### 2.3 RO Cartridge Filter Rev E — P22-ET-09-009-005

**Response Code: 1 — Approved**

**Status.** Approved as-is. The premise of the Technical Note (FRP to SS316) no longer applies — Rev E retains the FRP housing — so the material concern falls away, and the datasheet is complete (vendor, 1 µm rating, 7 bar design accepted in Transmittal N19, flows, ANSI B16.5 Class 150 connections). The outstanding items are not changes to the specification: the FRP housing material certificate travels with the vessel fabrication dossier, and the vertical as-built and procedural commitments are handled elsewhere — tracked in Section 3.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** Related deliverables tracked in Section 3 — Pending Observations from Previous Transmittals: the FRP housing material certificate, to be issued with the vessel fabrication dossier; the vertical-configuration as-built, through the Equipment Layout (Section 2.2); and the pre-Purchase-Order approval and tie-in immobility attestation, through the Technical Note reply.

---

### 2.4 CIP Cartridge Filter Rev D — P22-ET-09-009-006

**Response Code: 3 — To be revised**

**Status.** The closure threshold set in Transmittal N19 is not met: the chemical-compatibility statement for the pH 2–12 cleaning duty is still missing and the brochure-default nitrile gasket is unsuitable for high-pH service. The horizontal-to-vertical change and the Filtrek-to-Sysflo substitution also remain ahead of ADASA's formal Technical Note position, so any Purchase Order before that release is at BW Water's risk; two minor consistency items remain (Component Name, surface-area basis). Annotations on `P22-ET-09-009-006_D_CIP_Cartridge_Filter_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The FRP housing and gasket chemical-compatibility statement for the pH 2 to 12 cleaning duty is still missing; the default nitrile gasket has poor high-pH resistance. Name a gasket suitable across the full pH range and attach a compatibility statement for the housing and seal against the cleaning reagents — the item Transmittal N19 OBS-03 asked to close in this revision |
| OBS-02 | MAJOR | The horizontal-to-vertical change and the Filtrek-to-Sysflo vendor substitution remain ahead of ADASA's formal Technical Note position; re-issue only after that position, and do not place the Purchase Order until the formal release, with any earlier purchase at BW Water's risk |
| OBS-03 | MINOR | The Component Name field labels the CIP filter as "RO CIP Cartridge Filter"; correct to "CIP Cartridge Filter" consistent with tag FIL-09-002 |
| OBS-04 | MINOR | The filter surface-area basis differs from the RO Cartridge Filter sibling (total versus per-cartridge), and the filtration rate is stated in a unit that does not allow an area cross-check; homologate the basis and express the rate in m³/h/m² |
| NOTE-01 | NOTE | The container as-built with the vertical configuration is a separate, shared deliverable — verified through the Equipment Layout (Section 2.2) and tracked in Section 3 |

**Action — re-issue as Rev E:** name the gasket and o-ring material selected for the pH 2 to 12 duty and attach the chemical-compatibility statement for the FRP housing and seal against the cleaning reagents, closing the Transmittal N19 item (OBS-01). Re-issue only after ADASA's formal position on the Technical Note clarifications, and hold the Purchase Order until that release (OBS-02). Correct the Component Name (OBS-03) and homologate the surface-area basis with the RO sibling, expressing the filtration rate in m³/h/m² (OBS-04).

---

### 2.5 Static Mixer Rev C — P22-ET-09-009-012

**Response Code: 2 — Approved as Noted**

**Status.** The carry-forward tag discrepancy is closed (MZE-09-001 now agrees with the P&ID) and the component is sound (FRP, ANSI 150 RF, 49 m³/h, four elements) on the low-pressure feed line. What remains is internal to the document — the vendor data sheet and the ADASA front sheet state different design conditions and injection rates — reconciled at Rev 0 without a new revision. Annotations on `P22-ET-09-009-012_C_Static_Mixer_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MINOR | The vendor technical data sheet (1150 kg/m³, 35 °C, fluid labelled "Antiscalant") contradicts the ADASA front sheet (feed brine, specific gravity 1.05, 19 to 24 °C); both agree the main stream is 49 m³/h, so the sizing is unaffected |
| OBS-02 | MINOR | The antiscalant injection rate is stated with different values across the sheets; align to a single value and unit matching the accepted Antiscalant Dosing Pump duty |
| NOTE-01 | NOTE | Component duty, sizing and connections (49 m³/h main stream, FRP, ANSI 150 RF, four elements) accepted as-is |

**Action to issue at IFC Rev 0 — no new Static Mixer revision required:**
1. Reconcile the vendor technical data sheet with the ADASA front sheet so the project feed-brine conditions read consistently on both pages, or add a remark stating that 1150 kg/m³ and 35 °C is a conservative design envelope (OBS-01).
2. Align the injection rate to a single value and unit matching the accepted Antiscalant Dosing Pump duty (OBS-02).

ADASA accepts the component as noted on the basis that these reconciliations are folded into the Rev 0 issue and the sizing is unchanged.

---

### 2.6 Utility Consumption List Rev C — P22-LI-09-009-001

**Response Code: 1 — Approved**

**Status.** Approved as-is. The 50 Hz frequency now reads throughout (closing the original 60 Hz CRITICAL of Transmittal N4) and the HP Pump power reconciles (93 kW rating / 78.5 kW operating). Three points are noted for the record without changing the list: the 3.97 kWh/m³ figure is normal-operation consumption, not the guaranteed 4.71 kWh/m³ ±5%; the maintenance socket is counted 24 h/day (conservative); and the standby air-conditioning connected load reads against the Electrical Load List.

**Action: none on this document — accepted; issue directly at IFC Rev 0.** The notes above are for the record; the 50 Hz frequency and the HP Pump power reconciliation are confirmed closed.

---

### 2.7 HMI Display Screenshot Rev A — P22-LI-09-008-016

**Response Code: 3 — To be revised**

**Status.** Rev A delivers a real screen design for the first time, materially closing the HMI commitment opened at Transmittal N4 — the oldest open item of the project. It does not close because the screen set is incomplete against the Technical Specification: the electrical-variables/energy-consumption (kWh/m³) screen, a trending screen, a setpoint screen and several process zones are missing, and ISA-101 conformance is asserted but not yet evidenced. Annotations on `P22-LI-09-008-016_A_HMI_Display_Screenshot_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | The screen set omits a screen showing the electrical-variables meter readings together with the specific energy consumption in kWh/m³, which the Technical Specification requires; add it or document the existing screen where these variables are presented |
| OBS-02 | MAJOR | The screen set omits a process-variable trending screen (distinct from the alarm history present); add at least one trending screen for the important process variables (flow, pressure, conductivity, levels) |
| OBS-03 | MAJOR | The screen set omits a setpoint and parameterization screen with safe operating limits, which the Technical Specification requires; add it or document the faceplate path by which the operator sets values and limits |
| OBS-04 | MAJOR | Only two process screens are delivered (RO Cartridge Filter, RO Feed/HP Pump); the module also requires an overview screen and screens for second-stage RO, CIP, dosing, energy recovery and brine, with tags consistent with the approved P&ID and the Instrument List |
| OBS-05 | MINOR | ISA-101 conformance (screen hierarchy, state colour-coding, alarm prioritization) is declared but not evidenced; demonstrate it in the next revision and reserve the full visual verification for the Factory Acceptance Test |
| NOTE-01 | NOTE | P22-LI-09-008-016 is registered as the document that materially closes the historical HMI screenshot commitment P22-BREAD-09-008-001 |

**Action — re-issue as Rev B:** complete the screen set — add the electrical-variables and energy-consumption screen (OBS-01), a process-variable trending screen (OBS-02), a setpoint and parameterization screen with safe operating limits (OBS-03), and the missing process screens including an overview (OBS-04), with tags consistent with the approved P&ID and the current Instrument List; and evidence ISA-101 conformance, reserving the full visual verification for the Factory Acceptance Test (OBS-05). The HMI hardware fixed in the PLC and HMI Panel Component Datasheet Rev B (PanelView Plus 7) is the basis for the screen layout.

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

This submittal delivered E49 and E50 only. The status below reflects what those packages resolved and what remains tracked from Transmittal N21 and earlier.

**Addressed in this transmittal (moved into Section 2):**

- TM N18 Section 2.1 OBS-01 (CRITICAL, HP Pump permissive — duplicated VE-09-007 and spurious VE-09-014) — closed by the Plant Control Philosophy Rev D (Section 2.1 NOTE-01); the Contract C-4300 reservation on this point is satisfied.
- TM N18 Section 2.1 OBS-03 (salt-rejection formula) — corrected in Rev D; a residual narrative-versus-formula contradiction is now tracked as Section 2.1 OBS-02.
- TM N18 Section 2.1 NOTE-01 / NOTE-02 (energy-consumption metering point and contractual value) — substantially resolved; the 4.71 kWh/m³ ±5% value is declared and the metering point reconciled, with a residual scope-enumeration gap as Section 2.1 OBS-03.
- TM N4 NOTE-05 (HMI screen design, P22-BREAD-09-008-001, the oldest open commitment, about 127 days) — materially delivered as P22-LI-09-008-016 Rev A; downgraded from open to materially delivered, with the screen-set completion tracked under Section 2.7.
- Technical Note P22-NT-09-000-001-0 clarifications on the cartridge-filter datasheets (due 15-Jun-2026) — addressed in the RO Cartridge Filter Rev E and the CIP Cartridge Filter Rev D and dispositioned under Sections 2.3 and 2.4.

**Open from previous transmittals — the three most serious** (minor open items remain tracked in the Master Deliverable Register):

| Origin TM | Document | Observation | Status |
|-----------|----------|-------------|--------|
| TM N19 Section 2.10 | ITP Offsite (P22-BA-09-000-004) and vessel test procedures | Vessel hydrostatic test evidence, dossier and witness point; Hydrostatic, Preservation and FAT procedures — to be captured in the ITP | OPEN — the ASME stamp was waived by ADASA (02-Jun, reaffirmed on the adopted Project Schedule Rev A of 09-Jun); fabrication and testing follow ASME standards without the stamp. What remains is the ITP Rev C documenting that agreed basis, with the vessel hydrostatic test at 1,800 psi × 1.1, the complete production/test dossier and ADASA's witness point at the vendor — none of which the adopted schedule shows |
| TM N20 Section 2.6 | PLC-LCP Outline Panel Drawing Rev A (P22-CD-09-008-001) | Enclosure contradiction (sheet steel / IP55 versus SS316L / NEMA 4X-IP66) — fabrication gate | OPEN — Outline Rev B with the aligned Panel Specification Sheet, actual panel weight and reconciled cooling awaited; the expedited release path stated in the response of 10-Jun applies |
| TM N18 Section 2.1 | Control cascade: I/O List Rev 2, Instrumentation and Control Cable Schedule, Alarm and Interlock List, PLC/LCP Schematic | The whole control package gated on the control logic | OPEN — each remains Code 3 on its own re-submittal; closure now waits on the undelivered Sequence Charts, Setpoint List and Control Matrix (Section 2.1 OBS-01), no longer on the Control Philosophy itself |

**Open deliverables and procedural items (not document defects):**

- RO Cartridge Filter housing material certificate (Section 2.3) — to be issued with the vessel fabrication dossier; the datasheet itself is approved as-is.
- Vertical-configuration as-built — partially addressed: the Equipment Layout Rev C shows the CIP filter vertical but still draws the RO filter horizontal (Section 2.2 OBS-01); the vertical clearance and cartridge-withdrawal envelope are to be confirmed when the layout is updated.
- Pre-Purchase-Order approval and tie-in immobility attestation — procedural commitments to be handled through the Technical Note reply. Procurement of the alternative filter before ADASA's formal release remains at BW Water's risk.

---

## 4. ATTACHMENTS

| Document | Verdict | Annotated File | Annotations |
|----------|---------|---------------|-------------|
| Plant Control Philosophy Rev D | Code 3 | P22-BT-09-009-001_D_Control_Philosophy_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, NOTE-01, NOTE-02 |
| Equipment Layout Rev C | Code 3 | P22-DWG-09-005-003_C_Equipment_Layout_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03 |
| CIP Cartridge Filter Rev D | Code 3 | P22-ET-09-009-006_D_CIP_Cartridge_Filter_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01 |
| Static Mixer Rev C | Code 2 | P22-ET-09-009-012_C_Static_Mixer_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |
| HMI Display Screenshot Rev A | Code 3 | P22-LI-09-008-016_A_HMI_Display_Screenshot_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05 |

Five documents carry open observations or notes and are returned with annotated PDFs (4 Code 3 + 1 Code 2). The two Code 1 — Approved documents — the RO Cartridge Filter Rev E and the Utility Consumption List Rev C — carry no annotated PDF; their related deliverables are tracked in Section 3.

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-BT-09-009-001 | Plant Control Philosophy | D | 3 — To Be Revised |
| P22-DWG-09-005-003 | Equipment Layout | C | 3 — To Be Revised |
| P22-ET-09-009-005 | Datasheet of RO Cartridge Filter | E | 1 — Approved |
| P22-ET-09-009-006 | Datasheet of CIP Cartridge Filter | D | 3 — To Be Revised |
| P22-ET-09-009-012 | Datasheet of Static Mixer | C | 2 — Approved as Noted |
| P22-LI-09-009-001 | Utility Consumption List | C | 1 — Approved |
| P22-LI-09-008-016 | HMI Display Screenshot | A | 3 — To Be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** Tally: 2 Code 1, 1 Code 2, 4 Code 3. The Plant Control Philosophy Rev D fixes the verdict: the repeated CRITICAL permissive is closed and the body is materially better, but its operative numerical logic stays in three undelivered child documents, sustaining the new-revision path for a sixth cycle on a documentation-delivery driver rather than a safety driver. The Equipment Layout repeats the open status because it still draws the RO cartridge filter horizontal against its own vertical datasheet, and the CIP Cartridge Filter still lacks the pH-range seal compatibility statement. The RO Cartridge Filter and the Utility Consumption List are Approved as-is, their related deliverables tracked in Section 3, and the Static Mixer is Approved as Noted with its page reconciliation folded into the Rev 0 issue. Documents not appearing in this response are unaffected by this transmittal.
