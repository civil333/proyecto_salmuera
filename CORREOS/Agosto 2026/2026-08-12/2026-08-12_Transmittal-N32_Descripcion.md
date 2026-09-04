---
titulo: Correo de cobertura del Transmittal N32
codigo: P22-TM-09-000-032-0 — submittal 25007-0075
fecha: 2026-08-12
estado: ENVIADO
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-08-12
---

# Correo de cobertura — Transmittal N32 (submittal 25007-0075)

**Estado: ENVIADO** el miércoles 12-Ago-2026 a las 15:30, respaldo en `correo del transmiital 32.pdf`.

| Campo | Valor |
|---|---|
| Archivo | `2026-08-12_Transmittal-N32.docx` · una página · inglés |
| Para | Eduardo Yamauchi (BW Water) |
| CC | Andrew Sia, Magdier Arias, Víctor Gutiérrez, Jeryl F. Regulacion, Jorge Guevara, Ronald Pellejero, Stephane Gehant |
| Asunto | 25007 Taltal - Technical Review Transmittal N32 - submittal 25007-0075 |
| Cadena | Cadena regular de revisión documental. Separada del hilo de repuestos y del hilo del tercero inspector |
| Adjunto | `TRANSMITTAL N32 ADASA-BW_WATER.pdf` |
| Por enlace | Los tres `CC_ADASA` de los documentos con Código 3, listados en la Sección 4 del transmittal. Enlace aplicado el 12-Ago en el transmittal y en el correo, idéntico en los dos |
| Script | `crear_correo_tm32.py` |


## Envío

**ENVIADO el 12-Ago-2026 15:30.** Asunto real: *"ADASA – Taltal Brine Module: Technical Review Transmittal N32 (25007-0075)"*. To: Fitri Indriyani, Eduardo Yamauchi y los tres de ADASA; CC: la distribución completa del hilo de submittals, once direcciones de BW Water. Es el reply-all del hilo, que es lo correcto, y no la lista que declaraba el script.

**El primer párrafo sale más corto que en el borrador, por edición del usuario al enviar.** Termina en *"It responds to submittal 25007-0075"*: el recuento y el *"Overall verdict: 3 - To be revised"* se quitaron a propósito, porque el veredicto va en el transmittal adjunto y repetirlo en el cuerpo es la duplicación que este correo vino a eliminar. No es una pérdida de pegado.

🔴 **El párrafo del enlace de descarga no aparece en el enviado.** Es la tercera vez que ocurre tras el N30 y el N31, aunque aquí no está confirmado que sea el pegado y no una edición más. Los tres `CC_ADASA` siguen alcanzables por el enlace **impreso en la Sección 4 del PDF adjunto**, que es exactamente para lo que se imprime ahí. **Confirmar si conviene responder el hilo con el enlace en texto plano.**

## Cuerpo

**266 palabras.** Ejecutivo por pedido del usuario: el correo no repite lo que va en el adjunto.

1. **Una línea:** qué es, a qué submittal responde, recuento y veredicto.
2. **Disposición**, una viñeta por documento con el código y la acción en una cláusula. Es el índice escaneable, lo único que el lector necesita antes de abrir el PDF.
3. **Una frase de método:** cada bloque de acción de la Sección 2 separa lo que bloquea al inspector de lo que se corrige en la misma emisión, para que la Rev B no espere un ciclo completo.
4. **El único punto que no está en los documentos:** los ensayos de penetrantes del 7 de agosto se hicieron bajo un procedimiento que llega recién en esta entrega. Se pide declarar qué registros existen y bajo qué criterio se evaluaron.
5. **Plazo en una línea:** viernes 21 de agosto, per Cláusula 37.2.

### Qué se sacó y por qué

| Bloque eliminado | Dónde vive ahora |
|---|---|
| Por qué dos documentos vuelven sin código | Resumen ejecutivo del transmittal, párrafo propio |
| La cita de la ET Sección 8 y del NDE Plan Rev C como fuente del criterio de aceptación | Resumen ejecutivo y Sección 2 del transmittal |
| El detalle del `RAL 5010` contra el `RAL 5012` y de la especificación aprobada | Subsección 2.4 del transmittal |
| El detalle del formulario del ensayo y la fila 5.2 del ITP | Subsección 2.3 del transmittal. Además ya se pidió operativamente en el correo conjunto a Bureau Veritas, que es otra cadena |
| La explicación del plazo de la Cláusula 37.2 | Resumen ejecutivo del transmittal; en el correo queda solo la fecha |

El correo pasó de 643 a 266 palabras sin perder ninguna petición: las siete acciones siguen enunciadas en la disposición, y la única pregunta que el transmittal no contesta por sí sola —los registros de penetrantes— es la que se destaca.

## Verificación de fuentes

| Afirmación | Fuente |
|---|---|
| Criterio de aceptación del circuito de alta en super dúplex | NDE Plan `P22-BA-09-000-005` Rev C, Código 1 en el TM N26 |
| RAL 5012 Luminous Blue para el soporte estructural dentro del contenedor | Painting Specification `P22-ET-09-006-002` Rev C, ítem 4 |
| RAL 5010 Gentian Blue en el formulario | Painting Procedure Rev 0 del 11-Ago, página 11, verificado por render PNG |
| El ensayo hidrostático de alta presión es punto de detención | ITP `P22-BA-09-000-004` Rev 0, fila 5.2 |
| Jornada de inspección del 13 y 14 de agosto | `AQ-QAM-F027 Inspection Request (003)` |
| Siete días hábiles desde la recepción | BAE 12803, Cláusula 37.2 |
| Los tres procedimientos responden a un pedido de ADASA | Sección 2 del TM N30, bloque de acción del Dossier Index |

## Contexto Interno (No enviar)

- **Los cuatro Rev 0 se juzgaron solo por las peticiones del 06-Ago.** Todo lo demás verificado —las tres regresiones que la Rev D del procedimiento de presión introdujo y que ADASA aprobó sin detectar, el encuadre de refinería que sobrevive en el PMI más allá de las dos cláusulas de extensión, la numeración de referencias del Visual— vive en `ENTREGAS_BWWATER/ENTREGA 75/_HALLAZGOS_DETERMINISTAS.md` y no se emite. Levantarlo reabriría aprobaciones propias.
- **El PMI terminó en Código 1 tras el triaje.** Contestaron las dos cosas que se les pidieron: la declaración de aplicabilidad al proyecto está en la cláusula 2.0 del frontispicio y la base de aceptación en la 13.4. Exigir además que la cláusula 8.1 y el Apéndice 1 dejen de citar PTS 15.02.01 era leer más estricto que la instrucción escrita. Lo que queda va como aseo a la Sección 3.
- **El color del formulario de pintura es el punto de mayor consecuencia inmediata.** La inspección de preparación no mide color, de modo que no bloquea la jornada del 13 y 14; el riesgo es que la capa de terminación se aplique contra un formulario que declara RAL 5010. Si BW Water responde que el formulario es un ejemplo en blanco, la respuesta es que fue rellenado a pedido de ADASA y por eso su contenido gobierna.
- **El espesor por capa del formulario de pintura se deja pasar.** BW Water contestó que el formulario adjunto es una muestra y que los valores reales se llenan en el informe del día. Es una lectura razonable de una petición que decía "print the nominal values" sin distinguir criterio de aceptación de registro. El transmittal lo replantea una vez con esa distinción, reconociendo su respuesta.
- **Las erratas del procedimiento de presión salieron.** ADASA pidió "edition and addenda"; addenda no existen y las erratas nunca se pidieron.
- **Ningún documento que venía de Código 2 se codifica 3.** Decisión del usuario del 12-Ago: contradice la aprobación propia. Los tres que no cerraron vuelven sin código, con los puntos íntegros en su subsección, como el N31 hizo con la Plant Control Philosophy.
- **El formulario del ensayo de presión se pidió solo por correo el 06-Ago y no se contestó** (`PRG-24`, abierto, sin fecha). Por eso va como confirmación operativa antes del 13-Ago y no como defecto que espera una revisión: se pidió por el instrumento débil.
- **El HP y LP había quedado en Código 1 en el primer borrador y la verificación adversarial lo volteó.** El primer borrador lo aprobaba porque la petición de la edición cerró. La fila 5.2 del ITP exige un gráfico presión-tiempo como certificado de un Punto de Detención y el procedimiento no identifica el formulario que lo produce; además era una de las ocho peticiones del 06-Ago y quedó sin respuesta. Tratarlo distinto del Visual, que gana su Código 1 precisamente por identificar su formulario, no se sostenía.
- **El paquete de Bureau Veritas quedó repuesto el mismo 12-Ago**: siete archivos reemplazados dentro de `PAQUETE_INSPECCION_BV/`, los superados a `_superseded/`, y el aviso va en el correo conjunto `2026-08-12_BV-Inspections-3-and-4.docx`, que es cadena aparte de este transmittal.
- 🔴 **El ensayo de penetrantes del 7 de agosto se hizo antes de que su procedimiento existiera para ADASA.** El correo pide declarar qué registros hay y bajo qué criterio.
- **`BV-09` se cierra al enviar ese correo conjunto.** La revisión que se le entregó al inspector es la Rev 0 del 11-Ago, que es la que corrige el perfil de anclaje en los dos lugares del formulario.
- **El submittal 25007-0073** (Alarm & Interlock List Rev 0 y Control and Sequence Chart Rev 0, recibido el 11-Ago) queda fuera de este transmittal por decisión de alcance. Está registrado como entrega recibida y pendiente de revisión.
- **El enlace de descarga se cayó del cuerpo del correo en el N30 y en el N31.** Verificar sobre el correo enviado, no sobre el borrador, y si no salió, responder el propio hilo con el enlace.

## Checklist pre-envío

- [x] `DOWNLOAD_LINK` aplicado en `crear_correo_tm32.py` **y** en `crear_transmittal.py`, verificado idéntico en los dos `.docx` por sus relaciones de hipervínculo
- [ ] Subir a la carpeta del enlace **solo los tres `CC_ADASA` de los Código 3**; los tres de los documentos sin código quedan como traza interna
- [ ] Generar el PDF del transmittal abriendo el `.docx` en Word real, para que la tabla de contenidos se actualice
- [ ] To/CC correctos y envío en la cadena regular de transmittals
- [ ] **Al pegar en Outlook, confirmar que el párrafo del enlace viaja en el cuerpo**
- [x] 100% inglés; sin símbolo de sección; sin Van Doorn; sin la palabra "letter" (barrido ejecutado, 0 coincidencias)
- [x] Día de la semana verificado: 12-Ago-2026 es miércoles, 13 y 14 son jueves y viernes, 15 es sábado y 21-Ago es viernes
- [x] Metadatos Word limpios (autor Luis Rivera Gonzalez, company Aguas Antofagasta, en-US)
- [x] Master Register actualizado con `update_register_n32.py`: 113 items / 89 delivered, 53 Código 1 / 25 Código 2 / 8 Código 3 / 0 Código 4 más tres sin código
- [ ] Tras envío: BORRADOR → ENVIADO aquí y en el README, respaldo PDF o `.msg` en esta carpeta, entrada nueva arriba en la Bitácora y actualización del Estado Vigente
