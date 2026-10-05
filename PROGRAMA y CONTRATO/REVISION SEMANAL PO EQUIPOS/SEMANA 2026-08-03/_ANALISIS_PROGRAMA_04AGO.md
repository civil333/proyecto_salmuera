---
titulo: Analisis de programa y procurement — paquete semanal del 03-Ago-2026
proyecto: salmuera-taltal
fecha: 2026-08-04
autor: Luis Rivera Gonzalez (ADASA)
estado: INTERNO — insumo de trabajo, no se envia
second_brain: skip
---

# Análisis de programa — corte martes 04-Ago-2026

> Documento interno de trabajo. Consolida el paquete semanal del 03-Ago, la minuta del 04-Ago, el cronograma del 04-Ago y la respuesta de Fedco. Los dos informes de diff (`DIFF_TRACKERS.md` y `DIFF_FABRICATION_SCHEDULE.md`) son el insumo base y no se reproducen aquí.

**Titular.** El hito Ready to Ship (EXW Penang) no es solo una linea base de cronograma: es el Plazo de Entrega de la Cláusula 27 de las BAE (300 días corridos desde la Notificación de Adjudicación del 07-Oct-2025 = lunes 03-Ago-2026). Vencio ayer. La fecha vigente que el propio cronograma de BW Water proyecta es 19-21 de septiembre, con lo que la multa de la Cláusula 43.1 letra b (0,2% diario del valor neto) corre desde hoy y, de materializarse el 21-Sep, acumularia 49 días equivalentes a 9,8% del valor neto del contrato, sobre un tope global de 15%.

---

## 1. Fuentes leidas

| Documento | Ruta `.md` (o `.xlsx` leido directo) | Fecha del documento |
|---|---|---|
| Diff del Procurement Tracking (13-Jul → 03-Ago) | `PROGRAMA y CONTRATO\REVISION SEMANAL PO EQUIPOS\SEMANA 03-08-26\DIFF_TRACKERS.md` | generado 04-Ago-2026 |
| Diff del Fabrication Schedule (01-Jul → 03-Ago) | `PROGRAMA y CONTRATO\REVISION SEMANAL PO EQUIPOS\SEMANA 03-08-26\DIFF_FABRICATION_SCHEDULE.md` | generado 04-Ago-2026 |
| Progress Report Week 31 | `...\SEMANA 03-08-26\md\25007 TALTAL PROGRESS REPORT (WEEK 31)_extracted.md` | periodo 27-Jul a 02-Ago-2026 |
| Progress Report Week 30 | `...\SEMANA 27-07-26\md\25007 TALTAL PROGRESS REPORT (WEEK 30)_extracted.md` | periodo 20-Jul a 26-Jul-2026 |
| Progress Report Week 29 | `...\SEMANA 20-07-26\md\25007 TALTAL PROGRESS REPORT (WEEK 29)_extracted.md` | periodo 14-Jul a 20-Jul-2026 |
| Progress Update (cronograma MS Project) | `PROGRAMA y CONTRATO\PROGRAMA DE MITIGACION\md\2026-08-04_TALTAL Water Treatment Plan Project _Progress Update_extracted.md` | impreso 04-Ago-2026 |
| Progress Update (cronograma MS Project) | `...\SEMANA 27-07-26\md\2026-07-27_TALTAL Water Treatment Plan Project _Progress Update_extracted.md` | impreso 27-Jul-2026 |
| Meeting Notes weekly call | `...\SEMANA 27-07-26\md\25007 Project Taltal - Weekly Coordination Call - Meeting Notes, schedule, and reports - 28_extracted.md` | martes 28-Jul-2026, 09:38 |
| Minuta weekly call | `MINUTAS DE REUNION\md\MINUTA DE REUNION 04-08-26_extracted.md` | martes 04-Ago-2026, 09:31 |
| Minuta weekly call | `MINUTAS DE REUNION\md\MINUTA DE REUNION 07-07-26 (OFICIAL BWWATERS)_extracted.md` | martes 07-Jul-2026, 16:13 |
| Minuta weekly call | `MINUTAS DE REUNION\md\MINUTA DE REUNION 30-06-26_extracted.md` | martes 30-Jun-2026, 10:23 |
| Fedco Manufacturing Schedule R5 | `PROGRAMA y CONTRATO\RESPUESTA DE FEDCO\md\19554 BW Water - Manufacturing Schedule R5_extracted.md` | cover sheet sin fecha de R5; última rev listada 04 = 10-Jul-2026 |
| Cadena de correo Fedco (Burton → BW Water → ADASA) | `PROGRAMA y CONTRATO\RESPUESTA DE FEDCO\md\Bandeja de entrada_ Luis Rivera Gonzalez - Outlook_extracted.md` | martes 04-Ago-2026, 08:24 |
| DDSR (Document and Drawing Status Report) | `...\SEMANA 20-07-26\md\25007_Taltal_DDSR_2026.07.20_extracted.md` | 20-Jul-2026 |
| Procurement tracking (hojas Weekly Dashboard, Milestone Tracker, Change Log) | `...\SEMANA 03-08-26\Copy of Procurement tracking - BW Water 2906.xlsx` | versión del 03-Ago-2026 |
| Fabrication schedule (hoja `RO system`) | `...\SEMANA 03-08-26\Fabrication schedule.xlsx` | versión del 03-Ago-2026 |
| Recovery Schedule del 14-Jul (verificación puntual de hitos) | `...\SEMANA 13-07-26\md\2026-07-14_TALTAL Water Treatment Plan Project _Progress Update_extracted.md` | impreso 14-Jul-2026 |
| BAE 12803, Cláusulas 27, 37, 43.1 y 43.4 (verificación contractual) | `BASES TECNICAS\md\BAE-12803-PLANTA-MODULAR.md` | documento contractual |

La raiz de las rutas abreviadas con `...` es `C:\SynologyDrive\SynologyDrive\DESAROLLO PROYECTOS CLAUDE\MODULO DE SALMUERA TALTAL\PROGRAMA y CONTRATO\REVISION SEMANAL PO EQUIPOS`.

---

## 2. Hechos nuevos

### 2.1 El hito Ready to Ship coincide exactamente con el Plazo de Entrega contractual

La Cláusula 27 de las BAE 12803 dice: *"El Plazo de Entrega para el modulo RO de segunda etapa para salmuera, en las condiciones descritas en las Bases de Licitacion, sera de maximo 300 dias corridos contados desde la emision de la Notificacion de Adjudicacion por parte de ADASA"*, y agrega que *"El Plazo de Entrega sera firme y constituye una condicion esencial para el cumplimiento del Contrato"*.

El cronograma de BW Water fija `Contract Award / NTP` el 07-Oct-2025 (martes). Sumados 300 días corridos, el vencimiento cae el **lunes 03-Ago-2026**, que es exactamente la `Baseline Date` que la hoja `Milestone Tracker` asigna al hito `Ready to Ship (EXW Penang)` (celda B5 = "3 Aug 2026"). La coincidencia no es casual: el hito de embarque del tracker es la fecha contractual.

### 2.2 La fecha de embarque vigente es 19-21 de septiembre, y ya venia del paquete anterior

El cronograma del 04-Ago, tarea ID 416 `System ready to ship(Ex-work-Penang, Malaysia)`, trae `Baseline1` 14-Ago a 15-Ago-2026 y `Projected` **19-Sep (sabado) a 21-Sep (lunes)**. El cronograma del 27-Jul trae, en la misma tarea, exactamente las mismas fechas proyectadas. El movimiento no ocurrio esta semana; entro con el paquete del 27-Jul.

Las meeting notes del martes 28-Jul lo declaran por escrito, bajo el titulo `Schedule Update`: *"Overall shipment readiness moved to 21-Sep-2026. Primary driver is piping fabrication and assembly sequencing. Team believes recovery is possible through schedule optimization."*

### 2.3 Fedco confirma por escrito el 21-Ago y entrega el Manufacturing Schedule R5

Correo de Lester Burton (Senior Project Engineer, Fedco) del martes 04-Ago-2026 01:47, reenviado por Eduardo Yamauchi a ADASA a las 08:24 del mismo dia: *"In summary, no delays or issues have been raised, and we are on track for the previously estimated ship date of 8/21. Motor was delivered to FEDCO today (8/3). Most all manufacturing is complete, with next steps being installation of vibration sensor mounts and equipment assembly."*

El texto de traspaso de Yamauchi es de una sola linea: *"I would like just to keep you updated on FEDCO's latest information. They informed that was delivered yesterday and they are on track for delivery on 8/21."*

### 2.4 El motor llego a Fedco el lunes 03-Ago

Es el hecho físico mas relevante de la semana en la ruta critica de equipos. El Manufacturing Schedule R5 lo registra como tarea 10, `Long-lead Orders (Motor)`, del 10-Jun al lunes 03-Ago-2026, al 100%. La minuta del 04-Ago lo confirma: *"FEDCO package confirmed receipt of the motor and remains committed to 21 August delivery."* El motor era el gatillante del bloqueo declarado en la minuta del 07-Jul (*"Still waiting for Fedco to issue the revised motor drawings and confirm the delivery date... Escalation to higher management is required immediately"*).

### 2.5 Primera inspección de taller ejecutada el 28-Jul; segunda fijada para el viernes 07-Ago

Meeting notes del 28-Jul: *"First inspection took place today in Penang (28-Jul-2026). Witness PMI completed. Next inspection: 07-Aug, for PT and spools dimensional check."* La minuta del 04-Ago la ratifica: *"Friday inspection on track – pipe spool in-progress fabrication inspection"*, y agrega dos jornadas nuevas: *"Two days, Aug 12 and 13. Hydro test for low pressure and high-pressure piping. Structure frame surface preparation."*

### 2.6 Arranco la fabricación de la estructura y de los spools

El Progress Report Week 31 registra `Fabrication - Skid Structure` en 25% con fecha de inicio 01-Ago-2026 (sabado) y `Fabrication - Pipe Spool` en 10% con inicio 29-Jul-2026 (miercoles). Ambas venian en 0% en las semanas 29 y 30. La minuta del 04-Ago lo confirma: *"Frame fabrication has started and is expected to be completed early next week. Super Duplex pipe spools fabrication started, beveling and grinding ongoing."*

### 2.7 Equipos recibidos en Penang durante la semana

- `CIP / Flushing Pumps` (BH-09-002, NTK): llegada real 28-Jul-2026 (martes), contra una estimacion que el tracker mantuvo en 01-Sep durante cuatro versiones consecutivas. Adelanto real de 35 días.
- `Structural Frames / Supports`: llegada parcial 31-Jul-2026 (viernes). El tracker aclara *"Partial material arrived in Penang workshop. Pending for SHS 50x50x5t and Angle Bar 75x5t"*, y el Week 31 dice que el saldo llega el 04-Ago (hoy).

### 2.8 Membranas RO con entrega directa a Taltal

El Weekly Dashboard, item 19, comenta: *"Direct delivery to Taltal on 3/8"*, con `Estimate Arrival Penang` 03-Ago-2026. Las membranas no pasan por Penang y por lo tanto quedan fuera del FAT atestiguado. La minuta del 04-Ago deja el `Packing list of membranes` como pendiente, sin responsable ni fecha.

### 2.9 BW Water anuncia una Change Order por cambios de ingeniería en el area CIP

Minuta del 04-Ago, bajo `Pending items`: *"Change order – Engineering changes (CIP area)"*. Es la primera mencion en el material revisado. No hay monto, alcance ni fundamento documental.

---

## 3. Cambios respecto del 25-Jul

| Frente | Estado al 25-Jul | Estado al 04-Ago | Lectura |
|---|---|---|---|
| EXW Penang | 09-10 Sep (Recovery Schedule 14-Jul, declarado referencia fija por ADASA) | 19-21 Sep (cronogramas 27-Jul y 04-Ago; meeting notes 28-Jul) | Slip de 10 a 11 días sobre una referencia que ADASA declaro inamovible |
| FAT | Banda 07-12 Sep base, desplazamiento probable a 14-19 Sep | 07-Sep a 18-Sep, 11 días corridos | La ventana cubre ambas bandas comunicadas a Bureau Veritas, pero deja de ser una banda de 6 días |
| Llegada a sitio | 26-Oct | 13-Nov | +18 días |
| Performance Test | 10-15 Dic | 29-Dic a 02-Ene-2027 | +18 días; cruza el cambio de ano |
| Fedco (bomba HP + 2 turbos) | Llegada estimada a Penang ~02-Sep, status D | 02-Sep confirmado; motor recibido 03-Ago; Fedco ratifica embarque 21-Ago | Consolidacion favorable, la unica de la semana |
| Panel PLC | A taller BW ~23-Ago | 23-Ago sin cambios (tracker y cronograma) | Estable; el tracker declara fin de fabricación 14-Ago y el cronograma 09-Ago |
| Reporte de causa raiz Fedco | Exigido por ADASA el 29-Jun con plazo viernes 03-Jul | Sin entregar | 32 días de mora |
| DDSR | Última emisión 20-Jul | Ausente en los paquetes del 27-Jul y del 03-Ago | Dos semanas consecutivas sin reporte de estado documental |

Movimientos silenciosos detectados en el cronograma entre el 27-Jul y el 04-Ago, ninguno declarado:

- `Engineering` (ID 4): fin proyectado 05-Ago → 12-Ago (+7 días), manteniendo 96% de avance. La duracion pasa de 217 a 222 días.
- `Mechanical` (ID 71): fin proyectado 05-Ago → 12-Ago (+7 días).
- `All Valve` motorizadas, manuales y PVC (IDs 321, 325, 329): `Shipping` termina 04-Ago → 15-Ago (+11 días), con la duracion estirada de 7 a 10 días.
- `RO Membrane` (ID 217): fin proyectado 19-Ago → 22-Ago (+3 días).
- `Pre-Assembly / Installation at Penang Workshop` (ID 404): el inicio se corre de 31-Jul a 08-Ago (+8 días) mientras el fin se mantiene en 18-Sep, comprimiendo la duracion de 43 a 36 días.

El último punto merece nombre propio: la fecha de embarque del 21-Sep se sostiene comprimiendo duraciones, no recuperando trabajo. La misma mecánica aparece en el FAT, que pasa de 15 días en la linea base a 14 en el Recovery del 14-Jul y a 11 en los cronogramas del 27-Jul y del 04-Ago.

---

## 4. Compromisos y fechas

| Compromiso | Obligado | Fecha comprometida | Origen de la fecha | Fuente contractual | Estado | Criterio de cierre | Evidencia |
|---|---|---|---|---|---|---|---|
| Plazo de Entrega del modulo (EXW Penang) | BW Water | lunes 03-Ago-2026 (300 días corridos desde NTP 07-Oct-2025) | CONTRACTUAL | BAE Cláusula 27 — Plazos de Ejecución del Pedido | INCUMPLIDO, 1 dia de mora al 04-Ago | Hito Ready to Ship ejecutado y Release for Dispatch liberado | `Milestone Tracker` B5 "3 Aug 2026"; sin `Actual` real |
| Recepcion Provisional dentro del Plazo Contractual | BW Water | lunes 01-Mar-2027 (510 días corridos desde NTP) | CONTRACTUAL | BAE Cláusula 27 | EN RIESGO | Acta de Recepcion Provisional | Performance Test proyectado al 02-Ene-2027, margen de 58 días |
| Aviso escrito de pruebas con inspección de terceros, suministro internacional | BW Water | 30 días de antelacion | CONTRACTUAL | BAE Cláusula 37, cuerpo (antes de 37.1) | INCUMPLIDO de forma reiterada | Notificación formal H/W con 30 días | Jornadas del 12 y 13-Ago avisadas el 04-Ago = 8 días |
| Aviso escrito de pruebas, regla general | BW Water | 10 días de antelacion | CONTRACTUAL | BAE Cláusula 37, cuerpo | INCUMPLIDO para el 07-Ago si se cuenta desde el 04-Ago | Confirmación escrita | Minuta 04-Ago; el 07-Ago ya se había anunciado el 28-Jul, que si cumple los 10 días |
| Reporte formal de causa raiz Fedco, con secuencia de eventos y acciones de recuperacion | BW Water | viernes 03-Jul-2026 | FIJADA ADASA | Correo ADASA del 29-Jun-2026 | INCUMPLIDO, 32 días de mora | Reporte en formato informe con los 4 contenidos exigidos | Ningun documento del paquete 03-Ago lo contiene; el R5 es un cronograma |
| Embarque de bomba HP y 2 turbochargers desde fabrica Fedco | BW Water / Fedco | viernes 21-Ago-2026 | COMPROMISO ESCRITO BW | Correo Yamauchi 04-Ago 08:24; Manufacturing Schedule R5, tarea 28 `Shipment Ready` | VIGENTE | AWB emitido y packing list entregado | R5 al 89% en `Production`; motor recibido 03-Ago |
| Llegada de los tres equipos Fedco a Penang | BW Water | miercoles 02-Sep-2026 | COMPROMISO ESCRITO BW | Weekly Dashboard items 1, 12 y 16; cronograma IDs 224, 228 y 232 | VIGENTE, con contradiccion interna | Recepcion en taller Penang registrada | El comentario del propio tracker declara fin de fabricación el 31-Ago |
| Fecha de embarque EXW Penang | BW Water | 09-10 Sep-2026 | FIJADA ADASA | Recovery Schedule del 14-Jul declarado referencia fija e inamovible | SUPERADA por el proveedor sin acuerdo | Reprogramación aceptada por escrito por ADASA o cumplimiento | Cronograma 04-Ago ID 416 = 19-21 Sep |
| Shipment readiness | BW Water | lunes 21-Sep-2026 | COMPROMISO ESCRITO BW | Meeting notes 28-Jul, bloque `Schedule Update`; cronograma ID 416 | DECLARADO, NO ACEPTADO por ADASA | Aceptacion formal de ADASA o recuperacion al 09-10 Sep | Ausente de la minuta del 04-Ago |
| Entrega de valvulas en Penang | BW Water | jueves 06-Ago-2026 | COMPROMISO VERBAL-MINUTA | Minuta 04-Ago *"Valve delivery moved to 6 August"*; tracker items 3, 4 y 5 | VIGENTE, con contradiccion interna | Recepcion en taller | El cronograma pone la llegada el 15-Ago |
| Entrega del CIP / Flushing Tank | BW Water | miercoles 26-Ago-2026 | COMPROMISO VERBAL-MINUTA | Minuta 04-Ago *"Flushing tank delayed to 26 August"*; tracker item 10 | VIGENTE, con contradiccion interna | Recepcion en taller | Meeting notes 28-Jul decian 03-Sep con llegada 05-Sep; el cronograma del 04-Ago aun dice 05-Sep |
| Entrega del panel PLC al taller de Penang | BW Water | domingo 23-Ago-2026 | COMPROMISO ESCRITO BW | Tracker item 21; cronograma ID 358 | VIGENTE | Recepcion en taller | Fin de fabricación: 14-Ago según el tracker, 09-Ago según el cronograma |
| Inspección de fabricación de spools en curso | BW Water | viernes 07-Ago-2026 | COMPROMISO VERBAL-MINUTA | Meeting notes 28-Jul; minuta 04-Ago | VIGENTE | Correo formal de confirmación emitido por BW Water | *"Send email confirming Friday's inspection"* |
| Inspección de prueba hidrostática LP y HP, y preparacion de superficie de la estructura | BW Water | miercoles 12 y jueves 13-Ago-2026 | COMPROMISO VERBAL-MINUTA | Minuta 04-Ago | VIGENTE, aviso insuficiente | Notificación formal H/W | 8 días de aviso contra los 30 de la Cláusula 37 |
| Calendario semanal de inspecciones para que ADASA coordine inspectores | BW Water | semanal, borrador de la semana siguiente | COMPROMISO VERBAL-MINUTA | Meeting notes 28-Jul; minuta 04-Ago *"Send draft next week's inspection"* | PARCIALMENTE CUMPLIDO | Calendario emitido cada semana | Las jornadas del 12 y 13-Ago se comunicaron en la reunion, no por calendario |
| Emisión de toda la documentación de ingeniería pendiente en Código 1 | BW Water | jueves 30-Jul-2026 | COMPROMISO VERBAL-MINUTA | Meeting notes 28-Jul *"Target to complete remaining Code 1 documentation: Thursday"* | INCUMPLIDO | Cero documentos pendientes de Código 1 | La minuta del 04-Ago aun lista *"Pending document submittals to support inspections – they need to be approved CODE 1"* |
| Entrega de repuestos: sensores y flowmeters | BW Water | martes 15-Sep-2026 | COMPROMISO ESCRITO BW | Meeting notes 28-Jul; cronograma IDs 377, 385, 389 | VIGENTE | Recepcion | BW Water declara que no impacta el ensamble ni la entrega |
| Packing list de membranas | BW Water | sin fecha | COMPROMISO VERBAL-MINUTA | Minuta 04-Ago, bloque `Pending items` | ABIERTO SIN FECHA | Documento emitido | Membranas con entrega directa a Taltal el 03-Ago |
| Actualizacion del panel PLC tras las pruebas | BW Water | miercoles 05-Ago-2026 | COMPROMISO VERBAL-MINUTA | Minuta 04-Ago *"PLC tests ongoing. Updates expected by tomorrow"* | VIGENTE | Reporte de pruebas recibido | — |
| Reporte de estado documental (DDSR) semanal | BW Water | semanal | COMPROMISO VERBAL-MINUTA | Minuta 07-Jul, bloque `Reporting`, lista `Document status report` como reporte pendiente | INCUMPLIDO 2 semanas | DDSR en el paquete semanal | Última emisión 20-Jul |

---

## 5. Discrepancias entre documentos de BW Water

### 5.1 Ready to Ship: 10-Sep en el tracker contra 19-21 Sep en el cronograma

Gobierna el **21-Sep**, y la conclusión se sostiene en cuatro documentos convergentes contra uno aislado:

| Fuente | Fecha | Naturaleza |
|---|---|---|
| Cronograma MS Project 04-Ago, ID 416 | 19-Sep a 21-Sep | Documento de control del proyecto, impreso el 04-Ago |
| Cronograma MS Project 27-Jul, ID 416 | 19-Sep a 21-Sep | Identico, una semana antes |
| Meeting notes del 28-Jul | 21-Sep | Declaracion escrita del PMO Leader |
| Fabrication Schedule 03-Ago, `Ready for shipment` | 19-Sep a 21-Sep | Cronograma de taller del mismo paquete |
| Hoja `Milestone Tracker` del tracker 03-Ago, celda D5 | 10-Sep | Unica fuente discrepante |

El 10-Sep del Milestone Tracker es una foto congelada del Recovery Schedule del 14-Jul, cuya tarea ID 387 proyectaba ex-works el 09-10 de septiembre. El diff confirma que la hoja `Milestone Tracker` no registro **ningun** cambio en las cuatro versiones comparadas (13-Jul, 20-Jul, 27-Jul y 03-Ago), de modo que quedo detenida en la fecha del 14-Jul mientras el cronograma se movia al 21-Sep.

Hay un segundo defecto en la misma celda: el 10-Sep esta cargado en la columna **`Actual`** (D5), no en `Estimate` (C5, que sigue diciendo 03-Ago-2026, es decir la linea base). Un hito que no ha ocurrido no puede tener fecha real. La columna `Estimate`, que es la que deberia llevar el pronostico, nunca se actualizo.

El Progress Report Week 31 no aporta a la controversia: no contiene fechas de embarque ni de FAT, solo porcentajes de avance por actividad. La minuta del 04-Ago tampoco: no menciona la fecha de embarque en ningun punto. Ese silencio es en si mismo un hallazgo, porque la reunion se celebro al dia siguiente del vencimiento del Plazo de Entrega contractual.

### 5.2 Tres fechas para el CIP / Flushing Tank

| Fuente | Fecha |
|---|---|
| Meeting notes 28-Jul | Entrega 03-Sep, llegada a Penang 05-Sep |
| Weekly Dashboard 03-Ago, item 10 | `Estimate Arrival Penang` 26-Ago |
| Minuta 04-Ago | *"Flushing tank delayed to 26 August"* |
| Cronograma 04-Ago, IDs 240 y 241 | Fabricación hasta 03-Sep, envio 04-05 Sep |

El cronograma del 04-Ago sigue con el escenario 05-Sep mientras el tracker y la minuta del mismo dia manejan el 26-Ago. Es la misma patologia que el equipo ya documento en junio: el cronograma y el tracker no se reconcilian entre si.

### 5.3 Valvulas: 06-Ago contra 15-Ago

El tracker mueve la llegada estimada de los tres items de valvulas (`All Valve Set`, `Metal Valve`, `PVC Valve`) de 23-Jul a 06-Ago, y la minuta del 04-Ago lo repite. El cronograma del 04-Ago, en cambio, pone el fin del `Shipping` de los tres el 15-Ago. Nueve días de diferencia dentro del mismo paquete.

### 5.4 Bomba HP Fedco: 21-Ago contra 31-Ago

El comentario del Weekly Dashboard, item 1, dice: *"Due to repositioning of terminal box, expected completion date is on 8/31."* Fedco, en su correo del 04-Ago, y BW Water, en su minuta del mismo dia, sostienen el 21-Ago. Con fin de fabricación el 31-Ago mas 12 días de flete aereo, la llegada a Penang seria alrededor del 12-Sep, no el 02-Sep que el propio tracker consigna dos columnas antes. La celda del comentario contradice a la celda de la fecha en la misma fila.

### 5.5 Panel PLC: fin de fabricación 09-Ago contra 14-Ago

El cronograma (ID 357) cierra la fabricación del LCP Panel el 09-Ago; el comentario del tracker (item 21) declara *"Manufacturing completion date target on 8/14"*. Ambos convergen en la llegada a Penang el 23-Ago, que además es domingo.

### 5.6 Dos lineas base conviviendo en el mismo paquete

La hoja `Milestone Tracker` se titula *"Milestone Tracker - Baseline issued by BW Water on 05-Mar-2026"*, y para Ready to Ship usa la fecha de esa linea base (03-Ago). Para el FAT, en cambio, declara `Baseline Date` "13 Aug - 18 Aug 2026", que no corresponde a la linea base del 05-Mar (25-Jul a 01-Ago) ni a la `Baseline1` del cronograma (24-Jul a 13-Ago). El mismo archivo mezcla dos lineas base distintas según la fila.

### 5.7 Los porcentajes agregados del Progress Report retroceden

| Bloque | Week 29 | Week 30 | Week 31 |
|---|---|---|---|
| SWRO | 68% | 68% | 55% |
| CIP | 59% | 59% | 52% |
| Antiscalant | 100% | 100% | 27% |

Ningun documento explica el retroceso. [Probable] Se trata de un recalculo de las ponderaciones y no de una regresion física: el Week 31 reordena las columnas del cuadro y el bloque Antiscalant mantiene `Fabrication - Antiscalant Dosing Box` en 0%, fila que el 100% de las semanas anteriores no podia estar considerando. En cualquier caso, un reporte de avance cuyo total baja 13 puntos sin nota al pie no sirve como evidencia de avance para un estado de pago.

Advertencia de lectura: la cifra de 27% del bloque Antiscalant proviene de una celda que el extractor partio en dos fragmentos (`2` y `7%`) por la estructura de la tabla del PDF. Conviene confirmarla visualmente antes de citarla a terceros.

### 5.8 Fechas estimadas vencidas que el tracker no depura

- `Instrument Set` (item 2): llegada estimada 29-Jul, sin llegada real, status E. Vencida hace 6 días, con el comentario *"Nego on leadtime with vendor still ongoing"*.
- `CIP Heater` (Week 30): decia *"pending for CIP Panel to deliver est. on 7/30"*. El Week 31 elimina la fecha y deja *"pending for CIP Panel to deliver"*. La fecha desaparece en vez de actualizarse.

### 5.9 El Change Log sigue vacio

Cero filas con contenido en las cuatro versiones del tracker. Los cinco movimientos de fecha del último salto (CIP Tank +30 días, los tres items de valvulas +14, estructuras +14) ocurrieron sin declaracion, igual que los cinco movimientos del cronograma listados en la Sección 3.

---

## 6. Riesgos y exposición contractual

### 6.1 Multa por atraso en la entrega del suministro — activa desde hoy

La Cláusula 43.1 letra b establece: *"Por atraso en la entrega del suministro (EXW): Se aplicara una multa diaria equivalente al 0,2% del valor neto total del Contrato u Orden de Compra, por cada dia calendario en que se exceda el Plazo de Entrega del Modulo RO Segunda Etapa establecido en la Clausula 27."*

El Plazo de Entrega vencio el lunes 03-Ago-2026. La mora corre desde hoy.

| Escenario de EXW | Días de exceso sobre el 03-Ago | Multa acumulada |
|---|---|---|
| Hoy, 04-Ago | 1 | 0,2% del valor neto |
| 19-Sep (inicio del hito proyectado) | 47 | 9,4% del valor neto |
| 21-Sep (término del hito proyectado) | 49 | 9,8% del valor neto |
| Tope de la Cláusula 43.4 | 75 | 15% del valor neto |

La Cláusula 43.4 fija el limite: *"El monto acumulado de multas cursadas al Proveedor, por cualquier concepto (atrasos, desempeno, otros), tendra como limite 15% del monto neto del Contrato u Orden de Compra"*, y agrega que se descuentan de los estados de pago pendientes o se hacen efectivas contra las boletas de garantía. En el escenario del 21-Sep, la multa por atraso sola consume dos tercios del tope global, dejando margen escaso para cualquier multa por desempeno en el Performance Test.

La Cláusula 27 cierra la puerta a la reprogramación tacita: *"No se admitiran modificaciones en dicho plazo, a menos que el Comprador lo acepte expresamente por escrito mediante la correspondiente revision del Pedido"*, y además *"Si se produjesen retrasos imputables al Proveedor, este debera poner los medios a su alcance para recuperar los mencionados retrasos, a su costa y sin cargo alguno para el Comprador"*. ADASA no ha emitido revisión del Pedido; el 21-Sep es una fecha declarada por el proveedor, no una fecha contractual.

### 6.2 Notificación de inspecciones fuera de plazo, por segunda vez

El cuerpo de la Cláusula 37 dispone: *"En aquellos equipos para los que pudiera existir una inspeccion de terceros, la fecha prevista por el Proveedor para la realizacion de las pruebas o ensayos debera ser comunicada por escrito con un minimo de Treinta (30) dias de antelacion para suministros internacionales y diez (10) dias de antelacion para suministros a nivel nacional."*

Las jornadas del 12 y 13 de agosto se comunicaron en la reunion del 04-Ago: 8 días de antelacion. La prueba hidrostática es punto de Hold según el ITP aprobado. Es la segunda notificación consecutiva fuera de plazo, después del Request to Witness Inspection 001 del 23-24 de julio, que aviso la jornada del 28-Jul con 4 días. El riesgo practico es operativo: con 8 días de aviso puede no alcanzarse a comprometer al inspector, y un punto de Hold queda sin testigo.

> ⚠️ **Corrección del 31-Ago-2026.** Esta línea decía que *"Bureau Veritas moviliza inspectores desde Chile"*, y es falso: **los inspectores son de Bureau Veritas Malasia, oficina BVKL, y atienden en Penang**. Por Bureau Veritas Chile pasan la contratación (Orden de Compra 836492) y la coordinación. El riesgo del aviso corto sigue siendo real, pero no por el viaje internacional sino por la agenda del inspector.

### 6.3 Riesgo de ruptura del Plazo Contractual de 510 días

La Cláusula 27 fija también que *"El Plazo Contractual se extendera desde la Notificacion de Adjudicacion por parte de ADASA hasta la obtencion por parte del Proveedor de la Recepcion Provisional del Pedido, y no debera superar los 510 dias corridos"*, es decir el lunes 01-Mar-2027. El cronograma del 04-Ago cierra el Performance Test el 02-Ene-2027. El margen es de 58 días, contra los 44 días que el proyecto ya perdio sobre la `Baseline1` en la última cadena. Un segundo deslizamiento del orden del ya ocurrido consume el margen completo.

### 6.4 Multa por atraso en documentación

La Cláusula 43.1 letra a aplica 0,05% diario del valor neto por atraso en la entrega de la ingeniería según la Sección 7 de la Especificacion Técnica. Dos frentes alimentan este riesgo: el target de Código 1 del jueves 30-Jul incumplido, y el fin de `Engineering` en el cronograma corrido de 05-Ago a 12-Ago sin declaracion. No corresponde cuantificarlo aquí, porque exige verificar que documentos concretos de la Sección 7 están vencidos y con que fecha comprometida; el DDSR es justamente el instrumento que permitiria hacerlo, y lleva dos semanas sin emitirse.

### 6.5 Concentracion del riesgo en la ventana del 07 al 18 de septiembre

La cadena que sostiene el 21-Sep es serial y sin holgura: llegada Fedco 02-Sep, posicionamiento de bomba y turbos 03-05 Sep, Dry Test y FAT 07-18 Sep, ready for shipment 19-21 Sep. Un dia de atraso en Fedco se traslada dia a dia al embarque. El propio cronograma ya comprimio el FAT de 15 a 11 días para sostener la fecha, lo que significa que la holgura de esa ventana se consumio antes de empezar.

### 6.6 Change Order anunciada sin sustento

El anuncio de una Change Order por cambios de ingeniería en el area CIP, sin monto ni fundamento, se produce el mismo dia en que el proveedor entra en mora contractual. Conviene registrar la asimetria y exigir que cualquier propuesta llegue con la trazabilidad de origen que exige el criterio de responsabilidad del proyecto, antes de que se mezcle con la discusion del atraso.

---

## 7. Verificado vs NO verificado

### Verificado en esta sesion, contra fuente primaria

- Plazo de Entrega de 300 días corridos, caracter firme, prohibicion de modificacion tacita y obligación de recuperar a costa del proveedor: leidos textualmente en la Cláusula 27 del archivo `BASES TECNICAS\md\BAE-12803-PLANTA-MODULAR.md`.
- Multa de 0,2% diario por atraso EXW, 0,05% por ingeniería y documentos, 0,1% por comisionamiento, y tope acumulado de 15%: leidos textualmente en las Cláusulas 43.1 y 43.4 del mismo archivo.
- Aviso de 30 días para inspección de terceros en suministros internacionales: leido textualmente en el cuerpo de la Cláusula 37.
- Aritmetica de los 300 días: 07-Oct-2025 mas 300 días corridos da 03-Ago-2026, calculado y verificado.
- Dia de la semana de todas las fechas citadas: calculado. 03-Ago-2026 lunes, 04-Ago martes, 06-Ago jueves, 07-Ago viernes, 12-Ago miercoles, 13-Ago jueves, 21-Ago viernes, 23-Ago domingo, 26-Ago miercoles, 02-Sep miercoles, 07-Sep lunes, 10-Sep jueves, 18-Sep viernes, 19-Sep sabado, 21-Sep lunes, 13-Nov viernes, 01-Mar-2027 lunes.
- Celdas del `Milestone Tracker` y del `Weekly Dashboard`: leidas directamente del `.xlsx`, no del diff, incluidos los comentarios completos de los items 1, 2, 10, 13, 21, 22 y 24.
- Change Log vacio: verificado directamente, la hoja tiene 3 filas y solo encabezados.
- Ausencia del DDSR y del cronograma en el paquete del 03-Ago: verificada por listado de directorio. El paquete contiene unicamente el Progress Report Week 31, el tracker y el Fabrication Schedule.
- Identidad de las fechas del cronograma del 27-Jul y del 04-Ago en las tareas 414, 416, 417 y 424: verificada por lectura de ambos archivos.
- Fechas del Recovery Schedule del 14-Jul (FAT 24-Ago a 08-Sep, ex-works 09-10 Sep, sitio 26-Oct, Performance Test 10-15 Dic): verificadas contra el archivo extraido, no tomadas del enunciado.

### NO verificado — se declara como tal

- **Fecha de la Notificación de Adjudicación.** El cálculo de los 300 días usa el 07-Oct-2025 que el cronograma de BW Water rotula `Contract Award / NTP`. [Suposicion] Que esa fecha coincida con la Notificación de Adjudicación formal de ADASA. La coincidencia exacta con el 03-Ago del Milestone Tracker es un indicio fuerte de que así es, pero la Notificación misma no se leyo en esta sesion. Antes de cursar multa, verificar la fecha en el documento de adjudicación.
- **Valor neto del contrato.** No se leyo. Las multas se expresan como porcentaje, sin monto.
- **Bandas de FAT comunicadas a Bureau Veritas (07-12 Sep base, 14-19 Sep alternativa).** Provienen del enunciado del encargo y de la memoria del proyecto, no de la lectura del correo a Bureau Veritas del 14-Jul. La conclusión de la Sección 5 sobre el FAT depende de esas bandas.
- **Validez de la oferta Bureau Veritas 600049 Rev 2 hasta el 05-Ago-2026.** Proviene de la memoria del proyecto. Si es correcta, vence manana y es una accion administrativa urgente e independiente del proveedor.
- **Corrección de memoria pendiente.** La memoria del proyecto atribuye el aviso de 30 días a la Cláusula 37.2. Es incorrecto: la Cláusula 37.2 trata de los plazos de revisión y aprobación por ADASA. El aviso de 30 días vive en el cuerpo de la Cláusula 37, antes de la subseccion 37.1. Verificado en esta sesion.
- **Segunda corrección de memoria.** Varias memorias citan la Cláusula 27 como fuente de las multas por atraso. La Cláusula 27 fija el plazo; las multas están en la Cláusula 43.1. La cita correcta para reclamar el atraso es "Clausula 27 para el plazo, Clausula 43.1 letra b para la multa".
- **Revisión R5 del Manufacturing Schedule de Fedco.** El archivo se llama R5, pero el bloque de control de revisiones del propio documento llega hasta la revisión 04, del 10-Jul-2026. La R5 no esta registrada en su propia tabla de revisiones, y el documento carece de firma y fecha de aprobación del cliente. No se puede afirmar cual es su fecha de emisión.
- **Causa raiz del atraso Fedco.** Sigue sin sustanciar. El R5 registra `Receive Down Payment` el 09-Jun-2026 como hito de arranque de la ingeniería, lo que respalda documentalmente la narrativa que BW Water planteo el 26-Jun. No es una asignación de responsabilidad aceptada por ADASA y no se trata aquí.
- **Retroceso de los porcentajes del Progress Report.** La lectura de recalculo de ponderaciones es una inferencia, marcada como [Probable]. Ningun documento la confirma.
- **Cifra de 27% del bloque Antiscalant.** Extraida de una celda que el extractor fragmento. Confirmar visualmente antes de usarla ante terceros.
- **Impacto real de la Change Order del area CIP.** Solo consta el titulo en la minuta. Sin alcance, monto ni fundamento.
- **Estado documental posterior al 20-Jul.** Sin DDSR de las semanas del 27-Jul y del 03-Ago, el 92% de avance de aprobación es un dato de hace 15 días. Las conclusiones sobre documentación se apoyan en los reports y las minutas, no en un DDSR vigente.

---

## 8. Entradas de Bitacora propuestas

### 2026-08-04 — Vencimiento del Plazo de Entrega contractual y confirmación del embarque al 21-Sep — INTERNO

> El Plazo de Entrega de la Cláusula 27 de las BAE 12803 (300 días corridos desde la Notificación de Adjudicación del 07-Oct-2025) vencio el lunes 03-Ago-2026, fecha que coincide exactamente con la linea base del hito `Ready to Ship (EXW Penang)` del Milestone Tracker de BW Water. El hito no se cumplio y la multa de la Cláusula 43.1 letra b (0,2% diario del valor neto, tope global 15% por Cláusula 43.4) corre desde el 04-Ago.

> La fecha de embarque vigente es 19-21 de septiembre de 2026, sostenida por cuatro fuentes de BW Water: los cronogramas MS Project del 27-Jul y del 04-Ago (tarea ID 416), las meeting notes del 28-Jul (*"Overall shipment readiness moved to 21-Sep-2026"*) y el Fabrication Schedule del paquete del 03-Ago. El 10-Sep que aparece en el Milestone Tracker es una foto congelada del Recovery Schedule del 14-Jul, cargada además en la columna `Actual` de un hito que no ha ocurrido; la hoja no registro cambios en las cuatro versiones comparadas desde el 13-Jul. Variacion contra la referencia declarada fija por ADASA el 14-Jul: 10 a 11 días. Contra la linea base contractual: 47 a 49 días. Cascada: llegada a sitio 26-Oct a 13-Nov, Performance Test 10-15 Dic a 29-Dic-02-Ene-2027. Análisis completo en `PROGRAMA y CONTRATO\REVISION SEMANAL PO EQUIPOS\SEMANA 03-08-26\_ANALISIS_PROGRAMA_04AGO.md`.

### 2026-08-04 — Fedco confirma embarque 21-Ago y entrega el Manufacturing Schedule R5 — RECIBIDO

> Lester Burton (Fedco) confirmo por escrito el 04-Ago: *"no delays or issues have been raised, and we are on track for the previously estimated ship date of 8/21. Motor was delivered to FEDCO today (8/3)."* Eduardo Yamauchi lo reenvio a ADASA a las 08:24 con el Manufacturing Schedule R5 (orden 19554, PO BW-PO-2026M183 R1, series 17538, 17540 y 17542). El cronograma cierra `Production` al 89%, `Manufacturing Complete` el 11-Ago, `Performance Testing` el 18-19 Ago y `Shipment Ready` el viernes 21-Ago. No mueve la llegada a Penang del 02-Sep, que se mantiene en el tracker y en las tres tareas de flete aereo del cronograma.

> El R5 no responde el reclamo de causa raiz que ADASA formulo el 29-Jun con plazo al viernes 03-Jul: es un cronograma de fabricación, sin secuencia de eventos ni acciones de recuperacion. La mora del reporte formal alcanza 32 días. Además, el comentario del Weekly Dashboard del 03-Ago para la bomba HP declara fin de fabricación el 31-Ago (*"Due to repositioning of terminal box, expected completion date is on 8/31"*), diez días después del 21-Ago que sostienen Fedco y la propia minuta de BW Water del mismo dia. Archivos en `PROGRAMA y CONTRATO\RESPUESTA DE FEDCO\`.

### 2026-08-04 — Minuta de la weekly call — RECIBIDO

> BW Water informa: recepcion del motor Fedco confirmada y compromiso mantenido al 21-Ago; pruebas de PLC en curso con actualizacion para el 05-Ago; fabricación de estructura iniciada con término a comienzos de la próxima semana; spools de super duplex en biselado y esmerilado; skids a pintura externa en Penang la próxima semana. Inspecciones: viernes 07-Ago confirmada para fabricación de spools en curso, mas dos jornadas nuevas el miercoles 12 y jueves 13 de agosto para prueba hidrostática de baja y alta presión y preparacion de superficie de la estructura. Procurement: bomba CIP recibida, valvulas al 06-Ago, flushing tank al 26-Ago, con BW Water sosteniendo que el atraso no afecta la ruta critica por tratarse de equipo de embarque suelto. Pendientes declarados: packing list de membranas, una Change Order por cambios de ingeniería en el area CIP, y documentación aun sin Código 1 requerida para soportar las inspecciones.

> La minuta no menciona la fecha de embarque, pese a celebrarse al dia siguiente del vencimiento del Plazo de Entrega. El target de completar toda la documentación en Código 1 el jueves 30-Jul, comprometido en la reunion del 28-Jul, quedo incumplido. Las jornadas del 12 y 13 de agosto se avisaron con 8 días, contra los 30 que exige la Cláusula 37 para inspección de terceros en suministros internacionales; es la segunda notificación consecutiva fuera de plazo. Fuente: `MINUTAS DE REUNION\md\MINUTA DE REUNION 04-08-26_extracted.md`.

### 2026-08-03 — Paquete semanal incompleto: sin DDSR ni cronograma — RECIBIDO

> El paquete del 03-Ago contiene el Progress Report Week 31, el Procurement tracking y el Fabrication Schedule. No incluye el Document and Drawing Status Report, ausente también en el paquete del 27-Jul; la última emisión disponible es la del 20-Jul (73 documentos, 92% de avance de aprobación, 47 aprobados, 16 aprobados con comentarios, 6 en Revise & Resubmit y 3 no entregados). No hay declaracion de discontinuacion en ninguna minuta, y el correo del 28-Jul enumera lo adjunto sin incluirlo, de modo que el reporte falta, no fue dado de baja. El cronograma llego por separado, fechado el 04-Ago, a la carpeta `PROGRAMA y CONTRATO\PROGRAMA DE MITIGACION\`.

> Cinco movimientos de fecha del tracker sin entrada en el Change Log, que sigue vacio en las cuatro versiones comparadas: CIP / Flushing Tank +30 días, los tres items de valvulas +14 días y estructuras +14 días. Cinco movimientos adicionales en el cronograma entre el 27-Jul y el 04-Ago, también sin declarar: fin de `Engineering` y de `Mechanical` +7 días, llegada de valvulas +11 días, membranas RO +3 días, y el `Pre-Assembly` con inicio corrido +8 días y duracion comprimida de 43 a 36 días para sostener el 18-Sep. Detalle en `SEMANA 03-08-26\DIFF_TRACKERS.md` y `DIFF_FABRICATION_SCHEDULE.md`.

---

## 9. Sugerencias a memorias

**Correcciones a memorias existentes.** Dos citas contractuales que circulan en las memorias del proyecto están mal atribuidas y conviene corregirlas antes de que lleguen a un documento externo:

1. En `project_fedco_fat_conflict_14may.md` y en `project_recovery_schedule_asme_31jul.md` se cita la Cláusula 27 como fuente de las multas por atraso ("dentro de Cl.27", "multas BAE Cl.27/43.1"). La Cláusula 27 fija el Plazo de Entrega; las multas viven en la Cláusula 43.1. La cita correcta es "Clausula 27 para el plazo, Clausula 43.1 letra b para la multa por atraso EXW, Clausula 43.4 para el tope de 15%".
2. En `project_bureau_veritas_inspection.md` se atribuye el aviso de 30 días a la Cláusula 37.2. La Cláusula 37.2 regula los plazos de revisión y aprobación de ADASA. El aviso de 30 días para suministros internacionales, y de 10 días para nacionales, esta en el cuerpo de la Cláusula 37, antes de la subseccion 37.1.

**Memoria nueva propuesta: `reference_plazo_entrega_clausula27_300dias.md`.** El anclaje contractual del hito de embarque merece memoria propia porque se va a usar en cada reclamo de aquí en adelante: NTP 07-Oct-2025, Plazo de Entrega 300 días corridos = 03-Ago-2026, Plazo Contractual hasta Recepcion Provisional 510 días = 01-Mar-2027, multa 0,2% diario por dia calendario de exceso, tope acumulado 15%, plazo firme sin modificacion salvo revisión expresa del Pedido por escrito, y obligación del proveedor de recuperar a su costa. Incluir la equivalencia de que la `Baseline Date` del Milestone Tracker de BW Water para Ready to Ship es la fecha de la Cláusula 27, no una fecha de conveniencia del proveedor.

**Actualizacion de `project_fedco_fat_conflict_14may.md`.** Agregar el bloque del 04-Ago: motor recibido en Fedco el 03-Ago, R5 con `Shipment Ready` el 21-Ago, llegada a Penang 02-Sep sostenida, y el reclamo de causa raiz aun sin responder con 32 días de mora. Registrar también que el R5 documenta el `Receive Down Payment` del 09-Jun como arranque de la ingeniería, lo que respalda la narrativa de BW Water sin que ADASA la haya aceptado.

**Actualizacion de `feedback_silent_slip_detection.md`.** La regla actual cubre el tracker. Extenderla al cronograma MS Project y al Fabrication Schedule, porque esta semana los movimientos no declarados mas relevantes ocurrieron ahi y no en el tracker: la hoja `Milestone Tracker` no cambio ni una celda en cuatro versiones mientras el cronograma movia el embarque once días. Agregar dos patrones nuevos: (a) una fecha congelada durante varias versiones es tan sospechosa como una fecha que se mueve, y (b) revisar la compresion de duraciones, porque una fecha de fin que se sostiene mientras el inicio se corre y la duracion se acorta no es recuperacion sino traslado del riesgo a la ventana final.

**Actualizacion de `feedback_procurement_review_pattern.md`.** Sumar el chequeo de coherencia intra-fila del tracker: comparar la celda de fecha estimada contra el texto del comentario de la misma fila. Esta semana la fila de la bomba HP declara llegada a Penang el 02-Sep y comenta fin de fabricación el 31-Ago, dos datos incompatibles en la misma linea. Sumar también la verificación de que las fechas estimadas vencidas se depuren: `Instrument Set` arrastra una llegada estimada al 29-Jul sin llegada real.

**Actualizacion de `project_bureau_veritas_inspection.md`.** Registrar la primera inspección ejecutada el 28-Jul con witness PMI completado, la segunda fijada para el viernes 07-Ago, y las jornadas del 12 y 13 de agosto avisadas con 8 días. Dejar constancia de que el FAT vigente ocupa del lunes 07 al viernes 18 de septiembre, once días corridos que abarcan las dos bandas comunicadas a Bureau Veritas el 14-Jul, y que la ventana ya no es de seis días. Verificar la fecha de validez de la oferta 600049 Rev 2, que según la memoria vence el 05-Ago.

---

## 10. Linea de tiempo vigente

### Contra la linea base cargada en el cronograma (`Baseline1` del MS Project)

| Hito | Fecha baseline | Fecha vigente | Variacion (días) | Fuente |
|---|---|---|---|---|
| Fabricación en taller Penang, término | 10-Ago-2026 | 21-Ago-2026 (viernes) | +11 | Cronograma 04-Ago, ID 397 |
| Pre-ensamble e instalación, término | 13-Ago-2026 | 18-Sep-2026 (viernes) | +36 | Cronograma 04-Ago, ID 404 |
| CSC del contenedor | 10-11 Ago-2026 | 27-28 Ago-2026 | +17 | Cronograma 04-Ago, ID 413 |
| Factory Acceptance Test del sistema | 24-Jul a 13-Ago-2026 (15 días) | 07-Sep a 18-Sep-2026 (11 días) | +45 en el inicio | Cronograma 04-Ago, ID 414 |
| Ready to Ship / Ex-works Penang | 14-15 Ago-2026 | 19-21 Sep-2026 | +36 al inicio, +37 al término | Cronograma 04-Ago, ID 416 |
| Entrega del paquete en sitio | 30-Sep-2026 | 13-Nov-2026 (viernes) | +44 | Cronograma 04-Ago, ID 417 |
| Supervisión de instalación | 27-Oct a 05-Nov-2026 | 10-19 Dic-2026 | +44 | Cronograma 04-Ago, ID 421 |
| Puesta en marcha | 06-11 Nov-2026 | 21-25 Dic-2026 | +44 | Cronograma 04-Ago, ID 422 |
| Entrenamiento de operadores | 12-13 Nov-2026 | 26-28 Dic-2026 | +45 | Cronograma 04-Ago, ID 423 |
| Performance Test | 14-19 Nov-2026 | 29-Dic-2026 a 02-Ene-2027 | +44 | Cronograma 04-Ago, ID 424 |

### Contra la referencia que ADASA declaro fija e inamovible (Recovery Schedule del 14-Jul)

| Hito | Recovery Schedule 14-Jul | Fecha vigente 04-Ago | Variacion (días) | Fuente |
|---|---|---|---|---|
| Factory Acceptance Test, inicio | 24-Ago-2026 | 07-Sep-2026 (lunes) | +14 | 14-Jul ID 385 contra 04-Ago ID 414 |
| Factory Acceptance Test, término | 08-Sep-2026 | 18-Sep-2026 (viernes) | +10 | Idem |
| Ready to Ship, inicio | 09-Sep-2026 | 19-Sep-2026 (sabado) | +10 | 14-Jul ID 387 contra 04-Ago ID 416 |
| Ready to Ship, termino | 10-Sep-2026 | 21-Sep-2026 (lunes) | +11 | Idem |
| Entrega en sitio | 26-Oct-2026 | 13-Nov-2026 (viernes) | +18 | 14-Jul ID 388 contra 04-Ago ID 417 |
| Entrenamiento | 08-09 Dic-2026 | 26-28 Dic-2026 | +19 | 14-Jul ID 394 contra 04-Ago ID 423 |
| Performance Test, término | 15-Dic-2026 | 02-Ene-2027 | +18 | 14-Jul ID 395 contra 04-Ago ID 424 |

### Contra la linea base contractual

| Hito | Fecha contractual | Fecha vigente | Variacion (días) | Fuente |
|---|---|---|---|---|
| Plazo de Entrega, EXW Penang | 03-Ago-2026 (lunes) | 19-21 Sep-2026 | +47 al inicio, +49 al término | BAE Cláusula 27; NTP 07-Oct-2025 mas 300 días corridos |
| Plazo Contractual hasta Recepcion Provisional | 01-Mar-2027 (lunes) | Performance Test al 02-Ene-2027 | 58 días de margen restante | BAE Cláusula 27; cronograma 04-Ago ID 424 |

### Equipos criticos en la ventana de embarque

| Equipo | Fecha vigente | Fuente | Nota |
|---|---|---|---|
| Bomba HP y dos turbochargers Fedco, listos para embarque | 21-Ago-2026 (viernes) | Manufacturing Schedule R5, tarea 28; correo Burton 04-Ago | El comentario del tracker dice 31-Ago |
| Bomba HP y turbos, llegada a Penang | 02-Sep-2026 (miercoles) | Tracker items 1, 12 y 16; cronograma IDs 224, 228 y 232 | 12 días de flete aereo desde el 21-Ago |
| Panel PLC en taller de Penang | 23-Ago-2026 (domingo) | Tracker item 21; cronograma ID 358 | Fin de fabricación 09-Ago según cronograma, 14-Ago según tracker |
| Valvulas, llegada | 06-Ago-2026 (jueves) | Tracker items 3, 4 y 5; minuta 04-Ago | El cronograma dice 15-Ago |
| CIP / Flushing Tank, llegada | 26-Ago-2026 (miercoles) | Tracker item 10; minuta 04-Ago | El cronograma dice 05-Sep |
| Membranas RO | 03-Ago-2026 (lunes), directo a Taltal | Tracker item 19 | No pasan por Penang, quedan fuera del FAT |
| Repuestos, sensores y flowmeters | 15-Sep-2026 (martes) | Meeting notes 28-Jul; cronograma IDs 377, 385 y 389 | BW Water declara que no impacta la entrega del sistema |

---

> **Auditado el 05-Ago-2026.** Ver `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/_ANALISIS_CRONOGRAMA_04AGO_REVISION.md`. Resultado: sostiene el anclaje contractual, el EXW del 19-21 Sep, la descalificacion del 10-Sep del Milestone Tracker, los diez slips silenciosos y la cadena critica. **Se retira un argumento:** el del FAT de "4 dias calendario para 7 jornadas contratadas", que salia del correo del 28-Jul y no se sostiene contra el cronograma del 04-Ago (ID 414 = 07 al 18-Sep, once dias). **Se corrige un dato:** la jornada de inspeccion es el **13 y 14 de agosto**, no el 12 y 13, per el Inspection Request 003, que supera a la minuta y ademas recorta el alcance.
