# _ANALISIS_TRABAJO.md — Transmittal N19 (P22-TM-09-000-019-0)

**Documento INTERNO ADASA — NO ENVIAR a BW Water**

Consolida cross-checks técnicos, análisis del historial OBS/NOTE por documento, verificación de Comments Response Sheets, y justificación de veredictos. Input para la redacción del `P22-TM-09-000-019-0_TRANSMITTAL.md`.

---

## 1. Estado al 25-May-2026

- TM N18 ENVIADO 18-May-2026 (4 Code 1 + 1 Code 3 Plant Control Philosophy Rev C). Control Philosophy Rev D esperada, **NO entregada** en E42-E45.
- 4 entregas nuevas E42, E43, E44, E45 entre 21-May y 25-May, 13 documentos a revisar.
- NT-001 (Mitigation Plan Clarifications) emitida 25-May, BORRADOR pendiente Víctor + envío. Cross-references explícitas con E44 ITP Offsite (ASME X stamp) y E45 Cartridge Filters (FRP/H→V).

## 2. Tally final TM N19

| # | Documento | Rev | Code | Driver |
|---|---|---|---|---|
| 2.1 | Electrical Load List | B | **2** | Falta declaración Pt-100 motores ET §5.3 L1032 |
| 2.2 | Power Cable Schedule | B | **2** | REL-001 CIP Heater 2 líneas — topología control intermedia poco clara |
| 2.3 | Datasheet Power & Control Cable | B | **1** | Especificación completa, normativa cumplida |
| 2.4 | Single Line Diagram | B (nuevo) | **2** | Enclosure NEMA 4X/IP66 no especificado; SPDs no visibles |
| 2.5 | Grounding & Power Panel Layout | E | **3** | Items NO RESPONDIDO (TM N11 OBS-03 + TM N15 NOTE-03 + TM N17 NOTE-02, 70-110 días); Comments Sheet degradada |
| 2.6 | Cable Tray Layout | C | **1** | **CIERRA 100+ días**: TM N4 OBS-06/07 + TM N15 OBS-04..08 con evidencia específica |
| 2.7 | Typical Power Works Installation | C | **2** | Cierra TM N17 NOTE-01/02/03/04 (adopta IEC 60364-5-54); método grounding 1-7 no designado |
| 2.8 | I/O List | 1 IFC | **2** | 6/8 items abiertos cierran; bandera IFC submission con Control Philosophy Rev D aún Code 3 |
| 2.9 | Project Quality Plan | B | **2** | Cierra TM N17 OBS-01/02 CRÍTICOS → **vínculo pago 40% liberable** |
| 2.10 | ITP Offsite | B | **3** | **Silencio sobre ASME X stamp post-mitigation plan** — cross-NT-001 6.A/6.C |
| 2.11 | Instrumentation Cable Schedule | 0 (nuevo) | **3** | 4 OBS-NEW + dependencia Control Philosophy Rev D |
| 2.12 | Datasheet RO Cartridge Filter | D | **3** | Cambio H→V **unilateral pre-NT-001** (5.A-E); FRP mantenido sin justificación PREN |
| 2.13 | Datasheet CIP Cartridge Filter | C | **3** | Igual que 2.12 |

**Tally: 2 Code 1 + 6 Code 2 + 5 Code 3 = 13 documentos**
**Veredicto global: 3 — TO BE REVISED**

## 3. Drivers principales (Why Code 3)

### 3.1 Grounding & Power Panel Layout Rev E (Section 2.5)
Items abiertos previos sin respuesta en Comments Response Sheet del Rev E:
- TM N11 OBS-03 (70+ días): cronograma completo puesta a tierra (PE identifiers, sección, topología ring main per NCh Eléct. 4/2003 §10.0, bonding equipotencial)
- TM N15 NOTE-03 (~34 días): grounding schedule completeness
- TM N17 NOTE-02 (~12 días): revision history block vacío
Status del Comments Sheet: degradado en extracción — solicitar PDF re-enviado.

### 3.2 ITP Offsite Rev B (Section 2.10)
Silencio administrativo sobre ASME X stamp para Pressure Vessels. La oferta BW Water Rev1 ITP §12 (página 100, línea 3905) comprometió *"Test certification to ASME X"* rated 1000 PSI SWRO. El Mitigation Plan 22-May propuso eliminar el sello. ADASA emitió NT-001 (25-May) cuestionando el waiver. Rev B del ITP no menciona ASME X — ni para mantenerlo ni para eliminarlo. **Posición ADASA**: BW Water no puede modificar el alcance contratado por omisión. Code 3 con OBS-01 reincidente cross-reference NT-001 6.A/6.C exigiendo declaración explícita en próxima Rev del ITP.

### 3.3 Instrumentation Cable Schedule Rev 0 (Section 2.11)
Documento nuevo (primer review formal). 4 OBS detectadas:
- OBS-NEW-01: VFD comms internas HP/CIP Pump listadas como "PANEL INTERIOR WIRE" sin especificación de cable
- OBS-NEW-02: Dosing pumps (Items 82-85) sin señal "IN REMOTE" DI consistente con HP/CIP
- OBS-NEW-03: Inconsistencia nomenclatura LIT/LS switches (Items 80-81)
- OBS-NEW-04: PHIT09-006 con tag incompleto en algunas filas (merged cells)
Dependencia: alinear con Control Philosophy Rev D antes de IFC final del Cable Schedule.

### 3.4 RO Cartridge Filter Rev D + CIP Cartridge Filter Rev C (Sections 2.12 + 2.13)
BW Water emitió ambas Rev el 25-May, **mismo día** que ADASA emitió NT-001 (BORRADOR pendiente envío). Las nuevas Rev:
- Mantienen FRP (Section 3.5 NT-001 5.A) — correcto vs propuesta FRP→SS316 del mitigation plan
- Cambian configuración H→V — **cambio unilateral pre-NT-001 5.C/5.E** (drawing container actualizado + tie-ins inamovibles)
- Nuevo vendor: **Sysflo** (no Filtrek como en oferta, no Protec como rumoreado)
- RO: 22 cartuchos (flow 2.23 m³/h/cartucho — cierra TM N3 OBS-01 flow rate 4.08 alto)
- CIP: 31 cartuchos (flow 1.84 m³/h/cartucho)
**Posición ADASA**: BW Water no puede materializar unilateralmente el cambio V (ni el cambio de vendor a Sysflo) antes de recibir respuesta a NT-001. Code 3 con OBS-NEW-01 cross-NT-001 5.A-E exigiendo: (a) confirmación tie-ins inamovibles con drawing actualizado del container, (b) justificación FRP en feed brine ~40k ppm Cl⁻, (c) confirmación equivalencia técnica Sysflo vs Filtrek (ofertado).

---

## 4. Cierres consolidados (~14 items históricos)

| TM origen | Item | Días | Cierra con |
|---|---|---|---|
| TM N3 | OBS-01 (vibration VT-09-001/002/003 en IO List) | 110 | IO List Rev 1 ✅ |
| TM N3 | OBS-03 (VFD vars HP/CIP) | 110 | IO List Rev 1 PARCIAL |
| TM N3 | OBS-04 (external enable DI) | 110 | IO List Rev 1 ✅ |
| TM N3 | OBS-05 (external status DO) | 110 | IO List Rev 1 ✅ |
| TM N3 | OBS-01 (RO Cartridge flow rate 4.08 m³/h alto) | 110 | RO Cartridge Filter Rev D ✅ (22 cartuchos, 2.23 m³/h) |
| TM N4 | OBS-06 (Cable Tray vibration locations) | 110 | Cable Tray Rev C ✅ |
| TM N4 | OBS-07 (Cable Tray Pt-100 locations) | 110 | Cable Tray Rev C ✅ |
| TM N14 | NOTE-02 (analyzer voltage 220 VAC vs 24 VDC) | ~80 | IO List Rev 1 — **NO RESPONDIDO** (mantener abierto) |
| TM N15 | OBS-04 (S4 interference) | 34 | Cable Tray Rev C ✅ |
| TM N15 | OBS-05 (anchoring) | 34 | Cable Tray Rev C ✅ (Rev B ya lo cerraba) |
| TM N15 | OBS-06 (MAIN PANEL routing) | 34 | Cable Tray Rev C ✅ |
| TM N15 | OBS-07 (S3/S4 zoning) | 34 | Cable Tray Rev C ✅ |
| TM N15 | OBS-08 (CIP tray conflict) | 34 | Cable Tray Rev C ✅ |
| TM N17 | OBS-01 (PQP inspection matrix CRÍTICO) | 12 | PQP Rev B ✅ |
| TM N17 | OBS-02 (PQP FAT scope CRÍTICO, vínculo pago 40%) | 12 | PQP Rev B ✅ |
| TM N17 | OBS-03 (PQP procedure codes) | 12 | PQP Rev B → DIFERIDO al ITP |
| TM N17 | OBS-04 (PQP H/W/S/R points) | 12 | PQP Rev B ✅ |
| TM N17 | OBS-01 (ITP placeholders X/Y bar) | 12 | ITP Rev B ✅ |
| TM N17 | OBS-02 (ITP document control) | 12 | ITP Rev B ✅ |
| TM N17 | OBS-03 (ITP placeholder codes) | 12 | ITP Rev B → DIFERIDO ("submit separate for approval") |
| TM N17 | NOTE-01/02/03/04 (Power Works SEC/NEC, grounding, feed, duct bank) | 12 | Typical Power Works Rev C ✅ |
| TM N17 | NOTE-01 (IO List dosing IN REMOTE) | 12 | IO List Rev 1 PARCIAL |
| TM N17 | NOTE-02 (IO List RTD °C) | 12 | IO List Rev 1 ✅ |
| TM N17 | NOTE-03 (IO List CIP P&ID page) | 12 | IO List Rev 1 ✅ |

**Total: ~14 items históricos cerrados, ~3 parciales/diferidos, ~3 no respondidos**

## 5. Carry-forward a Section 3 del TM N19

**(a) Code 3 abierto sin entregar:**
- **Plant Control Philosophy Rev D** — TM N18 OBS-01 CRITICAL permissive HP Pump + OBS-02 MAJOR Sequence Charts + OBS-03 MAJOR salt rejection formula. Reincidente desde TM N15 NOTE-20 (~40+ días). Mantener lenguaje firme sin pre-rechazo (lección NT-001 tono).

**(b) Tracked IFC Rev 0 (entregables de docs Code 1 TM N18):**
- TM N16 NOTE-01 weight disclosure — no abordado en E42-E45 directamente; verificar referencia indirecta en SLD Rev B
- PSV-09-002 overpressure analysis (Valve List Rev D Code 1) — no entregado
- CIT-09-004 reflejado en Instrument List Rev D + Line List Rev C + nota de lazo (P&ID Rev D Code 1) — IO List Rev 1 confirma cambio CIT-09-004 (4-20mA, P9) ✅ parcial
- Dual-value CIP Tank (P&ID/datasheet/Equipment List) — no entregado
- AC Thermal margen efectivo explícito +13.3% — no entregado

**(c) Items históricos no cerrados en TM N19:**
- TM N4 NOTE-05 HMI screenshots (~110 días) — no en E42-E45
- TM N5 OBS-02 (~92 días) — verificar contexto
- TM N10 OBS-05 (~75 días) — verificar contexto
- TM N11 OBS-03 grounding cronograma (en Doc 2.5 Grounding Rev E, NO RESPONDIDO) — sigue abierto
- TM N13 NOTE-02 (~50 días) — verificar contexto
- TM N14 NOTE-02 analyzer voltage 220 VAC vs 24 VDC (~80 días) — IO List Rev 1 NO RESPONDIDO
- TM N15 LCP Datasheet Rev B (~34 días) — no en E42-E45
- TM N15 Cable Tray NOTE-03 (~34 días) — Grounding Rev E NO RESPONDIDO
- TM N17 OBS-01 (Grounding Consolidated Sheet) — Grounding Rev E parcial

**(d) Items nuevos TM N19 que se trackearán para futuro IFC:**
- OBS-NEW Electrical Load List Pt-100 motores ET §5.3
- OBS-NEW Power Cable Schedule REL-001 topología 2 cables
- OBS-NEW SLD Rev B enclosure NEMA 4X/IP66 + SPDs
- OBS-NEW Cable Tray tabla XYZ separaciones S1-S7
- OBS-NEW Power Works Method 1-7 grounding no designado
- 4 OBS-NEW Cable Schedule (VFD comms, IN REMOTE dosing, switches nomenclatura, PHIT09-006 tag)
- Cross-NT-001: 2.10 ITP ASME X + 2.12/2.13 Cartridge V unilateral

---

## 6. Cross-checks por disciplina

### 6.1 Eléctrica (E42)
- Electrical Load List Rev B (Doc 1) vs Single Line Diagram Rev B (Doc 4): cargas listadas presentes en SLD, capacidades coherentes
- Power Cable Schedule Rev B (Doc 2) vs Load List + SLD: secciones apropiadas, caída tensión <3% (Cable Schedule reporta 1.62% peor caso CIP Pump) ✅
- Pt-100 motores ET §5.3 L1032: **NO declarado explícitamente en Load List Rev B** — OBS-NEW
- Datasheet Cable Rev B (Doc 3): cumplimiento IEC 60228, EN 50525, certificaciones UL/CE/RoHS ✅
- Grounding Rev E vs Typical Power Works Rev C: Power Works adopta IEC 60364-5-54 (Doc 7 cierra); Grounding Rev E sigue sin cronograma completo per NCh Eléct. 4/2003 (Doc 5 abierto)
- Cable Tray Rev C: cierra todos los items históricos con evidencia específica (rows 1-5 del Consolidated Comment Sheet)

### 6.2 Instrumentación / Control (E43 + E44 doc 11)
- IO List Rev 1 (Doc 8) vs Instrument List Rev D (TM N18 Code 1): tags vibración + RTD presentes
- IO List Rev 1 vs Valve List Rev D (TM N18 Code 1): DI/DO válvulas instrumentadas
- IO List Rev 1 vs P&ID Rev D (TM N18 Code 1): CIT-09-004 reflejado (4-20mA, P9) ✅ Tracked IFC parcial
- IO List Rev 1 vs Control Philosophy Rev C (Code 3 abierto): **bandera IFC submission con lógica PLC no aprobada**
- Instrumentation Cable Schedule Rev 0 (Doc 11) vs IO List Rev 1: 4 OBS-NEW detectadas
- Protocolo señal 4-20mA + HART (ET §5.5 + memoria `project_hart_precedente.md`): verificar en datasheets si aplica

### 6.3 Quality (E44 docs 9-10)
- PQP Rev B (Doc 9) vs PIE Base ADASA P22-IT-09-000-001-0 Sections 5-11: inspection matrix incorporada
- PQP Rev B FAT scope + Acta de Aprobación FAT (BAE Cl. 31 pago 40%): incorporados ✅
- ITP Offsite Rev B (Doc 10) vs Technical Offer Rev1 ITP §12 ASME X: **silencio = no aceptado**
- ITP Offsite Rev B vs ET §7 (Engineering Submittals - PIE Detallado) + §8 (Inspections During Manufacturing) + §8.1 (Minimum FAT Scope)

### 6.4 Cartridge Filters (E45 docs 12-13)
- RO Cartridge Filter Rev D (Doc 12): FRP + Vertical + Sysflo + 22 cartuchos
- CIP Cartridge Filter Rev C (Doc 13): FRP + Vertical + Sysflo + 31 cartuchos
- ET Section 5.1.5 Cartridge Filter: material plástico ✅, retención 1 micrón ✅, longitud 40" ✅, diámetro 2.5" ✅, presión 10 bar ✅ (datasheet 7 bar), conexiones flangeadas ANSI B16.5 Cl 150 ✅
- Cross-NT-001 Section 3.5:
  - 5.A material justification SS316 — N/A (mantienen FRP, correcto)
  - 5.B datasheet completo — Sysflo datasheet adjuntado ✅ pero falta justificación FRP en feed brine ~40k ppm Cl⁻
  - 5.C drawing as-built container con configuración V — **NO adjuntado en E45**
  - 5.D ADASA pre-approval pre-PO — **incumplido**: BW Water cambió vendor a Sysflo unilateralmente
  - 5.E tie-ins inamovibles — **NO confirmado**: cambio H→V puede mover posiciones de conexiones

---

## 7. Banderas críticas y precedentes

### 7.1 IFC submission con Control Philosophy pendiente (Doc 8 IO List Rev 1)
Marca "Issued for Construction" en revisión 1 cuando la lógica del PLC (Control Philosophy Rev D) aún no está aprobada por ADASA. Si Rev D modifica permissives, sequence charts o setpoints, las señales IO declaradas IFC pueden quedar inconsistentes. **Condicionar aceptación**: "approval subject to Plant Control Philosophy Rev D final approval".

### 7.2 Silencio administrativo ASME X (Doc 10 ITP Offsite Rev B)
Patrón documentado en NT-001: BW Water plantea waiver verbal en mitigation plan pero la documentación contractual subsecuente (ITP Rev B) ni mantiene ni elimina el compromiso original. Posición ADASA: **el silencio no cambia el alcance contratado**. Code 3 con OBS reincidente.

### 7.3 Cambio unilateral pre-NT-001 (Docs 12-13 Cartridge Filters)
BW Water emitió Rev D y Rev C el 25-May (mismo día que ADASA emitió NT-001), materializando parte del cambio del mitigation plan (vendor nuevo Sysflo + configuración V) sin esperar respuesta. **Posición ADASA**: rechazar y exigir validación tie-ins + justificación material + equivalencia vendor antes de proceder con la PO Sysflo.

### 7.4 Reincidente Plant Control Philosophy
TM N15 NOTE-20 → TM N18 Section 2.1 OBS-01 CRITICAL → TM N19 Section 3 (esperaba Rev D, no entregada). 3º TM consecutivo con el mismo defecto (permissive HP Pump). Escalación contractual bajo C-4300 ya registrada en TM N18.

---

## 8. Cierres notables (no banderas, sino logros del TM N19)

- **Cable Tray Rev C cierra 100+ días**: este es el cierre más significativo del TM N19. Doc que estuvo Code 3 en TM N15 y se arrastraba desde TM N4 — finalmente todos los items respondidos.
- **PQP Rev B libera pago 40%**: cierra los 2 OBS críticos del TM N17 (inspection matrix + FAT scope). Sujeto a validación final del Acta de Aprobación FAT durante la implementación.
- **TM N3 OBS-01 RO Cartridge flow rate (110 días)**: cierra con Rev D (22 cartuchos = 2.23 m³/h/cartucho, dentro de recomendación 2 m³/h).
- **Power Works Rev C adopción IEC 60364-5-54**: gobernanza normativa coherente con SEC chilena.

---

## 9. Próximos pasos de redacción

Con este `_ANALISIS_TRABAJO.md` consolidado, la redacción del `P22-TM-09-000-019-0_TRANSMITTAL.md` puede proceder con:
1. EXECUTIVE SUMMARY: veredicto 3 — TO BE REVISED, 13 docs, tally 2 Code 1 + 6 Code 2 + 5 Code 3, drivers (5 listed in §3)
2. DETAILED OBSERVATIONS (13 sub-secciones 2.1-2.13): usar veredictos y justificaciones del §2 y §3 + cross-checks §6
3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS: usar §5 carry-forward + cierres notables §8
4. ATTACHMENTS: 5 CC_ADASA (solo los 5 Code 3 — Grounding, ITP, Cable Schedule, RO Cartridge, CIP Cartridge)
5. RESPONSE SUMMARY: tabla con código ADASA + verdict

Banderas críticas (§7) integradas en las sub-secciones correspondientes con tono firme sin pre-rechazo (lección NT-001).
