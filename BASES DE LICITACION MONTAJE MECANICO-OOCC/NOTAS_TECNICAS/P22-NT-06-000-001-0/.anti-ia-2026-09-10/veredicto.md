# Veredicto anti-ia — NT P22-NT-06-000-001-0, revision del 10-09-2026

Fecha: 10-09-2026. Documento evaluado: el `.md` fuente de la Nota Tecnica tras incorporar la
ENTREGA 15 de L&A y los nativos DWG. Se reescribieron seis parrafos (objeto, contenido del paquete,
formatos, sistema CIP, movimiento de tierra y partidas); el resto es el texto que paso VERDE el
04-09-2026 y no se toco.

## Veredicto

Cobertura: modo=revisar | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto Claude Fable 5.1 en esta sesion sobre un borrador de Claude Opus 5]
VERDE | Confianza: Alta
Pre-filtro: no activado | Checklist: A (proposito analitico-declarativo) | Registro: prosa normativa, calibrado en el perfil
Base de deteccion: tecnicas estadisticas propias mas medicion estilometrica reproducible; senal, no prueba (R-09)

**Hallazgos clave:**

- Barrido de frases prohibidas y de los universales U-01 a U-12 sobre el documento completo:
  cero coincidencias (sin antitesis "no es X sino Y", sin auto-referencia del texto, sin
  auto-valoracion de hallazgos, sin hedging, sin em dash, sin punto y coma).
- Fingerprints de Claude sobre los parrafos nuevos (CL-19 inflacion de extension, CL-22 apertura
  escindida, CL-23 a CL-25): ninguno. Los parrafos nuevos abren con el sustantivo tecnico o con
  el impersonal ("Cada plano va en PDF...", "El fondo de excavacion se lleva...", "Los rellenos
  del trazado no cambian...").
- Dos oraciones sobre 50 palabras (65 y 52), ambas del texto del 04-09 ya aceptado: el objeto
  de la nota y la que enumera los codigos repetidos del Formato. No se tocaron.
- Sin ornamento: 0 candidatas en 77 oraciones.

**Fingerprints detectados:** ninguno.
**Modelo autor:** Claude Fable 5.1 sobre borrador de Opus 5 (autoria conocida, no sospechada).

## Contraste estilometrico contra el perfil (medido sobre el .docx, que filtra tablas y rotulos)

| Rasgo | Perfil, prosa analitica | NT 04-09 | NT 10-09 | Juicio |
|---|---|---|---|---|
| Mediana de oracion | 22 palabras | 20,0 | 19,0 | en rango |
| Percentil 90 de oracion | 43 | 40,4 | 33,8 | algo bajo |
| Oraciones sobre 30 palabras | 26,3% | 20,0% | 16,9% | algo bajo |
| Oraciones bajo 8 palabras | 5,6% | 2,0% | 3,9% | en rango |
| Punto y coma | 0 | 0 | 0 | calza |
| Em dash | 0 | 0 | 0 | calza |
| Parentesis por mil palabras | 5,06 | 6,39 | 5,07 | calza |
| Impersonal "se" por mil | ~25 | 24,3 | 19,0 | algo bajo |
| "segun" por mil | >1,5 | - | 3,2 | calza |
| "debido a" por mil | >1,5 | - | 1,9 | calza |
| Mediana de parrafo | 28 palabras | 38,5 | 41,0 | alto, propio de prosa normativa con tablas |

Estilo personal: Aplicado, Caso A (solo los parrafos reescritos; el empalme con los originales
se verifico leyendo). Voz propia. Registro calibrado (estilo-personal.md 11.3, prosa normativa).

## Rendimiento del Analisis
Fingerprints mas efectivos: barrido U-01/U-02B/U-12 y CL-22 por lectura de aperturas.
Fingerprints no aplicables: los de listas y bullets (el documento es prosa con tablas).
Checklist: A. Consenso semiotico: 4/4 niveles sin senal.
Nota: `estilometria.py` sobre el `.md` da mediana 11 porque cuenta las celdas de tabla y las
lineas cortadas a 100 caracteres como oraciones; medir sobre el `.docx`.
