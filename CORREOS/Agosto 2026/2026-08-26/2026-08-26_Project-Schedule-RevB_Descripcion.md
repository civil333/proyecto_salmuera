# Correo contractual — Project Schedule Rev B

**Estado:** **SUPERADO — no se envía.** El 31-Ago-2026 BW Water corrió el ex-works del 21 al 28 de
septiembre, de modo que las tres cifras de este correo quedaron obsoletas (los 37 días del ex-works
pasaron a 44 y los 44 de la entrega en sitio a 51) y su plazo del miércoles 2 de septiembre nunca
llegó a correr. **Lo reemplaza la Nota Técnica `P22-NT-09-000-003-0`**, emitida el 31-Ago desde
`CORREOS/Agosto 2026/2026-08-31/`, que absorbe sus tres preguntas: el alcance del FAT contra su
ventana declarada entra como punto 3.B, y el desglose del tramo de embarque más la ausencia de
certificación de recipientes y de ensayo de presión entran como contenido exigido del plan de
recuperación en el punto 4.A. La reserva contractual de este borrador sigue siendo válida y se
reemite ahí, con la misma regla de no cursar cifra.
**Fecha:** 26-Ago-2026 (miercoles)
**Archivos:** `2026-08-26_Project-Schedule-RevB.docx`
**Generador:** `crear_correo_programa_revB.py`
**Cadena:** hilo de programa, **separada** de la de transmittals. El mismo dia sale por la otra cadena el correo de cobertura del Transmittal N36 (`2026-08-26_Transmittal-N36.docx`, misma carpeta). El transmittal dispone el codigo de respuesta del documento; este correo plantea el fondo.

## Destinatarios

- **To:** Eduardo Yamauchi (BW Water)
- **CC:** Stephane Gehant, Andrew Sia, Fitri Indriyani (BW Water); Victor Gutierrez, Jorge Guevara, Ronald Pellejero (ADASA)
- **Asunto:** TALTAL - Project Schedule Rev B - contractual position on the delivery period
- **Sin adjuntos.** El documento comentado ya esta en poder de las dos partes y su PDF anotado viaja por el enlace del transmittal.

## Resumen del cuerpo

**345 palabras, cinco parrafos y tres vinetas.** Tono contractual, no acusatorio.

1. **Acuse de recibo** del Rev B y remision del codigo de respuesta al Transmittal N36, declarando que este correo trata la sustancia del programa.
2. **Se reconoce lo que el Rev B si hace bien:** no reabre la linea base de recuperacion adoptada el 09-Jun-2026.
3. **Los tres desplazamientos**, en vinetas: ex-works Penang del 15-Ago al 21-Sep (+37 dias), entrega en sitio del 30-Sep al 13-Nov (+44) y fin de programa del 19-Nov-2026 al 02-Ene-2027 (+44).
4. **La reserva de posicion contractual:** el Plazo de Entrega vencio el 03-Ago-2026, con la cita doble correcta (la Clausula 27 fija el plazo, la 43.1 letra b la multa diaria y la 43.4 el tope). **No se cursa cifra**: se pide que BW Water confirme por escrito la fecha de la Notificacion de Adjudicacion, y se declara que ADASA la verificara contra su propio registro antes de cuantificar.
5. **Tres preguntas con fecha de respuesta:** como cabe el alcance del FAT en una ventana declarada que bajo de quince a once dias; el desglose del tramo de embarque, que paso de 46 a 53 dias corridos; y la ausencia de toda actividad de certificacion de recipientes y de ensayo de presion. Deadline: **miercoles 02-Sep-2026**.

## La regla dura que gobierna este correo

**No se cursa cifra de multa.** La Seccion 9.3 del CLAUDE.md lo fija: antes de cursar multa hay que leer la fecha de la **Notificacion de Adjudicacion en el documento original de ADASA**, y calcularla sobre el rotulo del cronograma del proveedor deja el reclamo atacable por solida que sea la coincidencia. Esa lectura **esta pendiente**, de modo que el correo reserva la posicion, cita las tres clausulas y pide el dato. Cuantificar viene despues.

**La cita es triple y va completa:** Clausula 27 para el plazo, 43.1 letra b para la multa diaria, 43.4 para el tope. Citar solo la 27 como fuente de la multa es refutable.

## Verificacion de fuentes

| Afirmacion del cuerpo | Verificado contra |
|---|---|
| Ex-works Penang, linea base 15-Ago y proyectado 21-Sep | Tarea 416 del Rev B, columnas de linea base y proyeccion |
| Entrega en sitio, 30-Sep contra 13-Nov | Tarea 417 |
| Fin de programa, 19-Nov-2026 contra 02-Ene-2027 | Fila 0 del programa y tarea 424 |
| FAT proyectado del 7 al 18-Sep, duracion declarada de 15 a 11 dias | Tarea 414. **La duracion declarada y el calendario difieren en un dia**: el 7 al 18 de septiembre son diez dias habiles. El correo cita la duracion **declarada**, que es el dato del documento |
| Tramo de embarque de 46 a 53 dias | Diferencia entre las tareas 416 y 417 en cada columna |
| La linea base no se reabrio | Los cuatro anclajes de la columna de linea base intactos: 23-Jun, 2-Ago, 15-Ago y 19-Nov |
| Cero actividad de certificacion y cero ensayo de presion | Cero ocurrencias de `ASME`, `stamp`, `certif`, `waiver`, `hydro`, `pressure test` y `leak` en las catorce paginas |
| El 02-Sep-2026 es miercoles | `datetime`, verificado |
| El Plazo de Entrega vencio el 03-Ago-2026 | Registro de compromisos del proyecto |

## Contexto Interno (No enviar)

- **La fecha de la Notificacion de Adjudicacion sigue sin verificar.** Es el unico dato que falta para cuantificar, y hay que leerlo en el documento original de ADASA, no en el rotulo del cronograma del proveedor.
- **Lo que no se dijo y podria decirse en el siguiente ciclo:** que los recipientes ya estan fabricados y recibidos en Penang al cien por ciento sin que el programa muestre su hidrostatica de fabrica, lo que alimenta directamente el dossier de fabricacion pendiente. El transmittal ya lo plantea como observacion documental; el correo lo deja como la tercera pregunta, sin desarrollarlo.
- **El typo `ADISA` de la tarea 419** y la ausencia de fecha de corte y de version de linea base quedaron fuera de los dos vehiculos, por regla de alcance. Estan registrados en el ledger de la entrega.

## Checklist pre-envio

- [x] Fecha de carpeta igual a la fecha del encabezado (26-Ago-2026)
- [x] Dia de la semana del deadline verificado (miercoles 02-Sep-2026)
- [x] Idioma `en-US` fijado; metadatos con autoria
- [x] Cero simbolo de seccion, cero fuga interna
- [x] **Ninguna cifra de multa cursada**
- [x] Cita triple completa: Clausula 27, 43.1 letra b y 43.4
- [x] Confirmar que la cadena es la de programa y no la de transmittals

## Checklist post-envio

- [ ] Cambiar BORRADOR por ENVIADO, con la hora de Chile tomada del respaldo
- [ ] Archivar el respaldo del enviado en esta carpeta
- [ ] Registro de compromisos: abrir el compromiso de respuesta al 02-Sep
- [ ] Bitacora del README
