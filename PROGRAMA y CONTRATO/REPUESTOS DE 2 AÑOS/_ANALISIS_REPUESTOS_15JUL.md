---
codigo: ANALISIS-REPUESTOS-2ANOS-15JUL2026
fecha: 2026-07-20
proyecto: Modulo de Salmuera Taltal — Contrato C-4300 / BAE 12803
asunto: Auditoria de la cotizacion de repuestos recomendados a 2 anos recibida el 15-Jul-2026
estado: INTERNO — NO ENVIAR
second_brain: skip
---

# Auditoria — Recommended Two-Year Spare Parts (recibida 15-Jul-2026)

> Documento interno de trabajo. No se envia a BW Water. Sustenta el correo de respuesta del 20-Jul-2026.

## 1. Que se recibio

Correo de Eduardo Yamauchi del miercoles 15-Jul-2026 15:29, respuesta al thread *"Formal Re-validation of Spare Parts Quotation C4300"*. To: Luis Rivera, Andrea Frezzi. CC: Jorge Guevara, Victor Gutierrez, Stephane Gehant. Adjunto: `Recomended 2-year spare parts.pdf` (1 pagina).

Texto integro del cuerpo, en lo sustantivo:

> *"Most of the items remain with the same price, but there are some updates in price and quantities. Please refer to the notes in the table. Solenoid valve was removed – not needed anymore as it was not used in the project."*

## 2. Cronologia del requerimiento

Cuatro meses y tres semanas desde la solicitud original; seis recordatorios de ADASA.

| Fecha | Hecho |
|---|---|
| 18-Sep-2025 | Oferta comercial BWWA Ref. 20.24.6501.F Rev.1. Lista de 2 anos declarada en USD 43.790 EXW (opcional); lista mandatoria USD 17.310 (contratada, suma alzada) |
| Jue 26-Feb-2026 15:15 | ADASA abre el thread. Pide (a) re-validacion formal de precio, alcance y condiciones comerciales **con fecha de validez actualizada**, y (b) kits de servicio de SIP-09-001 y SIP-09-002, ausentes de la lista. Plazo Vie 07-Mar |
| Jue 26-Mar-2026 | Follow-up por otra cadena (reply a las notas de reunion del 26-Mar). Plazo Mar 31-Mar |
| Mar 12-May-2026 10:13 | Recordatorio en el thread. Se suma Andrew Zaske en copia |
| Lun 25-May-2026 14:29 | Recordatorio en el thread |
| Lun 15-Jun-2026 15:39 | Recordatorio duro: *"which has now expired… this is currently holding our procurement decision"*. Plazo Vie 19-Jun |
| Mar 16-Jun-2026 | Minuta BW Water: *"Spare parts quotes / To be released next Monday"* (22-Jun). Incumplido |
| Lun 22-Jun-2026 | ADASA reclama el incumplimiento: *"1. Spare parts quotes: not included."* |
| Mar 30-Jun-2026 | Minuta BW Water: *"BW Water to submit the complete two-year spare parts package by 03-Jul-2026."* Incumplido |
| Mar 07-Jul-2026 | Accion de la weekly call con plazo Vie 10-Jul. Incumplido. El acta de BW Water lo degrada a *"waiting for final quotations from vendors"*, sin fecha |
| Lun 13-Jul-2026 | Replica de ADASA a la minuta del 07-Jul. Deadline endurecido al mismo dia, "con lo que tengan" |
| Mie 15-Jul-2026 15:29 | Se recibe la cotizacion actualizada |

Los recordatorios del 12-May, 25-May y 15-Jun no estaban documentados en el proyecto antes de esta auditoria. Se recuperaron del thread archivado en esta misma carpeta.

## 3. La valvula solenoide — punto cerrado

`Bray or Equivalent | Series 63, 120VAC | Solenoid Valve | 2 unit | USD 1.650 c/u | USD 3.300`, linea de la lista de 2 anos de la oferta (Comercial pagina 14; Propuesta Tecnica Rev.1 Seccion 15).

La Bray Series 63 es un piloto solenoide para actuadores **neumaticos**. El retiro es correcto y se acepta. Evidencia cruzada:

| Fuente | Resultado |
|---|---|
| ET P22-ET-09-000-001-0 | Cero menciones a valvulas solenoides. Nunca fue un requisito |
| Valve List P22-LI-09-005-002 Rev D (111 valvulas) | Cero solenoides. Prefijos presentes: VM manuales, VE motorizadas, VR retencion, PSV seguridad |
| IO List P22-LI-09-008-001 Rev C | Toda valvula automatica es motorizada (VE-09-xxx, 380/220 VAC, senal sobre Ethernet/IP) |
| Equipment List P22-LI-09-005-001 Rev B | Unico "solenoid" = BDS-09-001/002, bomba dosificadora *solenoid-driven metering* — es una bomba, no una valvula |
| Utility Consumption List P22-LI-09-009-001 | Sin aire de instrumentos como utilidad requerida |

No hay actuacion neumatica en el modulo, por lo que no hay nada que pilotear. Fue arrastre de plantilla desde la oferta.

**Falsos positivos descartados:** `VS-03-009 Solenoide Control CO2` pertenece al P&ID de la planta de remineralizacion 11 L/s, area 03, fuera del alcance; el "solenoid valve" del datasheet del analizador pH/ORP es un accesorio del jet cleaner Rosemount marcado *supplied by customer*.

**Consecuencia sobre otro entregable:** el Manual O&M P22-BA-09-000-012 Rev A (Codigo 3 en el transmittal N27; Rev B vence 31-Jul) instruye en su procedimiento de commissioning *"Open the corresponding solenoid valve by manually switching the knob on each solenoid valve"* y *"place their control selector switches and solenoid valve knobs in REMOTE position"*. La propia declaracion de BW Water confirma que ese pasaje es texto generico no adaptado a la planta. Entra como observacion en la revision del Rev B.

## 4. Aritmetica

| Concepto | Valor |
|---|---|
| Total declarado en la oferta Sep-2025 | USD 43.790,00 |
| **Suma real de las 22 lineas de esa misma tabla** | **USD 42.550,00** |
| **Diferencia no explicada en la oferta original** | **USD 1.240,00** |
| Total declarado 15-Jul-2026 | USD 51.224,50 |
| Suma real de las 24 lineas nuevas | USD 51.224,50 (cuadra) |
| Alza sobre el total declarado | +USD 7.434,50 / +17,0% |
| **Alza sobre la suma real** | **+USD 8.674,50 / +20,4%** |

La cifra "USD 43.790" que ADASA ha citado en toda la correspondencia desde el 26-Feb proviene de la oferta y esta sobredeclarada en USD 1.240 respecto de la suma de sus propias lineas. Debe reconciliarse antes de emitir orden de compra.

## 5. Comparacion linea por linea

Precios en USD. Δ = variacion del monto extendido. Veredicto: `OK` · `PRECIO` (alza a justificar) · `OBSOLETO` (no corresponde al equipo suministrado) · `ALCANCE` (reduccion de alcance) · `CORRESPONDENCIA` (no se identifica el equipo servido).

| # | Item | Sep-25 ext. | Jul-26 ext. | Δ | Veredicto |
|---|---|---|---|---|---|
| 1 | Set of Gaskets (LP, plastic piping), 4 set | 960 | 960 | 0 | OK — ahora especifica CUT Gasket SJP HB Black CR Rubber 1,5 mm |
| 2 | Set of Gaskets (HP), 2 set | 800 | 3.776 | **+2.976 (+372%)** | **PRECIO** — el spec sube a Spiral Wound tipo IOR, anillos Super Duplex S32507, relleno PTFE 4,5 mm (coherente con circuito 900#), pero la magnitud exige respaldo del fabricante |
| 3 | Flexible Coupling 77DX 2.5", 20 un | 3.000 | 3.000 | 0 | **CORRESPONDENCIA** — fabricante cambiado de Protec Arisawa a **Hengshui Snowate**, material SS2205 (la oferta decia *Duplex bolt & SS316 nut*). Nota del proveedor: *"Change or manufacturer, but price remains the same"*. Requiere sustento de equivalencia |
| 4 | RO Vessel Head Assembly, 1 un | 2.380 | 2.380 | 0 | OK — part no. 2081006 → 208106 (confirmar si es errata) |
| 5 | RO Vessel Head Locking Ring, 3 un | 1.920 | 1.920 | 0 | OK — part no. 4080474-1 → 400747-1 (confirmar) |
| 6 | RO Vessel Seal Set, 2 set | 1.020 | 1.460 | **+440 (+43%)** | **PRECIO** — alza **sin nota** en la tabla, a diferencia de las otras cuatro. Part no. 6100442MK → 610434-NK |
| 7 | RO Membrane Adapters, 4 un | 2.320 | 2.320 | 0 | OK — part no. 5080074 → 5008074 (confirmar) |
| 8 | SWRO High Pressure Pump, 1 set | 9.560 | 9.560 | 0 | **ALCANCE** — la descripcion pasa de *Service Kit* a *Mechanical Seal* **al mismo precio y sin nota**. Ademas conserva part no. MSD-130 cuando la bomba suministrada es **Fedco MSD-7016** (Equipment List Rev B) |
| 9 | Feed Turbocharger Service Kit KH060, 1 set | — | 1.540 | nuevo | **Cumple** lo pedido desde el 26-Feb. Falta justificar que 1 set cubre 2 anos |
| 10 | Interstage Turbocharger Service Kit KH060, 1 set | — | 1.540 | nuevo | **Cumple**. Ambos kits comparten los mismos part numbers (KH060-CBK / KH060-TBK) — confirmar que aplican a los dos turbos |
| 11 | Chemical Dosing Pump Repair Kit, 2 set | 3.560 | 3.560 | 0 | Part no. **corregido** a GMXA 1602PPT200000UA1130BEN (ProMinent real). La columna de fabricante sigue diciendo *Pulsafeeder, Prominent or Equivalent* |
| 12 | pH Sensor, 1 un | 2.060 | 2.060 | 0 | **OBSOLETO** — cotiza *Foxboro pH 10*; el instalado es **Rosemount 3900 + transmisor 1056** (Instrument List Rev E, PHIT-09-006) |
| 13 | ORP Sensor, 1 un | 2.060 | 2.060 | 0 | **OBSOLETO** — mismo caso (ORPIT-09-001A). Ademas el part no. de esta linea dice **"pH 10 (or equal)"**: errata en la propia cotizacion |
| 14 | Conductivity Sensor (toroidal), 1 un | 1.370 | 1.370 | 0 | Descripcion **corregida** a Rosemount 228 toroidal. Falta el part no. real `228-04-21-56-61-LC`; la columna de fabricante sigue en *Thornton, E+H* |
| 15 | Conductivity Sensor (contacting), 1 un | — | 858 | nuevo | **Correccion valida** — Rosemount 400. Falta el part no. real `400-13-20-LC` |
| 16 | Solenoid Valve, 2 un | 3.300 | — | **−3.300** | **Retirado — correcto** (ver Seccion 3) |
| 17 | Pressure Gauge, Monel, 2 un | 1.460 | 1.460 | 0 | **OBSOLETO** — los manometros instalados son **Wika 233.50 / 990.10 con sello de diafragma Superduplex 2507** (Instrument List Rev E, PI-09-001 a 005). Monel no corresponde al servicio de salmuera concentrada |
| 18 | 3" Lined Butterfly Valve, Bray S01-0200, 1 un | 1.350 | 4.160 | **+2.810 (+208%)** | **PRECIO** — la correspondencia es correcta: 5 valvulas DN80 con cuerpo DI y disco DI Halar Coat |
| 19 | 2.5" Lined Butterfly Valve, Asahi 57L, 1 un | 1.290 | 3.100,50 | **+1.810,50 (+140%)** | **PRECIO + CORRESPONDENCIA** — la unica valvula mariposa DN65 del modulo es VE-09-009: cuerpo y disco CE3MN, asiento F53+STL, **ANSI 900#**, motorizada. No es una valvula *lined* |
| 20 | 2" Lined Ball Valve, Asahi 57L, 1 un | 1.100 | 1.100 | 0 | **CORRESPONDENCIA** — **no existe ninguna valvula de bola DN50** en la Valve List Rev D. La unica DN50 es VM-09-064, mariposa PVC |
| 21 | 4" Plastic Butterfly Valve, Asahi 57P, 1 un | 550 | 550 | 0 | OK — 4 instaladas DN100 PVC |
| 22 | 3" Plastic Butterfly Valve, Asahi 57P, 1 un | 500 | 500 | 0 | **CORRESPONDENCIA** — **no existe mariposa DN80 en PVC**. Las DN80 son DI (5) y CE3MN (3); la unica DN80 PVC es VR-09-003, valvula de retencion |
| 23 | 2" Plastic Ball Valve, Type 21, 1 un | 240 | 240 | 0 | **CORRESPONDENCIA** — sin valvula de bola DN50 (ver linea 20) |
| 24 | 1.5" Plastic Ball Valve, TB Series, 5 un | 1.200 | 1.200 | 0 | **CORRESPONDENCIA** — solo **una** valvula DN40 de bola PVC instalada (VM-09-063, servicio CIP). Se cotizan 5 repuestos |
| 25 | 1" Plastic Ball Valve, Type 21, 5 un | 550 | 550 | 0 | OK — 8 instaladas DN25 PVC |

### Omision de cobertura

La Valve List Rev D contiene **64 valvulas de bola DN15** (34 en PVC y **30 en CE3MN**) y 10 labcocks DN8. Son, por lejos, las mas numerosas del modulo, y la lista de 2 anos **no cotiza ninguna**. Las 30 en CE3MN son ANSI 900# sobre el circuito de alta presion, distribuidas en: rechazo 2a etapa (8), bomba HP (7), rechazo 1a etapa (5), rechazo 2a etapa adicional (4), turbocharger de alimentacion (3) y alimentacion del turbo de 2a etapa (3).

### Marca de las valvulas sin declarar

La Valve List Rev D aprobada trae **248 campos "TBA"** y **ninguna marca declarada** — no aparece Bray ni Asahi en todo el documento. Las ocho lineas de valvulas de la cotizacion (USD 11.400) nombran modelos que no pueden contrastarse contra el equipo que efectivamente se instalara.

## 6. Requerimientos del 26-Feb y del 13-Jul aun no satisfechos

| Requerimiento | Origen | Estado |
|---|---|---|
| Fecha de validez de la cotizacion | 26-Feb (literal: *"provide an updated valid date"*), reiterado 15-Jun | **No entregado.** El PDF solo trae *"Date: July 15th, 2026"* |
| Confirmacion de que el alcance no cambio desde Sep-2025 | 26-Feb | **No entregado** como declaracion; el cambio *Service Kit → Mechanical Seal* apunta en sentido contrario |
| Separacion de la lista Mandatoria (USD 17.310, contratada) respecto de la Recomendada | 13-Jul | **No entregado.** El PDF solo cubre la lista de 2 anos |
| Cantidades recomendadas para dos anos de operacion | 26-Feb | **No justificado** en ninguna linea |
| Part numbers del fabricante | 26-Feb; BAE clausula 35 exige cantidad, nombre y numero de identificacion, descripcion, precio unitario y manuales | **Parcial.** Persisten *Custom Part*, *Cond Sensor*, *pH 10 (or equal)* |
| Plazo de entrega, condiciones de pago, Incoterm completo | Necesario para emitir orden de compra | **No entregado** |
| Manuales | BAE clausula 35 | **No entregados** |

## 7. Forma del documento

El adjunto no reune las condiciones minimas de un documento comercial:

| Atributo | Estado |
|---|---|
| Membrete / identidad corporativa | **Ausente.** El archivo no contiene ninguna imagen (verificado: 0 objetos de imagen) ni menciona el nombre de la empresa |
| Numero de cotizacion | Ausente |
| Referencia al Contrato C-4300 / BAE 12803 | Ausente |
| Firma y cargo del emisor autorizado | Ausente |
| Validez, moneda, Incoterm completo, plazo de entrega, condiciones de pago | Ausentes |
| Metadatos del archivo | Titulo `TALTA_UHPRO_2Y_Spare_Parts-EY.xlsx`; autor `Eduardo Yamauchi`; productor `Microsoft: Print To PDF` |

Es la impresion de una planilla de trabajo. Para ejercer la opcion de dos anos y emitir orden de compra por sobre USD 50.000, ADASA requiere una cotizacion formal emitida y firmada por la empresa.

## 8. Cierre — el punto de fondo

De las 24 lineas cotizadas, **once** presentan un defecto de correspondencia, obsolescencia o alcance frente al diseno aprobado, y **cuatro** llevan alzas de entre 43% y 372%. La solenoide es la unica que BW Water detecto por si mismo.

La conclusion operativa es que la lista sigue siendo, en lo esencial, la lista preliminar de septiembre de 2025 — la propia oferta la califica de *preliminary* — con un refresco de precios encima. Lo que ADASA pidio el 26 de febrero fue una re-validacion de alcance contra el diseno final, y el diseno se cerro despues: Equipment List Rev B, Instrument List Rev E, Valve List Rev D.

El mecanismo de correccion mas eficiente, y el que debe exigirse, es que **cada linea de la lista cite el TAG del equipo o valvula que sirve**. Esa sola condicion resuelve las once observaciones sin discutirlas una por una.

## 9. Alcance y ruta critica

La lista **mandatoria** (USD 17.310) es parte del precio base a suma alzada y debe entregarse junto con el modulo. El embarque ex-works Penang esta previsto para el 09-10 de septiembre de 2026. Sus part numbers siguen declarados como `tba` en la oferta mientras la instrumentacion real ya esta definida: transmisores de presion Schneider Foxboro IGP05S, caudalimetros Rosemount 8750W, conductividad de permeado Rosemount 400. Un repuesto que no corresponde al equipo instalado no cumple la funcion contratada.

## 10. Archivos

| Archivo | Contenido |
|---|---|
| `Recomended 2-year spare parts.pdf` | Cotizacion recibida 15-Jul-2026 |
| `md/Recomended-2-year-spare-parts_extracted.md` | Extraccion literal |
| `md/Thread-Formal-Re-validation-Spare-Parts-C4300_extracted.md` | Cadena completa de correo, 26-Feb a 15-Jul |
| `OFERTA ECONOMICA/pdf/OFERTA ECONOMICA BW WATER.pdf` paginas 11-14 | Baseline Sep-2025, ambas listas |
| `ENTREGAS_BWWATER/ENTREGA 19/P22-LI-09-005-001_REV.B Equipment List_extracted.md` | Equipos suministrados |
| `ENTREGAS_BWWATER/ENTREGA 46/md/P22-LI-09-008-003_E Instrument List_extracted.md` | Instrumentacion suministrada |
| `ENTREGAS_BWWATER/ENTREGA 38/P22-LI-09-005-002_D Valve List.pdf` | 111 valvulas, marcas TBA |
