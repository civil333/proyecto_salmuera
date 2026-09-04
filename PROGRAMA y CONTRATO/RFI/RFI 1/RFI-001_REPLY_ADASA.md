<!-- Registro interno ADASA — fuente del texto cargado en el form RFI-001 (Replied Information). NO se envía; el deliverable es RFI-001 ..._ADASA_REPLY.docx -->

# RFI-001 — Reply (ADASA)

| Campo | Valor |
|---|---|
| RFI Ref. | 25007-RO-RFI-0001 |
| Subject | Clarification on Compliance of Standard Analog Input Modules with Instrumentation Requirement "4-20 mA + HART" |
| Spec Ref. | P22-ET-09-000-001-0 (Section 5.5 — Instrumentation Specification) |
| Issued | 22 Jun. 2026 (BW Water — Billy Tan) |
| Replied | 24 Jun. 2026 (ADASA — Luis Rivera Gonzalez) |
| Reply To | Billy Tan — BW Water / Engineering |
| Reply From | Luis Rivera Gonzalez — Aguas Antofagasta / Projects |

## Reply text (cargado en la celda de cuerpo del bloque "Replied Information")

ADASA confirms that compliance with the Technical Specification, Section 5.5 — Instrumentation Specification, is achieved under the configuration described in the Contractor Understanding, namely: all field instruments supplied as 4-20 mA with HART communication capability; HART communication available locally at the field instrument through a handheld HART communicator; and the PLC analog input module (Allen-Bradley 5069-IF8) acquiring the 4-20 mA process variable, with the 250 ohms resistor noted on the module datasheet allowing an external HART device (e.g. a handheld communicator) on the loop, preserving field HART access.

Section 5.5 sets the instrumentation signal protocol as 4-20 mA + HART at the field-instrument level. It does not require HART pass-through to the PLC or SCADA, HART-capable I/O modules, or a dedicated HART asset-management solution. The control-system communication required by the Specification is Modbus TCP/IP over Ethernet, which is unaffected. The alternative HART-capable I/O hardware referenced in the RFI is therefore not required, with no associated cost, engineering, procurement or schedule impact.

Transmittal N24 already confirmed the 4-20 mA + HART instrumentation requirement as met by the offered transmitters (all 4-20 mA + HART) and closed the point; this disposition is consistent with that.

This confirmation is conditioned on every field instrument being supplied as 4-20 mA + HART-capable. Any instrument supplied as 4-20 mA only, without HART capability, would not comply with Section 5.5; the observations previously issued on instruments lacking HART capability remain in force.
