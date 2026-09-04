# Correo de cobertura — Transmittal N34

**Estado:** ENVIADO el 18-Ago-2026 (hora de Chile por registrar desde el respaldo)
**Fecha:** 18-Ago-2026
**Archivos:** `2026-08-18_Transmittal-N34.docx` · `.pdf`
**Generador:** `crear_correo_tm34.py`
**PDF:** `exportar_pdf_word_mac.sh` (Word real; el paso va por el contenedor de Word)
**Cadena:** hilo de los submittals (la misma de los transmittals). NO es Reply-To del
hilo del endoso profesional, que corre por separado ese mismo dia.

## Destinatarios

- **To:** Allan Valentos, Eduardo Yamauchi (BW Water)
- **CC:** Fitri Indriyani, Stephane Gehant, Magdier Arias, Muhammad Fadhil Bin Abdul
  Wahid (BW Water); Victor Gutierrez, Jorge Guevara, Ronald Pellejero (ADASA)
- **Asunto:** TALTAL - Transmittal N34 - submittals 25007-0073, 25007-0077 and 25007-0080

## Resumen del cuerpo

**Directo: 156 palabras de prosa en cuatro parrafos**, oracion maxima de 21, una
pagina. El pedido del usuario fue que el correo **no detalle el documento adjunto**.

1. **Veredicto.** Transmittal N34, tres submittals, cinco documentos.
   3 — To be revised: 2 Codigo 1, 2 Codigo 2, 1 Codigo 3.
2. **Que solo un documento vuelve a revision**, el Quality Dossier Index Rev B; que
   los dos planos son Codigo 2 e incorporan su punto al emitir Rev 0 sin nueva
   revision; que los dos Rev 0 no requieren accion. Cierra con "the transmittal states
   what each one requires": el detalle vive en el adjunto y en los tres `CC_ADASA`.
3. **Lo unico que cae FUERA del transmittal**, y por eso si va en el cuerpo: ADASA
   declara el rango vinculante de `VT-09-001` en 0 a 12 mm/s rms y pide reemitir la
   Instrument List, para que el disparo por vibracion de la bomba de alta pueda actuar.
4. **Recepcion de las submittals 0073 y 0077** y el plazo de la Clausula 37.2
   (20 y 27 de agosto).

**Lo que se saco a proposito** en esta version: por que C21 no es el Acta de
Aprobacion FAT, las cifras del Fz por perno, la discrepancia Manhole contra Handhole
y el estado de las columnas del indice. Todo eso es contenido del transmittal.

## Verificacion de fuentes

| Afirmacion del cuerpo | Verificado contra |
|---|---|
| C21 es la fila 8.4 y el Acta de Aprobacion FAT es la 7.9 | ITP `P22-BA-09-000-004` Rev 0, filas 7.9 y 8.4; ET `P22-ET-09-000-001-0` Seccion 8 |
| Indice preliminar 7.6 contra indice final 8.3 | ITP Rev 0: `PROV-LIST-DOSS-PRE-001` y `PROV-LIST-DOSS-FIN-001` |
| Instrument List Rev E en 0 a 8,9 mm/s rms | `P22-LI-09-008-003` Rev E, fila 7, Wilcoxon PCH420V-M12 |
| Alarm List Rev 0 en 0 a 12,0 con disparo en 10,0 | `P22-LI-09-008-015` Rev 0, items 6.0 y 6.1 |
| Fz por perno 0,205 contra total 1,0242 sobre 10 pernos | Render a 300 dpi de `P22-DWG-09-005-011` Rev C, notas 7.2 y 7.9.1 |
| Manhole 533 mm contra Handhole DN300 | GA `P22-DWG-09-005-014` Rev B y Datasheet `P22-ET-09-009-009` Rev B |
| Fechas de la Clausula 37.2 | Recepcion efectiva: 0073 el 11-Ago, 0077 el 18-Ago 07:49, 0080 el 18-Ago 09:58 |
| **Enlace de descarga** | Verificado **sobre el `.docx` y el `.pdf` emitidos**, texto visible y destino del hipervinculo, no sobre el script |

## Contexto Interno (No enviar)

- **El veredicto de la Alarm and Interlock List se corrigio antes de emitir.** La
  primera version la dispuso en Codigo 3 y era over-reach: ante un Rev 0 el defecto
  que vive en otro documento no degrada. Su `CC_ADASA` quedo en
  `REVISIONES/TRANSMITTALES/P22-TM-09-000-034-0/_analisis_no_anotado/`.
- **Los dos TAG mal formados** (`VE09-014-XT001` y `VE09-016-XT001`) van solo como una
  linea del bloque de accion del transmittal, no en el correo. Housekeeping.
- **Lo que se retiro y no se emite** esta tabulado en la Seccion 9 de
  `_ANALISIS_N34.md`.
- **No se abre** el eje del plazo de entrega vencido ni la multa de la Clausula 43.1
  letra b): es otra cadena, y el correo del endoso del mismo dia tampoco los abre.

## Checklist pre-envio

- [x] Enlace verificado sobre el `.docx` y el `.pdf` emitidos
- [x] Tres `CC_ADASA` nombrados en el cuerpo y presentes en la carpeta publicada
- [x] Fecha de carpeta igual a la fecha del encabezado (18-Ago-2026)
- [x] Idioma `en-US` fijado; metadatos con autoria y compania
- [x] Cero simbolo de seccion
- [ ] Abrir el enlace y confirmar que la carpeta muestra el transmittal y los tres PDF
- [ ] Confirmar que la cadena es el hilo de submittals y no el del endoso

## Checklist post-envio

- [x] Cambiar BORRADOR por ENVIADO (hora pendiente de registrar desde el respaldo)
- [ ] Archivar el respaldo del enviado en esta carpeta
- [x] Master Deliverable Register con `update_register_n34.py` (backup _pre-N34.xlsx del 18-Ago 11:16)
- [x] Registro de compromisos: reemision de la Instrument List (PRG-33)
- [x] Bitacora del README y correccion del Estado Vigente (las submittals 0073 y 0077
      si existen; la serie no tiene numeros ausentes; 80 entregas)
