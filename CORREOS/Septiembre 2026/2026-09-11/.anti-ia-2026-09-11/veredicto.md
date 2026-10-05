# Veredicto anti-ia — Respuesta a BW Water sobre el paquete de izaje

Documento: `2026-09-11_Lifting-Package-Reply.docx` (618 palabras de cuerpo, inglés, correspondencia de proyecto)
Fecha: 2026-09-11 | Modo: revisar

## Veredicto del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Fable 5.1 en esta sesión]
Familias cargadas en detalle: universales U-01 a U-12 completos; Claude CL-01 a CL-25 completos, con foco en CL-19/20/21 (Opus 5) y CL-22/23/24/25 (Fable 5.1).
VERDE | 4% | Confianza: Alta
Pre-filtro: Activado (Q3 vocabulario técnico normalizado) | Checklist: A | Pasos evaluados: 19/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave, ninguno crítico y todos de voz:**

- **Dos aperturas escindidas (CL-22)**, 3,4 por mil contra el umbral de 2: *"What remains is the check you say the criteria serve"* y *"What the forwarder does with the container… is the forwarder's matter"*. El sujeto se enunciaba después de anunciarlo.
- **Cinco punto y coma**, donde el registro de correspondencia del perfil (sección 11.1) mide cero. Los cinco unían dos oraciones completas: *"against your design; it cannot replace it"*, *"reports reactions at nodes; it does not check"*, *"designed for it; if it is the 30-degree lift"*, *"once the design was finished; it was issued"*, *"covered by his review; please confirm that scope"*.
- **Ritmo largo (C2, alerta):** mediana de oración 25 contra 18, percentil 90 en 36,6 contra 35, y el 40 % de las oraciones sobre 30 palabras contra 14,3 % del registro. Oración más larga de 43 palabras, sobre el umbral de alerta de 40 y bajo el crítico de 50.
- **Paréntesis en 1,71 por mil** contra 6,18 del perfil: un solo paréntesis, el código de la ET.
- Tres dos puntos explicativos (CL-25, 5 por mil, bajo el umbral de 10) que sustituían al punto.

**Fingerprints detectados en el original:** CL-22 (contextual, 1 %); U-03 en alerta sin activarse; C2 +3 %.
**Modelo autor:** Claude Fable 5.1 (autoría conocida, no sospechada).
**Chequeo de voz:** genérica en cuatro de seis rasgos (mediana, oraciones largas, punto y coma, paréntesis). Corresponde el Caso B, estilización del documento completo.

## Cambios realizados

| Patrón original | Corrección | Fingerprint / rasgo |
|---|---|---|
| *"What remains is the check you say the criteria serve, the lift points and the members at the lift point."* | *"The check you say the criteria serve, the lift points and the members at the lift point, is still missing."* | CL-22 |
| *"What the forwarder does with the container between factory, port and vessel is the forwarder's matter."* | *"The forwarder's handling of the container between factory, port and vessel is the forwarder's matter."* | CL-22 |
| Cinco uniones con punto y coma | Punto y oración nueva en las cinco | punto y coma = 0 |
| *"lists the lifting calculation, the lifting drawing with weights, and the yoke design and drawing inside the erection manual, for ADASA's approval"* (43 palabras) | Dos oraciones: *"lists three deliverables inside the erection manual, for ADASA's approval. They are…"* | U-03 alerta, C2 |
| *"leaves the yoke itself out: ADASA builds it"*, *"settles the route: the module lifts"*, *"The load is eccentric: the center of gravity"* | Punto y oración nueva | CL-25 |
| *"Rev 0 models the lift globally"* | *"The Rev 0 report (P22-CD-09-005-001) models the lift globally"* | densidad de paréntesis, y el documento queda citado por código |
| *"the center of gravity sits 5,486 mm from one end and 6,514 from the other"* | *"sits off center along the module (5,486 mm from one end, 6,514 from the other)"* | densidad de paréntesis |
| *"at the factor of safety of 2.0"* | *"at the factor of safety (FS) of 2.0"* | densidad de paréntesis; la sigla es la del criterio del proveedor |

Sin cambios de contenido: mismas cifras, mismas citas, mismos siete asuntos y misma fecha del 15 de septiembre.

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Alta
Estilo personal: Aplicado — Caso B (documento completo)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1), primera persona como en los tres correos anteriores de esta cadena.

### Estilometría contra el registro 11.1 y el par de control

| Rasgo | Original | **Final** | 10-Sep enviado | N39 enviado | Perfil 11.1 |
|---|---|---|---|---|---|
| palabras de prosa | 586 | **602** | 618 | 404 | — |
| mediana de oración | 25,0 | **16,0** | 17,5 | 16,0 | 18 |
| percentil 90 | 36,6 | **28,0** | 35,9 | 28,8 | 35 |
| oraciones sobre 30 palabras | 40,0 % | **5,4 %** | — | — | 14,3 % |
| oración más larga | 43 | **33** | 44 | 36 | — |
| punto y coma | **5** | **0** | 0 | 0 | 0 |
| paréntesis /mil | **1,71** | **6,64** | 8,09 | 7,43 | 6,18 |
| em dash | 0 | **0** | 0 | 1 | 0 |
| dos puntos en prosa | 3 | **0** | — | — | — |
| comas por oración | 1,48 | **0,92** | 1,37 | — | — |

Los cuatro rasgos que estaban fuera de banda entran, y el ritmo queda algo más corto que el perfil (mediana 16 contra 18) por partir las cinco uniones de punto y coma. Es el mismo valor del correo del N39 enviado y no se alarga artificialmente.

### Barridos duros sobre el documento final

Cero símbolo de sección, cero castellano en el cuerpo, cero mención del asesor interno, cero frases-firma, cero hedging, cero grafía británica (*centre, modelled, metre, analyse*), cero *endorse / Chilean / registered*, cero *"previous email"* (por decisión del usuario no se menciona el correo previo que BW Water cita), cero antítesis *not… but*. Las secciones de la ET van con código una vez y *"Section N - Nombre"* con guion normal, no em dash.

### Una decisión declarada

El párrafo 5 repite en una oración las cuatro piezas pedidas el 10 de septiembre. Roza CL-19 (recapitulación), pero el usuario pidió mantenerlas y la oración agrega dos cosas nuevas: la pieza del punto de izaje pasa a la ruta declarada y el compromiso del 24 de junio queda atado al diseño ya emitido. No es relleno.

### Rendimiento del análisis

Fingerprints más efectivos: CL-22, que atrapó las dos aperturas escindidas que el barrido de universales no ve, y los rasgos medidos del registro 11.1 (punto y coma, paréntesis, mediana), que fueron los que de verdad rindieron.
No aplicables: U-01, U-04, U-06, U-07, U-12, CL-17, CL-18, CL-20, CL-21, CL-24.
Checklist A, 19 pasos aplicables de 19.
Consenso semiótico: 4/4 niveles coinciden en la versión final.
Nota para correos futuros del mismo tipo: al responder punto por punto a un correo del proveedor, la voz tiende al punto y coma para pegar la réplica al dato (*"reports reactions at nodes; it does not check"*). El perfil mide cero: partir en dos oraciones antes de medir.

## Segunda pasada: versión ejecutiva por respuesta

El usuario pidió el correo "más ejecutivo y resumido" y que mencionara las respuestas de BW Water. Se reestructuró en un párrafo de encuadre (quién iza y las tres secciones de la ET), **tres viñetas con lead en negrita, una por cada respuesta del proveedor** (*Padeye*, *Yoke*, *Forwarder and rigging plan*), y un cierre con la fecha, el compromiso del 24 de junio y las dos anclas de la ET. Baja de **618 a 498 palabras de cuerpo, un 19 %**, sin sacar ningún argumento ni cifra: cada viñeta abre con lo que BW Water dijo y responde en tres o cuatro oraciones.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Alta
Estilo personal: Aplicado — Caso B (documento completo, redactado directamente en la voz del registro 11.1)

| Rasgo | Caso B anterior | **Final ejecutivo** | 10-Sep enviado | Perfil 11.1 |
|---|---|---|---|---|
| palabras de prosa | 602 | **481** | 618 | — |
| mediana de oración | 16,0 | **18,0** | 17,5 | 18 |
| percentil 90 | 28,0 | **31,4** | 35,9 | 35 |
| oraciones sobre 30 palabras | 5,4 % | **13,8 %** | — | 14,3 % |
| oración más larga | 33 | **36** | 44 | — |
| punto y coma | 0 | **0** | 0 | 0 |
| paréntesis /mil | 6,64 | **6,24** | 8,09 | 6,18 |
| em dash | 0 | **0** | 0 | 0 |
| dos puntos en prosa | 0 | **1** (introduce la lista) | — | — |
| comas por oración | 0,92 | **0,90** | 1,37 | — |

**Es el calce más exacto de toda la serie**: mediana 18 contra 18, oraciones largas 13,8 % contra 14,3 % y paréntesis 6,24 contra 6,18. Las viñetas con lead en negrita son el patrón del correo del 10-Sep y de los correos de notificación de transmittal del proyecto, no CL-24: el lead es un rótulo de una o dos palabras que nombra la respuesta que se contesta, no una oración completa resaltada. Barridos duros repetidos sobre el documento final, todos en cero (símbolo de sección, grafía británica, *endorse / Chilean / registered*, *previous email*, antítesis, apertura escindida, cola de relativo, punto y coma, em dash).

## Tercera pasada: la fecha como fecha última

El usuario pidió declarar que la fecha se fija para que BW Water pueda cumplirla y que el 15 de septiembre es la última, sin margen. El cierre pasa de *"I need the package on Tuesday 15 September, the day…"* a *"I set the date so that you can meet it. Tuesday 15 September is the day the four days committed for the professional end. It is the latest date for the package, with the lifting covered by his review, and it cannot slip past that day."* Tres oraciones cortas en lugar de una de 28 palabras, sin punto y coma ni dos puntos. Cuerpo en 519 palabras. La mediana de oración baja de 18 a 14 por las tres oraciones nuevas del cierre, dentro del par de control (el N38 enviado mide 13 y el N39, 16); percentil 90 en 31, oraciones sobre 30 palabras 12,9 %, paréntesis 5,98 por mil, cero punto y coma, cero em dash. Barridos duros repetidos en cero. VERDE se mantiene.

## Cuarta pasada: las fuentes del cierre, nombradas primero

El usuario no entendió el cierre porque las tres frases finales daban el dato antes que su fuente. Se separaron en un párrafo propio y cada oración abre con el documento del que sale: la hoja de comentarios del 24 de junio y el Informe de Cálculo Rev 0 (23 de julio), la Technical Specification Section 7 página 30 (no liberar para transporte sin aprobación) y la Technical Specification Section 8.1 (puntos de izaje en la verificación dimensional del FAT). La primera oración quedó en 42 palabras y se partió en dos. Cuerpo final en 544 palabras, mediana de oración 18, cero punto y coma, cero em dash. Barridos en cero. VERDE se mantiene.

## Quinta pasada: la viñeta del forwarder, sobre el módulo contenerizado

El usuario objetó que la viñeta hablara de "port and vessel". Se reescribió sobre el objeto real: el forwarder transporta el módulo de planta contenerizado desde la fábrica hasta Taltal y su manejo en tránsito es asunto suyo; posar el módulo en su fundación es el izaje en sitio, que es de ADASA, y el method statement del rigger elige grúa, eslingas y grilletes para ese izaje contra el diseño de BW Water. Cuerpo en 564 palabras. Barridos en cero. VERDE se mantiene.
