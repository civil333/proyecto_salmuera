# Veredicto anti-ia — NT P22-NT-06-000-001-0 y correo de remision

Fecha: 04-09-2026. Documentos evaluados: el `.md` fuente de la Nota Tecnica y el cuerpo del
correo `2026-09-04_Entrega-Ingenieria-Vigente-Construccion-Taltal.docx`.

## Veredicto

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto Claude Opus 5 en esta sesion]
VERDE | Confianza: Alta
Pre-filtro: no activado | Checklist: A (proposito analitico-declarativo) | Registro: correspondencia y prosa normativa, ambos calibrados en el perfil
Base de deteccion: tecnicas estadisticas propias mas medicion estilometrica reproducible; senal, no prueba (R-09)

**Hallazgos clave:**

- **CL-22, apertura escindida — DETECTADO Y CORREGIDO.** El borrador abria una oracion con
  "Lo que cambia es la accesoria". El perfil declara ese patron como ajeno al autor, que abre
  con el sustantivo tecnico o con el impersonal. Corregido a "Los accesorios y las bridas si
  cambian" (el colectivo "la accesoria" era ademas un termino inexistente, corregido el mismo dia
  a peticion del usuario).
- **Ritmo de oracion desviado en el primer borrador.** La medida inicial daba parentesis a
  2,92 por mil contra 5,06 del perfil, e impersonal "se" a 13,6 por mil contra 25. Ambos
  corregidos en la pasada de revision.
- Sin ornamento: 0 candidatas en 48 oraciones, confirmado tambien a mano.

**Fingerprints detectados tras la correccion:** ninguno.
**Modelo autor:** Claude Opus 5 (autoria conocida, no sospechada).

## Contraste estilometrico contra el perfil

| Rasgo | Perfil, prosa analitica | Nota Tecnica | Juicio |
|---|---|---|---|
| Mediana de oracion | 22 palabras | 20,0 | en rango |
| Percentil 90 de oracion | 43 | 40,4 | en rango |
| Oraciones sobre 30 palabras | 26,3% | 20,0% | algo bajo |
| Oraciones bajo 8 palabras | 5,6% | 2,0% | bajo |
| Punto y coma | 0 | 0 | calza |
| Em dash | 0 | 0 | calza |
| Parentesis por mil palabras | 5,06 | 6,39 | en rango (correspondencia da 6,18) |
| Impersonal "se" por mil | ~25 | 24,3 | calza |
| Mediana de parrafo | 28 palabras | 38,5 | alto |
| Percentil 90 de parrafo | 81 | 63,6 | en rango |
| TTR en ventanas de 300 | 0,469 | 0,487 | en rango |
| Conectores del perfil | segun, debido a, por lo que | 5 / 3 / 3 | calza |
| Ornamento | 0 | 0 | calza |

**Voz: propia.** Los rasgos duros calzan. Las dos desviaciones que quedan, mediana de parrafo
un 37% sobre el perfil y menos oraciones en los extremos de longitud, se atribuyen al registro:
el documento es normativo-contractual y encadena datos por parrafo, mas cerca de la
especificacion tecnica que de la prosa analitica libre. El perfil mide el ritmo de oracion de
la prosa normativa (mediana 23 contra 22) pero no publica su mediana de parrafo, por lo que
esa fila queda sin linea base y se declara en vez de forzarse.

**Correo de remision.** Registro de correspondencia, seccion 11.1 del perfil: 135 palabras,
primera persona ("les remito", "les pido", "quedo atento"), apertura "Estimados señores" y
cierre "Saludos cordiales", sin punto y coma ni em dash en el cuerpo. Cumple los tres
movimientos de la estructura invariable.

## Medicion

Reproducible con:

```
python3 ~/.claude/skills/anti-ia/estilometria.py <prosa desenvuelta>
```

La prosa se extrae del `.md` quitando frontmatter, titulos y filas de tabla, y **uniendo las
lineas fisicas de cada parrafo**. Sin desenvolver, el script lee cada linea del `.md` como un
parrafo y devuelve mediana de oracion 11,5 y de parrafo 14, que no describen el texto.

---

## Constancia de la correccion de vocabulario del 04-09-2026

El usuario observo en el PDF emitido la subseccion "El listado de materiales cambia la accesoria" y
pregunto que era la accesoria. **Era un termino inexistente**: "accesoria" no funciona como
colectivo en espanol tecnico, a diferencia de "la perneria" o "la tornilleria", y el propio texto ya
usaba el plural correcto dos parrafos mas abajo ("se retiran los dos accesorios de PVC-U"), de modo
que el documento se contradecia consigo mismo. Se reemplazo por **"accesorios y bridas"**, que
distingue las dos familias que efectivamente se mueven y que se compran por separado.

**Efecto sobre la medicion:** ninguno material. El contraste con el perfil se mantiene en mediana de
oracion 20,0, percentil 90 de 40,4, parentesis 6,38 por mil, impersonal 24 apariciones, mediana de
parrafo 38,5, TTR 0,488, cero em dash, cero punto y coma y cero ornamento. El veredicto sigue en
**VERDE, voz propia**, con las dos desviaciones de registro ya declaradas arriba.

**Leccion que no es de estilo sino de metodo:** el fingerprint CL-22 se detecto y se corrigio, pero
la revision anti-ia no cuestiono el **sustantivo** de la frase. Un chequeo de fingerprints no
sustituye la lectura tecnica del vocabulario por parte de quien conoce el dominio.

---

## Segunda actualizacion del 04-09-2026: ampliacion tras la revision de isometrias

La nota crecio de 6 a 7 paginas: se corrigio el encuadre de la brida (misma pieza, el material lo
fija el listado), se agregaron las empaquetaduras y entro una subseccion nueva sobre el cuadernillo
de isometrias con la advertencia de renumeracion de hojas.

**Medicion tras la ampliacion**, sobre 1.264 palabras de prosa: mediana de oracion 20,0 (perfil 22),
percentil 90 de 37,6 (43), oraciones sobre 30 palabras 16,9 % (26,3 %), bajo 8 palabras 3,4 %
(5,6 %), parentesis 6,33 por mil (5,06), impersonal 24 apariciones, mediana de parrafo 40,0 (28),
percentil 90 de parrafo 63,0 (81), TTR 0,491 (0,469), **cero em dash, cero punto y coma, cero
ornamento**.

**Veredicto: VERDE, voz propia.** El perfil se mantiene estable respecto de la medicion anterior; la
ampliacion no movio ningun rasgo duro. Persisten las dos desviaciones ya declaradas y atribuidas al
registro normativo-contractual: la mediana de parrafo por sobre el perfil y menos oraciones en los
extremos de longitud.

**Sin fingerprints nuevos.** Se reviso en particular que la subseccion nueva no abriera con la
apertura escindida CL-22, que ya habia aparecido una vez en este documento.

---

## Tercera actualizacion del 04-09-2026: la nota absorbe el indice del paquete

Se elimino el `00_INDICE.txt` y su contenido propio paso a la nota, que crecio a **8 paginas** con
una seccion **Contenido del paquete** (que hay en cada carpeta y notas de formato) y una subseccion
**Documentos que cambian de revision** con la tabla de los once.

**Medicion sobre 1.570 palabras de prosa:** mediana de oracion 17,0 (perfil 22), percentil 90 de
35,8 (43), oraciones sobre 30 palabras 14,9 % (26,3 %), bajo 8 palabras 4,1 % (5,6 %), parentesis
6,37 por mil (5,06), impersonal 28 apariciones, mediana de parrafo 40,0 (28), TTR 0,487 (0,469),
**cero em dash, cero punto y coma, cero ornamento**.

**Veredicto: VERDE, voz propia.** El ritmo baja respecto de las mediciones anteriores (mediana de 20
a 17) y la causa es identificable: la seccion nueva es un **indice en prosa**, con frases de
enumeracion cortas por naturaleza. No se fuerza su fusion, porque alargar artificialmente las
oraciones de un indice lo hace menos legible sin acercarlo a la voz del autor. Se declara la
desviacion y se mantiene.

**Un punto y coma detectado y corregido.** Aparecio en la seccion nueva, en el par de anexos de la
ET de montaje ("con sus anexos; y el anexo A13"), y se partio en dos oraciones. El perfil registra
cero punto y coma en prosa analitica y en correspondencia.

**Dos artefactos de medicion, no de estilo, que conviene recordar.** El script corta los rotulos
numerados (`**0. CONTROL DE CAMBIOS`) como oraciones de una palabra, lo que hundia el porcentaje de
oraciones cortas al 10,1 % aparente contra el 4,1 % real. Es el mismo tipo de artefacto que ya
habia aparecido con las filas de tabla y con las lineas fisicas del `.md`: **antes de leer una
desviacion como defecto de voz, comprobar que el parser este midiendo prosa.**
