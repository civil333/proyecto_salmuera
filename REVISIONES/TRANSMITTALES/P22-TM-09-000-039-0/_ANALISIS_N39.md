---
titulo: Analisis interno — Transmittal N39 (P22-TM-09-000-039-0)
codigo: P22-TM-09-000-039-0
fecha: 2026-09-09
estado: INTERNO — disposicion propuesta
type: analisis
project: salmuera-taltal
---

# Analisis interno — Transmittal N39

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

## 1. Recepcion y plazos

| Submittal | Entrega | Emitido | Devolucion pedida | Vencimiento real Clausula 37.2 | Docs |
|---|---|---|---|---|---|
| 25007-0091 | E91 | 4-Sep-2026 | 7-Sep-2026 | **martes 15-Sep-2026** | 2 |
| 25007-0092 | E92 | 8-Sep-2026 | 11-Sep-2026 | **jueves 17-Sep-2026** | 1 |

Los dos formularios piden devolucion en tres dias corridos contra los siete habiles del
contrato. Son el octavo y el noveno lote consecutivos por debajo del plazo. Este transmittal
sale dentro de los dos vencimientos reales.

La E91 entrega ademas el `.dwg` nativo del plano, que **no esta declarado en su formulario**.

## 2. La regla que gobierna: solo se verifica el cierre de lo pedido

Los tres documentos responden a comentarios previos, de modo que el universo de la revision
es la lista de lo exigido y nada mas. No se abren observaciones nuevas. El estado es binario,
levantado o no levantado, y cada cierre exige cita del cuerpo del documento: la respuesta de
la hoja de comentarios no cierra nada por si sola.

El procedimiento de radiografia llega ademas en **Rev 0**, y sobre un Rev 0 solo caben
Codigo 1 o Codigo 3.

## 3. Valve List `P22-LI-09-005-002` Rev E

**Origen.** Rev D en **Codigo 1** desde el TM N18, sin comentarios de contenido abiertos. La
re-emision responde a tres cambios que BW Water comprometio por escrito, que son el universo
de esta revision. El criterio esta fijado en el seguimiento de compromisos.

**Verificacion punto por punto sobre el documento:**

| Punto | Pedido | Verificado en la Rev E | Estado |
|---|---|---|---|
| TAG del modelo 3D | Incorporar `VM-09-131`, `VM-09-132`, `VM-09-133` y `VRP-09-001`, ausentes de las listas aprobadas | Los cuatro estan, y los cuatro figuran en el P&ID Rev 0 aprobado. Son exactamente los TAG que aparecen respecto de la Rev D | **Cerrado** |
| Valvula reductora | Reflejar el cambio de placa de orificio a valvula reductora en `CIT-09-004` | Fila 114: `VRP-09-001 ... PRESSURE REGULATING VALVE, SELF-ACTUATED, CE3MN, REJECT 1ST, SSDS, NPT, SCH80, ANSI 900#` | **Cerrado** |
| Succion CIP en SS316 | Reflejar en la lista el cambio de material de la succion de la bomba CIP | La linea `CP-SS316-DN150-09-022`, DN150, `CIP PUMP SUCTION`, es `316L Stainless Steel` en la Line List Rev 1 aprobada. En el P&ID Rev 0, hoja 11, el rotulo de esa linea esta a **16 puntos** de `VM-09-065`, que es la unica valvula DN150 del circuito CIP. La Rev E mantiene esa valvula en `PVC PVC PVC EPDM`, con extremos `Lug SCH80 ANSI 150#` | **Abierto** |

**Mejora no pedida, que se reconoce.** `VM-09-015` sale de la lista. Ese TAG no existe en el
P&ID Rev 0 y arrastraba historia desde el TM N3; su eliminacion alinea la lista con el plano
aprobado. La fila que ocupaba pasa a `VM-09-131`, con los mismos atributos.

### Fuera de alcance, con la razon

- **La tension de alimentacion de los actuadores.** Trece valvulas motorizadas pasan de
  `380/220 VAC` a `230 VAC, 50Hz, Single Phase` sin que la hoja de comentarios lo declare, y
  el Electrical Load List Rev 0 aprobado dice `220 V`. **No se emite.** ADASA entrega en el
  gabinete principal a 380 V y toda la transformacion y distribucion interna del modulo es
  alcance de BW Water, de modo que la tension de sus propios actuadores es decision suya.
  Queda la constancia de que se reviso y no se objeta.
- **La portada declara `Revision No.: A` y `Date: 11/12/2025`** sobre un documento que se
  emite como Rev E del 2-Sep-2026, y anuncia `Page: 1of 2` en un PDF de tres paginas.
  Housekeeping documental: **no se emite**.
- **El historial de la portada no coincide con el del cajetin** en la fila de la Rev A, ni en
  fecha ni en aprobador. Housekeeping: **no se emite**.
- **La hoja de comentarios no transcribe ningun comentario de ADASA**: su unica fila dice
  `(changes on file)` y deja vacia la columna del transmittal de origen. Se traslada al texto
  de la subseccion, sin observacion propia, porque la exigencia de una fila por comentario se
  hizo sobre otro documento.

### Disposicion

**Codigo 2 — Approved as noted.** Dos de los tres cambios comprometidos estan incorporados y
verificados contra el P&ID Rev 0. Falta el tercero, que es el unico con consecuencia de
compra: una valvula declarada en PVC sobre una linea que la Line List aprobada lleva en 316L.
Se incorpora al emitir Rev 0, sin revision intermedia.

## 4. GA del estanque de antiescalante `P22-DWG-09-005-015` Rev D

**Origen.** Rev C en **Codigo 2** desde el TM N36, cuya accion decia emitir a Rev 0 sin nueva
revision de aprobacion. Llega una Rev D de aprobacion, que ADASA no requirio. Se codifica
igual, con constancia, que es el precedente del TM N34 sobre el GA de la bomba dosificadora.

**Verificacion punto por punto sobre el documento:**

| Punto | Pedido | Verificado en la Rev D | Estado |
|---|---|---|---|
| OBS-01 | Reconciliar las dos cotas del agujero de anclaje contra el perno M12 | El detalle de empotramiento rotula `Ø14 [Ø35/64"]`. Treinta y cinco sesenta y cuatroavos de pulgada son 13,89 mm, de modo que las dos unidades ya nombran la misma dimension y ambas admiten el `M12 HH BOLT C/W WASHER` del mismo detalle | **Cerrado** |
| NOTE-01 | Declarar la elevacion de la marca de nivel correspondiente al volumen util | La fila `LEVEL MARKING` de la tabla de boquillas mantiene guion en `SIZE` y guion en `ELEVATION (in)`, con `SIDE` en `LOCATION`. Identica a la Rev C. Verificado por render a 300 ppp de la lamina, que esta rotada 270 grados | **Abierto** |

🔴 **La hoja de comentarios declara un cierre que el documento no tiene.** Su fila 3 responde
`2. Level mark added with dimensions` a la NOTE-01. La tabla no lleva ni tamano ni elevacion.
Es el mismo modo de falla que el TM N6 califico de falla severa de aseguramiento de calidad
cuando la hoja declaro corregidos dos TAG duplicados que seguian en el documento.

**Dependencia que no degrada a este plano.** La nota 16 declara las reacciones sismicas
`(AS PER CALCULATION REPORT)` sin citar codigo ni revision, y la propia hoja de comentarios
responde que los datos sismicos se entregaran cuando un Ingeniero Profesional verifique los
calculos. El informe `P22-CD-09-005-001` sigue sin endoso y vive en la Seccion 3.

### Fuera de alcance, con la razon

- **El volumen total instalado.** La nota 7 mantiene `TANK CAPACITY 335 L` y el ciclo de la
  Rev A pedia declarar 0,34 metros cubicos. El TM N26 no lo repitio en su accion sobre la
  Rev B, de modo que exigirlo ahora seria leer de mas. **No se emite.**
- **El radio rotulado `R74 [R3"]`**, otra pareja que no equivale. Identico en la Rev B, la C y
  la D, de modo que no forma parte de lo agregado. **No se emite.**

### Disposicion

**Codigo 2 — Approved as noted.** De los dos puntos del Codigo 2 del TM N36, uno cierra y el
otro no. El que queda es una celda de la tabla de boquillas, incorporable al emitir Rev 0 sin
revision intermedia.

## 5. Procedimiento de radiografia `P22-BA-09-000-015` Rev 0

**Origen.** Rev C en **Codigo 2** desde el TM N37, con el determinante en el alcance. Es el
tercero de la familia de ensayos no destructivos en llegar a revision numerica y el unico de
las dos entregas sometido para construccion.

**Verificacion punto por punto sobre el documento:**

| Punto | Pedido | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| OBS-01, el determinante | Declarar en el alcance el material y el rango de espesor efectivamente radiografiados | La clausula de alcance dice `This procedure describes the Radiography Testing of Material Duplex S32750, In walls thickness of 6.02 to 8.56mm using Gamma ray (Ir 192)` | **Cerrado** |
| NOTE-02 | Reapuntar las dos referencias cruzadas que quedaron del renumerado | La clausula 11.6 remite a `T-277.2 Section 5 Article 2` y la 19.4 a `(T-282.1)`. Ninguna apunta ya a 15.3 ni a 17.3 | **Cerrado** |
| NOTE-03 | Llevar cada comentario del transmittal anterior como fila propia de la hoja | La hoja trae cuatro filas, una por comentario, contra la Rev C | **Cerrado** |
| NOTE-01 | Declarar el numero de documento propio al emitir Rev 0 | La caratula pasa de `DOC NO: PMI PROV-PROC-RT-001` a `DOC NO: RT PROV-PROC-RT-001`. Cambio el prefijo, no el numero: sigue sin ser `P22-BA-09-000-015` | **Abierto** |

Las cuatro respuestas de la hoja dicen lo mismo, `Revised as per comment`, incluida la del
numero de documento, que no se corrigio.

### Fuera de alcance, con la razon

- **El documento no declara internamente ningun estado de emision**, pese a que su formulario
  lo somete como IFC. No existe campo de proposito de emision en las 33 paginas. Se documenta
  junto al numero de documento, sin degradar.
- **La caratula cita `ASME Section V, Article 9`**, que gobierna el examen visual, mientras el
  procedimiento del subcontratista aplica el Articulo 2, que es el de radiografia. El punto
  vive en la caratula, que ya venia asi en la Rev C y que ADASA no objeto entonces. **No se
  emite**, por la regla del diff contra lo aprobado.
- **El anexo del subcontratista se rotula `WI-OD-RT02, Rev.0`** y su propio registro de
  revisiones no tiene fila para esa revision, con la ultima en `C / 26 AUGUST 2026`.
  Housekeeping del anexo: **no se emite**.

### Disposicion

**Codigo 1 — Approved.** El determinante cerro y con el las dos notas de forma. Lo que queda
es el numero de documento, que es identificacion documental y por regla propia no degrada por
si solo: se documenta para incorporar cuando el procedimiento vuelva a tocarse. Es el mismo
tratamiento que recibio el procedimiento de liquidos penetrantes en el TM N38, con el mismo
defecto y en la misma familia.

## 6. Resumen de disposicion

| # | Documento | Rev | Emision | Codigo previo | **Propuesto** | CC_ADASA |
|---|---|---|---|---|---|---|
| 2.1 | Valve List | E | IFA | 1 (N18) | **2** | si |
| 2.2 | GA of Antiscalant Dosing Tank | D | IFA | 2 (N36) | **2** | si |
| 2.3 | Radiography Examination Procedure | 0 | IFC | 2 (N37) | **1** | no |

**Veredicto global: 2 — Approved as noted.** Un Codigo 1 y dos Codigo 2. **Cero Codigo 3.**
Ningun documento vuelve a revision.

**Efecto en el Master Register**, desde 68 / 19 / 2 / 0:

- `P22-LI-09-005-002` de 1 a 2, Rev D a Rev E, E38 a E91.
- `P22-DWG-09-005-015` se mantiene en 2, Rev C a Rev D, E84 a E91.
- `P22-BA-09-000-015` de 2 a 1, Rev C a Rev 0, E86 a E92.

**Tally esperado 68 / 19 / 2 / 0.** El de Codigo 1 no se mueve porque uno entra y otro sale, y
el de Codigo 2 tampoco por la misma razon. Sin items nuevos: los tres son re-revisiones.
Entregas 91 y 92; transmittals 38 a 39.

🔴 **Correccion aparte, de ADASA y no del proveedor.** La fila del `P22-CD-09-005-001` esta en
Rev B del TM N29 cuando los transmittals N37 y N38 lo declaran emitido en revision 0 para
construccion desde la entrega 71 del 6 de agosto. Se corrige en la misma corrida del updater
y se declara como accion propia, no como observacion.

## 7. Que NO puede cruzar al documento emitido

- Ninguna observacion nueva: el universo son los comentarios previos y esta cerrado.
- La tension de los actuadores, que es alcance interno del proveedor.
- Los cuatro puntos de housekeeping de la Valve List, del GA y del procedimiento.
- Sin codigos internos de seguimiento, sin el asesor interno, sin el saldo de jornadas del
  tercero inspector.
- Sin cifras de multa y sin invocar el umbral de atraso.
- Sin numeros manuales en los encabezados: el template numera solo.
- Referencias por nombre de seccion, cero simbolo de seccion.
