# Revision Tecnica - Entrega 11 BW Water

**Submittal:** 25007-0011
**Fecha Emision:** 03-Feb-2026
**Fecha Revision:** 03-Feb-2026
**Revisor:** ADASA
**Version:** 2.0 (Revision rigurosa con cruce vs ET, Oferta Tecnica, transmittales previos y revision cruzada instrumentacion)

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0011 |
| Fecha Emision | 03-Feb-2026 |
| Documentos | 2 |
| Tipos | CD (Control Document), DWG (Drawing) |
| Submittal For | FA (For Approval) |
| Nota | Control Architecture Rev.B + Cable Tray Layout Rev.A |

---

## 2. Documentos Recibidos

| # | Codigo | Titulo | Rev | Paginas | Tipo |
|---|--------|--------|-----|---------|------|
| 1 | P22-CD-09-004-001 | Control System Architecture | B | 3 | Control Document |
| 2 | P22-DWG-09-007-004 | Cable Tray Layout and Support Details | A | 4 | Drawing |

**Documentos Adicionales:**
- P22-CD-09-004-001 CONTROL ARCHITECTURE REVB_CCS.pdf (Consolidated Comment Sheet)

---

## 3. Revision Documento 1: Control System Architecture (P22-CD-09-004-001-B)

### 3.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-CD-09-004-001-B |
| Titulo | Control System Architecture |
| Fecha | 29-Ene-2026 |
| Preparado | BT |
| Revisado | NHH |
| Aprobado | JFR |
| Revision | B (Segunda emision) |
| Drawing Status | Issued for Approval |

### 3.2 Historial de Revisiones

| Rev | Fecha | Descripcion |
|-----|-------|-------------|
| A | 05-Dic-2025 | Emision inicial (Entrega 4) |
| B | 29-Ene-2026 | Revision con respuesta a comentarios ADASA |

### 3.3 Contenido del Documento

El Control System Architecture Rev.B presenta:

**Sheet 1 (P22-CD-09-004-001-P1):** Cover Sheet

**Sheet 2 (P22-CD-09-004-001-P2):** 
- Diagrama de arquitectura de control
- Leyenda de cables (Control, Ethernet/IP, Power, CAT6, Fiber Optic)
- Tabla de responsabilidades de cableado (BW vs Others)
- BOM de sistema de control

### 3.4 Bill of Materials - Sistema de Control

| No. | Descripcion | Modelo | Fabricante | QTY |
|-----|-------------|--------|------------|-----|
| 1 | PLC CPU | 5069-L320ER | Allen Bradley | 1 |
| 2 | PLC Digital Input Module 16 x DI, 24VDC | 5069-IB16 | Allen Bradley | A/R |
| 3 | PLC Digital Output Module 16 x DO, 24VDC | 5069-OB16 | Allen Bradley | A/R |
| 4 | PLC Analog Input Module 8 x AI, 24VDC | 5069-IF8 | Allen Bradley | A/R |
| 5 | PLC Analog Output Module 4 x AO, 24VDC | 5069-OF4 | Allen Bradley | A/R |
| 6 | PanelView Plus 7 10" Color Touch Screen, 24VDC | 2711P-T10C21D8S | Allen Bradley | 1 |
| 7 | Stratix 2100 Unmanaged Ethernet Switch 8 Ports | 1783-USP8T | Allen Bradley | 1 |
| 8 | Ethernet/IP to Modbus TCP/IP Communications Gateway | PLX32-EIP-MBTCP | ProSoft | 1 |
| 9 | Studio 5000 Logix Designer V37 | - | Allen Bradley | 1 |
| 10 | FactoryTalk View Studio V15 | - | Allen Bradley | 1 |
| 11 | Dell 14" Latitude 3450 (W/ Win 11) | - | Dell | 1 |

### 3.5 Responsabilidades de Cableado

| Item | Descripcion | Responsable |
|------|-------------|-------------|
| 1 | CAT6/Ethernet/IP Cable within LCP Panel and to VFD/Field devices | BW |
| 2 | Power Cable between LCP Panel and Pump | BW |
| 3 | Control Cable between PLC and VFD within LCP Panel | BW |
| 4 | Control Cable between LCP Panel and Instruments/Junction Box/Valve/Heater | BW |
| 5 | Fiber Optic Cable between DCS and LCP Panel (Converter, Patch Panel, Cable tray, splicing) | Others |
| 6 | Ethernet cable from LCP panel to DCS | Others |
| 7 | Power cable between LCP Panel and Heater, Dosing Pump, A/C Unit & Lighting | BW |
| 8 | Incoming power cable 1 phase (220Vac) & 3 phase (380Vac) to LCP Panel | Others |

---

### 3.6 VERIFICACION RIGUROSA VS ESPECIFICACION TECNICA (ET P22-ET-09-000-001-0)

#### 3.6.1 Requisito: PLC Allen Bradley (ET Seccion 5.4)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4 - Especificacion de tableros de fuerza y control |
| **Lineas ET** | 1039 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Linea 1039):**
> "El control de los equipos se realizara mediante un PLC **(Allen Bradley)** que comandara toda la secuencia de funcionamiento automatico..."

**Evaluacion:**

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| Fabricante PLC | Allen Bradley | Allen Bradley 5069-L320ER | **SI** |
| Familia | No especificado | CompactLogix 5380 | **SI** |

**EVALUACION POSITIVA:** El PLC Allen Bradley 5069-L320ER (familia CompactLogix 5380) cumple con el requisito explicito de la ET.

#### 3.6.2 Requisito: HMI 10" Color Touch (ET Seccion 5.4)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4 - Especificacion de tableros de fuerza y control |
| **Lineas ET** | 1069 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Linea 1069):**
> "El sistema de control debera incorporar un HMI con **pantalla tactil de 10" color**."

**Evaluacion:**

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| HMI pantalla | 10" color touch | PanelView Plus 7 10" Color Touch 2711P-T10C21D8S | **SI** |

**EVALUACION POSITIVA:** El HMI PanelView Plus 7 de 10" cumple con el requisito de la ET.

#### 3.6.3 Requisito: Comunicacion Modbus TCP/IP (ET Seccion 5.4)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4 - Especificacion de tableros de fuerza y control |
| **Lineas ET** | 1075-1077 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Lineas 1075-1077):**
> "Tambien se debera considerar un sistema de comunicacion via Ethernet, con protocolo **Modbus TCP/IP**, que permita controlar y/o extraer datos en forma remota. Para la conexion se debe proveer un **Switch Ethernet industrial, no administrable, de al menos 5 bocas**."

**Evaluacion:**

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| Protocolo | Modbus TCP/IP | Gateway PLX32-EIP-MBTCP (EtherNet/IP to Modbus TCP) | **SI** |
| Switch Ethernet | Min 5 puertos, no administrable | Stratix 2100 1783-USP8T (8 ports, unmanaged) | **SI** |

**EVALUACION POSITIVA:** El gateway ProSoft PLX32-EIP-MBTCP convierte EtherNet/IP a Modbus TCP/IP cumpliendo el requisito. El switch Stratix 2100 de 8 puertos excede el requisito minimo de 5.

#### 3.6.4 Requisito: Software y Licenciamiento (ET Seccion 5.4)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4 - Especificacion de tableros de fuerza y control |
| **Lineas ET** | 1093-1103 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Lineas 1093-1096):**
> "Asimismo, debe entregarse, como parte del suministro, el respaldo de los softwares y programas de PLC y HMI y, los softwares y hardware necesarios para interactuar con ambos sistemas (PLC y HMI). En definitiva, **todo el licenciamiento perpetuo necesario** para poder interactuar con la logica de control programada."

**Evaluacion:**

| Requisito ET | Software Requerido | Valor Entregado | Cumple |
|--------------|-------------------|-----------------|--------|
| Software PLC | Licencia perpetua | Studio 5000 Logix Designer V37 | **SI** |
| Software HMI | Licencia perpetua | FactoryTalk View Studio V15 | **SI** |
| Hardware mantenimiento | Laptop/PC | Dell Latitude 3450 (Win 11) | **SI** |

**EVALUACION POSITIVA:** El BOM incluye las licencias de software requeridas y laptop de ingenieria.

#### 3.6.5 Requisito: UPS para Control (ET Seccion 5.4)

| Campo | Valor |
|-------|-------|
| **Seccion ET** | 5.4 - Especificacion de tableros de fuerza y control |
| **Lineas ET** | 1088-1089 |
| **Caracter** | **OBLIGATORIO** |

**Texto exacto ET (Lineas 1088-1089):**
> "Para el control debe suministrarse una **UPS con la capacidad suficiente para mantener el sistema de control activo por al menos 8 horas**."

**Evaluacion:**

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| UPS Control | 8 horas autonomia | **NO ESPECIFICADO EN BOM** | **NO** |

**OBSERVACION MAYOR OBS-01:** El BOM del Control System Architecture NO incluye la UPS requerida por ET 5.4 (L1088-1089). Se requiere incluir UPS con autonomia minima de 8 horas para el sistema de control.

---

### 3.7 VERIFICACION DE RESPUESTAS A COMENTARIOS TRANSMITTAL N2

El documento incluye Consolidated Comment Sheet (CCS) con respuestas a 3 comentarios levantados en Transmittal N2:

#### 3.7.1 Comentario 1: Modbus TCP Memory Map

| Campo | Valor |
|-------|-------|
| **Comentario ADASA** | "It must come programmed and deliver the Modbus TCP memory map." |
| **Respuesta BW Water** | "NOTED. WILL SUBMIT I/O MODBUS LIST SEPARATELY." |
| **Estado** | **PENDIENTE - NO ENTREGADO EN E11** |

**OBSERVACION CRITICA OBS-02:** BW Water comprometio entregar el I/O Modbus List separadamente. Han transcurrido **38 dias desde Transmittal N2** (26-Ene-2026) y el documento **NO ha sido entregado** en Submittal 0011. Este documento es critico para la integracion con el DCS de ADASA.

#### 3.7.2 Comentario 2: VFD Fieldbus para SCADA

| Campo | Valor |
|-------|-------|
| **Comentario ADASA** | "It should be a fieldbus to be able to retrieve electrical variables from both VFDs via SCADA." |
| **Respuesta BW Water** | "HAS REVISED IN CONTROL SYSTEM ARCHITECTURE - P22-CD-09-004-001 REVB" |
| **Estado** | **VERIFICAR EN DIAGRAMA** |

**Evaluacion:** El diagrama Rev.B muestra conexion CAT6/Ethernet/IP entre LCP Panel y VFDs. Sin embargo, **no se especifica explicitamente el protocolo de comunicacion VFD** (EtherNet/IP, Modbus RTU, etc.) ni las variables electricas disponibles.

**OBSERVACION MAYOR OBS-03:** Aunque BW Water indica que el diagrama fue revisado para incluir fieldbus a VFDs, se requiere confirmacion explicita de:
1. Protocolo de comunicacion VFD (EtherNet/IP, Modbus RTU, etc.)
2. Lista de variables electricas disponibles via SCADA (V, A, kW, Hz, temperatura motor)
3. Confirmacion de que ambos VFDs (HP Pump BH-09-001 y CIP Pump BH-09-002) estan conectados

#### 3.7.3 Comentario 3: Power Meter Clarification

| Campo | Valor |
|-------|-------|
| **Comentario ADASA** | "Include an electrical variable meter with fieldbus communication that records all the module's power consumption. Or is it the analyzer? Please clarify." |
| **Respuesta BW Water** | "LCP is come with a Digital Power Meter, Modbus TCP/IP protocol. This ANALYZER is for pH, ORP, Conductivity Analyzer with analog 4-20mA feedback." |
| **Estado** | **CERRADO** |

**Evaluacion:** La clarificacion es aceptable:
- **Digital Power Meter:** Incluido en LCP con Modbus TCP/IP para variables electricas
- **ANALYZER:** Se refiere a analizadores de proceso (pH, ORP, Conductividad) con 4-20mA

**COMENTARIO CERRADO** - Aclaracion satisfactoria.

---

### 3.8 VERIFICACION VS OFERTA TECNICA REV.1

**Fuente:** OFERTA-TECNICA-BWWATER-Rev1.md, Seccion 4 - Scope of Supply

| Componente | Oferta Rev.1 | Control Architecture Rev.B | Cumple |
|------------|-------------|---------------------------|--------|
| PLC | Allen Bradley | Allen Bradley 5069-L320ER | **SI** |
| HMI | 10" touch screen | PanelView Plus 7 10" | **SI** |
| Gateway Modbus | Incluido | PLX32-EIP-MBTCP | **SI** |
| Engineering Laptop | Incluido | Dell Latitude 3450 | **SI** |
| Software licencias | Perpetuas | Studio 5000 + FactoryTalk | **SI** |

**EVALUACION POSITIVA:** El Control System Architecture cumple con los compromisos de la Oferta Tecnica Rev.1.

---

### 3.9 Resumen de Observaciones Documento 1

| # | Observacion | Severidad | Referencia | Estado |
|---|-------------|-----------|------------|--------|
| **OBS-01** | **UPS no incluida en BOM.** ET 5.4 (L1088-1089) requiere UPS con 8 horas de autonomia para sistema de control. | **MAYOR** | ET 5.4 L1088-1089 | Nueva |
| **OBS-02** | **Modbus TCP Memory Map no entregado.** BW comprometio entrega separada hace 38 dias (TM N2). Documento critico para integracion DCS. | **CRITICA** | TM N2 OBS-08 | Arrastrada 38 dias |
| **OBS-03** | **VFD fieldbus no especificado explicitamente.** Falta confirmacion de protocolo, variables disponibles, y conexion de ambos VFDs. | **MAYOR** | TM N2 OBS-09 | Pendiente verificacion |

### 3.10 Veredicto Documento 1

| Aspecto | Veredicto |
|---------|-----------|
| Cumplimiento ET 5.4 | **PARCIAL** (falta UPS) |
| Cumplimiento Oferta | **CUMPLE** |
| Resolucion comentarios TM N2 | **PARCIAL** (1/3 cerrado, 2/3 pendientes) |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

**Justificacion:** El documento cumple con los requisitos principales de ET 5.4 (PLC Allen Bradley, HMI 10", Modbus TCP/IP, Switch Ethernet, Software). Sin embargo, requiere:
1. Inclusion de UPS en proxima revision del BOM
2. Entrega urgente del Modbus TCP Memory Map
3. Confirmacion explicita de configuracion VFD fieldbus

---

## 4. Revision Documento 2: Cable Tray Layout and Support Details (P22-DWG-09-007-004-A)

### 4.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-DWG-09-007-004-A |
| Titulo | Cable Tray Layout and Support Details |
| Fecha | 27-Ene-2026 |
| Preparado | BT |
| Revisado | NHH |
| Aprobado | JFR |
| Revision | A (Primera emision) |
| Drawing Status | Issued for Approval |

### 4.2 Contenido del Documento

El Cable Tray Layout presenta 4 hojas:

**Sheet 1 (P22-DWG-09-007-004-P1):** Plan View - Cable Tray Layout and Support Details
**Sheet 2 (P22-DWG-09-007-004-P2):** Instrument Location Schedule (32 instrumentos)
**Sheet 3 (P22-DWG-09-007-004-P3):** Installation Details (Transmitter/Analyzer mounting)

### 4.3 Notas Criticas del Documento

| # | Nota | Contenido |
|---|------|-----------|
| 1 | Elevacion | The elevation of the cable trays are subject for adjustment based on the actual condition at site |
| 2 | Material | **The cable trays shall be STEEL HOT DIP GALVANIZED** with a minimum width & height of 50mm(W) x 50mm(H) |
| 3 | Fill | The cable fill of cable trays **shall not exceed 80%** |

### 4.4 Cable Tray Schedule

| Tag | Elevacion | Dimensiones (W x H) | Tipo |
|-----|-----------|---------------------|------|
| EPCBT09001 | EL+2100 | W150 x H100 mm | Low Voltage |
| EPCCT09001 | EL+1850 | W150 x H100 mm | Discrete Signals |
| EPCBT09002 | EL+0300 | W150 x H100 mm | Low Voltage |
| EPCCT09002 | EL+0050 | W150 x H100 mm | Discrete Signals |
| EPCBT09003 | EL+2100 | W100 x H100 mm | Low Voltage |
| EPCCT09003 | EL+2100 | W100 x H100 mm | Discrete Signals |
| EPCBT09004 | EL+0500 | W100 x H100 mm | Low Voltage |
| EPCCT09004 | EL+0500 | W100 x H100 mm | Discrete Signals |

**Sistema de Codificacion:**
- EPC = Metal Tray (COND = Conduit)
- BT = Low Voltage, CT = Discrete Signals, MT = Medium Voltage, CD = Communications
- 09 = Area Osmosis Inversa Segunda Etapa
- XXX = Numero consecutivo

### 4.5 Power Panel Location Schedule

| No. | Tag | Descripcion |
|-----|-----|-------------|
| P1 | SAI-09-001 | LCP PLC & Instrumentation |
| P2 | SSAA-09-001B | Light (Outdoor) |
| P3 | BDS-09-001AC | Antiscalant Dos Pump Power Junction Box |
| P4 | BDS-09-001DC | Antiscalant Dos Pump Control Junction Box |
| P5 | REL-09-001 | CIP Heater Control Panel |
| P6 | UHPRO-09-001AC | UHPRO System Power Distribution Panel |
| P7 | UHPRO-09-001DC | UHPRO System Control Distribution Panel |
| P8 | SSAA-09-001A | Light (Indoor) |
| P9 | SSAA-09-002 | A/C Unit |
| S1 | - | Light (Indoor) Switch |

### 4.6 Instrument Location Schedule (32 Instrumentos)

| No. | Tag Number | System | Description | P&ID | Installation Location |
|-----|------------|--------|-------------|------|----------------------|
| 1 | DPS-09-001 | RO Cartridge Filter | Differential Pressure Switch | P22-DWG-09-02-P8 | Feed/Discharge Pipe |
| 2 | ORPIT-09-001 | RO Cartridge Filter | Discharge ORP Analyzer | P22-DWG-09-02-P8 | Discharge Pipe |
| 3 | CIT-09-001 | RO Cartridge Filter | Discharge Conductivity Analyzer | P22-DWG-09-02-P8 | Discharge Pipe |
| **4** | **FIT-09-001** | RO Cartridge Filter | **Discharge Flow Transmitter** | P22-DWG-09-02-P8 | **Discharge Pipe** |
| 5 | PIT-09-001 | RO HP Pump | Feed Pressure Transmitter | P22-DWG-09-02-P9 | Feed Pipe |
| 6 | PIT-09-002 | RO HP Pump | Discharge Pressure Transmitter | P22-DWG-09-02-P9 | Discharge Pipe |
| 7 | PI-09-001 | RO HP Pump | Discharge Pressure Gauge | P22-DWG-09-02-P9 | Discharge Pipe |
| 8 | PIT-09-003 | RO Stage 1 | Feed Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 9 | PIT-09-009 | RO Train | Combined Permeate Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 10 | PIT-09-004 | RO Stage 1 | Reject Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 11 | FIT-09-003 | RO Train | Permeate Flow Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 12 | CIT-09-002 | RO Train | Permeate Conductivity Analyzer | P22-DWG-09-02-P9 | RO Skid |
| **13** | **FIT-09-001** | RO 2nd Stage | **Permeate Flow Transmitter** | P22-DWG-09-02-P9 | **RO Skid** |
| 14 | PIT-09-007 | Interstage Turbo | to Feed Turbocharger Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 15 | PIT-09-005 | RO Stage 2 | Feed Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 16 | PIT-09-006 | RO Stage 2 | Reject Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 17 | CIT-09-004 | RO Stage 1 | Reject Conductivity Analyzer | P22-DWG-09-02-P9 | RO Skid |
| 18 | CIT-09-003 | RO Stage 2 | Permeate Conductivity Analyzer | P22-DWG-09-02-P9 | RO Skid |
| 19 | PI-09-002 | RO Train | Reject Pressure Gauge | P22-DWG-09-02-P9 | RO Skid |
| 20 | CIT-09-005 | RO Train | Reject Conductivity Analyzer | P22-DWG-09-02-P9 | RO Skid |
| 21 | FIT-09-004 | RO Train | Reject Flow Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 22 | PIT-09-008 | RO Train | Reject Pressure Transmitter | P22-DWG-09-02-P9 | RO Skid |
| 23 | TIT-09-001 | CIP Tank | Temperature Transmitter | P22-DWG-09-02-P10 | CIP Tank Side |
| 24 | LIT-09-001 | CIP Tank | Level Transmitter | P22-DWG-09-02-P10 | CIP Tank Side |
| 25 | PI-09-003 | CIP Pump | Discharge Pressure Gauge | P22-DWG-09-02-P10 | Discharge Pipe |
| 26 | PI-09-004 | CIP Cartridge Filter | Feed Pressure Gauge | P22-DWG-09-02-P10 | Feed Pipe |
| 27 | PI-09-005 | CIP Cartridge Filter | Discharge Pressure Gauge | P22-DWG-09-02-P10 | Discharge Pipe |
| 28 | PHIT-09-001 | RO CIP/Flush | pH Analyzer | P22-DWG-09-02-P10 | CIP/Flush Pipe |
| 29 | FIT-09-005 | CIP Pump | Discharge Flow Transmitter | P22-DWG-09-02-P10 | Discharge Pipe |
| 30 | LS-09-001 | Antiscalant Tank | Level Switch High | P22-DWG-09-02-P11 | Tank Side |
| 31 | LS-09-002 | Antiscalant Tank | Level Switch Low | P22-DWG-09-02-P11 | Tank Side |
| 32 | PI-09-006 | Antiscalant Dosing Pump | Discharge Pressure Gauge | P22-DWG-09-02-P11 | Discharge Pipe |

---

### 4.7 VERIFICACION RIGUROSA: TAG DUPLICADO FIT-09-001

| Campo | Valor |
|-------|-------|
| **Origen** | Transmittal N3, Instrument List OBS-02 |
| **Severidad** | **CRITICA** |
| **Dias Pendiente** | 6 dias (desde 28-Ene-2026) |

**Analisis:**

| Item | TAG | Sistema | Descripcion | Diametro | Rango |
|------|-----|---------|-------------|----------|-------|
| **4** | **FIT-09-001** | RO Cartridge Filter | Discharge Flow | DN100 | 0-100 m3/h |
| **13** | **FIT-09-001** | RO 2nd Stage | Permeate Flow | DN50 | 0-18 m3/h |

**OBSERVACION CRITICA OBS-04:** El Cable Tray Layout **HEREDA** el TAG duplicado FIT-09-001 del Instrument List (P22-LI-09-008-003-A). **Dos instrumentos completamente diferentes** (distinto diametro, distinto rango, distinta ubicacion) tienen el **mismo TAG**. Esto hace **IMPOSIBLE**:
1. Direccionamiento PLC unico
2. Cableado sin ambiguedad
3. Mantenimiento e identificacion en campo

**Accion Requerida:** Renumerar Item 13 como **FIT-09-002** para 2nd Stage Permeate Flow (consistente con IO List que ya usa FIT-09-002).

---

### 4.8 VERIFICACION VS INSTRUMENT LIST (P22-LI-09-008-003-A)

#### 4.8.1 Cruce Layout vs Instrument List

| Layout Item | Layout TAG | IL Line | IL TAG | Consistente |
|-------------|------------|---------|--------|-------------|
| 1 | DPS-09-001 | 1 | DPS-09-001 | **SI** |
| 2 | ORPIT-09-001 | 2 | ORPIT-09-001 | **SI** |
| 3 | CIT-09-001 | 3 | CIT-09-001 | **SI** |
| 4 | FIT-09-001 | 4 | FIT-09-001 | **SI** |
| 5 | PIT-09-001 | 5 | PIT-09-001 | **SI** |
| ... | ... | ... | ... | ... |
| **13** | **FIT-09-001** | **13** | **FIT-09-001** | **DUPLICADO** |
| ... | ... | ... | ... | ... |
| 24 | LIT-09-001 | 24 | LIT-09-001 | **SI** |

**Resultado:** El Layout es consistente con el Instrument List, **incluyendo el error del TAG duplicado**.

#### 4.8.2 Instrumentos Faltantes vs ET

**Referencia:** ET Seccion 5.5.7 (L1390-1394) - Transmisores de Vibracion

**Texto ET:**
> "Se debera incluir la instalacion de transmisores de vibracion en la bomba de alta presion (Item 5.1.1) y en las unidades del sistema de recuperacion de energia (ej. Turbos, Items 5.1.2 y 5.1.3)."

| Equipo | TAG Esperado | En Layout | En Instrument List | Estado |
|--------|--------------|-----------|-------------------|--------|
| HP Pump (BH-09-001) | VT-09-001 | **NO** | **NO** | **FALTANTE** |
| Feed Turbocharger (SIP-09-001) | VT-09-002 | **NO** | **NO** | **FALTANTE** |
| Interstage Turbocharger (SIP-09-002) | VT-09-003 | **NO** | **NO** | **FALTANTE** |

**OBSERVACION CRITICA OBS-05:** El Layout NO incluye ubicaciones para transmisores de vibracion requeridos por ET 5.5.7. Esta observacion fue levantada en **Transmittal N3 (28-Ene-2026)** y permanece **SIN RESOLVER**.

#### 4.8.3 Sensores Temperatura Motor vs ET

**Referencia:** ET Seccion 5.3 (L1032-1033) - Motores Electricos

**Texto ET:**
> "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos."

| Motor | Potencia | Pt-100 Devanados | Pt-100 Rodamientos | En Layout |
|-------|----------|------------------|-------------------|-----------|
| HP Pump (87 kW) | 87 kW | Requerido | Requerido | **NO** |
| CIP Pump (15 kW) | 15 kW | Requerido | Requerido | **NO** |

**OBSERVACION CRITICA OBS-06:** El Layout NO incluye ubicaciones para sensores Pt-100 de temperatura de motores requeridos por ET 5.3. Esta observacion fue levantada en **Transmittal N3 OBS-06/OBS-07** y permanece **SIN RESOLVER**.

---

### 4.9 VERIFICACION DE MATERIAL CABLE TRAY

| Requisito | Especificado | Evaluacion |
|-----------|--------------|------------|
| Material | Steel Hot Dip Galvanized | **ACEPTABLE** |
| Dimensiones minimas | 50mm x 50mm | **CUMPLE** (todas >= 100x100) |
| Fill maximo | 80% | **DECLARADO** |

**EVALUACION POSITIVA:** Las especificaciones de material y dimensiones de cable trays son aceptables.

---

### 4.10 NUEVA OBSERVACION CRITICA: Dimensiones Container Exceden 40ft Aprobado

#### OBS-08: Container Dimensions Exceed Approved 40ft Configuration (CRITICAL)

| Campo | Valor |
|-------|-------|
| **Documento** | P22-DWG-09-007-004-A - Cable Tray Layout |
| **Severidad** | **CRITICA** |
| **Referencia** | Correo 17-Nov-2025 "RE: Project TalTal-Quotation for additional 20ft container" |

**Descripcion:**
El Plan View del Cable Tray Layout muestra una configuracion de container que aparenta exceder las dimensiones del container estandar de 40ft aprobado. La distribucion de equipos (RO Skid con 9 vessels de membrana, HP Pump, Turbochargers, Sistema CIP, area Antiscalant) dentro de un unico container elongado sugiere configuracion de 60ft (40ft + 20ft).

**Antecedentes:**
El 17 de noviembre de 2025, ADASA rechazo formalmente la propuesta de BW Water para un container adicional de 20ft debido a:
- **Exceso presupuesto:** +USD $67,208
- **Extension de plazo:** +5 semanas (3 semanas ingenieria + 2 semanas manufactura)

ADASA confirmo continuar con el **container estandar de 40ft original** segun la oferta inicial de BW Water.

**Cita de Referencia (Luis Rivera, 17-Nov-2025):**
> "the budget increase (USD $67,208) and schedule extension (+3 weeks engineering, +2 weeks manufacturing) are too far from our available budget and original project timeline"

**Impacto:**
Si BW Water esta disenando para configuracion de 60ft a pesar del rechazo de ADASA:
1. Desviacion de alcance del contrato aprobado
2. Potencial reclamo de costos por cambio no aprobado
3. Impacto de cronograma no autorizado

**Accion Requerida:**
1. **URGENTE:** Confirmar dimensiones del container mostradas en Cable Tray Layout
2. Si el layout muestra configuracion de 60ft, **revisar inmediatamente a 40ft estandar**
3. Proveer confirmacion escrita de que el diseno cumple con el alcance aprobado

---

### 4.11 Tabla de Concordancia Completa: Cable Tray Layout vs Documentos Anteriores

| No. | TAG (Layout) | Sistema | En IL | En IO List | En Layout Anterior | Status |
|-----|--------------|---------|-------|------------|-------------------|--------|
| 1 | DPS-09-001 | RO Cartridge Filter | SI | SI | SI | OK |
| 2 | ORPIT-09-001 | RO Cartridge Filter | SI | SI | SI | OK |
| 3 | CIT-09-001 | RO Cartridge Filter | SI | SI | SI | OK |
| **4** | **FIT-09-001** | RO Cartridge Filter | SI | SI | SI | **DUPLICADO (vs Item 13)** |
| 5 | PIT-09-001 | RO HP Pump | SI | SI | SI | OK |
| 6 | PIT-09-002 | RO HP Pump | SI | SI | SI | OK |
| 7 | PI-09-001 | RO HP Pump | SI | SI | SI | OK |
| 8 | PIT-09-003 | RO Stage 1 | SI | SI | SI | OK |
| 9 | PIT-09-009 | RO Train | SI | SI | SI | OK |
| 10 | PIT-09-004 | RO Stage 1 | SI | SI | SI | OK |
| 11 | FIT-09-003 | RO Train | SI | SI | SI | OK |
| 12 | CIT-09-002 | RO Train | SI | SI | SI | OK |
| **13** | **FIT-09-001** | RO 2nd Stage | SI | **FIT-09-002** | SI | **DUPLICADO - Debe ser FIT-09-002** |
| 14 | PIT-09-007 | Interstage Turbo | SI | SI | SI | OK |
| 15 | PIT-09-005 | RO Stage 2 | SI | SI | SI | OK |
| 16 | PIT-09-006 | RO Stage 2 | SI | SI | SI | OK |
| 17 | CIT-09-004 | RO Stage 1 | SI | SI | SI | OK |
| 18 | CIT-09-003 | RO Stage 2 | SI | SI | SI | OK |
| 19 | PI-09-002 | RO Train | SI | SI | SI | OK |
| 20 | CIT-09-005 | RO Train | SI | SI | SI | OK |
| 21 | FIT-09-004 | RO Train | SI | SI | SI | OK |
| 22 | PIT-09-008 | RO Train | SI | SI | SI | OK |
| 23 | TIT-09-001 | CIP Tank | SI | SI | SI | OK |
| **24** | **LIT-09-001** | CIP Tank | SI | **LIT-09-002** | SI | **DISCREPANTE vs IO List** |
| 25 | PI-09-003 | CIP Pump | SI | SI | SI | OK |
| 26 | PI-09-004 | CIP Cartridge Filter | SI | SI | SI | OK |
| 27 | PI-09-005 | CIP Cartridge Filter | SI | SI | SI | OK |
| 28 | PHIT-09-001 | RO CIP/Flush | SI | SI | SI | OK |
| 29 | FIT-09-005 | CIP Pump | SI | SI | SI | OK |
| 30 | LS-09-001 | Antiscalant Tank | SI | SI | SI | OK |
| 31 | LS-09-002 | Antiscalant Tank | SI | SI | SI | OK |
| 32 | PI-09-006 | Antiscalant Pump | SI | SI | SI | OK |

**Leyenda:** IL = Instrument List, IO = IO List

**Resumen Concordancia:**
- Total instrumentos: 32
- Concordancia perfecta: 29 (91%)
- TAGs duplicados: 1 (FIT-09-001 en Items 4 y 13)
- TAGs discrepantes: 1 (LIT-09-001 vs LIT-09-002)

### 4.12 Instrumentos FALTANTES vs ET (Revision Cruzada)

| TAG Esperado | Equipo | Requisito ET | En Layout | Status |
|--------------|--------|--------------|-----------|--------|
| VT-09-001 | HP Pump (BH-09-001) | ET 5.5.7 L1390-1394 | **NO** | **FALTANTE** |
| VT-09-002 | Feed Turbocharger (SIP-09-001) | ET 5.5.7 L1390-1394 | **NO** | **FALTANTE** |
| VT-09-003 | Interstage Turbocharger (SIP-09-002) | ET 5.5.7 L1390-1394 | **NO** | **FALTANTE** |
| TE-09-003 to TE-09-007 | Motor HP Pump (Pt-100 devanados/rodamientos) | ET 5.3 L1032-1033 | **NO** | **FALTANTE** |
| TE-09-008 | Motor CIP Pump (Pt-100) | ET 5.3 L1032-1033 | **NO** | **FALTANTE** |
| CIT-09-006 | Interstage Turbo Conductivity | IO List Item 28 | **NO** | **FALTANTE** |

---

### 4.13 Resumen de Observaciones Documento 2

| # | Observacion | Severidad | Referencia | Estado |
|---|-------------|-----------|------------|--------|
| **OBS-04** | **TAG duplicado FIT-09-001** en Items 4 y 13. Dos instrumentos diferentes con mismo TAG. Imposible direccionamiento PLC. | **CRITICA** | TM N3 OBS-02 | Arrastrada 7 dias |
| **OBS-05** | **Faltan ubicaciones transmisores vibracion** (VT-09-001/002/003) para HP Pump y Turbochargers per ET 5.5.7 | **CRITICA** | TM N3 Grupo B | Arrastrada 7 dias |
| **OBS-06** | **Faltan ubicaciones Pt-100 motores** para HP Pump y CIP Pump per ET 5.3 | **CRITICA** | TM N3 Grupo C | Arrastrada 7 dias |
| OBS-07 | Discrepancia LIT TAG: Layout usa LIT-09-001, IO List usa LIT-09-002 | Mayor | TM N3 OBS-05 | Arrastrada 7 dias |
| **OBS-08** | **Container excede 40ft aprobado** - Layout muestra configuracion >40ft. Container 60ft rechazado 17-Nov-2025 (+USD $67K, +5 semanas) | **CRITICA** | Correo 17-Nov-2025 | **NUEVA** |

### 4.11 Veredicto Documento 2

| Aspecto | Veredicto |
|---------|-----------|
| Cumplimiento ET | **NO CUMPLE** (OBS-05, OBS-06) |
| Consistencia con Instrument List | **NO CUMPLE** (hereda TAG duplicado) |
| **VEREDICTO FINAL** | **3 - TO BE REVISED** |

**Justificacion:** El documento presenta **3 observaciones criticas**:
1. TAG duplicado FIT-09-001 heredado del Instrument List
2. Faltan ubicaciones para transmisores de vibracion requeridos por ET 5.5.7
3. Faltan ubicaciones para sensores Pt-100 de motores requeridos por ET 5.3

El documento **no puede ser aprobado** hasta que se corrija el Instrument List (FIT-09-001 -> FIT-09-002) y se incluyan los instrumentos faltantes.

---

## 5. Observaciones Pendientes de Transmittales Anteriores

### 5.1 Desde Transmittal N2 (26-Ene-2026) - 38 DIAS PENDIENTE

| # | Observacion | Documento | Status E11 |
|---|-------------|-----------|------------|
| OBS-08 | Modbus TCP Memory Map | Control Architecture | **NO ENTREGADO** |
| OBS-09 | VFD Fieldbus para SCADA | Control Architecture | **PARCIAL** - Diagrama muestra conexion pero sin especificacion explicita |
| OBS-10 | Power Meter Clarification | Control Architecture | **CERRADO** |

### 5.2 Desde Transmittal N3 (28-Ene-2026) - 6 DIAS PENDIENTE

| # | Observacion | Documento | Status E11 |
|---|-------------|-----------|------------|
| Grupo A | TAG duplicado FIT-09-001 | Instrument List | **NO CORREGIDO** - Heredado en Layout |
| Grupo B | Transmisores vibracion faltantes | Instrument List | **NO CORREGIDO** - No aparecen en Layout |
| Grupo C | Pt-100 motores faltantes | HP Pump Datasheet | **NO CORREGIDO** - No aparecen en Layout |
| Grupo D | VM-09-015 manual DN100 ANSI 900# | Valve List | **NO VERIFICABLE EN E11** |
| Grupo G | VFD electrical variables, DO/DI | IO List | **NO VERIFICABLE EN E11** |

---

## 6. Verificacion de Codificacion

| Documento | Codigo | Formato P22-TT-AA-DDD-NNN-R | Cumple |
|-----------|--------|-----------------------------|----- ---|
| Control Architecture | P22-CD-09-004-001-B | P22-CD-09-004-001-B | **SI** |
| Cable Tray Layout | P22-DWG-09-007-004-A | P22-DWG-09-007-004-A | **SI** |

**Todos los documentos cumplen** con el sistema de codificacion P00-IT-00-000-101.

---

## 7. Resumen Consolidado de Observaciones

### 7.1 Observaciones Criticas (Requieren correccion inmediata)

| # | Documento | Descripcion | Referencia | Estado |
|---|-----------|-------------|------------|--------|
| **OBS-02** | Control Architecture | **Modbus TCP Memory Map no entregado** - 38 dias pendiente desde TM N2 | TM N2 OBS-08 | **ARRASTRADA** |
| **OBS-04** | Cable Tray Layout | **TAG duplicado FIT-09-001** - Items 4 y 13 con mismo TAG, imposible PLC | TM N3 OBS-02 | **ARRASTRADA** |
| **OBS-05** | Cable Tray Layout | **Faltan transmisores vibracion** - ET 5.5.7 requiere VT para HP Pump y Turbos | ET 5.5.7, TM N3 | **ARRASTRADA** |
| **OBS-06** | Cable Tray Layout | **Faltan Pt-100 motores** - ET 5.3 requiere sensores temperatura devanados y rodamientos | ET 5.3, TM N3 | **ARRASTRADA** |

### 7.2 Observaciones Mayores (Requieren clarificacion)

| # | Documento | Descripcion | Referencia | Estado |
|---|-----------|-------------|------------|--------|
| **OBS-01** | Control Architecture | **UPS no incluida en BOM** - ET 5.4 requiere 8 horas autonomia | ET 5.4 L1088-1089 | **NUEVA** |
| **OBS-03** | Control Architecture | **VFD fieldbus no especificado explicitamente** - Falta protocolo y variables | TM N2 OBS-09 | **PARCIAL** |
| **OBS-07** | Cable Tray Layout | **Discrepancia LIT TAG** - Layout: LIT-09-001 vs IO List: LIT-09-002 | TM N3 | **ARRASTRADA** |

---

## 8. Acciones Requeridas BW Water

### 8.1 Acciones Criticas (Plazo: Inmediato)

| # | Accion | Documento | Prioridad | Referencia |
|---|--------|-----------|-----------|------------|
| 1 | **URGENTE: Entregar Modbus TCP Memory Map** - Documento pendiente 38 dias, critico para integracion DCS | Nuevo documento | **CRITICA** | OBS-02, TM N2 |
| 2 | **Corregir TAG duplicado FIT-09-001** en Instrument List. Renumerar Item 13 como FIT-09-002 y actualizar Layout | P22-LI-09-008-003 + P22-DWG-09-007-004 | **CRITICA** | OBS-04, TM N3 |
| 3 | **Incluir transmisores vibracion** en Instrument List y Layout para HP Pump (BH-09-001), Feed Turbo (SIP-09-001), Interstage Turbo (SIP-09-002) | P22-LI-09-008-003 + P22-DWG-09-007-004 | **CRITICA** | OBS-05, ET 5.5.7 |
| 4 | **Incluir sensores Pt-100 motores** en documentacion para HP Pump (87 kW) y CIP Pump (15 kW) - devanados y rodamientos | HP Pump DS + CIP Pump DS + Layout | **CRITICA** | OBS-06, ET 5.3 |

### 8.2 Acciones Mayores (Plazo: Proxima revision)

| # | Accion | Documento | Prioridad | Referencia |
|---|--------|-----------|-----------|------------|
| 5 | **Incluir UPS en BOM** del Control System Architecture con autonomia minima 8 horas | P22-CD-09-004-001 | **ALTA** | OBS-01, ET 5.4 |
| 6 | **Especificar VFD fieldbus explicitamente** - Protocolo, variables electricas disponibles, conexion ambos VFDs | P22-CD-09-004-001 | **ALTA** | OBS-03, TM N2 |
| 7 | **Unificar TAG LIT** - Decidir LIT-09-001 o LIT-09-002 para CIP Tank Level y actualizar todos los documentos | IL + IO List + Layout | **ALTA** | OBS-07, TM N3 |

---

## 9. Veredicto Final de la Entrega

### 9.1 Resumen por Documento

| # | Documento | Veredicto |
|---|-----------|-----------|
| 1 | P22-CD-09-004-001-B Control System Architecture | **2 - Approved as noted** |
| 2 | P22-DWG-09-007-004-A Cable Tray Layout | **3 - To be revised** |

### 9.2 Veredicto Consolidado

| Campo | Valor |
|-------|-------|
| **VEREDICTO ENTREGA 11** | **3 - TO BE REVISED** |
| Documentos Approved | 0 |
| Documentos Approved as Noted | 1 |
| Documentos To Be Revised | 1 |
| Documentos Rejected | 0 |

### 9.3 Justificacion del Veredicto

La Entrega 11 **requiere revision** debido a los siguientes hallazgos:

**Control System Architecture (P22-CD-09-004-001-B):**
- Aprobado con notas menores
- Cumple requisitos principales de ET 5.4 (PLC Allen Bradley, HMI 10", Modbus TCP/IP)
- Requiere inclusion de UPS y especificacion explicita de VFD fieldbus
- **PENDIENTE CRITICO:** Modbus TCP Memory Map no entregado (38 dias)

**Cable Tray Layout (P22-DWG-09-007-004-A):**
- **NO PUEDE SER APROBADO** en estado actual
- Hereda TAG duplicado FIT-09-001 del Instrument List
- Faltan ubicaciones para instrumentos requeridos por ET:
  - Transmisores de vibracion (ET 5.5.7)
  - Sensores Pt-100 de motores (ET 5.3)

**Aspectos Positivos:**
- Control Architecture cumple con especificaciones de PLC, HMI y comunicaciones
- Cable Tray Layout presenta especificaciones correctas de material y dimensiones
- Sistema de codificacion cumple con P00-IT-00-000-101

---

## 10. Documentos de Referencia

| Documento | Ubicacion |
|-----------|-----------|
| ET Modulo | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md |
| Oferta Tecnica Rev.1 | OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md |
| Instrument List | ENTREGAS_BWWATER/ENTREGA 8/md/P22-LI-09-008-003_Instrument List_A.md |
| IO List | ENTREGAS_BWWATER/ENTREGA 8/md/P22-LI-09-008-001 IO List.md |
| Transmittal N2 | REVISIONES/TRANSMITTALES/P22-TM-09-000-002-0/P22-TM-09-000-002-0_TRANSMITTAL.md |
| Transmittal N3 | REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/P22-TM-09-000-003-0_TRANSMITTAL.md |
| Control Architecture E11 | ENTREGAS_BWWATER/ENTREGA 11/md/P22-CD-09-004-001_CONTROL_ARCHITECTURE_REVB.md |
| Cable Tray Layout E11 | ENTREGAS_BWWATER/ENTREGA 11/md/P22-DWG-09-007-004_Cable_Tray_Layout.md |
| CCS Control Architecture | ENTREGAS_BWWATER/ENTREGA 11/md/P22-CD-09-004-001_CONTROL_ARCHITECTURE_CCS.md |

---

*Fin del documento*
*Revision preparada: 03-Feb-2026*
*Version 1.0 - Revision rigurosa con cruce completo vs ET, Oferta Tecnica y transmittales previos*
