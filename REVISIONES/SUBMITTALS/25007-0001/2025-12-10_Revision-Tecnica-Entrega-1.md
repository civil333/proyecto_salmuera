# REVISION TECNICA - ENTREGA 1 BW WATER

**Fecha:** 10 de diciembre de 2025
**Proyecto:** BAE 12803 - Modulo de Salmuera Taltal
**Revision:** #006

---

## DOCUMENTOS REVISADOS

| Codigo | Descripcion |
|--------|-------------|
| P22-ET-09-000-01 | Datasheet Container |
| P22-ITEM-09-009-001-A | Datasheet UHPRO System (Membrane + Vessel) |
| P22-ITEM-09-009-002-A | Datasheet RO High Pressure Pump |
| P22-ITEM-09-009-003-A | Datasheet CIP Pump |
| P22-ITEM-09-009-004-A | Datasheet Antiscalant Dosing Pump |
| P22-ET-09-006-001-A | Piping Specifications |
| P22-ET-09-006-002-A | Painting Specifications |
| P22-ET-09-007-001-A | Datasheet Electrical Aux Component |
| P22-ET-09-008-001-A | Datasheet PLC & HMI |
| P22-LI-09-007-001-A | Electrical Load List |
| P22-CD-09-007-001-A | Single Line Diagram |
| P22-CD-09-009-001-A | Process Calculation |
| P22-DWG-09-009-001-A | PFD |

---

## DOCUMENTOS DE REFERENCIA

| Documento | Codigo | Ubicacion |
|-----------|--------|-----------|
| Especificacion Tecnica | P22-ET-09-000-001-0 | `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md` |
| Codificacion ADASA | P00-IT-00-000-101 | `BASES TECNICAS/md/P00-IT-00-000-101-CODIFICACION-GENERAL.md` |
| Bases Administrativas | BAE 12803 | `BASES TECNICAS/md/BAE-12803-PLANTA-MODULAR.md` |
| Oferta Tecnica | Rev.1 (VIGENTE) | `OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md` |

---

## 1. CONTENEDOR (P22-ET-09-000-01)

### 1.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Largo maximo | **ET 5.1.10, pag.14** | 13 metros | 12.192 m (40 ft) | CUMPLE |
| Ancho maximo | **ET 5.1.10, pag.14** | 2.5 metros | 2.438 m | CUMPLE |
| Alto | **ET 5.1.10, pag.14** | 2.8 metros | 2.896 m | **EXCEDE 96mm** |
| Puerta acceso peatonal | **ET 5.1.10, pag.15** | 900 x 2200 mm | NO ESPECIFICADO | **NO CUMPLE** |
| Puerta acceso equipos | **ET 5.1.10, pag.15** | Segun equipo mayor, apertura 110°, hacia exterior | NO ESPECIFICADO | **NO CUMPLE** |
| Puerta emergencia | **ET 5.1.10, pag.15** | Requerida | NO ESPECIFICADO | **NO CUMPLE** |
| Puerta corrediza lateral | **ET 5.1.10, pag.15** | Requerida | NO ESPECIFICADO | **NO CUMPLE** |
| Piso rejilla PRFV | **ET 5.1.10, pag.15** | Antideslizante | NO ESPECIFICADO | **NO CUMPLE** |

### 1.2 Incumplimientos Especificos

| # | Incumplimiento | Referencia Exacta | Texto Requisito |
|---|----------------|-------------------|-----------------|
| 1 | Puerta acceso peatonal no especificada | **P22-ET-09-000-001-0, Seccion 5.1.10, Pagina 15** | *"Las puertas de acceso de personas deben tener un ancho de 900 mm por 2.200 mm de alto"* |
| 2 | Puerta equipos no especificada | **P22-ET-09-000-001-0, Seccion 5.1.10, Pagina 15** | *"Las puertas de acceso para equipos deberan tener dimensiones adecuadas... con un angulo de apertura de 110° y se abriran siempre hacia el exterior"* |
| 3 | Puerta emergencia no especificada | **P22-ET-09-000-001-0, Seccion 5.1.10, Pagina 15** | *"El contenedor debera considerar puerta de acceso peatonal, puerta para acceso de equipos y puerta de emergencia"* |
| 4 | Puerta corrediza no especificada | **P22-ET-09-000-001-0, Seccion 5.1.10, Pagina 15** | *"el contenedor debera garantizar el acceso lateral mediante una puerta corrediza"* |
| 5 | Rejilla PRFV no especificada | **P22-ET-09-000-001-0, Seccion 5.1.10, Pagina 15** | *"El piso por donde caminaran los operarios debera constar de una rejilla de PRFV antideslizante"* |

**OBSERVACION CRITICA:** El datasheet del contenedor es generico (catalogo Pacific Marine) y NO incluye las modificaciones especificas requeridas por la ET Seccion 5.1.10.

---

## 2. BOMBA DE ALTA PRESION (P22-ITEM-09-009-002-A)

### 2.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Tipo | **ET 5.1.1, pag.10** | Desplazamiento positivo o centrifuga multietapa | Centrifuga Horizontal | CUMPLE |
| Caudal | **ET 5.1.1, pag.10** | 49 m³/h | 49 m³/h | CUMPLE |
| Material voluta | **ET 5.1.1, pag.10** | **Super Duplex PREN > 40** | SS Duplex PREN > 40 | **VERIFICAR** |
| Material impulsor | **ET 5.1.1, pag.10** | **Super Duplex PREN > 40** | SS Duplex PREN > 40 | **VERIFICAR** |
| Tension/frecuencia | **ET 5.1.1, pag.10** | 3 x 380 V / 50 Hz | 380V / 50Hz / 3ph | CUMPLE |
| Proteccion/aislacion | **ET 5.1.1, pag.10** | IP55 / Clase B | IP55 / Clase B | CUMPLE |
| Tipo arranque | **ET 5.1.1, pag.10** | VFD | VFD | CUMPLE |
| RTDs rodamientos | **ET 5.1.1, pag.10** | **RTDs a 3 hilos para temperatura de rodamientos** | NO MENCIONADO | **NO CUMPLE** |

### 2.2 Incumplimientos Especificos

| # | Incumplimiento | Referencia Exacta | Texto Requisito |
|---|----------------|-------------------|-----------------|
| 1 | Material dice "Duplex" no "Super Duplex" | **P22-ET-09-000-001-0, Seccion 5.1.1, Pagina 10** | *"Material voluta: Acero inoxidable Super Duplex PREN > 40"* y *"Material impulsor: Acero inoxidable Super Duplex PREN > 40"* |
| 2 | RTDs no mencionados | **P22-ET-09-000-001-0, Seccion 5.1.1, Pagina 10** | *"Instrumentacion: RTDs a 3 hilos para temperatura de rodamientos"* |

**OBSERVACION:** La ET especifica explicitamente "**Super** Duplex" (no solo "Duplex"). Solicitar aclaracion si es error de nomenclatura o material diferente.

---

## 3. BOMBA CIP (P22-ITEM-09-009-003-A)

### 3.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Tipo | **ET 5.1.4, pag.11-12** | **Centrifuga Vertical** | PENDIENTE VERIFICAR | **VERIFICAR** |
| Material voluta | **ET 5.1.4, pag.11** | AISI 316 | PENDIENTE VERIFICAR | VERIFICAR |
| Material impulsor | **ET 5.1.4, pag.11** | AISI 316 | PENDIENTE VERIFICAR | VERIFICAR |
| Tension/frecuencia | **ET 5.1.4, pag.11** | 3 x 380 V / 50 Hz | 380V / 50Hz / 3ph | CUMPLE |
| Proteccion/aislacion | **ET 5.1.4, pag.12** | IP55 / Clase B | PENDIENTE VERIFICAR | VERIFICAR |
| Tipo arranque | **ET 5.1.4, pag.12** | **Partida directa** | VFD (segun Load List) | **DIFERENCIA** |
| RTDs rodamientos | **ET 5.1.4, pag.12** | **RTDs a 3 hilos para rodamientos** | NO MENCIONADO | **NO CUMPLE** |

### 3.2 Incumplimientos Especificos

| # | Incumplimiento | Referencia Exacta | Texto Requisito |
|---|----------------|-------------------|-----------------|
| 1 | Tipo de arranque diferente | **P22-ET-09-000-001-0, Seccion 5.1.4, Pagina 12** | *"Tipo de Arranque: Partida directa"* - DS indica VFD |
| 2 | RTDs no mencionados | **P22-ET-09-000-001-0, Seccion 5.1.4, Pagina 12** | *"Instrumentacion: RTDs a 3 hilos para rodamientos"* |

**OBSERVACION:** La ET indica "Partida directa" pero el Load List muestra VFD. Si es mejora, documentar justificacion.

---

## 4. BOMBA DOSIFICADORA (P22-ITEM-09-009-004-A)

### 4.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Marca | **ET 5.1.8, pag.13** | Grundfos, Milton Roy | PENDIENTE VERIFICAR | VERIFICAR |
| Tipo | **ET 5.1.8, pag.13** | **Membrana** | PENDIENTE VERIFICAR | VERIFICAR |

### 4.2 Incumplimientos Especificos

| # | Incumplimiento | Referencia Exacta | Texto Requisito |
|---|----------------|-------------------|-----------------|
| 1 | Falta verificar tipo Membrana | **P22-ET-09-000-001-0, Seccion 5.1.8, Pagina 13** | *"Tipo: Membrana"* |

---

## 5. SISTEMA UHPRO - MEMBRANAS Y VESSELS (P22-ITEM-09-009-001-A)

### 5.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Marca membranas | **ET 5.1.7, pag.13** | DUPONT, HYDRANAUTICS, LG | LG | CUMPLE |
| Tipo | **ET 5.1.7, pag.13** | Poliamida espiral | Polyamide Thin-Film Composite | CUMPLE |
| Diametro | **ET 5.1.7, pag.13** | 8" | 7.9" OD | CUMPLE |
| Longitud | **ET 5.1.7, pag.13** | 40" | 40" | CUMPLE |
| Marca tubos presion | **ET 5.1.6, pag.12** | PROTEC o similar | Protec o First Line | CUMPLE |
| Material tubos | **ET 5.1.6, pag.12** | PRFV | FRP | CUMPLE |
| Presion Vessel UHPRO | **ET 5.1.6, pag.12** | **1800 psi para UHPRO** | Stage 2: 1800 psi | CUMPLE |
| Elementos por tubo | **ET 5.1.6, pag.12** | 7 membranas de 8" | 7 | CUMPLE |

---

## 6. ESPECIFICACION DE PIPING (P22-ET-09-006-001-A)

### 6.1 Alta Presion - Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Material caneria | **ET 5.2.2, pag.16** | ASTM A790 UNS S32750 PREN>40 SCH80 | ASTM A790 UNS S32750 PREN>40 SCH80 | CUMPLE |
| Clase flange | **ET 5.2.2, pag.16** | 900 | 900 | CUMPLE |
| Material flange | **ET 5.2.2, pag.16** | ASTM A182 F53 UNS S32750 | ASTM A182 F53 UNS S32750 | CUMPLE |
| Empaquetaduras | **ET 5.2.2, pag.16** | Espirometalica PTFE | Spiral Wound PTFE con anillo Super Duplex | CUMPLE |
| Victaulic | **ET 5.2.2, pag.16** | ASTM A-890 Gr. CE8MN EPDM | ASTM A890 Grade CE8MN EPDM | CUMPLE |

### 6.2 Baja Presion - Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Material | **ET 5.2.1, pag.16** | PVC SCH 80 ASTM D1784/D1785 | PVC SCH 80 ASTM D1784/D1785 | CUMPLE |
| Clase flange | **ET 5.2.1, pag.16** | 150 | 150 | CUMPLE |

---

## 7. ESPECIFICACION DE PINTURA (P22-ET-09-006-002-A)

### 7.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Preparacion superficie | **ET 5.1.9, pag.13** | SSPC-SP10 / Sa 2½ | PENDIENTE VERIFICAR | **VERIFICAR** |
| Imprimacion | **ET 5.1.9, pag.14** | Zinc Clad II 80µm | PENDIENTE VERIFICAR | **VERIFICAR** |
| Capa intermedia | **ET 5.1.9, pag.14** | Macropoxy 646 200µm | PENDIENTE VERIFICAR | **VERIFICAR** |
| Acabado | **ET 5.1.9, pag.14** | Acrolon 218 HS 75µm | PENDIENTE VERIFICAR | **VERIFICAR** |
| Espesor total | **ET 5.1.9, pag.14** | >= 355µm | PENDIENTE VERIFICAR | **VERIFICAR** |
| Color | **ET 5.1.9, pag.14** | RAL 5012 | PENDIENTE VERIFICAR | **VERIFICAR** |

### 7.2 Incumplimientos Potenciales

| # | Item a Verificar | Referencia Exacta | Texto Requisito |
|---|------------------|-------------------|-----------------|
| 1 | Preparacion superficie | **P22-ET-09-000-001-0, Seccion 5.1.9, Pagina 13** | *"Limpieza mediante chorreado abrasivo hasta grado SSPC-SP10 (Metal Casi Blanco) / Sa 2½ (ISO 8501-1)"* |
| 2 | Sistema de pintura completo | **P22-ET-09-000-001-0, Seccion 5.1.9, Pagina 14** | *"Zinc Clad II 80µm + Macropoxy 646 200µm + Acrolon 218 HS 75µm = minimo 355µm"* |
| 3 | Color RAL 5012 | **P22-ET-09-000-001-0, Seccion 5.1.9, Pagina 14** | *"Color: RAL 5012 (Azul Luminoso)"* |

---

## 8. PLC Y HMI (P22-ET-09-008-001-A)

### 8.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Fabricante | Por proveedor | - | Allen Bradley | OK |
| Modelo | Por proveedor | - | CompactLogix 5069-L320ER | OK |
| Comunicacion | **ET Seccion 5** | **Modbus TCP/RTU, Ethernet/IP** | 2x Ethernet/IP | **VERIFICAR MODBUS** |
| IP tablero | **ET 5.4.1** | IP55 minimo | NO ESPECIFICADO | **FALTA INFO** |

### 8.2 Incumplimientos Potenciales

| # | Item a Verificar | Referencia Exacta | Texto Requisito |
|---|------------------|-------------------|-----------------|
| 1 | Protocolo Modbus | **P22-ET-09-000-001-0, Seccion 5** | Verificar si Modbus TCP/RTU es requerido ademas de Ethernet/IP |

---

## 9. ELECTRICAL LOAD LIST (P22-LI-09-007-001-A)

### 9.1 Requisitos vs Entrega

| Requisito | Referencia ET | Valor Requerido | Valor Entregado | Veredicto |
|-----------|---------------|-----------------|-----------------|-----------|
| Tension trifasica | **ET 5.4.7** | 3 x 380 V / 50 Hz | 380V / 50Hz / 3ph | CUMPLE |
| Tension monofasica | **ET 5.4.7** | 220 V / 50 Hz | 220V / 50Hz | CUMPLE |
| SEC garantizado | **ET 10.1.3** | < 5.0 kWh/m³ | 4.52 kWh/m³ | CUMPLE |

---

## 10. REVISION DE CODIFICACION DOCUMENTAL

### 10.1 Requisitos de Codificacion

Segun **P00-IT-00-000-101, Seccion 2.1**, el formato requerido es:

**A - B - C - D - E - F**

Donde:
- A = Numero de Proyecto (P22 segun Tabla 2-1)
- B = **Tipo de Documento (segun Tabla 2-2)**
- C = Area del proyecto (09 segun Tabla 2-3)
- D = Codigo de Disciplina (segun Tabla 2-4)
- E = Numero correlativo de 3 digitos
- F = Letra o numero de la revision

### 10.2 Tipos de Documento Validos (Tabla 2-2)

| Tipo de Documento | Abreviatura |
|-------------------|-------------|
| Especificacion Tecnica | **ET** |
| Criterios de Diseno | CD |
| Planos | DWG |
| Listado | LI |
| Memoria de Calculo | MC |

**NOTA: El tipo "ITEM" NO existe en la Tabla 2-2 del instructivo P00-IT-00-000-101.**

### 10.3 Analisis de Codificacion

| Codigo BW Water | Cumple | Incumplimiento |
|-----------------|--------|----------------|
| P22-CD-09-009-001-A | CUMPLE | - |
| P22-DWG-09-009-001-A | CUMPLE | - |
| P22-CD-09-007-001-A | CUMPLE | - |
| P22-LI-09-007-001-A | CUMPLE | - |
| P22-ET-09-000-01 | **PARCIAL** | Correlativo 2 digitos (debe ser 001), sin revision |
| P22-ET-09-007-001-A | CUMPLE | - |
| P22-ET-09-008-001-A | CUMPLE | - |
| P22-ITEM-09-009-001-A | **NO CUMPLE** | "ITEM" no existe en Tabla 2-2 |
| P22-ITEM-09-009-002-A | **NO CUMPLE** | "ITEM" no existe en Tabla 2-2 |
| P22-ITEM-09-009-003-A | **NO CUMPLE** | "ITEM" no existe en Tabla 2-2 |
| P22-ITEM-09-009-004-A | **NO CUMPLE** | "ITEM" no existe en Tabla 2-2 |
| P22-ET-09-006-001-A | CUMPLE | - |
| P22-ET-09-006-002-A | CUMPLE | - |

### 10.4 Incumplimientos de Codificacion

| # | Codigo Actual | Incumplimiento | Referencia Exacta | Codigo Correcto |
|---|---------------|----------------|-------------------|-----------------|
| 1 | P22-ITEM-09-009-001-A | Tipo "ITEM" no definido | **P00-IT-00-000-101, Seccion 2.1.2, Tabla 2-2** | P22-ET-09-009-001-A |
| 2 | P22-ITEM-09-009-002-A | Tipo "ITEM" no definido | **P00-IT-00-000-101, Seccion 2.1.2, Tabla 2-2** | P22-ET-09-009-002-A |
| 3 | P22-ITEM-09-009-003-A | Tipo "ITEM" no definido | **P00-IT-00-000-101, Seccion 2.1.2, Tabla 2-2** | P22-ET-09-009-003-A |
| 4 | P22-ITEM-09-009-004-A | Tipo "ITEM" no definido | **P00-IT-00-000-101, Seccion 2.1.2, Tabla 2-2** | P22-ET-09-009-004-A |
| 5 | P22-ET-09-000-01 | Correlativo 2 digitos, sin revision | **P00-IT-00-000-101, Seccion 2.1.5** | P22-ET-09-000-001-A |

---

## 11. VEREDICTO POR DOCUMENTO

### 11.1 Tabla de Veredictos

**Response Codes:** 1=Approved, 2=Approved as noted, 3=To be revised as noted, 4=Rejected

| # | Codigo | Descripcion | Tecnico | Codificacion | **VEREDICTO** |
|---|--------|-------------|---------|--------------|---------------|
| 1 | P22-ET-09-000-01 | DS Container | ❌ 4 | ❌ 4 | ❌ **4 - Rejected** |
| 2 | P22-ITEM-09-009-001-A | DS UHPRO System | ✅ 1 | ❌ 4 | ⚠️ **3 - To be revised** |
| 3 | P22-ITEM-09-009-002-A | DS RO HP Pump | ❌ 4 | ❌ 4 | ❌ **4 - Rejected** |
| 4 | P22-ITEM-09-009-003-A | DS CIP Pump | ❌ 4 | ❌ 4 | ❌ **4 - Rejected** |
| 5 | P22-ITEM-09-009-004-A | DS Antiscalant Pump | ⚠️ 2 | ❌ 4 | ⚠️ **2 - Approved as noted** |
| 6 | P22-ET-09-006-001-A | Piping Specifications | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |
| 7 | P22-ET-09-006-002-A | Painting Specifications | ⚠️ 2 | ✅ 1 | ⚠️ **2 - Approved as noted** |
| 8 | P22-ET-09-007-001-A | DS Electrical Aux | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |
| 9 | P22-ET-09-008-001-A | DS PLC & HMI | ⚠️ 2 | ✅ 1 | ⚠️ **2 - Approved as noted** |
| 10 | P22-LI-09-007-001-A | Electrical Load List | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |
| 11 | P22-CD-09-007-001-A | Single Line Diagram | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |
| 12 | P22-CD-09-009-001-A | Process Calculation | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |
| 13 | P22-DWG-09-009-001-A | PFD | ✅ 1 | ✅ 1 | ✅ **1 - Approved** |

### 11.2 Detalle de Comentarios por Documento

| # | Codigo | Comentario Tecnico | Comentario Codificacion |
|---|--------|-------------------|-------------------------|
| 1 | P22-ET-09-000-01 | 5 incumplimientos: puertas (peatonal, equipos, emergencia, corrediza), rejilla PRFV | Correlativo 2 digitos, sin revision → P22-ET-09-000-001-A |
| 2 | P22-ITEM-09-009-001-A | Sin observaciones tecnicas | Cambiar "ITEM" por "ET" → P22-ET-09-009-001-A |
| 3 | P22-ITEM-09-009-002-A | Material "Duplex" vs "Super Duplex", RTDs no mencionados | Cambiar "ITEM" por "ET" → P22-ET-09-009-002-A |
| 4 | P22-ITEM-09-009-003-A | Arranque VFD vs Partida directa, RTDs no mencionados | Cambiar "ITEM" por "ET" → P22-ET-09-009-003-A |
| 5 | P22-ITEM-09-009-004-A | Verificar tipo Membrana y marca | Cambiar "ITEM" por "ET" → P22-ET-09-009-004-A |
| 6 | P22-ET-09-006-001-A | Sin observaciones | Sin observaciones |
| 7 | P22-ET-09-006-002-A | Verificar sistema pintura completo (SSPC-SP10, espesores, RAL 5012) | Sin observaciones |
| 8 | P22-ET-09-007-001-A | Sin observaciones | Sin observaciones |
| 9 | P22-ET-09-008-001-A | Verificar disponibilidad Modbus TCP/RTU | Sin observaciones |
| 10 | P22-LI-09-007-001-A | Sin observaciones | Sin observaciones |
| 11 | P22-CD-09-007-001-A | Sin observaciones | Sin observaciones |
| 12 | P22-CD-09-009-001-A | Sin observaciones | Sin observaciones |
| 13 | P22-DWG-09-009-001-A | Sin observaciones | Sin observaciones |

### 11.3 Estadisticas

| Metrica | Valor |
|---------|-------|
| Total documentos | 13 |
| **1 - Approved** | 6 (46%) |
| **2 - Approved as noted** | 3 (23%) |
| **3 - To be revised** | 1 (8%) |
| **4 - Rejected** | 3 (23%) |

### 11.4 Resumen por Categoria

| Categoria | Cumple | Verificar | No Cumple/Falta Info |
|-----------|--------|-----------|----------------------|
| Contenedor | 2 | 1 | **5** |
| Bomba HP | 5 | 2 | **1** |
| Bomba CIP | 1 | 4 | **2** |
| Bomba Dosif. | 0 | 2 | 0 |
| UHPRO System | 8 | 0 | 0 |
| Piping | 7 | 0 | 0 |
| Pintura | 0 | 6 | 0 |
| PLC/HMI | 2 | 1 | 1 |
| Load List | 3 | 0 | 0 |
| Codificacion | 8 | 0 | **5** |
| **TOTAL** | **36** | **16** | **14** |

---

## 12. LISTA CONSOLIDADA DE INCUMPLIMIENTOS

### 12.1 Incumplimientos ET P22-ET-09-000-001-0

| # | Equipo | Incumplimiento | Seccion ET | Pagina |
|---|--------|----------------|------------|--------|
| 1 | Contenedor | Puerta acceso peatonal 900x2200mm no especificada | 5.1.10 | 15 |
| 2 | Contenedor | Puerta acceso equipos apertura 110° no especificada | 5.1.10 | 15 |
| 3 | Contenedor | Puerta emergencia no especificada | 5.1.10 | 15 |
| 4 | Contenedor | Puerta corrediza lateral no especificada | 5.1.10 | 15 |
| 5 | Contenedor | Rejilla PRFV antideslizante no especificada | 5.1.10 | 15 |
| 6 | Bomba HP | Material "Duplex" vs "Super Duplex" requerido | 5.1.1 | 10 |
| 7 | Bomba HP | RTDs 3 hilos rodamientos no mencionados | 5.1.1 | 10 |
| 8 | Bomba CIP | Tipo arranque VFD vs "Partida directa" requerida | 5.1.4 | 12 |
| 9 | Bomba CIP | RTDs 3 hilos rodamientos no mencionados | 5.1.4 | 12 |

### 12.2 Incumplimientos P00-IT-00-000-101

| # | Documento | Incumplimiento | Seccion | Tabla |
|---|-----------|----------------|---------|-------|
| 1 | P22-ITEM-09-009-001-A | Tipo "ITEM" no existe | 2.1.2 | 2-2 |
| 2 | P22-ITEM-09-009-002-A | Tipo "ITEM" no existe | 2.1.2 | 2-2 |
| 3 | P22-ITEM-09-009-003-A | Tipo "ITEM" no existe | 2.1.2 | 2-2 |
| 4 | P22-ITEM-09-009-004-A | Tipo "ITEM" no existe | 2.1.2 | 2-2 |
| 5 | P22-ET-09-000-01 | Correlativo debe ser 3 digitos | 2.1.5 | - |

---

## 13. ACCIONES REQUERIDAS

| # | Accion | Referencia Incumplimiento | Responsable | Prioridad |
|---|--------|---------------------------|-------------|-----------|
| 1 | Entregar datasheet especifico del contenedor con modificaciones segun ET 5.1.10 | ET 5.1.10, pag.15 | BW Water | **ALTA** |
| 2 | Aclarar nomenclatura material bomba HP: "Duplex" vs "Super Duplex" | ET 5.1.1, pag.10 | BW Water | **ALTA** |
| 3 | Confirmar inclusion RTDs 3 hilos en bombas HP y CIP | ET 5.1.1 y 5.1.4 | BW Water | **MEDIA** |
| 4 | Justificar cambio de arranque bomba CIP (VFD vs Partida directa) | ET 5.1.4, pag.12 | BW Water | **MEDIA** |
| 5 | Corregir codificacion de 5 documentos segun P00-IT-00-000-101 | P00-IT-00-000-101, Tabla 2-2 | BW Water | **ALTA** |
| 6 | Entregar detalle esquema de pintura segun ET 5.1.9 | ET 5.1.9, pag.13-14 | BW Water | **BAJA** |
| 7 | Confirmar disponibilidad protocolo Modbus en PLC | ET Seccion 5 | BW Water | **MEDIA** |

---

## 14. VEREDICTO

### 14.1 Veredicto Tecnico

# ❌ 4 - REJECTED

Los documentos presentan **9 incumplimientos tecnicos** respecto a la Especificacion Tecnica P22-ET-09-000-001-0:

| # | Equipo | Incumplimiento | Seccion ET |
|---|--------|----------------|------------|
| 1 | Contenedor | Puerta acceso peatonal no especificada | 5.1.10 |
| 2 | Contenedor | Puerta acceso equipos no especificada | 5.1.10 |
| 3 | Contenedor | Puerta emergencia no especificada | 5.1.10 |
| 4 | Contenedor | Puerta corrediza lateral no especificada | 5.1.10 |
| 5 | Contenedor | Rejilla PRFV antideslizante no especificada | 5.1.10 |
| 6 | Bomba HP | Material "Duplex" vs "Super Duplex" requerido | 5.1.1 |
| 7 | Bomba HP | RTDs 3 hilos no mencionados | 5.1.1 |
| 8 | Bomba CIP | Tipo arranque VFD vs "Partida directa" | 5.1.4 |
| 9 | Bomba CIP | RTDs 3 hilos no mencionados | 5.1.4 |

### 14.2 Veredicto Codificacion

# ❌ 4 - REJECTED

Los documentos presentan **5 incumplimientos de codificacion** respecto a P00-IT-00-000-101:

| # | Documento | Incumplimiento |
|---|-----------|----------------|
| 1 | P22-ITEM-09-009-001-A | Tipo "ITEM" no existe en Tabla 2-2 |
| 2 | P22-ITEM-09-009-002-A | Tipo "ITEM" no existe en Tabla 2-2 |
| 3 | P22-ITEM-09-009-003-A | Tipo "ITEM" no existe en Tabla 2-2 |
| 4 | P22-ITEM-09-009-004-A | Tipo "ITEM" no existe en Tabla 2-2 |
| 5 | P22-ET-09-000-01 | Correlativo 2 digitos, sin revision |

### 14.3 Veredicto Consolidado

# ❌ 4 - REJECTED

**Total: 14 incumplimientos** (9 tecnicos + 5 codificacion)

Los documentos requieren correccion y re-envio antes de su aprobacion

---

*Revision preparada por: Claude Code*
*Fecha: 10 de diciembre de 2025 (actualizado 16 de diciembre de 2025)*

---

## DOCUMENTOS DE REFERENCIA

- **Oferta Tecnica vigente:** `OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md` (Rev.1)
- **Especificacion Tecnica:** `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md`
- **Codificacion:** `BASES TECNICAS/md/P00-IT-00-000-101-CODIFICACION-GENERAL.md`
