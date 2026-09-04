# SCRIPT DE VIDEO: Funcionamiento del Módulo RO BiTurbo para Tratamiento de Salmuera — Planta Desaladora Taltal

## INSTRUCCIONES PARA NOTEBOOKLM
> Este documento es un guion detallado para generar un VIDEO EXPLICATIVO tipo "explainer" sobre el funcionamiento del módulo de ósmosis inversa de segunda etapa con tecnología BiTurbo™ para tratamiento de salmuera. El video debe seguir el flujo del P&ID (Diagrama de Tuberías e Instrumentación) del proceso, explicando CADA equipo en el orden en que el agua lo atraviesa. Usar los datos numéricos EXACTOS que se proporcionan. El tono debe ser técnico pero accesible, como una explicación de un ingeniero senior a un equipo de proyecto.

---

## METADATOS DEL PROYECTO

| Campo | Valor |
|---|---|
| **Proyecto** | Second Stage RO Module for Brine — PD Taltal |
| **Cliente** | ADASA / Aguas de Antofagasta |
| **Fabricante del Módulo** | BW Water Americas Inc. |
| **Código de Proyecto** | BAE 12803 / BWWA Job 25007 |
| **Documento de Referencia** | P22-CD-09-009-001 Rev B (Process Calculation) |
| **PFD de Referencia** | P22-DWG-09-009-01 Rev B |
| **P&ID de Referencia** | P22-DWG-09-009-002 Rev A (12 páginas) |

---

## SECCIÓN 1: INTRODUCCIÓN — CONTEXTO Y PROPÓSITO DEL MÓDULO

### Narración:
"La Planta Desaladora de Taltal, ubicada en la Región de Antofagasta, Chile, cuenta con un sistema de ósmosis inversa convencional (SWRO) que trata agua de mar. Este primer proceso genera un subproducto: la salmuera de rechazo, un fluido con alta concentración de sales disueltas que normalmente se descarta al mar.

El módulo que estamos por analizar cambia esa ecuación. Se trata de un **módulo de segunda etapa de ósmosis inversa**, diseñado por **BW Water Americas**, que toma esta salmuera de rechazo del SWRO (con una concentración de 43,000 a 53,000 mg/L de TDS) y la procesa una segunda vez para extraer agua adicional. Es, en esencia, un segundo exprimido de la salmuera.

El resultado: **21 m³/h de agua permeada adicional** con una calidad inferior a 230 mg/L de TDS, recuperando un **42.86%** del flujo de alimentación."

### Puntos Clave para Visualización:
- Diagrama general: SWRO → Salmuera → Módulo RO 2da Etapa → Permeado + Rechazo final
- Datos de alimentación: 49 m³/h, 43,000-53,000 mg/L TDS, pH 6-9, temperatura 19-24°C
- Producción: 21 m³/h permeado, 28 m³/h rechazo concentrado (~75,500 mg/L TDS)

---

## SECCIÓN 2: VISIÓN GENERAL DEL SISTEMA (Siguiendo el PFD)

### Narración:
"El módulo está completamente contenido dentro de un contenedor, operando 24 horas al día, los 365 días del año. Antes de adentrarnos en los detalles de cada equipo, veamos el recorrido completo del agua según el Diagrama de Flujo de Proceso (PFD Rev B):

1. La salmuera del SWRO ingresa al módulo
2. Se le dosifica **antiincrustante** para proteger las membranas
3. Pasa por un **mezclador estático** (MZE-09-001) para homogeneizar
4. Se filtra en el **filtro de cartuchos RO** (FIL-09-001) — protección final de 1 micrón
5. Ingresa a la **bomba de alta presión** (BH-09-001) FEDCO MSD-7016
6. La bomba impulsa el agua a través de la sección de bombeo del **Feed Turbocharger** (SIP-09-001)
7. El agua, ahora a alta presión, entra a la **1ª etapa de membranas RO** (BOI-09-001)
8. El permeado de la 1ª etapa sale hacia el colector común
9. El rechazo (concentrado) de la 1ª etapa pasa por la sección de bombeo del **Interstage Turbocharger** (SIP-09-002) — recibiendo un boost adicional de presión
10. Este concentrado, ahora a presión aún mayor, entra a la **2ª etapa de membranas RO** (BOI-09-002)
11. El permeado de la 2ª etapa se une al del primer tren
12. El rechazo final de la 2ª etapa, a ~83 bar de presión, alimenta la turbina del **Interstage Turbocharger** y luego la turbina del **Feed Turbocharger**, recuperando energía
13. El rechazo sale a ~1 bar hacia descarte

Este es el **circuito BiTurbo™ de FEDCO**: dos turbocargadores en serie que recuperan la energía hidráulica de la salmuera concentrada y la reutilizan para presurizar la alimentación."

### Equipos a Mostrar (con TAGs del P&ID):
| # | TAG | Equipo | Material Principal |
|---|---|---|---|
| 1 | TK-09-002 | Tanque Dosificador Antiincrustante | HDPE, 0.25 m³ |
| 2 | BDS-09-001/002 | Bombas Dosificadoras (2×100%) | 2.3 LPH @ 16 bar |
| 3 | MZE-09-001 | Mezclador Estático | PVC |
| 4 | FIL-09-001 | Filtro de Cartuchos RO | FRP, 49 m³/h |
| 5 | BH-09-001 | Bomba de Alta Presión | Super Duplex 2507 |
| 6 | SIP-09-001 | Feed Turbocharger | Super Duplex 2507 |
| 7 | BOI-09-001 | 1ª Etapa RO (6 vessels) | FRP vessels |
| 8 | SIP-09-002 | Interstage Turbocharger | Super Duplex 2507 |
| 9 | BOI-09-002 | 2ª Etapa RO (4 vessels) | FRP vessels |

---

## SECCIÓN 3: DOSIFICACIÓN DE ANTIINCRUSTANTE

### Narración:
"Antes de cualquier presurización, se dosifica un **antiincrustante al 100%** en la línea de alimentación. El sistema cuenta con:

- **Tanque** TK-09-002: capacidad 0.25 m³ (HDPE), con autonomía de 30 días
- **Bombas dosificadoras** BDS-09-001/002: dos unidades al 100% de redundancia (2×100%), tipo metering, 2.3 litros/hora a 16 bar, con control 4-20 mA
- **Dosificación**: 0.50 ppm promedio, hasta 3.00 ppm máximo
- El químico se inyecta antes del mezclador estático MZE-09-001 (fabricado en PVC), que garantiza una mezcla homogénea antes de la filtración

El antiincrustante es crítico porque el sistema opera con índices de saturación cercanos al límite: el LSI (Langelier Saturation Index) del concentrado final alcanza 1.61 y la saturación de CaSO₄ llega al 59%."

---

## SECCIÓN 4: FILTRACIÓN PRE-RO (Filtro de Cartuchos)

### Narración:
"El filtro de cartuchos FIL-09-001 es la última línea de defensa antes de las membranas. Sus características:

- **Capacidad**: 49 m³/h (100% del flujo de alimentación)
- **Carcasa**: FRP (fibra de vidrio reforzada), 12 pulgadas de diámetro × 63.25 pulgadas de largo
- **Cartuchos**: 12 unidades de 2.5" OD × 40" L
- **Filtración**: 1 micrón absoluto
- **Área de filtración**: 2.43 m², resultando en una tasa de 20.2 m³/h/m²
- **Función**: retener partículas que podrían dañar las membranas o bloquear los espaciadores

Cualquier partícula mayor a 1 micrón se detiene aquí. Esto protege no solo las membranas sino también los componentes sensibles de los turbocargadores."

---

## SECCIÓN 5: BOMBA DE ALTA PRESIÓN (El Motor del Sistema)

### Narración:
"La bomba de alta presión BH-09-001 es el único equipo motorizado de proceso en todo el módulo. Todo lo demás se mueve con la energía hidráulica que ella genera. Sus especificaciones reales (Rev B):

**Pump Data — FEDCO MSD-7016:**
- **Tipo**: Centrífuga horizontal multietapa, 16 etapas
- **Caudal**: 49.0 m³/h
- **Presión de entrada**: 2.0 bar (proporcionada por la bomba de salmuera del SWRO)
- **Presión de descarga**: 51.4 bar (punto de diseño a 53k TDS, 24°C)
- **Diferencial de presión**: 49.4 bar
- **Eficiencia**: 80.9%
- **Potencia absorbida**: 83.1 kW
- **RPM de diseño**: 3,006
- **NPSHR**: 4.4 m
- **Peso de la bomba**: 415.9 kg

**Motor — ABB o equivalente:**
- **Potencia nominal**: 125 HP (93 kW) a 380V/50Hz/3φ
- **Eficiencia**: 95%
- **Full Load Amps**: 167.8 A
- **Frame**: 445TSC
- **Encapsulamiento**: TEFC (Totally Enclosed Fan Cooled), IP66
- **Peso del motor**: 706.2 kg

**Drive (VFD) — Siemens SINAMICS G120X:**
- **Potencia**: 110 kW
- **Modelo**: 6SL3220-3YE46-0UF0
- Es fundamental: el VFD permite arrancar gradualmente, ajustar la presión según la salinidad del agua y coordinar con los turbocargadores

**Material de construcción**: Todo el camino húmedo es **Super Duplex Stainless Steel 2507** — impellers, difusores, carcasa, ejes, throttle nipple. Esto es obligatorio dada la corrosividad de una salmuera a más de 43,000 mg/L de TDS.

La bomba NO necesita generar toda la presión que requieren las membranas. Solo genera una fracción, porque los turbocargadores proveen el resto. Esa es la magia del sistema BiTurbo."

### Tabla de Puntos de Operación (datos reales del datasheet):
| Escenario | ΔP (bar) | RPM | Eficiencia | Potencia (kW) | NPSHR (m) |
|---|---|---|---|---|---|
| 43k TDS, 19°C | 35.4 – 36.3 | 2,618 – 2,644 | 82.4-82.5% | 58.4 – 59.9 | 3.4 |
| 43k TDS, 24°C | 41.8 – 42.8 | 2,801 – 2,827 | 81.8-81.9% | 69.4 – 71.2 | 3.8 |
| 53k TDS, 24°C | 46.5 – 46.9 | 2,930 – 2,938 | 81.3% | 77.8 – 78.5 | 4.1 – 4.2 |

---

## SECCIÓN 6: EL SISTEMA BiTurbo™ — CORAZÓN DE LA RECUPERACIÓN DE ENERGÍA

### Narración:
"Aquí está la innovación central del diseño: el sistema **BiTurbo™ de FEDCO**. Son dos turbocargadores modelo **HPB-60** conectados en serie. Cada uno recibe energía de la salmuera de rechazo y la convierte en presión adicional para la alimentación. Veamos cada uno:

### Feed Turbocharger — SIP-09-001
El primer turbo en el camino de la alimentación, pero alimentado por la salmuera que ya salió del segundo turbo:

- **Modelo**: HPB-60
- **Caudal de alimentación (Feed)**: 49.0 m³/h
- **Caudal de salmuera (Brine)**: 28.0 m³/h
- **Boost de presión generado**: ~20.9 bar (escenario 53k TDS máximo)
- **Presión de salmuera entrante (a la turbina)**: la que le pasa el Interstage
- **Presión de salmuera saliente**: 1.0 bar (descarte final)
- **Eficiencia de transferencia**: 70.3%
- **Peso**: 27.7 kg (compacto pero potente)
- **Material**: Super Duplex SS 2507

### Interstage Turbocharger — SIP-09-002
El segundo turbo, ubicado entre la 1ª y 2ª etapa de membranas:

- **Modelo**: HPB-60 (igual modelo)
- **Caudal de alimentación (Feed)**: 36.0 m³/h (el concentrado de la 1ª etapa)
- **Caudal de salmuera (Brine)**: 28.0 m³/h (rechazo directo de la 2ª etapa)
- **Boost de presión**: ~16.8 bar (escenario 53k TDS máximo)
- **Presión de entrada de la salmuera**: 83.3 bar
- **Presión de salida de la salmuera**: 53.5 bar (pasa al Feed Turbo)
- **Eficiencia**: 73.1%

### ¿Cómo funciona la recuperación de energía en cascada?

Siguiendo el P&ID, el ciclo energético es el siguiente:

1. **La bomba HPP** entrega al agua una presión de ~37-49 bar al agua (variable según TDS y temperatura)
2. El agua pasa por la **sección de bombeo** del Feed Turbo → recibe +14 a +21 bar adicionales → sale a 51-70 bar hacia la 1ª etapa
3. El concentrado de la 1ª etapa (36 m³/h a ~51-68 bar) entra a la **sección de bombeo** del Interstage Turbo → recibe +11 a +17 bar → sale a 62-85 bar hacia la 2ª etapa
4. El rechazo final (28 m³/h a ~60-83 bar) entra a la **turbina** del Interstage Turbo → transfiere energía → sale a ~47-54 bar
5. Esa salmuera (28 m³/h, ~47-54 bar) entra a la **turbina** del Feed Turbo → transfiere el resto de la energía → sale a 1 bar al descarte

La conexión es cruzada: la turbina del segundo turbo alimenta la cuarta operación más importante, y la turbina del primero completa la recuperación."

### Tabla Resumen BiTurbo™ (Datos Reales):

| Parámetro | Feed Turbo (SIP-09-001) | Interstage Turbo (SIP-09-002) |
|---|---|---|
| Modelo | HPB-60 | HPB-60 |
| Feed Flow | 49.0 m³/h | 36.0 m³/h |
| Brine Flow | 28.0 m³/h | 28.0 m³/h |
| Boost Presión (max) | 20.9 bar | 16.8 bar |
| Eficiencia | 70.3% | 73.1% |
| Kvt (aux cerrada) | 3.98 | 5.28 |
| Kvt (aux abierta) | 4.69 | 5.90 |
| Pérdida eff. boquilla | 1.5% | 1.5% |
| Peso | 27.7 kg | 27.7 kg |
| Conexiones Feed | DN50 / DN50 | DN50 / DN50 |
| Conexiones Brine | DN40 / DN40 | DN40 / DN40 |

---

## SECCIÓN 7: LAS MEMBRANAS UHPRO — DOS ETAPAS, DOS TECNOLOGÍAS

### Narración:
"El módulo emplea una configuración de **2 etapas en arreglo 6:4** con un total de **10 vessels y 70 elementos de membrana**. Lo notable es que cada etapa usa una membrana diferente, optimizada para su rango de presión:

### 1ª Etapa (BOI-09-001) — LG SW 400 SR
- **6 vessels Protec BPV-8-1200-SP-7** (rating 1,200 psi / 82.7 bar)
- **42 membranas** LG SW 400 SR (7 por vessel)
- **Rechazo de sales**: 99.85% estabilizado (99.7% mínimo)
- **Área activa**: 400 ft² (37 m²) por elemento
- **Caudal producido**: 13 m³/h de permeado
- **Flux promedio**: 8.3 lmh
- **Rango de presión operativa**: 51-54 bar (alimentación)

### 2ª Etapa (BOI-09-002) — LG SW 400R G2 UHP (Ultra High Pressure)
- **4 vessels Protec BPV-8-1800-SP-7** (rating 1,800 psi / 124 bar)
- **28 membranas** LG SW 400R G2 UHP (7 por vessel)
- **Rechazo de sales**: 99.85% estabilizado (99.7% mínimo)
- **Área activa**: 380 ft² (35 m²) por elemento
- **Caudal producido**: 8 m³/h de permeado
- **Flux promedio**: 7.8 lmh
- **Rango de presión operativa**: 62-85 bar (alimentación)
- **Presión máxima ratings**: 1,740 psi (120 bar)

### ¿Por qué dos tipos de membranas?
La clave está en la presión. La 1ª etapa opera a presiones moderadas (51-54 bar), para lo cual las membranas seawater convencionales (SW 400 SR) son adecuadas. Pero la 2ª etapa debe operar a presiones significativamente mayores (62-85 bar) para superar la presión osmótica del concentrado enriquecido. Aquí se necesitan membranas **UHP** (Ultra High Pressure) capaces de soportar hasta 120 bar continuamente."

### Calidad del Permeado (Datos de Modelación LG Chem Design):
| Escenario | TDS Permeado Compuesto | TDS Permeado Etapa 1 | TDS Permeado Etapa 2 |
|---|---|---|---|
| 43k TDS, 19°C, Y0 | 165 mg/L | 122 mg/L | 235 mg/L |
| 43k TDS, 19°C, Y1 | 176 mg/L | 131 mg/L | 249 mg/L |
| 43k TDS, 19°C, Y5 | 229 mg/L | 172 mg/L | 317 mg/L |
| 53k TDS, 19°C, Y0 | (ver Process Calc) | — | — |

---

## SECCIÓN 8: ARRANQUE DEL SISTEMA Y COMPORTAMIENTO DINÁMICO

### Narración:
"La pregunta que todo ingeniero se hace: ¿cómo arranca un sistema donde los turbocargadores dependen de la salmuera que aún no existe porque las membranas todavía no producen rechazo? La respuesta es un arranque secuencial coordinado:

**Paso 1 — Empuje inicial con VFD:**
La bomba de alta presión (HPP) arranca con el VFD Siemens a velocidad mínima. Los turbocargadores están parados — el agua simplemente fluye a través de sus secciones de bombeo como un conducto pasivo.

**Paso 2 — Cebado hidráulico:**
El agua presurizada por la HPP sola (sin boost de turbos) atraviesa la 1ª etapa de membranas, genera el primer concentrado que cruza el Interstage Turbo y pasa a la 2ª etapa.

**Paso 3 — Activación en cascada:**
La 2ª etapa genera rechazo a alta presión (~60-83 bar). Esta salmuera entra a la turbina del Interstage Turbo → empieza a girar → genera boost. Luego fluye a la turbina del Feed Turbo → ambos turbos comienzan a aportar presión.

**Paso 4 — Ajuste y estabilización:**
A medida que los turbos asumen carga: el VFD reduce la velocidad de la HPP, las válvulas de boquilla integradas regulan el flujo de salmuera, y el bypass se ajusta para prevenir sobre-presurización.

**Paso 5 — Régimen estable:**
El sistema alcanza equilibrio donde la HPP aporta solo 37-49 bar y los turbos aportan el resto (+14 a +21 bar el Feed, +11 a +17 bar el Interstage). El consumo energético específico (SEC) en régimen es de **3.98 kWh/m³** — cumpliendo con amplio margen la garantía contractual de 4.71 kWh/m³."

---

## SECCIÓN 9: ADAPTACIÓN A CAMBIOS DE SALINIDAD

### Narración:
"El diseño BiTurbo™ responde dinámicamente a variaciones en la salinidad del agua de alimentación. Según los 10 escenarios modelados en el Process Calculation Rev B:

### Alta Salinidad (53,000 ppm TDS) — Condición de Diseño Máxima
- **Presiones de membrana**: 1ª etapa 62-70 bar / 2ª etapa 75-85 bar
- **Bypass cerrado**: Qbyp = 0.0 m³/h para ambos turbos
- **Válvulas boquilla**: posición **Part** (parcialmente cerrada)
- **SEC**: 3.98 kWh/m³
- El sistema opera a máxima carga, toda la energía de salmuera se aprovecha

### Baja Salinidad (43,000 ppm TDS) — Condición de Diseño Mínima
- **Presiones de membrana**: 1ª etapa 51-54 bar / 2ª etapa 60-65 bar
- **Feed Turbo**: Bypass cerrado (0.0 m³/h), boquilla **Part**
- **Interstage Turbo**: Bypass ABIERTO (1.4-1.5 m³/h), boquilla **Open**
- **SEC**: 4.84-5.09 kWh/m³ (aún dentro de garantía)
- El bypass desvía salmuera excedente para no sobre-revolucionar el turbo

Esta adaptación es automática a través de las válvulas integradas en cada HPB-60. La pérdida de eficiencia al abrir la boquilla es de solo 1.5%."

---

## SECCIÓN 10: SISTEMA CIP (CLEAN-IN-PLACE)

### Narración:
"Para mantener las membranas en óptimas condiciones, el módulo incluye un sistema completo de limpieza en sitio (CIP):

- **Tanque CIP** (TK-09-001): 6.1 m³, HDPE, dimensionado para lavar las 6 vessels de la 1ª etapa en un ciclo
- **Calentador CIP** (REL-09-001): 20 kW eléctrico
- **Bomba CIP** (BH-09-002): centrífuga SS316, 57 m³/h a 4.0 bar
- **Filtro de cartuchos CIP** (FIL-09-002): SS316, 57 m³/h, 17 cartuchos de 1 micrón

**Químicos de limpieza:**
- Ácido cítrico: concentración 30%, dosificación 20,000 ppm, ~673 L por ciclo
- Hidróxido de sodio (NaOH): concentración 50%, dosificación 1,000 ppm, ~16 L por ciclo

El circuito CIP es completamente independiente del proceso — tiene su propia bomba, filtro y calentador."

---

## SECCIÓN 11: BALANCE DE ENERGÍA Y EFICIENCIA GLOBAL

### Narración:
"Ahora el dato más importante: ¿cuánta energía ahorra el sistema BiTurbo™?

Sin recuperación de energía, la bomba HPP tendría que generar TODA la presión necesaria (~70-85 bar para 53k TDS). Con el BiTurbo™:
- La bomba solo genera 37-49 bar
- Los turbos proveen los 21-38 bar restantes — SIN CONSUMO ELÉCTRICO ADICIONAL

**Consumo Energético Específico (SEC) medido:**

| Escenario | TDS (ppm) | Temp (°C) | Membrana | Presión Feed (bar) | SEC (kWh/m³) |
|---|---|---|---|---|---|
| Mínimo | 43,000 | 24°C | Y0 | 50.82 | 4.84 |
| Nominal | 43,000 | 19°C | Y0 | 51.64 | 4.84 |
| Nominal | 43,000 | 19°C | Y1 | 52.14 | 4.88 |
| Intermedio | 43,000 | 19°C | Y5 | 54.71 | 5.09 |
| Máxima carga | 53,000 | 19°C | Y0 | 62.57 | Garantía contractual ≤4.71 |
| Máx + 10% seguridad | 53,000 | 19°C | Y1+10% | 69.53 | — |

**Garantía contractual**: SEC ≤ 4.71 kWh/m³. BW Water reporta SEC de 3.98 kWh/m³ con un **15.5% de margen** sobre la garantía."

---

## SECCIÓN 12: RESUMEN EJECUTIVO Y CIERRE

### Narración:
"En resumen, este módulo RO de segunda etapa con tecnología BiTurbo™ representa una solución compacta y eficiente para maximizar la recuperación de agua en la planta desaladora de Taltal:

**Cifras clave:**
- 🔹 Alimentación: 49 m³/h de salmuera SWRO (43k-53k mg/L TDS)
- 🔹 Producción: 21 m³/h de agua permeada (<230 mg/L TDS)
- 🔹 Recuperación: 42.86%
- 🔹 70 membranas en 10 vessels, configuración 6:4
- 🔹 2 turbocargadores HPB-60 que recuperan hasta 37.7 bar de presión
- 🔹 1 bomba FEDCO MSD-7016 con VFD Siemens
- 🔹 SEC: 3.98 kWh/m³ (15.5% bajo garantía)
- 🔹 Operación 24/7 dentro de un contenedor

El diseño es robusto: materiales Super Duplex 2507 en todo el camino húmedo, membranas LG UHP de última generación, y un sistema de recuperación de energía que reduce drásticamente el consumo eléctrico."

---

## GLOSARIO DE TÉRMINOS TÉCNICOS DEL VIDEO

| Término | Definición |
|---|---|
| **TDS** | Total Dissolved Solids — sólidos totales disueltos (mg/L) |
| **SWRO** | Seawater Reverse Osmosis — ósmosis inversa de agua de mar |
| **UHPRO** | Ultra High Pressure Reverse Osmosis |
| **BiTurbo™** | Configuración de dos turbocargadores en serie (FEDCO) |
| **HPB-60** | Modelo de turbocargador hidráulico FEDCO |
| **SEC** | Specific Energy Consumption — consumo energético específico (kWh/m³) |
| **VFD** | Variable Frequency Drive — variador de frecuencia |
| **CIP** | Clean-In-Place — limpieza en sitio |
| **Flux** | Flujo por unidad de área de membrana (L/m²/h) |
| **NDP** | Net Driving Pressure — presión neta de impulso |
| **Boost** | Incremento de presión aportado por un turbocargador |
| **Qbyp** | Caudal de bypass de salmuera alrededor del turbocargador |
| **LSI** | Langelier Saturation Index — indicador de tendencia a precipitar CaCO₃ |

---

*Script generado con datos reales de las Entregas BW Water Revisions B / Process Calculation P22-CD-09-009-001 Rev B / Datasheets aprobados Entregas 6, 7 y 8 — Proyecto BAE 12803*
