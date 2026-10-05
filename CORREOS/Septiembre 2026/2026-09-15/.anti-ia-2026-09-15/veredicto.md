# Veredicto anti-ia — Respuesta a BW Water sobre el addendum de izaje (versión ejecutiva)

Documento: `2026-09-15_Lifting-Addendum-Reply.docx` (224 palabras de cuerpo, inglés, correspondencia de proyecto)
Fecha: 2026-09-15 | Modo: revisar, con redacción en la voz del registro 11.1 a pedido del usuario

## Veredicto del original

El original de esta pasada es la versión de 432 palabras, que ya había salido VERDE esa misma mañana tras corregir CL-22, CL-24 y una viñeta de 46 palabras.

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó el asistente sobre Claude Opus 5 en esta sesión]
Familias cargadas en detalle: universales U-01 a U-12 completos; Claude CL-01 a CL-25 completos, con foco en CL-19/20/21 (Opus 5, modelo autor) y CL-22 a CL-25.
VERDE | 2% | Confianza: Media
Pre-filtro: Activado (Q3 vocabulario técnico normalizado, Q4 formato de correspondencia del proyecto) | Checklist: A | Pasos evaluados: 11/19
Base de detección: técnicas estadísticas propias, sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave:**

- **CL-19 en el límite, y es lo que el usuario leyó como falta de ejecutividad.** Dos bloques se podían borrar sin perder ningún pedido: la aritmética del peso vacío (suma de la Figura 16 dividida por 2,0) y el pedido de código propio para el addendum. La lista de contenido mínimo repetía en detalle lo que los tres entregables de la ET ya nombran.
- **Sin fingerprints críticos.** U-01 a U-06 en cero, barridos duros en cero.

**Fingerprints detectados:** CL-19 (borde, 2 %).
**Modelo autor:** Claude Opus 5 (autoría conocida, no sospechada).

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| Aritmética del peso vacío, 100,80 kN | Fuera. Basta decir que la Figura 16 repite las reacciones del Rev 0 | CL-19 |
| Pedido de código propio para el addendum | Fuera, a la Sección 3 del próximo transmittal | CL-19 |
| Lista de contenido mínimo en tres viñetas (yugo, plano de izaje, memoria) | Dos oraciones: plano de fabricación del yugo y verificación local pendiente | CL-19 |
| Plazo con embarque del 28 y reserva de derechos | Plazo ligado solo a la Sección 7, pág. 30. La reserva sigue en el hilo desde el 11-Sep | CL-19 |
| Traducción larga de los entregables con "The Plant Erection Manual, … in the original" | Entregable corto en inglés y cita literal | CL-19 |
| Primer borrador ejecutivo abría con "Thank you for the addendum." (5 palabras) y "The addendum does not complete the package." (7) | Apertura directa en el hecho, y la afirmación unida a su prueba con "because" | voz 11.1 |

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida]
VERDE | 0% | Confianza: Baja (texto bajo 300 palabras)
Estilo personal: Aplicado — Caso B (documento completo, reescrito en la voz del registro 11.1)
Registro: calibrado, correspondencia de proyecto (`estilo-personal.md` sección 11.1), primera persona como en los correos anteriores de esta cadena.
Estilometría (`estilometria.py` sobre el `.docx`, que mide la prosa y excluye viñetas), contra el perfil 11.1:

| Rasgo | 432 palabras | Primer borrador ejecutivo | Final | Perfil 11.1 |
|---|---|---|---|---|
| mediana de oración | 19 | 15,5 | 20,5 | 18 |
| percentil 90 | 27,7 | 28,1 | 30,7 | 35 |
| oraciones sobre 30 palabras | 10,0 % | 0 % | 12,5 % | 14,3 % |
| oraciones bajo 8 palabras | 0 % | 20 % | 0 % | sin dato propio |
| paréntesis por mil | 5,5 | 5,8 | 5,9 | 6,18 |
| punto y coma | 0 | 0 | 0 | 0 |
| em dash | 0 | 0 | 0 | 0 |

Contando también las viñetas, la versión final tiene 11 oraciones con mediana 17 y máximo 37. Impersonal "se" y conectores del perfil no aplican en inglés, salvo "because", que es el "debido a" del perfil.

**Fingerprints detectados:** Ninguno.

- **CL-19 resuelto.** 224 palabras, cinco movimientos, cada uno con un pedido o la prueba de uno. Sin recapitulación de los correos del 10, 11 y 14.
- **U-09 revisado y aceptado.** *lifting* aparece 7 veces y *izaje* 4, todas dentro de nombres de entregables y citas literales de la ET.
- **CL-24 descartado.** Solo el párrafo del plazo abre en negrita, uno de cinco.
- **CL-25 descartado.** Dos dos puntos: la introducción de la lista de la ET y la del contenido del plano del yugo.
- **CL-22 y CL-23 descartados.** Sin aperturas escindidas ni colas de relativo.
- **U-01 descartado.** *"we cannot build it from this document"* es negación simple, sin contraste con un Y.
- **Chequeo de voz.** Los cinco rasgos medibles quedan en banda. El registro 11.1 cierra con "Quedo atento". Esta cadena en inglés nunca lo usó y se mantiene su cierre, porque traducirlo agregaría una fórmula que el correo no necesita.

### Barridos duros sobre el documento

Cero símbolo de sección, cero grafía británica, cero antítesis *not… but*, cero *endorse / Chilean / registered*, cero *previous email*, cero *maneuver*, cero punto y coma en el cuerpo, cero em dash, cero apertura escindida, cero cola de relativo y cero "Cálculo" con tilde. El único punto y coma del documento está en la línea CC del encabezado, que separa destinatarios.

### Rendimiento del análisis

Fingerprints más efectivos: CL-19, que explica el pedido de ejecutividad del usuario, y la estilometría contra el registro 11.1, que detectó que recortar dejaba oraciones de apertura demasiado cortas.
No aplicables: U-04, U-06, U-07, U-08, CL-09, CL-11, CL-14, CL-17, CL-18 (texto corto, sin secciones ni metáforas).
Checklist A, 11 pasos aplicables de 19 (C1, C2, C4, C8, C10, C13, C14, C15, C16, C17, C18).
Consenso semiótico: 4/4 niveles coinciden en la re-evaluación.
Nota para correos futuros del mismo tipo: al ejecutivizar, el recorte deja oraciones de 5 a 7 palabras al inicio y la mediana cae bajo el perfil. Se corrige uniendo la afirmación con su prueba, sin agregar palabras.
