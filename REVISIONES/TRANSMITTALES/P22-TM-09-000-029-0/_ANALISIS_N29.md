# _ANALISIS_N29 (interno — NO ENVIAR)

TM N29 · submittal 25007-0067 (E67, 21-Jul) · 4 re-revisiones · veredicto global **2 — Approved as Noted**.
Register tras N29: **49 C1 / 29 C2 / 6 C3 / 0 C4**, 108 items / 84 delivered, 29 TMs / 67 entregas.

## Disposición por documento (con verificación adversarial + CCS (regla 6.5))

### 010 HP/LP Pressure Test Procedure Rev D (#105) — Code 2
- **Prev:** Rev C = Code 3 (N27), driver único = 75 bar de hidrotest sobre línea PVC DA-PVC-DN65-09-016.
- **Verificación:** clausula 5.5.12 (pág 7) diferencia HP 135 bar / LP 7,5 bar y cita la Line List Rev 0; la Line List embebida (págs 11-12) fija 09-016 a **diseño 2 / hidrotest 3 bar**; ninguna PVC >7,5 bar; 75 bar solo en Super Duplex; gap 5.7.2.2 corregido. **Crítico RESUELTO en la raíz.**
- **CCS (regla 6.5):** 4 ítems del N27 (OBS-01 75 bar PVC / OBS-02 transmitir Line List / OBS-03 presión en cuerpo / OBS-04 gap) declarados cerrados **y verificados en el cuerpo** (cierre real, no declarado).
- **Residual:** NOTE-01 — 3.1/3.2 (pág 4) citan ASME Section V / B31.3 "Applicable Edition/Addenda" sin fijar edición. → **Code 2**, CC_ADASA NOTE-01.

### 005-001 UHPRO Structural Calc Rev B (#108) — Code 2
- **Prev:** Rev A = Code 3 (N26), 7 comentarios.
- **Verificación (render de páginas-imagen):** corte basal **NCh 2369:2003 Zona 3 = 41,62 kN** (A0=0,40g, Cmax=0,34, coherente con STAAD); **utilización máx 0,454 < 1,0** (Fig.13); tensión 163,8 MPa < 207 admisible; warnings STAAD 3472/3473 = resorte débil benigno (solución completada); norma **2003 (no 2025)**; los 7 comentarios del N26 incorporados. **Adecuación estructural CONFIRMADA.**
- **CCS (regla 6.5):** responde los 7 comentarios; salvedad = la hoja de comentarios no reproduce el texto del comentario del cliente.
- **Residuales (housekeeping):** NOTE-01 — PDF duplicado (2 copias concatenadas, ~58 MB/1101 págs); NOTE-02 — CCS sin texto de comentarios. → **Code 2**, CC_ADASA NOTE-01/02 (anotado con PyMuPDF directo `garbage=1` por tamaño).

### 008-001 PLC/LCP Outline Panel Drawing Rev 0 IFC (#98) — Code 1
- **Prev:** Rev C = Code 2 (N27), 3 MINOR.
- **Verificación:** hoja 5 (Hoffman Material Spec) = exterior body/door/roof/plinth SS316L, mounting plate HDG, swing door CRS RAL7035, frame galvanizado, **NEMA 4X/IP66** = disposición RFI-002 exacta; gland plate SS316L + cable-clamps especificados (cierra OBS-01 N27); BOM TP1 = PLX32-EIP-MBTCP (cierra OBS-03); "CABLE ENTRY" corregido; SLD reemitido Rev 1 (cierra el compromiso cross-doc del N27).
- **CCS (regla 6.5):** 3 OBS + 1 Note del N27, todas respondidas y verificadas; Note-01 confirma SLD Rev 1.
- **Residuales (cosméticos, no degradan):** sello "ISSUED FOR APPROVAL" en un plano Rev 0 IFC; acabado mounting plate "zinc-plated" (hoja 3) vs "hot-dip galvanized" (hoja 5). → **Code 1**, sin CC_ADASA; cosméticos a la nota del Status; SLD Rev 1 a Sección 3.

### 009-003 Line List Rev 0 IFC (#38) — Code 1
- **Prev:** Rev C = Code 1 (N18).
- **Verificación:** único cambio de diseño = 09-016 **50→2 bar** (hidrotest 3); columna Hydrotest agregada (1,5×diseño); consistente con el **P&ID Rev D** (línea PVC = descarga de salmuera a drenaje, aguas abajo del turbocharger; los 50 bar viven en las líneas SDX del turbo) y con la Valve List Rev D. **Corrección técnicamente respaldada; reconciliación P&ID satisfecha.**
- **CCS (regla 6.5):** 1 ítem ("Added Hydrotest Pressure") **incompleto** — no declara la corrección 50→2 (silent slip, pero correcto).
- → **Code 1**, sin CC_ADASA; nota de Status: declarar la corrección de 09-016 en el historial de revisión.

## Verificaciones completadas
- Render Structural Calc (scratchpad) → corte basal + utilizaciones confirmados <1,0.
- Line List 09-016 vs P&ID Rev D (`ENTREGA 41\P22-DWG-09-009-002_D...pdf`) → consistente con 2 bar.

## Artefactos
- Transmittal: `crear_transmittal.py` → `TRANSMITTAL N29 ADASA-BW_WATER.docx` (+ PDF desde Word, 6 págs).
- CC_ADASA: `COMENTARIOS/agregar_comentarios_hplp_pressure_test.py` (010, NOTE-01) + `agregar_comentarios_structural_calc.py` (Struct Calc, NOTE-01/02, garbage=1).
- Register: `../../EVALUACIONES/update_register_n29.py` (49/29/6/0; backup `_pre-N29.xlsx`).
- Correo cobertura: `CORREOS/Julio 2026/2026-07-21/crear_correo_tm29.py`.
- Pendiente pre-envío: reemplazar `DOWNLOAD_LINK` (Synology) en el transmittal y el correo; `anti-ia revisar` sobre el `.md`.
