# Veredicto anti-ia — P22-TM-09-000-042-0_TRANSMITTAL.md y cuadros de los CC_ADASA (revisar)

Corrida el 5-Oct-2026 sobre el borrador para el envío del 7-Oct.

## Evaluación del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó Claude Opus 5.5 en esta sesión]
**AMARILLO** | 9% | Confianza: Media
Pre-filtro: Activado (PF-3 documento técnico-normativo con vocabulario estandarizado; inglés institucional) | Checklist: B | Pasos evaluados: 12/17 (no aplican: código, fórmulas, comandos, tolerancias numéricas propias, versionado de software)
Base de detección: técnicas estadísticas propias (`estilometria.py`, conteo de oraciones, barrido de frases-firma); señal, no prueba (R-09)

**Hallazgos clave:**
- U-03 (oraciones de más de 50 palabras): cinco, de 51 a 71 palabras. Eran el Status y la Action de la 2.1 (paquete de izaje), la Action de la 2.2 y el párrafo "Also open" de la Sección 3.
- Punto y coma en prosa: tres ("section F; that part is accepted", "EPDM seat; only its pipe material", "Issue at Rev 0; reflect there"). El perfil mide cero. Los tres del cierre canónico "accepted; issue directly at IFC Rev 0" son formato de CLAUDE.md sección 6.3 y se conservan.
- U-02B (auto-referencia): "The re-issued documents are reviewed against the comments already raised, and no new comment is added to them." Explicaba la tabla en vez de dejarla hablar y, además, comprometía por escrito a ADASA a no levantar comentarios nuevos en reemisiones futuras.
- CL-24, variante en lista: las tres viñetas del "Why Code 3" abrían con rótulo en negrita, que el formato del proyecto no exige en esa parte (sí en "Disposition at a glance", donde se conserva).
- U-01 (antítesis): "the addendum designs the lugs and not the frame".
- Ornamento: "from a hook with nothing above it", imagen retórica fuera del perfil (umbral cero).
- CL-22 (apertura escindida): "What arrived does not allow the yoke to be fabricated".

**Fingerprints detectados:** U-03, U-02B, U-01, CL-24 (lista), CL-22, ornamento.
**Modelo:** Claude Opus 5.5 (autoría conocida).

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| Status 2.1: cuatro oraciones de 51, 51 y 52 palabras con punto y coma | Siete oraciones de 4 a 49 palabras, sin punto y coma | U-03, punto y coma |
| "What arrived does not allow the yoke to be fabricated: ..." | "The sheet received does not allow the yoke to be fabricated." + dos oraciones | CL-22, U-03 |
| Action 2.1 de 71 palabras | Cuatro oraciones | U-03 |
| Action 2.2 de 49 palabras con enumeración larga | Dos oraciones | U-03 |
| "Also open" de 53 palabras | Cuatro oraciones con su transmittal de origen | U-03 |
| "One lift of one motor, from a hook with nothing above it." | "The maintenance lifting points sheet shows the lift of one motor, with no runway beam or fixed point, and leaves out both turbochargers." | Ornamento |
| "**Lifting package.** ... designs the lugs and not the frame" | Viñeta sin rótulo; "the addendum checks only the lugs" | CL-24, U-01 |
| Frase de método sobre la tabla de levantamiento | Eliminada; queda el rótulo de la tabla | U-02B |
| Cuadro de la Valve List: "in 316L; only the pipe material column changed" | Dos oraciones | Punto y coma |
| Tres paréntesis opcionales (9.5 t, asunto del correo, Transmittal N30) | Integrados a la oración | Densidad de paréntesis 11,2 a 8,4 por mil |

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, Claude Opus 5.5]
**VERDE** | 3% | Confianza: Media
- U-03: ninguna oración sobre 50 palabras (máximo 49).
- U-10 / CL-13: ocho em dash, todos en títulos de subsección y en los encabezados canónicos (`Code 3 —`, `Action —`), ninguno como inciso en prosa. No activa.
- CL-24: los rótulos en negrita que quedan son los del formato fijo del transmittal (`Status.`, `Action ...:`, `Disposition at a glance`, cada viñeta con `<Doc> <Rev> — Code <N>.`). No se corrigen, igual que en el N40.
- CL-25: dos puntos explicativos en prosa bajo 10 por mil palabras.
- CL-19, CL-20, CL-21, U-05, U-11, U-12: sin instancias. El "Section 3 lists the pending observations" lo exige CLAUDE.md sección 3.2 y no se cuenta como auto-referencia.
- Cuadros de los CC_ADASA (9 textos, formato fijo "ID: error. Correct: action."): sin punto y coma, sin antítesis, sin valoración del hallazgo. Una sola cita por cuadro.

Estilo personal: Aplicado solo en lo transferible, Caso B acotado. El perfil `estilo-personal.md` está medido en español. Del perfil se tomaron cero em dash en prosa, cero punto y coma en prosa, cero ornamento, paréntesis para aclaraciones y referencias, cita por número de documento y sección, y ritmo sin staccato. La primera persona de la sección 11.1 corresponde al correo de cobertura, no al transmittal, que es institucional en tercera persona.
Registro: no calibrado para inglés (no hay corpus del autor en inglés). Se declara, igual que en el N40.
Estilometría (antes → después): mediana de oración 17 → 16 palabras (perfil de correspondencia 18; el formato de Status y Action fija frases cortas); p90 49,4 → 34,8 (perfil 35); oraciones sobre 30 palabras 26,5 % → 19,3 % (perfil 14,3 %); máximo 71 → 49; punto y coma 5 → 3, todos del cierre canónico; paréntesis 7,45 → 8,41 por mil (el borrador nuevo tenía 11,2 antes del ajuste; cuatro son rangos de ID exigidos por el formato); em dash en prosa 0; ornamento 0. "Según" y "debido a" e impersonal "se": no aplican en inglés.

## Rendimiento del análisis

Fingerprints más efectivos: U-03 (recurrente en los Status y Action de los Código 3, como en el N40), U-02B y el umbral de ornamento.
No aplicables al tipo: CL-17 y CL-18, U-06 y U-07 (la numeración la impone el template), U-08.
Checklist: B — pasos aplicables: 12 de 17.
Consenso semiótico: léxico, sintaxis y estructura coinciden en registro técnico institucional (3 de 4).
Nota para evaluaciones futuras del mismo tipo: la frase que explica el método de revisión de ADASA ("no new comment is added") es a la vez U-02B y un compromiso contractual no buscado. En un transmittal, la regla interna de revisión no se escribe; se aplica.

## Re-evaluación tras la verificación adversarial y el plano del yugo como documento propio (5-Oct, tarde)

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, Claude Opus 5.5]
**VERDE** | 3% | Confianza: Media
- Cambios de contenido, no de estilo: el plano del yugo tiene subsección propia (2.1); la Valve List pasó a Código 1; las eslingas piden tensión de diseño y largo; la cita del correo del 15-Sep quedó literal ("a yoke drawing to fabricate from"); "Also open" suma la línea 09-001 del N36.
- U-03: las tres oraciones nuevas de 50, 55 y 57 palabras se partieron. Máximo final 48.
- Estilometría final: mediana 18,5 palabras (perfil de correspondencia 18), p90 34,0 (perfil 35), sobre 30 palabras 16,1 % (perfil 14,3 %), paréntesis 6,7 por mil, punto y coma 3 (los del cierre canónico), em dash en prosa 0, ornamento 0.

## Re-evaluación tras perfiles nacionales, empalmes y NCh3171 (5-Oct, noche)

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, Claude Opus 5.5]
**VERDE** | 3% | Confianza: Media
- Textos nuevos en las Secciones 2.1 y 2.2, la disposición, el "Why Code 3" y dos cuadros del plano del yugo, más la OBS-02 del addendum.
- Ninguna oración sobre 50 palabras (máximo 48). Mediana 19 (perfil de correspondencia 18), p90 34,5, paréntesis 6,1 por mil. Sin punto y coma en prosa, sin em dash en prosa, sin ornamento ni antítesis.
- Los dos puntos de "cannot be fabricated from: imported W10x49 sections, ..." introducen una enumeración y no un inciso explicativo (CL-25 no aplica).

## Ajuste de numeración (5-Oct, cierre)

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, Claude Opus 5.5]
**VERDE** | 3% | Confianza: Media
- Las secciones 2.1, 2.2 y 2.3 recorren los puntos en el orden de sus IDs, y cada pedido de la Action lleva su ID: OBS-01 a OBS-05 en el plano del yugo, OBS-01 a OBS-03 en el addendum y OBS-01 y OBS-02 en Lifting Points. Máximo de oración 48 palabras. Los paréntesis suben por los IDs citados uno a uno, que son referencia numerada y no aclaración.

## Re-evaluación tras el comentario de viga intermedia, torsión y desangulación (5-Oct, cierre)

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, Claude Opus 5.5]
**VERDE** | 3% | Confianza: Media
- Textos nuevos: cuadro OBS-02 de la planta del yugo, cuadro OBS-04 del addendum, Status y Action de 2.1 y 2.2, disposición, "Why Code 3" y dos viñetas del correo.
- U-03: ninguna oración sobre 50 palabras; máximo 48 en el transmittal y 45 en el correo. Mediana 18,5, p90 33,8.
- La causalidad que no se sostiene quedó fuera. El texto no dice que la falta de viga intermedia *impida* la verificación ("so ... are not verified"). Se dejaron dos hechos coordinados: no hay viga intermedia, y la torsión y el pandeo no están verificados.
- Sin punto y coma en prosa, sin em dash en prosa, sin antítesis, sin ornamento ni valoración del hallazgo. Una sola acción por cuadro.
