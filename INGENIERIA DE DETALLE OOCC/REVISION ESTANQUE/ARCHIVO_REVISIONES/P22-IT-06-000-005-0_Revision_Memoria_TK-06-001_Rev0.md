# REVISIÓN DE MEMORIA DE CÁLCULO ESTANQUE TK-06-001 — TRATAMIENTO DEL SISMO VERTICAL SEGÚN NCh 2369 OF.2003

**Código:** P22-IT-06-000-005-0
**Proyecto:** Módulo RO Segunda Etapa para Salmuera — PD Taltal
**Revisión:** 0
**Fecha:** 06-May-2026

---

## ANTECEDENTES

El estanque de salmuera **TK-06-001** es de suministro ADASA para el Módulo de Salmuera de la Planta Desaladora Taltal. Es un estanque vertical de poliéster reforzado con fibra de vidrio (PRFV), Ø2.625 mm × H2.570 mm, volumen útil 10 m³, peso vacío 586 kg y peso en operación con salmuera (gravedad específica 1,05) de 12.572 kg.

El equipo es fabricado por Exfibro Ltda. bajo orden de compra Folio N° 834750. La memoria de cálculo (`Memoria Estanque AFTA Taltal.pdf`, Rev. A, 02-Mar-2026) y el plano de fabricación (`EX-26005-F01 Rev C`) acompañan al equipo y declaran las cargas que se transmiten a la fundación de hormigón armado.

Durante la revisión técnica de los antecedentes para licitación de la ingeniería de detalle de obras civiles, el equipo de ADASA identificó que el cálculo de fuerzas en los pernos de anclaje no incorpora explícitamente la componente sísmica vertical exigida por NCh 2369. El presente documento revisa la memoria EXFIBRO Rev. A contra los requisitos de **NCh 2369 Of.2003** —norma con la que efectivamente se diseñó el equipo, según se desprende de los parámetros aplicados (Z=3, I=1,2, Cmax=0,40, R=3, ξ_imp=2 %, ξ_conv=0,5 %)— y produce un re-cálculo independiente para validar si los pernos especificados cumplen con la combinación correcta H+V.

> **Nota normativa:** El plano EX-26005-F01 Rev C cita "NCh 2369-2025" en su cajetín, mientras que los términos de referencia de OOCC ADASA (`P22-TR-00-010-01-1`) exigen NCh 2369:2025. La memoria EXFIBRO no declara año de la norma. La presente revisión se realiza contra **NCh 2369 Of.2003** por decisión expresa del proyecto, en consideración a que los parámetros usados por EXFIBRO corresponden a esa versión. La discrepancia normativa entre plano y memoria es por sí misma una observación que se traslada a EXFIBRO en la consulta técnica P22-CT-06-000-002-0.

---

## ALCANCE DE LA REVISIÓN

La revisión está acotada al **mínimo crítico**: verificación del par tracción/corte en los 8 pernos de anclaje M25 (1") F1554 Gr.36 con la combinación H+V correcta según NCh 2369 Of.2003 §5.5.2 y §5.5.3. No se rehace la cadena completa de Housner→momentos→fundación civil; se acepta el cálculo de masas impulsiva/convectiva, períodos y momentos volcantes horizontales reportados por EXFIBRO, y se modifica únicamente el peso estabilizador para reflejar el efecto vertical sísmico.

**Excluido del alcance:**
- Revisión de masa impulsiva/convectiva (modelo Housner)
- Revisión de períodos T_imp / T_conv
- Revisión de pandeo combinado del manto
- Diseño de fundación civil (responsabilidad del consultor OOCC)
- Verificación de los topes sísmicos del plano

---

## DOCUMENTOS DE REFERENCIA

| # | Código | Documento | Rev | Origen |
|---|--------|-----------|-----|--------|
| 1 | EX-26005-F01 | Plano vistas y detalles — Estanque vertical Ø2600 × H2570 | C | Exfibro |
| 2 | — | Memoria de cálculo — Estanque Salmuera 10 m³ | A | Exfibro |
| 3 | NCh 2369 Of.2003 | Diseño sísmico de estructuras e instalaciones industriales | — | INN |
| 4 | ASME RTP-1 | Reinforced thermoset plastic corrosion-resistant equipment | 2017/2021 | ASME |
| 5 | API 650 — Anexo E | Welded tanks for oil storage — seismic design | — | API |
| 6 | P22-TR-00-010-01 | TdR Ingeniería de detalle OOCC y estructuras metálicas | 1 | ADASA |

---

## DATOS DE ENTRADA

### Geometría y masas (memoria EXFIBRO Rev. A)

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| Diámetro interior D | 2.600 | mm |
| Altura manto Hss | 2.570 | mm |
| Altura líquido operación | 2.150 | mm |
| Espesor manto inferior T2 | 4,80 | mm |
| Peso vacío W_vessel | 586 | kg |
| Peso fluido W_cont | 11.986 | kg |
| Peso total W_tot | 12.572 | kg |
| Masa impulsiva W1 (W1/Wt = 0,736) | 8.968 | kg |
| Masa convectiva W2 (W2/Wt = 0,277) | 3.368 | kg |

### Anclajes (plano EX-26005-F01 RevC + memoria p.11)

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| Cantidad de pernos N | 8 | — |
| Diámetro nominal | 1" (M25) | — |
| Diámetro raíz dp | 2,14 | cm |
| Material | F1554 Gr.36 (ASTM A307 Gr.C) | — |
| Fluencia Fy | 248 | MPa |
| BCD (bolt circle diameter) | 2.755 | mm |
| Radio R = BCD/2 | 131,2 | cm |
| Distancia carga P → perno (a) | 65 | mm |
| Distancia perno → ancla A (b) | 130 | mm |
| Altura silla h | 140 | mm |

### Parámetros sísmicos NCh 2369 Of.2003 (verificados contra memoria)

| Parámetro | Símbolo | Valor | Referencia Of.2003 |
|-----------|---------|-------|---------------------|
| Zona sísmica | Z | 3 | Tabla 4.1 |
| Aceleración efectiva | A0/g | 0,40 g | Tabla 4.2 (Zona 3) |
| Tipo de suelo (asumido) | — | II | Tabla 4.3 — confirmar c/geotécnico |
| Categoría de ocupación | — | C2 | Tabla 4.5 |
| Coef. importancia | I | 1,20 | Tabla 4.5 (consistente con memoria p.7) |
| Razón amortiguamiento impulsivo | ξ_imp | 2 % | Tabla 5.5 |
| Razón amortiguamiento convectivo | ξ_conv | 0,5 % | Tabla 5.5 |
| Factor modificación respuesta | R | 3,0 | Tabla 5.6 |
| Coef. sísmico horizontal máximo | Cmax | 0,40 | Tabla 5.7 |
| Coef. sísmico convectivo (memoria) | Cc | 0,103 | p.7 memoria — fórmula §11.8.8 Of.2003 |
| **Coef. sísmico vertical (Of.2003 §5.5.3)** | **Cv** | **(2/3)·Cmax = 0,267** | §5.5.3 Of.2003 |

### Cargas resultantes (memoria EXFIBRO p.7-8)

| Magnitud | Valor | Unidad |
|----------|-------|--------|
| Cortante basal V (combinado SRSS) | 4.617 | kg |
| Momento volcante M_base (SRSS imp+conv) | 431.846 | kg·cm |
| M impulsivo (sobre base) | 380.871 | kg·cm |
| M convectivo (sobre base) | 213.158 | kg·cm |
| Fz reportado en tabla p.18 | -2.514 | kg |

---

## HALLAZGOS DE LA REVISIÓN

### Tabla resumen

| # | Hallazgo | Severidad | Página memoria |
|---|----------|-----------|----------------|
| H1 | `Ez = -2.514 kg` aparece en la tabla de cargas basales sin desarrollo previo. El cociente Ez/W_tot = 0,20 sugiere Cv = (2/3)·0,30, valor que no corresponde a Cmax = 0,40 declarado. Origen no trazable. | CRÍTICA | p.18 |
| H2 | La fórmula de tracción del perno `tb = 1.510 kg` (p.11-12) se construye como `Msr = W·D/2 → Mt = M − Msr → X = Mt/(π·R²) → P = π·D·X/N → F = P·(a+b)/b → tb = F·1,5`. **No incluye factor (1−Cv) sobre el peso estabilizador W**, que es el desarrollo exigido por NCh 2369 Of.2003 §5.5 para el caso desfavorable. | CRÍTICA | p.11-12 |
| H3 | Discrepancia de versión normativa: plano EX-26005-F01 RevC cita "NCh 2369-2025" en cajetín; la memoria solamente "Nch 2369 y API STANDARD 650" sin año, pero los parámetros aplicados (Cmax = 0,40 de tabla 5.7, R = 3 de tabla 5.6 con criterio 7.5 PRFV-GRP, ξ_imp/ξ_conv = 2 %/0,5 %) son los de **Of.2003**. Posible incoherencia entre diseño y plano. | ALTA | Plano cajetín; mem. p.7 |
| H4 | Inconsistencia interna en factor de importancia: memoria p.7 usa **I = 1,20**; memoria p.16 (cálculo de altura de ola por sloshing) usa **I = 1,00**. Los dos valores no pueden ser simultáneamente correctos para un mismo equipo. | MEDIA | p.7 vs p.16 |
| H5 | Combinación direccional H+V no documentada explícitamente en la memoria. NCh 2369 Of.2003 §5.5.2 requiere aplicar la regla 100/30 (1,0·H ± 0,3·V o 0,3·H ± 1,0·V, la combinación más desfavorable). | MEDIA | p.7-8, p.18 |
| H6 | Verificación de interacción `σ/σ_adm + τ/τ_adm` reportada como 0,92 (p.12). El recálculo con los valores de la propia memoria da 0,21 + 0,73 = 0,94. Diferencia menor pero indica que el valor presentado no es trazable directamente. Debe rehacerse con la nueva tracción que incluya Cv. | MEDIA | p.12 |
| H7 | Peso estabilizador utilizado en `Msr = W·D/2` corresponde solo al peso vacío del manto **W = 586 kg** (p.11). Este valor es trazable pero conservador frente al uso del peso operacional total (12.572 kg). Es coherente con la práctica habitual para estanques anclados PRFV; la memoria debe declararlo explícitamente. | MEDIA | p.11 |

---

## RE-CÁLCULO INDEPENDIENTE ADASA

### Reproducción del procedimiento EXFIBRO (sanity check)

Aplicando la fórmula textual de la memoria p.11 con los parámetros declarados:

```
M = 431.846 kg·cm        (momento volcante, mem. p.7)
W = 586 kg               (peso vacío, mem. p.11)
D = 260 cm               (diámetro interior)
R = 131,2 cm             (radio BCD/2)
N = 8 pernos
a = 6,5 cm ; b = 13,0 cm

Msr = W·D/2 = 586·260/2 = 76.180 kg·cm        (mem.: 76.187)
Mt  = M − Msr = 355.666 kg·cm                  (mem.: 355.658)
X   = Mt/(π·R²) = 6,58 kg/cm                   (mem.: 6,57)
P   = π·D·X/N = 671,5 kg                       (mem.: 671)
F   = P·(a+b)/b = 1.007,3 kg                   (mem.: 1.007)
tb  = F · 1,5 = 1.510,9 kg                     (mem.: 1.510) ✓
```

Reproducción al 99,9 %. El procedimiento EXFIBRO queda confirmado.

### Aplicación de Cv = 0,267 con regla 100/30

Caso A — sismo horizontal dominante (1,0·H + 0,3·V), que tipicamente controla pernos en estanques anclados con baja relación altura/diámetro:

```
Cv_efectivo  = 0,3 · 0,267 = 0,080
W_eff        = 586 · (1 − 0,080) = 539,1 kg     (peso estabilizador reducido)
M_eff        = 1,0 · 431.846 = 431.846 kg·cm
Msr_eff      = W_eff · D/2 = 70.080 kg·cm
Mt_eff       = M_eff − Msr_eff = 361.766 kg·cm
X_eff        = Mt_eff / (π·R²) = 6,69 kg/cm
P_eff        = π·D·X_eff / N = 683,3 kg
F_eff        = P_eff · (a+b)/b = 1.024,9 kg
tb_eff       = F_eff · 1,5 = 1.537 kg          (+1,7 % vs 1.510 sin Cv)
```

Verificación de esfuerzos:

```
A_raíz       = π·(2,14)²/4 = 3,597 cm²
σ            = tb_eff / A_raíz = 427 kg/cm²
σ_adm        = 0,8 · Fy = 2.024 kg/cm²
σ / σ_adm    = 0,211                            CUMPLE

V_perno      = V_basal/(N/3)·1,5 = 4.617/2,67·1,5 = 2.597 kg
τ            = V_perno / A_raíz = 722 kg/cm²
τ_adm        = 0,4 · Fy = 992 kg/cm²
τ / τ_adm    = 0,728                            CUMPLE

Interacción  = σ/σ_adm + τ/τ_adm = 0,211 + 0,728 = 0,939 ≤ 1,0   CUMPLE
```

### Tabla comparativa EXFIBRO vs ADASA

| Magnitud | EXFIBRO Rev.A (sin Cv) | ADASA (Caso A 100/30) | Δ % | Veredicto |
|----------|------------------------|------------------------|-----|-----------|
| Tracción tb | 1.510,9 kg | 1.537 kg | +1,7 % | Aumenta — caso desfavorable |
| σ tracción | 420 kg/cm² | 427 kg/cm² | +1,7 % | σ_adm = 2.024 → CUMPLE |
| Corte V_perno | 2.597 kg | 2.597 kg | 0,0 % | Sin cambio (V no afecta por Cv) |
| τ corte | 723 kg/cm² | 723 kg/cm² | 0,0 % | τ_adm = 992 → CUMPLE |
| Interacción σ+τ | 0,939 | 0,939 | +0,0 % | ≤ 1 → CUMPLE |

### Casos alternativos evaluados

| Caso | Combinación | tb (kg) | Comentario |
|------|-------------|---------|------------|
| 0 | EXFIBRO sin Cv (referencia) | 1.510,9 | — |
| A | 1,0·H + 0,3·V (regla 100/30) | 1.537 | Controla diseño en este equipo |
| B | 0,3·H + 1,0·V | 313,7 | No crítico — el momento horizontal reducido domina |
| C | 1,0·H + 1,0·V (suma directa, conservador) | 1.601 | Cota superior — no exigido por norma |

---

## VEREDICTO

Los 8 pernos M25 (1") F1554 Gr.36 especificados por EXFIBRO **siguen cumpliendo** la verificación de tracción, corte e interacción aun cuando se incorpora la componente sísmica vertical Cv = 0,267 con la combinación 100/30 exigida por NCh 2369 Of.2003. La interacción σ/σ_adm + τ/τ_adm se mantiene en 0,939, esencialmente sin cambio respecto al cálculo original de EXFIBRO (0,939 también, dado que el corte por perno —que domina la interacción— no se ve afectado por Cv).

Sin embargo, la memoria de cálculo EXFIBRO Rev. A presenta **incumplimientos formales** que deben corregirse para una entrega definitiva:

1. **Falta el desarrollo explícito del coeficiente sísmico vertical Cv** según NCh 2369 Of.2003 §5.5.3, con su fórmula `Cv = (2/3)·Ah` y su aplicación a las combinaciones de carga.
2. **La componente vertical Ez = -2.514 kg** que aparece en la tabla de cargas basales (p.18) **no es trazable** a una fórmula explícita; el cociente Ez/W_tot = 0,20 sugiere Cv = (2/3)·0,30, pero la memoria declara Cmax = 0,40, lo que daría Cv = 0,267. La inconsistencia debe resolverse documentalmente.
3. **La fórmula de tracción del perno** debe re-presentarse mostrando explícitamente cómo Cv afecta el peso estabilizador `W → W·(1−Cv)` en el caso desfavorable, conforme §5.5.
4. **La combinación direccional H+V** (regla 100/30 según §5.5.2) debe documentarse explícitamente.

Estos incumplimientos no comprometen la integridad estructural del estanque tal como se ha diseñado, pero impiden que la memoria sea aceptada como antecedente autocontenido para revisión por terceros (ingeniero civil de OOCC, auditor externo, autoridad).

> **Recomendación:** ADASA debe emitir consulta técnica formal a EXFIBRO/Anwo (P22-CT-06-000-002-0) solicitando una revisión de la memoria que: (a) declare explícitamente la versión normativa aplicada (Of.2003), (b) muestre el cálculo de Cv con su fórmula, (c) reporte la tracción de pernos con la combinación 100/30 y (d) ratifique las reacciones basales que se entregan al ingeniero civil.

---

## REACCIONES BASALES PARA INGENIERÍA CIVIL — VALORES CORREGIDOS

Las cargas que el consultor OOCC debe utilizar para el diseño de la fundación de hormigón armado del estanque TK-06-001 deben incluir explícitamente la componente sísmica vertical. Se presenta la tabla corregida a continuación; la memoria EXFIBRO debe ratificar estos valores antes de su uso final.

### Cargas estáticas

| Combinación | Fx (kg) | Fy (kg) | Fz (kg) | Mx (kg·cm) | My (kg·cm) |
|-------------|---------|---------|---------|------------|------------|
| Peso propio (estanque) | 0 | 0 | -586 | 0 | 0 |
| Fluido en operación | 0 | 0 | -11.986 | 0 | 0 |
| **Carga total estática** | **0** | **0** | **-12.572** | **0** | **0** |

### Cargas sísmicas (NCh 2369 Of.2003 — Cmax = 0,40 ; Cv = 0,267 ; I = 1,20)

| Combinación | Fx (kg) | Fy (kg) | Fz (kg) | Mx (kg·cm) | My (kg·cm) |
|-------------|---------|---------|---------|------------|------------|
| Sismo Ex (100 % H) | ±4.617 | 0 | 0 | 0 | ±431.846 |
| Sismo Ey (100 % H) | 0 | ±4.617 | 0 | ±431.846 | 0 |
| **Sismo Ez (100 % V — Cv·W_tot)** | **0** | **0** | **±3.357** | **0** | **0** |

> **Notas:**
> 1. **Ez corregido = ±Cv · W_tot = 0,267 · 12.572 = 3.357 kg** (vs 2.514 declarado por EXFIBRO). El signo es ±, no solo negativo: el caso desfavorable para tracción de pernos es +Cv (peso reducido); el caso desfavorable para compresión en losa es −Cv (peso aumentado).
> 2. La regla 100/30 entre componentes H y V debe aplicarla el ingeniero civil sobre estas cargas elementales, evaluando la combinación más desfavorable para cada elemento de la fundación (anclaje, losa, llaves de corte, topes sísmicos).
> 3. Estas cargas no incluyen viento (NCh 432 / ASCE 7) ni cargas térmicas, que deben evaluarse por separado conforme TdR OOCC.

---

## RECOMENDACIONES

### A EXFIBRO/Anwo (vía consulta técnica P22-CT-06-000-002-0)

1. Emitir Rev B de la memoria de cálculo declarando explícitamente: versión NCh 2369 utilizada, fórmula de Cv, peso estabilizador adoptado, combinación H+V aplicada (regla 100/30) y verificación de pernos con la combinación corregida.
2. Aclarar el origen del valor Ez = -2.514 kg de la tabla p.18 y, si corresponde, ratificar o corregir las reacciones basales que recibe el ingeniero civil.
3. Resolver la inconsistencia normativa entre plano (NCh 2369-2025) y memoria (parámetros de Of.2003): declarar formalmente cuál norma rige el diseño, modificando el plano si fuese necesario.
4. Resolver la inconsistencia interna del factor de importancia I (1,20 en p.7 vs 1,00 en p.16).
5. Documentar la repartición del corte basal entre pernos y topes sísmicos del plano, indicando qué fracción del esfuerzo horizontal toma cada elemento.

### A ADASA — uso interno

1. Trasladar al consultor de OOCC las cargas basales corregidas (con Ez = ±3.357 kg, no -2.514 kg) para el diseño de la fundación.
2. No aceptar la memoria EXFIBRO Rev. A como antecedente final hasta que se emita la Rev B con las correcciones formales.
3. Verificar con Anwo si la fabricación del estanque (en curso) refleja efectivamente el diseño con los parámetros de Of.2003 declarados en la memoria, dado que el plano cita "NCh 2369-2025".

---

## ANEXOS

- **Anexo A — Planilla de cálculo independiente:** `calculo_pernos_TK-06-001_ADASA.xlsx` (5 hojas: Datos, Sismo Of.2003, Memoria EXFIBRO, Re-cálculo ADASA, Comparación).
- **Anexo B — Consulta técnica formal:** `P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx`.

---

*Documento de uso interno ADASA. Constituye base técnica para la consulta formal P22-CT-06-000-002-0 dirigida a EXFIBRO/Anwo.*
