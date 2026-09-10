# Veredicto anti-ia — Correo del paquete de izaje y el alcance de la revision estructural

Documento: `2026-09-10_Lifting-Package-and-PE-Scope.docx` (716 palabras de prosa, ingles)
Dos pasadas: la primera sobre 534 palabras, la segunda tras reforzar el pedido del yugo.
Fecha: 2026-09-10 | Modo: revisar

## Veredicto del original

Cobertura: modo=revisar | familias=[universales U-01 a U-12, claude CL-01 a CL-25 con foco en CL-19/20/21] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto el asistente sobre Claude Opus 5 en esta sesion]
AMARILLO | 4% | Confianza: Alta
Pre-filtro: Activado (Q3 vocabulario tecnico normalizado) | Checklist: A | Pasos evaluados: 19/19
Base de deteccion: tecnicas estadisticas propias, sin verificador oficial validado; senal, no prueba (R-09)

**Hallazgos clave, los dos de formato y no de contenido:**

- **Tres em dash, donde el perfil mide cero** en 70.738 palabras de prosa propia. Venian de las
  tres vinetas del pedido, que separaban el nombre del entregable de su glosa. Los correos anteriores
  de esta serie llevaban uno solo, y era el del codigo de respuesta.
- **Parentesis en cero**, contra 6,18 por mil del perfil y 5,8 a 7,4 de los correos ya enviados. El
  texto no tenia ni una acotacion.

**Fingerprints detectados en el original:** U-10 en su forma de densidad
**Modelo autor:** Claude Opus 5 (autoria conocida, no sospechada)

## Cambios realizados

| Patron original | Correccion | Motivo |
|---|---|---|
| Vinetas con `" — as a document of its own..."`, `" — showing the lifting points..."`, `" — including who supplies it."` | Coma o continuacion directa | em dash a cero |
| "The Structural Calculation Report P22-CD-09-005-001 Rev 0" | "...Report (P22-CD-09-005-001 Rev 0)" | densidad de parentesis |
| "The Structural Design Criteria P22-CD-09-005-003 Rev 0" | "...Criteria (P22-CD-09-005-003 Rev 0)" | densidad de parentesis |
| "at the Factory Acceptance Test, which opens" | "...Factory Acceptance Test (FAT), which opens" | densidad, y la sigla queda introducida antes de usarse |
| "within the erection manual, and none has been submitted" | "inside the erection manual for the plant. That manual is where the lifting operation itself is described, and neither it nor the three documents have been submitted" | contenido: la ET no exige un procedimiento de maniobra suelto, lo pone dentro del Manual de Montaje |

## Re-evaluacion

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida]
VERDE | 0% | Confianza: Alta
Estilo personal: Aplicado — Caso A
Registro: **primera persona**, el mismo de los dos correos anteriores de esta cadena.

### Estilometria contra el par de control

| Rasgo | Antes | **Final** | N39 enviado | Auditoria | N38 enviado | Perfil 11.1 |
|---|---|---|---|---|---|---|
| palabras de prosa | 514 | **534** | 404 | 627 | 249 | — |
| mediana de oracion | 19,0 | **19,5** | 16,0 | 18,5 | 13,0 | 18 |
| percentil 90 | 35,4 | **35,0** | 28,8 | 35,1 | 29,6 | 35 |
| oracion mas larga | 43 | **43** | 36 | 43 | 33 | — |
| punto y coma | 0 | **0** | 0 | 0 | 1 | 0 |
| parentesis /mil | **0** | **5,62** | 7,43 | 6,38 | 4,02 | 6,18 |
| em dash | **3** | **0** | 1 | 0 | 1 | 0 |

**Es el correo de la serie que mejor calza con el perfil**: mediana 19,5 contra 18, percentil 90 en
35,0 contra 35, y cero en los dos rasgos que el perfil mide en cero.

### Una decision declarada, no un descuido

La frase *"A good part of the work is already done, and I want to be precise about that"* roza
**U-02B**, porque la segunda mitad se puede borrar y el parrafo sigue diciendo lo mismo. Se mantiene
por funcion de registro: el correo reclama despues de reconocer lo entregado, y esa clausula es la
que senala que ADASA no esta inflando el pedido. En un correo cuyo objetivo es que emitan, el tono
paga mas que la economia. Queda anotada para no repetirla por inercia.

### Barridos duros, sobre el documento emitido

Cero simbolo de seccion, cero castellano en el cuerpo, cero mencion del asesor interno, cero
frases-firma, cero hedging.

🔴 **Y el barrido que este correo necesitaba mas que ninguno, la regla anti-invencion:** cero frases
que aten la Especificacion Tecnica a un endoso, un profesional o una nacionalidad. El correo **no
usa las palabras "endorse", "Chilean" ni "registered"**, verificado por conteo. Habla de *"the
structural review"* y *"the professional's delivery"*, que son hechos de la minuta del 9 de
septiembre, no interpretaciones de la ET. Fundar el reclamo en que la ET exige un profesional
chileno lo habria hecho refutable de una linea, porque la ET no lo dice.

## Segunda pasada, por refuerzo del pedido

El usuario pidio precisar el pedido: el yugo **no existe y hay que disenarlo contra una hipotesis
que el modelo ya fijo**, y **no hay ningun plano que ubique los puntos de izaje**. Entraron dos
parrafos y las cuatro vinetas del pedido, con las cifras que lo prueban, verificadas por render
sobre las paginas 17 y 18 de 548 del informe.

**Un hallazgo de la relectura, y es de molde y no de medicion.** El correo quedo con dos glosas del
mismo patron: *"and I want to be precise about that"* en el parrafo 2 y *"and it is the one I want
to be clearest about"* en el cuarto. Una sola pasa como senal de buena fe; dos se leen como
muletilla, que es **U-08 en su variante de cierre formulario**. Se elimino la segunda y el punto
entra directo, que ademas pega mas fuerte.

| Rasgo | 1a pasada | **Final** | Perfil 11.1 |
|---|---|---|---|
| palabras de prosa | 534 | **716** | — |
| mediana de oracion | 19,5 | **19,5** | 18 |
| percentil 90 | 35,0 | **36,5** | 35 |
| oracion mas larga | 43 | **43** | — |
| punto y coma | 0 | **0** | 0 |
| parentesis /mil | 5,62 | **4,19** | 6,18 |
| em dash | 0 | **0** | 0 |

**El unico rasgo que baja es la densidad de parentesis**, de 5,62 a 4,19 por mil, porque el texto
crecio y los parentesis siguen siendo tres. Queda dentro del par de control, donde el correo del N38
enviado mide 4,02, y no se fuerzan parentesis artificiales en un correo que ya es el mas largo de la
serie. VERDE se mantiene.

## Tercera pasada: la disyuntiva de los esquineros

El usuario pidio exigir que, si se usan los esquineros ISO del contenedor, **este escrito que no
requieren refuerzo**. Entraron dos frases al cierre del parrafo del padeye y la vineta del punto de
izaje reformulada para cubrir las dos rutas.

🔴 **Y aparecio CL-19 de verdad, no como sospecha.** El parrafo nuevo repetia, con las mismas
palabras, la descripcion de las dos condiciones de izaje que el parrafo 2 ya daba: *"from the top
corner fittings with a spreader beam and from the bottom corner fittings with slings"*. El punto
nuevo era la **disyuntiva**, no la descripcion. Se corto la repeticion y el parrafo baja de 79 a 59
palabras sin perder nada.

| Rasgo | 2a pasada | 3a con redundancia | **Final** | Perfil 11.1 |
|---|---|---|---|---|
| palabras de prosa | 716 | 826 | **807** | — |
| mediana de oracion | 19,5 | 20,0 | **20,0** | 18 |
| percentil 90 | 36,5 | 37,0 | **37,0** | 35 |
| oracion mas larga | 43 | 44 | **44** | — |
| punto y coma | 0 | 0 | **0** | 0 |
| parentesis /mil | 4,19 | 3,63 | **3,72** | 6,18 |
| em dash | 0 | 0 | **0** | 0 |

**Dos rasgos a declarar, y los dos son consecuencia del largo:**

- **807 palabras** es el correo mas largo de la serie, contra 627 del de auditoria, que era el record
  del par de control. **No es relleno**: cubre siete asuntos con sustancia y cada parrafo aporta un
  hecho verificado. Pero es el limite: si entra algo mas, hay que sacar algo.
- **Parentesis en 3,72 por mil**, contra 6,18 del perfil. Bajan porque el texto crece y siguen siendo
  tres. Queda cerca del correo del N38 enviado, que mide 4,02, y **no se fuerzan parentesis
  artificiales** para maquillar la densidad en un correo que ya es largo.

VERDE se mantiene.

## Cuarta pasada: compresion a 573 palabras

El usuario pidio el correo "mas resumido y ejecutivo". Baja de **807 a 573 palabras, un 29 por
ciento**, y por decision suya **sin perder ningun argumento**: se aprieta la redaccion y la cita del
padeye pasa de bloque sangrado a linea, recortada a las dos frases que prueban el punto.

🔴 **Un falso positivo de la medicion, y conviene dejarlo escrito.** Tras comprimir, las comas por
oracion saltaron de 1,29 a **1,52**, contra 0,65 a 0,88 del par de control. Parecia prosa recargada.
No lo era: **el script cuenta las comas de millar** —13,300, 32,500, 5,486, 6,514— y las de enumerar
cifras. Descontadas, la densidad real era 1,28, la misma de antes. Lo que subio no fue la carga
sintactica sino **la densidad de cifras por palabra**, que es consecuencia aritmetica de acortar un
texto cuyas cifras no se tocan. Antes de corregir un rasgo, comprobar si la metrica lo esta contando
bien.

Se hizo igual **un cambio de ritmo que si valia**: la oracion de las tensiones, 33 palabras con siete
comas, se partio en tres, y las cotas del centro de gravedad pasaron a parentesis. Eso subio la
densidad de parentesis, que la compresion habia dejado en dos.

| Rasgo | 3a pasada | Comprimido | **Final** | Perfil 11.1 |
|---|---|---|---|---|
| palabras de prosa | 807 | 570 | **573** | — |
| mediana de oracion | 20,0 | 19,0 | **18,5** | 18 |
| percentil 90 | 37,0 | 36,0 | **36,0** | 35 |
| oracion mas larga | 44 | 41 | **41** | — |
| punto y coma | 0 | 0 | **0** | 0 |
| parentesis /mil | 3,72 | 3,51 | **5,24** | 6,18 |
| em dash | 0 | 0 | **0** | 0 |
| comas por oracion | 1,29 | 1,52 | **1,37** | — |

**Es el mejor calce de toda la serie**: mediana 18,5 contra 18 del perfil y percentil 90 en 36,0
contra 35, con cero en los dos rasgos que el perfil mide en cero. VERDE se mantiene.

## Cierre: glosa del termino y correccion de grafia

Dos ajustes finales, ninguno de estilo medido:

- **Ortografia.** Cuatro `centre` en un documento emitido en `en-US`, que Word subraya en rojo.
  Corregidos a `center`. **Ningun modo de anti-ia detecta esto**: la skill mide fingerprints y ritmo,
  no ortografia regional. El barrido posterior encontro ademas dos `metre` en el Transmittal N39, que
  ya se habia enviado. Quedo como regla en [[feedback_grafia_americana_en_documentos_en_us]].
- **Glosa de `padeye`.** Se anade *"a padeye (a welded lifting lug)"* en la primera aparicion. El
  termino se eligio por frecuencia en el propio expediente del proveedor, 19 documentos contra 2, y
  no por ser el mas comun en abstracto. En parentesis y no entre comas, porque la frase ya carga dos
  pares de comillas.

| Rasgo | Antes de estos dos | **Final** | Perfil 11.1 |
|---|---|---|---|
| palabras de prosa | 573 | **577** | — |
| mediana de oracion | 18,5 | **18,5** | 18 |
| percentil 90 | 36,0 | **36,0** | 35 |
| punto y coma | 0 | **0** | 0 |
| parentesis /mil | 5,24 | **6,93** | 6,18 |
| em dash | 0 | **0** | 0 |

**Todos los rasgos quedan en banda o mejor**, y la glosa corrigio de paso el unico que estaba bajo.
VERDE se mantiene.

## Quinta pasada: las citas de la ET, y un em dash que se colo por la puerta de atras

El usuario observo que el correo nombraba "Section 9" a secas, sin codigo ni nombre, y que eso es
debil para un reclamo contractual. Se reescribieron las tres citas al formato del proyecto: codigo
del documento una sola vez en la primera, y `Section N - Nombre` en cada una. La Seccion 9 pasa
ademas de parafrasis suelta a cenirse al texto de la ET.

🔴 **Y al hacerlo entro un defecto por la puerta de atras: tres em dash.** Los use como separador
entre el numero de seccion y su nombre, y el perfil mide **cero em dash en 70.738 palabras**. El
formato del proyecto usa **guion normal** —`Section 5.4.1 - Constructive Characteristics`—, de modo
que la correccion resuelve las dos cosas a la vez. Es la segunda vez en este mismo correo que el em
dash entra por un separador de lista o de titulo, no por prosa: **es ahi donde hay que buscarlo**.

| Rasgo | Comprimido | Con las citas | **Final** | Perfil 11.1 |
|---|---|---|---|---|
| palabras de prosa | 577 | 618 | **618** | — |
| mediana de oracion | 18,5 | 17,5 | **17,5** | 18 |
| percentil 90 | 36,0 | 35,9 | **35,9** | 35 |
| punto y coma | 0 | 0 | **0** | 0 |
| parentesis /mil | 6,93 | 8,09 | **8,09** | 6,18 |
| em dash | 0 | **3** | **0** | 0 |

**La densidad de parentesis queda en 8,09 por mil, sobre el perfil y sobre el par de control**, cuyo
maximo es 7,43. Se acepta: los cinco parentesis son codigos de documento, la glosa del termino y las
cotas del centro de gravedad. **Quitar una referencia de documento para ajustar una metrica seria
empeorar el correo**, y un exceso de parentesis no es fingerprint de maquina sino rasgo del autor.

El correo sube de 577 a 618 palabras, y las 41 de diferencia son casi todas nombre de seccion. Se
pagan: son el fundamento de que el paquete de izaje tenga fecha propia.

### Rendimiento del analisis

Fingerprints mas efectivos: U-10 en densidad, y los dos rasgos medidos del autor, em dash y
parentesis, que aqui fueron los unicos que rindieron.
No aplicables: U-01, U-04, U-06, U-12. CL-19 tampoco: las 716 palabras cubren siete asuntos
distintos sin relleno, y el correo es largo porque el pedido tiene cuatro piezas que hay que
nombrar una por una, no por inflacion.
Checklist A, 19 pasos aplicables de 19.
Nota para correos futuros del mismo tipo: cuando el pedido se enumera en vinetas, el em dash entra
solo como separador entre el nombre del entregable y su glosa. Revisarlo antes de medir.
