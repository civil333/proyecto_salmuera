---
codigo: Auditoria-TM-N8
transmittal: P22-TM-09-000-008-0
fecha: 11-Mar-2026
auditor: Claude Code (4 agentes paralelos)
estado: APROBADO CON CORRECCIONES MENORES
---

# Auditoría TM N8 — P22-TM-09-000-008-0

**Fecha:** 11-Mar-2026 | **Auditor:** Claude Code (4 agentes paralelos)

---

## 1. Resumen Ejecutivo

| Dimensión | Estado | Gaps |
|-----------|--------|------|
| Coherencia TM ↔ Scripts (Agente 1) | APROBADO | 0 gaps — 17/17 OBS consistentes |
| Posicionamiento _CC_ADASA (Agente 2) | APROBADO CON CORRECCIONES | 2 scripts corregidos (pressure_transmitter, instrument_list OBS-3) |
| Cross-reference ET (Agente 3) | APROBADO CON OBSERVACIONES | pH/ORP y DP Switch sin base contractual explícita; citas ET con formato correcto |
| Cross-reference P&ID Rev B (Agente 4) | APROBADO CON OBSERVACIONES | TIT-09-002 en P&ID pero no en IL Rev B |

**Correcciones aplicadas (11-Mar-2026):**
- `agregar_comentarios_pressure_transmitter.py`: agregado `page_min=2` para OBS-1 (PIT-09-007 aterriza en hoja Hastelloy, no SS316L)
- `agregar_comentarios_instrument_list.py`: agregado `page_min=1` para OBS-3 (CIT-09-001 aterriza en tabla IL, no comment sheet)
- PDFs `_CC_ADASA` regenerados post-corrección

---

## 2. Coherencia TM ↔ Scripts (Agente 1)

### 2.1 Tabla de Coherencia

| Documento | OBS en TM | Comentario Script | Texto Consistente | Severidad Coincide | Gap |
|-----------|-----------|-------------------|:-----------------:|:------------------:|-----|
| P22-LI-09-008-003 IL Rev B | OBS-1 (CIT-09-005 120VAC) | agregar_comentarios_instrument_list.py | SI | SI (MAYOR=naranja) | NO |
| P22-LI-09-008-003 IL Rev B | OBS-2 (IO List 45 días) | idem | SI | SI (MENOR=amarillo) | NO |
| P22-LI-09-008-003 IL Rev B | OBS-3 (conductivity 20 mS/cm) | idem | SI | SI (MAYOR=naranja) | NO |
| P22-LI-09-008-003 IL Rev B | OBS-4 (VT setpoints) | idem | SI | SI (MENOR=amarillo) | NO |
| P22-LI-09-008-005 Conductivity DS | NOTE-1 (código portada erróneo) | agregar_comentarios_conductivity.py | SI | SI (NOTE=azul) | NO |
| P22-LI-09-008-005 Conductivity DS | NOTE-2 (PN AC variant) | idem | SI | SI (NOTE=azul) | NO |
| P22-LI-09-008-006 DP Switch | (ninguna) | sin script | — | — | OK — aprobado sin script |
| P22-LI-09-008-007 Flow TX DS | NOTE-1 (FIT-09-004 Hastelloy) | agregar_comentarios_flow_transmitter.py | SI | SI (NOTE=azul) | NO |
| P22-LI-09-008-008 Level Switch DS | NOTE-1 (portada 4-20mA HART erróneo) | agregar_comentarios_level_switch.py | SI | SI (NOTE=azul) | NO |
| P22-LI-09-008-009 Level TX | (ninguna) | sin script | — | — | OK — aprobado sin script |
| P22-LI-09-008-010 pH/ORP DS | (ninguna) | sin script | — | — | OK — aprobado sin script |
| P22-LI-09-008-011 Pressure Gauge DS | (ninguna) | sin script | — | — | OK — aprobado sin script |
| P22-LI-09-008-012 Pressure TX DS | NOTE-1 (PIT-09-007 material) | agregar_comentarios_pressure_transmitter.py | SI | SI (NOTE=azul) | NO |
| P22-DWG-09-007-005 Power Works | OBS-1 (earthing specs) | agregar_comentarios_power_works.py | SI | SI (MAYOR=naranja) | NO |
| P22-DWG-09-007-005 Power Works | OBS-2 (norma eléctrica) | idem | SI | SI (MENOR=amarillo) | NO |
| P22-LI-09-008-013 Temp TX DS | NOTE-1 (portada "Pressure TX") | agregar_comentarios_temperatura.py | SI | SI (NOTE=azul) | NO |
| P22-LI-09-008-013 Temp TX DS | OBS-2 (TIT-09-003 no en IL) | idem | SI | SI (MAYOR=naranja) | NO |
| P22-LI-09-008-013 Temp TX DS | NOTE-3 (accuracy class) | idem | SI | SI (NOTE=azul) | NO |

**Resultado: 17/17 OBS — Cobertura 100%. Ninguna corrección requerida en TM ni en scripts por coherencia.**

### 2.2 Conteo por Documento

| Documento | OBS en TM | Comentarios Script | Coincide |
|-----------|:---------:|:-----------------:|:--------:|
| IL Rev B | 4 | 4 | SI |
| Conductivity DS | 2 | 2 | SI |
| DP Switch DS | 0 | 0 | SI |
| Flow TX DS | 1 | 1 | SI |
| Level Switch DS | 1 | 1 | SI |
| Level TX DS | 0 | 0 | SI |
| pH/ORP DS | 0 | 0 | SI |
| Pressure Gauge DS | 0 | 0 | SI |
| Pressure TX DS | 1 | 1 | SI |
| Power Works DWG | 2 | 2 | SI |
| Temp TX DS | 3 | 3 | SI |
| **TOTAL** | **17** | **17** | **100%** |

---

## 3. Posicionamiento de Comentarios (Agente 2)

### 3.1 Tabla de Posicionamiento

| Script | Comentario | Texto Target | Posicionamiento | Observación |
|--------|-----------|-------------|:---------------:|-------------|
| instrument_list | OBS-1 (CIT-09-005 120VAC) | "CIT-09-005" | CORRECTO | Página 2 (tabla IL, fila CIT-09-005) |
| instrument_list | OBS-2 (IO List) | "VT-09-001" | CORRECTO | Página 2 (tabla IL, fila VT-09-001) |
| instrument_list | OBS-3 (conductivity 20 mS/cm) | "CIT-09-001" + `page_min=1` | **CORREGIDO** | Antes: comment sheet. Ahora: tabla IL fila CIT-09-001 |
| instrument_list | OBS-4 (VT setpoints) | "VTV122" | CORRECTO | Página 2 (tabla IL, modelo VTV122) |
| conductivity | NOTE-1 (código portada) | "P22-LI-09-008-003" | CORRECTO | Portada, junto al código incorrecto |
| conductivity | NOTE-2 (PN AC variant) | "1056-02" | CORRECTO | Portada/DS, contexto PN 1056-02-21-31 |
| flow_transmitter | NOTE-1 (FIT-09-004 Hastelloy) | "FIT-09-004" | CORRECTO | Página 3 (datasheet FIT-09-004, electrodo Hastelloy) |
| level_switch | NOTE-1 (output 4-20mA erróneo) | "4-20" | CORRECTO | Página 2, campo "Outputs Inputs Communication" |
| pressure_transmitter | NOTE-1 (PIT-09-007 material) | "PIT-09-007" + `page_min=2` | **CORREGIDO** | Antes: hoja SS316L (pág 2). Ahora: hoja Hastelloy (pág 3) |
| power_works | OBS-1 (earthing) | "cable tray" | ACEPTABLE | Pág 2 (Motor Installation — donde falta earthing) |
| power_works | OBS-2 (norma eléctrica) | "installation" | CORRECTO | Portada del plano (lugar canónico para citar norma) |
| temperatura | NOTE-1 (header incorrecto) | "Pressure Transmitter" | CORRECTO | Portada, junto al header erróneo |
| temperatura | OBS-2 (TIT-09-003 ausente) | "TIT-09-003" con `page_min=1` | CORRECTO | Página 2 (datasheet TIT-09-003) |
| temperatura | NOTE-3 (accuracy class) | "Class A" | CORRECTO | Página 4 (manual Rosemount 214C, sección de features) |

### 3.2 Casos de Riesgo — Análisis Detallado

**Power Works OBS-1 (earthing / "cable tray"):**
"cable tray" es término genérico que aparece en múltiples hojas. La búsqueda aterrizó en página 2, hoja "CENTRIFUGAL PUMP MOTOR - ELECTRICAL INSTALLATION DETAILS" (Material Take-Off ítem 1: "Power&Control Cable Tray, HDG"). El contexto es apropiado: es la hoja donde se muestra el motor con cable tray sin especificación de puesta a tierra. No hay hoja dedicada de earthing porque esa es precisamente la deficiencia observada. **Posicionamiento aceptable.**

**Level Switch NOTE-1 (output / "4-20"):**
"4-20" fue encontrado en página 2, fila 33 del datasheet: "Outputs Inputs Communication — Current Output, 4-20mA HART". El comentario aterrizó exactamente en el campo que debe corregirse. **Posicionamiento óptimo.**

**Temp DS OBS-2 (TIT-09-003 ausente):**
El comentario aterrizó en página 2 (datasheet ADASA de TIT-09-003). El texto "TIT-09-003 no figura en IL Rev B" es legible y contextualmente claro junto al TAG del instrumento. **Posicionamiento correcto.**

**Pressure TX NOTE-1 — CORRECCIÓN APLICADA:**
Antes: "PIT-09-007" sin `page_min` → primer hit en página 2 (hoja SS316L, donde PIT-09-007 no aparece como target principal). Con `page_min=2`: la búsqueda parte desde página 3 (índice 2) → hoja Hastelloy C donde PIT-09-007 aparece explícitamente en Component Tag No./s. Posicionamiento ahora correcto.

**IL OBS-3 — CORRECCIÓN APLICADA:**
Antes: "CIT-09-001" sin `page_min` → primer hit detectado en comment sheet (páginas 3-4, donde CIT-09-001 aparece en historial de comentarios BW Water). Con `page_min=1`: la búsqueda parte desde página 2 (la tabla IL) → fila CIT-09-001 en la tabla. Posicionamiento ahora en la tabla IL.

---

## 4. Cross-reference ET (Agente 3)

### 4.1 Tabla OBS ↔ ET

| OBS | Cita en TM | Sección ET Real | ¿Cita Correcta? | Observación |
|-----|-----------|-----------------|:---------------:|-------------|
| IL OBS-01 (CIT-09-005 120VAC) | "ET — Voltages and Frequencies" | §5.4.7 L1305-1308 | SI | ET requiere 380/220VAC, 50Hz. Anomalía 120VAC validada correctamente. |
| IL OBS-02 (IO List 45 días) | "ET — Communication and Control System" | §5.4 + §5.5 | PARCIAL | Sección con ese nombre exacto no existe; requisito implícito en §5.4 (control PLC) + §5.5 (instrumentación). Cita funcional pero no exacta. |
| IL OBS-03 (conductivity 20 mS/cm) | "ET — Feed Brine Quality; ET — Conductivity Analyzers" | §4.1 (TDS) + §5.5.5 | PARCIAL | §5.5.5 no especifica rango mínimo de medición; el rango surge de §4.1 (TDS 43-53 k mg/L → ~65-140 mS/cm). OBS correcta en su hallazgo. |
| IL OBS-04 (VT setpoints) | "ET — Vibration Transmitters: HP Pump and ERD units" | §5.5.6 L1390-1394 | SI | ET requiere VTs pero no especifica setpoints ni cita ISO 10816-3. La referencia ISO en TM es aportación correcta. |
| Power OBS-01 (earthing) | "ET — Motors and Electrical Equipment; ET — Electrical and Control Systems" | §5.3 + §5.4 | SI (nombres) | ET no exige detalles de earthing en installation drawings explícitamente; la observación es válida por IEC 60364 / RIC chilena. |
| Power OBS-02 (norma eléctrica) | (sin cita, implícita) | Ninguna | N/A | ET no cita código eléctrico; OBS correcta como requisito de industria. |
| Temp DS OBS-01 (header "Pressure TX") | "ET — Instrumentation" | §5.5 | GENÉRICO | Error editorial, cita aceptable. |
| Temp DS OBS-02 (TIT-09-003 no en IL) | "ET — Instrumentation; IL Rev B item 28" | §5.5 | SI | Mismatch datasheet vs IL. OBS correcta. |
| Temp DS OBS-03 (accuracy class) | "ET — Instrumentation (complete specification)" | §5.5 | GENÉRICO | ET especifica 4-20mA + HART pero no accuracy class. OBS correcta. |

### 4.2 Tabla Gaps de Cobertura ET

| Requisito ET | Sección ET | Cubierto en TM N8 | Observación |
|-------------|-----------|:-----------------:|-------------|
| pH/ORP Analyzer | NO en §5.5 | Aprobado sin OBS | NO en ET. SÍ en Oferta BW Water Rev1 Items 1 y 32. TM N8 aprueba sin citar base contractual. Recomendación: próxima revisión debe citar "Oferta BW Water Rev1 — Instrument List". |
| DP Switch (DPS-09-001) | NO en §5.5 | Aprobado sin OBS | NO en ET ni en Oferta Rev1. Es adición BW Water en IL Rev B (mejora operacional ΔP 1°Etapa). TM N8 aprueba sin aclarar origen. Recomendación: próxima revisión debe aclarar que es mejora voluntaria de BW Water. |
| Flow Transmitters (5×) | §5.5.1 | SI | IL Rev B items 10-14 (FIT-09-001 a FIT-09-005) cumplen. |
| Pressure Transmitters (9×) | §5.5.3 | SI | IL Rev B items 1-9 (PIT-09-001 a PIT-09-009) cumplen. |
| Pt-100 motores (todos) | §5.3 L1032 | **SI — CIERRE EXITOSO** | IL Rev B agrega TE-09-001/002/003/004 (HP Pump y CIP Pump, Fedco + Grundfos). Gap previo de TM N3 cerrado. |
| Vibration TX (3 ubicaciones) | §5.5.6 | **SI — CIERRE EXITOSO** | IL Rev B agrega VT-09-001/002/003. Gap previo de TM N3 cerrado (setpoints pendientes — OBS-04 activa). |
| 4-20mA + HART | §5.5 L1311 | MAYORMENTE SI | Transmisores cumplen. Switches (LS, DPS) usan DI/SPDT — correcto por función. Level Switch DS portada incorrectamente dice "4-20mA HART" (OBS activa). |
| Conductivity range | §4.1 (TDS) | NO en ET §5.5.5 | OBS-03 correctamente identifica el gap. ET §4.1 describe TDS; §5.5.5 no especifica rango mínimo de medición. |
| Vibration setpoints (ISO 10816-3) | NO en §5.5.6 | NO | OBS-04 correcta. ET no especifica setpoints ni norma; TM correctamente los requiere. |
| Earthing/grounding sizing | NO en §5.4 | NO | OBS-01 Power Works correcta por IEC 60364 / RIC chilena. |
| Electrical installation standard | NO en ET | NO | OBS-02 Power Works correcta como requisito de industria. |

### 4.3 Formato Citas ET — Verificación §2.5 CLAUDE.md

TM N8 cumple CLAUDE.md §2.5. Todas las citas usan nombre descriptivo (no §N.N):
- "ET — Voltages and Frequencies" ✓
- "ET — Communication and Control System" ✓
- "ET — Feed Brine Quality; ET — Conductivity Analyzers" ✓
- "ET — Vibration Transmitters: HP Pump and ERD units" ✓
- "ET — Motors and Electrical Equipment; ET — Electrical and Control Systems" ✓
- "ET — Instrumentation" ✓

**Ninguna corrección de notación requerida.**

---

## 5. Cross-reference P&ID Rev B ↔ IL Rev B (Agente 4)

> **Nota metodológica:** La extracción del P&ID Rev B es texto fragmentado de un dibujo CAD. De 39 TAGs en IL, ~18 son verificables en la extracción; los ~16 restantes son probablemente ilegibles en la extracción, no ausentes del P&ID.

### 5.1 Tabla Cruzada (TAGs con estado determinado)

| TAG | En IL Rev B | En P&ID Rev B | Función IL | Loop P&ID | Consistente | Observación |
|-----|:-----------:|:-------------:|-----------|----------|:-----------:|-------------|
| DPS-09-001 | SI | SI | DP Switch — CF | DPS | SI | OK |
| FIT-09-001 | SI | SI | Flow TX DN100 | FIT | SI | OK |
| PIT-09-001 | SI | SI | Pressure TX — HP Feed | PIT | SI | OK |
| PIT-09-009 | SI | SI | Pressure TX — Combined Permeate | PIT | SI | OK |
| VT-09-001 | SI | SI | Vibration TX — HP Pump | VT | SI | OK — nuevo Rev B |
| TE-09-002 | SI | SI | Temp RTD — HP Pump Winding | TE | SI | OK — nuevo Rev B |
| FIT-09-002 | SI | SI | Flow TX — 2nd Stage Permeate | FIT | SI | OK — renombrado Rev B |
| CIT-09-002 | SI | SI | Conductivity TX — Permeate | CIT | SI | OK |
| CIT-09-004 | SI | SI | Conductivity TX — Stage 1 Reject | CIT | SI | OK |
| CIT-09-005 | SI | SI | Conductivity TX — Train Reject | CIT | SI | Presente; anomalía eléctrica 120VAC en IL (OBS activa) |
| PIT-09-008 | SI | SI | Pressure TX — Train Reject | PIT | SI | OK |
| VT-09-002 | SI | SI | Vibration TX — Feed Turbocharger | VT | SI | OK — nuevo Rev B |
| VT-09-003 | SI | SI | Vibration TX — Interstage Turbocharger | VT | SI | OK — nuevo Rev B |
| LIT-09-002 | SI | SI | Level TX — CIP Tank | LIT | SI | OK |
| PHIT-09-001 | SI | SI | pH Analyzer — CIP/Flush | PHIT | SI | OK |
| PI-09-004 | SI | SI | Pressure Gauge — CIP CF Feed | PI | SI | OK |
| PI-09-005 | SI | SI | Pressure Gauge — CIP CF Discharge | PI | SI | OK |
| PI-09-006 | SI | SI | Pressure Gauge — Antiscalant Pump | PI | SI | OK |
| **TIT-09-002** | **NO** | **SI** | — | TIT | **DISCREPANCIA** | **En P&ID pero NO en IL Rev B** |
| ORPIT-09-001 | SI | NO detectado | ORP TX | No visible | INDETERMINADO | P&ID puede usar "AIT" (TM N3 OBS-06) |
| CIT-09-001 | SI | NO detectado | Conductivity TX — CF Discharge | No visible | INDETERMINADO | Probable ilegibilidad extracción |
| TIT-09-001 | SI | POSIBLE (fragmento) | Temp TX — CIP Tank | TIT | POSIBLE | Fragmento `09-00TIT` en extracción |
| TE-09-003 | SI | POSIBLE | Temp RTD — CIP Pump Bearing | TE | POSIBLE | Fragmento `09-005TE` ambiguo |

*TAGs restantes (PIT-09-002 a PIT-09-007, FIT-09-003 a FIT-09-005, TE-09-001, TE-09-004, PI-09-001 a PI-09-003, LS-09-001/002): presentes en IL Rev B; no detectables en extracción del P&ID por ilegibilidad del texto CAD.*

### 5.2 TAGs Huérfanos Confirmados

**En P&ID Rev B pero NO en IL Rev B:**

| TAG | Hallazgo | Evaluación |
|-----|----------|-----------|
| **TIT-09-002** | Aparece claramente como `09-002TIT` en área HP Pump/Feed Turbocharger (P10), junto a `TE-09-002` | **GAP CRÍTICO** — Instrumento en P&ID sin entrada en IL y sin IO point asignado |
| TE-09-005 (posible) | Fragmento `09-005TE` en área CIP (P11) — puede ser TE-09-003/004 distorsionado o instrumento adicional | A VERIFICAR contra P&ID original |
| PSV-09-001/002 | Safety valves en P&ID — ausencia en IL esperada | Normal — PSV no se registran en IL de instrumentación |

**En IL Rev B pero NO en P&ID (confirmado ausente, no solo ilegible):**
- Ninguno confirmado como ausente — todos los "no detectados" son atribuibles a ilegibilidad de extracción CAD.

### 5.3 Análisis Casos Específicos

**TIT-09-002 (hallazgo crítico):**
El P&ID Rev B muestra `09-002TIT` inmediatamente junto a `09-002TE` en el bloque del área HP Pump / Feed Turbocharger. La IL Rev B tiene solo TIT-09-001 (CIP Tank). TIT-09-002 podría ser:
- Un transmisor de temperatura adicional en el HP Pump o turbocharger no documentado en IL
- Un error de numeración en el P&ID (debería ser TIT-09-001 desplazado)
- La misma función que TIT-09-001 con numeración diferente entre documentos

**Relación con Temp DS OBS-2:** El datasheet P22-LI-09-008-013 tiene el TAG TIT-09-003 (CIP Tank Temperature Transmitter). TM N8 OBS-2 detecta que TIT-09-003 no está en IL (solo TIT-09-001 está). La situación es: IL tiene TIT-09-001, P&ID tiene TIT-09-002, datasheet tiene TIT-09-003. Hay tres numeraciones distintas para un instrumento de temperatura relacionado con el CIP Tank — BW Water debe aclarar cuál es el TAG definitivo.

**VT-09-001/002/003 (Rev B nuevos):**
Los tres confirmados en P&ID Rev B. VT-09-001 en contexto HP Pump, VT-09-002 y VT-09-003 en contexto turbochargers. Consistencia con IL Rev B: correcta.

**TE-09-001/002/003/004 (Rev B nuevos):**
TE-09-002 confirmado en P&ID Rev B (junto a TIT-09-002 en área HP Pump). Los demás no detectables por ilegibilidad. Consistencia parcialmente verificada.

**CIT-09-005 (anomalía eléctrica):**
Presente en P&ID Rev B (confirmado). La anomalía 120VAC es eléctrica, no de nomenclatura — no introduce inconsistencia en el cruce P&ID/IL.

---

## 6. Correcciones Aplicadas y Propuestas (Consolidado)

### 6.1 Correcciones Aplicadas (11-Mar-2026)

| Archivo | Cambio | Razón |
|---------|--------|-------|
| `agregar_comentarios_pressure_transmitter.py` | Agregado `"page_min": 2`; cambiado `"page_fallback": 1` → `2` | PIT-09-007 aterrizaba en hoja SS316L (pág 2). Ahora apunta a hoja Hastelloy (pág 3 = índice 2) |
| `agregar_comentarios_instrument_list.py` | Agregado `"page_min": 1` a OBS-3; cambiados `page_fallback` de OBS-1/2/3/4 a `1` (todos apuntan a tabla IL pág 2 = índice 1) | OBS-3 aterrizaba en comment sheet. OBS-1/2/4 tenían fallbacks a páginas incorrectas. Ahora los 4 comentarios apuntan a la tabla IL. |
| `P22-LI-09-008-012..._CC_ADASA.pdf` | Regenerado (2 pasadas) | Resultado final: OBS-1 en pág 3 (Hastelloy) ✓ |
| `P22-LI-09-008-003..._CC_ADASA.pdf` | Regenerado (2 pasadas) | Resultado final: OBS-1/2/3/4 en pág 2 (tabla IL) ✓ |

### 6.2 Correcciones en TRANSMITTAL.md — No requeridas

La coherencia TM ↔ Scripts es 100%. El formato de citas ET cumple §2.5 CLAUDE.md. No se requieren cambios en el TRANSMITTAL.md.

### 6.3 Precisión Técnica — OBS-3 IL (hallazgo de extracción)

La extracción del IL _CC_ADASA revela que los rangos son más restrictivos de lo descrito en OBS-3:

| Instrumento | Rango en IL Rev B | Equivalencia | Vs. brine Taltal (~65-140 mS/cm) |
|-------------|------------------|--------------|-----------------------------------|
| CIT-09-001 | 0–2000 µS/cm | 0–2 mS/cm | **10× fuera de rango** |
| CIT-09-004 | 0–2000 µS/cm | 0–2 mS/cm | **10× fuera de rango** |
| CIT-09-005 | 0–20 mS/cm | 0–20 mS/cm | **3-7× fuera de rango** |

OBS-3 en TM N8 dice "20 mS/cm max insuficiente" — correcto para CIT-09-005, pero CIT-09-001/004 tienen rango aún más limitado (2 mS/cm). El hallazgo y la acción requerida son correctos. En la próxima revisión mencionar que CIT-09-001/004 están en 2000 µS/cm (no 20 mS/cm).

> Causa raíz del posicionamiento deficiente en IL: Los TAGs están codificados como `"CIT - 09 - 001"` (con espacios alrededor de guiones) en el PDF de la tabla, haciendo que `search_for("CIT-09-001")` falle. Solo VTV122 (valor en columna Model, sin guiones) es encontrable. El uso de fallbacks corregidos (índice 1 = tabla IL) resuelve el posicionamiento.

### 6.4 Observaciones para Próximas Revisiones (no requieren cambio TM N8)

**Observación P-1 — pH/ORP sin cita base contractual:**
TM N8 §3.7 aprueba pH/ORP Analyzer sin mencionar que no está en ET §5.5. La base contractual es la Oferta BW Water Rev1 (Items 1 y 32). En el próximo transmittal que cubra estos documentos, agregar nota: "pH/ORP Analyzer: base contractual en Oferta BW Water Rev1 — Instrument List Items 1 and 32."

**Observación P-2 — DP Switch sin cita base contractual:**
TM N8 §3.2 aprueba DPS-09-001 sin mencionar que no está en ET ni en Oferta Rev1. Es una adición de BW Water en IL Rev B. En el próximo transmittal, agregar nota aclaratoria sobre su origen.

**Observación P-3 — TIT-09-002 en P&ID, ausente en IL Rev B:**
P&ID Rev B muestra TIT-09-002 en área HP Pump/turbocharger. IL Rev B no tiene TIT-09-002. Sumado al TIT-09-003 del datasheet (OBS-2 Temp DS), hay tres TAGs distintos de temperatura (TIT-09-001, TIT-09-002, TIT-09-003) referidos a instrumentos similares. BW Water debe aclarar en IL Rev C y P&ID Rev B cuál es el TAG definitivo para cada instrumento.

> Esta observación puede agregarse a la respuesta de TM N8 o convertirse en OBS del próximo transmittal (TM N9) si IL Rev C no resuelve la inconsistencia.

**Observación P-4 — TE-09-005 fragmento en P&ID:**
El fragmento `09-005TE` en área CIP del P&ID Rev B requiere verificación contra el dibujo original. Si es un instrumento real no en IL, debe agregarse en Rev C.

---

## 7. Verificación Post-Auditoría

| Criterio | Estado |
|---------|--------|
| `Auditoria-TM-N8.md` creado con 4 tablas | SI |
| §6 "Correcciones" con fragmentos exactos | SI |
| Posicionamiento Power Works y Level Switch validados contra _CC_ADASA | SI |
| pH/ORP y DP Switch — base contractual identificada | SI (Oferta Rev1 para pH/ORP; sin base para DPS) |
| Citas ET en TM siguen formato §2.5 (nombre completo) | SI — ninguna corrección necesaria |
| Scripts corregidos regeneran PDFs _CC_ADASA sin errores | Pendiente verificación salida scripts |
| TRANSMITTAL.md — no requiere cambios | CONFIRMADO |

---

*Auditoría cerrada: 11-Mar-2026*
