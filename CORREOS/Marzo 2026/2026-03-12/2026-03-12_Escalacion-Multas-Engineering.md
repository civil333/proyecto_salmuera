---
codigo: CORREO-2026-03-12-MULTAS
tipo: Correo Ejecutivo
fecha: 2026-03-12
autor: Luis Rivera Gonzalez
estado: PENDIENTE ENVIO
asunto: Contract C-4300 — Engineering Delay and Accumulated Contractual Penalties (BAE Cl. 43.1.a)
destinatario: Eduardo Yamauchi (BW Water)
cc: Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) / Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)
referencias: Contract C-4300 / BAE 12803 / ET Sec. 7 / TM N1–TM N9
adjuntos: ninguno
calculo_multas:
  monto_contrato: USD 613,991.00
  multa_diaria: USD 307.00 (0.05% diario)
  inicio_mora: 06-Ene-2026
  dias_atraso_hoy: 65
  acumulado_hoy: USD 19,955
  proyeccion_09jul2026: USD 56,488 (184 dias)
  cap_bae_43_4: USD 92,098.65 (15%)
  porcentaje_cap_hoy: 21.7%
  porcentaje_cap_proyectado: 61.3%
nivel: Warning ejecutivo (no activa cure period BAE 49)
---

# Contexto Interno — No Enviar

## Propósito

Correo de escalación ejecutiva que cuantifica formalmente las multas acumuladas por atraso
en ingeniería conforme a BAE Cl. 43.1.a. El correo previo de pre-reunión (2026-03-06,
pendiente envío) era confrontacional respecto al Schedule pero no calculaba multas. Este
agrega la dimensión contractual-financiera.

Nivel de escalación: warning ejecutivo. No activa formalmente el cure period BAE 49 ni la
cláusula de terminación BAE 50, pero los referencia como consecuencias posibles si la
situación no se corrige.

## Cálculo de Multas

- NTP / Inicio engineering: 07-Oct-2025 (BW Water Baseline Schedule)
- Plazo engineering (ET Sec. 7): 90 días calendario desde adjudicación
- Deadline engineering contractual: 05-Ene-2026
- Inicio mora automática: 06-Ene-2026 (BAE Cl. 43, pág. 72 — sin requerimiento previo)
- Multa diaria: 0.05% × USD 613,991 = USD 307.00/día
- Días de atraso a 12-Mar-2026: 65 días (06-Ene → 12-Mar)
- Acumulado a hoy: 65 × USD 307 = USD 19,955
- Proyección per BW Water Catch-Up Schedule Mar-2026 (Engineering fin 09-Jul-2026):
  - 184 días de atraso × USD 307 = USD 56,488
  - 61.3% del cap total
- Cap total multas (BAE 43.4): 15% × USD 613,991 = USD 92,098.65

## Cita BAE que Garantiza Mora Automática

BAE Cl. 43 (página 72/94): "El Proveedor quedará constituido en mora del cumplimiento
de sus obligaciones por el solo hecho de exceder los plazos estipulados, sin necesidad de
requerimiento, intimación o notificación alguna."

## Estado de Documentos Críticos

| Documento | Estado | Impacto |
|-----------|--------|---------|
| Valve List Rev C | Code 4 REJECTED — Rev C no entregada | PO Válvulas bloqueada (109 válvulas) |
| Feed Turbocharger Rev D | Code 4 REJECTED — Rev D no entregada | PO TC1 bloqueada (PO 01-Abr) |
| Control Philosophy Rev B | Code 3 — Rev B no entregada (UPS 30min vs 8h ET) | Afecta diseño MCC, control, commissioning |
| P&ID Rev B corrections | Code 3 (TM N9) — correcciones pendientes | Referencia maestra del proyecto sin cerrar |
| Modbus TCP Memory Map | NO ENTREGADO — comprometido TM N2, 75+ días vencido | Integración PLC-SCADA ADASA bloqueada |
| IO List — Modbus signals | OVERDUE desde TM N3 | Diseño eléctrico ADASA incompleto |

---

# Correo (Enviar a BW Water)

**Date:** March 12, 2026
**From:** Luis Rivera Gonzalez — Leader, Infrastructure Engineering (ADASA)
**To:** Eduardo Yamauchi — Operations Director Americas (BW Water)
**CC:** Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) / Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)
**Subject:** Contract C-4300 — Engineering Delay and Accumulated Contractual Penalties (BAE Cl. 43.1.a)
**Ref:** Contract C-4300 / BAE 12803 / ET Sec. 7 / TM N1–TM N9

---

Dear Mr. Yamauchi,

This communication formally quantifies the contractual penalties accrued to date under
Contract C-4300, resulting from BW Water's continued failure to complete the engineering
deliverable program within the contractually established timeframe.

---

## 1. Accumulated Engineering Delay

ET — Engineering Schedule and Deliverables establishes a 90-calendar-day engineering
period from Notice to Proceed. With NTP effective October 7, 2025, the contractual
engineering completion deadline was January 5, 2026. BW Water's engineering program
remains incomplete as of this date, placing BW Water in breach of this obligation
for 65 consecutive calendar days (January 6 — March 12, 2026).

Under BAE Cl. 43 (p. 72), default is constituted automatically upon expiration of the
agreed term, without prior notice, demand, or notification of any kind:

> *"El Proveedor quedará constituido en mora del cumplimiento de sus obligaciones por
> el solo hecho de exceder los plazos estipulados, sin necesidad de requerimiento,
> intimación o notificación alguna."*

---

## 2. Contractual Penalty Calculation (BAE Cl. 43.1.a — Engineering Delay)

BAE Cl. 43.1.a establishes a daily penalty of 0.05% of the net contract value for
delay in engineering deliverables. Applied to Contract C-4300:

**Daily penalty: 0.05% × USD 613,991.00 = USD 307.00 per calendar day**

| Reference Date | Days in Default | Accumulated Penalty | % of Cap (BAE 43.4) |
|----------------|-----------------|---------------------|----------------------|
| January 6, 2026 (start) | 1 | USD 307 | 0.3% |
| March 12, 2026 (today) | **65** | **USD 19,955** | **21.7%** |
| July 9, 2026 (per BW Water Catch-Up Schedule Mar-2026) | **184** | **USD 56,488** | **61.3%** |

BAE Cl. 43.4 establishes a total penalty cap of 15% of the net contract value:
**USD 92,098.65**. At the current rate of accumulation, BW Water's own projected
engineering completion date (July 9, 2026) would consume 61.3% of that cap on
engineering delay penalties alone — before any EXW delivery penalties are considered.

---

## 3. Engineering Document Status

The following table summarizes the critical engineering deliverables that remain
unresolved as of March 12, 2026:

| Document | Contractual Deadline | Current Status | Delay (days) |
|----------|---------------------|----------------|--------------|
| Valve List Rev C | January 5, 2026 | **Code 4 Rejected** — Rev C not submitted | 65+ |
| Feed Turbocharger Datasheet Rev D | January 5, 2026 | **Code 4 Rejected** — Rev D not submitted | 65+ |
| Control Philosophy Rev B | January 5, 2026 | **Code 3 To Be Revised** — Rev B not submitted (UPS 30 min vs. 8 h per ET) | 65+ |
| P&ID Rev B — Corrective Resubmission | January 5, 2026 | **Code 3 To Be Revised** (TM N9, March 11) — corrections pending | 65+ |
| Modbus TCP Memory Map | January 5, 2026 | **Not submitted** — committed in TM N2, now 75+ days overdue | 75+ |
| IO List — Modbus signals update | January 5, 2026 | **Overdue** since TM N3 | 65+ |

30 of approximately 55 engineering deliverables have received a final approval verdict
(Code 1 or Code 2). Critical procurement-path documents remain unresolved, directly
blocking ADASA's procurement activities and downstream engineering.

---

## 4. Contractual Implications

**BAE Cl. 43.4 — Penalty Cap:** The total penalty ceiling is USD 92,098.65. As of
today, USD 19,955 has accrued — 21.7% of the cap. This figure increases by USD 307
for each additional calendar day of non-compliance.

**BAE Cl. 49 — Formal Non-Compliance Notice:** ADASA has not issued a formal
non-compliance notice under BAE Cl. 49 at this stage. This letter constitutes an
executive-level warning. Should the current situation not be corrected through
specific, verifiable actions within the deadlines set forth in Section 5 below, ADASA
will proceed with formal notification under BAE Cl. 49.

**BAE Cl. 50 — Contract Termination:** BAE Cl. 50 allows ADASA to terminate the
contract if accumulated penalties reach or are reasonably projected to reach the
15% cap. BW Water's own Catch-Up Schedule (March 2026) projects engineering
completion on July 9, 2026 — which would result in penalties of USD 56,488 from
engineering delay alone, equivalent to 61.3% of the total cap. ADASA reserves all
rights under BAE Cl. 50 should projected penalties approach this threshold.

ADASA reserves all contractual rights under Contract C-4300, including the right
to apply, offset, or enforce accumulated and future penalties in accordance with
BAE Cl. 43, 49, and 50.

---

## 5. Required Actions

ADASA requires the following actions to be completed by the dates indicated:

- **Valve List Rev C** — Submit corrected revision addressing all Code 4 observations
  (TAGs duplicados, actuación incorrecta): **by March 16, 2026**
- **Feed Turbocharger Datasheet Rev D** — Submit revision addressing coupling
  pressure rating and Class H upgrade: **by March 25, 2026**
- **Control Philosophy Rev B** — Submit corrected revision addressing UPS duration
  (minimum 8 hours), CEE/MVE control functions, and enable permissive interface:
  **by March 20, 2026**
- **Modbus TCP Memory Map** — Committed in TM N2, now 75+ days overdue. Submit
  immediately: **by March 14, 2026**
- **Written schedule explanation** — Provide a written explanation, signed by BW
  Water management, of how the projected engineering completion date (July 9, 2026)
  is compatible with the EXW delivery obligation of August 3, 2026 and the
  contractual FAT, commissioning, and training program.

Please confirm receipt of this communication and provide written acknowledgment of
the required actions and their completion dates.

Sincerely,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA — Aguas de Antofagasta S.A.
