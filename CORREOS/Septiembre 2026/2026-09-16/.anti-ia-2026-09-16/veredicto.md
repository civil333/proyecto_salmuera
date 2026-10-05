# Veredicto anti-ia: correo urgente a BW Water por el procedimiento FAT del módulo

Documento: `2026-09-16_Module-FAT-Procedure-Required.docx` (207 palabras de cuerpo más una tabla de nueve filas y 181 palabras; inglés, correspondencia de proyecto)
Fecha: 2026-09-16 | Modo: revisar

## Veredicto del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
Familias cargadas en detalle: universales U-01 a U-12 completos. Claude CL-01 a CL-25, con foco en CL-19/20/21 (Opus 5, modelo autor) y CL-22 a CL-25.
VERDE | 1% | Confianza: Baja (texto bajo 300 palabras)
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave:**

- **CL-24 sobre el umbral:** 2 de 5 párrafos abrían con una oración completa en negrita (40 % contra 30 %). Eran el hecho de apertura, que ya va en el asunto, y el pedido con plazo.
- **Ritmo algo largo para el registro 11.1:** mediana 20,5 y percentil 90 en 37,1, con 20 % de oraciones sobre 30 palabras, contra 18, 35 y 14,3 % del perfil. La oración de 28 palabras que unía las filas 7.2 a 7.9 con la consecuencia se podía partir sin perder nada.
- **Sin fingerprints críticos.** U-01 a U-06 en cero y barridos duros en cero.

**Fingerprints detectados:** CL-24 (borde, 1 %).
**Modelo autor:** Claude Opus 5 (autoría conocida, no sospechada).

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| **"The Factory Acceptance Test procedure for the module has never been submitted, and the test is planned for next week."** en negrita al abrir | Sin negrita, porque el hecho ya viaja en el asunto | CL-24 |
| "...are carried out against that procedure, so the FAT cannot formally open until it is approved." (28 palabras) | Partida en dos. La consecuencia queda como oración propia en negrita al cierre del párrafo: **"The FAT cannot formally open until it is approved."** | CL-24, ritmo 11.1 |
| Fila del índice del dossier: "the only procedure in the index without a document number" | "the only entry of its QA documents section without a document number". B1 y B2 son el ITP y el NDE Plan, no procedimientos, así que la versión anterior era refutable | exactitud, no fingerprint |

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Baja (texto bajo 300 palabras)
Estilo personal: Aplicado, Caso A (solo el párrafo corregido; el resto ya estaba en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1). Primera persona en el pedido ("Please submit", "I look forward", "My email"), como los correos anteriores a BW Water.
Estilometría (`estilometria.py` sobre el `.docx`, prosa sin tabla), contra el perfil 11.1:

| Rasgo | Original | Final | Perfil 11.1 |
|---|---|---|---|
| mediana de oración | 20,5 | 18,0 | 18 |
| percentil 90 | 37,1 | 37,0 | 35 |
| oraciones sobre 30 palabras | 20,0 % | 18,2 % | 14,3 % |
| oraciones bajo 8 palabras | 10,0 % | 9,1 % | sin dato propio |
| paréntesis por mil | 10,15 | 10,2 | 6,18 |
| punto y coma | 0 | 0 | 0 |
| em dash | 0 | 0 | 0 |

Las dos oraciones sobre 30 palabras son la cita contractual completa de la ET y el ITP (37), que la regla del proyecto obliga a escribir con código y sección deletreada, y la enumeración del alcance mínimo de la Section 8.1 (38). Los dos paréntesis encierran códigos de documento. Con 11 oraciones, el percentil 90 y la densidad de paréntesis no son estables, así que no se recortó contenido para calzar el perfil.

**Fingerprints detectados:** Ninguno.

- **CL-24 resuelto.** Un solo párrafo de cinco abre en negrita, el del pedido con plazo (20 %).
- **CL-25 descartado.** Dos dos puntos: uno introduce la tabla y el otro la enumeración del alcance.
- **U-09 revisado y aceptado.** *procedure* aparece 5 veces en el cuerpo porque es el objeto del correo; *section* e *inspection*, 3 cada una, dentro de nombres de documentos y del alcance citado.
- **CL-19 descartado.** El párrafo del P22-PP-09-000-001 Rev C adelanta la respuesta previsible del proveedor, y la tabla de nueve filas la pidió el usuario explícitamente ("citando toda la trazabilidad"). No hay resumen final ni anuncio de intención.
- **CL-21 descartado.** No declara verificaciones propias ni amplía el alcance. El procedimiento de conservación y embalaje, también faltante, quedó fuera a propósito.
- **U-02B descartado.** Cero punteros posicionales ("above", "previous", "below").
- **U-01, CL-22 y CL-23 descartados.** Sin *not… but*, *rather than*, aperturas escindidas ni colas *, which is*.
- **Falso positivo de hedging.** El barrido marcó *may*, que es el mes (*since May*).

### Barridos duros sobre el documento

Cero símbolo de sección en el `.py` y en el `.docx`, cero grafía británica, cero em dash y en dash, cero punto y coma en el cuerpo (los de la línea CC separan destinatarios), y días de la semana comprobados con `datetime` (jueves 3 y viernes 18 de septiembre).

### Rendimiento del análisis

Fingerprints más efectivos: CL-24 y la estilometría contra el registro 11.1.
No aplicables: U-04, U-06, U-07, U-08, CL-09, CL-11, CL-14, CL-17, CL-18 (texto corto, sin secciones ni metáforas).
Checklist A, 11 pasos aplicables de 19 (C1, C2, C4, C8, C10, C13, C14, C15, C16, C17, C18).
Consenso semiótico: 4/4 niveles coinciden en la re-evaluación.
Nota para correos futuros del mismo tipo: cuando el asunto ya lleva el hecho urgente, la negrita rinde más sobre la consecuencia y sobre el pedido que sobre la apertura.

## Segunda pasada (reordenamiento pedido por el usuario)

El usuario objetó la apertura del correo. Era *"The Factory Acceptance Test procedure for the module has never been submitted, and the test is planned for next week."* Puesta primero, hace parecer que ADASA recién se acuerda del procedimiento a días del ensayo, cuando la tabla prueba que se viene levantando por escrito desde mayo. También pidió lógica entre párrafos. Ningún fingerprint detectaba esto, porque es una corrección de registro y de orden argumental, no de marcador.

| Orden anterior | Orden nuevo |
|---|---|
| 1. Faltante y plazo, obligación y Hold | 1. Obligación de la ET Section 8.1 e historial desde mayo, con la tabla a continuación |
| 2. El Rev C del tablero no lo reemplaza | 2. Estado (*"still not been received"*), Hold de la fila 7.1 y consecuencia en negrita al cierre |
| 3. Línea puente y tabla | 3. El Rev C no cubre *"this requirement"*: excluye software y lógica, y *"Section 8.1 requires both at the FAT"* |
| 4. Pedido | 4. Pedido en negrita que retoma *"the full minimum scope of Section 8.1"* |

Se eliminó la línea puente *"The procedure has been on record as outstanding since May:"*, que absorbe el primer párrafo.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Baja (texto bajo 300 palabras)
Estilo personal: Aplicado, Caso A (reordenamiento del cuerpo en la misma voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1).

| Rasgo | Primera pasada | Segunda pasada | Perfil 11.1 |
|---|---|---|---|
| mediana de oración | 18,0 | 16,0 | 18 |
| percentil 90 | 37,0 | 32,9 | 35 |
| oraciones sobre 30 palabras | 18,2 % | 16,7 % | 14,3 % |
| oraciones bajo 8 palabras | 9,1 % | 16,7 % | sin dato propio |
| paréntesis por mil | 10,2 | 9,8 | 6,18 |
| punto y coma | 0 | 0 | 0 |
| em dash | 0 | 0 | 0 |

Las dos oraciones bajo 8 palabras son *"Section 8.1 requires both at the FAT."*, que ancla el paso al pedido, y el cierre *"I look forward to your comments."* Unir la primera a la anterior la convertiría en cola explicativa (CL-23), así que se deja. Con 12 oraciones, la mediana de 16 queda dentro del ruido.

**Fingerprints detectados:** Ninguno.

- **CL-24:** 1 de 5 párrafos abre en negrita (20 %).
- **CL-23 y U-01:** cero *", which / that"*, cero *not… but* y cero *rather than*.
- **CL-22 y U-02B:** cero aperturas escindidas y cero punteros posicionales. *"this requirement"* remite a la Section 8.1 nombrada en el párrafo anterior, no a una parte del documento.
- **CL-25:** dos dos puntos, uno introduce la tabla y el otro la enumeración del alcance.
- Barridos duros: cero símbolo de sección, cero grafía británica, cero em dash y en dash, cero *never* en el cuerpo.

---

# Veredicto anti-ia: respuesta a BW Water por el desalineamiento de los spools de los turbos

Documento: `2026-09-16_Turbocharger-Spool-Offset-Response.docx` (531 palabras de cuerpo con la lista numerada, más una tabla de diez filas y 211 palabras; inglés, correspondencia de proyecto)
Fecha: 2026-09-16 | Modo: revisar

## Veredicto del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
VERDE | 0% | Confianza: Media
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave:**

- **Sin fingerprints críticos.** U-01 a U-06 en cero: sin *not… but*, sin *rather than* y sin certeza sentenciosa. La oración en negrita del primer párrafo es un hecho verificable contra los TM N30, N36 y N39.
- **CL-19 revisado y descartado.** Cada párrafo trae un hecho o un pedido. La tabla la pidió el usuario y la lista numerada es lo que se exige para la reunión. No hay resumen final ni anuncio de intención.
- **Una corrección de exactitud, no de estilo.** El primer borrador decía *"spools already installed and pressure tested"*. Sin saber qué spools están afectados no se puede afirmar que ya estaban ensayados, así que quedó *"already installed"*.

**Fingerprints detectados:** Ninguno.
**Modelo autor:** Claude Opus 5 (autoría conocida, no sospechada).

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Media
Estilo personal: Aplicado, Caso A (redactado directo en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1). Primera persona en *"I also have no assurance"*, *"I take note"* y *"My email"*.

| Rasgo | Final | Perfil 11.1 |
|---|---|---|
| mediana de oración | 17,0 | 18 |
| percentil 90 | 26,0 | 35 |
| oraciones sobre 30 palabras | 0 % | 14,3 % |
| oraciones bajo 8 palabras | 9,5 % | sin dato propio |
| paréntesis por mil | 5,6 | 6,18 |
| punto y coma | 0 | 0 |
| em dash | 0 | 0 |

`estilometria.py` mide 357 palabras de prosa porque descarta los ítems numerados.

- **CL-24:** 1 de 14 párrafos abre en negrita, el que introduce el pedido.
- **CL-25:** tres dos puntos, que introducen la tabla y la lista.
- **CL-22, CL-23 y U-02B:** cero aperturas escindidas, cero *", which / that"* y cero punteros posicionales.
- **U-09 aceptado:** *turbocharger* y *spools* se repiten porque son el objeto del correo.
- Barridos duros: cero símbolo de sección, cero grafía británica, cero em dash y en dash, días de la semana comprobados con `datetime`, y ninguna oración que califique como aprobados los planos generales `P22-DWG-09-005-012` y `-013`, por decisión del usuario.

### Segunda pasada: párrafo de plazo y derechos (pedido del usuario)

El usuario objetó *"it is not accepted as a contractual date"*, porque puede leerse como que ADASA no quiere que despachen. El párrafo nuevo toma nota del 12 de octubre y declara que la prioridad es despachar en cuanto el módulo esté listo. Deja la palanca como *"the actions available to it under the Contract and the BAE, including those of Clause 43.1 b)"*. Los hechos de la Cláusula 27 no cambian.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Media
Estilo personal: Aplicado, Caso A (solo el párrafo reescrito)

- **Oraciones del párrafo:** 11, 24, 11, 27 y 20 palabras. La de 38 se partió en dos.
- **Documento completo:** mediana 19,0, percentil 90 de 26,0 y ninguna oración sobre 30, contra el perfil 11.1 de 18 y 35.
- **U-01:** cero *not… but*. *"does not waive any right"* es negación simple, sin contraste.
- **CL-23:** cero *", which / that"*.
- **Barridos:** cero *"not accepted"*, cero símbolo de sección, grafía británica y guiones largos.

### Tercera pasada: versión ejecutiva y directa (pedido del usuario)

De 550 a 344 palabras de cuerpo, y la tabla de 211 a 137, sin sacar ningún pedido. Se recortaron la explicación larga de los turbos (quedó en una oración y en el punto 4), la explicación de la Cláusula 27 (quedó citada junto a la 43.1 b) como acción disponible) y el detalle del Request 008.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Media
Estilo personal: Aplicado, Caso A

- **Estilometría del documento:** mediana 17,0, percentil 90 de 26,0 y ninguna oración sobre 30, contra el perfil 11.1 de 18 y 35.
- **CL-23 corregido en el recorte:** la primera versión corta unía el desfase y el retrabajo con *", which have to be cut"* en 33 palabras. Se partió en dos oraciones.
- **CL-24:** 1 de 14 párrafos abre en negrita.
- **Exactitud:** el punto 1 decía *"the affected turbocharger"*, que da por hecho que es uno solo. Quedó *"Which turbochargers and spools are affected"*.
- **Barridos:** cero *"not accepted"*, cero símbolo de sección, grafía británica y guiones largos.

---

# Veredicto anti-ia: correo conjunto a Bureau Veritas por el Request 008

Documento: `2026-09-16_BV-Request-008-Turbocharger-As-Found.docx`, movido el 16-Sep a `CORREOS/Septiembre 2026/2026-09-17/` y eliminado ese mismo día sin enviarse, por decisión del usuario. Lo reemplaza `2026-09-16_BV-Survey-Turbocharger-Offset.docx` (247 palabras de cuerpo con cuatro viñetas; inglés, correspondencia de proyecto)
Fecha: 2026-09-16 | Modo: revisar

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
VERDE | 0% | Confianza: Baja (texto bajo 300 palabras)
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)
Estilo personal: Aplicado, Caso A (redactado directo en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1).

**Fingerprints detectados:** Ninguno.

- **Estilometría:** mediana 14, percentil 90 de 27 y una sola oración sobre 30, contra el perfil 11.1 de 18 y 35. La mediana baja es propia de un correo operativo con instrucciones por día.
- **CL-24:** cero párrafos abren en negrita. La negrita va dentro de la oración, en la instrucción de cada día.
- **CL-25:** dos dos puntos, que introducen la lista del registro y la línea de adjuntos.
- **U-01, CL-22 y CL-23:** cero *not… but*, cero aperturas escindidas y cero *", which / that"*.
- **Grafía:** *pressurised* se corrigió a *pressurized* tras el primer barrido. Cero grafía británica en el documento final.
- **Exactitud:** la primera versión decía *"the connections of the two turbochargers"*, que da por hecho que los dos están desplazados. Quedó *"the turbocharger connections"*.

### Cuarta pasada: encuadre de lo emitido y captura del modelo 3D (pedido del usuario)

El usuario objetó *"Those spools were built to drawings never submitted to ADASA"*, porque deja mal a ADASA. El primer párrafo se partió en dos. El segundo dice que los planos de cañerías, incluido el Piping Layout, y el modelo 3D se emitieron y revisaron y que en ellos las conexiones de los turbos calzan, y cierra en negrita con que los planos de fabricación oficiales nunca se emitieron. Debajo va la captura del modelo 3D, y la tabla nombra el modelo 3D Rev A y Rev B junto al layout en los TM N30 y N36.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Media
Estilo personal: Aplicado, Caso A

- **Estilometría:** mediana 18,0, percentil 90 de 27,7 y una oración de 31 palabras, la del Piping Layout y el modelo, contra el perfil 11.1 de 18 y 35.
- **CL-24:** 1 de 16 párrafos abre en negrita. La negrita nueva va al cierre del párrafo.
- **U-01:** cero *not… but*. El contraste entre lo emitido y lo no emitido va en dos oraciones afirmativas, sin la antítesis retórica.
- **CL-23:** cero *", which / that"*.
- **Barridos:** cero *"never submitted to ADASA"*, cero *"annotations"*, cero símbolo de sección, grafía británica y guiones largos. Una imagen embebida.

### Quinta pasada: el turbo interetapa (pedido del usuario)

Se agrega que, por las fotos, el afectado es el turbo interetapa, y que eso agrava el caso porque trabaja a la presión más alta del módulo. La cifra se verificó contra las hojas de datos Rev 0: el interetapa tiene 84,8 bar a la salida de alimentación y el de alimentación 69,53 bar. En la Line List Rev 1 la alimentación a segunda etapa, `09-006`, tiene 90 barG de diseño y 135 barG de prueba.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Media
Estilo personal: Aplicado, Caso A

- **Estilometría:** mediana 15,5, percentil 90 de 23,5 y una oración sobre 30.
- **CL-23:** la consecuencia va en una oración propia con *"because"*, no en una cola *", which makes"*.
- **CL-25:** sin dos puntos explicativos en el párrafo nuevo. La cifra va en una oración aparte.
- **Barridos:** cero símbolo de sección, grafía británica y guiones largos. Una imagen embebida y un solo párrafo abre en negrita.

---

# Veredicto anti-ia: correo a Bureau Veritas por el levantamiento en Penang

Documento: `2026-09-16_BV-Survey-Turbocharger-Offset.docx` (377 palabras de cuerpo con cuatro ítems numerados; inglés, correspondencia de proyecto)
Fecha: 2026-09-16 | Modo: revisar

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
VERDE | 0% | Confianza: Media
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)
Estilo personal: Aplicado, Caso A (redactado directo en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1).

**Fingerprints detectados:** Ninguno.

- **Estilometría:** mediana 20,0, percentil 90 de 23,0 y ninguna oración sobre 30, contra el perfil 11.1 de 18 y 35.
- **CL-24:** 1 de 11 párrafos abre en negrita, el del pedido de levantamiento.
- **CL-25:** un solo dos puntos, que introduce la lista del levantamiento.
- **CL-19 revisado:** cada ítem es un pedido con su base en el ITP. Sin resumen final ni anuncio de intención.
- **U-01, CL-22 y CL-23:** cero *not… but*, cero aperturas escindidas y cero *", which / that"*. *"the one that runs at the highest pressure"* es aposición y no reinterpreta el dato.
- **Barridos:** cero símbolo de sección, grafía británica (*mobilizing* en grafía americana) y guiones largos, y cero oferta, tarifas o saldo de jornadas.

### Segunda pasada: versión ejecutiva en la voz de Luis (pedido del usuario)

#### Evaluación del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
VERDE | 2% | Confianza: Media
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave:**

- **CL-19 en el borde, y explica el pedido de ejecutividad.** Los cuatro ítems del levantamiento enumeraban los documentos contra los que comparar y los atributos a revisar, algo que ya traen los adjuntos. Además, informes y jornadas iban en párrafos separados y el cuerpo sumaba 377 palabras.
- **Voz institucional en lugar de la del registro 11.1.** El pedido abría con *"ADASA requests Bureau Veritas"*, en tercera persona, y el correo cerraba sin la fórmula de atento a la respuesta que usa el autor.
- **Sin fingerprints críticos.** U-01 a U-06 en cero.

**Fingerprints detectados:** CL-19 (borde, 2 %).

#### Cambios realizados

| Patrón original | Corrección | Motivo |
|---|---|---|
| *"At today's coordination meeting, BW Water informed ADASA of..."* | *"BW Water informed us today of..."* | Voz 11.1, primera persona |
| *"ADASA requests Bureau Veritas to carry out a survey... It should cover:"* | *"Starting with the visit of 18 September, I ask Bureau Veritas for a survey at the Penang workshop covering:"* | Voz 11.1; una oración en vez de dos |
| Ítem 1 con cuatro documentos de comparación y dos oraciones | Una oración: causa raíz, qué se registra antes de cortar, fila 4.2 | CL-19 |
| Ítem 2 con siete atributos de los turbos | *"including both turbochargers against their datasheets Rev 0"* | CL-19; los atributos están en las hojas de datos adjuntas |
| Informes y jornadas en dos párrafos | Un párrafo de dos oraciones | CL-19 |
| *"...goes ahead, excluding every line connected to either turbocharger"* | *"...goes ahead, excluding the lines connected to the turbochargers"* | Más directo |
| Sin cierre | *"I look forward to your confirmation."* | Cierre del registro 11.1 ("Quedo atento") |

#### Texto corregido (cuerpo)

> BW Water informed us today of an offset of about 50 mm between the turbocharger connections and their piping spools. The affected spools have to be cut, re-welded and re-tested, and ready to ship moves to 12 October. From the photographs I understand it is the interstage turbocharger, the one with the highest operating pressure in the module. The background is in my email to BW Water, attached.

> The high-pressure test of 17 September (Request 008) goes ahead, excluding the lines connected to the turbochargers.

> **Starting with the visit of 18 September, I ask Bureau Veritas for a survey at the Penang workshop covering:**

> 1. Root cause of the spool offset, with offsets, photographs and spool identification recorded before any cut (Inspection and Test Plan P22-BA-09-000-004 Rev 0, row 4.2).

> 2. Equipment against the Equipment List Rev 0, including both turbochargers against their datasheets Rev 0 (row 4.1).

> 3. Instruments against the Instrument List Rev F and the P&ID Rev 0 (rows 4.3 and 4.4).

> 4. Any other construction issue found now that all the equipment is reported at the workshop.

> Please issue the survey in one inspection report and the electrical progress (rows 6.1 to 6.3) in a **separate report**, with a Flash Report for any deviation. Please also propose the inspection days needed, for our approval before mobilizing beyond 18 September.

> Magdier, Eduardo and Lokman, please give the inspector access to the equipment, spools and records.

> From tomorrow Victor Gutierrez leads this matter for ADASA, so please send the reports to both of us.

> I look forward to your confirmation.

#### Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Baja (texto bajo 300 palabras)
Estilo personal: Aplicado, Caso B (documento completo reescrito en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1). Primera persona: *us*, *I understand*, *my email*, *I ask*, *our approval*, *I look forward*.

| Rasgo | Original | Final | Perfil 11.1 |
|---|---|---|---|
| palabras de cuerpo | 377 | 262 | sin referencia |
| mediana de oración | 20,0 | 18,0 | 18 |
| percentil 90 | 23,0 | 20,0 | 35 |
| oraciones sobre 30 palabras | 0 % | 0 % | 14,3 % |
| paréntesis por mil | 4,48 | 11,17 | 6,18 |
| punto y coma | 0 | 0 | 0 |
| em dash | 0 | 0 | 0 |

Los paréntesis son dos sobre 179 palabras de prosa: *(Request 008)* y *(rows 6.1 to 6.3)*, referencias numeradas del tipo que el perfil admite. Con 11 oraciones la densidad no es estable.

**Fingerprints detectados:** Ninguno.

- **CL-19 resuelto:** 262 palabras, cada párrafo es un hecho o un pedido.
- **CL-24:** 1 de 11 párrafos abre en negrita, el del levantamiento.
- **CL-25:** un solo dos puntos, que introduce la lista.
- **U-01, CL-22 y CL-23:** cero *not… but*, cero aperturas escindidas y cero *", which / that"*. *"the one with the highest operating pressure"* es aposición.
- **Ornamento:** cero.
- **Barridos:** cero símbolo de sección, grafía británica, guiones largos, oferta y tarifas.

#### Ajuste posterior: la oración del traspaso (pedido del usuario)

*"From tomorrow Victor Gutierrez leads this matter for ADASA, so please send the reports to both of us."* pasa a *"I will be out of the office for the next two weeks. In the meantime, Victor Gutierrez will handle communications for ADASA, so please send the reports to both of us."* El usuario objetó que la primera versión sonaba a que se estaba escondiendo. La nueva declara la ausencia de frente y en primera persona, que es el registro 11.1. Cuerpo final de 275 palabras, mediana de 17,5, percentil 90 de 20 y ninguna oración sobre 30. Sigue en VERDE: cero *", which / that"*, cero guiones largos y cero grafía británica.

#### Ajuste posterior: los antecedentes adjuntos (pedido del usuario)

La última oración del primer párrafo pasa de *"The background is in my email to BW Water, attached."* a *"I attach the background documents, including my email to BW Water and its latest weekly report."* El reporte semanal (Progress Report Week 37) ya iba en los adjuntos. Sigue en VERDE: primera persona del registro 11.1, sin *", which / that"* y sin guiones largos.

#### Ajuste posterior: agradecimiento al cierre (pedido del usuario)

El cierre pasa a *"Thank you for coordinating this. I look forward to your confirmation."* Es cortesía directa, sin fórmula inflada, dentro del registro 11.1. Sigue en VERDE.
