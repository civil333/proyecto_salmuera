---
titulo: ENTREGA 81 — hallazgos verificados que NO se emiten
codigo: submittal 25007-0081
fecha: 2026-08-20
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 81 — lo verificado que queda fuera del transmittal

Todo lo de abajo esta comprobado contra el documento y su fuente. No se emite, y cada bloque dice por que. Sirve para no repetir el modo de falla y para tener trazabilidad si el defecto reaparece en el dossier o en terreno.

## Regla que gobierna el filtro

Los cinco documentos responden al Transmittal N32 y se juzgan solo por si cerraron lo que ese transmittal exigio. Los dos primeros ademas llegan por sobre la Rev 0 y ya estan emitidos para construccion, de modo que levantar hallazgos nuevos sobre ellos reabre una aprobacion propia de ADASA. Que el defecto sea cierto y este verificado no lo hace emitible.

Para los tres procedimientos de ensayos no destructivos el filtro es el mismo por decision del usuario, aunque esten en Rev B: el universo es el del N32. La excepcion seria una regresion introducida por la propia Rev B, y no hay ninguna.

---

## HP and LP Pressure Test Procedure `P22-BA-09-000-010` Rev 1

| Hallazgo verificado | Por que no se emite |
|---|---|
| La portada rotula `Date: 20/07/2026` mientras la fila de revision de la Rev 1 dice 19-08-2026. La fecha del cajetin quedo en la de la Rev D | Aseo documental que nunca se pidio. La revision y su fecha si estan correctas en la fila que gobierna |
| La clausula 5.8.1 sigue diciendo *"the Pressure Test Report"* sin nombrar el `AQ-QAM-F018` por numero y revision | El formulario entra ahora como pagina del propio procedimiento, de modo que queda identificado por pertenencia. Insistir en la redaccion sobre un documento ya emitido para construccion es aseo |
| El ITP nombra dos procedimientos distintos, `PROV-PROC-PH-LP-001` en la fila 5.1 y `PROV-PROC-PH-HP-001` en la 5.2, y el documento entregado se identifica como `PROV-PROC-HP-LP-001`, uno solo para los dos | Nunca se pidio. Es una inconsistencia entre el ITP aprobado y el procedimiento, y el ITP es el que habria que corregir. Se registra por si aparece al armar el dossier |
| Las tres regresiones de la Rev D siguen presentes: la clausula 5.6.5 ausente, y el factor `1.5 x design pressure` del paso 5.5.12 de la Rev C | Ya se dejaron pasar en el N32 por la misma razon: ADASA codifico 2 esa Rev D en el TM N29 sin detectarlas, y la revision que las introdujo esta aprobada |

**El formulario del ensayo no produce el registro grafico** que la fila 5.2 del ITP exige. Esto **si se emite**, pero en la Seccion 3 del transmittal y no como observacion que degrade el documento: el usuario dispuso Codigo 1 porque el formulario se incorporo, que era lo operativamente urgente. La jornada del 20-Ago demostro ademas que el grafico se produce en la practica, en un `PRESSURE TEST RECORD CHART` que no tiene numero de documento ni revision; lo que falta es su control documental, y eso se pide por la via operativa en el correo del 20-Ago de la cadena de inspecciones.

---

## Painting Procedure `P22-BA-09-000-011` Rev 1

| Hallazgo verificado | Por que no se emite |
|---|---|
| La fila `Specified DFT` del formulario sigue en `355 µm Min`, sin los espesores nominales por capa de 80, 200 y 75 micrones | El TM N32 lo replanteo reconociendo la respuesta de BW Water y lo declaro literal *"Not a condition of this transmittal"*. Exigirlo ahora contradice lo escrito |
| Las hojas de datos tecnicos de Jotun que se incorporaron declaran *"Recommended surface profile 30-85 µm"*, franja mas ancha que los 50 a 80 del cuerpo y del formulario | Es el anexo generico del fabricante, no el criterio del proyecto. El cuerpo y el formulario, que son lo que el inspector lee, estan en 50-80 en los dos lugares. Objetar la hoja de datos del fabricante no tiene requisito que lo sostenga |
| El documento crece de 11 a 38 paginas con contenido que no se pidio | No estorba y no altera ningun criterio |

**Accion propia de ADASA, no observacion a BW Water:** con esta Rev 1 el paquete del tercero inspector queda desactualizado en el procedimiento de pintura. Hay que reponerlo, igual que se hizo el 12-Ago bajo `BV-09`.

---

## Liquid Penetrant Examination Procedure `P22-BA-09-000-014` Rev B

| Hallazgo verificado | Por que no se emite como observacion separada |
|---|---|
| La numeracion duplica la clausula 9.2, que aparece como `Penetrant Removal Application` y como `Developer Application` | Nunca se pidio y no bloquea. Se registra |
| El limite de cloro mas fluor de 0,1% se enuncia para *"austenitic stainless steel or titanium"*, sin nombrar el super duplex UNS S32750 | Nunca se pidio. Tecnicamente el limite es igual o mas exigente para el duplex, de modo que el criterio escrito no es permisivo |
| Los umbrales del criterio B31.3 que se agrego coinciden digito a digito con los del Apendice 6 que se mantiene y con los del Apendice 8 del formulario | **No es un hallazgo sino un matiz de equidad**, y va escrito en el Status de la subseccion: el riesgo de que el examinador acepte una soldadura que otro criterio rechazaria es nulo. Lo que sostiene el Codigo 3 es que el registro que entra al dossier citara el codigo de recipientes a presion y no el de cañerias |

---

## Radiography Examination Procedure `P22-BA-09-000-015` Rev B

| Hallazgo verificado | Por que no se emite |
|---|---|
| La pagina de la Tabla 341.3.2-1 entra como imagen sin numero de figura ni referencia en el indice del anexo | Aseo. Lo que se pidio era el criterio, y el criterio esta |
| El alcance del anexo sigue declarando *"up to 3-inch thickness"* sin la franja real del circuito | Es la OBS-03 del N32, aseo declarado que no retiene la reemision. Se repite en el bloque de accion como parte del mismo lote, no como observacion nueva |

---

## Ultrasonic Thickness Procedure `P22-BA-09-000-016` Rev B

| Hallazgo verificado | Por que no se emite |
|---|---|
| La clausula 4.1 escribe `UNS S32750 or S32250`, y `S32250` no existe como designacion UNS. Lo mas probable es que se quisiera escribir `S32205`, que es el duplex 2205 | Error de tipeo dentro de un punto que **si** se emite. Va como una clausula del bloque de accion, no como observacion propia, para no inflar el conteo |
| La clausula 9.0 escribe `UNS2750` sin la S y sin el 3, y la referencia como `SA79M` | Mismo criterio: el punto emitido es que el criterio de aceptacion no es el de espesor minimo; la designacion mal escrita es una clausula de ese mismo punto |
| El acoplante se declara de tres maneras: grasa, aceite o pasta base agua en la clausula 5.0, `Starch` en la hoja de tecnica y `Wallpaper Paste` en el formulario | Se pidio en la OBS-04 del N32 como aseo del formulario y se cerro a medias. Sigue en el lote de aseo, sin retener la reemision |
| El texto de calibracion es el manual del equipo Olympus 38DL PLUS | Estaba en la Rev A y no se pidio quitarlo. La ET no exige un formato de procedimiento |

**Lo que si se reconoce en el Status:** de los tres procedimientos de ensayos no destructivos, este es el que mas trabajo. Nueve cambios de contenido contra los dos del de radiografia y el uno del de penetrantes, y **cerro la hoja de tecnica**, que era una de sus dos observaciones bloqueantes. Escribirlo asi no debilita el Codigo 3: lo hace mas dificil de discutir.

---

## Los tres procedimientos, control de revisiones

El diferencial medido entre la Rev A y la Rev B, linea a linea:

| Documento | Cambios de contenido | Perdidas |
|---|---|---|
| `-014` Liquid Penetrant | 1 (el bloque `b. ASME B31.3` de la clausula 13.0) | ninguna |
| `-015` Radiography | 2 (el parentesis de la letra d y la pagina de la tabla) | ninguna |
| `-016` Ultrasonic | 9 | ninguna |

Ningun parrafo desaparecio en las tres re-emisiones. Se verifico a proposito, porque la leccion de la ENTREGA 71 fue que una re-emision puede perder contenido por el camino.

---

## Lo que esta revision puso sobre la mesa y no estaba

**Los tres procedimientos de ensayos no destructivos se re-emiten sin hoja de comentarios consolidada.** Venian de Codigo 3 con observaciones bloqueantes y la Rev B no declara como respondio a ninguna. Esto **si se emite**, como NOTE de calidad documental en la subseccion del primero de los tres, porque obliga a ADASA a verificar por diferencia de texto lo que la hoja deberia declarar. Los dos procedimientos que llegan por sobre la Rev 0 si la traen.

**La hoja del `-010` transcribe el comentario de ADASA reducido a una frase.** Lo emitido fue una OBS-01 de seis lineas que incluia el registro grafico; la hoja lo resume a *"NOTE-01: Identify the pressure test record"* y responde a esa version resumida. Se registra y no se emite: el documento cierra el punto por Codigo 1 y reclamar la transcripcion seria aseo sobre un documento aprobado.
