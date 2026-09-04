# Correo — Fedco: reporte formal de causas pendiente

**Estado:** ENVIADO 29-Jun-2026 (respaldo `Re: 25007 Taltal - Schedule Update.pdf` en la carpeta)
**Fecha:** 29-Jun-2026 (lunes)
**Cadena:** **Reply-All al thread "25007 Taltal - Schedule Update"** (correo de Yamauchi del 26-Jun) — cadena separada de los transmittals y del thread Meeting Notes 16-Jun.
**To:** Eduardo Yamauchi + equipo BW Water del 26-Jun (Gehant, Adzlan, Jeryl, Lokman, Sadeep, Nick). **CC:** Victor Gutierrez (ADASA).
**Archivo:** `2026-06-29_Fedco-Root-Cause-Report-Request.docx` | Script: `crear_correo_fedco_root_cause.py`
**Deadline pedido:** viernes **03-Jul-2026**.

## Qué exige y por qué

ADASA pidió el **25-Jun** (encuadrado como compromiso de la call del 23-Jun) DOS entregables: (1) cronograma re-secuenciado que **absorbe** el slip y (2) **reporte formal de causas** (root cause + sequence of events + recovery actions). BW Water respondió el **26-Jun** con solo el cronograma (que **propaga** el slip: shipping 15-Ago→10-Sep) + una **narrativa en el cuerpo del correo** — no el reporte formal. El "Progress Update" PDF es solo el Gantt impreso (verificado por extracción). El reporte formal **sigue pendiente**.

El correo exige el reporte formal por 03-Jul con 4 contenidos: (1) fecha única conciliada con **respaldo documental del vendor** (carta/PO Fedco, no "as advised"); (2) causa raíz + secuencia con fechas/documentos; (3) acciones de recuperación + decisión del **lugar del running test** (Penang vs SAT en sitio) con personal/ventana/costo; (4) plan de ruta crítica del **LCP panel** (debe llegar antes del FAT 19-Ago-08-Sep).

ADASA necesita el reporte formal —no un párrafo en un cover email— para reportar el retraso a su mandante con la causa bien sustentada y blindar la trazabilidad contractual (multas BAE Cl.27/43.1, gatillo de terminación a los 30 días Cl.206).

## Postura (decisiones del usuario 29-Jun)

- **Firme + reservar posición**, con referencia **medida** al régimen de atraso ("the basis on which the delay is assessed under the contract", "reserves all of its rights") — **sin citar números de cláusula de multa/terminación**, sin acusar.
- **Atribución al down-payment:** BW Water atribuye el slip al *"delayed down payment received on 09 June"* (el anticipo 30% que ADASA fijó como su costo). El correo **PIDE SUSTANCIACIÓN sin rechazar** (punto 2): que el reporte documente la cadena (PO Fedco, términos de pago, dependencia anticipo↔orden, fechas); ADASA **reserva su posición** sobre responsabilidad y "does not accept any allocation by implication". **La disputa del anticipo se deja para una vía contractual separada** (no se litiga aquí).

## Contexto Interno (No enviar)

- **02-Sep (Penang) es posterior al 21-Ago ya rechazado por escrito el 17-Jun** y reabre el conflicto FAT/running-test integrado (NT-001): si la bomba llega tras la ventana de despacho, el running test integrado no cabe en Penang. El correo lo señala.
- **El cronograma propaga, no absorbe** — el pedido del 25-Jun (y la lista del 22-Jun) era un cronograma que demuestre cómo se absorbe el slip dentro del Performance Test; el 26-Jun solo promete "monitorear".
- **Sin respaldo documental del vendor**: la fecha viene "as advised by the supplier" / "supplier has confirmed", sin carta/PO Fedco adjunta.
- **No se litiga el anticipo** (decisión del usuario): la postura adversa de BW Water (causa = down payment de ADASA) se neutraliza pidiendo sustanciación + reservando posición, no rechazando. Vía contractual del anticipo, aparte.
- Verificación: workflow `fedco-email-audit` (factual/anti-fabricación + postura + contractual + tono/anti-IA) + `anti-ia revisar`.

## Pendiente antes de enviar

1. Aplicar las correcciones obligatorias del workflow de auditoría (si las hay) + anti-ia VERDE.
2. Verificar adjunto si se quiere referenciar (este correo no adjunta nada — exige el reporte; opcional re-adjuntar la solicitud del 25-Jun).
3. Tras envío: marcar este `.md` ENVIADO, dejar respaldo (PDF/.msg), actualizar README §8/§9 + memoria `project_fedco_fat_conflict_14may`.
