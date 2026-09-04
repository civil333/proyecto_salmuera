# Correo — Consulta sobre tratamiento del sismo vertical en memoria de cálculo TK-06-001

**Estado:** ENVIADO 06-May-2026 (respaldo PDF/.msg pendiente de archivar en esta carpeta)
**Fecha:** 06-May-2026

> **Nota interna 07-May-2026:** auditoría posterior detectó tres errores de citación normativa en este correo (heredados de CT-002 Rev 0 y IT-005 Rev 0): (1) el factor Cv = (2/3)·Cmax debería leerse Cv = (2/3)·A0/g según la Sección 5.5.1 letra b) NCh 2369 Of.2003 — Acción sísmica vertical; (2) la "regla 100/30 (1,0·H + 0,3·V)" no es prescripción de NCh — la combinación H+V correcta para tensiones admisibles está en la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles) y exige 100 % + 100 % con signos ±; (3) la Sección 11.8 NCh 2369 Of.2003 — Estanques verticales apoyados en el suelo está restringida por la Sección 11.8.1 (Alcance del capítulo: acero u hormigón armado) y no rige al recipiente PRFV (gobernado por ASME RTP-1), pero el resto de NCh 2369 sí aplica al cálculo sísmico vía Tabla 5.6 ítem 7.5 (R = 3 para FRP/GFRP/HDPE/similares). El veredicto estructural no cambia: con la combinación de la Sección 4.5 letra a) plena, los pernos siguen cumpliendo (interacción σ+τ = 0,933 ≤ 1,0). CT-002 e IT-005 fueron emitidos a Rev 1 el 07-May-2026. Decisión pendiente: emitir un correo de errata a Anwo/Exfibro o esperar la respuesta de Exfibro y aclarar entonces.
**De:** Luis Rivera — ADASA
**Para:** Anwo Ltda. — Departamento Técnico (revisar destinatarios antes de enviar)
**CC:** Exfibro Ltda. (J. Aguilar / C. Salas), Víctor Gutiérrez (ADASA)
**Asunto:** PD Taltal — Consulta sobre tratamiento del sismo vertical en memoria de cálculo del Estanque de Salmuera TK-06-001 (EX-26005-F01)

---

## Contexto Interno (No enviar)

Correo cordial dirigido a Anwo (mandante del suministro) con copia a Exfibro (fabricante) solicitando rectificación de la memoria de cálculo del estanque TK-06-001. La revisión interna ADASA (P22-IT-06-000-005-0) y la consulta técnica formal (P22-CT-06-000-002-0) acompañan al correo como adjuntos.

**Hallazgo principal:** la memoria EXFIBRO Rev. A no aplica explícitamente el factor `(1 − Cv)` al peso estabilizador en la fórmula de tracción de pernos, según exige NCh 2369 Of.2003 §5.5. El re-cálculo independiente ADASA confirma que los pernos siguen cumpliendo, pero la memoria debe rectificarse formalmente.

**Tono:** cordial, no acusatorio. Reconocer el trabajo bien hecho en el resto del cálculo (Housner, momentos, geometría) y enfocar la solicitud en la formalización del Cv y la trazabilidad para terceros (consultor de OOCC).

---

## Cuerpo del correo

Estimados:

Junto con saludarles, en el marco de la preparación de la licitación de la ingeniería de detalle de obras civiles del proyecto Taltal, el equipo técnico de ADASA ha completado la revisión de los antecedentes del estanque de salmuera **TK-06-001** entregados por Exfibro: el plano `EX-26005-F01 Rev C` y la memoria de cálculo `Memoria Estanque AFTA Taltal` Rev. A.

La revisión confirma que el modelo dinámico aplicado (Housner impulsivo + convectivo, parámetros NCh 2369, ASME RTP-1) es **correcto y trazable**, y que los pernos M25 (1") F1554 Gr.36 especificados son **adecuados para las cargas sísmicas del proyecto**.

Sin embargo, hemos identificado un punto que requiere rectificación formal de la memoria antes de que ADASA pueda trasladarla al consultor de obras civiles como antecedente final: **la fórmula de tracción de los pernos no incorpora explícitamente el efecto desfavorable del sismo vertical sobre el peso estabilizador**, conforme exige NCh 2369 Of.2003 §5.5.

A continuación presentamos el hallazgo numérico clave que ADASA ha verificado de manera independiente, con tres elementos: (1) el cálculo original de EXFIBRO tal como aparece en la página 11 de la memoria; (2) la tabla comparativa con el re-cálculo ADASA; y (3) el análisis paso a paso de las diferencias.

### 1) Cálculo original — EXFIBRO Rev. A (memoria página 11, "Load on Anchor Bolt")

El bloque de cálculo emitido por Exfibro se reproduce a continuación (valores y fórmulas literales de la memoria):

| Variable | Fórmula | Valor | Unidad |
|----------|---------|-------|--------|
| Msr | W · D / 2 | 76.187 | kg·cm |
| Mt | M − Msr | 355.658 | kg·cm |
| X | fb · t = Mt / (π · R²) | 6,57 | kg/cm |
| Y | p · d / 4 | 0 | kg/cm |
| P | π · D · (X + Y) / N | 671 | kg |
| F | P · (a + b) / b | 1.007 | kg |
| Mt (Total moment at Base) | — | 355.658 | kg·cm |
| Load in Bolt | F | 1.007 | kg (Allowable for 1" Dia. Mín.) |
| Load per anchor Dog | P | 671 | kg/dog (C.S. A36) |

Sobre F = 1.007 kg, EXFIBRO aplica una amplificación adicional de 50 % (página 12) y reporta la tracción de diseño **tb = 1.510 kg**. El peso utilizado en la línea Msr es exclusivamente W = 586 kg (peso vacío del estanque, sin fluido). En este desarrollo, el coeficiente sísmico vertical Cv no aparece.

### 2) Tabla comparativa — solicitaciones del perno

| Magnitud | Memoria EXFIBRO (sin Cv) | Re-cálculo ADASA (Cv = 0,267 — regla 100/30) | Δ |
|----------|---------------------------|------------------------------------------------|---|
| Peso estabilizador efectivo W·(1−Cv) | 586 kg | 539 kg | −8,0 % |
| Msr = W_eff · D / 2 | 76.187 kg·cm | 70.080 kg·cm | −8,0 % |
| Mt = M − Msr | 355.658 kg·cm | 361.766 kg·cm | +1,7 % |
| Tensión circunferencial X | 6,57 kg/cm | 6,69 kg/cm | +1,8 % |
| Carga radial por perno P | 671 kg | 683 kg | +1,8 % |
| Carga por perno F = P·(a+b)/b | 1.007 kg | 1.025 kg | +1,8 % |
| **Tracción tb (amplificada 50 %)** | **1.510 kg** | **1.537 kg** | **+1,7 %** |
| σ tracción | 420 kg/cm² | 427 kg/cm² | +1,7 % |
| τ corte (sin variación) | 723 kg/cm² | 723 kg/cm² | — |
| **Interacción σ/σ_adm + τ/τ_adm** | **0,939** | **0,939** | **≤ 1 → CUMPLE** |

### 3) Análisis paso a paso — cómo cambia cada línea del procedimiento al introducir Cv

Aplicando el coeficiente sísmico vertical Cv = (2/3)·Cmax = 0,267 con la combinación 100/30 (1,0·H + 0,3·V), el efecto sobre cada línea del procedimiento original es el siguiente:

- **Peso estabilizador efectivo.** El peso vacío W = 586 kg se reemplaza por W_eff = W·(1 − 0,3·Cv) = 586 · 0,920 = 539 kg (−8,0 %). Es la única variable que cambia directamente por efecto del sismo vertical.
- **Msr = W · D / 2.** Como Msr es lineal en W, el momento estabilizador disminuye en la misma proporción: 76.187 → 70.080 kg·cm (−8,0 %).
- **Mt = M − Msr.** El momento volcante M no cambia (sigue siendo 431.846 kg·cm), pero Msr es menor; por lo tanto el momento neto que llega a los pernos aumenta: 355.658 → 361.766 kg·cm (+1,7 %).
- **X = Mt / (π · R²).** La tensión circunferencial sobre el anillo de anclaje es proporcional a Mt; aumenta de 6,57 → 6,69 kg/cm (+1,8 %).
- **P = π · D · X / N.** La carga radial por perno es proporcional a X; pasa de 671 → 683 kg (+1,8 %).
- **F = P · (a + b) / b y tb = F · 1,5.** La amplificación geométrica de la silla y el factor 1,5 son constantes; F sube de 1.007 → 1.025 kg y la tracción de diseño tb pasa de 1.510 → 1.537 kg (+1,7 %).
- **Verificación de esfuerzos.** σ tracción aumenta de 420 → 427 kg/cm² (+1,7 %), muy por debajo del admisible de 2.024 kg/cm² (0,8·Fy). El corte τ no cambia (Cv no afecta la fuerza horizontal). La interacción σ/σ_adm + τ/τ_adm se mantiene en 0,939, dominada por el corte. Los pernos M25 F1554 Gr. 36 siguen cumpliendo con margen.

En resumen, la corrección por sismo vertical actúa exclusivamente sobre el peso estabilizador del término Msr, y se propaga proporcionalmente al resto del procedimiento. El impacto numérico final es modesto (+1,7 % en tb) gracias a que en este equipo el peso vacío representa solo 586/12.572 ≈ 4,7 % del peso total y Msr es pequeño frente a M; sin embargo, el desarrollo formal debe constar en la memoria por exigencia de NCh 2369 Of.2003 §5.5.

En consecuencia, el resultado físico no cambia —el diseño es seguro—, pero la memoria de cálculo no documenta hoy el desarrollo del Cv ni la combinación direccional, y el valor `Ez = -2.514 kg` que aparece en la tabla de cargas basales (página 18) no es trazable a una fórmula explícita: el cociente `Ez / W_tot = 0,20` sugiere `Cv = (2/3)·0,30`, lo que es inconsistente con el `Cmax = 0,40` declarado en página 7 (que daría `Cv = 0,267 → Ez = ±3.357 kg`).

Por lo anterior, solicitamos atentamente:

- Emisión de **Rev B de la memoria de cálculo** que: (a) declare la versión de NCh 2369 efectivamente aplicada, (b) muestre el desarrollo del coeficiente sísmico vertical Cv y su origen normativo, (c) re-presente el cálculo de tracción de pernos aplicando explícitamente `W → W·(1 − Cv)` y la combinación 100/30, y (d) ratifique las reacciones basales (Ex, Ey, Ez, Mx, My) que se entregan al ingeniero civil para diseño de fundación.
- Aclaración del valor `Ez = -2.514 kg` de la tabla página 18.
- Resolución de la cita normativa del plano `EX-26005-F01 Rev C` ("NCh 2369-2025"), que difiere de los parámetros aplicados en la memoria (correspondientes a Of.2003).

Como referencia técnica formal adjuntamos:

1. **Consulta técnica P22-CT-06-000-002-0** — documento ADASA con las 8 preguntas (Q1 a Q8) detalladas.
2. **Memorando interno P22-IT-06-000-005-0** — desarrollo completo del re-cálculo independiente y trazabilidad numérica.

Quedamos atentos a su respuesta. Considerando que el material es antecedente directo para la licitación de obras civiles, agradeceríamos contar con la Rev B de la memoria en un plazo de **diez (10) días hábiles**.

Cualquier consulta de aclaración técnica antes de emitir la nueva revisión, no duden en contactarnos directamente.

Saludos cordiales,

**Luis Rivera**
Ingeniero de Proyecto
ADASA — Aguas de Antofagasta S.A.
luis.rivera@adasa.cl

---

**Adjuntos:**
1. P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx
2. P22-IT-06-000-005-0_Revision_Memoria_TK-06-001.docx
3. calculo_pernos_TK-06-001_ADASA.xlsx (planilla de respaldo del re-cálculo independiente)
