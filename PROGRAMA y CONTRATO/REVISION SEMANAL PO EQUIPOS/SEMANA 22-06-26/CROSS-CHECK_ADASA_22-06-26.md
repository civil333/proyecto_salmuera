# Cross-check ADASA — Seguimiento Semanal BW Water (Semana 22-Jun-2026)

> Análisis overlay ADASA del paquete recibido el lunes 22-Jun (correo Yamauchi 10:45 + `Copy of Procurement tracking - BW Water 2206.xlsx` + `25007 TALTAL PROGRESS REPORT (WEEK 25).pdf` + `25007_Taltal_DDSR_2026.06.22.pdf`), cruzado contra: cronograma **VIGENTE** `Project Schedule 08-06-26` (Rev A), minuta/Meeting Notes del 16-Jun (Yamauchi), y la semana anterior (`CROSS-CHECK_ADASA_15-06-26.md`). Validado con workflow de 4 frentes + verificación adversarial entre documentos (56 de 57 hallazgos confirmados; 1 refutado, 12 corregidos). Metodología CLAUDE.md Sección 11. Días de semana verificados contra calendario.

## 1. Veredicto y resumen por clasificación

**Veredicto de la semana: 6 focos CRITICAL · 13 WARNING · 2 OK (+ notas INFO de data-quality). Determinante = Fedco.** El paquete del 22-Jun es el status report rutinario; **no movió la ruta crítica** y omitió dos compromisos de la minuta del 16-Jun que vencían hoy. El hallazgo central lo expuso el cruce entre los propios documentos de BW Water: tres fechas distintas para los equipos Fedco, la más reciente (21-Ago) posterior a la fecha de despacho del sistema.

| Clasif. | Cant. | Focos |
|---|---|---|
| **CRITICAL** | 6 | (1) Fedco completion 21-Ago — 6 d **después** del EXW Penang 14-15 Ago, vendor único de 3 equipos, reabre el conflicto FAT de NT-001; (2) HP Feed Pump BH-09-001 sigue en status D + anticipo 30% Fedco sin resolución escrita; (3) cálculo sísmico sin certificar → RO Skid y pipe spools al 0% + Stress & Flexibility de cañerías HP no emitido (vence 29-Jun); (4) spare parts quotes y ex-work shipment details (minuta 16-Jun, vencían hoy) ausentes del paquete; (5) tres planos mecánicos de ruta de instalación Not submitted, vencen 26-Jun (Maintenance Lifting Points, 3D Model, GA RO HP Pump); (6) RO Pressure Vessel — tracker EAP Penang 29-May obsoleto (~65 d off vs 02-Ago del schedule), toca el hito de pago 15% |
| **WARNING** | 13 | Tracker no reconciliado al Schedule Rev A (cabecera aún 05-Mar); 5 ítems en status E con PO ya cargada (toca pago 15%); Structural Frames status C en tracker vs RO Skid 0% en Progress Report; Super Duplex retrasado en taller (ETA Ann Aik 26-Jun); CIP/Flushing Pumps Grundfos EAP "TBC" pese a completion 1-Sep; ITP RO PV Rev D Approved As Noted (waiver ASME ya concedido) con evidencia de ensayo + tabla FAT/SAT pendientes; CIP Cartridge Filter Rev E en Revise & Resubmit (gasket pH 2-12); Equipment/Tie-In/GA Turbos en Revise & Resubmit (vencen 26-Jun); Shipping Plan Not submitted (vence 25-Jun) + hold-point pre-despacho; Project Schedule Rev B Approved As Noted (re-emisión 25-Jun); ingeniería 86% (DDSR) vs cierre declarado; RO Membranes LG con 3 referencias de fecha/ruta sin conciliar; GA CIP Tank Not submitted |
| **OK** | 2 | Container 40FT + AC (Pacific): procurement 100% cerrado y consistente; Antiscalant Dosing Tank + Pumps entregados (recibidos en BW Prai). Static Mixer arribado a Penang (16-Jun) |

## 2. Top-3 alertas

1. **Fedco completa 21-Ago, DESPUÉS del EXW Penang 14-15 Ago — choque de ruta crítica.** El Progress Report W25 y la minuta del 16-Jun declaran completion de los tres equipos Fedco (HP Feed Pump BH-09-001, Feed Turbo SIP-09-001, Interstage Turbo SIP-09-002) el **21-Ago**. El Schedule Rev A fija manufacturing finish Fedco **09-Ago**, instalación de la RO Feed Pump 10-11 Ago y system ready-to-ship / EXW Penang **14-15 Ago**: el 21-Ago llega 12 d después del finish y 6 d después del despacho — la pieza llegaría cuando el sistema ya debía estar a bordo. Reabre el conflicto FAT de NT-001 (ventana de running test integrado ahora negativa). BW Water califica el 21-Ago de "unacceptable" y declara que está expeditando, sin fecha mejorada confirmada. El tracker, en cambio, mantiene EAP Penang **05-Ago** (desfasado 16 d) y BH-09-001 en status D. **Acción:** exigir por escrito antes de la reunión semanal (a) una fecha única conciliada de Fedco con respaldo de vendor (carta/OC, no "estimate"); (b) confirmar si el running test del HP Pump + turbos se ejecuta en Penang o pasa a SAT en sitio (NT-001 3.C/3.D), con plan de personal, ventana y costo SAT a cargo BW Water; (c) cronograma re-secuenciado que demuestre cómo se absorbe el slip sin pasar el fin del Performance Test (16-Nov baseline). **Deadline:** confirmación escrita antes de la reunión semanal; hito gobernado EXW Penang 14-15 Ago.

2. **Sísmico sin certificar y Stress & Flexibility no emitido congelan skid y spools.** La minuta del 16-Jun declara el cálculo sísmico (a certificar por un PE en Chile) "aún en progreso" y lo califica de riesgo sobre el diseño y la fabricación de spools. El Progress Report W25 lo confirma: RO Skid (Mild Steel Structure) procurement 0% "Pending for PR/PO, confirmation on seismic calculation", Fabrication Skid Structure 0% y Pipe Spool 0%. En paralelo, el Stress & Flexibility analysis for High Pressure Pipes (P22-CD-09-005-001) figura **Not submitted**, vence el lunes 29-Jun. Dos insumos de ingeniería de los spools abiertos cuando la fabricación debía avanzar; el tracker, no obstante, declara Structural Frames status C con target ready 01-Jul sin respaldo. **Acción:** exigir fecha firme de emisión del sísmico certificado y el alcance de la liberación parcial para fabricar que BW Water mencionó; condicionar la fabricación de spools HP a la aprobación del Stress & Flexibility (29-Jun) más el sísmico; pedir el estado real de la PR/PO del RO Skid y reclasificar su status del tracker. **Deadline:** Stress & Flexibility lunes 29-Jun; target frame 01-Jul.

3. **Compromisos de la minuta del 16-Jun incumplidos hoy + entregables mecánicos sin primera emisión (vencen 26-Jun).** El paquete recibido hoy (cuerpo genérico "project status report") **no contiene** las spare parts quotes ni los ex-work shipment details comprometidos en la minuta para "next Monday" (= 22-Jun): ambos missed, con el RO PV en ex-works España programado para mañana 23-Jun sin detalle de embarque sobre la mesa. Además, el DDSR lista tres planos mecánicos de ruta de instalación **Not submitted** que vencen el viernes 26-Jun — Maintenance Lifting Points (P22-DWG-09-005-006), 3D Model (P22-DWG-09-005-007) y GA of RO HP Pump (P22-DWG-09-005-009, equipo Fedco en ruta crítica) — más el GA CIP/Flushing Tank (-014); el Shipping Plan (P22-BA-09-000-002) sigue Not submitted (vence 25-Jun). **Acción:** reclamar por correo la entrega inmediata de las spare parts quotes y los ex-work shipment details, dejando registro del incumplimiento de la minuta, y vincular los ex-work details al Shipping Plan; exigir fecha firme de envío de los planos Not submitted, priorizando GA HP Pump y Lifting Points (insumos de la instalación en contenedor 10-11 Ago y del pre-assembly Penang 7-Jul). **Deadline:** quotes y ex-work details inmediato (vencidos hoy); planos mecánicos viernes 26-Jun; Shipping Plan jueves 25-Jun.

## 3. Compromisos de la minuta del 16-Jun — estado al lunes 22-Jun

| Compromiso (minuta 16-Jun) | Vencía | Estado | Evidencia |
|---|---|---|---|
| Spare parts quotes "to be released next Monday" | lun 22-Jun | **Incumplido** | No en el paquete del 22-Jun (correo 10:45 + tracker + Progress Report W25 + DDSR); cuerpo solo dice "project status report" |
| Ex-work shipment details "to be released next Monday" | lun 22-Jun | **Incumplido** | No incluido ni mencionado; crítico porque el RO PV tiene ex-works España el 23-Jun y el Shipping Plan sigue Not submitted (vence 25-Jun) |
| Fabrication schedule status report cada lunes | recurrente (1.º = 22-Jun) | **Parcial** | Llegó Progress Report W25 (% de avance) + DDSR, pero ninguno es un *fabrication schedule* con fechas; el Project Schedule sigue Rev B (re-emisión planeada 25-Jun) |
| Columna extra "material received status at workshop" | a integrar desde 22-Jun | **Parcial** | El Progress Report W25 tiene una sección "MATERIAL ARRIVAL – STATUS / REMARKS"; el Project Schedule Rev B aún no la incorpora como columna |
| Fedco: asegurar fecha anterior al 21-Ago (expediting) | en curso | **Abierto** | Declarado "unacceptable" + "expediting"; sin fecha mejorada confirmada al 22-Jun |
| Seismic calculation: completar "soonest possible", cert. PE Chile | en curso | **Abierto** | Sigue "in progress"; bloquea RO Skid (0%) y spools (0%) |
| Invoice status update (BWW to provide) | en curso | **Abierto** | No incluido en el paquete del 22-Jun |
| Super Duplex "expected to arrive next week" | sem. 22-Jun | **En seguimiento** | Progress Report: "material delayed to arrive at vendor's shop; estimate arrival to Ann Aik on 6/26" |

## 4. Bottleneck — Fedco (vendor único, 3 equipos en ruta crítica)

HP Feed Pump (BH-09-001) + Feed Turbo (SIP-09-001) + Interstage Turbo (SIP-09-002), todos Fedco, concentrados sobre el cierre del FAT. Tres fechas BW Water distintas para el mismo equipo: **EAP tracker 05-Ago / Progress Report 21-Ago / Schedule Rev A 09-Ago**. La más reciente (21-Ago) cae 6 días después del EXW Penang 14-15 Ago. BH-09-001 sigue en status D (la propia legend del tracker obliga escalación a Fadey Kassim en 24 h) y el anticipo 30% que Fedco impuso el 26-May —que ADASA rechazó como causal de atraso propio (BAE Cl.27/31/32/35/46)— no tiene confirmación escrita de resolución. Mientras no exista fecha Fedco anterior a la ventana de instalación Penang (10-11 Ago), el riesgo de ruta crítica permanece abierto y empeoró respecto al 15-Jun (donde la ventana ya era de solo 6 días). La posición ADASA sobre el anticipo está fijada y no se reabre: se exige su resolución a costo BW Water.

## 5. Estado documental con vencimiento esta semana (DDSR 22-Jun)

| Documento | Rev | Status | Vence | Nota |
|---|---|---|---|---|
| CIP Cartridge Filter datasheet (P22-ET-09-009-006) | E | Revise & Resubmit | mar 23-Jun | Re-emitir corrigiendo gasket pH 2-12 (Code 3 TM N22) |
| PLC/LCP Outline Panel Drawing (P22-CD-09-008-001) | B | Revise & Resubmit | mié 24-Jun | Gate de la contradicción enclosure SS316L NEMA4X/IP66 vs sheet steel IP55 (TM N20) |
| Project Schedule (P22-BA-09-000-001) | B | Approved As Noted | jue 25-Jun | Re-emisión: incorporar columna "material received" + fabrication schedule (minuta) |
| Shipping Plan (P22-BA-09-000-002) | A | **Not submitted** | jue 25-Jun | 0%; ligado a los ex-work shipment details no entregados |
| Equipment Layout (P22-DWG-09-005-003) | D | Revise & Resubmit | vie 26-Jun | RO cartridge filter horizontal vs datasheet vertical (NT-001 5.C); gatea Instrument Location Layout |
| Tie-In Point Layout (P22-DWG-09-005-005) | B | Revise & Resubmit | vie 26-Jun | Interfaz ADASA-módulo abierta desde marzo (>100 d) |
| Maintenance Lifting Points (P22-DWG-09-005-006) | A | **Not submitted** | vie 26-Jun | Sin primera emisión; insumo de montaje |
| 3D Model (P22-DWG-09-005-007) | A | **Not submitted** | vie 26-Jun | Soporta verificación de interferencias pre-ensamblaje |
| GA of RO HP Pump (P22-DWG-09-005-009) | A | **Not submitted** | vie 26-Jun | Equipo Fedco en ruta crítica; insumo install contenedor 10-11 Ago |
| GA 1st/2nd Stage Turbo (P22-DWG-09-005-012/-013) | B | Revise & Resubmit | vie 26-Jun | Equipos Fedco; abiertos desde marzo |
| GA CIP/Flushing Tank (P22-DWG-09-005-014) | A | **Not submitted** | vie 26-Jun | Sin primera emisión |
| Stress & Flexibility HP Pipes (P22-CD-09-005-001) | A | **Not submitted** | lun 29-Jun | Insumo directo de los spools (Fab 0%) |
| ITP RO PV (P22-BA-09-000-004) | D | Approved As Noted | 26-Jun (submittal) | Documenta la base del waiver ASME (concedido 02-Jun); falta evidencia de ensayo |
| Plant Control Philosophy (P22-BT-09-009-001) | E | Revise & Resubmit | 6-Jul | 6.º ciclo; carry-forward vivo |

Registro DDSR 22-Jun: 76 documentos, 86% de avance ponderado. **El propio dashboard es internamente inconsistente** (dashboard: 9 Not submitted / 8 Revise & Resubmit / 8 Submitted; conteo fila a fila del mismo archivo: 6 / 11 / 5) — pedir versión reconciliada.

## 6. Variances y contradicciones de fechas entre documentos BW Water

- **Fedco (3 equipos):** completion 21-Ago vs manufacturing finish Rev A 09-Ago = slip ~12 d, y 6 d después del EXW Penang. Tres fechas para el mismo equipo (EAP tracker 05-Ago / Progress 21-Ago / Schedule 09-Ago).
- **RO Pressure Vessel (Protec Arisawa):** EAP Penang tracker 29-May (fecha pasada) vs arribo Penang Schedule Rev A 02-Ago = ~65 d off; tracker no reconciliado a la ruta post-ASME (ex-works España 23-Jun + 40 d mar).
- **Tie-In Point Layout (P22-DWG-09-005-005) Rev B:** Revise & Resubmit desde 6-Mar / 12-Mar, vence 26-Jun = >100 d de interfaz sin cerrar.
- **GA Turbos 1.ª/2.ª etapa (P22-DWG-09-005-012/-013) Rev B:** Revise & Resubmit desde marzo, vence 26-Jun = ~3 meses.
- **CIP Cartridge Filter:** EAP/completion tracker-Progress ~20-21 Jul vs Schedule Rev A finish 13-Ago = ~3 semanas de discrepancia para el mismo ítem.
- **RO Membranes (LG):** la fila se contradice (header "Estimate Arrival Penang" 03-Ago vs comentario "Direct delivery to Taltal on 3/8"); Progress 7/30; Schedule arribo 19-Ago. Tres referencias, destino ambiguo (Penang para FAT vs directo a Taltal).
- **Static Mixer / Antiscalant:** Actual Arrival Penang 16-Jun (tracker) vs 15-Jun (Progress); Dosing Tank 11-May vs 12-May; Dosing Pump 27-Abr vs 23-Abr — diferencias menores entre fuentes.

## 7. Notas operativas (data quality)

1. **Tracker casi estático vs 15-Jun:** línea por línea idéntico en status/PO Date/EAP/comentarios salvo Static Mixer (item 17, gana Actual Arrival Penang 16-Jun + "Received in Penang workshop"). A ~54 días del EXW Penang 15-Ago, un tracker estático semana a semana no es instrumento de monitoreo confiable.
2. **Baseline del tracker desactualizado:** la cabecera mantiene "Baseline: Schedule issued 05-Mar-2026" y la columna "Baseline PR/PO Window" referida a ese baseline antiguo, sin incorporar el Schedule Rev A (08-Jun) vigente. Exigir reconciliación a Rev A o declaración explícita de varianza.
3. **Status "E" con PO ya cargada (5 ítems):** Instrument Set (PO 29-Abr), RO Cartridge Filter (10-Jun), CIP Cartridge Filter (10-Jun), CIP/Flushing Pumps (13-May), PLC Panel (12-May). El status contradice el dato; **bloquea certificar OCs confirmadas para el pago 15% (EP-2)**. Pedir aclaración binaria por ítem.
4. **Structural Frames** declarado status C (PO emitida) en el tracker mientras el Progress Report lo da 0% "Pending for PR/PO": reclasificar.
5. **CIP/Flushing Pumps (Grundfos):** EAP "TBC" en tracker pese a que el Progress Report da completion 1-Sep; cargar la fecha y confirmar status.
6. **Static Mixer:** PO Date 2025-05-06 (año 2025) = typo arrastrado desde 15-Jun; debería ser 2026-05-06.
7. **Super Duplex (Ann Aik):** tracker da EAP 26-Jun sin comentario mientras el Progress Report aclara "material delayed to arrive at vendor's shop" — el 26-Jun es arribo al vendor, no fin de fabricación. Distinguir ambos en el tracker.
8. **Avance en Penang 0%** (Skid Structure, Pipe Spool, todo el Assembly, Hydrotest, Final Dimension/Inspection, Punch List, Packing); solo Container modification 50%. El ensamblaje + FAT (24-Jul a 13-Ago) se apoyan en arribos de fin de julio/agosto sin holgura; pedir el plan de secuencia de ensamblaje contra fechas de arribo reales.

## 8. Lectura ejecutiva

A ~54 días del EXW Penang (15-Ago, dentro de tolerancia Cl.27 tal como está dibujado: +12 d vs baseline 05-Mar, −1 d vs Recovery 22-May), la conformidad del cronograma es **condicional a la recuperación de Fedco**: el dato más reciente del propio proveedor (21-Ago) cae después del despacho y, de no recuperarse, empuja el EXW a ~25-Ago y el fin del Performance Test a ~17-Nov, consumiendo el margen contra el 16-Nov baseline. El segundo gate es físico e inmediato: sin el sísmico certificado y el Stress & Flexibility emitido, el RO Skid y los spools no arrancan (0% al 22-Jun) con el FAT iniciando el 24-Jul. El paquete del 22-Jun no atendió ninguno de los dos frentes ni los compromisos de la minuta que vencían hoy; el tracker sigue siendo un instrumento de monitoreo poco confiable (estático, baseline desactualizado, status ambiguos que tocan el pago del 15%). La acción de la semana es contractual y de fecha: exigir por escrito, antes de la reunión semanal, la fecha Fedco conciliada con respaldo de vendor, el cierre del sísmico certificado y la entrega de los compromisos pendientes (spare parts quotes, ex-work shipment details, planos mecánicos del 26-Jun).

---

*Fuentes: `tracker_22-06-26.md`, `25007_Taltal_DDSR_2026.06.22_extracted.md`, `25007 TALTAL PROGRESS REPORT (WEEK 25)_extracted.md`, `MINUTA DE REUNION 16-06-26_extracted.md`, `Project Schedule 08-06-26_extracted.md`, `Bandeja de entrada... Outlook_extracted.md`, `CROSS-CHECK_ADASA_15-06-26.md`, NT-001, respuesta ADASA 01-Jun. Validación: workflow `cross-check-bwwater-22jun` (62 agentes, 4 frentes + verificación adversarial, 56/57 hallazgos confirmados).*
