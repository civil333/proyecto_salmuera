# ANALISIS DE TRABAJO — P22-TM-00-010-003-0 (Revision Tecnica N3, ENTREGA 5)

> Documento interno ADASA — NO SE ENVIA. Matriz de levantamiento de los puntos del TM N2
> contra la ENTREGA 5 de L&A (carta 067-032-032-COR-TT-006, 09-Jun-2026) + primera revision
> de los documentos nuevos. Estado 10-Jun-2026: **MATRIZ COMPLETA** (agentes A/B/C1/C2/C3 +
> verificacion adversarial + verificaciones puntuales en PDF). **PENDIENTE: calibracion del
> usuario sobre la propuesta de codigos (Seccion 5)** antes de redactar el TM N3.
> Fuentes: ENTREGA 5/md/ (texto + diffs Rev N→N+1) y ENTREGA 5/Planos/*_drawing/ (cajetines,
> texto rotado y PNG 300/600 dpi por lamina, via large-pdf-reader modo drawing).

## 1. Inventario de la ENTREGA 5 — verificacion carta vs archivos (CERRADO 10-Jun)

Carta 067-032-032-COR-TT-006 (09-Jun-2026, P. Castillo → L. Rivera): 31 items declarados
(22 "Revision Cliente" + 9 "Para Uso e Informacion"; 0 "Para Construccion").

| Grupo | Declarado en carta | Archivo fisico | Estado |
|-------|--------------------|----------------|--------|
| IT-101 / IT-102 / IT-103 | Rev C, Revision Cliente | `_C.xlsx` + `_C.pdf` | OK |
| ET-101 / ET-102 / ET-103 | Rev 0, Para Uso e Informacion | `_0.doc` + `_0.pdf` | OK (cajetin declara "Aprobado Cliente 08-06-2026" — ADASA no ha aprobado: punto administrativo) |
| MC-001 / -002 / -004 / -005 | Rev 1, Para Uso e Informacion | `_1.docx` + `_1.pdf` | OK |
| MC-002-003 Sistema de Drenajes | **Rev 0 declarada (item 9)** | **AUSENTE** | **FALLA DE ENTREGA** — en su lugar vino la Rev 0 antigua (28-May, Entrega 4) de MC-003-001 Cubierta (verificado por caratula de ambos PDF). Solicitar el archivo |
| MC-003-001 Cubierta | Rev 1 (item 12) | `_1.docx/pdf` + `_0.docx/pdf` extra no declarado | Rev 1 vigente (04-Jun); el `_0` es la rev antigua incluida por error |
| DWG-00-001-001 (NUEVO) | Rev B, L1+L2 | 2 PDF | OK — primera revision ADASA |
| DWG-00-002-001 | Rev C, L1 | 1 PDF | OK |
| DWG-00-002-002 | Rev C, L1-L4 | 4 PDF | OK |
| DWG-00-002-003 | Rev C, L1-L3 | 3 PDF | OK |
| DWG-00-002-004 | Rev C, L1-L2 | 2 PDF | OK (titulo de carta sigue "Fosa de drenajes TK-06-002" — tag a verificar en lamina) |
| DWG-00-002-006 | Rev C, L1-L2 | 2 PDF | OK |
| DWG-00-002-007 | **C L1, B L2, C L3** | 3 PDF (L2 en Rev B) | Mezcla declarada por la propia carta (item 28): LAM2 quedo en Rev B 28-May — verificar si LAM2 tenia comentarios TM N2 sin levantar |
| DWG-00-003-001 | Rev C, L1-L2 | 2 PDF | OK |
| **DWG-00-002-005 Detalles de Anclaje** | **NI DECLARADO NI INCLUIDO** | — | **Sigue faltante** (comprometido en Listado 067-032-032-COR-LI-001; exigido en TM N2) |

## 2. Matriz de levantamiento — puntos TM N2 (POR COMPLETAR con agentes A/B/C)

Leyenda de veredicto: LEVANTADO / PARCIAL / NO LEVANTADO / REGRESION.

### 2.1 Memorias de Calculo (Agente A)

| ID TM N2 | Documento | Exigencia | Veredicto | Evidencia |
|----------|-----------|-----------|-----------|-----------|
| OBS-01 | MC-001 (era Cod 3) | Anclaje preinstalado colado ASTM F1554 + ACI 318-19 Cap.17/Sec.17.10, reconciliar Exfibro EX-26005-F01 Rev C | **PARCIAL (rebajado por verificacion adversarial)** | La Rev 1 cambia la intencion (declara "pernos de anclaje preinstalado de 1''... empotramiento de 40 cm", elimina el adhesivo HIT-RE 500, FU 68%→34%) **pero la especificacion es contradictoria e incompleta**: (a) mantiene la varilla **HAS-V-36** (producto de anclaje quimico postinstalado) rotulada "ASTM F1554" como preinstalado; (b) **no define el extremo embebido** (cabeza/tuerca+placa) que califica un preinstalado por ACI 318-19 Cap.17; (c) no cita Cap.17/Sec.17.10 en la seccion del anclaje ni muestra los modos de falla de preinstalado (breakout con hef=40 cm, pullout de cabeza); (d) **sin reconciliacion con el patron de pernos Exfibro EX-26005-F01 Rev C**; (e) el salto de FU 68→34% no se explica |
| NOTA-03 | MC-001 | Citar P22-IT-06-000-005-0 como fuente de reacciones (Ez ±3.357 kgf) | **PARCIAL** | Adopta Ez = 3.357 kgf pero cita "Memoria Estanque AFTA Taltal", no el codigo P22-IT-06-000-005-0 (la exigencia era la cita del codigo vinculante) |
| NOTA-10 | MC-001 | Typos F1554/HIT-RE 500; justificar armadura Ø16@100; recubrimientos 50/70 | **PARCIAL** | F1554 corregido; HIT-RE no aplica (adhesivo eliminado); recubrimientos NO declarados; armadura ahora Ø12@200 — **CALIBRACION USUARIO (10-Jun):** el espaciamiento @200 es aceptable si cumple cuantia minima de ACI 318 (no ACI 350: la losa es fundacion de estanque PRFV apoyado, NO contencion de liquido); preferir **Ø16@200**; la accion es *justificar el calculo*, no rechazar |
| NOTA-02 | MC-002 (era Cod 2) | Recubrimientos 50/70 | **PARCIAL** | Nueva tabla "Recubrimiento": declara solo "Contacto con terreno 70"; falta 50 mm expuesto |
| NOTA-04 | MC-004 (era Cod 2) | Notacion/fuente del peso 17,3 t (conservador vs 14.934 kg vinculante) | **PARCIAL** | Agrega cita "en el punto 2.1.2" pero mantiene "17.334 [tonf]" (notacion erronea persiste) y no declara la adopcion conservadora |
| OBS-02 | MC-004 | Unificar ACI 318-19; recubrimientos 50/70 | **PARCIAL** | ACI 318-19 unificado (pedestales corregidos); recubrimientos NO declarados |
| NOTA-01 | MC-005 (era Cod 2) | Recubrimientos 50/70 | **PARCIAL** | Tabla 2-3 "Recubrimiento adoptado": solo "Contacto con terreno 70"; falta 50 mm expuesto |
| NOTA-02 | MC-005 (= PEND-03) | Anclajes CIP diferidos — estado del diferimiento (seguimiento, no rechazo) | **LEVANTADO (sigue diferido, conforme)** | Rev 1 declara el compromiso con normas: "queda pendiente de diseño los anclajes postinstalados (ACI 318-19 Cap.17/Sec.17.10, precalificados ACI 355.2/355.4) cuando lleguen los datos del proveedor" — coherente con PEND-03 |
| OBS-02 | MC-003-001 (era Cod 3) | Declarar C5-M (ISO 12944) o referir a ET-103 | **LEVANTADO** | Tabla completa: "C5-M (costa marina)... SSPC-SP10/Sa 2½... Zinc 80 µm + epoxico 200 µm + poliuretano 75 µm, total >=355 µm, RAL 5012"; sin referencia cruzada a ET-103 (menor) |
| OBS-05 | MC-003-001 | Anexos en rev vigente; coef. sismico vertical 0,74 vs 0,67; factor 1,4E; recubrimientos | **PARCIAL** | Coef. vertical unificado a 0,74 (texto y Tabla 2-4 coherentes); combinacion declarada "1,2D±E" (antes 1,2D+1,4E+L — declarada, evaluar suficiencia); **anexos ahora INTEGRADOS al documento Rev 1** (Anexo A pag. 45, Anexo B pag. 50, sin cajetin Rev B independiente — verificado en PDF 10-Jun: cerrado); recubrimientos NO declarados |

### 2.2 Especificaciones Tecnicas Rev 0 e Itemizados Rev C (Agente B)

| ID TM N2 | Documento | Exigencia | Veredicto | Evidencia |
|----------|-----------|-----------|-----------|-----------|
| OBS-07 | ET-101 (era Cod 2) | Mejoramiento/reemplazo de suelo como condicion de diseño (material, espesor, compactacion) | **LEVANTADO** | Eliminadas las remisiones al "Informe de Mecanica de Suelos" inexistente; condiciones declaradas ("suelo libre de sales, cloruros y sulfatos"; base granular especificada) — pagina 10 |
| NOTA-11 | ET-101 | Taltal; sigma_adm <= 1,0 kg/cm2 del TdR; codigo portada ET | **PARCIAL** | "Las obras se emplazaran en la ciudad Taltal (ambiente marino)" OK; codigo portada ET-00-010-101 OK; **falta declarar sigma_adm <= 1,0 kg/cm2** (solo remite a validacion del especialista); residuo "Municipalidad de Antofagasta" (menor) |
| OBS-07 | ET-102 (era Cod 2) | Recubrimientos 50 y 70 mm (ambos, TdR Seccion 3.3.4) + impermeabilizacion enterrados | **LEVANTADO** | "recubrimiento de 50mm expuesto y 70mm en contacto con el terreno" (pag. 8) + "1 mano de Sika Igol Primer y 2 manos de Sika Igol denso... laminas de polietileno de 0.4mm" (pag. 8) |
| NOTA-11 | ET-102 | Taltal; codigo portada ET | **PARCIAL** | Taltal OK; **portada sigue "P22-IT-00-010-102-0"** (codigo IT; el cajetin si dice ET) |
| OBS-08 | ET-103 (era Cod 2) | C5-M por capas (SSPC-SP10/Sa 2½ + zinc 80 + epoxico 200 + PU 75 µm); AWS D1.1; perneria galvanizada/inox | **PARCIAL** | C5-M ISO 12944-2/-5 + "espesor total minimo 355 µm" declarados pero **sin desglose por capas ni preparacion de superficie**; AWS D1.1 LEVANTADO (sustituyo A5.1/A5.17); **perneria NO LEVANTADO** (mantiene HILTI HIT RE-500 V3 + A325 sin exigir galvanizado/inox para C5-M) |
| NOTA-11 | ET-103 | Taltal; codigo portada ET | **PARCIAL** | Taltal OK; **portada sigue "P22-IT-00-010-103-0"** (cajetin si dice ET) |
| — | IT-101/-102/-103 (eran Cod 3) | Declarar Clase 2 AACE (Minuta MI-001 item 1.2) | **NO LEVANTADO (los 3)** | Solo "PRESUPUESTO REFERENCIAL REV. C"; ninguna mencion a Clase 2 AACE en ningun IT |
| OBS-02 | IT-102 | Tag fosa TK-06-004 (no TK-06-002) | **NO LEVANTADO** | IT-101 e IT-102 mantienen "Fosa TK-06-002"; TK-06-004 no aparece en ningun IT |
| — | IT-102 | Partidas de impermeabilizacion | **NO LEVANTADO** | Sin item de impermeabilizacion (Sika Igol) pese a que la ET-102 Rev 0 ya la especifica — descalce ET vs IT |
| — | IT-103 | Partidas de proteccion superficial C5-M y soldadura | **NO LEVANTADO** | Sin items de preparacion de superficie/pintura por capas ni soldadura AWS D1.1 |
| — | IT (los 3) | Eliminar hojas/pestañas ajenas del Excel | **NO LEVANTADO (los 3)** | Hoja "BOM" = "CUADRO DE PIEZAS ESPECIALES INTERCONEXION LA CHIMBA" (otro proyecto) persiste en IT-101, IT-102 e IT-103 |

### 2.3 Planos Rev C + DWG-00-001-001 Rev B nuevo (Agente C)

| ID TM N2 | Plano / Lamina | Exigencia | Veredicto | Evidencia |
|----------|----------------|-----------|-----------|-----------|
| NOTA-01 | -002-001 L1 (era Cod 3) | Coordenadas adicionales para azimut absoluto del estanque | **LEVANTADO** | Nuevo "CUADRO DE COORDENADAS UTM" con 13 vertices V01-V13 (N/E) plotteados sobre las estructuras — azimut absoluto queda fijado |
| OBS-01 | -002-001 L1 | Acotar N.T.N. por zona coincidente con montaje -101/-103/-105 y Levantamiento DIO | **NO LEVANTADO** | Cero ocurrencias de N.T.N./NPT/+5,75/+6,00 en la lamina; las llamadas solo remiten a los planos de fundacion. (Los planos de fundacion si declaran ahora los N.T.N. absolutos — pero la implantacion sigue sin acotarlos por zona) |
| OBS-01 | -002-002 L1 | Nota de mejoramiento de suelo conforme ET-101 | **NO LEVANTADO** | Notas particulares solo remiten a notas generales (-002-001 Rev C, notas 1-15: ninguna de mejoramiento) y al plano vendor; cuadro de excavacion con RELLENO "—". Positivo no pedido: cotas ahora absolutas EL.+5,950 N.T.C. / +5,750 N.T.N. / +5,350 N.S.F. |
| OBS-01 | -002-002 L2 | Anclaje estanque preinstalado colado (ASTM F1554, ACI 318-19) reconciliado con Exfibro | **LEVANTADO (en el plano)** | Tabla "DIMENSIONES DE PERNOS PREINSTALADOS": PA-2 Ø1'' x8, A=220/B=300/L=600/placa F=18; "BARRA ASTM F1554 Gr.36 / TUERCAS HEX. ASTM A563 / GOLILLAS F436"; detalle con placa+tuerca embebida y silla de anclaje; **cero menciones a HAS-V-36 o HIT-RE 500**; nota "VER PLANO VENDOR EX-2600-F01_Rev.C". **Pendiente conciliar MC↔plano**: la MC Rev 1 mantiene "HAS-V-36" y empotramiento 40 cm vs ~38 cm del plano (L600-A220) |
| OBS-01 | -002-002 L4 | Nota de mejoramiento de suelo | **NO LEVANTADO** | Notas solo remiten a generales + vendor KSB; relleno sin especificar |
| OBS-02 | -002-002 L4 | Anclaje bomba: evaluar preinstalado o justificar postinstalado segun categoria sismica | **CERRADA POR CALIBRACION (10-Jun) — se retira** | El usuario acepta el anclaje **postinstalado** de la bomba conforme a los planos KSB. Ya no es observacion; no se anota en el CC_ADASA. (El plano -002-002 sigue Codigo 3 por el mejoramiento de suelo de L1/L4, no por este punto) |
| OBS-01 | -002-003 L1 | Cotas en N.T.N. absoluto coincidente con montaje -103 (no datum relativo) | **LEVANTADO** | Elevaciones declaran EL.+6,050 N.T.C. / EL.+6,000 N.T.N. / EL.+5,150 N.S.F. — zona ~+6,00 coherente con montaje -103; datum relativo eliminado |
| OBS-02 | -002-003 L1 | Callout al detalle INS-1 (LAM2) | **PARCIAL** | Callout existe ("INSERTO INS-1 VER PLANO P22-DWG-00-002-003 (LAM2)") **pero el archivo LAM2 entregado es un duplicado de LAM1** — el detalle INS-1 no esta en la entrega (ver anomalias) |
| NOTA-01 | -002-003 L1 | Nota de mejoramiento de suelo | **NO LEVANTADO** | Unica nota: remision a notas generales; cuadro cuantifica RELLENO 30,03 m3 pero sin material/espesor/% compactacion |
| OBS-01 | -002-004 L1 | Mejoramiento de suelo + impermeabilizacion exterior enterrada | **PARCIAL** | Impermeabilizacion exterior cubierta por via indirecta (nota general 10 de -002-001 Rev C: "1 MANO SIKA IGOL PRIMER, 2 MANOS SIKA IGOL DENSO" en paredes bajo terreno; Sikatop interior se mantiene). Mejoramiento: aparece capa grafica **"M.H.A. e=15"** bajo el sello + emplantillado e=5, pero la sigla no esta definida en notas ni leyenda de ninguna lamina (grep MEJORAMIENTO = 0) |
| NOTA-01 | -002-004 L1 | Tag fosa TK-06-004 | **PARCIAL (regresion en L2)** | Cajetin L1: "FOSA DE DRENAJE TK-06-004 - FORMAS" OK. **Pero cajetin L2 dice "TK-006-002"** (tag viejo y mal formateado) y la llamada de la implantacion -002-001 sigue "FOSA DE DRENAJE TK-06-002" |
| OBS-01 | -002-004 L2 | Parrilla PRFV pultruida transito liviano | **PARCIAL** | "PARRILLA DE PISO FRP 1,87 m2" en cuadro de materiales + planta de disposicion + detalle de apoyo; pero el detalle conserva la designacion "PARRILLA PISO ARS-5" (acero, residuo) y no declara "pultruida" ni condicion de transito liviano |
| OBS-02 | -002-004 L2 | Aperturas de rebalse indicadas y acotadas | **NO LEVANTADO** | Cero ocurrencias de "REBALSE" en toda la entrega; solo una pasada Ø24 "SOLO EN EJE B" (compatible con la entrada DN200, no con el rebalse) |
| OBS-01 | -002-006 L1 | Nomenclatura camaras CD-06-00N | **NO LEVANTADO** | Todas las camaras siguen "CAMARA N°1...N°7 PROYECTADA" (grep CD-06 = 0 en toda la entrega); se agregaron coordenadas N/E por camara (mejora no pedida) |
| NOTA-01 | -002-006 L1 | Lamina detalle tipico camara prefabricada; pendientes longitudinales acotadas | **PARCIAL** | Pendientes LEVANTADAS: LAM2 "PERFIL TRAZADO N°1" (i=1,37%) y "PERFIL TRAZADO N°2" (-0,12/-0,10/-0,07/-0,10/-0,06%) con banda de pendientes y B.O.P. por estacion. **Detalle tipico de camara AUSENTE** — el cajetin dice "PLANO 1 de 3"/"2 de 3" y la LAM3 no vino en la entrega |
| OBS-01 | -002-007 L1 | Mejoramiento de suelo + impermeabilizacion | **NO LEVANTADO** | Notas particulares: solo remision a generales + nota 2 nueva "DISPOSICION Y DIMENSIONES DE PERNOS DE ANCLAJE, PENDIENTES HASTA LA ENTREGA DE LOS PLANOS VENDOR" (hold consistente con PEND-03, ahora declarado en plano). Sin nota de mejoramiento ni impermeabilizacion especifica |
| OBS-02 | -002-007 L1 | NPT +5,610 reconciliado con montaje -103 (zona ~+6,00) | **LEVANTADO** | Secciones A y B declaran EL.+6,200 N.T.C. / EL.+6,000 N.T.N. / EL.+5,500 N.S.F. — el +5,610 desaparecio; coherente con contenedor RO (+6,050 N.T.C. / +6,000 N.T.N.) |
| OBS-01 | -002-007 L3 | Mejoramiento de suelo + impermeabilizacion | **NO LEVANTADO** | Unica nota: remision a generales. Cuadro de excavacion cuantifica RELLENO 1,96 m3 sin especificacion. (El perno PA-1 del cobertizo si es preinstalado: barra A36 3/4'' x24 con placa embebida — correcto, pero colisiona con la marca PA-1 postinstalada de -002-002 L4) |
| OBS-01 | -003-001 L1 (era Cod 2) | Nota C5-M referida a ET-103 | **PARCIAL** | La lamina solo remite a notas generales; la declaracion C5-M vive en -002-001 nota 6 ("ISO 12944-2: C5-M... RAL 5012... SEGUN ESPECIFICACION TECNICA **P22-IT**-00-010-103-0" — typo de sigla IT por ET). Cumplimiento indirecto, sin esquema de espesores en lamina |
| — | -002-007 L2 (quedo Rev B) | ¿Era exigible re-emision? | **DEFENDIBLE** | LAM2 = armaduras; no contiene cotas de elevacion ni notas de suelo (los comentarios del TM N2 viven en las laminas de formas L1/L3); el cambio +5,610→+6,200 fue de datum, no de geometria. Aceptable porque la carta lo declara explicitamente |
| NUEVO | -001-001 L1+L2 Rev B | Primera revision: coherencia ET-101, niveles vs DIO y montaje | **REVISADO — 4 OBS Mayores + 5 NOTAS candidatas (ver 2.3.1)** | El plano solo contiene las **zanjas de drenaje** (2 trazados, 7 camaras, descarga a camara existente); no cubre excavaciones de fundaciones, plataformas ni NPT por zona pese al titulo/compromiso |

#### 2.3.1 DWG-00-001-001 Rev B (NUEVO) — hallazgos de primera revision (Agente C3)

| ID candidato | Severidad | Hallazgo | Corregir |
|--------------|-----------|----------|----------|
| OBS-01 | Mayor | **Alcance incompleto vs compromiso**: solo zanjas de drenaje; faltan excavaciones/mejoramiento de fundaciones (TK-06-001, BH-06-001, TK-06-004, contenedor RO, CIP), niveles de plataforma y NPT por zona (+5,75 / ~+6,00) | Incorporar movimiento de tierras general o declarar alcance parcial + referenciar planos de fundacion; declarar NPT por zona (montaje P22-DWG-06-005-103) |
| OBS-02 | Mayor | Rellenos sin especificacion: "ARENA LIMPIA COMPACTADA" y "RELLENO EXTRUCTURAL" (typo) sin granulometria, % Proctor ni material libre de sales/cloruros/sulfatos; cuadro REFERENCIAS **vacio** en ambas laminas | Referenciar P22-ET-00-010-101 Rev 0; declarar % compactacion y calidad de material |
| OBS-03 → NOTA | Menor (rebajada por cruce con IT-101) | Las cubicaciones del plano (2,82+20,64 exc / 9,00+13,02 rell, zanjas) y las de la ET-101 (4,22/5,06/5,01, fundaciones) son de **alcances distintos** y el IT-101 Rev C integra AMBOS sets correctamente (items 2-6 zanjas + items 7+ fundaciones, verificado 10-Jun). Defecto residual: ni el plano ni la ET declaran la base/alcance de su set | Declarar en el plano y la ET el alcance de cada cuadro de cubicaciones |
| OBS-04 | Mayor | Rasante de drenaje no resuelta: fondo EL 5,45→5,41 (pendiente media ~0,11% en 37 m) sin pendiente de proyecto declarada ni cota invert de empalme a la camara existente | Declarar pendiente longitudinal de la linea DN200 por gravedad y cota de empalme; verificar pendiente minima |
| NOTA-01 | Menor | Camaras "CAMARA N°1...N°7" sin codificacion CD-06-00N (mismo defecto que -002-006 en TM N2) | Rotular CD-06-001 a CD-06-007 |
| NOTA-02 | Menor | Estanque/bomba/fosa/contenedores sin TAG; tuberia solo "Ø8''" sin tag de linea/material | Rotular TAGs y tag de linea |
| NOTA-03 | Menor | Typos "EXTRUCTURAL" (x2), "09,00" | Corregir en Rev C |
| NOTA-04 | Menor | Segundo trazado (7,99 m2) sin secciones ni cota de fondo | Agregar secciones o cota de fondo |
| NOTA-05 | Menor | Profundidad "VAR." sin recubrimiento minimo sobre clave (hay cruces con cañerias existentes top 4,63/4,79); topografia sin citar Levantamiento DIO Abr-2026; sin escala grafica (cajetin "ESCALA IND", PDF A3) | Declarar recubrimiento minimo, citar topografia, agregar barra grafica |

Positivo (C3): no invoca "Informe de Mecanica de Suelos" inexistente; cotas de terreno declaradas (5,72-5,87 + curva 6,00) coherentes en orden de magnitud con NPT +5,75/+6,00; interferencias con cañerias existentes declaradas (top 4,630/4,790); correspondencia planta-cortes por progresivas completa en el trazado largo.

### 2.4 Pendientes heredados TM N1

| ID | Estado en ENTREGA 5 |
|----|---------------------|
| PEND-01 | PARCIAL — DWG-00-001-001 Rev B recibido (con 4 OBS Mayores propias); MC-002-003 declarada pero archivo ausente; DWG-00-002-005 ni declarado ni incluido |
| PEND-02 | PARCIAL — MC-001 Rev 1 adopta los valores ADASA (Ez ±3.357 kgf) pero sigue citando "Memoria Estanque AFTA Taltal" en vez del codigo vinculante P22-IT-06-000-005-0 (via NOTA-03) |
| PEND-03 | EN SEGUIMIENTO, CONFORME — MC-005 Rev 1 declara el diferimiento con las normas correctas (ACI 318-19 Cap.17/Sec.17.10 + ACI 355.2/355.4); el plano -002-007 L1 lo declara tambien (nota 2: pernos pendientes hasta planos vendor). Sigue abierto hasta que BW Water entregue los datos |

## 3. Hallazgos nuevos y cambios no solicitados

### 3.1 Memorias de Calculo (Agente A + verificacion adversarial CERRADA)

1. **MC-001 — armadura de losa: justificar el calculo (OBS, NO rechazo — recalibrado 10-Jun).** La Rev 0 tenia Ø16@100; la Rev 1 declara **Ø12@200**, **elimino la seccion "Verificacion de losa - Fisuramiento"**, no declara el espesor de losa y las secciones de flexion/corte no muestran valores numericos de solicitacion vs capacidad. **Correccion de criterio (usuario):** el verificador adversarial aplico ACI 350 (cuantia 0,5%, contencion de liquido), pero la losa es **fundacion de un estanque PRFV apoyado** — el liquido esta dentro del PRFV, no en contacto con el hormigon → aplica **ACI 318** (cuantia minima de retraccion/temperatura ~0,0018). Con esa vara Ø12@200 (~5,65 cm2/m para e=30) cumple por poco; Ø16@200 (~10 cm2/m, ρ≈0,34%) es el valor preferido. Accion: que L&A **justifique el calculo de la armadura de losa** (cuantia minima ACI 318 + flexion/corte con las solicitaciones del anclaje preinstalado), idealmente Ø16@200. NO escala a Codigo 3/4.
2. **MC-001 — anclaje "preinstalado" con especificacion hibrida** (ver matriz OBS-01): mantiene producto quimico HAS-V-36, sin extremo embebido definido, sin ACI 318-19 Cap.17 explicito, sin reconciliacion Exfibro, FU 34% sin sustento visible (verificaciones PROFIS anunciadas pero figuras/reportes ausentes del texto extraido — confirmar en PDF).
3. **MC-003-001 — coeficiente sismico vertical subio de 0,67 a 0,74** — consistente con la unificacion pedida en OBS-05 (la tabla decia 0,74), pero verificar que los calculos se recorrieron con 0,74 (no solo el texto).
4. **(Candidato a evaluar en calibracion)** MC-001 adopta parametros de suelo (Vs30/Tg, criterios NCh3793) que el verificador adversarial señala como divergentes del informe sismico LNS-ADASA-INF-040-Rev0 — confirmar si es una adopcion ya aceptada en ciclos previos antes de levantar OBS.
5. **(Documentacion)** Conclusiones de MC-001 genericas, sin reconciliar los cambios de la Rev 1 (anclaje + armadura); tabla C5-M de MC-003-001 correcta pero aislada en Materiales, sin criterio de aceptacion/inspeccion en obra (solo "recomendaciones del fabricante").

### 3.2 Especificaciones Tecnicas (Agente B)

3. **ET-101 — cubicaciones de excavacion/relleno cambiaron** sin que el TM N2 lo pidiera (ej.: 5.05→4.22, 6.06→5.06, 1.60→5.01, 1.92→6.01 m3). Cruzar contra el plano nuevo DWG-00-001-001 y el IT-101 (consistencia de cantidades).
4. **ET-102 — "Parrilla de piso ARS-5" cambio a "Parrilla de FRP"** — alineado con la OBS-01 de -002-004 L2 (parrilla PRFV): cambio no pedido a la ET pero CONSISTENTE con lo exigido al plano. Verificar que el plano -002-004 L2 tambien lo adopte.

### 3.3 Descalces ET ↔ IT detectados

5. La ET-102 Rev 0 ya especifica impermeabilizacion (Sika Igol) pero el IT-102 Rev C no la presupuesta; la ET-103 declara C5-M 355 µm pero el IT-103 no presupuesta pintura ni soldadura. El descalce sostiene el Codigo 3 de los IT.
6. La ET-103 Rev 0 **mantiene "pernos post-instalados HILTI HIT RE-500 V3 + HAS-E" y A325 sin proteccion** para ambiente C5-M — incoherente ademas con el rediseño preinstalado de MC-001 para el estanque (verificar a que elementos aplica esa perneria en la ET).

## 4. Anomalias administrativas y de QA (consolidado 10-Jun, insumo TM N3 / correo)

**Fallas de entrega (3 archivos):**
1. **MC-002-003 declarada en carta (item 9) pero archivo no incluido** — vino la Rev 0 antigua de MC-003-001 en su lugar (verificado por caratula). Solicitar el archivo de inmediato.
2. **DWG-00-002-003 LAM2: el PDF entregado es un duplicado de LAM1** (cajetin "PLANO 1 de 3", mismas vistas; 172.464 bytes ambos). **El detalle del inserto INS-1 — destino del callout de la OBS-02 — no llego.** Solicitar re-emision del archivo correcto.
3. **DWG-00-002-006 anuncia "PLANO 1 de 3 / 2 de 3" y la entrega trae solo 2 laminas** — la LAM3 (donde iria el detalle tipico de camara prefabricada exigido en NOTA-01) no vino ni esta declarada en la carta.
4. **DWG-00-002-005 (Detalles de Anclaje y Conexiones)** ni declarado ni incluido — segunda solicitud consecutiva incumplida (Listado 067-032-032-COR-LI-001).

**QA de cajetines y rotulos:**
5. **ET Rev 0 con cajetin "Aprobado Cliente 08-06-2026"** — ADASA no ha emitido aprobacion; estatus prematuro.
6. **Tag de la fosa inconsistente en el paquete**: corregido solo en -002-004 LAM1 (TK-06-004); persiste "TK-06-002" en la implantacion -002-001 y "TK-006-002" en -002-004 LAM2; la carta TT-006 y los IT-101/-102 tambien mantienen TK-06-002.
7. **-002-006 con doble cajetin contradictorio** (cajetin grande "REV B" vs cajetin A3 "REV C", ambos fechados 09-Jun) y formato distinto al resto del paquete.
8. **Fecha "09/09/26" en cajetin de -002-007 C LAM1** (typo por 09/06/26).
9. **Cronologia de revisiones invertida** en cajetines de -002-001 y -002-004 (Rev A 27/05/26 posterior a Rev B 28/04/26).
10. **Marca de perno PA-1 con doble definicion**: postinstalado HAS-V-36 5/8'' L=250 en -002-002 LAM4 vs preinstalado A36 3/4'' L=530 en -002-007 LAM3.
11. **Referencia vendor "EX-2600-F01"** en -002-002 L1/L2 (el plano Exfibro es EX-26005-F01; en L1 ademas sin sufijo de revision).
12. Typos: "2DA EPATA" en titulo de -002-002 (4 laminas); "ELVACION" en -002-004 L1; nota 6 de -002-001 cita la ET como "P22-IT-00-010-103-0" (sigla IT por ET); "RELLENO EXTRUCTURAL" en -001-001 (x2).

## 5. Codigos por documento (CALIBRADO CON EL USUARIO — 10-Jun-2026)

Criterio: el codigo refleja el documento revisado en si (CLAUDE.md Seccion 6.2). Calibraciones del usuario aplicadas: (a) MC-001 → Codigo 2 (armadura @200 aceptable por ACI 318, solo justificar calculo, preferir Ø16@200); (b) ET-103 → Codigo 2 duro; (c) anclaje postinstalado de la bomba ACEPTADO (se retira la OBS); (d) **NO invocar el limite del ciclo del TdR en el TM N3** — el transmittal va 100% tecnico; el tema del ciclo (planos+IT en Rev C aun Codigo 3) queda reservado para una escalacion posterior si persiste.

| Documento | Rev | Codigo | Determinante / accion a Rev 0 o Rev C |
|-----------|-----|--------|---------------------------------------|
| MC-00-002-001 Fundacion Estanque | 1 | **2 — Aprobado con comentarios** | Anclaje preinstalado OK; justificar calculo de armadura de losa (cuantia minima ACI 318, preferir Ø16@200) y conciliar designacion MC↔plano (retirar "HAS-V-36", empotramiento 40 vs 38 cm); declarar recubrimientos 50/70; citar P22-IT-06-000-005-0 como fuente |
| MC-00-002-002 Fundacion Bomba | 1 | **2 — Aprobado con comentarios** | Declarar 50 mm expuesto. Anclaje postinstalado de la bomba aceptado (planos KSB) — sin observacion |
| MC-00-002-003 Sistema Drenajes | 0 | **SIN CODIGO — archivo no recibido** | Falla de entrega; exigir el archivo y revisar en el proximo ciclo |
| MC-00-002-004 Fundacion Contenedor | 1 | **2 — Aprobado con comentarios** | ACI unificado OK; corregir notacion "17.334 [tonf]" + declarar adopcion conservadora; recubrimientos 50/70 |
| MC-00-002-005 Fundacion CIP | 1 | **2 — Aprobado con comentarios** | Declarar 50 mm expuesto; diferimiento de anclajes conforme (PEND-03) |
| MC-00-003-001 Cubierta Metalica | 1 | **2 — Aprobado con comentarios** | C5-M completo + coef. 0,74 unificado + anexos integrados; faltan recubrimientos (pedestales) y evaluar combinacion 1,2D±E |
| ET-00-010-101 Mov. de Tierras | 0 | **2 — Aprobado con comentarios** | Mejoramiento OK; declarar sigma_adm <= 1,0 kg/cm2; residuo "Municipalidad de Antofagasta" |
| ET-00-010-102 Hormigon Armado | 0 | **2 — Aprobado con comentarios** | Incorporacion completa (recubrimientos duales + impermeabilizacion); corregir portada con sigla IT |
| ET-00-010-103 Estructura Metalica | 0 | **2 — Aprobado con comentarios (duro)** | Trasladar a la ET el esquema C5-M por capas que ya vive en la MC/nota general; exigir perneria protegida; corregir sigla portada/nota 6. Sin nueva Rev intermedia |
| IT-00-010-101 / -102 / -103 | C | **3 — Por revisar (los 3)** | Nada levantado: sin Clase 2 AACE, tag TK-06-002 persiste (101/102), sin partidas de impermeabilizacion (102) ni pintura/soldadura (103), hoja ajena "La Chimba" en los 3 |
| DWG-00-001-001 Excavaciones (nuevo) | B | **3 — Por revisar** | 4 OBS Mayores de 1a revision; **punto rector: el plano cubre solo zanjas de drenaje, no las excavaciones de fundaciones → las cubicaciones de excavacion de fundaciones no tienen plano que las respalde** |
| DWG-00-002-001 Implantacion | C | **3 — Por revisar** | NPT por zona sigue sin acotarse (arrastre mayor) + tag fosa TK-06-002 + typo sigla en nota 6 C5-M |
| DWG-00-002-002 Fund. Equipos Ext. | C | **3 — Por revisar** | Anclaje estanque L2 LEVANTADO (logro clave); pero mejoramiento de suelo ausente (L1/L4) + EX-2600-F01 + PA-1 duplicado. (Anclaje de bomba ya no es observacion) |
| DWG-00-002-003 Fund. Contenedor | C | **3 — Por revisar** | Datum absoluto LEVANTADO; pero archivo LAM2 duplicado (detalle INS-1 no verificable) + mejoramiento ausente |
| DWG-00-002-004 Fosa Drenajes | C | **3 — Por revisar** | Rebalse NO indicado + tag regresivo en L2 + M.H.A. sin definir + parrilla sin "pultruida/transito" |
| DWG-00-002-006 Canalizaciones | C | **3 — Por revisar** | CD-06-00N no adoptado + detalle de camara ausente (LAM3 no entregada) + doble cajetin B/C |
| DWG-00-002-007 Fund. CIP | C (L2 B) | **3 — Por revisar** | NPT LEVANTADO (logro clave); pero mejoramiento/impermeabilizacion ausentes (L1/L3) + fecha 09/09/26 + anclajes en hold vendor |
| DWG-00-003-001 Cubierta Metalica | C | **2 — Aprobado con comentarios** | C5-M cumplido por via indirecta (nota 6 de -002-001 → ET-103); corregir typo de sigla |

**Recuento calibrado: 9 Codigo 2 + 10 Codigo 3 + 1 sin codigo (MC-002-003 no recibida) — veredicto global 3 — Por revisar.**

Logros del ciclo (resumen ejecutivo del TM N3): anclaje del estanque rediseñado preinstalado en plano (cierre del punto mas antiguo del stream, abierto desde TM N1), datum absoluto del contenedor, NPT del CIP reconciliado (+6,200/+6,000), pendientes de drenaje acotadas, azimut con cuadro UTM, impermeabilizacion en ET-102 y nota general 10, C5-M en MC y nota general 6. Las 6 MC + 3 ET quedan en via a Rev 0 (Codigo 2); el veredicto 3 lo fijan los planos y los Itemizados.

Determinantes del Codigo 3 global: (1) **mejoramiento de suelo ET-101 ausente en TODOS los planos de fundacion (2o ciclo consecutivo)**; (2) **plano de excavaciones (DWG-00-001-001) cubre solo zanjas — las cubicaciones de excavacion de fundaciones no estan respaldadas por plano** (punto rector del usuario); (3) los 3 IT sin levantar nada (3a evaluacion); (4) NPT por zona sin acotar en la implantacion; (5) fallas de entrega (MC-002-003, -002-003 LAM2 duplicada, -002-006 LAM3) + DWG-00-002-005 aun faltante.

## 6. Correo de remision del TM N3 — directiva del usuario (10-Jun)

El correo a Pablo Castillo que acompaña el TM N3 debe señalar las fallas de entrega y, como **punto mas grave / rector**: **si no se entregan los planos de excavacion de las fundaciones, no hay sustento para las cubicaciones de excavacion de fundaciones** (el DWG-00-001-001 Rev B solo trae las zanjas de drenaje; las cubicaciones de fundaciones aparecen en los cuadros de los planos de fundacion y en el IT sin un plano de excavacion que las respalde). Sin correo separado previo — la mencion va en el correo de remision del TM N3. Archivos a exigir: MC-002-003 (no llego), -002-003 LAM2 correcta (vino duplicada), -002-006 LAM3 (detalle de camara), DWG-00-002-005 (anclajes/conexiones, nunca entregado) y los planos de excavacion de fundaciones que respalden las cubicaciones.
