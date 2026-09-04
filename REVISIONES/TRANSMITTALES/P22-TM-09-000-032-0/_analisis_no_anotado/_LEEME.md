# Análisis que no produce PDF anotado — TM N32

Estos tres scripts se escribieron durante la revisión de la ENTREGA 75 y **no generan un `CC_ADASA` que se emita**. Viven fuera de `COMENTARIOS/` a propósito: esa carpeta contiene solo lo que se adjunta y se sube al enlace de descarga, de modo que no quede ningún archivo ahí que pueda enviarse por error.

| Documento | Disposición en el TM N32 | Por qué no lleva anotado |
|---|---|---|
| PMI Procedure `P22-BA-09-000-006` Rev 0 | **1 — Approved** | Un Código 1 no lleva `CC_ADASA`. Lo que queda son dos ítems de aseo que la Sección 3 del transmittal recoge para la próxima emisión natural |
| HP and LP Pressure Test Procedure `P22-BA-09-000-010` Rev 0 | **Sin código de respuesta** | Un documento devuelto sin código no se anota: su punto abierto va íntegro en el texto de su subsección de la Sección 2 |
| Painting Procedure `P22-BA-09-000-011` Rev 0 | **Sin código de respuesta** | Ídem |

**Qué conservan.** El encabezado de cada script guarda el razonamiento del triaje del 12-Ago: qué pidió ADASA literalmente, qué contestó BW Water en la hoja de comentarios y por qué el punto se mantuvo, se replanteó o se dejó pasar. Esa traza no está en ningún otro lado en esa forma; el detalle emitible vive en el transmittal y el registro completo del triaje en `ENTREGAS_BWWATER/ENTREGA 75/_LEDGER_COMENTARIOS.md`.

**Si alguna vez hay que reconstruir el anotado** —por ejemplo si uno de estos documentos vuelve a revisión con código— los scripts corren tal cual: copian su PDF fuente desde `ENTREGAS_BWWATER/ENTREGA 75/` y escriben la salida junto a sí mismos, no en `COMENTARIOS/`.
