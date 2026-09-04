# Project Schedule Rev B — retirado del Transmittal N36

> **TRAZA INTERNA. Nada de esta carpeta se emite.**

## Que hay aqui

| Archivo | Que es |
|---|---|
| `P22-BA-09-000-001_B_Project_Schedule_CC_ADASA.pdf` | El PDF anotado que se genero y **no se emite** |
| `agregar_comentarios_project_schedule_revB.py` | El script que lo produjo |
| `sched_p11.png`, `sched_p14.png` | Renders de verificacion de las dos anotaciones |

## Por que se retiro

**Decision del usuario, 26-Ago-2026:** el seguimiento del cronograma se lleva por la reunion semanal de coordinacion y no por el transmittal. Las dos observaciones que este PDF llevaba anotadas salen del Transmittal N36 junto con el documento, que **no recibe codigo de respuesta** en ese transmittal.

El transmittal lo declara en una linea de su Resumen Ejecutivo, para que BW Water no quede esperando un codigo que no va a llegar por esa via.

**Esta carpeta salio del paquete del transmittal** por instruccion del usuario y vive junto al documento que comenta. El PDF fuente no se duplica aqui: es `25007-0084/P22-BA-09-000-001_B Project Schedule.pdf`, en esta misma entrega.

## La evidencia verificada, que se conserva por si el punto reaparece

Las dos observaciones del TM N20, subseccion 2.16, **siguen sin cerrar** en el Rev B. Verificado sobre las catorce paginas del documento:

- **Base de certificacion de los recipientes a presion.** Cero ocurrencias de `ASME`, `stamp`, `certif` y `waiver`. El bloque de recipientes encadena orden de compra, aprobacion de planos, fabricacion y embarque, sin actividad de certificacion ni liberacion entre ellas. La fecha ex-works corresponde a la ruta sin estampa aceptada bajo el waiver del 02-Jun-2026, y el cronograma no lo declara.
- **Ensayos de presion.** Cero ocurrencias de `hydro`, `hydrostatic`, `pressure test` y `leak`. Las dos unicas tareas con la palabra `Test` son el FAT del sistema, que no tiene subtareas, y el ensayo de desempeno en obra. `Protec` y `Arisawa` no aparecen.
- **Agravante temporal:** los recipientes ya estan fabricados y recibidos en Penang, ambas tareas al cien por ciento.
- **Lo que si cumple:** la tercera clausula de la accion del TM N20. La columna de linea base conserva integros los cuatro anclajes adoptados el 09-Jun-2026 y no reabre la adopcion.

El cierre punto por punto y la tabla de hitos con sus desplazamientos siguen en `ENTREGAS_BWWATER/ENTREGA 84/_LEDGER_COMENTARIOS.md`, que no se toca.

## Regla que se aplico

Al retirar un veredicto, el `CC_ADASA` se retira con el y la evidencia verificada se conserva por si el defecto reaparece: no se borra. El destino habitual es una subcarpeta del propio transmittal; aqui se movio a la carpeta de la entrega porque el documento salio del eje documental por completo.
