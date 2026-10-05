---
titulo: Ledger de revisión — ENTREGA 99 (submittal 25007-0099), addendum de izaje y plano del yugo
fecha: 2026-10-05
estado: INTERNO
type: ledger
project: salmuera-taltal
second_brain: skip
---

# Ledger de revisión — ENTREGA 99

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0099`, emitido el martes 29-Sep-2026 a las 04:32 por Fitri Indriyani. Devolución pedida el viernes 2-Oct, tres días corridos. El plazo de la Cláusula 37.2 vence el jueves 8-Oct. El formulario lista **un solo documento**: `P22-CD-09-005-003` Rev A, *UHPRO Structural Calculation Report - Addendum*, `Sub. For` **IFA**. El archivo del formulario se llama `Submittal Form_25007-0098.pdf`, pero por dentro dice 0099. Es un defecto de nombre de archivo y no se emite.

**Contra qué se revisa.** Es la primera emisión formal del paquete de izaje. El estándar es lo que ADASA ya pidió, no una lectura nueva:

- la ET `P22-ET-09-000-001-0`, Sección 7, pág. 29, dentro del Manual de montaje: *"Memoria de Calculo para el izaje del módulo"*, *"Plano de izaje del módulo indicando los puntos de izaje, indicando claramente pesos"* y *"Plano y diseño del yugo de Izaje para el módulo"*;
- el Criterio de Diseño `P22-CD-09-005-003` Rev 0, sección F, pág. 10: FS 2,0 y 5 % de carga lateral fuera del plano para el padeye;
- los correos de ADASA del 11-Sep (verificación local del punto de izaje en los esquineros ISO, validada por el profesional) y del **15-Sep** (`CORREOS/Septiembre 2026/2026-09-15/`): la revisión de Thomas Engineers debe cubrir el paquete completo y **el plano del yugo tiene que ser de fabricación** (literal: *"The yoke drawing must be one we can fabricate from: dimensions, connections and welds, sling attachment points and the connection to the top corner fittings."*). El diseño del marco se funda en la ET Sección 7, pág. 29 ("Plano y diseño del yugo") y en los correos del 10 y del 11-Sep, no en el del 15. Plazo fijado: jueves 17-Sep, vencido sin entrega (`PRG-49`).

En la reunión del 16-Sep (minuta automática, no oponible), BW Water dijo que los planos de izaje con el yugo se terminaban el viernes 18 y llegaban el 21 o el 22. El plano que vino tiene fecha 21-Sep y llegó el 29.

## Lo que trae el archivo (13 páginas, verificado por render)

| Página | Contenido | Evidencia |
|---|---|---|
| 1 | Portada ADASA: `ADASACode: P22-CD-09-005-003`, Rev A, **22 Sep 26**, "Page 1 of 13". Firmas: Aulem prepara, JFR/NOP revisan, LPL chequea, MA aprueba. **Ninguna es del profesional chileno** | texto extraído |
| 2 | Portada Aulem `P2616-STR-CAL-001-IFR-RB`, **Rev A, 29-JUN-2026, FOR APPROVAL** | `render/addendum_A_p02_portada_aulem.png` |
| 3 a 12 | *Padeye Design Calculation*, "Page 2 of 11" a "Page 11 of 11". Las páginas son imagen, sin capa de texto | `render/addendum_A_p03_cargas.png` |
| 7 | La cabecera de esta sola página dice **"REV. B DATE: 18-SEP-2026"** | `render/addendum_A_p07_cabecera_revB.png` |
| 13 | Plano A1 **`P22-DWG-09-005-019` Rev A, "GA of Module Lifting from Top", ISSUED FOR APPROVAL, SEP.21.26, hoja 1 de 3** | `render/dwg019_A_cajetin_1de3.png` |

### El cálculo de las orejas (páginas 3 a 12)

- **Carga de diseño** = máx(WLL del grillete Crosby, 9,5 t = 93,16 kN; tensión crítica en STAAD, 92,59 kN) = **93,16 kN**. Lateral fuera del plano = 5 % = 4,66 kN. A36 (Fy 250, Fu 400 MPa), electrodo E70XX.
- **Lug A** (base de 160 mm, tiro vertical) y **Lug B** (base de 340 mm con cartela, tiro a 45°): t = 15 mm, placas de refuerzo del ojo (cheek plates) de 10 mm, agujero de 35 mm, Dc = 120 mm, R = 80 mm, h = 90 mm, filete de base de 8 mm, filete de cheek plate de 6 mm.
- Chequeos de AISC 360-05 (ajuste del grillete, distancias al borde, rotura por tracción y por corte, aplastamiento, fluencia, flexión combinada, soldaduras, carga lateral) y ASME BTH-1-2020 C-3.3.1 para la soldadura de la cheek plate. **Utilización máxima 0,8694**, aplastamiento sobre la placa principal sola.
- **El 5 % lateral está considerado** (sección 11, páginas 10 a 12 del PDF, que el cálculo numera 9 a 11 de 11).
- **Lo que este cálculo NO trae:** ningún chequeo de los perfiles W10x49 del marco ni de sus uniones; ningún peso de izaje (la versión del 14-Sep tenía 10.278,74 kg vacío y 12.482,35 kg en operación, y esta no los repite); ninguna verificación de los esquineros ISO.

**Fuera de alcance, no se emite.** La fluencia y la flexión usan λ = 1,67 y no el FS 2,0 del Criterio. Con 2,0 todas las razones siguen bajo 0,65. Además, el plano dibuja filetes de 13 mm en la base y de 8 mm en la cheek plate, mayores que los 8 y 6 mm del cálculo, del lado conservador. Ninguno de los dos cambia algo físico.

### El plano del yugo (página 13)

| Lo pedido en el correo del 15-Sep | Lo que trae la hoja 1 de 3 | Estado |
|---|---|---|
| Plano de fabricación del yugo | **Arreglo general**: planta, frontal, lateral, isométrica, detalle de Lug A y Lug B, tabla *Steel Structure* de 8 ítems (2 W10x49 de 12.776, 2 W10x49 de 2.271, 4 esquineros ISO 1161, 4 eslingas, 4 Lug A, 4 Lug B, 12 grilletes Crosby G-209 WLL 9,5 t, 4 eslingas) | **Parcial** |
| Dimensiones | Largo 12.776 y vano 12.014, CG a 5.500 y 6.514, y a 909 y 1.371, gancho a 6.604 aprox., marco a 1.500 sobre el techo, ángulos de 45° y 50° en el frontal | Cerrado en la hoja 1 |
| Uniones y soldaduras | Solo las de las orejas. **Las uniones W10x49 con W10x49 del marco no tienen detalle**, y tampoco la posición de las orejas sobre el ala ni rigidizadores | **No cerrado** |
| Material | Solo en el cálculo (A36, E70XX). **La tabla del plano no tiene columna de material** | **No cerrado** |
| Puntos de eslinga en el marco | Lug A abajo y Lug B arriba, en los extremos | Cerrado |
| Conexión a los esquineros superiores | Grillete y eslinga hasta el esquinero. **La nota 2 dice "CHECK COMPATIBILITY WITH CONTAINER LIFTING ACCESSORY"**, de modo que el accesorio en el esquinero queda sin definir. La verificación local del esquinero, pedida el 11 y el 15-Sep, no está | **No cerrado** |
| Eslingas | Ítems 4 y 8 con guion en largo, **sin WLL ni largo** | **No cerrado** |
| Pesos (ET Sección 7, pág. 29) | **Ningún peso en la lámina** | **No cerrado** |
| Hojas 2 y 3 | **No recibidas**. El plano no figura en el formulario 25007-0099 | **No cerrado** |
| Revisión del profesional (correo del 15-Sep) | Ninguna firma de Thomas Engineers | No cerrado, va a la Sección 3 junto con el endoso |

Recortes: `render/dwg019_A_planta.png`, `render/dwg019_A_frontal_esquineros.png`, `render/dwg019_A_tabla_estructura.png` y `render/dwg019_A_detalle_orejas.png`.

## Disposición

**Dos documentos, los dos en Código 3.**

- **Plano del yugo `P22-DWG-09-005-019` Rev A: Código 3, reemitir como Rev B completo (hojas 1 a 3) y como documento propio.** Primero se revisó dentro del addendum sin código propio, porque no está en el formulario. Luis preguntó el 5-Oct por qué no veía el plano del yugo en el transmittal: escondido dentro del addendum, el reclamo no se veía. Pasó a tener subsección propia (2.1), fila en el Response Summary y PDF anotado aparte, extraído de la página 13.
- **Addendum `P22-CD-09-005-003` Rev A: Código 3, reemitir con código propio.** Con un código nuevo el índice de revisión se reinicia, así que no se le fija letra. Solo verifica las orejas, y faltan el diseño del marco y la verificación local de los esquineros.

**Reclamo al correo, pedido por Luis (5-Oct).** El transmittal cita **el correo de ADASA del 15 de septiembre de 2026**, asunto *"RE: TALTAL - Lifting package for the module and the scope of the structural review"*, como el pedido del plano de fabricación del yugo con fecha del 17-Sep, y el del 11-Sep para la verificación de los esquineros.

**Correcciones de la verificación adversarial del 5-Oct:**

- **Eslingas.** El 11-Sep ADASA dejó al contratista de izaje la selección de grúa, eslingas y grilletes, así que no se pide el WLL. Se pide la tensión de diseño por ramal y el largo, que fijan los ángulos de 45° y 50°.
- **Material del marco.** Se mantiene: la versión informal del 14-Sep declaraba los W10x49 en ASTM A36 y la Rev A formal lo perdió.
- **Plano como documento propio.** No se atribuye al correo del 15-Sep. Se funda en el formulario y en la ET Sección 7, pág. 29, que trata el plano y la memoria como entregables distintos.

## Comentarios de los CC_ADASA (IDs por posición final del cuadro)

**Plano del yugo** (`P22-DWG-09-005-019_A_GA_Module_Lifting_from_Top_CC_ADASA.pdf`):

| ID | Dónde quedó el cuadro | Texto |
|---|---|---|
| OBS-01 | arriba, junto al gancho | Sin pesos, y eslingas 4 y 8 sin tensión de diseño ni largo. Corregir: peso izado, peso del marco y de los aparejos, carga total en el gancho y tensión de diseño y largo por ramal (ET Sección 7, pág. 29) |
| OBS-02 | bajo la vista en planta, a la derecha de su título, con flecha al punto medio del larguero inferior | El marco no tiene viga intermedia; la torsión del marco durante el izaje y el pandeo de los largueros de 12.776 mm, comprimidos por las eslingas inclinadas, no están verificados. Corregir: al menos una viga intermedia a medio largo, con sus uniones y soldaduras, y verificar torsión, desangulación y pandeo en el addendum |
| OBS-03 | bajo la vista en planta, a la izquierda | Largueros de 12.776 mm sin empalme y sin detalle de las uniones de esquina. Corregir: detallar el empalme y las esquinas, con sus soldaduras |
| OBS-04 | sobre el bloque de revisiones | Hoja 1 de 3, fuera del formulario. Corregir: someterlo completo como documento propio; es el plano del yugo pedido para fabricación en el correo del 15-Sep |
| OBS-05 | junto a la tabla *Steel Structure* | W10x49 es laminado importado y ADASA fabrica el yugo en Chile. Corregir: cambiar cada miembro a su equivalente soldado nacional IN o HN, con calidad según NCh203 como exige el Criterio aprobado |
| OBS-06 | junto al cajetín | La nota 2 deja abierta la conexión en los esquineros. Corregir: mostrar cómo conecta cada eslinga a su esquinero (correo del 15-Sep) |

**Addendum** (`P22-CD-09-005-003_A_Lifting_Addendum_CC_ADASA.pdf`):

| ID | Página | Texto |
|---|---|---|
| OBS-01 | 1 | Código del Criterio de Diseño y tres marcas de revisión. Corregir: código propio, una revisión, una fecha |
| OBS-02 | 3 | Solo orejas, en ASD sobre la carga de trabajo del grillete y sin combinación declarada. Marco, empalmes y uniones sin verificar. Corregir: diseñarlos con la sección nacional IN o HN, declarando el método, con las combinaciones NCh3171 de la sección D del Criterio como mínimo y los factores 1,35D y 2,0D de su sección F |
| OBS-03 | 3 | Esquineros y postes de esquina sin verificar. Corregir: verificación local con FS 2,0 y 5 % lateral (correo del 11-Sep) |
| OBS-04 | 4, al pie (la página 3 no tiene zona libre) | El STAAD del marco se usa solo para la tensión crítica de eslinga (página 2 of 11); nada verifica la torsión, la desangulación ni el pandeo de los largueros comprimidos. Corregir: modelar el marco con al menos una viga intermedia a medio largo y demostrar torsión, desangulación y pandeo dentro de los límites del método, con las combinaciones y factores del Criterio aprobado |

**Perfiles, empalmes y combinaciones (Luis, 5-Oct).**
- **Perfiles.** El W10x49 se consigue en Chile solo importado. Prodalam lo vende como W 250 x 73,0 en ASTM A572 Gr50, no en A36. Se pide el equivalente soldado de fabricación nacional, IN o HN según NCh 730. Se deja fuera a HEA y HEB porque también son laminados importados; el argumento de peso vale para el HEB y no para el HEA 260, así que no se escribe.
- **Empalme.** No se afirma que el perfil nacional se venda en 12 m, porque Cintac y Prodalam declaran "largo variable a pedido" para las vigas soldadas. Se pide el empalme porque el plano no lo muestra en 12.776 mm.
- **Combinaciones.** La NCh3171 es la norma de combinaciones de carga; rige la versión 2017, aunque el Criterio cita la de 2010.
- **Fuentes:** `BASES TECNICAS/REFERENCIAS ACERO CHILE/_LEEME.md`.

**Viga intermedia, torsión y desangulación (Luis, 5-Oct).** Comentario propio sobre la vista en planta del plano (OBS-02) y su espejo en el addendum (OBS-04). Es un requisito de ADASA como fabricante del yugo, no un incumplimiento de BW Water.
- Estimación interna, no emitida. Las eslingas superiores a 45° y 50° comprimen cada larguero con unos 50 a 60 kN bajo 2,0D. El W10x49 sin arriostrar en su eje débil (r = 64,5 mm, L = 12.776 mm) tiene esbeltez de unos 198 y admite unos 245 kN en ASD con K = 1. El pandeo del larguero aislado no parece crítico.
- La incertidumbre está en el modo traslacional: los dos largueros desplazados hacia el mismo lado y el marco desangulado en paralelogramo, que solo resisten las esquinas, hoy sin detalle. Una viga intermedia sin arriostramiento en planta no lo corrige. Por eso se pide verificar la desangulación de forma explícita, y la solución (uniones rígidas o arriostramiento) queda a BW Water.

Verificado por render (`REVISIONES/TRANSMITTALES/P22-TM-09-000-042-0/COMENTARIOS/`): ningún cuadro tapa el dibujo ni el cajetín.
