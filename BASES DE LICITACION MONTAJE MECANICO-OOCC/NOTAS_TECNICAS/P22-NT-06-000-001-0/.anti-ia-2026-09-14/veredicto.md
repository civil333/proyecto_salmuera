# Veredicto anti-ia — P22-NT-06-000-001-0, párrafos nuevos del 14-09-2026

Documento: `P22-NT-06-000-001-0_Ingenieria-Vigente-para-Construccion.md`, sección Contenido del paquete.
Alcance: solo los tres párrafos agregados hoy (4. SITIO, 5. EQUIPOS y el párrafo de formatos), unas 250 palabras. El resto de la nota tiene su veredicto en `.anti-ia-2026-09-10/`.

## Evaluación del original

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=[37 de 63] | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida, texto redactado por Claude Opus 5 en esta sesión]
VERDE | 0% | Confianza: Baja (menos de 300 palabras)
Pre-filtro: Activado (Q3 vocabulario técnico estandarizado, Q4 formato institucional de nota técnica) | Checklist: B | Pasos evaluados: fingerprints universales y Claude
Base de detección: técnicas estadísticas propias — sin verificador oficial validado; señal, no prueba (R-09)

**Hallazgos clave:**
- CL-25 cerca del umbral: dos dos puntos explicativos ("de abril de 2026: el plano de monografía", "los emitió: todos en PDF"), 8 por mil palabras contra umbral de 10. El perfil reserva los dos puntos a listas y rótulos. El de "planos de fundación: PA-1 en ..." introduce enumeración y no cuenta.
- U-09 y U-04 no activan: "plano" se repite por ser el objeto técnico (checklist B tolera vocabulario de dominio) y la secuencia "X lleva el plano" replica el patrón del párrafo 1. ING. DETALLE MECANICA, escrito antes con la misma construcción.
- CL-24 no activa: el rótulo en negrita es el nombre de carpeta, convención de toda la sección (seis de unos sesenta párrafos de prosa de la nota).
- CL-23 no activa: ", que cubre VR-06-001 y VR-06-003" agrega dato, no glosa.

**Fingerprints detectados:** Ninguno sobre umbral
**Modelo sospechado:** Claude (autoría conocida)

## Cambios realizados

| Patrón original | Corrección | Fingerprint |
|---|---|---|
| "El levantamiento del sitio de abril de 2026: el plano de monografía, en PDF y en DWG, y el ortomosaico" | "El levantamiento del sitio de abril de 2026, con el plano de monografía en PDF y en DWG y el ortomosaico" | CL-25 (optimización) |
| "los emitió: todos en PDF y el plano de la bomba además en DWG" | "los emitió, todos en PDF y el plano de la bomba además en DWG" | CL-25 (optimización) |

Aplicado en el `.md` y en `crear_nota_tecnica_montaje.py`.

## Re-evaluación

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=[37 de 63] | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoría conocida Claude Opus 5]
VERDE | 0% | Confianza: Baja
Estilo personal: Aplicado — Caso A (solo secciones reescritas; el resto de la sección ya estaba en la voz del autor y los párrafos nuevos replican su construcción)
Registro: calibrado (nota técnica a contratista, impersonal)
Estilometría: el `.md` va con salto de línea físico, por lo que `estilometria.py` cuenta líneas como párrafos y corta oraciones. Párrafos nuevos: cero em dash, cero punto y coma, cero paréntesis (nota completa 5,7 por mil), un impersonal "se", oración máxima de 20 palabras. La nota completa conserva 31 impersonales y "según" como conector dominante.
Persistido en: NOTAS_TECNICAS/P22-NT-06-000-001-0/.anti-ia-2026-09-14/veredicto.md

### Rendimiento del análisis
Fingerprints más efectivos: CL-25 (única señal cercana a umbral)
Fingerprints no aplicables: U-06, U-07, CL-15 a CL-18 (texto descriptivo de inventario)
Checklist: B
Nota para evaluaciones futuras del mismo tipo: en párrafos de inventario de carpetas la repetición de "lleva" y del sustantivo técnico es propia del género; no leerla como U-09.
