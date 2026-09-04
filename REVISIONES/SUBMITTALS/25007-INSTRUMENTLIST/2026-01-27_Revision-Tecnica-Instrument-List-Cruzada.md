# Revision Tecnica Cruzada - Instrument List P22-LI-09-008-003

**Submittal:** 25007-INSTRUMENTLIST
**Fecha Revision:** 27-Ene-2026
**Revisor:** ADASA
**Version:** 1.0
**Tipo:** Revision Cruzada (Cross-Reference Check)

---

## 1. Resumen Ejecutivo

### 1.1 Objetivo

Verificar la consistencia del Instrument List (P22-LI-09-008-003 Rev.A) contra:
- P&ID (P22-DWG-09-009-002-A)
- IO List (P22-LI-09-008-001 Rev.A)
- Estandar de Codificacion ADASA (P00-IT-00-000-101)

### 1.2 Hallazgos Criticos

| Severidad | Cantidad | Descripcion |
|-----------|----------|-------------|
| **CRITICO** | 1 | TAG FIT-09-001 duplicado con diferentes especificaciones |
| MAYOR | 4 | Instrumentos faltantes, discrepancias TAG, senales I/O ausentes |
| MENOR | 2 | Inconsistencias nomenclatura, tipo DPS no definido |
| **TOTAL** | 7 | - |

### 1.3 Veredicto

| Campo | Valor |
|-------|-------|
| **VEREDICTO** | **3 - TO BE REVISED** |
| Justificacion | Error critico de duplicidad impide direccionamiento univoco en PLC |

---

## 2. Documentos Analizados

| Documento | Codigo | Revision | Fecha | Ubicacion |
|-----------|--------|----------|-------|-----------|
| Instrument List | P22-LI-09-008-003 | A | 15-Ene-2026 | ENTREGA 8/md/ |
| P&ID | P22-DWG-09-009-002 | A | 09-Dic-2025 | ENTREGA 3/md/ |
| IO List | P22-LI-09-008-001 | A | 11-Ene-2026 | ENTREGA 8/md/ |
| Codificacion General | P00-IT-00-000-101 | 0 | 19-Jun-2023 | BASES TECNICAS/md/ |

---

## 3. Observaciones Previas (Referencia)

La siguiente observacion fue documentada en la revision de Entrega 8 (25007-0008) y **NO SE REPITE** en este documento:

| Codigo | Titulo | Estado |
|--------|--------|--------|
| OBS-04 (E8) | Faltan transmisores de vibracion (VT) para HP Pump BH-09-001 y Turbochargers SIP-09-001/002 segun ET 5.5.7 | Pendiente respuesta BW Water |

---

## 4. Hallazgos Nuevos

### OBS-IL-01: TAG FIT-09-001 Duplicado con Diferentes Especificaciones

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 Instrument List |
| Ubicacion | Lineas 4 y 13 |
| Categoria | Tecnico |
| Severidad | **CRITICO** |

**Descripcion:**

El TAG **FIT-09-001** aparece dos veces en el Instrument List con especificaciones completamente diferentes:

| Linea | TAG | Descripcion | Diametro | Rango | Modelo |
|-------|-----|-------------|----------|-------|--------|
| 4 | FIT-09-001 | RO Cartridge Filter Discharge Flow Transmitter | DN100 | 0-100 m3/h | 8750WDMT2A2FTSB0**40**CA1 |
| 13 | FIT-09-001 | RO 2nd Stage Permeate Flow Transmitter | DN50 | 0-18 m3/h | 8750WDMT2A2FTSB0**20**CA1 |

**Impacto:**
- Direccionamiento PLC ambiguo - imposible determinar cual FIT-09-001 se referencia
- Confusion en cableado y configuracion de I/O
- Error critico para puesta en marcha

**Requisito:**
- Cada TAG debe ser unico e inequivoco (principio basico ISA 5.1)

**Accion Requerida:**
- Renumerar uno de los transmisores de caudal
- Sugerencia: El transmisor en linea 13 (2nd Stage Permeate) deberia ser **FIT-09-002**

---

### OBS-IL-02: Instrumentos CIT-09-006 y FIT-09-002 Ausentes en Instrument List

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 vs P22-LI-09-008-001 |
| Pagina/Seccion | IO List lineas 28 y 40 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

Los siguientes instrumentos aparecen en el IO List pero **NO** en el Instrument List:

| TAG IO List | Descripcion IO List | En Instrument List |
|-------------|--------------------|--------------------|
| CIT09-006-XQ001 | Interstage Turbocharger Inlet Conductivity Analyzer | **NO** |
| FIT09-002-XQ001 | RO 2nd Stage Permeate Flow Transmitter | **NO** |

**Analisis:**
- **CIT-09-006:** El IO List indica un analizador de conductividad en la entrada del turbocharger interstage (P9). Este instrumento NO esta en el Instrument List.
- **FIT-09-002:** El IO List indica un transmisor de caudal para 2nd Stage Permeate (P9). En el Instrument List la linea 13 usa FIT-09-001 (duplicado) para esta ubicacion.

**Requisito:**
- Consistencia entre IO List e Instrument List

**Accion Requerida:**
1. Agregar CIT-09-006 al Instrument List con especificaciones completas
2. Corregir TAG de 2nd Stage Permeate Flow a FIT-09-002 (resuelve OBS-IL-01)

---

### OBS-IL-03: Discrepancia TAG LIT-09-001 vs LIT-09-002

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 vs P22-LI-09-008-001 |
| Pagina/Seccion | Instrument List linea 24 vs IO List linea 70 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

| Documento | TAG | Descripcion | P&ID Page |
|-----------|-----|-------------|-----------|
| Instrument List (linea 24) | **LIT-09-001** | CIP Tank Level Transmitter | P10 |
| IO List (linea 70) | **LIT09-002**-XQ001 | CIP Tank Level Transmitter | P10 |

Ambos documentos refieren al mismo instrumento fisico (nivel del tanque CIP en P10), pero usan TAGs diferentes.

**Impacto:**
- Discrepancia en programacion PLC
- Confusion en documentacion as-built

**Requisito:**
- Consistencia de TAGs entre documentos de ingenieria

**Accion Requerida:**
- Unificar el TAG del transmisor de nivel CIP Tank
- Verificar cual es el TAG correcto segun P&ID

---

### OBS-IL-04: Transmisores sin Senales I/O Asignadas

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 vs P22-LI-09-008-001 |
| Pagina/Seccion | Multiple |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

Los siguientes transmisores aparecen en el Instrument List con tipo de senal "AI" pero **NO** tienen entrada correspondiente en el IO List:

| TAG IL | Descripcion | IO Type | En IO List |
|--------|-------------|---------|------------|
| PIT-09-005 | RO Stage 2 Feed Pressure Transmitter | AI | **NO ENCONTRADO** |
| CIT-09-004 | RO Stage 1 Reject Conductivity Analyzer | AI | **NO ENCONTRADO** |
| TIT-09-001 | CIP Tank Temperature Transmitter | AI | **NO ENCONTRADO** |

**Nota sobre busqueda:**
- Se busco en IO List por patrones: PIT09-005, PIT-09-005, 09-005
- No se encontraron coincidencias para estos TAGs

**Verificacion IO List disponibles:**
- PIT09-001 a PIT09-004: Presentes
- PIT09-006 a PIT09-009: Presentes
- **PIT09-005: AUSENTE**

**Impacto:**
- Transmisores instalados sin conexion al PLC
- Senales no monitoreadas por sistema de control

**Requisito:**
- Todo transmisor con senal 4-20mA debe tener entrada AI en IO List

**Accion Requerida:**
- Agregar PIT-09-005, CIT-09-004 y TIT-09-001 al IO List con sus senales AI correspondientes

---

### OBS-IL-05: Inconsistencia Nomenclatura P&ID vs Instrument List

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 vs P22-DWG-09-009-002 |
| Pagina/Seccion | Multiple |
| Categoria | Tecnico |
| Severidad | **MENOR** |

**Descripcion:**

El P&ID utiliza nomenclatura diferente al Instrument List para algunos tipos de instrumentos:

| Funcion | TAG en P&ID | TAG en Instrument List | Discrepancia |
|---------|-------------|------------------------|--------------|
| ORP Analyzer | AIT-09-001 | ORPIT-09-001 | AIT vs ORPIT |
| Conductivity | AIT-09-002/003/005 | CIT-09-001 to 006 | AIT vs CIT |
| Level Indicator | LI-09-001 | LIT-09-001 | LI vs LIT |

**Analisis:**
- El P&ID usa nomenclatura generica "AIT" (Analyzer Indicator Transmitter)
- El Instrument List usa nomenclatura especifica segun variable medida (ORPIT, CIT)
- Ambas aproximaciones son validas segun ISA 5.1
- La nomenclatura del Instrument List es mas descriptiva y preferible

**Impacto:**
- Confusion menor al cruzar documentos
- No afecta funcionalidad

**Requisito:**
- Se recomienda actualizar P&ID con nomenclatura especifica en proxima revision

**Accion Requerida:**
- Documentar en leyenda del P&ID la equivalencia de nomenclaturas
- Actualizar P&ID en revision para construccion (Rev.0)

---

### OBS-IL-06: Tipo DPS No Definido en Estandar Codificacion ADASA

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-003 vs P00-IT-00-000-101 |
| Pagina/Seccion | IL linea 1 vs Tabla 3-3 |
| Categoria | Documental |
| Severidad | **MENOR** |

**Descripcion:**

El Instrument List incluye el instrumento **DPS-09-001** (Differential Pressure Switch) en linea 1, pero el tipo "DPS" no esta definido en la Tabla 3-3 del estandar de codificacion ADASA (P00-IT-00-000-101).

**Tipos de presion definidos en Tabla 3-3:**
| TAG | Descripcion |
|-----|-------------|
| PIT | Transmisor de presion |
| DPIT | Transmisor de presion diferencial |
| PS | Presostato |
| PI | Indicador de presion |

**Analisis:**
- DPS (Differential Pressure Switch) es una combinacion de "D" (diferencial) + "PS" (presostato)
- La codificacion es logica pero no esta formalmente definida
- Alternativa seria usar "DPSH" (Differential Pressure Switch High)

**Impacto:**
- Inconsistencia con estandar de codificacion del proyecto
- Menor - el TAG es autoexplicativo

**Accion Requerida:**
- Agregar tipo "DPS" a la Tabla 3-3 del estandar de codificacion, o
- Renombrar a "DPSH-09-001" segun convencion ISA

---

## 5. Tabla de Cruce: P&ID vs Instrument List

### 5.1 Instrumentos del P&ID

La siguiente tabla verifica que cada instrumento listado en el P&ID aparezca en el Instrument List:

| # | TAG P&ID | Ubicacion P&ID | En Instrument List | Estado |
|---|----------|----------------|-------------------|--------|
| 1 | PIT-09-001 | Alimentacion RO | SI (linea 5) | OK |
| 2 | PIT-09-002 | Descarga bomba HP | SI (linea 6) | OK |
| 3 | PIT-09-003 | Entrada 1ra etapa | SI (linea 8) | OK |
| 4 | PIT-09-004 | Salida 1ra etapa | SI (linea 10) | OK |
| 5 | PIT-09-005 | Entrada 2da etapa | SI (linea 15) | OK |
| 6 | PIT-09-006 | Salida 2da etapa | SI (linea 16) | OK |
| 7 | PIT-09-007 | Brine 2da etapa | SI (linea 14) | OK |
| 8 | PIT-09-008 | Permeado | SI (linea 22) | OK |
| 9 | PIT-09-009 | Rechazo final | SI (linea 9) | OK |
| 10 | PI-09-001 | Feed turbocharger | SI (linea 7) | OK |
| 11 | PI-09-003 | Descarga bomba CIP | SI (linea 25) | OK |
| 12 | PI-09-004 | Filtro CIP entrada | SI (linea 26) | OK |
| 13 | PI-09-005 | Filtro CIP salida | SI (linea 27) | OK |
| 14 | PI-09-006 | Dosificacion antiincrustante | SI (linea 32) | OK |
| 15 | FIT-09-001 | Alimentacion RO | SI (linea 4) | **DUPLICADO** |
| 16 | FIT-09-003 | Permeado 1ra etapa | SI (linea 11) | OK |
| 17 | FIT-09-004 | Permeado 2da etapa | SI (linea 21) | OK |
| 18 | FIT-09-005 | CIP | SI (linea 29) | OK |
| 19 | AIT-09-001 (ORP) | Alimentacion | SI como ORPIT-09-001 (linea 2) | OK (nomenclatura) |
| 20 | CIT-09-001 | Alimentacion | SI (linea 3) | OK |
| 21 | AIT-09-002 (Cond.) | Permeado 1ra | SI como CIT-09-002 (linea 12) | OK (nomenclatura) |
| 22 | AIT-09-003 (Cond.) | Permeado 2da | SI como CIT-09-003 (linea 18) | OK (nomenclatura) |
| 23 | AIT-09-005 (Cond.) | Permeado final | SI como CIT-09-005 (linea 20) | OK (nomenclatura) |
| 24 | PHIT-09-001 | CIP | SI (linea 28) | OK |
| 25 | TE-09-001 | RO Train | SI como TE-09-001 (HP Pump) | OK |
| 26 | TE-09-002 | CIP Tank | SI como TE-09-002 (CIP Pump) | OK |
| 27 | TIT-09-001 | CIP Tank | SI (linea 23) | OK |
| 28 | TIT-09-002 | CIP Tank | **NO** | **REVISAR** |
| 29 | LI-09-001 | CIP Tank | SI como LIT-09-001 (linea 24) | OK (nomenclatura) |
| 30 | LI-09-002 | Antiscalant Tank | **NO** (solo LS) | **REVISAR** |
| 31 | LS-09-001 | Antiscalant Tank High | SI (linea 30) | OK |
| 32 | LS-09-002 | Antiscalant Tank Low | SI (linea 31) | OK |
| 33 | DPS-09-001 | Cartridge Filter | SI (linea 1) | OK |
| 34 | PI-09-002 | Train Reject | SI (linea 19) | OK |
| 35 | CIT-09-004 | Stage 1 Reject | SI (linea 17) | OK |
| 36 | FIT-09-001 (dup) | 2nd Stage Permeate | SI (linea 13) | **DUPLICADO** |

### 5.2 Resumen Cruce P&ID

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| OK | 31 | 86% |
| DUPLICADO | 2 | 6% |
| REVISAR | 2 | 6% |
| FALTANTE | 1 | 3% |

---

## 6. Tabla de Cruce: IO List vs Instrument List

### 6.1 Transmisores con Senal AI

| # | TAG IO List | Descripcion | En Instrument List | Estado |
|---|-------------|-------------|--------------------|--------|
| 1 | ORPIT09-001 | ORP Analyzer | SI | OK |
| 2 | CIT09-001 | Conductivity Feed | SI | OK |
| 3 | FIT09-001 | Flow Feed | SI | OK |
| 4 | PIT09-001 | Pressure HP Inlet | SI | OK |
| 5 | PIT09-002 | Pressure HP Discharge | SI | OK |
| 6 | PIT09-007 | Pressure Turbo Inlet | SI | OK |
| 7 | PIT09-003 | Pressure 1st Stage Inlet | SI | OK |
| 8 | PIT09-004 | Pressure 1st Stage Outlet | SI | OK |
| 9 | **CIT09-006** | Conductivity Interstage | **NO** | **FALTANTE** |
| 10 | PIT09-009 | Pressure Permeate | SI | OK |
| 11 | FIT09-003 | Flow 1st Permeate | SI | OK |
| 12 | CIT09-002 | Conductivity 1st Permeate | SI | OK |
| 13 | **FIT09-002** | Flow 2nd Permeate | Como FIT-09-001 (dup) | **DISCREPANCIA** |
| 14 | CIT09-003 | Conductivity 2nd Permeate | SI | OK |
| 15 | PIT09-006 | Pressure 2nd Stage | SI | OK |
| 16 | CIT09-005 | Conductivity Reject | SI | OK |
| 17 | PIT09-008 | Pressure Reject | SI | OK |
| 18 | FIT09-004 | Flow Reject | SI | OK |
| 19 | **LIT09-002** | Level CIP Tank | Como LIT-09-001 | **DISCREPANCIA** |
| 20 | PHIT09-001 | pH CIP | SI | OK |
| 21 | FIT09-005 | Flow CIP | SI | OK |

### 6.2 Switches con Senal DI

| # | TAG IO List | Descripcion | En Instrument List | Estado |
|---|-------------|-------------|--------------------|--------|
| 1 | DPS09-001 | Differential Pressure High | SI | OK |
| 2 | TE09-001 | HP Pump Temp Switch | SI | OK |
| 3 | TE09-002 | CIP Pump Temp Switch | SI | OK |
| 4 | LS09-001 | Antiscalant Level High | SI | OK |
| 5 | LS09-002 | Antiscalant Level Low | SI | OK |

### 6.3 Resumen Cruce IO List

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| OK | 22 | 85% |
| FALTANTE | 1 | 4% |
| DISCREPANCIA | 3 | 12% |

---

## 7. Verificacion Estandar de Codificacion ADASA

### 7.1 Formato de TAGs

Segun P00-IT-00-000-101 Seccion 3.3, el formato es:

**[TIPO]-[AREA]-[CORRELATIVO]**

| Campo | Descripcion | Valor P22 |
|-------|-------------|-----------|
| TIPO | Codigo instrumento Tabla 3-3 | PIT, FIT, CIT, etc. |
| AREA | Area proyecto Tabla 2-3 | 09 (Osmosis Inversa 2da Etapa) |
| CORRELATIVO | Numero secuencial 3 digitos | 001, 002, etc. |

### 7.2 Verificacion de Tipos

| TAG IL | Tipo | En Tabla 3-3 | Cumple |
|--------|------|--------------|--------|
| DPS-09-001 | DPS | **NO** | **NO** |
| ORPIT-09-001 | ORPIT | SI | OK |
| CIT-09-001 to 006 | CIT | SI | OK |
| FIT-09-001 to 005 | FIT | SI | OK |
| PIT-09-001 to 009 | PIT | SI | OK |
| PI-09-001 to 006 | PI | SI | OK |
| LIT-09-001 | LIT | SI | OK |
| LS-09-001/002 | LS | SI | OK |
| TIT-09-001 | TIT | SI | OK |
| PHIT-09-001 | PHIT | SI | OK |

### 7.3 Verificacion de Area

Todos los instrumentos usan Area **09** (Osmosis Inversa Segunda Etapa/Segundo Paso) - **CORRECTO**

### 7.4 Verificacion de Correlativos

| Tipo | Correlativos Usados | Secuencia | Estado |
|------|---------------------|-----------|--------|
| DPS | 001 | Unico | OK |
| ORPIT | 001 | Unico | OK |
| CIT | 001-006 | Secuencial | OK |
| FIT | 001-005 | **001 DUPLICADO** | **ERROR** |
| PIT | 001-009 | Secuencial | OK |
| PI | 001-006 | Secuencial | OK |
| LIT | 001 | Unico | OK |
| LS | 001-002 | Secuencial | OK |
| TIT | 001 | Unico | OK |
| PHIT | 001 | Unico | OK |

---

## 8. Acciones Requeridas BW Water

| # | Accion | OBS Ref | Prioridad | Impacto |
|---|--------|---------|-----------|---------|
| 1 | **CRITICO:** Eliminar duplicidad FIT-09-001. El transmisor de 2nd Stage Permeate (linea 13) debe renombrarse a FIT-09-002 | OBS-IL-01 | **URGENTE** | PLC |
| 2 | Agregar CIT-09-006 (Interstage Turbocharger Inlet Conductivity) al Instrument List | OBS-IL-02 | Alta | Completitud |
| 3 | Unificar TAG del transmisor de nivel CIP Tank: decidir entre LIT-09-001 (IL) o LIT-09-002 (IO) | OBS-IL-03 | Alta | Consistencia |
| 4 | Agregar al IO List las senales AI para: PIT-09-005, CIT-09-004, TIT-09-001 | OBS-IL-04 | Alta | PLC |
| 5 | Documentar equivalencia de nomenclaturas P&ID vs IL (AIT vs ORPIT/CIT) | OBS-IL-05 | Media | Documentacion |
| 6 | Agregar tipo DPS a estandar de codificacion o usar DPSH-09-001 | OBS-IL-06 | Baja | Estandar |

---

## 9. Matriz de Impacto por Observacion

| OBS | Documento Afectado | Ingenieria | Construccion | Puesta en Marcha |
|-----|-------------------|------------|--------------|------------------|
| OBS-IL-01 | IL, IO List, P&ID | ALTO | MEDIO | **CRITICO** |
| OBS-IL-02 | IL | MEDIO | MEDIO | MEDIO |
| OBS-IL-03 | IL, IO List | MEDIO | MEDIO | ALTO |
| OBS-IL-04 | IO List | ALTO | MEDIO | **ALTO** |
| OBS-IL-05 | P&ID | BAJO | BAJO | BAJO |
| OBS-IL-06 | Estandar | BAJO | BAJO | BAJO |

---

## 10. Veredicto Final

### 10.1 Criterios de Evaluacion

| Criterio | Resultado |
|----------|-----------|
| TAGs unicos | **NO CUMPLE** (FIT-09-001 duplicado) |
| Consistencia IL vs IO List | **NO CUMPLE** (3 discrepancias) |
| Consistencia IL vs P&ID | CUMPLE PARCIAL (nomenclatura diferente pero aceptable) |
| Codificacion ADASA | CUMPLE PARCIAL (DPS no definido) |

### 10.2 Veredicto

| Campo | Valor |
|-------|-------|
| **VEREDICTO INSTRUMENT LIST** | **3 - TO BE REVISED** |

**Justificacion:**

El Instrument List P22-LI-09-008-003 Rev.A presenta un error **CRITICO** de duplicidad en el TAG FIT-09-001 que impide su aprobacion. Este error tendria consecuencias graves en la programacion del PLC y puesta en marcha del sistema.

Adicionalmente, se identificaron 4 discrepancias **MAYORES** entre el Instrument List y el IO List que deben corregirse para garantizar la consistencia de la documentacion de ingenieria.

Se requiere revision del documento antes de aprobacion.

---

## 11. Anexo: Extracto Instrument List

### Instrumentos con Senal 4-20mA (AI)

| # | TAG | Descripcion | Rango | Modelo |
|---|-----|-------------|-------|--------|
| 1 | DPS-09-001 | Cartridge Filter DP Switch | 0-2 bar | Ashcroft 1132 |
| 2 | ORPIT-09-001 | ORP Analyzer | -1500 to 1500 mV | Rosemount 396P/1056 |
| 3 | CIT-09-001 | Conductivity Feed | 0-2000 uS/cm | Rosemount 400/1056 |
| 4 | **FIT-09-001** | Flow Feed | 0-100 m3/h, DN100 | Rosemount 8750W |
| 5 | PIT-09-001 | Pressure HP Inlet | 0-6 bar | Foxboro IGP05S |
| 6 | PIT-09-002 | Pressure HP Discharge | 0-100 bar | Foxboro IGP05S |
| 7 | PIT-09-003 | Pressure 1st Stage | 0-150 bar | Foxboro IGP05S |
| 8 | PIT-09-009 | Pressure Permeate | 0-2 bar | Foxboro IGP05S |
| 9 | PIT-09-004 | Pressure 1st Reject | 0-150 bar | Foxboro IGP05S |
| 10 | FIT-09-003 | Flow 1st Permeate | 0-40 m3/h, DN80 | Rosemount 8750W |
| 11 | CIT-09-002 | Conductivity 1st Permeate | 0-200 uS/cm | Rosemount 400/1056 |
| 12 | **FIT-09-001** | Flow 2nd Permeate | 0-18 m3/h, DN50 | Rosemount 8750W |
| 13 | PIT-09-007 | Pressure Turbo Interstage | 0-100 bar | Foxboro IGP05S |
| 14 | PIT-09-005 | Pressure 2nd Stage Feed | 0-150 bar | Foxboro IGP05S |
| 15 | PIT-09-006 | Pressure 2nd Stage Reject | 0-150 bar | Foxboro IGP05S |
| 16 | CIT-09-004 | Conductivity 1st Reject | 0-20 mS/cm | Rosemount 400/1056 |
| 17 | CIT-09-003 | Conductivity 2nd Permeate | 0-200 uS/cm | Rosemount 400/1056 |
| 18 | CIT-09-005 | Conductivity Train Reject | 0-20 mS/cm | Rosemount 400/1056 |
| 19 | FIT-09-004 | Flow Reject | 0-60 m3/h, DN65 | Rosemount 8750W |
| 20 | PIT-09-008 | Pressure Reject | 0-2 bar | Foxboro IGP05S |
| 21 | TIT-09-001 | Temperature CIP Tank | 0-100 C | Rosemount 214C/644 |
| 22 | LIT-09-001 | Level CIP Tank | 0-10 m | Vega VEGABAR 82 |
| 23 | PHIT-09-001 | pH CIP | 0-14 pH | Rosemount 396P/1056 |
| 24 | FIT-09-005 | Flow CIP | 0-100 m3/h, DN100 | Rosemount 8750W |

**Nota:** TAG FIT-09-001 aparece en filas 4 y 12 (DUPLICADO en rojo).

---

## 12. Documentos de Referencia

| Documento | Codigo | Ubicacion |
|-----------|--------|-----------|
| Instrument List | P22-LI-09-008-003-A | ENTREGAS_BWWATER/ENTREGA 8/md/ |
| IO List | P22-LI-09-008-001-A | ENTREGAS_BWWATER/ENTREGA 8/md/ |
| P&ID | P22-DWG-09-009-002-A | ENTREGAS_BWWATER/ENTREGA 3/md/ |
| Codificacion General | P00-IT-00-000-101 | BASES TECNICAS/md/ |
| Revision Entrega 8 | 25007-0008 | REVISIONES/SUBMITTALS/ |

---

*Fin del documento*
*Revision Tecnica Cruzada preparada: 27-Ene-2026*
*Revisor: ADASA*
