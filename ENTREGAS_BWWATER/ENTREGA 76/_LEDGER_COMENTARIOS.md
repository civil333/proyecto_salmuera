---
titulo: ENTREGA 76 — libro mayor de comentarios y su cierre
codigo: submittal 25007-0076
fecha: 2026-08-13
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 76 (submittal `25007-0076`) — libro mayor de comentarios

**Recibida el jueves 13-Ago-2026.** Dos planos, los dos en Rev B y los dos emitidos para aprobación. El Submittal Form pide respuesta el **domingo 16-Ago-2026**, día no hábil; el plazo contractual de ADASA son siete días hábiles desde la recepción, per la Cláusula 37.2 de la BAE, es decir el **lunes 24-Ago-2026**.

| # | Documento | Código | Rev | Sub. For | Comentario que responde | Veredicto previo |
|---|---|---|---|---|---|---|
| 1 | Civil and Loading Layout | `P22-DWG-09-005-001` | B | IFA | TM N16 NOTE-01 (submittal 25007-0034) | 2 — Approved as noted |
| 2 | GA of CIP Flushing Skid Pump | `P22-DWG-09-005-010` | B | IFA | TM N11 NOTE-05 (submittal 25007-0019) | 2 — Approved as noted |

Los dos venían de un Código 2 que no exigía nueva revisión: la instrucción era incorporar al emitir Rev 0. BW Water emitió una Rev B intermedia, que es más de lo que se le pidió, y la aprovechó para reescribir por completo la lámina de plintos del plano civil e incorporar detalles de anclaje por equipo que ADASA nunca solicitó. Ese contenido nuevo nunca estuvo aprobado y alimenta directamente el diseño civil, así que se revisa a fondo.

ADASA no aporta comentarios propios en esta entrega. Todo lo que sigue sale del contraste contra los documentos aprobados y contra el cuerpo de los planos, nunca contra la columna de respuesta de la hoja de comentarios.

---

## Parte A — Civil and Loading Layout `P22-DWG-09-005-001` Rev B

La hoja consolidada de comentarios trae una sola fila, con las dos partes de la NOTE-01 del TM N16 y una respuesta de dos líneas: *"1. Total approximate weight indicated in the revised drawing"* y *"2. Refer to notes in the drawing"*.

### Parte (a) — peso total del contenedor modificado: NO CERRADA

La Nota 2 de las dos láminas dice *"TOTAL ESTIMATED WEIGHT OF THE CONTAINER AND ITS CONTENTS IS APPROXIMATELY 29318.0 LBS [13300.0 KG]"*. La fila 17 de la tabla de cargas asigna al contenedor 3.700 kg.

Rehechas las sumas sobre la tabla de la Rev B:

| Suma | Valor |
|---|---|
| Pesos de operación de las filas 1 a 16 | 18.661,6 kg |
| Filas 17 a 23, que solo traen peso seco | 11.867,9 kg |
| **Operación de las filas 1 a 16 más seco de las filas 17 a 23** | **30.529,5 kg** |
| Suma en seco de todas las filas | 17.017,2 kg |
| **Suma en seco de todas las filas menos el contenedor** | **13.317,2 kg** |

El número declarado, 13.300 kg, coincide con la última fila con 0,1% de diferencia. Es decir: el rótulo dice contenedor más contenido, y el número es la suma en seco del contenido **excluyendo el contenedor** y excluyendo todo el inventario de fluido. El peso que necesita el diseñador de la fundación, con el módulo en operación y el contenedor incluido, es 30.529,5 kg, dos coma tres veces el valor declarado.

La conversión interna es correcta (29.318,0 lb son 13.298,4 kg), de modo que el error no está en las unidades sino en qué se sumó.

**Acción:** declarar por separado el peso del contenedor modificado vacío y el peso total en operación del conjunto, y corregir el rótulo de la Nota 2 para que diga qué incluye el número que da.

### Parte (b) — desglose del peso de operación del RO Skid: CERRADA, con un cabo suelto

BW Water hizo el trabajo, y conviene reconocerlo antes de observar. Las filas 6 y 7 pasaron de rotularse `RO SKID` con 4.278 kg seco y 8.058 kg de operación a rotularse `RO PRESSURE VESSELS` con 2.060 kg seco y 4.160 kg de operación. Se agregaron dos notas y seis filas:

- Nota 3: *"THE TABULATED WEIGHTS REFLECT THE UNIT MASS OF EACH COMPONENT, CONSIDERED INDEPENDENTLY"*.
- Nota 4: *"THE SPECIFIED ROPV WEIGHT IS INCLUSIVE OF THE MEMBRANE ASSEMBLIES AND THE HYDRAULIC CONTENTS"*.
- Filas 18 a 23: válvulas de PVC 60 kg, cañerías y fittings de PVC 490 kg, válvulas de super dúplex 245 kg, cañerías y fittings de super dúplex 1.090 kg, instrumentos 182,9 kg y soportes de cañería 6.100 kg.

Eso responde exactamente lo que se preguntó: qué incluye el peso y qué se contabiliza aparte.

El cabo suelto es el **marco estructural del skid**. Estaba dentro de la fila que se llamaba `RO SKID` y ahora esa fila solo cubre los recipientes a presión. Ninguna de las seis filas nuevas lo nombra; la única candidata por magnitud es `PIPE SUPPORTS`, que es otra cosa. Se pide indicar dónde quedó contabilizado o agregar su fila.

### Contenido nuevo — los detalles de anclaje

La Rev B incorpora siete tipos de plinto y cinco detalles de anclaje que la Rev A no tenía. Verificado por render, el detalle lleva el mismo número que el plinto:

| Plinto | Equipo | Dimensiones | Anclaje |
|---|---|---|---|
| 1 | Contenedor 40', extremos | 2,60 × 0,30 × 0,30 m | — |
| 2 | Contenedor 40', centrales | 2,60 × 0,30 × 0,322 m | — |
| 3 | Filtro cartucho CIP FIL-09-002 | 0,74 × 0,88 × 0,30 m | M10, 4 pernos, circunferencia Ø638, a 45° |
| 4 | Bomba CIP BH-09-002 | 0,50 × 0,52 × 0,26 m | **M12**, 4 pernos, patrón 200 × 266 mm |
| 5 | Skid dosificación BDS-09-001/002 | 1,23 × 0,88 × 0,20 m | **M18**, 10 pernos |
| 6 | Estanque dispersante TK-09-002 | 0,97 × 0,88 × 0,27 m | M8, 3 pernos, circunferencia Ø740 |
| 7 | Estanque CIP TK-09-001 | 2,50 × 2,50 × 0,20 m | M18, 4 pernos, circunferencia Ø1940 |

**El diámetro de perno contradice a los planos de detalle de los mismos equipos, y en un caso dentro de la misma entrega.**

- **Bomba CIP.** El detalle 4 del plano civil fija M12. El `GA of CIP Flushing Skid Pump` Rev B, que viaja en este mismo submittal, fija en su Nota 4.1 *"M14 THREADED ROD ANCHOR BOLTS"* y rotula la vista de empotramiento *"M14 BOLT X 4PCS"*. El patrón de pernos sí coincide en los dos planos, 200 × 266 mm. Lo que decide cuál es el correcto está en el propio plano de la bomba: su vista `BOLTING LAYOUT` acota el agujero de la placa base en **Ø14**, que es el agujero de paso normal de un perno M12 y no admite un M14. El error está del lado del plano de la bomba.
- **Skid de dosificación de dispersante.** El detalle 5 del plano civil fija M18 en 10 pernos. El `GA of Antiscalant Dosing Pump Skid` `P22-DWG-09-005-011` Rev B, aprobado en Código 2 en el TM N26, fija M10 en 10 pernos con 120 mm de empotramiento mínimo. El patrón y la cantidad coinciden; el diámetro no. Aquí el plano civil contradice un documento que ADASA ya aprobó.

**El empotramiento contra el espesor del plinto.** Los planos de detalle exigen 120 mm de empotramiento mínimo. Los plintos 5 y 7 tienen 0,20 m de espesor y el 7 lleva pernos M18. Un anclaje adhesivo M18 necesita del orden de 8 a 12 diámetros de empotramiento, entre 145 y 215 mm, y ahí ya no cabe en 200 mm con recubrimiento. Se pide declarar el empotramiento requerido de los detalles 5 y 7 y confirmar que el espesor del plinto lo admite.

**Los tres plintos centrales del contenedor quedan 22 mm más altos que los dos extremos.** La Sección A-A acota el plinto tipo 1 con la cara superior en la cota 300 y el tipo 2 en la 322, sobre un mismo cero. En la planta el orden es 1, 2, 2, 2, 1: los extremos abajo y los tres centrales arriba. Un contenedor de 40 pies transmite su carga por los castings de esquina, así que apoyarlo sobre tres puntos centrales levantados 22 mm lo deja en falso sobre las esquinas, salvo que el escalón sea una contraflecha deliberada. El plano no lo dice, y quien construya nivelará los siete plintos a una sola cota. Se pide declarar si el escalón es intencional y, si lo es, escribirlo como nota.

### Contenido nuevo — la tabla de cargas contra los documentos aprobados

**Estanque CIP TK-09-001, 10.470 kg de operación.** La Equipment List `P22-LI-09-005-001` Rev B fija Dayamas DYM 6800, HDPE, 1.800 mm de diámetro por 2.950 mm de altura, altura efectiva 2.550 mm y **capacidad efectiva 6,1 m³**, confirmada por la propia hoja de comentarios de esa lista (*"CIP tank effective capacity is 6.1 m3"*). Con 270 kg de tara, el peso en operación queda del orden de 6.400 kg, y aun lleno hasta el borde geométrico, 7,5 m³, no pasa de 7.800 kg. El plano declara 10.470 kg, que exigen 10,2 toneladas de líquido en un estanque que no las contiene. El valor viene sin cambios desde la Rev A.

**Estanque de dispersante TK-09-002, 517,5 kg de operación.** La misma lista fija Promatics PLC330, 630 mm de diámetro por 1.090 mm de altura y capacidad efectiva 0,27 m³. Con 15 kg de tara y una densidad de dispersante del orden de 1,2, el peso en operación queda entre 340 y 420 kg. El plano declara 517,5 kg, y la Rev A declaraba 490.

Los dos son conservadores para la fundación, y por eso no comprometen la seguridad. Comprometen el costo: ADASA paga la fundación que estos números dimensionan.

### Diferencial completo de la tabla de cargas, Rev A contra Rev B

| Fila | Ítem | Rev A operación | Rev B operación | Δ |
|---|---|---|---|---|
| 2 | Filtro cartucho RO | 462,6 | 470,0 | +7,4 |
| 3 | Bomba de alta BH-09-001 | 1.340,0 | 1.406,1 | +66,1 |
| 6 y 7 | `RO SKID` → `RO PRESSURE VESSELS` | 8.058,0 | 4.160,0 | **−3.898,0** |
| 11 | Filtro cartucho CIP | 267,6 | 270,0 | +2,4 |
| 12 | Estanque dispersante | 490,0 | 517,5 | +27,5 |
| 13 | Skid dosificación | 57,4 | 100,0 | +42,6 |
| 14 | Panel de control local | 350,0 | 800,0 | **+450,0** |
| 16 a 23 | Aire acondicionado, contenedor, válvulas y cañerías de PVC y de super dúplex, instrumentos, soportes | — | 12.007,9 | **filas nuevas** |

Las filas 1, 4, 5, 8, 9, 10 y 15 no se movieron.

El salto del panel de control local, de 350 a 800 kg, es coherente con el cambio de envolvente a acero inoxidable que dejó el RFI-002 y con el datasheet nVent Hoffman FS66S aprobado. Se declara como tal y no como error.

---

## Parte B — GA of CIP Flushing Skid Pump `P22-DWG-09-005-010` Rev B

La hoja de comentarios trae la NOTE-05 del TM N11 con sus tres peticiones y una respuesta de dos líneas, que solo reclama haber hecho dos. Verificado contra el cuerpo del plano, las tres están.

| Pedido del TM N11 | Estado | Evidencia en la Rev B |
|---|---|---|
| Plano de disposición de pernos con diámetro, separación y empotramiento | **CERRADA** | Nota 4: pernos de barra roscada, cantidad 4, empotramiento mínimo 120 mm, distancia al borde no menor a 150 mm, separación no menor a 100 mm. Vistas `BOLTING LAYOUT` (placa base 251 × 331 mm, patrón 200 × 266 mm, agujero Ø14) y `EMBEDMENT DEPTH` |
| Reacciones sísmicas de base Fx, Fy, Fz | **CERRADA** | Nota 9.1: Fx = 1,2356 kN rotulado corte sísmico, Fy = 1,7652 kN rotulado carga muerta, Fz = 0,6178 kN rotulado corte del perno |
| Masa del equipo para verificación de carga | **CERRADA**, aunque la respuesta escrita no la menciona | Nota 3: *"ESTIMATED LOADING: 180 KGS [397 LB]"*, y Nota 8.1 el centro de gravedad, Z = 742 mm |

La NOTE-05 cierra. Lo que queda es la coherencia interna de esas cifras, y es todo incorporable al emitir sin nueva revisión.

**El factor sísmico declarado no es el que se usó.** La Nota 6 fija la carga de diseño como *"180 KG PUMP + SEISMIC FORCE 0.3G"*. Fy vale 1,7652 kN, que es exactamente 180 kg por 9,81, de modo que Fy es el peso propio. Fx vale 1,2356 kN, que es **0,70 veces** ese peso, no 0,30. El plano hermano `-011`, aprobado en Código 2, usa el mismo factor 0,70 declarando también 0,3 g. El factor aplicado es más exigente que el declarado, así que las reacciones no quedan cortas; lo que falla es el rótulo, y un revisor externo que verifique la nota contra el número encuentra una contradicción.

**El bloque se titula reacciones totales y da un valor por par de pernos.** Fz vale 0,6178 kN, que es Fx dividido por dos sobre cuatro pernos. En el plano hermano la relación es la misma: Fz vale 0,2048 y Fx 1,0242, dividido por cinco sobre diez pernos. En los dos casos el divisor es la mitad de la cantidad de pernos, criterio conservador y habitual, pero el encabezado dice `TOTAL SEISMIC REACTION FORCES` y el valor no es total. Es el mismo defecto que el TM N26 levantó como OBS-01 sobre el plano hermano y que no se corrigió al escribir este.

**El rótulo de los ejes no sigue convención.** Fy se declara carga muerta vertical y Fz corte del perno, cuando Fz es habitualmente el eje vertical. El diseñador civil no recibe la tracción ni la compresión vertical por perno, que es lo que gobierna un anclaje químico post-instalado. Se pide declarar tracción y compresión por perno con los ejes rotulados en la convención habitual.

**La vista de empotramiento no acota el empotramiento.** La vista `EMBEDMENT DEPTH` acota 149 mm desde la cara superior de la tuerca hasta el extremo inferior de la barra, que es el largo total del perno. Descontando la placa base y la tuerca, la parte embebida queda por debajo de los 120 mm que exige la Nota 4.3. La vista que debiera demostrar el cumplimiento del empotramiento demuestra lo contrario.

**El informe de cálculo no está identificado.** La Nota 9 dice *"AS PER CALCULATION REPORT"* sin código ni revisión. El candidato es el `UHPRO Structural Calculation Report` `P22-CD-09-005-001` Rev 0 de la ENTREGA 71. Se pide identificarlo por código y revisión; sin eso la cifra no es trazable.

**La Nota 2 mantiene** *"BOLTING DETAILS TO BE FINALIZED AND ENDORSED"*, igual que el plano hermano. Ese cierre vive en el informe de cálculo endosado y se sigue por la Sección de pendientes del transmittal; no degrada este plano.

---

## Parte C — el impacto sobre el frente OOCC y sobre la licitación

Está desarrollado en `_IMPACTO_OOCC_BL.md`. El resumen que gobierna el veredicto:

- La Nota Particular 2 del plano `P22-DWG-00-002-007` Rev 0 de L&A, apto para construcción, dice literal: *"DISPOSICIÓN Y DIMENSIONES DE PERNOS DE ANCLAJE, PENDIENTES HASTA LA ENTREGA DE LOS PLANOS VENDOR DE LOS EQUIPOS"*. **Esta Rev B es ese insumo**, y llega con los dos diámetros contradictorios de la Parte A. Mientras no se resuelvan, L&A no puede cerrar su nota y los pernos no se pueden dejar. Esto fija la fecha de la confirmación operativa, no el código del documento.
- El plinto del estanque CIP mide 2,50 × 2,50 m en la Rev B y la fundación construida es un octógono de **2,20 × 2,20 m**. Sobre el octógono construido, la circunferencia de pernos Ø1940 deja 130 mm al borde, por debajo de los 150 mm que el propio BW Water fija como distancia mínima.
- La malla de plintos del contenedor sí coincide: cinco plintos a 3,000 m entre ejes en los dos documentos.
- La tabla de pesos de la Sección 6.4 de la BL Montaje Rev 0 está tomada de la Rev A, y cinco de sus nueve filas cambian con la Rev B.
- Las seis filas nuevas de cañerías, válvulas, instrumentos y soportes son un total de módulo sin repartir entre el interior del contenedor y la zona CIP, que son dos fundaciones distintas. Tal como están, no se pueden asignar.

---

## Disposición propuesta

| Documento | Rev | Código | Motivo en una línea |
|---|---|---|---|
| GA of CIP Flushing Skid Pump `-010` | B | **2** | Cerró las tres partes de la NOTE-05; lo que queda son rótulos y coherencia interna que se incorporan al emitir Rev 0 |
| Civil and Loading Layout `-001` | B | **2** | Cerró el desglose que se le pidió; el diámetro de anclaje se alinea con el plano del equipo y el número de la Nota 2 se rectifica, las dos cosas al emitir Rev 0 |

**Veredicto global propuesto: 2 — Approved as noted.**

El criterio es el de la Sección 6.2: el código refleja el estado del documento revisado en sí, y la pregunta que decide es si el propio plano debe cambiar para llegar a Rev 0 sin una revisión intermedia. Todo lo que se le pide al plano civil cabe en esa forma: fijar el diámetro en los detalles 4 y 5, rectificar el número de la Nota 2, agregar la fila del marco estructural del skid y declarar si el escalón de 22 mm es intencional. Ninguna de esas correcciones exige rehacer el documento.

Un Código 3 aquí no se sostiene por tres razones. La primera es que alinear un documento con otro es Código 2 por regla del proyecto, y el 3 se reserva para cuando el contenido propio está mal de raíz. La segunda es que los dos planos venían de un Código 2 de ADASA y el proveedor reemitió sin estar obligado a hacerlo, de modo que bajarlos ahora contradice la aprobación propia, que es el mismo criterio con que se resolvió la ENTREGA 75. La tercera es que la urgencia de la interfaz con L&A es un argumento de plazo y no de codificación: se atiende por su propia vía, no inflando el código.

**Esa urgencia sale como confirmación operativa con fecha propia.** El diámetro de los pernos de anclaje de los detalles 4 y 5 se pide confirmado **antes de que se ejecuten los pernos post-instalados**, no como condición de la Rev 0, porque la Nota Particular 2 del plano de fundaciones de L&A depende de ese dato y la obra civil está construida. Es el mecanismo que se usó en la ENTREGA 75 con el formulario del ensayo hidrostático.

---

## Triaje: por qué cada punto queda dentro o fuera

### ADASA fue clara y BW Water no lo hizo

| Punto | Qué se pidió, literal | Qué contestó | Decisión |
|---|---|---|---|
| Peso total del contenedor | *"Total weight of the modified 40 ft container"* (NOTE-01 del TM N16) | *"Total approximate weight indicated in the revised drawing"*, con una Nota 2 cuyo número es la suma en seco del contenido sin el contenedor | **Se mantiene.** La petición nombra un peso concreto y el plano da otro con un rótulo que no le corresponde |

### ADASA no fue suficientemente clara

| Punto | Qué se pidió | Qué contestó | Decisión |
|---|---|---|---|
| Desglose del RO Skid | *"Confirm the RO Skid operating weight (items 6-7, 8,058 kg) fully accounts for all interior piping (super-duplex HP + process), including steel mass, fluid inventory and fittings, **together with skid frame**, pressure vessels and wet membranes. If any piping mass is excluded, declare it separately"* | Reclasificó la fila a recipientes a presión, agregó las Notas 3 y 4 y seis filas de cañerías, válvulas, instrumentos y soportes | **Cierra en lo que respondió, y NO cierra en el marco del skid.** 🔴 **Corrección del 17-Ago:** este ledger afirmaba que la petición no nombraba el marco. Sí lo nombra, literal, en la hoja de comentarios del propio plano. De modo que el marco es **cierre pendiente de un comentario previo**, no un agregado de ADASA, y por eso sobrevive al re-alcance |

### ADASA estaría exigiendo más de lo que pidió

| Punto | Situación | Decisión |
|---|---|---|
| Rigor de la hoja de comentarios | La respuesta a la NOTE-05 reclama dos de las tres partes, pero el plano trae las tres | **Se saca.** El documento manda sobre la columna de respuesta, y el documento cumple |
| Nueva revisión del plano de la bomba | Venía de Código 2 sin obligación de reemitir, y reemitió | **Se saca como reclamo.** Emitir la Rev B es más de lo pedido; los defectos que trae se tratan por su mérito |
| Pesos conservadores de los dos estanques | Los valores exceden lo que los equipos aprobados admiten, pero por exceso | **Se mantiene, con encuadre de costo, no de seguridad.** El sobredimensionamiento lo paga ADASA en la fundación |
| Contraflecha de 22 mm en los plintos centrales | No hay requisito que prohíba una contraflecha | **Se mantiene como pregunta, no como incumplimiento.** Lo que se exige es que quede escrito, porque quien construye nivela |
| Detalles de anclaje que nadie pidió | ADASA nunca solicitó los detalles 3 a 7 | **Se revisan igual.** Son contenido nuevo, no aprobado, y son el insumo que la ingeniería civil está esperando. Lo que no corresponde es imputar falta por haberlos entregado |

### Lo que este triaje puso sobre la mesa y no estaba en la entrega

Que la fundación del estanque CIP ya construida mide 2,20 m y el plano del proveedor sigue mostrando 2,50 m no lo levantó ninguna de las dos partes. Es acción de ADASA sobre su propia ingeniería y sobre el paquete de licitación, y no depende de la respuesta de BW Water.

---

## Re-alcance del 17-Ago-2026 — solo cierre de comentarios previos

**Criterio del usuario, aplicado a todo el análisis:** la revisión de un documento que responde a comentarios previos se limita a **si esos comentarios están cerrados**. No se introducen observaciones nuevas. Dos razones: la ingeniería de obras civiles la ejecuta L&A y lo que sale de los planos de BW Water se ve con ellos, no con el proveedor; y no hay tiempo para más iteraciones de revisión.

**El alcance lo fija la columna de comentario del cliente de la hoja consolidada**, que trae el texto literal del pedido original. Leerla cambió dos cosas en esta entrega: confirmó que el marco del skid **sí** estaba pedido (ver la corrección de arriba), y dejó fuera todo lo demás.

### Disposición final de la entrega

| Documento | Comentario previo | Estado | Código |
|---|---|---|---|
| Civil and Loading Layout `-001` | NOTE-01 del TM N16, dos partes | **Ninguna cerrada**: falta el peso del contenedor vacío y el marco del skid quedó sin fila | **2**, con dos observaciones |
| GA of CIP Flushing Skid Pump `-010` | NOTE-05 del TM N11, tres partes | **Las tres cerradas.** La respuesta escrita reclama dos; la masa de 180 kg y el centro de gravedad están en las Notas 3 y 8.1. El documento manda sobre la columna de respuesta | **1**, sin PDF anotado |

### Lo que se retira del transmittal

Todo esto queda acá con su evidencia y **no se le comenta a BW Water**. Los cinco primeros son la conversación con L&A y están consolidados en `_IMPACTO_OOCC_BL.md`:

1. Diámetro de los pernos de anclaje de los detalles 4 y 5 (M12 contra M14 y M18 contra M10).
2. Empotramiento requerido de los plintos 5 y 7 contra su espesor de 200 mm.
3. Escalón de 22 mm de los tres plintos centrales del contenedor.
4. Reparto de las seis filas nuevas entre el interior del contenedor y la zona CIP.
5. Fundación del estanque CIP de 2,20 m construida contra 2,50 m dibujada, y los pedestales de los equipos CIP sobre un bloque plano.
6. Valores vinculantes que ADASA iba a declarar: el peso de operación del estanque CIP contra los 6,1 m³ efectivos, y el TAG del mezclador estático `MZE-09-001` contra `MZE-09-009`.
7. Del plano de la bomba: factor sísmico declarado (0,3 g contra 0,70 aplicado), título del bloque de reacciones, tracción y compresión por perno, vista de empotramiento que acota el largo total de la barra, e identificación del informe de cálculo.

Los puntos 6 y 7 no tienen vía abierta hoy: quedan registrados para el ciclo de Rev 0 de cada plano. Los 1 a 5 viven en `INT-11` del registro de compromisos, y la tabla de pesos de la BL Montaje en `INT-10`.
