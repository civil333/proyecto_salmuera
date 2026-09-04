---
titulo: "TECHNICAL REVIEW TRANSMITTAL N10"
subtitulo: "Second Stage RO Brine Module — Delivery 18 (25007-0018)"
codigo: "P22-TM-09-000-010-0"
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
fecha: "12-Mar-2026"
veredicto: "3 — TO BE REVISED"
---

# TECHNICAL REVIEW TRANSMITTAL N10

**Date:** March 12, 2026
**Project:** BAE 12803 — Second Stage RO Brine Module
**From:** ADASA — Aguas de Antofagasta S.A.
**To:** BW Water Americas Inc.
**Status:** FINAL

---

## 1. EXECUTIVE SUMMARY

**TRANSMITTAL VERDICT: 3 — TO BE REVISED**

Delivery 18 (25007-0018, received March 12, 2026) submits six documents: four approved as noted, two requiring revision. Seven observations are raised — six MAJOR, one MINOR. Required actions are detailed in Section 2.

Consolidated Comment Sheets (I/O List 7 items, Data Transfer List 3 items, Control Architecture 8 items) are reviewed; all responses are acceptable except one unfulfilled commitment — HMI Display Screenshots P22-BREAD-09-008-001 — tracked as NOTE-05.

---

## 2. DETAILED OBSERVATIONS BY DOCUMENT

### 2.1 I/O List Rev B — P22-LI-09-008-001

**Response Code: 2 — Approved as Noted**

Rev B incorporates motor RTDs (TE09-002/003/004/005), vibration transmitters (VT09-001/002/003), CIP Tank temperature transmitter, five new CIP valves, VFD electrical parameters via Ethernet/IP, eleven Power Meter readings via Modbus TCP/IP, and ADASA–module interface signals — closing TM N8 OBS-2.

#### OBS-01 — Motor temperature tag inconsistency (MAJOR)

The I/O List uses TE09-002/003 and TE09-004/005 for the four motor RTD inputs. The Data Transfer List submitted simultaneously maps the same physical instruments under TIT09-002/003 and TIT09-004/005. A field device cannot hold two different tags across project documents. TE designates a sensor-only element; TIT designates a transmitter with 4-20mA output — the correct functional class for these instruments.

A second conflict involves TIT-09-003 specifically. TM N8 datasheet P22-LI-09-008-013 assigned TIT-09-003 to the CIP Tank Temperature Transmitter. The Data Transfer List now assigns it to HP Pump Bearing Temperature (address 30009). BW Water must issue a consolidated resolution in I/O List Rev C and Data Transfer List Rev B: (1) adopt a single tag per instrument; (2) confirm the service of TIT-09-003; (3) update Instrument List Rev C accordingly.

*Technical Basis: ET — Communication and Control System; Instrument List Rev B; Data Transfer List Rev A*

#### NOTE-01 — Interface contact type (MINOR)

Items 19 and 21 specify "Dry Contact (N.O) 24VDC." Both signals must use relay contacts: ADASA PLC provides relay output for the DI enable; BW Water PLC must provide relay output for the DO running status. Update to "relay contact" in the next revision.

---

### 2.2 Data Transfer List (Modbus TCP/IP) Rev A — P22-LI-09-008-004

**Response Code: 2 — Approved as Noted**

Rev A delivers the complete Modbus TCP/IP map (64 DI, 16 DO, 109 analog points), closing TM N7 OBS-03.

#### OBS-02 — Conductivity ranges incompatible with brine conditions (MAJOR)

Three brine-side instruments carry Modbus scaling ranges that cannot cover their operating window:

| Tag | Location | DTL Range | Expected Range | Status |
|-----|----------|-----------|----------------|--------|
| CIT-09-001 | RO Cartridge Filter Discharge | 0–20 mS/cm | 65–80 mS/cm | NOT CORRECTED |
| CIT-09-004 | Interstage Turbocharger Inlet | 0–20 mS/cm | 85–108 mS/cm | NOT CORRECTED |
| CIT-09-005 | Concentrate Reject Discharge | 0–20 mS/cm | 108–133 mS/cm | NOT CORRECTED |

Expected conductivities are derived from Process Calculation P22-CD-09-009-001 Rev B (feed TDS 43,000–53,000 mg/L). BW Water must correct all three entries in Data Transfer List Rev B and Instrument List Rev C. CIT-09-001 and CIT-09-004, currently specified as contacting (Rosemount 400), must also be evaluated for toroidal technology per ET — Conductivity Transmitters (services above 20 mS/cm).

*Technical Basis: ET — Conductivity Transmitters; ET — Feed Brine Quality; Process Calculation P22-CD-09-009-001 Rev B*

#### OBS-03 — VE09-014 duplicated in DI block; level alarms absent (MAJOR)

Items 22–23 (addresses 10002.5–10002.6) assign VE09-014-SI001 and VE09-014-SIC001 as single-bit DI signals. These are REAL-type 0–100% signals already correctly mapped at analog addresses 40039 and 40071. Their presence in the DI block is a copy/paste error.

The correct entries at 10002.5–10002.6 are LS09-001-XB001 (Antiscalant Tank Level High) and LS09-002-XB001 (Antiscalant Tank Level Low) — both discrete DI signals from I/O List Rev B Items 128–129. These signals are entirely absent from the Modbus map. Add both in Rev B.

#### Cross-reference OBS-01

Data Transfer List Rev A uses TIT09-002/003/004/005 while the I/O List uses TE09-002/003/004/005 for the same instruments. See Section 2.1 OBS-01.

---

### 2.3 Control System Architecture Rev C — P22-CD-09-004-001

**Response Code: 2 — Approved as Noted**

Rev C confirms the network topology: Ethernet/IP for HMI, PLC, VFDs, and motorized valves; Modbus TCP/IP for DCS and Digital Power Meter; fiber optic DCS–LCP panel (installation by others). Digital Power Meter integration is confirmed, consistent with I/O List Items 1–11 and DTL Items 81–91.

#### OBS-04 — UPS 8-hour autonomy not confirmed (MAJOR)

TM N7 OBS-01 required UPS upgrade from 30 minutes to 8 hours per ET — Control and Automation System. The CCS states the architecture "has been revised." The submitted document is predominantly graphical; no UPS specification or capacity calculation is extractable. Provide written confirmation — in a comment sheet or technical note — that the UPS delivers 8-hour autonomy after grid loss, with a supporting capacity calculation (load list, battery bank specification).

#### NOTE-02 — Energy metering: progress noted, CEE pending (informational)

Digital Power Meter integration is confirmed; eleven electrical parameters appear in the I/O List and DTL. CEE (kWh/m³) calculation logic and HMI display must be confirmed in Control Philosophy Rev B.

#### NOTE-05 — HMI Display Screenshots not submitted (informational)

Control Architecture CCS Item 4 (response to TM N4) commits BW Water to submit P22-BREAD-09-008-001. The document has not been received. Required to verify HMI layout compliance with ET — HMI and Operator Interface and ISA 101. Submit with Entrega 19.

---

### 2.4 General Arrangement — Antiscalant Dosing Tank Rev A — P22-DWG-09-005-015

**Response Code: 2 — Approved as Noted**

Rev A shows tank geometry (OD 630 mm, body height 880 mm, total height 1120 mm) and nozzle schedule.

#### OBS-05 — Volume, material and seismic anchor data absent from Notes (MAJOR)

The Notes section is empty. Total installed volume, effective working volume, body material, and anchor data are not stated. A geometric estimate from the GA dimensions yields approximately 0.25 m³ — consistent with neither the accepted datasheet value (0.34 m³ total) nor the P&ID annotation (0.27 m³ effective). TM N9 OBS-02 remains unresolved.

Rev B must populate the Notes section with: (1) total installed volume, 0.34 m³ per accepted datasheet P22-ET-09-009-010 Rev B; (2) effective working volume, 0.27 m³; (3) body and liner material; (4) anchor bolt pattern and seismic reaction loads per ET — Seismic Conditions (NCh 2369, Zone 3, 2025 edition). The P&ID Rev C must simultaneously annotate TK-09-002 with 0.34 m³ total installed volume.

ET — Seismic Conditions (Section 4.4) requires that anchors of all main equipment associated with the module be designed for seismic Zone 3 per NCh 2369. The GA is the appropriate document to show anchor bolt layout, bolt size, and reaction loads that feed the civil foundation design.

*Technical Basis: ET — Seismic Conditions (NCh 2369, Zone 3); Datasheet P22-ET-09-009-010 Rev B*

---

### 2.5 General Arrangement — 1st Stage Feed Turbocharger Rev A — P22-DWG-09-005-012 (SIP-09-001)

**Response Code: 3 — To be Revised**

First submission. Four views at 1:2 scale; four grooved-end connections (Feed Inlet/Outlet 2", Brine Inlet/Outlet 1.5", CUT GROOVE STYLE 77).

#### OBS-06 — Vibration transducer mounting provision absent (MAJOR)

ET — Vibration Transmitters requires continuous vibration monitoring on each Energy Recovery Device. I/O List Rev B includes VT09-002-XQ001 (Item 43). GA Rev A shows no transducer mounting provision on SIP-09-001.

Rev B must show the vibration transducer mounting location with sensor type reference. If the FEDCO unit delivers monitoring via internal provisions with pre-wired leads, document that configuration on the GA.

*Technical Basis: ET — Vibration Transmitters; I/O List Rev B Item 43*

#### NOTE-03 — Coupling pressure rating (informational)

TM N6 OBS-01 rejected the turbocharger datasheet for coupling pressure rating downgraded to 1,200 psi (19% margin over 1,008 psi operating). GA Rev A specifies CUT GROOVE STYLE 77 on all nozzles. Provide the working pressure rating certificate for Style 77 couplings at 1.5" and 2" bore, and a deviation disposition resolving TM N6 OBS-01.

---

### 2.6 General Arrangement — 2nd Stage Interstage Turbocharger Rev A — P22-DWG-09-005-013 (SIP-09-002)

**Response Code: 3 — To be Revised**

First submission. Four views at 1:2 scale; connections identical to SIP-09-001 (CUT GROOVE STYLE 77).

#### OBS-07 — Vibration transducer mounting provision absent (MAJOR)

Same deficiency as OBS-06 for SIP-09-001. I/O List Rev B includes VT09-003-XQ001 (Item 48). GA Rev A shows no mounting provision for the vibration transducer. Rev B must document the mounting location per Section 2.5 OBS-06 requirements.

#### NOTE-04 — Coupling pressure rating (informational)

CUT GROOVE STYLE 77 connections on SIP-09-002 carry the same pressure rating concern as SIP-09-001. The rating certificate must cover both units.

---

## 3. ATTACHMENTS

| Attachment | Document Code | Title | Rev |
|------------|---------------|-------|-----|
| 1 | P22-LI-09-008-001 | I/O List | B |
| 2 | P22-LI-09-008-004 | Data Transfer List (Modbus TCP/IP) | A |
| 3 | P22-CD-09-004-001 | Control System Architecture | C |
| 4 | P22-DWG-09-005-015 | General Arrangement — Antiscalant Dosing Tank | A |
| 5 | P22-DWG-09-005-012 | General Arrangement — 1st Stage Feed Turbocharger (SIP-09-001) | A |
| 6 | P22-DWG-09-005-013 | General Arrangement — 2nd Stage Interstage Turbocharger (SIP-09-002) | A |

---

## 4. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-LI-09-008-001 | I/O List | B | 2 — Approved as Noted |
| P22-LI-09-008-004 | Data Transfer List (Modbus TCP/IP) | A | 2 — Approved as Noted |
| P22-CD-09-004-001 | Control System Architecture | C | 2 — Approved as Noted |
| P22-DWG-09-005-015 | General Arrangement — Antiscalant Dosing Tank | A | 2 — Approved as Noted |
| P22-DWG-09-005-012 | General Arrangement — 1st Stage Feed Turbocharger (SIP-09-001) | A | 3 — To be Revised |
| P22-DWG-09-005-013 | General Arrangement — 2nd Stage Interstage Turbocharger (SIP-09-002) | A | 3 — To be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED**

Seven observations require resolution before the next delivery. Required actions are detailed in Section 2.
