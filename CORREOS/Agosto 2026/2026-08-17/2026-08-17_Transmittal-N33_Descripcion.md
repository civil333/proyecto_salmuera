---
titulo: "Correo de cobertura del Transmittal N33 — submittals 25007-0076, 25007-0078 y 25007-0079"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-08-17
---

# Correo de cobertura del Transmittal N33

**Estado: ENVIADO** — lunes 17-Ago-2026, registrado a las **12:17 de Chile (16:17 en Penang)**. La hora exacta se confirma con el respaldo del enviado.

> **Con esto queda emitido el Transmittal N33.** Los cinco documentos de las entregas 76, 78 y 79 tienen respuesta formal, y los plazos de la Cláusula 37.2 (24 y 26 de agosto) se cumplieron con holgura.

| Campo | Valor |
|---|---|
| Archivo | `2026-08-17_Transmittal-N33.docx` · una página · inglés · **199 palabras de cuerpo** |
| Para | Allan Valentos, Eduardo Yamauchi (BW Water) |
| CC | Fitri Indriyani, Stephane Gehant, Magdier Arias, Muhammad Fadhil Bin Abdul Wahid (BW Water); Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero (ADASA) |
| Asunto | TALTAL - Transmittal N33 - submittals 25007-0076, 25007-0078 and 25007-0079 |
| Cadena | Sobre el hilo de los submittals. Cadena de transmittals, separada de la de las jornadas de inspección |
| Adjuntos | `TRANSMITTAL N33 ADASA-BW_WATER.pdf` (**cinco páginas**, sin tabla de contenidos) |
| Por enlace | Un solo `CC_ADASA`, el del plano civil |
| Script | `crear_correo_tm33.py` |

Allan Valentos va en el Para porque es quien emitió los tres Submittal Forms; Yamauchi lo acompaña por ser el destinatario principal de la cadena formal.

## Qué dice

Cuatro cosas. **No repite la sustancia del transmittal**: el detalle de cada documento vive en el adjunto.

1. **El adjunto y el veredicto en dos frases:** cinco documentos de tres submittals, veredicto 2 — Approved as noted, cuatro Código 1, un Código 2, ninguno vuelve a revisión. La frase que explica el alcance de la revisión vive en el transmittal, no acá.
2. **Las dos acciones**, las dos sobre el plano civil: el peso del contenedor vacío y la fila que contabiliza el marco del skid. Se incorporan al emitir Rev 0, sin nueva revisión del plano, y se dice explícito que **los otros cuatro documentos no requieren acción**, que es lo que el proveedor necesita saber primero.
3. **La alerta del submittal `25007-0077` ausente**, como pregunta y sin imputar: la serie salta del 0076 al 0078. Reforzada el 17-Ago con la consecuencia contractual, que es lo que le da peso: **si ese número se emitió y no llegó, la recepción formal y completa nunca ocurrió**, de modo que los siete días hábiles de la Cláusula 37.2 no han empezado a correr para él y su contenido no está cubierto por este transmittal. La misma frase va en la Sección 1 del transmittal.
4. **El plazo real de la Cláusula 37.2** frente a las fechas de retorno de los Submittal Forms: lunes 24-Ago para el 0076 y miércoles 26 para los otros dos, contra las que pidió el proveedor, una de ellas en domingo.

**El enlace de descarga va en el cuerpo, con el nombre del archivo.** Se cayó del cuerpo en el N30, en el N31 y en el N32. Enlace publicado el 17-Ago: `https://lrg.synology.me:6501/d/s/19Vh5BdPy7Bawfney5aMrUV8sZlaFy99/hGVtoOjNlRe8KS3GBP2Ek-22F4fX0UUP-4rJA83s3bw0`. Verificado sobre el texto extraído del `.docx` y no sobre el script, que es donde estaba el modo de falla.

**Lo que la alerta NO dice, a propósito:** que es la segunda vez, por el `25007-0073` ausente. Ese caso es más turbio — la carpeta `ENTREGA 73` contiene el 0074 y su correo nunca pasó por la captura de `_RECIBIDOS`, que está en HOLD, así que la causa pudo ser de este lado. Afirmar un patrón sobre esa base es refutable, y el antecedente queda en el README.

## Qué salió del correo en el re-alcance del 17-Ago

El párrafo que adelantaba **el diámetro de los pernos de anclaje**. Ese punto, como todo lo que salía del contenido nuevo que los planos agregaron, no es materia de este transmittal: la ingeniería de obras civiles la ejecuta L&A y esas divergencias se ven con ellos. Vive en el compromiso `INT-11`.

También salieron, respecto de la primera versión del correo, la mención a los dos valores vinculantes y las cuatro viñetas de PDF anotados, que ahora es una sola.

## Métricas y auditoría anti-IA

**199 palabras de cuerpo** · 13 oraciones · máxima de 32 palabras · sigma 9,4 · cero símbolo de sección · cero "letter". Venía de 293 antes del recorte ejecutivo del 17-Ago. Los em dash son separadores de la línea de veredicto y de la viñeta del archivo, que es la convención del proyecto.

**Transmittal:** **cinco páginas y 1.138 palabras**, sin tabla de contenidos, exportado desde Word real. Venía de diez al retirar las observaciones nuevas, de siete al comprimir los Status de la Sección 2, y de seis al sacar el índice. `anti-ia` modo revisar, checklist B: **VERDE**, familias universales y Claude, sin fingerprints críticos. Las oraciones largas que arroja el barrido son los bloques `Action` y la línea `Also open`, que el CLAUDE.md pide como una sola frase.

## Checklist pre-envío

- [x] Inglés íntegro, sin símbolo de sección, sin "letter", sin códigos internos ni mención a Van Doorn
- [x] Días de la semana verificados: 24-Ago lunes, 26-Ago miércoles, y la fecha de retorno del 0076 cae domingo
- [x] Metadatos Word limpios (autor Luis Rivera Gonzalez, company Aguas Antofagasta, en-US)
- [x] PDF del transmittal de **cinco páginas** desde Word real, con el veredicto en la página 2
- [x] Un solo `CC_ADASA` en la Sección 4 y en el cuerpo del correo; los tres retirados están en `_analisis_no_anotado/`
- [x] **Enlace real de Synology** en `crear_transmittal.py` y en `crear_correo_tm33.py`, los dos regenerados. Verificado sobre el texto extraído: está en el cuerpo del correo con el token completo, y en el PDF del transmittal como hipervínculo activo
- [x] Alerta del `25007-0077` reforzada con la consecuencia de la Cláusula 37.2, en el correo y en la Sección 1 del transmittal
- [x] **Sin tabla de contenidos**, por decisión del 17-Ago: un índice de cinco títulos gastaba una página entera. Desviación puntual de la Sección 3.1 del CLAUDE.md, anotada en el script; la regla no cambia para los próximos
- [x] Estado a ENVIADO acá, en el README y en la memoria del TM N33
- [ ] **Abrir el enlace y confirmar que muestra el `CC_ADASA` del plano civil.** Es la única verificación que queda con consecuencia: si la carpeta está vacía, BW Water recibió una ruta muerta y hay que reenviar el archivo
- [ ] **Verificar sobre el respaldo del enviado que el párrafo del enlace y la viñeta del archivo viajaron.** Se cayeron en el N30, el N31 y el N32, y es lo que este correo vino a corregir
- [ ] **Archivar el respaldo del enviado en esta carpeta**, con la hora exacta

## Contexto Interno (No enviar)

- **Cuatro Código 1 en un ciclo es inédito en este proyecto.** El proveedor va a leerlo así, y es correcto que lo lea así: los tres documentos que cerraron sus comentarios previos los cerraron de verdad, verificados contra la fuente y no contra su hoja de comentarios.
- **Lo que se retiró no desapareció.** Los ledgers de las tres entregas registran cada punto con su evidencia. La conversación con L&A tiene su propio compromiso (`INT-11`) y el mapeo de sensores de la bomba de alta el suyo (`INT-12`), atado al cierre del ciclo del HMI.
- **El correo no menciona el mapeo de sensores ni la lectura equivocada del TM N31.** Es la decisión del re-alcance: un documento en Rev 1 no recibe comentarios nuevos, y esa página la aprobó el propio TM N31.
