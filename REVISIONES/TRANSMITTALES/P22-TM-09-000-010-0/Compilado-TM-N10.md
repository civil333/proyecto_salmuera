---
tipo: Compilado Interno
transmittal: TM N10 — P22-TM-09-000-010-0
entrega: E18 / Submittal 25007-0018
fecha: 12-Mar-2026
veredicto: 3 — TO BE REVISED
nota: DOCUMENTO INTERNO — NO ENVIAR A BW WATER
---

# COMPILADO INTERNO — TM N10
## Entrega 18 (25007-0018) — 12-Mar-2026
## **NO ENVIAR — USO INTERNO ADASA**

---

## 1. Documentos Revisados

| Código | Rev | Título | Veredicto |
|--------|-----|--------|-----------|
| P22-LI-09-008-001 | B | I/O List | 2 — Approved as Noted |
| P22-LI-09-008-004 | A | Data Transfer List (Modbus TCP/IP) | 2 — Approved as Noted |
| P22-CD-09-004-001 | C | Control System Architecture | 2 — Approved as Noted |
| P22-DWG-09-005-015 | A | GA Antiscalant Dosing Tank | 2 — Approved as Noted |
| P22-DWG-09-005-012 | A | GA 1st Stage Turbo (SIP-09-001) | 3 — To be Revised |
| P22-DWG-09-005-013 | A | GA 2nd Stage Turbo (SIP-09-002) | 3 — To be Revised |

---

## 2. Contexto Técnico Interno

### 2.1 IO List Rev B — Análisis Detallado

**Lo que responde correctamente:**
- VT09-001/002/003: agregados (vibración HP Pump, Feed Turbocharger, Interstage TC)
- TE09-002/003 (HP Pump winding/bearing) y TE09-004/005 (CIP Pump winding/bearing): 3-Wire RTD a módulo 5069-IY4 → cierra solicitud TM N8
- PIT09-005 (2nd Stage Inlet Pressure) agregado Rev B
- TIT09-001 (CIP Tank Temperature): agregado Rev B — item 108
- VE09-012/013/014/015/016: nuevas válvulas motorizadas
- Items 19 y 21: señales de interfaz ADASA↔módulo agregadas en Rev B
- Power Meter (UHPRO LCP): Items 1-11 via Modbus TCP/IP
- VFD parameters (HP/CIP Pump): Items 34-37 y 115-118 via Ethernet/IP
- FIT-09-002 confirmado (renombrado desde FIT-09-001 TM N3 OBS-05)

**Problemas identificados:**
- Tags TE09-002/003/004/005 en IO List vs TIT09-002/003/004/005 en Data Transfer List para los mismos equipos → inconsistencia grave inter-documental
- TIT-09-003: IO List no lo tiene (usa TE09-003 = HP Pump bearing). Data Transfer List tiene TIT09-003 = HP Pump Bearing. Pero TM N8 datasheet P22-LI-09-008-013 decía TIT-09-003 = CIP Tank Temperature → CONTRADICCIÓN. Hay que resolverlo en IL Rev C.
- Items 19/21: dicen "Dry Contact (N.O) 24VDC". Ronald confirmó el 11-Mar que debe ser "relay contact". Es diferenciación importante para documentación de loop. Levantado como MINOR.
- CIT-09-001/004/005: rangos NO en IO List (el IO List no muestra measurement ranges). Los rangos incorrectos están en Data Transfer List → se levanta contra el DTL.

**Cierre de observaciones TM N8:**
- TM N8 OBS-2 (IO List update con 7 instrumentos): **CERRADO** — Rev B incorpora VT-001/002/003, RTDs TE-002/003/004 y la revisión de FIT-002

### 2.2 Data Transfer List Rev A — Análisis Detallado

**Lo que está bien:**
- Mapa completo Modbus: 64 DI, 16 DO, ~60 AI, ~22 AO
- Sistema Enable Command (DCS→módulo): 10001.7 ✓
- System Running Status (módulo→DCS): 00001.0 ✓
- Power meter: 40001-40011 (11 variables) ✓
- VFDs HP y CIP: parámetros eléctricos en 40015-40020 y 40022-40027 ✓
- Posición válvulas motorizadas: 40028-40049 (13 válvulas) ✓
- Instrumentación de proceso: 30003-30040 ✓
- Antiscalant dosing pump speed control: 40052-40053 ✓

**Cierre TM N7 OBS-03:** CERRADO — Data Transfer List Rev A entregada. 65+ días pendiente.

**Problemas:**
1. Conductividades: CIT-09-001 (0-20 mS/cm, dirección 30004), CIT-09-004 (0-20 mS/cm, 30015), CIT-09-005 (0-20 mS/cm, 30023) → rangos incorrectos, confirma que Instrument List no los corrigió aún
2. Items 22-23: VE09-014-SI001 y VE09-014-SIC001 en bloque DI (10002.5-10002.6) → error copy/paste. La descripción dice "CLOSE=HIGH / LOW" → debería ser LS09-001 (tank level HIGH) y LS09-002 (tank level LOW). LS09-001/002 NO están mapeados en DTL → son señales faltantes.
3. Tags TIT vs TE para temperaturas motores → mismo problema que IO List

### 2.3 Control Architecture Rev C — Análisis Detallado

**Positivo:**
- Digital Power Meter integrado vía Modbus TCP/IP → confirma avance TM N7 OBS-09
- Ethernet/IP para MOVs, VFDs, HMI, PLC CPU confirmado
- Fiber optic DCS-LCP panel documentado (responsabilidad Others/ADASA)
- PLC standalone confirmado en CCS (sin redundancia) → BW Water cita Tender Proposal

**Problema TM N7 OBS-01 (UPS 8h):**
El diagrama es gráfico, no hay texto extraíble con especificación UPS. El CCS dice "has been revised" pero no podemos confirmar el valor. Levantado como OBS-04 (MAJOR). BW Water debe dar confirmación escrita + cálculo.

**HMI Screenshots P22-BREAD-09-008-001:** Aún pendiente (mencionado en CCS respuesta N4).

### 2.4 GA Antiscalant Dosing Tank Rev A — Análisis Detallado

- Geometría cilíndrica: OD 630 mm, H_cuerpo 880 mm, H_total 1120 mm
- 8 boquillas especificadas (nozzle schedule presente)
- Estimación geométrica: ~0.249 m³ (no coincide con 0.27 m³ efectivo ni 0.34 m³ total del datasheet)
- **NOTAS VACÍAS**: sin volumen, sin material, sin presión de diseño → no resuelve TM N9 OBS-02
- N85 OUTLET = 1/2" → muy pequeño, verificar con caudal de dosificación

### 2.5 GAs Turbochargers Rev A — Análisis Detallado

**SIP-09-001 y SIP-09-002:**
- Tags correctos confirmados ✓ (SIP-09-001, SIP-09-002)
- Formato 4 vistas, escala 1:2 ✓
- Conexiones tipo CUT GROOVE STYLE 77 en todos los nozzles
- BOM (items 1-16) embebido como gráfico → no extraíble por PDF extractor
- **Sin provisiones para VT (vibración)**: ninguna referencia a montaje de sensor
- **Sin provisiones para Pt-100 (rodamientos)**: ningún boss o fitting de RTD visible
- Presión operacional: ~1000 psi en brine inlet/feed outlet → preocupación sobre rating Style 77

**Nota sobre TM N6 OBS-01 (coupling rejection):**
TM N6 rechazó el turbocharger datasheet por downgrade de 2000 psi a 1200 psi (Piedmont Style H). El GA muestra Style 77 en nozzles. Hay que distinguir si el "coupling" del TM N6 era: (a) el acoplamiento de tubería (pipe coupling = Victaulic), o (b) el acoplamiento mecánico de eje. Dado que el TM N6 mencionó "Piedmont Style H" y "Style D" (que son Victaulic-style pipe couplings), el coupling del TM N6 es pipe coupling. Style 77 es Victaulic flexible coupling ~300 psi rating. Esto es más grave que el Style H (1200 psi) que fue rechazado. Levantado como NOTE (no OBS) porque el GA es un nuevo documento y necesitamos que BW Water aclare el rating.

---

## 3. Observaciones Cerradas por E18

| Obs | TM | Descripción | Cierre |
|-----|-----|-------------|--------|
| OBS-03 | N7 | Data Transfer List Modbus TCP/IP | CERRADO — P22-LI-09-008-004 Rev A |
| OBS-2 | N8 | IO List Rev B (7 instrumentos faltantes) | CERRADO — P22-LI-09-008-001 Rev B |

---

## 4. Pendientes Consolidados (después de E18)

**Documentos a emitir por BW Water:**
- Instrument List Rev C → cierra: CIT rangos, TIT-09-003 conflict, power supply 120VAC, TE/TIT unification
- Valve List Rev C → cierra: 4 TAGs duplicados (VM-09-015/VE-09-008/VE-09-009/VM-09-065)
- Power Works Installation Drawing Rev B → cierra: grounding/earthing TM N8
- Control Philosophy Rev B → cierra: CEE/MVE HMI, vibration setpoints
- Piping Layout Rev B → cierra: TM N7 Note
- P&ID Rev C → cierra: VM→VE-09-015 prefix, TK-09-002 volume 0.34 m³
- Turbocharger Datasheet Rev C → cierra: TM N6 OBS-01 coupling rating
- GA Antiscalant Tank Rev B → cierra: volumen + material
- GA SIP-09-001/002 Rev B → cierra: VT + Pt-100 provisions
- Confirmación escrita UPS 8h → cierra: TM N7 OBS-01

---

## 5. Notas de Metodología

**Extracción PDFs Entrega 18:** Todos los PDFs convertidos a .md via large-pdf-reader.
- IO List: 141 items, extracción completa
- Data Transfer List: 189 items (120 activos), extracción completa
- Control Architecture: gráfico predominante, texto extraído de portada/CCS/labels
- GA Antiscalant Tank: fuentes SHX AutoCAD decodificadas (offset -3)
- GA 1st Stage Turbo: fuentes SHX decodificadas; BOM no extraíble (gráfico vectorial)
- GA 2nd Stage Turbo: ídem SIP-09-001

**Deadline E18:** 15-Mar-2026. Revisión completada 12-Mar-2026. ✓

---

## 6. Auditoría CCS — Completada 16-Mar-2026

Revisión de Consolidated Comment Sheets incluidos en los documentos de Entrega 18.
Documentos SIN CCS (primeras entregas): GA Antiscalant Tank, GA SIP-09-001, GA SIP-09-002.

### IO List Rev B — 7 CCS items (respondiendo TM N8)

| Item | Respuesta BW Water | Evaluación |
|------|--------------------|-----------|
| 1–4 | "HAS BEEN ADDED IN I/O LIST REV B" | ✅ Aceptable — items incorporados |
| 5 | RTDs 3 hilos conectados a módulo 5069-IY4 + DO/DI interfaz agregados | ✅ Aceptable — TE09-002/003/004/005 confirmados como 3-wire RTD |
| 6 | VFD params (Items 34–37, 115–118) + Power Meter (Items 1–11) + DO/DI interfaz | ✅ Aceptable — todo presente en IO List Rev B y DTL Rev A |
| 7 | "HAS BEEN ADDED IN I/O LIST REV B" | ✅ Aceptable |

**Gaps residuales detectados post-CCS:** TE vs TIT inconsistencia (OBS-01), relay contact specification (NOTE-01). Ambos levantados en TM N10.

### Data Transfer List Rev A — 3 CCS items (respondiendo TM N3)

| Item | Respuesta BW Water | Evaluación |
|------|--------------------|-----------|
| 1 | "HAS BEEN ADDED IN P22-LI-09-008-004A" | ✅ Aceptable |
| 2 | "HAS BEEN ADDED IN P22-LI-09-008-004A" | ✅ Aceptable |
| 5 | Power Meter, VFD params, DO/DI interfaz agregados — referencia cruzada IO List Rev B | ✅ Aceptable — documento substantivo 189 items |

**Gaps residuales detectados post-CCS:** Error copy/paste Items 22–23 (OBS-03), rangos CIT incorrectos (OBS-02). Ambos levantados en TM N10.

### Control Architecture Rev C — 8 CCS items (respondiendo TM N4)

| Item | Respuesta BW Water | Evaluación |
|------|--------------------|-----------|
| 1 | Power Meter, VFD, MOV via TCP/IP confirmado | ✅ Aceptable |
| 2 | "HAS REVISED IN CONTROL SYSTEM ARCHITECTURE REVC" | ✅ Aceptable |
| 3 | PLC standalone (sin redundancia) — per Tender Proposal | ✅ Aceptable — conforme con Technical Offer Rev1 |
| 4 | "WILL SUBMIT IN HMI DISPLAY SCREENSHOT P22-BREAD-09-008-001" | ⚠️ **Pendiente — NO entregado** → NOTE-05 TM N10 |
| 5 | IO List referencia cruzada | ✅ Aceptable |
| 6 | DTL referencia cruzada | ✅ Aceptable |
| 7–8 | "HAS ADDED IN CONTROL SYSTEM ARCHITECTURE REVC" | ✅ Aceptable |

**Gap crítico detectado:** CCS Item 4 — P22-BREAD-09-008-001 HMI Screenshots comprometido pero no entregado. Registrado como NOTE-05 en TM N10 y en §4 Pending.

### Conclusión de la Auditoría

TM N10 es técnicamente correcto en la totalidad de sus observaciones (OBS-01 a OBS-07, NOTE-01 a NOTE-04). La auditoría CCS identificó:
- **1 brecha nueva:** NOTE-05 — P22-BREAD-09-008-001 HMI Screenshots pendiente
- **4 brechas en §4:** Control Philosophy OBS detallados, Piping Layout OBS específicos, A/C Thermal Calc no estaba en §4, HMI Screenshots no estaba en §4

Todas las brechas incorporadas en TM N10 Rev 0 final (16-Mar-2026).
