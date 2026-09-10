---
titulo: Paquete de izaje del módulo y alcance de la revisión estructural
fecha: 2026-09-10
estado: ENVIADO
destinatario: Eduardo Yamauchi (BW Water)
cadena: transmittals
type: correo
project: salmuera-taltal
---

# Correo — El paquete de izaje y el alcance de la revisión estructural

> **ENVIADO el jueves 10 de septiembre de 2026.** Hora pendiente de registrar desde el respaldo.

**Archivo:** `2026-09-10_Lifting-Package-and-PE-Scope.docx` · **Script:** `crear_correo_izaje_pe.py`
**Sin adjuntos.** Responde en Reply-To a la cadena del Transmittal N39, que salió ayer.
**Plazo pedido:** ninguno impuesto. Se pide en la misma fecha que BW Water comprometió para la entrega del profesional, y se le pide confirmar cuál es.

## Por qué sale hoy y no la semana entrante

La minuta del 09-09-26, Agenda Item 5, registra: *"Thomas documentation received; PO placement today; expedite vendor registration and PO due to urgency"*, con un compromiso de cuatro días. **El trabajo del profesional está abierto ahora.** El izaje y el sismo viven en el mismo informe y en el mismo modelo STAAD, de modo que ampliar el alcance mientras el trabajo corre no agrega carga: la ordena. Si el correo llega después, la revisión hay que pagarla dos veces.

## Resumen del cuerpo

Siete párrafos y cuatro viñetas, **618 palabras**, **primera persona**, sin tablas y sin adjunto.

1. **La oportunidad, no el reproche.** La orden se colocó ayer con cuatro días. Antes de que cierre, el alcance debe cubrir el izaje. Se pide confirmar la fecha del profesional, porque el paquete de izaje se pide para esa misma fecha.
2. **Lo que ya está, dicho primero.** Las dos condiciones de izaje modeladas en STAAD, los factores 1,35 D y 2,0 D de API RP 2A-WSD, el centro de gravedad con tolerancia de 300 mm y la tensión máxima de eslinga de 130 kN. Reconocerlo es lo que hace creíble el resto.
3. **La primera brecha: la contradicción propia del proveedor, y ahora con la disyuntiva que la completa.** Su Criterio de Diseño exige diseñar el padeye con factor de seguridad 2,0 y carga lateral fuera de plano del 5 %, con la cita literal, y el índice del informe de cálculo salta de *Bolt Design at the Base* a los anexos sin ninguna sección de padeye. 🔴 **Y el cálculo no iza desde padeyes en absoluto: iza desde los esquineros ISO del contenedor.** Una oreja soldada y un esquinero ISO son **dos rutas distintas y excluyentes**, y el informe no dice cuál se construye.
4. 🔴 **La segunda, y es la que el usuario pidió dejar clara: el yugo no es un accesorio que se elija después, es una hipótesis que el cálculo ya hizo.** Las eslingas se modelaron uniendo los puntos de izaje a la disposición de ganchos, y las cuatro tensiones que salen **no son iguales**: 129,2 / 125,3 / 90,5 / 88,5 kN. Esa diferencia viene de un **centro de gravedad descentrado a lo largo del módulo, 5.486 mm de un lado y 6.514 del otro**. Un yugo con otra geometría da otras tensiones y el análisis deja de aplicarle. El correo cierra dando la salida: o el yugo se diseña contra la disposición que el modelo asumió, **o el modelo se rehace contra el yugo que se fabrique**.
5. **Las cuatro piezas, nombradas y separadas.** El plano de izaje con los puntos identificados, acotados y con su capacidad, más cuál usa cada condición, porque **hoy solo existen como números de nodo y como una figura sin una sola cota**; el diseño del yugo consistente con esa disposición y quién lo suministra; 🔴 **el diseño del punto de izaje por la ruta que elijan** —o el padeye con FS 2,0 y el 5 % lateral, **o, si la ruta son los esquineros ISO, la constancia escrita de que toman las reacciones calculadas sin refuerzo y la base sobre la que lo afirman**—; y la memoria de cálculo de izaje como documento propio, con el peso en kilogramos.
6. **Por qué tiene fecha propia.** ADASA iza el módulo: la Sección 9 pone el montaje en sitio y las grúas de su lado. No se contrata una grúa sin peso de izaje, centro de gravedad y diseño del yugo. Hoy hay tres pesos que no concuerdan y ninguno es el de izaje. Y la Sección 8.1 hace de los puntos de izaje materia de verificación dimensional en el FAT, que abre en días.
7. **El marco, sin imponer nada.** Los siete días hábiles de comentarios de la Sección 7 y la prohibición de liberar los equipos para transporte sin la aprobación de ADASA.

Cierra con la reserva genérica de derechos.

## Verificación de fuentes

Todas las citas se verificaron sobre la fuente primaria, y **las dos decisivas por render**, porque los PDF no devuelven texto.

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| Los tres entregables de izaje | ET `P22-ET-09-000-001-0`, Sección 7, pág. 29, dentro del Manual de Montaje | Sí, cita literal sobre `BASES TECNICAS/md/` |
| *"For the design of the padeye, a factor of safety, FS, of 2.0..."* | Criterio de Diseño `P22-CD-09-005-003` Rev 0, sección F, pág. 10 de 10 | **Sí, por render.** El PDF da 605 caracteres en 11 páginas: es imagen |
| El informe de cálculo no trae diseño de padeye | Índice del `P22-CD-09-005-001` Rev 0 | **Sí, por render del índice.** Salta de *Bolt Design at the Base* a los anexos; no hay sección de padeye |
| Las dos condiciones de izaje, factores, CG y 130 kN | Mismo informe, Anexo C y cuerpo | Sí |
| Las cuatro tensiones de eslinga desiguales, 129,2 / 125,3 / 90,5 / 88,5 kN | Mismo informe, Figura 15 y su tabla, pág. 18 de 548 | **Sí, por render** |
| El centro de gravedad descentrado, 5.486 contra 6.514 mm | Mismo informe, Figura 14, pág. 17 de 548 | **Sí, por render.** Las cotas están solo en la figura, sin tabla que las etiquete |
| Los puntos de izaje solo existen como nodos y una figura sin cotas | Anexo C, nodos 126/127/128/129 y 3472/3473; Figura 15 | Sí |
| El cálculo iza desde los esquineros ISO, no desde padeyes | Anexo C: *"lifting from the top corner fittings using a spreader beam"* y *"from the bottom corner fittings using slings"* | Sí, cita literal |
| El informe no verifica el esquinero ni menciona refuerzos | Barrido del texto extraíble: **cero** apariciones de *reinforcement*, *capacity* e *ISO 1496*; y su índice no tiene sección de verificación de puntos de izaje | Sí |
| La hoja del contenedor es de enero de 2026 y no menciona izaje | `P22-ET-09-000-001` Rev B, 15-Ene-2026, anterior a las modificaciones | Sí |
| Las grúas son alcance de ADASA | ET Sección 9, pág. 34 | Sí, cita literal |
| Verificación dimensional de puntos de izaje en el FAT | ET Sección 8.1, pág. 32 | Sí |
| Siete días hábiles y no liberar sin aprobación | ET Sección 7, pág. 30 | Sí, cita literal |
| Los tres pesos que no concuerdan | Cálculo (122,41 kN), plano `P22-DWG-09-005-001` Rev B (13.300 kg), DS del contenedor Rev B (32.500 kg) | Sí |
| La orden colocada ayer con cuatro días | Minuta 09-09-26, Agenda Item 5 | Sí |

## Contexto Interno (No enviar)

- 🔴 **El encuadre es lo que hace que este correo no se pueda refutar.** La ET **no exige** un profesional chileno: cero apariciones de "profesional", "ingeniero", "endoso" o "inscrito" en la ET, la BAE y el PIE. Lo que la ET sí exige es **NCh 2369 Zona 3** y la aprobación de ADASA, y **BW Water eligió el PE local como su vía de cumplimiento**, declarada por escrito tres veces (20-May, 16-Jun y 30-Jun-2026). ADASA no le impone un profesional: le pide cerrar la vía que él mismo eligió. Por eso el correo **no usa las palabras "endorse", "Chilean" ni "registered"**, verificado por barrido: habla de "the structural review" y "the professional's delivery", que son hechos de la minuta.
- **El punto más fuerte es del expediente de BW Water, no una opinión de ADASA:** su propio Criterio de Diseño manda diseñar el padeye y su cálculo no lo trae, y el informe salió igual apto para construcción.
- **Una parte del izaje sí está entregada, y reclamarlo entero habría quemado el correo.** Por eso el párrafo 2 lo reconoce con las cifras exactas antes de pedir nada.
- **Fuera del correo, disponible si escala:** la multa de la **Cláusula 43.1 letra a)**, el hito de pago, y que el `PRG-32` venció el 22 de agosto, hace diecinueve días. El cierre lleva reserva genérica.
- 🔴 **El dato más incómodo para ADASA, que por eso no va:** el informe sin revisión profesional ya gobierna las reacciones de anclaje de fundaciones **que en Taltal ya están construidas**. Es la razón real por la que el alcance del profesional importa ahora.
- **Las vigas carrileras y los puntos de izaje internos** de la ET Sección 7 pág. 28 quedaron **fuera a propósito**: son izaje de mantención para extraer bombas y turbos, cosa distinta del yugo, y mezclarlos diluiría el pedido. Están pendientes y se reclaman por su vía.
- **La minuta de ayer no es oponible** (resumen automático, hablantes sin identificar) y **no menciona el izaje ni el PE**: barrido completo de sus 12 páginas, cero apariciones de izaje, yugo, grúa, maniobra, PE, endoso o cálculo estructural. Por eso el correo cita lo que Eduardo confirmó, no la minuta.
- **El yugo, ¿quién lo suministra?** El informe lo menciona dos veces como hipótesis y no lo atribuye. El correo lo pregunta expresamente, porque si no viene con el módulo, ADASA tiene que fabricarlo y necesita el diseño ya.
- 🔴 **El argumento del yugo se reforzó en una segunda pasada, a pedido del usuario.** La primera versión pedía "el diseño del yugo" y se quedaba corta: el yugo **no existe y hay que diseñarlo contra una hipótesis que el modelo ya fijó**, y **no hay ningún plano que ubique los puntos de izaje**. Ahora el correo lo dice con las cifras que lo prueban y ofrece la salida alternativa —rehacer el modelo—, que lo vuelve exigible sin ser un ultimátum.
- 🔴 **Cuarta pasada: se comprimió a 573 palabras, un 29 % menos, sin perder un solo argumento.** Tres pasadas de refuerzo lo habían dejado en 807, más que el correo de auditoría, que era el récord del par de control con 627. **Se apretó la redacción, no el fondo**: sobreviven la cita del padeye, las cuatro tensiones, el centro de gravedad descentrado, la disyuntiva de rutas, las cuatro viñetas, los tres pesos y la palanca de la Sección 7. **La cita del padeye pasó de bloque sangrado a línea**, recortada a las dos frases que prueban el punto, por decisión del usuario. Lo que salió fue repetición: las cifras del centro de gravedad y de las tensiones ya no se anticipan en el párrafo de lo entregado, porque reaparecen donde prueban algo.
- **El helper `add_quote` se retiró del script**, porque ya no hay cita en bloque.
- 🔴 **Las secciones de la ET se citan ahora con código, número y nombre, como manda la regla del proyecto, y la Sección 9 ceñida a su texto.** Antes decían "Section 9" a secas, que es débil para un reclamo contractual. Quedaron así: **Section 7 - Engineering and Documentation to be Developed During the Assignment** (con el código `P22-ET-09-000-001-0`, que va una sola vez en el cuerpo, en la primera cita), **Section 9 - Commissioning and Start-up** y **Section 8.1 - Minimum Scope of Factory Acceptance Testing**. La Sección 9 pasa de una paráfrasis suelta a decir lo que la ET dice: pone en alcance de ADASA la interconexión del módulo y el anclaje del contenedor a su base, **y declara que eso incluye los equipos de izamiento requeridos para ese fin, las grúas entre ellos**. Cuesta 41 palabras y las paga: es el fundamento de que el paquete tenga fecha propia.
- **El separador de la cita de sección es guion, no em dash.** El formato del proyecto es `Section N.N - Nombre`, y usar em dash además rompía el cero que el perfil mide en ese rasgo.
- **Se glosó `padeye` la primera vez que aparece: *"a padeye (a welded lifting lug)"*.** El término es opaco fuera de la ingeniería estructural, y quien lee del lado de BW Water incluye a Eduardo, que es gestión. **`lifting lug` no se eligió por ser el más común en abstracto, sino porque es el de ellos**: aparece en **19 documentos de BW Water** contra 2 de `padeye`, y es campo fijo de la plantilla de sus datasheets (*"With Lifting Lug/Eye (Yes / No)"*). Va en paréntesis y no entre comas, porque la frase ya lleva dos pares de comillas y un paréntesis: así se lee mejor, bajan las comas por oración y sube la densidad de paréntesis, que estaba en 5,24 contra 6,18 del perfil y quedó en 6,93.
- 🔴 **Se corrigió la grafía: cuatro "centre" pasaron a "center".** El documento se emite en `en-US` y la grafía británica queda subrayada en rojo en Word. **`anti-ia` no detecta esto**: mide fingerprints y ritmo, no ortografía regional. El barrido posterior encontró además dos "metre" en el Transmittal N39 **que ya se había enviado**, de modo que el defecto no era aislado y quedó como regla.
- 🔴 **Tercera pasada, a pedido del usuario: si usan los esquineros ISO, tiene que estar escrito que no requieren refuerzo.** El planteamiento es correcto y verificado resultó más fuerte de lo planteado, porque hay **dos rutas incompatibles en el expediente y ninguna declarada**: el Criterio manda diseñar padeye y el cálculo iza desde los esquineros. Entra en **dos lugares y ninguno más**: dos frases al cierre del párrafo del padeye, que plantean la disyuntiva, y la viñeta del punto de izaje, que la convierte en pedido. **No lleva viñeta propia** porque es un argumento, no un quinto entregable.
- **No se exige una norma concreta para el esquinero**, y es deliberado: la ET no fija ninguna para el izaje, de modo que exigir ISO 1496 o cualquier otra sería over-reach. Se pide "la base sobre la que lo afirman" y que el proveedor elija cuál invoca.
- **Se eliminó una muletilla repetida.** El correo llevaba *"I want to be precise about that"* y *"the one I want to be clearest about"*, dos glosas del mismo molde. Quedó la primera, que señala buena fe antes de reclamar; la segunda salió y el punto entra directo, que además pega más fuerte.

## Checklist pre-envío

- [x] ~~Confirmar que Thomas Engineers es el profesional de la orden del 9 de septiembre.~~ Confirmado por el usuario.
- [x] ~~Enviar en Reply-To sobre la cadena del Transmittal N39.~~
- [x] ~~Revisar que no se haya colado ninguna atribución a la ET sobre endoso, profesional o nacionalidad.~~ Barrido en cero: el correo no usa "endorse", "Chilean" ni "registered".

## Checklist post-envío

- [x] ~~`BORRADOR` → `ENVIADO`.~~ Hecho.
- [x] ~~Entrada de bitácora en el README y Estado Vigente.~~ Hecho.
- [ ] 🔴 **Dejar el respaldo del enviado en esta carpeta y anotar la hora** en la Bitácora del README.
- [ ] 🔴 **Fijar la fecha del `PRG-49` cuando BW Water confirme la de entrega de su profesional.** Sigue SIN FECHA a propósito: el correo la pide y no la impone, de modo que escribirla antes de que la confirmen afirmaría un acto que no ocurrió.
- [ ] Si la respuesta declara la ruta de izaje, registrarla: define si el cierre del `PRG-49` exige padeye diseñado o constancia sobre los esquineros.
