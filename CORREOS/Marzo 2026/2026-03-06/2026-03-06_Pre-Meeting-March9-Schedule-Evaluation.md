---
codigo: CORREO-2026-03-06
asunto: "March 9 Meeting — EXW August 3 vs. Engineering Status: Clarification Required"
fecha: 2026-03-06
autor: Luis Rivera Gonzalez
estado: PENDIENTE ENVIO
version: 2.2
---

# Contexto Interno — NO ENVIAR

## Situacion

BW Water entrego el 05-Mar-2026 un nuevo "Baseline Schedule" (12803_Taltal Water Treatment Plant,
fecha del documento 5/3/2026). ADASA realizo el analisis completo en:
`PROGRAMA y CONTRATO/REVISIONES/2026-03-06_Analisis-Catch-Up-Schedule-Mar2026.md`

Este correo reemplaza la version v1.0 (briefing colaborativo con agenda). Version v2.0:
tono ejecutivo y confrontacional, foco central en la contradiccion EXW agosto vs. estado real
de la ingenieria. Sin agenda propuesta al final.

## Problema central

El schedule declara EXW August 3 intacto, pero muestra Engineering hasta July 9 (+185 dias
sobre la linea base contractual de Jan 5, 2026). No se explica como esos dos numeros son
compatibles. La fase "General Engineering" aparece cerrada el Feb 20 — eso contradice
directamente 15 documentos no entregados y 14 con observaciones abiertas. ADASA no ve
ningun plan de recuperacion que sustente la fecha EXW.

## Procurement en ruta critica

- HP Pump: PO semana 4-10 Mar — Code 2-AN FORMAL (TM N6, 27-Feb). PO PUEDE PROCEDER con nota aclaratoria: 93 kW nameplate / 78.5 kW operacion / 83-85 kW FEDCO refs.
- Interstage TC: PO TBD — Code 2-AN (TM N6, 27-Feb). PO EN HOLD: datasheet fabricante acople no entregado (MAWP ≥1,845 psi, HPB service cert., vibration mounting ET 5.5.7).
- Feed TC: PO 01-Abr — Code 4 activo (TM N6), Rev D no presentada. Coupling 1,200 psi inaceptable (margen 1.19x vs ASME 1.5x min). ≥2,000 psi preferido / ≥1,800 psi minimo.
- Valve List (109 valvulas): PO 11-Mar — Code 4 activo (TM N6), Rev C no presentada.

Emitir POs con documentos rechazados o documentacion pendiente no acelera el proyecto — genera retrabajo que lo atrasa.

## Referencia contractual clave

Compromiso formal de BW Water registrado en reunion 18-Feb-2026:
"No POs before ADASA approval."

## Cambios respecto a v1.0

- Eliminada seccion "What the March 5 Document Resolves" (positivos)
- Eliminada seccion "Proposed Agenda"
- Agregada tabla central: Schedule vs Project Records (EXW vs Engineering)
- Agregada tabla procurement: 3 items con POs bloqueados
- Tono: cuestiona coherencia del schedule, no negocia

---

# Correo Formal — ENVIAR

**Date:** March 6, 2026
**From:** Luis Rivera Gonzalez — Leader, Infrastructure Engineering (ADASA)
**To:** Eduardo Yamauchi — Operations Director Americas (BW Water)
**CC:** Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) /
        Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)
**Subject:** March 9 Meeting — EXW August 3 vs. Engineering Status: Clarification Required
**Ref:** Contract C-4300 / BAE 12803 / TM N6 (P22-TM-09-000-006-0)
**Attachments:** P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx — ADASA Master Deliverable Register (62 items, updated March 6, 2026)

---

Eduardo,

ADASA acknowledges receipt of the Baseline Schedule dated March 5, 2026
("12803_Taltal Water Treatment Plant_Baseline Schedule"). Before the March 9 meeting,
ADASA has evaluated that document and has critical observations that require a response.

---

## The EXW Date vs. the Schedule

The schedule maintains EXW August 2–3, 2026 without change. The engineering data in
the same document does not support that date.

| Item | Schedule — March 5 | Project records — March 6 |
|------|---------------------|---------------------------|
| Engineering end date | July 9, 2026 (198 days) | Contractual baseline: January 5, 2026. Current delay: +185 days |
| General Engineering | Complete as of February 20, 2026 | 15 documents never submitted; 14 with open observations |
| EXW delivery | August 2–3, 2026 (no change) | No recovery plan submitted. Basis for this date not explained. |

ADASA requests that BW Water explain, before March 9, how Engineering at +185 days over the
contractual baseline is consistent with an unchanged EXW date of August 3, 2026. A recovery
plan with document-level milestones — covering the 15 pending deliverables and 14
open-observation items — is required.

ADASA's Master Deliverable Register (Attachment 1) lists all 62 engineering deliverables with
current review verdicts and outstanding actions. BW Water's recovery plan must address each
item in that register.

---

## Procurement Items on the Critical Path

Four procurement items are scheduled within the next 30 days. Two carry an active
Code 4 — Rejected verdict; one is approved as noted but has an outstanding documentation
requirement that blocks the PO; one is formally approved with a clarifying note. Issuing
POs without resolving open conditions does not accelerate the project; it introduces
rework that delays EXW further.

| Equipment | PO Date | ADASA Status | Action Required |
|-----------|---------|--------------|-----------------|
| RO HP Pump | Week of March 4–10 | Code 2 — Approved as Noted (TM N6, Feb 27) | PO may proceed. BW Water must add clarifying note in DS: 93 kW nameplate / 78.5 kW at design point / 83–85 kW FEDCO internal refs. |
| Interstage Turbocharger | TBD | Code 2 — Approved as Noted (TM N6, Feb 27) | PO on hold: coupling manufacturer's datasheet not submitted. Required: MAWP ≥ 1,845 psi, HPB service certification, vibration sensor mounting documented (ET 5.5.7). No datasheet → no PO. |
| Feed Turbocharger | April 1 | Code 4 — Rejected (TM N6, Feb 27) | PO suspended. Coupling downgraded from 2,000 psi to 1,200 psi (1.19x margin — ASME minimum 1.5x). Rev D required: ≥ 2,000 psi preferred (Piedmont Style H); ≥ 1,800 psi minimum. Submit coupling manufacturer's datasheet. |
| Valve List (109 valves) | March 11 | Code 4 — Rejected (TM N6, Feb 27) | Rev C required before March 10. Duplicate TAGs (VM-09-015, VE-09-008, VE-09-009, VM-09-065) must be resolved for correct procurement traceability and SCADA assignment. VE-09-008 (items 44/57 — ANSI 900# vs ANSI 150#) carries direct procurement risk: two physically different valves share the same TAG. |

These four items are on the critical path to EXW. BW Water committed at the
February 18, 2026 meeting: no purchase orders before ADASA approval. All four items
above fall under that commitment.

---

Before March 9, ADASA requires: (a) BW Water's explanation of how EXW August 3 remains
achievable given Engineering at +185 days over the contractual baseline, including a
document-level recovery plan covering all 15 pending deliverables and 14 open-observation
items with individual dates; (b) delivery status of the three March 6 commitments —
IO MODBUS list, Control Architecture Rev C, VFD variables — and a firm date for the
Modbus TCP Memory Map, outstanding 51 days since TM N2; (c) coupling manufacturer's
datasheet for the Interstage Turbocharger confirming MAWP ≥ 1,845 psi, HPB service
certification, and vibration sensor mounting per ET 5.5.7.
Without these responses, the March 9 meeting cannot resolve the project's critical items.

Best regards,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA — Aguas de Antofagasta S.A.
BAE 12803 — Second Stage RO Brine Module Taltal
