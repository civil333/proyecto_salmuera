---
titulo: ENTREGA 78 — libro mayor de comentarios y su cierre
codigo: submittal 25007-0078
fecha: 2026-08-17
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 78 (submittal `25007-0078`) — libro mayor de comentarios

**Recibida el lunes 17-Ago-2026.** Dos planos. El Submittal Form pide respuesta el jueves 20-Ago; el plazo de ADASA son siete días hábiles desde la recepción per la Cláusula 37.2 de la BAE, es decir el **miércoles 26-Ago-2026**.

| # | Documento | Código | Rev | Sub. For | Responde a | Veredicto previo |
|---|---|---|---|---|---|---|
| 1 | Equipment Layout | `P22-DWG-09-005-003` | D | IFA | TM N22 OBS-01/02/03 | 3 — To be revised |
| 2 | Process Flow Diagram | `P22-DWG-09-009-01` | 0 | IFA | nada abierto | 1 — Approved (Rev B, TM N3) |

Las dos naturalezas son distintas y se revisan distinto. El Equipment Layout viene de un **Código 3**, así que el documento entero está en ciclo y se revisa a fondo. El Process Flow Diagram viene de un **Código 1** y llega en **Rev 0**: se revisa solo por diferencia contra lo aprobado, sin comentarios nuevos.

---

## Parte A — Equipment Layout `P22-DWG-09-005-003` Rev D

Cajetín de la Rev D fechado **AUG.02.26**, sometida el 17-Ago: quince días. La hoja consolidada de comentarios reproduce las tres OBS del TM N22 y declara las tres cerradas.

### OBS-01 — filtro de cartucho RO vertical: CERRADA, verificada por render

**Verificado por render a 500 dpi, no por texto.** En la planta, el filtro `FIL-09-001` al que apunta la llamada 2 se dibuja como **circunferencia con base cuadrada de apoyo**, que es la firma en planta de un recipiente vertical; un filtro horizontal aparecería como rectángulo alargado. El filtro CIP `FIL-09-002`, ítem 11, se dibuja igual.

Cierra el punto que llevaba tres vueltas y que arrastraba el cambio de horizontal a vertical de la NT-001. El plano queda consistente con el Datasheet Rev E del propio filtro.

> La lámina trae **solo vista en planta**. El registro del proyecto anota que la Rev B tenía vistas de sección que confirmaban las puertas (peatonal, de acceso de equipos, de emergencia y corredera lateral). No se levanta: las puertas no son objeto de las tres OBS del TM N22 y el punto de la puerta corredera de la ET Sección 5.1.10 se sigue por su propia vía.

### OBS-02 — tabla de pesos de operación: CERRADA, y abre el conflicto de las dos tablas

**Lo que hizo.** Empotró la tabla en la lámina: 17 filas con `ID / TAG / DESCRIPTION / PID / OPERATING WEIGHT`. Es la primera de las dos vías que el TM N22 ofreció.

**El conflicto.** El plano `Civil and Loading Layout` Rev B del submittal `25007-0076`, recibido cuatro días antes y también emitido para aprobación, trae su propia tabla de cargas. Cotejadas fila por fila, **las dos coinciden en todo salvo una**:

| Fila | Ítem | Civil Rev B | Equipment Layout Rev D | Δ |
|---|---|---|---|---|
| 14 | Panel de control | `LOCAL CONTROL PANEL` — **800,0 kg** | `LCP PANEL AND INSTRUMENTATION` — **989,2 kg** | **+189,2** |

Todas las demás filas comunes son idénticas: mezclador 13,0 · filtro RO 470,0 · bomba de alta 1.406,1 · turbochargers 30,0 cada uno · recipientes a presión 4.160,0 (el civil los agrupa, el layout los parte en 2.496,0 más 1.664,0) · estanque CIP 10.470,0 · calentador 25,0 · bomba CIP 180,0 · filtro CIP 270,0 · estanque de dispersante 517,5 · skid de dosificación 100,0 · panel del calentador 50,0 · aire acondicionado 140,0.

**El incremento no se puede reconciliar por inspección.** La fila cambió de nombre y ahora dice incluir la instrumentación, pero la fila de instrumentos del plano civil vale **182,9 kg** y la diferencia es de **189,2**: no calzan. Y la fila 17 del Equipment Layout, `INSTRUMENT PANELS`, **va sin peso**, de modo que no se sabe si esos paneles están contabilizados en la fila 14, en la 17 vacía, o dos veces.

**Las dos tablas no son equivalentes en alcance.** El civil trae 23 filas con peso seco y de operación por separado, e incluye contenedor 3.700, válvulas de PVC 60, cañerías de PVC 490, válvulas de super dúplex 245, cañerías de super dúplex 1.090, instrumentos 182,9 y soportes de cañería 6.100. El Equipment Layout trae 17 y ninguna de esas siete.

**Decisión de ADASA (17-Ago): el plano civil es la fuente única de pesos.** Se ejerce por escrito la segunda vía que el propio TM N22 ofreció (*"or obtain ADASA's written acceptance to keep it only in the Civil and Loading drawing"*), porque es el documento que dimensiona la fundación, el que distingue seco de operación y el que alimenta la Sección 6.4 de la BL Montaje. El Equipment Layout cita ese plano en vez de repetir la tabla. **No se imputa falta por haberla empotrado**: hizo una de las dos cosas que se le pidieron.

### OBS-03 — rótulo del panel principal: PARCIAL

**Lo que cerró.** La fila 14 rotula el panel y la llamada 14 lo identifica en la planta, de modo que la leyenda ya no lo omite. El campo de revisión del cajetín es legible: `REV.: D`, con el bloque de revisiones A a D fechado.

**Lo que no cerró.** El TM N22 pidió rotularlo **y unificar su nombre y su posición** entre los dos planos. El `Grounding Point & Power Panel Location Layout` Rev F nombra al panel **`P22-LCP-01`**, "LCP / Main Switchboard", y su hoja de comentarios registra la instrucción de ADASA de prepararlo **sobre el Equipment Layout Rev B**, manteniendo el panel y los puntos de tierra en las posiciones de ese layout aceptado. El Equipment Layout Rev D lo rotula `LCP PANEL AND INSTRUMENTATION` con la columna TAG en `N/A`.

Se pide unificar nombre y tag con los del Grounding Layout Rev F, y **confirmar que la posición del panel no cambió** respecto de la Rev B sobre la que se preparó ese plano, que va dos revisiones atrás.

### Contenido nuevo — el TAG del mezclador estático es el que BW Water descartó por escrito

La fila 1 de la tabla rotula el mezclador **`MZE-09-009`**. El TAG vinculante es **`MZE-09-001`**, y lo fijó BW Water por escrito: la hoja de comentarios de la `Equipment List` Rev B responde a una observación de ADASA sobre esta misma discrepancia con *"BW confirms the following: 1. Static mixer tag is MZE-09-001"*. La fila 1 de esa Equipment List usa `MZE-09-001`, y el Process Flow Diagram de **este mismo submittal** también.

Conteo determinista sobre el set: `MZE-09-001` aparece dos veces en el cuerpo del diagrama de flujo; `MZE-09-009` aparece **cero** veces en cuerpo y una sola en la fila de cuadro del Equipment Layout.

> El plano civil `-001` **también** rotula `MZE-09-009`, y ya lo hacía en la **Rev A que ADASA aprobó en Código 2 en el TM N16**. Por eso el punto no se levanta contra el plano civil: hacerlo reabriría una aprobación propia. Se resuelve declarando el TAG vinculante y exigiendo su adopción en la Rev 0 de los dos planos, como reconciliación y no como incumplimiento.

### Contenido nuevo — el peso del estanque CIP contra la capacidad que el proveedor confirmó

La fila 8 declara **10.470 kg** de operación para `TK-09-001`. La `Equipment List` Rev B fija Dayamas DYM 6800, HDPE, capacidad efectiva **6,1 m³**, y **BW Water lo confirmó por escrito** en la hoja de comentarios de esa lista: *"CIP tank effective capacity is 6.1 m3"*. El TM N18 cerró además la NOTE-01 del TM N13 resolviendo 6,8 m³ geométricos contra 6,1 m³ efectivos utilizables.

Con 270 kg de tara, el peso en operación es del orden de **6.400 kg**, y aun lleno al borde geométrico no pasa de 7.100. El plano exige 10,2 toneladas de líquido en un estanque que no las contiene. El valor viene sin cambios desde la Rev A del plano civil.

**No compromete la seguridad, compromete el costo:** ADASA paga la fundación que ese número dimensiona, y la BL Montaje cotiza sobre él. Se resuelve con el valor vinculante declarado por ADASA sobre los dos planos.

### Control documental

La hoja consolidada de comentarios está fechada **3-Jul-2026**, un mes antes de la Rev D que comenta (AUG.02.26). Es el mismo defecto del plano civil de la E76. Se registra y no se emite: no induce a error en obra y la emisión de Rev 0 lo corrige por sí sola.

---

## Parte B — Process Flow Diagram `P22-DWG-09-009-01` Rev 0

**Alcance: solo diferencia contra la Rev B aprobada en Código 1 en el TM N3.** No se introducen comentarios nuevos sobre contenido que ADASA aprobó y no observó entonces.

### La diferencia, cotejada dato por dato

La Rev B es un plano **escaneado** y su capa de texto viene de OCR, de modo que un diff de texto crudo produce ruido. Se cotejaron los valores uno por uno:

| Dato | Rev B (aprobada) | Rev 0 | Estado |
|---|---|---|---|
| **Bomba de alta** | 49 m³/h @ **49,4 bar** | 49 m³/h @ **46,9 bar** | **CAMBIÓ** |
| Estanque CIP | 6,1 m³ | 6,1 m³ | igual |
| Estanque de dispersante | 0,25 m³ | 0,25 m³ | igual |
| Dosificadoras | 2,3 LPH | 2,3 LPH | igual |
| Bomba CIP | 57 m³/h | 57 m³/h | igual |
| RO 1ª y 2ª etapa | 13 y 8 m³/h | 13 y 8 m³/h | igual |
| Calentador CIP | 20 kW | 20 kW | igual |
| Mezclador estático | `MZE-09-001` | `MZE-09-001` | igual |
| Materiales | SDSS 2507, SS316, FRP, HDPE, PVC | idénticos | igual |

**El único cambio alinea el plano con el datasheet aprobado.** El `Datasheet of RO HP Feed Pump` `P22-ET-09-009-002` **Rev D**, aprobado en Código 2 en el TM N11, declara `Differential Head — 46,9 bar` (y presión de descarga 48,9 bar con 2,0 bar de succión). La Rev 0 corrigió los 49,4 bar de la Rev B al valor del datasheet. Es una corrección, no una desviación.

### Dos cosas que NO se levantan, y por qué

- **El código del documento.** El Rev 0 se identifica como `P22-DWG-09-009-01`, con correlativo de dos dígitos, mientras el Master Register lo lleva como `P22-DWG-09-009-001`. **La Rev B que ADASA aprobó en Código 1 ya decía `P22-DWG-09-009-01`** en su portada y en su cajetín. Es contenido aprobado y no se reabre. Lo que corresponde es **corregir la clave del Master Register de ADASA**, que es registro propio.
- **La portada dice "PD Tattal".** También venía así en la Rev B aprobada. Misma categoría.

### El estanque de dispersante: la discrepancia que NO aplica acá

La Rev 0 declara 0,25 m³ y la `Equipment List` Rev B fija 0,27 m³ efectivos, confirmados por BW Water. **Pero la Rev B del diagrama de flujo ya declaraba 0,25 y ADASA la aprobó en Código 1**, y la reconciliación de los 0,27 se resolvió entre la Equipment List y el P&ID, que son otros documentos. Levantarlo ahora sobre este plano sería introducir un comentario nuevo sobre una Rev 0. **Se registra internamente y no se emite.**

---

## Disposición propuesta

| Documento | Rev | Código | Motivo en una línea |
|---|---|---|---|
| Equipment Layout `-003` | D | **2** | Cierra las tres OBS del TM N22, la del filtro verificada por render; lo que queda es reconciliar la tabla de pesos con el plano civil, el TAG del mezclador y el nombre del panel, todo incorporable al emitir Rev 0 |
| Process Flow Diagram `-009-01` | 0 | **1** | Emite lo aprobado en la Rev B con un solo cambio, y ese cambio corrige la presión de la bomba al valor del datasheet aprobado |

**Por qué el Equipment Layout es 2 y no 3.** El documento cerró los tres puntos por los que fue devuelto, incluido el que llevaba tres vueltas. Lo que queda es alinearlo con documentos aprobados, y la regla del proyecto es que alinear a otro documento es Código 2; el 3 se reserva para cuando el contenido propio está mal de raíz. Ninguna de las correcciones exige rehacer el plano.

**Por qué el diagrama de flujo es 1 y no 2.** Sobre una Rev 0 el Código 2 no tiene mecanismo: el veredicto es 1 o 3. Emite lo aprobado, así que es 1, y no lleva PDF anotado.

---

## Triaje: por qué cada punto queda dentro o fuera

### ADASA fue clara y BW Water cumplió

| Punto | Qué se pidió | Qué hizo | Decisión |
|---|---|---|---|
| Filtro vertical | Redibujarlo vertical con huella, acceso de operador y 2.000 mm de altura libre | Lo redibujó vertical | **Cierra.** Se reconoce en el Status, no se pide nada más |
| Tabla de pesos | Empotrarla, **o** aceptación escrita de ADASA para dejarla solo en el plano civil | Empotró la tabla | **Cierra por la vía que él eligió.** ADASA ejerce ahora la otra vía por coherencia de fuente única, sin imputarle falta |

### ADASA no fue suficientemente clara

| Punto | Qué se pidió | Qué hizo | Decisión |
|---|---|---|---|
| Rótulo del panel | "Label the main panel and unify its name and position between both drawings" | Lo rotuló con un nombre propio y sin tag | **Se mantiene la mitad no cumplida**, con el nombre y el tag del Grounding Layout Rev F escritos, para que no quede a interpretación |

### ADASA estaría exigiendo más de lo que pidió

| Punto | Situación | Decisión |
|---|---|---|
| Ausencia de vistas de sección en la Rev D | No es objeto de las tres OBS del TM N22 | **Se saca** |
| `MZE-09-009` en el plano civil `-001` | Ya estaba en la Rev A aprobada en Código 2 | **No se levanta contra el plano civil.** Se declara el TAG vinculante para los dos |
| 0,25 contra 0,27 m³ del estanque de dispersante en el diagrama de flujo | La Rev B aprobada ya decía 0,25 | **Se saca.** Comentario nuevo sobre una Rev 0 |
| Código de dos dígitos y "PD Tattal" del diagrama de flujo | Los dos venían en la Rev B aprobada | **Se sacan.** Lo que se corrige es la clave del registro de ADASA |
| Fecha de la hoja de comentarios anterior a la revisión que comenta | Defecto documental que la Rev 0 corrige por sí sola | **Se saca** |

### Lo que este triaje puso sobre la mesa y no estaba en la entrega

Que las dos tablas de pesos vivas divergen en una sola fila, y que esa fila es la del panel cuyo peso ya había saltado de 350 a 800 kg por el cambio de envolvente a inoxidable del RFI-002. Ahora aparece un tercer valor, 989,2 kg, cuatro días después del segundo. Sin el cruce entre las dos entregas el conflicto no se veía: cada plano es internamente coherente.

---

## Re-alcance del 17-Ago-2026 — solo cierre de comentarios previos

**Criterio del usuario, aplicado a todo el análisis:** la revisión se limita a **si los comentarios previos están cerrados**. No se introducen observaciones nuevas. Para esta entrega el cambio es grande, porque las dos disposiciones suben a Código 1.

### Equipment Layout Rev D — de Código 2 a **Código 1**

Las tres observaciones del TM N22 **cierran**, y la tercera se resolvió al verificar la fuente en vez de asumir:

- **OBS-01** filtro de cartucho RO vertical: cerrada, verificada por render a 500 dpi.
- **OBS-02** tabla de pesos de operación: cerrada, empotrada en la lámina. Era una de las dos vías que el TM N22 ofreció y el proveedor eligió esa.
- **OBS-03** rótulo del panel: 🔴 **corrección.** Este ledger la dejaba a medias porque el nombre no coincidía con `P22-LCP-01`. Ese código sale del **texto de un comentario de ADASA** en la hoja del Grounding Layout, no del rótulo del plano: la lámina del `P22-DWG-09-007-003` Rev F identifica el panel como **`LCP`**, mismo identificador que la fila 14 del Equipment Layout. La respuesta de BW Water, *"Main panel has been labelled correctly and consistent with Grounding Layout Drawing Rev F"*, es exacta. **Cerrada.** Exigir la columna TAG habría sido comentario nuevo.

**Se retira todo lo demás:** la tabla de pesos duplicada y la decisión de fuente única, el peso del panel de control (800 contra 989,2 kg), la fila 17 sin peso, el TAG del mezclador estático y el peso del estanque CIP. Queda registrado arriba. Los pesos y las fundaciones son materia de la conversación con L&A (`INT-11` e `INT-10`).

### Process Flow Diagram Rev 0 — **Código 1**, sin cambios

Ya estaba dispuesto así. Se confirma: emite lo aprobado en la Rev B con un solo cambio, y ese cambio corrige la presión de la bomba de alta al valor del datasheet Rev D. El código de dos dígitos y el "PD Tattal" venían en la Rev B aprobada y no se levantan; la clave del Master Register se alineó al código del documento.

**Consecuencia para la entrega: ningún PDF anotado.** Los dos scripts y sus `CC_ADASA` quedan en `REVISIONES/TRANSMITTALES/P22-TM-09-000-033-0/_analisis_no_anotado/` como traza interna.
