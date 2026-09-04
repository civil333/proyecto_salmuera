# Correo — Informe de ensayo hidrostatico del 20-Ago-2026

**Estado:** **ENVIADO el jueves 20-Ago-2026 a las 11:00 de Chile**
**Fecha:** 20-Ago-2026 (jueves)
**Archivos:** `2026-08-20_Hydrotest-Report-20-Aug.docx` · respaldo del enviado en
`PRUEBAS DE PRESION.pdf` (8 paginas)
**Generador:** `crear_correo_hidrostatica_20ago.py`
**Cadena:** hilo del `Request to witness inspection 003/004`, es decir la cadena de las
jornadas de inspeccion. **Separada del Transmittal N35**, que fue por la cadena de los
submittals y con su propio correo, por decision del usuario.

## Destinatarios y asunto, segun el respaldo del enviado

El usuario ajusto la lista y el asunto al enviar. Se registra lo que salio, no lo que
proponia el borrador.

- **To:** Muhammad Fadhil Bin Abdul Wahid, Mohd Adnin Bin Zulkaflee, Stephane Gehant,
  Eduardo Yamauchi, Magdier Arias (BW Water); Ahmad Hazwan, Wan Mohd Adli W Yahya,
  Emylia Rosli (Bureau Veritas)
- **CC:** Victor Gutierrez (ADASA); Carlo Alberto Montecinos (Bureau Veritas)
- **Asunto:** RE: 25007 TALTAL - Request to witness inspection **003/004**
- **Sin adjuntos:** el informe de ensayo lo emitio la contraparte y ya obraba en su poder;
  el correo responde sobre el.
- Saludo: *"Dear Adnin, Magdier"*. El borrador abria *"Dear Adnin, Fadhil"*.

**Diferencias respecto del borrador:** el asunto quedo sobre la cadena **003/004** y no solo
la 004, lo que ademas reengancha la hidrostatica de baja presion y la del RO Vessel que el
Request 003 recorto (`PRG-13`); los cuatro de Bureau Veritas subieron a **To** en vez de
copia, que es coherente con pedirles constancia; y Lokman Hakim, Jorge Guevara y Ronald
Pellejero quedaron fuera.

**Verificado sobre el respaldo:** el cuerpo salio integro, con los cuatro codigos
(`P22-LI-09-009-003`, `P22-BA-09-000-010`, `P22-BA-09-000-004`, `P22-IT-09-000-001-0`), la
tabla de las once lineas y la viñeta de retencion.

## Resumen del cuerpo

**518 palabras, cinco parrafos, una tabla de once filas y cinco viñetas.** Version
ejecutiva: la primera pasada llego a 877 palabras y se recorto a 381; luego subio a 518 al
incorporar el enfasis que pidio el usuario sobre que **la regla ya esta aprobada**, con los
documentos nombrados por codigo. **El correo dice el hecho, la fuente y la peticion**; el
desarrollo completo vive en el analisis interno y en el Transmittal N35. La tabla hace el
trabajo que antes hacia la prosa: con las once lineas a la vista no hace falta explicar cual
va a que presion.

Los cinco parrafos, uno por idea, cada uno abriendo con la frase corta en negrita que carga
el juicio: acuse y Spool 2 conforme · Spool 1 no conforme · la clausula 5.5.12 como causa ·
**los documentos aprobados que fijan la regla** · la exposicion en las dos direcciones.

Parrafo por parrafo, en el orden en que aparecen:

1. **Acuse y Spool 2 conforme.** El inspector asistio y firmo los dos registros y el
   Inspection Request, primera jornada de la serie con constancia completa de asistencia,
   lo que cierra el punto levantado el 17-Ago. `DA-SSD-DN100-09-003` ensayada a 90 barG,
   retencion de treinta minutos, caida nula, **con la derivacion escrita**: diseño 60 barG
   en la Line List, por el factor 1,5, igual a 90. Sin esa derivacion, quien compare el
   certificado contra la fila 5.2 del ITP lee 90 contra 135 y supone una prueba de menos.
2. **Spool 1 no conforme.** Registrada como `DA-SSD-DN100-09-014` y ensayada a **7,5 barG**
   con dos manometros de rango 0 a 16 bar. Ninguna linea de super duplex del modulo se
   ensaya bajo 75 barG, y ese TAG no existe en la Line List: el correlativo 09-014 es
   `CP-SSD-DN100-09-014`, diseño 80 barG e hidrostatica 120 barG.
3. 🔴 **La clausula 5.5.12 como causa.** Dice en una sola frase que la cañeria de alta se
   ensaya a 135 bar y la de baja a 7,5, y que la presion se toma de la Line List, que
   prescribe seis valores. El factor 1,5 no esta escrito en ninguna parte del procedimiento.
4. **Los documentos aprobados que fijan la regla**, cada uno con su codigo. Ver la seccion
   siguiente: es el enfasis que pidio el usuario.
5. **La exposicion en las dos direcciones.** Ensayar de menos deja el ensayo sin calificar,
   que es lo que paso; aplicar 135 barG a toda linea de super duplex somete siete de las
   once a sobrepresion, hasta **2,7 veces el diseño** en las dos salidas de turbocharger,
   que estan en la descarga de `SIP-09-001` y `SIP-09-002`.
6. **Tabla de las once lineas** con diseño y prueba, **espejo exacto de la del Transmittal
   N35**, comparada por script antes de emitir.
7. **Cinco peticiones**, encabezadas por la retencion: **ningun ensayo mas del circuito de
   super duplex hasta que BW Water confirme por escrito la presion de cada linea** contra
   `P22-LI-09-009-003` Rev 0. Luego identificar el spool por su TAG y repetirlo si es super
   duplex; corregir el registro y el item 5 del checklist; que cada registro cite la presion
   de diseño junto a la de prueba; y el plan de las diez lineas que faltan, con el
   `Pressure Test Record Chart` emitido como formulario controlado.
8. **Respuesta pedida para el viernes 21-Ago**, para que una eventual repeticion alcance a
   correr dentro de la ventana abierta en Penang.

## El enfasis en lo aprobado, que es lo que hace irrebatible la exigencia

A pedido del usuario, el correo insiste en que **la tabla no es una imposicion nueva de
ADASA** y nombra cada fuente por codigo:

- **El propio procedimiento de BW Water remite a la Line List por codigo y revision.** La
  clausula 5.5.12 del `P22-BA-09-000-010` cita literal *"approved line list (Doc no:
  P22-LI-09-009-003 REV 0)"*. El correo lo dice asi: *"None of this is new, and your own
  pressure test procedure says where it lives."* No pueden alegar desconocimiento de la
  tabla que su propio documento nombra.
- **La Line List `P22-LI-09-009-003` Rev 0 la emitio BW Water y ADASA la aprobo en Codigo 1
  en el TM N29** del 21-Jul. Se dice con esas palabras, incluida la fecha.
- **El ITP `P22-BA-09-000-004` Rev 0, aprobado en Codigo 1 en el TM N26**, fija en su fila
  5.2 la presion de prueba en 1,5 veces la de diseño.
- **El PIE Base `P22-IT-09-000-001-0`**, fila 5.2, fija el mismo factor desde la licitacion.
- Cierre del bloque: *"The table below is those documents, not a new requirement."*
- El codigo `P22-LI-09-009-003 Rev 0` se repite ademas en el encabezado de la tabla y en la
  primera viñeta, que es la de la retencion de ensayos.

Cuatro codigos citados en el cuerpo, verificados por barrido sobre el `.docx` emitido:
`P22-BA-09-000-004`, `P22-BA-09-000-010`, `P22-IT-09-000-001-0` y `P22-LI-09-009-003`.

## Por que se pregunta y no se imputa

El hecho de la presion esta verificado y es duro. La identidad de la linea no: el TAG
puede estar mal transcrito. El correo declara lo que el registro dice, lo contrasta con
la Line List aprobada y pide identificar la linea antes de exigir la repeticion. Es la
regla anti-invencion del proyecto.

## Verificacion de fuentes

| Afirmacion del cuerpo | Verificado contra |
|---|---|
| Spool 1 a 7,5 barG, Spool 2 a 90 barG | Los dos `AQ-QAM-F018` Rev 4 del informe, render a 420 dpi de la fila de datos |
| Rangos 0-16 bar y 0-160 bar de los manometros | Certificados Trescal `PSPP-26605340` (FAC-MT-015), `-26605337` (FAC-MT-070), `-26605330` (FAC-MT-012) y `-26605335` (FAC-MT-013) |
| Las once lineas de super duplex y sus hidrostaticas de 75 a 135 barG | Line List `P22-LI-09-009-003` Rev 0, adjunta al procedimiento `P22-BA-09-000-010` |
| `CP-SSD-DN100-09-014`, diseño 80 barG e hidrostatica 120 barG | Misma Line List, fila de CIP FEED TO 1ST STAGE RO |
| 7,5 barG es la presion del sistema de baja | Fila 5.1 del ITP `P22-BA-09-000-004` Rev 0 |
| Fila 5.2 como Punto de Detencion con certificado grafico | Fila 5.2 del mismo ITP, columna de certificado: *"Pressure Test report (Graphic P vs T)"* |
| El TAG aparece tambien en la nota manuscrita | Render a 330 dpi de la pagina 1 del Inspection Request |
| Asistencia y firma del inspector | Timbre de Bureau Veritas y firma con fecha 20/08/2026 en las tres hojas |
| El viernes 21-Ago es viernes | `datetime`, verificado |
| **El factor es 1,5 sobre la presion de DISEÑO** | PIE Base `P22-IT-09-000-001-0`, fila 5.2: *"Presion Prueba = 1.5 x P.diseño = Y bar"*; ASME B31.3 para. 345.4.2 |
| **El 1,25 no existe en el contrato** | Barrido del arbol completo: unica aparicion, el paso de rosca M8x1,25 de un datasheet de vibracion |
| Diseño 60 barG de `DA-SSD-DN100-09-003`, y 60 x 1,5 = 90 | Line List Rev 0, fila de RO HP FEED PUMP DISCHARGE. Aritmetica verificada sobre las 34 filas: relacion 1,5 exacta |
| **Line List Rev 0 aprobada en Codigo 1** | Master Deliverable Register, item 38: Rev 0 / E67 / **TM N29** / 1-Approved |
| **ITP Rev 0 aprobado en Codigo 1** | Master Deliverable Register: Rev 0 / E57 / **TM N26** / 1-Approved |
| Los 135 barG son 1,5 x 90 barG, el diseño mas alto | ITP Rev 0, fila 5.2, texto literal |
| Solo cuatro lineas se ensayan a 135 barG | Recuento sobre la Line List Rev 0, verificado por script |
| El binomio de la clausula 5.5.12 | Texto literal del procedimiento Rev 1, pagina 7 |
| Boost de 19,6 bar del turbocharger | Datasheet `P22-ET-09-009-007` Rev D, *"Feed Boost Pressure 19.6 bar"* |
| Las dos tablas, correo y transmittal, son identicas | Comparadas fila a fila por script antes de emitir |

## Contexto Interno (No enviar)

- **El analisis completo** esta en `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/_ANALISIS_HYDROTEST_20AGO.md`,
  con la tabla de las once lineas de super duplex y la seccion de lo que no se levanta.
- **Item 5 del checklist.** El formulario pregunta si el rango del manometro esta entre
  1,5 y 4 veces la presion de ensayo requerida, y esta marcado que si. Con 7,5 barG
  requeridos y 16 bar de rango, la razon es 2,1 y la respuesta es correcta; con 120 barG
  requeridos, tendria que haberse marcado que no. Por eso el correo pide revisarlo "en la
  misma base" en vez de afirmar que esta mal: si la linea era de baja, no lo esta.
- **El grafico presion contra tiempo si se produce.** Las hojas de adjuntos traen el
  `PRESSURE TEST RECORD CHART` con escalones, horas y firmas. Eso **precisa** la
  observacion abierta sobre el procedimiento `P22-BA-09-000-010`: lo que falta no es la
  practica sino el control documental del formulario, que no tiene numero ni revision.
  El transmittal lo lleva como pendiente de la Seccion 3; aca va como peticion operativa.
- **Lo que se deja fuera a proposito:** el veredicto del Transmittal N35, el plazo de
  entrega vencido el 03-Ago y la multa de la Clausula 43.1 letra b, la hidrostatica de
  baja presion y la del RO Vessel que el Request 003 recorto (siguen en `PRG-13`), el
  formato manuscrito del grafico y la ausencia de `Report No.` en los formularios.
- **Excepcion de correo conjunto:** se nombra a BW Water aunque Bureau Veritas este entre
  los destinatarios, igual que en los correos del 14 y del 17 de agosto de esta cadena.

## anti-ia

Modo revisar, cuatro pasadas. Cobertura: familias universales mas Claude, por la regla de
autoria conocida (Opus 5). **VERDE.** Cero marcadores, cero em dash, cero simbolo de
seccion, oracion maxima de **45 palabras**, media 18,5 y sigma 11,13.

Corregido en la primera pasada: dos aperturas de parrafo con oracion-marco antes del dato
(CL-19) y una viñeta de 42 palabras (U-03 en alerta). En la segunda, tras agregar la alerta:
la apertura *"This is where we ask you to look closely"* activaba **U-02**, enmarcado
retorico, y se reescribio entrando por el hecho. La tercera fue el recorte a version
ejecutiva, que de paso resolvio **CL-19** por la via de fondo. En la cuarta, al sumar el
enfasis en lo aprobado, una oracion llego justo a 50 palabras y se partio en dos.

## Checklist pre-envio

- [x] Fecha de carpeta igual a la fecha del encabezado (20-Ago-2026)
- [x] Dia de la semana del vencimiento verificado (viernes 21-Ago)
- [x] Idioma `en-US` fijado; metadatos con autoria y compania
- [x] Cero simbolo de seccion
- [x] Cifras contrastadas contra Line List, ITP y certificados de calibracion
- [x] Confirmar que la cadena es el hilo del Request 004 y no la de transmittals

## Checklist post-envio

- [x] Cambiar BORRADOR por ENVIADO, con la hora de Chile tomada del respaldo
- [x] Archivar el respaldo del enviado en esta carpeta: `PRUEBAS DE PRESION.pdf`, 8 paginas, enviado 11:00
- [x] Registro de compromisos: `PRG-34` abierto (CRITICA, vence el viernes 21-Ago) por
      la confirmacion escrita de la presion de cada linea y la retencion de ensayos, y
      `PRG-35` por el Pressure Test Record Chart como formulario controlado
- [x] Bitacora del README
