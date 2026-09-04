---
titulo: Ledger de cierre de comentarios — ENTREGA 88 (submittals 25007-0087 y 25007-0088)
fecha: 2026-08-28
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 88

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Dos submittals llegaron juntos en un solo correo el viernes 28-Ago-2026 a las 08:04 y quedaron archivados en la misma carpeta.

| Submittal | Emitido | Emision para | Devolucion pedida | Vencimiento real, Clausula 37.2 | Documento |
|---|---|---|---|---|---|
| `25007-0087` | jue 27-Ago-2026 | **IFC** | dom 30-Ago-2026 | **lun 7-Sep-2026** | Tie-In Point Layout `P22-DWG-09-005-005` Rev 0 |
| `25007-0088` | vie 28-Ago-2026 | **IFA** | lun 31-Ago-2026 | **mar 8-Sep-2026** | PLC/LCP FAT Procedure - Hardware `P22-PP-09-000-001` Rev B |

La fecha de devolucion del `25007-0087` cae en **domingo**. Es el quinto lote consecutivo con una fecha de devolucion por debajo del plazo contractual de siete dias habiles. Se declara como constancia, no como observacion de documento.

El vencimiento del `25007-0088` cae **un dia despues** de que abre el FAT del modulo, el 7-Sep. El documento de puerta de esa prueba se somete tan tarde que su propio plazo de revision vence con la prueba ya iniciada.

---

## 1. PLC/LCP FAT Procedure - Hardware Rev B — `P22-PP-09-000-001`

**Origen:** Rev A, **Codigo 2 — Approved as noted** en el TM N27, subseccion 2.5. Cinco puntos: OBS-01, OBS-02, OBS-03, NOTE-01 y NOTE-02.

### Lo primero, porque cambia la naturaleza del documento

**La Rev B ya no es un procedimiento a la espera de aprobacion: es el registro de un ensayo que ya se ejecuto.** Las paginas 2 a 16 son fotografias de un ejemplar impreso, llenado a mano, capturadas con CamScanner. El documento trae:

- Un **cierre de FAT firmado** (Seccion 9 del propio documento), con el resultado marcado **PASS WITH PUNCHLIST**.
- Un **punchlist de quince lineas** (Seccion 10), llenado a mano.
- Un **FAT Supplementary Rectification Report** de cuatro paginas con fotografias (paginas 13 a 16).

**El ensayo se ejecuto entre el 3 y el 5 de agosto de 2026 en Ningbo**, veintitres dias antes de que este documento se sometiera. El bloque de informacion del proyecto declara `FAT Location: Ningbo` y `FAT Date: 3rd August 2026`; el cierre firmado lleva fecha `2026.8.5` del fabricante del tablero y `5/8/26` de los otros dos firmantes.

### 🔴 Quien firmo, que es el punto mas grave

Verificado sobre el render de la pagina 2:

| Casilla del formulario | Quien firma | Empresa |
|---|---|---|
| Tested by (Panel Builder) | firma en caracteres chinos | 宁波捷创 (fabricante del tablero, Ningbo) |
| **Witnessed by (Client / Third-Party Inspector)** | **Billy Tan** | **BW Water**, E&C Engineer |
| **Accepted by (BW Water)** | **Chee De Yi** | **KVC Industrial Supplies**, Solution Architect |

**BW Water firmo la casilla del Comprador y del Tercero Inspector, y el proveedor del tablero firmo la casilla de BW Water.** Ni ADASA ni Bureau Veritas participaron. Las tres firmas del cierre pertenecen a la cadena de suministro.

**Base contractual, verbatim de la BAE, Clausula 37, pagina 59:** *"La fecha prevista por el Proveedor para la realizacion de las pruebas y ensayos sera confirmada por escrito al Comprador con un minimo de diez (10) dias de antelacion, tanto si van a llevarse a cabo en sus propios talleres o laboratorios como si se realizan fuera de ellos"*, y *"En aquellos equipos para los que pudiera existir una inspeccion de terceros, la fecha prevista por el Proveedor para la realizacion de las pruebas o ensayos debera ser comunicada por escrito con un minimo de Treinta (30) dias de antelacion para suministros internacionales"*. Este suministro tiene tercero inspector contratado, de modo que rige el plazo de treinta dias.

**Y la base mas fuerte no es la BAE sino el ITP que ADASA ya aprobo.** El `P22-BA-09-000-004` **Rev 0** del 29-Jun-2026, dispuesto en **Codigo 1 en el TM N26**, asigna en su columna de responsabilidad de ADASA:

| Fila del ITP | Actividad | Sub-Vendor | BW Water | **ADASA** |
|---|---|---|---|---|
| **6.1** | Inspection Manufacturing of Power and Control Panels | P | M | **W** |
| **6.2** | Electrical Testing of Switchboards | P | M | **W** |
| **7.1** | Approval of Detailed FAT Procedure | P | M | **H** |

El documento de referencia que la propia fila 6.2 declara es *"GA Drawing & Wiring Diagram/**FAT Procedure**"*, es decir, exactamente este documento.

La leyenda del ITP define la W sin ambiguedad: *"**W: Witness** — Client or 3rd party witness inspection (**requires notification**). However inspection and test are performed as scheduled, and even if the client or 3rd party is not present."*

**Ese matiz decide el encuadre y conviene respetarlo.** BW Water **no estaba obligado a esperar** a ADASA ni a Bureau Veritas para ejecutar el ensayo: el ITP lo autoriza a proceder en la fecha programada aunque no asistan. Lo que si estaba obligado a hacer, y no consta, es **notificar**. Reclamar por la ejecucion es refutable con el propio ITP; reclamar por el aviso no lo es.

La fila **7.1**, ademas, es **punto de detencion** de ADASA sobre la aprobacion del procedimiento detallado del FAT, y su leyenda exige asistencia. El procedimiento estaba en Codigo 2 con condiciones a incorporar **antes de testificar**, y el ensayo se corrio sin incorporarlas.

ADASA **no tiene registro** de esa comunicacion escrita. El punto se plantea pidiendo que BW Water la exhiba, no afirmando que no existe: el repositorio de correo entrante esta en pausa desde el 06-Ago. Lo que si es irrefutable, porque esta en la cara del documento, es quien firmo cada casilla.

Antecedente interno propio: el FAT del tablero en KVC estaba identificado como **hueco de alcance** de la oferta de Bureau Veritas desde el 07-Jul, con decision de ADASA pendiente (ver `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/PLAN_INSPECCION/Inspection-Coordination-Plan_INTERNAL.md`, punto 6). Que ADASA no hubiera cerrado esa decision no releva del aviso: el aviso es el que habilita la decision.

### Cierre de los cinco puntos del TM N27

| Punto | Pedido, literal | Verificado en la Rev B | Estado |
|---|---|---|---|
| **OBS-01** (MAYOR) | *"the governing drawings are cited under wrong or not-issued references. The Outline is cited 'P22-ET-09-008-001' (real code P22-CD-09-008-001; the ET number is the PLC & HMI Datasheet). The Schematic is cited 'P22-ET-09-008-002 Rev B', but it exists only at Rev A. **Correct: cite the correct CD codes and the issued Schematic revision before witnessing**"* | La tabla de documentos de referencia de la Seccion 5 (pagina 6, verificada por render) sigue con los dos codigos ET y ahora ademas con revisiones inexistentes: `P22-ET-09-008-001 -Rev3` rotulado *"PLC/LCP Schematic Diagram – GA-Drawing"*, `Rev. 3`; y `P22-ET-09-008-002 -Rev5`, `Rev. 5`. El codigo real del esquematico es `P22-CD-09-008-002` y **en este mismo ciclo llega en Rev B**. `P22-ET-09-008-001` es el Datasheet of PLC and HMI Panel Component, aprobado en Codigo 1 a Rev 0 en el TM N30. Ni la `Rev. 3` ni la `Rev. 5` existen en el proyecto. El encabezado de cada pagina y el bloque `Drawing Ref` repiten lo mismo | **No cerrado, y agravado.** La instruccion decia *before witnessing* y el testimonio ocurrio igual |
| **OBS-02** (MENOR) | corregir el TAG de la salida analogica del canal 3 (`BDS-09-001` donde la IO List asigna `-002`), el numero de documento del bloque de proyecto (`P22-PP-000-001`, sin el segmento `-09`) y el rotulo `KA2` donde el ensayo verifica `KA3` | El archivo tiene dos identidades. La **pagina 1 es una caratula nativa de BW Water** y esa si lleva `ADASA Code: P22-PP-09-000-001`, `Revision No.: B`, `Date: 27/8/2026`, con su tabla de revisiones (`A` el 6-Jul-26, `B` el 27-Ago-26). El **cuerpo escaneado que envuelve**, que es el documento del fabricante del tablero, se identifica en su bloque de informacion del proyecto como `Document Number: P22-ET-09-008 – FAT Procedure` y `Revision: Rev. 0 – Issued for FAT`. De modo que la caratula dice Rev B de un codigo y el documento que ejecuto el ensayo dice Rev 0 de otro. El defecto del numero de documento que la OBS-02 pedia corregir **no se corrigio**: cambio de forma. El rotulo de rele si quedo corregido: la fila del canal 2 lee `Relay KA3: Tag: HS001 - RO HP Pump Start Command` | **No cerrado.** El numero de documento empeoro |
| **OBS-03** (MENOR) | reconciliar dos criterios de aceptacion con los documentos aprobados: placa de montaje `Hot-Dip Galvanized` contra el zincado del Outline, y las señales de marcha de las bombas dosificadoras ensayadas como entrada digital cableada contra la IO List, que las lleva como entrada blanda sobre Ethernet/IP | La fila de placa de montaje sigue en `Hot-Dip Galvanized (HDG), 2.5 mm`; ese punto quedo **superado** por la resolucion del RFI-002, que acepto los componentes internos galvanizados. Las señales de marcha de las dosificadoras se siguen ensayando por cierre de contacto (`Dosing Pump 1 Running Test. Simulate closure`) | **Cierre parcial.** La mitad de la placa de montaje ya no corresponde exigirla; la mitad de las dosificadoras sigue abierta |
| **NOTE-01** | reconocimiento: la cobertura del ensayo y sus criterios son completos y consistentes con la IO List Rev 4 y la Especificacion Tecnica | La cobertura se mantiene: rack `5069-L320ER` con dos `5069-IB16`, un `5069-OB16`, dos `5069-IY4`, cinco `5069-IF8` y dos `5069-OF4`, mas los canales de devanado y rodamiento de los dos motores | **Cerrado**, sin accion |
| **NOTE-02** | *"the RTD protection tests are witnessed only after that list is reconciled to this mapping and the bearing AHH is set to the vendor-confirmed 95C"* | Los ensayos de RTD y de los transmisores de temperatura de devanado y rodamiento aparecen ejecutados y visados en las paginas 10 y 11. La Alarm and Interlock List se reconcilio recien al emitirse en **Rev 0**, sometida el **11-Ago** y dispuesta en Codigo 1 en el **TM N34 del 18-Ago**. El ensayo es del **3 al 5 de agosto** | **No respetado.** La retencion se levanto por el paso del tiempo, no antes del ensayo |

### 🔴 El punchlist: ocho lineas de categoria A sin cerrar en el formulario

La Seccion 10 define: *"A = Must be resolved BEFORE panel dispatch | B = Must be resolved before SAT/commissioning | C = For information only"*. Verificado sobre el render de la pagina 2:

| Linea | Hallazgo, transcrito | Categoria | Fecha objetivo | Fecha real | Estado |
|---|---|---|---|---|---|
| 1 | Remote Status: NO contact to add into S/S | A | — | — | en blanco |
| 2 | VFD Running & Fault — missing to PLC | A | — | — | en blanco |
| 3 | Speed command (4-20 mA) — missing to PLC | A | — | — | en blanco |
| 4 | Speed feedback — missing to PLC | A | — | — | en blanco |
| 5 | Main MCCB signal — missing to PLC | A | — | — | en blanco |
| 6 | PSU Fault signal — missing to PLC | A | — | — | en blanco |
| 7 | UPS Alarm signal — missing to PLC | A | — | — | en blanco |
| 8 | Start command from PLC to VFD | A | — | — | en blanco |
| 9 | Acrel Power Meter configuration | A | 4/8/2026 | 4/8/2026 | DONE |
| 10 | Residual Current Relay configuration | — | — | — | en blanco |
| 11 | Component data sticker English version | — | — | — | en blanco |
| 12 | ELR/RCR tripping + sparking | A | 5/8/2026 | — | DONE |
| 13 | Panel nameplate | — | — | — | en blanco |
| 14 | Drawing update + CAD update | — | — | — | en blanco |
| 15 | Aircond DI - input Add-on / cabinet light | — | — | — | en blanco |

Las quince lineas las levanto **Billy Tan**, de BW Water. El bloque de cierre del punchlist —`Rectified by (Panel Builder)` / `Witnessed by (Client / Inspector)` / `Accepted by (BW Water)`— esta **integramente en blanco**: sin nombre, sin firma, sin empresa, sin fecha.

El **FAT Supplementary Rectification Report** de las paginas 13 a 16 declara las dieciseis lineas como `Done&Tested` o `Done`, con fotografias. Ese reporte **no lleva firma, ni fecha, ni testigo**, y agrega una linea decimosexta que el punchlist no tiene. De modo que la unica evidencia de cierre de ocho no conformidades que el propio documento declara bloqueantes del despacho es una declaracion sin firmar del proveedor.

**Que son esas ocho lineas.** Todas son señales de interfaz del variador y del tablero hacia el sistema de control: marcha y falla del variador, comando y realimentacion de velocidad, señal del interruptor general, falla de la fuente, alarma de la unidad de respaldo, comando de partida al variador, y el contacto de estado remoto hacia la subestacion. El registro dice, con la letra del propio ingeniero de BW Water, que **el tablero se fabrico sin ellas** y que se agregaron durante el ensayo.

**Lo que si quedo verificado y conviene no confundir:** las cuatro señales de coordinacion con el sistema de control de planta, las que ADASA exigio desde el TM N19 y cerro en el TM N24, **si estan y se ensayaron**: `XA005 - System Enable Command from DCS` y `YA001 - System Running Status to DCS` aparecen visadas, junto con `XA001` a `XA004`. Las ocho lineas del punchlist son de otro nivel, el del variador y los servicios internos del tablero.


🔴 **El cruce con la I/O List aprobada, que es lo que le da peso al punto.** La I/O List Rev 6 —que llega en el mismo lote, en la ENTREGA 86— **ya define esas señales, y no desde ahora**. La ultima columna de cada fila declara en que revision se introdujo:

| Señal del punchlist | TAG en la I/O List | Tipo | Introducida en |
|---|---|---|---|
| Main MCCB signal | `XA001` Incoming Molded Case Circuit Breaker Close Status | DI, contacto seco | **rev 3** |
| PSU Fault signal | `XA003` y `XA004` PSU 1 ON y PSU 2 ON | DI, contacto seco | **rev 3** |
| VFD Running | `XB002` RO HP Pump Running | DI, contacto seco | **rev 4** |
| VFD Fault | `XT001` RO HP Pump Fault | DI, contacto seco | **rev 4** |
| Speed feedback | `SI001` RO HP Pump Speed Feedback | AI, 4-20 mA | **rev 4** |
| Speed command | `SIC001` RO HP Pump Speed Control | AO, 4-20 mA | **rev 4** |
| Remote status a la subestacion | `YA001` System Running Status to DCS | DO, contacto de rele | **rev 3** |

De modo que **el tablero se fabrico sin puntos que la lista aprobada define desde junio y julio**, y fue el propio ingeniero de BW Water quien tuvo que levantarlos en el ensayo como categoria A. No es una discrepancia de criterio ni una discusion de esquema blando contra cableado: son puntos que la lista lleva como entrada y salida fisica desde hace dos y tres revisiones.

**Y la lista si absorbio una de las lineas del punchlist:** la fila `XA009 A/C FAULT FEEDBACK` entra en la **revision 6**, que corresponde a la linea 15 del punchlist, el agregado de la entrada digital del equipo de aire acondicionado. Es la prueba de que la actualizacion documental de la linea 14 del punchlist empezo a ocurrir.

**Y de ahi sale el cruce que decide parte de este transmittal:** la linea 14 del punchlist es *"Drawing update + CAD update"*, y la **IO List Rev 6** y el **PLC/LCP Schematic Diagram Rev B** se emitieron el **27 de agosto**, despues del ensayo. La pregunta que hay que contestar antes de disponer es si esos dos documentos reflejan lo que efectivamente se construyo. **No corresponde exigir que esas señales sean cableadas**: el esquema de entradas y salidas blandas sobre Ethernet/IP esta aceptado desde el TM N20 y exigir cableado seria reabrirlo.

### 🔴 El terminal de operacion instalado es el `-D8S`

Verificado por render de la pagina 9: *"Verify HMI (HMI1: **2711P-T10C21D8S**, Allen-Bradley) is installed on inner door"*, visado. La misma referencia reaparece en el ensayo de encendido del terminal.

En el **TM N30** ADASA **declaro vinculante** el `2711P-T10C22D9P` —dos puertos Ethernet RJ45 y 1 GB, filas 15 y 18 del datasheet aprobado— frente al `2711P-T10C21D8S`, que segun el catalogo Rockwell 2711P-TD008 tiene un solo puerto y 512 MB, y que llevaban cuatro documentos del set de control. Aquella correccion se traslado a la Seccion 3 y no degradaba al documento revisado. Ahora el registro del ensayo muestra que **el tablero se armo fisicamente con el `-D8S`**.

### Otros hechos del registro, verificados

- **Instrumentos de ensayo sin identificar.** De los seis instrumentos de la Seccion 6, solo el multimetro trae modelo y numero de serie (`FLUKE 15B`, `20001523`). Los otros cinco —incluido el ohmetro de baja resistencia con que se miden las continuidades de tierra— llevan guion en modelo y en numero de serie. Ningun certificado de calibracion se registra, contra el requisito de seguridad 3 del propio documento: *"Verify that all test instruments carry a valid calibration certificate traceable to national standards. Record instrument details in the Test Equipment section"*.
- **Un criterio de aceptacion tachado.** En la fila de entradas de cable, las palabras *"and correctly sized"* estan tachadas y el diametro de las prensas queda como `TBC`, con la anotacion manuscrita *"open at Malaysia"*, sin visado de quien corrigio. La regla 13 del propio documento permite tachar un **resultado** con una linea y firmar al lado; aqui se tacho el **criterio**.
- **Los documentos que viajan dentro del tablero.** Una fila del ensayo verifica, y da por conforme, que *"the latest approved wiring diagram (P22-ET-09-008-001 Rev.3 and P22-ET-09-008-002) and GA drawing are filed inside the panel document box"*. El juego documental que acompaña fisicamente al tablero esta identificado con los mismos codigos y revisiones inexistentes de la OBS-01.
- **Color del envolvente.** El criterio de la fila de pintura dice *"Check panel paint colour: RAL 7035 Gray on enclosure frame, door, and roof"*, y el valor registrado a mano es `DOOR - RAL 7035`. Dos filas mas abajo, el cuerpo y la puerta se verifican en `SUS316L 2.0 mm` y el plinto en `SUS316L 2.5 mm`. El criterio de color aplicado al exterior contradice el datasheet aprobado del tablero, que fija SS316L sin pintar en el exterior, y la resolucion del RFI-002, que dejo el RAL 7035 para los componentes internos.
- **Sin hoja de comentarios consolidada.** La Rev B no trae ninguna: no hay columna de comentario del cliente ni columna de respuesta. El cierre de los cinco puntos del TM N27 se verifico contra el texto del propio documento.

### 🔴 Los tres documentos se contradicen sobre cuatro entradas digitales y sobre el mapa de reles

Este es el hallazgo que sale de cruzar el registro del FAT con los dos documentos de control que llegaron al dia siguiente, y conviene enunciarlo con el limite que la evidencia permite.

La seccion 8 del FAT, *"PLC I/O Static Wiring Test — Digital Inputs"*, con la instruccion impresa *"All tags per approved I/O list"*, registra visado manuscrito borne por borne. Cuatro de esos bornes del modulo `-A2`:

| Canal | Borne | TAG y descripcion en el FAT | Visado |
|---|---|---|---|
| 1 | DITB1-4 | `XT001` Incoming MCCB **Trip** States | si |
| 2 | DITB1-6 | `XA002` Disconnect Switch ON Status | si |
| 3 | DITB1-8 | `XT002` Feeder Power Failure | si |
| 4 | DITB1-10 | `XT003` Common Alarm Signal | si |

Dieciseis dias despues, **la I/O List Rev 6 elimina tres de ellos** —`XA002`, `XT002` y `XT003`, tachados en rojo—, y `XT001` del PLC no existe en ninguna revision de la lista. Tres dias mas tarde, **el esquematico Rev B rotula esos cuatro canales como reserva**.

En salidas hay un corrimiento de un rele: el FAT asigna `KA3` al arranque de la bomba de alta y `KA4` al de la bomba de CIP, dejando `KA7` y `KA8` de reserva; el esquematico Rev B pone `KA3` en el estado local y remoto, `KA4` en el arranque de la bomba de alta y `KA8` en el calentador.

**El limite de la evidencia, que decide como se redacta.** El cuerpo ejecutado del FAT **no cita la I/O List por codigo ni por revision**: su lista de referencias solo trae los dos codigos internos del proveedor. El visado prueba que se aplico señal a ese borne y que el controlador la vio, pero la nomenclatura de su tabla puede venir de una asignacion anterior a la Rev 5. Por eso la afirmacion defendible **no es** *"el tablero se construyo distinto de los planos"*, **sino** que los tres documentos se contradicen sobre cuatro entradas digitales y sobre el mapa de reles de salida, y que **ninguno de los dos documentos del `25007-0086` dice una palabra sobre el FAT**, pese a que la linea 14 del punchlist —*"Drawing Update + CAD update"*— se declara cumplida.

**Y una precision sobre las señales de las bombas dosificadoras que no debe convertirse en exigencia.** En el modulo `-A3` el FAT tiene la marcha de las dos dosificadoras cableada, y el esquematico Rev B la lleva a Ethernet/IP. La divergencia va en el sentido de que el tablero se construyo cableado y el plano lo paso a blando. **El esquema blando esta aceptado desde el TM N20** y exigir cableado lo reabriria.

### Sintesis para la disposicion

De los cinco puntos del TM N27, **uno cerro** (NOTE-01, que era un reconocimiento), **uno cerro a medias** (OBS-03) y **tres siguen abiertos**, incluido el mayor, cuya instruccion decia expresamente que se corrigiera **antes de testificar**. El ensayo se ejecuto igual, sin el Comprador y sin el tercero inspector, contra un procedimiento que se remite a dos documentos que no existen con esa identificacion, y se cerro con ocho no conformidades de categoria A cuyo levantamiento no esta firmado por nadie.

El documento se somete **para aprobacion (IFA)**, de modo que el Codigo 3 esta disponible sin contradecir ninguna frase propia: la condicion del Codigo 2 anterior no vencia al emitir Rev 0 sino **antes del testimonio**, y se incumplio.

---

## 2. Tie-In Point Layout Rev 0 — `P22-DWG-09-005-005`

**Origen:** Rev B, **Codigo 2** en el TM N31, subseccion 2.3, que cerro el Codigo 3 del TM N7 —el documento abierto mas antiguo del proyecto—. **Emitido para construccion (IFC).**

**Trae hoja de comentarios consolidada**, pagina 3, fechada el 18/8/2026, con dos filas: la primera recoge los cinco comentarios del Codigo 3 del TM N7 sobre la Rev A, y la segunda, con `Rev.` igual a `IFC`, transcribe textualmente el bloque de accion del TM N31. Las columnas `Status` y `SUB NO.` estan en blanco en las dos filas.

| Punto | Pedido, literal | Respuesta de BW Water | Verificado en la Rev 0 | Estado |
|---|---|---|---|---|
| **OBS-01** — presion de diseño en `TP-DA P8-001` | *"State the design pressure at the brine feed tie-in point TP-DA P8-001, so that compatibility with the ANSI 150# rating shown can be verified"*; el PDF anotado fijaba el umbral en 19,6 barG a temperatura de operacion | *"Design pressure for TP's added"* | **Cerrado y verificado contra la fuente.** La tabla incorpora una columna `DESIGN PRESSURE` que no existia en la Rev B, y la fila 2 lee `TP-DA P8-001 \| FEED \| 4" \| 150 \| ASME B16.5 \| **5 BARG** \| 8'-6 1/4" [2597mm]`. Coincide exactamente con la linea `DA-PVC-DN100-09-001`, `SWRO BRINE FEED`, de la **Line List Rev 0 aprobada en Codigo 1 en el TM N29**, que le asigna 3 barG de operacion, **5 barG de diseño** y 7,5 barG de ensayo, en la hoja P8 del diagrama de proceso. Los 5 barG estan muy por debajo del limite de 19,6 barG, de modo que la aceptacion condicionada de ADASA a la clase ANSI 150# se puede confirmar | **Cerrado** |
| **OBS-02** — clase y estandar de brida en `TP-AS P11-001` | *"complete the flange class and flange standard cells of tie-in point TP-AS P11-001, which remain blank"*, con la alternativa que ofrecia el PDF anotado: *"or state on the sheet that this connection is not flanged and how it is made"* | *"TP-AS P11-001 is not a flanged connection, instead the termination point provided will be the valve itself"* y *"DN15 AS connection is no longer identified as tie-in point. It is connected directly to the static mixer"* | **La sustancia esta contestada; el plano no la dice.** La fila 1 sigue identica a la Rev B: `TP-AS P11-001 \| ANTISCALANT \| 1" \| **-** \| **-** \| 5 BARG`. El bloque de notas conserva sus dos notas y no menciona el punto; **la palabra `valve` no aparece en ninguna parte de la lamina**. En la vista de la Seccion 2-2 la flecha de `TP-AS P11-001` si aterriza sobre un cuerpo de valvula dibujado, lo que respalda graficamente la respuesta sin enunciarla | **Cierre parcial** |

**Cajetin y estado, verificados por render:** `PROJECT DRAWING NO.: P22-DWG-09-005-005`, `REV.: 0`, `SHEET: 1`, `DWG. SIZE: A1`, `SCALE: AS-SHOWN`, `DISCIPLINE: MECHANICAL`, preparado BUK, revisado AIA, aprobado NOP. El bloque de revisiones tiene una sola fila, `0 | ISSUED FOR CONSTRUCTION | AUG.18.26 | AHR | A.I.A`.

🔴 **El plano se contradice sobre su propio estado.** El campo `DRAWING STATUS` del cajetin dice `ISSUED FOR APPROVAL`, valor arrastrado de la Rev B, mientras la fila de revision del mismo cajetin dice `ISSUED FOR CONSTRUCTION` y el formulario de envio lo somete como IFC. Y la caratula conserva `Revision No.: A` y `Date: 02/04/2026` sobre un documento que es Rev 0 de tres paginas.

**Sintesis.** El punto sustantivo cerro y quedo verificado contra la lista aprobada. Lo que resta —dos celdas en guion donde deberia decir que la terminacion es una valvula, y un campo de estado sin actualizar— es forma sobre un plano ya emitido para construccion, que no se retiene por eso.

**Cruce que sirve a otro frente:** la respuesta de BW Water —que en el antiscalante no hay brida porque la terminacion es la valvula— es **directamente pertinente al punto que el TM N36 dejo abierto en el Piping Layout Rev D**, donde la clase de brida de las terminaciones de antiscalante y de CIP sigue sin declararse.

---

## Municion que NO se emite

- Las tres normas de la tabla de documentos de referencia (`IEC 61439-1`, `IEC 60529`, `NEMA 4X`) quedan citadas como `Latest Edition`. Es el mismo defecto que ADASA objeto en las clausulas 5.5.2 y 5.6.3 del procedimiento de presion, pero **nunca se pidio sobre este documento**: exigirlo ahora es observacion nueva. Queda en traza por si reaparece en el dossier.
- La ausencia de una seccion de ensayo de resistencia de aislacion, que el alcance del propio documento anuncia, no se afirma: la extraccion viene de reconocimiento optico sobre fotografias y una ausencia solo se declara tras renderizar pagina por pagina. Si el punto se quiere emitir, hay que renderizar las dieciseis paginas y confirmarlo.
- **El diametro de `TP-AS P11-001`** figura como 1 pulgada en la tabla mientras la linea rotulada en la lamina es `AS-PVC-DN15-09-035`, es decir DN15. Venia igual desde la Rev B y el TM N31 no lo objeto.
- **La caratula del plano de puntos de conexion** declara `Revision No.: A` y dos paginas sobre un documento que es Rev 0 y tiene tres. Observacion nueva y aseo documental.
- Las lecturas de continuidad de tierra aparecen visadas contra el criterio de 0,10 ohm sin valor medido anotado. No se emite por si sola: la columna de valor real esta en blanco en varias filas del formulario y no se puede distinguir un formulario mal llenado de una medicion no hecha sin la evidencia del proveedor.
