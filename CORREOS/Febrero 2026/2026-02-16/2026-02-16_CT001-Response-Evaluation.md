---
titulo: "CT-001 Response Evaluation - Cover Email"
codigo: "CORREO-2026-02-16"
fecha: "2026-02-16"
autor: "Luis Rivera"
destinatario: "Eduardo Yamauchi (BW Water)"
tipo: "Correo formal"
estado: "Borrador"
relacionado: "P22-CT-09-000-001-1"
---

# CT-001 Response Evaluation — Cover Email

**Date:** February 16, 2026
**From:** Luis Rivera Gonzalez - Leader, Infrastructure Engineering (ADASA)
**To:** Eduardo Yamauchi - Operations Director Americas (BW Water)
**CC:** ADASA Technical Management; BW Water Engineering Team
**Subject:** Technical Query CT-001 — Response Evaluation and Pending Observations (C-4300)
**Ref:** Contract C-4300 / BAE 12803
**Attachments:** P22-CT-09-000-001-1 (Response Evaluation — Antiscalant Dosing Justification)

---

Dear Eduardo,

We have completed our evaluation of BW Water's response to Technical Query CT-001 (Antiscalant Dosing Justification). The response was received on **February 13, 2026**, three days after the agreed deadline of February 10. Three documents were submitted: a BW Water Memorandum, an AWC projection for Pureflux SW antiscalant, and a CREST Water assessment email.

The formal evaluation document (P22-CT-09-000-001-1) is attached. This email summarizes the main findings.

**Acceptance**

ADASA accepts in principle the **0.5 ppm dosing rate** for Pureflux SW antiscalant. The AWC PROTON simulation confirms positive safety margins for CaCO₃, CaSO₄, BaSO₄, SrSO₄, and silica scaling under the modeled conditions. The dosing pump's 115x capacity margin provides adequate operational flexibility.

This acceptance is conditional on the satisfactory resolution of four observations identified during our review.

**Pending Observations**

**Temperature basis (Major).** The AWC projection was run at 19°C feed temperature. CT-001 specifically requested validation at 24°C, which is the worst-case condition per the Technical Specification Table 4-1. Higher temperature increases both saturation indices and crystal growth rates. We need either a revised projection at 24°C or a technical justification explaining why 19°C is representative.

**Chemical Consumption List inconsistency (Minor).** The volumetric flow listed as 0.02 L/h does not reconcile with the 0.59 kg/day daily consumption. Cross-checking against the AWC dosing rate (0.396 mL/min), the correct value should be 0.024 L/h. This is a documentation correction and does not affect equipment sizing.

**AWC projection input data (Major).** ADASA has verified the AWC PROTON input data against the ANAM brine characterization. Strontium was entered as 0.00 mg/L in the AWC simulation, while the ANAM reports measured 10–11 mg/L — directly relevant for SrSO₄ scaling. Silica was entered as 2.1 mg/L (first sampling only), not the worst-case 6.4 mg/L from the second sampling. A revised AWC projection incorporating these measured values is required.

**Contradictory conclusions (Major).** AWC concludes that 0.5 ppm antiscalant is needed; CREST Water concludes that no antiscalant is necessary. The BW Water memorandum presents both assessments without stating which one forms the design basis. We need a clear statement of the adopted position and the reasoning behind it.

**Required Actions Summary**

| # | Action | Priority | Ref |
|---|--------|----------|-----|
| 1 | AWC projection at 24°C, or technical justification for 19°C | High | OBS-1 |
| 2 | Correct volumetric flow in Chemical Consumption List (0.02 → 0.024 L/h) | Low | OBS-2 |
| 3 | Revised AWC projection with Sr (10–11 mg/L) and worst-case SiO₂ (6.4 mg/L) | High | OBS-3 |
| 4 | State adopted design basis: AWC or CREST Water | High | OBS-4 |

**Response deadline: February 20, 2026.**

The full evaluation with detailed findings is in the attached document. Please do not hesitate to reach out if you need to discuss any of the observations or coordinate the response.

Best regards,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module Taltal

---

## Contexto Interno (No enviar)

### Timeline CT-001

| Fecha | Evento |
|-------|--------|
| 05-Feb-2026 | CT-001 emitida (P22-CT-09-000-001-0) - deadline 10-Feb |
| 10-Feb-2026 | Deadline vencida sin respuesta |
| 12-Feb-2026 | Correo recordatorio Outstanding Responses (TM N3, N4 + CT-001) |
| 13-Feb-2026 | BW Water responde CT-001 (3 días tarde) con 3 documentos |
| 16-Feb-2026 | ADASA emite evaluación (P22-CT-09-000-001-1) + este correo |
| 20-Feb-2026 | Deadline respuesta observaciones pendientes (cierre anti-escalamiento) |

### Documentos recibidos de BW Water
1. **BW Water Memorandum** — Cover letter con resumen de dos evaluaciones independientes
2. **AWC Projection (Pureflux SW)** — Simulación PROTON a 19°C (no 24°C worst-case)
3. **CREST Water Email** — Opinión de tercero sin datos de metales pesados

### Evaluación general
- Dosing rate 0.5 ppm aceptado en principio (AWC confirma márgenes positivos)
- 4 observaciones pendientes: 3 Major + 1 Minor
- Observación más crítica: temperatura 19°C vs 24°C worst-case
- AWC PROTON usó Sr=0.00 (ANAM midió 10-11 mg/L) y SiO2=2.1 (worst-case 6.4)
- CREST Water trabajó sin datos completos de caracterización ANAM
- Contradicción AWC vs CREST no resuelta en memorándum BW Water
