# TM N18 — Análisis de Trabajo (INTERNO, NO ENVIAR)

Submittals: 25007-0038 (E38), 25007-0039 (E39), 25007-0040 (E40), 25007-0041 (E41)
Fecha análisis: 18-May-2026

> **DISPOSICIÓN FINAL (re-disposición 18-May, criterio ejecutivo Code 1/2 — esto prevalece sobre las tablas de veredictos más abajo, que son historia del análisis):**
> El código refleja el documento revisado en sí; si no requiere modificación a sí mismo → Code 1, y los entregables sobre otros documentos/análisis separados se trackean en Sección 3.
> - Plant Control Philosophy Rev C = **Code 3** (driver único; OBS-01 CRITICAL repetido + OBS-02 child docs).
> - Valve List Rev D = **Code 1** (tabla intacta; PSV-09-002 análisis → Sección 3).
> - Line List Rev C = **Code 1**.
> - AC Thermal Calc Rev C = **Code 1** (verificado verbatim sin error: carga 6.24 kW=1.774 TR, margen 2.04, unidad 2.01 TR +13.3% sobre peak, n+1 ok; solo indicar margen explícito → Sección 3).
> - P&ID Rev D = **Code 1** (plano as-is; CIT-09-004 → Instrument/Line List + nota; dual-value → Sección 3).
> Tally final: **4 Code 1 + 0 Code 2 + 1 Code 3**. Global 3 — TO BE REVISED (sin cambio). 1 CC_ADASA emitido (Control Philosophy Code 3); 4 Code 1 sin CC_ADASA (CLAUDE.md sección 3.8), scripts/PDFs traza interna. Regla en CLAUDE.md secciones 6.2/6.3 v6.11.

---

## E39 — Plant Control Philosophy Rev C (P22-BT-09-009-001) — VEREDICTO: 3 — TO BE REVISED

Responde a TM N15 Section 2.10 (NOTE-13..NOTE-29, 17 hallazgos, 1 CRITICAL).
E39 entrega SOLO el Control Philosophy — NO se entregó Sequence Chart ni Alarm & Control Setpoint List
(referidos como "SEPARATE DOCUMENT" en pág. ~22, líneas 405-418). CCS ahora presente (59 págs vs 51/53).

### Verificación hallazgo por hallazgo vs TM N15 §2.10

| Origen TM N15 | Severidad | Estado en Rev C | Evidencia |
|---|---|---|---|
| NOTE-13 SEC vs Offer Rev1 | MAJOR | **PARCIAL — abierto** | Aclara naturaleza (target, no setpoint, líneas 524-525) pero mantiene 4.8/5.0 kWh/m³ en dos bandas TDS (líneas 516-517), diverge de Offer Rev1 (single 4.71 ±5%, sin bandas) |
| NOTE-14 vibración numérica | MAJOR | **CERRADO** | 4.5 mm/s RMS alarm / 7.1 mm/s RMS trip, ISO 10816-3 (CCS #15, línea 221) |
| NOTE-15 antiscalant ratio source | MAJOR | **CERRADO** | FIT-09-001 = cartridge filter discharge, alineado P&ID/IO List (CCS #12 línea 189; líneas 1228, 1295-1296) |
| NOTE-16 VE-09-002 algoritmo | MAJOR | **PARCIAL — abierto** | Define PID (PV=PIT-09-005, MV=VE-09-002) pero "to submit along with sequence chart" (CCS #15 línea 220) — chart no entregado |
| NOTE-17 secuencia válvulas CIP | MAJOR | **ABIERTO** | "To submit along with sequence chart (May 13 - Tentative)" (CCS #17 línea 251) — no entregado |
| NOTE-18 motor RTD thresholds | MINOR | **CERRADO** | Winding 130/155 °C, bearing 80/95 °C, IEC 60034-1 (CCS #15 línea 221) |
| NOTE-19 turbo isolation status | MINOR | **CERRADO** | SIP-09-001 pasivo, sin válvula aislamiento dedicada, clarificado (CCS #13 línea 204) |
| **NOTE-20 HP Pump permissive** | **CRITICAL** | **NO CERRADO — REPITE CRITICAL** | Línea 1692: "Turbocharger isolation valve **VE-09-007 and VE-09-007** AVAILABLE" (TAG duplicado SIN corregir a VE-09-008). Línea 1703: "**VE-09-014 is fully CLOSED**" permanece en el permissive de arranque HP Pump. VE-09-014 = válvula entrada estanque antiescalante (línea 1231, 1303: abre para llenado por bajo nivel). El PLC, literal, bloquea arranque HP Pump cada vez que el estanque se rellena. Segundo TM consecutivo con el mismo defecto. |
| NOTE-21 FIT-09-001 reuso Stage 2 | MAJOR | **CERRADO** | "Permeate flow is measured by FIT-09-002, all related sections aligned" (CCS #18 línea 252); FIT-09-001 ahora consistente feed-side |
| NOTE-22 fórmula salt rejection | MAJOR | **ABIERTO** | "To submit and align along with sequence chart (May 13 - Tentative)" (CCS #20 línea 268) — fórmula no corregida en cuerpo |
| NOTE-23 TAGs huérfanos | MAJOR | **CERRADO** | TE-09-005 ahora en tabla grupo CIP (línea 1977 "CIP Heater High-Temperature Protection Element") y descrito (línea 2035); VE-09-006 en tabla (1385) y descrito (1542); VE-09-008 en tabla CIP (1970). Los 3 TAGs restaurados |
| NOTE-24 child docs sin compromiso | MAJOR | **ABIERTO — agravado** | Sequence Chart + Alarm & Control Setpoint List siguen "SEPARATE DOCUMENT" (líneas 405-418); fecha tentativa 13-May vencida (hoy 18-May), no entregados con E39; sin códigos/revisiones formales |
| NOTE-25 SEC bus eléctrico | MAJOR | **NO CERRADO** | Líneas 503-510: "Total Energy Consumed (kWh) (Parameter from RO PLC panel power meter)". Mantiene el medidor del panel PLC (mide PLC+UPS+control gear, NO el motor HP Pump ~85 kW). Solo añade aserción verbal "represents total RO system energy"; no reubica al MCC main breaker ni lista medidores sumados |
| NOTE-26 red SPoF/gateway | MAJOR | **PARCIAL** | CCS #11 (línea 173) define fault response de switches, gateway timeout "last state", heartbeat monitoring; declara HW redundancy "Not applicable". Respuesta sustantiva — evaluar si suficiente o NOTE residual |
| NOTE-27 3 requisitos ET | MAJOR | **PARCIAL** | CCS #10 (línea 158): (1) modo local por selector en LCP con PLC off; (2) VFD ramp 0.1-0.3 Hz/s preliminar; (3) low-P rupture detection con delay/fallback. Valores preliminares "fine-tuned during commissioning" — verificar setpoints numéricos en cuerpo |
| NOTE-28 off-spec interlock + turbo bypass | MAJOR | **ABIERTO** | "To submit and align along with sequence chart" + descripción genérica position-confirmation (CCS #19 línea 267) — lógica no implementada en cuerpo, diferida a chart no entregado |
| NOTE-29 calidad documental | MINOR | **PARCIAL — CERRADO mayor parte** | CCS ahora incluido; tag formats amended (CCS #9 línea 143). Persisten: doble fila "11" en tabla grupo (VE-09-006 línea 1385 / VE-09-007 línea 1386); VE-09-007 descrito inconsistente como "Turbocharger Isolation" (1386) y "Interstage Isolation" (1969) |

### Resumen E39
- **1 CRITICAL repetido sin cerrar (NOTE-20)** — driver del veredicto, escalable (2º TM consecutivo).
- 3 MAJOR no cerrados (NOTE-22, NOTE-24, NOTE-28) + 2 MAJOR parciales abiertos (NOTE-13, NOTE-16).
- NOTE-25 MAJOR respuesta no-conforme (mantiene bus incorrecto).
- Cerrados: NOTE-14, 15, 18, 19, 21 + mayor parte NOTE-29.
- Patrón: lógica de control núcleo (secuencias, setpoints, fórmula rejection, interlocks) diferida sistemáticamente a Sequence Chart + Setpoint List NO entregados; fecha tentativa 13-May vencida.

---

## E38 — Valve List Rev D (P22-LI-09-005-002) — VEREDICTO: 2 — APPROVED AS NOTED

**Es el MISMO Rev D (tabla fechada 18-Mar-26, 111 ítems) que TM N14 §2.2 ya revisó Code 2.**
Re-emitido bajo submittal 25007-0038 con un CCS (fechado 27-Abr-26) que responde a TM N14.
La tabla de válvulas no cambió — extracción texto/OCR triplica glifos (artefacto de render del PDF
BW Water), pero el contenido sustantivo ya fue verificado en TM N14 (TAG uniqueness 111 ítems vs P&ID Rev C vía PyMuPDF).

CCS — respuestas a TM N14:
- **TM N14 NOTE-01 (Item 112 removido, 112→111):** BW aclara que los duplicados Rev C eliminados
  fueron Ítems 44 y 64. Aclaración administrativa — **aceptada**.
- **Acción PSV-09-002 (TM N14):** ADASA pidió análisis de protección sobrepresión confirmando que
  la configuración PSV restante es adecuada, O reinstalar con TAG único. BW responde solo
  "PSV-09-002 is already included in Revision C under Item 104". **No responde a lo solicitado** —
  confirma existencia de un PSV pero NO demuestra adecuación de protección sobrepresión tras
  remover el segundo PSV-09-002. Ítem de seguridad (sistema HP ~80-90 bar).

Disposición: tabla de válvulas se mantiene Code 2 (heredado TM N14, sin cambios). Notas TM N18:
- NOTE (MAJOR): análisis de adecuación de protección de sobrepresión para el segundo PSV-09-002
  removido — solicitado en TM N14 — sigue sin entregarse. Requerido antes de IFC Rev 0.
- NOTE (MINOR): irregularidad de control de revisiones — respuesta a comentarios de transmittal
  vía CCS re-emitiendo el mismo Rev D en vez de avanzar revisión o llevar a IFC Rev 0.

## E38 — Line List Rev C (P22-LI-09-009-003) — VEREDICTO: 1 — APPROVED

Rev C fechado 5-May-26. CCS responde a TM N12:
- **TM N12 NOTE-01 (línea "MAKE-UP FOR CIP" sin LINE NO.):** asignada PE-PVC-DN80-09-019.
  "BW has revised accordingly." **CERRADO.**
- **TM N12 NOTE-02 (designación SCH 80S):** todas las líneas Super Duplex ahora
  "SUPER DUPLEX STEEL, SCH80S" (líneas 32-59 del cuerpo); PVC mantiene SCH 80 (correcto).
  "BW has revised accordingly." **CERRADO** (era tracked-for-IFC; corregido anticipadamente en Rev C).
- Presiones consistentes (DA-SSD-DN80-09-005 op 68 / diseño 80, margen 17.6%). HP Super Duplex
  SCH80S, baja presión PVC SCH80. Sin hallazgos nuevos.

Disposición: ambas notas TM N12 cerradas, sin observaciones nuevas → **Code 1 — Approved**
(NO anotar PDF, sin CC_ADASA per CLAUDE.md §3.8).

## E40 — AC Thermal Calculation Rev C (P22-CD-09-005-002) — VEREDICTO: 2 — APPROVED AS NOTED

**Mismo Rev C** que TM N15 §2.2 ya revisó Code 2 (cerró TM N2 OBS-02, 180+ días). Cálculo sin
cambios (peak 1.774 TR × 15% margen = 2.04 TR; unidad 2.5 HP = 2.01 TR). Re-emitido bajo submittal
25007-0040 con CCS que responde a TM N15 NOTE-02:

- **CCS Row 1 → TM N15 NOTE-02 (déficit margen 0.03 TR):** BW justifica que 2.01 vs 2.04 TR es
  −0.03 TR (~1.5%), "within acceptable engineering tolerance / within the applied design margin".
  Redacción imprecisa (el 0.03 TR ES la erosión del margen, no "dentro" de él) pero la conclusión
  técnica se sostiene: la unidad supera el peak NO-margenado (1.774 TR) en +13.3% → margen efectivo
  positivo. Aceptable como resolución de nota Code 2.
- **CCS Row 2 → TM N15 NOTE-02 (n+1):** "Confirmed. Each 2.5 HP unit can carry 100% load"
  (1 Duty + 1 Standby). **n+1 CONFIRMADO — CERRADO.**

Disposición: cálculo inalterado (Code 2 heredado TM N15); n+1 cerrado; margen justificado.
→ **Code 2 — Approved as Noted**, NOTE-01: n+1 aceptado; recomendar que IFC Rev 0 declare
explícitamente el margen efectivo post-selección (2.01 TR vs peak 1.774 TR = +13.3%) para
trazabilidad del design basis, en lugar de la redacción imprecisa "within the applied design
margin". Cierra TM N15 NOTE-02 (degradada a clarificación documental para IFC).

---

## VEREDICTOS CONSOLIDADOS TM N18

| Doc | Submittal | Rev | Veredicto |
|-----|-----------|-----|-----------|
| Plant Control Philosophy | 25007-0039 | C | **3 — To be revised** |
| Valve List | 25007-0038 | D | 2 — Approved as Noted |
| Line List | 25007-0038 | C | 1 — Approved |
| AC Thermal Calculation | 25007-0040 | C | 2 — Approved as Noted |

Tally: 1 Code 1 + 2 Code 2 + 1 Code 3 → **VEREDICTO GLOBAL TM N18: 3 — TO BE REVISED**
(driver: Control Philosophy Rev C, CRITICAL NOTE-20 repetido sin cerrar).

Cierres logrados por TM N18:
- TM N12 NOTE-01 (Line List línea sin ID) — CERRADO por Line List Rev C
- TM N12 NOTE-02 (SCH 80S) — CERRADO por Line List Rev C (era tracked-for-IFC)
- TM N15 NOTE-02 (AC Thermal n+1 + margen) — CERRADO por AC Thermal Rev C CCS
- TM N15 §2.10 parcial: NOTE-14/15/18/19/21/23 + mayor parte NOTE-29 — CERRADOS por Control Philosophy Rev C

Siguen abiertos (heredados, no cubiertos): TM N4 OBS-06/07 + NOTE-05 (Cable Tray/HMI),
TM N15 LCP Rev A, TM N15 Cable Tray Rev B→C, TM N5 OBS-02, TM N10 OBS-05, TM N11 OBS-03,
TM N13 NOTE-02, TM N16 NOTE-01 (tracked IFC).

## E41 — Piping & Instrumentation Diagram Rev D (P22-DWG-09-009-002) — VEREDICTO: 2 — APPROVED AS NOTED

Re-escopeo TM N18 (correo aún BORRADOR): submittals pasan a 25007-0038..0041, 5 docs.
P&ID Rev D fechado 12-May-2026 (rev block A 13/11/25, B 04/03/26, C 27/03/26, D 12/05/26).
Historial: Rev B (TM N9 Code 2), Rev C (TM N13 Code 2, NOTE-01 abierta CIP Tank 6.81 vs 6.1).

CCS Rev D (5 comentarios):
1-2-4. BW-initiated: diaphragm seals para pressure gauges; area limits del container;
   manhole size CIP Tank. Mejoras/clarificaciones, sin objeción.
3. BW-initiated: cambio de tapping de CIT-09-004 — añade orifice plate + needle valve
   para bajar presión y proteger el sensor del analizador de conductividad. Cambio de
   instalación de instrumento sensato pero NO solicitado por ADASA.
5. **Responde TM N13 NOTE-01** (CIP Tank TK-09-001 6.81 vs 6.1 m³): BW aclara que son
   dos valores — total (6.8 m³, dimensiones del estanque) y efectivo/usable (6.1 m³,
   el del Equipment List). Antiscalant Tank: total 0.34 / efectivo 0.27. Revisaron el
   P&ID para mostrar AMBOS valores. Cuerpo confirma anotación dual (líneas 1151-1155
   "6.81 ... 6.1"; 1242 "0.34"). **TM N13 NOTE-01 CERRADO** — justificación técnica
   válida (total geométrico vs volumen de trabajo bajo rebalse; físicamente consistente
   para HDPE 1800 mmØ × 2950 mm H) y P&ID actualizado; no requiere Equipment List Rev C
   porque el valor del Equipment List (6.1 efectivo) siempre fue correcto.

Disposición: cierra la única observación ADASA abierta del P&ID (era MINOR/tracked-IFC),
sin ítems rejected/requires-revision. NOTE-01 (MINOR) sobre el cambio BW-initiated de
tapping de CIT-09-004: confirmar que está reflejado consistentemente en Instrument List
Rev D y Line List Rev C, y que la reducción de presión (orificio + aguja) no introduce
lag/dead-leg que afecte el indicador interstage de salt rejection que usa CIT-09-004
(relacionado con OBS-03). → **Code 2 — Approved as Noted**.

Nota extracción: P&ID es plano — texto del dibujo disperso (single-char vertical, esperado
[[feedback_doc_annotator_pid]]); CCS y revision block extrajeron limpios (base de verdad
para esta disposición). Cross-check de TAGs valvula/instrumento en el dibujo no posible
desde texto degradado; el defecto del permissive es del Control Philosophy (OBS-01), no
del P&ID. P&ID = autoridad que BW debe reconciliar → refs "P&ID Rev C" del TM N18 pasan
a "P&ID Rev D".

### VEREDICTOS CONSOLIDADOS TM N18 (RE-ESCOPEADO, 5 docs)
| Doc | Submittal | Rev | Veredicto |
|-----|-----------|-----|-----------|
| Plant Control Philosophy | 25007-0039 | C | **3 — To be revised** |
| Valve List | 25007-0038 | D | 2 — Approved as Noted |
| Line List | 25007-0038 | C | 1 — Approved |
| AC Thermal Calculation | 25007-0040 | C | 2 — Approved as Noted |
| Piping & Instrumentation Diagram | 25007-0041 | D | 2 — Approved as Noted |

Tally: 1 Code 1 + 3 Code 2 + 1 Code 3 → **VEREDICTO GLOBAL: 3 — TO BE REVISED** (sin cambio;
driver Control Philosophy Rev C). Cierres añadidos: **TM N13 NOTE-01** (P&ID Rev D) — la
lista "Tracked for IFC Rev 0" queda vacía. Van Doorn: P&ID es área 09 BW Water — sin
segregación (igual criterio que el resto de TM N18).

---

## Regla Van Doorn (CLAUDE.md §3.7)

Los 4 documentos de TM N18 son scope área 09 BW Water (Control Philosophy, Valve List,
Line List, AC Thermal Calc). Van Doorn = asesor interno área 06 (proceso/mecánica
perimetral). No hay insumo Van Doorn ni omisión de entregable área 06 identificada en
este transmittal — sin contenido a segregar para versión interna. Este archivo
`_ANALISIS_TRABAJO.md` es el documento interno (NO ENVIAR); el oficial es
`P22-TM-09-000-018-0_TRANSMITTAL.md` (inglés, BW Water).

## Adjuntos CC_ADASA por veredicto (§3.8)
- Control Philosophy Rev C — Code 3 → anotar todas: OBS-01/02/03 + NOTE-01/02/03
- Valve List Rev D — Code 2 → anotar NOTEs: NOTE-01, NOTE-02
- AC Thermal Calc Rev C — Code 2 → anotar NOTE: NOTE-01
- Line List Rev C — Code 1 → NO anotar, sin CC_ADASA
