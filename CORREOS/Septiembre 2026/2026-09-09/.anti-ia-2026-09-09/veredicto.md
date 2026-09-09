---
titulo: Veredicto anti-ia del correo de auditoria de emision para construccion
documento: 2026-09-09_Issue-for-Construction-Audit.docx
fecha: 2026-09-09
modo: revisar
estado: INTERNO
---

# Veredicto anti-ia, modo revisar

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: el texto lo genero el asistente en esta sesion, de modo que la familia del modelo autor es conocida y no sospechada]

Documento: correspondencia de proyecto en ingles, a BW Water. Checklist A. Registro
**calibrado** contra la seccion 11.1 del perfil, que mide 971 palabras de correo enviado.
Base de deteccion: tecnicas estadisticas propias, sin verificador oficial validado. Senal,
no prueba (R-09).

## Evaluacion del original

**AMARILLO** | Confianza: Alta

El texto llegaba con el ritmo del autor ya puesto y fallaba en dos reglas duras del perfil
y en la extension.

| Hallazgo | ID | Evidencia |
|---|---|---|
| Inflacion de extension | CL-19 | 926 palabras de prosa para un correo cuyo nucleo son cuatro tablas. Es el prior dominante de Opus 5 y el usuario lo pidio explicitamente mas ejecutivo |
| Cascada de ordinales | U-06 | "First, ... Second, ... Third, ... Fourth, ..." en el bloque de peticiones, cuatro escalones perfectos |
| Template identico entre bloques | U-04 | Las cuatro glosas de tabla abrian con la misma forma y la misma longitud |
| Em dash | perfil, regla 6 | 2 apariciones. El corpus del autor tiene 0 en 70.738 palabras |
| Punto y coma | perfil, regla 6 | 2 apariciones. El corpus de correspondencia tiene 0 |
| Densidad de parentesis | perfil, regla 3 | 7,56 por mil contra 6,18 del registro |

## Cambios realizados

| Patron original | Correccion | ID |
|---|---|---|
| 926 palabras de prosa | 627 palabras, un tercio menos, con las cuatro tablas y todos los datos intactos | CL-19 |
| "First, ... Second, ... Third, ... Fourth, ..." | Un solo parrafo que enumera lo pedido sin escalones | U-06 |
| Bloque del DDSR en tres parrafos | Un parrafo, con el dato que sostiene el punto | CL-19 |
| Parrafo entero sobre el formulario PEM-F013 y el codigo IFA | Eliminado. Era un punto secundario que dispersaba el reclamo | CL-19 |
| Glosas de tabla de forma identica | Cada una con estructura y largo propios | U-04 |
| "Luis Rivera Gonzalez — Leader", "ADASA — Aguas de Antofagasta", "Table 1 — ..." | Coma y punto en lugar del em dash | perfil, regla 6 |
| "Victor Gutierrez (ADASA); Jeryl Regulacion" | Coma | perfil, regla 6 |
| "The workshop reads the document, not the form. These need the issue purpose corrected, not a new revision." | "What reaches the workshop is the document. Correcting the issue purpose is enough on these, without a new revision." | U-01 |
| "46 have never been issued for construction. 34 of those carry..." | Oracion unica, ninguna abre con cifra | forma |
| "ADASA approved them", "we are asking" | "I approved them", "the rule I am asking you to apply" | perfil, 11.1 |

## Re-evaluacion

**VERDE** | Confianza: Alta

**Fingerprints detectados:** ninguno activo. U-01 marca dos coincidencias que son los
rotulos de tabla ("approved with no open observation, not issued for construction"), donde
la construccion describe un estado documental y no es antitesis retorica. U-09 registra
"Revision 0" seis veces y "issued for construction" cinco, que es la terminologia del
asunto y no relleno.

**Modelo:** Claude Opus 5, autoria conocida.

Estilo personal: **Aplicado, Caso A**. El borrador ya estaba en la voz del autor en ritmo
y en ornamento, de modo que no habia que estilizar el documento entero; las reescrituras
se redactaron directamente en esa voz y el resto solo se verifico en el empalme.

## Estilometria, antes y despues

| Rasgo | Original | Final | Perfil 11.1 |
|---|---:|---:|---:|
| Mediana de oracion | 18,0 | **18,5** | 18 |
| Percentil 90 | 35,1 | **35,1** | 35 |
| Oraciones sobre 30 palabras | 14,0% | 17,6% | 14,3% |
| Parentesis por mil palabras | 7,56 | **6,38** | 6,18 |
| Em dash | 2 | **0** | 0 |
| Punto y coma | 2 | **0** | 0 |
| Ornamento | 0 | **0** | 0 |
| Rachas de 3 oraciones cortas | 0 | **0** | 0 |
| Palabras de prosa | 926 | **627** | — |

Voz: primera persona dominante, que es lo que manda el registro de correspondencia. Seis
"I", un "my" y dos "me" contra cinco menciones de ADASA, de las cuales tres estan en el
encabezado y en la reserva de derechos del cierre.

Oraciones sobre 50 palabras: ninguna. Las tres que el segmentador marca son artefactos de
concatenar encabezados sin punto final con la oracion siguiente. La oracion real mas larga
tiene 43 palabras.

## Nota para revisiones futuras del mismo tipo

En correspondencia de este proyecto el em dash entra siempre por tres puertas que no son
prosa: la linea del remitente, el rotulo de tabla y el bloque de firma. Conviene barrerlas
antes de medir, porque el conteo las cuenta y el perfil exige cero. El punto y coma entra
por la lista de copia del encabezado.
