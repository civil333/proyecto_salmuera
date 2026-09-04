---
codigo: CORREO-2026-05-18-TM-N18
autor: Luis Rivera
fecha: 2026-05-18
version: 1.0
estado: ENVIADO
fecha_envio: 2026-05-18
respaldo: "Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf"
---

# Correo: Transmittal N18 — Submittals 25007-0038, 25007-0039, 25007-0040

## Header

| Campo | Valor |
|-------|-------|
| Date | May 18, 2026 |
| From | Luis Rivera — Contract Administrator (ADASA) |
| To | Eduardo Yamauchi — BW Water Americas Inc. |
| CC | Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim |
| Subject | ADASA – Taltal Brine Module: Technical Review Transmittal N18 — Submittals 25007-0038 to 25007-0041 |
| Ref | Contract C-4300 / BAE 12803 / P22-TM-09-000-018-0 |

---

## Cuerpo del Correo

Dear BW Water Project Team,

Attached: Transmittal N18 (P22-TM-09-000-018-0), submittals 25007-0038 to 25007-0041 — five documents.

**Verdict: 3 — To Be Revised.** Tally: 4 Code 1, 1 Code 3. Only **Plant Control Philosophy Rev C** requires a new revision (Rev D); the other four documents are approved as-is, with residual deliverables listed in Section 3 of the transmittal.

**Plant Control Philosophy Rev C — re-issue as Rev D:**

- **HP Pump start permissive (repeat CRITICAL).** Still "VE-09-007 and VE-09-007" (not corrected to VE-09-008) and requires "VE-09-014 fully CLOSED" — VE-09-014 is the antiscalant tank inlet valve, so the PLC blocks HP Pump start during routine refill. Same defect as Transmittal N15 NOTE-20, second consecutive transmittal; recorded for contractual follow-up under Contract C-4300.
- **Core control logic in undelivered child documents.** Sequence Charts, Alarm & Control Setpoint List and Control Matrix remain "SEPARATE DOCUMENT"; the 13-May-2026 tentative date passed. Deliver them with formal codes, revisions and a binding date.

**Approved as-is (Code 1) — deliverables tracked in Section 3:** Valve List Rev D (PSV-09-002 overpressure analysis); P&ID Rev D (closes TM N13 NOTE-01; CIT-09-004 → Instrument List / Line List + loop-response note); AC Thermal Calculation Rev C (closes TM N15 NOTE-02; explicit margin statement); Line List Rev C (closes the two TM N12 notes).

One annotated PDF is attached (Plant Control Philosophy Rev C); the four Code 1 documents carry none.

Please confirm receipt and the target dates for Plant Control Philosophy Rev D and the Section 3 deliverables.

We look forward to your comments.

Best regards,

**Luis Rivera**
Project Engineer
ADASA — Aguas de Antofagasta S.A.

---

## Contexto Interno (No enviar)

- RE-ESCOPEADO 18-May: se añadió E41/25007-0041 P&ID Rev D (Sección 2.5). Submittals 25007-0038..0041, 5 documentos. Correo aún BORRADOR (no enviado), por eso se re-escopeó en vez de crear TM N19.
- RE-DISPOSICIÓN 18-May (criterio ejecutivo del usuario): el código refleja el estado del documento revisado en sí. Si el documento no requiere modificación a sí mismo → Code 1; los entregables sobre otros documentos / análisis separados se trackean en Sección 3 (no degradan a Code 2). Resultado: Valve List Rev D, AC Thermal Rev C, P&ID Rev D bajan de Code 2 → **Code 1**.
- Veredicto global 3 — TO BE REVISED, driver **solo** Plant Control Philosophy Rev C (Code 3). Tally: **4 Code 1** (Valve List Rev D, Line List Rev C, AC Thermal Calc Rev C, P&ID Rev D) **+ 0 Code 2 + 1 Code 3**.
- AC Thermal Rev C → Code 1: verificado verbatim que NO hay error (carga 6.24 kW=1.774 TR, margen 2.04, unidad 2.01 TR +13.3% sobre peak; n+1 confirmado). Solo se pide indicar el margen explícito → "indicar" = Code 1 por la regla del usuario.
- OBS-01 CRITICAL Control Philosophy = repetición de TM N15 NOTE-20 (2º transmittal consecutivo). Condición bloqueante + registro para seguimiento contractual C-4300.
- Code 2 NO se usa en TM N18; sigue existiendo en la metodología para casos reales donde el propio documento tiene un error/cambio menor a incorporar en Rev 0. Regla refinada codificada en CLAUDE.md secciones 6.2/6.3 (v6.11).
- Cierres logrados: TM N12 NOTE-01/02 (Line List Rev C), TM N15 NOTE-02 (AC Thermal Rev C), TM N13 NOTE-01 (P&ID Rev D), y parte de TM N15 Sección 2.10 (NOTE-14/15/18/19/21/23).
- anti-ia: VERDE confianza Alta (2 rondas). multi-audit: 2 rondas de 8 agentes, sin contenido FABRICADO, confianza veracidad ALTO; obligatorias aplicadas en ambas.
- Van Doorn: no aplica (5 docs área 09 BW Water).
- Adjuntos a enviar: TRANSMITTAL N18 ADASA-BW_WATER.pdf + **1 CC_ADASA PDF** (solo Control Philosophy Rev C, Code 3). Los 4 docs Code 1 no llevan CC_ADASA (CLAUDE.md sección 3.8); sus scripts/PDFs quedan como traza interna, no se adjuntan; entregables residuales en Sección 3.
- Tras envío: estado BORRADOR → ENVIADO, respaldo PDF/.msg en esta carpeta, actualizar README secciones 2 y 9.
