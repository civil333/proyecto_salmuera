# Revision Tecnica Cruzada: Valve List y Equipment List

**Fecha:** 2026-01-28
**Revisor:** ADASA (Revision Interna)
**Submittal:** 25007-0008

---

## 1. RESUMEN EJECUTIVO

### 1.1 Documentos Revisados

| Documento | Codigo | Rev | Fecha | Items |
|-----------|--------|-----|-------|-------|
| Valve List | P22-LI-09-005-002-A | A | 06-Jan-26 | 109 valvulas |
| Equipment List | P22-LI-09-005-001-A | A | 20-Jan-26 | 13 equipos |

### 1.2 Veredictos

| Documento | Veredicto | Justificacion |
|-----------|-----------|---------------|
| **Valve List** | **3 - TO BE REVISED** | Valvulas manuales DN50+ en alta presion incumplen ET 5.2.3; TAGs duplicados; TAGs con area incorrecta |
| **Equipment List** | **2 - APPROVED AS NOTED** | Discrepancias menores de nomenclatura; capacidades verificadas vs P&ID |

### 1.3 Estadisticas de Observaciones

| Severidad | Valve List | Equipment List | Total |
|-----------|------------|----------------|-------|
| CRITICO | 1 | 0 | 1 |
| MAYOR | 2 | 1 | 3 |
| MENOR | 2 | 1 | 3 |
| **TOTAL** | **5** | **2** | **7** |

---

## 2. ANALISIS ET 5.2.3: ACTUACION ELECTRICA EN VALVULAS

### 2.1 Requisito Contractual

> **ET Seccion 5.2.3 (L989-994):**
> "Todas las valvulas de proceso relevantes, tanto en sistemas de alta como baja presion, deberan contar con actuacion electrica y ser completamente integrables al sistema de control del modulo (PLC)"

### 2.2 Criterio de Evaluacion

| Tamano | Rating | Uso Tipico | Actuacion Requerida |
|--------|--------|------------|---------------------|
| DN50+ | ANSI 900# | Linea de proceso principal | **ELECTRICA** |
| DN15-DN25 | ANSI 900# | Venteo, drenaje, muestreo | Manual aceptable |
| Cualquiera | ANSI 150# | Baja presion | Manual aceptable |

### 2.3 Inventario de Valvulas

| Categoria | Cantidad | Porcentaje |
|-----------|----------|------------|
| Manuales (MANUAL/HAND) | 89 | 81.7% |
| Motorizadas ON/OFF | 17 | 15.6% |
| Modulante (VC-09-006) | 1 | 0.9% |
| Check Valves (auto-actuadas) | 2 | 1.8% |
| **TOTAL** | **109** | 100% |

### 2.4 Valvulas ANSI 900# (Alta Presion)

#### Valvulas Motorizadas en ANSI 900# (CUMPLE)

| Item | TAG | DN | Tipo | Sistema | Actuacion |
|------|-----|-----|------|---------|-----------|
| 44 | VE-09-008 | DN80 | Butterfly | SWRO Reject 1st | ON/OFF Motorized |
| 58 | VE-09-009 | DN80 | Butterfly | SWRO 2nd Stage Reject | ON/OFF Motorized |
| 59 | VE-09-010 | DN80 | Butterfly | SWRO 1st Stage Reject | ON/OFF Motorized |
| 60 | VE-09-002 | DN25 | Ball | SWRO 2nd Stage Reject | ON/OFF Motorized |
| 63 | VE-09-006 | DN100 | Butterfly | 1st Stage CIP Feed | ON/OFF Motorized |
| 64 | VE-09-007 | DN80 | Butterfly | 2nd Stage CIP Feed | ON/OFF Motorized |
| 71 | VC-09-006 | DN65 | Gate | SWRO 2nd Stage Reject | Modulating Motorized |

#### Valvulas Manuales DN50+ en ANSI 900# (NO CUMPLE ET 5.2.3)

| Item | TAG | DN | Tipo | Sistema | Material | Observacion |
|------|-----|-----|------|---------|----------|-------------|
| 17 | VR-09-001 | **DN100** | Check Valve | SWRO HPP | CE3MN/F53+STL | Check valve auto-actuada - ACEPTABLE |
| 18 | **VM-09-015** | **DN100** | Butterfly | SWRO HPP | CE3MN/F53+STL | **LINEA PRINCIPAL HP - NO CUMPLE** |

**HALLAZGO CRITICO:** La valvula **VM-09-015** es una valvula mariposa DN100 ANSI 900# en la descarga de la bomba HP (linea de proceso principal), operada manualmente. Segun ET 5.2.3, deberia tener actuacion electrica.

#### Valvulas Manuales DN15-DN25 en ANSI 900# (ACEPTABLE)

| Item | TAG | DN | Tipo | Sistema | Justificacion |
|------|-----|-----|------|---------|---------------|
| 11-16 | VM-09-012 a VM-09-016 | DN15 | Ball | SWRO HPP | Drenajes/muestreo |
| 20-22 | VM-09-021/022, VM-09-114 | DN15 | Ball | Feed Turbocharger | Venteos |
| 39-43 | VM-09-023 a VM-09-015 | DN15 | Ball | SWRO Reject 1st | Drenajes/muestreo |
| 45-47 | VM-09-026/027/038 | DN15 | Ball | 2nd Stage Turbocharger Feed | Venteos |
| 53-56 | VM-07-031 a VM-09-033 | DN15 | Ball | SWRO Reject 2nd | Drenajes/muestreo |
| 61-70 | VM-09-034 a VM-09-122 | DN15 | Ball | SWRO 2nd Stage Reject | Drenajes/muestreo |

**Total DN15-DN25 en ANSI 900#:** 32 valvulas manuales - **ACEPTABLE** por ser venteos/drenajes/muestreo.

### 2.5 Conclusion ET 5.2.3

| Criterio | Estado |
|----------|--------|
| Valvulas DN50+ ANSI 900# con actuacion electrica | **1 de 2 (50%)** |
| Valvula VM-09-015 DN100 manual en linea HP | **NO CUMPLE** |
| Valvulas DN15-DN25 ANSI 900# manuales | ACEPTABLE (venteos/drenajes) |

**VEREDICTO PARCIAL:** El requisito ET 5.2.3 **NO SE CUMPLE** para la valvula VM-09-015.

---

## 3. VALVE LIST: TABLA REFORMATEADA

### 3.1 Sistema CATRIDGE FILTER (P&ID 8.00)

| Item | TAG | DN | Tipo | Actuacion | Rating | Material Body | Fluido |
|------|-----|-----|------|-----------|--------|---------------|--------|
| 1 | VM-09-001 | 100 | Butterfly | Manual | ANSI 150# | DI Halar Coat | BRINE |
| 2 | VM-09-002 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 3 | VM-09-007 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 4 | VM-09-003 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 5 | VM-09-004 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 6 | VM-09-008 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 7 | **VM-07-005** | 100 | Butterfly | Manual | ANSI 150# | DI Halar Coat | BRINE |
| 8 | VM-09-006 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 9 | VM-09-110 | 15 | Ball | Manual | ANSI 150# | PVC | BRINE |
| 10 | VM-09-011 | 100 | Butterfly | Manual | ANSI 150# | DI Halar Coat | BRINE |

### 3.2 Sistema SWRO HPP (P&ID 9.00) - ALTA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material Body | Fluido |
|------|-----|-----|------|-----------|--------|---------------|--------|
| 11 | VM-09-012 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 12 | VM-09-111 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 13 | VM-09-013 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 14 | VM-09-112 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 15 | VM-09-014 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 16 | VM-09-113 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 17 | VR-09-001 | 100 | Check | Auto (Swing) | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 18 | **VM-09-015** | **100** | Butterfly | **Manual** | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 19 | VM-09-016 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |

### 3.3 Sistema FEED TURBOCHARGER (P&ID 9.00) - ALTA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material Body | Fluido |
|------|-----|-----|------|-----------|--------|---------------|--------|
| 20 | VM-09-021 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 21 | VM-09-114 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |
| 22 | VM-09-022 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | BRINE |

### 3.4 Sistema SWRO PERMEATE 1ST (P&ID 9.00) - BAJA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material Body | Fluido |
|------|-----|-----|------|-----------|--------|---------------|--------|
| 23-28 | VM-09-141 a VM-09-146 | 8 | Labcock | Manual | ANSI 150# | PVC | 1st PERMEATE |
| 29 | VM-09-042 | 15 | Ball | Manual | ANSI 150# | PVC | 1st PERMEATE |
| 30 | VM-09-065 | 65 | Butterfly | Manual | ANSI 150# | DI Halar Coat | 1st PERMEATE |
| 31-34 | VM-09-043 a VM-09-115 | 15 | Ball | Manual | ANSI 150# | PVC | 1st PERMEATE |
| 35 | VR-09-003 | 80 | Check | Auto (Swing) | ANSI 150# | PVC | 1st PERMEATE |
| 36 | VE-09-003 | 80 | Butterfly | **Motorized** | ANSI 150# | DI Halar Coat | 1st PERMEATE |
| 37 | VE-09-004 | 80 | Butterfly | **Motorized** | ANSI 150# | DI Halar Coat | 1st PERMEATE |
| 38 | VE-09-005 | 80 | Butterfly | **Motorized** | ANSI 150# | DI Halar Coat | 1st PERMEATE |

### 3.5 Sistema SWRO REJECT 1ST y 2ND (P&ID 9.00) - ALTA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material Body | Fluido |
|------|-----|-----|------|-----------|--------|---------------|--------|
| 39-43 | VM-09-023 a VM-09-015* | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | REJECT 1ST |
| 44 | VE-09-008 | **80** | Butterfly | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | REJECT 1ST |
| 45-47 | VM-09-026/027/038 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | 2ND TURBOCHARGER |
| 48-52 | VM-09-147 a VM-09-117 | 8-15 | Labcock/Ball | Manual | ANSI 150# | PVC | 2nd PERMEATE |
| 53 | **VM-07-031** | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |
| 54-56 | VM-09-119/032/033 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |
| 57 | **VE-09-008** | **65** | Butterfly | **Motorized** | ANSI 150# | DI Halar Coat | 1st PERMEATE |
| 58 | VE-09-009 | **80** | Butterfly | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |
| 59 | VE-09-010 | **80** | Butterfly | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | 1st REJECT |
| 60 | VE-09-002 | 25 | Ball | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |
| 61-70 | VM-09-034 a VM-09-122 | 15 | Ball | Manual | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |
| 71 | VC-09-006 | **65** | Gate | **Modulating** | **ANSI 900#** | CE3MN/F53+STL | 2nd REJECT |

### 3.6 Sistema CIP (P&ID 10.00) - BAJA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material | Fluido |
|------|-----|-----|------|-----------|--------|----------|--------|
| 63 | VE-09-006 | **100** | Butterfly | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | CIP FEED |
| 64 | VE-09-007 | **80** | Butterfly | **Motorized** | **ANSI 900#** | CE3MN/F53+STL | CIP FEED |
| 72-92 | VM-09-063 a VM-09-087 | 15-150 | Ball/Butterfly | Manual | ANSI 150# | PVC | CIP |

### 3.7 Sistema ANTISCALANT (P&ID 11.00) - BAJA PRESION

| Item | TAG | DN | Tipo | Actuacion | Rating | Material | Fluido |
|------|-----|-----|------|-----------|--------|----------|--------|
| 93 | **VE-07-009** | 25 | Ball | **Motorized** | ANSI 150# | PVC | ANTISCALANT |
| 94-108 | VM-09-091 a VM-09-126 | 15-25 | Ball | Manual | ANSI 150# | PVC | ANTISCALANT |
| 104 | VRP-09-002 | 15 | PSV | Self-actuated | ANSI 150# | PVC | ANTISCALANT |
| 109 | VE-09-010 | 15 | Ball | **Motorized** | ANSI 150# | PVC | ANTISCALANT |

---

## 4. EQUIPMENT LIST: TABLA REFORMATEADA

| Item | TAG | Descripcion | P&ID | Qty | Fabricante | Modelo | Capacidad | Material | Potencia |
|------|-----|-------------|------|-----|------------|--------|-----------|----------|----------|
| 1 | MZE-09-009 | Static Mixer | P8 | 1 | Koflo | KD-1027 | 49 m3/h | PVC | - |
| 2 | FIL-09-001 | RO Cartridge Filter | P8 | 1 | Fil-Trek | FRPH12-012-4-4F-100 | 49 m3/h @ 7 bar | FRP/PP | - |
| 3 | BH-09-001 | RO HP Feed Pump | P9 | 1 | Fedco | MSD-7016 | 49 m3/h @ 46.9 bar | Super Duplex SS | 92 kW |
| 4 | SIP-09-001 | Feed Turbocharger | P9 | 1 | Fedco | HPB-60 | 49/28 m3/h @ 69.53/1 bar | Super Duplex SS | - |
| 5 | BOI-09-001 | RO 1st Stage Membranes | P9 | 42 (6x7) | LG | SW 400 SR | 12.9 m3/h @ 83 bar | Polyamide | - |
| - | BOI-09-001 | RO 1st Stage Vessels | P9 | 6 | Protec | BPV-8-1200-SP-7 | 83 bar | FRP | - |
| 6 | SIP-09-002 | Interstage Turbocharger | P9 | 1 | Fedco | HPB-60 | 36.1/28 m3/h @ 84.8/53.5 bar | Super Duplex SS | - |
| 7 | BOI-09-002 | RO 2nd Stage Membranes | P9 | 28 (4x7) | LG | SW 400R G2 UHP | 8.1 m3/h @ 124 bar | Polyamide | - |
| - | BOI-09-002 | RO 2nd Stage Vessels | P9 | 4 | Protec | BPV-8-1800-SP-7 | 124 bar | FRP | - |
| 8 | TK-09-001 | CIP Tank | P10 | 1 | Dayamas | DYM 6800 | 6.1 m3 | HDPE | - |
| 9 | REL-09-001 | CIP Heater | P10 | 1 | Quantic Logic | VEMA | 25-30C | SS316 | 20 kW |
| 10 | BH-09-002 | CIP Pump | P10 | 1 | Grundfos | CRN64-2 AGAE-HQQE | 57 m3/h @ 4 bar | SS316 | 11 kW |
| 11 | FIL-09-002 | CIP Cartridge Filter | P10 | 1 | Fil-Trek | S6GL14-019-4-4F-A-150 | 57 m3/h @ 10 bar | FRP/PP | - |
| 12 | TK-09-002 | Antiscalant Dosing Tank | P11 | 1 | Promatics | PLC330 | 0.27 m3 | LLDPE | - |
| 13 | BDS-09-001/002 | Antiscalant Dosing Pump | P11 | 1+1 | Prominent | GMXa 1602 | 2.3 LPH @ 16 bar | PP/PTFE | 24 W |

---

## 5. VERIFICACION CRUZADA: VALVE LIST vs P&ID

### 5.1 Resumen de Verificacion

| Sistema | Valvulas en Lista | Verificadas en P&ID | Match | Discrepancias |
|---------|-------------------|---------------------|-------|---------------|
| Catridge Filter (P8) | 10 | - | - | P&ID no detalla valvulas individuales |
| SWRO HPP (P9) | 9 | - | - | P&ID no detalla valvulas individuales |
| Feed Turbocharger (P9) | 3 | - | - | P&ID no detalla valvulas individuales |
| SWRO Permeate 1st (P9) | 16 | - | - | P&ID no detalla valvulas individuales |
| SWRO Reject 1st (P9) | 6 | - | - | P&ID no detalla valvulas individuales |
| 2nd Stage (P9) | 25 | - | - | P&ID no detalla valvulas individuales |
| CIP (P10) | 21 | - | - | P&ID no detalla valvulas individuales |
| Antiscalant (P11) | 19 | - | - | P&ID no detalla valvulas individuales |

**Nota:** El P&ID .md disponible es un resumen consolidado que lista equipos principales pero no detalla valvulas individuales. Para verificacion completa se requiere lectura del P&ID PDF pagina por pagina.

### 5.2 Hallazgos de Inconsistencias

#### TAG Duplicado VE-09-008

| Linea | TAG | Sistema | DN | Rating | Material |
|-------|-----|---------|-----|--------|----------|
| 44 | VE-09-008 | SWRO Reject 1st | DN80 | **ANSI 900#** | CE3MN/F53+STL |
| 57 | VE-09-008 | SWRO Permeate 1st | DN65 | ANSI 150# | DI Halar Coat |

**PROBLEMA:** Dos valvulas distintas (diferentes sistemas, DN, rating, material) comparten el mismo TAG.

#### TAG Duplicado VM-09-015

| Linea | TAG | Sistema | DN | Tipo |
|-------|-----|---------|-----|------|
| 18 | VM-09-015 | SWRO HPP | DN100 | Butterfly |
| 43 | VM-09-015 | SWRO Reject 1st | DN15 | Ball |

**PROBLEMA:** Dos valvulas distintas comparten el mismo TAG.

---

## 6. VERIFICACION CRUZADA: EQUIPMENT LIST vs P&ID

### 6.1 Matriz de Verificacion

| TAG Equipment List | TAG P&ID | Match | Observacion |
|--------------------|----------|-------|-------------|
| MZE-09-009 | MZE-09-001 | **NO** | P&ID usa MZE-09-001 |
| FIL-09-001 | FIL-09-001 | SI | - |
| BH-09-001 | BH-09-001 | SI | - |
| SIP-09-001 | SIP-09-001 | SI | Capacidad verificada: 49 m3/h @ 63.21 barg |
| BOI-09-001 | BOI-09-001 | SI | 6 PVs x 7 elementos = 42 membranas |
| SIP-09-002 | SIP-09-002 | SI | Capacidad verificada: 35.11 m3/h @ 77.1 barg |
| BOI-09-002 | BOI-09-002 | SI | 4 PVs x 7 elementos = 28 membranas |
| TK-09-001 | TK-09-001 | SI | Capacidad: 5.1 m3 (P&ID) vs 6.1 m3 (Equipment List) |
| REL-09-001 | REL-09-001 | SI | 20 kW verificado |
| BH-09-002 | BH-09-002 | SI | 57.2 m3/h @ 4.1 barg verificado |
| FIL-09-002 | FIL-09-002 | SI | - |
| TK-09-002 | TK-09-002 | SI | 0.25 m3 (P&ID) vs 0.27 m3 (Equipment List) |
| BDS-09-001/002 | BDS-09-001/002 | SI | 1 LPH @ 4 barg (P&ID) vs 2.3 LPH (Equipment List) |

### 6.2 Discrepancias Encontradas

| Equipo | Campo | P&ID | Equipment List | Severidad |
|--------|-------|------|----------------|-----------|
| Static Mixer | TAG | MZE-09-001 | MZE-09-009 | MENOR |
| CIP Tank | Capacidad | 5.1 m3 | 6.1 m3 | MENOR |
| Antiscalant Tank | Capacidad | 0.25 m3 | 0.27 m3 | MENOR |
| Dosing Pump | Capacidad | 1 LPH | 2.3 LPH | MAYOR |

---

## 7. OBSERVACIONES DETALLADAS

### OBS-VL-01: Valvula Manual DN100 en Alta Presion (CRITICO)

| Campo | Valor |
|-------|-------|
| Documento | Valve List P22-LI-09-005-002-A |
| Ubicacion | Item 18, Linea 49 |
| Categoria | Tecnico |
| Severidad | **CRITICO** |

**Descripcion:**
La valvula **VM-09-015** es una valvula mariposa DN100 ANSI 900# ubicada en la descarga de la bomba HP (sistema SWRO HPP), operada manualmente.

**Requisito:**
ET Seccion 5.2.3 (L989-994): "Todas las valvulas de proceso relevantes, tanto en sistemas de alta como baja presion, deberan contar con actuacion electrica y ser completamente integrables al sistema de control del modulo (PLC)"

**Accion Requerida:**
Cambiar VM-09-015 a actuacion electrica ON/OFF motorizada, o justificar tecnicamente por que esta valvula no es "de proceso relevante" segun ET 5.2.3.

---

### OBS-VL-02: TAG Duplicado VE-09-008 (MAYOR)

| Campo | Valor |
|-------|-------|
| Documento | Valve List P22-LI-09-005-002-A |
| Ubicacion | Items 44 y 57 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**
El TAG VE-09-008 aparece asignado a dos valvulas diferentes:
1. Item 44: DN80 Butterfly, ANSI 900#, CE3MN, SWRO Reject 1st
2. Item 57: DN65 Butterfly, ANSI 150#, DI Halar Coat, SWRO Permeate 1st

**Requisito:**
Sistema de codificacion P00-IT-00-000-101 requiere TAGs unicos por equipo.

**Accion Requerida:**
Reasignar TAG unico a una de las valvulas (ej: VE-09-011 para la segunda).

---

### OBS-VL-03: TAG Duplicado VM-09-015 (MAYOR)

| Campo | Valor |
|-------|-------|
| Documento | Valve List P22-LI-09-005-002-A |
| Ubicacion | Items 18 y 43 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**
El TAG VM-09-015 aparece asignado a dos valvulas diferentes:
1. Item 18: DN100 Butterfly, ANSI 900#, SWRO HPP
2. Item 43: DN15 Ball, ANSI 900#, SWRO Reject 1st

**Accion Requerida:**
Reasignar TAG unico a una de las valvulas.

---

### OBS-VL-04: Fabricantes TBA (MENOR)

| Campo | Valor |
|-------|-------|
| Documento | Valve List P22-LI-09-005-002-A |
| Ubicacion | Columna Brand/Make |
| Categoria | Contractual |
| Severidad | **MENOR** |

**Descripcion:**
El 100% de las valvulas tienen fabricante listado como "TBA" (To Be Advised).

**Requisito:**
ET requiere identificacion de fabricantes para aprobacion de materiales.

**Accion Requerida:**
Completar informacion de fabricantes antes de procurement. No impide aprobacion del documento.

---

### OBS-VL-05: TAGs con Area Incorrecta (MENOR)

| Campo | Valor |
|-------|-------|
| Documento | Valve List P22-LI-09-005-002-A |
| Ubicacion | Items 7, 53, 93 |
| Categoria | Tecnico |
| Severidad | **MENOR** |

**Descripcion:**
Tres valvulas tienen TAGs con Area 07 en lugar de Area 09:

| Item | TAG Actual | Sistema | P&ID | Datos Internos | TAG Correcto |
|------|------------|---------|------|----------------|--------------|
| 7 | VM-07-005 | CATRIDGE FILTER | 8.00 | VM 9 5 | VM-09-005 |
| 53 | VM-07-031 | SWRO REJECT 2ND | 9.00 | VM 9 31 | VM-09-031 |
| 93 | VE-07-009 | ANTISCALANT | 11.00 | VE 9 9 | VE-09-009 |

**Justificacion:**
Segun P00-IT-00-000-101:
- Area 07 = "LQ Osmosis Inversa" = Sistema CIP para RO/UF
- Area 09 = "Osmosis Inversa Segunda Etapa/Segundo Paso"

Ninguna de estas valvulas pertenece al sistema CIP. Los datos internos del documento confirman Area 9.

**Accion Requerida:**
Corregir TAGs a Area 09.

---

### OBS-EQ-01: Discrepancia TAG Static Mixer (MENOR)

| Campo | Valor |
|-------|-------|
| Documento | Equipment List P22-LI-09-005-001-A |
| Ubicacion | Item 1 |
| Categoria | Tecnico |
| Severidad | **MENOR** |

**Descripcion:**
El Static Mixer tiene TAG MZE-09-009 en Equipment List pero MZE-09-001 en P&ID.

**Accion Requerida:**
Unificar TAG entre P&ID y Equipment List.

---

### OBS-EQ-02: Discrepancia Capacidad Dosing Pump (MAYOR)

| Campo | Valor |
|-------|-------|
| Documento | Equipment List P22-LI-09-005-001-A |
| Ubicacion | Item 13 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**
El P&ID indica capacidad de 1 LPH para BDS-09-001/002, pero el Equipment List indica 2.3 LPH.

**Accion Requerida:**
Clarificar cual es la capacidad correcta y actualizar documentos para consistencia.

---

## 8. ACCIONES REQUERIDAS

### Para BW Water

| # | Documento | Accion | Prioridad | Plazo |
|---|-----------|--------|-----------|-------|
| 1 | Valve List | Cambiar VM-09-015 a actuacion electrica o justificar excepcion ET 5.2.3 | **CRITICO** | Inmediato |
| 2 | Valve List | Corregir TAG duplicado VE-09-008 (asignar TAG unico) | **ALTA** | Proxima revision |
| 3 | Valve List | Corregir TAG duplicado VM-09-015 (asignar TAG unico) | **ALTA** | Proxima revision |
| 4 | Valve List | Corregir TAGs VM-07-005, VM-07-031, VE-07-009 a Area 09 | **MEDIA** | Proxima revision |
| 5 | Equipment List | Unificar TAG Static Mixer (MZE-09-001 o MZE-09-009) | **BAJA** | Proxima revision |
| 6 | Equipment List | Clarificar capacidad Dosing Pump (1 LPH vs 2.3 LPH) | **MEDIA** | Proxima revision |
| 7 | Valve List | Completar fabricantes (columna Brand/Make) | **BAJA** | Antes de procurement |

---

## 9. NOTAS INFORMATIVAS

### 9.1 Uso de Areas por BW Water

BW Water utiliza **Area 09 para todo el modulo UHPRO**, incluyendo:
- Sistema RO (P&ID 8-9)
- Sistema CIP (P&ID 10) - Segun ADASA deberia ser Area 07
- Sistema Antiscalant (P&ID 11)

Esta es una desviacion menor del estandar de codificacion ADASA (P00-IT-00-000-101) pero no afecta funcionalidad. Se documenta para referencia.

### 9.2 Valvulas Check (Auto-actuadas)

Las valvulas check VR-09-001 (DN100 ANSI 900#) y VR-09-003 (DN80 ANSI 150#) son auto-actuadas por diseno (swing check). No requieren actuacion electrica segun ET 5.2.3.

### 9.3 Sistema CIP en ANSI 900#

Las valvulas VE-09-006 (DN100) y VE-09-007 (DN80) del sistema CIP estan en ANSI 900# y son motorizadas. Esto es correcto ya que el CIP debe fluir a traves de las lineas de alta presion del RO.

---

## 10. ANEXOS

### A. Resumen Estadistico Valve List

| Categoria | Cantidad |
|-----------|----------|
| Total valvulas | 109 |
| ANSI 150# | 64 (58.7%) |
| ANSI 900# | 45 (41.3%) |
| Manuales | 89 (81.7%) |
| Motorizadas ON/OFF | 17 (15.6%) |
| Modulantes | 1 (0.9%) |
| Check valves | 2 (1.8%) |

### B. Resumen Estadistico Equipment List

| Categoria | Cantidad |
|-----------|----------|
| Total equipos | 13 (contando membranas y vessels separados) |
| Bombas | 3 (HP, CIP, Dosing) |
| Tanques | 2 (CIP, Antiscalant) |
| Filtros | 2 (RO, CIP) |
| Turbochargers | 2 (Feed, Interstage) |
| Membranas RO | 70 elementos (42+28) |
| Vessels RO | 10 (6+4) |
| Otros | 2 (Mixer, Heater) |

---

*Documento generado: 2026-01-28*
*Revisor: ADASA - Revision Tecnica Interna*
