# SCRIPT DE PRESENTACIÓN: Módulo RO de Segunda Etapa con Tecnología BiTurbo™ — Planta Desaladora Taltal

## INSTRUCCIONES PARA NOTEBOOKLM
> Este documento es un guion estructurado para generar una PRESENTACIÓN (slide deck) tipo "detailed_deck" sobre el módulo de ósmosis inversa de segunda etapa. Cada sección corresponde a una o más diapositivas. Incluir tablas de datos cuando se indiquen, gráficos conceptuales del flujo de proceso, y usar los valores numéricos EXACTOS proporcionados. La presentación debe ser apta para una audiencia técnico-ejecutiva: ingenieros de proyecto, gerencia de operaciones y revisores contractuales.

---

## DIAPOSITIVA 1: PORTADA

**Título:** Módulo de Ósmosis Inversa de Segunda Etapa para Tratamiento de Salmuera
**Subtítulo:** Tecnología BiTurbo™ FEDCO — Planta Desaladora PD Taltal
**Datos adicionales:**
- Fabricante: BW Water Americas Inc. (Job 25007)
- Cliente: ADASA / Aguas de Antofagasta
- Ingeniería de Referencia: Process Calculation P22-CD-09-009-001 Rev B (Enero 2026)
- 12 entregas técnicas / 52 documentos revisados

---

## DIAPOSITIVA 2: PROBLEMA Y SOLUCIÓN

**Título:** ¿Por qué un segundo paso de ósmosis inversa sobre la salmuera?

**El Problema:**
- Las plantas SWRO convencionales descartan salmuera con 43,000-53,000 mg/L TDS
- Este rechazo contiene agua potencialmente aprovechable
- En zonas de escasez hídrica como Taltal (Atacama), cada m³ cuenta

**La Solución:**
- Un módulo RO de segunda etapa que trata la salmuera SWRO como alimentación
- Produce **21 m³/h adicionales** de agua tratada (<230 mg/L TDS)
- Recupera un **42.86%** adicional del flujo de salmuera
- Contenido en un container: operación 24/7, indoor

---

## DIAPOSITIVA 3: PARÁMETROS DE DISEÑO

**Título:** Bases de Diseño del Módulo

| Parámetro | Valor |
|---|---|
| **Alimentación** | Salmuera de rechazo SWRO |
| **TDS de entrada** | 43,000 – 53,000 mg/L |
| **Temperatura** | 19°C – 24°C |
| **pH** | 6 – 9 |
| **Turbidez máxima** | 1 NTU , SDI₁₅ < 5 |
| **Gravedad específica** | 1.05 |
| **Caudal de alimentación** | 49 m³/h |
| **Caudal de permeado** | 21 m³/h |
| **Caudal de rechazo** | 28 m³/h |
| **Recuperación del sistema** | 42.86% |
| **Calidad de permeado** | < 230 mg/L TDS |
| **Horas de operación** | 24 h/día |
| **Ubicación** | Indoor (contenedor), nivel de suelo |

---

## DIAPOSITIVA 4: DIAGRAMA DE FLUJO DEL PROCESO (PFD)

**Título:** Flujo de Proceso — P22-DWG-09-009-01 Rev B

**Instrucción visual:** Generar un diagrama que muestre el recorrido del agua en el siguiente orden, con los TAGs de cada equipo:

```
Salmuera SWRO → TK-09-002 Antiincrustante → BDS-09-001/002 Dosificación
       ↓
MZE-09-001 Mezclador Estático (PVC)
       ↓
FIL-09-001 Filtro Cartuchos RO (49 m³/h, 1μm, FRP)
       ↓
BH-09-001 Bomba HP FEDCO MSD-7016 (49 m³/h @ 49.4 bar)
       ↓
SIP-09-001 Feed Turbocharger HPB-60 [Sección Bomba] → Boost +14 a +21 bar
       ↓
BOI-09-001 → 1ª Etapa RO (6 vessels × 7 membranas LG SW 400 SR)
       ↓ Permeado 13 m³/h                    ↓ Concentrado 36 m³/h
    Colector Permeado              SIP-09-002 Interstage Turbo [Sección Bomba] → Boost +11 a +17 bar
                                              ↓
                                   BOI-09-002 → 2ª Etapa RO (4 vessels × 7 membranas LG UHP)
                                              ↓ Permeado 8 m³/h    ↓ Rechazo 28 m³/h @ 60-83 bar
                                           Colector         SIP-09-002 [Turbina] → Recupera energía
                                                                     ↓ Salmuera @ 47-54 bar
                                                            SIP-09-001 [Turbina] → Recupera energía
                                                                     ↓ Salmuera @ 1 bar → Descarte
```

---

## DIAPOSITIVA 5: EQUIPOS PRINCIPALES

**Título:** Equipos Principales del Módulo — Datos Rev B

| TAG | Equipo | Fabricante | Capacidad | Material |
|---|---|---|---|---|
| BH-09-001 | Bomba HP | FEDCO | 49 m³/h @ 49.4 bar, 83 kW | Super Duplex 2507 |
| SIP-09-001 | Feed Turbocharger | FEDCO | 49/28 m³/h, boost 20.9 bar | Super Duplex 2507 |
| SIP-09-002 | Interstage Turbocharger | FEDCO | 36/28 m³/h, boost 16.8 bar | Super Duplex 2507 |
| BOI-09-001 | 1ª Etapa RO | BW Water/LG/Protec | 6 vessels, 42 membranas SW 400 SR | FRP |
| BOI-09-002 | 2ª Etapa RO | BW Water/LG/Protec | 4 vessels, 28 membranas UHP | FRP |
| FIL-09-001 | Filtro Cartuchos RO | — | 49 m³/h, 12 cartuchos 1μm | FRP |
| BH-09-002 | Bomba CIP | — | 57 m³/h @ 4 bar | SS316 |
| TK-09-001 | Tanque CIP | — | 6.1 m³ | HDPE |
| REL-09-001 | Calentador CIP | — | 20 kW eléctrico | — |
| MZE-09-001 | Mezclador Estático | — | — | PVC |
| BDS-09-001/002 | Bombas Dosificadoras | — | 2×100%, 2.3 LPH @ 16 bar | — |

---

## DIAPOSITIVA 6: BOMBA DE ALTA PRESIÓN — FEDCO MSD-7016

**Título:** Corazón Mecánico: Bomba FEDCO MSD-7016

**Datos de rendimiento (punto de diseño):**
| Parámetro | Valor |
|---|---|
| Tipo | Centrífuga horizontal, 16 etapas |
| Caudal | 49.0 m³/h |
| Presión de descarga | 51.4 bar |
| Eficiencia | 80.9% |
| Potencia absorbida | 83.1 kW |
| RPM | 3,006 |
| NPSHR | 4.4 m |
| Peso bomba | 415.9 kg |

**Motor ABB:**
| Parámetro | Valor |
|---|---|
| Potencia | 125 HP (93 kW), 380V/50Hz/3φ |
| Eficiencia | 95% |
| FLA | 167.8 A |
| Encapsulamiento | TEFC, IP66 |
| Peso | 706.2 kg |

**VFD:** Siemens SINAMICS G120X 110 kW (modelo 6SL3220-3YE46-0UF0)

**Nota importante:** La bomba NO entrega toda la presión que necesitan las membranas. Solo genera 37-49 bar. Los dos turbocargadores proveen los 14-38 bar adicionales sin consumo eléctrico.

---

## DIAPOSITIVA 7: SISTEMA BiTurbo™ — RECUPERACIÓN DE ENERGÍA

**Título:** Tecnología BiTurbo™ FEDCO: Dos Turbocargadores HPB-60 en Serie

**Punto clave:** Dos equipos de solo 27.7 kg cada uno que recuperan la energía hidráulica de la salmuera de rechazo y la reutilizan para presurizar la alimentación — eliminando la necesidad de una bomba mayor.

| | Feed Turbo (SIP-09-001) | Interstage Turbo (SIP-09-002) |
|---|---|---|
| **Feed Flow** | 49.0 m³/h | 36.0 m³/h |
| **Brine Flow** | 28.0 m³/h | 28.0 m³/h |
| **Máx. Boost** | 20.9 bar | 16.8 bar |
| **Eficiencia** | 70.3% | 73.1% |
| **Material** | Super Duplex 2507 | Super Duplex 2507 |
| **Dimensiones** | 288×279×254 mm | 288×279×254 mm |
| **Peso** | 27.7 kg | 27.7 kg |

**Principio:** La salmuera de rechazo a alta presión (~83 bar) pasa por las turbinas de ambos equipos, transfiriendo su energía hidráulica al flujo de alimentación a través de las secciones de bombeo. La salmuera sale finalmente a ~1 bar.

---

## DIAPOSITIVA 8: MEMBRANAS — CONFIGURACIÓN Y TECNOLOGÍA

**Título:** 10 Vessels, 70 Membranas, 2 Tecnologías

**Configuración:** Arreglo en serie 6:4 (1ª Etapa → 2ª Etapa)

| | 1ª ETAPA (BOI-09-001) | 2ª ETAPA (BOI-09-002) |
|---|---|---|
| **Membranas** | LG SW 400 SR | LG SW 400R G2 **UHP** |
| **Vessels** | 6 × Protec BPV-8-1200-SP-7 | 4 × Protec BPV-8-1800-SP-7 |
| **Elementos** | 42 (7/vessel) | 28 (7/vessel) |
| **Presión rating** | 1,200 psi (82.7 bar) | 1,800 psi (124 bar) |
| **Rechazo sales** | 99.85% | 99.85% |
| **Área activa unitaria** | 400 ft² (37 m²) | 380 ft² (35 m²) |
| **Permeado** | 13 m³/h | 8 m³/h |
| **Flux** | 8.3 lmh | 7.8 lmh |
| **Rango presión operación** | 51 – 54 bar | 62 – 85 bar |

**¿Por qué UHP en la 2ª etapa?** La presión osmótica del concentrado enriquecido (~75,500 mg/L TDS) supera los 53 bar. Se necesitan membranas capaces de operar continuamente hasta 120 bar.

---

## DIAPOSITIVA 9: 10 ESCENARIOS DE OPERACIÓN BiTurbo™

**Título:** Modelación BiTurbo™ — 10 Condiciones de Operación Verificadas

| # | TDS (ppm) | Temp | Membrana | P feed 1ª (bar) | P feed 2ª (bar) | P rechazo 2ª (bar) | HPP ΔP (bar) | Feed Boost (bar) | Interstage Boost (bar) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 53,000 | 19°C | Y1+10% | 69.53 | 84.81 | 83.33 | 48.9 | 20.9 | 16.8 |
| 2 | 53,000 | 19°C | Y0+10% | 68.83 | 84.11 | 82.62 | 48.5 | 20.6 | 16.8 |
| 3 | 53,000 | 19°C | Y1 | 63.21 | 77.10 | 75.75 | 44.8 | 18.7 | 15.4 |
| 4 | 53,000 | 19°C | Y0 | 62.57 | 76.46 | 75.11 | 44.5 | 18.4 | 15.4 |
| 5 | 53,000 | 24°C | Y1 | 62.11 | 76.01 | 74.67 | 44.2 | 18.3 | 15.4 |
| 6 | 53,000 | 24°C | Y0 | 61.59 | 75.49 | 74.16 | 43.8 | 18.0 | 15.4 |
| 7 | 43,000 | 19°C | Y1 | 52.14 | 62.03 | 60.68 | 37.7 | 14.7 | 11.4 |
| 8 | 43,000 | 19°C | Y0 | 51.64 | 61.53 | 60.18 | 37.5 | 14.4 | 11.4 |
| 9 | 43,000 | 24°C | Y1 | 51.21 | 61.11 | 59.77 | 37.3 | 14.2 | 11.4 |
| 10 | 43,000 | 24°C | Y0 | 50.82 | 60.72 | 59.38 | 37.1 | 14.0 | 11.4 |

**Nota:** Los escenarios #1 y #2 incluyen margen de seguridad del 10% en ambas etapas. Los escenarios Y5 (membrana de 5 años) no se incluyen en la tabla BiTurbo pero sí en la modelación LG Chem.

---

## DIAPOSITIVA 10: ARRANQUE Y SECUENCIA OPERACIONAL

**Título:** Secuencia de Arranque del Sistema BiTurbo™

**Paso 1 — Arranque de HPP con VFD**
- VFD Siemens arranca la bomba a velocidad mínima
- Turbocargadores: sin giro, actúan como conductos pasivos
- Presión inicial: solo la que produce la HPP

**Paso 2 — Cebado Hidráulico**
- Agua forzada a través de membranas 1ª y 2ª etapa
- Se genera el primer flujo de rechazo

**Paso 3 — Activación en Cascada**
- Rechazo de 2ª etapa → Turbina Interstage → gira → genera boost
- Salmuera del Interstage → Turbina Feed → gira → boost adicional

**Paso 4 — Estabilización**
- VFD reduce velocidad de HPP (la bomba trabaja menos)
- Válvulas integradas HPB-60 regulan flujo de salmuera
- Bypass se ajusta según condiciones

**Paso 5 — Régimen Estable**
- HPP: aporta 37-49 bar | Feed Turbo: +14-21 bar | Interstage Turbo: +11-17 bar

---

## DIAPOSITIVA 11: ADAPTACIÓN A CAMBIOS DE SALINIDAD

**Título:** Respuesta Dinámica del Sistema a Variaciones de TDS

**Alta Salinidad (53,000 ppm):**
- Presiones elevadas: 1ª etapa 62-70 bar / 2ª etapa 75-85 bar
- Bypass cerrado en ambos turbos (Qbyp = 0.0 m³/h)
- Válvula boquilla en posición **Part** (parcialmente cerrada)
- Máxima recuperación de energía

**Baja Salinidad (43,000 ppm):**
- Presiones menores: 1ª etapa 51-54 bar / 2ª etapa 60-65 bar
- Feed Turbo: bypass cerrado, boquilla Part
- Interstage Turbo: bypass **ABIERTO** (1.4-1.5 m³/h), boquilla **Open**
- Pérdida de eficiencia: solo 1.5% (Aux noz eff loss = 0.015)

**Conclusión:** El bypass actúa como válvula de alivio de energía cuando la salinidad baja, evitando sobre-presurización y sobre-revolución del turbo.

---

## DIAPOSITIVA 12: CONSUMO ENERGÉTICO Y EFICIENCIA

**Título:** Balance Energético — SEC vs Garantía Contractual

**Consumo Energético Específico (SEC):**

| Escenario | TDS | Temp | Membrana | Feed Pressure | SEC |
|---|---|---|---|---|---|
| Operación nominal | 43,000 | 19°C | Y0 | 51.64 bar | **4.84 kWh/m³** |
| Con envejecimiento 1 año | 43,000 | 19°C | Y1 | 52.14 bar | **4.88 kWh/m³** |
| Con envejecimiento 5 años | 43,000 | 19°C | Y5 | 54.71 bar | **5.09 kWh/m³** |

**Garantía contractual BW Water:** SEC ≤ **4.71 kWh/m³**
**SEC reportado por BW Water (53k TDS):** **3.98 kWh/m³**
**Margen sobre garantía:** **15.5%**

**Comparativa sin BiTurbo™ (estimada):**
- Sin recuperación de energía, la bomba HPP necesitaría generar 70-85 bar completos
- El SEC superaría los 8-10 kWh/m³
- El sistema BiTurbo™ reduce el consumo en aproximadamente un **50-60%**

---

## DIAPOSITIVA 13: SISTEMA CIP

**Título:** Limpieza en Sitio (Clean-In-Place)

| Equipo | Especificación |
|---|---|
| Tanque CIP (TK-09-001) | 6.1 m³, HDPE |
| Calentador (REL-09-001) | 20 kW eléctrico |
| Bomba CIP (BH-09-002) | 57 m³/h @ 4 bar, SS316 |
| Filtro CIP (FIL-09-002) | 57 m³/h, 17 cartuchos 1μm, SS316 |

**Químicos:**
| Reagente | Concentración | Dosis | Consumo/Ciclo |
|---|---|---|---|
| Ácido Cítrico | 30% | 20,000 ppm | 673 L |
| NaOH | 50% | 1,000 ppm | 16 L |

**Dimensionamiento:** El tanque CIP se calculó para lavar los 6 vessels de la 1ª etapa (volumen total vessels + piping = 5.1 m³ + factor 1.1 seguridad).

---

## DIAPOSITIVA 14: CALIDAD DEL PERMEADO

**Título:** Calidad del Agua Producida — Modelación LG Chem Design v3.3

| Componente | Feed (mg/L) | Permeado Compuesto (mg/L) | Rechazo (mg/L) |
|---|---|---|---|
| **Sodio** | 13,447 | 59.5 – 86.2 | 23,506 |
| **Cloruro** | 23,702 | 97.0 – 134.7 | 41,438 |
| **Magnesio** | 1,462 | 1.4 – 2.0 | 2,559 |
| **Sulfato** | 3,362 | 1.4 – 1.9 | 5,887 |
| **Calcio** | 506 | 0.5 – 0.7 | 885 |
| **Potasio** | 474 | 2.5 – 3.4 | 828 |
| **Bicarbonato** | 221 | 1.6 – 2.3 | 386 |
| **Boro** | 7.5 | 1.3 – 1.7 | 12 |
| **Sílice** | 2.1 | 0.01 | 3.7 |
| **TDS Total** | 43,191 | **165 – 229** | **75,470 – 75,520** |
| **pH** | 7.60 | 5.93 – 6.07 | 7.73 |

**Índices de saturación del concentrado:**
- LSI: 1.61 (tendencia a precipitación CaCO₃ — requiere antiincrustante)
- CaSO₄: 59% de saturación
- Stiff-Davis Index: 0.08

---

## DIAPOSITIVA 15: OBSERVACIONES CRÍTICAS DE LA REVISIÓN TÉCNICA

**Título:** Estado de la Revisión Técnica — Entregas BW Water

**Aspectos positivos confirmados:**
- ✅ SEC 3.98 kWh/m³ cumple garantía contractual (4.71 kWh/m³) con 15% margen
- ✅ 65% de los documentos aprobados (categorías 1 y 2)
- ✅ Materiales SDSS 2507 consistentes en toda la línea húmeda
- ✅ Cambio de tanque HDPE→LMDPE aceptado con justificación técnica

**Observaciones pendientes de resolución:**
- ⚠️ PLC especificado a 60Hz — Chile opera a 50Hz (viola ET 5.4.7)
- ⚠️ Solo 1 A/C instalado — ET exige n+1 redundancia (mínimo 2 unidades)
- ⚠️ Falta memoria de cálculo térmico del A/C
- ⚠️ 4 valores distintos de potencia HP Pump en documentos: 93/86/92/83 kW
- ⚠️ Discrepancia CIP Pump: 11 kW (Utility) vs 15 kW (Oferta) — 27% diferencia

---

## DIAPOSITIVA 16: RESUMEN EJECUTIVO

**Título:** Módulo RO BiTurbo™ Taltal — Resumen de Capacidades

| Parámetro | Valor |
|---|---|
| **Alimentación** | 49 m³/h, salmuera SWRO 43k-53k mg/L |
| **Producción** | 21 m³/h permeado (<230 mg/L TDS) |
| **Recuperación** | 42.86% |
| **Membranas** | 70 elementos, 10 vessels (6+4) |
| **Tecnología 1ª Etapa** | LG SW 400 SR (1200 psi) |
| **Tecnología 2ª Etapa** | LG SW 400R G2 UHP (1800 psi) |
| **Bomba HP** | FEDCO MSD-7016, 83 kW absorbidos |
| **Recuperación Energía** | 2× FEDCO HPB-60 BiTurbo™ |
| **SEC** | 3.98 kWh/m³ (garantía ≤4.71) |
| **Operación** | 24/7, containerizado |
| **Material húmedo** | Super Duplex SS 2507 |
| **Entregas técnicas** | 12 entregas / 52 documentos |

---

*Script generado con datos reales de las Entregas BW Water Rev B / Process Calculation P22-CD-09-009-001 Rev B / Datasheets aprobados — Proyecto BAE 12803*
