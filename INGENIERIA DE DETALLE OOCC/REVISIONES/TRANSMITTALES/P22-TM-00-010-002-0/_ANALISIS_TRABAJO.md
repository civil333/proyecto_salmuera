# _ANALISIS_TRABAJO.md — TM N2 OOCC (P22-TM-00-010-002-0)

**Documento INTERNO ADASA — NO ENVIAR a L&A.** Insumo para el TRANSMITTAL formal.

Revisión de la **ENTREGA 4** de L&A Ingeniería (carta de remisión 067-032-032-COR-TT-005, 28-May-2026), respuesta al TM N1 + entregables nuevos. Stream OOCC/L&A — 100% español, IDs NOTA-XX/OBS-XX/PEND-XX, comentarios como directivas.

`.md` extraídos en `ENTREGA 4/02 Documentos/md/` (5 MC + 3 ET); itemizados leídos de los `.xlsx`; planos leídos de los PDF de `03 Planos/PDF/`.

---

## 1. Veredicto global y recuento

**Veredicto global: 3 — POR REVISAR** (regresión vs TM N1, que fue 2 Cód.3 + 3 Cód.2).

| Disciplina | Cód. 1 | Cód. 2 | Cód. 3 |
|---|---|---|---|
| Memorias de Cálculo (5) | 0 | 1 (MC-002) | 4 (MC-001, -004, -005, -003-001) |
| Especificaciones Técnicas (3) | 0 | 0 | 3 (ET-101/102/103) |
| Itemizados/cubicaciones (3) | 0 | 0 | 3 (IT-101/102/103) |
| Planos (7 códigos) | 0 | 1 (DWG-003-001) | 6 (DWG-002-001/002/003/004/006/007) |
| **Total (18 ítems)** | **0** | **2** | **16** |

Faltante: **MC-002-003 Sistema de Drenajes** no entregada (PEND-01 abierto; sí llegó el plano de canalizaciones -006).

---

## 2. Determinantes del veredicto (transversales)

1. **NPT — match contra los planos de montaje (NO unificar).** Corrección del usuario: es **correcto** que los NPT difieran por zona (escalón salmuera vs RO/CIP); el hallazgo es el **match contra los planos de montaje mecánico** (`INGENIERIA DE DETALLE MECANICA/ENTREGAS/COMPILADO REV 0/02_MECANICA/`: -101 salmuera/bomba, -103 RO/desalación, -105 fosa). Resultado: (a) **memorias**: ninguna declara el NPT (siguen "Modelo Navis Referencial") → exigir que lo declaren conforme al montaje; (b) **estanque/bomba (-002) y fosa (-004): +5,75 COINCIDE** con el montaje (-101/-105) — OK (menor: nivel inferior fosa +4,800 montaje vs +4,305 L&A, reconciliar); (c) **contenedor (-003)**: usa **datum relativo ≈0,00**, debe pasar a la cota absoluta de su zona citando el montaje -103 → "estas elevaciones no corresponden" (comentario del usuario); (d) **CIP/cobertizo (-007/-003-001): +5,610 / +5,840** → reconciliar contra el montaje -103 (referencia de proyecto de la zona RO/CIP ≈ +6,00; no afirmar la cifra como cerrada porque el PDF de montaje no la acota legible — la directiva es "declarar y coincidir con el plano de montaje -103 + Levantamiento DIO"). El escalón +5,75 vs zona RO/CIP es intencional.
2. **Anclaje estanque/bomba sigue postinstalado.** MC-001 OBS-01 NO resuelta: la Rev 0 mantiene perno postinstalado adhesivo (HAS-V-36 + HIT RE-500 V3, ACI 318-19 vía PROFIS) — exactamente lo rechazado; además densificó la losa Ø16@150→@100 (agrava la inviabilidad). Los planos -002 (estanque LAM2 y bomba LAM4) confirman el anclaje químico. No se rediseñó a preinstalado colado (ACI 318-19 Cap.17/Sec.17.10) ni se reconcilió con Exfibro EX-26005-F01 Rev C. Corrobora el comentario del usuario.
3. **MC-004 peso del contenedor erróneo (regresión).** Rev 0 declara "17.334 [tonf]" (pág. 14): no coincide con los 14.934 kg vinculantes (TR Sección 2.1.2 / P22-DWG-09-005-001 Rev A), unidad absurda, sin fuente — y ya propagó a las presiones de contacto (0,47/0,66). Un insumo de carga errado invalida la verificación → sube de Cód.2 a Cód.3.
4. **ET genéricas, no de proyecto.** Las 3 ET son plantillas de pliego AGUAS DE ANTOFAGASTA: dicen emplazamiento "Antofagasta" (es **Taltal**, costero), invocan un "Informe de Mecánica de Suelos" que el TdR declara inexistente (σ_adm ≤ 1,0 kg/cm² por asunción), y portan código tipo IT en portada. ET-102 declara recubrimiento 70 mm pero NO los 50 mm expuesto y NO menciona impermeabilización; ET-103 declara C5-M/≥355 µm/RAL 5012 (cierra OBS-02 por remisión) pero sin desglose por capas (SSPC-SP10/Sa 2½ + 80/200/75 µm) y cita AWS A5.1/A5.17 en vez de AWS D1.1.
5. **Itemizados no conformes al TdR.** Rotulados "PRESUPUESTO REFERENCIAL" (el TdR exige Clase 1 AACE ±3–15%); sin columnas de vínculo a plano/memoria; tag fosa **TK-06-002** (debe ser **TK-06-004**); pestaña BOM "CUADRO DE PIEZAS INTERCONEXIÓN LA CHIMBA" (copy-paste de otro proyecto, con termofusión prohibida en Taltal); faltan partidas de impermeabilización (IT-102), protección anticorrosiva m² y soldadura (IT-103).
6. **Mejoramiento de suelo / impermeabilización: vacío repetido** en planos (-002, -003, -004, -007) y ET — ningún plano declara σ_adm, tipo de suelo, ni refiere a ET-101/102. Es el tema de 9 de tus 11 comentarios.
7. **Codificación / entregables faltantes vs TdR Sección 6.2:** no entregados **DWG-00-001-001 (Excavaciones/mov. tierra)** ni **DWG-00-002-005 (Detalles de anclaje y conexiones)**; falta la 3ª lámina de **-002-006** (detalle típico de cámara CD-06-00N); el split de fundaciones reintroduce códigos no previstos (MC-005 y DWG-007) — formalizar vía lista 067-032-032-COR-LI-001; tag TK-06-002 en planos+itemizados.

---

## 3. Cierre del carry-forward TM N1 — Memorias de Cálculo

### MC-002-001 Fundación Estanque — Cód. 3 (era 3)
- OBS-01 anclaje preinstalado: **ABIERTO** (sigue postinstalado HAS-V-36/HIT RE-500; ACI 318-19 pero método equivocado; no reconcilia Exfibro). Determinante.
- OBS-02 NPT: **ABIERTO** ("Modelo Navis Referencial", pág. 4).
- NOTA-01 ACI 318-19: **CERRADO** (pág. 7/25).
- NOTA-02 recubrimientos: **ABIERTO**.
- NOTA-03 reacciones basales: **PARCIAL** (adopta valores ADASA pero cita fuente "Memoria AFTA", no P22-IT-06-000-005-0; cortante 4.617 no explícito).
- NOTA-04 base sísmica 2003/2025: **PARCIAL**.
- Nuevos: typo "ASTM F1553" (debe F1554) y "HIR-RE 500" (HIT-RE); losa Ø16@150→@100 sin justificar; typo "ACI50-01".

### MC-002-002 Fundación Bomba (ACI 351.3R) — Cód. 2 (era 2; NO escala)
- NOTA-07 peso + rehacer ACI 351.3R: **CERRADO** (peso 223,5 kg trazado al plano KSB pieza por pieza; relación de masa 10 ≥ 3; fn 2,37 Hz vs 50 Hz → no gatilla escalamiento).
- OBS-01 NPT: **ABIERTO**.
- NOTA-06 valores numéricos: **CERRADO**. NOTA-01 ACI 318-19: **CERRADO**. Anclaje desarrollado FU 51% (postinstalado, aceptable en bomba).
- NOTA-02 recubrimientos: **ABIERTO**. NOTA-05 base sísmica: **PARCIAL** (adopta 2025 de hecho; limpiar referencia residual 2003).
- Pendientes para Rev 0: declarar NPT (+5,75) verificado vs DIO + recubrimientos 50/70.

### MC-002-004 Fundación Contenedor RO — Cód. 3 (era 2; REGRESIÓN)
- OBS-01 retirar cargas CIP + título/alcance: **CERRADO**.
- OBS-03 NPT (+6,00): **ABIERTO**.
- NOTA-08 peso 14.934 kg: **ABIERTO con desviación** → "17.334 [tonf]" erróneo, no trazable, contaminó presiones. Determinante.
- OBS-02/NOTA-01 ACI 318: **PARCIAL** (listado 318-19 pero pedestales aún 318-10). NOTA-02 recubrimientos: **ABIERTO**.
- Nuevo: doble paginación en pie (44 vs 43).

### MC-002-005 Fundación CIP — Cód. 3 (era 2)
- OBS-02 split/código: **CERRADO** (formalizado en el TT 067-032-032-COR-TT-005; salvedad: el xlsx Listado de entregables 067-032-032-COR-LI-001 está viejo, aún dice "Fundación Compartida").
- OBS-01/PEND-03 anclajes CIP: **ABIERTO (diferido legítimo)** — datos del proveedor no han llegado.
- NOTA-07 pesos dosificación 550 kg: **CERRADO**. NOTA-01 ACI 318-19: **CERRADO**. NOTA-05 base sísmica: **CERRADO**.
- OBS-03 NPT (+6,00): **ABIERTO**. NOTA-02 recubrimientos: **ABIERTO**.
- Emitida etiquetada "0 / Para Uso e Información" sin cerrar OBS-03 → debe ser Rev A intermedia, no Rev 0 directa.
- Nuevos: inconsistencia tabla de presiones; numeración de figuras duplicada.

### MC-003-001 Cubierta Metálica CIP — Cód. 3 (era 3)
- OBS-01 suelo D→E: **CERRADO** (reconciliado a Tipo E contra LNS-ADASA-INF-040, re-verificado). Determinante previo resuelto.
- OBS-03 NCh 427/1: **CERRADO** (unificado 2016). NOTA-01 ACI 318-19: **CERRADO**.
- OBS-02 C5-M: **ABIERTO** (no declara ni refiere a ET-103) → puede bajar a NOTA por remisión a ET-103.
- NOTA-02 recubrimientos: **ABIERTO**.
- Nuevos: anexos (págs. 45-72) siguen en Rev B; Cv 0,74 (tabla) vs texto "0,67" incoherente; factor "1,4E" en cargas pedestal/zapata no declarado en combinaciones (1,2D±E).

---

## 4. Especificaciones Técnicas (3) — todas Cód. 3
- **ET-101 Mov. Tierra:** compactación/CBR/sales/explosivos cubiertos; mejoramiento/reemplazo de suelo solo diferido a obra (no especificado como condición); lenguaje genérico "Antofagasta" + "Informe Mecánica Suelos" inexistente.
- **ET-102 Obras Civiles:** G-25/A630-420H OK; recubrimiento **70 mm sí / 50 mm expuesto NO**; **impermeabilización ausente**; clase exposición marina no declarada. → NOTA-02 recubrimientos transversal NO cierra.
- **ET-103 Estructura Metálica:** C5-M/ISO 12944/≥355 µm/RAL 5012 **declarado (cierra OBS-02 por remisión)** pero sin desglose por capas + SSPC-SP10/Sa 2½; cita AWS A5.1/A5.17 en vez de **AWS D1.1**; pernería sin exigir galvanizado/inox.
- Transversal: las 3 dicen "Antofagasta", invocan estudio de suelos inexistente, portan código IT en portada; sin referencia cruzada recíproca con las MC.

## 5. Itemizados (3) — todos Cód. 3
- Transversales: "PRESUPUESTO REFERENCIAL" (no Clase 1 AACE); sin columnas vínculo plano/memoria; tag **TK-06-002** (→ TK-06-004); pestaña **BOM "La Chimba"** ajena (con termofusión prohibida).
- IT-101 Mov. Tierra ($26.296.281): partidas por elemento OK; alinear "mejoramiento/base estabilizada" con el Formato BL.
- IT-102 Obras Civiles ($51.520.368): **falta impermeabilización** (fosa/estanque); aclarar a qué elemento pertenecen los 24 pernos F-1554.
- IT-103 Estructura Metálica ($42.107.588): **falta protección anticorrosiva m²** y **soldadura** como partidas (mínimas del TdR).
- Overlap con el Formato de Presupuesto del BL Montaje: definir que el itemizado L&A es referencial interno y el Formato BL es el que cotiza el contratista.

## 6. Planos (7) — códigos y observaciones
Mapeo real (de cajetín; corrige el inventario inicial): -002-002 = Equipos Ext. Área 06 (estanque LAM1-3 + bomba LAM4); -002-003 = Fundaciones Contenedor RO; -002-004 = Fosa Drenaje TK-06-002; -002-007 = Equipos CIP (estanque CIP + equipos + cobertizo); -003-001 = Cubierta cobertizo.

- **-002-001 Layout — Cód.3:** [U] faltan coordenadas/orientación estanque; [A] NPT no acotado en layout; callouts de lámina imprecisos.
- **-002-002 Equipos Ext — Cód.3:** [U] pernos preinstalados (rechazo previo); [U] indicar mejoramiento de suelo (LAM1/LAM4); [A] bomba LAM4 también anclaje postinstalado; NPT +5,750 OK (cierra NPT de -002 a nivel plano).
- **-002-003 Contenedor RO — Cód.3:** [U] "estas elevaciones no corresponden" (datum relativo vs +6,00); [U] INS-1 (detalle está en LAM2, falta callout); [U] mejoramiento de suelo.
- **-002-004 Fosa Drenaje — Cód.3:** [U] mejoramiento de suelo + impermeabilización exterior enterrada (interior Sikatop ya está); [U] parrilla → PRFV tránsito liviano + indicar aperturas de rebalse; tag TK-06-002 → TK-06-004.
- **-002-006 Canalizaciones — Cód.3:** [A] nomenclatura cámaras CD-06-00N (hoy "Cámara N°N"); falta 3ª lámina detalle típico de cámara; pendientes longitudinales no acotadas; cajetín distinto.
- **-002-007 Equipos CIP — Cód.3:** [U] mejoramiento de suelo + impermeabilizaciones (LAM1/LAM3); [A] NPT +5,610 inconsistente con +6,00 de zona; anclaje cobertizo preinstalado OK, equipos CIP diferido (PEND-03).
- **-003-001 Cubierta — Cód.2:** [A] C5-M por nota (referir ET-103); cotas placa base +5,840 coherentes con -007 pero zona ~+5,8 ≠ +6,00; soldadura AWS D1.1 OK. (Subir a 3 si se amarra el NPT de zona.)

---

## 7. Pendientes (PEND)
- **PEND-01** MC Sistema de Drenajes (P22-MC-00-002-003): **sigue sin entregarse** (llegó el plano -006, no la memoria). Exigir.
- **PEND-02** ratificación Exfibro (gestión ADASA): MC-001 adopta los valores ADASA pero sin citar la fuente P22-IT-06-000-005-0 → corregir cita.
- **PEND-03** anclajes postinstalados Sistema CIP: diferido legítimo hasta datos del proveedor; mantener en seguimiento.

## 8. Valores vinculantes ADASA (no renegociar; declarar en observaciones)
- NPT por zona: **+5,75** (estanque/bomba/fosa) / **+6,00** (contenedor/CIP), único sistema absoluto verificado vs Levantamiento DIO.
- Peso contenedor RO = **14.934 kg**; reacciones estanque P22-IT-06-000-005-0; peso bomba ficha KSB (ya adoptado); pesos dosificación ≈550 kg (ya adoptado); recubrimientos **50 mm expuesto / 70 mm terreno**; C5-M completo (SSPC-SP10/Sa 2½ + 80/200/75 µm); soldadura **AWS D1.1**; clasificación de suelo **Tipo E** única; tag fosa **TK-06-004**.

## 9. Para los scripts de COMENTARIOS (CC_ADASA)
- **Planos:** regenerar `*_CC_ADASA.pdf` desde los originales de `03 Planos/PDF/` (no desde los del usuario) con doc-annotator, cada comentario como NOTA-XX/OBS-XX, **conservando el texto de los 11 comentarios del usuario** marcados [U] + los [A] de ADASA. En planos `search` casi nunca ancla → usar `page_fallback` (0-based).
- **MC con ítems abiertos** (001, 004, 005, 003-001 + las NOTA de 002): CC_ADASA con recuadros ≤8 líneas Defecto→Corregir→Requisito.
- IDs deben coincidir entre este `_ANALISIS`, el TRANSMITTAL.md y los scripts.
