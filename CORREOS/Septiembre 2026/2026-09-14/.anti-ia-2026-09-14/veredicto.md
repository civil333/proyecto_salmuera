# Veredicto anti-ia — Recordatorio a BW Water del paquete de izaje

Documento: `2026-09-14_Lifting-Package-Reminder.docx` (106 palabras de cuerpo, inglés, correspondencia de proyecto)
Fecha: 2026-09-14 | Modo: revisar

## Veredicto del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
Familias cargadas en detalle: universales U-01 a U-12 completos; Claude CL-01 a CL-25 completos, con foco en CL-19/20/21 (Opus 5, modelo autor) y CL-22 a CL-25.
VERDE | 0% | Confianza: Baja
Pre-filtro: Activado (Q3 vocabulario técnico normalizado) | Checklist: A | Pasos evaluados: 9/19 (evaluación cualitativa, el texto está bajo 300 palabras)
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave, ninguno activa un fingerprint:**

- **U-03 y C2 dentro de rango.** Oración más larga de 37 palabras (la de los dos puntos abiertos), bajo el umbral de alerta de 40. Ritmo 17, 11, 37, 5, 24 y 12 palabras, con la oración corta de anclaje *"Please confirm both before then."* conectada al contenido.
- **U-09 en el límite sin superarlo.** *lifting* y *package* aparecen tres veces cada una; son el objeto del correo y el umbral activa sobre tres.
- **CL-19, CL-20 y CL-21 sin señal.** Sin resumen, sin anuncio de intención, sin verificación declarada y sin alcance agregado: el cuerpo trae solo lo que el usuario pidió (recordar, pedir respuesta, enlace de la reunión).
- **CL-23 revisado y descartado.** *", which needs to be on Wednesday 16 September at the usual time"* es un relativo que carga el requisito, no una glosa que reinterprete el dato.
- **CL-25 descartado.** El único dos puntos introduce la enumeración de las dos confirmaciones pendientes.
- **CL-24 no aplica.** La oración en negrita va dentro del párrafo, no lo abre.

**Fingerprints detectados:** Ninguno.
**Modelo autor:** Claude Opus 5 (autoría conocida, no sospechada).

### Chequeo de voz contra el registro 11.1

| Rasgo | Correo | Perfil 11.1 | Lectura |
|---|---|---|---|
| mediana de oración | 14,5 | 18 | bajo el perfil, en el nivel del par de control de esta serie (N38 enviado 13, N39 enviado 16, según el veredicto del 11-Sep) |
| percentil 90 | 30,5 | 35 | en banda |
| oraciones sobre 30 palabras | 16,7 % (1 de 6) | 14,3 % | en banda a la resolución de seis oraciones |
| punto y coma | 0 | 0 | en banda |
| paréntesis por mil | 0 | 6,18 | no medible: en 106 palabras un solo paréntesis vale 9,4 por mil, y el correo no tiene aclaración lateral que lo justifique |
| em dash | 0 | 0 | en banda |
| primera persona | sí | domina | en banda |

Con seis oraciones la mediana y la densidad de paréntesis no son estables, y los dos rasgos que se apartan lo hacen por granularidad y no por voz. **Caso A**: voz propia, sin reescritura. Forzar un paréntesis o alargar oraciones para calzar el perfil agregaría relleno, que es justo lo que CL-19 penaliza en el modelo autor.

## Cambios realizados

Ninguno. El texto evaluado es el que queda.

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Baja
Estilo personal: Aplicado — Caso A (redactado directamente en la voz del registro 11.1; sin secciones reescritas)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1), primera persona como en los correos anteriores de esta cadena.
Estilometría: mediana 14,5 contra 18; percentil 90 30,5 contra 35; paréntesis 0 contra 6,18 (no medible a este largo); impersonal "se" y conectores del perfil no aplican en inglés; mediana de párrafo 53; antes y después iguales, sin cambios.

### Barridos duros sobre el documento

Cero símbolo de sección, cero grafía británica (*centre, metre, modelled, analyse, organise, colour*), cero antítesis *not… but*, cero *endorse / Chilean / registered*, cero *previous email*, cero *letter*, cero punto y coma, cero em dash, cero apertura escindida.

### Rendimiento del análisis

Fingerprints más efectivos: ninguno activó; los que más discriminaron fueron U-03, U-09 y CL-23, que quedaron en el límite y obligaron a revisar la oración de 37 palabras y el relativo del segundo párrafo.
No aplicables: U-04, U-06, U-07, U-08, CL-09, CL-11, CL-14, CL-17, CL-18 (texto corto, sin secciones ni metáforas).
Checklist A, 9 pasos aplicables de 19 (C1, C2, C4, C10, C13, C14, C15, C17, C18).
Consenso semiótico: 4/4 niveles coinciden (léxico, sintáctico, discursivo, pragmático).
Nota para correos futuros del mismo tipo: en un recordatorio de dos párrafos la estilometría contra el perfil no discrimina; lo que decide es no agregar recapitulación del correo previo, que es el modo de fallo de Opus 5.
