# CONSULTA TÉCNICA: TRATAMIENTO DEL SISMO VERTICAL EN MEMORIA DE CÁLCULO ESTANQUE TK-06-001

**Código:** P22-CT-06-000-002-0
**Proyecto:** BAE 12803 — Módulo de Salmuera Segunda Etapa Taltal
**Revisión:** 1
**Fecha:** 07-May-2026
**De:** ADASA — Aguas de Antofagasta S.A. (Luis Rivera)
**Para:** Anwo / Exfibro Ltda.
**Referencia:** Memoria Estanque AFTA Taltal Rev. A (02-Mar-2026); Plano EX-26005-F01 Rev C
**Estado:** EMITIDA Rev 1 (Rev 0 emitida 06-May-2026, sustituida por la presente)

> **Nota de errata sobre Rev 0 (06-May-2026):** la presente Rev 1 corrige tres citas normativas erróneas que aparecían en Rev 0.
>
> 1. El coeficiente sísmico vertical Cv proviene de la Sección 5.5.1 letra b) NCh 2369 Of.2003 — Acción sísmica vertical (`Cv = (2/3)·A0/g`) — y no de la Sección 5.5.3, que no existe en la norma.
> 2. La combinación direccional H+V por método de tensiones admisibles está prescrita en la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles): 100 % H + 100 % V con signos ±. La "regla 100/30 (Sección 5.5.2)" mencionada en Rev 0 fue una atribución incorrecta; la Sección 5.5.2 trata sobre análisis dinámico vertical alternativo.
> 3. El capítulo Sección 11.8 NCh 2369 Of.2003 — Estanques verticales apoyados en el suelo está restringido por la Sección 11.8.1 (Alcance del capítulo: acero u hormigón armado) y no rige la fabricación del estanque PRFV.
>
> Las consultas Q1, Q3, Q4 y Q5 fueron reformuladas en consecuencia. El veredicto técnico de fondo no cambia: la verificación independiente de ADASA confirma que los pernos M25 (1") F1554 Gr.36 cumplen las verificaciones de tracción, corte e interacción aun con la combinación de la Sección 4.5 letra a) plena (interacción σ+τ = 0,933 ≤ 1,0).

---

## 1. ANTECEDENTES

ADASA ha revisado los antecedentes técnicos del estanque de salmuera **TK-06-001** entregados por Exfibro: el plano `EX-26005-F01 Rev C` y la memoria de cálculo `Memoria Estanque AFTA Taltal` Rev. A. La revisión apoya la preparación de la licitación de la ingeniería de detalle de obras civiles del proyecto Taltal.

La revisión técnica interna ADASA (`P22-IT-06-000-005-0` Rev 1) confirma que los pernos M25 (1") F1554 Gr.36 especificados cumplen las verificaciones de tracción, corte e interacción, incluso al incorporar la componente sísmica vertical Cv = 0,267 con la combinación de la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles) plena (1,0·H + 1,0·V con signos ±). La interacción σ/σ_adm + τ/τ_adm resulta 0,933 ≤ 1,0. Sin embargo, se han identificado **siete observaciones formales** sobre la memoria que deben resolverse antes de que el documento pueda ser aceptado como antecedente final para el diseño de fundaciones por terceros.

> **Nota normativa sobre alcance NCh 2369 al estanque PRFV:** salvo que la memoria documente formalmente otro criterio, NCh 2369 Of.2003 aplica al estanque TK-06-001 para el cálculo de las solicitaciones sísmicas: la Tabla 5.6 ítem 7.5 reconoce explícitamente "Estanques y ductos de materiales sintéticos compuestos (FRP, GFRP, HDPE y similares)" con R = 3, y los capítulos Sección 4.5 NCh 2369 Of.2003 — Combinaciones de cargas y Sección 5.5 NCh 2369 Of.2003 — Acción sísmica vertical son de aplicación general. El capítulo Sección 11.8 NCh 2369 Of.2003 — Estanques verticales apoyados en el suelo está restringido por la Sección 11.8.1 NCh 2369 Of.2003 — Alcance del capítulo (acero u hormigón armado) y, por tanto, no rige la fabricación del recipiente PRFV — gobernada por ASME RTP-1 y por el sistema de cálculo que Exfibro adopte. La presente consulta se enmarca en el conjunto de NCh 2369 que sí aplica al estanque y solicita consistencia interna en su uso por parte de la memoria.

La presente consulta solicita aclaraciones puntuales y la emisión de una **Rev B de la memoria** que cierre estos aspectos.

---

## 2. DOCUMENTOS DE REFERENCIA

| # | Código | Documento | Rev | Rol |
|---|--------|-----------|-----|-----|
| 1 | EX-26005-F01 | Plano vistas y detalles — Estanque vertical Ø2600 × H2570 | C | Documento bajo consulta |
| 2 | — | Memoria de cálculo — Estanque Salmuera 10 m³ | A (02-Mar-2026) | Documento bajo consulta |
| 3 | NCh 2369 Of.2003 | Diseño sísmico de estructuras e instalaciones industriales | — | Norma de referencia |
| 4 | ASME RTP-1 | Reinforced thermoset plastic corrosion-resistant equipment | 2017/2021 | Norma de referencia (fabricación PRFV) |
| 5 | P22-IT-06-000-005-0 | Revisión interna ADASA — Memoria TK-06-001 | 1 | Análisis de soporte |

---

## 3. CONSULTAS Y ACCIONES REQUERIDAS

### 3.1 Q1 — Origen del valor Ez = -2.514 kg en tabla de cargas basales (CRÍTICA)

**Estado actual:** La memoria reporta en la página 18, dentro de la tabla "Cargas basales a nivel de fondo del equipo", la fila:

| Combinación | Fz (kg) | Mz (kg·cm) |
|-------------|---------|-------------|
| Ez | **-2.514** | 0 |

El valor Ez = -2.514 kg aparece sin desarrollo previo en el cuerpo de la memoria. El cociente Ez / W_tot = 2.514 / 12.572 = **0,200** sugiere haber adoptado un coeficiente Cv ≈ 0,20, valor compatible con el de la **Sección 5.6 NCh 2369 Of.2003 — Equipos robustos y rígidos apoyados en el suelo** (equipos con período fundamental ≤ 0,06 s, donde se prescribe Cv = 0,5·A0/g = 0,20 para A0/g = 0,40). Sin embargo, el modo impulsivo del estanque tiene período T_imp = 0,158 s (memoria p.7), por lo que **la Sección 5.6 no aplicaría** y el coeficiente correcto sería el de la Sección 5.5.1 letra b) = (2/3)·A0/g = 0,267, que conduce a **Ez = ±3.357 kg**.

**Acción requerida:**
1. Mostrar explícitamente la fórmula utilizada para calcular Ez, incluyendo el coeficiente sísmico vertical Cv y la masa o peso sobre el cual se aplica (¿W_total, W_impulsivo, W_vacío?).
2. Justificar normativamente el valor de Cv adoptado, citando la sección de NCh 2369 Of.2003 que lo respalda. En particular, aclarar si se aplicó la Sección 5.6 (equipos rígidos, T ≤ 0,06 s) o la Sección 5.5.1 letra b) (coeficiente vertical general).
3. Si la fórmula correcta es la Sección 5.5.1 letra b) → `Cv = (2/3)·A0/g = 0,267`, ratificar el valor de Ez en la tabla p.18 (debería ser ±3.357 kg, no -2.514).

### 3.2 Q2 — Versión de NCh 2369 efectivamente aplicada (MENOR — confirmado Of.2003)

**Estado actual:**
- La memoria Rev. A cita "**NCh 2369 y API STANDARD 650**" sin indicar año (página 7).
- Los parámetros aplicados (Cmax = 0,40 Tabla 5.7, R = 3 Tabla 5.6 ítem 7.5 "Estanques y ductos de materiales sintéticos compuestos: FRP, GFRP, HDPE y similares", ξ_imp = 2 %, ξ_conv = 0,5 % Tabla 5.5) corresponden a **NCh 2369 Of.2003**, confirmado por la coordinación interna del proyecto.
- El plano `EX-26005-F01 Rev C`, en su cajetín, presenta una cita aparente a "NCh 2369-2025" que es inconsistente con la memoria. Tratado como errata del cajetín del plano, sin impacto en el cálculo.

**Acción requerida:**
1. Declarar explícitamente, en el documento Rev B de la memoria, que la versión aplicada es **NCh 2369 Of.2003**.
2. Corregir la nota del cajetín del plano `EX-26005-F01` en Rev D para que coincida con la memoria (NCh 2369 Of.2003).

### 3.3 Q3 — Aplicación del factor (1−Cv) al peso estabilizador en cálculo de pernos (CRÍTICA)

**Estado actual:** En la página 11 de la memoria, bajo "Diseño de anillo y sillas de anclaje", la tracción por perno se calcula como:

```
Msr = W·D/2 = 76.187 kg·cm     (con W = 586 kg, peso vacío)
Mt  = M − Msr = 355.658 kg·cm
X   = Mt/(π·R²) = 6,57 kg/cm
P   = π·D·X/N = 671 kg
F   = P·(a+b)/b = 1.007 kg
tb  = F · 1,5 = 1.510 kg
```

Esta formulación no incorpora el factor `(1 − Cv)` sobre el peso estabilizador W, que resulta de aplicar la combinación de la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles) al equilibrio de momentos. La componente vertical sísmica de la Sección 5.5.1 letra b) (`Cv = (2/3)·A0/g = 0,267`), combinada en su sentido descendente con el sismo horizontal pleno, reduce la fuerza estabilizadora gravitatoria y aumenta la tracción que reciben los pernos.

**Acción requerida:**
1. Re-presentar el cálculo de tracción de pernos aplicando explícitamente `W → W·(1 − Cv)` en la fórmula `Msr = W·(1 − Cv)·D/2` para el caso desfavorable.
2. Documentar el valor de Cv adoptado y su origen normativo (Sección 5.5.1 letra b) NCh 2369 Of.2003: `Cv = (2/3)·A0/g`).
3. Reportar el nuevo valor de `tb` y la verificación de esfuerzos resultante. La verificación independiente de ADASA (`P22-IT-06-000-005-0` Rev 1) obtiene tb = 1.598 kg con la combinación de la Sección 4.5 letra a) plena (1,0·H + 1,0·V con signos ±); los pernos siguen cumpliendo (interacción σ+τ = 0,933 ≤ 1,0), pero el desarrollo formal debe constar en la memoria.

### 3.4 Q4 — Propagación de Cv al cálculo de tracción de pernos y consistencia interna (MAYOR)

**Estado actual:** En la página 11 se utiliza `W = 586 kg` (peso vacío del estanque) como peso estabilizador, sin incorporar el factor `(1 − Cv)` que correspondería al combinar la componente sísmica vertical de la Sección 5.5.1 letra b) con la horizontal mediante la Sección 4.5 letra a). La memoria aplica correctamente NCh 2369 Of.2003 al cálculo del cortante basal y momento volcante horizontales, pero la componente vertical Cv no se propaga al diseño del sistema de anclaje. Salvo que la memoria justifique formalmente otro criterio, se observa una inconsistencia interna en la aplicación de NCh 2369.

**Acción requerida:**
1. Ratificar que el peso estabilizador en el cálculo de tracción de pernos incorpora el factor `(1 − Cv)` con `Cv = (2/3)·A0/g = 0,267` según la Sección 5.5.1 letra b) NCh 2369 Of.2003 — Acción sísmica vertical, aplicado mediante la combinación de la Sección 4.5 letra a) (método de tensiones admisibles), de manera consistente con el uso que la memoria ya hace de NCh 2369 para el cálculo sísmico horizontal y con el reconocimiento explícito del estanque PRFV en Tabla 5.6 ítem 7.5 (R = 3 para "Estanques y ductos de materiales sintéticos compuestos: FRP, GFRP, HDPE y similares").
2. Declarar formalmente el criterio adoptado para el peso estabilizador que entra en la fórmula `Msr`: ¿se considera estanque vacío como caso desfavorable (W = 586 kg)? ¿se incluye fracción de masa impulsiva W1?
3. Si la memoria adopta una norma de fabricación distinta para el sistema de anclaje (por ejemplo ASME RTP-1 Sección 3A-460 o API 650 Anexo E), declararla explícitamente y mostrar cómo esa norma trata la componente sísmica vertical, de modo que la trazabilidad sea completa.

### 3.5 Q5 — Combinación direccional H+V (MEDIA)

**Estado actual:** La memoria no documenta explícitamente cómo se combinan las componentes sísmicas horizontal y vertical. Las cargas elementales (Ex, Ey, Ez) aparecen tabuladas en la página 18 sin instrucción sobre cómo combinarlas para el diseño de pernos o de la fundación.

**Acción requerida:**
1. Documentar en la memoria Rev B la combinación direccional aplicada conforme **la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles)**, que prescribe `Cargas Permanentes + ... ± Sismo Horizontal ± Sismo Vertical` — es decir, **100 % H + 100 % V con signos ± para producir el efecto desfavorable**, sin factor 30 % entre componentes en este método. La regla 100/30 que aparece en la Sección 5.1.2 NCh 2369 Of.2003 — Combinación entre componentes horizontales aplica entre componentes horizontales bajo condiciones específicas (irregularidad torsional, marcos rígidos comunes a dos líneas) y no se aplica a la combinación H+V.
2. Indicar cuál combinación de signos controla el diseño de los pernos.

### 3.6 Q6 — Repartición del corte basal entre pernos y topes sísmicos (MEDIA)

**Estado actual:** El plano `EX-26005-F01 Rev C` muestra topes sísmicos en la base del estanque, pero la memoria asume que los pernos toman todo el corte horizontal vía la fórmula `V_perno = V_basal / (N/3) · 1,5`, sin descontar la fracción que tomarían los topes.

**Acción requerida:**
1. Aclarar si los topes sísmicos del plano son redundantes o si toman una fracción del corte horizontal.
2. Si toman corte, justificar la repartición y revisar el cálculo de V_perno en la memoria.
3. Si son redundantes, indicarlo explícitamente para evitar interpretaciones contradictorias por terceros.

### 3.7 Q7 — Inconsistencia interna del factor de importancia I (MEDIA)

**Estado actual:**
- Memoria página 7 (verificación sísmica principal): "Z = 3, I = 1,20".
- Memoria página 16 (altura de ola por sloshing): "Nch2369 I = 1,00".

**Acción requerida:**
1. Resolver la inconsistencia adoptando un único valor de I para todo el cálculo del equipo, salvo que se justifique formalmente la diferenciación entre el cálculo estructural (I = 1,20 para Categoría C2) y el cálculo de altura de ola por sloshing (donde algunas referencias internacionales como API 650 Anexo E.7.2 prescinden del factor de importancia).
2. Justificar el valor adoptado citando Tabla 4.5 de NCh 2369 Of.2003 (categoría de ocupación).

### 3.8 Q8 — Ratificación de reacciones basales para ingeniería civil

**Estado actual:** La tabla de cargas basales de página 18 será utilizada por el consultor de obras civiles ADASA como entrada de diseño para la fundación de hormigón armado y los topes/llaves de corte. Las observaciones Q1 a Q7 inciden directamente sobre los valores de esta tabla.

**Acción requerida:**
1. Tras incorporar las correcciones Q1-Q7, ratificar o corregir formalmente la tabla de cargas basales p.18, incluyendo:
   - Cargas estáticas (peso propio, fluido)
   - Cargas sísmicas Ex, Ey, Ez con signo `±` y valor numérico actualizado
   - Combinaciones recomendadas para diseño civil según la Sección 4.5 letra a) NCh 2369 Of.2003
2. Confirmar si la fórmula `Mz` (momento de torsión basal) es efectivamente cero o si debe calcularse para excentricidades del centro de masa.

---

## 4. RESUMEN DE LA VERIFICACIÓN ADASA Y POSICIÓN RESULTANTE

La verificación independiente de ADASA (`P22-IT-06-000-005-0` Rev 1) muestra que los pernos M25 (1") F1554 Gr.36 cumplen incluso bajo la combinación más estricta de NCh 2369 Of.2003:

| Magnitud | Sin Cv (memoria Rev. A) | **Sección 4.5 letra a) ASD pleno (1,0·H + 1,0·V)** |
|----------|-------------------------|---------------------------------------|
| Cv efectivo sobre W estabilizador | 0 | **0,267** |
| W_eff = W·(1 − Cv) | 586 kg | **429,5 kg** |
| tb (tracción por perno) | 1.510 kg | **1.598 kg** |
| σ / σ_adm | 0,207 | **0,219** |
| τ / τ_adm | 0,714 | **0,714** |
| Interacción σ + τ | 0,921 | **0,933 ≤ 1,0 ✓** |

> **Posición ADASA:** las consultas Q1-Q7 son de **forma normativa**, no de seguridad estructural. La integridad del estanque y de su sistema de anclaje no está en cuestión. Lo que se requiere es que la memoria refleje formalmente el cumplimiento que el diseño ya tiene, aplicando consistentemente NCh 2369 Of.2003 — incluyendo la componente sísmica vertical Cv en el cálculo de tracción de pernos — y resolviendo las inconsistencias internas (versión normativa, factor de importancia, trazabilidad de Ez).

---

## 5. DOCUMENTOS A EMITIR

Se solicita a Exfibro/Anwo emitir, en respuesta a esta consulta:

| # | Documento | Acción |
|---|-----------|--------|
| 1 | Memoria de cálculo Rev. B | Emisión con correcciones Q1-Q7 |
| 2 | Plano `EX-26005-F01` Rev. D | Si corresponde modificar la cita normativa del cajetín (Q2) |
| 3 | Tabla de reacciones basales actualizada | Como anexo de Rev. B (Q8) |
| 4 | Respuesta narrativa | Documento que aclare cada Q1-Q8 con referencia a páginas y secciones de la memoria Rev. B |

---

## 6. PLAZOS

ADASA solicita respuesta a esta consulta en un plazo de **diez (10) días hábiles** desde la emisión de la presente Rev 1 (07-May-2026), considerando que el material es antecedente directo para la licitación de la ingeniería de detalle de obras civiles cuya emisión está prevista en el corto plazo.

---

## 7. CONTACTO

Para consultas técnicas:
- **Luis Rivera** — luis.rivera@adasa.cl

---

*Esta consulta es emitida por ADASA y se traslada a Exfibro Ltda. a través de Anwo (mandante del suministro). La trazabilidad documental se mantiene en `REVISIONES/CONSULTAS_TECNICAS/P22-CT-06-000-002-0`. Rev 0 (06-May-2026) archivada en `INGENIERIA DE DETALLE OOCC/REVISION ESTANQUE/ARCHIVO_REVISIONES/`.*
