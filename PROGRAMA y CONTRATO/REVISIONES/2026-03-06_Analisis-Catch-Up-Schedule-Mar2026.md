# Análisis Catch-Up Schedule — BW Water 05-Mar-2026

**Fecha análisis:** 06 de marzo de 2026
**Documento interno ADASA — NO ENVIAR**
**Proyecto:** 12803 — Módulo de Salmuera Taltal
**Contrato:** C-4300
**Referencia:** `PROGRAMA y CONTRATO/05.03.26_12803_Taltal Water Treatment Plant.pdf`
**Análisis previo:** `REVISIONES/2026-02-10_Analisis-Comparativo-Programas-BW-Water.md`

---

## 1. Resumen Ejecutivo

BW Water presentó el 05-Mar-2026 un nuevo "Baseline Schedule" denominado "12803_Taltal Water Treatment Plant_Baseline Schedule", con fecha del documento 5/3/2026. La duración total declarada es de 290 días (07-Oct-2025 a 16-Nov-2026).

El schedule incorpora cuatro correcciones importantes respecto al programa de febrero-2026: reincorpora el FAT, la supervisión de comisionamiento, la capacitación de operadores y el close-out documental, y corrige el punto de entrega a EXW Malasia. En ese sentido, es más completo que su antecesor.

Sin embargo, introduce un agravamiento mayor: la fase de ingeniería "Equipment & Procurement Related" se extiende hasta el 09-Jul-2026, lo que representa 198 días totales de ingeniería frente a los 65 días de la línea base original (Oct-2025). Ese es un incremento del 205% sobre el compromiso contractual.

Adicionalmente, el schedule muestra la fase "General" de ingeniería (Civil, Proceso, Eléctrico, I&C, Mecánico) como completada el 20-Feb-2026, lo que no refleja la realidad del proyecto: hay al menos 15 documentos nunca entregados y 14 con observaciones abiertas, varios de ellos bajo esa categoría.

La discrepancia de mayor impacto inmediato es la de los plazos de procurement. El schedule programa Purchase Orders para la Bomba HP durante la semana del 04 al 10 de marzo de 2026 — esta semana — sin que el datasheet esté formalmente aprobado. La Valve List tiene un PO programado el 11-Mar con veredicto activo Code 4 (Rechazado). El Feed Turbocharger aparece en PO el 01-Abr también con Code 4. Estas tres situaciones contradicen el compromiso formal de BW Water registrado en la reunión del 18-Feb-2026: "no POs before ADASA approval."

---

## 2. Comparativa de los Tres Schedules

### 2.1 Hitos Principales

| Hito | Oct-2025 | Feb-2026 | Mar-2026 | Δ Oct→Mar | Δ Feb→Mar |
|------|----------|----------|----------|-----------|-----------|
| **NTP / Contract Award** | 07-Oct-2025 | 07-Oct-2025 | 07-Oct-2025 | — | — |
| **Fin Engineering (General)** | 05-Ene-2026 | 24-Abr-2026 | **20-Feb-2026** | N/A | N/A (ver §3.1) |
| **Fin Engineering (E&P Related)** | 05-Ene-2026 | 24-Abr-2026 | **09-Jul-2026** | **+185 días** | **+76 días** |
| **Fin Fabricación** | 31-Jul-2026 | 01-Ago-2026 | 01-Ago-2026 | +1 día | Sin cambio |
| **FAT** | 30-31 Jul | **NO INCLUIDO** | **25-Jul a 01-Ago (7d)** | Reinstaurado | **Reinstaurado** |
| **EXW / Ready to Ship** | 03-Ago (Malasia) | NO incluido | **02-03 Ago (Malasia)** | Sin cambio | **Corregido** |
| **Site Supervision / Commissioning** | 26-Sep a 16-Oct | **NO INCLUIDO** | **18-Sep a 08-Oct (21d)** | Reinstaurado | **Reinstaurado** |
| **Operator Training** | 17-25 Oct | **NO INCLUIDO** | **09-17 Oct (9d)** | Reinstaurado | **Reinstaurado** |
| **Final Documentation & Close-out** | Oct-Nov | **NO INCLUIDO** | **18-Oct a 16-Nov (30d)** | Reinstaurado | **Reinstaurado** |
| **Fin Proyecto** | 24-Nov-2026 | 16-Sep-2026 | **16-Nov-2026** | Sin cambio neto | +61 días |

### 2.2 Ingeniería: Nueva Extensión Crítica

| Parámetro | Oct-2025 | Feb-2026 | Mar-2026 | Δ desde línea base |
|-----------|----------|----------|----------|-------------------|
| **Ingeniería "General"** | 65 días | 83 días (≈) | **99 días (a 20-Feb-2026)** | N/A (mostrado como completo) |
| **Engineering (E&P Related)** | 65 días | 139 días | **198 días (a 09-Jul-2026)** | **+133 días (+205%)** |
| **Fin contrato línea base** | 05-Ene-2026 | 24-Abr-2026 | 09-Jul-2026 | **+185 días** |

La extensión de 76 días adicionales respecto a febrero-2026 se origina en los ítems bajo "Equipment & Procurement Related": el último hito de fabricación (CSC for Container) queda registrado el 09-Jul-2026, tirando del plazo del padre "Engineering."

Este encadenamiento es estructuralmente incorrecto: BW Water agrupa bajo "Engineering" tanto los documentos técnicos como el procurement y la fabricación en Penang. El resultado es que la fecha de cierre de "Engineering" refleja en realidad el fin de la fabricación, no el fin de la actividad de diseño. ADASA debe exigir que el schedule separe explícitamente (a) ingeniería documental, (b) procurement, y (c) fabricación como fases independientes con sus propias fechas de inicio y fin.

---

## 3. Bloque 1 — Estado de la Ingeniería Documental

### 3.1 La Fase "General" Mostrada Como Completada al 20-Feb-2026

El schedule muestra la rama "General" de ingeniería (Civil, Proceso, Eléctrico, I&C, Mecánico) con todas sus actividades de revisión terminadas el 20-Feb-2026. Esto no es consistente con el estado real del proyecto.

| Disciplina | Documentos con observaciones abiertas (al 06-Mar-2026) |
|------------|-------------------------------------------------------|
| Proceso | Plant Control Philosophy — nunca entregado; Process Calculation Rev A/B observaciones cerradas Rev B |
| Eléctrico | MCC Datasheet — **nunca entregado** (referencia: Fabricación del panel ya realizada según schedule anterior) |
| I&C | Control System Architecture — BW Water comprometió Rev C el **06-Mar-2026** (esta fecha); I/O List Rev A — "3 - To be revised"; Modbus TCP Memory Map — **51 días vencido desde TM N2** |
| Mecánico | A/C Thermal Calculation — **51 días vencido desde TM N2**; Equipment Layout — "3 - To be revised" (TM N5, footprint CIP externo pendiente) |
| General | 15 documentos nunca entregados; 14 documentos con observaciones activas |

El schedule no indica cómo ni cuándo se resolverán estos ítems. Mostrar la fase como cerrada crea la apariencia de que el backlog documental ya fue liquidado — apariencia que los números de este proyecto desmienten.

### 3.2 Documentos Comprometidos para 06-Mar (Hoy) No Presentes en el Schedule

El correo de BW Water del 05-Mar-2026 comprometió tres entregables para el 06-Mar-2026:

| Ítem | Compromiso | ¿Aparece en schedule? |
|------|------------|-----------------------|
| IO MODBUS | 06-Mar-2026 | **NO** |
| Control Architecture Rev C + UPS ≥ 8h | 06-Mar-2026 | **NO** (solo actividad genérica de I&C) |
| VFD variables en I/O List | 06-Mar-2026 | **NO** |

### 3.3 Ítems Sistémicamente Ausentes

Los siguientes entregables con observaciones abiertas desde transmittales anteriores no tienen entrada individual en el schedule:

| Ítem | Origen | Días vencido |
|------|--------|:------------:|
| Modbus TCP Memory Map | TM N2 | **51 días** |
| A/C Thermal Calculation Rev B | TM N2 | **51 días** |
| Valve List Rev C (4 TAGs duplicados + 109 ítems) | TM N6 | 7 días |
| Feed Turbocharger Rev D (coupling ≥ 1,800 psi) | TM N6 | 7 días |
| Coupling datasheets SIP-09-001 y SIP-09-002 | TM N6 | 7 días |
| Interstage TC: confirmación MAWP 1,800 psi (FEDCO) | TM N6 | 7 días |
| Vibration mounting ambos Turbochargers | TM N6 | 7 días |
| DS MCC | Lista pendiente | >60 días |
| Equipment Layout Rev B (footprint CIP externo) | TM N5 Rev 1 | >10 días |

---

## 4. Bloque 2 — Issues TM N6 vs. Schedule de Procurement

### 4.1 Tabla de Conflictos Procurement vs. Estado Técnico

| Equipo | PR/PO en Schedule | Estado ADASA | Conflicto |
|--------|:-----------------:|:------------:|:----------:|
| **RO HP Pump** | **04-10 Mar (esta semana)** | Aceptación condicional 93 kW (05-Mar correo) | **ALTO** — condición no formalizada en transmittal |
| **All Valve** | 11-17 Mar | **Code 4 — RECHAZADO** (TM N6) | **CRÍTICO** — compra con lista rechazada |
| **Instrument Set** | 11-17 Mar | "3 - To be revised" (TM N3) | **CRÍTICO** — compra sin lista aprobada |
| **Feed Turbo** | 01-07 Abr | **Code 4 — RECHAZADO** (TM N6) | **CRÍTICO** — compra con TC rechazado |
| **Interstage Turbo** | 24-30 Abr | Condicional (pendiente MAWP FEDCO) | MAYOR |
| **Antiscalant Dosing Pump** | 10-16 Abr | Condicionado a CT-001 sin respuesta | MAYOR |

BW Water comprometió formalmente el 18-Feb-2026 no emitir órdenes de compra antes de la aprobación de ADASA. El schedule presenta ese compromiso como papel mojado: la PO de HP Pump está agendada cuatro días después de la reunión del 09-Mar.

### 4.2 Static Mixer: Reversión Inexplicada

El schedule de Feb-2026 mostraba el Static Mixer con fabricación completada en octubre-noviembre 2025 (34 días desde NTP). El schedule actual lo presenta como un item de procurement futuro: PR/PO 01-07 May-2026, fabricación 08-May a 04-Jun-2026.

Hay tres interpretaciones posibles, ninguna de ellas tranquilizadora:
- El Static Mixer **no fue fabricado** en 2025 y la entrada anterior era un error.
- Fue fabricado pero **no es aceptable** (DS Rev A: "3 - To be revised", material PVC vs FRP de la oferta) y se requiere reemplazar.
- Hay una confusión de ítems en el schedule.

BW Water debe aclarar el estado real del Static Mixer antes de la reunión del 09-Mar.

### 4.3 Panel Eléctrico: Otra Inconsistencia

| Schedule | Actividad "Electrical panel delivery" |
|----------|--------------------------------------|
| Feb-2026 | 07-Oct-2025 a 12-Ene-2026 (84 días, **aparentemente completado**) |
| Mar-2026 | **02-Abr-2026 a 08-Jul-2026** (84 días, futuro) |

El panel aparecía entregado en el schedule anterior. Ahora aparece como actividad futura de abril a julio. Este cambio requiere aclaración explícita: ¿el panel fue entregado o no? ¿Hubo rechazo del panel original? Si no fue entregado, el DS del MCC (nunca presentado a ADASA) sigue siendo urgente.

---

## 5. Bloque 3 — Procurement Sin Aprobación Técnica

### 5.1 Resumen Cronológico de Riesgo

El orden de prioridad de riesgo, considerando fechas y estado técnico:

**Semana actual (04-10 Mar-2026):**
- HP Pump: PO pendiente de emitir. La aceptación condicional del 05-Mar ("93 kW CONDITIONAL") no equivale a un Code 1 o Code 2 formal de transmittal. ADASA debe formalizar la posición antes del lunes 09-Mar.

**Semana del 11-17 Mar-2026:**
- Valve List (All Valve): PO programada con Code 4 activo. Veredicto emitido en TM N6 el 27-Feb-2026. La Rev C no ha sido ni siquiera presentada. Emitir PO con esta lista implica comprar valvulas con TAGs duplicados y actuaciones incorrectas.
- Instrument Set: PO programada con Instrument List en estado "3 - To be revised" desde TM N3. Errores documentados: TAG FIT-09-001 (renombrado pero con posibles consecuencias en IO), transmisores de vibración y Pt-100 de motor faltantes.

**Semana del 01-07 Abr-2026:**
- Feed Turbocharger: PO programada con Code 4 activo (coupling 1,200 psi, margen 1.19x < ASME 1.5x). El Rev D no ha sido presentado.

**Semana del 10-16 Abr-2026:**
- Antiscalant Dosing Pump: PO con CT-001 vencida más de 30 días sin respuesta. El potencial cambio de dosificación de 0.5 a 5 ppm podría inutilizar la bomba ProMinent seleccionada.

---

## 6. Bloque 4 — FAT, Comisionamiento y Training

### 6.1 Positivo: Obligaciones Contractuales Reinstauradas

A diferencia del schedule de feb-2026, el documento actual incluye:

| Actividad | Fechas | Duración | Evaluación |
|-----------|--------|:--------:|------------|
| Factory Acceptance Test (FAT) | 25-Jul a 01-Ago-2026 | 7 días | Consistente con schedule oct-2025 |
| Site Supervision & Commissioning | 18-Sep a 08-Oct-2026 | 21 días | Reinstaurado |
| Operator Training | 09-17 Oct-2026 | 9 días | Reinstaurado |
| Final Documentation & Close-out | 18-Oct a 16-Nov-2026 | 30 días | Reinstaurado |

Esta reincorporación es un avance. Sin embargo, hay puntos que ADASA debe verificar antes de dar por confirmado el FAT:

- ¿El FAT incluye presencia formal de ADASA como cliente? El schedule solo indica "Factory Acceptance Test for System" sin especificar quién asiste.
- 7 días de FAT para un sistema UHPRO completo con bomba de alta presión, dos turbochargers, sistema CIP y racks de membranas es estrecho. El schedule oct-2025 también usó 2 días para FAT; ahora son 7.
- La logística entre EXW (02-03 Ago) y Commissioning en Chile (18-Sep) implica ~46 días de tránsito. Si el sistema viaja de Penang a Taltal, ese plazo es ajustado pero posible (~35-40 días). ADASA debe confirmar que BW Water no está asumiendo una ruta que no cuadra con las fechas.

### 6.2 EXW Malasia: Corregido

El schedule de feb-2026 mostraba un envío a Florida de 45 días. El schedule actual confirma "System ready to ship (Ex-work)" el 02-03 Ago-2026 sin referencia a Florida. Esto alinea con el Contrato C-4300. La inconsistencia anterior queda superada, aunque ADASA debe confirmar por escrito que BW Water no tiene planes de tránsito intermedio.

---

## 7. Bloque 5 — Fechas Contractuales

### 7.1 EXW y Multas

| Parámetro | Valor Contractual | Schedule Mar-2026 | Δ |
|-----------|:-----------------:|:-----------------:|:-:|
| **EXW (Ex-Works)** | ~03-Ago-2026* | **02-03 Ago-2026** | Sin atraso declarado |
| **Multa atraso suministro** | 0,2%/día = USD 1,228/día | — | — |
| **Tope multas** | 15% = USD 92,099 | — | — |
| **Cláusula terminación** | Atraso > 30 días | — | — |

*Fecha EXW contractual a calcular contra C-4300; en análisis anterior se trabajó con 03-Ago-2026 como referencia.

El schedule declara EXW el 02-03 Ago-2026. Si se cumple, no habría multa por atraso de suministro. El riesgo está en la cadena crítica: la fabricación depende de que los POs de Valve List y Instrument Set se emitan con documentación aprobada. Si esos POs se atrasan porque ADASA no aprueba las correcciones, la ruta crítica se desplaza.

### 7.2 Multa por Atraso de Ingeniería

La multa por atraso de ingeniería/documentos es del 0,05%/día = USD 307/día.

El backlog actual incluye ítems con 51 días de atraso (Modbus TCP Memory Map, A/C Calculation). Si se considera que la línea base de ingeniería era 05-Ene-2026 y hoy es 06-Mar-2026 (60 días de atraso general en ingeniería documental), la multa acumulada teórica sería del orden de USD 18,400 por el conjunto de documentos atrasados. Esto no ha sido formalmente cuantificado ni reclamado.

---

## 8. Bloque 6 — Compromisos 05-06 Mar Sin Reflejo en el Schedule

Del correo ADASA del 05-Mar-2026 y los compromisos registrados de BW Water para el 06-Mar:

| Ítem | Compromiso BW Water | ¿En Schedule? | Estado al 06-Mar |
|------|---------------------|:-------------:|:----------------:|
| IO MODBUS | Entrega 06-Mar | **NO** | Sin confirmar |
| Control Architecture Rev C + UPS ≥ 8h | Entrega 06-Mar | **NO** | Sin confirmar |
| VFD variables en I/O List | Entrega 06-Mar | **NO** | Sin confirmar |
| Modbus TCP Memory Map | Vencido desde TM N2 | **NO** | 51 días atrasado |

La ausencia de estos ítems en el schedule de catch-up es consistente con el patrón de febrero: BW Water presenta un programa general sin desglose de documentos específicos. No es posible hacer seguimiento fiable del estado de ingeniería con una sola barra de "Engineering" de 198 días.

---

## 9. Evaluación Global

### 9.1 Lo Que el Schedule Resuelve

| Problema (Feb-2026) | Resolución (Mar-2026) |
|---------------------|----------------------|
| FAT eliminado | **Reinstaurado** (7 días, Jul-2026) |
| Commissioning eliminado | **Reinstaurado** (21 días, Sep-Oct-2026) |
| Operator Training eliminado | **Reinstaurado** (9 días, Oct-2026) |
| Close-out eliminado | **Reinstaurado** (30 días, Oct-Nov-2026) |
| Shipping a Florida (no EXW) | **Corregido**: EXW Malasia confirmado |

### 9.2 Lo Que el Schedule No Resuelve

| Problema Activo | Situación en Mar-2026 |
|-----------------|----------------------|
| Ingeniería extendida | **Agravada**: 198 días vs 139 días (feb), +76 días adicionales |
| Documentos pendientes (15) | No hay desglose ni fechas |
| Documentos rechazados/a revisar (14) | No hay desglose ni fechas |
| Valve List RECHAZADA (Code 4) | PO programada 11-Mar con lista rechazada |
| Feed TC RECHAZADO (Code 4) | PO programada 01-Abr con TC rechazado |
| Modbus TCP Memory Map (51 días vencido) | Ausente del schedule |
| Compromisos 06-Mar | Ausentes del schedule |
| Panel eléctrico: contradicción de estado | Sin explicación |
| Static Mixer: contradicción de estado | Sin explicación |
| A/C Calculation (51 días vencido) | Mostrado como "completo" en General engineering |

---

## BULLETS REUNIÓN 09-MAR-2026

### Puntos a Plantear a BW Water — Orden de Prioridad

---

**BLOQUE A: PROCUREMENT INMEDIATO (Decisiones esta semana)**

**1. HP Pump — PO esta semana: posición ADASA**
El schedule programa PO de HP Pump para el 04-10 Mar. La aceptación condicional del 05-Mar ("93 kW CONDITIONAL") no es un Code 1 o Code 2 de transmittal formal. ADASA debe confirmar si esa aceptación condicional libera la PO o si se requiere un transmittal con Code 2 primero. Si el criterio es que se necesita transmittal formal, comunicarlo en la reunión y fijar fecha para emitir TM N7 con ese único ítem.

**2. Valve List: No emitir PO el 11-Mar**
La Valve List tiene Code 4 activo (TM N6, 27-Feb-2026). Hay 4 TAGs duplicados documentados y pendiente de revisión sistemática de 109 ítems. La PO de "All Valve" está agendada para el 11-Mar. ADASA debe solicitar explícitamente que esa PO quede suspendida hasta que Rev C sea revisada y reciba al menos Code 2.
*Base contractual:* Compromiso formal de BW Water (18-Feb-2026): "No POs before ADASA approval."

**3. Feed Turbocharger: No emitir PO el 01-Abr**
Feed TC tiene Code 4 activo (TM N6). La PO está en el schedule para el 01-Abr. La condición mínima para levantar el rechazo es: Rev D con coupling ≥ 1,800 psi + datasheet del fabricante del acople certificado para HPB service. Sin Rev D revisada y con al menos Code 2, la PO no puede emitirse.

---

**BLOQUE B: DELIVERABLES VENCIDOS (Urgencia alta)**

**4. Modbus TCP Memory Map — 51 días vencido**
Requerido desde TM N2. Sin este documento, ADASA no puede avanzar en la ingeniería de integración SCADA. Solicitar fecha de entrega firme. Si BW Water no puede dar fecha, escalar formalmente por carta con referencia a la multa de ingeniería del 0,05%/día.

**5. A/C Thermal Calculation — 51 días vencido**
El schedule muestra esta actividad como completada dentro de la fase "General Engineering" al 13-Ene-2026. En realidad sigue abierta desde TM N2. Exigir que BW Water explique la discrepancia y entregue el cálculo completo (incluyendo configuración n+1 per ET 5.1.11).

**6. Compromisos 06-Mar: IO MODBUS + Control Architecture Rev C + VFD variables**
Solicitar estado de los tres entregables comprometidos para el 06-Mar. Si no fueron entregados ayer, registrar incumplimiento y fijar nuevo deadline con consecuencia formal.

---

**BLOQUE C: SCHEDULE — EXIGENCIAS PARA ACEPTARLO FORMALMENTE**

**7. Exigir desglose de ingeniería documental por ítem**
El schedule actual muestra una sola barra de 198 días para "Engineering." No es posible gestionar el proyecto sin un desglose por documento que incluya: (a) 15 documentos nunca entregados, (b) 14 documentos con observaciones activas. ADASA debe pedir un schedule de documentos en los mismos términos que solicitó en el correo del 28-Ene-2026 — con fecha de entrega por documento, responsable y condiciones de aprobación previa.

**8. Aclarar la contradicción del panel eléctrico**
El schedule de feb-2026 mostraba el panel entregado (Oct-2025 a Ene-2026). El schedule actual lo muestra como actividad futura (Abr-Jul-2026). ¿Cuál es el estado real del panel? Si fue entregado, ¿fue fabricado sin DS MCC presentado a ADASA? Si no fue entregado, el DS MCC sigue siendo urgente y debe aparecer en el schedule de documentos.

**9. Aclarar el estado del Static Mixer**
Feb-2026: fabricado en oct-nov 2025. Mar-2026: PR/PO mayo, fabricación junio. ¿El primer static mixer no es aceptable (PVC vs FRP)? ¿O el schedule anterior era incorrecto? La respuesta impacta directamente el costo y el cronograma de procurement.

---

**BLOQUE D: ISSUES TM N6 (Deadline 10-Mar-2026)**

**10. Valve List Rev C: 4 TAGs duplicados + revisión sistemática**
Confirmar que BW Water tiene claro el alcance de la corrección requerida: no solo eliminar los 4 duplicados documentados, sino verificar los 109 ítems de la lista completa. El deadline del TM N6 es el 10-Mar.

**11. Coupling datasheets — ambos Turbochargers**
Solicitar el datasheet del fabricante del acople para SIP-09-001 (Feed) y SIP-09-002 (Interstage). Es condición necesaria para levantar el Code 4 del Feed TC y para confirmar la aceptación condicional del Interstage TC. Sin ese documento, no hay base técnica para emitir las POs.

**12. Confirmación escrita de FEDCO: MAWP 1,800 psi Interstage TC en servicio brine**
ADASA aceptó condicionalmente el Interstage TC sujeto a confirmación por escrito del fabricante (FEDCO). Solicitar esa carta en la reunión o antes del 10-Mar.

---

**BLOQUE E: CONTEXTO CONTRACTUAL**

**13. Obligaciones contractuales pendientes de BW Water**
La ingeniería lleva 185 días de extensión respecto a la línea base contractual. ADASA no ha cuantificado formalmente las multas de ingeniería acumuladas (0,05%/día). La reunión del 09-Mar es el momento adecuado para informar a BW Water que ADASA mantiene el derecho a aplicar esas multas retroactivamente si el estado documental no se normaliza dentro de un plazo razonable.

**14. EXW Malasia: confirmar por escrito**
El schedule actual corrige el error de febrero (envío a Florida) y declara EXW el 02-03 Ago-2026 en Malasia. Solicitar confirmación formal por escrito de que el punto de entrega es Penang y que no hay envío intermedio a Florida ni a otro destino. Necesario para que ADASA planifique la logística de transporte a Chile.

---

*Documento interno ADASA — NO ENVIAR*
*Preparado: 06 de marzo de 2026 | Proyecto: 12803 — Módulo de Salmuera Taltal | Contrato: C-4300*
