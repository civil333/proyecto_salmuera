---
titulo: "TECHNICAL REVIEW TRANSMITTAL N9"
subtitulo: "Second Stage RO Brine Module — P&ID Rev B"
codigo: "P22-TM-09-000-009-0"
version: "Rev.0"
autor: "ADASA"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Luis Rivera"
aprobado_por: "Victor Gutierrez"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
fecha: "11-Mar-2026"
---

# TECHNICAL REVIEW TRANSMITTAL N9

**Date:** March 11, 2026
**Project:** BAE 12803 — Second Stage RO Brine Module
**From:** ADASA — Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** FINAL

---

## 1. EXECUTIVE SUMMARY

### Key Findings

**TRANSMITTAL VERDICT: 2 — APPROVED AS NOTED**

BW Water Delivery 17 (Submittal 25007-0017, received March 11, 2026) submits the P&ID
Revision B (P22-DWG-09-009-002). This is the first P&ID revision since Transmittal N2,
which identified 13 open observations on Rev A. All 13 observations are addressed in
Rev B, accompanied by a Consolidated Comment Sheet with BW Water's responses. ADASA
acknowledges this as a substantive step forward.

Rev B closes all outstanding TM N2 observations: high-pressure lines confirmed in Super
Duplex Stainless Steel; battery limits show flanged tie-in points with TAGs and diameters;
1st and 2nd stage labels added; valve and instrument TAGs completed per the project
coding convention; and the legend revised. The Static Mixer TAG (MZE-09-001) is now
consistent with the datasheet, closing an indirect observation from Transmittal N3.

Two minor notes prevent unconditional approval. The document code in the title block
reads P22-DWG-09-009-02 (two-digit correlativo) where P22-DWG-09-009-002 is required.
The antiscalant tank annotation shows 0.27 m³ (effective working volume) where 0.34 m³
(total installed volume per the accepted datasheet) is the correct P&ID annotation.
Neither item affects the engineering content of the drawing.

**Note on VM-09-015:** The P&ID correctly shows VM-09-015 (HP Pump to Feed Turbocharger
isolation) as a manual valve. ADASA formally withdrew TM N3 OBS-11 in its March 5, 2026
response after BW Water confirmed that this valve serves as a maintenance isolation point
and is not a process control valve subject to ET — Valves and Piping electric actuation
requirement. An unresolved inconsistency remains in the Valve List: Rev B item 18
records VM-09-015 as ON/OFF MOTORIZED, contradicting its confirmed manual function.
Valve List Rev C must resolve this inconsistency.

### Notes

| # | Observation | Severity |
|---|-------------|----------|
| NOTE-01 | Document code P22-DWG-09-009-02 in title block; correct code is P22-DWG-09-009-002 (three-digit correlativo). | MINOR |
| NOTE-02 | TK-09-002 annotated as 0.27 m³ (effective volume); total installed volume per accepted datasheet is 0.34 m³. | MINOR |

---

## 2. GENERAL INFORMATION

| Field | Value |
|-------|-------|
| **Transmittal Code** | P22-TM-09-000-009-0 |
| **Submittal** | 25007-0017 |
| **Delivery date** | 11-Mar-2026 |
| **Review completion** | 11-Mar-2026 |
| **Total documents reviewed** | 1 |
| **Response code** | 2 — Approved as Noted |
| **Response codes reference** | 1=Approved, 2=Approved as Noted, 3=To be Revised, 4=Rejected, 5=For Information |
| **Contract** | C-4300 BW WATER SUPPLY-12803 V2 |

---

## 3. DETAILED OBSERVATIONS BY DOCUMENT

### 3.1 Piping and Instrumentation Diagram Rev B — P22-DWG-09-009-002

**Response Code: 2 — Approved as Noted**

Rev B includes a Consolidated Comment Sheet covering the 13 open observations from
Transmittal N2 (OBS-01 through OBS-14, excluding OBS-09 which was already closed
by the Process Calculation review). All 13 observations are addressed.

#### TM N2 Observations — Status in Rev B

| TM N2 OBS | Description | BW Water Response | ADASA Assessment |
|-----------|-------------|-------------------|------------------|
| OBS-01 | Battery limits with flange | Added accordingly | **CLOSED** |
| OBS-02 | PVC lines within SDSS zone | HP = SDSS; PVC only for LP (permeate, CIP) | **CONDITIONALLY CLOSED** — see Note 1 |
| OBS-03 | Line TAGs with diameter | Added accordingly | **CLOSED** |
| OBS-04 | Drainage stream routing | Revised accordingly | **CLOSED** |
| OBS-05 | Battery limit: flange + TAG + diameter | Revised accordingly | **CLOSED** |
| OBS-06 | CIP connection to TK-09-001 | Revised accordingly | **CLOSED** |
| OBS-07 | HP Pump characteristics (BH-09-001) | Added accordingly | **CLOSED** |
| OBS-08 | 1st and 2nd stage labels | Revised accordingly | **CLOSED** |
| OBS-09 | Design pressures | Already closed in TM N2 | CLOSED (TM N2) |
| OBS-10 | SDSS material confirmation in HP lines | All HP lines shall be in SDSS | **CLOSED** |
| OBS-11 | Valve TAGs | Added; VE = motor actuated, VM = manual | **CLOSED** |
| OBS-12 | Instrument TAGs | Added per tagging procedure | **CLOSED** |
| OBS-13 | Flow direction arrows | Added more arrows | **CLOSED** |
| OBS-14 | Legend update | Legend revised | **CLOSED** |

**Note 1 — OBS-02 Residual (PVC lines and SDSS zone boundary):** BW Water confirmed
the material policy: HP lines = SDSS; LP lines (permeate, CIP) = PVC. This policy is
correct. The original concern was about PVC pipes visually appearing within the
high-pressure zone rectangle. Physical routing segregation cannot be evaluated from
the P&ID alone; the Piping Layout (P22-DWG-09-005-004 Rev B, pending since
Transmittal N7 OBS-01) must confirm that PVC lines do not physically route through
the HP equipment zone. The P&ID OBS-02 is conditionally closed pending Piping
Layout Rev B.

---

#### Note 1 — Document code truncated in title block (MINOR)

The title block shows ADASA Code: P22-DWG-09-009-02. The project coding system requires
a three-digit correlativo: P22-DWG-09-009-002. The CCS itself correctly references
P22-DWG-09-009-002 throughout, confirming this is a title block transcription error.
Correct the title block in Rev C.

---

#### Note 2 — Antiscalant Tank TK-09-002: effective volume annotated rather than total installed volume (MINOR)

The P&ID Rev B annotates TK-09-002 with VOL: 0.27 m³. The accepted Antiscalant Dosing
Tank Datasheet (P22-ET-09-009-010 Rev B, Transmittal N4) specifies a total capacity of
0.34 m³ and an effective working volume of 0.27 m³. Transmittal N4 OBS-11 requested
updating the P&ID from 0.25 m³ to 0.34 m³ (total capacity). Rev B was updated to
0.27 m³ (effective volume). P&ID convention is to annotate the total installed tank
volume. Update TK-09-002 to 0.34 m³ in Rev C.

---

#### Indirect Observations — Status in Rev B

| Origin | Observation | Rev B Status |
|--------|-------------|-------------|
| TM N3 OBS-14 / TM N6 Note | Static Mixer TAG: MZE-09-009 vs MZE-09-001 | **CLOSED** — Rev B shows MZE-09-001 |
| TM N4 OBS-11 | Antiscalant Tank capacity: update P&ID from 0.25 m³ to 0.34 m³ | **PARTIALLY CLOSED** — updated to 0.27 m³ (effective); 0.34 m³ total required (NOTE-02 above) |
| TM N3 OBS-11 | VM-09-015 electric actuation | **WITHDRAWN** — ADASA email 05-Mar-2026. Valve confirmed as manual maintenance isolation (HP Pump to Feed Turbocharger); ET — Valves and Piping electric actuation requirement does not apply. P&ID shows VM prefix correctly. |

---

## 4. ATTACHMENTS

| Attachment | Document Code | Title | Rev |
|------------|---------------|-------|-----|
| 1 | P22-DWG-09-009-002 | Piping and Instrumentation Diagram (ADASA annotated) | B |

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-DWG-09-009-002 | Piping and Instrumentation Diagram | B | 2 — Approved as Noted |

**Overall Transmittal Verdict: 2 — APPROVED AS NOTED**

Notes to address in Rev C:
1. Correct document code P22-DWG-09-009-002 in title block (NOTE-01 — MINOR)
2. Update TK-09-002 annotation to 0.34 m³ total installed volume (NOTE-02 — MINOR)
