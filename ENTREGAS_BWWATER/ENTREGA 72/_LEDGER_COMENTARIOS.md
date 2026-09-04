---
titulo: "Libro mayor de comentarios — ENTREGA 72 (25007-0072), cuatro documentos"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-10
---

# Libro mayor de comentarios — ENTREGA 72

> Documento interno de trabajo. **NO ENVIAR.** Registra cada comentario que ADASA emitió sobre los cuatro documentos de esta entrega y el estado de su cierre, verificado contra la revisión nueva.

## Alcance

La ENTREGA 72 (submittal `25007-0072`, recibida el 06-Ago-2026 a las 09:46) trae cuatro documentos. Llegó un día después de que saliera el Transmittal N30, así que quedó sin veredicto hasta ahora.

| Documento | Rev | Venía de | Condición |
|---|---|---|---|
| `P22-BT-09-009-001` Plant Control Philosophy | **0** | Código 2, TM N28 | OBS-01 a OBS-04 más NOTE-01 |
| `P22-BA-09-000-009` RO Vessel Hydrostatic Test Procedure | **0** | Código 2, TM N27 | OBS-01, OBS-02, NOTE-01 |
| `P22-DWG-09-005-005` Tie-In Point Layout | B | Código 3, TM N7 | Cinco puntos |
| `P22-DWG-09-005-008` GA of SWRO System Skid | B | Código 2, TM N15 | NOTE-11, NOTE-12 |

**Catorce entradas a verificar.** Los cuatro documentos traen Consolidated Comment Sheet.

## Estados

**CERRADO** — la evidencia cubre íntegra la acción pedida. **PARCIAL** — cubre parte, o el documento se contradice. **NO LEVANTADO** — el defecto sobrevive o el proveedor hizo otra cosa. Cada estado exige cita con página. Una respuesta del tipo *"Updated. Aligned with..."* no cierra nada por sí sola.

**Convención de página.** Se cita la **página impresa del documento**, que es la del pie (`N of 59` en la filosofía de control), y entre paréntesis la **página del archivo PDF**, que es donde se coloca la anotación del `CC_ADASA`. Las dos difieren en tres, porque el archivo antepone la carátula y las tres hojas de comentarios.

**Para los dos Rev 0 el estado se colapsa a binario al decidir**: la condición se cumplió entera o no se cumplió.

## Advertencia de método que este trabajo confirmó

La hoja de comentarios de la Plant Control Philosophy **no tiene texto extraíble en la columna del cliente**: los comentarios de ADASA están pegados como recortes de imagen del PDF anotado. La extracción devuelve la columna vacía. Solo aparecen al renderizar las páginas 2 a 4. Es el mismo modo de falla que ya costó dos retractaciones en el proyecto.

## Fuentes de verificación

Instrument List `P22-LI-09-008-003` Rev E · Valve List `P22-LI-09-005-002` Rev D · Equipment List `P22-LI-09-005-001` Rev B · Alarm and Interlock List `P22-LI-09-008-015` Rev C · Especificación Técnica `P22-ET-09-000-001-0`.

---

## 1. `P22-BT-09-009-001` — Plant Control Philosophy Rev 0

Condición del Código 2 del Transmittal N28: espejar los TAG de devanado y rodamiento de las bombas de alta y de CIP a la Instrument List, reconciliar las consignas de temperatura de motor, vibración y baja presión de descarga con la Alarm and Interlock List, y confirmar el disparo de devanado contra la clase de aislación del motor.

| ID | Estado | Evidencia |
|---|---|---|
| OBS-01 | **NO LEVANTADO** | La corrección se aplicó solo a la bomba de alta. Página 36 (PDF 39): *"RO HP Pump Winding Temperature Sensor (PT100) — TE-09-001/003"* y *"RO HP Pump Bearing Temperature Sensor (PT100) — TE-09-002/004"*, correcto. **Página 55 (PDF 58), sección 3.4.2, el par del CIP sigue invertido**: ítem 13 *"CIP Pump Bearing Temperature Sensor (PT100) — TE-09-003"* e ítem 14 *"CIP HP Pump Winding Temperature Sensor (PT100) — TE-09-004"*, cuando la Instrument List Rev E define `TE-09-003` como *CIP Pump Winding* y `TE-09-004` como *CIP Pump Bearing*. El documento además se contradice: su página 36 cuenta a `TE-09-003` entre los sensores de devanado |
| OBS-02 | **PARCIAL** | Los valores sí se reconciliaron. Página 38 (PDF 41): devanado alarma 120 °C y disparo 140 °C, rodamiento alarma 90 °C y disparo 95 °C, que son los de la Alarm and Interlock List Rev C. **La segunda mitad no**: se pedía confirmar el disparo de devanado contra la clase de aislación, y la cita de *Class B* se eliminó en vez de confirmarse. Las palabras `class` e `insulation` no aparecen en ninguna de las 62 páginas del archivo, de modo que un disparo de 140 °C queda sin clase declarada que lo respalde |
| OBS-03 | **NO LEVANTADO** | Página 39 (PDF 42): bomba de alta *"High alarm: 7.1 mm/s RMS"*, contra los **7,0** de `VIT-09-001.AH` en la Alarm and Interlock List Rev C. Páginas 41 y 43 (PDF 44 y 46): los dos turbochargers con *"High-high trip: 7.1 mm/s RMS"*, contra los **6,0** de `VT-09-002.AHH` en esa misma lista. La diferencia de 7,1 contra 6,0 es literalmente la que enunciaba el comentario. Se mantiene además el disparo de 10,0 mm/s sobre un transmisor rangeado de 0,0 a 8,9 |
| OBS-04 | **CERRADO** | El comentario ofrecía dos vías y el documento tomó la segunda. Página 40 (PDF 43): *"a sustained low-pressure condition at the discharge side shall be monitored to detect potential rupture or major leakage scenarios (please refer to Alarm and Interlock List documentation)"*. Los valores de 45 bar por 5 segundos y 50 bar por 3 segundos ya no están en el cuerpo |
| NOTE-01 | **PARCIAL** | Los dos errores de TAG se corrigieron: la página 46 (PDF 49) tagea la *RO Stage 2 Permeate Flow* como `FIT-09-002`, y la página 34 (PDF 37) lista *"Motorized valves VE-09-014/016"*. **Fijar los hijos por código y revisión no se hizo**: la tabla de documentos de referencia de la página 5 (PDF 8) sigue diciendo `Controls & Sequence Chart | SEPARATE DOCUMENT` y `Alarm and Control Setpoint List | SEPARATE DOCUMENT`, pese a que los dos están emitidos como `P22-LI-09-008-017` Rev A y `P22-LI-09-008-015` Rev C |

**Binario: 1 de 5.** Las respuestas de la hoja de comentarios dicen *"Updated. Aligned with alarm and interlock list"* en OBS-02, OBS-03 y OBS-04, y *"Updated. Aligned with other list"* en OBS-01. Tres de esas cuatro no se sostienen contra el cuerpo.

**Disposición decidida:** se devuelve **sin código**, declarando qué puntos siguen abiertos y por qué. No se codifica un documento ya emitido para construcción.

---

## 2. `P22-BA-09-000-009` — RO Vessel Hydrostatic Test Procedure Rev 0

Condición del Código 2 del Transmittal N27: declarar las presiones de ensayo vinculantes en la cara del procedimiento, y confirmar qué manómetro se usó en el ensayo de 136,5 bar adjuntando su certificado dentro del rango de 1,5 a 4 veces que el propio procedimiento fija.

| ID | Estado | Evidencia |
|---|---|---|
| OBS-01 | **CERRADO** | PDF página 9, hoja 4 de 6 del procedimiento Protec, bajo el rótulo *Test Pressure*: *"1.1 times the design pressure for ASME certified vessels / BPV81200SP7 Tested at 91.0 Bar / BPV81800SP7 Tested at 136.5 Bar"*. Las dos presiones vinculantes están en la cara del procedimiento |
| OBS-02 | **CERRADO con residual** | Los dos certificados no conformes desaparecieron: el 0 a 160 bar (27258) y el 0 a 2.500 bar (27249) ya no se adjuntan. En su lugar va el **certificado 26993** de INCANE, acreditación 185/LC10.133, para un manómetro analógico MEI de **campo de medida (0…250) bar**, clase 1, calibrado el 12-Dic-2025; el dato está en la hoja 2 de 4 del certificado, PDF página 14. Para el ensayo de 136,5 bar eso es **1,83 veces**, dentro de la ventana de 1,5 a 4. **Residual**: el esquema de la PDF página 9 sigue rotulando *"PRESSURE GAUGE: ASME [0-160 bares]"*, que es el manómetro rechazado; para el ensayo de 136,5 bar ese rango da 1,17 veces |
| NOTE-01 | **SIN ACCIÓN** | Era la declaración de cierre del crítico arrastrado desde el Transmittal N23, y la aceptación de un solo manómetro calibrado para el ensayo. No pedía nada |

**Veredicto: Código 1 — Approved.** La condición se cumplió: las presiones están declaradas y el certificado adjunto es único y cae en rango, de modo que qué manómetro se usó queda confirmado de hecho. El rótulo del esquema se corrige en la próxima emisión natural y se trackea en la Sección 3 del transmittal.

---

## 3. `P22-DWG-09-005-005` — Tie-In Point Layout Rev B

Cinco puntos del Código 3 del Transmittal N7, el más antiguo abierto de este grupo.

| Punto | Estado | Evidencia |
|---|---|---|
| 1 — Redibujar sobre el Piping Layout consolidado | **CERRADO** | La lámina muestra el estanque CIP, el estanque de antiscalante, la bomba CIP, el filtro de cartuchos CIP y el mezclador estático dentro de una sola huella, con el skid de dosificación de antiscalante rotulado |
| 2 — Completar la conexión DN15 de antiscalante con TAG, referencia de P&ID y estándar de brida | **PARCIAL** | La conexión DN15 dejó de ser punto de conexión y se conecta directo al mezclador estático, vía que resuelve el punto. Pero el punto 1 de la tabla, `TP-AS P11-001` ANTISCALANT de 1", **sigue con las celdas de clase y de estándar de brida en guion**, mientras los otros cuatro llevan 150 y ASME B16.5 |
| 3 — Declarar la presión de diseño en la interfaz de alimentación de salmuera | **NO LEVANTADO** | La tabla declara `TP-DA P8-001` FEED 4" 150 ASME B16.5, y **no hay columna ni nota de presión de diseño en toda la lámina**. La respuesta —*"Feed tie-in point according to the PID; 4 inch ND and 150# flange rating"*— repite la clase de brida, que es el dato que ya se tenía; lo que se pidió es la presión a la que la salmuera llega al límite de batería, para verificar que sea compatible con ANSI 150# |
| 4 — Cruzar los identificadores internos de línea contra la numeración del P&ID | **CERRADO** | La tabla encabeza la columna como `TAG (PID)` y los cinco puntos van con su TP: `TP-AS P11-001`, `TP-DA P8-001`, `TP-PE P9-001`, `TP-PE P9-002`, `TP-DA P9-003` |
| 5 — Vista de elevación con posición y cota de todas las bridas | **CERRADO** | La lámina incorpora tres vistas nuevas —*Section 1-1 Elevation View*, *Section 2-2 Elevated View* y *Section 3-3 Elevation View*— y la tabla suma la columna de cota de eje con valor para los cinco puntos: 1.680, 2.597, 2.947, 2.947 y 2.940 mm |

**Tres de cinco cerrados.** Lo que resta —la presión de diseño en la alimentación y las dos celdas de brida del punto 1— se incorpora al emitir Rev 0 sin revisión intermedia. **Veredicto: Código 2.**

---

## 4. `P22-DWG-09-005-008` — GA of SWRO System Skid Rev B

Dos notas del Código 2 del Transmittal N15.

| ID | Estado | Evidencia |
|---|---|---|
| NOTE-11 — Cuadro de equipos y válvulas | **CERRADO con residual** | El bloque de notas de las láminas 2 y 3 entrega los cuatro datos: nota 2, seis recipientes en primera etapa y cuatro en segunda; nota 3, siete elementos por recipiente, `BPV-8-1200-SP-7` en primera y `BPV-8-1800-SP-7` en segunda; nota 4, manifold en acero inoxidable súper dúplex clase 900 lb; notas 5 y 6, matriz función contra TAG remitida a la Valve List y a la Instrument List. **Residual**: la nota 6 cita la Instrument List en **Rev D** cuando la vigente es **Rev E** |
| NOTE-12 — Cuadro de presión de diseño y materiales | **CERRADO con residual** | Nota 7, presión y temperatura remitidas a la Line List; nota 8, espesor nominal por línea remitido a la especificación de cañerías; el rating del manifold queda declarado en la nota 4. **Residual**: los dos códigos citados están truncados — la nota 7 dice `P22-LI-09-009-00` cuando la Line List aprobada es `P22-LI-09-009-003`, y la nota 8 dice `P22-ET-09-006-01`, que no es un código válido de la codificación del proyecto, que usa tres dígitos de correlativo |

**Las dos notas cerraron en sustancia.** Los tres residuales están en las notas mismas que se agregaron para cerrarlas, así que pertenecen al comentario y no son hallazgo nuevo. Se corrigen al emitir Rev 0. **Veredicto: Código 2.**

---

## Recuento

| Documento | Entradas | Cerradas | Parciales | No levantadas | Disposición |
|---|---|---|---|---|---|
| Plant Control Philosophy Rev 0 | 5 | 1 | 2 | 2 | **Sin código** |
| RO Vessel Hydrostatic Test Procedure Rev 0 | 3 | 2 | 0 | 0 (1 sin acción) | **1 — Approved** |
| Tie-In Point Layout Rev B | 5 | 3 | 1 | 1 | **2 — Approved as noted** |
| GA of SWRO System Skid Rev B | 2 | 2 | 0 | 0 | **2 — Approved as noted** |
| **Total** | **15** | **8** | **3** | **3** | |

Ninguna entrada quedó sin cita. La entrada sin acción del procedimiento hidrostático era una declaración de cierre de ADASA, no una instrucción.
