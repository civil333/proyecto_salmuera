---
codigo: CORREO-2026-03-04-B
asunto: RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses
fecha: 2026-03-04
autor: Luis Rivera Gonzalez
estado: FINAL
version: 2.0
---

# Contexto Interno — NO ENVIAR

## Situacion

Eduardo Yamauchi respondio hoy (04-Mar-2026) con comentarios inline en azul al correo de
evaluacion ADASA del 17-Feb-2026 ("Catch-Up Schedule Request"). Esta version abandona el
enfoque de proceso (correo anterior v1) y va directamente al fondo: evaluacion tecnica por
item — ACCEPTED / CONDITIONAL / NOT ACCEPTED / COMMITMENT REGISTERED — con justificacion
citando ET nombre de seccion, Oferta Tecnica Rev1 seccion, y BAE clausula donde aplique.

## Hallazgos Clave de Validacion Cruzada

### HP Pump 93 kW (TM N4 OBS-08)
- Eduardo confirma 93 kW
- PROBLEMA: Oferta Tecnica Rev1 §4.1 especifica 86 kW (115.3 hp) — diferencia de 7 kW (8%)
- SEC garantizado (4.71 kWh/m³, OT §3.1; BAE Garantia Consumo Energetico) podria verse afectado
- Posicion ADASA: CONDITIONAL — todos los documentos deben unificarse a 93 kW + calculo SEC actualizado

### VM-09-015 Actuation (TM N3 OBS-11) — OBSERVATION WITHDRAWN
- Eduardo: "Not a process relevant valve, ET 5.2.3 not applicable"
- VM-09-015 es valvula de aislamiento manual entre bomba HP y turbocharger — no es valvula de
  control de proceso. ADASA acepta la caracterizacion de Eduardo: ET 5.2.3 no aplica.
- Inconsistencia documental: Valve List Rev B item 18 muestra VM-09-015 como ON/OFF MOTORIZED
  (Ethernet IP, 380/220 VAC) — contradice la propia respuesta de Eduardo ("manual").
- BW Water debe resolver en Rev C: revertir a MANUAL si ese es el diseno, o confirmar MOTORIZED
  si Rev B es correcto.
- Posicion ADASA: OBSERVATION WITHDRAWN (con nota de inconsistencia documental)

### Temperature Switches vs Transmitters (TM N3 OBS-08) — CERRADA

- BW Water confirmó Pt-100 en devanados y rodamientos (16-Feb-2026); ADASA aceptó (17-Feb-2026)
- HP Pump Datasheet Rev C (E13): RTDs 3-wire en rodamientos y devanados incluidos
- TM N6 registra formalmente: "Pt-100 motor windings confirmed (TM N3) | HP Pump Rev C | RESOLVED ✓"
- Posicion ADASA: CLOSED — eliminada de "Items Not Addressed" por error (corregido 05-Mar-2026)

### IO MODBUS list (TM N4 OBS-04)
- Eduardo: entrega 06-Mar
- ET — Communication and Control System: MODBUS TCP/IP obligatorio
- Technical Offer Rev1 — Communication Protocols: Modbus TCP/IP con cliente externo
- Posicion ADASA: COMMITMENT REGISTERED

### Control System Architecture Rev C + UPS (TM N4 OBS-09)
- Eduardo: entrega Rev C el 06-Mar con UPS incluido
- ET — Control System Power Backup: UPS minimo 8 horas de autonomia para sistema de control
- Technical Offer Rev1 — Power and Load Consumption List: "RO PLC + Instrumentation (UPS powered) 2.0 kW"
- Posicion ADASA: COMMITMENT REGISTERED — Rev C debe confirmar 8 horas de autonomia explicitamente

### VFD Electrical Variables como AI Signals (TM N3 OBS-15)
- Eduardo: entrega listado el 06-Mar con variables electricas de VFDs como AI
- ET — Energy Metering and SEC Verification: monitoreo energetico para verificacion de SEC
- Technical Offer Rev1 — Power and Load Consumption List: VFDs HP Pump (Fedco) y CIP Pump (Grundfos)
- Posicion ADASA: COMMITMENT REGISTERED

### Container 40ft (TM N4 OBS-10)
- Eduardo: confirma 40ft (con CIP y dosificacion fuera del container)
- ET — Container Dimensions: dimensiones max 13m x 2.5m x 2.8m
- Technical Offer Rev1 — Equipment List: 40ft ISO estandar
- Posicion ADASA: ACCEPTED — pendiente revision documental

### IO MODBUS señales externas (TM N3 OBS-04/05)
- Comprometido al 03-Mar — vencio ayer, Eduardo no lo menciono
- ET — Communication and Control System
- Posicion ADASA: OVERDUE — no entregado

### A/C Thermal Calculation (TM N4 OBS-03)
- Comprometido para 18-Feb — 15 dias vencido, no mencionado
- ET — Air Conditioning System: "se debera entregar una memoria de calculo termica"
- Posicion ADASA: OVERDUE — no entregado

### SEC Calculation con Turbochargers (TM N3 OBS-02)
- No mencionado por Eduardo
- Technical Offer Rev1 — Guaranteed Performance: SEC garantizado 4.71 kWh/m³ ± 5% incluyendo ERD
- ET — Performance Testing: prueba de desempeno mide kWh/m³ vs garantia
- Posicion ADASA: NOT ADDRESSED

---

# Correo Formal — ENVIAR

**Date:** March 5, 2026
**From:** Luis Rivera Gonzalez — Leader, Infrastructure Engineering (ADASA)
**To:** Eduardo Yamauchi — Operations Director Americas (BW Water)
**CC:** Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) /
        Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)
**Subject:** RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses
**Ref:** Contract C-4300 / BAE 12803 / TM N3 (P22-TM-09-000-003-0) / TM N4 (P22-TM-09-000-004-0)

---

Eduardo,

We have reviewed your March 4 inline responses against the project technical requirements.
Our evaluation of each item is set out below.

---

## Evaluation of Responses Received — March 4, 2026

| OBS | Eduardo (04-Mar-2026) | ADASA Position | Technical Basis |
|---|---|---|---|
| TM N4 OBS-08 | HP Pump confirmed 93 kW | **CONDITIONAL** — 93 kW conflicts with 86 kW in Technical Offer Rev1. All project documents must be unified to 93 kW; updated SEC calculation required to confirm compliance with guaranteed performance. | Technical Offer Rev1 — Equipment List and Technical Details (86 kW stated); Technical Offer Rev1 — Guaranteed Performance (4.71 kWh/m³ guaranteed); BAE — Garantía de Consumo Energético |
| TM N3 OBS-11 | VM-09-015: not a process relevant valve; ET 5.2.3 not applicable | **OBSERVATION WITHDRAWN** — ADASA accepts Eduardo's characterization of VM-09-015 as a manual isolation valve (HP pump to turbocharger), not subject to ET 5.2.3. However, Valve List Rev B item 18 shows this valve as ON/OFF MOTORIZED (Ethernet IP, 380/220 VAC), contradicting the current response. BW Water must align Rev C: revert to MANUAL actuation if that is the intended design, or confirm motorized if Rev B is correct. | Valve List Rev B item 18: ON/OFF MOTORIZED (contradicts Eduardo's response of "manual"); ET — Actuadores (scope limited to "válvas de proceso relevantes") |
| TM N4 OBS-04 | IO MODBUS list to be delivered March 6 | **COMMITMENT REGISTERED** | ET — Communication and Control System (MODBUS TCP/IP required); Technical Offer Rev1 — Communication Protocols (Modbus TCP/IP with client SCADA) |
| TM N4 OBS-09 | Control System Architecture Rev C (with UPS) to be delivered March 6 | **COMMITMENT REGISTERED** — Rev C must explicitly state UPS autonomy ≥ 8 hours | ET — Control System Power Backup ("UPS con capacidad suficiente para mantener el sistema de control activo por al menos 8 horas"); Technical Offer Rev1 — Power and Load Consumption List (UPS powered PLC, 2.0 kW) |
| TM N3 OBS-15 | VFD electrical variables to be included as AI signals | **COMMITMENT REGISTERED** — IO List must include AI signals from HP Pump VFD and CIP Pump VFD | ET — Energy Metering and SEC Verification; Technical Offer Rev1 — Power and Load Consumption List (VFD: HP Pump Fedco, CIP Pump Grundfos) |
| TM N4 OBS-10 | Container confirmed as 40ft; CIP and chemical dosing located outside container | **ACCEPTED** — pending document revision reflecting the confirmed layout | ET — Container Dimensions ("dimensiones máximas del contenedor: 13m × 2.5m × 2.8m"); Technical Offer Rev1 — Equipment List |

---

## Items Not Addressed / Overdue

| OBS | Topic | Status | Technical Requirement |
|---|---|---|---|
| TM N3 OBS-04/05 | IO MODBUS external interface signals (DO module status / DI external enable) | **OVERDUE** — Committed March 3; not delivered | ET — Communication and Control System (MODBUS TCP/IP for remote control and data extraction) |
| TM N4 OBS-03 | A/C thermal calculation | **OVERDUE 15 days** — Committed Feb 18; not mentioned in today's response | ET — Air Conditioning System ("se deberá entregar una memoria de cálculo térmica para determinar la cantidad del sistema de aire acondicionado") |
| TM N3 OBS-02 | SEC calculation incorporating turbocharger energy recovery | **NO RESPONSE** | Technical Offer Rev1 — Guaranteed Performance (4.71 kWh/m³ ± 5%, including ERD contribution); ET — Performance Testing (SEC measured as kWh/m³ against guaranteed value) |

---

Formal written responses to TM N3 and TM N4 — with revised documents at incremented revision
numbers — remain required under Contract C-4300. We request that all overdue items be delivered
prior to the March 9 meeting, together with the March 6 commitments.

Best regards,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA — Aguas de Antofagasta S.A.
BAE 12803 — Second Stage RO Brine Module Taltal

---

# Versión Alternativa (Prosa) — Para elección del usuario

> **Nota:** Esta versión usa prosa narrativa por ítem en lugar de tablas.
> Si se aprueba, regenerar el DOCX actualizando `crear_correo_catchup.py`.

---

**Date:** March 5, 2026
**From:** Luis Rivera Gonzalez — Leader, Infrastructure Engineering (ADASA)
**To:** Eduardo Yamauchi — Operations Director Americas (BW Water)
**CC:** Jeryl F. Regulacion; Adzlan Bin Abd Rahim; Andrew Zaske (BW Water) / Cesar Malhue; Jorge Guevara; Ronald Pellejero; Victor Gutierrez (ADASA)
**Subject:** RE: Catch-Up Schedule Request — ADASA Evaluation of March 4 Responses
**Ref:** Contract C-4300 / BAE 12803 / TM N3 (P22-TM-09-000-003-0) / TM N4 (P22-TM-09-000-004-0)

---

Eduardo,

Regarding your comments in blue in the batch email, we have reviewed each item against the project technical requirements and the six transmittals issued to date. Our evaluation is set out below, ordered by urgency.

---

### Items with Response Received

**1. HP Pump Power Rating — Conditional Acceptance (TM N4 OBS-08)**

CONDITIONAL. Technical Offer Rev1 — Equipment List states 86 kW; the confirmed 93 kW creates an 8% discrepancy that bears on the guaranteed SEC of 4.71 kWh/m³ under the Technical Offer Rev1 — Guaranteed Performance and the BAE — Garantía de Consumo Energético. All project documents must be unified to 93 kW and an updated SEC calculation submitted.

**2. VM-09-015 Valve Actuation — Observation Withdrawn (TM N3 OBS-11)**

OBS-11 WITHDRAWN — VM-09-015 accepted as a manual isolation valve not subject to ET — Actuadores. Note: Valve List Rev B item 18 lists it as ON/OFF MOTORIZED (Ethernet IP, 380/220 VAC), contradicting your response. Rev C must resolve the discrepancy.

**3. IO MODBUS List — Commitment Registered (TM N4 OBS-04)**

REGISTERED — March 6 delivery. List must cover all Modbus TCP/IP data points per ET — Communication and Control System.

**4. Control System Architecture Rev C + UPS — Commitment Registered (TM N4 OBS-09)**

REGISTERED — Rev C due March 6. The document must explicitly state UPS autonomy ≥ 8 hours; a general reference to UPS inclusion is not sufficient.

**5. VFD Electrical Variables as AI Signals — Commitment Registered (TM N3 OBS-15)**

REGISTERED — March 6 delivery. AI signals required for HP Pump VFD (Fedco) and CIP Pump VFD (Grundfos) per ET — Energy Metering and SEC Verification.

**6. Container Layout — Accepted (TM N4 OBS-10)**

ACCEPTED. Formal document revision required to reflect the confirmed layout.

---

### Items Not Addressed in Today's Response

**7. SEC Calculation Incorporating Turbocharger Energy Recovery (TM N3 OBS-02)**

No response received. The guaranteed 4.71 kWh/m³ (±5%) cannot be verified without an explicit SEC calculation accounting for turbocharger energy recovery. A substantive technical response is required — not a delivery date.

**8. IO MODBUS External Interface Signals — Overdue (TM N3 OBS-04/05)**

OVERDUE. Committed March 3; not delivered, not mentioned today. DO module status and DI external enable are required for external SCADA integration per ET — Communication and Control System.

**9. A/C Thermal Calculation — Overdue 15 Days (TM N4 OBS-03)**

OVERDUE 15 DAYS. Committed February 18; not submitted, not referenced today. Required by ET — Air Conditioning System.

---

Overdue items 8 and 9 must be delivered before the March 9 meeting, together with the March 6 commitments (items 3, 4, and 5). Formal written responses to TM N3 and TM N4 — with documents at incremented revision numbers — remain due under Contract C-4300.

Best regards,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA — Aguas de Antofagasta S.A.
BAE 12803 — Second Stage RO Brine Module Taltal
