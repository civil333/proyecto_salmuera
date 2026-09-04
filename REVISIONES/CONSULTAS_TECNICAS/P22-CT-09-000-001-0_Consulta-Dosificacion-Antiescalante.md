---
titulo: "Technical Query - Antiscalant Dosing Justification"
subtitulo: "Second Stage RO Brine Module - Taltal"
codigo: "P22-CT-09-000-001-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Technical Query"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# TECHNICAL QUERY: ANTISCALANT DOSING JUSTIFICATION

**Date:** February 05, 2026
**Project:** BAE 12803 - Second Stage RO Brine Module
**From:** ADASA - Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** ISSUED

---

## 1. QUERY DESCRIPTION

### 1.1 Subject

Justification of antiscalant dosing rate (0.5 ppm) for high LSI concentrate conditions.

### 1.2 Reference Documents

| Document | Code | Rev | Submittal |
|----------|------|-----|-----------|
| Chemical Consumption List | P22-LI-09-009-002 | A | E7 (25007-0007) |
| Datasheet of Antiscalant Dosing Pump | P22-ET-09-009-004 | B | E7 (25007-0007) |
| Datasheet of Antiscalant Dosing Tank | P22-ET-09-009-010 | B | E10 (25007-0010) |
| Technical Offer | BW Water Proposal | Rev.1 | - |

**Review Status:** The Chemical Consumption List and Dosing Pump were approved in Transmittal N3 (P22-TM-09-000-003-0). The Antiscalant Dosing Tank (P22-ET-09-009-010-B) has been approved in Transmittal N4 (P22-TM-09-000-004-0) subject to satisfactory response to this Technical Query (OBS-14). This query seeks manufacturer validation of the specified dosing rate.

### 1.3 Background

During detailed review of the antiscalant system design, ADASA has identified that the specified dosing rate appears significantly lower than industry norms for comparable applications. This query is raised to understand the technical basis and ensure long-term membrane protection.

---

## 2. TECHNICAL ANALYSIS

### 2.1 Specified Dosing Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Antiscalant dosage | 0.5 ppm | Chemical Consumption List |
| Consumption rate | 0.02 L/h | Chemical Consumption List |
| Dosing pump capacity | 2.3 L/h | Datasheet P22-ET-09-009-004-B |
| Tank capacity | 340 L (effective 270 L) | Datasheet P22-ET-09-009-010-B |
| Calculated autonomy | ~19 months | Based on 0.02 L/h consumption |

### 2.2 Concentrate Water Quality (Worst Case)

Based on LG Chem membrane projections included in Technical Offer Rev.1:

| Parameter | Value | Units |
|-----------|-------|-------|
| TDS (concentrate) | 53,000 | ppm |
| Temperature | 24 | C |
| LSI (Langelier Saturation Index) | 2.0 - 2.11 | - |

**Note:** LSI values above 2.0 indicate high scaling potential requiring aggressive antiscalant treatment.

### 2.3 Industry Reference Values

| LSI Range | Typical Dosage | Application |
|-----------|----------------|-------------|
| < 1.0 | 1-2 ppm | Low scaling potential |
| 1.0 - 1.5 | 2-4 ppm | Moderate scaling |
| 1.5 - 2.0 | 4-6 ppm | High scaling |
| > 2.0 | 5-10 ppm | Very high scaling (brine concentration) |

**Observation:** The specified 0.5 ppm is 10-20x lower than typical values for LSI > 2.0.

### 2.4 Positive Design Elements

ADASA acknowledges the following positive aspects of the antiscalant system design:

| Aspect | Evaluation |
|--------|------------|
| Dosing pump capacity margin | **115x** (0.02 L/h operating vs 2.3 L/h capacity) |
| Tank size | Exceeds Technical Offer requirement (340 L vs 246 L) |
| Material compatibility | LMDPE compatible with antiscalant chemicals |

The substantial pump capacity margin allows dosage increase without equipment replacement if required.

---

## 3. CLARIFICATION REQUESTED

### 3.1 Required Information

Please provide the following documentation to support the specified 0.5 ppm dosing rate:

| # | Item | Description |
|---|------|-------------|
| 1 | **Antiscalant manufacturer scaling projection** | Simulation or calculation from the selected antiscalant supplier demonstrating that 0.5 ppm is sufficient for the specified water quality (LSI up to 2.11) |
| 2 | **Antiscalant product datasheet** | Technical specifications including recommended dosing range for high-LSI applications |
| 3 | **Membrane manufacturer compatibility confirmation** | Documentation from LG Chem confirming compatibility between specified antiscalant and NanoH2O membranes |

### 3.2 Alternative Response

If the dosing rate of 0.5 ppm is not supported by manufacturer calculations, please provide:

1. Revised dosing rate recommendation
2. Updated Chemical Consumption List
3. Impact assessment on tank autonomy and operational costs

---

## 4. TECHNICAL REFERENCE

### 4.1 LG Chem Disclaimer (Technical Offer)

The LG Chem membrane projection software includes the following statement:

> *"It is the user's responsibility to make provisions against fouling, scaling and chemical attacks."*

This disclaimer transfers scaling prevention responsibility to the system designer (BW Water), making proper antiscalant selection and dosing critical.

### 4.2 Scaling Risk Assessment

| Failure Mode | Consequence | Mitigation |
|--------------|-------------|------------|
| Membrane scaling (CaCO3, CaSO4) | Reduced permeate flow, increased pressure | Adequate antiscalant dosing |
| Premature membrane replacement | USD 15,000-30,000 per element | Manufacturer-validated dosing |
| Unplanned shutdown | Production loss, maintenance cost | Monitoring + correct chemistry |

---

## 5. RESPONSE REQUESTED

### 5.1 Response Deadline

Please provide the requested documentation by **February 10, 2026**.

### 5.2 Contact

For clarification on this query, please contact:

**Luis Rivera**
Contract Administrator
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module Taltal

---

## 6. DOCUMENT HISTORY

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 0 | 05-Feb-2026 | Initial issue | L. Rivera |
