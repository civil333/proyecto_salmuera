---
titulo: "Alertas Procurement vs. Ingeniería No Aprobada"
codigo: "INTERNO-ADASA"
fecha: "10-Mar-2026"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
fuentes:
  - "PROGRAMA y CONTRATO/estado_compras_09-03-26.md (Baseline Schedule BW Water Mar-2026)"
  - "P22-TM-09-000-006-0 (TM N6, 27-Feb-2026)"
  - "P22-TM-09-000-007-0 (TM N7, 08-Mar-2026)"
  - "P22-TM-09-000-008-0 (TM N8, 09-Mar-2026)"
  - "P22-IT-06-000-002-0 Master Deliverable Register"
---

# Alertas Procurement vs. Ingeniería No Aprobada
## Cruce Baseline Schedule BW Water (Mar-2026) × Estado Revisión ADASA

**Fecha del análisis:** 10-Mar-2026
**Propósito:** Identificar equipos con PR/PO programada pero con ingeniería rechazada, en revisión, u observaciones abiertas bloqueantes. Uso interno ADASA — no enviar a BW Water.

---

## 1. Semáforo Consolidado

| # | Equipo | PO Inicio | PO Fin | Mfg. Termina | Documento Técnico | Rev | Veredicto | Riesgo |
|---|--------|-----------|--------|--------------|-------------------|-----|-----------|--------|
| 1 | RO Membrane | 24/02/2026 | 02/03/2026 | 03/08/2026 | UHPRO System DS | — | Code 1 — Approved | ✅ VERDE |
| 2 | RO High Feed Pump | 04/03/2026 | 10/03/2026 | 28/07/2026 | DS HP Feed Pump | Rev C | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 3 | **Instrument Set** | **11/03/2026** | **17/03/2026** | **09/07/2026** | **Instrument List / IO List** | **Rev B / Rev A** | **Code 3 — To be Revised / Sin actualizar** | **🔴 ROJO** |
| 4 | **All Valve** | **11/03/2026** | **17/03/2026** | **09/07/2026** | **Valve List** | **Rev B** | **Code 4 — REJECTED** | **🔴 ROJO CRÍTICO** |
| 5 | CIP Heater | 16/03/2026 | 20/03/2026 | 29/05/2026 | DS CIP Heater | — | Code 1 — Approved | ✅ VERDE |
| 6 | Container | 18/03/2026 | 24/03/2026 | 28/04/2026 | DS RO Container | — | Code 1 — Approved | ✅ VERDE |
| 7 | CIP/Flushing Cartridge Filter | 23/03/2026 | 27/03/2026 | 05/06/2026 | DS Cartridge Filter | Rev C | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 8 | CIP/Flushing Pumps | 25/03/2026 | 31/03/2026 | 21/07/2026 | DS CIP Pump | Rev B | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 9 | CIP/Flushing Tank | 27/03/2026 | 02/04/2026 | 28/05/2026 | DS CIP Tank | — | Code 1 — Approved | ✅ VERDE |
| 10 | **RO Pressure Vessel/Tubes** | **31/03/2026** | **06/04/2026** | **15/06/2026** | **Sin datasheet entregado** | **—** | **No revisado** | **🟠 NARANJA** |
| 11 | **Feed Turbocharger** | **01/04/2026** | **07/04/2026** | **02/06/2026** | **DS Feed Turbocharger** | **Rev C** | **Code 4 — REJECTED** | **🔴 ROJO CRÍTICO** |
| 12 | **Structural Frames/Supports** | **06/04/2026** | **10/04/2026** | **05/05/2026** | **Sin datasheet entregado** | **—** | **No revisado** | **🟠 NARANJA** |
| 13 | Antiscalant Dosing Tank | 07/04/2026 | 13/04/2026 | 25/05/2026 | DS Antiscalant Tank | — | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 14 | Antiscalant Dosing Pumps | 10/04/2026 | 16/04/2026 | 25/06/2026 | DS Antiscalant Pump | — | Code 1 — Approved | ✅ VERDE |
| 15 | Interstage Turbocharger | 24/04/2026 | 30/04/2026 | 25/06/2026 | DS Interstage TC | Rev C | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 16 | Static Mixer | 01/05/2026 | 07/05/2026 | 04/06/2026 | DS Static Mixer | Rev B | Code 2 — Appr. as Noted | 🟡 AMARILLO |
| 17 | RO Cartridge Filter | 04/05/2026 | 08/05/2026 | 17/07/2026 | DS RO Cartridge Filter | Rev C | Code 2 — Appr. as Noted | 🟡 AMARILLO |

**Resumen de riesgos:**

| Nivel | Equipos afectados | PO más urgente |
|-------|-------------------|----------------|
| 🔴 ROJO CRÍTICO (Code 4) | All Valve, Feed Turbocharger | 11-Mar-2026 |
| 🔴 ROJO (Code 3 bloqueante) | Instrument Set + IO List | 11-Mar-2026 |
| 🟠 NARANJA (sin DS) | RO Pressure Vessel, Structural Frames | 31-Mar-2026 |
| 🟡 AMARILLO (Code 2 con obs) | HP Pump, CIP Cart. Filter, CIP Pumps, Antiscalant Tank, Interstage TC, Static Mixer, RO Cart. Filter | 10-Mar-2026 |
| ✅ VERDE (aprobado) | RO Membrane, CIP Heater, Container, CIP Tank, Antiscalant Pumps | — |

---

## 2. Alertas Críticas 🔴

### 🔴 ALL VALVE — ALERTA CRÍTICA (Code 4 — Rejected)

| Campo | Valor |
|-------|-------|
| PO Programada | 11-Mar-2026 (inicia en 1 día) |
| PO Cierra | 17-Mar-2026 |
| Manufactura termina | 09-Jul-2026 |
| Documento | P22-LI-09-005-002 — Valve List |
| Revisión revisada | Rev B |
| Veredicto ADASA | Code 4 — REJECTED (TM N6, 27-Feb-2026) |
| Días hasta PO | **1 día** |

**Observaciones bloqueantes que causan el rechazo:**

- **OBS-02 — Duplicate TAG VM-09-015 (CRITICAL):** Ítem 18 (DN100, Mariposa, ON/OFF MOTORIZED) e ítem 43 (DN15, Ball, MANUAL) comparten el mismo TAG. BW Water declaró en su CCS "Already revised on Valve List Rev. B" — la corrección no fue implementada. La declaración de conformidad no coincide con el documento entregado.
- **OBS-03 — Duplicate TAG VE-09-008 (CRITICAL):** Ítem 44 (DN80, ANSI 900#, CE3MN) e ítem 57 (DN80, ANSI 150#, DI/SS420) comparten el mismo TAG. Mismo escenario: declarado como corregido en CCS, no implementado en Rev B.
- **OBS-04 — Duplicate TAG VE-09-009 (CRITICAL — NUEVO EN REV B):** Ítem 58 (DN80, ANSI 900#) e ítem 93 (DN25, ANSI 150#). Duplicado introducido en Rev B que no existía en Rev A.
- **OBS-05 — Duplicate TAG VM-09-065 (MAJOR — NUEVO EN REV B):** Ítem 30 (DN65, Mariposa) e ítem 76 (DN150, Mariposa). Duplicado introducido en Rev B.

**Impacto:** TAGs duplicados impiden identificación unívoca de válvulas en el PLC. Falla QA grave: una declaración CCS de conformidad que no corresponde al documento entregado es inadmisible. BW Water no puede completar la PO de All Valve con la lista en Code 4.

**Condición para levantar el bloqueo:** BW Water debe entregar Valve List Rev C con los cuatro TAGs duplicados corregidos (VM-09-015, VE-09-008, VE-09-009, VM-09-065) y realizar una revisión sistemática de unicidad de TAGs en toda la lista.

---

### 🔴 INSTRUMENT SET — ALERTA CRÍTICA (Code 3 + IO List sin actualizar)

| Campo | Valor |
|-------|-------|
| PO Programada | 11-Mar-2026 (inicia en 1 día) |
| PO Cierra | 17-Mar-2026 |
| Manufactura termina | 09-Jul-2026 |
| Documento principal | P22-LI-09-008-003 — Instrument List |
| Revisión revisada | Rev B |
| Veredicto ADASA — IL | Code 3 — To be Revised (TM N8, 09-Mar-2026) |
| Documento secundario | IO List Rev A (sin actualizar desde TM N3) |
| Veredicto ADASA — IO List | Pendiente — 45 días sin revisión |
| Días hasta PO | **1 día** |

**Observaciones bloqueantes:**

- **OBS-IL-1 — CIT-09-005 suministro 120VAC vs. bus de instrumentación 24VDC (MAYOR):** El ítem 25 (Conductividad RO Train Reject, Rosemount 228/1056) especifica 120VAC. Todos los demás instrumentos del listado operan a 24VDC. 120VAC no es una tensión definida en el proyecto (ET define 380VAC/220VAC como suministro AC; 24VDC como bus de instrumentación). BW Water debe aclarar si es un error tipográfico o una decisión de diseño deliberada. Si es deliberada, debe documentar la justificación y la fuente de suministro.
- **OBS-IL-2 — Rangos de conductividad insuficientes para salmuera brine (MAYOR):** CIT-09-001 (Feed), CIT-09-004 (Stage 1 Reject) y CIT-09-005 (Train Reject) especifican rango máximo de 20 mS/cm. El TDS de diseño de la salmuera (43,000–53,000 mg/L per ET) corresponde a conductividades esperadas de 65–80 mS/cm en feed y 80–140 mS/cm en rechazo. Con el rango actual, los tres transmisores operarían en saturación (>20 mA) durante operación normal, sin entregar datos útiles de proceso.
- **OBS-IO-1 — IO List no actualizada desde TM N3 (45 días):** Rev B del Instrument List agrega 7 nuevos puntos de instrumentación (VT-09-001/002/003, TE-09-001/002/003/004) que no están en el IO List Rev A. Sin IO List actualizado, no es posible completar la asignación de canales PLC ni planificar loop checks. Este bloqueo impacta directamente el FAT (25-Jul-2026).

**Condición para levantar el bloqueo:** (1) Instrument List Rev C aclarando CIT-09-005 (120VAC o 24VDC con justificación) y confirmando rangos de conductividad con datos de medición de la salmuera Taltal. (2) IO List Rev B incorporando los 7 puntos nuevos de Rev B y los cambios de TAG (FIT-09-002, LIT-09-002).

---

### 🔴 FEED TURBOCHARGER — ALERTA CRÍTICA (Code 4 — Rejected)

| Campo | Valor |
|-------|-------|
| PO Programada | 01-Abr-2026 |
| PO Cierra | 07-Abr-2026 |
| Manufactura termina | 02-Jun-2026 |
| Documento | P22-ET-09-009-007 — DS Feed Turbocharger (SIP-09-001, FEDCO HPB-60) |
| Revisión revisada | Rev C |
| Veredicto ADASA | Code 4 — REJECTED (TM N6, 27-Feb-2026) |
| Días hasta PO | 22 días |

**Observación bloqueante:**

- **OBS-01 — Coupling presión: 1,200 psi en Rev C vs. 2,000 psi contractual (CRÍTICO):** BW Water redujo unilateralmente el rating del coupling HP del Feed Turbocharger de 2,000 psi (Rev B, baseline contractual confirmado en Technical Proposal Rev1) a 1,200 psi (82.7 bar), citando desabastecimiento ("out of stock"). El rechazo se funda en cuatro argumentos técnicos y contractuales:
  1. **Margen de seguridad insuficiente:** 1,200 psi entrega un margen de 1.19× sobre la presión de operación (69.53 bar) — inferior al mínimo aceptable para servicio de salmuera concentrada de alta presión.
  2. **El coupling propuesto cae físicamente bajo la presión de operación en los joints 2° etapa UHPRO** (83.9 bar > 82.7 bar): si esta política se aplicara en todos los joints, el coupling fallaría en condiciones de diseño normales.
  3. **Cambio de clase de producto:** 2,000 psi = Piedmont Pacific Style H (certificado para HPB Energy Recovery). 1,200 psi = Piedmont Style D (RO estándar). No es sustitución equivalente.
  4. **Incumplimiento de compromiso formal:** En CCS de Submittal 25007-0002 (22-Ene-2026), BW Water declaró explícitamente: *"BW will provide coupling rated 2000 psi."* Esta declaración aplica a SIP-09-001 y SIP-09-002. Rev C viola el compromiso formal sin aprobación de ADASA.

**Condición para levantar el bloqueo:** ADASA ha confirmado una vía técnica aceptable: coupling ≥ 1,800 psi **más** entrega del datasheet del fabricante del coupling (modelo, MAWP, certificación servicio HPB) para ambos turbochargers (SIP-09-001 y SIP-09-002). La solución preferida de ADASA sigue siendo el retorno a 2,000 psi (Piedmont Style H). Adicionalmente, BW Water debe confirmar si el HPB-60 entregado es el modelo Standard (MAWP 83 bar) o Ultra (MAWP 124 bar), y confirmar compatibilidad a largo plazo de los O-rings internos FEDCO (Buna N) con salmuera 53,000 ppm TDS.

---

## 3. Alertas Mayores 🟠 (Sin Datasheet Entregado)

### 🟠 RO PRESSURE VESSEL / TUBES — Sin datasheet entregado

| Campo | Valor |
|-------|-------|
| PO Programada | 31-Mar-2026 |
| PO Cierra | 06-Abr-2026 |
| Manufactura termina | 15-Jun-2026 |
| Documento técnico | Sin datasheet específico entregado a la fecha |
| Veredicto ADASA | Sin revisión — documento no recibido |
| Días hasta PO | 21 días |

**Situación:** No existe datasheet de Pressure Vessel/Tubes revisado por ADASA en ninguno de los 8 transmittals emitidos. La PO abre en 21 días. BW Water debe entregar el documento con antelación suficiente para completar la revisión técnica antes del 30-Mar-2026. Sin documento aprobado, ADASA no puede validar que las especificaciones de los tubos de presión sean conformes con ET §5.1 (materiales, rating de presión) antes del cierre de compra.

**Acción requerida:** BW Water debe entregar el datasheet de RO Pressure Vessel/Tubes a la brevedad para permitir revisión técnica antes del 30-Mar-2026.

---

### 🟠 STRUCTURAL FRAMES / SUPPORTS — Sin datasheet entregado

| Campo | Valor |
|-------|-------|
| PO Programada | 06-Abr-2026 |
| PO Cierra | 10-Abr-2026 |
| Manufactura termina | 05-May-2026 |
| Documento técnico | Sin datasheet estructural entregado; Piping Layout Rev A → Code 3 (TM N7) |
| Veredicto ADASA | Sin revisión estructural; layout que define la estructura en Code 3 |
| Días hasta PO | 27 días |

**Situación:** El Piping Layout Rev A (P22-DWG-09-005-004), primer documento que entrega la disposición física del módulo, fue rechazado en TM N7 (Code 3) por incumplir la restricción de footprint externo CIP: el sistema CIP y el sistema de dosing están separados 11,150 mm (toda la longitud del módulo), superando en 3× el máximo de 3.5 m establecido en TM N5. Los marcos y soportes estructurales dependen directamente del layout aprobado. La PO de Structural Frames abre en 27 días, con una manufactura que termina el 05-May-2026 — ventana de fabricación de solo 25 días. Cualquier demora en aprobar el Piping Layout Rev B comprime directamente este calendario.

**Acción requerida:** BW Water debe entregar Piping Layout Rev B consolidando CIP y dosing en un único footprint externo ≤ container width × 3.5 m, alineado al lado indicado en el markup de TM N5. Solo después de aceptar el Piping Layout Rev B puede avanzar el diseño estructural.

---

## 4. Observaciones Abiertas (Código 2 — Equipos Amarillos) 🟡

Equipos con Code 2 — Approved as Noted. La PO puede avanzar, pero las observaciones abiertas deben resolverse antes del cierre de fabricación o del FAT. Se listan las que tienen carácter bloqueante para etapas posteriores.

| Equipo | Doc/Rev | Obs Abierta | Impacto si no se cierra |
|--------|---------|-------------|------------------------|
| RO High Feed Pump | DS Rev C | Nota de poder: diferenciar en datasheet entre nameplate (93 kW), potencia absorbida (78.5 kW) y referencias internas FEDCO (83/85 kW) | Riesgo de malinterpretación en revisiones de ingeniería eléctrica y MCC |
| CIP/Flushing Cartridge Filter | DS Rev C | Cambio de orientación de nozzle debe reflejarse en isométrico de cañería del container y en el layout | Inconsistencia piping / layout; potencial problema en pre-comisionamiento |
| Antiscalant Dosing Tank | DS (sin rev conocida) | Sujeto a respuesta a CT-001 (Consulta Técnica N°1) sin respuesta de BW Water | Si CT-001 cambia especificaciones del tank, el datasheet queda obsoleto |
| Interstage Turbocharger | DS Rev C | (1) Coupling 1,800 psi aceptado condicionalmente: FEDCO debe confirmar por escrito que MAWP real ≥ 1,845 psi bajo condiciones de servicio. (2) Datasheet de coupling no incluido — debe entregarse con próxima revisión. (3) Confirmación de montaje de sensor de vibración pendiente | Si FEDCO no confirma el MAWP, la aceptación condicional Code 2 se revierte |
| Static Mixer | DS Rev B | TAG discrepancia: datasheet indica MZE-09-001; P&ID muestra MZE-09-009. Debe resolverse en Rev C | Trazabilidad de TAG comprometida; conflicto en listados y loop sheets |
| RO Cartridge Filter | DS Rev C | Cambio de orientación de nozzle debe reflejarse en isométrico de cañería del container | Misma consecuencia que CIP Cartridge Filter |

> **Nota sobre CIP/Flushing Pumps:** El Code 2 no lleva observaciones bloqueantes identificadas en los transmittals; el riesgo amarillo se asigna por precaución dada la cercanía de la PO (25-Mar-2026) y la dependencia del Piping Layout aprobado para validar la ubicación final de las bombas.

---

## 5. Sin Riesgo — Ingeniería Aprobada ✅

| Equipo | PO Cerrada / Inicio | Doc Técnico | Rev | Veredicto |
|--------|---------------------|-------------|-----|-----------|
| RO Membrane | 24/02 – 02/03/2026 (**cerrado**) | UHPRO System DS | — | Code 1 — Approved |
| CIP Heater | 16/03/2026 | DS CIP Heater | — | Code 1 — Approved |
| Container | 18/03/2026 | DS RO Container | — | Code 1 — Approved |
| CIP/Flushing Tank | 27/03/2026 | DS CIP Tank | — | Code 1 — Approved |
| Antiscalant Dosing Pumps | 10/04/2026 | DS Antiscalant Pump | — | Code 1 — Approved |

Estos cinco equipos tienen su ingeniería aprobada sin condiciones. El procurement puede proceder sin restricciones técnicas desde ADASA.

---

## 6. Timeline Visual con Alertas

```
Mar-2026                         Abr-2026                     May-2026
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
10   14   18   22   26   30   03   07   11   15   19   23   27   01   05

PO EN CURSO / INMINENTES:
[🔄 HP Pump       ]10-Mar
[🔴 INSTR. SET    ]11-Mar ← ALERTA — Code 3 + IO List sin actualizar (1 día)
[🔴 ALL VALVE     ]11-Mar ← ALERTA — Code 4 REJECTED (1 día)
         [✅ CIP Heater   ]16-Mar
               [✅ Container     ]18-Mar
                    [🟡 CIP Cart.Flt ]23-Mar
                        [🟡 CIP Pumps   ]25-Mar
                             [✅ CIP Tank     ]27-Mar
                                  [🟠 PRESSURE VES]31-Mar ← Sin DS (21 días)
                                      [🔴 FEED TURBO  ]01-Abr ← Code 4 REJECTED (22 días)
                                           [🟠 STRUCT.FRAME]06-Abr ← Sin DS (27 días)
                                                [🟡 Antiscal.Tank]07-Abr
                                                    [✅ Antiscal.Pump]10-Abr

                                                                       [🟡 Interstage TC]24-Abr
                                                                            [🟡 Static Mixer ]01-May
                                                                                 [🟡 RO Cart.Flt ]04-May
```

**Hitos críticos del programa (referencia):**

| Hito | Fecha |
|------|-------|
| Último PR/PO (RO Cartridge Filter) | 04/05/2026 |
| Ingeniería completa | 09/07/2026 |
| FAT (Factory Acceptance Test) | 25/07 – 01/08/2026 |
| Shipping | 02/08/2026 |
| Comisionamiento en sitio | 18/09 – 08/10/2026 |

---

## 7. Condiciones de Cierre para Levantar Alertas

| Alerta | Condición mínima para levantar | Urgencia |
|--------|-------------------------------|----------|
| 🔴 All Valve | Valve List Rev C con 4 TAGs corregidos (VM-09-015, VE-09-008, VE-09-009, VM-09-065) + revisión sistemática de unicidad | **Inmediata — PO abre 11-Mar** |
| 🔴 Instrument Set — IL | Instrument List Rev C: CIT-09-005 aclarado (120VAC o 24VDC) + rangos conductividad confirmados con datos medición salmuera Taltal | **Inmediata — PO abre 11-Mar** |
| 🔴 Instrument Set — IO List | IO List Rev B incorporando 7 nuevos puntos de IL Rev B + correcciones de TAG | **Inmediata — bloquea FAT planning** |
| 🔴 Feed Turbocharger | DS Rev D con coupling ≥ 1,800 psi (mín. aceptable) o ≥ 2,000 psi (preferido ADASA) + datasheet fabricante coupling (MAWP, cert. HPB) para SIP-09-001 y SIP-09-002 | **Antes de 31-Mar — PO abre 01-Abr** |
| 🟠 RO Pressure Vessel | Entrega de datasheet + revisión técnica completada antes de 30-Mar | **Antes de 30-Mar** |
| 🟠 Structural Frames | Piping Layout Rev B aprobado (Code 1 o Code 2) como prerequisito | **Antes de 05-Abr** |
| 🟡 Interstage TC | Confirmación escrita FEDCO: MAWP coupling ≥ 1,845 psi + datasheet coupling | **Antes del FAT** |
| 🟡 Static Mixer | Aclaración TAG MZE-09-001 vs MZE-09-009 (Rev C) | **Antes del FAT** |
| 🟡 Cart. Filters (x2) | Reflejar cambio orientación nozzle en isométrico de cañería | **Antes del FAT** |

---

*Documento de uso interno ADASA — 10-Mar-2026*
*Fuentes: estado_compras_09-03-26.md, TM N6 (27-Feb-2026), TM N7 (08-Mar-2026), TM N8 (09-Mar-2026)*
