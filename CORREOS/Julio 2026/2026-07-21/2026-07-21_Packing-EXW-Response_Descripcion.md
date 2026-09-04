# Correo — Taltal Equipment Dispatch (EXW) / Packing Cost: ADASA Response

**Estado:** BORRADOR (21-Jul-2026)
**Fecha:** 21-Jul-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water)
**Cadena:** **Reply-To** al thread "20.25.6501 TALTAL: RFQ FOR PACKING COST" (reenvío de Eduardo del 20-jul 21:00 con el plan de despacho de Faizah Bardan). Cadena SEPARADA del correo del panel PLC/LCP del mismo día.
**Script:** `crear_correo_packing_exw_response.py` · **Output:** `2026-07-21_Packing-EXW-Response.docx`

## Cuerpo (resumen)

1. Acusa el plan de despacho desde Penang (3 bultos, EXW): 40' HC (UHPRO containerizado), 20' GP (equipo suelto), 20' flat rack (estanque CIP).
2. **Confirma el alcance logístico EXW de ADASA:** aportar el 20' GP vía side-loader, haulage del 40' HC y del 20' flat rack, y freight forwarding / transporte interno / aduana / flete marítimo desde el patio BWW. Pide el loading schedule y el vessel closing date para posicionar el contenedor 2-3 días antes y alinear el haulage con la grúa de 1 día que arregla BWW.
3. **Reserva el packing cost:** bajo EXW (Incoterms) el embalaje y marcado para exportación en el punto Ex-Works son alcance y costo del vendedor. Antes de considerar cualquier cargo, pide a BW confirmar si pretende cargar un packing cost a ADASA y, en tal caso, la base contractual. Reserva de derechos, sin perjuicio de la coordinación logística.

## Verificación de fuentes

- Contenido del correo entrante VERIFICADO por extracción directa del PDF `CORREOS/Fw 20.25.6501 TALTAL RFQ FOR PACKING COST.pdf` (reparto de alcance BWW/ADASA verbatim del correo de Faizah Bardan, 16-jul).
- **"20.25.6501" = número de proyecto interno de BW Water para Taltal** (equivalente a "25007" de ADASA), NO una cotización — confirmado contra Progress Report Week 28, PO Fedco M183 e ITP Offsite (todos citan "Project No: 20.25.6501"). Por eso NO se trata como referencia comercial en el correo.
- Incoterm **EXW Penang** confirmado en el cronograma vigente y memorias de procurement (`project-procurement-22jun`, `reference_unpriced_po_mapping`).

## Contexto Interno (No enviar)

- El correo NO es respuesta a un correo de ADASA: lo inicia BW Water (es el "Ex Work shipment details" comprometido en la reunión del 16-jun). ADASA responde para (a) confirmar lo que sí es su alcance y (b) fijar una reserva temprana sobre el packing cost antes de que se convierta en una factura o change order.
- **Ángulo comercial:** bajo EXW el packing de exportación es del vendedor. Precedente útil: en nov-2025 ADASA rechazó cotizar un 20ft adicional con equipos (USD 67.208) y se quedó con el schedule original de BW → hay historia de no absorber costos extra de logística que BW intente agregar. NO conceder el packing cost por defecto.
- No confundir con la Cotización de Repuestos 2 años (ref. BWWA 20.24.6501.F Rev.1), que es un documento distinto con su propio deadline de reemisión (31-jul).
- Este despacho corresponde a la ventana de RFS del módulo (~7-12 sep, ligada al recovery del panel y a la bomba HP Fedco). No comprometer fechas de posicionamiento del contenedor hasta que BW entregue el loading schedule / vessel closing date.
- Enviar como Reply-To a la cadena del packing; NO fusionar con el correo del panel (cadena separada, CLAUDE.md 3.3.1/3.4).

## Checklist pre-envío

- [ ] To/CC correctos (Eduardo + Stephane Gehant / Faizah Bardan / Lokman Hakim + Victor Gutierrez por ADASA)
- [ ] Asunto exacto "RE: 20.25.6501 TALTAL: RFQ FOR PACKING COST"
- [ ] 100% inglés; sin símbolo de sección; sin Van Doorn ni códigos internos
- [ ] `anti-ia revisar` sin frases-firma prohibidas
- [ ] Metadatos Word limpios (autor Luis Rivera Gonzalez / company Aguas de Antofagasta / en-US)
- [ ] Tras envío: BORRADOR → ENVIADO, respaldo PDF/.msg, actualizar README
