---
titulo: Ledger de cierre de comentarios — ENTREGA 84 (submittal 25007-0084)
fecha: 2026-08-26
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 84

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0084`, "Project Schedule & General Arrangement Drawings", emitido el lunes 24-Ago-2026, devolucion pedida el jueves 27-Ago-2026, plazo real de la Clausula 37.2 el miercoles 2-Sep-2026. Tres documentos.

**Regla de alcance aplicada.** Los tres vienen de un codigo previo. Se verifica unicamente si las condiciones de ese codigo estan incorporadas.

---

## 1. GA of SWRO System Skid Rev 0 (IFC) — `P22-DWG-09-005-008`

Seis paginas: portada, dos laminas, dos de hoja de comentarios y una captura de pantalla. Venia de **Codigo 2 en el TM N31**, cuya unica accion fue corregir tres referencias documentales del bloque de notas.

| Punto del TM N31 | Pedido, literal | Declarado en la hoja | Verificado en la Rev 0 | Estado |
|---|---|---|---|---|
| Nota 6 | "note 6 cites the Instrument List at Rev D where the current revision is Rev E" | "Note 6 and 7 has been corrected accordingly" | La **Hoja 2** dice `P22-LI-09-008-003_INSTRUMENT LIST REV.E`. La **Hoja 1 sigue diciendo `REV.D`**. La correccion se aplico en una sola de las dos laminas | **Cierre parcial** |
| Nota 7 | "note 7 cites P22-LI-09-009-00 where the approved Line List is P22-LI-09-009-003" | "Note 6 and 7 has been corrected accordingly" | Las dos hojas dicen `P22-LI-09-009-003 - LINE LIST REV.0` | **Cerrado** |
| Nota 8 | "note 8 cites P22-ET-09-006-01, which is not a valid document code in the project numbering" | "As for Note 8, snapshot is showing the document number has already been submitted in the earlier stage of the project" | Sin cambio en las dos hojas: `8. FOR NOMINAL THICKNESS PER PIPELINE - REFER TO : P22-ET-09-006-01 - PIPING SPECIFICATIONS`. **La propia captura que adjuntan para justificarlo escribe el codigo con tres digitos**, `P22-ET-09-006-001`, y la fila siguiente de esa misma captura es `P22-ET-09-006-002 Painting Specification`. La evidencia que invocan confirma el punto en vez de refutarlo | **No cerrado** |

Peso del punto abierto: la nota 8 es la que remite al espesor nominal por linea, sobre un plano emitido **para construccion**.

### Disposicion: Codigo 1, y por que

**Los dos puntos abiertos son de cita, no de contenido.** `P22-ET-09-006-01` esta a un digito de `P22-ET-09-006-001` y el titulo coincide; la nota 6 trae el codigo correcto en las dos hojas y solo el indice de revision desactualizado en una. Ninguno cambia una cota, un material, un rating ni una cantidad del skid, y los dos documentos referidos siguen siendo identificables.

**Y el plano esta en Rev 0 emitido para construccion**, de modo que no se devuelve a revision por un defecto de forma: sobre un Rev 0 el Codigo 3 queda reservado a un defecto sustantivo que obligue a rehacer el documento.

**Codigo 1, sin CC_ADASA.** El PDF anotado que se habia generado se retiro a `_skid_fuera_de_anotacion/`, en esta misma carpeta de entrega, con su evidencia. **El tono no baja con el codigo**: el transmittal enuncia que de las tres referencias solo una se corrigio, que la respuesta a la nota 8 queda refutada por el anexo del propio proveedor, y escribe literal el codigo correcto para que quede en el registro.

### Fuera de alcance (no se emite)

- El cajetin declara `DRAWING STATUS: ISSUED FOR APPROVAL` en las dos hojas, mientras la fila 0 de la tabla de revisiones dice `ISSUED FOR CONSTRUCTION` con fecha `AUG.17.26`, y las fechas de preparado, revisado y aprobado siguen en `JUL.27.26`, que es la fecha de la Rev B. **Housekeeping documental: observacion nueva, no se emite.**
- La nota 5 cita `P22-LI-09-005-002 _VALVE LIST REV.D` en las dos hojas. No formaba parte del pedido de las tres referencias. **No se emite.**

---

## 2. GA of Antiscalant Dosing Tank Rev C — `P22-DWG-09-005-015`

Tres paginas: portada, plano (rotacion 270) y hoja de comentarios. Venia de **Codigo 3 en el TM N26**, el unico Codigo 3 del lote.

| Punto del TM N26 | Pedido, literal | Declarado en la hoja | Verificado en la Rev C | Estado |
|---|---|---|---|---|
| OBS-01 — cargas sismicas y patron de pernos | "add the anchor-bolt pattern and the NCh 2369 seismic reaction loads (or reference the endorsed Module Seismic Calculation Report)" | "1. Reaction loads stated in the drawing" | **Nota 16**: `TOTAL SEISMIC REACTION FORCES (AS PER CALCULATION REPORT)` con `SumFx = 6,73 kN`, `SumFy = 5,86 kN`, `SumFz = 4,81 kN`. **Nota 15**: centro de gravedad `Z = 560 MM FROM BOTTOM`. **Detalle 4, nuevo en esta revision**, `BOLTING EMBEDMENT` 1:2, con `M12 HH BOLT C/W WASHER`, carga por perno `Fx = 2,24 kN`, `Fy = 1,95 kN`, `Fz = 1,60 kN` y empotramiento `MIN 150`. **Detalle 3** `ANCHORING DETAILS` 1:5 con tres orejas, placa 100 x 100, saliente 80, agujero, radio R74. Las tres posiciones angulares se leen del Detalle 2: 90, 210 y 330 grados. Las cargas por perno son consistentes con tres apoyos (6,73/3 = 2,24; 5,86/3 = 1,95; 4,81/3 = 1,60) | **Cerrado con residuo** — ver abajo |
| OBS-02 — volumen util efectivo | "state the effective working volume" | "2. Effective working volume added in notes" | **Nota 8**: `EFFECTIVE WORKING VOLUME 0.27 M3`, junto a la nota 7 `TANK CAPACITY 335 L` | **Cerrado** |
| OBS-02 — fila LEVEL MARKING | "the LEVEL MARKING row is blank" | no responde este punto por separado | La fila `LM` de la tabla de boquillas paso de `LEVEL MARKING / - / - / -` en la Rev B a `LEVEL MARKING / - / SIDE / -`. Se poblo la ubicacion; el tamano y la **elevacion** siguen con guion, de modo que el volumen util declarado no tiene cota que lo materialice | **Cierre parcial** |
| NOTE-02 — TAG del equipo | "label the equipment tag TK-09-002" | "3. Drawing labelled with the correct equipment tag" | Cajetin, campo `DRAWING TITLE`: `DETAIL - ANTISCALANT DOSING TANK / TK-09-002`. En la Rev B ese campo no traia TAG. Unica ocurrencia en la lamina | **Cerrado** |
| NOTE-01 | accion sobre el P&ID, no sobre este plano | — | Se confirma que sigue siendo accion sobre el P&ID | **No aplica a este documento** |

### Residuo de la OBS-01, dentro del alcance

El pedido fue "add the anchor-bolt pattern". Verificar que lo agregado es correcto forma parte de verificar el cierre, no es abrir un frente nuevo. Dos cosas quedan por reconciliar en el propio detalle que se agrego:

- El agujero del Detalle 3 rotula **`Ø14 [Ø1/2"]`**, y esos dos valores no son equivalentes: media pulgada son 12,7 mm. En la Rev B el mismo rotulo decia `Ø10 [Ø1/2"]`, de modo que la cota metrica cambio y la imperial no. El perno declarado en el Detalle 4 es **M12**, que en un agujero de 14 mm tiene la holgura normal de montaje y en uno de 12,7 mm queda en ajuste estrecho.
- El radio rotula `R74 [R3"]`, otra pareja que no es equivalente. **No se emite**: es identico en la Rev B y en la Rev C, de modo que no forma parte de lo agregado y cae fuera de la regla de alcance.

### Dependencia que no degrada a este plano

La nota 16 declara las cargas `(AS PER CALCULATION REPORT)` **sin citar el codigo ni la revision del informe**. El informe que las produce es el `P22-CD-09-005-001`, que sigue **sin el endoso de un ingeniero profesional chileno** (compromiso `PRG-32`, critico y vencido). Las cargas que alimentan el diseno de fundacion de obras civiles provienen de un informe sin endosar. **Es dependencia sobre otro documento: va a la Seccion 3 y no degrada a este plano.**

### Fuera de alcance (no se emite)

- El cajetin declara `ISSUED FOR APPROVAL` con fechas de preparado, revisado y aprobado en `MAY.19.26`, aunque la fila de revision C es `AUG.19.26`. **Housekeeping: no se emite.**
- El comentario del ciclo de la Rev A pedia ademas declarar el volumen total instalado como 0,34 metros cubicos; la nota 7 mantiene `335 L`. El TM N26 **no** lo repitio en su accion sobre la Rev B, de modo que exigirlo ahora seria leer de mas. **No se emite.**

---

## 3. Project Schedule Rev B — `P22-BA-09-000-001` — RETIRADO DEL TRANSMITTAL N36

> **Decision del usuario, 26-Ago-2026:** el seguimiento del cronograma se lleva por la **reunion semanal de coordinacion**. El documento no recibe codigo de respuesta en el TM N36 y su PDF anotado no se emite. **Todo lo que sigue se conserva verificado**, para esa reunion y por si el punto vuelve al eje documental. El paquete retirado esta en `_cronograma_fuera_de_transmittal/`, en esta misma carpeta de entrega.

Catorce paginas: portada mas trece de diagrama de barras. Venia de **Codigo 2 en el TM N20**. **No trae hoja de comentarios consolidada** y la palabra "comment" no aparece en ninguna pagina.

| Punto del TM N20 | Pedido, literal | Verificado en el Rev B | Estado |
|---|---|---|---|
| OBS-01 — base de certificacion de los recipientes | "state the certification basis consistent with the 02-Jun waiver" | **Cero ocurrencias** de `ASME`, `stamp`, `certif` y `waiver` en las catorce paginas. El bloque de los recipientes son cuatro tareas encadenadas (`PR/PO`, `Drawing Internal Approval`, `Manufacturing (Vendor)` y `Shipping to Penang (from Spain-by airfreight)`), sin actividad de certificacion, liberacion ni inspeccion entre ellas | **No cerrado** |
| OBS-02 — ensayos de presion | "add the factory vessel hydrostatic test and the pre-FAT system hydrostatic tests as discrete, dated activities" | **Cero ocurrencias** de `hydro`, `hydrostatic`, `pressure test` y `leak`. Las dos unicas tareas del programa que contienen la palabra `Test` son la 414 `Factory Acceptance Test for System` y la 424 `Performance Test`, esta ultima en obra. La 414 **no tiene subtareas**, de modo que tampoco alberga los ensayos de sistema previos al FAT. `Protec` y `Arisawa` no aparecen | **No cerrado** |
| Tercera clausula de la accion | "The baseline adoption of 09-Jun-2026 is not re-opened by these actions" | La columna `Baseline1` conserva integros los cuatro anclajes del Rev A: 23-Jun, 2-Ago, 15-Ago y 19-Nov de 2026 | **Cumplido** |

### Lo que el Rev B mueve (dato factual, va por la cadena contractual)

| Hito | Tarea | Linea base | Proyectado en el Rev B | Desplazamiento |
|---|---|---|---|---|
| Recipientes ex-works Espana | 300, `Manufacturing (Vendor)` | 23-Jun-2026 | 29-Jun-2026, cumplido | +6 dias |
| Llegada a Penang | 301, `Shipping to Penang` | 2-Ago-2026 | 4-Jul-2026, cumplido | 29 dias de adelanto |
| Fabricacion en Penang | 397 | 10-Ago-2026 | 28-Ago-2026, al 67 por ciento | +18 dias |
| Fabricacion de spools de caneria | 398 | 5-Ago-2026 | 28-Ago-2026, al 70 por ciento | +23 dias |
| **FAT del sistema** | 414 | 24-Jul al 13-Ago-2026, 15 dias declarados | **7 al 18-Sep-2026, 11 dias declarados** | +36 dias, y la ventana declarada se acorta de 15 a 11 dias |
| **Ex-works Penang** | 416 | 14 al 15-Ago-2026 | **19 al 21-Sep-2026** | **+37 dias** |
| Entrega en sitio | 417 | 30-Sep-2026 | **13-Nov-2026** | +44 dias |
| Fin del programa | 0 / 424 `Performance Test` | 19-Nov-2026 | **2-Ene-2027** | **+44 dias** |

Precisiones verificadas:

- **No existe hito de embarque ni de zarpe.** El resumen 415 `Shipping` abarca 48 dias entre el ex-works Penang y la entrega en sitio, sin desglose de transito maritimo, aduana ni transporte interno.
- **No existe tarea de SAT ni de puesta en servicio.** El arranque en obra se representa con `Start UP`, `Training` y `Performance Test`. Las palabras `SAT`, `commissioning` y `Chile` no aparecen.
- El documento **no declara fecha de corte ni version de linea base**: la columna se rotula `Baseline1`, el nombre por defecto de la herramienta, sin decir a que revision ni a que fecha de adopcion corresponde. Lo unico fechado es el pie automatico, `Date: 8/18/2026`.
- La tarea 419 rotula `ADISA` en vez de ADASA.
- El deslizamiento se acumula entre la fabricacion en Penang y el FAT: +18 dias al cierre de fabricacion y +37 en el ex-works. Entre el ex-works y la entrega en sitio crece siete dias mas, porque el tramo de embarque se alarga de 46 a 53 dias corridos; de ahi al fin se mantiene en +44, ya que el tramo de obra conserva sus 50 dias.
- La ventana del FAT declara once dias entre el 7 y el 18 de septiembre, que son diez dias habiles. La duracion declarada y el calendario no cuadran por un dia; conviene fijar el dato antes de citarlo en el correo contractual.

### Fuera de alcance (no se emite)

- La tarea 419 rotula `ADISA` en vez de ADASA. **Housekeeping documental: observacion nueva, no se emite.**
- El documento no declara fecha de corte ni version de linea base: la columna se rotula `Baseline1`, el nombre por defecto de la herramienta. El TM N20 no lo pidio. **No se emite**, aunque conviene tenerlo presente al citar la linea base en la cadena contractual.

### Fuera de alcance del transmittal

Todo el contenido de la tabla de hitos es **materia contractual**, no disposicion documental: el Plazo de Entrega vencio el 03-Ago-2026 y la exposicion se rige por la Clausula 27 (plazo), la 43.1 letra b (multa) y la 43.4 (tope). Va por **correo separado**, en su propia cadena. El transmittal solo dispone el codigo del documento por el cumplimiento de las dos observaciones del TM N20.
