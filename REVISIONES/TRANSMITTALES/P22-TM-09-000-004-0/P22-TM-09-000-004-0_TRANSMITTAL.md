---
titulo: "TECHNICAL REVIEW TRANSMITTAL N4"
subtitulo: "Second Stage RO Brine Module - Submittals 0010, 0011"
codigo: "P22-TM-09-000-004-0"
version: "Rev.1"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# TECHNICAL REVIEW TRANSMITTAL N4

## 1. EXECUTIVE SUMMARY

### 1.1 Key Findings

**TRANSMITTAL VERDICT: 3 - TO BE REVISED**

Two submittals reviewed with critical observations requiring immediate attention. The Utility Consumption List (E10) has persistent non-compliance with A/C n+1 requirements (30 days pending). The Cable Tray Layout (E11) inherits duplicate TAG FIT-09-001 from Instrument List and is missing instrument locations required by ET.

| Validation Item | Status | Reference |
|-----------------|--------|-----------|
| SEC (Specific Energy Consumption) | **VALIDATED** | 3.98 kWh/m3 vs 4.71 kWh/m3 guaranteed (15% margin) |
| Production rate 21 m3/h | **VALIDATED** | Matches design requirements |
| PLC frequency 50 Hz compliance | **REQUIRES CONFIRMATION** | ET 5.4.7 - Currently specified at 60 Hz |
| A/C n+1 configuration | **NOT COMPLIANT** | ET 5.1.11 - Only 1 unit specified (30 days pending) |
| A/C thermal calculation | **NOT DELIVERED** | ET 5.1.11 - Required document (30 days pending) |
| Antiscalant Tank material change | **ACCEPTED** | HDPE to LMDPE justified |
| PLC Allen Bradley compliance | **VALIDATED** | 5069-L320ER meets ET 5.4 |
| HMI 10" color touch | **VALIDATED** | PanelView Plus 7 2711P-T10C21D8S |
| Modbus TCP/IP Gateway | **VALIDATED** | PLX32-EIP-MBTCP installed |
| Modbus TCP Memory Map | **NOT DELIVERED** | 30 days pending (TM N2) |

**Statistics:** 0 Approved (0%) | 2 Approved as noted (50%) | 2 To be revised (50%)

### 1.2 Critical Observations

| # | Observation | Document | Severity | Status |
|---|-------------|----------|----------|--------|
| OBS-01 | **PLC specified at 60 Hz:** Utility List indicates PLC power supply as 220V/1PH/60Hz. ET Section 5.4.7 states equipment operating at frequencies other than 50 Hz will NOT be accepted. Chilean grid operates at 50 Hz. | Utility Consumption List | **CRITICAL** | NEW |
| OBS-02 | **A/C without n+1 configuration:** Only 1 A/C unit (2.64 kW) specified. ET 5.1.11 requires n+1 (minimum 2 units). Technical Offer committed "2 A/C (1W+1S)" with 5.28 kW total. | Utility Consumption List | **CRITICAL** | PENDING 30 DAYS |
| OBS-03 | **Missing A/C thermal calculation:** ET 5.1.11 (L757-759) requires thermal calculation document to determine A/C sizing based on equipment heat loads and site conditions. | Missing document | **CRITICAL** | PENDING 30 DAYS |
| OBS-04 | **Modbus TCP Memory Map not delivered:** BW Water committed "WILL SUBMIT I/O MODBUS LIST SEPARATELY" in response to TM N2 comment (Jan-26-2026). Document has NOT been delivered after 30 days. Critical for DCS integration. | Control Architecture | **CRITICAL** | PENDING 30 DAYS |
| OBS-05 | **Duplicate TAG FIT-09-001:** Cable Tray Layout inherits duplicate TAG from Instrument List. Items 4 (Cartridge Filter DN100) and 13 (2nd Stage Permeate DN50) have same TAG. PLC addressing impossible. | Cable Tray Layout | **CRITICAL** | PENDING 8 DAYS |
| OBS-06 | **Missing vibration transmitters:** Layout does not include locations for vibration transmitters on HP Pump (BH-09-001), Feed Turbocharger (SIP-09-001), and Interstage Turbocharger (SIP-09-002) per ET Section 5.5.7. | Cable Tray Layout | **CRITICAL** | PENDING 8 DAYS |
| OBS-07 | **Missing Pt-100 motor sensors:** Layout does not include locations for Pt-100 temperature sensors in HP Pump (87 kW) and CIP Pump (15 kW) motors per ET Section 5.3. | Cable Tray Layout | **CRITICAL** | PENDING 8 DAYS |
| OBS-08 | **HP Pump power inconsistency:** Four different values across documents: 93 kW (Utility List) vs 86 kW (Technical Offer) vs 92 kW (Equipment List) vs 83 kW (Load List). | Multiple documents | **MAJOR** | NEW |
| OBS-09 | **UPS not included in BOM:** Control Architecture BOM does not include UPS required by ET 5.4 (L1088-1089) with minimum 8 hours autonomy for control system. | Control Architecture | **MAJOR** | NEW |
| OBS-10 | **Container dimensions exceed approved 40ft configuration:** Cable Tray Layout shows elongated container suggesting 60ft (40ft + 20ft extension). ADASA rejected 60ft proposal on Nov 17, 2025 due to +USD $67,208 and +5 weeks impact. Container must conform to approved 40ft standard. | Cable Tray Layout | **CRITICAL** | NEW |

---

## 2. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| **Transmittal Code** | P22-TM-09-000-004-0 |
| **Submittal 0010** | 25007-0010 (Jan-30-2026) - 2 documents |
| **Submittal 0011** | 25007-0011 (Feb-03-2026) - 2 documents |
| **Total Documents** | 4 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information |

### Documents Reviewed

| # | Code | Title | Rev | Verdict |
|---|------|-------|-----|---------|
| 1 | P22-LI-09-009-001 | Utility Consumption List | A | **3 - To be revised** |
| 2 | P22-ET-09-009-010 | Datasheet of Antiscalant Dosing Tank | B | 2 - Approved as noted |
| 3 | P22-CD-09-004-001 | Control System Architecture | B | 2 - Approved as noted |
| 4 | P22-DWG-09-007-004 | Cable Tray Layout and Support Details | A | **3 - To be revised** |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 Utility Consumption List (P22-LI-09-009-001-A) - TO BE REVISED

#### 3.1.1 Document Information

| Field | Value |
|-------|-------|
| Code | P22-LI-09-009-001-A |
| Title | Utility Consumption List |
| Date | 21-Jan-2026 |
| Prepared | KOB / DCS |
| Revision | A (First issue) |

#### 3.1.2 Observations

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| **OBS-01** | **PLC Frequency** | The Utility Consumption List specifies PLC power supply as "220V/1PH/60Hz". ET Section 5.4.7 (Lines 1305-1308) states: "Para todos los equipos electricos se debe considerar una alimentacion electrica de operacion en 380 VAC/220 VAC, 50 Hz. **No se aceptaran equipos principales que operen en otros voltajes y frecuencias.**" Chilean electrical grid operates at 50 Hz. **ACTION:** If the PLC power supply is dual-frequency (50/60 Hz auto-ranging), please confirm this specification and document explicitly. If the PLC operates only at 60 Hz, replacement with 50 Hz compatible equipment is required. | **CRITICAL** |
| **OBS-02** | **A/C Configuration** | Only 1 A/C unit (2.64 kW) is specified. ET Section 5.1.11 (Lines 747-750) requires: "El proveedor debera considerar la cantidad y necesidad de unidades de aire acondicionado en cantidad **n+1**". Technical Offer Rev.1 Section 4 committed: "2 A/C (1W + 1S) are provided inside container" with total connected load of 5.28 kW. **This observation was first raised in Transmittal N2 (January 6, 2026) and remains unresolved after 30 days.** | **CRITICAL** |
| **OBS-03** | **Thermal Calculation** | ET Section 5.1.11 (Lines 757-759) requires: "Durante la ingenieria de detalles se debera entregar una **memoria de calculo termica** para determinar la cantidad del sistema de aire acondicionado". This document has not been delivered. **This observation was first raised in Transmittal N2 (January 6, 2026) and remains unresolved after 30 days.** | **CRITICAL** |
| **OBS-08** | **HP Pump Power** | Four different power values exist for HP Pump: Utility List (93 kW), Technical Offer (86 kW), Equipment List (92 kW), Electrical Load List (83 kW). This inconsistency affects SEC calculations and electrical system sizing. Unification required across all documents. | **MAJOR** |
| OBS-10 | **CIP Pump Power** | Utility List indicates 11 kW vs Technical Offer 15 kW. Difference of 4 kW (27%) is significant and requires clarification. | **MAJOR** |

#### 3.1.3 Positive Findings

| Item | Status | Details |
|------|--------|---------|
| **SEC Compliance** | **VALIDATED** | SEC = 3.98 kWh/m3 meets contractual guarantee of 4.71 kWh/m3 +/- 5% with favorable margin of 15% |
| **Electrical frequency (most equipment)** | **COMPLIANT** | HP Pump, CIP Pump, CIP Heater, Dosing Pump all specified at 50 Hz |
| **Production rate** | **VALIDATED** | 21 m3/h meets minimum 20 m3/h requirement |

#### 3.1.4 Verdict

| Aspect | Result |
|--------|--------|
| ET Compliance | **NOT COMPLIANT** (OBS-01, OBS-02, OBS-03) |
| Technical Offer Compliance | **NOT COMPLIANT** (OBS-02, OBS-08, OBS-10) |
| **FINAL VERDICT** | **3 - TO BE REVISED** |

---

### 3.2 Antiscalant Dosing Tank Datasheet (P22-ET-09-009-010-B) - APPROVED AS NOTED

#### 3.2.1 Document Information

| Field | Value |
|-------|-------|
| Code | P22-ET-09-009-010-B |
| Title | Datasheet of Antiscalant Dosing Tank |
| Date | 20-Jan-2026 |
| TAG | TK-09-002 |
| Manufacturer | Promatics |
| Model | PLC330 |
| Revision | B (Material change from Rev A) |

#### 3.2.2 Material Change Evaluation

| Parameter | Technical Offer | Rev A | Rev B | Evaluation |
|-----------|-----------------|-------|-------|------------|
| Material | HDPE | HDPE | **LMDPE** | **ACCEPTED** |
| Capacity | 65 gal (246 L) | 246 L | 340 L (0.34 m3) | **EXCEEDS** requirement |
| Manufacturer | Norwesco or Equal | Norwesco | Promatics | Acceptable equivalent |

**Justification provided by BW Water:** "Material changed from HDPE to LMDPE due to dimensional limitations. The smallest available HDPE tank is 1.1 m3 with diameter ~1.2 m. LMDPE tank provides more suitable size while meeting capacity requirements."

**ADASA Evaluation:** The material change from HDPE to LMDPE is technically acceptable because:
- Both materials are polyethylene with similar chemical resistance
- LMDPE is compatible with antiscalant chemicals (pH > 10)
- Delivered capacity (340 L) exceeds committed capacity (246 L)
- Change is justified by dimensional constraints

**MATERIAL CHANGE ACCEPTED.**

#### 3.2.3 Observations

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| OBS-11 | P&ID Update | Tank capacity in P&ID (0.25 m3) differs from Datasheet (0.34 m3 total / 0.27 m3 effective). Update P&ID in next revision. | MINOR |
| **OBS-14** | **Dosing Rate Validation** | The Antiscalant Dosing Tank is part of a dosing system with specified rate of 0.5 ppm (per Chemical Consumption List P22-LI-09-009-002-A). ADASA has issued **Technical Query P22-CT-09-000-001-0** requesting manufacturer validation of this dosing rate for concentrate conditions with LSI 2.0-2.11. Industry practice for LSI > 2.0 typically requires 5-10 ppm. **Tank approval is subject to satisfactory response to the Technical Query.** | **MEDIUM** |

#### 3.2.4 Verdict

| Aspect | Result |
|--------|--------|
| ET Compliance | **COMPLIANT** (material not specified in ET) |
| Technical Offer Compliance | **COMPLIANT** (change justified, capacity exceeds requirement) |
| **FINAL VERDICT** | **2 - APPROVED AS NOTED** |

---

### 3.3 Control System Architecture (P22-CD-09-004-001-B) - APPROVED AS NOTED

#### 3.3.1 Document Information

| Field | Value |
|-------|-------|
| Code | P22-CD-09-004-001-B |
| Title | Control System Architecture |
| Date | 29-Jan-2026 |
| Prepared | BT |
| Reviewed | NHH |
| Approved | JFR |
| Revision | B (Response to TM N2 comments) |

#### 3.3.2 Bill of Materials - Control System

| No. | Description | Model | Manufacturer |
|-----|-------------|-------|--------------|
| 1 | PLC CPU | 5069-L320ER | Allen Bradley |
| 2 | Digital Input Module 16 x DI | 5069-IB16 | Allen Bradley |
| 3 | Digital Output Module 16 x DO | 5069-OB16 | Allen Bradley |
| 4 | Analog Input Module 8 x AI | 5069-IF8 | Allen Bradley |
| 5 | Analog Output Module 4 x AO | 5069-OF4 | Allen Bradley |
| 6 | HMI 10" Color Touch Screen | 2711P-T10C21D8S | Allen Bradley |
| 7 | Ethernet Switch 8 Ports | 1783-USP8T | Allen Bradley |
| 8 | EtherNet/IP to Modbus TCP Gateway | PLX32-EIP-MBTCP | ProSoft |
| 9 | Studio 5000 Logix Designer V37 | - | Allen Bradley |
| 10 | FactoryTalk View Studio V15 | - | Allen Bradley |
| 11 | Engineering Laptop | Latitude 3450 | Dell |

#### 3.3.3 ET 5.4 Compliance Verification

| ET Requirement | Specification | Delivered | Complies |
|----------------|---------------|-----------|----------|
| PLC Allen Bradley | Required | 5069-L320ER CompactLogix | **YES** |
| HMI 10" color touch | Required | PanelView Plus 7 10" | **YES** |
| Modbus TCP/IP | Required | PLX32-EIP-MBTCP Gateway | **YES** |
| Ethernet Switch 5+ ports | Minimum 5 | 8 ports (Stratix 2100) | **YES** |
| Software licenses | Perpetual | Studio 5000 + FactoryTalk | **YES** |
| UPS 8 hours autonomy | Required | **NOT IN BOM** | **NO** |

#### 3.3.4 Response to TM N2 Comments

| Comment | BW Water Response | Status |
|---------|-------------------|--------|
| Modbus TCP Memory Map | "WILL SUBMIT I/O MODBUS LIST SEPARATELY" | **NOT DELIVERED (30 days)** |
| VFD Fieldbus for SCADA | "HAS REVISED IN CONTROL SYSTEM ARCHITECTURE REVB" | **PARTIAL** - Connection shown but protocol not specified |
| Power Meter Clarification | "LCP includes Digital Power Meter with Modbus TCP/IP" | **CLOSED** |

#### 3.3.5 Observations

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| **OBS-04** | **Modbus Map** | BW Water committed to deliver Modbus TCP Memory Map separately. Document has NOT been delivered after 30 days. Critical for DCS integration planning. | **CRITICAL** |
| **OBS-09** | **UPS Missing** | ET Section 5.4 (L1088-1089) requires: "UPS con la capacidad suficiente para mantener el sistema de control activo por al menos 8 horas." UPS not included in BOM. | **MAJOR** |
| OBS-12 | VFD Fieldbus | Diagram shows CAT6/Ethernet connection to VFDs but does not explicitly specify communication protocol or available electrical variables for SCADA monitoring. | MAJOR |

#### 3.3.6 Verdict

| Aspect | Result |
|--------|--------|
| ET 5.4 Compliance | **PARTIAL** (UPS missing) |
| Technical Offer Compliance | **COMPLIANT** |
| TM N2 Comment Resolution | **PARTIAL** (1/3 closed, Modbus Map pending 38 days) |
| **FINAL VERDICT** | **2 - APPROVED AS NOTED** |

---

### 3.4 Cable Tray Layout (P22-DWG-09-007-004-A) - TO BE REVISED

#### 3.4.1 Document Information

| Field | Value |
|-------|-------|
| Code | P22-DWG-09-007-004-A |
| Title | Cable Tray Layout and Support Details |
| Date | 27-Jan-2026 |
| Prepared | BT |
| Reviewed | NHH |
| Approved | JFR |
| Revision | A (First issue) |

#### 3.4.2 Document Content Summary

- **Sheet 1:** Plan View - Cable Tray Layout
- **Sheet 2:** Instrument Location Schedule (32 instruments)
- **Sheet 3:** Installation Details

**Cable Tray Specifications:**
- Material: Steel Hot Dip Galvanized
- Minimum dimensions: 50mm x 50mm
- Maximum fill: 80%

#### 3.4.3 Observations

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| **OBS-05** | **Duplicate TAG** | FIT-09-001 appears in Item 4 (Cartridge Filter Discharge, DN100, 0-100 m3/h) AND Item 13 (2nd Stage Permeate, DN50, 0-18 m3/h). Two different instruments with same TAG. **PLC addressing impossible.** Layout inherits this error from Instrument List. | **CRITICAL** |
| **OBS-06** | **Missing Vibration** | Layout does not include locations for vibration transmitters on HP Pump (BH-09-001), Feed Turbocharger (SIP-09-001), and Interstage Turbocharger (SIP-09-002) as required by ET Section 5.5.7 (L1390-1394). This observation was raised in TM N3 and remains unresolved after 8 days. | **CRITICAL** |
| **OBS-07** | **Missing Pt-100** | Layout does not include locations for Pt-100 temperature sensors in HP Pump (87 kW) and CIP Pump (15 kW) motors as required by ET Section 5.3 (L1032-1033). This observation was raised in TM N3 and remains unresolved after 8 days. | **CRITICAL** |
| **OBS-10** | **Container >40ft** | Cable Tray Layout shows elongated container suggesting 60ft configuration (40ft + 20ft extension). **ADASA rejected 60ft proposal on November 17, 2025** due to: (1) Budget impact of +USD $67,208, (2) Schedule impact of +5 weeks. Container must conform to approved 40ft standard. | **CRITICAL** |
| OBS-13 | LIT TAG Discrepancy | Layout uses LIT-09-001 for CIP Tank Level, IO List uses LIT-09-002. Unification required. | MAJOR |

#### 3.4.4 Positive Findings

| Item | Status | Details |
|------|--------|---------|
| Cable Tray Material | **COMPLIANT** | Steel Hot Dip Galvanized |
| Fill Maximum | **COMPLIANT** | 80% declared |
| Instrument Count | **DOCUMENTED** | 32 instruments with locations |
| Panel Count | **DOCUMENTED** | 10 power panels with TAGs |

#### 3.4.5 Verdict

| Aspect | Result |
|--------|--------|
| ET Compliance | **NOT COMPLIANT** (OBS-06, OBS-07) |
| Instrument List Consistency | **NOT COMPLIANT** (OBS-05 - inherits duplicate TAG) |
| **FINAL VERDICT** | **3 - TO BE REVISED** |

**Justification:** Document cannot be approved due to:
1. Duplicate TAG FIT-09-001 inherited from Instrument List
2. Missing instrument locations for vibration transmitters (ET 5.5.7)
3. Missing instrument locations for motor Pt-100 sensors (ET 5.3)
4. Container dimensions appear to exceed approved 40ft configuration (rejected Nov-17-2025)

---

## 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

This section summarizes critical observations raised in previous transmittals that remain unresolved.

### 4.1 From Transmittal N2 (January 6, 2026) - 30 DAYS PENDING

| # | Observation | Original Document | Days Pending | Impact |
|---|-------------|-------------------|--------------|--------|
| 1 | **A/C n+1 configuration required** | E5 - DS Air Conditioning | **31** | Blocks container thermal compliance |
| 2 | **A/C thermal calculation required** | New document required | **31** | Required per ET 5.1.11 |
| 3 | **Static Mixer material justification** | E5 - DS Static Mixer | **31** | FRP to PVC change |
| 4 | **Modbus TCP Memory Map required** | Control Architecture | **31** | Critical for DCS integration |

**Note:** Observations #1 and #2 are directly related to findings in Submittal 0010 (Utility Consumption List still shows only 1 A/C unit). Observation #4 was committed to be delivered separately but has not been received.

### 4.2 From Transmittal N3 (January 28, 2026) - 8 DAYS PENDING

| # | Observation | Document | Days Pending | Severity |
|---|-------------|----------|--------------|----------|
| 1 | Vibration transmitters missing | Instrument List | 9 | CRITICAL |
| 2 | Pt-100 motor windings HP Pump | HP Pump Datasheet | 9 | CRITICAL |
| 3 | CIP Pump datasheet missing | New document required | 9 | CRITICAL |
| 4 | VM-09-015 manual DN100 ANSI 900# | Valve List | 9 | CRITICAL |
| 5 | Duplicate TAGs (VM-09-015, VE-09-008, VE-09-010) | Valve List | 9 | MAJOR |
| 6 | Missing VFD electrical variables | IO List | 9 | CRITICAL |
| 7 | Missing DO/DI external coordination | IO List | 9 | CRITICAL |
| 8 | Duplicate TAG FIT-09-001 | Instrument List | 9 | CRITICAL |

**Reference:** See Transmittal N3 (P22-TM-09-000-003-0) Section 4 for complete details.

**Note:** Observation #8 (FIT-09-001 duplicate) is inherited by Cable Tray Layout in Submittal 0011.

---

## 5. REQUIRED ACTIONS - BW WATER

### 5.1 Critical Actions (HIGH Priority)

| # | Action | Document | Reference | Status |
|---|--------|----------|-----------|--------|
| 1 | **Confirm PLC frequency compatibility:** If dual-frequency (50/60 Hz), document explicitly in specifications. If 60 Hz only, replace with 50 Hz compatible equipment. | P22-LI-09-009-001-A | OBS-01, ET 5.4.7 | **PENDING** |
| 2 | **Add 2nd A/C unit:** Include n+1 configuration (2 units) as required by ET 5.1.11 and committed in Technical Offer. Update Utility List and Load List. | P22-LI-09-009-001-A | OBS-02, ET 5.1.11 | **PENDING 30 DAYS** |
| 3 | **Deliver A/C thermal calculation:** Provide thermal load calculation document considering ALL heat sources (equipment, lighting, wall transmission, solar radiation) per ET 5.1.11. | New document | OBS-03, ET 5.1.11 | **PENDING 30 DAYS** |
| 4 | **URGENT: Deliver Modbus TCP Memory Map:** Document committed 30 days ago. Critical for DCS integration planning. Include variable names, addresses, and data types. | New document | OBS-04, TM N2 | **PENDING 30 DAYS** |
| 5 | **Correct duplicate TAG FIT-09-001:** Renumber Item 13 (2nd Stage Permeate) as FIT-09-002 in Instrument List. Update Cable Tray Layout accordingly. | P22-LI-09-008-003 + P22-DWG-09-007-004 | OBS-05, TM N3 | **PENDING 8 DAYS** |
| 6 | **Include vibration transmitter locations:** Add mounting locations for VT-09-001/002/003 on HP Pump and Turbochargers in Layout. Add instruments to Instrument List. | P22-DWG-09-007-004 + P22-LI-09-008-003 | OBS-06, ET 5.5.7 | **PENDING 8 DAYS** |
| 7 | **Include Pt-100 motor sensor locations:** Add mounting locations for temperature sensors in HP Pump (87 kW) and CIP Pump (15 kW) motors. Update datasheets. | P22-DWG-09-007-004 + Datasheets | OBS-07, ET 5.3 | **PENDING 8 DAYS** |
| 8 | **URGENT: Confirm container dimensions:** Cable Tray Layout shows elongated container suggesting 60ft. ADASA rejected 60ft on Nov-17-2025 (+USD $67,208, +5 weeks). Confirm layout uses approved 40ft standard OR justify deviation. | P22-DWG-09-007-004 | OBS-10 | **NEW - CRITICAL** |

### 5.2 Major Actions (MEDIUM Priority)

| # | Action | Document | Reference | Status |
|---|--------|----------|-----------|--------|
| 9 | **Unify HP Pump power:** Determine correct value (83/86/92/93 kW) and update ALL documents (Utility List, Load List, Equipment List, Datasheet). | Multiple | OBS-08 | **PENDING** |
| 10 | **Include UPS in BOM:** Add UPS with minimum 8 hours autonomy for control system per ET 5.4 (L1088-1089). | P22-CD-09-004-001 | OBS-09, ET 5.4 | **PENDING** |
| 11 | **Clarify CIP Pump power:** Confirm correct value (11 kW vs 15 kW) and update documents accordingly. | P22-LI-09-009-001-A | Cross-ref | **PENDING** |
| 12 | **Specify VFD fieldbus explicitly:** Document communication protocol and available electrical variables for SCADA monitoring. | P22-CD-09-004-001 | OBS-12 | **PENDING** |
| 13 | **Unify LIT TAG:** Decide between LIT-09-001 (Layout) or LIT-09-002 (IO List) for CIP Tank Level. Update all documents. | Multiple | OBS-13 | **PENDING** |

### 5.3 Minor Actions (LOW Priority)

| # | Action | Document | Reference | Status |
|---|--------|----------|-----------|--------|
| 14 | **Update P&ID Antiscalant Tank capacity:** Change from 0.25 m3 to 0.34 m3 in next P&ID revision. | P22-DWG-09-009-002 | OBS-11 | **PENDING** |
| 15 | **Clarify Dosing Pump capacity:** Resolve discrepancy between P&ID (1 LPH) and Equipment List (2.3 LPH). | Equipment List / P&ID | Cross-ref | **PENDING** |

### 5.4 Reference: Pending Actions from Previous Transmittals

The following critical actions from Transmittals N2 and N3 remain open:

**From TM N2 (30 days pending):**
- Actions #2, #3: A/C configuration and thermal calculation (see Section 4.1)
- Action #4: Modbus TCP Memory Map (30 days pending)

**From TM N3 (8 days pending):**
- Group A: TAG corrections (FIT-09-001 duplicate - now affecting Layout)
- Group B: Vibration instrumentation (HP Pump, Turbochargers)
- Group C: Pump temperature sensors (Pt-100 motor windings)
- Group D: Valve List corrections (VM-09-015 motorized, duplicate TAGs)
- Group G: IO List coordination signals (VFD variables, DO/DI)

**Reference:** See Transmittal N3 (P22-TM-09-000-003-0) Section 4 for complete action list.

---

## 6. ATTACHMENTS

| # | Attachment | Description |
|---|------------|-------------|
| L | P22-LI-09-009-001-A_Utility_Consumption_List_Comments.pdf | Utility Consumption List with ADASA review comments highlighting PLC frequency, A/C configuration, and power discrepancies |
| M | P22-ET-09-009-010-B_Antiscalant_Tank_Comments.pdf | Antiscalant Dosing Tank datasheet with ADASA annotations on material change acceptance and P&ID capacity update |
| N | P22-CD-09-004-001-B_Control_Architecture_Comments.pdf | Control System Architecture with ADASA review comments on UPS requirement and Modbus Map pending status |
| O | P22-DWG-09-007-004-A_Cable_Tray_Layout_Comments.pdf | Cable Tray Layout with ADASA annotations highlighting duplicate TAG FIT-09-001 and missing instrument locations |

**Download Link:** [To be provided]

*Annotated PDFs with ADASA review comments attached.*

---

## 7. RESPONSE SUMMARY

| Document | Code | Verdict |
|----------|------|---------|
| Utility Consumption List | P22-LI-09-009-001-A | **3 - To be revised** |
| Antiscalant Dosing Tank DS | P22-ET-09-009-010-B | 2 - Approved as noted* |
| Control System Architecture | P22-CD-09-004-001-B | 2 - Approved as noted |
| Cable Tray Layout | P22-DWG-09-007-004-A | **3 - To be revised** |

*Subject to satisfactory response to **Technical Query P22-CT-09-000-001-0** regarding antiscalant dosing rate justification (0.5 ppm for LSI 2.0-2.11 conditions). See Antiscalant Dosing Tank Observations (OBS-14).

**TRANSMITTAL VERDICT: 3 - TO BE REVISED**
