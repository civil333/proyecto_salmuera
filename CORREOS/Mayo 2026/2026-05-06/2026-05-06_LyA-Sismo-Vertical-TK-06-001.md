# Correo ejecutivo — L&A: cargas para diseño de fundación TK-06-001 con sismo vertical

**Estado:** ENVIADO 07-May-2026 (respaldo PDF/.msg pendiente de archivar en esta carpeta)
**Fecha:** 06-May-2026 (actualizado 07-May-2026 con valores de la Sección 4.5 letra a) ASD validados)
**De:** Luis Rivera — DIO ADASA
**Para:** Pablo Castillo (L&A Ingeniería y Proyectos) — `pcastillo@lyaingenieria.cl`
**CC:** Yohana Rodríguez Flores, Cristhian Sánchez, Luciano Méndez Huidobro (L&A); Víctor Gutiérrez (ADASA)
**Asunto:** PD Taltal — Cargas para diseño de fundación TK-06-001: efecto del sismo vertical (NCh 2369 Of.2003)

---

## Contexto Interno (No enviar)

Correo ejecutivo a L&A en respuesta a la consulta de Pablo Castillo sobre el tratamiento del sismo vertical en la memoria de cálculo del estanque. ADASA realizó el re-cálculo independiente (memorando P22-IT-06-000-005-0 Rev 1) y solicitó la Rev B a Exfibro/Anwo (consulta P22-CT-06-000-002-0). El mensaje a L&A es: **el delta principal es +5,8 % en tracción de pernos (1.510 → 1.598 kg, +88 kg/perno) y el cambio de signo en la componente vertical Ez. Los pernos M25 siguen cumpliendo (interacción 0,934 ≤ 1,0). L&A puede avanzar con el dimensionamiento; la Rev B de Exfibro formalizará los números.**

---

## Cuerpo del correo

Estimado Pablo:

En respuesta a tu consulta sobre el tratamiento del sismo vertical en la memoria de cálculo del estanque TK-06-001 (Exfibro Rev. A, plano EX-26005-F01 Rev C), ADASA realizó la revisión independiente y trasladamos las observaciones formales a Anwo/Exfibro solicitando la Rev B de la memoria. La buena noticia: el efecto numérico es modesto y no es un bloqueante para que ustedes avancen con el dimensionamiento de la fundación.

A continuación el resumen de los dos cambios relevantes para el diseño civil.

### 1. Reacciones basales para diseño de la fundación

| Componente | EXFIBRO Rev. A | Re-cálculo ADASA (Cv = 0,267) | Δ |
|------------|----------------|--------------------------------|---|
| Peso propio Fz | −586 kg | −586 kg | 0 % |
| Fluido en operación Fz | −11.986 kg | −11.986 kg | 0 % |
| Peso total estático Fz | −12.572 kg | −12.572 kg | 0 % |
| Cortante basal Ex (sismo H) | ±4.617 kg | ±4.617 kg | 0 % |
| Cortante basal Ey (sismo H) | ±4.617 kg | ±4.617 kg | 0 % |
| Momento volcante Mx (sismo H) | ±431.846 kg·cm | ±431.846 kg·cm | 0 % |
| Momento volcante My (sismo H) | ±431.846 kg·cm | ±431.846 kg·cm | 0 % |
| **Carga sísmica vertical Ez** | **−2.514 kg** | **±3.357 kg** | **+33,5 % (signo ±)** |

> El único valor que cambia es **Ez**. Exfibro lo reporta como −2.514 kg (Cv aparente ≈ 0,20 sin desarrollo trazable). El re-cálculo ADASA con Cv = (2/3)·A0/g = 0,267 según NCh 2369 Of.2003 Sección 5.5.1 letra b), aplicado sobre el peso total, da **Ez = ±Cv·W_tot = ±3.357 kg**. La diferencia más relevante respecto al diseño civil no es la magnitud sino el **signo ±**: para diseño de losa hay que evaluar las dos direcciones (peso aumentado +Cv para compresión sobre la losa; peso reducido −Cv para tracción de pernos).

### 2. Solicitaciones del perno de anclaje

| Magnitud | Exfibro Rev. A (sin Cv) | ADASA validado (Cv = 0,267 — combinación 1,0·H + 1,0·V con signos ±, ASD) | Δ |
|----------|--------------------------|------------------------------------------------------------------------------|---|
| Tracción tb por perno | 1.510 kg | **1.598 kg** | **+5,8 % (+88 kg)** |
| Corte V por perno | 2.597 kg | 2.597 kg | 0 % |
| σ tracción | 420 kg/cm² | 444 kg/cm² | +5,7 % |
| τ corte | 723 kg/cm² | 723 kg/cm² | 0 % |
| σ / σ_adm (σ_adm = 2.024 kg/cm²) | 0,207 | 0,219 | — |
| τ / τ_adm (τ_adm = 1.011 kg/cm²) | 0,715 | 0,715 | 0 % |
| **Interacción σ/σ_adm + τ/τ_adm** | **0,922** | **0,934** | **≤ 1 — CUMPLE** |

> Combinación aplicada: Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método de tensiones admisibles).
>
> Nota: τ_adm = 1.011 kg/cm² resulta de la conversión 99,2 MPa × 10,197 (factor exacto MPa → kg/cm²); la memoria Exfibro Rev. A reporta τ_adm = 99,2 MPa.

> Los pernos M25 (1") F1554 Gr.36 siguen cumpliendo con margen. Para el embebido y arrancamiento del perno en el hormigón, la tracción de diseño se actualiza a **1.598 kg/perno** (en lugar de 1.510 kg de Exfibro Rev. A). **Diferencia: +88 kg por perno (+5,8 %)**.

### 3. Recomendación

- **Pueden continuar con el dimensionamiento de la fundación** del estanque TK-06-001 usando las cargas de la columna "ADASA validado". Los deltas son: **+5,8 % en tracción del perno (1.510 → 1.598 kg)** y cambio de signo en Ez (−2.514 → ±3.357 kg). El resto de las cargas basales no cambia.
- Para el cálculo de la losa: aplicar la combinación direccional **Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas** (método de tensiones admisibles, 100 % H + 100 % V con signos ±). El caso desfavorable para compresión bajo el estanque es 1,0·Fz_total + 1,0·Ez (peso aumentado); para arrancamiento de pernos es 1,0·Fz − 1,0·Ez (peso reducido).
- La Rev B de la memoria Exfibro está solicitada con plazo de 10 días hábiles. **No anticipamos cambios mayores** sobre los valores de la columna "ADASA validado", salvo que Exfibro justifique un Cv distinto al (2/3)·A0/g = 0,267 que estamos asumiendo conforme NCh 2369 Of.2003 Sección 5.5.1 letra b). Les avisaremos en cuanto llegue.

Quedo atento a cualquier consulta adicional para no detener su diseño.

Saludos cordiales,

**Luis Rivera**
Departamento de Ingeniería y Optimización (DIO)
ADASA — Aguas de Antofagasta S.A.
luis.rivera@adasa.cl

---

**Adjunto opcional:**
- `calculo_pernos_TK-06-001_ADASA.xlsx` — planilla de respaldo del re-cálculo (reproduce tb = 1.510 kg de la memoria Exfibro al 99,9 % y aplica Cv = 0,267 con la combinación de la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (ASD pleno); resultado tb = 1.598 kg).
