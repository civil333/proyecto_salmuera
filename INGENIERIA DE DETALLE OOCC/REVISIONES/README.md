# REVISIONES OOCC — Stream L&A (Obras Civiles y Estructuras Metálicas)

Flujo de revisión técnica de los entregables de L&A Ingeniería y Proyectos SpA para la Ingeniería de Detalle de Obras Civiles y Estructuras Metálicas del Módulo RO 2da Etapa Salmuera Taltal. Espejo en español del flujo de transmittales ADASA → BW Water, independiente del árbol `REVISIONES\` raíz del proyecto (que es exclusivo del stream BW Water, inglés).

**Contraparte:** L&A Ingeniería y Proyectos SpA — Pablo Castillo (pcastillo@lyaingenieria.cl)
**Términos de Referencia:** `P22-TR-00-010-01-0\P22-TR-00-010-01-1(Ingenieria OOCC Modulo Taltal).pdf` (Rev 1, 24-Abr-2026)
**Codificación transmittales:** `P22-TM-00-010-NNN-0` (área 00, disciplina 010, consistente con `P22-TR-00-010` y `P22-MC-00-002-00X`).

## Estructura

```
REVISIONES\
├── README.md                         (este archivo — índice + trazabilidad)
├── Hitos de revision.md              (bitácora de revisiones OOCC)
├── TRANSMITTALES\P22-TM-00-010-NNN-0\
│       ├── crear_transmittal.py
│       ├── P22-TM-00-010-NNN-0_TRANSMITTAL.md   (español, se envía a L&A)
│       ├── _ANALISIS_TRABAJO.md                 (interno, NO se envía)
│       ├── TRANSMITTAL NX ADASA-LYA.docx / .pdf
│       └── COMENTARIOS\ (agregar_comentarios_*.py + *_CC_ADASA.pdf)
├── SUBMITTALS\ENTREGA-N\              (extracción .md de entregas)
├── EVALUACIONES\
└── CONSULTAS_TECNICAS\RESPUESTA\
```

## Códigos de respuesta (Términos de Referencia — Sección 6.2)

| Código | Significado | Próxima revisión L&A |
|--------|-------------|----------------------|
| 1 | Aprobado | IFC directo (Rev 0) |
| 2 | Aprobado con comentarios | IFC directo (Rev 0); comentarios incorporados sin nueva Rev B |
| 3 | Por revisar | Nueva Rev B.1 |
| 4 | Rechazado | Rehacer |

Ciclo de revisión: Rev A → Rev B → (Rev B.1 opcional) → Rev 0. Máximo 2 × Rev B.

## Trazabilidad de documentos

| Documento | Código | Rev | Entrega | Transmittal | Cód. Resp. | Fecha | Estado |
|-----------|--------|-----|---------|-------------|-----------|-------|--------|
| Fundación Estanque TK-06-001 | P22-MC-00-002-001 | B | ENTREGA 3 | P22-TM-00-010-001-0 | 3 | 19-May-2026 | Rev B.1 — rediseñar anclaje preinstalado (colado en sitio) ACI 318-19; + OBS-NPT |
| Fundación Dinámica Bomba BH-06-001 | P22-MC-00-002-002 | B | ENTREGA 3 | P22-TM-00-010-001-0 | 2 | 19-May-2026 | Comentarios a Rev 0 — OBS-NPT; peso BH-06-001 ficha técnica KSB (escala a Cód. 3 si ACI 351.3R no cumple) |
| Fundación Contenedor RO | P22-MC-00-002-004 | B | ENTREGA 3 | P22-TM-00-010-001-0 | 2 | 19-May-2026 | Comentarios a Rev 0 — OBS-NPT; retirar cargas CIP/dosificación (van en MC-005); peso contenedor 14.934 kg (TR 2.1.2 / P22-DWG-09-005-001 Rev A) |
| Fundación Sistema CIP | P22-MC-00-002-005 | B | ENTREGA 3 | P22-TM-00-010-001-0 | 2 | 19-May-2026 | Comentarios a Rev 0 — anclaje (postinstalado) diferido por datos del proveedor (PEND-03); + OBS-NPT; pesos dosificación ≈550 kg |
| Cubierta Metálica Sistema CIP | P22-MC-00-003-001 | B | ENTREGA 3 | P22-TM-00-010-001-0 | 3 | 19-May-2026 | Rev B.1 — reconciliar clasificación de suelo D vs E; declarar protección C5-M |
| Sistema de Drenajes (fosa + cámaras) | P22-MC-00-002-003 | 0 | ENTREGA 10 (recibida) | — | — | 23-Jun-2026 | **Recibida en la ENTREGA 10 (Rev 0)** tras declararse sin archivo en E5/E7. Fuera del paquete de licitación (las MC no se distribuyen); copia de trazabilidad en `BORRADOR_REV0/_memorias_excluidas_del_paquete/` |

## Pendientes y dependencias abiertas

- **PEND-01** — Entregables comprometidos (TdR Sección 6 + Listado 067-032-032-COR-LI-001) solicitados en el TM N2. **Cierre parcial en ENTREGA 5 (09-Jun-2026):** recibido el plano de Excavaciones y Movimiento de Tierras (P22-DWG-00-001-001 Rev B, 2 láminas). La MC Sistema de Drenajes (P22-MC-00-002-003 Rev 0) figura **declarada en la carta TT-006 (ítem 9) pero el archivo no viene en la entrega** (L&A incluyó por error la Rev 0 antigua de la MC-003-001 Cubierta) → solicitar el archivo. **Sigue pendiente** el plano de Detalles de Anclaje y Conexiones (P22-DWG-00-002-005), ni declarado ni incluido. **Cierre en ENTREGA 9 (22-Jun-2026):** el plano de Excavaciones pasa a **Rev 0** cubriendo la excavación de fundaciones + cota de plataforma + sello de fundación (cierra el punto rector de las cubicaciones). **DWG-00-002-005 confirmado: NO se emite** (los detalles de anclaje viven en los planos de fundaciones 002-002/003/007; retirado de las referencias del BL). **P22-MC-00-002-003 (MC de Drenajes): no forma parte del paquete de licitación** (las MC no se distribuyen al oferente); su no-entrega no afecta el dossier. PEND-01 cerrado a efectos del paquete.
- **PEND-02** — Las reacciones basales del estanque TK-06-001 (usadas en P22-MC-00-002-001) dependen de la ratificación del antecedente Exfibro Memoria Rev B. ADASA lo gestiona vía consulta técnica P22-CT-06-000-002-0. L&A ya adoptó los valores corregidos por ADASA (Ez ±3.357 kgf).
- **PEND-03** — Verificación de anclajes de MC-005 diferida por falta de planos/fichas finales del proveedor de equipos CIP; serán postinstalados; completar con anclajes postinstalados que cumplan las solicitaciones (ACI 318-19 Cap. 17/Sección 17.10; ACI 355.2/355.4 + ESR ICC-ES) cuando se disponga de los datos. No es rechazo.
- **NPT (transversal)** — El NPT es dato fijo de los planos de montaje (TdR Secciones 3.3.1/4.1), verificable contra el Levantamiento DIO Abr-2026. **Refinado en TM N2:** los planos del estanque, la bomba y la fosa ya lo declaran y coinciden con el montaje (+5,75) → conforme, se deja pasar en sus memorias; los planos del contenedor RO (datum relativo) y del Sistema CIP (+5,610) deben reconciliar el N.T.N. absoluto con el plano de montaje P22-DWG-06-005-103. La observación de NPT en el TM N2 queda solo en los planos -001/-003/-007 (no en las memorias cuyo plano ya lo refleja).

## Transmittales emitidos

| TM | Fecha | Entrega | Docs | Veredicto | Estado |
|----|-------|---------|------|-----------|--------|
| P22-TM-00-010-001-0 | 19-May-2026 | ENTREGA 3 | 5 MC Rev B | 3 — Por revisar (3 Cód. 2 + 2 Cód. 3; drivers MC-001 y MC-003-001) | BORRADOR (versión ejecutiva) |
| P22-TM-00-010-002-0 | 01-Jun-2026 | ENTREGA 4 | 18 docs (5 MC + 3 ET + 3 IT + 7 planos) | 3 — Por revisar (7 Cód. 2 + 11 Cód. 3; drivers planos, Itemizados, MC-001 anclaje, MC-003-001) | ENVIADO 01-Jun-2026 (TRANSMITTAL N2 ADASA-LYA.pdf) |
| P22-TM-00-010-003-0 | 10-Jun-2026 | ENTREGA 5 | 19 docs (5 MC Rev 1 + 3 ET Rev 0 + 3 IT Rev C + 8 planos Rev C/B) | 3 — Por revisar (9 Cód. 2 + 10 Cód. 3 + 1 sin código; drivers planos, Itemizados, mejoramiento de suelo ausente, plano de excavación de fundaciones faltante) | ENVIADO 10-Jun-2026 (TRANSMITTAL N3 ADASA-LYA.pdf + 25 CC_ADASA + correo de remisión) |
| P22-TM-00-010-004-0 | 18-Jun-2026 | ENTREGA 7 | 19 docs (5 MC Rev 2 + 3 ET Rev 1 + 3 IT Rev D + planos Rev D/C) | 3 — Por revisar (7 Cód. 1 + 6 Cód. 2 + 6 Cód. 3) | **Solo comentarios enviados** — CC_ADASA (`COMENTARIOS.rar`, 16 archivos) por correo directo de L. Rivera (Reply a la cadena TT-008) 18-Jun; **el transmittal NO se emitió** (existe como base interna). Ningún comentario nuevo (14 desde TM N2, 4 desde TM N3); invoca el límite de ciclo del TdR |

## ENTREGA 10 — Recepción y actualización del paquete (23/25-Jun-2026)

Carta de transmisión 067-032-032-COR-TT-011 (23-Jun-2026, "COMPILADO"): L&A re-emite el set civil completo un día después de la E9. La diferencia material es la **corrección del estado del cajetín de la Rev 0**: en las **18 láminas** la fila Rev 0 de la tabla REVISIONES pasa de **"PARA USO E INFORMACIÓN"** a **"APTO PARA CONSTRUCCIÓN"** (misma geometría, misma Rev 0); en las **2 ET** (Movimiento de Tierra y Obras Civiles, Rev 1) la portada pasa del estado **"Aprobado Cliente"** a **"Apto para Construcción"**. La entrega trae además 6 MC (incluida la nueva **MC-002-003 Rev 0** de Drenajes), 4 Itemizados y los documentos de la cubierta.

**Verificación (compuerta antes de tocar el paquete):** las 18 láminas se extrajeron con **large-pdf-reader modo drawing**; se confirmó por render del recorte de la tabla REVISIONES que las 18 traen Rev 0 = "APTO PARA CONSTRUCCIÓN" (diff de control contra las versiones E8/E9 del paquete, que mostraban "PARA USO E INFORMACIÓN"). El cambio de estado de las ET se confirmó por diff del texto de portada. Es una re-emisión solo de cajetín/estado, sin cambio de contenido.

**Actualización del paquete (25-Jun-2026, solo la parte civil — decisión del usuario):** las 18 láminas + 2 ET del dossier `Bases REV 0/5. OBRAS CIVILES (A2)/` se reemplazaron por la versión E10 (byte-idénticas a la fuente E10, verificado por SHA256); las E8/E9 se archivaron en `BORRADOR_REV0/_dossier_superseded_pre-E10/`. El cuerpo del BL se regeneró con `md_to_adasa_docx.py` (`[CHEQUEO LAYOUT] OK`) declarando los planos "en revisión 0, apto para construcción" (Antecedentes, Anexo A2 y la fila A2 de la Sección 9); PDF re-exportado por Word COM (win32com late binding). LEEME e ÍNDICE del paquete actualizados; carpetas excluidas refrescadas a E10 (cubierta → ET-103 Rev 1, MC-003-001 Rev 2; memorias → +MC-002-003 Rev 0). El **Formato de Presupuesto (A9) no se tocó**. Sin transmittal a L&A (verificación interna, coherente con el cierre E9/TM N4). Ver memoria `project_entrega10_cierre_civil_rev0`.

## ENTREGA 9 — Recepción y verificación interna (23-Jun-2026)

Carta de transmisión 067-032-032-COR-TT-010 (22-Jun-2026): las **5 láminas civiles** que quedaban con letra tras la ENTREGA 8 pasan a **Rev 0**, más la re-emisión completa de la fosa — 6 láminas: DWG-00-001-001 LAM1/LAM2 (Excavaciones), DWG-00-002-003 LAM2/LAM3 (Fundación contenedor), DWG-00-002-007 LAM2 (Fundación CIP) y DWG-00-002-004 LAM1 (Fosa). El set de planos civiles del paquete de licitación queda **completo en Rev 0 (18/18 láminas)**.

**Verificación interna, sin transmittal a L&A** (coherente con la postura del TM N4: ciclo del TdR ya excedido invocado, ADASA avanza la licitación en paralelo). Revisión cruzada con workflow de 5 revisores por dimensión + verificación adversarial + síntesis (render PNG con PyMuPDF de las 6 láminas + referencias + superadas).

**Puntos rectores RESUELTOS:** excavación de fundaciones + plataforma + sello en el plano de Excavaciones Rev 0 (cierra el punto rector del TM N3); N.T.N. acotado por zona; fosa rotulada TK-06-004 (cierra el tag del TM N2); DWG-00-002-003 LAM2 con detalle propio INS-1 (ya no duplica la LAM1).

**Residuales menores (carry-forward, sin hallazgos nuevos):** la nota de mejoramiento de suelo (ET-101) está en las láminas de formas pero no repetida en las de armadura (002-003 LAM2/LAM3, 002-007 LAM2), que remiten a la matriz 002-001 (CF-1); el anclaje de equipos de etapa posterior queda diferido a planos vendor (002-007 LAM1, CF-6). No bloquean la licitación.

**Acciones sobre el paquete:** las 6 láminas Rev 0 se incorporaron a `Bases REV 0/5. OBRAS CIVILES (A2)/PLANOS/`; las superadas (Rev C/B + el *stub* defectuoso de 002-004 LAM1 que había entrado con la E8 sin cajetín) se archivaron en `BORRADOR_REV0/_dossier_superseded_pre-E9/`; LEEME e ÍNDICE del paquete actualizados a "18/18 Rev 0". Cubicación del Formato (A9): 4.8 excavación 115,1 m³ consistente con el plano (≈91 m³ geométrico + 20 % de esponjamiento que el plano declara); 4.9 relleno 91,5 m³ a revisar contra el plano (el plano solo tabula relleno de trazado, ≈38,7 m³). Ver memoria `project_entrega9_cierre_civil_rev0`.

## ENTREGA 7 — Recepción y Disposición (Revisión Técnica N4, 18-Jun-2026)

Carta de transmisión 067-032-032-COR-TT-008 (17-Jun-2026): 24 ítems — respuesta de L&A a los comentarios del TM N3. 5 Memorias de Cálculo Rev 2, 3 Especificaciones Técnicas Rev 1, 3 Itemizados Rev D, P22-IT-00-010-001-0 Rev 0 (Estimación de Inversión), planos en Rev D (+ DWG-00-001-001 Excavaciones Rev C). Verificación de levantamiento en `TRANSMITTALES/P22-TM-00-010-004-0/_ANALISIS_TRABAJO.md`. **Recuento interno: 7 Código 1 + 6 Código 2 + 6 Código 3; veredicto 3 — Por revisar.**

**Lo que se envió — SOLO los comentarios, no el transmittal.** El 18-Jun-2026 (12:05) Luis Rivera respondió la cadena del correo TT-008 con un mensaje directo a Pablo Castillo (CC equipo L&A/ADASA) adjuntando **`COMENTARIOS.rar`** (16 CC_ADASA: las MC/IT/planos con observación abierta). **El transmittal P22-TM-00-010-004-0 NO se emitió** — el `.docx` y el `_ANALISIS_TRABAJO.md` quedan como base interna. El correo plantea que no hay comentarios nuevos (todos son puntos sin cerrar desde transmittals anteriores), que lo medular sigue sin levantarse desde el TM N2 (mejoramiento de suelo + ciclo de revisión del TdR ya excedido sin converger), que el respaldo de las cubicaciones de excavación sigue pendiente (DWG-00-001-001 Rev C cubre solo zanjas), y pregunta directo si L&A va a abordarlo porque ADASA **espera la Rev 0 para poder licitar**. Respaldo del envío: `CORREOS/Junio 2026/2026-06-18/correo enviado a LYA.pdf`.

**Por qué solo comentarios y no un transmittal formal (decisión del usuario):** los puntos pendientes son refinamientos de documentación/especificación que **no impiden la construcción** (se incorporan al emitir Rev 0), y ADASA necesita **iniciar ya el proceso de licitación**; por eso se deja el registro de forma directa y se avanza con el tender **en paralelo**, sin esperar la convergencia formal de L&A a Rev 0. La licitación de montaje/OOCC se arma con el Formato de Presupuesto propio de ADASA (no con los Itemizados de L&A), de modo que el punto rector de las cubicaciones es deuda de documentación de L&A, no un bloqueo del tender. El transmittal P22-TM-00-010-004-0 queda disponible internamente por si hay que escalar el registro contractual del límite de ciclo.

**Calibración del usuario (18-Jun):** Código 1 y Código 2 → emitir en Rev 0 (13 docs; las observaciones Código 2 son menores e incorporables sin revisión intermedia); **Clase 2 AACE reclasificada menor** → los 3 Itemizados suben de Código 3 a Código 2; **MC-002-001 → Código 2 con condiciones** (justificar armadura + reconciliar empotramiento memoria-plano; no regresión); **única regresión DWG-00-003-001 (2→3)** (sigla C5-M en la LAM2 no re-emitida; discrepancia carta Rev D / cajetín Rev 0); **se invoca el límite de ciclo del TdR** (anclado en los planos no convergentes desde el TM N2; AACE no es driver).

**Narrativa "ningún comentario nuevo":** los 18 comentarios trazan a un transmittal anterior — 14 desde el TM N2 (3ª vez) y 4 desde el TM N3 (plano de Excavaciones, nuevo en ese ciclo). Cada comentario lleva su transmittal de origen en el transmittal y en los CC_ADASA. Coherencia del ciclo: el plano Exfibro del anclaje del estanque se referencia como EX-26005-F01 **Rev 0** (MC-002-001 + DWG-00-002-002 LAM2); la LAM4 (bomba) usa el plano KSB (no Exfibro) y su nota estaba levantada.

**Re-emisión parcial de láminas / faltantes:** DWG-00-002-006 llegó solo con L3 (faltan L1/L2, nomenclatura CD-06-00N); -002-007 solo con L1 (falta L3); -003-001 solo con L1 (falta L2). **MC-002-003 (Sistema de Drenajes) y DWG-002-005 (Detalles de Anclaje) sin entregar por 3ª vez consecutiva.** Plazos planteados (versión extensa del correo, no en el enviado directo): reposición 24-Jun, revisión a Rev 0 el 02-Jul. Ver memoria `project_tm_oocc_004_hallazgos`.

## ENTREGA 6 — Recepción y análisis (10/11-Jun-2026)

Carta de transmisión 067-032-032-COR-TT-007 (10-Jun-2026, mismo día del envío del TM N3): **P22-IT-00-010-001-0 Rev B "Estimación de Inversión"** (PDF + xlsx; Rev A 04-Jun revisión interna, Rev B 10-Jun revisión cliente). Documento nuevo del TdR: roll-up de inversión total del proyecto OOCC — 4.944,5 UF ≈ USD 219.959 (costos directos 2.403,7 UF, GG+Utilidades 64,3% de los directos, costos del dueño 350 UF, contingencia 15%; UF 40.765,97 / USD 916,39 al 04-Jun).

**Análisis interno (11-Jun) — insumo para el próximo TM (N4):** la hoja BASE replica 1:1 las cubicaciones de los Itemizados IT-101/102/103 Rev C revisados en el TM N3, de modo que **hereda completos los defectos ya observados** (fosa rotulada "TK-06-002", sin declaración Clase 2 AACE — solo "Valor Referencial", sin partidas de impermeabilización ni de protección C5-M/soldadura, y cubicaciones de excavación de fundaciones sin plano que las respalde — punto rector del TM N3). Hallazgos propios del documento nuevo: **(a)** panel PV-6 de la cubierta = 118 m² en la BASE vs 25,2 m² del IT-103 Rev C (factor 4,7×, infla el costo de estructuras); **(b)** varilla del estanque rotulada 5/8" vs 1" del IT-102 Rev C. El documento se revisará formalmente en el próximo ciclo; no se re-escopa el TM N3 (ya enviado).

La Estimación sirvió además como fuente consolidada para cargar las cantidades referenciales del Capítulo 4 del Formato de Presupuesto de la BL Montaje (ver actualización 11-Jun del paquete `Bases REV 0`).

## ENTREGA 5 — Disposición (P22-TM-00-010-003-0, 10-Jun-2026)

Revisión de levantamiento de los puntos del TM N2 contra la ENTREGA 5 + primera revisión de los documentos nuevos. **Recuento 9 Código 2 + 10 Código 3 + 1 sin código (MC-002-003 no recibida); veredicto 3 — Por revisar.**

**Logros del ciclo:** anclaje del estanque rediseñado a preinstalado colado **en el plano** (cierre del punto más antiguo del stream, abierto desde el TM N1); datum absoluto del contenedor RO; N.T.N. del Sistema CIP reconciliado (+6,000); pendientes de drenaje acotadas; cuadro de coordenadas UTM en la implantación; impermeabilización en la ET-102 y nota general; C5-M completo en la MC de la cubierta. Las 6 MC + 3 ET quedan en vía a Rev 0 (Código 2).

**Determinantes del Código 3:** (1) mejoramiento de suelo (ET-101) ausente en todos los planos de fundación, 2º ciclo consecutivo; (2) **el plano de Excavaciones (DWG-00-001-001 Rev B) cubre solo las zanjas de drenaje → las cubicaciones de excavación de fundaciones no tienen plano que las respalde** (punto rector del correo); (3) los 3 Itemizados sin levantar nada (Clase 2 AACE, tag fosa TK-06-004, partidas faltantes, hoja "La Chimba"); (4) N.T.N. por zona sin acotar en la implantación.

**Fallas de entrega elevadas en el correo de remisión:** MC-002-003 (no llegó), DWG-00-002-003 LAM2 (duplicada de LAM1, falta detalle INS-1), DWG-00-002-006 LAM3 (detalle de cámara, no incluida), DWG-00-002-005 (anclajes/conexiones, nunca entregado).

**Calibración del usuario (10-Jun):** MC-001 → Código 2 (armadura @200 aceptable por ACI 318 — la losa es fundación de estanque PRFV apoyado, no contención de líquido; solo justificar el cálculo, preferir Ø16@200); ET-103 → Código 2 duro; anclaje postinstalado de la bomba aceptado (planos KSB); no invocar el límite del ciclo del TdR (TM 100% técnico).

**Estado:** ENVIADO a L&A el 10-Jun-2026. `TRANSMITTAL N3 ADASA-LYA.pdf` + 25 CC_ADASA (5 MC + 3 ET + 14 láminas de plano + 3 Itemizados Excel) + correo de remisión a Pablo Castillo (`CORREOS/Junio 2026/2026-06-10/`). Ver memoria `project_tm_oocc_003_hallazgos`.

## ENTREGA 5 — Recepción (09-Jun-2026)

Carta de transmisión 067-032-032-COR-TT-006 (09-Jun-2026): 31 ítems declarados que responden al TM N2 — Memorias de Cálculo en Rev 1 (MC-001/-002/-004/-005/-003-001), 3 Especificaciones Técnicas directo en Rev 0 (consistente con su Código 2), 3 Itemizados Rev C y planos en Rev C, incluido el **plano nuevo P22-DWG-00-001-001 Rev B (Excavaciones, 2 láminas)**.

Anomalías administrativas detectadas a la recepción (verificación de carátulas 10-Jun):
- **MC-002-003 (Sistema de Drenajes) declarada en la carta (ítem 9, Rev 0) pero el archivo NO viene en la entrega**: en su lugar L&A incluyó la Rev 0 antigua (28-May, Entrega 4) de la MC-003-001 Cubierta — verificado por carátula de ambos PDF. Solicitar el archivo correcto.
- P22-DWG-00-002-007 mezcla láminas: LAM1/LAM3 Rev C, LAM2 Rev B (28-May) — así declarado en la propia carta (ítem 28).
- **P22-DWG-00-002-005 (Detalles de Anclaje y Conexiones) sigue sin entregarse** (ni declarado ni incluido).
- Los títulos de la carta siguen rotulando la fosa como TK-06-002 (el TM N2 exigió TK-06-004).

Revisión en curso → P22-TM-00-010-003-0 (matriz de levantamiento de los puntos del TM N2 + primera revisión de MC-002-003 y DWG-00-001-001).

## ENTREGA 4 — Disposición (P22-TM-00-010-002-0, 01-Jun-2026)

Revisión de la ENTREGA 4 (cover L&A 067-032-032-COR-TT-005, 28-May-2026). 18 documentos; recuento **7 Código 2 + 11 Código 3**; veredicto global **3 — Por revisar**.

| Documento | Código | Acción a Rev 0 |
|-----------|--------|----------------|
| P22-MC-00-002-001 Fundación Estanque | 3 | Rediseñar anclaje preinstalado colado (ACI 318-19), como en TM N1 |
| P22-MC-00-002-002 Fundación Bomba | 2 | Declarar recubrimientos 50/70 mm |
| P22-MC-00-002-004 Fundación Contenedor RO | 2 | Peso ~17,3 t aceptado como conservador; unificar ACI 318-19; recubrimientos |
| P22-MC-00-002-005 Fundación Sistema CIP | 2 | Recubrimientos; anclaje CIP diferido en seguimiento (datos del proveedor, PEND-03) |
| P22-MC-00-003-001 Cubierta Metálica | 3 | Declarar C5-M (o referir ET) y reemitir anexos a Rev 0 |
| P22-ET-00-010-101 Movimiento de Tierra | 2 | Mejoramiento de suelo como condición; particularizar a Taltal |
| P22-ET-00-010-102 Obras Civiles | 2 | Recubrimientos 50/70 mm (TdR Sección 3.3.4) e impermeabilización |
| P22-ET-00-010-103 Estructura Metálica | 2 | Esquema C5-M por capas + AWS D1.1 |
| P22-IT-00-010-101/-102/-103 Itemizados | 3 | Declarar Clase 2 AACE (Minuta arranque); tag fosa TK-06-004; quitar pestaña ajena; partidas faltantes |
| P22-DWG-00-002-001/-002/-003/-004/-006/-007 Planos | 3 | Comentarios por lámina (NPT/montaje, anclajes, mejoramiento de suelo, parrilla PRFV, nomenclatura cámaras) |
| P22-DWG-00-003-001 Cubierta metálica | 2 | Declarar C5-M por nota referida a la ET de Estructura Metálica |

**Calibración del usuario (11 comentarios del revisor + 3 follow-ups):** NPT es dato fijo de montaje — estanque/bomba/fosa coinciden (+5,75, se deja pasar en sus memorias), contenedor/CIP reconcilian con el montaje (queda solo en los planos -003/-007); peso del contenedor ~17,3 t aceptado conservador (no rechazo); anclaje CIP diferido aceptado; las ET genéricas en el título NO se rechazan (Código 2); Itemizados referenciales OK, solo declarar Clase 2 AACE. **Convención Código 1** declarada (documentos no listados = Aprobados). El listado de comentarios a planos del transmittal es **espejo 1:1 de los CC_ADASA** (mismos IDs OBS/NOTA por lámina). Los CC_ADASA de planos rotados se corrigieron con **doc-annotator v1.6** (texto que salía boca abajo en `rotation=90`).
