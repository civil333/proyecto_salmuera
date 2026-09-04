---
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-06-03
cliente: BW Water
estado: ENVIADO
asunto: "RE: 25007 Taltal: Ground cable schedule clarification"
---

# Correo — Respuesta a la contra-pregunta BW Water sobre Grounding Layout Rev F (TM N19)

**Date:** June 3, 2026
**From:** Luis Rivera — Project Engineer (ADASA)
**To:** Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)
**CC:** Billy Tan, Adzlan Bin Abd Rahim, Jeryl F. Regulacion, Stephane Gehant, David Chee Keat Swee, Sadeep Irugalbandara, Nick Huta, Victor Gutierrez (ADASA)
**Subject:** RE: 25007 Taltal: Ground cable schedule clarification
**Ref:** Contract C-4300 / BAE 12803 / Technical Review Transmittal N19 (P22-TM-09-000-019-0, 25-May-2026) / Grounding Point & Power Panel Location Layout Rev E (P22-DWG-09-007-003)

---

## CUERPO DEL CORREO (a enviar — inglés)

Dear Eduardo,

Thank you for your message of 2-Jun-2026. We are glad to provide clarification on any of the Transmittal N19 comments, and we welcome these questions ahead of Rev F. Our position on each point raised on the Grounding Point & Power Panel Location Layout (Rev E) is set out below.

**1. Dependency on the Equipment Layout.** The Equipment Layout (P22-DWG-09-005-003) and the Piping Layout (P22-DWG-09-005-004) are **both approved (Code 2)**, issued in Transmittal N15 on 22-Apr-2026. This satisfied the condition set in Transmittal N11, under which the Grounding layout was to follow their acceptance, so the layout dependency is now closed and Rev F can proceed without further wait. A direct consequence follows: with the arrangement approved, **the position of the main panel (LCP / Main Switchboard, P22-LCP-01) is fixed and must not be relocated in Rev F**. We therefore do not accept note 5 of Rev E, which reads "panel locations are indicative only and subject to relocation based on site condition": the main panel position is set by the approved Equipment Layout, and any change to it requires a revised layout approved by ADASA, not a site decision. Please prepare Rev F on the approved Equipment Layout (Rev B), keeping the main panel and the grounding points at the positions of that accepted arrangement. We have no record of a formal Equipment Layout Rev C; if you hold a later revision internally, submit it, but it does not block Rev F. The item that has stayed open since Transmittal N11 is the grounding schedule itself, which point 2 addresses.

**2. Grounding schedule.** Yes, the grounding schedule is the deliverable that closes this item, open since Transmittal N11 and carried through Transmittal N15 and Transmittal N17. The schedule you attached is the right format and is substantially complete: it lists the PE points, the conductor sizes, the ring-main topology, the equipotential bonding and the ADASA-scope main grounding connection. A separate template-approval step is therefore not necessary. To close the item, carry this schedule into Rev F, either on the drawing or as a referenced annex, and we will assess it formally when Rev F is reviewed. One refinement to fold in: the Cable Specification column shows Cu/PVC throughout, while the drawing's own Material Take-Off already lists a copper earth link, tinned braided copper and a copper bar for the ring main and tray bonding. Reconcile the two so the schedule distinguishes the bare or braided copper of the earth electrode and ring main from the insulated PE conductors used for equipment bonding, consistent with the interconnection drawing P22-DWG-06-006-101 and with NCh Eléctrica 4/2003 Section 10.0.

**3. Consolidated Comment Sheet description.** Noted. With the description corrected to "Grounding Point & Power Panel Location Layout", and the sheet now carrying the comment-closure record for this drawing rather than for the Cable Tray Layout, the Transmittal N17 observation closes when we review Rev F, provided the sheet is legible (see point 5).

**4. Grounding method reference.** The detail we asked for in Transmittal N17 is the resolution of the cross-reference printed on the drawing: confirm that the typical detail it points to is contained in the Typical Installation Details of Power Works (P22-DWG-09-007-005, Rev C). On top of that, designate which of the seven grounding methods shown on that drawing applies to each load type, following IEC 60364-5-54. If the cross-reference resolves and the method is designated, no detail different from Rev E is needed. While on this point, please align the conductor cross-section basis to IEC 60364-5-54 across the whole drawing: note 8 on page 2 still cites NEC Table 250.122, whereas page 3 already cites IEC 60364-5-54, and the basis adopted in Transmittal N17 is IEC 60364-5-54.

**5. Revision history and screenshots.** The status labels "Issued for Approval" (Rev A) and "Revised as per Comment" (Rev B onward) are correct as status, but they are not what our comment asks for. Add a one-line description of what actually changed in each revision from Rev B through Rev E, with the ECN reference where applicable, so the history block is traceable. On the screenshots: pasting captures from the Transmittal PDF into the Consolidated Comment Sheet is not prohibited. The point of our note was legibility, since the Rev E sheet came through partly unreadable. Issue the sheet from the electronic source at a resolution that reads clearly, regardless of where the content originates.

**6. Schedule.** With the layout dependency resolved, there is no longer a basis to defer Rev F. As a one-time accommodation for raising these clarifications, we extend the Rev F due date set in Transmittal N19 to Wednesday 17-Jun-2026 (ten working days from this reply).

We look forward to Rev F.

Best regards,

**Luis Rivera**
Project Engineer
ADASA — Aguas de Antofagasta S.A.

---

## Contexto Interno (No enviar)

Base factual verificada que sustenta cada punto. **No forma parte del correo.**

**Origen.** Correo de Eduardo Yamauchi 02-Jun-2026 23:05 (reenvía consulta de Billy Tan, EIC, 28-May), thread "25007 Taltal: Ground cable schedule clarification". Adjuntos: `comment.xlsx` (las 4 preguntas), `Ground Cable Schedule sample.pdf`, `P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf`, `TM N19 Grounding ADASA comment.pdf`. Carpeta fuente: `REVISIONES/TRANSMITTALES/P22-TM-09-000-019-0/CONTRA PREGUNTA BW WATERS/`.

**Punto 1 — la dependencia la creó ADASA y ya está resuelta.** TM N11 OBS-03 (literal): *"BW Water must resubmit Grounding Point & Power Panel Location Layout as Rev C after Equipment Layout (P22-DWG-09-005-003) and Piping Layout (P22-DWG-09-005-004) are revised and accepted by ADASA."*
- Equipment Layout P22-DWG-09-005-003: Rev A Code 3 (TM N5) → **Rev B Code 2 (TM N15, 22-Abr-2026)**. No hay Rev C formal (Master Register fila 74).
- Piping Layout P22-DWG-09-005-004: Rev A Code 3 (TM N7) → **Rev B Code 2 (TM N15, 22-Abr-2026)**; restricción footprint 3.500 mm retirada por ADASA (Master Register fila 42).
- TM N15 registró la parte de alineación de layout de OBS-03 como resuelta. Lo que sigue abierto y reincidente (TM N11 → TM N15 NOTE-03 → TM N17 → TM N19 OBS-01) es el **grounding schedule**, no el layout. Por eso el Code 3 de TM N19 no depende del layout.

**Punto 2 — grounding schedule (revisado contra el adjunto completo, 3-Jun).** TM N15 NOTE-03 pidió: PE point identifiers, sección de conductor por circuito (Cu bare, mm²), topología ring main, bonding equipotencial a acero estructural del contenedor, conexión a malla externa ADASA; per NCh Eléct. 4/2003 Section 10.0. El `Ground Cable Schedule sample.pdf` tiene **26 filas (NO truncado)** y es **sustancialmente completo**: tablero PE-LCP-01, contenedor, 2 bandejas, HP/CIP pump, calefactor, 2 dosificadoras, 2 luminarias, A/C, enchufe y 13 válvulas motorizadas; con PE IDs, secciones phase/PE/bonding (mmsq), Grounding Topology = Ring Main, Equipotential Bonding = Yes, fila 1 = "Main Grounding Connection ADASA Scope (~90 m)". **El driver OBS-01 (schedule ausente) queda materialmente resuelto.** Bonding a acero estructural YA mostrado en el plano: PE points = "M10x30L SS304 stud welded on container structure". Única brecha real de material: la columna Cable Specification dice "Cu/PVC" en todo, pero el **Material Take-Off del propio plano** lista Copper Earth Link, 25mmsq CU Tinned Flexible Braided y "standard copper bar" para tray-to-tray (nota 3) — pedir consistencia (cobre desnudo/trenzado/barra para electrodo y anillo vs Cu/PVC aislado para PE de equipos). La anotación CC_ADASA OBS-01 acepta el schedule "integrated on the drawing **or as a referenced annex**" → no exigir solo embebido. Decisión del usuario: NO abrir loop de aprobación separado de plantilla.

**Punto 3 — CCS description.** TM N17 OBS-01: el CCS embebido en pág. 2 del Grounding pertenecía al Cable Tray Layout (P22-DWG-09-007-004). BW Water dice que ya lo corrigió en Rev E. Cierre condicionado a legibilidad (ver punto 5 / TM N19 NOTE-01).

**Punto 4 — grounding method reference + NEC/IEC.** TM N17 NOTE-02: detalle típico referenciado desde el plano no estaba incluido; confirmar que vive en Typical Installation Details of Power Works (P22-DWG-09-007-005 Rev C). Además, TM N19 Section 2.7 NOTE-01 pide designar cuál de los 7 métodos de grounding aplica a cada carga (IEC 60364-5-54). **Hallazgo de la revisión de adjuntos (usuario aprobó incluir):** el plano Rev E es inconsistente — nota 8 pág. 2 cita NEC Table 250.122, pág. 3 cita IEC 60364-5-54. ADASA ya impuso IEC 60364-5-54 en TM N17 (Typical Power Works Rev C) → pedir reconciliación a IEC 60364-5-54 en todo el plano.

**Punto 5 — revision history + screenshots.** Sub-3: la frase genérica "Revised as per Comment" no satisface TM N19 OBS-02. La anotación CC_ADASA OBS-02 (literal) pide descripción de cambios **y referencia ECN** para **cada Rev de B a E** (Rev B 2-Mar, C 17-Apr, D 30-Apr, E 12-May) → el correo pide "Rev B through Rev E + ECN where applicable". Sub-4: pegar screenshots del TM en el CCS no está prohibido; el problema (TM N19 NOTE-01) es la ilegibilidad → emitir desde fuente electrónica.

**Punto 6 — plazo.** TM N19 fijó 14 días corridos para Rev F con reserva C-4300 (deadline original ≈ lunes 08-Jun-2026). Decisión del usuario: extensión corta acotada. Nueva fecha firme: **miércoles 17-Jun-2026** = +10 días hábiles desde la réplica (03-Jun, miércoles); evita el sábado 13-Jun. **Por instrucción del usuario, el correo NO nombra la reserva del Contrato C-4300**; se sustituyó por "there is no longer a basis to defer Rev F". La omisión es deliberada y no implica renuncia de derechos: ADASA conserva sus remedios contractuales aunque no los explicite en este correo de aclaración.

**Cadena de correo.** Reply-To al thread de Eduardo del 02-Jun (no es re-emisión del TM N19 ni instrumento nuevo). Mismo patrón que la réplica al Mitigation Plan del 01-Jun.

**ENVIADO 03-Jun-2026** a Eduardo Yamauchi + CC del thread (Billy Tan, Adzlan Bin Abd Rahim, Jeryl F. Regulacion, Stephane Gehant, David Chee Keat Swee, Sadeep Irugalbandara, Nick Huta) + ADASA (Víctor Gutiérrez), Reply-To al thread "25007 Taltal: Ground cable schedule clarification".

**Trazabilidad sincronizada:** estado ENVIADO en este `.md` ✓; README §9 (entrada 03-Jun) + tabla de seguimiento (#065) ✓; puntero en `REVISIONES/TRANSMITTALES/P22-TM-09-000-019-0/CONTRA PREGUNTA BW WATERS/` ✓; memoria de proyecto (`project_tm19_grounding_clarification_revF`) ✓. **Pendiente manual:** dejar el respaldo PDF/.msg del correo enviado en esta carpeta.
