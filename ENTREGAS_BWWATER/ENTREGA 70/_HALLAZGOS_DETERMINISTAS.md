---
titulo: Hallazgos deterministas de la ENTREGA 70 — verificados por script y por lectura visual
codigo: E70-HALLAZGOS
fecha: 2026-08-05
estado: INTERNO — insumo del TM N30, no se envia
second_brain: skip
---

# Hallazgos deterministas — ENTREGA 70 (submittal 25007-0070)

> Documento interno de trabajo. Reúne lo que se verificó **por script o por lectura visual directa**, no por inferencia de un agente. Es la base contra la que se contrasta la salida del workflow de revisión antes de que nada llegue al transmittal.

## 1. Lo que trae la entrega

| # | Documento | Código | Rev | Tipo | Sub. For |
|---|---|---|---|---|---|
| 1 | Piping Layout | `P22-DWG-09-005-004` | C | DWG | IFA |
| 2 | 3D MODEL (`V14 Taltal.nwd`) | `P22-DWG-09-005-007` | A | DWG | IFA |
| 3 | Datasheet of Differential Pressure Switch | `P22-LI-09-008-006` | B | DOC | IFA |

Emitida el miércoles 05-Ago-2026 por Fitri Indriyani. **Mapeo confirmado sobre el render del formulario**, no sobre la extracción de texto, que interleaba las columnas y asignaba mal el tipo de documento.

**Req. Return Date declarada: sábado 08-Ago-2026**, tres días corridos desde la emisión. La BAE Cláusula 37.2 concede a ADASA un plazo estándar de **siete días hábiles** de revisión documental, que vencen el **viernes 14-Ago-2026**. ADASA no incurre en mora por no responder el día 8.

**La columna `Remarks` del formulario está vacía en las tres filas.** El propio formulario define ahí los códigos de estado previo (`Code 1 No update` / `Code 1 Previously submission w. update/amendment` / `Code 2 Previously` / `Code 3 Previously` / `New Submission`). Sin ese dato, el formulario no declara que el datasheet ya estaba aprobado ni que el modelo es primera emisión.

---

## 2. El PDF trae 22 páginas para un documento que declara 4

**Verificado sobre la portada y sobre el propio PDF, página por página.** La portada del documento controlado dice literalmente:

> `ADASACode: P22-DWG-09-005-004` · `Date: 27/07/2026` · `Revision No.: C` · **`Page: 1 of 4`**

Historial de revisiones del cajetín de portada: Rev A 03-03-2026, Rev B 02-04-2026, **Rev C 27-07-2026**. Preparado CAD, revisado AIA, chequeado SI, aprobado LPL; la columna `Customer` está en blanco, como corresponde.

**El archivo entregado tiene 22 páginas.** Su composición real:

| Páginas | Qué son | Numeración | Formato |
|---|---|---|---|
| 1 | Portada del documento controlado | `P22-DWG-09-005-004` Rev C, "1 of 4" | A4 vertical |
| 2, 3, 4 | Las tres láminas del Piping Layout | `P22-DWG-09-005-004` Rev C | A1 apaisada |
| **5 a 21** | **17 páginas con 11 planos de taller de BW Water** | **`25007-ME-PI-0901-0006` a `-0016`** | A1 y A2 |
| 22 | Lámina final sin numeración BW | — | A4 apaisada |

Es decir: **18 de las 22 páginas quedan fuera del documento que la portada declara**. Los once planos de taller son `-0006`, `-0007`, `-0008`, `-0009`, `-0010`, `-0011`, `-0012`, `-0013`, `-0014`, `-0015` y `-0016`; varios ocupan dos páginas.

**Confirmado visualmente en el cajetín de la lámina 11:**

| Lo que declara el submittal | Lo que dice el cajetín de la lámina 11 |
|---|---|
| `P22-DWG-09-005-004`, Rev **C** | `25007-ME-PI-0901-0010`, Rev **1** |
| Piping Layout | `DA-SSD-DN100-09-003` — el título es un TAG de línea: es un plano de spool |
| Issued for Approval | Doble sello: **FOR CONSTRUCTION** (preparado, chequeado y aprobado, firmado el 23-07-2026) y **SHOP FABRICATION** |
| — | Tabla de revisión propia: `1 · 20/07/2026 · ISSUED FOR APPROVAL · AHR · AIA` |

**Barrido de sellos, leído del PDF página por página:**

| Sello | Láminas |
|---|---|
| `ISSUED FOR APPROVAL` | 20 de 22 (todas menos la portada y la 22) |
| **`FOR CONSTRUCTION`** | **17 de 22 — exactamente las páginas 5 a 21**, es decir las 17 que componen los once planos de taller |
| `SHOP FABRICATION` | 0 en la capa de texto, pero **visible en el PNG de la lámina 11** |

Las láminas 2, 3 y 4 —las únicas que pertenecen al documento controlado— llevan solo `ISSUED FOR APPROVAL`, como corresponde. El sello de construcción está en las otras diecisiete y en ninguna del layout.

> **La capa de texto sub-detecta.** Sobre el `.md` extraído por la skill aparecían 4 números internos y 3 sellos; sobre el PDF aparecen 11 números y 17 sellos. Y `SHOP FABRICATION` no aparece en ninguna búsqueda de texto pese a estar impreso, porque es un sello gráfico. **Toda afirmación sobre sellos y cajetines se sostiene en la imagen o en el texto del PDF, nunca en el `.md` intermedio.** El conteo de `SHOP FABRICATION` no se puede declarar: solo consta en la lámina que se abrió.

Cuatro consecuencias:

1. **La fabricación avanza sobre planos que ADASA no ha aprobado.** Las láminas están firmadas y liberadas a taller el 23-07-2026, con doble sello de construcción y fabricación; el paquete llega a revisión el 05-08-2026, trece días después.
2. **Se rompe la trazabilidad documental.** Las láminas llevan número y revisión propios (`25007-ME-PI-0901-00NN` Rev 1), distintos de los que el submittal declara. Un comentario de ADASA sobre "la lámina 11 del Rev C" no tiene contraparte en el sistema de numeración con el que el taller trabaja, y la revisión de esos planos avanza por un carril que ADASA no ve.
3. **No está claro qué se está sometiendo a aprobación.** Si ADASA responde Código 1 sobre `P22-DWG-09-005-004` Rev C, aprueba un documento de cuatro páginas; las otras dieciocho quedarían aprobadas de hecho sin haberlo sido de derecho. Esa ambigüedad hay que cerrarla en el transmittal.
4. **Toca directo la inspección del 13 y 14 de agosto.** Fuente: `AQ-QAM-F027 Inspection Request (003)`, en el repositorio desde el 05-Ago, que declara *"9.00am - 5.00pm 13 Aug 2026 and 14 Aug 2026"* con alcance *"1-HP piping pressure test / 2- Painting preparation inspection"*. Supera a la minuta del 04-Ago, que decía *"Two days, Aug 12 and 13. Hydro test for low pressure and high-pressure piping. Structure frame surface preparation"*. **Dos cosas cambiaron, no una:** la fecha corrió un día y el alcance se recortó — desaparece la hidrostática de baja presión y no aparece la del RO Vessel, ambas exigidas por la NT-002, Sección 3.2 como puntos de Witness y de Hold. La solicitud `AQ-QAM-F027` declara como planos de referencia `P22-DWG-09-005-003 / P22-DWG-09-005-004`, pero el taller ejecuta contra los `25007-ME-PI-*`. El inspector de Bureau Veritas testificaría la prueba de presión de la cañería HP contra un plano cuya correspondencia con el aprobado no está establecida.

**Cadena de fechas:** revisión `1` de los planos de taller el 20-07-2026 · firmas de liberación a fabricación el 23-07-2026 · portada del documento controlado el 27-07-2026 · emisión del submittal el 05-08-2026 · inspección solicitada para el 13 y 14-08-2026.

> **Antes de redactar:** esto se levanta como **hallazgo de control documental y de secuencia**, no como acusación de que los spools estén mal fabricados. No se ha revisado la ingeniería de esos planos y no hay base para afirmar que su contenido sea incorrecto. Lo que se objeta es que se liberaron a taller sin pasar por el ciclo de aprobación y que llegan mezclados dentro de otro documento.

---

## 3. Cruce de TAG de línea: modelo, plano y Line List aprobada

Hecho por script sobre las tres fuentes. La **Line List `P22-LI-09-009-003` Rev 0** (entrega E67, aprobada) es la línea base.

| Fuente | TAG únicos | Colisiones de correlativo |
|---|---|---|
| Line List Rev 0 (aprobada) | 34 | **ninguna** |
| Modelo 3D Rev A | 38 | **4** |
| Piping Layout Rev C (capa de texto) | 28 | **2** |

**En el modelo y no en la Line List aprobada (6):** `AS-PVC-DN100-09-026` · `AS-PVC-DN25-09-033` · `CP-PVC-DN80-09-042` · `CP-SSD-DN100-09-015` · `CP-SSD-DN65-09-044` · `RD-PVC-DN15-09-001`

**En la Line List y no en el modelo (2):** `CP-PVC-DN50-09-042` · `DA-PVC-DN65-09-016`

**Colisiones de correlativo** (un mismo número de línea usado por dos líneas distintas):

| Documento | Correlativo | Líneas en conflicto |
|---|---|---|
| Modelo 3D | 09-001 | `DA-PVC-DN100-09-001` vs `RD-PVC-DN15-09-001` |
| Modelo 3D | **09-015** | `CP-SSD-DN100-09-015` vs `CP-SSD-DN80-09-015` — mismo servicio y material, **distinto diámetro** |
| Modelo 3D | 09-026 | `AS-PVC-DN100-09-026` vs `CP-PVC-DN100-09-026` |
| Modelo 3D | **09-044** | `CP-SSD-DN65-09-044` vs `CP-SSD-DN80-09-044` — mismo servicio y material, **distinto diámetro** |
| Piping Layout Rev C | 09-001 | `DA-PVC-DN100-09-001` vs `RD-PVC-DN15-09-001` |
| Piping Layout Rev C | 09-019 | `CP-PVC-DN80-09-019` vs `PE-PVC-DN80-09-019` |

**Discrepancia de diámetro sobre el mismo correlativo entre documentos:** la Line List aprobada dice `CP-PVC-DN50-09-042`; el modelo dice `CP-PVC-DN80-09-042`.

Que la Line List aprobada no tenga ninguna colisión y el plano y el modelo sí, indica que la divergencia se introdujo aguas abajo de la lista.

> **Dirección de inferencia válida.** Que un TAG **aparezca** en el plano o el modelo es evidencia positiva y se puede afirmar. Que **no aparezca** en el plano no es evidencia de ausencia: la extracción lee la capa de texto de láminas A1 y pierde rótulos vectorizados. No fundar observaciones en una ausencia del plano.

---

## 4. El modelo 3D como entregable controlado

Extraído con Navisworks Manage 2026 mediante plugin in-process. 7.558 líneas en `25007-0070/md/P22-DWG-09-005-007_3D-Model_RevA_extraccion.md`.

| Qué se verificó | Resultado |
|---|---|
| Título interno del documento | `V14 Taltal.nwd` — **no lleva el código `P22-DWG-09-005-007` ni el índice de revisión** |
| Archivo original | `C:\Users\AhmadHaffizieBinRosl\BW Water\...\14.3 3D Model\01 Navis\V14 Taltal.nwd` — ruta personal, versión interna "V14" |
| Propiedades de publicación del NWD | **Ausentes.** Sin autor, sin fecha de publicación, sin destinatario, sin control de caducidad |
| Conjuntos de selección | **Ninguno.** No declara estructura por disciplina ni por sistema |
| Viewpoints guardados | **Ninguno.** No propone puntos de revisión |
| Composición | Un único DWG agregado, `TALTAL CONTAINER.dwg`. Unidades en milímetros |
| Tipo de objetos | Capas de AutoCAD con entidades `3D Solid` **sin nombre**. No hay objetos tipados de tubería, válvula o equipo con propiedades de ingeniería |

Las capas **sí** llevan los TAG de línea, y de ahí sale el cruce de la Sección 3. El modelo es por tanto verificable en su contenido de líneas, pero no en diámetros, materiales ni especificaciones, porque esos datos no están en propiedades sino implícitos en el nombre de la capa.

Rótulos con error de tipeo en capas: `FIBRATION PAD` (por *vibration*) y `ADDITIONAL SRUCTURE - INSTRUMENT PANEL` (por *structure*).

---

## 5. Datasheet del presostato diferencial Rev B: qué cambió y por qué

La Rev A quedó en **Código 1 — Approved** en el TM N8, sin observaciones. La hoja de respuesta a comentarios de la Rev B declara el motivo del cambio:

> *"Vendor/supplier could not pass the quality test of using Monel material for wetted part. Therefore diaphragm seal is added for alternative option. Attached revised datasheet Rev.B with added diaphragm seal information for review."*

Es decir: **cambio de material en las partes mojadas** de un instrumento previamente aprobado. TAG `DPS-09-001`, proveedor Ashcroft, hoja de P&ID `P22-DWG-09-009-002-P8`, fechado 21-Jul-2026.

Configuración declarada en la Rev B:

| Fila | Parámetro | Valor |
|---|---|---|
| 20 | Material - Wetted Part | **SS316L** |
| 21 | Material - Actuator Seal | Viton |
| 32 | Diaphragm Seal - Material Upper Part | SS316L |
| 33 | Diaphragm Seal - **Material Lower Part (Wetted Part)** | **PVC** |
| 34 | Diaphragm Seal - Material Diaphragm | **PTFE** |
| 41 | Material - Process Connection | SS316L |
| 42 | Material - Capillary | **SS304** |

Puntos a resolver en la revisión:

- **Dos declaraciones contradictorias de qué está mojado.** Con sello de diafragma instalado, el cuerpo del presostato ya no toca el proceso: ve el fluido de llenado. La fila 20 sigue declarando SS316L como parte mojada mientras la fila 33 declara PVC. El documento debe declarar una sola.
- **El fluido de llenado del sello no aparece declarado.** Un sistema con sello de diafragma lo necesita, con su rango de temperatura y su compatibilidad.
- **Capilar en SS304.** Aunque no sea parte mojada, queda expuesto a la atmósfera de una planta desaladora. Contrastar con el criterio de materiales del proyecto.
- La numeración de filas repite el número 8 en dos parámetros distintos (temperatura ambiente y presión de operación).

Nota de contexto: el par Monel contra sello Superduplex 2507 ya apareció en la auditoría de la cotización de repuestos, donde BW Water ofreció manómetros Monel frente a los Wika con sello Superduplex 2507 instalados. Conviene revisar ambos frentes con el mismo criterio de material.

---

## 6. Estado de la extracción

Todo completo. Piping Layout en modo drawing: **22 de 22 láminas**, 171 archivos, 134 MB, con `full.png`, seis tiles y `titleblock.png` por lámina. Modelo 3D, datasheet, formulario de submittal y solicitud de inspección de Bureau Veritas: extraídos.

## 7. Verificación de la salida del workflow

El workflow de cinco lentes devolvió **62 observaciones, 62 confirmadas y 0 descartadas**. Ese cero es en sí una señal: la etapa adversarial no filtró nada. Funcionó como **editor**, no como filtro — sus razones de verificación corrigen errores de redacción dentro de las observaciones, pero no descartó ninguna. Por eso el contraste contra fuente primaria se hizo aquí.

### Confirmado leyendo la fuente primaria

| Afirmación del workflow | Verificación |
|---|---|
| ET fija altura máxima de contenedor en 2,8 m | **Correcto.** ET línea 704: *"Las dimensiones máximas del contenedor serán de 13 metros de largo por 2,5 metros de ancho, y 2.8 metros de altura"*. La lámina 2 acota 2896 mm |
| ET Sección 5.2.2 exige super duplex en alta presión | **Correcto.** ET línea 838: *"Para las cañerías de alta presión (hasta 120 bar) se utilizará acero inoxidable super duplex"*, con A790 S32750 PREN>40, SCH 80S y bridas clase 900 |
| Presiones de diseño y prueba de las ocho líneas SSD citadas | **Correctas las diez**, leídas de la Line List Rev 0: 003 60/90 · 004 80/120 · 005 80/120 · 006 90/135 · 014 80/120 · 015 90/135 · 044 80/120 · 045 90/135 barG |
| Las líneas PVC del lado CIP están rateadas a baja presión | **Correcto.** `CP-PVC-DN100-09-017` y `-024`: diseño 5 barG, prueba 7,5 barG. El contraste con los 80–90 barG de las líneas SSD que las alimentan es real |
| Half coupling ANSI 150# austenítico en las tomas de instrumento | **Correcto, y el workflow se quedó corto.** Aparece en **7 láminas** (11, 12, 14, 16, 17, 18 y 20), no en 4: `HALF COUPLING, ANSI 150# SCRD, A182GR.F316L, SCH10S` y `A182GR.F304, PExFPT` |
| Es inconsistencia y no criterio de diseño | **Correcto.** Las mismas láminas resuelven otras derivaciones de 1/2" con `SOCKOLET SCH80, Super Duplex, ASTM A182 F53 UNS S32750` |
| DP Switch: temperatura de proceso 0 a 65 °C y sello de 200 psi | **Correcto.** Fila 19 del datasheet: `Process Temperature 0 to 65 °C`. Fila 31: `Max. Pressure Range 200 psi` |
| ET Sección 5.1.5 fija 10 bar para el filtro cartucho | **Correcto.** ET línea 588: *"Presión de trabajo máxima 10 bar"*, dentro de 5.1.5 Filtros cartucho, que es el equipo a través del cual mide este presostato |

### Corregido antes de usar

- **`layout` OBS-02 tiene mal los números.** Dice "17 páginas", "trece láminas" y "`-0006` a `-0014`". El PDF tiene **22 páginas**, las láminas de taller son **17** y los planos **11**, de `-0006` a `-0016`. La causa está identificada: el workflow arrancó mientras la extracción del plano seguía corriendo, y esa lente leyó 17 de 22 láminas. **Se usan las cifras de la Sección 2 de este documento, no las suyas.**
- **`tuberias` OBS-01** dice 4 láminas y 6 piezas; son **7 láminas**.
- **`carry-forward` OBS-01** afirmaba que todos los demás equipos de la lámina llevan TAG. Es falso: las dos unidades de aire acondicionado tampoco. La propia verificación adversarial lo detectó y lo dejó anotado; hay que aplicar esa corrección al redactar.

### No confirmado — no se emite como está

- **`layout` OBS-01, TAG `FIL-09-001` duplicado.** El TAG aparece dos veces en la lámina 2, mientras el resto de los equipos aparece una sola vez, lo que es un indicio. Pero **no logré confirmar visualmente** que rotule dos filtros distintos: la lámina está rotada 270 grados y los recortes construidos desde las coordenadas de búsqueda no caen sobre el rótulo. La afirmación de que uno es el filtro RO y el otro el del CIP queda sin verificar.
  **Cómo emitirlo:** como solicitud de aclaración —confirmar qué TAG lleva cada filtro cartucho y corregir si corresponde— y no como defecto de duplicación afirmado. Si se quiere emitir como defecto, hay que abrir la lámina y verlo.

---

## 8. Qué queda por verificar antes de emitir

- **Sellos lámina por lámina.** Solo se confirmó visualmente la 11. Hay que recorrer los 22 `titleblock.png` y anotar en cuáles aparece `FOR CONSTRUCTION` y `SHOP FABRICATION`, porque el número exacto va en la observación.
- **Qué es la lámina 22**, A4 apaisada y sin numeración de BW Water.
- **Servicio de `DPS-09-001`** en la hoja `P22-DWG-09-009-002-P8` del P&ID, para juzgar si PVC y PTFE son adecuados y si el capilar en SS304 tiene problema en esa ubicación.
- **Fluido de llenado del sello de diafragma**, que no aparece en el datasheet.
- **Las cuatro NOTE del TM N15** sobre las láminas 2 a 4, que son las únicas que pertenecen al documento controlado. Ojo: la Rev B tenía las cuatro NOTE abiertas y el documento sigue siendo de cuatro páginas, de modo que el cierre debe verse en esas tres láminas de layout.
