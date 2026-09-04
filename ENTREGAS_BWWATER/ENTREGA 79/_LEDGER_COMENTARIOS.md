---
titulo: ENTREGA 79 — libro mayor de comentarios y su cierre
codigo: submittal 25007-0079
fecha: 2026-08-17
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 79 (submittal `25007-0079`) — Control Philosophy Rev 1

**Recibida el lunes 17-Ago-2026.** Un documento, `P22-BT-09-009-001` Rev 1, emitido para aprobación (IFA), 59 páginas. El Submittal Form pide respuesta el jueves 20-Ago; el plazo de ADASA son siete días hábiles desde la recepción per la Cláusula 37.2 de la BAE, es decir el **miércoles 26-Ago-2026**.

Rev 0 del 28-Jul, Rev 1 del 11-Ago, sometida el 17: seis días entre la fecha del cajetín y el envío.

## Alcance de esta revisión

**Solo los cuatro puntos que el TM N31 dejó abiertos.** El TM N31 devolvió la Rev 0 sin código de respuesta, porque estaba emitida para construcción, y enumeró cuatro puntos "for closure at the next issue of this document". Esta Rev 1 es ese next issue, así que se revisa contra esos cuatro y nada más. No se hace lectura fresca de las 59 páginas ni se abren frentes nuevos: hacerlo sería exigir de más, que es el modo de falla que el triaje del TM N32 ya identificó.

La Rev 1 llega para aprobación, de modo que a diferencia de la Rev 0 **sí lleva código de respuesta**: reingresó al ciclo por decisión del propio proveedor.

Cada punto se verifica **contra el cuerpo del documento y contra la fuente aprobada, nunca contra la columna de respuesta de la hoja de comentarios**. La hoja declara los cuatro alineados al 100%.

---

## Punto 1 — mapeo de sensores de temperatura: cierra la mitad y la otra mitad queda mal

### Lo que dice la fuente aprobada

La **Instrument List Rev E** (`P22-LI-09-008-003`, entregada en la E46) declara cuatro sensores de temperatura, dos por máquina, y el proveedor de cada uno confirma que son máquinas distintas:

| Tag | Descripción | Proveedor |
|---|---|---|
| TE-09-001 | RO HP Pump **Winding** Temperature Sensor | Fedco |
| TE-09-002 | RO HP Pump **Bearing** Temperature Sensor | Fedco |
| TE-09-003 | **CIP Pump** Winding Temperature Sensor | Grundfos |
| TE-09-004 | **CIP Pump** Bearing Temperature Sensor | Grundfos |

La **Alarm and Interlock List Rev C** lo confirma en su propia hoja de comentarios, donde BW Water declara la corrección que ADASA le pidió en el TM N20: *"Winding/bearing temperature tags revised to follow instrument list rev.E as below"*, y transcribe las cuatro asignaciones idénticas a la tabla de arriba.

**No hay cuatro RTD en la bomba de alta.** Hay dos por máquina, de proveedores distintos, porque son los RTD embebidos en cada motor.

### Lo que hizo la Rev 1

**La sección de la bomba CIP cerró.** La subsección 3.4.2, ítems 13 y 14, ahora lee `CIP HP Pump Winding Temperature Sensor (PT100) → TE-09-003` y `CIP Pump Bearing Temperature Sensor (PT100) → TE-09-004`, que es lo que piden las dos listas aprobadas. Es exactamente lo que el TM N31 pidió corregir.

**La sección de la bomba de alta quedó mal, y es la que ADASA declaró correcta.** La subsección 3.2.2, `HIGH-PRESSURE PUMPING SYSTEM INSTRUMENT`, páginas 38 y 39 del documento, lee:

- `RO HP Pump Bearing Temperature Sensor (PT100) → TE-09-002/004`
- `RO HP Pump Winding Temperature Sensor (PT100) → TE-09-001/003`

**TE-09-003 y TE-09-004 son los dos RTD de la bomba CIP.** La tabla de la bomba de alta se los atribuye como si esa máquina tuviera cuatro sensores. El documento asigna los mismos dos tags a dos máquinas distintas en dos secciones distintas.

### El problema de encuadre, que hay que resolver antes de redactar

**El TM N31 declaró esa página correcta.** Su punto 1 dice literal: *"Page 36 now reads winding TE-09-001 and TE-09-003 and bearing TE-09-002 and TE-09-004, which is correct."* ADASA leyó `001/003` como los dos winding de la bomba de alta y no lo cruzó contra la Instrument List, que asigna el 003 a la bomba CIP.

De modo que BW Water hizo **exactamente lo que ADASA le pidió**: corrigió la sección de la CIP y dejó la de la bomba de alta como ADASA la había aprobado. Imputarle una falta acá sería doble error: la regla anti-invención de la Sección 6.2 obliga a verificar qué se pidió realmente antes de codificar un incumplimiento, y lo que se pidió fue lo que se hizo.

**Encuadre correcto, decidido por el usuario el 17-Ago: rectificación explícita.** El transmittal declara que ADASA rectifica su lectura del TM N31 y fija el mapeo vinculante de las cuatro filas citando la Instrument List Rev E y la Alarm and Interlock List Rev C. Se redacta como corrección de ADASA, sin verbo de incumplimiento contra el proveedor. Poner el error propio por escrito cierra de antemano la réplica de que BW Water hizo lo aprobado, que de otro modo cuesta un ciclo completo sobre una asignación de sensor de protección que ya lleva tres vueltas.

**Severidad:** es asignación de sensor de protección sobre un motor de 93 kW, con setpoints de disparo distintos por elemento (140 °C en devanado contra 95 °C en rodamiento, per la Alarm and Interlock List Rev C). Con los tags cruzados el enclavamiento actúa sobre el elemento equivocado. Es el mismo argumento con que el TM N31 lo puso primero en su resumen ejecutivo.

**Alcance cruzado:** el TM N31 pidió al **HMI Display Screenshot Rev B** reconciliar seis tags porque los de la bomba de alta estaban duplicados. Ese pedido se hizo sobre la misma lectura equivocada, así que hay que revisar qué se le exigió al HMI antes de darlo por cerrado. Va a la Sección de pendientes del transmittal, no como comentario nuevo a este documento.

**Estado: NO CERRADO.**

---

## Punto 2 — pares de alarma y disparo de vibración: CERRADO

Contrastado valor por valor contra la **Alarm and Interlock List Rev C**, que es la fuente que el TM N31 citó:

| Máquina | Documento | Alarma alta | Disparo alto-alto | Lista aprobada | Estado |
|---|---|---|---|---|---|
| Bomba de alta | `VT-09-001`, pág. 42 | 7,0 mm/s RMS | 10 mm/s RMS | `VIT-09-001.AH` = 7,0 · `VIT-09-001.AHH` = 10,0 | **coincide** |
| Turbocharger de alimentación | `VT-09-002`, pág. 41 | 4,5 mm/s RMS | 6,0 mm/s RMS | 4,5 y 6,0 | **coincide** |
| Turbocharger interetapa | `VT-09-003`, pág. 46 | 4,5 mm/s RMS | 6,0 mm/s RMS | 4,5 y 6,0 | **coincide** |

El 7,1 mm/s que el TM N31 objetó desapareció del documento. Las dos coincidencias que quedan de "7.1" en el texto son la numeración de la sección 1.7.1.

**Dos residuos, los dos menores y ninguno de fondo:**

- Los tres bloques cierran con *"(Reference: ISO 10816-3, typical Class III machinery baseline; **subject to vendor confirmation**)"*. Los seis valores ya están fijados por un documento aprobado en Código 1, así que la salvedad sobra y conviene retirarla al emitir: un valor de disparo no queda sujeto a confirmación cuando la lista que lo gobierna ya está aprobada.
- El documento usa `VT-09-001` y la Alarm and Interlock List Rev C usa `VIT-09-001` para el mismo instrumento. **La discrepancia está entre las dos listas del proveedor**, no la creó este documento: la Instrument List Rev E también lo llama `VT-09-001`. No se le imputa a la Control Philosophy; si se levanta, es como punto cruzado sobre la Alarm and Interlock List.

---

## Punto 3 — clase de aislación que sostiene el disparo de 140 °C: CERRADO

La Rev 1 declara: *"Motor is specified with Class F insulation (rated up to 155 °C) operating with Class B temperature rise (80 K max rise). Therefore, winding alarm is set to 120 °C and winding trip is set to 140 °C."*

Verificado contra el datasheet vigente: **`P22-ET-09-009-002` Rev D**, entregado en la E20 y aprobado en Código 2 en el TM N11, línea 50: `Insulation Class — F`. La afirmación del documento coincide con el datasheet aprobado y el disparo de 140 °C queda soportado, porque el límite de la Clase F es 155 °C.

> **Cuidado con el datasheet equivocado.** El `P22-ITEM-09-009-002-A` de la ENTREGA 1 declara `Thermal Insulation Class: Class B` y **está superado**: es de diciembre de 2025, tiene otro prefijo de código y la revisión vigente es la D. Leer ese habría producido un hallazgo falso justo en el punto que el TM N28 abrió, y que la Rev 1 resolvió bien.

El esquema F/B que declara el documento es además práctica estándar y conservadora: aislación Clase F con elevación limitada a Clase B.

---

## Punto 4 — documentos hijos fijados por código y revisión: PARCIAL

El TM N31 pidió fijarlos **por código y revisión**. La Rev 1 fijó el código y no la revisión.

**Lo que cerró.** La tabla de referencias de la página 5 ya no dice `SEPARATE DOCUMENT`: cita `P22-LI-09-008-017` para el Controls & Sequence Chart y `P22-LI-09-008-015` para el Alarm and Control Setpoint List.

**Lo que no cerró:**

1. **Ninguna de las dos filas trae revisión.** Los documentos existen emitidos como Rev A y Rev C respectivamente, y sin la revisión la referencia no fija qué versión gobierna, que es la mitad de lo que se pidió.
2. **Tres referencias del cuerpo siguen sin fijar.** Las páginas de protección de la bomba de alta, del turbocharger y de la CIP cierran con *"Detailed setpoints are stated in a separate document (alarm and setpoint list)"* y variantes, sin código.
3. **Dos códigos de la misma tabla están mal formados.** Declara `P22-DWG-09-009-0001` para el PFD y `P22-CD-09-004-0001` para el Control System Architecture, con correlativo de cuatro dígitos, que no existe en el sistema de codificación del proyecto (tres dígitos, 001 a 999).

> **El código del PFD circula en tres formas al mismo tiempo.** El aprobado y el del Master Register es `P22-DWG-09-009-001`; el Rev 0 que llegó hoy en el submittal 25007-0078 se identifica a sí mismo como `P22-DWG-09-009-01`; y esta tabla de referencias dice `P22-DWG-09-009-0001`. Tres variantes del mismo documento en dos submittals del mismo día.

---

## Disposición propuesta

| Documento | Rev | Código | Motivo en una línea |
|---|---|---|---|
| Control Philosophy `P22-BT-09-009-001` | 1 | **2** | Dos de los cuatro puntos cierran completos y uno cierra a medias; el mapeo de la bomba de alta se corrige contra las dos listas aprobadas, todo incorporable en la emisión siguiente sin revisión intermedia |

**Por qué Código 2 y no 3.** Lo que hay que corregir es alinear tablas y referencias con documentos aprobados, y la regla del proyecto es que alinear a otro documento es Código 2; el 3 se reserva para cuando el contenido propio está mal de raíz. El contenido de control de este documento no lo está: la lógica, los setpoints de vibración y el criterio de temperatura de devanado quedaron correctos y verificados contra las fuentes aprobadas. Pesa además que en el punto abierto **BW Water hizo lo que ADASA le pidió**, y lo que falla es la instrucción de ADASA, no la ejecución del proveedor.

---

## Triaje: por qué cada punto queda dentro o fuera

### ADASA no fue clara, y en un caso estuvo equivocada

| Punto | Qué se pidió | Qué contestó | Decisión |
|---|---|---|---|
| Mapeo de sensores | Corregir la sección de la CIP para alinearla con la página 36, la Instrument List Rev E y la Alarm and Interlock List Rev C | Corrigió la sección de la CIP exactamente así | **Se mantiene el punto, con encuadre de rectificación propia.** ADASA declaró correcta una página que no lo era; el pedido se reformula declarando el mapeo vinculante de las cuatro filas |
| Documentos hijos | Fijarlos "by code and revision" | Fijó el código, no la revisión | **Se mantiene.** La petición nombraba las dos cosas |

### ADASA estaría exigiendo más de lo que pidió

| Punto | Situación | Decisión |
|---|---|---|
| `VT-09-001` contra `VIT-09-001` | Las dos listas aprobadas del proveedor se contradicen entre sí en la forma del tag; este documento sigue a la Instrument List | **Se saca de este documento.** Si se levanta, va contra la Alarm and Interlock List |
| Numeración de ítems de las tablas de instrumentos | Hay dos ítems 8 y dos ítems 13 en la tabla de la bomba de alta | **Se saca.** Defecto de maquetación, fuera de los cuatro puntos, y no induce a error de operación |
| Lectura fresca de las 59 páginas | El alcance lo fijó el TM N31 en cuatro puntos | **No se hace.** Abrir frentes nuevos sobre un documento cuya revisión responde a un alcance acotado es exigir de más |
| Nombre del archivo `Control Narrative_r1` | La portada, el Submittal Form y el Master Register dicen `Control Philosophy` | **Se saca del transmittal.** Es el nombre del archivo, no el documento |

### Lo que este triaje puso sobre la mesa y no estaba en la entrega

Que el pedido de reconciliar seis tags que el TM N31 hizo al **HMI Display Screenshot Rev B** se apoyó en la misma lectura equivocada del mapeo de la bomba de alta. Hay que revisar qué se le exigió al HMI antes de darlo por cerrado, y no es un comentario a este documento.

---

## Re-alcance del 17-Ago-2026 — lo de abajo supersede la disposición de arriba

**Criterio del usuario:** *"un documento en Rev 1 no puede tener más comentarios... de partida esto se emite porque habíamos hecho un comentario en la Rev 0, indicando que no se había levantado de manera correcta un comentario, no puede haber nuevos."* Aplicado, la disposición cambia de **Código 2 a Código 1** y el punto 1 sale del transmittal.

### Disposición final: **Código 1 — Approved**

Los cuatro puntos del TM N31 se declaran cerrados, cada uno verificado contra el documento que gobierna y no contra la hoja de comentarios:

| Punto | Estado final | Evidencia |
|---|---|---|
| 1. Mapeo de sensores de la bomba CIP | **CERRADO** | La subsección 3.4.2 lee TE-09-003 devanado y TE-09-004 rodamiento, que es lo que piden la Instrument List Rev E y la Alarm and Interlock List Rev C |
| 2. Pares de vibración | **CERRADO** | 7,0 y 10 mm/s en la bomba de alta y 4,5 y 6,0 en los dos turbochargers, idénticos a la Alarm and Interlock List Rev C |
| 3. Clase de aislación | **CERRADO** | Clase F con elevación Clase B contra el `Insulation Class — F` del datasheet vigente `P22-ET-09-009-002` Rev D |
| 4. Documentos hijos | **CERRADO**, con aseo | La tabla de referencias los fija por código. Agregar la revisión (Rev A y Rev C) queda como aseo documental para la emisión natural siguiente y no retiene el documento |

### El mapeo de la bomba de alta sale del transmittal

El hallazgo **se mantiene íntegro y verificado** en la sección de arriba: la tabla de instrumentos de la sección 3.2.2 atribuye a la bomba de alta los dos RTD de la bomba CIP, contra las dos listas aprobadas. Lo que cambia es el vehículo, no el hecho.

**Por qué sale:** el punto 1 del TM N31 declaró correcta esa página. Objetarla ahora es comentario nuevo sobre una Rev 1, y eso es exactamente lo que el criterio prohíbe. El proveedor hizo lo que se le pidió.

**Dónde vive ahora:** compromiso **`INT-12`** del registro, interno de ADASA. El vehículo para declarar el mapeo sin abrir un instrumento nuevo es el pedido de reconciliar seis tags que el TM N31 dejó abierto al **HMI Display Screenshot Rev B**: al cerrar ese ciclo hay que declarar la asignación de todas formas, y ahí es donde corresponde.

**Lo que hay que tener presente al hacerlo:** es asignación de sensor de protección sobre un motor de 93 kW, con disparos distintos por elemento, 140 °C en devanado contra 95 en rodamiento. El error de lectura es de ADASA y el encuadre, cuando se declare, es de corrección propia.

### También se retiran

Las tres referencias del cuerpo que siguen diciendo "separate document" sin código, los dos códigos mal formados de la tabla de referencias (`P22-DWG-09-009-0001` y `P22-CD-09-004-0001`) y el calificativo *"subject to vendor confirmation"* de los tres bloques de vibración. Los tres son comentarios nuevos: el punto 4 del TM N31 se refería a la tabla de referencias de la página 5, y esa tabla se corrigió. Quedan registrados acá para la emisión natural siguiente del documento.

**Consecuencia: sin PDF anotado.** El script y su `CC_ADASA` quedan en `REVISIONES/TRANSMITTALES/P22-TM-09-000-033-0/_analisis_no_anotado/` como traza interna.
