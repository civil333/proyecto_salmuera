---
codigo: CORREO-2026-03-11-TM-N7
autor: Luis Rivera
fecha: 2026-03-11
version: 1.0
estado: LISTO - PENDIENTE ENVIO
---

# Correo: Transmittal N7 — Submittal 25007-0014

## Header

| Campo | Valor |
|-------|-------|
| Date | March 11, 2026 |
| From | Luis Rivera — Contract Administrator (ADASA) |
| To | Eduardo Yamauchi — BW Water Americas Inc. |
| CC | Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim |
| Subject | ADASA – Taltal Brine Module: Technical Review Transmittal N7 — Submittal 25007-0014 |
| Ref | Contract C-4300 / BAE 12803 / P22-TM-09-000-007-0 |

---

## Cuerpo del Correo

Dear BW Water Project Team,

Please find attached Transmittal N7 (P22-TM-09-000-007-0), corresponding to your Submittal 25007-0014 (4 documents). All four documents received a verdict of **Code 3 — To Be Revised**.

---

**Control Philosophy Rev A — 12 observations, 3 critical findings:**

**UPS Backup Duration — CRITICAL:** The Control Philosophy specifies a 30-minute UPS backup for the module control system. Contract C-4300 — ET — Communication and Control System requires a minimum of 8 hours of uninterrupted operation. This is a direct non-conformance with the contractual baseline and must be corrected in Rev B.

**CEE/MVE Not Described — CRITICAL:** The Energy Efficiency Control (CEE) and Energy Recovery Verification (MVE) functions are listed in ET — Communication and Control System as contractual guarantees, but are absent from the Control Philosophy. Without a documented description of these functions, ADASA cannot verify contractual compliance during commissioning.

**Enable Permissive Interface — MAJOR:** The Control Philosophy defines two individual DI signals (tank level high, tank level low) as the module start permissive. The correct interface, as confirmed by both parties, is: one DI relay contact (ADASA → module: general enable) and one DO relay contact (module → ADASA: operational status). The current definition does not match the agreed signal interface per ET — Communication and Control System and IO List Rev A.

---

**Piping Layout — distance non-conformance:**

CIP connections and dosing points are located at 11,150 mm from the module boundary — more than three times the 3.5 m limit established in Transmittal N5. Additionally, sliding door access and equipment maintenance clearances are not shown on the layout.

---

**Overdue items from previous transmittals:**

- Modbus Memory Map (TM N2): **65 days overdue** — no response received.
- IO List (TM N3): **44 days overdue** — no response received.

Annotated PDFs are available at: http://gofile.me/7k8qL/RHWabtKCE

Please confirm receipt of this transmittal and provide a response schedule for Rev B submissions.

Best regards,

Luis Rivera
Project Engineer
ADASA — Aguas de Antofagasta S.A.

---

## Contexto Interno (No enviar)

- Correo asociado a TM N7 (P22-TM-09-000-007-0), emitido 08-Mar-2026.
- Incorpora comentarios de Ronald Pellejero (11-Mar-2026) sobre interfaz permisivo: 1 DI relay contact (ADASA→módulo, habilitación general) + 1 DO relay contact (módulo→ADASA, estado operacional). Fuente: confirmación directa Ronald, MEMORY.md.
- Revisiones de notación aplicadas según CLAUDE.md §2.5: referencias a secciones de documentos BW Water con nombre completo de sección (sin "§N.N").
- Attachment 4: Control Philosophy Rev A con 12 anotaciones ADASA disponible en gofile.
- PDFs originales BW Water con marcas ADASA: link gofile.me compartido con equipo.
- OBS-11 (permisivo incorrectamente definido) y OBS-12 (permisivo HP sin presión mínima) incorporados en TM N7 Rev final (10-Mar-2026).
