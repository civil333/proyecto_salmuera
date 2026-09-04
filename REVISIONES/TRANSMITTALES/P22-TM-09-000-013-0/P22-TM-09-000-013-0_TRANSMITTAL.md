# TECHNICAL REVIEW TRANSMITTAL N13 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-013-0
**Date:** 06-Apr-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittals:** 25007-0024, 25007-0025

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 2 — APPROVED AS NOTED**

Two deliveries are evaluated in this transmittal. Both documents are approved as noted.

Key findings:

- **Piping and Instrumentation Diagram Rev C (Code 2 — Approved as Noted):** Delivery 24 (25007-0024, received March 31, 2026). Transmittal N9 NOTE-01 (title block code) and NOTE-02 (antiscalant tank volume) are confirmed closed in Rev C, as documented in the Consolidated Comment Sheet. One notation note is raised regarding a discrepancy between the CIP Tank (TK-09-001) capacity annotated in Rev C (6.81 m³) and the value established in the accepted Equipment List Rev B (6.1 m³). Clarification is requested prior to IFC (Rev 0).

- **Typical Installation Details of Power Works Rev B (Code 2 — Approved as Noted):** Delivery 25 (25007-0025, received April 6, 2026). Both observations from Transmittal N8 are closed: OBS-01 (grounding/earthing specifications) is addressed by the new grounding detail page covering seven installation methods; OBS-02 (installation standard) is addressed by citation of NEMA VE-2, NEC Article 392.30(B), and NEC Article 352 throughout. Three informational notes are raised: grounding conductor sizing basis not cited, Cable Tray Layout drawings not yet submitted, and ADASA duct bank interface data required.

---

## 2. DETAILED OBSERVATIONS BY DOCUMENT

### 2.1 Piping and Instrumentation Diagram Rev C — P22-DWG-09-009-002

**Response Code: 2 — Approved as Noted**

The Consolidated Comment Sheet (CCS) included in Rev C addresses both notes from Transmittal N9:

**Transmittal N9 NOTE-01 — CLOSED:** The document code in the title block has been corrected to P22-DWG-09-009-002 (three-digit correlativo). BW Water response in CCS: "BW has revised accordingly."

**Transmittal N9 NOTE-02 — CLOSED:** TK-09-002 (Antiscalant Dosing Tank) is now annotated as VOL: 0.34 m³ (TOTAL), consistent with the total installed capacity of the accepted datasheet (P22-ET-09-009-010 Rev B). BW Water response in CCS: "BW has revised accordingly."

The P&ID continues to show all principal process equipment correctly identified and tagged: HP Feed Pump (BH-09-001), Feed Turbocharger (SIP-09-001), Interstage Turbocharger (SIP-09-002), 1st and 2nd Stage RO Racks (BOI-09-001/002), Static Mixer (MZE-09-001), Cartridge Filters (FIL-09-001/002), CIP Tank (TK-09-001), and Antiscalant Dosing Skid (BDS-09-001/002). High-pressure lines are shown in Super Duplex Stainless Steel consistent with previous reviews.

#### Note NOTE-01 — CIP Tank capacity annotation inconsistency (MINOR)

**Document:** Piping and Instrumentation Diagram Rev C — P22-DWG-09-009-002
**Severity:** Informational

Rev C annotates TK-09-001 (CIP Tank) with a capacity of 6.81 m³. The accepted Equipment List Rev B (P22-LI-09-005-001, Delivery 19) specifies the CIP Tank (Dayamas DYM 6800, HDPE, 1800 mm diameter × 2950 mm height) with a working volume of 6.1 m³, consistent with the Process Calculation Rev B selected volume. Revision B of this P&ID showed 6.1 m³.

The 0.71 m³ increase between Rev B and Rev C has no supporting documentation in any submittal received to date. Confirm the correct installed capacity of TK-09-001 and update the P&ID annotation consistent with the Equipment List prior to IFC (Rev 0). If the CIP Tank specification was revised, submit an updated Equipment List Rev C with justification.

---

### 2.2 Typical Installation Details of Power Works Rev B — P22-DWG-09-007-005

**Response Code: 2 — Approved as Noted**

Rev B was submitted in response to Transmittal N8, which issued Code 3 — To Be Revised on Rev A for two observations. Both are addressed in Rev B.

**Transmittal N8 OBS-01 — CLOSED:** Rev B adds a dedicated grounding page (Page 9: Grounding Link — Electrical Installation Details) specifying seven grounding methods: cable tray bonding via copper earth link bar, Cu/PVC green wire, and Cu tinned flexible braided conductor (all bonded to container structure); skid structure grounding; motor grounding via two methods (cable tray bonding to motor frame or motor terminal box ground terminal); panel grounding; and analog instrument cable shield termination to a grounded terminal block. Conductor sizes are specified: 16 mm² for main bonding conductors, 4 mm² for instrument grounding wires.

**Transmittal N8 OBS-02 — CLOSED:** Rev B cites applicable installation standards throughout all pages: NEMA VE-2 (cable tray installation and bonding), NEC Article 392.30(B) (cable tray support spacing), and NEC Article 352 (conduit installation).

#### Note NOTE-01 — Grounding conductor sizing basis not cited (MINOR)

Rev B specifies bonding and grounding conductor sizes (16 mm² for main conductors, 4 mm² for instrument grounds) but does not cite the NEC table or design calculation used to establish these values. BW Water should confirm the sizing basis — for example, NEC 250.122 for equipment grounding conductor sizing — in the next revision of this drawing or in a supporting design calculation. No further review cycle is required for this document on this point; sizing basis may be incorporated in IFC (Rev 0).

#### Note NOTE-02 — Cable Tray Layout drawings not yet submitted (INFORMATIONAL)

The installation details in Rev B define standard assembly configurations for cable trays, conduits, and grounding connections. The complete internal cable routing from the main panel (LCP/MCC) to each load endpoint — including BH-09-001 (HP Pump motor), BH-09-002 (CIP Pump motor), antiscalant dosing pump, CIP heater, and instrumentation panels — has not been submitted. This routing information falls within the scope of the Cable Tray Layout drawing(s), which are a distinct deliverable and have not been received. BW Water must submit the Cable Tray Layout drawing(s) showing the complete routing path and cable segregation (power / control / analog) throughout the module prior to IFC (Rev 0).
*Basis: ET — Electrical and Control Systems; ET §5.6 — Scope of Supply (all internal wiring, interconnection of equipment, and internal conduit/cable tray routing is provider scope)*

#### Note NOTE-03 — ADASA incoming power connection via duct bank (INFORMATIONAL)

ADASA confirms that the incoming power supply from the ADASA electrical room to the BW Water main panel will be routed via underground duct bank. To allow ADASA to finalize the duct bank civil design, BW Water must confirm: (a) the number and diameter of incoming conduits required at the main panel entry point; (b) the terminal block or busbar arrangement for incoming power conductors; (c) the conductor count and cross-section per circuit (main feeder, control power supply, UPS input). This information must be included in the next revision of this drawing or submitted as a dedicated Interface Document prior to commencement of duct bank civil works.
*Basis: ET §5.6 — Electrical Supply Limit (incoming connection to panel terminals = ADASA scope; BW Water scope begins at panel incoming terminals)*

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

The following observations from Transmittals N10, N11, and N12 remain open. No documents addressing these items have been received since Transmittal N12 (issued March 30, 2026).

**Status update for TM N10 OBS-05:** P&ID Rev C confirms TK-09-002 = 0.34 m³ total volume, partially addressing this observation. GA Antiscalant Tank Rev B is still required for seismic anchor data and body material confirmation.

ADASA requests BW Water to confirm the expected submission dates for I/O List Rev C, Data Transfer List Rev B, and Valve List Rev D, as these carry multiple Major open observations that have been outstanding for more than 18 days.

| Transmittal | OBS/NOTE | Document | Description | Status |
|-------------|----------|----------|-------------|--------|
| N10 | OBS-01 | I/O List Rev B / Data Transfer List Rev A | Motor temperature TAG inconsistency (TE vs TIT); TIT-09-003 service conflict (CIP Tank vs HP Pump Bearing) | OPEN — I/O List Rev C and Data Transfer List Rev B not received |
| N10 | OBS-02 | Data Transfer List Rev A | Conductivity scaling 0–20 mS/cm for brine lines CIT-09-001/004/005; expected 65–133 mS/cm | OPEN — Data Transfer List Rev B not received |
| N10 | OBS-03 | Data Transfer List Rev A | VE-09-014 duplicated in DI Modbus block; LS-09-001 and LS-09-002 absent from Modbus map | OPEN — Data Transfer List Rev B not received |
| N10 | OBS-04 | Control System Architecture Rev C | UPS 8-hour autonomy not confirmed — no load list or battery calculation provided | OPEN — Confirmation not received |
| N10 | OBS-05 | GA Antiscalant Dosing Tank Rev A | Effective working volume, body material, and seismic anchor data (NCh 2369 Zone 3) absent | PARTIALLY ADDRESSED — P&ID Rev C now shows TK-09-002 as 0.34 m³ total. GA Rev B still required for remaining items |
| N10 | NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | HMI display screenshots committed at Transmittal N4 — not yet submitted | OPEN — Document not received |
| N11 | OBS-01 | Valve List Rev C | Duplicate TAG VE-09-007 — Items 44 and 64 | OPEN — Valve List Rev D not received |
| N11 | OBS-02 | Valve List Rev C | Duplicate TAG PSV-09-002 — Items 105 and 112 | OPEN — Valve List Rev D not received |
| N11 | OBS-03 | Grounding Point and Power Panel Location Layout Rev B | Equipment positions derived from Piping Layout Rev A, rejected in Transmittal N7 | OPEN — pending acceptance of Equipment Layout Rev B |
| N11 | OBS-04 | Instrument Location Layout Rev B | Same basis as OBS-03 | OPEN — pending acceptance of Equipment Layout Rev B |
| N12 | OBS-01 | Datasheet of Vibration Transmitter Rev A | HART protocol not specified for IFM VTV122 — ET Instrumentation requires 4–20 mA + HART for all field instruments | OPEN — Datasheet Rev B not received |
| N12 | NOTE-01 | Datasheet of Vibration Transmitter Rev A | Quantity field reads 1 for three TAGs (VT-09-001/002/003) | OPEN — Datasheet Rev B not received |
| N12 | NOTE-02 | Line List Rev B | Super Duplex Steel lines designated SCH80 without S suffix; correct designation is SCH 80S per ASME B36.19M | OPEN — to be incorporated in IFC (Rev 0) |

---

## 4. ATTACHMENTS

The following BW Water document was reviewed and annotated by ADASA:

| Attachment | Document Code | Title | Rev | Annotations |
|------------|---------------|-------|-----|-------------|
| A | P22-DWG-09-009-002 | Piping and Instrumentation Diagram | C | NOTE-01 |
| B | P22-DWG-09-007-005 | Typical Installation Details of Power Works | B | NOTE-01, NOTE-02, NOTE-03 |

---

## 5. RESPONSE SUMMARY

| Submittal No. | Document No. | Document Description | Rev | Response Code |
|---------------|-------------|---------------------|-----|---------------|
| 25007-0024 | P22-DWG-09-009-002 | Piping and Instrumentation Diagram | C | **2 — Approved as Noted** |
| 25007-0025 | P22-DWG-09-007-005 | Typical Installation Details of Power Works | B | **2 — Approved as Noted** |

**Overall Transmittal Verdict: 2 — APPROVED AS NOTED**

Both documents are accepted. The P&ID Rev C NOTE-01 (CIP Tank capacity annotation) and the Power Works Rev B NOTE-01 (grounding sizing basis) are to be resolved prior to IFC (Rev 0). NOTE-02 (Cable Tray Layout) and NOTE-03 (duct bank interface data) require dedicated submittals from BW Water prior to IFC.
