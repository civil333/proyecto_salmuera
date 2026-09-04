---
titulo: "Correo de cobertura — Transmittal N28 (familia de Control) a BW Water"
codigo: "Notificación de transmittal P22-TM-09-000-028-0"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-07-20
---

# Correo — Cobertura del Transmittal N28 (documentos de Control) a BW Water

**Estado:** ENVIADO (20-Jul-2026; cadena regular de transmittals). Link Synology del TM N28 incluido en el transmittal y en el correo. PDF del transmittal generado desde Word (TOC refrescado) con `exportar_pdf_word_mac.sh` (§3.13 del CLAUDE.md) y paquete subido a Synology.
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water) · **CC:** Andrew Sia, Victor Gutierrez, Jeryl Regulacion, Jorge Guevara, Ronald Pellejero, Stephane Gehant.
**Script:** `crear_correo_tm28.py` · **Output:** `2026-07-20_Transmittal-N28.docx`

## Cuerpo (resumen)

Notifica el TM N28 (P22-TM-09-000-028-0, submittals 25007-0065 + 25007-0066), los 4 documentos de la familia de Control (Control Philosophy Rev E, Alarm & Interlock List Rev C, Control & Sequence Chart Rev A nuevo, IO List Rev 5). **Veredicto 2 — Approved as Noted (4 Code 2).** Pide re-emitir los 4 como **conjunto coordinado a Rev 0** con dos definiciones fijadas: (1) mapeo winding/bearing (winding TE-09-001, bearing TE-09-002, como ya lo tienen Alarm List/IO List/Instrument List, pero la CP lo invierte); (2) un único trip de vibración de la bomba HP alcanzable (el Alarm List lo pone en 10.0 sobre un transmisor de rango 8.9). Re-escala los 3 vencidos que son la ruta al set de control Rev 0: HP/LP Pressure Test Rev D (75 bar sobre PVC), O&M Manual Rev B, UHPRO Structural Calc Rev B, deadline **viernes 31-Jul-2026**. Cierre "look forward to your comments" + link Synology.

## Verificación

- Metadatos limpios (creator "Luis Rivera Gonzalez", company "Aguas Antofagasta", en-US).
- Sin em-dash en prosa (solo cabecera/firma), sin `§`.
- Días verificados: 20-Jul = lunes; 31-Jul = viernes.
- Coherente con el transmittal (mismo veredicto, mismas dos definiciones, mismos 3 vencidos).

## Contexto Interno (No enviar)

- La palanca del correo es el **conjunto coordinado a Rev 0** (para evitar que los 4 vayan a Rev 0 sin reconciliar entre sí y quede la circularidad de "alinear entre ellos"). Las dos definiciones (winding/bearing + trip de vibración) son las que hoy no están cerradas en ningún documento; sin ellas la reconciliación no es determinista.
- El detalle por documento vive en los 4 CC_ADASA (todos Code 2). El análisis interno de disposición está en `REVISIONES/TRANSMITTALES/P22-TM-09-000-028-0/_ANALISIS_N28.md` (NO enviar; incluye la clasificación punto-por-punto propio vs cross-doc que bajó los 4 a Code 2 por regla del usuario).
- La condición de firma RTD del FAT (N27) queda abierta en Sección 3 hasta que la CP Rev 0 refleje el mapeo (los hijos ya lo tienen). El O&M (N27 Code 3) sigue gated.

## Checklist pre-envío

- [x] Transmittal .docx + .md generados, barridos `§`=0 / Van Doorn=0, prosa "Why" sin em-dash
- [x] 4 CC_ADASA generados y verificados por render (placement + legibilidad; confirman los hallazgos)
- [x] Master Register a N28 (`update_register_n28.py`): 108 items / 84 delivered · 48/28/8/0 · 28 TMs / 66 entregas
- [x] Correo de cobertura + metadatos limpios
- [x] `DOWNLOAD_LINK` del TM N28 incluido en `crear_transmittal.py` (re-generado) y en el correo (clicable)
- [x] PDF del transmittal desde Word (TOC refrescado, `exportar_pdf_word_mac.sh`) + paquete (transmittal + 4 CC_ADASA) subido a Synology
- [x] **ENVIADO 20-Jul-2026**; README + memorias actualizados. Pendiente menor: dejar respaldo (PDF/.msg) del envío en la carpeta
