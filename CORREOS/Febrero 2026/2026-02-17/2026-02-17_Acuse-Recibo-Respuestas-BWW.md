---
titulo: "Acknowledgment of Responses - Transmittals N3, N4 and Schedule (C-4300)"
fecha: "2026-02-17"
de: "Luis Rivera Gonzalez <lrivera@aguasantofagasta.cl>"
para: "Eduardo Yamauchi <Eduardo.Yamauchi@bw-water.com>"
cc: "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim"
adjuntos: "None"
---

Dear Eduardo,

We acknowledge receipt of your three responses dated February 16, 2026, covering Transmittal N3 (P22-TM-09-000-003-0), Transmittal N4 (P22-TM-09-000-004-0), and schedule-related items. Six items are accepted, but two critical items remain without acceptable resolution, and several others need clarification. Our full evaluation follows.

**Items Accepted**

We confirm the following items as resolved:

- **Pt-100 motor windings** (TM N3 OBS-06 to OBS-09): Pt-100 for windings and bearings confirmed per ET 5.3. Accepted.
- **Vibration transmitters** (TM N3 OBS-01): Transmitters for HP Pump and Turbochargers confirmed per ET 5.5.7. Accepted.
- **Duplicate TAG FIT-09-001** (TM N3 OBS-05, TM N4 OBS-05): Renumbered to FIT-09-002. Accepted.
- **A/C n+1 configuration** (TM N4 OBS-02): Second A/C unit confirmed per ET 5.1.11. Accepted.
- **EXW Penang basis** (Schedule): EXW Penang confirmed, shipping estimated August 3, 2026. Noted.
- **No POs before datasheet approval** (Schedule): Purchase orders will not be issued before ADASA approval. Recorded as formal commitment.

**Critical Items Requiring Immediate Resolution**

These two items have been open for an unacceptable period and must be resolved at the February 18 meeting:

| Item | Issue | Required Action | Open Since |
|------|-------|-----------------|------------|
| **Modbus TCP Memory Map** (TM N4 OBS-04) | Program "has not yet started" — 42 days after commitment (TM N2, Jan 6). Prerequisite for PLC-to-PLC interface design. | Concrete delivery date required. Discuss at Feb 18 meeting. | 42 days |
| **Container 60ft** (TM N4 OBS-10) | "Still under review" — ADASA formally rejected the 60ft proposal on November 17, 2025 (+USD $67,208, +5 weeks) and confirmed this decision on December 17, 2025. The 40ft configuration is the approved basis. | Engineering drawings must reflect the approved 40ft configuration. Documents showing an enlarged container do not correspond to the communicated decision. | 92 days |

**Items Requiring Clarification**

- **VM-09-015 actuation** (TM N3 OBS-03): Response does not explicitly confirm change to electric actuation. ET 5.2.3 requires electric for DN100 ANSI 900#. Please confirm: yes or no.
- **VFD electrical variables** (TM N3 OBS-15): Response addresses communication protocol, but our requirement is the data content — voltage, current, power, frequency, temperature from both VFDs as AI signals in the IO List for SEC calculation.
- **HP Pump power** (TM N4 OBS-08): Not addressed. Four values exist (83/86/92/93 kW). A single correct value must be established before procurement.
- **UPS in BOM** (TM N4 OBS-09): Not addressed. ET 5.4 requires UPS with 8h autonomy for the control system. Must be added to BOM.
- **Partial coverage** (16 of 27 observations): Responses cover 6/17 from TM N3 and 5/10 from TM N4. The remaining observations were not mentioned. Please confirm all are being tracked.

**Regarding OBS-04 and OBS-05 TM N3 (External Coordination Signals)**

To provide the context you requested: the "external system" referred to in these observations is a PLC external to the BW Water module, part of the broader ADASA plant control architecture but outside BW Water's supply scope. This external PLC is currently in development. The coordination signals required between the two systems are:

- **DO - Module Status:** A digital output from the BW Water PLC indicating module running status (0 = stopped, 1 = running). This allows the external PLC to coordinate feed supply and reject disposal.
- **DI - External Enable:** A digital input to the BW Water PLC from the external system (1 = module authorized to operate, 0 = module must stop). This allows plant-level control over module operation.

These are standard interface signals between independent control systems. They should be included in the IO List as hardwired signals (not via Modbus).

**Coordination Meeting - February 18, 2026**

We confirm the coordination meeting for tomorrow, **Wednesday February 18, 9:00 AM EST (11:00 AM Chile)**. As discussed, we expect to receive before or during the meeting:

- Delivery plan with engineering milestones
- Updated schedule showing document delivery dates
- Document delivery schedule for the 14 pending documents and 16 currently under revision

**Proposed Agenda (1 hour):**

1. **Engineering Recovery Plan** (15 min)
   - Delivery plan and measures to recover engineering timeline
   - Confirmation of April 24 as engineering completion baseline
   - Mitigation actions for critical path items

2. **Document Delivery Schedule** (10 min)
   - Submission dates for 14 pending documents and 16 under revision
   - Priorities: MCC datasheet, CIP Pump datasheet, PIE Detallado

3. **Critical Open Items from Transmittals** (20 min)
   - Modbus TCP Memory Map (42 days pending, program not started)
   - Container 60ft (under review since Nov 2025)
   - HP Pump power unification (4 values)
   - VM-09-015 electric actuation confirmation
   - VFD electrical variables for SEC verification
   - UPS inclusion in control system BOM

4. **Procurement Alignment** (10 min)
   - Confirmation that no POs will be issued before datasheet approval
   - HP Pump PR/PO status (datasheet carries "To be revised" verdict)
   - Antiscalant system procurement (CT-001 observations pending, deadline Feb 20)

5. **Next Steps and Follow-up** (5 min)

Please confirm the agenda or propose modifications.

Best regards,

**Luis Rivera Gonzalez**
Leader, Infrastructure Engineering
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module Taltal

---

## Contexto Interno (No enviar)

### Estrategia del correo
- **Tipo:** Acuse de recibo formal + evaluacion preliminar de respuestas parciales + agenda reunion
- **Tono:** Constructivo donde se acepta, firme donde falta. Sin escalamiento (ya tenemos reunion manana).
- **Estructura:** Aceptaciones primero (genera buena fe), luego items insuficientes con justificacion clara.
- **Objetivos:**
  1. Documentar formalmente que se recibieron las respuestas y cuales se aceptan
  2. Dejar en evidencia que Modbus Map (42 dias) y Container 60ft (3 meses) son inaceptablemente lentos
  3. Aclarar OBS-04/05 TM N3 (senales externas) para desbloquear respuesta de BWW
  4. Fijar agenda de reunion con temas priorizados
  5. Recordar que delivery plan + schedule son entregables esperados para manana

### Datos al 17-Feb-2026
- TM N3: 20 dias desde emision (28-Ene). Respuesta parcial recibida 16-Feb (6/17 obs)
- TM N4: 12 dias desde emision (05-Feb). Respuesta parcial recibida 16-Feb (5/10 obs)
- Modbus Map: 42 dias desde compromiso (06-Ene TM N2)
- Container 60ft: Rechazado 17-Nov-2025, "under review" desde entonces (3 meses)
- CT-001: Evaluacion ya enviada 16-Feb, deadline observaciones 20-Feb
- Compromiso "no POs antes de aprobacion": clave contractual, registrado
- Multas acumuladas: ~USD 13,500+ (44+ dias x USD 307/dia) -- NO incluir en correo
