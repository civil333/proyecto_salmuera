# Revision Tecnica - Entrega 10 BW Water

**Submittal:** 25007-0010
**Fecha Emision:** 30-Ene-2026
**Fecha Revision:** 02-Feb-2026
**Revisor:** ADASA
**Version:** 2.0 (Revision rigurosa con cruce vs ET, Oferta Tecnica y revisiones previas)

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0010 |
| Fecha Emision | 30-Ene-2026 |
| Documentos | 2 |
| Tipos | LI (Lista), ET (Datasheet) |
| Submittal For | FA (For Approval) |
| Nota | Utility Consumption List (nuevo) + Antiscalant Dosing Tank DS Rev B |

---

## 2. Documentos Recibidos

| # | Codigo | Titulo | Rev | Paginas | Tipo |
|---|--------|--------|-----|---------|------|
| 1 | P22-LI-09-009-001 | Utility Consumption List | A | 2 | Lista |
| 2 | P22-ET-09-009-010 | Datasheet of Antiscalant Dosing Tank | B | 3 | Datasheet |

---

## 3. Revision Documento 1: Utility Consumption List (P22-LI-09-009-001-A)

### 3.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-009-001-A |
| Titulo | Utility Consumption List |
| Fecha | 21-Ene-2026 |
| Preparado | KOB / DCS |
| Revisado | GO |
| Aprobado | LPL |
| Revision | A (Primera emision) |

### 3.2 Contenido del Documento

El Utility Consumption List presenta el consumo de electricidad y agua del modulo RO:

**Equipos Incluidos:**
1. RO HP Feed Pump (93 kW)
2. Antiscalant Dosing Pump A/B (0.024 kW)
3. CIP Pump (11 kW)
4. CIP Tank Heater (20 kW)
5. PLC and Control System (2 kW)
6. Lighting Indoor/Outdoor (0.32 kW total)
7. Air Conditioning (2.64 kW)
8. Motorized Valves (13 x 0.12 kW)

### 3.3 Detalle de Consumo Electrico

| Item | Equipo | Alimentacion | Motor [kW] | Carga Op. [kW] | Hrs/dia | Consumo [kWh/dia] |
|------|--------|--------------|------------|----------------|---------|-------------------|
| 1 | RO HP Feed Pump | 380V/3PH/50Hz | 93 | 78.5 | 24 | 1,884.0 |
| 2 | Antiscalant Dosing Pump | 220V/1PH/50Hz | 0.024 | 0.02 | 24 | 0.5 |
| 3 | CIP Pump | 380V/3PH/50Hz | 11 | 10.00 | 0.04 | 0.44 |
| 4 | CIP Tank Heater | 380V/3PH/50Hz | 20 | 17.00 | 0.07 | 1.16 |
| 5 | PLC and Control System | **220V/1PH/60Hz** | 2 | 2.00 | 24 | 48.0 |
| 6 | Lighting (Indoor) | - | 0.16 | 0.16 | 24 | 3.8 |
| 7 | Lighting (Outdoor) | - | 0.16 | 0.16 | 24 | 3.8 |
| 8 | Air Conditioning | - | 2.64 | 2.64 | 24 | 63.4 |
| 9 | Motorized Valves | - | 0.12 | 0.12 | 0.11 | 0.2 |

### 3.4 Resumen de Consumos

| Parametro | Valor | Unidad |
|-----------|-------|--------|
| Consumo Diario Estimado | 2,005 | kWh |
| Produccion de Agua | 21 | m3/h |
| **SEC (Specific Energy Consumption)** | **3.98** | **kWh/m3** |
| Consumo Agua Cruda | 1,176 | m3/dia |

---

### 3.5 VERIFICACION RIGUROSA VS ESPECIFICACION TECNICA (ET P22-ET-09-000-001-0)

#### 3.5.1 Requisito CRITICO: Frecuencia Electrica (ET Seccion 5.4.7)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4.7 - Voltajes y frecuencia que considerar |
| **Lineas ET** | 1305-1308 |
| **Caracter** | **OBLIGATORIO - NO NEGOCIABLE** |

**Texto exacto ET:**
> "Para todos los equipos electricos se debe considerar una alimentacion electrica de operacion en 380 VAC/220 VAC, 50 Hz. **No se aceptaran equipos principales que operen en otros voltajes y frecuencias.**"

**Evaluacion:**

| Equipo | Utility List | Requisito ET | Cumple |
|--------|--------------|--------------|--------|
| HP Pump | 380V/3PH/50Hz | 380V/50Hz | **SI** |
| CIP Pump | 380V/3PH/50Hz | 380V/50Hz | **SI** |
| CIP Heater | 380V/3PH/50Hz | 380V/50Hz | **SI** |
| Dosing Pump | 220V/1PH/50Hz | 220V/50Hz | **SI** |
| **PLC** | **220V/1PH/60Hz** | **220V/50Hz** | **NO** |

**OBSERVACION CRITICA OBS-01:** El PLC esta especificado a **60 Hz**. La ET Seccion 5.4.7 establece explicitamente que "No se aceptaran equipos principales que operen en otros voltajes y frecuencias". El sistema electrico chileno opera a 50 Hz. **Este es un incumplimiento directo del requisito ET.**

**Nota:** Si el PLC tiene fuente de poder con rango de frecuencia 50-60 Hz, debe documentarse explicitamente.

#### 3.5.2 Requisito CRITICO: Sistema A/C (ET Seccion 5.1.11)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.1.11 - Servicios Auxiliares |
| **Lineas ET** | 747-759 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Lineas 747-750):**
> "El proveedor debera considerar la cantidad y necesidad de unidades de aire acondicionado para trabajo 24 horas por dia los siete dias de la semana en **cantidad n+1**, para que la temperatura se mantenga por debajo de los 25°C al interior del contenedor."

**Texto exacto ET (Lineas 757-759):**
> "Durante la ingenieria de detalles se debera entregar una **memoria de calculo termica** para determinar la cantidad del sistema de aire acondicionado, en base a la informacion de la carga termica de los equipos a instalar en ella y las condiciones ambientales especificadas por ADASA."

**Condiciones de sitio (ET Lineas 752-756):**
- Temperatura maxima: 28°C
- Temperatura minima: 8°C
- Humedad relativa promedio: 48%
- Presion atmosferica: 93.3 kPa

**Evaluacion:**

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| Cantidad A/C | **n+1 (minimo 2)** | 1 unidad | **NO** |
| Operacion | 24/7 | 24 hrs | SI |
| Temperatura interior | < 25°C | No demostrado | **PENDIENTE** |
| Memoria calculo termica | **Obligatoria** | No incluida | **NO** |

**OBSERVACION CRITICA OBS-02:** La Utility List especifica **solo 1 unidad A/C** (2.64 kW). La ET requiere configuracion **n+1**, es decir, minimo 2 unidades. **Esta observacion fue levantada en Transmittal N2 (Entrega 5, 06-Ene-2026) y permanece SIN RESOLVER despues de 27 dias.**

**OBSERVACION CRITICA OBS-03:** No se incluye memoria de calculo termica requerida por ET 5.1.11. **Esta observacion fue levantada en Transmittal N2 (Entrega 5) y permanece SIN RESOLVER.**

#### 3.5.3 Verificacion SEC vs Garantia (ET Seccion 10.1.3)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 10.1.3 - Consumo Especifico de Energia Electrica |
| **Lineas ET** | 1928-1939 |
| **Caracter** | **GARANTIZADO CONTRACTUALMENTE** |

**Valores Maximos ET (Lineas 1935-1939):**

| TDS (mg/L) | SEC Maximo Requerido |
|------------|---------------------|
| 43,000 - 48,000 | < 4.8 kWh/m3 |
| 48,000 - 53,000 | < 5.0 kWh/m3 |

**Evaluacion:**

| Parametro | Garantia ET | Utility List | Cumple |
|-----------|-------------|--------------|--------|
| SEC @ 53,000 ppm | < 5.0 kWh/m3 | 3.98 kWh/m3 | **SI** |

**EVALUACION POSITIVA:** El SEC calculado (3.98 kWh/m3) cumple holgadamente la garantia ET (< 5.0 kWh/m3) y la garantia contractual de la Oferta (4.71 kWh/m3). Margen favorable de ~20%.

---

### 3.6 VERIFICACION RIGUROSA VS OFERTA TECNICA REV.1

#### 3.6.1 Potencia de Equipos Principales

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 4.1 - Mechanical Equipment List

| Equipo | Oferta Rev.1 | Utility List E10 | Load List E1 | Equipment List E8 | Datasheet E7 |
|--------|-------------|------------------|--------------|-------------------|--------------|
| **HP Pump** | **86 kW** | **93 kW** | 83 kW | 92 kW | 92 kW |
| **CIP Pump** | **15 kW** | **11 kW** | 9.3 kW | 11 kW | - |
| CIP Heater | 20 kW | 20 kW | 16 kW | 20 kW | 20 kW |
| A/C (total) | **5.28 kW (2x2.64)** | **2.64 kW (1x2.64)** | 1.86 kW | - | - |

**OBSERVACION MAYOR OBS-04:** Discrepancia en potencia HP Pump:
- Oferta Rev.1: **86 kW**
- Utility List: **93 kW** (+7 kW, +8%)
- Load List E1: 83 kW
- Equipment List/Datasheet: 92 kW

Existen **4 valores diferentes** en la documentacion del proyecto. Se requiere unificacion urgente.

**OBSERVACION MAYOR OBS-05:** Discrepancia en potencia CIP Pump:
- Oferta Rev.1: **15 kW**
- Utility List: **11 kW** (-4 kW, -27%)

La diferencia de 4 kW (27%) es significativa y debe clarificarse.

#### 3.6.2 Sistema A/C - Compromiso de Oferta

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 4 - Scope of Supply (Linea 549-551)

**Texto exacto Oferta Rev.1:**
> "1 Lot HVAC for the container (a separate price will be provided in Commercial proposal). **2 A/C (1W + 1S) are provided inside container.**"

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 17 - Power & Load Consumption List

| Item | Descripcion | Oferta Rev.1 |
|------|-------------|--------------|
| A/C Unit | Configuracion | 1 + 1 (1 duty + 1 standby) |
| A/C Unit | Potencia por unidad | 2.64 kW |
| A/C Unit | Potencia total conectada | **5.28 kW** |

**Evaluacion:**

| Compromiso Oferta | Valor Comprometido | Utility List E10 | Cumple |
|-------------------|-------------------|------------------|--------|
| Cantidad A/C | **2 unidades (1W+1S)** | 1 unidad | **NO** |
| Potencia total A/C | 5.28 kW | 2.64 kW | **NO** |

**OBSERVACION CRITICA OBS-06:** La Oferta Tecnica Rev.1 comprometio explicitamente **2 unidades A/C en configuracion 1W+1S**. La Utility List muestra solo 1 unidad. Esto representa:
1. **Incumplimiento de la ET** (requisito n+1)
2. **Incumplimiento de la Oferta Tecnica** (compromiso contractual)

#### 3.6.3 SEC Garantizado

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 19 - Guaranteed SEC Value

| Parametro | Valor Oferta Rev.1 |
|-----------|-------------------|
| SEC Garantizado | **4.71 kWh/m3 +/- 5%** |
| TDS de referencia | 53,000 ppm |
| Frecuencia CIP base | 60 dias |

**Evaluacion:**

| Parametro | Garantia Oferta | Utility List | Margen | Cumple |
|-----------|-----------------|--------------|--------|--------|
| SEC | 4.71 +/- 5% (4.47-4.95) | 3.98 kWh/m3 | -15% | **SI** |

**EVALUACION POSITIVA:** SEC cumple garantia con margen favorable del 15%.

#### 3.6.4 Material Estanque Antiincrustante

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 4.1 - Item 12

| Parametro | Oferta Rev.1 | Datasheet E10 |
|-----------|-------------|---------------|
| Material | **HDPE** | **LMDPE** |
| Capacidad | 65 gal (246 L) | 340 L (0.34 m3) |
| Fabricante | Norwesco or Equal | Promatics |

**Evaluacion:** El cambio de HDPE a LMDPE esta justificado por BW Water (limitaciones dimensionales). LMDPE mantiene compatibilidad quimica. La capacidad es mayor que la comprometida. **CAMBIO ACEPTADO.**

---

### 3.7 VERIFICACION VS REVISIONES CRUZADAS PREVIAS

#### 3.7.1 Observaciones Arrastradas desde Transmittal N2 (Entrega 5)

**Fuente:** REVISIONES/SUBMITTALS/25007-0005/2026-01-06_Revision-Tecnica-Entrega-5.md

| # | Observacion Original | Fecha | Estado en E10 |
|---|---------------------|-------|---------------|
| 1 | A/C: Calculo termico NO incluye todas las cargas (11-15 kW real vs 5.96 kW calculado) | 06-Ene-2026 | **SIN RESOLVER** |
| 2 | A/C: NO considera configuracion n+1 requerida | 06-Ene-2026 | **SIN RESOLVER** |
| 3 | A/C: NO indica marca/modelo del equipo propuesto | 06-Ene-2026 | **SIN RESOLVER** |

**Tiempo transcurrido sin resolucion:** 27 dias

#### 3.7.2 Discrepancias con Otras Listas

**Fuente:** REVISIONES/SUBMITTALS/25007-VALVELIST/2026-01-28_Revision-Tecnica-Cruzada-ValveList-EquipmentList.md

| Parametro | P&ID E3 | Equipment List E8 | Utility List E10 |
|-----------|---------|-------------------|------------------|
| Capacidad bomba dosificadora | 1 LPH | 2.3 LPH | - |

**OBSERVACION MENOR OBS-07:** Discrepancia de capacidad de bomba dosificadora (1 vs 2.3 LPH) identificada en revision cruzada Valve List. No resuelta en E10.

---

### 3.8 Resumen de Observaciones Documento 1

| # | Observacion | Severidad | Referencia | Arrastrada |
|---|-------------|-----------|------------|------------|
| **OBS-01** | **PLC especificado a 60Hz. ET 5.4.7 requiere 50Hz y establece "No se aceptaran equipos que operen en otras frecuencias"** | **CRITICA** | ET 5.4.7 L1305-1308 | Nueva |
| **OBS-02** | **Solo 1 unidad A/C. ET 5.1.11 requiere n+1 (minimo 2). Oferta Rev.1 comprometio 2 unidades (1W+1S)** | **CRITICA** | ET 5.1.11, Oferta Sec 4 | TM N2 (27 dias) |
| **OBS-03** | **Falta memoria de calculo termica del A/C requerida por ET 5.1.11** | **CRITICA** | ET 5.1.11 L757-759 | TM N2 (27 dias) |
| **OBS-04** | Discrepancia HP Pump: 93 kW (Utility) vs 86 kW (Oferta) vs 92 kW (Equipment List) vs 83 kW (Load List). 4 valores diferentes. | **MAYOR** | Multiple | Nueva |
| **OBS-05** | Discrepancia CIP Pump: 11 kW (Utility) vs 15 kW (Oferta). Diferencia de 27%. | **MAYOR** | Oferta Rev.1 Sec 4.1 | Nueva |

### 3.9 Veredicto Documento 1

| Aspecto | Veredicto |
|---------|-----------|
| Cumplimiento ET | **NO CUMPLE** (OBS-01, OBS-02, OBS-03) |
| Cumplimiento Oferta | **NO CUMPLE** (OBS-02, OBS-04, OBS-05) |
| Tecnico | **3 - To be revised** |
| **VEREDICTO FINAL** | **3 - TO BE REVISED** |

**Justificacion:** El documento presenta **3 incumplimientos criticos**:
1. PLC a 60Hz viola requisito explicito ET 5.4.7
2. A/C sin configuracion n+1 viola ET 5.1.11 y compromiso de Oferta Rev.1
3. Falta memoria de calculo termica requerida por ET 5.1.11

Adicionalmente, hay discrepancias mayores en potencias de equipos (HP Pump, CIP Pump) que afectan la confiabilidad de los datos.

---

## 4. Revision Documento 2: Datasheet of Antiscalant Dosing Tank (P22-ET-09-009-010-B)

### 4.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-009-010-B |
| Titulo | Datasheet of Antiscalant Dosing Tank |
| Fecha | 20-Ene-2026 |
| Preparado | KOB / DCS |
| Revisado | GO |
| Aprobado | LPL |
| Revision | B |
| TAG | TK-09-002 |
| Fabricante | Promatics |
| Modelo | PLC330 |

### 4.2 Historial de Revisiones

| Rev | Fecha | Cambio |
|-----|-------|--------|
| A | 28-Nov-2025 | Emision inicial (Entrega 2) |
| B | 20-Jan-2026 | Cambio material HDPE a LMDPE |

### 4.3 Especificaciones Principales

#### 4.3.1 Informacion General

| Parametro | Valor |
|-----------|-------|
| Component Name | Antiscalant Dosing Tank |
| TAG | TK-09-002 |
| Type | PE Tank, Open Top, Flat Bottom |
| P&ID Reference | P22-DWG-09-009-02-P11 |
| Quantity Duty | 1 |
| Quantity Standby | 0 |
| Operating Hours | 24 hrs/day |
| Location | Outdoor, Ground Level |

#### 4.3.2 Especificaciones del Estanque

| Parametro | Valor | Unidad |
|-----------|-------|--------|
| Total Capacity | 0.34 | m3 |
| Effective Capacity | 0.27 | m3 |
| Dimensions | 630 mm (D) x 1090 mm (H) | - |
| Effective Height | 1030 mm | - |
| Rim Height | 1085 mm | - |

#### 4.3.3 Condiciones de Diseno

| Parametro | Valor |
|-----------|-------|
| Design Code | ASTM D1998 Standard |
| Seismic Zone Factor | 3 |
| Operating Temperature | Ambient |
| Operating Pressure | Atmospheric, Full Liquid |
| Design Temperature | 55 C |
| Design Pressure | Full Liquid |

#### 4.3.4 Materiales de Construccion

| Componente | Material |
|------------|----------|
| **Tank** | **Linear Polyethylene Medium Density (LMDPE)** |
| Lining | N/A |
| Gaskets | 3-mm thick EPDM |
| Bolt and Nuts | SS304 |
| Flange Rating | Universal Flange |

#### 4.3.5 Especificaciones del Fluido

| Parametro | Valor |
|-----------|-------|
| Fluid | Antiscalant |
| Specific Gravity | 1.03 |
| Temperature | 19 - 24 C |
| pH | > 10 |
| Corrosive | Yes |
| Chemical Reagents | Yes |

#### 4.3.6 Boquillas (Nozzles)

| Nozzle | Function | Size | Location | Elevation |
|--------|----------|------|----------|-----------|
| N01 | Inlet | DN25 | top | - |
| N41 | Spare | DN25 | top | - |
| N75 | Vent | DN25 | top | - |
| N80 | Overflow | DN50 | side | 1030 mm |
| N85 | Outlet | DN15 | side | 150 mm |
| N81 | Drain | DN25 | side | 150 mm |
| N90 | Level Gauge | DN25 | side | 1030 mm |
| N91 | Level Gauge | DN25 | side | 150 mm |

### 4.4 Respuesta a Comentarios ADASA (Consolidated Comment Sheet)

| # | Comentario ADASA | Respuesta BW Water |
|---|------------------|-------------------|
| 1 | Change ITEM to ET | BW has revised accordingly |
| 2 | Material tank | Material changed from HDPE to LMDPE due to dimensional limitations. The smallest available HDPE tank is 1.1 m3 with diameter ~1.2 m. LMDPE tank provides more suitable size while meeting capacity requirements. |

---

### 4.5 VERIFICACION RIGUROSA VS ET

#### 4.5.1 Material del Estanque

| Campo | Valor |
|-------|-------|
| **Seccion ET aplicable** | N/A |
| **Requisito especifico** | NO ESPECIFICADO |

**Evaluacion:** La ET P22-ET-09-000-001-0 **no especifica** el material requerido para el estanque de dosificacion de antiincrustante. Los materiales mencionados en la ET para otros componentes son PRFV, PVC, y PP. El cambio de HDPE a LMDPE es **aceptable** dado que:
- Ambos son polietileno con resistencia quimica similar
- LMDPE es compatible con antiincrustantes (pH > 10)
- El cambio esta justificado por limitaciones dimensionales

---

### 4.6 VERIFICACION RIGUROSA VS OFERTA TECNICA REV.1

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 4.1 - Item 12

| Parametro | Oferta Rev.1 | Datasheet E10 | Cumple |
|-----------|-------------|---------------|--------|
| Material | HDPE | LMDPE | **CAMBIO JUSTIFICADO** |
| Capacidad | 65 gal (246 L) | 340 L (0.34 m3) | **SI** (mayor) |
| Fabricante | Norwesco or Equal | Promatics | SI (equivalente) |

**Evaluacion del Cambio de Material:**

El cambio de HDPE a LMDPE esta justificado por:
- Limitaciones dimensionales del HDPE para capacidades pequenas
- LMDPE mantiene compatibilidad quimica con antiscalante
- Ambos materiales son polietileno con resistencia quimica similar
- La capacidad entregada (340 L) es **mayor** que la comprometida (246 L)

**CAMBIO ACEPTADO** - No genera desviacion tecnica negativa.

---

### 4.7 Verificacion vs P&ID (P22-DWG-09-009-002-A)

| Parametro | Datasheet Rev B | P&ID E3 | Equipment List E8 | Consistencia |
|-----------|-----------------|---------|-------------------|--------------|
| TAG | TK-09-002 | TK-09-002 | TK-09-002 | **SI** |
| Capacidad | 0.34 m3 total | 0.25 m3 | 0.27 m3 | **NOTA** |
| Material | LMDPE | HDPE | LMDPE | P&ID desactualizado |

**OBSERVACION MENOR OBS-08:** Capacidad en P&ID (0.25 m3) difiere de Datasheet (0.34 m3 total / 0.27 m3 efectivo). Diferencia menor y favorable. Actualizar P&ID en proxima revision.

### 4.8 Verificacion vs Instrument List (P22-LI-09-008-003-A)

| Instrumento | TAG | Descripcion | Ubicacion | Consistente |
|-------------|-----|-------------|-----------|-------------|
| Level Switch High | LS-09-001 | Antiscalant Dosing Tank Level Switch High | Tank Side | **SI** |
| Level Switch Low | LS-09-002 | Antiscalant Dosing Tank Level Switch Low | Tank Side | **SI** |

**Evaluacion:** La instrumentacion del tanque (LS-09-001 y LS-09-002) esta correctamente definida y es consistente con las boquillas N90/N91.

### 4.9 Resumen de Observaciones Documento 2

| # | Observacion | Severidad | Referencia |
|---|-------------|-----------|------------|
| **OBS-08** | Capacidad P&ID (0.25 m3) vs Datasheet (0.34 m3). Actualizar P&ID. | Menor | P&ID E3 |

### 4.10 Veredicto Documento 2

| Aspecto | Veredicto |
|---------|-----------|
| Cumplimiento ET | **CUMPLE** (material no especificado en ET) |
| Cumplimiento Oferta | **CUMPLE** (cambio justificado, capacidad mayor) |
| Tecnico | **2 - Approved as noted** |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

**Justificacion:** El Datasheet Rev B responde adecuadamente a los comentarios ADASA. El cambio de material de HDPE a LMDPE esta justificado tecnica y documentalmente. El documento es consistente con Equipment List e Instrument List. Solo se requiere actualizacion menor de capacidad en P&ID.

---

## 5. Verificacion de Codificacion

| Documento | Codigo | Formato P22-TT-AA-DDD-NNN-R | Cumple |
|-----------|--------|-----------------------------|----- ---|
| Utility Consumption List | P22-LI-09-009-001-A | P22-LI-09-009-001-A | **SI** |
| Antiscalant Tank DS | P22-ET-09-009-010-B | P22-ET-09-009-010-B | **SI** |

**Todos los documentos cumplen** con el sistema de codificacion P00-IT-00-000-101.

---

## 6. Resumen Consolidado de Observaciones

### 6.1 Observaciones Criticas (Requieren correccion inmediata)

| # | Documento | Descripcion | Referencia | Estado |
|---|-----------|-------------|------------|--------|
| **OBS-01** | Utility List | **PLC a 60Hz viola ET 5.4.7** "No se aceptaran equipos que operen en otras frecuencias" | ET 5.4.7 L1305-1308 | **NUEVA** |
| **OBS-02** | Utility List | **A/C sin n+1** - Solo 1 unidad. ET requiere 2, Oferta comprometio 2 (1W+1S) | ET 5.1.11, Oferta Sec 4 | **ARRASTRADA 27 dias** |
| **OBS-03** | Utility List | **Falta memoria calculo termico A/C** requerida por ET 5.1.11 | ET 5.1.11 L757-759 | **ARRASTRADA 27 dias** |

### 6.2 Observaciones Mayores (Requieren clarificacion)

| # | Documento | Descripcion | Referencia | Estado |
|---|-----------|-------------|------------|--------|
| **OBS-04** | Utility List | **4 valores diferentes para HP Pump:** 93 kW (Utility) vs 86 kW (Oferta) vs 92 kW (Equipment List) vs 83 kW (Load List) | Multiple | **NUEVA** |
| **OBS-05** | Utility List | **CIP Pump 11 kW vs 15 kW (Oferta)** - Diferencia de 27% | Oferta Rev.1 Sec 4.1 | **NUEVA** |

### 6.3 Observaciones Menores (Actualizar documentacion)

| # | Documento | Descripcion | Referencia | Estado |
|---|-----------|-------------|------------|--------|
| **OBS-06** | Antiscalant DS | Cambio material HDPE a LMDPE | Oferta Rev.1 | **ACEPTADO** |
| **OBS-07** | Utility List | Discrepancia capacidad bomba dosificadora (1 vs 2.3 LPH) | Valve List Review | **PENDIENTE** |
| **OBS-08** | Antiscalant DS | Capacidad P&ID (0.25 m3) vs Datasheet (0.34 m3) | P&ID E3 | **PENDIENTE** |

---

## 7. Acciones Requeridas BW Water

### 7.1 Acciones Criticas (Plazo: Inmediato)

| # | Accion | Documento | Prioridad | Referencia |
|---|--------|-----------|-----------|------------|
| 1 | **Confirmar frecuencia PLC.** Si el equipo opera solo a 60Hz, reemplazar por equipo compatible 50Hz. Si es dual-frequency (50/60Hz), documentar explicitamente. | P22-LI-09-009-001-A | **CRITICA** | OBS-01, ET 5.4.7 |
| 2 | **Incluir 2da unidad A/C** segun ET 5.1.11 (n+1) y compromiso Oferta Rev.1. Actualizar Utility List y Load List. | P22-LI-09-009-001-A | **CRITICA** | OBS-02 |
| 3 | **Entregar memoria de calculo termica** del sistema A/C considerando TODAS las cargas termicas del container (HP Pump, CIP Pump, VFDs, PLC, iluminacion, calor solar, infiltracion). | Nuevo documento | **CRITICA** | OBS-03, ET 5.1.11 |

### 7.2 Acciones Mayores (Plazo: Proxima revision)

| # | Accion | Documento | Prioridad | Referencia |
|---|--------|-----------|-----------|------------|
| 4 | **Unificar potencia HP Pump** en todos los documentos. Confirmar valor correcto y actualizar Load List, Utility List, Equipment List. | Multiple | **ALTA** | OBS-04 |
| 5 | **Clarificar potencia CIP Pump** - 11 kW vs 15 kW. Actualizar si corresponde. | P22-LI-09-009-001-A | **ALTA** | OBS-05 |

### 7.3 Acciones Menores (Plazo: Proxima emision)

| # | Accion | Documento | Prioridad | Referencia |
|---|--------|-----------|-----------|------------|
| 6 | Actualizar capacidad Antiscalant Tank en P&ID (0.25 -> 0.34 m3) | P22-DWG-09-009-002 | Baja | OBS-08 |
| 7 | Clarificar capacidad bomba dosificadora (1 vs 2.3 LPH) | P&ID, Equipment List | Baja | OBS-07 |

---

## 8. Veredicto Final de la Entrega

### 8.1 Resumen por Documento

| # | Documento | Veredicto |
|---|-----------|-----------|
| 1 | P22-LI-09-009-001-A Utility Consumption List | **3 - To be revised** |
| 2 | P22-ET-09-009-010-B Antiscalant Dosing Tank DS | **2 - Approved as noted** |

### 8.2 Veredicto Consolidado

| Campo | Valor |
|-------|-------|
| **VEREDICTO ENTREGA 10** | **3 - TO BE REVISED** |
| Documentos Approved | 0 |
| Documentos Approved as Noted | 1 |
| Documentos To Be Revised | 1 |
| Documentos Rejected | 0 |

### 8.3 Justificacion del Veredicto

La Entrega 10 **requiere revision** debido a los siguientes incumplimientos criticos en el documento Utility Consumption List:

1. **Incumplimiento ET 5.4.7 (Frecuencia):** El PLC esta especificado a 60Hz. La ET establece explicitamente que "No se aceptaran equipos principales que operen en otros voltajes y frecuencias" (50Hz es mandatorio en Chile).

2. **Incumplimiento ET 5.1.11 (A/C n+1):** Solo 1 unidad A/C especificada. La ET requiere configuracion n+1 (minimo 2 unidades). Esta observacion fue levantada hace 27 dias (TM N2) y permanece sin resolver.

3. **Incumplimiento Oferta Tecnica Rev.1:** La Oferta comprometio explicitamente "2 A/C (1W + 1S)". La Utility List muestra solo 1 unidad.

4. **Falta documento requerido:** La ET 5.1.11 requiere "memoria de calculo termica" que no ha sido entregada.

El Datasheet del Antiscalant Dosing Tank (P22-ET-09-009-010-B) es aprobado con notas menores - el cambio de material HDPE a LMDPE esta justificado tecnicamente.

**Aspectos Positivos:**
- SEC 3.98 kWh/m3 cumple garantia (4.71 kWh/m3) con margen de 15%
- Datasheet Antiscalant Tank es consistente con Equipment List e Instrument List

---

## 9. Documentos de Referencia

| Documento | Ubicacion |
|-----------|-----------|
| ET Modulo | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md |
| Oferta Tecnica Rev.1 | OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md |
| P&ID | ENTREGAS_BWWATER/ENTREGA 3/md/P22-DWG-09-009-002-A_Piping and Instrumentation Diagram.md |
| Equipment List | ENTREGAS_BWWATER/ENTREGA 8/md/P22-LI-09-005-001-A Equipment List.md |
| Instrument List | ENTREGAS_BWWATER/ENTREGA 8/md/P22-LI-09-008-003_Instrument List_A.md |
| Load List | ENTREGAS_BWWATER/ENTREGA 1/md/P22-LI-09-007-001_A Electrical Load List.md |
| Revision Entrega 5 (A/C) | REVISIONES/SUBMITTALS/25007-0005/2026-01-06_Revision-Tecnica-Entrega-5.md |
| Revision Cruzada Valve List | REVISIONES/SUBMITTALS/25007-VALVELIST/2026-01-28_Revision-Tecnica-Cruzada-ValveList-EquipmentList.md |
| Revision Cruzada HP Pump | REVISIONES/SUBMITTALS/25007-HPPUMP/2026-01-27_Revision-Tecnica-Temperatura-Bombas.md |

---

*Fin del documento*
*Revision preparada: 02-Feb-2026*
*Version 2.0 - Revision rigurosa con cruce completo vs ET, Oferta Tecnica y revisiones previas*
