# P22-TM-09-000-007-0
# TECHNICAL REVIEW TRANSMITTAL N7
# SECOND STAGE RO BRINE MODULE — PD TALTAL

**Date:** 08-Mar-2026
**Submittal reviewed:** 25007-0014 (received 06-Mar-2026)
**Documents reviewed:** 4 engineering documents
**Transmittal Verdict: 3 — TO BE REVISED**

---

## 1. EXECUTIVE SUMMARY

- All four documents require revision. Verdict: **3 — To be Revised.**
- Control Philosophy specifies 30-minute UPS; ET requires 8 hours — direct contractual non-conformance.
- A/C Thermal Calculation: load inventory incomplete; n+1 configuration not stated in document.
- Piping Layout: CIP and dosing separated 11,150 mm — exceeds the 3.5 m consolidated footprint by 3×. Tie-In Layout is drawn over the non-conforming Piping Layout and must be redrawn after Rev B is accepted.
- Piping Layout: container shows a single hinged personnel door on the lateral face; the required lateral sliding door and the equipment access door (sized for the largest installed item, 110° outward opening) are absent — two distinct ET — Container requirements not addressed.
- Two prior items related to this delivery remain open: Modbus TCP Memory Map (65 days, TM N2) and IO List update (44 days, TM N3).
- Control Philosophy does not describe energy consumption metering (CEE/MVE) — contractual performance guarantee (ET — Performance Guarantees) cannot be verified without this instrument.
- Control Philosophy declares 4-20mA as the sole field protocol; Control Architecture Rev B includes an Ethernet/IP field network not acknowledged in the Philosophy. HART protocol, required by ET — Instrumentation Specification, is also absent.
- Control Philosophy Section 3.3.3 defines two individual tank-level DI signals from the client, inconsistent with the correct interface: a single general enable DI from ADASA (consolidating all external conditions) plus one module status DO. Rev B must correct the interface definition and assign both signals in IO List Rev B.
- HP Pump start permissive checks only instrument health (PIT-09-001 NOT FAULT) with no minimum process pressure threshold; if ADASA delivers insufficient feed pressure the PLC will start the pump regardless, risking cavitation.
- Piping Layout: control/power cabinet shown as physically separated from the module. BW Water must clarify the integration plan and FAT testing procedure for the separated cabinet.

---

## 2. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| Submittal | 25007-0014 |
| Delivery date | 06-Mar-2026 |
| Review completion | 08-Mar-2026 |
| Total documents reviewed | 4 |
| Response codes summary | 4× Code 3 (To be Revised), 0× Code 2 |
| Contract | C-4300 BW WATER SUPPLY-12803 V2 |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 A/C Thermal Calculation Rev B — P22-CD-09-005-002
**Response Code: 3 — To be Revised**

Rev B adds VFD losses (absent in Rev A) and confirms the recommended unit size at 2.5 HP. Two issues prevent acceptance.

**Observation 1 — Incomplete thermal load inventory**

The calculation covers HP pump motor losses (4.26 kW) and VFD losses (1.70 kW) only. Control panel/PLC, instrumentation, antiscalant dosing equipment, and lighting are excluded without basis. Rev C must itemize all heat-generating equipment inside the container.

Technical Basis: Technical Offer Rev1 — A/C System, Section on Sizing Methodology; ET — Air Conditioning System

**Observation 2 — n+1 configuration not established in the calculation document**

The calculation recommends "a 2.5 HP air-conditioning unit." The Piping Layout shows two external A/C units. The calculation must explicitly state that the two-unit configuration is n+1 and that each 2.5 HP unit independently covers 100% of the verified load.

Technical Basis: ET — Air Conditioning System (n+1 requirement)

---

### 3.2 Piping Layout Rev A — P22-DWG-09-005-004
**Response Code: 3 — To be Revised**

The Piping Layout provides, for the first time, the physical arrangement of the complete module. Two major non-conformances prevent acceptance.

**Observation 1 — CIP and dosing equipment not consolidated in a single external footprint (MAJOR)**

Transmittal N5 OBS-01 established as a condition for acceptance that all CIP and dosing equipment must be arranged within a single external footprint with a maximum length of 3.5 meters. The CIP system (TK-09-001, BH-09-002, REL-09-001, FIL-09-002) is shown in Section 2-2 at one end of the module; the antiscalant dosing system (TK-09-002, BDS-09-001/002) is in Section 3-3 at the opposite end. The separation equals the full module length of 11,150 mm — more than 3× the permitted footprint. Two external A/C units are shown in Sheet 4 (n+1 physically confirmed).

Required action: Piping Layout Rev B must consolidate all external CIP and dosing equipment within a single external sector, footprint ≤ container width × 3.5 m, aligned to the side specified in ADASA's Transmittal N5 markup.

Technical Basis: Transmittal N5 Rev 1 — OBS-01 (CIP and Anti-Scalant Dosing External Footprint)

**Observation 2 — Antiscalant and CIP connections at module boundary must be flanged**

The antiscalant supply and injection connections (AS-PVC-DN25-09-031 and AS-PVC-DN15-09-035) are module boundary interfaces and therefore tie-in points. Per Transmittal N5, all process connections at the module boundary must be terminated with flanges. BW Water must confirm flanged termination for all antiscalant and CIP make-up connections at the module boundary in Piping Layout Rev B.

Technical Basis: Transmittal N5 — Module Boundary Connection Requirements

**Observation 3 — Container lateral access: sliding door not shown; equipment access door absent (MAJOR)**

The lateral view of the container shows a single hinged door at 900 mm × 2,200 mm — adequate only for personnel access. Two additional door requirements from ET — Container are not addressed in the current revision:

**(a) Equipment access door missing.** ET — Container requires a dedicated door with dimensions sufficient to allow entry and removal of the largest equipment installed inside the container. This door must open at a minimum angle of 110° toward the exterior. No such door appears in the Piping Layout.

**(b) Lateral sliding door not shown.** ET — Container states that the container must guarantee lateral access by means of a sliding door. The door shown in the lateral view is a conventional hinged door, not a sliding door. This is a distinct requirement from the personnel, equipment, and emergency doors.

Required action: Piping Layout Rev B must show all four required door types — personnel (900×2,200 mm), equipment (dimensioned to largest installed item, 110° outward opening), emergency, and lateral sliding — with their respective positions on the container perimeter.

Technical Basis: ET — Container (access doors and lateral sliding door requirement)

**Note — Missing elevation view showing process connection positions**

No elevation view is included to show the position of all process tie-in points along the module perimeter. An elevation view identifying all process connections (antiscalant, feed, permeate, concentrate, CIP) with relative positions is required for field installation planning. Include in Piping Layout Rev B.

**Observation 4 — Control/power cabinet shown separated from module (MAJOR)**

The Piping Layout shows the control and power cabinet as a physically separated unit from the module container. All power and communication cables from module equipment must be connected to this cabinet. BW Water must clarify: (a) whether the cabinet will be permanently integrated into the module structure or installed separately at site, (b) the cable routing arrangement, and (c) how factory acceptance testing (FAT) will be conducted with the cabinet separated from the module.

Required action: Piping Layout Rev B must show the cabinet mounting arrangement, cable routing, and the integration method between the cabinet and the module.

Technical Basis: ET — Control and Automation System; FAT inspection protocol

---

### 3.3 Tie-In Point Layout Rev A — P22-DWG-09-005-005
**Response Code: 3 — To be Revised**

This document cannot be accepted in its current revision. Its content is directly dependent on the Piping Layout Rev A, which does not conform to the layout requirement established in Transmittal N5 OBS-01.

**Observation 1 — Tie-In Point document has a direct dependency on the non-conforming Piping Layout (MAJOR)**

The antiscalant tie-in points (N°1 and N°2) reflect the position of the dosing system in the non-conforming Piping Layout Rev A. Once the Piping Layout consolidates CIP and antiscalant dosing within a single footprint, these tie-in positions will change. Required action: Submit Tie-In Point Rev B after Piping Layout Rev B is accepted. Rev B must reflect the consolidated layout, complete tie-in N°1 (tag, P&ID reference, flange standard), and include an elevation view showing the position and elevation of all connection flanges.

**Observation 2 — Make-up water connection for external CIP not shown (NOTE)**

The Piping Layout shows a Make-up CIP line (CP-PVC-DN80-09-019) with no corresponding battery-limit tie-in. BW Water must confirm whether CIP make-up water is supplied from an external source or from the module's own permeate stream.

**Note 1 — Tie-in N°1 incomplete**

The DN15 antiscalant connection has no tag, no P&ID reference, and no flange standard. These fields must be completed in the next revision.

**Note 2 — Design pressure at brine feed tie-in**

Tie-in N°3 (TP-DA, P8-001, Feed DN100, ANSI 150#) requires confirmation that the SWRO brine arrives at the module battery limit at a pressure compatible with ANSI 150# rating (≤19.6 bar at operating temperature). BW Water should state the design pressure at this interface.

---

### 3.4 Control Philosophy Rev A — P22-BT-09-009-001
**Response Code: 3 — To be Revised**

First submission of the Control Philosophy. Nine issues require revision before acceptance. Three trace directly to IO List observations in Transmittal N3, pending 44 days without a revised IO List being submitted.

**Observation 1 — UPS autonomy: 30 minutes specified vs. 8 hours required (CRITICAL)**

The document states: "The UPS will provide 30 minutes of power to ensure the controls and instrumentation do not shutdown." ET — Control and Automation System requires a minimum **8 hours** of UPS autonomy after a grid power interruption. The 30-minute figure is a 16-fold shortfall. BW Water must confirm an 8-hour UPS in Rev B and provide the supporting capacity calculation.

Technical Basis: ET — Control and Automation System (minimum 8-hour UPS autonomy)

**Observation 2 — Instrument tag discrepancy (VE-07-014 vs. VE-09-014)**

The Feed Preparation System Instruments table lists the antiscalant valves as **VE-07-014** and **VE-07-016**; the Process Description references the same valves as **VE-09-014** and **VE-09-016**. Area codes 07 and 09 represent distinct project areas. This inconsistency must be resolved consistently with the Valve List and P&ID.

**Observation 3 — Modbus TCP/IP interface not addressed**

The Control Philosophy does not reference the Modbus TCP/IP interface required for integration with the plant SCADA. The Control Philosophy must at minimum acknowledge this interface and confirm it is within module scope. The detailed architecture and variable mapping belong in the Modbus TCP Memory Map (outstanding since Transmittal N2, 65 days) and the IO List.

Technical Basis: ET — Communication and Control System (Modbus TCP/IP)

**Observation 4 — "BT" document type code not defined in project coding system**

The code P22-BT-09-009-001 uses "BT," which is not defined in the project coding standard. Defined type codes include ET, DWG, LI, CD, TM, CT, and IT. BW Water should assign a standard type code or formally define "BT" in the project document register.

**Observation 5 — Motor temperature monitoring not described (CRITICAL)**

No continuous motor temperature monitoring is described for the HP Pump or CIP Pump motors. TE09-001-XB001 and TE09-002-XB001 are temperature switches (DI), not Pt-100 transmitters (AI). ET requires Pt-100 sensors in the windings and bearings of all motors. Rev B must describe the AI motor temperature inputs, specify whether PT-100 sensors are wired to RTD inputs or analog AI inputs on the PLC (both comply with ET — Motors and Electrical Equipment), alarm setpoints, and their role in motor protection logic.

Technical Basis: ET — Motors and Electrical Equipment (Pt-100 windings and bearings, all motors); TM N3 OBS-01 — 44 days pending

**Observation 6 — DO Module Status output absent**

No discrete output reporting the operational state of the module to external systems is defined. Transmittal N3 OBS-04 requested this signal (0 = stopped; 1 = in operation) — 44 days pending. Rev B must describe this DO and include it in IO List Rev B.

Technical Basis: TM N3 OBS-04 — 44 days pending; ET — Communication and Control System

**Observation 7 — General module enable DI incomplete**

The Control Philosophy describes two product permissives (permeate tank permissive and off-spec tank permissive) but not a general module enable. Transmittal N3 OBS-05 requested a dedicated DI (1 = module may operate; 0 = module must stop) allowing the SWRO plant to inhibit module start-up or force a controlled shutdown independently of tank levels. Rev B must incorporate this signal in the control logic and in IO List Rev B.

Technical Basis: TM N3 OBS-05 — 44 days pending

**Note — Companion documents not yet submitted**

The Control Philosophy explicitly references two companion documents as "SEPARATE DOCUMENT": the Operating Sequence Chart and the Alarm and Control Setpoint List. BW Water should provide a committed delivery date for both.

**Observation 8 — HMI screen design standard not declared (ISA 101) (MAJOR)**

The document establishes an internal color coding scheme for equipment states and measured values. The scheme is broadly consistent with conventional practice but is presented without reference to a normative standard. ET — Control and Automation System requires HMI screens to comply with ISA 101 as the design standard, a requirement reiterated in the FAT inspection protocol. Rev B must formally declare ISA 101 compliance and confirm that screen layout, alarm presentation, navigation hierarchy, and color conventions all conform to that standard.

Technical Basis: ET — Control and Automation System (HMI ISA 101 requirement)

**Observation 9 — Energy consumption metering absent: CEE indicator and MVE not described (CRITICAL)**

The Control Philosophy contains no reference to energy metering. ET — Control and Automation System requires an Electrical Variables Meter (MVE) — connected to the PLC and accessible from the HMI — that continuously displays voltage, current, and power, and from which the Specific Energy Consumption (CEE, in kWh/m³) is derived as total electrical consumption divided by net permeate volume produced. The CEE is a contractual performance guarantee (< 4.8 kWh/m³ for TDS 43,000–48,000 mg/l; < 5.0 kWh/m³ for TDS 48,000–53,000 mg/l per ET — Performance Guarantees) and the basis for acceptance of the Performance Test. Without this instrument, the performance guarantee cannot be verified during commissioning. Rev B must describe the MVE, its PLC integration, the CEE calculation, the HMI display screen, and any alarm setpoints associated with energy performance.

VFD-driven loads (HP Pump, CIP Pump) are currently controlled with discrete and 4-20mA signals — no individual power measurement is available per load. A dedicated MVE is therefore required. Rev B must confirm that the CEE calculation is active in the PLC and that the resulting value is permanently displayed on an HMI screen.

Technical Basis: ET — Control and Automation System (MVE and CEE display); ET — Performance Guarantees (CEE contractual limit)

**Note — Digital Power Meter committed in CCS but absent from BOM**

Control Architecture Consolidated Comment Sheet (CCS) Comment 3 confirms that the LCP includes a Digital Power Meter with Modbus TCP/IP protocol, distinct from the process chemistry ANALYZER (pH/ORP/conductivity, 4-20mA) shown in the architecture diagram. Despite being committed in the CCS response, this instrument does not appear in the Control Architecture Rev B Bill of Materials (items 1–11). BW Water must formally include the MVE in the Control Architecture BOM and submit the instrument datasheet.

**Observation 10 — Communication protocol inconsistency: 4-20mA only vs. Ethernet/IP in Architecture; HART not declared (MAJOR)**

Two protocol gaps require resolution:

**(a) Ethernet/IP field network undeclared in Control Philosophy.** Control Architecture Rev B (P22-CD-09-004-001) includes a PROSOFT PLX32-EIP-MBTCP gateway and Ethernet/IP cabling to field devices, indicating that at least some field devices communicate via Ethernet/IP rather than hardwired 4-20mA or discrete I/O. The Control Philosophy describes only 4-20mA analog inputs and 24 VDC discrete I/O — no Ethernet/IP field network is mentioned. Rev B must include a complete signal philosophy table that identifies, for each device type, the physical communication medium (hardwired 4-20mA, 24 VDC DI/DO, or Ethernet/IP) and reconcile this with the Control Architecture drawing.

**(b) HART protocol not declared despite ET requirement.** ET — Instrumentation Specification requires 4-20mA + HART for all field instrumentation. The Control Philosophy specifies 4-20mA only, with no reference to HART. BW Water must confirm that all analog transmitters are HART-capable and state how the HART channel is used (diagnostics only, or active device management via the PLC or a HART multiplexer).

Technical Basis: ET — Instrumentation Specification (4-20mA + HART protocol); Control Architecture Rev B — P22-CD-09-004-001 (Ethernet/IP gateway and field cabling)

**Observation 11 — Client-side start permissive interface incorrectly defined as individual tank signals (MAJOR)**

Control Philosophy — Client Interface Permissive defines two hardwired DI signals from the client: "Permissive to fill Permeate Tank" and "Permissive to fill Off-Spec Tank." This approach is not consistent with the correct interface architecture for this project.

The module start permissive from the client side must be a single DI input to the BW Water PLC: a general module enable signal (1 = module may start; 0 = module must stop). ADASA will provide this signal from its own control system, consolidating all external conditions — downstream tank availability, SWRO plant readiness, and feed conditions — using ADASA's own instrumentation outside the module battery limit. The BW Water PLC does not require individual signals for each external condition.

Correspondingly, one DO output from the module PLC (to ADASA) must confirm module status (0 = stopped; 1 = in operation), so ADASA can coordinate its own systems.

Rev B must replace the two individual tank permissive DIs with a single general enable DI from ADASA and confirm that both signals are relay contacts: the ADASA enable DI is driven by a relay output from the ADASA PLC; the module status DO is a relay output from the BW Water PLC. IO List Rev B must assign both signals.

Technical Basis: ET — Communication and Control System; IO List Rev A — interface signal architecture between module PLC and client control system

**Observation 12 — HP Pump start permissive has no minimum feed pressure threshold (MAJOR)**

Control Philosophy — HP Pumping System Permissive lists "Pump suction pressure NOT FAULT as indicated by PIT-09-001" as an HP Pump start permissive. This condition verifies only that the instrument is functional — it does not verify that the actual suction pressure meets a minimum process value. If ADASA delivers feed pressure below the design minimum at Tie-in 1 (ET — Module Supply Limits), the PLC will start the HP Pump regardless, risking pump cavitation and membrane damage. Rev B must define a Low Suction Pressure setpoint (PSL-09-001) as a discrete start permissive, with the minimum threshold value derived from the pump hydraulic curve and confirmed in the Alarm and Control Setpoint List.

Technical Basis: ET — Module Supply Limits (Tie-in 1 feed pressure by BW Water offer); ET — High-Pressure Pumping System (cavitation protection); Control Philosophy Rev A — HP Pumping System Permissive

---

## 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

The following items from prior transmittals remain unresolved and have direct bearing on the documents reviewed in this transmittal.

| Item | Origin | Status | Days Open | Action Required |
|------|--------|--------|-----------|-----------------|
| Modbus TCP Memory Map | TM N2 | STILL PENDING | 65 | Immediate delivery date required. Integration planning is blocked without this document. |
| IO List update — Ethernet IP and digital stop signals | TM N3 | STILL PENDING | 44 | Include in next IO List revision. |

---

## 5. ATTACHMENTS

The following BW Water documents were reviewed as part of this transmittal. ADASA-annotated copies are attached:

| Attachment | Document | Rev |
|------------|----------|-----|
| Attachment 1 | P22-CD-09-005-002 — A/C Thermal Calculation | B |
| Attachment 2 | P22-DWG-09-005-004 — Piping Layout | A |
| Attachment 3 | P22-DWG-09-005-005 — Tie-In Point Layout | A |
| Attachment 4 | P22-BT-09-009-001 — Control Philosophy | A |

Documents available for download at: http://gofile.me/7k8qL/RHWabtKCE

---

## 6. RESPONSE SUMMARY

| Document | Code | Title | Rev | Response Code |
|----------|------|-------|-----|---------------|
| P22-CD-09-005-002 | CD | A/C Thermal Calculation | B | 3 — To be Revised |
| P22-DWG-09-005-004 | DWG | Piping Layout | A | 3 — To be Revised |
| P22-DWG-09-005-005 | DWG | Tie-In Point Layout | A | 3 — To be Revised |
| P22-BT-09-009-001 | BT | Control Philosophy | A | 3 — To be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED**
