# COMPILADO INTERNO — TM N13
**PROYECTO:** BAE 12803 — Módulo Salmuera Taltal
**CÓDIGO:** P22-TM-09-000-013-0
**FECHA:** 31-Mar-2026
**ENTREGA:** E24 (25007-0024)
**USO:** INTERNO ADASA — NO ENVIAR A BW WATER

---

## 1. DOCUMENTOS REVISADOS

| N° | Código | Descripción | Rev | Veredicto |
|----|--------|-------------|-----|-----------|
| 1 | P22-DWG-09-009-002 | Piping and Instrumentation Diagram | C | **2 — Approved as Noted** |

**VEREDICTO GLOBAL: 2 — APPROVED AS NOTED**

---

## 2. ANÁLISIS: P&ID Rev C (E24, 25007-0024)

**Fecha recepción:** 31-Mar-2026
**Páginas:** 12 (proceso) + 1 (CCS) = 13 páginas
**Extracto MD:** `ENTREGAS_BWWATER/ENTREGA 24/md/P22-DWG-09-009-002_C - Piping & Instrumentation Daigram_extracted_chunk_1.md` + chunk_2

---

### 2.1 Title Block (Bloque A-1)

**Código en Rev C:** P22-DWG-09-009-002 ✓
**Revisión:** C, **Fecha:** 27/03/2026 ✓

**TM N9 NOTE-01: CERRADA**
CCS Consolidated Comment Sheet (página 13 del PDF, comment 14, status "Current"):
- BW Reply: "BW has revised accordingly."
El código del title block fue corregido de P22-DWG-09-009-02 a P22-DWG-09-009-002 (tres dígitos de correlativo).

---

### 2.2 TK-09-002 Antiscalant Tank (Bloque A-2)

**Volumen en Rev C:** VOL: 0.34 m³ (TOTAL) ✓

**TM N9 NOTE-02: CERRADA**
CCS página 13, comment 15, status "Current":
- ADASA Comment: "Update to 0.34 m³ in Rev C."
- BW Reply: "BW has revised accordingly."
El P&ID Rev C anota TK-09-002 con 0.34 m³ (TOTAL), consistente con el datasheet aceptado P22-ET-09-009-010 Rev B.

**Implicación TM N10 OBS-05:**
La parte relacionada con el P&ID (volumen TK-09-002) está atendida. La GA Antiscalant Tank Rev B sigue siendo requerida para completar el cierre (seismic anchor data, body material, effective/total volumes en el GA drawing). Estado actualizado: PARTIALLY ADDRESSED.

---

### 2.3 TAGs Duplicados Valve List (Bloque B)

**TM N11 OBS-01 (VE-09-007) y OBS-02 (PSV-09-002):**

El texto fragmentado del P&ID no permite verificar directamente la unicidad de VE-09-007 en el plano. La duplicación fue originada en la Valve List Rev C (items 44 y 64 para VE-09-007; items 105 y 112 para PSV-09-002). El P&ID Rev C muestra PSV-09-002 en un solo punto (zona antiscalant, página 12) y PSV-09-001 en la zona HP/RO — sin evidencia de duplicación en el P&ID.

Estas observaciones permanecen abiertas contra la Valve List (no el P&ID). No se genera nueva OBS en TM N13 por este concepto.

---

### 2.4 Verificación Equipos Principales (Bloque E)

| TAG | Descripción | Rev C | Estado |
|-----|-------------|-------|--------|
| BH-09-001 | HP Feed Pump | Presente | ✓ |
| SIP-09-001 | Feed Turbocharger | Presente | ✓ |
| SIP-09-002 | Interstage Turbocharger | Presente | ✓ |
| BOI-09-001 | 1st Stage RO Rack | Presente | ✓ |
| BOI-09-002 | 2nd Stage RO Rack | Presente | ✓ |
| MZE-09-001 | Static Mixer | Presente | ✓ |
| FIL-09-001 | Cartridge Filter (RO Feed) | Presente | ✓ |
| FIL-09-002 | CIP Cartridge Filter | Presente | ✓ |
| TK-09-001 | CIP Tank | Presente — **6.81 m³** | ⚠️ Ver NOTE-01 |
| TK-09-002 | Antiscalant Tank | Presente — **0.34 m³ (TOTAL)** | ✓ |
| BDS-09-001/002 | Antiscalant Dosing Skid | Presente | ✓ |
| VE-09-014 | Antiscalant Dosing Pump valve | Presente | ✓ |
| VT-09-001 | Vibration Transmitter (BH-09-001) | Presente | ✓ |
| VT-09-002 | Vibration Transmitter (SIP-09-001) | Presente | ✓ |

---

### 2.5 HALLAZGO NUEVO: TK-09-001 Volumen (NOTE-01)

**Observación:**
- P&ID Rev C: TK-09-001 (CIP Tank) = **6.81 m³** (HDPE)
- P&ID Rev B: 6.11 m³ (mismo tanque)
- Equipment List Rev B (E19, aprobado TM N11): 6.1 m³ (Dayamas DYM 6800, HDPE, 1800 mmD × 2950 mmH, Eff. Height 2550 mm)
- Process Calculation Rev B (E7): Selected CIP Tank Volume = 6.1 m³

**Análisis:**
La diferencia de 0.7 m³ (6.11 → 6.81 m³) entre Rev B y Rev C del P&ID no tiene antecedente justificado en ningún submittal o revisión de transmittal. El Equipment List Rev B y el Process Calculation Rev B especifican 6.1 m³ como el volumen correcto. El modelo Dayamas DYM 6800 con dimensiones 1800 mmD × 2950 mmH tiene un volumen geométrico de:

V = π/4 × 1.8² × 2.95 ≈ 7.5 m³ (bruto), pero el volumen efectivo de trabajo es 6.1 m³.

El valor 6.81 m³ puede ser un error de redondeo o de actualización sin base documental. Se clasifica como NOTE para aclaración prior to IFC.

**Clasificación:** NOTE-01 MINOR
**Severidad para doc-annotator:** NOTE
**Acción:** Confirmar volumen correcto de TK-09-001 y actualizar P&ID consistente con Equipment List Rev B (6.1 m³) prior to IFC (Rev 0). Si el CIP Tank fue rediseñado con mayor capacidad, emitir Equipment List Rev C con justificación.

---

### 2.6 Instrumentación (Bloque D)

| TAG | Descripción | Rev C |
|-----|-------------|-------|
| VT-09-001 | Vibration Transmitter HP Pump | Presente ✓ |
| VT-09-002 | Vibration Transmitter SIP-09-001 | Presente (fragmentado: "09-00VT") ✓ |
| CIT-09-001 | Conductivity 1st stage feed | Presente ✓ |
| CIT-09-002 | Conductivity RO output/permeate | Presente ✓ |
| PSV-09-001 | Pressure Safety Valve HP zone | Presente ✓ |
| PSV-09-002 | Pressure Safety Valve antiscalant | Presente — único en P&ID ✓ |

**Nota sobre TIT-09-003 y LS-09-001/002:**
El texto fragmentado del P&ID no permite confirmar/descartar la presencia de estos instrumentos. Las observaciones TM N10 OBS-01 (TIT-09-003 conflicto de servicio) y TM N10 OBS-03 (LS-09-001/002 ausentes del Modbus map) están abiertas contra el I/O List y Data Transfer List, no contra el P&ID directamente.

---

### 2.7 Válvulas (Bloque C)

| Check | Resultado |
|-------|-----------|
| VM-09-015 manual (HP Pump to Feed TC isolation) | No visible en texto fragmentado; TM N9 confirmó correcto |
| VE-09-008/009 eléctricas (RO Reject) | Presentes ✓ |
| VE-09-014 eléctrica (antiscalant) | Presente ✓ |
| VE-09-016 eléctrica (antiscalant) | Presente ✓ |
| Footprint CIP ≤3,500 mm | No verificable desde texto extraído |

**Nota sobre OBS-03/04 TM N11:**
No es posible verificar desde el texto extraído si el footprint CIP cumple ≤3,500 mm. Las OBS-03 y OBS-04 de TM N11 permanecen abiertas. Si el P&ID Rev C incluye el layout actualizado del CIP externo, ADASA debería revisar el plano visualmente para confirmar.

---

## 3. RESUMEN OBS/NOTE TM N13

| ID | Tipo | Documento | Severidad | Descripción breve | Acción |
|----|------|-----------|-----------|-------------------|--------|
| NOTE-01 | Nueva | P&ID Rev C | MINOR | TK-09-001 volumen = 6.81 m³ vs 6.1 m³ en Equipment List Rev B | Confirmar/corregir prior to IFC |

---

## 4. ESTADO OBSERVACIONES HEREDADAS

| TM | OBS | Documento | Estado anterior (TM N12) | Estado en TM N13 |
|----|-----|-----------|--------------------------|------------------|
| N10 | OBS-01 | I/O List / DTL | OPEN | OPEN — sin respuesta |
| N10 | OBS-02 | Data Transfer List | OPEN | OPEN — sin respuesta |
| N10 | OBS-03 | Data Transfer List | OPEN | OPEN — sin respuesta |
| N10 | OBS-04 | Control Architecture | OPEN | OPEN — sin respuesta |
| N10 | OBS-05 | GA Antiscalant Tank | OPEN | **PARTIALLY ADDRESSED** — P&ID Rev C corrige TK-09-002 a 0.34 m³. GA Rev B sigue pendiente. |
| N10 | NOTE-05 | HMI Screenshots | OPEN | OPEN — sin respuesta |
| N11 | OBS-01 | Valve List Rev C | OPEN | OPEN — Valve List Rev D no recibida |
| N11 | OBS-02 | Valve List Rev C | OPEN | OPEN — Valve List Rev D no recibida |
| N11 | OBS-03 | Grounding Layout Rev B | OPEN | OPEN — pending Equipment Layout acceptance |
| N11 | OBS-04 | Instrument Location Layout Rev B | OPEN | OPEN — pending Equipment Layout acceptance |
| N12 | OBS-01 | Datasheet Vibration Transmitter Rev A | OPEN | OPEN — Rev B no recibida |
| N12 | NOTE-01 | Datasheet Vibration Transmitter Rev A | OPEN | OPEN — Rev B no recibida |
| N12 | NOTE-02 | Line List Rev B | OPEN | OPEN — Rev C (IFC) no recibida |

---

## 5. DECISION PARA ANOTACIÓN PDF

**NOTE-01** → Se anotará en el P&ID Rev C con color NOTE (azul claro)
- Página: 11 (zona CIP Tank TK-09-001)
- Texto de búsqueda: "6.81" o "TK-09" zona CIP
- Texto anotación: "NOTE-01: CIP Tank TK-09-001 annotated as 6.81 m³. Equipment List Rev B specifies 6.1 m³ (Dayamas DYM 6800). Confirm correct volume and update P&ID consistent with Equipment List prior to IFC (Rev 0). If tank capacity was revised, submit updated Equipment List Rev C with justification."

---

## 6. NOTAS INTERNAS (VAN DOORN — NO ENVIAR)

- El cambio de 6.11 → 6.81 m³ en TK-09-001 puede estar relacionado con el relayout del CIP system fuera del contenedor (TM N7). Es posible que BW Water seleccionó un tanque de mayor capacidad en la nueva ubicación exterior. Sin embargo, no hay evidencia de que esta selección fue comunicada formalmente a ADASA.
- El footprint CIP externo no es verificable desde el texto del P&ID. Se recomienda revisión visual del PDF para confirmar el cumplimiento de ≤3,500 mm (prerequisito para desbloquear TM N11 OBS-03/04).
- La tabla PSV del P&ID: PSV-09-001 en zona HP/RO (presión alta) y PSV-09-002 en zona antiscalant. Ambas parecen únicas en el P&ID, pero la Valve List Rev C tenía duplicado para PSV-09-002 (items 105 y 112). La Valve List duplicado puede ser un error de la Valve List que el P&ID no refleja (dos ítems distintos con el mismo TAG en el inventario, pero el P&ID solo tiene una posición para PSV-09-002). Esto confirma que la observación TM N11 OBS-02 debe resolverse en Valve List Rev D.
- Procesamiento de la ENTREGA 24 completado el 31-Mar-2026. TM N13 emitido el mismo día de la entrega.
