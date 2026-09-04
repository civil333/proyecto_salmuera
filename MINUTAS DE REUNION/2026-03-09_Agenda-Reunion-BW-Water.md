# Agenda Reunion BW Water — 09-Mar-2026
**Hora:** 10:00 AM Chile | **Participantes:** ADASA + BW Water (Eduardo, Nick)

> Preparado: Luis Rivera | Proyecto: BAE 12803 — C-4300

---

## Contexto previo

- TM N6 enviado 02-Mar: Valve List RECHAZADA + Feed TC RECHAZADO
- TM N7 emitido 08-Mar: Control Philosophy + A/C Calc requieren revision
- Schedule Mar-2026 (05-Mar): Engineering extendida a 09-Jul-2026 (+185 dias vs linea base)
- Reunion reprogramada desde 04-Mar al 09-Mar (Eduardo en Malasia)

---

## 1. PROCUREMENT BLOQUEADO — ITEM URGENTE

**Cuatro items de procurement tienen PO programada en los proximos dias pero estan bloqueados por documentos rechazados o pendientes.**

| Item | PO Programada (Schedule) | Estado actual | Bloqueo |
|------|--------------------------|---------------|---------|
| All Valve (Valve List) | 11-Mar-2026 | Code **4 — Rejected** (TM N6) | Rev C no recibida. 4 duplicados no resueltos. |
| Instrument Set | 11-Mar-2026 | IO List sin actualizar | 44 dias pendiente desde TM N3. Falta Modbus + DO/DI signals. |
| HP High Feed Pump | 4-10 Mar-2026 | Code 2-AN (TM N6) — **PO puede proceder** | Nota aclaratoria: 93 kW / HPB-60 Standard / FEDCO coupling. |
| Feed Turbocharger | 01-Abr-2026 | Code **4 — Rejected** (TM N6) | Coupling 1,200 psi inaceptable. Rev D: ≥2,000 psi / ≥1,800 psi min + datasheet acople. |

**Pregunta directa BW Water:**
- Valve List Rev C: fecha de entrega confirmada. Si llega despues del 11-Mar, la PO de valvulas debe postergarse.
- Instrument Set PO del 11-Mar: no puede ejecutarse con IO List desactualizada.

---

## 2. SCHEDULE — CONTRADICCION CRITICA

**El schedule de Mar-2026 muestra Engineering terminando el 09-Jul-2026. Los plazos de fabricacion y ensamble llevan a EXW 02-03 Ago-2026. No hay margen para demoras adicionales en ingenieria.**

| Hito (Schedule Mar-2026) | Fecha | Observacion |
|--------------------------|-------|-------------|
| Engineering completa | 09-Jul-2026 | +185 dias vs linea base contractual |
| FAT (7 dias) | 25-Jul a 01-Ago-2026 | Requiere todos los equipos instalados |
| EXW Malasia (Shipping) | 02-03 Ago-2026 | Hito contractual — multa 0.2%/dia si se atrasa |
| Commissioning | 18-Sep a 08-Oct-2026 | 21 dias en sitio |
| Training | 09-17 Oct-2026 | 9 dias |
| Close-out | 18-Oct a 16-Nov-2026 | 30 dias |

**Puntos a plantear:**

1. Engineering aun no termina — el schedule marca "General Engineering" como completo al 20-Feb, pero hay 15 documentos pendientes y 14 requiriendo correccion. ¿Sobre qué base se declara completa?

2. Fabrication starts 02-Apr (Container). FAT el 25-Jul. Son 115 dias de fabricacion total. No hay margen si documentos de ingenieria llegan en julio.

3. ¿Cual es el plan de recuperacion para los documentos criticos todavia abiertos? La ingenieria no puede terminar el 09-Jul si al 08-Mar-2026 el Control Philosophy (primera entrega Rev A) ya requiere 7 correcciones.

---

## 3. TM N7 — TRANSMITTAL EMITIDO HOY (08-Mar-2026)

**Se entrego TM N7 respondiendo Submittal 25007-0014 (E14).** Veredicto: 3 — TO BE REVISED.

### 3.1 Control Philosophy Rev A — 7 correcciones requeridas

| # | Tema | Criticidad | Contexto |
|---|------|------------|----------|
| 1 | UPS 30 minutos especificado — ET requiere **8 horas** | **CRITICO** | Incumplimiento contractual directo. Rev B debe incluir calculo de capacidad. |
| 2 | VE-07-014 vs VE-09-014 — misma valvula, area distinta | Medio | Resolver con Valve List y P&ID. |
| 3 | Modbus TCP/IP no referenciado en ninguna de las 48 paginas | **MAYOR** | 65 dias desde TM N2 sin Memory Map. |
| 4 | Codigo "BT" no definido en sistema de codificacion P22 | Formal | Asignar codigo estandar o registrar "BT" formalmente. |
| 5 | Sin monitoreo continuo temperatura motores (AI Pt-100) | **CRITICO** | Solo switches DI actuales — ET §5.3 requiere Pt-100 AI en devanados y rodamientos. |
| 6 | DO Module Status ausente | Medio | 44 dias pendiente desde TM N3. |
| 7 | DI General Module Enable ausente | Medio | 44 dias pendiente desde TM N3. |

**Implicacion en procurement:** El Control Philosophy Rev B es prerrequisito para que el set documental de instrumentacion y control este completo. La PO del Instrument Set (11-Mar schedule) depende de esto.

### 3.2 A/C Thermal Calculation Rev B — 2 correcciones

1. Inventario de cargas incompleto: solo motor HP y VFD incluidos. Faltan PLC/panel, instrumentos, dosificacion, luminarias.
2. Configuracion n+1 no declarada en el documento (solo inferible del Piping Layout).

### 3.3 Piping Layout Rev A + Tie-In Point Rev A — Aprobados con notas

- CIP externo confirmado fisicamente — cierra parcialmente TM N5 OBS-01.
- CIP y dosificacion en extremos opuestos del modulo: 11,150 mm de separacion vs 3.5 m exigidos. **Piping Layout Rev B requerido.**
- Tie-In Point Rev B: entregar despues de Piping Layout Rev B aprobado.

---

## 4. ITEMS STILL PENDING — CRONOLOGIA

Los siguientes items no son nuevos: llevan semanas o meses sin cierre.

| Item | Origen | Dias Abierto | Estado |
|------|--------|--------------|--------|
| Modbus TCP Memory Map | TM N2 | **65 dias** | Sin fecha de entrega |
| IO List update (Ethernet IP + DO/DI) | TM N3 | **44 dias** | Sin revision recibida |
| Valve List Rev C (4 duplicados) | TM N6 | 9 dias | Rev C no recibida |
| Feed TC Rev D (coupling ≥2,000 psi) | TM N6 | 9 dias | Rev D no recibida |
| Interstage TC — FEDCO coupling MAWP ≥1,845 psi | TM N6 | 9 dias | Confirmacion escrita pendiente |
| Vibration mounting ambos TCs (datasheet) | TM N6 | 9 dias | Pendiente |
| Piping Layout Rev B (CIP footprint ≤3.5m) | TM N7 | 0 dias | Nuevo |
| Control Philosophy Rev B (7 correcciones) | TM N7 | 0 dias | Nuevo |
| A/C Thermal Calc Rev C | TM N7 | 0 dias | Nuevo |
| Consulta Tecnica CT-001 respuesta | CT-001 | **27+ dias VENCIDO** | Sin respuesta BW Water |

**Solicitud concreta:** BW Water debe entregar un programa de documentos con fecha firme para cada item. Sin ese programa, ADASA no puede evaluar el avance real de ingenieria.

---

## 5. COMPROMISOS SOLICITADOS A BW WATER

Al finalizar la reunion, ADASA requiere fechas concretas para los siguientes items:

| Compromiso | Plazo Solicitado |
|-----------|-----------------|
| Valve List Rev C (4 duplicados resueltos, 109 items verificados) | Maximo 5 dias habiles |
| Feed Turbocharger Rev D (coupling ≥2,000 psi + datasheet) | Maximo 10 dias habiles |
| Datasheet acople Interstage TC + confirmacion MAWP FEDCO | Maximo 5 dias habiles |
| Control Philosophy Rev B (7 correcciones) | Maximo 10 dias habiles |
| Modbus TCP Memory Map | Fecha firme — 65 dias de atraso |
| IO List Rev B (Ethernet IP + DO Module Status + DI Enable) | Con Control Philosophy Rev B |
| A/C Thermal Calc Rev C | Maximo 10 dias habiles |
| Piping Layout Rev B (CIP + dosificacion en footprint ≤3.5m) | Maximo 15 dias habiles |
| Respuesta CT-001 (antiscalant dosing) | VENCIDA — respuesta inmediata |
| Programa de documentos pendientes con fechas | En la reunion |

---

## 6. NOTAS CONTRACTUALES

- El contrato C-4300 establece multa de **0.05%/dia** por atraso en documentos de ingenieria.
- La multa por atraso en EXW es **0.2%/dia** (USD ~1,228/dia).
- El limite de multas acumuladas es **15% del monto neto** = USD 92,099, tras lo cual ADASA puede terminar el contrato.
- La engineering tiene un atraso documentado de **185 dias** respecto a la linea base. El schedule Mar-2026 no presenta plan de recuperacion.
- **Clausula de terminacion:** Atraso >30 dias en entrega suministro o incapacidad manifiesta del proveedor.

> **Nota interna (no mencionar en reunion):** El atraso en ingenieria acumulado desde la linea base contractual (Oct-2025) es suficiente para sostener un reclamo formal de multas. La reunion es una oportunidad para registrar compromisos escritos antes de escalar.

---

## 7. TEMAS SECUNDARIOS (si hay tiempo)

- **Static Mixer:** El schedule Feb-2026 mostraba fabricacion como completa; el Mar-2026 programa PO el 01-May-2026. Requiere clarificacion sobre el estado real.
- **Panel Electrico:** Contradiccion entre completado Oct-2025 y entrega programada Abr-2026 (delivery 08-Jul-2026). Aclarar cual es correcto.
- **Operating Sequence Chart y Alarm & Setpoint List:** Referenciados en Control Philosophy como "SEPARATE DOCUMENT". BW Water debe comprometer fecha.
- **Reunion quincenal:** Proponer calendario fijo — no se han realizado las reuniones de coordinacion previstas en el contrato.

---

*Preparado: Luis Rivera — 08-Mar-2026*
*Basado en TM N7 (08-Mar-2026), TM N6 (27-Feb-2026), Schedule BW Water 05-Mar-2026*
