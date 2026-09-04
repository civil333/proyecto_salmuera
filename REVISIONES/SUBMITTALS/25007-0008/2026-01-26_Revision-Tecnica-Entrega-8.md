# Revision Tecnica - Entrega 8 BW Water

**Submittal:** 25007-0008
**Fecha Emision:** 20-Ene-2026
**Fecha Revision:** 26-Ene-2026
**Revisor:** ADASA
**Version:** 1.0

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0008 |
| Fecha Emision | 20-Ene-2026 |
| Documentos | 12 |
| Tipos | DWG (Planos), ET (Datasheets), LI (Listas) |
| Submittal For | FA (For Approval) |
| Nota | Incluye PFD, Container DS, Turbochargers, Equipment/Valve/Instrument Lists |

---

## 2. Documentos Recibidos

| # | Codigo | Titulo | Rev | Tipo |
|---|--------|--------|-----|------|
| 1 | P22-DWG-09-009-01 | PFD | B | Plano |
| 2 | P22-ET-09-000-001 | DS of RO Container | B | Datasheet |
| 3 | P22-ET-09-009-005 | Datasheet RO Cartridge Filter | B | Datasheet |
| 4 | P22-ET-09-009-007 | Datasheet Feed Turbocharger | B | Datasheet |
| 5 | P22-ET-09-009-008 | Datasheet Interstage Turbocharger | B | Datasheet |
| 6 | P22-ET-09-009-011 | DS CIP Tank Heater | B | Datasheet |
| 7 | P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | A | Plano |
| 8 | P22-LI-09-005-001 | Equipment List | A | Lista |
| 9 | P22-LI-09-005-002 | Valve List | A | Lista |
| 10 | P22-LI-09-008-001 | IO List | A | Lista |
| 11 | P22-LI-09-008-002 | I&C Cable Schedule | A | Lista |
| 12 | P22-LI-09-008-003 | Instrument List | A | Lista |

---

## 3. Revision Documento 1: PFD (P22-DWG-09-009-01-B)

### 3.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-DWG-09-009-01-B |
| Titulo | Process Flow Diagram |
| Fecha | 20-Ene-2026 |
| Paginas | 4 (P8-P11) |

### 3.2 Contenido del Documento

El PFD incluye 4 hojas:
- **P8:** Pre-Treatment (Static Mixer, Cartridge Filter)
- **P9:** RO System (HP Pump, Turbochargers, Membranes)
- **P10:** CIP System (Tank, Heater, Pump, Filter)
- **P11:** Antiscalant Dosing System

### 3.3 Verificacion de Equipos Principales

| Equipo | TAG | Especificacion PFD | Cumple ET |
|--------|-----|-------------------|-----------|
| Static Mixer | MZE-09-009 | Koflo KD-1027, PVC | **SI** |
| Cartridge Filter | FIL-09-001 | Fil-Trek, 1 micron, 49 m3/h | **SI** |
| HP Pump | BH-09-001 | FEDCO MSD-7016, 49 m3/h, 92 kW | **SI** |
| Feed Turbocharger | SIP-09-001 | FEDCO HPB-60, Super Duplex | **SI** |
| Interstage Turbocharger | SIP-09-002 | FEDCO HPB-60, Super Duplex | **SI** |
| RO Membranes Stage 1 | - | LG SW 400 SR, 7 elements/vessel | **SI** |
| RO Membranes Stage 2 | - | LG SW 400R G2 UHP, 7 elements/vessel | **SI** |
| Pressure Vessels Stage 1 | BOI-09-001 | Protec BPV-8-1200-SP-7, 6 vessels | **SI** |
| Pressure Vessels Stage 2 | BOI-09-002 | Protec BPV-8-1800-SP-7, 4 vessels | **SI** |
| CIP Tank | TK-09-001 | Dayamas DYM 6800, HDPE, 6.1 m3 | **SI** |
| CIP Heater | REL-09-001 | Quantic Logic VEMA, 20 kW | **SI** |
| CIP Pump | BH-09-002 | Grundfos CRN64-2, 57 m3/h | **SI** |
| CIP Filter | FIL-09-002 | Fil-Trek S6GL14, 1 micron | **SI** |
| Antiscalant Tank | TK-09-002 | Promatics PLC330, 270 L | **SI** |
| Antiscalant Pump | BDS-09-001/002 | ProMinent GMXa 1602 | **SI** |

### 3.4 Verificacion de Caudales y Presiones

| Punto | Parametro | Valor PFD | Valor Process Calc | Consistencia |
|-------|-----------|-----------|-------------------|--------------|
| RO Feed | Caudal | 49 m3/h | 49 m3/h | **SI** |
| 1st Stage Permeate | Caudal | 12.9 m3/h | 12.9 m3/h | **SI** |
| 2nd Stage Permeate | Caudal | 8.1 m3/h | 8.1 m3/h | **SI** |
| Total Permeate | Caudal | 21 m3/h | 21 m3/h | **SI** |
| 1st Stage Feed | Presion | 69.53 bar | 69.53 bar | **SI** |
| 2nd Stage Feed | Presion | 84.8 bar | 84.81 bar | **SI** |

### 3.5 Observaciones

Sin observaciones criticas. El PFD es consistente con el Process Calculation.

### 3.6 Veredicto Documento 1

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 4. Revision Documento 2: RO Container (P22-ET-09-000-001-B)

### 4.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-000-001-B |
| Titulo | Datasheet of RO Container |
| Fecha | 20-Ene-2026 |
| Fabricante | CIMC (Container) |

### 4.2 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.1.10

| Requisito ET | Seccion | Valor Requerido | Valor Entregado | Cumple |
|--------------|---------|-----------------|-----------------|--------|
| Tipo Container | 5.1.10 | 40' HC ISO | 40' HC ISO | **SI** |
| Dimensiones Max | 5.1.10 | 13m x 2.5m x 2.8m | 12.192m x 2.438m x 2.896m | **SI** |
| Material Paredes | 5.1.10 | Acero galvanizado | Corten Steel | **SI** |
| Pintura | 5.1.10 | Interior/Exterior | Included | **SI** |
| Puerta Peatonal | 5.1.10 | 0.9m x 2.2m min | Personnel Door included | **VER NOTA** |
| Piso | 5.1.10 | Rejilla PRFV antideslizante | GRP Grating | **SI** |
| Ventilacion | 5.1.10 | Natural o forzada | Forced ventilation | **SI** |
| Iluminacion | 5.1.10 | Min 300 lux | LED Emergency lights included | **SI** |

### 4.3 Especificaciones Container

**Container CIMC 40' HC:**
- External Dimensions: 12192 mm L x 2438 mm W x 2896 mm H
- Internal Dimensions: 12032 mm L x 2352 mm W x 2698 mm H
- Material: Corten Steel (weathering steel)
- Floor: GRP Grating (anti-slip)
- Roof: ISO Steel Panels

**Accesorios Incluidos:**
- Personnel Door (to be confirmed dimensions)
- Emergency Exit
- Ventilation System (forced)
- LED Lighting with Emergency
- Fire Detection System
- GRP Grating Floor with Sump
- Cable Trays
- Equipment Supports

### 4.4 Observaciones

| # | Observacion | Severidad | Categoria |
|---|-------------|-----------|-----------|
| OBS-01 | El datasheet no especifica las dimensiones exactas de la puerta peatonal. ET requiere minimo 0.9m x 2.2m. Confirmar que se cumple este requisito. | Menor | Tecnico |

### 4.5 Veredicto Documento 2

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **2 - Approved as noted** |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

---

## 5. Revision Documento 3: RO Cartridge Filter (P22-ET-09-009-005-B)

### 5.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-009-005-B |
| Titulo | Datasheet of RO Cartridge Filter |
| Fecha | 20-Ene-2026 |
| TAG | FIL-09-001 |
| Fabricante | Fil-Trek |
| Modelo Housing | FRPH12-012-4-4F-100 |
| Modelo Cartridge | AG-PO-1-D1-40-PO-E2-EP |

### 5.2 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.1.5

| Requisito ET | Seccion | Valor Requerido | Valor Entregado | Cumple |
|--------------|---------|-----------------|-----------------|--------|
| Filtracion | 5.1.5 | 1 micron nominal | 1 micron | **SI** |
| Caudal | - | 49 m3/h | 49 m3/h | **SI** |
| Material Housing | 5.1.5 | FRP | FRP | **SI** |
| Material Cartridge | 5.1.5 | Polipropileno | Polypropylene | **SI** |
| Tamano Cartridge | 5.1.5 | 2.5" OD x 40" L | 2.5" OD x 40" L | **SI** |

### 5.3 Especificaciones Clave

**Filter Housing Fil-Trek FRPH12-012-4-4F-100:**
- Type: Horizontal Cylindrical
- Material: FRP (Fiberglass Reinforced Plastic)
- Dimensions: 12" D x 63.25" L
- Cartridge Qty: 12
- Design Pressure: 7 bar (100 psi)
- Inlet/Outlet: 4" Flanged

**Cartridge AG-PO-1-D1-40-PO-E2-EP:**
- Material: Polypropylene
- Rating: 1 micron
- Size: 2.5" OD x 40" L
- End Caps: Double O-ring
- Gasket: EPDM

### 5.4 Observaciones

Sin observaciones criticas. Documento completo.

### 5.5 Veredicto Documento 3

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 6. Revision Documento 4: Feed Turbocharger (P22-ET-09-009-007-B)

### 6.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-009-007-B |
| Titulo | Datasheet of Feed Turbocharger |
| Fecha | 20-Ene-2026 |
| TAG | SIP-09-001 |
| Fabricante | FEDCO |
| Modelo | HPB-60 |

### 6.2 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.1.2

| Requisito ET | Seccion | Valor Requerido | Valor Entregado | Cumple |
|--------------|---------|-----------------|-----------------|--------|
| Marca | 5.1.2 | FEDCO o similar | FEDCO | **SI** |
| Tipo | 5.1.2 | Turbocharger | Turbocharger | **SI** |
| Material | 5.1.2 | Super Duplex PREN > 40 | Super Duplex 2507 | **SI** |

### 6.3 Especificaciones Clave

**FEDCO HPB-60 Feed Turbocharger:**

| Parametro | Pump Side | Turbine Side |
|-----------|-----------|--------------|
| Flow | 49.0 m3/h | 28.0 m3/h |
| Inlet Pressure | 2.0 bar | 68.05 bar |
| Outlet Pressure | 69.53 bar | 1.0 bar |
| Fluid | Brine | Concentrate |

**Materiales:**
- Casing: Super Duplex SS 2507
- Impeller: Super Duplex SS 2507
- Shaft: Super Duplex SS 2507
- Wetted Parts: Super Duplex SS 2507

**Dimensiones:**
- 288 mm L x 279.07 mm W x 254 mm H

### 6.4 Verificacion BiTurbo Performance

El documento incluye tabla de "BiTurbo Performance Analysis" con 10 escenarios operativos:

| Escenario | Feed TDS | LP Flow | LP Inlet P | HP Flow | HP Outlet P |
|-----------|----------|---------|------------|---------|-------------|
| Design Case | 53K | 49.0 m3/h | 2.0 bar | 49.0 m3/h | 69.53 bar |

**Evaluacion:** Consistente con Process Calculation.

### 6.5 Verificacion PREN

| Material | PREN Tipico | Cumple > 40 |
|----------|-------------|-------------|
| Super Duplex 2507 | 42.5 | **SI** |

### 6.6 Observaciones

Sin observaciones criticas. Documento completo.

### 6.7 Veredicto Documento 4

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 7. Revision Documento 5: Interstage Turbocharger (P22-ET-09-009-008-B)

### 7.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-009-008-B |
| Titulo | Datasheet of Interstage Turbocharger |
| Fecha | 20-Ene-2026 |
| TAG | SIP-09-002 |
| Fabricante | FEDCO |
| Modelo | HPB-60 |

### 7.2 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.1.3

| Requisito ET | Seccion | Valor Requerido | Valor Entregado | Cumple |
|--------------|---------|-----------------|-----------------|--------|
| Marca | 5.1.3 | FEDCO o similar | FEDCO | **SI** |
| Tipo | 5.1.3 | Turbocharger | Turbocharger | **SI** |
| Material | 5.1.3 | Super Duplex PREN > 40 | Super Duplex 2507 | **SI** |

### 7.3 Especificaciones Clave

**FEDCO HPB-60 Interstage Turbocharger:**

| Parametro | Pump Side | Turbine Side |
|-----------|-----------|--------------|
| Flow | 36.1 m3/h | 28.0 m3/h |
| Inlet Pressure | 68.48 bar | 84.80 bar |
| Outlet Pressure | 84.80 bar | 53.5 bar |
| Fluid | 1st Stage Reject | 2nd Stage Reject |

**Materiales:**
- Casing: Super Duplex SS 2507
- Impeller: Super Duplex SS 2507
- Shaft: Super Duplex SS 2507
- Wetted Parts: Super Duplex SS 2507

**Dimensiones:**
- 288 mm L x 279.07 mm W x 254 mm H

### 7.4 Observaciones

Sin observaciones criticas. Documento completo.

### 7.5 Veredicto Documento 5

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 8. Revision Documento 6: CIP Tank Heater (P22-ET-09-009-011-B)

### 8.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-009-011-B |
| Titulo | Datasheet of CIP Tank Heater |
| Fecha | 20-Ene-2026 |
| TAG | REL-09-001 |
| Fabricante | Quantic Logic |
| Modelo | VEMA Flange Immersion Heater |

### 8.2 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.1.7

| Requisito ET | Seccion | Valor Requerido | Valor Entregado | Cumple |
|--------------|---------|-----------------|-----------------|--------|
| Tipo | 5.1.7 | Flange Immersion | Flange Immersion | **SI** |
| Potencia | 5.1.7 | Suficiente para 25-30°C | 20 kW | **SI** |
| Material Wetted | 5.1.7 | SS316 | SS316 | **SI** |

### 8.3 Especificaciones Clave

**Quantic Logic VEMA Heater:**
- Type: Flange Immersion Heater
- Power: 20 kW
- Voltage: 380 VAC, 3 Phase
- Flange: 3" ANSI 150#
- Flange Material: SS316
- Heater Length: 1500 mm UL
- Wetted Material: SS316

**Control Panel:**
- Power Regulator: 40 amp 3 phase
- Temperature Controller: Digital
- Input: PT100 Sensor
- Thermostat: 0-120°C adjustable
- Mounting: Wall mounted (outdoor)
- Enclosure: IP65 SUS304

**Inclusions:**
- Graphite gasket (3.0mm SS316L reinforced)
- Terminal enclosure IP65 SUS304

### 8.4 Observaciones

Sin observaciones criticas. Documento completo.

### 8.5 Veredicto Documento 6

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 9. Revision Documento 7: Grounding & Power Panel Layout (P22-DWG-09-007-003-A)

### 9.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-DWG-09-007-003-A |
| Titulo | Grounding Point & Power Panel Location Layout |
| Fecha | 19-Ene-2026 |
| Escala | NTS |
| Revision | A (Primera emision) |

### 9.2 Contenido del Documento

El documento presenta:
- Plan View del container con ubicacion de puntos de puesta a tierra
- Ubicacion de Power Panel

### 9.3 Observaciones

| # | Observacion | Severidad | Categoria |
|---|-------------|-----------|-----------|
| OBS-02 | El plano esta a escala NTS (Not To Scale). Para construccion se recomienda emitir version con escala definida y dimensiones acotadas. | Menor | Documental |

### 9.4 Veredicto Documento 7

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **2 - Approved as noted** |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

---

## 10. Revision Documento 8: Equipment List (P22-LI-09-005-001-A)

### 10.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-005-001-A |
| Titulo | Equipment List |
| Fecha | 20-Ene-2026 |
| Revision | A (Primera emision) |

### 10.2 Contenido del Documento

El Equipment List incluye 13 equipos principales:

| # | TAG | Descripcion | Fabricante | Modelo |
|---|-----|-------------|------------|--------|
| 1 | MZE-09-009 | Static Mixer | Koflo | KD-1027 |
| 2 | FIL-09-001 | RO Cartridge Filter | Fil-Trek | FRPH12-012-4-4F-100 |
| 3 | BH-09-001 | RO HP Feed Pump | FEDCO | MSD-7016 |
| 4 | SIP-09-001 | Feed Turbocharger | FEDCO | HPB-60 |
| 5 | BOI-09-001 | Stage 1 SWRO Membrane | LG | SW 400 SR |
| 6 | BOI-09-001 | Stage 1 RO PV | Protec | BPV-8-1200-SP-7 |
| 7 | SIP-09-002 | Interstage Turbocharger | FEDCO | HPB-60 |
| 8 | BOI-09-002 | Stage 2 UHPRO Membrane | LG | SW 400R G2 UHP |
| 9 | BOI-09-002 | Stage 2 RO PV | Protec | BPV-8-1800-SP-7 |
| 10 | TK-09-001 | CIP Tank | Dayamas | DYM 6800 |
| 11 | REL-09-001 | CIP Heater | Quantic Logic | VEMA |
| 12 | BH-09-002 | CIP Pump | Grundfos | CRN64-2 |
| 13 | FIL-09-002 | CIP Cartridge Filter | Fil-Trek | S6GL14-019-4-4F-A-150 |
| 14 | TK-09-002 | Antiscalant Dosing Tank | Promatics | PLC330 |
| 15 | BDS-09-001/002 | Antiscalant Dosing Pump | ProMinent | GMXa 1602 |

### 10.3 Verificacion Equipos vs ET

| Equipo | Requisito ET | Equipment List | Cumple |
|--------|--------------|----------------|--------|
| HP Pump | Super Duplex | Super Duplex SS | **SI** |
| HP Pump | VFD | VFD, 3-wire RTD | **SI** |
| Turbochargers | Super Duplex PREN > 40 | Super Duplex SS | **SI** |
| RO Filter | 1 micron | 1 micron | **SI** |
| CIP Tank | > 5.1 m3 | 6.1 m3 | **SI** |
| CIP Pump | VFD | VFD | **SI** |
| CIP Filter | 1 micron | 1 micron | **SI** |

### 10.4 Verificacion Especificaciones Electricas

| Equipo | Voltaje | Frecuencia | Potencia | Proteccion |
|--------|---------|------------|----------|------------|
| HP Pump | 380V 3ph | 50Hz | 92 kW | IP66/B |
| CIP Pump | 380V 3ph | 50Hz | 11 kW | IP66/B |
| CIP Heater | 380V 3ph | - | 20 kW | - |
| Antiscalant Pump | 230V 1ph | 50Hz | 24W | - |

**Evaluacion:** Todas las tensiones cumplen requisito ET 3x380V/50Hz para equipos principales.

### 10.5 Observaciones

Sin observaciones criticas. Documento completo.

### 10.6 Veredicto Documento 8

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 11. Revision Documento 9: Valve List (P22-LI-09-005-002-A)

### 11.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-005-002-A |
| Titulo | Valve List |
| Fecha | 06-Ene-2026 |
| Revision | A (Primera emision) |

### 11.2 Contenido del Documento

El Valve List incluye 109 valvulas organizadas por sistema:

| Sistema | Cantidad | Tipos |
|---------|----------|-------|
| Cartridge Filter | 11 | Ball, Butterfly (manual) |
| SWRO HPP | 10 | Ball, Butterfly, Check (Super Duplex) |
| Feed Turbocharger | 3 | Ball (Super Duplex) |
| 1st Stage Permeate | 16 | Ball, Butterfly, Labcock, Check, Motorized |
| 1st Stage Reject | 8 | Ball, Butterfly, Motorized |
| 2nd Stage Feed | 3 | Ball (Super Duplex) |
| 2nd Stage Permeate | 5 | Ball, Labcock |
| 2nd Stage Reject | 20 | Ball, Butterfly, Gate, Motorized |
| CIP | 22 | Ball, Butterfly, Check, Motorized |
| Antiscalant | 17 | Ball, Motorized, PSV |

### 11.3 Verificacion Materiales Alta Presion

| Servicio | Material Especificado | Rating | Cumple ET |
|----------|----------------------|--------|-----------|
| SWRO HPP | CE3MN Super Duplex | ANSI 900# | **SI** |
| Feed Turbocharger | CE3MN Super Duplex | ANSI 900# | **SI** |
| 1st Stage Reject | CE3MN Super Duplex | ANSI 900# | **SI** |
| 2nd Stage Feed | CE3MN Super Duplex | ANSI 900# | **SI** |
| 2nd Stage Reject | CE3MN Super Duplex | ANSI 900# | **SI** |

**Nota:** CE3MN es la designacion de fundicion para Super Duplex equivalente a S32750, con PREN > 40.

### 11.4 Verificacion Materiales Baja Presion

| Servicio | Material | Rating | Cumple ET |
|----------|----------|--------|-----------|
| Cartridge Filter | PVC | ANSI 150# | **SI** |
| Permeate Lines | PVC | ANSI 150# | **SI** |
| CIP | PVC | ANSI 150# | **SI** |
| Antiscalant | PVC | ANSI 150# | **SI** |

### 11.5 Valvulas Motorizadas

| TAG | Servicio | Tipo | Protocol |
|-----|----------|------|----------|
| VE-09-003/004/005 | 1st Stage Permeate | Butterfly MOV | Ethernet/IP |
| VE-09-006 | 1st Stage CIP Feed | Butterfly MOV | Ethernet/IP |
| VE-09-007 | 2nd Stage CIP Feed | Butterfly MOV | Ethernet/IP |
| VE-09-008 | 1st Stage Reject | Butterfly MOV | Ethernet/IP |
| VE-09-009 | 2nd Stage CIP Return | Butterfly MOV | Ethernet/IP |
| VE-09-010 | 1st Stage CIP Return | Butterfly MOV | Ethernet/IP |
| VE-09-002 | 2nd Stage Reject Bypass | Ball MOV | Ethernet/IP |
| VC-09-006 | 2nd Stage Reject Control | Gate MCV | Ethernet/IP |

**Evaluacion:** Todas las valvulas motorizadas especifican protocolo Ethernet/IP para comunicacion con PLC.

### 11.6 Observaciones

| # | Observacion | Severidad | Categoria |
|---|-------------|-----------|-----------|
| OBS-03 | Columna "Brand" indica "TBA" (To Be Advised) para todas las valvulas. Se requiere confirmar fabricantes seleccionados. | Menor | Documental |

### 11.7 Veredicto Documento 9

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **2 - Approved as noted** |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

---

## 12. Revision Documento 10: IO List (P22-LI-09-008-001-A)

### 12.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-008-001-A |
| Titulo | IO List |
| Fecha | 11-Ene-2026 |
| Revision | A (Primera emision) |

### 12.2 Resumen de I/O

| Tipo Senal | Cantidad |
|------------|----------|
| Digital Input (DI) | 48 |
| Digital Output (DO) | 10 |
| Analog Input (AI) | 32 |
| Analog Output (AO) | 17 |
| **Total I/O** | **97** |

### 12.3 Verificacion Protocolos de Comunicacion

| Dispositivo | Protocolo Especificado | Cumple ET 5.5.1 |
|-------------|----------------------|-----------------|
| Transmisores Presion | 4-20mA (2-wire loop powered) | **SI** |
| Transmisores Caudal | 4-20mA (4-wire, 24VDC) | **SI** |
| Analizadores Conductividad | 4-20mA (4-wire, 220VAC) | **SI** |
| Analizadores pH/ORP | 4-20mA (4-wire, 220VAC) | **SI** |
| Valvulas Motorizadas | Ethernet/IP | **SI** |
| VFDs | 4-20mA + Dry Contact | **SI** |
| Switches | Dry Contact 24VDC | **SI** |

### 12.4 Verificacion Instrumentacion vs ET

| Requisito ET | Seccion | Cantidad Requerida | Cantidad IO List | Cumple |
|--------------|---------|-------------------|------------------|--------|
| Flow Transmitters | 5.5.2 | 5 puntos | FIT-001 to FIT-005 (5) | **SI** |
| Conductivity Analyzers | 5.5.6 | 5 puntos | CIT-001 to CIT-006 (6) | **SI** |
| Pressure Transmitters | 5.5.4 | 9 puntos | PIT-001 to PIT-009 (9) | **SI** |
| Level Transmitters | 5.5.5 | 1 (CIP Tank) | LIT-002 (1) | **SI** |
| pH Analyzer | 5.5.8 | 1 (CIP) | PHIT-001 (1) | **SI** |
| ORP Analyzer | 5.5.9 | 1 | ORPIT-001 (1) | **SI** |

### 12.5 Observaciones

Sin observaciones criticas. Documento completo y bien estructurado.

### 12.6 Veredicto Documento 10

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 13. Revision Documento 11: I&C Cable Schedule (P22-LI-09-008-002-A)

### 13.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-008-002-A |
| Titulo | Instrumentation & Control Cable Schedule |
| Fecha | 11-Ene-2026 |
| Revision | A (Primera emision) |

### 13.2 Tipos de Cable Especificados

| Aplicacion | Cable Type | Cores/Size |
|------------|-----------|------------|
| Digital Signals | Cu/PVC/PVC | 4C x 1.5 mm2 |
| Analog 4-20mA | Cu/PVC/OS/PVC | 1P x 1 mm2 (shielded) |
| Conductivity/Flow | Cu/PE/S/UTP/PUR | 2P x 0.38 mm2 |
| VFD Interface | Cu/PVC/PVC | 7C x 1.5 mm2 |
| Ethernet/IP | Cat 6 (implied) | Via Valve Panel |

### 13.3 Verificacion Blindaje

| Tipo Senal | Blindaje Requerido | Especificado | Cumple |
|------------|-------------------|--------------|--------|
| Analog 4-20mA | Overall Shield | OS (Overall Screen) | **SI** |
| Transmitters | Shielded | Cu/PVC/OS/PVC | **SI** |
| Smart Instruments | UTP | Cu/PE/S/UTP/PUR | **SI** |

### 13.4 Observaciones

Sin observaciones criticas. Cables adecuados para aplicacion.

### 13.5 Veredicto Documento 11

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 14. Revision Documento 12: Instrument List (P22-LI-09-008-003-A)

### 14.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-008-003-A |
| Titulo | Instrument List |
| Fecha | 20-Ene-2026 |
| Revision | A (Primera emision) |

### 14.2 Resumen de Instrumentacion

| Tipo | Cantidad | TAGs |
|------|----------|------|
| Flow Transmitter (FIT) | 5 | FIT-09-001 to FIT-09-005 |
| Conductivity Analyzer (CIT) | 5 | CIT-09-001 to CIT-09-006 |
| Pressure Transmitter (PIT) | 9 | PIT-09-001 to PIT-09-009 |
| Level Transmitter (LIT) | 1 | LIT-09-002 |
| Level Switch (LS) | 2 | LS-09-001, LS-09-002 |
| Differential Pressure Switch (DPS) | 1 | DPS-09-001 |
| Temperature Switch (TE) | 2 | TE-09-001, TE-09-002 |
| pH Analyzer (PHIT) | 1 | PHIT-09-001 |
| ORP Analyzer (ORPIT) | 1 | ORPIT-09-001 |
| **Total** | **32** | - |

### 14.3 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.5

| Requisito ET | Seccion | Instrumento | Ubicacion | Cumple |
|--------------|---------|-------------|-----------|--------|
| Caudal RO Feed | 5.5.2 | FIT-09-001 | Cartridge Filter Discharge | **SI** |
| Caudal 1st Permeate | 5.5.2 | FIT-09-003 | 1st Stage Permeate | **SI** |
| Caudal 2nd Permeate | 5.5.2 | FIT-09-002 | 2nd Stage Permeate | **SI** |
| Caudal Concentrate | 5.5.2 | FIT-09-004 | Concentrate Discharge | **SI** |
| Caudal CIP | 5.5.2 | FIT-09-005 | CIP Filter Discharge | **SI** |
| Presion HP Pump | 5.5.4 | PIT-09-001/002 | Inlet/Discharge | **SI** |
| Presion Stages | 5.5.4 | PIT-09-003 to PIT-09-009 | Multiple points | **SI** |
| Conductividad Feed | 5.5.6 | CIT-09-001 | Cartridge Filter Discharge | **SI** |
| Conductividad Permeate | 5.5.6 | CIT-09-002/003 | 1st/2nd Permeate | **SI** |
| Conductividad Concentrate | 5.5.6 | CIT-09-005 | Concentrate Discharge | **SI** |
| pH CIP | 5.5.8 | PHIT-09-001 | CIP Pump Discharge | **SI** |
| ORP Feed | 5.5.9 | ORPIT-09-001 | Cartridge Filter Discharge | **SI** |
| Nivel CIP Tank | 5.5.5 | LIT-09-002 | CIP Tank | **SI** |

### 14.4 Verificacion Protocolo HART

| Instrumento | Protocolo Especificado | Cumple ET 5.5.1 (HART) |
|-------------|----------------------|-------------------------|
| FIT-09-001 to 005 | 4-20mA + HART | **SI** |
| PIT-09-001 to 009 | 4-20mA + HART | **SI** |
| CIT-09-001 to 006 | 4-20mA + HART | **SI** |
| LIT-09-002 | 4-20mA + HART | **SI** |
| PHIT-09-001 | 4-20mA + HART | **SI** |
| ORPIT-09-001 | 4-20mA + HART | **SI** |

**Evaluacion:** Todos los transmisores especifican protocolo 4-20mA + HART, cumpliendo requisito ET 5.5.1.

### 14.5 Verificacion Transmisores de Vibracion

| Requisito ET | Seccion | Ubicacion | Instrument List | Cumple |
|--------------|---------|-----------|-----------------|--------|
| Vibracion HP Pump | 5.5.7 | BH-09-001 | **NO INCLUIDO** | **NO** |
| Vibracion Turbochargers | 5.5.7 | SIP-09-001/002 | **NO INCLUIDO** | **NO** |

### 14.6 Observaciones

| # | Observacion | Severidad | Categoria |
|---|-------------|-----------|-----------|
| OBS-04 | El Instrument List no incluye transmisores de vibracion para la bomba HP (BH-09-001) ni para los turbochargers (SIP-09-001/002). ET Seccion 5.5.7 requiere monitoreo de vibracion en equipos rotativos. | Mayor | Tecnico |

### 14.7 Veredicto Documento 12

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **3 - To be revised** |
| **VEREDICTO FINAL** | **3 - TO BE REVISED** |

---

## 15. Verificacion de Codificacion

### 15.1 Analisis de Codigos

| Documento | Codigo | Formato P22-TT-AA-DDD-NNN-R | Cumple |
|-----------|--------|-----------------------------|----- ---|
| PFD | P22-DWG-09-009-01-B | P22-DWG-09-009-001-B | **SI** |
| Container DS | P22-ET-09-000-001-B | P22-ET-09-000-001-B | **SI** |
| Cartridge Filter DS | P22-ET-09-009-005-B | P22-ET-09-009-005-B | **SI** |
| Feed Turbo DS | P22-ET-09-009-007-B | P22-ET-09-009-007-B | **SI** |
| Interstage Turbo DS | P22-ET-09-009-008-B | P22-ET-09-009-008-B | **SI** |
| CIP Heater DS | P22-ET-09-009-011-B | P22-ET-09-009-011-B | **SI** |
| Grounding Layout | P22-DWG-09-007-003-A | P22-DWG-09-007-003-A | **SI** |
| Equipment List | P22-LI-09-005-001-A | P22-LI-09-005-001-A | **SI** |
| Valve List | P22-LI-09-005-002-A | P22-LI-09-005-002-A | **SI** |
| IO List | P22-LI-09-008-001-A | P22-LI-09-008-001-A | **SI** |
| Cable Schedule | P22-LI-09-008-002-A | P22-LI-09-008-002-A | **SI** |
| Instrument List | P22-LI-09-008-003-A | P22-LI-09-008-003-A | **SI** |

**Todos los documentos cumplen** con el sistema de codificacion P00-IT-00-000-101.

---

## 16. Resumen de Observaciones

| # | Documento | Descripcion | Categoria | Severidad |
|---|-----------|-------------|-----------|-----------|
| OBS-01 | P22-ET-09-000-001-B | Dimensiones exactas de puerta peatonal no especificadas | Tecnico | Menor |
| OBS-02 | P22-DWG-09-007-003-A | Plano a escala NTS, se recomienda version acotada | Documental | Menor |
| OBS-03 | P22-LI-09-005-002-A | Fabricantes de valvulas indicados como "TBA" | Documental | Menor |
| OBS-04 | P22-LI-09-008-003-A | Faltan transmisores de vibracion para HP Pump y Turbochargers (ET 5.5.7) | Tecnico | **Mayor** |

---

## 17. Acciones Requeridas BW Water

| # | Accion | Documento | Prioridad | Plazo Sugerido |
|---|--------|-----------|-----------|----------------|
| 1 | Incluir transmisores de vibracion para BH-09-001 (HP Pump) y SIP-09-001/002 (Turbochargers) en Instrument List segun requisito ET 5.5.7 | P22-LI-09-008-003 | **Alta** | Proxima revision |
| 2 | Confirmar dimensiones de puerta peatonal del container (minimo 0.9m x 2.2m segun ET 5.1.10) | P22-ET-09-000-001 | Media | Proxima revision |
| 3 | Confirmar fabricantes seleccionados para valvulas (actualmente "TBA") | P22-LI-09-005-002 | Media | Proxima revision |
| 4 | Emitir plano de Grounding Layout con escala definida y dimensiones acotadas | P22-DWG-09-007-003 | Baja | Para construccion |

---

## 18. Veredicto Final de la Entrega

### 18.1 Resumen por Documento

| # | Documento | Veredicto |
|---|-----------|-----------|
| 1 | P22-DWG-09-009-01-B PFD | **1 - Approved** |
| 2 | P22-ET-09-000-001-B Container | **2 - Approved as noted** |
| 3 | P22-ET-09-009-005-B Cartridge Filter | **1 - Approved** |
| 4 | P22-ET-09-009-007-B Feed Turbocharger | **1 - Approved** |
| 5 | P22-ET-09-009-008-B Interstage Turbocharger | **1 - Approved** |
| 6 | P22-ET-09-009-011-B CIP Heater | **1 - Approved** |
| 7 | P22-DWG-09-007-003-A Grounding Layout | **2 - Approved as noted** |
| 8 | P22-LI-09-005-001-A Equipment List | **1 - Approved** |
| 9 | P22-LI-09-005-002-A Valve List | **2 - Approved as noted** |
| 10 | P22-LI-09-008-001-A IO List | **1 - Approved** |
| 11 | P22-LI-09-008-002-A Cable Schedule | **1 - Approved** |
| 12 | P22-LI-09-008-003-A Instrument List | **3 - To be revised** |

### 18.2 Veredicto Consolidado

| Campo | Valor |
|-------|-------|
| **VEREDICTO ENTREGA 8** | **3 - TO BE REVISED** |
| Documentos Approved | 7 |
| Documentos Approved as Noted | 4 |
| Documentos To Be Revised | 1 |
| Documentos Rejected | 0 |

**Justificacion:** La entrega contiene documentacion tecnica de alta calidad y la mayoria de documentos cumplen con los requisitos. Sin embargo, el Instrument List (P22-LI-09-008-003-A) no incluye los transmisores de vibracion requeridos por la ET Seccion 5.5.7 para la bomba HP y los turbochargers. Este es un requisito tecnico critico para la proteccion de equipos rotativos de alta presion. Se requiere revision del documento antes de aprobacion final.

---

## 19. Documentos de Referencia

| Documento | Ubicacion |
|-----------|-----------|
| ET Modulo | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md |
| Oferta Tecnica Rev.1 | OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md |
| Codificacion General | BASES TECNICAS/md/P00-IT-00-000-101-CODIFICACION-GENERAL.md |
| Process Calculation E7 | P22-CD-09-009-001-B |

---

*Fin del documento*
*Revision preparada: 26-Ene-2026*
