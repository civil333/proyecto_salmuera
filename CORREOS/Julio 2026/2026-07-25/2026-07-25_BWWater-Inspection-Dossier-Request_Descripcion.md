---
titulo: "Correo ADASA → BW Water — Dossier de fabricación y pruebas no entregado (inspección Bureau Veritas)"
codigo: "Correo de coordinación (sin código ADASA)"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-07-25
---

# Correo — Dossier de fabricación y pruebas para la revisión de Bureau Veritas

**Estado:** ENVIADO el sábado 25-Jul-2026 09:03 (hora Chile)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi, Stephane Gehant, Magdier Arias, Lokman Hakim Mat (BW Water)
**CC:** ninguno
**Cadena:** enviado como **RV del hilo "25007 TALTAL - Request to witness inspection 001"**, no como reply-all al thread de designación del inspector. Bureau Veritas queda fuera del hilo (el Request 001 original sí los tenía como destinatarios). Inglés. Respaldo: `RV: 25007 TALTAL -  Request to witness inspection 001.pdf` en esta carpeta.

> **Divergencias vs el borrador planificado** (registradas para trazabilidad, no requieren acción): (1) cadena = hilo del Request 001 en vez del thread de designación, lo que deja el reclamo dentro de la conversación que lo originó y sin exposición al inspector; (2) sin CC — el equipo ADASA (Gutiérrez, Guevara, Pellejero) y Mohd Adnin Zulkifli, emisor del Request 001, no quedaron en copia; (3) al pegar en Outlook el punto del dossier perdió su número y los tres restantes quedaron numerados 1, 2 y 3.
**Script:** `crear_correo_dossier_inspeccion.py` · **Output:** `2026-07-25_BWWater-Inspection-Dossier-Request.docx`

## Cuerpo (resumen)

Acusa la Inspection Request 001 (PMI de super duplex el 28-Jul) y confirma la asistencia del inspector. Abre cuatro puntos:

1. **El dossier de fabricación y pruebas sigue sin entregarse.** Se funda en la obligación contractual, no en el compromiso de fecha: entregable de la ET P22-ET-09-000-001-0, Section 7 (máximo 90 días desde la adjudicación, con los certificados de fabricación de los aceros super duplex) y documento que ADASA revisa bajo el item 7.6 del Inspection and Testing Base Plan P22-IT-09-000-001-0; el contenido es la lista que BW Water presentó en la Quality Kick-off Meeting. Registra que la fecha del viernes 24-Jul, dejada por escrito en el correo del 21-Jul, venció sin entrega. Pide en dos tramos: **lunes 27-Jul** el índice del dossier más los registros que sostienen la primera semana (MTR y trazabilidad de los spools super duplex, calibración del equipo PMI con los certificados del técnico, y WPS/PQR con las calificaciones de soldadores de las juntas ya soldadas desde mediados de julio, porque la soldadura arrancó antes de abrirse la ventana de inspección); **viernes 31-Jul** el dossier preliminar completo. Cierra vinculándolo a los items 8.3 y 8.4 (aprobación final del dossier y Release for Dispatch, que soporta el 40%) y pide confirmar que los registros de las pruebas FEDCO se incorporan a ese dossier.
2. **Los documentos entregados al inspector no son las revisiones vigentes.** La Request 001 adjuntó el ITP en Rev C, superada por la Rev 0 devuelta en Código 1, y ambos adjuntos son las copias con las anotaciones de revisión de ADASA. Pide reemitir a Bureau Veritas las revisiones limpias vigentes antes de la jornada del 28-Jul, con el paquete de inspección del 21-Jul como referencia.
3. **Alcance de la Semana 1 y plazo de notificación.** Una jornada notificada de las tres comunicadas el 21-Jul, y la calificación de soldadores movida al 7-Ago. Pide notificar las jornadas 2 y 3 con su alcance y confirmar si ese ensayo queda en la Semana 2. Deja asentado que la Request 001 se emitió con 4 días de aviso frente a los 30 de la BAE Cláusula 37: se acepta para la primera visita sin sentar precedente.
4. **Los puntos de reconciliación siguen sin respuesta** (V5 y V6 sobre el programa fijo, FAT y Dispatch Release con el alcance mínimo preservado, Kick-off). Sin esa respuesta ADASA no puede confirmar las visitas 2 a 6 al inspector. Respuesta escrita antes de la reunión semanal del martes 28-Jul.

Cierre: toda desviación del programa fijo debe notificarse por escrito y con antelación, indicando su causa. Sin proponer reunión.

## Verificación de fuentes

- **ET Section 7:** `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md` (línea 1508 y siguientes): 90 días desde la adjudicación; "Dossier de fabricación y pruebas de todos los equipos eléctricos y electromecánicos con sus certificados de fabricación de aceros especiales para los equipos en superduplex".
- **PIE Base:** `BASES TECNICAS/md/P22-IT-09-000-001-0-PIE-BASE.md`: item 7.6 Revisión Documentación Preliminar (Dossier Calidad), intervención ADASA = R; item 8.3 Revisión y Aprobación Final Dossier Calidad = Hold; item 8.4 Liberación para Despacho = Hold.
- **Master Register:** ítem 65 "Manufacturing and Testing Dossier" = `NOT DELIVERED` ("Prerequisite for factory acceptance / ET Sec.7: Max. 90 days from NTP").
- **Contenido del dossier:** lámina QKOM de BW Water, `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/DOCUMENTOS A ENVIA A BV.png` (Required Documentation: MTR y trazabilidad, PMI, WPS/PQR y calificación de soldadores, END, hidrostáticas, coating y DFT, calibraciones, planos, reportes de inspección y MRB).
- **Compromiso del 24-Jul:** `CORREOS/Julio 2026/2026-07-21/crear_correo_tm29.py`, bloque "Near-term commitments" ("By this Friday, 24 July 2026: deliver the shop-inspection dossier for Bureau Veritas' review, as committed").
- **Request 001 y adjuntos:** `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/CORREOS VBV-BW/` (tres correos, 23–24 de julio). Adjuntos declarados: AQ-QAM-F027 Inspection Request, `P22-BA-09-000-006_A_PMI_Procedure_CC_ADASA.pdf`, `P22-BA-09-000-004_C_ITP_CC_ADASA.pdf`. Inspección: 28-Jul, 9:00–17:00, PMI super duplex. BV Malaysia preguntó por el WQT y BW Water respondió 7-Ago.
- **ITP vigente:** Rev 0, Código 1 en el TM N26 (Master Register ítem 92). La Rev C está superada.
- **Días de la semana verificados con `date`:** 24-Jul viernes, 25-Jul sábado, 27-Jul lunes, 28-Jul martes, 31-Jul viernes.

## Contexto Interno (No enviar)

- **Por qué el correo NO lidera con el compromiso de fecha:** el compromiso del viernes 24-Jul no consta por escrito de BW Water; quedó registrado por ADASA en la cobertura del TM N29 del 21-Jul y no fue objetado. La base sólida es la ET Section 7 más el PIE, que convierte el reclamo en entregable contractual vencido, no en promesa incumplida.
- **ADASA también quedó en incumplimiento** de su compromiso del 24-Jul con Bureau Veritas (confirmación final de V2 a V6). Se decidió no escribir a BV en esta pasada; ese correo se emite cuando BW Water reconcilie V5/V6 y el FAT.
- **NO reclamar los tres procedimientos que estaban en Código 3:** 009 Rev C, 010 Rev D y 011 Rev B están los tres en Código 2. El punto 6 del correo de reconciliación quedó cerrado.
- **No se exponen datos comerciales de Bureau Veritas** (25 jornadas contratadas, tarifas, política de cancelación menor a 24 h).
- **Discrepancia de registro pendiente:** el correo de reconciliación figura internamente como enviado el 20-Jul, pero el hilo de Outlook lo muestra enviado el sábado 18-Jul 13:43. El correo lo cita solo como "our previous email", sin fecha, hasta que se confirme.
- **Pendiente conexo:** reemplazar en `PAQUETE_INSPECCION_BV` el Datasheet PLC/HMI Rev C por la Rev 0 aprobada en el TM N30 (Bureau Veritas tiene el paquete desde el 21-Jul).
- **Fecha del correo:** si se envía el lunes en vez del sábado, mover la carpeta y el header a `2026-07-27` y ajustar el plazo del primer tramo.

## Checklist pre-envío

- [x] `anti-ia` modo revisar: **VERDE**. Corregidas 1 activación crítica U-03 (oración de 65 palabras) y 2 alertas (46 y 41 palabras). Métricas finales: 552 palabras, 29 oraciones, media 18,9, sigma 9,2, máximo 42, cero em-dash en prosa
- [x] Barrido `§` = 0; sin referencias internas (Van Doorn, IDs OBS, nombres de archivo `CC_ADASA`)
- [x] Metadatos Word limpios: autor y lastModifiedBy "Luis Rivera Gonzalez", company "Aguas Antofagasta", `comments` explícito, idioma en-US
- [x] Citación ejecutiva: código de la ET y del PIE una sola vez; después "Section 7" e "item 7.6 / 8.3 / 8.4"
- [x] Visto bueno de Luis al borrador
- [x] Confirmar destinatarios exactos en Outlook (reply-all al thread de designación del inspector)
- [x] **ENVIADO 25-Jul-2026 09:03**; `BORRADOR` → `ENVIADO` hecho; README (Estado Vigente + Bitácora) y memoria `project_bureau_veritas_inspection` actualizados
- [x] Respaldo del envío en esta carpeta (`RV: 25007 TALTAL -  Request to witness inspection 001.pdf`)

## Seguimiento abierto tras el envío

| Vence | Qué se espera de BW Water |
|---|---|
| Lun 27-Jul | Índice del dossier + registros de la Semana 1 (MTR/trazabilidad SDX, calibración PMI y certificados del técnico, WPS/PQR y calificación de soldadores) |
| Antes del 28-Jul | Reemisión a Bureau Veritas de las revisiones limpias vigentes (ITP Rev 0, no Rev C) |
| Antes del 28-Jul | Notificación de las jornadas 2 y 3 de la Semana 1 con su alcance |
| Mar 28-Jul (weekly) | Respuesta escrita a la reconciliación: V5/V6 sobre el programa fijo, FAT y Dispatch Release con alcance mínimo preservado, Kick-off |
| Vie 31-Jul | Dossier preliminar completo estructurado contra el índice |

Del cumplimiento del punto de reconciliación depende que ADASA confirme V2 a V6 a Bureau Veritas (compromiso propio vencido el 24-Jul).
