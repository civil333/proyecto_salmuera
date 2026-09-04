---
titulo: "Análisis interno ENTREGA 69 (25007-0069) — Fabrication and Testing Dossier Index Rev A"
proyecto: salmuera-taltal
estado: INTERNO
second_brain: skip
date: 2026-08-04
---

# Análisis interno — ENTREGA 69 (25007-0069)

**Documento único:** `P22-BA-09-000-013` Rev A — *Fabrication and Testing Dossier Index*, 2 páginas, fechado 27-07-2026.
**Recibida:** lunes 27-Jul-2026 08:17. **Analizada:** martes 04-Ago-2026 (8 días después; la *Req. Return Date* que declara el submittal era el jueves 30-Jul-2026, ya vencida).
**Respuesta a:** primer tramo del reclamo ADASA del sábado 25-Jul-2026.

---

## 1. Fuentes leidas

| Fuente | Ruta | Uso |
|---|---|---|
| Index Rev A (el entregable) | `ENTREGAS_BWWATER/ENTREGA 69/md/P22-BA-09-000-013_A Fabrication and Testing Dossier Index__extracted.md` | Contenido revisado |
| Submittal Form 25007-0069 | `ENTREGAS_BWWATER/ENTREGA 69/md/Submittal Form_25007-0069_extracted.md` | Fecha de emisión, tipo IFA, fecha de retorno requerida |
| ITP Rev 0 (Código 1, TM N26) | `ENTREGAS_BWWATER/ENTREGA 57/md/P22-BA-09-000-004_0_ITP_extracted.md` | Matriz de registros y Hold/Witness Points; hoja de comentarios consolidada |
| NDE Plan Rev C (Código 1, TM N26) | `ENTREGAS_BWWATER/ENTREGA 61/md/P22-BA-09-000-005_C_ NDE Plan_extracted.md` | Alcance END, calificación de personal, trazabilidad de reparaciones |
| Correo del reclamo, 25-Jul | `CORREOS/Julio 2026/2026-07-25/2026-07-25_BWWater-Inspection-Dossier-Request_Descripcion.md` | Qué se pidió y en qué dos tramos |
| ET Módulo, Sección 7 y Sección 8 | `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md` (líneas 1549-1550 y 1825-1829) | Obligación del dossier y del Acta de Aprobación FAT |
| PIE Base, ítems 7.6 / 8.1 / 8.2 / 8.3 / 8.4 | `BASES TECNICAS/md/P22-IT-09-000-001-0-PIE-BASE.md` (líneas 903-910 y 975-1009) | Intervención ADASA y Hold Points |
| Master Deliverable Register | `REVISIONES/EVALUACIONES/P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx` (openpyxl, `read_only=True`, sin escritura) | Ítem 65, numeración, métricas |
| Memorias | `project_entregas_estado`, `feedback_qa_fabrication_review_calibration`, `feedback_master_register_explicit_updater` | Calibración de códigos y patrón de actualización del registro |
| Árbol de entregas | `ENTREGAS_BWWATER/` (listado de directorios) | Confirmar que E69 es la última entrega recibida |

---

## 2. Hechos nuevos

**Qué contiene realmente el Index.** Dos páginas: la primera es solo carátula (bloque de revisión Rev A / 27-07-2026, preparado MF, revisado y verificado MAZ, aprobado LHM). Toda la sustancia está en la página 2, una tabla de 27 líneas agrupadas en cinco capítulos:

| Capítulo | Líneas | Contenido enumerado |
|---|---|---|
| **A. General** | A1 | Certificate(s) of Conformance |
| **B. QA Documents** | B1-B10 | ITP; NDE Plan; Ultrasonic Examination Procedure; Dye Penetrant Test Procedure; Positive Material Identification Procedure; Radiography Testing Procedure; WPS, PQR y WPQ; Painting Procedures; Hydrostatic Test Procedures; FAT Procedure |
| **C. Quality Control Records for Each Equipment as Applicable** | C1-C11 | GA Drawings; Fabrication Drawings; P&IDs; NDE Test Report; PMI Test Report; Pressure Test / Leak Test Report; Painting / Coating Report; Visual and Dimension Inspection Records; Material Traceability Report y MTCs; Final Inspection Record; FAT Report |
| **D. Mechanical Equipment Records** | D1-D2 | Equipment List; Mechanical Equipment FAT report |
| **E. Electrical Equipment and Instruments Records** | E1-E3 | Electrical List; Electrical Equipment Certificates (paneles, cajas de conexión, cables); Instruments Calibration Certificates (transmisores, manómetros) |

**Ninguna de las 27 líneas remite a un documento con código.** La tabla tiene seis columnas y cuatro están vacías: solo se usan el identificador de línea (A1, B1, ...) y una descripción genérica. No hay columna de número de documento, de revisión, de estado de inclusión, ni de referencia cruzada a la fila del ITP que genera el registro. Esto ocurre incluso donde el documento ya existe con código ADASA y revisión aprobada: B1 es `P22-BA-09-000-004` Rev 0, B2 es `P22-BA-09-000-005` Rev C, B5 es `P22-BA-09-000-006` Rev A, B7 es `P22-BA-09-000-007` Rev A, B8 es `P22-BA-09-000-011` Rev B, B9 son `P22-BA-09-000-009` Rev C y `-010` Rev D, y B10 es `P22-PP-09-000-001` Rev A. El índice no los nombra.

**Cobertura de lo exigido para la Semana 1.** De los tres paquetes de registros pedidos el 25-Jul, el índice contempla dos y omite parcialmente el tercero:

| Pedido del 25-Jul (Semana 1) | Capítulo del Index | Veredicto de cobertura |
|---|---|---|
| MTR y trazabilidad de los spools super duplex | C9 (Material Traceability Report y MTCs); apoyo en A1 | **Cubierto** como capítulo, sin identificar el alcance super duplex |
| Calibración del equipo PMI con certificados del técnico | B5 (procedimiento) y C5 (reporte) | **Parcial** — existe el reporte PMI, pero no hay capítulo para el certificado de calibración del equipo ni para la certificación del personal. E3 cubre calibración de *instrumentos de proceso*, no de equipos de ensayo |
| WPS/PQR con calificaciones de soldadores | B7 (WPS, PQR **y WPQ**) | **Cubierto** — el WPQ es precisamente la calificación del soldador |

**Certificados de fabricación de los aceros super duplex (ET Sección 7).** La ET exige el "Dossier de fabricación y pruebas de todos los equipos eléctricos y electromecánicos con sus certificados de fabricación de aceros especiales para los equipos en superduplex". El capítulo C9 es un domicilio legítimo para esos certificados, pero el índice no declara ese alcance ni lo ata a la verificación de PREN mayor a 40 sobre UNS S32750 que pide la fila 2.1 del ITP.

**Preservación, embalaje y liberación de despacho: no están.** El índice termina en el FAT. No hay capítulo alguno para los registros de limpieza y preservación (ITP fila 8.1, PIE ítem 8.1), ni para los de embalaje y marcado con su packing list, checklist y evidencia fotográfica (ITP fila 8.2, PIE ítem 8.2, BAE Cláusula 38). Es la omisión de un capítulo completo del propio ITP aprobado de BW Water, y es justamente el capítulo cuyos registros sostienen el ítem 8.4, Liberación para Despacho.

**Falta el Acta de Aprobación FAT de ADASA.** La ET, en su Sección 8, es literal: "Tanto el protocolo de pruebas FAT generado por el Proveedor como el Acta de Aprobación FAT emitida por ADASA formarán parte integral e indispensable del dossier final de calidad del módulo". El índice prevé el procedimiento FAT (B10) y el reporte FAT (C11), pero no el Acta que emite ADASA.

**El índice revela tres procedimientos END nunca sometidos.** B3 (Ultrasonic Examination Procedure), B4 (Dye Penetrant Test Procedure) y B6 (Radiography Testing Procedure) aparecen como capítulos del dossier, pero ninguno de los tres figura en el Master Register: la serie BA entregada llega hasta `-012` y no incluye procedimientos de UT, PT ni RT. El NDE Plan Rev C, en su Sección 2.0, dice que los procedimientos de END "shall be reviewed and approved by client". La fabricación ya está soldando desde mediados de julio.

**Nada más llegó.** Al martes 04-Ago-2026, `ENTREGAS_BWWATER/` termina en ENTREGA 69: no hay E70. El tramo 2 del reclamo (dossier preliminar completo, viernes 31-Jul) venció hace cuatro días sin entrega.

**Master Register.** El ítem 65 "Manufacturing and Testing Dossier" (código "ET Sec 7, p.28", fila Excel 92, Sección 3 FABRICATION & FAT) está en `NOT DELIVERED`, con Rev / Delivery / TM / Verdict todos en "--" y acción requerida "Prerequisite for factory acceptance". El máximo número de ítem usado es **112**; hay 108 filas de ítem, con huecos históricos en 60, 61, 69 y 74. Métricas de la hoja Summary a la fecha de estado 23-Jul-2026: 108 ítems, 84 delivered, 22 not delivered, 1 partial, veredictos 50 / 28 / 6 / 0, 30 transmittales, 68 entregas.

---

## 3. Cambios respecto del 25-Jul

El primer tramo del reclamo se cumplió **a medias**: llegó el índice, no llegaron los registros. Ese matiz es el eje de la disposición — BW Water entregó el continente y no el contenido.

Cambios concretos desde el 25-Jul:

- **Aparece un documento nuevo con código propio**, `P22-BA-09-000-013`, primero de la serie BA desde el O&M Manual `-012`. Es la primera vez que BW Water formaliza por escrito la estructura que propone para el dossier; hasta ahora el contenido esperado se apoyaba en la lámina de la Quality Kick-off Meeting.
- **Ningún registro de la Semana 1 fue entregado.** No llegaron MTR ni trazabilidad de spools, ni el certificado de calibración del equipo PMI, ni los certificados del técnico, ni las calificaciones de soldadores. La inspección de Bureau Veritas del martes 28-Jul (PMI super duplex) se ejecutó, si se ejecutó, sin que ADASA tuviera esos registros.
- **El tramo 2 venció sin entrega.** El dossier preliminar completo del viernes 31-Jul no llegó y hoy acumula cuatro días de atraso.
- **Sigue sin responderse la pregunta sobre FEDCO.** El correo del 25-Jul pidió confirmar que los registros de las pruebas FEDCO se incorporan al dossier; el índice no tiene capítulo para registros de ensayo de equipos principales de sub-proveedor, de modo que la pregunta queda contestada de facto en sentido negativo.
- **Se descubre un frente nuevo:** los procedimientos de UT, PT y RT que el propio índice enumera nunca se sometieron a aprobación.
- **El ítem 65 del Master Register no se mueve.** El índice no es el dossier; el entregable de la ET Sección 7 sigue sin entregar.

---

## 4. Compromisos y fechas

| Compromiso | Obligado | Fecha comprometida | Origen de la fecha | Fuente contractual | Estado | Criterio de cierre | Evidencia |
|---|---|---|---|---|---|---|---|
| Índice del dossier de fabricación y pruebas | BW Water | Lun 27-Jul-2026 | Correo ADASA 25-Jul, tramo 1 | ET Sección 7; PIE ítem 7.6 | **CUMPLIDO en forma, deficiente en fondo** | Índice recibido y aprobado por ADASA | E69, `P22-BA-09-000-013` Rev A (27-Jul 08:17) |
| Registros Semana 1: MTR y trazabilidad de spools super duplex | BW Water | Lun 27-Jul-2026 | Correo ADASA 25-Jul, tramo 1 | ET Sección 7; ITP fila 2.1 | **INCUMPLIDO** | Recepción de los MTR con PREN mayor a 40 sobre UNS S32750 | Ninguna; E69 no trae registros |
| Registros Semana 1: calibración del equipo PMI y certificados del técnico | BW Water | Lun 27-Jul-2026 | Correo ADASA 25-Jul, tramo 1 | ITP fila 2.4; NDE Plan Sección 3.0 | **INCUMPLIDO** | Certificado de calibración vigente y certificación del personal | Ninguna |
| Registros Semana 1: WPS/PQR y calificación de soldadores de juntas ya soldadas | BW Water | Lun 27-Jul-2026 | Correo ADASA 25-Jul, tramo 1 | ITP fila 3.1 (ASME IX) | **INCUMPLIDO** | WPQ vigentes de los soldadores que ejecutaron las juntas de julio | Ninguna |
| Dossier preliminar completo, estructurado contra el índice | BW Water | Vie 31-Jul-2026 | Correo ADASA 25-Jul, tramo 2 | ET Sección 7; PIE ítem 7.6 | **VENCIDO SIN ENTREGA** (4 días al 04-Ago) | Dossier revisable contra el índice aprobado | `ENTREGAS_BWWATER/` termina en E69 |
| Dossier de fabricación y pruebas (entregable contractual) | BW Water | 90 días desde la adjudicación | ET Sección 7 | ET Sección 7, p.28 | **VENCIDO** | Ítem 65 del Master Register pasa a Delivered | Master Register ítem 65 = NOT DELIVERED |
| Confirmar que los registros de las pruebas FEDCO se incorporan al dossier | BW Water | Con el índice (27-Jul) | Correo ADASA 25-Jul, punto 1 | ITP fila 2.3 | **NO RESPONDIDO** | Capítulo explícito en el índice o confirmación escrita | El índice no tiene capítulo de certificados de equipos principales |
| Reemitir a Bureau Veritas las revisiones limpias vigentes (ITP Rev 0, no Rev C) | BW Water | Antes del Mar 28-Jul-2026 | Correo ADASA 25-Jul, punto 2 | — | **SIN VERIFICAR** | Acuse de BV con el paquete correcto | Fuera del alcance de esta revisión |
| Notificar jornadas 2 y 3 de la Semana 1 con su alcance | BW Water | Antes del Mar 28-Jul-2026 | Correo ADASA 25-Jul, punto 3 | BAE Cláusula 37 (30 días de aviso) | **SIN VERIFICAR** | Notificación escrita con alcance por jornada | Fuera del alcance de esta revisión |
| Respuesta escrita a la reconciliación (V5/V6, FAT, Dispatch Release, Kick-off) | BW Water | Mar 28-Jul-2026, reunión semanal | Correo ADASA 25-Jul, punto 4 | — | **SIN VERIFICAR** | Respuesta escrita punto por punto | Fuera del alcance de esta revisión |
| Calificación de soldadores (WQT) | BW Water | Vie 07-Ago-2026 | Respuesta de BW Water a Bureau Veritas | ITP fila 3.1 | **PENDIENTE (futuro)** | Ejecución testificada y registro en el dossier | Hilo BV-BW, 23-24 de julio |
| Confirmar a Bureau Veritas las visitas V2 a V6 | **ADASA** | Vie 24-Jul-2026 | Compromiso propio de ADASA | — | **VENCIDO (propio)** | Correo de confirmación a BV | Condicionado a la respuesta de reconciliación de BW Water |
| Devolver el submittal 25007-0069 revisado | **ADASA** | Jue 30-Jul-2026 | *Req. Return Date* del propio Submittal Form | — | **VENCIDO (propio)**, 5 días | Emisión del transmittal con el veredicto | Submittal Form 25007-0069 |

---

## 5. Discrepancias entre documentos

1. **El índice no declara cuál de los dos índices del ITP es.** El ITP Rev 0 prevé dos: el preliminar de la fila 7.6 (referencia `PROV-LIST-DOSS-PRE-001`, intervención ADASA = R, revisión documental antes del FAT) y el final de la fila 8.3 (referencia `PROV-LIST-DOSS-FIN-001`, Hold Point de BW Water y de ADASA). El documento se titula solo "Fabrication and Testing Dossier Index" y no referencia ninguno de los dos. Sin esa declaración no se sabe si lo que ADASA está revisando cumple el ítem 7.6 o pretende cumplir el 8.3.

2. **Índice contra ITP Rev 0, capítulo 8 completo.** Las filas 8.1 (Inspection, Cleaning and Preservation) y 8.2 (Inspection, Packaging and Marking) generan reportes, checklists y evidencia fotográfica que ADASA testifica como Witness Point. El índice no tiene dónde alojarlos. Es la discrepancia más grave porque el ítem 8.4, Liberación para Despacho, se apoya en esos registros y es el que sostiene el 40% del pago.

3. **Índice contra ET Sección 8.** La ET declara el Acta de Aprobación FAT emitida por ADASA parte "integral e indispensable" del dossier final. El índice prevé B10 (procedimiento FAT) y C11 (reporte FAT) y omite el Acta.

4. **Índice contra NDE Plan Rev C, Sección 3.0.** El propio plan de BW Water obliga a que los técnicos de END tengan certificación vigente y a que los documentos de certificación se entreguen al cliente antes del inicio de los trabajos. No hay capítulo de calificaciones de personal de inspección.

5. **Índice contra ITP fila 2.4.** La fila lista como registro el "PMI equipment calibration cert". El índice tiene C5 (PMI Test Report) y ningún domicilio para el certificado de calibración del equipo. E3 se refiere a instrumentos de proceso (transmisores, manómetros), no a equipos de ensayo.

6. **Índice contra ITP fila 2.3.** La fila exige verificar certificados de fabricante de los equipos principales (bombas, turbos, motores, VFDs, PLCs, instrumentos). En el índice, D2 es solo un reporte FAT de equipos mecánicos y E2 son certificados eléctricos: los registros de ensayo de sub-proveedor, entre ellos los de FEDCO, no tienen capítulo declarado.

7. **Índice contra ITP fila 2.2 y el waiver ASME.** El ensayo hidrostático del RO Vessel (ASME Sección X sin estampa, 1.800 psi por 1,1) fue elevado a Hold Point en la hoja de comentarios del ITP Rev 0. El índice no nombra el paquete documental del vessel; quedaría repartido de facto entre A1 y C6 sin decirlo.

8. **Índice contra el Master Register.** B3, B4 y B6 enumeran procedimientos de UT, PT y RT que nunca se sometieron a ADASA, pese a que el NDE Plan Rev C exige que los procedimientos de END sean revisados y aprobados por el cliente y a que su matriz obliga a PT 100% en pase de raíz y de terminación, RT 10% en soldaduras a tope y medición UT de espesores.

9. **Índice contra ITP filas 4.1 a 4.4 y 6.3.** Los checklists de montaje de equipos, alineamiento y soportación de cañerías, montaje de instrumentos y válvulas, y la verificación de cableado interno no tienen capítulo propio; el C10 (Final Inspection Record) podría absorberlos, pero eso hay que declararlo.

10. **Índice contra ITP fila 7.7.** La verificación de cumplimiento de la normativa eléctrica chilena (SEC) es Hold Point y su registro son certificados o declaraciones. Sin capítulo explícito.

---

## 6. Riesgos y exposición contractual

**El índice, tal como está, no habilita la revisión documental que le corresponde a ADASA.** El ítem 7.6 del PIE asigna a ADASA una revisión (R) del dossier preliminar y exige levantar una "Lista Chequeo Dossier Preliminar". Un listado de 27 descripciones genéricas sin códigos, sin revisiones y sin estado de inclusión no se puede chequear: no permite distinguir lo que está de lo que falta. Si ADASA acepta este índice como base, pierde el instrumento de control del ítem 7.6 y llega al FAT sin una lista contra la cual verificar.

**La cadena 7.6 - 8.3 - 8.4 sostiene el 40% del pago.** El índice omite justamente los capítulos que alimentan el 8.4. Aprobarlo con esa omisión deja abierta la discusión de si el dossier estaba completo al momento de solicitar la liberación de despacho, y esa discusión se daría con la fabricación terminada y el módulo listo para embarcar, que es el peor momento posible para ADASA.

**Se están generando registros sin domicilio aprobado.** La soldadura arrancó a mediados de julio y la ventana de inspección de Bureau Veritas abrió el martes 28-Jul. Cada día que pasa se producen MTR, reportes de PMI y registros de soldadura que se acumulan sin un índice aprobado que los ordene. Si el dossier preliminar completo se arma contra la estructura de la Rev A, habrá retrabajo cuando se incorporen los capítulos faltantes.

**Ensayos bajo procedimientos no aprobados.** El riesgo más concreto: si se ejecutan ensayos de UT, PT o RT antes de que ADASA apruebe los procedimientos correspondientes, sus registros son impugnables y el NDE Plan Rev C respalda esa impugnación. Conviene levantar este punto de inmediato y por separado, sin esperar al ciclo del transmittal.

**Exposición propia de ADASA.** Dos plazos vencidos del lado de ADASA debilitan el reclamo: la fecha de retorno del submittal (jueves 30-Jul, hoy con 5 días de atraso) y la confirmación a Bureau Veritas de las visitas V2 a V6 (viernes 24-Jul). El segundo está condicionado a una respuesta de BW Water que no llegó, y conviene dejarlo dicho por escrito; el primero es atribuible solo a ADASA y aconseja emitir el veredicto sin más demora.

**Riesgo de que el índice se lea como cumplimiento.** Si el veredicto no distingue con claridad entre el índice y el dossier, BW Water puede sostener que el reclamo del 25-Jul quedó atendido. El transmittal debe decir de forma expresa que el entregable de la ET Sección 7 sigue sin entregar y que el ítem 65 del registro no se mueve.

---

## 7. Verificado vs NO verificado

**Verificado con fuente primaria leída en esta sesión:**

- Contenido íntegro del Index Rev A: 2 páginas, 27 líneas, 5 capítulos, sin columna de código, revisión ni estado. Leído del `.md` extraído.
- Contenido del ITP Rev 0: las 12 secciones, filas 1.1 a 12.3, con sus registros y la asignación H / W / SW / R para ADASA, más las dos entradas de la hoja de comentarios consolidada (waiver sin estampa y elevación de la fila 2.2 a Hold Point).
- Contenido del NDE Plan Rev C: Sección 2.0 (procedimientos a aprobar por el cliente), Sección 3.0 (calificación de personal), matriz VT/PT/UT/RT/PMI y Sección 9.0 (identificación de reparaciones R1, R2, RW).
- Texto literal de la ET: dossier con certificados de aceros super duplex (líneas 1549-1550) y Acta de Aprobación FAT como parte integral del dossier final (líneas 1825-1829).
- Texto de la PIE Base: ítems 7.6, 8.1, 8.2, 8.3 y 8.4 con su intervención ADASA.
- Master Register leído en modo solo lectura: ítem 65 completo, máximo ítem 112, 108 filas de ítem, huecos en 60, 61, 69 y 74, y métricas de la hoja Summary.
- E69 es la última entrega recibida: el árbol `ENTREGAS_BWWATER/` no contiene E70.
- Días de la semana, comprobados con `date`: 24-Jul viernes, 25-Jul sábado, 27-Jul lunes, 28-Jul martes, 30-Jul jueves, 31-Jul viernes, 04-Ago martes, 07-Ago viernes.
- No existe carpeta de transmittal N31; el último es `P22-TM-09-000-030-0`.

**NO verificado — no afirmar como hecho:**

- **El PDF del Index no fue abierto** (regla dura del proyecto). Todo lo anterior proviene del `.md` extraído; el layout, las firmas gráficas y cualquier anotación o sello del PDF no están comprobados.
- Si BW Water envió registros de la Semana 1 **por correo, fuera del sistema de submittals**. Solo se revisó el árbol de entregas.
- Si se reemitieron a Bureau Veritas las revisiones limpias vigentes antes del 28-Jul.
- Si la inspección del martes 28-Jul (PMI super duplex) se ejecutó y qué registros produjo.
- Si la reunión semanal del 28-Jul se realizó y qué se respondió sobre V5/V6, FAT y Dispatch Release.
- Si existen físicamente los registros de ensayo de FEDCO.
- Si los procedimientos de UT, PT y RT existen en BW Water sin haber sido sometidos, o no existen. Solo consta que **no fueron entregados a ADASA**.
- La lámina de la Quality Kick-off Meeting (`DOCUMENTOS A ENVIA A BV.png`) no se abrió en esta sesión; su contenido se toma del resumen del correo del 25-Jul.
- El estado real del avance de fabricación y cuántas juntas se soldaron desde mediados de julio.

---

## 8. Entradas de Bitacora propuestas

### 2026-07-27 — ENTREGA 69 (25007-0069): Fabrication and Testing Dossier Index Rev A — RECIBIDO

> Recibida el lunes 27-Jul-2026 08:17 con un único documento: `P22-BA-09-000-013` Rev A, *Fabrication and Testing Dossier Index*, 2 páginas, emitido IFA con fecha de retorno requerida el jueves 30-Jul-2026. Es la respuesta al primer tramo del reclamo del sábado 25-Jul (índice del dossier más registros de la Semana 1). Llegó el índice; **no llegó ningún registro**. Entregas recibidas E1-E69.

### 2026-08-04 — Revisión de la E69: el índice llega, el dossier no — Código 3 propuesto — INTERNO

> Revisión del Index Rev A contra el ITP `P22-BA-09-000-004` Rev 0, el NDE Plan `P22-BA-09-000-005` Rev C, la ET Sección 7 y Sección 8 y la PIE Base. Veredicto propuesto **3 — To be revised (reemitir como Rev B)**: el índice enumera 27 capítulos sin un solo código de documento, revisión ni estado, y omite el capítulo 8 completo del propio ITP (preservación, embalaje y marcado), el Acta de Aprobación FAT que la ET declara parte integral del dossier final, las certificaciones del personal de END que exige el NDE Plan, el certificado de calibración del equipo PMI y los certificados de fabricante de los equipos principales. 6 OBS y 4 NOTE al PDF anotado. Hallazgo colateral: los capítulos B3, B4 y B6 enumeran procedimientos de UT, PT y RT que nunca se sometieron a aprobación de ADASA pese a que el NDE Plan lo exige, con la fabricación soldando desde mediados de julio.
>
> **El índice no es el dossier.** El ítem 65 del Master Register, "Manufacturing and Testing Dossier", se mantiene en `NOT DELIVERED`: el entregable de la ET Sección 7 sigue pendiente. Se abre ítem nuevo **113** para `P22-BA-09-000-013`. El tramo 2 del reclamo del 25-Jul (dossier preliminar completo, viernes 31-Jul) **venció sin entrega**; al martes 04-Ago la última entrega recibida sigue siendo la E69. Vencido también del lado de ADASA: la fecha de retorno del submittal (jueves 30-Jul, 5 días) y la confirmación a Bureau Veritas de las visitas V2 a V6 (viernes 24-Jul, condicionada a una respuesta de BW Water que no llegó).

---

## 9. Sugerencias a memorias

| Memoria | Acción | Contenido |
|---|---|---|
| `project_entregas_estado` | **Actualizar** | Bloque nuevo 04-Ago-2026: E69 recibida el 27-Jul con el Dossier Index Rev A; entregas E1-E69; el índice no cierra el ítem 65; TM N31 pendiente de abrir |
| `feedback_qa_fabrication_review_calibration` | **Ampliar** | Regla nueva de calibración: *un índice de dossier sin códigos de documento, revisión ni estado, y que omite capítulos completos del ITP aprobado, es Código 3* — no soporta la revisión documental que el ítem 7.6 del PIE asigna a ADASA. Es la misma lógica ya validada para procedimientos de ensayo sin su presión vinculante: el documento enuncia la estructura genérica y omite el dato de proyecto que lo hace ejecutable o revisable |
| Memoria nueva sugerida: `feedback_indice_no_es_el_entregable` | **Crear** | El índice de un dossier no cierra el ítem del dossier en el Master Register. Patrón híbrido: ítem nuevo para el índice con su código y veredicto, ítem del entregable de la ET intacto en `NOT DELIVERED` con la acción requerida reescrita para citar que el índice llegó y el dossier no. Evita que la entrega de un continente se lea como cumplimiento del contenido |
| `project_bureau_veritas_inspection` | **Actualizar** | Tramo 1 del reclamo cumplido solo en forma (índice sí, registros no); tramo 2 del 31-Jul vencido sin entrega; frente nuevo abierto: procedimientos de UT, PT y RT nunca sometidos mientras la fabricación suelda |
| `transmittals` | **Actualizar al emitir** | Reservar N31 para la E69; hoy el índice llega hasta N30 (BORRADOR 23-Jul) |
| `feedback_master_register_explicit_updater` | **Anotar** | Confirmado en esta pasada: las filas nuevas se apilan físicamente bajo el último encabezado de sección (filas 106-114 están bajo "5. RECEPCIÓN PROVISIONAL" siendo documentos BA, CD y DWG). `ITEMS BY SECTION` sigue sin poder recomputarse desde la hoja |

---

## 10. Veredicto propuesto y disposicion

### Código propuesto

**Código 3 — To be revised. Reemitir como Rev B.**

**Justificación en una frase:** el índice omite un capítulo completo de su propio ITP aprobado (preparación para el despacho: preservación, embalaje y marcado, cuyos registros sostienen la liberación de despacho y el 40% del pago) y el Acta de Aprobación FAT que la ET declara parte integral del dossier final, y enumera sus 27 capítulos sin un solo código de documento, revisión ni estado de inclusión, de modo que no puede servir de lista de chequeo para la revisión documental preliminar que el ítem 7.6 del PIE asigna a ADASA.

**Por qué Código 3 y no Código 2.** El criterio determinante es si el documento debe cambiar para llegar a Rev 0, y aquí la respuesta no solo es sí, sino que el cambio es estructural: hay que agregar capítulos que no existen y tres columnas que no existen. Un Código 2 mandaría el documento directo a Rev 0 sin que ADASA vea el resultado, y este índice es precisamente el instrumento de control con el que ADASA verificará el dossier antes del FAT y antes de liberar el despacho. ADASA necesita ver la Rev B antes de la Rev 0. Se suma que la Rev A es una primera emisión, donde el Código 3 no tiene ningún costo procesal.

**Distinción que el transmittal debe hacer explícita:** este veredicto califica **el Index como documento**. El **dossier como entregable de la ET Sección 7** no ha sido entregado y no se ve afectado por este código: sigue vencido, sigue en `NOT DELIVERED` y sigue siendo prerrequisito de los ítems 8.3 y 8.4.

### Observaciones para el PDF anotado (`P22-BA-09-000-013_A ..._CC_ADASA.pdf`)

| ID | Severidad | Texto de la instrucción (inglés, se emite a BW Water) |
|---|---|---|
| **OBS-01** | MAYOR | **Correct:** add to every line of the index the project document number, its current revision and its inclusion status (included / pending / not applicable), and cross-reference each chapter to the row of the Inspection and Test Plan (P22-BA-09-000-004) that generates the record. As issued, the index lists 27 generic descriptions with no traceability, including for documents that already carry an approved ADASA code and revision, so it cannot serve as the checklist for the preliminary documentation review that the Inspection and Testing Base Plan (P22-IT-09-000-001-0) assigns to ADASA at item 7.6. |
| **OBS-02** | MAYOR | **Correct:** add a dossier chapter for preparation for dispatch, covering the cleaning and preservation records, the packaging and marking records with their checklists and photographic evidence, and the packing list, as required by the Inspection and Test Plan (P22-BA-09-000-004), rows 8.1 and 8.2, and by the Technical Specification (P22-ET-09-000-001-0), Section 7. The index as issued ends at the factory acceptance test and omits the records that support the release for dispatch at row 8.4. |
| **OBS-03** | MAYOR | **Correct:** add a chapter for the FAT Approval Certificate issued by ADASA. The Technical Specification (P22-ET-09-000-001-0), Section 8, states that both the supplier's FAT test protocol and the FAT Approval Certificate issued by ADASA form an integral and indispensable part of the final quality dossier of the module. The index currently provides for the FAT procedure and the FAT report only. |
| **OBS-04** | MAYOR | **Correct:** add a chapter for inspection and testing personnel qualifications and for test equipment calibration, covering the certification documents of the non-destructive examination technicians and the calibration certificate of the PMI equipment. The NDE Plan (P22-BA-09-000-005), Section 3.0 - Personal Qualifications, requires the personnel certification documents to be submitted to the client prior to work commencement, and the Inspection and Test Plan (P22-BA-09-000-004), row 2.4, lists the PMI equipment calibration certificate as a required record. Chapter E3 covers process instrument calibration and does not cover inspection equipment. |
| **OBS-05** | MAYOR | **Correct:** add a chapter for the manufacturer certificates and factory test records of the main equipment, covering pumps, turbochargers, motors, variable frequency drives, the programmable logic controller and instruments, as required by the Inspection and Test Plan (P22-BA-09-000-004), row 2.3. Chapter D2 provides only for a mechanical equipment factory acceptance test report and chapter E2 only for electrical equipment certificates, so the sub-vendor test records have no declared location in the dossier. |
| **OBS-06** | MENOR | **Correct:** state in which chapter the reverse osmosis pressure vessel documentation package is filed, namely the manufacturer certification to ASME Section X without code stamp and the hydrostatic test report at 1,800 psi x 1.1. The Inspection and Test Plan (P22-BA-09-000-004), row 2.2, holds that test as a hold point requiring ADASA attendance and written approval. |
| **NOTE-01** | NOTA | **Note:** the Inspection and Test Plan (P22-BA-09-000-004) provides for two separate indices, a preliminary dossier index at row 7.6 which ADASA reviews before the factory acceptance test, and a final dossier index at row 8.3 which is a hold point for both BW Water and ADASA. State on the cover sheet which of the two this document is, and keep the same chapter numbering in both so that the final dossier can be verified against the preliminary one. |
| **NOTE-02** | NOTA | **Note:** the index has no chapter for non-conformance reports and weld repair records. The NDE Plan (P22-BA-09-000-005), Section 9.0 - Report, requires repairs to be identified as R1, R2 and RW on the examination reports, and the Inspection and Test Plan (P22-BA-09-000-004), row 7.9, makes the closure of factory acceptance test non-conformances a condition for the issuance of the ADASA approval certificate. A non-conformance register with its close-out evidence is expected in the dossier. |
| **NOTE-03** | NOTA | **Note:** chapters B3 - Ultrasonic Examination Procedure, B4 - Dye Penetrant Test Procedure and B6 - Radiography Testing Procedure are listed in this index, but none of the three procedures has been submitted to ADASA for review. The NDE Plan (P22-BA-09-000-005), Section 2.0 - Scope, states that the non-destructive testing procedures shall be reviewed and approved by the client, and its examination matrix requires 100% penetrant testing on root and end passes, 10% radiography on butt welds and ultrasonic thickness measurement. Submit the three procedures for review; records produced under procedures not yet approved by ADASA cannot be accepted into the dossier. |
| **NOTE-04** | NOTA | **Note:** chapter C9 - Material Traceability Report and Material Test Certificates is understood to be the location for the mill certificates of the super duplex material. The Technical Specification (P22-ET-09-000-001-0), Section 7, requires the dossier to carry the manufacturing certificates of the special steels for the super duplex equipment, and the Inspection and Test Plan (P22-BA-09-000-004), row 2.1, requires verification of PREN above 40 for UNS S32750. Identify that scope explicitly in chapter C9, spool by spool. |

Total: **6 OBS + 4 NOTE = 10 anotaciones.** Consistente con la regla del proyecto: un Código 3 se anota completo.

### Estado propuesto del Master Register

**Opción adoptada: híbrida.** Ítem nuevo para el índice, ítem del dossier intacto. Verificada contra el registro y **sin obstáculos**.

**a) Ítem nuevo 113** — el número está libre: el máximo en uso es **112**, sin duplicados. Los huecos históricos en 60, 61, 69 y 74 existen pero **no deben reutilizarse** (rompería la trazabilidad de ítems retirados).

| Campo | Valor propuesto |
|---|---|
| # | 113 |
| Document | Fabrication and Testing Dossier Index |
| Code / ET Reference | P22-BA-09-000-013 |
| Rev | A |
| Delivery | E69 |
| TM | N31 |
| Verdict | 3-To be revised |
| Status | Delivered |
| Action Required | Re-issue as Rev B. Index lists 27 chapters with no document code, revision or inclusion status, and omits ITP Section 8 (preservation, packaging and marking), the ADASA FAT Approval Certificate required by ET Section 8, NDE personnel certifications, the PMI equipment calibration certificate and the main equipment manufacturer certificates. Chapters B3, B4 and B6 list UT, PT and RT procedures never submitted for ADASA approval — tracked separately. |
| ET Deadline | ET Sec.7; PIE item 7.6 (preliminary dossier review before FAT) |

**b) Ítem 65 — se mantiene `NOT DELIVERED`.** Rev, Delivery, TM y Verdict siguen en "--". Solo se reescribe `Action Required`:

> *Prerequisite for factory acceptance. Dossier INDEX received in E69 (P22-BA-09-000-013 Rev A, 27-Jul-2026 — tracked as item 113, Code 3); the dossier itself remains undelivered. Week-1 records demanded on 25-Jul-2026 (super duplex MTR and traceability, PMI equipment calibration and technician certificates, WPS/PQR and welder qualifications) not received. Complete preliminary dossier due Fri 31-Jul-2026 not received as of 04-Aug-2026. Gates PIE items 7.6, 8.3 and 8.4 (Release for Dispatch, 40% payment milestone).*

**c) Impacto en la hoja Summary** (recomputar desde la hoja Master Register, según el patrón del updater explícito por TM):

| Métrica | Antes (a N30) | Después (a N31) |
|---|---|---|
| Total Items | 108 | 109 |
| Delivered | 84 | 85 |
| Not Delivered | 22 | 22 (sin cambio: el ítem 65 no se mueve) |
| Verdict 1-Approved | 50 | 50 |
| Verdict 2-AN | 28 | 28 |
| Verdict 3-To be revised | 6 | **7** |
| Verdict 4-Rejected | 0 | 0 |
| Transmittals Issued | 30 | 31 |
| Deliveries Received | 68 (E1-E68) | 69 (E1-E69) |
| Latest Delivery Date | 23-Jul-2026 (E68) | 27-Jul-2026 (E69) |
| Status Date | 23-Jul-2026 | fecha de emisión del TM N31 |

**d) Obstáculos y cautelas verificadas:**

- **Ninguno bloqueante.** El número 113 está libre y el código `P22-BA-09-000-013` no existe en el registro (la serie BA llega hasta `-012`, ítem 111).
- **Ubicación física de la fila.** El ítem 65 vive en la fila Excel 92, bajo el encabezado "3. FABRICATION & FAT", que es donde el ítem 113 pertenece por materia. Pero la práctica del registro es apilar los ítems nuevos al final de la hoja: las filas 106 a 114 (ítems 104 a 112, entre ellos documentos BA, CD, DWG y LI) están físicamente bajo el encabezado "5. RECEPCIÓN PROVISIONAL". Agregar el 113 en la fila 115 mantiene esa práctica, pero deja el ítem fuera de su sección visual.
- **Consecuencia:** `ITEMS BY SECTION` debe ajustarse **a mano** (Sección 3: total 11 a 12, delivered 8 a 9), no recomputarse desde la hoja. Es la limitación ya conocida del registro, no un defecto nuevo.
- **Respaldar antes de escribir:** copiar a `*_pre-N31.xlsx` antes de correr el updater, y restaurar desde el backup si hay que re-ejecutar.
- **`REVIEW CYCLES DISTRIBUTION`:** el ítem 113 entra como 1 cycle. También se edita a mano.
- Esta sesión **no modificó el archivo**: se abrió con `read_only=True`.
