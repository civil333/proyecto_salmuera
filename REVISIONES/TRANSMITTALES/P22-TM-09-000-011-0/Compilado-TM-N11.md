---
tipo: Compilado Interno — Análisis Técnico TM N11
transmittal: P22-TM-09-000-011-0
entregas: E19 (25007-0019) / E20 (25007-0020) / E21 (25007-0021)
fecha: 17-Mar-2026
nota: DOCUMENTO INTERNO — NO ENVIAR A BW WATER
---

# COMPILADO TÉCNICO — TM N11
## Análisis por Documento — Entregas 19, 20 y 21
## **NO ENVIAR — USO INTERNO ADASA**

---

## 1. Contexto General

TM N10 (16-Mar-2026) revisó 6 documentos de Entrega 18, emitido con Code 3 (TO BE REVISED).
TM N11 cubre las Entregas 19, 20 y 21 (recibidas 13–16 Mar 2026) con 10 documentos.

**Veredicto Global TM N11: 3 — TO BE REVISED**
La Valve List Rev C introduce 2 nuevos TAGs duplicados (VE-09-007 y PSV-09-002), constituyendo fallos de QA críticos que requieren corrección antes de que el documento pueda usarse para SCADA y finalización del P&ID.

**Estado de cierres importantes:**
- TM N6 OBS-01 (coupling pressure turbochargers): **CERRADO** en esta entrega para ambos turbochargers (Style S, 1800 psi) y HP Pump (Style H, 2000 psi)
- TM N10 OBS-06 (vibración SIP-09-001): **CERRADO** — "vibration sensor mounting surface" confirmado en Datasheet Rev D item 38
- TM N10 OBS-07 (vibración SIP-09-002): **CERRADO** — idem
- TM N10 OBS-05 (Antiscalant Tank GA anchor data): **PARCIAL** — Equipment List Rev B provee material (LPMD) y volumen (0.27 m³ efectivo), pero GA Rev B con datos sísmicos y anchor layout sigue pendiente

---

## 2. Valve List Rev C — P22-LI-09-005-002

**Veredicto: 3 — To be Revised**
**CCS referenciado:** Submittal 6/3/2026 (fecha en CCS)

### 2.1 CCS — 3 ítems

| Item | Observación ADASA | Respuesta BW | Veredicto |
|------|-------------------|--------------|-----------|
| 1 | VM-09-015, VE-09-008, VE-09-009, VM-09-065 duplicados | "Noted, Already revised on Valve List Rev. C" | VERIFICAR en documento |
| 2 | Todos los TAGs deben ser únicos | "Noted, All Valves have unique TAGs on Rev. C" | VERIFICAR en documento |
| 3 | VM-09-015 item 18: ON/OFF MOTORIZED contradice OBS-11 WITHDRAWN | "Noted, Already revised on Valve List Rev. C" | VERIFICAR en documento |

### 2.2 Verificación en documento (Valve List Rev C, ítems 1–112)

**4 duplicados originales de TM N6 OBS-01:**
- VM-09-015: Item 18 → renombrado a **VM-09-151** (DN100, Butterfly, MANUAL) ✓; Item 43 → VM-09-015 (DN15, Ball, MANUAL) ✓ — DUPLICADO RESUELTO
- VE-09-008: Solo ítem 57 (DN80, ANSI 150#, Permeate 1st) — DUPLICADO RESUELTO ✓
- VE-09-009: Solo ítem 58 (DN80, ANSI 900#, 2nd Stage Reject) — DUPLICADO RESUELTO ✓
- VM-09-065: Solo ítem 77 (DN150, CIP, PVC) — DUPLICADO RESUELTO ✓
- VM-09-151 (item 18): MANUALLY ACTUATED VALVE / MANUAL/HAND ✓ — consistente con OBS-11 WITHDRAWN

**Nuevos duplicados introducidos en Rev C:**
- **VE-09-007**: Item 44 (DN80, ANSI 900#, CE3MN, SWRO REJECT 1ST) Y Item 64 (DN80, ANSI 900#, CE3MN, 1ST STAGE REJECT TO 2ND STAGE) — NUEVO DUPLICADO CRÍTICO ⚠️
- **PSV-09-002**: Item 105 (ANTISCALANT, Valve Series No. 2) Y Item 112 (RO PERMEATE, Valve Series No. 1 pero tag dice PSV-09-002) — NUEVO DUPLICADO / TYPO ⚠️

**Error área-07 persistente:**
- Item 7: VM-07-005 — área "07" sigue presente (debe ser VM-09-005). Error detectado en TM N3 OBS-13. NO CORREGIDO ✗

### 2.3 Análisis crítico

BW Water resolvió los 4 duplicados originales de TM N6 OBS-01, pero al renombrar/reorganizar introdujo dos nuevos conflictos de TAG:

1. **VE-09-007** en ítems 44 y 64: Probable causa — el item 44 (antes identificado como VE-09-008 en Rev B, ahora "corregido" a VE-09-007) colisiona con el existente item 64 que ya tenía VE-09-007. BW Water renombró el ítem 44 a VE-09-007 sin verificar la unicidad.

2. **PSV-09-002** en ítems 105 y 112: Ítem 112 parece ser PSV-09-001 con typo en el campo de TAG. La Valve Series No. muestra "1" pero el campo TAG dice "PSV-09-002".

Ambos son fallos QA críticos que impiden la identificación unívoca de válvulas en PLC/SCADA.

---

## 3. Equipment List Rev B — P22-LI-09-005-001

**Veredicto: 2 — Approved as Noted**
**CCS:** Submittal 25007-0008, 11/3/2026

### 3.1 CCS — 1 ítem

| Item | Comentario ADASA | Respuesta BW | Veredicto |
|------|-----------------|--------------|-----------|
| 1 | Discrepancias vs P&ID: TAG Static Mixer, CIP Tank, Antiscalant Tank, Dosing Pump | BW confirma: (1) MZE-09-001, (2) CIP 6.1 m³, (3) Antiscalant 0.27 m³ eff., (4) HP Pump 125 hp=93 kW, (5) Dosing 2.3 LPH | **CERRADO** ✓ |

### 3.2 Verificación en documento

- BH-09-001 (HP Pump): 125 hp = 93 kW, 380V/50Hz/3ph, VFD, 3-wire RTD, ABB or equiv. ✓
- SIP-09-001/002: Correct tags, HPB-60, no motor ✓
- BH-09-002 (CIP Pump): 11 kW, 380V/50Hz, Grundfos CRN64-2, 3-wire RTD ✓
- TK-09-002 (Antiscalant Tank): 0.27 m³ effective, 630mm D × 1090mm H, Linear Polyethylene MD ✓
- BDS-09-001/002 (Dosing Pump): 2.3 LPH, Prominent GMXa 1602, 230V/50Hz/1ph ✓
- Nota: TM N10 OBS-05 (seismic anchor data para antiscalant tank) aún requiere GA Rev B — el Equipment List provee material y volumen ✓ pero no anchor layout

### 3.3 Sin nuevas observaciones formales

El documento cierra las discrepancias de TM N9. No se generan nuevas OBS.

---

## 4. GA CIP Flushing Skid Pump Rev A — P22-DWG-09-005-010

**Veredicto: 2 — Approved as Noted**
**Primera entrega — sin CCS**

### 4.1 Análisis

El PDF utiliza fuentes cipher-encoded que impiden la extracción de texto de las vistas técnicas del plano. La información del título block y descripción del proyecto es legible.

Esta es la primera entrega del GA del skid de la bomba CIP (BH-09-002, Grundfos CRN64-2). Por ser GA de un skid (no datasheet del equipo), los datos de RTD/instrumentación estarán principalmente en el datasheet P22-ET-09-009-003. Lo que sí debe verificar el GA son:
- Anchor bolt layout y datos sísmicos (NCh 2369, Zona 3) — requerimiento ET §4.4
- Dimensional para coordinación con civil/piping

Sin poder verificar el contenido técnico desde el texto extraído, se levanta NOTE solicitando confirmación de datos sísmicos en la siguiente revisión.

---

## 5. GA Antiscalant Dosing Skid Pump Rev A — P22-DWG-09-005-011

**Veredicto: 2 — Approved as Noted**
**Primera entrega — sin CCS**

### 5.1 Análisis

Situación idéntica a CIP Pump GA — fuentes cipher-encoded impiden lectura. La bomba BDS-09-001/002 es de tipo solenoide metering (24W, 230V, 1ph) — no aplican requisitos de Pt-100 de motor per ET §5.3. Lo relevante para este GA es el anchor layout sísmico (ET §4.4) y la disposición del skid.

Se visualizan algunas dimensiones: 500 mm × 1380 mm × 500 mm (footprint aproximado), tuberías DN25 confirmadas, referencia al antiscalant tank TK-09-002.

Se levanta NOTE sobre datos de anclaje sísmico.

---

## 6. Painting Specifications Rev B — P22-ET-09-006-2

**Veredicto: 1 — Approved**
**CCS:** Submittal 5/3/2026

### 6.1 CCS — 2 ítems

| Item | Comentario ADASA | Respuesta BW | Veredicto |
|------|-----------------|--------------|-----------|
| 1a | RAL 5017 no coincide con ET §5.1.9 (RAL 5012 para estructura) | ET §5.1.9 aplica a estructura (ítem 4); RAL 5017 es para el container. | **CERRADO** ✓ |
| 1b | DFT 350 µm debe ser 355 µm mínimo | "Revised 350 µm to 355 µm for the container." | **CERRADO** ✓ |

### 6.2 Verificación en documento

- Ítem 4 (Frame Support, CS A-36): RAL 5012 (Luminous Blue), 355 µm ✓
- Ítem 12 (Container External): RAL 5017 (Traffic Blue), 355 µm ✓
- Sistema de pintura ítem 4: Zinc Clad II (80µm) + Macropoxy 646 (200µm) + Acrolon 218 HS (75µm) = 355 µm ✓
- Preparación de superficie: ISO 8501-1 SA 2.5 (ítem 4) ✓
- Pipe labelling: ASME A13.1-2020 ✓

Todas las observaciones previas correctamente incorporadas. Documento aprobado sin observaciones adicionales.

---

## 7. HP Pump Datasheet Rev D — P22-ET-09-009-002

**Veredicto: 2 — Approved as Noted**
**CCS:** Submittal 25007-0007, 12/3/2026

### 7.1 CCS — 1 ítem

| Item | Comentario ADASA | Respuesta BW | Veredicto |
|------|-----------------|--------------|-----------|
| 9 | (No se muestra comentario original de ADASA en CCS) | "As there are no 1800 psi coupling for 4 inch, BW will provide 2000 psi coupling instead. Coupling datasheet has been attached." | **CERRADO** ✓ |

### 7.2 Verificación en documento

- Parámetros: Q=49.0 m³/h, ΔP=46.9 bar, 380V/50Hz/3ph, 125 hp (93 kW), VFD ✓
- Motor: TEFC, IP66, Insulation F ✓
- **Row 55: "3-wire RTDs for bearings (100 Ohm Platinum), 3-wire RTDs for windings (100 Ohm Platinum)"** — ET §5.3 CUMPLE ✓ (Pt-100 devanados Y rodamientos confirmados)
- **Row 55: "With mounting surface for a vibration sensor"** — ET §5.5.7 CUMPLE ✓
- Coupling: Style H adjunto, 2000 psi para DN25-DN100 ✓ — cierra TM N6 OBS-01 para HP Pump
- Coupling MAWP vs presión operación: 2000 psi >> 48.9 bar (~710 psi) proceso HP pump ✓

**Inconsistencia interna motor manufacturer:**
- Component Datasheet row 39 (sección MOTOR): "GE"
- FEDCO Technical Proposal (tabla Motor Data p.3): "ABB or equivalent"
- El modelo de motor está aún en TBA — la inconsistencia es documental y debe reconciliarse

### 7.3 Nota

Se levanta NOTE-02 sobre inconsistencia de fabricante de motor dentro del mismo documento (GE vs ABB equiv.). No impide la aprobación del documento dado que el modelo es TBA.

---

## 8. Feed Turbocharger Datasheet Rev D — P22-ET-09-009-007 (SIP-09-001)

**Veredicto: 2 — Approved as Noted**
**CCS:** Submittal 25007-0008, 11/3/2026

### 8.1 CCS — 1 ítem

| Item | Comentario ADASA | Respuesta BW | Veredicto |
|------|-----------------|--------------|-----------|
| 5 | (No se muestra comentario original) | "BW has revised the turbocharger coupling. Datasheet of Coupling also attached." | **VERIFICAR** |

### 8.2 Verificación en documento

- Conexiones Feed: DN50/DN50, Coupling 1800 psi (row 29) ✓
- Conexiones Brine: DN40/DN40, Coupling 1800 psi (row 30) ✓
- **Row 38: "vibration sensor mounting surface"** — resuelve TM N10 OBS-06 ✓
- Materials: Casing Super Duplex 2507, O-rings Buna N ✓
- Coupling datasheet adjunto: Piedmont Style S/X, 1800 psi para DN40 y DN50 ✓
  - Style S 1-1/2" (DN40): 1800 psi ✓ (brine inlet/outlet)
  - Style S 2" (DN50): 1800 psi ✓ (feed inlet/outlet)
  - Presión operación SIP-09-001: ~69.5 bar (brine inlet) = ~1,008 psi << 1800 psi ✓
- **TM N6 OBS-01: CERRADO** — coupling 1800 psi cumple el requisito de ADASA

**Inconsistencia coupling style:**
- Outline drawing HPB-60 (p.6): muestra "CUT GROOVE STYLE 77" en los 4 nozzles
- Coupling datasheet adjunto: STYLE S/X (producto Piedmont diferente de STYLE 77)
- Conclusión: El Style S con 1800 psi es el producto a instalar, pero el outline drawing debe actualizarse

### 8.3 Cerramiento TM N6 OBS-01

TM N6 OBS-01 rechazó el datasheet por coupling a 1200 psi (Piedmont Style H 2" a 1200 psi, margen del 19% sobre 1008 psi operación). Rev D cambia el coupling a Style S/X con 1800 psi, dando margen de ~79% sobre la presión de operación. **TM N6 OBS-01 se cierra formalmente en TM N11.**

---

## 9. Interstage Turbocharger Datasheet Rev D — P22-ET-09-009-008 (SIP-09-002)

**Veredicto: 2 — Approved as Noted**

Análisis idéntico a SIP-09-001:
- Row 29/30: Coupling 1800 psi (DN50 feed, DN40 brine) ✓
- Row 38: "vibration sensor mounting surface" ✓ — resuelve TM N10 OBS-07 ✓
- Coupling Style S/X 1800 psi adjunto ✓ — cierra TM N6 OBS-01 ✓
- Misma inconsistencia outline drawing Style 77 vs datasheet Style S/X — NOTE-04

Brine outlet pressure SIP-09-002: 53.5 bar (~776 psi) << 1800 psi ✓
Brine inlet pressure SIP-09-002: 83.33 bar (~1,208 psi) — Style S 1800 psi >> margen adecuado ✓

---

## 10. Grounding Point & Power Panel Location Layout Rev B — P22-DWG-09-007-003

**Veredicto: 2 — Approved as Noted**
**CCS:** Submittal referenciado (CCS cipher-encoded, parcialmente legible)

El PDF utiliza fuentes cipher-encoded que impiden la lectura completa del plano. El CCS (páginas 1-2) indica que los comentarios previos de TM N3 ADASA-BW han sido incorporados en Rev B. La fecha del título block es 2-Mar-26 (Rev B), Rev A fue 19-Jan-26.

Sin observaciones formales. El dibujo de distribución eléctrica no es un documento de alcance técnico-proceso que requiera verificación detallada de TAGs de instrumentación.

---

## 11. Instrument Location Layout Rev B — P22-DWG-09-008-001

**Veredicto: 2 — Approved as Noted**
**CCS:** Submittal TRANSMITTAL N3 ADASA-BW (8 ítems)

### 11.1 CCS — 8 ítems, todos "Current"

| Item | Respuesta BW | Veredicto |
|------|--------------|-----------|
| 1 | "Has been revised and added in RevB" | CERRADO |
| 2 | "Has been added in RevB" | CERRADO |
| 3 | "Has been added in RevB" | CERRADO |
| 4 | "Has been revised. I/O List has been revised to CIT-09-004." | CERRADO — tag CIT-09-004 correcto ✓ |
| 5 | "Has been revised in RevB" | CERRADO |
| 6 | "Has been revised in RevB" | CERRADO |
| 7 | "Has been added. This is RTD temperature element and directly connect into PLC RTD module and able to continuous monitoring and trending." | CERRADO — motor RTDs mostrados en layout ✓ |
| 8 | "Has been revised and added in RevB" | CERRADO |

**Resumen:** 8 CERRADOS / 0 PARCIALES / 0 ABIERTOS — respuestas comprensivas y bien ejecutadas.

El ítem 7 es particularmente significativo: confirma que los RTDs de temperatura de motores están representados en el Instrument Location Layout y conectan al módulo RTD del PLC para monitoreo continuo. Esto es consistente con el cierre de TM N8 OBS-2 (motor RTDs solicitados) que ya se había cerrado en TM N10.

---

## 12. Tabla Resumen TM N11

| # | Documento | Rev | Entrega | Veredicto | OBS/NOTE |
|---|-----------|-----|---------|-----------|---------|
| 1 | Valve List | C | E19 | **3 — To be Revised** | OBS-01, OBS-02, NOTE-01 |
| 2 | Equipment List | B | E19 | 2 — Approved as Noted | — |
| 3 | GA CIP Pump | A | E19 | 2 — Approved as Noted | NOTE-05 |
| 4 | GA Antiscalant Pump | A | E19 | 2 — Approved as Noted | NOTE-06 |
| 5 | Painting Specs | B | E19 | **1 — Approved** | — |
| 6 | HP Pump Datasheet | D | E20 | 2 — Approved as Noted | NOTE-02 |
| 7 | Turbo 1 Datasheet | D | E20 | 2 — Approved as Noted | NOTE-03 |
| 8 | Turbo 2 Datasheet | D | E20 | 2 — Approved as Noted | NOTE-04 |
| 9 | Grounding Layout | B | E21 | 2 — Approved as Noted | — |
| 10 | Instrument Layout | B | E21 | 2 — Approved as Noted | — |

**Veredicto Global: 3 — TO BE REVISED**

---

## 13. Estado de Observaciones Pendientes de TMs Anteriores

| TM N° | OBS | Descripción | Estado en TM N11 |
|-------|-----|-------------|-----------------|
| TM N6 | OBS-01 | Coupling pressure turbochargers | **CERRADO** — Style S 1800 psi (Turbo 1+2); Style H 2000 psi (HP Pump) |
| TM N10 | OBS-01 | TE vs TIT motor tags | ABIERTO — IO List Rev C no recibida |
| TM N10 | OBS-02 | Conductivity ranges CIT-09-001/004/005 | ABIERTO — DTL Rev B no recibida |
| TM N10 | OBS-03 | VE09-014 DI block + level alarms Modbus | ABIERTO — DTL Rev B no recibida |
| TM N10 | OBS-04 | UPS 8h autonomy | ABIERTO — sin confirmación recibida |
| TM N10 | OBS-05 | Antiscalant Tank GA anchor/seismic data | PARCIAL — EL Rev B confirma material/volumen; GA Rev B (anchor layout) pendiente |
| TM N10 | OBS-06 | SIP-09-001 vibration mounting | **CERRADO** — DS Rev D row 38 |
| TM N10 | OBS-07 | SIP-09-002 vibration mounting | **CERRADO** — DS Rev D row 38 |
| TM N10 | NOTE-05 | HMI Screenshots P22-BREAD-09-008-001 | ABIERTO — no recibido |

---

*Generado: 17-Mar-2026 | Revisado por: Luis Rivera | Para uso interno ADASA*
