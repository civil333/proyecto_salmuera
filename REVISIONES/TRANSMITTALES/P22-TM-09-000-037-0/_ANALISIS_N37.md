---
titulo: Analisis interno — Transmittal N37 (P22-TM-09-000-037-0)
codigo: P22-TM-09-000-037-0
fecha: 2026-08-28
estado: INTERNO — BORRADOR, disposicion en revision del usuario
type: analisis
project: salmuera-taltal
---

# Analisis interno — Transmittal N37

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Tres submittals sin responder: `25007-0086`, `25007-0087` y `25007-0088`. **Siete documentos.**

El cierre punto por punto de cada documento vive en el `_LEDGER_COMENTARIOS.md` de su entrega. La disposicion se resuelve en las secciones 3 a 9.

---

## 1. Recepcion y plazos

| Submittal | Emitido | Emision para | Devolucion pedida por BW | Vencimiento real, Clausula 37.2 |
|---|---|---|---|---|
| `25007-0086` | jue 27-Ago-2026 | **IFA** cuatro documentos, **IFC** la IO List | **dom 30-Ago-2026** | **lun 7-Sep-2026** |
| `25007-0087` | jue 27-Ago-2026 | **IFC** | **dom 30-Ago-2026** | **lun 7-Sep-2026** |
| `25007-0088` | vie 28-Ago-2026 | **IFA** | lun 31-Ago-2026 | **mar 8-Sep-2026** |

**La columna de emision decide la disposicion.** Un documento sometido para aprobacion no ha llegado a la fecha en que vencen las condiciones que su Codigo 2 anterior difirio al Rev 0; uno sometido para construccion si. La unica excepcion es una condicion que el transmittal anterior amarro a un hito distinto del Rev 0: entonces vence en ese hito, y es exactamente el caso del procedimiento del FAT.

**Dos hechos contractuales que se declaran como constancia, sin convertirlos en observacion de documento:**

1. **Dos de las tres submittals piden devolucion el domingo 30-Ago**, tres dias corridos despues de emitidas, contra los siete dias habiles de la Clausula 37.2 de las Bases Administrativas Especiales. Es el quinto lote consecutivo con fecha de devolucion por debajo del plazo contractual, y la segunda vez que cae en fin de semana.
2. **El plazo de revision del `25007-0088` vence el 8 de septiembre, un dia despues de que abre el FAT del modulo.** El documento de puerta de esa prueba se somete tan tarde que su propio plazo contractual de revision expira con la prueba ya iniciada.

Los vencimientos se computan sobre la fecha de emision declarada en cada Submittal Form, que es el dato del propio documento. Las fechas de archivo no se usan: el repositorio de correo entrante lleva sin capturar desde el 06-Ago.

---

## 2. Higiene de carpeta

- **`25007-0086`** llego como un unico archivo comprimido, `TALTAL_ DOCUMENT SUBMISSION 25007-0086.zip`, que se descomprimio en la carpeta conservando el original. Contiene los cinco documentos declarados mas el Submittal Form: **la lista real coincide con la declarada**, sin archivos nativos adicionales y sin faltantes. Se hasheo cada archivo interno.
- **`25007-0087` y `25007-0088` comparten la carpeta `ENTREGA 88`**, porque llegaron en el mismo correo del 28-Ago. La carpeta trae los dos formularios y tres archivos: el plano de puntos de conexion en PDF y en su nativo `.dwg`, y el procedimiento del FAT en PDF. **Ningun documento declarado falta**; el `.dwg` es el archivo nativo que el formulario no enumera porque lista documentos y no ficheros.
- **Anomalia de numeracion de carpetas, que se documenta y no se corrige.** La carpeta `ENTREGA 87` aloja el submittal `25007-0073` —la Alarm and Interlock List Rev 0 y el Control and Sequence Chart Rev 0, dispuestos en el TM N34— y **la carpeta `ENTREGA 73` no existe**. El correlativo 87 quedo asi ocupado por un contenido que no le corresponde, y el submittal `25007-0087` real vive en `ENTREGA 88`. Renombrar rompe las rutas citadas en el README, en transmittals ya emitidos y en las memorias del proyecto, de modo que se deja constancia y no se mueve nada. **La serie de submittals del proveedor sigue sin numeros ausentes**; el hueco es de la numeracion interna de carpetas.
- **Triaje de los siete documentos antes de extraer.** Cinco traen capa de texto nativa y se extrajeron directo. Dos exigieron otro tratamiento: el **Instrument Location Layout** y el **Tie-In Point Layout** son planos, con 12.060 y 75.633 objetos vectoriales y una lamina rotada 270 grados el segundo, y se leyeron en modo plano mas render. El **procedimiento del FAT** es el caso extremo: dieciseis paginas con 1.378 caracteres extraibles en total, de las cuales once devuelven unicamente la marca de agua `CamScanner`. Es un documento **fotografiado**, y toda cifra citada de el se confirmo sobre render a 200 dpi.

---

## 3. Liquid Penetrant Examination Procedure Rev C — `P22-BA-09-000-014`

**Origen:** Rev B, **Codigo 3** en el TM N35, que venia del TM N32. **IFA.** Detalle en `ENTREGAS_BWWATER/ENTREGA 86/_LEDGER_COMENTARIOS.md`.

**Que cerro.** El determinante. La clausula 13.0 ofrece hoy **un solo criterio de aceptacion** —`ASME B31.3 para. 341.3.2`, con sus umbrales— y el bloque del Apendice 6 de la Seccion VIII Div. 1 fue eliminado. El formulario que firma el examinador declara ese mismo criterio y marca la casilla de B31.3, donde antes declaraba el Apendice 8. El examinador ya no elige. Cerraron tambien la frase de proposito de la portada y la alineacion de ediciones.

**Que no.** 🔴 El **formulario de informe sigue intacto**, con el numero de informe y el numero de trabajo de **otro contrato**, los tres numeros de lote de los consumibles y la columna de observaciones **pre-escrita** con el resultado *"No Relevant Indication Was Found During PT Examination Time"*. Es la hoja que entra al dossier de calidad y es la **segunda vez** que se levanta. Dentro de ese mismo formulario, el campo del procedimiento sigue en `Rev.00` cuando el documento es Rev C. Y el numero de documento de la pagina 2 sigue siendo el de un procedimiento de identificacion positiva de material.

🔴 **La hoja de comentarios declara un cierre que no ocurrio.** Responde `Revised as per comment` a un bloque que nombra textualmente *"the report form data of another contract"*.

### Disposicion

**Codigo 2 — Approved as noted.** El determinante cerro, de modo que el Codigo 3 ya no se sostiene. Pero el documento mismo debe cambiar antes de emitirse en Rev 0, y el documento se somete para aprobacion, de modo que el Codigo 2 es el que corresponde. **Lleva CC_ADASA.**

---

## 4. Radiography Examination Procedure Rev C — `P22-BA-09-000-015`

**Origen:** Rev B, **Codigo 3** en el TM N35. **IFA.**

**Que cerro.** El determinante, en sus dos mitades. La lista de cinco codigos de la clausula 23.0 bajo a uno y la lista de referencias de la clausula 2.0 bajo de cinco a dos. Y el limite de borrosidad geometrica de **1,8 mm** —que era la dispensa del parrafo PW-51.1 de ASME Seccion I para items con sello PP, y que B31.3 no concede— **desaparecio del cuerpo** y fue reemplazado por los **0,020 in.** de la Tabla T-274 del Articulo 2, con el texto de T-274 reproducido integro. Cerro tambien la renumeracion de las sub-clausulas, que corrian un numero por detras de sus propios encabezados.

**Que no.** El **alcance sigue siendo generico**: la clausula 1.0 declara *"Stainless, Carbon, low alloy and high alloy steel welds up to 3-inch thickness"* y no nombra el `ASTM A790 UNS S32750` ni el rango de 6,02 a 8,56 mm de pared que efectivamente se radiografia en este modulo. El numero de documento de la portada sigue siendo el de un procedimiento de identificacion positiva de material.

**La hoja de comentarios trae dos filas, OBS-01 y OBS-02, y no incluye la NOTE-01**, de modo que los tres items de aseo no se respondieron como fila.

### Disposicion

**Codigo 2 — Approved as noted.** Mismo razonamiento que el de penetrantes: el determinante cerro y el documento mismo debe cambiar antes del Rev 0. **Lleva CC_ADASA.**

---

## 5. PLC/LCP Schematic Diagram Rev B — `P22-CD-09-008-002`

**Origen:** Rev A, **Codigo 2** en el TM N20, subseccion 2.7, con una sola NOTE-01. **IFA.**

**Trae hoja de comentarios**, fechada el 24-Ago-2026, con un solo item. La NOTE-01 pedia confirmar la asignacion de entradas y salidas despues de emitida la Control Philosophy Rev D; la respuesta remite a una *"I/O List Rev B"* que **no existe**, porque esa lista lleva revisiones numericas y va en la Rev 6.

**La reconciliacion esta casi hecha, y le falta un borne.** La lamina 39 cablea la salida del calentador de CIP en el modulo `-A4`, salida 7, con el rele `KA8`; las entradas 1 a 4 de la lamina 35 figuran como reserva, coherente con las tres filas que la Rev 6 elimino; y las señales de auto, manual y falla del equipo de aire acondicionado estan en las laminas 37 y 38. 🔴 Pero **la entrada `CIP HEATER RUNNING`, que es el item 109 de la I/O List Rev 6, no tiene borne en ninguna de las cuatro laminas de entradas digitales**: diecinueve entradas asignadas contra veinte activas en la lista, con trece bornes libres. La salida del calentador se cableo y su realimentacion de marcha no.

🔴 **El terminal de operacion sigue siendo el `2711P-T10C21D8S`.** Verificado por render de la **lamina 28**, fila 11 de la lista de materiales del tablero de control: `HMI1 | 1 | Touch Screen | 2711P-T10C21D8S | Allen-Bradley`. Es la unica aparicion del numero de catalogo completo en las 71 laminas, y **la hoja de comentarios no trae ninguna fila para este punto**. En el **TM N30** ADASA **declaro vinculante** el `2711P-T10C22D9P` —dos puertos Ethernet RJ45 y 1 GB segun las filas 15 y 18 del datasheet aprobado— frente a ese mismo `-D8S`, de un puerto y 512 MB, y nombro a este esquematico entre los cuatro documentos a corregir. **No se corrigio.**

**Y el punto dejo de ser documental.** El registro del FAT del tablero, en la ENTREGA 88, visa la fila *"Verify HMI (HMI1: 2711P-T10C21D8S, Allen-Bradley) is installed on inner door"*: **el tablero se armo con el `-D8S`**.

### Disposicion

**Codigo 2 — Approved as noted**, reiterando la condicion con constancia de que es el segundo ciclo. El documento se somete para aprobacion, de modo que la condicion de su Codigo 2 anterior aun no vence, y escalar contradiria la propia frase de ADASA. **Lleva CC_ADASA.**

> **Decision que excede al transmittal y corresponde al usuario.** ADASA declaro vinculante el `-D9P` y el tablero se construyo con el `-D8S`. Caben dos caminos, y el transmittal debe reflejar el que se elija: exigir el terminal declarado, con impacto de plazo a dias del FAT; o aceptar el `-D8S` y exigir por escrito como cumple el requisito de dos puertos Ethernet del datasheet aprobado, alineando los cuatro documentos. Mientras no se decida, el bloque de accion pide **confirmar por escrito cual esta instalado**.

---

## 6. Instrument Location Layout Rev D — `P22-DWG-09-008-001`

**Origen:** Rev C, **Codigo 3** en el TM N23, subseccion 2.6, con cuatro observaciones. **IFA.** Es uno de los tres planos cuya reemision el TM N31 reclamo contra el reporte de estado del proveedor, con fecha comprometida vencida el **2-Ago**.

**Trae hoja de comentarios**, pagina 4, fechada el 24-Ago-2026, con las cuatro observaciones transcritas.

| Punto | Estado |
|---|---|
| **OBS-01** — la letra de revision se reutilizo y dos planos compartian el identificador Rev C | **Cierre parcial.** La emision avanzo a **Rev D** y la ambiguedad ya no afecta a la revision vigente. Pero el bloque `REVISIONS` de las laminas sigue **vacio**, sin fila, sin numero de aviso de cambio y sin descripcion: verificado por render del cajetin a 300 dpi. La respuesta de BW Water no contesta el punto, habla de otra cosa |
| **OBS-02** — la geometria estaba amarrada al Equipment Layout superado, abierto en Codigo 3 | **Cerrado en sustancia.** La respuesta declara *"Instrument Location RevD has been updated based on approved P22-DWG-09-005-003_Equipment Layout_Rev.D"*, y ese Equipment Layout Rev D **cerro en Codigo 1 en el TM N33**: la dependencia se levanto. Pero esa declaracion vive **solo en la hoja de respuesta**: la cadena `005-003` aparece una sola vez en todo el archivo, el cuadro de notas de las dos laminas esta vacio y no hay lista de documentos de referencia |
| **OBS-03** — el codigo del cajetin frontal a dos digitos | **Cerrado.** Los cajetines leen `P22-DWG-09-008-001-P1` y `-P2`, con tres digitos, y `REV.: D`. En la Rev C el cajetin de lamina ya venia correcto: el error de dos digitos vivia solo en la caratula, que es lo que decia la observacion |
| **OBS-04** — la Rev C llevaba dos fechas de emision | **Cerrado.** El encabezado dice 24/8/2026 y las tres firmas del cajetin, `AUG.24.26` |

### Disposicion

**Codigo 2 — Approved as noted.** El determinante —la dependencia con un plano superado en Codigo 3— cerro, de modo que el Codigo 3 no se sostiene. Quedan dos cambios al propio plano: que el registro de revisiones diga que cambio en cada emision en vez de repetir la misma frase cuatro veces, y que el plano declare en su cuadro de notas contra que revision del Equipment Layout esta dibujado, que hoy solo consta en la hoja de respuesta. **Lleva CC_ADASA.**

> **No se exige la columna de aviso de cambio.** Esta vacia en las cuatro filas de este plano y tambien en las del Equipment Layout Rev D, de modo que apunta a que BW Water no usa esa numeracion en el proyecto y no a un incumplimiento.

> **CORRECCION del 31-Ago-2026, verificada por render propio.** La frase de la fila del OBS-01 que dice que el bloque `REVISIONS` sigue **vacio** es **incorrecta**. El bloque trae **cuatro filas** —D `AUG.24.26`, C `JUN.16.26`, B `FEB.27.26`, A `JAN.17.26`, todas `BT`/`JFR`— con la columna `ECN.` en blanco y **la misma descripcion `ISSUED FOR APPROVAL` en las cuatro**, de modo que ninguna dice que cambio. El `_LEDGER_COMENTARIOS.md` de la ENTREGA 86 lo tenia bien y este analisis no. Ademas se confirmo la reescritura de la fila historica: la Rev C emitida (ENTREGA 52) la fecha `APR.17.26` y la Rev D la fecha `JUN.16.26`, de modo que la emision de abril desaparecio del historial en vez de distinguirse de la de junio. **El transmittal emitido lleva la version corregida.** Renders en `COMENTARIOS/_render/`.

> **Dependencia que no degrada y va a la seccion de pendientes:** la respuesta al OBS-01 declara que la Rev D se basa en la **Instrument List Rev E**, que es justamente la lista cuya reemision ADASA exige con `VT-09-001` rangeado de 0 a 12 mm/s rms.

---

## 7. I/O List Rev 6 — `P22-LI-09-008-001`

**Origen:** Rev 5, **Codigo 2** en el TM N28, con **una sola** accion. **Emitida para construccion (IFC).**

**Trae hoja de comentarios** que transcribe el pedido integro y responde *"HAS BEEN REVISED IN I/O LIST - P22-LI-09-008-001 REV6. Heater Start and Running feedback has been added."*

**Verificado sobre la lista y no sobre la declaracion.** La fila 108 es `REL-09-001`, `HS001`, `CIP HEATER ON/OFF COMMAND`, del PLC al tablero de control del calentador, tipo `DO`, contacto seco normalmente abierto de 24 VDC, revision `6`. La fila 109 es `REL-09-001`, `XB002`, `CIP HEATER RUNNING`, en sentido inverso, tipo `DI`, revision `6`.

### Disposicion

**Codigo 1 — Approved.** La unica condicion cerro. La lista se emite para construccion, de modo que la condicion vencio y solo caben Codigo 1 o Codigo 3; no hay defecto sustantivo. **Sin CC_ADASA.**

---

## 8. Tie-In Point Layout Rev 0 — `P22-DWG-09-005-005`

**Origen:** Rev B, **Codigo 2** en el TM N31, que cerro el Codigo 3 del TM N7 —el documento abierto mas antiguo del proyecto—. **Emitido para construccion (IFC).** Cajetin: `DRAWING STATUS: ISSUED FOR CONSTRUCTION`, `REV.: 0`, `AUG.18.26`.

**Trae hoja de comentarios** fechada el 18/8/2026, con los cinco puntos del TM N7 sobre la Rev A y el bloque de accion del TM N31 sobre la Rev B, respondidos uno por uno.

| Punto | Estado |
|---|---|
| **OBS-01** — declarar la presion de diseño en el punto de conexion de alimentacion de salmuera `TP-DA P8-001`, para verificar compatibilidad con la clase ANSI 150# | **Cerrado, y verificado contra la fuente.** La tabla de puntos de conexion declara ahora una columna `DESIGN PRESSURE` completa, y el `TP-DA P8-001` —alimentacion, 4 pulgadas, clase 150, ASME B16.5— lleva **5 BARG**. Coincide exactamente con la linea `DA-PVC-DN100-09-001`, `SWRO BRINE FEED`, de la **Line List Rev 0 aprobada en Codigo 1 en el TM N29**, que le asigna 3 barG de operacion, **5 barG de diseño** y 7,5 barG de ensayo, en la hoja P8 del diagrama de proceso. La aceptacion condicionada de ADASA a la clase ANSI 150# queda satisfecha con holgura |
| **OBS-02** — completar la clase y el estandar de brida del `TP-AS P11-001`, con la alternativa de *"state on the sheet that this connection is not flanged and how it is made"* | **Respondido, no incorporado al plano.** Las dos celdas siguen en guion y **la palabra `valve` no aparece en ninguna parte de la lamina**. BW Water responde que *"TP-AS P11-001 is not a flanged connection, instead the termination point provided will be the valve itself"*. En la vista de la Seccion 2-2 la flecha de ese punto si aterriza sobre un cuerpo de valvula dibujado, lo que respalda graficamente la respuesta sin enunciarla. Es una respuesta razonada, no una negativa; falta que el plano diga lo que dice la hoja |

### Disposicion

**Codigo 1 — Approved.** El plano se emite para construccion, de modo que solo caben Codigo 1 o Codigo 3, y el Codigo 3 exige un defecto sustantivo. El punto sustantivo —la presion de diseño en el limite de bateria— **cerro y es consistente con la lista aprobada**. Lo que queda es que dos celdas digan guion donde deberian decir que la terminacion es una valvula, que es forma. **Sin CC_ADASA.**

🔴 **El plano se contradice sobre su propio estado.** El campo `DRAWING STATUS` del cajetin dice `ISSUED FOR APPROVAL`, valor arrastrado de la Rev B, mientras la fila de revision del mismo cajetin dice `ISSUED FOR CONSTRUCTION` y el formulario lo somete como IFC. La caratula, ademas, conserva `Revision No.: A` y `Date: 02/04/2026`.

**Bajar el codigo no baja el tono:** el transmittal deja escrito que la terminacion del antiscalante es una valvula y no una brida, segun la propia hoja de comentarios de BW Water, que eso debe quedar en el plano, y que el campo de estado del cajetin y la caratula deben decir lo mismo que la fila de revision. Ninguna de esas correcciones retiene un plano que ya gobierna construccion.

**Cruce que sirve a otro frente:** la respuesta sobre el antiscalante es **directamente pertinente al punto que el TM N36 dejo abierto en el Piping Layout Rev D**, donde la clase de brida de las terminaciones de antiscalante y de CIP sigue sin declararse.

---

## 9. PLC/LCP FAT Procedure - Hardware Rev B — `P22-PP-09-000-001`

**Origen:** Rev A, **Codigo 2 — Approved as noted** en el TM N27, subseccion 2.5. Cinco puntos: OBS-01 mayor sobre los codigos de los planos gobernantes, OBS-02 y OBS-03 menores, NOTE-01 de reconocimiento y NOTE-02 reteniendo el visado de la proteccion por RTD. **Sometido para aprobacion (IFA).** Evidencia completa en `ENTREGAS_BWWATER/ENTREGA 88/_LEDGER_COMENTARIOS.md`.

### La Rev B no es un procedimiento: es el registro de un ensayo ya ejecutado

Las paginas 2 a 16 son fotografias de un ejemplar impreso y llenado a mano, capturadas con CamScanner. El documento contiene el **cierre de FAT firmado** con resultado **PASS WITH PUNCHLIST**, un **punchlist de quince lineas** y un **reporte de rectificacion** de cuatro paginas con fotografias. El ensayo se ejecuto **del 3 al 5 de agosto de 2026 en Ningbo**, veintitres dias antes de someterse.

### 🔴 El punto de fondo: quien firmo

| Casilla | Quien firma | Empresa |
|---|---|---|
| Tested by (Panel Builder) | firma en caracteres chinos | fabricante del tablero, Ningbo |
| **Witnessed by (Client / Third-Party Inspector)** | **Billy Tan** | **BW Water** |
| **Accepted by (BW Water)** | **Chee De Yi** | **KVC Industrial Supplies** |

BW Water firmo la casilla del Comprador y del Tercero Inspector, y el proveedor del tablero firmo la casilla de BW Water. **Las tres firmas del cierre pertenecen a la cadena de suministro.** Ni ADASA ni Bureau Veritas participaron.

**El fundamento es el ITP que ADASA ya aprobo, no una interpretacion.** El `P22-BA-09-000-004` Rev 0, en Codigo 1 desde el TM N26, asigna a ADASA la **W de testigo** en su fila **6.1** (fabricacion de tableros de fuerza y control) y en su fila **6.2** (ensayo electrico de tableros), y esta ultima declara como documento de referencia literal *"GA Drawing & Wiring Diagram/FAT Procedure"*. La leyenda del propio ITP define la W como *"Client or 3rd party witness inspection (**requires notification**). However inspection and test are performed as scheduled, and even if the client or 3rd party is not present."*

**Ese matiz decide el encuadre y hay que respetarlo:** BW Water podia ejecutar el ensayo en su fecha sin esperar a nadie. Lo que no podia era **no avisar**. Reclamar por la ejecucion es refutable con el propio ITP; reclamar por el aviso no lo es. La Clausula 37 de las Bases Administrativas Especiales lo refuerza con dos plazos, diez dias corridos para cualquier ensayo y **treinta dias para suministros internacionales cuando pudiera existir inspeccion de terceros**, que es el caso.

La fila **7.1** del mismo ITP, ademas, es **punto de detencion** de ADASA sobre la aprobacion del procedimiento detallado del FAT. El procedimiento estaba en Codigo 2 con condiciones a incorporar **antes de testificar**, y el ensayo corrio sin incorporarlas.

### Cierre de los cinco puntos del TM N27

| Punto | Estado |
|---|---|
| OBS-01 — citar los codigos CD correctos y la revision emitida del esquematico **antes de testificar** | **No cerrado y agravado.** La tabla de documentos de referencia sigue con `P22-ET-09-008-001 Rev. 3` y `P22-ET-09-008-002 Rev. 5`; ninguna de las dos revisiones existe, el codigo real del esquematico es `P22-CD-09-008-002` y `P22-ET-09-008-001` es el Datasheet of PLC and HMI Panel Component. Una fila del ensayo da por conforme que ese mismo juego documental viaja **dentro del tablero** |
| OBS-02 — TAG de la salida analogica, numero de documento y rotulo de rele | **No cerrado.** El rotulo de rele si quedo bien (`KA3` en el comando de partida). El numero de documento no: la caratula nativa dice `P22-PP-09-000-001` Rev B y el cuerpo escaneado se identifica como `P22-ET-09-008 – FAT Procedure`, `Rev. 0 – Issued for FAT` |
| OBS-03 — dos criterios de aceptacion contra los documentos aprobados | **Cierre parcial.** La mitad de la placa de montaje quedo superada por la resolucion del RFI-002; las señales de marcha de las dosificadoras se siguen ensayando por cierre de contacto |
| NOTE-01 — cobertura completa | **Cerrado.** El rack y los canales de temperatura de los dos motores se mantienen |
| NOTE-02 — el visado de la proteccion por RTD se retiene hasta reconciliar la Alarm and Interlock List | **No respetado.** Los ensayos de RTD aparecen visados el 3 al 5 de agosto; esa lista se reconcilio al emitirse en Rev 0, sometida el 11-Ago y dispuesta en Codigo 1 el 18-Ago |

### 🔴 Ocho no conformidades de categoria A sin cierre firmado

El punchlist define la categoria A como *"Must be resolved BEFORE panel dispatch"*. Las lineas 1 a 8, todas de categoria A y todas levantadas por el propio ingeniero de BW Water, quedan con fecha objetivo, fecha real y estado **en blanco**. El bloque de cierre del punchlist esta **integramente vacio**. Un reporte de rectificacion anexo las declara ejecutadas y probadas con fotografias, **sin firma, sin fecha y sin testigo**.

🔴 **Y el cruce que le da peso:** la **I/O List Rev 6**, que llega en el mismo lote, **ya define esas señales desde las revisiones 3 y 4**, es decir desde junio y julio: `XA001` del interruptor general y `XA003`/`XA004` de las fuentes en la revision 3; `XB002` de marcha, `XT001` de falla, `SI001` de realimentacion de velocidad y `SIC001` de comando de velocidad de la bomba de alta en la revision 4; `YA001` de estado de marcha al sistema de planta en la revision 3. **El tablero se fabrico sin puntos que la lista aprobada lleva desde hace dos y tres revisiones**, y fue el propio ingeniero de BW Water quien los levanto en el ensayo. No es una discusion de esquema blando contra cableado. La lista si absorbio una linea del punchlist: `XA009` de falla del equipo de aire acondicionado entra en la **revision 6**.

Las ocho son señales del variador y de los servicios internos del tablero hacia el sistema de control. No se confunden con las cuatro señales de coordinacion con el sistema de planta, que **si estan y se ensayaron** (`XA005` de habilitacion y `YA001` de marcha, mas `XA001` a `XA004`).

### 🔴 Los tres documentos se contradicen sobre cuatro entradas digitales y sobre el mapa de reles

La seccion 8 del FAT registra visado manuscrito borne por borne, bajo la instruccion impresa *"All tags per approved I/O list"*. Cuatro bornes del modulo `-A2` aparecen visados: `XT001` Incoming MCCB Trip States, `XA002` Disconnect Switch ON Status, `XT002` Feeder Power Failure y `XT003` Common Alarm Signal.

Dieciseis dias despues **la I/O List Rev 6 elimina tres de ellos**, tachados en rojo, y el cuarto no existe en ninguna revision de la lista. Tres dias mas tarde **el esquematico Rev B rotula esos cuatro canales como reserva**. En salidas hay ademas un corrimiento de un rele entre el FAT y el esquematico.

**El limite de la evidencia decide como se redacta.** El cuerpo ejecutado del FAT **no cita la I/O List por codigo ni por revision**, de modo que la nomenclatura de su tabla puede venir de una asignacion anterior. La afirmacion defendible no es que el tablero se construyo distinto de los planos, sino que **los tres documentos se contradicen** sobre esas cuatro entradas y sobre el mapa de reles, y que ninguno de los dos documentos de control dice una palabra sobre el FAT, pese a que la linea 14 del punchlist —*"Drawing Update + CAD update"*— se declara cumplida.

### 🔴 El terminal de operacion instalado es el `-D8S`

Verificado por render: *"Verify HMI (HMI1: `2711P-T10C21D8S`, Allen-Bradley) is installed on inner door"*, visado. En el TM N30 ADASA declaro **vinculante** el `2711P-T10C22D9P`, de dos puertos Ethernet y 1 GB, frente a ese mismo `-D8S` de un puerto y 512 MB. Aquella correccion se traslado a la Seccion de pendientes y no degradaba a ningun documento. Ahora hay evidencia de que **el tablero se armo con el `-D8S`**.

### Otros hechos del registro

Cinco de los seis instrumentos de ensayo van sin modelo y sin numero de serie, y ninguno con certificado de calibracion, contra el requisito de seguridad 3 del propio documento. Un criterio de aceptacion —el dimensionamiento de las prensas de cable— aparece **tachado** y diferido con la anotacion *"open at Malaysia"*, sin visado. La Rev B **no trae hoja de comentarios consolidada**.

### Disposicion propuesta

**Codigo 3 — To be revised.**

El Codigo 3 esta disponible sin contradecir ninguna frase propia de ADASA. La regla que reserva el Codigo 2 reiterado para las emisiones sometidas a aprobacion supone que la condicion **vence al emitir Rev 0**; aqui el TM N27 amarro la condicion a un hito distinto y anterior, *"before witnessing"*, y ese hito ocurrio. Y no se trata de un defecto de forma: el documento ya no se puede aprobar como esta porque es el registro de un ensayo cerrado con ocho no conformidades bloqueantes cuyo levantamiento no firma nadie, ejecutado contra un procedimiento que se remite a dos documentos inexistentes.

**Lleva CC_ADASA.**

**Y una recomendacion que excede al transmittal, para decision del usuario:** el aviso de la Clausula 37 y de la W del ITP hay que exigirlo **hacia adelante**, no solo por lo ocurrido. El FAT del modulo abre el 7 de septiembre y quedan puntos de testigo y de detencion por delante. Eso pertenece a la cadena de inspecciones, no a la de transmittals.

## 10. Resumen de disposicion

| # | Documento | Rev | Emision | Codigo previo | Que falta, en una linea | Codigo | CC_ADASA |
|---|---|---|---|---|---|---|---|
| 1 | Liquid Penetrant Examination Procedure `P22-BA-09-000-014` | C | IFA | 3 (N35) | el formulario de informe sigue con el numero de informe y de trabajo de otro contrato y el resultado pre-escrito, y cita `Rev.00` | **2** | si |
| 2 | Radiography Examination Procedure `P22-BA-09-000-015` | C | IFA | 3 (N35) | el alcance sigue generico y no nombra el super duplex ni el rango de pared que se radiografia | **2** | si |
| 3 | PLC/LCP Schematic Diagram `P22-CD-09-008-002` | B | IFA | 2 (N20) | el terminal sigue en `-D8S` contra el vinculante declarado; falta el borne de la realimentacion de marcha del calentador; y cuatro entradas quedan como reserva contra el registro del FAT | **2** | si |
| 4 | Instrument Location Layout `P22-DWG-09-008-001` | D | IFA | 3 (N23) | las cuatro filas del registro de revisiones repiten la misma descripcion y la fila historica de la Rev C se reescribio; el plano no declara contra que Equipment Layout esta dibujado | **2** | si |
| 5 | I/O List `P22-LI-09-008-001` | 6 | **IFC** | 2 (N28) | nada | **1** | no |
| 6 | Tie-In Point Layout `P22-DWG-09-005-005` | 0 | **IFC** | 2 (N31) | dos celdas de brida en guion donde deberia declararse que la terminacion es una valvula, y el campo de estado del cajetin dice para aprobacion sobre una emision para construccion | **1** | no |
| 7 | PLC/LCP FAT Procedure - Hardware `P22-PP-09-000-001` | B | IFA | 2 (N27) | el ensayo se ejecuto sin aviso y sin testigo del Comprador, tres de los cinco puntos siguen abiertos y ocho no conformidades bloqueantes no tienen cierre firmado | **3** | si |

**Veredicto global: 3 — To be revised. 2 Codigo 1, 4 Codigo 2 y 1 Codigo 3 sobre siete documentos.** El codigo lo fija **un solo documento**, el registro del FAT del tablero.

**Lo que este lote cierra, y conviene tener presente al calibrar el tono:** dos de los tres Codigo 3 mas antiguos del paquete de ensayos no destructivos cerraron su determinante, el Codigo 3 del Instrument Location Layout que llevaba abierto desde el TM N23 cerro su dependencia, y el plano de puntos de conexion —el documento abierto mas antiguo del proyecto hasta el TM N31— llega a Rev 0 con su ultimo punto sustantivo cerrado y verificado contra la Line List aprobada.

---

## 11. Seccion de pendientes de transmittals previos

Los tres mas graves, que se mantienen del TM N36 con un cambio de orden:

| Origen | Documento | Observacion | Estado |
|---|---|---|---|
| N30 | Conjunto de planos de taller `25007-ME-PI-0901-0006` a `-0016` | Once laminas timbradas para construccion, retiradas del Piping Layout al emitir la Rev D y nunca sometidas como entregable propio con codigo y revision. Sus dos hallazgos de contencion de presion siguen sin respuesta | Abierto, agravado por el retiro sin reemision |
| N25, N29, N30 | Dossier de fabricacion y pruebas | El item 65 sigue NOT DELIVERED. El indice llego a la Rev B; ningun registro lo ha seguido. Sostiene las filas 8.3 y 8.4 del ITP, de las que depende el 40 por ciento del pago | Abierto, vencido |
| N26, N30 | Informe de calculo estructural endosado `P22-CD-09-005-001` | Emitido en Rev 0 apto para construccion con solo iniciales internas. Sigue sin el endoso de un ingeniero registrado en Chile, comprometido por escrito tres veces | Abierto, vencido |

**Candidato a entrar en la tabla, y decision del usuario:** el **aviso escrito de la Clausula 37 y de la W del ITP** para los puntos de testigo que quedan por delante. El FAT del modulo abre el 7 de septiembre. Si el usuario quiere que viaje en el transmittal, desplaza a uno de los tres.

**Tambien abierto**, en una linea: 🔴 **el Ultrasonic Thickness Procedure `P22-BA-09-000-016` no volvio** —de los tres procedimientos que el TM N35 devolvio en Codigo 3, dos llegaron en Rev C y este no, y era el que mas habia cambiado de los tres—; los registros de penetrantes del 7 de agosto, examinados cinco dias antes de que su procedimiento se sometiera; el plano de puntos de medicion que exige la fila 7.8 del ITP; el formulario de registro de ensayo de presion como documento controlado; la presion de ensayo de cada linea de super duplex, a confirmar por escrito; la reemision de la Equipment List y de la Valve List; la **Instrument List Rev E** con `VT-09-001` rangeado de 0 a 12 mm/s rms, de la que depende ademas el Instrument Location Layout Rev D; la reconciliacion de seis TAG del HMI Display Screenshot Rev B; y el hito de los tres datasheets Fedco en Rev 0 antes del FAT.

**Entra a la lista con este transmittal:** la **reconciliacion de las cuatro entradas digitales y del mapa de reles de salida** entre el registro del FAT, la I/O List Rev 6 y el esquematico Rev B, que hoy dicen tres cosas distintas.

**Cierra en este transmittal**, y por eso sale de la lista: la presion de diseño en el punto de conexion de alimentacion de salmuera. Y queda **contestado el punto de la clase de brida del antiscalante del Piping Layout Rev D**, que el TM N36 dejo abierto: BW Water declara aqui que en el antiscalante no hay brida porque la terminacion es la valvula.

---

## 12. Que se retira y no se emite

- **El Articulo 9 de la clausula 4.0 de los dos procedimientos de ensayos no destructivos.** Ambos siguen citando `ASME Section V, Article 9 – 2025` donde corresponden el Articulo 6 y el Articulo 2. Pero la NOTE-01 del TM N32 reconoce por escrito que esa lista *"is inherited from the reference section of the NDE Plan, which ADASA will align at its next issue"*, y esa alineacion no se ha emitido. Reclamarlo por tercera vez sin haber hecho lo propio es refutable. **Corresponde que ADASA emita la alineacion de su NDE Plan**: compromiso interno.
- **La frase generica de apertura de la clausula 23.0 de radiografia.** Se pidio poner el criterio de B31.3 en lugar de la lista, y la lista salio. Con una sola entrada debajo ya no hay menu.
- **Las tres normas del FAT citadas como `Latest Edition`.** Es el mismo defecto que ADASA objeto en el procedimiento de presion, pero nunca se pidio sobre este documento.
- **La caratula del Tie-In Point Layout declara `Revision No.: A` y `Page: 1of 2`** sobre un documento que es Rev 0 y tiene tres paginas. Es observacion nueva sobre una emision que responde a comentarios previos, y es aseo documental, que por si solo no degrada.
- **Erratas de tipeo** del indice de radiografia y `ASME 31.3` sin la B. Nunca se pidieron.
- **La numeracion de carpetas de entregas.** Se documenta en la seccion de higiene y no se corrige.

## 12.1 Que no puede cruzar al documento emitido

- Ninguna referencia a Van Doorn, a numeraciones internas de ADASA ni a los ledgers.
- El signo de seccion no aparece en ninguna parte; las citas van como "Seccion N — Nombre".
- La cita a la Especificacion Tecnica va por codigo mas numero de seccion deletreado mas nombre.
- Al citar el punto de borrosidad geometrica de radiografia, la referencia correcta contra la Rev C es **la clausula 13.0, Geometric Unsharpness**: el rotulo `12.1` cambio de dueño con la renumeracion y hoy corresponde a calibracion.
