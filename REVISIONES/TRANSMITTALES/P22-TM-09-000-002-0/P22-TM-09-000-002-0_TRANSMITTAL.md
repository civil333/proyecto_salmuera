---
titulo: "TECHNICAL REVIEW TRANSMITTAL N2"
subtitulo: "Second Stage RO Brine Module - Submittals 0003, 0004, 0005, 0006, 0007"
codigo: "P22-TM-09-000-002-0"
version: "Rev.1"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Gerencia Tecnica ADASA"
aprobado_por: "Pendiente"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# TECHNICAL REVIEW TRANSMITTAL N2

**Date:** January 26, 2026
**Project:** BAE 12803 - Second Stage RO Brine Module
**From:** ADASA - Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** FINAL

---

## 1. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| **Transmittal Code** | P22-TM-09-000-002-0 |
| **Submittal 0003** | 25007-0003 (Dec-16-2025) - 1 document |
| **Submittal 0004** | 25007-0004 (Dec-24-2025) - 1 document |
| **Submittal 0005** | 25007-0005 (Jan-06-2026) - 2 documents |
| **Submittal 0006** | 25007-0006 (Jan-08-2026) - 3 documents |
| **Submittal 0007** | 25007-0007 (Jan-14-2026) - 1 document |
| **Total Documents** | 8 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information |

---

## 2. EXECUTIVE SUMMARY

### 2.1 Process Calculation Validation

**IMPORTANT:** Process Calculation Rev B (P22-CD-09-009-001-B) received on January 14, 2026 (Submittal 25007-0007) has been reviewed and **validates the following critical items:**

| Validation Item | Status | Reference |
|-----------------|--------|-----------|
| Design pressures with 10% margin | **VALIDATED** | Stage 1: 70 bar, Stage 2: 85 bar |
| Turbocharger modeling (43k & 53k TDS) | **VALIDATED** | BiTurbo Analysis - 10 scenarios |
| HP Pump TDH | **VALIDATED** | 49.4 barg consistent with modeling |
| Membrane configuration | **VALIDATED** | 6×7 SR + 4×7 UHP = 70 elements |
| Permeate quality guarantee | **VALIDATED** | TDS < 500 mg/L all scenarios |

This validation allows closure of previously blocking observations on P&ID and equipment datasheets.

### 2.2 Remaining Critical Observations

| # | Observation | Document | Severity |
|---|-------------|----------|----------|
| 1 | **A/C thermal load undersized:** Calculated 5.96 kW vs estimated ~11-15 kW real load | A/C Thermal Calc | **HIGH** |
| 2 | **Missing n+1 A/C configuration:** Required per ET 5.1.11 and Technical Offer | A/C Thermal Calc | **HIGH** |
| 3 | **Material change FRP to PVC:** Requires justification for Static Mixer | Static Mixer | **MEDIUM** |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 P&ID (P22-DWG-09-009-002-A) - APPROVED AS NOTED

**Status Change:** Design pressure validation completed. OBS-09 CLOSED.

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Battery limits | Indicate ADASA/BW Water supply limit with flange | OPEN |
| OBS-02 | PVC in SDSS zone | PVC lines found within SDSS zone rectangle | OPEN |
| OBS-03 | Line TAGs | Indicate line TAG with diameter | OPEN |
| OBS-04 | Drainage | This stream should go to drainage | OPEN |
| OBS-05 | Battery limit | Indicate BW/ADASA supply limit with flange + TAG + diameter | OPEN |
| OBS-06 | CIP connection | Goes to CIP TANK TK-09-001 | OPEN |
| OBS-07 | HP Pump | Include pump characteristics | OPEN |
| OBS-08 | Stage connection | Comes from 1st and 2nd stage | OPEN |
| OBS-09 | Design pressures | ~~Verify 10% margin vs current ~4%~~ | **CLOSED** - Process Calc validates 70/85 bar with 10% margin |
| OBS-10 | Super Duplex | Confirm SDSS material in HP lines | OPEN |
| OBS-11 | Valve TAGs | Add valve identification | OPEN |
| OBS-12 | Instrument TAGs | Complete instrumentation TAGs | OPEN |
| OBS-13 | Flow directions | Verify flow arrows consistency | OPEN |
| OBS-14 | Legend | Update legend with all symbols used | OPEN |

### 3.2 Control Architecture (P22-CD-09-004-001-A) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | PLC Datasheet | Pending PLC detailed specifications | OPEN |
| OBS-02 | Communication | Confirm Modbus TCP/RTU availability | OPEN |
| OBS-03 | Ethernet ports | Indicate available Ethernet ports in LCP | OPEN |
| OBS-04 | I/O count | Verify I/O count vs instrument list | OPEN |
| OBS-05 | Redundancy | Confirm controller redundancy if applicable | OPEN |
| OBS-06 | HMI screens | Pending HMI screen layout | OPEN |
| OBS-07 | I/O Signals | Indicate all IN/OUT signals required for module operation with corresponding P&ID instrumentation TAGs | OPEN |
| OBS-08 | Modbus TCP Map | Provide Modbus TCP memory map and PLC programming specifications for DCS integration | OPEN |
| OBS-09 | VFD Fieldbus | Implement fieldbus communication between VFDs and SCADA to monitor electrical variables from HP Pump (BH-09-001) and CIP Pump (BH-09-002) VFDs | OPEN |
| OBS-10 | Power Metering | Clarify total module power consumption metering: via fieldbus communication or analyzer SAI-09-001? Specify configuration | OPEN |

### 3.3 A/C Thermal Calculation (P22-CD-09-005-002-A) - TO BE REVISED

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| OBS-01 | Thermal load | Calculated 5.96 kW vs estimated real ~10-12 kW (see detailed breakdown below) | **HIGH** |
| OBS-02 | Missing loads | PLC + Instrumentation (2.0 kW per Load List), Indoor Lighting (0.16 kW) not included | **HIGH** |
| OBS-03 | n+1 config | Missing redundant A/C unit per ET 5.1.11 and Technical Offer (2 A/C 1W+1S offered) | **HIGH** |
| OBS-04 | Load List | Update Electrical Load List with 2x A/C units | MEDIUM |
| OBS-05 | Heat transmission | Container envelope heat transfer not considered (T_ext=28°C max, T_int<25°C required, A≈100m²) | MEDIUM |
| OBS-06 | Solar radiation | Solar heat gain not considered - Taltal is desert coastal zone with high radiation | MEDIUM |
| OBS-07 | Safety margin | No contingency factor included (typical 10-15% for HVAC sizing) | LOW |
| OBS-08 | Design conditions | Design conditions not specified (summer peak vs annual average) | LOW |

**Detailed Heat Load Analysis:**

| Heat Source | Value (kW) | Status in Calculation |
|-------------|------------|----------------------|
| HP Pump motor losses | 4.26 | Included |
| HP Pump VFD losses | 1.70 | Included |
| PLC + Instrumentation | 2.00 | **MISSING** |
| Indoor lighting | 0.16 | **MISSING** |
| Container wall transmission | ~1.0-1.5 | **MISSING** |
| Solar radiation (desert) | ~0.5-1.0 | **MISSING** |
| **TOTAL ESTIMATED** | **~10-12 kW** | |

**Action Required:** Complete thermal calculation with ALL heat sources (per Load List and environmental conditions), include heat transmission through container walls, consider solar radiation for Taltal location, add safety margin, and include n+1 configuration as required by ET 5.1.11 and offered in Technical Proposal.

### 3.4 Static Mixer (P22-ITEM-09-009-012-A) - TO BE REVISED

| # | Code | Observation | Impact |
|---|------|-------------|--------|
| OBS-01 | Material | Proposed PVC vs FRP in Technical Offer | MEDIUM |
| OBS-02 | Dimensions | Different L/D ratio affects mixing efficiency | MEDIUM |
| OBS-03 | Velocity | 71% lower velocity (0.17 vs 0.59 m/s) | MEDIUM |
| OBS-04 | Brand | Confirm Koflo equivalence to KOMAX | LOW |

**Action Required:** Provide technical justification for material change and mixing efficiency validation.

### 3.5 UHPRO System (P22-ET-09-009-001-B) - APPROVED

**Status Change:** Upgraded from "Approved as noted" to "Approved".

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Membrane table | ~~Include clear table with quantities per model/stage~~ | **CLOSED** - Process Calc confirms 6×7=42 SR + 4×7=28 UHP |
| OBS-02 | Code correction | ITEM to ET corrected in Rev B | **CLOSED** |

**Validation Summary from Process Calculation Rev B:**
- Stage 1: 6 vessels × 7 elements = 42 LG SW 400 SR
- Stage 2: 4 vessels × 7 elements = 28 LG SW 400 R G2 UHP
- Total: 70 membrane elements
- Recovery: 42.86%
- Capacity: 21 m³/h (504 m³/day > 480 required)

### 3.6 CIP Pump (P22-ET-09-009-003-B) - APPROVED AS NOTED

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Start type | VFD to Direct start - acceptable for CIP application | **CLOSED** |
| OBS-02 | Motor | Different motor specs - verify compatibility | OPEN |
| OBS-03 | Code correction | ITEM to ET corrected in Rev B | **CLOSED** |

### 3.7 CIP Cartridge Filter (P22-ET-09-009-006-B) - APPROVED AS NOTED

**Status Change:** Upgraded from "To be revised" to "Approved as noted".

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Cartridge count | ~~19 to 17 cartridges - justify capacity~~ | **CLOSED** - Process Calc validates: 17 cartridges @ 3.45 m² = 57 m³/hr @ 16.5 m³/hr/m² |
| OBS-02 | Closure type | Swing Bolts vs Quick Opening - noted | OPEN (minor) |
| OBS-03 | Orientation | Vertical to Horizontal - noted | OPEN (minor) |

### 3.8 Process Calculation (P22-CD-09-009-001-B) - APPROVED AS NOTED

**Status:** Critical document that validates design parameters. Closes blocking observations on other documents.

| # | Code | Observation | Status |
|---|------|-------------|--------|
| OBS-01 | Summary table | Recommend adding summary table at document start | OPEN (minor) |

**Key Validations Provided:**
- Design pressures: Stage 1 = 70 barg, Stage 2 = 85 barg (10% margin confirmed)
- Turbocharger modeling: BiTurbo analysis for 43k and 53k TDS - 10 scenarios
- HP Pump TDH: 49.4 barg consistent with energy recovery modeling
- Membrane configuration: 6×7 SR + 4×7 UHP = 70 elements
- Recovery: 42.86% | Capacity: 21 m³/h (504 m³/day > 480 required)
- Permeate quality: TDS < 500 mg/L guaranteed in all scenarios

**Documents Unblocked by this Calculation:**
| Document | Observation Closed | Impact |
|----------|-------------------|--------|
| P&ID | OBS-09 Design pressures | 10% margin validated |
| UHPRO System | OBS-01 Membrane table | Configuration confirmed |
| CIP Filter | OBS-01 Cartridge count | 17 cartridges validated |

---

## 4. REQUIRED ACTIONS - BW WATER

### 4.1 Critical Actions (HIGH Priority)

| # | Action | Document | Status |
|---|--------|----------|--------|
| 1 | ~~Provide Process Calculation with turbocharger modeling~~ | Process Calc | **RECEIVED & VALIDATED** |
| 2 | Complete A/C thermal calculation with ALL loads (~11-15 kW vs 5.96 kW) | A/C Thermal Calc | **PENDING** |
| 3 | Include n+1 configuration (2x A/C units per ET 5.1.11 and Offer) | A/C Thermal Calc | **PENDING** |

### 4.2 Technical Actions (MEDIUM Priority)

| # | Action | Document | Status |
|---|--------|----------|--------|
| 4 | Justify material change FRP to PVC | Static Mixer | **PENDING** |
| 5 | Confirm mixing efficiency with new dimensions | Static Mixer | **PENDING** |
| 6 | Indicate battery limits with flanges at all connection points | P&ID | PENDING |
| 7 | Add line TAGs with diameters | P&ID | PENDING |
| 8 | Review PVC lines within SDSS zone | P&ID | PENDING |
| 9 | Provide Modbus TCP memory map for DCS integration | Control Architecture | PENDING |
| 10 | Implement VFD fieldbus for SCADA electrical monitoring | Control Architecture | PENDING |
| 11 | Clarify power consumption metering configuration | Control Architecture | PENDING |

### 4.3 Completed Actions

| # | Action | Document | Completion |
|---|--------|----------|------------|
| A | Process Calculation with turbocharger modeling | P22-CD-09-009-001-B | Jan-14-2026 |
| B | Design pressure validation (10% margin) | Process Calc | Jan-26-2026 |
| C | Membrane configuration validation | Process Calc | Jan-26-2026 |
| D | CIP Filter capacity justification | Process Calc | Jan-26-2026 |

---

## 5. ATTACHMENTS

| # | Attachment | Description |
|---|------------|-------------|
| A | P22-DWG-09-009-002_A - P&ID Coment LH.pdf | P&ID with ADASA review comments |
| B | P22-ET-09-009-001-B Datasheet of UHPRO System Coment LH.pdf | UHPRO System with annotations |
| C | P22-ET-09-009-003-B_Datasheet of RO CIP Pump Coment LH.pdf | CIP Pump with annotations |
| D | P22-ITEM-09-009-012-A_Datasheet of Static Mixer Coment LH.pdf | Static Mixer with annotations |
| E | P22-CD-09-009-001-B_Process Calculation.pdf | Process Calculation Rev B |
| F | CC P22-CD-09-004-001_A CONTROL ARCHITECTURE.pdf | Control Architecture with ADASA review comments |

**Download Link:** https://www.dropbox.com/t/INLfLK7p4ISQiAnz

*This link contains all PDFs with ADASA review comments and annotations.*

---

*Prepared by: ADASA - Aguas de Antofagasta S.A.*
*Date: January 26, 2026*
*Contract: C-4300 BW Water - BAE 12803*
*Revision: Rev.1 - Process Calculation validation incorporated*
