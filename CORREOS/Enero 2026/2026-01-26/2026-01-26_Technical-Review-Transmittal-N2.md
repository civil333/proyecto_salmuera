---
titulo: "Technical Review Transmittal N2"
subtitulo: "BAE 12803 - Brine Module Taltal"
codigo: "P22-TM-09-000-002-0"
version: "Rev.1"
autor: "ADASA"
empresa: "ADASA"
preparado_por: "Luis Rivera"
revisado_por: "Gerencia Tecnica ADASA"
tipo_documento: "Correo"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# Technical Review Transmittal N2 - BAE 12803 Brine Module Taltal

**Date:** January 27, 2026
**From:** Luis Rivera (ADASA)
**To:** BW Water Team
**Subject:** P22-TM-09-000-002-0 | Technical Review Transmittal N2 - Submittals 0003-0007

---

Dear BW Water Team,

Please find attached the Technical Review Transmittal N2 (P22-TM-09-000-002-0) covering Submittals 0003 through 0007.

**Key Highlights:**

Process Calculation Rev B (P22-CD-09-009-001-B) has been reviewed and **validates critical design parameters**, including:
- Design pressures with 10% margin (Stage 1: 70 bar, Stage 2: 85 bar)
- Turbocharger modeling for 43k and 53k TDS scenarios
- Membrane configuration (70 elements total)
- Permeate quality guarantee (TDS < 500 mg/L)

This validation allows closure of previously blocking observations on P&ID and equipment datasheets.

**Pending Critical Actions:**

| # | Document | Issue | Severity |
|---|----------|-------|----------|
| 1 | A/C Thermal Calculation | Calculated heat load 5.96 kW vs estimated ~10-12 kW (missing: PLC 2.0 kW, lighting 0.16 kW, wall transmission, solar radiation) | HIGH |
| 2 | A/C Thermal Calculation | Missing n+1 redundant unit per ET 5.1.11 and Technical Offer (2 A/C 1W+1S offered) | HIGH |
| 3 | A/C Thermal Calculation | No safety margin included (typical 10-15% for HVAC sizing) | MEDIUM |
| 4 | Static Mixer | Material change FRP to PVC requires technical justification | MEDIUM |
| 5 | Control Architecture | Provide Modbus TCP memory map for DCS integration | MEDIUM |

A detailed heat load analysis has been included in the transmittal showing the breakdown of missing thermal loads.

**Download Link for Reviewed Documents:**
https://www.dropbox.com/t/INLfLK7p4ISQiAnz

Please do not hesitate to contact us should you have any questions.

Best regards,

**Luis Rivera**
ADASA - Aguas de Antofagasta S.A.
Project: BAE 12803 - Second Stage RO Brine Module

---

## Attachments
- TRANSMITTAL N2 ADASA-BW_WATER.docx
- P22-DWG-09-009-002_A - P&ID Coment LH.pdf
- P22-ET-09-009-001-B Datasheet of UHPRO System Coment LH.pdf
- P22-ET-09-009-003-B_Datasheet of RO CIP Pump Coment LH.pdf
- P22-ITEM-09-009-012-A_Datasheet of Static Mixer Coment LH.pdf
- P22-CD-09-009-001-B_Process Calculation.pdf
- CC P22-CD-09-004-001_A CONTROL ARCHITECTURE.pdf
