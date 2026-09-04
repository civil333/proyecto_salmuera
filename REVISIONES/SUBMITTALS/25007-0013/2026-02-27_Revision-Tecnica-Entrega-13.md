# Revisión Técnica — Entrega 13 (Submittal 25007-0013)

**Fecha revisión:** 27-Feb-2026
**Submittal:** 25007-0013
**Fecha entrega:** 26-Feb-2026
**Preparado por:** Luis Rivera

---

## Documentos Recibidos

| # | Código | Descripción | Rev | Estado |
|---|--------|-------------|-----|--------|
| 1 | P22-ET-09-009-002 | Datasheet RO HP Feed Pump | C | Revisado |
| 2 | P22-ET-09-009-005 | Datasheet RO Cartridge Filter | C | Revisado |
| 3 | P22-ET-09-009-007 | Datasheet Feed Turbocharger | C | Revisado |
| 4 | P22-ET-09-009-008 | Datasheet Interstage Turbocharger | C | Revisado |
| 5 | P22-ET-09-009-012 | Datasheet Static Mixer | B | Revisado |
| 6 | P22-LI-09-005-002 | Valve List | B | Revisado |
| 7 | P22-LI-09-009-001 | Utility Consumption List | B | Revisado |
| 8 | CCS - RO Cartridge Filter | Vendor Spec CCS | — | Revisado |
| 9 | CCS - Static Mixer | Vendor Spec CCS | — | Revisado |

---

## 1. Utility Consumption List Rev B (P22-LI-09-009-001)

### Estado de observaciones previas

| Obs | Origen | Descripción | Veredicto Rev B |
|-----|--------|-------------|----------------|
| TM N4 OBS-05 | PLC 60Hz | Sistema de control indicaba 220V/1PH/60Hz | **RESUELTO ✓** — Rev B muestra 220V/1PH/50Hz |
| TM N2/N4 | A/C n+1 | Solo 1 unidad especificada, ET 5.1.11 requiere n+1 | **RESUELTO ✓** — Descripción ahora indica "(1W+1S)" |
| TM N2 | A/C thermal calc | Cálculo térmico de A/C no presentado | **PENDIENTE** — BWW afirma "revised based on thermal calculation" pero no entrega el cálculo |

### Datos Rev B

| Ítem | Descripción | Alimentación | Potencia Motor [kW] | Carga Operacional [kW] |
|------|-------------|--------------|---------------------|------------------------|
| 1 | RO HP Feed Pump | 380V/3PH/50Hz | 93 | 78.5 |
| 2 | Antiscalant Dosing Pump A/B | 220V/1PH/50Hz | 0.024 | 0.02 |
| 3 | CIP Pump | 380V/3PH/50Hz | 11 | 10.00 |
| 4 | CIP Tank Heater | 380V/3PH/50Hz | 20 | 17.00 |
| 5 | PLC and Control System | 220V/1PH/**50Hz** | 2 | 2.00 |
| 6 | Lighting (Indoor) | — | 0.16 | 0.16 |
| 7 | Lighting (Outdoor) | — | 0.16 | 0.16 |
| 8 | Air Conditioning **(1W+1S)** | — | 2.00 | 1.70 |
| 9 | Motorized Valves (×13) | — | 0.12 | 0.12 |

**Consumo total declarado:** 1,983 kWh/día | 21 m3/h producción | 3.93 kWh/m3

### Hallazgos

**RESUELTO — PLC 50Hz:** La referencia a 60Hz fue eliminada. Rev B indica 220V/1PH/50Hz. Observación TM N4 OBS-05 cerrada.

**RESUELTO — A/C n+1:** La descripción del ítem 8 indica "Air Conditioning (1W+1S)", confirmando configuración 1 activo + 1 standby. Potencia total de 2 unidades no explicitada en tabla (solo se muestra operacional), pero la nota de BW Water ("We have assumed that only one unit will be running at any given time") es técnicamente correcto para tabla de consumo.

**PENDIENTE — Cálculo térmico A/C:** El cálculo específico que justifica los 2.00 kW por unidad no ha sido entregado como documento separado. BW Water indica que el consumo fue revisado "based on the A/C thermal calculation", pero este cálculo no forma parte de E13. Observación TM N2 sigue técnicamente abierta para cierre formal.

**NOTA — HP Pump 93 kW:** La Utility List Rev B muestra 93 kW (motor rating) con 78.5 kW operating load. Esto es técnicamente correcto: 93 kW es la potencia nominal de placa (125 HP × 0.746 = 93.25 kW), 78.5 kW es la potencia absorbida en punto de diseño. La distinción resuelve la inconsistencia reportada en TM N4 OBS-06.

**Veredicto Utility List Rev B: 2 — Approved as Noted**
*(PLC y A/C n+1 resueltos; cálculo térmico A/C pendiente como documento separado)*

---

## 2. Valve List Rev B (P22-LI-09-005-002)

### Estado de observaciones previas

| Obs | Descripción | Respuesta BW Water en CCS | Veredicto en Rev B |
|-----|-------------|---------------------------|-------------------|
| OBS-01 | VM-09-015 DN100 sin actuación eléctrica | "Noted, Already revised on Valve List Rev. B" | **PARCIALMENTE RESUELTO** |
| OBS-02 | TAG duplicado VM-09-015 | "Noted, Already revised on Valve List Rev. B" | **NO RESUELTO — CRÍTICO** |
| OBS-03 | TAG duplicado VE-09-008 | "Noted, Already revised on Valve List Rev. B" | **NO RESUELTO — CRÍTICO** |
| OBS-04 | TAG duplicado VE-09-010 | "Noted, Already revised on Valve List Rev. B" | **RESUELTO ✓** |
| OBS-05 | Area codes VM-07-xxx incorrecto | "Noted, Already revised on Valve List Rev. B" | **RESUELTO ✓** |
| OBS-06 | Manufacturers "TBA" | "Will submit datasheet/brochure prior to procurement" | **PENDIENTE** |

### Hallazgos Detallados

#### OBS-01 — VM-09-015: Actuación Eléctrica

**Estado: PARCIALMENTE RESUELTO**

El ítem 18 de Rev B muestra la válvula VM-09-015 como "ON/OFF MOTORIZED", DN100, Butterfly, ANSI 900#, CE3MN, con alimentación 380/220 VAC 50Hz y protocolo Ethernet IP. La actuación eléctrica fue incorporada, atendiendo la observación principal (ET 5.2.3).

**Observación residual (menor):** El TAG del ítem 18 sigue siendo "VM-09-015" (prefijo "VM" = Manual Valve) cuando debería actualizarse a "VE-09-015" (prefijo "VE" = Electric Valve) para consistencia con la nomenclatura del proyecto. Esto no es técnicamente bloqueante pero requiere corrección documental y actualización en P&ID, IO List e Instrument List.

#### OBS-02 — TAG duplicado VM-09-015

**Estado: NO RESUELTO — CRÍTICO**

A pesar de que BW Water afirma "Already revised", la Valve List Rev B mantiene dos ítems con el TAG "VM-09-015":

| Ítem | TAG | Sistema | Tamaño | Tipo | Actuación |
|------|-----|---------|--------|------|-----------|
| 18 | VM-09-015 | SWRO HPP | DN100 | Butterfly | MOTORIZADA (VE) |
| 43 | VM-09-015 | SWRO REJECT 1ST | DN15 | Ball | MANUAL |

Dos válvulas con el mismo TAG es un error de ingeniería que genera conflicto en P&ID, SCADA/DCS, IO List y pruebas de comisionamiento. BW Water no revisó este ítem correctamente en Rev B.

**Acción requerida:** Reasignar TAG único a la válvula del ítem 43 (sugerido: VM-09-015A o VM-09-017 según correlativo disponible).

#### OBS-03 — TAG duplicado VE-09-008

**Estado: NO RESUELTO — CRÍTICO**

La Valve List Rev B mantiene dos ítems con el TAG "VE-09-008":

| Ítem | TAG | Sistema | Tamaño | Rating | Material | Servicio |
|------|-----|---------|--------|--------|----------|---------|
| 44 | VE-09-008 | SWRO REJECT 1ST | DN80 | ANSI 900# | CE3MN | Rechazo 1° etapa |
| 57 | VE-09-008 | SWRO PERMEATE 1ST | DN80 | ANSI 150# | DI/SS420 | Permeado 1° etapa |

Materiales, presiones y servicios completamente distintos bajo el mismo TAG. Error crítico para control y comisionamiento.

**Acción requerida:** Reasignar TAG único al ítem 57 (sugerido: VE-09-011 o correlativo siguiente disponible).

#### NUEVAS OBSERVACIONES en Rev B

**OBS-07 (NUEVO) — TAG duplicado VE-09-009:**

| Ítem | TAG | Sistema | Tamaño | Rating | Material |
|------|-----|---------|--------|--------|----------|
| 58 | VE-09-009 | SWRO 2ND STAGE REJECT | DN80 | ANSI 900# | CE3MN |
| 93 | VE-09-009 | ANTISCALANT | DN25 | ANSI 150# | PVC |

Nueva duplicación introducida en Rev B. Materiales y ratings incompatibles.

**OBS-08 (NUEVO) — TAG duplicado VM-09-065:**

| Ítem | TAG | Sistema | Tamaño | Rating | Servicio |
|------|-----|---------|--------|--------|---------|
| 30 | VM-09-065 | SWRO PERMEATE 1ST | DN65 | ANSI 150# | Permeado 1° etapa |
| 76 | VM-09-065 | CIP | DN150 | ANSI 150# | CIP |

Nueva duplicación introducida en Rev B.

### Resumen Valve List Rev B

| # | Observación | Severidad | Estado |
|---|-------------|-----------|--------|
| 1 | VM-09-015 DN100 actuación eléctrica | Crítico | Resuelto ✓ (pendiente renombrar VM→VE) |
| 2 | Duplicado TAG VM-09-015 | Crítico | No resuelto — Rev C requerida |
| 3 | Duplicado TAG VE-09-008 | Crítico | No resuelto — Rev C requerida |
| 4 | Duplicado TAG VE-09-010 | Mayor | Resuelto ✓ (ahora VE-09-016) |
| 5 | Area codes VM-07-xxx | Menor | Resuelto ✓ |
| 6 | Manufacturers TBA | Mayor | Pendiente — deferido a pre-procurement |
| 7 (NUEVO) | Duplicado TAG VE-09-009 | Crítico | Nuevo en Rev B |
| 8 (NUEVO) | Duplicado TAG VM-09-065 | Mayor | Nuevo en Rev B |

**Veredicto Valve List Rev B: 3 — To be Revised**
*(TAGs duplicados OBS-02, OBS-03, OBS-07, OBS-08 no resueltos y/o nuevos — crítico para P&ID y SCADA)*

---

## 3. HP Pump Datasheet Rev C (P22-ET-09-009-002)

### Estado de observaciones previas

| Obs | Origen | Descripción | Veredicto Rev C |
|-----|--------|-------------|----------------|
| 25007-HPPUMP / TM N3 | Pt-100 devanados | Motor sin Pt-100 en bobinados | **RESUELTO ✓** |
| TM N3 | RTD tipo Pt-100 | Confirmación tipo 100Ω @ 0°C | **RESUELTO ✓** |
| TM N4 OBS-06 | Power inconsistency | 4 valores diferentes (83/86/92/93 kW) | **SUSTANCIALMENTE RESUELTO ✓** |
| TM N3 | Vibration mounting | Falta de montaje para sensor de vibración | **RESUELTO ✓** |

### Datos Rev C

- **Fabricante:** FEDCO, Modelo MSD-7016
- **Potencia motor (nameplate):** 125 HP = 93 kW
- **Potencia absorbida (design point):** 78.5 kW @ 49.0 m3/h, 46.9 bar
- **Velocidad:** 2,938 RPM (VFD)
- **RTDs rodamientos:** 3-wire, 100 Ohm Platinum (Pt-100) ✓
- **RTDs devanados:** 3-wire, 100 Ohm Platinum (Pt-100) ✓
- **Montaje sensor vibración:** Confirmado en datasheet ✓
- **Clase de aislamiento:** F, IP66

### Hallazgos

**RESUELTO — Pt-100 devanados:** El datasheet Rev C incluye explícitamente: "3-wire RTDs for bearings (100 Ohm Platinum)" y "3-wire RTDs for windings (100 Ohm Platinum)". Observación cerrada. Cumple ET 5.3 L1032.

**RESUELTO — Vibración:** "With Mounting Surface for a vibration sensor" confirmado. Cumple ET 5.5.7 L1390.

**RESUELTO — Consistencia de potencia:** Rev C muestra 93 kW (motor rating) como potencia de placa y 78.5 kW como potencia absorbida en el punto de diseño. Esta distinción resuelve la confusión anterior. La Utility List Rev B usa los mismos valores consistentemente.

**NOTA (menor):** El datasheet FEDCO incluido en el DS (Technical Proposal) muestra "Electric Power 83 kW" (motor input nominal) y "Electric Power 85 kW" (VFD input), que son valores legítimos pero distintos métricas. Se recomienda incluir nota en el documento que aclare la diferencia: 93 kW = nameplate rating, 78.5 kW = absorbed power at design point, 83 kW = motor input (nominal), 85 kW = VFD input (nominal).

**Veredicto HP Pump Rev C: 2 — Approved as Noted**
*(Todas las observaciones críticas resueltas; nota menor sobre clarificación de valores de potencia)*

---

## 4. Feed Turbocharger Rev C (P22-ET-09-009-007)

### Estado de observaciones previas

| Obs | Descripción | Veredicto Rev C |
|-----|-------------|----------------|
| TM N3 | Vibration transmitters | **VER NOTA** — HP Pump CCS menciona "same will be done for turbochargers" pero NO está explícito en el datasheet |
| TM N3 | Margen operacional 10% | **MANTENIDO ✓** — Performance data confirma 10% safety margin |
| TM N3 | Coupling 2000 psi | **CAMBIADO — OBSERVACIÓN** — Reducido a 1200 psi |

### Datos Rev C

- **Fabricante:** FEDCO, Modelo HPB-60
- **TAG:** SIP-09-001
- **Feed Flow:** 49.0 m3/h | Brine Flow: 28.0 m3/h
- **Feed Inlet Pressure:** 48.9 bar | Membrane Pressure: 69.53 bar
- **Brine Inlet Pressure:** 53.5 bar | Brine Outlet: 1.0 bar
- **Coupling Feed:** 1200 psi (reducido de 2000 psi en Rev B)
- **Coupling Brine:** 1200 psi
- **Margen operacional:** 10% safety margin (53k TDS, 19°C, 1 year projection)
- **Material:** Super Duplex 2507

### Hallazgos

**OBSERVACIÓN CRÍTICA — Reducción de rating de acople 2000 → 1200 psi: RECHAZADO**

La presión de diseño del sistema en la conexión del Feed Turbocharger (1° etapa) alcanza 69.53 bar (1,009 psi) a la salida hacia la membrana. Los acoples de 1200 psi ofrecen un margen de solo 19% sobre la presión máxima de operación (1200/1009 = 1.19x).

Para sistemas de proceso con fluidos corrosivos (salmuera concentrada), los estándares de ingeniería requieren un factor de diseño mínimo de 1.5x sobre la presión máxima operacional (MAWP). El margen de 1.19x incumple este criterio de forma clara. Adicionalmente, el acople Style D no está clasificado para HPB service (cambio de clase de producto respecto a Rev B, que utilizaba Piedmont Style H para Energy Recovery turbochargers). La justificación de BW Water ("2000 psi coupling is out of stock") no constituye criterio técnico válido y no puede usarse para justificar un cambio de clase de producto.

**Ref:** ET §5.2 criterios de rating de presión

**PENDIENTE — Datasheet del coupling no incluido en Rev C:** El datasheet Rev C no adjunta la ficha técnica del fabricante del acople (modelo, MAWP, clasificación de servicio). Sin este documento no es posible verificar el MAWP efectivo del acople Style D en servicio con brine a temperatura de diseño.

**PENDIENTE — Montaje sensor vibración:** El datasheet Rev C no incluye explícitamente referencia a "Mounting Surface for vibration sensor" en las turbocharger datasheets. El CCS del HP Pump indica "same will be done for turbochargers" pero no está documentado en el datasheet. Requiere confirmación explícita en Rev D o addendum.

**Ref:** ET 5.5.7 L1390.

**MANTENIDO — Margen operacional 10%:** Los datos BiTurbo confirman 10% safety margin en todas las condiciones de diseño (Y0/Y1 projection, 19°C/24°C). ✓

**Path to Resolution (Code 4 → Code 2):** ADASA confirma una vía técnicamente aceptable: upgrade del acople Feed TC a ≥ 1,800 psi Y entrega del datasheet del fabricante del acople (modelo, MAWP, certificación HPB service) para ambos turbochargers. Bajo estas condiciones, ADASA revisaría el veredicto de Code 4 a Code 2. La solución preferida de ADASA sigue siendo el retorno a 2,000 psi (Piedmont Style H), que constituyó la línea de base contractual.

**Veredicto Feed Turbocharger Rev C: 4 — Rejected**
*(Margen 1.19x inferior al mínimo ASME 1.5x; cambio de clase de producto Style D sin justificación técnica; datasheet del coupling no entregado)*

---

## 5. Interstage Turbocharger Rev C (P22-ET-09-009-008)

### Datos Rev C

- **Fabricante:** FEDCO, Modelo HPB-60
- **TAG:** SIP-09-002
- **Feed Flow:** 36.1 m3/h | Brine Flow: 28.0 m3/h
- **Feed Inlet Pressure:** 68.2 bar | Membrane Pressure: 84.8 bar
- **Brine Inlet Pressure:** 83.33 bar | Brine Outlet: 53.5 bar
- **Coupling Feed & Brine:** 1800 psi (reducido de 2000 psi en Rev B)

### Hallazgos

**ACEPTABLE — Reducción coupling 2000 → 1800 psi:** La presión máxima de operación en 2° etapa alcanza 84.8 bar (1,230 psi). Con acople de 1800 psi, el margen es 1800/1230 = 1.46x, cercano al mínimo aceptable de 1.5x. Es marginalmente aceptable con nota de que el MAWP efectivo sea confirmado formalmente por FEDCO.

**PENDIENTE — Datasheet del coupling no incluido en Rev C:** El documento especifica 1,800 psi para el acople pero no adjunta la ficha técnica del fabricante del acople (modelo, MAWP, clasificación de servicio). La entrega de este datasheet es condición para mantener el Code 2 aprobado. Acción requerida: entregar datasheet del coupling junto con la próxima revisión.

**PENDIENTE — Montaje sensor vibración:** Mismo comentario que Feed Turbocharger. No está explícitamente documentado en Rev C.

**Ref:** ET 5.5.7 L1390.

**Veredicto Interstage Turbocharger Rev C: 2 — Approved as Noted**
*(Coupling 1800 psi marginalmente aceptable a 84.8 bar servicio; datasheet del coupling no entregado — condición para mantener Code 2; vibration mounting pendiente de confirmación explícita)*

---

## 6. RO Cartridge Filter Rev C (P22-ET-09-009-005)

### Datos Rev C

- **Fabricante:** Filtrek, Modelo FRPH12-012-4-4F-100
- **TAG:** FIL-09-001
- **Cartuchos:** 12 unidades, 2.5" OD × 40" L, 1 micron, Polipropileno (Alaris Gold)
- **Flujo por cartucho:** 4.08 m3/h (49.0/12)
- **Material housing:** FRP
- **Presión de diseño:** 100 psi (6.9 bar)
- **Cambio Rev C vs Rev B:** Orientación de boquillas modificada para optimizar piping en container

### Hallazgos

**CONFIRMADO — 12 cartuchos:** BW Water justifica con el flujo recomendado por el fabricante de 4.54 m3/h (20 GPM) por cartucho de 40". El valor actual (4.08 m3/h) está dentro del rango recomendado. Esta observación del TM N2 puede considerarse cerrada con nota.

**NOTA — Orientación boquillas:** BW Water informa que la orientación de las boquillas fue modificada. Esto requiere actualización del isométrico/layout de piping para reflejar la nueva orientación. Confirmar que P&ID no requiere revisión.

**Veredicto Cartridge Filter Rev C: 2 — Approved as Noted**
*(12 cartuchos justificados; confirmar actualización de isométrico por cambio de orientación de boquillas)*

---

## 7. Static Mixer Rev B (P22-ET-09-009-012)

### Datos Rev B

- **Fabricante:** N-Spindle, Modelo NS11 80 100-750 A-I15 A-F
- **TAG:** MZE-09-001
- **Longitud:** 750 mm (aumentada)
- **DN:** 100, ANSI #150
- **Material:** FRP (casing y elementos)
- **Flujo:** 49.0 m3/h
- **Velocidad de mezcla:** 1.84 m/s (según fabricante)
- **Presión de diseño:** 4.5 bar
- **Número de Reynolds:** 205,084 (turbulento — buena mezcla)
- **CoV:** 0.05 (excelente uniformidad de mezcla)

### Hallazgos

**RESUELTO — Material FRP:** CCS respuesta OBS-01 indica "BW Water has revised and ensured compliance". FRP confirmado para body y elementos. ✓

**RESUELTO — L/D ratio:** Longitud aumentada a 750 mm. ✓

**PENDIENTE — TAG MZE-09-001 vs P&ID:** El datasheet usa TAG MZE-09-001. La revisión TM N3 señaló posible discrepancia con MZE-09-009 en P&ID. No hay evidencia en E13 de que esto haya sido resuelto. Requiere verificación cruzada con P&ID actualizado.

**PENDIENTE — Velocidad (velocimetría):** BW Water solicita clarificación del método de cálculo de ADASA (0.17 vs 0.59 m/s). El fabricante calcula 1.84 m/s. Esta discrepancia necesita ser resuelta formalmente — aparentemente ADASA calculó la velocidad en la tubería, no en el mixer. La velocidad de mezcla del fabricante (1.84 m/s) es correcta para el sizing del mixer pero diferentes secciones tienen diferentes velocidades.

**Veredicto Static Mixer Rev B: 2 — Approved as Noted**
*(FRP y L/D resueltos; TAG MZE-09-001 requiere verificación vs P&ID; velocidad a aclarar en respuesta a BWW)*

---

## CCS Cartridge Filter y Static Mixer

Los documentos CCS corresponden a los Consolidated Comment Sheets del vendedor (respuestas a comentarios de ADASA de revisiones previas). Confirman:
- Cartridge Filter: flujo 4.08 m3/h/cartucho dentro del rango del fabricante; orientación de boquillas modificada
- Static Mixer: FRP confirmado, longitud aumentada, velocidad a aclarar

---

## 8. Resumen de Veredictos

| # | Documento | Rev | Veredicto | Observaciones abiertas |
|---|-----------|-----|-----------|----------------------|
| 1 | Utility Consumption List | B | **2 — Approved as Noted** | Cálculo térmico A/C pendiente |
| 2 | Valve List | B | **3 — To be Revised** | TAGs duplicados OBS-02, OBS-03, OBS-07, OBS-08 |
| 3 | HP Pump Datasheet | C | **2 — Approved as Noted** | Nota clarificación potencias |
| 4 | Feed Turbocharger | C | **4 — Rejected** | Coupling 1200 psi rechazado (margen 1.19x < ASME 1.5x); cambio clase producto; datasheet coupling no entregado |
| 5 | Interstage Turbocharger | C | **2 — Approved as Noted** | Coupling 1800 psi marginal; datasheet coupling no entregado (condición Code 2); vibration mounting |
| 6 | Cartridge Filter | C | **2 — Approved as Noted** | Actualizar isométrico por boquillas |
| 7 | Static Mixer | B | **2 — Approved as Noted** | TAG vs P&ID; velocidad a aclarar |

**Veredicto General E13 (25007-0013): 4 — REJECTED**
*(Valve List Rev B y Feed Turbocharger Rev C rechazados; coupling datasheets pendientes en ambos turbochargers)*

---

## 9. Observaciones Pendientes de TM N2–N5 (No Abordadas en E13)

| Obs | Origen | Descripción | Días abierta (al 27-Feb) | En E13 |
|-----|--------|-------------|--------------------------|--------|
| TM N2 | Modbus TCP Memory Map | No entregado | 51 | NO |
| TM N2 | A/C thermal calculation | No entregado | 51 | NO (solo referenciado) |
| TM N3 | IO List coordination signals | No entregado/revisado | 30 | NO |
| TM N4 | UPS no incluida en BOM | No respondido | 22 | NO |
| TM N5 | Footprint CIP externo (Layout) | No entregado | 4 | NO |

---

*Revisión preparada por Luis Rivera — 27-Feb-2026*
