---
titulo: Analisis interno — Transmittal N38 (P22-TM-09-000-038-0)
codigo: P22-TM-09-000-038-0
fecha: 2026-09-03
estado: INTERNO — disposicion propuesta
type: analisis
project: salmuera-taltal
---

# Analisis interno — Transmittal N38

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

## 1. Recepcion y plazos

| Submittal | Entrega | Emitido | Devolucion pedida | Vencimiento real Clausula 37.2 | Docs |
|---|---|---|---|---|---|
| 25007-0089 | E89 | martes 1-Sep-2026 | viernes 4-Sep | **jueves 10-Sep** | 1 |
| 25007-0090 | E90 | jueves 3-Sep-2026 | **domingo 6-Sep** | **lunes 14-Sep** | 10 |

Sexto y septimo lote consecutivo con devolucion pedida en tres dias corridos contra los siete habiles de la Clausula 37.2. Tercera vez que la fecha cae en fin de semana.

La E90 es la respuesta a la exigencia de cierre consolidado del TM N37, que vencia hoy jueves 3 de septiembre.

## 2. El hecho central: 7 de 12

La tabla del TM N37 pedia doce items. Llegaron siete.

| # | Item exigido | Estado |
|---|---|---|
| 1 | P22-BA-09-000-016 Ultrasonic Thickness Rev C | **Llego** (Rev C IFA) |
| 2 | P22-ET-09-009-002 / -007 / -008 datasheets Fedco Rev 0 IFC | **Llegaron los tres** |
| 3 | P22-LI-09-008-003 Instrument List con VT-09-001 en 0 a 12 mm/s rms | **Llego** (Rev F) |
| 4 | 25007-ME-PI-0901-0006 a -0016, once planos de taller | **NO llego** |
| 5 | P22-CD-09-005-001 Structural Calculation Report endosado | **NO llego** |
| 6 | Numeracion de linea unificada (P&ID + Line List + planos de fabricacion) | **Parcial** — llegaron P&ID y Line List, no los planos, y se contradicen entre si |
| 7 | P22-BA-09-000-012 O&M Manual Rev B | **NO llego** |
| 8 | P22-BA-09-000-013 Dossier Index Rev C | **NO llego** |
| 9 | P22-LI-09-008-016 HMI Display Screenshot | **Llego** (Rev C IFA, no Rev 0) |
| 10 | Procedimiento de FAT del modulo (ET Seccion 8.1) | **NO llego** |
| 11 | Preservation, Packaging and Transport Procedure | **NO llego** |
| 12 | P22-LI-09-005-001 Equipment List y P22-LI-09-005-002 Valve List | **Parcial** — llego la Equipment List, no la Valve List |

Ademas no llego el plan de entrega del Dossier con fechas por capitulo, ni la Radiography Examination Procedure en Rev 0 (era Codigo 2 en el N37).

**Los cinco ausentes incluyen los tres pendientes que el propio N37 llamo los mas graves:** planos de taller, dossier e informe estructural endosado.

## 3. La regla que gobierna: sobre un Rev 0 no se agregan comentarios nuevos

Siete de los once llegan emitidos para construccion. Sobre esos solo se verifica si la condicion que los dejo en Codigo 2 se cumplio. Ninguno falla su condicion, de modo que los siete van en Codigo 1 y ninguno lleva CC_ADASA. Lo que la revision encontro de nuevo en ellos se **documenta** en el texto y en la Seccion 3, sin observacion y sin degradar el codigo.

Los cuatro restantes llegan para aprobacion (IFA) y admiten observacion y anotacion normal.

## 4. P&ID Rev 0 — P22-DWG-09-009-002

**Origen:** Rev D, Codigo 1 en el TM N18. Sin condicion abierta: el N18 declara que el plano no requiere modificacion y queda aprobado tal como esta.

**Verificacion:** emitido en Rev 0 IFC. Condicion de forma cumplida.

**Cinco cambios que BW Water introdujo por su cuenta**, declarados en su hoja de comentarios:

1. Orientacion del filtro de cartuchos corregida a vertical — cierra un hallazgo conocido de ADASA.
2. Linea de drenaje del panel de instrumentos agregada, `RD-PVC-DN15-09-046`.
3. Placa de orificio al analizador de conductividad `CIT-09-004` cambiada por valvula reductora de presion. Su propia nota dice que la Valve List debe actualizarse y reemitirse.
4. Rotulado de linea agregado para los spools de super duplex de baja presion, reflejado en la Line List Rev 1.
5. Succion de la bomba CIP cambiada de PVC a SS316 por no conseguir un reductor excentrico de PVC.

**Contradiccion verificada con la Line List Rev 1**, en la lamina 10 del P&ID contra la pagina 3 de la lista:

| Numero de linea | P&ID Rev 0 | Line List Rev 1 |
|---|---|---|
| 09-048 | `CP-SSD-DN65-09-048` | `CP-SSD-DN80-09-048` (2ND STAGE CIP REJECT OUT) |
| 09-049 | `CP-SSD-DN80-09-049` | `CP-SSD-DN65-09-049` (1ST STAGE CIP REJECT OUT) |

Diametros opuestos en los dos documentos, sobre spools a fabricar, y justo en el rotulado nuevo que la reunion del 26 de agosto pidio unificar.

**ADASA determina cual esta mal, y lo declara.** La columna de caudal de la propia Line List lo resuelve: el rechazo CIP de primera etapa lleva **54 m3/h** y el de segunda **36 m3/h**, y el par de **alta presion aprobado en Rev 0** los dimensiona **DN80** y **DN65** respectivamente (`CP-SSD-DN80-09-044` y `CP-SSD-DN65-09-045`). El par nuevo de baja presion invierte esa correspondencia: asigna DN65 al servicio de 54 m3/h y DN80 al de 36. El P&ID Rev 0 los rotula al reves de la lista, o sea **correctamente**.

**Medidas vinculantes que declara el transmittal:** el rechazo CIP de primera etapa a baja presion es `CP-SSD-DN80-09-049` y el de segunda `CP-SSD-DN65-09-048`. **El P&ID no cambia; la que se corrige es la Line List**, antes de fabricar esos spools.

### Disposicion

**Codigo 1 — Approved.** No habia condicion que verificar y el plano se emitio en Rev 0, y ademas es el documento que tiene los diametros correctos. La determinacion y los cambios propios se documentan en la Seccion 3; no degradan el plano porque el entregable de numeracion unificada exige ademas los planos de fabricacion, que no llegaron, y por eso no puede cerrarse en este ciclo de ninguna manera.

## 5. Liquid Penetrant Examination Procedure Rev 0 — P22-BA-09-000-014

**Origen:** Rev C, Codigo 2 en el TM N37. Condicion: limpiar el formulario de los identificadores de otro contrato y del resultado pre-escrito, y alinear el indice de revision que cita.

**Verificacion punto por punto sobre el documento:**

| Punto | Pedido | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| OBS-01 | Formulario en blanco, con identificacion de este modulo | `ITS-PT230601` y los lotes `2408019 / 2405026 / 2404074` desaparecieron. El formulario del Apendice 1 esta integramente vacio: Client, Report No, Project, Procedure, Job No, Date of Test, criterio y las cuatro casillas de firma | **Cerrado** |
| OBS-02 | Columna de observaciones en blanco | `No Relevant Indication` ya no aparece en el cuerpo | **Cerrado** |
| OBS-03 | Alinear el campo Procedure del formulario con la revision emitida | El campo esta en blanco, para que lo complete el examinador | **Cerrado** |
| NOTE-01 | Declarar el numero de documento de este procedimiento | La caratula sigue leyendo `DOC NO: PT PROV-PROC-PT-001`. Quitaron el prefijo `PMI`, no el numero | **Abierto** |

**Residuo adicional detectado:** trece de las quince paginas del cuerpo rotulan `WI-OD-PT02, Rev.0` y dos siguen en `Rev.C`.

`XESSB` persiste en los encabezados: es el membrete de Xpert Engineering Solution Sdn Bhd, el subcontratista de ensayos no destructivos. Es legitimo y no se observa.

### Disposicion

**Codigo 1 — Approved.** Las tres acciones de la condicion se cumplieron. El numero de documento y los dos encabezados desalineados no formaban parte de la condicion y son de identificacion documental: se documentan en la Seccion 3 para incorporar cuando el procedimiento vuelva a tocarse, sin retener el documento.

## 6. Ultrasonic Thickness Procedure Rev C — P22-BA-09-000-016

**Origen:** Rev B, Codigo 3 en el TM N35. Es el unico de los tres procedimientos de ensayos no destructivos que seguia en Codigo 3.

**Verificacion:**

| Punto | Pedido | Verificado en la Rev C | Estado |
|---|---|---|---|
| OBS-01 | Declarar el criterio del NDE Plan en la clausula 9.0 y escribir el material como UNS S32750 | La clausula 9.0 remite ahora al NDE Plan `P22-BA-09-000-005` Rev C y declara el material como `UNS S32750`. Ya no cita SA-790. `UNS2750` y `S32250` desaparecieron | **Cerrado en lo esencial** — cita el documento que gobierna, pero no escribe el criterio (espesor medido mayor o igual al minimo requerido) |
| NOTE-01 | Declarar la velocidad sonica como valor y corregir el segundo grado | `S32250` corregido. La velocidad sonica sigue sin declararse como valor numerico | **Parcial** |
| NOTE-02 (a) | Acoplante coherente | `Wallpaper Paste` desaparecio | **Cerrado** |
| NOTE-02 (b) | Lista de referencias | `ASME E 797` y los codigos de inspeccion en servicio API 510, 570 y 653 desaparecieron. Quedan `SA790` y `SA79M` | **Parcial** |
| NOTE-02 (c) | Caratula: no es un procedimiento de identificacion positiva de material, y el articulo correcto | La descripcion como identificacion positiva de material desaparecio. La clausula 4.0 sigue citando **`ASME Section V, Article 9`**. El Articulo 9 es examen visual; la medicion de espesor por ultrasonido es el **Articulo 5** | **Abierto** |
| NOTE-02 (d) | Emitir con hoja de comentarios | La Rev C trae hoja de comentarios consolidada | **Cerrado** |

El Articulo 9 se declaro corregido y no se corrigio. Es la segunda vez.

### Disposicion

**Codigo 2 — Approved as noted.** El determinante que sostenia el Codigo 3 cerro: la clausula 9.0 ya remite al NDE Plan aprobado. Lo que queda son cuatro correcciones de referencia incorporables al emitir Rev 0, sin revision intermedia.

## 7. Datasheet of RO High Pressure Pump Rev 0 — P22-ET-09-009-002

**Origen:** Rev E, Codigo 1 en el TM N36, sin accion sobre el contenido. La unica condicion era emitir en Rev 0 apto para construccion.

**Verificacion:** emitido en Rev 0 IFC. Contenido sin cambios respecto de la Rev E salvo el bloque de revision y la supresion de la hoja de comentarios, que no tenia comentarios que responder. Motor GE consistente en los dos bloques de datos.

### Disposicion

**Codigo 1 — Approved.** Condicion cumplida.

## 8. Line List Rev 1 — P22-LI-09-009-003

**Origen:** Rev 0, Codigo 1 en el TM N29. Sin condicion abierta; solo registrar en el historial la correccion de presion de diseno de `09-016`.

**Verificacion — diff fila por fila contra la Rev 0 aprobada:**

- **Ocho lineas nuevas:** `CP-SS316-DN150-09-022` (reemplaza a `CP-PVC-DN150-09-022`), `RD-PVC-DN15-09-046`, y los seis spools de super duplex de baja presion `09-047` a `09-052`.
- **La columna HYDROTEST no cambio en ninguna linea comun.** Las presiones que ADASA viene exigiendo (75, 90, 120 y 135 barG segun la linea) siguen identicas. Esto importa: no mueve la base de los ensayos ya reclamados.
- Cambios menores en lineas comunes: caudal de `09-044` y `09-045` de menos de 1 a 54 y 36 m3/h; presion de operacion de `DA-SSD-DN100-09-003` de 51 a 49 bar; redondeos.
- Los seis spools de baja presion entran con hidrostatica de **7,5 barG**, que documenta formalmente la base de los ensayos que Bureau Veritas dio por conformes el 20 y 21 de agosto.

**Cambio de material:** `CP-PVC-DN150-09-022` pasa a `CP-SS316-DN150-09-022`, succion de la bomba CIP, declarado por no conseguir un reductor excentrico de PVC. La columna de ensayo no destructivo pasa de no aplica a liquidos penetrantes, coherente con una linea metalica. El P&ID Rev 0 lo recoge con el mismo TAG.

**Contradiccion con el P&ID:** ver la tabla de la Seccion 4 de este analisis.

### Disposicion

**Codigo 1 — Approved.** No habia condicion abierta, y la regla del proyecto no da Codigo 2 sobre un documento ya emitido para construccion. El cambio de material se acepta como sustitucion menor por disponibilidad. **Las dos medidas invertidas se corrigen contra el valor que ADASA declara en la Seccion 3**, sin reemitir la lista: el transmittal deja la cifra escrita en el registro aunque el documento no vuelva a emitirse, que es lo que la regla del N36 contempla para un Codigo 1 con puntos sin levantar.

## 9. Datasheet of Feed Turbocharger Rev 0 — P22-ET-09-009-007

**Origen:** Rev E, Codigo 2 en el TM N36. Condicion: borrar `STYLE 77` de las cuatro llamadas de conexion, dejando la designacion de ranura y `PIEDMONT STYLE S`.

**Verificacion:** la lamina de contorno lee ahora `FEED OUTLET / PIEDMONT STYLE S / 2" CUT GROOVE`, `FEED INLET / PIEDMONT STYLE S / 2" CUT GROOVE`, `BRINE INLET / PIEDMONT STYLE S / 1.5" CUT GROOVE` y `BRINE OUTLET / PIEDMONT STYLE S / 1.5" CUT GROOVE`. **Las cuatro llamadas quedaron limpias.** La unica ocurrencia de `STYLE 77` que queda en el archivo esta dentro de la hoja de comentarios, citando la propia instruccion de ADASA.

### Disposicion

**Codigo 1 — Approved.** Condicion cumplida y emitido en Rev 0 IFC.

## 10. Datasheet of Interstage Turbocharger Rev 0 — P22-ET-09-009-008

**Origen y condicion:** identicos al 007.

**Verificacion:** identica. Las cuatro llamadas limpias, `STYLE 77` solo en la hoja de comentarios.

### Disposicion

**Codigo 1 — Approved.**

> Con los tres datasheets Fedco en Rev 0 IFC, el compromiso que exigia emitirlos sin revision de aprobacion intermedia queda cumplido.

## 11. Equipment List Rev 0 — P22-LI-09-005-001

**Origen:** Rev B, Codigo 2 en el TM N11, que no levanto observaciones nuevas. Lo exigible viene del compromiso escrito en la hoja de comentarios del modelo 3D: reemitirla alineada al desglose de recipientes.

**Verificacion:** la Rev 0 declara tres cambios propios (especificacion de los filtros de cartucho RO y CIP, TAG individuales para los recipientes en linea con el modelo 3D, y specs del motor de la bomba de alta) y ahora trae:

| TAG | Descripcion | Cantidad |
|---|---|---|
| `BOI-09-001` | Stage 1: SWRO Membrane, 7 por recipiente | 42 total |
| `BOI-09-001-1` a `-6` | Stage 1: RO PV, Protec BPV-8-1200-SP-7 | **6** |
| `BOI-09-002` | Stage 2: UHPRO Membrane, 7 por recipiente | 28 total |
| `BOI-09-002-1` a `-4` | Stage 2: RO PV, Protec BPV-8-1800-SP-7 | **4** |

El desglose es internamente coherente: 42 membranas a 7 por recipiente dan 6 recipientes en primera etapa, y 28 a 7 dan 4 en segunda. **La reconciliacion comprometida se hizo.**

Queda una diferencia con el modelo 3D Rev A, que traia cinco recipientes en primera etapa contra los seis de esta lista. La lista aprobada gobierna; lo que debe alinearse es el modelo. Va a la Seccion 3.

**No llego la Valve List `P22-LI-09-005-002`**, que estaba comprometida en el mismo par.

### Disposicion

**Codigo 1 — Approved.** El compromiso sobre este documento se cumplio. La Valve List es un entregable distinto y sigue pendiente, agravado por el cambio de placa de orificio a valvula reductora que el propio P&ID dice que obliga a reemitirla.

## 12. Instrument List Rev F — P22-LI-09-008-003

**Origen:** Rev E, Codigo 1 en el TM N20. El determinante es posterior y viene de otro documento: ADASA declaro en el TM N34 el rango vinculante de `VT-09-001`.

**Verificacion:**

| Punto | Pedido | Verificado en la Rev F | Estado |
|---|---|---|---|
| N34 | `VT-09-001` en 0 a 12 mm/s rms | La fila lee `0.0 / 12.0 mm/s rms`, contra `0.0 / 8.9` de la Rev E. Alarmas en 2,3 y 4,5 sin cambio | **Cerrado** |

El disparo de alta-alta por vibracion de 10,0 mm/s de la Alarm and Interlock List Rev 0 queda ahora dentro del rango del instrumento, y el enclavamiento de parada de la bomba de alta puede actuar.

`VT-09-002` y `VT-09-003`, los dos turbochargers, siguen en `0.0 / 8.9 mm/s rms`. ADASA solo declaro vinculante el rango de `VT-09-001`, de modo que esto **no es un incumplimiento**: es una consulta de consistencia que se documenta, porque son el mismo transmisor Wilcoxon PCH420V-M12 en el mismo servicio.

### Disposicion

**Codigo 1 — Approved.** Emitir en Rev 0 apto para construccion.

## 13. HMI Display Screenshot Rev C — P22-LI-09-008-016

**Origen:** Rev B, Codigo 2 en el TM N31. Condicion: agregar las lecturas de variables electricas y expresar la potencia en kW, y reconciliar seis TAG contra las listas aprobadas, ademas de declarar donde se muestran `PIT-09-008` y `FIT-09-002`.

**La hoja de comentarios declara solo dos acciones. La verificacion por render de las pantallas muestra que hicieron mas de lo que declararon.**

| Punto | Pedido | Verificado por render | Estado |
|---|---|---|---|
| OBS-01 | Voltaje, corriente y potencia en kW | **Seccion 7.7 Digital Power Meter, nueva**: tensiones de linea L1/L2/L3 y linea-neutro, corriente por fase, potencia activa en kW, potencia reactiva, frecuencia, factor de potencia y energia activa | **Cerrado** |
| OBS-02 | `LS-09-002` en nivel bajo y `LS-09-001` en alto | Pantalla 7.1: `TANK LSL — LS-09-002` y `TANK LSH — LS-09-001` | **Cerrado** |
| OBS-03 | `BH-09-001` en la bomba de alta | Pantalla 7.2: la bomba lee `BH-09-001`. La 7.5 mantiene `BH-09-002` en la bomba CIP | **Cerrado** |
| OBS-04 | `TE-09-001` en devanado, `TE-09-002` en rodamiento | Pantalla 7.2: `TE-09-001` y `TE-09-002`, distintos | **Cerrado** |
| OBS-05 | `VE-09-005` en la derivacion de reposicion CIP | Pantalla 7.3: la valvula a MAKE-UP CIP lee `VE-09-005` | **Cerrado** |
| OBS-06 | `PIT-09-003` en la alimentacion de primera etapa | **NO cerrado, e invertido.** La pantalla 7.3 mantiene `PIT-09-005` aguas arriba de `BOI-09-001`, y la 7.4 pasa a mostrar `PIT-09-003` aguas arriba de `BOI-09-002`. La Instrument List Rev F define `PIT-09-003` como RO 1st Stage Feed y `PIT-09-005` como RO 2nd Stage Feed: los dos quedaron cruzados | **Abierto** |
| OBS-07 | `FIT-09-004` en la linea de rechazo a drenaje de salmuera | Pantalla 7.3: `FIT-09-004` en la linea a BRINE TO DRAIN | **Cerrado** |
| Adicional | Declarar donde se muestran `PIT-09-008` y `FIT-09-002` | `PIT-09-008` en la pantalla 7.3, `FIT-09-002` en la 7.4 | **Cerrado** |

**Seis de siete observaciones cerradas y una invertida.** BW Water marco con recuadro rojo cada cambio, incluido el de la pantalla 7.4, lo que confirma que toco `PIT-09-003` deliberadamente y lo puso en la pantalla equivocada.

**Cierre de INT-12:** las pantallas declaran el mapeo de sensores de temperatura — `TE-09-001` y `TE-09-002` en la bomba de alta, `TE-09-003` y `TE-09-004` en la bomba CIP. El compromiso interno queda cerrado.

Los valores que muestran las capturas son de simulacion. La verificacion visual completa de las pantallas sigue reservada al FAT, como se declaro en el TM N31.

### Disposicion

**Codigo 2 — Approved as noted.** Al emitir en Rev 0 hay que intercambiar `PIT-09-003` y `PIT-09-005` entre las pantallas de primera y segunda etapa.

## 14. PLC/LCP FAT Procedure - Hardware Rev C — P22-PP-09-000-001

**Origen:** Rev B, Codigo 3 en el TM N37. Era el documento que fijaba el codigo del transmittal entero.

**Verificacion:**

| Punto | Pedido | Verificado en la Rev C | Estado |
|---|---|---|---|
| OBS-01 | Emitir el procedimiento como procedimiento, separado de todo registro, y avisar cada punto de testigo y detencion | La Rev B eran 16 paginas fotografiadas con 1.378 caracteres extraibles, once de ellas solo con la marca de agua de CamScanner. **La Rev C es nativa, 23 paginas, 50.980 caracteres**, con los campos de lugar y fecha del FAT en blanco, columnas de aprobado y rechazado por llenar y la seccion de punchlist como tabla vacia de quince filas con sus tres casillas de firma. Y BW Water responde por escrito que hara otro FAT en Penang con testigo de ADASA y de un tercero, contra el procedimiento aprobado | **Cerrado** |
| OBS-02 | Cerrar los ocho items categoria A con fecha objetivo, fecha real, estado y firma, testificado | No se cierra aqui, y **no puede**: al separar el procedimiento del registro, esos ocho items pertenecen al registro de la Rev B. Su cierre firmado es ahora un entregable aparte | **Se traslada a la Seccion 3** |
| OBS-03 | Citar el esquematico y la I/O List por codigo y revision emitida | La Rev C cita `P22-LI-09-008-001 Rev.6`, `P22-CD-09-008-001 Rev.1` y `P22-CD-09-008-002 Rev.C`. Codigos y revisiones reales | **Cerrado** |
| OBS-04 entradas | Reconciliar las cuatro entradas digitales del modulo `-A2` | Los canales 1 a 4 se declaran ahora canales de reserva, con `XT001`, `XA002`, `XT002` y `XT003` rotulados como tales. Coincide con el esquematico Rev B y con la I/O List Rev 6, que los da de baja | **Cerrado** |
| OBS-04 salidas | Reconciliar el mapa de reles | **NO cerrado.** ADASA declara cual gobierna: la I/O List Rev 6, aprobada en Codigo 1, lleva ese servicio como **item 108, `REL-09-001-HS001`, salida digital de contacto seco**, de modo que `KA8` no es de reserva y la columna de observaciones de esa fila es la que esta mal. El `HS001` repetido en cinco salidas es el **sufijo del TAG**: la lista los lleva completos con el prefijo del equipo | **Abierto** |
| OBS-05 | Modelo, numero de serie y certificado de calibracion de cada instrumento de ensayo | El requisito 3 de seguridad se mantiene y remite a la seccion de equipos de ensayo, que como corresponde a un procedimiento en blanco esta por completar en el ensayo | **Cerrado en estructura** |
| NOTE-01 | Un solo numero de documento y un solo indice de revision | `P22-PP-09-000-001` aparece 34 veces de forma consistente; las tres menciones a `P22-ET-09-008` estan dentro de la hoja de comentarios | **Cerrado** |
| NOTE-02 | Como cierra BW Water la brecha del terminal de operacion | El cuerpo sigue especificando el terminal `2711P-T10C21D8S`. El `-D9P` solo aparece en la hoja de comentarios. La respuesta se esperaba sobre el esquematico, que no vino en este lote | **Abierto, se traslada** |

**Dato favorable adicional:** la tabla de inspeccion visual del panel declara ahora la materialidad exterior e interior de forma explicita — cuerpo y puerta SUS316L 2,0 mm, plinto SUS316L 2,5 mm, puerta batiente interior en acero laminado 2,0 mm pintado RAL 7035 y placa de montaje galvanizada 2,5 mm — que es la distribucion que ADASA acepto.

### Disposicion

**Codigo 2 — Approved as noted.** El determinante del Codigo 3 cerro: el documento es hoy un procedimiento, no el registro de un ensayo corrido. Al emitir en Rev 0 hay que resolver la fila del rele KA8 y los TAG repetidos de salida.

## 15. Resumen de disposicion

| # | Documento | Rev | Emision | Codigo previo | **Propuesto** | CC_ADASA |
|---|---|---|---|---|---|---|
| 2.1 | P&ID | 0 | IFC | 1 (N18) | **1** | no |
| 2.2 | Liquid Penetrant Examination Procedure | 0 | IFC | 2 (N37) | **1** | no |
| 2.3 | Ultrasonic Thickness Procedure | C | IFA | 3 (N35) | **2** | si |
| 2.4 | Datasheet of RO High Pressure Pump | 0 | IFC | 1 (N36) | **1** | no |
| 2.5 | Line List | 1 | IFC | 1 (N29) | **1** | no |
| 2.6 | Datasheet of Feed Turbocharger | 0 | IFC | 2 (N36) | **1** | no |
| 2.7 | Datasheet of Interstage Turbocharger | 0 | IFC | 2 (N36) | **1** | no |
| 2.8 | Equipment List | 0 | IFC | 2 (N11) | **1** | no |
| 2.9 | Instrument List | F | IFA | 1 (N20) | **1** | no |
| 2.10 | HMI Display Screenshot | C | IFA | 2 (N31) | **2** | si |
| 2.11 | PLC/LCP FAT Procedure - Hardware | C | IFA | 3 (N37) | **2** | si |

**Veredicto global: 2 — Approved as noted.** Ocho Codigo 1 y tres Codigo 2. **Cero Codigo 3.**

**Efecto en el Master Register**, desde 64 / 21 / 4 / 0: suben a Codigo 1 el Liquid Penetrant, los dos turbochargers y la Equipment List; suben de 3 a 2 el ultrasonido y el procedimiento de FAT. **Tally esperado 68 / 19 / 2 / 0.** Sin items nuevos: los once son re-revisiones. Entregas 88 a 90; transmittals 37 a 38.

**Los dos unicos documentos que quedan en Codigo 3 son el O&M Manual y el Dossier Index — dos de los cinco que no llegaron.**

## 16. Seccion de pendientes

**Lo que no llego, con su consecuencia ya declarada en el N37.** Los cinco items, mas la Valve List y el plan de entrega del dossier.

**Los tres mas graves**, todos exigidos nominalmente el jueves y ausentes: los once planos de taller, el dossier del item 65 y el informe estructural endosado.

**Entra a la lista con este transmittal:**

- Las dos medidas invertidas de los spools de rechazo CIP a baja presion, que ADASA declara vinculantes: `CP-SSD-DN80-09-049` en primera etapa y `CP-SSD-DN65-09-048` en segunda, a corregir en la Line List antes de fabricar.
- El cambio de succion CIP a SS316, aceptado, a reflejar en la Valve List y en los planos de fabricacion.
- El cambio de placa de orificio a valvula reductora en `CIT-09-004`, que obliga a reemitir la Valve List.
- El cierre firmado de los ocho items categoria A del punchlist del registro de la Rev B.
- El desglose de recipientes del modelo 3D, que debe pasar de cinco a seis en primera etapa para alinearse con la Equipment List aprobada.
- El numero de documento del procedimiento de liquidos penetrantes.

**Cierra y sale de la lista:** el rango de `VT-09-001`, el borrado de `STYLE 77` en los dos turbochargers, la emision en Rev 0 de los tres datasheets Fedco, el mapeo de sensores de temperatura y la reconciliacion de las cuatro entradas digitales.

## 17. Que NO puede cruzar al documento emitido

- **La fecha del FAT.** La Nota Tecnica `P22-NT-09-000-003-0` dejo en disputa cual ventana gobierna. Se dice que es antes de que abra el FAT, sin fecha.
- **Cifras de multa y el umbral de treinta dias.** `INT-08` sigue abierto.
- **Codigos internos** `PRG-`, `INT-`, `BV-`, Van Doorn, y el saldo de jornadas de Bureau Veritas.
- **El simbolo de seccion** en cualquier archivo persistido.
- **El factor de potencia y demas valores de simulacion** de la pantalla 7.7: son datos de prueba y la verificacion visual quedo reservada al FAT desde el TM N31. Objetarlos ahora seria exceso de alcance.
