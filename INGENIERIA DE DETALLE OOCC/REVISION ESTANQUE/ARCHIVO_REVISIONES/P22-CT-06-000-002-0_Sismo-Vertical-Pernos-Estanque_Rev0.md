# CONSULTA TÉCNICA: TRATAMIENTO DEL SISMO VERTICAL EN MEMORIA DE CÁLCULO ESTANQUE TK-06-001

**Código:** P22-CT-06-000-002-0
**Proyecto:** BAE 12803 — Módulo de Salmuera Segunda Etapa Taltal
**Fecha:** 06-May-2026
**De:** ADASA — Aguas de Antofagasta S.A. (Luis Rivera)
**Para:** Anwo / Exfibro Ltda.
**Referencia:** Memoria Estanque AFTA Taltal Rev. A (02-Mar-2026); Plano EX-26005-F01 Rev C
**Estado:** EMITIDA

---

## 1. ANTECEDENTES

ADASA ha revisado los antecedentes técnicos del estanque de salmuera **TK-06-001** entregados por Exfibro: el plano `EX-26005-F01 Rev C` y la memoria de cálculo `Memoria Estanque AFTA Taltal` Rev. A. La revisión se enmarca en la preparación de la licitación de la ingeniería de detalle de obras civiles del proyecto Taltal.

La revisión técnica interna ADASA (`P22-IT-06-000-005-0`) confirma que los pernos M25 (1") F1554 Gr.36 especificados cumplen las verificaciones de tracción, corte e interacción incluso al incorporar la componente sísmica vertical Cv = 0,267 con la combinación 100/30 de NCh 2369 Of.2003. Sin embargo, se han identificado **siete observaciones formales** sobre la memoria que deben resolverse antes de que el documento pueda ser aceptado como antecedente final para el diseño de fundaciones por terceros.

La presente consulta solicita aclaraciones puntuales y la emisión de una **Rev B de la memoria** que cierre estos aspectos.

---

## 2. DOCUMENTOS DE REFERENCIA

| # | Código | Documento | Rev | Rol |
|---|--------|-----------|-----|-----|
| 1 | EX-26005-F01 | Plano vistas y detalles — Estanque vertical Ø2600 × H2570 | C | Documento bajo consulta |
| 2 | — | Memoria de cálculo — Estanque Salmuera 10 m³ | A (02-Mar-2026) | Documento bajo consulta |
| 3 | NCh 2369 Of.2003 | Diseño sísmico de estructuras e instalaciones industriales | — | Norma de referencia |
| 4 | P22-IT-06-000-005-0 | Revisión interna ADASA — Memoria TK-06-001 | 0 | Análisis de soporte |

---

## 3. CONSULTAS Y ACCIONES REQUERIDAS

### 3.1 Q1 — Origen del valor Ez = -2.514 kg en tabla de cargas basales (CRÍTICA)

**Estado actual:** La memoria reporta en la página 18, dentro de la tabla "Cargas basales a nivel de fondo del equipo", la fila:

| Combinación | Fz (kg) | Mz (kg·cm) |
|-------------|---------|-------------|
| Ez | **-2.514** | 0 |

El valor Ez = -2.514 kg aparece sin desarrollo previo en el cuerpo de la memoria. El cociente Ez / W_tot = 2.514 / 12.572 = **0,200** sugiere un coeficiente Cv = 0,20, valor que no corresponde a `Cv = (2/3)·Cmax` con Cmax = 0,40 declarado en página 7 (lo cual daría **Cv = 0,267 → Ez = 3.357 kg**).

**Acción requerida:**
1. Mostrar explícitamente la fórmula utilizada para calcular Ez, incluyendo el coeficiente sísmico vertical Cv y la masa o peso sobre el cual se aplica (¿W_total, W_impulsivo, W_vacío?).
2. Justificar normativamente el valor de Cv adoptado, citando la sección de NCh 2369 que lo respalda.
3. Si la fórmula correcta es `Cv = (2/3)·Cmax = 0,267`, ratificar el valor de Ez en la tabla p.18 (debería ser ±3.357 kg, no -2.514).

### 3.2 Q2 — Versión de NCh 2369 efectivamente aplicada (ALTA)

**Estado actual:**
- El plano `EX-26005-F01 Rev C`, en su cajetín, cita expresamente "**NCh 2369-2025**".
- La memoria de cálculo Rev. A cita "**NCh 2369 y API STANDARD 650**" sin indicar año (página 7).
- Los parámetros aplicados por la memoria (Cmax = 0,40 de tabla 5.7, R = 3 de tabla 5.6 con criterio 7.5 PRFV-GRP, ξ_imp = 2 % y ξ_conv = 0,5 % de tabla 5.5) corresponden a la estructura de **NCh 2369 Of.2003**.

**Acción requerida:**
1. Declarar explícitamente, en el documento Rev B, qué versión de NCh 2369 se aplicó al diseño (Of.2003 o :2025).
2. Si la respuesta es :2025, justificar por qué los parámetros de cálculo son los de Of.2003 y reemplazarlos por los actualizados de :2025 (cuyos coeficientes Cmax y combinaciones direccionales difieren).
3. Si la respuesta es Of.2003, modificar la nota del cajetín del plano `EX-26005-F01` para que coincida con la memoria, o explicar formalmente la coexistencia de ambas referencias.

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

Esta formulación **no incorpora el factor `(1 − Cv)` sobre el peso estabilizador W**, que es el desarrollo exigido por NCh 2369 Of.2003 §5.5 para evaluar el caso desfavorable: el sismo vertical en su sentido descendente reduce la fuerza estabilizadora gravitatoria, lo que aumenta la tracción que reciben los pernos.

**Acción requerida:**
1. Re-presentar el cálculo de tracción de pernos aplicando explícitamente `W → W·(1 − Cv)` en la fórmula `Msr = W·(1 − Cv)·D/2` para el caso desfavorable.
2. Documentar el valor de Cv adoptado y su origen normativo.
3. Reportar el nuevo valor de `tb` y la verificación de esfuerzos resultante. ADASA ha realizado este cálculo de manera independiente (memorando `P22-IT-06-000-005-0`) y obtiene tb = 1.537 kg con la combinación 100/30; los pernos siguen cumpliendo, pero el desarrollo formal debe constar en la memoria.

### 3.4 Q4 — Peso estabilizador adoptado en el cálculo de pernos (ALTA)

**Estado actual:** En la página 11 se utiliza `W = 586 kg`, que corresponde al peso vacío del estanque (manto + accesorios). El peso del fluido en operación (11.986 kg) no se considera como estabilizador en la fórmula de tracción de pernos. Esta práctica es habitual en estanques anclados PRFV cuando no se garantiza que el fluido esté presente durante el sismo, pero no se declara explícitamente en la memoria.

**Acción requerida:**
1. Declarar formalmente el criterio adoptado para el peso estabilizador: ¿se considera estanque vacío en el caso desfavorable? ¿se aplica el peso impulsivo W1 = 8.968 kg como masa que efectivamente acompaña al estanque?
2. Justificar la elección citando NCh 2369 Of.2003 §11 (estanques apoyados sobre el suelo) o la práctica de ASME RTP-1 / API 650 Anexo E.

### 3.5 Q5 — Combinación direccional H+V (MEDIA)

**Estado actual:** La memoria no documenta explícitamente cómo se combinan las componentes sísmicas horizontal y vertical. Las cargas elementales (Ex, Ey, Ez) aparecen tabuladas en página 18 sin instrucción sobre cómo combinarlas para diseño de pernos o fundación.

**Acción requerida:**
1. Documentar en la memoria Rev B la combinación direccional aplicada conforme NCh 2369 Of.2003 §5.5.2 (regla 100/30: 1,0·H ± 0,3·V o 0,3·H ± 1,0·V, la más desfavorable).
2. Indicar cuál combinación controla el diseño de pernos.

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
1. Resolver la inconsistencia adoptando un único valor de I para todo el cálculo del equipo.
2. Justificar el valor adoptado citando Tabla 4.5 de NCh 2369 Of.2003 (categoría de ocupación).

### 3.8 Q8 — Ratificación de reacciones basales para ingeniería civil

**Estado actual:** La tabla de cargas basales de página 18 será utilizada por el consultor de obras civiles ADASA como entrada de diseño para la fundación de hormigón armado y los topes/llaves de corte. Las observaciones Q1 a Q7 inciden directamente sobre los valores de esta tabla.

**Acción requerida:**
1. Tras incorporar las correcciones Q1-Q7, ratificar o corregir formalmente la tabla de cargas basales p.18, incluyendo:
   - Cargas estáticas (peso propio, fluido)
   - Cargas sísmicas Ex, Ey, Ez con signo `±` y valor numérico actualizado
   - Combinaciones recomendadas para diseño civil
2. Confirmar si la fórmula `Mz` (momento de torsión basal) es efectivamente cero o si debe calcularse para excentricidades del centro de masa.

---

## 4. DOCUMENTOS A EMITIR

Se solicita a Exfibro/Anwo emitir, en respuesta a esta consulta:

| # | Documento | Acción |
|---|-----------|--------|
| 1 | Memoria de cálculo Rev. B | Emisión con correcciones Q1-Q7 |
| 2 | Plano `EX-26005-F01` Rev. D | Si corresponde modificar la cita normativa del cajetín (Q2) |
| 3 | Tabla de reacciones basales actualizada | Como anexo de Rev. B (Q8) |
| 4 | Respuesta narrativa | Documento que aclare cada Q1-Q8 con referencia a páginas y secciones de la memoria Rev. B |

---

## 5. PLAZOS

ADASA solicita respuesta a esta consulta en un plazo de **diez (10) días hábiles** desde su emisión, considerando que el material es antecedente directo para la licitación de la ingeniería de detalle de obras civiles cuya emisión está prevista en el corto plazo.

---

## 6. CONTACTO

Para consultas técnicas:
- **Luis Rivera** — luis.rivera@adasa.cl

---

*Esta consulta es emitida por ADASA y se traslada a Exfibro Ltda. a través de Anwo (mandante del suministro). La trazabilidad documental se mantiene en `REVISIONES/CONSULTAS_TECNICAS/P22-CT-06-000-002-0`.*
