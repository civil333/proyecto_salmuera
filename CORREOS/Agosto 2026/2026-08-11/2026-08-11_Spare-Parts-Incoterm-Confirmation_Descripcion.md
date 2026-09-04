# Correo — Two-Year Spare Parts Package: Incoterm Confirmation

**Estado:** BORRADOR (11-Ago-2026)
**Fecha:** 11-Ago-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi, Andrea Frezzi (BW Water)
**CC:** Jorge Guevara, Victor Gutiérrez (ADASA); Stephane Gehant (BW Water)
**Cadena:** **Reply-To** al hilo propio "Formal Re-validation of Spare Parts Quotation C4300", donde llegó la propuesta formal el 28-Jul. Cadena separada de los transmittals y del hilo de packing/EXW del módulo.
**Formato:** ejecutivo, 213 palabras, con dos recortes del propio PDF de BW Water incrustados.
**Scripts:** `generar_figuras_incoterm.py` (recortes) → `crear_correo_incoterm_repuestos.py` (Word) · **Output:** `2026-08-11_Spare-Parts-Incoterm-Confirmation.docx`

## Cuerpo

1. **Abre atribuyendo el tema:** Eduardo levantó el punto de entrega del paquete de repuestos en la reunión semanal de coordinación de hoy, entendiendo que la cotización muestra varios puntos de entrega en lugar de un embarque único consolidado desde Penang. Cierra el párrafo agradeciendo la cotización formal del 28-Jul.
2. **"Your proposal states a single Incoterm for the package:"** seguido de la **figura 1**.
3. Una frase sobre el Anexo A: la columna Incoterms lleva los términos de suministro de cada sub-proveedor y la columna contigua asigna dos semanas de tránsito a lo que viene de España, China y Estados Unidos y cero a lo ya cotizado DDP Penang, de modo que todas las líneas convergen en Penang. Seguido de la **figura 2**.
4. **"A reissue is not needed; please confirm in writing:"** con los tres puntos: (a) EXW Penang aplica al paquete completo; (b) el total se mantiene en USD 51.224,50 con consolidación y transporte a Penang incluidos; (c) una fecha única de disponibilidad en Penang, en semanas calendario desde la orden de compra.
5. ADASA está lista para emitir la orden de compra y la cotización vence el 28-Ago-2026; diez semanas de fabricación más dos de tránsito dejan el paquete en Penang holgadamente dentro del plazo contractual de 510 días corridos.
6. Respuesta pedida para el **jueves 13-Ago-2026**. Sin proponer reunión.

## Figuras

Recortes **crudos**, sin resaltados ni marcas añadidas: la evidencia es un extracto intacto del documento del proveedor. Generados a 300 DPI con PyMuPDF desde `PROGRAMA y CONTRATO/REPUESTOS DE 2 AÑOS/propuesta formal/Proposal 25007-PL-0002_rev.0 - 2y spare parts_s.pdf`, que el script solo lee.

| Figura | Origen | Contenido | Tamaño en el Word |
|---|---|---|---|
| `figuras/fig1_commercial_conditions.png` | Página 1 | Payment Terms, **Incoterms: EXW Penang, Malaysia**, y validez hasta el 28-Ago-2026 | 5,5" × 2,19" |
| `figuras/fig2_annexA_incoterms.png` | Página 3 | Encabezado del Anexo A y once líneas, con la columna Incoterms mostrando DDP Penang, EXW Hengshui (China), EXW Mungia (España) y EXW Michigan (EE.UU.), junto a la columna Estimated Transit Time con 2 semanas y 0 | 6,4" × 3,56" |

Las coordenadas del recorte se resuelven con `page.search_for()` en tiempo de ejecución, no hardcodeadas, de modo que el script sobrevive a una reemisión del PDF. Los recuadros amarillos de la figura 2 son de BW Water (marcan sus long-lead items), no de ADASA.

**Cuidado propio de este PDF:** la página 1 usa una fuente con codificación desplazada en ASCII y la extracción de texto devuelve los encabezados ilegibles, aunque el render sale correcto. Por eso las dos figuras se validaron abriendo los PNG, no leyendo el texto extraído.

## Verificación de fuentes

| Dato del correo | Fuente |
|---|---|
| Incoterm único "EXW Penang, Malaysia" y validez al 28-Ago-2026 | Página 1 de la propuesta, incrustada como figura 1 |
| Columna Incoterms con cinco orígenes y columna Estimated Transit Time (2 semanas / 0) | Anexo A, página 3, incrustada como figura 2 |
| Total USD 51.224,50 | Total del Anexo A y encabezado descifrado, verificados por dos caminos en `_ANALISIS_COMERCIAL_04AGO.md` |
| Lead time máximo de diez semanas (manómetros Monel) más dos de tránsito | Anexo A, columnas Lead Time y Estimated Transit Time |
| Plazo contractual de 510 días corridos | `PROGRAMA y CONTRATO/md/CONTRATO-C4300-BWWATER-SUMINISTRO.md` |
| Punto levantado hoy y acción de consolidar en Penang | Nota de la reunión del 11-Ago-2026 (documento interno de ADASA, no se cita en el correo) |

## Contexto Interno (No enviar)

- **El riesgo que gobierna la redacción es el precio, no el Incoterm.** La columna de precio unitario del Anexo A dice "Unit Price (USD) EXW terms". Una Rev.1 "consolidada" habilita a BW Water a cargar el flete a Penang y subir el total, después de que ADASA formalizó exactamente USD 51.224,50 dentro de la Carta de Aumento de Monto del 04-Ago (USD 56.990,50 = repuestos 51.224,50 + adicional CIP `25007-PL-0001` rev.3 5.766,00). Por eso se pide confirmación escrita y **no** reemisión, y el punto (b) fija el total.
- **Alcance logístico, si lo preguntan:** paquete único consolidado en Penang, un embarque de exportación, una internación y una tramitación aduanera en Chile, dentro del alcance que ADASA ya cubre para el módulo bajo EXW. Salió del cuerpo al comprimir a formato ejecutivo; se responde si BW Water lo consulta.
- **Un solo eje, por decisión de método.** Quedan fuera y van en correo aparte antes del 28-Ago: las once líneas mal correspondidas (part number MSD-130 contra la bomba Fedco MSD-7016; *Service Kit* convertido en *Mechanical Seal* al mismo precio; sensores pH y ORP Foxboro contra los Rosemount 3900 y 1056 instalados; manómetros Monel contra los Wika con sello Superduplex 2507; válvula de bola DN50 y mariposa DN80 en PVC que no existen; 5 repuestos DN40 contra 1 válvula instalada), las cuatro alzas de 43% a 372%, la diferencia de USD 1.240 de la oferta de septiembre de 2025 y la ausencia de repuestos para las 64 válvulas de bola DN15. La figura 2 muestra algunas de esas líneas, pero el correo no las comenta: mezclarlas permitiría refundir todo en una reemisión re-cotizada.
- **No se ofrece extensión de plazo.** El planteamiento de que consolidar en Penang "may affect the contract duration" se refuta con las cifras de la propia propuesta. Si BW Water insiste por escrito, se trata como instrumento separado.
- **El módulo embarca de Penang alrededor del 19 al 21 de septiembre**, antes de que los repuestos estén listos. La consolidación implica un segundo despacho desde Penang, que ADASA asume bajo EXW igual que el del módulo. No comprometer fechas de posicionamiento ni de flete hasta tener la confirmación del punto (c).
- **No se aborda el reclamo de BW Water** de que la carta de aumento de monto no trae detalle de alcance. Si lo repiten por escrito, la respuesta es que el alcance son el Anexo A de la `25007-PL-0002` rev.0 y el adicional CIP `25007-PL-0001` rev.3, y esa composición conviene declararla recién cuando el fondo esté resuelto.
- La nota de la reunión de hoy es un documento interno de ADASA generado por transcripción asistida, no un acta de BW Water: el correo dice "today's meeting", sin citarla como documento.

## Checklist pre-envío

- [ ] To/CC correctos (Eduardo Yamauchi + Andrea Frezzi; CC Jorge Guevara, Victor Gutiérrez, Stephane Gehant)
- [ ] Asunto exacto "RE: Formal Re-validation of Spare Parts Quotation C4300" y envío como Reply al hilo, no como correo nuevo
- [ ] **Al pegar en Outlook, confirmar que las dos imágenes viajan en el cuerpo.** Precedente propio: un enlace de descarga no sobrevivió al pegado y hubo que verificarlo sobre el correo enviado, no sobre el borrador
- [x] Los dos PNG abiertos y leídos antes de insertarlos: la figura 1 muestra "Incoterms — EXW Penang, Malaysia" completo; la figura 2, la fila de encabezado con "Incoterms" y "Estimated Transit Time" más las cuatro variantes de origen
- [x] 100% inglés; sin símbolo de sección; sin Van Doorn, códigos de observación ni la palabra "letter" (barrido ejecutado, 0 coincidencias)
- [x] Barrido anti-IA: sin em dash en el cuerpo, sin relleno estructural, oración más larga de 34 palabras. Se reemplazó "Rather than reissuing the document" por "A reissue is not needed" para no rozar la antítesis retórica (U-01)
- [x] Cuerpo de 194 palabras y dos imágenes efectivamente incrustadas
- [x] Metadatos Word limpios (autor Luis Rivera Gonzalez, company Aguas Antofagasta, en-US)
- [x] Cifras cotejadas: USD 51.224,50 · validez 28-Ago-2026 · diez semanas más dos de tránsito · 510 días corridos
- [x] Día de la semana verificado: 13-Ago-2026 es jueves (deadline de respuesta) y 28-Ago-2026 es viernes (vencimiento de la validez)
- [ ] Tras envío: BORRADOR → ENVIADO, respaldo PDF o `.msg` en esta carpeta, entrada nueva arriba en la Bitácora del README y actualización del frente comercial en Estado Vigente
