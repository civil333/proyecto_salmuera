---
titulo: ENTREGA 76 — hallazgos verificados que NO se emiten
codigo: submittal 25007-0076
fecha: 2026-08-13
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 76 — lo verificado que queda fuera del transmittal

Todo lo de abajo está comprobado contra el documento y su fuente. No se emite, y cada bloque dice por qué. Sirve para no repetir el modo de falla y para tener trazabilidad si el defecto reaparece.

## Regla que gobierna el filtro

Los dos planos venían de un Código 2 que no exigía nueva revisión. Se juzgan por si incorporaron lo que era condición de esa aprobación, y por el contenido nuevo que la Rev B agrega, que nunca estuvo aprobado. Levantar defectos que ya estaban en la Rev A y que ADASA no observó entonces reabre una aprobación propia, salvo que el defecto sea el objeto mismo del comentario que se está cerrando.

---

## Control documental de los dos planos

Se registra completo y no se emite: son cosas que no inducen a error en obra y que la emisión de Rev 0 corrige por sí sola.

| Punto | Evidencia |
|---|---|
| La portada del plano civil declara *"Page: 1of 1"* y el documento trae dos láminas; la del plano de la bomba declara *"Page: 1of 2"* y trae una. Las dos declaraciones están invertidas | Página 1 de cada PDF |
| La Rev B tiene tres fechas distintas | Cajetín del plano civil AGO.02.26 y portada 10-08-2026; cajetín del plano de la bomba AGO.08.26 y portada 11-08-2026; Submittal Form 13-Ago-26 |
| La hoja consolidada de comentarios del plano civil está fechada 24-07-2026, antes de la revisión que comenta, y su columna `Status` va vacía. La del plano de la bomba dice `Current` | Última página de cada PDF |
| El cajetín del plano de la bomba rotula el dibujo `DETAIL - CIP FLUSHING SKID PUMP`, mientras el documento se llama `GA of CIP Flushing Skid Pump` en la portada, en el Submittal Form y en el Master Register | Cajetín de la lámina |
| El cajetín del plano civil describe la Rev A como `ISSUED FOR INTERNAL APPROVAL`, cuando esa revisión se sometió a ADASA en el submittal 25007-0034 y se codificó 2 en el TM N16 | Bloque de revisiones |
| La numeración de notas del plano de la bomba se rompe: el bloque de anclaje va 4.1 a 4.4 y sigue con `5. SPACING`, que pertenece al bloque 4 como 4.5. Todas las notas siguientes quedan corridas | Bloque de notas |
| El Submittal Form pide respuesta el domingo 16-Ago-2026, día no hábil | Campo `Req. Return Date` |

El punto de la fecha de retorno sí se menciona en el correo de remisión cuando se emita el transmittal, no como observación de documento sino para dejar constancia del plazo que rige.

## Conversiones al sistema imperial redondeadas al entero

El plano de la bomba acota `Ø14 [Ø1"]`, `Ø19 [Ø1"]` y `Ø38 [Ø2"]`. Los tres valores métricos son 0,55, 0,75 y 1,50 pulgadas, y los tres se imprimen redondeados al entero. Lo mismo ocurre en varias cotas menores del plano civil.

**No se emite.** El valor métrico es el que gobierna, per la Nota 1 de los dos planos, y el TM N5 OBS-02 sobre unidades imperiales quedó cerrado con esa misma regla. Objetar la conversión de cortesía sin un requisito que la respalde es refutable.

## Fuerza sísmica del plano hermano

El plano `P22-DWG-09-005-011` Rev B declara una masa de 100 kg y una carga muerta Fy de 1,4632 kN, que corresponde a 149 kg. Los dos números no cierran entre sí.

**No se emite.** Ese plano está aprobado en Código 2 desde el TM N26 y no forma parte de esta entrega. Se registra porque el mismo criterio de cálculo produce las cifras del plano que sí se está revisando, y porque si alguna vez se pide el informe de cálculo endosado, ahí hay que mirarlo.

## Peso del estanque CIP arrastrado desde la Rev A

Los 10.470 kg de operación de TK-09-001 estaban idénticos en la Rev A que ADASA codificó 2 en el TM N16 sin observarlos.

**Sí se emite**, pese a lo anterior, porque el objeto del comentario que se está cerrando es precisamente la declaración de pesos de la tabla, y porque el número dimensiona una fundación que ADASA paga. Se redacta como reconciliación pedida contra la Equipment List aprobada, no como incumplimiento nuevo.

Distinto es el estanque de dispersante TK-09-002: pasó de 490 a 517,5 kg, de modo que la Rev B lo empeoró y no hay que justificar el encuadre.

## Panel de control del calentador sin plinto

El ítem 15 de la tabla de cargas, `HEATER CONTROL PANEL`, 50 kg, se dibuja apoyado en el suelo de la zona CIP entre el estanque de dispersante y el estanque CIP, y no tiene plinto en el listado ni detalle de anclaje.

**No se emite.** Son 50 kg sobre una fundación de equipos que ya existe y que lo admite sin pedestal. El calentador REL-09-001, que a primera vista parecía en la misma situación, va montado sobre la boquilla del estanque CIP y no necesita apoyo propio: se verificó en la planta de la lámina 1.

## Anclaje del estanque de dispersante

El detalle 6 fija tres pernos M8 en circunferencia Ø740 para un estanque de 517,5 kg en operación, en Zona Sísmica 3.

**No se emite como observación autónoma.** El pedido que sí se hace, declarar el empotramiento requerido y confirmar que el espesor del plinto lo admite, ya cubre este detalle, y separarlo multiplicaría el conteo sin agregar exigencia. Si el informe de cálculo endosado llega y no cubre este anclaje, entra por esa vía.

## Lo que no se observa por falta de requisito

- **El formato del plano.** El cajetín, el orden de las vistas y la ausencia de una tabla de referencias cruzadas no están exigidos por la Especificación Técnica.
- **La ausencia de tolerancias de nivelación y de planitud** en los plintos. Sería útil, pero no hay requisito escrito que la sostenga, y el criterio de nivelación de una fundación es alcance de ADASA, no del proveedor del módulo.
- **La ausencia de referencia cruzada** desde el plano civil a los planos de fundaciones de L&A. El proveedor no tiene por qué conocer la codificación de la ingeniería civil de ADASA. Lo que sí se le pide es declarar el arreglo de apoyo requerido, que es información suya.
