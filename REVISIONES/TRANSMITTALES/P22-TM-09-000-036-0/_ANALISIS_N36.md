---
titulo: Analisis interno — Transmittal N36 (P22-TM-09-000-036-0)
codigo: P22-TM-09-000-036-0
fecha: 2026-08-26  # redaccion y emision: enviado el 2026-08-26 a las 18:08
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Analisis interno — Transmittal N36

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Cuatro entregas sin responder: `25007-0082`, `25007-0083`, `25007-0084` y `25007-0085`. Nueve documentos.
Veredicto global: **2 — Approved as noted**, con **3 Codigo 1 y 5 Codigo 2** sobre los **ocho documentos que se disponen**. Ningun documento vuelve a revision. El noveno, el Project Schedule Rev B, se retiro del transmittal: su seguimiento se lleva por la reunion semanal de coordinacion y el transmittal lo declara en una linea sin asignarle codigo (decision del usuario, 26-Ago-2026).

**Ningun documento vuelve a revision, y el transmittal deja dos frentes en el registro.** El primero es el GA of SWRO System Skid, unico del lote emitido para construccion, donde de las tres referencias que constituian su Codigo 2 anterior solo una se corrigio: se dispone en **Codigo 1** porque los documentos referidos siguen siendo identificables y ninguna errata altera el contenido del plano, y el texto lo enuncia con dureza. El segundo es el **hito documental de los tres equipos Fedco**, comprados, fabricados y a dias de montarse, cuyas hojas de datos siguen circulando en Rev E para aprobacion: se exige cerrarlas en Rev 0 antes de que abra el FAT.

El cierre punto por punto de cada documento, y lo verificado que no se emite, viven en el `_LEDGER_COMENTARIOS.md` de su entrega. La disposicion se resuelve en las secciones 3 a 10.

---

## 1. Recepcion y plazos

| Submittal | Emitido | Emision para | Devolucion pedida por BW | Vencimiento real, Clausula 37.2 |
|---|---|---|---|---|
| `25007-0082` | vie 21-Ago-2026 | IFC | lun 24-Ago-2026 | **mar 1-Sep-2026** |
| `25007-0083` | vie 21-Ago-2026 | IFA | lun 24-Ago-2026 | **mar 1-Sep-2026** |
| `25007-0084` | lun 24-Ago-2026 | IFC el skid, IFA los otros dos | jue 27-Ago-2026 | **mie 2-Sep-2026** |
| `25007-0085` | mie 26-Ago-2026 | IFA | **sab 29-Ago-2026** | **vie 4-Sep-2026** |

**La columna de emision decide la disposicion.** Un documento sometido **para aprobacion** no ha llegado a la fecha en que vencen las condiciones que su Codigo 2 anterior difirio al Rev 0. Un documento sometido **para construccion** si.

**Hecho contractual.** Las cuatro submittals piden devolucion **tres dias corridos** despues de emitidas, contra los siete dias habiles que fija la Clausula 37.2 de las Bases Administrativas Especiales, y la del `25007-0085` cae en **sabado**. Es el cuarto lote consecutivo con fecha de devolucion por debajo del plazo contractual. Se declara en el transmittal como constancia, sin convertirlo en observacion de documento.

Los vencimientos se computan sobre la fecha de emision declarada en cada Submittal Form, que es el dato del propio documento. Las fechas de archivo no se usan: el repositorio de correo entrante lleva sin capturar desde el 06-Ago, y la del `25007-0082` es anterior en horas a la emision por las doce horas de diferencia entre Malasia y Chile.

---

## 2. Higiene de carpeta

- **`25007-0082`**: dos archivos. El Structural Design Criteria son once paginas, de las cuales **diez son imagen escaneada** (443 caracteres extraibles en total, concentrados en la portada). Se resolvio con reconocimiento optico mas render a 300 dpi; toda cifra citada se confirmo sobre el render.
- **`25007-0083`**: el Submittal Form aparece dos veces, en la raiz y en la subcarpeta, con **md5 identico**. No es hallazgo. El Piping Layout trae tres laminas con rotacion 270 y se verificaron por render. El modelo llega como `.nwd` de 9,58 MB mas el `.dwg` fuente de 168 MB.
- **`25007-0084`**: tres documentos en subcarpeta. El plano del estanque antiscalante trae la lamina con rotacion 270. El cronograma son catorce paginas de texto nativo.
- **`25007-0085`**: cuatro archivos en raiz, texto nativo integro.
- **La lista real de cada carpeta trae mas archivos de los que declara su Submittal Form**, y la diferencia son los **archivos nativos** que el formulario no enumera porque lista documentos y no ficheros: el `.dwg` del Piping Layout y el del modelo en la `25007-0083`, y los `.dwg` de los dos planos generales en la `25007-0084`. La `25007-0083` trae ademas la hoja de comentarios del modelo como archivo suelto. **Ningun documento declarado falta**, de modo que la diferencia es informacion de revision y no defecto de entrega.
- El modelo 3D se verifico volcando su base de propiedades por objeto: **7.486 objetos en la Rev A y 9.155 en la Rev B**. Todas las cifras de objetos que este analisis cita son de **objetos unicos**, no de filas del volcado.

---

## 3. UHPRO Structural Design Criteria Rev 0 — `P22-CD-09-005-003`

**Origen:** Rev B, **Codigo 1 — Approved** en el TM N25, subseccion 2.5, con la accion literal *"none on this criteria document — accepted; issue directly at IFC Rev 0, folding the editorial items at issue"*.

**Que se verifico.** El cuerpo tecnico es identico al aprobado: parametros sismicos, las tres tablas de combinaciones de carga, materiales, viento y el capitulo de izaje llegan sin un solo cambio, y nada desaparecio ni contradice la Rev B. Los unicos cambios son de identificacion y la fila nueva de la tabla de revisiones.

**Que no.** Dos de los tres items editoriales siguen abiertos: la fecha de portada (18-Ago) no concuerda con la del cuerpo (11-Ago), y la duplicacion de numero de tabla persiste, con la secuencia 1, 2, 3, 4, 5, 7, 6, 7. El tercero, las unidades de presion de viento, si quedo correcto. **El Rev 0 ademas perdio la hoja de comentarios consolidada que la Rev B si traia.**

### Disposicion

**Codigo 1 — Approved.**

El fundamento es el codigo anterior, no la naturaleza de los items. **La Rev B quedo en Codigo 1**, es decir ADASA declaro el documento correcto; sobre un Rev 0 que viene de Codigo 1 la unica pregunta es si contradice lo aprobado, y no lo contradice. Los tres items editoriales viajaban en una nota, con la accion declarada como "ninguna", y son housekeeping documental, que no degrada por si solo.

**Sin CC_ADASA.** Los dos items abiertos y la hoja de comentarios ausente se declaran en el texto de la subseccion, que es su unico vehiculo, para ordenar en la proxima emision natural.

**No se exige endoso profesional sobre este documento.** El compromiso de endoso recae sobre el informe de calculo sismico `P22-CD-09-005-001`, no sobre el documento de criterios. Se sigue en la Seccion 3.

---

## 4. Piping Layout Rev D — `P22-DWG-09-005-004`

**Origen:** Rev C, **Codigo 2** en el TM N30, subseccion 2.3, cuya accion se titula literal *"Action to issue at IFC Rev 0 — no new drawing revision required"* y fija tres condiciones. **La Rev D se somete para aprobacion**, no en Rev 0.

**Que cerro.** El conjunto de once planos de taller que la Rev C traia embebido en diecisiete paginas fue removido: el archivo baja de 22 paginas a 5.

**Que no.**

| Condicion | Estado |
|---|---|
| Tabla de tie-in con TAG de linea, diametro, tipo de conexion y elevacion referida a un datum declarado, cubriendo permeado y CIP | **Cierre parcial.** La tabla existe, con cinco filas, y no incluye **ninguna** de las **siete** lineas de CIP que rotula esa misma lamina. Las cinco cotas de elevacion **no declaran datum**: los tres bloques de notas del plano estan vacios |
| Clase de brida en las terminaciones de CIP y antiscalante | **No cerrado.** La fila de antiscalante trae guion en las dos columnas de brida; las de CIP no estan en la tabla |
| Declarar si el modulo lleva uno o dos tableros locales, con TAG por envolvente | **No cerrado.** La lamina rotula **dos** envolventes con la misma palabra `LCP`, ninguna con TAG, y ninguna nota lo declara |

La hoja de comentarios consolidada transcribe **una** de las tres condiciones. Las otras dos no aparecen en la columna del cliente, que es como se pierden.

### Disposicion

**Codigo 2 — Approved as noted.** Las tres condiciones vencen al emitir Rev 0 y la Rev D es una emision intermedia para aprobacion que BW Water no estaba obligado a hacer. Se reiteran las tres, con la constancia de que es la segunda vez y de que la hoja de comentarios solo recogio una. **Lleva CC_ADASA.**

**La condicion de aceptacion se declara:** ADASA acepta el plano sobre la base de que las tres son anotaciones y cuadros sobre la geometria existente, sin cambio de disposicion, y de que el datum es lo que permite replantear las conexiones en terreno.

---

## 5. 3D Model Rev B — `P22-DWG-09-005-007`

**Origen:** Rev A, **Codigo 2** en el TM N30, subseccion 2.5, con la misma formula *"no new model revision required"*. **La Rev B se somete para aprobacion.**

**Trae hoja de comentarios propia** que transcribe los dos comentarios de reconciliacion y responde con nueve items. **No transcribe el primer punto del TM N30**, el de identificacion del archivo, ni en la columna del cliente ni en la respuesta.

**Que cerro.** Los TAG malformados de valvula: los **siete** que llevaban signo de interrogacion al final (`VM-09-076`, `-094`, `-095`, `-101`, `-102`, `-107` y `-117`) estan limpios, contra el unico que el TM N30 nombro. `BH-009-002` paso a `BH-09-002`. `DPS-09-002` paso a `DPS-09-001`. `BOI-09-006` paso a `BOI-09-001-6`. Las lineas `09-042` (nueve objetos en DN80 a cero, trece en DN50), `09-044` (treinta y tres en DN65 a cero) y `09-026` (veintiseis objetos de servicio antiscalante a cero) cerraron.

**Que no.**

- **Identificacion.** El nombre de archivo ya es el codigo del documento, contra el `V14 Taltal.nwd` de la Rev A. Pero las propiedades de publicacion siguen declarando **Titulo `V16 TALTAL`** y **no hay indice de revision en ninguna propiedad**, aunque el Submittal Form declara Rev B. Es lo unico que la especificacion sostiene sobre un archivo de modelo, y sigue abierto.
- **Colision del correlativo `09-001`.** La respuesta esta en futuro: *"RD-PVC-DN15-09-001 **will be** renamed to RD-PVC-DN25-09-046"*. `RD-PVC-DN25-09-046` no existe en el modelo y `RD-PVC-DN15-09-001` paso de **123 a 133 objetos**, coexistiendo con los **90** de `DA-PVC-DN100-09-001`. La linea `RD-PVC-DN15-09-001` no figura en la Line List aprobada en Codigo 1, y el Piping Layout Rev D del mismo submittal la rotula igual en sus tres laminas.
- **Linea `09-015`, casi cerrada.** Quedan **tres objetos** en DN100 contra los diecinueve ya correctos en DN80. En la Rev A eran veintiuno y diecinueve.
- **Los soportes sin TAG.** La hoja declara *"fifty-seven objects tags corrected with the question marks removed"*. Lo corregido fueron los siete TAG de valvula; **los cincuenta y siete objetos con la propiedad TAG en signo de interrogacion son soportes de caneria, ninguno se toco y ahora son setenta y dos**. Ningun soporte del modelo lleva TAG, ni en la Rev A ni en la Rev B.

**Lo que no degrada al modelo.** BW Water comprometio por escrito reemitir la **Equipment List** para alinearla con el desglose de recipientes y la **Valve List** para incorporar `VM-09-131`, `-132`, `-133` y `VRP-09-001`. Las dos reemisiones son entregables sobre otros documentos: van a la Seccion 3.

### Disposicion

**Codigo 2 — Approved as noted.** Las condiciones vencen al emitir Rev 0 y la Rev B es emision intermedia. Lo que se reitera con peso son la identificacion del archivo y la colision del correlativo, que contradice una lista aprobada en Codigo 1 con la fabricacion de spools de caneria al setenta por ciento. **La declaracion de cierre de los cincuenta y siete objetos se corrige por escrito**, sin convertirla en el determinante del codigo: los soportes de caneria no figuran en ninguna lista aprobada, de modo que el punto vive del pedido del TM N30 que BW Water acepto, y no de un requisito de la especificacion.

**No admite anotacion.** Un archivo Navisworks no puede llevar el formato de anotacion de los planos, de modo que sus observaciones van **integras en el texto de su subseccion** y la Seccion 4 declara la excepcion de forma explicita.

---

## 6. Project Schedule Rev B — `P22-BA-09-000-001` — RETIRADO DEL TRANSMITTAL

**Decision del usuario, 26-Ago-2026:** el seguimiento del cronograma se lleva por la **reunion semanal de coordinacion** y no por el transmittal. El documento **no recibe codigo de respuesta**, sus dos observaciones salen del transmittal y su PDF anotado no se emite.

El transmittal lo declara en una linea del Resumen Ejecutivo, para que BW Water no quede esperando un codigo que no va a llegar por esa via. El paquete retirado, con la evidencia verificada, **sale de la carpeta del transmittal** y queda en `ENTREGAS_BWWATER/ENTREGA 84/_cronograma_fuera_de_transmittal/`, junto al documento que comenta; el cierre punto por punto y la tabla de hitos siguen en el ledger de la ENTREGA 84, que no se toca.

**Lo verificado, que se conserva:** ninguna de las dos observaciones del TM N20 cerro. Cero ocurrencias de `ASME`, `stamp`, `certif` y `waiver` en las catorce paginas, y cero de `hydro`, `hydrostatic`, `pressure test` y `leak`, con los recipientes ya fabricados y recibidos en Penang al cien por ciento. Si respeta la tercera clausula de esa accion: la linea base de recuperacion no se reabre.

**En el Master Register** se registra la entrega —Rev B, ENTREGA 84— y **se conservan el TM y el veredicto del N20**, porque este transmittal no le asigno codigo. Por lo mismo no entra al Revision History, donde cada fila es un ciclo de revision con veredicto.

---

## 7. GA of SWRO System Skid Rev 0 — `P22-DWG-09-005-008`

**Origen:** Rev B, **Codigo 2** en el TM N31, subseccion 2.4. Su accion fue una sola: corregir tres referencias documentales del bloque de notas. **Ese es el universo entero de esta revision, y esta vez el plazo si vencio: el Submittal Form declara la emision como IFC.**

| Referencia | Estado |
|---|---|
| Nota 6, Instrument List a Rev E | **Cierre parcial.** La Hoja 2 dice `REV.E`; la **Hoja 1 sigue diciendo `REV.D`** |
| Nota 7, Line List a `P22-LI-09-009-003` | **Cerrado** en las dos hojas |
| Nota 8, codigo valido en vez de `P22-ET-09-006-01` | **No cerrado.** Sin cambio en las dos hojas |

**La respuesta a la nota 8 se refuta a si misma.** BW Water contesta *"snapshot is showing the document number has already been submitted in the earlier stage of the project"* y adjunta una captura del formulario de remision. Esa captura escribe el codigo **con tres digitos**, `P22-ET-09-006-001`, y la fila siguiente de la misma captura es `P22-ET-09-006-002`. La evidencia que invocan confirma el punto.

**Peso practico:** la nota 8 es la que remite al **espesor nominal por linea**, en un documento emitido para construccion. Como esta escrita, el fabricante no puede localizar la especificacion que gobierna el espesor.

### Disposicion

**Codigo 1 — Approved.** El plano esta emitido para construccion y **no se retiene**: los dos documentos referidos siguen siendo identificables —`P22-ET-09-006-001` esta a un digito del codigo escrito y su titulo coincide; la nota 6 trae el codigo correcto en las dos hojas y solo el indice de revision desactualizado en una— y ninguna de las dos erratas cambia una cota, un material, un rating ni una cantidad del skid. Son correcciones de cita en un bloque de notas, que la regla del proyecto trata como housekeeping documental y que **nunca degrada por si solo**. Precedente: el TM N29 dispuso en Codigo 1 los dos primeros Rev 0 del proyecto con sus residuales declarados para ordenar en la proxima emision.

**Sin CC_ADASA.** El PDF anotado que se habia generado se retiro a `ENTREGAS_BWWATER/ENTREGA 84/_skid_fuera_de_anotacion/`, con la evidencia verificada.

**Bajar el codigo no baja el tono.** El transmittal enuncia el punto con dureza en su Resumen Ejecutivo y en la subseccion: de las tres referencias pedidas solo una se corrigio, la respuesta a la nota 8 queda refutada por el anexo que el propio proveedor adjunto, y ADASA deja constancia de que el plano se emitio para construccion citando un codigo de documento que no existe. El codigo correcto se escribe **literal** en el transmittal, de modo que queda en el registro aunque el plano no se reemita nunca.

> **Correccion de criterio, 26-Ago-2026.** La disposicion inicial fue Codigo 3, con reemision a Rev 1. El usuario la objeto con dos argumentos y los dos se sostienen: los puntos son **de forma** y no de contenido, y el documento **esta en Rev 0 emitido para construccion**, de modo que no se devuelve a revision por una errata de cita. Sobre un Rev 0 el Codigo 3 queda reservado a un defecto sustantivo que obligue a rehacer el documento. Detalle en la Seccion 13.

---

## 8. GA of Antiscalant Dosing Tank Rev C — `P22-DWG-09-005-015`

**Origen:** Rev B, **Codigo 3** en el TM N26, subseccion 2.8. Es el unico documento del lote que venia de Codigo 3.

**Que cerro.** La accion pedia tres cosas y llegaron las tres:

- **Cargas de reaccion sismica y patron de anclaje.** Nota 16: `SumFx = 6,73 kN`, `SumFy = 5,86 kN`, `SumFz = 4,81 kN`; nota 15, centro de gravedad a 560 mm del fondo; y un **Detalle 4 nuevo**, `BOLTING EMBEDMENT`, con perno `M12` con golilla, empotramiento minimo de 150 mm y carga por perno `Fx = 2,24 kN`, `Fy = 1,95 kN`, `Fz = 1,60 kN`. Las cargas por perno son aritmeticamente consistentes con las tres orejas del Detalle 3, cuyas posiciones angulares se leen del Detalle 2 a 90, 210 y 330 grados.
- **Volumen util efectivo**, nota 8: `0,27 m3`.
- **TAG del equipo** `TK-09-002`, en el cajetin.

**Los dos residuos.** Verificar que lo agregado es correcto forma parte de verificar el cierre:

- **En el detalle de anclaje que se pidio agregar.** El agujero rotula **`Ø14 [Ø1/2"]`**, dos valores que no son equivalentes: media pulgada son 12,7 mm. En la Rev B el mismo rotulo decia `Ø10 [Ø1/2"]`, de modo que **la cota metrica cambio en esta revision y la imperial no**. El perno declarado es M12, que en 14 mm tiene la holgura normal de montaje y en 12,7 mm queda en ajuste estrecho.
- **En la tabla de boquillas, dentro de la OBS-02.** La fila `LEVEL MARKING`, que el TM N26 declaro en blanco, se poblo solo en ubicacion; el **tamano y la elevacion siguen con guion**, de modo que el volumen util declarado no tiene cota que lo materialice.

**Lo que no degrada a este plano.** La nota 16 declara las cargas *"as per calculation report"* sin citar codigo ni revision, y ese informe sigue sin endoso de ingeniero profesional habilitado en Chile. Es dependencia sobre otro documento: va a la Seccion 3.

### Disposicion

**Codigo 2 — Approved as noted.** Lo sustantivo del Codigo 3 cerro. Quedan dos correcciones menores sobre el propio documento, incorporables al emitir Rev 0. **Lleva CC_ADASA.**

---

## 9. Los tres datasheets Fedco Rev E

Los tres venian de **Codigo 2 en el TM N11**, con exactamente una nota abierta cada uno. Ninguno trae hoja de comentarios.

### El hito documental, que es lo mas grave del lote

Los tres cubren equipos **comprados, fabricados y a dias de montarse**: la bomba de alta `BH-09-001` y los dos turbocargadores `SIP-09-001` y `SIP-09-002`. Fueron aprobados en Codigo 2 en Rev D en el TM N11, con una sola nota menor cada uno, y el equipo se compro y se fabrico sobre esa base. El cronograma del propio proveedor programa la instalacion de la bomba dentro del contenedor para el **3 al 5 de septiembre** y la apertura del FAT para el **7**.

Y siguen llegando **en Rev E, sometidos para aprobacion**. El registro documental va por detras del estado fisico del equipo.

**El transmittal lo exige con bloque propio en el Resumen Ejecutivo y bloque de accion con fecha en las tres subsecciones:** emitir los tres en **Rev 0 para construccion antes de que abra el FAT el 7 de septiembre de 2026**, y ADASA declara que no seguira recibiendo y devolviendo revisiones de aprobacion de hojas de datos de equipos en camino al montaje.

**Fuente del argumento: el registro propio de ADASA.** Se argumenta desde el Codigo 2 del TM N11 y desde la compra y fabricacion del equipo, no desde el cronograma, que se retiro de este transmittal. El dato de que **su propio programa declara este ciclo de revision y aprobacion cerrado al 100 % desde el 16 de abril de 2026** (tareas 177 a 183) **no se emite**: queda como municion para la reunion semanal, donde el cronograma si es materia.

**El codigo de los tres no cambia por esto.** El Codigo 1 del `-002` ya significa emitir directamente en Rev 0, y el Codigo 2 de los turbocargadores significa incorporar y emitir en Rev 0. Lo que cambia es que el bloque de accion exige el cierre **con fecha**.

### 9.1 Datasheet of RO HP Feed Pump Rev E — `P22-ET-09-009-002`

La NOTE-02 tenia dos clausulas: reconciliar el campo de fabricante del motor entre los dos bloques de datos, y **confirmar el fabricante real una vez completada la compra**. Las dos quedan satisfechas por el mismo hecho: **cero ocurrencias de `ABB`** en las diez paginas, los dos bloques declaran `Manufacturer: GE`, modelo `444 TSC`, y la lamina de contorno rotula `GE 444/5 TSC`. La Rev E es posterior a la emision de la orden de compra del equipo, de modo que la declaracion de un fabricante concreto es la confirmacion pedida.

La lamina de contorno registra ademas `A - Changed motor box location and add note for "Style H" to the inlet and outlet` y rotula las conexiones `PIEDMONT STYLE H`, coherente con la hoja de acople de 2000 psi que el TM N11 acepto.

**Disposicion: Codigo 1 — Approved. Sin CC_ADASA.**

> **Precaucion de fuente.** Existe una version antigua con prefijo distinto, `P22-ITEM-09-009-002-A`, en la ENTREGA 1, que declara clase de aislacion B y esta superada. Leerla produce un hallazgo falso. El punto de clase de aislacion del TM N28 es accion sobre la Control Philosophy, no sobre este datasheet.

### 9.2 y 9.3 Datasheets of Feed and Interstage Turbocharger Rev E — `-007` y `-008`

Las NOTE-03 y NOTE-04 pedian lo mismo: actualizar el rotulo de la lamina de contorno a `Style S` **para eliminar la discrepancia** con el `STYLE 77` que figuraba en las conexiones, porque Style 77 es otro producto con otra presion de trabajo.

**Se agrego `PIEDMONT STYLE S` y no se borro `STYLE 77`.** En los dos documentos, las cuatro llamadas quedaron con las dos designaciones juntas. La discrepancia que se pidio eliminar sigue en la lamina.

El acople aceptado es **Piedmont Pacific Style S/X a 1800 psi**, y asi lo declara el cuerpo de los dos datasheets en sus conexiones de proceso. `Style 77` si es designacion Victaulic, y ese es el punto: la lamina nombra dos productos de fabricantes distintos en la misma conexion.

**Disposicion: Codigo 2 — Approved as noted** en los dos. Es una correccion de rotulo sobre el propio documento, incorporable al emitir Rev 0. **Los dos llevan CC_ADASA.**

---

## 10. Resumen de disposicion

| # | Documento | Rev | Emision | Codigo previo | Que falta, en una linea | Codigo | CC_ADASA |
|---|---|---|---|---|---|---|---|
| 1 | UHPRO Structural Design Criteria `P22-CD-09-005-003` | 0 | IFC | 1 (N25) | nada; dos items de aseo a ordenar en la proxima emision | **1** | no |
| 2 | Piping Layout `P22-DWG-09-005-004` | D | IFA | 2 (N30) | datum de las elevaciones, lineas de CIP en la tabla, clase de brida y TAG de los dos tableros | **2** | si |
| 3 | 3D Model `P22-DWG-09-005-007` | B | IFA | 2 (N30) | identificacion en las propiedades, renombre de la linea `09-001`, tres objetos de la `09-015` y los TAG de los soportes | **2** | no admite |
| 4 | GA of SWRO System Skid `P22-DWG-09-005-008` | 0 | IFC | 2 (N31) | nota 6 en la Hoja 1 y nota 8 en las dos hojas, a ordenar en la proxima emision | **1** | no |
| 5 | GA of Antiscalant Dosing Tank `P22-DWG-09-005-015` | C | IFA | 3 (N26) | cota del agujero contra el perno M12 y elevacion de la marca de nivel | **2** | si |
| 7 | Datasheet of RO HP Feed Pump `P22-ET-09-009-002` | E | IFA | 2 (N11) | nada de contenido; **emitir en Rev 0 antes del FAT** | **1** | no |
| 8 | Datasheet of Feed Turbocharger `P22-ET-09-009-007` | E | IFA | 2 (N11) | borrar `STYLE 77` y **emitir en Rev 0 antes del FAT** | **2** | si |
| 9 | Datasheet of Interstage Turbocharger `P22-ET-09-009-008` | E | IFA | 2 (N11) | borrar `STYLE 77` y **emitir en Rev 0 antes del FAT** | **2** | si |

**Veredicto global: 2 — Approved as noted. 3 Codigo 1 y 5 Codigo 2 sobre ocho documentos. Ningun documento vuelve a revision.**
**Cuatro PDF anotados**, mas la excepcion declarada del modelo Navisworks. Los tres Codigo 1 no llevan, y el Project Schedule Rev B queda fuera del transmittal.

---

## 11. Seccion 3 — pendientes de transmittals previos

| Origen | Documento | Observacion | Estado |
|---|---|---|---|
| N30 | Conjunto de planos de taller `25007-ME-PI-0901-0006` a `-0016` | Once laminas timbradas para construccion. Removidas del Piping Layout al emitir Rev D y **nunca reemitidas** con codigo y revision propios. Sus dos hallazgos de contencion de presion siguen sin respuesta: conexiones de instrumentacion roscadas en acero austenitico sobre lineas de super duplex de 60 a 90 barG de diseno, y quiebre de especificacion sin declarar entre super duplex y PVC. La fabricacion de spools de caneria va al 70 por ciento | Abierto, agravado al retirarse el conjunto sin reemitirlo |
| N25, N29, N30 | Dossier de fabricacion y pruebas | El item 65 sigue sin entregar. El indice llego a Rev B y ningun registro lo siguio. Sostiene las filas 8.3 y 8.4 del plan de inspeccion, de las que depende el 40 por ciento del pago | Abierto, vencido |
| N26, N30 | Informe de calculo estructural endosado `P22-CD-09-005-001` | Gobierna las cargas de anclaje que el GA del estanque antiscalante Rev C acaba de declarar en su nota 16, y las fundaciones ya construidas en terreno. Sigue sin endoso de ingeniero profesional habilitado en Chile | Abierto, vencido, reiterado aqui |

**Also open, del ciclo del TM N35:** los tres procedimientos de ensayos no destructivos devueltos en Codigo 3, a la espera de su Rev C; los registros de liquidos penetrantes del 7 de agosto, ejecutados cinco dias antes de que su procedimiento fuera sometido; el plano de puntos de medicion que exige la fila 7.8 del plan de inspeccion; el Pressure Test Record Chart como formulario controlado; y la confirmacion escrita de la presion de ensayo de cada linea de super duplex.

**Also open, de ciclos anteriores:** la reemision de la Equipment List y de la Valve List que BW Water comprometio por escrito en la hoja de comentarios del modelo 3D; la Instrument List Rev E con `VT-09-001` rangeada en 0 a 12 mm/s rms; la reconciliacion de seis TAG del HMI Display Screenshot Rev B; y la presion de diseno del punto de conexion de alimentacion de salmuera.

**Residuos que no tienen otro vehiculo que el texto de su subseccion**, porque sus documentos van en Codigo 1 y no llevan PDF anotado: los dos items editoriales del UHPRO Structural Design Criteria y la hoja de comentarios que su Rev 0 perdio.

---

## 12. Que se retira y no se emite

El detalle con sus citas literales vive en el epigrafe de fuera de alcance de cada `_LEDGER_COMENTARIOS.md`. En sintesis se retiraron:

- **Housekeeping de cajetin y portada** en cinco documentos: estado del plano que dice para aprobacion mientras la tabla de revisiones dice para construccion, fechas de firma congeladas en la revision anterior, portada del GA del skid que sigue rotulada Rev B, conteo de paginas declarado que no coincide, filas historicas perdidas del cajetin.
- **Referencias no pedidas**: la nota 5 del GA del skid, que cita la Valve List en Rev D y no formaba parte del pedido de las tres referencias.
- **Observaciones nuevas sobre el modelo**: la valvula `VM-09-130`, las **diez valvulas nuevas que llegaron con el TAG `?-?-?`** y no existian en la Rev A, la ausencia de conjuntos de seleccion y de viewpoints, y la ruta personal del archivo de origen. Ninguna tiene requisito que la sostenga ni estaba en la instruccion escrita.
- **La cota `R74 [R3"]` del estanque antiscalante**: es identica en la Rev B y en la Rev C, de modo que no es parte de lo agregado y cae fuera de la regla de alcance. Solo se emite la cota del agujero, que si cambio en esta revision.
- **Defectos heredados de una revision aprobada**: los dos errores de composicion de la portada del documento de criterios venian en la Rev B que ADASA aprobo en Codigo 1.
- **El volumen total instalado de 0,34 metros cubicos** del estanque antiscalante: se pidio en el ciclo de la Rev A y el TM N26 no lo repitio en su accion sobre la Rev B.
- **El PDF anotado del GA of SWRO System Skid**, generado y retirado al bajar el documento de Codigo 3 a Codigo 1. Un Codigo 1 no lleva anotacion. El paquete y su evidencia quedan en `ENTREGAS_BWWATER/ENTREGA 84/_skid_fuera_de_anotacion/`.
- **El dato del cronograma sobre el ciclo de aprobacion de los datasheets Fedco**, cerrado al 100 % desde el 16-Abr-2026 segun su propio programa. Es el argumento mas dificil de refutar, pero citarlo reintroduce en el transmittal el documento que se retiro. Va a la reunion semanal.
- **Del cronograma**: la tarea 419 rotula `ADISA` en vez de ADASA, y el documento no declara fecha de corte ni version de linea base.

**La hoja de comentarios ausente si se emite, pero como clausula y no como observacion.** Cuatro de los ocho documentos dispuestos llegan sin ella: el UHPRO Structural Design Criteria y los tres datasheets Fedco. La traen el Piping Layout, el modelo 3D, el GA del skid y el GA del estanque antiscalante. El noveno documento, el cronograma, tampoco la trae, pero salio del transmittal. Se declara en el texto de las subsecciones que corresponde, con el peso que tiene en el documento de criterios, que la traia en la Rev B con nueve comentarios y la perdio al emitir Rev 0.

## 12.1 Que no puede cruzar al documento emitido

El transmittal va a BW Water. De este archivo y de los ledgers **no cruza nada de lo siguiente**: los correlativos del registro de compromisos de ADASA, la dependencia con la ingenieria civil propia, las herramientas y versiones con que ADASA verifico, la ruta personal del autor del modelo, y la Seccion 13 completa. A BW Water se le cita la obligacion, no como ADASA llego a ella.

---

## 13. Registro del criterio aplicado

**La regla de alcance.** Instruccion del usuario, reafirmada el 26-Ago-2026: *"para los documentos que ya estan en rev 0, solo debemos revisar que se levantaron los comentarios realizados, de lo contrario estariamos invalidando la definicion que dimos anteriormente de code 2 o 1"*. Aplicada a todo el lote, porque los nueve documentos responden a comentarios previos.

**El corolario que la verificacion adversarial obligo a incorporar, y que es el hallazgo de metodo de este ciclo.** La regla tiene una segunda mitad que no estaba escrita: **la condicion de un Codigo 2 vence cuando el documento se emite en Rev 0, no antes.** Un Codigo 2 dice literal *"Action to issue at IFC Rev 0 — no new revision required"*. Si el proveedor somete una revision intermedia **para aprobacion** y esa revision aun no incorpora las condiciones, escalar a Codigo 3 contradice la frase que ADASA misma escribio y ordena una revision que ADASA declaro innecesaria.

Por eso la **columna de emision del Submittal Form decide**: IFC significa que el plazo vencio y quedan Codigo 1 o Codigo 3; IFA significa que la condicion se reitera en Codigo 2, con constancia de la reincidencia.

La primera version de esta disposicion tenia cuatro Codigo 3 sobre ese error. Sobrevive uno, el unico documento del lote emitido para construccion.

**Como se resolvio cada caso limite.**

- **Verificar que lo agregado es correcto no es abrir un frente nuevo, pero solo alcanza a lo agregado.** En el estanque antiscalante se pidio el patron de pernos: la cota del agujero, que cambio en esta revision, esta dentro; el radio, identico desde la Rev B, esta fuera.
- **Un pendiente que vive en otro documento no degrada al revisado.** Las reemisiones de la Equipment List y de la Valve List, y el endoso del informe de calculo que respalda las cargas del estanque, van a la Seccion 3.
- **El housekeeping documental nunca degrada por si solo.** Aplicado a cinco documentos.
- **Un punto sin requisito que lo sostenga se emite como correccion de la declaracion, no como determinante.** Los TAG de los soportes de caneria del modelo viven del pedido del TM N30 que BW Water acepto, no de la especificacion. Se corrige por escrito la declaracion de cierre y no se apoya el codigo en ellos.
- **Sobre un Rev 0 no existe el Codigo 2.** Los dos Rev 0 del lote resolvieron a los extremos: el documento de criterios a Codigo 1 porque venia de Codigo 1 y su cuerpo llega intacto; el GA del skid a Codigo 3 porque venia de Codigo 2 y dos de las tres referencias que lo constituian siguen sin corregir.

**Errores propios que la verificacion adversarial corrigio antes de emitir.** Se registran porque el modo de falla es reutilizable:

1. **Conteo de objetos del modelo.** Las cifras se habian tomado del numero de **filas** del volcado de propiedades, donde cada objeto genera unas veinte. Decian 110 objetos en la linea `09-015` donde hay **tres**, y 5.033 en la `09-001` donde hay **133**. Al volcar una base de propiedades, contar siempre por indice de objeto unico.
2. **La declaracion de BW Water sobre los cincuenta y siete objetos no era enteramente falsa.** Corrigieron los siete TAG de valvula y atribuyeron mal el conteo. Escribir "no se corrigio ninguno" les daba una respuesta facil.
3. **Presiones de los turbocargadores.** Los 1.008 y 1.208 psi que el TM N11 rotulo como presion de entrada son en realidad la presion de descarga y la de entrada de salmuera. No se repiten.
4. **Los acoples aceptados son Piedmont Pacific, no Victaulic.** `Style 77` si es Victaulic, y ese es justamente el punto.

**La correccion de criterio sobre el GA of SWRO System Skid, y la regla que deja.**

La disposicion inicial fue **Codigo 3** con reemision a Rev 1. El usuario la objeto con dos argumentos, y los dos se sostienen contra la evidencia:

1. **Los dos puntos son de forma, no de contenido.** `P22-ET-09-006-01` esta a un digito de `P22-ET-09-006-001` y el titulo coincide; la nota 6 trae el codigo correcto en las dos hojas y solo el indice de revision desactualizado en una. Ninguno cambia una cota, un material, un rating ni una cantidad. La memoria del proyecto reserva el Codigo 2 para cuando falta *un dato o valor tecnico*, e interpreta el criterio como cambio **tecnico o sustantivo**, no como housekeeping administrativo.
2. **Esta en Rev 0 emitido para construccion: no se devuelve a revision por un defecto de forma.** Sobre un Rev 0 el Codigo 3 queda reservado a un defecto sustantivo que obligue a rehacer el documento. Retener un plano que ya gobierna fabricacion por una errata de cita cuesta un ciclo y no corrige nada fisico.

**Lo que la correccion NO cambia es el tono.** Instruccion del usuario: *si hay cosas que se comentaron y no se levantaron hay que indicarlo con fuerza en el transmittal*. Bajar el codigo no es bajar la exigencia, y callar el punto lo daria por aceptado. El texto emitido enuncia que de las tres referencias solo una se corrigio, que la respuesta a la nota 8 queda refutada por el anexo del propio proveedor, y escribe literal el codigo correcto.

**Decisiones del usuario registradas, 26-Ago-2026.**

1. **Alcance:** un solo transmittal con las cuatro entregas, emitido antes del vencimiento mas temprano.
2. **Calibracion:** la disposicion paso por tres estados. Primero cuatro Codigo 3; la verificacion adversarial mostro que tres recaian sobre revisiones sometidas para aprobacion y quedo uno; y el usuario objeto ese ultimo por ser de forma sobre un Rev 0 emitido para construccion. **Resultado: ningun Codigo 3 y veredicto global 2.**
3. **Project Schedule:** primero se decidio que entrara al transmittal con codigo de respuesta y que el fondo contractual fuera por correo separado. El 26-Ago el usuario lo **retiro del transmittal**: el seguimiento del cronograma se lleva por la reunion semanal de coordinacion. El transmittal lo declara sin codigo y el correo contractual queda en borrador, con su envio por decidir.
4. **Modelo 3D:** se revisa solo contra el cierre de los comentarios del TM N30, sin cruce masivo contra listados.
5. **Equipos Fedco:** el transmittal exige cerrar las tres hojas de datos en Rev 0 antes de que abra el FAT, con bloque propio en el Resumen Ejecutivo. Es el punto que el usuario califico de mas grave del lote.

---

## 14. Cierre del ciclo

**Enviado el miercoles 26-Ago-2026 a las 18:08 de Chile.** Un adjunto, `TRANSMITTAL N36 ADASA-BW_WATER.pdf` de nueve paginas; los cuatro `CC_ADASA` por el enlace de descarga, verificado caracter a caracter sobre el respaldo del enviado (`CORREOS/Agosto 2026/2026-08-26/envio transmittal 36.pdf`).

**Recorte ejecutivo antes de emitir**, a peticion del usuario: el transmittal bajo de 3.223 a 2.122 palabras de prosa, de once a nueve paginas, y el correo de 525 a 242 palabras de cuerpo. Se corto duplicacion entre el Resumen Ejecutivo y la Seccion 2, no contenido; los diez hechos que no podian perderse se verificaron uno por uno sobre el `.docx` emitido. El `.md` fuente se regenera desde las constantes de `crear_transmittal.py`, de modo que no pueden derivar.

**`anti-ia` modo revisar, con la familia del modelo autor cargada.** Barrido de fingerprints limpio en los dos documentos. El chequeo de voz, corrido aparte y contra los transmittals en ingles ya enviados, encontro una sola desviacion: parentesis a 1,9 por mil contra la banda de 3,3 a 4,0; corregida a 3,8 reponiendo codigos ya verificados.

**Registros cerrados.** Master Register aplicado con `update_register_n36.py`: tally 62 / 21 / 6 / 0, 113 items con 89 entregados, 36 transmittals y 85 entregas, coincidiendo con lo esperado; gate `openpyxl_lint.py` en exit 0. Compromiso `PRG-37` abierto con su evidencia de emision, vence el 7-Sep. README, Bitacora, Indice de Transmittales y memorias al dia.

**Unico pendiente:** decidir si sale el correo contractual del cronograma, que sigue en borrador porque el tema paso a la reunion semanal de coordinacion.
