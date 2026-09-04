---
titulo: "Libro mayor de comentarios — ENTREGA 71 (25007-0071), cinco documentos en Rev 0"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-06
---

# Libro mayor de comentarios — ENTREGA 71

> Documento interno de trabajo. **NO ENVIAR.** Registra cada comentario que ADASA emitió sobre los cinco documentos de esta entrega y el estado de su cierre verificado contra la Rev 0.

## Alcance

La ENTREGA 71 (submittal `25007-0071`, recibida el 06-Ago-2026, retorno declarado 09-Ago) trae cinco documentos, **todos en Rev 0 emitidos IFC**. Son las re-emisiones finales de once ciclos de revisión repartidos en los transmittals N20, N23, N26, N27 y N29.

**38 comentarios emitidos en total.** De ellos, **33 requieren verificación**: 13 abiertos que la Rev 0 debía levantar y 20 en regresión, ya declarados cerrados pero que se re-verifican porque el proveedor tiene precedente documentado de perderlos al re-emitir. Los 5 restantes son declaraciones de cierre o notas informativas sin acción, y se conservan como contexto.

## Procedencia del texto

El texto literal de cada comentario se extrajo por análisis del árbol sintáctico de los diez scripts `COMENTARIOS/agregar_comentarios_*.py` de los transmittals de origen, que son la fuente de lo que efectivamente se escribió sobre el PDF anotado. No se usó el `.md` del transmittal, que parafrasea.

| Transmittal | Script | Comentarios |
|---|---|---|
| N20 | `agregar_comentarios_pmi_procedure.py` | 3 |
| N20 | `agregar_comentarios_visual_procedure.py` | 3 |
| N23 | `agregar_comentarios_hp_lp_pressure.py` | 2 |
| N23 | `agregar_comentarios_painting.py` | 7 |
| N26 | `agregar_comentarios_hp_lp_pressure.py` | 3 |
| N26 | `agregar_comentarios_uhpro_structural.py` | 7 |
| N27 | `agregar_comentarios_hp_lp_pressure.py` | 5 |
| N27 | `agregar_comentarios_painting.py` | 5 |
| N29 | `agregar_comentarios_hplp_pressure_test.py` | 1 |
| N29 | `agregar_comentarios_structural_calc.py` | 2 |

## Estados

| Estado | Significado | Exige cita |
|---|---|---|
| **CERRADO** | La cita del Rev 0 cubre íntegra la acción pedida | Sí |
| **PARCIAL** | La cita cubre parte, o el documento se contradice a sí mismo en otra página | Sí |
| **NO LEVANTADO** | El defecto sobrevive, o el proveedor hizo algo distinto de lo pedido | Sí, de la ausencia |
| **SIN CITA** | Transitorio. Ninguna entrada puede quedar así al cerrar el bucle | — |

Una respuesta del CCS del tipo *"Revised as per comment"* **no cierra nada por sí sola**. Sin cita del cuerpo del Rev 0, la entrada queda SIN CITA.

## Qué entrada decide el veredicto y cuál no

Los cinco documentos venían **de un Código 2**, que es una aprobación con condición acotada. **El veredicto de la Rev 0 lo deciden solo las entradas que eran esa condición** — doce en total, marcadas abajo como `CONDICIÓN`. Las 21 restantes pertenecen a ciclos ya cerrados y se verificaron únicamente para saber si el contenido se conservó: su resultado es **registro interno y no se emite**, porque degradar un documento aprobado con hallazgos que no eran la condición reabre una aprobación propia.

| Documento | Código 2 en | Entradas que son CONDICIÓN |
|---|---|---|
| PMI `-006` | N20, sobre Rev A | 1, 2, 3 |
| Visual `-008` | N20, sobre Rev A | 4, 5, 6 |
| HP/LP `-010` | N29, sobre Rev D | 17 |
| Painting `-011` | N27, sobre Rev B | 24, 25, 26 |
| Structural `-005-001` | N29, sobre Rev B | 34, 35 |

---

## 1. P22-BA-09-000-006 — PMI Procedure

Rev A revisada en el N20 con Código 2 y acción *"no new PMI Procedure revision required"*. Nunca se re-revisó: **las tres anotaciones llegan abiertas a la Rev 0**.

| # | ID | Origen | Tipo | Estado | Cita Rev 0 |
|---|---|---|---|---|---|
| 1 | OBS-01 | N20 | ABIERTO | **PARCIAL** | pág. 4: *"10 percent of the Super duplex high pressure piping component will be tested and witness by ADASA."* — declara el 10% y la testificación; **no** declara la conformidad UNS S32750 como base de aceptación (verificado: `S32750` aparece una sola vez en las 31 páginas y es en la comment sheet, pág. 30) |
| 2 | OBS-02 | N20 | ABIERTO | **NO LEVANTADO** | Sin declaración de aplicabilidad al proyecto. El procedimiento del subcontratista sobrevive íntegro con su alcance de refinería: pág. 14 *"PMI is the responsibility of a refinery or fabricator"*, pág. 16 *"Thermowells in HF Acid units"* y *"Fired heater external piping"*, pág. 21 filas *"Fired Heater / Reformer / Furnace"* |
| 3 | NOTE-01 | N20 | ABIERTO | **CERRADO** | pág. 4: *"PERSONAL QUALIFICATIONS / Refer to XPERT PMI procedure."* La cláusula copiada del NDE Plan desapareció; la calificación real del operador PMI vive en pág. 10 (*"manufacturer instruction in the use of the analyzer or sufficient classroom (1 day Internal with OEM Manufacturing Equipment)"* + *"PMI operator mock-up test shall be conducted and approved by Owner"*) |

**OBS-01** — `ET requirement not declared - PMI on at least 10 percent of the Super Duplex high-pressure circuit components, UNS S32750 conformity as acceptance basis, ADASA witness right (Punto W). Correct: add the project scoping clause at IFC Rev 0.`

**OBS-02** — `embedded subcontractor procedure scoped to refinery services (PTS, HF acid, fired heaters) not applicable to this module. Correct: add a project-applicability statement at IFC Rev 0.`

**NOTE-01** — `cover qualification clause is copied from the NDE Plan (refers to non-destructive examination personnel). Correct: replace with the PMI operator qualification defined in the body (OEM training + Owner-approved mock-up).`

Respuestas del CCS (páginas 30 y 31): OBS-01 *"Revised as per comment, Added in the scope."* · OBS-02 *"Revised as per comment."* · NOTE-01 *"Revised as per comment."*

---

## 2. P22-BA-09-000-008 — Visual Procedure

Rev A revisada en el N20 con Código 2 y acción *"no new Visual Procedure revision required"*. Igual que el PMI: **las tres llegan abiertas**.

| # | ID | Origen | Tipo | Estado | Cita Rev 0 |
|---|---|---|---|---|---|
| 4 | OBS-01 | N20 | ABIERTO | **CERRADO** | pág. 5, sección 5.1.1: *"Minimum qualification to perform visual inspection SNT-TC-1A VT level II."* Coherente con la base de personal del NDE Plan Rev C |
| 5 | OBS-02 | N20 | ABIERTO | **PARCIAL** | pág. 4, sección 2.0: *"visual inspection on all types of steel piping and structure welds"* — la Rev A decía *"steel and thermoplastic welds"*. La exclusión se ejecutó **borrando la palabra**: `thermoplastic` no aparece en el cuerpo (verificado, única ocurrencia en la comment sheet, pág. 11), no hay frase de exclusión ni remisión a otro documento, y los criterios de la sección 5.7 son solo ASME B31.3 y AWS D1.1 |
| 6 | NOTE-01 | N20 | ABIERTO | **NO LEVANTADO** | pág. 8, sección 5.8.1: *"The results of the inspection and examination shall be recorded on an inspection record form."* La Rev A nombraba *"QAM-F004 ... and QAM-F005"*; la Rev 0 los eliminó junto con QAM-P008 y QAM-P009 de la sección 3.0. Se pidió **listar**; se **eliminó**. La Rev 0 no identifica ningún formulario, código de registro ni revisión de formato |

**OBS-01** — `VT inspector qualification not stated. Correct: align with the NDE Plan personnel basis (SNT-TC-1A VT Level II or ISO 9712) at IFC Rev 0.`

**OBS-02** — `scope includes thermoplastic welds but no thermoplastic acceptance criteria cited. Correct: add DVS 2202-1 visual acceptance or exclude thermoplastics at IFC Rev 0.`

**NOTE-01** — `referenced QAM forms and procedures not attached. Correct: list them as controlled external references at IFC Rev 0.`

Respuestas del CCS (páginas 11 y 12): OBS-01 *"Revised as per comment"* · OBS-02 *"Updated, exclude the thermoplastic"* · NOTE-01 *"Remove from procedure"*.

> **Alerta de método.** La respuesta a NOTE-01 no es lo pedido. Se pidió **listar** los formularios como referencias externas controladas; el proveedor declara **eliminarlos** del procedimiento. Verificar si con ello el procedimiento perdió el mecanismo de registro.
>
> La respuesta a OBS-02 escoge una de las dos vías ofrecidas (excluir termoplásticos en vez de citar DVS 2202-1). Es admisible, pero obliga a verificar qué documento cubre entonces la inspección visual de las soldaduras termoplásticas de HDPE y PVC.

---

## 3. P22-BA-09-000-010 — HP and LP Pressure Test Procedure

Cuatro ciclos previos: Rev A (N23, Código 3), Rev B (N26, Código 3), Rev C (N27, Código 3 y driver de seguridad del transmittal), Rev D (N29, Código 2). Once comentarios en total.

| # | ID | Origen | Tipo | Estado | Cita Rev 0 |
|---|---|---|---|---|---|
| 7 | OBS-01 | N23 | REGRESIÓN | **PARCIAL** | pág. 7, paso 5.5.12: *"HP piping will test to 135 bar, and LP will test to 7.5 bar. Testing pressure will refer in approved line list (Doc no: P22-LI-09-009-003 REV 0)"*. Falta la presión de diseño por subsistema (cero ocurrencias de "design pressure" en el cuerpo), el factor 1,5x y la reconciliación 90 bar del ITP contra hasta 120 bar de la ET. **El factor 1,5x estaba escrito en la Rev C (pág. 7) y se perdió en la Rev D** |
| 8 | OBS-02 | N23 | REGRESIÓN | **PARCIAL** | La reversión a 5.5.17/5.5.18 está corregida (la sección 5.5 corre 1 a 19 sin saltos). **El paso 5.6.5 falta**: pág. 8, *"5.6.4 The test medium... shall be used for pneumatic tests. 5.6.6 Prior to commencement of pneumatic testing..."*. Cero ocurrencias de `5.6.5` en las 13 páginas |
| 9 | OBS-01 | N26 | REGRESIÓN | **PARCIAL** | Misma sustancia y misma cita que la entrada 7 |
| 10 | OBS-02 | N26 | REGRESIÓN | **PARCIAL** | La mitad de 5.7.2.2 cerró (ver entrada 15); la otra mitad, *"5.6.4 jumps to 5.6.6"*, describe el Rev 0 sin cambiar una palabra |
| 11 | NOTE-01 | N26 | REGRESIÓN | **NO LEVANTADO — regresión** | El formulario `AQ-QAM-F018` *"Pressure and Leak Test Report"* estaba en la **página 13 de la Rev C** y cerró la nota en el N27. **Desapareció en la Rev D y no está en la Rev 0** (cero ocurrencias de `AQ-QAM`). Solo queda la remisión de la pág. 10: *"The results of the test shall be recorded in the Pressure Test Report."* |
| 12 | OBS-01 | N27 | REGRESIÓN (fue CRITICAL) | **CERRADO** | pág. 11, Line List: `DA-PVC-DN65-09-016 | POLYVINYL CHLORIDE, SCH 80 | DN65` con OPER 1 / DESIGN 2 / HYDROTEST **3 bar**. Barrido de las 34 filas: 23 líneas de PVC, ninguna sobre 7,5 bar; relación hidrostática/diseño = 1,5 exacta en las 34 |
| 13 | OBS-02 | N27 | REGRESIÓN | **PARCIAL** | La rama hidrostática cita *"(Doc no: P22-LI-09-009-003 REV 0)"* (pág. 7). La rama neumática mantiene la referencia genérica: pág. 9, paso 5.6.13, *"Testing pressure needs to refer in approved line list."* Además la Line List solo tiene columna `HYDROTEST PRESS.`, sin presión de ensayo neumático |
| 14 | OBS-03 | N27 | REGRESIÓN | **PARCIAL** | Ya no se enuncia como mínimo y se nombra la revisión de la Line List, pero **falta la envolvente por circuito**: el binomio 135 / 7,5 bar del cuerpo contradice 17 de las 34 filas de su propia Line List, que prescribe 135, 120, 90, 75, 7,5 y 3 bar |
| 15 | OBS-04 | N27 | REGRESIÓN | **CERRADO** | pág. 9: *"5.7.2 Weld Joints / 5.7.2.1 Depressurize the system gradually. / 5.7.2.2 The weld joint must be clean and dry before re-welding. / 5.7.2.3 Only qualified welders are allowed to repair the weld."* La subsección corre 1-2-3-4 sin saltos |
| 16 | NOTE-01 | N27 | **ABIERTO** | **NO LEVANTADO** | No hay formulario al que agregarle el campo de presión requerida: ver entrada 11. El Rev 0 tiene 13 páginas (carátula, portada, índice, cuerpo 4-10, Line List 11-12, comment sheet 13) y ninguna es formulario |
| 17 | NOTE-01 | N29 | **ABIERTO** | **PARCIAL** | pág. 4: *"3.1 ASME Code Section V, Article 1 – 2025 edition / 3.2 ASME B31.3 – 2024 edition"* — la edición quedó fijada (la Rev D decía *"Applicable Edition/Addenda"*), y `ASME B31.3-2024` existe, publicada el 27-Dic-2024. Pero las dos cláusulas que gobiernan la ejecución siguen flotantes: pág. 7, paso 5.5.2 y pág. 8, paso 5.6.3, *"the latest edition/addenda of ASME B31.3"*. Tampoco se declara addenda, que también se pidió |

**N23 OBS-01** — `The procedure writes no numeric test pressure or the ASME B31.3 factor, repeating the required test pressure generically. The ITP fixes 135 bar (1.5 x 90 bar) HP and 7.5 bar LP. The HP design pressure is also unreconciled (ITP 90 bar vs Technical Specification up to 120 bar). Correct: declare the design pressure per subsystem, the B31.3 factor (1.5x), and the resulting test pressure in bar matching the ITP; reconcile the HP design pressure citing the source. Requirement: ASME B31.3 para. 345.4.2; ITP rows 5.1/5.2.`

**N23 OBS-02** — `In the pneumatic-test section, after step 5.6.16 the numbering reverts to 5.5.17 and 5.5.18 (duplicating the hydrostatic-section identifiers) and step 5.6.5 is missing. Correct: renumber section 5.6 consecutively, removing the duplicates and the gap.`

**N26 OBS-01** — `the body omits the numeric test pressure (135 bar HP / 7.5 bar LP fixed by the ITP) and does not reconcile the HP design pressure (90 bar ITP vs up to 120 bar ET); both steps defer to the line list, leaving the result indeterminate. Correct: state the design pressure per subsystem with a cited source and write the resulting numeric test pressure in the body.`

**N26 OBS-02** — `the reversion was corrected but step 5.6.5 is still missing (5.6.4 jumps to 5.6.6) and subsection 5.7.2 skips 5.7.2.2. Correct: renumber contiguously.`

**N26 NOTE-01** — `the Pressure Test Report form is not in this delivery; attach it at the next submittal so any pre-printed pressure matches 135 bar HP / 7.5 bar LP.`

**N27 OBS-01** (fue CRITICAL) — `line DA-PVC-DN65-09-016 (RO Brine Discharge) is PVC SCH 80 DN65 operating at 1 bar, yet it carries a 50 bar design pressure, so this column orders a 75 bar hydrostatic test on a plastic line with Class 150 flanges. Testing to this value would rupture the line. Correct: reconcile the piping class and the design pressure of this line per ET Section 5.2.1 - Low-Pressure Piping, and re-derive the test pressure from the corrected value.`

**N27 OBS-02** — `this Line List is labelled Rev 0, a revision never transmitted. The revision ADASA approved is Rev C (Code 1, Transmittal N18), and it carries no HYDROTEST PRESS. column. Correct: transmit the corrected Line List revision as a submittal and cite it in the procedure body by number and revision.`

**N27 OBS-03** — `the body still writes no numeric test pressure and states it as a minimum, not as the single value to apply. Correct: state the governing envelope per circuit (135 bar HP / 7.5 bar LP, per ITP rows 5.2 and 5.1) and name the Line List revision that fixes the value line by line.`

**N27 OBS-04** — `subsection 5.7.2 still skips 5.7.2.2 (5.7.2.1 jumps to 5.7.2.3). The gap at 5.6.5 is corrected; this one was reported as resolved in the previous reply and survives. Correct: renumber contiguously.`

**N27 NOTE-01** (abierto) — `the report form is now attached and carries no pre-printed pressure, which closes the Transmittal N26 note. It has no field for the required test pressure, only for the applied one. Correct: add a Required Test Pressure field referencing the approved Line List revision.`

**N29 NOTE-01** (abierto) — `Sections 3.1 and 3.2 cite ASME Section V (Article 1) and ASME B31.3 as 'Applicable Edition/Addenda' without fixing the edition. Correct: state the applicable edition and addenda of ASME Section V and ASME B31.3 to be used for the tests. The critical test-pressure error of Rev C (75 bar on the PVC line) is resolved and verified; the HP hydrostatic test remains a Hold Point.`

CCS del Rev 0 (página 13): una sola fila, la NOTE-01 del N29, respondida *"Revised as per comment"*. Los diez comentarios anteriores no aparecen.

> **Por qué la regresión es obligatoria aquí.** El **gap 5.7.2.2** fue declarado corregido en la respuesta al N23 y otra vez en la respuesta al N26, y era falso las dos veces. Se corrigió efectivamente recién en la Rev D. Que la Rev 0 no lo haya perdido no se puede asumir: se comprueba.

---

## 4. P22-BA-09-000-011 — Painting Procedure

Dos ciclos previos: Rev A (N23, Código 3) y Rev B (N27, Código 2). Doce comentarios en total.

| # | ID | Origen | Tipo | Estado | Cita Rev 0 |
|---|---|---|---|---|---|
| 18 | OBS-01 | N23 | REGRESIÓN | **CERRADO — sin regresión** | pág. 9: *"1st COAT – JOTUN BARRIER 80: DFT – 80µ / 2nd COAT – JOTUN PENGUARD MIDCOAT: - 200µ / 3rd COAT – JOTUN HARDTOP XP: 75µ"*. Carta Jotun `TSS-DD-MYPC039-26` del 02-Jul-2026 en pág. 12 y las tres fichas técnicas en págs. 14 a 36, idénticas carácter por carácter a la Rev B |
| 19 | OBS-02 | N23 | REGRESIÓN | **CERRADO — sin regresión** | pág. 12: *"Proposed Jotun Coating System Suitability for ISO 12944 C5M/ CX Environment ... suitable to be used for C5M/ CX corrosivity category as per ISO 12944"*. Salvedad: la declaración C5-M vive **solo** en la carta anexa del fabricante; el cuerpo del procedimiento no la declara en ninguna parte (verificado: `C5M`/`CX` solo en pág. 12) |
| 20 | OBS-03 | N23 | Reemitido como N27 OBS-01 | — | ver #24 |
| 21 | OBS-04 | N23 | Reemitido como N27 OBS-03 | — | ver #26 |
| 22 | OBS-05 | N23 | REGRESIÓN | **CERRADO — sin regresión** | pág. 8, sección 1.0: *"This procedure covers minimum requirements for surface blasting and painting work for ASTM A36 carbon steel and exclude stainless steel and non-metallic surface."* |
| 23 | OBS-06 | N23 | REGRESIÓN parcial | **CERRADO — sin regresión** (las tres partes cerradas en el N27) | Adherencia: pág. 10, sección 6.7, *"c. Adhesion Pull off test on test panel"*. ISO 2808: pág. 8. SSPC-SP-10: pág. 8. La cuarta parte (DFT nominal) no pertenece aquí: quedó abierta como N27 OBS-02, entrada 25 |
| — | NOTE-01 | N23 | Informativa, sin acción | — | — |
| 24 | OBS-01 | N27 | **ABIERTO** | **CERRADO** | pág. 11, formulario: la celda de criterio dice `50-80 µm` y la fila de aceptación `50-80 Microns`; pág. 9, cuerpo: *"Blasted surface shall have a surface profile range of 50 – 80 microns."* La Rev B decía `40-75 µm` en la celda de criterio. Única supervivencia de `40-75` en las 38 páginas: la comment sheet (pág. 37), citando el texto de ADASA |
| 25 | OBS-02 | N27 | **ABIERTO** | **PARCIAL** | pág. 11: el placeholder `xxx µm` se reemplazó por `Specified DFT : 355 µm Min`. **No se cumplió el resto**: los valores nominales por capa (80 / 200 / 75) no aparecen en el formulario, y las filas `Type` y `Colour` siguen en blanco en las tres columnas. El proveedor lo admite: *"Actual product will update in actual report"* |
| 26 | OBS-03 | N27 | **ABIERTO** | **PARCIAL** | pág. 9: *"3rd COAT – JOTUN HARDTOP XP: 75µ Finish Colour RAL5012 LUMINOUS BLUE"* cierra la primera mitad. La segunda no: se pidió *"state RAL 5012 here **and in the Colour row of the inspection form**"* y la fila `Colour` del formulario de la pág. 11 sigue vacía |
| — | NOTE-01 | N27 | Declaración de cierre de N23 OBS-01 y OBS-02 | — | — |
| — | NOTE-02 | N27 | Declaración de cierre de N23 OBS-05 y parte de OBS-06 | — | — |

**N23 OBS-01** — `The procedure proposes a Jotun system (Barrier 80, Penguard Midcoat, Hardtop XP) in place of the Sherwin-Williams system (Zinc Clad II, Macropoxy 646, Acrolon 218 HS) fixed in the Painting Specifications Rev B (approved Code 1 at TM N11), with no equivalence justification; the ET conditions any equivalent on ADASA approval. Correct: attach a product-to-product equivalence table (generic chemistry, % solids by volume, ISO 12944-6 class, DFT range) and obtain ADASA approval of the Jotun system, or adopt the Sherwin-Williams system; reconcile both documents.`

**N23 OBS-02** — `Marine durability is not demonstrated: the body declares no target corrosivity category, and the Barrier 80 primer is certified for C5-I (industrial), not C5-M (marine), where coastal Taltal and the ET require C5-M with high durability. Correct: declare the target category C5-M (or CX) and high durability, and provide the ISO 12944-6 evidence for the complete system.`

**N23 OBS-05** — `The scope is generic and does not limit the coating to the ASTM A-36 structural carbon steel nor exclude stainless steel and non-metallic surfaces (FRP, HDPE), which are not painted. Correct: bound the scope to the ASTM A-36 carbon steel and exclude stainless steel and non-metallic surfaces.`

**N23 OBS-06** — `QC lacks an adhesion test (pull-off ISO 4624 or cross-cut ISO 2409), the nominal DFT per coat/total is not pre-loaded in the form (left as xxx microns), ISO 2808 is not cited as the DFT method, and SSPC-SP10 / NACE No. 2 is not listed among the references. Correct: add an adhesion test, the nominal DFT per coat (80/200/75 = 355 microns), and the ISO 2808 and SSPC-SP10 references.`

**N27 OBS-01** (abierto) — `this criterion still reads 40-75 um while the procedure body and the acceptance row of this same form read 50-80 um. The inspector works against two incompatible criteria and can accept a 40 um profile, below the 50 um lower bound required at Transmittal N23 and below the anchor profile of ET Section 5.1.9 - Support Frame. Correct: unify the form to a single 50-80 um criterion.`

**N27 OBS-02** (abierto) — `the specified DFT is still the placeholder "xxx um" and the Type row of the painting system is blank, so the nominal thickness per coat appears nowhere on the record the inspector signs. Correct: print the nominal values (80 / 200 / 75 um, not less than 355 um total) and the product per coat.`

**N27 OBS-03** (abierto) — `the painting system does not state the finish colour. RAL 5012 (Luminous Blue) is fixed for the structural support frame by the approved Painting Specification Rev C and by ET Section 5.1.9 - Support Frame. Correct: state RAL 5012 here and in the Colour row of the inspection form.`

Respuestas del CCS (páginas 37 y 38): OBS-01 *"Revised as per comment"* · OBS-02 *"xxx um update to 355um min, Actual product will update in actual report, attached report in this report just for sample"* · OBS-03 *"Revised as per comment"*.

> **Alerta de método.** La respuesta a OBS-02 no cubre lo pedido. Se pidieron los **valores nominales por capa** (80 / 200 / 75 µm) **y el producto por capa** impresos en el formulario que firma el inspector. El proveedor declara haber puesto solo el total *"355um min"* y difiere el producto al reporte real. Candidato a PARCIAL.
>
> **Contexto vinculante del N27:** la aceptación de ADASA quedó condicionada a *"the coating actually applied being the C5-M certified Jotun system, not less than 355 micrometres total, RAL 5012, over a 50 to 80 micrometre anchor profile"*. Las tres observaciones abiertas son exactamente las tres variables de esa condición.
>
> **Por qué la regresión es obligatoria aquí.** Las observaciones del formulario de inspección (perfil de anclaje, espesor nominal, color) se pidieron en el N23, sobrevivieron intactas a toda la Rev B y hubo que repedirlas en el N27.

---

## 5. P22-CD-09-005-001 — UHPRO Structural Calculation Report

Dos ciclos previos: Rev A (N26, Código 3) y Rev B (N29, Código 2). Nueve comentarios en total.

| # | ID | Origen | Tipo | Estado | Cita Rev 0 |
|---|---|---|---|---|---|
| 27 | OBS-01 | N26 | REGRESIÓN (fue CRITICAL) | **PARCIAL** | pág. 20, sección *"D. Bolt Design at the Base"*, bloque "Anchored to Skid": *"RO Cartridge Filter | 4 | 12mm | 0.10 · RO HP Feed Pump – Motor | 8 | 12mm | 0.11 · RO HP Feed Pump – Pipe | 8 | 12mm | 0.03 · Feed Turbocharger | 4 | 10mm | 0.01 · Interstage Turbocharger | 4 | 10mm | 0.01"*. Cubre 4 de los 6 TAG: **faltan BOI-09-001 y BOI-09-002**, los recipientes a presión, que el propio informe declara como el ítem más pesado (pág. 64, *"BOI-09-001/002 | RO PRESSURE VESSELS | Operating Weight 9169.2 lbs [4160.0 kg]"*). Ninguna hoja del Attachment B ni fila de la pág. 20 los verifica |
| 28 | OBS-02 | N26 | REGRESIÓN | **CERRADO** | pág. 14, sección *"C. Design Results"*: *"The operating seismic weight of the unit is 122.41 kN. The calculated horizontal base shear in accordance with NCh 2369:2003 is 41.62 kN... The seismic input parameters in the STAAD model were adjusted to produce a design base shear equal to the calculated NCh 2369:2003 base shear."* Los tres valores quedaron resumidos en el cuerpo |
| 29 | OBS-03 | N26 | REGRESIÓN | **NO LEVANTADO** | pág. 44: el listado impreso ya dice 224/225 = EOX y 226/227 = EOZ. **Pero el modelo no cambió.** Parseadas las reacciones del Attachment C: los casos básicos 1 (EOX) y 2 (EOZ) difieren en los ocho nodos de apoyo (nodo 122: `-4.718 / -12.151 / -4.196` contra `-0.96 / -1.952 / -3.972`), y sin embargo **224 y 226 son idénticas dígito a dígito en los ocho nodos**, igual que 225 y 227. Se corrigió el rótulo, no el análisis; el caso de gravedad mínima en dirección X sigue sin existir. El propio proveedor lo declara: *"This is a typographical error in the calculation report only."* |
| 30 | OBS-04 | N26 | REGRESIÓN | **CERRADO** | pág. 17, bajo la Figura 13: *"All members satisfy the acceptance criteria, with a maximum (governing) utilization ratio of 0.454, which is below the allowable limit of 1.0."* |
| 31 | OBS-05 | N26 | REGRESIÓN | **PARCIAL** | Material (pág. 5): *"Table 1 Material Properties: Structural Steel | Corten A | fy = 345 MPa · Structural Steel | S275JR | fy = 275 MPa"* — sin citar el Structural Design Criteria ni reconciliar con el ASTM A-36 de la ET; esa explicación vive solo en la comment sheet. Etiqueta de revisión: corregida (`REV.0` en todo el cuerpo, el token `A1` desapareció), con residual de que las dos portadas declaran historiales distintos. **Contador de páginas: no corregido** — los pies de Aulem siguen diciendo `Page N of 548` sobre un archivo de 551 |
| 32 | NOTE-01 | N26 | REGRESIÓN | **PARCIAL** | La aclaración de alcance sí quedó escrita (pág. 20: *"For units anchored to the concrete foundation, only the bolt material has been checked. The concrete supporting these units shall be checked by others for shear and tension."*). La tabla de interfaz para obras civiles **no** se entregó como tal, y los únicos valores gobernantes declarados (pág. 25: *"Shear at the bolt V := √((4.711 kN)² + (9.42 kN)²) = 10.5323 kN"*) **son los de la Rev A**: el Attachment C de la Rev 0 da −4,642 y −9,547 kN para esos mismos nodos y casos |
| 33 | NOTE-02 | N26 | REGRESIÓN | **PARCIAL** | pág. 6, Tabla 4: *"Type of Soil | E | NCh2369:2003, Table 5.3"* — la Tabla 5.3 de esa norma clasifica en tipos I a IV y no contiene un tipo "E", de modo que la cita es refutable. Los parámetros usados (`T' = 1.35`, `n = 1.80`) sí corresponden al suelo Tipo IV, el más desfavorable, y se agregó la nota *"Soil classification is assumed as a conservative envelope pending geotechnical confirmation."* La procedencia del dato (entregado por el mandante) vive solo en la comment sheet |
| 34 | NOTE-01 | N29 | **ABIERTO** | **CERRADO** | 551 páginas y 26,6 MB contra 1.101 páginas y 58 MB de la Rev B. Sin duplicación interna: la estructura aparece una sola vez (portada ADASA pág. 1, portada Aulem pág. 2, Contents pág. 3, Anexos A/B/C/D/E en págs. 22/24/42/62/126, comment sheet 550-551). El único par de páginas idénticas (76 y 80) es una portada de catálogo de proveedor adjuntada para dos filtros distintos |
| 35 | NOTE-02 | N29 | **ABIERTO** | **CERRADO** | pág. 550-551: la columna `Comment from Client` está poblada en las ocho filas con el texto original de ADASA, con su ID y severidad. Verificado por render a 170 dpi. **Cautela de método:** el texto está pegado como imágenes rasterizadas (5 en la pág. 550, 4 en la 551), de modo que la extracción de texto devuelve la columna vacía y produce la conclusión contraria. Queda como residual menor que los comentarios no sean texto seleccionable |

**N26 OBS-01** (fue CRITICAL) — `the Bolt Design at the Base checks only 8 ancillary units and omits the main process equipment - HP pump BH-09-001, turbos SIP-09-001/002, RO filter FIL-09-001 and pressure vessels BOI-09-001/002 (4160 kg) - which the Technical Specification requires anchored for NCh 2369 Zone 3. Correct: add the anchor check for these, or document and certify their anchorage route via the skid frame.`

**N26 OBS-02** — `Design Results does not state the consolidated design seismic weight, the global base shear or the NCh 2369 base-shear check; these live only in the seismic-load attachment. Correct: summarise them in the body.`

**N26 OBS-03** — `in the load-combination list, cases 226/227 duplicate 224/225 (both Z) and the X-direction minimum-gravity case 0.9(DS+DO+FR)+1.1 EOX+/-0.3 EV is absent. Correct: fix cases 226/227 to the EOX case.`

**N26 OBS-04** — `the skid-frame utilization is shown only as a colour map (Figure 13) without the governing maximum value. Correct: state the maximum utilization ratio and confirm it is below 1.0.`

**N26 OBS-05** — `confirm the frame material (Corten A fy=345, S275JR fy=275) against the approved Structural Design Criteria Rev B and reconcile with the ASTM A-36 reference of the Technical Specification; unify the revision label (Rev A vs 'A1') and the page count.`

**N26 NOTE-01** — `the container base bolts to the concrete are deferred 'to others'. Transmit the governing base-bolt tension/shear as an interface table for the OOCC foundation, and clarify that 'concrete by others' applies to the container base, not the equipment-to-skid anchors.`

**N26 NOTE-02** — `the soil is labelled 'Type E' (NCh 433) while NCh 2369 uses Types I-IV. Confirm the soil type against the site geotechnical report and the T' and n parameters.`

**N29 NOTE-01** (abierto) — `this PDF is a duplicated concatenation of the same report (about 58 MB, 1101 pages = two copies of the 549-page report). Correct: issue a single, non-duplicated report file. The seismic calculation itself is accepted (base shear NCh 2369:2003 Zone 3 = 41.62 kN; governing skid utilization 0.454 < 1.0).`

**N29 NOTE-02** (abierto) — `the comment sheet records BW Water's replies to the Transmittal N26 comments without reproducing ADASA's original comment text. Correct: complete the comment sheet with the client comment text alongside each reply, so each closure is traceable.`

CCS del Rev 0 (páginas 550 y 551): ocho filas, siete atribuidas al N26 sobre la Rev A y una al N29 sobre la Rev B.

---

## Nota sobre el alcance de la verificación estructural

Por decisión de alcance, **no se re-audita de novo el cálculo sísmico** aceptado en el N29 (corte basal 41,62 kN en Zona 3, utilización gobernante 0,454). Lo que se verifica es que los nueve comentarios estén levantados y no hayan regresado.

El documento trae 551 páginas, de las cuales **101 tienen el texto vectorizado** (páginas 2 a 21, 23, 25 a 41 y 63 a 125) y no devuelven texto extraíble. Solo se renderizan las páginas necesarias para verificar una entrada concreta.

---

## Estado de cierre del libro mayor

**33 entradas de verificación, cero en SIN CITA.** El bucle convergió.

| Documento | Entradas | CERRADO | PARCIAL | NO LEVANTADO |
|---|---|---|---|---|
| PMI `-006` | 3 | 1 | 1 | 1 |
| Visual `-008` | 3 | 1 | 1 | 1 |
| HP/LP `-010` | 11 | 2 | 7 | 2 |
| Painting `-011` | 7 | 5 | 2 | 0 |
| Structural `-005-001` | 9 | 4 | 4 | 1 |
| **Total** | **33** | **13** | **15** | **5** |

**En binario: 13 levantados, 20 no.** Los tres estados de arriba son el detalle de la evidencia; para decidir, PARCIAL y NO LEVANTADO cuentan igual — un comentario cumplido a medias no está cumplido.

De los 13 cerrados, **ninguno cerró por la vía de la declaración del proveedor**: los 13 tienen cita literal del cuerpo del Rev 0 verificada. Las respuestas *"Revised as per comment"* que no se pudieron respaldar con una cita quedaron en PARCIAL o en NO LEVANTADO.

## Lo que decide el veredicto: las doce condiciones del Código 2 — respuesta binaria

**No hay estado intermedio.** Un comentario se levantó cuando el Rev 0 hace lo que la instrucción pedía, entero. Si hace una parte, no se levantó.

| # | Documento | ID | Qué pedía la instrucción | ¿Levantado? |
|---|---|---|---|---|
| 1 | PMI | OBS-01 (N20) | Cláusula de alcance con tres elementos: 10% del Super Duplex de alta, conformidad **UNS S32750 como base de aceptación**, testificación de ADASA | **NO** — falta la base de aceptación |
| 2 | PMI | OBS-02 (N20) | Declaración de aplicabilidad al proyecto | **NO** — no se agregó nada |
| 3 | PMI | NOTE-01 (N20) | Reemplazar la cláusula de calificación copiada del NDE Plan | **SÍ** |
| 4 | Visual | OBS-01 (N20) | Declarar la calificación del inspector VT | **SÍ** |
| 5 | Visual | OBS-02 (N20) | Citar DVS 2202-1 **o** excluir los termoplásticos | **SÍ** — tomó la segunda vía, que ADASA ofreció |
| 6 | Visual | NOTE-01 (N20) | **Listar** los formularios QAM como referencias externas controladas | **NO** — los eliminó |
| 7 | HP/LP | NOTE-01 (N29) | Declarar edición **y addenda** de ASME Sección V y B31.3 **a usar para los ensayos** | **NO** — la sección 3 fija edición sin addenda, y los pasos 5.5.2 y 5.6.3, que gobiernan los ensayos, siguen en `latest edition/addenda` |
| 8 | Painting | OBS-01 (N27) | Unificar el formulario a un solo criterio de 50-80 µm | **SÍ** |
| 9 | Painting | OBS-02 (N27) | Imprimir los valores por capa (80 / 200 / 75) **y el producto por capa** | **NO** — solo imprimió el total de 355 µm |
| 10 | Painting | OBS-03 (N27) | Declarar RAL 5012 en el esquema **y en la fila Colour del formulario** | **NO** — solo en el esquema |
| 11 | Structural | NOTE-01 (N29) | Emitir un archivo único sin duplicar | **SÍ** |
| 12 | Structural | NOTE-02 (N29) | Completar la comment sheet con el texto del comentario del cliente | **SÍ** |

**Seis levantados, seis no.** Por documento:

| Documento | Condiciones | Levantadas | Veredicto |
|---|---|---|---|
| Structural `-005-001` | 2 | **2** | **1 — Approved** |
| Visual `-008` | 3 | 2 | 3 |
| PMI `-006` | 3 | 1 | 3 |
| Painting `-011` | 3 | 1 | 3 |
| HP/LP `-010` | 1 | **0** | 3 |

Las 21 entradas restantes del libro mayor son registro interno. Su estado se conservó verificado, pero **no funda observación ni veredicto**.

## Tres regresiones de cierre verificado

Son distintas de un pendiente arrastrado: ADASA comprobó el cierre en su momento y el contenido se perdió después.

| Qué se perdió | Dónde estaba | Dónde se perdió | Estado en Rev 0 |
|---|---|---|---|
| Cláusula 5.6.5 del procedimiento de presión | Rev C, cuerpo, con su texto propio | Rev D | Ausente. El cuerpo salta de 5.6.4 a 5.6.6 |
| Formulario `AQ-QAM-F018` *"Pressure and Leak Test Report"* | Rev C, página 13 | Rev D | Ausente. Cero ocurrencias de `AQ-QAM` |
| Factor `1.5 x design pressure` | Rev C, paso 5.5.12 | Rev D | Ausente. El procedimiento afirma dos presiones sin declarar de dónde salen |

Las tres se introdujeron en la **misma edición, la Rev D**, que ADASA codificó 2 en el transmittal N29 sin detectarlas. La revisión del N29 se concentró en la edición normativa y no re-barrió el resto del documento contra la Rev C.

## Cautela de método que este trabajo dejó registrada

Dos conclusiones se sacaron primero de la extracción de texto y resultaron **falsas al mirar la página renderizada**:

1. La comment sheet del informe estructural parecía tener la columna `Comment from Client` vacía. Está poblada; el texto es imagen.
2. Los TAG de los equipos principales parecían ausentes del informe estructural. Están, dentro de planos vectorizados.

En los dos casos la extracción devolvía vacío por la forma del PDF, no por ausencia de contenido. En un documento con páginas vectorizadas o imágenes pegadas, **la ausencia solo se afirma tras renderizar**.

---

*Cerrado el 06-Ago-2026. Los hallazgos y el veredicto propuesto por documento viven en `_HALLAZGOS_DETERMINISTAS.md`.*
