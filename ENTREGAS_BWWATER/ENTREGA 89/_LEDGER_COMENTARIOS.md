---
titulo: Ledger de cierre de comentarios — ENTREGA 89 (submittal 25007-0089)
fecha: 2026-09-03
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 89

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0089`, emitido el **martes 1 de septiembre de 2026**, con devolucion pedida al **viernes 4 de septiembre**: tres dias corridos. El vencimiento real de la Clausula 37.2, siete dias habiles, es el **jueves 10 de septiembre**. Sexto lote consecutivo por debajo del plazo contractual.

Llego como archivo comprimido con los nativos de AutoCAD ademas del PDF. Se desempaqueto verificando el contenido por hash, no el contenedor.

## Contenido del submittal

| # | Documento | Codigo | Rev | Emision | Origen |
|---|---|---|---|---|---|
| 1 | Piping & Instrumentation Diagram | `P22-DWG-09-009-002` | 0 | **IFC** | Rev D, Codigo 1 en el TM N18 |

Ademas, sin figurar en el formulario: `BWWA P&ID LEGEND_REV.0_250826.dwg` y `P22-DWG-09-009-02_REV.0_250826.dwg`, los nativos. **La lista real de la carpeta manda sobre la tabla del correo** y la diferencia se anota: son dos archivos que el formulario no declara.

## 1. Piping & Instrumentation Diagram Rev 0 — `P22-DWG-09-009-002`

**Origen:** Rev D, **Codigo 1** en el TM N18 del 18-May-2026. El N18 declaro que el plano no requeria modificacion y quedaba aprobado tal cual. **No habia condicion abierta que verificar.**

**Trae hoja de comentarios consolidada**, con cinco cambios que declara BW Water por iniciativa propia, no en respuesta a un comentario de ADASA.

| Punto | Declarado por BW Water | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| 1 | Orientacion del filtro de cartuchos cambiada a vertical | Correcto. Cierra un hallazgo conocido de ADASA sobre el layout | **Favorable** |
| 2 | Linea de drenaje del panel de instrumentos agregada, `RD-PVC-DN15-09-046` | Presente, y aparece tambien en la Line List Rev 1 | **Coherente** |
| 3 | Placa de orificio al analizador `CIT-09-004` cambiada por valvula reductora. *"Valve list to be updated and resubmitted"* | El propio proveedor declara que obliga a reemitir la Valve List, que no llego | **Genera pendiente** |
| 4 | Rotulado de linea agregado para los spools de super duplex de baja presion | Presente, pero **contradice a la Line List Rev 1** en dos numeros | 🔴 **Discrepancia** |
| 5 | Succion de la bomba CIP cambiada de PVC a SS316 | `CP-SS316-DN150-09-022` en la lamina 10, coincidente con la Line List Rev 1 | **Aceptado** como sustitucion menor |

### La discrepancia del punto 4, verificada

Lamina 10 del P&ID contra pagina 3 de la Line List Rev 1:

| Numero de linea | P&ID Rev 0 | Line List Rev 1 |
|---|---|---|
| 09-048 | `CP-SSD-DN65-09-048` | `CP-SSD-DN80-09-048`, 2ND STAGE CIP REJECT OUT |
| 09-049 | `CP-SSD-DN80-09-049` | `CP-SSD-DN65-09-049`, 1ST STAGE CIP REJECT OUT |

Diametros opuestos, sobre spools a fabricar, y precisamente en el rotulado nuevo que la reunion de coordinacion del 26 de agosto pidio unificar. Los dos documentos llegaron ademas en dias distintos, el 1 y el 3 de septiembre, contra un criterio que los pedia juntos y con los planos de fabricacion.

**ADASA determina cual esta mal, y lo declara.** La columna de caudal de la propia Line List lo resuelve: el rechazo CIP de primera etapa lleva **54 m3/h** y el de segunda **36 m3/h**, y el par de **alta presion aprobado en Rev 0** los dimensiona **DN80** y **DN65** respectivamente (`CP-SSD-DN80-09-044` y `CP-SSD-DN65-09-045`). El par nuevo de baja presion invierte esa correspondencia: asigna DN65 al servicio de 54 m3/h y DN80 al de 36. El P&ID Rev 0 los rotula al reves de la lista, o sea **correctamente**.

**Medidas vinculantes que declara el transmittal:** el rechazo CIP de primera etapa a baja presion es `CP-SSD-DN80-09-049` y el de segunda `CP-SSD-DN65-09-048`. **El P&ID no cambia; la que se corrige es la Line List**, antes de fabricar esos spools.

## Sintesis

El plano venia de Codigo 1 y sin condicion abierta, y se emite para construccion. **Sobre un Rev 0 no se agregan comentarios nuevos**: la determinacion de las medidas y los cambios propios se documentan en el texto de la subseccion, en la Seccion 3 del transmittal y en el correo, sin degradar el codigo y sin PDF anotado. Este plano ademas es el que esta correcto.

La unificacion de numeracion no puede cerrarse en este ciclo de ninguna manera, porque exige ademas los planos de fabricacion, que no llegaron.

**Codigo propuesto: 1 — Approved.**
