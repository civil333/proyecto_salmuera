# Veredicto anti-ia — P22-TM-09-000-040-0_TRANSMITTAL.md (revisar)

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, el texto lo redactó Claude Fable 5.1 en esta sesión]
**VERDE** | 4% | Confianza: Media
Pre-filtro: Activado (PF-3 documento técnico-normativo con vocabulario estandarizado; inglés institucional en tercera persona) | Checklist: B | Pasos evaluados: 12/17 (5 no aplican: código, fórmulas, comandos, tolerancias numéricas propias, versionado de software)
Base de detección: técnicas estadísticas propias (conteo de oraciones, densidad de signos, barrido de frases-firma); señal, no prueba (R-09)

**Hallazgos clave:**
- U-03 (oraciones de más de 50 palabras): activado en el borrador con cinco oraciones de 51 a 83 palabras (bullets 1 y 3 del Executive Summary, Status y Action de la 2.1, Status de la 2.4). Corregidas partiéndolas; la versión emitida mide 71 oraciones, mediana 13, máximo 50, ninguna sobre 50.
- CL-24 (rótulo en negrita al abrir el párrafo) y CL-25 (dos puntos explicativos, 0,42 por oración): presentes por el formato del transmittal (`Status.`, `Action ...:`), que es plantilla del proyecto desde el N27 y no elección del texto. No se corrigen.
- U-10 / CL-13 (em dash): 18 apariciones, todas en títulos de subsección, en la línea de veredicto y en los leads de acción (`Code 3 —`, `Rev A —`, `Action —`), ninguna como inserción parentética en prosa. No activa.
- U-01, U-02, U-05, U-11, U-12, CL-01, CL-05, CL-19, CL-20, CL-21: sin instancias. `The code is 1 and not 3 because...` es declaración exigida por la regla del proyecto para una Rev 0 en Código 1, no antítesis retórica.
- U-09 (repetición léxica): `approved` 22 veces en 1.240 palabras; registro técnico con vocabulario fijado por el ITP y la ET (PF-3), no penaliza.

**Fingerprints detectados:** U-03 (corregido antes de emitir). Ninguno vigente.
**Modelo:** Claude Fable 5.1 (autoría conocida).

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| Bullet 1 del Executive Summary, 73 palabras con dos puntos | Dos oraciones: la cita contractual y la descripción de las diez páginas | U-03 |
| Bullet 3, 51 palabras | Dos oraciones: la delegación del ITP y la devolución del procedimiento | U-03 |
| Status 2.1, 83 palabras en una enumeración | Cuatro oraciones | U-03 |
| Action 2.1, 68 palabras | Dos oraciones | U-03 |
| Status 2.4, 50 palabras con dos puntos | Dos oraciones | U-03 |

## Estilo personal

No aplicado. El documento es un transmittal institucional de ADASA en inglés y tercera persona; el perfil `estilo-personal.md` mide prosa analítica en español y su sección 11.1 reserva la primera persona a la correspondencia, que aquí es el correo de cobertura y no el transmittal. Registro: no calibrado para inglés. Estilometría: mediana de oración 13 palabras (perfil 22), máximo 50; punto y coma 0; em dash 0 en prosa; sin paréntesis explicativos fuera de los códigos de documento.

## Rendimiento del análisis
Fingerprints más efectivos: U-03 (único activado). No aplicables al tipo: CL-17, CL-18 (narrativa y metáfora), U-06 y U-07 (la numeración la impone el template), CL-03 (los paréntesis son códigos de documento).
Checklist: B — pasos aplicables: 12 de 17.
Consenso semiótico: léxico, sintaxis y estructura coinciden en registro técnico institucional (3 de 4; el nivel pragmático no se mide en un documento de formato fijo).
Nota para evaluaciones futuras del mismo tipo: en los transmittals el único fingerprint que se activa de forma recurrente es U-03 en los Status y Actions de los documentos Código 3; conviene medir las oraciones antes de generar el Word, no después.
