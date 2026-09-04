---
titulo: "Hallazgos y veredicto propuesto — ENTREGA 73 (25007-0074), HMI Display Screenshot Rev B"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-10
---

# Hallazgos y veredicto propuesto — ENTREGA 73

> Documento interno de trabajo. **NO ENVIAR.** Complementa el [libro mayor de comentarios](_LEDGER_COMENTARIOS.md), que verifica el cierre de lo que estaba abierto. Aquí va lo que la Rev B trajo de nuevo y la propuesta de veredicto.

## Ficha

| Campo | Valor |
|---|---|
| Submittal | `25007-0074` |
| Emitido | lunes 10-Ago-2026 |
| Documento | `P22-LI-09-008-016` *HMI Display Screenshot* Rev B, 80 páginas, IFA |
| Fecha del documento | viernes 24-Jul-2026 |
| Revisión anterior | Rev A, 9 páginas, **Código 3** en el Transmittal N22 |
| Veredicto propuesto | **2 — Approved as noted** (ver la discusión al final) |
| Comentarios verificados | 7 de 7 — cuatro cerrados, dos parciales |

## Lo que decide el veredicto

Dos observaciones no cierran, y las dos exigen cambiar este mismo documento:

**OBS-01.** La pantalla de vista general trae el consumo específico en kWh/m³ y la energía total, pero **no hay tensión ni corriente en ninguna de las 80 páginas**. La Sección 5.4 de la ET pide que el medidor de variables eléctricas entregue al menos voltaje, corriente y potencias y que esas variables estén en una pantalla del HMI junto al consumo específico. Llegó la mitad. El Transmittal N10 ya había registrado que el Digital Power Meter integra once parámetros eléctricos en la IO List y en la Data Transfer List: el dato está en el PLC y no se despliega.

**OBS-04.** El conjunto de pantallas se completó —seis pantallas de proceso contra dos— pero la mitad de la observación que pedía TAG consistentes con el P&ID y la Instrument List no se cumplió. Hay **seis defectos de TAG** contra los listados aprobados, repartidos en cinco de las seis pantallas. El más grave rotula la bomba de alta presión de 93 kW con el TAG de la bomba CIP de 11 kW.

El detalle de los seis, con su cita y su evidencia renderizada, está en el libro mayor.

## Lo que la Rev B trajo sin que se le pidiera

Registro interno. **Nada de esto se emite**: levantarlo excede el alcance de los comentarios abiertos y, en el caso de la documentación de biblioteca, no afecta a las pantallas.

**Cincuenta y ocho páginas de manual de Rockwell reproducidas literalmente.** Las secciones 2.1 a 2.10 son la documentación de la biblioteca PlantPAx tal cual, con TAG de ejemplo genéricos (`FI101`, `P_PF753`), tablas numeradas de la fuente (Table 55, Table 57, Table 58, Table 222) y referencias cruzadas a páginas que no existen en este documento — *"Basic Faceplate Attributes on page 32"*, *"Common Operator Tab - Motors on page 247"*, cuando el cuerpo tiene 77 páginas numeradas. Es lo que hace que el documento crezca de 9 a 80 páginas. Sirve como manual de faceplates y por eso cierra OBS-03 y OBS-05; el punto es solo que su procedencia no está declarada.

**La numeración interna no cuadra.** La portada declara `Page 1 of 80` y los pies del cuerpo corren `Page N of 77`. Las dos páginas de la hoja de comentarios quedan fuera del recuento del cuerpo.

**La hoja de comentarios está mal numerada.** Cinco filas numeradas 1, 2, 3, 3 y 4: dos filas llevan el número 3, y la de la ISA-101 aparece como 4 cuando era la quinta observación. Defecto de trazabilidad de la propia hoja.

**Diecisiete días entre la fecha del documento y su emisión.** Fechado el viernes 24-Jul, emitido el lunes 10-Ago. En un frente donde el Plazo de Entrega ya está vencido y este es el comentario más antiguo abierto, el dato se registra.

**Escala única en la pantalla de tendencias.** El eje vertical va de −1.500 a 1.500 para todos los TAG, con independencia de su unidad. Verificable en el FAT.

**Resumen de alarmas sin diferenciación de prioridad.** Todas las filas sobre una única banda roja, mientras la página 26 documenta cuatro niveles con icono propio. Verificable en el FAT.

## Plazo de revisión

El Submittal Form pide retorno el **jueves 13-Ago**, tres días desde la emisión. El plazo de revisión documental de la BAE 12803, **Cláusula 37.2**, son siete días hábiles, que desde el lunes 10-Ago vencen el **miércoles 19-Ago**. Es el mismo criterio con que se computó el plazo en el Transmittal N30. La respuesta se emite dentro de ese plazo, no dentro del que pide el formulario.

## Discusión del veredicto

**Propuesta: Código 2 — Approved as noted.**

El criterio determinante de la Sección 6.2 es si el documento revisado debe cambiar para llegar a Rev 0. Aquí sí: hay que re-rotular seis TAG y agregar tensión y corriente a la pantalla de vista general. La pregunta siguiente es si eso es Código 2 o Código 3.

Va como **Código 2** porque lo que fundó el Código 3 del Transmittal N22 —que el conjunto de pantallas estaba incompleto— ya no existe: las seis pantallas están, con la recuperación de energía y la salmuera representadas dentro de las etapas, y las tres observaciones restantes de aquel ciclo cierran. Lo que queda es alineación con listados ya aprobados y un elemento de despliegue que se agrega, todo incorporable al emitir Rev 0 sin una revisión intermedia. El precedente del proyecto es explícito: alinear un documento a otro documento aprobado es Código 2, y el Código 3 se reserva para cuando el contenido propio está mal de raíz. La topología de las pantallas es correcta; lo que está mal son las etiquetas.

**El argumento en contra, para que quede registrado.** Un Código 2 manda el documento directo a IFC Rev 0 sin que ADASA vea el resultado, y son seis defectos de TAG, no uno. Uno de ellos confunde la identidad de dos máquinas —la bomba de 93 kW con vibración y RTD contra la bomba CIP de 11 kW— y otro repite, en un documento nuevo, la pérdida del mapeo devanado/rodamiento que mantiene retenida desde el Transmittal N27 la firma de protección por RTD del FAT Procedure. Además, el Operating and Maintenance Manual depende de estas pantallas y reproducirá los TAG que aquí queden.

Si se prefiere ver las correcciones antes del IFC, el Código 3 es defensible y su determinante es el intercambio de identidad de las bombas. **Es una decisión de criterio, no de hecho.**

## Condición de aceptación si se emite como Código 2

Redactada para pasar al bloque `Action to issue at IFC Rev 0` del transmittal:

- Agregar a la pantalla de vista general las lecturas del medidor de variables eléctricas —tensión, corriente y potencia— junto al consumo específico que ya despliega, conforme a la Especificación Técnica (`P22-ET-09-000-001-0`), Section 5.4 - Control System, y expresar la potencia en kW.
- Reconciliar los seis TAG contra la Instrument List Rev E, la Valve List Rev D y la Equipment List Rev B: `BH-09-001` en la bomba de alimentación de alta presión, `TE-09-001` en el devanado de esa bomba, `VE-09-005` en el ramal de make-up CIP, `PIT-09-003` en la alimentación de primera etapa, `FIT-09-004` en la línea de rechazo a drenaje, y `LS-09-002` en el nivel bajo del estanque de antiscalante de la vista general.
- Declarar en qué pantalla se despliegan `PIT-09-008` y `FIT-09-002`, o por qué no se despliegan.

La verificación visual completa del conjunto queda reservada al FAT.

## Trazas de la revisión

| Ruta | Contenido |
|---|---|
| `md/P22-LI-09-008-016_HMI_Display_Screenshot_B_extracted.md` | Texto extraíble de las 80 páginas |
| `render/pagina_NN.png` | Render completo de las 80 páginas |
| `render/nativo/` | Imágenes embebidas a resolución nativa de las páginas decisivas |
| `render/crop_*.png`, `render/zoom_*.png` | Recortes ampliados que sostienen cada afirmación de TAG |

## Puntos de contexto que no pertenecen a este documento

- **La ENTREGA 72 sigue sin transmittal.** El submittal `25007-0072` entró el 06-Ago, un día después de que saliera el Transmittal N30, que cubría los submittals `25007-0068`, `25007-0069` y `25007-0070`. Sus cuatro documentos no tienen veredicto, y uno de ellos es la Plant Control Philosophy Rev 0, que gobierna el contenido de estas pantallas y que sostiene el mapeo devanado/rodamiento mencionado arriba.
- **No existe el submittal `25007-0073`.** Esta carpeta, rotulada ENTREGA 73, contiene el `25007-0074`. O BW Water saltó el correlativo, o ese submittal llegó y no se descargó: el barrido de correo entrante está en HOLD con 22 correos identificados sin capturar.
- **El correo del `25007-0074` no está en el registro de recibidos.** Los archivos aparecieron en la carpeta sin pasar por la captura de `CORREOS/_RECIBIDOS/`.
