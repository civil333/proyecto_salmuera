# _ANALISIS_N30 (interno — NO ENVIAR)

TM N30 · submittal 25007-0068 (E68, recibido jueves 23-Jul-2026) · **1 documento, re-revisión a Rev 0 (IFC)** · veredicto global **1 — Approved**.

Documento: **Datasheet of PLC and HMI Panel Component (Major Component)**, código de registro `P22-ET-09-008-001`, ítem **#29** del Master Register. Cuarto ciclo: Rev A Code 2 (N1) → Rev B Code 3 (N21) → Rev C Code 2 (N26) → **Rev 0 Code 1** (N30).

## Triaje y extracción (E68)

- Zip descomprimido; 2 archivos: el datasheet (50 págs, 5,07 MB) y el Submittal Form (declara `P22-ET-09-008-001` Rev 0, `Sub. For: IFC`, retorno pedido 26-Jul, que es domingo).
- Triaje página por página (PyMuPDF): 49 páginas verticales carta/A4 + la 50 apaisada (hoja de comentarios). **Ninguna lámina de proyecto con cajetín** → extracción textual estándar a `ENTREGA 68/md/`. Las páginas con 4.000-8.000 trazos vectoriales son figuras dimensionales de los datasheets Rockwell embebidos.
- El **Control System Architecture Rev D**, fuente de cruce, sí es plano (A1 apaisado, texto vectorizado, 0 caracteres extraíbles en la lámina P2) → `large-pdf-reader --mode drawing` y lectura por render. Sin ese paso la cita a la lámina P2 habría sido una afirmación sin respaldo.
- Cajetín de portada, hoja del componente HMI, hoja de salida analógica, BOM del Outline y hoja de comentarios: leídos por **render PNG**.

## Cierre de las dos NOTE del TM N26

| Ítem N26 | Estado | Verificación |
|---|---|---|
| **NOTE-01** — alinear el código al de tres dígitos | **Cerrado real** | Portada (dos lugares) y los **7 encabezados de componente** leen `P22-ET-09-008-001`; cero ocurrencias del código de dos dígitos en el contenido. Cambiaron 6 encabezados: la hoja del módulo analógico (pág 36) ya traía el código correcto en Rev C, que es justo lo que decía la NOTE-01. Residual: el **nombre del archivo** entregado conserva `P22-ET-09-008-01_0`. |
| **NOTE-02** — cantidad de módulos 5069-IY4 | **Cerrado en sustancia, con desvío de fuente** | BW remite a `P22-CD-09-004-001-P2 Control System Architecture Rev D`: verificado por render, ítem 4 = "PLC RTD INPUT MODULE 4 X RTD, 5069-IY4, **QTY 2**". Coincide con el BOM del Outline Rev 0 (A5;A6). Cubre con holgura los **4 puntos RTD** de la IO List Rev 5. **Ojo:** ADASA había nombrado como gobernante el LCP Datasheet Rev 1, que **no declara la cantidad y ni menciona el HMI** — la NOTE-02 estaba mal fundada y BW citó el documento correcto. No escribir "confirmado según el LCP Datasheet": es refutable. |

## Diff Rev C → Rev 0

Verificado por dos vías (diff textual página por página y comparación de píxeles de las 50 páginas): **41 páginas bit-idénticas**; difieren la 1, 2, 8, 15, 21, 28, 36, 47 y 50. **Ninguna especificación técnica cambió.** Sin páginas añadidas, eliminadas ni reordenadas. Cambios: código del documento, fila de revisión del cajetín, fecha, contador de páginas y hoja de comentarios. Sin datos agregados por iniciativa del proveedor en el cuerpo técnico.

## Hallazgo principal — número de catálogo del terminal de operación

**La primera redacción decía "dos documentos" y "hallazgo nuevo". Las dos cosas eran falsas** y habrían invitado una réplica documentada. Corregido tras la verificación adversarial.

- **Este datasheet** (hoja del componente HMI, pág 47): Modelo **2711P-T10C22D9P**; fila 15 `Ethernet Interface = 2 x Ethernet RJ45`; fila 18 `RAM = 1 GB`. La fila 2 (`Type`) dice solo "PanelView Plus 7" — **no** dice "Performance"; esa palabra solo aparece en la hoja NHP embebida (págs 48-49). Liderar con el número de catálogo, nunca con la gama.
- **El `-D8S` está en cuatro documentos vivos**, todos verificados por mí:

| Documento | Evidencia | Veredicto ADASA |
|---|---|---|
| Control System Architecture Rev B (E11) → Rev D | ítem 6 / lámina P2 ítem 7 | Rev B **VALIDATED** en N4; **Rev D Code 1 en N14** |
| PLC/LCP Schematic Diagram Rev A (E46), pág 29 | `Touch Screen 2711P-T10C21D8S 1 HMI1` | Code 2 en N20 |
| PLC/LCP FAT Procedure - Hardware Rev A (E64), pág 16 | `Power ON HMI (HMI1: 2711P-T10C21D8S, Allen-Bradley)` | Code 2 en N27 |
| Outline Panel Drawing Rev 0 (IFC), pág 13 ítem 11 | render del BOM | **Code 1 en N29** |

- El `-D9P` vive **solo en la familia del datasheet** (Rev A, B, C, 0) desde el 23-nov-2025. No es un desliz reciente.
- **Fechas:** solo el datasheet Rev 0 y el Outline Rev 0 comparten el 20/07/26. El Control System Architecture Rev D es del **1-abr-2026** — no atribuirle esa fecha.
- **Ancla técnica (el enunciado que no admite réplica):** per la ficha técnica del fabricante para los terminales Standard (Rockwell 2711P-TD008), el campo `21` designa **un** puerto 10/100Base-T (el campo `22` designa dos con topología DLR) y esos terminales llevan **512 MB de RAM**. El `2711P-T10C21D8S` **no satisface** las filas 15 y 18 de la ficha del propio proveedor. El eje NO es "Performance vs Standard" ni capacidad de pantallas: el Standard admite 100 pantallas, 500 alarmas y un controlador, y el proyecto tiene un PLC y ~109 entradas de alarma.
- **Encuadre (regla anti-invención):** ADASA validó el `-D8S` en el N4, aprobó Code 1 el Architecture en el N14, codificó Code 2 el Schematic (N20) y el FAT Procedure (N27) con el `-D8S` dentro, y aceptó el `-D9P` en el N21. **No es imputable a BW Water.** Nada de "missing", "inconsistent selection" ni "non-compliance".
- **Por qué ADASA declara en vez de preguntar** (`feedback_adasa_declara_valor_vinculante`): el borrador inicial pedía a BW Water "confirmar cuál corresponde". Eso es impropio de la postura del proyecto y además deja el punto abierto justo cuando el panel entra a fabricación. ADASA declara vinculante el **2711P-T10C22D9P** apoyándose en: (a) es el modelo de la ficha del propio proveedor desde la Rev A; (b) el **TM N22 fijó expresamente este datasheet como la base de hardware del diseño de pantallas**; (c) el `-D8S` no cumple dos filas de requisito de esa misma ficha. Se deja la puerta abierta con carga de prueba: si BW quiere suministrar el Standard, debe declararlo por escrito antes de comprar y demostrar que cumple la ET (Section 5.4: históricos y tendencias) y que hospeda las pantallas que el N22 ya exigió (variables eléctricas y energía, tendencias, setpoints).

## Ítems documentales del propio documento (no degradan; a la próxima emisión natural)

1. **La hoja de comentarios dejó de consolidar:** la Rev C listaba los tres ítems del N21 con sus respuestas (HART aparecía 15 veces, más el typo "Tattal" y OBS-01/02); la Rev 0 los **borró** y solo muestra los dos del N26 (3.071 → 1.773 caracteres). En un documento emitido para construcción se perdió el registro de cierre de la disposición HART. Mismo patrón que `feedback_acta_proveedor_corregir_registro`: lo que el proveedor borra es información.
2. **La CCS cita una "Rev D" inexistente** (el cajetín es A/B/C/0) — copy-paste de la respuesta de la Rev C con la letra incrementada.
3. **Portada "Page: 1 of 49" con 50 páginas.** Regresión: la Rev C decía 50 correctamente (la Rev B ya había tenido el mismo error).
4. **`Issued for: ISSUED FOR APPROVAL` en las 7 hojas** de una emisión que el Submittal Form somete como IFC. Precedente vinculante: el N29 trató el mismo defecto en el Outline Rev 0 como cosmético, Code 1, "tidy at the next natural issue". Se le da el mismo peso.
5. **Hoja de salida analógica (pág 28):** el `Design Intent/Purpose` describe *"an on/off electrical switch for devices that operate using a Direct Current (DC) power source"* — es la descripción de la salida **digital**, copiada sobre una hoja cuyo `Type` es `Analog Output`; y el `Model` dice `5069-OF4/ OF8`, dos catálogos, cuando el Architecture Rev D y el BOM fijan **OF4 qty 2**. Ambos van a construcción así.
6. **Los encabezados no llevan índice de revisión** junto al número de documento.

## Veredicto — **1 — Approved**

Se descartó el Code 2 de la primera pasada. **Argumento estructural decisivo:** el Code 2 significa "corregir antes de emitir a Rev 0" y este documento **ya está en Rev 0**; su fórmula canónica ("issue at IFC Rev 0 — no new revision required") le ordenaría a BW Water incorporar algo a una emisión ya hecha, y el CLAUDE.md prohíbe expresamente el "in Rev X" en Code 2. Sobre un Rev 0 solo caben Code 1 (nada cambia en este documento) o Code 3 (re-emitir). **Precedente:** el N29 dispuso los dos primeros Rev 0 del proyecto (Outline y Line List) y ambos fueron Code 1, con los residuales declarados "to tidy at the next natural issue". No hay ningún Code 2 sobre un Rev 0 en 29 transmittals.

Fijado el vinculante en el `-D9P`, este datasheet **es correcto en su contenido propio**: el defecto vive en los otros cuatro documentos → Sección 3, que es exactamente el criterio de la Sección 6.2 ("una nota cuyo entregable vive fuera del documento revisado no lo degrada"). Los seis ítems documentales son housekeeping de emisión (`feedback_code1_housekeeping_rev0`) y no justifican forzar una Rev 1.

**Consecuencia operativa:** Code 1 → **sin CC_ADASA** (Sección 3.8). El PDF anotado que se generó cuando el veredicto de trabajo era Code 2 queda como traza interna en `COMENTARIOS/` con su `_NO_EMITIR.md`; no se adjunta ni se sube.

Tally del registro tras N30: **50 C1 / 28 C2 / 6 C3 / 0 C4**, 108 items / 84 delivered, **30 TMs / 68 entregas**.

## Correcciones de arrastre aplicadas a la Sección 3

- **El HMI Display Screenshot NO está "sin entregar".** Los TM N26 a N29 lo arrastraban como *"never submitted / last undelivered control child"*. Falso desde el 15-Jun-2026: se entregó **Rev A en la E50** y volvió **Code 3 en el TM N22** con OBS-01 a OBS-05. La fuente de la contaminación era la celda "Action Required" de la fila #68 del registro, que seguía con el texto viejo; **corregida** en `update_register_n30.py` (bloque `MR_ACTION_FIXES`).
- **La GA del Antiscalant Dosing Tank es Rev B**, no Rev C (los N27 a N29 la listaban mal). El registro estaba bien.
- **Dos Code 3 abiertos que llevaban cuatro transmittals sin aparecer** en ninguna Sección 3: el **Instrument Location Layout Rev C** (Code 3 desde el N23) y el **Tie-In Point Layout Rev A** (Code 3 desde el N7, el más antiguo vivo del proyecto). Ambos incorporados al "Also open". Con ellos, los seis Code 3 del Summary cuadran.

## Verificación adversarial

Tres verificadores en paralelo instruidos a refutar. Aportes que cambiaron el entregable: el conteo real de documentos con el `-D8S` y su estado ADASA; la fecha del Architecture Rev D; que el datasheet no se autodeclara "Performance"; el ancla de las filas 15/18 contra la ficha del fabricante; el argumento estructural que volteó el veredicto de Code 2 a Code 1; la pérdida del historial en la CCS; los defectos de la hoja de salida analógica; y las tres correcciones de arrastre de la Sección 3. Todos los hallazgos críticos fueron **verificados a mano** (render de los tres BOM, grep de los PDF fuente, ficha técnica del fabricante, filas del registro) antes de incorporarse.

## Artefactos

- Transmittal: `crear_transmittal.py` → `TRANSMITTAL N30 ADASA-BW_WATER.docx` + PDF de 5 páginas generado con Word real (`exportar_pdf_word.py`, nuevo en la raíz; TOC resuelto y verificado).
- Registro: `../../EVALUACIONES/update_register_n30.py` (50/28/6/0; backup `_pre-N30.xlsx`; incluye la corrección de la celda #68).
- `COMENTARIOS/` — traza interna, no se emite (ver `_NO_EMITIR.md`).
- Correo de cobertura: `CORREOS/Julio 2026/2026-07-23/crear_correo_tm30.py` (BORRADOR, `DOWNLOAD_LINK` pendiente).

## Pendiente para Luis

- Pegar el enlace Synology del paquete N30 en el transmittal (`DOWNLOAD_LINK`) y en el correo, regenerar ambos y volver a exportar el PDF.
- **Paquete Bureau Veritas:** `PAQUETE_INSPECCION_BV/05_INGENIERIA_REFERENCIA/INSTRUMENTACION_ELECTRICA/` contiene este datasheet en **Rev C**, ahora superada. A BV se le declaró que toda actualización iría por el mismo enlace Synology; corresponde reemplazarlo por la Rev 0 antes de la V1 (27-31 Jul). Decisión del usuario: es material en manos de un tercero.
