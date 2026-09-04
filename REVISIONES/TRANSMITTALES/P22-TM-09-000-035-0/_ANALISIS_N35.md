---
titulo: Analisis interno — Transmittal N35 (P22-TM-09-000-035-0)
codigo: P22-TM-09-000-035-0
fecha: 2026-08-20
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Analisis interno — Transmittal N35

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

**Entrega cubierta:** ENTREGA 81, submittal `25007-0081`, cinco documentos.
**Veredicto global propuesto:** **3 — To be revised**. Recuento: **2 Codigo 1, 3 Codigo 3**.
**El codigo lo fijan los tres procedimientos de ensayos no destructivos**, que vuelven por segunda vez sin fijar el criterio de aceptacion que la ET Seccion 8 y el NDE Plan Rev C hacen aplicable.

El cierre punto por punto, con el texto literal de cada pedido y su verificacion, vive en `ENTREGAS_BWWATER/ENTREGA 81/_LEDGER_COMENTARIOS.md`. Lo verificado que no se emite, en `_HALLAZGOS_DETERMINISTAS.md` de la misma carpeta. Este archivo resuelve la disposicion.

---

## 1. Recepcion y plazos

| Submittal | Emitido | Devolucion pedida por BW | Recibido por ADASA | Vencimiento real, Clausula 37.2 |
|---|---|---|---|---|
| `25007-0081` | 20-Ago-26 | **domingo 23-Ago-26** | jueves 20-Ago-26 | **lunes 31-Ago-26** |

**Hecho contractual.** La Clausula 37.2 de la BAE concede a ADASA siete dias habiles de revision documental desde la recepcion. Tres dias corridos, con vencimiento en domingo, no desplazan ese plazo. Es la tercera submittal consecutiva cuya fecha de devolucion pedida cae por debajo del plazo contractual, despues del `25007-0075` (sabado 15) y del `25007-0077` (recibido un dia despues de su propia fecha de devolucion). Se menciona en el Resumen Ejecutivo, sin abrir un eje contractual propio.

---

## 2. Higiene de carpeta

- Los cinco archivos tienen texto extraible; ninguno escaneado. Extraidos a `ENTREGAS_BWWATER/ENTREGA 81/md/`.
- Los cinco hashes de contenido son nuevos: sin duplicado de payload contra la ENTREGA 71 ni la 75.
- El `-014` trae una pagina vacia y paginas rotadas a 90 grados; verificadas por render.
- La Tabla 341.3.2-1 del `-015` entra como imagen y no aparece en la extraccion de texto: **verificada por render a 200 dpi**. Sin ese render se habria afirmado una ausencia falsa.

---

## 3. `P22-BA-09-000-010` Rev 1 — HP and LP Pressure Test Procedure

**Origen:** OBS-01 del TM N32, subseccion 2.3. La Rev 0 se devolvio **sin codigo de respuesta**.

**Que cerro.** El formulario **`AQ-QAM-F018` "Pressure and Leak Test Report" Rev 4** entra como pagina 11 del procedimiento, en blanco y con membrete. Es el que estaba en la Rev C y desaparecio en la Rev D. El punto operativamente urgente — que el inspector tuviera contra que registrar el ensayo — esta resuelto, y la jornada del 20-Ago lo confirma: los dos ensayos se levantaron en ese formulario.

**Que no.** El formulario registra valores puntuales y no produce el registro grafico presion contra tiempo que las filas 5.1 y 5.2 del ITP `P22-BA-09-000-004` Rev 0 exigen como certificado. La clausula 5.8.1 tampoco lo nombra por numero ni revision.

### Disposicion

**Codigo 1 — Approved.** Decision del usuario. El documento llega **por sobre la Rev 0**, ya emitido para construccion, y ahi el Codigo 2 no tiene mecanismo: es 1 si lo que era condicion quedo incorporado, o 3 si no. El formulario esta incorporado. Lo que falta vive en un formulario distinto — el `PRESSURE TEST RECORD CHART` que la jornada del 20-Ago demostro que existe y que no tiene numero de documento ni revision — y por lo tanto **no es un defecto intrinseco de este documento**: se traslada a la Seccion 3, consistente con el criterio de que un pendiente que vive en otro entregable no degrada al revisado.

**Sin `CC_ADASA`**, por ser Codigo 1.

**El pendiente se persigue ademas por la via operativa**, en el correo del 20-Ago de la cadena de inspecciones, porque el ensayo esta en ejecucion esta semana y no puede esperar a la proxima emision del procedimiento.

---

## 4. `P22-BA-09-000-011` Rev 1 — Painting Procedure

**Origen:** OBS-01 del TM N32, subseccion 2.4. La Rev 0 se devolvio **sin codigo de respuesta**.

**Que cerro.** La fila `Colour` del formulario de inspeccion lee **`RAL 5012 Luminous Blue`** en la tercera capa, que era la unica condicion vinculante. El perfil de anclaje sigue unificado en 50 a 80 micrones en las dos filas y el producto de cada capa esta escrito.

**Lo que sigue abierto y no se exige.** Los espesores nominales por capa no estan impresos. El propio N32 lo declaro *"Not a condition of this transmittal"* al replantearlo.

### Disposicion

**Codigo 1 — Approved.** Cierra lo que era condicion, sobre un documento ya emitido para construccion. **Sin `CC_ADASA`.**

**Accion propia de ADASA**, no observacion: reponer el paquete del tercero inspector con esta Rev 1, como se hizo el 12-Ago bajo `BV-09`.

---

## 5. `P22-BA-09-000-014` Rev B — Liquid Penetrant Examination Procedure

**Origen:** OBS-01 a OBS-04 y NOTE-01 del TM N32, subseccion 2.5. Rev A en Codigo 3. Compromiso `PRG-25`.

| Punto | Estado |
|---|---|
| OBS-01, criterio en la clausula 13.0 | **Cierre parcial.** Se agrego `b. ASME B31.3 - Process Piping` **manteniendo** `a. ASME Section VIII Div. 1, Appendix 6`. Dos criterios en paralelo, ninguno declarado como el que gobierna, y el parrafo 341.3.2 no se cita por su numero |
| OBS-02, criterio en el formulario | **No cerrado.** Sigue `Acceptance Criteria: ASME VIII DIV.1 Appendix 8` |
| OBS-03, formulario en blanco | **No cerrado** |
| OBS-04, indice de revision unico | **No cerrado** |
| NOTE-01, proposito y Articulo 6 | **No cerrado** |

**El diferencial completo entre Rev A y Rev B son once lineas.** Ninguna de las cuatro observaciones de aseo se atendio, pese a haberse pedido para la misma emision.

### Disposicion

**Codigo 3 — To be revised.** La observacion bloqueante del formulario no se toco y la de la clausula cerro a medias. Segunda vez que se pide fijar el criterio.

**Matiz que va escrito en el Status**, porque es cierto y porque hace mas dificil de discutir el codigo: los umbrales del criterio B31.3 agregado coinciden digito a digito con los del Apendice 6 y con los del Apendice 8. El riesgo de un resultado distinto es nulo. Lo que sostiene el Codigo 3 es que el registro que entra al dossier citara el codigo de recipientes a presion y no el de cañerias.

**Lleva `CC_ADASA`.** Ademas, la NOTE de la hoja de comentarios ausente se levanta aqui, por ser el primero de los tres.

---

## 6. `P22-BA-09-000-015` Rev B — Radiography Examination Procedure

**Origen:** OBS-01 a OBS-04 y NOTE-01 del TM N32, subseccion 2.6. Rev A en Codigo 3. Compromiso `PRG-25`.

| Punto | Estado |
|---|---|
| OBS-01, criterio en la clausula 23.0 | **Cierre parcial.** Se incorporo la **Tabla 341.3.2-1 de ASME B31.3-2024 completa** como pagina nueva del anexo, verificada por render. La clausula 23.0 conserva la lista de cinco codigos y solo añade el parentesis que remite a esa pagina |
| OBS-02, borrosidad geometrica | **No cerrado.** La clausula 12.1 sigue literal en 1,8 mm para items con sello `PP` |
| OBS-03, alcance sin material ni espesor | **No cerrado** |
| OBS-04, numeracion rota | **No cerrado** |
| NOTE-01, proposito y Articulo 2 | **No cerrado** |

**El diferencial completo son dos cambios.**

### Disposicion

**Codigo 3 — To be revised.** La OBS-02 es la que decide: **no se toco una sola palabra**, y es el punto que admite una borrosidad tres veces y media superior a la que el codigo permite para la pared que se radiografia en este modulo. La incorporacion de la tabla se reconoce en el Status.

**Lleva `CC_ADASA`.**

---

## 7. `P22-BA-09-000-016` Rev B — Ultrasonic Thickness Procedure

**Origen:** OBS-01 a OBS-05 y NOTE-01 del TM N32, subseccion 2.7. Rev A en Codigo 3. Compromiso `PRG-25`.

| Punto | Estado |
|---|---|
| OBS-01, criterio de aceptacion en la clausula 9.0 | **No cerrado.** Paso de *"at the discretion by the client"* a *"Acceptance as per ASME Section II (SA790/790M) according to Grade UNS2750"*, que es un criterio de **material**, no de espesor. El NDE Plan Rev C fija el espesor medido igual o mayor al espesor minimo requerido por el codigo de diseño y el calculo |
| OBS-02, hoja de tecnica para UNS S32750 | **Cerrado con residuo.** El alcance, el Apendice 1 y el bloque de calibracion declaran ahora el material. Falta el valor de la velocidad de propagacion, y `S32250` no existe como designacion |
| OBS-03, plano de puntos de medicion | **Abierto**, con fecha propia. No era condicion de la Rev B |
| OBS-04, formulario en blanco | **Cierre parcial.** Se borraron el numero de informe y de trabajo; sigue `Wallpaper Paste` |
| OBS-05, edicion y codigos | **Cierre parcial.** La edicion se unifico en 2025; siguen `ASME E 797` y los codigos de inspeccion en servicio |
| NOTE-01, proposito y Articulo 5 | **No cerrado** |

**Nueve cambios de contenido.** Es el que mas trabajo de los tres.

### Disposicion

**Codigo 3 — To be revised.** Cerro una de sus dos bloqueantes y el Status lo dice. La otra, que es la critica, cambio a un criterio que no resuelve lo que una medicion base de fabricacion tiene que resolver.

**Lleva `CC_ADASA`.**

---

## 8. Resumen de disposicion

| Documento | Rev | Codigo | Que falta, en una linea | CC_ADASA |
|---|---|---|---|---|
| HP and LP Pressure Test `-010` | 1 | **1** | Nada en este documento. El formulario del registro grafico va a la Seccion 3 | No |
| Painting `-011` | 1 | **1** | Nada | No |
| Liquid Penetrant `-014` | B | **3** | Un solo criterio de aceptacion, en la clausula y en el formulario | Si |
| Radiography `-015` | B | **3** | El limite de borrosidad de T-274 para la pared de este modulo | Si |
| Ultrasonic Thickness `-016` | B | **3** | El criterio de espesor minimo requerido en la clausula 9.0 | Si |

**Veredicto global: 3 — To be revised.** Recuento: 2 Codigo 1, 3 Codigo 3.

**Tres `CC_ADASA`**, uno por cada Codigo 3. Los dos Codigo 1 no llevan anotado, per la regla del proyecto.

---

## 9. Que se retira y no se emite

Detalle completo en `ENTREGAS_BWWATER/ENTREGA 81/_HALLAZGOS_DETERMINISTAS.md`. En resumen: la fecha de portada del `-010`, la doble identificacion del procedimiento entre el ITP y el documento, el perfil de 30 a 85 micrones de la hoja de datos de Jotun, la clausula 9.2 duplicada del `-014`, y el manual del equipo Olympus dentro del `-016`. Ninguno tiene requisito que lo sostenga dentro del universo del N32.

---

## 10. Registro del criterio aplicado

**El usuario fijo el alcance antes de la revision:** los documentos que llegan por sobre la Rev 0 ya estan emitidos para construccion, de modo que la revision verifica si los comentarios previos cerraron y no introduce observaciones nuevas. El mismo alcance se extendio a los tres procedimientos en Rev B.

**El usuario decidio ademas el Codigo 1 del `-010`**, contra una propuesta inicial de Codigo 3. El razonamiento que la sostiene y que quedo escrito: el formulario se incorporo, que era la parte urgente; lo que falta vive en otro formulario; y un pendiente que no es intrinseco al documento revisado se sigue en la Seccion 3 sin degradarlo. Es coherente con las dos correcciones de over-reach sobre Rev 0 que ya se registraron en el N34.
