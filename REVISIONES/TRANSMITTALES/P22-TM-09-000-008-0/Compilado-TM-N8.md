---
codigo: P22-TM-09-000-008-0
tipo: Compilado Interno (NO ENVIAR)
fecha: 09-Mar-2026
revision: 0
entregas: E15 (25007-0015) + E16 (25007-0016)
documentos: 10 datasheets + IL Rev B + 1 faltante (P22-LI-09-008-013)
veredicto_global: 3 — TO BE REVISED
preparado_por: Luis Rivera
---

# COMPILADO INTERNO — TM N8 (E15 + E16)
## Análisis ADASA — 09-Mar-2026

> **DOCUMENTO INTERNO — NO ENVIAR A BW WATER**

---

## 1. CONTEXTO

BW Water emitió dos submittals el 09-Mar-2026 con respuesta requerida al 12-Mar-2026:
- **25007-0015 (E15):** 10 documentos (9 datasheets + 1 drawing). NOTA: el submittal form lista P22-LI-09-008-013 como ítem 10, pero este archivo NO fue recibido (solo 9 datasheets entregados físicamente + Power Works DWG).
- **25007-0016 (E16):** Instrument List Rev B (P22-LI-09-008-003 Rev B) — también presente físicamente en la carpeta de E15.

TM N8 cubre ambas entregas. IL Rev B revisada una sola vez.

---

## 2. INSTRUMENT LIST REV B — ANÁLISIS COMPARATIVO

### 2.1 Resumen de cambios Rev A → Rev B

| Campo | Rev A | Rev B |
|-------|-------|-------|
| Total ítems | 32 | 39 |
| Nuevos ítems | — | +7 |
| Referencias P&ID | Rev A | Rev B |
| Fecha | 15-Jan-2026 | 26-Feb-2026 |

### 2.2 Nuevos ítems en Rev B (positivos — cierran observaciones previas)

| TAG nuevo | Descripción | Criterio ET | Origen |
|-----------|-------------|-------------|--------|
| VT-09-001 | Vibration Tx — HP Pump (ifm VTV122, 4-20mA) | ET §5.5.6 | Cierra gap de Rev A |
| VT-09-002 | Vibration Tx — Feed Turbocharger (ifm VTV122, 4-20mA) | ET §5.5.6 | Cierra gap de Rev A |
| VT-09-003 | Vibration Tx — Interstage Turbocharger (ifm VTV122, 4-20mA) | ET §5.5.6 | Cierra gap de Rev A |
| TE-09-001 | RTD Bearing — HP Pump motor (Fedco PT100, 3-wire, DIN 44082) | ET §5.3 | Cierra gap de Rev A |
| TE-09-002 | RTD Winding — HP Pump motor (Fedco PT100, 3-wire, DIN 44082) | ET §5.3 | Cierra gap de Rev A |
| TE-09-003 | RTD Bearing — CIP Pump motor (Grundfos PT100, 3-wire, DIN 44082) | ET §5.3 | Cierra gap de Rev A |
| TE-09-004 | RTD Winding — CIP Pump motor (Grundfos PT100, 3-wire, DIN 44082) | ET §5.3 | Cierra gap de Rev A |

### 2.3 TAGs corregidos

| TAG Rev A | TAG Rev B | Cambio |
|-----------|-----------|--------|
| FIT-09-001 (duplicado para 2nd stage, DN50) | FIT-09-002 | Desduplicación de TAG — correcto |
| LIT-09-001 (CIP tank level) | LIT-09-002 | Renumeración para alineación con IO List |
| CIT-09-002 rango 0-200 uS/cm | CIT-09-002 rango 0-2000 uS/cm | Corrección de rango (permeado total, rango anterior insuficiente) |

### 2.4 ANOMALÍA CRÍTICA — CIT-09-005 Power Supply 120VAC

- **Ítem 25:** CIT-09-005 (RO Train Reject Conductivity Analyzer, Rosemount 228 + 1056)
- **Power Supply en IL Rev B:** 120VAC
- **Todos los demás transmisores:** 24VDC
- **ET §5.4.7:** Los equipos principales operan en 380VAC/220VAC, 50Hz. No se aceptan equipos en otros voltajes.
- **Conflicto:** 120VAC no es 380/220VAC (ET sistema de fuerza), ni 24VDC (sistema de instrumentación). ¿Error de tipeo o diseño real?
- **El Rosemount 1056 transmitter:** acepta 20-30VDC (low power) o también 85-265VAC. Si el 1056 se especificó para alimentación AC, requiere diseño de suministro de 120VAC no estándar.
- **Acción:** BW Water debe confirmar si es error tipográfico (se corrige a 24VDC) o si hay un razonamiento de diseño para 120VAC.

### 2.5 Verificación de cobertura ET §5.5

| Criterio ET | Requerimiento | IL Rev B | Estado |
|-------------|---------------|---------|--------|
| §5.5.1 Caudalímetros electromagnéticos | 5 puntos | FIT-09-001/002/003/004/005 (5 unidades) | ✅ CUMPLE |
| §5.5.2 Manómetros | 6 puntos | PI-09-001 a PI-09-006 (6 unidades) | ✅ CUMPLE |
| §5.5.3 Transmisores de presión | 9 puntos | PIT-09-001/002/003/004/005/006/007/008/009 | ✅ CUMPLE |
| §5.5.4 Sensor de nivel CIP (tipo Dpcell) | 1 transmisor continuo | LIT-09-002 (VEGABAR 82, gauge pressure type) | ✅ CUMPLE (pressure-based, acceptable) |
| §5.5.5 Conductímetros (5 puntos) | 5 puntos | CIT-09-001/002/003/004/005 | ✅ CUMPLE cobertura — ver OBS-10 para rangos lado salmuera |
| §5.5.6 Transmisores de vibración | HP Pump + Turbos (2 min.) | VT-09-001/002/003 (3 unidades) | ✅ CUMPLE cobertura — ver OBS-11 para umbrales de alarma |
| §5.3 Pt-100 motores devanados+rodamientos | Todos los motores | TE-09-001/002 (HP Pump, Fedco), TE-09-003/004 (CIP Pump, Grundfos) | ✅ CUMPLE |

### 2.6 IO List pendiente

- **IO List Rev A** (E8, TM N3): desactualizada — no refleja FIT-09-002 (nuevo), LIT-09-002 (renumerado), VT-09-001/002/003 (nuevos), TE-09-001/002/003/004 (nuevos)
- **IO List Rev B:** no recibida (pendiente desde TM N3, 45 días)
- La IL Rev B sin IO List correspondiente impide verificar asignación completa de canales PLC

---

## 3. ANÁLISIS DATASHEETS

### 3.1 P22-LI-09-008-005 — Conductivity Analyzer Rev A

**Make/Model:**
- CIT-09-001/002/003/004: Rosemount 400 (contacting) + Rosemount 1056 transmitter → 4-20mA HART ✓
- CIT-09-005: Rosemount 228 (toroidal, para fluido de mayor conductividad/corrosividad) + Rosemount 1056 → 4-20mA HART ✓

**Hallazgos:**
- **ANOMALÍA DE PORTADA:** La carátula (página 1) muestra código "P22-LI-09-008-003" — debe ser "P22-LI-09-008-005". Error de control documental, no afecta contenido técnico.
- Dos tecnologías en un solo datasheet: lógica técnica correcta (baja conductividad → contacto; alta conductividad/brine → toroidal).
- 4-20mA HART confirmado para todos los modelos ✓
- Señales: AI (HART) para todos los CIT ✓

**NOTA Van Doorn (no incluir en TM):** El sensor Rosemount 228 para CIT-09-005 (Rechazo total, salmuera concentrada) es apropiado — la tecnología toroidal no tiene electrodos expuestos al fluido, superior para fluidos altamente conductivos o corrosivos como brine RO.

### 3.2 P22-LI-09-008-006 — Differential Pressure Switch Rev A

**Make/Model:** Ashcroft 1132, SPDT relay (libre de potencial, ON/OFF)

**Hallazgos:** Sin observaciones técnicas. El tipo switch (ON/OFF) es apropiado para monitoreo de diferencial de filtro cartucho. Señal DI correcta en IL Rev B. ✅ APROBADO.

### 3.3 P22-LI-09-008-007 — Flow Transmitter Rev A

**Make/Model:** Rosemount 8750W electromagnético → confirma tipo requerido por ET §5.5.1 ✓. 4-20mA HART ✓.

**Hallazgos:**
- **FIT-09-004 (Reject Flow, Train Reject):** Electrodos Hastelloy C-276 en lugar de SS316L. Técnicamente justificado para brine concentrado de mayor corrosividad. BW Water debe confirmar las condiciones del fluido que justifican esta selección de material.
- Los 4 FIT con electrodos SS316L están en servicio de agua filtrada/CIP ✓.
- Modelo orden inicia con 'D' (Low-power DC, 12-42VDC) → compatible con 24VDC del sistema de instrumentación ✓.

### 3.4 P22-LI-09-008-008 — Level Switch Rev A

**Make/Model:** IFM KQ6005 capacitive proximity switch, salida PNP digital (IO-Link)

**Hallazgos:**
- Salida ON/OFF (PNP) es correcta para switches de nivel en estanque antiscalant ✓.
- **ERROR EN DATASHEET:** Fila de "Output Communication" dice "Current Output, 4-20mA HART". El KQ6005 es un switch digital con IO-Link — NO tiene salida 4-20mA HART. El IO Type "DI" en la IL Rev B es correcto. El datasheet tiene un error de plantilla en ese campo.
- Compatibilidad química con antiscalant: el datasheet no especifica. Material PBT + TPE-U apropiado para uso general; sin datos de compatibilidad explícita con antiscalant.

**NOTA Van Doorn (no incluir en TM):** IFM es marca reconocida con presencia en Chile. El sensor capacitivo exterior a la pared del estanque (non-invasive a través de pared no metálica) es una solución limpia para aplicación antiscalant.

### 3.5 P22-LI-09-008-009 — Level Transmitter Rev A

**Make/Model:** VEGA VEGABAR 82, CERTEC (ceramic cell, gauge pressure), 4-20mA HART ✓.

**Hallazgos:** Sin observaciones. FFKM (Kalrez) seals apropiados para CIP. ET §5.5.4 requiere "tipo Dpcell" — el VEGABAR 82 mide nivel por presión relativa (gauge), equivalente funcional a Dpcell para estanque abierto. ✅ APROBADO.

### 3.6 P22-LI-09-008-010 — pH/ORP Analyzer Rev A

**Make/Model:** Rosemount 3900 sensor + 1056 dual-channel transmitter. Un solo equipo cubre PHIT-09-001 (pH) y ORPIT-09-001 (ORP) mediante 2 canales independientes, 2x 4-20mA HART ✓.

**Hallazgos:**
- Sensor Rev A mostraba modelo 396P; Rev B de IL y datasheet coinciden con modelo 3900. Consistencia confirmada.
- Servicio: CIP Water — apropiado para análisis pH/ORP en lavado. ✅ APROBADO.

### 3.7 P22-LI-09-008-011 — Pressure Gauge Rev A

**Make/Model:** Wika 233.50 (Bourdon tube). Sin salida eléctrica, indicación local.

**Hallazgos:** PI-09-001/002 sin sello, PI-09-003/004/005/006 con sello de diafragma 990.10 (PTFE). Apropiado para servicios de CIP y antiscalant. ✅ APROBADO.

### 3.8 P22-LI-09-008-012 — Pressure Transmitter Rev A

**Make/Model:** Schneider Foxboro IGP05S, 4-20mA HART ✓, 2 hilos loop powered ✓.

**Hallazgos:**
- **Dos grupos de materiales:** PIT-09-001/002/003/004/005/009 (SS316L) vs PIT-09-006/007/008 (Hastelloy C). El split es técnicamente lógico: Hastelloy C para las líneas de rechazo/concentrado de mayor agresividad química.
- **PIT-09-007 (Interstage Turbo to Feed TC):** Su asignación al grupo Hastelloy C merece confirmación del tipo de fluido en ese punto de medición.
- Rangos disponibles del IGP05S (0-2 / 0-13.8 / 0-138 bar) cubren todos los rangos de operación de los PITs en la IL ✓.

### 3.9 P22-DWG-09-007-005 — Typical Installation Details of Power Works Rev A

**Contenido:** 7 hojas de detalles típicos de instalación eléctrica: motores centrifugos, bomba dosificadora, panel de calefacción, tableros PLC/LCP, bandejas portacables (pared, techo, piso).

**Hallazgos:**
1. **AUSENCIA DE DETALLES DE PUESTA A TIERRA (MAYOR):** No hay especificación de conductores de tierra de equipo, conexiones de bonding a bandejas portacables, ni esquemas de tierra de instrumentación (pantallas de cables analógicos). Para una instalación eléctrica de potencia, esto es una omisión significativa.
2. **SIN NORMAS ELÉCTRICAS CITADAS (MENOR):** El documento menciona "installation standards" de forma genérica sin identificar IEC 61439, IEC 60364, NEC, NCh o equivalente.
3. **Calibre de cables:** Diferido al Cable Schedule (no enviado) — aceptable como práctica de ingeniería.
4. **Separación de bandejas power / I&C:** Especificada ✓. Espaciado mínimo 300mm ✓.
5. **Material:** HDG (galvanizado en caliente) para todas las bandejas y soportes ✓.

### 3.10 P22-LI-09-008-013 — Temperature Transmitter Rev A

**Veredicto: 3 — To be Revised**

**Equipos cubiertos:** TIT-09-003 (CIP Tank Temperature Transmitter)
- Rosemount 214C RTD — PT-100, 3 hilos (S3), SS316 sheath, 10" sensor
- Rosemount 114C Thermowell — SS316/316L Dual Rated, tapered stem, 8" inmersión, 2" head
- Rosemount 644H Transmitter — DIN A head mount, 4-20mA HART, 24VDC, IP66, LCD display

**Aspectos conformes:**
- Protocolo 4-20mA HART confirmado ✓ (ET §5.5 L1311)
- Sensor Pt-100, 3 hilos confirmado ✓ (estándar proyecto)
- Fabricante Rosemount (Emerson) = marca reconocida ✓
- Material thermowell SS316/316L adecuado para CIP Water ✓
- IP66 confirmado ✓

**ANOMALÍA — Portada incorrecta (OBS-1 NOTA):**
La carátula muestra "Datasheet of Pressure Transmitter" en el encabezado del formulario ADASA. El documento es un Temperature Transmitter datasheet (TIT-09-003). Mismo patrón que -005 (Conductivity DS OBS-1). No afecta contenido técnico.

**ANOMALÍA CRÍTICA — TIT-09-003 no figura en IL Rev B (OBS-2 MAYOR):**
El TAG del datasheet es TIT-09-003. IL Rev B ítem 28 registra TIT-09-001 como el único transmisor de temperatura del CIP Tank (Rosemount 644 + RTD 214C + Thermowell 114C). TIT-09-003 no existe en la IL y no tiene punto IO asignado.

- La IL es el registro maestro de instrumentación: un instrumento con datasheet aprobable debe estar en ella con punto IO confirmado.
- Coherente con OBS-2 MENOR IL Rev B (IO List comprometida, 45 días): TIT-09-003 amplía el gap — no solo falta el punto IO sino el registro mismo.
- BW Water debe: (a) confirmar si TIT-09-001 y TIT-09-003 son instrumentos distintos o si uno reemplaza al otro; (b) agregar TIT-09-003 a la próxima IL con su punto AI; (c) presentar datasheet del instrumento que quede sin DS.

**Clase de exactitud no especificada (OBS-3 NOTA):**
El formulario de especificación no indica si se requiere Class A o Class B1 para el Rosemount 214C. El datasheet menciona "Optional Class A accuracy RTDs" como variante disponible. BW Water debe especificar la clase requerida para la aplicación de proceso CIP en la próxima revisión.

**NOTA Van Doorn (no incluir en TM):** La combinación 644H + 214C + 114C es la solución estándar Rosemount para aplicaciones industriales de temperatura de proceso. La configuración 3-wire es correcta para minimizar el error de resistencia de cables. La clase A vs B es relevante si se requiere alta exactitud (±0.15°C + 0.002|T| Class A vs ±0.3°C + 0.005|T| Class B).

---

## 4. OBSERVACIONES CONSOLIDADAS

| OBS | Documento | Severidad | Hallazgo | Acción requerida |
|-----|-----------|-----------|---------|-----------------|
| OBS-01 | IL Rev B | MAYOR | CIT-09-005 power supply = 120VAC (todos los demás = 24VDC) | Confirmar si error tipográfico o intención de diseño; corregir IL Rev C |
| OBS-02 | IL Rev B | MENOR | TAGs renumerados (FIT-09-002, LIT-09-002, VT/TE nuevos) no reflejados en IO List | Emitir IO List Rev B |
| OBS-03 | Power Works DWG | MAYOR | Sin detalles de puesta a tierra de equipos ni bonding de bandejas | Rev B debe incluir detalles de earthing |
| OBS-04 | Power Works DWG | MENOR | Sin normas eléctricas identificadas por nombre | Citar norma aplicable en Rev B |
| OBS-05 | Conductivity DS | MENOR | Carátula muestra código P22-LI-09-008-003 (debe ser -005) | Corregir en siguiente emisión |
| OBS-06 | Flow TX DS | NOTA | FIT-09-004 usa electrodos Hastelloy C-276 vs SS316L para otros FIT | Confirmar servicio de FIT-09-004 en respuesta a transmittal |
| OBS-07 | Level Switch DS | MENOR | Campo "Output Communication" dice "4-20mA HART" — incorrecto para KQ6005 (PNP digital) | Corregir en siguiente emisión |
| OBS-08 | Pressure TX DS | NOTA | PIT-09-007 (Interstage Turbo) en grupo Hastelloy C — confirmar servicio | Confirmar servicio en respuesta |
| OBS-09 | Temp TX DS | NOTA | Portada muestra "Pressure Transmitter" — documento es Temperature Transmitter DS (TIT-09-003) | Corregir designación en próxima revisión |
| OBS-10 | Temp TX DS | MAYOR | TIT-09-003 no figura en IL Rev B (ítem 28 registra solo TIT-09-001); sin punto IO asignado | Agregar TIT-09-003 a IL con punto AI; confirmar si TIT-09-001 y TIT-09-003 son distintos; presentar DS faltante |
| OBS-11 | Temp TX DS | NOTA | Clase de exactitud sensor Rosemount 214C no especificada (Class A vs Class B) | Especificar clase requerida para aplicación CIP en próxima revisión |
| OBS-12 | IL Rev B | MAYOR | CIT-09-001/004/005 (conductímetros lado salmuera) especifican rango máximo 20 mS/cm — posiblemente insuficiente para la conductividad real de la salmuera de Taltal (TDS diseño 43.000–53.000 mg/L per ET §4.1) | BW Water debe confirmar conductividad medida de la salmuera de Taltal y demostrar adecuación del rango; si conductividad supera 20 mS/cm, corregir rangos en IL Rev C |
| OBS-13 | IL Rev B | MENOR | VT-09-001/002/003 especifican modelo ifm VTV122 (0–25 mm/s RMS) pero no definen umbrales de alarma ni condiciones de interlock | BW Water debe definir setpoints de alarma (alta vibración) e interlock (alta-alta vibración) para cada equipo; referencia sugerida: ISO 10816-3 |

---

## 5. POSITIVOS A RESALTAR EN TM N8 (ACCIONES DE BW WATER QUE CIERRAN GAPS)

1. **3 vibration transmitters** (VT-09-001/002/003): cierra ET §5.5.6 — previamente ausentes en IL Rev A
2. **4 motor RTDs** (TE-09-001/002/003/004 — Pt-100, 3-wire): cierra ET §5.3 — previamente ausentes
3. **Duplicado FIT-09-001 corregido:** Dos instrumentos compartían el mismo TAG en Rev A; ahora FIT-09-001 y FIT-09-002 diferenciados correctamente
4. **5 conductivity measurement points confirmados** per ET §5.5.5 (CIT-09-001 a CIT-09-005)
5. **IL Rev B P&ID references updated** to Rev B drawings throughout

---

## 6. RESPONSE CODES Y VEREDICTO

| Código documento | Título | Rev | Response Code |
|-----------------|--------|-----|---------------|
| P22-LI-09-008-003 | Instrument List | B | **3 — To be Revised** |
| P22-LI-09-008-005 | Datasheet Conductivity Analyzer | A | 2 — Approved as Noted |
| P22-LI-09-008-006 | Datasheet Differential Pressure Switch | A | **1 — Approved** |
| P22-LI-09-008-007 | Datasheet Flow Transmitter | A | 2 — Approved as Noted |
| P22-LI-09-008-008 | Datasheet Level Switch | A | 2 — Approved as Noted |
| P22-LI-09-008-009 | Datasheet Level Transmitter (Pressure) | A | **1 — Approved** |
| P22-LI-09-008-010 | Datasheet pH/ORP Analyzer | A | **1 — Approved** |
| P22-LI-09-008-011 | Datasheet Pressure Gauge | A | **1 — Approved** |
| P22-LI-09-008-012 | Datasheet Pressure Transmitter | A | 2 — Approved as Noted |
| P22-DWG-09-007-005 | Typical Installation Details of Power Works | A | **3 — To be Revised** |
| P22-LI-09-008-013 | Datasheet Temperature Transmitter | A | **3 — To be Revised** |

**VEREDICTO GLOBAL: 3 — TO BE REVISED**
(IL Rev B: CIT-09-005 120VAC + TIT-09-003 no en IL; Power Works DWG: sin earthing specs)

---

## 8. ANÁLISIS DE LÍMITES OPERACIONALES

> Revisión cruzada rangos IL Rev B vs condiciones operacionales reales (ET §4.1 + Process Calculation Note P22-CD-09-009-001 Rev B).

### 8.1 Transmisores de Presión — Verificación de Rangos

Todos los PITs tienen rangos calibrados consistentes con las presiones de proceso calculadas.

| TAG | Servicio | Presión Proceso | Rango Calibrado IL Rev B | Evaluación |
|-----|---------|----------------|--------------------------|-----------|
| PIT-09-001 | HP Pump suction | ~3 bar (estimado) | 0–6 bar | ✅ Adecuado |
| PIT-09-002 | HP Pump discharge | ~51 bar | 0–51 bar | ✅ Adecuado |
| PIT-09-003 | Stage 1 feed (Turbo 1 outlet) | ~70 bar | 0–70 bar | ✅ Adecuado |
| PIT-09-004 | Stage 1 reject | ~68 bar | 0–68 bar | ✅ Adecuado |
| PIT-09-005 | Stage 2 feed (Turbo 2 outlet) | ~85 bar | 0–85 bar | ✅ Adecuado |
| PIT-09-006 | Stage 2 reject | ~60 bar | 0–83 bar | ✅ Adecuado |
| PIT-09-007 | Interstage Turbo to Feed TC | ~46 bar | 0–46 bar | ✅ Adecuado |
| PIT-09-008 | Train reject (Tie-in 3) | ~1 bar | 0–2 bar | ✅ Adecuado |
| PIT-09-009 | Permeate (Tie-in 2) | ~1 bar | 0–2 bar | ✅ Adecuado |

**Fuente presiones:** P22-CD-09-009-001 Rev B (Process Calculation Note).

### 8.2 Conductímetros — Verificación de Rangos vs Conductividad Esperada

| TAG | Servicio | TDS Estimado | Conductividad Esperada | Rango IL Rev B | Evaluación |
|-----|---------|-------------|----------------------|----------------|-----------|
| CIT-09-001 | Alimentación módulo | 43.000–53.000 mg/L | ~65–80 mS/cm | 0–20 mS/cm | ⚠ REQUIERE CONFIRMACIÓN |
| CIT-09-002 | Permeado total | <500 mg/L | <750 µS/cm | 0–2.000 µS/cm | ✅ Adecuado |
| CIT-09-003 | Permeado 2ª etapa | <500 mg/L | <750 µS/cm | similar CIT-09-002 | ✅ Adecuado |
| CIT-09-004 | Rechazo 1ª etapa | ~80.000–90.000 mg/L | ~80–100 mS/cm | 0–20 mS/cm | ⚠ REQUIERE CONFIRMACIÓN |
| CIT-09-005 | Rechazo total tren | ~90.000–100.000 mg/L | ~110–140 mS/cm | 0–20 mS/cm | ⚠ REQUIERE CONFIRMACIÓN |

**Base de cálculo conductividad:**
- Factor aproximado: ~1,5 µS/cm por mg/L TDS (válido para salmueras concentradas)
- Salmuera alimentación (53.000 mg/L): 53.000 × 1,5 ≈ 80 mS/cm
- Rechazo total estimado (~90.000–100.000 mg/L): ~135 mS/cm

**Caveat crítico:** ET §4.1 indica que "La relación entre conductividad y TDS será acordada con el Comprador durante la etapa de revisión de ingeniería." La observación OBS-10 debe formularse como solicitud de confirmación a BW Water, no como certeza de error.

### 8.3 Caudalímetros — Verificación de Rangos

| TAG | Servicio | Caudal Diseño | Rango IL Rev B | Evaluación |
|-----|---------|--------------|----------------|-----------|
| FIT-09-001 | Alimentación | 49 m³/h | 0–100 m³/h | ✅ Adecuado |
| FIT-09-002 | Permeado 2ª etapa | ~8–9 m³/h | 0–18 m³/h | ✅ Adecuado |
| FIT-09-003 | Permeado total tren | ~20–21 m³/h | 0–40 m³/h | ✅ Adecuado |
| FIT-09-004 | Rechazo total tren | ~28–29 m³/h | 0–60 m³/h | ✅ Adecuado |
| FIT-09-005 | Bomba CIP | ~54 m³/h | 0–100 m³/h | ✅ Adecuado |

### 8.4 Resumen de Hallazgos

- **Transmisores de presión (9 PITs):** todos los rangos verificados como adecuados ✅
- **Caudalímetros (5 FITs):** todos los rangos verificados como adecuados ✅
- **Conductímetros lado permeado (CIT-09-002/003):** rangos adecuados ✅
- **Conductímetros lado salmuera (CIT-09-001/004/005):** rango máximo 20 mS/cm requiere confirmación contra conductividad real medida de la salmuera de Taltal ⚠
- **Transmisores de vibración (VT-09-001/002/003):** rangos adecuados; umbrales de alarma no definidos ⚠

---

## 7. PENDIENTES PREVIOS RELEVANTES

| Ítem | Origen | Días abierto (al 09-Mar-2026) | Estado |
|------|--------|-------------------------------|--------|
| Modbus TCP Memory Map | TM N2 | ~66 días | PENDIENTE |
| IO List Rev B | TM N3 | ~45 días | PENDIENTE — crítico: IL Rev B agrega 7 nuevos puntos |

---

## 9. ANÁLISIS CONSOLIDADO DE VOLTAJES — REVISIÓN CRUZADA

> **Objetivo:** Cuadro definitivo de voltajes del módulo cruzando Load List Rev A, Utility Consumption List Rev B, IO List Rev A, IL Rev B y ET §5.4.7. Identifica inconsistencias pendientes y el estado actualizado post-Rev B de documentos BW Water.

---

### 9.1 Matriz de Voltajes por Categoría

| Categoría | Equipo / TAG | Voltaje | Fase | Frecuencia | Fuente Load List Rev A | Fuente Utility List Rev B | Estado |
|-----------|--------------|---------|------|------------|----------------------|--------------------------|--------|
| **Motor principal (VFD)** | BH-09-001 HP Feed Pump | 380 V | 3Ph | 50 Hz | 83 kW ✓ | 93 kW nominal / 78.5 kW op. | ⚠ Potencia difiere entre documentos — TM N4 OBS-08 PENDIENTE |
| **Motor principal (VFD)** | BH-09-002 CIP Pump | 380 V | 3Ph | 50 Hz | 9.30 kW ✓ | 11 kW nominal / 10 kW op. | ⚠ Potencia nominal difiere entre documentos |
| **Calefacción resistiva** | REL-09-001 CIP Tank Heater | 380 V | 3Ph | 50 Hz | 16 kW ✓ | 20 kW nominal / 17 kW op. | ⚠ Potencia nominal difiere entre documentos |
| **Auxiliar monofásico** | BDS-09-001 A/B Dosing Pumps | 220 V | 1Ph | 50 Hz | 0.24 kW ✓ | 0.024 kW nominal | ⚠ Decimal posiblemente errado en Utility List (factor 10x) |
| **Auxiliar monofásico** | SAI-09-001 PLC / LCP | 220 V | 1Ph | 50 Hz | 1.00 kW ✓ | 2 kW nominal | ⚠ Potencia difiere (1 vs 2 kW) |
| **Auxiliar monofásico** | SSAA Lighting Indoor/Outdoor | 220 V | 1Ph | 50 Hz | 0.16 kW ✓ | 0.16 kW ✓ | ✅ Consistente |
| **Auxiliar monofásico** | A/C (1W+1S) | 220 V | 1Ph | 50 Hz | — | 2.00 kW nominal / 1.70 kW op. | ✅ Corregido a 2 unidades (TM N4) |
| **Actuadores** | Motorized Valves (13 uds.) | — | — | — | — | 0.12 kW c/u | ✅ Sin observaciones |
| **Control / I&C** | PLC I/O modules (24VDC bus) | 24 VDC | — | — | — | (power interna desde SAI-09-001) | ✅ Consistente con ET |
| **Instrumentación** | Todos los instrumentos (38/39) | 24 VDC | — | — | — | (ver §9.2) | ✅ Excepto CIT-09-005 |
| **ANOMALÍA** | CIT-09-005 RO Train Reject Cond. | **120 VAC** | 1Ph | — | — | No aparece | ⚠ TM N8 OBS-01 — único instrumento no 24VDC |

---

### 9.2 Sistema de 24 VDC — Instrumentación y Control

Revisión ítem por ítem de la columna "Power Supply" en IL Rev B (39 ítems totales):

| TAG | Descripción | Power Supply IL Rev B | Estado |
|-----|-------------|----------------------|--------|
| DPS-09-001 | Differential Pressure Switch (Cartridge Filter) | 24 VDC | ✅ |
| ORPIT-09-001 | ORP Analyzer (CIP Water) | 24 VDC | ✅ |
| CIT-09-001 | Conductivity — Cartridge Filter Discharge | 24 VDC | ✅ |
| CIT-09-002 | Conductivity — RO Train Permeate | 24 VDC | ✅ |
| CIT-09-003 | Conductivity — Stage 2 Permeate | 24 VDC | ✅ |
| CIT-09-004 | Conductivity — Stage 1 Reject | 24 VDC | ✅ |
| **CIT-09-005** | **Conductivity — RO Train Reject (toroidal)** | **120 VAC** | ⚠ **ANOMALÍA** |
| FIT-09-001 | Flow — Cartridge Filter Discharge | 24 VDC | ✅ |
| FIT-09-002 | Flow — Stage 2 Permeate | 24 VDC | ✅ |
| FIT-09-003 | Flow — RO Train Permeate | 24 VDC | ✅ |
| FIT-09-004 | Flow — RO Train Reject | 24 VDC | ✅ |
| FIT-09-005 | Flow — CIP Pump Discharge | 24 VDC | ✅ |
| PIT-09-001 | Pressure — HP Pump Feed | 24 VDC | ✅ |
| PIT-09-002 | Pressure — HP Pump Discharge | 24 VDC | ✅ |
| PIT-09-003 | Pressure — Stage 1 Feed | 24 VDC | ✅ |
| PIT-09-004 | Pressure — Stage 1 Reject | 24 VDC | ✅ |
| PIT-09-005 | Pressure — Stage 2 Feed | 24 VDC | ✅ |
| PIT-09-006 | Pressure — Stage 2 Reject | 24 VDC | ✅ |
| PIT-09-007 | Pressure — Interstage Turbo to Feed TC | 24 VDC | ✅ |
| PIT-09-008 | Pressure — Train Reject | 24 VDC | ✅ |
| PIT-09-009 | Pressure — Combined Permeate | 24 VDC | ✅ |
| VT-09-001 | Vibration — HP Pump | 24 VDC | ✅ |
| VT-09-002 | Vibration — Feed Turbocharger | 24 VDC | ✅ |
| VT-09-003 | Vibration — Interstage Turbocharger | 24 VDC | ✅ |
| TE-09-001 | RTD Bearing — HP Pump motor (Fedco PT100) | 24 VDC | ✅ |
| TE-09-002 | RTD Winding — HP Pump motor (Fedco PT100) | 24 VDC | ✅ |
| TE-09-003 | RTD Bearing — CIP Pump motor (Grundfos PT100) | 24 VDC | ✅ |
| TE-09-004 | RTD Winding — CIP Pump motor (Grundfos PT100) | 24 VDC | ✅ |
| TIT-09-001 | Temperature Transmitter — CIP Tank | 24 VDC | ✅ |
| LIT-09-002 | Level Transmitter — CIP Tank | 24 VDC | ✅ |
| LS-09-001 | Level Switch High — Antiscalant Dosing Tank | 24 VDC | ✅ |
| LS-09-002 | Level Switch Low — Antiscalant Dosing Tank | 24 VDC | ✅ |
| PHIT-09-001 | pH Analyzer (CIP Water) | 24 VDC | ✅ |
| PI-09-001/006 | Pressure Gauges (6 uds., indicación local) | Sin alimentación eléctrica | ✅ |

**Resultado:** 33 instrumentos con salida eléctrica activa → 32 en 24 VDC, **1 en 120 VAC (CIT-09-005)**. Uniformidad del sistema de instrumentación: 97%.

---

### 9.3 Sistema de Fuerza — 380 V / 220 V

Cuadro consolidado de equipos de fuerza, cruzando Load List Rev A vs Utility Consumption List Rev B:

| Ítem | Equipo | Voltaje | Frecuencia | kW nominal — Load List Rev A | kW nominal — Utility List Rev B | Δ Potencia |
|------|--------|---------|------------|------------------------------|----------------------------------|-----------|
| 1 | BH-09-001 HP Feed Pump | 380V / 3Ph | 50 Hz | **83 kW** | **93 kW** | **+10 kW** — TM N4 OBS-08 PENDIENTE |
| 2 | BH-09-002 CIP Pump | 380V / 3Ph | 50 Hz | **9.30 kW** | **11 kW** | **+1.7 kW** |
| 3 | REL-09-001 CIP Tank Heater | 380V / 3Ph | 50 Hz | **16 kW** | **20 kW** | **+4 kW** |
| 4 | BDS-09-001A/B Dosing Pumps | 220V / 1Ph | 50 Hz | **0.24 kW** | **0.024 kW** | **Factor 10x** — posible error decimal |
| 5 | SAI-09-001 PLC / LCP | 220V / 1Ph | 50 Hz | **1.0 kW** | **2.0 kW** | **+1.0 kW** |
| 6 | SSAA Lighting | 220V / 1Ph | 50 Hz | 0.16 kW | 0.16 kW | ✅ Sin diferencia |
| 7 | A/C units (1W+1S) | 220V / 1Ph | 50 Hz | — | 2.00 kW (1 op.) | ✅ Corregido (TM N4) |
| 8 | Motorized Valves (13 uds.) | — | — | — | 0.12 kW c/u | — |

**Frecuencias:** Todos los equipos de fuerza confirman **50 Hz** en Utility List Rev B — consistente con ET §5.4.7 y la red eléctrica chilena.

**Nota sobre BDS-09-001:** El factor 10x entre Load List (0.24 kW) y Utility List (0.024 kW = 24W) sugiere un error decimal en uno de los documentos. Para una bomba dosificadora de antiscalant, 0.24 kW (240W) es el orden de magnitud realista. BW Water debe confirmar el valor correcto.

---

### 9.4 Inconsistencias Identificadas — Estado Actualizado al 09-Mar-2026

| Inconsistencia | TM | OBS | Severidad | Estado |
|---|---|---|---|---|
| CIT-09-005: 120 VAC vs 24 VDC (sistema instrumentación) | N8 | OBS-01 | MAYOR | **BORRADOR** — TM N8 no enviado. Incluir en envío |
| HP Pump potencia: 83 kW (Load List Rev A) vs 93 kW (Utility List Rev B / datasheet Rev C) | N4 | OBS-08 | MAYOR | PENDIENTE ~30 días (N4 enviado, sin respuesta) |
| PLC frecuencia: 60 Hz (Utility List Rev A) vs 50 Hz (ET) | N4 | OBS-01 | CRÍTICO | **CORREGIDO** en Utility List Rev B (E13, 11-Feb-2026). BW confirmó "revised accordingly" en comment sheet |
| UPS autonomía: 30 min (BW Water) vs 8 h (ET §5.4) | N7 | OBS-01 | CRÍTICO | **BORRADOR** — TM N7 no enviado |
| Dosing Pump: 0.24 kW (Load List Rev A) vs 0.024 kW (Utility List Rev B) | — | Nuevo | MENOR | No cubierto en transmittal previo — evaluar incluir en TM N8 o nuevo ítem |
| PLC potencia: 1.0 kW (Load List Rev A) vs 2.0 kW (Utility List Rev B) | — | Nuevo | MENOR | No cubierto en transmittal previo — evaluar incluir |

**Observación sobre TM N4 OBS-01 (PLC 60 Hz):** La Utility List Rev B (emitida 11-Feb-2026, Entrega 13) corrigió explícitamente la frecuencia de PLC a 50 Hz, con confirmación en el comment sheet. Aunque TM N4 fue enviado antes de E13, la corrección está documentada. Al recibir la respuesta formal de BW Water a TM N4, este ítem debería cerrarse con referencia a Utility List Rev B.

---

### 9.5 Anomalía CIT-09-005 — Análisis Técnico Detallado

**Equipo:** Rosemount 228 (sensor toroidal) + Rosemount 1056 (transmisor)
**Power Supply declarado en IL Rev B:** 120 VAC
**Part number 1056 para CIT-09-005:** `1056-02-21-31-HT-UL`
**Part number 1056 para CIT-09-001/002/003/004:** `1056-03-20-30-HT-UL`

Los part numbers de los transmisores 1056 difieren en la posición 3 (`02` vs `03`) y en los campos siguientes. En la nomenclatura Rosemount 1056, esta posición indica la configuración de alimentación y canales. La diferencia entre `1056-02-21-31` y `1056-03-20-30` sugiere que BW Water ordenó deliberadamente una versión de alimentación diferente para CIT-09-005 — lo que sería coherente con la anotación 120 VAC en la IL.

**Análisis del Rosemount 1056 según hoja de datos del fabricante:**
- El transmisor Rosemount 1056 acepta dos rangos de alimentación según la versión ordenada:
  - **Low Power DC:** 20–30 VDC (opción estándar, usada en los 4 CITs contacting)
  - **AC Power:** 85–265 VAC (opción de mayor potencia, para sensores más demandantes)
- El sensor toroidal Rosemount 228 requiere mayor energía de excitación que el contacting 400 series. La versión AC del 1056 puede ser técnicamente necesaria para este sensor.

**Implicaciones de diseño si 120 VAC es intencional:**
1. Se necesita un ramal 120 VAC aislado dentro del tablero eléctrico — este voltaje no existe como estándar en la red chilena (ET §5.4.7 lista solo 380V y 220V).
2. Se requiere un transformador 220V → 120V dedicado para alimentar este único instrumento, o bien cambiar a la versión 220 VAC del 1056.
3. El diagrama eléctrico del tablero y el esquema de distribución deben reflejar este ramal aislado.

**Hipótesis más probable:** La selección de la versión AC del 1056 para el sensor toroidal 228 tiene justificación técnica, pero el voltaje debería especificarse como 220 VAC (compatible con la red chilena) y no 120 VAC (que no es estándar en el proyecto). La anotación 120 VAC puede ser un error de transcripción desde la hoja de datos norteamericana del 1056 (que lista 120 VAC para la versión AC en estándar UL), cuando el proyecto requiere 220 VAC / 50 Hz.

**Acción requerida de BW Water:**
- Confirmar si el voltaje real de operación de CIT-09-005 es 120 VAC o 220 VAC.
- Si es AC (cualquier voltaje): identificar el punto de suministro en el diagrama eléctrico y confirmar que el transformador de aislamiento (si aplica) está incluido en el alcance de suministro.
- Si es error tipográfico: corregir a 24 VDC (versión DC del 1056) o a 220 VAC (versión AC adaptada a la red del proyecto) en IL Rev C.
