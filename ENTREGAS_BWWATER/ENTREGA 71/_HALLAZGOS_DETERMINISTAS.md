---
titulo: "Hallazgos verificados — ENTREGA 71 (25007-0071), cinco documentos en Rev 0 IFC"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-06
---

# Hallazgos verificados — ENTREGA 71

> Documento interno de trabajo. **NO ENVIAR.** Recoge lo que quedó confirmado contra fuente primaria, lo que se corrigió antes de darlo por bueno, y lo que no se puede afirmar todavía. El detalle comentario por comentario vive en `_LEDGER_COMENTARIOS.md`.

## Regla de encuadre — leer antes que nada

Los cinco documentos llegaron a esta entrega **desde un Código 2**, que es una aprobación con condición acotada: *"incorpórese lo anotado al emitir Rev 0, sin nueva revisión intermedia"*. Por lo tanto **el veredicto de la Rev 0 lo decide una sola pregunta: ¿se cumplió esa condición?**

Lo que no era condición del Código 2 **no entra en el veredicto**, aunque se haya encontrado ahora y sea cierto. Un documento que ADASA ya aprobó no se degrada por hallazgos nuevos: hacerlo reabre una aprobación propia y le entrega al proveedor la réplica de que el documento ya había sido aceptado. Los hallazgos fuera de esa condición se registran aquí para trazabilidad interna y, si tienen consecuencia operativa, se canalizan por su propia vía — nunca como observación nueva sobre un documento aprobado.

**Las condiciones vigentes eran doce:**

| Documento | Código 2 en | Condición del Código 2 |
|---|---|---|
| PMI `-006` | N20, sobre Rev A | OBS-01, OBS-02, NOTE-01 |
| Visual `-008` | N20, sobre Rev A | OBS-01, OBS-02, NOTE-01 |
| Painting `-011` | N27, sobre Rev B | OBS-01, OBS-02, OBS-03 |
| HP/LP `-010` | N29, sobre Rev D | NOTE-01 (edición de los códigos) |
| Structural `-005-001` | N29, sobre Rev B | NOTE-01, NOTE-02 |

Los otros 21 comentarios del libro mayor pertenecen a ciclos ya cerrados (N23, N26, N27 sobre revisiones anteriores) y se verificaron **solo para saber si el contenido se conservó**. Su resultado es información interna, no materia de este veredicto.

---

## Respuesta binaria

**No hay estado intermedio.** Un comentario se levantó cuando el Rev 0 hace lo que la instrucción pedía, entero. Si hace una parte, no se levantó.

| # | Documento | ID | ¿Levantado? | Por qué |
|---|---|---|---|---|
| 1 | PMI | OBS-01 | **NO** | La cláusula agregada declara el 10% y la testificación, pero no la conformidad UNS S32750 como base de aceptación. `S32750` aparece una sola vez en las 31 páginas, y es en la comment sheet |
| 2 | PMI | OBS-02 | **NO** | No se agregó ninguna declaración de aplicabilidad. El procedimiento del subcontratista conserva íntegro su alcance de refinería |
| 3 | PMI | NOTE-01 | **SÍ** | Pág. 4: *"PERSONAL QUALIFICATIONS / Refer to XPERT PMI procedure."* |
| 4 | Visual | OBS-01 | **SÍ** | Pág. 5: *"Minimum qualification to perform visual inspection SNT-TC-1A VT level II."* |
| 5 | Visual | OBS-02 | **SÍ** | ADASA ofreció dos vías y el proveedor tomó la exclusión. Pág. 4: alcance limitado a *"steel piping and structure welds"* |
| 6 | Visual | NOTE-01 | **NO** | Se pidió listar los formularios y los eliminó. Pág. 8: *"recorded on an inspection record form"*, sin código ni revisión |
| 7 | HP/LP | NOTE-01 | **NO** | La sección 3 fija edición pero no addenda, y los pasos 5.5.2 y 5.6.3 —los que gobiernan los ensayos— siguen ordenando *"the latest edition/addenda of ASME B31.3"* |
| 8 | Painting | OBS-01 | **SÍ** | Pág. 11: `50-80 µm` en el criterio y `50-80 Microns` en la aceptación |
| 9 | Painting | OBS-02 | **NO** | Solo imprimió `355 µm Min`. Los valores por capa no están y la fila `Type` sigue en blanco |
| 10 | Painting | OBS-03 | **NO** | El esquema del cuerpo declara `RAL5012`; la fila `Colour` del formulario sigue vacía |
| 11 | Structural | NOTE-01 | **SÍ** | 551 páginas y 26,6 MB, sin duplicación interna |
| 12 | Structural | NOTE-02 | **SÍ** | La columna `Comment from Client` está poblada en las ocho filas |

**Seis levantados de doce, seis no levantados.** El único documento que levantó todo lo suyo es el informe estructural.

En el barrido completo de los 33 comentarios verificables —incluidos los 21 de ciclos cerrados, que son registro interno— 13 quedaron levantados y 20 no.

| Documento | Entradas | Levantado | No levantado |
|---|---|---|---|
| PMI Procedure `-006` | 3 | 1 | 2 |
| Visual Procedure `-008` | 3 | 1 | 2 |
| HP and LP Pressure Test `-010` | 11 | 2 | 9 |
| Painting Procedure `-011` | 7 | 5 | 2 |
| UHPRO Structural Calculation `-005-001` | 9 | 4 | 5 |
| **Total** | **33** | **13** | **20** |

En la columna "No levantado" se cuentan juntos los que sobrevivieron intactos y los que el proveedor cumplió a medias: para efectos de decisión son lo mismo. El desglose de cuál es cuál está en el estado de cada entrada del libro mayor.

Ninguno de los 13 cierres se aceptó por la declaración del proveedor: los 13 tienen cita literal del cuerpo del Rev 0. Los 38 comentarios emitidos históricamente se extrajeron por análisis del árbol sintáctico de los diez scripts de anotación de los transmittals N20, N23, N26, N27 y N29; 33 requerían verificación y 5 eran notas informativas o declaraciones de cierre.

---

## Tabla de decisión — los seis no levantados

Para juzgar si cada uno es gravitante para el funcionamiento del módulo o solo para la trazabilidad documental.

| # | Documento | ID | Qué pedía la instrucción | Qué hizo el Rev 0 | Por qué no cuenta como levantado |
|---|---|---|---|---|---|
| 1 | PMI | OBS-01 | Cláusula de alcance con **tres** elementos: 10% del Super Duplex de alta, **conformidad UNS S32750 como base de aceptación**, y testificación de ADASA | Agregó una frase con el 10% y la testificación (pág. 4) | Falta el elemento central. `S32750` no aparece en el cuerpo; la sección 13 sigue diciendo *"Acceptance and rejection criteria shall be specified by the customer"* y remite a dos PTS de Shell |
| 2 | PMI | OBS-02 | Declaración de aplicabilidad al proyecto, porque el procedimiento del subcontratista está escrito para servicios de refinería | Nada. Solo borró dos líneas del listado de referencias | Págs. 14, 16, 17, 21 y 24 conservan el programa de mantención de refinería, unidades de ácido HF, hornos de proceso y la tabla de extensión genérica |
| 3 | Visual | NOTE-01 | **Listar** los formularios QAM como referencias externas controladas | Los eliminó del documento | Acción opuesta a la pedida. La Rev 0 dice solo *"an inspection record form"*, sin código, sin revisión y sin remisión |
| 4 | HP/LP | NOTE-01 | Declarar edición **y addenda** de ASME Sección V y B31.3 **a usar para los ensayos** | Fijó `Sección V – 2025` y `B31.3 – 2024` en la sección 3 de referencias | Los pasos 5.5.2 y 5.6.3, que son los que ordenan ejecutar los ensayos, siguen diciendo *"the latest edition/addenda"*. Y no se declaró addenda en ninguna parte |
| 5 | Pintura | OBS-02 | Imprimir en el formulario los espesores nominales **por capa** (80 / 200 / 75 µm) **y el producto por capa** | Reemplazó el placeholder `xxx µm` por `Specified DFT : 355 µm Min` | Las tres columnas de capa no tienen valor objetivo y la fila `Type` sigue en blanco. El proveedor lo difiere: *"Actual product will update in actual report"* |
| 6 | Pintura | OBS-03 | Declarar RAL 5012 en el esquema **y en la fila `Colour` del formulario** | Lo agregó al esquema del cuerpo (pág. 9) | La fila `Colour` del formulario de la pág. 11 sigue vacía en las tres columnas |

### Lectura de materialidad

| # | Qué afecta en la práctica | Peso |
|---|---|---|
| 1 | **Nadie puede aceptar o rechazar una lectura de PMI.** El ITP remite el criterio de aceptación a este procedimiento y el procedimiento lo devuelve al cliente. Es el criterio con que se acepta el super dúplex del circuito de 135 bar | **Alto** |
| 5 | **Un reparto de espesor no conforme pasa el criterio impreso.** 300 + 30 + 25 suma 355 y aprueba. El primario rico en zinc a 80 µm es lo que da la protección C5-M; sobre-espesor de primario con terminación delgada degrada adherencia y resistencia UV en ambiente marino | **Alto** |
| 3 | **Un punto de testificación sin formato aprobado.** La fila 3.2 del ITP exige *"Visual report"*; sin formulario identificado, ADASA y Bureau Veritas no tienen contra qué contrastar el registro que se les presente, y el dossier recibirá un formato que nadie aprobó | **Medio-alto** |
| 2 | Más allá de la higiene documental, el anexo **contradice el alcance del proyecto**: su Apéndice 1 fija *"Bolt & Nut 5% per lot"* contra el mínimo de 10% del ITP, y el cuerpo dice que la extensión se rige por PTS 15.02.01 y no por la ET | **Medio** |
| 6 | Completitud del registro. El color está declarado en el cuerpo del procedimiento que sigue el aplicador y en la Painting Specification Rev C aprobada; el riesgo de aplicar un color equivocado es bajo | **Bajo** |
| 4 | Documental. Entre `B31.3-2022` y `B31.3-2024` no hay cambio que altere el ensayo hidrostático a 1,5 veces la presión de diseño. El requisito es de control de configuración, no de resultado del ensayo | **Bajo** |

**Conviene tener presente una asimetría:** el procedimiento de ensayo de presión queda en Código 3 por el ítem 4, que es el **menos gravitante de los seis**. Es consecuencia mecánica de que ese documento tenía una sola condición y no la descargó entera. Los dos hallazgos de mayor peso, el 1 y el 5, viven en documentos que además tienen otras condiciones sin levantar.

---

## 1. Lo urgente: la inspección del 13 y 14 de agosto

La `AQ-QAM-F027 Inspection Request (003)` fija: *"Date and Time : 9.00am - 5.00pm 13 Aug 2026 and 14 Aug 2026 · Location : BW Water, Penang · Inspection Item : 1-HP piping pressure test  2- Painting preparation inspection"*. Las dos jornadas cubren precisamente los dos procedimientos con más defectos abiertos.

### 1.1 Pintura — aquí la Rev 0 corrige y hay que hacerla llegar

El paquete del inspector en `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/PAQUETE_INSPECCION_BV/03_PROCEDIMIENTOS_QA_APROBADOS/` contiene la **Rev B**. Verificado abriendo las dos copias:

| | Rev B (la del inspector) | Rev 0 |
|---|---|---|
| Celda de criterio de perfil, formulario pág. 11 | `40-75 µm` | `50-80 µm` |
| Fila de aceptación, mismo formulario | `50-80 Microns` | `50-80 Microns` |
| Cuerpo, pág. 9 | `50 – 80 microns` | `50 – 80 microns` |

La Rev B se contradice a sí misma dentro de la misma hoja, y su límite inferior permite firmar como conforme un perfil de 40 µm — por debajo del mínimo de 50 del propio cuerpo, de la fila 3.5 del ITP y del anclaje de la ET Sección 5.1.9 — Support Frame. **Reemplazar esa copia antes del 13 de agosto cierra un riesgo real de aceptación.**

### 1.2 Presión — aquí cambiar la versión no arregla nada

La Rev D que tiene el inspector y la Rev 0 comparten todos los defectos. Verificado abriendo ambas:

| | Rev D (la del inspector) | Rev 0 |
|---|---|---|
| Formulario de reporte `AQ-QAM-F018` | ausente | ausente |
| Factor `1.5 x design pressure` | ausente | ausente |
| Cláusula 5.6.5 en el cuerpo | ausente | ausente |
| Calificación exigida al ejecutante | ninguna | ninguna |
| Cuerpo, paso 5.5.12 | `HP piping will test to 135 bar, and LP will test to 7.5 bar` | idéntico |
| "Hold Point" en el cuerpo | no aparece | solo en la comment sheet, citando a ADASA |

El ensayo hidrostático de alta presión es **Hold Point** por la fila 5.2 del ITP. El 13 y 14 de agosto se va a testificar con un procedimiento que no trae formulario donde anotar el resultado, no exige calificación a quien lo ejecuta, y cuya cifra de cabecera contradice a la tabla que gobierna línea por línea (ver 2.2).

### 1.3 El plazo de revisión juega en contra

Calculado, no supuesto: el 6 de agosto de 2026 es **jueves**; la fecha de retorno que pide el Submittal Form, el 9 de agosto, es **domingo**; la inspección cae **jueves 13 y viernes 14**; y los 7 días hábiles que la cláusula 37.2 de las BAE concede a ADASA vencen el **lunes 17 de agosto**. Si se agota el plazo contractual, el inspector entra a taller cuatro días antes con las revisiones antiguas. Cerrar antes del 12 de agosto es una decisión de ADASA, no una obligación.

---

## 2. Los cinco documentos

### 2.1 PMI Procedure `P22-BA-09-000-006` — 1 cerrado, 1 parcial, 1 no levantado

En 31 páginas la Rev 0 agregó **una sola frase de 24 palabras** (pág. 4): *"10 percent of the Super duplex high pressure piping component will be tested and witness by ADASA."*

- **OBS-01 parcial.** Declara el 10% y la testificación. **No declara la conformidad UNS S32750 como base de aceptación**: verificado, la cadena `S32750` aparece una sola vez en las 31 páginas y es en la comment sheet, citando el propio comentario de ADASA. La sección 13 del procedimiento del subcontratista sigue diciendo *"Acceptance and rejection criteria shall be specified by the customer"* y remitiendo a dos PTS de Shell. Y la fila 2.4 del ITP remite el criterio de aceptación a este procedimiento: los dos documentos se apuntan mutuamente y la base química no queda fijada en ninguno.
- **OBS-02 no levantado.** No hay declaración de aplicabilidad al proyecto. El procedimiento del subcontratista sobrevive íntegro con su alcance de refinería: pág. 14 *"PMI is the responsibility of a refinery or fabricator"*, pág. 16 *"Thermowells in HF Acid units"* y *"Fired heater external piping"*, pág. 21 con filas *"Fired Heater / Reformer / Furnace"*. El único cambio en ese anexo fue **borrar** dos líneas del listado de referencias, lo que dejó colgando las normas que el propio cuerpo sigue invocando como criterio de aceptación.
- **NOTE-01 cerrado.** La cláusula copiada del NDE Plan desapareció; la calificación real del operador PMI está en la pág. 10.

Además, el ITP fila 2.4 exige *"Min. 10% for the material and **10% on the weldment**"* y el Rev 0 no menciona la soldadura.

### 2.2 HP and LP Pressure Test `P22-BA-09-000-010` — condición no descargada, Código 3

> **Su condición del Código 2 era una sola: la NOTE-01 del N29, sobre la edición de los códigos.** No se descargó del todo, y eso basta para el Código 3. El resto de esta sección corresponde a los diez comentarios de los ciclos N23, N26 y N27, cerrados en su momento: es **registro interno y no se emite**. El `CC_ADASA` de este documento lleva una sola anotación.

Es el documento con más historial, cuatro ciclos previos.

**Lo que sí cerró.** La línea de PVC que ordenaba 75 bar de hidrostática quedó corregida: pág. 11, `DA-PVC-DN65-09-016 | POLYVINYL CHLORIDE, SCH 80` con 1 / 2 / 3 bar. Barridas las 34 filas de la Line List adjunta, **ninguna línea plástica supera los 7,5 bar** y la relación hidrostática/diseño es 1,5 exacta en las 34. El punto de mayor consecuencia física no reingresó. Y la cláusula 5.7.2.2, que sobrevivió a dos declaraciones falsas de cierre, sigue corregida.

**La contradicción de presión, que es el hallazgo nuevo.** El cuerpo declara dos cifras y la Line List adjunta prescribe seis:

| Presión de ensayo | Líneas | Material |
|---|---|---|
| 135 bar | 4 | Super Duplex |
| 120 bar | 4 | Super Duplex |
| 90 bar | 1 | Super Duplex |
| 75 bar | 2 | Super Duplex |
| 7,5 bar | 13 | PVC |
| 3 bar | 10 | PVC |

Solo 4 de las 11 líneas metálicas se ensayan a los 135 bar que el cuerpo anuncia. La línea `DA-SSD-DN100-09-003`, descarga de la bomba de alta presión, tiene diseño 60 bar y ensayo listado en 90; aplicarle los 135 del cuerpo sería 2,25 veces su presión de diseño. Y la fila 5.2 del ITP también fija 135 bar al 100% del sistema de alta presión, sin remitir a la Line List.

**Las tres regresiones.** Se detallan en la sección 4.

**La contradicción normativa.** La sección 3 fija `ASME B31.3 – 2024 edition` (edición que existe, publicada el 27-Dic-2024), pero los pasos 5.5.2 y 5.6.3, que son los que gobiernan la ejecución, siguen ordenando *"the latest edition/addenda of ASME B31.3"*.

### 2.3 Visual Procedure `P22-BA-09-000-008` — 1 cerrado, 1 parcial, 1 no levantado

- **OBS-01 cerrado.** Pág. 5: *"Minimum qualification to perform visual inspection SNT-TC-1A VT level II."*
- **OBS-02 parcial, y abre un hueco de cobertura.** La exclusión de los termoplásticos se ejecutó **borrando la palabra** del alcance: `thermoplastic` no aparece en el cuerpo, no hay frase de exclusión ni remisión a otro documento, y los criterios de la sección 5.7 son solo ASME B31.3 y AWS D1.1. El problema es que el **NDE Plan Rev C, aprobado y en manos del inspector**, exige en su sección 7.0 `Low Pressure (PVC) | VT 100%` y fija en su sección 8.0 el criterio *"DVS 2202-1 (Low Pressure Piping)... Evaluation of discontinuities shall be meet the applicable requirements from Section 7.3 to Section 7.7"*. Ningún documento entregado describe cómo se ejecuta ni cómo se acepta ese 100% de inspección visual sobre las juntas de PVC.
- **NOTE-01 no levantado.** Se pidió **listar** los formularios QAM como referencias externas controladas; el proveedor los **eliminó**. La Rev A nombraba *"QAM-F004 ... and QAM-F005"*; la Rev 0 dice solo *"an inspection record form"*. No queda identificado ningún formulario, código de registro ni revisión de formato con el cual levantar un acta de inspección visual, y la fila 3.2 del ITP exige *"Visual report"* como certificado en un punto de testificación.

**Encuadre necesario para el hueco termoplástico:** no es incumplimiento del proveedor. La propia OBS-02 de ADASA ofrecía *"add DVS 2202-1 visual acceptance **or** exclude thermoplastics"*, y el proveedor eligió la segunda. La vía de cierre es alinear el NDE Plan, no imputar una falta.

### 2.4 Painting Procedure `P22-BA-09-000-011` — condición descargada solo en parte, Código 3

> Su condición eran las tres observaciones del N27 sobre el formulario del Anexo A. Se descargó una. Las cuatro del N23 que aparecen abajo se verificaron por regresión y **no regresaron**; su resultado es confirmatorio y no se emite.

Es el documento que mejor respondió. Las cuatro observaciones del N23 en seguimiento no regresaron: el sistema Jotun de tres capas se mantiene, la carta `TSS-DD-MYPC039-26` con la declaración C5M/CX sigue anexa, el alcance sigue acotado a `ASTM A36 carbon steel and exclude stainless steel and non-metallic surface`, y adherencia, ISO 2808 y SSPC-SP-10 siguen citados. Las páginas 12 a 36 son idénticas carácter por carácter a la Rev B.

Los dos parciales tienen la misma causa: **el cuerpo se corrigió y el formulario del Anexo A no**.

- **OBS-02 parcial.** El placeholder `xxx µm` se reemplazó por `Specified DFT : 355 µm Min`. Pero los valores nominales por capa (80 / 200 / 75) no aparecen en el formulario y la fila `Type` sigue en blanco en las tres columnas. El proveedor lo admite: *"Actual product will update in actual report"*. Consecuencia práctica: un reparto no conforme que sume el total —por ejemplo 300 + 30 + 25— pasa el criterio impreso.
- **OBS-03 parcial.** El cuerpo declara `Finish Colour RAL5012 LUMINOUS BLUE` (pág. 9), que es la mitad de lo pedido. La fila `Colour` del formulario sigue vacía, y se había pedido literalmente *"here **and in the Colour row of the inspection form**"*.

La aceptación que ADASA emitió en el N27 estaba condicionada a cuatro variables: sistema Jotun C5-M, no menos de 355 µm totales, RAL 5012 y perfil de 50 a 80 µm. El registro que el inspector firma controla dos de las cuatro.

Salvedad de fondo que conviene tener presente: la declaración C5-M vive **solo** en la carta anexa del fabricante, dirigida a *"BW WATER FDU SKID FRAME"* y sin mención del proyecto Taltal; el cuerpo del procedimiento no declara categoría de corrosividad en ninguna parte.

### 2.5 UHPRO Structural Calculation `P22-CD-09-005-001` — condición descargada, Código 1

> **Sus dos condiciones del Código 2 se cumplieron**, de modo que este documento va a Código 1 y **no lleva `CC_ADASA`**. Todo lo que sigue en esta sección, salvo esos dos puntos, corresponde a los siete comentarios del N26 que ADASA cerró al codificar la Rev B en el N29: es **registro interno y no se emite**. Se conserva porque parte de ello contradice lo que se dio por cerrado y conviene tenerlo trazado.

Los dos puntos del N29 cerraron: el archivo dejó de estar duplicado (551 páginas y 26,6 MB contra 1.101 y 58 MB) y la comment sheet ahora sí reproduce el texto de los comentarios de ADASA. También cerraron el resumen de resultados sísmicos en el cuerpo (peso sísmico 122,41 kN, corte basal 41,62 kN según NCh 2369:2003) y la utilización gobernante escrita como número (0,454 < 1,0).

**OBS-03 no levantado, y es de sustancia, no de forma.** El listado impreso de combinaciones quedó corregido —224/225 pasan a EOX y 226/227 a EOZ—, pero el modelo no cambió. Parseadas las reacciones del Attachment C: los casos básicos 1 (EOX) y 2 (EOZ) difieren en los ocho nodos de apoyo, y sin embargo las combinaciones 224 y 226 dan reacciones **idénticas dígito a dígito**, igual que 225 y 227. Dos combinaciones que solo se distinguen por la dirección del sismo no pueden coincidir si las direcciones difieren. El caso de gravedad mínima en dirección X que se pidió sigue sin existir en el análisis. El proveedor lo declara como *"a typographical error in the calculation report only"* y corrigió la descripción.

**OBS-01 parcial: faltan los recipientes a presión.** La sección *"D. Bolt Design at the Base"* (pág. 20) cubre cuatro de los seis TAG pedidos — filtro RO, bomba HP (motor y tubería), turbo de alimentación y turbo interetapa. **No hay verificación de pernos para BOI-09-001 ni BOI-09-002**, que el propio informe declara en su pág. 64 como *"RO PRESSURE VESSELS | Operating Weight 9169.2 lbs [4160.0 kg]"* — el ítem de proceso más pesado, y el que ADASA nombró explícitamente.

**NOTE-01 parcial, con un dato duro.** El chequeo de pernos de la base del contenedor (pág. 25) está calculado con reacciones que **no son las de este informe**: usa 4,711 / 2,249 / 9,42 kN, que son los valores del Attachment C de la Rev A; el Attachment C de la Rev 0 da −4,642 / 2,322 / −9,547 kN para esos mismos nodos y casos. Es justamente el dato que obras civiles necesita para dimensionar la fundación.

**OBS-05 parcial.** El contador de páginas no se unificó: la portada dice `Page: 1of 551`, correcto, y todos los pies de Aulem siguen diciendo `Page N of 548`.

**NOTE-02 parcial.** El suelo se sigue rotulando `Type E` atribuido a *"NCh2369:2003, Table 5.3"*, tabla que clasifica en tipos I a IV y no contiene un tipo E — la cita es refutable tal como está. Los parámetros usados, `T' = 1.35` y `n = 1.80`, sí corresponden al suelo Tipo IV, el más desfavorable, y se agregó la nota *"Soil classification is assumed as a conservative envelope pending geotechnical confirmation."*

---

## 3. Lo transversal a los cinco

**La cláusula de precedencia invertida.** Los cuatro procedimientos declaran en su página 4: *"In case of conflict between code requirements and client specification, code requirements shall prevail."* La misma cláusula está en el NDE Plan Rev C. La **cláusula 12 de las BAE** fija el orden de prelación del contrato — Contrato, modificaciones, Carta de Adjudicación, Circulares, BAE, ET, Oferta Técnica, Oferta Económica — y las normas no figuran en esa lista: entran por la ET. Un procedimiento del proveedor no puede alterar ese orden. Tiene consecuencia numérica concreta: la ficha técnica del Barrier 80 recomienda *"surface profile 30-85 µm"*, rango que admite 30 µm, muy por debajo del 50 que el propio procedimiento fija.

**El ITP cita dos documentos que no existen.** Sus filas 5.1 y 5.2 invocan `PROV-PROC-PH-LP-001` y `PROV-PROC-PH-HP-001`; el número interno real del entregable es `PROV-PROC-HP-LP-001`, y es uno solo. Un inspector que busque el documento que respalda el Hold Point no lo encuentra. Los otros tres números del ITP sí calzan.

**Asimetría de calificación de personal.** El Visual exige SNT-TC-1A VT Nivel II, el PMI remite a entrenamiento OEM más probeta aprobada por el mandante, el de pintura acredita Frosio Nivel III y AMPP-NACE Nivel II. **El de presión no exige ninguna**, y es el único de los cuatro ensayos que es Punto de Detención.

**Un pendiente que es nuestro, no del proveedor.** El procedimiento XPERT al que el PMI Rev 0 remite su calificación exige *"PMI operator mock-up test shall be conducted and approved by Owner"*. No hay registro de que ADASA lo haya aprobado. Al remitir la calificación a ese documento, esa aprobación pasa a ser condición del ensayo, y si no está hecha bloquea la testificación.

**Un defecto de rotulado en documento propio.** La guía del paquete de inspección lleva código `ADASA-BV-PAQUETE-INSPECCION-Rev1` y fecha 21/07/2026 en el encabezado de sus once páginas, pero el campo `Revisión N°` de ese mismo encabezado dice **0**. Es el mismo tipo de defecto que ADASA ha observado a BW Water.

---

## 4. Las tres regresiones de cierre verificado — registro interno, no se emiten

> **Ninguna de estas tres se levanta como observación.** Todas ocurrieron en la Rev D, que ADASA aprobó como Código 2 en el transmittal N29, y ninguna era la condición de ese Código 2. Se registran aquí por dos motivos: para no repetir el modo de falla en la próxima revisión, y para tener la trazabilidad si alguna aparece después en el dossier o en terreno.

Distintas de un pendiente arrastrado: ADASA comprobó el cierre y el contenido se perdió después.

| Qué se perdió | Estaba en | Se perdió en | Estado en Rev 0 |
|---|---|---|---|
| Cláusula 5.6.5 del procedimiento de presión | Rev C, con su texto propio | Rev D | Ausente; el cuerpo salta de 5.6.4 a 5.6.6 |
| Formulario `AQ-QAM-F018` *"Pressure and Leak Test Report"* | Rev C, página 13 | Rev D | Ausente; cero ocurrencias de `AQ-QAM` |
| Factor `1.5 x design pressure` | Rev C, paso 5.5.12 | Rev D | Ausente |

Las tres se introdujeron en la **misma edición, la Rev D**, que ADASA codificó 2 en el transmittal N29. **Parte del hallazgo es nuestro:** la revisión del N29 se concentró en la edición normativa y no re-barrió el documento contra la Rev C, de modo que las tres pérdidas pasaron sin detectarse y viajaron a un documento emitido For Construction.

El caso de la cláusula 5.6.5 completa una serie de cuatro apariciones: pedida en el N23, repedida en el N26, verificada como corregida en el N27 (*"The gap at 5.6.5 is corrected"*), perdida en la Rev D y ausente en la Rev 0.

---

## 5. Veredicto propuesto por documento

Sobre un Rev 0 el Código 2 no tiene mecanismo aplicable: ordenaría incorporar algo a un documento que ya salió. Solo caben **Código 1** —la condición se cumplió— o **Código 3**, re-emitir como Rev 1. Cada veredicto se funda **únicamente en la condición del Código 2**, según la regla de encuadre del inicio.

| Documento | Condiciones | Levantadas | No levantadas | Propuesta |
|---|---|---|---|---|
| `P22-CD-09-005-001` Structural | 2 | **2** | 0 | **1 — Approved** |
| `P22-BA-09-000-008` Visual | 3 | 2 | 1 | **3** |
| `P22-BA-09-000-006` PMI | 3 | 1 | 2 | **3** |
| `P22-BA-09-000-011` Painting | 3 | 1 | 2 | **3** |
| `P22-BA-09-000-010` HP/LP | 1 | **0** | 1 | **3** |

### Por qué cada uno

**Structural — Código 1.** Sus dos condiciones se cumplieron: el archivo dejó de estar duplicado (551 páginas y 26,6 MB) y la comment sheet reproduce el texto de los comentarios de ADASA junto a cada respuesta. Todo lo demás que aparece en la sección 2.5 de este documento pertenece a los siete comentarios del N26, que **ADASA cerró al codificar la Rev B como 2 en el transmittal N29**. No se reabren.

**HP/LP — Código 3, por una sola razón.** La condición decía *"state the applicable edition and addenda of ASME Section V and ASME B31.3 **to be used for the tests**"*. La sección 3 fija `ASME Code Section V, Article 1 – 2025 edition` y `ASME B31.3 – 2024 edition`, pero los pasos que gobiernan la ejecución de los ensayos, el 5.5.2 y el 5.6.3, siguen ordenando *"the latest edition/addenda of ASME B31.3"*. La edición no queda fijada para los ensayos, que es exactamente lo que se pidió; y las addenda no se declaran. Ese es el determinante y basta. Todo lo demás del documento —numeración, formulario, factor de derivación, contradicción con la Line List— queda fuera del veredicto por la regla de encuadre.

**PMI — Código 3.** De sus tres condiciones solo se descargó NOTE-01. OBS-01 quedó a medias: se declaró el 10% y la testificación, pero no la conformidad UNS S32750 como base de aceptación. OBS-02 no se ejecutó: no hay declaración de aplicabilidad al proyecto y el procedimiento del subcontratista conserva íntegro su alcance de servicios de refinería.

**Visual — Código 3, por NOTE-01 sola.** OBS-01 se descargó. **OBS-02 también se descargó**: ADASA ofreció dos vías —citar DVS 2202-1 o excluir los termoplásticos— y el proveedor tomó la segunda, que es una de las dos que ADASA autorizó. NOTE-01 no se descargó: se pidió **listar** los formularios como referencias externas controladas y el proveedor los **eliminó**, dejando el procedimiento sin ningún formulario identificado para un punto de testificación.

**Painting — Código 3.** OBS-01 se descargó y está bien verificado. OBS-02 y OBS-03 no: el formulario del Anexo A sigue sin los espesores nominales por capa, sin el producto y con la fila `Colour` en blanco, cuando la instrucción decía literalmente *"state RAL 5012 here **and in the Colour row of the inspection form**"*.

**Veredicto de conjunto propuesto: 3 — To be revised.** Cuatro documentos no descargaron su condición; el Structural sí y va a Código 1.

### Nota sobre el alcance de las observaciones a emitir

Los `CC_ADASA` de los cuatro Código 3 llevan **solo** las anotaciones correspondientes a la condición del Código 2 que no se descargó. No se anotan hallazgos nuevos sobre documentos aprobados.

---

## 5 bis. La única decisión de criterio que queda abierta

**El formulario `AQ-QAM-F018` del procedimiento de presión.** No es un hallazgo nuevo: es una nota del N26 que ADASA **cerró explícitamente en el N27** (*"the report form is now attached and carries no pre-printed pressure, which closes the Transmittal N26 note"*), y el formulario desapareció después, en la Rev D. Hay dos lecturas y conviene elegirla a conciencia:

- **Tratarlo como reapertura y no emitirlo.** Es lo coherente con la regla de encuadre: la Rev D se aprobó como Código 2 y la ausencia del formulario ya estaba ahí. Reclamarlo ahora es reabrir una aprobación propia.
- **Tratarlo como consulta operativa, no como observación.** No se imputa falta ni se degrada el documento; se pregunta, antes del Punto de Detención del 13 y 14 de agosto, **en qué formulario se va a registrar el ensayo hidrostático**, dado que el procedimiento remite a un *"Pressure Test Report"* que el paquete ya no contiene. Es una pregunta legítima de ejecución y no toca el veredicto.

La segunda vía es la recomendada: obtiene lo que hace falta para testificar sin contradecir la aprobación previa.

---

## 6. Lo que no se puede afirmar

- **La sustancia del cálculo sísmico no se re-auditó.** Por alcance acordado, el corte basal de 41,62 kN y la utilización de 0,454 se dan por aceptados desde el N29. Lo verificado es el cierre de los nueve comentarios.
- **Las advertencias de STAAD del Attachment E no se evaluaron.** El listado trae avisos de inestabilidad en los nodos 3472 y 3473 en las seis direcciones, y una nota de que el peso propio aplicado (13,583 kN) es menor que el peso total de los elementos estructurales (44,297 kN) en el caso de carga 60. Queda fuera del alcance de esta verificación; se registra como dato de estado.
- **La fecha del listado STAAD no coincide con la revisión.** Las 845 páginas del anexo llevan encabezado *"Monday, June 29, 2026"* y el banner de cierre dice *"DATE= JUL 10,2026"*; la Rev 0 está fechada 23-Jul-2026. No se determinó si eso implica que el anexo no corresponde al modelo de la Rev 0.
- **No consta si Bureau Veritas recibió actualizaciones del paquete después del 21-Jul-2026.** Se trabajó sobre el contenido actual de la carpeta.
- **No consta la aprobación de ADASA a la probeta de calificación del operador de PMI.**

---

*Verificado el 06-Ago-2026. El detalle comentario por comentario, con la cita literal de cada estado, vive en `_LEDGER_COMENTARIOS.md`.*
