# RFI 25007-RO-RFI-0002 — ADASA Reply (registro interno)

> **Estado: ENVIADO 07-Jul-2026.** Este `.md` NO se envía; es la fuente del texto y el registro de trazabilidad. El deliverable emitido es `RFI-002 Panel Enclosure Nema 4_IP66_ADASA_REPLY.docx` (form lleno) + su correo de cobertura (`CORREOS/Julio 2026/2026-07-07/2026-07-07_RFI-002-Enclosure-Reply.docx`).

## Datos del RFI

| Campo | Valor |
|---|---|
| Ref. No | 25007-RO-RFI-0002 |
| Issued Date | 1 July 2026 |
| From (emisor) | Billy Tan — BW Water / Engineering |
| To | Luis Rivera Gonzalez — Aguas Antofagasta / Projects |
| Spec Ref | P22-ET-09-000-001-0 |
| Subject | Clarification of LCP Enclosure Material Specification – Outline Drawing vs. Approved LCP Datasheet |

## Bloque "Replied Information" que ADASA llena

| Celda | Valor |
|---|---|
| To (Name) | Billy Tan |
| Company / Department (To) | BW Water / Engineering |
| From (Name) | Luis Rivera Gonzalez |
| Company / Department (From) | Aguas Antofagasta / Projects |
| Replied Date | 07 Jul. 2026 |

## Pregunta de BW Water (resumen)

BW Water reconcilia la contradicción documental que ADASA observó en el Outline Panel Drawing (MATERIAL "Sheet Steel (Interior Only)" + FINISHING RAL7035 vs "Exterior SUS316L" y el datasheet aprobado). Confirma exterior SS316L/NEMA 4X/IP66, sube los gland plates a SS316L, y pide aceptar que los componentes internos de montaje sean galvanizado/laminado (estándar nVent, no afectan el rating) + autorizar reemitir el Outline. No busca relajar el requisito.

## Respuesta de ADASA (cuerpo del form — 4 párrafos)

**Replied Date: 07 Jul. 2026**

1. ADASA confirms that the external enclosure body, external door, roof, rear panel, plinth and the gasketed gland plates on the upper and lower bases shall be Stainless Steel 316L, unpainted, in accordance with the approved Datasheet of Local Control Panel (LCP), P22-ET-09-007-005 Rev 1 (nVent Hoffman Type FS FS66S, SS316L, NEMA 4X / IP66). The Technical Specification (P22-ET-09-000-001-0), Section 5.4.1 - Constructive Characteristics, requires the upper and lower bases to carry a bolted metal plate with gaskets for the cable glands and a protection class of NEMA 4X or its IP equivalent; ADASA notes and accepts BW Water's confirmation that the gland plates change to SS316L, which maintains that requirement.

2. The internal mounting components that are not exposed to the external environment — mounting plate, internal swing door and internal frame — may be supplied in galvanized or cold-rolled steel in accordance with the manufacturer's standard construction. The Technical Specification, Section 5.4.1 - Constructive Characteristics, permits measuring, switching and control equipment to be mounted inside the cabinet provided the protection grade is not lower than NEMA 4X; these internal materials do not reduce the enclosure protection, which remains NEMA 4X / IP66. The Gray RAL 7035 finishing is accepted only on internal components and surfaces; the external SS316L enclosure remains unpainted as specified in the approved datasheet.

3. This is a documentation clarification, not a material or design deviation. The Technical Specification, Section 5.4.3 - Finishing, allows a stainless steel enclosure, and the approved LCP Datasheet fixes that stainless steel as SS316L; the Outline Panel Drawing must align to it. BW Water shall re-issue the PLC-LCP Outline Panel Drawing (P22-CD-09-008-001) at the next revision, distinguishing the external SS316L enclosure components from the internal mounting components, restricting the Gray RAL 7035 finishing to internal surfaces, and stating the protection class in full as "NEMA 4X / IP66". This closes the observation on the Outline Panel Drawing tracked since Transmittal N20 and re-issued at Transmittal N25.

4. This confirmation is conditional on the external enclosure and gasketed gland plates being Stainless Steel 316L and on the enclosure maintaining a protection class not lower than NEMA 4X per the Technical Specification, Section 5.4.1 - Constructive Characteristics. The observations on the Outline Panel Drawing remain in force until the corrected revision is submitted and approved.

## Contexto interno (no enviar)

- **Anclas de consistencia:** datasheet LCP Rev 1 aprobado **Código 1 en TM N25** (no N24); Outline Panel Drawing **Código 3** (CRITICAL en TM N20, reiterado en N25) = único gate abierto; SLD Rev 0 aprobado Código 1 en TM N20 (rótulo "METAL CLAD, NEMA4X/IP66").
- **Matiz §7.6 (anti-over-reach):** la ET (Finishing) **permite** acero inoxidable O pintado 3 capas ≥100µm → **NO afirmar que la ET exige SS316L**; el SS316L lo fija el datasheet aprobado de BW Water. El **NEMA 4X** sí es requisito ET (Constructive Characteristics), citado por nombre. Los internos galvanizados los habilita la propia ET ("equipos montados siempre que se mantenga NEMA 4X").
- **Coherencia con el correo D3** (PLC delay, mismo día, cadena separada): ambos sostienen que el Outline fue la desviación y el datasheet aprobado gobierna. El RFI-002 resuelve el material; el D3 reserva la responsabilidad del atraso.
- Referencias por nombre completo de documento/sección; sin §N, sin códigos internos (OBS/Code), 100% inglés.
