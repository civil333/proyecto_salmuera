# COMPILADO INTERNO — TM N12
**PROYECTO:** BAE 12803 — Módulo Salmuera Taltal
**CÓDIGO:** P22-TM-09-000-012-0
**FECHA:** 30-Mar-2026
**ENTREGAS:** E22 (25007-0022) / E23 (25007-0023)
**USO:** INTERNO ADASA — NO ENVIAR A BW WATER

---

## 1. DOCUMENTOS REVISADOS

| N° | Código | Descripción | Rev | Veredicto |
|----|--------|-------------|-----|-----------|
| 1 | P22-LI-09-008-014 | Datasheet of Vibration Transmitter | A | **3 — To be Revised** |
| 2 | P22-LI-09-009-003 | Line List | B | **2 — Approved as Noted** |

**VEREDICTO GLOBAL: 3 — TO BE REVISED**

---

## 2. ANÁLISIS DOCUMENT 1: VIBRATION TRANSMITTER DATASHEET (E22, 25007-0022)

**Fabricante:** IFM
**Modelo:** VTV122
**Tags:** VT-09-001 (BH-09-001 HP Pump) / VT-09-002 (SIP-09-001 Feed TC) / VT-09-003 (SIP-09-002 Interstage TC)
**Rev:** A — 17-Mar-2026

### Hallazgos positivos
- Cubre los 3 TAGs requeridos: VT-09-001/002/003 ✓
- Señal: 4-20mA (cubre requisito básico de salida analógica) ✓
- Tipo: MEMS — adecuado para aplicaciones de vibración continua ✓
- Rango: 0-25 mm/s RMS, frecuencia 10-1000 Hz — compatible con ISO 10816 ✓
- IP67/68/69K ✓
- Rango temperatura ambiente: -30 a 125°C (supera condición de instalación 23-33°C) ✓
- Material: SS316L ✓
- Ubicación: Indoor ✓

### OBS-01 (MAJOR): HART no especificado — P22-LI-09-008-014 Rev A

**Problema:** El VTV122 proporciona solo salida 4-20mA analógica. El protocolo HART no está listado en ninguna sección del datasheet (página 2 ítem 30 "Outputs Communication: 4 to 20 mA current outputs"; página 3 solo muestra "Analogue current output [mA]: 4...20").

**Requisito ET:** ET §5.5 (pág. 1311) establece explícitamente: *"El protocolo de la instrumentación deberá ser 4-20 mA + HART"* para todos los instrumentos del módulo.

**Impacto:**
- Sin HART no es posible realizar diagnósticos remotos desde el sistema de gestión de activos (si aplica)
- No permite parametrización en campo via comunicador HART
- Potencialmente inconsistente con los requisitos de la IO List si esta especifica HART para VT-09-001/002/003

**Acción requerida:** BW Water debe presentar una de las siguientes:
  a) Alternativa HART-capable para el transmisor de vibración (modelo diferente o serie superior IFM), o
  b) Documentación formal de desviación (deviation form) que justifique la ausencia de HART en transmisores de vibración con referencia al capítulo ET que lo autoriza.

**Nota Van Doorn (NO incluir en TM):** Verificar si la IO List Rev B especifica HART para VT-09-001/002/003. Si la IO List ya fue aceptada con 4-20mA sin HART para VT tags, documentar esto en la desviación.

### NOTE-01 (MINOR): Cantidad "1 duty" para 3 TAGs — P22-LI-09-008-014 Rev A

**Problema:** El datasheet (página 2, ítem 3) indica "Quantity - Duty: 1 / Standby: 0", pero el header del mismo documento lista tres TAGs: VT-09-001/002/003.

**Contexto:** El proyecto requiere 3 unidades físicas del VTV122 (una por equipo: BH-09-001, SIP-09-001, SIP-09-002).

**Acción:** Confirmar que la orden de compra incluye 3 unidades, y actualizar el campo Quantity en Rev B.

---

## 3. ANÁLISIS DOCUMENT 2: LINE LIST REV B (E23, 25007-0023)

**Rev B:** 25-Mar-2026 | **Rev A:** 12-Jan-2026

### Cierre TM N3 OBS-01 ✓ CERRADO
DA-SSD-DN80-09-005 (1st Stage Reject): DP actualizada de 70 bar → **80 bar**
Margen: (80-68)/68 = **17.6%** — cumple ≥10% ✓
Consolidated Comment Sheet (página 4): "BW has revised accordingly." ✓

### OBS-01 (MINOR): Margen de presión insuficiente — DA-SSD-DN80-09-006

**Línea:** DA-SSD-DN80-09-006 — 2nd Stage RO Feed
**Valores Rev B:** OP = 85 bar, DP = 90 bar → **Margen = 5.9%**

**Problema:** Margen < 10% mínimo recomendado para líneas de proceso (mismo criterio aplicado en TM N3 OBS-01 para línea 09-005). La presión operacional de 85 bar en la alimentación de segunda etapa RO es la más alta del sistema. Un margen del 5.9% es insuficiente para transitorios de presión normales en el arranque/paro de equipos.

**Acción:** Aumentar DP de DA-SSD-DN80-09-006 a mínimo **95 bar** (margen 11.8%) en Rev C.

**Líneas adicionales con margen <10%:** (informacional — no constituyen OBS separadas)
- DA-SSD-DN65-09-007 (2nd Stage Reject): OP=83, DP=90 → 8.4%
- DA-SSD-DN65-09-008 (Interstage TC Brine Outlet): OP=46, DP=50 → 8.7%

Considerar revisar también estas dos líneas en Rev C para consistencia.

### NOTE-01 (MINOR): Línea sin identificador — Make-Up for CIP

**Problema:** Página 2, la fila para "MAKE-UP FOR CIP" (PVC SCH80, DN80, 7.62mm, P9) tiene el campo LINE NO. en blanco. El resto de las líneas tienen identificador asignado.

**Acción:** Asignar LINE NO. correspondiente (probablemente de la serie PE-PVC-DN80-09-0XX) en Rev C.

### NOTE-02 (MINOR): Notación "SCH80" para líneas SSD

**Problema:** Todas las líneas Super Duplex Steel utilizan la notación "SUPER DUPLEX STEEL, SCH80" sin el sufijo "S". Per ASME B36.19M, las tuberías de acero inoxidable y duplex se designan como "Schedule 80S". Los espesores de pared listados son correctos para SCH 80S (DN100: 8.56mm, DN80: 7.62mm, DN65: 6.02mm).

**Acción:** Corregir notación a "SCH 80S" en todas las filas SSD en Rev C.

### Tabla completa de líneas HP — Verificación ET §5.2.2

| Línea | Servicio | Material | OP (bar) | DP (bar) | Margen | OK? |
|-------|---------|---------|----------|----------|--------|-----|
| DA-SSD-DN100-09-003 | HP Pump Discharge | SSD | 51 | 60 | 17.6% | ✓ |
| DA-SSD-DN100-09-004 | 1st Stage RO Feed | SSD | 70 | 80 | 14.3% | ✓ |
| DA-SSD-DN80-09-005 | 1st Stage RO Reject | SSD | 68 | 80 | 17.6% | ✓ CLOSED |
| DA-SSD-DN80-09-006 | 2nd Stage RO Feed | SSD | 85 | 90 | 5.9% | ❌ OBS-01 |
| DA-SSD-DN65-09-007 | 2nd Stage RO Reject | SSD | 83 | 90 | 8.4% | ⚠ <10% |
| DA-SSD-DN65-09-008 | Interstage TC Brine Outlet | SSD | 46 | 50 | 8.7% | ⚠ <10% |
| DA-SSD-DN65-09-009 | Feed TC Brine Outlet | SSD | 1 | 50 | — | ✓ |
| DA-SSD-DN65-09-016 | RO Brine Discharge | SSD | 1 | 50 | — | ✓ |

Líneas CIP HP:
| Línea | Servicio | Material | OP (bar) | DP (bar) | OK? |
|-------|---------|---------|----------|----------|-----|
| CP-SSD-DN100-09-014 | CIP Feed 1st Stage | SSD | 4 | 80 | ✓ |
| CP-SSD-DN80-09-015 | CIP Feed 2nd Stage | SSD | 4 | 90 | ✓ |
| CP-SSD-DN80-09-044 | 1st Stage CIP Reject | SSD | 4 | 80 | ✓ |
| CP-SSD-DN65-09-045 | 2nd Stage CIP Reject | SSD | 4 | 90 | ✓ |

Líneas LP verificadas: todas PVC SCH80, presiones bajas (<10 bar design) ✓

---

## 4. OBSERVACIONES PENDIENTES DE TM ANTERIORES

### Desde TM N10 (entrega E18, 12-Mar-2026) — todas sin cierre

| OBS | Documento | Descripción | Estado |
|-----|-----------|-------------|--------|
| OBS-01 | I/O List | TAGs TE vs TIT inconsistentes; TIT-09-003 servicio conflicto | ❌ OPEN |
| OBS-02 | Data Transfer List | Rangos conductividad 0-20 mS/cm (brine necesita 65-133 mS/cm) | ❌ OPEN |
| OBS-03 | Data Transfer List | VE09-014 duplicado en DI; LS09-001/002 ausentes Modbus | ❌ OPEN |
| OBS-04 | Control Architecture | UPS 8h autonomy sin cálculo ni especificación | ❌ OPEN |
| OBS-05 | GA Antiscalant Tank | Volumen efectivo, material, datos sísmicos ausentes | ❌ OPEN |
| NOTE-05 | Control Architecture | HMI Screenshots P22-BREAD-09-008-001 comprometido TM N4, jamás entregado | ❌ OPEN |

### Desde TM N11 (entregas E19/E20/E21, 17-Mar-2026) — todas sin cierre

| OBS | Documento | Descripción | Estado |
|-----|-----------|-------------|--------|
| OBS-01 | Valve List Rev C | TAG duplicado VE-09-007 (ítems 44 y 64) | ❌ OPEN |
| OBS-02 | Valve List Rev C | TAG duplicado PSV-09-002 (ítems 105 y 112) | ❌ OPEN |
| OBS-03 | Grounding Layout Rev B | Posiciones derivadas de Piping Layout Rev A rechazado | ❌ OPEN — depende Equipment Layout Rev B |
| OBS-04 | Instrument Location Layout Rev B | Misma causa que OBS-03 | ❌ OPEN — depende Equipment Layout Rev B |

**Nota operacional:** TM N10 OBS-01/02/03 requieren IO List Rev C y Data Transfer List Rev B — no recibidos. TM N11 OBS-03/04 no pueden cerrarse hasta que Equipment Layout Rev B sea formalizado como submittal oficial.

---

## 5. TABLA RESPONSE SUMMARY (CCS)

| Submittal | Doc. No. | Descripción | Rev | Code |
|-----------|----------|-------------|-----|------|
| 25007-0022 | P22-LI-09-008-014 | Datasheet of Vibration Transmitter | A | **3** |
| 25007-0023 | P22-LI-09-009-003 | Line List | B | **2** |
