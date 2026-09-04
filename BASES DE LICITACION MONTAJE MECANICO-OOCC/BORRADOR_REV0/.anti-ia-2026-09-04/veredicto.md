# Veredicto anti-ia — modo smoke

Documento: `BL_MONTAJE_TALTAL_REV1.md`, prosa nueva de la revision 1 (1.019 palabras, 55 oraciones).
Fecha: 04-09-2026.

## Veredicto

Cobertura: modo=smoke | familias=[universales, claude] | IDs evaluados=37 de 63 | omitidas=[gpt, gpt5, gemini, llama, deepseek, grok: autoria conocida, el texto lo redacto Claude Opus 5 en esta sesion, de modo que la familia del autor es Claude y las demas no aplican]

**VERDE Express** | 0 puntos de 45 posibles | Confianza: Media
Pre-filtro: activado en PF-3 (documento tecnico de ingenieria con vocabulario estandarizado). PF-1, PF-2 y PF-4 negativos.
Checklist: express de 9 items | Pasos evaluados: 8 de 9 aplicables
Base de deteccion: tecnicas estadisticas propias, sin verificador oficial validado. Senal, no prueba (R-09).

## Hoja de trabajo

| Paso | Hallazgo | Puntos |
|---|---|---|
| 1 — Gestaltico | Prosa tecnica declarativa, densa en datos verificables: codigos de plano, cotas, revisiones y cifras de cubicacion con su fuente. Impresion: legitima para el genero | orientador |
| 2 — U-01 antitesis y U-02 colapso modal | Cero instancias de "no es X sino Y", "no se trata de", "no basta con", "paradoja" o "tension". Los parrafos varian entre dos y cinco oraciones | 0 |
| 3 — U-03 oraciones largas | Maximo 38 palabras. Cero oraciones sobre 50 y cero entre 40 y 50 | 0 |
| 4 — Burstiness | Mediana 17 palabras, percentil 90 en 34, seis oraciones bajo ocho palabras sobre 55. Variacion perceptible | 0 |
| 5 — Conocimiento situado | Abundante y verificable contra fuente primaria: cotas +6,300 y +5,400, cuatro cotas de tie-in, 2,63 y 5,80 metros cubicos, diez pedestales de 1,00 por 1,00 m, inserto INS-1, codigos de lamina | −5 |
| 6 — Marcadores humanos | Sin errores de concordancia, regionalismos ni fatiga final. No se acredita autoria humana y no corresponde puntuar a favor | 0 |
| 7 — Diversidad lexica | Cero apariciones de las once palabras de la lista de alerta (importante, relevante, significativo, crucial, fundamental, clave, esencial, permite, busca, facilita, promueve) | 0 |
| 8 — Familia del autor, Claude Opus 5 | CL-01 hedging y CL-08 "si bien" en cero. CL-20 y CL-21 no activan. **CL-19 activa de forma leve**: el parrafo del peso del contenedor agrega una clausula de encuadre ("Esta cifra es informacion de contexto para el contratista") que el documento no exigia | +1 |
| 9 — Score | −4, que se normaliza a 0. Coincide con la impresion gestaltica del paso 1 | **0** |

**Fingerprints detectados:** CL-19 en grado leve, una instancia.
**Modelo autor:** Claude Opus 5 (autoria conocida, no sospechada).

## Sin correcciones requeridas

### Optimizaciones opcionales, no requeridas
- **CL-19**: la clausula "Esta cifra es informacion de contexto para el contratista" del parrafo de pesos de la Seccion 6.4 se puede borrar sin que el parrafo pierda nada, porque la frase siguiente ya dice que las fundaciones estan dimensionadas en los planos del Anexo A2. Se mantiene a proposito: en un documento de licitacion evita que el oferente lea la cifra de peso como un dato de diseño a su cargo.

## Rendimiento del analisis

Fingerprints mas efectivos: ninguno detecto marcador real fuera del CL-19 leve. El barrido mecanico de U-01, U-05, U-10, U-11 y U-12 dio cero en todos.
Fingerprints no aplicables: U-06 numeracion sistematica y U-07 sistemas escalonados no aplican, porque el fragmento evaluado es prosa corrida extraida de un documento cuya numeracion la impone la plantilla corporativa.
Checklist: express — pasos aplicables 8 de 9.
Consenso semiotico: 3 de 4 niveles coincidieron (lexico, sintactico y discursivo limpios; el pragmatico aporta el unico matiz, la clausula de encuadre).
Nota para evaluaciones futuras del mismo tipo: en documentos de licitacion la prosa nueva suele ser declarativa y corta por exigencia del genero, de modo que los pasos 3 y 4 tienden a dar cero sin que eso acredite nada. El paso que discrimina es el 8, y dentro de el CL-19, porque la tentacion de explicar de mas es justamente la que aparece cuando hay que justificar un cambio de cifra frente a un tercero.
