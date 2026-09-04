---
titulo: "Technical Query — Control Logic Completeness Review"
subtitulo: "Second Stage Brine Module — P22-IT-06-008-101-B Rev B"
codigo: "P22-CT-06-000-001-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Technical Query (Internal)"
proyecto: "BAE 12803 - Módulo de Salmuera Segunda Etapa Taltal"
---

# TECHNICAL QUERY: CONTROL LOGIC COMPLETENESS — P22-IT-06-008-101-B Rev B

**Date:** February 28, 2026
**Project:** BAE 12803 — Second Stage RO Brine Module, Taltal
**From:** ADASA — Aguas de Antofagasta S.A. (Luis Rivera)
**To:** Van Doorn (Engineering Detail — Internal ADASA Consultant)
**Reference Document:** P22-IT-06-008-101-B, Rev B, 22-Feb-2026
**Status:** ISSUED

---

## 1. BACKGROUND

ADASA has reviewed the Control Logic Description P22-IT-06-008-101-B Rev B submitted in
Engineering Delivery 1 (Nota de Envío N°1). The review was conducted against the equivalent
document P13-IT-03-008-001-0 (2019), which was the document used to successfully program,
commission, and operate Module 3.

The Rev B document correctly identifies the main permissives, the primary control loop
(CTRL_BH06_001 — 3 bar at PIT-06-001), and the BW Water interface signals. However, the
review identified seven gaps that must be resolved before the document can be approved for
PLC programming.

A formal internal evaluation (P22-IT-06-000-004-0) has been issued to document the full
comparative analysis. This query summarizes the required actions for Rev C.

---

## 2. REFERENCE DOCUMENTS

| # | Code | Document | Rev | Role |
|---|------|----------|-----|------|
| 1 | P22-IT-06-008-101-B | Descriptivo Lógica de Control — 2da Etapa Salmuera | B (22-Feb-2026) | Document under review |
| 2 | P13-IT-03-008-001-0 | Descriptivo Lógica de Control — Módulo 3 | 0 (2019) | Benchmark |
| 3 | P22-IT-06-000-004-0 | Control Logic Review Evaluation (ADASA Internal) | 0 | Supporting analysis |

---

## 3. IDENTIFIED GAPS AND REQUIRED ACTIONS

### 3.1 GAP-01 — Incomplete Start-up Sequence (MAJOR)

**Current state:** Rev B lists 16 start-up permissives but does not describe the step-by-step
sequence once permissives are verified.

**Impact:** BW Water's PLC programmer cannot implement the correct interlock sequence between
ADASA's feeding system and the RO module without verbal clarification. This creates risk of
programming rework after the first commissioning attempt.

**Action required for Rev C:**

Please add a numbered step-by-step start-up sequence after the permissive list, addressing:

| # | Question to Resolve |
|---|---------------------|
| 1 | When does BH-06-001 start and at what initial VFD frequency? |
| 2 | How long does the system wait to confirm pressure at PIT-06-001? |
| 3 | What happens if required pressure is not reached within that time (alarm, shutdown, retry)? |
| 4 | When is the start pulse OI-06-003 sent to BW Water (immediately after pump confirms, or after pressure confirmed)? |
| 5 | How does the ADASA PLC confirm the OI module is running (via OI-06-004)? |
| 6 | What is the timeout for OI start confirmation before a fault is declared? |

---

### 3.2 GAP-02 — Incomplete Shutdown Sequence + Tag Error (MAJOR)

**Current state:** Rev B contains 3 shutdown steps. Step 3 references "Parada Bomba de
alimentación BH-**03**-001" — an incorrect tag from Module 3. The correct tag is **BH-06-001**.

**Impact:** Tag error will cause incorrect I/O assignment in PLC programming if not corrected.
Incomplete shutdown creates undefined behavior for drainage pump and valve states.

**Action required for Rev C:**

1. **Correct tag error:** Replace BH-03-001 → BH-06-001 in shutdown step 3.
2. **Add missing shutdown steps:**

| Missing Item | Define |
|---|---|
| BS-06-001 (drainage submersible pump) | Is it stopped before or after BH-06-001? What is the sequence? |
| VM-06-001 / VM-06-002 (manual valves) | Final state after shutdown — remain open or are they closed? |
| Instrumented valves | Final state of any instrumented valves at end of shutdown |
| OI-06-004 timeout | Maximum wait time for BW Water OI shutdown confirmation before fault alarm |

---

### 3.3 GAP-03 — No Level Band Table for TK-06-001 (MINOR)

**Current state:** Rev B mentions >70% level as start-up permissive and "low level" as an
interlock, but does not define the full operational level behavior of the storage tank.

**Action required for Rev C:**

Please add a level band table for TK-06-001 equivalent to the one in P13, covering:

| Band | Level Range | Equipment State | Action |
|------|-------------|-----------------|--------|
| High-High | Define | Define | Define (e.g., OI stop pulse) |
| Normal High | Define | Define | Normal operation upper limit |
| Normal Low | Define | Define | Normal operation lower limit |
| Low-Low | Define | Define | BH-06-001 and OI emergency stop |

---

### 3.4 GAP-04 — Post-Treatment Integration Not Documented (MINOR)

**Current state:** Rev B states that post-treatment "ya se encuentra en operación y no requiere
acción alguna desde el nuevo PLC." This is operationally correct but leaves coordination
points undefined.

**Action required for Rev C:**

Please confirm and document:

1. Is the TK-00-001 high level signal the only coordination point between the new module and
   the existing post-treatment system?
2. Are there any inter-PLC signals between the new ADASA PLC and the existing plant PLC,
   or do the systems share only the physical tank TK-00-001?
3. Is there a flow or production confirmation available to the operator (e.g., FIT on the
   discharge line) so that the operator can verify the 25 m³/h contribution is reaching
   post-treatment?

A single paragraph or small table in Rev C clarifying these points is sufficient.

---

### 3.5 GAP-05 — Control Loop BH-06-001 Without Complete Definition (MINOR)

**Current state:** CTRL_BH06_001 is documented as maintaining 3 bar at PIT-06-001. The
control type, VFD limits, and failure behavior are not defined.

**Action required for Rev C:**

Please complete the CTRL_BH06_001 definition with:

| Parameter | Required Information |
|-----------|---------------------|
| Control type | PI or PID? |
| VFD frequency range | Hz minimum / maximum |
| Setpoint | 3 bar (confirm) or adjustable range? |
| PIT-06-001 fault behavior | What mode does BH-06-001 enter if pressure transmitter fails? |
| Start ramp | Frequency ramp profile for BH-06-001 start |

---

### 3.6 GAP-06 — Fault Alarm Signal and Restart Procedure Not Documented (MINOR)

**Current state:** Rev B lists 4 signals with the BW Water PLC (OI-06-002, OI-06-003,
OI-06-004, OI-06-005). A direct comparison with the P13 benchmark (Osmoflo interface)
confirms the signal count is equivalent — the P13 also had 4 signals in its formal
signal section. The gap is not a missing signal count, but two specific omissions.

**First omission — Fault alarm signal not listed:**
The fault alarm signal from BW Water OI to ADASA PLC (equivalent to OI-03-003 in P13)
does not appear in the Rev B signal list. In P13 this signal triggered immediate plant
shutdown and required operator acknowledgement. It must be documented with its tag,
direction (DI to ADASA PLC), and the interlock it activates.

**Second omission — Restart procedure after fault not documented:**
The P13 explicitly stated that no dedicated reset signal to the OI module is required —
the operator must normalize the fault condition and reset via ADASA HMI before the plant
can restart. Rev B contains no equivalent statement, leaving the restart logic undefined
for the BW Water OI interface.

**Action required for Rev C:**

| # | Action |
|---|--------|
| 1 | Add fault alarm signal (equivalent to OI-03-003) to signal list with tag, type DI, and interlock description. |
| 2 | Document restart procedure after OI fault: confirm no dedicated reset signal to BW Water is needed and that reset is via ADASA HMI. |

---

### 3.7 GAP-07 — Authorship Does Not Comply with ADASA Protocol (ADMINISTRATIVE)

**Current state:** Revisions A and B show Prepared/Reviewed/Approved = L. Hughes (same
person for all fields).

**Action required for Rev C:**

Per ADASA document control protocol, the title block for Rev C must show:

| Field | Value |
|-------|-------|
| Prepared By | Luis Rivera |
| Reviewed By | Luis Rivera |
| Approved By | Victor Gutierrez |

---

## 4. SUMMARY OF REQUIRED ACTIONS

| Gap | Severity | Action | Rev C Section |
|-----|----------|--------|---------------|
| GAP-01 | Major | Add numbered start-up sequence (6 items) | Start-up |
| GAP-02 | Major | Correct BH-03 → BH-06 tag; complete shutdown (4 items) | Shutdown |
| GAP-03 | Minor | Add level band table TK-06-001 (4 bands) | Level control |
| GAP-04 | Minor | Document post-treatment coordination points (3 items) | System integration |
| GAP-05 | Minor | Complete CTRL_BH06_001 definition (5 parameters) | Control loop |
| GAP-06 | Minor | Add fault alarm signal to signal list; document restart procedure after OI fault via HMI | Signals |
| GAP-07 | Admin | Correct authorship in title block | Title block |

---

## 5. RESPONSE REQUESTED

Please provide Rev C of P22-IT-06-008-101-B addressing the above items.

**Suggested deadline:** 2 weeks from date of this query (target: March 14, 2026).

Rev C will be reviewed by ADASA. If all gaps are resolved, the document will be formally
approved for PLC programming by BW Water.

---

## 6. DOCUMENT HISTORY

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 0 | 28-Feb-2026 | Initial issue | L. Rivera |
