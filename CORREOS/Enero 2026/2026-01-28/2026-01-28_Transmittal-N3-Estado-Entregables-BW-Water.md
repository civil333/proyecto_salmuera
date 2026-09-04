---
titulo: "Technical Review Transmittal N3 + Engineering Deliverables Status"
subtitulo: "BAE 12803 - Brine Module Taltal"
codigo: "P22-TM-09-000-003-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Gerencia Tecnica ADASA"
tipo_documento: "Correo"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# Correo: Technical Review Transmittal N3 + Engineering Deliverables Status + Catch-Up Schedule Request

**Date:** January 28, 2026
**From:** Luis Rivera - Contract Administrator
**To:** BW Water Americas Inc. (Marjan Fariborz / Logan Maroney)
**CC:** ADASA Technical Management
**Subject:** Technical Review Transmittal N3 (P22-TM-09-000-003-0) + Engineering Deliverables Status + Catch-Up Schedule Request
**Ref:** Contract C-4300 / BAE 12803 / Baseline Schedule

---

Dear BW Water Team,

We submit Technical Review Transmittal N3 (P22-TM-09-000-003-0) along with an updated Engineering Deliverables Status for the Second Stage RO Brine Module project. We also request a catch-up schedule to support project recovery planning.

---

## 1. TRANSMITTAL N3 - TECHNICAL REVIEW

Attached: Technical Review Transmittal N3 covering the latest submittals received.

### 1.1 Submittal Coverage

| Submittal | Date Received | Documents | Topics |
|-----------|---------------|-----------|--------|
| 25007-0007 | Jan-12-2026 | 6 | Process Calculation Rev.B, HP Pump Rev.B, CIP Tank Rev.B, Chemical List, Line List |
| 25007-0008 | Jan-20-2026 | 12 | PFD Rev.B, Container Rev.B, Turbochargers Rev.B, Equipment List, Valve List, IO List, Instrument List |
| 25007-0009 | Jan-20-2026 | 5 | Electrical Cables DS, Cable Tray DS, Conduit DS, Instrument Layout, Power Cable Schedule |
| **TOTAL** | | **23** | |

### 1.2 Review Statistics

| Verdict | Quantity | % |
|---------|----------|---|
| 1 - Approved | 13 | 57% |
| 2 - Approved as noted | 5 | 22% |
| 3 - To be revised | 5 | 22% |
| **TOTAL** | **23** | 100% |

**Transmittal Verdict: 3 - TO BE REVISED**

### 1.3 Key Observations Requiring Immediate Attention

**Instrumentation Issues (Instrument List P22-LI-09-008-003-A)**

The most critical finding is a duplicate TAG assignment: FIT-09-001 appears both for Cartridge Filter DN100 (Line 4) and 2nd Stage Permeate DN50 (Line 13). This makes PLC addressing impossible and must be corrected before control system programming.

Additionally, vibration transmitters for HP Pump, Feed Turbocharger, and Interstage Turbocharger are not included per ET Section 5.5.7 requirements.

**Pump Temperature Protection (HP Pump Datasheet)**

The datasheet specifies RTDs for bearing temperature but does not include Pt-100 sensors for motor windings. ET Section 5.3 (L1032-1033) requires both. The 87 kW motor with VFD needs winding thermal protection - unless an alternative protection method is documented.

**Valve Actuation (Valve List P22-LI-09-005-002-A)**

VM-09-015 (DN100 Butterfly, ANSI 900#) on HP Pump discharge is specified MANUAL. ET Section 5.2.3 requires electric actuation for relevant process valves. BW Water should either change to motorized actuation or provide technical justification for the manual configuration.

**Control System Integration (IO List P22-LI-09-008-001-A)**

| Issue | Description | Severity |
|-------|-------------|----------|
| VFD variables | Missing electrical parameters (V, I, P, Hz) for SEC verification per ET 5.6 | CRITICAL |
| Coordination signals | System needs DO (module status) and DI (external enable) for plant integration | CRITICAL |

### 1.4 Validated Items (Positive Findings)

| Item | Status | Reference |
|------|--------|-----------|
| Process Calculation - Design Basis | **VALIDATED** | All parameters per ET |
| BiTurbo modeling (43k & 53k TDS) | **VALIDATED** | 10 scenarios included |
| HP Pump operating point | **VALIDATED** | 49 m³/h @ 49.4 bar DP |
| Permeate TDS < 500 mg/L guarantee | **VALIDATED** | < 248 mg/L worst case |
| Permeate chlorides < 400 mg/L | **VALIDATED** | < 146 mg/L worst case |
| Production rate 20 m3/h minimum | **VALIDATED** | 21 m3/h achieved |
| Super Duplex material (PREN > 40) | **VALIDATED** | PREN 42.5 confirmed |
| HART protocol on transmitters | **VALIDATED** | All 4-20mA + HART |
| Conductivity instrumentation (5 locations) | **VALIDATED** | ET 5.5.5 fully covered |

**Download Link for Reviewed Documents:**
https://www.dropbox.com/t/tDInLROUqCSiQlYM

---

## 2. ENGINEERING DELIVERABLES STATUS

Per the Baseline Schedule (12803_Taltal Water Treatment Plant), the Engineering phase was scheduled to complete on **January 5, 2026** (65 days from NTP). This section provides the current status as of January 28, 2026.

### 2.1 Overall Status Summary

| Status | Quantity | % of Engineering Phase |
|--------|----------|------------------------|
| **1 - Approved** | 21 | 33% |
| **2 - Approved as noted** | 13 | 20% |
| **3 - To be revised** | 9 | 14% |
| **4 - Rejected** | 3 | 5% |
| **Not delivered** | 14 | 22% |
| **TOTAL ENGINEERING PHASE** | **64** | 100% |

### 2.2 Key Performance Indicators

| Indicator | Value | Target | Status |
|-----------|-------|--------|--------|
| Documents delivered | 38 of 52 | 52 | **73%** |
| Ready for fabrication (1+2) | 29 of 52 | 52 | **56%** |
| Requiring correction (3+4) | 9 of 38 | 0 | **24%** of delivered |
| Days since Engineering Complete deadline | 23 days | 0 | **DELAYED** |

### 2.3 Critical Pending Documents (14 documents)

The following documents have not been delivered and are critical for project progress:

| # | Document | Baseline Date | Days Delayed |
|---|----------|---------------|--------------|
| 1 | PIE Detallado (ITP) | Dec-31-2025 | **28** |
| 2 | Equipment Layout | Dec-05-2025 | **54** |
| 3 | DS MCC | Nov-19-2025 | **70** |
| 4 | CIP Pump Datasheet (complete) | Nov-13-2025 | **76** |
| 5 | Plant Control Philosophy | Dec-23-2025 | **36** |
| 6 | 3D Model | Dec-29-2025 | **30** |
| 7 | Piping Layout | Dec-30-2025 | **29** |
| 8 | Stress & Flexibility Analysis | Dec-29-2025 | **30** |
| 9 | Maintenance Lifting Points | Dec-29-2025 | **30** |
| 10 | Utility Consumption List | Nov-04-2025 | **85** |
| 11 | High Pressure Isometrics | Dec-29-2025 | **30** |
| 12 | Seismic Calculation | Dec-29-2025 | **30** |
| 13 | Crane Beams / Lifting Points | Dec-29-2025 | **30** |
| 14 | HMI Screen Design | Dec-23-2025 | **36** |

### 2.4 Documents Requiring Correction (9 documents)

| # | Document | Current Verdict | Key Issue |
|---|----------|-----------------|-----------|
| 1 | HP Pump Datasheet | 3 - To be revised | Missing Pt-100 motor windings (unless alternative protection documented) |
| 2 | Valve List | 3 - To be revised | Manual actuation VM-09-015 requires justification per ET 5.2.3; duplicate TAGs |
| 3 | IO List | 3 - To be revised | Missing VFD variables, coordination signals |
| 4 | Instrument List | 3 - To be revised | Duplicate FIT-09-001, missing vibration transmitters |
| 5 | Instrument Location Layout | 3 - To be revised | Inherits Instrument List issues |
| 6 | A/C Thermal Calculation | 3 - To be revised | Heat load calculation incomplete - awaiting revised analysis |
| 7 | Static Mixer Datasheet | 3 - To be revised | Material change FRP to PVC requires technical justification |
| 8 | Antiscalant Tank Datasheet | 3 - To be revised | Pending Rev.B |
| 9 | CIP Pump Datasheet | 3 - To be revised | Incomplete - missing RTD specifications per ET 5.1.4 |

---

## 3. CATCH-UP SCHEDULE REQUEST

The engineering phase currently shows a 23-day delay from baseline. A catch-up schedule will help both parties coordinate recovery efforts and maintain alignment with contracted milestones.

### 3.1 Requested Information

Please provide a recovery plan that includes:

1. **Pending Documents Plan:** Proposed delivery dates for the 14 outstanding engineering documents listed in Section 2.3

2. **Revision Plan:** Re-submission dates for the 9 documents currently marked "To be revised" (Section 2.4)

3. **Milestone Impact Assessment:** Updated dates for key milestones if impact is expected:
   - Engineering Complete (originally Jan-05-2026)
   - Fabrication Start (originally Jan-02-2026)
   - FAT (originally Jul 30-31, 2026)
   - Ready to Ship (originally Aug-03-2026)

4. **Mitigation Actions:** Specific measures to recover the current 23-day delay in the engineering phase

### 3.2 Timeline

Please provide the catch-up schedule within **7 business days** (by **February 6, 2026**) to allow proper coordination and support from ADASA's side.

---

## 4. NEXT STEPS

1. Please confirm receipt of this transmittal
2. Provide the requested catch-up schedule by February 6, 2026
3. Address the critical observations identified in Transmittal N3
4. Schedule a coordination meeting to review the recovery plan if needed

Available for coordination as needed.

Best regards,

**Luis Rivera**
Contract Administrator
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module Taltal

---

## Attachments

- P22-TM-09-000-003-0 - TRANSMITTAL N3 ADASA-BW_WATER.docx
- Annotated documents available at: https://www.dropbox.com/t/tDInLROUqCSiQlYM
- Attachment A: Instrument List with ADASA comments
- Attachment B: Process Calculation with ADASA annotations
- Attachment C: Line List with pressure margin observations
- Attachment G: Cross-reference analysis Instrument List vs P&ID vs IO List
- Attachment H: Pump temperature measurement cross-reference
- Attachment I: Layout cross-reference analysis
- Attachment J: Valve List and Equipment List cross-reference
- Attachment K: Conductivity and Flow instrumentation compliance analysis (P22-CD-09-008-001-0)

---

## Contexto Interno (No enviar)

### Estrategia de Comunicacion
- **Tono:** Colaborativo y constructivo, sin mencionar multas ni penalidades
- **Enfoque:** Solicitar catch-up schedule como herramienta de planificacion conjunta
- **Plazo:** 7 dias habiles es razonable para preparar un cronograma de recuperacion

### Referencias Contractuales (NO incluidas en correo)
- Atraso actual: 23 dias desde termino ingenieria programado (05-Ene-2026)
- Documentos pendientes criticos: 14
- Documentos por corregir: 9
- Multa por atraso: 0.05% diario del monto neto (Contrato C-4300)
- Exposicion potencial: USD 7,061+ (NO MENCIONAR EN CORREO)

### Proximos Pasos si No Hay Respuesta
1. **Dia 3:** Seguimiento cordial por correo
2. **Dia 7:** Segundo seguimiento mencionando la importancia del catch-up schedule
3. **Dia 10:** Escalamiento formal con referencia a obligaciones contractuales (sin mencionar multas especificas)

### Documentos Clave para Fabricacion
Los siguientes documentos son criticos para iniciar fabricacion:
- PIE Detallado (ITP) - **28 dias atraso** - BLOQUEA TODO
- Equipment Layout - **54 dias atraso** - Bloquea piping/3D
- DS MCC - **70 dias atraso** - Bloquea tableros electricos

### Metricas de Seguimiento
| Metrica | Valor 06-Ene | Valor 28-Ene | Tendencia |
|---------|--------------|--------------|-----------|
| Docs entregados | 22 | 50 | +127% |
| Docs aprobados | 12 (55%) | 34 (68%) | +13pp |
| Dias atraso | 1 | 23 | +22 dias |

### Historial de Transmittales
| TM | Fecha | Entregas | Veredicto |
|----|-------|----------|-----------|
| N1 | 16-Dic-2025 | E1+E2 | 4 - Rejected |
| N2 | 26-Ene-2026 | E3-E7 | 3 - To be revised |
| N3 | 28-Ene-2026 | E7-E9 | 3 - To be revised |

---

*Documento creado: 28 de enero de 2026*
*Proyecto: BAE 12803 - Modulo de Salmuera Taltal*
*Contrato: C-4300 BW Water Americas Inc.*
