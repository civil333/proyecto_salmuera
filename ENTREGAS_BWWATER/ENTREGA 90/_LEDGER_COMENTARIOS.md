---
titulo: Ledger de cierre de comentarios — ENTREGA 90 (submittal 25007-0090)
fecha: 2026-09-03
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 90

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0090`, emitido el **jueves 3 de septiembre de 2026**, con devolucion pedida al **domingo 6 de septiembre**: tres dias corridos, y en fin de semana. El vencimiento real de la Clausula 37.2 es el **lunes 14 de septiembre**. Septimo lote consecutivo por debajo del plazo contractual y tercera vez que la fecha cae en fin de semana.

**Esta entrega es la respuesta a la exigencia de cierre consolidado del TM N37**, que vencia hoy. De los doce items exigidos llegaron siete, contando el P&ID de la ENTREGA 89.

## Contenido del submittal

| # | Documento | Codigo | Rev | Emision | Origen |
|---|---|---|---|---|---|
| 1 | Liquid Penetrant Examination Procedure | `P22-BA-09-000-014` | 0 | **IFC** | Rev C, Codigo 2 en el TM N37 |
| 2 | Ultrasonic Thickness Procedure | `P22-BA-09-000-016` | C | IFA | Rev B, Codigo 3 en el TM N35 |
| 3 | Datasheet of RO High Pressure Pump | `P22-ET-09-009-002` | 0 | **IFC** | Rev E, Codigo 1 en el TM N36 |
| 4 | Line List | `P22-LI-09-009-003` | 1 | **IFC** | Rev 0, Codigo 1 en el TM N29 |
| 5 | Datasheet of Feed Turbocharger | `P22-ET-09-009-007` | 0 | **IFC** | Rev E, Codigo 2 en el TM N36 |
| 6 | Datasheet of Interstage Turbocharger | `P22-ET-09-009-008` | 0 | **IFC** | Rev E, Codigo 2 en el TM N36 |
| 7 | Equipment List | `P22-LI-09-005-001` | 0 | **IFC** | Rev B, Codigo 2 en el TM N11 |
| 8 | Instrument List | `P22-LI-09-008-003` | F | IFA | Rev E, Codigo 1 en el TM N20 |
| 9 | HMI Display Screenshot | `P22-LI-09-008-016` | C | IFA | Rev B, Codigo 2 en el TM N31 |
| 10 | PLC/LCP FAT Procedure - Hardware | `P22-PP-09-000-001` | C | IFA | Rev B, Codigo 3 en el TM N37 |

🔴 **Lo que la entrega NO trae, y estaba exigido para hoy:** los once planos de taller `25007-ME-PI-0901-0006` a `-0016`, el informe estructural `P22-CD-09-005-001` endosado, el O&M Manual `P22-BA-09-000-012` Rev B, el indice del dossier `P22-BA-09-000-013` Rev C, el procedimiento de FAT del modulo, el Preservation Packaging and Transport Procedure, la Valve List `P22-LI-09-005-002` y el plan de entrega del dossier con fechas. Tampoco la Radiography Examination Procedure en Rev 0, que era Codigo 2 en el N37.

## La regla que gobierna la revision de esta entrega

**Seis documentos llegan emitidos para construccion** (items 1, 3, 4, 5, 6 y 7). Sobre un Rev 0 no se agregan comentarios nuevos: solo se verifica si la condicion que los dejo en Codigo 2 se cumplio. **Ninguno de los seis falla su condicion.** Van en Codigo 1, sin PDF anotado.

**Cuatro llegan para aprobacion** (items 2, 8, 9 y 10) y admiten observacion y anotacion normal.

## Cierre punto por punto

### 1. Liquid Penetrant Examination Procedure Rev 0 — Codigo 2 del TM N37

| Punto | Pedido, literal | Respuesta de BW Water | Verificado en la Rev 0 | Estado |
|---|---|---|---|---|
| OBS-01 | Emitir el formulario en blanco, con la identificacion de este modulo | *Revised as per comment* | El formulario del Apendice 1 esta vacio en todos sus campos. `ITS-PT230601` y los lotes `2408019`, `2405026` y `2404074` desaparecieron | **Cerrado** |
| OBS-02 | Dejar la columna de observaciones en blanco | *Revised as per comment* | `No Relevant Indication` ya no aparece en el cuerpo | **Cerrado** |
| OBS-03 | Alinear el campo Procedure del formulario con la revision emitida | *Revised as per comment* | El campo esta en blanco, para que lo complete el examinador | **Cerrado** |
| NOTE-01 | Declarar el numero de documento de este procedimiento | *Revised as per comment* | La caratula lee `DOC NO: PT PROV-PROC-PT-001`. Quitaron el prefijo `PMI`, no el numero | **Abierto** |

**Residuo detectado fuera de la condicion:** trece de las quince paginas del cuerpo rotulan `WI-OD-PT02, Rev.0` y dos siguen en `Rev.C`.

`XESSB` en los encabezados es el membrete de Xpert Engineering Solution Sdn Bhd, el subcontratista de ensayos no destructivos. **Legitimo, no se observa.**

**Sintesis.** Las tres acciones de la condicion se cumplieron y el punto de fondo, que se venia arrastrando desde el N32, cerro. El numero de documento y los dos encabezados no formaban parte de la condicion. **Codigo 1**, con esos residuos documentados en la Seccion 3.

### 2. Ultrasonic Thickness Procedure Rev C — Codigo 3 del TM N35

| Punto | Pedido, literal | Respuesta de BW Water | Verificado en la Rev C | Estado |
|---|---|---|---|---|
| OBS-01 | Declarar el criterio del NDE Plan en la clausula 9.0 y escribir el material como UNS S32750 | *Revised as per comment* | La clausula 9.0 remite al NDE Plan `P22-BA-09-000-005` Rev C y declara `UNS S32750`. Ya no cita SA-790. Remite al criterio, no lo escribe | **Cerrado en lo esencial** |
| NOTE-01 | Velocidad sonica como valor; corregir el segundo grado | *Revised as per comment* | `S32250` corregido. La velocidad sigue sin declararse como valor | **Parcial** |
| NOTE-02 a | Acoplante coherente con la clausula 5.0 | *Revised as per comment* | `Wallpaper Paste` desaparecio | **Cerrado** |
| NOTE-02 b | Lista de referencias | *Revised as per comment* | `ASME E 797` y API 510, 570 y 653 desaparecieron. Quedan `SA790` y `SA79M` | **Parcial** |
| NOTE-02 c | Caratula y articulo correcto | *Revised as per comment* | La descripcion como procedimiento de identificacion positiva de material desaparecio. La clausula 4.0 **sigue citando `ASME Section V, Article 9`**, que es examen visual; corresponde el **Articulo 5** | 🔴 **Abierto, segunda vez** |
| NOTE-02 d | Emitir con hoja de comentarios | *Revised as per comment* | La Rev C la trae | **Cerrado** |

**Sintesis.** El determinante que sostenia el Codigo 3 cerro. Lo que queda son cuatro correcciones de referencia incorporables al emitir Rev 0. **Codigo 2**, con `CC_ADASA` de dos cuadros.

### 3, 5 y 6. Los tres datasheets Fedco — Codigo 1 y Codigo 2 del TM N36

| Documento | Condicion | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| `P22-ET-09-009-002` HP Pump | Ninguna de contenido; solo emitir en Rev 0 IFC | Emitido. Fabricante del motor consistente en los dos bloques de datos | **Cerrado** |
| `P22-ET-09-009-007` Feed Turbo | Borrar `STYLE 77` de las cuatro llamadas de conexion | Las cuatro llamadas leen `PIEDMONT STYLE S` + `CUT GROOVE`. La unica ocurrencia de `STYLE 77` que queda esta en la hoja de comentarios, citando la instruccion de ADASA | **Cerrado** |
| `P22-ET-09-009-008` Interstage | Idem | Idem | **Cerrado** |

**Sintesis.** Los tres en Rev 0 apto para construccion, sin revision de aprobacion intermedia, que es exactamente lo que ADASA exigio para equipos ya comprados y fabricados. **Codigo 1 los tres.**

### 4. Line List Rev 1 — Codigo 1 del TM N29

Sin condicion abierta. Diff fila por fila contra la Rev 0 aprobada:

| Hallazgo | Detalle |
|---|---|
| Ocho lineas nuevas | `CP-SS316-DN150-09-022` (reemplaza a la de PVC), `RD-PVC-DN15-09-046` y los seis spools de baja presion `09-047` a `09-052` |
| **La columna HYDROTEST no cambio en ninguna linea comun** | Las presiones que ADASA viene exigiendo (75, 90, 120 y 135 barG) siguen identicas. **No mueve la base de los ensayos ya reclamados** |
| Los seis spools de baja presion | Entran con hidrostatica de **7,5 barG**, que documenta formalmente la base de los ensayos que Bureau Veritas dio por conformes el 20 y 21 de agosto |
| Cambio de material | Succion CIP de PVC a SS316; la columna de ensayo no destructivo pasa de no aplica a liquidos penetrantes, coherente con una linea metalica |
| Cambios menores | Caudal de `09-044` y `09-045`; presion de operacion de `DA-SSD-DN100-09-003` de 51 a 49 bar; redondeos |
| 🔴 Medidas invertidas | `09-049` (1a etapa, **54 m3/h**) va en DN65 y `09-048` (2a etapa, **36 m3/h**) en DN80, al reves del par de alta presion aprobado en Rev 0, que dimensiona 54 m3/h en DN80 y 36 en DN65. El P&ID Rev 0 los tiene correctos. **ADASA declara vinculantes `CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`** |

**Sintesis.** **Codigo 1.** El cambio de material se acepta como sustitucion menor por disponibilidad. Las dos medidas invertidas se corrigen contra el valor que ADASA declara, sin reemitir la lista.

### 7. Equipment List Rev 0 — Codigo 2 del TM N11

El N11 no levanto observaciones. Lo exigible es el compromiso escrito en la hoja de comentarios del modelo 3D: reemitirla alineada al desglose de recipientes.

| TAG | Descripcion | Cantidad |
|---|---|---|
| `BOI-09-001` | Stage 1 SWRO Membrane, 7 por recipiente | 42 total |
| `BOI-09-001-1` a `-6` | Stage 1 RO PV, Protec BPV-8-1200-SP-7 | **6** |
| `BOI-09-002` | Stage 2 UHPRO Membrane, 7 por recipiente | 28 total |
| `BOI-09-002-1` a `-4` | Stage 2 RO PV, Protec BPV-8-1800-SP-7 | **4** |

Internamente coherente: 42 a 7 por recipiente dan 6; 28 a 7 dan 4. **La reconciliacion comprometida se hizo.** El modelo 3D Rev A traia cinco en primera etapa: la lista aprobada gobierna y es el modelo el que debe alinearse.

**No llego la Valve List**, comprometida en el mismo par.

**Sintesis. Codigo 1.**

### 8. Instrument List Rev F — Codigo 1 del TM N20

| Punto | Pedido | Verificado en la Rev F | Estado |
|---|---|---|---|
| N34 | `VT-09-001` en el rango vinculante de 0 a 12 mm/s rms | La fila lee `0.0 / 12.0 mm/s rms` contra `0.0 / 8.9` de la Rev E. Alarmas en 2,3 y 4,5 sin cambio | **Cerrado** |

El disparo de 10,0 mm/s de la Alarm and Interlock List Rev 0 ya cae dentro del rango del instrumento aprobado. `VT-09-002` y `VT-09-003` siguen en 0 a 8,9: **ADASA solo declaro vinculante el de `VT-09-001`**, de modo que no es incumplimiento; se pregunta por consistencia.

**Sintesis. Codigo 1.**

### 9. HMI Display Screenshot Rev C — Codigo 2 del TM N31

🔴 **La hoja de comentarios declara solo dos acciones. La verificacion por render muestra que hicieron mas de lo que declararon.** Los TAG viven dentro de las imagenes: `get_text()` devuelve vacio en 60 de las 80 paginas y **la ausencia no se puede afirmar sin renderizar**.

| Punto | Pedido | Verificado por render | Estado |
|---|---|---|---|
| OBS-01 | Voltaje, corriente y potencia en kW | **Seccion 7.7 Digital Power Meter, nueva**: tensiones L1/L2/L3 y linea-neutro, corriente por fase, potencia activa en kW, reactiva, frecuencia, factor de potencia y energia | **Cerrado** |
| OBS-02 | `LS-09-002` en nivel bajo, `LS-09-001` en alto | Pantalla 7.1 correcta | **Cerrado** |
| OBS-03 | `BH-09-001` en la bomba de alta | Pantalla 7.2 correcta; la 7.5 mantiene `BH-09-002` en la CIP | **Cerrado** |
| OBS-04 | `TE-09-001` devanado, `TE-09-002` rodamiento | Pantalla 7.2 correcta | **Cerrado** |
| OBS-05 | `VE-09-005` en la reposicion CIP | Pantalla 7.3 correcta | **Cerrado** |
| OBS-06 | `PIT-09-003` en la alimentacion de primera etapa | 🔴 **Invertido.** La 7.3 mantiene `PIT-09-005` y la 7.4 pasa a mostrar `PIT-09-003`. Los dos quedaron cruzados | **Abierto** |
| OBS-07 | `FIT-09-004` en el rechazo a drenaje | Pantalla 7.3 correcta | **Cerrado** |
| Pedido | Donde se muestran `PIT-09-008` y `FIT-09-002` | En las pantallas 7.3 y 7.4 respectivamente | **Cerrado** |

BW Water marco con recuadro rojo cada cambio, incluido el de la 7.4: toco `PIT-09-003` deliberadamente y lo puso en la pantalla equivocada.

**Cierra ademas el mapeo de sensores de temperatura**: `TE-09-001` y `TE-09-002` en la bomba de alta, `TE-09-003` y `TE-09-004` en la CIP.

Los valores de las capturas son de simulacion y la verificacion visual completa sigue reservada al FAT, como declaro el N31.

**Sintesis.** Seis de siete cerradas y una invertida. **Codigo 2**, con `CC_ADASA` de un cuadro.

### 10. PLC/LCP FAT Procedure - Hardware Rev C — Codigo 3 del TM N37

| Punto | Pedido | Verificado en la Rev C | Estado |
|---|---|---|---|
| OBS-01 | Emitir el procedimiento como procedimiento, separado del registro | La Rev B eran 16 paginas fotografiadas con 1.378 caracteres extraibles. **La Rev C es nativa, 23 paginas, 50.980 caracteres**, con lugar y fecha del FAT en blanco, resultados por llenar y punchlist vacio con sus tres casillas de firma. Y BW Water responde por escrito que hara **otro FAT en Penang con testigo de ADASA y de un tercero** contra el procedimiento aprobado | **Cerrado** |
| OBS-02 | Cerrar los ocho items categoria A con firma | **No puede cerrarse aqui**: al separar procedimiento de registro, esos items pertenecen al registro de la Rev B. Su cierre firmado es un entregable aparte | **Se traslada** |
| OBS-03 | Citar esquematico e I/O List por codigo y revision emitida | Cita `P22-LI-09-008-001 Rev.6`, `P22-CD-09-008-001 Rev.1` y `P22-CD-09-008-002 Rev.C` | **Cerrado** |
| OBS-04 entradas | Reconciliar las cuatro entradas digitales del modulo `-A2` | Los canales 1 a 4 se declaran de reserva. Coincide con el esquematico Rev B y con la I/O List Rev 6 | **Cerrado** |
| OBS-04 salidas | Reconciliar el mapa de reles | 🔴 **La fila del canal 7 se contradice a si misma** sobre el rele `KA8`. **ADASA declara cual gobierna**: la I/O List Rev 6 lleva el calentador CIP como **item 108, `REL-09-001-HS001`, salida digital de contacto seco**. El `HS001` repetido en cinco salidas es el sufijo del TAG; la lista los lleva completos | **Abierto** |
| OBS-05 | Instrumentos de ensayo identificados | El requisito 3 de seguridad se mantiene y remite a la seccion correspondiente, que como corresponde a un procedimiento en blanco queda por completar | **Cerrado en estructura** |
| NOTE-01 | Un solo numero de documento | `P22-PP-09-000-001` consistente en todo el cuerpo | **Cerrado** |
| NOTE-02 | Como cierra la brecha del terminal de operacion | El cuerpo sigue especificando el `-D8S`. La respuesta se esperaba sobre el esquematico, que no vino | **Se traslada** |

**Dato favorable:** la tabla de inspeccion visual declara ahora la materialidad exterior e interior del tablero — cuerpo y puerta SUS316L 2,0 mm, plinto SUS316L 2,5 mm, puerta batiente interior en laminado 2,0 mm RAL 7035 y placa de montaje galvanizada 2,5 mm — que es la distribucion que ADASA acepto.

**Sintesis.** El determinante del Codigo 3 cerro. **Codigo 2**, con `CC_ADASA` de dos cuadros.

## Disposicion de la entrega

| Documento | Codigo | `CC_ADASA` |
|---|---|---|
| Liquid Penetrant Examination Procedure Rev 0 | **1** | no |
| Ultrasonic Thickness Procedure Rev C | **2** | si |
| Datasheet of RO High Pressure Pump Rev 0 | **1** | no |
| Line List Rev 1 | **1** | no |
| Datasheet of Feed Turbocharger Rev 0 | **1** | no |
| Datasheet of Interstage Turbocharger Rev 0 | **1** | no |
| Equipment List Rev 0 | **1** | no |
| Instrument List Rev F | **1** | no |
| HMI Display Screenshot Rev C | **2** | si |
| PLC/LCP FAT Procedure - Hardware Rev C | **2** | si |

Con el P&ID de la ENTREGA 89: **8 Codigo 1, 3 Codigo 2, cero Codigo 3.** Veredicto global del TM N38: **2 — Approved as noted**.
