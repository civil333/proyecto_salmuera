---
titulo: Revisión del cronograma del 04-Ago-2026 y auditoría del análisis previo
codigo: E-CRONO-04AGO-REV
fecha: 2026-08-05
estado: INTERNO — no se envía
second_brain: skip
---

# Revisión del cronograma del 04-Ago y auditoría del análisis previo

> Se revisó `2026-08-04_TALTAL Water Treatment Plan Project _Progress Update.pdf` y se auditó `REVISION SEMANAL PO EQUIPOS/SEMANA 03-08-26/_ANALISIS_PROGRAMA_04AGO.md`, que lo tomó como fuente. Este documento no reemplaza aquel: dice qué de aquel sigue en pie, qué se cae, y qué aporta realmente el cronograma nuevo.

## 1. Sí, es el cronograma vigente — pero no lo era en todas partes

El `Progress Update` del 04-Ago se venía usando como el actual en los artefactos vivos: `Estado Vigente` y Bitácora del README, `hitos.yaml`, `compromisos.yaml` y el análisis del 04-Ago. **No** se usaba en los durables, que estaban cinco semanas atrás:

| Dónde | Declaraba | Corregido el 05-Ago |
|---|---|---|
| README, sección `Baseline Schedule` | *"CRONOGRAMA OPERATIVO VIGENTE = `Project Schedule 08-06-26` (Rev A)"*, EXW **14-15 Ago** | Cronograma del 04-Ago, EXW **19-21 Sep**; el Rev A pasa a histórico |
| `feedback_procurement_review_pattern`, que gobierna la revisión semanal de PO | *"juzgar avance contra Rev A… EXW Penang 14-15 Ago"* | La serie `Progress Update`, leída por ID de tarea |
| `hitos.yaml` H-06, H-07, H-08 | 18-Sep→08-Oct, 09-17 Oct, 18-Oct→16-Nov, atribuidos al Milestone Tracker | 10-19 Dic, 26-28 Dic, 29-Dic→02-Ene-2027 (IDs 421/423/424) |

El caso de H-06 a H-08 merece nombre: llevaban **fechas del baseline 05-Mar presentadas como vigentes**, tomadas de una hoja que el propio análisis había probado congelada. La revisión semanal de procura, mientras tanto, medía contra un hito muerto — un ítem "en ventana" contra el Rev A podía estar cinco semanas atrasado contra el cronograma real.

## 2. Qué aporta el 04-Ago sobre el 27-Jul: casi nada, y eso es el hallazgo

Verificado leyendo ambas extracciones, tarea por tarea:

| ID | Tarea | 27-Jul | 04-Ago | Δ |
|---|---|---|---|---|
| 414 | Factory Acceptance Test | 07-Sep → 18-Sep | 07-Sep → 18-Sep | **idéntico** |
| 415 | Shipping | 19-Sep → 13-Nov | 19-Sep → 13-Nov | **idéntico** |
| **416** | **System ready to ship (EXW Penang)** | **19-Sep → 21-Sep** | **19-Sep → 21-Sep** | **idéntico** |
| 417 | Package Delivery to Site | 13-Nov | 13-Nov | **idéntico** |
| 397 | Fabricación en taller Penang | fin 24-Ago | fin **21-Ago** | −3 días |
| 404 | Pre-ensamble e instalación | 31-Jul → 18-Sep (43 d) | **08-Ago** → 18-Sep (**36 d**) | inicio +8, fin fijo |

Ningún hito crítico se movió. El documento es **confirmatorio, no informativo**: su valor es que una segunda versión consecutiva sostiene el 21-Sep, no que traiga noticias.

**El dato que sí importa está en el ID 404.** El pre-ensamble arranca ocho días más tarde y termina el mismo día: la duración se comprime de 43 a 36 días. El análisis previo ya lo había nombrado —*"la fecha de embarque del 21-Sep se sostiene comprimiendo duraciones, no recuperando trabajo"*— y ahora hay dos versiones seguidas que lo muestran. La compresión del FAT va en la misma dirección: 15 días de línea base → 14 en el Recovery del 14-Jul → **11** en las dos últimas versiones.

## 3. La limitación del documento del 04-Ago

| | 27-Jul | 04-Ago |
|---|---|---|
| Páginas | 12 | **4** |
| Caracteres de texto | 51.135 | **13.195** |
| ID máximo | 424 | 424 |

Mismo plan, **impresión colapsada**. Faltan las filas de detalle de ingeniería (IDs 6 a 70) y buena parte del desglose. Los hitos críticos están todos, así que las conclusiones de arriba se sostienen; lo que no se puede hacer con este documento es **auditar el camino crítico tarea por tarea**. Se suma a que llegó **fuera del paquete semanal** y a que el paquete tampoco trajo el DDSR por segunda semana consecutiva. Se reclama junto con el DDSR.

## 4. Auditoría del análisis previo

### Sostiene

- **El anclaje contractual.** Cláusula 27 para el plazo (300 días desde la NTP del 07-Oct-2025 = 03-Ago-2026), 43.1 letra b) para la multa (0,2% diario), 43.4 para el tope de 15%. La distinción está bien hecha y es la que hay que citar.
- **El EXW del 19-21 Sep por convergencia de cuatro fuentes** del propio proveedor: cronogramas del 27-Jul y del 04-Ago (ID 416), meeting notes del 28-Jul, y el `Ready for shipment` del Fabrication Schedule del 03-Ago.
- **La descalificación del 10-Sep del Milestone Tracker**, con dos argumentos independientes: es una foto congelada del Recovery del 14-Jul, y está cargado en la columna `Actual` de un hito que no ha ocurrido, mientras `Estimate` sigue en la línea base.
- **Los diez movimientos silenciosos** (cinco en el tracker, cinco en el cronograma) y el **Change Log vacío en las cuatro versiones** comparadas.
- **La cadena crítica sin holgura**: llegada Fedco 02-Sep → posicionamiento 03-05 Sep → Dry Test y FAT 07-18 Sep → embarque 19-21 Sep. Un día de atraso en Fedco se traslada día a día.

### No sostiene

**El argumento del FAT.** El análisis y el registro sostenían que *"del 15-Sep al 18-Sep hay 4 días calendario para 7 jornadas contratadas"*. Esa cifra sale del **correo de BW Water del 28-Jul**; el **cronograma del 04-Ago, ID 414, da 11 días**, que sí acomodan las siete jornadas. Decisión del usuario: manda el cronograma. Si ADASA reclamara con la cifra de 4 días, BW Water respondería con su propio cronograma y el reclamo se caería solo.

Lo reclamable es otra cosa, y es más limpio: **dos documentos del proveedor, del mismo paquete, declaran fechas de FAT distintas**, y el inspector no se puede agendar sobre esa ambigüedad. Lo que se exige es que declare por escrito cuál gobierna. Corregido en `BV-13` y en `H-03`.

> ⚠️ **Corrección del 31-Ago-2026.** Este párrafo decía *"ADASA moviliza inspectores desde Chile"*, y es falso: **los inspectores son de Bureau Veritas Malasia, oficina BVKL, y atienden en Penang**. Lo que pasa por Bureau Veritas Chile es la contratación (Orden de Compra 836492) y la coordinación. El argumento correcto no es el viaje internacional sino que, sobre una fecha ambigua, no se le puede comprometer la agenda al inspector.

### Queda pendiente de verificar

Lo que el propio análisis declaró no verificado y sigue igual. El primero es el que bloquea una acción real:

1. **La fecha de la Notificación de Adjudicación.** Los 300 días se calculan sobre el `Contract Award / NTP` que rotula el cronograma **del proveedor**. Antes de cursar multa hay que leerla en el documento de adjudicación de ADASA: la coincidencia con la `Baseline Date` del Milestone Tracker es indicio fuerte, no prueba.
2. El **valor neto del contrato** para expresar la multa en monto y no solo en porcentaje.
3. La **fecha de emisión real del Manufacturing Schedule R5 de Fedco**, cuyo bloque de revisiones interno llega hasta la revisión 04 del 10-Jul.
4. El **27% del bloque Antiscalant** del Progress Report Week 31, extraído de una celda que el extractor fragmentó.

## 5. Una corrección de método

El análisis del 04-Ago fijó la jornada de inspección en el **12 y 13 de agosto**, tomándola de la minuta del mismo día. El `AQ-QAM-F027 Inspection Request (003)` —en el repositorio desde el 05-Ago a las 07:59— la fija en el **13 y 14**, y recorta el alcance. La minuta es un compromiso verbal; el Request es escrito y posterior.

El error se propagó a ocho archivos y llegó al correo del TM N30, emitido ese mismo día a las 14:20. La causa es acotada y evitable: **la búsqueda se hizo solo sobre `.md` y ese PDF no tenía extracción**. Regla que queda: en un frente donde las fechas se mueven por formulario, barrer también los PDF sin extraer de las carpetas del frente, no solo el texto ya indexado.

---

*Ver `_ANALISIS_PROGRAMA_04AGO.md` para el análisis completo del que esto es auditoría.*
