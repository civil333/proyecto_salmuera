---
titulo: Correo de cobertura — Transmittal N38
fecha: 2026-09-03
estado: ENVIADO
tipo: correo
destinatario: BW Water
project: salmuera-taltal
---

# Correo de cobertura del Transmittal N38

**Estado:** **ENVIADO el jueves 3-Sep-2026 a las 18:19 hora de Chile.** Respaldo archivado en esta carpeta: `transmittal 38 enviado.pdf`.

**Lo que salió, según el respaldo**

- **Asunto íntegro**, con la exigencia por delante: se lee desde la bandeja sin abrir el adjunto.
- **Un adjunto de 229 KB**, el transmittal en PDF; en disco pesa 234.267 bytes.
- **Los tres párrafos sustantivos salieron palabra por palabra**, verificados contra el `.docx`.
- **Distribución idéntica al borrador:** cinco destinatarios —Víctor Gutiérrez, Ronald Pellejero y Jorge Guevara por ADASA; Eduardo Yamauchi y Fitri Indriyani por BW Water— y nueve en copia, todos de BW Water.
- **Allan Valentos quedó fuera por segunda vez consecutiva**, de modo que la omisión del N37 se confirma deliberada y deja de ser una duda abierta.

🔴 **Lo que NO salió, y hay que reparar:** el bloque del enlace de descarga desapareció al pegar en Outlook. No salieron la línea que lo introduce, ni el enlace, ni las tres viñetas que nombran los `CC_ADASA`. **BW Water recibió el transmittal pero no tiene cómo llegar a los tres PDF anotados**, y la Sección 4 del propio transmittal los remite a un enlace que no llegó. Es el modo de falla ya catalogado: el enlace va dos veces. Se repara con un correo corto en la misma cadena.

Las líneas de firma en texto plano tampoco están, pero eso es lo esperado: Outlook las reemplazó por la firma corporativa.

**Archivos de esta carpeta**

| Archivo | Qué es |
|---|---|
| `crear_correo_tm38.py` | Generador. El cuerpo vive aquí, hardcodeado |
| `2026-09-03_Transmittal-N38.docx` | El correo, para pegar en Outlook |
| `2026-09-03_Transmittal-N38_Descripcion.md` | Este archivo |

## Qué dice el correo

Tres párrafos, **230 palabras de prosa**. Ejecutivo y directo: toda la explicación en detalle vive en el transmittal, y el correo no reproduce la tabla de doce documentos ni el detalle de los códigos.

**Encabeza con el compromiso de BW Water, no con la exigencia de ADASA.** Es más fuerte, porque son sus propias palabras y sus propias fechas, registradas en dos minutas:

- **Minuta del 26 de agosto de 2026:** *"P&ID / Line List: Amendments to correct wrongly mentioned line list items; fabrication drawings to be updated and sent by Friday, August 28, 2026."*
- **Minuta del 1 de septiembre de 2026**, en Next Arrangements: *"Submit the complete documentation package (updated P&IDs, line list, ISO drawings) by tomorrow"*, es decir el 2 de septiembre.

**Tres fechas comprometidas y ninguna cumplida:** viernes 28 de agosto y miércoles 2 de septiembre por compromiso propio en minuta, y jueves 3 de septiembre por la exigencia del Transmittal N37.

El **segundo párrafo** pone la consecuencia operativa, que es de hoy: las dos minutas fijan a Bureau Veritas testificando ensayos hidrostáticos el jueves y el viernes, y la del 1 de septiembre registra que ADASA necesita el mapeo de números de línea y presiones para informar al inspector. Ese mapeo es justo lo que el P&ID Rev 0 y la Line List Rev 1 dicen distinto. Ahí va **la exigencia en negrita: cerrar los submittals pendientes con documento esta semana, como se acordó**, y la consecuencia que el N37 ya declaró, sin agravarla.

El **tercer párrafo** es el adjunto y el veredicto en una línea, con el saldo de siete de doce y la remisión a la Sección 3.

## Asunto

`TALTAL - Transmittal N38 - outstanding submittals to be closed with documents this week`

Encabeza con la exigencia, no con el número de submittal, porque tiene que leerse desde la bandeja sin abrir el adjunto.

## Adjunto y enlace

- **Adjunto:** el transmittal en PDF, exportado desde Word real para que el índice quede resuelto.
- **Por enlace de descarga**, no adjuntos: los tres `CC_ADASA` del ultrasonido, el HMI y el procedimiento de FAT.

## Contexto Interno (No enviar)

- **Las dos citas de minuta son literales** y están verificadas contra los PDF en `MINUTAS DE REUNION/`. Son la munición más fuerte del correo porque no son un pedido de ADASA: son el compromiso escrito del proveedor, con fecha, incumplido dos veces antes de la exigencia del N37.
- **El orden importa.** La regla del proyecto pide liderar con la obligación y usar el compromiso como refuerzo. Aquí la obligación de someter los planos de taller como entregable propio viene del Transmittal N30, y va escrita en la Sección 3 del transmittal; el correo lidera con las fechas de minuta porque es el vehículo ejecutivo y lo que tiene que quedar es el patrón.
- **Los siete Código 1 no llevan PDF anotado a propósito.** Vienen en Rev 0 apto para construcción; se verificó únicamente la condición que los había dejado en Código 2 y ninguno la falla. Lo que la revisión encontró de nuevo en ellos se documenta, no se observa.
- **La verificación del HMI se hizo por render.** Su hoja de comentarios declaraba dos acciones y en realidad cerraron seis de siete observaciones. Los TAG viven dentro de las imágenes y sesenta de las ochenta páginas devuelven texto vacío: afirmar una ausencia sin renderizar habría sido refutable.
- 🔴 **La fecha del FAT no aparece** ni en el correo ni en el transmittal. La Nota Técnica `P22-NT-09-000-003-0` dejó en disputa cuál ventana gobierna, así que se dice que es antes de que abra el FAT.
- 🔴 **Sin cifras de multa y sin invocar el umbral de treinta días.** `INT-08` sigue abierto: la Notificación de Adjudicación no está en el repositorio.
- **Sin códigos internos** `PRG-`, `INT-` ni `BV-`, sin Van Doorn y sin el saldo de jornadas de Bureau Veritas.
- **La distribución reproduce la que el usuario fijó al enviar el N37.** 🔴 Allan Valentos quedó fuera de aquel envío y no se ha aclarado si fue deliberado: **confirmar antes de enviar**.
- El registro de compromisos ya quedó actualizado y regenerado; `update_register_n38.py` está escrito y **no se corre hasta después del envío**.

## Correo de reenvío del enlace — ENVIADO

**Estado:** **ENVIADO el jueves 3-Sep-2026**, por confirmación del usuario. Generador `crear_correo_tm38_enlace.py`, documento `2026-09-03_Transmittal-N38_Enlace.docx`.

Existe porque el bloque del enlace no sobrevivió al pegado del correo de las 18:19. Va como **respuesta a la misma cadena**, con `RE:` y el mismo asunto, y es transaccional: 71 palabras, sin repetir sustancia del transmittal, sin reabrir el veredicto y sin volver a exigir nada. Solo la línea que introduce el enlace, la URL y las tres viñetas de los `CC_ADASA`.

⚠️ **No verificado.** No hay respaldo del enviado en esta carpeta, de modo que no se pudo comprobar que el enlace sobreviviera esta vez. Es justamente el chequeo que importa: la pérdida del enlace en Outlook va cuatro veces y en el correo anterior se comió incluso la URL en texto plano. Dejando el respaldo aquí se confirma en un minuto.

## Checklist pre-envío

- [x] Carpeta `COMENTARIOS/` publicada y enlace pegado en los dos generadores
- [x] Los dos documentos regenerados y el enlace **verificado carácter a carácter sobre el `.docx` emitido**: idéntico en el destino del hipervínculo, en el texto visible del transmittal y en la línea del correo
- [x] PDF exportado desde Word real con `exportar_pdf_word.py`: **12 páginas**, índice resuelto con las páginas reales y sin el placeholder de campo, y el enlace clicable verificado en la anotación del PDF
- [x] Allan Valentos fuera por segunda vez: omisión deliberada, confirmada
- [x] Distribución confirmada en el envío

## Checklist post-envío

- [x] `BORRADOR` a `ENVIADO` con la hora de Chile, en este archivo y en la Bitácora del README
- [x] Respaldo archivado: `transmittal 38 enviado.pdf`
- [x] Cuerpo verificado contra el `.docx`: los tres párrafos íntegros; 🔴 **falta el bloque del enlace**
- [x] `update_register_n38.py` corrido: seis filas del Master Register actualizadas y once de Revision History agregadas; el tally obtenido **68 / 19 / 2 / 0** coincide con el declarado antes de correr
- [x] `Estado Vigente` del README pisado con las cifras aplicadas
- [x] Enlace de descarga reenviado en la misma cadena el 3-Sep-2026 (`2026-09-03_Transmittal-N38_Enlace.docx`)
- [ ] ⚠️ **Dejar el respaldo del reenvío y verificar que el enlace sí salió esta vez** — sin respaldo en carpeta, el envío está registrado por confirmación del usuario y **no verificado**
