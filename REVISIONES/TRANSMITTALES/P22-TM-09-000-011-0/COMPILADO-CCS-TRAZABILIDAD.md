---
tipo: Trazabilidad CCS — Documento Interno
transmittal: TM N11 — P22-TM-09-000-011-0
entregas: E19 (25007-0019) / E20 (25007-0020) / E21 (25007-0021)
fecha: 17-Mar-2026
nota: DOCUMENTO INTERNO — NO ENVIAR A BW WATER
referencia_compilado: Compilado-TM-N11.md (análisis detallado por documento)
---

# TRAZABILIDAD CCS — ENTREGAS 19, 20 Y 21
## Consolidated Comment Sheets — Verificación ítem por ítem
## **NO ENVIAR — USO INTERNO ADASA**

---

## 1. Propósito y Alcance

Este documento verifica que las respuestas en los CCS de Entregas 19, 20 y 21 correspondan a correcciones reales en los documentos revisados. Se aplica la metodología establecida en TM N10 (verificación ítem por ítem, no solo confianza en el CCS).

**Criterios de veredicto:**
- **CERRADO:** Respuesta confirma acción realizada; documento muestra la corrección; TM N11 no levanta nueva observación sobre ese punto específico.
- **PARCIAL:** Respuesta reconoce el issue; acción ejecutada pero incompleta o con error secundario.
- **ABIERTO:** Respuesta genérica sin evidencia, o contradice lo observado en el documento.

---

## 2. Valve List Rev C — CCS (3 ítems)

**Submittal:** 6/3/2026 | **Documento:** P22-LI-09-005-002 Rev C → *3 — To be Revised*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 1 | TM N6 OBS-01 — VM-09-015/VE-09-008/VE-09-009/VM-09-065 duplicados | "Noted, Already revised on Valve List Rev. C" | **PARCIAL** | Los 4 duplicados originales están resueltos ✓. Sin embargo, Rev C introduce 2 nuevos duplicados: VE-09-007 (ítems 44 y 64) y PSV-09-002 (ítems 105 y 112) → TM N11 OBS-01 y OBS-02 |
| 2 | Todos los TAGs deben ser únicos | "All Valves have unique TAGs on Rev. C" | **ABIERTO** | La afirmación es incorrecta: Rev C contiene VE-09-007 duplicado (ítems 44/64) y PSV-09-002 duplicado (ítems 105/112). La declaración de unicidad no puede verificarse como correcta → requiere Rev D |
| 3 | VM-09-015 item 18: ON/OFF MOTORIZED contradice OBS-11 WITHDRAWN | "Already revised on Valve List Rev. C" | **CERRADO** | Item 18 renombrado a VM-09-151, MANUALLY ACTUATED VALVE ✓. Consistente con OBS-11 WITHDRAWN |

**Resumen Valve List CCS:** 1 CERRADO / 1 PARCIAL / 1 ABIERTO

**Coherencia con TM N11:** La respuesta "all valves have unique TAGs" es **INCORRECTA** — 2 nuevos duplicados introducidos. Este es el mismo patrón de riesgo que en Entrega 13 (Valve List Rev B): BW Water declara corrección pero introduce nuevos errores. El análisis documento-por-documento de ADASA detecta lo que el CCS no refleja.

**Ítem VM-07-005 (área 07):** No está en el CCS porque no fue parte de la respuesta explícita al ítems 1-3. Sin embargo, el TM N3 OBS-13 (TAGs área 07: VM-07-005, VM-07-031, VE-07-009) sigue sin resolverse en Rev C — VM-07-005 ítem 7 sigue mostrando área "07". Este error no forma parte del CCS de E19 porque no fue explícitamente señalado en TM N6; lo fue en TM N3 pero no se incluyó como ítem CCS corriente.

---

## 3. Equipment List Rev B — CCS (1 ítem)

**Submittal:** 25007-0008, 11/3/2026 | **Documento:** P22-LI-09-005-001 Rev B → *2 — Approved as Noted*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 1 | Discrepancias P&ID vs EL: TAG Static Mixer, CIP Tank 5.1 vs 6.1 m³, Antiscalant 0.27 vs 0.25 m³, Dosing Pump 2.3 vs 1 LPH | (1) MZE-09-001; (2) CIP 6.1 m³; (3) Antiscalant 0.27 m³ eff.; (4) HP Pump 125 hp = 93 kW; (5) Dosing 2.3 LPH | **CERRADO** | Todas las confirmaciones verificadas en el documento Rev B. El ítem sobre HP Pump 125 hp no era parte del comentario original del CCS pero BW lo incluyó proactivamente — valor agregado. Sin gaps residuales para este CCS. |

**Resumen EL CCS:** 1 CERRADO / 0 PARCIALES / 0 ABIERTOS

---

## 4. Painting Specifications Rev B — CCS (2 ítems)

**Submittal:** 5/3/2026 | **Documento:** P22-ET-09-006-2 Rev B → *1 — Approved*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 1a | RAL 5017 no coincide con ET §5.1.9 (RAL 5012 estructural) | ET §5.1.9 aplica a estructura (ítem 4 = RAL 5012); container es RAL 5017 | **CERRADO** | Verificado: ítem 4 = RAL 5012 ✓, ítem 12 container = RAL 5017 ✓. Distinción correcta. |
| 1b | DFT 350 µm → debe ser 355 µm | "Revised 350 µm to 355 µm for the container" | **CERRADO** | Verificado: ítem 12 = 355 µm ✓; ítem 4 = 355 µm (80+200+75) ✓ |

**Resumen Painting CCS:** 2 CERRADOS / 0 PARCIALES / 0 ABIERTOS

**Resultado:** Documento perfectamente corregido. Aprobado sin nuevas observaciones.

---

## 5. HP Pump Datasheet Rev D — CCS (1 ítem)

**Submittal:** 25007-0007, 12/3/2026 | **Documento:** P22-ET-09-009-002 Rev D → *2 — Approved as Noted*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 9 | (Comentario ADASA no visible en CCS) | "No 1800 psi coupling for 4 inch; BW will provide 2000 psi coupling instead. Coupling datasheet attached." | **CERRADO** | Style H 2000 psi adjunto para DN25-DN100 ✓. Margen sobre presión de proceso HP Pump (~710 psi): amplio. Inconsistencia interna (GE vs ABB equiv.) → NOTE-02, no impide aprobación. |

**Resumen HP Pump CCS:** 1 CERRADO / 0 PARCIALES / 0 ABIERTOS

---

## 6. Feed Turbocharger Datasheet Rev D — CCS (1 ítem)

**Submittal:** 25007-0008, 11/3/2026 | **Documento:** P22-ET-09-009-007 Rev D → *2 — Approved as Noted*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 5 | (Comentario ADASA no visible) | "BW has revised the turbocharger coupling. Datasheet of Coupling also attached." | **PARCIAL** | Style S/X 1800 psi para DN40 y DN50 adjunto ✓. TM N6 OBS-01 cerrado ✓. TM N10 OBS-06 (vibración): row 38 "vibration sensor mounting surface" ✓. Gap: outline drawing HPB-60 (p.6) sigue referenciando "CUT GROOVE STYLE 77" — debe actualizarse a Style S → NOTE-03 |

**Resumen Turbo 1 CCS:** 0 CERRADOS / 1 PARCIAL / 0 ABIERTOS (PARCIAL porque coupling datasheet adjunto pero outline drawing inconsistente)

---

## 7. Interstage Turbocharger Datasheet Rev D — CCS (1 ítem)

**Submittal:** 25007-0008, 11/3/2026 | **Documento:** P22-ET-09-009-008 Rev D → *2 — Approved as Noted*

| Item CCS | Observación original | Respuesta BW | Veredicto | Gap residual |
|----------|---------------------|--------------|-----------|--------------|
| 4 | (Comentario ADASA no visible) | "BW has attached the coupling datasheet" | **PARCIAL** | Idéntico a Turbo 1: Style S/X 1800 psi ✓ para DN40/DN50. TM N6 OBS-01 cerrado ✓. TM N10 OBS-07 (vibración): row 38 ✓. Gap: outline drawing con "STYLE 77" inconsistente → NOTE-04 |

**Resumen Turbo 2 CCS:** 0 CERRADOS / 1 PARCIAL / 0 ABIERTOS

---

## 8. Instrument Location Layout Rev B — CCS (8 ítems)

**Submittal:** TRANSMITTAL N3 ADASA-BW | **Documento:** P22-DWG-09-008-001 Rev B → *2 — Approved as Noted*

| Item CCS | Respuesta BW | Veredicto | Gap residual |
|----------|--------------|-----------|--------------|
| 1 | "Has been revised and added in RevB" | **CERRADO** | Sin gap |
| 2 | "Has been added in RevB" | **CERRADO** | Sin gap |
| 3 | "Has been added in RevB" | **CERRADO** | Sin gap |
| 4 | "Has been revised. I/O List revised to CIT-09-004." | **CERRADO** | Tag correcto ✓ |
| 5 | "Has been revised in RevB" | **CERRADO** | Sin gap |
| 6 | "Has been revised in RevB" | **CERRADO** | Sin gap |
| 7 | "RTD temperature element directly connected into PLC RTD module for continuous monitoring." | **CERRADO** | Motor RTDs en layout ✓ |
| 8 | "Has been revised and added in RevB" | **CERRADO** | Sin gap |

**Resumen Instrument Layout CCS:** 8 CERRADOS / 0 PARCIALES / 0 ABIERTOS

---

## 9. GA CIP Pump Rev A y GA Antiscalant Pump Rev A — Sin CCS

Primera entrega de ambos documentos. No hay CCS previo. Verificación de primera entrega.

---

## 10. Grounding Layout Rev B — CCS (cipher-encoded, parcialmente legible)

CCS indica incorporación de comentarios previos de TRANSMITTAL N3. Sin ítems verificables en detalle por limitación de extracción. Se acepta como Approved as Noted.

---

## 11. Tabla Resumen Consolidada

| Documento | CERRADO | PARCIAL | ABIERTO | Total |
|-----------|:-------:|:-------:|:-------:|:-----:|
| Valve List Rev C (3 ítems) | 1 | 1 | 1 | 3 |
| Equipment List Rev B (1 ítem) | 1 | 0 | 0 | 1 |
| Painting Specs Rev B (2 ítems) | 2 | 0 | 0 | 2 |
| HP Pump DS Rev D (1 ítem) | 1 | 0 | 0 | 1 |
| Turbo 1 DS Rev D (1 ítem) | 0 | 1 | 0 | 1 |
| Turbo 2 DS Rev D (1 ítem) | 0 | 1 | 0 | 1 |
| Instrument Layout Rev B (8 ítems) | 8 | 0 | 0 | 8 |
| **TOTAL** | **13** | **3** | **1** | **17** |

**Interpretación:** 76% CERRADO, 18% PARCIAL, 6% ABIERTO.

La alta tasa de cierre refleja que BW Water ejecutó la mayoría de las acciones requeridas. Los PARCIALes corresponden a acciones ejecutadas con gaps documentales secundarios (coupling style inconsistency en turbos) y el ABIERTO corresponde a la Valve List donde la afirmación "unique TAGs" es incorrecta en el documento entregado.

---

## 12. Candidatos TM N12

### 12.1 Crítico (observaciones activas que requieren resolución)

| Issue | Origen | Observación TM N11 | Acción requerida |
|-------|--------|-------------------|-----------------|
| VE-09-007 duplicado (ítems 44/64) | Valve List Rev C | OBS-01 (MAJOR) | Valve List Rev D: TAG único para cada válvula |
| PSV-09-002 duplicado (ítems 105/112) | Valve List Rev C | OBS-02 (MAJOR) | Valve List Rev D: Corregir ítem 112 a PSV-09-001 |
| VM-07-005 área-07 (ítem 7) | Valve List Rev C | NOTE-01 (MINOR) | Valve List Rev D: Corregir a VM-09-005 (y verificar VM-07-031, VE-07-009) |
| TE vs TIT motor tags | IO List/DTL | TM N10 OBS-01 | IO List Rev C + DTL Rev B |
| Conductivity ranges CIT-09-001/004/005 | DTL | TM N10 OBS-02 | DTL Rev B |
| Level alarms LS09-001/002 Modbus | DTL | TM N10 OBS-03 | DTL Rev B |
| UPS 8h autonomy | Control Arch | TM N10 OBS-04 | Confirmación escrita + cálculo |

### 12.2 Pendientes de primera revisión

| Issue | Origen | Observación TM N11 | Acción requerida |
|-------|--------|-------------------|-----------------|
| Coupling style inconsistency (STYLE 77 vs STYLE S) | Turbo 1+2 DS | NOTE-03, NOTE-04 | Actualizar outline drawing HPB-60 a Style S |
| Motor manufacturer inconsistency (GE vs ABB equiv.) | HP Pump DS | NOTE-02 | Rev E: reconciliar campo fabricante motor |
| Seismic anchor data CIP pump GA | GA CIP Rev A | NOTE-05 | Rev B: anchor bolt layout + reacción sísmica |
| Seismic anchor data Antiscalant pump GA | GA Antiscalant Rev A | NOTE-06 | Rev B: anchor bolt layout + reacción sísmica |
| Antiscalant Tank GA Rev B anchor layout | TM N10 OBS-05 | Pendiente | GA Rev B: datos sísmicos + anchor layout |
| HMI Screenshots P22-BREAD-09-008-001 | TM N10 NOTE-05 | Pendiente | Comprometido desde TM N4 |

---

## 13. Patrón de Documentación — Evaluación de Riesgo Valve List

| Patrón | Entrega 13 (Valve List Rev B) | Entrega 19 (Valve List Rev C) |
|--------|-------------------------------|-------------------------------|
| Comentario original ADASA visible en CCS | Parcialmente | Parcialmente (3 ítems, texto visible) |
| Corrección efectivamente aplicada al documento | **NO** (cero evidencia) | **PARCIAL** — 4 duplicados resueltos + 2 nuevos introducidos |
| Declaración de unicidad en CCS es correcta | N/A | **INCORRECTA** — 2 duplicados persisten |
| Veredicto | Code 4 REJECTED | Code 3 To be Revised |

**Conclusión:** La Valve List sigue siendo el documento más problemático del proyecto. En Rev C se resolvieron los 4 duplicados originales pero se introdujeron 2 nuevos. El patrón "fix one, break another" indica que BW Water no tiene un proceso de QA sistemático para verificar unicidad en la lista completa (112 ítems). En Rev D se debe aplicar una revisión completa de unicidad antes de entregar.

---

*Generado: 17-Mar-2026 | Revisado por: Luis Rivera | Para uso interno ADASA*
*Referencia: Compilado-TM-N11.md + PDFs extraídos de Entregas 19, 20 y 21*
