---
titulo: "COMPILADO REVISION TECNICA N4"
subtitulo: "Second Stage RO Brine Module - Entregas 10, 11"
codigo: "P22-TM-09-000-004-0"
version: "BORRADOR v1.0"
autor: "ADASA + Asesor Van Doorn"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Pendiente Asesor LH Van Doorn"
aprobado_por: "Pendiente"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# COMPILADO DE REVISION TECNICA N4 - ADASA

**Fecha:** 03 de febrero de 2026
**Proyecto:** BAE 12803 - Modulo de Salmuera Taltal
**Revision:** ADASA + Pendiente Asesor Van Doorn
**Estado:** BORRADOR - Pendiente comentarios Van Doorn

---

## 1. INFORMACION GENERAL

| Campo | Valor |
|-------|-------|
| **Transmittal Code** | P22-TM-09-000-004-0 |
| **Submittal 0010** | 25007-0010 (30-Ene-2026) - 2 documentos |
| **Submittal 0011** | 25007-0011 (03-Feb-2026) - 2 documentos |
| **Total documentos** | 4 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised, 4=Rejected, 5=For Information |

---

## 2. RESUMEN EJECUTIVO

### 2.1 Veredicto por Entrega

| Entrega | Submittal | Documentos | Veredicto | Motivo |
|---------|-----------|------------|-----------|--------|
| E10 | 25007-0010 | 2 | **3 - To be revised** | PLC 60Hz, A/C sin n+1 (29 dias pendiente) |
| E11 | 25007-0011 | 2 | **3 - To be revised** | TAG duplicado FIT-09-001, faltan instrumentos ET |

### 2.2 Veredicto Final Transmittal N4

| Campo | Valor |
|-------|-------|
| **VEREDICTO FINAL** | **3 - TO BE REVISED** |
| **Motivo Principal E10** | PLC especificado 60Hz viola ET 5.4.7; A/C sin n+1 viola ET 5.1.11 (29 dias sin resolver) |
| **Motivo Principal E11** | Cable Tray Layout hereda TAG duplicado FIT-09-001; faltan transmisores vibracion y Pt-100 motores |

### 2.3 Observaciones CRITICAS

| ID | Documento | Observacion | Severidad | Dias Pendiente |
|----|-----------|-------------|-----------|----------------|
| **OBS-E10-01** | Utility Consumption List | PLC especificado a 60 Hz. ET 5.4.7 prohibe equipos que operen en frecuencias distintas a 50 Hz. | **CRITICA** | Nueva |
| **OBS-E10-02** | Utility Consumption List | A/C sin configuracion n+1. Solo 1 unidad (2.64 kW) vs 2 requeridas por ET 5.1.11 y Oferta (5.28 kW). | **CRITICA** | 29 (TM N2) |
| **OBS-E10-03** | Documento faltante | Memoria de calculo termica A/C no entregada. Requerida por ET 5.1.11 L757-759. | **CRITICA** | 29 (TM N2) |
| **OBS-E11-01** | Control Architecture | Modbus TCP Memory Map no entregado. BW comprometio entrega separada hace 38 dias (TM N2). | **CRITICA** | 38 (TM N2) |
| **OBS-E11-02** | Cable Tray Layout | TAG duplicado FIT-09-001 en Items 4 y 13. Dos instrumentos diferentes con mismo TAG. | **CRITICA** | 7 (TM N3) |
| **OBS-E11-03** | Cable Tray Layout | Faltan ubicaciones transmisores vibracion para HP Pump y Turbochargers per ET 5.5.7. | **CRITICA** | 7 (TM N3) |
| **OBS-E11-04** | Cable Tray Layout | Faltan ubicaciones sensores Pt-100 motores para HP Pump y CIP Pump per ET 5.3. | **CRITICA** | 7 (TM N3) |

---

## 3. DOCUMENTOS REVISADOS (4 total)

### 3.1 Entrega 10 - Submittal 25007-0010 (2 documentos)

| # | Codigo | Titulo | Rev | Veredicto |
|---|--------|--------|-----|-----------|
| 1 | P22-LI-09-009-001-A | Utility Consumption List | A | **3 - To be revised** |
| 2 | P22-ET-09-009-010-B | Datasheet of Antiscalant Dosing Tank | B | **2 - Approved as noted** |

**Estadisticas E10:** 0 Approved, 1 Approved as noted, 1 To be revised, 0 Rejected

### 3.2 Entrega 11 - Submittal 25007-0011 (2 documentos)

| # | Codigo | Titulo | Rev | Veredicto |
|---|--------|--------|-----|-----------|
| 1 | P22-CD-09-004-001-B | Control System Architecture | B | **2 - Approved as noted** |
| 2 | P22-DWG-09-007-004-A | Cable Tray Layout and Support Details | A | **3 - To be revised** |

**Estadisticas E11:** 0 Approved, 1 Approved as noted, 1 To be revised, 0 Rejected

---

## 4. OBSERVACIONES ADASA - ENTREGA 10

### 4.1 Utility Consumption List (P22-LI-09-009-001-A) - TO BE REVISED

| # | Observacion | Severidad | Referencia |
|---|-------------|-----------|------------|
| OBS-E10-01 | **PLC a 60 Hz:** Utility List indica alimentacion PLC como "220V/1PH/60Hz". ET 5.4.7 establece que no se aceptaran equipos que operen en frecuencias distintas a 50 Hz. Sistema electrico chileno opera a 50 Hz. | **CRITICA** | ET 5.4.7 L1305-1308 |
| OBS-E10-02 | **A/C sin n+1:** Solo 1 unidad A/C (2.64 kW). ET 5.1.11 requiere n+1 (minimo 2). Oferta Rev.1 comprometio "2 A/C (1W+1S)" con 5.28 kW total. Observacion levantada TM N2 hace 29 dias. | **CRITICA** | ET 5.1.11, Oferta Sec 4 |
| OBS-E10-03 | **Falta memoria calculo termica:** ET 5.1.11 L757-759 requiere documento de calculo termico para A/C. No ha sido entregado. Observacion levantada TM N2 hace 29 dias. | **CRITICA** | ET 5.1.11 L757-759 |
| OBS-E10-04 | **Discrepancia HP Pump:** 4 valores diferentes: 93 kW (Utility), 86 kW (Oferta), 92 kW (Equipment List), 83 kW (Load List). Afecta calculos SEC y dimensionamiento electrico. | **MAYOR** | Multiple docs |
| OBS-E10-05 | **Discrepancia CIP Pump:** 11 kW (Utility) vs 15 kW (Oferta). Diferencia de 27% requiere clarificacion. | **MAYOR** | Oferta Rev.1 |

**Aspectos Positivos E10:**
- SEC = 3.98 kWh/m3 cumple garantia 4.71 kWh/m3 con margen favorable 15%
- Produccion 21 m3/h cumple requisito minimo 20 m3/h
- HP Pump, CIP Pump, CIP Heater, Dosing Pump todos especificados a 50 Hz

### 4.2 Antiscalant Dosing Tank (P22-ET-09-009-010-B) - APPROVED AS NOTED

| # | Observacion | Severidad | Referencia |
|---|-------------|-----------|------------|
| OBS-E10-06 | **Capacidad P&ID vs Datasheet:** P&ID indica 0.25 m3, Datasheet indica 0.34 m3 total / 0.27 m3 efectivo. Actualizar P&ID en proxima revision. | Menor | P&ID E3 |

**Cambio de Material ACEPTADO:**
- Material: HDPE -> LMDPE (justificado por limitaciones dimensionales)
- Capacidad: 246 L (Oferta) -> 340 L (Datasheet) - EXCEDE requisito
- Compatibilidad quimica con antiincrustante (pH > 10) confirmada

---

## 5. OBSERVACIONES ADASA - ENTREGA 11

### 5.1 Control System Architecture (P22-CD-09-004-001-B) - APPROVED AS NOTED

| # | Observacion | Severidad | Referencia |
|---|-------------|-----------|------------|
| OBS-E11-01 | **Modbus TCP Memory Map no entregado:** BW comprometio "WILL SUBMIT I/O MODBUS LIST SEPARATELY" en respuesta a comentario TM N2 (26-Ene-2026). Han transcurrido 38 dias y el documento NO ha sido entregado. Critico para integracion DCS. | **CRITICA** | TM N2 OBS-08 |
| OBS-E11-05 | **UPS no incluida en BOM:** ET 5.4 L1088-1089 requiere UPS con autonomia minima 8 horas para sistema de control. El BOM no incluye este item. | **MAYOR** | ET 5.4 L1088-1089 |
| OBS-E11-06 | **VFD fieldbus no especificado:** Diagrama muestra conexion CAT6/Ethernet a VFDs pero no especifica protocolo ni variables disponibles via SCADA. | **MAYOR** | TM N2 OBS-09 |

**Aspectos Positivos E11 - Control Architecture:**
- PLC Allen Bradley 5069-L320ER: CUMPLE ET 5.4
- HMI PanelView Plus 7 10" Color Touch: CUMPLE ET 5.4
- Gateway Modbus PLX32-EIP-MBTCP: CUMPLE ET 5.4
- Switch Ethernet Stratix 2100 8 puertos: EXCEDE requisito 5 puertos
- Software licenciado: Studio 5000 V37 + FactoryTalk View V15
- Laptop ingenieria: Dell Latitude 3450 incluida
- Power Meter: Clarificado - Digital Power Meter con Modbus TCP/IP

### 5.2 Cable Tray Layout (P22-DWG-09-007-004-A) - TO BE REVISED

| # | Observacion | Severidad | Referencia |
|---|-------------|-----------|------------|
| **OBS-E11-02** | **TAG duplicado FIT-09-001:** Items 4 y 13 del Instrument Location Schedule tienen el mismo TAG para instrumentos diferentes (Item 4: Cartridge Filter DN100, Item 13: 2nd Stage Permeate DN50). Hace imposible direccionamiento PLC. | **CRITICA** | TM N3 OBS-02 |
| **OBS-E11-03** | **Faltan transmisores vibracion:** Layout no incluye ubicaciones para VT en HP Pump (BH-09-001), Feed Turbo (SIP-09-001), Interstage Turbo (SIP-09-002). Requeridos por ET 5.5.7. | **CRITICA** | ET 5.5.7, TM N3 |
| **OBS-E11-04** | **Faltan Pt-100 motores:** Layout no incluye ubicaciones para sensores temperatura en HP Pump (87 kW) y CIP Pump (15 kW) - devanados y rodamientos. Requeridos por ET 5.3. | **CRITICA** | ET 5.3, TM N3 |
| OBS-E11-07 | **Discrepancia LIT TAG:** Layout usa LIT-09-001, IO List usa LIT-09-002 para CIP Tank Level. Unificar. | **MAYOR** | TM N3 |

**Aspectos Positivos E11 - Cable Tray Layout:**
- Material: Steel Hot Dip Galvanized - CUMPLE
- Fill maximo 80%: Declarado - CUMPLE
- Dimensiones minimas 50x50mm: Todas bandejas >= 100x100mm - EXCEDE
- 32 instrumentos documentados con ubicaciones
- 10 paneles electricos documentados con TAGs

---

## 6. [PENDIENTE] OBSERVACIONES ASESOR VAN DOORN

> **NOTA:** Esta seccion se completara una vez recibidos los comentarios del Asesor Van Doorn.

### 6.1 Entrega 10

*Pendiente revision Van Doorn*

### 6.2 Entrega 11

*Pendiente revision Van Doorn*

---

## 7. ESTADISTICAS CONSOLIDADAS

### 7.1 Estados Finales por Entrega

| Veredicto | E10 | E11 | Total | % |
|-----------|-----|-----|-------|---|
| **1 - Approved** | 0 | 0 | **0** | 0% |
| **2 - Approved as noted** | 1 | 1 | **2** | 50% |
| **3 - To be revised** | 1 | 1 | **2** | 50% |
| **4 - Rejected** | 0 | 0 | **0** | 0% |
| **Total** | 2 | 2 | **4** | 100% |

### 7.2 Observaciones Pendientes de Transmittales Anteriores

| Transmittal | Fecha Original | Dias Pendiente | Observaciones Criticas |
|-------------|---------------|----------------|------------------------|
| TM N2 | 26-Ene-2026 | **29** | A/C n+1, A/C calculo termico, Static Mixer material, Modbus TCP Map |
| TM N3 | 28-Ene-2026 | **7** | FIT-09-001 duplicate, Vibracion, Pt-100, VM-09-015, VFD variables, DO/DI |

### 7.3 Resumen de Observaciones por Severidad

| Severidad | E10 | E11 | Total |
|-----------|-----|-----|-------|
| **CRITICA** | 3 | 4 | **7** |
| **MAYOR** | 2 | 3 | **5** |
| **MENOR** | 1 | 0 | **1** |
| **Total** | 6 | 7 | **13** |

---

## 8. ACCIONES REQUERIDAS BW WATER

### 8.1 Acciones Criticas (Prioridad ALTA)

| # | Accion | Documento | Plazo | Referencia |
|---|--------|-----------|-------|------------|
| 1 | **Confirmar frecuencia PLC:** Si dual-frequency (50/60 Hz), documentar explicitamente. Si solo 60 Hz, reemplazar equipo. | P22-LI-09-009-001-A | Inmediato | OBS-E10-01 |
| 2 | **Incluir 2da unidad A/C:** Configuracion n+1 segun ET 5.1.11 y Oferta Rev.1. Actualizar Utility List y Load List. | P22-LI-09-009-001-A | Inmediato | OBS-E10-02 |
| 3 | **Entregar memoria calculo termica A/C:** Considerar TODAS las cargas (equipos, iluminacion, transmision paredes, radiacion solar). | Nuevo documento | Inmediato | OBS-E10-03 |
| 4 | **URGENTE: Entregar Modbus TCP Memory Map:** Documento pendiente 38 dias, critico para integracion DCS. | Nuevo documento | Inmediato | OBS-E11-01 |
| 5 | **Corregir TAG duplicado FIT-09-001:** Renumerar Item 13 como FIT-09-002 en Instrument List y actualizar Layout. | P22-LI-09-008-003 + P22-DWG-09-007-004 | Inmediato | OBS-E11-02 |
| 6 | **Incluir transmisores vibracion:** Agregar en Instrument List y Layout para HP Pump, Feed Turbo, Interstage Turbo. | P22-LI-09-008-003 + P22-DWG-09-007-004 | Inmediato | OBS-E11-03 |
| 7 | **Incluir sensores Pt-100 motores:** Documentar para HP Pump (87 kW) y CIP Pump (15 kW) - devanados y rodamientos. | Datasheets + Layout | Inmediato | OBS-E11-04 |

### 8.2 Acciones Mayores (Prioridad MEDIA)

| # | Accion | Documento | Plazo | Referencia |
|---|--------|-----------|-------|------------|
| 8 | **Unificar potencia HP Pump:** Determinar valor correcto y actualizar TODOS los documentos. | Multiple | Proxima revision | OBS-E10-04 |
| 9 | **Clarificar potencia CIP Pump:** Confirmar 11 kW vs 15 kW y actualizar. | P22-LI-09-009-001-A | Proxima revision | OBS-E10-05 |
| 10 | **Incluir UPS en BOM:** Control Architecture debe incluir UPS con 8 horas autonomia. | P22-CD-09-004-001 | Proxima revision | OBS-E11-05 |
| 11 | **Especificar VFD fieldbus:** Documentar protocolo y variables electricas disponibles via SCADA. | P22-CD-09-004-001 | Proxima revision | OBS-E11-06 |
| 12 | **Unificar TAG LIT:** Decidir LIT-09-001 o LIT-09-002 para CIP Tank Level. | IL + IO List + Layout | Proxima revision | OBS-E11-07 |

### 8.3 Acciones Menores (Prioridad BAJA)

| # | Accion | Documento | Plazo | Referencia |
|---|--------|-----------|-------|------------|
| 13 | **Actualizar capacidad Antiscalant Tank en P&ID:** Cambiar de 0.25 m3 a 0.34 m3. | P22-DWG-09-009-002 | Proxima emision | OBS-E10-06 |
| 14 | **Clarificar capacidad bomba dosificadora:** Resolver discrepancia 1 vs 2.3 LPH. | P&ID / Equipment List | Proxima emision | Cross-ref |

---

## 9. REFERENCIAS

### 9.1 Documentos Fuente

| Entrega | Archivo | Version |
|---------|---------|---------|
| E10 | REVISIONES/SUBMITTALS/25007-0010/2026-02-02_Revision-Tecnica-Entrega-10.md | v2.0 |
| E11 | REVISIONES/SUBMITTALS/25007-0011/2026-02-03_Revision-Tecnica-Entrega-11.md | v1.0 |

### 9.2 Documentos de Referencia

| Documento | Ubicacion |
|-----------|-----------|
| ET Modulo | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md |
| Oferta Tecnica Rev.1 | OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md |
| Codificacion General | BASES TECNICAS/md/P00-IT-00-000-101-CODIFICACION-GENERAL.md |
| Transmittal N2 | REVISIONES/TRANSMITTALES/P22-TM-09-000-002-0/P22-TM-09-000-002-0_TRANSMITTAL.md |
| Transmittal N3 | REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/P22-TM-09-000-003-0_TRANSMITTAL.md |

### 9.3 Documentos E10 Revisados

| Documento | Ubicacion |
|-----------|-----------|
| Utility Consumption List | ENTREGAS_BWWATER/ENTREGA 10/md/ |
| Antiscalant Tank DS | ENTREGAS_BWWATER/ENTREGA 10/md/ |

### 9.4 Documentos E11 Revisados

| Documento | Ubicacion |
|-----------|-----------|
| Control Architecture Rev.B | ENTREGAS_BWWATER/ENTREGA 11/md/P22-CD-09-004-001_CONTROL_ARCHITECTURE_REVB.md |
| Cable Tray Layout | ENTREGAS_BWWATER/ENTREGA 11/md/P22-DWG-09-007-004_Cable_Tray_Layout.md |
| CCS Control Architecture | ENTREGAS_BWWATER/ENTREGA 11/md/P22-CD-09-004-001_CONTROL_ARCHITECTURE_CCS.md |

---

*Compilado preparado por: ADASA*
*Fecha: 03 de febrero de 2026*
*Estado: BORRADOR v1.0 - Pendiente comentarios Asesor Van Doorn*
*Contrato: C-4300 BW Water - BAE 12803*
