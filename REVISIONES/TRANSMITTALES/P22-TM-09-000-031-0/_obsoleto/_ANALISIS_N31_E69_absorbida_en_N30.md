---
titulo: Analisis interno TM N31 — ENTREGA 69 (submittal 25007-0069)
codigo: P22-TM-09-000-031-0
estado: TERRENO PREPARADO — transmittal sin generar
second_brain: skip
---

# TM N31 — terreno preparado

> Documento interno de trabajo. **NO ENVIAR.** Reúne lo necesario para generar el transmittal cuando se decida emitirlo. El análisis completo, con la trazabilidad contra cada fuente, vive en `ENTREGAS_BWWATER/ENTREGA 69/_ANALISIS_E69.md`.

## Alcance

| Campo | Valor |
|---|---|
| Submittal | `25007-0069` |
| Entrega | E69, recibida el **lunes 27-Jul-2026 08:17** |
| Documentos | **1** |
| Fecha de retorno requerida | **jueves 30-Jul-2026** (vencida; el propio Submittal Form la fija) |
| Veredicto propuesto | **3 — To be revised** |
| Tally | 1 Code 3 |

Documento único: `P22-BA-09-000-013` Rev A, *Fabrication and Testing Dossier Index*, 2 páginas, emitido IFA.

## Por qué Código 3 y no Código 2

El determinante es si **el propio documento** debe cambiar para llegar a Rev 0. Aquí no solo la respuesta es sí: el cambio es **estructural** — hay que agregar capítulos que no existen y tres columnas que no existen. Un Código 2 mandaría el documento directo a Rev 0 sin que ADASA vea el resultado, y este índice es precisamente el instrumento con el que ADASA verificará el dossier antes del FAT y antes de liberar el despacho. Rev A es primera emisión, donde el Código 3 no tiene costo procesal.

## Distinción que el transmittal debe hacer explícita

El veredicto califica **el Index como documento**. El **dossier como entregable de la ET Sección 7** no ha sido entregado y no se ve afectado por este código: sigue vencido, sigue en `NOT DELIVERED` como ítem 65 del Master Register, y sigue siendo prerrequisito de los ítems 8.3 y 8.4 del PIE, que soportan el 40% del pago. El tramo 2 del reclamo del 25-Jul (dossier preliminar completo, viernes 31-Jul) venció sin evidencia de entrega.

## Anotaciones para el CC_ADASA

**6 OBS + 4 NOTE = 10 anotaciones**, redactadas en inglés y listas para copiar desde la Sección 10 de `_ANALISIS_E69.md`. Consistente con la regla del proyecto: un Código 3 se anota completo.

| ID | Severidad | Asunto |
|---|---|---|
| OBS-01 | MAYOR | Sin código de documento, revisión ni estado de inclusión en ninguna de las 27 líneas; sin referencia cruzada a la fila del ITP que genera cada registro |
| OBS-02 | MAYOR | Falta el capítulo de preparación para el despacho (limpieza y preservación, embalaje y marcado, packing list) — ITP filas 8.1 y 8.2 |
| OBS-03 | MAYOR | Falta el Acta de Aprobación FAT emitida por ADASA — ET Sección 8 la declara parte integral del dossier final |
| OBS-04 | MAYOR | Falta el capítulo de calificaciones del personal de END y calibración del equipo de inspección — NDE Plan Sección 3.0, ITP fila 2.4 |
| OBS-05 | MAYOR | Falta el capítulo de certificados de fabricante y ensayos de fábrica de los equipos principales — ITP fila 2.3 |
| OBS-06 | MENOR | No declara en qué capítulo se archiva el paquete de los RO pressure vessels (certificación ASME X sin estampe, hidrostática a 1.800 psi × 1,1) — ITP fila 2.2, punto Hold |
| NOTE-01 | NOTA | Declarar si este es el índice preliminar de la fila 7.6 o el final de la 8.3, y mantener la misma numeración de capítulos en ambos |
| NOTE-02 | NOTA | Falta el registro de no conformidades y reparaciones de soldadura — NDE Plan Sección 9.0, ITP fila 7.9 |
| NOTE-03 | NOTA | Los capítulos B3, B4 y B6 listan procedimientos de UT, PT y RT nunca sometidos a aprobación de ADASA, que el NDE Plan Sección 2.0 exige |
| NOTE-04 | NOTA | Identificar explícitamente en el capítulo C9, spool por spool, los certificados de molino del super duplex con PREN mayor a 40 sobre UNS S32750 |

## Lo que falta para emitir

1. `crear_transmittal.py` clonado del N30, con `incluir_toc=True` y autoría fija Rivera / Rivera / Gutiérrez.
2. `P22-TM-09-000-031-0_TRANSMITTAL.md` en inglés, con la Sección 2 condensada (Response Code, Status corto y bloque `Action — re-issue as Rev B` citando el rango de IDs, sin reproducir la tabla de observaciones, que vive en el CC_ADASA).
3. `COMENTARIOS/agregar_comentarios_dossier_index.py` con las 10 entradas y el PDF fuente.
4. Sección 3 con los pendientes de transmittals previos.
5. Enlace Synology del paquete.
6. Validación con `anti-ia` modo `revisar` antes de emitir.

## Cuidado al redactar

**NOTE-03 no debe afirmar que hay soldadura ejecutada.** El informe de Bureau Veritas del 28-Jul deja el PMI de weldment pendiente porque no había soldadura, y BW Water lo declaró por escrito ese mismo día. El argumento correcto es que los procedimientos deben aprobarse **antes** de que la soldadura arranque, porque los registros producidos bajo procedimientos no aprobados no son admisibles en el dossier. Es más fuerte y no es refutable.

Referencias a la ET, al PIE y al ITP van por **código más número de sección deletreado**, nunca con el símbolo de sección. Sin referencias internas del propio transmittal ni menciones a Van Doorn.
