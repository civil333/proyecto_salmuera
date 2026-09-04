---
titulo: Comentarios aún no incorporados en la ENTREGA 71
codigo: Correo comentarios pendientes submittal 25007-0071
fecha: 2026-08-06
estado: ENVIADO
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-08-06
---

# Correo de comentarios pendientes — submittal 25007-0071

**Estado: ENVIADO el 06-Ago-2026.**

| Campo | Valor |
|---|---|
| Archivo | `2026-08-06_Submittal-25007-0071-Outstanding-Items.docx` · **1 página, 341 palabras de cuerpo** · inglés |
| Para | Eduardo Yamauchi (BW Water) |
| CC | Andrew Sia, Magdier Arias, Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero |
| Asunto | 25007 Taltal - Submittal 25007-0071: outstanding items |
| Cadena | Cadena regular de revisión documental |
| Adjuntos | Ninguno |

## Qué comunica

Documento por documento, qué comentario de la aprobación previa quedó incorporado y cuál no. Un bloque por documento, con lo cerrado primero y lo pendiente después.

**Registro: petición, no imputación.** Todo lo pendiente se enuncia como `Please review` o `Please clarify`, y los dos ítems operativos como `Please confirm` — ocho peticiones en total. El correo no afirma incumplimiento: pide revisar o aclarar. Es la diferencia entre "no incorporaron X" y "por favor aclaren qué documento fija X", y con documentos ya aprobados y emitidos para construcción la segunda forma obtiene la corrección sin abrir una discusión sobre quién tenía razón.

El caso más claro es el de la base de aceptación del PMI: en vez de afirmar que falta, el correo pide aclarar **qué documento la fija**, porque hay una contradicción real — la sección de aceptación del procedimiento apunta a normas de terceros y tanto la ET como el ITP nombran UNS S32750. La pregunta es legítima y su respuesta cierra el punto.

| Documento | Reconoce cerrado | Queda pendiente |
|---|---|---|
| PMI Procedure | El 10% sobre el circuito de alta y la testificación de ADASA | La base de aceptación UNS S32750 (la sección de aceptación sigue remitiendo a normas de refinería de terceros) y la acotación del anexo del subcontratista, que además fija 5% por lote contra el 10% mínimo del ITP |
| Visual Procedure | La calificación del inspector VT | El formulario de registro: el procedimiento ya no identifica ninguno, y la fila 3.2 del ITP exige un `Visual report` en punto de testificación |
| Painting Procedure | El perfil de anclaje, ahora 50-80 µm en todo el documento | RAL 5012 y el producto por capa en el formulario de inspección |
| HP and LP Pressure Test | Las ediciones fijadas en las secciones 3.1 y 3.2 | Las cláusulas 5.5.2 y 5.6.3 siguen exigiendo la última edición, de modo que la edición no queda fijada para los ensayos; y no se declaran addenda |
| UHPRO Structural Calculation | Los dos puntos | Nada |

Más dos confirmaciones previas a la inspección del 13 y 14 de agosto: en qué formulario se registrará el ensayo hidrostático, y qué revisión del procedimiento de pintura gobierna la inspección de preparación.

## Decisión de fondo: sin códigos de respuesta

El correo **no asigna Código 1, 2, 3 ni 4**. Dos razones:

1. **Procesal.** Los códigos son instrumento del transmittal. Comunicarlos por correo sin que exista el transmittal deja la disposición sin respaldo formal.
2. **De tono.** Devolver a Código 3 cuatro documentos que ADASA ya había aprobado como noted, y que el proveedor emitió a Rev 0 para construcción, sube el conflicto sin necesidad. Lo que se necesita es que corrijan cuatro cosas concretas, y eso se obtiene diciéndolas.

Cada bloque abre reconociendo lo que sí se cerró. No es cortesía: delimita exactamente qué falta y hace verificable el pedido.

## Lo que deliberadamente NO dice

- **Ningún hallazgo nuevo sobre documentos aprobados.** Solo se menciona lo que era condición de la aprobación previa. Las tres regresiones introducidas en la Rev D del procedimiento de presión, el modelo de combinaciones de carga del informe estructural y los pernos de los recipientes a presión quedan como registro interno en `ENTREGAS_BWWATER/ENTREGA 71/_HALLAZGOS_DETERMINISTAS.md`.
- **Nada sobre el desfase del paquete de Bureau Veritas.** Reemplazar la copia del procedimiento de pintura que tiene el inspector es acción de ADASA. Al proveedor solo se le pide confirmar qué revisión gobierna.
- **Ninguna imputación por el formulario de ensayo ausente.** Va como confirmación operativa: el formulario desapareció en la Rev D, que ADASA aprobó.
- **Ninguna referencia interna.** Sin IDs `OBS-`/`NOTE-`, sin números de transmittal, sin el símbolo de sección. Verificado: cero coincidencias.

## Verificación de fuentes

| Afirmación del correo | Verificado contra |
|---|---|
| `UNS S32750` no está en el cuerpo del PMI Rev 0 | Barrido del PDF: una sola ocurrencia, en la comment sheet |
| El anexo fija 5% por lote para pernería | PMI Rev 0, pág. 21, Apéndice 1 |
| El ITP exige mínimo 10% | ITP `P22-BA-09-000-004` Rev 0, fila 2.4, leída por render |
| La calificación VT está declarada | Visual Rev 0, pág. 5, sección 5.1.1 |
| El Visual Rev 0 no identifica formulario | Pág. 8, sección 5.8.1; la Rev A nombraba `QAM-F004` y `QAM-F005` |
| La fila 3.2 del ITP exige `Visual report` | ITP Rev 0, leído por render |
| El perfil quedó en 50-80 µm en todo el documento | Painting Rev 0, págs. 9 y 11; la única supervivencia de `40-75` es la comment sheet |
| La fila `Colour` del formulario está vacía | Painting Rev 0, pág. 11, verificado por render PNG |
| Secciones 3.1 y 3.2 fijan las ediciones; 5.5.2 y 5.6.3 no | HP/LP Rev 0, págs. 4, 7 y 8 |
| `ASME B31.3-2024` existe | Publicada el 27-Dic-2024 |
| Los dos puntos del estructural están incorporados | 551 págs. sin duplicación; columna `Comment from Client` poblada, verificada por render |
| La inspección es el 13 y 14 de agosto | `AQ-QAM-F027 Inspection Request (003)` |

## Checklist pre-envío

- [x] `anti-ia` modo revisar: **VERDE**, 0% — 354 palabras, 21 oraciones, media 16,5, sigma 8,7, máxima 35 (ninguna sobre el umbral de 40 de U-03). Cero fingerprints en universales y en la familia Claude, incluidos los priors de Opus 5 (CL-19, CL-20, CL-21)
- [x] Sin códigos de respuesta, sin símbolo de sección, sin referencias internas, sin em dash: cero coincidencias en los cuatro
- [x] Ocho peticiones `Please review` / `Please clarify` / `Please confirm`; cero afirmaciones de incumplimiento
- [x] Una página, verificada por render
- [x] Metadatos Word limpios (`docx_metadata`, autoría Luis Rivera Gonzalez, en-US)
- [x] Enviado el 06-Ago-2026

## Checklist post-envío

- [x] `BORRADOR` → `ENVIADO` aquí y en el README
- [x] Registrado en `compromisos.yaml` (`PRG-24`, respuesta esperada de BW Water)
- [x] Cerrado `PRG-16`, el compromiso sobre si existía una Rev 0 del PMI Procedure: esta entrega lo responde
- [ ] Dejar el respaldo del envío en esta carpeta (`.msg` o PDF de la bandeja)
