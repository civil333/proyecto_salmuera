# Auditoría multi-audit — Sismo vertical TK-06-001

**Fecha:** 7 de mayo de 2026
**Revisión:** 1 (Rev 0 corregida tras verificación directa del extract NCh 2369 sobre Tabla 5.6 ítem 7.5 y alcance dual de Sección 11.8)

**Documentos auditados:**
- `P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.md` (consulta a Exfibro, Rev 0 emitida 06-May-2026; Rev 1 emitida 07-May-2026 incorpora estas conclusiones)
- `P22-IT-06-000-005-0_Revision_Memoria_TK-06-001.md` (revisión interna ADASA, Rev 0 → Rev 1 07-May-2026)

**Fuentes cruzadas:** NCh 2369 Of.2003 (norma), Memoria Estanque AFTA Taltal (Exfibro Rev A), plano EX-26005-F01-RevC.

**Modo de ejecución:** dos auditorías sintéticas en fork (la skill `multi-audit` orchestrator.py requiere `ANTHROPIC_API_KEY` separada de Claude Max; los forks ejecutaron las nueve perspectivas — DEFENSOR, NEUTRO, FISCAL, JUEZ, ESTILISTA, FACTUAL, ABOGADO DEL DIABLO, VERIFICADOR, AUDITOR SOMBRA — en pasada única contra las tres fuentes).

---

## 1. Veredicto global

**Núcleo técnico correcto. Citas normativas con dos errores confirmados. Posición ADASA defendible en el fondo, frágil en la forma — corregible sin pivote estratégico.**

| Dimensión | Estado |
|-----------|--------|
| Cifras numéricas (Cv, Ez, tb, σ, τ, áreas, momentos) | **CORRECTAS**. Reproducibles al 99,9 % contra MC Exfibro y NCh. |
| Conclusión estructural (los pernos M25 F1554 Gr.36 cumplen) | **CORRECTA**. Interacción σ+τ = 0,933 ≤ 1,0 con la combinación Sección 4.5 letra a) ASD plena (1,0·H + 1,0·V con signos ±) y τ_adm corregido a 1.011 kg/cm². |
| Diagnóstico de error en Ez declarado por Exfibro (−2.514 kg ↔ Cv ≈ 0,20 implícito) | **CORRECTO**. La diferencia 33,5 % vs ±3.357 kg es real y trazable a una posible aplicación indebida de Sección 5.6 (equipos rígidos T ≤ 0,06 s) cuando T_imp = 0,158 s. |
| Citas normativas a NCh 2369 Of.2003 | **DOS ERRORES CONFIRMADOS** (Sección 5.5.3 (inexistente) inexistente; "regla 100/30 Sección 5.5.2" fabricada). El alcance NCh 2369 al estanque PRFV es correcto en lo general (Tabla 5.6 ítem 7.5 incluye explícitamente FRP/GFRP/HDPE con R = 3); solo Sección 11.8 está restringido a acero/HA por Sección 11.8.1. |
| Posición ADASA frente a un Exfibro técnicamente preparado | **DEFENDIBLE EN EL FONDO, FRÁGIL EN LA FORMA**. Reformular las citas erróneas pero mantener la exigencia de fondo: incluir Cv en el cálculo de tracción de pernos según Sección 5.5.1 letra b) + Sección 4.5 letra a). |

> **Recomendación AUDITOR SOMBRA (consenso):** corregir las dos citas erróneas en IT-005 antes de cualquier emisión derivada y emitir CT-002 Rev 1 con nota de errata. La verificación independiente con la combinación Sección 4.5 letra a) plena (1,0·H + 1,0·V) confirma interacción σ+τ = 0,933 ≤ 1,0; los pernos cumplen con margen suficiente.

---

## 2. Hallazgos críticos comunes (consenso entre las dos auditorías)

### F-COMUN-1 — Sección 5.5.3 (inexistente) NCh 2369 Of.2003 NO EXISTE

| Doc | Frecuencia | Contexto |
|-----|------------|----------|
| IT-005 | 5+ ocurrencias (header, tabla parámetros, H1, H2, recomendaciones) | "Cv = (2/3)·Cmax según NCh 2369 Sección 5.5.3 (inexistente)" |
| CT-002 | Heredada en el desarrollo de Q3 | "factor (1−Cv) según Sección 5.5" |

**Hecho normativo:** Sección 5.5 cierra con Sección 5.5.1 (cálculo estático del Fv vertical) y Sección 5.5.2 (alternativa dinámica con espectro). **No hay Sección 5.5.3 (inexistente).** La fórmula de Cv aplicable al estanque (R = 3) es **Sección 5.5.1 letra b)**, que prescribe `Cv = (2/3)·A0/g` para los casos contemplados en Sección 5.1.1 letra c) y Sección 5.1.1 letra d). Numéricamente coincide con `(2/3)·Cmax` cuando A0/g = Cmax = 0,40, pero conceptualmente debe citarse contra A0/g, no contra Cmax.

### F-COMUN-2 — "Regla 100/30 Sección 5.5.2" es fabricación

| Doc | Frecuencia | Contexto |
|-----|------------|----------|
| IT-005 | H5, sección Re-cálculo, Caso A, recomendaciones a Exfibro | "Aplicar regla 100/30: 1,0·H ± 0,3·V (Sección 5.5.2)" |
| CT-002 | Q5 | "Sección 5.5.2 (regla 100/30: 1,0·H ± 0,3·V)" |

**Hecho normativo:**
- Sección 5.5.2 NCh 2369 trata sobre **análisis dinámico vertical alternativo con espectro** (R = 3, ξ = 0,03). No es una regla de combinación direccional.
- La regla 100/30 entre componentes **horizontales** está en Sección 5.1.2 NCh 2369 con condiciones específicas (irregularidad torsional, marcos rígidos comunes a dos líneas).
- La combinación H+V correcta en NCh 2369 para método de tensiones admisibles está en **Sección 4.5 letra a)** y exige **100 % + 100 % con signos ± para efecto desfavorable**, sin factor 30 %.
- La regla 100/30 H+V que ambos documentos ADASA citaban **proviene de ASCE 7-16 Sección 12.5.3 / API 650 Anexo E.6.1.5**, no de NCh 2369.

**Implicación práctica:** la combinación correcta es Sección 4.5 letra a) ASD plena. El recálculo con esta combinación produce tb = 1.598 kg (vs 1.537 en el caso intermedio 100/30 que aparecía en Rev 0); los pernos siguen cumpliendo con interacción 0,933.

### F-COMUN-3 — Imprecisión de redacción en cita Tabla 5.6 (NO ES ERROR)

**Aclaración tras revisión Rev 1:** la cita ADASA "Tabla 5.6 punto 7.5 PRFV-GRP" es **correcta** pero imprecisa en redacción. El texto literal del ítem 7.5 NCh 2369 Of.2003 es: *"Estanques y ductos de materiales sintéticos compuestos (FRP, GFRP, HDPE y similares) | R = 3"*. PRFV (Poliéster Reforzado con Fibra de Vidrio) entra como sinónimo español de GFRP/FRP. Recomendación de redacción: en Rev 1 se sustituye la abreviatura "PRFV-GRP" por el texto literal de la norma para evitar dudas. El hallazgo de Rev 0 (que decía "el ítem 7.5 no existe") fue una falsa alarma del fork de auditoría — verificado contra `md/NCh2369-2003_extracted.md` línea 1359.

### F-COMUN-4 — Alcance dual de NCh 2369 sobre estanque PRFV

NCh 2369 Of.2003 tiene **dos alcances distintos** sobre el TK-06-001:

**(a) Solicitaciones sísmicas — APLICA:**
- Tabla 5.6 ítem 7.5: PRFV está explícitamente incluido (R = 3 para "Estanques y ductos de materiales sintéticos compuestos: FRP, GFRP, HDPE y similares").
- Capítulo 5 NCh 2369 Of.2003 — Cálculo sísmico: aplica a toda estructura industrial bajo NCh 2369, incluido el PRFV.
- Sección 5.5.1 letra b): `Cv = (2/3)·A0/g` aplica a casos Sección 5.1.1 letras c) y d) — incluye estanques con R = 3.
- Sección 4.5 letra a) (método tensiones admisibles): combinación H ± V con signos, aplica a la verificación de pernos por ASD.

**(b) Requerimientos específicos del Cap. 11.8 — NO APLICA al recipiente PRFV:**
- Sección 11.8.1 restringe el capítulo a "estanques fabricados de acero u hormigón armado".
- Sección 11.8.9 (Cv = 2/3 · C_modo_impulsivo) y Sección 11.8.13 (N/3 pernos toman 100 % del corte) son provisiones específicas de Sección 11.8: no son prescriptivas para PRFV. Pueden invocarse como referencia analógica conservadora, no como obligación normativa.
- La fabricación del recipiente PRFV se rige por **ASME RTP-1**, que la MC Exfibro Rev A invoca correctamente.

**Conclusión consolidada:** Exfibro hace bien al usar NCh 2369 para el cálculo sísmico (V_basal, M_volc, R = 3, masas impulsiva/convectiva). El gap es que **no propagan Cv = 0,267 al cálculo de tracción de pernos**. La obligación de incluirlo se deriva de Sección 5.5.1 letra b) + Sección 4.5 letra a) NCh 2369 (general), aplicable al estanque PRFV en virtud de Tabla 5.6 ítem 7.5. La posición ADASA es técnicamente defendible si se citan las secciones correctas.

---

## 3. Hallazgos exclusivos por documento

### Sólo en IT-005

- **F-IT-1 (CRÍTICA, no detectada en CT-002):** Rev 0 calculaba Ez = 0,267·12.572 = 3.357 kg sobre el peso total operacional, pero la fórmula de tracción de pernos seguía usando peso estabilizador W_vacío = 586 kg sin aplicarle el factor (1−Cv). El cálculo correcto con (1−Cv)·W_vacío = 0,733·586 = 429,5 kg → Msr_eff = 55.835 kg·cm → tb_eff = 1.598 kg → interacción 0,933 (con τ_adm corregido a 1.011 kg/cm²). En Rev 1 se aplica explícitamente.
- **F-IT-2 (MEDIA):** suma de masas impulsiva + convectiva = 8.968 + 3.368 = 12.336 kg vs W_tot = 12.572 kg. Diferencia 1,9 %. IT-005 declara "aceptamos Housner sin revisar" sin observar la diferencia. Se mantiene como observación menor; no afecta el veredicto.
- **F-IT-3 (MENOR):** conversión τ_adm. La memoria Exfibro p.12 da τ_adm = 99,2 MPa. La conversión correcta MPa → kg/cm² usa factor 10,197 → 1.011 kg/cm² (no 992). Rev 1 incorpora la corrección; el efecto numérico es pequeño pero mejora la trazabilidad.

### Sólo en CT-002

- **F-CT-1 (MAYOR):** Q4 Rev 0 invocaba Sección 11.8 como respaldo del peso estabilizador. Sección 11.8 está restringida por Sección 11.8.1 a acero/HA, así que no es la cita correcta para PRFV. Sin embargo, la obligación de incluir Cv en el peso estabilizador se deriva de **Sección 5.5.1 letra b) + Sección 4.5 letra a)** (combinación H ± V por tensiones admisibles), aplicable a PRFV. Q4 Rev 1 fue reformulada para pedir consistencia interna en la aplicación de NCh 2369 que Exfibro ya invoca, no cambio de norma.
- **F-CT-2 (MAYOR):** Q3 Rev 0 enunciaba "Cv = (2/3)·Cmax" cuando NCh 2369 Sección 5.5.1 letra b) dice **"Cv = (2/3)·A0/g"**. Numéricamente equivalentes en este caso (A0/g = Cmax = 0,40), pero conceptualmente distintos. Rev 1 cita Sección 5.5.1 letra b) `(2/3)·A0/g`.
- **F-CT-3 (MENOR):** Q-prefacio Rev 0 enunciaba que "los pernos cumplen con la combinación 100/30" pero esa combinación no es prescripción NCh — es práctica importada de ASCE 7. Rev 1 actualiza el resumen ejecutivo con la combinación Sección 4.5 letra a) plena (1,0·H + 1,0·V) y la interacción 0,933.
- **F-CT-4 (MENOR):** Q1 Rev 0 no advertía explícitamente que la diferencia entre Ez memoria (−2.514 kg, Cv ≈ 0,20) y Ez correcto (±3.357 kg, Cv = 0,267) sugiere que Exfibro aplicó **Sección 5.6 (equipos rígidos T ≤ 0,06 s)** indebidamente. Rev 1 incorpora esta hipótesis explícita en Q1.

---

## 4. Discrepancias entre las dos auditorías (resueltas)

| Punto | Fork IT-005 | Fork CT-002 | Resolución Rev 1 |
|-------|-------------|-------------|-------------------|
| ¿Cuál es la cita correcta para Cv en este estanque PRFV? | "Sección 11.8.9 — estanques verticales apoyados en suelo" | "Sección 5.5.1 letra b) Cv=(2/3)·A0/g; Sección 11.8 NO aplica a PRFV en cuanto a fabricación" | **Sección 5.5.1 letra b) prevalece como cita normativa** para el coeficiente Cv. Sección 11.8.9 está restringido por Sección 11.8.1 a acero/HA y no es invocable para el recipiente PRFV. La base correcta es Sección 5.5.1 letra b) (general NCh 2369), válida para PRFV en virtud de Tabla 5.6 ítem 7.5. ASME RTP-1 gobierna la fabricación del recipiente, no la solicitación sísmica. |
| ¿Cuál es la cita correcta para H+V? | "Sección 4.5 letra a) 100 % + 100 % con signos ±" | "ASCE 7-16 Sección 12.5.3 / API 650 Anexo E.6.1.5" | **Sección 4.5 letra a) NCh 2369 prevalece** para una consulta a fabricante chileno. La regla 100/30 H+V de ASCE 7 / API 650 puede mencionarse como práctica internacional alternativa, pero la prescripción aplicable en Chile por método de tensiones admisibles es Sección 4.5 letra a) sin factor 30 %. |
| ¿La diferencia 33,5 % en Ez justifica detener fundación OOCC? | No la cuestiona | "ADV-1: marginal; <2 % peso muerto, ~0 % momento volcante; sólo cambia 5 % en tracción de pernos. Bloqueo desproporcionado" | **Mantener bloqueo formal**. El bloqueo no es por magnitud sino por trazabilidad contractual: el consultor OOCC no puede recibir cargas no ratificadas, sin importar la magnitud del cambio. Si el plazo de fundación es crítico, evaluar emisión de cargas preliminares con nota "sujetas a ratificación final". |

---

## 5. TOP 5 acciones priorizadas (consolidado JUEZ)

| # | Acción | Documento | Esfuerzo | Plazo |
|---|--------|-----------|----------|-------|
| 1 | **Reescribir las citas normativas en IT-005**: eliminar todas las "Sección 5.5.3 (inexistente)" → reemplazar por "Sección 5.5.1 letra b) NCh 2369". Eliminar "regla 100/30 Sección 5.5.2" → reemplazar por "Sección 4.5 letra a) NCh 2369 (combinación 100 % + 100 % con signos ±)". Mantener cita "Tabla 5.6 ítem 7.5 — Estanques y ductos de materiales sintéticos compuestos (FRP, GFRP, HDPE y similares), R = 3"; usar texto literal de la norma en lugar de la abreviatura "PRFV-GRP". | IT-005 | 90 min | Antes de cualquier emisión derivada |
| 2 | **Emitir CT-002 Rev 1** con: (a) Q3 reformulado citando Sección 5.5.1 letra b) y reconociendo que (1−Cv) viene de aplicar Sección 4.5 letra a) al equilibrio de momentos; (b) Q5 reformulado citando Sección 4.5 letra a) NCh (100 % + 100 % con signos ±); (c) Q4 reformulado eliminando Sección 11.8 y pidiendo consistencia interna en propagación de Cv a pernos según Sección 5.5.1 letra b) + Sección 4.5 letra a); (d) Q1 ampliada con la hipótesis explícita: "¿se aplicó Sección 5.6 — equipos rígidos T ≤ 0,06 s? El modo impulsivo T = 0,158 s lo excluye." | CT-002 | 2 h | EOD 12-May-2026 |
| 3 | **Recomputar la tracción tb con la combinación Sección 4.5 letra a) plena** (1,0·H + 1,0·V con signos ±) y declarar la interacción 0,933 (con τ_adm corregido). Mantener veredicto "cumple" pero con derivación trazable. | IT-005 | 30 min | Antes de Rev 1 IT-005 |
| 4 | **Mantener NCh 2369 como norma de solicitaciones sísmicas; ASME RTP-1 sólo gobierna fabricación.** La Tabla 5.6 ítem 7.5 NCh 2369 incluye explícitamente PRFV/FRP/GFRP/HDPE con R = 3. La consulta CT-002 debe pedir que Exfibro **propague Cv = 0,267 al cálculo de tracción de pernos** según Sección 5.5.1 letra b) + Sección 4.5 letra a) NCh 2369, dentro del marco que ya usan para el sismo horizontal. **No es pivote — es exigir consistencia interna en la aplicación de NCh 2369 que Exfibro ya invoca.** ASME RTP-1 sigue gobernando el diseño/fabricación del recipiente PRFV; ambas normas conviven sin conflicto. | CT-002, IT-005 | Decisión técnica + 1 h redacción | Junto con CT-002 Rev 1 |
| 5 | **Pasar IT-005 Rev 1 y CT-002 Rev 1 por anti-ia revisar** (per CLAUDE.md Sección 2 — Redacción Analítica Humana). El fork ESTILISTA detectó frase-firma "se enmarca en la preparación de la licitación", estructura plantilla idéntica entre Q1-Q7 y aperturas categóricas sin matiz. Suavizar Q3, Q4, Q7 con "salvo que la memoria justifique formalmente otro criterio". | CT-002 Rev 1 | 30 min | Antes de envío |

---

## 6. Acciones secundarias (no bloquean emisión)

- **Confirmación de versión NCh 2369**: la coordinación interna del proyecto **confirma que el estanque está calculado con NCh 2369 Of.2003**, consistente con los parámetros aplicados en la memoria (Cmax = 0,40, R = 3, ξ_imp/ξ_conv). Q2 queda reducida a una errata del cajetín del plano `EX-26005-F01` (la cita aparente a "NCh 2369-2025" es inconsistente con la memoria y debe corregirse en Rev D del plano). Sin impacto en el cálculo.
- **Sección 11.8.13 (N/3 pernos toman corte)**: la norma especifica "estanques metálicos anclados de fondo plano", por lo que la prescripción no es aplicable directamente al estanque PRFV. Se puede invocar como **referencia analógica conservadora**: si Exfibro asume N/3, está siendo conservador (no menos exigente que la norma). Si en cambio asumen N pernos en paralelo, el corte por perno es menor y la interacción aún más holgada. ADASA puede preguntar qué hipótesis usa Exfibro y si las orejas/sillas garantizan 100 % activos (lo cual permitiría reducir el corte por perno).
- **Topes sísmicos**: IT-005 H5 los excluye del alcance. Si los topes toman parte del corte horizontal, V_perno = 2.597 kg está sobreestimado y la interacción es aún menor. Trasladar al consultor OOCC para diseño correlativo.
- **Inconsistencia I = 1,20 vs I = 1,00 en MC Exfibro p.7 vs p.16**: clasificar como error de transcripción (Tabla 4.5 NCh 2369 → C2 = 1,20 es la cita correcta), salvo que se justifique formalmente la diferenciación entre cálculo estructural y cálculo de altura de ola.

---

## 7. Estado de emisión y próximos pasos

| Doc | Estado actual | Acción siguiente | Owner | Plazo propuesto |
|-----|---------------|------------------|-------|-----------------|
| CT-002 | Rev 0 emitida 06-May-2026; **Rev 1 emitida 07-May-2026** | Notificar a Exfibro/Anwo el envío de Rev 1 con nota de errata sobre Rev 0 | Luis Rivera | EOD 12-May-2026 |
| IT-005 | Rev 0 archivada; **Rev 1 emitida 07-May-2026** (soporte interno) | Trasladar al consultor OOCC junto con la respuesta Exfibro a CT-002 Rev 1 | Luis Rivera | Tras respuesta Exfibro |
| Tabla de cargas basales para fundación OOCC | No emitida | Esperar respuesta Exfibro a CT-002 Rev 1 (≥10 días hábiles desde emisión Rev 1) | — | EOD 21-May-2026 (estimado) |
| Auditoría multi-audit (este informe) | Rev 1 generado 07-May-2026 | Archivar como soporte interno; usar como guía de trazabilidad para futuras revisiones | — | — |

---

## 8. Confianza y limitaciones de esta auditoría

**Cambios Rev 1 vs Rev 0 (07-May-2026):** se retiró F-COMUN-3 (la cita Tabla 5.6 ítem 7.5 ADASA es correcta — el ítem existe en NCh 2369 Of.2003 con texto "FRP, GFRP, HDPE y similares"). Se reformuló F-COMUN-4: Sección 11.8 está restringido a acero/HA solo en cuanto a sus requerimientos específicos del capítulo (fabricación, N/3, etc.); el resto de NCh 2369 (Tabla 5.6, Sección 5.5, Sección 4.5) sí aplica a PRFV. La acción #4 dejó de ser un "pivote" hacia ASME RTP-1 y pasó a ser "exigir consistencia interna en aplicación de NCh 2369". La tabla de combinaciones se actualizó al caso Sección 4.5 letra a) ASD pleno (1,0·H + 1,0·V) con interacción σ+τ = 0,933 ≤ 1,0 (incorporando la corrección del factor de conversión MPa → kg/cm² a 10,197).

**Confianza veracidad numérica:** ALTA (todos los cálculos reproducibles al 99,9 %).
**Confianza veracidad normativa:** las correcciones Rev 1 están verificadas contra `md/NCh2369-2003_extracted.md` (líneas 736-749 para Sección 4.5, 1037-1058 para Sección 5.5, 1358-1359 para Tabla 5.6 ítem 7.5, 2417-2486 para Sección 11.8). La skill `multi-audit` real (con orchestrator + AUDITOR SOMBRA independiente) no se ejecutó por restricción de credencial; si surge duda sobre alguna cita propuesta, contraverificar manualmente contra el texto extraído.

**Limitación de la extracción del plano EX-26005-F01-RevC:** texto rotado vectorizado → MD corrupto. Las cifras del plano (BCD = 2.755 mm, 8 pernos M25) se confirmaron por triangulación con MC Exfibro p.11-12. La aparente cita "NCh 2369-2025" del cajetín queda como errata a corregir en Rev D del plano; la versión efectivamente aplicada al diseño es **NCh 2369 Of.2003** (confirmado por la coordinación interna del proyecto y por los parámetros declarados en la memoria).

**Estado del correo a Anwo/Exfibro:** el correo de consulta fue **enviado el 06-May-2026** (`CORREOS/Mayo 2026/2026-05-06/2026-05-06_Consulta-Sismo-Vertical-Memoria-TK-06-001.md`) con los textos heredados de CT-002 Rev 0 e IT-005 Rev 0 — es decir, contiene las mismas tres citas erróneas que esta auditoría identifica (Sección 5.5.3 (inexistente), "regla 100/30 Sección 5.5.2", Sección 11.8 invocado para PRFV). El veredicto estructural no cambia. Decisión pendiente del equipo: (a) emitir un correo de errata a Anwo/Exfibro antes de su respuesta para corregir las citas, o (b) esperar la respuesta de Exfibro y aclarar entonces. Recomendación AUDITOR SOMBRA: opción (a), por defensa proactiva de la posición ADASA.

**Falta de auditoría sobre la decisión de bloqueo OOCC:** ABOGADO DEL DIABLO advierte que detener la fundación por una diferencia <2 % del peso muerto es desproporcionado. La decisión de mantener el bloqueo es contractual (trazabilidad de cargas), no técnica. Si el plazo de fundación es crítico, evaluar emitir cargas preliminares al consultor OOCC con nota "sujetas a ratificación final".

---

*Documento de soporte interno ADASA. Rev 0 generada 07-May-2026 a partir de dos auditorías sintéticas (forks Claude). Rev 1 (07-May-2026) corregida tras verificación directa del extract NCh 2369 sobre Tabla 5.6 ítem 7.5 y alcance dual de Sección 11.8. Sin emisión externa.*
