# INFORME DE REVISIÓN OFERTA BOMBAS KSB

**Fecha:** 29 de Diciembre de 2025  
**Referencia:** Compra de Bombas Planta Desaladora Taltal (P22-ET-06-005-001)  
**Oferente:** KSB Chile S.A.  
**Oferta:** SC80371-CV406762-REV1

---

## 1. RESUMEN EJECUTIVO

La oferta presentada por KSB Chile S.A. cumple parcialmente con los requerimientos técnicos y presenta una desviación económica respecto al presupuesto base.

*   **Cumplimiento de Puntos de Operación:** CUMPLE (Ambos ítems).
*   **Materiales:** DESVIACIÓN. Se ofertan ejes en Acero Duplex (1.4462) cuando la especificación exige Superduplex (PREN > 40) para todas las partes mojadas. La bomba sumergible oferta material 1.4517 (Duplex) en carcasa e impulsor.
*   **Económico:** La oferta neta ($47,552 USD) supera al presupuesto base ($41,645 USD) en un **14.2%**.

---

## 2. ANÁLISIS ECONÓMICO

| Ítem | Descripción | Cant. | Presupuesto Unit. (USD) | Presupuesto Total (USD) | Oferta KSB Unit. (USD) | Oferta KSB Total (USD) | Delta Total |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Bomba Sumergible (BS-06-001) | 1 | $18,879 | $18,879 | $20,284 | $20,284 | + $1,405 |
| 2 | Bombas Horizontales (BH-06-001) | 2 | $11,383 | $22,766 | $11,779 | $23,558 | + $792 |
| 3 | Asistencia Puesta en Marcha | 1 | (No detallado) | - | $3,710 | $3,710 | + $3,710 |
| **TOTAL** | **Neto sin IVA** | | | **$41,645** | | **$47,552** | **+ $5,907** |

> **Nota:** El presupuesto base no desglosaba explícitamente la asistencia técnica, lo que explica la mayor parte de la diferencia. Los equipos en sí mismos presentan un sobrecosto menor (~5.3%).

---

## 3. CHECKLIST TÉCNICO

### 3.1. Ítem 1: Bomba Sumergible Drenajes (BS-06-001)
*TAG: BS-06-001 | Modelo Ofertado: KRTF 65-215/44UEC2-S*

| Requerimiento (ET / Hoja Datos) | Especificado | Ofertado KSB | Estado | Observación |
| :--- | :--- | :--- | :---: | :--- |
| **Caudal** | 48.24 m³/h | 49.13 m³/h | ✅ OK | |
| **Altura (TDH)** | 10 m.c.a. | 10.37 m.c.a. | ✅ OK | |
| **Tipo** | Sumergible aguas residuales | Amarex KRT (Sumergible) | ✅ OK | |
| **Material Carcasa/Impulsor** | **Superduplex (PREN > 40)** | 1.4517 (ASTM A890 1B) | ⚠️ ALERTA | El 1.4517 es típicamente un Duplex (PREN ~34-37). **No cumple PREN > 40.** |
| **Material Eje** | **Superduplex (PREN > 40)** | 1.4462 (Duplex 2205) | ❌ NO | El material 1.4462 tiene PREN ~34. Desviación de especificación. |
| **Motor** | 380V / 50Hz / IP68 | 4 kW / IP68 | ✅ OK | |
| **Protecciones** | Sensores no requeridos | Incluye sensor temp. y humedad | ✅ EXTRA | Mejora respecto a lo solicitado. |
| **Impulsor** | - | Tipo Vortex (F-max) | ✅ OK | Adecuado para drenajes. |

### 3.2. Ítem 2: Bombas Alimentación Salmuera (BH-06-001)
*TAG: BH-06-001 | Modelo Ofertado: KNCPP 5A M 11-050*

| Requerimiento (ET / Hoja Datos) | Especificado | Ofertado KSB | Estado | Observación |
| :--- | :--- | :--- | :---: | :--- |
| **Caudal** | 48.2 m³/h | 48.22 m³/h | ✅ OK | |
| **Altura (TDH)** | 40 m.c.a. | 40.03 m.c.a. | ✅ OK | |
| **Tipo** | Centrífuga Horizontal | Química Normalizada ISO 2858 | ✅ OK | |
| **Material Carcasa/Impulsor** | **Superduplex (PREN > 40)** | A995 Gr 5A (Superduplex) | ✅ OK | Cumple especificación (CE3MN). |
| **Material Eje** | **Superduplex (PREN > 40)** | 1.4462 (Duplex 2205) | ❌ NO | **Desviación importante.** ET pide eje Superduplex. |
| **Eficiencia** | - | 61% (Bomba) / IE3 (Motor) | ✅ OK | |
| **Motor** | 380V / VDF | 11 kW / IE3 / 2930 rpm | ✅ OK | Confirmar aptitud VDF en placa (Ofertado arranque Y-D, pero motor IE3 suele ser apto VDF). |

---

## 4. CONCLUSIONES Y RECOMENDACIONES

1.  **Desviación de Materiales (Crítica):** La Especificación Técnica solicita explícitamente **Superduplex (PREN > 40)** para todas las partes mojadas, incluido el eje. KSB oferta ejes en **Duplex (1.4462)** para ambas bombas, y carcasa/impulsor en **1.4517 (Duplex)** para la sumergible.
    *   **Acción:** Se debe consultar a Ingeniería si se acepta Duplex estándar o se exige el cumplimiento estricto del Superduplex por corrosión severa de la salmuera (TDS 50,000-90,000 mg/L).
2.  **Presupuesto:** El sobrecosto del 14% se debe principalmente a la inclusión de la asistencia técnica en terreno ($3,710) que no parecía estar en el presupuesto original de equipos.
    *   **Acción:** Si se descuenta la asistencia, la oferta es competitiva ($43,842 vs $41,645, solo +5%).
3.  **Habilitación VDF:** Para las bombas horizontales (Ítem 2), se menciona arranque Estrella-Triángulo. Se debe confirmar que el motor incluya aislamiento reforzado apto para Variador de Frecuencia (VDF) tal como pide la ET.

**Estatus General:** Oferta **Técnicamente Condicionada** (a resolución de materiales) y **Económicamente Superior** al presupuesto.
