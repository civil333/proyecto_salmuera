# Veredicto anti-IA — Puntos de revisión para la reunión del 9-Sep-2026

Documento: `2026-09-08_Puntos-Revision-Reunion-09Sep.docx` · 566 palabras de prosa más una tabla de cuatro filas · inglés · correspondencia de proyecto.

> **Cuarta pasada, 8-Sep 16:35.** El usuario no entendió qué alertaba el párrafo de apertura. Se descartó entero y se reemplazó por un solo asunto, los planos de taller que no hemos recibido, con la exigencia de que Bureau Veritas los tenga en las tres jornadas. Entró además el desfase de juntas del `CP-SSD-DN80-09-044`.
>
> **Tercera pasada, 8-Sep 16:05.** El usuario objetó lo que el correo decía de las presiones. La revisión contra el ITP y los transmittales le dio la razón en el fondo y cambió cuatro tramos del cuerpo. Las medidas de abajo son de la versión resultante.

Modo **revisar**: el borrador se reescribió entero con el perfil de estilo cargado **antes** de redactar, no después. Es un Caso B del paso 4b, porque las dos versiones anteriores estaban en voz genérica y la reescritura alcanza a todo el documento.

## Evaluación del original (versión de las 15:22)

**AMARILLO** | 6 % | Confianza: Media. Dos fallas de voz y una de sustancia:
- **Sintaxis fuera de perfil.** Oración media de 11,4 palabras contra los 18,5 de la calibración en inglés, sin una sola oración larga y con el impersonal dominando. Ejecutivo en la sintaxis en vez de en la estructura.
- **Sin primera persona.** El perfil, sección 11.1, declara que en correspondencia el impersonal desaparece y manda la primera persona. La versión anterior no tenía ninguna.
- **U-06 en el límite.** Trece puntos numerados de corrido, funcional pero al borde de la numeración impuesta.

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| "Items 1 to 4 need an answer before the Wednesday session opens" | "Two things need your written answer ...: the shop drawing question below and the four corrections in the table" | U-02B, auto-referencia estructural: se nombra la sustancia, no el número de bloque |
| "The plan is right on two points that were open" | "The plan is right on the pressures." más las cifras detrás | U-12, auto-valoración del propio hallazgo |
| Lista de trece ítems numerados, cada uno de una a dos oraciones cortas | Punto de seguridad en prosa, tabla compacta de cuatro filas y tres rótulos de agenda con dos o tres oraciones cada uno | U-06 y CL-24: los rótulos en negrita bajan de cinco a dos |
| Tres oraciones de agenda de 55, 61 y 87 palabras en la primera pasada de esta reescritura | Partidas en dos y tres oraciones cada una | U-03 y regla 7 del perfil, que prohíbe pasar de 55 palabras sin puntuación interna |
| Ausencia de primera persona | "I need written confirmation", "I take the rest at the meeting", "our review runs seven working days" | Perfil sección 11.1 |

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=[37 de 63] | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo generó Claude Opus 5 en esta sesión]

**VERDE** | 1 % | Confianza: Media
Pre-filtro: No activado | Checklist: express (9 ítems) | Pasos evaluados: 9/9
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09).

**Fingerprints detectados:** ninguno por sobre umbral.
**Modelo:** Claude Opus 5 (autoría conocida, no sospechada).

## Estilometría contra el perfil, antes y después

| Rasgo | Perfil correspondencia (11.1) | Versión telegráfica | Versión emitida |
|---|---|---|---|
| Mediana de oración | 18 | 11 | **20,0** |
| Media | 18,5 (calibración en inglés) | 11,4 | **19,4** |
| Percentil 90 | 35 | 26 | **30** |
| Oraciones sobre 30 palabras | 14,3 % | 0 % | **6,7 %** |
| Paréntesis por mil palabras | 6,18 | 0 | **3,5** |
| Punto y coma | 0 | 0 | **0** |
| Em dash | 0 | 0 | **0** |
| Ornamento | 0 | 0 | **0** |
| Primera persona | domina | ausente | **presente (3)** |
| Staccato, tres seguidas bajo 10 palabras | no | no | **no** |

**Voz: propia.** El registro de correspondencia de proyecto está calibrado sobre 971 palabras de correo enviado, de modo que esta evaluación no cae en la advertencia de la sección 11.3.

## Desviaciones declaradas

- **CL-24, rótulo en negrita al abrir párrafo: 2 de 10 párrafos de prosa, un 20 %**, bajo el umbral de 30 %. El párrafo del Pressure Test Record Chart se escribió a propósito sin rótulo para no cruzar el umbral. Los dos que quedan son el punto de seguridad y el reconocimiento, y ambos responden a una regla del propio usuario: la memoria `feedback_correos_ejecutivos` prescribe la acción incómoda arriba y en negrita inline. No es un tic del modelo, es formato de casa.
- **CL-19, inflación de extensión: 581 palabras contra las 300 que fijé en el primer plan**, casi el doble. Creció en dos tandas y las dos por sustancia verificada, no por relleno: el hallazgo de los planos de taller agregó un párrafo de 110 palabras, y la objeción del usuario sobre las presiones agregó el párrafo que declara que están zanjadas y que la retención del circuito queda levantada. No hay resumen recapitulativo, ni sección de contexto, ni oración de anuncio de intención. Si hubiera que recortar, lo primero en salir sería un frente de la agenda, no una de estas dos.

## Verificaciones mecánicas

| Chequeo | Resultado |
|---|---|
| Signo de sección en el `.py` y en el `.docx` | 0 |
| Em dash y punto y coma | 0 y 0 |
| Antítesis "not X but Y" | 0 |
| Hedging ("it is worth noting", "please be advised") | 0 |
| Oración más larga | 36 palabras (regla del perfil: 55) |
| Afirmaciones sin prueba en el cuerpo | 0: cero menciones al PVC dentro de los carretes y cero al ANSI 150#, porque sin los planos no se sostienen |
| Peticiones cuya respuesta ya esté en un documento en Código 1 | 0, tras corregir la acción del ítem 16 |
| Párrafos vacíos al cierre | 0 |
| Metadatos Word | author y last_modified_by = Luis Rivera Gonzalez; title, subject, category y comments poblados |

## Rendimiento del análisis

Fingerprints más efectivos: U-02B y U-12, los dos que el perfil declara no negociables y que aparecieron en la apertura y en el reconocimiento; U-03, que capturó las tres oraciones de agenda cuando la reescritura las dejó en 55, 61 y 87 palabras.
Fingerprints no aplicables: el módulo de español, por el idioma; U-01, sin candidatas en un texto de peticiones.
Checklist: express — 9 pasos aplicables de 9.
Nota para evaluaciones futuras del mismo tipo: un párrafo que el lector no entiende no lo arregla ningún fingerprint, porque el defecto no es de superficie sino de orden. El de apertura enumeraba historial documental, hallazgos técnicos y una petición, y el lector tenía que armar solo la conclusión. Un asunto por párrafo y una petición por asunto. Y pedir "más ejecutivo" y responder acortando la oración es el otro error a no repetir. Y el orden de los bloques es sustantivo, no cosmético: abrir con una tabla de discrepancias hace leer como abierto algo que está cerrado, de modo que el reconocimiento va delante de la tabla y no detrás. Lo ejecutivo es la estructura, es decir la acción arriba, la tabla para lo enumerable y un rótulo por frente; la sintaxis se queda en la banda del perfil. La versión de 11 palabras por oración pasó todos los fingerprints y aun así no era su voz.
