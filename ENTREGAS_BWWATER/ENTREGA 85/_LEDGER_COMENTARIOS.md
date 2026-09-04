---
titulo: Ledger de cierre de comentarios — ENTREGA 85 (submittal 25007-0085)
fecha: 2026-08-26
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 85

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0085`, "Engineering Datasheets", emitido el miercoles 26-Ago-2026, **devolucion pedida para el sabado 29-Ago-2026** (dia no habil), plazo real de la Clausula 37.2 el viernes 4-Sep-2026. Tres datasheets, los tres de equipos Fedco, los tres en Rev E y los tres provenientes de **Codigo 2 en el TM N11**, que dejo exactamente una nota abierta por documento.

Ninguno de los tres trae hoja de comentarios consolidada.

---

## 1. Datasheet of RO HP Feed Pump Rev E — `P22-ET-09-009-002`

Diez paginas. Unico punto abierto: la **NOTE-02 del TM N11**.

| Punto | Pedido, literal | Verificado en la Rev E | Estado |
|---|---|---|---|
| NOTE-02, fabricante del motor | "The HP Feed Pump Component Datasheet identifies the motor manufacturer as GE in the equipment data block, while the FEDCO pump data section lists ABB or equivalent. These two fields describe the same motor. BW Water must reconcile the motor manufacturer field across both data blocks in Datasheet Rev E and confirm the actual manufacturer once procurement is complete." | **Cero ocurrencias de `ABB`** en las diez paginas. El bloque de datos del motor declara `Manufacturer: GE`, `Model: 444 TSC`, `Type: Totally enclosed fan-cooled (TEFC)`; el plano de contorno rotula `GE 444/5 TSC`. Los dos bloques dicen lo mismo y nombran un fabricante concreto | **Cerrado** |

Dato colateral verificado: el plano de contorno del equipo registra en su tabla de revisiones `A - Changed motor box location and add note for "Style H" to the inlet and outlet, 7/8/2026`, y rotula las conexiones `PIEDMONT STYLE H`, coherente con la hoja de acople de 2000 psi que la Rev D adjunto y que el TM N11 acepto. **Sin resto abierto.**

### Precaucion registrada

Existe una version antigua de este datasheet con prefijo distinto, `P22-ITEM-09-009-002-A`, en la ENTREGA 1, que declara clase de aislacion B y esta superada. **El documento vigente es `P22-ET-09-009-002`.** Leer el otro produce un hallazgo falso justo en el punto de clase de aislacion. El punto de clase de aislacion del TM N28 es accion sobre la **Control Philosophy**, no sobre este datasheet.

---

## 2. Datasheet of Feed Turbocharger Rev E — `P22-ET-09-009-007`

Nueve paginas. Unico punto abierto: la **NOTE-03 del TM N11**.

| Punto | Pedido, literal | Verificado en la Rev E | Estado |
|---|---|---|---|
| NOTE-03, etiqueta del acople | "The HPB-60 outline drawing references CUT GROOVE STYLE 77 at the inlet and outlet connections. The attached coupling datasheet documents Style S/X at 1800 psi, which is the accepted rating. Style 77 is a different Victaulic product with a different pressure rating. **The outline drawing label must be updated to Style S (or the appropriate Style S/X designation) in the next datasheet revision to eliminate the discrepancy and prevent field installation errors.**" | La lamina de contorno agrego `PIEDMONT STYLE S` **y conservo `STYLE 77`**. Las cuatro llamadas quedaron con las dos designaciones juntas: `FEED OUTLET / PIEDMONT STYLE S / 2" CUT GROOVE / STYLE 77`, y lo mismo en entrada de alimentacion y entrada y salida de salmuera. Verificado por render: `render/007_p06_outline.png`. La discrepancia que se pidio eliminar sigue en la lamina: cada conexion nombra dos modelos de acople con presiones de trabajo distintas, sobre un equipo cuyas conexiones de proceso el propio cuerpo del datasheet especifica en `Coupling 1800 psi`, que es el rating del Style S | **Cierre parcial** |

---

## 3. Datasheet of Interstage Turbocharger Rev E — `P22-ET-09-009-008`

Nueve paginas. Unico punto abierto: la **NOTE-04 del TM N11**, identica a la anterior.

| Punto | Pedido, literal | Verificado en la Rev E | Estado |
|---|---|---|---|
| NOTE-04, etiqueta del acople | "Identical condition to NOTE-03 for SIP-09-001: the HPB-60 outline drawing references CUT GROOVE STYLE 77 at process connections while the accepted coupling is Style S/X at 1800 psi. BW Water must update the outline drawing label to Style S in the next revision to prevent field installation errors." | Mismo comportamiento exacto que el `-007`: se agrego `PIEDMONT STYLE S` en las cuatro llamadas y se conservo `STYLE 77` en las cuatro. El cuerpo de este datasheet especifica igualmente sus conexiones de proceso en `Coupling 1800 psi` | **Cierre parcial** |

---

## Sintesis para la disposicion

- **`-002` Rev E:** su unico punto abierto cerro. Disposicion natural **Codigo 1**, sin PDF anotado.
- **`-007` y `-008` Rev E:** el punto abierto cerro a medias. Se agrego la designacion correcta pero no se borro la equivocada, de modo que la lamina sigue nombrando dos acoples distintos en la misma conexion. Es una correccion de rotulo sobre el propio documento, incorporable al emitir Rev 0 sin nueva revision intermedia: disposicion natural **Codigo 2**, con PDF anotado.

## El hito documental, y es lo mas grave del lote

Los tres documentos de esta entrega cubren equipos **comprados, fabricados y a dias de montarse**: la bomba de alta `BH-09-001` y los dos turbocargadores `SIP-09-001` y `SIP-09-002`, los tres de Fedco. Fueron aprobados en Codigo 2 en Rev D en el TM N11, con una sola nota menor cada uno, y el equipo se compro y se fabrico sobre esa base.

El cronograma que BW Water emitio en la entrega 84 programa la **instalacion de la bomba dentro del contenedor para el 3 al 5 de septiembre** y la **apertura del FAT para el 7**. Y las tres hojas de datos siguen llegando **en Rev E, sometidas para aprobacion**: el registro documental va por detras del estado fisico del equipo.

**El transmittal lo exige con bloque propio en el Resumen Ejecutivo y bloque de accion con fecha en las tres subsecciones:** emitir los tres en **Rev 0 para construccion antes de que abra el FAT el 7 de septiembre de 2026**, con la declaracion de que ADASA no seguira recibiendo y devolviendo revisiones de aprobacion de hojas de datos de equipos en camino al montaje.

**El codigo de los tres no cambia por esto.** El Codigo 1 del `-002` ya significa emitir directamente en Rev 0; el Codigo 2 de los turbocargadores, incorporar y emitir en Rev 0. Lo que cambia es que el bloque de accion exige el cierre con fecha.

### Municion que NO se emite

**Su propio cronograma declara el ciclo de revision y aprobacion de estas hojas de datos cerrado al 100 % desde el 16 de abril de 2026**, en las tareas 177 a 183 (*Review & Approval* y *Datasheet of Feed Turbocharger*). Cuatro meses despues las siguen sometiendo para aprobacion.

Es el argumento mas dificil de refutar porque sale de su propio documento, y **por eso mismo no va al transmittal**: el cronograma se retiro de este transmittal por decision del usuario y citarlo lo reintroduciria por la puerta de atras. Queda aqui como municion para la **reunion semanal de coordinacion**, que es donde el cronograma si es materia.

---

## Nota de plazo

Es la cuarta submittal de este lote, y la septima consecutiva del proyecto, que pide devolucion muy por debajo de los siete dias habiles de la Clausula 37.2: tres dias corridos en las cuatro. La del `25007-0085` cae ademas en **sabado**. Se declara en el transmittal como constancia, sin convertirlo en observacion de documento.
