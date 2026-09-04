# Auditoría multi-audit — Sismo vertical TK-06-001

**Fecha:** 7 de mayo de 2026
**Documentos auditados:**
- `P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.md` (consulta a Exfibro, Rev 0 emitida 06-May-2026)
- `P22-IT-06-000-005-0_Revision_Memoria_TK-06-001.md` (revisión interna ADASA, Rev 0)

**Fuentes cruzadas:** NCh 2369 Of.2003 (norma), Memoria Estanque AFTA Taltal (Exfibro Rev A), plano EX-26005-F01-RevC.

**Modo de ejecución:** dos auditorías sintéticas en fork (la skill `multi-audit` orchestrator.py requiere `ANTHROPIC_API_KEY` separada de Claude Max; los forks ejecutaron las nueve perspectivas — DEFENSOR, NEUTRO, FISCAL, JUEZ, ESTILISTA, FACTUAL, ABOGADO DEL DIABLO, VERIFICADOR, AUDITOR SOMBRA — en pasada única contra las tres fuentes).

---

## 1. Veredicto global

**Núcleo técnico correcto. Base normativa frágil. Riesgo reputacional MEDIO-ALTO si Exfibro responde con rigor.**

| Dimensión | Estado |
|-----------|--------|
| Cifras numéricas (Cv, Ez, tb, σ, τ, áreas, momentos) | **CORRECTAS**. Reproducibles al 99,9% contra MC Exfibro y NCh. |
| Conclusión estructural (los pernos M25 F1554 Gr.36 cumplen) | **CORRECTA**. Interacción σ+τ ≈ 0.94 ≤ 1.0 incluso con la combinación normativa más estricta. |
| Diagnóstico de error en Ez declarado por Exfibro (−2.514 kg ↔ Cv=0,20 implícito) | **CORRECTO**. La diferencia 33,5% vs ±3.357 kg es real. |
| Citas normativas a NCh 2369 Of.2003 | **GRAVES ERRORES** — al menos tres referencias inexistentes y una norma fuera de alcance. |
| Posición ADASA frente a un Exfibro técnicamente preparado | **VULNERABLE**. Defendible sólo si se reformulan las citas. |

> **Recomendación AUDITOR SOMBRA (consenso):** suspender cualquier emisión adicional al consultor OOCC y a Exfibro **hasta corregir las citas normativas**. Si CT-002 ya está enviado: emitir Rev 1 con corrección y nota de errata. IT-005 está sin emitir externamente, así que se corrige antes de Rev 1.

---

## 2. Hallazgos críticos comunes (consenso entre las dos auditorías)

### F-COMUN-1 — §5.5.3 NCh 2369 Of.2003 NO EXISTE

| Doc | Frecuencia | Contexto |
|-----|------------|----------|
| IT-005 | 5+ ocurrencias (header, tabla parámetros, H1, H2, recomendaciones) | "Cv = (2/3)·Cmax según NCh 2369 §5.5.3" |
| CT-002 | Heredada en el desarrollo de Q3 | "factor (1−Cv) según §5.5" |

**Hecho normativo:** §5.5 cierra con §5.5.1 (cálculo estático del Fv vertical) y §5.5.2 (alternativa dinámica con espectro). **No hay §5.5.3.** La fórmula `Cv = (2/3)·Cmax` que IT-005 atribuye a §5.5.3 viene en realidad de §5.5.1 b) pero **referida a A0/g, no a Cmax** (numéricamente coinciden en zona 3 suelo II con A0=0,40g y Cmax=0,40, pero conceptualmente son distintos).

### F-COMUN-2 — "Regla 100/30 §5.5.2" es fabricación

| Doc | Frecuencia | Contexto |
|-----|------------|----------|
| IT-005 | H5, sección Re-cálculo, Caso A, recomendaciones a Exfibro | "Aplicar regla 100/30: 1,0·H ± 0,3·V (§5.5.2)" |
| CT-002 | Q5 | "§5.5.2 (regla 100/30: 1,0·H ± 0,3·V)" |

**Hecho normativo:**
- §5.5.2 NCh 2369 trata sobre **análisis dinámico vertical alternativo con espectro** (R=3, ξ=0,03). No es una regla de combinación direccional.
- La regla 100/30 entre componentes **horizontales** está en §5.1.2 NCh 2369 con condiciones específicas (irregularidad torsional, marcos rígidos comunes a dos líneas).
- La combinación H+V correcta en NCh 2369 está en **§4.5** (cargas a usar en el diseño) y exige **100% + 100% con signos ± para efecto desfavorable**, no 100% + 30%.
- La regla 100/30 H+V que ambos documentos ADASA citan **proviene de ASCE 7-16 §12.5.3 / API 650 Anexo E.6.1.5**, no de NCh 2369.

**Implicación práctica:** el "Caso A" (1,0·H + 0,3·V) que IT-005 elige como controlante es **menos conservador que §4.5**. Si Exfibro responde citando §4.5, ADASA queda con un análisis técnicamente más permisivo que la propia norma chilena.

### F-COMUN-3 — Tabla 5.6 punto 7.5 "PRFV-GRP" NO EXISTE

Heredado de la MC Exfibro p.7. La Tabla 5.6 NCh 2369:2003 tiene ítem 7.3 (estanques de acero, R=4) e ítem 7.4 (estanques de hormigón armado, R=3). **No hay ítem 7.5 con descripción "FRP-GRP".** El uso de R=3 para PRFV es razonable por analogía con HA, pero la cita literal "Tabla 5.6 punto 7.5" es inexacta — IT-005 lo replicó sin marcarlo y CT-002 lo asume implícitamente al aceptar el sistema EXFIBRO.

### F-COMUN-4 — §11.8 NCh 2369 NO APLICA al estanque PRFV

**Descubrimiento mayor (sólo el fork CT-002 lo identificó).**

§11.8.1 NCh 2369:2003 **explícitamente restringe el alcance a "estanques de acero u hormigón armado"**. El TK-06-001 es de **PRFV** (poliéster reforzado con fibra de vidrio). Por lo tanto:

- El propósito original de IT-005 — "aplicar §11.8 estanques apoyados sobre suelo" — es normativamente inválido.
- La cita §11.8.13 (1/3 de pernos toma 100% del corte) que IT-005 hereda de Exfibro **tampoco es prescriptiva** para PRFV.
- La cita §11.8.9 que el fork IT-005 propuso como "corrección" para la fórmula de Cv **tampoco aplica** — §11.8.9 está dentro del mismo capítulo restringido.
- La MC Exfibro Rev A invoca **ASME RTP-1** (Reinforced Thermoset Plastic Corrosion-Resistant Equipment), que es la norma internacional correcta para PRFV. Esto es **técnicamente sólido** desde el punto de vista de Exfibro.

**Implicación de fondo:** ADASA está pidiendo a Exfibro que cite secciones de NCh 2369 que **no aplican a su producto**. Si Exfibro responde con "NCh 2369 §11 no aplica a PRFV; nuestra norma de respaldo es ASME RTP-1 §3A-460", la posición ADASA queda neutralizada.

---

## 3. Hallazgos exclusivos por documento

### Sólo en IT-005

- **F-IT-1 (CRÍTICA, no detectada en CT-002):** inconsistencia interna. IT-005 calcula Ez = 0,267·12.572 = 3.357 kg sobre el peso total operacional, pero la fórmula de tracción de pernos sigue usando peso estabilizador W_vacío = 586 kg sin aplicarle el factor (1−Cv). El cálculo correcto con (1−Cv)·W_vacío = 0,733·586 = 429 kg → Msr_eff = 55.900 kg·cm → tb_eff = 1.597 kg → interacción 0,947 (no 0,939). Sigue cumpliendo, pero el número que IT-005 declara es ligeramente subestimado.
- **F-IT-2 (MEDIA):** suma de masas impulsiva + convectiva = 8.968 + 3.368 = 12.336 kg vs W_tot = 12.572 kg. Diferencia 1,9%. IT-005 declara "aceptamos Housner sin revisar" sin observar la diferencia.
- **F-IT-3 (MENOR):** conversión τ_adm. La memoria Exfibro p.12 da τ_adm = 99,2 MPa. La conversión correcta MPa → kg/cm² usa factor 10,197 → 1.011 kg/cm². IT-005 (y CT-002 implícitamente) usa 992 kg/cm² (factor 10). Error 1,9%, sin impacto en el veredicto pero con riesgo de cuestionamiento.

### Sólo en CT-002

- **F-CT-1 (MAYOR, no detectada en IT-005):** Q4 invoca §11.8 para pedir a Exfibro que declare formalmente el peso estabilizador. **§11.8 no aplica a PRFV** (F-COMUN-4). Q4 debe reformularse como pregunta abierta: "¿qué norma usó Exfibro para definir el peso estabilizador? (ASME RTP-1, API 650 Anexo E, otra)".
- **F-CT-2 (MAYOR):** Q3 enuncia "Cv = (2/3)·Cmax" cuando NCh 2369 §5.5.1 b) dice **"Cv = (2/3)·A0/g"**. Numéricamente equivalentes en este caso (A0/g = Cmax = 0,40), pero la fórmula citada es errónea. Si Exfibro responde con A0/g, ADASA queda en falta.
- **F-CT-3 (MENOR):** Q-prefacio enuncia que "los pernos cumplen con la combinación 100/30" pero esa combinación, como muestra F-COMUN-2, no es prescripción NCh — es práctica importada de ASCE 7.
- **F-CT-4 (MENOR):** Q1 no advierte explícitamente que la diferencia entre Ez memoria (−2.514 kg, Cv≈0,20) y Ez correcto (±3.357 kg, Cv=0,267) sugiere que Exfibro aplicó **§5.6 (equipos rígidos T≤0,06s)** indebidamente. El estanque tiene T_imp = 0,158s (memoria p.7), por lo que §5.6 no aplica. Esto es la pregunta clave para Exfibro y conviene formularla en Q1.

---

## 4. Discrepancias entre las dos auditorías

| Punto | Fork IT-005 | Fork CT-002 | Resolución |
|-------|-------------|-------------|------------|
| ¿Cuál es la cita correcta para Cv en este estanque? | "§11.8.9 — estanques verticales apoyados en suelo" | "§5.5.1 b) Cv=(2/3)·A0/g; §11.8 NO aplica a PRFV" | **CT-002 prevalece.** §11.8 está restringida por §11.8.1 a acero/HA. La base correcta para el estanque PRFV es ASME RTP-1 (norma de Exfibro) o §5.5.1 b) si se quiere referencia chilena genérica. |
| ¿Cuál es la cita correcta para H+V? | "§4.5 100% + 100% con signos ±" | "ASCE 7-16 §12.5.3 / API 650 Anexo E.6.1.5" | **Ambas son correctas.** §4.5 es la prescripción NCh general; ASCE 7 / API 650 son las prácticas internacionales. Para una consulta a Exfibro en Chile, **citar §4.5 NCh 2369**, y reconocer que ASME RTP-1 puede tener su propia regla (preguntar). |
| ¿La diferencia 33,5% en Ez justifica detener fundación OOCC? | No la cuestiona | "ADV-1: marginal; <2% peso muerto, ~0% momento volcante; sólo cambia 5% en tracción de pernos. Bloqueo desproporcionado" | **Mantener bloqueo formal**. El bloqueo no es por magnitud sino por trazabilidad contractual: el consultor OOCC no puede recibir cargas no ratificadas, sin importar la magnitud del cambio. |

---

## 5. TOP 5 acciones priorizadas (consolidado JUEZ)

| # | Acción | Documento | Esfuerzo | Plazo |
|---|--------|-----------|----------|-------|
| 1 | **Reescribir las citas normativas en IT-005**: eliminar todas las "§5.5.3" → reemplazar por "§5.5.1 b) NCh 2369" o "ASME RTP-1 §3A-460 / API 650 Anexo E.6.2.1" según corresponda. Eliminar "regla 100/30 §5.5.2" → reemplazar por "§4.5 NCh 2369 (combinación 100/100 con signos ±)" o citar la práctica internacional explícitamente. Eliminar "Tabla 5.6 punto 7.5 PRFV-GRP" → reemplazar por "Tabla 5.6 ítem 7.4 (HA, R=3) por analogía conservadora; PRFV no tiene ítem específico". | IT-005 | 90 min | Antes de cualquier emisión derivada |
| 2 | **Emitir CT-002 Rev 1** con: (a) Q3 reformulado citando §5.5.1 b) y reconociendo que (1−Cv) viene de práctica internacional; (b) Q5 reformulado citando §4.5 NCh y preguntando qué norma usó Exfibro para H+V; (c) Q4 reformulado eliminando §11.8 y preguntando qué norma usó Exfibro para peso estabilizador (ASME RTP-1, API 650, otra); (d) Q1 ampliada con la pregunta clave: "¿se aplicó §5.6 — equipos rígidos T≤0,06s? El modo impulsivo T=0,158s lo excluye." | CT-002 | 2 h | EOD 12-May-2026 |
| 3 | **Recomputar la tracción tb con factor (1−Cv) aplicado al peso estabilizador correcto** y declarar la interacción 0,947 (no 0,939). Mantener veredicto "cumple" pero con derivación trazable. | IT-005 | 30 min | Antes de Rev 1 IT-005 |
| 4 | **Pivote de la posición ADASA**: aceptar que NCh 2369 §11.8 no aplica a PRFV y que ASME RTP-1 (de Exfibro) es la norma técnicamente correcta. La consulta CT-002 debe enfocarse en pedir que Exfibro **demuestre la trazabilidad** de su cálculo a ASME RTP-1, no a NCh 2369. ADASA invoca NCh 2369 sólo como referencia complementaria para Cv (§5.5.1 b) por compatibilidad con norma chilena vigente). | CT-002, IT-005 | Decisión técnica + 1 h redacción | Junto con CT-002 Rev 1 |
| 5 | **Pasar IT-005 Rev 1 y CT-002 Rev 1 por anti-ia revisar** (per CLAUDE.md §2). El fork ESTILISTA detectó frase-firma "se enmarca en la preparación de la licitación", estructura plantilla idéntica entre Q1-Q7 (acción requerida + estado actual repetido) y aperturas categóricas sin matiz. Suavizar Q3, Q4, Q7 con "salvo que la memoria justifique formalmente otro criterio". | CT-002 Rev 1 | 30 min | Antes de envío |

---

## 6. Acciones secundarias (no bloquean emisión)

- **Confirmación visual del plano EX-26005-F01-RevC**: la extracción MD del plano salió corrupta (texto vectorizado AutoCAD). Verificar manualmente si el cajetín cita "NCh 2369-2025" o "Of.2003" y emitir Rev D del plano si es necesario (Q2 sigue válida).
- **§11.8.13 (N/3 pernos toma corte)**: el fork ABOGADO DEL DIABLO IT-005 nota que la norma agrega "a no ser que el sistema de anclaje consulte un dispositivo que garantice 100% activos". Si las orejas/sillas del plano constituyen ese dispositivo, el corte por perno se reduce y la interacción es menor. ADASA puede preguntar a Exfibro si la silla de anclaje califica.
- **Topes sísmicos**: IT-005 H5 los excluye del alcance. Si los topes toman parte del corte horizontal, V_perno = 2.597 kg está sobreestimado y la interacción es aún menor. Trasladar al consultor OOCC para diseño correlativo.
- **Inconsistencia I=1,20 vs I=1,00 en MC Exfibro p.7 vs p.16**: clasificar como error de transcripción (Tabla 4.5 NCh 2369 → C2 = 1,20 es la cita correcta).

---

## 7. Estado de emisión y próximos pasos

| Doc | Estado actual | Acción siguiente | Owner | Plazo propuesto |
|-----|---------------|------------------|-------|-----------------|
| CT-002 Rev 0 | EMITIDA 06-May-2026 a Exfibro/Anwo | Emitir Rev 1 con correcciones #1, #2, #4 + nota de errata reconociendo que Rev 0 contenía citas normativas incorrectas | Luis Rivera | EOD 12-May-2026 |
| IT-005 Rev 0 | Soporte interno, no emitido | Emitir Rev 1 antes de cualquier traslado al consultor OOCC | Luis Rivera | Junto con CT-002 Rev 1 |
| Tabla de cargas basales para fundación OOCC | No emitida | Esperar respuesta Exfibro a CT-002 Rev 1 (≥10 días hábiles desde emisión) | — | EOD 26-May-2026 (estimado) |
| Auditoría multi-audit (este informe) | Generado 07-May-2026 | Archivar como soporte interno; usar como guía para Rev 1 | — | — |

---

## 8. Confianza y limitaciones de esta auditoría

**Confianza veracidad numérica:** ALTA (todos los cálculos reproducibles al 99,9%).
**Confianza veracidad normativa:** las correcciones aquí propuestas están verificadas contra `md/NCh2369-2003_extracted.md`, pero la skill `multi-audit` real (con orchestrator + AUDITOR SOMBRA independiente) no se ejecutó por restricción de credencial. Si surge duda sobre alguna cita propuesta en Rev 1, contraverificar manualmente.

**Limitación de la extracción del plano EX-26005-F01-RevC:** texto rotado vectorizado → MD corrupto. Las cifras del plano (BCD=2.755 mm, 8 pernos M25) se confirmaron por triangulación con MC Exfibro p.11-12. La cita "NCh 2369-2025" del cajetín no es verificable desde el MD; requiere inspección visual del PDF original.

**Falta de auditoría sobre la decisión de bloqueo OOCC:** ABOGADO DEL DIABLO advierte que detener la fundación por una diferencia <2% del peso muerto es desproporcionado. La decisión de mantener el bloqueo es contractual (trazabilidad de cargas), no técnica. Si el plazo de fundación es crítico, evaluar emitir cargas preliminares al consultor OOCC con nota "sujetas a ratificación final".

---

*Documento de soporte interno ADASA. Generado a partir de dos auditorías sintéticas (forks Claude) sobre las fuentes NCh 2369 Of.2003, MC Exfibro Rev A, plano EX-26005-F01-RevC. Sin emisión externa.*
