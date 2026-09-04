# Revision Tecnica - Entrega 9 BW Water

**Submittal:** 25007-0009
**Fecha Emision:** 20-Ene-2026
**Fecha Revision:** 26-Ene-2026
**Revisor:** ADASA
**Version:** 1.0

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0009 |
| Fecha Emision | 20-Ene-2026 |
| Documentos | 5 |
| Tipos | ET (Datasheets), DWG (Planos), LI (Listas) |
| Submittal For | FA (For Approval) |
| Nota | Documentacion electrica: cables, bandejas, conduits, layout instrumentos |

---

## 2. Documentos Recibidos

| # | Codigo | Titulo | Rev | Tipo |
|---|--------|--------|-----|------|
| 1 | P22-ET-09-007-002 | Datasheet of Power & Control Cable | A | Datasheet |
| 2 | P22-ET-09-007-003 | Datasheet of Cable Tray | A | Datasheet |
| 3 | P22-ET-09-007-004 | Datasheet of Conduit & Flexible | A | Datasheet |
| 4 | P22-DWG-09-008-001 | Instrument Location Layout | A | Plano |
| 5 | P22-LI-09-007-002 | Power Cable Schedule | A | Lista |

---

## 3. Revision Documento 1: Power & Control Cable (P22-ET-09-007-002-A)

### 3.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-007-002-A |
| Titulo | Datasheet of Power & Control Cable |
| Fecha | 19-Ene-2026 |
| Fabricantes | MasterTec (Power/Control), Belden (Ethernet) |

### 3.2 Tipos de Cable Especificados

| Tipo | Modelo | Voltaje | Temp. Op. | Aislacion | Cumple |
|------|--------|---------|-----------|-----------|--------|
| Power Cable | Cu/XLPE/PVC | 600/1000V | 90°C | XLPE/PVC | **SI** |
| Control Cable | Cu/XLPE/PVC | 450/750V | 70°C | XLPE/PVC | **SI** |
| Grounding Cable | Cu/PVC | - | 70°C | PVC | **SI** |
| Instrument Cable | Cu/PVC/OSCR/PVC | 500V | 70°C | PVC (shielded) | **SI** |
| Ethernet Cable | Cat 6+ (Belden 2412) | 300V | -20 to 75°C | Polyolefin | **SI** |

### 3.3 Verificacion vs ET P22-ET-09-000-001-0 Seccion 5.3

| Requisito ET | Valor Requerido | Valor Entregado | Cumple |
|--------------|-----------------|-----------------|--------|
| Conductor | Cobre | Copper (Stranded Plain Annealed) | **SI** |
| Voltaje Power | 600/1000V | 600/1000V | **SI** |
| Voltaje Control | 450/750V | 450/750V | **SI** |
| Blindaje Instrumentacion | Overall Screen | Cu/PVC/OSCR/PVC (shielded) | **SI** |
| Ethernet | Cat 6 min | Cat 6+ Enhanced (350MHz) | **MEJOR** |

### 3.4 Especificaciones Power Cable

**MasterTec Cu/XLPE/PVC:**
- Conductor: Stranded Plain Annealed Copper
- Insulation: XLPE (Cross-linked Polyethylene)
- Outer Sheath: PVC, Black
- Operating Temperature: 90°C
- Nominal Voltage: 600/1000V
- Core Identification:
  - 3G: Brown, Blue, Green
  - 4G: Brown, Black, Grey, Green
  - 5G: Brown, Black, Grey, Blue, Green

### 3.5 Especificaciones Control Cable

**MasterTec Cu/PVC/PVC:**
- Conductor: Stranded Plain Annealed Copper
- Insulation: PVC
- Outer Sheath: PVC, Black
- Operating Temperature: 70°C
- Nominal Voltage: 600/1000V
- Core Identification: White with Black numberings

### 3.6 Especificaciones Instrument Cable

**MasterTec Cu/PVC/OSCR/PVC:**
- Conductor: Stranded Plain Annealed Copper
- Insulation: PVC
- Shield: Laminated aluminum polyester tape with tinned copper drain wire
- Outer Sheath: PVC, Black
- Operating Temperature: 70°C
- Nominal Voltage: 500V
- Core Identification: White and Black with numberings

### 3.7 Especificaciones Ethernet Cable

**Belden 2412 Cat 6+ Enhanced:**
- Conductor: 23 AWG Solid BC (Bare Copper), 4 pairs
- Insulation: Polyolefin (PO)
- Outer Jacket: PVC, 0.224" (5.69 mm) diameter
- Performance: 350 MHz (enhanced Cat 6)
- Temperature: -20°C to +75°C
- Voltage Rating: 300V (CMR)
- Compliance: TIA-568.2-D Category 6, ISO/IEC 11801-1
- IEEE: 802.3bt Type 1, 2, 3, 4 (PoE++)

### 3.8 Observaciones

Sin observaciones criticas. El cable Ethernet Cat 6+ excede requisitos minimos.

### 3.9 Veredicto Documento 1

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 4. Revision Documento 2: Cable Tray (P22-ET-09-007-003-A)

### 4.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-007-003-A |
| Titulo | Datasheet of Cable Tray |
| Fecha | 19-Ene-2026 |
| Fabricante | San Engineering |

### 4.2 Especificaciones Cable Tray

**San Engineering Full Return Flange (FRF):**

| Componente | Modelo | Ancho | Alto | Espesor | Material |
|------------|--------|-------|------|---------|----------|
| Cable Tray | SANSTFR | 100, 150, 200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| 90° Elbow | SANTFREL90 | 100, 150, 200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Equal Tee | SANTFRET | 100, 150, 200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Riser Inside 90° | SANTFRIR90 | 100, 150, 200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Riser Outside 90° | SANTFROR90 | 100, 150, 200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Left Reducer | SANTFRLR | 100-200 mm | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Splice Plate | - | - | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Cover w/U Clip | - | 100, 150, 200 mm | - | 1.5 mm | Steel, HDG, Epoxy |
| End Plate | - | - | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |
| Hold Down Clamp | - | - | 75, 100 mm | 1.5 mm | Steel, HDG, Epoxy |

**Radios disponibles:** 200-450 mm
**Longitud estandar:** 3000 mm

### 4.3 Verificacion Normativas

| Norma | Descripcion | Cumple |
|-------|-------------|--------|
| IEC 61537 | Cable management - Cable tray systems | **SI** |
| NEMA VE1 | Metal Cable Tray Systems | **SI** |
| NEMA VE2 | Cable Tray Installation Guidelines | **SI** |
| NEC ANSI/NFPA 70 | National Electric Code | **SI** |

### 4.4 Verificacion Acabado

| Acabado | Especificado | Cumple |
|---------|--------------|--------|
| Hot-Dip Galvanization (HDG) | ASTM A123 / ISO 1461 | **SI** |
| Epoxy Powder Coating | BS 3900 / ISO 2409 | **SI** |

### 4.5 Observaciones

Sin observaciones criticas. Documentacion completa con catalogo del fabricante.

### 4.6 Veredicto Documento 2

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 5. Revision Documento 3: Conduit & Flexible (P22-ET-09-007-004-A)

### 5.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-ET-09-007-004-A |
| Titulo | Datasheet of Conduit & Flexible |
| Fecha | 20-Ene-2026 |
| Fabricantes | Cantex (Conduit), Carlon (Flexible) |

### 5.2 Especificaciones Conduit Rigido

**Cantex Schedule 80 PVC Conduit:**
- Material: Rigid Nonmetallic PVC
- Sizes: 3/4", 1", 1-1/4", 1-1/2", 2"
- Color: Grey
- Resistance: Corrosion, Rust, Sunlight Resistant
- Compliance: UL651, NEMA TC-2, ETL Listed
- Temperature Rating: 90°C conductors

**Cantex Schedule 80 Fittings:**
- 90° Elbow (Plain End)
- 45° Elbow (Plain End)
- Center Stop Coupling
- Female Adapter
- Reducer Bushings
- Conduit Bodies Type C, T, LR, E
- Box Adapters
- Pipe Straps/Clamps

### 5.3 Especificaciones Flexible Conduit

**Carlon Carflex Liquidtight Flexible Conduit:**
- Material: PVC
- Type: LFNC-B (Liquidtight Flexible Nonmetallic Conduit)
- Sizes: 1/2", 3/4", 1"
- Color: Grey
- Resistance: Oil, acid, ozone, alkaline, crush, abrasion, strain resistant
- Compliance: UL Listed Article 356 NEC
- Temperature: 80°C dry, 60°C wet, 60°C oil resistant
- UL Listed: Outdoor use, Sunlight resistant, Direct bury (1/2", 3/4", 1")

**Carlon Carflex Fittings:**
- Straight Fittings: LT43D, LT43E, LT43F (1/2", 3/4", 1")
- 90° Fittings: LT20D, LT20E (1/2", 3/4")
- Compliance: UL Standard 514B

### 5.4 Verificacion Normativas

| Norma | Aplicacion | Cumple |
|-------|------------|--------|
| UL 651 | Rigid Nonmetallic Conduit | **SI** |
| NEMA TC-2 | Conduit Dimensions | **SI** |
| NEMA TC-3 | Fittings | **SI** |
| UL 1660 | Liquidtight Flexible Conduit | **SI** |
| UL 514B | Conduit Fittings | **SI** |
| NEC Article 356 | LFNC Installation | **SI** |

### 5.5 Observaciones

Sin observaciones criticas. Documentacion completa con catalogos de fabricantes.

### 5.6 Veredicto Documento 3

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 6. Revision Documento 4: Instrument Location Layout (P22-DWG-09-008-001-A)

### 6.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-DWG-09-008-001-A |
| Titulo | Instrument Location Layout |
| Fecha | 19-Ene-2026 |
| Escala | NTS (Not To Scale) |
| Paginas | 3 |
| Revision | A (Primera emision) |

### 6.2 Contenido del Documento

El documento presenta:
- Plan View del container con ubicacion de instrumentos
- Escala: NTS

### 6.3 Observaciones

| # | Observacion | Severidad | Categoria |
|---|-------------|-----------|-----------|
| OBS-01 | El plano esta a escala NTS. Para construccion se recomienda emitir version con escala definida y dimensiones acotadas de ubicacion de instrumentos. | Menor | Documental |

### 6.4 Veredicto Documento 4

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **2 - Approved as noted** |
| **VEREDICTO FINAL** | **2 - APPROVED AS NOTED** |

---

## 7. Revision Documento 5: Power Cable Schedule (P22-LI-09-007-002-A)

### 7.1 Identificacion del Documento

| Campo | Valor |
|-------|-------|
| Codigo | P22-LI-09-007-002-A |
| Titulo | Power Cable Schedule |
| Fecha | 14-Ene-2026 |
| Revision | A (Primera emision) |

### 7.2 Contenido del Documento

| # | TAG | Equipo | Potencia | Voltaje | Fases | Cable | Seccion | Long. | V Drop |
|---|-----|--------|----------|---------|-------|-------|---------|-------|--------|
| 1 | BH-09-001 | RO HP Feed Pump | 93.3 kW | 380V | 3 | Cu/XLPE/PVC | 4G x 95 mm² | 20m | 0.43% |
| 2 | REL-09-001 | CIP Heater | 20.0 kW | 380V | 3 | Cu/XLPE/PVC | 4G x 6 mm² | 20m | 1.21% |
| 3 | BH-09-002 | CIP Pump | 9.3 kW | 380V | 3 | Cu/XLPE/PVC | 4G x 4 mm² | 20m | 0.86% |
| 4 | BDS-09-001 | Antiscalant Pump A | 0.02 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 0.02% |
| 5 | BDS-09-002 | Antiscalant Pump B | 0.02 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 0.02% |
| 6 | SAI-09-001 | LCP PLC & Instr. | 1.0 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 0.73% |
| 7 | SSAA-09-001A | Light (Indoor) | 0.16 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 0.12% |
| 8 | SSAA-09-001B | Light (Outdoor) | 0.16 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 0.12% |
| 9 | SSAA-09-002 | A/C Unit | 1.86 kW | 220V | 1 | Cu/XLPE/PVC | 3G x 2.5 mm² | 20m | 1.37% |

### 7.3 Verificacion Caida de Tension

| Criterio | Limite | Valor Maximo Entregado | Cumple |
|----------|--------|------------------------|--------|
| Voltage Drop (Motores) | < 3% | 1.37% (A/C Unit) | **SI** |
| Voltage Drop (VFD) | < 3% | 0.86% (CIP Pump) | **SI** |
| Voltage Drop (HP Pump) | < 3% | 0.43% | **SI** |

**Evaluacion:** Todas las caidas de tension estan por debajo del limite aceptable del 3%.

### 7.4 Verificacion Cable Rating

| Equipo | Corriente Calc. | Rating Cable | Factor Servicio | Cumple |
|--------|-----------------|--------------|-----------------|--------|
| HP Pump | 164.42 A | 298 A (95 mm²) | 0.27 | **SI** |
| CIP Heater | 33.76 A | 54 A (6 mm²) | 0.63 | **SI** |
| CIP Pump | 16.39 A | 42 A (4 mm²) | 0.39 | **SI** |
| A/C Unit | 9.41 A | 32 A (2.5 mm²) | 0.29 | **SI** |

**Evaluacion:** Todos los cables tienen capacidad adecuada para las corrientes de operacion.

### 7.5 Verificacion Tipo de Alimentacion

| Equipo | Tipo Alimentacion | Especificado | Cumple |
|--------|-------------------|--------------|--------|
| HP Pump | VFD | VFD | **SI** |
| CIP Heater | Feeder 3P+N | FEEDER (3P+N) | **SI** |
| CIP Pump | VFD | VFD | **SI** |
| Dosing Pumps | Feeder 1P+N | FEEDER (1P+N) | **SI** |

### 7.6 Observaciones

Sin observaciones criticas. Dimensionamiento de cables es adecuado.

### 7.7 Veredicto Documento 5

| Aspecto | Veredicto |
|---------|-----------|
| Tecnico | **1 - Approved** |
| **VEREDICTO FINAL** | **1 - APPROVED** |

---

## 8. Verificacion de Codificacion

### 8.1 Analisis de Codigos

| Documento | Codigo | Formato P22-TT-AA-DDD-NNN-R | Cumple |
|-----------|--------|-----------------------------|----- ---|
| Power & Control Cable DS | P22-ET-09-007-002-A | P22-ET-09-007-002-A | **SI** |
| Cable Tray DS | P22-ET-09-007-003-A | P22-ET-09-007-003-A | **SI** |
| Conduit & Flexible DS | P22-ET-09-007-004-A | P22-ET-09-007-004-A | **SI** |
| Instrument Layout | P22-DWG-09-008-001-A | P22-DWG-09-008-001-A | **SI** |
| Power Cable Schedule | P22-LI-09-007-002-A | P22-LI-09-007-002-A | **SI** |

**Verificacion de campos:**
- P22: Codigo proyecto correcto
- ET/DWG/LI: Tipos de documento correctos
- 09: Area de proceso correcta (Osmosis Inversa)
- 007/008: Disciplina correcta (Electrico/Instrumentacion)
- NNN: Correlativo secuencial
- A: Revision correcta (Primera emision)

**Todos los documentos cumplen** con el sistema de codificacion P00-IT-00-000-101.

---

## 9. Resumen de Observaciones

| # | Documento | Descripcion | Categoria | Severidad |
|---|-----------|-------------|-----------|-----------|
| OBS-01 | P22-DWG-09-008-001-A | Plano a escala NTS, se recomienda version acotada | Documental | Menor |

---

## 10. Acciones Requeridas BW Water

| # | Accion | Documento | Prioridad | Plazo Sugerido |
|---|--------|-----------|-----------|----------------|
| 1 | Emitir plano de Instrument Location Layout con escala definida y dimensiones acotadas | P22-DWG-09-008-001 | Baja | Para construccion |

---

## 11. Veredicto Final de la Entrega

### 11.1 Resumen por Documento

| # | Documento | Veredicto |
|---|-----------|-----------|
| 1 | P22-ET-09-007-002-A Power & Control Cable | **1 - Approved** |
| 2 | P22-ET-09-007-003-A Cable Tray | **1 - Approved** |
| 3 | P22-ET-09-007-004-A Conduit & Flexible | **1 - Approved** |
| 4 | P22-DWG-09-008-001-A Instrument Location Layout | **2 - Approved as noted** |
| 5 | P22-LI-09-007-002-A Power Cable Schedule | **1 - Approved** |

### 11.2 Veredicto Consolidado

| Campo | Valor |
|-------|-------|
| **VEREDICTO ENTREGA 9** | **2 - APPROVED AS NOTED** |
| Documentos Approved | 4 |
| Documentos Approved as Noted | 1 |
| Documentos To Be Revised | 0 |
| Documentos Rejected | 0 |

**Justificacion:** La entrega contiene documentacion electrica de alta calidad. Los datasheets de cables, bandejas y conduits estan completos e incluyen catalogos de fabricantes reconocidos. El Power Cable Schedule demuestra un dimensionamiento correcto con caidas de tension aceptables. La unica observacion menor es el plano de ubicacion de instrumentos a escala NTS, que se recomienda emitir con dimensiones acotadas para construccion.

---

## 12. Documentos de Referencia

| Documento | Ubicacion |
|-----------|-----------|
| ET Modulo | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md |
| Oferta Tecnica Rev.1 | OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md |
| Codificacion General | BASES TECNICAS/md/P00-IT-00-000-101-CODIFICACION-GENERAL.md |
| IO List E8 | P22-LI-09-008-001-A |
| I&C Cable Schedule E8 | P22-LI-09-008-002-A |

---

*Fin del documento*
*Revision preparada: 26-Ene-2026*
