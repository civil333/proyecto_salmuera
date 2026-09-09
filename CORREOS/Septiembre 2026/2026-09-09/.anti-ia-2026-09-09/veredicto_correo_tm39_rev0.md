# Veredicto anti-ia — Correo unico del Transmittal N39 y la emision en revision 0

Documento: `2026-09-09_Transmittal-N39-and-Rev0-Issue.docx` (419 palabras de prosa, ingles)
Fecha: 2026-09-09 | Modo: revisar

> El `veredicto.md` de esta misma carpeta corresponde al correo de auditoria del que este
> hereda, hoy archivado en `_no_enviados_fusionados/`. Los dos se conservan.

## Veredicto del original

Cobertura: modo=revisar | familias=[universales U-01 a U-12, claude CL-01 a CL-25 con foco en CL-19/20/21] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto el asistente sobre Claude Opus 5 en esta sesion]
AMARILLO | 5% | Confianza: Alta
Pre-filtro: Activado (Q3 vocabulario tecnico normalizado) | Checklist: A | Pasos evaluados: 19/19
Base de deteccion: tecnicas estadisticas propias, sin verificador oficial validado; senal, no prueba (R-09)

**Hallazgos clave, los tres del mismo parrafo:**

- **U-03.** El pedido del viernes 11 salio como **una sola oracion de 78 palabras**, muy
  sobre el umbral critico de 50. Al fundir dos correos, la enumeracion de los cuatro grupos
  de documentos se encadeno en un solo periodo.
- **Punto y coma: 3, donde el perfil mide 0.** La medicion del 26-ago-2026 arroja cero en
  70.738 palabras de prosa propia, de modo que sembrarlos es voz ajena aunque el resto
  acierte. Los tres venian de esa misma enumeracion.
- **Parentesis en 2,43 por mil**, contra 6,18 del perfil y 6,38 del correo de auditoria del
  que este hereda. Densidad a la mitad.

**Fingerprints detectados en el original:** U-03
**Modelo autor:** Claude Opus 5 (autoria conocida, no sospechada)

## Cambios realizados

| Patron original | Correccion | Fingerprint |
|---|---|---|
| "What I am asking for on Friday 11 September: the 34 documents of Table 1...; the 12 of Table 2...; the corrected title block...; and the seven deliverables of Table 4." (78 palabras, 3 punto y coma) | Cuatro oraciones sueltas, que es la forma que ya tenia el correo de auditoria y que midio VERDE | U-03, punto y coma |
| "the oldest four are 267, from Transmittal N1 of 16 December 2025" | "...are 267 (from Transmittal N1 of 16 December 2025)" | densidad de parentesis |
| "its committed issue date that same day in the DDSR" | "...in the Document and Drawing Status Report (DDSR)" | densidad de parentesis, y la sigla queda introducida antes de usarse |

## Re-evaluacion

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida]
VERDE | 0% | Confianza: Alta
Estilo personal: Aplicado — Caso A (solo el parrafo reescrito; el resto hereda la voz ya validada del correo de auditoria)
Registro: **primera persona**, calibrado contra la seccion 11.1 del perfil y contra el par de control de correos realmente enviados. Es deliberado: el argumento del correo es que quien reclama la emision es quien aprobo los documentos, y eso se pierde en tercera persona. El transmittal adjunto se queda en tercera persona institucional.

### Estilometria contra el par de control

El perfil esta medido en espanol, de modo que la banda la fijan los correos realmente
enviados y el borrador de auditoria que ya paso el gate.

| Rasgo | Antes | **Final** | Auditoria | N38 enviado | Perfil 11.1 |
|---|---|---|---|---|---|
| palabras de prosa | 411 | **419** | 627 | 249 | — |
| mediana de oracion | 15,5 | **15,5** | 18,5 | 13,0 | 18 |
| percentil 90 | 34,2 | **29,5** | 35,1 | 29,6 | 35 |
| oracion mas larga | **78** | **36** | 43 | 33 | — |
| sobre 30 palabras | 13,6 % | **11,5 %** | 17,6 % | 6,7 % | 14,3 % |
| punto y coma | **3** | **0** | 0 | 1 | 0 |
| parentesis /mil | 2,43 | **7,16** | 6,38 | 4,02 | 6,18 |
| em dash | 1 | **1** | 0 | 1 | 0 |
| comas por oracion | 0,82 | **0,65** | 0,88 | 0,87 | — |

**Los dos rasgos que no calzan con el perfil, y por que se aceptan:**

- **Mediana 15,5 contra 18 del perfil.** El correo cae entre el de auditoria (18,5) y el del
  N38 realmente enviado (13,0), y hace las dos cosas que esos dos hacian por separado. El
  par de control real manda sobre el perfil, que esta medido en espanol.
- **Un em dash.** Es el del codigo de respuesta, "2 — Approved as noted", que es convencion
  del proyecto y aparece igual en el correo del N38 enviado. No es insercion parentetica, de
  modo que U-10 no aplica.

Barridos duros sobre el **documento emitido**, no sobre el script: cero simbolo de seccion,
cero castellano en el cuerpo (las dos unicas apariciones son el apellido Gonzalez y el
placeholder del enlace, que se reemplaza antes de enviar), cero frases-firma, cero hedging.

## Cambio posterior de tono, por decision del usuario

Despues del VERDE, el usuario pidio suavizar el parrafo de la regla: *"hazlo mas suave y
directo, me interesa que entreguen"*. Es una correccion de **registro**, no de fingerprint,
y ninguna medicion la habria detectado: el parrafo estaba limpio de marcadores y aun asi
leia como un "te agarre".

| Antes | Despues |
|---|---|
| "The rule I am asking you to apply is your own." | "The criterion is already agreed, and BW Water set it out first." |
| "...BW Water replied to ADASA:" | "...document P22-DWG-09-007-003 of 12 May 2026:" |
| "That drawing has been Code 1 since 11 June. It is now on Rev F and its title block still reads ISSUED FOR APPROVAL." | "That is what I am asking for now, with a date." |

El hecho suprimido no se perdio: vive en la Seccion 3 del transmittal. **El correo persuade
y el transmittal deja constancia**, y eso permite bajar el tono del primero sin perder nada.

Estilometria tras el cambio, sobre 404 palabras: mediana **16,0** (antes 15,5), percentil 90
**28,8**, oracion mas larga **36**, punto y coma **0**, parentesis **7,43 por mil**, un em
dash, el del codigo de respuesta. Todo en banda; el veredicto VERDE se mantiene.

### Rendimiento del analisis

Fingerprints mas efectivos: U-03 y la densidad de punto y coma del perfil, que no es un
fingerprint de la skill sino un rasgo medido del autor y aqui fue el que mas rindio.
No aplicables: U-04 y U-06 (seis parrafos sin estructura repetida), U-10 (el unico em dash
es de convencion), U-12.
Checklist A, 19 pasos aplicables de 19.
Nota para correos futuros del mismo tipo: al fundir dos correos, el defecto previsible
aparece justo en la costura, donde una enumeracion que antes era una tabla se convierte en
prosa. Buscar la oracion mas larga primero, que ahi esta.
