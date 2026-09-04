# Correo de remisión — Transmittal N25

**Estado:** BORRADOR (pendiente de envío)
**Fecha:** 29-Jun-2026 (lunes)
**Cadena:** thread regular de transmittals (no Reply-To a un thread de proveedor)
**Archivo:** `2026-06-29_Transmittal-N25.docx` | Script: `crear_correo_tm25.py`

## Qué remite

Transmittal N25 (P22-TM-09-000-025-0) — submittals 25007-0055 (E55) + 25007-0056 (E56), 6 documentos.

**Veredicto: 3 — To Be Revised. Tally 4 Code 1 + 1 Code 2 + 1 Code 3.**

| Documento | Rev | Code | Nota |
|-----------|-----|------|------|
| IO List | 4 | **2** | Las 4 señales de coordinación con el PLC externo CUMPLIDAS (cierra OBS-01 N24). Única nota: celda de conteo dosificadoras (menor, fold a Rev 0). Sin Rev 5 |
| LCP Datasheet | 1 | 1 | Cierra N24 (UPS sheet 114 + código unificado) |
| Static Mixer | 0 | 1 | Cierra N22 (reconcilia condiciones de diseño) |
| Outline Panel Drawing | B | **3** | Gate de fabricación: enclosure material aún contradictorio. Re-issue Rev C. **Único driver del veredicto 3** |
| UHPRO Structural | B | 1 | Cierra N23 (NCh 2369:2003 + criterios de izaje) |
| Painting Spec | C | 1 | Jotun condicionado a equivalencia + cambio de código 005-002→006-002 |

2 CC_ADASA adjuntos (IO List Code 2 + Outline Code 3). Los 4 Code 1 sin anotación.

## Escalación incluida (lo nuevo de este correo)

Párrafo "Outstanding deliverables" enumera los vencidos con deadline consolidado **viernes 03-Jul-2026**:
- Grounding Layout Rev F (venció 17-Jun, 12 días)
- Tabla FAT/SAT (venció 15-Jun, 14 días)
- Hijos del Control Philosophy (6º ciclo, gatea el paquete de control)
- 3 planos mecánicos de ruta (vencieron 26-Jun)

## Contexto Interno (No enviar)

- **El gate de fabricación del Outline sigue abierto** — driver contractual del veredicto. BW Water "medio corrigió": agregó "Exterior SUS316L" + A/C sellado + peso, pero la fila MATERIAL aún lista frame/roof/rear panel/door como sheet steel bajo "interior only" (incluyendo superficies expuestas), contradiciendo el datasheet (FS66S SS316L unpainted). Su propia Consolidated Comment Sheet (pág 12 del PDF) dice "sheet steel only for interior frame and inner door" — pero el plano no lo dibuja así. No se construye de ahí.
- **El Static Mixer y el Painting Spec NO eran "nuevos"** — el cruce con el Master Register lo corrigió: Static Mixer ya estaba en N22 (Rev C Code 2-AN), Painting Spec en N11 (Rev B Code 1, código 005-002). El workflow los revisó como nuevos por mi premisa errónea; corregido en el transmittal.
- **HART / CIP filter / ASME** cerrados, NO se reabren.
- **Las 2 señales FAULT + LOCAL/REMOTE** son pedido nuevo de ADASA (cerradas como Code 2 en N24, ahora incorporadas correctamente en Rev 4) — no imputar incumplimiento.
- **Re-verdict IO List Code 3→Code 2 (revisión del usuario 29-Jun).** El Code 3 inicial lo gatilló una OBS-01 mía (RUNNING dosificadoras = "soft BOOL desde HMI, no feedback real") que era **over-reach con premisa falsa**: esa señal nunca fue hardwired aceptado — ADASA misma pidió relabelearla DI→soft en N20 NOTE-02, hecho en Rev 3, y N24 NOTE-01 declaró el esquema Ethernet/IP "no se reabre". Retirada la OBS-01; queda solo la celda de conteo (OBS-02 N24, menor) + una NOTE de confirmación de fuente. Las 4 señales de coordinación están cumplidas → Code 2. El Outline queda como único driver del veredicto 3. Ver `project_senales_interfaz` / `feedback_soft_io_ethernet_aceptado_n20`.
- El correo es 322 palabras (más largo que un TM estándar porque incluye la escalación de vencidos solicitada).

## Pendiente antes de enviar

1. ~~Reemplazar el placeholder del link de descarga de CC_ADASA.~~ **RESUELTO (decisión usuario 29-Jun):** se **quitó el link** del transmittal; los 2 CC_ADASA (Outline 3,44 MB + IO List 1,35 MB = 4,8 MB) **se adjuntan directo** al correo. Transmittal regenerado sin hipervínculo (verificado: 0 `w:hyperlink`, URL Synology eliminado).
2. **Adjuntar al correo:** el `.docx` (o PDF) del transmittal N25 + los 2 CC_ADASA (`P22-LI-09-008-001_4_IO_List_CC_ADASA.pdf`, `P22-CD-09-008-001_B_Outline_Panel_CC_ADASA.pdf`).
3. Tras envío: marcar este `.md` como ENVIADO, dejar respaldo (PDF/.msg), actualizar README §8/§9.
