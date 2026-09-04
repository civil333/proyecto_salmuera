---
tipo: Compilado Interno — Documento Interno ADASA
transmittal: TM N14 — P22-TM-09-000-014-0
entrega: E26 / Submittal 25007-0026 + E27 / Submittal 25007-0027 + E28 / Submittal 25007-0028 + E29 / Submittal 25007-0029
fecha: 15-Apr-2026
nota: DOCUMENTO INTERNO — NO ENVIAR A BW WATER
---

# COMPILADO TM N14 — ENTREGA 26 / 27 / 28 / 29
## **NO ENVIAR — USO INTERNO ADASA**

---

## 1. Resumen General

TM N14 consolida cuatro entregas de BW Water recibidas entre el 08-Apr y el 15-Apr-2026, abarcando 11 documentos en total: 1 de arquitectura de control, 2 de listas (valvulas, IO List), 1 de transferencia de datos (DTL), 1 de instrumentos (IL), y 6 datasheets.

| Entrega | Submittal | Fecha recepcion | Documentos | Veredicto parcial |
|---------|-----------|-----------------|------------|-------------------|
| E26 | 25007-0026 | 08-Apr-2026 | Control System Architecture Rev D | Code 1 |
| E27 | 25007-0027 | 10-Apr-2026 | Valve List Rev D, DS Pressure Gauge Rev B | Code 2, Code 1 |
| E28 | 25007-0028 | 13-Apr-2026 | IO List Rev C, IL Rev C, DTL Rev B, DS Conductivity Rev B, DS pH/ORP Rev B, DS Temperature Rev B, DS Vibration Rev B | 4x Code 2, 3x Code 1 |
| E29 | 25007-0029 | 15-Apr-2026 | DS Flow Transmitter Rev B | Code 1 |

**Veredicto global: Code 2 — Approved as Noted** (7 documentos Code 1, 4 documentos Code 2).

**Observaciones cerradas por E26+E27+E28+E29:** 9 items heredados cerrados (ver Seccion 6).
**Observaciones nuevas TM N14:** 5 NOTEs (1 existente de E27, 4 nuevas de E28).
**Items que permanecen abiertos:** 5 observaciones heredadas + TM N13 NOTE-01 y NOTE-02 para IFC.

---

## 2. SECCION E26 — Control System Architecture Rev D

### 2.1 Datos de la Entrega

| Campo | Valor |
|-------|-------|
| Entrega | E26 |
| Submittal | 25007-0026 |
| Fecha recepcion | 08-Apr-2026 |
| Documento | P22-CD-09-004-001 Rev D — Control System Architecture |
| Tipo | DWG (Drawing), IFA (Issued For Approval) |
| De | Fitri Indriyani (BW Water) |
| A | Luis Rivera Gonzalez (ADASA) |

### 2.2 Trazabilidad

| Rev | Entrega | Submittal | TM | Fecha revision | Veredicto | OBS levantadas |
|-----|---------|-----------|-----|----------------|-----------|----------------|
| A | E4 | 25007-0004 | TM N2 | 26-Jan-2026 | 2 — Approved as Noted | OBS-01 a OBS-10 |
| B | E11 | 25007-0011 | TM N4 | 05-Feb-2026 | 2 — Approved as Noted | OBS-04, OBS-09, OBS-12 + CCS 8 items |
| C | E18 | 25007-0018 | TM N10 | 12-Mar-2026 | 2 — Approved as Noted | OBS-04, NOTE-02, NOTE-05 |
| **D** | **E26** | **25007-0026** | **TM N14** | **08-Apr-2026** | **1 — Approved** | **Sin observaciones** |

### 2.3 Hallazgos de la Revision

Rev D tiene 5 paginas: caratula con historia de revisiones (A-D), notas del diagrama y leyenda, diagrama de arquitectura (2 paginas graficas), y CCS respondiendo a TM N10.

**Notas del diagrama (sin cambios respecto a Rev C):**
1. Fiber optic converter panel y fiber box por otros
2. Instalacion y materiales de campo por otros
3. HUB1: 9 spare ports; HUB2: 1 spare port; HUB3: 2 spare ports
4. Protocolo: DCS y Digital Power Meter = Modbus TCP/IP; HMI, PLC CPU, VFD y Motorized Valve = Ethernet/IP

**Equipos en diagrama (confirmados):** BH-09-001, BH-09-002, REL-09-001, SAI-09-001, SSAA-09-002, SSAA-09-001A/B, BDS-09-001A/B, 14 instrumentos de campo, 1 motorized valve, analyzers.

### 2.4 Evaluacion CCS — Respuesta a TM N10

**TM N10 OBS-04 (UPS 8h autonomia) — CERRADO:**
CCS declara: UPS-BAT B/PU/FF/24DC/40AH, 2 unidades, 8h runtime a 4.35A full load. Verificacion: 40 Ah / 4.35 A = 9.2 horas > 8 horas. Cumple ET §5.4 L1088-1089. La carga de 4.35A es consistente con los componentes tipicos del sistema (PLC ~0.8A, HMI ~0.6A, modulos I/O ~1.5A, switches Ethernet ~0.5A, gateway PLX32 ~0.3A, otros ~0.75A). Configuracion probable: UPS controller + battery module (serie Phoenix Contact QUINT). El desglose detallado de cargas deberia documentarse en el Control Philosophy Rev B para referencia de comisionamiento.

**TM N10 NOTE-05 (HMI Screenshots) — ABIERTO:**
P22-BREAD-09-008-001 comprometido en TM N4 CCS (03-Feb-2026). No recibido en ninguna entrega hasta E28. A 13-Apr-2026 lleva **69 dias** pendiente. Es un entregable separado, no una deficiencia de la arquitectura de control.

### 2.5 Veredicto E26

**Code 1 — Approved.** OBS-04 cerrada, sin nuevas deficiencias MAJOR. Las notas sobre UPS load calculation y HMI screenshots son informacionales y se trackean en observaciones heredadas.

---

## 3. SECCION E27 — Valve List Rev D + DS Pressure Gauge Rev B

### 3.1 Datos de la Entrega

| Campo | Valor |
|-------|-------|
| Entrega | E27 |
| Submittal | 25007-0027 |
| Fecha recepcion | 10-Apr-2026 |
| Documentos | P22-LI-09-005-002 Rev D (Valve List), P22-LI-09-008-011 Rev B (DS Pressure Gauge) |
| De | Fitri Indriyani (BW Water) |

---

### 3.2 Valve List Rev D — P22-LI-09-005-002

#### 3.2.1 Trazabilidad

| Rev | Entrega | Submittal | TM | Fecha | Veredicto | OBS levantadas |
|-----|---------|-----------|-----|-------|-----------|----------------|
| A | E7 | 25007-0007 | TM N2 | 26-Jan-2026 | 2 — Approved as Noted | OBS |
| B | E9 / E13 | 25007-0009/0013 | TM N3 / TM N6 | 28-Jan / 27-Feb-2026 | 3 / 2 — Code 3 luego 2 | 4 duplicados |
| C | E19 | 25007-0019 | TM N11 | 17-Mar-2026 | 3 — To be Revised | OBS-01, OBS-02, NOTE-01 |
| **D** | **E27** | **25007-0027** | **TM N14** | **10-Apr-2026** | **2 — Approved as Noted** | **NOTE-01** |

#### 3.2.2 Analisis de Cierre de Observaciones

**TM N11 OBS-01 (VE-09-007 duplicado) — CERRADO:**
TAG VE-09-007 ya no esta duplicado. Item 44 retiene VE-09-007 (DN80 butterfly, motorized, SWRO Reject 1st Stage, ANSI 900#). El antiguo item 64, que tambien portaba VE-09-007 en Rev C, fue reasignado a VM-09-120 (DN15 ball valve, manual, SWRO 2nd Stage Reject, ANSI 900#). Verificado: VE-09-007 aparece exactamente una vez. Ambos TAGs presentes en P&ID Rev C aprobado (TM N13).

**TM N11 OBS-02 (PSV-09-002 duplicado) — CERRADO:**
TAG PSV-09-002 ya no esta duplicado. Item 104 retiene PSV-09-002 (DN15 PSV, Antiscalant service). Item 112 de Rev C fue eliminado — la lista contiene ahora 111 items. Ver NOTE-01 sobre confirmacion de esta eliminacion.

**TM N11 NOTE-01 (area-07 error) — CERRADO:**
Todos los TAGs area-07 corregidos a area-09: VM-07-005 → VM-09-005, VM-07-031 → VM-09-031, VE-07-009 → VE-09-009. Este error fue levantado originalmente en TM N3 OBS-13 y persistio a traves de Rev B y Rev C.

**TM N6 4 duplicados originales — CERRADO:**
Los cuatro TAGs duplicados originales (VM-09-015, VE-09-008, VE-09-009, VM-09-065) identificados en TM N6 estan completamente resueltos en Rev D. Los TAGs renombrados (VM-09-151, VM-09-120, VE-09-016, VM-09-041) verificados contra P&ID Rev C aprobado — cada TAG aparece en su ubicacion correcta tanto en la Valve List como en el P&ID.

**Verificacion sistematica:** 111 items revisados. Cero TAGs duplicados, cero errores area-07, actuaciones conformes a ET §5.2.3 (criterio funcional, no dimensional).

#### 3.2.3 NOTE-01 — Confirmacion eliminacion Item 112 (MINOR)

Rev C contenia 112 items. Rev D contiene 111 items. Item 112 (segunda PSV-09-002, valvula de seguridad) fue eliminado en lugar de recibir un TAG unico como sugeria TM N11 OBS-02. BW Water debe confirmar si esta eliminacion es una decision de diseno (valvula removida del alcance) o un descuido. Implicacion: si la segunda PSV fue eliminada del diseno, verificar que la proteccion por sobrepresion del sistema antiscalant sigue siendo adecuada con una sola PSV.

**Veredicto: Code 2 — Approved as Noted.**

---

### 3.3 DS Pressure Gauge Rev B — P22-LI-09-008-011

#### 3.3.1 Trazabilidad

| Rev | Entrega | TM | Veredicto |
|-----|---------|-----|-----------|
| A | E15 | TM N8 (09-Mar-2026) | 1 — Approved |
| **B** | **E27** | **TM N14** | **1 — Approved** |

#### 3.3.2 Cambio

CCS indica un unico cambio: diaphragm seal para PI-09-003 a PI-09-006 (CIP Water y Antiscalant service) cambiado de Wika 990.10 (lower body acero inoxidable) a Wika 990.31 (lower body polipropileno, diafragma EPDM con foil PTFE). Motivacion declarada: compatibilidad con tuberias PVC en sistemas CIP y antiscalant.

El cambio de material es tecnicamente apropiado: polipropileno es quimicamente compatible con soluciones CIP y quimicos de dosificacion antiscalant. PTFE-lined EPDM provee resistencia a corrosion adecuada. Rating de presion del diaphragm seal (0 a 10 bar max) consistente con rango operativo ANSI 150# de tuberias CIP/antiscalant.

PI-09-001 y PI-09-002 (Filtered Water service) retienen Wika 233.50 Bourdon tube sin diaphragm seal — correcto para servicio de agua limpia.

**Veredicto: Code 1 — Approved.** Sin observaciones.

---

## 4. SECCION E28 — 7 Documentos de Instrumentacion y Control

### 4.1 Datos de la Entrega

| Campo | Valor |
|-------|-------|
| Entrega | E28 |
| Submittal | 25007-0028 |
| Fecha recepcion | 13-Apr-2026 |
| Cantidad documentos | 7 |
| De | BW Water Americas Inc. |

| N | Codigo | Descripcion | Rev | Veredicto |
|---|--------|-------------|-----|-----------|
| 1 | P22-LI-09-008-001 | IO List | C | **Code 2** |
| 2 | P22-LI-09-008-003 | Instrument List | C | **Code 2** |
| 3 | P22-LI-09-008-004 | Data Transfer List (Modbus TCP/IP) | B | **Code 2** |
| 4 | P22-LI-09-008-005 | DS Conductivity Analyzer | B | Code 1 |
| 5 | P22-LI-09-008-010 | DS pH/ORP Analyzer | B | Code 1 |
| 6 | P22-LI-09-008-013 | DS Temperature Transmitter | B | Code 1 |
| 7 | P22-LI-09-008-014 | DS Vibration Transmitter | B | Code 1 |

---

### 4.2 IO List Rev C — P22-LI-09-008-001

#### 4.2.1 Trazabilidad

| Rev | Entrega | TM | Fecha | Veredicto |
|-----|---------|-----|-------|-----------|
| A | E7 | TM N2 | 26-Jan-2026 | Revisado |
| B | E18 | TM N10 | 12-Mar-2026 | 2 — Approved as Noted |
| **C** | **E28** | **TM N14** | **13-Apr-2026** | **2 — Approved as Noted** |

Revision: C, Fecha documento: 31-Mar-2026. Preparado por Davis/BT, revisado GHY/NHH, aprobado JFR.

#### 4.2.2 Contenido General

141 items (antes 112 en Rev B). Crecimiento de 29 items explicado por:
- Adicion VE09-015 (Feed TC isolation, 4 senales Ethernet/IP) — items 103-106
- Adicion TIT-09-006 (CIP tank temperature, 4-20mA AI) — item 108
- Adicion PHIT-09-006 (pH CIP, 4-20mA AI) — item 122
- Adicion TE-09-003/004 (CIP pump winding/bearing temperature, RTD 3-wire) — items 120-121
- Reorganizacion y renumeracion de items existentes

#### 4.2.3 CCS — Respuesta a TM N10

El CCS (pagina 5 del PDF) tiene 2 items:

**Item 1 — TM N10 OBS-01 (TE vs TIT) — RESUELTO:**
Respuesta BW Water: "5069-IY4 is a universal input module that acts as a direct reader for sensors. The instrument does not have a transmitter and the signal is not modulated over 4-20mA range so RTD sensor for motor pump will remain TE instead of TIT."

**Analisis interno (Van Doorn):** La explicacion es tecnicamente correcta. El modulo 5069-IY4 de Allen-Bradley es un modulo de entrada universal que lee directamente la resistencia del RTD sin necesidad de un transmisor intermedio. La senal no pasa por conversion 4-20mA — se lee como variacion de resistencia (ohmica). Por tanto:
- TE (Temperature Element) es la designacion ISA correcta para un sensor sin transmisor dedicado
- TIT (Temperature Indicating Transmitter) seria incorrecto porque implica un transmisor que modula senal 4-20mA

La confusion en TM N10 surgio porque en UHPRO de segunda etapa, las RTDs de motores se conectan directamente al 5069-IY4, mientras que en plantas convencionales tipicamente van a traves de un transmisor de cabezal (head-mount transmitter) tipo Rosemount 644.

**Resolucion del conflicto TIT-09-003 → separacion TE-09-003 / TIT-09-006:**
- TE-09-003 = CIP pump winding temperature (RTD directo al 5069-IY4, sin transmisor)
- TIT-09-006 = CIP tank temperature (Rosemount 214C + 644 transmitter, 4-20mA HART)
- El conflicto de servicio (mismo TAG para dos servicios distintos) queda resuelto

Verificado en DTL Rev B: TE-09-001/002 en 5069-IY4 (addresses 40075/40076, data type REAL), TE-09-003/004 en 5069-IY4 (40077/40078, REAL), TIT-09-006 en 5069-IF8 (30028, data type 4000~20000). Consistente.

**Item 2 — TM N10 OBS-02 (revision general) — CERRADO:**
Respuesta generica "HAS BEEN REVISED". Verificado en contenido del documento: cambios incorporados. Cierre confirmado mediante verificacion cruzada con DTL Rev B.

#### 4.2.4 Nuevos Items Rev C

| Item | TAG | Descripcion | Senal | Rev columna |
|------|-----|-------------|-------|-------------|
| 103-106 | VE09-015 | Feed TC isolation motorized valve | 4 senales Ethernet/IP (BOOL x2, REAL x2) | C |
| 108 | TIT09-006 | CIP tank temperature transmitter | 4-20mA AI | C |
| 120 | TE09-003 | CIP pump winding temperature | RTD 3-wire | C |
| 121 | TE09-004 | CIP pump bearing temperature | RTD 3-wire | C |
| 122 | PHIT09-006 | CIP pump discharge pH analyzer | 4-20mA AI | C |

#### 4.2.5 NOTE-02 — Discrepancia voltaje analyzers (MENOR)

La columna REMARKS del IO List Rev C muestra "220VAC Supply" para los siguientes instrumentos:
- Item 24: ORPIT09-001A (ORP analyzer)
- Item 25: CIT09-001B (Conductivity analyzer)
- Item 47: CIT09-004 (Conductivity analyzer)
- Item 59: CIT09-002 (Conductivity analyzer) — Rev A, pero REMARKS identico
- Item 61: CIT09-003 (Conductivity analyzer) — Rev A
- Item 83: CIT09-005 (Conductivity analyzer)
- Item 122: PHIT09-006 (pH analyzer)

La Instrument List Rev C (seccion 4.3 abajo) indica "24VDC" como power supply para estos mismos instrumentos. Ademas, los datasheets de los Rosemount 1056 (transmitter comun a conductividad, ORP y pH) especifican "20 to 30 Vdc" como power supply.

La discrepancia es relevante: si los analyzers requieren efectivamente 220VAC, la interfaz electrica con el panel LCP cambia (se necesita un circuito de alimentacion AC separado en lugar del bus 24VDC). Para ADASA, la definicion correcta de voltaje afecta el diseno de la interfaz de potencia en el MCC/tablero de distribucion.

**Hipotesis (Van Doorn):** Los analyzers Rosemount 1056 operan con 24VDC (per datasheet). El "220VAC Supply" del IO List probablemente se refiere al suministro al enclosure externo (fan, heater, iluminacion interna del shelter del analyzer) o es un error heredado de la Rev A. Requiere aclaracion formal de BW Water para que ADASA pueda especificar correctamente la interfaz electrica.

**Veredicto: Code 2 — Approved as Noted** (NOTE-02).

---

### 4.3 Instrument List Rev C — P22-LI-09-008-003

#### 4.3.1 Trazabilidad

| Rev | Entrega | TM | Fecha | Veredicto |
|-----|---------|-----|-------|-----------|
| A | E7 | TM N2 | Ene-2026 | Revisado |
| B | E16 | TM N8 | 09-Mar-2026 | 2 — Approved as Noted |
| **C** | **E28** | **TM N14** | **13-Apr-2026** | **2 — Approved as Noted** |

Revision: C, Fecha documento: 16-Mar-2026. Preparado por VOON, revisado BT/NHH, checked GHY, aprobado JFR/LPL.

#### 4.3.2 Contenido General

39 instrumentos listados (1 pagina de datos). Documento sin CCS — las respuestas a TM N8 se evaluan por comparacion directa con Rev B.

#### 4.3.3 Cierre de Observaciones TM N8

**TM N8 OBS-01 (CIT-09-005 voltaje) — CERRADO:**
CIT-09-005 ahora muestra 24VDC como power supply. Corregido respecto a Rev B.

**TM N8 OBS-02 (alineacion IO List) — CERRADO:**
Alineacion verificada entre IL Rev C y IO List Rev C. TAGs, descripciones y tipos de senal consistentes.

**TM N8 OBS-03 (rangos conductividad / tecnologia toroidal) — CERRADO:**
Cambio tecnologico fundamental implementado:
- CIT-09-001B, CIT-09-004, CIT-09-005 (servicios salmuera/rechazo): ahora Rosemount 228 (toroidal, Non-Contacting), rango 0-200 mS/cm. Correcto para concentraciones 65-133 mS/cm en servicios brine.
- CIT-09-002, CIT-09-003 (servicios permeado): mantienen Rosemount 400 (Contacting, Electrode), rango 0-20 mS/cm. Correcto para permeado.
Cumple ET §5.5.5. Confirmado en DS Conductivity Analyzer Rev B (ver seccion 4.6).

**TM N8 OBS-04 (alarmas vibracion) — PENDIENTE:**
Los setpoints de alarma de vibracion fueron diferidos a un documento separado "Alarm and Interlock Setpoints" que no ha sido entregado. Esta observacion permanece abierta como item pendiente fuera de la IL — no genera nueva OBS en TM N14 sobre la IL directamente, pero se trackea como compromiso pendiente de BW Water.

#### 4.3.4 Cambios Notables en Rev C

**Transmisores de vibracion:**
VT-09-001, VT-09-002, VT-09-003 ahora especifican Wilcoxon PCH420V-M12 (antes IFM VTV122 en Rev A/B). Protocolo HART confirmado en el campo "Protocol Type" = HART. Rango instrumento: 0-127 mm/s. Material SS316L, IP67, conexion M12.

**Elementos de temperatura motor HP Pump:**
TE-09-001 (winding), TE-09-002 (bearing): Fedco PT100, DIN 44082, 3-wire RTD. Rango 60-180 C. Built-in motor. Sin transmisor dedicado (lectura directa por 5069-IY4).

**Elementos de temperatura motor CIP Pump:**
TE-09-003 (winding), TE-09-004 (bearing): Grundfos PT100, DIN 44082, 3-wire RTD. Misma configuracion que HP Pump pero fabricante Grundfos (motor CIP = Grundfos).

**TIT-09-006 (CIP Tank):**
Rosemount 214C RTD + 114C thermowell + 644 transmitter. PT100 Class A, 4-20mA HART, DN40 flange Class 150. Part number completo: 214CRWSSA1S3E0120SL / 114CE0090FAB2SC030A / 644HANAJ5M5Q4XAK1105. El sufijo "RW" en la 214C indica calibracion RW option = Class A accuracy.

**PHIT-09-006 (pH CIP):**
Rosemount 3900 sensor + 1056 transmitter. 4-20mA HART, 0-14 pH. Low Flow Cell 24091-00.

**Pressure Gauges CIP:**
PI-09-003, PI-09-004, PI-09-005 ahora incluyen Wika 990.31 diaphragm seal (polypropylene). Consistente con DS Pressure Gauge Rev B.

#### 4.3.5 NOTE-03 — Rango calibrado VT (MENOR)

El Instrument List muestra rango de instrumento 0-127 mm/s para VT-09-001/002/003. El Data Transfer List Rev B muestra 0-25 mm/s como escala Modbus para las mismas senales (items 134, 138, 143 del DTL). El PCH420V-M12 tiene rango full-scale configurable — 0-127 mm/s es el rango maximo del sensor, mientras que 0-25 mm/s es probablemente el rango calibrado para mapeo PLC (4000-20000 counts = 0-25 mm/s).

El IL deberia reflejar el rango calibrado que vera el PLC, ya que este valor se utiliza para configurar alarmas y visualizacion HMI. Si el PLC recibe 0-25 mm/s via Modbus y el IL dice 0-127 mm/s, hay riesgo de que las alarmas se configuren con el rango incorrecto. BW Water debe confirmar cual es el rango calibrado efectivo y actualizar el IL para que sea consistente con el DTL.

#### 4.3.6 NOTE-04 — Working medium "Filtered Water" (MENOR)

La columna "Working Medium" de la IL muestra "Filtered Water" para instrumentos que operan en servicios de salmuera/rechazo: PIT-09-004 (Interstage TC inlet), PIT-09-006 (2nd Stage Reject), PIT-09-007 (Feed TC inlet), PIT-09-008 (Reject discharge), CIT-09-004 (Reject conductivity), CIT-09-005 (Reject conductivity), FIT-09-004 (Reject flow). Los transmisores de vibracion (VT-09-001/002/003) tambien muestran "Filtered Water" cuando en realidad estan montados sobre carcasas de equipos sin contacto con medio de proceso — "N/A" seria mas preciso.

La etiqueta "Filtered Water" es ambigua y puede inducir error en la verificacion de compatibilidad de materiales: un instrument engineer revisando la lista asumira agua filtrada (baja salinidad, ~1-2 g/L TDS) cuando en realidad el servicio es salmuera concentrada (~55-80 g/L TDS) o rechazo de segunda etapa (~100+ g/L TDS). Los materiales de wetted parts ya estan correctamente especificados (Hastelloy C para PIT en servicio corrosivo, Tefzel para CIT en brine), pero la columna Working Medium deberia reflejar el medio real para que la verificacion sea autocontenida.

**Veredicto: Code 2 — Approved as Noted** (NOTE-03, NOTE-04).

---

### 4.4 Data Transfer List Rev B — P22-LI-09-008-004

#### 4.4.1 Trazabilidad

| Rev | Entrega | TM | Fecha | Veredicto |
|-----|---------|-----|-------|-----------|
| A | E18 | TM N10 | 12-Mar-2026 | 3 — To be Revised |
| **B** | **E28** | **TM N14** | **13-Apr-2026** | **2 — Approved as Noted** |

Revision: B, Fecha documento: 01-Apr-2026. Preparado BT, checked GHY/NHH, aprobado JFR.

#### 4.4.2 Contenido General

189 items totales en el mapa Modbus:
- Digital: items 1-80 (IB16 inputs, OB16 outputs)
- Analog inputs/outputs: items 81-189 (IF8, IY4, OF8, DPM, VFD, MOV)

6 paginas incluyendo CCS en pagina 6.

#### 4.4.3 CCS — Respuesta a TM N10

CCS en pagina 6 con 3 items (numerados 1, 2, 5 — item 3 y 4 ausentes, probablemente corresponden a observaciones que ya no aplican):

**Item 1 — TM N10 OBS-01 (Tags TE/TIT inconsistentes) — CERRADO:**
Respuesta generica "Has been revised in P22-LI-09-008-004B". Verificacion:
- TE-09-001/002 (HP Pump): en 5069-IY4, addresses 40075/40076, data type REAL. Correcto — lectura directa RTD.
- TE-09-003/004 (CIP Pump): en 5069-IY4, addresses 40077/40078, data type REAL. Correcto — lectura directa RTD.
- TIT-09-006 (CIP Tank): en 5069-IF8, address 30028, data type 4000~20000. Correcto — senal 4-20mA desde Rosemount 644.
La distincion TE (RTD directo) vs TIT (con transmisor 4-20mA) es ahora consistente entre IO List Rev C, IL Rev C y DTL Rev B. Cierre confirmado.

**Item 2 — TM N10 OBS-02 (conductividad) — CERRADO:**
Verificacion de escalas:
- CIT-09-001B: 0-200 mS/cm (item 131, 5069-IF8, address 30004). Correcto para Rosemount 228 toroidal en servicio brine.
- CIT-09-004: 0-200 mS/cm (item 142, 5069-IF8, address 30015). Correcto.
- CIT-09-005: 0-200 mS/cm (item 150, 5069-IF8, address 30023). Correcto.
- CIT-09-002: 0-200 uS/cm (item 146, address 30019). Correcto para Rosemount 400 contacting en permeado.
- CIT-09-003: 0-200 uS/cm (item 148, address 30021). Correcto.
Todas las escalas ahora reflejan los rangos reales de los instrumentos seleccionados. Cierre confirmado.

**Item 5 — TM N10 OBS-03 (VE-09-014 duplicado DI, LS ausentes) — CERRADO:**
Verificacion:
- VE-09-014: items 55-56 (DI: remote + fault) + items 119-120 (analog: position feedback + control). Total 4 entradas, NO duplicado — son 2 DI + 1 feedback + 1 control, estructura estandar para motorized valve.
- LS-09-001: item 22, address 10002.5. Presente.
- LS-09-002: item 23, address 10002.6. Presente.
Cierre confirmado.

#### 4.4.4 Nuevos Items en Rev B

| Item | TAG | Descripcion | Modbus Address |
|------|-----|-------------|----------------|
| 59-60 | VE09-015 | Feed TC isolation (DI: remote + fault) | 10004.10 / 10004.11 |
| 121 | VE09-015-SI001 | Feed TC isolation position feedback | 40041 |
| 189 | VE09-015-SIC001 | Feed TC isolation position control | 40073 |
| 155 | TIT09-006-XQ001 | CIP tank temperature | 30028 |
| 156-157 | TE09-003/004-XQ001 | CIP pump winding/bearing temperature | 40077 / 40078 |
| 158 | PHIT09-006-XQ001 | CIP pump pH analyzer | 30031 |

#### 4.4.5 NOTE-05 — Rango VT en Modbus (MENOR, cross-cutting con NOTE-03)

Items 134, 138, 143 del DTL muestran escala 0-25 mm/s para VT-09-001/002/003. El IL Rev C muestra 0-127 mm/s como rango de instrumento. Mismo hallazgo que NOTE-03 de la IL — cross-cutting. El DTL es probablemente correcto (rango calibrado para el PLC), y la IL deberia actualizarse para reflejar este rango. Requiere confirmacion de BW Water.

**Veredicto: Code 2 — Approved as Noted** (NOTE-05).

---

### 4.5 Observacion Pendiente Transversal: Alarm and Interlock Setpoints

TM N8 OBS-04 (alarmas vibracion) fue diferida por BW Water a un documento separado "Alarm and Interlock Setpoints" que no ha sido entregado. Este documento es necesario para verificar:
- High alarm (HH) y pre-alarm (H) de vibracion para HP Pump, Feed TC e Interstage TC
- Setpoints de conductividad para rechazo/desvio automatico
- Interlock de temperatura motores

Este item se mantiene como pendiente general, no como observacion contra un documento especifico de E28.

---

### 4.6 DS Conductivity Analyzer Rev B — P22-LI-09-008-005

#### 4.6.1 Trazabilidad

| Rev | Entrega | TM | Veredicto |
|-----|---------|-----|-----------|
| A | E15 | TM N8 (09-Mar-2026) | 2 — Approved as Noted |
| **B** | **E28** | **TM N14** | **1 — Approved** |

Revision: B, Fecha documento: 02-Apr-2026.

#### 4.6.2 Contenido

DOS datasheets en un solo documento:

**Datasheet 1 — CIT-09-002/003 (Permeado):**
- Sensor: Rosemount 400, Contacting, Electrode
- Materiales: SS316 body, Titanium electrodes, Viton O-ring, PEEK insulator
- Rango: 0.1 uS/cm a 2000 uS/cm
- Transmitter: Rosemount 1056, 2x 4-20mA HART, 20-30 VDC
- Servicio: Filtered Water (permeado combinado 1st+2nd stage y permeado 2nd stage)

**Datasheet 2 — CIT-09-001B/004/005 (Salmuera):**
- Sensor: Rosemount 228, Toroidal, Non-Contacting
- Materiales: Tefzel body
- Rango: 0.1 uS/cm a 2,000,000 uS/cm
- Temp sensor: Pt 100 (vs Pt 1000 del Rosemount 400)
- Transmitter: Rosemount 1056 identico
- Servicio: RO Stage 1 & 2 Reject

**Analisis (Van Doorn):** Este cambio de contacting a toroidal para servicios brine fue la observacion principal de TM N8 OBS-03. El Rosemount 228 (toroidal, sin contacto fisico con el medio) es la tecnologia correcta para conductividades >20 mS/cm y medios con alta concentracion de cloruro. Los electrodos SS316L del Rosemount 400 son incompatibles con 45,000-55,000 ppm Cl- de la salmuera de rechazo. El cambio es exactamente lo que ADASA solicito. El rango extendido a 2,000,000 uS/cm (2000 mS/cm) cubre ampliamente la conductividad esperada de la salmuera concentrada (~85-135 mS/cm).

**Veredicto: Code 1 — Approved.** Sin observaciones. Cierra TM N8 OBS-03 desde la perspectiva del datasheet.

---

### 4.7 DS pH/ORP Analyzer Rev B — P22-LI-09-008-010

#### 4.7.1 Trazabilidad

| Rev | Entrega | TM | Veredicto |
|-----|---------|-----|-----------|
| A | E15 | TM N8 (09-Mar-2026) | 1 — Approved |
| **B** | **E28** | **TM N14** | **1 — Approved** |

Revision: B, Fecha documento: 02-Apr-2026.

#### 4.7.2 Contenido

CCS muestra solo cambios de TAG respecto a Rev A:
- ORPIT-09-001 → ORPIT-09-001A
- PHIT-09-001 → PHIT-09-006

Ambos cambios alinean los TAGs con el P&ID Rev C aprobado. Especificaciones tecnicas sin cambios: Rosemount 3900 sensor, Rosemount 1056 transmitter, 4-20mA HART, rango pH 0-14, ORP -1500 a 1500 mV. Cantidad: 2 unidades.

**Veredicto: Code 1 — Approved.** Sin observaciones.

---

### 4.8 DS Temperature Transmitter Rev B — P22-LI-09-008-013

#### 4.8.1 Trazabilidad

| Rev | Entrega | TM | Veredicto | OBS levantadas |
|-----|---------|-----|-----------|----------------|
| A | E15 | TM N8 (09-Mar-2026) | 3 — To be Revised | OBS-01, OBS-02, OBS-03 |
| **B** | **E28** | **TM N14** | **1 — Approved** | **Sin observaciones** |

Revision: B, Fecha documento: 02-Apr-2026.

#### 4.8.2 CCS — Respuesta a TM N8

**TM N8 OBS-01 (Header "Pressure Transmitter") — CERRADO:**
Header corregido a "Temperature Transmitter" en Rev B. Confirmado en caratula y header del datasheet.

**TM N8 OBS-02 (TIT-09-003 conflicto servicio) — CERRADO:**
TAG renombrado de TIT-09-003 a TIT-09-006 per P&ID Rev C. Servicio: CIP Tank. Alineado con IL Rev C (item 28) y IO List Rev C (item 108). El conflicto original era que TIT-09-003 estaba asignado a CIP Tank temperature en el datasheet pero a HP Pump bearing en el IO List Rev B.

**TM N8 OBS-03 (Accuracy Class no especificada) — CERRADO:**
Part number 214CRWSSA1S3E0**1**00SL — el sufijo "RW" confirma opcion Callendar-Van Dusen para calibracion Class A. El campo "Temperature Sensor Accuracy" del datasheet ahora dice explicitamente "Class A". Longitud del sensor: 12 pulgadas (inmersion 9 pulgadas via thermowell 114C).

**Cambio adicional:** Process connection cambiada a flange DN40 Class 150 (thermowell 114C). Adecuado para insercion en tanque CIP.

#### 4.8.3 Especificaciones Verificadas

| Parametro | Valor |
|-----------|-------|
| TAG | TIT-09-006 |
| Servicio | CIP Tank temperature |
| RTD | Rosemount 214C, PT100, Class A, Single 3-Wire |
| Thermowell | Rosemount 114C, SS316/316L, DN40 flange Class 150, tapered stem |
| Transmitter | Rosemount 644H, 4-20mA HART, LCD display, IP66 |
| Power supply | 24 VDC |
| Rango medicion | -196 a 600 C (sensor), 0 a 100 C (operativo CIP) |

**Veredicto: Code 1 — Approved.** Sin observaciones.

---

### 4.9 DS Vibration Transmitter Rev B — P22-LI-09-008-014

#### 4.9.1 Trazabilidad

| Rev | Entrega | TM | Veredicto | OBS levantadas |
|-----|---------|-----|-----------|----------------|
| A | E22 | TM N12 (30-Mar-2026) | 3 — To be Revised | OBS-01 (HART), NOTE-01 (qty) |
| **B** | **E28** | **TM N14** | **1 — Approved** | **Sin observaciones** |

Revision: B, Fecha documento: 02-Apr-2026.

#### 4.9.2 Cambio de Modelo

**Modelo anterior:** IFM VTV122 — no tenia HART, lo que motivo Code 3 en TM N12.
**Modelo nuevo:** Wilcoxon PCH420V-M12 — HART 7.0 confirmado.

Este es un cambio de proveedor y modelo, no solo una actualizacion de firmware. La decision de BW Water de cambiar a Wilcoxon resuelve de raiz el problema: IFM VTV122 no ofrecia HART en ninguna variante, mientras que la serie PCH420V fue disenada con HART 7.0 como feature nativo.

#### 4.9.3 CCS — Respuesta a TM N12

**TM N12 OBS-01 (HART no especificado) — CERRADO:**
Datasheet Rev B campo "Outputs Communication": "4 to 20 mA current output with HART". Manufacturer datasheet adjunto (paginas 3-5) confirma: PCH420V-M12 = 4-20 mA + HART 7.0, tres bandas de vibracion configurables por usuario. Cumple ET §5.5 (todos los instrumentos de campo con 4-20mA + HART).

**TM N12 NOTE-01 (cantidad) — CERRADO:**
Campo Quantity: 3 unidades. TAG listing: VT-09-001 (RO HP Pump), VT-09-002 (Feed Turbocharger), VT-09-003 (Interstage Turbocharger). Consistente con P&ID Rev C y ET §5.5.7 L1390.

#### 4.9.4 Especificaciones Verificadas

| Parametro | Valor | Requisito ET |
|-----------|-------|-------------|
| Tipo sensor | PZT, Shear | Cumple |
| Modelo | Wilcoxon PCH420V-M12 | Cumple |
| Rango | 0-127 mm/s (configurable) | Cumple |
| Frecuencia | 10-1000 Hz | Cumple |
| Accuracy | +-5% | Cumple |
| Material | SS316L | Cumple |
| IP | IP67 | Cumple |
| Conexion electrica | M12 connector | Cumple |
| Power supply | 12-30 VDC | Cumple (24VDC del sistema) |
| Protocolo | 4-20mA + HART 7.0 | **Cumple** |
| Vibration limit | 500 g peak | Cumple |
| Shock limit | 5000 g peak | Cumple |

**Nota (Van Doorn):** La especificacion del PCH420V-M12 incluye tres bandas de vibracion configurables por usuario (PV, SV, TV), lo que permite monitoreo mas granular que el VTV122 (banda unica). Para la configuracion durante comisionamiento, las bandas deberian alinearse con los rangos especificados en el futuro documento "Alarm and Interlock Setpoints".

**Veredicto: Code 1 — Approved.** Sin observaciones. Cumple todos los requisitos ET para transmisores de vibracion.

---

## 5. SECCION E29 — DS Flow Transmitter Rev B

### 5.1 Datos de la Entrega

| Campo | Valor |
|-------|-------|
| Entrega | E29 |
| Submittal | 25007-0029 |
| Fecha recepcion | 15-Apr-2026 |
| Documento | P22-LI-09-008-007 Rev B — Datasheet of Flow Transmitter |
| Tipo | DOC (Document), IFA (Issued For Approval) |
| De | Fitri Indriyani (BW Water) |
| A | Luis Rivera Gonzalez (ADASA) |
| Req. Return Date | 18-Apr-2026 |

### 5.2 Trazabilidad

| Rev | Entrega | Submittal | TM | Fecha revision | Veredicto | OBS levantadas |
|-----|---------|-----------|-----|----------------|-----------|----------------|
| A | E15 | 25007-0015 | TM N8 | 09-Mar-2026 | 2 — Approved as Noted | Nota inline (FIT-09-004 fluid/medium) |
| **B** | **E29** | **25007-0029** | **TM N14** | **15-Apr-2026** | **1 — Approved** | **Sin observaciones** |

### 5.3 Hallazgos de la Revision

Documento de 60 paginas: 1 caratula con historial de revisiones (A-B), 2 hojas de especificacion BW Water (paginas 2-3), y 57 paginas de literatura del fabricante Rosemount (Product Data Sheet 00813-0300-4750, Rev CF, October 2025).

**Hoja 1 (pagina 2) — FIT-09-001/002/003/005:**
- **Make/Model:** Rosemount 8750W electromagnetico, tipo In-Line, flanged
- **Cantidad:** 4 unidades duty, 0 standby
- **Fluid/Medium:** Filtered/CIP Water — correcto para estos servicios
- **Electrodos:** SS316L — correcto para servicio agua filtrada/CIP
- **Lining:** PTFE
- **Rangos medicion:** 0-18, 0-40, 0-100 m3/h (tres rangos para diferentes TAGs)
- **Flange:** Slip-On, Raised Face, Carbon Steel, Class 150
- **Power Supply:** 12 to 42 VDC — **CORREGIDO** (Rev A decia "90 to 250 VDC")
- **Output:** 4 to 20 mA current outputs with HART — conforme ET §5.5.1
- **P&ID refs:** P22-DWG-09-009-002-P8/P9/P10

**Hoja 2 (pagina 3) — FIT-09-004:**
- **Make/Model:** Rosemount 8750W electromagnetico (mismo modelo)
- **Cantidad:** 1 unidad duty
- **Fluid/Medium:** "Concentrated Brine" — **CORREGIDO** (Rev A decia "Filtered/CIP Water")
- **Electrodos:** Nickel alloy 276 (= Hastelloy C-276) — correcto para brine concentrado (TDS estimado 75,000-93,000 mg/L, Cl- 45,000-55,000 ppm)
- **Lining:** PTFE
- **Rango medicion:** 0-60 m3/h
- **Power Supply:** 12 to 42 VDC — **CORREGIDO**
- **Output:** 4 to 20 mA current outputs with HART
- **P&ID ref:** P22-DWG-09-009-002-P9

### 5.4 Verificacion Cruzada

| Instrumento | IL Rev C | IO List Rev C | DTL Rev B | DS Rev B |
|-------------|----------|---------------|-----------|----------|
| FIT-09-001 | Item 4: Rosemount 8750W, 0-18 m3/h | Item 26: DC 4-20mA, 4 Wire 24VDC | Reg 30005: 4000-20000, 5069-IF8 | Pag 2: SS316L, 0-18 m3/h, HART |
| FIT-09-002 | Item 14: 0-18 m3/h | Item 58: DC 4-20mA | Reg 30020: 4000-20000 | Pag 2: SS316L, 0-18 m3/h |
| FIT-09-003 | Item 16: 0-100 m3/h | Item 60: DC 4-20mA | Reg 30018: 4000-20000 | Pag 2: SS316L, 0-100 m3/h |
| FIT-09-004 | Item 26: Nickel alloy 276, 0-60 m3/h | Item 85: DC 4-20mA | Reg 30025: 4000-20000 | Pag 3: Nickel alloy 276, 0-60 m3/h, "Concentrated Brine" |
| FIT-09-005 | Item 36: 0-40 m3/h | Item 123: DC 4-20mA | Reg 30032: 4000-20000 | Pag 2: SS316L, 0-40 m3/h |

**Consistencia:** Todos los FITs alineados entre los 4 documentos en modelo, material de electrodo, rango y tipo de senal. Power supply ahora consistente (12-42 VDC en DS, 24VDC en IO List — dentro del rango).

**Nota respecto a NOTE-04 (TM N14):** La IL Rev C sigue mostrando "Filtered Water" como Working Medium para FIT-09-004. El datasheet Rev B ya corrigio a "Concentrated Brine" — progreso parcial. NOTE-04 sigue vigente para la proxima revision de IL.

### 5.5 Veredicto E29

**Code 1 — Approved.** Ambas notas inline de TM N8 resueltas (fluid/medium y power supply). Sin observaciones nuevas. Cumple ET §5.5.1 integralmente.

---

## 6. Estado de Observaciones Heredadas (actualizado desde TM N13)

TM N13 tenia 13 items pendientes. TM N14 cierra 9 items y mantiene 5 abiertos (mas 2 para IFC). Se agregan 5 NOTEs nuevas.

### 6.1 Items CERRADOS por E26 + E27 + E28

| # | TM | OBS/NOTE | Documento cierre | Metodo de verificacion |
|---|-----|----------|-----------------|----------------------|
| 1 | N10 | OBS-01 (TE vs TIT) | IO List Rev C + DTL Rev B | CCS IO List + verificacion cruzada modulos 5069-IY4/IF8 |
| 2 | N10 | OBS-02 (conductividad) | DTL Rev B + IL Rev C + DS Conductivity Rev B | Escalas 0-200 mS/cm brine, 0-200 uS/cm permeado |
| 3 | N10 | OBS-03 (VE-09-014 DI) | DTL Rev B | 4 entradas = 2 DI + 1 feedback + 1 control; LS en 10002.5/6 |
| 4 | N10 | OBS-04 (UPS 8h) | CCS Rev D | UPS-BAT B/PU/FF/24DC/40AH x2, 9.2h a 4.35A |
| 5 | N11 | OBS-01 (VE-09-007 dup) | Valve List Rev D | VE-09-007 unico; item 64 → VM-09-120 |
| 6 | N11 | OBS-02 (PSV-09-002 dup) | Valve List Rev D | Item 112 eliminado; PSV-09-002 unico (item 104) |
| 7 | N11 | NOTE-01 (area-07) | Valve List Rev D | VM-07-005/031 → VM-09-005/031; VE-07-009 → VE-09-009 |
| 8 | N12 | OBS-01 (VT HART) | DS Vibration Rev B | Cambio IFM VTV122 → Wilcoxon PCH420V-M12, HART 7.0 |
| 9 | N12 | NOTE-01 (VT qty) | DS Vibration Rev B | Qty = 3 (VT-09-001/002/003) |

### 6.2 Items que PERMANECEN ABIERTOS

| # | TM | OBS/NOTE | Descripcion | Dias abierto | Estado TM N14 |
|---|-----|----------|-------------|-------------|---------------|
| 1 | N10 | OBS-05 | GA Antiscalant Tank — volumen efectivo, material body, anclaje sismico NCh 2369 | 32 | PARTIALLY ADDRESSED — P&ID Rev C corrige TK-09-002 a 0.34 m3. GA Rev B sigue pendiente. |
| 2 | N10 | NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | **69 dias** | OPEN — comprometido TM N4 (03-Feb-2026), no entregado |
| 3 | N11 | OBS-03 | Grounding Layout Rev B — posiciones equipos basadas en Piping Layout Rev A rechazado | 27 | OPEN — pendiente aceptacion Equipment Layout Rev B |
| 4 | N11 | OBS-04 | Instrument Location Layout Rev B — misma base que OBS-03 | 27 | OPEN — pendiente aceptacion Equipment Layout Rev B |
| 5 | N13 | NOTE-02 | Cable Tray Layout — ruteo cables interno desde LCP/MCC no entregado | 7 | OPEN — requerido para verificacion segregacion cables |

### 6.3 Items para IFC (no se cargan como observaciones activas)

| TM | OBS/NOTE | Descripcion | Status |
|-----|----------|-------------|--------|
| N12 | NOTE-02 | Line List SCH 80S notation | Para incorporar en IFC Rev 0 |
| N13 | NOTE-01 | P&ID CIP Tank TK-09-001 volumen 6.81 vs 6.1 m3 | Para confirmar/corregir en IFC Rev 0 |

---

## 7. Determinacion Veredicto Global

| Entrega | Documento | Veredicto |
|---------|-----------|-----------|
| E26 | Control System Architecture Rev D | **1 — Approved** |
| E27 | Valve List Rev D | **2 — Approved as Noted** |
| E27 | DS Pressure Gauge Rev B | **1 — Approved** |
| E28 | IO List Rev C | **2 — Approved as Noted** |
| E28 | Instrument List Rev C | **2 — Approved as Noted** |
| E28 | Data Transfer List Rev B | **2 — Approved as Noted** |
| E28 | DS Conductivity Analyzer Rev B | **1 — Approved** |
| E28 | DS pH/ORP Analyzer Rev B | **1 — Approved** |
| E28 | DS Temperature Transmitter Rev B | **1 — Approved** |
| E28 | DS Vibration Transmitter Rev B | **1 — Approved** |
| E29 | DS Flow Transmitter Rev B | **1 — Approved** |

**Resumen:** 7 documentos Code 1, 4 documentos Code 2.

Per CLAUDE.md §6.2: Al menos 1 con notas → **Code 2 — Approved as Noted**.

---

## 8. Notas Nuevas TM N14

| ID | Tipo | Documento | Severidad | Descripcion |
|----|------|-----------|-----------|-------------|
| NOTE-01 | E27 | Valve List Rev D | MINOR | Item 112 eliminado — confirmar decision de diseno vs oversight |
| NOTE-02 | E28 | IO List Rev C | MINOR | Discrepancia voltaje analyzers: REMARKS "220VAC" vs IL "24VDC" |
| NOTE-03 | E28 | Instrument List Rev C | MINOR | Rango calibrado VT: IL 0-127 mm/s vs DTL 0-25 mm/s |
| NOTE-04 | E28 | Instrument List Rev C | MINOR | Working medium "Filtered Water" en instrumentos brine-side |
| NOTE-05 | E28 | Data Transfer List Rev B | MINOR | Rango VT 0-25 mm/s en Modbus vs 0-127 mm/s en IL (cross-cutting con NOTE-03) |

---

## 9. Notas Internas (Van Doorn — NO ENVIAR)

### 9.1 Coherencia del Paquete E28

La entrega E28 demuestra un nivel de coherencia interna significativamente superior a entregas anteriores. Los 7 documentos se alinean entre si: TAGs consistentes entre IO List, IL, DTL; rangos de conductividad corregidos en los tres documentos simultaneamente; nomenclatura TE/TIT resuelta de forma coordinada. La madurez del paquete de instrumentacion se nota en el detalle de part numbers (Rosemount 214CRWSSA1S3E0120SL, Wilcoxon PCH420V-M12 con especificaciones completas).

### 9.2 Riesgo Residual: Alarm and Interlock Setpoints

BW Water diferio los setpoints de alarma de vibracion a un documento separado que no ha sido entregado ni tiene fecha comprometida en el schedule. Con el cambio de sensor VTV122 → PCH420V-M12 (tres bandas configurables), la definicion de setpoints se vuelve mas relevante porque ahora hay mas parametros por configurar. Se recomienda solicitar formalmente este documento en el proximo correo de seguimiento.

### 9.3 Discrepancia 220VAC — Implicacion para ADASA

Si los analyzers efectivamente requieren 220VAC (shelter heating, AC unit para panel externo, etc.), ADASA debe prever un circuito AC dedicado desde el tablero de distribucion hacia la zona de analyzers. Esto impacta el diseno del MCC ADASA y las canalizaciones electricas. La aclaracion de BW Water en respuesta a NOTE-02 deberia recibirse antes de avanzar con el diseno electrico de detalle de ADASA.

### 9.4 Working Medium como Riesgo QA

La etiqueta "Filtered Water" para instrumentos en servicio brine (NOTE-04) es un patron recurrente en la documentacion BW Water — probablemente heredado de un template generico de planta SWRO donde todos los instrumentos ven agua de mar pre-filtrada. En una planta UHPRO de segunda etapa, los medios de proceso divergen significativamente: el rechazo de primera etapa (~65 mS/cm), el rechazo de segunda etapa (~85-135 mS/cm) y el permeado (<1 mS/cm) requieren materiales distintos. Aunque BW Water ha seleccionado los materiales correctos (Hastelloy C, Tefzel), la etiqueta incorrecta del working medium dificulta la auditoria independiente de compatibilidad de materiales.

### 9.5 Progreso General del Proyecto

Con TM N14, el paquete de instrumentacion y control esta sustancialmente cerrado. Los 4 datasheets revisados en E28 (conductividad, pH/ORP, temperatura, vibracion) quedan todos en Code 1. Las tres listas maestras (IO List, IL, DTL) quedan en Code 2 con notas menores. El bottleneck del proyecto se desplaza hacia:
1. Layouts pendientes (Equipment Layout Rev B, Grounding, Instrument Location)
2. HMI Screenshots (69 dias sin entrega)
3. Alarm and Interlock Setpoints (sin fecha comprometida)

---

*Generado: 13-Apr-2026 | Revisado por: Luis Rivera | Para uso interno ADASA*
