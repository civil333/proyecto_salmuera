# ANÁLISIS DE TRABAJO INTERNO — TM P22-TM-00-010-001-0 (ENTREGA 3 L&A)

**Documento de uso interno ADASA. NO se envía a L&A.** Trazabilidad del razonamiento que sustenta el transmittal en español a L&A Ingeniería y Proyectos.

**Fecha:** 19-May-2026 · **Entrega:** ENTREGA 3 · **Cover L&A:** 067-032-032-COR-TT-003 (15-May-2026, P. Castillo → E. Peralta)

---

## DISPOSICIÓN FINAL (prevalece sobre el detalle de análisis posterior)

| # | Documento (Rev B) | Veredicto | Driver |
|---|-------------------|-----------|--------|
| 1 | P22-MC-00-002-001 Fundación Estanque TK-06-001 | **3 — Por revisar** | Anclaje especificado como postinstalado (contradicción F1554/mecánico); rediseñar preinstalado según ACI 318-19 (OBS-01) |
| 2 | P22-MC-00-002-002 Fundación Dinámica Bomba BH-06-001 | **2 — Aprobado con comentarios** | Declarar recubrimientos y margen efectivo masa/frecuencia en Rev 0 |
| 3 | P22-MC-00-002-004 Fundación Contenedor RO | **2 — Aprobado con comentarios** | Reconciliar codificación/alcance y pesos vs TR Rev 1 en Rev 0 |
| 4 | P22-MC-00-002-005 Fundación Sistema CIP | **2 — Aprobado con comentarios** | Anclaje (postinstalado) DIFERIDO por falta de datos del proveedor — no es rechazo (PEND-03); reconciliar código y NPT; pesos dosificación ≈550 kg |
| 5 | P22-MC-00-003-001 Cubierta Metálica Sistema CIP | **3 — Por revisar** | Inconsistencia de clasificación de suelo (D en cubierta vs E en fundaciones); protección C5-M no abordada |

**Veredicto global del transmittal: 3 — POR REVISAR.** Recuento: **3 Código 2 (MC-002, MC-004, MC-005) + 2 Código 3 (MC-001, MC-003-001)**. Determinantes del Código 3: MC-001 (anclaje preinstalado/colado en sitio ACI 318-19) y MC-003-001 (clasificación de suelo D/E + C5-M). **Cambio 19-May-2026 (decisión usuario):** MC-005 OBS-01 baja de Crítico/Código 3 a condición diferida (Menor) — L&A no tiene los planos/fichas finales del proveedor de equipos CIP; los anclajes serán postinstalados; es aceptable si cumplen las solicitaciones; en seguimiento como PEND-03. **Formato ejecutivo:** transmittal y comentarios CC_ADASA comprimidos a directivas de una línea / recuadros ≤ ~8 líneas (Defecto/Corregir/Requisito), estructura ADASA de 5 secciones intacta.

**Pendientes a Sección 3 (no degradan ningún documento entregado):**
- PEND-01 — MC Sistema de Drenajes (P22-MC-00-002-003, exigida por Términos de Referencia — Sección 6), y planos asociados de fosa y canalizaciones, no incluidos en ENTREGA 3. Por decisión del proyecto se trackea como **pendiente informativo** (se entiende que L&A la entregará en una entrega posterior); no se trata como brecha crítica en este transmittal.
- PEND-02 — Las cargas basales del estanque TK-06-001 que usa MC-001 dependen de la ratificación de la Memoria de Cálculo Exfibro Rev B (consulta técnica P22-CT-06-000-002-0, abierta a Exfibro/Anwo). MC-001 ya adoptó el valor corregido por ADASA (Ez ±3.357 kgf) — consistente con la línea base interna P22-IT-06-000-005-0 — pero la fuente Exfibro aún no formaliza Rev B.
- PEND-03 — La verificación de anclajes de MC-005 (Sistema CIP) depende de los planos/fichas finales del proveedor de equipos CIP, aún no disponibles. Los anclajes serán postinstalados; se acepta diferir la verificación (no es rechazo): completar con anclajes postinstalados dimensionados a las cargas (ACI 318-19 Cap. 17/Sección 17.10; precalificación sísmica ACI 355.2/355.4 Cat. 1 + ESR ICC-ES) cuando se disponga de los datos. En seguimiento hasta Rev 0.

**Decisiones de criterio aplicadas (confirmadas con el usuario 19-May-2026):**
1. MC Drenajes ausente → pendiente informativo (entrega posterior), no brecha crítica.
2. ACI 318-14 vs ACI 318-19 (exigido por TR) → **NOTA transversal** en cada MC: L&A debe demostrar que la verificación de anclajes/hormigón armado con ACI 318-14 no cambia o es conservadora frente a ACI 318-19; si no lo demuestra, re-verificar con ACI 318-19 en la próxima Rev. No se eleva a OBS por defecto.
3. Reasignación fundación compartida (TR -004) → dos fundaciones independientes (-004 contenedor, -005 CIP): se **acepta el enfoque** de independencia estructural (coherente con Minuta 067-032-032-COR-MI-001 ítem 1.7); OBS de codificación para reconciliar títulos/códigos y formalizar -005 vía actualización de la lista de entregables 067-032-032-COR-LI-001.
4. Base normativa sísmica: revisión contra NCh 2369:2025. Base Of.2003 heredada de antecedentes → NOTA si se demuestra ≥ conservadora; OBS si no.
5. **Redacción directiva en todo el transmittal** (confirmada 19-May-2026): cada OBS/NOTA de las 5 MC se redacta como directiva de corrección (defecto factual + `Corregir:`/`Acción:` imperativo + `Requisito:`), sin frases de opinión ("se acepta", "no se objeta", "se reconoce"). Aplica feedback global [[feedback_comentarios_directivos]].
7. **OBS-NPT transversal Mayor (multi-audit, 19-May-2026) en MC-001/-002/-004/-005.** Auditoría multi-audit `auditar` (10 agentes) del transmittal vs ENTREGA 3 + equipo Exfibro + cortes Van Doorn (Imágenes 2/3) + TR. Hallazgo nuclear (confianza ALTA, consenso de los 10): ninguna de las 5 MC declara NPT/cota; todas usan "Modelo Navis Referencial" (que el TR degrada a consulta, planos 2D prevalecen); el TR (Secciones 3.3.1, 4.1, 2.1.3) hace el NPT dato fijo y exige verificarlo contra el Levantamiento DIO Abr-2026 antes de Rev A; el transmittal no lo traccionaba. Doble N.T.N. **+5,75 (zona estanque/bomba, P22-DWG-06-005-101) vs +6,00 (zona módulo/CIP, P22-DWG-06-005-103 VISTA A)**, escalón ≈0,25 m — redactado como **"a confirmar"** (puede ser desnivel intencional de plataformas, no necesariamente error). Severidad **Mayor**, encuadre declarar+verificar: MC-001 absorbe la OBS en su Código 3; MC-002, MC-004 y MC-005 mantienen Código 2 (declaración/verificación incorporable, condición previa a Rev A). **Recuento al cierre (ver decisión 11 / Disposición Final): 3 Código 2 (MC-002, MC-004, MC-005) + 2 Código 3 (MC-001, MC-003-001)** — MC-005 fue reclasificada a Código 2 el 19-May-2026 (anclaje diferido PEND-03), drivers del veredicto global son MC-001 y MC-003-001. Adicional MC-002 NOTA-07: la memoria no declara el peso de BH-06-001 (montaje lo rotula 250 kg); reconciliar contra ficha técnica KSB y rehacer ACI 351.3R — escala a Código 3 solo si el recálculo no cumple. **Corrección anti-alucinación (Verificador + Auditor Sombra):** el "~400 kg" inicial NO era rastreable a las fuentes auditadas (MC-002 no declara peso); reformulado a "peso no declarado; montaje rotula 250 kg; reconciliar contra ficha técnica". Cotas leídas de imágenes de corte → indicativas (no exactas). Comparación geométrica 3010 vs 2770 → posible no homología, planteada como aclaración, no discrepancia dura. Van Doorn citable a L&A en el stream OOCC porque el propio TR los nombra como antecedente vinculante (a diferencia del stream BW Water, regla CLAUDE.md Sección 3.7) — ver [[reference_van_doorn_oocc_citable]].
8. **Criterio metodológico — ADASA declara el valor vinculante; no se pide a L&A confirmar la fuente (corrección transversal 19-May-2026).** El cruce de un dato (peso, cota, reacción) contra su fuente vinculante (plano BW Water P22-DWG-09-005-001 Rev A, TR Rev 1 Sección 2.1.2, ficha técnica del fabricante, Exfibro, P22-IT-06-000-005-0) es deber de revisión de ADASA. Las observaciones declaran el valor + fuente que ADASA verificó y **exigen** que L&A lo adopte/declare; se prohíbe "confirmar que coincide con X", "reconciliar contra… y dejar trazado el valor asumido", "el valor asumido es conservador pero debe quedar trazado". Aplicado a: MC-004 NOTA-08 (contenedor RO = 14.934 kg, TR Sección 2.1.2 / plano P22-DWG-09-005-001 Rev A), MC-005 NOTA-07 (el supuesto de 500 kg se **acepta por conservador, sin recálculo**, pero se marca como no correcto; valores correctos declarados: TK-09-002 = 490 kg, BDS-09-001/002 = 57,4 kg, TR Sección 2.1.2 — ajuste de redacción confirmado por el usuario 19-May-2026), MC-002 NOTA-07 (ficha técnica KSB + divergencia 250 vs ~400 kg), MC-001 NOTA-03 (reacciones de P22-IT-06-000-005-0). Excepción: las verificaciones que el TR asigna explícitamente al consultor (NPT vs Levantamiento DIO antes de Rev A — OBS-NPT) sí se le exigen, porque ahí la obligación es contractual del consultor. Ver feedback global [[feedback_adasa_declara_valor_vinculante]].
9. **MC-004 NOTA-07 eliminada (alcance contenedor, no CIP).** MC-004 es solo fundación del contenedor RO; las cargas del estanque/equipo de dosificación (Sistema CIP) que la memoria incluía no le corresponden. NOTA-07 (pesos dosificación) se suprime; el punto se consolida en **OBS-01** (codificación/alcance), cuyo `Corregir:` ahora exige retirar esas cargas — se verifican en MC-005 con los pesos del TR Sección 2.1.2. MC-004 sigue Código 2 (corrección documental/de alcance, conservadora, Rev-0). Anotaciones MC-004: OBS-01/02/03 + NOTA-01/02/08 (6, sin NOTA-07).
10. **Español 100 % en comentarios (CLAUDE.md Sección 3.4).** Reemplazada en `.md`, `crear_transmittal.py` y los 5 scripts de anotación la terminología inglesa de anclajes, planos y fichas por su equivalente español: anclaje preinstalado (colado en sitio) / postinstalado; cabeza hexagonal pesada; plano civil y de cargas; ficha técnica. Conservados los códigos y marcas (ASTM/ACI/NCh/ISO/AISC/ICC-ES/PROFIS/KSB/Exfibro/Navis/DIO).
6. **MC-001 anclaje preinstalado (OBS-01, Mayor) → MC-001 reclasificada Código 3.** La memoria especifica F1554 Gr.36 + cabeza hexagonal pesada + empotramiento 30 cm (= perno preinstalado con cabeza) pero lo verifica como anclaje mecánico postinstalado (PROFIS, ACI 318-14): contradicción interna. Por constructibilidad (perforación postinstalada en losa con doble malla Ø16@150 y patrón de pernos fijo Exfibro BCD 2755 → interferencia con armadura, GPR, inspección especial continua ACI 318-19 Cap. 26, especialista en sitio remoto, no justificado en fundación nueva) y por normativa (postinstalados en zona sísmica alta exigen precalificación ACI 355.2/355.4 Cat. 1 + ESR ICC-ES; preinstalado se diseñan directo por Cap. 17 y Sección 17.10), se exige rediseñar preinstalado según ACI 318-19. Cambio de diseño sustantivo → Rev B.1, no incorporación en Rev 0. El antiguo NOTA-03 (patrón de anclaje) se absorbe en OBS-01. Lógica del usuario validada con investigación dirigida (citas: ACI 318-19 Cap. 17 / Sección 17.10, ACI 355.2/355.4, ASTM F1554; subnumerales no citados por no verificados). Encuadre: ACI 318-19 sí permite postinstalados — se exige preinstalado *para este caso*, no como prohibición de norma.

---

## CONTRASTE DE ALCANCE — TR Sección 6 vs ENTREGA 3 real

Términos de Referencia P22-TR-00-010-01-1 — Sección 6 (líneas 794–833 del extracted.md) exige 5 Memorias de Cálculo:

| TR Sección 6 | ENTREGA 3 (cover 067-032-032-COR-TT-003) | Estado |
|--------------|------------------------------------------|--------|
| P22-MC-00-002-001 Fundación estanque TK-06-001 | ítem 1 — P22-MC-00-002-001 Rev B | ✓ entregado |
| P22-MC-00-002-002 Fundación bomba BH-06-001 (ACI 351) | ítem 2 — P22-MC-00-002-002 Rev B | ✓ entregado |
| **P22-MC-00-002-003 Sistema de drenajes — fosa TK-06-002 y red de cámaras CD-06-00N** | — | ✗ no entregado → PEND-01 |
| P22-MC-00-002-004 Fundación compartida | ítem 3 — P22-MC-00-002-004 Rev B (cuerpo: "Fundación Contenedor RO"; cover: "Fundación Compartida Contenedor RO + Sistema CIP") | ⚠ codificación/alcance — OBS |
| — (no previsto en TR) | ítem 4 — P22-MC-00-002-005 Rev B "Fundación Sistema CIP" | ⚠ código no previsto — OBS |
| P22-MC-00-003-001 Cubierta metálica CIP | ítem 5 — P22-MC-00-003-001 Rev B "Cubierta Metálica Sistema CIP Exterior" | ✓ entregado |

La fundación compartida del TR se materializó como dos fundaciones independientes. El enfoque de independencia se acepta (Minuta MI-001 ítem 1.7). La traza documental requiere reconciliarse (OBS en MC-004 y MC-005).

---

## VERIFICACIÓN HALLAZGO POR HALLAZGO

### MC-001 — Fundación Estanque TK-06-001 — **Código 3**

| Hallazgo | Severidad | Estado | Evidencia (md líneas) |
|----------|-----------|--------|------------------------|
| Ez vertical = 3.357 kgf, M volcante = 431.846 kgf·cm, pesos 585/11.986 kgf | — | **Consistente** con línea base ADASA P22-IT-06-000-005-0 (Ez ±3.357; M 431.846; W 586/11.986). L&A adoptó el valor corregido. | MC-001 ll.304, 318, 267, 285 |
| "Pernos de anclaje **mecánicos** de 1\", tipo cabeza hexagonal pesada, ASTM F1554 Gr.36, empotramiento 30 cm", PROFIS ACI 318-14, FU 68 % | **OBS-01 Mayor** | Contradicción: F1554 + cabeza + 30 cm = preinstalado, no mecánico postinstalado. Postinstalado inviable (interferencia armadura doble malla, patrón fijo Exfibro, GPR, inspección especial, especialista sitio remoto). Rediseñar preinstalado por ACI 318-19 Cap. 17 + Sección 17.10; reconciliar patrón con plano Exfibro EX-26005-F01 Rev C (absorbe ex NOTA-03). Cambio de diseño → Rev B.1. | MC-001 ll.438, 440, 442 |
| Verificación de anclajes/HA con ACI 318-14; TR exige ACI 318-19 | NOTA-01 Mayor | Anclaje redisenado por ACI 318-19 directo; resto HA: demostrar equivalencia o re-verificar 318-19 | MC-001 l.438 |
| Recubrimientos 50/70 mm no declarados | NOTA-02 | TR exige 50 mm expuesto / 70 mm contacto terreno; declarar | (ausente en texto) |
| Origen de reacciones basales no declarado en la memoria | NOTA-03 (ex NOTA-04) | Declarar que son la versión corregida ADASA del antecedente Exfibro, citando fuente; ratificación Exfibro Rev B la gestiona ADASA (PEND-02) | MC-001 ll.260, 302, 436 |
| NCh 2369:2003 + :2025 listadas; adopta :2025; parámetros de suelo tipo E justificados | NOTA-04 (ex NOTA-05) | Declarar que las fuerzas heredadas de Exfibro (base 2003) están acotadas/conservadoras vs :2025, o reconciliar | MC-001 ll.216–220 |
| Cargas dependen de Exfibro Memoria Rev B | — | PEND-02 (Sección 3) | MC-001 ll.260, 302, 436 |

Determinante de veredicto (CLAUDE.md Sección 6.2): el rediseño del anclaje (preinstalado vs postinstalado) es un cambio de diseño sustantivo de la propia memoria — no es incorporación cosmética en Rev 0 → exige nueva revisión → **Código 3 — Por revisar (Rev B.1)**.

### MC-002 — Fundación Dinámica Bomba BH-06-001 — **Código 2**

| Hallazgo | Severidad | Estado | Evidencia |
|----------|-----------|--------|-----------|
| ACI 351.3R-04 aplicado (fundación dinámica) | — | **Conforme** TR (exige ACI 351.3R) | MC-002 l.147 |
| Relación masa fundación/equipo ≥ 3; separación frecuencia ±20 % vs 50 Hz | NOTA-06 | Criterio correcto; resultados numéricos en figuras — reportar el margen efectivo logrado | MC-002 ll.407, 415 |
| Presiones contacto 0,17 / 0,29 < 1,0 kgf/cm²; 100 % / 92,38 % apoyo | — | Conforme (criterio 100 %/80 %) | MC-002 ll.391, 401 |
| Cita ACI 318-14 vs TR 318-19 | NOTA-01 | Transversal | MC-002 l.145 |
| Recubrimientos no declarados | NOTA-02 | Declarar en Rev 0 | (ausente) |

→ **Código 2** (sólido; comentarios documentales a Rev 0).

### MC-004 — Fundación Contenedor RO — **Código 2**

| Hallazgo | Severidad | Estado | Evidencia |
|----------|-----------|--------|-----------|
| Título cuerpo "Fundación Contenedor RO" vs cover "Compartida Contenedor RO + Sistema CIP" vs TR -004 "Fundación compartida"; incorpora estanque/equipo dosificación (alcance CIP) | OBS-01 Mayor (documental) | Reconciliar título/código/alcance; formalizar split independiente (Minuta MI-001 1.7) y código -005 vía 067-032-032-COR-LI-001 | MC-004 ll.7, 10, 308; cover ll.16–17 |
| "ACI 318-10" en diseño de pedestales vs "ACI 318-14" en listado de códigos | OBS-02 Menor | Unificar versión; reconciliar con TR (ACI 318-19, ver NOTA-01) | MC-004 ll.155, 444 |
| Pesos estanque/equipo dosificación asumidos 500 kg c/u "no especificado en TR" | NOTA-07 | TR Rev 1 reconcilió pesos CIP; reconciliar. Valor conservador frente a TR Rev 1 pero debe trazarse | MC-004 l.308 |
| Peso contenedor RO empleado | NOTA-08 | Confirmar vs plano BW Water P22-DWG-09-005-001 Rev A / tabla de pesos TR Rev 1 (no explicitado en texto) | MC-004 l.306 |
| Presiones 0,44 / 0,63 < 1,0; 100 % apoyo ambos casos | — | Conforme | MC-004 ll.420, 430 |
| ACI 318-14 vs TR 318-19; recubrimientos | NOTA-01 / NOTA-02 | Transversal | MC-004 l.155 |

Enfoque de independencia aceptado; reconciliación es documental → incorporable en Rev 0, sin nueva Rev B → **Código 2**.

### MC-005 — Fundación Sistema CIP — **Código 3**

| Hallazgo | Severidad | Estado | Evidencia |
|----------|-----------|--------|-----------|
| **"Diseño de pernos de anclaje … esta no ha sido realizada … queda pendiente hasta disponer de la información correspondiente."** | OBS-01 Crítico | Entregable incompleto: el TR exige diseño de anclajes/previsión pernos químicos. Completar con fichas técnicas/cargas de equipos CIP y re-emitir | MC-005 l.425 |
| Código -005 "Fundación Sistema CIP" no previsto en TR Sección 6 | OBS-02 Mayor (documental) | Formalizar split y código vía 067-032-032-COR-LI-001 (ver MC-004 OBS-01) | MC-005 ll.7, 12 |
| Pesos dosificación 500 kg | NOTA-07 | Reconciliar vs TR Rev 1 | MC-005 l.289 |
| Presiones 0,41 / 0,45 < 1,0; 100 % apoyo | — | Conforme | MC-005 ll.405, 419 |
| ACI 318-14 vs TR 318-19; recubrimientos; base sísmica | NOTA-01 / NOTA-02 / NOTA-05 | Transversal | MC-005 ll.145, 207–211 |

Verificación obligatoria incompleta → nueva Rev requerida → **Código 3**.

### MC-003-001 — Cubierta Metálica Sistema CIP — **Código 3**

| Hallazgo | Severidad | Estado | Evidencia |
|----------|-----------|--------|-----------|
| Suelo tipo **D** (To 0,60; T1 0,41; r 3,5) y Cv 0,74; las MC de fundaciones usan suelo tipo **E** y Cv 0,45 para el mismo emplazamiento | OBS-01 Mayor | La clasificación de suelo del sitio (informe LNS-ADASA-INF-040) debe ser única y consistente entre memorias; reconciliar y re-verificar demanda sísmica de la cubierta | MC-003-001 ll.214–220; MC-001 l.212 |
| Sistema de pintura/protección C5-M (ISO 12944-2/-5) no abordado | OBS-02 Mayor | TR exige protección C5-M para estructura metálica en ambiente marino; declarar o referir explícitamente a ET Estructura Metálica P22-ET-00-010-103-0 | (ausente en texto) |
| "NCh427/1 2006" en normativa vs "NCh427/1 2016 / AISC 360-2016" en análisis | OBS-03 Menor | Unificar versión aplicada | MC-003-001 ll.136, 419 |
| FU máx 57,5 %; deformaciones OK; fundaciones (zapata/pedestal/anclaje) OK; contacto 0,34 / 0,69 < 1,0; 87 % contacto sísmico | NOTA-09 | Verificaciones estructurales conformes; observaciones acotadas a suelo, protección y consistencia normativa | MC-003-001 ll.555, 581, 726–730 |
| ACI 318-14 vs TR 318-19; recubrimientos | NOTA-01 / NOTA-02 | Transversal | MC-003-001 l.154 |

Inconsistencia de clasificación de suelo entre memorias del mismo sitio + C5-M → nueva Rev requerida → **Código 3**.

---

## ANOTACIÓN PDF POR VEREDICTO (CLAUDE.md Sección 3.8)

| Documento | Veredicto | Anotaciones CC_ADASA |
|-----------|-----------|----------------------|
| MC-001 | Código 3 | OBS-01/02 + NOTA-01/02/03/04 (todas; OBS-02 = NPT) |
| MC-002 | Código 2 | OBS-01 + NOTA-01/02/05/06/07 (OBS-01 = NPT; NOTA-07 = peso BH-06-001) |
| MC-004 | Código 2 | OBS-01/02/03 + NOTA-01/02/08 (OBS-03 = NPT; NOTA-07 eliminada — alcance contenedor, folded en OBS-01) |
| MC-005 | Código 2 | OBS-01 (anclaje diferido, Menor) + OBS-02/03 + NOTA-01/02/05/07 (OBS-03 = NPT; NOTA-07 = pesos dosificación ≈550 kg) |
| MC-003-001 | Código 3 | OBS-01/02/03 + NOTA-01/02/09 (todas; sin OBS-NPT — alcance las 4 MC de fundación) |

Ningún documento es Código 1 → todos llevan CC_ADASA. PDFs fuente normalizados desde `ENTREGAS\ENTREGA 3\`. Anclaje por `page_fallback` (0-based, derivado del índice de cada MC) — los PDF de memoria de cálculo tienen figuras/tablas densas; `search=None` evita fallos de búsqueda (memoria `feedback_doc_annotator_page_fallback_0based`). Texto FreeText en español, sin etiqueta de criticidad (el color del recuadro transmite severidad).
