---
codigo: CORREO-2026-03-16-TM-N10
autor: Luis Rivera
fecha: 2026-03-16
version: 1.0
estado: LISTO - PENDIENTE ENVIO
---

# Correo: Transmittal N10 — Submittal 25007-0018 (I/O List, DTL, Control Architecture, GAs)

## Header

| Campo | Valor |
|-------|-------|
| Date | March 16, 2026 |
| From | Luis Rivera — Contract Administrator (ADASA) |
| To | Eduardo Yamauchi — BW Water Americas Inc. |
| CC | Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim |
| Subject | ADASA – Taltal Brine Module: Technical Review Transmittal N10 — Submittal 25007-0018 |
| Ref | Contract C-4300 / BAE 12803 / P22-TM-09-000-010-0 |

---

## Cuerpo del Correo

Dear BW Water Project Team,

Please find attached Transmittal N10 (P22-TM-09-000-010-0), covering Submittal 25007-0018 (6 documents: I/O List Rev B, Data Transfer List Rev A, Control System Architecture Rev C, GA Antiscalant Dosing Tank Rev A, GA SIP-09-001 Rev A, GA SIP-09-002 Rev A). **Transmittal verdict: Code 3 — To Be Revised.**

---

**Progress acknowledged:** The Data Transfer List Rev A delivers the complete Modbus TCP/IP memory map, closing TM N7 OBS-03 outstanding since Transmittal N3. I/O List Rev B incorporates vibration transmitters, motor RTDs, and the ADASA–module interface signals. Control System Architecture Rev C confirms Ethernet/IP topology and Digital Power Meter integration.

**Seven MAJOR observations require resolution:**

- **OBS-01 — Motor temperature tag conflict:** I/O List uses TE09-002/003/004/005; Data Transfer List maps the same instruments as TIT09-002/003/004/005. Conflicting assignment of TIT-09-003 between HP Pump bearing and CIP Tank. Single tag per instrument required across all documents.
- **OBS-02 — Conductivity ranges incompatible with brine:** CIT-09-001/004/005 remain at 0–20 mS/cm. Expected service conductivities are 65–133 mS/cm. Raised in TM N8; uncorrected in this submittal.
- **OBS-03 — DI block error and missing level alarms:** VE09-014 position feedback appears in DI block (addresses 10002.5–10002.6) — it is an analog signal already mapped correctly. LS09-001/002 (Antiscalant Tank Level High/Low) are in the I/O List but absent from the Modbus map.
- **OBS-04 — UPS 8-hour autonomy not confirmed:** Control System Architecture Rev C does not confirm the upgrade from 30 min to 8 h required in TM N7 OBS-01. Written confirmation with capacity calculation required.
- **OBS-05 — GA Antiscalant Tank: volume and material absent:** Notes section empty. Total installed volume, effective volume, and body material must be specified per accepted datasheet (0.34 m³ total).
- **OBS-06 — GA SIP-09-001: monitoring provisions absent:** No vibration transducer mounting point and no Pt-100 RTD connection on bearing housing shown on the GA.
- **OBS-07 — GA SIP-09-002: same as OBS-06 for the second unit.**

---

Please confirm receipt and provide a revised submission schedule covering all open items.

Best regards,

Luis Rivera
Project Engineer
ADASA — Aguas de Antofagasta S.A.

Best regards,

Luis Rivera
Project Engineer
ADASA — Aguas de Antofagasta S.A.

---

## Contexto Interno (No enviar)

- Transmittal N10 (P22-TM-09-000-010-0) emitido 12-Mar-2026. Correo enviado 16-Mar-2026.
- 6 documentos Submittal 25007-0018: IO List Rev B, DTL Rev A, Control Arch Rev C, GA TK-09-002 Rev A, GA SIP-09-001 Rev A, GA SIP-09-002 Rev A.
- Veredicto global: Code 3 — To Be Revised. 4 Code 2 + 2 Code 3.
- Progreso positivo reconocido: DTL cierra TM N7 OBS-03 (Modbus TCP/IP, 65+ días pendiente). IO List Rev B incorpora VTs y RTDs solicitados en múltiples TMs.
- 7 observaciones MAJOR activas (OBS-01 a OBS-07). Una MINOR (NOTE-01 sobre tipo relay contact en items 19/21 — no incluida en el correo para no saturar; queda en el transmittal formal).
- Párrafo de pendientes previos incluido para presión formal sobre Valve List Rev C (deadline hoy 16-Mar), Feed TC Rev D, Control Philosophy Rev B.
- Reemplazar [LINK_PLACEHOLDER] con el link real (Synology/gofile) antes de enviar.
- Al enviar: registrar en README.md §2 (resumen) y §9 (detalle).
