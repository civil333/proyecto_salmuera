---
titulo: Ledger de revisión — ENTREGA 96 (submittal 25007-0096)
fecha: 2026-10-05
estado: INTERNO
type: ledger
project: salmuera-taltal
second_brain: skip
---

# Ledger de revisión — ENTREGA 96

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0096`, emitido el martes 22-Sep-2026, devolución pedida el viernes 25-Sep. El plazo de la Cláusula 37.2 venció el jueves 1-Oct (el feriado del 18 y el 19 es anterior a la recepción y no cuenta). Cuatro documentos:

| # | Documento | Rev | `Sub. For` | Viene de |
|---|---|---|---|---|
| 1 | Piping Layout `P22-DWG-09-005-004` | E | IFA | Código 2 en el N36 (Rev D) |
| 2 | Maintenance Lifting Points Layout and Details `P22-DWG-09-005-006` | A | IFA | Primera emisión |
| 3 | GA of Antiscalant Dosing Tank `P22-DWG-09-005-015` | E | IFA | Código 2 en el N39 (Rev D) |
| 4 | PLC/LCP FAT Procedure - Hardware `P22-PP-09-000-001` | 0 | IFC | Código 2 en el N38 (Rev C) |

Los tres planos traen su `.dwg`. Dos copias de la Rev E del Piping Layout, idénticas byte a byte, quedaron en `_duplicado_payload_identico/`.

**Regla de alcance.** Las reemisiones se revisan contra lo pedido, con la hoja de comentarios ítem por ítem y lo que el proveedor agregó. La primera emisión se revisa contra la ET.

---

## 1. Piping Layout Rev E — `P22-DWG-09-005-004`

Cinco páginas: portada, tres láminas A1 rotadas 270° y la hoja de comentarios. Rev E del **10-Sep-2026**, "REVISED FOR APPROVAL".

### Cierre punto por punto contra el N36 (Sección 2.2)

| Pedido, literal | Declarado en la hoja | Verificado en la Rev E | Estado |
|---|---|---|---|
| "add one row per CIP battery-limit connection and state the datum of the elevations" | "Datum added" / "CIP BL added, with related information in table format" | Tabla de 9 filas. Suma `TP-CP P10-001` CIP FEED 4", `TP-CP P9-001` CIP RETURN 4" y `TP-PE P9-003` MAKE-UP CIP 3". Nota 1: "DATUM (EL. +0.00) FOR THE TIE-INS ARE INDICATED IN SECOND & THIRD PAGE DRAWING". La lámina 2 marca `EL. + 0.00m` y las cotas `EL. + 2.597m`, `2.94m` y `2.947m` | **Cerrado** |
| "State the flange class of the antiscalant and CIP terminations against the approved Line List" | "AS and CIP BL labelled accordingly" | Todas las filas con `RATING` y `STD`: `TP-AS P11-001` 1" **SW 150 ASME B16.5**, las CIP en FL 150 ASME B16.5. En la Rev D eran guiones | **Cerrado** |
| "state whether the module carries one or two local control panels, tagging each enclosure" | "Control panels labelled accordingly" | Dos envolventes con TAG: `LCP PLC & INSTRUMENT (SAI-09-001)` y `CIP HEATER CONTROL PANEL (REL-09-001)`, coherentes con los alimentadores del Schematic Rev C (SAI-09-001 2,0 kW y REL-09-001 20 kW) | **Cerrado** |

La hoja de comentarios transcribe esta vez la acción completa del N36, y la responde punto por punto.

### Lo que el proveedor agregó (diff de texto D contra E)

- La tabla de tie-in completa y las cotas EL. de la lámina 2.
- **Seis líneas super dúplex nuevas**: `CP-SSD-DN100-09-051`, `CP-SSD-DN80-09-047`, `CP-SSD-DN80-09-049`, `CP-SSD-DN65-09-048`, `DA-SSD-DN65-09-052` y `DA-SSD-DN100-09-050`. Las seis están en la Line List Rev 2 aprobada en el N40.
- El rótulo `DA-SSD-DN65-09-009` sale de la lámina 1 pero sigue en la lámina 2, y la Line List Rev 2 lo mantiene. No se emite.
- La tabla rotula la conexión de antiescalante `TP-AS P11-001`, y la planta y la isométrica la rotulan `TP-DA P11-001` (`AS-PVC-DN25-09-031`). Es de forma y nuevo en la Rev E, y se identifica por la línea. No se emite.
- 🔴 **Hallazgo de la verificación de lo agregado.** Cruzando los TAG de línea del plano contra la Line List Rev 2, la succión de la bomba CIP figura como **`CP-PVC-DN150-09-022`** en la lámina 1 ("TO CIP PUMP") y en la lámina 3 ("TO CIP PUMP INLET"). La Line List Rev 1 (N38) y la Rev 2 (N40), ambas en Código 1, la llevan como **`CP-SS316-DN150-09-022`, 316L**. Su hoja de comentarios lo declara: "CIP Pump suction changed to SS316". Es la misma línea de la VM-09-065, que lleva la Valve List a Código 3 en este transmittal. El rótulo ya venía en la Rev D, y el cambio de material es posterior a la aprobación de esa revisión.

**Otras dos diferencias de TAG, que no se emiten.** `CP-PVC-DN80-09-019` (make-up) contra `PE-PVC-DN80-09-019` de la Line List es solo prefijo de servicio, y el mismo plano trae la segunda forma en la lámina 2. `RD-PVC-DN15-09-001` no es hallazgo nuevo: el N36, Sección 2.3 (modelo 3D), pidió resolver la reutilización de la línea 09-001 y darla de alta en la Line List, y la Rev 2 sigue sin ella. Va a la Sección 3 del N42 como pendiente del N36.

### Disposición

**Código 1**, sin CC_ADASA. Las tres condiciones del N36 y la NOTE-01 están cerradas.

**El rótulo de la línea 022 no se emite.** Primero se propuso Código 2 para alinearlo con la Line List. Se retiró el 5-Oct-2026 por instrucción de Luis: *"para las revisiones E debiésemos estar revisando que los comentarios hechos se levantaron, no incluir más nuevos a no ser que sean errores garrafales que no vimos antes"*. Un TAG desalineado con la Line List, que es la que gobierna el material de línea, no es garrafal. El script y el PDF que se alcanzaron a generar quedan en `REVISIONES/TRANSMITTALES/P22-TM-09-000-042-0/COMENTARIOS/_no_emitido/`. **Riesgo que se acepta:** la Rev 0 del plano puede salir con PVC en la línea en que ADASA rechaza la válvula en PVC. Si BW Water lo invoca para defender la VM-09-065, la respuesta es que la Line List Rev 2 aprobada gobierna el material.

**Fuera de este código, a la Sección 3.** La Rev E es del 10-Sep, anterior a la modificación de los spools 004 y 008 del 22-Sep. Victor pidió una Rev F el 24-Sep y el 1-Oct. La Sección 3 pide las isométricas de los spools modificados y que la Rev 0 refleje cualquier cambio de recorrido.

Recortes: `render/piping_E_h2.png`, `render/piping_E_h3.png` y `render/piping_E_h4.png`.

---

## 2. Maintenance Lifting Points Layout and Details Rev A — `P22-DWG-09-005-006`

Dos páginas: portada (18/09/2026) y una lámina A1 rotada 270°, "ISSUED FOR APPROVAL", SEP.18.26. Primera emisión del entregable que el N39 listaba como no recibido en su Tabla 4.

**Requisito.** ET Sección 7, pág. 28: *"Propuesta de vigas carrileras y puntos de izaje internos dentro del módulo, para extraer equipos mecánicos (Bombas y Turbos)."* Los equipos mecánicos del módulo son la bomba de alta presión `BH-09-001` (Fedco MSD-7016, 3.291 mm de largo) con su motor de 93 kW, y los turbocargadores `SIP-09-001` (feed) y `SIP-09-002` (interstage), Fedco HPB-60, según el Equipment List.

| Qué pide la ET | Qué trae la lámina | Estado |
|---|---|---|
| Puntos de izaje para bombas y turbos | **Un solo punto, sobre el motor de la bomba de alta presión** (a 2.224 del extremo y a 411 y 364 de la pared), con gancho, eslinga y eslabón. El cuerpo de la bomba va en línea de trazos. **Los dos turbocargadores no aparecen** | **No cerrado** |
| Vigas carrileras o punto fijo interno | **Ninguno.** El gancho cuelga a 1.422 mm aprox. sobre el piso, sin estructura dibujada encima. La nota 2 dice "LIFTING METHOD IS ONLY FOR REFERENCE, TO BE VERIFIED BY LIFTING CONTRACTOR" | **No cerrado** |
| Extracción fuera del módulo | Sin recorrido ni puerta indicada | **No cerrado** |
| Capacidad del punto | Sin WLL. La nota 3 remite al datasheet de la bomba | **No cerrado** |

El título dice "Layout & Detail" y la lámina no trae ningún detalle del punto de izaje.

### Disposición

**Código 3, reemitir como Rev B.** La lámina no contiene lo que la ET pide: ni viga carrilera, ni punto fijo, ni los turbos.

| ID | Ancla | Texto ejecutivo (borrador) |
|---|---|---|
| OBS-01 | vista en planta, motor | Solo cubre el motor de BH-09-001. Corregir: punto de izaje y recorrido de salida para las bombas y los turbocargadores SIP-09-001 y SIP-09-002 (ET Sección 7, pág. 28). La ET dice "Bombas" en plural; el texto no enumera las bombas para no afirmar cuáles quedan dentro del módulo |
| OBS-02 | vista frontal, gancho y nota 2 | El gancho cuelga sin viga carrilera ni punto fijo, y la nota 2 deja el método al contratista de izaje. Corregir: dibujar la viga carrilera o el punto fijo, su unión a la estructura del módulo y su WLL contra la pieza más pesada que levanta |

Recortes: `render/lifting_points_A_completa.png`, `render/lifting_points_A_frontal.png` y `render/lifting_points_A_isometrica.png`.

---

## 3. GA of Antiscalant Dosing Tank Rev E — `P22-DWG-09-005-015`

Tres páginas, lámina A1 rotada 270°, Rev E "ISSUED FOR APPROVAL" SEP.18.26. **Tercer ciclo** del mismo punto: N36 (Rev C), N39 (Rev D) y ahora la Rev E.

| Pedido, literal (N39) | Declarado en la hoja | Verificado en la Rev E | Estado |
|---|---|---|---|
| "state the size and the elevation of the level marking row, the elevation being the one that corresponds to the effective working volume of note 8" | "1. No size for Level Markings, dimensions on the markings are to scale" / "2. Exact elevation that corresponds to 0.27 cubic meter is now indicated in the drawing" | **La vista 1 sí lo marca**: `864 [2'-10"]` con `0.27 m³`. **La tabla de boquillas dice otra cosa**: fila `LM LEVEL MARKING`, SIZE `-`, ELEVATION **`3' 7"`**. 3'-7" es la cota de 1.085 mm de la altura total del estanque, y queda **sobre el rebalse N80 a 39 3/8"** (1.000 mm), físicamente imposible para un nivel de trabajo | **Parcial: el plano se contradice** |

El tamaño en guion se acepta: una marca no tiene diámetro y la respuesta es razonable. Exigirlo sería pedir de más.

### Disposición

**Código 2, reiterado con constancia de tercer ciclo.** El Status deja dicho que la Rev E es la segunda revisión de aprobación que no se pidió: el N36 y el N39 ordenaron emitir en Rev 0. Es IFA, así que la condición aún no vence (regla de la columna `Sub. For`). **ADASA declara el valor vinculante**: 864 mm, que en la columna en pulgadas de la tabla es 34". Se corrige al emitir la Rev 0.

| ID | Ancla | Texto ejecutivo (borrador) |
|---|---|---|
| OBS-01 | fila `LM LEVEL MARKING` | La fila LM dice 3' 7", la altura total del estanque, sobre el rebalse N80 a 39 3/8"; la vista 1 fija los 0,27 m³ en 864 mm. Corregir en Rev 0: elevación LM 34" (864 mm) |

Recortes: `render/ga_tanque_E_tabla_LM.png` y `render/ga_tanque_E_vista1_0.27m3_864mm.png`.

---

## 4. PLC/LCP FAT Procedure - Hardware Rev 0 — `P22-PP-09-000-001`

22 páginas, IFC. Hoja de comentarios en la página 22.

| Pedido, literal (N38 Sección 2.11) | Declarado en la hoja | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| OBS-01: "channel 7 of the output module, relay KA8, is the CIP heater on and off command [...] Correct the remarks column of that row accordingly" | respondido | Página 15: "DO Channels 7 → Relays KA8: CIP Heater ON/OFF Command [...] KA8 – CIP Heater ON/OFF. Tag:REL-09-001-HS001". Ya no figura como spare | **Cerrado** |
| OBS-02: "Write each output row with the full tag the I/O List carries" | "Rev0 is has been revised", con la lista KA4 a KA8 | KA4 `BH-09-001-HS001`, KA5 `BH-09-002-HS001`, KA6 `BDS-09-001-HS001`, KA7 `BDS-09-002-HS001`, KA8 `REL-09-001-HS001` | **Cerrado** |

### Disposición

**Código 1**, sin CC_ADASA. Los ocho ítems de categoría A del punch list son del registro de la Rev B y no de este procedimiento (lo dijo el N38). Siguen en la Sección 3, en la línea "Also open".
