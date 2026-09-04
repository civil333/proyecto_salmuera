---
titulo: ENTREGA 81 — libro mayor de comentarios y su cierre
codigo: submittal 25007-0081
fecha: 2026-08-20
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 81 (submittal `25007-0081`) — libro mayor de comentarios

**Recibida el jueves 20-Ago-2026.** Cinco documentos, todos del paquete de calidad y fabricacion, todos re-emisiones que responden al Transmittal N32 del 12-Ago. El Submittal Form declara fecha de emision 20-Ago-26 y pide respuesta el **domingo 23-Ago-26**; el plazo contractual de ADASA son siete dias habiles desde la recepcion, per la Clausula 37.2 de la BAE, es decir el **lunes 31-Ago-2026**.

| # | Documento | Codigo | Rev | Sub. For | Veredicto previo |
|---|---|---|---|---|---|
| 1 | HP and LP Pressure Test Procedure | `P22-BA-09-000-010` | 1 | IFC | Rev 0 devuelta **sin codigo** (TM N32) |
| 2 | Painting Procedure | `P22-BA-09-000-011` | 1 | IFC | Rev 0 devuelta **sin codigo** (TM N32) |
| 3 | Liquid Penetrant Examination Procedure | `P22-BA-09-000-014` | B | IFA | Rev A en **Codigo 3** (TM N32) |
| 4 | Radiography Examination Procedure | `P22-BA-09-000-015` | B | IFA | Rev A en **Codigo 3** (TM N32) |
| 5 | Ultrasonic Thickness Procedure | `P22-BA-09-000-016` | B | IFA | Rev A en **Codigo 3** (TM N32) |

**Alcance de esta revision, fijado por el usuario.** Los dos primeros llegan por sobre la Rev 0 y ya estan emitidos para construccion: se juzgan solo por si se incorporo lo que era condicion. Los tres ultimos, aunque estan en Rev B, se revisan con el mismo criterio: el universo es lo que el TM N32 exigio, y nada mas. Los hallazgos fuera de ese universo van a `_HALLAZGOS_DETERMINISTAS.md` y no se emiten.

**Higiene del paquete.** Los cinco archivos tienen texto extraible, ninguno escaneado. Los cinco hashes de contenido son nuevos: no hay duplicado de payload contra la ENTREGA 71 ni la 75.

---

## Hoja de comentarios: quien la trae y quien no

| Documento | Hoja consolidada | Observacion |
|---|---|---|
| `-010` Rev 1 | Si, pagina 14 | Un solo item, transcrito como *"NOTE-01: Identify the pressure test record"*. El comentario que ADASA emitio fue una **OBS-01** de seis lineas que incluia el registro grafico. La hoja lo resume a una frase y responde a esa version resumida |
| `-011` Rev 1 | Si, paginas 37 y 38 | Tres items, los tres con *"Revised as per comment"* |
| `-014` Rev B | **No** | Venia de Codigo 3 con dos observaciones bloqueantes |
| `-015` Rev B | **No** | Idem |
| `-016` Rev B | **No** | Idem |

Los tres procedimientos de ensayos no destructivos se re-emiten **sin declarar como respondieron cada comentario**. La verificacion se hizo entonces contra el texto, por diferencia linea a linea entre la Rev A y la Rev B.

---

## 1. HP and LP Pressure Test Procedure `P22-BA-09-000-010` Rev 1

**Origen:** OBS-01 y NOTE-01 del TM N32, subseccion 2.3. Compromiso `PRG-27`, vencido el 13-Ago.

### Cierre punto por punto

| Punto del TM N32 | Pedido, literal | Declarado en la hoja | Verificado en la Rev 1 | Estado |
|---|---|---|---|---|
| OBS-01, primera parte | *"identify the form on which the high-pressure test is recorded, by number and revision, and make it available to the inspector for that attendance"* | *"Pressure test record attached"* | El formulario **`AQ-QAM-F018` "Pressure and Leak Test Report" Rev 4, fecha efectiva 12.08.2024**, entra como pagina 11 del procedimiento, en blanco y con membrete de BW Water. Es el mismo que estaba en la pagina 13 de la Rev C y desaparecio en la Rev D. La clausula 5.8.1 sigue diciendo solo *"The results of the test shall be recorded in the Pressure Test Report"*, sin nombrarlo por numero ni revision | **Cerrado con residuo** — el formulario esta incorporado, de modo que queda identificado por pertenencia; el texto no lo nombra |
| OBS-01, segunda parte | *"attach that form to this procedure, **so that it produces the graphic record**"* | Sin mencion | **No cerrado.** Verificado por render a 190 dpi de la pagina 11: el formulario registra valores puntuales — `Test Pressure`, `Start Test Pressure`, `Start Time (Start Date)`, `End Test Pressure`, `End Time (End Date)`, `Pressure Drop` — y un checklist de once items. **No tiene zona de registro grafico ni casilla para adjuntar la carta del registrador**, pese a identificar dos veces un `Gauge/Recorder S/N` con su fecha de calibracion. Las filas 5.1 y 5.2 del ITP `P22-BA-09-000-004` Rev 0 exigen como certificado un *"Pressure Test report (Graphic P vs T)"*, y la 5.2 es Punto de Detencion | **Cierre parcial** — segunda vez que se pide el registro del ensayo |
| NOTE-01 | Constataba que las clausulas 5.5.2 y 5.6.3 ya fijaban la edicion | — | Sin cambios; sigue cerrado | **Cerrado** |

### Lo que decide

El ensayo hidrostatico de alta presion es Punto de Detencion y el `Inspection Request 004` lo traslado al **20 y 21 de agosto**, que es esta semana. Con el formulario tal como esta incorporado, el certificado que se emita no reune lo que la fila 5.2 del ITP define como certificado del Punto de Detencion.

### Punto adicional que SI se emite: la clausula 5.5.12

Detectado el 20-Ago al revisar el informe de ensayo de ese mismo dia, y **fuera del universo estricto del TM N32**. Se emite igual, por dos razones: es el cierre incompleto de la **OBS-03 del TM N27**, que pedia *"state the governing envelope per circuit ... and name the Line List revision that fixes the value line by line"*, y hay un **hecho nuevo** que prueba que el punto no estaba cerrado — el ensayo del 20-Ago.

| Punto | Verificado en la Rev 1 | Estado |
|---|---|---|
| La clausula 5.5.12 enuncia el binomio junto a la remision a la tabla | Literal: *"HP piping will test to 135 bar, and LP will test to 7.5 bar. Testing pressure will refer in approved line list (Doc no: P22-LI-09-009-003 REV 0)"*. Son dos instrucciones incompatibles: dos valores fijos y una tabla que prescribe seis. **El factor 1,5 no esta escrito en ninguna parte del procedimiento**; estaba en la Rev C y se perdio en la Rev D | **Abierto, emitido en el TM N35** |

**No degrada el documento.** El procedimiento remite a la Line List aprobada, de modo que la regla existe; lo que faltaba era que ADASA declarara cual gobierna. Decision del usuario: se mantiene **Codigo 1** y el transmittal emite la declaracion, la tabla por TAG y la retencion de ensayos. Reabrir el codigo de un documento ya emitido para construccion, por un punto que ADASA misma dejo pasar en el TM N32, seria contradecir una aprobacion propia.

El detalle completo de la regla, con la cadena PIE → ITP → Line List → procedimiento y la tabla de las once lineas, esta en `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/_ANALISIS_HYDROTEST_20AGO.md`.

---

## 2. Painting Procedure `P22-BA-09-000-011` Rev 1

**Origen:** OBS-01, NOTE-01 y NOTE-02 del TM N32, subseccion 2.4. Compromiso `PRG-27`.

### Cierre punto por punto

| Punto del TM N32 | Pedido, literal | Declarado en la hoja | Verificado en la Rev 1 | Estado |
|---|---|---|---|---|
| OBS-01, la unica condicion vinculante | *"state RAL 5012 Luminous Blue for the third coat on this form"* | *"Revised as per comment"* | Pagina 11, formulario `F/PQR/SP(B)IR-15 R2`, fila `Colour`: primera capa Grey, segunda Grey, **tercera `RAL 5012 Luminous Blue`**. Coincide con la pagina 9 del cuerpo y con la Painting Specification `P22-ET-09-006-002` Rev C | **Cerrado** |
| OBS-01 del TM N27, perfil de anclaje | *"unify the form to a single 50-80 um criterion"* | *"Revised as per comment"* | La fila `ROUGHNESS` lee `50-80 Microns` y la fila `Criteria` de la actividad de granallado lee `50-80 um`. Ya no aparece el rango 40-75 | **Cerrado** — venia cerrado desde la Rev 0 |
| OBS-02 del TM N27, espesor por capa | *"print the nominal values (80 / 200 / 75 um, not less than 355 um total) and the product per coat"*, replanteado por el N32 y declarado expresamente **"Not a condition of this transmittal"** | *"xxx um update to 355um min, Actual product will update in actual report"* | La fila `Specified DFT` sigue en `355 µm Min`, sin los valores por capa. La fila `Type` si trae el producto de cada capa: Barrier 80 / Penguard Midcoat M20 / Hardtop XP | **Abierto, no exigible** — el N32 lo saco de las condiciones |
| NOTE-02, revision que gobierna | *"Confirm which revision governs the painting preparation inspection"* | Sin mencion | Superado por los hechos: existe ahora una Rev 1 unica, fechada 19-08-2026. **Genera accion propia de ADASA**: el paquete del tercero inspector queda desactualizado y hay que reponerlo | **Cerrado por sustitucion** |

El documento crece de 11 a 38 paginas al incorporar las hojas de datos tecnicos de Jotun de las tres capas. Contenido adicional que no se pidio y que no estorba.

---

## 3. Liquid Penetrant Examination Procedure `P22-BA-09-000-014` Rev B

**Origen:** OBS-01 a OBS-04 y NOTE-01 del TM N32, subseccion 2.5. Compromiso `PRG-25`.

### Cierre punto por punto

| Punto del TM N32 | Pedido, literal | Verificado en la Rev B | Estado |
|---|---|---|---|
| **OBS-01**, bloqueante | *"state ASME B31.3 para. 341.3.2 and Table 341.3.2 here"*, en la clausula 13.0, en lugar del Apendice 6 | Se **agrego** un bloque `b. ASME B31.3 - Process Piping` con el texto del criterio, **manteniendo** `a. ASME Section VIII Div. 1, Appendix 6`. La clausula ofrece ahora dos criterios en paralelo, sin declarar cual gobierna, y no cita el parrafo 341.3.2 por su numero | **Cierre parcial** |
| **OBS-02**, bloqueante | *"state on the form the same criterion required by OBS-01"* | **Sin cambio alguno.** La pagina 19 sigue leyendo `Acceptance Criteria: ASME VIII DIV.1 Appendix 8.` | **No cerrado** |
| OBS-03, aseo | Emitir el formulario en blanco | Sin cambio: sigue `Report No: XESSB-ITS-PT230601(Cth)`, `Job No: (Cth: ITS-PT230601)`, los lotes de penetrante y el resultado ya escrito | **No cerrado** |
| OBS-04, aseo | Indice de revision unico en el anexo | Sin cambio: `Rev.01` en las paginas 11 a 14 del anexo y `Rev.00` en la 15 | **No cerrado** |
| NOTE-01, aseo | Proposito, numero de documento y Articulo 6 | Sin cambio: la clausula 1.0 sigue describiendo el documento como procedimiento de identificacion positiva de materiales y la 4.0 sigue citando el Articulo 9 | **No cerrado** |

**El diferencial completo entre la Rev A y la Rev B son once lineas**: el bloque `b. ASME B31.3` y la fila de revision del cajetin. Nada mas cambio en el documento.

**Matiz de equidad, para el Status:** los umbrales del criterio B31.3 que se agrego coinciden digito a digito con los del Apendice 6 que se mantiene y con los del Apendice 8 del formulario — sin indicaciones lineales relevantes, redondeadas mayores a 5 mm, cuatro o mas en linea separadas 1,5 mm o menos. El riesgo de que el examinador acepte una soldadura que otro criterio rechazaria es nulo. Lo que sigue abierto es que el registro que entra al dossier citara el codigo de recipientes a presion y no el de cañerias, que es el que la ET Seccion 8 y el NDE Plan Rev C hacen aplicable.

---

## 4. Radiography Examination Procedure `P22-BA-09-000-015` Rev B

**Origen:** OBS-01 a OBS-04 y NOTE-01 del TM N32, subseccion 2.6. Compromiso `PRG-25`.

### Cierre punto por punto

| Punto del TM N32 | Pedido, literal | Verificado en la Rev B | Estado |
|---|---|---|---|
| **OBS-01**, bloqueante | *"state ASME B31.3 para. 341.3.2 and Table 341.3.2 as the acceptance criteria in clause 23.0, **in place of the list of five codes**"* | Se incorporo una **pagina nueva al final del anexo con la Tabla 341.3.2-1 de ASME B31.3-2024 completa**, *Acceptance Criteria for Welds — Visual and Radiographic Examination*, con sus notas generales; verificado por render a 200 dpi, porque la tabla entra como imagen y no aparece en la extraccion de texto. La clausula 23.0 **conserva la lista de cinco codigos** con la formula *"shall be in accordance with the specific contract specification, codes and standards"*, y solo añade el parentesis *"(Acceptance criteria table in page 23)"* en la letra d | **Cierre parcial** — la tabla exigida esta incorporada; el que gobierna sigue sin declararse |
| **OBS-02**, bloqueante | *"replace the 1.8 mm of clause 12.1 ... with the limit that T-274 of ASME Section V, Article 2 requires for the wall radiographed here"* | **Sin cambio alguno.** La clausula 12.1 sigue leyendo literal *"The value however shall not exceed 1.8 mm for welds of 'PP' (pressure piping) stamped items"* | **No cerrado** |
| OBS-03, aseo | Declarar material y franja de espesor del proyecto | Sin cambio | **No cerrado** |
| OBS-04, aseo | Renumerar el cuerpo | Sin cambio: la clausula 12.0 sigue con sub-numeracion 11.1 a 11.3, la 13.0 con 12.1 y la 14.0 con 13.1 | **No cerrado** |
| NOTE-01, aseo | Proposito, numero de documento y Articulo 2 | Sin cambio | **No cerrado** |

**El diferencial completo entre la Rev A y la Rev B son dos cambios**: el parentesis de la letra d y la pagina de la tabla.

---

## 5. Ultrasonic Thickness Procedure `P22-BA-09-000-016` Rev B

**Origen:** OBS-01 a OBS-05 y NOTE-01 del TM N32, subseccion 2.7. Compromiso `PRG-25`.

### Cierre punto por punto

| Punto del TM N32 | Pedido, literal | Verificado en la Rev B | Estado |
|---|---|---|---|
| **OBS-01**, bloqueante y critica | *"state that criterion in clause 9.0"*, el del NDE Plan Rev C: el espesor medido igual o mayor al espesor minimo requerido por el codigo de diseño y el calculo de ingenieria | La clausula 9.0 paso de *"Acceptance or rejection shall be the discretion by the client"* a *"Acceptance as per ASME Section II (SA790/790M) according to Grade UNS2750"*. **Es un criterio de material, no de espesor.** SA-790 es la especificacion de suministro del tubo: composicion, propiedades mecanicas y tolerancias de fabricacion. No enuncia la comparacion contra el espesor minimo de diseño, que es lo que una medicion base de fabricacion tiene que resolver. La designacion ademas se escribe `UNS2750`, sin la S y sin el 3, y la referencia como `SA79M` | **No cerrado** — segunda vez que se pide el criterio |
| **OBS-02**, bloqueante | *"write the technique sheet for UNS S32750, stating the sound velocity and the calibration block for that material"* | Cerrado en lo esencial. El alcance del anexo ahora dice *"written for techniques involving for UNS S32750"*; la clausula 4.1 paso de `Calibration Block` a **`Calibration Block Material Grade UNS S32750 or S32250`**; el Apendice 1 se retitulo `UTM TECHNIQUE FOR UNS S32750` y su fila de material paso de `Carbon Steel` a `UNS S32750`; y las referencias suman `ASME B31.3` y `ASME BPVC Section II (SA790/SA79M) (S32750)`. **Falta el valor de la velocidad de propagacion**, que el pedido nombraba, aunque el procedimiento incorpora la calibracion de velocidad sobre bloque escalonado del propio material, que es el camino para obtenerla. La designacion `S32250` no existe | **Cerrado con residuo** — el residuo no bloquea |
| OBS-03, con fecha propia | Someter el plano de puntos de medicion `PROV-DWG-UTP-001` de la fila 7.8 del ITP | Sin mencion en ninguna parte del documento | **Abierto** — no era condicion de la Rev B; se sigue en su propia fecha |
| OBS-04, aseo | Emitir el formulario en blanco | Cerrado a medias: se borraron `Report No: XESSB-XIYIN-UG230601(cth)` y `Job No: XIYIN-UG230601`. Sigue `Couplant: Wallpaper Paste`, distinto de la clausula 5.0 y de la hoja de tecnica | **Cierre parcial** |
| OBS-05, aseo | Unificar la edicion y declarar los codigos que gobiernan una medicion base de fabricacion | La edicion se unifico en `ASME Sec. V 2025` y las certificaciones del personal se re-fecharon. Siguen `ASME E 797` y los codigos de inspeccion en servicio API 510, 570 y 653 | **Cierre parcial** |
| NOTE-01, aseo | Proposito, numero de documento y Articulo 5 | Sin cambio: `DOC NO: PMI PROV-PROC-UT-001` y la clausula 1.0 sigue describiendo identificacion positiva de materiales | **No cerrado** |

**De los tres procedimientos de ensayos no destructivos, este es el que mas trabajo**: nueve cambios de contenido contra los dos del de radiografia y el uno del de penetrantes. Lo que no resolvio es justamente el bloqueante critico.

---

## Resumen de cierre

| Documento | Rev | Puntos bloqueantes del N32 | Cerrados | Aseo pedido | Hecho |
|---|---|---|---|---|---|
| HP and LP Pressure Test `-010` | 1 | 1 | 0, con la mitad incorporada | — | — |
| Painting `-011` | 1 | 1 | **1** | — | — |
| Liquid Penetrant `-014` | B | 2 | 0, una a medias | 3 | 0 |
| Radiography `-015` | B | 2 | 0, una a medias | 3 | 0 |
| Ultrasonic Thickness `-016` | B | 2 | **1**, la otra no | 3 | 2 a medias |
