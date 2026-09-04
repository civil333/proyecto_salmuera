---
titulo: "TECHNICAL REVIEW TRANSMITTAL N3"
subtitulo: "Second Stage RO Brine Module - Submittals 0007, 0008, 0009"
codigo: "P22-TM-09-000-003-0"
version: "DRAFT Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Gerencia Tecnica ADASA"
aprobado_por: "Pending"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# TECHNICAL REVIEW TRANSMITTAL N3

**Date:** January 28, 2026
**Project:** BAE 12803 - Second Stage RO Brine Module
**From:** ADASA - Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** DRAFT

---

## 1. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| **Transmittal Code** | P22-TM-09-000-003-0 |
| **Submittal 0007** | 25007-0007 (Jan-12-2026) - 6 documents |
| **Submittal 0008** | 25007-0008 (Jan-20-2026) - 12 documents |
| **Submittal 0009** | 25007-0009 (Jan-20-2026) - 5 documents |
| **Total Documents** | 23 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information |

---

## 2. EXECUTIVE SUMMARY

### 2.1 Key Findings

**TRANSMITTAL VERDICT: 3 - TO BE REVISED** (due to missing vibration transmitters in Instrument List)

| Validation Item | Status | Reference |
|-----------------|--------|-----------|
| Process Calculation BiTurbo modeling (43k & 53k TDS) | **VALIDATED** | 10 scenarios included |
| Permeate quality guarantee TDS < 500 mg/L | **VALIDATED** | < 248 mg/L worst case |
| Permeate chlorides < 400 mg/L | **VALIDATED** | < 146 mg/L worst case |
| Production rate 20 m3/h minimum | **VALIDATED** | 21 m3/h achieved |
| Recovery 42.86% | **VALIDATED** | Matches design |
| Equipment material compliance (Super Duplex) | **VALIDATED** | PREN 42.5 > 40 required |
| HART protocol on transmitters | **VALIDATED** | All transmitters 4-20mA + HART |
| Electrical documentation NEC/UL compliance | **VALIDATED** | All cables and conduits compliant |
| Conductivity instrumentation (5 locations) | **VALIDATED** | ET 5.5.5 vs IL - 5/5 covered |
| Flow instrumentation (5 locations) | **TAG ISSUE** | FIT-09-001 duplicate |

**Statistics:** 13 Approved (57%) | 5 Approved as noted (22%) | 5 To be revised (22%) | 0 Missing document (0%)

### 2.2 Remaining Critical Observations

| # | Observation | Document | Severity |
|---|-------------|----------|----------|
| 1 | **Missing vibration transmitters:** Instrument List does not include vibration transmitters for HP Pump (BH-09-001), Feed Turbocharger (SIP-09-001), and Interstage Turbocharger (SIP-09-002) as required by ET Section 5.5.7 (L1390-1394) | Instrument List | **HIGH** |
| 2 | **SEC calculation incomplete:** Process Calculation does not include explicit SEC calculation for complete system considering turbocharger energy recovery to demonstrate compliance with guaranteed 4.71 kWh/m3 | Process Calculation | **MEDIUM** |
| 3 | **Low pressure margin:** Line DA-SSD-DN80-09-005 (1st Stage Reject) has only 3% margin between operating pressure (68 bar) and design pressure (70 bar) | Line List | **MEDIUM** |
| 4 | **High cartridge flow rate:** RO pre-filter unit flow rate of 4.08 m3/h per cartridge (49 m3/h / 12 cartridges) exceeds recommended values. Consider increasing cartridge quantity to reduce unit flow to ~2 m3/h for extended cartridge life and improved membrane protection | Cartridge Filter | **MEDIUM** |
| 5 | **CRITICAL - Duplicate TAG FIT-09-001:** Instrument List assigns same TAG to two different flow transmitters (Line 4: Cartridge Filter DN100 vs Line 13: 2nd Stage Permeate DN50). Makes PLC addressing impossible | Instrument List | **CRITICAL** |
| 6 | **Missing Pt-100 in HP Pump motor windings:** Datasheet specifies RTDs for bearings but does NOT include Pt-100 for motor windings as required by ET Section 5.3 (L1032-1033). Motor is 87 kW with VFD | HP Pump Datasheet | **CRITICAL** |
| 7 | **CIP Pump missing RTDs in bearings:** No datasheet delivered for CIP Pump. ET Section 5.1.4 (L581) requires "RTDs a 3 hilos para rodamientos" | Missing document | **CRITICAL** |
| 8 | **CIP Pump missing Pt-100 in motor:** No temperature sensors specified for CIP Pump 15 kW motor windings and bearings per ET Section 5.3 | Missing document | **CRITICAL** |
| 9 | **Temperature switches instead of transmitters:** TE09-001-XB001 (HP Pump) and TE09-002-XB001 (CIP Pump) are digital switches (DI) providing only ON/OFF alarm, not analog transmitters with 4-20mA+HART as required by ET Section 5.5 | IO List | **MAJOR** |
| 10 | **Layout inherits duplicate TAG:** Instrument Location Layout shows duplicate FIT-09-001 in positions 4 and 13 (inherited from Instrument List). Layout also missing locations for vibration transmitters and motor Pt-100 sensors | Instrument Layout | **CRITICAL** |
| 11 | **CRITICAL - Manual valve DN100 ANSI 900#:** VM-09-015 (DN100 Butterfly) in HP Pump discharge line is specified MANUAL. ET Section 5.2.3 (L989-994) requires electric actuation for process valves in high-pressure systems. This is HP Pump main discharge at ~80 bar | Valve List | **CRITICAL** |
| 12 | **Duplicate TAGs in Valve List:** VE-09-008 appears twice (Item 44: DN80 900# vs Item 57: DN65 150#). VE-09-010 appears twice (Item 59: DN80 900# vs Item 109: DN15 150#). VM-09-015 appears twice (Item 18: DN100 vs Item 43: DN15). Makes valve identification impossible | Valve List | **MAJOR** |
| 13 | **TAGs with incorrect area code:** VM-07-005, VM-07-031, VE-07-009 use Area 07 instead of Area 09 | Valve List | **MINOR** |
| 14 | **Equipment List vs P&ID discrepancies:** Static Mixer TAG (MZE-09-009 vs MZE-09-001), CIP Tank capacity (6.1 vs 5.1 m3), Antiscalant Tank capacity (0.27 vs 0.25 m3), Dosing Pump capacity (2.3 vs 1 LPH) | Equipment List | **MINOR** |
| 15 | **Missing VFD electrical variables:** IO List does not include electrical variables from VFDs (HP Pump, CIP Pump) nor general electrical metering variables for SEC verification per ET Section 5.6 | IO List | **CRITICAL** |
| 16 | **Missing DO for module status:** System requires digital output (DO) signal for external coordination: 0 = module stopped, 1 = module running. Allows external systems to coordinate with module status | IO List | **CRITICAL** |
| 17 | **Missing DI for external enable:** System requires digital input (DI) signal for external enable: 1 = module can start/run, 0 = module must stop. Allows plant-level control to enable/disable module | IO List | **CRITICAL** |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 Process Calculation (P22-CD-09-009-001-B) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | SEC Calculation | Process Calculation does not include explicit SEC calculation for complete system considering turbocharger energy recovery. Recommend including system SEC to demonstrate compliance with guaranteed 4.71 kWh/m3 | OPEN |
| OBS-02 | Pressure margin | Pressure margin at 2nd stage is only 6% (84.81 bar operation vs 90 bar design). Noted for severe fouling conditions | OPEN (minor) |

**Validation Summary:**
- Feed TDS Range: 43,000 - 53,000 mg/L - COMPLIANT
- Permeate TDS: < 248 mg/L (worst case) - COMPLIANT
- Permeate Chlorides: < 146 mg/L (worst case) - COMPLIANT
- Production Rate: 21 m3/h - COMPLIANT
- BiTurbo Modeling: 10 scenarios included - COMPLIANT

### 3.2 RO HP Pump (P22-ET-09-009-002-B) - TO BE REVISED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Drawing status | Dimensional drawing marked as "Preliminary - Not Suitable for Construction". Final version required for fabrication | OPEN (minor) |
| **OBS-02** | **Missing Pt-100 motor windings** | Datasheet includes "3-wire RTDs for bearing temperature" but does NOT specify Pt-100 sensors for motor windings. ET Section 5.3 (L1032-1033) requires: "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos." Motor is ABB 125 HP (87 kW) with VFD - thermal protection of windings is critical | **OPEN (CRITICAL)** |
| OBS-03 | RTD type confirmation | Confirm that RTDs provided are Pt-100 type (100 ohms @ 0C) as required by ET Section 5.3 | OPEN |

**Verdict changed from APPROVED to TO BE REVISED** due to missing motor winding temperature protection.

### 3.3 Antiscalant Dosing Pump (P22-ET-09-009-004-B) - APPROVED

No observations. Document fully complies with ET requirements.

### 3.4 CIP Tank (P22-ET-09-009-009-B) - APPROVED

No observations. Document fully complies with ET requirements.

### 3.5 Chemical Consumption List (P22-LI-09-009-002-A) - APPROVED

No observations. Document fully complies with ET requirements.

### 3.6 Line List (P22-LI-09-009-003-A) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Pressure margin | Line DA-SSD-DN80-09-005 (1st Stage Reject) has very low margin (3%) between operating pressure (68 bar) and design pressure (70 bar). Consider increasing design pressure to 80 bar for additional safety margin | OPEN |

### 3.7 PFD (P22-DWG-09-009-01-B) - APPROVED

No observations. Document fully complies with ET requirements.

### 3.8 RO Container (P22-ET-09-000-001-B) - APPROVED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Door dimensions | Container datasheet does not specify exact personnel door dimensions. ET requires minimum 0.9m x 2.2m. Confirm compliance | OPEN (minor) |

### 3.9 RO Cartridge Filter (P22-ET-09-009-005-B) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Cartridge flow rate | Unit flow rate of 4.08 m3/h per cartridge (49 m3/h / 12 cartridges) is high. Consider increasing cartridge quantity to reduce unit flow to ~2 m3/h per cartridge for extended cartridge life and improved membrane protection | OPEN |

1 micron rating complies with ET requirements.

### 3.10 Feed Turbocharger (P22-ET-09-009-007-B) - APPROVED

No observations. Super Duplex SS 2507 (PREN 42.5) exceeds ET requirement of PREN > 40.

### 3.11 Interstage Turbocharger (P22-ET-09-009-008-B) - APPROVED

No observations. Super Duplex SS 2507 (PREN 42.5) exceeds ET requirement of PREN > 40.

### 3.12 CIP Tank Heater (P22-ET-09-009-011-B) - APPROVED

No observations. SS316 wetted parts comply with ET requirements.

### 3.13 Grounding Layout (P22-DWG-09-007-003-A) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Scale | Layout is NTS (Not To Scale). Recommend issuing version with defined scale and dimensions for construction | OPEN (minor) |

### 3.14 Equipment List (P22-LI-09-005-001-A) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | TAG discrepancy | Static Mixer: Equipment List uses MZE-09-009, P&ID uses MZE-09-001. Unify TAG | OPEN (minor) |
| OBS-02 | Capacity discrepancies | Minor differences between Equipment List and P&ID: CIP Tank (6.1 vs 5.1 m3), Antiscalant Tank (0.27 vs 0.25 m3), Dosing Pump (2.3 vs 1 LPH). Confirm correct values | OPEN (minor) |

**Verdict changed from APPROVED to APPROVED AS NOTED** due to TAG and capacity discrepancies with P&ID.

### 3.15 Valve List (P22-LI-09-005-002-A) - TO BE REVISED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| **OBS-01** | **Manual valve DN100 ANSI 900#** | VM-09-015 (DN100 Butterfly, CE3MN, ANSI 900#) in SWRO HPP system is specified with MANUAL actuation. This is HP Pump discharge line at ~80 bar operating pressure. ET Section 5.2.3 (L989-994) states: "Todas las valvulas de proceso relevantes, tanto en sistemas de alta como baja presion, deberan contar con actuacion electrica". DN100 on main process line qualifies as "relevant" | **OPEN (CRITICAL)** |
| **OBS-02** | **Duplicate TAG VM-09-015** | TAG VM-09-015 appears in Item 18 (DN100 Butterfly) and Item 43 (DN15 Ball). Two different valves with same TAG | **OPEN (MAJOR)** |
| **OBS-03** | **Duplicate TAG VE-09-008** | TAG VE-09-008 appears in Item 44 (DN80 ANSI 900#, CE3MN) and Item 57 (DN65 ANSI 150#, DI/SS420). Different ratings and materials with same TAG | **OPEN (MAJOR)** |
| **OBS-04** | **Duplicate TAG VE-09-010** | TAG VE-09-010 appears in Item 59 (DN80 ANSI 900#) and Item 109 (DN15 ANSI 150#). Two different valves with same TAG | **OPEN (MAJOR)** |
| OBS-05 | TAGs with incorrect area | VM-07-005 (should be VM-09-005), VM-07-031 (should be VM-09-031), VE-07-009 (should be VE-09-009). Area code 07 is incorrect for module 09 | OPEN (minor) |
| OBS-06 | Manufacturers | Valve "Brand" column indicates "TBA" (To Be Advised) for all 109 valves. Confirm selected manufacturers before procurement | OPEN (minor) |

**Verdict changed from APPROVED to TO BE REVISED** due to:
- Critical: VM-09-015 manual actuation violates ET 5.2.3 for high-pressure process valves
- Major: Three duplicate TAGs make valve identification impossible (VM-09-015, VE-09-008, VE-09-010)

**Cross-Reference Analysis:** See Attachment J for complete Valve List vs P&ID vs ET 5.2.3 analysis.

### 3.16 IO List (P22-LI-09-008-001-A) - TO BE REVISED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Temperature switches | TE09-001-XB001 (HP Pump) and TE09-002-XB001 (CIP Pump) are configured as digital inputs (DI) with dry contact N.O. This indicates they are temperature switches (TSH) providing only ON/OFF alarm, not continuous temperature monitoring. ET Section 5.5 requires 4-20mA + HART protocol for instrumentation. **Additionally, temperatures must be connected to PLC for continuous monitoring and HMI screens must display real-time temperatures and trending for predictive maintenance** | OPEN |
| **OBS-02** | **Missing fieldbus variables list** | IO List does not include variables to be controlled via fieldbus (Modbus/Ethernet). BW Water to provide separate list with all fieldbus variables including names, addresses, and data types | **OPEN (MAJOR)** |
| **OBS-03** | **Missing VFD electrical variables** | IO List does not include electrical variables from VFDs (HP Pump, CIP Pump) nor general electrical metering variables for the system. ET Section 5.6 requires energy monitoring for SEC calculation verification | **OPEN (CRITICAL)** |
| **OBS-04** | **Missing DO for module status** | System requires a digital output (DO) signal for external coordination: 0 = module stopped, 1 = module running. This allows external systems (feed pump, reject disposal) to coordinate with module status | **OPEN (CRITICAL)** |
| **OBS-05** | **Missing DI for external enable** | System requires a digital input (DI) signal for external enable: 1 = module can start/run, 0 = module must stop. This allows plant-level control system to enable/disable module operation | **OPEN (CRITICAL)** |

**Verdict changed from APPROVED AS NOTED to TO BE REVISED** due to missing external coordination signals and VFD electrical variables.

All transmitters include 4-20mA + HART as required.

### 3.17 I&C Cable Schedule (P22-LI-09-008-002-A) - APPROVED

No observations. Document fully complies with ET requirements.

### 3.18 Instrument List (P22-LI-09-008-003-A) - TO BE REVISED

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| **OBS-01** | Vibration transmitters | Instrument List does not include vibration transmitters for HP Pump (BH-09-001), Feed Turbocharger (SIP-09-001), and Interstage Turbocharger (SIP-09-002). ET Section 5.5.7 requires vibration monitoring | **HIGH** |
| **OBS-02** | **CRITICAL: Duplicate TAG FIT-09-001** | TAG FIT-09-001 appears twice with different specifications: Line 4 (Cartridge Filter Discharge, DN100, 0-100 m3/h) and Line 13 (2nd Stage Permeate, DN50, 0-18 m3/h). Unique TAG identification impossible for PLC | **CRITICAL** |
| OBS-03 | Missing instruments vs IO List | CIT-09-006 (Interstage Turbocharger Conductivity) and FIT-09-002 (2nd Stage Permeate Flow) appear in IO List but are absent from Instrument List | HIGH |
| OBS-04 | TAG discrepancy LIT-09-001 vs LIT-09-002 | CIP Tank Level Transmitter: Instrument List uses LIT-09-001 but IO List uses LIT-09-002 for same physical instrument | HIGH |
| OBS-05 | Transmitters without I/O signals | PIT-09-005 (2nd Stage Feed Pressure), CIT-09-004 (1st Reject Conductivity), TIT-09-001 (CIP Temperature) are listed with 4-20mA output but have no corresponding AI entries in IO List | HIGH |
| OBS-06 | P&ID nomenclature inconsistency | P&ID uses AIT for analyzers, Instrument List uses specific types (ORPIT, CIT). Acceptable but recommend documenting equivalence | MINOR |
| OBS-07 | DPS type not in ADASA standard | DPS-09-001 (Differential Pressure Switch) uses type code not defined in P00-IT-00-000-101 Table 3-3 | MINOR |
| OBS-08 | Missing pump temperature sensors | Instrument List only includes TIT-09-001 (CIP Tank). Temperature sensors for HP Pump and CIP Pump (TE09-001, TE09-002) are not listed. Document should include all temperature instrumentation or clarify scope exclusion | MINOR |
| OBS-09 | CIT-09-002 range vs TDS guarantee | CIT-09-002 range is 0-200 uS/cm (~0-140 mg/L TDS). ET Section 10.1 guarantees TDS <= 500 mg/L (~700-1000 uS/cm). If permeate operates near guarantee limit, instrument would be OUT OF RANGE. BW Water to confirm range is adequate for expected operating conditions | REVIEW |

**Action Required:** Eliminate duplicate TAGs, add missing instruments, reconcile TAGs with IO List, include vibration transmitters, clarify pump temperature sensor documentation. Cross-reference analysis available in Attachment G.

### 3.18.1 Conductivity and Flow Instrumentation Compliance

**Reference:** Detailed analysis in Attachment K (P22-CD-09-008-001-0)

#### Conductivity (ET Section 5.5.5) - COMPLIANT

| # | ET Requirement | Proposal Item | TAG IL | IL Description | Complies |
|---|----------------|---------------|--------|----------------|----------|
| 1 | Feed to module | - | CIT-09-001 | RO Cartridge Filter Discharge | **YES** |
| 2 | Permeate outlet | Item 16 | CIT-09-002 | RO Train Permeate | **YES** |
| 3 | 2nd stage permeate | - | CIT-09-003 | RO Stage 2 Permeate | **YES** |
| 4 | 1st stage reject | - | CIT-09-004 | RO Stage 1 Reject | **YES** |
| 5 | Final reject | - | CIT-09-005 | RO Train Reject | **YES** |

**Result:** 5/5 locations covered. Instrument List COMPLIES with ET conductivity requirements.

#### Flow (ET Section 5.5.1) - TAG ISSUE

| # | ET Requirement | Proposal Item | TAG IL | IL Description | Complies |
|---|----------------|---------------|--------|----------------|----------|
| 1 | Feed to module | - | FIT-09-001 | RO Cartridge Filter Discharge | **YES** |
| 2 | 2nd stage permeate | Item 14 | FIT-09-001 | RO 2nd Stage Permeate | **DUPLICATE** |
| 3 | Permeate outlet | Item 13 | FIT-09-003 | RO Train Permeate | **YES** |
| 4 | Final reject | Item 15 | FIT-09-004 | RO Train Reject | **YES** |
| 5 | CIP filter outlet | Item 33 | FIT-09-005 | CIP Pump Discharge | **YES** |

**Result:** 5/5 locations covered BUT FIT-09-001 TAG is duplicated. See OBS-02 above.

### 3.19 Power & Control Cable (P22-ET-09-007-002-A) - APPROVED

No observations. Conductor material, voltage rating, and insulation comply with ET requirements.

### 3.20 Cable Tray (P22-ET-09-007-003-A) - APPROVED

No observations. IEC 61537 and NEMA VE1/VE2 compliance confirmed.

### 3.21 Conduit & Flexible (P22-ET-09-007-004-A) - APPROVED

No observations. UL Listed and NEC Article 356 compliance confirmed.

### 3.22 Instrument Location Layout (P22-DWG-09-008-001-A) - TO BE REVISED

**Layout Summary:**
| Location | Instruments | Description |
|----------|-------------|-------------|
| Inside Container (40 ft) | 22 | RO Skid: Cartridge Filter, HP Pump, Stage 1, Stage 2, Turbochargers |
| Outside Container | 10 | CIP System (7) + Antiscalant (3) |
| **Total Documented** | **32** | Matches Instrument List count |
| **Missing per ET** | **9+** | 3 vibration + 6 Pt-100 motor sensors |

| # | Code | Observation | Status |
|---|------|-------------|--------|
| **OBS-01** | **Duplicate TAG FIT-09-001** | Layout inherits duplicate TAG from Instrument List: FIT-09-001 appears in positions 4 (Cartridge Filter DN100) and 13 (2nd Stage Permeate DN50). PLC addressing impossible | **CRITICAL** |
| **OBS-02** | **Missing vibration transmitters** | Layout does not show locations for vibration transmitters on HP Pump (BH-09-001), Feed Turbocharger (SIP-09-001), and Interstage Turbocharger (SIP-09-002) per ET Section 5.5.7 (L1390-1394) | **CRITICAL** |
| **OBS-03** | **Missing Pt-100 motor sensors** | Layout does not include locations for Pt-100 temperature sensors in HP Pump (87 kW) and CIP Pump (15 kW) motors per ET Section 5.3 (L1032-1033). Affects: 3 windings + 2 bearings HP Pump, 1 winding CIP Pump | **CRITICAL** |
| OBS-04 | Missing CIT-09-006 | Interstage Turbocharger Inlet Conductivity (CIT-09-006) appears in IO List but not in Layout | MAJOR |
| OBS-05 | TAG discrepancy LIT | CIP Tank Level: Layout uses LIT-09-001, IO List uses LIT-09-002 | MAJOR |
| OBS-06 | Scale | Layout is NTS (Not To Scale). Recommend issuing version with defined scale | MINOR |

**Verdict changed from APPROVED AS NOTED to TO BE REVISED** due to duplicate TAG and missing instrument locations.

**Cascade Impact:** Layout corrections depend on prior correction of Instrument List (FIT-09-001→FIT-09-002) and inclusion of vibration/temperature instruments in documentation chain (P&ID→IL→IO→Layout).

**Cross-Reference Analysis:** See Attachment I for complete Layout vs Instrument List vs IO List vs ET requirements cross-reference.

### 3.23 Power Cable Schedule (P22-LI-09-007-002-A) - APPROVED

No observations. Voltage drop < 3% all circuits as required.

---

## 4. REQUIRED ACTIONS - BW WATER

### 4.1 Critical Actions (HIGH Priority)

**Group A: TAG Correction (Instrument List + Layout)**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 1 | **URGENT:** Eliminate duplicate TAG FIT-09-001 - Renumber 2nd Stage Permeate transmitter to FIT-09-002 per IO List | P22-LI-09-008-003-A | **PENDING** |
| 2 | **Update Layout with corrected TAGs:** After correcting Instrument List, update Instrument Location Layout to reflect FIT-09-002 in position 13 | P22-DWG-09-008-001-A | **PENDING** |
| 3 | **Unify LIT TAG:** Decide between LIT-09-001 (current in IL/Layout) or LIT-09-002 (IO List) and update all documents for CIP Tank Level | IL + IO List + Layout | **PENDING** |

**Group B: Vibration Instrumentation (ET 5.5.7)**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 4 | **Include vibration transmitters** for BH-09-001 (HP Pump), SIP-09-001 (Feed Turbocharger), and SIP-09-002 (Interstage Turbocharger) per ET Section 5.5.7 (L1390-1394) | P22-LI-09-008-003-A | **PENDING** |
| 5 | **Add vibration transmitter locations in Layout:** Include mounting locations for VT-09-001/002/003 on HP Pump and Turbochargers once instruments are specified | P22-DWG-09-008-001-A | **PENDING** |

**Group C: Pump Temperature Sensors (ET 5.3)**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 6 | **Confirm/include Pt-100 in HP Pump motor windings:** ET Section 5.3 (L1032-1033) requires Pt-100 for windings AND bearings. Current datasheet only specifies RTDs for bearings. ABB motor 87 kW requires winding protection | P22-ET-09-009-002 | **PENDING** |
| 7 | **Confirm RTD type is Pt-100:** Verify that RTDs in HP Pump datasheet are Pt-100 type (100 ohms @ 0C) per ET Section 5.3 specification | P22-ET-09-009-002 | **PENDING** |
| 8 | **Deliver CIP Pump datasheet with RTDs:** ET Section 5.1.4 (L581) requires "RTDs a 3 hilos para rodamientos". No datasheet currently exists for BH-09-002 | New document required | **PENDING** |
| 9 | **Confirm/include Pt-100 in CIP Pump motor:** ET Section 5.3 requires Pt-100 for motor windings and bearings. CIP Pump 15 kW motor currently has no specified temperature sensors | CIP Pump datasheet | **PENDING** |

### 4.2 Technical Actions (MEDIUM Priority)

| # | Action | Document | Status |
|---|--------|----------|--------|
| 10 | Include explicit SEC calculation for complete system considering turbocharger energy recovery, demonstrating compliance with guaranteed 4.71 kWh/m3 +/- 5% | P22-CD-09-009-001 | PENDING |
| 11 | Review design pressure of line DA-SSD-DN80-09-005 (1st Stage Reject) - currently 70 bar with only 3% margin. Consider increasing to 80 bar | P22-LI-09-009-003 | PENDING |
| 12 | Confirm personnel door dimensions for container (minimum 0.9m x 2.2m per ET 5.1.10) | P22-ET-09-000-001 | PENDING |
| 13 | Confirm selected valve manufacturers (currently "TBA") | P22-LI-09-005-002 | PENDING |
| 14 | Review cartridge filter configuration - consider increasing cartridge quantity to reduce unit flow from 4.08 m3/h to ~2 m3/h per cartridge for improved membrane protection | P22-ET-09-009-005 | PENDING |
| 15 | Add CIT-09-006 (Interstage Turbocharger Inlet Conductivity) to Instrument List and Layout with complete specifications | P22-LI-09-008-003-A + Layout | PENDING |
| 16 | Add AI entries in IO List for: PIT-09-005, CIT-09-004, TIT-09-001 (transmitters listed in IL without IO signals) | P22-LI-09-008-001-A | PENDING |
| 17 | **Evaluate temperature transmitters (TIT) for pumps:** Consider replacing temperature switches (TSH) with 4-20mA+HART transmitters for continuous monitoring and trending capability, or provide technical justification for switch-only configuration | IO List / IL | PENDING |

**Group D: Valve List Corrections (ET 5.2.3)**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 18 | **CRITICAL: Change VM-09-015 to MOTORIZED** actuation or provide technical justification why this DN100 ANSI 900# valve on HP Pump discharge is not "relevant for the process" per ET Section 5.2.3 | P22-LI-09-005-002 | **PENDING** |
| 19 | **Eliminate duplicate TAG VM-09-015:** Assign unique TAG to Item 43 (DN15 Ball valve in SWRO Reject 1st) | P22-LI-09-005-002 | **PENDING** |
| 20 | **Eliminate duplicate TAG VE-09-008:** Assign unique TAG to one of the valves (Item 44 or Item 57) | P22-LI-09-005-002 | **PENDING** |
| 21 | **Eliminate duplicate TAG VE-09-010:** Assign unique TAG to one of the valves (Item 59 or Item 109) | P22-LI-09-005-002 | **PENDING** |
| 22 | **Correct TAGs with wrong area code:** Change VM-07-005→VM-09-005, VM-07-031→VM-09-031, VE-07-009→VE-09-009 | P22-LI-09-005-002 | **PENDING** |

**Group E: Equipment List Corrections**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 23 | **Unify Static Mixer TAG:** Decide between MZE-09-009 (Equipment List) or MZE-09-001 (P&ID) and update accordingly | Equipment List / P&ID | **PENDING** |
| 24 | **Confirm capacities:** Resolve discrepancies CIP Tank (6.1 vs 5.1 m3), Antiscalant Tank (0.27 vs 0.25 m3), Dosing Pump (2.3 vs 1 LPH). Update document with incorrect values | Equipment List / P&ID | **PENDING** |

**Group F: Conductivity/Flow Instrumentation Analysis**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 25 | **Confirm 5 conductivity transmitters in contractual scope:** Technical Proposal lists only 1 conductivity transmitter (Item 16). Instrument List includes 5 (CIT-09-001 to CIT-09-005). Confirm all 5 are included in Contract C-4300 supply scope | Response letter | **PENDING** |
| 26 | **Confirm CIT-09-002 range adequacy:** Range 0-200 uS/cm covers ~0-140 mg/L TDS. If permeate quality approaches guarantee limit (500 mg/L TDS), instrument may be out of range. Confirm selection is appropriate for expected operating conditions | Response letter | **PENDING** |

**Group G: IO List Corrections (Coordination & Monitoring)**

| # | Action | Document | Status |
|---|--------|----------|--------|
| 27 | **Provide fieldbus variables list:** Submit separate document listing all variables to be controlled/monitored via fieldbus (Modbus TCP/Ethernet IP) including variable names, addresses, data types | New document | **PENDING** |
| 28 | **Include VFD electrical variables:** Add AI signals for VFD electrical parameters: voltage, current, power, frequency, motor temperature. Also include general power metering for SEC verification per ET Section 5.6 | P22-LI-09-008-001-A | **PENDING** |
| 29 | **Add DO for module status:** Include digital output signal for external coordination. DO=0 when module stopped (normal or fault), DO=1 when module running | P22-LI-09-008-001-A | **PENDING** |
| 30 | **Add DI for external enable:** Include digital input signal for external enable/permissive. DI=1 allows module to start/maintain operation, DI=0 requires module to stop | P22-LI-09-008-001-A | **PENDING** |
| 31 | **Include HMI temperature screens:** Provide HMI screen designs showing real-time pump/motor temperatures with trending capability for predictive maintenance | HMI Design | **PENDING** |

### 4.3 Completed Actions

| # | Action | Document | Completion |
|---|--------|----------|------------|
| A | Process Calculation with BiTurbo modeling (43k & 53k TDS) | P22-CD-09-009-001-B | Jan-12-2026 |
| B | Equipment datasheets with Super Duplex PREN > 40 | P22-ET-09-009-007/008-B | Jan-20-2026 |
| C | IO List with HART protocol | P22-LI-09-008-001-A | Jan-20-2026 |
| D | Electrical documentation NEC/UL compliance | P22-ET-09-007-002/003/004-A | Jan-20-2026 |

---

## 5. ATTACHMENTS

| # | Attachment | Description |
|---|------------|-------------|
| A | P22-LI-09-008-003-A_Instrument_List_Comments.pdf | Instrument List with ADASA review comments |
| B | P22-CD-09-009-001-B_Process_Calc_Comments.pdf | Process Calculation with ADASA annotations |
| C | P22-LI-09-009-003-A_Line_List_Comments.pdf | Line List with pressure margin observations |
| G | 2026-01-27_Revision-Tecnica-Instrument-List-Cruzada.pdf | Complete cross-reference analysis: Instrument List vs P&ID vs IO List vs ADASA coding standard |
| H | 2026-01-27_Revision-Tecnica-Temperatura-Bombas.pdf | Pump temperature measurement cross-reference: ET requirements vs delivered documentation for Pt-100 and RTDs |
| I | 2026-01-28_Revision-Tecnica-Instrument-Location-Layout.pdf | Layout cross-reference: 32 instruments vs Instrument List, IO List, and ET requirements |
| J | 2026-01-28_Revision-Tecnica-Cruzada-ValveList-EquipmentList.pdf | Valve List and Equipment List cross-reference: 109 valves vs P&ID, ET 5.2.3 actuacion electrica analysis, duplicate TAG identification |
| K | P22-CD-09-008-001-0_Informe-Conductividad-Caudal.pdf | Comparative analysis: Conductivity and Flow instrumentation - ET requirements vs Technical Proposal vs Instrument List. Includes 5/5 compliance matrices and range verification for performance guarantees |

**Download Link:** https://www.dropbox.com/t/tDInLROUqCSiQlYM

*Annotated PDFs with ADASA review comments to be attached in final transmittal.*

---

*Prepared by: ADASA - Aguas de Antofagasta S.A.*
*Date: January 28, 2026*
*Contract: C-4300 BW Water - BAE 12803*
*Status: DRAFT Rev.0 - Pending internal approval*
