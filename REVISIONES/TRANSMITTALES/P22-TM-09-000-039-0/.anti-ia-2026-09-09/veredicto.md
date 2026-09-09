# Veredicto anti-ia — Transmittal N39

Documento: `P22-TM-09-000-039-0_TRANSMITTAL.md` (1.687 palabras, ingles)
Fecha: 2026-09-09 | Modo: revisar | **Segunda pasada**, tras entrar la Seccion 3

## Contexto de esta pasada

La primera pasada de hoy cerro en VERDE sobre un transmittal de 1.511 palabras y cinco
secciones. Despues el usuario pidio fundir en un solo correo la cobertura del N39 y la
auditoria de emision para construccion, de modo que las cuatro tablas de esa auditoria
entraron como **Seccion 3 — Issue for Construction of the Approved Engineering** y las
secciones que la seguian corrieron a 4, 5 y 6. El documento crecio a 1.687 palabras de
prosa mas 73 filas de tabla. Este veredicto cubre esa version.

## Veredicto del original de esta pasada

Cobertura: modo=revisar | familias=[universales U-01 a U-12, claude CL-01 a CL-25 con foco en CL-19/20/21] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto el asistente sobre Claude Opus 5 en esta sesion]
AMARILLO | 2% | Confianza: Alta
Pre-filtro: Activado (Q3 vocabulario tecnico normalizado, Q4 formato institucional obligatorio del proyecto) | Checklist: B | Pasos evaluados: 17/17
Base de deteccion: tecnicas estadisticas propias, sin verificador oficial validado; senal, no prueba (R-09)

**Hallazgo unico y real:** el bloque `Action` de la Seccion 3 nueva salio como **una sola
oracion de 76 palabras con tres punto y coma**, sobre el umbral critico de U-03, que esta
en 50. Es el mismo defecto que aparecio en el parrafo equivalente del correo, y por la
misma causa: enumerar cuatro grupos de documentos encadenados.

**Falsos positivos descartados, y por que.** El particionador de oraciones junta un rotulo
en negrita con el parrafo que le sigue, de modo que reporta como oraciones largas cosas
que no lo son: `Disposition at a glance` con sus tres vinetas (73 palabras aparentes),
`Why Code 2` con su primera vineta (58), y el rotulo de la Tabla 4 pegado al parrafo
siguiente (59). Se verifican leyendolas, no confiando en el conteo.

**Preexistentes que NO se tocan:** `Entering the list`, `Also open` y `Closing with this
transmittal` miden 64, 61 y 64 palabras con punto y coma. Son el formato fijo de la
seccion de pendientes en todos los transmittals del proyecto, identico en el N37 y el N38
ya enviados, y pasaron el gate en la primera pasada. Cambiarlos aqui romperia la
consistencia de la serie sin ganar nada.

**Fingerprints detectados:** U-03 (una ocurrencia, corregida)
**Modelo autor:** Claude Opus 5 (autoria conocida, no sospechada)

## Cambios realizados

| Patron original | Correccion | Fingerprint |
|---|---|---|
| "Action — issue at Revision 0 by Friday 11 September 2026: the 34 documents of Table 1, which need no change of content...; the 12 of Table 2...; the corrected title block...; and the seven deliverables of Table 4." (76 palabras, 3 punto y coma) | Cinco oraciones sueltas de 11 a 30 palabras, sin punto y coma | U-03 |

El `.md` y el `crear_transmittal.py` quedaron sincronizados y el Word se regenero.

## Re-evaluacion

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida]
VERDE | 0% | Confianza: Alta
Estilo personal: Aplicado — Caso A. El transmittal se mantiene en **tercera persona institucional**, que es su registro de siempre; la primera persona vive en el correo que lo acompana, porque ese lo firma una persona y este lo emite ADASA.
Registro: calibrado contra el par de control de transmittals enviados, no contra el perfil en espanol.

Barridos duros, todos en cero sobre el `.md`: simbolo de seccion, referencias internas de
ADASA, mencion del asesor interno, frases-firma, castellano filtrado, y "in Rev X" sobre un
Code 2. Las cuatro marcas de contenido de la Seccion 3 se verificaron presentes en el `.md`
y en el Word emitido.

### Estilometria contra el par de control

| Rasgo | N39 antes | **N39 con Seccion 3** | N38 | N37 | N36 |
|---|---|---|---|---|---|
| mediana de oracion | 18,0 | **22,0** | 26,0 | 23,0 | 23,0 |
| percentil 90 | 48,1 | **45,0** | 45,0 | 49,9 | 42,8 |
| sobre 30 palabras | 35,0 % | **32,9 %** | 41,8 % | 40,2 % | 37,7 % |
| punto y coma /100 or. | 25,0 | **14,5** | 27,5 | 17,1 | 23,4 |
| parentesis /mil | 2,11 | **2,96** | 2,07 | 3,18 | 4,77 |
| comas por oracion | 1,00 | **1,00** | 1,01 | 1,33 | 0,99 |
| parrafo, mediana | 56 | **51,5** | 61 | 72,5 | 56,5 |
| TTR | 0,527 | **0,507** | 0,549 | 0,518 | 0,541 |

Todos los rasgos dentro de banda o mejor. La Seccion 3 **subio** la mediana de 18 a 22,
que la acerca al control, y bajo la densidad de punto y coma.

> Medido con el `.md` desenvuelto. El archivo lleva cada parrafo en una sola linea, con un
> maximo de 864 columnas: envuelto a 100, el script cuenta la linea fisica y la mediana
> cae a 12. Comprobar el ancho antes de leer cualquier cifra.

### Rendimiento del analisis

Fingerprints mas efectivos: U-03, el unico que atrapo algo real en esta pasada.
No aplicables: U-04, U-06, U-08 (la estructura repetida entre subsecciones y los rotulos de
tabla son formato obligatorio), U-09 (el TAG y el termino tecnico no se rotan por
sinonimos), U-10 (los siete em dash son los del codigo de respuesta y los titulos de
subseccion, no inserciones parenteticas).
Checklist B, 17 pasos aplicables de 17.
Nota para revisiones futuras del mismo tipo: cuando entra una seccion con enumeraciones de
grupos de documentos, el defecto previsible es la oracion-lista con punto y coma. Se busca
por conteo de palabras entre puntos, filtrando antes los rotulos en negrita y las filas de
tabla, o el informe se llena de falsos largos.
