---
second_brain: skip
type: otro
project: salmuera-taltal
date: 2026-06-18
---

# Verificacion de Levantamiento — ENTREGA 7 vs TM N3 (P22-TM-00-010-003-0)

**Documento de trabajo interno — NO SE ENVIA.** Insumo de calibracion para el usuario antes de redactar el TM N4. Stream OOCC / L&A. Consolida las cuatro matrices de disciplina ya verificadas adversarialmente (workflow 9 agentes, diff de contenido E5->E7).

- **Entrega verificada:** ENTREGA 7 (carta de remision 067-032-032-COR-TT-008, 17-06-2026, P. Castillo -> L. Rivera).
- **Referencia de levantamiento:** TM N3 = P22-TM-00-010-003-0 (enviado 10-Jun-2026 contra ENTREGA 5).
- **Metodo:** diff de contenido E5 -> E7 (no por letra de cajetin). Datos graficos confirmados leyendo los tiles/full.png como imagen; xlsx por celda exacta + enumeracion de hojas; docx por texto extraido. Las cuatro matrices de disciplina son autoritativas.

---

## 1. Inventario E7 vs carta TT-008 + faltantes / anomalias

### 1.1 Carta vs archivos fisicos recibidos

| Documento declarado en carta TT-008 | Rev en carta | Disposicion | Archivo fisico en E7 | Consistencia |
|---|---|---|---|---|
| P22-MC-00-002-001 (Fundacion Estanque TK-06-001) | 2 | Para Uso e Informacion | `Documentos/P22-MC-00-002-001_2.docx/.pdf` | OK |
| P22-MC-00-002-002 (Fundacion Dinamica Bomba BH-06-001) | 2 | Para Uso e Informacion | `Documentos/P22-MC-00-002-002_2.docx/.pdf` | OK |
| P22-MC-00-002-004 (Fundacion Contenedor RO) | 2 | Para Uso e Informacion | `Documentos/P22-MC-00-002-004_2.docx/.pdf` | OK |
| P22-MC-00-002-005 (Fundacion Sistema CIP) | 2 | Para Uso e Informacion | `Documentos/P22-MC-00-002-005_2.docx/.pdf` | OK |
| P22-MC-00-003-001 (Estructura Metalica + Fundaciones Cobertizo) | 2 | Para Uso e Informacion | `Documentos/P22-MC-00-003-001_2.docx/.pdf` | OK |
| P22-MC-00-002-003 (Sistema de Drenajes) | — | — | **NO incluido** | **FALTANTE (3a vez)** |
| P22-ET-00-010-101-0 (Movimiento de Tierra) | 1 | Revision Cliente | `Documentos/P22-ET-00-010-101-0_1.doc/.pdf` | OK |
| P22-ET-00-010-102-0 (Obras Civiles) | 1 | Revision Cliente | `Documentos/P22-ET-00-010-102-0_1.doc/.pdf` | OK |
| P22-ET-00-010-103-0 (Estructura Metalica) | 1 | Revision Cliente | `Documentos/P22-ET-00-010-103-0_1.doc/.pdf` | OK |
| P22-IT-00-010-101-0 (Itemizado Mov. Tierra) | D | Revision Cliente | `Documentos/P22-IT-00-010-101-0_D.xlsx/.pdf` | OK |
| P22-IT-00-010-102-0 (Itemizado Obras Civiles) | D | Revision Cliente | `Documentos/P22-IT-00-010-102-0_D.xlsx/.pdf` | OK |
| P22-IT-00-010-103-0 (Itemizado Estructura Metalica) | D | Revision Cliente | `Documentos/P22-IT-00-010-103-0_D.xlsx/.pdf` | OK |
| P22-IT-00-010-001-0 (Estimacion de Inversion) | 0 | Para Uso e Informacion | `Documentos/P22-IT-00-010-001-0_0, Estimacion de Inversion.xlsx/.pdf` | OK (insumo, no del paquete de licitacion) |
| P22-DWG-00-001-001 (Excavaciones / Canalizaciones) | C | Revision Cliente | `Planos/...001-001_C LAM 1.pdf` + `LAM 2.pdf` | OK (L1+L2) |
| P22-DWG-00-002-001 (Implantacion / Disposicion OOCC) | D | Revision Cliente | `Planos/...002-001_D.pdf` | OK |
| P22-DWG-00-002-002 (Fundacion TK / Anclaje / Bomba) | D | Revision Cliente | `Planos/...002-002_D LAM1/LAM2/LAM4.pdf` | OK (L1, L2, L4) |
| P22-DWG-00-002-003 (Fundacion Contenedor) | D | Revision Cliente | `Planos/...002-003_D LAM1.pdf` | **Parcial: solo L1** |
| P22-DWG-00-002-004 (Fosa de Drenaje) | D | Revision Cliente | `Planos/...002-004_D LAM1/LAM2.pdf` | OK (L1, L2) |
| P22-DWG-00-002-006 (Camaras CD-06-00N) | D | Revision Cliente | `Planos/...002-006_D LAM 3.pdf` | **Parcial: solo L3** (L1 y L2 no re-emitidas) |
| P22-DWG-00-002-007 (Fundacion CIP) | D | Revision Cliente | `Planos/...002-007_D LAM1.pdf` | **Parcial: solo L1** (L3 no re-emitida) |
| P22-DWG-00-003-001 (Cubierta / Estructura Cobertizo) | **D (carta)** | Para Uso e Informacion | `Planos/...003-001_0 LAM1.pdf` | **DISCREPANCIA: archivo y cajetin = Rev 0; solo L1** (L2 no re-emitida) |
| P22-DWG-00-002-005 (Detalles de Anclaje y Conexiones) | — | — | **NO incluido** | **FALTANTE (3a vez)** |

Recuento de la carta: 24 documentos (15 "Revision Cliente" + 9 "Para Uso e Informacion"); **0 "Para Construccion"**.

### 1.2 Faltantes no declarados ni incluidos (3a vez consecutiva)

- **P22-MC-00-002-003 (Sistema de Drenajes):** ausente por tercera entrega consecutiva. No declarado en la carta ni incluido como archivo.
- **P22-DWG-00-002-005 (Detalles de Anclaje y Conexiones):** ausente por tercera entrega consecutiva. Es el plano que cierra la coherencia memoria-plano del anclaje preinstalado (OBS-01 de MC-002-001): su ausencia deja esa observacion no verificable en cruce directo.

### 1.3 Laminas no re-emitidas (cargan comentarios abiertos)

| Plano | Laminas re-emitidas en E7 | Laminas NO re-emitidas | Comentario abierto que queda colgado |
|---|---|---|---|
| DWG-00-002-003 | L1 | (la entrega de E5 solo tenia L1; sin cambio de alcance) | OBS-01 (mejoramiento + relleno) vive en L1, re-emitida pero sin cambio |
| DWG-00-002-006 | L3 (nueva) | L1 (Planta General Canalizaciones), L2 | OBS-01 nomenclatura CD-06 en L1 -> no migra completa a L3 |
| DWG-00-002-007 | L1 | L3 | OBS-01 (mejoramiento + impermeabilizacion + relleno 1,96 m3) tambien vivia en L3 -> no verificable |
| DWG-00-003-001 | L1 | L2 | NOTA-01 (sigla C5-M "P22-IT" -> "P22-ET-00-010-103-0") vive en L2 -> no verificable |

**Regla aplicada:** comentario sobre lamina no re-emitida = NO VERIFICABLE -> se trata como NO LEVANTADO a efectos de codigo, salvo que el contenido haya migrado completo a otra lamina entregada.

### 1.4 Anomalia DWG-00-003-001 (carta Rev D vs archivo Rev 0)

La carta TT-008 declara el plano como **Rev D**, pero el nombre del archivo es `..._0 LAM1.pdf` y el cajetin / bloque de revisiones de la lamina muestran **Rev 0, motivo "PARA USO E INFORMACION", 17/06/26** (salta de la letra C al numero 0). Discrepancia administrativa carta <-> plano a registrar. Ademas, la fecha de la casilla principal del cajetin quedo congelada en 09/06/26 (fecha de la Rev C) mientras la fila Rev 0 dice 17/06/26.

### 1.5 Tag TK-06-002 persistente a nivel de carta y de la Estimacion de Inversion

La carta TT-008 sigue rotulando la fosa como **"TK-06-002"** en los titulos de DWG-00-002-004 (tag incorrecto: la Fosa de Drenajes ADASA es **TK-06-004**; TK-06-002 es el estanque CIP de BW Water). El mismo tag erroneo persiste dentro de la hoja BASE del IT-001-0 (Estimacion de Inversion), celdas B28 y B54, **aunque los itemizados IT-101/IT-102 Rev D ya lo corrigieron a TK-06-004 el mismo dia**. En los planos DWG el tag de tanque ya no apunta al CIP (corregido a "...-004"), con la salvedad del formato no unificado en DWG-002-004 L2 (ver Seccion 2).

---

## 2. Matriz de levantamiento (42 comentarios)

Columnas: ID | Documento / Lamina | Rev E5->E7 | Comentario TM N3 (resumen) | Evidencia en E7 (pagina/celda/tile) | Estado | Codigo propuesto.

### 2.A Disciplina A — Memorias de Calculo (5 docx, Rev 1 -> 2)

| ID | Documento / Lamina | Rev E5->E7 | Comentario TM N3 (resumen) | Evidencia en E7 (pagina/celda/tile) | Estado | Codigo propuesto |
|---|---|---|---|---|---|---|
| OBS-01 | P22-MC-00-002-001 | 1->2 | Coherencia memoria-plano del anclaje: quitar HAS-V-36, unificar empotramiento al plano (38 cm), mostrar modos de falla del preinstalado. Req.: ACI 318-19 Cap.17/17.10; plano Exfibro EX-26005-F01 Rev C | `_extracted.md` p.25: "pernos de anclaje preinstalado de 1\" de calidad ASTM F1554 Gr.36... empotramiento de 30 cm" (HAS-V-36 eliminado; E5 decia "varilla HAS-V-36... 40 cm"). Tabla de modos de falla NUEVA (p.24). PERO empotramiento bajo a 30 cm — empeora la divergencia con el plano (38 cm) vs los 40 cm de E5; DWG-00-002-005 (plano de anclaje) NO re-emitido -> coherencia no verificable | PARCIAL | 2 (condicion a Rev 0) |
| OBS-02 | P22-MC-00-002-001 | 1->2 | Justificar armadura de losa: cuantia minima ACI 318 + flexion/corte con solicitaciones del anclaje; se recomienda Phi16@200 | `_extracted.md` p.35: sigue Phi12@200 sup. e inf. (no se adopto Phi16@200). Frase NUEVA p.35: "...queda controlada por la armadura de retraccion y temperatura". Sin cuantia minima, sin espesor de losa, sin verificacion flexion/corte ligada al anclaje | PARCIAL | 2 (condicion a Rev 0) |
| NOTA-01 | P22-MC-00-002-001 | 1->2 | Trazabilidad de la reaccion basal Ez=+-3.357 kgf: citar P22-IT-06-000-005-0 (no "Memoria Estanque AFTA Taltal") | `_extracted.md` p.17: Ez "segun la actualizacion del valor mencionado en el documento... 'P22-IT-06-000-005-0'" + p.7 agrega el codigo a Documentos de referencia | LEVANTADO | — |
| NOTA-02 | P22-MC-00-002-001 | 1->2 | Recubrimientos: 50 mm expuestos / 70 mm terreno. Req.: TdR 3.3.4 | `_extracted.md` p.8, nueva subseccion 2.4.3: "50 mm para elementos expuestos... 70 mm... contacto con el terreno... ambiente marino corrosivo" (E5 sin seccion de recubrimiento) | LEVANTADO | — |
| NOTA-01 | P22-MC-00-002-002 | 1->2 | Recubrimientos: declaraba solo 70 mm; falta 50 mm expuesto. (Anclaje postinstalado bomba YA aceptado conforme KSB — no reabrir) | Sec. 2.4.3: "50 mm para elementos expuestos... 70 mm... contacto con el terreno". Anclaje postinstalado 5/8" sin cambios (no reabierto) | LEVANTADO | — |
| NOTA-01 | P22-MC-00-002-004 | 1->2 | Recubrimientos 50/70. Arrastre: notacion "17.334 [tonf]" + declarar adopcion conservadora del peso (vs 14.934 kg vinculante del contenedor RO) | Recubrimientos: "50 mm... expuestos... 70 mm... terreno" (typo "recubrimiento mino"). Peso: SIGUE "punto 2.1.2 que corresponde a 17.334 [tonf]" — identico a E5; no corrige notacion ni declara 14.934 kg ni la adopcion conservadora | PARCIAL (sin levantar: notacion "17.334 [tonf]" + adopcion 14.934 kg) | 2 |
| NOTA-01 | P22-MC-00-002-005 | 1->2 | Recubrimientos: declaraba solo 70; falta 50. (Diferimiento anclajes CIP conforme/seguimiento PEND-03 — no reabrir) | Sec. 2.4.3: "50 mm... expuestos... 70 mm... terreno". Diferimiento de anclajes CIP (Sec. 6.2) sin cambios, conforme PEND-03 | LEVANTADO | — |
| NOTA-01 | P22-MC-00-003-001 | 1->2 | Recubrimientos de pedestales 50/70 + dejar explicita la combinacion de cargas adoptada (se expresaba "1,2D+-E"). Req.: TdR 3.3.4; NCh 2369 | Recubrimientos: "50 mm... expuestos... 70 mm... terreno" (E5 no declaraba). Combinacion: YA estaba explicita en E5 (Tablas ASD/LRFD + Tabla 4-5 que define E = +-1,0Ex+-0,3Ey+-0,3Ez); E7 la mantiene. "1,2D+-E" es referencia compacta a una E plenamente definida | LEVANTADO | — |

### 2.B Disciplina B — Especificaciones Tecnicas (Rev 0 -> 1) + Itemizados (Rev C -> D) + IT-001-0

| ID | Documento / Lamina | Rev E5->E7 | Comentario TM N3 (resumen) | Evidencia en E7 (pagina/celda/tile) | Estado | Codigo propuesto |
|---|---|---|---|---|---|---|
| OBS-01 | P22-ET-00-010-101-0 (Mov. de Tierra) | 0->1 | Declarar sigma_adm <= 1,0 kg/cm2 y eliminar la referencia residual a "Municipalidad de Antofagasta" | `_1_extracted.md`: "tension admisible (sigma_ADM) de 1,0 kgf/cm2, por tanto, parametros inferiores no son admisibles" (no existia en E5). "Municipalidad de Antofagasta" eliminada de la frase normativa | LEVANTADO | 1 |
| NOTA-01 | P22-ET-00-010-102-0 (Obras Civiles) | 0->1 | Corregir codigo de portada de tipo IT a P22-ET-00-010-102-0; recubrimientos duales + impermeabilizacion ya OK | portada = `P22-ET-00-010-102-0` (E5 = `P22-IT-00-010-102-0`); 0 codigos `P22-IT-00-010` en el cuerpo de Rev 1 | LEVANTADO | 1 |
| OBS-02 | P22-ET-00-010-103-0 (Estructura Metalica) | 0->1 | Trasladar a la ET el esquema C5-M por capas (SSPC-SP10 + zinc + epoxico + poliuretano), exigir perneria galvanizada en caliente o inoxidable, corregir portada | Esquema por capas verificado por render del tile `et103_rev1_p11.png`: Prep. SSPC-SP10/Sa2 1/2 (perfil 50 um) + Zinc Clad II 80 um + Macropoxy 646 200 um + Acrolon 218 HS 75 um, total >=355 um. Perneria: "galvanizada en caliente... ASTM F2329... o... inoxidable AISI 316 (A4)". Portada = `P22-ET-00-010-103-0` | LEVANTADO | 1 |
| OBS-01 | P22-IT-00-010-101-0 (Mov. Tierra) | C->D | Declarar Clase 2 AACE citando Minuta 067-032-032-COR-MI-001 | `_D` Detalle Presupuesto B5 = "PRESUPUESTO REFERENCIAL"; 0 coincidencias "AACE"/"Clase 2"/"Minuta" en el libro. Identico a E5 Rev C | NO LEVANTADO | 2 (menor; declarar a Rev 0) |
| OBS-02 | P22-IT-00-010-101-0 | C->D | Corregir tag de la fosa TK-06-002 -> TK-06-004 | `_D` Detalle Presupuesto D23 = "Fosa TK-06-004" (E5 Rev C D23 = "Fosa TK-06-002"); sin reaparicion de TK-06-002 en el libro | LEVANTADO | — |
| CHIMBA | P22-IT-00-010-101-0 | C->D | Eliminar la pestana ajena "BOM" = Cuadro de Piezas Especiales Interconexion La Chimba | E7 Rev D SHEETS = ['Tapa','Detalle Presupuesto'] — sin hoja BOM (E5 Rev C tenia BOM!A1 = "...LA CHIMBA") | LEVANTADO | — |
| OBS-01 | P22-IT-00-010-102-0 (Obras Civiles) | C->D | Declarar Clase 2 AACE (Minuta 067-032-032-COR-MI-001) | `_D` B5 = "PRESUPUESTO REFERENCIAL"; 0 coincidencias AACE/Clase 2/Minuta. Igual que E5 Rev C | NO LEVANTADO | 2 (menor; declarar a Rev 0) |
| OBS-02 | P22-IT-00-010-102-0 | C->D | Corregir tag fosa -> TK-06-004 | `_D` Detalle Presupuesto D29 = "Fosa TK-06-004" (E5 = "Fosa TK-06-002"); sin reaparicion TK-06-002 | LEVANTADO | — |
| OBS-03 | P22-IT-00-010-102-0 | C->D | Incorporar partida de impermeabilizacion (la ET-102 especifica Sika Igol) | `_D`: "Sika Igol Primer"/"Sika Igol Denso" en 12 celdas (D18/D19, D27/D28, D34/D35, D40/D41, D48/D49, D56/D57). E5 Rev C: 0 coincidencias -> adicion real | LEVANTADO | — |
| CHIMBA | P22-IT-00-010-102-0 | C->D | Eliminar pestana ajena La Chimba | E7 Rev D SHEETS = ['Tapa','Detalle Presupuesto'] — sin BOM | LEVANTADO | — |
| OBS-01 | P22-IT-00-010-103-0 (Estructura Metalica) | C->D | Declarar Clase 2 AACE (Minuta 067-032-032-COR-MI-001) | `_D` B5 = "PRESUPUESTO REFERENCIAL"; 0 coincidencias AACE/Clase 2/Minuta. Igual que E5 Rev C | NO LEVANTADO | 2 (menor; declarar a Rev 0) |
| OBS-03 | P22-IT-00-010-103-0 | C->D | Incorporar partidas de proteccion C5-M y de soldadura (la ET-103 las declara) | Proteccion C5-M: `_D` D23 y D27 = "Esquema de pintura - Proteccion superficial – C5M" (E5 no las tenia). Soldadura: sin partida explicita — solo "Conexiones 20%" en D17/D19 (igual que E5) | PARCIAL (sin levantar: partida de soldadura; la union soldada sigue absorbida en "Conexiones 20%") | 2 (cond. Rev 0: agregar partida de soldadura + declarar Clase 2) |
| CHIMBA | P22-IT-00-010-103-0 | C->D | Eliminar pestana ajena La Chimba | E7 Rev D SHEETS = ['Tapa','Detalle Presupuesto'] — sin BOM | LEVANTADO | — |
| INFO | P22-IT-00-010-001-0 (Estimacion de Inversion) | NUEVO Rev 0 | (No es comentario emitido) Verificar que NO arrastre defectos heredados: fosa TK-06-002, ausencia Clase 2 AACE, partidas faltantes | Hoja BASE B28 y B54 = "FOSA TK-06-002" (tag incorrecto, NO corregido aunque IT-101/102 si lo hicieron). Sin "AACE"/"Clase 2" en ninguna hoja. BASE sin partidas Sika/Igol, C5-M ni soldadura -> subestima Civil/Estructuras. BASE "Panel PV-6 Prepintado" = 118 m2 vs 25,2 m2 en IT-103 Rev D y ET-103 Rev 1 | NO LEVANTADO (arrastra los 3 defectos heredados; fila informativa) | — (insumo) |

### 2.C Disciplina C — Planos de Fundacion, Implantacion y Fosa (7 laminas, Rev C -> D)

| ID | Documento / Lamina | Rev E5->E7 | Comentario TM N3 (resumen) | Evidencia en E7 (pagina/celda/tile) | Estado | Codigo propuesto |
|---|---|---|---|---|---|---|
| OBS-01 | DWG-00-002-001 (Implantacion / Disposicion OOCC) | C->D | N.T.N. por zona sin acotar; acotar coincidente con montaje -101/-103/-105 y Levantamiento DIO | tile NW: callouts nuevos `+5.750 N.T.N` (TK-06-001), `+6.000 N.T.N` (Fosa de Drenaje), `+6.000 N.T.N` (Estanque CIP TK-09-001). El tile NW de E5 NO tiene cota de N.T.N. por zona. Cambio de contenido real | LEVANTADO | — |
| NOTA-01 | DWG-00-002-001 (Implantacion) | C->D | Fosa figura TK-06-002 y nota C5-M cita sigla "P22-IT"; corregir a TK-06-004 y P22-ET-00-010-103-0 | tile NW: callout `FOSA DE DRENAJE TK-06-004` (E5: `TK-06-002`); tile SE nota 6 C5-M cierra `...ESPECIFICACION TECNICA P22-ET-00-010-103-0` (E5: `P22-IT-00-010-103-0`). Ambas mitades cambiaron de contenido | LEVANTADO | — |
| OBS-01 | DWG-00-002-002 LAM1 (Disposicion Fund. TK - Formas) | C->D | Nota de mejoramiento de suelo ausente; agregar conforme ET-101 | tile SE: NOTAS PARTICULARES solo (1) ref. generales y (2) `VER PLANO VENDOR N° EX-2600-F01`. Byte-identico al SE tile de E5. Sin nota de mejoramiento | NO LEVANTADO | 3 |
| NOTA-01 | DWG-00-002-002 LAM2 (Anclaje Fund. TK) | C->D | Conciliar PA-1 entre laminas y corregir ref vendor a EX-26005-F01 Rev C | NOTAS PARTICULARES nota 2 = `VER PLANO VENDOR N° EX-2600-F01_Rev.C.` IDENTICO al SE tile de E5. El detalle `PERNO PA-2` preinstalado tambien IDENTICO a E5 (la renominacion a PA-2 YA estaba en E5). Numero vendor sigue `EX-2600` (no `EX-26005`) | NO LEVANTADO (numero vendor no corregido; la conciliacion PA-2 ya venia de E5) | 3 (residual; el documento ya es 3 por L1/L4) |
| OBS-01 | DWG-00-002-002 LAM4 (Fund. Bomba) | C->D | Nota de mejoramiento de suelo ausente | tile SW: NOTAS PARTICULARES solo (1) ref. generales y (2) `VER PLANO VENDOR N° KSB-...`. Byte-identico a E5. Sin nota de mejoramiento | NO LEVANTADO | 3 |
| NOTA-01 | DWG-00-002-002 LAM4 (Fund. Bomba) | C->D | PA-1 / ref vendor (igual que L2) | tile SW: `DETALLE PERNO PA-1` postinstalado, IDENTICO a E5; ref vendor = plano KSB. Anclaje postinstalado bomba ya aceptado conforme KSB (carry-forward, no se reabre). PA-1 exclusivo del postinstalado y PA-2 del preinstalado (L2) en ambas entregas -> marcas consistentes | LEVANTADO (estado consistente; ya conforme desde E5) | — |
| OBS-01 | DWG-00-002-003 LAM1 (Fund. Contenedor) | C->D | Nota de mejoramiento ausente; relleno 30,03 m3 sin material/espesor/% compactacion; agregar nota y especificar relleno (ET-101) | tile SE: NOTA PARTICULAR unica (1) ref. generales, IDENTICA a E5; tile E: CUADRO DE EXCAVACION `RELLENO 30,03` m3, unica NOTA `20% DE ESPONJAMIENTO`, sin material/espesor/compactacion. Sin cambio de contenido C->D | NO LEVANTADO | 3 |
| OBS-01 | DWG-00-002-004 LAM1 (Fosa - Formas) | C->D | M.H.A. e=15 no definida en notas/leyenda; impermeabilizacion de enterrados incompleta; declarar mejoramiento (definir "M.H.A.") y completar impermeabilizacion | tile SE: NOTA PARTICULAR (2) NUEVA `CONSIDERAR COMO REVESTIMIENTO INTERIOR SIKATOP SEAL-107 O SIMILAR TECNICO` (E5 solo tenia nota 1); tile E: seccion mantiene rotulo `M.H.A. e=15` SIN nota/leyenda que defina la sigla. Impermeabilizacion agregada; M.H.A. sigue indefinida | PARCIAL (impermeabilizacion agregada via SikaTop Seal-107; falta definir la sigla "M.H.A.") | 3 |
| NOTA-01 | DWG-00-002-004 LAM1+LAM2 (Tag fosa) | C->D | L1=TK-06-004 pero L2=TK-006-002; unificar a TK-06-004 en TODAS las laminas | L1 tile NE: cajetin `FOSA DE DRENAJE TK-06-004 - FORMAS`; L2 tile SE: cajetin `FOSA DE DRENAJE TK-006-004 - ARMADURA`. E5 L2 decia `TK-006-002`. Se corrigio el digito de tanque (2->4) pero el formato sigue `TK-006-004` (cero de mas) | PARCIAL (L2 paso de TK-006-002 a TK-006-004; falta unificar formato: L1=TK-06-004 vs L2=TK-006-004) | 3 |
| OBS-02 | DWG-00-002-004 LAM2 (Fosa - Armadura/Detalles) | C->D | Aperturas de rebalse no indicadas; detalle conservaba "PARRILLA PISO ARS-5" (acero); agregar/acotar rebalse y especificar parrilla PRFV pultruida | tile NW: PLANTA INFERIOR sin apertura de rebalse acotada, IDENTICO a E5; tile E: CUADRO DE MATERIALES `PARRILLA DE PISO FRP` (ya estaba en E5) pero `DETALLE APOYO DE PARRILLA` sigue rotulando `PARRILLA PISO ARS-5` (acero). Byte-identico a E5 | NO LEVANTADO | 3 |

### 2.D Disciplina D — Planos Excavacion, Canalizaciones, Fundacion CIP y Cubierta (5 laminas)

| ID | Documento / Lamina | Rev E5->E7 | Comentario TM N3 (resumen) | Evidencia en E7 (pagina/celda/tile) | Estado | Codigo propuesto |
|---|---|---|---|---|---|---|
| OBS-01 [RECTOR] | DWG-00-001-001 L1 | B->C | Alcance incompleto: solo zanjas de drenaje; faltan excavaciones de fundaciones (estanque, bomba, fosa, contenedor RO, CIP), niveles de plataforma y N.T.N. por zona | Cuadro CUBICACIONES MOVIMIENTO TIERRA (tile E) sigue con 4 items, todos de zanja: "EXCAVACION TRAZADO 1" 5,22 m3, "EXCAVACION TRAZADO 2" 34,91 m3, "RELLENO SELECCIONADO ARENA" 09,00, "RELLENO EXTRUCTURAL" 29,69 m3. NO hay item de excavacion de fundaciones. Planta sin poligono de excavacion de fundacion; "COTA 5,82/5,87 MTS" sin N.T.N. de plataforma por zona | NO LEVANTADO | 3 |
| OBS-02 | DWG-00-001-001 L1 | B->C | Rellenos sin especificacion (granulometria/% Proctor/material libre de sales); cuadro REFERENCIAS vacio | Cuadro REFERENCIAS (tile SW) vacio, identico a E5. NOTAS identicas a E5: solo 3 genericas. Sin ET-101, sin granulometria/% Proctor/material | NO LEVANTADO | 3 |
| NOTA-01 | DWG-00-001-001 L1 | B->C | Nomenclatura/TAGs/typos: camaras sin CD-06-00N; estanque/bomba/fosa/contenedores sin TAG; tuberia sin tag de linea; typo "relleno extructural"; recubrimiento minimo | tiles NW/W/SW: camaras siguen "CAMARA N°1, N°3, N°4, N°5, N°7 PROYECTADA" (sin CD-06); estanque/camaras sin TAG. Cubicaciones item 4: "RELLENO EXTRUCTURAL" (typo persiste). Tuberia sin tag de linea; sin recubrimiento minimo | NO LEVANTADO | 3 |
| OBS-03 | DWG-00-001-001 L2 | B->C | Rasante red de drenaje: sin pendiente longitudinal de proyecto ni cota invert de empalme | Secciones por estacion 0+001…0+019 (tile NW): cota de fondo bajo vs E5 (E5 EL.5,45->5,43; E7 EL.5,20->5,18) -> pendiente solo implicita en el escalonamiento; NO se declara pendiente longitudinal (%) ni cota invert de empalme | NO LEVANTADO | 3 |
| NOTA-01 | DWG-00-001-001 L2 | B->C | Nomenclatura/escala: camaras sin CD-06-00N; falta recubrimiento minimo sobre la clave; sin barra de escala grafica | tile SW/SE: DETALLE TIPO ZANJA (identico a E5, sin recubrimiento minimo sobre clave); "TUBERIA o6\" PROYECTADA" sin tag de linea; "ESCALA: 1:20" textual, sin barra de escala grafica; REFERENCIAS vacio | NO LEVANTADO | 3 |
| OBS-01 | DWG-00-002-006 L1 | C->D (L1 NO re-emitida) | Camaras seguian "CAMARA N1…N7 PROYECTADA" -> adoptar CD-06-001 a CD-06-00N | L1 (PLANTA GENERAL CANALIZACIONES, distinta de la planta de disposicion de L3) NO re-emitida en E7. La nomenclatura CD-06 aparece en L3 (tile W: "CAMARA CD-06-001…CD-06-004"; TABLA N°1: CD-06-001 a 006), pero L3 NO sustituye a L1 (alcances distintos) y L1 sigue con la nomenclatura antigua. Conflicto de conteo: L3 = 6 camaras vs DWG-001-001 L1 = hasta N°7 | PARCIAL (CD-06 adoptado en L3; L1 no re-emitida sigue con N1-N7; conflicto 6 vs 7 camaras) | 2 |
| NOTA-01 | DWG-00-002-006 L1/L2->L3 | C->D (L3 nueva) | Faltaba detalle tipico de camara prefabricada (anunciado L3, no entregado en E5); coexistian Rev B y C | L3 SI entregada: PLANTA CAMARA ESC 1:10 + SECCION A/B ESC 1:20: CUBIERTA/MARCO/MODULO 600 mm REDONDO, RADIER e=15, N.T.N/B.O.P segun TABLA N°1. Cajetin L3: "P22-DWG-00-002-006 LAM3", REV. D, "PLANO 3 de 3"; bloque revisiones A/B/C/D coherente, fecha 17/06/26 | LEVANTADO | 2 |
| OBS-01 | DWG-00-002-007 L1 | C->D | Mejoramiento de suelo + impermeabilizacion (notas faltantes); fecha cajetin 09/09/26 -> corregir a 09/06/26 | Notas mejoramiento/impermeabilizacion: AUSENTES. NOTAS PARTICULARES (tile SE) solo dos: (1) ref. generales -002-001; (2) "Disposicion y dimensiones de pernos de anclaje, pendientes hasta... planos vendor". Fecha: contradiccion interna — bloque REVISIONES fila C corregida a 09/06/26 y D 17/06/26; PERO casilla FECHA del cajetin principal sigue 09/09/26. N.T.N. +6,000 confirmado | PARCIAL (sin notas mejoramiento ni impermeabilizacion; fecha solo en bloque revisiones, no en cajetin principal) | 3 |
| OBS-01 | DWG-00-002-007 L3 | C->(L3 NO re-emitida) | Mejoramiento de suelo e impermeabilizacion; cuadro relleno 1,96 m3 sin especificacion | L3 de 002-007 NO re-emitida en E7 (E7 trae solo L1). El contenido no migro a otra lamina entregada | NO VERIFICABLE (lamina no re-emitida) | 3 |
| NOTA-01 | DWG-00-003-001 L1 | C->0 | Sigla en nota C5-M citaba "P22-IT" -> corregir a "P22-ET-00-010-103-0" | La nota C5-M (caso de carga montaje) vive en LAM2; en E7 solo se re-emitio LAM1 (PLANTA DISPOSICION DE PILARES + elevaciones + CUADRO MATERIALES con PANEL PV-6 25,2 m²). La sigla a corregir no esta en LAM1. LAM2 NO re-emitida. Cambio en LAM1 = NOTA 4 nueva "ESTE PLANO TRABAJA CON PLANO P22-DWG-00-002-007 LAM1/2/4" | NO VERIFICABLE (nota vive en LAM2, no re-emitida) | 3 |

### 2.E Recuento de estados (42 comentarios)

| Estado | Conteo |
|---|---|
| LEVANTADO | 17 |
| PARCIAL | 6 |
| NO LEVANTADO | 14 |
| NO VERIFICABLE | 2 |
| REGRESION (a nivel de codigo de documento) | 1 documento: DWG-003-001 (2->3). MC-002-001 se mantiene en Codigo 2 con condiciones duras a Rev 0 (calibracion usuario 18-Jun) |

Nota de conteo: la matriz lista 39 filas de comentario + 1 fila INFO (IT-001-0). El total de 42 comentarios emitidos incluye sub-laminas (DWG-001-001 lleva 5 entre L1/L2; DWG-002-002 lleva 4 entre L1/L2/L4).

---

## 3. Codigo por documento (propuesto)

| # | Documento | Rev E7 | Codigo TM N3 | Codigo E7 | Movimiento | Determinante |
|---|---|---|---|---|---|---|
| 1 | P22-MC-00-002-001 (Fund. Estanque TK-06-001) | 2 | 2 | **2** | SE MANTIENE (2->2) con condiciones duras a Rev 0 | **[Calibracion usuario 18-Jun: se mantiene en Codigo 2, no regresion.]** OBS-01 y OBS-02 quedan PARCIAL. Condiciones a incorporar en Rev 0 (sin nueva revision intermedia): (a) justificar el calculo de la armadura de losa (cuantia minima ACI 318 + flexion/corte con las solicitaciones del anclaje; preferir Phi16@200); (b) reconciliar el empotramiento memoria<->plano (E7 lo movio a 30 cm; el plano indica ~38 cm) y conciliar con DWG-00-002-005 cuando se re-emita. Senal de atencion: el ciclo movio el empotramiento alejandolo del plano en vez de acercarlo |
| 2 | P22-MC-00-002-002 (Fund. Dinamica Bomba BH-06-001) | 2 | 2 | **1** | SUBE (2->1) | NOTA-01 recubrimientos LEVANTADO; anclaje postinstalado correctamente no reabierto. Documento correcto en si (typo "ASTM F1553" cosmetico) |
| 3 | P22-MC-00-002-004 (Fund. Contenedor RO) | 2 | 2 | **2** | SE MANTIENE | NOTA-01 recubrimientos LEVANTADO, pero persiste "17.334 [tonf]" + falta declarar adopcion conservadora vs 14.934 kg: correccion menor que el propio documento incorpora a Rev 0 sin ciclo intermedio |
| 4 | P22-MC-00-002-005 (Fund. Sistema CIP) | 2 | 2 | **1** | SUBE (2->1) | NOTA-01 recubrimientos LEVANTADO; diferimiento anclajes CIP correctamente no reabierto (PEND-03 en seguimiento). Documento correcto en si |
| 5 | P22-MC-00-003-001 (Estructura Metalica + Fund. Cobertizo) | 2 | 2 | **1** | SUBE (2->1) | NOTA-01: recubrimientos LEVANTADO y combinacion de cargas ya explicita desde E5 y mantenida en E7. Sin defecto vivo |
| 6 | P22-ET-00-010-101-0 (Mov. de Tierra) | 1 | 2 | **1** | SUBE (2->1) | OBS-01 levantada: sigma_adm <= 1,0 kgf/cm2 declarada + "Municipalidad de Antofagasta" eliminada |
| 7 | P22-ET-00-010-102-0 (Obras Civiles) | 1 | 2 | **1** | SUBE (2->1) | NOTA-01 levantada: portada corregida a codigo ET. Recubrimientos/impermeabilizacion ya OK desde Rev 0 |
| 8 | P22-ET-00-010-103-0 (Estructura Metalica) | 1 | 2 | **1** | SUBE (2->1) | OBS-02 levantada en sus tres frentes: esquema C5-M por capas (>=355 um), perneria galvanizada/AISI 316, portada corregida |
| 9 | P22-IT-00-010-101-0 (Itemizado Mov. Tierra) | D | 3 | **2** | SUBE (3->2) | OBS-02 (tag fosa) y CHIMBA levantadas. Solo queda OBS-01 Clase 2 AACE, reclasificada MENOR (calibracion usuario 18-Jun): declaracion incorporable a Rev 0 sin ciclo intermedio |
| 10 | P22-IT-00-010-102-0 (Itemizado Obras Civiles) | D | 3 | **2** | SUBE (3->2) | OBS-02 (tag), OBS-03 (impermeabilizacion Sika Igol) y CHIMBA levantadas. Solo queda OBS-01 Clase 2 AACE, reclasificada MENOR: declaracion a Rev 0 |
| 11 | P22-IT-00-010-103-0 (Itemizado Estructura Metalica) | D | 3 | **2** | SUBE (3->2) | CHIMBA levantada y proteccion C5-M incorporada. Pendientes a Rev 0 (ambos incorporables sin ciclo): declarar Clase 2 AACE (MENOR) + agregar la partida de soldadura (hoy absorbida en "Conexiones 20%") |
| 12 | P22-DWG-00-001-001 (Excavacion / Canalizaciones, L1+L2) | C | 3 | **3** | SE MANTIENE | Punto RECTOR OBS-01 NO levantado: cubicaciones siguen con 4 items solo de zanja, sin excavaciones de fundaciones ni N.T.N. de plataforma; OBS-02, OBS-03 y NOTA-01 x2 sin levantar. El cambio B->C toco volumenes/cotas de zanja pero no abordo ningun comentario |
| 13 | P22-DWG-00-002-001 (Implantacion / Disposicion OOCC) | D | 2 | **1** | SUBE (2->1) | OBS-01 y NOTA-01 levantados con cambio de contenido real: N.T.N. por zona acotado, tag a TK-06-004, sigla C5-M IT->ET. Documento correcto en si |
| 14 | P22-DWG-00-002-002 (Fund. TK / Anclaje / Bomba, L1/L2/L4) | D | 3 | **3** | SE MANTIENE | OBS-01 (mejoramiento de suelo) MAYOR abierto en LAM1 y LAM4 (notas byte-identicas a E5). LAM2 sin cambio de contenido (vendor EX-2600 no corregido a EX-26005) |
| 15 | P22-DWG-00-002-003 (Fund. Contenedor, L1) | D | 3 | **3** | SE MANTIENE | OBS-01 MAYOR abierto: sin nota de mejoramiento y relleno 30,03 m3 sin material/espesor/% compactacion. Contenido identico a E5 |
| 16 | P22-DWG-00-002-004 (Fosa de Drenaje, L1/L2) | D | 3 | **3** | SE MANTIENE | OBS-01 PARCIAL (M.H.A. sin definir; impermeabilizacion si agregada) + OBS-02 NO LEVANTADO (rebalse ausente; detalle parrilla aun "ARS-5") + NOTA-01 tag PARCIAL (L2=TK-006-004 no unificado) |
| 17 | P22-DWG-00-002-006 (Camaras CD-06-00N, solo L3) | D | 3 | **2** | SUBE (3->2) | NOTA-01 (detalle tipico de camara) LEVANTADO en L3. OBS-01 (nomenclatura) PARCIAL: CD-06 en L3, pero L1/L2 NO re-emitidas siguen con N1-N7 + conflicto de conteo 6 vs 7. El cierre a Cod 1 exige re-emitir L1/L2 |
| 18 | P22-DWG-00-002-007 (Fundacion CIP, solo L1) | D | 3 | **3** | SE MANTIENE | OBS-01 sin levantar: notas de mejoramiento e impermeabilizacion AUSENTES; fecha corregida solo en bloque de revisiones (09/06/26) pero NO en casilla FECHA del cajetin (sigue 09/09/26). L3 (misma OBS-01 + relleno 1,96 m3) no re-emitida |
| 19 | P22-DWG-00-003-001 (Cubierta / Estructura Cobertizo, solo L1) | 0 (cajetin) / D (carta) | 2 | **3** | **BAJA (REGRESION 2->3)** | NOTA-01 (sigla C5-M) vive en LAM2, NO re-emitida -> no verificable/no levantada. Se emitio Rev 0 ("Para Uso e Informacion") de solo LAM1 + discrepancia carta (Rev D) vs cajetin (Rev 0) + fecha cajetin 09/06/26 vs fila Rev 0 17/06/26 |
| — | P22-IT-00-010-001-0 (Estimacion de Inversion) | NUEVO 0 | — | **sin codigo (insumo)** | — | No es entregable del paquete de licitacion. Arrastra fosa TK-06-002 (B28/B54), ausencia Clase 2 AACE, partidas faltantes y Panel PV-6 118 m2 vs 25,2 m2. Observacion informativa |

### 3.1 Lectura de la transicion vs lo esperado

- **De los 9 documentos en Codigo 2 del TM N3** (5 MC + 3 ET + DWG-003-001): 6 suben a Codigo 1 (MC-002-002, MC-002-005, MC-003-001, ET-101, ET-102, ET-103); 2 se mantienen en Codigo 2 (MC-002-004 correccion menor; MC-002-001 con condiciones duras a Rev 0 — calibracion usuario 18-Jun); **1 BAJA a Codigo 3 por REGRESION: DWG-003-001.** Ademas DWG-002-001 sube a Codigo 1.
- **Total Codigo 1 = 7 documentos** (los 6 anteriores + DWG-002-001).
- **De los Codigo 3:** los 3 IT SUBEN a Codigo 2 (calibracion usuario 18-Jun: la unica observacion restante, Clase 2 AACE, es MENOR e incorporable a Rev 0; el resto — tag, La Chimba, impermeabilizacion, C5-M — ya levantado). De los planos Codigo 3: DWG-002-006 sube a Codigo 2; DWG-001-001, -002-002, -002-003, -002-004 y -002-007 se mantienen en Codigo 3.
- **El Codigo 3 global queda anclado SOLO en los planos de obra civil** (no en los itemizados): es la senal limpia de no-convergencia del ciclo.

---

## 4. Veredicto global propuesto

**Veredicto: Codigo 3 — Por revisar.** Se fija por el documento mas severo de cada disciplina y por la concentracion de comentarios MAYOR no levantados en los planos de fundacion y movimiento de tierra. Determinantes:

1. **Punto RECTOR sin levantar (DWG-00-001-001):** el plano de excavaciones sigue cubicando solo zanjas de drenaje (4 items), sin excavaciones de fundaciones ni niveles de plataforma por zona. Sin este plano, las cubicaciones de los itemizados (IT-101/102/103) no tienen sustento de excavacion de fundaciones — es la observacion que el correo del ciclo anterior declaro rectora.
2. **Mejoramiento de suelo ausente en los planos de fundacion** (DWG-002-002 L1/L4, DWG-002-003 L1): notas particulares byte-identicas a E5; el avance de revision C->D no incorporo la nota exigida por ET-101.
3. **N.T.N. por zona:** levantado donde se reviso (DWG-002-001), pero ausente en el plano rector DWG-001-001.
4. **Faltantes y regresion:** MC-002-003 y DWG-002-005 ausentes por 3a vez; DWG-003-001 BAJA de Codigo 2 a Codigo 3 (regresion). MC-002-001 se mantiene en Codigo 2 con condiciones duras a Rev 0 (calibracion usuario), pero con la senal de que el empotramiento se movio alejandose del plano.

Nota de calibracion (18-Jun): la Clase 2 AACE NO es determinante del veredicto — reclasificada MENOR (declaracion incorporable a Rev 0); los 3 itemizados suben a Codigo 2. El veredicto global Codigo 3 queda anclado **exclusivamente en los planos de obra civil** (fundaciones + movimiento de tierra). El ciclo muestra avance neto en memorias de calculo, especificaciones tecnicas e itemizados, pero los planos de fundacion / movimiento de tierra no movieron sus puntos de fondo (notas byte-identicas a E5) y aparecio una regresion (DWG-003-001). El veredicto global no puede ser superior a Codigo 3.

---

## 5. Logros del ciclo (resumen ejecutivo)

E7 cerro materialmente lo siguiente:

- **Recubrimientos 50/70 en las cinco memorias de calculo:** todas declaran ahora 50 mm para elementos expuestos y 70 mm en contacto con el terreno (ambiente marino), conforme TdR 3.3.4. Cierra el punto transversal de recubrimientos del stream.
- **Trazabilidad de la reaccion basal Ez (MC-002-001):** la reaccion Ez=+-3.357 kgf cita ahora P22-IT-06-000-005-0, no la memoria del fabricante AFTA.
- **Las tres Especificaciones Tecnicas (ET-101/102/103) suben a Codigo 1:** sigma_adm <= 1,0 kgf/cm2 declarada y referencia municipal eliminada (ET-101); portadas corregidas de codigo IT a codigo ET (ET-102 y ET-103); esquema C5-M por capas trasladado a la ET con perneria galvanizada/AISI 316 (ET-103).
- **Higiene de los itemizados:** la pestana ajena "La Chimba" eliminada de los tres IT; tag de fosa corregido a TK-06-004 en IT-101 e IT-102; partida de impermeabilizacion Sika Igol incorporada al IT-102 (12 celdas); proteccion C5-M incorporada al IT-103.
- **Plano de implantacion DWG-002-001 a Codigo 1:** N.T.N. acotado por zona, tag de fosa a TK-06-004 y sigla C5-M corregida de IT a ET.
- **Detalle tipico de camara prefabricada (DWG-002-006 L3, nueva):** se entrego la lamina anunciada y no entregada en E5; el plano sube de Codigo 3 a Codigo 2.

Direccion del ciclo: las disciplinas de calculo y especificacion avanzaron de forma clara; los planos de obra civil de fundacion y el plano rector de movimiento de tierra, no.

---

## 6. Decision pendiente de calibracion (la toma el usuario)

### 6.a Propuesta de codigos para calibrar

- **Codigo 1 (7 documentos):** MC-002-002, MC-002-005, MC-003-001, ET-101, ET-102, ET-103, DWG-002-001.
- **Codigo 2 (6 documentos):** MC-002-001 (condiciones duras a Rev 0: justificar armadura + reconciliar empotramiento memoria-plano — calibracion usuario 18-Jun), MC-002-004 (correccion menor de notacion/peso a Rev 0), IT-101 (declarar Clase 2 AACE a Rev 0), IT-102 (declarar Clase 2 AACE a Rev 0), IT-103 (declarar Clase 2 AACE + agregar partida de soldadura a Rev 0), DWG-002-006 (re-emitir L1/L2 alineadas a CD-06 + reconciliar 6 vs 7 camaras).
- **Codigo 3 (6 documentos):** DWG-001-001 (rector), DWG-002-002, DWG-002-003, DWG-002-004, DWG-002-007 + 1 por REGRESION: DWG-003-001 (2->3). **Todos planos de obra civil** — la no-convergencia del ciclo esta concentrada aqui.
- **Sin codigo (insumo):** IT-001-0 (Estimacion de Inversion).
- **No recibidos / no verificables:** MC-002-003 y DWG-002-005 (no entregados, 3a vez); DWG-002-006 L1/L2, DWG-002-007 L3 y DWG-003-001 L2 (no re-emitidas, cargan comentarios abiertos).

Calibracion del usuario (18-Jun): MC-002-001 se mantiene en **Codigo 2 con condiciones duras a Rev 0** (no regresion): justificar el calculo de la armadura de losa y reconciliar el empotramiento memoria-plano. Queda registrada la senal de atencion: E7 no aporto la justificacion pedida en el TM N3 y movio el empotramiento (40->30 cm) alejandolo del plano (38 cm). **Unica regresion del ciclo: DWG-003-001 (2->3)** — su pendiente (sigla C5-M) vive en LAM2 no re-emitida y se emitio una Rev 0 de solo LAM1 con discrepancia carta (Rev D) vs cajetin (Rev 0).

### 6.b Datos para la postura sobre el limite de ciclo del TdR (sin decision)

**Persistencia por punto Codigo 3 (ciclos consecutivos sin levantar):**

| Punto Codigo 3 | Documento | TM N2 (E4) | TM N3 (E5) | E7 | Ciclos consecutivos |
|---|---|---|---|---|---|
| ~~Clase 2 AACE no declarada~~ (reclasificada MENOR 18-Jun; NO es driver de la escalacion) | IT-101 / IT-102 / IT-103 | Codigo 3 | Codigo 3 (no levantada) | Codigo 2 (declaracion a Rev 0) | — (fuera del argumento de ciclo) |
| Mejoramiento de suelo ausente | DWG-002-002 / -003 | Codigo 3 | Codigo 3 (no levantada) | Codigo 3 (no levantada) | hasta 3 |
| Excavacion de fundaciones (rector) | DWG-001-001 | abierto (B) | Codigo 3 (B->C, no levantada) | Codigo 3 (no levantada) | 2-3 |
| Rebalse / parrilla FRP | DWG-002-004 L2 | abierto | Codigo 3 (no levantada) | Codigo 3 (no levantada) | 2-3 |
| Mejoramiento + impermeabilizacion CIP | DWG-002-007 | abierto | Codigo 3 (no levantada) | Codigo 3 (L1 parcial, L3 no re-emitida) | 2-3 |

> Nota de verificacion: el conteo exacto de ciclos debe cruzarse contra el TM N2 (P22-TM-00-010-002-0, ENTREGA 4) al redactar el TM N4. Lo confirmado aqui es la persistencia TM N3 -> E7. Varios planos e itemizados ya venian observados desde TM N2, por lo que para esos puntos el numero real seria 3 ciclos.

**Reincidencia de fallas de entrega:**

| Falla de entrega | TM N2 | TM N3 | E7 | Reincidencia |
|---|---|---|---|---|
| P22-MC-00-002-003 (Sistema de Drenajes) faltante | faltante | faltante | faltante | **3a vez consecutiva** |
| P22-DWG-00-002-005 (Detalles Anclaje y Conexiones) faltante | faltante | faltante | faltante | **3a vez consecutiva** |
| Laminas re-emitidas parciales (comentario abierto en lamina no re-emitida) | — | observado | DWG-002-006 (L1/L2), -002-007 (L3), -003-001 (L2) | reincide |
| Avance de revision sin cambio de contenido (C->D byte-identico) | — | — | DWG-002-002 L1/L4/L2, -002-003 L1, -002-004 L2 | nuevo patron en E7 |
| Discrepancia carta <-> archivo (Rev D carta vs Rev 0 archivo) | — | — | DWG-003-001 | nuevo en E7 |
| Tag TK-06-002 persistente a nivel de carta / Estimacion de Inversion | — | observado | carta TT-008 (titulos DWG-002-004) + IT-001-0 BASE B28/B54 | reincide |

**Decision del usuario (18-Jun): el correo de remision del TM N4 INVOCA el limite de ciclo del TdR.** Anclaje de la escalacion (NO la Clase 2 AACE, reclasificada menor):
1. **No-convergencia del mejoramiento de suelo** en los planos de fundacion (DWG-002-002 L1/L4, -002-003 L1): planteado desde el TM N2, no levantado en E5 ni en E7, con notas particulares byte-identicas a E5 pese al avance de revision C->D. Requisito: ET-101.
2. **Plano rector de excavacion de fundaciones (DWG-001-001)** sin incorporar las excavaciones de fundaciones por 2o ciclo: las cubicaciones de los itemizados siguen sin sustento.
3. **Patron de no-diligencia:** avance de la letra de revision sin cambio de contenido (varios planos C->D byte-identicos); 3a falta de entrega consecutiva de MC-002-003 y DWG-002-005; re-emision parcial de laminas que deja comentarios colgados.

La Clase 2 AACE queda fuera del argumento de ciclo (menor, declaracion a Rev 0). El correo se redacta firme y contractual (no acusatorio), con los codigos ADASA explicitos, y exige la convergencia a Rev 0 dentro del ciclo del TdR. Verificar el dia de la semana de cualquier deadline contra calendario antes de emitir.
