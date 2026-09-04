---
titulo: "Technical Review Transmittal N4 - Submittal 0010"
subtitulo: "BAE 12803 - Brine Module Taltal"
codigo: "P22-TM-09-000-004-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Gerencia Tecnica ADASA"
tipo_documento: "Correo"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# Correo: Technical Review Transmittal N4 - Submittal 0010

**Date:** February 02, 2026
**From:** Luis Rivera - Contract Administrator
**To:** BW Water Americas Inc. (Marjan Fariborz / Logan Maroney)
**CC:** ADASA Technical Management
**Subject:** Technical Review Transmittal N4 (P22-TM-09-000-004-0) - Submittal 0010 Review
**Ref:** Contract C-4300 / BAE 12803 / Transmittals N2, N3

---

Dear BW Water Team,

We submit Technical Review Transmittal N4 (P22-TM-09-000-004-0) covering the review of Submittal 0010 received January 30, 2026.

---

## 1. TRANSMITTAL N4 - TECHNICAL REVIEW SUMMARY

### 1.1 Documents Reviewed

| # | Code | Title | Rev | Verdict |
|---|------|-------|-----|---------|
| 1 | P22-LI-09-009-001 | Utility Consumption List | A | **3 - To be revised** |
| 2 | P22-ET-09-009-010 | Antiscalant Dosing Tank DS | B | 2 - Approved as noted |

**Transmittal Verdict: 3 - TO BE REVISED**

### 1.2 Key Findings

**Positive:**
- SEC (Specific Energy Consumption) **validated at 3.98 kWh/m3** vs 4.71 kWh/m3 guaranteed (15% favorable margin)
- Antiscalant Tank material change HDPE to LMDPE **accepted** (justified by dimensional constraints)
- Production rate 21 m3/h validated

**Critical Issues:**

| # | Observation | Severity | Status |
|---|-------------|----------|--------|
| OBS-01 | PLC specified at 60 Hz - ET 5.4.7 requires 50 Hz (Chilean grid) | CRITICAL | NEW |
| OBS-02 | Only 1 A/C unit specified - ET 5.1.11 requires n+1 (minimum 2) | CRITICAL | **27 DAYS PENDING (TM N2)** |
| OBS-03 | A/C thermal calculation not delivered - Required per ET 5.1.11 | CRITICAL | **27 DAYS PENDING (TM N2)** |
| OBS-04 | HP Pump has 4 different power values (83/86/92/93 kW) | MAJOR | NEW |
| OBS-05 | CIP Pump power discrepancy (11 kW vs 15 kW Technical Offer) | MAJOR | NEW |

### 1.3 PLC Frequency Observation

The Utility Consumption List specifies PLC power supply as 220V/1PH/60Hz. ET Section 5.4.7 states equipment operating at frequencies other than 50 Hz will not be accepted. If the PLC power supply is dual-frequency (50/60 Hz auto-ranging), please confirm this specification explicitly. If the PLC operates only at 60 Hz, replacement with 50 Hz compatible equipment is required.

---

## 2. PENDING OBSERVATIONS STATUS

Transmittal N4 includes a new Section 4 summarizing pending observations from previous transmittals:

| Origin | Days Pending | Key Items |
|--------|--------------|-----------|
| TM N2 (Jan-06) | **27 days** | A/C n+1 configuration, A/C thermal calculation, Static Mixer material |
| TM N3 (Jan-28) | 5 days | Vibration transmitters, Pt-100 motor windings, VM-09-015 motorized, VFD variables |

The A/C observations (OBS-02, OBS-03) were first raised in Transmittal N2 on January 6, 2026. The Utility Consumption List in Submittal 0010 still shows only 1 A/C unit (2.64 kW), confirming this non-compliance persists.

---

## 3. CATCH-UP SCHEDULE REMINDER

Per our request dated January 28, 2026, we are awaiting the catch-up schedule by **February 6, 2026** (4 days remaining).

The current status shows 52 documents delivered with:
- 34 approved/approved as noted (65%)
- 15 requiring revision (29%)
- 3 rejected (6%)

---

## 4. REQUIRED ACTIONS

### 4.1 Critical Actions (E10)

1. **PLC Frequency:** Confirm dual-frequency compatibility OR replace with 50 Hz equipment
2. **A/C Configuration:** Add 2nd A/C unit per ET 5.1.11 and Technical Offer commitment
3. **A/C Thermal Calculation:** Deliver thermal load document

### 4.2 Major Actions (E10)

4. **HP Pump Power:** Unify values across all documents (Utility List, Load List, Equipment List)
5. **CIP Pump Power:** Clarify correct value (11 kW vs 15 kW)

---

## 5. NEXT STEPS

1. Please confirm receipt of Transmittal N4
2. Provide the catch-up schedule by February 6, 2026 (as previously requested)
3. Address A/C observations that are now 27 days pending
4. Coordinate on PLC frequency confirmation

Available for coordination as needed.

Best regards,

**Luis Rivera**
Contract Administrator
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module Taltal

---

## Attachments

- P22-TM-09-000-004-0 - TRANSMITTAL N4 ADASA-BW_WATER.docx
- Attachment L: P22-LI-09-009-001-A_Utility_Consumption_List_Comments.pdf
- Attachment M: P22-ET-09-009-010-B_Antiscalant_Tank_Comments.pdf

---

## Contexto Interno (No enviar)

### Estrategia de Comunicacion
- **Tono:** Colaborativo pero enfatizando observaciones de larga data (27 dias A/C)
- **Enfoque:** Recordar catch-up schedule deadline (06-Feb) sin repetir solicitud completa
- **Prioridad:** El PLC 60Hz es nuevo, pero A/C n+1 es el tema mas critico por tiempo pendiente

### Observacion PLC 60 Hz - Contexto Tecnico
- Chile usa red electrica de 50 Hz (norma sudamericana)
- La mayoria de PLCs industriales son multi-frecuencia (50/60 Hz auto-ranging)
- Es probable que sea un error de documentacion, no de equipo
- Dejamos apertura para que confirmen compatibilidad dual-frecuencia

### Cronologia A/C n+1
| Fecha | Evento |
|-------|--------|
| 06-Ene-2026 | Primera observacion en TM N2 |
| 26-Ene-2026 | Emision TM N2, sin respuesta A/C |
| 28-Ene-2026 | TM N3 reitera A/C pendiente |
| 30-Ene-2026 | E10 entregada, aun 1 A/C |
| 02-Feb-2026 | TM N4 - 27 dias sin resolver |

### SEC Validation (Positivo)
- SEC calculado: 3.98 kWh/m3
- SEC garantizado: 4.71 kWh/m3 +/- 5%
- Margen favorable: 15%
- Este es el cumplimiento MAS IMPORTANTE del contrato

### Exposicion Contractual (NO MENCIONAR)
- Multa por atraso: 0.05% diario del monto neto
- Dias atraso ingenieria: 28+ dias
- Exposicion acumulada: > USD 8,500
- A/C n+1 puede afectar funcionamiento en Taltal (desierto, temperaturas extremas)

### Proximos Pasos si No Hay Respuesta al Catch-Up Schedule
1. **07-Feb-2026:** Seguimiento formal dia siguiente del deadline
2. **10-Feb-2026:** Segundo seguimiento con escalamiento
3. **14-Feb-2026:** Carta formal mencionando impacto contractual

### Historial de Transmittales Completo
| TM | Fecha | Entregas | Docs | Veredicto |
|----|-------|----------|------|-----------|
| N1 | 16-Dic-2025 | E1+E2 | 20 | 4 - Rejected |
| N2 | 26-Ene-2026 | E3-E7 | 8 | 3 - To be revised |
| N3 | 28-Ene-2026 | E7-E9 | 23 | 3 - To be revised |
| N4 | 02-Feb-2026 | E10 | 2 | 3 - To be revised |

---

*Documento creado: 02 de febrero de 2026*
*Proyecto: BAE 12803 - Modulo de Salmuera Taltal*
*Contrato: C-4300 BW Water Americas Inc.*
