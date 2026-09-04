---
titulo: Ledger de cierre de comentarios — ENTREGA 86 (submittal 25007-0086)
fecha: 2026-08-28
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 86

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0086`, emitido el jueves **27-Ago-2026**, devolucion pedida el **domingo 30-Ago-2026**, vencimiento real de la Clausula 37.2 el **lunes 7-Sep-2026**. Llego como un unico archivo comprimido que se descomprimio conservando el original; la lista real coincide con la declarada en el formulario.

| # | Documento | Codigo | Rev | Emision | Origen |
|---|---|---|---|---|---|
| 1 | Liquid Penetrant Examination Procedure | `P22-BA-09-000-014` | C | IFA | Codigo 3, TM N35 |
| 2 | Radiography Examination Procedure | `P22-BA-09-000-015` | C | IFA | Codigo 3, TM N35 |
| 3 | I/O List | `P22-LI-09-008-001` | 6 | **IFC** | Codigo 2, TM N28 |
| 4 | Instrument Location Layout | `P22-DWG-09-008-001` | D | IFA | Codigo 3, TM N23 |
| 5 | PLC/LCP Schematic Diagram | `P22-CD-09-008-002` | B | IFA | Codigo 2, TM N20 |

🔴 **Falta el tercero del trio de ensayos no destructivos.** El TM N35 devolvio en Codigo 3 los tres procedimientos —penetrantes, radiografia y **espesor por ultrasonido `P22-BA-09-000-016`**— por el mismo punto. Volvieron dos. **La Rev C del de ultrasonido no se sometio**, y es el que mas habia cambiado de los tres en su Rev B, con nueve cambios de contenido. Va a la seccion de pendientes.

---

## 1. I/O List Rev 6 — `P22-LI-09-008-001`

**Origen:** Rev 5, **Codigo 2** en el TM N28, con **una sola** accion. **Emitida para construccion (IFC).**

**Trae hoja de comentarios consolidada**, que transcribe el pedido de ADASA integro.

| Punto | Pedido, literal en la columna del cliente | Respuesta de BW Water | Verificado en la Rev 6 | Estado |
|---|---|---|---|---|
| OBS-01 del TM N28 | *"add the CIP tank heater start/stop output (and run/fault feedback if applicable) so the Alarm and Interlock List Stop-heater interlock can be executed, or confirm in writing that the CIP heater is controlled outside the module PLC"* | *"HAS BEEN REVISED IN I/O LIST - P22-LI-09-008-001 REV6. Heater Start and Running feedback has been added."* | **Verificado sobre la lista, no sobre la declaracion.** Fila 108: `REL-09-001`, `HS001`, `CIP HEATER ON/OFF COMMAND`, de `PLC` a `HCP`, tipo `DO`, contacto seco normalmente abierto 24 VDC, revision `6`. Fila 109: `REL-09-001`, `XB002`, `CIP HEATER RUNNING`, de `HCP` a `PLC`, tipo `DI`, mismo tipo de contacto, revision `6` | **Cerrado** |

**Sintesis.** La unica condicion del Codigo 2 quedo cerrada y verificada contra el contenido. El documento se emite para construccion, de modo que la condicion vencio y quedan solo Codigo 1 o Codigo 3; no hay defecto sustantivo. **Codigo 1.**

---

## 2. PLC/LCP Schematic Diagram Rev B — `P22-CD-09-008-002`

**Origen:** Rev A, **Codigo 2** en el TM N20, subseccion 2.7, con una sola NOTE-01. **Emitido para aprobacion (IFA).**

**Trae hoja de comentarios consolidada**, fechada el **24-Ago-2026**, con un solo item.

| Punto | Pedido, literal en la columna del cliente | Respuesta de BW Water | Verificado en la Rev B | Estado |
|---|---|---|---|---|
| NOTE-01 del TM N20 | *"Acceptance is conditional on Plant Control Philosophy Rev D: any signal divergence introduced by Rev D propagates to the panel wiring and terminal assignments. Spare I/O capacity should absorb signal-level changes; confirm the I/O assignment after Rev D issue"* | *"Noted. +as been added and revised in I/O List RevB."* | La respuesta remite a una *"I/O List Rev B"* que **no existe**: esa lista lleva revisiones numericas y va en la **Rev 6**. La reconciliacion esta casi hecha —la lamina 39 cablea la salida del calentador en el modulo `-A4`, salida 7, con el rele `KA8`, y las entradas 1 a 4 de la lamina 35 figuran como reserva—, pero 🔴 **la entrada `CIP HEATER RUNNING`, que es el item 109 de la lista, no tiene borne en ninguna de las cuatro laminas de entradas digitales**: 19 entradas asignadas contra 20 activas en la lista, con 13 bornes libres | **Cierre parcial** |

🔴 **El terminal de operacion sigue siendo el `-D8S`.** Verificado por render de la **lamina 28**, tabla `PLC PANEL BILL OF MATERIAL (BOM) LIST`, fila 11: `HMI1 | 1 | Touch Screen | 2711P-T10C21D8S | Allen-Bradley`. Es la unica aparicion del numero de catalogo completo en las 71 laminas. El TM N30 se envio el 05-Ago y esta Rev B esta fechada el 24-Ago. **La hoja de comentarios no trae ninguna fila para este punto.** En el **TM N30** ADASA **declaro vinculante** el `2711P-T10C22D9P` —dos puertos Ethernet RJ45 y 1 GB, filas 15 y 18 del datasheet aprobado— frente a ese mismo `-D8S`, de un puerto y 512 MB segun el catalogo Rockwell 2711P-TD008, y nombro a este esquematico entre los cuatro documentos que debian corregirse. **No se corrigio.**

**Y ahora hay evidencia de que el tablero se armo con el `-D8S`**: el registro del FAT del tablero, en la ENTREGA 88, visa la fila *"Verify HMI (HMI1: 2711P-T10C21D8S, Allen-Bradley) is installed on inner door"*. El punto deja de ser documental.

---

## 3. Liquid Penetrant Examination Procedure Rev C — `P22-BA-09-000-014`

**Origen:** Rev B, **Codigo 3** en el TM N35, que a su vez venia del TM N32. **Emitido para aprobacion (IFA).** Portada `Date: 27/08/2026`, Revision C, preparado MF, revisado y chequeado MAZ, aprobado LHM.

**Trae hoja de comentarios consolidada**, pagina 22 de 22, fechada el 27/8/2026. **Una sola fila**: pega el bloque de accion completo de la subseccion 2.3 del TM N35 y responde `Revised as per comment`, sin decir que se cambio.

| Punto | Pedido, literal | Verificado en la Rev C | Estado |
|---|---|---|---|
| **OBS-01** — criterio de aceptacion unico en la clausula 13.0 | *"state ASME B31.3 para. 341.3.2 and Table 341.3.2 as the single criterion, and delete the reference to Appendix 6"* | Pagina 16 de 22, clausula 13.0. El bloque del Apendice 6 y sus tres umbrales **fueron eliminados**. Queda una sola entrada, `a. ASME B31.3 - Process Piping (State ASME B31.3 para. 341.3.2)`, con los umbrales de B31.3 debajo | **Cerrado** |
| **OBS-02** — el mismo criterio en el formulario de informe | *"state ASME B31.3 para. 341.3.2 on this form, matching clause 13.0"* | Pagina 19 de 22. Donde decia `Acceptance Criteria: ASME VIII DIV.1 Appendix 8` ahora dice `Acceptance Criteria: ASME B31.3 para. 341.3.2`, y la casilla `☒ ASME B31.3` quedo marcada; en la Rev B las cuatro estaban en blanco | **Cerrado** |
| **NOTE-01 (a)** — formulario en blanco | *"issue the form blank, with the project and contract identification of this module"* | 🔴 Pagina 19 de 22, **sin un solo cambio respecto de la Rev B**: `Report No: XESSB-ITS-PT230601(Cth)`, `Job No: (Cth: ITS-PT230601)`, los tres lotes MR CHEMIE (`2408019`, `2405026`, `2404074`) y la columna de observaciones pre-escrita con `No Relevant Indication Was Found During PT Examination Time` | **No cerrado** |
| **NOTE-01 (b)** — indice de revision del procedimiento adjunto | *"issue the procedure under a single revision index"* | Los encabezados de las quince paginas dicen ahora `WI-OD-PT02, Rev.C` de forma uniforme; en la Rev B alternaban `Rev.00` y `Rev.01`. Pero el campo `Procedure:` **dentro del formulario**, pagina 19, sigue leyendo `WI-OD-PT02, Rev.00`, y es la unica aparicion de `Rev.00` que queda en el archivo | **Cierre parcial** |
| **NOTE-01 (c)** — clausula de proposito y numero de documento | *"state the purpose and the document number of this procedure, cite Article 6, and align the editions"* | La frase de proposito **cerro**: la clausula 1.0 dice ahora *"the procedure for liquid penetrant examination"*, donde decia *"positive material Identification"*. Las ediciones **cerraron**: la pagina 9 dice `ASME B31.3 2024 Edition`, era 2021, y se borraron VIII Div.1, B31.8 y B31.1 del listado del adjunto. El numero de documento **no**: la pagina 2 sigue en `DOC NO: PMI PROV-PROC-PT-001` | **Cierre parcial** |

🔴 **La hoja de comentarios declara un cierre que no ocurrio.** Responde `Revised as per comment` a un bloque que incluye textualmente *"the report form data of another contract"*, y ese formulario esta intacto. Es la **segunda vez** que ese item se levanta, y aplica la regla de verificacion de la hoja de respuesta a comentarios de la Seccion 6.5 del CLAUDE.md.

**Sintesis.** El determinante del Codigo 3 cerro: la clausula 13.0 ofrece hoy un solo criterio y el formulario que firma el examinador declara ese mismo criterio con su numero de parrafo, de modo que el examinador ya no elige. Lo que queda es el formulario, que es la hoja que entra al dossier de calidad, y el numero de documento. **El documento mismo debe cambiar antes de emitirse en Rev 0.**

---

## 4. Radiography Examination Procedure Rev C — `P22-BA-09-000-015`

**Origen:** Rev B, **Codigo 3** en el TM N35. **Emitido para aprobacion (IFA).** Portada `Date: 27/08/2026`, Revision C.

**Trae hoja de comentarios consolidada**, paginas 29 y 30 de 30, fechada el 27/8/2026, con **dos filas** —OBS-01 y OBS-02 literales, ambas respondidas `Revised as per comment`—. **La NOTE-01 no aparece en la hoja**, de modo que los tres items de aseo no fueron respondidos como fila.

| Punto | Pedido, literal | Verificado en la Rev C | Estado |
|---|---|---|---|
| **OBS-01** — criterio unico en lugar de la lista de cinco codigos | *"state ASME B31.3 para. 341.3.2 and Table 341.3.2 as the acceptance criteria of this project, in place of the list"* | Pagina 21 de 30, clausula 23.0: la lista bajo de cinco codigos a uno. Salieron VIII Div.1 UW-51, VIII Div.1 UW-52, VIII Div.2 para. 7.5.3.2 y B31.8. La lista de referencias de la clausula 2.0 bajo de cinco a dos, Seccion V y B31.3. La Tabla 341.3.2-1 de B31.3-2024 sigue completa en la pagina 28, confirmado por render | **Cerrado** |
| **OBS-02** — reemplazar los 1,8 mm por el limite de T-274 | *"state the T-274 limit applicable to the wall radiographed on this module"*, esto es 0,020 in. | El texto de los 1,8 mm y la dispensa de items con sello `U` y `PP` **desaparecieron por completo del cuerpo**: `1.8 mm` y `PW-51` aparecen una vez cada uno en las treinta paginas, y las dos estan dentro de la hoja de comentarios citando el propio texto de ADASA. En su lugar, pagina 12, clausula nueva `13.0 GEOMETRIC UNSHARPNESS` con `13.1 ... Table T-274 Article 2 specifies a maximum geometric unsharpness (Ug) of 0.020 in.`, y la pagina 13 reproduce integro el texto de T-274 con la definicion de D, d, F y Ug | **Cerrado** |
| **NOTE-01 (a)** — declarar material y rango de espesor del proyecto | *"declare the material and the thickness range of this project"* | 🔴 Pagina 9 de 30, clausula 1.0 SCOPE, **sin un solo cambio**: *"Radiography Testing of Stainless, Carbon, low alloy and high alloy steel welds up to 3-inch thickness using Gamma ray (Ir 192)"*. No nombra `ASTM A790 UNS S32750` ni el rango de 6,02 a 8,56 mm | **No cerrado** |
| **NOTE-01 (b)** — renumerar las sub-clausulas | *"renumber so that each clause can be cited without ambiguity"* | Renumeracion real y practicamente completa: los encabezados corren de 1.0 a 25.0 sin salto y cada sub-clausula coincide con el suyo; `PACKING OF FILMS`, que aparecia como 15.0 despues de la 24.0, es ahora 25.0 y esta en su lugar; el indice se actualizo. Quedan dos referencias cruzadas internas sin corregir, la 11.6 remite a `para 15.3` y la 19.4 a `17.3` | **Cierre parcial** |
| **NOTE-01 (c)** — clausula de proposito y numero de documento | *"state the purpose and the document number of this procedure, and cite Article 2"* | La frase de proposito **cerro**: la clausula 1.0 dice ahora *"the procedure for radiographic examination"*. El numero de documento **no**: la pagina 2 sigue en `DOC NO: PMI PROV-PROC-RT-001` | **Cierre parcial** |

**Sintesis.** El determinante cerro en sus dos mitades. La lista de cinco codigos desaparecio y queda un unico criterio nombrado por su numero de parrafo; el limite de borrosidad geometrica de 1,8 mm fue reemplazado por los 0,020 in. de T-274, que es exactamente lo que el TM N35 exigio. Lo que queda es el alcance, que sigue siendo generico y no nombra el material ni el espesor que efectivamente se radiografia en este modulo, y el numero de documento. **El documento mismo debe cambiar antes de emitirse en Rev 0.**

> **Aviso de citacion para el proximo transmittal.** El rotulo `12.1` cambio de dueño con la renumeracion: en la Rev C la 12.1 es *"The maximum source size or focal spot size shall not exceed..."*, bajo `12.0 CALIBRATION`. Si el punto de borrosidad se vuelve a citar, la referencia correcta es **la clausula 13.0, Geometric Unsharpness**.

---

## 5. Instrument Location Layout Rev D — `P22-DWG-09-008-001`

**Origen:** Rev C, **Codigo 3** en el TM N23, subseccion 2.6, con cuatro observaciones. **Emitido para aprobacion (IFA).** Es uno de los tres planos cuya reemision el TM N31 reclamo contra el reporte de estado del proveedor, con fecha comprometida vencida el **2-Ago-2026**.

**Trae hoja de comentarios consolidada**, pagina 4 de 4, fechada el 24/8/2026, con las cuatro observaciones del TM N23 transcritas literales.

| Punto | Pedido, literal en la columna del cliente | Respuesta de BW Water | Verificado en la Rev D | Estado |
|---|---|---|---|---|
| **OBS-01** | *"Re-issued on 16-Jun-2026 with content changes (items 8, 9, 31 and 32 and the CIP relocation) but the revision letter stays C with no new revision-history row, so two drawings share the identifier Rev C"* | *"This revision is based on Instrument list RevE instead of Instrument Location revision D."* — no contesta el punto | La emision avanzo a **Rev D** y la ambiguedad ya no afecta a la revision vigente. El bloque `REVISIONS` de las dos laminas **si tiene filas** —cuatro, D/C/B/A, verificadas por render a 288 dpi—, pero **las cuatro repiten la misma descripcion, `ISSUED FOR APPROVAL`**, de modo que ninguna dice que cambio. 🔴 **Y la fila historica de la Rev C fue reescrita**: en la Rev C decia `APR.17.26` y en la Rev D dice `JUN.16.26`. En vez de diferenciar las dos emisiones de junio, cuadraron la fila con la caratula. **Las dos Rev C siguen sin quedar distinguibles**, que era exactamente el punto | **No cerrado** |
| **OBS-02** | *"The geometry is aligned to the superseded Equipment Layout Rev B, open at Code 3 (RO Cartridge Filter still horizontal); BW Water concedes it cannot be issued for construction until the upstream layouts are approved"* | *"Noted. Instrument Location RevD has been updated based on approved P22-DWG-09-005-003_Equipment Layout_Rev.D."* | El Equipment Layout Rev D **cerro en Codigo 1 en el TM N33**, de modo que la dependencia que sostenia el Codigo 3 se levanto | **Cerrado** |
| **OBS-03** | *"The front title-block code reads P22-DWG-09-008-01 (two-digit correlative) versus the three-digit P22-DWG-09-008-001 in the file name and the sheet cajetin"* | *"Has been revised and aligned in P22-DWG-09-008-001 RevD"* | Verificado por render: los cajetines leen `P22-DWG-09-008-001-P1` y `-P2`, con el correlativo de tres digitos, y `REV.: D`. **Dato de contraste:** en la Rev C el cajetin de lamina **ya venia correcto** con tres digitos; el error de dos vivia solo en la caratula, que es lo que decia la OBS-03 | **Cerrado** |
| **OBS-04** | *"Rev C carries two issue dates: the front header dates it 16/6/2026 and the revision block dates it in April"* | *"Has been revised and aligned in P22-DWG-09-008-001 RevD"* | El encabezado de la caratula dice 24/8/2026 y las tres firmas del cajetin, `AUG.24.26`. Coinciden | **Cerrado** |

**Dato del cajetin, verificado por render:** `DRAWING STATUS: ISSUED FOR APPROVAL`, `DISCIPLINE: ELECTRICAL`, `SYSTEM CODE: 000`, `PROJECT NO.: 25007`, `SCALE: 1:30`, `DWG. SIZE.: A1`, `SHEET: 1`.

**Sintesis.** El determinante del Codigo 3 —la dependencia con un plano superado y abierto en Codigo 3— cerro, y con el los defectos de codigo y de fecha. Queda el registro de revisiones: ninguna fila describe su cambio y la fila historica de la Rev C se reescribio en vez de diferenciarse. Es un cambio al propio plano.

🔴 **Y la declaracion de cierre de la OBS-02 no esta en el plano.** La cadena `005-003` aparece **una sola vez en todo el archivo**, en la columna de respuesta de la hoja de comentarios. El cuadro `NOTES` de las dos laminas esta **vacio**, no hay lista de documentos de referencia y el campo `ORIGINATOR DRAWING NO.` lee guion. El plano no declara contra que revision del Equipment Layout esta dibujado: lo declara solo la hoja de respuesta.

**Dependencia cruzada que no degrada:** la respuesta al OBS-01 declara que la Rev D se basa en la **Instrument List Rev E**, que es la lista cuya reemision ADASA exige con `VT-09-001` rangeado de 0 a 12 mm/s rms. Va a la seccion de pendientes.

---

## Municion que NO se emite

- **La frase generica de apertura de la clausula 23.0 de radiografia.** ADASA pidio poner el criterio de B31.3 **en lugar de la lista**, y la lista salio. Con una sola entrada debajo ya no hay menu, y la especificacion del contrato a la que remite —la Especificacion Tecnica Seccion 8 mas el NDE Plan Rev C— apunta al mismo B31.3 para. 341.3.2. Seguir exigiendo que se borre la frase es exigir mas de lo que se pidio.
- 🔴 **El Articulo 9 de la clausula 4.0 de ambos procedimientos NO se reclama.** Los dos siguen citando `ASME Section V, Article 9 – 2025` donde corresponden el Articulo 6 y el Articulo 2. Pero el propio texto de la NOTE-01 del TM N32 reconoce que *"that list is inherited from the reference section of the NDE Plan, which ADASA will align at its next issue"*: la cita viene de la lista de referencias del **NDE Plan de ADASA**, y esa alineacion prometida no se ha emitido. Reclamarlo por tercera vez sin haber hecho lo propio es refutable. **Lo que corresponde es que ADASA emita la alineacion de su NDE Plan**, y eso es compromiso interno.
- **La errata `ASME 31.3` sin la B**, en la clausula 23.0 y en la lista de referencias de radiografia. Observacion nueva, fuera del universo del TM N35 y del TM N32.
- **Las dos referencias cruzadas internas de radiografia** que quedaron desfasadas tras la renumeracion (11.6 a `para 15.3`, 19.4 a `17.3`). Se mencionan dentro del punto de renumeracion, no como observacion propia.
- **Las erratas de tipeo del indice de radiografia** (`EXAMUNATION`, `TECNIQUE`, `EVALUTION`) y el `Doucment Description` del encabezado de las hojas de comentarios. Nunca se pidieron.
- **La columna `ECN` vacia del bloque de revisiones.** Esta vacia en las cuatro filas de este plano y tambien en las cuatro del Equipment Layout Rev D, de modo que apunta a que BW Water no usa numeracion de aviso de cambio en este proyecto y no a un incumplimiento. No se exige.
- Todo lo anterior queda en traza por si reaparece en el dossier de calidad.
