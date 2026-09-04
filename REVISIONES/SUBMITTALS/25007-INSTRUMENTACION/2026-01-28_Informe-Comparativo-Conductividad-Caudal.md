# Informe Comparativo: Instrumentacion de Conductividad y Caudal

**Codigo:** P22-CD-09-008-001-0
**Fecha:** 28 de enero de 2026
**Revision:** 0
**Preparado por:** ADASA - Ingenieria de Proyectos

---

## 1. RESUMEN EJECUTIVO

### 1.1 Objetivo

Verificar el cumplimiento de la instrumentacion de conductividad y caudal propuesta por BW Water contra los requisitos contractuales establecidos en las Especificaciones Tecnicas (ET) del proyecto BAE 12803 - Planta Modular UHPRO Taltal.

### 1.2 Hallazgos Principales

| Variable | ET Requiere | Oferta Tecnica | Instrument List | Estado |
|----------|-------------|----------------|-----------------|--------|
| **Conductividad** | 5 ubicaciones | 1 instrumento | **5 instrumentos** | **CUMPLE** |
| **Caudal** | 5 ubicaciones | 4 instrumentos | **4 TAGs unicos** | **TAG DUPLICADO** |

### 1.3 Veredicto

**3 - TO BE REVISED**

La Instrument List cubre todas las ubicaciones requeridas por la ET para conductividad y caudal. Sin embargo, se detecta un **error critico de codificacion**: el TAG **FIT-09-001 esta DUPLICADO** (Items 4 y 13), lo que requiere correccion inmediata antes de continuar con la ingenieria de detalle.

---

## 2. DOCUMENTOS ANALIZADOS

| Documento | Codigo | Revision | Fecha | Fuente |
|-----------|--------|----------|-------|--------|
| Especificacion Tecnica Modulo OI | P22-ET-09-000-001-0 | 0 | Sep-2025 | ADASA |
| Oferta Tecnica BW Water | - | **Rev.1** | Oct-2025 | BW Water |
| P&ID Sistema UHPRO | P22-DWG-09-009-002-A | A | Dic-2025 | BW Water |
| Instrument List | P22-LI-09-008-003-A | A | Ene-2026 | BW Water |

---

## 3. REQUISITOS CONTRACTUALES (ET P22-ET-09-000-001-0)

### 3.1 Conductimetros (Seccion 5.5.5, Lineas 1363-1389)

La ET establece los siguientes puntos de medicion de conductividad:

| # | Ubicacion Requerida | Proposito |
|---|---------------------|-----------|
| 1 | Alimentacion al modulo | Monitoreo calidad entrada |
| 2 | Salida de permeado | Verificacion garantia TDS |
| 3 | Salida de permeado de segunda etapa | Control de proceso |
| 4 | Salida de rechazo de primera etapa | Monitoreo interstage |
| 5 | Salida de rechazo | Balance de masas |

**Cita ET Sec. 5.5.5:**
> "Se instalaran conductimetros en los siguientes puntos: alimentacion al modulo, salida de permeado, salida de permeado de segunda etapa, salida de rechazo de primera etapa, y salida de rechazo."

### 3.2 Caudalimetros (Seccion 5.5.1, Lineas 1313-1320)

La ET establece los siguientes puntos de medicion de caudal:

| # | Ubicacion Requerida | Proposito |
|---|---------------------|-----------|
| 1 | Alimentacion al modulo | Balance de masas, control HP pump |
| 2 | Salida permeado del rack 2da Etapa | Verificacion recuperacion |
| 3 | Salida de permeado | Verificacion garantia capacidad |
| 4 | Salida de rechazo | Balance de masas |
| 5 | Salida filtro cartucho CIP | Control sistema CIP |

**Cita ET Sec. 5.5.1:**
> "Se instalaran caudalimetros en: alimentacion al modulo, salida permeado del rack de segunda etapa, salida de permeado, salida de rechazo, y salida del filtro cartucho del sistema CIP."

### 3.3 Protocolo de Comunicacion (Seccion 5.5, Linea 1311)

**Requisito:** Todos los transmisores deben operar con protocolo **4-20mA + HART**.

> "Todos los transmisores de instrumentacion deberan disponer de protocolo de comunicacion 4-20 mA + HART."

---

## 4. COMPROMISOS OFERTA TECNICA (Rev.1)

### 4.1 Conductividad

La Oferta Tecnica Rev.1 lista **1 instrumento** de conductividad:

| Item | Descripcion | Marca | Ubicacion |
|------|-------------|-------|-----------|
| 16 | Analytical Transmitter CONDUCTIVITY | EMERSON/ABB | RO TRAIN COMBINED PERMEATE |

**Observacion:** La oferta solo menciona 1 conductimetro para permeado combinado. Las 4 ubicaciones restantes no se mencionan explicitamente.

### 4.2 Caudal

La Oferta Tecnica Rev.1 lista **4 instrumentos** de caudal:

| Item | Descripcion | Marca | Ubicacion |
|------|-------------|-------|-----------|
| 13 | Flow Transmitter | ROSEMOUNT/ABB | RO TRAIN COMBINED PERMEATE |
| 14 | Flow Transmitter | ROSEMOUNT/ABB | RO TRAIN STAGE 2 PERMEATE |
| 15 | Flow Transmitter | ROSEMOUNT/ABB | RO TRAIN REJECT |
| 33 | Flow Transmitter | ROSEMOUNT/ABB | CIP TO RO TRAIN |

**Observacion:** La oferta NO menciona caudalimetro para alimentacion al modulo.

---

## 5. IMPLEMENTACION INSTRUMENT LIST (P22-LI-09-008-003-A)

### 5.1 Conductimetros Incluidos

La Instrument List Rev.A incluye **5 conductimetros**:

| # | TAG | Descripcion | Marca/Modelo | Rango Operativo | Rango Max | Protocolo |
|---|-----|-------------|--------------|-----------------|-----------|-----------|
| 3 | CIT-09-001 | RO Cartridge Filter Discharge | Rosemount 400 / 1056400-13 | 0-2000 uS/cm | 0-20 mS/cm | 4-20mA HART |
| 12 | CIT-09-002 | RO Train Permeate | Rosemount 400 / 1056400-13 | 0-200 uS/cm | 0-200 uS/cm | 4-20mA HART |
| 18 | CIT-09-003 | RO Stage 2 Permeate | Rosemount 400 / 1056400-13 | 0-200 uS/cm | 0-200 uS/cm | 4-20mA HART |
| 17 | CIT-09-004 | RO Stage 1 Reject | Rosemount 400 / 1056400-13 | 0-12 mS/cm | 0-20 mS/cm | 4-20mA HART |
| 20 | CIT-09-005 | RO Train Reject | Rosemount 400 / 1056400-13 | 0-12 mS/cm | 0-20 mS/cm | 4-20mA HART |

### 5.2 Caudalimetros Incluidos

La Instrument List Rev.A incluye **5 entradas de caudalimetros**, pero con un **TAG DUPLICADO**:

| # | TAG | Descripcion | Marca/Modelo | Rango Operativo | Rango Max | DN | Protocolo |
|---|-----|-------------|--------------|-----------------|-----------|-----|-----------|
| 4 | FIT-09-001 | RO Cartridge Filter Discharge | Rosemount 8750W | 0-49 m3/h | 0-100 m3/h | DN100 | 4-20mA HART |
| 13 | **FIT-09-001** | **RO 2nd Stage Permeate** | Rosemount 8750W | 0-9 m3/h | 0-18 m3/h | DN50 | 4-20mA HART |
| 11 | FIT-09-003 | RO Train Permeate | Rosemount 8750W | 0-21 m3/h | 0-40 m3/h | DN80 | 4-20mA HART |
| 21 | FIT-09-004 | RO Train Reject | Rosemount 8750W | 0-28 m3/h | 0-60 m3/h | DN65 | 4-20mA HART |
| 29 | FIT-09-005 | CIP Pump Discharge | Rosemount 8750W | 0-54 m3/h | 0-100 m3/h | DN100 | 4-20mA HART |

**ALERTA CRITICA:** El TAG FIT-09-001 aparece DOS VECES con ubicaciones completamente diferentes:
- Item 4: Alimentacion (DN100, 0-49 m3/h)
- Item 13: Permeado 2da etapa (DN50, 0-9 m3/h)

---

## 6. MATRIZ COMPARATIVA

### 6.1 Conductividad

| # | Requisito ET (Sec. 5.5.5) | Oferta Rev.1 | TAG IL | Descripcion IL | **CUMPLE** |
|---|---------------------------|--------------|--------|----------------|------------|
| 1 | Alimentacion al modulo | NO | CIT-09-001 | RO Cartridge Filter Discharge | **SI** |
| 2 | Salida de permeado | Item 16 | CIT-09-002 | RO Train Permeate | **SI** |
| 3 | Salida permeado 2da etapa | NO | CIT-09-003 | RO Stage 2 Permeate | **SI** |
| 4 | Salida rechazo 1ra etapa | NO | CIT-09-004 | RO Stage 1 Reject | **SI** |
| 5 | Salida de rechazo | NO | CIT-09-005 | RO Train Reject | **SI** |

**Resultado Conductividad:** 5/5 ubicaciones cubiertas. **CUMPLE REQUISITOS ET.**

### 6.2 Caudal

| # | Requisito ET (Sec. 5.5.1) | Oferta Rev.1 | TAG IL | Descripcion IL | **CUMPLE** |
|---|---------------------------|--------------|--------|----------------|------------|
| 1 | Alimentacion al modulo | NO | FIT-09-001 | RO Cartridge Filter Discharge | **SI** |
| 2 | Salida permeado 2da etapa | Item 14 | FIT-09-001 | RO 2nd Stage Permeate | **TAG DUPLICADO** |
| 3 | Salida de permeado | Item 13 | FIT-09-003 | RO Train Permeate | **SI** |
| 4 | Salida de rechazo | Item 15 | FIT-09-004 | RO Train Reject | **SI** |
| 5 | Salida filtro CIP | Item 33 | FIT-09-005 | CIP Pump Discharge | **SI** |

**Resultado Caudal:** 5/5 ubicaciones cubiertas, PERO con TAG duplicado que requiere correccion.

---

## 7. OBSERVACIONES

### OBS-01: TAG DUPLICADO FIT-09-001 (CRITICO)

| Campo | Valor |
|-------|-------|
| **Documento** | Instrument List P22-LI-09-008-003-A |
| **Ubicacion** | Items 4 y 13 |
| **Categoria** | Tecnico |
| **Severidad** | **CRITICO** |

**Descripcion:**
El TAG FIT-09-001 aparece asignado a DOS ubicaciones completamente diferentes:

| Item | TAG | Ubicacion | DN | Rango |
|------|-----|-----------|-----|-------|
| 4 | FIT-09-001 | RO Cartridge Filter Discharge | DN100 | 0-49 m3/h |
| 13 | FIT-09-001 | RO 2nd Stage Permeate | DN50 | 0-9 m3/h |

**Impacto:**
1. Violacion de estandar de codificacion ADASA (P00-IT-00-000-101)
2. Imposibilidad de distinguir senales en sistema PLC/SCADA
3. Mapeo incorrecto en IO List
4. Imposibilidad de verificar garantias de desempeno por etapa

**Accion Requerida:**
Corregir Item 13 asignando TAG **FIT-09-002** al caudalimetro de permeado de segunda etapa. Actualizar IO List y P&ID consecuentemente.

---

### OBS-02: Discrepancia Cantidad Conductimetros Oferta vs IL

| Campo | Valor |
|-------|-------|
| **Documento** | Oferta Tecnica Rev.1 vs Instrument List |
| **Categoria** | Contractual |
| **Severidad** | MAYOR |

**Descripcion:**
La Oferta Tecnica Rev.1 menciona solo **1 conductimetro** (Item 16 - Combined Permeate), mientras que la Instrument List incluye **5 conductimetros** que cubren todos los requisitos de la ET.

**Pregunta Contractual:**
¿Los 4 conductimetros adicionales (alimentacion, permeado 2da etapa, rechazo 1ra etapa, rechazo final) estan incluidos en el suministro contractual?

**Accion Requerida:**
Solicitar confirmacion escrita de que los 5 conductimetros listados en P22-LI-09-008-003-A estan incluidos en el alcance de suministro del Contrato C-4300.

---

### OBS-03: Caudalimetro Alimentacion No en Oferta

| Campo | Valor |
|-------|-------|
| **Documento** | Oferta Tecnica Rev.1 |
| **Categoria** | Contractual |
| **Severidad** | MENOR |

**Descripcion:**
La Oferta Tecnica no lista explicitamente un caudalimetro para la alimentacion al modulo. Sin embargo, la Instrument List incluye FIT-09-001 "RO Cartridge Filter Discharge" que cumple este requisito.

**Accion Requerida:**
Confirmar inclusion del caudalimetro de alimentacion (FIT-09-001) en el suministro contractual.

---

### OBS-04: TAG FIT-09-002 No Existe

| Campo | Valor |
|-------|-------|
| **Documento** | Instrument List P22-LI-09-008-003-A |
| **Categoria** | Tecnico |
| **Severidad** | MAYOR |

**Descripcion:**
La secuencia de TAGs de caudalimetros salta de FIT-09-001 a FIT-09-003, sin existir FIT-09-002. Esto es consecuencia directa de OBS-01 (TAG duplicado).

**Accion Requerida:**
Al corregir OBS-01, asignar TAG FIT-09-002 al caudalimetro de permeado de segunda etapa.

---

### OBS-05: Discrepancia de Marca (EMERSON/ABB vs Rosemount)

| Campo | Valor |
|-------|-------|
| **Documento** | Oferta Rev.1 vs Instrument List |
| **Categoria** | Tecnico |
| **Severidad** | MENOR |

**Descripcion:**
La Oferta indica marcas "EMERSON/ABB" para conductimetros, mientras que la Instrument List especifica "Rosemount".

**Mitigacion:**
Rosemount es una division de Emerson. La marca cumple los requisitos de la ET Seccion 5.5 (marca reconocida con presencia en Chile).

**Accion Requerida:**
Ninguna accion requerida. Discrepancia aclarada.

---

### OBS-06: Rango Conductimetro Permeado - Verificar Adecuacion

| Campo | Valor |
|-------|-------|
| **Documento** | Instrument List P22-LI-09-008-003-A |
| **TAG** | CIT-09-002 |
| **Categoria** | Tecnico |
| **Severidad** | REVISAR |

**Descripcion:**
El conductimetro CIT-09-002 (RO Train Permeate) tiene rango 0-200 uS/cm.

**Analisis:**
- Garantia de TDS permeado: <= 500 mg/l (ET Sec. 10.1)
- Factor tipico TDS/Conductividad para permeado RO: 0.5-0.7
- 500 mg/l TDS equivale aproximadamente a 700-1000 uS/cm
- Rango del instrumento (0-200 uS/cm) cubre hasta ~140 mg/l TDS

**Pregunta:**
Si el permeado opera cerca del limite de garantia (500 mg/l TDS), el instrumento estaria **fuera de rango**. ¿Es el rango de 0-200 uS/cm apropiado para las condiciones operativas esperadas?

**Accion Requerida:**
Solicitar a BW Water confirmacion de que el rango de CIT-09-002 es adecuado considerando:
1. Calidad esperada del permeado en operacion normal
2. Capacidad de verificar cumplimiento de garantia TDS <= 500 mg/l

---

## 8. VERIFICACION GARANTIAS DE DESEMPENO

### 8.1 Referencia: ET Seccion 10.1

| Garantia | Valor Garantizado | Instrumento Verificacion | TAG IL | Rango | Estado |
|----------|-------------------|-------------------------|--------|-------|--------|
| Capacidad Nominal | 480 m3/dia (20 m3/h) | Caudalimetro permeado | FIT-09-003 | 0-21 m3/h op / 0-40 max | **ADECUADO** |
| TDS Permeado | <= 500 mg/l | Conductimetro permeado | CIT-09-002 | 0-200 uS/cm | **VERIFICAR** |
| Cloruros Permeado | <= 400 mg/l | Analisis laboratorio | N/A | - | N/A |
| SEC | 4.71 kWh/m3 +/- 5% | FIT + Medidor energia | FIT-09-003 + EIT | - | **VERIFICAR** |

### 8.2 Analisis de Rangos

**Capacidad (FIT-09-003):**
- Rango operativo: 0-21 m3/h
- Capacidad garantizada: 20 m3/h
- **Evaluacion:** El rango es **ADECUADO**. El punto de operacion garantizado (20 m3/h) esta dentro del rango operativo con margen.

**TDS via Conductividad (CIT-09-002):**
- Rango: 0-200 uS/cm (~0-140 mg/l TDS)
- Garantia: <= 500 mg/l TDS (~700-1000 uS/cm)
- **Evaluacion:** **INSUFICIENTE** si el permeado opera cerca del limite de garantia. Ver OBS-06.

---

## 9. CONCLUSION

### 9.1 Cumplimiento General

| Aspecto | Evaluacion |
|---------|------------|
| Conductimetros - Cantidad | **CUMPLE** (5/5 ubicaciones) |
| Conductimetros - Protocolo | **CUMPLE** (4-20mA HART) |
| Conductimetros - Marca | **CUMPLE** (Rosemount/Emerson) |
| Caudalimetros - Cantidad | **CUMPLE** (5/5 ubicaciones) |
| Caudalimetros - Protocolo | **CUMPLE** (4-20mA HART) |
| Caudalimetros - TAGs | **NO CUMPLE** (TAG duplicado) |
| Verificacion Garantia Capacidad | **CUMPLE** |
| Verificacion Garantia TDS | **VERIFICAR** rango instrumento |

### 9.2 Veredicto Final

**3 - TO BE REVISED**

La Instrument List P22-LI-09-008-003-A **cubre todas las ubicaciones** requeridas por la ET para instrumentacion de conductividad y caudal. Sin embargo, el documento **requiere revision** debido a:

1. **Error critico:** TAG FIT-09-001 duplicado (debe corregirse a FIT-09-002 para permeado 2da etapa)
2. **Verificacion pendiente:** Rango de CIT-09-002 para condiciones cercanas al limite de garantia

---

## 10. ACCIONES REQUERIDAS A BW WATER

| # | Accion | Prioridad | Documento Afectado | Plazo |
|---|--------|-----------|-------------------|-------|
| 1 | **Corregir TAG duplicado FIT-09-001** - Asignar FIT-09-002 a caudalimetro permeado 2da etapa | **CRITICA** | Instrument List Rev.B | Inmediato |
| 2 | Actualizar IO List con TAG corregido (FIT-09-002) | ALTA | IO List Rev.B | Con Rev. IL |
| 3 | Verificar que P&ID refleje TAGs correctos | ALTA | P&ID | Con Rev. IL |
| 4 | Confirmar que 5 conductimetros estan incluidos en suministro contractual | MEDIA | Respuesta tecnica | 5 dias |
| 5 | Confirmar adecuacion de rango CIT-09-002 (0-200 uS/cm) para verificar garantia TDS | MEDIA | Respuesta tecnica | 5 dias |
| 6 | Confirmar inclusion de FIT-09-001 (alimentacion) en suministro | BAJA | Respuesta tecnica | 5 dias |

---

## ANEXOS

### Anexo A: Referencias Normativas

- P22-ET-09-000-001-0: Especificacion Tecnica Modulo de Osmosis Inversa
- P00-IT-00-000-101: Codificacion de Documentos ADASA
- ISA-5.1: Instrumentation Symbols and Identification

### Anexo B: Documentos Relacionados

- P22-LI-09-008-003-A: Instrument List
- P22-LI-09-008-001-A: IO List
- P22-DWG-09-009-002-A: P&ID Sistema UHPRO
- P22-TM-09-000-003-0: Transmittal N3 (donde se reporto inicialmente OBS FIT-09-001)

---

*Documento preparado por ADASA - Ingenieria de Proyectos*
*Fecha: 28 de enero de 2026*
