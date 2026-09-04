---
titulo: "Technical Query CT-001 - Response Evaluation"
subtitulo: "Antiscalant Dosing Justification - BW Water Response Assessment"
codigo: "P22-CT-09-000-001-1"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Technical Query - Response Evaluation"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# TECHNICAL QUERY CT-001: RESPONSE EVALUATION

**Date:** February 16, 2026
**Project:** BAE 12803 - Second Stage RO Brine Module
**From:** ADASA - Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Reference:** P22-CT-09-000-001-0 (issued February 05, 2026)

---

## RESPONSE EVALUATION

### Summary

ADASA issued Technical Query CT-001 on February 05, 2026, requesting manufacturer validation of the 0.5 ppm antiscalant dosing rate for concentrate conditions with LSI 2.0-2.11 at 24°C. The response deadline was February 10, 2026.

BW Water submitted their response on February 13, 2026 (3 days past deadline) with the following documents:

| # | Document | Content |
|---|----------|---------|
| 1 | BW Water Memorandum | Cover letter summarizing two independent assessments |
| 2 | AWC Projection (Pureflux SW) | PROTON software simulation for Pureflux SW antiscalant |
| 3 | CREST Water Email | Third-party opinion on scaling potential |

### General Assessment

The AWC projection demonstrates that **0.5 ppm of Pureflux SW antiscalant is acceptable** for the modeled conditions. The PROTON software simulation confirms dosing adequacy with positive safety margins for CaCO3, CaSO4, BaSO4, SrSO4, and silica scaling.

However, ADASA has identified **four technical observations** that require clarification or correction before CT-001 can be formally closed.

---

## DETAILED OBSERVATIONS

### Observation 1: Antiscalant Projection Temperature

| Field | Value |
|-------|-------|
| Document | AWC Projection - Pureflux SW |
| Severity | Major |
| Category | Design Basis |

**Finding:** The AWC PROTON simulation was run at a feed temperature of **19°C**. CT-001 specifically requested justification for worst-case conditions at **24°C**, where scaling potential is highest.

**Requirement:** The Technical Specification (P22-ET-09-000-001-0) Table 4-1 defines the brine feed water temperature range as 19-24°C. The Technical Offer Rev.1 Section 7 reports LSI values of 2.0-2.11 at 24°C concentrate conditions. Higher temperature increases LSI and accelerates CaCO3 precipitation kinetics.

**Impact:** The projection at 19°C represents the most favorable operating condition, not the worst case. The 5°C difference affects both saturation indices and crystal growth rates. While 0.5 ppm may still be adequate at 24°C, this has not been demonstrated.

**Required Action:** BW Water shall provide an AWC projection at **24°C feed temperature** confirming that 0.5 ppm Pureflux SW remains sufficient, or alternatively, provide a technical justification explaining why the 19°C projection is representative of worst-case scaling behavior.

---

### Observation 2: Chemical Consumption List Internal Inconsistency

| Field | Value |
|-------|-------|
| Document | P22-LI-09-009-002-A (Chemical Consumption List) |
| Severity | Minor |
| Category | Documentation |

**Finding:** The Chemical Consumption List reports two values for antiscalant consumption that are not internally consistent:

| Parameter | Listed Value | Calculated Cross-Check |
|-----------|-------------|----------------------|
| Volumetric flow | 0.02 L/h | 0.59 kg/day ÷ 24h ÷ 1.031 = **0.0238 L/h** |
| Daily consumption | 0.59 kg/day | 0.02 L/h × 24h × 1.031 = **0.495 kg/day** |

The AWC projection specifies a dosing rate of 0.396 mL/min, which translates to 0.0238 L/h and 0.589 kg/day. This confirms that 0.59 kg/day is the correct value and the volumetric flow should be 0.024 L/h (not 0.02 L/h).

**Impact:** Minor documentation error. Does not affect system operation or equipment sizing, since the dosing pump has 115x capacity margin.

**Required Action:** Update Chemical Consumption List to correct the volumetric flow from 0.02 L/h to 0.024 L/h, or verify which value is the intended design basis.

---

### Observation 3: AWC Projection Input Data — Verified Gaps

| Field | Value |
|-------|-------|
| Document | AWC Projection (PROTON) / CREST Water Email |
| Severity | Major |
| Category | Design Input |

**Finding:** ADASA has cross-checked the AWC PROTON simulation input data against the ANAM Laboratory brine characterization reports (Report Nos. 240123822 and 240123823). Two gaps were confirmed:

1. **Strontium omitted.** The AWC projection uses Sr = 0.00 mg/L as input. The ANAM characterization measured Sr at 10–11 mg/L across both sampling campaigns. Strontium is directly relevant for SrSO4 saturation index calculation, and its omission means the SrSO4 safety margin reported by PROTON has not been validated against actual brine chemistry.

2. **Silica — worst case not used.** The AWC projection uses SiO2 = 2.1 mg/L, which corresponds to the first ANAM sampling only. The second sampling measured 6.4 mg/L. The projection does not reflect the worst-case silica concentration.

Additionally, CREST Water stated that heavy metals data was unavailable, which is incorrect — the ANAM reports include a comprehensive heavy metals analysis. This confirms that BW Water did not provide the complete characterization data to either assessor.

**AWC Input vs ANAM Measured Data — Critical Parameters:**

| Parameter | AWC Input | ANAM 1st Sampling | ANAM 2nd Sampling | Gap |
|-----------|-----------|-------------------|-------------------|-----|
| Sr (mg/L) | 0.00 | 11.226 | 10.067 | NOT INCLUDED |
| SiO2 (mg/L) | 2.10 | 2.1 | 6.4 | Worst-case not used |
| Ba (mg/L) | 0.00 | <0.01 | <0.01 | OK — below detection |
| B (mg/L) | 7.48 | 7.475 | 6.739 | OK |

**Impact:** The SrSO4 saturation index in the AWC projection is based on zero strontium and therefore does not reflect actual brine conditions. While the PROTON report shows a positive safety margin for SrSO4, this margin was computed without the measured 10–11 mg/L Sr concentration. The silica margin may also be understated at higher SiO2 concentrations.

**Required Action:** BW Water shall provide a revised AWC PROTON projection incorporating the measured **Sr concentration (10–11 mg/L)** and **worst-case SiO2 (6.4 mg/L)** from the ANAM characterization, confirming that 0.5 ppm Pureflux SW remains adequate under corrected input data.

---

### Observation 4: Contradictory Assessments Without Resolution

| Field | Value |
|-------|-------|
| Document | BW Water Memorandum |
| Severity | Major |
| Category | Design Decision |

**Finding:** BW Water presents two independent assessments that reach contradictory conclusions:

| Assessor | Conclusion |
|----------|------------|
| **AWC (Pureflux SW)** | 0.5 ppm antiscalant is sufficient; dosing is recommended |
| **CREST Water** | No antiscalant is needed for this application |

The BW Water memorandum presents both assessments side by side but does not take a position on which evaluation forms the basis of design. It does not explain the technical reasons for the discrepancy or indicate which assessment was used to size the antiscalant system.

**Impact:** Without a clear statement of the adopted design basis, there is ambiguity regarding:

- Whether the system is designed to operate with or without antiscalant
- Which scaling model governs the membrane warranty conditions
- What the recommended operating protocol will be during commissioning

**Required Action:** BW Water shall formally state which assessment is adopted as the **design basis** for the antiscalant system and provide a brief explanation for why the alternative assessment is not adopted.

---

## REQUIRED ACTIONS

The following actions are required from BW Water to close CT-001:

| # | Action | Priority | Reference |
|---|--------|----------|-----------|
| 1 | Provide AWC projection at **24°C** feed temperature, or technical justification for 19°C | **High** | OBS-1 |
| 2 | Correct Chemical Consumption List volumetric flow (0.02 → 0.024 L/h) | Low | OBS-2 |
| 3 | Provide revised AWC projection with measured Sr (10–11 mg/L) and worst-case SiO2 (6.4 mg/L) | **High** | OBS-3 |
| 4 | State which assessment (AWC or CREST Water) is the adopted design basis | **High** | OBS-4 |

**Response Deadline:** February 20, 2026

---

## CONCLUSION

The AWC projection for Pureflux SW antiscalant provides reasonable technical justification for the 0.5 ppm dosing rate under the modeled conditions. ADASA accepts this dosing rate in principle, subject to satisfactory resolution of the four observations listed above.

The most significant concern is the projection temperature (19°C vs. the 24°C worst case specified in the Technical Specification). If the 24°C projection confirms adequate margins, CT-001 will be closed with status **"Accepted with observations resolved."**

The substantial dosing pump capacity margin (115x) provides operational flexibility to increase the dosing rate if field conditions require it, which partially mitigates the residual risk.

---

## DOCUMENT HISTORY

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 0 | 16-Feb-2026 | Initial issue - Response evaluation | L. Rivera |

---

## REFERENCE DOCUMENTS

| Document | Code/Reference |
|----------|---------------|
| Technical Query CT-001 | P22-CT-09-000-001-0 (05-Feb-2026) |
| Technical Specification | P22-ET-09-000-001-0, Table 4-1 |
| Chemical Consumption List | P22-LI-09-009-002-A |
| Technical Offer Rev.1 | BW Water Proposal, Section 7 |
| Brine Characterization | ANAM Lab Reports 240123822 / 240123823 |
| AWC Projection | Pureflux SW - PROTON simulation |
| BW Water Memorandum | Response to CT-001 (13-Feb-2026) |
| CREST Water Assessment | Email included in BW Water response |
