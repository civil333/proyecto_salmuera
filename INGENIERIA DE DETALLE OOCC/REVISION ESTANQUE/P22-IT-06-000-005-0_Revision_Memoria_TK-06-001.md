# REVISIÓN DE MEMORIA DE CÁLCULO ESTANQUE TK-06-001 — TRATAMIENTO DEL SISMO VERTICAL SEGÚN NCh 2369 OF.2003

**Código:** P22-IT-06-000-005-0
**Proyecto:** Módulo RO Segunda Etapa para Salmuera — PD Taltal
**Revisión:** 1
**Fecha:** 07-May-2026

> **Motivo del cambio (Rev 0 → Rev 1):** auditoría interna ADASA sobre Rev 0 detectó tres errores de citación normativa que debilitaban la posición frente a Exfibro: (1) Sección 5.5.3 (inexistente) NCh 2369 Of.2003 no existe — la cita correcta es Sección 5.5.1 letra b); (2) "regla 100/30 Sección 5.5.2" es atribución incorrecta — la combinación H+V por método de tensiones admisibles está en Sección 4.5 letra a) y exige 100 % + 100 % con signos ±, no 100/30; (3) Sección 11.8 está restringido por Sección 11.8.1 a estanques de acero u hormigón armado y no rige la fabricación del recipiente PRFV. Se recomputó la verificación de pernos con la combinación correcta Sección 4.5 letra a) y se corrigió la conversión de τ_adm (factor MPa → kg/cm² = 10,197). Veredicto estructural sin cambios: los pernos cumplen con interacción σ+τ = 0,933 ≤ 1,0.

---

## ANTECEDENTES

El estanque de salmuera **TK-06-001** es de suministro ADASA para el Módulo de Salmuera de la Planta Desaladora Taltal. Es un estanque vertical de poliéster reforzado con fibra de vidrio (PRFV), Ø2.625 mm × H2.570 mm, volumen útil 10 m³, peso vacío 586 kg y peso en operación con salmuera (gravedad específica 1,05) de 12.572 kg.

El equipo es fabricado por Exfibro Ltda. bajo orden de compra Folio N° 834750. La memoria de cálculo (`Memoria Estanque AFTA Taltal.pdf`, Rev. A, 02-Mar-2026) y el plano de fabricación (`EX-26005-F01 Rev C`) acompañan al equipo y declaran las cargas que se transmiten a la fundación de hormigón armado.

Durante la revisión técnica de los antecedentes para licitación de la ingeniería de detalle de obras civiles, el equipo de ADASA identificó que el cálculo de fuerzas en los pernos de anclaje no incorpora explícitamente la componente sísmica vertical exigida por NCh 2369. El presente documento revisa la memoria EXFIBRO Rev. A contra los requisitos de **NCh 2369 Of.2003** —norma con la que efectivamente se diseñó el equipo, según se desprende de los parámetros aplicados (Z=3, I=1,2, Cmax=0,40, R=3, ξ_imp=2 %, ξ_conv=0,5 %)— y produce un re-cálculo independiente para validar si los pernos especificados cumplen con la combinación correcta H+V.

> **Nota normativa sobre alcance NCh 2369 al estanque PRFV:** el capítulo 11.8 de NCh 2369 Of.2003 (Estanques verticales apoyados en suelo) está restringido por Sección 11.8.1 a estanques fabricados de acero u hormigón armado y, por tanto, no rige la fabricación del recipiente PRFV TK-06-001 (gobernada por ASME RTP-1). Sin embargo, el resto de NCh 2369 — Tabla 5.6 ítem 7.5 (R = 3 para "Estanques y ductos de materiales sintéticos compuestos: FRP, GFRP, HDPE y similares"), Sección 5.5 (acción sísmica vertical), Sección 4.5 (combinaciones de carga) — sí aplica al cálculo sísmico del estanque y al diseño del sistema de anclaje. La memoria EXFIBRO usa correctamente este marco para el cálculo horizontal; el gap es la propagación de la componente vertical Cv al cálculo de tracción de pernos.

> **Nota normativa sobre versión:** el plano EX-26005-F01 Rev C cita "NCh 2369-2025" en su cajetín, mientras que los términos de referencia de OOCC ADASA (`P22-TR-00-010-01-1`) exigen NCh 2369:2025. La memoria EXFIBRO no declara año de la norma. La presente revisión se realiza contra **NCh 2369 Of.2003** por decisión expresa del proyecto, en consideración a que los parámetros usados por EXFIBRO corresponden a esa versión. La discrepancia normativa entre plano y memoria es por sí misma una observación que se traslada a EXFIBRO en la consulta técnica P22-CT-06-000-002-0.

---

## ALCANCE DE LA REVISIÓN

La revisión está acotada al **mínimo crítico**: verificación del par tracción/corte en los 8 pernos de anclaje M25 (1") F1554 Gr.36 con la combinación H+V correcta según NCh 2369 Of.2003 Sección 4.5 letra a) (método de tensiones admisibles, 100 % H + 100 % V con signos ±) y Sección 5.5.1 letra b) (coeficiente sísmico vertical Cv). No se rehace la cadena completa de Housner→momentos→fundación civil; se acepta el cálculo de masas impulsiva/convectiva, períodos y momentos volcantes horizontales reportados por EXFIBRO, y se modifica únicamente el peso estabilizador para reflejar el efecto vertical sísmico.

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
| Factor modificación respuesta | R | 3,0 | Tabla 5.6 ítem 7.5 ("Estanques y ductos de materiales sintéticos compuestos: FRP, GFRP, HDPE y similares") |
| Coef. sísmico horizontal máximo | Cmax | 0,40 | Tabla 5.7 |
| Coef. sísmico convectivo (memoria) | Cc | 0,103 | p.7 memoria — fórmula Sección 11.8.8 Of.2003 (referencia analógica; Sección 11.8 restringido a acero/HA por Sección 11.8.1) |
| **Coef. sísmico vertical** | **Cv** | **(2/3)·A0/g = 0,267** | **Sección 5.5.1 letra b) Of.2003** (casos Sección 5.1.1 letras c) y d): "el coeficiente sísmico debe ser 2 A0 / 3 g") |

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
| H1 | `Ez = -2.514 kg` aparece en la tabla de cargas basales sin desarrollo previo. El cociente Ez/W_tot = 0,20 sugiere Cv ≈ 0,20, lo que es consistente con haber aplicado Sección 5.6 NCh 2369 Of.2003 (equipos rígidos T ≤ 0,06 s, Cv = 0,5 A0/g). El estanque tiene T_imp = 0,158 s (memoria p.7), por lo que Sección 5.6 no aplica y el Cv correcto es Sección 5.5.1 letra b) → 0,267 → Ez = ±3.357 kg. Origen no trazable en la memoria. | CRÍTICA | p.18 |
| H2 | La fórmula de tracción del perno `tb = 1.510 kg` (p.11-12) se construye como `Msr = W·D/2 → Mt = M − Msr → X = Mt/(π·R²) → P = π·D·X/N → F = P·(a+b)/b → tb = F·1,5`. **No incluye factor (1−Cv) sobre el peso estabilizador W**, que es el desarrollo exigido al combinar la componente vertical de Sección 5.5.1 letra b) con la horizontal mediante Sección 4.5 letra a) NCh 2369 Of.2003 (método de tensiones admisibles, 100 % H + 100 % V con signos ±, considerando el caso desfavorable). | CRÍTICA | p.11-12 |
| H3 | Versión NCh 2369 aplicada al diseño: **confirmada Of.2003** (los parámetros aplicados — Cmax = 0,40 de Tabla 5.7, R = 3 de Tabla 5.6 ítem 7.5 "FRP, GFRP, HDPE y similares", ξ_imp/ξ_conv = 2 %/0,5 % — son consistentes con Of.2003). La memoria Rev. A omite el año explícito (p.7) y el cajetín del plano `EX-26005-F01 Rev C` muestra una cita aparente a "NCh 2369-2025" inconsistente con la memoria. Se requiere declarar Of.2003 explícitamente en Rev B y corregir el cajetín del plano en Rev D. Sin impacto en el cálculo. | MENOR | Plano cajetín; mem. p.7 |
| H4 | Inconsistencia interna en factor de importancia: memoria p.7 usa **I = 1,20**; memoria p.16 (cálculo de altura de ola por sloshing) usa **I = 1,00**. Los dos valores no pueden ser simultáneamente correctos para un mismo equipo. | MEDIA | p.7 vs p.16 |
| H5 | Combinación direccional H+V no documentada explícitamente en la memoria. NCh 2369 Of.2003 Sección 4.5 letra a) prescribe, para el método de tensiones admisibles, la combinación `Cargas Permanentes + ... ± Sismo Horizontal ± Sismo Vertical` con 100 % H + 100 % V y signos ± (no la regla 100/30, que NCh 2369 reserva en Sección 5.1.2 para componentes horizontales bajo condiciones específicas). El sismo vertical se considera solo en los casos indicados en Sección 5.1.1 y su magnitud se determina conforme Sección 5.5. | ALTA | p.7-8, p.18 |
| H6 | Verificación de interacción `σ/σ_adm + τ/τ_adm` reportada como 0,92 (p.12). Recomputada con conversión MPa → kg/cm² correcta (factor 10,197): τ_adm = 99,2 MPa = 1.011 kg/cm² (no 992). Con la combinación Sección 4.5 letra a) plena, interacción = 0,219 + 0,714 = 0,933 ≤ 1,0. Diferencia menor frente al 0,92 declarado por EXFIBRO, pero indica que el valor presentado no es trazable directamente y debe rehacerse con la nueva tracción que incluya Cv. | MEDIA | p.12 |
| H7 | Peso estabilizador utilizado en `Msr = W·D/2` corresponde solo al peso vacío del manto **W = 586 kg** (p.11). Este valor es trazable pero conservador frente al uso del peso operacional total (12.572 kg). Es coherente con la práctica habitual para estanques anclados PRFV; la memoria debe declararlo explícitamente. Para el caso desfavorable Sección 4.5 letra a) con sismo vertical pleno (Cv = 0,267 sobre W estabilizador), el peso efectivo es W_eff = 586·(1−0,267) = 429,5 kg. | MEDIA | p.11 |

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

### Aplicación de Cv = 0,267 con combinación Sección 4.5 letra a) NCh 2369 Of.2003

NCh 2369 Of.2003 Sección 4.5 letra a) prescribe, para el diseño por método de tensiones admisibles, la combinación:

```
Cargas Permanentes + ... ± Sismo Horizontal ± Sismo Vertical
```

Es decir, **100 % de la componente horizontal con 100 % de la componente vertical**, con signos elegidos para producir el efecto desfavorable. No corresponde aplicar factor 30 % a una de las componentes en este método; la regla 100/30 que aparece en otras normas (ASCE 7, IBC) o entre componentes horizontales por Sección 5.1.2 NCh, no es la prescripción Sección 4.5 letra a) para H+V.

Para tracción de pernos en estanque anclado, el caso desfavorable es **+Cv** sobre el peso estabilizador (lo reduce y aumenta la tracción):

```
Cv = (2/3)·A0/g = (2/3)·0,40 = 0,267              (Sección 5.5.1 letra b))
W_eff   = W·(1 − Cv) = 586·(1 − 0,267) = 429,5 kg  (peso estabilizador reducido)
M_eff   = 1,0 · M_volc = 431.846 kg·cm             (sismo horizontal pleno)
Msr_eff = W_eff · D/2 = 429,5·130 = 55.835 kg·cm
Mt_eff  = M_eff − Msr_eff = 376.011 kg·cm
X_eff   = Mt_eff / (π·R²) = 376.011 / (π·131,2²) = 6,955 kg/cm
P_eff   = π·D·X_eff / N = π·260·6,955/8 = 710,3 kg
F_eff   = P_eff · (a+b)/b = 710,3 · 19,5/13 = 1.065,4 kg
tb_eff  = F_eff · 1,5 = 1.598 kg                   (+5,8 % vs 1.510 sin Cv)
```

Verificación de esfuerzos (con conversión MPa → kg/cm² corregida con factor 10,197):

```
A_raíz       = π·(2,14)²/4 = 3,597 cm²
σ            = tb_eff / A_raíz = 444 kg/cm²
σ_adm        = 0,8 · Fy = 0,8 · 2.529 kg/cm² = 2.024 kg/cm²
σ / σ_adm    = 0,219                            CUMPLE

V_perno      = V_basal/(N/3)·1,5 = 4.617/2,67·1,5 = 2.597 kg
τ            = V_perno / A_raíz = 722 kg/cm²
τ_adm        = 0,4 · Fy = 0,4 · 2.529 = 1.011 kg/cm²
τ / τ_adm    = 0,714                            CUMPLE

Interacción  = σ/σ_adm + τ/τ_adm = 0,219 + 0,714 = 0,933 ≤ 1,0   CUMPLE
```

> **Nota sobre conversión τ_adm:** la memoria EXFIBRO p.12 reporta τ_adm = 99,2 MPa (= 0,4·Fy). La conversión correcta a kg/cm² es 99,2 MPa × 10,197 cm²·kgf/(N·cm²) = **1.011 kg/cm²** (no 992 como podría obtenerse usando un factor aproximado de 10). El cálculo con el valor corregido produce τ/τ_adm = 0,714 e interacción 0,933, levemente menos exigente que con τ_adm = 992 (0,728 e interacción 0,947).

### Tabla comparativa de combinaciones

| Magnitud | EXFIBRO Rev. A (sin Cv) | Caso intermedio (1,0·H + 0,3·V — referencia) | **Sección 4.5 letra a) ASD pleno (1,0·H + 1,0·V)** |
|----------|-------------------------|-----------------------------------------------|---------------------------------------|
| Cv efectivo sobre W estabilizador | 0 | 0,3 · 0,267 = 0,080 | **0,267** |
| W_eff = W·(1−Cv) | 586,0 kg | 539,1 kg | **429,5 kg** |
| Msr_eff = W_eff · D/2 | 76.180 kg·cm | 70.080 kg·cm | **55.835 kg·cm** |
| Mt_eff = M_volc − Msr_eff | 355.666 kg·cm | 361.766 kg·cm | **376.011 kg·cm** |
| tb (tracción por perno) | 1.510 kg | 1.537 kg | **1.598 kg** |
| σ = tb / A_raíz | 420 kg/cm² | 427 kg/cm² | **444 kg/cm²** |
| σ / σ_adm | 0,207 | 0,211 | **0,219** |
| τ / τ_adm (invariante) | 0,714 | 0,714 | **0,714** |
| **Interacción σ + τ** | 0,921 | 0,925 | **0,933 ≤ 1,0 ✓** |

> El "Caso intermedio 1,0·H + 0,3·V" se incluye solo como referencia para mostrar la sensibilidad del resultado. La combinación normativa exigida por NCh 2369 Of.2003 Sección 4.5 letra a) para método de tensiones admisibles es **1,0·H + 1,0·V** con signos ±.

---

## VEREDICTO

Los 8 pernos M25 (1") F1554 Gr.36 especificados por EXFIBRO **siguen cumpliendo** la verificación de tracción, corte e interacción aun cuando se incorpora la componente sísmica vertical Cv = 0,267 con la combinación Sección 4.5 letra a) ASD plena (100 % H + 100 % V con signos ±) exigida por NCh 2369 Of.2003. La interacción σ/σ_adm + τ/τ_adm = 0,933 ≤ 1,0 se mantiene con margen suficiente (incremento de tb del orden del 5,8 % respecto al cálculo original sin Cv).

Sin embargo, la memoria de cálculo EXFIBRO Rev. A presenta **incumplimientos formales** que deben corregirse para una entrega definitiva:

1. **Falta el desarrollo explícito del coeficiente sísmico vertical Cv** según NCh 2369 Of.2003 Sección 5.5.1 letra b), con su fórmula `Cv = (2/3)·A0/g` y su aplicación a las combinaciones de carga.
2. **La componente vertical Ez = -2.514 kg** que aparece en la tabla de cargas basales (p.18) **no es trazable** a una fórmula explícita; el cociente Ez/W_tot = 0,20 sugiere haber aplicado Sección 5.6 NCh 2369 (equipos rígidos, Cv = 0,5·A0/g), lo cual no aplica al estanque (T_imp = 0,158 s > 0,06 s). El Cv correcto por Sección 5.5.1 letra b) es 0,267 → Ez = ±3.357 kg.
3. **La fórmula de tracción del perno** debe re-presentarse mostrando explícitamente cómo Cv afecta el peso estabilizador `W → W·(1−Cv)` en el caso desfavorable, conforme Sección 4.5 letra a) (combinación 100 % H + 100 % V con signos ±).
4. **La combinación direccional H+V** (Sección 4.5 letra a) NCh 2369 Of.2003: 100 % + 100 % con signos ±) debe documentarse explícitamente en la memoria.
5. **Conversión de unidades τ_adm:** corregir factor MPa → kg/cm² a 10,197 (τ_adm = 1.011 kg/cm², no 992), aunque el efecto numérico es menor.

Estos incumplimientos no comprometen la integridad estructural del estanque tal como se ha diseñado, pero impiden que la memoria sea aceptada como antecedente autocontenido para revisión por terceros (ingeniero civil de OOCC, auditor externo, autoridad).

> **Recomendación:** ADASA debe emitir consulta técnica formal a EXFIBRO/Anwo (P22-CT-06-000-002-0 Rev 1) solicitando una revisión de la memoria que: (a) declare explícitamente la versión normativa aplicada (Of.2003), (b) muestre el cálculo de Cv con su fórmula `(2/3)·A0/g` citando Sección 5.5.1 letra b), (c) reporte la tracción de pernos con la combinación Sección 4.5 letra a) (100 % H + 100 % V con signos ±) y (d) ratifique las reacciones basales que se entregan al ingeniero civil.

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
> 2. La combinación H+V para diseño debe aplicarse según NCh 2369 Of.2003 Sección 4.5 letra a) (método tensiones admisibles): 100 % H + 100 % V con signos ±, evaluando la combinación más desfavorable para cada elemento de la fundación (anclaje, losa, llaves de corte, topes sísmicos).
> 3. Estas cargas no incluyen viento (NCh 432 / ASCE 7) ni cargas térmicas, que deben evaluarse por separado conforme TdR OOCC.

---

## RECOMENDACIONES

### A EXFIBRO/Anwo (vía consulta técnica P22-CT-06-000-002-0 Rev 1)

1. Emitir Rev B de la memoria de cálculo declarando explícitamente: versión NCh 2369 utilizada, fórmula de Cv (Sección 5.5.1 letra b)), peso estabilizador adoptado, combinación H+V aplicada (Sección 4.5 letra a) — 100 % + 100 % con signos ±) y verificación de pernos con la combinación corregida.
2. Aclarar el origen del valor Ez = -2.514 kg de la tabla p.18 (¿se aplicó Sección 5.6 indebidamente?) y, si corresponde, ratificar o corregir las reacciones basales que recibe el ingeniero civil.
3. Declarar explícitamente NCh 2369 Of.2003 en la Rev B de la memoria (versión confirmada por los parámetros aplicados y por la coordinación interna del proyecto). Corregir el cajetín del plano `EX-26005-F01` en su próxima revisión D.
4. Resolver la inconsistencia interna del factor de importancia I (1,20 en p.7 vs 1,00 en p.16).
5. Documentar la repartición del corte basal entre pernos y topes sísmicos del plano, indicando qué fracción del esfuerzo horizontal toma cada elemento.

### A ADASA — uso interno

1. Trasladar al consultor de OOCC las cargas basales corregidas (con Ez = ±3.357 kg, no -2.514 kg) para el diseño de la fundación.
2. No aceptar la memoria EXFIBRO Rev. A como antecedente final hasta que se emita la Rev B con las correcciones formales.
3. Confirmar con Anwo/Exfibro que la fabricación del estanque corresponde a los parámetros de Of.2003 (versión confirmada). Solicitar corrección del cajetín del plano en Rev D para eliminar la cita errónea a "NCh 2369-2025".

---

## ANEXOS

- **Anexo A — Planilla de cálculo independiente:** `calculo_pernos_TK-06-001_ADASA.xlsx` (5 hojas: Datos, Sismo Of.2003, Memoria EXFIBRO, Re-cálculo ADASA, Comparación).
- **Anexo B — Consulta técnica formal:** `P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx` (Rev 1).

---

*Documento de uso interno ADASA. Constituye base técnica para la consulta formal P22-CT-06-000-002-0 dirigida a EXFIBRO/Anwo. Rev 0 archivada en `ARCHIVO_REVISIONES/`. Rev 1 (07-May-2026) corrige tres citas normativas y recompute la verificación de pernos con la combinación Sección 4.5 letra a) ASD plena.*
