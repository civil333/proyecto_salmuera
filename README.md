# Modulo de Salmuera Taltal

Proyecto de suministro de Modulo de Osmosis Inversa UHPRO para segunda etapa de tratamiento de salmuera en Planta Desaladora Taltal.

---

## Estado Vigente

> Snapshot que se **pisa** en cada cambio (no se acumula). El detalle cronológico está en la Bitácora; las referencias estables (contrato, equipos, baseline, contactos, QA) al final.

- 🔴 **BW Water corrió el embarque al 28 de septiembre alegando clima. ADASA respondió el 31-Ago con la Nota Técnica `P22-NT-09-000-003-0`, **ENVIADA** en versión suave, por decisión del usuario de no comprometer la entrega del 28.** El documento deja de disputar la fecha y pasa a asegurarla: cinco puntos, cuatro páginas, y **una sola frase con efecto contractual** —tomar nota de la fecha revisada no constituye aceptación de una nueva fecha contractual ni renuncia a los derechos del Contrato—, sin números de cláusula y sin plazo impuesto. Los tres puntos que sí entraron son los que **amenazan** el 28: qué ventana del FAT gobierna, porque el Rev B la pone del 7 al 18 de septiembre y el Progress Update del **15 al 25** y el inspector se agenda por Bureau Veritas Chile con su oficina de Malasia (`BV-13`, cuarta reprogramación); la bomba de alta que se instala el **9 y 10** mientras su flete aterriza el **11**; y el *loading schedule* con el *vessel closing date*, pedidos desde el 21 de julio (`PRG-41`, `PRG-42`). 🔴 **Lo retirado sigue verificado y guardado** en la Bitácora y en la nota de `PRG-41`, listo para reponerse si la fecha vuelve a moverse: que el Rev B del 24-Ago ya daba el pintado del contenedor terminado el 21 y al 0 % y que esa actividad no tiene línea base; que la Cláusula 44 excluye el clima salvo Fuerza Mayor con aviso en 48 horas; los **44 días** de desviación en el ex-works contra la línea base del propio proveedor y **51** en la entrega en sitio; y que el umbral de treinta días de atraso se cumple el **jueves 3 de septiembre**. 🔴 **`INT-08`: la Notificación de Adjudicación no está en el repositorio** y hay que pedirla a Abastecimiento antes de cuantificar nada. 🔴 **El plazo de la NT-003 venció con el paquete del martes 8 de septiembre.** La nota pidió sus cinco puntos con el próximo reporte semanal de avance: llegó el reporte y no llegaron los puntos, de modo que `PRG-41` y `PRG-42` quedan vencidos desde el 4. **Ese paquete tampoco trae cronograma ni fabrication schedule, por primera vez**, así que no hay cambio declarado en la entrega y la última fecha que el proveedor sostiene sigue siendo la del Progress Update del 28-Ago. **Decisión del usuario el 8 de septiembre: mantener el 28 y preguntar en la reunión**, con el correo de puntos de revisión de `CORREOS/Septiembre 2026/2026-09-08/` y sin declarar todavía que la fecha no se sostiene.
- 🟡 **Los ensayos de alta presión se reactivaron y la campaña que cierra el punto Hold corre el miércoles 9, el jueves 10 y el viernes 11.** Al 8 de septiembre hay **cuatro líneas conformes** de las once de alta —`DA-SSD-DN100-09-003` el 2, `DA-SSD-DN80-09-005` y `CP-SSD-DN80-09-044` el 3, `DA-SSD-DN65-09-009` el 4, informes `BVM-IR010` a `IR012`— y las siete restantes, dos de ellas repeticiones, entran en las tres jornadas del `Request to witness inspection 007`. **Ninguna de las cuatro líneas que exigen 135 barG se ha ensayado todavía.** Si las tres jornadas se cumplen, el requisito de la ET Section 8.1 —hidrostáticas completadas y aprobadas antes del inicio formal del FAT— queda cubierto el viernes 11. 🟢 **La objeción del 20 y 21 de agosto quedó resuelta por diseño:** BW Water partió el circuito CIP en tramos de alta y de baja, les dio número de línea y presión propios en la Line List Rev 1, y ADASA la aprobó en Código 1 en el TM N38, de modo que ensayar `09-047`, `09-048`, `09-049` y `09-051` a 7,5 barG ya no es irregular. 🔴 **Lo que queda abierto son tres defectos de rótulo del Testing Plan, no de presión**, verificados contra la Line List aprobada: el ítem 9 rotula `DA-SSD-DN100-09-005` cuando la línea es DN80; el ítem 16 rotula como super dúplex a `09-016`, que es `DA-PVC-DN65-09-016` en PVC SCH80; y **`DA-SSD-DN100-09-050`, la succión de la bomba de alta, no tiene ensayo programado**, la única de las diecisiete líneas de super dúplex ausente del plan. Los tres van en el correo de puntos de revisión del 8-Sep, con respuesta pedida antes de que abra la jornada del miércoles. 🔴 **Y el plan traza cada carrete de alta a los planos `25007-ME-PI-0901-0006` a `-0016`, que son los que el TM N30 devolvió como no recibidos** y cuyos dos puntos de contención de presión siguen abiertos desde el 5 de agosto (`PRG-22`, vencido el 24): mañana esos carretes se presurizan y cuatro van a 135 barG, de modo que el correo vuelve a pedir la confirmación escrita que nunca llegó. Los planos `-0023` a `-0028` de los carretes de baja no aparecen en ningún submittal. 🟢 **El inspector para las tres jornadas ya está confirmado y ADASA no tiene que emitir nada**: BW Water pidió las tres visitas el viernes 4 y Bureau Veritas asignó al mismo inspector, Fakhrul, el martes 8 a las 00:50, con Luis en copia en las dos puntas. 🟢 **Las presiones de ensayo están zanjadas y no son materia de discusión:** las fija la columna de hidrostática de la Line List Rev 1, aprobada en Código 1 en el TM N38, y el Testing Plan las aplica sin desviaciones, con lo que **queda levantada la retención que el TM N35 impuso sobre todo el circuito** (`PRG-34`). Lo que la fila 5.2 del ITP exige es **presencia**, no aprobación de la presión, y eso lo cubre el inspector. Deslinde en `feedback_presion_acordada_no_libera_la_presencia`. 🔴 **Dos huecos que el correo del 8-Sep pone por escrito:** los planos de detalle de los carretes siguen sin recibirse, de modo que ni ADASA ni el inspector pueden contrastar el carrete del banco contra su plano, y se exige que Bureau Veritas los tenga en las tres jornadas. Y el `CP-SSD-DN80-09-044`, rechazado el 21 de agosto en las juntas 03 y 04, se reensayó el 3 de septiembre en las juntas 01 y 02, con el Testing Plan dándolo por terminado: **las juntas que fallaron no aparecen reensayadas en ningún informe**.
- 🔴 **No hay quién endose el cálculo sísmico, y el informe ya salió en Rev 0 apto para construcción.** El 17-Ago BW Water informó que el ingeniero chileno que le certificaba los documentos no está disponible y pidió a ADASA que le recomiende uno. Lo había comprometido por escrito el **20-May**, el **16-Jun** y el **30-Jun**, esta última con la acción tabulada de enviar el paquete al profesional el **01-Jul**; ADASA pidió la fecha de emisión del informe certificado el **17-Jun** y nunca la recibió. La Rev 0 del 23-Jul (`P22-CD-09-005-001`) lleva solo iniciales internas, sin firma ni timbre. **El endoso no lo exige la ET, la BAE ni el PIE: es compromiso unilateral de BW Water**, y ahí se ancla el reclamo. Respuesta **ENVIADA el 18-Ago** desde `CORREOS/Agosto 2026/2026-08-18/`, con cierre exigido al **viernes 22-Ago** y la recomendación de Thomas Engineers entregada como referencia sin designación (`PRG-32`, CRÍTICA).
- 🔴 **El Plazo de Entrega contractual venció el lunes 03-Ago-2026.** BAE **Cláusula 27**: máximo 300 días corridos desde la Notificación de Adjudicación (07-Oct-2025), plazo firme, sin modificación salvo aceptación escrita mediante revisión del Pedido. La fecha calculada coincide exactamente con la línea base del hito `Ready to Ship` del propio Milestone Tracker de BW Water. Fecha de embarque declarada por el proveedor: **28 de septiembre**, no aceptada por ADASA, es decir **47 a 49 días** sobre la línea base contractual. Multa aplicable: **Cláusula 43.1 letra b)**, 0,2% diario del valor neto del Contrato, con tope acumulado de 15% en la **Cláusula 43.4**. **Antes de cursar multa hay que leer la Notificación de Adjudicación**: los 300 días se calculan sobre el `Contract Award / NTP` del cronograma del proveedor, y la coincidencia con el Milestone Tracker es indicio fuerte, no prueba.
- 🔴 **Dos hallazgos de contención de presión en planos de taller timbrados FOR CONSTRUCTION.** En las láminas `25007-ME-PI-*` de la E70: acoples roscados ANSI 150# en austenítico F304 y F316L para las tomas de instrumento de ½", sobre líneas que la Line List aprobada rotula de 60 a 90 barG de diseño y hasta 135 barG de prueba en salmuera de 45.000 a 55.000 ppm de cloruro; y el límite entre el sistema super dúplex y el PVC sin quiebre de especificación ni corte de número de línea, con PVC de 5 barG dentro de líneas de 80 y 90 barG. Las mismas láminas ya usan el sockolet super dúplex correcto en otras derivaciones. Se pide **confirmación escrita de si alguna ya se fabricó**, antes de la jornada de prueba hidrostática del **13 y 14 de agosto**, que es punto Hold del ITP (`PRG-22`).
- 🔴 **El turbo interetapa no calza con sus spools: unos 50 mm de desfase, spools a cortar, resoldar y reensayar, y listo para despacho al 12 de octubre.** Lo informó BW Water en la reunión del 16-Sep, después de reportarlo el 14 en una sola línea. Por las fotos, el afectado es el interetapa, que trabaja a la presión más alta del módulo (84,8 bar; líneas de 90 barG de diseño y 135 barG de prueba). El Piping Layout y el modelo 3D se emitieron y revisaron en Código 2 y en ellos las conexiones calzan. **Los planos de fabricación oficiales de los spools nunca se emitieron**, pese a los TM N30, N36, N37, N38 y N39. **Respuesta ENVIADA el 16-Sep** con esa trazabilidad y seis pedidos para antes de la reunión del 17 a las 08:30 (`PRG-51`, CRÍTICA): ningún spool se corta antes de que ADASA reciba los planos, y el reensayo va completo, fuera del contenedor y con Bureau Veritas. Toma nota del 12-Oct sin renunciar a derechos, con las Cláusulas 27 y 43.1 b) nombradas y sin cifras. **Correo a Bureau Veritas ENVIADO el 16** (`2026-09-16_BV-Survey-Turbocharger-Offset.docx`): mantiene la prueba de alta del 17 sin las líneas de los turbos y pide un levantamiento desde el 18 de causa raíz, equipos, instrumentos y otros temas constructivos, más un informe eléctrico aparte (`BV-26`, `BV-27`). Victor Gutierrez lleva el tema desde el 17. 🔴 **Reunión del 17-Sep:** el informe escrito no llegó. BW Water dice de palabra que el turbo cumple el modelo 3D y que solo dos spools de la conexión superior chocan, y atribuye el desfase, sin confirmarlo, a su largo e inclinación. Plan: planos corregidos y corte el 18, raíz el 19, PT el 21, hidrostática el 22 y remontaje el 23. **ADASA aceptó que el corte avance en paralelo con su revisión de los planos**, sin dejar reserva de riesgo, lo que deja sin efecto el "antes de cortar" de `PRG-51`. 🔴 **Pendiente interno:** los GA de los turbos siguen en Código 3 desde el TM N10, pero el Master Register y la Tabla 1 del TM N39 los dan por aprobados. Se corrige en el TM N41, porque el N40 va solo del FAT.
- 🔴 **El procedimiento FAT del módulo nunca se sometió, y el FAT ya no será la semana del 21 de septiembre**, según la reunión del 16. El barrido de las 93 entregas del 16-Sep (933 archivos por nombre y 390 PDF únicos por texto) confirma que `PROV-PROC-FAT-001` no existe. El único procedimiento FAT recibido es el `P22-PP-09-000-001` Rev C, que es solo hardware del tablero y excluye por su Section 3 las pruebas de software y la verificación de lógica. Su aprobación es Hold de ADASA en la fila 7.1 del ITP Rev 0. **Correo urgente ENVIADO el 16-Sep por hilo nuevo**, con la trazabilidad desde el TM N17 del 5 de mayo y plazo al **viernes 18 de septiembre**, feriado en Chile y hábil en Malasia (`PRG-50`, CRÍTICA). El 17 BW Water dijo que el procedimiento quedó preparado ese día, en revisión interna, y que lo somete el 18. 🟢 **La plantilla del TM N40 quedó lista para que la emita Victor Gutierrez**, solo del FAT y sin pendientes de transmittales anteriores, con su guía de revisión, en `REVISIONES/TRANSMITTALES/P22-TM-09-000-040-0/`. Con recepción el 18, la Cláusula 37.2 vence el martes 29-Sep. El FAT se reprograma con el cronograma que BW Water emitirá el 23 o 24-Sep, y el embarque queda en espera hasta recibirlo.
- **Punto de contacto:** Luis Rivera fuera de la oficina hasta el 2-Oct, de vuelta el 5-Oct. Victor Gutierrez lleva la comunicación con BW Water y decide, incluido el despacho.
- **Compromisos:** 91 vivos · 45 vencidos (39 BW Water / 3 ADASA / 3 otros) · 6 vencen esta semana · 38 sin fecha comprometida — corte 17-Sep-2026. `PRG-52` nuevo: la coordinación del despacho de membranas, a cargo de ADASA, sin fecha. **`PRG-51`, el informe del desalineamiento de los spools del turbo, para antes de la reunión del 17 de septiembre**, fijado por ADASA el 16-Sep. **`PRG-50`, el procedimiento FAT del módulo, con fecha al viernes 18 de septiembre**, fijada por ADASA el 16-Sep. **`PRG-49`, el paquete de izaje del módulo, con fecha al jueves 17 de septiembre, vencida sin entrega**, fijada por ADASA el 15-Sep tras un addendum incompleto. Las fechas que BW Water dio en las reuniones del 16 y el 17 (planos el 21 o 22, cálculos y yugo el 18) son verbales y no mueven el registro. 🔴 **`PRG-48`, el más crítico: la emisión en revisión 0 de la ingeniería ya aprobada, ahora con fecha al viernes 11 de septiembre.** Se pidió el 7 de mayo, nunca se respondió y nunca se registró, de modo que dejó de seguirse. Entró SIN FECHA porque BW Water no comprometió ninguna y ADASA tampoco la había fijado, y la fecha se escribió el 9 de septiembre, el día en que salió el correo que la comunica, no antes.
- 🔴 **Último transmittal: TM N39 ENVIADO el miércoles 9-Sep-2026, con la exigencia de emisión en revisión 0 en su Sección 3 y un solo correo para las dos cosas.** `P22-TM-09-000-039-0`, submittals `25007-0091` (E91, del viernes 4-Sep) y `25007-0092` (E92, del martes 8-Sep), tres documentos.** Veredicto global **2 — Approved as noted: 1 Código 1, 2 Código 2, cero Código 3**. Ninguno vuelve a revisión. **Los tres son re-emisiones y se revisaron solo contra los comentarios ya levantados**, que es la regla que el usuario reiteró al encargarlo. **El punto con fecha es la Valve List Rev E**, que baja de Código 1 a Código 2: de los tres cambios que BW Water comprometió por escrito hizo dos —los cuatro TAG del modelo 3D están y los cuatro figuran en el P&ID Rev 0, y `VRP-09-001` reemplaza la placa de orificio en `CIT-09-004`— y falta el tercero, porque `VM-09-065` sigue en PVC sobre la línea `CP-SS316-DN150-09-022`, que la Line List Rev 1 aprobada en Código 1 en el N38 lleva en 316L, siendo además la única DN150 del circuito CIP. **Las válvulas se compran contra esa lista.** El GA del estanque de antiescalante cierra la cota del agujero de anclaje y no cierra la fila `LEVEL MARKING`, que sigue con guion en tamaño y en elevación mientras su hoja de comentarios la declara agregada: se verificó por render, no por el texto extraído. **El procedimiento de radiografía llega en Rev 0 y sale en Código 1**, tercero y último de los ensayos no destructivos en emitirse; lo que le queda, el número de documento propio, es housekeeping y por regla del proyecto no degrada. **Dos PDF anotados**, los dos verificados por render. 🔴 **El transmittal lleva además una Sección 3 nueva, `Issue for Construction of the Approved Engineering`**, con las cuatro tablas de la auditoría de emisión y sus 51 filas: los 34 aprobados sin observación, los 12 con condición abierta, los 7 de calidad y los 7 entregables de la Sección 7 no recibidos. Las cifras las importa del auditor en tiempo de ejecución, de modo que el transmittal y su correo no pueden discrepar. Las secciones que la seguían corrieron a 4, 5 y 6. **El enlace de descarga ya está incorporado y el PDF emitido**: 11 páginas desde Microsoft Word, con el índice resuelto, el enlace clicable e idéntico al publicado, y las tablas sin ninguna palabra partida ni fila cortada entre páginas. **Enviado con el PDF de 11 páginas como adjunto y los dos `CC_ADASA` por enlace de descarga.** Master Register aplicado y `PRG-48` fijado al viernes 11. **Pendiente:** archivar el respaldo del enviado con su hora, y comprobar sobre él que el bloque del enlace viajó, que es donde el proyecto lleva cuatro pérdidas.
- **Un transmittal atrás:** TM N38 ENVIADO el jueves 3-Sep-2026 a las 18:19, con el saldo del cierre documental consolidado.** `P22-TM-09-000-038-0`, submittals `25007-0089` (E89, del martes 1-Sep) y `25007-0090` (E90, del jueves 3-Sep), **once documentos**. Veredicto global **2 — Approved as noted: 8 Código 1, 3 Código 2 y cero Código 3**. **El hecho central no es el veredicto: de los doce documentos que el N37 exigió para hoy llegaron siete**, y los cinco ausentes son los tres pendientes más graves del proyecto —los once planos de taller, el dossier y el informe estructural endosado— más el procedimiento de FAT del módulo y el de conservación y embalaje. Los once que sí llegaron están en buen estado y cierran ciclos largos: los tres datasheets Fedco salen para construcción sin revisión intermedia, el transmisor de vibración queda re-rangeado, **el procedimiento de FAT del tablero dejó de ser el registro de un ensayo ya corrido y es un procedimiento en blanco**, y **BW Water compromete por escrito un segundo FAT en Penang con testigo de ADASA y de un tercero**. **Siete de los once vienen emitidos para construcción y sobre un Rev 0 no se abren comentarios nuevos**: se verificó la condición de cada uno, ninguno la falla, y lo que la revisión encontró de nuevo se documenta en la Sección 3 y en el correo sin degradar el código. **En dos puntos ADASA declara el valor vinculante en vez de pedir que lo reconcilien:** las dos medidas invertidas de los spools de rechazo CIP, donde la Line List Rev 1 se contradice con su propia columna de caudal y el P&ID es el que está correcto, y la asignación del relé del calentador CIP en el procedimiento de FAT, que gobierna la I/O List Rev 6 aprobada en Código 1. **Tres PDF anotados** con cinco cuadros verificados por render. PDF de **12 páginas** exportado desde Word real, con el índice resuelto y el enlace clicable verificado sobre el documento emitido. **Master Register aplicado**: el tally obtenido coincide con el declarado antes de correr y el gate quedó en exit 0. 🔴 **El bloque del enlace de descarga no sobrevivió al pegado en Outlook**: los tres párrafos salieron íntegros pero el enlace y las viñetas de los `CC_ADASA` no, de modo que BW Water tiene el transmittal y no los anotados. **El enlace se reenvió el mismo día en la misma cadena**, con un correo transaccional de 71 palabras; queda sin verificar contra respaldo, que es el chequeo que importa porque la pérdida en Outlook ya va cuatro veces. Allan Valentos quedó fuera por segunda vez consecutiva: la omisión se confirma deliberada.
- **Dos transmittals atrás:** TM N36 (P22-TM-09-000-036-0) **ENVIADO el miércoles 26-Ago-2026 a las 18:08**, submittals `25007-0082`, `25007-0083`, `25007-0084` y `25007-0085` (E82 a E85, recibidas entre el 21 y el 26 de agosto), **nueve documentos**, el lote más grande desde el TM N26, de los cuales **el transmittal dispone ocho**. Veredicto global **2 — Approved as noted: 3 Código 1 y 5 Código 2. Ningún documento vuelve a revisión.** 🔴 **El Project Schedule Rev B se retiró del transmittal** por decisión del usuario: su seguimiento se lleva por la **reunión semanal de coordinación**, de modo que no recibe código de respuesta, sus dos observaciones salen y su PDF anotado no se emite. El transmittal lo declara en una línea para que BW Water no quede esperando un código. El paquete retirado sale de la carpeta del transmittal y queda junto al documento, en `ENTREGAS_BWWATER/ENTREGA 84/_cronograma_fuera_de_transmittal/`. 🔴 **El punto más grave del lote es el hito documental de los tres equipos Fedco.** La bomba de alta y los dos turbocargadores están **comprados, fabricados y a días de montarse** —su cronograma programa la instalación de la bomba dentro del contenedor del 3 al 5 de septiembre y la apertura del FAT el 7— y sus hojas de datos siguen llegando **en Rev E para aprobación**. El transmittal exige cerrarlas en **Rev 0 antes de que abra el FAT**, con bloque propio en el Resumen Ejecutivo, y declara que ADASA no seguirá recibiendo y devolviendo revisiones de aprobación de equipos en camino al montaje. Compromiso `PRG-37`, crítico. **El segundo frente es el GA of SWRO System Skid Rev 0**, único emitido para construcción: de las tres referencias que constituían su Código 2 del TM N31 **solo una se corrigió**, la nota 8 sigue citando un código inexistente en un plano que ya gobierna fabricación, y **la captura que BW Water adjunta para justificarla escribe ese mismo código con tres dígitos**. Se dispone en **Código 1 y no en Código 3**: está en Rev 0 emitido para construcción y los dos puntos son de cita, no de contenido, así que no se retiene el plano; el texto, en cambio, va endurecido y escribe literal el código correcto. 🔴 **La calibración se corrigió antes de emitir.** La primera disposición llevaba cuatro Código 3; la verificación adversarial mostró que tres recaían sobre revisiones sometidas **para aprobación**, cuyas condiciones vencen al emitir Rev 0 según la frase literal que ADASA misma escribió en los transmittals N20 y N30, de modo que escalar se contradecía. Quedan reiteradas en Código 2 con constancia de segundo ciclo. **La columna de emisión del Submittal Form pasa a decidir el código:** IFC deja Código 1 o Código 3; IFA reitera en Código 2. **Hallazgos de fondo:** en el modelo 3D la hoja de comentarios declara corregidos cincuenta y siete TAG que son soportes de cañería y **ninguno se tocó, ahora son setenta y dos**, aunque sí cerraron los siete TAG de válvula donde el TM N30 nombró uno; el cronograma no trae **ninguna** actividad de certificación de recipientes ni **ningún** ensayo de presión, con los recipientes ya fabricados y recibidos en Penang; y el GA del estanque antiscalante **recupera desde Código 3** entregando cargas sísmicas, patrón de anclaje, volumen útil y TAG. **Cuatro PDF anotados** más la excepción declarada del modelo Navisworks, que no admite el formato. **Enviado a las 18:08 con el transmittal en PDF de nueve páginas como único adjunto —índice resuelto desde Word real— y los cuatro `CC_ADASA` por enlace de descarga, verificado carácter a carácter sobre el respaldo. Master Register aplicado. Único pendiente del ciclo: decidir si sale el correo contractual del cronograma, que sigue en borrador.**
- **Dos transmittals atrás:** TM N35 (P22-TM-09-000-035-0) **ENVIADO el jueves 20-Ago-2026 a las 11:16**, submittal `25007-0081` (E81, recibido el jueves 20-Ago), cinco procedimientos del paquete de calidad y fabricación, todos re-emisiones que responden al TM N32. Veredicto global **3 — To be revised: 2 Código 1 y 3 Código 3**. **El código lo fijan los tres procedimientos de ensayos no destructivos**, que vuelven por segunda vez sin fijar el criterio de aceptación de ASME B31.3 que la ET Sección 8 y el NDE Plan Rev C hacen aplicable, y los tres se re-emiten **sin hoja de comentarios consolidada**: el cierre se verificó comparando el texto de la Rev A contra la Rev B, y el diferencial es de once líneas en el de penetrantes, dos cambios en el de radiografía y nueve en el de ultrasonido. **Los dos que llegan por sobre la Rev 0 son Código 1**: el de presión incorporó el formulario `AQ-QAM-F018` Rev 4 que faltaba desde la Rev D, y el de pintura corrigió la fila de color a `RAL 5012 Luminous Blue`, que era su única condición. Tres PDF anotados. El transmittal declara además **la regla de presión de prueba** con listado por TAG de las once líneas de super dúplex y retención de ensayos. **Carpeta publicada, enlace pegado y verificado sobre los `.docx` emitidos, y PDF de 10 páginas exportado desde Word real con el índice resuelto. Los dos correos salieron el mismo día: el de la hidrostática a las 11:00 y el del transmittal a las 11:16, con los respaldos archivados.**
- **Tres transmittals atrás:** TM N34 (P22-TM-09-000-034-0) **ENVIADO el 18-Ago-2026** (hora de Chile por registrar desde el respaldo), submittals `25007-0073` (E73, 11-Ago), `25007-0077` (E77, recibido 18-Ago) y `25007-0080` (E80, 18-Ago), cinco documentos. Veredicto global **3 — To be revised: 2 Código 1, 2 Código 2 y 1 Código 3**, y el código lo fija **un solo documento**, el Quality Dossier Index Rev B. **El determinante:** su hoja de comentarios declara incorporada el Acta de Aprobación FAT en la Sección C21, pero C21 es el certificado de liberación para despacho de la fila 8.4 del ITP; el Acta es la fila 7.9, punto de detención, y la ET Sección 8 la hace parte integral e indispensable del dossier final. No tiene capítulo. **ADASA declara el rango vinculante de `VT-09-001` en 0 a 12 mm/s rms** y exige reemitir la Instrument List, que sigue en 8,9: mientras no ocurra, el disparo por vibración de un motor de 93 kW no puede actuar. **Los dos documentos en Rev 0 son Código 1**: sobre un Rev 0 el defecto que vive en otro documento no degrada. Tres PDF anotados. Transmittal de ocho páginas y correo de **156 palabras**. **Pendiente:** archivar el respaldo del enviado con la hora.
- **Cuatro transmittals atrás:** TM N33 (P22-TM-09-000-033-0) **ENVIADO el 17-Ago-2026 12:17**, submittals `25007-0076` (E76, 13-Ago), `25007-0078` y `25007-0079` (E78 y E79, 17-Ago), cinco documentos. Veredicto global **2 — Approved as noted: 4 Código 1 y 1 Código 2**, ningún documento vuelve a revisión, un solo PDF anotado con dos observaciones. **El criterio que lo gobierna:** la revisión de un documento que responde a comentarios previos se limita a si esos comentarios están cerrados, y no se introducen observaciones nuevas. El único Código 2 es el plano civil, cuyas dos partes de la NOTE-01 del TM N16 no cerraron. El Equipment Layout cierra su filtro de cartucho vertical, verificado por render, abierto desde el TM N22. **No existe el submittal `25007-0077`.** Lo retirado vive en los ledgers y en `INT-11` e `INT-12`. **Versión ejecutiva:** transmittal de **cinco páginas y 1.138 palabras, sin tabla de contenidos** (desviación puntual de la Sección 3.1, anotada en el script; la regla no cambia) y correo de **199 palabras**. **Pendiente:** abrir el enlace para confirmar que muestra el `CC_ADASA`, y archivar el respaldo del enviado.
- **Cinco transmittals atrás:** TM N32 (P22-TM-09-000-032-0) **ENVIADO el 12-Ago-2026 15:30**, submittal `25007-0075`, siete documentos del paquete de calidad y fabricación. Veredicto global **3 — To be revised**: 2 Código 1, 3 Código 3 y dos documentos devueltos sin código. Los tres procedimientos de ensayos no destructivos llegan por primera vez y ninguno fija el criterio de aceptación de ASME B31.3 que exige la ET Sección 8. 🔴 **Del cuerpo del correo salió el enlace de descarga**, ausente por tercera vez tras el N30 y el N31.
- **Entregas recibidas:** E1–E94, **94 en total**. **E93 y E94** llegaron después del N39 (hojas de datos y listados en Rev 0, la Line List Rev 2 y el esquemático del tablero Rev C) y **no tienen transmittal todavía**. La serie del proveedor **no tiene números ausentes**. Las dos anteriores: **E91** (`25007-0091`, la Valve List Rev E y el GA del estanque de antiescalante Rev D, recibida el viernes 4-Sep) y **E92** (`25007-0092`, el procedimiento de radiografía en Rev 0, recibida el martes 8-Sep), las dos devueltas en el TM N39. **Los formularios vuelven a pedir devolución en tres días corridos**, contra los siete días hábiles de la Cláusula 37.2 que vencen el martes 15 y el jueves 17: octavo y noveno lote consecutivo por debajo del plazo. ADASA devuelve los dos bien dentro del período. El nativo de AutoCAD del GA viajó en la E91 sin figurar en su formulario.
- 🔴 **Frente Bureau Veritas: entregó el set completo IR001 a IR009 y cerró cuatro de las seis peticiones del 21 de agosto, pero la No Conformidad sigue sin levantarse y el informe del 24 repite el defecto.** Carlo Montecinos remitió el lunes 31-Ago 14:47 los nueve informes, con el `IR005` y el `IR006` en revisión 01. **Verificado por render, no por texto extraído**: el `IR005` pasó de `Satisfactory (Without comments)` a **`Not Satisfactory`** y el `IR006` de `Satisfactory with comments` a **`Not Satisfactory`**; la tabla de presiones ahora coincide con la Line List; el P&ID `P22-DWG-09-009-002` Rev D y la Line List `P22-LI-09-009-003` Rev 0 entraron a la sección B y siguen ahí en los informes del 27 y del 28; y desde el `IR008` el registro fotográfico incluye la marca de identificación del carrete. `BV-24` a **CERRADO PARCIAL**. **Lo que queda es una contradicción del propio formulario reemitido**: marca `Not Satisfactory`, que el formulario define como No Conformidad levantada durante la inspección, y tres líneas más abajo marca `Open Non Conformities: No` con la sección G en `N/A`. El `BVM-IR007` del 24-Ago repite el defecto tres días después del reclamo, sobre un hallazgo real —la parte inferior del marco del skid no alcanza los 355 micrones de espesor de película seca (`PRG-40`, sin fecha)—. Su cuadro resumen declara además la visita del 14-Ago como ensayo de alta satisfactorio cuando el `BVM-IR004` dice que no pudo ejecutarse, y los once informes conservan `Revision No. 0` en su campo de revisión. **Correo ENVIADO el 31-Ago** en español por la cadena del Request 006, a Carlo Montecinos, con el registro consolidado de las nueve jornadas como adjunto (`ADASA-BV-REGISTRO-INSPECCIONES-Rev0`, cinco páginas). Plazo al viernes 4 de septiembre (`BV-25`). **Lo favorable, que también consta:** el inspector asistió a las nueve jornadas, firmó los registros, revisó los certificados y fotografió los escalones; y los dos ensayos de baja presión del 27 y del 28 están bien ejecutados y **cierran la parte de baja presión del alcance que el Inspection Request 003 recortó el 5 de agosto** (`PRG-13`, cierre parcial). El frente quedó ordenado en `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/` con una carpeta por informe, deduplicado por hash, y con los cinco informes que nunca se habían analizado ya revisados; registro en `_REGISTRO_INSPECCIONES_BV.md`.
- **Master Register:** **68 Code 1 / 19 Code 2 / 2 Code 3 / 0 Code 4** · **113 items / 89 delivered** · **39 TMs / 92 entregas** — cifras al cierre del **TM N39**, aplicado con `update_register_n39.py` tras el envío del 9-Sep: tres re-revisiones, ningún ítem nuevo y **dos cambios de código que se cancelan entre sí**. La Valve List baja de Código 1 a Código 2 por el material de `VM-09-065`, y el procedimiento de radiografía sube de Código 2 a Código 1 al llegar en Rev 0, de modo que el tally no se mueve. **El tally esperado se declaró en la cabecera del script antes de correrlo y el obtenido coincide.** Gate `openpyxl_lint.py` en exit 0. 🔴 **La misma corrida corrigió la fila del `P22-CD-09-005-001`**, que el registro tenía en Rev B cuando los transmittals N37 y N38 lo declaran emitido en Rev 0 desde la E71. **El veredicto de esa fila no se tocó**, porque la E71 se respondió por correo y sin códigos: ningún transmittal emitió veredicto sobre esa Rev 0 y escribirlo sería inventarlo. Antes, con `update_register_n38.py` tras el envío del 3-Sep: once re-revisiones, ningún ítem nuevo y **seis cambios de código**. Suben a Código 1 el procedimiento de líquidos penetrantes, los dos turbochargers y la Equipment List; suben de 3 a 2 el ultrasonido y el procedimiento de FAT del tablero. **El tally esperado se declaró en la cabecera del script antes de correrlo y el obtenido coincide.** Gate `openpyxl_lint.py` en exit 0. **Los dos únicos Código 3 que quedan en el proyecto son el O&M Manual y el índice del dossier, que son dos de los cinco documentos que no llegaron.** (`REVISIONES/EVALUACIONES/P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx`). Cifras al cierre del **TM N37**, aplicado con `update_register_n37.py` tras el envío del 31-Ago: siete re-revisiones con veredicto, ningún ítem nuevo, y **cuatro cambios de código**. Suben a Código 1 los dos documentos emitidos para construcción, la I/O List Rev 6 y el Tie-In Point Layout Rev 0; suben de Código 3 a Código 2 los dos procedimientos de ensayos no destructivos que volvieron y el Instrument Location Layout, que arrastraba el Código 3 desde el TM N23; y baja de Código 2 a Código 3 el registro del FAT del tablero. **El tally esperado se declaró en la cabecera del script antes de correrlo y el obtenido coincide.** Gate `openpyxl_lint.py` en exit 0. **Los cuatro Código 3 que quedan abiertos** son el procedimiento de espesor por ultrasonido, el O&M Manual, el índice del dossier y este registro del FAT. **El ítem 65, el Dossier de Fabricación y Pruebas como entregable, sigue en NOT DELIVERED.** El bloque `ITEMS BY SECTION` arrastra un descuadre heredado de un entregado de más; el updater lo reporta en cada corrida y no lo agranda.
- **Baseline schedule:** 05-Mar-2026 (ver Referencias Durables).
- **Frentes abiertos:** **Inspección de taller Bureau Veritas** — V1 ejecutada el 28-Jul en Penang con informe IR001 y 31 lecturas de PMI conformes; la **jornada del Request 002 se ejecutó el viernes 07-Ago** —fabricación de spools súper dúplex, líquidos penetrantes en raíz y peineta, marco del skid, y revisión de WPS y calificación de soldadores, la primera con soldadura ejecutada— y **tres días después no ha llegado ningún registro**: pedidos el 10-Ago por correo conjunto a BW Water y Bureau Veritas, con el precedente de que la V1 devolvió informe y anexos al día siguiente. Más dos jornadas nuevas el **13 y 14 de agosto** avisadas con 8 días contra los 30 de la Cláusula 37; **confirmación de V2–V6 a BV vencida desde el 24-Jul**; alcance mínimo del FAT y reunión de Kick-off sin respuesta, y la aritmética del FAT no cierra (del 15 al 18-Sep hay cuatro días para siete jornadas contratadas). **Dossier de fabricación y pruebas** — llegó el índice (E69) pero **ningún registro**; el ítem 65 sigue `NOT DELIVERED` y sostiene los ítems 8.3 y 8.4 del PIE, de los que depende el 40% del pago; BW Water reencuadra el alcance como "technical submittals", en disputa. **Atraso Fedco** — bomba HP y dos turbochargers con embarque comprometido al 21-Ago y llegada a Penang el 02-Sep; el reporte de causa raíz pedido para el 03-Jul lleva 32 días de mora. **Panel PLC** — entrega al taller el 23-Ago; pruebas en curso. **Familia de Control y O&M Manual** — reemisión coordinada a Rev 0 pendiente. **Comercial** — Carta de Aumento de Monto por USD 56.990,50 emitida el 04-Ago sin declarar su composición (repuestos USD 51.224,50 más adicional CIP USD 5.766,00); el fondo de la reemisión de repuestos sigue sin responder y la propuesta vence el 28-Ago; factura 25007-02 por USD 86.982,60 a pagar el 15-Ago; el adicional CIP rev.3 es la rev.2 re-datada. **Despacho/packing EXW** — respuesta que reserva el packing cost sigue en BORRADOR. **Reportería** — el **informe de avance semanal sí llega** (último, la semana 31, del 27-Jul al 2-Ago, en el paquete del 3-Ago); lo que falta es el **DDSR**, ausente de los paquetes del 27-Jul y del 3-Ago, con el último fechado el 20-Jul. El paquete de esta semana tampoco había llegado al 10-Ago, cuando se preguntó por escrito. El Change Log del tracker lleva cuatro versiones vacío mientras las fechas se mueven, aunque el archivo sí cambia de contenido cada semana.
- 🔴 **Correo entrante EN HOLD.** La captura por navegador exige intervención humana constante y no escala; 4 correos capturados y 22 identificados sin capturar. El desbloqueo es un interruptor: `UseNewOutlook = 1` impide que arranque Outlook Classic y con él todo el puente COM. Ver `CORREOS/_RECIBIDOS/_LEEME.md`.
- 🔴 **El paquete de izaje sigue incompleto. BW Water mandó el lunes 14 un addendum de una hoja que repite las reacciones del Rev 0 sin una sola cota, y la respuesta de ADASA del martes 15 fija el jueves 17 de septiembre con la ET adjunta.** La orden a Thomas Engineers se liberó recién el 14, así que la revisión estructural tampoco llegó. Antecedentes: BW Water respondió el 11-Sep, ADASA fijó el 15 y el lunes 14 salió un recordatorio. ADASA iza el módulo en Taltal con grúa propia (ET Sección 9, pág. 34; montaje en sitio por ADASA, Sección 3, entrega Ex Works), y la Sección 7 pág. 29 exige dentro del Manual de Montaje la memoria de cálculo de izaje, el plano de izaje con los pesos y el plano y diseño del yugo: **ninguno recibido**. La respuesta de Eduardo Yamauchi (9:18, tres comentarios `DWNT`, firma De Nora Water Inc) **declara la ruta**: esquineros ISO del contenedor, sin padeye, con los criterios de FS 2,0 y 5 % lateral como referencia para *"the lift points and members at the lift point"*; **admite que el izaje superior necesita un lifting frame**, que es el yugo de la ET; recomienda izar por abajo a 30° con accesorios de mercado, lo que **contradice su hoja de comentarios del 24-Jun** a los Criterios Rev B (*"spreader beams will be needed so that only vertical forces are induced at the lifting points"*), base sobre la que el TM N25 aprobó los criterios; y reasigna el detalle al *forwarder / rigging team* citando un correo previo que no existe en los registros. No respondió la fecha del profesional, ni si la revisión cubre el izaje, ni las cuatro piezas, ni el peso. **La Figura 15 del Rev 0, verificada por render, lleva las cuatro eslingas inferiores a dos puntos sobre el techo, uno por costado**: el izaje inferior también depende de un arreglo de gancho que hay que construir. **Respuesta de ADASA ENVIADA el 11-Sep** desde `CORREOS/Septiembre 2026/2026-09-11/`: el yugo es para el izaje en sitio y por eso la ET pide su diseño y no el yugo; se toma la ruta declarada y se exige la verificación local del punto bajo la excentricidad de la carga, porque hoy solo está el izaje global, validada por el profesional; paquete el **15-Sep**, día en que vencen los cuatro días del profesional; se acepta la oferta de revisar el lifting plan y se pide que queden en contacto con el forwarder y le compartan el procedimiento de izaje como base. Palancas en el cuerpo: solo Sección 7 pág. 30 y Sección 8.1; la BAE 43.1 a) y d) quedan en el `PRG-49` y en la Sección 3 del próximo transmittal.
- 🔴 **La ingeniería aprobada no está emitida para construcción: 46 de los 72 documentos siguen en revisión de letra, y 34 de ellos no tienen ninguna observación abierta.** Auditoría documento por documento de los 113 entregables del Master Register al cierre del TM N38, en `REVISIONES/EVALUACIONES/_AUDITORIA_REV0_2026-09-09.md`. Mediana de **184 días** desde la aprobación y **cuatro documentos con 267**, desde el primer transmittal. **La regla la escribió BW Water**, en la hoja de comentarios del `P22-DWG-09-007-003` Rev E: mantiene *Issued For Approval* hasta la aprobación y entonces cambia a *Issued For Construction - Rev0*; ese plano lleva Código 1 desde junio y va por la Rev F. El proveedor somete el **87 % para aprobación y no para construcción**, con un código `IFA` que su propio formulario no define, y **once documentos en revisión numérica conservan el cajetín de aprobación**. 🔴 **El registro con que el proveedor gestiona la revisión no mide la emisión**: el DDSR no tiene columna de revisión 0 ni de IFC, su ponderador da 100 % a un aprobado sin mirar la revisión, y **34 de los documentos sin emitir figuran ahí al 100 %**; además declara dos planos en revisión 0 que nunca llegaron. 🔴 **El reclamo viaja con el Transmittal N39 y no como correo aparte.** Por decisión del usuario los dos borradores del 9 de septiembre se fundieron en **un solo correo ejecutivo**, y las cuatro tablas pasaron a ser la **Sección 3 del transmittal**, que es el instrumento contractual que las sostiene. Es el precedente del N37, cuyo correo llevó una exigencia de igual peso en 72 palabras y mandó la lista nominal al transmittal. **El correo se envió el 9 de septiembre** y exige **todo emitido en revisión 0 al viernes 11**, la fecha que la reunión de ese día fijó para el cierre documental, con fecha comprometida en el DDSR para lo que no alcance. Con ese envío quedó fijado el compromiso `PRG-48`, que hasta entonces figuraba sin fecha a propósito. El idioma, el hito de pago y la liberación de despacho quedaron fuera por decisión del usuario, con reserva genérica de derechos en el cierre.
- **La ingeniería del módulo de BW Water está disponible para el equipo en un dossier por especialidades.** `BASES DE LICITACION MONTAJE MECANICO-OOCC/INGENIERIA MODULO BW WATER/`, **71 documentos en 78 archivos y 340 MB**, cada uno en la última revisión aprobada, ordenados por la disciplina de su propio código: general, proceso, mecánica, cañerías, electricidad, y control e instrumentación. **59 en Código 1 y 12 en Código 2**, sin ningún Código 3 en ingeniería. Se reconstruye corriendo `catalogar_ingenieria_bw.py` y `construir_dossier_bw.py`, que leen el Master Register y verifican cada copia por SHA256; el gate quedó en verde. La **NT `P22-NT-06-000-002-0`** de 16 páginas es el documento de control: declara la condición abierta de los doce Código 2 y los seis entregables de ingeniería que siguen sin recibirse. 🔴 **El armado destapó ocho discrepancias entre el Master Register y el documento emitido** —tres datasheets de estanques con el correlativo corrido, dos especificaciones en la disciplina equivocada, los dos planos de turbocargadores que son revisión A y no B, y el plano de puntos de conexión bajo la entrega 87, que no existe—: manda el documento, y **corregir el registro queda pendiente**. 🔴 **BW Water nunca ha entregado un listado en formato editable**, de modo que el dossier es cien por ciento PDF; el modelo Navisworks se entrega por enlace.
- 🔴 **Montaje adjudicado: el paquete de ingeniería vigente suma las carpetas `4. SITIO` y `5. EQUIPOS` (planos y folletos de proveedor del estanque, la bomba y las válvulas) y un índice Excel en su raíz; la Nota Técnica queda para revisión del equipo.** `BASES DE LICITACION MONTAJE MECANICO-OOCC/INGENIERIA VIGENTE PARA CONSTRUCCION/`, **63 documentos en 166 archivos** (6,5 GB con la nube de puntos), cada plano de ingeniería en PDF y DWG, sin Bases ni Formato, que son contractuales y no se reemiten. Reconstruido el 14-Sep con 170 copias verificadas por SHA256, **autochequeo de cinco reglas y gate de vigencia en verde**. El dossier civil lleva **8 láminas en Rev 1 y 10 en Rev 0**; las cinco que L&A reemitió el 10-Sep en la misma Rev 1 (carta TT-016) rigen identificadas por carta y fecha, con la anterior archivada. **El módulo subió 250 mm**; la fundación del sistema CIP baja de 7,36 a 5,80 m³ y 🔴 **la excavación común de 115,10 a 90,64 m³** sobre 75,53 excavados: los 115,10 eran volumen esponjado sobre una partida que se paga por m³ excavado. **Seis de las siete discrepancias del 9-Sep cerraron sobre los planos; la séptima era un error de lectura de ADASA** (el M.H.A. de la fosa es el muro, no un mejoramiento) y la nota se corrigió. **La NT `P22-NT-06-000-001-0`** (17 páginas, único documento de control, absorbió la planilla) declara las cantidades que rigen y de qué plano sale cada una, sin narrar el ciclo de comentarios. 🔴 **La cubierta CIP: su fundación sí está cotizada** (partida 4.3, 2,38 m³, con los 24 pernos F-1554); la estructura metálica no tiene partida y la ejecuta ADASA después. 🔴 **El Formato viajó con los precios de ADASA como fórmula visible** y **repite dos códigos de partida**; está adjudicado y no se corrige, así que la NT lo declara y fija la cita por número más nombre completo. **Pendiente:** enviar el correo al equipo (comentarios al viernes 11) y, con ellos, emitir al contratista; pedir a Van Doorn el ploteo de la Rev 1 del P&ID de alimentación, que hoy solo existe como DWG y no entra al paquete (la nota declara la Rev 0 sin excepciones).
- **Streams:** BW Water (inglés, TM N1–N39) · OOCC/L&A (español, TM N1–N4; ENTREGA 15 incorporada sin transmittal) · Montaje Mecánico-OOCC (**adjudicado**; ingeniería vigente para construcción, NT N1).

## Bitácora Cronológica

> Trazabilidad de todo lo generado: transmittales, correos, notas técnicas, RFIs y decisiones. **Más reciente primero.** Formato de entrada: `### AAAA-MM-DD — Título — ESTADO`.

### 2026-09-17 — Plantilla del Transmittal N40 para que Victor Gutierrez revise el procedimiento FAT del módulo — INTERNO

BW Water anunció en la reunión del 17 (minuta `P22-MI-10-000-002-0`) que el viernes 18 envía el procedimiento FAT del módulo, preparado sobre la fila 7 del ITP. Luis Rivera sale dos semanas, y la revisión la hace y la emite **Victor Gutierrez, en Word a mano**. Quedó armado en `REVISIONES/TRANSMITTALES/P22-TM-09-000-040-0/`:
- `TRANSMITTAL N40 ADASA-BW_WATER_PLANTILLA.docx`, en inglés, con marcadores resaltados. Lo fijo es el contexto contractual del procedimiento (ET Section 8.1 y fila 7.1 del ITP como Hold Point) y tres bloques Action alternativos. 🔴 **Versión ejecutiva solo del FAT, por decisión del usuario:** cuatro secciones, sin la de pendientes de transmittales anteriores.
- `_GUIA_REVISION_FAT_N40_NO_ENVIAR.docx`, en español. Trae los pasos, el plazo, una pauta de 21 filas contra la ET 8.1, el ITP Rev 0 y la PIE Base, lo que no se observa, el criterio de código, la convención del PDF anotado en Acrobat, el chequeo previo y el texto del correo de cobertura.
- Los scripts `crear_plantilla_tm40.py` y `crear_guia_n40.py` y el espejo `.md`, como respaldo.

**Decisiones del usuario:** número N40, porque el N39 ya salió; solo el procedimiento FAT; Victor Gutierrez en las tres casillas del cajetín; PDF anotado a mano en Acrobat.

**Verificado contra la fuente.** La ET Sección 8.1 exige escenarios de falla simulados y da tres como ejemplo, sin fijar una lista cerrada. La minuta del 17 no fija fecha de respuesta de ADASA, y con recepción el 18 la Cláusula 37.2 vence el martes 29-Sep.

**Pendiente.** Los pendientes de transmittales anteriores y el error de registro de los GA de los turbos (`P22-DWG-09-005-012` y `-013`), que la entrada del 16-Sep dejó para el próximo transmittal, pasan al N41. Al volver: Master Register, `PRG-50`, `BV-13`, `H-03` y reconciliación del `.md` con el Word emitido.

### 2026-09-17 — Reunión de seguimiento con BW Water: los spools se cortan en paralelo y el procedimiento FAT llega el 18 — GENERADO

Minuta `MINUTAS DE REUNION/P22-MI-10-000-002-0/`, en inglés y con template ADASA, generada desde la transcripción Plaud `2026-09-17 MINUTA BW WATERS` (30 minutos, 09:30 de Chile). El resumen automático `REUNION 17-09-26.pdf` quedó extraído en `MINUTAS DE REUNION/md/`, pero manda la transcripción. Mismas reglas que la minuta del 16: solo lo dicho y sin nombres internos de BW Water. **No enviada al cierre.** La minuta del 16, `P22-MI-10-000-001-0`, no tiene entrada propia en la Bitácora.

- **Spools del turbo.** El informe escrito no llegó. BW Water dice de palabra que el turbo cumple el modelo 3D y que solo dos spools de la conexión superior chocan, y atribuye el desfase, sin confirmarlo, a su largo e inclinación. La explicación del 16, un turbo distinto a los planos de Fedco, la descartó el propio BW Water. Plan: planos corregidos y corte el 18, raíz el 19, PT el 21, hidrostática el 22 y remontaje el 23.
- 🔴 **ADASA aceptó que el corte y la soldadura avancen en paralelo con su revisión de los planos**, para no perder dos o tres días con el feriado, a condición de recibirlos y pasarlos de inmediato a Bureau Veritas. No quedó reserva de que ese trabajo corre por riesgo de BW Water. Siguen sin respuesta si la corrección se hace en el modelo Plant 3D o en el CAD, y cuántas líneas están afectadas.
- **Procedimiento FAT:** preparado el 17, en revisión interna, a someter el 18. ADASA lo quiere aun preliminar, para Bureau Veritas y como base del procedimiento de pruebas en sitio.
- **Izaje:** la orden al profesional chileno está emitida sin confirmación, y los cálculos y planos del yugo apuntan al 18.
- **Programa:** el FAT se reprograma con el cronograma que BW Water emitirá el 23 o 24-Sep, cuya última estimación fue el 10-Oct. El embarque queda en espera hasta recibirlo, y el forwarder pide una semana de aviso.
- **Bureau Veritas** visita Penang el 18, y ADASA pidió a BW Water darle acceso a toda la información.
- **Contacto:** Victor Gutierrez lleva la comunicación durante la ausencia de Luis Rivera y enviará la coordinación del despacho de membranas la semana del 21.

La transcripción del 17 no permite decir qué turbo está afectado; la identificación como interetapa sigue siendo la de las fotos del 16.

**Registro de Compromisos** (corte 17-Sep): `PRG-51` con las respuestas verbales y la decisión de cortar en paralelo; `PRG-50` con el procedimiento al 18 y la plantilla del N40; `PRG-49` vencido el 17, sin mover la fecha porque las nuevas son verbales; `BV-13` y el hito `H-03` con el FAT a reprogramar; `BV-26` con el acceso pedido para la visita; y `PRG-52` nuevo. Excel regenerado con `openpyxl_lint.py` sin hallazgos. `compromisos.yaml` vuelve a fin de línea LF, como está en git.

### 2026-09-16 — El turbo interetapa no calza con sus spools, y la respuesta a BW Water con la trazabilidad de los planos de fabricación — ENVIADO

🔴 **El reporte semanal del lunes 14 lo registró en una línea y la reunión del 16 lo hizo grave.** El correo de Eduardo Yamauchi del 14 a las 18:41 cerraba con que el tubo de conexión de los turbos quedó desplazado y requería modificación. En la reunión del 16 BW Water informó un desfase vertical y horizontal de unos 50 mm. Los spools se cortan, resueldan y reensayan, la reparación va al 23-Sep y el listo para despacho pasa al **12 de octubre**. El modelo tenía el desfase, según Eduardo, y Stephane lo atribuye a una diferencia entre el plano de Fedco y el turbo entregado. Por las fotos, el afectado es el **turbo interetapa**. Verificado en las hojas de datos Rev 0, es el que trabaja a la presión más alta del módulo: 84,8 bar a la salida de alimentación, contra 69,5 del de alimentación, sobre líneas de 90 barG de diseño y 135 barG de prueba. La minuta del 16 es transcripción automática y no es oponible.

**La trazabilidad, verificada contra cada fuente.** La ET Sección 7 exige las isométricas de alta presión a 90 días de la adjudicación. El Piping Layout se aprobó en Código 2 en su Rev B (TM N15), Rev C (TM N30) y Rev D (TM N36), y el modelo 3D en su Rev A (N30) y Rev B (N36). Según el usuario y su captura del modelo, en esos documentos las conexiones de los turbos calzan. **Los planos de fabricación oficiales nunca se emitieron.** BW Water los emitió internamente el 24 de julio (su correo del 28). El N30 los devolvió como no recibidos y la Rev D del layout los retiró. El N37 los exigió al 3-Sep, el N38 los registró como no recibidos, el correo del 8 los volvió a pedir y en la reunión del 9 se comprometieron para el 11. El N39 lista las isométricas como no recibidas.

**Correo ENVIADO el 16-Sep** (hora pendiente de registrar desde el respaldo) desde `CORREOS/Septiembre 2026/2026-09-16/`. Reply-All sobre el reporte Week 37, con Victor Gutierrez agregado en copia. En inglés, versión ejecutiva de 426 palabras, con tabla de trazabilidad de diez filas y la captura del modelo 3D embebida. Lleva doce PDF adjuntos en `ADJUNTOS_Turbocharger-Spool-Offset/`. **Pide seis cosas para antes de la reunión del 17 a las 08:30:**
- turbos y spools afectados, con los desfases;
- planos de taller e isométricas de esos spools, sin cortar ninguno antes de que ADASA los reciba;
- causa raíz contra el contorno de Fedco y el modelo 3D;
- conformidad de los dos turbos con sus hojas de datos Rev 0 y GA actualizados;
- reensayo completo de cada línea de alta conectada a los turbos, fuera del contenedor, con Bureau Veritas según la fila 5.2 del ITP;
- cronograma de recuperación día a día.

Toma nota del 12-Oct con la prioridad de despachar en cuanto el módulo esté listo, sin renunciar a derechos, y nombra las Cláusulas 27 y 43.1 b) sin cifras.

🔴 **Tres decisiones del usuario en la redacción.**
- **La fecha no se rechaza.** *"Not accepted"* se leía como que ADASA no quiere el despacho.
- **No se escribe que los spools se fabricaron con planos nunca sometidos a ADASA.** Dejaba mal a ADASA. Se escribe lo emitido y revisado frente a lo nunca emitido.
- **No se abre el error propio de los GA de los turbos.** `P22-DWG-09-005-012` y `-013` Rev A quedaron en Código 3 en el TM N10 y nunca se reemitieron, pero el Master Register los registra como Rev B aprobada y la Tabla 1 del N39 los dio por aprobados. Por eso el PDF del N39 no va adjunto y el correo no califica esos planos. Queda para corregir en el próximo transmittal.

**Bureau Veritas.** El Request to witness inspection 008 tiene la jornada del 17 en ensayo de alta presión y la del 18 en instalación de equipos. El primer borrador para Bureau Veritas quedó para el 17 y el usuario lo eliminó sin enviarlo para cambiar el enfoque. El correo nuevo, `2026-09-16_BV-Survey-Turbocharger-Offset.docx`, va a Jaime Martínez, administrador de contrato de Bureau Veritas Chile, con copia a Carlo Montecinos, Luis Rodrigo Arcila, Magdier Arias, Eduardo Yamauchi, Lokman Hakim Bin Mat y Victor Gutierrez. Mantiene la prueba del 17 sin las líneas de los turbos. Pide un levantamiento desde el 18: causa raíz del desfase (fila 4.2 del ITP), equipos y conformidad de los turbos con sus hojas de datos Rev 0 (4.1), instrumentos (4.3 y 4.4) y otros temas constructivos. Pide además un informe eléctrico aparte (6.1 a 6.3), y que Bureau Veritas proponga las jornadas dentro de las contratadas para aprobación de ADASA. Lleva nueve PDF esenciales y 16,9 MB, incluido el correo a Eduardo exportado con Word y el Progress Report Week 37. **ENVIADO el 16-Sep** (hora pendiente de registrar desde el respaldo). La versión final tiene 286 palabras y está en la voz del usuario, pasada por `anti-ia` modo revisar. En la redacción el usuario pidió declarar de frente su ausencia de dos semanas, porque la frase de traspaso a Victor sonaba a esconderse, decir que los antecedentes van adjuntos y cerrar agradeciendo la gestión. Compromisos nuevos `BV-26` (levantamiento, con informe al día siguiente de la visita del 18 según la oferta y la propuesta de jornadas) y `BV-27` (informe eléctrico aparte, sin fecha).

**Registro de Compromisos:** `PRG-51` nuevo, CRÍTICA, fecha 2026-09-17, con los seis puntos como criterio de cierre. `PRG-21` y `BV-13` actualizados, con el FAT fuera de la semana del 21. Excel regenerado y `openpyxl_lint.py` sin hallazgos. `anti-ia` modo revisar en cinco pasadas, VERDE, con el veredicto en `.anti-ia-2026-09-16/`.

### 2026-09-16 — El procedimiento FAT del módulo nunca se sometió, y el correo que lo exige con la trazabilidad desde mayo — ENVIADO

🔴 **BW Water nunca entregó el procedimiento FAT del módulo, y el FAT es la semana del 21 de septiembre.** Se barrieron las 93 entregas de `ENTREGAS_BWWATER/`: 933 archivos por nombre, incluidos los diez comprimidos sin descomprimir, y 390 PDF únicos por texto. El único procedimiento FAT recibido es el `P22-PP-09-000-001`, que va por la Rev C (E64, E88 y E90) y cubre solo el hardware del tablero PLC/LCP. Su Section 3 excluye las pruebas funcionales de software y la verificación de lógica de proceso. El `PROV-PROC-FAT-001` que exige el ITP no aparece en ninguna entrega.

**Lo que lo exige y lo que lo dejó constando, verificado contra cada fuente.** La ET Section 8.1 pone la aprobación del procedimiento detallado como primer ítem del alcance mínimo del FAT. La fila 7.1 del ITP `P22-BA-09-000-004` Rev 0 (Código 1 en el TM N26) es Hold en la columna de ADASA, y las filas 7.2 a 7.5 y el Acta de la 7.9 se ejecutan contra ese procedimiento. El índice del dossier Rev B (E77) lista el capítulo B11 como la única entrada de su sección B sin código. El Progress Update del 28-Ago programa el FAT (ID 419) del 15 al 25 de septiembre, sin actividad para el procedimiento. Se levantó en el TM N17 (5-May), N19 (25-May) y N20 (10-Jun). El N37 lo exigió al 3-Sep, el N38 lo registró como no recibido y el correo del 8-Sep pidió su fecha de emisión. **El TM N39 lo dejó de arrastrar.** El DDSR no sirve de evidencia, porque no lista ningún procedimiento de calidad.

**Correo ENVIADO el miércoles 16-Sep** (hora pendiente de registrar desde el respaldo) desde `CORREOS/Septiembre 2026/2026-09-16/`. Hilo nuevo, `URGENT - TALTAL: Module Factory Acceptance Test procedure required before the FAT`, a Eduardo Yamauchi con siete de BW Water y Victor Gutierrez en copia. En inglés, con 216 palabras y una tabla de trazabilidad de nueve filas. Plazo al **viernes 18 de septiembre**, que es feriado en Chile y hábil en Malasia. 🔴 **El orden del cuerpo lo corrigió el usuario:** el primer borrador abría con que el procedimiento nunca se sometió y hacía parecer que ADASA recién se acordaba a días del ensayo. Ahora abre con la obligación y los pedidos desde mayo, con la tabla a continuación. Después va el estado, *"still not been received"*, con la consecuencia en negrita: *"The FAT cannot formally open until the procedure is approved"*. Cierran por qué el Rev C no lo cubre y el pedido. **Por decisión del usuario no menciona el plazo de revisión** de la Cláusula 37.2, que sometido el 18 vencería después del embarque del 28. `anti-ia` modo revisar en dos pasadas, VERDE, con el veredicto en `.anti-ia-2026-09-16/`.

**Registro de Compromisos:** `PRG-50` nuevo, CRÍTICA, fecha 2026-09-18 FIJADA ADASA, con origen en el TM N17. Excel regenerado con respaldo en `_backups/` y `openpyxl_lint.py` sin hallazgos. **Pendiente:** archivar el respaldo del enviado con su hora y reponer el punto en la Sección 3 del próximo transmittal.

### 2026-09-15 — BW Water manda un addendum de izaje que repite el Rev 0, y la respuesta de ADASA fija el jueves 17 — ENVIADO

**Eduardo Yamauchi respondió el lunes 14 a las 23:04 con un addendum de una sola hoja técnica.** Es el `P22-CD-09-005-003_UHPRO Structural Calculation Report - Addendum_RevA`, de Aulem en estado FOR REVIEW. Escribió que la orden al profesional esperaba ese documento, que se liberó ese día y que espera que "Eng. Thomas" acepte incluirlo en su alcance. "Eng. Thomas" es Thomas Engineers. 🔴 **La orden se liberó el 14 y no el 9**, así que los cuatro días del profesional recién empiezan y la revisión estructural tampoco llegó el 15. El correo quedó capturado en `CORREOS/_RECIBIDOS/Septiembre 2026/`, con el adjunto movido desde la raíz del proyecto (md5 idéntico) y el registro regenerado.

🔴 **El addendum repite el Rev 0 y no se puede fabricar.** Las cuatro cargas verticales de su Figura 16 son las reacciones de la Condición 1 del `P22-CD-09-005-001` Rev 0 a 2,0 D (nodos 126 a 129, diferencia máxima 0,08 kN), y su peso vacío de 100,80 kN es esa suma dividida por 2,0. Lo nuevo es un lifting frame de cuatro W10x49 en A36, gancho único sobre el centro de gravedad, eslingas a 45° como mínimo e izaje de prueba, con lo que **BW Water designa de hecho el izaje superior con marco**. La figura no tiene una sola cota. Tres defectos documentales quedan para la Sección 3 del próximo transmittal: usa el código de los Criterios de Diseño en Rev 0, dice Rev A en la portada y Rev B en la cabecera, y "Page 2 of 2" en un archivo de tres páginas.

**Respuesta de ADASA ENVIADA el martes 15** (hora pendiente de registrar desde el respaldo), en Reply-All con los siete CC de BW Water más Victor Gutierrez y la ET completa adjunta. Es una versión ejecutiva de 224 palabras, pedida por el usuario sobre una primera de 432. Pide que la revisión de Thomas Engineers cubra el paquete completo y que manden su fecha. Declara que el addendum no completa el paquete porque repite las reacciones del Rev 0 sin cotas, y cita la Section 7 pág. 29 con los tres entregables del Manual de montaje literales. Exige un plano del yugo de fabricación y la verificación local pedida el 11-Sep, con **paquete completo el jueves 17 de septiembre** ligado a la Sección 7 pág. 30.

**Decisiones.** La ET no pide "maniobra de izaje", y no se exigió. El plazo va sin el cálculo de los siete días hábiles, porque con el feriado del viernes 18 la revisión cerraría el 29, un día después del embarque. La reserva de derechos sigue en el hilo desde el 11-Sep. Gate `anti-ia` en VERDE, Caso B, en la voz del registro de correspondencia: mediana de oración 20,5 contra 18 y paréntesis en 5,9 por mil contra 6,18.

**Artefactos:** `CORREOS/Septiembre 2026/2026-09-15/` con `crear_correo_izaje_addendum.py`, `2026-09-15_Lifting-Addendum-Reply.docx`, su `_Descripcion.md` y `.anti-ia-2026-09-15/veredicto.md`. También el `_correo.md` del 14-Sep con el addendum en su carpeta `adjuntos/`, y el `PRG-49` con la fecha al 17-Sep fijada por ADASA, sin reprogramación por la regla escrita el 11-Sep, más el criterio de cierre ajustado al plano de fabricación del yugo. Excel del registro regenerado con lint en cero y memoria `project_izaje_yugo_modulo` actualizada.

### 2026-09-14 — Paquete de ingeniería vigente: carpetas 4. SITIO y 5. EQUIPOS, títulos de la Nota Técnica e índice Excel — GENERADO

**El paquete que se entrega al contratista de montaje lleva ahora los documentos de proveedor de lo que ADASA le suministra.** `5. EQUIPOS` tiene tres subcarpetas: el plano de fabricación Exfibro **EX-26005-F01 Rev 0** del estanque TK-06-001 ("Aprobado para fabricación" del 12-03-2026), el arreglo general **KSB-AAF-KNCPP11-050+160M Rev A** de la bomba BH-06-001 en PDF y DWG, y para las válvulas el dibujo **DWG-1206D-RV01** de la check de 4" (VATAC vía KSB, VR-06-001 y VR-06-003) con los folletos ISORIA 10, MS/MC y ALS 200. KSB nunca emitió plano de las mariposas por diámetro, así que el folleto de la serie es su documento dimensional. Las fuentes las fijó el usuario: `INGENIERIA DE DETALLE OOCC/ANTECEDENTES/03_EQUIPOS_CON_IMPACTO_CIVIL/` y `INGENIERIA DE DETALLE MECANICA/PLANOS VALVULAS/`. **Decisiones:** la Rev 0 del estanque en lugar de la Rev C de antecedentes, porque es la que citan la fundación P22-DWG-00-002-002 LAM1 Rev 1 y el Anexo B de la ET A12; las ofertas KSB quedan fuera por traer precios, y la memoria Exfibro también. `4. SITIO`, que se había copiado a mano y hacía fallar el autochequeo y el gate, entra al script.

🔴 **Tres hallazgos reportados y no corregidos.** Los pernos de la bomba difieren en cuatro documentos: M16 "no incluido" en el plano KSB, PA-1 de 5/8" HAS-V-36 postinstalado en la fundación LAM4 Rev 1, "suministrados por ADASA" en la ET A12 y a cargo del contratista en el BL. La memoria Exfibro Rev 0 del 26-May recalcula el anclaje del estanque a 7/8", mientras el plano Rev 0 y el PA-2 de la LAM2 siguen en 1", del lado seguro. El BL cita la Rev C del estanque.

**La Nota Técnica** pasa a seis carpetas, 63 documentos y 166 archivos, con un párrafo para cada carpeta nueva; el de `5. EQUIPOS` declara que el anclaje de los dos equipos lo fijan los planos de fundación. Sus once títulos narrativos pasaron a frase nominal por instrucción del usuario ("tiene que ser serio, di lo que cambia y punto"), y la tabla de vigencia sale con ortografía completa. Son 17 páginas, con PDF desde Word copiado a `0. CONTROL DE CAMBIOS`; `anti-ia` en VERDE sobre los párrafos nuevos.

**Índice `00_INDICE DEL PAQUETE.xlsx`** en la raíz del paquete, con 64 documentos: una fila por documento (PDF y DWG juntos), bandas por carpeta y subcarpeta, y columnas de código, documento, revisión y formato. Solo ubica documentos; los cambios y la vigencia siguen en la nota.

**Scripts y gates.** `construir_paquete_construccion.py` suma `dossier_sitio()` y `dossier_equipos()`, la regla 5 (un solo contenido por plano de proveedor, que también viaja en los anexos de la A12), la regla 3 ampliada a ofertas y correos, y `real()`, que resuelve fuente y destino por nombre normalizado: en el Mac mini el NAS devuelve las tildes en NFD y 16 fuentes salían como faltantes. `generar_ingenieria_vigente.py` acepta revisiones de proveedor (`Rev0`, `_A`, `RV01`) sin regresión sobre los 88 pares previos. El nuevo `generar_indice_paquete.py` trae gate propio: todo archivo del paquete cae en una sola fila. Reconstruido con 170 copias verificadas por SHA256, con autochequeo de cinco reglas, gate de vigencia (63 documentos sin diferencias) y lint en verde.

**Artefactos:** `INGENIERIA VIGENTE PARA CONSTRUCCION/5. EQUIPOS/` con su `LEEME.txt`; `00_INDICE DEL PAQUETE.xlsx`; la NT en `.md`, `.py`, `.docx` y `.pdf`, con `.anti-ia-2026-09-14/veredicto.md`; y `BORRADOR_REV0/script/` con `construir_paquete_construccion.py`, `generar_ingenieria_vigente.py` y `generar_indice_paquete.py`.

### 2026-09-14 — Recordatorio a BW Water del paquete de izaje y pedido del enlace de la reunión del 16 — ENVIADO

**BW Water no respondió nada al correo del 11 y el paquete vence el martes 15.** ADASA envió el lunes 14 un recordatorio de 106 palabras en la misma cadena, Reply-All sobre su correo del 11 y con los mismos ocho destinatarios (hora pendiente de registrar desde el respaldo). Reitera el 15 como fecha última y nombra las dos confirmaciones que BW Water no dio: que la revisión del profesional cubre el izaje del módulo, y la condición de izaje en sitio que designe, con el yugo o arreglo diseñado para ella. Pide además el enlace de la reunión semanal, que no había llegado y esta semana debe ser el miércoles 16 a la hora habitual, con el paquete de izaje en la agenda. **No reabre sustancia ni suma palancas**: sin secciones de la ET, sin BAE 43.1 y sin cifras. Si el paquete no llega el 15, se registra como incumplimiento y se lleva a la reunión del 16, y el `PRG-49` suma reprogramación solo si BW Water propone otra fecha. Gate `anti-ia` en VERDE sin cambios, con confianza baja por largo.

**Artefactos:** `CORREOS/Septiembre 2026/2026-09-14/` con `crear_correo_izaje_recordatorio.py`, `2026-09-14_Lifting-Package-Reminder.docx`, su `_Descripcion.md` y `.anti-ia-2026-09-14/veredicto.md`; `PRG-49` con el recordatorio en su acción y en su historial de fechas, sin reprogramación; Excel del registro regenerado con lint en cero.

### 2026-09-11 — BW Water responde sobre el izaje: el yugo no es del forwarder, y la respuesta de ADASA fija el 15 de septiembre — ENVIADO

**Eduardo Yamauchi respondió el viernes 11 a las 9:18, en la misma cadena, con tres comentarios en rojo bajo el prefijo `DWNT` y la firma "De Nora Water Inc, Formerly BW Water Inc".** Respondió a lo del padeye y a lo del yugo, y empujó el resto al *forwarder / rigging team*. **No respondió** la fecha del profesional, si la revisión estructural cubre el izaje, las cuatro piezas pedidas ni el peso de izaje. Respaldo en `CORREOS/Septiembre 2026/2026-09-10/RE: TALTAL - Lifting package….pdf`; capturado en `CORREOS/_RECIBIDOS/Septiembre 2026/` con el registro regenerado.

**Lo que BW Water entendió mal es el eje de la respuesta: trata el yugo como accesorio de transporte.** El yugo es para el izaje que ejecuta ADASA en Taltal, con grúa propia, para posar el módulo en su fundación; por eso la ET pide a BW Water **el diseño y el plano del yugo, no el yugo**, que ADASA fabrica en Chile a partir de ese diseño. La cadena de secciones que lo sostiene: **Sección 3** (montaje en sitio por ADASA, entrega Ex Works), **Sección 9** pág. 34 (grúas alcance de ADASA) y **Sección 7** pág. 29 (los tres entregables dentro del Manual de Montaje, para aprobación). El forwarder transporta el módulo de planta contenerizado desde la fábrica hasta Taltal; posarlo en su fundación es el izaje en sitio, que es de ADASA.

🔴 **Las tres respuestas confirman más de lo que refutan.** (1) Sobre el padeye: los criterios *"were included to be used as reference in designing for the lift points and members at the lift point"* y un padeye *"will not be very useful"* porque el contenedor ya trae puntos de izaje. **Queda declarada la ruta**, esquineros ISO sin padeye, y declarado que FS 2,0 y 5 % lateral gobiernan el punto; el Rev 0 modela el izaje **solo como global**, reacciones en los nodos 126-129 y 3472-3473, sin estado tensional del punto. (2) Sobre el yugo: *"lifting from the top will require the slings to be vertical – this would need lifting frames"*, y por abajo bastarían *"container bottom lift lug accessories… available in the market"*. **Admite el lifting frame, que es el yugo de la ET**, y **contradice su propia hoja de comentarios del 24-Jun-2026** a los Criterios Rev B (ENTREGA 55, respuesta al TM N23 OBS-03): *"spreader beams will be needed so that only vertical forces are induced at the lifting points during lifting"*, base sobre la que el TM N25 aprobó los criterios; la misma hoja comprometía *"final weight, COG and max load at the lifting points to be provided after we finish the design"*, y el diseño salió para construcción el 23-Jul sin nada de eso. **La Figura 15 del Rev 0, verificada por render (pág. 18 de 548), lleva las cuatro eslingas inferiores a dos puntos sobre el techo, uno por costado**: el izaje inferior también depende de un arreglo de gancho que hay que construir y cuya geometría fija las tensiones. (3) Sobre el forwarder: *"as mentioned in our previous email"*, el detalle lo desarrolla el *forwarder / rigging team*; **ese correo previo no existe en los registros del proyecto** (barrido de todos los `.md` con cero apariciones de *forwarder* o *rigging* atribuidas a BW Water) y, por decisión del usuario, **no se menciona**.

**La respuesta de ADASA, ENVIADA el viernes 11 (hora pendiente de registrar desde el respaldo), en la misma cadena: un párrafo de encuadre, tres viñetas (una por cada respuesta de BW Water: *Padeye*, *Yoke*, *Forwarder and rigging plan*) y el cierre, 564 palabras, versión ejecutiva pedida por el usuario, con las tres fuentes del cierre nombradas antes que el dato.** El énfasis lo fijó el usuario: no hay objeción a usar los esquineros del contenedor, pero **la verificación local del punto bajo la excentricidad de la carga** (CG a 5.486 / 6.514 mm, tensiones de 88,5 a 129,2 kN) tiene que existir y quedar **validada por el profesional** de la revisión estructural. Se devuelve la admisión del lifting frame como el yugo de la ET, se cita la base aprobada del 24-Jun y la Figura 15, y se pide **designar la condición de izaje en sitio** y entregar el yugo o arreglo diseñado para ella. Las cuatro piezas del 10-Sep se mantienen. **Fecha fijada por el usuario: martes 15 de septiembre**, día en que vencen los cuatro días comprometidos el 9-Sep para el profesional, declarada en el correo como puesta para que puedan cumplirla y como **fecha última, sin margen después del 15**. Se toma el punto de la revisión del lifting plan del rigger y se pide que queden en contacto con el forwarder y le compartan el procedimiento de izaje como base. **Palancas en el cuerpo: solo Sección 7 pág. 30 y Sección 8.1**; la BAE 43.1 a) y d) —el Manual de montaje con el diseño del yugo es documento principal para la Recepción— quedan en el `PRG-49` y en la Sección 3 del próximo transmittal. Barridos en cero: `§`, grafía británica, *endorse / Chilean / registered* y *previous email*. **Gate `anti-ia` en VERDE tras estilización completa (Caso B)**: el original traía cinco punto y coma contra cero del registro de correspondencia, dos aperturas escindidas y la mediana de oración en 25 contra 18; la versión ejecutiva final mide mediana 18 contra 18, percentil 90 en 31 contra 35, cero punto y coma y paréntesis en 6,2 por mil contra 6,2, sin tocar contenido: el calce más exacto de la serie.

**Artefactos:** `CORREOS/Septiembre 2026/2026-09-11/` con `crear_correo_izaje_respuesta.py`, `2026-09-11_Lifting-Package-Reply.docx` y su `_Descripcion.md`; `PRG-49` con `fecha_comprometida: 2026-09-15` (origen FIJADA ADASA) y la respuesta del 11-Sep en su nota; Excel del registro regenerado con lint en cero.

### 2026-09-10 — La ENTREGA 15 de L&A cierra las discrepancias, el paquete de ingeniería vigente pasa a llevar los DWG y la Nota Técnica se corrige — GENERADO

> **L&A respondió el correo del 9 en un día.** La ENTREGA 15 (`067-032-032-COR-TT-016`, 10-Sep) trae las cinco láminas comentadas reemitidas **en la misma revisión 1**, con la fila `SE MODIFICA LO INDICADO 10/09/26` y nubes numeradas, más sus cuatro DWG, incluido el de movimiento de tierra de 24,7 MB que en la ENTREGA 14 fallaba la integridad. **Decisión del usuario: rige la Rev 1 de la carta TT-016**, identificada por carta y fecha, sin objetar la numeración porque nada había salido al contratista; la Rev 1 anterior quedó en `BORRADOR_REV0/_dossier_superseded_pre-E15/` con el sufijo de su carta. **Y no se responde a L&A**: el cierre es registro interno en el análisis del `P22-TM-00-010-005-0`.
>
> **Seis de las siete observaciones cierran de verdad, verificadas sobre los planos y no sobre la carta.** Los cuadros se unificaron: zona CIP en **1,03 m³** en los dos planos (L&A tomó la cifra del movimiento de tierra, no los 1,60 que ADASA venía declarando), contenedor en **20,95** en los dos (retiro 25,14, relleno de 30,03 a 13,96), el estanque baja su fondo a **EL. 5,30** y sube su excavación de 4,22 a **4,84**, y el cuadro de la lámina 1 pasa a diez ítems con la bomba (0,62) y la cubierta CIP (4,25). 🔴 **La OBS-05 la devolvió L&A como "no aplica", y tenía razón:** el rótulo `M.H.A. e=15` del plano de la fosa es el **muro de hormigón armado** de 15 cm, no un mejoramiento de suelo; bajo el sello +4,305 va emplantillado de 5 cm como en las demás fundaciones, verificado en la elevación de eje 1 y 2 del `00-002-004`. El error fue de ADASA y se corrigió en la nota, en los dos LEEME y en el generador: la cota de la fosa pasa de 4,155 a **4,255** con el criterio uniforme, sello menos emplantillado. Quedan un residuo de 5 cm (la sección B acota 4,30) y un rótulo que regresó (ancho superior 3,4 m sobre un fondo de 3,5): 0,2 m³ y un rótulo, registrados sin reclamar.
>
> **Las cantidades que rigen:** excavado total **75,53 m³** (contra 75,48) y partida 4.6 en **90,64 m³** (contra 90,58); el cuadro del movimiento de tierra y los seis cuadros de fundación coinciden ahora en las ocho zonas. El relleno del contenedor baja de 30,03 a 13,96 y la nota lo declara; la 4.7 se mide por obra ejecutada y su referencial de 91,5 viene del itemizado del proyectista, no de los cuadros.
>
> 🔴 **El paquete pasa a llevar cada plano en PDF y en DWG**, por instrucción del usuario: **154 archivos** (88 más 66 DWG), 255 MB sin la nube de puntos. Los nativos civiles Rev 0 salen de la ENTREGA 10, cuyos PDF son byte a byte los del paquete; los Rev 1, de la entrega que trajo cada PDF; los mecánicos, del Compilado, de la NE°15 (que hubo que descomprimir con los nombres corregidos de cp437 a cp850), de la E16 y de la E17. El `P22-DWG-00-001-001_1.dwg` contiene las dos láminas y el cuadernillo de soportes lleva dos DWG. **Queda fuera el DWG Rev 1 del P&ID de alimentación** que vino en la NE°15: el paquete mantiene la Rev 0 en los dos formatos para no llevar un nativo en otra revisión que su PDF. `construir_paquete_construccion.py` ganó la tabla de nativos, el archivo de la Rev 1 superada con sufijo de carta y la **regla 4 del autochequeo**: 66 planos PDF con 66 DWG apareados, cero huérfanos, con las rutas comparadas en NFC porque el NAS devuelve las tildes en NFD y sin normalizar el mismo archivo parecía dos. Gate de vigencia con `.dwg` incluido: 55 documentos, sin diferencias. `0. CONTROL DE CAMBIOS`, que estaba vacía, vuelve a llevar el PDF de la nota con el mismo SHA que el de origen.
>
> **Nota Técnica regenerada**, 16 páginas, PDF desde Word real con el índice resuelto, anti-ia VERDE (`.anti-ia-2026-09-10/veredicto.md`): 154 archivos y nativos declarados, 4,84 y 1,03 en la tabla de excavación, 75,53, 90,64, 4,255, el relleno del contenedor, y "cinco láminas" corregido a ocho. Los dos LEEME al 10-Sep, el civil reorganizado por carta con TT-016 reemplazando a TT-013 y TT-015, siempre en positivo.
>
> **Herramientas.** `large-pdf-reader --mode drawing` dio el render y los tiles a 600 dpi de las cinco láminas; **su cajetín no sirve en estas láminas**, asigna el nombre del jefe de proyecto al campo revisión. Lo que la skill no tiene es la comparación entre revisiones (propuesta v9): la cubrió `comparar_reemision_e15.py`, superposición y máscara por cuadrícula, con una calibración que dejó lección: la erosión borra los dígitos y declaró sin cambio tres láminas cuyo cuadro sí cambió, y la dilatación marca toda la lámina cuando el ploteo viene desplazado; el script elige según el par. En las láminas de fundaciones los cuadros están en la capa de texto y el diff textual entregó los valores directamente.
>
> 🔴 **La nota no deja incertidumbres, por corrección del usuario.** El borrador cerraba con una excepción: el P&ID de alimentación tenía una Rev 1 emitida solo en editable y "se remitirá en cuanto se reciba el ploteo". Salió: la nota declara que rige la Rev 0, en PDF y DWG, y el mismo párrafo se retiró del LEEME mecánico. Conseguir el ploteo de la Rev 1 es gestión interna con Van Doorn y vive aquí como pendiente, no en el documento que sale (`feedback_nota_tecnica_sin_incertidumbres`). Nota regenerada, 16 páginas sin la excepción, y copiada a la carpeta 0.
>
> **Correo al equipo** refrescado (154 archivos, nativos, 90,64), sigue en BORRADOR con comentarios al viernes 11. **El correo del 9 a L&A cierra su checklist**: el nativo llegó sin pedirlo y el seguimiento no va al registro de compromisos, que es del contrato C-4300.

### 2026-09-10 — El paquete de izaje: el yugo, la maniobra y el alcance del profesional que revisa el cálculo — ENVIADO

**El módulo se embarca el 28 de septiembre y lo iza ADASA, y los tres documentos que hacen falta para contratar la grúa no han llegado.** La ET pone el montaje en sitio y los equipos de izamiento del lado de ADASA (Sección 9, pág. 34, entrega Ex Works), y su Sección 7 pág. 29 exige, dentro del Manual de Montaje, la **memoria de cálculo de izaje**, el **plano de izaje con los puntos y los pesos** y el **plano y diseño del yugo**. Ninguno se ha recibido, y el Manual de Montaje que los contiene tampoco.

🔴 **El hallazgo que sostiene el reclamo es una contradicción del propio expediente de BW Water, no una opinión de ADASA.** Su Criterio de Diseño `P22-CD-09-005-003` Rev 0, sección F, página 10, manda: *"For the design of the padeye, a factor of safety, FS, of 2.0 shall be used. It shall also be designed for a lateral out of plane load equivalent to 5% of the gravity load."* **El informe de cálculo `P22-CD-09-005-001` Rev 0 no trae ninguna sección de diseño de padeye**: su índice salta de *Bolt Design at the Base* directo a los anexos. Y el informe salió igual apto para construcción. **Los dos PDF son imagen y no devuelven texto, de modo que las dos citas se verificaron por render** y no por extracción, que es la regla del proyecto para afirmar una ausencia.

**Parte del izaje sí está entregada, y reclamarlo entero habría quemado el correo.** El cálculo Rev 0 modela dos condiciones, desde los esquineros superiores con viga distribuidora y desde los inferiores con eslingas a 30 grados; aplica los factores 1,35 D y 2,0 D de API RP 2A-WSD; da el centro de gravedad con tolerancia de 300 mm; y reporta una tensión máxima de eslinga de 130 kN. **Lo que falta es lo que convierte ese análisis en algo ejecutable**, y no bajó a ninguna lámina: ningún montajista sabe dónde enganchar ni con qué capacidad. 🔴 **Y el yugo no es un accesorio que se elija después: es una hipótesis que el cálculo ya hizo.** Las eslingas se modelaron uniendo los puntos de izaje a la disposición de ganchos, y las cuatro tensiones que salen **no son iguales** —129,2 / 125,3 / 90,5 y 88,5 kN— por un **centro de gravedad descentrado a lo largo del módulo, 5.486 mm de un lado y 6.514 del otro**. Un yugo con otra geometría da otras tensiones y el análisis deja de aplicarle, de modo que el correo ofrece la salida: o el yugo se diseña contra la disposición que el modelo asumió, **o el modelo se rehace contra el yugo que se fabrique**. **Los puntos de izaje tampoco tienen plano**: existen como números de nodo del modelo y como una figura sin una sola cota. El pedido quedó en cuatro piezas nombradas una por una, y las dos cifras se verificaron por render sobre las Figuras 14 y 15 del informe.

🔴 **Y hay tres pesos que no concuerdan, ninguno de los cuales es el de izaje:** 122,41 kN de peso sísmico operativo en el cálculo, 13.300 kg estimados en el plano de cargas Rev B, y 32.500 kg de masa bruta ISO en la hoja del contenedor, que además es de enero y anterior a las modificaciones. ADASA tiene que contratar una grúa con eso.

**El encuadre es lo que hace que el correo no se pueda refutar, y lo fijó el usuario.** La ET **no exige** un profesional chileno: cero apariciones de "profesional", "ingeniero", "endoso" o "inscrito" en la ET, la BAE y el PIE. Lo que sí exige es **NCh 2369 Zona 3** y la aprobación de ADASA, y **BW Water eligió el PE local como su vía de cumplimiento**, declarada por escrito tres veces. ADASA no le impone un profesional: le pide cerrar la vía que él mismo eligió. Por eso el correo **no usa las palabras "endorse", "Chilean" ni "registered"**, verificado por barrido.

**El momento es el que da la urgencia.** La minuta del 9 registra que la orden al profesional se colocó ese día con un compromiso de cuatro días. El izaje y el sismo viven en el mismo informe y en el mismo modelo STAAD, así que ampliar el alcance ahora cuesta una revisión en vez de dos. El correo abre por ahí, como oportunidad y no como reproche, **y no impone fecha**: pide el paquete en la misma fecha que BW Water comprometió para su profesional, y que la confirme.

**Lo que la reunión de ayer dice del tema: nada.** Barrido de las 12 páginas de la minuta del 09-09-26 — cero menciones de izaje, yugo, grúa, maniobra, PE, endoso o cálculo estructural.

🔴 **Y un tercer refuerzo, a pedido del usuario: si se usan los esquineros ISO del contenedor, tiene que estar escrito que no requieren refuerzo.** Verificado, el planteamiento resultó más fuerte de lo que se planteó: **hay dos rutas de izaje incompatibles en el expediente y ninguna declarada.** El Criterio manda diseñar un padeye, que es una oreja soldada, y el cálculo iza desde los esquineros ISO, que ya existen. El informe **no verifica el esquinero contra la reacción que él mismo calculó** —cero apariciones de *reinforcement*, *capacity* e *ISO 1496*, y ninguna sección de verificación en su índice— y la hoja del contenedor es de enero de 2026, anterior a que el módulo se construyera dentro. El correo pide la ruta declarada: **o el padeye diseñado, o la constancia escrita de que los esquineros toman las reacciones sin refuerzo, con su base**. No se exige norma, y es deliberado: la ET no fija ninguna para el izaje y exigirla sería over-reach.

**Correo ENVIADO el jueves 10 de septiembre**, siete párrafos y **618 palabras**, en la cadena del Transmittal N39. Las tres pasadas de refuerzo lo habían dejado en 807, más que el correo de auditoría, y se comprimió **sin perder un solo argumento**: se apretó la redacción y la cita del padeye pasó de bloque sangrado a línea. 🔴 **Después las secciones de la ET se citaron con código, número y nombre**, que es la regla del proyecto y no se estaba cumpliendo: `Section 7 - Engineering and Documentation to be Developed During the Assignment`, `Section 9 - Commissioning and Start-up` y `Section 8.1 - Minimum Scope of Factory Acceptance Testing`. La Sección 9 pasó de paráfrasis a ceñirse al texto, que pone en alcance de ADASA la interconexión y el anclaje del contenedor **incluyendo los equipos de izamiento requeridos para ese fin, las grúas entre ellos**. También se corrigieron cuatro `centre` por `center`, porque el documento se emite en inglés estadounidense y Word los subraya. Gate `anti-ia` en VERDE con el veredicto persistido: **es el correo de la serie que mejor calza con el perfil**, mediana de 19,5 contra 18 y percentil 90 en 35,0 contra 35. **Compromiso `PRG-49` abierto**, que hasta hoy no existía: el izaje había quedado archivado como contenido ya aprobado en los criterios Rev B del TM N25 y nadie lo siguió como entregable, pese a que ese mismo transmittal declaró que *"the final lifting design follows as a separate deliverable"*. El `PRG-32` del endoso **no se toca en su fecha vencida del 22 de agosto**, que es la prueba, y solo recibe el hecho nuevo de la orden colocada.

**Artefactos:** `CORREOS/Septiembre 2026/2026-09-10/` con `crear_correo_izaje_pe.py`, su `_Descripcion.md` y el veredicto; `PROGRAMA y CONTRATO/SEGUIMIENTO COMPROMISOS/compromisos.yaml` con el `PRG-49`.

### 2026-09-09 — Transmittal N39, la emisión en revisión 0 en su Sección 3, y un solo correo para las dos cosas — ENVIADO

**El transmittal cierra las dos entregas que quedaban sin devolver.** `P22-TM-09-000-039-0`, submittals `25007-0091` (E91, recibida el viernes 4-Sep) y `25007-0092` (E92, recibida el martes 8-Sep), tres documentos. Veredicto global **2 — Approved as noted: 1 Código 1, 2 Código 2 y cero Código 3**. Ningún documento vuelve a revisión. Bajo la Cláusula 37.2 los dos períodos vencen el martes 15 y el jueves 17 de septiembre, y ADASA devuelve los dos bien dentro del plazo.

**La regla de alcance gobernó toda la revisión, y el usuario la reiteró al encargarla:** una re-emisión se verifica solo contra los comentarios previos, el estado es binario, y no se abre nada nuevo. Cada cierre se afirmó con cita literal del cuerpo de la revisión nueva y no con la respuesta de la hoja de comentarios, que es la fuente que ya falló antes.

🔴 **El hallazgo que decide es de compra, no de documento.** La Valve List Rev E **baja de Código 1 a Código 2**, y venía en Código 1 sin condición abierta desde el TM N18. BW Water comprometió por escrito tres cambios y entregó dos: los cuatro TAG del modelo 3D están —`VM-09-131`, `VM-09-132`, `VM-09-133` y `VRP-09-001`— y los cuatro figuran en el P&ID Rev 0, con `VRP-09-001` como la válvula reductora que reemplaza la placa de orificio en `CIT-09-004`. ADASA registra además una mejora que no pidió: `VM-09-015` sale de la lista, que es justo lo que el P&ID aprobado dice. **El tercero no está.** La succión de la bomba CIP, línea `CP-SS316-DN150-09-022`, es 316L en la Line List Rev 1 que ADASA aprobó en Código 1 en el N38, y `VM-09-065` sigue con cuerpo, interior y disco de PVC y asiento de EPDM. El vínculo entre la válvula y la línea se verificó por coordenadas sobre el P&ID Rev 0, hoja 11, donde el rótulo de la línea está a 16 puntos del TAG, y es además la única válvula DN150 del circuito CIP. **La lista de válvulas es contra la que se compra**, de modo que el punto tiene fecha propia aunque el documento se acepte.

**El GA del estanque de antiescalante Rev D cierra uno de sus dos puntos.** El agujero de anclaje pasa de "14 mm y media pulgada", que no son la misma medida, a `Ø14 [Ø35/64"]`, y 35/64 de pulgada son 13,89 mm: las dos unidades ya nombran la misma dimensión y ambas admiten el M12 del mismo detalle. **No cierra la fila `LEVEL MARKING`**, que sigue con guion en tamaño y guion en elevación, idéntica a la Rev C, mientras la hoja de comentarios responde *"Level mark added with dimensions"*. Sin elevación no hay marca en el estanque que materialice los 0,27 m³ útiles de la nota 8. Se verificó por render de la lámina, no por texto extraído. ADASA deja constancia de que esta revisión de aprobación no se requirió: el TM N36 pidió emitir en Rev 0.

**El procedimiento de radiografía llega en Rev 0 y sale en Código 1.** Su determinante cerró: el alcance ya declara duplex S32750 en espesores de 6,02 a 8,56 mm con fuente de Iridio 192, que es el material y el rango que efectivamente se radiografía en este módulo, y de ahí se siguen la técnica, el tamaño de fuente y el indicador de calidad de imagen. Las dos referencias cruzadas del renumerado quedaron reapuntadas a T-277.2 y T-282.1, y la hoja de comentarios trae por primera vez una fila por comentario. **Lo que queda es housekeeping y por regla del proyecto no degrada por sí solo**: la carátula dice `DOC NO: RT PROV-PROC-RT-001` y el documento no declara su estado de emisión en ninguna parte. Es el tercero y último de los tres procedimientos de ensayos no destructivos en llegar a Rev 0.

**Dos PDF anotados, los dos verificados por render**, que es como el proyecto cierra una anotación. El de la Valve List falló en el primer intento: el texto de 23 líneas produjo un cuadro de 872 puntos en una lámina de 842, de modo que la línea del identificador quedó fuera del área visible. **El conteo de anotaciones no lo detecta**; lo detectó la extracción de texto de la página, que devolvió `'OBS-01' → False`. Se acortó el comentario a 18 líneas y el cuadro entró en 740 puntos.

**Gate `anti-ia` en modo revisar sobre el transmittal, con el veredicto persistido** en `.anti-ia-2026-09-09/veredicto.md`. Se corrigieron tres cosas y una es de fondo: el Resumen Ejecutivo llevaba un párrafo narrativo de cierres que la disciplina del proyecto prohíbe expresamente, y que además repetía íntegro el bloque de la Sección 3. En su lugar entró el bloque `Why Code 2` con los dos determinantes. 🔴 **La estilometría del `.md` daba mediana 12 y máximo 20 palabras, cifras imposibles en su prosa**: la causa era que el archivo venía envuelto a 100 columnas y el script cuenta la línea física. Desenvuelto, mide 18 de mediana y 48 de percentil 90, dentro de la banda de los transmittals N36 a N38 realmente enviados.

🔴 **Después de armado, el usuario pidió un solo correo ejecutivo que llevara además todo lo que falta emitir en revisión 0.** Había dos borradores del mismo día para Eduardo, con la misma copia y el mismo plazo: la cobertura del N39 y la auditoría de emisión para construcción. Se fundieron. **Las cuatro tablas de la auditoría pasaron al transmittal como Sección 3**, `Issue for Construction of the Approved Engineering`, y las secciones que la seguían corrieron a 4, 5 y 6. El precedente es exacto: el correo del N37 llevó una exigencia de igual peso en 72 palabras de primer párrafo y mandó la lista nominal de los doce documentos a la Sección 3 de su transmittal.

**La Sección 3 lleva 51 filas en cuatro tablas** y, antes de ellas, la regla escrita por el propio proveedor con su cita literal, y después el argumento del DDSR, los dos planos que ese registro declara en revisión 0 y nunca llegaron, y los once cajetines que se contradicen con su formulario. **Las cifras no se escriben a mano:** el generador importa `auditar`, `leer_ddsr` y `separar` de `auditar_documentos_bw.py`, igual que el correo, de modo que los dos documentos no pueden discrepar. Un párrafo propio declara que **tres filas se mueven con este mismo transmittal**: la Valve List figura en Rev D y el GA en Rev C porque esas eran las revisiones al cerrar la auditoría, y el procedimiento de radiografía sale de la Tabla 3 porque llega en Rev 0 y se aprueba aquí. Sin esa declaración, BW Water podría responder que acaba de entregarlos.

**El correo único salió el mismo día**, seis párrafos y 404 palabras, en **primera persona**: abre con la exigencia y su cifra, sigue con la cita del proveedor, y recién entonces remite el transmittal. 🔴 **El párrafo de la cita se suavizó por decisión del usuario**, porque el objetivo es que emitan y no ganar el argumento: abría con *"the rule I am asking you to apply is your own"* y cerraba usando el propio plano del proveedor como prueba de cargo. Ahora reconoce que el criterio ya está acordado y que lo puso BW Water, y cierra en una línea. El hecho del plano en Rev F con el cajetín de aprobación **se conserva en la Sección 3 del transmittal**: el correo persuade y el transmittal deja constancia. El registro es deliberado, porque el argumento es que quien reclama la emisión es quien aprobó los documentos, y eso se pierde en tercera persona; el transmittal, en cambio, se queda en tercera persona institucional. Distribución acotada, Eduardo con copia a Jeryl y Victor. Los dos borradores originales quedan en `_no_enviados_fusionados/` con un LEEME que dice dónde vive cada pieza, porque el de auditoría conserva tres citas verificadas sobre PDF y su propio veredicto.

**Segunda pasada de `anti-ia` sobre los dos**, con veredicto persistido en cada carpeta. El mismo defecto apareció en los dos documentos y en el mismo lugar, la costura donde una tabla se vuelve prosa: el pedido del viernes 11 salió como una sola oración de 76 palabras en el transmittal y de 78 en el correo, con punto y coma, sobre el umbral crítico de 50. Se partió en oraciones sueltas, que es la forma que el correo de auditoría ya tenía y que había medido VERDE. **La Sección 3 mejoró la estilometría del transmittal**, que sube de 18 a 22 de mediana y se acerca al par de control de los N36 a N38. Las cinco fechas se comprobaron contra el día de la semana.

**El `PRG-46` no se cierra.** El criterio exige los tres cambios y falta el material de la succión CIP; el registro se actualizó con la Rev E recibida y el Excel se regeneró con su gate en exit 0.

**Artefactos:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-039-0/` con `_ANALISIS_N39.md`, el `.md`, `crear_transmittal.py`, el Word y los dos `CC_ADASA` en `COMENTARIOS/`; `REVISIONES/EVALUACIONES/update_register_n39.py`; `CORREOS/Septiembre 2026/2026-09-09/` con `crear_correo_tm39.py` y su `_Descripcion.md`.

### 2026-09-09 — Reunión de estado: el viernes 11 como fecha de cierre de cinco frentes — INTERNO

> Reunión semanal con BW Water. Asistieron Eduardo, Stefan, Adnin, Alin y Nick por el proveedor; Lockman ausente. **El viernes 11 quedó como fecha de cierre de cinco frentes**: los ensayos de alta presión, el programa de inspección de la semana siguiente para coordinar a Bureau Veritas, los planos de taller de los carretes, la orden de compra de repuestos y **los hitos documentales**. La única excepción declarada es el hito del estanque de lavado, planificado al 16 y que Stefan intentará adelantar.
>
> **Lo que se conversó de documentación fue puntual**: los planos de taller de los carretes —el reclamo del correo del 8— que Eduardo aclaró que existen y que es un problema de envío, comprometidos para el 10 con tope el 11; y el plano general del estanque, cuyos comentarios el proveedor ya recibió y va a incorporar para reemitir. **No se habló de emisión en revisión 0 ni del DDSR**: cero menciones de ambos en la minuta.
>
> **Eduardo confirmó que el procedimiento SAT y el dossier final se entregarán en español**, con un equipo suyo que los revisa o traduce. Es munición para el frente del idioma de la Cláusula 6, que sigue fuera del reclamo por decisión del usuario. El FAT se discutió en el rango del 18 al 19, con referencia al 20, y Bureau Veritas asistiría la semana completa.
>
> **La minuta es una transcripción automática, no un acta bilateral.** Se genera desde la grabación, sin membrete ni firma, con los asistentes rotulados como Speaker 1 y Speaker 2, y su bloque de acciones está escrito desde la perspectiva de ADASA. No es oponible a BW Water, de modo que el correo de auditoría cita la conversación y no la minuta. Archivo en `MINUTAS DE REUNION/MINUTA DE REUNION 09-09-26.pdf`.

### 2026-09-09 — Auditoría documento por documento: 46 de 72 documentos de ingeniería nunca se emitieron para construcción — ENVIADO

> La pregunta era por qué hay tan pocos documentos en revisión 0 si ADASA ya aprobó casi todo. Se auditaron **los 113 entregables del Master Register uno por uno**, cruzando el registro con el formulario de submittal de cada entrega y con el cajetín de cada PDF, y clasificando cada ítem en una categoría de acción sin residuo. 🔴 **De los 72 documentos de ingeniería, 46 siguen en revisión de letra, y 34 de ellos están en Código 1, aprobados sin una sola observación abierta.** La mediana de esas aprobaciones es de **184 días** y **cuatro llevan 267**, desde el TM N1 del 16 de diciembre de 2025; dos de esos cuatro se aprobaron al primer ciclo, sin un comentario. El paquete de calidad y fabricación, en cambio, sí está migrando a revisión 0, lo que descarta que sea un problema de capacidad del proveedor.
>
> 🔴 **El argumento no lo pone ADASA: la regla la escribió BW Water.** En la hoja de comentarios del plano de puesta a tierra `P22-DWG-09-007-003` Rev E, del 12 de mayo, el proveedor respondió que mantendría *"Issued For Approval"* hasta que el documento se aprobara y entonces cambiaría a *"Issued For Construction - Rev0"*. Ese plano lleva Código 1 desde el 11 de junio, va por la Rev F y su cajetín sigue diciendo que es para aprobación. Verificado sobre el PDF, no sobre la extracción.
>
> **El mecanismo está medido.** BW Water somete **el 87 % de lo que transmite para aprobación y no para construcción** (227 contra 33 en los 91 formularios), y desde el submittal 25007-0019 escribe `IFA` en la columna `Sub. For`, **un código que la leyenda de su propio formulario `PEM-F013` Rev 3 no define**: la leyenda tiene `FA`, `FR`, `FI`, `IFC` y `AB`. En el registro, 49 de las revisiones vigentes entraron bajo ese código. 🔴 **Y once documentos en revisión numérica conservan el cajetín diciendo que son para aprobación**, entre ellos los tres datasheets Fedco de la entrega 90, que viajaron declarados `IFC` en el formulario y llevan `ISSUED FOR APPROVAL` dentro del documento.
>
> **Base contractual, en tres piezas:** la ET Sección 7 exige desarrollar la ingeniería *para construcción*; esa misma sección hace obligatorio el estándar de codificación `P00-IT-00-000-101-0`; y ese estándar define la revisión 0 como Para Construcción y establece que un documento revisado en Estatus 1 o 2 **debe** emitirse en revisión 0.
>
> 🔴 **Este correo no se envió por separado:** el mismo día se fundió con la cobertura del Transmittal N39 en un solo correo ejecutivo, que salió el 9 de septiembre, y sus cuatro tablas pasaron a la Sección 3 de ese transmittal. Queda archivado en `_no_enviados_fusionados/` con su veredicto y sus citas verificadas. Lo que sigue describe el borrador original, cuyo contenido se conserva íntegro repartido entre el correo único y el transmittal. **Correo a Eduardo Yamauchi en BORRADOR** (`CORREOS/Septiembre 2026/2026-09-09/`), inglés, con cuatro tablas en el cuerpo: los 34 aprobados sin observación, los 12 aprobados con observación, los 7 de calidad y los 7 entregables de la Sección 7 no recibidos. Se ancla en la reunión de ese día y exige **todo emitido en revisión 0 al viernes 11 de septiembre**, con fecha comprometida en el DDSR para lo que no alcance. 🔴 **Quedaron fuera por decisión del usuario**, y disponibles si el frente escala: el idioma castellano de la Cláusula 6, el hito de pago del 10 % que exige la totalidad de la ingeniería aprobada, la multa de la Cláusula 43.1 letra a) y la frase de la ET sobre la liberación de los equipos; el cierre lleva una reserva genérica de derechos. El correo pide primero la fecha y no la emisión inmediata, porque **la defensa previsible es que ADASA nunca fijó un plazo, y en sentido estricto es cierta**.
>
> 🔴 **Hallazgo de gestión propio: ADASA lo pidió una vez y no lo persiguió.** El correo del 7 de mayo a Eduardo y Andrew Sia pedía una fecha vinculante para la emisión en revisión 0 del conjunto de la Sección 1. La fecha nunca llegó y **el pedido nunca entró al Registro de Compromisos**. Se corrige con el **`PRG-48`**, crítico, sin fecha comprometida porque BW Water nunca dio una; la fecha del viernes 11 se escribirá cuando el correo se envíe y no antes. El propio DDSR del 7 de septiembre ya lleva ese viernes como fecha planificada en seis de sus diez filas con fecha.
>
> 🔴 **El registro con que BW Water gestiona la revisión no mide la emisión, y ahí está la explicación.** El DDSR del 7 de septiembre tiene doce columnas —revisión actual, fechas de envío y devolución, estado, ponderador— y **ninguna de emisión para construcción**: las cadenas IFC y Rev 0 no aparecen en el documento. Su ponderador da **100 % a un documento aprobado sin mirar en qué revisión quedó**, de modo que **34 de los documentos sin emitir figuran ahí al 100 %**. El Progress Report de la misma semana declara la documentación de ingeniería al 85 % en SWRO y al **100 % en CIP y en antiescalante**, con cuatro documentos de esos dos sistemas todavía en revisión de letra. 🔴 **Y el DDSR declara dos planos en revisión 0 que nunca llegaron**: el Cable Tray Layout, que ADASA tiene en Rev C, y el GA del estanque de lavado CIP, en Rev B; verificado sobre el árbol de entregas, no existe archivo en revisión 0 de ninguno. El correo lo pregunta en vez de afirmarlo.
>
> 🔴 **La auditoría destapó dos errores del propio registro de ADASA, y uno habría arruinado el correo.** El `P22-CD-09-005-001` **está emitido en revisión 0 desde la entrega 71 del 6 de agosto** y los transmittals N37 y N38 lo declaran así, pero el Master Register lo tenía en Rev B del N29: la tabla lo habría reclamado como no emitido. Sale de la lista, que baja de 47 a 46. Y la **entrega 91 trae la Valve List Rev E y el GA del estanque de antiescalante Rev D**, aún sin revisar; el correo lo reconoce en una línea en vez de afirmar que la revisión del registro es la última que enviaron. Las dos correcciones quedan declaradas en el archivo de auditoría.
>
> Respaldo interno en `REVISIONES/EVALUACIONES/_AUDITORIA_REV0_2026-09-09.md`, con la tabla de los 113 separada en ingeniería y calidad, generado por `auditar_documentos_bw.py`, que cruza cuatro fuentes: el Master Register, el formulario de submittal, el cajetín de cada PDF y el DDSR. Ninguna cifra del correo se escribe a mano: el generador importa la clasificación de ese script.

### 2026-09-09 — La ingeniería de BW Water queda en un dossier por especialidades para el equipo — GENERADO

> La ingeniería del módulo llega en submittals y se archiva por entrega, de modo que **ninguna carpeta refleja lo vigente**: la lista de I/O vive en diez entregas, el plano de disposición de equipos en seis y la filosofía de control en siete. Para leerla hay que saber de antemano en qué entrega cayó la última revisión aprobada de cada documento. Se armó `BASES DE LICITACION MONTAJE MECANICO-OOCC/INGENIERIA MODULO BW WATER/` con **71 documentos en 78 archivos, 340 MB**, uno por documento y en la última revisión que ADASA aprobó, repartidos en seis carpetas por especialidad según la **Tabla 2-4 de la codificación general del proyecto** (`P00-IT-00-000-101`), que es la que asigna el campo de disciplina del código. Alcance: solo ingeniería, sin el paquete de calidad y fabricación. De los 71, **59 en Código 1 y 12 en Código 2**; en ingeniería no hay ningún Código 3 ni 4, de modo que no hubo que elegir entre una revisión aprobada y una posterior rechazada.
>
> **Dos scripts nuevos en `BORRADOR_REV0/script/`, con el patrón del paquete civil.** `catalogar_ingenieria_bw.py` lee el Master Register, filtra la ingeniería y localiza el archivo físico de cada revisión vigente, emitiendo `vigencia_bw.py` como fuente única; `construir_dossier_bw.py` copia con verificación SHA256, escribe un LEEME por especialidad desde ese mismo catálogo, y corre el gate bidireccional más un autochequeo de cuatro reglas duras. **72 copias verificadas, gate en verde.** El localizador tuvo que absorber el desorden de nombres del proveedor: seis grafías de revisión, correlativos de dos y de tres dígitos, el tipo `ITEM` que fue reemplazado por `ET`, y los sufijos que agrega la revisión de ADASA, que no viajan.
>
> 🔴 **El Master Register discrepa del documento emitido en ocho puntos, y todos se descubrieron al buscar el archivo.** Los **tres datasheets de estanques llevan el correlativo corrido en uno** —el registro llama `-010` al estanque CIP, que es el `-009`, y así hasta el `-014` que no existe—, con el título y la entrega calzando exactos, de modo que lo único desplazado es el número. Las **dos especificaciones de cañerías y pintura** están registradas en la disciplina mecánica y el documento dice cañerías. **Los dos planos generales de los turbocargadores son revisión A**, verificado en su cajetín por extracción de texto, y el registro los anota en B, que no existe en el repositorio. Y el **plano de puntos de conexión figura en la entrega 87**, que es el hueco de la serie del proveedor; el archivo está en la 88. En todos manda el documento emitido; **corregir el registro queda pendiente y es tarea aparte**.
>
> **Nota Técnica `P22-NT-06-000-002-0`**, 16 páginas, PDF exportado desde Word real con el índice resuelto y copiado a `0. CONTROL DE CAMBIOS`. Importa `VIGENCIA_BW` en vez de transcribirla, igual que la NT del paquete civil importa `VIGENCIA`. Declara la condición abierta de cada uno de los doce Código 2, los **seis entregables de ingeniería que el registro marca como no recibidos** —cálculo sísmico NCh 2369, flexibilidad de líneas de alta, modelo interoperable con Autodesk, isometrías de alta, vigas carrileras y mapa de memoria Modbus— y que el cálculo estructural sigue sin endoso de profesional inscrito en Chile.
>
> **El dossier es cien por ciento PDF, y no por decisión.** El único `.xlsx` bajo `ENTREGAS_BWWATER` que no es un formulario de submittal es un archivo suelto de señales: **BW Water nunca ha entregado un listado en formato editable**, de modo que las listas de instrumentos, líneas, válvulas, equipos e I/O solo existen en PDF. La nota lo dice en una línea para que nadie las busque. El modelo Navisworks queda fuera por formato y se entrega por enlace.
>
> Corrección de arrastre: el `LEEME.txt` del dossier mecánico del paquete civil remitía a "la hoja Mecánica de la planilla de la carpeta 0", que dejó de viajar esta misma jornada cuando la nota técnica la absorbió. Reapuntado a la nota.

### 2026-09-09 — El paquete de ingeniería vigente se completa y la Nota Técnica queda lista para el equipo — GENERADO

> **El correo de discrepancias salió a L&A** con sus cuatro planos comentados, `OBS-01` a `OBS-07`, y la reemisión pedida al viernes 11. Con eso despachado, el frente se movió a dejar el paquete compartible.
>
> 🔴 **El paquete estaba incompleto en este equipo y nadie lo había notado: 35 de 88 archivos.** Las carpetas de los P&ID, del cuadernillo de isometrías, del de soportes y de los anexos de la especificación de cañerías HDPE estaban vacías, y faltaban los dos PDF raíz de las especificaciones de montaje. Compartirlo así habría entregado el dossier civil completo y la mecánica a menos de la mitad. Se reconstruyó con `construir_paquete_construccion.py`, al que hubo que hacerle dos arreglos: **la raíz pasó de un literal de macOS a derivarse de la ubicación del script** (`Path(__file__).resolve().parents[3]`), con lo que ahora corre en los tres equipos; y **el bloque del modelo todavía copiaba la maqueta del 23 de abril**, de modo que correrlo tal cual habría retrocedido lo incorporado el día anterior. **93 copias verificadas por SHA256, autochequeo en verde con 60 códigos, paquete en 88 archivos.**
>
> **La planilla se regeneró con el gate de vigencia limpio**, sin el flag de árbol incompleto: *55 documentos, sin diferencias*. Es la comprobación que declara el paquete entregable, y hasta hoy la planilla que lo acompañaba era provisoria. Lint en cero y copia al paquete verificada por SHA256.
>
> **La Nota Técnica quedó lista y sin bloqueador.** Se dirige **al equipo de ADASA como revisión interna previa**, con lo que desaparece el campo del nombre del contratista que la tenía detenida desde el 4 de septiembre. Se actualizaron sus dos fuentes de verdad, el `.md` y el texto duplicado dentro de `crear_nota_tecnica_montaje.py`: 55 documentos en 88 archivos, ocho láminas civiles en revisión 1, la sección de los dos modelos con la advertencia del archivo de 6,4 GB que se entrega por enlace, y 🔴 **la partida 4.6 de 115,10 a 90,58 m³**, con el criterio declarado en una frase, porque la cantidad se construyó como volumen retirado esponjado sobre una partida que se mide por metro cúbico excavado. PDF de 9 páginas exportado desde Word real con el índice actualizado; la PIA tipada falló y se resolvió por **late binding**, como ya estaba documentado.
>
> **Sección nueva en la nota: las cantidades de movimiento de tierra que rigen**, una tabla de ocho zonas con el plano del que sale cada cifra y el total excavado de 75,48 m³. Para la zona del sistema CIP rige **1,60 m³**, la del `00-002-007` LAM1, que es el plano que define la geometría de esa fundación; para el contenedor, **20,95 m³**, el único valor dimensionado sobre el sello vigente. Se agregan la fundación de la bomba y la de la cubierta CIP, 0,62 y 4,25, que el cuadro consolidado no recogía.
>
> **Nada de esto expone que hay un plano por corregir.** Por decisión del usuario, la nota y los dos `LEEME.txt` declaran las cantidades que rigen y de qué plano sale cada una, sin mencionar discrepancias ni la reemisión pedida. Verificado con barrido: cero apariciones en los tres documentos. El diagnóstico vive en el análisis del `P22-TM-00-010-005-0` y en el contexto interno del correo al equipo.
>
> 🔴 **La Nota Técnica absorbió la planilla de control de cambios.** La carpeta `0. CONTROL DE CAMBIOS` llevaba dos documentos que explicaban la misma materia, de modo que la planilla `P22-LI-06-000-002-1` **sale del paquete** y la nota pasa a ser el único documento de control. Es el mismo movimiento del 4-Sep con el índice del paquete. La nota creció de 9 a **16 páginas** con dos tablas nuevas: la de **vigencia, 55 filas** con código, lámina, revisión que rige y dossier, y la de las **14 partidas** del Capítulo 4 con cantidad cotizada y vigente. **Las dos se importan de `generar_ingenieria_vigente.py`** en vez de transcribirse: ese script conserva las listas y su gate, que es lo que contrasta lo declarado contra el árbol real, y su `.xlsx` queda como respaldo interno en `BORRADOR_REV0`. Sin esa importación la nota habría sido una tercera fuente de verdad de la misma lista. El constructor gana `dossier_control()`, que copia el PDF de la nota, de modo que la composición del paquete sigue siendo reproducible desde un solo script. Paquete en **88 archivos**, carpeta 0 con un solo archivo, gate en verde y cero remisiones a la planilla en el cuerpo de la nota. **Salieron además el acuse de recibo y el historial del documento**, que pedían una firma de vuelta y un registro de revisiones a un documento en revisión 0 que se comparte para comentarios; el cuerpo cierra ahora en la tabla de vigencia.
>
> **Correo al equipo en BORRADOR** (`CORREOS/Septiembre 2026/2026-09-09/`), 211 palabras, con comentarios pedidos al viernes 11 para emitir al contratista la semana entrante. El correo del 4 de septiembre dirigido al contratista queda intacto, para reusarlo cuando llegue el nombre de la empresa.

### 2026-09-09 — Movimiento de tierra Rev 1 revisado, incorporado al paquete, y la partida de excavación reconstruida — GENERADO

> **L&A respondió el pedido del 4 de septiembre.** La ENTREGA 14 (`067-032-032-COR-TT-015`, 8-Sep) trae `P22-DWG-00-001-001` láminas 1 y 2 en Rev 1, y la ENTREGA 13 (`TT-014`, 7-Sep) trajo además `P22-DWG-00-002-001` Rev 1, que el correo del 4-Sep había concluido que no correspondía pedir. Todo lo que sigue se leyó por render: las láminas son vectorizadas y la extracción de texto solo devuelve el cajetín.
>
> **Las cubicaciones bajan más de lo estimado.** La excavación total del cuadro pasa de 91,09 a **70,04 m³**: el contenedor de 38,02 a **20,95** sobre un área que baja de 53,51 a 49,96 m², y la zona CIP de 5,01 a **1,03**. Los rellenos no se mueven. En la lámina 2 el fondo de excavación del contenedor sube de EL. 5,15 a **EL. 5,35**, que es el sello +5,400 menos el emplantillado, y se corrige el ancho superior de la excavación del estanque de 3,4 a 3,7 m, que en la Rev 0 era menor que el ancho de fondo.
>
> **El cruce del sello contra los planos de fundaciones, zona por zona, es el hallazgo.** Contenedor y sistema CIP cuadran. **El estanque queda 5 cm alto y la fosa 14,5 cm**, porque en esas dos zonas el fondo declarado coincide con el propio sello sin descontar la capa inferior: el criterio nuevo se aplicó solo donde L&A rehizo el dibujo. Bajo la fosa va mejoramiento M.H.A. de 15 cm, no emplantillado de 5. **Y faltan dos excavaciones que sí se ejecutan:** la fundación de la bomba BH-06-001 (0,62 m³) y la de la cubierta CIP (4,25 m³). Además el cuadro **contradice a dos planos vigentes**: 20,95 contra los 38,02 del `00-002-003` Rev 1 y 1,03 contra los 1,60 del `00-002-007` Rev 1. De las cuatro fundaciones que el cuadro sí cubica, dos coinciden al centésimo con su plano y dos no, lo que descarta que sean criterios de medición distintos.
>
> 🔴 **La partida 4.6 estaba mal por partida doble y se corrigió.** Los 115,10 m³ contractuales no tienen respaldo en el repositorio: el generador del Formato pasó de vacío a 111,70 sin escala intermedia. Se reconstruyeron desde los planos y calzan como **95,96 × 1,2**, la suma de las ocho excavaciones en Rev 0 con el 20 % de esponjamiento que declaran los propios cuadros. Es decir, la cantidad se armó como volumen **retirado esponjado** mientras la partida se paga por m³ **excavado**. El paso a 111,70 restaba 3,41 sin esponjar a una cifra que sí lo estaba. Manteniendo el criterio con que se licitó, la cantidad vigente es **90,58 m³**: del orden de **$1,05 M** con gastos generales y utilidad, contra los $97.240 que declaraba la NT en borrador.
>
> **Incorporado al paquete**, cada copia verificada por SHA256 y el superado archivado en `_dossier_superseded_pre-REV1/`: las tres láminas civiles —el dossier queda en **8 en Rev 1 y 10 en Rev 0**— y los dos modelos del 8-Sep, `MODULO COMPLETO.nwd` (21 MB) y `MODULO COMPLETO (nube puntos).nwd` (6,4 GB), que reemplazan la maqueta del 23-Abr, anterior al cambio de nivel. El federado ya trae dentro el modelo civil de L&A Rev 1, así que no hubo que copiarlo aparte. Por su tamaño, el de nube de puntos se entrega por enlace y no dentro del comprimido. Planilla regenerada con la 4.6 en 90,58 y lint en cero; `construir_paquete_construccion.py` ganó las rutas de las entregas 13 y 14 y el renombrado a la convención del dossier.
>
> **Del modelo, con el puente de Navisworks** (que ahora detecta la versión: la instalación 2026 de este equipo ya no trae las bibliotecas de la API y responde la 2027): 213 objetos de soporte con el correlativo sin asignar y 26 cañerías con el TAG incompleto. El archivo no declara título, autor ni código de documento.
>
> **Los dos `LEEME.txt` del paquete se escribieron en positivo**, por decisión del usuario: declaran que rige el cuadro del `00-001-001`, que a él se suman las dos excavaciones faltantes y hasta dónde se lleva el fondo de excavación, sin narrar el defecto ni mencionar observaciones abiertas. **La Nota Técnica no le dirá al contratista que el plano tiene errores.** El diagnóstico completo vive en `INGENIERIA DE DETALLE OOCC/REVISIONES/TRANSMITTALES/P22-TM-00-010-005-0/_ANALISIS_TRABAJO.md`.
>
> **Correo a L&A en BORRADOR con los planos comentados adjuntos** (`CORREOS/Septiembre 2026/2026-09-09/`), como respuesta al hilo TT-015. Se aplicó la metodología del stream: cuatro `_CC_ADASA.pdf` generados con `doc-annotator` desde `P22-TM-00-010-005-0/COMENTARIOS/generar_cc_adasa_entrega14.py`. 🔴 **Solo se comentan discrepancias entre planos**, por decisión del usuario: una misma excavación o una misma cota declarada con dos valores distintos, de modo que la instrucción es siempre la misma, dejar una sola cifra. **Siete observaciones en serie única, `OBS-01` a `OBS-07`**, corrida por el orden en que se leen los planos: la zona CIP (1,03 contra 1,60), el contenedor (20,95 contra 38,02), los 4,87 m³ de la bomba y la cubierta CIP que el cuadro no recoge, los fondos del estanque (5,35 contra 5,30) y de la fosa (4,30 contra 4,155), y el reflejo de las dos primeras en los planos de fundaciones, que se citan entre sí con un «Ver OBS-xx». Los identificadores son de este paquete, no del historial del plano. **El correo no repite los comentarios**: lleva una tabla de cuatro filas, una por adjunto, con el rango de identificadores y la materia; el detalle vive en los recuadros. 340 palabras. **Reemisión pedida al viernes 11-Sep**, el mismo día en que se emite la Nota Técnica.
>
> **Lo que quedó fuera del correo y sigue en el registro interno:** que el cajetín de la lámina 1 declare la revisión y que la fila de la Rev 0 recupere su estado de emisión —el cajetín ya identifica la Rev 1 y las nubes están puestas—, las dos secciones de excavación ausentes, que son omisión de dibujo y no discrepancia, y el archivo nativo con la verificación de integridad fallida, que se pedirá al acusar la reemisión.
>
> **La anotación dejó dos lecciones.** En estas láminas el alto útil de la página es el lado corto, 842 puntos, y la caja mínima de la skill son 140: no caben más de cuatro recuadros por lámina, y el quinto **se dibuja fuera y se pierde sin error**. Y la verificación no puede ser `page.annots()`, que devuelve cero en páginas rotadas porque el cuadro va al flujo de contenido: se cierra por render PNG y por extracción de texto de cada recuadro.
>
> **Dos cosas que quedan abiertas.** El paquete está incompleto en este equipo: faltan 32 de los 54 documentos declarados (P&ID, isometrías, cuadernillo de soportes y las dos ET de montaje), cuyas carpetas están vacías mientras el origen sí los tiene. El gate de vigencia lo detectó y abortó; se le agregó un modo `--arbol-incompleto` que tolera solo archivos faltantes y marca la salida como provisoria, de modo que **la planilla hay que regenerarla sin ese flag antes de emitir**. Y la Nota Técnica sigue en borrador, ahora además con la cifra de la 4.6 por actualizar.

### 2026-09-08 — Paquete semanal Week 36 y puntos de revisión para la reunión del 9 — ENVIADO

> **Eduardo Yamauchi envió el paquete semanal el martes 8 a las 12:41** (`PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 08-09-26/`): Progress Report Week 36, DDSR del 7 de septiembre y el Procurement tracking. **Por primera vez el paquete no trae cronograma ni fabrication schedule.** No hay cambio declarado en la entrega: la última fecha que el proveedor sostiene sigue siendo la del Progress Update del 28-Ago, FAT del 15 al 25 y ex-works del 26 al 28. Lo que sí cambió de estado es que **este paquete era el plazo de la Nota Técnica `P22-NT-09-000-003-0`**, que pidió sus cinco puntos con el próximo reporte semanal: llegó el reporte y no llegaron los puntos (`PRG-41` y `PRG-42`, vencidos desde el 4 de septiembre).
>
> **Avance físico contra la semana 34:** SWRO 63 → 66 %, CIP 60 → 66 %, Antiscalant 32 → 35 %. Fabricación de spools 70 → 85 % en SWRO y 55 → 65 % en CIP. **Montaje de spools, válvulas, instrumentos y eléctrico: 0 % en las dos semanas**; bandejas, cableado, terminación y CSC sin iniciar; inspección dimensional final, punch list y embalaje en 0 %. Llegaron al taller el contenedor y el marco ya pintados, y los recipientes empezaron a insertarse en el skid el 6 de septiembre. Bomba de alta y los dos turbocargadores retirados de Fedco el 4, llegada a Penang el **10**, un día después de la fecha en que el propio plan los instalaba. Tablero PLC recibido el 3 por vía aérea y sensor de vibración el 7. **El estanque CIP se declara de dos maneras dentro del mismo paquete**: el reporte lo da al 100 % recibido y el tracker lo deja pendiente de documentación de calidad antes del retiro. Membranas LG sin ETA. **El Milestone Tracker sigue congelado desde julio** —línea base del FAT del 13 al 18 de agosto y un ex-works del 10 de septiembre cargado en la columna `Actual` de un hito que no ha ocurrido, ya objetado el 3-Ago— y el Change Log lleva seis versiones vacío: el diff celda a celda contra la semana 34 no arroja **ningún** cambio en esa hoja.
>
> 🔴 **El cuadro de los ensayos cambia con el `Request to witness inspection 007`**, que el usuario aportó y no estaba en el paquete: tres jornadas consecutivas, **miércoles 9, jueves 10 y viernes 11**, con las primeras pruebas a 135 barG el miércoles. Al 8 de septiembre hay **cuatro líneas conformes** de las once de alta —`DA-SSD-DN100-09-003` el 2, `DA-SSD-DN80-09-005` y `CP-SSD-DN80-09-044` el 3, `DA-SSD-DN65-09-009` el 4, informes `BVM-IR010` a `IR012`— y las siete restantes, dos de ellas repeticiones, entran en esas tres jornadas. **Ninguna de las cuatro líneas que exigen 135 barG se ha ensayado todavía.** Si las tres jornadas se cumplen, el requisito de la ET Section 8.1 —hidrostáticas completadas y aprobadas antes del inicio formal del FAT— queda cubierto el viernes 11.
>
> **Tres defectos del Testing Plan, verificados contra la Line List aprobada, y son de rótulo y no de presión:** el ítem 9 rotula `DA-SSD-DN100-09-005` cuando la Rev 0, la Rev 1 y el `BVM-IR011` la rotulan DN80; el ítem 16 rotula `DA-SSD-DN65-09-016` cuando `09-016` es `DA-PVC-DN65-09-016`, PVC SCH80; y **`DA-SSD-DN100-09-050`, la succión de la bomba de alta, está en la Rev 1 aprobada y no tiene ensayo programado**, la única de las diecisiete líneas de super dúplex ausente del plan. Las presiones que el plan aplica coinciden con la Line List en las diecisiete. 🟢 **Lo que el plan hizo bien y se le reconoce:** adopta los diámetros vinculantes que ADASA declaró en el Transmittal N38 (`CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`) y ensaya las seis líneas nuevas de baja presión a 7,5 y 3 barG en coherencia con la Rev 1, que les dio número y presión propios. **La objeción del 20 y 21 de agosto quedó resuelta por diseño, no por excepción.**
>
> 🔴 **El cruce completo del Testing Plan destapó lo que más pesa, y no son los rótulos.** El plan identifica cada carrete de alta por su plano de taller, y los once que cita para las líneas originales son `25007-ME-PI-0901-0006` a `-0016`: **exactamente el juego que ADASA devolvió como no recibido en el Transmittal N30**, retirado del Piping Layout en la Rev D y nunca sometido como entregable propio. Sus dos hallazgos de contención de presión siguen sin responder desde el 5 de agosto (`PRG-22`, CRÍTICA, vencido el 24): derivaciones roscadas austeníticas ANSI 150# sobre líneas de 60 a 90 barG de diseño, y el límite super dúplex a PVC sin quiebre de especificación. **Mañana esos carretes se presurizan y cuatro van a 135 barG.** Los planos `-0023` a `-0028`, de los carretes nuevos de baja presión, no aparecen en ningún submittal: el DDSR del 7 lista 73 documentos y ninguno es un `25007-ME-PI`.
>
> **El cruce fila por fila, en cambio, absuelve al plan en lo que más importa.** Las **diecisiete presiones coinciden con la Line List Rev 1 y las diecisiete cumplen 1,5 por la de diseño**, sin una sola desviación. Los desacuerdos son de rótulo y en cuatro filas, y **en dos de ellas el equivocado es la Line List**: el plan escribe `CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`, que son los diámetros que ADASA declaró vinculantes en el N38. Las otras dos sí son del plan, el ítem 9 que rotula DN100 una línea DN80 y el ítem 16 que rotula super dúplex una línea de PVC. Y falta `DA-SSD-DN100-09-050`, la succión de la bomba de alta, única línea de super dúplex sin ensayo programado; el ítem 14 declara además solo su Spool 2. Los cuatro PDF que el usuario descomprimió son **byte a byte** los del zip ya leído.
>
> **Decisión del usuario: ADASA mantiene el 28 de septiembre y pregunta en la reunión**, sin declarar todavía que la fecha no se sostiene, y se emite **solo el correo de puntos de revisión** (`CORREOS/Septiembre 2026/2026-09-08/`, inglés, **566 palabras** más una tabla de cuatro filas, Reply-All a la cadena `Project updates - 08-Sep-2026`). **Lo ejecutivo va en la estructura y no en la sintaxis:** el punto de seguridad de los planos abre en negrita, las cuatro correcciones van en tabla compacta, y los tres frentes de la reunión llevan un rótulo y dos o tres oraciones cada uno. 🔴 **El usuario objetó lo que el borrador decía de las presiones, y tenía razón en el fondo.** La Line List Rev 1 llegó con la columna de hidrostática en el submittal `25007-0090` y ADASA la aprobó en **Código 1** en el TM N38, de modo que **las presiones están zanjadas**. La tabla de discrepancias abría antes del reconocimiento, lo que hacía leer como abierto algo cerrado, y una de sus filas pedía declarar qué línea se ensaya cuando la Line List aprobada ya la identificaba. **Se reordenó el cuerpo:** el párrafo de las presiones va delante de la tabla, y las cuatro filas quedan como correcciones de registro que no cambian ninguna presión. 🟢 **Al barrer los transmittales apareció algo mejor todavía:** el TM N35 impuso el 20 de agosto una retención sobre **todo** el circuito de super dúplex hasta que BW Water confirmara por escrito la presión de cada línea (`PRG-34`, CRÍTICA, vencido el 1 de septiembre), y **el Testing Plan es exactamente esa confirmación**, de modo que el correo levanta la retención del circuito completo y no solo la de `CP-SSD-DN65-09-045`. Salió además la petición de emitir el Testing Plan con número de documento, que vestía de obligación del ITP una petición nueva de ADASA, y entró en su lugar la reiteración del `PRG-35` sobre el Pressure Test Record Chart, que sigue sin número ni revisión y sobre el que mañana se levantan tres jornadas de registros. 🔴 **El deslinde que estaba detrás de todo esto queda por escrito** en `feedback_presion_acordada_no_libera_la_presencia`: que la presión esté acordada y que ADASA deba estar presente son cosas distintas. El ITP `P22-BA-09-000-004` Rev 0 tiene **catorce Puntos de Detención en la columna de ADASA**, la 5.2 entre ellos, y su leyenda define la H como que el ensayo se ejecuta con el cliente o el tercero presente. La presencia no está en discusión y por eso va Bureau Veritas, así que el correo no la menciona. De paso se corrigió una cita propia defectuosa: la enumeración de nueve Hold Points del TM N17 es de la **Rev A** del ITP, omite la 5.2 y quedó superada por la Rev 0. 🔴 **El párrafo de apertura se descartó entero tras la lectura del usuario:** estaba armado alrededor del historial documental, mezclaba dos hallazgos técnicos con una queja de control documental, y no se entendía qué alertaba. Lo reemplaza **un solo asunto con una sola petición**, en 83 palabras: no tenemos los planos de detalle de los carretes, hay que emitirlos, y **Bureau Veritas tiene que tenerlos en cada una de las tres jornadas** para contrastar cada carrete contra su propio plano antes de presurizarlo. Entra además el desfase de juntas del `CP-SSD-DN80-09-044`, rechazado el 21 de agosto en las **juntas 03 y 04** y reensayado el 3 de septiembre en las **01 y 02**, con el plan dándolo por terminado. 🔴 **Y la verificación que pidió el usuario arrojó una coincidencia que no entra al correo:** los tres ensayos que BV rechazó el 20 y 21 de agosto aplicaron **7,5 barG**, que es justo la presión de ensayo del PVC, y uno de ellos es el `09-044`, uno de los dos carretes que el TM N30 describe construidos con PVC SCH 80. Es coincidencia y no causa probada, sin los planos no se sostiene, y por eso el correo pide los planos y no afirma nada. Sobre el FAT se piden las tres cosas que lo gobiernan: qué ventana rige, la fecha de emisión del **procedimiento de FAT del módulo que exige la ET Section 8.1 y que nunca se ha sometido**, cuya aprobación es Punto de Detención de la fila 7.1 del ITP, y el alcance mínimo con la secuencia de puntos. `anti-ia` modo **revisar**: el borrador anterior salió AMARILLO por voz —once palabras por oración contra las 18,5 de su calibración en inglés, y sin primera persona— y la reescritura queda **VERDE** con mediana de 20,0 y percentil 90 en 30. Veredicto y estilometría antes y después en `.anti-ia-2026-09-08/veredicto.md`. 🟢 **La asistencia del inspector ya está cerrada y ADASA no emite nada.** Mohd Adnin envió el Request 007 a Bureau Veritas el viernes 4 a las 16:26 con los tres formularios de día y el Testing Plan, y Ahmad Hazwan respondió el martes 8 a las 00:50 asignando al mismo inspector, Fakhrul, para el 9, el 10 y el 11. Luis va en copia en las dos puntas, así que la coordinación queda entre el proveedor y el inspector (`PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/TESTING PLAN 08-09-10/PETICION DE BV.pdf`). El aviso fue de cinco días contra los treinta de la Cláusula 37 y no se objeta: ADASA ya aceptó avisos de cuatro y ocho días, y reclamarlo ahora contradiría la posición del 14 de agosto.

### 2026-09-04 — La ingeniería vigente se ordena para el contratista, con Nota Técnica, y una auditoría propia que resultó estar mal dirigida — GENERADO

> **El trabajo empezó como actualización del paquete de licitación y terminó como entrega de ingeniería para construcción.** Desde la Rev 0 del 25-Jun, Van Doorn emitió cuatro entregas (E14 el 16-Jun, E15 el 17-Jul, E16 el 25-Ago y E17 el 31-Ago) y L&A re-emitió cinco láminas civiles en Rev 1 con la carta `067-032-032-COR-TT-013` del 3-Sep. Ninguna estaba revisada ni registrada. Se armó primero una `Bases REV 1` sobre la copia `Bases REV 0` del repositorio; al cotejarla después contra el paquete que realmente se licitó, el encuadre cambió, esa carpeta intermedia se descartó y el entregable pasó a ser **`INGENIERIA VIGENTE PARA CONSTRUCCION`**, 88 archivos, sin Bases ni Formato.

> 🔴 **El cambio de fondo: el módulo subió 250 mm.** La fundación del contenedor pasa de la cota +6,050 a la +6,300 y el sello de +5,150 a +5,400, que es la altura de plinto que fija la Rev B del `P22-DWG-09-005-001` de BW Water. Con ella suben las cuatro cotas de tie-in del Corte A: **P8-001 de +8,250 a +8,500; P9-001 y P9-002 de +8,593 a +8,850; P9-003 de +8,583 a +8,850**. Los tie-ins 1, 3 y 6 con el Módulo 3 no cambian. Verificado por render, porque los planos son vectorizados y el diff de texto no dice nada. La ENTREGA 12 de L&A y la E16 de Van Doorn son la misma decisión aplicada en las dos ingenierías.

> 🔴 **Corrección de un hallazgo propio.** Durante la mañana reporté que al dossier mecánico del paquete le faltaban 43 de sus 58 archivos, incluidos el Cuadernillo de Soportes y todas las isometrías. **Es falso para lo que se licitó.** El paquete real, en `RESPALDO NUBE/ONE DRIVE ADASA/.../FASE_06_CONTRUCCION/BASES_OOCC_MECANICA_PIPING`, lleva el dossier mecánico **completo**: 28 isometrías, el Cuadernillo de Soportes, el PFD, los cuatro P&ID y los seis planos de cañerías. El incompleto era el respaldo `Bases REV 0` del repositorio, que fue lo que audité. Los 42 archivos comunes entre ambos son byte-idénticos: el repositorio es un subconjunto exacto de lo enviado, salvo el BL y el Formato. **La lección real es otra: el respaldo del repositorio no era lo que se envió, y nadie lo había notado en tres meses.**

> 🔴 **Lo del Formato se confirma, y es peor.** El `Formato de Presupuesto Obras Civiles, Mecánica y Piping Taltal.xlsx` que viajó lleva precio en las 41 partidas y, en el Capítulo 4, **como fórmula visible**: `=739414*1.3`. El oferente no vio un número, vio el precio base de ADASA y el factor aplicado encima. Es además una rama divergente del 19-Jun que el repositorio nunca tuvo, con defectos propios: los TAG `PE-HDPE-DN90-PN10-002` y `-003` **duplicados** en dos partidas cotizadas por separado, los códigos `4.3` y `4.7` repetidos, gastos generales al 35% y utilidad como *markup*, y sin nota al pie de cubicación. Ya está adjudicado; queda registrado y no se corrige.

> 🔴 **El hallazgo grave, que nadie había visto: el dossier civil viajó con cuatro revisiones del mismo plano conviviendo.** 48 láminas donde correspondían 18. `00-002-002 LAM1` fue en Rev C, Rev D y Rev 0; `00-001-001` en Rev B, Rev C y Rev 0. Las tandas se apilaron sin retirar la anterior y **el paquete no tiene índice**: nada le decía al oferente cuál regía. Viajaron además `P22-DWG-00-003-001` LAM1/LAM2 y `P22-ET-00-010-103`, que son la cubierta metálica CIP **descopada el 18-Jun**, siete días antes de cerrar el paquete. En total **33 documentos quedan sin efecto**. Ese conteo queda en el registro interno: **de cara al contratista la vigencia se declara en positivo**, decisión del usuario, porque listar los retirados obliga a explicar por qué existían. La planilla cambió su hoja `Retirados` por una hoja **`Vigencia`** que declara, para cada uno de los 54 documentos, la revisión que rige. Protege igual de que alguien construya sobre una Rev C, y no narra el defecto de armado.

> 🔴 **El BL contractual no desciende del `.md` del repositorio, y mi Rev 1 lo habría borrado.** Jorge Valdés editó el Word el 25-Jun y esa rama nunca volvió a la fuente. Agrega la sección **3.2 Capacidad personal clave requerida** (Administrador con 5 años, Supervisor con 3, currículum y títulos, y **calificación WPS/PQR de los operadores de electrofusión aprobada por ADASA/ITO antes de intervenir en obra**), baja el **plazo de 4 a 3 meses** en dos lugares, renombra la Sección 4 a "Alcance Montaje Incluido" y suma la Tabla 10.3 y el análisis de riesgos. Se llama `REV1` en el nombre y en el encabezado, pero su código interno sigue en `-0`. **El BL Rev 1 que generé se retiró del paquete** y quedó en `BORRADOR_REV0/_bl_rev1_no_emitido/` con un LEEME; el `.md` fuente lleva ahora una advertencia al inicio para que la próxima regeneración no repita el borrado silencioso.

> **Cubicaciones: solo la zona CIP se mueve.** La fundación de equipos del sistema CIP baja de 4,13 a **2,63 m³** de G25 y el total de la zona de 7,36 a **5,80 m³**; la excavación de esa zona de 5,01 a **1,60 m³**. Entra una junta de dilatación (poliestireno expandido de 2,5 cm, Sikaflex 1A, primer VP-215). El bloque de 0,41 m³ que aparece en la Rev 1 **no es un elemento nuevo**: es el total del emplantillado G10 que la Rev 0 no totalizaba, y L&A lo rotuló por error "TOTAL HORMIGÓN G25". Las láminas del estanque y de la bomba tienen cubicación idéntica. La del contenedor tampoco declara cambio **pese a que sus cotas subieron 250 mm**, lo que deja ese movimiento de tierra sujeto a verificación en terreno.

> **El Listado de Materiales Rev 1 mueve suministro sin mover cañería.** Los 335 m se mantienen. Salen los dos accesorios de **PVC-U**, con lo que se cierra la contradicción con la ET, que declara la instalación 100 % HDPE. Los flange LJ pasan a flange suelto para stub end DIN 16963 en acero galvanizado por inmersión; el buje Super Duplex UNS S32750 sube de 2 a 5 y el spigot saddle 4"×1" de 2 a 5; entra la unión adaptador PE100 × Super Duplex, 3 unidades. Ese archivo es el Anexo A del ET de Montaje HDPE, que en el paquete seguía Rev 0.

> 🔴 **El repositorio tenía 27 archivos de un proyecto de casi un año: el 98% de la fuente estaba fuera de git.** Lo que llenaba `git status` de entradas que nunca se resolvían no era ruido de documentos generados, como se había diagnosticado primero, sino el proyecto entero pidiendo entrar: git colapsa en una sola línea cada carpeta donde no hay nada versionado, de modo que `ENTREGAS_BWWATER/`, `REVISIONES/`, `PROGRAMA y CONTRATO/` y los correos por mes aparecían como una línea cada uno. **Entraron 896 archivos de fuente, unos 14 MB**: 433 scripts, 405 documentos `.md` escritos, más `.txt`, `.json`, `.yaml`, `.ps1` y `.sh`. `git status` quedó en **cero entradas**. 🔴 **El `.gitignore` pasó a lista blanca** —ignora todo y habilita solo las extensiones de fuente— porque la lista negra se quedó corta dos veces seguidas: primero dejó pasar `.rar` y `.pyc`, y en el segundo intento audio y video de reuniones de 47, 39 y 30 MB más familias de Revit. En un árbol de 10 GB con planos, modelos y multimedia, la lista blanca es la única que no deja pasar lo que no se declaró. 🔴 **Y el `.git` pesaba 3,1 GB con 14 MB de contenido**: eran 3.851 objetos sueltos sin comprimir. Un `git gc --aggressive` los empaquetó en **15 MB**, con `git fsck` limpio.

> **Limpieza de la raíz y el proyecto entra a control de versiones.** La raíz mostraba doce archivos que parecían duplicados de `CLAUDE.md` y `README.md` y eran **respaldos manuales acumulados**, 4,4 MB en total. La causa de fondo: **el `README.md` nunca había entrado a git**, de modo que cada edición grande dejaba una copia. El `CLAUDE.md`, que sí estaba trackeado, tenía un solo respaldo frente a los once del README. Se incorporó el README al repositorio, se creó un `.gitignore` para `.DS_Store`, respaldos `.bak`, locks de Office y corridas de auditoría, y se eliminaron los doce respaldos más los **79 `.DS_Store`** del proyecto. 🔴 **Antes de borrar se corrió un gate**: se extrajeron los encabezados de bitácora de los once respaldos y se verificó que todos tuvieran equivalente en el README vivo. Saltó uno, del 21-Ago, que resultó ser **la misma entrada reescrita y ampliada** (de "dos spools" a "tres líneas", de BORRADOR a ENVIADO); y del respaldo anterior a la reestructura, en formato antiguo, se comprobaron once piezas clave (contrato, multas, cláusulas, garantías, equipos, transmittales, baseline, contactos), todas presentes en Referencias Durables. **Dos commits**: el trabajo de la jornada, y aparte el registro de la reorganización de doce PDF a subcarpetas `pdf/` que git arrastraba como eliminados desde antes de la sesión, verificando primero que los doce estuvieran en su nueva ubicación. **Los 75 `.bak` y 92 `_pre-*` del resto del proyecto no se tocaron**: varios son respaldos deliberados con valor y merecen una pasada con criterio. **Para que no se repita, el CLAUDE.md pasa a v6.32** con tres reglas nuevas en Mantenimiento: el historial de README y CLAUDE.md vive en git y no se crean copias `.bak` antes de editarlos; antes de borrar un respaldo se corre el gate de pérdida; y se versiona la fuente y la documentación, no el derivado. **Repo `claude-memory` sincronizado** (la propuesta v9 de la skill y las seis memorias de la jornada, con cero commits pendientes de push) y **proyecto `claude-skills` reindexado** en el MCP: de 8.571 a 10.292 nodos y de 22.972 a 27.436 aristas, con la propuesta verificada como buscable.

> **El índice del paquete se eliminó y la Nota Técnica pasó a ser el único punto de entrada.** El `00_INDICE.txt` había crecido a 139 líneas y era, de hecho, una segunda nota técnica en texto plano: sus bloques de cambios y de vigencia duplicaban tres secciones de la NT, con el riesgo de que ambos divergieran en la próxima actualización. Su contenido propio se absorbió en la nota, que gana una sección **Contenido del paquete** (qué hay en cada carpeta, más las notas de formato) y una subsección **Documentos que cambian de revisión** con la tabla de los once. La NT queda en **8 páginas** y el paquete en **87 archivos**, con solo las cuatro carpetas en la raíz. Antes de borrar se respaldó el índice en `BORRADOR_REV0/_00_INDICE_absorbido_por_la_NT.txt.bak` y se verificó con 25 chequeos por frase clave sobre el PDF que ningún bloque quedara huérfano. El correo de remisión se reapuntó a la nota. Gates en verde: autochequeo del paquete, gate de vigencia con 54 documentos, `openpyxl_lint` exit 0 y veredicto `anti-ia` VERDE revalidado.

> **El paquete quedó actualizado con todo lo verificado.** Planilla, LEEME mecánico y **Nota Técnica** (que terminó la jornada en 8 páginas, PDF re-exportado desde Word con índice resuelto) dicen ahora lo mismo en tres puntos que antes faltaban o estaban mal: la brida es **la misma pieza** en ambos documentos y lo que la Rev 1 del Listado aporta es su **material, acero galvanizado por inmersión**, para el cual rige el Listado; las **empaquetaduras bajan de 45 a 42**; y el cuadernillo de isometrías tiene **siete de once láminas idénticas** más la advertencia de que en `006-011` seis de siete hojas cambiaron de número, de modo que el cotejo contra el juego anterior se hace por contenido. El correo de remisión no cambia, por ser carta de cobertura. Gates en verde: `openpyxl_lint` exit 0, `comprobar_vigencia_contra_paquete` con 54 documentos sin diferencias, veredicto `anti-ia` VERDE con voz propia revalidado tras la ampliación. **Sigue en BORRADOR: falta el nombre del contratista.**

> **Propuesta v9 para el modo drawing de `large-pdf-reader`**, en `~/.claude/skills/large-pdf-reader/PROPUESTA_v9_drawing.md`. Cinco mejoras con la brecha verificada contra el código, encabezadas por `--diff-rev`: **la skill no tiene ninguna función de comparación entre revisiones**, que es la operación central de la revisión de ingeniería y que en esta jornada hubo que construir entera a mano. Le siguen la extracción de cuadros vectorizados (`_detect_schedule_blocks` solo lee el text layer, así que una Lista de Materiales vectorizada no se extrae) y la tabla de revisiones con su estado de emisión. Documenta además los tres aprendizajes que la hacen implementable: alinear por contenido y no por número de hoja, calibrar todo umbral contra un par de control conocido, y filtrar la grilla de un cuadro por contención y no por longitud. **Es propuesta: no se tocó el código de la skill.**

> **Verificación contra las isometrías: las tuberías casi no cambian.** A pedido del usuario se compararon las 28 hojas del Cuadernillo de Isometrías del COMPILADO Rev 0 contra las 31 vigentes. **Siete de las once isometrías son idénticas byte a byte**; solo cambian `006-005`, `006-008`, `006-009` y `006-011`, con tres hojas nuevas. En `006-011` **seis de siete hojas cambiaron de número** —entra una lámina en la posición H.2 y desplaza el resto—, así que hubo que alinearlas por firma de contenido: compararlas por número habría dado un diff falso. Lo que cambia en los cuadros de materiales es menor: dos largos de espárrago que intercambian orden, uno que baja de 8 a 4 unidades y una empaquetadura que baja una. 🔴 **Se retracta el encuadre de la brida que publiqué primero.** Había reportado que las isometrías y el Listado pedían bridas distintas. **No es así: `FLANGE LJ` significa Lap Joint, que es exactamente un flange suelto**, y las perforaciones son ASME B16.5 clase 150 en los dos documentos. Es la misma pieza. Lo único que la Rev 1 del Listado agrega es **el material, acero galvanizado por inmersión**, que las isometrías no declaran; para ese dato rige el Listado, y así quedó declarado en el paquete y en la Nota Técnica. Nadie iba a comprar la pieza equivocada. **Tercer hallazgo sobredimensionado de la misma jornada**, después de los espárragos y los stub end: el patrón es afirmar divergencia entre documentos sin leer la descripción completa de ambos. Informe en `BORRADOR_REV0/_COMPARACION_ISOMETRIAS_REV0_VS_VIGENTE.md`; scripts `comparar_isometrias.py` y `comparar_bom_isometrias.py`. **Aparte:** el estado de emisión es inconsistente entre hojas de la misma revisión (`011` H.1 dice "ACTUALIZADO DONDE SE INDICA" y H.3 dice "PARA CONSTRUCCIÓN"), y el COMPILADO Rev 0 trae los 28 nativos `.dwg` que el paquete vigente no lleva.

> **Diff del Listado de Materiales, corregido tras una retractación.** El cambio real es chico: salen los dos accesorios de PVC-U y el back-up flange de 4"; los 46 flange LJ pasan a 47 flange sueltos para stub end; buje Súper Dúplex, spigot saddle y unión adaptador suben 3 cada uno; las empaquetaduras bajan de 45 a 42. **Cañería, codos, cuplas, tee, reducciones, espárragos y stub end no se mueven.** 🔴 **Se retracta lo publicado horas antes en esta misma entrada:** había reportado que los stub end se duplicaban de 47 a 94 y que los espárragos de 5/8"×170 pasaban de 8 a 64. **Las dos cifras eran falsas y de la misma causa.** Los espárragos venían en dos filas duplicadas que la Rev 1 consolidó, con el total en 232 en ambas revisiones. Los stub end se inflaron porque la descripción `FLANGE SUELTO, PARA STUB END` contiene la cadena `STUB END` y el clasificador probaba ese patrón antes que `FLANGE SUELTO`, de modo que los 47 flange sueltos se contaron dos veces. **El usuario detectó el síntoma** al observar que no debía haber tanto cambio en las tuberías para una cañería que no se movió. **La Nota Técnica, que no mencionaba ninguno de los dos, estaba correcta**; lo único que su resumen omite son las empaquetaduras. Regla que faltaba: al clasificar por subcadena, ordenar los patrones de más específico a más genérico y comprobar que ninguna descripción caiga en dos familias.

> 🔴 **Ninguna de las ocho láminas nuevas declara su estado de emisión.** Las cinco de L&A dicen "MODIFICACIONES INDICADAS" y las de Van Doorn "ACTUALIZADO" o "ACTUALIZADO DONDE SE INDICA", cuando la fila de la Rev 0 decía "APTO PARA CONSTRUCCIÓN" o "PARA CONSTRUCCIÓN". La única excepción es la isometría `06-006-008` Rev 1. El respaldo del estado es solo la carta del proyectista, y quien construye lee el plano. Observado a los dos. **Aparte:** el plano `06-006-103` que viajó en la licitación estaba emitido "PARA REVISIÓN DEL CLIENTE"; su Rev 1 del 17-Jul lo corrige a "PARA CONSTRUCCIÓN".

> **Entregables.** `INGENIERIA VIGENTE PARA CONSTRUCCION/` con cuatro carpetas: `0. CONTROL DE CAMBIOS` con la planilla `P22-LI-06-000-002-1_Ingenieria-Vigente-y-Cambios.xlsx` (Resumen, **Vigencia**, Mecánica, Civil y Cubicaciones), `1. ING. DETALLE MECANICA` con 58 archivos, `2. OBRAS CIVILES` con 18 láminas y 2 ET, y `3. ET MONTAJE`. Índice en la raíz y LEEME en los dos dossiers de ingeniería. Armado por `construir_paquete_construccion.py`, que verifica cada copia por **SHA256** y corre un **autochequeo** de tres reglas duras: una sola revisión por código y lámina, cero documentos de la cubierta, cero Bases y cero Formato. Gate `openpyxl_lint.py` en exit 0. Análisis de respaldo en `BORRADOR_REV0/_ANALISIS_CAMBIOS_REV0_A_REV1.md`.

> **El documento sustantivo pasó a ser una Nota Técnica y el correo quedó de remisión.** `P22-NT-06-000-001-0 — Ingeniería vigente para construcción`, primera NT del área 06, en `BASES DE LICITACION MONTAJE MECANICO-OOCC/NOTAS_TECNICAS/`. Seis páginas, generada con `template-adasa` y exportada a PDF desde Word real con el índice actualizado. Declara qué gobierna el alcance y qué gobierna la construcción, los tres cambios de ingeniería, el efecto sobre las partidas, la cubierta y la vigencia, y pide acuse al **viernes 11-Sep**. El correo bajó de 549 a **135 palabras**, sin tablas, en primera persona, y no repite la sustancia. Ambos en BORRADOR: falta el nombre del contratista. La carta de aclaración a oferentes quedó **sin objeto** y está archivada sin enviar en `_no_enviado_aclaracion_oferentes/`.

> 🔴 **La lectura del Formato licitado corrigió la premisa de la cubierta y reordenó toda la entrega.** La fundación de la cubierta **sí se cotizó**: es la partida **4.3, Fundación de la cubierta metálica del sistema CIP (cobertizo), 2,38 m³, $2.287.747**, con los 24 pernos F-1554 de 3/4" colados y su protección interina incluidos en el precio. Lo que no tiene partida en ninguna parte del Formato es la **estructura metálica**. De ahí sale el criterio que ordena la nota y que evita narrar nada: **el Formato fija el alcance contratado y la ingeniería vigente fija cómo se construye ese alcance**, de modo que un plano que viajó sin partida asociada nunca fue alcance, y una revisión anterior de un plano cuya partida sí existe solo cambia el documento con que se construye.

> **Dos partidas bajan de cubicación y se liquidan por obra ejecutada.** Fundación sistema CIP de 7,36 a **5,80 m³** y Excavación común de 115,1 a **111,7 m³**: $1,60 M de costo directo, del orden de **$2,4 M** con gastos generales y utilidad a los factores del propio Formato, sobre $226,7 M. La nota lo declara sin abrir negociación. **Las cantidades del Capítulo 1 no cambian**, verificado: el Cuadernillo `06-006-107` y los planos de ubicación `105` y `106` están en Rev 0 en los dos paquetes, así que los 67 soportes se mantienen; y la válvula `VM-06-010` que desaparece del Corte D no tiene partida.

> 🔴 **El Formato contractual repite dos códigos de partida:** hay dos **4.3** (fundación de la cubierta y fundación dinámica de la bomba) y dos **4.7** (dados de hormigón y relleno compactado). La nota lo advierte y fija que toda referencia vaya por número más nombre completo, en la nota y en los estados de pago. El Formato está suscrito y no se enmienda; callarlo habría producido la discusión en el estado de pago. **Defecto propio corregido de paso:** la hoja Cubicaciones de la planilla usaba una numeración corrida `4.1`–`4.14` que se desalineaba del contrato desde la cuarta fila, justamente por esos códigos repetidos, y no era citable. Quedó re-mapeada a la numeración literal.

> **Gate nuevo contra la recaída.** `generar_ingenieria_vigente.py` gana `comprobar_vigencia_contra_paquete()`, que contrasta la hoja Vigencia contra el árbol real antes de escribir y **aborta** si un código declarado no tiene archivo, lo tiene en otra revisión, o si hay un archivo en el paquete que la hoja no declara. Resuelve las tres convenciones de nombre que conviven en el paquete. Pasó con **54 documentos y cero diferencias**.

> **Compromisos.** `INT-10` pasa a **CERRADO PARCIAL**: la tabla de pesos de la Rev B se corrigió, pero vive en un BL que no se emite, de modo que el dato corregido no llegó a ningún documento en circulación. `INT-11` avanza: la Nota Particular 2 de L&A, que dejaba los pernos de anclaje pendientes de los planos vendor, desaparece en la Rev 1.

> **Pedido a L&A, en borrador.** `CORREOS/Septiembre 2026/2026-09-04/`, Reply-To al hilo de la carta `067-032-032-COR-TT-013`. Pide la re-emisión de **`P22-DWG-00-001-001` LAM1 y LAM2** en Rev 1 y consulta el cuadro de excavación de `00-002-003` LAM1 Rev 1. **Verificado plano por plano:** el cuadro de cubicaciones de la LAM1 acota la excavación del contenedor en **38,02 m³ sobre 53,51 m² de área** y la de la zona CIP en **5,01 m³**, que la Rev 1 del `00-002-007` ya bajó a 1,60; las **Secciones E y F de la LAM2** ponen el fondo de excavación del contenedor en **EL. 5,15**, contra el sello vigente de +5,400. El correo declara la reducción de unos 13 m³ como estimación de ADASA y deja el cálculo a L&A, porque la excavación tiene taludes. 🔴 **Corrección de un pendiente propio: son dos láminas, no tres.** `P22-DWG-00-002-001` se revisó y **no corresponde pedirla**: solo acota el N.T.N. por zona (+6,000 y +5,750), las coordenadas UTM y las notas generales, y el N.T.N. no se movió. Lo que subió 250 mm es el sello y la cara superior de la fundación. El correo lo dice explícito para que no la re-emitan sin necesidad, e incluye como observación de forma que el cajetín de la Rev 1 declare el estado de emisión en la fila de la revisión vigente.

> 🔴 **Pendientes que esto abre:** completar el nombre del contratista y enviar la Nota Técnica con su correo de remisión; **pedir a L&A la re-emisión de `P22-DWG-00-001-001` LAM1 y LAM2** (correo en borrador del 04-Sep): su cuadro de cubicaciones acota la excavación del contenedor en 38,02 m³ y sus Secciones E y F el fondo en EL. 5,15, ambos sobre el sello viejo. **`00-002-001` no corresponde pedirla**: solo acota el N.T.N. por zona, que no se movió; pedir a Van Doorn el PDF del P&ID `06-009-102` Rev 1, que llegó solo en DWG; y **portar al `.md` fuente los cambios de Jorge Valdés**, que hoy son deuda documentada.

### 2026-09-03 — Transmittal N38 y saldo del cierre documental consolidado: siete de doce — ENVIADO

🔴 **Lo nuevo no es el veredicto, que es bueno: es que faltan cinco documentos.** El TM N37 exigió toda la ingeniería, planos y procedimientos pendientes en una sola entrega consolidada al jueves 3 de septiembre, con una tabla de doce ítems. BW Water respondió con dos entregas —la **E89** del martes 1, con el P&ID `P22-DWG-09-009-002` Rev 0 y sus nativos de AutoCAD, y la **E90** de hoy, con diez documentos— que cubren **siete de los doce**. Los cinco ausentes son los once planos de taller `25007-ME-PI-0901-0006` a `-0016`, el informe estructural `P22-CD-09-005-001` endosado, el O&M Manual Rev B, el índice del dossier Rev C y el procedimiento de FAT del módulo; faltan además el de conservación y embalaje, la Valve List y el plan de entrega del dossier con fechas. **Los tres pendientes que el propio N37 llamó los más graves están entre los ausentes.** La Sección 3 aplica la consecuencia que el N37 ya había declarado, sin ampliarla: lo que no llegó hoy no alcanza un ciclo de revisión antes de que abra el FAT y pasa al dossier final.

**Los once documentos que sí llegaron están en buen estado, y el transmittal no levanta ningún Código 3.** Veredicto global **2 — Approved as noted**, con **8 Código 1 y 3 Código 2**. Cierran ciclos que venían largos: los tres datasheets Fedco salen en Rev 0 apto para construcción sin revisión de aprobación intermedia, con `STYLE 77` borrado de las cuatro llamadas de conexión de cada turbocargador —verificado sobre la lámina de contorno, no sobre la hoja de comentarios—; la Instrument List Rev F re-rangea `VT-09-001` a 0 a 12 mm/s rms, de modo que el disparo de 10 mm/s de la Alarm and Interlock List Rev 0 ya cabe dentro del instrumento aprobado; el formulario del procedimiento de líquidos penetrantes se emitió por fin en blanco, cerrando un punto abierto desde el N32; y la Equipment List desglosa los recipientes uno a uno, seis en primera etapa y cuatro en segunda, que es la reconciliación comprometida en la hoja de comentarios del modelo 3D.

🔴 **Los dos cierres que más pesan.** El **procedimiento de FAT del tablero** dejó de ser lo que motivó el Código 3 del N37: la Rev B eran dieciséis páginas fotografiadas con 1.378 caracteres extraíbles, once de ellas sólo con la marca de agua del escáner, y la Rev C es un documento nativo de veintitrés páginas con el lugar y la fecha del ensayo en blanco, las columnas de resultado por llenar y el punchlist vacío con sus tres casillas de firma. Y en su hoja de comentarios **BW Water compromete por escrito un segundo Factory Acceptance Test en Penang, con testigo de ADASA y de un tercero inspector, contra el procedimiento aprobado**: es la reparación del ensayo del 3 al 5 de agosto que se corrió sin aviso, y reencuadra aquel registro como informe interno del fabricante de tableros. El segundo cierre es el **HMI Display Screenshot**, que reconcilió **seis de las siete observaciones del N31**, incluida una pantalla nueva de medidor digital con tensión, corriente y potencia en kilovatios que satisface la Especificación Técnica. Su hoja de comentarios declaraba sólo dos acciones: **hicieron más de lo que declararon, y sólo se supo renderizando las pantallas**, porque los TAG viven dentro de las imágenes y sesenta de las ochenta páginas devuelven texto vacío.

**Sobre un Rev 0 no se agregan comentarios nuevos, y eso gobernó la disposición.** Siete de los once vienen emitidos para construcción. De cada uno se verificó únicamente la condición que lo había dejado en Código 2, y **ninguno la falla**, de modo que los siete van en Código 1 y ninguno lleva PDF anotado. Lo que la revisión encontró de nuevo en ellos se **documenta** en el texto de su subsección, en la Sección 3 y en el correo, sin convertirse en observación: que **la Line List Rev 1 tiene dos medidas invertidas**, sobre spools a fabricar y justo en el rotulado nuevo que la reunión del 26 de agosto pidió unificar. Ese punto se pudo cerrar con la evidencia interna del propio proveedor: la lista da 54 m³/h al rechazo CIP de primera etapa y 36 al de segunda, y el par de alta presión aprobado en Rev 0 los dimensiona DN80 y DN65, de modo que el par nuevo de baja presión está al revés y **el P&ID es el que está correcto**. El transmittal declara las medidas vinculantes —`CP-SSD-DN80-09-049` y `CP-SSD-DN65-09-048`— en vez de pedirle a BW Water que decida, que es la postura del proyecto y lo que deja la cifra escrita en el registro aunque la lista no se reemita. También se documenta que BW Water introdujo cinco cambios por su cuenta en el P&ID, entre ellos el paso de la succión de la bomba CIP de PVC a SS316 por no conseguir un reductor excéntrico, **que ADASA acepta como sustitución menor por disponibilidad** y que debe reflejarse en la Valve List y en los planos de fabricación; y que el procedimiento de penetrantes conserva el número de documento provisional en su carátula. Los tres Código 2 —ultrasonido, HMI y procedimiento de FAT— sí llevan `CC_ADASA`, con **cinco cuadros en total, los cinco verificados por render**: dos de ellos tapaban el contenido que comentaban y hubo que reubicarlos.

**Un dato que conviene tener presente al reclamar:** la columna de presión de ensayo de la Line List **no cambió en ninguna línea común** entre la Rev 0 aprobada y la Rev 1, de modo que las presiones que ADASA viene exigiendo siguen siendo las aprobadas y la Rev 1 no mueve la base de los ensayos ya reclamados. Los seis spools de super dúplex de baja presión entran además con hidrostática de 7,5 barG, que documenta formalmente la base de los ensayos que Bureau Veritas dio por conformes el 20 y 21 de agosto.

**El correo encabeza con el compromiso del proveedor, no con la exigencia de ADASA.** Las minutas del 26 de agosto y del 1 de septiembre registran con sus propias palabras que BW Water se comprometió a enviar el P&ID, la Line List y los planos de fabricación actualizados el viernes 28 de agosto, y a someter el paquete documental completo y alineado el 2 de septiembre. **Tres fechas comprometidas y ninguna cumplida**, contando la del N37. Y la consecuencia es de hoy: las dos minutas fijan a Bureau Veritas testificando ensayos el jueves y el viernes, y el mapeo de líneas y presiones que ADASA debe entregarle al inspector es justo lo que los dos documentos dicen distinto. El correo son tres párrafos y 230 palabras, con la exigencia de cerrar los submittals con documento esta semana en negrita.

**Estado:** `.md` fuente, generador, análisis interno y ledgers por entrega escritos; Word generado. **Pendiente: publicar la carpeta de anotados, pegar el enlace, exportar el PDF desde Word real y enviar.** `update_register_n38.py` queda escrito y **sin correr**, con el tally esperado **68 / 19 / 2 / 0** declarado en su cabecera y ya contrastado en seco contra el libro; los dos únicos Código 3 que quedarían son el O&M Manual y el índice del dossier, **que son dos de los cinco que no llegaron**. Registro de compromisos actualizado y regenerado, con el gate `openpyxl_lint.py` en exit 0. **Confirmar antes de enviar si Allan Valentos vuelve a la distribución**, que quedó fuera del N37.

### 2026-08-31 — Transmittal N37 y exigencia de cierre documental consolidado al jueves 3 de septiembre — ENVIADO

🔴 **Lo nuevo no es el veredicto: es la orden de dejar de entregar documentos sueltos.** Por instrucción del usuario, y por el estado de la construcción y el atraso declarado del embarque, el transmittal **encabeza su Sección 3** con la exigencia de que BW Water entregue **toda la ingeniería, planos y procedimientos pendientes en una sola entrega consolidada, a más tardar el jueves 3 de septiembre de 2026**, y el correo la lleva como **primer párrafo**. Debajo va una **tabla de doce documentos** con lo que se exige de cada uno y el transmittal del que viene, porque una exigencia que no nombra los documentos no es exigible.

**Los tres hechos que la sostienen, y ninguno es opinión.** Los documentos llegan después de lo que describen: el registro del ensayo del tablero llega ahora y el ensayo corrió del 3 al 5 de agosto; el Tie-In Point Layout llega en Rev 0 con la fabricación en curso; la I/O List llega emitida para construcción. El plazo de revisión del `25007-0088` bajo la Cláusula 37.2 vence **después** de que abre el FAT, de modo que se pide revisar el documento de puerta de una prueba ya iniciada. Y es el **quinto lote consecutivo** cuyo formulario pide devolución en tres días corridos contra los siete hábiles de la Cláusula 37.2, dos de ellos en domingo.

**La consecuencia es documental, no contractual, y por eso es sostenible:** lo que llegue después del jueves ya no alcanza a entrar en un ciclo de revisión antes de que abra el FAT y queda para el dossier final. 🔴 **No se escribe la fecha del FAT en ninguna parte**: la Nota Técnica `P22-NT-09-000-003-0`, emitida esa misma tarde por la otra cadena, pregunta cuál ventana gobierna —el Rev B la pone del 7 al 18 de septiembre y el *Progress Update* del 15 al 25—, y escribir una fecha contradiría por escrito la nota. Las únicas fechas de septiembre del cuerpo son el plazo de la exigencia y los vencimientos de la Cláusula 37.2.

**El argumento más concreto de la tabla, y va escrito:** el O&M Manual quedó en Código 3 en el TM N27 porque sus secciones 4.4 y 4.5 reproducían lógica asignada a documentos de control entonces abiertos. **Esa dependencia se levantó**: la Alarm and Interlock List y el Control and Sequence Chart cerraron en Rev 0 y Código 1 en el TM N34. Ya no hay nada que lo detenga. **El Dossier de Fabricación se declara aparte** y no entra en la entrega del jueves, porque depende de registros que se generan durante la fabricación; de él se exige el **plan de entrega con fechas por capítulo**. Exigirlo entero en tres días sería refutable de inmediato.

**El veredicto.** Submittals `25007-0086`, `25007-0087` y `25007-0088` (E86, E87 y E88, del 27 y 28 de agosto), **siete documentos**. Veredicto global **3 — To be revised: 2 Código 1, 4 Código 2 y 1 Código 3**. El código lo fija **un solo documento**.

🔴 **El PLC/LCP FAT Procedure Rev B no es un procedimiento: es el registro de un ensayo ya ejecutado.** El ensayo de hardware del tablero corrió del **3 al 5 de agosto en Ningbo** y se somete veintitrés días después. La casilla *Witnessed by (Client / Third-Party Inspector)* la firma personal de BW Water y la casilla *Accepted by (BW Water)* la firma el proveedor del tablero: **las tres firmas del cierre pertenecen a la cadena de suministro**. La fila 6.2 del ITP `P22-BA-09-000-004` Rev 0, en Código 1, asigna a ADASA el testigo sobre ese ensayo y su leyenda lo define como inspección que **requiere aviso**; la fila 7.1 es punto de detención sobre la aprobación del procedimiento detallado. **El encuadre se cuidó**: la propia leyenda dice que el ensayo se ejecuta en su fecha aunque el cliente no esté presente, de modo que se reclama por **el aviso** y no por la ejecución; reclamar por la ejecución sería refutable con el mismo ITP. Diez ítems del punchlist están marcados categoría A —*"Must be resolved BEFORE panel dispatch"*— y **ocho quedan con fecha objetivo, fecha real y estado en blanco**, con el bloque de cierre vacío y un reporte de rectificación anexo sin firma, sin fecha y sin testigo.

**Dos cierres largos.** El Instrument Location Layout sale del Código 3 que cargaba **desde el TM N23** y el Tie-In Point Layout llega a Rev 0 declarando la presión de diseño del punto de alimentación de salmuera en **5 barG**, que coincide con la Line List Rev 0 aprobada en Código 1: la aceptación condicionada de ADASA a la clase ANSI 150 queda satisfecha. Los dos procedimientos de ensayos no destructivos que volvieron **cerraron su determinante** y suben de Código 3 a Código 2; el de espesor por ultrasonido no se sometió y sigue abierto.

🔴 **Dos afirmaciones del análisis interno se corrigieron antes de emitir, verificándolas por render propio.** El análisis del 28-Ago decía que el bloque `REVISIONS` del Instrument Location Layout seguía **vacío**; el render del cajetín muestra **cuatro filas** —D `AUG.24.26`, C `JUN.16.26`, B `FEB.27.26`, A `JAN.17.26`— todas repitiendo la misma descripción `ISSUED FOR APPROVAL`. El `_LEDGER_COMENTARIOS.md` de la ENTREGA 86 lo tenía bien y el análisis no. Emitir "vacío" habría sido refutable de un vistazo. Se confirmó además, contrastando contra la Rev C emitida, que **la fila histórica se reescribió**: decía `APR.17.26` y ahora dice `JUN.16.26`, de modo que la emisión de abril desapareció del historial en vez de distinguirse de la de junio, que era exactamente el punto de la observación original. La segunda corrección es de cifra: el punchlist del FAT marca **diez** ítems categoría A, no ocho; ocho son los que quedan en blanco, y las líneas 9 y 12 sí llevan fecha y dicen DONE.

**Lo que el registro del FAT deja probado, y se verificó sobre los tres documentos:** su Sección 8 visa los canales 1 a 4 del módulo `-A2` con los TAG `XT001`, `XA002`, `XT002` y `XT003`; la **I/O List Rev 6** muestra `XA002`, `XT002` y `XT003` **tachados en rojo** como eliminados en la revisión 6 y no tiene fila `XT001` para el tablero; y el **esquemático Rev B** conserva esos cuatro TAG en las entradas 1 a 4 del mismo módulo rotulados `SPARE`. En salidas, el canal 7 del módulo `-A4` con el relé `KA8` se visa como reserva en el registro mientras el esquemático cablea ahí el comando del calentador de CIP. **Tres documentos, tres estados, los mismos bornes.** La afirmación defendible no es que el tablero se construyó distinto de los planos —el cuerpo ejecutado del FAT no cita la lista por código ni por revisión—, sino que los tres se contradicen y ninguno declara cuál gobierna. Compromiso nuevo `PRG-44`.

🔴 **La decisión del terminal de operación queda abierta a propósito.** ADASA declaró vinculante el `2711P-T10C22D9P` en el TM N30 y el registro del FAT prueba que **el tablero se armó con el `-D8S`**, de un puerto Ethernet y 512 MB. Exigir el cambio a días del FAT tiene impacto de plazo; aceptarlo en silencio renuncia a una declaración propia. El transmittal **no elige**: pide que BW Water declare por escrito cómo cierra la brecha y cómo el terminal suministrado cumple los dos puertos del datasheet aprobado. Los dos caminos siguen disponibles.

**Cinco PDF anotados, veinte cuadros, todos verificados por render.** El del FAT es un documento **fotografiado** —once de sus dieciséis páginas devuelven solo la marca de agua de CamScanner—, de modo que sus siete cuadros van con posición fija y se comprobaron uno a uno sobre la imagen. En el Instrument Location Layout el ancla se movió del bloque de revisiones al rótulo del título, porque anclarla ahí dejaba la caja encima de las mismas filas que comenta.

**El correo es carta de cobertura y nada más.** Por instrucción del usuario salió del cuerpo todo lo que repetía sustancia del adjunto —los tres hechos que fundan la exigencia, el O&M Manual, el detalle del Código 3 y los vencimientos de la Cláusula 37.2—, y quedó en **dos párrafos, 206 palabras** contando encabezado, viñetas y firma. Lo único que se repite a propósito es **la orden**, con su consecuencia, porque tiene que leerse sin abrir el adjunto; el resto remite a la Sección 3.

**Archivos.** `REVISIONES/TRANSMITTALES/P22-TM-09-000-037-0/` con el `.md` fuente, `crear_transmittal.py`, el Word de siete secciones y la subcarpeta `COMENTARIOS/` con los cinco scripts, los cinco `CC_ADASA` y los renders de verificación. Correo en `CORREOS/Agosto 2026/2026-08-31/`. `update_register_n37.py` queda **escrito y sin correr**: el tally esperado se declara en su cabecera —**64 / 21 / 4 / 0**— y la regla del proyecto es aplicarlo después de enviar.

**ENVIADO el lunes 31-Ago a las 18:27 de Chile**, con el transmittal en PDF de **11 páginas** como único adjunto —índice resuelto desde Word real— y los cinco `CC_ADASA` por enlace de descarga, verificado carácter a carácter sobre el `.docx` y sobre el PDF emitidos y de nuevo sobre el respaldo, no sobre el script, que es el modo de falla del N30, N31 y N32. **Cuerpo íntegro**, los trece párrafos palabra por palabra. 🔴 **El usuario amplió bastante la distribución**: cinco destinatarios en vez de dos, porque los tres de ADASA y Fitri Indriyani subieron de copia, y nueve en copia con seis nombres nuevos de BW Water; **Allan Valentos quedó fuera por completo**. El asunto salió **íntegro, con el discriminador**, a diferencia de los otros tres correos del día: la orden se lee desde la bandeja sin abrir el adjunto. **Master Register aplicado**: el tally obtenido coincide con el declarado antes de correr y el gate quedó en exit 0.

### 2026-08-31 — BW Water corre el embarque al 28 de septiembre alegando clima, y ADASA responde con la Nota Técnica 003 en versión suave — ENVIADO

**El aviso.** Eduardo Yamauchi informó el lunes 31-Ago a las 15:29 de Chile que la *System Readiness Shipping Date* se corre **del 21 al 28 de septiembre** y que la fabricación en Penang pasa del 28 de agosto al 4 de septiembre, *"due to weather conditions — the challenge is the consistent rain and humid conditions"*. Adjunta el *Progress Update* del 28-Ago, producido el 29.

🔴 **Decisión del usuario que gobierna toda la respuesta: no comprometer la entrega del 28.** Se redactó una primera versión dura —diez puntos, citas literales de las Cláusulas 27 y 44, tabla de 44 y 51 días de desviación, plazo al viernes 4 y reserva de la Cláusula 49— y **no se emitió**. El objetivo del documento pasa de disputar la fecha a **asegurarla**, conservando la posición contractual en una sola frase neutra.

**El reencuadre que hace que suave y útil sean lo mismo.** Dos de los tres hallazgos no atacan la fecha, la amenazan: el cronograma del propio proveedor cierra el FAT el 25 de septiembre y pone el ready-to-ship del 26 al 28, o sea **tres días**; y programa la instalación de la bomba de alta el **9 y 10** mientras su flete aterriza el **11**. Preguntar por eso protege el 28. El punto del pintado y el interrogatorio de la Cláusula 44 miran al pasado y solo asignan culpa, así que salieron.

**Nota Técnica `P22-NT-09-000-003-0`**, *Clarifications to Secure the Ex-Works Date of 28 September 2026*, en `REVISIONES/NOTAS_TECNICAS/`. Inglés, template ADASA con índice, **cuatro páginas, 486 palabras de cuerpo y cinco puntos** (la versión dura tenía 1.050 y diez). **La tabla hace el trabajo**: las cuatro fechas de septiembre del propio adjunto puestas en orden cronológico —flete el 11, instalación de la bomba el 9 y 10, FAT del 15 al 25, ready-to-ship del 26 al 28— muestran solas que la bomba se instala antes de llegar y los tres días que quedan hasta el embarque, sin una palabra acusatoria. Cinco puntos en tres bloques: la ventana del FAT, la secuencia de llegada e instalación, y la información de embarque que ADASA necesita. Respuesta pedida **con el próximo reporte semanal y antes de que abra el FAT**, sin plazo impuesto.

**Correo de remisión ENVIADO el 31-Ago a las 17:12 de Chile**, 144 palabras, dos párrafos, sin viñetas y sin tabla, reply al hilo del Progress Update, con la Nota Técnica adjunta en PDF. El usuario ajustó al enviar: solo Eduardo en destinatario, Stephane a copia, y el asunto quedó sin discriminador para no romper el encadenado. Cuerpo verificado íntegro contra el `.docx`; respaldo archivado. Abre con el objetivo compartido —*"We are working with you so that the 28 September holds"*— y nombra los tres puntos en una línea cada uno.

**La única frase con efecto contractual, y va una sola vez** en cada documento: *"Taking note of the revised date does not constitute acceptance of a new contractual date, nor a waiver of any right under the Contract."* Sin números de cláusula, sin la palabra multa y sin mencionar el 21 de septiembre. **Sin ella, el 21 y el 28 se consolidarían por silencio** y se perdería la posición que `PRG-07` y `PRG-08` vienen sosteniendo desde julio. Barrido de tono sobre los dos documentos: `does not accept`, `reject`, `breach`, `penalty`, `Clause 4x`, `non-compliance` y `deadline` devuelven **cero**.

---

**🔴 Lo que se retiró del documento emitido, que sigue verificado y disponible.** Queda aquí y en la nota de `PRG-41`, y se repone si la fecha vuelve a moverse o si la respuesta no llega antes de que abra el FAT:

- **El pintado del contenedor.** El Project Schedule Rev B que BW Water sometió el **24 de agosto** proyectaba la tarea *Container Painting (at Vendor Shop)* del **13 al 21 de agosto** y la reportaba al **0 %**, en un documento con fecha de corte del 18. Diez días después de la fecha que él mismo declaraba, la lluvia aparece como causa. **Esa actividad no tiene línea base en ninguna de las dos revisiones** —inicio y fin en NA—, de modo que no puede oponerse como desviación contra una referencia acordada; su duración pasó de **8 a 20 días**. El rótulo de la propia tarea dice que se ejecuta en el taller de un proveedor de pintura.
- **La Cláusula 44 excluye el clima por defecto.** Abre así: *"No serán admitidos por el Comprador los retrasos originados por acontecimientos o condiciones especiales desfavorables, de cualquier naturaleza que estas sean, a menos que las mismas tengan su origen en causas de Fuerza Mayor."* La Fuerza Mayor remite al **artículo 45 del Código Civil** (imprevisto **e** irresistible) y su reconocimiento exige aviso **dentro de 48 horas** con los detalles completos, prueba de que impidió realmente el cumplimiento, prueba de las precauciones previas y acuerdo con el Comprador. El correo del 31 no la invoca ni cumple ninguno de esos requisitos. Refuerzo: la declaración jurada de la oferta, que la BAE hace prevalecer sobre cualquier otro documento, asigna al Proveedor *"la responsabilidad total de haber previsto cualquier dificultad y costo"* y declara su obligación **de resultado**.
- **La magnitud real, contra la línea base del propio proveedor:** **44 días** en el ex-works (15-Ago contra 28-Sep), **43** en el FAT (13-Ago contra 25-Sep) y **51** tanto en la entrega en sitio (30-Sep contra 20-Nov) como en el fin de programa (19-Nov-2026 contra 9-Ene-2027).
- **El aviso llegó tarde.** El cronograma está fechado el 28 y se produjo el 29; el aviso entró el 31 a las 15:30. La Cláusula 26 obliga a informar por escrito **sin dilación alguna**.
- **El umbral de los treinta días de atraso se cumple el jueves 3 de septiembre**, y con él se abre la causal de término anticipado por atraso de la BAE. La Cláusula 49 no se disparó ni se mencionó; el precedente del instrumento está en `CORREOS/Febrero 2026/2026-02-14_Escalation-Plan/`.

---

**Dos cambios que el aviso no declara, y que sí entraron al documento** porque amenazan la fecha: la ventana del **FAT** se movió del **7 al 18 de septiembre** del Rev B al **15 al 25** en el adjunto (`BV-13`, cuarta reprogramación), y el inspector se agenda contra esa ventana por Bureau Veritas Chile; y la instalación de la **bomba de alta** está programada el **9 y 10** mientras el flete aéreo de esa bomba y de los dos turbocargadores aterriza el **11**.

**Lo que ADASA reclama y lo que no.** El barrido del repositorio **no encuentra reserva de bodega, naviera, booking ni forwarder contratado**, así que no se afirma pérdida de flete. Lo que sí consta y sí se pide es el *loading schedule* y el *vessel closing date*, solicitados **desde el 21 de julio** y sin los cuales ADASA no posiciona contenedores ni reserva nave bajo EX Works (`PRG-42`, con fecha por primera vez).

**El correo contractual del 26-Ago queda SUPERADO** y no se envía: sus cifras cambiaron y su plazo del 2 de septiembre nunca corrió. Sus tres preguntas se absorben, aunque la de la certificación de recipientes y el desglose del tramo de embarque quedan **fuera del documento suave** y se reponen con el resto del material retirado.

🔴 **`INT-08`: la Notificación de Adjudicación no está en el repositorio.** Verificado el 31-Ago. Hay que pedirla a Abastecimiento; sin ella no se cursa ninguna cifra de multa, porque calcular sobre el rótulo del cronograma del proveedor deja el reclamo atacable.

**Registro de compromisos, corte 31-Ago:** `PRG-08` pasa de 21 a 28-Sep con su primera reprogramación y su acción queda **cubierta por la reserva de posición**, no por el rechazo expreso que pedía, y eso queda escrito; `PRG-07` registra lo mismo; `PRG-01` suma su tercera reprogramación; `BV-13` la cuarta; y entran `PRG-41` (los cinco puntos que aseguran el 28, ALTA, con el material retirado guardado en su nota) y `PRG-42` (*loading schedule* y *vessel closing date*, ALTA). Gate `openpyxl_lint.py` en exit 0.

**Se marcaron como ENVIADOS** los dos correos del 31-Ago del frente de inspecciones. Falta archivar sus respaldos y con ellos la hora.

### 2026-08-31 — Bureau Veritas entrega el set completo IR001 a IR009 y se descubre que los ensayos de alta de la semana pasada no se hicieron — ENVIADO

**El hallazgo operativo, que es lo urgente.** Los ensayos de alta presión comprometidos para el viernes 28 no se ejecutaron. El informe de ese día, el `BVM-IR009`, registra un ensayo de **baja** presión sobre el carrete de PVC `DA-PVC-DN100-09-001` a 7,5 barG, y el `BVM-IR008` del jueves 27 otro igual sobre `DA-PVC-DN100-09-002`. El `AQ-QAM-F027` del viernes declara `Inspection Item: 1- HP and LP pressure test` y se cerró como **Accepted** con la sola nota manuscrita del ensayo de baja. **Desde el 20 de agosto no se ha ejecutado ningún ensayo de super dúplex**, y de las once líneas del proyecto una tiene ensayo conforme, tres deben repetirse y siete no se han ensayado nunca. La fila 5.2 del ITP sigue abierta con el FAT del módulo abriendo el 7 de septiembre.

🔴 **El punto que corre riesgo físico.** El registro de la reunión de coordinación del 26 de agosto recoge la presión de ensayo del super dúplex "definida en 135 bar" y califica de incorrecto el ensayo a 90 barG del 20 de agosto. **Las dos cosas son al revés**: 90 barG es 1,5 × 60 de diseño y es el único ensayo que califica hasta hoy; los 135 barG corresponden solo a las cuatro líneas de 90 barG de diseño, y aplicarlos parejo sometería a **siete de las once** a sobrepresión, hasta 2,7 veces el diseño en las salidas de los dos Fedco. Es el mismo modo de falla del hallazgo crítico del TM N27, ahora por el lado contrario. Con el ensayo programado para el miércoles 2, la corrección encabeza el correo del día.

**Lo comprometido para el viernes 28 tampoco llegó.** Las acciones 5 y 9 de esa reunión —el P&ID, la Line List y los planos de fabricación con la numeración de línea unificada, y la presión de ensayo exacta por carrete— vencieron sin entrega. Los tres submittals recibidos el 28 (`25007-0086`, `-0087`, `-0088`) no traen ninguno de los tres documentos. Sin la numeración unificada no hay contra qué verificar el ensayo del miércoles, que es exactamente la causa raíz que se acordó cerrar.

🔴 **Bureau Veritas cumplió cuatro de las seis peticiones del 21 de agosto, y eso solo se ve por render.** Carlo Montecinos remitió el lunes 31 a las 14:47 el set completo de los nueve informes, con el `IR005` y el `IR006` en revisión 01, respondiendo a la petición de Luis Rivera del viernes 28 a las 14:42. **La primera lectura, hecha sobre texto extraído, concluyó que la reemisión no había cambiado el resultado, y es falso**: el render muestra que el `IR005` pasó de `Satisfactory (Without comments)` a **`Not Satisfactory`** y el `IR006` de `Satisfactory with comments` a **`Not Satisfactory`**. El formulario `GM-SI-101 INSP002-En` dibuja sus casillas como vectores y el texto plano devuelve las tres opciones sin decir cuál está marcada. Cerraron además la tabla de presiones contra la Line List, la incorporación del P&ID `P22-DWG-09-009-002` Rev D y la Line List `P22-LI-09-009-003` Rev 0 a la sección B, y —desde el `IR008`— la fotografía rotulada como identificación del carrete, con la marca manuscrita visible. `BV-24` pasa a **CERRADO PARCIAL**.

**Lo que queda abierto es una contradicción del propio formulario reemitido.** Los dos informes marcan `Not Satisfactory`, que el formulario define como *NCR raised during the inspection*, y tres líneas más abajo marcan **No** en `Open Non Conformities`, con la sección G en `N/A`. El argumento sale del documento y no de una interpretación. Y el `BVM-IR007` del 24 de agosto **repite el defecto tres días después del reclamo**: marca `Satisfactory (Without comments)` mientras su propio resumen declara el resultado no satisfactorio, sobre un hallazgo real —la parte inferior del marco del skid no alcanza los 355 micrones de espesor de película seca—, y deja las casillas de No Conformidad y punch list en No. Se abre `PRG-40` por el retrabajo del marco, sin fecha, porque ADASA aún no lo ha reclamado por escrito al proveedor.

**Errores de registro del propio resumen de Bureau Veritas.** Su cuadro declara la visita del 14 de agosto como *"Witnessed High Pressure piping pressure test — Satisfactorio"*; el `BVM-IR004` dice en su sección E1 que ese ensayo no pudo ejecutarse y que se sustituyó por examen visual y dimensional. Control documental: los once informes conservan `Revision No. 0` en su campo de revisión, de modo que la revisión 01 existe solo en el nombre del archivo, y el `IR006` Rev 01, el `IR007` y el `IR008` llevan el número del `IR005` en el encabezado de páginas interiores —en el `IR007` son las cinco páginas interiores, solo la portada lleva su propio número.

**Hallazgo colateral del `IR004`, que no se emite y queda como munición**: el inspector aceptó ajuste y examen dimensional contra los planos de taller `25007-ME-PI-0901-0007`, `-0009` y `-0010`, que pertenecen al conjunto de diecisiete láminas nunca sometidas a revisión y estampadas FOR CONSTRUCTION del TM N30, abierto en `PRG-21`.

**Lo favorable, que también consta y se dice en los dos correos.** El inspector asistió a las nueve jornadas, firmó y timbró los registros, revisó los certificados de calibración y fotografió los escalones con hora. La instrumentación es WIKA calibrada por Trescal con trazabilidad a NMIM y KRISS. Y **las dos jornadas de baja presión del 27 y del 28 están bien ejecutadas y cierran la parte de baja presión del alcance que el Inspection Request 003 recortó el 5 de agosto**, que ADASA venía reclamando en `PRG-13`. Objetarlas habría sido reclamar contra lo que pedimos nosotros.

**Ordenamiento del frente.** El árbol de `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/` queda con una carpeta por informe, `IR001` a `IR009`, cada una con el informe, su anexo y `md/`; el `IR005` y el `IR006` conservan las dos revisiones porque la comparación entre ellas es la evidencia del cierre parcial; el `IR005` y el `IR009` incorporan además el registro de ensayo del fabricante de su jornada. Deduplicado por hash md5 contra todo el árbol: las copias de `general/`, `inspeccion 009` e `INSPECTION 03` son payload idéntico y las carpetas por hilo de correo se mantienen, porque el mapa del frente (`REQUEST WITNESS INSPECTION/_ORIGEN.md`) las referencia. Análisis y renders de verificación en `_REGISTRO_INSPECCIONES_BV.md` y `_render/`. **Cinco informes que nunca se habían analizado —`IR003`, `IR004`, `IR007`, `IR008` e `IR009`— quedan revisados.**

**Dos correos ENVIADOS el 31-Ago** desde `CORREOS/Agosto 2026/2026-08-31/`, en cadenas separadas, con respaldo archivado y cuerpo verificado íntegro contra su `.docx`: el de los ensayos de alta a las **15:59** y el del set de informes a las **16:15**, este último con su anexo de 148 KB adjunto. El usuario ajustó la distribución al enviar: el primero salió sin línea de copia y el segundo con copia solo a Jaime Martínez.

- **A BW Water** (`2026-08-31_HP-Tests-Programme.docx`, 565 palabras, inglés), **suelto y no como respuesta**, con asunto propio `25007 TALTAL - Super duplex test pressures and test programme for 2 to 4 September`: el hilo del Request 003/004 ya no aparece en la bandeja, así que la trazabilidad se ancla por fecha y por código dentro del cuerpo. Tres cargas: la presión vinculante por línea con tabla de las once y la advertencia de sobrepresión; las dos acciones vencidas el viernes 28; y el programa del 2 al 4 de septiembre día por día, con la solicitud de atestiguamiento al inspector y ADASA en copia, las tres repeticiones, `CP-SSD-DN65-09-045` que sigue retenida, y la hidrostática del RO Vessel, fuera de alcance desde el 5 de agosto. **Plazo al martes 1 de septiembre en hora de Penang**, que va doce horas adelante y es el único día hábil completo antes del ensayo. **No se cita el registro de la reunión del 26**: es un resumen automático interno, no una minuta oficial del proveedor, y la regla del proyecto prohíbe citarle documentos internos.
- **A Bureau Veritas Chile** (`2026-08-31_BV-Set-Informes-IR001-IR009.docx`, 401 palabras, español, versión ejecutiva), por la cadena del Request 006, a Carlo Montecinos con Jaime Martínez y Víctor Gutiérrez en copia, sin nombrar al fabricante. Reconoce lo cerrado primero, cobra la No Conformidad con el argumento del propio formulario, el `IR007` y las dos correcciones de registro. **Adjunto**: `Anexo_Registro_Inspecciones_IR001_IR009.pdf`, cinco páginas, código `ADASA-BV-REGISTRO-INSPECCIONES-Rev0` siguiendo la convención propia del frente, exportado desde Word real y revisado por render.

Los dos correos en `anti-ia` modo revisar: **VERDE**, voz propia calibrada contra los enviados del 20 y del 21 de agosto de sus respectivas cadenas.

**Registro de compromisos actualizado**, corte 31-Ago: `BV-24` a CERRADO PARCIAL con la evidencia de los cuatro puntos cerrados; `PRG-34` con su **segunda** reprogramación al martes 1-Sep y `PRG-36` con la primera; `PRG-13` con la tercera y el cierre parcial de la baja presión; y cuatro compromisos nuevos, `BV-25` (No Conformidad y reemisión del `IR007`, al viernes 4-Sep), `PRG-38` (programa del 2 al 4 y solicitud al inspector, al martes 1-Sep), `PRG-39` (P&ID, Line List y planos con numeración unificada, al martes 1-Sep) y `PRG-40` (espesor del marco, sin fecha). Gate `openpyxl_lint.py` en exit 0.

**Pendiente de la sesión anterior, sin resolver acá:** el Transmittal N37 sigue en análisis interno del 28-Ago y las entregas 86 a 88 no tienen entrada de Bitácora propia.

### 2026-08-26 — Entregas 82 a 85 revisadas, Transmittal N36 enviado y exigido el cierre en Rev 0 de los tres equipos Fedco — ENVIADO

Cuatro entregas llevaban entre dos y seis días sin responder y ninguna tenía carpeta de revisión: `25007-0082` (21-Ago, UHPRO Structural Design Criteria Rev 0), `25007-0083` (21-Ago, Piping Layout Rev D y 3D Model Rev B), `25007-0084` (24-Ago, GA of SWRO System Skid Rev 0, GA of Antiscalant Dosing Tank Rev C y Project Schedule Rev B) y `25007-0085` (26-Ago, los tres datasheets Fedco en Rev E). **Nueve documentos en un solo transmittal**, el lote más grande desde el TM N26, emitido dentro de los cuatro vencimientos de la Cláusula 37.2. El transmittal **dispone ocho**: el Project Schedule Rev B se retiró por decisión del usuario, porque su seguimiento se lleva por la reunión semanal de coordinación.

**Veredicto global 2 — Approved as noted: 3 Código 1 y 5 Código 2. Ningún documento vuelve a revisión.** Paquete en `REVISIONES/TRANSMITTALES/P22-TM-09-000-036-0/` (transmittal de nueve páginas, `_ANALISIS_N36.md`, cuatro `CC_ADASA` con sus scripts y renders de verificación), ledgers de cierre en las cuatro carpetas de entrega, y los dos correos en `CORREOS/Agosto 2026/2026-08-26/`.

🔴 **El punto más grave: el hito documental de los tres equipos Fedco.** La bomba de alta `BH-09-001` y los dos turbocargadores `SIP-09-001` y `SIP-09-002` están **comprados, fabricados y a días de montarse** —el cronograma del propio proveedor programa la instalación de la bomba dentro del contenedor del 3 al 5 de septiembre y la apertura del FAT el 7— y sus tres hojas de datos siguen llegando **en Rev E, sometidas para aprobación**. Fueron aprobadas en Código 2 en Rev D en el TM N11, con una sola nota menor cada una, y el equipo se compró y fabricó sobre esa base. El transmittal exige **emitirlas en Rev 0 apto para construcción antes de que abra el FAT el 7 de septiembre**, con bloque propio en el Resumen Ejecutivo y bloque de acción con fecha en las tres subsecciones, y declara que ADASA no seguirá recibiendo y devolviendo revisiones de aprobación de hojas de datos de equipos en camino al montaje. Compromiso `PRG-37`, crítico. El dato más incómodo **no se emitió**: su propio cronograma declara este ciclo de revisión y aprobación cerrado al 100 % desde el 16 de abril, y citarlo habría reintroducido en el transmittal el documento que acabábamos de retirar. Queda como munición para la reunión semanal.

**El segundo frente: el GA of SWRO System Skid Rev 0**, único del lote emitido para construcción, de modo que las tres referencias que constituían íntegramente su Código 2 del TM N31 vencieron en esta emisión y **solo una se corrigió**. La nota 7 quedó bien en las dos hojas; la nota 6 solo en la Hoja 2, que ahora remite la misma matriz de instrumentos a dos revisiones distintas; y la nota 8, la que apunta al espesor nominal por línea, cita un código que no existe en la numeración del proyecto. **La captura que BW Water adjunta para justificar la nota 8 escribe ese mismo código con tres dígitos**: la evidencia que invocan confirma el punto. **Se dispone en Código 1 y no en Código 3**, y esa fue la segunda corrección de calibración del ciclo: el plano está en Rev 0 emitido para construcción y los dos puntos son de cita y no de contenido, con los documentos referidos identificables, así que no se retiene un plano que ya gobierna fabricación por una errata. Bajar el código no bajó el tono: el transmittal dice que de las tres referencias solo una se corrigió, que su propio anexo refuta su respuesta, y escribe literal el código correcto `P22-ET-09-006-001` para que quede en el registro aunque el plano no se reemita nunca.

🔴 **La calibración se corrigió dos veces antes de emitir, y ahí está el aprendizaje de método del ciclo.** La primera disposición llevaba **cuatro Código 3**. La verificación adversarial mostró que tres recaían sobre revisiones sometidas **para aprobación** —Piping Layout Rev D, modelo 3D Rev B y Project Schedule Rev B— cuyas condiciones vencen al emitir Rev 0 según la frase literal que ADASA misma escribió: *"Action to issue at IFC Rev 0 — no new revision required"*. Escalar habría contradicho esa frase y ordenado una revisión que ADASA declaró innecesaria. Las tres quedan reiteradas en **Código 2**, con constancia de que es el segundo ciclo en que siguen abiertas. **La regla que queda escrita: la columna de emisión del Submittal Form decide el código.** IFC significa que el plazo venció y quedan Código 1 o Código 3; IFA significa que la condición se reitera en Código 2.

🔴 **La segunda corrección la puso el usuario sobre el Código 3 que había sobrevivido.** Los dos puntos del GA of SWRO System Skid son **de forma** —una errata de un dígito en un código cuyo título coincide, y un índice de revisión desactualizado en una de dos hojas— y el plano **está en Rev 0 emitido para construcción**: no se devuelve a revisión por eso, porque retener un plano que ya gobierna fabricación cuesta un ciclo y no corrige nada físico. **Segunda regla que queda:** sobre un Rev 0 el Código 3 se reserva a un defecto sustantivo de contenido, y un defecto de forma se dispone en Código 1 **enunciándolo con fuerza en el texto**, porque bajar el código no es bajar el tono y callarlo lo daría por aceptado. **Resultado final: ningún Código 3 y veredicto global 2.**

**Cuatro cifras propias se corrigieron en la misma pasada**, todas registradas en la Sección 13 del análisis. Los conteos de objetos del modelo se habían tomado del número de **filas** del volcado de propiedades, donde cada objeto genera unas veinte: decían 110 objetos en la línea `09-015` donde hay **tres**, y 5.033 en la `09-001` donde hay **133**. La afirmación de que ningún TAG con interrogación se había corregido era falsa: **los siete de válvula sí cerraron**, donde el TM N30 había nombrado uno solo. Las presiones que el TM N11 rotuló como de entrada en los turbocargadores son de descarga. Y los acoples aceptados son Piedmont Pacific, no Victaulic.

**Los hallazgos de fondo, por documento.** En el **modelo 3D**, la hoja de comentarios declara *"fifty-seven objects tags corrected with the question marks removed"*: esos cincuenta y siete son **soportes de cañería**, ninguno se tocó y ahora son setenta y dos; ningún soporte del modelo lleva TAG en ninguna de las dos revisiones. Sigue además la colisión del correlativo `09-001` entre `DA-PVC-DN100-09-001` y `RD-PVC-DN15-09-001`, que no figura en la Line List aprobada en Código 1 y que el Piping Layout Rev D propaga en sus tres láminas, con la fabricación de spools al 70 %; y las propiedades de publicación del archivo siguen declarando el título `V16 TALTAL` sin índice de revisión. En el **Project Schedule Rev B**, retirado del transmittal pero verificado igual, no hay una sola ocurrencia de `ASME`, `stamp`, `certif`, `waiver`, `hydro`, `pressure test` ni `leak` en catorce páginas, con los recipientes ya fabricados y recibidos en Penang al cien por ciento. La evidencia se conserva en `ENTREGAS_BWWATER/ENTREGA 84/_cronograma_fuera_de_transmittal/` para la reunión semanal. En el **Piping Layout Rev D**, la tabla de tie-in se agregó pero no cubre ninguna de las siete líneas de CIP que rotula esa misma lámina y sus cinco cotas de elevación no declaran datum, con los tres bloques de notas vacíos.

**La recuperación del lote es el GA of Antiscalant Dosing Tank Rev C**, que **sube de Código 3 a Código 2** entregando las cargas de reacción sísmica, el patrón de anclaje con un detalle de empotramiento nuevo, el volumen útil efectivo y el TAG del equipo. Le quedan dos residuos menores sobre el propio detalle que se pidió agregar. Y el **datasheet de la bomba de alta sube de Código 2 a Código 1**: reconcilió el fabricante del motor en los dos bloques de datos y en la lámina de contorno.

**Cuatro de los ocho documentos dispuestos llegan sin hoja de comentarios consolidada**, entre ellos el UHPRO Structural Design Criteria, que la traía en la Rev B con nueve entradas y la perdió al emitir Rev 0. Donde la hay no siempre transcribe lo que se pidió: la del Piping Layout recoge una de las tres condiciones del TM N30 y la del modelo omite por completo el requisito de identificación del archivo.

**El cronograma sale del transmittal.** Por decisión del usuario del 26-Ago, el seguimiento del Project Schedule se lleva por la **reunión semanal de coordinación**. El transmittal lo declara en una línea del Resumen Ejecutivo y no le asigna código, para que BW Water no quede esperando uno. En el Master Register se registra la entrega —Rev B, ENTREGA 84— conservando el TM y el veredicto del N20, y no entra al Revision History, donde cada fila es un ciclo con veredicto. El **correo contractual** que se había preparado sobre el mismo documento —ex-works Penang del 15-Ago al 21-Sep, entrega en sitio al 13-Nov, fin de programa al 2-Ene-2027, más 44 días, con reserva bajo la Cláusula 27, la 43.1 letra b y la 43.4 y **sin cursar cifra**— queda **en borrador y su envío por decidir**, dado que el tema se ve en la reunión.

**Recorte ejecutivo antes de emitir, a petición del usuario.** El transmittal bajó de **3.223 a 2.122 palabras de prosa** —34 % menos— y de once a **nueve páginas**; el correo de cobertura, de 525 a **242 palabras de cuerpo**. Lo recortado es duplicación, no contenido: el GA del skid se contaba dos veces y el hito Fedco cuatro entre el Resumen Ejecutivo y la Sección 2, y ahora el titular va una vez en la Sección 1 y el detalle una vez en la 2, con cada subsección de vuelta al patrón de código, Status corto y bloque de acción. Los diez hechos que no podían perderse se verificaron uno por uno sobre el `.docx` emitido, y el `.md` fuente se regenera desde las mismas constantes del script, de modo que no pueden derivar. En `anti-ia` modo revisar, con la familia del modelo autor cargada, el barrido salió limpio en los dos documentos; **el chequeo de voz, que es un paso aparte, sí encontró una desviación**: paréntesis a 1,9 por mil contra la banda de 3,3 a 4,0 de sus propios transmittals, corregida reponiendo cuatro códigos ya verificados entre paréntesis hasta 3,8.

**Verificación.** El modelo se revisó con el puente de automatización Navisworks, adaptado a la versión 2027 porque la instalación 2026 ya no expone sus bibliotecas; el Structural Design Criteria llegó con diez de sus once páginas escaneadas y se resolvió por reconocimiento óptico más render a 300 dpi, confirmando toda cifra sobre el render. Las seis anotaciones se cerraron por render PNG, obligatorio en las láminas con rotación 270 donde el conteo de anotaciones devuelve cero aunque el cuadro sea visible. Cero símbolo de sección, cero fuga interna, y PDF de nueve páginas exportado desde Word real con el índice resuelto.

**Enviado a las 18:08 de Chile**, con el transmittal en PDF de nueve páginas como único adjunto y los cuatro `CC_ADASA` por el enlace de descarga, verificado carácter a carácter sobre el respaldo (`envio transmittal 36.pdf`). El usuario ajustó la distribución al enviar: los tres de ADASA suben de copia a destinatario junto con Fitri Indriyani, sale Allan Valentos y entran seis nombres nuevos de BW Water en copia; el cuerpo salió idéntico al borrador salvo el cierre de cortesía, que quitó. `update_register_n36.py` ya corrió y dejó el tally en **62 / 21 / 6 / 0** con 36 transmittals y 85 entregas, coincidiendo con lo esperado, y el gate `openpyxl_lint.py` en exit 0. **Único pendiente del ciclo:** decidir si sale el correo contractual del cronograma, que sigue en borrador porque el tema pasó a la reunión semanal.

### 2026-08-21 — El circuito CIP se está ensayando como sistema de baja presión: tres líneas a 7,5 barG y dos informes de tercero que las dieron por conformes — ENVIADO

**El hallazgo, que solo aparece al cruzar los dos informes de Bureau Veritas.** 🔴 **Tres de las cuatro líneas CIP de super dúplex se ensayaron a 7,5 barG en dos jornadas consecutivas, y los tres registros declaran 5,0 barG de presión de diseño.** La Line List `P22-LI-09-009-003` Rev 0 clasifica las cuatro como super dúplex SCH80S y les asigna 80 a 90 barG de diseño y 120 a 135 barG de hidrostática. No le da 5,0 barG a ninguna. Dejó de ser un incidente: es un criterio aplicado al circuito completo.

| Línea | Servicio | Jornada | Informe | Diseño real | Hidrostática real | Aplicado |
|---|---|---|---|---|---|---|
| `CP-SSD-DN100-09-014` | CIP Feed to 1st Stage RO | 20-Ago | BVM-IR005 | 80 | **120** | 7,5 |
| `CP-SSD-DN80-09-015` | CIP Feed to 2nd Stage RO | 21-Ago | BVM-IR006 | 90 | **135** | 7,5 |
| `CP-SSD-DN80-09-044` | 1st Stage CIP Reject Out | 21-Ago | BVM-IR006 | 80 | **120** | 7,5 |
| `CP-SSD-DN65-09-045` | 2nd Stage CIP Reject Out | 🔴 **pendiente** | — | 90 | **135** | — |

**El Spool 1 del 20 de agosto quedó identificado, y lo identificó el tercero inspector.** El formulario del proveedor lo registró como `DA-SSD-DN100-09-014`, TAG que no existe en la Line List; el `BVM-IR005` lo escribe como **`CP-SSD-DN100-09-014`**, que sí existe. La petición del correo del 20 de agosto queda respondida y se reemplaza por la repetición del ensayo a 120 barG.

**El 21-Ago ocurrió bajo retención escrita.** ADASA la comunicó el 20-Ago a las 23:01 de Penang. A las 09:13 del 21 Adnin respondió pidiendo a su equipo que explicara el ensayo a 7,5 bar, con la justificación *"This spool that has two flange class, 900# and 150#"* y el anuncio *"We also have the same spool that will be test today"*. Y lo ensayó. **Esa justificación es el quiebre de especificación no declarado del Transmittal N30**, levantado sobre `CP-SSD-DN80-09-044` y `CP-SSD-DN65-09-045` por TAG y todavía abierto en `PRG-22`: con tres líneas CIP ensayadas a presión de PVC dejó de ser un comentario de plano, y por eso se le fijó fecha al lunes 24-Ago.

🔴 **Los dos informes de Bureau Veritas declaran conforme un ensayo que no califica, y el del 20 de agosto sin comentario alguno.** El `BVM-IR005` marca **`Satisfactory (Without comments)`**, con No Conformidades y punch list en **No** y un resumen de una línea; la salvedad de *line list* aparece solo en el `BVM-IR006` del día siguiente. **Ni la Line List ni el P&ID figuran en la sección B de ninguno de los dos**, pese a que la Guía del Paquete `ADASA-BV-PAQUETE-INSPECCION` Rev 1 del 21-Jul entregó los dos con asignación expresa a la hidrostática: el P&ID `P22-DWG-09-009-002` Rev D como *"trazado maestro — soldadura, hidrostática, montaje"* y la Line List para las *"visitas 2-3"*. **Y el inspector corrigió el prefijo del TAG**: tuvo `CP-SSD-DN100-09-014` delante y aun así consignó 5,0 barG sobre una línea que esa lista fija en 80.

**No es falta de instrumentación.** La sección D del `BVM-IR005` lista cuatro manómetros el 20 de agosto, **dos de ellos de 0 a 160 bar**, usados esa misma mañana para el ensayo a 90 barG, y el punto 6 de su sección E1 declara que el inspector revisó los certificados. El 21 solo se llevaron los de 0 a 16 bar: la jornada se planificó de entrada como ensayo de baja presión.

**Y el registro fotográfico no permite verificar qué se ensayó.** Ninguna imagen de la sección I de los dos informes muestra una marca de identificación del carrete; la del `IR006` rotula **una sola fotografía con dos números de línea distintos**. Verificado por render.

**Dos réplicas ENVIADAS el 21-Ago a las 12:15 de Chile** (`CORREOS/Agosto 2026/2026-08-21/`), en cadenas separadas, las dos con plazo al **lunes 24-Ago**, y con el respaldo del enviado archivado en la carpeta:

- **A BW Water** (`2026-08-21_Pressure-Tests-21-Aug.docx`, 455 palabras), **enviado 12:15:38**, por el hilo del Request 003/004. **To: Magdier Arias, Eduardo Yamauchi y Stephane Gehant**; Adnin y Fadhil bajan a copia, junto con Ahmad Iqbal, Dalejan Simoy y Libert Lomuntad —los que Adnin había sumado el 20-Ago— y los tres de Bureau Veritas Malasia. Cuerpo enviado íntegro. Abre con el encuadre del circuito CIP. Ocho peticiones encabezadas por la **retención explícita de `CP-SSD-DN65-09-045`**, más dos nuevas: declarar por escrito **qué presión de diseño usa el taller para el CIP y de qué documento la toma**, y explicar la elección de manómetros teniendo los de alta en la mesa.
- **A Bureau Veritas Chile** (`2026-08-21_BV-Informe-IR006.docx`, 529 palabras, **en español y sin nombrar al fabricante**), **enviado 12:15:49** a **Carlo Montecinos con solo Víctor Gutiérrez en copia**: el equipo de Malasia quedó fuera y el reclamo va a la contraparte de la Orden de Compra 836492. Subido de tono. El eje ya no es el dato mal transcrito sino **qué contrató ADASA al designar un tercero inspector**: la Nota Técnica `P22-NT-09-000-002-0` lo designa **representante de ADASA** y la oferta `600049` Rev.3 lo obliga en su sección 1 a velar por los intereses del cliente revisando planos y procedimientos. Sobre la identidad de lo ensayado, con el módulo a 17.000 km, **el inspector presente es el único control de ADASA**. Pide reemitir **los dos informes**, una No Conformidad que cubra los tres ensayos, y dos cambios de método: contrastar contra el P&ID y la Line List antes de firmar, y fotografiar la marca de identificación del carrete. **Reserva de posición** y **cierre en el trabajo conjunto**, sin objetar el desempeño en terreno.

> ⚠️ **Corrección de una versión previa de este mismo día.** El primer borrador del correo a Bureau Veritas afirmaba que el informe del 20 de agosto no había llegado. **Es falso.** El `BVM-IR005-20082026` lo remitió Emylia Rosli el **20-Ago 23:35 hora de Chile**, con Luis Rivera en copia, por la cadena `RE: 25007 TALTAL - Request to witness inspection 004` — una tercera cadena del frente, y de ahí salió el error. Llegó **dentro del plazo** de la sección 3 de la oferta. El reclamo se retiró antes de emitir y se sustituyó por el acuse expreso, lo que además acota el reclamo a su contenido, que es donde no tiene defensa. Lección: **una ausencia no se afirma sin barrer todas las cadenas de correo del frente.**

**Dos ediciones del usuario al emitir el correo a Bureau Veritas**, verificadas contra el respaldo y ya incorporadas al generador: se quitó *"sobre la identidad de lo que se ensaya"* del segundo párrafo, y *"En ADASA mantenemos el paquete al día y respondemos"* pasó a *"Estamos disponibles para responder"*. El correo a BW Water salió sin cambios.

**Registro de compromisos:** `PRG-34` venció incumplido y quedó reprogramado al lunes 24-Ago; `PRG-36` (CRÍTICA) amplía su alcance a la declaración escrita de la presión de diseño del circuito CIP; `BV-24` (CRÍTICA) pasa a cubrir los dos informes y los dos cambios de método; y **`PRG-22` recibe fecha comprometida** al lunes 24-Ago. Los cuatro corren desde el envío de hoy.

**Análisis internos:** `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 05/_ANALISIS_INSPECCION_05.md` y `.../INSPECTION 06/_ANALISIS_INSPECCION_06.md`.

### 2026-08-20 — Entrega 81 revisada, Transmittal N35 emitido y ensayo hidrostático objetado — ENVIADO

> **La entrega 81 llegó el jueves 20-Ago con cinco procedimientos del paquete de calidad y fabricación, todos re-emisiones que responden al TM N32.** El submittal `25007-0081` pide devolución al **domingo 23-Ago**; el plazo de la Cláusula 37.2 vence el **lunes 31-Ago**, y es la tercera submittal consecutiva con fecha de devolución por debajo del plazo contractual. Todo en `REVISIONES/TRANSMITTALES/P22-TM-09-000-035-0/`, con el libro mayor de comentarios y lo verificado que no se emite en `ENTREGAS_BWWATER/ENTREGA 81/`.

> **El criterio de revisión lo fijó el usuario antes de empezar:** los documentos que llegan por sobre la revisión 0 ya están emitidos para construcción, de modo que la revisión verifica **solo** si los comentarios de los transmittals anteriores cerraron, sin observaciones nuevas. El mismo alcance se extendió a los tres procedimientos que llegan en Rev B. El universo de los cinco es el TM N32 y nada más.

> **Veredicto global 3 — To be revised: 2 Código 1 y 3 Código 3.** Tres PDF anotados.

> 🔴 **El determinante: los tres procedimientos de ensayos no destructivos vuelven sin hoja de comentarios y sin fijar el criterio de aceptación.** Como ninguno declara cómo respondió, el cierre se verificó comparando el texto de la Rev A contra la Rev B. El de **penetrantes** cambió **once líneas**: agregó ASME B31.3 a la cláusula 13.0 pero dejó el Apéndice 6 al lado, y el formulario que el examinador firma sigue intacto declarando el Apéndice 8. Se reconoce por escrito que los umbrales de los dos criterios coinciden dígito a dígito, de modo que ningún resultado de examen cambia; lo que cambia es el código que citará el registro que entra al dossier. El de **radiografía** cambió **dos cosas**: incorporó la Tabla 341.3.2-1 de B31.3-2024 completa —verificada por render a 200 dpi, porque entra como imagen y no aparece en la extracción de texto— y agregó un paréntesis. Su cláusula 12.1 sigue **intacta** en 1,8 mm, que es la dispensa de la Sección I para cañería de potencia con sello PP, tres veces y media el límite que T-274 exige para la pared de 6,02 a 8,56 mm que se radiografía aquí. El de **ultrasonido** es el que más trabajó, con nueve cambios, y **cerró su hoja de técnica**: alcance, bloque de calibración y Apéndice 1 declaran ahora UNS S32750 donde la Rev A estaba escrita para acero al carbono. Su cláusula 9.0 pasó de *"a discreción del cliente"* a SA-790, que es la especificación de **material** del tubo y no un criterio de espesor.

> **Los dos que llegan por sobre la Rev 0 son Código 1.** El *HP and LP Pressure Test Procedure* Rev 1 incorporó el formulario **`AQ-QAM-F018` Rev 4** que estaba en la Rev C y desapareció en la Rev D, y el ensayo del mismo día lo confirma en uso. El *Painting Procedure* Rev 1 corrigió la fila `Colour` del formulario a **`RAL 5012 Luminous Blue`**, que era su única condición vinculante. **Decisión de criterio del usuario:** el de presión quedó en Código 1 contra una propuesta inicial de Código 3, porque el formulario se incorporó —que era la parte urgente— y lo que falta, el registro gráfico presión contra tiempo, vive en **otro** formulario; un pendiente que no es intrínseco al documento revisado se sigue en la Sección 3 sin degradarlo. Sobre un documento emitido para construcción el Código 2 no tiene mecanismo: es 1 o es 3.

> 🔴 **El ensayo hidrostático del 20-Ago, por la otra cadena.** El informe recibido ese día trae dos ensayos firmados y timbrados por el inspector. El **Spool 2**, `DA-SSD-DN100-09-003`, se ensayó a **90 barG**, exactamente lo que la Line List Rev 0 le asigna, escalonado 45, 67,5 y 90, retención de treinta minutos y caída nula: conforme. El **Spool 1** se registra como `DA-SSD-DN100-09-014` y se ensayó a **7,5 barG**, con dos manómetros de rango **0 a 16 bar** que físicamente no llegan a 120. Las once líneas de super dúplex del proyecto se ensayan entre 75 y 135 barG y **ninguna a 7,5**, que es la presión de las líneas de PVC; y ese TAG **no existe** en la Line List, cuyo correlativo 09-014 es `CP-SSD-DN100-09-014`, con hidrostática de **120 barG**. La jornada se rotula *HP piping pressure test* y se acepta. **Se pregunta antes de imputar:** el hecho de la presión está verificado, la identidad de la línea no. Correo en `CORREOS/Agosto 2026/2026-08-20/`, **cadena de inspecciones, separada de la del transmittal por decisión del usuario**, con respuesta pedida al viernes 21-Ago para que una eventual repetición alcance la ventana abierta en Penang.

> **Lo favorable del mismo informe, que también queda registrado:** el inspector **asistió y firmó** los dos ensayos y el Inspection Request, primera jornada de la serie con constancia completa de asistencia, lo que cierra por los hechos el reclamo del 17-Ago; los cuatro manómetros están calibrados por Trescal, laboratorio acreditado SAMM, vigentes al 14-Jun-2027; y el **registro gráfico presión contra tiempo sí se produce**, en un `PRESSURE TEST RECORD CHART` con escalones, horas y firmas. Eso **precisa** el pendiente del procedimiento de presión: lo que falta no es la práctica sino el control documental de ese formulario, que no tiene número ni revisión.

> 🔴 **La duda del usuario sobre los 90 barG destapó el hallazgo mayor del día.** Preguntó si aceptar 90 barG contradecía el criterio aprobado, que él recordaba como 1,25 o 1,5 veces la presión de operación. La verificación deja tres cosas asentadas. **El factor es 1,5 sobre la presión de DISEÑO**, lo fija la fila 5.2 del PIE Base de ADASA (*"Presión Prueba = 1.5 x P.diseño"*) y concuerda con ASME B31.3 párrafo 345.4.2; **el 1,25 no existe en el contrato**, su única aparición en todo el árbol es un paso de rosca M8×1,25. **Los 90 barG son correctos**: la línea tiene diseño 60 barG y 60 × 1,5 = 90, que además es el valor más alto de las cuatro combinaciones posibles del criterio, de modo que bajo ninguna lectura se ensayó por debajo. Y **los 135 barG del ITP son ese mismo factor sobre el diseño más alto del circuito**, 90 barG, que corresponde a cuatro líneas, no a las once.

> 🔴 **El hueco que eso reveló, y que es lo grave.** La cláusula 5.5.12 del procedimiento dice en una sola frase que la cañería de alta se ensaya a 135 bar y la de baja a 7,5, y que la presión se toma de la Line List, que prescribe seis valores. **El factor 1,5 no está escrito en ninguna parte del procedimiento**: estaba en la Rev C, se perdió en la Rev D, y el TM N32 decidió no reclamarlo porque el N29 ya había aprobado esa revisión. El 20-Ago el taller aplicó la rama de baja del binomio a un spool de super dúplex. **El riesgo inverso es peor:** aplicar 135 barG a toda línea de super dúplex sometería siete de las once a sobrepresión, hasta 2,7 veces el diseño en las dos salidas de turbocharger. **El transmittal declara la regla, con tabla por TAG y retención de ensayos**; el procedimiento se mantiene en **Código 1** por decisión del usuario, porque remite a la Line List aprobada y lo que faltaba era que ADASA declarara cuál gobierna.

> **Dos correos, dos cadenas, con respaldo archivado.** El de la hidrostática salió a las **11:00** por el hilo del Request **003/004** (`PRUEBAS DE PRESION.pdf`, 8 páginas, 518 palabras y la tabla de las once líneas); el del transmittal a las **11:16** por el hilo de los submittals (`TRANSMITTAL 35.pdf`, 2 páginas, 212 palabras, con el transmittal en PDF como único adjunto y los tres `CC_ADASA` por el enlace). Los dos con `anti-ia` en **VERDE**, y las dos tablas comparadas fila a fila por script antes de emitir. **Al enviar, el usuario ajustó ambas listas de distribución**: en el de la hidrostática los cuatro de Bureau Veritas subieron a destinatario principal y el asunto quedó sobre la cadena 003/004, lo que reengancha las hidrostáticas de baja presión y del RO Vessel que el Request 003 recortó (`PRG-13`); en el del transmittal la copia de BW Water se amplió de cuatro a nueve.

> **Carpeta publicada y paquete cerrado.** El enlace de descarga quedó pegado en el script del transmittal y en el del correo, y se verificó **sobre los `.docx` emitidos**, no sobre los scripts: texto visible correcto en ambos, destino del hipervínculo coincidente carácter a carácter en el transmittal, y cero placeholder residual. El PDF salió de **Word real** (`exportar_pdf_word.py`, COM con late binding): **10 páginas y tabla de contenido resuelta con números de página**, sin el placeholder de campo sin actualizar que deja LibreOffice.

> **Cerrado el ciclo administrativo.** `update_register_n35.py` corrido: **60 Código 1 / 22 Código 2 / 7 Código 3 y cero documentos sin código**, 113 ítems / 89 entregados, 35 transmittals / 81 entregas. Los dos procedimientos que el TM N32 había devuelto sin código suben a Código 1 al cerrar sus condiciones. Registro de compromisos regenerado: **`PRG-27` cerrado** el 20-Ago, **`PRG-25` reprogramado** a la Rev C porque la Rev B no cerró el criterio, y **`PRG-34` (CRÍTICA, vence el 21-Ago) y `PRG-35` abiertos**. Corte: 72 vivos, 23 vencidos, 6 vencen esta semana. Gate `openpyxl_lint.py` en exit 0. Respaldos archivados, con lo que queda registrada la hora de cada envío.

### 2026-08-18 — Entregas 73, 77 y 80 revisadas y Transmittal N34 emitido — ENVIADO

> **Las dos submittals que el N33 dio por inexistentes sí existen, y una de ellas llevaba siete días sin responder.** La **E73** (`25007-0073`, 11-Ago) trae la *Alarm and Interlock List* Rev 0 y el *Control and Sequence Chart* Rev 0, con el plazo de la Cláusula 37.2 venciendo el miércoles 20. La **E77** (`25007-0077`) trae el *Quality Dossier Index* Rev B, emitido el 14-Ago con devolución pedida al 17 y **recibido el 18 a las 07:49**, un día después de esa fecha. La **E80** (`25007-0080`, 18-Ago) trae el *GA of Antiscalant Dosing Pump Skid* Rev C y el *GA of CIP/Flushing Tank* Rev B. Cinco documentos. Todo en `REVISIONES/TRANSMITTALES/P22-TM-09-000-034-0/`.

> **Veredicto global 3 — To be revised: 2 Código 1, 2 Código 2, 1 Código 3.** El código lo fija **un solo documento**. Tres PDF anotados.

> 🔴 **El determinante: un cierre declarado sin estarlo sobre el capítulo que la ET llama indispensable.** La hoja de comentarios del *Quality Dossier Index* Rev B reporta el Acta de Aprobación FAT incorporada en la Sección C21. C21 se titula *Certificate Release ADASA* y referencia la **fila 8.4** del ITP, que es la liberación para despacho. El Acta de Aprobación FAT es la **fila 7.9**, punto de detención, y la ET `P22-ET-09-000-001-0` Sección 8 dice literal que el protocolo del proveedor y el Acta emitida por ADASA "formarán parte integral e indispensable del dossier final de calidad". No tiene capítulo. A eso se suma que la OBS-01 del N30 volvió cosmética —las dos columnas nuevas existen y están casi vacías, y ninguna línea trae estado de inclusión— y que la NOTE-01 sigue abierta: el ITP nombra dos índices distintos, el preliminar de la fila 7.6 y el final de la 8.3, que es punto de detención para ambas partes, y la Rev B no declara cuál es. **El índice no es el dossier:** el ítem 65 sigue en NOT DELIVERED.

> **ADASA declara el valor vinculante en vez de preguntar.** La *Alarm and Interlock List* Rev 0 declara `VT-09-001` en 0 a 12 mm/s rms con el disparo en 10, y la *Instrument List* Rev E, aprobada en Código 1, sigue en 0 a 8,9. BW Water tomó la ruta de re-rangear que el N28 ofrecía y no reemitió la Instrument List, de modo que la definición aprobada del instrumento satura por debajo del disparo y la parada por vibración de un motor de 93 kW no puede actuar. El transmittal **fija el rango vinculante en 0 a 12 mm/s rms** y exige la reemisión. Compromiso nuevo **`PRG-33`** (ALTA, obligado BW Water), **sin fecha comprometida** porque el transmittal no fijó plazo: hay que fijarlo.

> 🔴 **Una corrección de criterio propia, a instancias del usuario.** La primera versión dispuso la *Alarm and Interlock List* Rev 0 en **Código 3** y era over-reach. Ante un Rev 0 la pregunta no es si hay observaciones sino **si el defecto es intrínseco al documento o vive en otro**: el rango de vibración vive en la Instrument List, y los dos TAG que llegaron sin guion (`VE09-014`, `VE09-016`) son housekeeping documental, que por regla no degrada. Pasó a **Código 1** con el pendiente en la Sección 3 y una línea de housekeeping en el bloque de acción; su `CC_ADASA` quedó como traza interna en `_analisis_no_anotado/`. El mismo error apareció una segunda vez en el plano del estanque CIP, donde se había levantado una NOTE-01 por el contador de páginas de la carátula: **observación nueva, fuera del universo del N26**, y también salió. Segunda vez que el criterio se aplica de más sobre un Rev 0.

> **Lo demás, documento por documento.** *Control and Sequence Chart* Rev 0, **Código 1**: los siete puntos del N28 cerrados, uno de ellos sin que la hoja de comentarios lo reclamara. Se verificó y **no se levantó** que queden dos rampas de 1 Hz/s en la secuencia CIP: pertenecen a las bombas CIP y de enjuague, y la Control Philosophy fija el límite de 0,1 a 0,3 Hz/s solo para la bomba de alta. *GA of Antiscalant Dosing Pump Skid* Rev C, **Código 2**: la mitad de rotulado de la OBS-01 del N26 cerró, la de conciliación no, por segunda vez consecutiva y contra una hoja que declara las fuerzas actualizadas; con los diez pernos de la nota 7.2, Fx y Fy cuadran y **Fz por perno es 0,205 contra 0,102**, el doble, donde en la Rev B la diferencia era de factor diez. La lámina sigue rotulando *BOLTING DETAILS TO BE FINALIZED AND ENDORSED*, que enlaza con `PRG-32`. *GA of CIP/Flushing Tank* Rev B, **Código 2**: el TAG `TK-09-001` cerró, la tabla de boquillas no, y las tres entradas en disputa son idénticas a las de la Rev A sin que ninguno de los dos documentos se reemitiera.

> **Master Register actualizado** con `update_register_n34.py`: cinco re-revisiones, ningún ítem nuevo, **58 Código 1 / 22 Código 2 / 7 Código 3 / 0 Código 4 más dos sin código**; 113 ítems / 89 entregados; **34 transmittals / 80 entregas**. El contador de entregas sube de 78 a 80 al corregir las dos submittals que se daban por ausentes.

> **Se resolvió además el diálogo de permisos de Word que aparecía en cada exportación a PDF.** No era la automatización ni el volumen de red: `exportar_pdf_word_mac.sh` creaba el directorio de paso con `mktemp` y por lo tanto una **ruta nueva cada corrida**, y el sandbox de Word exige autorización explícita para cada ruta ajena. El paso se movió a una ruta estable dentro del contenedor de Word, `~/Library/Containers/com.microsoft.Word/Data/pdf_export`, al que Word entra sin pedir nada. Dos corridas seguidas sin diálogo. La regla quedó en el CLAUDE.md global.

> **Pendiente:** archivar el respaldo del enviado con la hora, que no consta, y abrir el enlace de descarga para confirmar que la carpeta muestra los tres `CC_ADASA`.

### 2026-08-18 — BW Water no tiene quién endose el cálculo sísmico y pide a ADASA que le recomiende uno — ENVIADO

> 🔴 **El endoso profesional del informe de cálculo estructural nunca empezó.** Eduardo Yamauchi reenvió el 17-Ago a las 18:52 de Chile un hilo interno de Stephane Gehant del 16-Ago, con prioridad Alta: *"The Chilean PE Engineer that used to provide us the certified documents is not available… Would you have someone to recommend?"*, precedido de *"Sadeep has not managed to contact yet the Chilean PE we used for Centinela"*. Llegó **seis horas después** del Transmittal N33, cuya Sección 3 seguía listando *"the endorsed structural calculation report"* como pendiente abierto.

> **Lo que revela no es una agenda ocupada, es que no hay endosante.** BW Water lo comprometió por escrito tres veces: la hoja de comentarios del plano `P22-DWG-09-005-015` Rev B del **20-May-2026** (*"Seismic data will be furnished once all the calculations are verified by a Professional Engineer"*), la minuta del **16-Jun** (*"Report to be certified by a PE in Chile"*) y la minuta del **30-Jun**, con la acción tabulada *"Frame Structure | Submit package to Chilean PE | BW Water | 01-Jul-2026"*. ADASA pidió por escrito la fecha de emisión del informe certificado el **17-Jun** (*"Please confirm a specific commited date for issuance of the PE-certified report"*) y nunca la recibió. Han pasado **48 días** desde la acción del 01-Jul y **90** desde la primera declaración.

> **El informe salió igual.** La Rev 0 apta para construcción (`P22-CD-09-005-001`, 23-Jul-2026, 551 páginas) lleva solo iniciales internas en su bloque de revisiones —`AULEM / JFR / NOP / LPL / MA`—, sin firma, timbre ni mención de profesional chileno; verificado por extracción de texto y OCR de sus 101 páginas imagen. Los planos generales `P22-DWG-09-005-010` y `-011`, el primero aprobado en Código 1 el 17-Ago, siguen rotulando *"BOLTING DETAILS TO BE FINALIZED AND ENDORSED"*. Las reacciones de anclaje que alimentaron la fundación de Taltal, ya construida por L&A, provienen de ese cálculo.

> 🔴 **El hallazgo contractual que gobierna el reclamo: el endoso NO es exigencia de la ET, la BAE ni el PIE.** Se verificó los tres. La ET `P22-ET-09-000-001-0` pide la Memoria de Cálculo Sísmico y su aprobación por ADASA (Sección 7), sin nombrar profesional chileno, revisor independiente ni timbre; la BAE no menciona la palabra "sísmico"; el PIE tampoco. La única certificación chilena con Punto de Detención en la ET es la eléctrica, régimen SEC. **El endoso es compromiso unilateral de BW Water y ahí se ancla el reclamo**; fundarlo en la ET lo volvería refutable en una línea.

> **Respuesta ENVIADA el 18-Ago-2026.** `CORREOS/Agosto 2026/2026-08-18/` (`crear_correo_pe_endorsement.py`, inglés, 309 palabras, una página, **solo Word por decisión del usuario**). Reply-To al hilo del propio endoso, cadena separada de los transmittals y del frente Bureau Veritas. To: Yamauchi; CC: Gehant, Irugalbandara, Arsovic y Victor Gutierrez. Cuatro bloques: la cronología en **viñetas con la fecha como lead**, a pedido del usuario; la obligación bajo la **Cláusula 45 de la BAE** (todo certificado necesario para el cumplimiento del Pedido a cargo y expensas del Proveedor, eximiendo al Comprador de responsabilidad); la recomendación de **Thomas Engineers, Tomás Ávila** entregada **como referencia y sin designación**, sin relación contractual ni responsabilidad de ADASA por desempeño, honorarios ni plazo; y el cierre exigido al **viernes 22-Ago**, con declaración escrita antes del cierre del miércoles 19 si no es alcanzable, más la reserva de que todo retrabajo derivado del endoso corre por cuenta y plazo de BW Water. `anti-ia` modo escribir, Checklist B, **VERDE**: cero marcadores críticos, oración máxima de 30 palabras, sigma 7,83, cero em dash. La apertura se reescribió a pedido del usuario: la primera versión anunciaba el correo que se está respondiendo, que es auto-referencia estructural (U-02 variante B); ahora abre respondiendo la pregunta de Yamauchi y entra al hecho.

> **Lo que se dejó fuera a propósito.** Los cuatro defectos del informe Rev 0 que ADASA registró y no emitió (combinaciones 224 y 226 con reacciones idénticas dígito a dígito, pernos de `BOI-09-001/002` ausentes, chequeo de la base del contenedor con reacciones de la Rev A, suelo Tipo E citado de una tabla que clasifica en tipos I a IV). **Decisión del usuario:** el documento está en Código 1 y mencionarlos reabriría una aprobación propia; un revisor independiente los encontrará por su cuenta. También quedan fuera el Plazo de Entrega vencido y la multa de la Cláusula 43.1 letra b), que son otra cadena. Si alguna vez se cursa multa por este eje, la letra aplicable es la **43.1 letra a)**, 0,05% diario por atraso en la ingeniería de la ET Sección 7.

> **Compromiso nuevo `PRG-32`** (CRÍTICA, obligado BW Water, `origen_fecha: COMPROMISO ESCRITO BW`, `fecha_origen: 30-Jun-2026`, vence **22-Ago-2026**, una reprogramación por el incumplimiento del 01-Jul). Registro regenerado: **70 vivos · 24 vencidos (20 BW Water / 3 ADASA / 1 otros) · 4 vencen esta semana**, corte 18-Ago. Gate `openpyxl_lint.py` en exit 0.

> 🔴 **Pendiente que esto destapa:** el Master Deliverable Register sigue mostrando `P22-CD-09-005-001` en **Rev B / Código 2**. El Código 1 del Rev 0 se dispuso por correo el 06-Ago sin asignar código y ningún actualizador posterior a `update_register_n29.py` tocó ese ítem, de modo que el registro y la posición de ADASA no coinciden. 🔴 **Pendiente inmediato:** avisar a Tomás Ávila, cuyo nombre y teléfono ya viajaron a BW Water; y archivar el respaldo del enviado, con el que queda registrada la hora, que no consta.

### 2026-08-17 — Entregas 76, 78 y 79 revisadas y Transmittal N33 emitido — ENVIADO

> **Tres submittals sin responder y un criterio de revisión que los recortó a lo esencial.** La **E76** (`25007-0076`, 13-Ago, dos planos en Rev B), la **E78** (`25007-0078`, Equipment Layout Rev D y Process Flow Diagram Rev 0) y la **E79** (`25007-0079`, Control Philosophy Rev 1). Cinco documentos. **Veredicto global 2 — Approved as noted: 4 Código 1 y 1 Código 2, ningún documento vuelve a revisión.** Un solo PDF anotado, con dos observaciones. Todo en `REVISIONES/TRANSMITTALES/P22-TM-09-000-033-0/`.

> 🔴 **No existe el submittal `25007-0077`.** La serie del proveedor salta del 0076 al 0078, segunda vez tras el 0073 ausente. El transmittal lo pregunta sin imputar.

> **El criterio que gobierna la revisión, fijado por el usuario:** la revisión de un documento que responde a comentarios previos se limita a **si esos comentarios están cerrados**, y no se introducen observaciones nuevas. Dos razones: la ingeniería de obras civiles la ejecuta L&A y lo que sale de los planos de BW Water se ve con ellos, no con el proveedor; y no hay tiempo para más iteraciones. Un documento en Rev 1, que existe porque ADASA observó que un comentario de la Rev 0 no se había levantado bien, no puede llegar con comentarios nuevos.

> **El instrumento que fija el alcance es la columna de comentario del cliente de la hoja consolidada**, que trae el texto literal del pedido original. Leerla cambió tres veredictos y corrigió un error propio: el pliego del plano civil nombra literal *"together with skid frame"*, de modo que el marco del skid **sí** estaba pedido y es cierre pendiente, no agregado de ADASA; y el Grounding Layout Rev F rotula el panel **`LCP`** en su propia lámina, mismo identificador que la fila 14 del Equipment Layout, así que la tercera observación del TM N22 **sí** cerró (el `P22-LCP-01` que se citaba salía del texto de un comentario de ADASA, no del rótulo del plano).

> **Disposición final.** **Civil and Loading Layout Rev B, Código 2**: ninguna de las dos partes de la NOTE-01 del TM N16 cerró, porque el peso del contenedor vacío no se declara (la Nota 2 da 13.300 kg rotulados como contenedor y contenido, y ese número es la suma en seco del contenido **sin** el contenedor; el operativo con contenedor es 30.529,5 kg) y el marco del skid quedó sin fila tras reclasificar las filas 6 y 7 a `RO Pressure Vessels`. **GA of CIP Flushing Skid Pump Rev B, Código 1**: las tres partes de la NOTE-05 del TM N11 cerradas, y el plano entrega más de lo que su respuesta reclama, porque la masa de 180 kg y el centro de gravedad están en las Notas 3 y 8.1. **Equipment Layout Rev D, Código 1**: las tres observaciones del TM N22 cerradas, con el filtro de cartucho vertical **verificado por render a 500 dpi**, punto que estaba abierto desde el N22. **Process Flow Diagram Rev 0, Código 1**: emite lo aprobado en la Rev B con un solo cambio, y ese cambio corrige la presión de la bomba de alta a los 46,9 bar del datasheet Rev D. **Control Philosophy Rev 1, Código 1**: los cuatro puntos del TM N31 cerrados y verificados contra el documento que gobierna en cada caso.

> **Lo que se retiró del transmittal, y a dónde fue.** Veinte observaciones bajaron a dos. A la conversación con **L&A** (compromiso `INT-11`, CRÍTICA): diámetros de anclaje M12 y M10, empotramiento de los plintos 5 y 7, escalón de 22 mm de los plintos centrales, fundación del estanque CIP de 2,20 m construida contra 2,50 m dibujada, y los pedestales de los equipos CIP sobre un bloque plano. Solo al ledger interno: la tabla de pesos duplicada y el peso del panel de control (800 contra 989,2 kg), el TAG del mezclador estático, el peso de operación del estanque CIP, el factor sísmico declarado, la vista de empotramiento y los códigos mal formados de la tabla de referencias.

> **El mapeo de sensores de la bomba de alta sale del transmittal, y esa fue la decisión difícil.** La tabla de instrumentos de la Control Philosophy atribuye a la bomba de alta los dos RTD de la bomba CIP, contra la Instrument List Rev E y contra la hoja de comentarios de la Alarm and Interlock List Rev C, que asignan dos sensores por máquina con proveedores distintos, Fedco y Grundfos. **Pero el punto 1 del TM N31 declaró correcta esa página**, así que objetarla sobre una Rev 1 es comentario nuevo. Queda en el compromiso **`INT-12`**: el vehículo para declarar el mapeo sin abrir un instrumento nuevo es el pedido de reconciliar seis tags que el TM N31 dejó abierto al HMI. Al hacerlo hay que tener presente que es asignación de sensor de protección sobre un motor de 93 kW, con disparos de 140 °C en devanado contra 95 en rodamiento, y que el error de lectura es de ADASA.

> **Master Register actualizado** con `update_register_n33.py`: cinco re-revisiones, ningún ítem nuevo, **56 Código 1 / 24 Código 2 / 7 Código 3 / 0 Código 4 más dos sin código**; 113 ítems / 89 entregados; 33 transmittals / 78 entregas. Se alineó la clave del PFD al código del documento, `P22-DWG-09-009-01`, que es como se identifica desde su Rev A, y se realinearon sus dos filas históricas del Revision History.

> **Compromisos:** se eliminaron los cuatro `PRG` que la primera versión del transmittal había abierto, porque nacieron de observaciones retiradas y ninguno se emitió al proveedor. En su lugar quedan tres internos: `INT-10` la tabla de pesos y plintos de la Sección 6.4 de la BL Montaje, `INT-11` la coordinación con L&A, e `INT-12` el mapeo de sensores. 🔴 **La licitación de montaje sigue abierta con las cifras de la Rev A**: cinco de nueve filas de pesos cambian y ninguno de los cinco datos de plintos sobrevive a la Rev B.

> **Versión ejecutiva y enlace, cerrados el mismo día.** El enlace de descarga quedó puesto en los dos scripts (`https://lrg.synology.me:6501/d/s/19Vh5BdPy7Bawfney5aMrUV8sZlaFy99/...`), verificado sobre el **texto extraído del Word y no sobre el script**, que es donde estaba el modo de falla que costó los envíos del N30, N31 y N32. A pedido del usuario los dos documentos se hicieron más ejecutivos, para acelerar la comunicación: el **transmittal bajó a cinco páginas y 1.138 palabras** (venía de diez, luego siete al comprimir los Status de la Sección 2, y luego seis al **sacar la tabla de contenidos**, que gastaba una página entera para indexar cinco títulos), y el **correo a 199 palabras** con la oración más larga en 32. El veredicto ahora abre en la página 2. La ausencia de índice es desviación puntual de la Sección 3.1 del CLAUDE.md, anotada en el script; **la regla no cambia para los próximos transmittales**. La alerta del `25007-0077` se reforzó con la consecuencia contractual: si ese número se emitió y no llegó, la recepción formal nunca ocurrió y los siete días hábiles de la Cláusula 37.2 no han empezado a correr para él.

> **ENVIADO el lunes 17-Ago-2026, registrado a las 12:17 de Chile** (16:17 en Penang), a Allan Valentos y Eduardo Yamauchi, con el equipo de BW Water y el interno de ADASA en copia. Con esto queda emitido el TM N33, dentro de los dos plazos de la Cláusula 37.2, que vencían el 24 y el 26 de agosto. **Quedan dos verificaciones:** abrir el enlace y confirmar que muestra el `CC_ADASA` del plano civil, porque si la carpeta está vacía BW Water recibió una ruta muerta; y comprobar sobre el respaldo del enviado que el párrafo del enlace y la viñeta del archivo viajaron, que es justo lo que este correo vino a corregir tras el N30, el N31 y el N32. Falta archivar ese respaldo con la hora exacta. Los tres `CC_ADASA` retirados quedan en `_analisis_no_anotado/` como traza interna.

### 2026-08-17 — Tres días de silencio sobre el Request 004: constancia de Cláusula 37 y reserva del Punto de Detención — ENVIADO

> 🔴 **Ninguna de las cinco peticiones del correo del 14-Ago fue respondida.** `PRG-28`, el Inspection Request revisado con plazo de 24 horas, venció el sábado 15. Al preparar la réplica son las **08:34 del lunes 17 en Chile, es decir 12:34 en Penang, con la ventana de 09:00 a 17:00 corriendo y sin aviso de la prueba**: la primera de las dos fechas que ADASA ofreció se consume sin acto. Sigue sin constar qué se ejecutó el jueves 13 ni el viernes 14, ni si el inspector asistió, y los registros del 7-Ago llevan diez días.

> **La escalada estaba escrita de antemano.** El campo `accion_adasa` de `PRG-28`, redactado el 14-Ago, ya la fijaba para este escenario: si el formulario no llega, escalar a Yamauchi y Gehant. La réplica sale con los dos en el **To**, junto al equipo QAQC de Penang y Bureau Veritas, y el equipo interno de ADASA en copia.

> **Tres decisiones del usuario gobiernan el cuerpo.** Primera, **firmeza**: se deja constancia de que el aviso posterior al cierre de la ventana incumple la **Cláusula 37 de la BAE**, y se declara la **reserva de que una prueba de punto Hold ejecutada sin aviso escrito y sin el inspector presente no se acepta como evidencia y hay que repetirla** (fila 5.2 del ITP `P22-BA-09-000-004`; nuevo `PRG-31`). Segunda, **alcance**: todo lo que no se reporte del 13 y del 14 se tiene por no ejecutado y vuelve al Inspection Request, lo que alcanza al ensayo de alta, al examen visual y dimensional de spools que lo sustituyó y a la preparación de pintura (`PRG-29`, que pasa de sin fecha al 17-Ago). Tercera, **fecha**: el ensayo se exige **hoy**, dentro de la ventana abierta en Penang, con Bureau Veritas notificado ahora.

> **La constancia se acota al orden temporal del aviso, no a los treinta días.** El correo del 14-Ago declaró que ADASA aceptó avisos de cuatro y de ocho días para no frenar la fabricación; exigir ahora los treinta se contradiría con eso y sería refutable. Tampoco se abre el eje del plazo de entrega vencido ni la multa de la **Cláusula 43.1 letra b)**: es otra cadena, y el inspector está entre los destinatarios.

> **Réplica ENVIADA el lunes 17-Ago, registrada a las 09:07 de Chile**, desde `CORREOS/Agosto 2026/2026-08-17/` (`crear_correo_bv_inspeccion_004_seguimiento.py`, inglés, 356 palabras, una página, PDF desde Word real). Reply-all al mismo hilo del Request 004. **Salió con la ventana de inspección abierta**, que es lo que sostiene la primera petición: en Penang eran las 13:07 sobre una ventana de 09:00 a 17:00, con cerca de cuatro horas por delante; el límite para que la exigencia del mismo día tuviera sentido eran las 13:00 de Chile. Seis peticiones: el ensayo hoy; si no corre, declaración escrita **antes del cierre de la ventana** con la prueba al 19-Ago a más tardar; Inspection Request revisado que reemplace al 004, con un formulario y un resultado por inspección; los registros firmados del 13 y del 14, hoy; los del 7-Ago; y a Bureau Veritas, la confirmación de asistencia de cada día con su informe por jornada. `anti-ia` modo revisar en **VERDE**, checklist B; se partió una oración de 42 palabras del primer párrafo. **Falta archivar el respaldo del enviado** y verificar sobre él que los tres párrafos del medio viajaron, que son la sustancia.

> **Dos cosas declaradas, no ocultas.** La viñeta del tope del **miércoles 19** es una expansión respecto de lo que pidió el usuario, que fijó "hoy" y nada más; se mantiene porque sin fecha de reemplazo el vacío lo llena por defecto el 20 y 21 que propuso BW Water, y se borra si sobra. Y **exigir el ensayo hoy es difícil de cumplir en la práctica**: con la ventana a mitad de camino y sin inspector movilizado, el resultado esperable es la declaración escrita antes del cierre, que es justamente lo que `PRG-30` persigue; su ausencia sería el segundo aviso posterior al hecho en una semana.

> **Lo que queda fuera de esta réplica y sigue abierto:** las hidrostáticas de **baja presión a 7,5 bar** y del **RO Vessel**, que la NT-002 exigía en la Semana 3 y que el `Inspection Request 003` recortó el 05-Ago. Van tres semanas sin reclamarse y viven en `PRG-13`.

### 2026-08-14 — La inspección 004 no se ejecutó y el aviso llegó con la ventana cerrada — ENVIADO

> 🔴 **El ensayo hidrostático de alta presión no se ejecutó, y ADASA se enteró después.** El correo de Mohd Adnin entró el **viernes 14-Ago a las 05:15 hora de Chile**, que en Penang son las **17:15**: la ventana de 09:00 a 17:00 ya estaba cerrada y la jornada, perdida. Declara que por un desperfecto técnico no pudo correr el ensayo de alta, que esta semana solo hubo preparación de pintura, y que la inspección de ese día se reemplazó por un examen visual y dimensional de spools de cañería. **Un desperfecto ocurre; enterarse una vez cerrada la ventana es lo que ningún desperfecto justifica**, y es donde se apoya el reclamo.

> **El ensayo de alta es Punto de Detención de la fila 5.2 del ITP `P22-BA-09-000-004` Rev 0**, con informe de gráfico presión contra tiempo. El examen visual y dimensional de spools es otra actividad del mismo plan, filas 3.2 y 3.4, decidida sin consulta: no libera el punto. **No consta qué se ejecutó el jueves 13 ni si Bureau Veritas asistió**; las carpetas `INSPECTION 03` e `INSPECTION 04` no tenían ningún registro, así que el correo lo pregunta en vez de suponerlo.

> **El `Inspection Request 004` adjunto no le sirve a ADASA.** Verificado por render a 200 dpi, no por extracción de texto: resultado, comentarios y los **tres bloques de firma vacíos**, sin paquete de prueba, y sin identificar el procedimiento ni su revisión. No registra nada de lo ocurrido. Traslada al **20 y 21 de agosto las mismas dos actividades** que no se ejecutaron, y vuelve a cubrir dos días distintos en una casilla de fecha y un bloque de resultado, que es exactamente lo que ADASA pidió corregir el 12-Ago. El correo de remisión del 13-Ago lo transmite además como *"request to witness inspection 003"* mientras el asunto y el formulario son el **004**, de modo que el inspector firmaría un documento que se identifica con otro número.

> **Correo de reclamo y reprogramación ENVIADO** el 14-Ago, desde `CORREOS/Agosto 2026/2026-08-14/` (`crear_correo_bv_inspeccion_004.py`, inglés, 406 palabras, una página). Reply-all al hilo del Request 004, con el equipo interno de ADASA en copia, que faltó el 12-Ago. **Falta archivar el respaldo del enviado, y con él la hora exacta.** Cinco peticiones con plazo: **formulario revisado en 24 horas** con un formulario por inspección; **ensayo de alta al lunes 17 o martes 18**, no al jueves 20; **tres jornadas la próxima semana**, que es el ritmo acordado con Bureau Veritas; la solicitud emitida **sobre disponibilidad confirmada y no sobre intención**, para no volver a movilizar al inspector a un ensayo que no puede correr; y los registros del 13 y del 14 más los del 7-Ago, que siguen pendientes.

> **Tres cosas que el correo no afirma, a propósito.** No declara qué pasó cada día, porque no hay evidencia. No exige los 30 días de la Cláusula 37, porque pedirlos junto con una reprogramación para el lunes sería contradictorio: se citan para mostrar la flexibilidad ya concedida, con avisos aceptados de cuatro y de ocho días. Y no menciona la tarifa de Bureau Veritas ni el saldo de jornadas contratadas, que es información interna con el inspector entre los destinatarios. Tampoco discute que la pintura sea Spot Witness en la fila 3.5, aunque lo sea: abrirlo debilitaría el día de pintura que ADASA preparó con el criterio de perfil de 50 a 80 micrones.

> **Registro de compromisos actualizado.** `PRG-13` pasa a criticidad **CRÍTICA**, su fecha corre al 20-Ago por el Request 004 escrito y suma su **segunda reprogramación**; el historial queda con las tres fechas (12-13 verbal, 13-14 por Request 003, 20-21 por Request 004). El correo abre cuatro: **`PRG-28`** el Inspection Request revisado, vence el 15-Ago y es CRÍTICA; **`PRG-29`** declarar qué se ejecutó cada día con su registro; **`PRG-30`** notificar toda cancelación o cambio de alcance antes de que abra la ventana, de origen CONTRACTUAL por la Cláusula 37, que es el precedente al que se apunta si vuelve a ocurrir; y **`BV-23`** sobre Bureau Veritas, confirmar la asistencia de cada día y emitir su informe por jornada. Las tres últimas salen **SIN FECHA** porque el correo no les puso vencimiento y en este registro ninguna fecha se infiere. Recuento: 65 vivos, 21 vencidos, 4 vencen esta semana, 28 sin fecha.

> **Los dos PDF del hilo quedaron archivados** en `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/`, con extracción en `md/`. El nombre del correo traía un carácter de área privada (`U+F022`), residuo del "imprimir a PDF" de Outlook, que lo hacía inalcanzable desde el shell aunque `ls` lo mostrara; se retiró.

> **Se corrigió el protocolo de exportación a PDF** (`exportar_pdf_word_mac.sh`). El sandbox de Word 16.112 no escribe bajo `~/Library/CloudStorage/` —`save as` devuelve -1708 siempre, venga el documento de donde venga— y abrir desde ahí dispara el diálogo de acceso de macOS en cada corrida. Tampoco alcanza el `$TMPDIR` del usuario, bajo `/var/folders/`, donde acepta el `open` sin abrir nada. El script ahora copia el `.docx` a un directorio de paso en `/private/tmp`, deja que Word abra y guarde ahí, y el shell mueve el PDF al destino; se agregó espera activa a la apertura en vez del retardo fijo. Alternativa no aplicada, por ser decisión del usuario sobre su equipo: conceder Full Disk Access a Microsoft Word.

### 2026-08-12 — Reposición del paquete de Bureau Veritas y recordatorio de las inspecciones 3 y 4 — ENVIADO

> **El 13 y el 14 de agosto son dos inspecciones distintas**, no una visita de dos días: la **N°3 el jueves 13** con el ensayo de presión de la cañería de alta, y la **N°4 el viernes 14** con la preparación de pintura, las dos de 9:00 a 17:00 en Penang. El `AQ-QAM-F027 Inspection Request (003)` las cubre a las dos en una sola casilla de fecha y una sola de resultado, y no existe un Request 004: el correo pide un formulario y un resultado por inspección, porque con uno solo una firma cubre dos días de alcances distintos.

> 🔴 **El paquete que ADASA publicó a Bureau Veritas el 21 de julio tenía siete documentos en revisión superada, y uno cambiaba un criterio de aceptación.** El formulario del procedimiento de pintura **Rev B**, que es el que tiene el inspector, declara perfil de anclaje `40-75 µm` en la celda de criterio y `50-80` en la fila de aceptación del mismo formulario; la **Rev 0** vigente lee `50-80` en los dos lugares, que es lo que exigen la ET y la Painting Specification Rev C. Con la Rev B el inspector podía aceptar un perfil de 40 micrones el día 14.

> **Reposición ejecutada en `PAQUETE_INSPECCION_BV/`**, sin mover ni renombrar la carpeta, que tiene enlace publicado vivo. Siete archivos reemplazados y los superados a subcarpetas `_superseded/`: procedimiento de pintura Rev B → Rev 0, de presión Rev D → Rev 0, PMI Rev A → Rev 0, Visual Rev A → Rev 0, hidrostático de vessel Rev C → Rev 0, GA del skid Rev A → Rev B y filosofía de control Rev E → Rev 0. Recuento 43 → 50 archivos, ninguno perdido, revisión de cajetín verificada en los siete. Quedan fuera el `Alarm and Interlock List` y el `Control and Sequence Chart`, que llegaron en Rev 0 el 11-Ago y ADASA aún no revisa: reponerlos sería declararlos aprobados.

> **Correo conjunto en borrador** en `CORREOS/Agosto 2026/2026-08-12/`, a Eduardo Yamauchi, Magdier Arias y Carlo Montecinos, con el equipo de taller y el de Bureau Veritas en copia. Recuerda las dos inspecciones por separado, declara qué revisión gobierna cada día, fija el color de terminación en `RAL 5012 Luminous Blue` como valor vinculante, y pide identificar el formulario del ensayo de presión antes del día 13, que la fila 5.2 del ITP exige como gráfico presión-tiempo en Punto de Detención. Adjunta los dos procedimientos del caso y repite el enlace del paquete, porque el envío del 21-Jul fue solo a Bureau Veritas Chile y los que atienden en Penang no estaban entre los destinatarios. Al enviarlo cierra `BV-09`.

### 2026-08-12 — ENTREGA 75 revisada y Transmittal N32 emitido — ENVIADO

> **Submittal `25007-0075`, recibido el miércoles 12-Ago-2026 con siete documentos del paquete de calidad y fabricación.** La entrega mezcla dos naturalezas: cuatro procedimientos vuelven **en Rev 0 con la misma letra de revisión y contenido distinto**, re-fechados 11-08-2026, en respuesta al correo del 06-Ago sobre la ENTREGA 71; y tres procedimientos de ensayos no destructivos llegan por primera vez, en Rev A para aprobación, en respuesta al pedido que el TM N30 hizo sobre el Dossier Index. Veredicto global **3 — To be revised**, con **2 Código 1, 3 Código 3 y dos documentos devueltos sin código**. Todo en `REVISIONES/TRANSMITTALES/P22-TM-09-000-032-0/`, con los tres `CC_ADASA` que se emiten en su `COMENTARIOS/` —los otros tres quedan como traza interna— y el correo de cobertura en `CORREOS/Agosto 2026/2026-08-12/`.

> **Criterio del usuario, fijado en la revisión de códigos:** no se codifica 3 un documento que ADASA ya había dispuesto Código 2 y que el proveedor ya emitió a Rev 0 para construcción, porque contradice la aprobación propia. Los que no cerraron su condición vuelven **sin código de respuesta**, con sus puntos abiertos declarados íntegros en su subsección y sin PDF anotado, que es el mecanismo que el N31 usó con la Plant Control Philosophy. Los tres procedimientos de ensayos no destructivos no están alcanzados: nunca estuvieron en Código 2, son primera emisión, y ahí el Código 3 es el ciclo normal.

> **Los cuatro Rev 0 se juzgaron solo por las peticiones del 06-Ago**, y cada punto abierto se contrastó después con el texto literal de lo que ADASA había pedido y con la respuesta de BW Water en la hoja de comentarios. Dos cierran: el **Visual Procedure** identifica el formulario `AQ-QAM-F020` y lo incorpora, y el **PMI** contestó las dos cosas que se le pidieron —la declaración de aplicabilidad al proyecto está en la cláusula 2.0 del frontispicio y la base de aceptación en la 13.4—, de modo que exigirle además que la cláusula 8.1 deje de citar PTS 15.02.01 era leer más estricto que la instrucción escrita. El **HP y LP de presión** fijó la edición ASME B31.3 2024, que era una de las dos peticiones, y dejó la otra sin respuesta: su cláusula 5.8.1 nombra un `Pressure Test Report` que ningún formulario del procedimiento produce, mientras la fila 5.2 del ITP exige un gráfico presión-tiempo como certificado de un Punto de Detención, con el ensayo el 13 y 14 de agosto.

> 🔴 **El procedimiento de pintura cerró su comentario con el color equivocado.** La celda de color del formulario de inspección quedó en **`RAL 5010 Gentian Blue`** mientras la página 9 del propio procedimiento dice `RAL 5012 Luminous Blue` y la Painting Specification `P22-ET-09-006-002` Rev C, aprobada en Código 1, fija RAL 5012 para el soporte estructural dentro del contenedor. `RAL 5010` no aparece en ninguna fila de esa especificación. Sin código, con la jornada de inspección de preparación de pintura el 13 y 14 de agosto encima. **El espesor nominal por capa, en cambio, se deja pasar**: BW Water contestó que el formulario adjunto es una muestra y que los valores reales se llenan en el informe del día, y esa lectura es razonable frente a una petición que decía "print the nominal values" sin distinguir criterio de registro. El transmittal lo replantea una vez con esa distinción escrita.

> **Los tres procedimientos de ensayos no destructivos comparten el mismo defecto de fondo: el criterio de aceptación no es el de este alcance.** La ET, Sección 8, exige que el plan de END fije los criterios de aceptación **según ASME B31.3**, y el NDE Plan Rev C aprobado concreta el párrafo 341.3.2. Penetrantes remite al Apéndice 6 de la Sección VIII Div. 1, que es el de **partículas magnéticas** y ni siquiera el del método que el documento cubre; radiografía da un menú de cinco códigos sin fijar cuál gobierna; y **ultrasonido no tiene criterio: su cláusula 9.0 lo deja "a discreción del cliente"**.

> **El hallazgo de la radiografía tuvo que reencuadrarse tras la verificación adversarial.** El límite de borrosidad geométrica de 1,8 mm que fija su cláusula 12.1 **no es una fila de la tabla de T-274**: es la dispensa del párrafo **PW-51.1 de ASME Sección I**, que permite usar T-274 como guía y fija un umbral único de rechazo para items con sello **PP** (power piping, cuyo paquete de códigos es B31.1, no B31.3). Este módulo es cañería de proceso B31.3, cuyo párrafo 344.5.1 remite la radiografía íntegra al Artículo 2 de la Sección V, de modo que rige T-274 y para pared bajo 2 pulgadas el límite es 0,020". Las líneas con `10% RT` en la Line List aprobada son DN65, DN80 y DN100, de **6,02 a 8,56 mm** de pared — no el rango 3,7 a 11 mm que sale de la Piping Specification e incluye líneas de PVC sin END.

> **Dos observaciones más que la verificación corrigió antes de emitir:** en ASME VIII Div. 1 el Apéndice 6 es partículas magnéticas y el 8 es líquidos penetrantes, de modo que el formulario del `-014` está bien y el cuerpo es el que cita el apéndice equivocado; y el `Article 9` que los tres frontispicios citan **no es arrastre del PMI**, sino de la sección de referencias del propio NDE Plan Rev C que ADASA aprobó en Código 1, así que se pide por método sin imputar invención.

> **Triaje contra la inspección de Bureau Veritas.** Antes de cerrar el transmittal se revisó, punto por punto, si cada cosa abierta lo estaba porque ADASA no fue clara, porque BW Water se negó, o porque ADASA estaba exigiendo de más. Salieron cuatro exigencias: la acotación del anexo del PMI y su base de aceptación, que ya estaban contestadas; las erratas del procedimiento de presión, que ADASA nunca pidió; y el espesor nominal por capa del formulario de pintura, donde BW Water contestó que el formulario es una muestra y los valores reales van en el informe del día — lectura razonable frente a una petición que no distinguía criterio de registro. Los bloques de acción de los tres procedimientos de ensayos no destructivos se partieron en dos, lo que bloquea al inspector y lo que se corrige en la misma emisión, para que la Rev B salga en días y no en un ciclo completo. El registro del triaje, con la cita literal de cada petición y de cada respuesta, vive en `ENTREGAS_BWWATER/ENTREGA 75/_LEDGER_COMENTARIOS.md`.

> 🔴 **El ensayo de líquidos penetrantes se ejecutó el 7 de agosto, cinco días antes de que su procedimiento se sometiera.** El `Inspection Request 002` lo declara como ítem 2, y el procedimiento llega por primera vez en esta entrega. El TM N30 había advertido que los registros producidos bajo procedimientos no aprobados no son admisibles en el dossier. El transmittal pide declarar qué registros existen y bajo qué criterio se evaluaron.

> **El paquete de Bureau Veritas tenía la revisión superada de los cinco procedimientos de calidad**, más el GA del skid y la filosofía de control. Se detectó al revisar esta entrega y **se repuso el mismo día**: siete archivos reemplazados dentro de `PAQUETE_INSPECCION_BV/`, superados a `_superseded/`, con el correo conjunto de aviso en borrador. El detalle está en la entrada de la reposición, más arriba en esta Bitácora.

> **Observaciones transversales:** las cuatro hojas de comentarios consolidadas vienen fechadas el 5 de agosto y rotulan la revisión anterior, y dos declaran cerrado lo que no lo está; y existen dos documentos físicos distintos identificados los dos como Rev 0 en cada uno de los cuatro procedimientos re-emitidos, lo que obliga a decirle a Bureau Veritas cuál rige para el procedimiento de pintura (`BV-09`, sigue siendo acción de ADASA).

> **Plazo:** el Submittal Form pide respuesta el sábado 15-Ago; la Cláusula 37.2 de la BAE recoge el compromiso de ADASA de comentar dentro de siete días hábiles desde la recepción formal y completa, que cae el **viernes 21-Ago-2026**.

> **Master Register actualizado** con `update_register_n32.py`: 113 items, 89 entregados, **53 Código 1 / 25 Código 2 / 8 Código 3 / 0 Código 4** más tres sin código; 32 transmittals y 75 entregas. Los tres procedimientos de ensayos no destructivos entran como items 115, 116 y 117, que no existían en el registro.

> **Pendiente para emitir:** reemplazar el enlace de descarga en los dos scripts, subir los tres `CC_ADASA` a la carpeta del enlace y generar el PDF abriendo el `.docx` en Word real.


> **Emitido el 12-Ago a las 15:30**, sobre el hilo del propio submittal, con Fitri Indriyani y Eduardo Yamauchi entre los destinatarios directos y las once direcciones de BW Water del hilo en copia. Adjunto el PDF del transmittal, diez páginas, con la tabla de contenidos actualizada desde Word real; los tres `CC_ADASA` por enlace de descarga.

> **El cuerpo salió más corto que el borrador, y en su mayor parte a propósito.** El primer párrafo termina en *"It responds to submittal 25007-0075"*: el usuario quitó al enviar el recuento y el *"Overall verdict: 3 - To be revised"*, porque el veredicto va en el transmittal adjunto y repetirlo en el cuerpo es la duplicación que este correo vino a eliminar. 🔴 **Lo que sí falta y no se quiso quitar es el párrafo del enlace de descarga**, ausente por tercera vez tras el N30 y el N31. Los tres `CC_ADASA` siguen alcanzables por el enlace impreso en la Sección 4 del PDF adjunto. Queda por decidir si se responde el hilo con el enlace en texto plano.
### 2026-08-11 — Submittal 25007-0073 recibido y sin revisar — RECIBIDO

> **Dos documentos de control en Rev 0**, recibidos el lunes 11-Ago-2026 en `ENTREGAS_BWWATER/ENTREGA 73/`: `P22-LI-09-008-015 Alarm & Interlock List` Rev 0 y `P22-LI-09-008-017 Control and Sequence Chart` Rev 0. **No entraron en el TM N31**, que se emitió el día anterior, y quedaron **fuera del alcance del TM N32 por decisión del usuario**, que acotó ese transmittal al submittal 25007-0075. Quedan pendientes de revisión.

> Corrige el registro anterior, que declaraba que el submittal `25007-0073` no existía: existe, y su carpeta es la que lleva ese número. La numeración de carpetas quedó alineada con la de submittals (ENTREGA 73 = 0073, ENTREGA 74 = 0074, ENTREGA 75 = 0075), de modo que el contador de entregas del registro maestro pasa a 75.

> Son la familia de la **Plant Control Philosophy** que el N31 devolvió sin código, así que al revisarlos hay que cruzar el mapeo devanado/rodamiento contra los tres documentos a la vez: es lo que mantiene retenida la firma de protección por RTD del FAT Procedure desde el N27.

### 2026-08-10 — Dos consultas por entregables que no llegan: la jornada del 7-Ago y el paquete semanal — ENVIADO

> **Dos correos separados, los dos enviados**, cada uno con su audiencia, en `CORREOS/Agosto 2026/2026-08-10/`. La separación es deliberada: el paquete de reportería es desempeño de BW Water frente a ADASA y no se expone a Bureau Veritas, que es un tercero contratado por ADASA. **Falta archivar el respaldo de ambos**, y con él la hora exacta de cada uno.

> **Correo conjunto BW Water + Bureau Veritas, sobre el hilo del Request 002** (`crear_correo_inspection_002_records.py`, 160 palabras). Nada ha llegado de la jornada del viernes 7-Ago, que cubría fabricación de spools de cañería súper dúplex, líquidos penetrantes en raíz y peineta de esas soldaduras, fabricación del marco del skid, y revisión de WPS y calificación de soldadores. **Reparte el pedido por dueño:** a BW Water el formulario 002 firmado con su casilla de resultado, los informes de penetrantes y los WPS y calificaciones revisados; a Bureau Veritas el informe de la jornada, en el formato del `BVM-IR001-28072026`. Ancla el plazo en el precedente de los propios destinatarios: la Visita 1 del 28-Jul devolvió informe y anexos al día siguiente. Va a Eduardo Yamauchi con **Magdier Arias, Quality Manager**, más Mohd Adnin y Fadhil Wahid, y las cuatro direcciones de Bureau Veritas del hilo. Se nombra a BW Water porque aplica la excepción de correo conjunto de [[feedback_bv_no_nombrar_bw_water]].

> **Correo a BW Water por el paquete semanal** (`crear_correo_weekly_package.py`, 145 palabras). **Distingue dos documentos que no son lo mismo.** El informe de avance semanal sí ha estado llegando: el último es el de la **semana 31**, que cubre del 27-Jul al 2-Ago y vino en el paquete del 3-Ago; lo que falta es el de esta semana. El **DDSR** es lo que lleva dos paquetes sin aparecer: el más reciente es el del **20-Jul**, y los del 27-Jul y 3-Ago trajeron cada uno su informe de avance pero no el reporte de estado. Explica por qué importa —el N31 emitido hoy lo cita para tres planos con fecha de reemisión vencida— y pregunta por el paquete de esta semana con el informe de la semana 32. El primer borrador mezclaba los dos y daba a entender que no llegaba nada desde hacía dos semanas; reclamar de más sobre algo que sí se entregó habría debilitado el punto cierto.

> Dos precisiones que evitaron reclamos débiles. Los paquetes se archivan los **martes**, así que no se afirma atraso del de esta semana, solo su ausencia. Y el tracker de procura **sí cambia de contenido** cada semana pese a conservar el nombre de archivo, verificado por md5, de modo que no se reclama. **El correo de reportería del 05-Ago nunca se envió** —sigue en borrador—, así que éste es el primer reclamo escrito del tema y no lo invoca; conviene archivar aquel como superado.

### 2026-08-10 — ENTREGAS 72 y 73 revisadas y Transmittal N31 emitido — ENVIADO

> Llegan la **E73** (submittal `25007-0074`, un solo documento: `P22-LI-09-008-016` **HMI Display Screenshot Rev B**) y se recupera la **E72** (submittal `25007-0072`, recibida el 06-Ago y sin veredicto porque entró un día después de que saliera el N30). El **TM N31** cubre las dos, con un alcance que fijaste explícito: **solo los comentarios históricos que no fueron levantados**. Todo lo que las dos entregas trajeron de nuevo quedó registrado en sus `_HALLAZGOS_DETERMINISTAS.md` y no se emite. Veredicto global **2 — Approved as noted**.

> **El HMI cierra el compromiso más antiguo del proyecto y deja seis TAG mal.** La Rev B pasa de 9 a 80 páginas y entrega el conjunto de pantallas completo, de modo que el compromiso abierto desde el TM N4 bajo el código `P22-BREAD-09-008-001` queda cumplido en sustancia. De los siete puntos verificados, cuatro cierran —tendencias, ruta de consignas por faceplate, evidencia ISA-101 y el compromiso mismo— y dos quedan a medias. Faltan **tensión y corriente** en las 80 páginas, cuando la ET Sección 5.4 las pide junto al consumo específico, que sí está. Y hay **seis defectos de TAG** contra los listados aprobados, en cinco de las seis pantallas: la bomba de alta rotulada `BH-09-002`, que es la CIP de 11 kW; `TE-09-002` duplicado perdiendo el devanado `TE-09-001`; `VE-09-003` duplicado; `PIT-09-005` en las dos etapas; `FIT-09-005` en primera etapa y CIP; y `LS-09-001` duplicado e invertido en la vista general. La hoja de comentarios los declara todos resueltos.

> **La Plant Control Philosophy Rev 0 vuelve sin código, por decisión tuya.** Sobre un Rev 0 solo caben Código 1 o Código 3, y devolver a revisión un documento ya emitido para construcción sube el conflicto sin ganar nada — el mismo criterio del correo de la E71. De las cinco condiciones del Código 2 del N28 solo cerró una. El determinante es que **el mapeo devanado/rodamiento se corrigió en la bomba de alta y quedó invertido en la de CIP** (página 55 contra la Instrument List Rev E), con el documento contradiciendo su propia página 36; siguen además las consignas de vibración en 7,1 contra 7,0 y 6,0 de la Alarm and Interlock List, el disparo de devanado de 140 °C sin clase de aislación declarada, y los hijos sin fijar por código y revisión. Es el mismo defecto que el HMI acaba de cometer, y el que mantiene retenida la firma de protección por RTD del FAT desde el N27.

> **Los otros tres cierran.** El **RO Vessel Hydrostatic Test Procedure Rev 0** queda **Código 1**: declaró las presiones vinculantes en la cara y reemplazó los dos certificados no conformes por el 26993, de un manómetro de 0 a 250 bar que da 1,83 veces para el ensayo de 136,5 bar. Se pide aparte, en la Sección 3, la **vigencia de esa calibración**: está fechada el 12-Dic-2025 y el ensayo se ejecutó el 17-Jun-2026, cinco días después del intervalo de seis meses que fija la cláusula 4 del propio procedimiento. El **Tie-In Point Layout Rev B** cierra el Código 3 del N7, el documento con el historial abierto más largo, con las tres vistas de elevación y la columna de cota; queda **Código 2** por la presión de diseño en la alimentación. El **GA of SWRO System Skid Rev B** entrega el cuadro pedido en el N15 y queda **Código 2** porque las tres referencias que agregó para cerrarlo citan documentos que no se pueden identificar.

> **La ENTREGA 71 entra en la Sección 3 sin códigos nuevos**, con una línea por documento y citando el correo del 06-Ago, para que la disposición no viva solo en un correo. El informe de cálculo estructural no aparece: incorporó las dos condiciones suyas.

> **El N31 cierra la orientación del filtro de cartuchos, arrastrada desde el N22.** La línea de pendientes venía diciendo *"Equipment Layout Rev C (Code 3, cartridge filter orientation)"*, copiada del N30, cuando el punto ya estaba resuelto: el **Piping Layout Rev C del submittal `25007-0070` dibuja el filtro vertical**, en la planta de la Lámina 1 y en la Sección 1-1 de la Lámina 2. ADASA lo había verificado en el análisis de la E70 y **no lo emitió** — la nota quedó entre las 48 observaciones descartadas de 62, y la NOTE-02 que sí salió en el PDF anotado del Piping Layout trata del anclaje sísmico. El N31 lo declara cerrado en párrafo propio y deja el Equipment Layout pendiente solo de re-emitirse alineado.

> **El barrido de la Rev D dejó además material de reclamo.** ADASA nunca recibió una Rev D del Equipment Layout, pero **el propio DDSR de BW Water declara su `Curr Rev` en D desde el reporte del 22-Jun** — de ahí la sacaron los TM N28 y N29, que la repitieron sin que fuera una entrega. Lo que ese reporte también muestra es que **el `Sent Date` sigue congelado en el 12-Jun-26**, la fecha de la Rev C, y que **la reemisión prometida se corrió tres veces: 26-Jun, 15-Jul y 29-Jul**. El mismo patrón está en los otros dos planos abiertos: el GA del Estanque de Antiscalante, que ADASA tiene en Rev B, figura con `Curr Rev` C y fecha 30-Jul; y el Instrument Location Layout, que ADASA tiene en Rev C, con `Curr Rev` D y fecha 2-Ago. Las tres vencidas. La Sección 3 del N31 ya no las lista como pendientes sueltos: las reclama contra ese reporte, con la revisión que ADASA tiene y la fecha que el proveedor se puso. Ver [[feedback_carryforward_refleja_estado_acordado]].

> **El mensaje del correo de cobertura es el patrón, no el veredicto:** diez condiciones de aprobaciones de ADASA siguen sin incorporar en **cinco documentos ya emitidos a Rev 0 para construcción** — seis de los cuatro procedimientos de la ENTREGA 71 y cuatro de la Plant Control Philosophy —, y sobre un Rev 0 ya no queda código con que devolverlos, de modo que la corrección solo cabe en la próxima emisión mientras se fabrica e inspecciona contra el documento tal como está. La misma cifra queda declarada en el resumen ejecutivo del transmittal. Al corregirla, corregirla en los dos.

> **Enviado el lunes 10-Ago a las 15:33**, asunto *"ADASA – Taltal Brine Module: Technical Review Transmittal N31 (25007-0072/0074)"*, con Eduardo Yamauchi y Fitri Indriyani entre los destinatarios directos. Respaldo en la carpeta del correo. **El párrafo del enlace de descarga no salió en el cuerpo**, igual que en el N30: los tres anotados quedan alcanzables solo por el enlace impreso en la Sección 4 del PDF adjunto, y falta responder el hilo con el enlace. El Master Register quedó en 51 Código 1, 29 Código 2, 5 Código 3, cero Código 4 y un entregado sin código, con 31 transmittals y 73 entregas.

> Paquete en `REVISIONES/TRANSMITTALES/P22-TM-09-000-031-0/`, con tres `CC_ADASA` verificados por render. Los del HMI van agrupados en el frontispicio, como en la Rev A del N22, porque las capturas ocupan el ancho útil completo y las cajas tapaban justo los TAG señalados. Correo de cobertura de una página en `CORREOS/Agosto 2026/2026-08-10/`. **Antes de emitir** falta reemplazar el enlace Synology en los dos scripts, generar el PDF desde Word real y correr `update_register_n31_e72_e73.py`, que está escrito y no ejecutado. Verificación punto por punto en los `_LEDGER_COMENTARIOS.md` de las entregas 72 y 73.

### 2026-08-06 — El correo entrante deja de estar disperso: convención, scripts y skill — GENERADO

> El proyecto tenía 99 scripts para **escribir** correo y ninguno para leerlo. La sección 3.4 del CLAUDE.md regulaba el saliente en detalle y no decía una palabra del entrante, y se notaba: una veintena de piezas recibidas infiltradas dentro de `CORREOS/` en tres convenciones distintas, el archivo `Bandeja de entrada_ Luis Rivera Gonzalez - Outlook.pdf` repetido en **seis** carpetas sin decir de quién ni de cuándo, y `ENTREGAS_BWWATER/` **sin un solo correo** pese a ser el frente con más entrante real. Ahora hay domicilio único en `CORREOS/_RECIBIDOS/`, con la convención en su `_LEEME.md` como fuente única, tres scripts idempotentes, la skill global **`correo-taltal`** y la **sección 3.15** nueva del CLAUDE.md.

> **La vía técnica costó encontrarla y quedó documentada.** El conector de Microsoft 365 no sirve: está autenticado con la cuenta de LRG Ingeniería y el tenant de ADASA exige aprobación de administrador para la aplicación de Anthropic. El Outlook nuevo no expone COM ni deja caché local, de modo que el puente clásico tampoco. Queda la sesión de Outlook Web en Chrome, con seis restricciones verificadas que están anotadas en el `references/` de la skill: el extractor de texto plano falla siempre porque la página nunca queda inactiva, el clic sintético no cambia el panel de lectura, y construir una URL de mensaje rompe la sesión. Lo que sí funciona: **un script localiza el correo por su asunto y devuelve coordenadas, el mouse hace clic ahí, y otro script extrae el cuerpo íntegro**. Dos puntos exigen a una persona y no se pueden automatizar: iniciar sesión cuando caduca, y confirmar en Chrome una descarga retenida.

> **El primer barrido encontró algo que ya estaba costando archivos.** Desde el submittal `25007-0072` BW Water dejó de adjuntar los documentos y los publica en una carpeta de su OneDrive. Esa carpeta trae **siete** archivos y el cuerpo del correo declara **cuatro**: faltan de la tabla los **archivos nativos** de dos planos, `P22-DWG-09-005-005_B` (15,04 MB) y `P22-DWG-09-005-008_B` (37,99 MB). Al capturar se comprobó que los cinco PDF ya estaban en `ENTREGAS_BWWATER/ENTREGA 72/` con hash idéntico y **los dos `.dwg` no**: alguien había bajado la entrega siguiendo la tabla del correo y esos 53 MB se quedaron fuera sin que nadie lo notara. Ya están instalados. Regla que queda: **la lista real de la carpeta manda sobre la tabla del correo**, y la diferencia se anota. Ver `feedback_correo_entrante_lista_real_manda`.

> Capturados y registrados **cuatro correos**: el aviso de **De Nora** del 26-May-2026 —que llevaba dos meses y medio sin registrar—, el submittal `25007-0072` con sus siete archivos instalados, el submittal `25007-0071`, y el **`Recall`** que BW Water emitió sobre ese mismo submittal el 05-Ago a las 21:16, el mismo minuto en que lo envió. `PAQUETE_INSPECCION_BV/` intacta, verificada por hash del listado antes y después.

> **El barrido masivo quedó EN HOLD el mismo día, por decisión del usuario.** Se enumeraron con `from:bw-water.com` los **26 correos** del 3 al 6 de agosto en bandeja de entrada, se capturaron los de más peso y se detuvo: la vía por navegador **exige intervención humana constante** y no escala. Tres modos de falla la condenan, los tres documentados en `CORREOS/_RECIBIDOS/_LEEME.md`: la pestaña de Outlook Web se degrada cada quince o veinte operaciones y **los clics dejan de registrarse en silencio** —llegó a devolver tres veces el mismo correo bajo tres objetivos distintos, y solo la comprobación del asunto en el encabezado evitó guardar tres duplicados—; las descargas piden confirmación manual; y la sesión caduca.

> **La vía que lo reabre está identificada y es un interruptor.** El puente COM de Outlook falla con `CO_E_SERVER_EXEC_FAILURE` por una sola causa: `UseNewOutlook = 1` en `HKCU:\Software\Microsoft\Office\16.0\Outlook\Preferences`. Con esa marca, `OUTLOOK.EXE` redirige al Outlook nuevo y Classic nunca arranca — pese a estar instalado, registrado como servidor COM y con la cuenta de ADASA declarada en el perfil `LUIS_WORKSTATION`. **Es un interruptor de usuario, no una política de la empresa.** Volviendo a Outlook Classic, la skill `pst-extractor` hace la extracción entera por script, sin navegador y sin clics. No se cambió la clave: decide qué cliente de correo se usa a diario y esa decisión es del usuario. Ver `feedback_usenewoutlook_rompe_el_puente_com`.

> Pendiente al momento del hold: 22 correos ya identificados uno por uno, el `_CONTACTOS.md` y el modo de barrido de la skill. La captura de **un correo puntual** sigue vigente y probada; lo que está detenido es el barrido de decenas.

### 2026-08-06 — ENTREGA 71 (25007-0071): los cinco documentos a Rev 0 y seis comentarios sin incorporar — ENVIADO

> Llega el submittal `25007-0071` con **cinco documentos, todos en Rev 0 emitidos IFC**: PMI Procedure, Visual Procedure, HP and LP Pressure Test Procedure, Painting Procedure y UHPRO Structural Calculation Report. No son entregables nuevos: son las re-emisiones finales de once ciclos de revisión repartidos en los transmittals N20, N23, N26, N27 y N29. Los cinco venían **de un Código 2**, de modo que el veredicto lo decide una sola pregunta — si se cumplió la condición de esa aprobación. **De las doce condiciones, seis se incorporaron y seis no.** El único documento que levantó todo lo suyo es el informe de cálculo estructural.

> **Lo pendiente, por documento.** El **PMI** declara el 10% sobre el circuito de alta y la testificación de ADASA, pero su sección de aceptación sigue remitiendo aprobación y rechazo a normas de refinería de terceros en vez de la conformidad UNS S32750, y el anexo del subcontratista —que fija 5% por lote para pernería contra el 10% mínimo de la fila 2.4 del ITP— sigue sin acotarse al proyecto. El **Visual** declara la calificación del inspector, pero ya no identifica ningún formulario donde registrar la inspección, y la fila 3.2 del ITP exige un `Visual report` en punto de testificación. La **pintura** unificó el perfil de anclaje en 50-80 µm, pero su formulario sigue sin el RAL 5012 ni el producto por capa. El **ensayo de presión** fijó las ediciones en su sección de referencias, pero las cláusulas 5.5.2 y 5.6.3 siguen exigiendo la última edición, con lo que la edición no queda fijada para los ensayos. El **estructural** incorporó los dos suyos.

> **Correo emitido sin códigos de respuesta**, `CORREOS/Agosto 2026/2026-08-06/2026-08-06_Submittal-25007-0071-Outstanding-Items.docx`. Los códigos son instrumento del transmittal, y devolver a Código 3 cuatro documentos ya aprobados y emitidos para construcción sube el conflicto sin obtener nada: el correo dice, documento por documento, qué cerró y qué falta, todo en registro de petición (`Please review` / `Please clarify`, ocho en total). Se agregan dos confirmaciones con fecha, previas a la jornada del 13 y 14 de agosto: en qué formulario se registrará el ensayo hidrostático —el procedimiento remite a un `Pressure Test Report` que el paquete ya no contiene y el ensayo es punto Hold— y qué revisión del procedimiento de pintura gobierna la inspección de preparación. Nuevo compromiso `PRG-24`.

> **Criterio que gobernó el alcance, y lo que quedó fuera.** Solo se pide lo que era condición del Código 2. Todo lo demás que la revisión encontró se registra pero **no se emite**, porque levantarlo reabriría una aprobación propia: tres regresiones introducidas en la **Rev D** del procedimiento de presión —la cláusula 5.6.5, el formulario `AQ-QAM-F018` y el factor `1.5 x design pressure`, los tres presentes en la Rev C y perdidos en la Rev D que ADASA codificó 2 en el N29—, el modelo de combinaciones de carga del estructural (las combinaciones 224 y 226 dan reacciones idénticas dígito a dígito en los ocho nodos de apoyo pese a que los casos sísmicos básicos en X y Z difieren, de modo que se corrigió el rótulo y no el análisis) y la ausencia de verificación de pernos para los recipientes `BOI-09-001/002`, el ítem de proceso más pesado con 4.160 kg operativos. Detalle en `ENTREGAS_BWWATER/ENTREGA 71/_HALLAZGOS_DETERMINISTAS.md` y libro mayor de los 33 comentarios verificados en `_LEDGER_COMENTARIOS.md`.

> **Desfase del paquete de Bureau Veritas, que es acción ADASA.** El inspector tiene el procedimiento de pintura en **Rev B**, cuya celda de criterio del formulario dice `40-75 µm` mientras la fila de aceptación de esa misma hoja dice `50-80` — puede firmar como conforme un perfil por debajo del mínimo. La Rev 0 lo dejó en `50-80` en los dos lugares. La inspección de preparación de pintura es el **14 de agosto**. En el ensayo de presión ocurre lo contrario: la Rev D del inspector y la Rev 0 comparten todos los defectos, así que reemplazar la copia no aporta. `BV-09` queda anotado y **abierto**: la Rev 0 existe, pero su criterio de cierre exige además entregarla al inspector.

> **Dos correcciones de método propias.** Afirmé que la comment sheet del estructural tenía la columna del cliente vacía y que los TAG de los equipos no aparecían en el informe; las dos eran falsas. El texto está pegado como imágenes rasterizadas y los TAG viven dentro de planos vectorizados, de modo que la extracción devuelve vacío por la forma del PDF y no por ausencia de contenido. **En un documento con páginas vectorizadas o imágenes pegadas, la ausencia solo se afirma tras renderizar.** Es el mismo modo de falla que costó la fecha de inspección el 05-Ago.

### 2026-08-05 — La jornada de inspección se mueve al 13-14 de agosto y pierde alcance — RECIBIDO

> El `AQ-QAM-F027 Inspection Request (003)` llega al repositorio a las 07:59 y **supera a la minuta del 04-Ago**: declara la jornada el **jueves 13 y viernes 14 de agosto**, no el 12 y 13. **Cambian dos cosas, no una.** El alcance queda en *"1-HP piping pressure test / 2- Painting preparation inspection"*: **desaparece la hidrostática de baja presión** que ofrecía la minuta y **no aparece la del RO Vessel**, cuando la NT-002, Sección 3.2, exige las tres — LP a 7,5 bar como Witness, HP a 135 bar como Hold y RO Vessel como Hold. El aviso son **8 días** contra los 30 que pide el cuerpo de la Cláusula 37 para suministro internacional: segunda notificación consecutiva fuera de plazo, después de los 4 días del Request 001. Extraído a `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 02/md/`; `PRG-13` actualizado con la reprogramación y el recorte de alcance.

> **La corrección se propagó tarde y con un costo.** El análisis del 04-Ago había fijado la jornada en el 12 y 13 tomándola de la minuta, y esa fecha llegó al correo del TM N30, emitido ese mismo día a las 14:20. La causa es acotada: el barrido de fechas se hizo sobre archivos `.md` y ese PDF no tenía extracción. **Regla que queda:** en un frente donde las fechas se mueven por formulario, barrer también los PDF sin extraer de las carpetas del frente. Sin corrigendum del transmittal — la petición sustantiva no depende de la fecha. Ver [[project_bureau_veritas_inspection]].

### 2026-08-05 — El cronograma del 04-Ago pasa a vigente y se corrigen cinco semanas de deriva — INTERNO

> Se confirma que el `2026-08-04_TALTAL Water Treatment Plan Project _Progress Update` es el cronograma vigente, y se corrige que **los documentos durables no lo reflejaban**: la sección `Baseline Schedule` de este README y la memoria que gobierna la revisión semanal de procura seguían declarando vigente el `Project Schedule 08-06-26` (Rev A) con **EXW 14-15 Ago**, cinco semanas superado. Una revisión de PO corrida contra esa referencia medía un ítem "en ventana" que en realidad iba cinco semanas atrasado. También llevaban fechas del baseline 05-Mar presentadas como vigentes los hitos `H-06`, `H-07` y `H-08` del registro, tomadas del Milestone Tracker — la misma hoja que el análisis había probado congelada en cuatro versiones.

> **El cronograma del 04-Ago casi no aporta.** Verificado tarea por tarea contra el del 27-Jul: los IDs **414** (FAT 07-18 Sep), **415**, **416** (EXW 19-21 Sep) y **417** (sitio 13-Nov) traen fechas **idénticas**. Lo único que se movió es el pre-ensamble (ID 404), cuyo inicio corrió ocho días con el fin clavado en el 18-Sep — la duración se comprime de 43 a 36 días. **La fecha de embarque se sostiene comprimiendo duraciones, no recuperando trabajo**, y ahora hay dos versiones consecutivas que lo muestran. Además llegó como **impresión colapsada de 4 páginas** (13.195 caracteres) contra las 12 del 27-Jul (51.135), sin las filas de detalle de ingeniería, y **fuera del paquete semanal**.

> **Se retira un argumento de ADASA.** El registro sostenía que *"del 15-Sep al 18-Sep hay 4 días calendario para 7 jornadas contratadas"* de FAT. Esa cifra salía del correo de BW Water del 28-Jul; su cronograma del 04-Ago da **once días**, que sí las acomodan. Reclamar con la cifra de 4 días habría permitido a BW Water responder con su propio cronograma. Lo reclamable es que **dos documentos suyos del mismo paquete declaren fechas distintas**, y que el inspector no se puede agendar sobre una ambigüedad de ocho días. `BV-13` y `H-03` reescritos en ese sentido. Auditoría completa en `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/_ANALISIS_CRONOGRAMA_04AGO_REVISION.md`. Ver [[feedback_procurement_review_pattern]], [[project_registro_compromisos]].

### 2026-08-05 — Reclamo de reportería semanal: DDSR ausente y cronograma colapsado — BORRADOR

> Correo ejecutivo de una página a BW Water por la **cadena de coordinación semanal**, no la de transmittals (`CORREOS/Agosto 2026/2026-08-05/crear_correo_reporting_gap.py`). Dos puntos: el **DDSR falta por segunda semana consecutiva** —no vino el 27-Jul ni el 03-Ago, y el último que ADASA tiene es del 20-Jul— y el **cronograma del 04-Ago llegó colapsado y fuera del paquete**. Se pide reponer ambos en el paquete del lunes 10-Ago; alta de `PRG-23`. No menciona el atraso del Plazo de Entrega ni la exposición a multa: eso vive en la cadena contractual y meterlo aquí le quitaría filo a las dos peticiones. `anti-ia` VERDE.

### 2026-08-05 — ENTREGA 70 (25007-0070) y Transmittal N30 re-escopeado a tres submittals — ENVIADO

> Llega la **E70** con tres documentos: Piping Layout Rev C (`P22-DWG-09-005-004`), 3D Model Rev A (`P22-DWG-09-005-007`, primer envío del modelo federado Navisworks) y Datasheet of Differential Pressure Switch Rev B (`P22-LI-09-008-006`). El **TM N30, que seguía en BORRADOR desde el 23-Jul con solo la E68**, absorbe la E69 y la E70 — mismo precedente del N27, que se re-escopeó de E63 a E63+E64. El **TM N31 deja de existir**. Veredicto global **3 — To be revised**: Datasheet PLC/HMI Rev 0 **Código 1**, Dossier Index Rev A **Código 3**, Piping Layout Rev C **Código 2**, 3D Model Rev A **Código 2**, DP Switch Rev B **Código 1**, y el conjunto de taller devuelto **sin codificar**. Paquete en `REVISIONES/TRANSMITTALES/P22-TM-09-000-030-0/`: transmittal de 9 páginas con TOC resuelto desde Word real, dos `CC_ADASA` anotados (14,3 MB, por enlace de descarga) y correo de cobertura de una página en `CORREOS/Agosto 2026/2026-08-05/`.

> **El Piping Layout Rev C creció de 5 páginas a 22, y las 17 nuevas son planos de taller que nunca se sometieron.** Van bajo numeración BW Water `25007-ME-PI-0901-0006` a `-0016`, sin código ADASA, ausentes del Submittal Form, y la portada del archivo sigue declarando "Page 1 of 4"; diecisiete llevan timbre **FOR CONSTRUCTION** firmado el 23-Jul. No se aprueban ni se rechazan: el transmittal los **devuelve como no recibidos** y exige someterlos como entregable propio, y **no entran al Master Register** hasta entonces. Los dos hallazgos de contención de presión se emiten igual contra ellos, para que al llegar formalmente ya se sepa qué corregir. Que Rev A y Rev B tuvieran 5 páginas y cero planos de taller es lo que descarta que esto sean comentarios reabiertos sobre material ya cerrado.

> **El modelo 3D se revisó contra los listados aprobados, no contra un estándar BIM.** La revisión inicial objetaba ausencia de propiedades de publicación, conjuntos de selección y viewpoints; **la ET no da base para exigir nada de eso** y esas observaciones se retiraron, por la misma regla anti-invención que gobierna el resto del proyecto. En su lugar se leyó la categoría **`AutoCAD` de Plant 3D del propio `.nwd`**, objeto por objeto, con un puente de automatización Navisworks, y se cruzaron los TAG contra la Valve List Rev D, la Instrument List Rev E y la Line List Rev 0 —las tres en Código 1— más la Equipment List Rev B. Leer los TAG desde nombres de capa, como se hizo en el primer pase, había producido dos observaciones falsas: que no existían objetos tipados y que ninguna válvula estaba identificada. El comentario que queda es que el archivo se identifique por su código y revisión (llega titulado `V14 Taltal.nwd`) y la reconciliación de cuatro números de línea y un correlativo reusado.

> De las **62 observaciones** que arrojó la revisión de la E70 se emiten **14**; las 48 descartadas no aparecen en ninguna parte del transmittal ni de los anotados. Master Register a **110 ítems / 86 delivered · 50/29/7/0 · 30 TMs / 70 entregas**, con `update_register_n30_rescope.py`, que **supersede a `update_register_n31.py`** y no debe correrse en cadena con él. Registro de Compromisos: `INT-09` cerrado con el envío, y entran `PRG-20` (Dossier Index Rev B), `PRG-21` (sometimiento formal del conjunto de taller) y `PRG-22` (confirmación escrita sobre las derivaciones ya fabricadas, criticidad CRÍTICA). Ver [[project_e70_piping_layout_revC]], [[reference_navisworks_automation_windows]], [[project_tm30_state]].

> **ENVIADO 05-Ago-2026 14:20** (respaldo `CORREOS/Agosto 2026/2026-08-05/Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf`; cuerpo verbatim del borrador, adjunto confirmado de 217 KB). Cuatro desviaciones respecto del borrador. **La que importa: el párrafo del enlace de descarga no salió**, de modo que BW Water recibió el transmittal pero no la oferta de los dos `CC_ADASA` — el enlace sí viaja impreso y clicable dentro del PDF adjunto, en su Sección 4, así que los anotados son alcanzables; queda pendiente un seguimiento de una línea en la misma cadena. Las otras tres son de forma: el `To` se amplió de solo Eduardo Yamauchi a cinco (Fitri Indriyani y Yamauchi por BW Water; Víctor Gutiérrez, Ronald Pellejero y Jorge Guevara por ADASA), el `CC` a diez de BW Water, y el asunto salió como *"ADASA – Taltal Brine Module: Technical Review Transmittal N30 (25007-0068/0069/0070)"*. **Un dato del cuerpo quedó desactualizado al momento del envío:** dice *"the hydrostatic test of 12 and 13 August"* contra el **13 y 14** del `Inspection Request 003`, que estaba en el repositorio desde las 07:59 de ese mismo día. No se emite corrigendum — la petición sustantiva no depende de la fecha — y la corrección se propagó al resto del proyecto.

### 2026-08-05 — Registro de Compromisos operativo y hallazgo sobre la oferta de Bureau Veritas — INTERNO

> Se monta el **Registro de Compromisos `P22-IT-06-000-006-0`** en `PROGRAMA y CONTRATO/SEGUIMIENTO COMPROMISOS/`: 59 compromisos y 10 hitos derivados de un `compromisos.yaml` que es la fuente única, con generador Python, validación que aborta ante vocabulario fuera de lista o referencia cruzada inexistente, y render de control por Excel COM. Semáforo y días de mora por fórmula viva, nunca por relleno fijo. Corte inicial: **56 vivos, 14 vencidos (12 de BW Water y 2 de ADASA), 7 vencen esta semana**, y **21 de 59 sin fecha comprometida** — más de un tercio de los compromisos del proyecto no tiene vencimiento exigible.

> **Hallazgo al verificar la oferta de inspección:** existe una **Rev 3 de la cotización BV 600049, emitida el 07-Jul-2026**, que el registro del proyecto no tenía. Mismo total (USD 24.425) pero tarifa unitaria de **USD 977 por jornada** en lugar de 1.017: la Rev 2 no cuadraba, porque 1.017 × 25 da 25.425 y el documento declaraba 24.425. La Rev 3 corrige la aritmética al día siguiente. La validez **no es una fecha fija sino 30 días desde la emisión** (Cláusula 11), de modo que vence el **jueves 06-Ago-2026** y, pasado ese día, la propia cláusula obliga a un reajuste o a una nueva propuesta. La Cláusula 12 condiciona el inicio de los trabajos a la aceptación por escrito, Anexo 1 firmado y sellado más orden de compra. **[Corregido el 05-Ago:** esa aceptación sí existe y estaba en el repositorio desde el 15-Jul — la **OC-836492, folio 836492 del 14-Jul-2026**, adjudica la línea `600049 Rev 3` a Bureau Veritas Chile S.A. por USD 24.425 netos, dentro de la ventana de validez, de modo que la Cláusula 11 nunca se gatilló. La afirmación de que no había evidencia salió de buscar solo en archivos `.md` sin extraer el PDF de la orden.**]** Ver [[project_registro_compromisos]], [[project_bureau_veritas_inspection]].

### 2026-08-04 — Carta Solicitud Formal de Aumento de Monto por USD 56.990,50 — ENVIADO

> ADASA emite la Carta Solicitud Formal de Aumento de Monto asociada al Contrato C-4300 por un Valor Neto Total de **USD 56.990,50**. Firman por ADASA Manuel Alexander Cáceres Godoy (Técnico de Contratos) y Guido Néstor Tejeda Salazar (Jefe Unidad Gestión de Proveedores); por BW Water Americas Inc., Fadey Kassim (Representante Legal). La carta declara que la solicitud no implica modificación alguna al plazo contractual vigente. Ruta: `PROGRAMA y CONTRATO/ESTADOS DE PAGO/md/L-12803; C-4300; Carta Formal Solicitud Aumento de Monto_extracted.md`.

> El monto corresponde **exactamente** a la suma de la propuesta de repuestos `25007-PL-0002` rev.0 (USD 51.224,50) y el adicional CIP `25007-PL-0001` rev.3 (USD 5.766,00), verificada al centavo. La carta no declara esa composición ni cita documento de respaldo. Sobre el contrato de USD 613.991,00 el aumento representa **+9,28%** y llevaría el monto a USD 670.981,50. Riesgo registrado: formalizar el monto antes de que ADASA responda el fondo de la reemisión de repuestos consolida once líneas mal correspondidas, cuatro alzas sin justificar y una reducción de alcance de USD 9.560. Análisis en `PROGRAMA y CONTRATO/_ANALISIS_COMERCIAL_04AGO.md`.

### 2026-08-04 — Adicional CIP 25007-PL-0001 re-datado como rev.3 — RECIBIDO

> BW Water emite el `25007-PL-0001` rev.3 por el cambio de layout del área CIP. Alcance idéntico al rev.2 (los mismos seis documentos), precio idéntico (USD 5.766,00) y validez de precio idéntica (viernes 18-Sep-2026). Las únicas diferencias de texto son la fecha de emisión, de March 18th 2026 a August 4th 2026, y el índice de revisión. **Es una re-datación de una propuesta cuya validez de precio había expirado, no una propuesta nueva.**

> Verificación forense de los PDF: el rev.3 conserva la fecha de creación interna del rev.2 (18-Mar-2026 12:57:41), el nombre del archivo Word fuente (`25007-PL-0001_rev.2`) y las ocho imágenes con hash MD5 idéntico. El rev.3 repite además textualmente, cuatro meses y medio después, que el trabajo *"has been developed and needs to be revised"* y que se emitirá *"within two weeks"*. Contrastar contra los Instrument Layout y Grounding Layout ya emitidos antes de aprobar el pago. Ruta: `PROGRAMA y CONTRATO/ADICIONALES DE INGENIERIA/md/25007-PL-0001_rev3_extracted.md`.

### 2026-08-04 — Fedco confirma embarque al 21-Ago y entrega el Manufacturing Schedule R5 — RECIBIDO

> Lester Burton (Fedco) confirmó por escrito: *"no delays or issues have been raised, and we are on track for the previously estimated ship date of 8/21. Motor was delivered to FEDCO today (8/3)."* Eduardo Yamauchi lo reenvió a ADASA a las 08:24 con el Manufacturing Schedule R5 (orden 19554, PO BW-PO-2026M183 R1, series 17538, 17540 y 17542). El cronograma cierra `Production` al 89%, `Manufacturing Complete` el 11-Ago, `Performance Testing` el 18 y 19 de agosto y `Shipment Ready` el **viernes 21-Ago**. No mueve la llegada a Penang del 02-Sep. Archivos en `PROGRAMA y CONTRATO/RESPUESTA DE FEDCO/`.

> El R5 **no responde** el reclamo de causa raíz que ADASA formuló el 29-Jun con plazo al viernes 03-Jul: es un cronograma de fabricación, sin secuencia de eventos ni acciones de recuperación. La mora del reporte formal alcanza 32 días. El propio documento tampoco registra la revisión R5 en su tabla de control, que llega hasta la 04 del 10-Jul, y carece de firma y fecha de aprobación. Contradicción interna adicional: el comentario del Weekly Dashboard del 03-Ago para la bomba HP declara fin de fabricación el **31-Ago** (*"Due to repositioning of terminal box, expected completion date is on 8/31"*), diez días después del 21-Ago que sostienen Fedco y la minuta de BW Water del mismo día.

### 2026-08-04 — Minuta de la weekly call: dos jornadas nuevas y el embarque sin mencionar — RECIBIDO

> BW Water informa: recepción del motor Fedco confirmada y compromiso mantenido al 21-Ago; pruebas de PLC en curso con actualización para el 05-Ago; fabricación de estructura iniciada; spools de super duplex en biselado y esmerilado; skids a pintura externa en Penang la próxima semana. Inspecciones: viernes **07-Ago** confirmada para fabricación de spools, más **dos jornadas nuevas el miércoles 12 y el jueves 13 de agosto** para prueba hidrostática de baja y alta presión y preparación de superficie de la estructura. Procurement: bomba CIP recibida, válvulas al 06-Ago, flushing tank al 26-Ago. Pendientes declarados: packing list de membranas, una Change Order por cambios de ingeniería en el área CIP, y documentación aún sin Código 1 requerida para soportar las inspecciones. Fuente: `MINUTAS DE REUNION/md/MINUTA DE REUNION 04-08-26_extracted.md`.

> **La minuta no menciona la fecha de embarque**, pese a celebrarse al día siguiente del vencimiento del Plazo de Entrega. El objetivo de completar toda la documentación en Código 1 el jueves 30-Jul, comprometido en la reunión del 28-Jul, quedó incumplido. Las jornadas del 13 y 14 de agosto se avisaron con **8 días**, contra los 30 que exige la BAE Cláusula 37 para inspección de terceros en suministros internacionales: es la segunda notificación consecutiva fuera de plazo.

### 2026-08-04 — Revisión de la ENTREGA 69: el índice llega, el dossier no — Código 3 propuesto — INTERNO

> Revisión del `P22-BA-09-000-013` Rev A contra el ITP `P22-BA-09-000-004` Rev 0, el NDE Plan `P22-BA-09-000-005` Rev C y la ET Secciones 7 y 8. Veredicto propuesto **3 — To be revised, reemitir como Rev B**: el índice enumera 27 capítulos **sin un solo código de documento, revisión ni estado de inclusión**, y omite el capítulo completo de preparación para el despacho del propio ITP (preservación, embalaje y marcado, cuyos registros sostienen la liberación de despacho), el Acta de Aprobación FAT que la ET declara parte integral del dossier final, las certificaciones del personal de END, el certificado de calibración del equipo PMI y los certificados de fabricante de los equipos principales. **6 OBS y 4 NOTE** para el PDF anotado. Hallazgo colateral: los capítulos B3, B4 y B6 enumeran procedimientos de UT, PT y RT que nunca se sometieron a aprobación de ADASA pese a que el NDE Plan lo exige; deben aprobarse **antes** de que arranque la soldadura, porque los registros producidos bajo procedimientos no aprobados no son admisibles en el dossier.

> **El índice no es el dossier.** El ítem 65 del Master Register, *Manufacturing and Testing Dossier*, se mantiene en `NOT DELIVERED`: el entregable de la ET Sección 7 sigue pendiente y sostiene los ítems 8.3 y 8.4 del PIE, de los que depende el 40% del pago. Se abre el ítem **113** para el índice como documento propio. El tramo 2 del reclamo del 25-Jul (dossier preliminar completo, viernes 31-Jul) **venció sin evidencia de entrega**. Vencido también del lado de ADASA: la fecha de retorno del submittal (jueves 30-Jul) y la confirmación a Bureau Veritas de las visitas V2 a V6 (viernes 24-Jul). Análisis en `ENTREGAS_BWWATER/ENTREGA 69/_ANALISIS_E69.md`. Ver [[project_e69_dossier_index]].

### 2026-08-04 — Puesta al día del backlog documental: higiene, extracción y cuatro análisis — INTERNO

> El pipeline documental llevaba diez días detenido. Se ejecuta la puesta al día completa: manifiesto de rollback con hash de los 30 archivos entrados desde el 26-Jul; higiene del repositorio (carpeta `SEMANA 27-06-26` renombrada a `SEMANA 27-07-26`, que era su contenido real; ZIP duplicado de la RWI 01 apartado con registro de ambos hash; carpeta `COTIZACION REPUESTOS 2 AÑOS` apartada por ser subconjunto; y **deuda propia saldada** — el Datasheet PLC/HMI del `PAQUETE_INSPECCION_BV` pasa de Rev C a la Rev 0 vigente, con la Rev C a `_superseded`). **29 documentos extraídos a `.md`**, incluidos un informe escaneado sin capa de texto que requirió OCR y la factura firmada que solo existía dentro de un `.msg`.

> Dos scripts de diff nuevos en `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/`: `diff_trackers.py` (cuatro versiones del Procurement tracking, celda a celda, con bloque de slip silencioso) y `diff_fabrication_schedule.py` (hoja `RO system`, con resolución de columnas **por encabezado y no por posición**, porque la versión de julio no tenía la columna `Progress` y comparar por índice producía un diff enteramente falso). Cuatro análisis de frente en `REQUEST WITNESS INSPECTION/_ANALISIS_BV_04AGO.md`, `.../SEMANA 03-08-26/_ANALISIS_PROGRAMA_04AGO.md`, `PROGRAMA y CONTRATO/_ANALISIS_COMERCIAL_04AGO.md` y `ENTREGAS_BWWATER/ENTREGA 69/_ANALISIS_E69.md`. Ver [[feedback_zip_duplicado_payload_no_contenedor]], [[feedback_pdf_escaneado_triaje_texto_cero]], [[feedback_carpeta_semana_mal_rotulada]].

### 2026-08-03 — Vence el Plazo de Entrega contractual sin cumplirse — INTERNO

> El **Plazo de Entrega de la BAE Cláusula 27** —máximo 300 días corridos desde la Notificación de Adjudicación— venció el **lunes 03-Ago-2026**. El cálculo (07-Oct-2025 más 300 días corridos) coincide exactamente con la línea base del hito `Ready to Ship (EXW Penang)` del propio Milestone Tracker de BW Water, que declara "3 Aug 2026". El hito no se cumplió. La multa de la **Cláusula 43.1 letra b)** —0,2% diario del valor neto total del Contrato por día calendario de exceso, con tope acumulado de 15% en la Cláusula 43.4— corre desde el 04-Ago. La Cláusula 27 fija además que el plazo es firme, que no admite modificación salvo aceptación escrita del Comprador mediante revisión del Pedido, y que los retrasos imputables al Proveedor debe recuperarlos a su costa.

> **Fecha de embarque vigente: 19 al 21 de septiembre de 2026**, sostenida por cuatro fuentes del propio proveedor: los cronogramas MS Project del 27-Jul y del 04-Ago (tarea ID 416), las meeting notes del 28-Jul (*"Overall shipment readiness moved to 21-Sep-2026"*) y el Fabrication Schedule del paquete del 03-Ago. El 10-Sep que muestra el Milestone Tracker es una foto congelada del Recovery Schedule del 14-Jul, cargada además en la columna `Actual` de un hito que todavía no ha ocurrido. Desviación contra la referencia declarada fija por ADASA el 14-Jul: 10 a 11 días. Contra la línea base contractual: **47 a 49 días**. Cascada: llegada a sitio del 26-Oct al 13-Nov, Performance Test del 10-15 Dic al 29-Dic o 02-Ene-2027. **Antes de cursar multa hay que leer la Notificación de Adjudicación**: los 300 días se calculan sobre el `Contract Award / NTP` del cronograma del proveedor, y la coincidencia con el Milestone Tracker es indicio fuerte, no prueba. Ver [[project_plazo_entrega_vencido_03ago]].

### 2026-08-03 — Factura 25007-02 por USD 86.982,60 remitida por BW Water — RECIBIDO

> Andrea Frezzi remite la factura `25007-02` correspondiente al E.E.P.P. N° 24786, aprobado el viernes 31-Jul-2026. Monto **USD 86.982,60**, condiciones net 15 días sobre fecha 31-Jul, con vencimiento el **sábado 15-Ago-2026**. Firmada por Eduardo Yamauchi, PMO Leader. Destino de pago: Truist Bank, cuenta 146122299, ABA 263191387, SWIFT BRBTUS33, con cargos bancarios por cuenta del cliente. La factura firmada existía únicamente dentro del `.msg` y se rescató en la extracción. Rutas: `PROGRAMA y CONTRATO/ESTADOS DE PAGO/EDP 2/md/` y `.../msg_extraido/`.

### 2026-08-03 — Paquete semanal incompleto: sin DDSR ni cronograma — RECIBIDO

> El paquete del 03-Ago contiene el Progress Report Week 31, el Procurement tracking y el Fabrication Schedule. **No incluye el Document and Drawing Status Report**, ausente también en el paquete del 27-Jul; la última emisión disponible es la del 20-Jul (73 documentos, 92% de avance de aprobación, 47 aprobados, 16 aprobados con comentarios, 6 en Revise & Resubmit y 3 no entregados). No hay declaración de discontinuación en ninguna minuta y el correo del 28-Jul enumera lo adjunto sin incluirlo: el reporte falta, no fue dado de baja. El cronograma llegó por separado, fechado el 04-Ago, a `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/`.

> **Cinco movimientos de fecha del tracker sin entrada en el Change Log**, que sigue vacío en las cuatro versiones comparadas desde el 13-Jul: CIP / Flushing Tank +30 días, los tres ítems de válvulas +14 días y estructuras +14 días. Cinco movimientos adicionales en el cronograma entre el 27-Jul y el 04-Ago, también sin declarar: fin de `Engineering` y de `Mechanical` +7 días, llegada de válvulas +11 días, membranas RO +3 días, y el `Pre-Assembly` con inicio corrido +8 días y duración comprimida de 43 a 36 días para sostener el 18-Sep. Detalle en `SEMANA 03-08-26/DIFF_TRACKERS.md` y `DIFF_FABRICATION_SCHEDULE.md`.

### 2026-07-31 — E.E.P.P. N° 24786 aprobado por USD 86.982,60, avance acumulado 20,49% — DECIDIDO

> ADASA aprueba el Estado de Pago N° 24786 del período Julio 2026 por **USD 86.982,60** netos, sin retención, anticipo, multas ni reajuste, y solicita la facturación el mismo día a las 10:49 (Manuel Cáceres Godoy). El monto equivale al 15,00% de la partida de Suministro y Diseño del Módulo RO (USD 579.884,00); el acumulado llega a USD 125.834,83, que es 21,70% de esa partida y **20,49% del contrato** de USD 613.991,00, con un saldo por facturar de USD 488.156,17. Las partidas de Repuestos Mandatorios (USD 17.310) y Comisionamiento (USD 16.797) permanecen en 0,00%.

> El soporte documental son las copias sin precio de las órdenes de compra de siete equipos principales: Fedco `BW-PO-2026M183` (bombas de alta presión), TK Water `BW-PO-2026M260` (filtros de cartucho), Protec Arisawa `BW-PO-2026M184` (recipientes a presión), LG NanoH2O `PO-0016155` (membranas), ProMinent `BW-PO-2026M089` y Promatics `BW-PO-2026M074` (dosificación química), Quantic Logic `BW-PO-2026M062` y Dayamas `BW-PO-2026M073` (sistema CIP). La fila del ERD figura sin número de orden ni proveedor. Observaciones de forma: la carta de cobertura de BW Water solicita gestionar el *"Estado de Pago N° 1"* cuando el formulario dice N° 2, y su firma lleva fecha domingo 26-Jul-2026, posterior al documento (jueves 23-Jul-2026). Rutas: `PROGRAMA y CONTRATO/ESTADOS DE PAGO/EDP 2/md/` y `PROGRAMA y CONTRATO/DOCUMENTOS PARA EL ESTADO DE PAGO/ESTADO DE PAGO 2/md/`.

### 2026-07-29 — Request to Witness Inspection 002 para la jornada del 7-Ago — RECIBIDO

> Mohd Adnin emite a las 04:10 la segunda solicitud de inspección a Bureau Veritas con ADASA en copia (`REQUEST WITNESS INSPECTION/RWI 02/`). Jornada del **viernes 07-Ago, 09:00 a 17:00 en Penang**, con cuatro actividades: inspección de fabricación de spools SDSS, PT de raíz y capping de la soldadura SDSS, inspección de fabricación del marco del skid, y revisión de WPS y registros de calificación de soldadores. **Adjunta el ITP Rev 0 y el NDE Plan `P22-BA-09-000-005` Rev C, ambos byte-idénticos a los aprobados y sin anotaciones de ADASA**, lo que cierra el punto 2 del reclamo del 25-Jul: BW Water sí corrigió, y los hash lo prueban. El formulario corrige el campo Client Name a ADASA y declara los planos `P22-DWG-09-005-003` y `P22-DWG-09-005-004`. Aviso de nueve días, sobre los cuatro del Request 001 y por debajo de los 30 de la BAE Cláusula 37.

### 2026-07-28 — Propuesta formal de repuestos 25007-PL-0002 rev.0, tres días antes del deadline — RECIBIDO

> BW Water reemite la cotización de repuestos recomendados a dos años como documento comercial controlado, cumpliendo el deadline del viernes 31-Jul fijado por ADASA en el rechazo por forma del 20-Jul. Total sin cambio: **USD 51.224,50**, 24 líneas, validez hasta el viernes 28-Ago-2026, pago 50% contra orden de compra a NET 30 y 50% contra readiness to ship. Ruta: `PROGRAMA y CONTRATO/REPUESTOS DE 2 AÑOS/propuesta formal/md/`.

> **Los cuatro requisitos se abordaron; ninguno se satisfizo por completo.** El documento incorpora membrete, número de cotización con índice de revisión, referencia al Contrato C-4300, lead time y tránsito por línea, condiciones comerciales y la columna de reconciliación de alcance con el TAG de cada equipo. No lleva firma del representante legal ni del responsable comercial: el único bloque de firma es el del cliente y está en blanco. El Incoterm del cuerpo (EXW Penang) contradice los cinco Incoterms del Anexo A, y los Términos y Condiciones adjuntos citan la edición Incoterms 2000.

> **El fondo quedó intacto:** cero cambios de precio en las 24 líneas y persisten las once observaciones de correspondencia del 15-Jul, incluidas el part number MSD-130 contra la bomba Fedco MSD-7016, el cambio de descripción de Service Kit a Mechanical Seal a precio idéntico (USD 9.560), los sensores pH y ORP Foxboro contra los Rosemount 3900 y 1056 instalados, los manómetros Monel contra los Wika con sello Superduplex 2507, y la ausencia de repuestos para las 64 válvulas de bola DN15. La columna de reconciliación no corrigió esas líneas: las volvió verificables dentro del propio documento. Ver [[project_cotizacion_repuestos_2anos]].

### 2026-07-28 — Visita 1 de Bureau Veritas: PMI de super duplex en Penang — RECIBIDO

> Bureau Veritas ejecuta la primera jornada de vigilancia y emite el informe **BVM-IR001-28072026 Rev 0**, 12 páginas más un Annex A de 17 (`REQUEST WITNESS INSPECTION/RWI 01/ZIP_EXTRAIDO/md/`). Inspector Ismail Bin Kormain, oficina BV Kuala Lumpur, job BVM 26/1366, orden de compra ADASA 836492. Inspección ejecutada **contra el ITP Rev 0** y el procedimiento `P22-BA-09-000-006` Rev A: visual, dimensional y cantidad conformes, y **31 lecturas de PMI** sobre tubería A790 S32750, bridas y codos A182 F53 y fittings A815 WPS32750, todas dentro de banda. Sin no conformidades ni punch list. Tres puntos abiertos: el fabricante no entregó su reporte oficial de PMI, sockolets y half couplings no pudieron verificarse por geometría, y el 10% de weldment que exige la actividad 2.4 del ITP queda pendiente. El Annex A trae el Material Traceability Record QAM-0001, los certificados de molino y el certificado de calibración del analizador LIBS Z902-01702, vigente hasta el 16-Dic-2026: **parte de los registros de la Semana 1 llegaron a ADASA por vía del inspector, no del proveedor**.

> **Corrección de una premisa propia:** el reclamo del 25-Jul exigió las calificaciones de los soldadores "de las juntas ya soldadas desde mediados de julio". El informe del inspector deja el PMI de weldment pendiente **porque no había soldadura ejecutada** al 28-Jul, lo que corrobora la afirmación de BW Water del mismo día. La ventana de fabricación 17-Jul a 10-Ago del status update del 14-Jul era planificación, no avance real. La exigencia de los WPS/PQR se sostiene igual —son prerrequisito, no consecuencia— pero el encuadre "juntas ya soldadas" no se debe repetir.

### 2026-07-28 — Respuesta de BW Water al reclamo del dossier de inspección — RECIBIDO

> Eduardo Yamauchi responde a las 15:31 los cuatro puntos del reclamo del 25-Jul (`PROGRAMA y CONTRATO/HITO BUREAU VERITAS/CORREOS VBV-BW/md/`). **Punto 2 cumplido:** el inspector recibió el paquete Rev 0 antes de la jornada. **Punto 1 incumplido en su tramo del lunes 27-Jul:** BW Water sostiene que la fabricación no ha comenzado, que los planos aprobados se emitieron el viernes 24-Jul y que no existen registros de fabricación; **reencuadra el dossier como "technical submittals"** y lo compromete para el fin de la semana laboral. Confirma por escrito que los reportes y certificados FEDCO se incorporan al dossier final antes del embarque. **Punto 3 movido:** una sola jornada para la Visita 1, de dos a tres días para V2 a V6, y revisión de WPS, PQR y calificación de soldadores el 7-Ago; contrapropone un aviso de **3 a 5 días** frente a los 30 de la BAE Cláusula 37. **Punto 4 respondido a medias:** V5 y V6 el miércoles 9-Sep, FAT comenzando el martes 15-Sep y Release for Dispatch el viernes 18-Sep, sin confirmar el alcance mínimo del FAT ni la reunión de Kick-off.

> Dos cuestiones que conviene resolver antes de responder. El reencuadre se apoya en un *"As clarified this morning"* cuyo intercambio no consta en ninguna fuente, de modo que no se puede verificar si ADASA acotó el alcance o es lectura unilateral del proveedor. Y la aritmética del FAT no cierra: del 15-Sep al 18-Sep hay cuatro días calendario para las **siete jornadas de testificación** contratadas a Bureau Veritas. Ver [[project_bv_v1_penang_28jul]].

### 2026-07-27 — ENTREGA 69 (25007-0069): Fabrication and Testing Dossier Index Rev A — RECIBIDO

> Recibida el lunes 27-Jul-2026 08:17 con un único documento: `P22-BA-09-000-013` Rev A, *Fabrication and Testing Dossier Index*, 2 páginas, emitido IFA con fecha de retorno requerida el jueves 30-Jul-2026. Es la respuesta al primer tramo del reclamo del 25-Jul (índice del dossier más registros de la Semana 1). **Llegó el índice; no llegó ningún registro.** Entregas recibidas E1–E69.

### 2026-07-25 — Reclamo del dossier de fabricación y pruebas para Bureau Veritas — ENVIADO

> **El dossier no llegó en la fecha comprometida (Vie 24-Jul).** Lo que sí ocurrió el 23–24 de julio fue la **Request to Witness Inspection 001** que Mohd Adnin emitió directo a Bureau Veritas Malaysia con ADASA en copia (`PROGRAMA y CONTRATO/HITO BUREAU VERITAS/CORREOS VBV-BW/`, tres correos): una sola jornada, **28-Jul 9:00–17:00, PMI de super duplex**, con **4 días de aviso** contra los 30 de la BAE Cláusula 37. Sus adjuntos son el **ITP en Rev C** (superada; la vigente aprobada Código 1 es la **Rev 0**, TM N26) y el PMI Procedure Rev A, ambos en la copia **con las anotaciones de revisión de ADASA**, no los documentos limpios. Bureau Veritas preguntó por el WQT y WPS/PQR; BW Water lo movió al **7-Ago**, fuera de la Semana 1 de tres jornadas comunicada a BV el 21-Jul.

> **Encuadre del reclamo:** el compromiso del 24-Jul **no consta por escrito de BW Water** (quedó registrado por ADASA en la cobertura del TM N29 del 21-Jul, sin objeción), por lo que el correo se funda en la obligación contractual: el dossier es entregable de la **ET P22-ET-09-000-001-0, Section 7** (90 días desde la adjudicación, con los certificados de fabricación de los aceros super duplex), es el documento que ADASA revisa bajo el **item 7.6 del PIE P22-IT-09-000-001-0**, y figura como **ítem 65 del Master Register = NOT DELIVERED**. Se exige en dos tramos (**Lun 27-Jul** índice del dossier + MTR/trazabilidad de los spools SDX, calibración del equipo PMI con certificados del técnico y WPS/PQR con calificaciones de soldadores de las juntas ya soldadas desde mediados de julio; **Vie 31-Jul** dossier preliminar completo), encadenado a los **items 8.3 y 8.4** (aprobación final del dossier y Release for Dispatch, que soporta el 40%). Sin invocar la BAE Cláusula 43.

> **Artefactos:** `CORREOS/Julio 2026/2026-07-25/` (`crear_correo_dossier_inspeccion.py` → `2026-07-25_BWWater-Inspection-Dossier-Request.docx` + `_Descripcion.md` + respaldo `RV: 25007 TALTAL - Request to witness inspection 001.pdf`). **ENVIADO el sábado 25-Jul-2026 09:03**, como **RV del hilo del Request 001** (no por el thread de designación): To Yamauchi, Gehant, Arias y Lokman Hakim, **sin CC** — el reclamo queda dentro de la conversación que lo originó y fuera del alcance de Bureau Veritas. Cuatro puntos: dossier, revisiones equivocadas en manos del inspector (reemitir las limpias antes del 28-Jul), alcance de la Semana 1 y plazo de notificación, y los puntos de reconciliación sin respuesta (V5/V6, FAT y Dispatch Release, Kick-off) que **impiden a ADASA confirmar V2–V6 a su inspector** — compromiso propio que también venció el 24-Jul. anti-ia **VERDE** (552 palabras, sigma 9,2, cero em-dash en prosa).

> **Seguimiento abierto:** Lun 27-Jul índice del dossier + registros de la Semana 1; antes del 28-Jul reemisión de las revisiones limpias a BV y notificación de las jornadas 2 y 3; Mar 28-Jul (weekly) respuesta escrita a la reconciliación; Vie 31-Jul dossier preliminar completo. **Pendientes de ADASA:** reenviar internamente el correo al equipo (Gutiérrez, Guevara, Pellejero), que no quedó en copia; reemplazar el Datasheet PLC/HMI Rev C por la Rev 0 en el `PAQUETE_INSPECCION_BV`; emitir a Bureau Veritas la confirmación de V2–V6 cuando BW Water reconcilie; y verificar en Outlook la fecha real del correo de reconciliación (el hilo lo muestra el **sábado 18-Jul 13:43**, el registro interno dice 20-Jul). Ver [[project_bureau_veritas_inspection]], [[feedback_reclamo_por_obligacion_no_por_compromiso]].

### 2026-07-23 — Transmittal N30, primer borrador con solo la E68 — SUPERADO

> **TM N30** (`P22-TM-09-000-030-0`, submittal **25007-0068** = E68, recibido el jueves 23-Jul), **1 documento**: el *Datasheet of PLC and HMI Panel Component (Major Component)* **Rev 0 (IFC)**, ítem #29 del registro, cuarto ciclo (A Code 2 → B Code 3 → C Code 2 → **0 Code 1**). Veredicto global **1 — Approved**.

> **Cierres verificados.** Las dos NOTE del N26 quedan cerradas: el código del documento ya lee `P22-ET-09-008-001` en portada y en los 7 encabezados de componente (solo el nombre del archivo entregado conserva el de dos dígitos), y la cantidad de **2 módulos 5069-IY4** está declarada en la lámina **P22-CD-09-004-001-P2** del Control System Architecture Rev D — verificada por render, porque esa lámina es un plano A1 con texto vectorizado sin capa extraíble — que da 8 canales RTD contra los 4 puntos de la IO List Rev 5. El **diff Rev C → Rev 0 no cambia ninguna especificación técnica**: 41 de 50 páginas son bit-idénticas.

> **Declaración vinculante (el punto del transmittal).** El número de catálogo del terminal de operación difiere entre el datasheet (**2711P-T10C22D9P**, desde la Rev A de noviembre) y **cuatro documentos del set de control** que llevan el **2711P-T10C21D8S**: el BOM del Outline Rev 0 IFC (Code 1 en N29), el Schematic Rev A (Code 2 en N20), el FAT Procedure Rev A (Code 2 en N27) y el Control System Architecture Rev B/D (validado en N4, Code 1 en N14). **ADASA declara vinculante el `-D9P`** en vez de preguntar cuál corresponde: es el modelo de la ficha del propio proveedor, el TM N22 lo fijó como base de hardware del diseño de pantallas, y per la ficha técnica del fabricante (Rockwell 2711P-TD008) el campo `21` del `-D8S` designa **un** puerto 10/100Base-T con 512 MB, que no cumple las filas 15 y 18 del datasheet (`2 x Ethernet RJ45`, `1 GB`). La corrección cae en esos cuatro documentos → **Sección 3**, no degrada al revisado. **No se imputa incumplimiento a BW Water**: ADASA codificó documentos de ambos lados durante 4,5 meses. Puerta abierta con carga de prueba: si BW quiere el Standard, debe declararlo por escrito antes de comprar y demostrar el cumplimiento de la ET Section 5.4 (históricos y tendencias) y de las pantallas exigidas en el N22.

> **Seis ítems documentales a la próxima emisión natural** (no degradan, precedente del Outline Rev 0 en el N29): la hoja de comentarios **perdió el registro de cierre de los tres ítems del TM N21** (incluida la disposición HART, que aparecía 15 veces en la Rev C y ahora cero); cita una "Rev D" inexistente; la portada declara 49 páginas contra 50 (regresión, la Rev C decía 50); las 7 hojas mantienen "ISSUED FOR APPROVAL" mientras el Submittal Form somete la revisión como IFC; la hoja de salida analógica lleva el design intent de una salida **digital** y su modelo dice `5069-OF4/ OF8`; los encabezados no llevan índice de revisión.

> **Metodología.** Triaje página por página antes de extraer (ninguna lámina en el datasheet → extracción textual; el Control Architecture Rev D sí es plano → `--mode drawing` + render). **Verificación adversarial con tres agentes** que cambió el entregable: volteó el veredicto de un Code 2 de trabajo a **Code 1** (sobre un documento ya emitido en Rev 0 el Code 2 no tiene mecanismo aplicable — su fórmula ordena corregir *antes* de emitir a Rev 0, y el CLAUDE.md prohíbe el "in Rev X"; precedente N29: los dos primeros Rev 0 del proyecto fueron Code 1), corrigió el conteo de documentos con el `-D8S`, aportó el ancla de las filas 15/18 y detectó tres arrastres de la Sección 3. Todos los hallazgos críticos re-verificados a mano por render y grep antes de incorporarse. anti-ia **VERDE** (checklist B; cero fingerprints críticos, σ=16,9).

> **Correcciones de arrastre.** El **HMI Display Screenshot NO está "sin entregar"** — se entregó Rev A en la E50 y volvió **Code 3 en el TM N22**; los TM N26 a N29 lo arrastraban como *"never submitted"* por una celda obsoleta del registro, **corregida** en `update_register_n30.py`. La GA del Antiscalant Dosing Tank es **Rev B**, no Rev C. Se incorporan a la Sección 3 dos Code 3 que llevaban cuatro transmittals sin aparecer: **Instrument Location Layout Rev C** (N23) y **Tie-In Point Layout Rev A** (N7, el más antiguo vivo).

> **Artefactos:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-030-0/` (`crear_transmittal.py` → `TRANSMITTAL N30 ADASA-BW_WATER.docx` + PDF de 5 páginas desde Word real; `P22-TM-09-000-030-0_TRANSMITTAL.md`; `_ANALISIS_N30.md`; `COMENTARIOS/` = **traza interna, no se emite**, per Code 1 sin CC_ADASA). **Master Register a N30** (`update_register_n30.py`, backup `_pre-N30.xlsx`): **50 C1 / 28 C2 / 6 C3 / 0 C4**, 108 items / 84 delivered, **30 TMs / 68 entregas**. Correo de cobertura `CORREOS/Julio 2026/2026-07-23/crear_correo_tm30.py` (BORRADOR). Nuevo utilitario en la raíz: **`exportar_pdf_word.py`** (Word COM por late binding; la PIA tipada falla en este equipo y dejaba un WINWORD huérfano). **Pendiente pre-envío:** pegar el `DOWNLOAD_LINK` de Synology en transmittal y correo y re-exportar el PDF; y **reemplazar el datasheet Rev C por la Rev 0 en el `PAQUETE_INSPECCION_BV`**, que quedó superado y está en manos de Bureau Veritas desde el 21-Jul (V1 arranca el 27-Jul). Ver [[project_tm30_state]], [[transmittals]].

> **Este borrador quedó superado.** Nunca se envió, y el 05-Ago el N30 absorbió la E69 y la E70. Vale lo sustantivo de arriba —el análisis del datasheet, la declaración vinculante del `-D9P` y las correcciones de arrastre, que sobreviven íntegras como subsección 2.1 del transmittal emitido—, pero no lo operativo: el tally, el conteo del Master Register, el PDF de 5 páginas y la carpeta del correo `CORREOS/Julio 2026/2026-07-23/` (movida a `CORREOS/Agosto 2026/2026-08-05/`). El estado vigente está en la entrada del 05-Ago.

### 2026-07-21 — Correos ENVIADOS: cobertura TM N29 + correo conjunto Bureau Veritas — ENVIADO

> **Ambos correos ENVIADOS el 21-Jul-2026**, con respaldo PDF en `CORREOS/Julio 2026/2026-07-21/`: la cobertura del **TM N29** (`envio transmittal 29.pdf`) y el **correo conjunto BV-BW** (`correo coordinacion bureau veritas-bw waters.pdf`). El correo del TM N29 se reformó a versión **ejecutiva** (veredicto + 4 bullets de acción) e incorpora el **compromiso de BW Water de entregar el dossier de inspección para Bureau Veritas el viernes 24-Jul** (near-term commitment, junto a la familia de Control a Rev 0 el 31-Jul); lleva el link Synology del paquete N29. El correo conjunto a BV declara el **ITP (P22-BA-09-000-004 Rev 0) como documento base** de la planificación y que el link contiene la documentación vigente, con toda actualización por la misma vía.

> **Correo conjunto a Bureau Veritas** (`CORREOS/Julio 2026/2026-07-21/crear_correo_bv_weekly_inspection.py`): se le agregó el **hipervínculo de descarga** del paquete de inspección (link Synology de la carpeta `PAQUETE_INSPECCION_BV`, dado por el usuario); regenerado y refrescado en Word (1 hipervínculo verificado, sin em-dash/`§`). **Correo de cobertura del TM N29** (`crear_correo_tm29.py` + `_Descripcion.md`): listo con el `DOWNLOAD_LINK` **ya insertado** (enlace Synology del paquete del transmittal N29, dado por Luis el 21-Jul); el transmittal `.docx`/PDF y el correo se regeneraron con el link (verificado en ambos).

> **Ajustes finales del paquete BV:** la **carpeta 04_PROCEDIMIENTOS_QA_PENDIENTES fue retirada** (ya no hay procedimientos en Código 3; el 010 Rev D quedó Code 2 en 03) y se quitaron sus referencias en la guía (regenerada; el 00 queda solo con el PDF de la guía + NT-002; script y `.docx` en `HITO BUREAU VERITAS/_fuentes_guia_bv/`). **06_CRONOGRAMA confirmado sin cambios:** los 3 archivos del `SEMANA 20-07-26` son **internos de ADASA** (Progress Report Week 29, DDSR y el tracker de procura con proveedores/PO/escalamientos) y **no van al paquete de un tercero**; el 06 ya tiene el correcto (Gantt de fabricación 07-Jul + Project Schedule Rev A; la Rev B se emitiría el 23-Jul). Envío: TM N29 primero (insertar link N29 + `anti-ia revisar`), luego el correo conjunto BV-BW con el link del paquete. Ver [[project_bureau_veritas_inspection]].

### 2026-07-21 — QA final del PAQUETE_INSPECCION_BV (adjunto para Bureau Veritas) — LISTO

> Revisión QA final del paquete `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/PAQUETE_INSPECCION_BV` (43 PDFs). **Verificado por apertura de cada PDF:** la revisión interna del cajetín coincide con el nombre en los 41 documentos técnicos (incl. los actualizados/renombrados: Control Arch D, PLC&HMI C, IO List 5, Line List 0, Outline 0, 009 C, 011 B, FAT A, 010 D, familia de Control); la guía (Rev 1) es espejo exacto de las carpetas; baseline TM N29 coherente. **Correcciones aplicadas:** (1) sacados del paquete el script generador `crear_guia_paquete_bv.py` (tenía notas internas), el `.docx` editable de la guía y la cotización comercial de BV (600049) → movidos a `HITO BUREAU VERITAS/_fuentes_guia_bv/` (fuera del paquete); (2) renombrado el GA Skid (tenía un zero-width space en el nombre); (3) guía actualizada: agregado "preservación/embalaje/liberación de despacho" a los registros MRB (cierra el último ítem QKOM), etiqueta "Código 1" explícita para Outline Rev 0 y Line List Rev 0, y nota de que el Valve List es Rev D vigente pese al campo de portada en "A". **Seguimiento a levantar a BW Water:** corregir el campo de revisión de portada del Valve List (P22-LI-09-005-002) a D (defecto de cajetín; el historial y la comment sheet confirman D). Paquete listo para adjuntar al correo conjunto BV-BW. Ver [[project_bureau_veritas_inspection]].

### 2026-07-21 — Transmittal N29 (E67, submittal 25007-0067) — ENVIADO

> **TM N29** (`P22-TM-09-000-029-0`, submittal **25007-0067** = E67, 21-Jul), **4 documentos, todas re-revisiones**. Veredicto global **2 — Approved as Noted (2 Code 2 + 2 Code 1)**. **TM de recuperación**: cierra los dos Code 3 vencidos de N26/N27. Generado para **ordenar el baseline** antes del correo conjunto BV-BW.

> **Veredictos (verificados adversarialmente + render + CCS §6.5):** **HP/LP Pressure Test Rev D** (P22-BA-09-000-010, #105) → **Code 2**: el error crítico del N27 (75 bar de hidrotest sobre línea PVC DA-PVC-DN65-09-016) está **resuelto y verificado** — presiones por línea/material, 09-016 a 2 bar diseño/3 bar hidrotest, 135 bar solo en Super Duplex; residual = fijar edición ASME (NOTE-01). **UHPRO Structural Calc Rev B** (P22-CD-09-005-001, #108) → **Code 2**: responde los 7 comentarios del N26; **corte basal NCh 2369:2003 Zona 3 = 41,62 kN, utilización máx 0,454 < 1,0** (render confirmado), norma 2003 (no 2025); residuales housekeeping = PDF duplicado 58MB + CCS sin texto de comentarios (NOTE-01/02). **Outline Panel Drawing Rev 0 IFC** (P22-CD-09-008-001, #98) → **Code 1**: incorpora la RFI-002 completa (SS316L exterior+gland plates, internos galvanizados, NEMA 4X/IP66), cierra los 3 MINOR del N27, SLD reemitido Rev 1. **Line List Rev 0 IFC** (P22-LI-09-009-003, #38) → **Code 1**: consistente con el P&ID Rev D (09-016 50→2 bar verificado); declarar la corrección en el historial de revisión.

> **Artefactos:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-029-0/` (`crear_transmittal.py` → `TRANSMITTAL N29 ADASA-BW_WATER.docx` + PDF desde Word, 6 págs; `P22-TM-09-000-029-0_TRANSMITTAL.md`; `_ANALISIS_N29.md`; `COMENTARIOS/` con 2 CC_ADASA Code 2 — 010 NOTE-01 y Structural Calc NOTE-01/02 anotado con `garbage=1` por sus 58MB). **Master Register a N29** (`update_register_n29.py`, backup `_pre-N29.xlsx`): **49 C1 / 29 C2 / 6 C3 / 0 C4**, 108 items / 84 delivered, **29 TMs / 67 entregas**. Correo de cobertura `CORREOS/Julio 2026/2026-07-21/crear_correo_tm29.py`. **Feedback al paquete BV:** el 010 Rev D (ahora Code 2) se movió a `PAQUETE_INSPECCION_BV/03_PROCEDIMIENTOS_QA_APROBADOS`; guía Rev 1 y LEEME actualizados. **Pendiente pre-envío:** reemplazar `DOWNLOAD_LINK` (Synology) en transmittal y correo; `anti-ia revisar` sobre el `.md`; envío lo hace Luis. Ver [[transmittals]], [[reference_fat_seco_vs_sat_taltal]].

### 2026-07-21 — Correo conjunto a Bureau Veritas: plan de inspección de taller (Penang) por semanas — ENVIADO

> **Correo conjunto ADASA→Bureau Veritas, copiando al QAQC de Penang de BW Water** (`CORREOS/Julio 2026/2026-07-21/crear_correo_bv_weekly_inspection.py` + `2026-07-21_BV-Weekly-Inspection-Plan.docx` + `_Descripcion.md`). Correo NUEVO (asunto propio "Taltal SWRO Module - Weekly Shop Inspection Plan at Penang"), no reply al hilo de BW. **To:** Luis Arcila (Bureau Veritas Chile). **CC:** Mohd Adnin Zulkifli + Lokman Hakim Mat (QAQC Penang, contactos que entregó Magdier Arias el 21-Jul) + Magdier/Eduardo/Stephane (BW Water) + Victor Gutierrez/Jorge Guevara/Ronald Pellejero (ADASA).

> **Cambio pedido:** presentar los hitos **por semana** (no por día como el correo del 18/20-Jul), con la actividad de cada semana definida y **3 visitas por semana**. Tabla de 7 filas: 6 semanas de vigilancia (3 visitas c/u = 18 QAQC) + semana de FAT (7 jornadas) = 25 (oferta BV 600049 Rev 2); alcance semanal per NT-002 Section 3.2 (W1 spools/PMI SDX · W2 NDE/dimensional · W3 hidrostática 135 bar+RO vessel Hold · W4 coating/ensamble · W5 posicionamiento · W6 bomba HP/turbos+panel · FAT ~7-12 Sep). Las fechas-día exactas las fijan las notificaciones H/W del taller (BAE Cl.37). **Programa verificado** contra el Week 29 (20-Jul): **sin cambios** vs la referencia fija del 14-Jul; ninguna ventana se movió; bomba HP+turbos siguen llegando ~2-Sep (estatus FEDCO "D" por reposición de caja de bornes, sin mover fecha). Coordinación: (1) BV confirma Semana 1 firme + disponibilidad; (2) Penang cursa las notificaciones H/W; (3) kick-off antes de la Semana 1. anti-ia OK; sin em-dash/§/IDs internos; sin jornadas/costos BV; metadatos limpios; Word refrescado (637 palabras/2 págs). **Nota de postura:** este correo une a BV y BW Water en un mismo hilo, abandonando la separación previa (`feedback_bv_no_nombrar_bw_water`) de forma deliberada. **Pendiente: revisión de Luis y envío (BORRADOR → ENVIADO + respaldo).** La confirmación de V2-V6 a BV se comprometió para el **Vie 24-Jul**. Ver [[project_bureau_veritas_inspection]].

### 2026-07-21 — Respuesta a BW Water: recovery del panel PLC-LCP (reencuadre FAT seco / SAT Taltal) — ENVIADO

> **Contexto.** BW Water envió dos correos el 20-Jul. **(1)** Eduardo reenvió la respuesta de Billy Tan al thread del panel PLC/LCP (*"Re: 25007 Taltal: PLC/LCP Panel Delivery - Notice of Delay"*, 20:47) con las contestaciones en azul a los 3 puntos de ADASA del 07-Jul. **(2)** Reenvió el plan de despacho desde Penang bajo EXW (*"20.25.6501 TALTAL: RFQ FOR PACKING COST"*, 21:00), el "Ex Work shipment details" comprometido el 16-Jun (**"20.25.6501" = nº de proyecto interno de BW Water**, no una cotización). El de packing NO responde un correo de ADASA — lo inicia BW.

> **Análisis del recovery del panel.** BW **no rebatió** la reserva de responsabilidad/EOT (queda sin contestar, a favor de ADASA). De los 3 puntos que pidió ADASA: (1) **no comprometió una fecha única** — dio dos secuencias que no reconcilian (panel listo a embarcar 7-Ago / taller BW 23-Ago vs FAT taller 26-Ago→5-Sep, listo 7-Sep); (2) el FAT "mantiene alcance" pero el software FAT es **"dry test only"**, sin bomba HP, verificando solo voltaje/Hz del VFD (reducción real de integridad de prueba del lazo de la bomba); (3) **concede** que el RFS 12-Sep excluye la bomba HP y que la fecha final depende de la entrega Fedco.

> **Respuestas (21-Jul, cadenas separadas, Reply-To a cada thread).** **(A) Panel — postura firme:** `CORREOS/Julio 2026/2026-07-21/crear_correo_plc_recovery_response.py` + `2026-07-21_PLC-Panel-Recovery-Response.docx` + `_Descripcion.md`. Acusa el recovery como información sin renunciar a la reserva; exige (1) una secuencia integrada con una fecha comprometida por hito; (2) **concuerda con el split FAT seco / ensayo con agua en sitio** — el FAT es seco per ET (P22-ET-09-000-001-0) Section 8, y el ensayo con agua (bomba HP bajo carga, performance del RO) es del comisionamiento y Performance Tests en Taltal per ET Section 9/10.2 e ITP Rev 0 aprobado (P22-BA-09-000-004) Section 10-11; sobre esa base: (a) FAT seco ejecutado completo per el ITP y registrado; (b) los ítems que el FAT seco no cierra (trips de devanado/rodamiento, trip de vibración de la bomba, lazo de secuencia/presión) se llevan al comisionamiento/Performance Tests de sitio, no se cierran en el FAT, y el FAT Procedure detallado + el Performance Test procedure de sitio (Hold de ADASA en el ITP) deben reflejar el split; (c) el FAT y el Dispatch Release **no son aceptación funcional/de desempeño** (queda en la prueba de 2 días en sitio, mandatoria para Recepción Provisional); (3) fecha de embarque con la bomba instalada, con la aceptación funcional/desempeño separada en SAT Taltal. Autorreferencia corregida: sin "letter/carta" (ADASA solo emite emails/NT/RFI); la posición del 07-jul se cita como email + respuesta a RFI 25007-RO-RFI-0002. To Eduardo, CC reply-all del hilo (8 de BW Water). **ENVIADO 21-Jul-2026 10:20** (respaldo `CORREOS/Julio 2026/2026-07-21/Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf`; cuerpo verbatim del borrador). Nota: salió como reply-all, por lo que los CC internos ADASA (Victor Gutierrez/Ronald Pellejero) que agregaba el borrador **no quedaron en el envío**. **Trazabilidad a comentarios por transmittal:** la respuesta NO reabre ningún comentario del panel (enclosure/HART/datasheets CERRADOS — Outline Rev C Code 2 en N27, LCP DS Rev 1 Code 1 en N25, PLC&HMI DS Rev C Code 2 en N26 — esa cadena es la defensa contra el EOT); su único impacto es diferir de FAT a SAT el cierre de la condición de firma RTD del FAT Rev A y de la familia de Control (Code 2 en N28), verificables recién con la bomba corriendo en el comisionamiento/Performance Tests de sitio (ITP Rev 0 Section 10-11), no en el FAT seco. **(B) Packing/EXW — reservar el costo:** `.../crear_correo_packing_exw_response.py` + `2026-07-21_Packing-EXW-Response.docx` + `_Descripcion.md`. Confirma el alcance logístico EXW de ADASA (20'GP side-loader, haulage del 40'HC y 20'FR, freight forwarding/aduana/flete) y pide loading schedule + vessel closing date; **reserva el packing cost**: bajo EXW el embalaje de exportación es alcance/costo del vendedor — pide a BW aclarar si pretende cargarlo y su base contractual. To Eduardo, CC Gehant/Faizah Bardan/Lokman + Victor Gutierrez. **Quedó BORRADOR (no enviado; foco en el panel por decisión del usuario).** Ambos anti-ia VERDE (inglés, contractual); metadatos limpios (autor Luis Rivera Gonzalez / Aguas de Antofagasta / en-US). **Panel ENVIADO 21-Jul-2026; pendiente menor: dejar respaldo PDF/.msg del envío en la carpeta. El correo de packing sigue BORRADOR (no enviado).** Ver [[project_plc_delay_rfi002_07jul]], [[project-procurement-22jun]].

### 2026-07-20 — Cotización de repuestos 2 años recibida (15-Jul) + auditoría + rechazo por forma — ENVIADO

> **Recepción.** El **miércoles 15-Jul-2026 15:29** Eduardo Yamauchi respondió al thread propio *"Formal Re-validation of Spare Parts Quotation C4300"* con la cotización actualizada (`PROGRAMA y CONTRATO/REPUESTOS DE 2 AÑOS/Recomended 2-year spare parts.pdf`). **4,7 meses y 6 recordatorios** desde la solicitud original del 26-Feb (el thread archivado aportó tres recordatorios que no estaban documentados: 12-May 10:13, 25-May 14:29 y 15-Jun 15:39, este último ya declarando *"this is currently holding our procurement decision"*). Cierra el reclamo abierto en la Bitácora del 13-Jul. **Total: USD 43.790 → USD 51.224,50 (+17,0% sobre el declarado; +20,4% sobre la suma real).** Llegaron por fin los **kits de servicio de los turbochargers** exigidos desde febrero (FEDCO KH060-CBK / KH060-TBK, HPB-60 Super Duplex, 1 set por turbo a USD 1.540).

> **Válvula solenoide — punto cerrado.** BW Water declara *"Solenoid valve was removed – not needed anymore as it was not used in the project"*. Verificado y **aceptado**: era la línea `Bray Series 63, 120VAC, 2 un., USD 3.300` de la lista de 2 años de la oferta, un **piloto solenoide para actuadores neumáticos**. La ET nunca la exigió; no existe ningún tag solenoide en la Valve List Rev D (111 válvulas), la IO List Rev C ni la Equipment List Rev B; el diseño usa solo válvulas manuales y VE motorizadas eléctricas sobre Ethernet/IP, sin aire de instrumentos. Arrastre de plantilla desde el origen. **Efecto colateral:** el **Manual O&M Rev A** instruye *"open the corresponding solenoid valve by manually switching the knob"* — la propia declaración de BW Water lo confirma como boilerplate genérico; entra como observación en la revisión del **Rev B (vence 31-Jul)**.

> **Auditoría línea por línea** (`PROGRAMA y CONTRATO/REPUESTOS DE 2 AÑOS/_ANALISIS_REPUESTOS_15JUL.md`, interno, con extracciones en `md/`). De 24 líneas, **once** fallan contra el diseño aprobado y **cuatro** llevan alzas de 43% a 372%. Drivers: (1) el ítem más caro, **USD 9.560**, cambió de descripción de *SWRO High Pressure Pump **Service Kit*** a ***Mechanical Seal*** **a precio idéntico y sin nota** (las otras cuatro modificadas sí llevan *"Price updated"*), y conserva part no. **MSD-130** cuando la bomba es una **Fedco MSD-7016**; (2) pH y ORP siguen como **Foxboro pH 10** frente a **Rosemount 3900 + 1056** (y el ORP arrastra el part no. del pH); (3) manómetros en **Monel** frente a **Wika con sello Superduplex 2507**; (4) el acople flexible cambió de fabricante a **Hengshui Snowate** (SS2205) manteniendo precio; (5) entre las válvulas, **no existe válvula de bola DN50 ni mariposa DN80 en PVC**, la única mariposa DN65 es super dúplex ANSI 900 motorizada, y se cotizan **5 repuestos DN40 contra 1 válvula instalada**. **Omisión de cobertura:** las **64 válvulas de bola DN15** (34 PVC + **30 CE3MN ANSI 900 del circuito de alta presión**) no tienen ningún repuesto. **Error aritmético en la oferta original:** declara **USD 43.790** mientras sus 22 líneas suman **USD 42.550** — 1.240 de más, cifra que ADASA citó en toda la correspondencia desde febrero. **Forma:** el PDF no contiene ninguna imagen (sin membrete, logo ni firma) y sus metadatos declaran `TALTA_UHPRO_2Y_Spare_Parts-EY.xlsx`, autor `Eduardo Yamauchi`, productor `Microsoft: Print To PDF`: es la impresión de una planilla de trabajo, sin el nombre de la empresa.

> **Decisión del mandante: ADASA ejerce la opción de 2 años**, de modo que el documento pasa a ser base de orden de compra. **Correo de respuesta** (`CORREOS/Julio 2026/2026-07-20/crear_correo_repuestos_revalidacion.py` + `.docx` + `_Descripcion.md`, **ENVIADO 20-Jul-2026**, 277 palabras; Reply-To al thread propio, cadena separada de transmittals y de la minuta; To Yamauchi + Frezzi, CC Guevara/Gutierrez + Gehant). **Redactado por el usuario, con un solo eje: rechazo por forma.** El archivo recibido es una planilla de trabajo, no una oferta comercial, y no puede procesarse en el ciclo interno de revisión y orden de compra. Pide reemitir como **documento comercial controlado** con cuatro requisitos mínimos: **emisión formal** (papelería e identidad corporativa BW Water, número de cotización con índice de revisión, fecha, **firma del representante legal o del responsable comercial autorizado** con nombre y cargo); **plazo de entrega** (lead time ex-works por línea en semanas desde la PO, más tránsito y punto de entrega, con los long-lead identificados); **condiciones comerciales** (validez, moneda, Incoterm 2020 con lugar, condiciones de pago); y **reconciliación de alcance** (cada línea referida al TAG del equipo que sirve, con el part number del ítem efectivamente suministrado). **Deadline viernes 31-Jul-2026**, fijado por ADASA y no pedido como compromiso de BW Water (ya incumplieron tres fechas propias: 22-Jun, 03-Jul, 10-Jul). El punto de la solenoide **no se menciona** (aceptado y cerrado antes). **Se reserva para la respuesta a la reemisión**, por decisión de método (se discute contra un documento formal, no contra una planilla): el cambio *Service Kit → Mechanical Seal*, las cuatro alzas, el part no. MSD-130, los instrumentos obsoletos, las válvulas inexistentes, la diferencia de USD 1.240 y los repuestos DN15. anti-ia VERDE (checklist B); metadatos limpios. Pendiente menor: dejar respaldo PDF/.msg del envío en la carpeta. Ver [[project_cotizacion_repuestos_2anos]], [[feedback_rechazo_por_forma_dos_tiempos]].

### 2026-07-20 — TM N28 (familia de Control, E65+E66) ENVIADO

> **TM N28** (`P22-TM-09-000-028-0`, submittals 25007-0065 [E65, 14-Jul] + 25007-0066 [E66, 17-Jul], **4 documentos de la familia de Control**). Veredicto **2 — Approved as Noted, tally 4 Code 2**. Los hijos de la Control Philosophy que llevaban **6-7 ciclos vencidos** por fin se entregaron: **Control & Sequence Chart Rev A** (P22-LI-09-008-017, primer issue, el "Operating Sequence Chart no emitido"), **Alarm & Interlock List Rev C** (015), padre **Plant Control Philosophy Rev E** (001), + **IO List Rev 5** IFC (008-001). La familia quedó **internamente inconsistente** (reconciliación cruzada de tags/setpoints a Rev 0). **Regla del usuario aplicada:** el comentario es sobre el documento; si el punto lo desarrolla otro documento y aquí solo falta reflejarlo → **Code 2, no Code 3** (los 4 son correctos en lo que cada uno desarrolla). Drivers verificados a mano: la CP Rev E **reabre el swap winding/bearing** que sus hijos ya corrigieron (TE-09-001=Bearing en la CP vs Winding en Alarm List/IO List/Instrument List) + Trip 155°C vs Class B; el Alarm List pone la **vibración AHH 10.0 sobre un transmisor de rango 8.9** (trip inalcanzable); el Sequence Chart Nota 5 **reintroduce el bypass por TDS** que la CP prohíbe. El correo pide re-emitir los 4 como **conjunto coordinado a Rev 0** con dos definiciones fijadas (mapeo winding/bearing + trip de vibración alcanzable). Metodología completa: triaje + extracción E65/E66, revisión adversarial (4 agentes) + verificación manual + revisión CCS ítem-por-ítem (**norma nueva CLAUDE.md §6.5**), disposición interna `_ANALISIS_N28.md`. **4 CC_ADASA** (todos Code 2, verificados por render). **Master Register a N28** (`update_register_n28.py`): **48/28/8/0, 108 items / 84 delivered, 28 TMs / 66 entregas**. Correo de cobertura `CORREOS/Julio 2026/2026-07-20/crear_correo_tm28.py` (ejecutivo y directo, link Synology, deadline vencidos Vie 31-Jul). **Estado: ENVIADO 20-Jul-2026** — PDF del transmittal generado desde Word (TOC refrescado, `exportar_pdf_word_mac.sh`, §3.13 CLAUDE.md) + paquete subido a Synology. Ver [[project_tm28_state]], [[transmittals]].

### 2026-07-20 — Dos correos a BW Water ENVIADOS: calendario Hold/Witness (inspeccion BV) + respuesta al pilot test FEDCO

> **(1) Respuesta al calendario Hold/Witness de BW Water** (`CORREOS/Julio 2026/2026-07-20/crear_correo_bv_calendar_bwwater.py` + `2026-07-20_BWWater-HW-Calendar-Response.docx` + `_Descripcion.md`, **ENVIADO 20-Jul**; reply-all al thread "RE: Taltal - Designation of Third-Party Shop Inspector and Inspection Schedule"; To Eduardo Yamauchi + Magdier Arias [Quality Manager BWW, sumado el 15-Jul] + Stephane Gehant, CC Gutierrez/Guevara/Pellejero). Acusa a Magdier + recibe el calendario H/W (Excel de Mohd Adnin, 15-Jul); confirma V1–V4 alineadas; **declara el Recovery Schedule del 14-Jul como referencia fija/inamovible** (fabricacion/FAT/despacho firmes, no deben correrse mas) con el calendario y la movilizacion del inspector ancladas a el. Exige: (1) ubicar V5/V6 en el programa fijo (ambas puestas en 09-Sep pese a que el posicionamiento corre de ~13-Ago a 03-04 Sep); (2) alinear el FAT (el calendario pone 16–18 Sep vs el programa fijo que cierra el FAT el 08-Sep con ready-to-ship 09–10 Sep) + Dispatch Release (Hold del 40%) + que la reduccion 10→5 dias preserve el alcance minimo del FAT; (3) **posicion FEDCO** — Bureau Veritas atestigua solo en Penang, ADASA NO asiste a pruebas FEDCO en EE.UU., pero BW Water debe entregar toda la documentacion de las pruebas FEDCO en el dossier de entrega; (4) Kick-off Meeting; (5) notificaciones formales H/W (BAE Cl.37, V1 28-Jul ya dentro de los 30 dias); (6) reemitir los 3 procedimientos Code 3 (009/010/011). Cierre endurecido: "any deviation from the fixed schedule must be notified in writing and in advance, stating its cause". anti-ia VERDE; metadatos limpios. Adjunta el Progress Update 14-Jul. Ver [[project_bureau_veritas_inspection]].

> **(2) Respuesta a la invitacion de FEDCO al pilot test** (`CORREOS/Julio 2026/2026-07-20/crear_correo_fedco_pilot_reply.py` + `2026-07-20_FEDCO-Pilot-Test-Reply.docx` + `_Descripcion.md`, **ENVIADO 20-Jul**; Reply-To al thread "25007 Taltal: FEDCO - Pilot Testing" [Yamauchi 15-Jul]; To Eduardo, CC Gutierrez/Guevara/Pellejero + Gehant). FEDCO invito a Aguas de Antofagasta a asistir al pilot test de las bombas HP + turbos en su fabrica (EE.UU.); ADASA **declina**: el atestiguamiento via Bureau Veritas se limita al FAT en Penang, no se viaja a pruebas FEDCO en EE.UU.; a cambio **exige toda la documentacion de las pruebas FEDCO (protocolos pilot/factory test, criterios de aceptacion, resultados, certificados) en el dossier de entrega**, disponible para el inspector en Penang. **Consistente con el punto 3 del correo del calendario.** Cadena separada del atraso/root-cause Fedco (thread Schedule Update). Transaccional ~110 palabras; sin em-dash en prosa; metadatos limpios. Ver [[project_fedco_fat_conflict_14may]].

> Pendiente menor comun: dejar respaldo PDF/.msg del envio de ambos en su carpeta.

### 2026-07-19 — Auditoría y reestructura de README/CLAUDE (eje cronológico único) — INTERNO

> Auditoría de gobernanza documental (pedido del usuario): los dos archivos habían dejado de cumplir su función primaria por deriva de ejecución. **README:** se eliminaron las dos estructuras cronológicas paralelas que competían con esta Bitácora — la "Cronología del Proyecto" (narrativa por fases) y los bloques de detalle-por-carpeta de "Transmittales histórico" (redundantes con las entradas de aquí; git los preserva). La Bitácora queda como ÚNICO eje cronológico; toda referencia estable se agrupó bajo un solo `## Referencias Durables` (Información, Estructura, Baseline, Equipos, Contactos, **Índice de Transmittales N1→N28**, Registro de Revisiones por ítem, QA Nomenclatura, Adicionales, Revisión BL). **CLAUDE.md:** se retiraron las citas de eventos con fecha incrustadas en reglas (`TM N`, `Regla del usuario DD-Mmm`, `Aplicado: RFI…`) — la regla queda atemporal con su procedencia colapsada a `(ver [[memoria]])`, per §12; se afiló §12 (eje único + bloque "Prohibido en CLAUDE.md") y se subió a v6.27. Respaldos `README.md.bak_pre-audit-19jul` y `CLAUDE.md.bak_pre-audit-19jul`. **Estado: INTERNO** (no se emite; git como red de seguridad).

### 2026-07-14 — Status update BW Water (Week 28) + validacion de fechas de visitas BV — correo a BV Chile ENVIADO

> **Paquete recibido** (correo Yamauchi 14-Jul 15:44, `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 13-07-26/`, ZIP descomprimido en `ZIP_EXTRAIDO/`, extracciones en `md/`): Recovery Schedule actualizado (impreso 14-Jul, 11 pags), Progress Report Week 28, DDSR 13-Jul (89.3% approval, 76 docs: 47 Approved / 13 AAN / 10 R&R / 4 Not submitted / 2 Submitted) y tracker de procurement.

> **Slips silenciosos** (tracker 13-Jul vs 22-Jun, Change Log vacio): **bomba HP + 2 turbos Fedco EAP Penang 05-Ago → 02-Sep (+28d)**; **panel PLC KVC 29-Jul → 23-Ago (+25d)**; frames estructurales 01-Jul → 20-Jul (+19d) y **degradados de C a E** (PO pendiente de confirmacion del calculo sismico; UHPRO Structural Calculation en R&R, reingreso 15-Jul). Schedule proyectado: spools 17-Jul→10-Ago; estructura skid 8–15-Ago; pintura 17–24-Ago; vessels al contenedor 13–15-Ago; HP pump al contenedor 3–4-Sep; bloque FAT 24-Ago→08-Sep; **ex-works Penang 09–10-Sep** (Rev A decia 15-Ago → +26d, ya reclamado el 29-Jun); llegada a sitio 26-Oct; **Performance Test termina 15-Dic** (Rev A: 19-Nov). Week 28: spool 0%, container mod 75-95%, SDX llego 10-Jul. Bombas CIP (NTK) van airfreight **directo a sitio** (02–13-Sep), no a Penang → fuera del FAT testificado (gap tipo KVC, decision de alcance pendiente).

> **Validacion de las ventanas NT-002** (consulta de BV Chile por fechas oficiales): **V1 27–31 Jul SE MANTIENE** (spools en curso); V2 3–7 Ago parcial (NDE si; dimensional del skid se corre); V3 hidrostaticas 10–14 Ago se corre ~1 semana; V5 se parte (vessels antes, HP pump despues); V6 31 Ago–4 Sep sostenible; **FAT base 07–12-Sep con desplazamiento probable de ~1 semana (14–19-Sep)** — el bloque FAT de BW Water termina en papel el 08-Sep con ex-works 09–10, pero con la bomba instalandose el 03–04-Sep quedan 3-4 dias habiles para un FAT testificado de 7 jornadas (infactible). Las fechas firmes las fija el calendario H/W que BW Water debe entregar el **viernes 17-Jul** (revision en la weekly del martes 21-Jul).

> **Correo a BV Chile** (`CORREOS/Julio 2026/2026-07-14/crear_correo_bv_fechas.py` + `2026-07-14_BV-Fechas-Visitas-Penang.docx` + `_Descripcion.md`, **ENVIADO 14-Jul-2026**; a Luis Rodrigo Arcila, CC Victor Gutierrez): confirma V1 para movilizacion inmediata; tabla V1–V6+FAT completa con V2–V6 "Planificada — puede variar en dias" (decision usuario: enviar calendario completo sin anticipar corrimientos semanales); **compromiso ADASA: confirmacion final a BV el viernes 24-Jul** (ajustes del orden de dias por visita de 3 jornadas); FAT en banda 07–12-Sep base / 14–19-Sep. Espanol es-CL, anti-ia VERDE. **Sin nombrar a BW Water** (regla del usuario: "el fabricante" / "taller de fabricacion (Penang)"; barrido = 0 menciones — ver memoria `feedback_bv_no_nombrar_bw_water`). No se adelantan a BV la inconsistencia interna del schedule BW Water ni los 2 frentes abiertos que vencen el 17-Jul (FAT 10→5 dias no acordado; sitio del FAT Fedco sin confirmar). Pendiente menor: dejar respaldo PDF/.msg del envio en la carpeta. **Housekeeping:** el correo de la NT-002 quedo confirmado como **ENVIADO el Mie 08-Jul 17:39** (a Yamauchi + Gehant, CC Gutierrez/Guevara/Pellejero) — `_Descripcion.md` del 07-Jul actualizada. Ver [[project_bureau_veritas_inspection]].

### 2026-07-13 — Replica a la minuta de la weekly call del 07-Jul (entregables vencidos + correcciones de registro) — ENVIADO

> **Correo** (`CORREOS/Julio 2026/2026-07-13/crear_correo_minuta_07jul_followup.py` [cuerpo] + `_Descripcion.md`, **ENVIADO 13-Jul-2026**). **Reply-All al thread de Eduardo Yamauchi** *"25007 Project Taltal - Weekly Coordination Call - Notes 07-Jul-2026"* (07-Jul, 16:13). Cadena **separada** de la del TM N27, enviado el mismo dia por la cadena regular de transmittals.

> **Dos actas divergentes.** La minuta **oficial de BW Water** es descriptiva, en voz pasiva, **sin un solo responsable asignado** y con 3 fechas (panel 13-Ago, skid ~12-Sep, I/O List 10-Jul). El **memorandum interno de ADASA** del mismo dia registra **8 acciones con responsable y plazo**. BW Water **omitio de su acta** las 4 que mas le exigen (repuestos con separacion de mandatorios, layouts + modelo 3D, anclaje sismico al frame, RFI-002) e **introdujo 2 elementos que le favorecen**: que el atraso del panel lo causo *"the change from the original enclosure specification to NEMA 4X"* y que el **FAT baja de 10 a 5 dias habiles**.

> **Verificacion previa (regla anti-invencion).** Contrastado contra las entregas reales: **el Painting Procedure Rev B SI llego el 10-Jul** (E63) y era uno de los vencidos del deadline consolidado del N26 → **no se reclama**. Entre el 08 y el 13-Jul no entro nada mas de BW Water. La **IP estatica del PLC es accion de ADASA** (el valor ya vive en el Data Transfer List `P22-LI-09-008-004` Rev 1 aprobado: 192.168.0.1 / 255.255.255.0, ADASA = Modbus master) → **no se le imputa a BW Water**.

> **Reclamo 1 — cotizacion de repuestos, nunca recibida (4,5 meses).** Solicitada el **26-Feb-2026** (plazo 07-Mar), reiterada el **26-Mar** (plazo 31-Mar). BW Water la comprometio **tres veces en sus propias minutas**: *"to be released next Monday"* (16-Jun → 22-Jun); *"BW Water to submit the complete two-year spare parts package by 03-Jul-2026"* (30-Jun); y **viernes 10-Jul** en la call del 07-Jul. Su acta del 07-Jul la degrada a *"waiting for final quotations from vendors"*, **sin fecha**. Se exige: lista **Mandatory/Critical (USD 17.310, ya contratada)** separada de la **Recommended Two-Year (USD 43.790 EXW)** — la desviacion en esa categorizacion es la causa declarada del atraso administrativo; **kits de servicio de los turbochargers SIP-09-001 y SIP-09-002** (part numbers, cantidades 2 anos, precios unitarios), ausentes desde el origen; y **fecha firme de validez**. **Deadline endurecido: HOY, fin de la jornada del lunes 13-Jul-2026** (no mas plazos) — se exige enviar **con lo que tengan** (cifras preliminares/presupuestarias donde falte cotizacion firme, p.ej. los kits de turbocharger) **para incorporar el costo al presupuesto del proyecto**; el balance con fecha firme a seguir.

> **Reclamo 2 — otros vencidos del 10-Jul.** No vinieron en E63 ni E64: **I/O List** (target propio de BW Water), **cronograma actualizado** con el hito ~12-Sep, **weekly fabrication report**, **document status report**. Mas los 4 entregables de ingenieria que vencieron el mismo dia (Grounding Rev F, tabla FAT/SAT, 3 planos de ruta, Control Philosophy children), que el TM N27 reitera. **Deadline: viernes 17-Jul-2026.**

> **Correcciones de registro (3).** (a) **Causa del atraso del panel:** ADASA no acepta la causalidad NEMA 4X — remite a la carta del 07-Jul; el NEMA 4X/IP66 en SS316L lo fijan el **LCP Datasheet aprobado de BW Water** y el **IFC SLD**, la desviacion fue el Outline, ya corregido en Rev C. **El silencio sobre esto habria dejado en pie la base de un claim de extension de plazo.** (b) **Duracion del FAT:** la reduccion 10 → 5 dias habiles **no fue acordada**; la confirmacion escrita que ADASA pidio el 07-Jul (que el alcance completo se preserva) **sigue pendiente** — se trata como pendiente, no como frente nuevo. (c) **Sitio del FAT de la bomba Fedco:** BW Water declara inspeccion *"at FEDCO and manufacturing in Penang"* (dos sitios) con la ubicacion **sin confirmar**; Bureau Veritas fue contratado asumiendo **Penang**, un segundo sitio es alcance y costo adicional y **bloquea la asignacion de inspectores** → confirmar al 17-Jul. Cierra pidiendo confirmacion de las 2 acciones que ADASA registro y el acta de BW Water omite (layouts + modelo 3D; anclaje sismico).

> **Nota de citacion.** La oferta numera los repuestos **3.12** (mandatorios) y **3.13** (2 anos); los correos del 26-Feb y 26-Mar citaron *"Section 3.8"*. El correo cita **por nombre + monto** para no arrastrar el error. Verificacion: `anti-ia revisar` **VERDE 5%**; metadatos limpios (author=ADASA, en-US). Ver [[project_correo_replica_minuta_07jul]], [[feedback_acta_proveedor_corregir_registro]].

### 2026-07-13 — Transmittal N27 RE-ESCOPEADO (E63+E64, 6 docs) — ENVIADO

> **TM N27 (P22-TM-09-000-027-0)** cubre **E63 + E64** (submittals 25007-0063 + 25007-0064), **6 documentos**. Veredicto **3 — To Be Revised. Tally 4 Code 2 + 2 Code 3.** **Re-escopeado:** el N27 estaba en BORRADOR (E63, 2 docs) cuando llego la E64 (4 docs, 13-Jul); con el correo aun sin enviar se **folded E64 en el N27** (patron validado, no se abrio N28). Con este TM el **paquete QA/fabricacion del N23 queda cerrado** (RO Vessel Hydro + Painting aqui; NDE en N26; solo HP/LP sigue abierto) y **el gate del enclosure del N20/N25 queda resuelto** (Outline Rev C).

> **Code 3 #1 — hallazgo de seguridad (HP/LP Rev C).** Responde a la observacion del N26 **adjuntando la Line List en vez de escribir la presion en el cuerpo**, con lo cual esa tabla pasa a ser la instruccion ejecutable. Ordena **75 bar de hidrostatica sobre `DA-PVC-DN65-09-016` (RO Brine Discharge)**, que es **PVC SCH 80 DN65 con brida Clase 150 y opera a 1 bar** pero arrastra un diseno de 50 bar: ejecutarlo **revienta la linea**. El diseno de 50 bar viene de la Line List Rev C aprobada Code 1 en el N18; la columna HYDROTEST nueva lo vuelve ejecutable. La Line List adjunta se rotula **"Rev 0"** (nunca transmitida). Accion: **Rev D** + reemitir la Line List; HP hydrostatic sigue Hold Point.

> **Code 3 #2 — O&M Manual (recalibrado por revision profunda de dependencia con Control/PLC-HMI).** Se aprobo primero como Code 2 tratandolo como documento autonomo; a peticion del usuario ("no aprobar si hay puntos abiertos con los entregables de los que dependen") se reviso en profundidad y **paso a Code 3**. Su **Seccion 4** reproduce secuencia/setpoints/HMI que la **Plant Control Philosophy Rev D** asigna a los hijos abiertos (Operating Sequence Chart 017 no emitido, Alarm & Control Setpoint List 015 Rev B Code 3, HMI Screenshots 016 Rev A Code 3) y **contradice el bypass aprobado** de la CP (abre VE-09-002 por TDS vs el lazo de presion que exige la CP). Accion: **Rev B**; no emite a IFC hasta que cierren los documentos de control gobernantes.

> **Cierres Code 2 (4).** **RO Vessel Hydrostatic Rev C (E64):** cierra el **CRITICAL del N26** — el formulario de 45,5 bar desaparecio y el **test report real (17-Jun)** evidencia los vessels a **91,01 bar (1.320 psi = 1,1×1200)** y **136,52 bar (1.980 psi = 1,1×1800)**, todos O.K., con certs de calibracion; es el ensayo por el que se canjeo la estampa ASME (no reabrir el waiver). **Painting Rev B:** cumple las dos condiciones del N25 (equivalencia Jotun `TSS-DD-MYPC039-26` + 3 TDS = 355 µm, C5-M ISO 12944); solo queda el formulario de inspeccion. **Outline Rev C (E64):** resuelve el gate del enclosure — exterior/gland plates **SS316L, NEMA 4X/IP66**, internos galvanizados/CRS per la **RFI-002**; hoja 5 = tabla material Hoffman, hoja 14 = CCS de BW; BW se compromete a reemitir el SLD. **FAT Procedure Rev A (E64, nuevo):** FAT de hardware **completo y correcto** (cobertura ET verificada contra la IO List Rev 4 de 138 puntos + Electrical Load List VFD 93/11 kW). Se codifico Code 2 (no Code 3) tras la 2ª pregunta del usuario ("¿es porque el documento debe corregirse o porque depende de docs no aprobados?"): 3 de sus 4 items son **defectos intrinsecos** clericales/de referencia (cita los planos gobernantes con codigo ET en vez de CD y un Schematic Rev B que no existe; tags/typos; criterios vs docs aprobados) que se incorporan al emitir; el 4º, el **swap winding/bearing del RTD, es dependencia pura** del Alarm & Interlock List abierto — el FAT esta del **lado correcto** (= IO List Rev 4), asi que per §6.2 no degrada: se reclasifico a **NOTE-02**, va a la **Seccion 3** y la firma RTD queda condicionada. Los 4 van a **IFC Rev 0 sin nueva revision**.

> **Metodologia.** Triaje PDF por PDF (el Outline, plano A3, con `large-pdf-reader --mode drawing`) + **verificacion adversarial ANTES de generar** (4 agentes refutadores, uno por doc E64) + **revision profunda de dependencia** sobre O&M y FAT (verificacion a mano contra CP Rev D, IO List Rev 4 y Alarm & Interlock List Rev B). La verificacion **confirmo el cierre de los 2 gates y corrigio over-reach**: retiro la falsa bandera del "52 bar bajo" del O&M (es la descarga de la bomba HP + boost de turbo, correcto — la inconsistencia real es de setpoint entre secciones), evito afirmar que un gauge concreto midio el ensayo de 136,5 bar (el doc no lo mapea), refuto el "reuso de tags" del FAT (son sufijos de tags compuestos unicos), y **al re-examinar el FAT distinguio defecto intrinseco vs dependencia** → lo dejo en Code 2 (el RTD es dependencia de Seccion 3, no baja el codigo). **6 CC_ADASA** en `REVISIONES/TRANSMITTALES/P22-TM-09-000-027-0/COMENTARIOS/` (**2 Code 3 + 4 Code 2**, ningun Code 1; el Outline anotado con posicionamiento 2D explicito, O&M OBS-02 sobre la matriz de control imagen y FAT **NOTE-02 RTD azul** sobre la tabla RTD; todos verificados por render PNG). anti-ia VERDE. Master Register a N27 (`update_register_n27.py`, restaura el baseline limpio antes de aplicar → idempotente; 4 updates + 2 filas nuevas #110 FAT [2-AN] / #111 O&M [3] + 6 RH; **48 Code 1 / 25 Code 2 / 10 Code 3 / 0 Code 4**; 107 items, 83 delivered; **27 TMs / 64 entregas**; backup `_pre-N27`). Regla nueva: [[feedback_revisar_manual_contra_documentos_de_control]].

> **Correo de cobertura** (`CORREOS/Julio 2026/2026-07-13/crear_correo_tm27.py` + `.docx`, **ENVIADO 13-Jul, 1 pagina**; respaldo `envio transmittal 27.pdf` en la carpeta): 6 docs; abre con el **safety item** (detener cualquier prueba de presion hasta reconciliar la linea de PVC), cierra los 2 gates + el **FAT como Approved-as-Noted** (correcciones de referencia/tags al emitir; firma RTD por la Seccion 3), un parrafo por el **O&M Code 3** (atado a los hijos abiertos de la Control Philosophy) y re-escala los vencidos con deadline consolidado **viernes 17-Jul-2026** (punteados a la Seccion 3 del transmittal, no re-enumerados). Carry-forward abierto (RO Vessel Hydro y Outline ya NO estan): Control Philosophy children (7o ciclo), UHPRO Structural Rev B, GA Antiscalant Tank Rev C, Equipment Layout Rev D, HMI Screenshots (N4), Grounding Rev F, FAT/SAT, 3 planos de ruta; cross-doc: Line List reconciliada, **SLD a reemitir** (compromiso BW), pernos de base (fundacion OOCC), Module Seismic Calc.

> **Formato condensado (13-Jul):** el transmittal se recorto de **16 a 9 paginas** eliminando las tablas OBS del §2 (cada subseccion quedo en `Response Code + Status corto + Action por rango de IDs`); el detalle itemizado vive en cada CC_ADASA. Estandar codificado en CLAUDE.md §3.2 y §6.3; ver [[feedback_transmittal_seccion2_condensada]].

> **Emision (13-Jul):** **link de descarga Synology** incrustado en el §4 del transmittal (URL completa) y en el correo de cobertura (ancla clicable); ambos `.docx` regenerados con el link, hipervinculo externo verificado. **Metadatos limpios** (`crear_correo_tm27.py` ya llama a `docx_metadata`; author=ADASA, en-US — corregido el defecto `author="python-docx"` de N25/N26). **ENVIADO 13-Jul-2026**, cadena regular de transmittals; el correo de la weekly call salio el mismo dia por su cadena separada. Ver [[project_tm27_state]], [[transmittals]], [[project_entregas_estado]], [[feedback_metadatos_correos_python_docx]].

### 2026-07-06 — Transmittal N26 (E57-E62, 9 docs: QA/fabricacion + I&C + estructura + GA) — ENVIADO 06-Jul-2026

> **TM N26 (P22-TM-09-000-026-0)** cubre **E57-E62** (submittals 25007-0057 a 25007-0062, 9 docs): ITP Rev 0, DS PLC & HMI Panel Component Rev C, UHPRO Structural Calculation Report Rev A, GA CIP Flushing Tank Rev A, GA Antiscalant Dosing Tank Rev B, NDE Plan Rev C, RO Vessel Hydrostatic Test Procedure Rev B, HP/LP Pressure Test Procedure Rev B, GA Antiscalant Dosing Pump Skid Rev B. Veredicto **3 — To Be Revised. Tally 2 Code 1 + 3 Code 2 + 4 Code 3.** Paquete mayoritariamente de cierre (7 re-revisiones + 2 nuevos: UHPRO Structural Calc y GA CIP Flushing Tank).

> **Drivers Code 3:** RO Vessel Hydrostatic Rev B (sin presion vinculante en el cuerpo; el formato Protec sigue en 45,5 bar vs los 1.980 psi = 1.800 x 1,1 que exigen ITP fila 2.2 y el waiver 02-Jun; no cierra el driver del N23); HP/LP Pressure Test Rev B (agrega el factor ASME B31.3 pero sin presion numerica; 90 vs 120 bar HP sin reconciliar); UHPRO Structural Calc Rev A (el Bolt Design at Base omite el anclaje de los equipos de proceso principales — bomba HP BH-09-001, turbos SIP-09-001/002, filtro RO FIL-09-001, tubos de presion BOI-09-001/002 = 4.160 kg — exigidos NCh 2369 Z3); GA Antiscalant Tank Rev B (cargas sismicas/anclaje NCh 2369 aun ausentes, diferidos por BW Water; no cierra TM N10 OBS-05). **Cierres Code 1:** ITP Rev 0 (IFC; incorpora las 2 ediciones del N23 — base sin estampa fila 2.2 + vessel test Witness→Hold Point) y NDE Plan Rev C (ediciones de codigo + mapeo junta-codigo; cierra N23). **Code 2:** DS PLC & HMI Rev C (cierra los 3 drivers del N21 — HART a nivel de instrumento por resistencia 250 ohm handheld, RTD 5069-IY4, typo; unico fix = inconsistencia interna de codigo -008-01 vs -008-001), GA CIP Flushing Tank Rev A (tag TK-09-001 + nozzle schedule vs datasheet), GA Antiscalant Pump Skid Rev B (fuerzas por perno; cierra materialmente N11 NOTE-06).

> **Metodologia:** workflow `tm26-review` (fan-out por documento con pregunta de cierre + obs previa embebida → verificacion adversarial por hallazgo con reglas anti-over-reach HART/soft-I/O/ASME → sintesis; 42 agentes; el DS PLC & HMI se re-corrio aislado por un loop de validacion de esquema). Calibracion doc-por-doc del usuario: DS PLC & HMI a Code 2 (por el codigo interno, no Code 1); GA Antiscalant Tank a Code 3 (sismico MAJOR en el propio GA). **7 CC_ADASA** en `REVISIONES/TRANSMITTALES/P22-TM-09-000-026-0/COMENTARIOS/` (4 Code 3 + 3 Code 2; planos verificados por render PNG, rotacion 270; ITP y NDE Plan Code 1 sin anotar). Master Register a N26 (`update_register_n26.py`; 7 updates + 2 filas nuevas; **48 Code 1 / 21 Code 2 / 12 Code 3 / 0 Code 4**; 105 items, 81 delivered; **26 TMs / 62 entregas**; backup `_pre-N26`). anti-IA VERDE.

> **Correo de cobertura** (`CORREOS/Julio 2026/2026-07-06/crear_correo_tm26.py` + `.docx`, BORRADOR) re-escala los vencidos con deadline consolidado **viernes 10-Jul-2026**: Grounding Rev F (17-Jun), FAT/SAT (15-Jun), Plant Control Philosophy children (6o ciclo), 3 planos de ruta (26-Jun), + Painting Procedure `P22-BA-09-000-011` (4o QA del N23, no entregado). Carry-forward abierto que E57-E62 no cerro: Painting Procedure, PLC-LCP Outline Panel Drawing Rev C (gate de fabricacion del enclosure), Equipment Layout RO Cartridge Filter horizontal (Rev D), HMI Screenshots (compromiso mas antiguo). **Estado: ENVIADO 06-Jul-2026** (correo enviado; entrega por link de descarga Synology + 7 CC_ADASA; respaldo `Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf` en `CORREOS/Julio 2026/2026-07-06/`). Pendiente: respuesta de BW Water (Rev C de los 2 procedimientos de presion + RO Vessel Hydrostatic; Rev B del UHPRO Structural Calc; Rev C del GA Antiscalant Tank; los Code 1/2 a IFC Rev 0; vencidos + Painting Procedure con deadline 10-Jul). Ver [[project_tm26_state]], [[transmittals]], [[project_entregas_estado]].

### 2026-06-29 — Fedco: reporte formal de causas pendiente (respuesta al Schedule Update del 26-Jun) — BORRADOR

> **BW Water respondió el 26-Jun** (`PROGRAMA y CONTRATO/PROGRAMA 26-06-26/`, correo de Yamauchi "25007 Taltal - Schedule Update") a la solicitud del 25-Jun. Entregó el **cronograma actualizado** (`.mpp` + "Progress Update" PDF, que es solo el Gantt impreso) y una **narrativa de causas en el cuerpo del correo** — pero **NO el reporte formal de causas** que ADASA pidió (compromiso de la call del 23-Jun: root cause + sequence of events + recovery actions). Verificado por extracción de los 2 PDFs: ningún reporte formal de causa raíz. Problemas: (a) el cronograma **propaga** el slip (shipping 15-Ago→10-Sep), no lo absorbe ("we will continue to closely monitor"); (b) Penang **02-Sep** es posterior al 21-Ago ya rechazado por escrito el 17-Jun y reabre el conflicto FAT/running-test integrado (NT-001); (c) sin respaldo documental del vendor ("as advised by the supplier"); (d) **atribuyen la causa al "delayed down payment received on 09 June"** — el anticipo 30% que ADASA fijó como costo de BW Water.

> **Correo de respuesta (BORRADOR, `CORREOS/Junio 2026/2026-06-29/crear_correo_fedco_root_cause.py`):** Reply-All al thread del 26-Jun; exige el **reporte formal por viernes 03-Jul** con 4 contenidos (fecha conciliada con carta/PO Fedco, no "as advised"; causa raíz + secuencia con documentos; acciones de recuperación + decisión del lugar del running test Penang/SAT con personal/ventana/costo; plan de ruta crítica del LCP). **Postura (decisión del usuario):** firme + reserva de posición, referencia **medida** al régimen de atraso (sin citar cláusulas de multa/terminación, no acusatorio); sobre la atribución al down-payment, **pide sustanciación SIN rechazar** (reserva "ADASA reserves its position on responsibility and does not accept any allocation by implication"; la disputa del anticipo 30% se deja a una vía contractual separada). **Verificación:** workflow `fedco-email-audit` (4 lentes: factual/anti-fabricación + postura + contractual + tono/anti-IA → síntesis) **VERDE, 0 obligatorias** — todos los anclajes de fecha confirmados, postura cumplida, sin error contractual; anti-IA aplicado (binarios "X, not Y" y em-dash parentéticos reducidos, conservando el `not "as advised"` como eco favorable). Fines contractuales del reporte (a seguir, NO citados a BW Water): multas BAE Cl.27/43.1, gatillo de terminación 30 días Cl.206; base para reportar el atraso al mandante. **Estado: ENVIADO 29-Jun-2026** (respaldo `Re: 25007 Taltal - Schedule Update.pdf` en la carpeta). Pendiente: respuesta de BW Water (reporte formal) para 03-Jul. Ver [[project_fedco_fat_conflict_14may]], [[project-procurement-22jun]].

### 2026-06-29 — Transmittal N25 (E55+E56, 6 docs I&C + estructura + coatings) — ENVIADO 29-Jun-2026

> **TM N25 (P22-TM-09-000-025-0)** cubre **E55 (25007-0055:** PLC-LCP Outline Panel Drawing Rev B, UHPRO Structural Design Criteria Rev B, Painting Specification Rev C**)** + **E56 (25007-0056:** IO List Rev 4, LCP Datasheet Rev 1, Static Mixer Datasheet Rev 0**)**. Veredicto **3 — To Be Revised. Tally 4 Code 1 + 1 Code 2 + 1 Code 3.** Cinco de los seis son re-revisiones que responden a observaciones ADASA previas (cierres de ciclo de N20/N22/N23/N24).

> **El Outline Panel Drawing es el único driver del veredicto 3 (gate de fabricación sigue abierto).** BW Water medio-corrigió la contradicción del TM N20: agregó "Exterior SUS316L", reemplazó el cooling de aire forzado por A/C sellado NEMA 4X y declaró el peso (814 kg), pero la fila MATERIAL aún lista frame/roof/rear panel/door como sheet steel bajo un encabezado "interior only" que incluye superficies expuestas, y FINISHING las pinta RAL 7035 — contradiciendo el "Exterior SUS316L" y el datasheet (FS66S SS316L unpainted). Su propia Consolidated Comment Sheet (pág 12 del PDF) dice "sheet steel solo para frame interior y puerta interior", pero el plano no lo dibuja así → re-issue Rev C con SS316L coherente en toda superficie expuesta. **Fundamento del Code 3 (revisión de trazabilidad del usuario, contra la ET Módulo):** el más fuerte e irrebatible es la **contradicción con los propios documentos aprobados de BW Water** — el LCP Datasheet Rev B (Code 2, *gobierna* el envolvente: SS316L/NEMA4X/IP66) y el IFC Single Line Diagram Rev 0 ("METAL CLAD NEMA4X/IP66"). La ET §5.4.1 (Tableros de fuerza y control, características constructivas) exige **NEMA 4X o IP equivalente, no inferior** (soporte; reforzado por PIE ITP 6.1), pero la **ET §5.4.3 permite acero pintado** → la ET **NO exige SS316L como material** (lo fija el datasheet aprobado). El framing del transmittal/CC_ADASA se reencuadró para liderar con la contradicción de documentos aprobados + ET §5.4.1 NEMA 4X y NO afirmar "la ET exige SS316L". Ver [[reference_et_tableros_nema4x_no_ss316l]].

> **IO List Rev 4 → Code 2 — Approved as Noted (re-verdict del usuario 29-Jun).** Las 4 señales de coordinación con el PLC externo (XA005/YA001/YA002/YA003, relay-contact) están **presentes y correctas — cierra OBS-01 del N24, el requisito prioritario está cumplido.** La única nota real es la celda de conteo de las dosificadoras (OBS-02 del N24: items 131/136 BOOL sin conteo, 129/134 con el "1" en columna DI), menor, a completar en Rev 0 (sin Rev 5). **Corrección de un over-reach propio:** el Code 3 inicial lo había gatillado una OBS-01 mía ("RUNNING dosificadoras = soft BOOL desde HMI, no feedback real"); la traza (Explore con citas) mostró que es **factualmente falsa** — esa señal nunca fue un contacto hardwired aceptado: ya iba sobre Ethernet/IP en Rev 2, **ADASA misma pidió relabelearla DI→soft en N20 NOTE-02**, el relabel se hizo en Rev 3 y **N24 NOTE-01 declaró el esquema Ethernet/IP de campo "accepted at N20 and not reopened"**. Exigir hardwired ahora sería un pedido nuevo que contradice N20 (anti-invención §6.2). Se retiró la OBS-01; queda una NOTE de confirmación de fuente (que el RUNNING FROM=HMI sea feedback real de bomba/VFD, no eco del faceplate). Ver [[feedback_soft_io_ethernet_aceptado_n20]].

> **Los 4 Code 1 cierran ciclos.** LCP Datasheet Rev 1 (cierra N24: UPS sheet 114 + código unificado), UHPRO Structural Rev B (cierra N23: sísmica NCh 2369 Of.2003 + caso de izaje con criterios padeye/yugo API RP 2A-WSD 1,35/2,0), Static Mixer Rev 0 (cierra N22: reconcilia condiciones de diseño + tasa de inyección), Painting Spec Rev C (matches ET marine 355 µm; Jotun condicionado a la equivalencia del Painting Procedure abierto en Section 3 + NOTE-03 cambio de código 005-002→006-002).

> **Metodología y trazabilidad.** Workflow `tm25-review` (22 agentes: revisión por documento → verificación adversarial de cada cierre contra el comentario previo + ET + Oferta → síntesis); bajó el Outline de cierre aparente a Code 3. **El cruce manual con el Master Register corrigió 2 premisas erróneas del workflow:** el Static Mixer (no "nuevo" — re-revisión de N22 Rev C, Code 2-AN) y el Painting Spec (re-revisión de N11 Rev B, con cambio de código que originó NOTE-03). **Y la revisión de trazabilidad del usuario corrigió un over-reach mío en el IO List** (Code 3→Code 2; ver bloque arriba). 2 CC_ADASA (IO List Code 2 + Outline Code 3; los 4 Code 1 sin anotación; placement verificado por render PNG; el Outline anotado en la hoja de especificación A1 sin tapar el cuadro). Master Register a N25 (`update_register_n25.py`; 46/21/12/0; backup `_pre-N25`). anti-ia VERDE (Checklist B). **Correo de remisión** (`CORREOS/Junio 2026/2026-06-29/`) escala los vencidos con deadline consolidado **Vie 03-Jul-2026**: Grounding Rev F (venció 17-Jun), FAT/SAT (15-Jun), Control Philosophy hijos (6º ciclo), 3 planos de ruta (26-Jun). **Estado: ENVIADO 29-Jun-2026** (transmittal + 2 CC_ADASA adjuntos directo, ~4,8 MB; el link de descarga Synology inválido se removió del transmittal; respaldo PDF en la carpeta). Pendiente: respuesta de BW Water (re-revisiones Rev C del Outline, Rev 5 del IO List, cierres de los Code 1 a IFC). Ver [[project_tm25_state]].

### 2026-06-25 — Insistencia por la minuta de la Weekly Coordination Call (23-Jun) + registro de los compromisos Fedco — ENVIADO

> **ADASA pidió la minuta de la reunión semanal del martes 23-Jun el mismo día y no obtuvo respuesta de Eduardo Yamauchi.** Este correo (Reply-All al thread `25007 Project Taltal - Weekly Coordination Call`) insiste con plazo firme (la minuta para el **viernes 26-Jun**) y deja por escrito, en el propio hilo, los dos compromisos asumidos en esa reunión: **(1) el cronograma re-secuenciado** que absorbe el slip de Fedco (HP pump BH-09-001 + turbochargers SIP-09-001/002) y **(2) el reporte oficial, en formato de reporte, del por qué y cómo ocurrió el retraso de Fedco**, con las acciones de recuperación. Exige confirmar la fecha de emisión comprometida de cada entregable para el 26-Jun.

> **Decisión de diseño:** el valor del correo no es solo perseguir la minuta (documento de BW Water) sino fijar el registro contractual de los dos compromisos en el hilo, independiente de si/cuándo Eduardo emite la minuta. Foco acotado — los pendientes del 22-Jun (spare parts quotes / ex-work details / estado de pago) siguen en su propia cadena (thread Meeting Notes 16-Jun), no se reabren aquí. Cuerpo `Document()` directo, 100% inglés, sin proponer reunión; `anti-ia revisar` VERDE; metadatos Word limpios; día de semana verificado (26-Jun = viernes). **Estado: ENVIADO 25-Jun-2026**, respaldo `ENVIADO A BW WATERS.pdf` en la carpeta. Archivos: `CORREOS/Junio 2026/2026-06-25/`. Ver [[project-procurement-22jun]] y [[project_fedco_fat_conflict_14may]].

### 2026-06-25 — ENTREGA 10 L&A (TT-011): cajetín corregido a "apto para construcción" → paquete BL actualizado

> **La ENTREGA 10** (carta `067-032-032-COR-TT-011`, 23-Jun-2026, "COMPILADO") re-emite el set civil completo un día después de la E9, corrigiendo el **estado del cajetín de la Rev 0** que la E8/E9 traían mal: en las **18 láminas** la fila Rev 0 de la tabla REVISIONES pasa de **"PARA USO E INFORMACIÓN"** a **"APTO PARA CONSTRUCCIÓN"** (misma geometría, misma Rev 0); en las **2 ET** civiles (Rev 1) la portada pasa de **"Aprobado Cliente"** a **"Apto para Construcción"**. La entrega trae además 6 MC (incluida la nueva **MC-002-003 Rev 0**), 4 IT y la cubierta.

> **Verificación (compuerta antes de tocar el paquete):** las 18 láminas se extrajeron con **large-pdf-reader modo drawing**; se confirmó por render de la tabla REVISIONES que las 18 traen Rev 0 = "APTO PARA CONSTRUCCIÓN" (diff de control contra las versiones E8/E9 del paquete, que decían "PARA USO E INFORMACIÓN"). El cambio de estado de las ET se verificó por diff del texto de portada. Re-emisión solo de cajetín/estado, sin cambio de contenido.

> **Actualización del paquete (solo la parte civil — decisión del usuario):** las 18 láminas + 2 ET del dossier `Bases REV 0/5. OBRAS CIVILES (A2)/` se reemplazaron por la versión E10 (byte-idénticas a la fuente, verificado por SHA256); las E8/E9 ("PARA USO E INFORMACIÓN") archivadas en `BORRADOR_REV0/_dossier_superseded_pre-E10/`. **BL regenerado** (`md_to_adasa_docx.py`, [CHEQUEO LAYOUT] OK; PDF por Word COM/win32com late binding) declarando los planos "en revisión 0, apto para construcción" en Antecedentes, Anexo A2 y la fila A2 de la Sección 9 → carpeta 1 (respaldos `_pre-E10`). LEEME e `00_INDICE` actualizados; carpetas excluidas refrescadas a E10 (cubierta ET-103 Rev 1 / MC-003-001 Rev 2; memorias +MC-002-003 Rev 0). El **Formato (A9) no se tocó** (cubicación 4.8/4.9 sigue como decisión separada). Sin transmittal a L&A. Ver memoria `project_entrega10_cierre_civil_rev0`.

### 2026-06-24 — RFI-001 (25007-RO-RFI-0001): confirmación de cumplimiento HART — módulo de entrada analógica y "4-20 mA + HART"

> **BW Water (Billy Tan / Engineering) emitió el RFI-001 el 22-Jun** pidiendo que ADASA confirme si la ET Sección 5.5 — Instrumentation Specification ("4-20 mA + HART") se cumple cuando los instrumentos de campo son 4-20mA+HART, el HART queda accesible por comunicador handheld en el lazo, y el módulo de entrada del PLC (**Allen-Bradley 5069-IF8**) adquiere solo la variable 4-20 mA, sin pass-through HART al PLC/SCADA; alternativamente, si el proyecto exige integrar HART al sistema de control (módulos I/O HART-capable o asset management dedicado), advirtiendo impacto de costo/plazo.

> **Respuesta ADASA: la configuración descrita cumple la Sección 5.5.** El protocolo 4-20mA+HART es requisito **a nivel de instrumento de campo**; la ET **no** exige pass-through HART al PLC/SCADA, módulos I/O HART-capable ni asset management dedicado (la comunicación del sistema de control exigida es Modbus TCP/IP sobre Ethernet, no afectada). El 5069-IF8 leyendo 4-20 mA con HART accesible en el lazo (el resistor de 250 ohms del datasheet permite el comunicador externo) cumple → **no se requiere hardware HART-capable adicional, sin impacto de costo/plazo.** **Condición:** cada instrumento debe ser 4-20mA+HART; un instrumento solo-4-20mA sin HART no cumpliría (precedente IFM VTV122 vigente). Consistente con el cierre positivo del TM N24, sin reabrir el over-reach del TM N21 OBS-01 (decisión: confirmar citando el cierre del N24, sin nombrar OBS-01 ni "retirada").

> **Forma y verificación.** Form RFI llenado round-trip (sección Replied Information del propio .docx; To=Billy Tan, From=Luis Rivera); original recibido respaldado (`..._ORIGINAL.docx.bak`). Workflow `rfi001-hart-verify` (4 verificadores adversariales + síntesis, **APROBADO 4/4 PASS, 0 correcciones obligatorias**): exacto contra la ET (HART = 1 mención; multiplexor/pass-through/asset-management = 0), fiel al cierre del TM N24, sin fugas internas (§N=0, sin Van Doorn, sin códigos OBS/Code), condición instrumento-a-instrumento preservada, limpio de fingerprints IA. Metadatos Word limpios. Archivos: `PROGRAMA y CONTRATO/RFI/RFI 1/` + correo de cobertura (Reply-To al thread del RFI) en `CORREOS/Junio 2026/2026-06-24/`. **Estado: ENVIADO 24-Jun-2026** (form RFI con la respuesta adjunto al correo de cobertura). Ver [[project_hart_precedente]].

### 2026-06-23 — Transmittal N24 (E53+E54, 5 docs I&C/eléctrico + CIP filter) — ENVIADO

> **TM N24 (P22-TM-09-000-024-0)** cubre **E53 (25007-0053:** IO List Rev 3, LCP Datasheet Rev 0, I&C Cable Schedule Rev 2, Data Transfer List Modbus Rev 2**)** + **E54 (25007-0054:** CIP Cartridge Filter Datasheet Rev E**)**. Veredicto **2 — Approved as Noted. Tally 3 Code 1 + 2 Code 2.** El **CIP Cartridge Filter Rev E cierra el Code 3 del TM N22** (gasket EPDM + statement de compatibilidad FRP). Cable Schedule y Modbus → Code 1. IO List Rev 3 y LCP Datasheet → Code 2.

> **Re-tono crítico del OBS-01 (IO List) — captura del usuario.** La versión inicial trataba "solo 2 de 4 señales de interfaz acordadas" como incumplimiento. Verificación del histórico (anti-invención): ADASA pidió formalmente **solo 2** señales (TM N3 OBS-04/05, reforzadas N7/N10, **cerradas en TM N19**), que BW Water entregó (XA005 enable, YA001 running); **falla y local/remoto son requisito NUEVO** (Excel de Ronald, E53). El OBS-01 se reescribió como **"NEW REQUEST"** (ADASA extiende la interfaz a 4 señales relay-contact; las 2 transmitidas están correctas; agregar fault status + local/remote status), el IO List bajó de Code 3 a **Code 2** y el TM de 3 a **2**. Validación interna (NO citada a BW Water, §3.7): la lógica de control P22-IT-06-008-101 (Van Doorn) confirma las 4 señales cableadas; hay un gap interno (la lógica define 4, solo se transmitieron 2) que el TM N24 cierra como pedido nuevo. Ver [[project_tm24_state]], [[project_senales_interfaz]].

> **LCP Datasheet Rev 0 Code 2:** enclosure SS316L/NEMA4X/IP66 reconfirma lo correcto (la contradicción del TM N20 vive en el Outline, no aquí); 2 menores a Rev 0 (declaración de potencia del panel + inconsistencia de código). **HART cerrado positivamente** (chequeo a pedido del usuario): la ET 5.5 pide que los **instrumentos** sean 4-20mA+HART (cumplido — la Oferta Rev1 tiene todos los transmisores 4-20mA+HART), NO decodificación HART central en el PLC; el hallazgo HART (arrastrado del TM N21) fue over-reach y se cerró en la Section 3, sin reabrir N21. Ver [[project_hart_precedente]]. **Section 3** arrastra Control Philosophy hijos (6º ciclo), Outline enclosure, Equipment Layout RO horizontal + Grounding/FAT-SAT/ITP.

> **Metodología:** workflow `tm24-review` (46 agentes: verificación adversarial de los comentarios de Ronald + 6 lentes disciplinarias + verificación de datos anti-alucinación + consulta de especialidad + síntesis). 2 CC_ADASA (IO List + LCP, ambos Code 2; los 3 Code 1 sin anotación). Master Register a N24 (`update_register_n24.py`; 43/23/13/0; backup `_pre-N24`). Correo de notificación a Eduardo Yamauchi `CORREOS/Junio 2026/2026-06-23/`. §N=0, anti-IA limpio. El transmittal incluye un **hipervínculo de descarga** de los CC_ADASA (Synology) en la sección Attachments, por el peso de los archivos. **Estado: ENVIADO 23-Jun-2026** (respaldo `correo enviado a bw waters.pdf` en la carpeta). **TM N23 enviado 18-Jun.**

### 2026-06-23 — ENTREGA 9 L&A (TT-010): cierre del set civil Rev 0 del paquete BL — verificación interna

> **La ENTREGA 9** (carta `067-032-032-COR-TT-010`, 22-Jun-2026) trae en **Rev 0** las 5 láminas civiles que faltaban tras la ENTREGA 8, más la re-emisión completa de la fosa: DWG-00-001-001 L1/L2 (Excavaciones), 002-003 L2/L3 (Fundación contenedor), 002-007 L2 (Fundación CIP), 002-004 L1 (Fosa). El dossier `Bases REV 0/5. OBRAS CIVILES (A2)/PLANOS/` queda **completo en Rev 0 (18/18 láminas)**. **Decisión del usuario: verificación interna, sin transmittal a L&A** (el ciclo del TdR ya se invocó en el TM N4; ADASA avanza la licitación en paralelo).

> **Revisión cruzada (workflow `review-civil-rev0-e9`, 5 revisores + verificación adversarial de 34 claims + síntesis; render PNG con PyMuPDF).** **Puntos rectores RESUELTOS:** el plano de Excavaciones Rev 0 cubre excavación de fundaciones + cota de plataforma + sello (cierra el punto rector del TM N3); N.T.N. acotado por zona; **fosa = TK-06-004** (cierra el tag arrastrado desde el TM N2); 002-003 LAM2 con detalle propio INS-1 (ya no duplica la LAM1). **Residuales menores (carry-forward, sin hallazgos nuevos):** nota de mejoramiento de suelo (ET-101) presente en las láminas de formas pero no repetida en las de armadura (002-003 L2/L3, 002-007 L2), que remiten a la matriz 002-001 (CF-1); anclaje de equipos de etapa posterior diferido a planos vendor (002-007 L1, CF-6). No bloquean la licitación.

> **Detección de calidad:** la versión de 002-004 LAM1 incorporada con la E8 era un *stub* de exportación (sin cajetín ni texto, solo figuras); se reemplazó por la E9 completa y se archivó la defectuosa. **Acciones sobre el paquete:** 6 láminas Rev 0 incorporadas a PLANOS; superadas (Rev C/B + stub E8) archivadas en `BORRADOR_REV0/_dossier_superseded_pre-E9/`; **LEEME e `00_INDICE` actualizados a "18/18 Rev 0"**. El **cuerpo del BL se actualizó a Rev 0** (decisión del usuario): el apartado de Antecedentes y las referencias del Anexo A2 declaran ahora los planos de obras civiles en revisión 0 y las ET civiles en revisión 1 (antes "última revisión disponible, en proceso de aprobación"). Regenerado con `md_to_adasa_docx.py` ([CHEQUEO LAYOUT] OK), TOC actualizado y exportado a PDF vía Word; **Word + PDF dejados en la carpeta 1** del paquete (respaldos `_pre-E9`).

> **Cubicación del Formato (A9) — cross-check, sin tocar cifras (a la espera de visto bueno):** la tabla de cubicaciones del plano de Excavaciones Rev 0 da ≈91 m³ de excavación geométrica (sin esponjamiento) y ≈38,7 m³ de relleno de trazado. La partida **4.8 (excavación 115,1 m³) queda consistente** con el plano aplicando el **20 % de esponjamiento** que el propio plano declara (91 × 1,20 ≈ 109; +5 %). La partida **4.9 (relleno 91,5 m³) queda a revisar**: el plano solo tabula relleno de trazado (≈38,7 m³); el resto sería backfill de fundaciones + base bajo losas que el plano no tabula. **El Formato no se modificó** (decisión pendiente). Ver memoria `project_entrega9_cierre_civil_rev0`; bitácora en `INGENIERIA DE DETALLE OOCC/REVISIONES/`.

### 2026-06-22 — Cross-check seguimiento semanal BW Water (Semana 22-Jun) + correo accountability minuta (Parte 1) — ENVIADO

> **Cronograma operativo vigente = `Project Schedule 08-06-26` (Rev A)** (reemplaza al baseline 05-Mar-2026 como plan de avance; 05-Mar queda solo como referencia de varianza contractual). Cross-check del paquete recibido el lunes 22-Jun (correo Yamauchi 10:45 + `Copy of Procurement tracking - BW Water 2206.xlsx` + `25007 TALTAL PROGRESS REPORT (WEEK 25).pdf` + `25007_Taltal_DDSR_2026.06.22.pdf`) contra el cronograma Rev A, la **minuta/Meeting Notes del 16-Jun** y la semana anterior. Validado con workflow `cross-check-bwwater-22jun` (62 agentes, 4 frentes + verificación adversarial; **56/57 hallazgos confirmados, 1 refutado, 12 corregidos**). Análisis: `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 22-06-26/CROSS-CHECK_ADASA_22-06-26.md`.

> **Veredicto: 6 focos CRITICAL · 13 WARNING · 2 OK. Determinante = Fedco.** (1) **Fedco completa 21-Ago** (Progress Report W25 + minuta 16-Jun) — 6 d **después** del EXW Penang 14-15 Ago del cronograma; tres fechas BW Water distintas para el mismo equipo (tracker EAP 05-Ago / Progress 21-Ago / Schedule 09-Ago); BH-09-001 en status D; anticipo 30% sin resolución escrita. (2) **Sísmico sin certificar + Stress & Flexibility no emitido** → RO Skid y pipe spools al 0% (vence 29-Jun). (3) **Compromisos de la minuta del lunes incumplidos:** spare parts quotes y ex-work shipment details no llegaron en el paquete. (4) Tres planos mecánicos de ruta de instalación Not submitted, vencen 26-Jun (Maintenance Lifting Points, 3D Model, GA RO HP Pump). (5) RO Pressure Vessel: tracker EAP 29-May obsoleto (~65 d off vs Penang 02-Ago). Tracker estático vs 15-Jun (solo Static Mixer recibido en Penang 16-Jun) y aún anclado al baseline 05-Mar.

> **Aprendizaje de la verificación adversarial:** el encuadre inicial de que el *cronograma* mostraba Fedco 21-Ago era falso (el cronograma Rev A muestra 9-Ago; el 21-Ago viene de minuta + Progress Report) — refutado por el verificador. Esto agrava el caso: ni el tracker ni el cronograma reflejan la fecha real del proveedor.

> **Se va por partes.** **Parte 1 — Correo de accountability** (inglés, Reply a `RE: 25007 Taltal: Meeting Notes`, To/CC del correo 17-Jun): reclama lo que BW Water comprometió en la minuta del 16-Jun y no llegó — **spare parts quotes** + **ex-work shipment details** (este ligado al RO PV ex-works España 23-Jun + Shipping Plan Not submitted) + **invoice/payment status update** (estado de pago) — y exige lo pendiente del reporte semanal (fabrication schedule con fechas; columna material-received en el Project Schedule), acusando lo ya cumplido (registros fotográficos + super duplex). Tono firme profesional; pide explicación por escrito + fecha firme por ítem ante la reunión semanal. Archivos: `CORREOS/Junio 2026/2026-06-22/` (`crear_correo_seguimiento_minuta_22jun.py` + `2026-06-22_Monday-Commitments-Follow-up.docx` + `.md` cuerpo + `_Descripcion.md`). **Reemplaza** al correo amplio de procurement (`2026-06-22_Procurement-Review.*`, eliminado). Cuerpo pasado por skill `anti-ia revisar` antes del Word (AMARILLO → **VERDE**: em dash, oración larga, antítesis suave y repetición corregidas). **Estado: ENVIADO 22-Jun-2026** (respaldo `correo enviado a BW WATER.pdf` en la carpeta).

> **Diferido a otras partes / memoria:** **Fedco** (completion 21-Ago posterior al EXW Penang; queda en seguimiento, ver [[project_fedco_fat_conflict_14may]] y [[project-procurement-22jun]]); sísmico (fecha PE-certificada + alcance liberable + izaje); fechas comprometidas de GA filtros / Main Control Panel / electrical package; invoices. El detalle completo de la semana (6 CRITICAL/13 WARNING/2 OK) vive en `CROSS-CHECK_ADASA_22-06-26.md` como respaldo. Ver [[project-procurement-22jun]].

### 2026-06-18 — Transmittal N23 (E51+E52, 7 docs) — ENVIADO (versión ejecutiva)

> **TM N23 (P22-TM-09-000-023-0)** cubre **E51 (25007-0051, 16-Jun — paquete QA/fabricación)** + **E52 (25007-0052, 18-Jun)**. Veredicto **3 — To Be Revised. Tally 0 Code 1 + 1 Code 2 + 6 Code 3.** **Driver: RO Vessel Hydrostatic Test Procedure Rev A (CRITICAL)** — el cuerpo no fija la presión de prueba vinculante (solo la regla genérica 1.1× ASME / 1.43× CE) y el formulario Protec embebido trae **45,5 bar (~660 psi)** contra los **1.980 psi (1.800×1,1)** que exigen el ITP y el waiver ASME; el testigo y el dossier que se negociaron a cambio de la estampa quedan sobre una cifra a ~1/3. **Lo positivo: el ITP Rev C cierra materialmente** el ítem de fabricación más antiguo del proyecto (TM N19 Section 2.10 / TM N22 Section 3) — ya carga los 3 elementos del waiver (1.800 psi×1,1 en la fila 2.2, witness ADASA, dossier en Hold Points 7.6/8.3); cierre total sujeto a 2 ediciones Rev 0 (declarar la base sin estampa; subir el ensayo del vessel de Witness→Hold Point) + corregir el procedimiento 009.

> **Veredictos por documento:** ITP Rev C (P22-BA-09-000-004) **Code 2** (cierra materialmente el carry-forward); RO Vessel Hydrostatic Test Procedure Rev A (-009) **Code 3** (CRITICAL presión); HP & LP Pressure Test Procedure Rev A (-010) **Code 3** (sin presión vinculante; diseño HP 90 vs 120 bar sin reconciliar); NDE Plan Rev B (-005) **Code 3** (ediciones de código como marcadores, repite gap de Rev A); Painting Procedure Rev A (-011) **Code 3** (sistema Jotun sustituye al Sherwin-Williams aprobado Code 1 en TM N11 sin equivalencia; C5-M marino no acreditada); Instrument Location Layout Rev C (P22-DWG-09-008-001) **Code 3** (Rev C reusada con cambios sin subir letra; geometría atada a Equipment Layout Rev B, hoy en Code 3); UHPRO Structural Design Criteria Rev A (P22-CD-09-005-003) **Code 3** (falta el caso de carga/criterio de **izaje** que exige la ET — driver; + cita sísmica a alinear a **NCh 2369 Of.2003**).

> **Calibraciones del usuario (clave):** (1) tipo de documento nuevo **`BA`** (calidad/fabricación: ITP, NDE, procedimientos de prueba, pintura). (2) Un **procedimiento de prueba sin su presión vinculante = Code 3**; un datasheet/lista/procedimiento correcto en contenido = Code 1 (certs al dossier). (3) **Norma sísmica = NCh 2369 Of.2003, NO la 2025**: aunque la 2025 ya está oficializada (9-Mar-2026), la ingeniería se contrató y vencía (9-Dic-2025) bajo Of.2003, antes de la oficialización → el proyecto se mantiene en Of.2003; el OBS-01 solo corrige el "NCh2369:2009" inexistente a Of.2003 (ver [[project-nch2369-2025-timing]]). (4) **Izaje:** la ET exige memoria de cálculo + plano de izaje + diseño del yugo (entregables #72/#76 en el register); **alcance del yugo = solo DISEÑO de BW Water**, la grúa y los equipos de izamiento son de ADASA (ET §5.6). (5) Combinaciones **ASD que gobiernan = NCh 2369 §4.5** (no las genéricas de NCh 3171).

> **Paquete:** `.md` fuente + `crear_transmittal.py` + Word/PDF (**11 pág, versión ejecutiva**: Section 1 = un párrafo introductorio, sin tabla de disposición; Section 2 lean) en `REVISIONES/TRANSMITTALES/P22-TM-09-000-023-0/`; **7 CC_ADASA** (6 Code 3 + 1 Code 2; sin Code 1 este ciclo) en `COMENTARIOS/` (el plano Instrument Location Layout verificado por render PNG). **Master Register** actualizado a N23 con script explícito `update_register_n23.py` (el `update_register.py` viejo es frágil: parsea veredicto case-sensitive con guion y no agrega filas) — 103 ítems / 79 delivered / verdicts 40-23-16; backup `_pre-N23.xlsx`. Correo de cobertura ejecutivo (carry-forward neutral) en `CORREOS/Junio 2026/2026-06-18/`. **QA:** workflow a medida `tm23-review` (5 lentes: ITP/waiver-ASME, NDE/pruebas, pintura, instrumentación, estructuras → verificación adversarial → síntesis), **anti-ia VERDE** (Checklist B; se redujeron los em-dash de prosa, conservando los de encabezado/etiqueta/código), §N=0, IDs 1:1 con CC_ADASA. Respaldo de la versión densa en `..._TRANSMITTAL_detailed.bak.md`.

> **Estado: ENVIADO 18-Jun-2026.** Carry-forward vivo (al cierre del TM N23): Control Philosophy hijos (6º ciclo), PLC-LCP Outline Rev B (enclosure), Equipment Layout RO horizontal (gatea el Instrument Layout), **Grounding Rev F vencido 17-Jun** (no llegó en E51/E52), **tabla FAT/SAT vencida 15-Jun**. Ver [[project-tm23-state]], [[transmittals]].

### 2026-06-18 — Cierre de la actualización del paquete BL Montaje: dados de soportes a piso, chequeo de layout del conversor (v7.7), memorias fuera del paquete

> **Formato (A9) — dados de soportes a piso.** Tras el descope de la cubierta, se reclasificaron los soportes de cañería: **solo los que tienen detalle de placa base cuadrada en planta van a piso** (llevan dado/pedestal de hormigón); el resto va a muro (ménsula) o suelda a soporte existente. Nueva **partida 4.7 "Dados de hormigón G25 para pedestales de soportes a piso"** = **17 dados** (placa de acero 200×200 sobre dado/pollo 350×350×100 mm; SP-04/05/06/07/08/09/11 del cuadernillo) cotizada por unidad × $40.000 = $0,68M; el anclaje químico de la placa queda en el montaje del soporte (Cap. 1). La partida 4.4 (bomba) pasó de "según MC ACI 351" a **"según ACI 351"** (las memorias de cálculo de OOCC no van al paquete). **Cap. 4 = 14 sub-ítems (4.1-4.14) ≈ $32,5M; COSTO DIRECTO ≈ $105,8M; TOTAL GENERAL ≈ $137,5M (sin IVA).**

> **Conversor template-adasa v7.7 — chequeo de layout incorporado.** Las dos correcciones que se iteraban a mano en el BL (figuras que dejaban páginas a medias; códigos `P22-DWG-…` que se partían en vertical) quedaron automatizadas en `md_to_adasa_docx.py`: **encuadre de figuras** en `FIGURA_MAX_W × FIGURA_MAX_H` (5.2"×5.8") pasando solo la dimensión limitante a `add_picture`, y **token-floor de anchos de columna** que ensancha solo las columnas con códigos largos. Al guardar emite `[CHEQUEO LAYOUT] OK`/advertencias (respaldo visual: `revisor-docx`). Skill subida a **v7.7** (SKILL/CHANGELOG), CLAUDE.md global §4 + proyecto §3/§4.1 actualizados, y **sincronizado a los otros equipos** vía `claude-memory`.

> **Memorias de cálculo fuera del paquete** (decisión del mandante; ver también la entrada del refresh E7): la carpeta MEMORIAS se retiró del dossier `5. OBRAS CIVILES (A2)` → queda **PLANOS 18 + ET 2**; las MC Rev 2 se conservan en `BORRADOR_REV0/_memorias_excluidas_del_paquete/`; el BL/`00_INDICE`/`LEEME` ya no las mencionan. Se mantienen las citas a memorias de **equipos** (Exfibro EX-26005-F01, manual KSB) y a **normas** (ACI 351/318), que no son las MC del dossier civil.

### 2026-06-18 — Refresh del dossier de Obras Civiles del paquete con la ENTREGA 7 de L&A

> **Contexto:** L&A entregó la **ENTREGA 7** (transmittal `067-032-032-COR-TT-008`, 17-06-2026, 24 docs, status "Revisión Cliente") con revisiones nuevas de la ingeniería OOCC. Se refrescó el dossier `Bases REV 0/5. OBRAS CIVILES (A2)/` con esas versiones, manteniendo el descope del cobertizo.

> **Dossier actualizado** (archivos superados archivados en `BORRADOR_REV0/_dossier_superseded_pre-E7/`): **PLANOS 17→18 láminas** (001-001 B→C; 002-001/002/003/004/006/007 a Rev D solo en las láminas entregadas; **002-006 L3 nueva**; las láminas no actualizadas por E7 quedan en Rev C/B, p.ej. 002-007 L3 Rev C que tiene la fundación del cobertizo); **ET** 101/102 Rev 0→**1**. Las **memorias de cálculo (MC) NO forman parte del paquete** (decisión del mandante; la carpeta MEMORIAS se retiró del dossier y las MC Rev 2 de E7 se conservan en `BORRADOR_REV0/_memorias_excluidas_del_paquete/`). La cubierta (003-001, MC-003-001 R2, ET-103 R1) está en E7 pero **sigue excluida** (descope vigente).

> **BL actualizado:** se **retiró el plano fantasma `P22-DWG-00-002-005`** (E7 confirma que nunca se emite; los detalles de anclaje viven en los planos de fundaciones 002-002/003/007) de sus 5 referencias (§3.4, §6.1 tabla, §6.4, §6.6, Anexo A2), reapuntadas a los planos de fundaciones; se corrigió la descripción de 002-006 L3 (detalle típico de cámaras prefabricadas). Docx/PDF regenerados (conversor v7.7, `[CHEQUEO LAYOUT] OK`) y copiados al paquete. `LEEME`/`00_INDICE` actualizados.

> **Decisiones / pendientes:** (1) **no se re-cubicó el Formato** contra los itemizados E7 (Rev D / Estimación Rev 0, en revisión cliente) — tarea separada. (2) El plano de la fosa sigue rotulado **TK-06-002** (error de L&A; el BL usa TK-06-004) — lo resuelve la revisión OOCC (TM N4). (3) La revisión técnica formal de E7 (qué cambió en cada Rev D) es el **TM OOCC N4**, no este refresh del paquete.

### 2026-06-18 — BL Montaje Rev 0: descope de la cubierta metálica (cobertizo) CIP, manteniendo su fundación

> **Cambio de alcance.** En esta oportunidad **NO se construye la cubierta metálica (cobertizo) del sistema CIP**, pero **SÍ su fundación**. La estructura metálica (perfiles ASTM A36, panel PV-6, pintura C5-M) se difiere a una etapa posterior (suministro e instalación ADASA), igual que el patrón de los equipos CIP. La fundación se cuela ahora completa con sus **24 pernos de anclaje F-1554 3/4" preinstalados (colados)** + **protección anticorrosiva interina** (caps/grasa o galvanizado/SS), para erigir la estructura después. Se mantiene **Rev 0 (edición en sitio)**; la BL sigue en borrador, no distribuida.

> **BL `.md`** (`BORRADOR_REV0/BL_MONTAJE_TALTAL_REV0.md`, fuente única): reescritas las Secciones de alcance global, alcance civil, suministros del contratista, alcance excluido (§4.2 corrige la contradicción que listaba la cubierta "dentro del alcance"), especificaciones civiles y programa, para reencuadrar la cubierta como "fundación en alcance, superestructura etapa posterior". La tabla de pintura **C5-M se relocalizó** a una subsección propia de protección anticorrosiva del acero estructural expuesto (la usan los soportes SP-01..11, que siguen en alcance); §6.8 pasó de "Cubierta metálica" a "Fundación de la cubierta metálica". Docx/PDF regenerados con el conversor `md_to_adasa_docx.py` (export PDF vía Word COM con `win32com.dynamic`; el COM por PowerShell falló con `TYPE_E_ELEMENTNOTFOUND` por caché de interop de Office) y copiados al paquete.

> **Formato de Presupuesto (A9)** (`generar_formato_presupuesto.py`): se **eliminó la partida 4.10 "Cubierta metálica" (1.668,42 kg @ $5.290/kg ≈ $8,83 M)** — el "fierro" descopado — y se **partió la fundación CIP 4.2 (9,74 m³)** en **4.2 losa CIP (7,36 m³)** + **4.3 fundación de la cubierta (2,38 m³, con los pernos F-1554 colados + protección interina)**, al mismo P.UNI. (split total-neutral). Cap. 4 queda en 13 ítems (4.1-4.13) renumerados. **COSTO DIRECTO $105,11 M → TOTAL GENERAL $136,64 M** (baja exactamente los $8,83 M del acero retirado; el resto intacto). Backup `Formato de Presupuesto_BACKUP_pre-descope-cubierta.xlsx`; xlsx copiado a `Bases REV 0/2. FORMATO DE LICITACION (A9)/`.

> **Dossier `Bases REV 0/5. OBRAS CIVILES (A2)`:** se retiraron los 4 documentos del "fierro" (verificado por extracción de título con PyMuPDF) a `BORRADOR_REV0/_cubierta_excluida_del_paquete/`: **P22-DWG-00-003-001 LAM1+LAM2** (estructura metálica cobertizo), **P22-MC-00-003-001** (MC estructural), **P22-ET-00-010-103** (ET estructura metálica). **La fundación se mantiene** en `P22-DWG-00-002-007 LAM3` ("FUNDACIÓN COBERTIZO - FORMAS - ARMADURAS - DETALLE PERNO PA-1", confirmado). Conteos: PLANOS 19→17, MEMORIAS 5→4, ET 3→2. Índice `00_INDICE` y `LEEME` del dossier actualizados.

> **Hallazgo flagueado `[Probable]`:** el dossier **no** trae `P22-DWG-00-002-005` (que el BL cita como "detalles de anclaje y conexiones"); el LEEME documenta que ese plano "aún no emitido" y que los puntos de anclaje están entretanto en los planos de fundaciones (`002-007`). Se mantuvo `002-005` como forward-reference (intención original del BL) y se **añadió `002-007` al manifiesto de planos** como hogar de la fundación del cobertizo. Pendiente: confirmar con el consultor si `002-005` y `002-007` son planos distintos o el mismo renumerado.

### 2026-06-15 — Transmittal N22 (E49+E50, 7 docs) — ENVIADO

> **TM N22 (P22-TM-09-000-022-0)** cubre los submittals **25007-0049 (E49, 6 docs)** + **25007-0050 (E50, HMI)**. Veredicto **3 — To Be Revised. Tally 2 Code 1 + 1 Code 2 + 4 Code 3.** El driver global es la **Plant Control Philosophy Rev D**: la lógica operativa numérica (Controls & Sequence Chart P22-LI-09-008-017 + Alarm & Control Setpoint List P22-LI-09-008-015 + Control Matrix) sigue en documentos hijos no entregados con la filosofía — **6º ciclo** del family con esa lógica fuera del paquete. Lo positivo del ciclo: **el permissive CRITICAL del HP Pump quedó CERRADO** (VE-09-007 una sola vez, VE-09-014 fuera del lazo de arranque; la reserva C-4300 en ese punto queda satisfecha), la fórmula de salt-rejection se corrigió a conductividad de alimentación (CIT-09-001B), el SEC se declaró 4.71 kWh/m³ y el protocolo 4-20mA+HART quedó confirmado en el cuerpo.

> **Veredictos por documento:** Equipment Layout Rev C **Code 3** — el **RO Cartridge Filter (ítem 2) sigue dibujado horizontal** pese a que su Datasheet Rev E ya lo declara vertical (cambio H→V de la NT-001 5.C); el CIP filter (ítem 11) sí está vertical. *Calibración del usuario:* el Equipment Layout NO se revisa contra el requisito de puertas del contenedor (eso es del plano del container) sino contra la orientación de los vessels de filtro. CIP Cartridge Filter Rev D **Code 3** (gasket/FRP sin documentar para CIP pH 2-12; el default nitrilo es inadecuado; TM N19 OBS-03 sin cerrar). HMI Display Screenshot Rev A **Code 3** (entrega real de pantallas que **cierra materialmente TM N4 NOTE-05** — el compromiso abierto más antiguo del proyecto, ~127d — pero el set está incompleto: faltan pantalla de variables eléctricas/CEE kWh/m³, tendencias, setpoints y varias zonas de proceso). Static Mixer Rev C **Code 2** (TAG MZE-09-001 reconciliado; reconciliación página-a-página a Rev 0). **RO Cartridge Filter Rev E y Utility Consumption List Rev C → Code 1** *(calibración del usuario: el datasheet/lista correcto en su contenido es Code 1; el certificado de material FRP va con el dossier de fabricación del vessel y la representación de carga A/C es nota — no degradan a Code 2)*.

> **Paquete:** `.md` fuente único + `crear_transmittal.py` + Word/PDF (13 pág, **versión ejecutiva**) en `REVISIONES/TRANSMITTALES/P22-TM-09-000-022-0/`; **5 CC_ADASA** (4 Code 3 + 1 Code 2; los 2 Code 1 sin anotación) en `COMENTARIOS/` (plano rotado 270° verificado por render PNG; el CC_ADASA del HMI se corrigió para **distribuir las 5 OBS una por página** — caían todas en el índice porque `search` halla el título de sección en la TOC primero, resuelto con `page_min`). Master Register `-002-0` actualizado a N22 (Master Register + Summary headline: Delivered 75 / Transmittals 22 / Deliveries 50-E50 / Verdict dist 40-23-12 + Revision History +7 filas; 4 hojas preservadas). **Correo de remisión ejecutivo corto (~120 palabras, sin detalle por documento)** en `CORREOS/Junio 2026/2026-06-15/` (`crear_correo_tm22.py` + `.docx`/`.pdf`). **Método:** workflow a medida `tm22-review-e49-e50` (42 agentes: revisión por documento → verificación adversarial → síntesis) + calibración del usuario documento por documento. QA: §N=0, escaneo anti-IA sin frases-firma (repetición estructural propia del formato), render PNG del plano.

> **Refinaciones de redacción del ciclo (15-Jun):** (1) Sumario §1 y comentarios de estado §2 reescritos a **versión ejecutiva** (verdict en una línea + viñetas de una cláusula; un párrafo "Status" breve por documento — el detalle queda en la tabla OBS y el bloque Action). (2) **Section 3 reducida a los 3 carry-forward más graves** (ITP/vessel, PLC-LCP Outline enclosure, cascada de control); el resto (incl. Datasheet PLC/HMI Rev B HART) se rastrea en el Master Register. (3) **Encuadre ASME corregido**: la estampa ASME ya está **waived/aceptada** (correo 02-Jun + schedule Rev A adoptado 09-Jun); el transmittal ya NO la lista como abierta — lo abierto es el ITP Rev C documentando la base acordada (hidrostática 1.800 psi×1,1, dossier, testigo). (4) Correo de cobertura acortado a ejecutivo. **Pendientes vivos (full inventory interno):** Control Philosophy Rev E con los 3 hijos, Datasheet PLC/HMI Rev C (HART), PLC-LCP Outline Rev B (enclosure), ITP Rev C (evidencia de prueba del vessel), y la cascada de control (I/O List, IC Cable Schedule, Alarm & Interlock List, Schematic) ya destrabada del gate "esperando Rev D". **Estado: ENVIADO 15-Jun-2026** (respaldo `Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf` en `CORREOS/Junio 2026/2026-06-15/`).

### 2026-06-15 — Formato de Presupuesto (A9): Capítulo 4 Obras Civiles valorizado a mercado norte + premium Taltal

> **Se poblaron los P.UNI. del Cap. 4** (estaban vacíos) del `Formato de Presupuesto.xlsx` del paquete "Bases REV 0". Las **cantidades de L&A cuadran 1:1** con el Formato, pero sus **precios unitarios están inflados ~5–9× en el material** (hormigón, tierra y acero) — validado con dos deep-research + búsquedas dirigidas (MINVU DS-27, CYPE Generador de Precios, ONDAC; verificación adversarial incompleta por throttling → `[Probable]`). Los P.UNI. se anclan a **mercado del norte de Chile con premium logístico de Taltal, NO al APU del consultor** (UF 40.765,97).

**Criterios de precio (decisiones del usuario vía AskUserQuestion):** **4.1–4.5 fundaciones** = costo directo CIV de L&A **× 0,60** (G25 colocado L&A $762k/m³ vs ~$350–450k realista aun con premium Taltal); **4.6 excavación $22.000/m³ + 4.7 relleno $45.000/m³** (opción "premium remoto"; L&A 4–26× alto por asumir métodos 100% manuales + tarifa 0,43 UF/HH ≈ $17.500/HH); **acero = una sola partida all-in por kg** — **4.10 cubierta CIP $5.290/kg** (suministro+fab $2.200 + traslado $300 + pintado marino **C5-M ISO 12944** $563 + montaje/erección Taltal $2.000 + panel PV-6 prorrateado $227; CANT 1.668,42 kg) y **4.11 insertos RO $3.000/kg** (embebido, sin erección ni C5-M). El montaje no debe quedar implícito (el factor ×0,30 inicial lo dejaba en ~$923/kg, bajo el mercado de erección $1.000–1.500/kg).

**3 gaps cerrados (L&A los dibujó/exigía pero no los costeó en la Estimación — mismo patrón del TM N3):** **6 cámaras de inspección prefabricadas** + radier G25 0,576 m³ (plano P22-DWG-00-002-006_B, ítem 4.9); **esquema de pintura marina C5-M** (ISO 12944; plegado en el $/kg de 4.10); **impermeabilización** de la fosa TK-06-004 (químico-resistente, salmuera) + hormigón enterrado de fundaciones (4.12/4.13). **Panel PV-6 corregido a 25,2 m²** (CUADRO DE MATERIALES del plano P22-DWG-00-003-001_C; la hoja BASE lo había inflado 4,7× a 118 m²).

**Resultado:** Cap. 4 = **13 sub-ítems, $40,62 M**; COSTO DIRECTO **$113,93 M**; **TOTAL GENERAL ≈ $148,12 M** (vs ~$227 M con el APU crudo de L&A; repricing + cierre de gaps ≈ −$79 M). Partidas 4.8 (drenaje red), 4.12/4.13 (impermeabilización) quedan referenciales `[Suposición]` a afinar contra la Rev 0 OOCC. **Reconciliación del generador:** el `.xlsx` estaba editado a mano y el script `generar_formato_presupuesto.py` quedaba desincronizado (lo dejaría en ceros); se reconcilió como **fuente única** y ambas copias (BORRADOR_REV0 + Bases REV 0) quedan **idénticas (0 diffs)**, con Cap. 1-3 intactos. Backup `Formato de Presupuesto_BACKUP_pre-precios-OOCC.xlsx`. **Hallazgo transversal relevante para el TM N4** (revisión formal de la Estimación de Inversión): el APU de L&A infla el material ~5–9× en las tres familias y omite partidas de su propia ingeniería. Detalle en memorias `project_formato_presupuesto_bl` y `project_entrega6_estimacion_inversion`.

### 2026-06-10 — Transmittal N20 (E46+E47, 20 docs) + respuesta panel drawings PLC-LCP — AMBOS CORREOS ENVIADOS

> **Contexto de urgencia:** Eduardo Yamauchi (Mié 10-Jun 9:52) pidió aprobación expedita de los 2 planos de panel PLC-LCP del submittal 25007-0046 (fabricación enclosure ~6 semanas + integración + shipping a Penang) ofreciendo revisión por correo o reunión corta sobre material/dimensiones/diseño.

**TM N20 (P22-TM-09-000-020-0)** generado el mismo día consolidando E46 (28-May, respuesta vencida 31-May) + E47 (09-Jun, respuesta pedida 12-Jun): 20 documentos, veredicto 3 — To Be Revised, 8 Code 1 + 7 Code 2 + 5 Code 3 (detalle en la tabla de la Sección 4, fila 20). Hallazgo central del paquete panel (revisión visual de planos): el **Panel Specification Sheet del Outline Rev A declara SHEET STEEL pintado RAL 7035 + IP55 + ventilación forzada + peso TBD**, contradiciendo el LCP Datasheet Rev B del mismo submittal (nVent FS66S, **SS316L sin pintar, NEMA 4X/IP66**, ambiente altamente corrosivo), el SLD Rev 0 IFC ("METAL CLAD, NEMA4X/IP66" en nube de revisión, verificado visual) y la ET. Reversión contractual materializada: I/O List Rev 2 vuelve a Code 3 porque la Plant Control Philosophy Rev D no llegó en la ventana de 14 días del TM N19 (venció 08-Jun; 4º ciclo consecutivo).

**Dos correos ENVIADOS 10-Jun-2026 desde `CORREOS/Junio 2026/2026-06-10/`** (cadenas separadas por instrumento, mismo día, cross-references mutuas): (1) `2026-06-10_Transmittal-N20.docx` — notificación TM cadena regular con el transmittal + 12 CC_ADASA adjuntos, drivers + cierres (paquete eléctrico IFC completo aceptado); (2) `2026-06-10_Panel-Drawings-Reply.docx` — Reply-To al thread de Yamauchi: ADASA acepta la vía email-review, identifica la única decisión que bloquea fabricación (material/IP del enclosure) y ofrece **ruta expedita**: confirmación escrita del enclosure del datasheet + Outline Rev B alineado ⇒ release de fabricación contra Rev B sin nuevo ciclo. Master Register actualizado a N19+N20 (99 ítems). Pendiente: respaldo PDF/.msg de ambos envíos en la carpeta. **Próximos hitos que quedan corriendo:** confirmación escrita enclosure + Outline Rev B (fabricación panel), Rev D Control Philosophy (remedies C-4300 vigentes), Grounding Rev F Mié 17-Jun, tabla FAT/SAT + pendientes NT-001 Lu 15-Jun.

### 2026-06-09 — Project Schedule Rev A (08-Jun) recibido: análisis + respuesta ADASA (baseline con reservas) — ENVIADO

> **La escalación del 08-Jun funcionó:** BW Water entregó el **Project Schedule 08-06-26 Rev A** (`PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/Project Schedule 08-06-26.pdf`; P22-BA-09-000-001, aprobado EY) el mismo día. Extracción citable: `Project Schedule 08-06-26_extracted.md`.

**El punto que ADASA forzó quedó respondido (confirma la sospecha):** RO pressure vessels terminan **ex-works España 23-Jun** (ID 300 Manufacturing), con línea separada de **40 días de mar España→Penang** (ID 301, llegada **02-Ago**), montaje en contenedor 03-05 Ago (ID 376), **EXW Penang 15-Ago** (ID 385), fin de proyecto **19-Nov** (Performance Test). Slip ~+12 d en EXW vs. baseline 05-Mar (03-Ago); ≈ Recovery 22-May (16-Ago, −1 d); dentro de tolerancia Cl.27. El waiver hace su trabajo: la ruta sin estampa (ex-works 23-Jun) es lo que sostiene el 15-Ago (con estampa serían ~+6 sem).

**Verificación ASME (instrucción del usuario):** (1) el schedule **NO menciona ASME/estampa/certificación** en ninguna de las 6 páginas — la ruta sin estampa es solo implícita; (2) **no hay tarea de prueba hidrostática/presión de los vessels** (ni España ni Penang), solo el FAT de sistema (24-Jul→13-Ago) y el Performance Test final. Corrección de premisa: el 23-Jun es fábrica en España, **no** tubos en Penang (eso es 02-Ago; montaje/pruebas en Penang son de inicios de agosto). Implicación: nada en Rev A documenta el waiver ni la base de pruebas → debe ir al **ITP actualizado** con la hidrostática de fábrica a rating (1800 psi × 1,1) + dossier + derecho de testigo en Protec.

**Correo respuesta (postura: aceptar con reservas).** `CORREOS/Junio 2026/2026-06-09/` (`crear_correo_schedule_revA_acceptance.py`, `2026-06-09_Recovery-Schedule-RevA-Acceptance-with-Reservations.docx`, `_Descripcion.md`). Inglés, Reply-To al thread del Mitigation Plan, `Document()` directo con viñetas nativas. Adopta Rev A como baseline de recuperación trazable y pide formalizarlo en el tracker semanal (NT-001 4.C); registra la base sin estampa→ITP+hidrostática+testigo; y deja abiertas, condicionando FAT/despacho/EP-2: 25 aclaraciones de la NT-001, tabla FAT/SAT + dry-test del 15-Jun, confirmación firmada de Fedco (ventana ~6 d a EXW, ~2 d de running test), y filtro RO SS316 (justificación + datasheet, aprobación antes de PO). **CC:** Andrew Sia + los 7 del thread.

**Verificación:** barrido §N = 0; anti-ia revisar VERDE (corregido el contraste "X, not Y" de la apertura; em dash solo en firma; idioma 100% inglés).

**Estado:** **ENVIADO 09-Jun-2026** (versión ejecutiva: 1 párrafo de adopción + 5 viñetas, punto ASME primero). Pendiente menor: respaldo (PDF/.msg) en la carpeta. **Próximo hito:** reunión semanal Ma 09-Jun (revisar Rev A) + entregables del 15-Jun (tabla FAT/SAT, dry-test, ITP).

### 2026-06-08 — Escalación: Recovery Schedule vencido (3er requerimiento) — ENVIADO (BW Water respondió mismo día)

> El **Recovery Schedule** (deliverable de BW Water; ADASA lo revisa, no lo produce) sigue sin llegar: pedido para la reunión semanal del Ma 02-Jun, re-pedido el 04-Jun, ausente al lunes 08-Jun. ADASA escala con un tercer requerimiento del mismo thread del Mitigation Plan (`RE: 25007 Taltal - Mitigation Plan - Pressure Vessel Protec`, Reply-To del 01/02/04-Jun).

**Jugada — palanca que el 04-Jun dejó implícita:** se hace explícito que la **condición #1 ("Availability") del waiver ASME del 02-Jun** es justamente este schedule, construido sobre la fecha sin estampa del **22-Jun** y con la declaración **ex-works España vs Penang + tránsito**. Mientras no llegue, la condición #1 está incumplida y **el waiver no queda consolidado**; la condición #3 sólo renuncia al Change Order "provided the time saved reaches the schedule", de modo que sin el schedule no hay forma de verificar que el tiempo ahorrado por la concesión llega al programa. Se reafirma por referencia, sin re-abrir ni re-listar las tres condiciones.

**Deadline firme anclado:** se exige el schedule **antes de la reunión semanal de mañana, Ma 09-Jun**, para revisarlo ahí (la cadencia de la reunión es los martes; la del 02-Jun fue la del ciclo anterior).

**Pie contractual (por referencia, sin re-argumentar):** plazo firme y atrasos de sub-proveedor recuperables a costa de BW Water (BAE Cl.27/35/46), pagos por hitos (Cl.31). El correo deja claro que no reabre nada de eso; sólo exige el schedule ya vencido.

**Archivos:** `CORREOS/Junio 2026/2026-06-08/` (`crear_correo_recovery_schedule_escalation.py`, `2026-06-08_Recovery-Schedule-Escalation.docx`, `_Descripcion.md` con sección "Contexto Interno (No enviar)"). Inglés, Reply-To al thread, `Document()` directo (sin template ADASA, sin tablas, ~185 palabras). **CC ampliado:** los 7 del 04-Jun (Adzlan Bin Abd Rahim, Jeryl Regulacion, Sadeep Irugalbandara, Nick Huta, Stephane Gehant, Shane Banks, Victor Gutiérrez) + **Andrew Sia** (PMO secundario) como señal de escalación.

**Verificación:** barrido §N = 0; anti-ia revisar VERDE (0 fingerprints críticos; em dash solo en la firma; oración más larga ~37 palabras, bajo el umbral de alerta); idioma 100% inglés.

**Estado:** **ENVIADO 08-Jun.** La escalación funcionó: **BW Water respondió el mismo día con el Project Schedule Rev A (08-Jun)** → análisis + respuesta ADASA en la entrada del 09-Jun (arriba). Pendiente menor: marcar `.md` a ENVIADO + respaldo en la carpeta.

### 2026-06-04 — Follow-up: Recovery Schedule vencido + confirmación waiver ASME — ENVIADO (Jue 04-Jun 17:57)

> El **Recovery Schedule actualizado vencía hoy (04-Jun)** y es deliverable de BW Water (ADASA lo revisa, no lo produce). No llegó → ADASA emite un correo de seguimiento que lo persigue y, en el mismo mensaje, cierra el loop del waiver ASME enviado el 02-Jun. Mismo thread del Mitigation Plan (`RE: 25007 Taltal - Mitigation Plan`, Reply-To del 01/02-Jun).

**Jugada:** el reclamo del schedule se ancla a la lógica del propio waiver — ADASA renunció a la estampa ASME precisamente para recuperar ~6 semanas, así que el schedule debe construirse sobre la fecha sin estampa del **22-Jun** y declarar si 22-Jun es **ex-works España o entregado en Penang + tránsito** (sin esa declaración, ADASA quedaría atrapada en una fecha que no se cumple; el Recovery Schedule del 22-May tiene una línea separada de 40 días de transporte a Penang). El schedule pendiente se vuelve así la ejecución natural de la concesión.

**Parte ASME:** se **confirma recepción y se reafirma** la posición del 02-Jun **sin re-abrir** las tres condiciones. La frase "on the terms set out in that message" las reafirma sin re-listarlas; re-presentar la alternativa (versión sin estampa + dossier de pruebas) como nueva sería redundante con el 02-Jun y se leería como waiver incondicional, diluyendo el framing condicionado que protege a ADASA. Se pide a Eduardo confirmar recibo y que el recovery schedule + el ITP actualizado reflejen el waiver.

**Archivos:** `CORREOS/Junio 2026/2026-06-04/` (`crear_correo_recovery_schedule_followup.py`, `2026-06-04_Recovery-Schedule-Request-and-ASME-Confirmation.docx`, `_Descripcion.md` con sección "Contexto Interno (No enviar)"). Inglés, Reply-To al thread, `Document()` directo (sin template ADASA, sin tablas, ~140 palabras). CC: lista canónica de 19 del 02-Jun.

**Verificación:** barrido §N = 0; anti-ia revisar VERDE (sin fingerprints críticos; U-10 em dash solo en firma; U-03 borderline de 41 palabras aceptable en registro técnico-contractual); idioma 100% inglés.

**Estado:** **ENVIADO — Jue 04-Jun-2026 17:57.** Notas de registro: el asunto efectivo del hilo llevó el sufijo "- Pressure Vessel Protec" (el `.md`/script decían solo "RE: 25007 Taltal - Mitigation Plan"); el CC efectivo se acotó a 7 nombres, no la lista de ~19 del script. Sin respuesta de BW Water → escalación del 08-Jun (ver entrada arriba). Pendiente menor: dejar respaldo (screenshot/.msg) en la carpeta.

### 2026-06-03 — Respuesta ADASA a la contra-pregunta de BW Water sobre el Grounding Layout Rev E (TM N19) — ENVIADO

> **BW Water (Billy Tan, EIC), vía Eduardo Yamauchi (Ma 02-Jun 23:05)**, pidió aclaraciones sobre los comentarios de ADASA al plano **Grounding & Power Panel Location Layout Rev E (P22-DWG-09-007-003)** — Code 3 en el TM N19 — *antes* de emitir el Rev F, planteando que si debían esperar la aprobación del Equipment Layout (TM N11 OBS-03) "probably we can't comply to revise and resubmit within 14 days". Thread "25007 Taltal: Ground cable schedule clarification", adjuntos: `comment.xlsx` (4 preguntas + 2 sub-puntos), `Ground Cable Schedule sample.pdf`, `P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf`, `TM N19 Grounding ADASA comment.pdf`.

> **Hallazgo central:** la dependencia que BW Water invoca la creó el propio **TM N11 OBS-03** y ya está resuelta. TM N11 OBS-03 condicionó el Rev F a que el **Equipment Layout (P22-DWG-09-005-003)** *y* el **Piping Layout (P22-DWG-09-005-004)** estuvieran aprobados; ambos quedaron **Code 2 — Approved as Noted en el TM N15 (22-Abr-2026)**. No existe Rev C formal del Equipment Layout. El driver real del Code 3 nunca fue el layout, sino el grounding schedule (OBS-01 reincidente 3 ciclos).

**Archivos:** `CORREOS/Junio 2026/2026-06-03/` (`crear_correo_grounding_clarification.py`, `2026-06-03_Grounding-RevF-Clarification.docx`, `_Descripcion.md` con sección "Contexto Interno (No enviar)": base factual de aprobación de layouts + hallazgos de la revisión de adjuntos). Inglés, Reply-To al thread, `Document()` directo (sin template ADASA).

**Posiciones por punto:**
1. **Layout dependency resuelta** → proceder con Rev F sobre el Equipment Layout aprobado (Rev B). **El main panel (LCP / Main Switchboard P22-LCP-01) queda fijo y no puede reubicarse**: se rebate expresamente la nota 5 del plano Rev E ("panel locations are indicative only and subject to relocation based on site condition"); cualquier cambio exige layout revisado y aprobado por ADASA.
2. **Grounding schedule** = el entregable que cierra OBS-01. El sample adjunto (26 conductores) es sustancialmente completo (PE points, secciones, ring main, bonding, conexión ADASA-scope) → incorporarlo al Rev F, en el plano o como anexo referenciado (texto literal de la anotación OBS-01). Único refinamiento de material: reconciliar la columna Cable Specification (Cu/PVC en todo) con el Material Take-Off del propio plano (cobre desnudo/trenzado y barra de cobre para electrodo y anillo vs Cu/PVC aislado para PE de equipos).
3. **CCS description** corregida (de "Cable tray layout" a "Grounding…"): cierra el TM N17 OBS-01 al revisar Rev F, condicionado a legibilidad.
4. **Grounding method** = resolver el cross-reference al Typical Installation Details of Power Works (P22-DWG-09-007-005 Rev C) + designar cuál de los 7 métodos aplica a cada carga (IEC 60364-5-54). Se añadió pedir reconciliar la inconsistencia normativa del plano: nota 8 pág. 2 cita **NEC Table 250.122**, pág. 3 cita **IEC 60364-5-54** → unificar a IEC 60364-5-54 (base adoptada en TM N17).
5. **Revision history** (OBS-02): la frase genérica "Revised as per Comment" no basta; pedir descripción de cambios **+ referencia ECN** por cada Rev de B a E.
6. **Screenshots** en el CCS: no están prohibidos; el problema (TM N19 NOTE-01) es la ilegibilidad → emitir desde fuente electrónica.

**Plazo:** extensión corta acotada del Rev F a **Mi 17-Jun-2026** (~+10 días hábiles desde la réplica; evita el sábado 13-Jun). Por instrucción del usuario **el correo NO nombra la reserva del Contrato C-4300** (sólo aparece en la línea Ref del header); la firmeza se sostiene con "there is no longer a basis to defer Rev F". La omisión no implica renuncia de derechos (documentado en el Contexto Interno).

**QA:** barrido §N = 0 en `.md`/`.py`; anti-IA manual (corregido el contraste "not X, it is Y"; em-dash acotado); idioma 100% inglés; metadatos Word limpios (author Luis Rivera, en-US, Application Word, Company ADASA). Días de semana verificados (envío Mi 03-Jun; deadline original Lun 08-Jun; extendido Mi 17-Jun).

**Estado:** **ENVIADO 03-Jun-2026** a Eduardo Yamauchi + CC del thread (Billy Tan, Adzlan Bin Abd Rahim, Jeryl F. Regulacion, Stephane Gehant, David Chee Keat Swee, Sadeep Irugalbandara, Nick Huta) + ADASA (Víctor Gutiérrez). **Pendiente manual:** respaldo PDF/.msg en la carpeta. **Próximo hito:** Grounding Rev F de BW Water el Mi 17-Jun-2026.

---

### 2026-06-02 — Carta Protec Arisawa (ASME) recibida + solicitud de nuevo Recovery Schedule — EN CURSO

> Llegó la **carta de Protec Arisawa Europe S.A.** (adjunta a la respuesta BW Water del 01-Jun; PDF escaneado en `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/RESPUESTA BW WATERS/Letter Protec Arisawa.pdf`). Fechas de entrega de los RO Pressure Vessels: **con ASME Stamp = 31/07**, sin ASME = 22/06; test **1800 psi × 1,1** en ambos casos (cierra de hecho la objeción del rating ASME X 1000 psi). El +6 semanas del ASME es por la obligación de fabricar y aprobar un **prototipo** antes de producir el lote.

**Decisión ADASA:** se acepta el **ASME stamp como un MUST** (se vive con la fecha). El **02-Jun ADASA solicitó a BW Water un nuevo Recovery Schedule** asumiendo los vessels **disponibles el 31/07**. **BW Water lo enviará el jueves 04-Jun-2026.**

**Punto crítico abierto (verificar al recibir el schedule):** ¿el 31/07 es **ex-works España** o **entregado en Penang**? El Recovery Schedule del 22-May está armado SIN ASME (tarea 297 *Manufacturing* termina ~21/06 = fecha sin ASME; tarea 298 *Shipping to Penang from Spain* = 40 días → Penang ~31/07). Si el 31/07 ASME es ex-works España, sumando 40 días de tránsito los vessels llegan a Penang ~09/09 y el embarque se corre ~6 semanas.

**Escenario base de shipment:**
- **Caso A (31/07 = vessels en Penang):** módulo listo para embarque Ex-Works Penang **~15-Aug-2026**; el gatillante real es la bomba HP + turbochargers de USA (airfreight ~11-Aug) + FAT 15 d. Llegada a sitio Taltal ~01-Oct; Performance Test ~mediados-nov.
- **Caso B (31/07 = ex-works España, más probable):** Penang ~09/09; listo para embarque **~inicios/mediados octubre**; sitio ~fin nov; PEM ~dic.

Detalle y trazabilidad: memoria `project_recovery_schedule_asme_31jul`. Vinculado al thread del Mitigation Plan (réplica 01-Jun).

**Update (reunión 02-Jun — reversión):** Tras la reunión (donde se había reiterado que la estampa era requerida) ADASA **revirtió la posición**: acepta la **versión SIN estampa** (entrega 22/06) como gesto de cooperación con la reprogramación, evitando las ~6 semanas que añadía el ASME. Esto **mantiene las fechas del Recovery Schedule del 22-May** para el vessel (que ya estaba armado sobre la base sin estampa: mfg ~21/06 + 40 d transporte = Penang ~31/07 → Ex-Works Penang ~15-Aug → sitio ~01-Oct). Correo de notificación a BW Water — apertura con disculpa por el cambio + condiciones (escenario 22/06 reflejado en el schedule, dossier completo de pruebas de Protec, sin precedente ni renuncia a otras exigencias/garantías, sin Change Order por el ítem ASME) — **ENVIADO 02-Jun-2026** (Reply-To thread del Mitigation Plan): `CORREOS/Junio 2026/2026-06-02/` (`crear_correo_asme_waiver.py` + `2026-06-02_ASME-Stamp-Waiver-RO-Pressure-Vessels.docx` + `_Descripcion.md`). Versión ejecutiva, anti-ia smoke VERDE. Pendiente: respaldo PDF/.msg en la carpeta + verificar con BW Water si 22/06 es ex-works España o Penang.

---

### 2026-06-01 — Respuesta ADASA a la respuesta BW Water del Mitigation Plan (réplica + exigencia de cronograma) — ENVIADO

> **BW Water respondió la NT-001 el Lun 01-Jun-2026 00:33** (tardío vs deadline EOB Vi 29-May; **parcial** — su propio correo dice "addressing part of the technical points"). El adjunto `P22-NT-09-000-001-0_..._ADASA.pdf` es la NT-001 devuelta **sin anotar** (219 KB idénticos); la respuesta sustantiva va en el cuerpo (secciones 3.1–3.6). ADASA contesta el mismo día con un **correo de réplica punto-por-punto**, encabezado por la exigencia del recovery schedule realista para mañana Ma 02-Jun, antes de la reunión semanal.

**Archivos:** `CORREOS/Junio 2026/2026-06-01/` (`crear_correo_respuesta_mitigation.py`, `2026-06-01_Respuesta-Mitigation-Plan.docx`, `2026-06-01_Respuesta-Mitigation-Plan_Descripcion.md` con sección "Contexto Interno (No enviar)": matriz de las 25 + cruce de cronograma + ledger BAE/ET/Oferta + talking points). Inglés, Reply-To al thread BW Water 01-Jun, subject `RE: 25007 Taltal - Mitigation Plan`.

**Disposición de la respuesta BW Water (25 clarificaciones):** ~7 sin responder · 9 parciales/comprometidas (la mayoría al 15-Jun) · 7 aceptadas · 1 resuelta. Hechos nuevos por ítem:
- **3.1 Fedco — NUEVO:** el 26-May FEDCO condicionó el inicio de la documentación a un **anticipo del 30%**; BW Water "engaging Fedco", sin fechas firmes (1.A/1.B/1.D no sustantivas).
- **3.2 CIP:** NTK 18-22 sem; air freight → ~11 sem EXW Penang; desacople **decidido** 20-May; INCOTERM EXW; lista de docs + ensayos FAT; ofrecen plan SAT. Base contractual de las "11 sem": no aportada.
- **3.3 UHPRO:** confirman que el **Performance & Running Test pasa a SAT en sitio**; tabla FAT/SAT al 15-Jun; dry test no inicia sin aprobación ADASA.
- **3.4 EXW:** ventana **8-12 Aug** "a confirmar por FEDCO" (no fecha firme); aceptan reflejar la cascada en el próximo tracker como baseline.
- **3.5 Filtro:** ambos verticales en **FRP** (cierra objeción de corrosión 5.A); datasheet 25-May (Sysflo); PO condicionada a aprobación ADASA; GA/layout/tie-ins pendientes.
- **3.6 ASME:** carta Protec Arisawa prometida "latest 01-Jun" **no llegó**; ITP actualizado al 15-Jun pre-fabricación; 6.A (1000/1800 psi) y 6.E (hito de pago) sin responder.

**Posición ADASA (postura mixta):**
1. **Schedule realista respaldado por vendor para MAÑANA Ma 02-Jun** — urgente: ADASA debe declarar la situación a su gerencia con documentación oficial, y no puede presentar el cronograma previo (EXW 16-Aug + downstream) junto a estas respuestas porque ya no concuerdan. Cada actividad de ruta crítica respaldada por OC confirmada / cronograma firmado / carta de vendor; estimaciones no se aceptan como baseline.
2. **Fedco/30% = rechazo:** asunto comercial interno BW Water↔FEDCO, no traslada el atraso a ADASA (BAE Cl.31 pago contra hitos; Cl.32 anticipo opcional 25% no invocado; Cl.35/46/27 riesgo de sub-proveedor + plazo firme a costo del proveedor).
3. **ASME = firme:** quitar el sello = cambio de alcance → **Change Order**; las 6 sem no agotan el buffer >10 sem (EAP Protec 29-May vs EXW 16-Aug); sin fabricar bajo método modificado sin aprobación del ITP (15-Jun); **se exige evidencia documental** de los ensayos (hidrostática a rating, END, dimensional/material + certificados), **sin enviar testigo**; hitos FAT/despacho condicionados; inquietud Tier-1 (si es un vessel estándar probado, por qué la certificación + 6 sem).
4. **FAT→SAT = solo preguntar:** con qué personal/ventana se ejecuta el ensayo reubicado, anclado a la propia Oferta §18 de BW Water (Field Service Engineer, ~12 días háb., ventana 21 días; la "on-site performance testing" ofertada = validación §10.2 de comisionamiento, no un SAT); posición y costo reservados hasta la tabla del 15-Jun.
5. **Menores:** CIP (punto de recolección + procedimiento FAT + aviso testigo 1 mes); filtro (atestación escrita de tie-ins + GA/layout); Hold Point 4.B (SEC, certs Super Duplex + dossier, preservación marítima) no contestado.

**Deadlines:** recovery schedule realista **Ma 02-Jun** (urgente); resto de pendientes + carta Protec **Vi 05-Jun**; entregables comprometidos (tabla FAT/SAT + ITP PV) **15-Jun**, con 5 días hábiles de revisión ADASA.

**Sustento verificado línea por línea:** BAE Cl.27/31/32/35/43.1.b/46 + Contrato C-4300 (orden de precedencia); ET §8.1 (FAT en fábrica, soporte hito Cl.31), §9 (dotación de comisionamiento = Responsable de Integración + Procesista, 21 días), §10.2 (pruebas de desempeño); Oferta Técnica §18.2/§18.3 + Económica §3.6 (field service = comisionamiento/start-up/performance/training, 21 días, lump-sum ~USD 16.798; "additional field services... under the attached field service policy"). **No existe "SAT"** en ET/BAE/Oferta. El framing del anticipo se apoya en Cl.32-no-invocada + Cl.31 (no se halló frase literal de "no anticipo" de BW Water).

**QA:** réplica anclada a las respuestas de BW Water (no re-emisión de la NT, corrección del usuario). `anti-ia revisar`: original **AMARILLO** por U-03 (oraciones >50p en Fedco/UHPRO/ASME) → corregido a **VERDE** (oraciones divididas + "confirm" reducido). Greps: §-notation = 0, em-dash parentético = 0 en el cuerpo. Día de la semana verificado (Lun 01-Jun, reunión Ma 02-Jun, Vi 05-Jun, 15-Jun lunes).

**Estado:** **ENVIADO 01-Jun-2026** a Eduardo Yamauchi + CC del thread (Adzlan Bin Abd Rahim, Jeryl F. Regulacion, Sadeep Irugalbandara, Nick Huta, Stephane Gehant, Shane Banks, Fadey Kassim) + ADASA (Víctor Gutiérrez).

**Acciones pendientes:**
1. Reunión semanal **Ma 02-Jun** — revisar respuestas + exigir el schedule realista.
2. Esperar: recovery schedule respaldado por vendor (Ma 02-Jun), carta Protec Arisawa + resto de pendientes (Vi 05-Jun), tabla FAT/SAT + ITP PV (15-Jun).
3. Tras la tabla FAT/SAT: definir posición sobre el traspaso a SAT (costo / personal / evidencia / hito de pago).
4. Emitir posición formal por ítem (acceptance / conditional / rejection / Change Order) a medida que lleguen los antecedentes.

---

### 2026-06-01 — Comentarios del revisor (jvaldes) aplicados a la BL Montaje + 2 ET → dossier "Bases REV 0"

> **Revisión de jvaldes sobre 3 PDF del paquete BL** (`BASES DE LICITACION MONTAJE MECANICO-OOCC/COMENTARIOS/`): BL_MONTAJE_TALTAL_REV0 (7 comentarios), ET Montaje Electromecánico P22-ET-06-007-001-0 (29 anotaciones → 6 temas), ET Montaje Cañerías HDPE P22-ET-06-007-002-0 (1). **Tema dominante:** sacar del alcance de montaje las pruebas eléctricas del motor, el conexionado eléctrico/lazo a PLC, el amarre de cableado de instrumentos, el sistema CIP (equipos) y el rodaje/puesta en marcha — todo electricidad e instrumentación / comisionado, etapa posterior. **Decisiones (AskUserQuestion):** (1) eliminar + dejar exclusión explícita; (2) fundaciones de equipos = misma licitación (mismo contratista) → aceptación reformulada a punto de control (hold point) interno de QC, sin aceptación/rechazo entre partes; (3) PDF vía Word COM con TOC actualizado. **BL:** equipos OI/CIP fuera de aportes; sistema CIP simplificado (sin 16/20 kW); cámara de carga = mismo G-25 marino; exclusiones eléctricas/comisionado explícitas. **ET Electromecánico:** Capítulo 7 "Pruebas Eléctricas del Motor" eliminado completo (+ IEEE 43/95, Megger/microohmímetro/personal, filas ITP, HSE eléctrica, hito H9, Figura 7.1); plano de montaje declarado "Apto para Construcción"; pág 35→ ahora 35 pág. **ET HDPE:** corregida la exclusión "sistema aéreo en su totalidad" (el drenaje es enterrado) + **capítulo nuevo "Instalación de Cañerías Enterradas"** adaptado de la ET de referencia P04-ET-00-006-102 Sección 7 (zanja, cama ≥10 cm, relleno cribado ½" + 90% Proctor, lomo de toro, tapado dejando uniones a la vista, cinta detectora; anticorrosión de acero AWWA C209/C210/catódica **N/A al HDPE**). **Generación:** BL del `.md` vía conversor `md_to_adasa_docx.py`; las 2 ET de sus generadores hardcoded (`crear_et_montaje*.py`) + `.md` espejo + `generar_figuras.py`. **3 PDF regenerados** (BL 52 pág, ET elec 35, ET HDPE 29) con TOC actualizado (Word COM, workaround MAX_PATH) y copiados al dossier `Bases REV 0/` (`1. BASES DE LICITACION`, `3. ET MONTAJE/A12`, `A13`) + carpetas fuente; los PDF de `COMENTARIOS/` se conservan como registro. **anti-ia VERDE** (Checklist B, 0 frases-firma, 0 em-dash). Los documentos se mantienen Rev 0 (corrección previa a la distribución). Detalle en memorias `project_bl_montaje_rev0_paquete`, `project_et_montaje_electromecanico_007_001`, `project_et_montaje_canerias_hdpe_007_002`.

### 2026-06-01 — Transmittal OOCC N2 (P22-TM-00-010-002-0, ENTREGA 4) — BORRADOR

> **Segunda revisión del stream OOCC/L&A.** ENTREGA 4 (cover L&A 067-032-032-COR-TT-005, 28-May): **18 documentos** — 5 Memorias de Cálculo (Rev 0), 3 Especificaciones Técnicas (Rev B), 3 Itemizados (Rev B), 7 planos de obras civiles (Rev B). **Veredicto 3 — Por revisar; recuento 7 Código 2 + 11 Código 3.** Drivers: planos + Itemizados (Cód 3), MC-001 (anclaje del estanque aún postinstalado → preinstalado colado, como en TM N1) y MC-003-001 (anexos en Rev B; C5-M). **Calibración del usuario (11 comentarios del revisor):** NPT es dato fijo de montaje — estanque/bomba/fosa coinciden (+5,75, se deja pasar en sus memorias), contenedor/CIP reconcilian con el montaje (queda solo en planos -001/-003/-007); peso del contenedor ~17,3 t aceptado conservador (MC-004 → Cód 2); anclaje CIP diferido aceptado (MC-005 → Cód 2, PEND-03); ET genéricas en título NO se rechazan (3 ET → Cód 2); ET-102 recubrimientos 50/70 mm (TdR Sección 3.3.4); Itemizados referenciales OK → declarar Clase 2 AACE (Minuta arranque). Solicitados los entregables no recibidos: MC Drenajes P22-MC-00-002-003, planos Excavaciones P22-DWG-00-001-001 y Detalles de Anclaje P22-DWG-00-002-005. **Tres follow-ups:** (1) eliminada la tabla "Disposición de los documentos" (redundante) + convención Código 1 (documentos no listados = Aprobados); (2) **doc-annotator v1.6** — texto de comentarios en planos `rotation=90` salía boca abajo (skill hardcodeaba `rotate=270`); fix `text_rotate = original_rotation`; 11 CC_ADASA de planos regenerados y verificados por render PNG; (3) **§2.4 = espejo 1:1 de los CC_ADASA** (19 comentarios, mismos IDs por lámina: NOTA = comentarios base del usuario, OBS = cruces ADASA), corrigiendo "anclaje de bomba debe ser preinstalado" → "evaluar o justificar según categoría sísmica". Fuente `crear_transmittal.py`. **Estado BORRADOR** — pendiente correo de remisión a Pablo Castillo + anti-ia. Detalle vivo en README OOCC + memoria `project_tm_oocc_002_hallazgos`.

### 2026-05-28 — BL Montaje Mecánico + OOCC Rev 0 + Paquete de Licitación "Bases REV 0"

> **Bases de Licitación de Montaje (P22-BL-06-000-001-0, Rev 0 borrador).** Carpeta `BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/`. **Fuente única = `BL_MONTAJE_TALTAL_REV0.md`**, regenerada a Word con el conversor `md_to_adasa_docx.py` de template-adasa (el generador hardcoded `crear_bases_licitacion.py` quedó retirado; el conversor SÍ existe — corrige creencia previa). Se aplicaron los **36 comentarios del revisor** (revisor-docx): despersonalizar (0 menciones a L&A, Vandoorn ni al TR P22-TR-00-010-01-1); estanque TK-06-001 y bomba BH-06-001 **INCLUIDOS** en el montaje (ET P22-ET-06-007-001-0); módulo OI y sistema CIP **"suministrado por ADASA en una etapa posterior"** (no BW Water); **fundaciones del contenedor RO y del CIP independientes** (correo 12-May a L&A) → Formato de Presupuesto a **37 ítems** (Cap.4 = 9, ítem 4.2 dividido); Anexo A9 = la planilla `Formato de Presupuesto.xlsx` (A9.1–A9.8 eliminados); Anexo A10 = índice basado en la **BAE 12803** (Anexo A6 TR L&A eliminado); fosa de drenajes = **TK-06-004**; línea AMF-HDPE-DN160 cubierta en la partida global de drenaje 4.9 (gl). **multi-audit** (7 agentes, sin fabricaciones) + **anti-ia VERDE** ~6-8%. Correcciones de formato del Word: Resumen Ejecutivo a "1." (H1) y cajetín completo en la Hoja 1 (`cliente: ADASA` corto + `cantSplit` → **template-adasa v7.6**). **Paquete distribuible `Bases REV 0/`** armado (solo PDF + xlsx + Navisworks, sin Word editable, sin DWG): `1. Bases` (BL.pdf) · `2. Formato (A9)` · `3. ET Montaje` (A12+A13) · `4. Ing. Detalle Mecánica (A1)` (Compilado Rev 0) · `5. Obras Civiles (A2)` PENDIENTE · `6. Bases Administrativas (A10)` PENDIENTE + `00_INDICE`. **Pendientes:** ingeniería de obras civiles Rev 0 y documento final de Bases Administrativas. Detalle en memoria `project_bl_montaje_rev0_paquete`.

### 2026-05-25 — Transmittal N19 (P22-TM-09-000-019-0) — EMITIDO Y ENVIADO

> Revisión técnica de 13 documentos de E42-E45 (Electrical Power Package + IO List IFC + Quality + Cable Schedule + Cartridge Filters). Veredicto **3 — TO BE REVISED**. Tally **3 Code 1 + 5 Code 2 + 5 Code 3**. Emitido conjuntamente con NT-001 el mismo día (en cadenas de correo separadas).

**Documentos:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-019-0/` (P22-TM-09-000-019-0_TRANSMITTAL.md, crear_transmittal.py, TRANSMITTAL N19 ADASA-BW_WATER.docx, COMENTARIOS/ con 10 scripts + 10 PDFs CC_ADASA = 5 Code 3 + 5 Code 2 per CLAUDE.md §3.8). Correo: `CORREOS/Mayo 2026/2026-05-25/` (`2026-05-25_Transmittal-N19.md/.py/.docx`; respaldo `correo transmittal 19.pdf`).

**Alcance — 13 documentos:**

| Doc | Rev | Veredicto | Observación |
|---|---|---|---|
| Electrical Load List | B | 1 — Approved | Resubmit Rev A Code 1 TM N3; consistente con SLD Rev B |
| Power Cable Schedule | B | 2 — Approved as Noted | OBS-01 MINOR REL-001 CIP Heater topology |
| Datasheet Power & Control Cable | B | 1 — Approved | IEC + SEC compliance |
| Single Line Diagram | B | 2 — Approved as Noted | OBS-01 NEMA 4X + NOTE-01 SPDs |
| Grounding & Power Panel Layout | E | 3 — To Be Revised | Grounding schedule NCh 4/2003 §10.0 ausente (3º TM consec) |
| Cable Tray Layout | C | 1 — Approved | **Cierra 7 items inherited TM N4 OBS-06/07 + TM N15 OBS-04..08 (110d, longest-open)** |
| Typical Power Works Installation | C | 2 — Approved as Noted | NOTE-01 designar METHOD 1-7. Cierra 4 NOTEs TM N17 |
| IO List Rev 1 IFC | 1 | 2 — Approved as Noted | OBS-01 analyser voltage (TM N14 NOTE-02), OBS-02 IFC condicional a Control Philosophy Rev D |
| Project Quality Plan | B | 2 — Approved as Noted | **Cierra 2 OBS CRITICAL TM N17 (inspection matrix + FAT scope) = prerequisito 40% BAE Cl.31** |
| ITP Offsite | B | 3 — To Be Revised | **OBS-01 CRITICAL: silencio ASME X stamp ↔ NT-001 6.A/6.C** |
| Instrumentation & Control Cable Schedule | 0 | 3 — To Be Revised | OBS-01/02 VFD comms + dosing IN REMOTE |
| Datasheet RO Cartridge Filter | D | 3 — To Be Revised | **OBS-01 CRITICAL H→V + Sysflo materializados pre-respuesta NT-001 5.A–5.E** |
| Datasheet CIP Cartridge Filter | C | 3 — To Be Revised | Misma + OBS-03 FRP/gasket compat pH 2-12 |

**Drivers Code 3 (3 críticos):** (1) ITP Offsite ASME X (BAE Cl.31 payment gate, NT-001 6.A/6.C); (2) Cartridge Filters H→V + Sysflo (NT-001 5.A–5.E, riesgo procurement); (3) Plant Control Philosophy Rev D no entregado en este ciclo (Section 3 carry-forward, 3º TM consecutivo — TM N15 NOTE-20 → TM N18 OBS-01 → TM N19, ADASA reserva remedies C-4300 si no llega en 14 días).

**Section 3 reducida a 3 pendientes más críticos** (criterio ejecutivo, los items de menor criticidad quedan en el Master Deliverable Register interno): (a) Plant Control Philosophy Rev D — 3º consecutivo, OBS-01 HP Pump permissive CRITICAL; (b) TM N11 OBS-03 Grounding Layout — 70 días, 3º consecutivo, Hold Point SEC compliance gated; (c) TM N4 NOTE-05 HMI Screenshots — 110 días, oldest open commitment. Closures de este ciclo: Cable Tray Rev C (7 items, longest-open inheritance), PQP Rev B (2 CRITICAL TM N17 + path 40% pago), Typical Power Works (4 NOTEs TM N17), I/O List Rev 1 (vibration/VFD/external TM N3, 110d + dosing TM N17), RO Cartridge flow rate TM N3 OBS-01. Tracked IFC Rev 0 (entregables de docs Code 1/Code 2 aceptados): PSV-09-002, P&ID CIP dual-value, CIT-09-004 loop, AC Thermal margen efectivo, Motor Datasheet Pt-100, REL-001 CIP Heater two-cable, SLD NEMA 4X+SPDs, Cable Tray S1-S7 table, Typical Power grounding method designation, I/O VFD freq + IN REMOTE final, PQP FAT Approval Certificate template.

**Hallazgos de proceso (errores rectificados durante ejecución, ver memorias para detalle):**
1. **Code 2 sin CC_ADASA → CORREGIDO** (CLAUDE.md §3.8: Code 2 SIEMPRE anota NOTEs/OBSs del documento). Detectado por el usuario al ver Section 4 Attachments con solo 5 CC_ADASA. Regenerados 5 PDFs adicionales Code 2 → total 10 CC_ADASA + tabla §4 expandida + texto corregido a "ten annotated PDFs / three Code 1 documents".
2. **Correo conjunto TM N19+NT-001 → SEPARADO en dos correos** (cadenas distintas: TM cadena regular transmittals; NT-001 Reply-To cover BW Water 24-May Mitigation Plan).
3. **NT-001 anti-IA post multi-audit** (~13% AMARILLO): 4 oraciones >50 palabras cortadas, 5 em-dashes parentéticos eliminados, repetición léxica `confirm/issue/address` rotada → VERDE ~4% Confianza MEDIA.
4. **Carpeta de correo NT-001 fechada 2026-05-26** mientras el body decía "25-May" → archivos movidos a `2026-05-25/`, carpeta vacía eliminada.

**QA:** anti-ia VERDE en TM y NT post-correcciones. Multi-audit 8 agentes en TM N19 (referenciado en ediciones previas). Greps pre-envío: 0 §-notation, 0 frases-firma IA, 0 frases pomposas, day-of-week verificado.

**Estado:** Correo TM N19 **ENVIADO 25-May-2026** a Eduardo Yamauchi + CC canónica (To: Eduardo Yamauchi; CC: 17 stakeholders incluido Andrew Sia, Víctor Gutiérrez, Jeryl F. Regulacion; respaldo `correo transmittal 19.pdf` en `CORREOS/Mayo 2026/2026-05-25/`).

**Acciones pendientes:**
1. Regenerar Master Deliverable Register `P22-IT-06-000-002-0_*.xlsx` a estado TM N19 (13 docs nuevos + cambios re-disposicionados + Open Observations + Section 3 reducida).
2. Esperar respuesta NT-001 EOB Vi 29-May para reunión Ma 02-Jun.
3. Esperar Plant Control Philosophy Rev D dentro de 14 días calendario (ADASA reserva remedies C-4300 si no llega).

---

### 2026-05-25 — Nota Técnica NT-001 (P22-NT-09-000-001-0) — Mitigation Plan Clarifications — ENVIADA

> **Primera Nota Técnica formal del proyecto. Introduce tipo NT** en CLAUDE.md §5 + §3.3.1 (carpeta `REVISIONES/NOTAS_TECNICAS/`). Distinción contractual vs CT (pregunta puntual) y TM (revisión sistemática de entregables): la NT agrupa contra-preguntas estructuradas en sub-secciones para responder a un cambio significativo planteado por el proveedor (mitigation plan, change request, technical dispute) con reserva formal de posición hasta recibida la respuesta.

**Documentos:**
- `REVISIONES/NOTAS_TECNICAS/P22-NT-09-000-001-0_Mitigation-Plan-Clarifications.md` (inglés, ENVIADO)
- `REVISIONES/NOTAS_TECNICAS/crear_nota_tecnica.py` (importa template-adasa, `incluir_toc=True`)
- `REVISIONES/NOTAS_TECNICAS/P22-NT-09-000-001-0_Mitigation-Plan-Clarifications_ADASA.docx`
- `CORREOS/Mayo 2026/2026-05-25/2026-05-25_NT-001-Submittal.md` + `.docx` + `crear_correo_nt001_submittal.py` (correo de remisión ejecutivo ~100 palabras; respaldo `Correo plan de mitigacion .pdf`)

**Destinatarios:** To: Eduardo Yamauchi (PMO Leader BW Water), Andrew Sia. CC: Víctor Gutiérrez (ADASA), Jeryl F. Regulacion + lista canónica.

**Contexto:** BW Water entregó **domingo 24-May 18:20** (~2 días después del deadline EOB Vi 22-May exigido en la escalación 14-May) el set `25007 Taltal — Mitigation Plan.pdf` + `12803 Recovery Schedule Updated 2026.05.22.pdf` + cover email con 6 acciones de mitigación. ADASA no acepta el plan en este round: emite NT-001 como **etapa intermedia** con contra-preguntas directas a cada afirmación, sin acceptar/rechazar todavía.

**Estructura (25 contra-preguntas en 6 sub-secciones):**

| Sub-section | Mitigation plan item | Contra-preguntas |
|---|---|---|
| 3.1 Fedco FAT Execution | Push to 29-Jul mfg + airfreight + arrival ~10-Aug | 1.A–1.D (4): firm commitment 29-Jul, pre-EX Works docs, uncertainty range, plan B |
| 3.2 CIP Pump Mitigation | Decoupling >11 weeks, individual FAT, direct shipment | 2.A–2.D (4): lead time real + basis 11-week threshold, INCOTERM, FAT protocol + witness, SAT vs FAT extension personal |
| 3.3 Dry Testing UHPRO | Substantial verification pre-shipment, SOP "ASAP June" | 3.A–3.D (4): scope coverage table, SOP deadline 15-Jun + 5d ADASA review, integrated FAT location, Performance & Running Test location |
| 3.4 EX Works Deferral | 03-Aug → 16-Aug (+13d) | 4.A–4.C (3): 8-Aug vs 10-Aug inconsistency, Hold Point ET §7+§8.1 status, baseline downstream formalization |
| 3.5 Alternative Cartridge Filter | H→V + FRP→SS316, "shorter lead time", "compliance" | 5.A–5.E (5): material justification SS316/Cl⁻, datasheet, container as-built, ADASA pre-approval, tie-ins inamovibles |
| 3.6 ASME PV Certification | PV sin sello ASME, "+6 weeks if stamped" | 6.A–6.E (5): inconsistencia ASME X @ 1000 PSI vs UHPRO 1800 psi, cotización formal Protec con 2 opciones, PIE Detallado aprobado pre-fabricación, witness right Protec facility, hito BAE Cl. 31 |

**Hallazgo crítico Section 3.6 (cross-check tracker SEMANA 11-05-26 + memoria EP-2):** vendor real RO Pressure Vessels = **Protec Arisawa Europe S.A.**, **PO M184 emitida 20-Apr-2026** (modelo BPV81200SP), EAP Penang declarada **29-May-2026** (lead time real 5,5 semanas), buffer >10 semanas hasta EX Works 16-Aug → el argumento BW Water "6 weeks added by ASME stamp" no agota el margen disponible. M184 cuenta como instrumento conforme para **EP-2 (BAE Cláusula 31)** → modificar alcance post-emisión (eliminar sello ASME X comprometido en ITP §12 oferta) = cambio al alcance contratado, requiere Change Order formal, puede afectar elegibilidad de M184 para EP-2.

**QA validación:** 4 agentes auditores en paralelo foco específico (fechas + day-of-week, citas literales contra ET/Oferta, coherencia interna, registro contractual). 24 fixes consolidados, los más críticos: **cita falsa a "Technical Specification Section 5.5.5" eliminada** (era Conductímetros, no SS316L — argumento PREN/Cl⁻ reformulado como análisis técnico ADASA con cita correcta a Section 5.2); **Hold Point pre-embarque reatribuido** de Section 6 (incorrecto) a Section 7 + Section 8.1; **fechas corregidas** (06-Jun era sábado → 05-Jun → 29-May para reunión 02-Jun); **pre-rechazos suavizados** ("ADASA will not absorb" → "does not anticipate absorbing… reserves the right"; "shall not proceed" → "ADASA requires… prior to"); **numeración renumerada contigua** 2.A-D y 6.A-E (originalmente 2.A,C,D,E y 6.A,B,E,F,G por descartes en revisión interactiva); **Section 5.2 ADASA Reservations suavizada** al tono "under technical review, invited to coordinate"; **eliminada Section 6 Document History** (redundante con cajetín). Greps pre-emisión: 0 frases-firma IA, 0 §-notation en contenido, 0 frases pomposas. Referencias ET por nombre completo "Technical Specification — [Name] (Section X)" per CLAUDE.md §2.4.

**Deadline respuesta BW Water:** **EOB Friday 29-May-2026**, para que las respuestas sean revisadas en la **reunión semanal del martes 02-Jun-2026**.

**Revisión anti-IA final (25-May, post multi-audit):** detección manual del usuario sobre patrón "muchas explicaciones con guiones" disparó revisión completa con skill `anti-ia`. Veredicto inicial AMARILLO ~13% atenuado: U-03 (4 oraciones >50 palabras), U-10 (5 em-dashes parentéticos explicativos), U-09 (`confirm/issue/address` 10+ ocurrencias c/u), U-04/U-06/CL-09 atenuados por formato contractual institucional. Aplicadas Acciones 1-5: oraciones cortadas (L32, 1.B, 2.A, 4.B, 3.6 prelude), em-dashes parentéticos → coma/paréntesis (L32, L145, L147, L179, L181), rotación de sinónimos (`issued`→`released/placed/sent`; `confirm`→`state in writing/acknowledge in writing/written attestation`; `considering`→`given that`). Veredicto post-corrección: VERDE ~4% Confianza MEDIA. Mantenido em-dash legítimo en nombres de sección contractual + headers de items + enumeración 6.B (i)/(ii).

**Cadena de correo separada:** NT-001 emitida como **Reply-To** al cover email de BW Water del **24-May-2026** que transmitió el Mitigation Plan + Recovery Schedule. **NO conjunta** con TM N19 (cadena de transmittals regular). Decisión post-revisión inicial (envío conjunto se planteó inicialmente para cerrar flanco procesal de cross-references desde TM N19 hacia NT-001, pero el riesgo se neutraliza enviando ambos el mismo día con cross-references explícitas en Sections 2.10, 2.12, 2.13 del TM N19). Cover NT-001 movido de `CORREOS/Mayo 2026/2026-05-26/` (carpeta de fecha errónea) a `2026-05-25/` y renombrado consistentemente.

**Estado:** Correo NT-001 **ENVIADO 25-May-2026** a Eduardo Yamauchi + CC canónica (respaldo `Correo plan de mitigacion .pdf` en `CORREOS/Mayo 2026/2026-05-25/`). **Respuesta BW Water recibida 01-Jun-2026 (tardía, parcial); ADASA replicó el mismo día — ver entrada `01-Jun-2026` al inicio de §9.**

**Cierre del ciclo NT-001:**
1. ~~Esperar respuesta escrita BW Water EOB Vi 29-May~~ → **recibida 01-Jun-2026 00:33** (parcial: ~7 sin responder · 9 parciales/15-Jun · 7 aceptadas · 1 resuelta). Set en `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/RESPUESTA BW WATERS/`.
2. Reunión Ma 02-Jun para revisar respuestas (en curso).
3. Posición formal ADASA por ítem (acceptance / conditional / rejection / Change Order) — **iniciada en el correo réplica del 01-Jun**; se completa a medida que lleguen los antecedentes (schedule 02-Jun, Protec + pendientes 05-Jun, tabla FAT/SAT + ITP 15-Jun).

### 2026-05-19 — Transmittal OOCC N1 (P22-TM-00-010-001-0) — BORRADOR (versión ejecutiva)

> **Nuevo stream OOCC/L&A (español).** Primera revisión técnica de L&A Ingeniería y Proyectos (Pablo Castillo): ENTREGA 3, 5 Memorias de Cálculo Rev B contra el TdR P22-TR-00-010-01-1, planos antecedentes (Van Doorn, BW Water), datos de equipos (Exfibro EX-26005-F01 Rev C, KSB) y la línea base sísmica interna del estanque (P22-IT-06-000-005-0). **Veredicto global: 3 — Por revisar.** Tally final **3 Código 2 + 2 Código 3**; lo fijan **MC-001** (anclaje especificado como postinstalado con material/geometría de preinstalado/colado en sitio → rediseñar preinstalado ACI 318-19 Cap. 17/Sección 17.10; lógica validada con investigación dirigida) y **MC-003-001** (clasificación de suelo D vs E + protección C5-M no abordada). Aprobadas con comentarios: MC-002, MC-004 y **MC-005** (reclasificada de Código 3 → 2 el 19-May: la verificación de anclajes deja de ser rechazo — L&A no tiene los planos/fichas finales del proveedor de equipos CIP, los anclajes serán postinstalados, aceptable si cumplen solicitaciones → diferida como **PEND-03**; NOTA-07: pesos de dosificación correctos del TdR 2.1.2 = ≈550 kg [TK-09-002 490 kg + BDS 57,4 kg], L&A asumió ≈1000 kg → corregir el valor declarado, diseño conservador sin recálculo). Hallazgo transversal ACI 318-14 vs 318-19 (TdR) tratado como NOTA. **Auditoría multi-audit** (modo `auditar`, 10 agentes, foco NPT): ninguna MC declara ni verifica el NPT (usan "Modelo Navis Referencial", no vinculante); TR lo hace dato fijo verificable contra el Levantamiento DIO antes de Rev A; doble N.T.N. +5,75 (estanque/bomba) vs +6,00 (módulo/CIP). Incorporada **OBS-NPT (Mayor)** en las 4 MC de fundación + NOTA-07 peso BH-06-001 en MC-002 (montaje 250 kg; reconciliar vs ficha técnica KSB / ACI 351.3R). MC Sistema de Drenajes (P22-MC-00-002-003) no entregada → pendiente informativo PEND-01. Fundación compartida TdR reasignada a dos fundaciones independientes (-004/-005), enfoque aceptado (Minuta MI-001 ítem 1.7), OBS de codificación. Comentarios redactados como **directivas de corrección** (no opiniones). **Versión ejecutiva** (19-May): Resumen Ejecutivo con tabla de disposición; cada OBS/NOTA en una línea Defecto→Corregir→Requisito; recuadros CC_ADASA ≤ ~8 líneas; estructura ADASA de 5 secciones intacta. **Correcciones de idioma/formato (19-May):** purga de anglicismos de jerga ejecutiva (Tally→Recuento, Drivers→Determinantes, Trackeado→Seguimiento); ID **NOTE→NOTA** (162 ocurrencias, español 100% para L&A); doble numeración de headers corregida (el `Template_ADASA` auto-numera H1/H2/H3 — se quitaron los números manuales de `add_heading()`). Flujo espejo en español en `INGENIERIA DE DETALLE OOCC/REVISIONES/` (README + Hitos propios). DOCX+PDF y 5 PDF CC_ADASA regenerados (NOTA-XX; anotaciones 6/6/6/7/6 = tabla ADJUNTOS). anti-ia VERDE (Checklist B). Falta envío a L&A.

### 2026-05-18 — Transmittal N18 (P22-TM-09-000-018-0) — EMITIDO Y ENVIADO

> **RE-ESCOPEADO 18-May-2026:** se incorporó E41/25007-0041 **P&ID Rev D** como Sección 2.5 (correo aún BORRADOR → re-escopeo, no TM N19). Ahora **5 documentos**, submittals 25007-0038..0041, tally **1 Code 1 + 3 Code 2 + 1 Code 3**. P&ID Rev D = Code 2: cierra **TM N13 NOTE-01** a nivel P&ID (CIP Tank 6.81 vs 6.1 m³ resuelto como total 6.8 / efectivo 6.1, ambos anotados; justificación física verificada). NOTE-01 P&ID: cambio BW-initiated del tapping de CIT-09-004 (orifice + needle valve) → entregables IFC definidos (Instrument List Rev D + Line List Rev C + nota de respuesta del lazo). 2º multi-audit 8 agentes (sin FABRICADO, ALTO): detectó y corrigió contradicción "Tracked for IFC: None" → ahora lista **TM N16 NOTE-01 + convención dual-value CIP Tank**. anti-ia VERDE 2ª ronda. Las descripciones siguientes (Alcance/tabla/hallazgos) reflejan la versión re-escopeada.

> **RE-DISPOSICIONADO 18-May-2026 (criterio ejecutivo Code 1/2):** el código refleja el estado del **documento revisado en sí**. Si el documento no requiere modificación a sí mismo → **Code 1**; los "comentarios" que son entregables sobre OTROS documentos / análisis separados se trackean en Sección 3, no degradan a Code 2. Verificado verbatim que AC Thermal Rev C no tiene error (carga/margen/unidad correctos; solo se pide indicar el margen explícito → Code 1). **Valve List Rev D, AC Thermal Rev C y P&ID Rev D bajan de Code 2 → Code 1.** Tally final: **4 Code 1 + 0 Code 2 + 1 Code 3**. Code 2 no se usa en TM N18 pero sigue en la metodología para casos donde el propio documento lleva un error/cambio menor a Rev 0. Regla refinada en CLAUDE.md §6.2/§6.3 (v6.11). Adjuntos: **1 CC_ADASA** (solo Control Philosophy, Code 3); los 4 Code 1 sin CC_ADASA (§3.8), scripts/PDFs como traza interna.

**Documentos:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-018-0/` (P22-TM-09-000-018-0_TRANSMITTAL.md inglés, crear_transmittal.py, TRANSMITTAL N18 ADASA-BW_WATER.docx, _ANALISIS_TRABAJO.md interno, COMENTARIOS/ con 4 scripts; solo Control_Philosophy_CC_ADASA.pdf se emite). Correo: `CORREOS/Mayo 2026/2026-05-18/` (.md BORRADOR + crear_correo_tm18.py + .docx).

**Alcance:** Submittals 25007-0038 (E38), 25007-0039 (E39), 25007-0040 (E40), 25007-0041 (E41) — 5 documentos. Veredicto global **3 — TO BE REVISED** (driver único Control Philosophy Code 3). Tally: 4 Code 1 + 1 Code 3.

| Documento | Rev | Veredicto |
|-----------|-----|-----------|
| Plant Control Philosophy | C | 3 — To Be Revised |
| Valve List | D | 1 — Approved |
| Line List | C | 1 — Approved |
| AC Thermal Calculation | C | 1 — Approved |
| Piping & Instrumentation Diagram | D | 1 — Approved |

**Hallazgo driver:** OBS-01 CRITICAL — el permissive de arranque del HP Pump en Control Philosophy Rev C sigue con "VE-09-007 and VE-09-007" duplicado y exige "VE-09-014 fully CLOSED" (VE-09-014 = válvula entrada estanque antiescalante que abre para rellenar). Repite TM N15 NOTE-20 (2º transmittal consecutivo) → tras multi-audit se añadió condición bloqueante para cierre del Control Philosophy + registro para seguimiento contractual C-4300. OBS-02 MAJOR: lógica de control núcleo (Sequence Charts / Alarm & Control Setpoint List / Control Matrix) sigue "SEPARATE DOCUMENT", fecha tentativa 13-May vencida, no entregada con E39. OBS-03 MAJOR: fórmula salt rejection usa CIT-09-005 reject en vez de feed CIT-09-001B.

**Documentos Code 1 (aceptados as-is, sin modificación al documento):** **Valve List Rev D** — misma Rev D (18-Mar-26, 111 ítems) ya Code 2 en TM N14, tabla intacta; el análisis de protección de sobrepresión del 2º PSV-09-002 es entregable separado → Sección 3. **Line List Rev C** — cierra TM N12 NOTE-01 (PE-PVC-DN80-09-019) y NOTE-02 (SCH80S). **AC Thermal Rev C** — verificado verbatim sin error (carga 6.24 kW=1.774 TR, margen 2.04, unidad 2.01 TR +13.3% sobre peak; n+1 confirmado); cierra TM N15 NOTE-02; solo se pide declarar el margen efectivo explícito → entregable Sección 3. **P&ID Rev D** — cierra TM N13 NOTE-01 (CIP Tank 6.81 vs 6.1 = total 6.8 / efectivo 6.1, ambos anotados); plano as-is; cambio BW-initiated tapping CIT-09-004 → Instrument List Rev D + Line List Rev C + nota de respuesta del lazo, entregables Sección 3; 3 cambios CCS aceptados (diaphragm seals, area limits, manhole).

**Carry-forward Section 3:** 9 ítems abiertos heredados (TM N4 OBS-06/07 101d, TM N4 NOTE-05 HMI 102d, TM N5 OBS-02 83d, TM N10 OBS-05 66d, TM N11 OBS-03 61d, TM N13 NOTE-02 41d, TM N15 LCP 25d, TM N15 Cable Tray 25d/101d, TM N16 NOTE-01 23d). Cerrados por TM N18: TM N12 NOTE-01/02, TM N15 NOTE-02, **TM N13 NOTE-01 (P&ID Rev D)**. **Tracked IFC Rev 0** (entregables de docs Code 1 aceptados, no nuevas revisiones): TM N16 NOTE-01 (weight disclosure); PSV-09-002 análisis de sobrepresión; CIT-09-004 en Instrument List Rev D + Line List Rev C + nota de lazo; convención dual-value CIP Tank (P&ID ↔ datasheet ↔ Equipment List); AC Thermal margen efectivo explícito (+13.3%).

**QA:** anti-ia `revisar`+`evaluar` VERDE confianza Alta en 2 rondas (0 fingerprints críticos, 0 §N, 0 frases prohibidas). multi-audit `auditar` 8 agentes ×2 rondas — 1ª ronda (Defensor 9, Fiscal 4.5, Juez 8.2, Estilista VERDE, Verificador MEDIO-ALTO, Auditor Sombra ALTO, Neutro, Abogado): 3 obligatorias (escalación OBS-01, candado pre-IFC Valve List NOTE-01, énfasis Exec Summary). 2ª ronda (re-escopeo P&ID Rev D): sin FABRICADO, confianza ALTO; 3 obligatorias (fix contradicción Tracked-IFC None→TM N16+dual-value, calificar cierre TM N13 NOTE-01, endurecer NOTE-01 P&ID a entregables IFC). 3ª fase (re-disposición criterio ejecutivo Code 1/2): Valve List/AC Thermal/P&ID → Code 1, entregables a Sección 3; regla codificada CLAUDE.md §6.2/§6.3 v6.11; anti-ia VERDE 3ª verificación (§N=0, 0 frases prohibidas). Van Doorn no aplica (5 docs área 09).

**Estado TM N15/N16:** confirmados ENVIADOS por el usuario (correos 22-Apr y 24-Apr); respaldos PDF pendientes de adjuntar al repo por el usuario. TM N17 ENVIADO 05-May (respaldo en carpeta).

**Estado:** Correo TM N18 **ENVIADO 18-May-2026** a Eduardo Yamauchi + CC canónica (respaldo "Elementos enviados ... Outlook.pdf" en `CORREOS/Mayo 2026/2026-05-18/`; `.md` estado ENVIADO). Master Deliverable Register `P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx` regenerado a estado TM N18 (5 docs re-dispositionados, Summary recalculado, Legend/Status Date 18-May).

**Acciones pendientes (esperando a BW Water / usuario):**
1. Esperar fecha objetivo Plant Control Philosophy **Rev D** (único Code 3) + fechas de los entregables Sección 3: PSV-09-002 análisis sobrepresión (Valve List), CIT-09-004 en Instrument List Rev D + Line List Rev C + nota de lazo (P&ID), margen efectivo explícito (AC Thermal), dual-value CIP Tank, TM N16 NOTE-01.
2. Adjuntar respaldos de envío de TM N15 y TM N16 al repo cuando estén disponibles (ambos confirmados ENVIADOS por el usuario; correos 22-Apr y 24-Apr).
3. Documento narrativo `P22-IT-06-000-002-0_Document-Status-Register_ADASA.docx` (vía `crear_registro.py`) está en estado Abril (no es companion del xlsx ni se actualiza por TM); el registro maestro vigente por entregable es el `.xlsx`. Actualizar el DOCX narrativo solo si se requiere un Document Status Register formal a fecha.

### 2026-05-14 — Fedco EAP vs EXW Shipping conflict — Mitigation plan requested — ENVIADO

**Documento:** `CORREOS/Mayo 2026/2026-05-14/2026-05-14_Fedco-FAT-Conflict.docx` (v1.2 ENVIADO)
**Script:** `CORREOS/Mayo 2026/2026-05-14/crear_correo_fedco_fat.py`
**Fuente:** `CORREOS/Mayo 2026/2026-05-14/2026-05-14_Fedco-FAT-Conflict.md`

**Destinatarios:** To: Eduardo Yamauchi (BW Water). CC: lista canónica 17 stakeholders (idéntica a correos previos 05-may y 12-may).

**Contexto:** Tras revisión detallada del tracker SEMANA 11-05-26 enviado por Yamauchi el 12-may, ADASA detectó que los 3 equipos Fedco (Bomba RO Alta Presión BH-09-001, Feed Turbocharger SIP-09-001, Interstage Turbocharger SIP-09-002) muestran EAP Penang 03-Ago-2026 — misma fecha del embarque EXW del baseline 05-Mar-2026. El FAT baseline (25-Jul a 01-Ago) cierra dos días antes de la llegada Fedco. Slip silencioso entre trackers consecutivos: PO Date +25 días (20-Abr→15-May); EAP Penang +16 días (18-Jul→03-Ago); Bomba RO reclasificada C→D-Delayed.

**Solicitud:** mitigation plan en reunión semanal lunes 18-May-2026, confirmación escrita EOB Friday 22-May-2026 cubriendo: (i) FAT execution plan Fedco, (ii) deferral EXW Shipping si aplica, (iii) vendor expedite efforts, (iv) impacto downstream (Site Supervision 18-Sep, Training 09-Oct, Close-out 18-Oct). Decoupling clause explícita: el FAT clarification corre en paralelo con el bundle EP-1+EP-2 propuesto el 12-may bajo Cláusula 31 BAE 12803; no condiciona el trámite contractual.

**Auditoría pre-envío:** multi-audit `auditar` con 8 agentes en paralelo (3 fuentes: tracker 11-05, tracker 04-05, baseline 05-Mar). Veredicto 8,0/10 con triple veracidad ALTO (Factual 10/10, Verificador, Auditor Sombra — 0 fabricaciones, 17/17 datos verificados). 3 obligatorias aplicadas en v1.1: (i) Subject acortado de 165→96 chars para evitar truncado Outlook, (ii) decoupling clause consolidada de 2 oraciones a 1, (iii) verbos endurecidos ("Please come prepared"→"BW Water is requested to present"; "we would appreciate confirmation"→"ADASA requests confirmation"). Recorte ejecutivo en v1.2: cuerpo ~770→440 palabras (−43%).

### 2026-05-14 — Aclaración Plazos EP-1+EP-2 (interno a Victor) — DESCARTADO

**Documento:** `CORREOS/Mayo 2026/2026-05-14/2026-05-14_Aclaracion-Plazos-EP1-EP2.md` (v2.1 DESCARTADO)

**Contexto:** correo formal en español preparado para que Victor Gutiérrez reenviase a gerencia AA, aclarando confusión EXW Penang (03-Ago) vs sitio Taltal (18-Sep), slip Fedco entre semanas, y separación entre hito de pago documental EP-2 vs entrega física. **No enviado:** el tema se discutió directamente con Victor en persona; el reenvío formal a gerencia no fue necesario. Auditoría multi-audit del documento y análisis quedan preservados como insumo si el tema se reactiva.

### 2026-05-12 — EP-1 + EP-2 Bundle Proposal — Closing pending POs by 31-May-2026 — ENVIADO

**Documento:** `CORREOS/Mayo 2026/2026-05-12/2026-05-12_Procurement-Backup-Request.docx`
**Script:** `CORREOS/Mayo 2026/2026-05-12/crear_correo_backup_request.py`
**Fuente:** `CORREOS/Mayo 2026/2026-05-12/2026-05-12_Procurement-Backup-Request.md`
**Respaldo:** `CORREOS/Mayo 2026/2026-05-12/Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf`

**Destinatarios:** To: Eduardo Yamauchi (BW Water). CC: Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim.

**Contexto:** Propuesta a BW Water para presentar EP-1 (10%) y EP-2 (15%) en bundle la primera semana de Junio, condicionado al cierre de las 2 POs aun pendientes para los 7 equipos principales del BAE Cl. 31 antes del 31-May-2026. Auditoria sobre el tracker SEMANA 11-05-26 + 17 unpriced PO PDFs en `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/Unprice PO/`.

**Cobertura EP-2 (tabla unica en el correo):**

| # | Equipo (BAE Cl. 31) | Cobertura | Source |
|---|---------------------|-----------|--------|
| 1 | High Pressure Pump | OK | Fedco package — PO M183 (08-May) |
| 2 | Energy Recovery (ERD) | OK | Fedco package — PO M183 (08-May) |
| 3 | Cartridge Filters | Pending | Fil-Trek — items 8/18 status E |
| 4 | Pressure Vessels | OK | Protec Arisawa — PO M184 (20-Apr) |
| 5 | RO Membranes | Pending | LG — item 19 status E, sin PO date |
| 6 | Dosing System | OK | ProMinent M089 + Promatics M074 |
| 7 | CIP System | OK | Quantic Logic M062 + Dayamas M073 |

**Preguntas formuladas:**
- Fil-Trek (items 8/18): tracker muestra PO Date 14-May / 05-May con status E y remark "Nego on leadtime with vendor still ongoing". ¿POs y unpriced PDFs antes del 31-May-2026?
- LG (item 19): status E sin PO date, ventana baseline cerrada 27-Apr-2026. ¿Fecha objetivo de LG? ¿31-May factible?

**Tono:** colaborativo, propositivo (no escalation). Una sola tabla. Bullets en Proposal y Questions. Sin meeting propuesto. Cierre directo.

**anti-ia v6.1.3:** VERDE 2%, confianza Media. 0 marcadores criticos. 4/4 niveles semioticos VERDE.

**Acciones post-envio:**
1. Esperar respuesta BW Water sobre fechas Fil-Trek y LG.
2. Si BW Water confirma 31-May para ambas POs: coordinar con Victor Gutierrez la presentacion bundle EP-1+EP-2 primera semana de Junio.
3. Si alguna PO no llega a 31-May: planificar EP-2 con fecha realista que provea BW Water.
4. Cross-check tracker SEMANA 18-05-26 para verificar status Fil-Trek y LG.

---

### 2026-05-07 — Engineering Closure Proposal — Interim Acceptance for Payment Milestone (31-May-2026) — ENVIADO

**Documento:** `CORREOS/Mayo 2026/2026-05-07/2026-05-07_Engineering-Closure-Interim-Proposal.docx`
**Script:** `CORREOS/Mayo 2026/2026-05-07/crear_correo.py`
**Fuente:** `CORREOS/Mayo 2026/2026-05-07/2026-05-07_Engineering-Closure-Interim-Proposal.md`

**Destinatarios:** To: Eduardo Yamauchi, Andrew Sia (BW Water). CC: Victor Gutierrez (ADASA), Jeryl Regulacion (BW Water).

**Contexto:** Propuesta a BW Water para habilitar Estado de Pago por la fase de ingenieria antes del 31-May-2026 sin renunciar al Spanish IFC Rev 0 contractual. Mecanismo de dos etapas: ADASA reconoce las Rev actuales en ingles como engineering closure for payment certification (sin renunciar al IFC Rev 0 espanol); a cambio BW Water entrega 8 items criticos antes del 31-May (#16 A/C Thermal, #28 Cable Tray, #67 Control Philosophy, #73 PIE, #75 Modbus, #81 LCP, #91 PQP, #93 A&I List) y compromete fecha binding para Spanish IFC Rev 0 (sugerido +30 dias post-EP).

**Tono:** ejecutivo, directo, 27 parrafos. Sin propuesta de reunion (cierre con "look forward to your comments"). Decision tomada tras feedback usuario.

**Acciones post-envio pendientes:**
1. Coordinar con Victor Gutierrez la version final del Engineering Completion Certificate (interim).
2. Pre-validar con Comercial (Cesar Malhue) que el certificado interino habilita el procesamiento del EP a fin de mes.
3. Si BW Water no entrega los 8 items criticos antes del 31-May, activar Plan B: pago parcial por items Code 1 ya cerrados.

---

### 2026-04-20 — TdR OOCC P22-TR-00-010-01-0 Revisado + Algoritmo D unificado en 3 skills + CLAUDE.md v6.4

**Documentos generados:**
- `INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/P22-TR-00-010-01-0_TDR_OOCC_EM.md` (fuente)
- `INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/crear_tdr_oocc.py` (generador DOCX)
- `INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/P22-TR-00-010-01-0_TDR_OOCC_EM.docx` (10.3 MB, regenerado)
- `CLAUDE.md` v6.2 → v6.3 → v6.4 (3 iteraciones el mismo dia)

**Contexto:** Revision del TdR de Obras Civiles y Estructuras Metalicas (trato directo bajo contrato marco ADASA-consultor, no licitacion). Originalmente redactado como licitacion publica con oferentes, boletas de garantia y clausula de suspension por BW Water — reescrito a modalidad de trato directo con condiciones comerciales remitidas al contrato marco. Eliminadas todas las menciones a terceros (Van Doorn en cuerpo y matriz RACI; BW Water en tablas de suministro y exclusiones).

**Cambios estructurales TdR:**
1. Eliminadas 5 secciones de licitacion (Glosario, Evaluacion de Ofertas, Vigencia/Visita/Consultas, Requisitos del Oferente, Clausula de Suspension BW Water).
2. Garantias, Moneda, Forma de Pago, Multas, Termino Anticipado, Resolucion de Controversias remitidas al contrato marco.
3. Paquete de antecedentes reescrito con nombres funcionales (Planos de sitio / Planos mecanicos y de piping / Planos de equipos con impacto civil / Documentos complementarios del modulo).
4. Normativa actualizada NCh 2369 → NCh 2369:2025 (7 ocurrencias).
5. Linea drenaje SA-CPVC-DN200-PN10-001 referenciada a planos piping P22-DWG-06-006-103/104 (no "planos de Van Doorn").
6. Matriz RACI reducida de 4 cols (Consultor/ADASA/Van Doorn/BW Water) a 2 cols (Consultor/ADASA).
7. Figura 4-4 Georadar con nota temporal — pendiente reemplazo por ortofoto DIO 2026.

**Fix skills — Algoritmo D unificado:**

Al regenerar el TdR se detectaron 2 bugs criticos en la infraestructura de skills:

- **Bug 1 — skill local desactualizada:** `.claude/skills/template-adasa/` del proyecto NO era symlink (Windows/Synology no lo soporta), sino copia v6.0 (Feb 2026). Generaba placeholders "RESUMEN EJECUTIVO" y "1. INTRODUCCION" antes del contenido real. Fix: script migrado a path global absoluto `~/.claude/skills/template-adasa/`. Regla documentada en CLAUDE.md §3 v6.3.

- **Bug 2 — anchos de columna:** La tabla §4.2 "Equipos Exteriores Area 06" (6 cols) quedo rota con columna TAG colapsada y filas extendidas en 3 paginas. Causa raiz: el algoritmo generaba anchos negativos cuando la suma de cortas saturadas excedia el ancho total. Fix aplicado como Algoritmo D (hibrido entre el algoritmo natural+cap de adasa y el piso+proporcional de lrg/mba), homogeneizado en las 3 skills globales:

| Skill | Archivo | Ancho total | Min col | Max corto | Unidad |
|-------|---------|-------------|---------|-----------|--------|
| template-adasa | `table_utils.py::calcular_anchos_columnas` | 6.5" | 0.6" | 2.0" | EMU (Inches) |
| template-lrg | `md_to_lrg_docx.py::_calcular_anchos_d` | 16.0 cm | 1.5 cm | 5.0 cm | cm |
| template-mba | `md_to_mba_docx.py::_calcular_anchos_d` | 16.0 cm | 1.5 cm | 5.0 cm | cm |

Algoritmo D verificado con 7 casos (desde 2 hasta 8 columnas, contenido uniforme vs heterogeneo, extremos con super-largas). Fix Caso 5 confirmado (cols uniformes antes `[5.3, 0.6, 0.6]`, ahora `[2.17, 2.17, 2.17]`).

**Nueva regla CLAUDE.md §2.6:** Referencias internas dentro del mismo documento usan `Seccion N — Nombre Completo` (ej. `Seccion 6 — Entregables por parte del Consultor`), prohibido `§NombreSeccion`. Razon: Word numera automaticamente los Heading 1; referenciar por numero permite ubicar la seccion sin depender de que el lector recuerde el nombre. Aplicado a 4 referencias del TdR.

**Verificacion DOCX final:** 50 gridCol generados (min 916 DXA = 0.64", max 7120 DXA = 4.94"), cero anchos sospechosos. Contenido arranca directamente en "INTRODUCCION" tras el TOC (sin placeholders residuales).

---

### 2026-04-20 — Weekly Procurement Reporting Protocol — Format & Cadence — ENVIADO (v8)

**Documento:** `CORREOS/Abril 2026/2026-04-20/2026-04-20_Weekly-Procurement-Reporting-Protocol.docx`
**Script correo:** `CORREOS/Abril 2026/2026-04-20/crear_correo.py`
**Script plantilla:** `CORREOS/Abril 2026/2026-04-20/generar_plantilla_procurement.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-20/2026-04-20_Weekly-Procurement-Reporting-Protocol.md`
**Adjunto:** `CORREOS/Abril 2026/2026-04-20/WEEKLY-PROCUREMENT-TRACKER_12803_v0.xlsx` (plantilla ejecutiva pre-poblada 17 lineas)
**Respaldo envio:** `CORREOS/Abril 2026/2026-04-20/respaldo envio correo de seguimiento.pdf`

**Contexto:** ADASA formaliza el protocolo de reporte semanal de procura el mismo dia de la minuta y del correo de Fadey Kassim, cerrando el ciclo sin demora. Respuesta al (a) commitment generico de Kassim 20-Abr ("regular, concise updates"), (b) Action Item 1 de la minuta 20-04 ("Reporte Ejecutivo en Excel"), y (c) agenda punto (d) del correo 17-Abr ("standing communication protocol — weekly PO status reporting"). Destinatarios: Andrew Zaske, Eduardo Yamauchi, Fadey Kassim, Victor Gutierrez (circuito ejecutivo cerrado). **Alcance:** 17 equipment lines (16 del Baseline Schedule BWW 05-Mar-2026 + RO Membranes declaradas en minuta BWW 20-Abr, origen US). **Cadencia:** lunes 10:00 AM CLT; primer reporte 27-Abr-2026. **Esquema de status C/E/D/N** (Committed / Enabled / Delayed / Not in Window) alineado con Codes 1/2/3/4 de revision de ingenieria. Plantilla v4 pre-pobla: 9 lineas con status C + 4 lineas E conforme minuta BWW 20-Apr; 4 lineas sin status (Instrument Set, All Valve Set, Structural Frames, Static Mixer). Suppliers pre-poblados: Fedco (3 lineas), Prominent (1 linea). Nota fija sobre EXW Penang. **v4 agrega parrafo sobre gap de proveedor en linea "All Valve Set"** — Valve List Rev D (18-Mar-2026) tiene todos los fields de brand/make/model como TBA; supplier chino mencionado en minuta BWW es declaracion verbal no respaldada documentalmente. Escalacion automatica a Fadey Kassim dentro de 24h para status D. Deadline confirmacion: EOB miercoles 22-Abr-2026.

---

### 2026-04-20 — ADASA Response to BW Water Meeting Minute — ENVIADO (v4)

**Documento:** `CORREOS/Abril 2026/2026-04-20/2026-04-20_Response-BWW-Meeting-Minute.docx`
**Script:** `CORREOS/Abril 2026/2026-04-20/crear_correo_response_minute.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-20/2026-04-20_Response-BWW-Meeting-Minute.md`
**Minuta respondida:** `CORREOS/Abril 2026/2026-04-20/respuesta de minuta de bwwaters reunion 20-04-26.pdf`
**Respaldo envio:** `CORREOS/Abril 2026/2026-04-20/respaldo envio correo de Minuta.pdf`

**Contexto:** Correo complementario al Weekly Procurement Protocol del mismo dia. Documenta la posicion ADASA sobre tres puntos de la minuta BW Water (Eduardo Yamauchi 20-Apr 10:24 AM) donde hay fricciones o vacios: (1) valvulas con proveedor chino, (2) Operating Weights removidas en Equipment Layout Rev C advance copy, (3) Emergency Access Door sin confirmar dimension y tipo. **Posicion clave valvulas:** no existe prohibicion de origen por nacionalidad en BAE ni ET — criterio es **funcional** (cumplimiento contractual), no geografico. Lista 6 requisitos explicitos: material ASTM A182 F53 UNS S32750 PREN>40, ANSI/ASME B16.5 Cl 900, PMI 10% espectrografico, NDE ASME B31.3, dossier con mill certificates, derecho de inspeccion ADASA en fabrica. Hallazgo documentado: Valve List Rev D (18-Mar-2026) lista todos brand/make/model como TBA — no hay supplier formal declarado. Aprobacion ADASA requiere datasheet fabricante + material certs + plan inspeccion + track record en Super Duplex. **Operating Weights:** reiterar restauracion de tabla (7 items, 34,739 lb / 15,758 kg) necesaria para fundaciones + NCh 2369 Zona 3 + lifting plan; entregar junto con Piping Layout final 24h. **Emergency Access Door:** confirmar (a) ancho final, (b) tipo (sliding vs hinged) en Equipment Layout formal. Destinatarios: TO Eduardo; CC Adzlan, Jeryl, Sadeep, Nick, Shane Banks, Farih Awang, Fadey Kassim, Andrew Zaske, Victor Gutierrez (mismo circulo que uso Eduardo). 640 palabras, 3 secciones + cierre.

---

### 2026-04-15 — Correo TM N14 — ENVIADO

**Documento:** `CORREOS/Abril 2026/2026-04-15/2026-04-15_Transmittal-N14.docx`
**Script:** `CORREOS/Abril 2026/2026-04-15/crear_correo_tm14.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-15/2026-04-15_Transmittal-N14.md`
**Respaldo:** `CORREOS/Abril 2026/2026-04-15/respaldo envio.pdf`

**Contexto:** Notificacion TM N14 (P22-TM-09-000-014-0). 11 documentos de entregas E26-E29 (08 a 15-Apr-2026). 7 Code 1, 4 Code 2. 12 observaciones previas cerradas. 5 NOTEs nuevas (2 MAJOR: PSV removal justification, analyzer voltage 220VAC vs 24VDC). 5 observaciones abiertas restantes. Deadline respuesta BW Water: 18-Apr-2026.

---

### 2026-04-15 — FINAL NOTICE Layouts, Operating Weight & Procurement Log — BORRADOR

**Documento:** `CORREOS/Abril 2026/2026-04-15/2026-04-15_Final-Notice-Layouts-Procurement.docx`
**Script:** `CORREOS/Abril 2026/2026-04-15/crear_correo_final_notice.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-15/2026-04-15_Final-Notice-Layouts-Procurement.md`

**Contexto:** Sexta comunicacion sin respuesta. TM N14 emitido hoy (12 obs cerradas) como contraste con silencio de BW Water en layouts y procurement. Tres items pendientes: (a) 6 layout documents 14 dias overdue desde 01-Apr; (b) Operating Weight Table eliminada de Rev C; (c) Procurement Log 16 lineas sin actualizar desde 06-Apr. Deadline FINAL: EOB 16-Apr-2026. Sin respuesta = formal delay notification al project sponsor bajo Contrato C-4300 el 17-Apr-2026.

---

### 2026-04-14 — Follow-Up Layouts & Operating Weight Data Required — ENVIADO

**Documento:** `CORREOS/Abril 2026/2026-04-14/2026-04-14_Follow-Up-Layouts-Weight-Table.docx`
**Script:** `CORREOS/Abril 2026/2026-04-14/crear_correo.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-14/2026-04-14_Follow-Up-Layouts-Weight-Table.md`
**Respaldo:** `CORREOS/Abril 2026/2026-04-14/respaldo envio.pdf`

**Contexto:** Quinta comunicacion sin respuesta (01, 06, 10, 13-Apr). Hallazgo nuevo: Equipment Layout Rev C (advance copy 02-Apr) elimino la Operating Weight Table que Rev A incluia (7 items, 34,739 lb / 15,758 kg). ADASA requiere pesos actualizados para: diseno de cimentaciones y OOCC, verificacion sismica NCh 2369 Zona 3, lifting plan del modulo (entregable contractual). Advance copies son copias cliente, no sustituyen submittal formal. Deadline: EOB 15-Apr. Advertencia: sin respuesta se procede con formal delay notification comunicado el 13-Apr.

---

### 2026-04-14 — Revision Ingenieria Detalle Mecanica Van Doorn (Entregas 4, 5 y 6)

**Carpeta de trabajo:** `INGENIERIA DE DETALLE MECANICA/ENTREGAS/ENTREGA 5/COMENTARIOS/`

**Documentos revisados y outputs generados:**

| Documento | Script | Output | Estado |
|-----------|--------|--------|--------|
| P22-DWG-06-009-102-C (P&ID Alimentacion) | `agregar_comentarios_pid_alimentacion.py` | `..._CC_ADASA.pdf` | Generado (4 obs) |
| P22-DWG-06-009-105-B (P&ID Reactivos) | `agregar_comentarios_pid_reactivos.py` | `..._CC_ADASA.pdf` | Generado (1 obs) |
| P22-LI-06-006-101-B (Listado Lineas) | `agregar_comentarios_lineas.py` | `..._CC_ADASA.xlsx` | PENDIENTE (cerrar Excel) |
| P22-LI-06-006-103-B (Listado Valvulas) | `agregar_comentarios_valvulas.py` | `..._CC_ADASA.xlsx` | Generado (1 obs) |
| P22-LI-06-008-101-B (Listado Instrumentos) | `agregar_comentarios_instrumentos.py` | `..._CC_ADASA.xlsx` | Generado (4 obs) |

**Hallazgos (5 observaciones):**

| OBS | Documento(s) | Observacion |
|-----|-------------|-------------|
| OBS-01 | P&ID 102-C | Volumen TK-06-002 indica 850 L en P&ID. Equipment List Rev B indica 2,000 L. Corregir en P&ID. |
| OBS-02 | P&ID 102-C | ORPIT-06-001A debe ser ORPIT-09-001A. Instrumento en suministro BW Water (area 09, no area 06). |
| OBS-03 | P&ID 102-C + LI Valvulas | Incluir valvula adicional de aislamiento cerca de VM-06-001/002 (zona tie-in con planta existente, relocalizacion VM-03-013). |
| OBS-04 | P&ID 102-C + P&ID 105-B + LI Lineas | TAG SA-HDPE-DN110-PN10-002 duplicado. P&ID 102 lo asigna a linea con destino TK-06-001; P&ID 105 lo asigna a linea con destino Fosa Drenajes. Renumerar una de las dos lineas. |
| OBS-05 | LI Instrumentos | FIT-06-005 y LS-06-002 usan area 06 pero estan instalados en modulo BW Water (area 09). CLIT-09-004/005 debe ser CIT-09-004/005 segun P&ID y documentacion BW Water. |

**Decisiones tomadas en esta revision:**
- **TK-06-002 = Fosa Drenajes (aceptado).** Van Doorn reasigno este TAG en Detalle Mecanica. En Ingenieria Basica (Nov-2024) TK-06-002 era el Estanque CIP (BW Water scope). La reasignacion es coherente con el nuevo esquema de TAGs. `generar_listado_consolidado.py` actualizado: TK-06-004 → TK-06-002 en EQUIPOS_06; referencias a "Estanque CIP TK-06-002" corregidas a TK-09-001.
- **BS-06-001 omitida en planos = cambio de ingenieria aprobado.** El drenaje de la Fosa TK-06-002 es por gravedad via linea SA-CPVC-DN200-PN10-001. No constituye hallazgo.
- **IO List area 06 = scope E&C,** fuera del alcance de Van Doorn Detalle Mecanica. Su ausencia en las entregas no es una omision de Van Doorn.

---

### 2026-04-13 — SECOND FOLLOW-UP — Outstanding Commitments | Structural Frames PO Window Closed — ENVIADO

**Documento:** `CORREOS/Abril 2026/2026-04-13/2026-04-13_Follow-Up-Outstanding-Commitments.docx`
**Script:** `CORREOS/Abril 2026/2026-04-13/crear_correo.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-13/2026-04-13_Follow-Up-Outstanding-Commitments.md`

**Contexto:** Follow-up energico al correo del 10-Apr (sin respuesta, primer dia habil lunes 13-Apr). Structural Frames PO window cerro el 10-Apr sin PO — manufactura hasta 05-May, 22 dias restantes. Layouts 12 dias overdue. Deadline duro COB 14-Apr. Clausula de escalacion: notificacion formal al project sponsor y proceso de delay notification bajo Contrato C-4300 si no hay respuesta substantiva.

---

### 2026-04-10 — RE: Outstanding Commitments — Layout Revisions & Procurement Log — ENVIADO

**Documento:** `CORREOS/Abril 2026/2026-04-10/2026-04-10_RE-Outstanding-Commitments.docx`
**Script:** `CORREOS/Abril 2026/2026-04-10/crear_correo.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-10/2026-04-10_RE-Outstanding-Commitments.md`

**Contexto:** Reply al correo del 6-Apr-2026 (sin respuesta, deadline 7-Apr incumplido). En reunion 9-Apr-2026, BW Water re-comprometio PO Log para 9-Apr y layouts para 10-Apr. Ninguno recibido. Cuarto compromiso consecutivo incumplido para layouts. Tabla procurement actualizada al 10-Apr: 8 ventanas PO cerradas sin confirmacion (eran 5 el 6-Apr). Structural Frames PO window cierra hoy — Mfg hasta 5-May, 25 dias calendario, sin margen. Accion requerida inmediata.

---

### 2026-04-06 — Outstanding Commitments — Layout Revisions & Procurement Log — ENVIADO

**Documento:** `CORREOS/Abril 2026/2026-04-06/2026-04-06_Outstanding-Commitments-Layouts-PO-Log.docx`
**Script:** `CORREOS/Abril 2026/2026-04-06/crear_correo_outstanding_commitments.py`
**Fuente:** `CORREOS/Abril 2026/2026-04-06/2026-04-06_Outstanding-Commitments-Layouts-PO-Log.md`

**Contexto:** Correo consolidado: layouts pendientes (6 docs), Procurement Log comprometido 2-Apr no entregado, analisis cruzado procurement vs Baseline Schedule (16 lineas PO). 4 POs confirmadas (25%), 5 ventanas vencidas, 3 activas cerrando esa semana. Deadline: 7-Apr-2026. Sin respuesta al 10-Apr.

---

### 2026-04-01 — Layout Revisions — Commitment Not Met — BORRADOR

**Documento:** `CORREOS/Abril 2026/2026-04-01/2026-04-01_Layout-Missed-Deadline.docx`
**Script:** `CORREOS/Abril 2026/2026-04-01/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Abril 2026/2026-04-01/2026-04-01_Layout-Missed-Deadline.md`

**Contexto:** En la reunion del 31-Mar-2026, BW Water confirmo entrega de tres layouts revisados para el 1-Apr-2026. Al cierre del dia, ningun documento fue recibido. El correo notifica formalmente el incumplimiento, lista las correcciones requeridas para cada documento y solicita nueva fecha de entrega con deadline EOB 3-Apr-2026. Se documenta el impacto en la ventana de PO para Structural Frames (6-10 Apr) y el procurement de tuberias CIP.

**Documentos comprometidos y correcciones requeridas:**
- Equipment Layout (P22-DWG-09-005-003) Rev. C: tank reubicado al lado opuesto para acceso carga quimica.
- Piping Layout (P22-DWG-09-005-004) Rev. B: CIP + antiscalant dosing en footprint unico externo ≤ 3,500 mm (TM N5 OBS-01).
- Tie-In Point Layout (P22-DWG-09-005-005) Rev. C: 5 puntos (pipe rack, acceso dosing tank, carga antiescalante directa, bridas cutover, elevacion container).

---

### 2026-03-27 — Advanced Copy Equipment Layout & Tie-In Points Rev.B — ADASA Review — BORRADOR

**Documento:** `CORREOS/Marzo 2026/2026-03-27/2026-03-27_Re-Preliminary-Layout-Review.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-27/crear_correo_re_preliminary_layout.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-27/2026-03-27_Re-Preliminary-Layout-Review.md`
**PDFs anotados:** `ENTREGAS_BWWATER/PRELIMINAR  LAYOUT/P22-DWG-09-005-003_Equipment Layout_Rev.B.pdf` y `P22-DWG-09-005-005_Tie-In Point_Rev.B.pdf`
**Script traducción:** `ENTREGAS_BWWATER/PRELIMINAR  LAYOUT/traducir_comentarios_layout.py`

**Contexto:** Eduardo Yamauchi envió el 27-Mar advanced copies de los layouts de equipos y tie-in points (Rev.B) y solicitó mover la reunión de lunes a martes por conflicto con auditoría. ADASA revisó ambos PDFs, tradujo las anotaciones existentes de español a inglés (PyMuPDF `set_info` + `update`, in-place) y preparó correo de respuesta ejecutivo.

**Observaciones Equipment Layout (P22-DWG-09-005-003):**
- Tank must be relocated to the opposite side — current position blocks chemical loading access.

**Observaciones Tie-In Point (P22-DWG-09-005-005):**
1. No space for a pipe rack — connections must come directly from the container.
2. Dosing tank has no access — relocation required.
3. Antiscalant loading must go directly to the dosing tank. No budget for a carrier pump.
4. Connection flanges for module relocation cutover are not shown.
5. Container elevation view is missing — required to confirm tie-in flange locations.

**Reunión confirmada:** Martes (31-Mar-2026) a las 8:30 AM hora Chile. Eduardo pendiente de enviar invite actualizada.

---

### 2026-03-26 — Follow-Up Spare Parts & Turbocharger Kits — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-26/2026-03-26_Follow-Up-Spare-Parts-Turbocharger.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-26/crear_correo_spare_parts_followup.py`
**Contexto:** `CORREOS/Marzo 2026/2026-03-26/2026-03-26_Follow-Up-Spare-Parts-Turbocharger.md`

**Contexto:** Follow-up ejecutivo al correo 26-Feb-2026 ("Spare Parts Quotation — Formal Re-validation & Missing Turbocharger Service Kits"), enviado como reply al hilo de notas de reunion del 26-Mar. La solicitud original tenia deadline 7-Mar-2026 — 19 dias vencida sin respuesta. Adicionalmente confirma que se espera recibir el CIP Area Layout el 27-Mar como fue comprometido.

**Items pendientes de BW Water (deadline 31-Mar-2026):**
- Re-validacion formal cotizacion Seccion 3.8 (USD 43,790 — precios sep-2025, 6+ meses sin validar)
- Kit de servicio SIP-09-001 Feed Turbocharger (ausente en Seccion 15 OT)
- Kit de servicio SIP-09-002 Inter-stage Turbocharger (ausente en Seccion 15 OT)

**Nota layout CIP:** Se recordo que se espera el layout actualizado el 27-Mar-2026 como fue comprometido por Eduardo en las notas de reunion.

---

### 2026-03-26 — Notas de Reunion BW Water (Eduardo Yamauchi) — RECIBIDAS

**Fuente:** `MINUTAS DE REUNION/RESPUESTA BW WATERS  MINUTA 26-03-26.pdf`
**Analisis comparativo:** `MINUTAS DE REUNION/REUNION 26-03-26_RESPONSE_STATUS.md`

**Contexto:** Eduardo Yamauchi respondio el mismo dia 26-Mar con notas de la reunion y status actualizado de procurement (responde al correo ADASA del 23-Mar y a los acuerdos de la reunion del 26-Mar).

**Avances confirmados por BW Water:**
- POs emitidas confirmadas: BW-PO-2026M062 (CIP Tank Heater), BW-PO-2026M073 (CIP Tank), BW-PO-2026M089 (Antiscalant Dosing Pump). Container recibido en taller Penang, Malaysia.
- Valvulas y Instrument Set: procediendo con PO a pesar de Code 3 — hold era solo por tags, sin problemas tecnicos.
- Acoples y CIP Pumps: issue tecnico resuelto (1800 psi). PO habilitada pendiente submittal formal.
- CIP Area Layout: a compartir 27-Mar-2026.
- Lead time Duplex: 4-6 semanas (no 3-4 meses como se temia). Monitoreo cercano.
- I&C Submittals (IL, IO List, CP): P&ID esperado 31-Mar. Submittals inicio semana 30-Mar/31-Mar.
- Propuesta Rev.2: aprobada tecnicamente por Aguas Antofagasta. Proximo paso: equipo financiero.

**Gaps / Items sin respuesta:**
- Structural Frames/Supports: solo "TBC" — sin datasheet. Ventana PO 6-10 Apr. CRITICO.
- CIP/Flushing Cartridge Filter: en espera de Code 1 (PT100 pendiente). Ventana PO 23-27 Mar ya vencida.
- RO Pressure Vessel: respuesta "ongoing" sin confirmar cobertura vessel housing UHPRO.
- Conductivity Meter: PO en hold (correcto) — BW Water debe presentar datasheet corregido.
- Cronograma POs actualizado: comprometido para EOD 27-Mar-2026.

---

### 2026-03-26 — Correo ADASA Respuesta BW Water — Procurement Log + Propuesta 25007-PL-0001 Rev.2 — BORRADOR

**Documento:** `CORREOS/Marzo 2026/2026-03-26/2026-03-26_Respuesta-Procurement-Layout-Proposal.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-26/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-26/2026-03-26_Respuesta-Procurement-Layout-Proposal.md`

**Contexto:** BW Water respondio el 26-Mar al correo ADASA del 23-Mar. Respuesta parcial al correo del 23-Mar: responde tablas de procurement pero ignoraba la Seccion 4 (Propuesta Layout). Ese gap fue subsanado en las notas de reunion del 26-Mar (Propuesta aprobada por Aguas Antofagasta, proximo paso finanzas).

**POs confirmados por BW Water:**
- CIP Tank Heater: BW-PO-2026M062
- Container (40'): En produccion, Malaysia workshop
- CIP / Flushing Tank: BW-PO-2026M073
- Antiscalant Dosing Pump: BW-PO-2026M089

**Puntos del correo ADASA:**
- Seccion 1 — Code 2 clarificacion: Code 2 habilita PO. CIP/Flushing Cartridge Filter (ventana 23-27 Mar) ya vencio. CIP/Flushing Pumps (cierra 31 Mar) y Feed Turbocharger (1-7 Apr) requieren PO inmediato. Deadline confirmacion: EOB 27-Mar.
- Seccion 2 — RO Pressure Vessel: respuesta "On going" no responde si vessel housing cubre UHPRO PO o requiere procurement separado.
- Seccion 3 — Structural Frames/Supports: "TBC" sin datasheet. Ventana abre 6-Apr. Deadline datasheet + fecha PO: 31-Mar.
- Seccion 4 — Propuesta 25007-PL-0001 Rev.2: Seccion 4 correo 23-Mar no respondida. Deadline EOB 25-Mar incumplido. Se reitera: (a) fecha Piping Layout Rev B + 3D Model, (b) fecha Instrument/Grounding Layout Rev B, (c) commercial close ambas fases. Nuevo deadline: EOB 27-Mar.

---

### 2026-03-23 — Correo Seguimiento Procurement Log + Propuesta 25007-PL-0001 Rev.2 — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-23/2026-03-23_Seguimiento-Procurement-Layout.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-23/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-23/2026-03-23_Seguimiento-Procurement-Layout.md`

**Contexto:** Correo semanal consolidado. Dos propositos: (1) seguimiento del log de compras segun schedule 05-Mar-2026 (commitment semanal BW Water); (2) posicion formal ADASA sobre Propuesta Rev.2 recibida 18-Mar-2026.

**Puntos clave:**
- Seccion 1 — Procurement Log semana 16-22 Mar: CIP Tank Heater y Container Code 1 (confirmar PO); Valve List y Instrument Set Code 3 (PO en hold).
- Seccion 2 — Procurement Log semana 23-29 Mar: CIP/Flushing Cartridge Filter, Pumps y Tank (Code 2/1 — confirmar fecha PO).
- Seccion 3 — Proximas semanas 30 Mar - 7 Abr: RO Pressure Vessel/Tubes (Code 1, PO 24-Feb, confirmar cobertura UHPRO); Feed Turbocharger Code 2 AN (PO puede proceder, NOTE-03 Style 77→Style S); Structural Frames/Supports (sin datasheet — PO window en 14 dias).
- Seccion 4 — Propuesta Rev.2: posicion bifasica. Fase 1 lista: Piping Layout Rev B, Tie-In Points Rev B, Equipment Layout Rev B, 3D Model. Fase 2 contingente: Instrument Layout Rev B + Grounding Layout Rev B (Code 3 TM N11 OBS-03/04).
- Reminder final: log de compras actualizado comprometido semanalmente per schedule 05-Mar — solicitar junto con respuesta.
- Deadline BW Water: EOB 25-Mar-2026.

---

### 2026-03-17 — Correo Envío Transmittal N11 (Submittals 25007-0019/0020/0021) — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-17/2026-03-17_Transmittal-N11.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-17/crear_correo_tm11.py`
**Respaldo:** `CORREOS/Marzo 2026/2026-03-17/respaldo_envio_correo_tm11.pdf`

**Contexto:** Notificacion formal de TM N11 (P22-TM-09-000-011-0) a Eduardo Yamauchi. Submittals 25007-0019, 25007-0020 y 25007-0021, 10 documentos (Entregas 19–21, recibidos 13–16 Mar). Veredicto Code 3 — To Be Revised.

**Puntos clave:**
- Reconocimiento de progreso: TM N6 OBS-01 (coupling) cerrado para HP Pump y ambos Turbos; TM N10 OBS-06/07 (vibration mounting) cerrados. Equipment List Rev B y Painting Spec Rev B aprobados. ILL Rev B cierra 8 items CCS de TM N3 (progreso reconocido).
- Bloqueante 1: Valve List Rev D requerida — 2 nuevos duplicados VE-09-007 (items 44/64) y PSV-09-002 (items 105/112); area-07 VM-07-005 persiste.
- Bloqueante 2: Grounding Layout Rev B (OBS-03) y Instrument Location Layout Rev B (OBS-04) rechazados — posiciones derivan de Piping Layout rechazado TM N7 (11,150 mm vs ≤3,500 mm TM N5). Ambos deben resubmitirse como Rev C tras aceptacion de Equipment Layout y Piping Layout.
- 6 pendientes TM N10 sin respuesta: IO List Rev C, DTL Rev B, confirmacion UPS 8h, GA Antiscalant Rev B, HMI Screenshots.
- Solicita confirmacion de recibo y schedule para resubmittals requeridos.

---

### 2026-03-17 — Respuesta BW Water a Propuesta Layout 25007-PL-0001 rev.1 — RECIBIDA

**Respaldo:** `CORREOS/Marzo 2026/2026-03-16/respaldo envio de correo propuesta de aumento v2.pdf` (hilo completo 14-17 Mar)

**Contexto:** Respuesta de Eduardo Yamauchi al follow-up ADASA del 17-Mar. BW Water acepta retirar Cable Tray Layout (sin cargo) y justifica la inclusion de Instrument Layout y Grounding Layout por dependencia tecnica con la relocalizacion CIP. Adjunta Propuesta Rev.2 directamente en el correo.

**Puntos clave:**
- Cable Tray Layout retirado del scope (sin cargo para ADASA)
- Instrument Layout y Grounding Layout: BW Water alega dependencia tecnica con relocalizacion CIP — ADASA evalua en posicion bifasica
- Propuesta Rev.2 adjunta: 6 documentos, USD 5,766, 2 semanas leadtime, mismas condiciones comerciales
- Este correo cierra el silencio posterior al 16-Mar y aporta la base para la posicion ADASA del 23-Mar

---

### 2026-03-17 — Correo Follow-Up Propuesta Layout 25007-PL-0001 rev.1 — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-17/2026-03-17_Followup-Layout-Proposal.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-17/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-17/2026-03-17_Followup-Layout-Proposal.md`

**Contexto:** Eduardo Yamauchi confirmo recibo del correo ADASA del 16-Mar y se comprometio a responder EOD ese dia. La respuesta no llego. Este correo reactiva el plazo sin nueva argumentacion: 3 parrafos, tono firme y factual.

**Puntos clave:**
- Referencia al compromiso EOD de Eduardo (16-Mar) y constata la falta de respuesta
- Reitera posicion ADASA sin cambios: 4 docs con dependencia evidente listos para cierre; 3 docs internos en espera de justificacion tecnica
- Nuevo deadline: EOD 17-Mar-2026. Sin respuesta → cierre comercial 4 docs el lunes 20-Mar-2026

---

### 2026-03-16 — Correo Envio Transmittal N10 (Submittal 25007-0018) — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-16/2026-03-16_Transmittal-N10.docx`
**Respaldo:** `CORREOS/Marzo 2026/2026-03-16/respaldo envio de correo.pdf`

**Contexto:** Notificacion formal de TM N10 (P22-TM-09-000-010-0) a Eduardo Yamauchi. Submittal 25007-0018, 6 documentos (IO List Rev B, Data Transfer List Rev A, Control Architecture Rev C, GA Antiscalant Dosing Tank Rev A, GA 1st Stage Turbocharger Rev A, GA 2nd Stage Turbocharger Rev A). Veredicto Code 3 — To Be Revised.

**Observaciones principales (7 MAJOR):**
- OBS-01: Tag inconsistency TE09-xxx vs TIT09-xxx entre IO List y DTL
- OBS-02: Rangos conductividad incorrectos para salmuera concentrada (CIT-09-001/004/005)
- OBS-03: Modbus addresses 10002.5-10002.6 reasignadas incorrectamente (faltan LS09-001/002)
- OBS-04: UPS 8-hora autonomia no confirmada textualmente en Control Architecture Rev C
- OBS-05: GA Antiscalant — notas en blanco (volumen, material, sismica) — TM N9 OBS-02 aun abierta
- OBS-06: GA SIP-09-001 — sin punto de montaje para VT09-002
- OBS-07: GA SIP-09-002 — sin punto de montaje para VT09-003
- NOTE-01/03/04: relay contact type, coupling pressure rating (ambos turbochargers)
- NOTE-05: HMI Screenshots P22-BREAD-09-008-001 comprometido pero no entregado

---

### 2026-03-16 — Correo Respuesta Propuesta Layout 25007-PL-0001 rev.1 — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-16/2026-03-16_Response-Layout-Proposal.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-16/crear_correo_layout_response.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-16/2026-03-16_Response-Layout-Proposal.md`

**Contexto:** Respuesta formal a la propuesta comercial de BW Water (25007-PL-0001 rev.1, 14-Mar-2026) que solicita USD 6,539 y 2 semanas para revisar 7 documentos de ingeniería por el cambio de ubicación del área CIP. ADASA rechaza la lógica comercial de la propuesta.

**Argumentos principales:**

- **Section 1 — Chronological Record:** Cronología documentada con respaldos: Piping Layout llegó 66 días tarde (deadline original 30-Dic-2025, recibido 06-Mar-2026). TM N5 (23-Feb-2026) estableció el límite de 3.5 m. Correo 26-Feb-2026 advirtió formalmente el problema 8 días antes de recibir el plano. Deadline correo (02-Mar) no fue cumplido por BW Water. Cable Tray Layout llegó 81 días tarde y fue aprobado sin observaciones en TM N4 (05-Feb-2026). ADASA procesó TM N7 en 48 horas.

- **Section 2 — Observations on Scope:** Acepta la necesidad de revisar Piping Layout, Tie-In Points y Equipment Layout. Impugna la inclusión de: (1) Instrument Layout, (2) Grounding Point & Power Panel Layout, (3) Cable Tray Layout P22-DWG-09-007-004 — todos aprobados, todos cubren sistemas interiores del container. CIP se reubica fuera del container. Sin justificación técnica de dependencia, su inclusión refleja un gap de coordinación interna de BW Water, no una obligación contractual de ADASA.

- **Section 3 — ADASA's Position (corregido 15-Mar-2026):** La Technical Offer Rev.1 confirmó que el CIP estará fuera del container — requisito sin cambios desde adjudicación. La oferta no definió footprint exacto ni distancias de conexión. ADASA estableció el límite de 3.5 m vía Transmittal N5 (P22-TM-09-000-005-1) el 23-Feb-2026, dos semanas antes de que BW Water entregara el Piping Layout. Ese constraint estaba por escrito. El plano entregado mostró 11,150 mm — más de tres veces el techo especificado. La revisión requerida es consecuencia de que BW Water ignoró un constraint ya formalizado. Engineering ~100 días atrasada (reconocido 12-Mar-2026). Cobrar a ADASA por corregir una entrega tardía y no conforme es inaceptable.

- **Section 4 — Request:** (a) Eliminar documentos 1/2/3 del scope o justificar con análisis de dependencias. (b) Timeline integrado al plan de recuperación general, no estimado standalone. (c) Posición comercial que refleje la responsabilidad de BW Water. Deadline propuesta revisada: 21-Mar-2026.

---

### 2026-03-13 — Correo Envío Transmittal N9 (Submittal 25007-0017) — PENDIENTE ENVIO

**Documento:** `CORREOS/Marzo 2026/2026-03-13/2026-03-13_Transmittal-N9.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-13/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-13/2026-03-13_Transmittal-N9.md`

**Contexto:** Notificacion formal de TM N9 (P22-TM-09-000-009-0) a Eduardo Yamauchi. Submittal 25007-0017, 1 documento (P&ID Rev B), veredicto Code 2 — Approved as Noted.

**Contenido:**
- Reconocimiento explicito del progreso en Rev B: cierra 13 OBS de TM N2 (Super Duplex, battery limits, TAGs, leyenda, MZE-09-001).
- NOTE-01 MINOR: codigo title block P22-DWG-09-009-02 debe ser P22-DWG-09-009-002 (3 digitos requeridos por P22).
- NOTE-02 MINOR: TK-09-002 anotado 0.27 m3 (efectivo) vs 0.34 m3 total en datasheet aceptado (TM N4). Corregir a 0.34 m3 en Rev C.
- Residual Valve List: VM-09-015 correctamente manual en P&ID (OBS-11 WITHDRAWN 05-Mar-2026), pero Valve List Rev B item 18 dice MOTORIZED — inconsistencia pendiente para Rev C.
- Pendiente: reemplazar [LINK_PLACEHOLDER] con link real antes de enviar.

---

### 2026-03-12 — Correo Escalacion Multas Engineering Delay — PENDIENTE ENVIO

**Documento:** `CORREOS/Marzo 2026/2026-03-12/2026-03-12_Escalacion-Multas-Engineering.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-12/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-12/2026-03-12_Escalacion-Multas-Engineering.md`

**Contexto:** Correo ejecutivo de escalacion a Eduardo Yamauchi + CC Andrew Zaske (VP Americas). Cuantifica formalmente las multas acumuladas por atraso en ingenieria bajo BAE Cl. 43.1.a. No activa cure period BAE 49 — warning ejecutivo previo.

**Calculos:**
- Multa diaria: 0.05% x USD 613,991 = **USD 307.00/dia**
- Inicio mora: 06-Ene-2026 (automatica per BAE Cl. 43 p.72 — sin requerimiento previo)
- Dias de atraso a 12-Mar: **65 dias**
- Acumulado a hoy: **USD 19,955 (21.7% del cap)**
- Proyeccion per BW Water Catch-Up Mar-2026 (fin 09-Jul): **USD 56,488 (61.3% del cap)**
- Cap total BAE 43.4: USD 92,098.65 (15% del contrato)

**Contenido:**
- §1 Accumulated Engineering Delay: 65 dias desde 06-Ene, ET Sec. 7 90 dias desde NTP, cita textual BAE Cl. 43 mora automatica.
- §2 Penalty Calculation (tabla): 6-Ene → hoy USD 19,955 → proyeccion BW Water USD 56,488.
- §3 Engineering Document Status (tabla): 6 documentos criticos — Valve List Rev C (Code 4), Feed TC Rev D (Code 4), Control Philosophy Rev B (Code 3), P&ID Rev B correcciones pendientes (Code 3 TM N9), Modbus TCP 75+ dias vencido, IO List vencido. 30/55 documentos aprobados.
- §4 Contractual Implications: BAE 43.4 cap 21.7% consumido; BAE 49 no activado (referencia preventiva); BAE 50 terminacion — proyeccion propia BW Water llevarıa a 61.3% del cap.
- §5 Required Actions: Valve List Rev C (16-Mar), Feed TC Rev D (25-Mar), Control Philosophy Rev B (20-Mar), Modbus TCP (14-Mar), explicacion escrita compatibilidad engineering 09-Jul vs EXW 03-Ago (16-Mar).

---

### 2026-03-11 — Envio Transmittal N7 (Submittal 25007-0014) — PENDIENTE ENVIO

**Documento:** `CORREOS/Marzo 2026/2026-03-11/2026-03-11_Transmittal-N7.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-11/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-11/2026-03-11_Transmittal-N7.md`

**Contexto:** Notificacion formal de TM N7 (P22-TM-09-000-007-0) a Eduardo Yamauchi. Submittal 25007-0014, 4 documentos, todos Code 3 — To Be Revised.

**Contenido:**
- Apertura: TM N7 adjunto, 4 docs Submittal 25007-0014, todos Code 3.
- **3 hallazgos criticos Control Philosophy Rev A (12 obs total):** UPS 30 min vs 8 h contractuales (CRITICAL); CEE/MVE no descrito — garantia contractual no verificable (CRITICAL); permisivo incorrecto — 1 DI relay contact (ADASA→modulo, habilitacion general) + 1 DO relay contact (modulo→ADASA, estado), no 2 DI individuales de tanques (MAJOR).
- **Piping Layout:** CIP y dosing a 11,150 mm (3× el limite 3.5 m de TM N5); puertas sliding y clearances de acceso ausentes.
- **Items vencidos:** Modbus Memory Map (TM N2, 65 dias); IO List (TM N3, 44 dias).
- Adjuntos: http://gofile.me/7k8qL/RHWabtKCE
- Solicitud: confirmar recibo + cronograma Rev B.

---

### 2026-03-10 — Correo interno a Ronald — Revision Control Philosophy Rev A (TM N7) — BORRADOR

**Documento:** `CORREOS/Marzo 2026/2026-03-10/2026-03-10_Revision-Control-Philosophy-Ronald.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-10/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-10/2026-03-10_Revision-Control-Philosophy-Ronald.md`

**Contexto:** Correo interno a Ronald (disciplina control/instrumentacion) con resumen ejecutivo de la revision de la Control Philosophy Rev A como parte del TM N7. Solicita validacion antes del despacho.

**Contenido (10 bullets — corregido 10-Mar-2026):**
- **3 CRITICO:** UPS 30 min vs 8h ET (no conformidad contractual); sin Pt-100 en devanados/rodamientos motores (ET §5.3); sin MVE/CEE integrado al PLC (garantia contractual no verificable en comisionamiento)
- **5 MAYOR:** Protocolo inconsistente (solo 4-20mA declarado, EtherNet/IP en Arq. Rev B, HART ausente); permisivo cliente mal definido (2 DI individuales vs 1 DI habilitacion general + 1 DO estado modulo); permisivo HP sin presion minima (riesgo cavitacion); Modbus TCP no descrita en CP; ISA 101 no declarado
- **2 MENOR:** Discrepancia tags antiscalant; codigo "BT" no definido en codificacion P22
- **Accion:** Revisar PDF comentado en COMENTARIOS/, agregar obs. disciplina si aplica, confirmar para despacho TM N7
- **Nota:** bullet "DO/DI estado y habilitacion" eliminado del correo — son pendientes del IO List (OBS-6/7 TM N3), no observaciones de la CP. Permanecen en el TM N7 como OBS-6 y OBS-7.

---

### 2026-03-06 — March 9 Meeting — EXW August 3 vs. Engineering Status: Clarification Required — PENDIENTE ENVIO v2.2

**Documento:** `CORREOS/Marzo 2026/2026-03-06/2026-03-06_Pre-Meeting-March9-Schedule-Evaluation.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-06/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-06/2026-03-06_Pre-Meeting-March9-Schedule-Evaluation.md`

**Contexto:** Correo previo a la reunion del 09-Mar-2026. BW Water entrego Baseline Schedule el 05-Mar-2026.
Analisis completo: `PROGRAMA y CONTRATO/REVISIONES/2026-03-06_Analisis-Catch-Up-Schedule-Mar2026.md`
Version v2.0 (06-Mar): tono ejecutivo confrontacional — cuestiona coherencia del schedule. Sin seccion de positivos. Sin agenda propuesta.
Version v2.1 (06-Mar): adjunto Master Deliverable Register (62 items, updated Mar 6) + oracion de enlace en body post-tabla EXW.
Version v2.2 (06-Mar): tabla procurement corregida — HP Pump Code 2-AN formal (no informal); Interstage TC agregado (Code 2-AN, PO on hold por datasheet acople); Feed TC expandido (≥2,000 psi preferido / ≥1,800 psi min + datasheet acople). 4 items totales.

**Contenido:**
- **Tabla central — EXW vs Engineering:** Engineering July 9 (+185 dias sobre baseline contractual Jan 5), General Engineering marcada completa Feb 20 (contradice 15 docs no entregados + 14 obs. abiertas), EXW agosto sin cambio y sin plan de recuperacion.
- **Tabla procurement — 4 items:** HP Pump Code 2-AN formal (PO puede proceder, nota aclaratoria 93 kW/78.5 kW/FEDCO), Interstage TC Code 2-AN PO on hold (datasheet acople: MAWP ≥1,845 psi + HPB cert. + vibration ET 5.5.7), Feed TC Code 4 PO 01-Abr (coupling 1,200 psi inaceptable 1.19x margin, Rev D ≥2,000 psi pref./≥1,800 psi min + datasheet acople), Valve List Code 4 PO 11-Mar (Rev C urgente).
- **Cierre — 3 requerimientos pre-09-Mar:** (a) explicacion como EXW agosto es sostenible + recovery plan documental; (b) estado compromisos 06-Mar (IO MODBUS, Control Arch Rev C, VFD vars) + fecha Modbus TCP Memory Map (51 dias vencido); (c) datasheet fabricante acople Interstage TC (MAWP ≥1,845 psi, HPB service cert., vibration mounting ET 5.5.7).

---

### 2026-03-05 — RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-05/2026-03-05_RE-CatchUp-Prose.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-05/crear_correo_catchup.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-05/2026-03-05_RE-CatchUp-Formal-Transmittal-Response.md`

**Contexto:** Eduardo Yamauchi respondio el 04-Mar-2026 con comentarios inline (azul) al correo ADASA de evaluacion del 17-Feb ("Catch-Up Schedule Request"). ADASA evalua cada item con posicion formal.

**Contenido:**
- **HP Pump 93 kW — CONDITIONAL:** OT Rev1 dice 86 kW (8% diferencia). Todos los documentos deben unificarse a 93 kW + calculo SEC actualizado.
- **VM-09-015 — OBS-11 WITHDRAWN:** Aceptado como valvula de aislamiento manual. Nota: Valve List Rev B item 18 la muestra MOTORIZED — inconsistencia que BW Water debe resolver en Rev C.
- **IO MODBUS list — REGISTERED:** entrega 06-Mar.
- **Control Arch Rev C + UPS — REGISTERED:** entrega 06-Mar. Rev C debe explicitar autonomia UPS ≥ 8 horas.
- **VFD electrical vars AI — REGISTERED:** entrega 06-Mar. HP Pump VFD (Fedco) + CIP Pump VFD (Grundfos).
- **Container 40ft — ACCEPTED:** revision documental pendiente.
- **SEC calc TM N3 OBS-02 — NO RESPONSE:** item critico de cumplimiento de garantia, requiere respuesta tecnica.
- **DO/DI signals TM N3 OBS-04/05 — OVERDUE:** vencio 03-Mar.
- **A/C thermal TM N4 OBS-03 — OVERDUE 15 dias:** vencio 18-Feb.

---

### 2026-03-04 — Correo Clarificacion Code 2 — Respuesta a Eduardo Yamauchi (BW Water)

**Documento:** `CORREOS/Marzo 2026/2026-03-04/2026-03-04_Clarification-Code2-Comments.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-04/crear_correo.py`
**Borrador/Contexto:** `CORREOS/Marzo 2026/2026-03-04/2026-03-04_Clarification-Code2-Comments.md`

**Motivo:** Eduardo Yamauchi (Operations Director Americas) solicito aclaracion sobre las notas de los 4 documentos con veredicto Code 2. El texto de las notas no llego claramente en la comunicacion formal.

**Respuesta preparada — 4 items:**

| # | Documento | Transmittal | Notas clave | Accion BWW pendiente |
|---|-----------|-------------|-------------|----------------------|
| 1 | Painting Spec — P22-ET-09-006-002-A | TM N1 | (a) RAL 5017 especificado vs RAL 5012 requerido ET 5.1.9; (b) DFT minimo 350µm vs 355µm requerido ET 5.1.9 | (1) Confirmar/justificar RAL 5017 o corregir a RAL 5012; (2) Actualizar DFT minimo a 355µm |
| 2 | CIP Pump DS — P22-ET-09-009-003-B | TM N2 | (a) VFD aceptado sobre DOL; (b) Motor Innomotics aceptado | Ninguna — obs. de Pt-100 (TM N3) resuelta 17-Feb-2026 |
| 3 | CIP Cartridge Filter DS — P22-ET-09-009-006-B | TM N2 | (a) 17 cartuchos aceptados; (b) Swing Bolts anotado (minor); (c) Orientacion H→V anotada (minor) | Confirmar layouts/isometrico actualizados con orientacion horizontal |
| 4 | Antiscalant Tank DS — P22-ET-09-009-010-B | TM N4 | (a) LMDPE aceptado; (b) OBS-11: actualizar P&ID (0.34 m³); (c) OBS-14: aprobacion condicional a CT-001; (d) CT-001-1 emitida 16-Feb con 4 obs abiertas — obs critica: modelo AWC no uso datos ANAM completos (Sr=0 vs 10-11 mg/L real, SiO₂ sin worst-case, metales pesados omitidos) | (1) Actualizar P&ID (0.34 m³); (2) Responder CT-001-1 con modelo AWC revisado usando datos ANAM completos — condicion OBS-14 activa |

**Estado:** LISTO (04-Mar-2026) — Item 1 actualizado (discrepancias pintura RAL+DFT); Item 4 expandido (estado CT-001-1). **Adjunto agregado:** carta 26-Feb-2026 referenciada en "Attachments:" del header y en action text Item 4 ("as documented in the attached communication"). DOCX regenerado. Pendiente envio.

---

### 2026-03-03 — Respuesta a Andrew Zaske — Reunion Reprogramada 09-Mar-2026 — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-03/2026-03-03_Re-Meeting-Rescheduled-March9.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-03/crear_correo.py`

**Contexto:** Andrew Zaske (VP Americas) respondio el 02-Mar-2026 19:54 indicando que Eduardo esta en Malasia esta semana visitando el equipo de ingenieria. Ofrecio tres opciones de reunion.

**Contenido del correo enviado:**
- Aceptacion Opcion 3: reunion reprogramada a **lunes 09-Mar-2026 a las 10:00 AM (Chile Time)**.
- Alternativa complementaria: breve call tecnica esta semana (Mie 4 o Jue 5) enfocada exclusivamente en acoples HP si hay disponibilidad tecnica sin Eduardo.
- Agenda confirmada para 09-Mar: HP Couplings, CIP External Layout, Catch-up Schedule.
- Solicitud a BW Water de confirmar fecha y enviar link Teams.

---

### 2026-03-02 — Envio Transmittal N6 (Entrega 13) + Correo Rejection Meeting — ENVIADO

**Documento:** `CORREOS/Marzo 2026/2026-03-02/2026-03-02_Transmittal-N6-Rejection-Meeting.docx`
**Script:** `CORREOS/Marzo 2026/2026-03-02/crear_correo.py`

**Contenido del correo enviado:**
- Notificacion formal de rechazo (Code 4) — Entrega 13, Transmittal N6 adjunto.
- **Critico 1 — Feed Turbocharger (Code 4):** coupling reducido de 2,000 psi a 1,200 psi es inadmisible. Margen 19% deficiente. Compromiso CCS 25007-0002 (22-Ene-2026: "BW will provide coupling rated 2000 psi") incumplido.
- **Path to resolution documentado:** upgrade Feed TC a ≥1,800 psi + datasheet del fabricante del acople (modelo, MAWP, certificacion HPB service) para SIP-09-001 y SIP-09-002 → Code 2. Solucion preferida ADASA: 2,000 psi (Piedmont Style H). Flanged CL900 o soldado disponible como ultimo recurso.
- **Nota Interstage TC (Code 2, SIP-09-002):** tambien sin datasheet del acople — debe entregarse junto con revision Feed TC.
- Incumplimiento deadline CIP tie-ins (vencio 02-Mar sin respuesta) y Catch-up Schedule (solicitado 28-Ene y 09-Feb sin entrega).
- **Reunion obligatoria:** miercoles 04-Mar-2026, 10:00 AM Chile — HP couplings, CIP tie-ins, Catch-up Schedule.

---

### 2026-02-28 — Revision Logica de Control Van Doorn Rev B

**Documento revisado:** `P22-IT-06-008-101-B (Lógica).docx` — Rev B, 22-Feb-2026 (Van Doorn)

**Metodologia:** Comparacion contra benchmark P13 (2019). Comentarios embebidos en XML Word (zipfile + lxml). Script: `INGENIERIA DE DETALLE MECANICA/ENTREGAS/ENTREGA 1/agregar_comentarios_logica.py`.

**Output:** `INGENIERIA DE DETALLE MECANICA/ENTREGAS/ENTREGA 1/P22-IT-06-008-101-B_ADASA-Review.docx`
— 11 comentarios totales: 4 Ronald Pellejero Salazar (preexistentes) + 7 Luis Rivera (ADASA)

**Herramienta de revision:** `INGENIERIA DE DETALLE MECANICA/ENTREGAS/ENTREGA 1/revisor_comentarios.html`
— Playground HTML (JSZip + DOMParser) para visualizar y agregar nuevos comentarios Word sin abrir Microsoft Word.
— Abre en Safari/Chrome, carga el DOCX, muestra highlights por autor, permite anclar nuevos comentarios a parrafos y exportar el DOCX modificado.

**7 GAPs identificados (actualizado 06-Mar-2026):**

| GAP | Parrafo | Hallazgo | Severidad |
|-----|---------|----------|-----------|
| GAP-01 | 211 — Encendido Bomba BH-06-001 | Secuencia arranque incompleta: faltan frecuencia VFD inicial, timeout presion PIT-06-001, timing pulso OI-06-003, timeout confirmacion marcha OI-06-004 | Mayor |
| GAP-02 | 219 — Parada BH-03-001 | Error de tag: BH-03-001 es del Modulo 3 (2019), tag correcto es BH-06-001. Ademas: disposicion BS-06-001, estado valvulas y timeout parada OI-06-004 no definidos | Critico |
| GAP-03 | 198 — Nivel TK-06-001 >70% | Tabla de bandas de nivel ausente: solo se define permisivo >70%. Sin rango operacional normal, umbrales alarma ni gestion desborde (~2%). P13 contemplaba 4 bandas | Mayor |
| GAP-04 | 261 — LS-00-002 / TK-00-001 | Integracion con postratamiento no documentada: sin confirmacion produccion, rol TK-00-001 no confirmado, interfaz inter-PLC sin definir | Mayor |
| GAP-05 | 236 — Lazo CTRL_BH06_001 | Lazo incompleto: sin tipo control (PI/PID), rango VFD (Hz min/max), fallback PIT-06-001, perfil rampa arranque | Mayor |
| GAP-06 | 194 — OI BW Water signals | Senal alarma falla ausente (equivalente OI-03-003 P13). Procedimiento reencendido no definido | Mayor |
| GAP-07 | 193 — Chequeo de permisivos | VM-06-001 y VM-06-002 ausentes de la logica. Valvulas manuales DN100 con finales de carrera en lineas de interconexion fuera del modulo. Permisivos requeridos: VM-06-001 CERRADA, VM-06-002 ABIERTA. Rev C debe incluir DI de posicion para ambas, criterio en tabla de arranque y alarma + bloqueo BH-06-001 si posicion incorrecta | Mayor |

---

### 2026-02-27 — TM N6 DOCX Regenerado + Verificacion 4 TAGs Duplicados

**Transmittal N6 (P22-TM-09-000-006-0) — DOCX regenerado:**
- Archivo: `REVISIONES/TRANSMITTALES/P22-TM-09-000-006-0/TRANSMITTAL N6 ADASA-BW_WATER.docx`
- Veredicto: **4 — REJECTED** | 5 Approved as noted, 2 Rejected
- **OBS-05 Ground 1 — argumentacion tecnica final:** coupling 1,200 psi (82.7 bar) es insuficiente para el circuito UHPRO. Joint 4 (Interstage TC outlet, 2da etapa) opera a 83.9 bar y Joint 5 a 82.4 bar — ambos SOBRE el rating propuesto. En Joint 2 (Feed TC outlet, 69.53 bar) el margen es solo 19% para servicio de salmuera concentrada 53,000 ppm TDS con transientes de presion. La especificacion Rev1 §13 cubre uniformemente los 6 joints del circuito UHPRO completo.
- **Estado:** GENERADO — pendiente envio a BW Water

**Verificacion completa 4 TAGs duplicados Valve List Rev B — fuente primaria:**

Verificados directamente contra `ENTREGAS_BWWATER/ENTREGA 13/P22-LI-09-005-002 - Valve List - REV.B_extracted.txt`:

| TAG | Item 1 | Item 2 | Evidencia |
|-----|--------|--------|-----------|
| **VM-09-015** | L50: item 18, DN100, Butterfly MOTORIZED, ANSI 900#, CE3MN | L75: item 43, DN15, Ball MANUAL, ANSI 900#, CE3MN | CCS "Already revised" = FALSO |
| **VE-09-008** | L76: item 44, DN80, ANSI 900#, CE3MN, Reject 1st | L89: item 57, DN80, ANSI 150#, DI/SS420, Permeate 1st | CCS "Already revised" = FALSO — materiales distintos |
| **VE-09-009** | L90: item 58, DN80, ANSI 900#, CE3MN, 2nd Stage Reject | L125: item 93, DN25, ANSI 150#, PVC, Antiscalant | NUEVO en Rev B — regresion |
| **VM-09-065** | L62: item 30, DN65, ANSI 150#, Permeate 1st | L108: item 76, DN150, ANSI 150#, PVC, CIP | NUEVO en Rev B — DN distintos |

Los 4 duplicados confirmados al 100%. TM N6 es correcto — no se requieren cambios adicionales.

---

### 2026-02-26 — Dos Correos Enviados a BW Water

**Correo 1 — Tie-ins CIP Externo (ENVIADO):**
- Archivo: `CORREOS/Febrero 2026/2026-02-26/2026-02-26_Request-Tie-in-Definition-CIP-External-Layout.docx`
- Script: `CORREOS/Febrero 2026/2026-02-26/crear_correo.py`
- Destinatario: Eduardo Yamauchi (BW Water)
- Solicita: tie-ins proceso (Feed/Permeate/Concentrate) con elevaciones, nuevos tie-ins CIP externo, footprint equipos CIP, elevaciones de referencia container
- Recordatorio incluido: P&ID Rev B (TM N2) con 13 obs abiertas — 31 dias sin respuesta
- **Deadline: lunes 2-Mar-2026**

**Correo 2 — Re-validacion Repuestos + Kits Turbocharger (ENVIADO):**
- Archivo: `CORREOS/Febrero 2026/2026-02-26/2026-02-26_Spare-Parts-Revalidation-Turbocharger-Kits.docx`
- Script: `CORREOS/Febrero 2026/2026-02-26/crear_correo_spare_parts.py`
- Destinatarios: Eduardo Yamauchi + Andrea (BW Water)
- Solicita: (1) re-validacion formal cotizacion Seccion 3.8 / Oferta BWWA Ref. 20.24.6501.F Rev.1 (USD 43,790.00 — 5+ meses sin decision), (2) kit de servicio/reparacion para SIP-09-001 (Feed Turbocharger) y SIP-09-002 (Inter-stage Turbocharger) — ausentes en Seccion 15 OT
- Hallazgo tecnico: Seccion 3.8 no contempla ningun repuesto para turbochargers de recuperacion de energia
- **Deadline: viernes 7-Mar-2026**

---

### 2026-02-25 — Alineacion NotebookLM (P22-IT-06-000-003-0)

**Documento emitido:** Technical Data Alignment: NotebookLM vs Official Project Documents

- Codigo: **P22-IT-06-000-003-0**
- Archivos: `REVISIONES/EVALUACIONES/P22-IT-06-000-003-0_Alineacion-NotebookLM.md` + `_ADASA.docx`
- Script: `REVISIONES/EVALUACIONES/crear_alineacion_notebooklm.py`

**Resultado del cruce (25 parametros verificados):**
- 25 parametros NotebookLM confirmados contra documentos oficiales — todos YES
- 10 escenarios de presion BiTurbo confirmados identicos al DS Feed TC Rev B
- Datos de permeado, recuperacion, TDS, flujos, equipos — confirmados

**Dos hallazgos criticos documentados:**
1. **HP Pump power (TM N4 OBS-08, 18 dias):** 4 valores (83.1 kW absorbido, 87 kW motor input, 90 kW VFD rated, 93 kW nameplate) son fisicamente distintos. NotebookLM usa 83.1 kW correctamente para SEC. BW Water debe unificar con nota de contexto.
2. **SEC calculation (TM N3 OBS-02, 28 dias):** SEC a 43k TDS = 4.84 kWh/m³ (Y0), 5.09 kWh/m³ (Y5) — excede garantia 4.71 kWh/m³. Condicion de referencia del claim 3.98 kWh/m³ no formalizada en Process Calc Rev B.

---

### 2026-02-23 — Transmittal N5 Rev 1 EMITIDO + Skill v7.3 + Correo Preparado

**Transmittal N5 Rev 0 (P22-TM-09-000-005-0) — EMITIDO:**
- Submittal 0012 (20-Feb-2026) — 1 documento: P22-DWG-09-005-003-A Equipment Layout of RO Container
- Veredicto: **3 — TO BE REVISED**
- OBS-01 original: CIP system dentro del container — contradice Oferta Rev.1 (corregido en Rev 1)
- 6 observaciones nuevas (1 CRITICAL, 3 MAJOR, 2 MINOR)
- 8 observaciones pendientes de TMs anteriores (mas antigua: 48 dias, TM N2)
- Positivo: container 40ft confirmado — cierra OBS-10 de TM N4

**Transmittal N5 Rev 1 (P22-TM-09-000-005-1) — EMITIDO MISMO DIA:**
- Eduardo (BW Water) confirmo por escrito que CIP y dosing systems estan fuera del container
- OBS-01 actualizado: `CRITICAL` → `MAJOR`. Nueva descripcion: "External CIP Equipment Footprint Not Defined"
- Requerimientos ADASA: footprint ancho container × max 3.5m; infraestructura LQ alineada al lado especificado; disposicion especifica de cada elemento (estanque, bomba, filtro, dosificacion)
- Cajetin de revisiones actualizado (fila Rev 1 insertada, header "Revision N°: 1" actualizado)
- Archivo: `REVISIONES/TRANSMITTALES/P22-TM-09-000-005-1/TRANSMITTAL N5 Rev 1 ADASA-BW_WATER.docx`

**Template ADASA v7.3 — ACTUALIZADO:**
- SKILL.md ahora autocontenido: no requiere CLAUDE.md del proyecto para operar
- Nueva seccion "Actualizacion de Revisiones" con patron completo cajetin + header (2 pasos)
- Nueva seccion "Dos Metodos de Generacion" (Metodo A md_to_adasa_docx.py, Metodo B script Python)
- Reglas criticas documentadas: NO numeros manuales en headings, NO page breaks extra, NO TOC manual
- Bug corregido en SKILL.md: ejemplo avanzado usaba numeros manuales en headings
- CHANGELOG.md actualizado con v7.2 y v7.3

**Correo ejecutivo TM N5 — ENVIADO 26-Feb-2026:**
- Archivo: `CORREOS/Febrero 2026/2026-02-23/2026-02-23_Transmittal-N5-Equipment-Layout.docx`
- Destinatario: Eduardo Yamauchi (BW Water)

**Schedule Eduardo (compromiso reunion 18-Feb):**
- Schedule preliminar 19-Feb: NO RECIBIDO
- Schedule final 23-Feb: NO RECIBIDO — **VENCIDO HOY**

---

### 2026-02-18 — Reunion de Coordinacion BW Water / ADASA

**Participantes:** Luis Rivera (ADASA, lider de proyecto), Ronald (equipo tecnico ADASA), Eduardo Yamauchi (BW Water, gestion), Nick (soporte tecnico vendor)

**Contexto:** Reunion post-evaluacion BWW 17-Feb. ADASA mantuvo posicion firme sobre PT100 mandatorios y condicionamiento de POs a documentacion aprobada.

**Decisiones tecnicas:**

| Tema | Resultado |
|------|-----------|
| PT100 sensores | Exigencia mandatoria reafirmada. Sin negociacion posible |
| POs Bomba / Turbo | Bloqueadas hasta entrega set documental corregido + aprobacion ADASA |
| Ethernet IP PLC↔VFD | Ratificado como protocolo de comunicacion entre PLC y variadores de frecuencia |
| CIP system | Confirmado externo al container. Vendor enviara plano layout actualizado |
| Cronograma abril | Rechazado. ADASA exigio actualizacion de hitos para recuperar ritmo |
| Margen operacional Turbo | 10% mantenido como requisito |
| I/O digitales planta | ADASA formalizo requisito de E/S para senales externas de parada segura |
| HMI variables | Voltaje, corriente y potencia requeridos para calculo consumo especifico (Ronald) |
| Dosificacion antiescalante | Preocupacion por caracterizacion de metales. Bomba de dosificacion debe ser correcta |
| Facturacion parcial | ADASA ofrecio revisar hitos cumplidos para autorizar pago parcial — post-recepcion docs |

**Compromisos formalizados:**

| Responsable | Accion | Fecha |
|-------------|--------|-------|
| Eduardo / Nick | Set documental corregido Bomba + Turbo para liberar POs | Inmediato |
| Eduardo | Schedule preliminar | 19-Feb-2026 |
| Eduardo | Schedule final (post-reunion ACES) | 23-Feb-2026 |
| Vendor | I/O List actualizada: senales Ethernet IP + digitales de parada | Proxima sesion |
| ADASA | Revision entregables aprobados para facturacion parcial | Post-recepcion docs |

**Archivo fuente:** `MINUTAS DE REUNION/REUNION 18-02-26.md`

**Nota tecnica — Ethernet IP vs Modbus TCP Map:** La confirmacion de Ethernet IP aplica al protocolo PLC↔VFD (bus de campo interno). El Modbus TCP Memory Map pendiente de TM N4 OBS-04 es distinto: es la interfaz de comunicacion del PLC con sistemas externos (SCADA/HMI corporativo). Ambas obligaciones siguen vigentes.

---

### 2026-02-17 — Respuesta Inline BWW a Evaluacion ADASA

**Recibido de BW Water (Eduardo Yamauchi, 17-Feb-2026):**
BWW respondio inline al correo ADASA "RE: Catch-Up Schedule Request — Overdue Response Required".

| Categoria | Detalle |
|-----------|---------|
| **Items Aceptados (6)** | Pt-100, Vibration TX, FIT-09-002, A/C n+1, EXW Penang, No POs antes de aprobacion |
| **Criticos diferidos (2)** | Modbus TCP Map ("will address later"), Container 60ft (posicion parcial, sin docs corregidos) |
| **Disputa tecnica (1)** | VM-09-015: BWW sostiene que ET 5.2.3 no aplica ("not a process relevant valve") |
| **Deferrals (4)** | HP Pump power, OBS-04/05 senales externas, cobertura parcial 16/27 obs |
| **No abordados (11)** | Observaciones restantes TM N3 y N4 |

**Nota reunion 18-Feb:** BWW confirma reunion pero alerta que equipo en Asia puede no asistir por Año Nuevo Chino (posible retraso 1 dia).

**Impacto en evaluacion P22-IT-06-000-001-0:**
Documento actualizado (18-Feb) con nueva seccion "BWW RESPONSE TO ADASA EVALUATION — FEB 17, 2026" que registra verbatim/resumidas las respuestas y actualiza el estado de cada item.

**Script regenerado:** `REVISIONES/EVALUACIONES/crear_evaluacion.py`

---

### 2026-02-17 — Acuse Recibo Respuestas BWW + Evaluacion + Agenda Reunion

**Respuestas recibidas de BW Water (16-Feb-2026):**
- Respuestas parciales a TM N3 (6/17 observaciones), TM N4 (5/10 observaciones), y schedule
- Items aceptados: Pt-100, vibration transmitters, FIT-09-002, A/C n+1, EXW Penang, no POs antes de aprobacion
- Items insuficientes: Modbus Map (programa no iniciado), Container 60ft (under review 3 meses), VM-09-015, VFD variables
- Items no abordados: HP Pump power, UPS, duplicate TAGs Valve List, area codes, Equipment List discrepancies

**Documentos generados (17-Feb-2026):**

| # | Tipo | Archivo | Codigo |
|---|------|---------|--------|
| 1 | Correo | `CORREOS/Febrero 2026/2026-02-17/2026-02-17_Acuse-Recibo-Respuestas-BWW.docx` | -- |
| 2 | Evaluacion | `REVISIONES/EVALUACIONES/2026-02-17_Evaluacion-Respuestas-BWW_ADASA.docx` | P22-IT-06-000-001-0 |
| 3 | Registro DOCX | `REVISIONES/EVALUACIONES/P22-IT-06-000-002-0_Document-Status-Register_ADASA.docx` | P22-IT-06-000-002-0 |
| 4 | Registro Excel | `REVISIONES/EVALUACIONES/P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx` | P22-IT-06-000-002-0 |

**Scripts generadores:**
- `CORREOS/Febrero 2026/2026-02-17/crear_correo.py`
- `REVISIONES/EVALUACIONES/crear_evaluacion.py`
- `REVISIONES/EVALUACIONES/crear_registro.py`
- `REVISIONES/EVALUACIONES/generar_excel_registro.py`

**Registro P22-IT-06-000-002-0 - Document Status Register:**
- 62 items totales (39 entregados + 23 no entregados)
- Cruce verificado contra ET Sec 7 (obligaciones contractuales)
- Incluye tabla de nomenclatura de veredictos (1, 2-AN, 3, 4, --)
- Excel con Legend sheet para codigos de veredicto

**Reunion confirmada:** 18-Feb-2026, 9 AM EST (11 AM Chile). Agenda de 5 temas (1 hora).

---

### 2026-02-16 — Evaluacion Respuesta CT-001 (Dosificacion Antiescalante)

**Respuesta recibida de BW Water (13-Feb-2026):**
- 3 documentos: Memorando BW Water, AWC Projection (Pureflux SW), Email CREST Water
- Respuesta 3 dias despues del deadline (10-Feb-2026)

**Evaluacion realizada (16-Feb-2026):**
- **Conclusion general:** 0.5 ppm Pureflux SW es aceptable segun proyeccion AWC
- **4 observaciones identificadas:**
  - OBS-1 (Major): Proyeccion AWC a 19°C, worst-case es 24°C (ET Tabla 4-1)
  - OBS-2 (Minor): Inconsistencia interna Chemical Consumption List (0.02 L/h vs 0.59 kg/day)
  - OBS-3 (Major): CREST Water afirma ausencia de metales pesados, pero ANAM Lab SI los incluye (Sr 10-11 mg/L)
  - OBS-4 (Major): AWC vs CREST Water contradictorios, sin posicion definida por BW Water

**Archivos generados:**
- `REVISIONES/CONSULTAS_TECNICAS/P22-CT-09-000-001-1_Evaluacion-Respuesta-Antiescalante.md` (fuente)
- `REVISIONES/CONSULTAS_TECNICAS/P22-CT-09-000-001-1_Evaluacion-Respuesta-Antiescalante_ADASA.docx` (DOCX)
- `REVISIONES/CONSULTAS_TECNICAS/crear_evaluacion_ct001.py` (script generador)

**Deadline BW Water:** 20-Feb-2026 (cierre anti-escalamiento)

---

### 2026-02-10 — Analisis Programa BW Water Feb-2026 + Correo Respuesta

**Respuesta recibida de BW Water (09-Feb-2026):**
- Eduardo Yamauchi envia programa general actualizado ("Taltal water treatment plant base schedule 090226.pdf")
- Indica que el schedule de documentos "still being worked on"
- Archivo respuesta: `CORREOS/Febrero 2026/2026-02-09/RESPUESTA/RE Catch-Up Schedule Request - Overdue Response Required.txt`

**Analisis realizado (10-Feb-2026):**
- Analisis comparativo de 3 programas (BW Oct-2025, BW Feb-2026, ADASA Ene-2026)
- Cruce completo de entregables de ingenieria vs fechas de procurement
- 5 incoherencias criticas identificadas: HP Pump, instrumentos, valvulas, antiescalante, MCC panel
- Archivo: `PROGRAMA y CONTRATO/REVISIONES/2026-02-10_Analisis-Comparativo-Programas-BW-Water.md`

**Correo preparado (10-Feb-2026):**
- Acuse de recibo + observaciones del programa + todas las incoherencias + requerimientos pendientes
- Deadline: 13-Feb-2026 (viernes)
- Archivo: `CORREOS/Febrero 2026/2026-02-10/2026-02-10_Respuesta-Schedule-BW-Water.md`
- DOCX: `CORREOS/Febrero 2026/2026-02-10/2026-02-10_Respuesta-Schedule-BW-Water.docx`
- Estado: **ENVIADO (10-Feb-2026)**
- Validado contra PROMPT_ANALITICA_HUMANA v4.10 (todas las oraciones <40 palabras, burstiness CV=0.67)

**Plan de Escalamiento preparado (10-Feb-2026):**
- Plan de 3 fases si BW Water no responde al deadline 13-Feb
- Fase 1 (14-Feb): Correo ejecutivo a Eduardo Yamauchi + CC Andrew Zaske (VP Americas)
- Fase 2 (20-Feb): Notificacion formal incumplimiento BAE 49 (10 dias para subsanar)
- Fase 3 (~03-Mar): Evaluar terminacion segun BAE 50
- Archivos: `CORREOS/Febrero 2026/2026-02-14_Escalation-Plan/`
- Incluye script Python para generar notificacion formal ADASA DOCX

---

### 2026-02-09 — Seguimiento Catch-Up Schedule + Respuesta BW Water

**Enviado por ADASA:** Seguimiento catch-up schedule vencido (deadline original 06-Feb-2026)
- Archivo: `CORREOS/Febrero 2026/2026-02-09/2026-02-09_Seguimiento-Catch-Up-Schedule.md`

**Recibido de BW Water (mismo dia, 23:38):** Programa general actualizado
- Eduardo Yamauchi adjunta "Taltal water treatment plant base schedule 090226.pdf"
- No incluye schedule de documentos ("team is still working on it")
- Archivo PDF: `PROGRAMA y CONTRATO/pdf/Taltal water treatment plant base schedule 090226.pdf`

---

### 2026-02-05 — ENVIO Transmittal N4 + Consulta Tecnica CT-001 a BW Water

**ENVIO REALIZADO - Documentos entregados a BW Water Americas Inc.**

**Correos enviados:**

| # | Documento | Destinatario | Estado |
|---|-----------|--------------|--------|
| 1 | **Transmittal N4** (P22-TM-09-000-004-0) | Marjan Fariborz / Logan Maroney | **ENVIADO** |
| 2 | **Consulta Tecnica CT-001** (P22-CT-09-000-001-0) | Marjan Fariborz / Logan Maroney | **ENVIADA** |
| 3 | **Correo ejecutivo** (acompana TM N4) | Marjan Fariborz / Logan Maroney | **ENVIADO** |

**Archivos de respaldo (.eml):**
```
CORREOS/Febrero 2026/2026-02-05/
├── 2026-02-05_Transmittal-N4-Revision-Tecnica-E10-E11.eml    # Correo ejecutivo
├── 2026-02-05_Technical-Query-Antiscalant-Dosing.eml         # Consulta CT-001
└── 2026-02-05_Transmittal-N4-Attachments.eml                 # TM N4 con adjuntos
```

**Contenido enviado:**

**Transmittal N4 (P22-TM-09-000-004-0):**
- 4 documentos revisados (E10 + E11)
- Veredicto: 3 - TO BE REVISED
- 8 observaciones criticas (7 heredadas de TM N2/N3 + 1 nueva)
- 4 adjuntos con comentarios ADASA (PDFs)

**Consulta Tecnica CT-001:**
- Tema: Dosificacion antiescalante 0.5 ppm para LSI 2.0-2.11
- Deadline respuesta: 10-Feb-2026 (VENCIDA - 2 dias)
- Vinculada a aprobacion del Antiscalant Dosing Tank

**Hallazgos criticos destacados:**
- PLC 60Hz (violacion ET 5.4.7)
- A/C sin n+1 (30 dias pendiente desde TM N2)
- Modbus TCP Map no entregado (30 dias pendiente)
- Container >40ft (rechazado Nov-2025, +USD $67,208)

**Estado post-envio:**
- TM N4: **ENVIADO** - A la espera de respuesta BW Water
- CT-001: **ENVIADA** - Deadline 10-Feb-2026 VENCIDA
- Catch-up Schedule: Pendiente respuesta (solicitado 28-Ene, deadline 06-Feb)

---

### 2026-02-05 — Skill template-adasa v7.2 + Consulta Tecnica CT-001 (Preparacion)

**Trabajo realizado:**

1. **Skill template-adasa actualizada a v7.2:**
   - Creado `config_defaults.py` - Configuracion centralizada
   - Creado `table_utils.py` - Funciones reutilizables para tablas
   - Creado `ejemplo_documento.py` - API programatica con TOC automatico
   - Parametro `incluir_toc` para control por tipo de documento

2. **Consulta Tecnica CT-001 preparada:**
   - Archivo: `REVISIONES/CONSULTAS_TECNICAS/P22-CT-09-000-001-0_Consulta-Dosificacion-Antiescalante.md`
   - DOCX generado con skill template-adasa

3. **Transmittal N4 regenerado** con TOC automatico

---

### 2026-02-03 — Preparacion Transmittal N4 (E10 + E11) - BORRADOR
**Archivos:**
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-004-0/TRANSMITTAL N4 ADASA-BW_WATER.docx` (BORRADOR)
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-004-0/P22-TM-09-000-004-0_TRANSMITTAL.md`
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-004-0/2026-02-03_Compilado-Revision-Entregas-10-11.md`
- `REVISIONES/SUBMITTALS/25007-0010/2026-02-02_Revision-Tecnica-Entrega-10.md`
- `REVISIONES/SUBMITTALS/25007-0011/2026-02-03_Revision-Tecnica-Entrega-11.md`
- `ENTREGAS_BWWATER/ENTREGA 11/md/` (3 archivos .md extraidos)
- `CORREOS/Febrero 2026/2026-02-03/2026-02-03_Transmittal-N4-Revision-Tecnica-E10-E11.docx` (BORRADOR)
- `CORREOS/Febrero 2026/2026-02-03/2026-02-03_Transmittal-N4-Revision-Tecnica-E10-E11.md`

**Estado:** BORRADOR - Pendiente revision final y envio

**Contenido:** Transmittal N4 preparado cubriendo Submittals 0010 + 0011 (E10 + E11, 4 documentos). Incluye seccion especial "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS" con trazabilidad de dias pendientes.

**Documentos Revisados:**
| # | Codigo | Titulo | Rev | Veredicto |
|---|--------|--------|-----|-----------|
| 1 | P22-LI-09-009-001 | Utility Consumption List | A | **3 - To be revised** |
| 2 | P22-ET-09-009-010 | Antiscalant Dosing Tank DS | B | 2 - Approved as noted |
| 3 | P22-CD-09-004-001 | Control System Architecture | B | 2 - Approved as noted |
| 4 | P22-DWG-09-007-004 | Cable Tray Layout | A | **3 - To be revised** |

**Hallazgos CRITICOS (7 total):**
- **OBS-01:** PLC especificado a 60Hz viola ET 5.4.7 (Chile usa 50Hz) - NEW
- **OBS-02:** Solo 1 A/C, ET requiere n+1. **Pendiente 29 dias desde TM N2**
- **OBS-03:** Falta memoria calculo termico A/C. **Pendiente 29 dias desde TM N2**
- **OBS-04:** Modbus TCP Map no entregado. **Pendiente 38 dias desde TM N2**
- **OBS-05:** TAG duplicado FIT-09-001 en Cable Tray Layout. **Pendiente 7 dias desde TM N3**
- **OBS-06:** Faltan ubicaciones vibration transmitters (ET 5.5.7). **Pendiente 7 dias desde TM N3**
- **OBS-07:** Faltan ubicaciones Pt-100 motores (ET 5.3). **Pendiente 7 dias desde TM N3**

**Hallazgos MAYORES (3 total):**
- **OBS-08:** HP Pump 4 valores diferentes (83/86/92/93 kW)
- **OBS-09:** UPS no incluido en BOM Control System
- **OBS-10:** CIP Pump 11 kW vs 15 kW Oferta (27% discrepancia)

**POSITIVOS:**
- SEC 3.98 kWh/m3 cumple garantia (4.71 kWh/m3) con 15% margen
- Control System Architecture cumple ET 5.4 (PLC, HMI, Modbus Gateway)

**Veredicto Final:** **3 - TO BE REVISED**

---

### 2026-02-02 — Revision Tecnica Entrega 10 (preliminar)
**Archivos:**
- `REVISIONES/SUBMITTALS/25007-0010/2026-02-02_Revision-Tecnica-Entrega-10.md`
- `CORREOS/Febrero 2026/2026-02-02/2026-02-02_Transmittal-N4-Revision-Tecnica-E10.md` (obsoleto - reemplazado por 03-Feb)

**Contenido:** Revision tecnica inicial de E10 (2 documentos). Posteriormente integrada en TM N4 junto con E11.

---

### 2026-01-29 — Analisis Comparativo de Programas + Solicitud Revised Schedule
**Archivos:**
- `PROGRAMA y CONTRATO/REVISIONES/2026-01-29_Solicitud-Revised-Schedule-BW-Water.md`

**Contexto:** Se realizo analisis comparativo entre el programa BW Water (Oct-2025) y el programa ADASA actualizado (Ene-2026). Se identifico discrepancia de 80 dias en fecha de entrega y 2.5 meses en comisionamiento.

**Hallazgos principales:**
- BW Water: Ready to Ship 03-Ago-2026, Comisionamiento 26-Sep-2026
- ADASA: Entrega 22-Oct-2026, Comisionamiento 07-Dic-2026
- Tránsito EXW Malasia-Taltal: 40-50 dias (no considerado por BW Water)

**Trazabilidad:** Se documenta que el 28-Ene-2026 se solicito catch-up schedule manteniendo fecha 03-Ago-2026. A la espera de respuesta BW Water.

---

### 2026-01-29 — Respuesta Cambio PM + Mensaje a Eduardo Yamauchi
**Archivos:**
- `CORREOS/Enero 2026/2026-01-29/2026-01-29_Respuesta-Cambio-PM-BW-Water.md`
- `CORREOS/Enero 2026/2026-01-29/crear_correo.py`
- `CORREOS/Enero 2026/2026-01-29/2026-01-29_Respuesta-Cambio-PM-BW-Water.docx`

**Contexto:** BW Water notifica cambio de Project Manager. Eduardo Yamauchi reemplaza a Marjan Fariborz/Logan Maroney como PM principal. Marco Arsovic (Head of Engineering) permanece involucrado durante periodo de handover de 2 semanas.

**Contenido del correo:**
- **Parte 1 (a Marco):** Acuse de recibo del cambio de PM, confirmacion de que ADASA esta OK con la transicion
- **Parte 2 (a Eduardo):** Bienvenida + contexto inmediato sobre el retraso de 23 dias + referencia al correo enviado ayer (Transmittal N3 + Catch-Up Request) + solicitud de priorizar respuesta

**Tono aplicado:** Cordial pero directo, sin minimizar la gravedad del retraso pero sin dramatismo. Aplicacion de PROMPT_ANALITICA_HUMANA v4.10.

**Contacto nuevo:**
- **Eduardo Yamauchi** - Project Manager, BW Water Americas Inc. (eduardo.yamauchi@bw-water.com)

---

### 2026-01-28 — Revision Tecnica Cruzada Valve List y Equipment List
**Archivos:**
- `REVISIONES/SUBMITTALS/25007-VALVELIST/2026-01-28_Revision-Tecnica-Cruzada-ValveList-EquipmentList.md`
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/P22-TM-09-000-003-0_TRANSMITTAL.md` (actualizado)
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/TRANSMITTAL N3 ADASA-BW_WATER.docx` (regenerado)

**Metodologia aplicada:** Revision cruzada de 109 valvulas y 13 equipos vs P&ID y requisitos ET.

**Hallazgos principales:**

| Documento | Veredicto | Hallazgo Critico |
|-----------|-----------|------------------|
| **Valve List** | **3 - TO BE REVISED** | VM-09-015 DN100 ANSI 900# manual viola ET 5.2.3 |
| **Equipment List** | 2 - APPROVED AS NOTED | Discrepancias menores vs P&ID |

**Observaciones Valve List (5 total):**
- **OBS-VL-01 (CRITICO):** VM-09-015 DN100 Butterfly en descarga HP Pump es manual. ET 5.2.3 requiere actuacion electrica para valvulas DN50+ en lineas de proceso ANSI 900#
- **OBS-VL-02/03/04 (MAYOR):** TAGs duplicados: VE-09-008, VM-09-015, VE-09-010
- **OBS-VL-05 (MENOR):** TAGs con area incorrecta (VM-07-005, VM-07-031, VE-07-009 deberian ser area 09)

**Criterio ET 5.2.3 aplicado:**
- Valvulas DN50+ en ANSI 900# (lineas de proceso): DEBEN ser electricas
- Valvulas DN15-DN25 en ANSI 900# (venteos/drenajes): Manual aceptable
- 32 valvulas DN15 manuales en ANSI 900# clasificadas como venteos/drenajes: ACEPTABLE

Transmittal N3 actualizado con observaciones #11-14 y acciones Group D (#10-14) y Group E (#15-16).

### 2026-01-27 — Revision Tecnica Temperatura Bombas
**Archivos:**
- `REVISIONES/SUBMITTALS/25007-HPPUMP/2026-01-27_Revision-Tecnica-Temperatura-Bombas.md`
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/P22-TM-09-000-003-0_TRANSMITTAL.md` (actualizado)
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-003-0/TRANSMITTAL N3 ADASA-BW_WATER.docx` (regenerado)

Revision tecnica cruzada identifico 5 observaciones sobre medicion de temperatura en bombas:
- **3 CRITICAS:** Pt-100 faltantes en devanados de motores HP y CIP, RTDs faltantes en Bomba CIP
- **1 MAYOR:** Switches digitales (TSH) en lugar de transmisores 4-20mA+HART
- **1 MENOR:** Documentacion incompleta en Instrument List

Transmittal N3 actualizado con observaciones OBS-TEMP-06 a OBS-TEMP-09 y acciones #6-9.

### 2026-01-26 — Emision Transmittal N2
**Archivos:**
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-002-0/P22-TM-09-000-002-0_TRANSMITTAL_ADASA.docx`
- `CORREOS/Enero 2026/2026-01-26/2026-01-26_Technical-Review-Transmittal-N2.md`
- `CORREOS/Enero 2026/2026-01-26/2026-01-26_Technical-Review-Transmittal-N2.docx`

Transmittal N2 emitido a BW Water cubriendo Submittals 0003-0007 (E3-E7, 8 documentos). Process Calculation Rev B valida diseno. Acciones criticas pendientes: A/C thermal load y Static Mixer material.

### 2026-01-12 — Transmittal N2 Preliminar
**Archivos:**
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-002-0/P22-TM-09-000-002-0_TRANSMITTAL.md`

Version preliminar preparada, pendiente Process Calculation.

### 2026-01-09 — Respuesta a BW Water
**Archivo:** `CORREOS/Enero 2026/2026-01-09/2026-01-09_Respuesta-Estado-Documentos-BW-Water.docx`

Correo confirmando fechas comprometidas y priorizando Process Calculation como documento critico.

### 2026-01-06 — Seguimiento Transmittal N1
**Archivo:** `CORREOS/Enero 2026/2026-01-06/2026-01-06_Seguimiento-Transmittal-N1.md`

Correo solicitando confirmacion de recepcion TM N1 y fechas de re-envio.

### 2026-01-01 — Recepcion Entregas 7, 8 y 9
**Archivos:**
- `ENTREGAS_BWWATER/ENTREGA 7/` - 6 docs (Process Calc Rev B, HP Pump, etc.)
- `ENTREGAS_BWWATER/ENTREGA 8/` - 12 docs (PFD Rev B, Container, Turbochargers, Listas)
- `ENTREGAS_BWWATER/ENTREGA 9/` - 5 docs (Cables, Conduit, Layouts)

Process Calculation Rev B con modelacion completa de turbochargers recibido. Entregas 8 y 9 pendientes de revision.

### 2025-12-31 — Aprobacion Valvulas KSB
**Archivos:**
- `COMPRA EQUIPOS/COMPRA DE VALVULAS/2025-12-31_Revision-Oferta-KSB-Rev1.md`

Oferta KSB CV421060 Rev.1 aprobada con 100% cumplimiento tecnico.

### 2025-12-16 — Emision Transmittal N1
**Archivo:** `REVISIONES/TRANSMITTALES/P22-TM-09-000-001-0/TRANSMITTAL N1 ADASA-BW_WATER.pdf`

Transmittal N1 emitido cubriendo Entregas 1 y 2 (20 documentos).

## Referencias Durables

> Información estable del proyecto (no cronológica). La trazabilidad de eventos vive en la Bitácora Cronológica; los índices de esta sección son tabulares (una fila por ítem), no narrativos.

### Información del Proyecto

#### Resumen Ejecutivo

| Campo | Valor |
|-------|-------|
| **Proyecto** | BAE 12803 - PLANTA MODULAR |
| **Contrato** | C-4300 |
| **Cliente** | ADASA (Aguas de Antofagasta S.A.) |
| **Proveedor** | BW Water Americas Inc. |
| **Ubicacion** | Planta Desaladora Taltal, Region de Antofagasta, Chile |
| **Industria** | Tratamiento de agua / Desalinizacion / Gestion de salmuera |

#### Objetivo Tecnico
Suministrar un Modulo de Osmosis Inversa UHPRO (Ultra High Pressure Reverse Osmosis) que:
- Desaliniza la salmuera proveniente del modulo de OI existente (11 lps de produccion)
- Produce 5.5 lps adicionales de permeado (equivalente a 480 m3/dia)
- Incrementa la recuperacion total de la planta

#### Datos del Contrato C-4300

| Campo | Valor |
|-------|-------|
| **Monto Total** | USD 613.991,00 |
| **Modalidad** | EXW (Ex Works) |
| **Duracion** | 510 dias corridos **desde la Notificacion de Adjudicacion**, no desde la firma (BAE Clausula 27) |
| **Notificacion de Adjudicacion (NTP)** | 07-Oct-2025 — ancla de los 300 dias del Plazo de Entrega y de los 510 del Plazo Contractual |
| **Fecha Firma** | 10-Nov-2025 |
| **Recepcion Provisional (fin del Plazo Contractual)** | **01-Mar-2027** (NTP + 510 dias corridos) |
| **Garantia Fiel Cumplimiento** | 15% = USD 92.098,65 |
| **Garantia Tecnica** | 10% = USD 61.399,10 (24 meses) |
| **Limite Multas** | 15% del monto neto |

#### Multas Principales
| Concepto | Multa Diaria |
|----------|--------------|
| Atraso ingenieria/documentos | 0,05% |
| Atraso entrega suministro (EXW) | 0,2% |
| Atraso Comisionamiento/PEM | 0,1% |
| Otros incumplimientos | 0,05% |

#### Clausulas de Terminacion
- Atraso > 30 dias en entrega suministro
- Multas acumuladas > 15% del monto neto
- Incapacidad manifiesta del proveedor

#### Garantias de Desempeno (ET Sec. 10.1)
| Parametro | Valor Garantizado |
|-----------|-------------------|
| Capacidad Nominal | 480 m3/dia (20 m3/h) |
| TDS Permeado | <= 500 mg/l |
| Cloruros Permeado | <= 400 mg/l |
| SEC (Consumo Energetico) | 4.71 kWh/m3 +/- 5% |

#### Equipos Principales

##### Suministro BW Water (Area 09)
| TAG | Equipo | Potencia |
|-----|--------|----------|
| BH-09-001 | Bomba Alta Presion | 225 kW |
| BH-09-002 | Bomba CIP | 11 kW |
| SIP-09-001/002 | Turbochargers (ERD) | - |
| BOI-09-001/002 | Racks OI (1ra y 2da Etapa) | - |
| TK-09-002 | Estanque CIP | - |
| LCP | Panel de Control Local | - |

##### Suministro ADASA (Area 06)
| TAG | Equipo | Potencia |
|-----|--------|----------|
| TK-06-001 | Estanque Salmuera | - |
| BH-06-001 | Bomba Alimentacion | 11 kW |
| BS-06-001 | Bomba Sumergible | 3 kW |

---

### Estructura del Repositorio

```
MODULO DE SALMUERA TALTAL/
├── .claude/skills/                 # Skills de Claude Code
│   ├── template-adasa/             # Template corporativo ADASA v7.3 — archivo real: ejemplo_documento.py
│   ├── large-pdf-reader/           # Lector de PDFs grandes v5.0
│   ├── doc-annotator/              # Anotaciones PDF (FreeText + visual) y comentarios Word v1.0
│   ├── anti-ia/                    # Escritura analitica y evaluacion de textos IA v5.0
│   └── canvas-design/              # Generacion de diagramas y arte visual
│
├── CORREOS/                        # Comunicaciones del proyecto
│   ├── [Mes YYYY]/YYYY-MM-DD/      # Correo SALIENTE por fecha (ver CLAUDE.md 3.4)
│   ├── _RECIBIDOS/                 # Correo ENTRANTE de BW Water y Bureau Veritas (ver CLAUDE.md 3.15)
│   │   ├── _LEEME.md               # La convencion: ruteo, nombres, deduplicacion — FUENTE UNICA
│   │   ├── _REGISTRO.md / .xlsx    # Indice durable, derivado de los _correo.md
│   │   ├── scripts/                # capturar_correo · instalar_adjuntos · generar_registro
│   │   └── [Mes YYYY]/<fecha>_<remitente>_<asunto>/_correo.md
│   ├── CORREO ENVIADOS POR TEMAS CONTRACTUALES/
│   └── CORREOS COMPRA EQUIPOS/     # Comunicaciones compra equipos
│
├── BASES TECNICAS/                 # Requisitos ADASA
│   ├── pdf/                        # PDFs originales especificaciones
│   ├── md/                         # 4 versiones .md extraidas
│   └── INGENIERIA BASICA/          # 24 documentos ing. basica (.md)
│
├── OFERTA TECNICA/                 # Propuesta BW Water
│   └── md/                         # Rev.0 OBSOLETO, Rev.1 VIGENTE
│
├── OFERTA ECONOMICA/               # Presupuesto BW Water
│   └── md/                         # 2 archivos
│
├── PROGRAMA y CONTRATO/            # Cronogramas y contrato
│   └── md/                         # 3 archivos incl. Contrato C-4300
│
├── ENTREGAS_BWWATER/               # Entregas documentales BW Water
│   ├── ENTREGA 1/                  # 13 docs (10-Dic-2025)
│   ├── ENTREGA 2/                  # 7 docs (16-Dic-2025)
│   ├── ENTREGA 3/                  # 1 doc (16-Dic-2025)
│   ├── ENTREGA 4/                  # 1 doc (24-Dic-2025)
│   ├── ENTREGA 5/                  # 2 docs (06-Ene-2026)
│   ├── ENTREGA 6/                  # 3 docs (08-Ene-2026)
│   ├── ENTREGA 7/                  # 6 docs (14-Ene-2026)
│   ├── ENTREGA 8/                  # 12 docs (Ene-2026)
│   ├── ENTREGA 9/                  # 5 docs (Ene-2026)
│   ├── ENTREGA 10/                 # 2 docs (30-Ene-2026)
│   ├── ENTREGA 11/                 # 2 docs (03-Feb-2026)
│   ├── ENTREGA 12/                 # 1 doc (20-Feb-2026)
│   ├── ENTREGA 13/                 # 9 docs (26-Feb-2026)
│   ├── ENTREGA 14/                 # 4 docs (06-Mar-2026)
│   ├── ENTREGA 15/                 # 10 docs (09-Mar-2026) — 9 datasheets + Power Works DWG
│   ├── ENTREGA 16/                 # 1 doc (09-Mar-2026) — Instrument List Rev B (standalone)
│   ├── ENTREGA 17/                 # 1 doc (11-Mar-2026) — P&ID Rev B (25007-0017)
│   ├── ENTREGA 18/                 # 6 docs (12-Mar-2026) — IO List Rev B, DTL Rev A, Control Arch Rev C, GA Tank+Turbos Rev A
│   ├── ENTREGA 19/                 # 5 docs (13-Mar-2026) — Valve List Rev C, Equipment List Rev B, GA CIP+Antiscalant Pump Rev A, Painting Rev B
│   ├── ENTREGA 20/                 # 3 docs (16-Mar-2026) — HP Pump DS Rev D, Turbo 1+2 DS Rev D
│   ├── ENTREGA 21/                 # 2 docs (16-Mar-2026) — Grounding Layout Rev B, Instrument Layout Rev B
│   ├── ENTREGA 22/                 # 2 docs (22-Mar-2026) — Datasheet Vibration Transmitter Rev A (25007-0022)
│   ├── ENTREGA 23/                 # 2 docs (26-Mar-2026) — Line List Rev B (25007-0023)
│   └── PRELIMINAR  LAYOUT/         # Advanced copies (27-Mar-2026) — Equipment Layout Rev B + Tie-In Points Rev B (sin submittal form)
│
├── REVISIONES/                     # Revisiones tecnicas ADASA
│   ├── TRANSMITTALES/              # Respuestas formales ADASA
│   │   ├── P22-TM-09-000-001-0/    # TM N1 - E1+E2 (16-Dic-2025)
│   │   ├── P22-TM-09-000-002-0/    # TM N2 - E3-E7 (26-Ene-2026)
│   │   ├── P22-TM-09-000-003-0/    # TM N3 - E7-E9 (EMITIDO 28-Ene-2026)
│   │   ├── P22-TM-09-000-004-0/    # TM N4 - E10+E11 (EMITIDO 05-Feb-2026)
│   │   ├── P22-TM-09-000-005-0/    # TM N5 Rev 0 - E12 (23-Feb-2026)
│   │   ├── P22-TM-09-000-005-1/    # TM N5 Rev 1 - OBS-01 actualizado (23-Feb-2026)
│   │   ├── P22-TM-09-000-006-0/    # TM N6 - E13 (27-Feb-2026)
│   │   ├── P22-TM-09-000-007-0/    # TM N7 - E14 (08-Mar-2026)
│   │   ├── P22-TM-09-000-008-0/    # TM N8 - E15+E16 (09-Mar-2026)
│   │   ├── P22-TM-09-000-009-0/    # TM N9 - E17 (11-Mar-2026)
│   │   ├── P22-TM-09-000-010-0/    # TM N10 - E18 (12-Mar-2026)
│   │   ├── P22-TM-09-000-011-0/    # TM N11 - E19+E20+E21 (17-Mar-2026)
│   │   └── P22-TM-09-000-012-0/    # TM N12 - E22+E23 (30-Mar-2026)
│   ├── CONSULTAS_TECNICAS/         # Consultas tecnicas formales ADASA
│   │   ├── P22-CT-09-000-001-0_*   # CT-001: Dosificacion Antiescalante
│   │   └── P22-CT-09-000-001-1_*   # CT-001: Evaluacion Respuesta BW Water
│   ├── EVALUACIONES/               # Evaluaciones formales y registros internos ADASA
│   │   ├── crear_evaluacion.py     # P22-IT-06-000-001-0 Evaluacion respuestas BWW
│   │   ├── crear_registro.py       # P22-IT-06-000-002-0 Document Status Register
│   │   ├── generar_excel_registro.py # Excel con Legend sheet
│   │   └── crear_alineacion_notebooklm.py # P22-IT-06-000-003-0 Alineacion NotebookLM
│   └── SUBMITTALS/                 # Analisis por submittal BW Water
│       ├── 25007-HPPUMP/           # Revisiones HP Pump y temperatura
│       ├── 25007-IOLIST/           # Revision cruzada Instrument List
│       ├── 25007-LAYOUT/           # Revision Instrument Location Layout
│       ├── 25007-VALVELIST/        # Revision cruzada Valve List/Equipment List
│       ├── 25007-0010/             # Revision Entrega 10 (02-Feb-2026)
│       ├── 25007-INSTRUMENTACION/  # Informe instrumentacion
│       ├── 25007-0013/             # Revision Entrega 13 (27-Feb-2026)
│       └── 25007-0014/             # Revision Entrega 14 (08-Mar-2026)
│
├── COMPRA EQUIPOS/                 # Procesos de compra ADASA
│   ├── Compra de Bombas/           # Bombas de proceso
│   └── COMPRA DE VALVULAS/         # Valvulas de proceso
│
├── CLAUDE.md                       # Configuracion Claude Code
└── README.md                       # Este archivo
```

---

### Baseline Schedule (05-Mar-2026)

> **CRONOGRAMA VIGENTE (desde 05-Ago-2026) = `2026-08-04_TALTAL Water Treatment Plan Project _Progress Update`.** Fuente: `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/` (extracto en `md/`). El avance se juzga contra él. El baseline **05-Mar-2026** de esta sección queda **solo como referencia de varianza contractual**, y el `Project Schedule 08-06-26` (Rev A) **pasa a histórico**: declaraba EXW 14-15 Ago y llevaba cinco semanas superado.
>
> **Es una serie, no un documento fijo.** BW Water reemite esta impresión MS Project del `Recovery Schedule` cada pocas semanas (24-Jun · 14-Jul · 27-Jul · 04-Ago). Se lee **por ID de tarea**, que son estables entre versiones: **416** EXW Penang · **414** FAT · **417** entrega a sitio · **424** Performance Test · **397** fabricación Penang · **404** pre-ensamble. Antes de medir nada, verificar cuál es la impresión más reciente.
>
> **Hitos vigentes:** fabricación Penang fin **21-Ago**; pre-ensamble 08-Ago→**18-Sep**; CSC contenedor 27-28 Ago; **FAT 07-18 Sep** (11 días); **EXW Penang 19-21 Sep**; entrega a sitio **13-Nov**; supervisión de montaje 10-19 Dic; puesta en marcha 21-25 Dic; entrenamiento 26-28 Dic; **Performance Test 29-Dic-2026 → 02-Ene-2027**. Contra la línea base contractual del **03-Ago** (Cláusula 27), el EXW acumula **+47 a +49 días**; contra la referencia que ADASA declaró fija el 20-Jul (Recovery del 14-Jul, ex-works 09-10 Sep), **+10 a +11**.
>
> **Dos caveats del documento del 04-Ago.** (1) No aporta ningún hito nuevo: los IDs 414, 415, 416 y 417 traen fechas **idénticas** a las del 27-Jul; lo único que se movió es el pre-ensamble, cuyo inicio corrió a 08-Ago con el fin clavado en 18-Sep — la fecha de embarque se sostiene **comprimiendo duraciones, no recuperando trabajo**. (2) Llegó como **impresión colapsada de 4 páginas** contra las 12 del 27-Jul, sin las filas de detalle de ingeniería, y **fuera del paquete semanal**. Los hitos críticos sí están; el detalle para auditar el camino crítico, no.

**Fuente (baseline contractual):** `PROGRAMA y CONTRATO/05.03.26_12803_Taltal Water Treatment Plant.pdf`
**Extracto MD:** `PROGRAMA y CONTRATO/05.03.26_12803_Taltal Water Treatment Plant_extracted.md`

#### Hitos clave (baseline 05-Mar; referencia de varianza)

| Hito | Fecha baseline 05-Mar | Vigente (cronograma 04-Ago) | ID | Δ |
|------|----------------|------------------------|----|---|
| BW Fabrication Penang | 02-Apr 2026 → 01-Aug 2026 | 03-Jun → **21-Ago 2026** | 397 | +20 |
| Pre-ensamble e instalación Penang | — | 08-Ago → **18-Sep 2026** | 404 | — |
| FAT (System) | 25-Jul 2026 → 01-Aug 2026 | **07-Sep → 18-Sep 2026** (11 días) | 414 | +44 |
| Ready to Ship (EXW Penang) | **03-Aug 2026** | **19-21 Sep 2026** | 416 | **+47/+49** |
| Package Delivery to Site | 18-Sep 2026 | **13-Nov 2026** | 417 | +56 |
| Site Supervision & Commissioning | 18-Sep 2026 → 08-Oct 2026 | **10-19 Dic 2026** | 421 | +72 |
| Operator Training | 09-Oct 2026 → 17-Oct 2026 | **26-28 Dic 2026** | 423 | +72 |
| Performance Test | 18-Oct 2026 → 16-Nov 2026 | **29-Dic-2026 → 02-Ene-2027** | 424 | +47 |

> La Δ es contra la fecha de término del baseline 05-Mar, en días corridos. El **Plazo Contractual** de la Cláusula 27 (510 días desde la NTP del 07-Oct-2025) vence el **01-Mar-2027**: el Performance Test proyectado deja **58 días** de margen, contra los ~47 que la cadena ya perdió. Un segundo deslizamiento del orden del ya ocurrido lo consume entero.

#### Items long-lead a vigilar

| Item | Manufacturing (baseline) | Vendor |
|------|--------------------------|--------|
| RO Membranes | 132 dias | LG |
| RO HP Pump | 120 dias | Fedco |
| All Valve Set | 98 dias | Belven |
| Instrument Set | 98 dias | Emerson / IFM |
| Feed Turbo | 48 dias | Fedco |
| Interstage Turbo | 48 dias | Fedco |

**Bottleneck Fedco:** vendor unico para 3 items criticos (RO HP Pump + Feed Turbo + Interstage Turbo). Si Fedco slip 1 sem, FAT slip 1 sem.

---

### Compra de Equipos ADASA

Procesos de compra directa de ADASA para equipos del proyecto.

#### 6.1 Compra de Bombas
**Ubicacion:** `COMPRA EQUIPOS/Compra de Bombas/`
**Estado:** En evaluacion tecnica

| Documento | Codigo |
|-----------|--------|
| Hoja de Datos | P22-ET-06-005-001 |
| Cotizacion vigente | SC80371-CV406762-REV1 |

#### 6.2 Compra de Valvulas
**Ubicacion:** `COMPRA EQUIPOS/COMPRA DE VALVULAS/`
**Estado:** **KSB CV421060 Rev.1 - APPROVED** (31-Dic-2025)

| Tipo | DN | Cantidad | P.U. USD | Total USD |
|------|-----|----------|----------|-----------|
| Mariposa Ebonita | 4" | 8 | 641 | 5.128 |
| Mariposa Ebonita | 2" | 2 | 255 | 510 |
| Mariposa CF8M | 3" | 5 | 334 | 1.670 |
| Check SD2507 | 4" | 4 | 1.312 | 5.248 |
| **Total Valvulas** | | **19** | | **12.556** |
| Servicio terreno | | 2 dias | | 1.340 |
| Repuestos PEM + 2 anos | | | | 666 |
| **TOTAL NETO** | | | | **14.562** |

**Incoterm:** DDP Planta Taltal
**Plazo critico:** VV Check 4" - 15 semanas

---

### Contactos y Referencias

#### READMEs del Proyecto

| Ubicacion | Proposito | Ultima Actualizacion |
|-----------|-----------|----------------------|
| [CLAUDE.md](CLAUDE.md) | Configuracion y estandares Claude Code (v6.4) | 20-Abr-2026 |
| [ENTREGAS_BWWATER/README.md](ENTREGAS_BWWATER/README.md) | Estado entregas BW Water (54 docs) | 02-Feb-2026 |
| [REVISIONES/README.md](REVISIONES/README.md) | Historial revisiones tecnicas (25 revisiones) | 17-Feb-2026 |
| [COMPRA EQUIPOS/README.md](COMPRA%20EQUIPOS/README.md) | Compras directas ADASA (Bombas, Valvulas) | 28-Ene-2026 |
| [BASES TECNICAS/INGENIERIA BASICA/README.md](BASES%20TECNICAS/INGENIERIA%20BASICA/README.md) | Ingenieria basica (24 docs) | 28-Ene-2026 |

**Nota:** Todos los READMEs incluyen navegacion al README principal.

#### Historial de Versiones CLAUDE.md

| Version | Fecha | Cambio |
|---------|-------|--------|
| v6.4 | 20-Abr-2026 | §2.6 nuevo — Referencias Internas dentro del Mismo Documento. Prohibido `§NombreSeccion`; correcto `Seccion N — Nombre Completo`. Aplicado en TdR OOCC (4 referencias: §Condiciones Comerciales, §Plazos de Ejecucion x2, §Entregables). |
| v6.3 | 20-Abr-2026 | §3 actualizado — skill template-adasa debe importarse SIEMPRE desde path global `~/.claude/skills/template-adasa/`. La carpeta local `.claude/skills/` del proyecto NO es symlink (Windows/Synology) — quedo desactualizada como copia v6.0. Script crear_tdr_oocc.py migrado. |
| v6.2 | 17-Abr-2026 | Unificacion skill template-adasa — symlink documentado (pero real copia en disco). Fixes tabla: CHARS_PER_INCH 7→5, max_ancho_corto 1.3→2.0, tblLayout fixed, gridCol DXA. Aplicado efectivamente el 20-Abr via Algoritmo D. |
| v6.1 | 14-Abr-2026 | §3.9 expandido — alcance Van Doorn (proceso/mecanica/tuberias, no E&C). Tabla TAGs area 06: TK-06-002 reasignado + BS-06-001 omision = cambio aprobado. Metodologia anotaciones Excel con openpyxl. |
| v6.0 | 31-Mar-2026 | Auditoria estructural — Sec10 Errores de Nomenclatura migrado a README.md Sec13. Ejemplos Change Orders eliminados. Renumeracion Sec10/11/12. |
| v5.14 | 18-Mar-2026 | §13 nuevo — Listado Consolidado EVI. EQUIPOS_06 solo ADASA (4 items). TAGs duplicados: correlativo propuesto (VE-09-017, PSV-09-003), sin notas externas. |
| v5.7 | 16-Mar-2026 | §3.10 nuevo — Anotaciones PDF (PyMuPDF). Skill pdf-comments autocontenida. Checklist pre-creacion scripts (5 puntos). Causa raiz TM N10 documentada. 6 scripts TM N10 migrados. |
| v5.6 | 15-Mar-2026 | §12 nuevo — Propuestas Comerciales de Cambio. Criterios responsabilidad, scope, historial entregas. |
| v5.5 | 13-Mar-2026 | §2.5 — regla nueva: transmittals a BW Water deben usar "Section X" (ingles), no "§X". Error detectado en TM N10. §11 trazabilidad TM N9 corregida (veredicto Code 2, VM-09-015 residual en Valve List no en P&ID). §11.6 codigo documento corregido (P22-DWG-09-009-002, no 005). |
| v5.4 | 11-Mar-2026 | §7.2 — criterio tecnologia transmisores conductividad: contacting <20 mS/cm, toroidal obligatorio >20 mS/cm. ET §5.5.5 no aplica a rechazo concentrado RO. Confirmado TM N8 CIT-09-005. |
| v5.3 | 11-Mar-2026 | §11 nuevo — Errores de Nomenclatura con trazabilidad completa (TAGs duplicados, prefijo VM/VE, area codes, inconsistencias intradocumento, codigos señal, title block, convencion equipos). |
| v5.2 | 09-Mar-2026 | §6.3 y §7.3 — criterio ET §5.2.3 corregido a funcional (no dimensional). Ejemplos canonicos VM-09-015/VM-09-012. |
| v5.1 | 08-Mar-2026 | §3.4 REQUIRED ACTIONS eliminado del formato transmittal estandar. §3.9 Regla Van Doorn documentada. |
| v5.0 | 06-Mar-2026 | Reorganizacion mayor. §1.4 TOC autocontenido. Metodo B como unico metodo DOCX. |

#### Trazabilidad de Documentos

| Carpeta | PDFs | .md | Estado |
|---------|------|-----|--------|
| BASES TECNICAS/md/ | 4 | 4 | Completo |
| BASES TECNICAS/INGENIERIA BASICA/md/ | 13 | 24 | Completo |
| OFERTA TECNICA/md/ | 2 | 2 | Completo |
| OFERTA ECONOMICA/md/ | 2 | 2 | Completo |
| PROGRAMA y CONTRATO/md/ | 4 | 3 | 3 completos + 1 Gantt (Feb-2026) |
| ENTREGAS_BWWATER/ENTREGA 1/md/ | 13 | 13 | Completo |
| ENTREGAS_BWWATER/ENTREGA 2/md/ | 7 | 7 | Completo |
| ENTREGAS_BWWATER/ENTREGA 3/md/ | 1 | 1 | Completo |
| ENTREGAS_BWWATER/ENTREGA 4/md/ | 1 | 1 | Completo |
| ENTREGAS_BWWATER/ENTREGA 5/md/ | 2 | 2 | Completo |
| ENTREGAS_BWWATER/ENTREGA 6/md/ | 3 | 3 | Completo |
| ENTREGAS_BWWATER/ENTREGA 7/md/ | 6 | 10 | Completo |
| ENTREGAS_BWWATER/ENTREGA 8/md/ | 12 | 16 | Completo |
| ENTREGAS_BWWATER/ENTREGA 9/md/ | 5 | 5 | Completo |
| ENTREGAS_BWWATER/ENTREGA 10/md/ | 2 | 2 | Completo |
| ENTREGAS_BWWATER/ENTREGA 11/md/ | 2 | 3 | Completo |
| ENTREGAS_BWWATER/ENTREGA 12/md/ | 1 | 1 | Completo |
| **TOTAL** | **79** | **91** | |

#### Contactos

##### ADASA (Cliente)
- **Gerente Comercial**: Raul Ardiles Cayo
- **Gerente Estrategia Corporativa**: Mario Corvalan Neira

##### BW Water (Proveedor)
- **Vice President Americas**: Andrew J. Zaske
- **Head of Engineering**: Dr. Marco Arsovic, Ph.D.
- **Project Manager**: Eduardo Yamauchi (desde 29-Ene-2026)

---

### Índice de Transmittales

> Una fila por transmittal (N1→N39). El detalle de cada uno vive en la Bitácora Cronológica.

| # | Codigo | Entregas | Docs | Fecha | Estado |
|---|--------|----------|------|-------|--------|
| 1 | P22-TM-09-000-001-0 | E1 + E2 | 20 | 16-Dic-2025 | **EMITIDO** |
| 2 | P22-TM-09-000-002-0 | E3 + E4 + E5 + E6 + E7 | 8 | 26-Ene-2026 | **EMITIDO** |
| 3 | P22-TM-09-000-003-0 | E7 + E8 + E9 | 23 | 28-Ene-2026 | **EMITIDO** |
| 4 | P22-TM-09-000-004-0 | E10 + E11 | 4 | 05-Feb-2026 | **EMITIDO Y ENVIADO** |
| 5 | P22-TM-09-000-005-0 | E12 | 1 | 23-Feb-2026 | **EMITIDO (Rev 0)** |
| 5.1 | P22-TM-09-000-005-1 | E12 | 1 | 23-Feb-2026 | **EMITIDO (Rev 1 — OBS-01 actualizado)** |
| 6 | P22-TM-09-000-006-0 | E13 | 9 | 27-Feb-2026 | **EMITIDO — 5 Approved as noted, 2 Rejected** |
| 7 | P22-TM-09-000-007-0 | E14 | 4 | 08-Mar-2026 | **EMITIDO — 0 Approved as noted, 4 To be Revised. Veredicto: 3 TO BE REVISED** |
| 8 | P22-TM-09-000-008-0 | E15 + E16 | 11 | 09-Mar-2026 | **GENERADO — 4 Approved, 4 Approved as noted, 2 To be Revised (+ 1 no recibido). Veredicto: 3 TO BE REVISED. Corregido 11-Mar-2026.** |
| 9 | P22-TM-09-000-009-0 | E17 | 1 | 11-Mar-2026 | **GENERADO — P&ID Rev B. Veredicto: 3 TO BE REVISED** |
| 10 | P22-TM-09-000-010-0 | E18 | 6 | 16-Mar-2026 | **ENVIADO 16-Mar-2026 — IO List Rev B, DTL Rev A, Control Arch Rev C, GAs antiscalant + turbochargers. Code 3 — To Be Revised. 7 obs MAJOR** |
| 11 | P22-TM-09-000-011-0 | E19+E20+E21 | 10 | 17-Mar-2026 | **EMITIDO Y ENVIADO 17-Mar-2026 — Valve List Rev C, Equipment List Rev B, GAs CIP+Antiscalant Pump, Painting Spec Rev B, Datasheets HP Pump+Turbo 1+Turbo 2 Rev D, Grounding Layout Rev B, ILL Rev B. Veredicto: 3 TO BE REVISED. 4 MAJOR (OBS-01/02 Valve List duplicados, OBS-03 Grounding Layout, OBS-04 ILL). 6 NOTE.** |
| 12 | P22-TM-09-000-012-0 | E22+E23 | 2 | 30-Mar-2026 | **EMITIDO Y ENVIADO 30/31-Mar-2026 — Datasheet Vibration Transmitter Rev A, Line List Rev B. Veredicto: 3 TO BE REVISED. OBS-01 MAJOR: VTV122 sin HART (ET §5.5 requiere 4-20mA+HART). OBS-01 MINOR: DA-SSD-DN80-09-006 margen 5.9%. CIERRA TM N3 OBS-01 (Line List DA-SSD-DN80-09-005 DP=80 bar).** |
| 13 | P22-TM-09-000-013-0 | E24 | 1 | 31-Mar-2026 | **GENERADO 31-Mar-2026 — PENDIENTE ENVIO — P&ID Rev C. Veredicto: 2 APPROVED AS NOTED. CIERRA TM N9 NOTE-01/NOTE-02. TM N10 OBS-05 PARTIALLY ADDRESSED. NOTE-01 MINOR: TK-09-001 (CIP Tank) 6.81 m3 vs 6.1 m3 Equipment List Rev B. 13 items heredados abiertos.** |
| 14 | P22-TM-09-000-014-0 | E26+E27 | 3 | 10-Apr-2026 | **EMITIDO Y ENVIADO 15-Apr-2026 — CSA Rev D, Valve List Rev D, DS Pressure Gauge Rev B. Veredicto: 2 APPROVED AS NOTED. Valve List Rev D TAG uniqueness 111 items vs P&ID Rev C; cierra TM N11 OBS-01/02 + TM N6 duplicados. NOTE-01: Item 112 eliminado.** |
| 15 | P22-TM-09-000-015-0 | E30+E31+E32+E33 | 10 | 22-Apr-2026 | **EMITIDO Y ENVIADO (correo 22-Apr-2026; respaldo PDF pendiente de adjuntar al repo) — Veredicto: 3 TO BE REVISED. 1 Code 1 + 6 Code 2 + 3 Code 3 (LCP, Cable Tray, Control Philosophy Rev B). NOTE-20 CRITICAL: HP Pump permissive VE-09-007 dup + VE-09-014. Refinado v3 post multi-audit.** |
| 16 | P22-TM-09-000-016-0 | E34 | 1 | 24-Apr-2026 | **EMITIDO Y ENVIADO (correo 24-Apr-2026; respaldo PDF pendiente de adjuntar al repo) — Civil and Loading Drawing Rev A. Veredicto: 2 APPROVED AS NOTED. NOTE-01 MAJOR: weight disclosure para Rev 0 IFC.** |
| 17 | P22-TM-09-000-017-0 | E35+E36+E37 | 9 | 05-May-2026 | **EMITIDO Y ENVIADO 05-May-2026 — Veredicto: 3 TO BE REVISED. 7 Code 2 + 2 Code 3 (Alarm & Interlock List Rev A, PQP Rev A). Respaldo: CORREOS/Mayo 2026/2026-05-05/.** |
| 18 | P22-TM-09-000-018-0 | E38+E39+E40+E41 | 5 | 18-May-2026 | **EMITIDO Y ENVIADO 18-May-2026 (re-escopeado +P&ID Rev D E41; RE-DISPOSICIONADO con criterio ejecutivo Code 1/2) — Correo ENVIADO 18-May-2026, respaldo "Elementos enviados ... Outlook.pdf" en CORREOS/Mayo 2026/2026-05-18/. Master Deliverable Register (P22-IT-06-000-002-0_*.xlsx) actualizado a estado TM N18. Veredicto: 3 TO BE REVISED. Tally: 4 Code 1 (Valve List Rev D, Line List Rev C, AC Thermal Calc Rev C, P&ID Rev D) + 1 Code 3 (Plant Control Philosophy Rev C). Criterio: el código refleja el documento revisado en sí — si no requiere modificación a sí mismo = Code 1, entregables cross-document → Sección 3 (CLAUDE.md §6.2 v6.11). Driver único Code 3: OBS-01 CRITICAL permissive HP Pump (repite TM N15 NOTE-20, condición bloqueante + C-4300) + OBS-02 child docs no entregados. CIERRA TM N12 NOTE-01/02 + TM N15 NOTE-02 + TM N13 NOTE-01. Tracked-IFC Sección 3: PSV-09-002 análisis, CIT-09-004 (Instrument/Line List + nota), dual-value CIP Tank, TM N16 NOTE-01, AC margen efectivo. Adjuntos: 1 CC_ADASA (Control Philosophy, Code 3); 4 Code 1 sin CC_ADASA (§3.8). anti-ia VERDE; multi-audit 8 agentes ×2 sin FABRICADO.** |
| 19 | P22-TM-09-000-019-0 | E42+E43+E44+E45 | 13 | 25-May-2026 | **EMITIDO Y ENVIADO 25-May-2026 — Correo ENVIADO, respaldo "correo transmittal 19.pdf" en CORREOS/Mayo 2026/2026-05-25/. Veredicto: 3 TO BE REVISED. Tally: 3 Code 1 + 5 Code 2 + 5 Code 3. Submittals 25007-0042..0045 = Electrical Power Package (7) + IO List IFC (1) + Quality/Instrumentation Cable (3) + Cartridge Filters (2). Drivers Code 3: ITP Offsite Rev B (silencio ASME X stamp ↔ NT-001 6.A/6.C), Grounding Rev E (3º TM consecutivo sin schedule), IC Cable Schedule Rev 0, RO + CIP Cartridge Filter (H→V + Sysflo materializados pre-respuesta NT-001 5.A–5.E). CIERRA: Cable Tray Rev C los 7 items inherited TM N4+N15 (110 días, longest-open), PQP Rev B los 2 CRITICAL TM N17 (inspection matrix + FAT scope = prerequisito 40% BAE Cl.31), Typical Power Works 4 NOTEs TM N17, TM N3 OBS-01 RO Cartridge flow rate. Section 3 reducida a 3 carry-forward más críticos (Plant Control Philosophy Rev D 3º consec, TM N11 OBS-03 Grounding 70d, TM N4 NOTE-05 HMI 110d). 10 CC_ADASA adjuntos (5 Code 3 + 5 Code 2 per §3.8 CLAUDE.md). NT-001 emitida en paralelo en cadena de correo separada (Reply-To cover BW Water 24-May Mitigation Plan). anti-ia VERDE; multi-audit 8 agentes.** |
| 20 | P22-TM-09-000-020-0 | E46+E47 | 20 | 10-Jun-2026 | **EMITIDO Y ENVIADO 10-Jun-2026** (correo TM cadena regular + Reply panel drawings cadena separada, ambos ENVIADOS mismo día; respaldo pendiente de adjuntar al repo). Veredicto: 3 TO BE REVISED. Tally: **8 Code 1 + 7 Code 2 + 5 Code 3**. Submittals 25007-0046 (C&I + paquete panel PLC-LCP) + 25007-0047 (eléctrico IFC Rev 0 + listas C&I + calidad). **Drivers Code 3:** PLC-LCP Outline Rev A (Panel Spec Sheet = sheet steel RAL 7035 + IP55 contradice LCP Datasheet Rev B SS316L/NEMA4X/IP66 + SLD IFC + ET — gate de fabricación del enclosure, urgencia correo Yamauchi 10-Jun), A&I List Rev B (swap winding/bearing TE-09-001/002 y 003/004 vs IL Rev E; 95 °C confirmado no aplicado; PHIT-09-001 vs -006), I/O List Rev 2 (reversión contractual: ventana 14d de Rev D vencida 08-Jun, 4º ciclo), IC Cable Schedule Rev 1 (items 54/55/56 duplicados + descripciones PWR copy-paste), NDE Plan Rev A (alcance vessel/waiver 02-Jun ausente). **CIERRA:** paquete eléctrico IFC Rev 0 completo (5 docs Code 1, todas las condiciones TM N19 verificadas incorporadas — SLD con NEMA4X/IP66 + SPD en nube Rev 0 verificado visual), TM N14 NOTE-02 voltaje analizadores (~96d), TM N15 OBS-01/02 LCP, TM N17 IL/DTL/PTx/A&I items. Section 3: Control Philosophy Rev D 4º ciclo (remedies C-4300 vigentes), Grounding Rev F 17-Jun, HMI ~126d, ITP Rev C + Hydrostatic/Preservation/FAT procedures, Cartridge Filters NT-001. 12 CC_ADASA (5 Code 3 + 7 Code 2). anti-ia VERDE post-correcciones. Correo TM cadena regular + Reply panel drawings cadena separada, mismo día. |
| 21 | P22-TM-09-000-021-0 | E48 | 2 | 11-Jun-2026 | **ENVIADO — 3 To Be Revised.** Grounding Rev F Code 1 (cierra el ítem eléctrico más antiguo) + DS PLC/HMI Rev B Code 3. |
| 22 | P22-TM-09-000-022-0 | E49+E50 | 7 | 15-Jun-2026 | **ENVIADO — 3 To Be Revised. 2 Code 1 + 1 Code 2 + 4 Code 3.** Driver: Plant Control Philosophy Rev D (permissive HP Pump CERRADO; hijos de lógica no entregados, 6º ciclo). |
| 23 | P22-TM-09-000-023-0 | E51+E52 | 7 | 18-Jun-2026 | **ENVIADO — 3 To Be Revised. 0 Code 1 + 1 Code 2 + 6 Code 3.** Driver CRITICAL: RO Vessel Hydrostatic Rev A (45,5 bar vs 1.980 psi del ITP/waiver); ITP Rev C cierra el waiver ASME. |
| 24 | P22-TM-09-000-024-0 | E53+E54 | 5 | 23-Jun-2026 | **ENVIADO — 2 Approved as Noted. 3 Code 1 + 2 Code 2.** CIP Cartridge Filter Rev E cierra el Code 3 del N22; HART cerrado a nivel instrumento. |
| 25 | P22-TM-09-000-025-0 | E55+E56 | 6 | 29-Jun-2026 | **ENVIADO — 3 To Be Revised. 4 Code 1 + 1 Code 2 + 1 Code 3.** Driver único: PLC-LCP Outline Rev B (gate de fabricación del enclosure). |
| 26 | P22-TM-09-000-026-0 | E57–E62 | 9 | 06-Jul-2026 | **ENVIADO — 3 To Be Revised. 2 Code 1 + 3 Code 2 + 4 Code 3.** Paquete QA/fabricación + I&C + estructura; ITP y NDE Plan a IFC. |
| 27 | P22-TM-09-000-027-0 | E63+E64 | 6 | 13-Jul-2026 | **ENVIADO — 3 To Be Revised. 4 Code 2 + 2 Code 3.** Drivers: HP/LP 75 bar sobre PVC (seguridad) + O&M Manual (dependencia de la familia de Control); cierra los 2 gates RO Vessel Hydro + enclosure. |
| 28 | P22-TM-09-000-028-0 | E65+E66 | 4 | 20-Jul-2026 | **ENVIADO — 2 Approved as Noted. 4 Code 2.** Familia de Control (Plant Control Philosophy Rev E + Alarm & Interlock Rev C + Control & Sequence Chart Rev A + IO List Rev 5); reconciliación cruzada a Rev 0. |
| 29 | P22-TM-09-000-029-0 | E67 | 4 | 21-Jul-2026 | **ENVIADO — 2 Approved as Noted. 2 Code 1 + 2 Code 2.** TM de recuperación: cierra los dos Code 3 vencidos (HP/LP Pressure Test Rev D, UHPRO Structural Calc Rev B); Outline y Line List recibidos a IFC Rev 0. |
| 30 | P22-TM-09-000-030-0 | E68+E69+E70 | 5 | 05-Ago-2026 | **ENVIADO — 3 To Be Revised. 2 Code 1 + 2 Code 2 + 1 Code 3**, más el conjunto de taller devuelto sin codificar. Re-escopeado desde el borrador del 23-Jul, que cubría solo la E68. Driver: Dossier Index Rev A. ADASA declara vinculante el terminal 2711P-T10C22D9P; dos hallazgos de contención de presión sobre planos timbrados FOR CONSTRUCTION. |
| 31 | P22-TM-09-000-031-0 | E72+E73 | 5 | 10-Ago-2026 | **ENVIADO 15:33 — 2 Approved as noted. 1 Code 1 + 3 Code 2**, más la Plant Control Philosophy Rev 0 devuelta **sin código** con cuatro condiciones del N28 abiertas. Alcance acotado a los comentarios históricos no levantados. Cierra la orientación del filtro de cartuchos y el Código 3 del Tie-In Point Layout, abierto desde el N7. La ENTREGA 71 entra en la Sección 3 sin códigos nuevos. El párrafo del enlace de descarga no salió en el cuerpo del correo. |
| 32 | P22-TM-09-000-032-0 | E75 | 7 | 12-Ago-2026 | **ENVIADO 15:30 — 3 To be revised. 2 Code 1 + 3 Code 3 + 2 sin código**. Cuatro procedimientos vuelven en Rev 0 con la misma letra y solo el Visual cierra su comentario; los tres procedimientos de ensayos no destructivos son primera emisión y ninguno fija el criterio de aceptación de ASME B31.3. El formulario de pintura quedó con RAL 5010 contra el RAL 5012 aprobado, y el de presión no identifica el formulario del ensayo que la fila 5.2 del ITP exige en Punto de Detención. Del cuerpo del correo no salió el párrafo del enlace, por tercera vez seguida. |
| 33 | P22-TM-09-000-033-0 | E76+E78+E79 | 5 | 17-Ago-2026 | **ENVIADO 12:17 — 2 Approved as noted. 4 Code 1 + 1 Code 2**. Ningún documento vuelve a revisión; el criterio de revisar solo el cierre de comentarios previos recortó veinte observaciones a dos. |
| 34 | P22-TM-09-000-034-0 | E73+E77+E80 | 5 | 18-Ago-2026 | **ENVIADO — 3 To be revised. 2 Code 1 + 2 Code 2 + 1 Code 3**. El código lo fija el Quality Dossier Index Rev B, que declara el Acta de Aprobación FAT en el capítulo equivocado. |
| 35 | P22-TM-09-000-035-0 | E81 | 5 | 20-Ago-2026 | **ENVIADO 11:16 — 3 To be revised. 2 Code 1 + 3 Code 3**. Los tres procedimientos de ensayos no destructivos vuelven por el mismo punto del N32 y los tres sin hoja de comentarios. |
| 36 | P22-TM-09-000-036-0 | E82+E83+E84+E85 | 8 de 9 | 26-Ago-2026 | **ENVIADO 18:08 — 2 Approved as noted. 3 Code 1 + 5 Code 2**, ningún documento vuelve a revisión. Exige cerrar en Rev 0 antes del FAT las tres hojas de datos de los equipos Fedco, comprados y a días de montarse (`PRG-37`). El GA of SWRO System Skid Rev 0 queda en Código 1 con texto endurecido: de las tres referencias del TM N31 solo una se corrigió. Cuatro PDF anotados más la excepción del modelo Navisworks. El Project Schedule Rev B se retiró del transmittal: se sigue por la reunión semanal. |
| 37 | P22-TM-09-000-037-0 | E86+E87+E88 | 7 | 31-Ago-2026 | **ENVIADO 18:27 — 3 To be revised. 2 Code 1 + 4 Code 2 + 1 Code 3**. Encabeza la Sección 3 con la exigencia de una entrega consolidada al jueves 3-Sep, con tabla de doce documentos nombrados uno por uno. Cinco PDF anotados. |
| 38 | P22-TM-09-000-038-0 | E89+E90 | 11 | 03-Sep-2026 | **ENVIADO 18:19 — 2 Approved as noted. 8 Code 1 + 3 Code 2**, cero Código 3. De los doce documentos exigidos llegaron siete. ADASA declara el valor vinculante en dos puntos en vez de pedir reconciliación. Tres PDF anotados. El bloque del enlace no sobrevivió al pegado en Outlook y se reenvió el mismo día. |
| 39 | P22-TM-09-000-039-0 | E91+E92 | 3 | 09-Sep-2026 | **ENVIADO — 2 Approved as noted. 1 Code 1 + 2 Code 2**, cero Código 3. Los tres son re-emisiones y se revisan solo contra los comentarios previos. La Valve List Rev E baja de Código 1 a Código 2 porque `VM-09-065` sigue en PVC sobre una línea que la Line List aprobada lleva en 316L, y esa lista gobierna la compra. El procedimiento de radiografía llega en Rev 0 y sale en Código 1. Dos PDF anotados. **Lleva una Sección 3 propia, `Issue for Construction of the Approved Engineering`**, con las cuatro tablas de la auditoría de emisión y la exigencia de emitir en revisión 0 al viernes 11 de septiembre. Un solo correo para las dos cosas. |

### Registro de Revisiones (por ítem)

> Índice tabular de las revisiones técnicas del proyecto (verdicto por ítem). Complementa la Bitácora.


| # | Tipo | Titulo | Veredicto | Fecha |
|---|------|--------|-----------|-------|
| 001 | Programa | Comparacion de Programas | 1 - Approved | 03-Nov-2025 |
| 002 | Tecnica | Cumplimiento ET | 1 - Approved | 25-Nov-2025 |
| 003 | Economica | Analisis Oferta Economica | 1 - Approved | 25-Nov-2025 |
| 004 | Proceso | Estado General Proyecto | 5 - For Information | 25-Nov-2025 |
| 005 | Entregables | Estado Entregas - Entrega 1 | 5 - For Information | 10-Dic-2025 |
| 006 | Tecnica | Revision Tecnica Entrega 1 | **4 - Rejected** | 10-Dic-2025 |
| 007 | Tecnica | Revision Tecnica Entrega 2 | 3 - To be revised | 16-Dic-2025 |
| 008 | Compilado | Revision Asesor LH + ADASA | Ver detalle | 16-Dic-2025 |
| 009 | Tecnica | Revision Tecnica Entrega 3 (P&ID) | 2 - Approved as noted | 05-Ene-2026 |
| 010 | Tecnica | Revision Tecnica Entrega 4 (Control Arch) | 2 - Approved as noted | 05-Ene-2026 |
| 011 | Tecnica | Revision Tecnica Entrega 5 (A/C + Mixer) | 3 - To be revised | 06-Ene-2026 |
| 012 | Tecnica | Revision Tecnica Entrega 6 (UHPRO, Pump, Filter) | 2 - Approved as noted | 08-Ene-2026 |
| 013 | Tecnica | Revision Tecnica Entrega 7 (Process Calc Rev B) | 2 - Approved as noted | 14-Ene-2026 |
| 014 | Cruzada | Revision Tecnica Instrument List Cruzada | 3 - To be revised | 27-Ene-2026 |
| 015 | Cruzada | Revision Tecnica Temperatura Bombas | 3 - To be revised | 27-Ene-2026 |
| 016 | Cruzada | Revision Tecnica Instrument Location Layout | 3 - To be revised | 28-Ene-2026 |
| 017 | Cruzada | **Revision Tecnica Cruzada Valve List/Equipment List** | **3 - To be revised** | 28-Ene-2026 |
| 018 | Tecnica | Revision Tecnica Entrega 10 (Utility, Antiscalant Tank) | 3 - To be revised | 02-Feb-2026 |
| 019 | Tecnica | **Revision Tecnica Entrega 11 (Control Arch, Cable Tray)** | **3 - To be revised** | 03-Feb-2026 |
| 020 | Consulta | **Consulta Tecnica CT-001: Dosificacion Antiescalante** | **Pendiente respuesta** | 05-Feb-2026 |
| 021 | Programa | **Analisis Comparativo Programas BW Water (Oct-2025 vs Feb-2026 vs ADASA)** | **Documento interno** | 10-Feb-2026 |
| 022 | Escalamiento | **Plan de Escalamiento BW Water (3 fases + Notificacion BAE 49)** | **Documento interno** | 10-Feb-2026 |
| 023 | Consulta | **CT-001 Evaluacion Respuesta: 0.5 ppm aceptable con 4 observaciones** | **Emitida - Deadline 20-Feb** | 16-Feb-2026 |
| 024 | Evaluacion | **Evaluacion Respuestas BWW a TM N3, N4 y Schedule (6 aceptadas, 4 insuficientes, 7 pendientes)** | **Documento interno** | 17-Feb-2026 |
| 025 | Registro | **Document Status Register: 15 docs no entregados + 14 requiriendo correccion (cruce verificado vs ET Sec 7)** | **Documento interno** | 17-Feb-2026 |
| 026 | Tecnica | **Revision Tecnica Entrega 12 (Equipment Layout RO Container)** | **3 - To be revised** | 23-Feb-2026 |
| 027 | Transmittal | **TM N5 Rev 1 (P22-TM-09-000-005-1): OBS-01 actualizado — CIP externo confirmado, footprint pendiente** | **3 - To be revised** | 23-Feb-2026 |
| 028 | Infra | **Template ADASA v7.3: SKILL.md autocontenido, patron revision history documentado** | **Actualizacion interna** | 23-Feb-2026 |
| 029 | Alineacion | **P22-IT-06-000-003-0: Technical Data Alignment NotebookLM vs Official Documents — 25 params confirmados, 2 hallazgos criticos documentados (HP Pump power 4 valores, SEC excede garantia a 43k TDS)** | **Documento interno** | 25-Feb-2026 |
| 030 | Tecnica | **Revision Tecnica Entrega 13 (25007-0013): Valve List Rev B (REJECTED — 4 TAGs duplicados + CCS falso), Feed TC Rev C (REJECTED — coupling 1,200 psi, margen 19%, bajo presiones UHPRO), HP Pump Rev C, Interstage TC Rev C, Utility List Rev B, Cartridge Filter Rev C, Static Mixer Rev B** | **4 - Rejected (2 docs)** | 27-Feb-2026 |
| 031 | Transmittal | **TM N6 (P22-TM-09-000-006-0): Submittal 0013 — 9 docs — Veredicto 4 REJECTED. OBS-05 Ground 1: coupling 1,200 psi insuficiente para circuito UHPRO (Joints 4+5 a 83.9/82.4 bar, margen 19% en Joint 2). 4 TAGs duplicados Valve List verificados desde fuente primaria (lineas 50/75, 76/89, 90/125, 62/108 del .txt).** | **4 - REJECTED** | 27-Feb-2026 |
| 032 | Revision | **Revision Logica de Control Van Doorn Rev B (P22-IT-06-008-101-B): 6 GAPs vs benchmark P13 (2019). GAP-01 arranque incompleto (VFD/timeout/OI), GAP-02 error tag BH-03-001 + parada incompleta, GAP-03 bandas nivel TK-06-001 (solo >70%), GAP-04 integracion postratamiento no documentada, GAP-05 lazo CTRL_BH06_001 sin parametros PI/VFD, GAP-06 senal alarma OI ausente + reencendido no definido. Documento anotado: P22-IT-06-008-101-B_ADASA-Review.docx (10 comentarios Word embebidos).** | **Documento interno** | 28-Feb-2026 |
| 034 | Correo | **Correo Clarificacion Code 2 (04-Mar-2026): adjunto carta 26-Feb-2026 agregado al header ("Attachments:" en tabla header_fields) y al action text Item 4 ("as documented in the attached communication"). Adjunto: ADASA letter dated February 26, 2026 — Pending Technical Deliverables: Tie-in Definitions, CIP Footprint & Overdue P&ID Rev B. DOCX regenerado sin errores. .md actualizado (YAML adjuntos + cuerpo). Pendiente envio a BW Water.** | **Actualizacion** | 04-Mar-2026 |
| 035 | Correo | **RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses (ENVIADO 05-Mar-2026): 9 items evaluados contra TM N3/N4. HP Pump 93 kW CONDITIONAL (vs 86 kW OT Rev1, impacto SEC garantizado). OBS-11 WITHDRAWN (VM-09-015 manual isolation, inconsistencia Rev B documentada). 3 compromisos registrados para 06-Mar: IO MODBUS list, Control Arch Rev C (UPS ≥8h explicito), VFD electrical vars AI. Container 40ft ACCEPTED. OVERDUE: SEC calc TM N3 OBS-02 (sin respuesta), DO/DI signals TM N3 OBS-04/05 (vencio 03-Mar), A/C thermal TM N4 OBS-03 (15 dias vencido). Auditoria numeracion TM N3 aplicada: OBS-10→11, OBS-14→15, OBS-02/13→02.** | **ENVIADO** | 05-Mar-2026 |
| 033 | Actualizacion | **Hallazgo coupling datasheet faltante ambos TCs (02-Mar-2026): el datasheet del fabricante del acople no fue entregado en Feed TC Rev C (Code 4) ni Interstage TC Rev C (Code 2). Revision E13 corregida: Feed TC Code 3→4; Interstage TC: nueva obs datasheet pendiente. Path to resolution documentado en TM N6 y correo: upgrade a ≥1,800 psi + datasheet coupling ambos TCs → Code 2 Feed TC. Solucion preferida ADASA: 2,000 psi (Piedmont Style H). 5 archivos actualizados (Revision E13.md, TRANSMITTAL.md, crear_transmittal.py, correo .md, crear_correo.py). DOCXs regenerados sin errores. Correo ENVIADO a BW Water con convocatoria reunion 04-Mar-2026 10:00 AM (Chile).** | **Actualizacion + Envio** | 02-Mar-2026 |
| 036 | Correccion | **P22-IT-06-000-005-0 — Correccion criterio actuacion Valve List en crear_analisis_schedule.py: accion BW Water corregida de "reconfirmar actuacion electrica DN50+ ANSI 900#" a "corregir 4 TAGs duplicados (VM-09-015, VE-09-008, VE-09-009, VM-09-065) + revision sistematica unicidad". La actuacion electrica de VM-09-015 fue confirmada en Valve List Rev B (RESOLVED TM N6) y la observacion fue WITHDRAWN en correo 05-Mar-2026 (OBS-11). DOCX regenerado. Auditoria TM N3–TM N7 confirma que todos los transmittales aplicaron criterio funcional correcto de ET §5.2.3 (linea de proceso principal). CLAUDE.md §6.3 y §7.3 corregidos: criterio de valvulas ahora es funcional (valvulas de proceso en linea principal), no dimensional (DN50+ ANSI 900#). Un venteo DN50 ANSI 900# no requiere actuacion electrica per ET §5.2.3.** | **Correccion interna** | 09-Mar-2026 |
| 037 | Correo | **Correo interno a Ronald — Revision Control Philosophy Rev A (TM N7): 10 bullets (3 CRITICO: UPS 30min vs 8h ET, sin Pt-100 motores, sin MVE/CEE; 5 MAYOR: protocolo inconsistente, permisivo cliente mal definido, permisivo HP sin presion minima, Modbus TCP no descrita, ISA 101 ausente; 2 MENOR). PDF comentado listo. Pendiente confirmacion de Ronald para despachar TM N7. Nota: bullet "DO/DI estado y habilitacion" eliminado (revision 10-Mar-2026) — esas senales son pendientes del IO List/TM N3, no observaciones propias de la CP; permanecen en el TM N7 como OBS-6 y OBS-7.** | **BORRADOR — Pendiente validacion Ronald** | 10-Mar-2026 |
| 038 | Correccion | **Correcciones post-revision CP (10-Mar-2026): (1) Correo Ronald — eliminado bullet "DO/DI estado y habilitacion" (pendiente IO List TM N3, no observacion de la CP). Correo queda con 10 bullets. .md + crear_correo.py actualizados, DOCX regenerado. (2) TM N7 crear_transmittal.py — agregados OBS-11 (permisivo cliente incorrectamente definido: 2 DI individuales de tanques vs interfaz correcta 1 DI habilitacion general + 1 DO estado modulo; ET Communication and Control System + IO List Rev A) y OBS-12 (permisivo arranque HP sin umbral presion minima: riesgo cavitacion; ET HP Pump + Process Design). Parrafo intro §3.4 corregido: "Ten issues" → "Twelve issues". DOCX TM N7 regenerado con 12 observaciones en seccion 3.4 (OBS-1 a OBS-12).** | **Correccion interna** | 10-Mar-2026 |
| 040 | Correo | **Respuesta a Propuesta 25007-PL-0001 rev.1 (15-Mar-2026): Correo PENDIENTE ENVIO 16-Mar-2026 a Eduardo Yamauchi rechazando lógica comercial de propuesta USD 6,539 / 2 semanas / 7 docs. Acepta revisión de Piping Layout, Tie-In Points y Equipment Layout (responsabilidad BW Water: 66 días tarde). Impugna inclusión de Instrument Layout, Grounding Layout y Cable Tray Layout (sistemas interiores container no afectados por relocalización CIP exterior; Cable Tray aprobado sin observaciones en TM N4). Corrección de §ADASA's Position: versión original erraba al decir "CIP externo predates any modification request from ADASA" — versión corregida distingue entre lo que la Technical Offer definió (CIP fuera del container) y lo que ADASA estableció vía TM N5 (límite 3.5 m, 23-Feb-2026). TM N5 establece el constraint dos semanas antes de la entrega del Piping Layout; BW Water lo ignoró (11,150 mm = 3x el límite). Scripts: `CORREOS/Marzo 2026/2026-03-16/crear_correo_layout_response.py`. DOCX regenerado 15-Mar-2026. Solicita propuesta revisada antes del 21-Mar-2026.** | **PENDIENTE ENVIO** | 15-Mar-2026 |
| 041 | Envio | **TM N10 enviado 16-Mar-2026 (P22-TM-09-000-010-0, Submittal 25007-0018, 6 docs, Code 3 — To Be Revised). Correo respuesta propuesta layout 25007-PL-0001 rev.1 enviado. Skill pdf-comments creada (.claude/skills/pdf-comments/pdf_comments.py — engine PyMuPDF aprobado TM N7-N10). 6 scripts TM N10 migrados a skill (25-35 lineas vs 165 lineas previo). CLAUDE.md v5.7 — §3.10 metodologia anotaciones PDF.** | **ENVIADO** | 16-Mar-2026 |
| 042 | Envio | **TM N11 enviado 17-Mar-2026 (P22-TM-09-000-011-0, Submittals 25007-0019/0020/0021, E19/E20/E21, 10 docs, Code 3 — To Be Revised). 10 observaciones: 4 MAJOR + 6 NOTE. OBS-01/02: Valve List Rev C introduce 2 nuevos duplicados (VE-09-007 / PSV-09-002) — Rev D requerida. OBS-03: Grounding Layout Rev B rechazado (posiciones no conformes por dependencia de Piping Layout rechazado TM N7). OBS-04: Instrument Location Layout Rev B rechazado (misma razon — footprint 11,150 mm vs 3,500 mm). Grounding + ILL Rev C requieren resubmision tras aceptacion de Equipment Layout y Piping Layout. 2 scripts nuevos creados: agregar_comentarios_grounding_layout.py + agregar_comentarios_instrument_layout.py. PDFs CC_ADASA generados. Correo enviado con link adjuntos. Respaldo: CORREOS/Marzo 2026/2026-03-17/respaldo_envio_correo_tm11.pdf. E21 actualizado de Code 2 → Code 3 en tabla Entregas.** | **ENVIADO** | 17-Mar-2026 |
| 043 | Listado | **LISTADO-CONSOLIDADO-EVI.xlsx limpiado para uso externo (18-Mar-2026). EQUIPOS_06 reducido de 15 a 4 ítems (solo suministro ADASA: TK-06-001, TK-06-004, BH-06-001, BS-06-001) — los 11 equipos BW Water eliminados de Area 06 ya estaban en EQUIPOS_09 con specs completas y TAGs Area 09 correctos. VALVULAS_09: 2 filas con TAG duplicado (VE-09-007 item 64 y PSV-09-002 item 112) reciben correlativo propuesto — VE-09-017 (siguiente tras VE-09-016) y PSV-09-003 (siguiente tras PSV-09-002). Notas con referencias internas (TM N11, "PENDIENTE Rev D", "renumerado") eliminadas de VM-09-005 y VM-09-151. Script: `generar_listado_consolidado.py`. CLAUDE.md v5.14 — §13 metodologia listado consolidado.** | **Documento de trabajo** | 18-Mar-2026 |
| 047 | Reunion | **Reunion Coordinacion Ingenieria y Adquisiciones 26-Mar-2026. Acuerdos de liberacion de Hold: Valvulas (PO procede, corregir tags), PT100 (PO procede), Acoples/Couplings (1,800 psi validado, PO procede), Estructuras y Racks RO (diseno original sin cambios). Items condicionados: Medidor conductividad salmuera (rango 20 µS inoperante, cambiar a mayor). Items en Hold: Sistema CIP (faltan P&IDs y layouts — bloqueante para Layouts Instrumentos/Cables). CRITICO: Tuberias Super Duplex/Duplex en Hold (Ingenieria) — lead time 3-4 meses importacion a Chile, requiere definicion urgente footprint CIP. Overdue: Bomba dosificadora (respuesta proveedor dosificacion metales pesados pendiente). Bloqueo Control Philosophy: Nick debe revisar comentarios ADASA y emitir Rev B. Compromisos: Eduardo envia cronograma POs EOD 27-Mar; Adenda Alasa Rev.2 aceptada, pasa a Gerencia Financiera. Proxima reunion: 30-Mar-2026.** | **Reunion interna** | 26-Mar-2026 |
| 046 | Correo | **Correo respuesta BW Water 26-Mar-2026 (CORREOS/Marzo 2026/2026-03-26/). BW Water respondio procurement log parcialmente — ignoro Seccion 4 (Propuesta Layout). Issues: (1) Code 2 clarificacion: BW retiene POs para Code 2 incorrectamente; ventana CIP Cartridge Filter (23-27 Mar) vencida; (2) RO Pressure Vessel respuesta evasiva; (3) Structural Frames "TBC" sin datasheet (ventana 6-Apr); (4) Propuesta Layout §4 ignorada — deadline EOB 25-Mar incumplido. Nuevo deadline propuesta: EOB 27-Mar. POs confirmados: BW-PO-2026M062, BW-PO-2026M073, BW-PO-2026M089 + Malaysia workshop. README.md §2 actualizado.** | **BORRADOR** | 26-Mar-2026 |
| 049 | Revision | **TM N12 generado 30-Mar-2026 (P22-TM-09-000-012-0, Submittals 25007-0022/0023, E22/E23, 2 docs, Code 3 — To Be Revised). E22: Datasheet Vibration Transmitter Rev A (IFM VTV122) — OBS-01 MAJOR: HART ausente, ET §5.5 requiere 4-20mA+HART para todos los instrumentos; NOTE-01: Quantity "1 duty" para 3 TAGs. E23: Line List Rev B — TM N3 OBS-01 CERRADO (DA-SSD-DN80-09-005 DP actualizado a 80 bar); OBS-01 MINOR: DA-SSD-DN80-09-006 margen 5.9% (OP=85, DP=90 bar); NOTE-01: linea Make-Up CIP sin LINE NO.; NOTE-02: notacion SCH80 → SCH 80S (ASME B36.19M). Scripts creados: crear_transmittal.py, agregar_comentarios_vibration_transmitter.py, agregar_comentarios_line_list.py. PDFs CC_ADASA generados (2 anotaciones VT, 3 anotaciones LL). DOCX generado. 10 items pendientes heredados (TM N10 OBS-01/05+NOTE-05, TM N11 OBS-01/04).** | **GENERADO — pendiente envio** | 30-Mar-2026 |
| 050 | Correo | **Correo Layout Missed Deadline 1-Apr-2026 (CORREOS/Abril 2026/2026-04-01/). BW Water comprometio en reunion 31-Mar-2026 entregar 3 layouts revisados para 1-Apr-2026: Equipment Layout Rev. C, Piping Layout Rev. B, Tie-In Point Rev. C. Ninguno recibido al cierre del dia. Correo notifica incumplimiento formal y solicita entrega EOB 3-Apr-2026. Impacto documentado: Structural Frames PO window (6-10 Apr) y CIP piping procurement schedule. Script: CORREOS/Abril 2026/2026-04-01/crear_correo.py.** | **BORRADOR** | 1-Apr-2026 |
| 051 | Correo | **Correo Outstanding Commitments — Layouts & Procurement Log 6-Apr-2026 (CORREOS/Abril 2026/2026-04-06/). Follow-up consolidado: (1) Layouts pendientes — 6 documentos (4 revisados sin submittal formal + 2 no recibidos del CO 25007-PL-0001 rev.2); (2) Procurement Log comprometido en reunion 2-Apr no entregado; (3) Analisis cruzado procurement vs Baseline Schedule: 4 POs confirmadas (25%), 5 ventanas vencidas sin confirmacion (HP Pump 27d, Instruments 20d, Valves 20d, CIP Filter 14d, CIP Pumps 10d), 3 ventanas activas cerrando esa semana (RO PV, Feed TC, Structural Frames). Instrument Set y All Valve: cero margen (Mfg = fecha cierre ingenieria 09-Jul). Deadline BW Water: 7-Apr-2026. Script: crear_correo_outstanding_commitments.py.** | **ENVIADO** | 6-Apr-2026 |
| 052 | Correo | **RE: Outstanding Commitments 10-Apr-2026 (CORREOS/Abril 2026/2026-04-10/). Follow-up al correo 6-Apr sin respuesta. Reunion 9-Apr: BW Water re-comprometio PO Log para 9-Apr (no recibido) y layouts para 10-Apr (no recibidos). 4to compromiso consecutivo incumplido para layouts (31-Mar→1-Apr, 1-Apr→3-Apr, 6-Apr→7-Apr, 9-Apr→10-Apr). Tabla procurement actualizada: 8 ventanas PO cerradas (eran 5 el 6-Apr). 3 nuevas cerradas: RO PV (6-Apr), Feed TC (7-Apr), Structural Frames (10-Apr = HOY). Structural Frames: Mfg hasta 5-May, 25 dias calendario, sin layout = sin PO. Accion requerida inmediata. Script: crear_correo.py.** | **ENVIADO** | 10-Apr-2026 |
| 053 | Revision + Transmittal | **TM N14 EMITIDO Y ENVIADO 15-Apr-2026 (P22-TM-09-000-014-0, Submittals 25007-0026+25007-0027+25007-0028+25007-0029, E26+E27+E28+E29, 11 docs). 7 Code 1, 4 Code 2. 12 obs cerradas (TM N10 OBS-01/02/03/04, TM N11 OBS-01/02/NOTE-01, TM N12 OBS-01/NOTE-01, TM N8 OBS-01/02/03). 5 NOTEs nuevas. Vibration transmitter cambiado a Wilcoxon PCH420V-M12 (HART 7.0). Conductividad brine: Rosemount 228 toroidal confirmado. Flow Transmitter Rev B: FIT-09-004 fluid/medium corregido a "Concentrated Brine", power supply corregido a 12-42 VDC. 5 obs abiertas restantes (TM N10 OBS-05/NOTE-05, TM N11 OBS-03/04, TM N13 NOTE-02). 4 PDFs CC_ADASA generados. Auditoria TM N1-N13: sin obs perdidas. Correo enviado 15-Apr-2026 (CORREOS/Abril 2026/2026-04-15/).** | **EMITIDO Y ENVIADO** | 15-Apr-2026 |
| 056 | Correo | **Correo SECOND FOLLOW-UP Outstanding Commitments 13-Apr-2026 (CORREOS/Abril 2026/2026-04-13/). Follow-up ejecutivo al correo 10-Apr sin respuesta. Structural Frames PO window CERRADA el 10-Apr sin PO, 22 dias restantes manufactura (05-May). Layouts 12 dias overdue (4to compromiso consecutivo). Deadline EOB 13-Apr. Clausula de escalacion: notificacion formal al project sponsor bajo Contrato C-4300.** | **ENVIADO** | 13-Apr-2026 |
| 057 | Correo | **Correo Follow-Up Layouts & Operating Weight 14-Apr-2026 (CORREOS/Abril 2026/2026-04-14/). Quinta comunicacion sin respuesta. Hallazgo nuevo: Equipment Layout Rev C (advance copy 02-Apr) no incluye Operating Weight Table que Rev A contenia (7 items, 34,739 lb / 15,758 kg). Pesos requeridos para: diseno cimentaciones OOCC, verificacion sismica NCh 2369 Zona 3, lifting plan modulo. Advance copies no sustituyen submittal formal. Deadline: EOB 15-Apr. Respaldo: respaldo envio.pdf. Script: crear_correo.py.** | **ENVIADO** | 14-Apr-2026 |
| 058 | Correo | **Correo FINAL NOTICE Layouts, Operating Weight & Procurement Log 15-Apr-2026 (CORREOS/Abril 2026/2026-04-15/). Sexta comunicacion sin respuesta (01, 06, 10, 13, 14-Apr). TM N14 emitido hoy (12 obs cerradas) como contraste vs silencio BW Water en layouts/procurement. 3 items pendientes: (a) 6 layout documents 14 dias overdue, (b) Operating Weight Table, (c) Procurement Log 16 lineas. Deadline FINAL: EOB 16-Apr. Sin respuesta = formal delay notification al project sponsor bajo C-4300 el 17-Apr. Script: crear_correo_final_notice.py.** | **BORRADOR** | 15-Apr-2026 |
| 059 | Registro | **Master Deliverable Register v2 generado 15-Apr-2026 (REVISIONES/EVALUACIONES/generar_excel_registro_v2.py). 4 hojas: Master Register (81 items, 8 correcciones TM N14), Revision History (104 entries, trazabilidad completa N1-N14), Summary (metricas), Legend (actualizada). 8 items corregidos: Valve List Rev D, DS Conductivity/Flow/pH/Pressure Gauge/Temperature/Vibration Rev B, Data Transfer List Rev B. Output: P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx.** | **GENERADO** | 15-Apr-2026 |
| 055 | Integracion | **E29 integrada a TM N14 (15-Apr-2026). Submittal 25007-0029: DS Flow Transmitter Rev B (P22-LI-09-008-007). Veredicto: Code 1 Approved. Notas inline TM N8 resueltas: FIT-09-004 fluid/medium corregido de "Filtered/CIP Water" a "Concentrated Brine"; power supply corregido de "90-250 VDC" a "12-42 VDC". Cross-reference con IL Rev C, IO List Rev C, DTL Rev B: 5 FITs consistentes. NOTE-04 (Working Medium en IL Rev C) sigue vigente — DS corregido pero IL aun dice "Filtered Water". TM N14 actualizado: §2.11 agregado, exec summary 11 docs/4 deliveries, Response Summary 11 filas, Compilado §5 E29. DOCX regenerado.** | **GENERADO** | 15-Apr-2026 |
| 060 | Revision + Transmittal + Multi-Audit | **TM N15 GENERADO 22-Apr-2026 (P22-TM-09-000-015-0, Submittals 25007-0030 + 0031 + 0032 + 0033, E30+E31+E32+E33, 10 docs). REFINADO v3 tras multi-audit exhaustivo del Plant Control Philosophy Rev B. Veredicto global: 3 TO BE REVISED. Tally final v3: 1 Code 1 (Level Switch) + 6 Code 2 (AC Thermal, Grounding, Equipment Layout, Piping Layout, Instrument Location, GA SWRO) + 3 Code 3 (LCP, Cable Tray, Control Philosophy). Evolucion de veredictos: v1 (1+5+4) -> v2 (1+7+2 tras Equipment B y Piping B bajan a Code 2) -> v3 (1+6+3 tras Control Philosophy sube de Code 2 a Code 3 por multi-audit). Cambios materiales v2: (a) Equipment Layout B 3->2 por compromiso Civil Loading drawing 23-Apr de BW Water (email Eduardo 22-Apr 10:24 AM); (b) Piping Layout B 3->2 por retiro formal del constraint 3,500 mm CIP/dosing — superseded por plano ADASA-side P22-DWG-06-006-101 (ENTREGA 7 Van Doorn). Cambios v3: Control Philosophy B 2->3 tras multi-audit skill (10 agentes paralelos: defender, neutral, fiscal, juez, estilista, factual, estrategico, abogado, verificador, sombra) que identifico 10 findings adicionales NOTE-20..29 (1 CRITICAL + 8 MAJOR + 1 MINOR consolidado). Findings clave multi-audit: NOTE-20 CRITICAL permissive HP Pump con TAGs erroneos (VE-09-007 duplicado + VE-09-014 antiscalant tank inlet sin razon); NOTE-21 FIT-09-001 reutilizado entre feed y Stage 2 permeate; NOTE-22 salt rejection formula invertida (usa reject en lugar de feed); NOTE-23 TE-09-005/VE-09-006/VE-09-008 huerfanos; NOTE-24 4 documentos hijos sin compromiso entrega (Alarm Setpoint List, RO Sequence Chart, CIP Sequence Chart, Control Matrix); NOTE-25 SEC methodology mide bus electrico equivocado (RO PLC panel meter vs MCC); NOTE-26 network SPoF sin watchdog; NOTE-27 3 requisitos ET (manual sin PLC, VFD ramp, low-P sostenida); NOTE-28 off-spec routing sin confirmed-closed interlock + bypass OR-logic sin cross-check; NOTE-29 calidad documental (TAG inconsistencies, template residue, CCS ausente). Verificador + Auditor Sombra confianza ALTA (sin FABRICADO detectado). 29 obs nuevas totales en TM N15 (8 OBS + 21 NOTEs). 6 obs cerradas, 2 WITHDRAWN, 2 INCORPORATED, 5 heredadas abiertas. 10 PDFs CC_ADASA generados (Control Philosophy con 17 anotaciones posicionadas por search string en parrafo correspondiente). Paquete audit consolidado en `REVISIONES/TRANSMITTALES/P22-TM-09-000-015-0/audit_control_philosophy/`. Correo TM N15: PENDIENTE emitir.** | **GENERADO — pendiente envio** | 22-Apr-2026 |
| 054 | Revision | **Revision Ingenieria Detalle Mecanica Van Doorn — Entregas 4, 5 y 6 (14-Apr-2026). Documentos revisados: P&ID Alimentacion 102-C (4 obs), P&ID Reactivos 105-B (1 obs), Listado Lineas 101-B, Listado Valvulas 103-B, Listado Instrumentos 101-B. Hallazgos: OBS-01 volumen TK-06-002 (850 L vs 2,000 L Equipment List), OBS-02 ORPIT-06-001A debe ser ORPIT-09-001A (area 09), OBS-03 valvula adicional aislamiento zona VM-06-001 (tie-in planta existente), OBS-04 TAG SA-HDPE-DN110-PN10-002 duplicado en P&ID 102 y P&ID 105 (destinos distintos), OBS-05 TAGs area incorrecta en Listado Instrumentos (FIT-06-005/LS-06-002 deben ser area 09; CLIT-09-004/005 deben ser CIT). Metodologia: doc-annotator FreeText PDF + openpyxl comentarios Excel. Carpeta COMENTARIOS: INGENIERIA DE DETALLE MECANICA/ENTREGAS/ENTREGA 5/COMENTARIOS/. Decisiones: TK-06-002 aceptado como TAG Fosa Drenajes (Van Doorn reasigno desde TK-06-004 Ing. Basica). BS-06-001 omitida en planos = cambio aprobado (drenaje por gravedad SA-CPVC-DN200-PN10-001). IO List area 06 = scope E&C, no Van Doorn.** | **Documento interno** | 14-Apr-2026 |
| 048 | Revision + Correo | **Advanced Copy Equipment Layout Rev.B (P22-DWG-09-005-003) y Tie-In Point Rev.B (P22-DWG-09-005-005) — revisión ADASA 27-Mar-2026. PDFs anotados con FreeText en inglés (PyMuPDF, traducción in-place de anotaciones Spanish→English). 6 observaciones: Equipment Layout 1 obs (tank relocation), Tie-In Point 5 obs (pipe rack, dosing tank access, antiscalant loading, cutover flanges, container elevation). Correo borrador preparado: confirma reunión martes 8:30 AM hora Chile + lista puntos críticos a corregir. Script: CORREOS/Marzo 2026/2026-03-27/crear_correo_re_preliminary_layout.py.** | **BORRADOR** | 27-Mar-2026 |
| 045 | Auditoria | **Auditoria README.md + CLAUDE.md (23-Mar-2026). Desviaciones corregidas: (1) Feed TC + Interstage TC couplings marcados CERRADO en tabla Schedule y Disputas Tecnicas (TM N11 Rev D, Code 2 AN — antes figuraban como Code 4/PENDIENTE). (2) Correo Follow-Up 17-Mar actualizado de PENDIENTE ENVIO → ENVIADO. (3) Agregadas filas: Respuesta BW Water 17-Mar, Propuesta Rev.2 18-Mar, Correo Seguimiento 23-Mar. (4) Acciones ABIERTAS: propuesta Rev.2 y deadline EOB 25-Mar actualizados. (5) Nueva seccion §12 Adicionales de Ingenieria: tabla Rev.1/Rev.2, cronologia 14-23 Mar, posicion bifasica ADASA. (6) Footer actualizado a 23-Mar-2026. CLAUDE.md v5.14 confirmado preciso — sin cambios.** | **Auditoria interna** | 23-Mar-2026 |
| 044 | Revision | **Revision Logica de Control Van Doorn — incorporacion comentarios Ronald Pellejero Salazar 18-Mar-2026 (19-Mar-2026). 14 comentarios nuevos (RS-01 a RS-14) agregados al documento ADASA-Review. RS-01: tabla local/remoto 3 sistemas (PLC BW Water, PLC Planta, HMI PC). RS-02: crear documento con pantallas. RS-03: incluir pantalla variables electricas. RS-04: ADASA usa usuarios generales (sin administrador). RS-05: integrar MVE al PLC Planta para consumo especifico del sistema completo. RS-06: incluir TAG TK agua producto. RS-07: verificar logica segura en senal falla OI BW Water (par con GAP-06). RS-08: indicar TAG e instrumento (indicador vs transmisor) TK-01-001. RS-09: DO tipo rele para PLC Planta. RS-10: aclarar si parada es desde HMI PC sala control o HMI PLC Planta. RS-11: describir lazo PID como tabla con ejemplo (par con GAP-05). RS-12: BS-06-001 eliminada, seccion drenajes. RS-13: no hay inter-PLC — LS-00-002 es el unico interlock/permisivo (responde directamente a GAP-04). RS-14: verificar 3 senales pedidas a BW Water. Script: `agregar_comentarios_logica.py` — 21 comentarios ADASA insertados (IDs 1-21, 21/21). Output: `P22-IT-06-008-101-B_ADASA-Review.docx` — 25 comentarios totales (7 Luis Rivera + 14 Ronald mar + 4 Ronald feb).** | **Documento interno** | 19-Mar-2026 |
| 039 | Correccion | **TM N8 — Eliminacion nota desviacion tecnologica CIT-09-005 (11-Mar-2026): investigacion tecnica con Emerson ADS 43-018 confirma que el sensor toroidal Rosemount 228 para CIT-09-005 (Train Reject, 105–135 mS/cm) es la seleccion de ingenieria correcta — no una desviacion. Tres fundamentos: (1) umbral practico toroidal es 20 mS/cm segun Emerson (CIT-09-005 opera a 5–7× ese umbral); (2) SS316L incompatible con 45,000–55,000 ppm Cl⁻; (3) error de polarizacion de 20–50%+ a esa conductividad hace la tecnologia de 2 electrodos inviable. Conclusion: ET §5.5.5 fue redactada para servicios <40 mS/cm y no contemplo el rechazo concentrado de segunda etapa. No es una desviacion de BW Water. Cambios: TRANSMITTAL.md §3.1 OBS-3 parrafo CIT-09-005 — eliminada oracion final que pedia justificacion de desviacion; agregar_comentarios_conductivity.py — eliminado OBS-3 (228 toroidal), docstring actualizado de 3 a 2 anotaciones; DOCX y PDF CC_ADASA regenerados sin errores.** | **Correccion tecnica** | 11-Mar-2026 |
| 062 | Revision interna + Consulta tecnica | **Revision Memoria Estanque TK-06-001 (sismo vertical NCh 2369 Of.2003) — P22-IT-06-000-005-0 + P22-CT-06-000-002-0 (06-May-2026). Hallazgo del cliente: el calculo de pernos no incorpora el sismo vertical. Re-calculo independiente ADASA reproduce tb=1.510 kg de la memoria EXFIBRO Rev.A al 99,9% (procedimiento Msr/Mt/P/F p.11-12) y aplica Cv = (2/3) Cmax = 0,267 con regla 100/30; resultado: tb pasa a 1.537 kg (+1,7%), interaccion sigma+tau = 0,939 ≤ 1 → pernos M25 F1554 Gr.36 SIGUEN CUMPLIENDO. Sin embargo se identificaron 7 hallazgos formales: H1 Ez=-2.514 sin desarrollo (Cv aparente 0,20 inconsistente con Cmax=0,40), H2 formula traccion sin (1-Cv) en peso estabilizador, H3 discrepancia plano cita NCh 2369-2025 vs memoria con parametros Of.2003, H4 inconsistencia I=1,20 (p.7) vs I=1,00 (p.16), H5 combinacion 100/30 no documentada, H6 interaccion 0,92 no trazable a esfuerzos individuales, H7 peso estabilizador (W=586 vacio) no declarado explicitamente. Reaccion Ez para fundacion civil corregida: ±3.357 kg (no -2.514). Entregables: INGENIERIA DE DETALLE OOCC/REVISION ESTANQUE/{calculo_pernos_TK-06-001_ADASA.xlsx, P22-IT-06-000-005-0_Revision_Memoria_TK-06-001.docx, P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx} + copia de la consulta en REVISIONES/CONSULTAS_TECNICAS/ + correo cordial a Anwo/Exfibro en CORREOS/Mayo 2026/2026-05-06/2026-05-06_Consulta-Sismo-Vertical-Memoria-TK-06-001.docx (BORRADOR) + correo ejecutivo a L&A (Pablo Castillo) en 2026-05-06_LyA-Sismo-Vertical-TK-06-001.docx con 2 tablas (reacciones basales + solicitaciones perno) y mensaje "deltas <2%, sigan dimensionando". Ambos correos con idioma es-CL aplicado (regla CLAUDE.md §3.6 v6.8). Plazo respuesta EXFIBRO/Anwo: 10 dias habiles (Rev B memoria + ratificar reacciones).** | **Borrador interno** | 06-May-2026 |
| 061 | TdR OOCC + Indice + CLAUDE.md | **TdR OOCC P22-TR-00-010-01 emitido en Rev 1 (24-Abr-2026) con pesos operativos reales del plano BW Water P22-DWG-09-005-001 Rev A Civil and Loading Layout (Entrega 34, 22-Abr-2026). Cambios principales: contenedor 17.334 -> 14.934 kg (shell 40 ft HC modificado ≥5.000 kg + items 1-7 del plano BW 9.934 kg); CIP Tank TK-09-001 8.140 -> 10.470 kg (+28,6%); CIP Pump 385 -> 180 kg; CIP Heater 220 -> 25 kg; CIP Cartridge Filter 880 -> 267,6 kg. Tabla §2.1 ampliada de 5 a 9 filas incorporando sistema antiscalante (TK-09-002 + BDS-09-001/002) y paneles de control (Local + Heater) que comparten fundacion segun plinth #3 del plano BW. Nuevo parrafo con detalle de los 4 plinths. §5 Planos BW Water Vigentes: P22-DWG-09-005-001 Rev A como fuente primaria de pesos; Equipment Layout Rev B redescribed. Cajetin apilado (Rev 1 sobre Rev 0 historica 21/04/2026). Rev 0 archivada en ARCHIVO_REVISIONES/. Archivos: `INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/{P22-TR-00-010-01-0(...).md, crear_tdr_oocc.py, P22-TR-00-010-01-1(...).docx}`. Indice Antecedentes OOCC emitido en Rev 1 (P22-IN-00-010-001-1) incorporando el plano (PDF+DWG) en `04_PLANOS_BW_WATER_VIGENTES/`, tabla Maqueta 3D ampliada con `MODELO EXPORTADO.dwg` + `TALTAL 2da. E. - COORDENADAS CAD VND.pdf` (Van Doorn), cajetin apilado y header actualizado. Script patcher nuevo: `ANTECEDENTES/actualizar_indice_rev1.py` (clona tr XML + deepcopy para preservar formato — no hay script generador original). CLAUDE.md v6.5: §3.12 nuevo formaliza protocolo de 4 pasos para Rev N → Rev N+1 (archivar fuentes, editar en sitio, cajetin apilado, patcher para docs sin script). Memoria del proyecto actualizada: `feedback_emision_rev_docx.md` + `project_state.md`.** | **Rev 1 emitida** | 24-Abr-2026 |
| 060 | TdR OOCC + Skills | **TdR P22-TR-00-010-01-0 (Ingenieria de Detalle Obras Civiles y Estructuras Metalicas) revisado con 12 comentarios del usuario + 2 decisiones adicionales (20-Abr-2026). Cambios: (1) eliminadas secciones de licitacion (Glosario, Evaluacion de Ofertas, Vigencia/Visita/Consultas, Requisitos del Oferente); (2) Garantias/Moneda/Multas/Termino/Controversias remitidas al "contrato marco suscrito entre ADASA y el consultor" (sin numero C-4300 explicito); (3) eliminada Clausula de Suspension por antecedentes BW Water; (4) paquete de antecedentes reescrito con nombres descriptivos (Planos de sitio, Planos mecanicos y de piping, Planos de equipos con impacto civil, Documentos complementarios del modulo); (5) Figura 4-4 Georadar con nota temporal para reemplazo por ortofoto DIO 2026; (6) normativa actualizada NCh 2369 → NCh 2369:2025 (7 ocurrencias); (7) eliminadas todas las menciones a "Van Doorn" en cuerpo y matriz RACI (columna Van Doorn removida); (8) linea SA-CPVC-DN200-PN10-001 ahora referenciada a planos piping P22-DWG-06-006-103/104; (9) "alcance BW Water" → "fuera del alcance del consultor / ADASA"; (10) 4 referencias internas `§NombreSeccion` → `Seccion N — Nombre Completo` (nueva regla CLAUDE.md §2.6). Fix skill template-adasa: la carpeta local `.claude/skills/template-adasa/` era copia vieja v6.0 (Feb 2026, no symlink como decia v6.2) — generaba placeholders "RESUMEN EJECUTIVO" y "1. INTRODUCCION" en el Word. Script crear_tdr_oocc.py migrado a path GLOBAL `~/.claude/skills/template-adasa/`. Algoritmo D de anchos de columna disenado e implementado en las 3 skills (template-adasa, template-lrg, template-mba): fix bug Caso 5 (cols uniformes concentraban excedente en una sola columna → ahora distribucion proporcional al contenido), fix anchos negativos por compresion con cortas saturadas, tblLayout=fixed + gridCol DXA positivos. Tabla §4.2 Equipos (6 cols) deja de romperse. CLAUDE.md versiones v6.2 (fix inicial negativos), v6.3 (migracion path global obligatorio), v6.4 (§2.6 Referencias Internas dentro del Mismo Documento — prohibido `§NombreSeccion`, correcto `Seccion N — Nombre Completo`). Archivos: INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/{P22-TR-00-010-01-0_TDR_OOCC_EM.md, crear_tdr_oocc.py, P22-TR-00-010-01-0_TDR_OOCC_EM.docx}; ~/.claude/skills/template-adasa/table_utils.py; ~/.claude/skills/template-{lrg,mba}/md_to_*.py. DOCX regenerado (10.3 MB, 50 gridCol, 0 anchos sospechosos).** | **Documento interno + Skills globales** | 20-Abr-2026 |
| 063 | Estado + Trazabilidad | **TM N18 ENVIADO + actualización listado de entregables + trazabilidad completa (18-May-2026). (1) Correo notificación TM N18 ENVIADO a Eduardo Yamauchi + CC canónica; `.md` estado BORRADOR→ENVIADO; respaldo "Elementos enviados ... Outlook.pdf" en carpeta. (2) Master Deliverable Register `P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx` regenerado a estado TM N18 vía `generar_excel_registro_v4.py`: 5 docs re-dispositionados (#2 P&ID Rev D, #16 AC Thermal Rev C, #33 Valve List Rev D, #38 Line List Rev C = 1-Approved; #67 Control Philosophy Rev C = 3-To be revised), Revision History +5 entradas TM N18, Open Observations +TM N18 (OBS-01/02/03 + 3 entregables Sección 3), Summary recalculado, Legend/Status Date 18-May. (3) Trazabilidad sincronizada en README (§4 N1-N18, §9, tabla entregas E1-E41, post-envío), memoria de proyecto (de-stale `project_state`/`project_entregas_estado`/`project_tm18_state`/índice MEMORY.md), memoria global (puntero Taltal en Proyectos activos) y verificación de coherencia CLAUDE.md v6.12 (instrucciones estables, sin estado operativo). Hallazgo: `crear_registro.py` (Document-Status-Register DOCX narrativo) está en estado Abril, NO es companion del xlsx ni se actualiza por TM — el registro maestro vigente por entregable es el `.xlsx`.** | **Estado operativo actualizado** | 18-May-2026 |
| 065 | Correo + Trazabilidad | **Respuesta ADASA a la contra-pregunta de BW Water sobre el plano Grounding & Power Panel Location Layout Rev E (P22-DWG-09-007-003, Code 3 en TM N19) + trazabilidad (03-Jun-2026).** Billy Tan (EIC), vía Eduardo Yamauchi (02-Jun, thread "25007 Taltal: Ground cable schedule clarification"), pidió aclaraciones antes de emitir Rev F, planteando que la dependencia del Equipment Layout (TM N11 OBS-03) impediría cumplir los 14 días. **Hallazgo central:** esa dependencia la creó el propio TM N11 OBS-03 y ya está resuelta — Equipment Layout (P22-DWG-09-005-003) **y** Piping Layout (P22-DWG-09-005-004) están **Code 2 aprobados desde TM N15 (22-Abr)**; no hay Rev C formal. Correo réplica punto-por-punto (inglés, Reply-To, `Document()` directo) en `CORREOS/Junio 2026/2026-06-03/` (`crear_correo_grounding_clarification.py` + `2026-06-03_Grounding-RevF-Clarification.docx` + `_Descripcion.md`). Posiciones: (1) dependencia resuelta → proceder con Rev F sobre el layout aprobado; **main panel (LCP/Main Switchboard P22-LCP-01) fijo, no reubicable** — se rebate la nota 5 del plano ("panel locations indicative only / subject to relocation based on site condition"); (2) el Ground Cable Schedule adjunto (26 conductores) es sustancialmente completo y cierra materialmente OBS-01 → incorporarlo al Rev F (en el plano o como anexo), reconciliando Cu desnudo/trenzado/barra vs Cu/PVC aislado con el Material Take-Off del propio plano; (3) CCS description: cierre condicionado a legibilidad; (4) método de grounding designado por carga (IEC 60364-5-54) + reconciliar la inconsistencia NEC Table 250.122 (pág.2) vs IEC (pág.3); (5) revision history con descripción de cambios + ECN por cada Rev B→E; (6) screenshots permitidos si legibles. **Plazo:** extensión corta acotada del Rev F a **Mi 17-Jun-2026** (~+10 días hábiles); por instrucción del usuario **el correo NO nombra la reserva C-4300** (sólo en Ref del header) — los derechos no se renuncian por la omisión. Verificación: barrido §N=0, anti-IA manual (corregido contraste "not X, it is Y"; em-dash acotado), idioma 100% inglés, metadatos Word limpios. Trazabilidad sincronizada: README §9 (entrada 03-Jun) + esta tabla, `.md` estado ENVIADO, puntero en la carpeta CONTRA PREGUNTA del TM N19, memoria `project_tm19_grounding_clarification_revF`. | **ENVIADO + trazabilidad sincronizada** | 03-Jun-2026 |
| 064 | Correo + Trazabilidad | **Respuesta ADASA a la respuesta de BW Water al Mitigation Plan + trazabilidad (01-Jun-2026). BW Water respondió la NT-001 el 01-Jun 00:33 (tardío, parcial); ADASA emitió el mismo día un correo de réplica punto-por-punto (`CORREOS/Junio 2026/2026-06-01/crear_correo_respuesta_mitigation.py` + `.docx` + `_Descripcion.md`), encabezado por la exigencia del recovery schedule realista respaldado por vendor para Ma 02-Jun (urgente: declaración a gerencia con documentación oficial; el cronograma previo EXW 16-Aug ya no concuerda con sus respuestas). Postura mixta: Fedco/30% rechazado como causal de atraso (BAE Cl.27/31/32/35/46); ASME firme (Change Order + evidencia documental sin testigo + hitos FAT/despacho condicionados + inquietud Tier-1); FAT→SAT solo pregunta (anclada a Oferta §18 BW Water; reserva hasta tabla 15-Jun); filtro vertical FRP OK. Deadlines: schedule 02-Jun, Protec+pendientes 05-Jun, tabla FAT/SAT+ITP 15-Jun. anti-ia VERDE (U-03 corregido). Trazabilidad sincronizada: README §9 (entrada 01-Jun + cierre ciclo NT-001 §9), memorias de proyecto y memoria global.** | **ENVIADO + trazabilidad sincronizada** | 01-Jun-2026 |
| 066 | Correo + Trazabilidad | **Follow-up ADASA a Eduardo Yamauchi: Recovery Schedule vencido (04-Jun) + confirmación del waiver ASME del 02-Jun (04-Jun-2026).** Mismo thread del Mitigation Plan (`RE: 25007 Taltal - Mitigation Plan`, Reply-To del 01/02-Jun). Dos pendientes en un solo correo: (1) **persigue el Recovery Schedule actualizado** que vencía hoy y es deliverable de BW Water (no llegó) — anclado a la lógica del propio waiver (ADASA renunció al sello para recuperar ~6 semanas, así que el schedule debe construirse sobre la fecha sin estampa del **22-Jun** y declarar si 22-Jun es ex-works España o Penang + tránsito, para trazar EXW-Penang y aguas abajo); (2) **confirma recepción y reafirma el waiver ASME del 02-Jun sin re-abrir** las tres condiciones (la frase "on the terms set out in that message" las reafirma sin re-listarlas — re-presentar la alternativa la leería como waiver incondicional y diluiría el framing). Pide a Eduardo confirmar recibo y que el recovery schedule + ITP actualizado reflejen el waiver. Inglés, `Document()` directo, sin tablas (~140 palabras). Archivos: `CORREOS/Junio 2026/2026-06-04/` (`crear_correo_recovery_schedule_followup.py` + `2026-06-04_Recovery-Schedule-Request-and-ASME-Confirmation.docx` + `_Descripcion.md`). Verificación: barrido §N=0, anti-ia revisar VERDE (sin críticos; U-03 borderline 41p aceptable en registro técnico). **ENVIADO Jue 04-Jun-2026 17:57** (asunto efectivo del hilo: "RE: 25007 Taltal - Mitigation Plan - Pressure Vessel Protec"; CC efectivo acotado a 7 nombres, no la lista de ~19 del script). Sin respuesta al 08-Jun → follow-up de escalación (entrada 067). | **ENVIADO** | 04-Jun-2026 |
| 067 | Correo + Trazabilidad | **Escalación ADASA a Eduardo Yamauchi: Recovery Schedule vencido — 3er requerimiento (08-Jun-2026).** Mismo thread del Mitigation Plan (`RE: 25007 Taltal - Mitigation Plan - Pressure Vessel Protec`, Reply-To del 01/02/04-Jun). El Recovery Schedule (deliverable de BW Water) sigue sin llegar: pedido para la reunión del Ma 02-Jun, re-pedido el 04-Jun, ausente al 08-Jun. Escala el tono y fija **deadline firme anclado a la reunión semanal de mañana Ma 09-Jun**. **Palanca que el 04-Jun dejó implícita:** hace explícito que la **condición #1 ("Availability") del waiver ASME del 02-Jun** es justamente este schedule sobre la fecha sin estampa del **22-Jun** + declaración **ex-works España vs Penang + tránsito**; mientras no llegue, la condición #1 está incumplida y **el waiver no queda consolidado** (la condición #3 sólo renuncia al Change Order "provided the time saved reaches the schedule"). Pie contractual por referencia, sin re-argumentar: plazo firme y atrasos de sub-proveedor a costa de BW Water (BAE Cl.27/35/46), pagos por hitos (Cl.31). **CC ampliado:** los 7 del 04-Jun + Andrew Sia (PMO secundario). Inglés, `Document()` directo, sin tablas (~185 palabras). Archivos: `CORREOS/Junio 2026/2026-06-08/` (`crear_correo_recovery_schedule_escalation.py` + `2026-06-08_Recovery-Schedule-Escalation.docx` + `_Descripcion.md`). Verificación: barrido §N=0, anti-ia revisar VERDE (0 críticos; em dash solo en firma; oración más larga ~37p). **ENVIADA 08-Jun; la escalación funcionó: BW Water respondió el mismo día con el Project Schedule Rev A (08-Jun)** → análisis + respuesta ADASA en entrada 068. | **ENVIADO** | 08-Jun-2026 |
| 068 | Schedule + Correo + Trazabilidad | **Análisis del Project Schedule Rev A (08-Jun) + respuesta ADASA adoptándolo como baseline con reservas (09-Jun-2026).** BW Water entregó `PROGRAMA y CONTRATO/PROGRAMA DE MITIGACION/Project Schedule 08-06-26.pdf` (P22-BA-09-000-001 Rev A, aprobado EY) en respuesta a la escalación. **El punto que ADASA forzó quedó respondido:** RO pressure vessels terminan **ex-works España 23-Jun** (ID 300), con línea separada de **40 d de mar a Penang** (ID 301, llegada **02-Ago**); montaje 03-05 Ago; **EXW Penang 15-Ago**; fin **19-Nov**. Slip ~+12 d EXW vs. baseline 03-Ago (≈ Recovery 22-May), dentro de Cl.27. El waiver hace su trabajo (ruta sin estampa sostiene el 15-Ago). **Hallazgos de verificación ASME:** el schedule **no menciona ASME/estampa/certificación** (ruta sin estampa solo implícita) y **no hay tarea de prueba hidrostática/presión de los vessels** → la base sin estampa + hidrostática de fábrica + dossier + testigo en Protec deben ir al ITP actualizado. Corrección de premisa: 23-Jun = fábrica España, no Penang. Extracción citable: `Project Schedule 08-06-26_extracted.md`. **Correo respuesta ADASA** (`CORREOS/Junio 2026/2026-06-09/` — `crear_correo_schedule_revA_acceptance.py` + `.docx` + `_Descripcion.md`): adopta Rev A como baseline de recuperación trazable y pide formalizarlo en el tracker; deja por escrito la base sin estampa→ITP+hidrostática+testigo; reservas abiertas que condicionan FAT/despacho/EP-2 (25 aclaraciones NT-001, tabla FAT/SAT 15-Jun, evidencia firmada Fedco con ventana ~6 d / running test ~2 d, filtro SS316). Inglés, `Document()` directo, viñetas nativas. Verificación: §N=0, anti-ia revisar VERDE (corregido contraste "X, not Y" en apertura). **Correo ENVIADO 09-Jun** (versión ejecutiva: 1 párrafo + 5 viñetas, ASME primero). | **Analizado + correo ENVIADO** | 09-Jun-2026 |
| 069 | Transmittal + 2 Correos | **TM N20 (P22-TM-09-000-020-0) E46+E47, 20 docs + respuesta panel drawings PLC-LCP (10-Jun-2026).** Veredicto 3 — To Be Revised, 8 Code 1 + 7 Code 2 + 5 Code 3 (detalle: tabla Sección 4 fila 20). Correo 1: notificación TM cadena regular (TM + 12 CC_ADASA adjuntos). Correo 2: Reply-To al thread Yamauchi 10-Jun 9:52 (pedía aprobación expedita de los planos panel por fabricación enclosure ~6 sem) — ADASA acepta vía email-review, identifica el gate único (Panel Spec Sheet del Outline = sheet steel RAL 7035 + IP55 vs LCP Datasheet Rev B SS316L/NEMA4X/IP66 + SLD IFC + ET) y ofrece ruta expedita: confirmación escrita del enclosure del datasheet + Outline Rev B alineado ⇒ release de fabricación contra Rev B. Reversión contractual materializada: I/O List Rev 2 → Code 3 (Rev D 4º ciclo, ventana 14d vencida 08-Jun). Master Register regenerado a N19+N20 (99 ítems, Summary/Legend verificados). Verificación: anti-ia VERDE, §N=0, 12 CC_ADASA verificados por conteo + render PNG (página rotada Schedule OK), día de semana verificado (Mié 10-Jun). | **AMBOS ENVIADOS** | 10-Jun-2026 |
| 070 | Transmittal | **TM N21 (P22-TM-09-000-021-0) ENVIADO 11-Jun-2026: Submittal 25007-0048 (E48), 2 docs. Grounding Point & Power Panel Location Layout Rev F **Code 1** (schedule de 48 conductores embebido cierra el item más antiguo del paquete eléctrico ~88d, 3 ciclos); Datasheet PLC/HMI Panel Component Rev B **Code 3** (sin vía de adquisición HART para la instrumentación 4-20mA+HART de la ET; +reconciliar módulos RTD 5069-IY4; typo portada "PD Tattal"). Query Modbus de TM N1 cerrada (gateway ProSoft PLX32 en Control System Architecture Rev B). 2 CC_ADASA.** | **3 - To Be Revised** | 11-Jun-2026 |
| 071 | Transmittal | **TM N22 (P22-TM-09-000-022-0) ENVIADO 15-Jun-2026: Submittals 25007-0049 (E49) + 25007-0050 (E50), 7 docs. Tally 2 Code 1 + 1 Code 2 + 4 Code 3, veredicto 3. Plant Control Philosophy Rev D **Code 3** (permissive CRITICAL del HP Pump CERRADO + salt-rejection corregida a feed conductivity + SEC 4.71 + HART confirmado, pero Sequence Charts/Setpoint List/Control Matrix no entregados, 6º ciclo); Equipment Layout Rev C **Code 3** (RO Cartridge Filter ítem 2 sigue horizontal vs su Datasheet Rev E vertical / NT-001 5.C; calibración usuario: el layout no se revisa contra puertas del container sino contra orientación del vessel); CIP Cartridge Filter Rev D **Code 3** (gasket/FRP vs CIP pH 2-12 sin documentar, TM N19 OBS-03 sin cerrar); HMI Display Screenshot Rev A **Code 3** (set de pantallas incompleto; cierra materialmente TM N4 NOTE-05, el compromiso abierto más antiguo ~127d); Static Mixer Rev C **Code 2**; RO Cartridge Filter Rev E + Utility Consumption List Rev C **Code 1** (datasheet correcto as-is, cert de material FRP al dossier de fabricación del vessel, no Code 2 — calibración usuario). 5 CC_ADASA (4 Code 3 + 1 Code 2). Workflow a medida tm22-review-e49-e50 (42 agentes) + calibración doc-por-doc. Master Register -002-0 a N22 (4 hojas). **Versión ejecutiva** (§1/§2 condensados); **Section 3 = 3 carry-forward más graves** (resto al Master Register); **ASME ya waived/aceptado** (02/09-Jun + schedule Rev A) — el transmittal no lo reabre, lo abierto es el ITP. Correo ejecutivo corto CORREOS/Junio 2026/2026-06-15/. ENVIADO.** | **3 - To Be Revised** | 15-Jun-2026 |
| 072 | Correo + Trazabilidad | **Correo de accountability (Parte 1) — compromisos de la minuta del 16-Jun no cumplidos al lunes 22-Jun. ENVIADO 22-Jun-2026** (Reply a `RE: 25007 Taltal: Meeting Notes`, To/CC del correo 17-Jun). Reclama 3 entregables pendientes: spare parts quotes + ex-work shipment details (ambos comprometidos para "next Monday") + invoice/payment status update (estado de pago); más fabrication schedule con fechas y columna "material received" al schedule (acusa fotos + super duplex ya cumplidos). Tono firme profesional, sin citar cláusulas. Fedco fuera (a memoria/seguimiento, ver TM-N22/cross-check). Cuerpo por `anti-ia revisar` → VERDE antes del Word. Reemplazó al correo amplio `2026-06-22_Procurement-Review.*` (eliminado). Respaldo `correo enviado a BW WATER.pdf`. Análisis de respaldo: `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 22-06-26/CROSS-CHECK_ADASA_22-06-26.md`. Archivos: `CORREOS/Junio 2026/2026-06-22/`.** | **Enviado** | 22-Jun-2026 |
| 073 | Transmittal | **TM N23 (P22-TM-09-000-023-0) ENVIADO 18-Jun-2026: E51+E52 (25007-0051/0052), 7 docs paquete QA/fabricación. Veredicto 3 — To Be Revised, 0 Code 1 + 1 Code 2 + 6 Code 3. Driver: RO Vessel Hydrostatic Test Procedure Rev A (45,5 bar vs 1.980 psi del ITP/waiver). Cierre positivo: ITP Rev C cierra materialmente el ítem de fabricación más antiguo (base del waiver ASME). 7 CC_ADASA. Correo `crear_correo_tm23.py`.** | **3 - To Be Revised** | 18-Jun-2026 |
| 074 | Transmittal | **TM N24 (P22-TM-09-000-024-0) ENVIADO 23-Jun-2026: E53+E54 (25007-0053/0054), 5 docs I&C/eléctrico + CIP filter. Veredicto 2 — Approved as Noted, 3 Code 1 + 2 Code 2. CIP Cartridge Filter Rev E cierra el Code 3 del TM N22. IO List Rev 3 y LCP Datasheet → Code 2. Re-tono OBS-01: las señales de interfaz falla/local-remoto son pedido NUEVO de ADASA (solo 2 se habían pedido, cerradas N19), no incumplimiento — con tabla de 4 señales. HART retirado/cerrado (over-reach: la ET pide instrumentos 4-20mA+HART, cumplido, no decodificación central). Workflow tm24-review 46 agentes; 2 CC_ADASA + hipervínculo de descarga; Master Register a N24. Ver [[project_tm24_state]].** | **2 - Approved as Noted** | 23-Jun-2026 |
| 076 | Correo + Trazabilidad | **Correo de insistencia: minuta de la Weekly Coordination Call del 23-Jun + compromisos Fedco. ENVIADO 25-Jun-2026** (Reply-All al thread `25007 Project Taltal - Weekly Coordination Call`). ADASA pidió la minuta el mismo 23-Jun y no obtuvo respuesta; este correo insiste con fecha firme (la minuta para el **Vie 26-Jun**) y, sobre todo, deja por escrito en el propio hilo los dos compromisos de esa reunión: (1) **cronograma re-secuenciado** que absorbe el slip de Fedco (BH-09-001 + SIP-09-001/002); (2) **reporte oficial, en formato de reporte, del por qué y cómo ocurrió el retraso de Fedco** + acciones de recuperación. Exige confirmar la fecha de emisión de cada entregable para el 26-Jun. **Decisión de diseño:** el correo no depende de que BW Water emita la minuta — fija el registro contractual de los compromisos en el hilo. Foco acotado (no reabre los pendientes del 22-Jun, cadena separada del thread Meeting Notes 16-Jun). Cuerpo `Document()` directo, 100% inglés, sin proponer reunión; `anti-ia revisar` VERDE; metadatos Word limpios; día de semana verificado (26-Jun = viernes). Respaldo `ENVIADO A BW WATERS.pdf`. Archivos: `CORREOS/Junio 2026/2026-06-25/`. Ver [[project-procurement-22jun]], [[project_fedco_fat_conflict_14may]]. | **ENVIADO** | 25-Jun-2026 |
| 075 | RFI + Correo | **RFI-001 (25007-RO-RFI-0001) respondido — confirmación HART (24-Jun-2026).** BW Water (Billy Tan, 22-Jun) preguntó formalmente si el módulo de entrada analógica Allen-Bradley **5069-IF8**, leyendo solo 4-20 mA con HART accesible por comunicador handheld en el lazo (sin pass-through al PLC/SCADA), cumple la ET Sección 5.5 — Instrumentation Specification ("4-20 mA + HART"). **Respuesta ADASA: sí cumple.** La ET exige 4-20mA+HART **a nivel de instrumento**; NO exige decodificación/pass-through HART central, módulos I/O HART-capable ni asset management dedicado (búsqueda en la ET: 0 menciones) → sin impacto de costo/plazo. Confirmación **condicionada** a que todo instrumento sea 4-20mA+HART (un instrumento solo-4-20mA sin HART no cumple — precedente IFM VTV122 vivo). Consistente con el cierre positivo del TM N24, sin reabrir el over-reach del TM N21 OBS-01. Form RFI llenado round-trip (sección Replied Information); original respaldado. Verificación: workflow `rfi001-hart-verify` (4 verificadores + síntesis: APROBADO, 4/4 PASS, 0 obligatorias) — exacto vs ET, fiel al TM N24, sin fugas internas, condición instrumento-a-instrumento preservada; §N=0, sin Van Doorn, metadatos limpios. Archivos: `PROGRAMA y CONTRATO/RFI/RFI 1/` (`..._ADASA_REPLY.docx` deliverable + `..._ORIGINAL.docx.bak` + `RFI-001_REPLY_ADASA.md` + `llenar_rfi_reply.py`) + correo de cobertura ENVIADO `CORREOS/Junio 2026/2026-06-24/`. Ver [[project_hart_precedente]]. | **ENVIADO** | 24-Jun-2026 |
| 077 | Transmittal | **TM N25 (P22-TM-09-000-025-0) ENVIADO 29-Jun-2026: E55+E56 (25007-0055/0056), 6 docs. Veredicto 3 — To Be Revised, 4 Code 1 + 1 Code 2 + 1 Code 3.** Driver único Code 3: **PLC-LCP Outline Panel Drawing Rev B** (gate de fabricación del enclosure aún abierto — agregó "Exterior SUS316L" + A/C sellado + peso 814 kg, pero MATERIAL/FINISHING describen sheet steel pintado bajo "interior only" pese al SUS316L; re-issue Rev C). **IO List Rev 4 Code 2** (Approved as Noted): las **4 señales de coordinación con el PLC externo cumplidas** (cierra OBS-01 N24); única nota = celda de conteo dosificadoras (menor, fold a Rev 0). **Re-verdict del usuario 29-Jun:** la OBS-01 inicial ("RUNNING soft BOOL desde HMI = no feedback", que había dejado el IO List en Code 3) era **over-reach con premisa falsa** — esa señal nunca fue hardwired aceptado; ADASA misma pidió relabelearla DI→soft en N20 NOTE-02 y N24 NOTE-01 declaró el esquema Ethernet/IP "no se reabre" → retirada; queda solo la celda de conteo + NOTE de fuente. Cierres Code 1: LCP Rev 1 (N24), UHPRO Structural Rev B (N23: NCh 2369:2003 + criterios de izaje), Static Mixer Rev 0 (N22), Painting Spec Rev C (Jotun condicionado + cambio de código 005-002→006-002, NOTE-03). Workflow `tm25-review` (22 agentes adversariales); **el cruce con el Master Register corrigió 2 premisas del workflow** (Static Mixer y Painting NO eran nuevos — re-revisiones). 2 CC_ADASA (IO List Code 2 + Outline Code 3, placement por render PNG). Master Register a N25 (46/21/12/0; backup `_pre-N25`). Correo de remisión escala los vencidos (Grounding Rev F, FAT/SAT, Control Philosophy hijos, planos de ruta) con deadline **Vie 03-Jul**; ENVIADO con transmittal + 2 CC_ADASA adjuntos (link Synology inválido removido), respaldo PDF en la carpeta. Ver [[project_tm25_state]], [[feedback_soft_io_ethernet_aceptado_n20]], [[reference_et_tableros_nema4x_no_ss316l]]. | **3 - To Be Revised (ENVIADO)** | 29-Jun-2026 |
| 078 | Correo | **Correo Fedco — reporte formal de causas pendiente. ENVIADO 29-Jun-2026** (Reply-All al thread `25007 Taltal - Schedule Update` del 26-Jun; respaldo `Re: 25007 Taltal - Schedule Update.pdf` en la carpeta). BW Water entregó el 26-Jun (`PROGRAMA 26-06-26/`) solo el cronograma `.mpp` + un "Progress Update" (Gantt impreso) + una **narrativa de causas en el cuerpo del correo** — NO el **reporte formal** que ADASA pidió el 25-Jun (compromiso de la call 23-Jun: root cause + sequence of events + recovery actions). Problemas: el cronograma **propaga** el slip (shipping 15-Ago→10-Sep) en vez de absorberlo; Penang **02-Sep** es posterior al 21-Ago ya rechazado el 17-Jun y reabre el conflicto FAT/running-test (NT-001); sin respaldo documental del vendor; **atribuyen la causa al "delayed down payment received on 09 June"** (anticipo 30% que ADASA fijó como costo BW Water). El correo exige el **reporte formal por Vie 03-Jul** con 4 contenidos (fecha conciliada con carta/PO Fedco; causa+secuencia con documentos; acciones de recuperación + lugar del running test Penang/SAT con costo; plan ruta crítica LCP). **Postura (decisión usuario):** firme + reserva de posición, referencia medida al régimen de atraso sin citar cláusulas; sobre el down-payment **pide sustanciación SIN rechazar** (reserva "does not accept any allocation by implication"; disputa del anticipo a vía separada). Verificación: workflow `fedco-email-audit` **VERDE 0 obligatorias** (postura/contractual/factual/tono) + anti-IA (binarios y em-dash reducidos, mantiene `not "as advised"`). Ver [[project_fedco_fat_conflict_14may]], [[project-procurement-22jun]]. | **ENVIADO** | 29-Jun-2026 |

---

### Registro QA — Errores de Nomenclatura BW Water

Errores recurrentes detectados en documentacion BW Water. **Verificar contra esta lista en cada revision** — especialmente al revisar Valve List, P&ID, Instrument List y Control Philosophy.

#### 13.1 TAGs Duplicados (Valve List)

**Regla critica:** Cada TAG debe ser unico en toda la lista. Mismo TAG en distintos items impide identificacion univoca en PLC — es falla QA critica.

| TAG | Items en conflicto | Deteccion | Estado |
|-----|-------------------|-----------|--------|
| VM-09-015 | Item 18 (DN100, Butterfly, MOTORIZED, ANSI 900#) vs Item 43 (DN15, Ball, MANUAL) | TM N3 OBS-12 / TM N6 OBS-01 | CERRADO en Rev C (TM N11) |
| VE-09-008 | Item 44 (DN80, ANSI 900#, CE3MN) vs Item 57 (DN80, ANSI 150#, DI/SS420) | TM N3 OBS-12 / TM N6 OBS-02 | CERRADO en Rev C (TM N11) |
| VE-09-009 | Item 58 (DN80, ANSI 900#) vs Item 93 (DN25, ANSI 150#, PVC) | TM N6 — nuevo en Rev B | CERRADO en Rev C (TM N11) |
| VM-09-065 | Item 30 (DN65, Permeate) vs Item 76 (DN150, PVC, CIP) | TM N6 — nuevo en Rev B | CERRADO en Rev C (TM N11) |
| VE-09-007 | Item 44 vs Item 64 — nuevo en Rev C | TM N11 OBS-01 | **PENDIENTE Rev D** |
| PSV-09-002 | Item 105 vs Item 112 — nuevo en Rev C | TM N11 OBS-02 | **PENDIENTE Rev D** |
| FIT-09-001 | Instrument List: Cartridge Filter vs 2nd Stage Permeate | TM N3 OBS-05 | CERRADO — renombrado FIT-09-002 (17-Feb-2026) |

#### 13.2 Prefijo de Actuacion en Valvulas BW Water (VM / VE)

**Codificacion BW Water:** `VE` = valvula electrica/motorizada | `VM` = valvula manual

| Error | Deteccion | Estado |
|-------|-----------|--------|
| VM-09-015 declarada manual en Valve List Rev A — ET §5.2.3 requiere electrica (linea principal proceso DN100 ANSI 900#) | TM N3 OBS-11 | CERRADO + OBS-11 WITHDRAWN 05-Mar-2026. VM-09-015 confirmada manual — ADASA retiro el requisito de actuacion electrica. P&ID Rev B correcto (prefijo VM = manual). |
| Valve List Rev B item 18 registra VM-09-015 como ON/OFF MOTORIZED — contradice funcion manual confirmada (OBS-11 WITHDRAWN 05-Mar-2026). P&ID Rev B correcto (VM = manual). | TM N9 / correo 13-Mar-2026 | CERRADO en Rev C (TM N11). Item 18 renumerado a VM-09-151, declarado MANUALLY ACTUATED VALVE / MANUAL HAND. |

#### 13.3 Codigo de Area en TAGs BW Water

**Regla:** Area 09 = modulo BW Water. Area 06 = suministro ADASA. Area 07 no corresponde a ninguna de las partes en este proyecto.

| TAGs con error | Error | Deteccion | Estado |
|----------------|-------|-----------|--------|
| VM-07-005, VM-07-031, VE-07-009 | Area "07" en lugar de "09" — Valve List | TM N3 OBS-13 / TM N11 NOTE-01 | **PENDIENTE Rev D** (VM-07-005 persiste en Rev C) |
| VE-07-014 (tabla instrumentos CP) vs VE-09-014 (texto operacional CP) | Area inconsistente dentro del mismo documento | TM N7 | **PENDIENTE Rev B Control Philosophy** |

#### 13.4 Inconsistencias de TAG Dentro del Mismo Documento

| TAG | Documentos | Deteccion | Estado |
|-----|-----------|-----------|--------|
| VE-07-014 / VE-09-014 | Control Philosophy Rev A: misma valvula con dos areas distintas | TM N7 | PENDIENTE Rev B |
| VE-07-016 / VE-09-016 | Control Philosophy Rev A: misma valvula con dos areas distintas | TM N7 | PENDIENTE Rev B |
| Tags antiscalant dosing | Discrepancia menor en tags entre secciones del Control Philosophy | TM N7 (MINOR) | PENDIENTE Rev B |

#### 13.5 Codigos de Señal No Definidos en Sistema P22

| Codigo | Contexto | Deteccion | Estado |
|--------|---------|-----------|--------|
| `BT` | Usado en Control Philosophy Rev A como tipo de señal — no esta definido en codificacion P22 del proyecto | TM N7 | PENDIENTE Rev B |

#### 13.6 Codigos de Documento — Title Block

| Error | Afecta | Deteccion | Estado |
|-------|--------|-----------|--------|
| P&ID title block muestra codigo con "-02" en lugar de "-002" (3 digitos requeridos por P22) | P22-DWG-09-009-002 | TM N9 NOTE-01 (MINOR) / correo 13-Mar-2026 | **PENDIENTE Rev C P&ID** |

#### 13.7 Convencion de Nomenclatura de Equipos

| TAG Incorrecto | TAG Correcto | Razon | Fuente |
|----------------|--------------|-------|--------|
| BH-09-003 | SIP-09-001 | Turbocharger usa convencion FEDCO (SIP=), no convencion bomba (BH=) | Datasheets P22-ITEM-09-009-007-A, confirmado 26-Feb-2026 |
| BH-09-004 | SIP-09-002 | Idem | Datasheets P22-ITEM-09-009-008-A, confirmado 26-Feb-2026 |

> **Nota:** BH-09-001 (HP Pump) y BH-09-002 (CIP Pump) son correctos — confirmados en datasheets Rev B.

#### 13.8 TAGs Propuestos EVI — Resolucion Provisional de Duplicados

Para el Listado Consolidado EVI (`LISTADO-CONSOLIDADO-EVI.xlsx`), cuando un TAG esta duplicado en el documento BW Water vigente se asigna el siguiente correlativo disponible de la serie. Sin notas al usuario final — el listado muestra el TAG propuesto como definitivo.

**Criterio:** siguiente entero tras el maximo usado en la serie (no rellenar gaps — pueden estar reservados en BW Water).

| TAG en doc BW Water | Servicio | TAG propuesto (listado EVI) | Base |
|---------------------|----------|----------------------------|------|
| VE-09-007 (item 64) | 1st Stage Reject to 2nd Stage | **VE-09-017** | VE-09-016 era el maximo (18-Mar-2026) |
| PSV-09-002 (item 112) | RO Permeate | **PSV-09-003** | PSV-09-002 era el maximo (18-Mar-2026) |

> **Solo para este listado.** En transmittals, correos y documentos oficiales los duplicados siguen PENDIENTES hasta que BW Water confirme en la revision siguiente.

---

### Adicionales de Ingeniería — Propuestas Comerciales BW Water

#### Propuesta 25007-PL-0001 — CIP Layout / Piping Layout / 3D Model

| Revision | Fecha | Documentos | Precio | Estado |
|----------|-------|-----------|--------|--------|
| Rev.1 | 14-Mar-2026 | 7 docs (Piping Layout, Tie-In, Equipment Layout, 3D Model, Instrument Layout, Grounding Layout, Cable Tray Layout) | USD 6,539 | IMPUGNADA PARCIALMENTE por ADASA |
| Rev.2 | 18-Mar-2026 | 6 docs (Cable Tray Layout retirado) | USD 5,766 | RECIBIDA — pendiente cierre bifasico |

**Cronologia:**

- **14-Mar-2026:** BW Water somete Rev.1 — 7 documentos, USD 6,539, 2 semanas leadtime.
- **16-Mar-2026:** ADASA acepta 4 documentos con dependencia tecnica evidente (Piping Layout, Tie-In Points, Equipment Layout, 3D Model); impugna 3 (Instrument Layout, Grounding Layout, Cable Tray Layout — sistemas interiores no afectados por relocalizacion CIP exterior). Solicita propuesta revisada EOD 16-Mar. Eduardo acusa recibo: "We confirm the receipt of the email and will prepare the response by EOD." — sin respuesta sustantiva ese dia.
- **17-Mar-2026:** ADASA follow-up (deadline EOD 17-Mar). BW Water responde: justifica Instrument Layout y Grounding Layout (dependencia tecnica CIP), retira Cable Tray Layout sin cargo. Adjunta Rev.2.
- **18-Mar-2026:** Rev.2 recibida: 6 documentos, USD 5,766, mismas condiciones comerciales.
- **23-Mar-2026:** ADASA somete posicion bifasica via correo semanal (deadline BW Water: EOB 25-Mar-2026).

**Posicion ADASA — cierre bifasico (23-Mar-2026):**

- **Fase 1 — lista para cierre comercial:** Piping Layout Rev B, Tie-In Points Rev B, Equipment Layout Rev B, 3D Model.
- **Fase 2 — contingente a Fase 1:** Instrument Layout Rev B y Grounding Layout Rev B. Ambos con Code 3 bajo TM N11 (OBS-03 y OBS-04 — MAJOR) por heredar disposicion del Piping Layout Rev A rechazado (11,150 mm vs ≤3,500 mm TM N5). No pueden cerrarse antes de entregar Piping Layout Rev B conforme.

**Fundamento contractual:**
- TM N5 (23-Feb-2026): establece limite 3.5 m para CIP exterior — formalmente notificado 8 dias antes de la entrega del Piping Layout.
- Piping Layout entregado 06-Mar-2026 (66 dias tarde vs deadline original 30-Dic-2025) con 11,150 mm (3x el limite TM N5).
- La correccion requerida es responsabilidad de BW Water (no modificacion solicitada por ADASA).

**Archivos de respaldo:**
- `CORREOS/Marzo 2026/2026-03-16/2026-03-16_Response-Layout-Proposal.md` — posicion ADASA Rev.1
- `CORREOS/Marzo 2026/2026-03-17/2026-03-17_Followup-Layout-Proposal.md` — follow-up + respuesta BW Water
- `PROGRAMA y CONTRATO/ADICIONALES DE INGENIERIA/25007-PL-0001_rev.2.pdf` — propuesta Rev.2
- `CORREOS/Marzo 2026/2026-03-23/2026-03-23_Seguimiento-Procurement-Layout.md` — posicion bifasica ADASA

---

### Revisión Visual del BL (revisor-docx v2.1.2)

A partir del 28-May-2026 el ciclo de revision interna del **BL Montaje Mecanico y OOCC** usa la skill global `revisor-docx` v2.1.2 como herramienta de auditoria visual + exportacion de comentarios al ciclo FONDO/FORMA.

**Comando:**
```
/revisor-docx "BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/BL_MONTAJE_TALTAL_REV0.docx"
```

El skill arranca un mini server HTTP local (`serve.py` en `127.0.0.1:47823`), abre el browser con el .docx ya cargado y detecta automaticamente que viene de `template-adasa` via cascada de 5 pasos. Auto-completa el campo `Comando regenerar` con el preset de la skill template y prefilla el `Nombre del documento` desde el filename normalizado (`BL MONTAJE TALTAL REV0`).

**Flujo de iteracion para futuras revisiones del BL:**

| Paso | Accion |
|------|--------|
| 1 | Editar `.md` fuente del BL (carpeta `BASES DE LICITACION MONTAJE MECANICO-OOCC/md/`) |
| 2 | Generar `.docx` con `template-adasa` (`md_to_adasa_docx.py`) |
| 3 | `/revisor-docx <path>` → revisar visualmente, seleccionar texto, agregar comentarios |
| 4 | Categorizar: **FONDO** (cambios al `.md`) / **FORMA** (cambios al template/Word) |
| 5 | Exportar `FONDO → .md` y/o `FORMA → template`, pegar el prompt en Claude Code |
| 6 | Regenerar el `.docx` y comparar con el JSON guardado para confirmar que las observaciones se atendieron (`⇆ Comparar`) |

**Trazabilidad de la validacion 28-May-2026** (BL Rev 0 como caso real):
- El BL Rev 0 sirvio como primer documento ADASA de produccion para validar el revisor end-to-end.
- La validacion expuso 3 bugs en cascada que se cerraron el mismo dia:
  - **v2.1**: detector miraba solo 5 KB de `document.xml`; firma `Aguas de Antofagasta` esta en pos 5863 del BL. Cascada ampliada a 5 pasos (filename + `docProps/app.xml` + headers/footers con `descr="…ADASA"` + ventana 50 KB + styles).
  - **v2.1.1**: `renderComments` destruia `<div id="emptyMsg">` con `innerHTML=''`; segundo comentario tiraba TypeError. Resuelto con remocion selectiva por clase de card.
  - **v2.1.2**: zoom solo afectaba la portada porque `docx-preview` con `inWrapper:true` no genera wrapper unificador. Resuelto con `getDocxScaleTargets()` iterativo sobre todas las paginas.
- Bug colateral pendiente (no bloqueante): `fix_app_xml()` de `template-adasa\docx_metadata.py` no setea `<Company>` correctamente. Detector funciona igual via pasos 3 y 4 de la cascada.

**Documentacion adicional:**
- `~/.claude/skills/revisor-docx/SKILL.md` — referencia canonica del skill (cascada de deteccion, server lifecycle, microcopy, ciclo FONDO/FORMA).
- `~/.claude/skills/revisor-docx/CHANGELOG.md` — historial v2.0 → v2.1 → v2.1.1 → v2.1.2.
- `~/.claude/skills/template-adasa/SKILL.md` seccion **"Revision visual con `revisor-docx`"** — flujo desde la perspectiva de template-adasa.
- Memorias relacionadas: `reference_revisor_docx_v212.md`, `project_revisor_visual_BL_taltal.md`.

---

*Ultima actualizacion: 28 de mayo de 2026 - Seccion 14 nueva: ciclo de revision visual del BL Montaje Mecanico via `revisor-docx v2.1.2`. Validacion end-to-end con BL Rev 0 expuso y resolvio 3 bugs en cascada (detector, renderComments, zoom). Las 3 skills template (template-adasa/lrg/mba) actualizadas a requisito minimo `revisor-docx v2.1.2+`.*

*Ultima actualizacion previa: 20 de abril de 2026 - TdR OOCC P22-TR-00-010-01-0 revisado con 12 comentarios + 2 decisiones (Van Doorn fuera; clausulas comerciales al contrato marco). Skill template-adasa global v7.3+ confirmada como unica fuente; copia local obsoleta reemplazada. Algoritmo D de anchos de columna disenado e implementado uniforme en las 3 skills (template-adasa/lrg/mba) — fix bug Caso 5 (cols uniformes) y anchos negativos. Regla CLAUDE.md §2.6 nueva: referencias internas `Seccion N — Nombre Completo` en vez de `§NombreSeccion`. CLAUDE.md v6.2 → v6.3 → v6.4. §8 entrada 060 + §11 historial versiones actualizado.*
