---
titulo: "Puntos de revisión para la reunión de coordinación del 9 de septiembre"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-09-08
---

# Puntos de revisión para la reunión del miércoles 9 de septiembre

**Estado: ENVIADO** el martes 8 de septiembre de 2026, dentro de la ventana que importaba: antes de las 21:00 de Chile, que son las 09:00 del miércoles en Penang, cuando abre la primera jornada de ensayos. **Falta archivar el respaldo del enviado en esta carpeta, y con él la hora exacta.**

| Campo | Valor |
|---|---|
| Archivo | `2026-09-08_Puntos-Revision-Reunion-09Sep.docx` · inglés · 566 palabras de prosa más una tabla de cuatro filas |
| Para | Eduardo Yamauchi (BW Water) |
| CC | Stephane Gehant, Lokman Hakim Bin Mat, Jeryl F. Regulacion, Sadeep Irugalbandara, Nick Huta, Magdier Arias (BW Water); Víctor Gutiérrez, Jorge Guevara (ADASA) |
| Asunto | RE: 25007 Taltal: Project updates - 08-Sep-2026 - review points for the coordination meeting of 9 September |
| Cadena | **Reply-All al correo de Eduardo Yamauchi del martes 8-Sep 12:41**, que transmitió el paquete semanal. Cadena separada de la de transmittals y de la de Bureau Veritas |
| Adjuntos | Ninguno |
| Script | `crear_correo_puntos_revision_09sep.py` |

## Por qué sale hoy y no mañana

La reunión semanal no se hizo el martes y quedó para el miércoles. Pero el `Request to witness inspection 007` abre la primera de tres jornadas de ensayo el **miércoles 9 a las 09:00 de Penang**, que en Chile es la noche del martes. Los tres defectos del plan de ensayos se corrigen antes de esa hora o el Día 1 se ejecuta con dos rótulos de línea equivocados en el registro de calidad. Por eso el correo separa lo urgente de lo que se ve en la reunión, y lo dice en la segunda frase.

## Qué dice

**Formato ejecutivo en la estructura, voz propia en la sintaxis.** La acción incómoda abre el correo, lo enumerable va en una tabla compacta y cada frente de la reunión lleva un rótulo y dos o tres oraciones. La oración queda en 19,4 palabras de media, que es la calibración del autor en inglés, con primera persona y no impersonal. La versión del mediodía tenía 11,4 y había perdido la voz por acortar.

**Apertura, dos frases.** Acuse del paquete Week 36 y las dos cosas que se responden antes de que abra la jornada del miércoles en Penang: la pregunta de los planos y las cuatro correcciones de la tabla.

**Los planos de taller, arriba y en negrita.** Un solo asunto y una sola petición, en 83 palabras. No tenemos los planos de detalle de los carretes y hay que emitirlos. Y **Bureau Veritas tiene que tenerlos en cada una de las tres jornadas**, para contrastar cada carrete contra su propio plano antes de presurizarlo. Cita los once `25007-ME-PI-0901-0006` a `-0016`, devueltos como no recibidos en el TM N30. Y los seis `-0023` a `-0028`, que nunca se sometieron. **La versión anterior se descartó entera.** Estaba armada alrededor del historial documental, mezclaba dos hallazgos técnicos con una queja de control documental, y no se entendía qué se alertaba.

**Una frase por el `CP-SSD-DN80-09-044`**, después de la tabla: fue rechazado el 21 de agosto en las juntas 03 y 04, el reensayo del 3 de septiembre cubrió las juntas 01 y 02, y el plan da el carrete por terminado. Se pide confirmar si las juntas rechazadas se reensayaron.

**Las presiones, y va delante de la tabla a propósito.** El párrafo declara tres cosas. Las diecisiete presiones están zanjadas por la Line List Rev 1 en Código 1. El Testing Plan es la confirmación escrita que exigió el TM N35, y por eso la retención sobre el circuito de super dúplex queda levantada. Cierra diciendo que las cuatro filas de la tabla son correcciones de registro y que ninguna cambia una presión. **Si la tabla abriera, el correo se leería como que las presiones están en cuestión**, y no lo están.

**Tabla de cuatro filas**, columnas Testing Plan, Approved Line List y Action: el ítem 9 por el diámetro, el ítem 16 por el material, la línea `09-050` que no tiene día de ensayo, y la cobertura de carretes del ítem 14.

**El Pressure Test Record Chart**, en un párrafo sin rótulo en negrita para no pasar el umbral de CL-24: sigue sin número ni revisión. Es el formulario del certificado de presión contra tiempo que exigen las filas 5.1 y 5.2 del ITP, y el TM N35 ya lo pidió el 20 de agosto. Mañana empiezan tres jornadas de registros sobre él.

**Tres frentes para la reunión**, un rótulo cada uno: Factory Acceptance Test, Assembly and equipment, Schedule and shipment.

**Cierre:** "We look forward to your comments", sin proponer reunión.

## Verificación de fuentes

| Afirmación del correo | Fuente |
|---|---|
| El ítem 9 del plan rotula `DA-SSD-DN100-09-005` y la línea es `DA-SSD-DN80-09-005`, ensayo 120 barG | `Testing Plan.pdf` del `Request to witness inspection 007`, ítem 9; Line List `P22-LI-09-009-003` Rev 0 (`ENTREGA 67`) y Rev 1 (`ENTREGA 90`), ambas DN80, diseño 80 barG, hidrostática 120 |
| El informe del 3 de septiembre también la rotula DN80 | `BVM-IR011-03092026`, sección E1: `DA-SSD-DN80-09-005 (Jt 35,36,37,38)` y `CP-SSD-DN80-09-044 (Jt 01,02)`, 120 barG aplicados, 30 minutos, satisfactorio |
| El ítem 16 rotula `DA-SSD-DN65-09-016` y la Line List la declara `DA-PVC-DN65-09-016`, PVC SCH80 | Testing Plan ítem 16; Line List Rev 1, fila `DA-PVC-DN65-09-016`, PVC SCH80, diseño 2 barG, hidrostática 3. **La presión de 3 barG del plan coincide y la línea está identificada**, de modo que la acción es corregir el material del rótulo y no declarar qué línea se ensaya |
| `DA-SSD-DN100-09-050` está en la Rev 1 y no en el plan | Line List Rev 1: `DA-SSD-DN100-09-050`, succión de la bomba de alta, super dúplex SCH80S, diseño 5 barG, hidrostática 7,5. El Testing Plan tiene 17 ítems y esta línea no aparece en ninguno |
| Son diecisiete las líneas de super dúplex | Conteo de TAG `*-SSD-*` únicos en la Line List Rev 1: diecisiete |
| El plan adopta los diámetros que ADASA declaró en el Transmittal N38 | Testing Plan ítems 5 y 7: `CP-SSD-DN80-09-047` y `CP-SSD-DN80-09-049`; ítem 11: `CP-SSD-DN65-09-048`. El `P22-TM-09-000-038-0`, Sección 2.5, declara vinculantes `CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`; la Line List Rev 1 los trae invertidos |
| Cinco de las seis líneas nuevas de baja presión se ensayan a la presión de su propia Rev 1 | La Rev 1 agrega seis TAG de super dúplex sobre los once de la Rev 0: `09-047`, `09-048`, `09-049`, `09-050`, `09-051` y `09-052`. El Testing Plan cubre cinco a 7,5 y 3 barG, que son las presiones de la Rev 1. **La sexta es `09-050`, la que falta en el plan**, de modo que el correo reconoce lo cubierto sin decir seis |
| `CP-SSD-DN65-09-045` retenida desde el 20 de agosto, programada el viernes a 135 barG | Correo ADASA del 31-Ago (`CORREOS/Agosto 2026/2026-08-31/`); Testing Plan ítem 10, `Spool 1 - 11/9/2026`; Line List Rev 1, diseño 90 barG, hidrostática 135 |
| La aprobación del procedimiento FAT es Punto de Detención de la fila 7.1 | ITP `P22-BA-09-000-004` Rev 0, aprobado en Código 1 en el Transmittal N26, fila 7.1, columna C con **H**. ⚠️ **No se cita el `P22-TM-09-000-017-0`**: su enumeración de nueve Hold Points corresponde a la **Rev A** y omite la fila 5.2, de modo que quedó superada por la Rev 0, que lleva catorce |
| El procedimiento de FAT del módulo no se ha sometido | `P22-TM-09-000-038-0`, Sección 3: la fila *"Factory Acceptance Test procedure of the module, required by Section 8.1 of the Technical Specification"* con estado *"Not received"*. En el repositorio solo existe el del tablero, `P22-PP-09-000-001` Rev A, B y C |
| La ET exige el procedimiento y condiciona el inicio del FAT a las hidrostáticas | `P22-ET-09-000-001-0`, Section 8.1: las pruebas hidrostáticas de baja y alta *"hayan sido completadas y aprobadas satisfactoriamente antes del inicio formal de las FAT"*, y el alcance mínimo abre con *"Aprobación del Procedimiento FAT"* |
| La revisión documental de ADASA corre siete días hábiles | BAE Cláusula 37.2, primer viñetado |
| Rev B pone el FAT del 7 al 18 y el Progress Update del 15 al 25 | `P22-BA-09-000-001_B Project Schedule` (`ENTREGA 84`), tarea 414: 9/7/2026 a 9/18/2026; Progress Update del 28-Ago, tarea 419: 9/15/2026 a 9/25/2026 |
| Montaje de spools, válvulas, instrumentos y eléctrico en 0 % | `25007 TALTAL PROGRESS REPORT (WEEK 36)`, filas Assembly; también 0 % en el Week 34, de modo que no avanzaron en dos semanas |
| Bandejas, cableado y CSC sin iniciar | Mismo reporte, filas correspondientes en 0 % |
| Bomba de alta y turbos llegan a Penang el 10 de septiembre | `Copy of Procurement tracking - BW Water 2906.xlsx`, comentario de las filas 4, 15 y 19: *"Collection has been made on 4/9, ETA at Penang on 10/9"*; el Progress Report declara *"Collection from FEDCO warehouse on 9/4. ETA on 9/10 at Penang"* |
| Su instalación estaba en el 9 y 10 de septiembre | Progress Update del 28-Ago, tareas 408 y 414 |
| El estanque CIP se declara de dos maneras en el mismo paquete | Progress Report: *"CIP Tank arrived on 9/4"*, 100 %, estado Yes. Tracker, fila 13: llegada real 4-Sep con `Received good` en `Not receive` y comentario *"pending for quality documentation before collection"* |
| El paquete no trae cronograma ni fabrication schedule | Los tres adjuntos del correo del 8-Sep son el Progress Report, el DDSR y el tracker. El paquete de la semana 34 sí incluía `Fabrication schedule.xlsx` |
| El Milestone Tracker declara la línea base del FAT del 13 al 18 de agosto y un ex-works del 10 de septiembre en la columna Actual | Hoja `Milestone Tracker` del tracker de esta semana, filas 4 y 5. Idénticas a las de la semana 34: el diff celda a celda no arroja ningún cambio en esa hoja |
| El Change Log sigue vacío | Misma planilla, hoja `Change Log`: solo el encabezado |
| Loading schedule y vessel closing date pedidos desde el 21 de julio | Nota Técnica `P22-NT-09-000-003-0`, punto 3.A; compromiso `PRG-42` |
| Las membranas siguen pendientes de la respuesta del proveedor | Progress Report, fila RO Membrane: 80 %, estado No, *"Delivery to Taltal site, pending for LG feedback"* |
| **Las diecisiete presiones del plan coinciden con la Line List Rev 1 y todas son 1,5 por la de diseño** | Cruce fila por fila de las 17 del `Testing Plan.pdf` contra la columna de hidrostática de la Line List Rev 1. Cero desviaciones de presión. Los desacuerdos son de rótulo en cuatro filas |
| Las filas 7 y 11 del plan están bien y la Line List mal | El plan escribe `CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`, que son los diámetros que el `P22-TM-09-000-038-0`, Sección 2.5, declaró vinculantes. La Line List Rev 1 los trae invertidos |
| **Los once planos que cita el plan para los carretes de alta son los devueltos como no recibidos** | El plan cita `PI-0901-0006` a `-0016` para las once líneas originales. El `P22-TM-09-000-030-0`, Sección 2.4, los devuelve como no recibidos, y el `P22-TM-09-000-038-0`, Sección 3, los mantiene así |
| Los dos puntos de contención de presión siguen abiertos desde el 5 de agosto | Carry-forward del `P22-TM-09-000-036-0`: derivaciones roscadas austeníticas sobre líneas de 60 a 90 barG de diseño, y el límite super dúplex a PVC sin quiebre de especificación. Compromiso `PRG-22`, CRÍTICA, vencido el 24 de agosto |
| Cuatro carretes van a 135 barG esta semana | Ítems 4, 10, 12 y 13 del Testing Plan: `CP-SSD-DN80-09-015`, `CP-SSD-DN65-09-045`, `DA-SSD-DN65-09-007` y `DA-SSD-DN80-09-006` |
| Los planos `-0023` a `-0028` no aparecen en ningún submittal | El DDSR del 7 de septiembre lista 73 documentos y ninguno es un `25007-ME-PI`. El único juego reclamado hasta ahora es el `-0006` a `-0016` (`PRG-21`) |
| El ítem 14 declara solo el Spool 2 | `Testing Plan.pdf`, fila 14: `DA-SSD-DN65-09-009`, única entrada `Spool 2 - 4/9/2026`. Las filas 1, 9 y 12 sí listan sus dos o tres carretes |
| Los cuatro PDF de la carpeta son los mismos que se leyeron del zip | md5 idéntico en los cuatro archivos entre `TESTING PLAN 08-09-10/` y la copia extraída del `Re_ 25007 TALTAL - Request to witness inspection 007.zip` |
| **Las presiones de prueba están zanjadas por un documento en Código 1** | La Line List Rev 1 llegó en el submittal `25007-0090` con la columna de hidrostática, y el `P22-TM-09-000-038-0`, Sección 2.5, la aprueba en Código 1 declarando que *"the hydrotest column of every line common to Rev 0 is unchanged, so the test pressures ADASA has been requiring remain the approved ones"* |
| **El Testing Plan descarga la retención del circuito completo** | El `P22-TM-09-000-035-0` la impuso: *"No test of the super duplex circuit is to be run until BW Water confirms in writing the pressure it will apply to each line against that table"*. Compromiso `PRG-34`, CRÍTICA, vencido el 1 de septiembre. El Testing Plan declara la presión de las diecisiete líneas y todas coinciden, de modo que la condición queda cumplida |
| El Pressure Test Record Chart sigue sin número ni revisión | `P22-TM-09-000-035-0`, Sección 3: *"Issue as a controlled form, with a document number and revision... It is the form that produces the pressure against time certificate required by rows 5.1 and 5.2 of the Inspection and Test Plan"*. Compromiso `PRG-35`, ALTA, abierto desde el 20 de agosto sin fecha comprometida |
| El ITP Rev 0 tiene catorce Puntos de Detención en la columna de ADASA | Filas 1.1, 2.2, 5.2, 7.1, 7.2, 7.3, 7.5, 7.7, 7.9, 8.3, 8.4, 11.1, 11.5 y 12.3, columna `C`, que la propia leyenda define como ADASA. La fila 5.1, hidrostática de baja en PVC, lleva **W** |
| La leyenda del ITP distingue presencia de notificación | **H**: *"Client or 3rd party requires notification of the inspection or test timing and inspection or test shall be carried out with the client or 3rd party in attendance"*. **W**: *"...However inspection and test are performed as scheduled, and even if the client or 3rd party is not present"* |
| El documento de referencia de la fila 5.2 es el procedimiento, no un cronograma | La fila 5.2 nombra `Pressure and Leak Test Procedure` / `PROV-PROC-PH-HP-001`, que es el `P22-BA-09-000-010`, en Código 1 desde el `P22-TM-09-000-035-0`. Por eso el correo **no** pide número de documento para el Testing Plan |
| **Los tres ensayos que BV rechazó aplicaron 7,5 barG** | `BVM-IR005` Rev 01: `CP-SSD-DN100-09-014` juntas 01 y 02, diseño 80, exigida 120, aplicada 7,5. `BVM-IR006` Rev 01: `CP-SSD-DN80-09-015` juntas 01 y 02, diseño 90, exigida 135, aplicada 7,5, y `CP-SSD-DN80-09-044` **juntas 03 y 04**, diseño 80, exigida 120, aplicada 7,5. Los tres son del circuito CIP |
| **Las juntas rechazadas del `09-044` no aparecen reensayadas** | El `BVM-IR011` del 3-Sep cubre las **juntas 01 y 02** de ese carrete, no las 03 y 04 que fallaron. El Testing Plan lo da por terminado con esa única fecha |
| Los planos `-0006` a `-0016` fueron devueltos como no recibidos | `P22-TM-09-000-030-0`, Sección 2.4: *"ADASA cannot approve or reject what was not submitted, so this set is returned as not received and carries no response code"*. Sigue abierto en la Sección 3 del `P22-TM-09-000-038-0` y en el `PRG-21` |
| 9-Sep es miércoles, 10 jueves, 11 viernes | Encabezado del correo de Eduardo Yamauchi del martes 8-Sep y los tres formularios `Inspection Request 007`, que declaran 9, 10 y 11 de septiembre |

## Contexto Interno (No enviar)

- **La respuesta a la Nota Técnica 003 venció con este paquete.** La NT pidió sus cinco puntos *"with the next weekly progress update"*. El reporte llegó y los puntos no. Los compromisos `PRG-41` y `PRG-42` están vencidos desde el 4 de septiembre. **El correo lo menciona una sola vez y sin reproche**, en el primer punto del bloque 2, porque la decisión del usuario es mantener el 28 de septiembre y preguntar, no declarar todavía que la fecha no se sostiene.
- **Lo que el correo deja fuera a propósito:** el Plazo de Entrega vencido el 3 de agosto y la multa de la Cláusula 43.1 letra b; el saldo de jornadas contratadas a Bureau Veritas y sus tarifas; los cinco documentos del cierre consolidado del 3 de septiembre que no llegaron, que ya viven en la Sección 3 del Transmittal N38; y la reserva de la Nota Técnica 003, que se emitió el 31 de agosto y no se repite.
- **No se cita el registro de la reunión del 1 de septiembre.** Es un resumen automático interno de ADASA, no una minuta oficial del proveedor, y la regla del proyecto prohíbe citarle documentos internos. Los ocho compromisos que ese registro recoge se verifican igual, pero por sus documentos: el paquete, el DDSR y el tracker.
- **La coincidencia del PVC con los 7,5 barG queda fuera del correo, por decisión del usuario.** Los tres ensayos que BV rechazó el 20 y 21 de agosto aplicaron 7,5 barG, que es justo la presión de ensayo que la Line List asigna al PVC, y uno de ellos, el `CP-SSD-DN80-09-044`, es uno de los dos carretes que el hallazgo del TM N30 describe construidos con tubería PVC SCH 80. **Es coincidencia, no causa probada**, y sin los planos de taller no se sostiene. Por eso el correo pide los planos y no afirma nada sobre el material de los carretes. Se plantea verbalmente en la reunión si el tema aparece.
- **Los tres defectos del plan de ensayos son de rótulo, no de presión.** Las presiones que el plan aplica coinciden con la Line List aprobada en las diecisiete líneas. Por eso el bloque 1 se redacta como corrección de registro y reconoce explícitamente que la presión está bien donde lo está: un reclamo que exagerara aquí sería refutable en un párrafo.
- **La objeción de fondo del 20 y 21 de agosto quedó resuelta por diseño.** BW Water partió el circuito CIP en tramos de alta y de baja, les dio número de línea propio en la Rev 1 y presión propia, y ADASA aprobó esa Rev 1 en Código 1 en el Transmittal N38. Ensayar `09-047`, `09-048`, `09-049` y `09-051` a 7,5 barG ya no es la irregularidad que era en agosto.
- **Estado real del Punto de Detención al 8 de septiembre:** de las once líneas de super dúplex de alta, cuatro tienen ensayo conforme (`09-003` el 2-Sep, `09-005` y `09-044` el 3-Sep, `09-009` el 4-Sep, informes `BVM-IR010` a `IR012`) y siete quedan pendientes, de las cuales dos son repeticiones. **Ninguna de las cuatro líneas que exigen 135 barG se ha ensayado todavía**; las tres jornadas de esta semana las cubren.
- **Bureau Veritas: la asistencia ya está confirmada y ADASA no interviene.** Mohd Adnin envió el Request 007 a Bureau Veritas el **viernes 4 de septiembre a las 16:26**, con los tres formularios de día y el Testing Plan, y Ahmad Hazwan respondió el **martes 8 a las 00:50** asignando al mismo inspector, Fakhrul, para las tres jornadas. Luis va en copia en las dos puntas, de modo que la coordinación queda entre el proveedor y el inspector y **no hay correo que ADASA deba emitir**. El respaldo vive en `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/TESTING PLAN 08-09-10/PETICION DE BV.pdf`. El aviso fue de cinco días contra los treinta de la Cláusula 37, y no se objeta: ADASA ya aceptó avisos de cuatro y ocho días, y reclamarlo ahora contradiría la posición del 14 de agosto.

## Checklist pre-envío

- [x] `anti-ia` modo **revisar** sobre la versión emitida: original AMARILLO por voz, reescritura **VERDE** al 1 %, con la familia Claude cargada por autoría conocida. Veredicto y estilometría antes y después en `.anti-ia-2026-09-08/veredicto.md`
- [x] Signo de sección: cero coincidencias en el `.py` y en el `.docx`
- [x] Em dash: cero
- [x] Estilometría contra el perfil de correspondencia: mediana 21,5, media 20,2, percentil 90 en 30, máxima 47, primera persona presente, cero punto y coma y cero em dash
- [x] Día de la semana verificado: 9 miércoles, 10 jueves, 11 viernes
- [x] Metadatos Word: autoría Luis Rivera Gonzalez, título y asunto poblados, sin `python-docx`
- [x] Cada cifra contrastada contra su fuente primaria, ninguna de memoria
- [x] Confirmar la lista de CC contra el correo original antes de responder
- [x] Enviar antes de las 21:00 de Chile

## Checklist post-envío

- [ ] Dejar el respaldo del enviado en esta carpeta, con la hora
- [ ] 🔴 **Verificar sobre el respaldo que la tabla de cuatro filas viajó completa.** En este proyecto el pegado en Outlook ya se comió cuatro veces un bloque del cuerpo, y la tabla es donde viven las cuatro correcciones
- [ ] Cerrar el `PRG-34` en `compromisos.yaml`: el Testing Plan es la confirmación escrita que su criterio de cierre exige
- [x] Cambiar el estado de este archivo a `ENVIADO`
- [x] Pasar de `BORRADOR` a `ENVIADO` la entrada del 8 de septiembre en la Bitácora del README
- [ ] Sumar el `Request to witness inspection 007` y los informes `BVM-IR010` a `IR012` al `_REGISTRO_INSPECCIONES_BV.md`, cuyo corte sigue en el 31 de agosto
