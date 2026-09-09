---
titulo: Transmittal N39 y emisión en revisión 0 de la ingeniería aprobada
fecha: 2026-09-09
estado: ENVIADO
destinatario: Eduardo Yamauchi (BW Water)
cadena: transmittals
type: correo
project: salmuera-taltal
---

# Correo único — Transmittal N39 y emisión en revisión 0

> **ENVIADO el miércoles 9 de septiembre de 2026.** Hora pendiente de registrar desde el respaldo.

**Archivo:** `2026-09-09_Transmittal-N39-and-Rev0-Issue.docx` · **Script:** `crear_correo_tm39_rev0.py`
**Adjunto:** `TRANSMITTAL N39 ADASA-BW_WATER.pdf` (P22-TM-09-000-039-0), **11 páginas**, exportado desde Microsoft Word con el índice resuelto.
**Enlace de descarga:** incorporado y verificado sobre el `.docx` y el `.pdf` emitidos, carácter a carácter y como destino del hipervínculo.
**Plazo pedido:** viernes 11 de septiembre, el que la reunión de hoy fijó para cerrar los hitos documentales.

## Por qué es uno y no dos

Había dos borradores del 9 de septiembre para Eduardo, con la misma copia y el mismo plazo: la cobertura del N39 y la auditoría de emisión para construcción. Se funden en este. Los dos originales quedan en `_no_enviados_fusionados/`.

El precedente es el correo del N37: llevó una exigencia de igual peso en 72 palabras de primer párrafo y mandó la lista nominal de los doce documentos a la Sección 3 del transmittal. Aquí pasa lo mismo. **Las cuatro tablas viven en la Sección 3 del transmittal** y el correo remite a ellas.

## Resumen del cuerpo

Seis párrafos, 404 palabras de prosa. **Primera persona**, que es el registro de la sección 11.1 del perfil y del que depende el argumento: quien reclama es quien aprobó.

1. **La exigencia.** La reunión de hoy fijó el viernes 11. De los 72 documentos de ingeniería, 46 nunca se emitieron para construcción y 34 de ellos no tienen ninguna observación abierta. Mediana de 184 días, los cuatro más antiguos 267. Remite a la Sección 3 del adjunto para el listado y los fundamentos.
2. **El criterio ya está acordado y lo puso BW Water**, con su cita literal de la hoja de comentarios del `P22-DWG-09-007-003` Rev E. Cierra en una línea: es lo que se pide ahora, con fecha.
3. **El transmittal N39.** Veredicto 2, un Código 1 y dos Código 2, cero Código 3. Los tres son re-emisiones revisadas solo contra los comentarios ya levantados.
4. **`VM-09-065`**, que es el único punto con fecha propia porque la lista gobierna la compra.
5. **Lo que se pide el viernes 11**, con el desactivador de la defensa previsible y la fecha comprometida en el DDSR para lo que no alcance.
6. **Reserva genérica de derechos.**

Cierra con el enlace de descarga y los dos PDF anotados.

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| 113 ítems, 72 de ingeniería, 46 sin emitir, 34 sin observación | `auditar_documentos_bw.py` en tiempo de ejecución | Sí, el script imprime las cifras en cada corrida |
| Mediana 184 días y máximo 267 | `_AUDITORIA_REV0_2026-09-09.md` | Sí |
| La cita de BW Water | Hoja de comentarios del `P22-DWG-09-007-003` Rev E, página 4, `ENTREGA 42` | Sí, sobre el PDF |
| Ese plano en Código 1 desde el 11 de junio, hoy en Rev F | Master Register e historial de transmittals | Sí, y **vive en la Sección 3 del transmittal, no en el correo** |
| Veredicto 2, un Código 1 y dos Código 2 | `P22-TM-09-000-039-0_TRANSMITTAL.md`, Response Summary | Sí |
| `VM-09-065` en PVC sobre una línea 316L | Valve List Rev E y Line List Rev 1 aprobada en el N38 | Sí, por extracción por coordenadas |
| 11 documentos con cajetín contradictorio | Auditor, categoría C | Sí |
| 6 filas del DDSR con fecha al 11-Sep | `leer_ddsr()` sobre el informe del 7 de septiembre | Sí |

**Las cifras del correo y las de la Sección 3 del transmittal salen del mismo auditor**, de modo que no pueden discrepar. Si el Master Register o el DDSR cambian, cambian las dos a la vez al regenerar.

Las fechas quedaron comprobadas contra el día de la semana: **viernes** 11, y las entregas llegaron el **viernes** 4 y el **martes** 8.

## Contexto Interno (No enviar)

- **Queda fuera por decisión del usuario, y disponible si el asunto escala:** el idioma castellano de la **Cláusula 6** de la BAE, el **hito de pago del 10 por ciento**, la multa de la **Cláusula 43.1 letra a), 0,05 % diario** por no entrega de documentación final, y la frase de la ET sobre no liberar equipos para transporte sin documentación aprobada. Por eso el cierre lleva reserva genérica de derechos.
- 🔴 **El tono del párrafo 2 se suavizó por decisión del usuario, y la razón es el objetivo del correo: que emitan, no ganar el argumento.** La primera redacción abría con *"the rule I am asking you to apply is your own"* y cerraba usando el propio plano del proveedor como prueba de cargo, que se lee como un "te agarré". Ahora abre reconociendo que el criterio ya está acordado y que lo puso BW Water, y cierra en una línea. **El hecho del plano en Rev F con el cajetín de aprobación no se perdió**: se conserva íntegro en la Sección 3 del transmittal, que es el instrumento donde corresponde registrarlo. El correo persuade, el transmittal deja constancia.
- ⚠️ **Queda una nota dura, y es deliberada:** el cierre "without prejudice to ADASA's rights under the Contract". Con el párrafo 2 ya suavizado, es la frase más áspera del correo. Se mantiene porque sin ella ADASA renuncia tácitamente a lo que dejó fuera (Cláusula 6, hito de pago del 10 por ciento, multa de la 43.1 letra a), pero conviene decidirlo a conciencia antes de enviar.
- **La defensa previsible de BW Water es que nunca se le fijó una fecha, y es cierta.** De ahí la frase *"I had not set a date for these reissues until now, and that is what this email fixes"*, que la desactiva antes de que se formule.
- ADASA sí lo pidió una vez, por correo del **07-May-2026** a Eduardo y Andrew Sia, y nunca entró al Registro de Compromisos. Es un defecto propio y por eso no se usa como reproche.
- **Viabilidad:** son 53 documentos en dos días. La salida no es mover la fecha sino la que el correo ya trae: lo que no alcance lleva su fecha comprometida en el DDSR ese mismo día.
- **La minuta de hoy no es oponible** (resumen automático, hablantes sin identificar, cero menciones de la revisión 0 y del DDSR). Por eso el correo dice "in today's meeting we set" y no cita la minuta.
- El **Project Schedule** quedó fuera del reclamo: se retiró del ciclo de transmittals en el N36 y se sigue por la reunión semanal.
- 🔴 **Dos correcciones al registro de ADASA que habrían arruinado el correo** ya están incorporadas: el `P22-CD-09-005-001` está en Rev 0 desde la E71, y la E91 traía la Valve List Rev E y el GA Rev D sin revisar. Lo segundo se resuelve solo, porque este mismo transmittal los dispone, y el párrafo "Three rows move with this transmittal" de la Sección 3 lo declara.
- 🔴 El DDSR declara dos planos en Rev 0 que nunca llegaron. El transmittal lo **pregunta**, no lo afirma.
- Munición no usada: Eduardo confirmó que el procedimiento SAT y el dossier final van en español.

## Checklist pre-envío

- [x] ~~Publicar la carpeta `COMENTARIOS` y pegar el enlace.~~ **Hecho.** Está en el transmittal y en el correo, y los dos se regeneraron.
- [x] ~~Exportar el PDF del transmittal desde Microsoft Word.~~ **Hecho.** 11 páginas, índice resuelto sin marcador de posición, enlace clicable e idéntico.
- [x] ~~Confirmar las tablas en el PDF.~~ **Hecho.** Cero palabras partidas por columna angosta y ninguna fila cortada entre páginas; las 51 filas de la Sección 3 están completas.
- [x] ~~Verificar el enlace después de pegar el cuerpo en Outlook.~~ El correo salió. **Comprobar sobre el respaldo** que el bloque del enlace y las dos viñetas viajaron: en el N38 los tres párrafos salieron íntegros y ese bloque no.
- [ ] Enviar por la cadena de los transmittals, en Reply-To.

## Checklist post-envío

- [x] ~~`BORRADOR` → `ENVIADO`.~~ Hecho, aquí y en el `.md` del transmittal.
- [x] ~~Fijar el `PRG-48` al 11 de septiembre.~~ Hecho. Pasa de SIN FECHA a POR VENCER, y su nota registra que la fecha entra el día en que el correo la comunica.
- [x] ~~Correr `update_register_n39.py`.~~ Hecho. Tally **68 / 19 / 2 / 0**, idéntico al declarado en la cabecera antes de correr, y la fila `P22-CD-09-005-001` corregida a Rev 0 desde la E71. Gate `openpyxl_lint.py` en exit 0.
- [x] ~~Entrada de bitácora, Estado Vigente e Índice de Transmittales.~~ Hecho.
- [ ] 🔴 **Dejar el respaldo del enviado (PDF o `.msg`) en esta carpeta**, y anotar la hora en la Bitácora del README.
