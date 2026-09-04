---
titulo: "TECHNICAL REVIEW TRANSMITTAL N6 - SECOND STAGE RO BRINE MODULE"
codigo: "P22-TM-09-000-006-0"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
nombre_planta: "TALTAL"
cliente: "ADASA"
fecha: "27-Feb-2026"
---

# 1. EXECUTIVE SUMMARY

## 1.1 Key Findings & Executive Summary

**TRANSMITTAL VERDICT: 4 - REJECTED**

BW Water Delivery 13 carries a Transmittal Verdict of 4 — Rejected. Two of the seven submitted documents are formally rejected: the Feed Turbocharger Datasheet Rev C and the Valve List Rev B. The five remaining documents are approved as noted. ADASA acknowledges the resolution of several historical items (Pt-100 sensors, PLC 50Hz, A/C configuration) addressed in this delivery.

**CRITICAL FAILURE 1: Unilateral Pressure Rating Downgrade (Turbochargers)**
BW Water has unilaterally reduced the HP coupling rating on the Feed Turbocharger from the contractual baseline of 2,000 psi (138 bar) down to 1,200 psi (82.7 bar), citing "out of stock" conditions. This is technically unacceptable for a UHPRO circuit. The 1,200 psi limit provides a severely deficient 19% safety margin at the Feed Turbocharger, and falls physically below the operating pressure of the 2nd stage joints (83.9 bar). Design safety margins cannot be compromised for logistical convenience. Furthermore, this represents a downgrade from the required Piedmont Pacific Style H (for HPB Energy Recovery) to Style D (standard RO).

**CRITICAL FAILURE 2: Quality Assurance Regression (Valve List)**
BW Water's formal Customer Comment Sheet (CCS) responses declared critical duplicate TAGs as "Already revised", yet the submitted Valve List Rev B entirely fails to implement these corrections. Furthermore, Rev B introduces two entirely new duplicate TAGs not present in the previous revision. A formal declaration of compliance that contradicts the actual engineering deliverable is inadmissible.

**Status Summary:**

| Status | Count | Documents |
|--------|-------|-----------|
| 1 — Approved | 0 | — |
| 2 — Approved as Noted | 5 | Utility List, HP Pump, Interstage TC, Cartridge Filter, Static Mixer |
| 3 — To be Revised | 0 | — |
| **4 — Rejected** | **2** | **Valve List, Feed Turbocharger** |

## 1.2 Critical Observations (Roadblocks)

| # | Observation | Severity | Document |
|---|-------------|----------|----------|
| OBS-01 | Feed Turbocharger coupling downgraded from 2,000 psi to 1,200 psi without formal deviation request. The 1,200 psi coupling (82.7 bar) provides only 19% margin over operating pressure (69.53 bar) and is below the operating pressure at UHPRO 2nd stage joints. Piedmont Style H substituted for lower-class Style D. EPDM Grade EW seal material must be confirmed. **REJECTED.** | CRITICAL | Feed Turbocharger Rev C |
| OBS-02 | Duplicate TAG VM-09-015: item 18 (DN100, motorized) and item 43 (DN15, manual) share the same TAG. BW Water claimed "Already revised" in CCS but the duplicate persists. | CRITICAL | Valve List Rev B |
| OBS-03 | Duplicate TAG VE-09-008: item 44 (DN80, ANSI 900#) and item 57 (DN80, ANSI 150#) share the same TAG despite different ratings and materials. Claimed as revised in CCS, but persists. | CRITICAL | Valve List Rev B |
| OBS-04 | Duplicate TAG VE-09-009 (NEW): item 58 (DN80, ANSI 900#) and item 93 (DN25, ANSI 150#) — new duplicate introduced in Rev B. | CRITICAL | Valve List Rev B |

## 1.3 Progress Noted (Closed Items)

| Item | Document | Status |
|------|----------|--------|
| PLC 50 Hz frequency corrected (TM N4 OBS-05) | Utility List Rev B | RESOLVED ✓ |
| A/C n+1 configuration confirmed (TM N2) | Utility List Rev B | RESOLVED ✓ |
| Pt-100 motor windings confirmed (TM N3) | HP Pump Rev C | RESOLVED ✓ |
| Vibration sensor mounting confirmed (TM N3) | HP Pump Rev C | RESOLVED ✓ |
| VM-09-015 electric actuation confirmed (TM N3) | Valve List Rev B | RESOLVED ✓ |

# 2. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| Transmittal Code | P22-TM-09-000-006-0 |
| BW Water Delivery | 13 (26-Feb-2026) |
| Total Documents Reviewed | 7 technical documents + 2 CCS |
| Response Required By | 10-Mar-2026 |

**Response Codes:** 1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information

# 3. DETAILED OBSERVATIONS BY DOCUMENT

## 3.1 Feed Turbocharger Rev C (P22-ET-09-009-007) — REJECTED

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-007 |
| Title | Datasheet of Feed Turbocharger |
| Vendor | FEDCO, Model HPB-60 |
| Tag | SIP-09-001 |
| Revision | C |
| Verdict | **4 — Rejected** |

**Confirmed acceptable items:**
- 10% operational safety margin maintained for all design cases (Year 0/Year 1, 19°C/24°C) ✓
- Super Duplex 2507 wetted materials ✓
- Performance BiTurbo data provided for all duty points ✓

**OBS-01 — Coupling pressure rating reduction: REJECTED (CRITICAL)**

Rev C reduces the coupling pressure rating from 2,000 psi (Rev B, confirmed in Technical Proposal Rev1 — Justification of Mechanical Couplings/Joints in High Pressure) to 1,200 psi, citing that 2,000 psi couplings are "out of stock and considered a rare item." This change is rejected on the following technical and contractual grounds:

**Ground 1 — Insufficient safety margin for UHPRO-rated HP circuit service**
The 1,200 psi (82.7 bar) coupling proposed in Rev C for the Feed Turbocharger operates at a maximum of 69.53 bar. At this joint the margin is 1.19x (19%) — completely insufficient for high-pressure concentrated brine service with transient pressure events. Furthermore, if this "out of stock" policy were applied across the system, the 1,200 psi coupling would fail at Joints 4 or 5 (UHPRO 2nd stage, 83.9 bar), as it would be physically below the operating pressure.

**Ground 2 — Change of product class, not equivalent substitution**
The 2,000 psi coupling specified in Rev B corresponds to the Piedmont Pacific Style H (classified for HPB Energy Recovery turbochargers). Rev C substitutes this with the Piedmont Style D (classified for standard RO). This is a unilateral contractual downgrade to a lower-class product. Logistical constraints ("out of stock") do not justify compromising design safety.

**Ground 3 — Breach of formal commitment in Submittal 25007-0002 CCS**
In BW Water's own consolidated comment sheet for Submittal 25007-0002 (January 22, 2026, Entrega 8), BW Water formally responded to ADASA's observation requesting CL900 specification with the following commitment: 'BW will provide coupling rated 2000 psi.' This statement applies to both the Feed Turbocharger and the Interstage Turbocharger. A formal commitment in a submitted CCS constitutes a contractual undertaking. Rev C violates this commitment without ADASA's approval.

**Ground 4 — Seal Material Confirmation**
Both coupling styles supply EPDM seals as standard. BW Water must confirm in Rev D that the replacement coupling (≥ 2,000 psi) is supplied with EPDM Grade EW pipe coupling seals per ET — High Pressure Piping. Additionally, BW Water must confirm the long-term compatibility of the FEDCO internal Buna N O-rings with 53,000 ppm TDS brine service.

**Required actions from BW Water:**
1. Revert to the coupling rated ≥ 2,000 psi with EPDM seals (Piedmont Style H or equivalent), or propose flanged CL900 or welded connection as offered in Technical Proposal Rev1 — Justification of Mechanical Couplings/Joints in High Pressure.
2. Confirm whether the HPB-60 delivered is the Standard model (MAWP 83 bar) or the Ultra model (MAWP 124 bar). Provide justification of the equipment rating against the system design pressure of 120 bar.
3. Issue datasheet Rev D incorporating the above corrections.

**Path to Resolution (Code 4 → Code 2):** ADASA confirms a technically acceptable path forward for the Feed Turbocharger: upgrade the coupling to ≥ 1,800 psi AND submit the coupling manufacturer's datasheet (model, MAWP, HPB service certification) for both turbochargers (SIP-09-001 and SIP-09-002). Under these conditions, ADASA would revise the verdict from Code 4 to Code 2. ADASA's preferred solution remains the return to 2,000 psi (Piedmont Style H), which constituted the contractual baseline.

## 3.2 Valve List Rev B (P22-LI-09-005-002) — REJECTED

| Field | Value |
|-------|-------|
| Code | P22-LI-09-005-002 |
| Title | Valve List — Second Stage RO Module for Brine |
| Revision | B |
| Verdict | **4 — Rejected** |

**Verdict rationale — Rejected (4):** BW Water's CCS submissions formally declared OBS-01 (VM-09-015) and OBS-02 (VE-09-008) as "Already revised on Valve List Rev. B" — neither correction was applied in the submitted document. A formal CCS declaration of compliance that does not correspond to the submitted revision is a severe QA failure. Furthermore, Rev B introduces two new duplicate TAGs (VE-09-009, VE-09-065). BW Water must issue Rev C resolving all four duplicates and perform a systematic uniqueness review.

**Outstanding observations — requiring Rev C:**

**OBS-02 — Duplicate TAG VM-09-015 (CRITICAL)**
Item 18 (DN100, Butterfly, ON/OFF MOTORIZED) and item 43 (DN15, Ball, MANUAL) share the same TAG. Claimed as fixed in CCS, but persists. Required action: Assign unique TAG.

**OBS-03 — Duplicate TAG VE-09-008 (CRITICAL)**
Item 44 (DN80, ANSI 900#, CE3MN) and item 57 (DN80, ANSI 150#, DI/SS420) share the same TAG. Claimed as fixed in CCS, but persists
. Required action: Assign unique TAG.

**OBS-04 — Duplicate TAG VE-09-009 (NEW - CRITICAL)**
Item 58 (DN80, ANSI 900#) and item 93 (DN25, ANSI 150#) — new duplicate introduced in Rev B. Required action: Assign unique TAG.

**OBS-05 — Duplicate TAG VM-09-065 (NEW - MAJOR)**
Item 30 (DN65, Butterfly) and item 76 (DN150, Butterfly) — new duplicate introduced in Rev B. Required action: Assign unique TAG.

## 3.3 Interstage Turbocharger Rev C (P22-ET-09-009-008) — APPROVED AS NOTED

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-008 |
| Title | Datasheet of Interstage Turbocharger |
| Vendor | FEDCO, Model HPB-60 |
| Tag | SIP-09-002 |
| Revision | C |
| Verdict | **2 — Approved as Noted** |

**Confirmed acceptable items:**
- Performance data consistent with 10% safety margin for all duty points ✓
- Super Duplex 2507 wetted materials ✓

**Note 1 — Coupling Rating:** The coupling was changed from 2,000 psi (Rev B) to 1,800 psi (Rev C). The 1,800 psi rating provides a 1.46x margin over the maximum service pressure (84.8 bar = 1,230 psi). ADASA accepts this marginal non-conformance (vs. strict 1.5x ASME requirement) on condition that FEDCO formally confirms in writing that the actual MAWP of the Style D SuperDuplex coupling is ≥ 1,845 psi under service conditions.

**Note 2 — Vibration sensor mounting:** ET 5.5.7 (L1390) applies to turbochargers. Confirmation of the mounting surface must be explicitly stated in the Interstage Turbocharger datasheet.

**Note 3 — Coupling datasheet not included:** Rev C specifies 1,800 psi for the coupling but does not include the coupling manufacturer's datasheet (model number, MAWP, service classification). This documentation must be submitted with the next revision as a condition for maintaining the Code 2 verdict.

## 3.4 HP Pump Datasheet Rev C (P22-ET-09-009-002) — APPROVED AS NOTED

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-002 |
| Title | Datasheet of RO HP Feed Pump |
| Revision | C |
| Verdict | **2 — Approved as Noted** |

**Resolved observations:**
- **TM N3:** 3-wire Pt-100 RTDs for bearings and windings included. CLOSED. ✓
- **TM N3:** Mounting surface for vibration sensor included. CLOSED. ✓

**Remaining note — Power clarification:**
To prevent misinterpretation in future reviews, ADASA requests that BW Water add a clarifying note in the datasheet distinguishing the Motor nameplate rating (93 kW), the Absorbed power at design point (78.5 kW), and the FEDCO internal nominal references (83 kW / 85 kW).

## 3.5 Cartridge Filter Rev C (P22-ET-09-009-005) — APPROVED AS NOTED

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-005 |
| Title | Datasheet of RO Cartridge Filter |
| Revision | C |
| Verdict | **2 — Approved as Noted** |

**Confirmed items:**
- 12 cartridges, FRP housing, EPDM seals confirmed. Justification of flow distribution accepted (90% of manufacturer maximum). ✓
- Nozzle orientation revised. ✓

**Note:** The change in nozzle orientation must be reflected in the container piping isometric and layout drawings. 

## 3.6 Static Mixer Rev B (P22-ET-09-009-012) — APPROVED AS NOTED

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-012 |
| Title | Datasheet of Static Mixer |
| Revision | B |
| Verdict | **2 — Approved as Noted** |

**Confirmed items:**
- Body and element material: FRP ✓
- Length increased to 750 mm (improved L/D ratio) ✓

**Note 1 — TAG discrepancy:** The datasheet specifies TAG MZE-09-001; however, the P&ID shows TAG MZE-09-009. This discrepancy must be resolved in Rev C.

## 3.7 Utility Consumption List Rev B (P22-LI-09-009-001) — APPROVED AS NOTED

| Field | Value |
|-------|-------|
| Code | P22-LI-09-009-001 |
| Title | Utility Consumption List |
| Revision | B |
| Verdict | **2 — Approved as Noted** |

**Resolved observations:**
- **TM N4:** PLC frequency corrected to 50Hz. CLOSED. ✓
- **TM N2/N4:** A/C (1W+1S) configuration confirmed. CLOSED. ✓
- **TM N4:** HP Pump power explicitly listed (93 kW nameplate vs 78.5 kW operating). CLOSED. ✓

**Remaining action:**
**TM N2 — A/C thermal calculation:** BW Water states the A/C power was revised "based on the A/C thermal calculation," but the calculation itself has not been submitted. BW Water must submit this document.

# 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

The following observations from Transmittals N2 through N5 have not been addressed in BW Water Delivery 13 and remain open.

| # | Origin | Description | Days Open | Status |
|---|--------|-------------|-----------|--------|
| 1 | TM N2 | A/C thermal calculation document not submitted | **51 days** | Open — submit within 10 days |
| 2 | TM N2 | Modbus TCP Memory Map not submitted | **51 days** | Open — submit with next engineering batch |
| 3 | TM N3 | IO List not updated after coordination signal changes | **30 days** | Open — coordinate with IO List Rev |
| 4 | TM N4 | UPS not included in BOM. Confirm supply scope. | **22 days** | Open — confirmation required |
| 5 | TM N5 | Equipment Layout Rev B not yet submitted. | **4 days** | Open — submit Equipment Layout Rev B |

# 5. REQUIRED ACTIONS — BW WATER

BW Water must address the following items by **10-Mar-2026**:

| Priority | Action | Document |
|----------|--------|----------|
| **CRITICAL** | **Feed Turbocharger:** Revert to coupling rated ≥ 2,000 psi with EPDM seals (Piedmont Style H or equivalent). | P22-ET-09-009-007 Rev D |
| **CRITICAL** | **Valve List:** Resolve duplicate TAGs (VM-09-015, VE-09-008, VE-09-009, VM-09-065). Perform systematic uniqueness review. | P22-LI-09-005-002 Rev C |
| **MAJOR** | **Feed TC:** Confirm whether HPB-60 is Standard or Ultra model. Confirm long-term compatibility of FEDCO internal Buna N O-rings. | P22-ET-09-009-007 Rev D |
| **MAJOR** | **Submit coupling datasheets:** Submit the coupling manufacturer's datasheet for both turbochargers (SIP-09-001 Feed TC, SIP-09-002 Interstage TC): model number, MAWP, HPB service certification. | P22-ET-09-009-007/008 Rev D |
| **MAJOR** | Document vibration sensor mounting explicitly in both Turbocharger datasheets. | TC Datasheets Rev D |
| **MAJOR** | Submit A/C thermal calculation document. | Supporting document |
| MINOR | Confirm MZE-09-001 TAG in Static Mixer datasheet matches P&ID. | P22-ET-09-009-012 |
| MINOR | Confirm nozzle orientation change in Cartridge Filter is reflected in piping isometrics. | Piping isometrics |
| MINOR | Confirm or include UPS in module BOM. | BOM / equipment list |

# 6. ATTACHMENTS

The following BW Water documents, as received in BW Water Delivery 13, have been reviewed and commented by ADASA. Marked-up PDF copies are provided as attachments to this transmittal:

| # | Document Code | Title | Rev |
|---|---------------|-------|-----|
| A1 | P22-LI-09-005-002 | Valve List | B |
| A2 | P22-LI-09-009-001 | Utility Consumption List | B |
| A3 | P22-ET-09-009-002 | Datasheet of RO HP Feed Pump | C |
| A4 | P22-ET-09-009-007 | Datasheet of Feed Turbocharger | C |
| A5 | P22-ET-09-009-008 | Datasheet of Interstage Turbocharger | C |
| A6 | P22-ET-09-009-005 | Datasheet of RO Cartridge Filter | C |
| A7 | P22-ET-09-009-012 | Datasheet of Static Mixer | B |

