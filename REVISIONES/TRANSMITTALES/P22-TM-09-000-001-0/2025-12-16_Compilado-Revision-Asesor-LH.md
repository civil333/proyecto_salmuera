# COMPILADO DE REVISION TECNICA - ADASA

**Fecha:** 16 de diciembre de 2025
**Proyecto:** BAE 12803 - Modulo de Salmuera Taltal
**Revision:** ADASA

---

## 1. INFORMACION GENERAL

| Campo | Valor |
|-------|-------|
| **Submittal 0001** | 25007-0001 (09-Dic-2025) - 13 documentos |
| **Submittal 0002** | 25007-0002 (15-Dic-2025) - 7 documentos |
| **Total documentos** | 20 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised as noted, 4=Rejected, 5=For Information |

---

## 2. RESUMEN EJECUTIVO

### 2.1 Estadisticas por Submittal

**Submittal 25007-0001 (Entrega 1):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 1 - Approved | 3 | 23% |
| 2 - Approved as noted | 2 | 15% |
| 3 - To be revised as noted | 1 | 8% |
| 4 - Rejected | 3 | 23% |
| Sin respuesta | 4 | 31% |

**Submittal 25007-0002 (Entrega 2):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 1 - Approved | 3 | 43% |
| 4 - Rejected | 4 | 57% |

### 2.2 Observaciones Criticas

| # | Observacion | Documento | Gravedad |
|---|-------------|-----------|----------|
| 1 | **GRAVE**: Falta modelacion de turbochargers para verificar bomba HP y ERDs | Process Calculation | **CRITICA** |
| 2 | **IMPORTANTE**: Presiones de diseno reducidas vs oferta (10% margen → ~4%) | PFD, Turbochargers | **ALTA** |
| 3 | **CAMBIO DE ALCANCE:** Oferta técnica especifica membranas LG SW 400 R G2 **UHP en ambas etapas** (70 uds). Ahora proponen: Etapa 1 con membranas **convencionales** LG SW 400 SR (42 uds) + Etapa 2 con UHP (28 uds). Similar situación con vessels (todos 1800 PSI en oferta). Técnicamente aceptable, pero genera **delta económico a favor de ADASA** (membranas convencionales cuestan 2-3x menos). Solicitar ajuste de precio. | UHPRO System, Process Calc | **MEDIA** (requiere ajuste económico) |
| 4 | Acople Victaulic 2000 PSI no verificable | Piping Specifications | **MEDIA** |

---

## 3. TABLA CONSOLIDADA POR DOCUMENTO

### 3.1 Entrega 1 - Submittal 25007-0001

| # | Codigo | Descripcion | Comentarios | **Estado Final** |
|---|--------|-------------|-------------|------------------|
| 1 | P22-ET-09-000-01 | DS Container | 5 incumplimientos puertas/rejilla, codificacion 2 digitos | **4 - Rejected** |
| 2 | P22-DWG-09-009-001 | PFD | Presiones reducidas vs oferta (10%→4%), indicar TAGs y presion tie-in N1 | **4 - Rejected** |
| 3 | P22-CD-09-007-001 | Single Line Diagram | - | **1 - Approved** |
| 4 | P22-CD-09-009-001 | Process Calculation | **GRAVE:** Falta modelacion turbochargers para verificar bomba HP y ERDs | **4 - Rejected** |
| 5 | P22-ITEM-09-009-001 | DS UHPRO System | Indicar cantidades membranas/vessels por etapa. Cambiar ITEM->ET | **3 - To be revised** |
| 6 | P22-ITEM-09-009-002 | DS HP Pump | Material Duplex vs Super Duplex, incluir RTDs, IP66, pressure rating Cl900 | **4 - Rejected** |
| 7 | P22-ITEM-09-009-003 | DS CIP Pump | Arranque VFD vs directa, RTDs faltantes, IP66, cambiar ITEM->ET | **4 - Rejected** |
| 8 | P22-ITEM-09-009-004 | DS Antiscalant Pump | Frecuencia debe ser 50 Hz, cambiar ITEM->ET | **2 - Approved as noted** |
| 9 | P22-ET-09-006-001 | Piping Specification | Verificar acople Victaulic 2000 PSI (marca/modelo) | **1 - Approved** |
| 10 | P22-ET-09-006-002 | Painting Specification | Verificar sistema pintura completo | **2 - Approved as noted** |
| 11 | P22-ET-09-008-001 | DS PLC/HMI | Verificar disponibilidad Modbus TCP/RTU | **2 - Approved as noted** |
| 12 | P22-LI-09-007-01 | Electrical Load List | - | **1 - Approved** |
| 13 | P22-ET-09-007-001 | DS Electrical Aux | - | **1 - Approved** |

### 3.2 Entrega 2 - Submittal 25007-0002

| # | Codigo | Descripcion | Comentarios | **Estado Final** |
|---|--------|-------------|-------------|------------------|
| 1 | P22-ITEM-09-009-005 | DS RO Cartridge Filter | Indicar solidos suspendidos, cantidad elementos y area. Cambiar ITEM->ET | **3 - To be revised** |
| 2 | P22-ITEM-09-009-006 | DS CIP Cartridge Filter | Indicar cantidad elementos y area. Cambiar ITEM->ET | **3 - To be revised** |
| 3 | P22-ITEM-09-009-007 | DS Feed Turbocharger | **IMPORTANTE:** Presiones con margen 10% (no 4%), flanges Cl900. Cambiar ITEM->ET | **3 - To be revised** |
| 4 | P22-ITEM-09-009-008 | DS Interstage Turbocharger | Presiones con margen 10%, flanges Cl900 lb. Cambiar ITEM->ET | **3 - To be revised** |
| 5 | P22-ITEM-09-009-009 | DS CIP Tank | Cambiar ITEM->ET | **3 - To be revised** |
| 6 | P22-ITEM-09-009-010 | DS Antiscalant Tank | Cambiar ITEM->ET | **3 - To be revised** |
| 7 | P22-ITEM-09-009-011 | DS CIP Tank Heater | Cambiar ITEM->ET | **3 - To be revised** |

---

## 4. ESTADISTICAS CONSOLIDADAS

### 4.1 Estados Finales Consolidados

| Veredicto | Entrega 1 | Entrega 2 | Total | % |
|-----------|-----------|-----------|-------|---|
| **1 - Approved** | 4 | 0 | 4 | 20% |
| **2 - Approved as noted** | 3 | 0 | 3 | 15% |
| **3 - To be revised** | 1 | 7 | 8 | 40% |
| **4 - Rejected** | 5 | 0 | 5 | 25% |
| **Total** | 13 | 7 | **20** | 100% |

### 4.2 Documentos Rejected (4) - Requieren re-envio

| # | Codigo | Descripcion | Razon Principal |
|---|--------|-------------|-----------------|
| 1 | P22-ET-09-000-01 | DS Container | Puertas/rejilla no especificadas (ET 5.1.10) |
| 2 | P22-DWG-09-009-001 | PFD | Presiones reducidas vs oferta (10%→4%) |
| 3 | P22-CD-09-009-001 | Process Calculation | Falta modelacion turbochargers (GRAVE) |
| 4 | P22-ITEM-09-009-002 | DS HP Pump | Material Duplex vs Super Duplex, RTDs, IP rating |
| 5 | P22-ITEM-09-009-003 | DS CIP Pump | Arranque VFD vs directa, RTDs faltantes |

---

## 5. ACCIONES REQUERIDAS CONSOLIDADAS

### 5.1 Acciones Criticas (Prioridad ALTA)

| # | Accion | Responsable |
|---|--------|-------------|
| 1 | Incluir modelaciones de turbochargers para ambas salinidades | BW Water |
| 2 | Corregir presiones de diseno al 10% de margen (83.9 bar) | BW Water |
| 3 | Redimensionar bomba HP aumentando TDH | BW Water |
| 4 | Entregar DS Container con modificaciones ET 5.1.10 | BW Water |
| 5 | Aclarar material bomba HP: Duplex vs Super Duplex | BW Water |

### 5.2 Acciones Tecnicas (Prioridad MEDIA)

| # | Accion | Responsable |
|---|--------|-------------|
| 6 | Indicar cantidades membranas/vessels por etapa | BW Water |
| 7 | Indicar tasa filtracion y elementos de filtros | BW Water |
| 8 | Especificar marca/modelo acople Victaulic 2000 PSI | BW Water |
| 9 | Especificar flanges Cl 900 lb en turbochargers | BW Water |
| 10 | Confirmar inclusion RTDs 3 hilos en bombas | BW Water |
| 11 | Corregir frecuencia bomba antiscalant a 50 Hz | BW Water |
| 12 | Confirmar IP66 en bomba HP y CIP | BW Water |

### 5.3 Acciones Administrativas (Prioridad BAJA)

| # | Accion | Responsable |
|---|--------|-------------|
| 13 | Corregir codificacion ITEM -> ET (12 documentos) | BW Water |
| 14 | Ajuste economico por membranas convencionales etapa 1 | Administrativo |
| 15 | Verificar disponibilidad Modbus en PLC | BW Water |

---

## 6. DOCUMENTOS PENDIENTES DE ENTREGA

Segun programa BW Water, quedan pendientes:

| # | Documento | Estado |
|---|-----------|--------|
| 1 | Control System Architecture | PENDIENTE |
| 2 | Utility Consumption List | PENDIENTE |
| 3 | Chemical and Consumption List | PENDIENTE |
| 4 | Line List | PENDIENTE |
| 5 | Instrument List | PENDIENTE |
| 6 | Valve List | PENDIENTE |
| 7 | DS MCC | PENDIENTE |
| 8 | A/C Thermal Calculation | PENDIENTE |

---

*Compilado preparado por: ADASA*
*Fecha: 16 de diciembre de 2025*
