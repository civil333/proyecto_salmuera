---
titulo: Las 62 observaciones de la ENTREGA 70, para revision de gravedad
codigo: E70-REVISION-OBS
fecha: 2026-08-05
estado: INTERNO - para decidir que se emite; nada de esto ha salido
second_brain: skip
---

# Las 62 observaciones de la ENTREGA 70

> Documento interno de decisión. Ninguna de estas observaciones se ha emitido. La columna **Decisión** esta vacia a proposito: es la que tienes que llenar.

## Lo primero: casi nada de esto reabre algo cerrado

La duda es legitima y hay que responderla con el dato antes de mirar una sola observacion. El historial del Piping Layout:

| Revisión | Paginas del PDF | Planos de taller incluidos |
|---|---|---|
| Rev A | 5 | 0 |
| Rev B (E32, quedo **Código 2**) | 5 | 0 |
| **Rev C (esta entrega)** | **22** | **11** |

**Las 17 páginas de planos de taller aparecen por primera vez en la Rev C.** Nunca se sometieron, nunca se revisaron y nunca se cerraron. Toda observacion que cae sobre ellos es de primer ciclo.

| Sobre que material caen | Observaciones | Estado previo |
|---|---|---|
| Planos de taller del Piping Layout | **38** | Material **nuevo**, nunca revisado |
| Modelo 3D | **15** | **Primera emisión**, item nuevo del registro |
| Datasheet DP Switch | **9** | Rev A quedo Código 1; lo que se revisa es el **sello de diafragma nuevo** |

Lo unico que quedaba abierto sobre el Piping Layout eran **las cuatro NOTE del TM N15**, y están tratadas una por una en la primera sección. El resto de la Rev B se acepto y no se reabre.

De las 62, el propio revisor marco **11 como pedido nuevo de ADASA** y no como incumplimiento: esas se redactan como extensión de alcance, nunca como falta del proveedor.

---

## Reparto por severidad

| Severidad | Cantidad | Que significa |
|---|---|---|
| 🔴 CRITICAL | 2 | Incumplimiento contractual o riesgo. Ambas caen sobre los planos de taller |
| 🟠 MAJOR | 20 | Incumplimiento con via de solucion |
| 🟡 MINOR | 18 | Documentación o clarificacion |
| ⚪ NOTE | 22 | Informativo o entregable externo |

---

## Piping Layout — las cuatro NOTE que el TM N15 dejo abiertas

**7 observaciones** — MAJOR 2 · MINOR 3 · NOTE 2

Rev B quedo **Código 2** con NOTE-06 a NOTE-09 abiertas para incorporar en Rev 0. **Esto es lo unico que estaba pendiente sobre este plano.** Todo lo demas de la Rev B se acepto.

### 🟠 MAJOR · OBS-01 — LCP integration and routing declared addressed by reference to a drawing that is not in this submittal

| | |
|---|---|
| **Donde** | Sheet 1 - PIPING LAYOUT - OVERALL (plan view, west end and CIP skid; ISO view); Consolidated Comment Sheet, page 22 of 22, Rev B item 4 |
| **Que dice** | Rev C answers this item with a single line on the Consolidated Comment Sheet, 'EIC details is shown in a separate drawing', and the drawing itself is unchanged on the point. Sheet 1 still shows the LCP as a free-standing two-door enclosure on its own plinth, clear of the container envelope at the west end, plus a second enclosure also labelled LCP on the CIP skid; neither carries an equipment tag, while every other item on the sheet does (TK-09-001, BH-09-002, FIL-09-001, BDS-09-001/002, TK-09-002, REL-09-001). No cable tray, no conduit run and no container wall penetration is drawn between either enclosure and... |
| **Fuente que invoca** | ADASA comment recorded on BW Water's own Consolidated Comment Sheet (page 22 of 22), Rev B item 4: 'Sheet 4 shows the LCP as a separate unit external to the module envelope. Cable routing, conduit penetrations and FAT scope (panel installed at FAT vs shipped separately) not documented. Confirm... |
| **Que pide a BW Water** | Identify the separate EIC drawing by document code and revision and add it to the Reference Drawing List of the Piping Layout; show the conduit routes and container wall penetrations serving both enclosures labelled LCP on Sheet 1; assign each enclosure its equipment tag; and state the FAT scope... |
| **Mi verificación** | La verificación adversarial corrigio dos errores de la redaccion original (no todos los equipos llevan TAG; las laminas 1-3 no tienen Reference Drawing List). |
| **Decisión** | |

### 🟠 MAJOR · OBS-03 — Tie-in elevations added only for the super duplex and drain lines; permeate and CIP supply/return still without elevation reference

| | |
|---|---|
| **Donde** | Sheet 2 - SECTION 1-1 FRONT VIEW, vertical dimension chains at both ends; Sheet 3 - SECTION 2-2 FRONT VIEW, left-hand chain; Consolidated Comment Sheet, page 22 of 22, Rev B item 1 |
| **Que dice** | Rev C does add elevation information that Rev B did not carry, and that progress is acknowledged: Sheet 2 now has a vertical chain at each end of the container fixing DA-SSD-DN80-09-006, DA-SSD-DN100-09-004 and DA-SSD-DN65-09-009 at the west face and DA-PVC-DN100-09-002, DA-PVC-DN100-09-001 and RD-PVC-DN15-09-001 at the east face against a 2,896 mm overall height, and Sheet 3 fixes two levels of the CIP header rack against a 3,499 mm overall height. The permeate and CIP supply and return tie-ins that ADASA named are not among them, no elevation datum or finished floor level is declared anywhere in the set (the... |
| **Fuente que invoca** | ADASA comment recorded on BW Water's own Consolidated Comment Sheet (page 22 of 22), Rev B item 1: 'Tie-in points (feed inlet, permeate, concentrate, CIP supply/return) are dimensioned in plan view; elevation references absent. Add a tie-in elevation summary table or section drawing prior to IFC... |
| **Que pide a BW Water** | Add a tie-in schedule to the Piping Layout listing, for every battery-limit connection, the line tag, nominal diameter, connection type and the elevation referred to a datum declared on the drawing, covering the permeate and CIP supply and return lines as well as the lines already dimensioned; and... |
| **Decisión** | |

### 🟡 MINOR · NOTE-02 — Consolidated Comment Sheet issued incomplete and dated ahead of the revision it reports on

| | |
|---|---|
| **Donde** | Consolidated Comment Sheet, page 22 of 22 of the PDF |
| **Que dice** | The re-revision does carry a Consolidated Comment Sheet and its content maps one to one onto the four items left open at Rev B, which is the right practice and is acknowledged. It is issued incomplete. The Submittal No. field and the SUB NO. column are blank for both rows, and the Status column is blank for every comment, so the sheet never declares which items BW Water considers closed and which remain open. It is dated 3/7/2026, ahead of the Rev C sheets themselves, which are dated 24 July 2026 on the title blocks and 27 July 2026 on the cover sheet; on either reading of the day/month format the sheet predates... |
| **Fuente que invoca** | The form's own Submittal No., SUB NO. and Status fields, provided on the Consolidated Comment Sheet and left blank on both rows, and the issue dates shown in the title blocks of Sheets 1 to 3 (24 July 2026) and on the cover sheet (27 July 2026). |
| **Que pide a BW Water** | Complete the Submittal No., SUB NO. and Status fields of the Consolidated Comment Sheet, declaring each comment as closed or open, and date the sheet with the revision it accompanies, when issuing Rev 0. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### 🟡 MINOR · NOTE-03 — Confirmations given on the comment sheet are not recorded on the drawing; the NOTES panel is blank on all three sheets

| | |
|---|---|
| **Donde** | Sheets 1, 2 and 3, NOTES panel in the right-hand column of each sheet |
| **Que dice** | Each of the three layout sheets carries a NOTES panel and all three are blank. The confirmations BW Water gives on the Consolidated Comment Sheet, namely the flanged joints at the antiscalant and CIP make-up connections, the door arrangement and the deferral of the EIC and tie-in detail to other drawings, live only on that sheet, which does not travel with the drawing once it is issued for construction. That is the mechanism by which items are closed on the comment sheet and remain invisible on the deliverable, and it is what turns OBS-01 and OBS-03 into carry-forwards. The drawing's own NOTES panel is the... |
| **Fuente que invoca** | The NOTES panel provided by BW Water on Sheets 1, 2 and 3 of the drawing, left blank, read against the confirmations recorded on the Consolidated Comment Sheet (page 22 of 22), Rev B items 3 and 4. |
| **Que pide a BW Water** | Transfer to the NOTES panel of the relevant sheet the confirmations given on the comment sheet, namely the flanged terminations at the antiscalant and CIP make-up connections, the lateral access door type, and the cross-references to the EIC and Tie-In Point drawings by document code, at IFC Rev 0. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### 🟡 MINOR · OBS-02 — Lateral access is drawn but not identified as the sliding door the specification requires

| | |
|---|---|
| **Donde** | Sheet 1 - PIPING LAYOUT - OVERALL, plan view south wall between grids 3 and 5, and ISO view; Consolidated Comment Sheet, page 22 of 22, Rev B item 2 |
| **Que dice** | The equipment access door is now fully represented and that half of the item closes against the drawing: Sheet 1 shows it at the west end of the container with both leaves, the two 110-degree opening arcs, outward swing and the 2,438 mm and 968 mm dimensions, which matches what the specification asks for. The lateral opening is a different matter. It is drawn on the south wall with a leaf, a head member and an access stair, and it is labelled only 'LATERAL ACCESS'. The term 'sliding door' does not appear anywhere in the 22-sheet set, no track, guide or slide direction is annotated in either the plan or the... |
| **Fuente que invoca** | The Technical Specification (P22-ET-09-000-001-0), Section 5.1.10 - Container: 'Adicionalmente, el contenedor debera garantizar el acceso lateral mediante una puerta corrediza' (the container shall provide lateral access by means of a sliding door), which the same Section also pairs with the... |
| **Que pide a BW Water** | Label the lateral access on Sheet 1 as a sliding door, show the track and the slide direction in both the plan and the isometric view, and dimension the clear opening, at IFC Rev 0. |
| **Decisión** | |

### ⚪ NOTE · NOTE-01 — Antiscalant and CIP battery-limit terminations resolved on the geometry; flange class not annotated

| | |
|---|---|
| **Donde** | Sheet 3 - SECTION 2-2 ISO VIEW, west end of the CIP header rack; Consolidated Comment Sheet, page 22 of 22, Rev B item 3 |
| **Que dice** | This item closes against the drawing, not only against the reply. Sheet 3 shows the four CIP and antiscalant header lines terminating in flanged ends at the module limit, with the leaders from CP-PVC-DN100-09-024, CP-PVC-DN100-09-021, CP-PVC-DN80-09-019 and AS-PVC-DN15-09-035 landing on the flange faces, so site connection without on-site PVC welding is demonstrated geometrically. What the drawing does not state is the flange class: no rating is annotated against these PVC terminations on Sheets 1 to 3, and the ANSI 150# socket RF PVC callouts that do appear in the bundled fabrication sheets belong to other... |
| **Fuente que invoca** | ADASA comment recorded on BW Water's Consolidated Comment Sheet (page 22 of 22), Rev B item 3, asking that AS-PVC-DN15-09-035 and CP-PVC-DN80-09-019 be ANSI-flanged to allow site connection without on-site PVC welding. |
| **Que pide a BW Water** | Annotate the flange class against the CIP and antiscalant battery-limit terminations shown on Sheet 3 at IFC Rev 0, consistent with the approved Line List P22-LI-09-009-003. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · NOTE-04 — Withdrawn footprint restriction still carried as a live client comment on the comment sheet

| | |
|---|---|
| **Donde** | Consolidated Comment Sheet, page 22 of 22, row 1 (Rev A) |
| **Que dice** | Row 1 of the comment sheet still carries the 3,500 mm maximum footprint restriction as a live client comment. ADASA withdrew that restriction formally and it is not reopened here; the point is only the record. Left as it stands, a requirement ADASA no longer holds travels into the IFC package as an outstanding client comment, which is the kind of stale entry that resurfaces during fabrication and inspection. |
| **Fuente que invoca** | ADASA's formal withdrawal of the maximum footprint restriction originally raised as TM N5 OBS-01, superseded by P22-DWG-06-006-101. |
| **Que pide a BW Water** | Mark row 1 of the Consolidated Comment Sheet as withdrawn by ADASA and superseded by P22-DWG-06-006-101 when issuing Rev 0; no change to the drawing is required on this account. |
| **Decisión** | |

---

## Piping Layout — contenedor, accesos y estructura del paquete

**15 observaciones** — MAJOR 5 · MINOR 6 · NOTE 4

Mezcla observaciones sobre las laminas 1 a 4, que son el documento que la Rev B dejo aceptado, con observaciones sobre las 18 paginas que aparecen por primera vez en la Rev C.

### 🟠 MAJOR · OBS-01 — Duplicate equipment TAG FIL-09-001 assigned to two different filters

| | |
|---|---|
| **Donde** | Sheet 1 - Piping Layout Overall (PDF page 2), plan view: RO Cartridge Filter inside the container and CIP Cartridge Filter in the external CIP area |
| **Que dice** | Sheet 1 labels two physically distinct items with the same TAG: 'RO CARTRIDGE FILTER (FIL-09-001)' inside the container and 'CIP CARTRIDGE FILTER (FIL-09-001)' in the external CIP area. Both labels were read on the rendered plan view at 600 dpi, so this is not an extraction artefact. A single TAG shared by two vessels breaks identification against the P&ID, the Instrument List and the control system, and the error has already propagated into documents released for fabrication. |
| **Fuente que invoca** | General Codification Instruction (P00-IT-00-000-101); cross-reference discipline between P&ID, Equipment List and layout drawings required by the Technical Specification (P22-ET-09-000-001-0), Section 5 - Caracteristicas de la Planta Modular. |
| **Que pide a BW Water** | Assign a unique TAG to each cartridge filter, aligned with the approved P&ID and Equipment List, and correct the label on Sheet 1 before re-issue. Confirm which of the two items keeps FIL-09-001 and reissue any downstream document that inherited the duplicated TAG. |
| **Mi verificación** | ⚠️ **NO CONFIRMADO.** El TAG aparece dos veces en la lamina 2, pero no logre ver que rotule dos filtros distintos. Emitir como aclaracion, no como defecto. |
| **Decisión** | |

### 🟠 MAJOR · OBS-02 — Thirteen uncoded shop fabrication sheets bundled inside a document declared as four pages

| | |
|---|---|
| **Donde** | PDF pages 5 to 17 (drawings 25007-ME-PI-0901-0006 to -0014); cover sheet PDF page 1 declares 'Page 1 of 4' |
| **Que dice** | The file submitted under ADASA code P22-DWG-09-005-004 Rev C contains 17 pages: the ADASA cover sheet plus three A1 sheets that make up the Piping Layout (consistent with the cover statement 'Page 1 of 4'), and thirteen further sheets that belong to a different document set. Those thirteen sheets carry a second title block (BW Water Sdn. Bhd., Penang), their own numbering 25007-ME-PI-0901-0006 to -0014, their own revision index (0 on nine sheets, 1 on four), spool titles instead of a drawing title, and a red 'FOR CONSTRUCTION / SHOP FABRICATION' status stamp. None carries an ADASA code, none appears in the cover... |
| **Fuente que invoca** | General Codification Instruction (P00-IT-00-000-101); Special Administrative Conditions (BAE 12803), Clause 37 on document review; the cover sheet of the drawing itself, which declares the document as four pages. |
| **Que pide a BW Water** | Either remove the shop fabrication set from P22-DWG-09-005-004 and submit it as a separate deliverable with its own ADASA code and revision index, or extend the cover sheet and the Submittal Form to declare it explicitly. In both cases state the review status expected from ADASA for those sheets. |
| **Mi verificación** | **Cifras corregidas.** Son 22 paginas, 17 laminas de taller y 11 planos (-0006 a -0016), no 17/13/-0014. El agente leyo la extraccion a medio terminar. |
| **Decisión** | |

### 🟠 MAJOR · OBS-03 — Piping spools released FOR CONSTRUCTION and internally signed before ADASA review of the parent layout

| | |
|---|---|
| **Donde** | PDF pages 5 to 17, status stamp 'FOR CONSTRUCTION / SHOP FABRICATION' with prepared/checked/approved signatures dated 23-07-2026, 27-07-2026 and 29-07-2026 |
| **Que dice** | Unless ADASA has already approved the corresponding fabrication drawings and the Detailed Inspection and Test Plan under a separate submittal, the release status of these sheets is difficult to reconcile with the review sequence. The thirteen spool sheets are stamped FOR CONSTRUCTION and carry internal preparation, checking and approval signatures dated between 23 and 29 July 2026, that is, before the parent Piping Layout Rev C was transmitted to ADASA on 05 August 2026 and while the four notes raised on Rev B remain to be incorporated at Rev 0. The spools are dimensioned from the same model as the layout, so... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 7 - Ingenieria de Detalle: the Detailed Inspection and Test Plan shall cross-reference the Supplier's own approved fabrication drawings, and ADASA's written approval of the Detailed Inspection and Test Plan is an indispensable requirement to... |
| **Que pide a BW Water** | State the approval basis under which these spools were released for construction, identifying the approved fabrication drawings and the approved Detailed Inspection and Test Plan they rely on. Where no such approval exists, confirm in writing that the spools are being fabricated at BW Water's own... |
| **Decisión** | |

### 🟠 MAJOR · OBS-04 — Container envelope height of 2896 mm against the 2.8 m maximum of the Technical Specification

| | |
|---|---|
| **Donde** | Sheet 2 - Section 1-1 Front View (PDF page 3), overall vertical dimension 2896 [9'-6"] at the left of the elevation; chain 338+313+435+498+740+401+171 = 2896 |
| **Que dice** | Unless the module envelope height has been re-based on the ADASA civil drawing P22-DWG-06-006-101 or otherwise accepted in an approved document, the elevation exceeds the specified maximum. Section 1-1 dimensions the overall container height as 2896 mm, the standard external height of a 40 ft high-cube unit, against a specified maximum of 2.8 m. Length and width comply: 12192 mm [40'] against 13 m and 2438 mm [8'] against 2.5 m, both dimensioned on Sheet 1. This observation concerns the height only and does not reopen the module footprint, which ADASA withdrew. |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.1.10 - Contenedor: 'Las dimensiones maximas del contenedor seran de 13 metros de largo por 2,5 metros de ancho, y 2.8 metros de altura'. |
| **Que pide a BW Water** | Confirm what the 2896 mm dimension envelopes (container structure only, or container plus base beams) and reconcile the module height with the specified 2.8 m maximum, or provide the written ADASA acceptance on which the high-cube envelope relies. Reflect the agreed value on Sheet 2 at re-issue. |
| **Mi verificación** | **Verificado.** ET linea 704: máximo 13 m x 2,5 m x **2,8 m de altura**. La lamina 2 acota 2896 mm. |
| **Decisión** | |

### 🟠 MAJOR · OBS-05 — Two untagged enclosures labelled LCP; cabinet integration and routing still unresolved (NOTE-07)

| | |
|---|---|
| **Donde** | Sheet 1 (PDF page 2), plan view: one enclosure labelled 'LCP' outside the left end of the container and a second enclosure labelled 'LCP' next to the antiscalant dosing tank in the external CIP area; both also visible in the isometric view |
| **Que dice** | Rev C now shows the panel positions, which Rev B did not, but the representation raises a new ambiguity instead of closing NOTE-07. Two separate enclosures appear on the same plan, both labelled 'LCP' and neither carrying an equipment TAG: one on an external platform at the left end of the container, one adjacent to the antiscalant dosing tank at the opposite end of the module. The approved Local Control Panel datasheet defines a single panel, so either a second panel exists and is undeclared, or the label is duplicated. No cable routing or tray is shown between the panels and the equipment they serve. |
| **Fuente que invoca** | NOTE-07 of Transmittal N15 on P22-DWG-09-005-004 Rev B (cabinet integration and Local Control Panel routing to be clarified); Technical Specification (P22-ET-09-000-001-0), Section 5.4 - Tableros de Fuerza y Control. |
| **Que pide a BW Water** | State whether the module carries one or two local control panels, TAG each enclosure on the drawing consistently with the approved Local Control Panel datasheet and the Single Line Diagram, and show the routing between each panel and the equipment it serves, or reference the drawing where that... |
| **Decisión** | |

### 🟡 MINOR · OBS-06 — Module limit flanges of the CIP and antiscalant lines still not declared (NOTE-08)

| | |
|---|---|
| **Donde** | Sheet 1 (PDF page 2), right-hand terminations CP-PVC-DN80-09-019 (make-up CIP), CP-PVC-DN100-09-021 (CIP return), CP-PVC-DN150-09-022 (to CIP pump), CP-PVC-DN100-09-025 (CIP recirculation) and AS-PVC-DN15-09-035 (antiscalant injection); Sheet 3 - Section 2-2... |
| **Que dice** | The CIP and antiscalant lines terminate at an unlabelled dashed boundary and carry only their line tag, a service description and an offset relative to the CIP tank centreline. No flange rating, facing, size or orientation is declared at any of those terminations, and the boundary line itself is not identified as the limit of supply. The note raised on Rev B therefore remains open on Rev C. |
| **Fuente que invoca** | NOTE-08 of Transmittal N15 on P22-DWG-09-005-004 Rev B (module limit flanges of the antiscalant and CIP lines to be confirmed); Technical Specification (P22-ET-09-000-001-0), Section 5.6 - Limites de Suministro, which sets ANSI B16.5 Class 150 for the tie-in flanges. |
| **Que pide a BW Water** | Declare, for each CIP and antiscalant line that reaches the limit of supply, the flange size, rating and facing, and identify the limit of supply line on the drawing. State which of those terminations correspond to the tie-ins defined in the Technical Specification and which are internal to the... |
| **Decisión** | |

### 🟡 MINOR · OBS-07 — Tie-ins not identified against the Technical Specification and elevations referred to the module only (NOTE-09)

| | |
|---|---|
| **Donde** | Sheet 2 - Section 1-1 Front View (PDF page 3), elevation chains at both ends of the container (338/313/435/498/740/401/171 on the left; 338/361/439/976/380/230/282/171 on the right) |
| **Que dice** | Rev C responds in part to NOTE-09: Section 1-1 now dimensions the elevation of every line that crosses the container envelope, which Rev B did not show. Two gaps remain for ADASA to design its connecting infrastructure. First, the elevations are chained from the top of the container downwards, with no reference to a construction datum such as finished floor or foundation level, so they cannot be transferred to the site. Second, none of the three sheets identifies which connections are the five tie-ins defined in the Technical Specification: the strings 'tie-in' and 'limit of supply' return zero hits on the text... |
| **Fuente que invoca** | NOTE-09 of Transmittal N15 on P22-DWG-09-005-004 Rev B (elevation view of the tie-in missing); Technical Specification (P22-ET-09-000-001-0), Section 5.6 - Limites de Suministro, which defines tie-ins 1 to 5 and requires flanges with gaskets, studs and nuts for tie-ins 1, 2 and 3. |
| **Que pide a BW Water** | ADASA extends NOTE-09: label each module connection with the tie-in number defined in the Technical Specification, and refer the elevation chains of Section 1-1 to a declared datum (finished floor or top of the concrete base), stating the offset of each tie-in from the module face. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### 🟡 MINOR · OBS-08 — ADASA cover sheet and drawing title blocks disagree on revision dates and on authorship

| | |
|---|---|
| **Donde** | Cover sheet (PDF page 1) against the title blocks of Sheets 1, 2 and 3 (PDF pages 2, 3 and 4) |
| **Que dice** | The cover sheet records Rev C on 27-07-2026, Rev B on 02-04-2026 and Rev A on 03-03-2026, prepared by CAD, reviewed by AIA, checked by SI and approved by LPL. The three drawing sheets record Rev C on JULY.24.26, Rev B on APR.02.26 and Rev A on FEB.02.26, prepared by AHR, checked by AIA and approved by NOP. Rev C differs by three days and Rev A by a month; the authorship record differs entirely. The sheet revision table also describes Rev A and Rev B as 'issued for internal review' and 'revised for internal review', although both were formally submitted to ADASA and returned with Code 3 and Code 2 respectively,... |
| **Fuente que invoca** | Special Administrative Conditions (BAE 12803), Clause 37 on document control and review; General Codification Instruction (P00-IT-00-000-101). |
| **Que pide a BW Water** | Align the revision dates and the preparer, checker and approver names between the ADASA cover sheet and the three drawing sheets, describe Rev A and Rev B by the status under which they were actually issued to ADASA, and complete the signature row before re-issue. |
| **Decisión** | |

### 🟡 MINOR · OBS-09 — Shop sheets: revision box contradicts the revision table, mixed indices, and declared size does not match the page

| | |
|---|---|
| **Donde** | PDF pages 5 to 17; verified on page 9 (25007-ME-PI-0901-0009, REV box 0 against revision row '1 | 27/7/2026 | ISSUED FOR APPROVAL | SKO | AIA'); pages 5, 6 rendered at A2 and page 11 at A3 while their title blocks declare SIZE A1 |
| **Que dice** | Three defects run through the appended set. The REV box reads 0 on the sheets numbered -0008, -0009, -0011, -0012 and -0013 while the revision table on the same sheet records a row 1 issued for approval dated 27/07/2026, so the two revision fields of one title block contradict each other. Across the set the index is mixed, 0 on nine sheets and 1 on four (-0006, -0007, -0010, -0014), with no description of what distinguishes them. Three pages are issued at A2 or A3 while their title block declares A1, so the view scales printed on those sheets (1:10, 1:12) are not reproducible from the file as issued. |
| **Fuente que invoca** | Special Administrative Conditions (BAE 12803), Clause 37 on document control; General Codification Instruction (P00-IT-00-000-101). |
| **Que pide a BW Water** | Reconcile the REV box with the revision table on every shop sheet, state a single consistent revision index for the set with its revision description, and issue all sheets at the size declared in their title block. |
| **Decisión** | |

### 🟡 MINOR · OBS-10 — Weight fields left as placeholders on every shop sheet

| | |
|---|---|
| **Donde** | PDF pages 5 to 17, General Notes item 3 'WEIGHTS: DRY - XXXX Kg / OPERATING - XXXX Kg' (16 occurrences across the 13 sheets) |
| **Que dice** | Every shop sheet carries its own weight field unfilled, printed as 'DRY - XXXX Kg' and 'OPERATING - XXXX Kg', on documents that are already stamped FOR CONSTRUCTION and signed. The same sheets leave 'ELECTRICAL LIST: 1. TBA'. Operating weight is the quantity on which the seismic design of the supports and anchorages is based, so a released fabrication drawing that does not carry it is difficult to use as a verification record. |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 4.4 - Condiciones Sismicas, which states that seismic forces are applied at the centre of gravity and that the weight to be considered is the operating weight; and Section 7 - Ingenieria de Detalle, which requires the module lifting drawing to... |
| **Que pide a BW Water** | Complete the dry and operating weight fields on each shop sheet, or remove the field if the weights are reported elsewhere and reference that document. Resolve the 'TBA' entry of the electrical list. |
| **Decisión** | |

### 🟡 MINOR · OBS-11 — Door openings not identified against the four access requirements, and no leaf dimensions given

| | |
|---|---|
| **Donde** | Sheet 1 (PDF page 2), plan view: 'EQUIPMENT ACCESS DOOR' with two 110 degree swing arcs and a 968 [3'-2"] leaf dimension on the end wall; 'LATERAL ACCESS' and 'EMERGENCY DOOR' on the long wall |
| **Que dice** | Three openings are shown where the specification defines four access functions: pedestrian access door, equipment access door, emergency door, and in addition lateral access by sliding door. The drawing does not state which opening serves which function, and no clear width or height is given for the two personnel openings; the only leaf dimension on the sheet is the 968 mm of the equipment door. The 888 [2'-11"] dimension near the emergency door is a transverse dimension inside the container, not a door width. The emergency door is shown without a swing arc, so its opening direction is not declared. |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.1.10 - Contenedor: pedestrian access door, equipment access door and emergency door; personnel doors of 900 mm wide by 2200 mm high; equipment doors with a 110 degree opening angle, always opening outwards; and lateral access guaranteed by a... |
| **Que pide a BW Water** | ADASA extends NOTE-06: add a door schedule to Sheet 1 identifying each opening against the four access requirements and stating its clear width and height, confirming 900 by 2200 mm for the personnel openings, and show the opening direction of the emergency door. The schedule may be placed on the... |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · NOTE-01 — NOTE-06 closed in part: equipment access door and lateral sliding door are now represented

| | |
|---|---|
| **Donde** | Sheet 1 (PDF page 2), plan view left end and isometric view of the long wall |
| **Que dice** | Rev C represents the two openings that Rev B omitted. The equipment access door appears on the end wall as a double leaf with two 110 degree swing arcs opening outwards, consistent with the specification. The lateral access is drawn in the isometric view as a sliding leaf running in front of the wall panel, with a head track and a flush recessed pull handle, which is the sliding arrangement required by the specification. The representation is accepted; only the identification and dimensioning of the openings remain, covered by OBS-11. |
| **Fuente que invoca** | NOTE-06 of Transmittal N15 on P22-DWG-09-005-004 Rev B; Technical Specification (P22-ET-09-000-001-0), Section 5.1.10 - Contenedor. |
| **Que pide a BW Water** | No action on this point beyond OBS-11. ADASA records NOTE-06 as addressed in respect of the representation of the equipment access door and the lateral sliding door. |
| **Decisión** | |

### ⚪ NOTE · NOTE-02 — RO cartridge filter shown vertical in Rev C; align the Equipment Layout to this arrangement

| | |
|---|---|
| **Donde** | Sheet 1 (PDF page 2), plan view: circular body with bolt circle at the filter station; Sheet 2 - Section 1-1 (PDF page 3), vertical cylindrical body with domed top head at the same station |
| **Que dice** | The Piping Layout Rev C shows the RO cartridge filter in a vertical arrangement: circular with a bolted head in plan and a vertical domed body in Section 1-1. The filter orientation is the item that keeps the Equipment Layout Rev C in Code 3, so this drawing sets the arrangement the Equipment Layout must be aligned to. No modification to the Piping Layout arises from this point. |
| **Fuente que invoca** | Open Code 3 item on P22-DWG-09-005-004 companion drawing Equipment Layout Rev C (RO cartridge filter orientation), tracked in the pending observations section of the transmittal. |
| **Que pide a BW Water** | Align the Equipment Layout to the vertical arrangement shown on this drawing when it is re-issued, and confirm that both drawings and the filter datasheet agree on the orientation. Tracked as a cross-document deliverable. |
| **Decisión** | |

### ⚪ NOTE · NOTE-03 — Notes panel left empty on the three ADASA sheets

| | |
|---|---|
| **Donde** | Sheets 1, 2 and 3 (PDF pages 2, 3 and 4), 'NOTES' panel on the upper right of each sheet |
| **Que dice** | The three sheets reserve a large NOTES panel and leave it blank. There is no statement of units, no general note, no reference document list and no legend, although dimensions are given in millimetres with imperial values in brackets and the sheets are the interface reference for ADASA. The appended shop sheets, by contrast, carry a full set of general notes with units, tolerances, test requirements and a reference drawing list. |
| **Fuente que invoca** | Drafting practice consistent with the Supplier's own shop sheets; General Codification Instruction (P00-IT-00-000-101). |
| **Que pide a BW Water** | Populate the NOTES panel of the three sheets with, as a minimum, the units statement, the reference drawing and design document list, and the legend for the boundary and section symbols used. |
| **Decisión** | |

### ⚪ NOTE · NOTE-04 — Anchorage and seismic interface not covered by this drawing, including the external CIP and dosing area

| | |
|---|---|
| **Donde** | Sheets 1, 2 and 3; Sheet 3 - Section 2-2 (PDF page 4) dimensions the external CIP and dosing area at 3499 [11'-6"] high, outside the container envelope |
| **Que dice** | All three sheets are dimensioned relative to the module envelope alone. No anchorage, hold-down detail, base plate or foundation load is shown for the container or for the external CIP, dosing and tank area, which stands 3499 mm high outside the container on its own base. ADASA does not expect that information on a piping layout, so this does not change the document; the point is recorded to keep the interface visible, because the concrete bases are built by ADASA and the seismic verification is a separate deliverable requiring ADASA approval. |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 4.4 - Condiciones Sismicas (NCh 2369, Zone 3, forces at the centre of gravity on operating weight, to be demonstrated by a specific calculation report approved by ADASA); and Section 7 - Ingenieria de Detalle, which requires a civil... |
| **Que pide a BW Water** | Confirm that the anchorage of the container and of the external CIP and dosing area, with the corresponding loads and bolt layout for the ADASA concrete bases, is covered by the seismic calculation report and the civil requirements drawing, and state the codes and issue dates of both. Tracked as a... |
| **Decisión** | |

---

## Piping Layout — tuberias, materiales y clases de presión

**17 observaciones** — CRITICAL 2 · MAJOR 6 · MINOR 6 · NOTE 3

Casi todas caen sobre los **planos de taller nuevos**. Aquí están los dos CRITICAL.

### 🔴 CRITICAL · OBS-01 — Acoples roscados austeniticos ANSI 150# en las cuatro lineas super duplex de mayor presión

| | |
|---|---|
| **Donde** | Lamina 11 (BOM item 4, spool DA-SSD-DN100-09-003, 25007-ME-PI-0901-0010); lamina 12 (item 5, DA-SSD-DN100-09-004, ...-0011); lamina 18 (item 5, DA-SSD-DN80-09-005, ...-0015); lamina 20 (item 5, DA-SSD-DN80-09-006, ...-0016). Total 6 piezas. |
| **Que dice** | Las tomas de instrumento de 1/2" (PI-09-001, PIT-09-002, PIT-09-003, PIT-09-004, PIT-09-005) se resuelven con un HALF COUPLING ANSI 150# SCRD en A182 Gr. F316L SCH10S PLxNPT (lamina 11, qty 2) y en A182 Gr. F304 PExFPT (laminas 12, 18 y 20). Verificado por lectura de la lamina, no solo de la capa de texto: en la lamina 11 el globo 4 apunta a las dos derivaciones bajo PI-09-001/PIT-09-002 y en la lamina 20 el globo 5 apunta a la derivacion de PIT-09-005. Son tres desviaciones simultaneas frente a la ET: (a) material austenitico -PREN del orden de 19 en F304 y 25 en F316L- en salmuera de 45.000-55.000 ppm Cl- y... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión: "Para las canerias de alta presion (hasta 120 bar) se utilizara acero inoxidable super duplex"; tabla de items 1/2"-4": "ACERO INOXIDABLE SUPER DUPLEX, SIN COSTURA, ASTM A790 UNS S32750, PREN>40, ASME B36.19M / SCH 80S / END BE" y... |
| **Que pide a BW Water** | Replace the six ANSI 150# threaded half couplings (A182 Gr. F304 and F316L) with super duplex branch fittings in ASTM A182 F53 UNS S32750, PREN>40, per MSS SP 97, welded, rated for the Class 900 line class, as already used elsewhere on the same sheets. Confirm in writing that no austenitic,... |
| **Mi verificación** | **Verificado.** Aparece en 7 laminas (11, 12, 14, 16, 17, 18, 20), no en 4. Presiones de la Line List Rev 0 confirmadas una a una. |
| **Decisión** | |

### 🔴 CRITICAL · OBS-02 — Quiebre de clase no declarado: tramos PVC y bridas ANSI 150# dentro de lineas tageadas 80-90 barG

| | |
|---|---|
| **Donde** | Lamina 5 (CP-SSD-DN100-09-014, BOM item 3); lamina 6 (CP-SSD-DN65-09-045, items 1, 2 y 7); lamina 7 (CP-SSD-DN80-09-015, item 4); lamina 9 (CP-SSD-DN80-09-044, items 1, 6 y 7). |
| **Que dice** | Los cuatro spools de alimentacion y retorno CIP colocan el quiebre entre el sistema super duplex de alta presión y el sistema PVC de baja presión en una union bridada ANSI 150# adyacente a una unica valvula mariposa motorizada, sin simbolo de spec break ni corte de número de linea. En las laminas 6 y 9 el efecto es directo: el spool titulado CP-SSD-DN65-09-045 incorpora 1.089 mm de caneria PVC SCH 80 de 2 1/2" y el titulado CP-SSD-DN80-09-044 incorpora 1.353 mm de PVC SCH 80 de 3" (verificado sobre la lamina 9, donde el propio isometrico dibuja el simbolo de cambio de material SS20/PVC y la flecha TO:... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión (bridas 1/2"-4" CLASE 900) y Sección 5.2.1 Canerias de baja presión (PVC ASTM D1784/D1785, bridas clase 150); tabla de valvulas de la Sección 5.2.2, item SEGURIDAD 1"-2", cuerpo y obturador en superduplex, clase 900. Line List... |
| **Que pide a BW Water** | On sheets 5, 6, 7 and 9, show the specification break explicitly and split the line numbers at that joint, so that the PVC segments carry their own line number, piping class, design pressure and hydrotest pressure; issue the corresponding addition to the Line List. State on the drawing how the PVC... |
| **Mi verificación** | **Verificado.** Las lineas PVC del CIP están rateadas a 5 barG de diseno y 7,5 de prueba; las SSD que las alimentan, a 80-90 y 120-135. |
| **Decisión** | |

### 🟠 MAJOR · OBS-03 — VM-09-151, mariposa DN100 clase 900 en la descarga de la bomba HP, indicada de accionamiento manual

| | |
|---|---|
| **Donde** | Lamina 11, spool DA-SSD-DN100-09-003 (25007-ME-PI-0901-0010), BOM item 18 y PLAN VIEW. |
| **Que dice** | El spool que va FROM OUTLET RO HP PUMP (BH-09-001) a TO INLET FEED TURBOCHARGER (SIP-09-001) muestra VM-09-151 como BUTTERFLY VALVE, MANUAL ACTUATED, F53+STL, LUG, 900LB de 4", dibujada con palanca en la vista en planta, aguas arriba de la valvula de retencion VR-09-001. Se trata de una valvula sobre la linea principal de proceso de mayor presión del modulo (51 barG de operacion), donde el criterio de la ET es funcional y no dimensional. Las restantes mariposas clase 900 del paquete si van motorizadas (VE-09-009, VE-09-010, VE-09-012, VE-09-013, VE-09-007), por lo que la discrepancia es puntual. El BOM tampoco... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.3 Actuadores: "Todas las valvulas de proceso relevantes, tanto en sistemas de alta como baja presión, deberan contar con actuacion eléctrica y ser completamente integrables al sistema de control del modulo (PLC) ... Asimismo, las valvulas manuales consideradas... |
| **Que pide a BW Water** | Confirm the actuation of VM-09-151 against the Valve List and the P&ID. Either fit an electric actuator integrated into the module PLC, or, if the valve is retained as a manual isolation, add open and closed limit switches with their corresponding I/O points and reflect them in the Valve List, the... |
| **Decisión** | |

### 🟠 MAJOR · OBS-04 — Fittings PVC roscados ASTM D2464 donde la ET exige fittings para soldar ASTM D2467

| | |
|---|---|
| **Donde** | Lamina 6 (BOM item 5, 2 unidades, spool CP-SSD-DN65-09-045) y lamina 9 (BOM item 5, 2 unidades, spool CP-SSD-DN80-09-044; globos 5 sobre los dos codos del montante PVC). |
| **Que dice** | Los tramos PVC de los spools CIP incorporan 45 DEG ELBOW THREADED, PVC, SCH80, ASTM D1784 ASTM D-2464. La ET especifica fittings PVC para soldar según ASTM D2467, que es precisamente lo que el mismo BOM usa en el codo de 90 grados (item 4, ASTM D-2467). Los fittings roscados D2464 llevan una reduccion sustancial de la presión admisible respecto de los encolados D2467, a la que se suma el factor de corrección por la temperatura de diseno de 45 degC declarada en la Line List, y el BOM no declara la presión resultante. Salvo que BW Water sustente que el fitting roscado cumple la presión de diseno y de prueba de la... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.1 Canerias de baja presión: "FITTINGS 40 mm 100 mm POLYVINYL CHLORIDE (PVC) SEGUN ASTM D1784. PARA SOLDAR DIMENSIONES SEGUN ASTM D2467. SCH 80". Line List P22-LI-09-009-003 Rev 0: temperatura de diseno 45 degC en todas las lineas PVC. |
| **Que pide a BW Water** | Replace the four ASTM D2464 threaded PVC elbows on sheets 6 and 9 with solvent-cemented socket fittings to ASTM D2467, Schedule 80, as required by the Technical Specification (P22-ET-09-000-001-0), Section 5.2.1 - Low Pressure Piping, or submit the pressure rating of the threaded fittings at the 45... |
| **Decisión** | |

### 🟠 MAJOR · OBS-05 — Valvulas y accesorios retenedores de presión listados sin material ni clase

| | |
|---|---|
| **Donde** | Lamina 11 (items 16 BALL VALVE 900LB qty 5, 17 SWING CHECK VALVE WAFER ANSI 900# RF / VR-09-001); lamina 18 (items 20 BALL VALVE qty 4, 21 NEEDLE VALVE, 22 PRESSURE REDUCING VALVE / VRP-09-001, 10 TUBE FITTING); laminas 12 y 20 (BALL VALVE 900LB). |
| **Que dice** | Varias piezas retenedoras de presión del sistema super duplex se describen en el BOM solo por tipo y clase, sin material: la retencion de 4" de la descarga de la bomba HP, las valvulas de bola de 1/2" de las tomas de instrumento, la valvula de aguja, la valvula reductora de presión VRP-09-001 y el tube fitting. En laminas timbradas FOR CONSTRUCTION esa omisión permite que el fabricante adquiera cuerpos austeniticos o de fundicion en un servicio de salmuera concentrada. La ET si define el material de la valvula de bola de alta presión, de modo que al menos ese item es una omisión directa respecto del documento... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión, tabla de valvulas: "BOLA 1/2" 4" ACERO INOXIDABLE SUPER DUPLEX, COMPLETAMENTE FABRICADA EN ASTM A182 Gr. F53 UNS S32750 (PREN>40), PASO TOTAL. DISENO DE 3 CUERPOS. CLASE 900, Para Soldar"; encabezado de la misma sección: "Para las... |
| **Que pide a BW Water** | State the body, trim and seat materials and the pressure class of every pressure-retaining item on the bills of materials, including the swing check valve VR-09-001, the 1/2" ball valves, the needle valve, the pressure reducing valve VRP-09-001 and the tube fitting. Wetted parts in the super duplex... |
| **Decisión** | |

### 🟠 MAJOR · OBS-06 — Correlativos de linea duplicados y TAG que no existen en la Line List aprobada

| | |
|---|---|
| **Donde** | Lamina 3 (Sheet 2): SECTION 1-1 FRONT VIEW y SECTION 1-1 ISO VIEW; también laminas 2 y 4. |
| **Que dice** | Sobre la misma lamina 3 conviven dos designaciones para el correlativo 09-019: la vista frontal rotula PE-PVC-DN80-09-019 y la vista isometrica rotula CP-PVC-DN80-09-019 (MAKE-UP CIP); el mismo TAG CP-PVC-DN80-09-019 se repite en las laminas 2 y 4. La Line List Rev 0 aprobada solo contiene PE-PVC-DN80-09-019, MAKE-UP FOR CIP, servicio PERMEATE WATER. En la misma lamina 3 aparece además RD-PVC-DN15-09-001, que no existe en la Line List aprobada -no hay ninguna linea con prefijo de servicio RD entre los 34 TAG del documento- y que reutiliza el correlativo 09-001 ya asignado a DA-PVC-DN100-09-002... perdon, a... |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0 aprobada (entrega E67), 34 TAG unicos y cero colisiones de correlativo: PE-PVC-DN80-09-019 MAKE-UP FOR CIP y DA-PVC-DN100-09-001 SWRO BRINE FEED; no existe RD-PVC-DN15-09-001 ni CP-PVC-DN80-09-019. |
| **Que pide a BW Water** | Align the layout to the approved Line List: designate the CIP make-up line as PE-PVC-DN80-09-019 on every view and sheet, and delete the CP-PVC-DN80-09-019 designation. Assign RD-PVC-DN15-09-001 a unique correlative that does not clash with DA-PVC-DN100-09-001 and submit the corresponding Line List... |
| **Decisión** | |

### 🟠 MAJOR · OBS-07 — Presión de prueba remitida a una especificacion interna de BW Water no sometida a aprobación

| | |
|---|---|
| **Donde** | Nota general 4 (TEST REQUIREMENT) de todas las laminas de spool: 5, 6, 7, 9, 11, 12, 18, 20 y siguientes. |
| **Que dice** | Cada lamina de fabricación fija el método de ensayo como hidrostatico y remite el valor a 25007-WTP-000-ME-DOC-00001 Piping and Material Specifications, documento interno de BW Water que no forma parte del registro de entregables ni ha sido sometido a ADASA. La misma lamina, en su REFERENCE DESIGN LIST, cita P22-LI-09-009-003 LINE LIST, que es el documento aprobado y que en su Rev 0 incorporo justamente la columna HYDROTEST PRESS. Bar(G) a solicitud de ADASA. La contradiccion deja la presión de prueba de spools ya timbrados FOR CONSTRUCTION fuera del control documental del proyecto. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0, columna HYDROTEST PRESS. Bar(G), y su Consolidated Comment Sheet: "Added Hydrotest Pressure". Nota 4 de las laminas: "TEST PRESSURE REFER TO 25007-WTP-000-ME-DOC-00001 - Piping and Material Specifications". |
| **Que pide a BW Water** | Reference the hydrotest pressure of each spool to the approved Line List (P22-LI-09-009-003) and state the value on the sheet, or submit 25007-WTP-000-ME-DOC-00001 for ADASA approval and reconcile it line by line with the Line List before any test is performed. |
| **Decisión** | |

### 🟠 MAJOR · OBS-08 — Laminas de spool timbradas FOR CONSTRUCTION y firmadas dentro de una entrega emitida solo para aprobación

| | |
|---|---|
| **Donde** | Cajetines y timbre rojo de las laminas 5, 6, 7, 9, 10, 11, 12, 18, 20, 21 (firmas PREPARED/CHECKED/APPROVED fechadas 23-07-2026 y 29-07-2026). |
| **Que dice** | Las laminas de spool llevan el timbre rojo FOR CONSTRUCTION / SHOP FABRICATION firmado, mientras el bloque de revisión de la misma lamina dice ISSUED FOR APPROVAL con fecha 27/07/2026 y el estado del plano matriz en la lamina 3 es ISSUED FOR APPROVAL, Rev C. El submittal 25007-0070 esta declarado IFA. Las laminas además mezclan dos sistemas de numeracion y de revisión: código ADASA P22-DWG-09-005-004 Rev C conviviendo con códigos internos 25007-ME-PI-0901-00XX en Rev 0 y Rev 1 con la misma fecha de emisión. Dado que los hallazgos OBS-01 y OBS-02 recaen sobre componentes retenedores de presión de esas mismas... |
| **Fuente que invoca** | Lamina 3 (Sheet 2), casilla DRAWING STATUS: "ISSUED FOR APPROVAL", Rev C, JULY.24.26. Bloque de revisión de las laminas de spool: "1 | 27/07/2026 | ISSUED FOR APPROVAL". Submittal 25007-0070 emitido como IFA (For Approval). |
| **Que pide a BW Water** | Withdraw the FOR CONSTRUCTION / SHOP FABRICATION stamp from the sheets while the document is under approval, and keep a single revision index traceable to the ADASA code P22-DWG-09-005-004. State whether any spool has already been fabricated or any material purchased against these sheets,... |
| **Decisión** | |

### 🟡 MINOR · NOTE-01 — Modelo 3D Rev A: TAG de linea fuera de la Line List aprobada, colisiones de correlativo y discrepancias de diametro

| | |
|---|---|
| **Donde** | Capas del DWG agregado TALTAL CONTAINER.dwg; 38 TAG unicos extraidos. |
| **Que dice** | El cruce determinista contra la Line List Rev 0 aprobada arroja seis TAG presentes en el modelo y ausentes de la lista -AS-PVC-DN100-09-026, AS-PVC-DN25-09-033, CP-PVC-DN80-09-042, CP-SSD-DN100-09-015, CP-SSD-DN65-09-044 y RD-PVC-DN15-09-001- y cuatro correlativos usados por dos lineas distintas: 09-001, 09-015, 09-026 y 09-044. Tres de esas colisiones son discrepancias de diametro sobre el mismo correlativo: la Line List declara CP-SSD-DN80-09-015 y CP-SSD-DN80-09-044, y las laminas de spool 7 y 9 confirman 3" -es decir DN80- en ambos casos, de modo que las variantes DN100 y DN65 del modelo son erroneas; y la... |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0 aprobada: 34 TAG unicos, cero colisiones de correlativo; CP-SSD-DN80-09-015 CIP FEED TO 2ND STAGE RO, CP-SSD-DN80-09-044 1ST STAGE CIP REJECT OUT, CP-PVC-DN50-09-042 2ND STAGE CIP PERMEATE OUT. |
| **Que pide a BW Water** | Align the line tags in the 3D model to the approved Line List (P22-LI-09-009-003), eliminating the duplicated correlatives 09-001, 09-015, 09-026 and 09-044 and correcting the diameters of 09-015, 09-042 and 09-044, so that model, Piping Layout and Line List share one single set of unique line... |
| **Decisión** | |

### 🟡 MINOR · NOTE-02 — Espesor de pared declarado para DN65 no corresponde a ningun schedule de la norma citada

| | |
|---|---|
| **Donde** | Line List, columna PIPE WALL THICKNESS (mm), filas DN65: DA-SSD-DN65-09-007, -008, -009, CP-SSD-DN65-09-045 y DA-PVC-DN65-09-016. |
| **Que dice** | La Line List aprobada asigna 6,02 mm de espesor a todas las lineas DN65, tanto super duplex como PVC. Para NPS 2 1/2 el espesor de Schedule 80S según ASME B36.19M y el de Schedule 80 PVC según ASTM D1785 son ambos 7,01 mm; 6,02 mm corresponde a NPS 4 Schedule 40, lo que sugiere un arrastre de fila. Las lineas afectadas incluyen CP-SSD-DN65-09-045 y DA-SSD-DN65-09-008, con 90 barG de diseno y 135 barG de prueba. El BOM del plano no declara espesores, de modo que no hay contradiccion en la lamina, pero la ET pide verificación del espesor por ASME B31.3 y esa verificación no se ha presentado. |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión, NOTAS: "1- El espesor de caneria debera ser verificado, basado en las condiciones reales de diseno por ASME B31.3". ASME B36.19M, NPS 2 1/2, Schedule 80S: 7,01 mm. Line List P22-LI-09-009-003 Rev 0: 6,02 mm en las filas DN65. |
| **Que pide a BW Water** | Reconcile the DN65 wall thickness in the Line List with Schedule 80S per ASME B36.19M and Schedule 80 per ASTM D1785 (7.01 mm for NPS 2-1/2), and submit the wall thickness verification to ASME B31.3 required by the Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure Piping,... |
| **Decisión** | |

### 🟡 MINOR · NOTE-03 — Pesos y listado eléctrico dejados como marcadores de posición en laminas de fabricación

| | |
|---|---|
| **Donde** | Notas generales 3 (WEIGHTS) y ELECTRICAL LIST de todas las laminas de spool: 5, 6, 7, 9, 11, 12, 18, 20 y siguientes. |
| **Que dice** | Todas las laminas de spool conservan DRY - XXXX Kg y OPERATING - XXXX Kg, y el ELECTRICAL LIST dice unicamente TBA. En laminas timbradas FOR CONSTRUCTION esos campos son necesarios para dimensionar soportes, definir izajes y coordinar el alcance eléctrico de las valvulas motorizadas. |
| **Fuente que invoca** | Notas generales de las propias laminas: "3. WEIGHTS: DRY - XXXX Kg / OPERATING - XXXX Kg" y "ELECTRICAL LIST: 1. TBA". |
| **Que pide a BW Water** | Fill in the dry and operating weights of every spool and complete the electrical list before issuing at IFC Rev 0, since the supports, lifting arrangements and the electrical scope of the motorised valves depend on them. |
| **Decisión** | |

### 🟡 MINOR · OBS-09 — Designacion de schedule SCH80 en lugar de SCH 80S para el super duplex

| | |
|---|---|
| **Donde** | Item PIPE Beveled End Super Duplex de todos los BOM de spool: laminas 5, 6, 7, 9, 11 (items 1-3), 12 (items 1-4), 18 (items 1-4), 20 (items 1-4). |
| **Que dice** | El BOM designa la caneria super duplex como SCH80 ASME B36.19M. ASME B36.19M es la norma de caneria de acero inoxidable y sus schedules llevan sufijo S -5S, 10S, 40S, 80S-; SCH 80 sin sufijo pertenece a ASME B36.10M. La ET y la Line List Rev 0 aprobada designan ambas SCH 80S. La propia lamina 11 usa correctamente el sufijo en otro item (SCH10S), de modo que la inconsistencia es interna. Conviene precisar que para el rango de diametros empleado -1/2" a 4"- el espesor de pared de SCH 80 y SCH 80S coincide numericamente, por lo que la corrección es de designacion y trazabilidad de certificados, sin implicancia... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión, tabla de items: "CANERIA 1/2" 4" ACERO INOXIDABLE SUPER DUPLEX, SIN COSTURA, ASTM A790 UNS S32750, PREN>40, ASME B36.19M / SCH. 80S / END BE". Line List P22-LI-09-009-003 Rev 0, columna PIPING CLASS: "SUPER DUPLEX STEEL, SCH80S". |
| **Que pide a BW Water** | Change the schedule designation of all super duplex pipe on the bills of materials to SCH 80S per ASME B36.19M, consistent with the Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure Piping, and with the approved Line List. No dimensional change is implied for the NPS 1/2... |
| **Decisión** | |

### 🟡 MINOR · OBS-10 — Sockolet empleado donde la ET lista weldolet para las derivaciones de alta presión

| | |
|---|---|
| **Donde** | Lamina 11 item 11 (4"x1/2", qty 3); lamina 12 item 17 (4"x1/2", qty 2); lamina 18 item 16 (3"x1/2", qty 2); lamina 20 items 16 y 17. |
| **Que dice** | Las derivaciones de instrumento en super duplex se resuelven con SOCKOLET SCH80, ASTM A182 F53 UNS S32750, PREN>40 PER MSS SP 97. El material y la norma coinciden con la ET, pero el accesorio tabulado es el weldolet, de union a tope. La union soldada de encastre deja una rendija anular entre el extremo del tubo y el fondo del alojamiento, que en salmuera concentrada es un sitio preferente de corrosion por rendija. Salvo que BW Water documente el sockolet como equivalente aprobado con el detalle de soldadura y separacion de fondo, corresponde alinearse a la ET. |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión, tabla de items: "WELDOLET, ACERO INOXIDABLE SUPER DUPLEX, ASTM A182 F53 UNS S32750, PREN>40, POR MSS SP 97 / NOTA 2 / BW". |
| **Que pide a BW Water** | Replace the sockolets with weldolets in ASTM A182 F53 UNS S32750, PREN>40, per MSS SP 97 and butt-welded as listed in the Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure Piping, or submit the equivalence justification including the socket weld detail and the crevice... |
| **Decisión** | |

### 🟡 MINOR · OBS-11 — Brida vanstone PVC sin material del anillo de respaldo y empaquetadura full face contra cara resaltada

| | |
|---|---|
| **Donde** | Lamina 6 (items 7 y 11) y lamina 9 (items 7 y 11). |
| **Que dice** | El BOM lista VANSTONE FLANGES ANSI 150# SOCKET - RF PVC ASME B 16.5 sin declarar el material del anillo de respaldo, que es la pieza que toma el apriete. La ET define ese elemento como brida loco en acero carbono recubierto de Rilsan o fibra de vidrio, o PP recubierto con fibra de vidrio. Adicionalmente la union combina una brida declarada RF con una FULL FACE GASKET for Flat Face Flange, combinacion contradictoria en cuanto a superficie de sello. El mismo BOM contiene el error de tipeo SHC80 por SCH80 en el codo PVC de 90 grados (item 4 en ambas laminas). |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.1 Canerias de baja presión: "FLANGE 2" 4" FLANGE LOCO EN ACERO CARBONO CUBIERTO DE RILSAN/FIBRA DE VIDRIO O PP RECUBIERTO CON FIBRA DE VIDRIO, PERFORACIONES CONFORME A ASME B 16.5 / 150"; "EMPAQUETADURA 2" 4" EMPAQUETADURA NO METALICA, CAUCHO NEOPRENO (CR), 1/16"... |
| **Que pide a BW Water** | State the backing ring material of the van stone flanges per the Technical Specification (P22-ET-09-000-001-0), Section 5.2.1 - Low Pressure Piping, reconcile the flange facing with the gasket type at that joint, and correct the SHC80 typographical error on the PVC 90 degree elbow. |
| **Decisión** | |

### ⚪ NOTE · NOTE-04 — El acople Victaulic en A890 Gr. CE8MN es especificacion de la propia ET y queda por debajo del PREN>40 exigido al resto

| | |
|---|---|
| **Donde** | Laminas 11 (items 5 y 6), 12 (items 6 y 7), 18 (items 6 y 7), 20 (items 6 y 7): VICTAULIC TYPE, 2000PSI Rigid Coupling, ASTM A890 Grade CE8MN, EPDM Seal (Grade EW), en 2", 2 1/2" y 4". |
| **Que dice** | BW Water empleo exactamente el acople que la ET especifica, en el rango de diametros que la ET cubre y con una capacidad declarada de 2000 psi, superior a la mayor presión de prueba del sistema. No hay incumplimiento y no procede accion sobre el proveedor. Se deja constancia para revisión interna de ADASA de que la composicion nominal del grado CE8MN de ASTM A890 arroja un PREN del orden de 38, por debajo del PREN>40 que la propia ET impone a todos los demas componentes humedos del sistema super duplex; si ADASA desea homogeneizar el criterio, el cambio a un grado de colada super duplex debe originarse en una... |
| **Fuente que invoca** | ET P22-ET-09-000-001-0, Sección 5.2.2 Canerias de alta presión, tabla de items: "VICTAULIC 1 1/2" 4" ACOPLE RIGIDO, CUERPO EN ASTM A-890 Gr. CE8MN, SELLO GRADO EW, EPDM, TIPO VICTAULIC". |
| **Que pide a BW Water** | No action required from BW Water; the coupling complies with the Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure Piping. Item retained for ADASA internal review of its own specification. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · NOTE-05 — Descripción de servicio de DA-SSD-DN65-09-009 distinta de la Line List aprobada

| | |
|---|---|
| **Donde** | Lamina 3 (Sheet 2), SECTION 1-1 ISO VIEW, rotulos de leader. |
| **Que dice** | La vista isometrica rotula DA-SSD-DN65-09-009 como (BRINE DISCHARGE TO DRAIN), mientras la Line List Rev 0 aprobada la describe como FEED TURBOCHARGER BRINE OUTLET, super duplex, 50 barG de diseno, y asigna la descarga de salmuera a DA-PVC-DN65-09-016, RO BRINE DISCHARGE, PVC, 2 barG de diseno. En la misma vista PE-PVC-DN80-09-013 también se rotula (BRINE DISCHARGE TO DRAIN) frente a la descripción RO OFF SPEC de la Line List. No se levanta como incumplimiento porque el plano puede estar rotulando el destino y no el servicio, pero la frontera entre 09-009 y 09-016 debe quedar identificada para que los paquetes... |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0 aprobada: DA-SSD-DN65-09-009 FEED TURBOCHARGER BRINE OUTLET, SUPER DUPLEX STEEL SCH80S, diseno 50 barG, prueba 75 barG; DA-PVC-DN65-09-016 RO BRINE DISCHARGE, PVC SCH 80, diseno 2 barG, prueba 3 barG; PE-PVC-DN80-09-013 RO OFF SPEC. |
| **Que pide a BW Water** | Use the line descriptions of the approved Line List on the layout callouts, and show on the drawing where DA-SSD-DN65-09-009 ends and DA-PVC-DN65-09-016 begins, so that the boundary between the 50 barG super duplex line and the 2 barG PVC discharge line is unambiguous. |
| **Decisión** | |

### ⚪ NOTE · NOTE-06 — La hoja de respuesta a comentarios cierra la observacion de elevacion de tie-in remitiendo a un plano no sometido

| | |
|---|---|
| **Donde** | Lamina 22, CONSOLIDATED COMMENT SHEET, fila 2, comentario 1. |
| **Que dice** | Revisada la hoja de respuesta item por item, tres de los cuatro comentarios de la Rev B se responden con cambios en la propia Rev C. El comentario de elevaciones de tie-in se responde con "Tie-in point details are indicated in the Tie-In Point Layout drawing", plano que no forma parte del submittal 25007-0070 y que la hoja no identifica por código ni revisión. El cierre no puede verificarse contra ninguna fuente disponible, de modo que la observacion permanece en seguimiento. Nota aparte: la hoja tampoco declara el estado de cada comentario en la columna correspondiente. |
| **Fuente que invoca** | Consolidated Comment Sheet de la lamina 22, fila 2, comentario 1: "Tie-in points (feed inlet, permeate, concentrate, CIP supply/return) are dimensioned in plan view; elevation references absent. Add a tie-in elevation summary table or section drawing prior to IFC (Rev 0)"; respuesta BW Water:... |
| **Que pide a BW Water** | Identify the Tie-In Point Layout drawing by document code and revision and submit it, or add the tie-in elevation summary to this drawing. Until either is received the observation remains open and is tracked as a pending item. |
| **Decisión** | |

---

## Datasheet del presostato diferencial Rev B

**9 observaciones** — MAJOR 3 · MINOR 1 · NOTE 5

La Rev A quedo **Código 1 Approved sin observaciones** en el TM N8. Lo que se revisa es el **contenido nuevo**: el sello de diafragma que la Rev B agrega tras reprobar el Monel.

### 🟠 MAJOR · OBS-01 — Wetted material downgraded from the approved Monel to SS316L, and the wetted-part row is inconsistent with the added diaphragm seal

| | |
|---|---|
| **Donde** | Page 2, rows 10, 20 and 21; Consolidated Comment Sheet, page 16 |
| **Que dice** | The Consolidated Comment Sheet states that the supplier could not pass the quality test for the Monel wetted part and that a diaphragm seal was therefore added as the alternative. Rev B, however, retains a row reading 'Material - Wetted Part: SS316L' for the switch itself, alongside 'Material - Actuator Seal: Viton', while the seal block declares PVC lower housing and PTFE diaphragm as the wetted materials. The two declarations cannot both be true. Unless BW Water confirms that the diaphragm seal fully isolates the switch body from the process, SS316L in direct contact with second stage RO brine is a downgrade... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification (instrumentation to be fully specified and of proven suitability for the service); the approved Rev A of this same datasheet, which carried Monel as the wetted material, as recorded in the Consolidated... |
| **Que pide a BW Water** | Restate the wetted-material rows so that the process boundary is unambiguous: identify every component in contact with the brine feed (seal lower housing, seal diaphragm, gaskets, process connection) with its material, and mark the switch body and its actuator seal as isolated by the diaphragm seal... |
| **Mi verificación** | **Verificado.** La hoja de comentarios declara que el Monel reprobo el ensayo de calidad. Filas 20 y 33 se contradicen sobre que esta mojado. |
| **Decisión** | |

### 🟠 MAJOR · OBS-02 — Declared 200 psi rating of the PVC-bodied diaphragm seal is not valid at the declared 65 C process temperature

| | |
|---|---|
| **Donde** | Page 2, rows 19, 31 and 33; Ashcroft 100/200/300 Threaded Diaphragm Seal data sheet attached at pages 11 (Table 2 and Pressure Ratings) |
| **Que dice** | The sheet declares the diaphragm seal at 'Max. Pressure Range 200 psi' with 'Material - Lower Part (Wetted Part): PVC' and a process temperature of 0 to 65 C. The vendor data attached to this same submittal derates a PVC lower housing to 200 psi at 74 F, 125 psi at 125 F and 80 psi at 150 F. The declared 65 C is 149 F, so the seal is limited to approximately 80 psi (5,5 bar) at its own declared maximum process temperature, that is 40 per cent of the figure printed on the sheet. Unless BW Water confirms that the design pressure at the DPS-09-001 tapping points is below that derated value, the seal becomes the... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.1.5 - Cartridge Filters (maximum working pressure 10 bar) and Section 5.5 - Instrumentation Specification; Ashcroft 100/200/300 Threaded Diaphragm Seal data sheet, Table 2 - Bottom Housing Materials and Pressure Ratings table, both attached... |
| **Que pide a BW Water** | State the derated maximum allowable working pressure of the seal at the declared 65 C, and demonstrate that it is at or above the design pressure of the line at the DPS-09-001 tapping points. If it is not, select a lower housing material that meets the design pressure at temperature, or reduce and... |
| **Mi verificacion** | **Verificado.** Datasheet fila 19: `Process Temperature 0 to 65 C`; fila 31: `200 psi`. ET 5.1.5: filtro cartucho a 10 bar. |
| **Decisión** | |

### 🟠 MAJOR · OBS-03 — Quantity of diaphragm seals and capillaries not declared for a two-port differential element

| | |
|---|---|
| **Donde** | Page 2, rows 3, 28 to 36 (Diaphragm Seal block) and 37 to 44 (Capillary Line block); Ashcroft L-Series dimensional views, page 7 (HIGH PRESSURE PORT / LOW PRESSURE PORT) |
| **Que dice** | A differential pressure element has a high-pressure port and a low-pressure port, both of which are shown on the vendor dimensional views attached to this submittal. Rev B declares a single Diaphragm Seal block and a single Capillary Line block, with quantity stated only once at the top of the sheet as one unit for the instrument. If a single seal is supplied, the low-pressure port remains in direct contact with the brine feed and the material substitution described in the Consolidated Comment Sheet is only half implemented, which would leave the same wetted-material exposure that motivated the change. If two... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification; Ashcroft G and L-Series Pressure Switches data sheet, L-Series differential pressure switch dimensional views, attached by BW Water to this Rev B. |
| **Que pide a BW Water** | Declare the quantity of diaphragm seals and capillaries supplied per instrument, confirm that both the high and low pressure ports are sealed, and state that the two capillary legs are of equal length. Quantify the resulting head offset and temperature zero shift, or confirm that both seals are... |
| **Decisión** | |

### 🟡 MINOR · OBS-04 — Capillary line specification incomplete and one parameter does not belong to the selected model

| | |
|---|---|
| **Donde** | Page 2, rows 37 to 44 (Capillary Line block); Ashcroft 1115A and 1115P Capillary Siphons data sheet attached at pages 14 and 15 |
| **Que dice** | The Capillary Line block declares model 1115A with a process connection of 1/2 inch Male NPT, but omits the parameters that define the installation. Line length is not stated, although the vendor offers it in increments from 1 to 100 feet and it governs the mounting arrangement and the response of the sealed system. The instrument connection is not stated either, although the vendor note is explicit that for switches the capillary instrument connection must be male and for seals the capillary process connection must be male, so the mating of switch, capillary and seal cannot be verified as declared. The block... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification; Ashcroft 1115A and 1115P Capillary Siphons data sheet, Specifications, Ordering Code and installation note, attached by BW Water to this Rev B. |
| **Que pide a BW Water** | Complete the capillary block with line length, instrument connection type and gender for each leg, and delete the diaphragm row, which does not apply to a capillary siphon. State whether the capillary run is exposed to the saline atmosphere inside the container and, if so, justify the bare 304... |
| **Decisión** | |

### ⚪ NOTE · NOTE-01 — Change is declared in the Consolidated Comment Sheet, but not in the revision record or in the Submittal Form Remarks column

| | |
|---|---|
| **Donde** | Page 1, revisión block; page 16, Consolidated Comment Sheet; Submittal Form 25007-0070, Remarks column |
| **Que dice** | BW Water did declare the reason for the revision: the Consolidated Comment Sheet on the last page states that the supplier could not pass the quality test for the Monel wetted part and that a diaphragm seal was added as the alternative. That declaration is acknowledged and it is what allowed ADASA to identify the delta. Two document-control gaps remain around it. The revision block on the cover carries revision B with its date and signatures but no description of the revision, so a reader of the cover alone cannot tell that the wetted material changed. And the Remarks column of the Submittal Form, which the form... |
| **Fuente que invoca** | BW Water Submittal Form 25007-0070, Remarks column definition (Code 1 No update / Code 1 Previously submission w. update / Code 2 Previously / Code 3 Previously / New Submission), and the revision record of the datasheet itself. |
| **Que pide a BW Water** | Populate the revision record with a short description of the change at each revision, and complete the Remarks column of the Submittal Form for every document, declaring the previous disposition and whether the document carries an update. |
| **Decisión** | |

### ⚪ NOTE · NOTE-02 — Relay output confirmed as compliant — no HART finding on this instrument

| | |
|---|---|
| **Donde** | Page 2, rows 24 and 25 (Local Display and Outputs Communication) |
| **Que dice** | The instrument outputs one SPDT contact rated 11 A at 125/250 Vac and 5 A at 30 Vdc, with no analogue output and no local display. ADASA has verified this against the Technical Specification and raises no observation on it. The minimum instrumentation listed in Section 5.5 of the Technical Specification comprises flowmeters, pressure gauges, pressure transmitters, level sensors, conductivity meters and vibration transmitters; a differential pressure switch is not among them, so this instrument is an addition by BW Water beyond the specified minimum. A process switch delivers an on/off alarm rather than... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification, including its list of minimum instrumentation in Sections 5.5.1 to 5.5.6. |
| **Que pide a BW Water** | No action. Recorded so that the point is not reopened at a later revision. |
| **Decisión** | |

### ⚪ NOTE · NOTE-03 — Item numbering duplicated in the requirements table

| | |
|---|---|
| **Donde** | Page 2, the two consecutive rows numbered 8 (Ambient Temperature of Installed Location and Operating Pressure) |
| **Que dice** | Two consecutive rows of the requirements table carry item number 8, so every item number below them is offset by one relative to the true row count. Editorial only, but it makes it awkward to reference a parameter of this sheet by number in a comment sheet or in a purchase order. |
| **Fuente que invoca** | Document quality, consistent with the numbering convention of the component datasheet template used by BW Water for the rest of this submittal. |
| **Que pide a BW Water** | Renumber the requirements table consecutively when the next revision is issued. |
| **Decisión** | |

### ⚪ NOTE · OBS-05 — Full configured part numbers not declared for the newly added seal and capillary

| | |
|---|---|
| **Donde** | Page 2, rows 30 and 39 (Model of the Diaphragm Seal and of the Capillary Line) |
| **Que dice** | The seal is identified only as model '200' and the capillary only as '1115A'. Both are product families whose configuration is set by the ordering codes reproduced in the attached vendor data: for the seal, process connection size, diaphragm type, flushing port, diaphragm and bottom housing materials, instrument connection size, fill fluid and options; for the capillary, process connection, instrument connection and length. As printed, neither component can be verified at goods receipt or during shop inspection, because the sheet does not identify what will actually be built. These two components appear for the... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification (instruments to be of recognised brands with demonstrated sales and technical service presence in Chile, which presupposes an identifiable configured product). |
| **Que pide a BW Water** | State the complete configured ordering code of the diaphragm seal and of the capillary siphon, consistent with the materials, connections, fill fluid and options already declared elsewhere on the sheet. |
| **Decisión** | |

### ⚪ NOTE · OBS-06 — Alarm setpoint and deadband not declared for the switch

| | |
|---|---|
| **Donde** | Page 2, rows 16, 18 and 25; Ashcroft G and L-Series data sheet, Table 2 - Differential Pressure Ranges, attached at page 5 |
| **Que dice** | The sheet declares the measuring principle as single setpoint with adjustable deadband over a 0 to 30 psi differential range and a single SPDT contact, but states neither the trip setpoint nor the deadband. ADASA acknowledges that Rev A was approved without them, so this is an extension of scope rather than an omission by BW Water; the reason ADASA now requires them is the change introduced at Rev B. Adding a sealed system alters the response of the switch, and the vendor data shows the operating window is not unconstrained: the setpoint is adjustable over 15 to 100 per cent of range, that is 4,5 to 30 psi, and... |
| **Fuente que invoca** | Technical Specification (P22-ET-09-000-001-0), Section 5.5 - Instrumentation Specification; Ashcroft G and L-Series Pressure Switches data sheet, Specifications and Table 2 - Differential Pressure Ranges, attached by BW Water to this Rev B. |
| **Que pide a BW Water** | State the alarm setpoint and the deadband to be factory set, and confirm that both fall within the adjustable window of the selected switch element on the declared 0 to 30 psi differential range. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

---

## Modelo 3D Rev A

**14 observaciones** — MAJOR 4 · MINOR 2 · NOTE 8

**Primera emisión.** No hay nada cerrado que reabrir: todo es primer ciclo.

### 🟠 MAJOR · OBS-01 — El TAG de la capa contradice el nombre del XREF y la Line List aprobada en tres lineas y un equipo

| | |
|---|---|
| **Donde** | XREF/capas en lineas 4974-4975, 5077-5078, 5096-5097 y 2326-2327 de la extraccion |
| **Que dice** | En tres XREF de linea el nombre del archivo lleva el TAG aprobado pero la capa interior lleva otro servicio u otro diametro: CP-PVC-DN100-09-026.dwg contiene la capa AS-PVC-DN100-09-026 (servicio CP cambiado a AS); CP-SSD-DN80-09-015.dwg contiene la capa CP-SSD-DN100-09-015 (DN80 cambiado a DN100); CP-SSD-DN80-09-044.dwg contiene la capa CP-SSD-DN65-09-044 (DN80 cambiado a DN65). El mismo defecto alcanza a un equipo: el archivo CIP PUMP (BH-09-002).dwg contiene la capa CIP PUMP BH-009-002. Como en este modelo la identidad la carga el nombre de capa (los solidos son entidades sin nombre), toda lectura del modelo,... |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0 (aprobada, Código 1): "CP-SSD-DN80-09-015 | SUPER DUPLEX STEEL, SCH80S | DN80 | CIP FEED TO 2ND STAGE RO"; "CP-SSD-DN80-09-044 | DN80 | 1ST STAGE CIP REJECT OUT"; "CP-PVC-DN100-09-026 | DN100 | CIP TANK OVERFLOW". |
| **Que pide a BW Water** | Rename the layers inside the three line XREFs and inside the CIP pump XREF so that each layer tag matches both its own file name and the approved Line List (P22-LI-09-009-003 Rev 0), and re-issue the model as Rev B. Confirm whether any isometric, bill of material or fabrication document has already... |
| **Decisión** | |

### 🟠 MAJOR · OBS-02 — RD-PVC-DN15-09-001 no figura en la Line List aprobada y reutiliza el correlativo 09-001

| | |
|---|---|
| **Donde** | XREF RD-PVC-DN15-09-001.dwg y capa homonima (lineas 6830-6831); rotulada también en el Piping Layout Rev C lamina 1 como "RD-PVC-DN15-09-001 (TO DRAIN)" |
| **Que dice** | El modelo, y el Piping Layout Rev C en su lamina 1, llevan una linea de drenaje DN15 con TAG RD-PVC-DN15-09-001. La Line List aprobada no tiene servicio RD ni fila para esa linea, y el correlativo 09-001 ya esta asignado alli a DA-PVC-DN100-09-001 (SWRO brine feed): dos lineas fisicamente distintas comparten un mismo número. Mas alla de la identificacion, la linea no tiene presión de diseno, presión de prueba hidrostática ni requisito de NDE asignados en ningun documento aprobado, de modo que tal como esta no quedaria cubierta por el procedimiento de prueba de presión. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0: "DA-PVC-DN100-09-001 | POLYVINYL CHLORIDE, SCH 80 | DN100 | SWRO BRINE FEED"; la lista no contiene ninguna fila de servicio RD. |
| **Que pide a BW Water** | Assign a free correlativo to the drain line so that no two lines share number 09-001, and add it to the Line List with its piping class, design pressure, hydrotest pressure and NDE requirement. As the Line List stands at Rev 0, issue the corresponding revision and state whether any other document... |
| **Mi verificación** | **Verificado por script.** `RD-PVC-DN15-09-001` no esta en la Line List y reutiliza el correlativo 09-001 de `DA-PVC-DN100-09-001`. |
| **Decisión** | |

### 🟠 MAJOR · OBS-03 — Diametro del CIP permeate out de segunda etapa: DN80 en el modelo, DN50 en la Line List aprobada

| | |
|---|---|
| **Donde** | XREF CP-PVC-DN80-09-042.dwg y capa homonima (lineas 4567-4568) |
| **Que dice** | El modelo, tanto en el nombre del XREF como en la capa, lleva CP-PVC-DN80-09-042, mientras la Line List aprobada asigna DN50 al correlativo 09-042 (2ND STAGE CIP PERMEATE OUT, 36 m3/h). Los dos documentos discrepan en una dimensión que gobierna el computo de materiales y la conexion al estanque CIP. Conviene decir que, hidraulicamente, el DN80 del modelo es el mas plausible de los dos: a 36 m3/h el DN50 SCH 80 PVC da del orden de 5,3 m/s frente a unos 2,4 m/s en DN80, de modo que la discrepancia bien puede ser un error de la Line List y no del modelo. ADASA no presume cual es correcto; hasta que BW Water lo... |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0: "CP-PVC-DN50-09-042 | POLYVINYL CHLORIDE, SCH 80 | DN50 | 5.54 | 2ND STAGE CIP PERMEATE OUT | 36 m3/h". |
| **Que pide a BW Water** | State which diameter governs for line 09-042. If DN80 is correct, revise the Line List and confirm the change does not affect the CIP tank return nozzle or the sizing of the common CIP permeate header (09-043); if DN50 is correct, correct the model. The two documents must not remain in disagreement... |
| **Mi verificación** | **Verificado por script.** Line List dice `CP-PVC-DN50-09-042`; el modelo, DN80. |
| **Decisión** | |

### 🟠 MAJOR · OBS-04 — La linea de descarga de salmuera DA-PVC-DN65-09-016 no aparece en el modelo

| | |
|---|---|
| **Donde** | Arbol completo del modelo (7.486 nodos): ningun XREF ni capa contiene la cadena 09-016 |
| **Que dice** | Ningun archivo XREF ni capa del modelo lleva el TAG DA-PVC-DN65-09-016, la descarga de salmuera RO que la Line List aprobada define en PVC SCH 80 DN65 a 1 bar(G). El modelo si contiene DA-SSD-DN65-09-009 (feed turbocharger brine outlet, super duplex, diseno 50 bar), y el Piping Layout Rev C rotula precisamente esa linea como "BRINE DISCHARGE TO DRAIN". Salvo que el tramo de PVC este modelado dentro del archivo de 09-009, la lectura es que el cambio de material de super duplex a PVC en la salida del modulo no esta representado, con efecto sobre el computo de materiales y sobre el tie-in en el limite de bateria. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0: "DA-PVC-DN65-09-016 | POLYVINYL CHLORIDE, SCH 80 | DN65 | 6.02 | RO BRINE DISCHARGE | 28.0 m3/h | OPER 1 bar(G) | DESIGN 2 bar(G) | HYDROTEST 3 bar(G)". |
| **Que pide a BW Water** | Confirm whether line DA-PVC-DN65-09-016 is modelled. If it is embedded in the DA-SSD-DN65-09-009 file, model it as its own tagged entity showing where the super duplex to PVC transition occurs. If the design now discharges in super duplex up to the battery limit, state so and revise the Line List... |
| **Mi verificación** | **Verificado por script.** `DA-PVC-DN65-09-016` esta en la Line List Rev 0 y no en el modelo. |
| **Decisión** | |

### 🟡 MINOR · OBS-05 — AS-PVC-DN25-09-033 esta modelada pero no tiene fila en la Line List aprobada

| | |
|---|---|
| **Donde** | XREF AS-PVC-DN25-09-033.dwg y capa homonima (lineas 4530-4531) |
| **Que dice** | El modelo federa el archivo AS-PVC-DN25-09-033.dwg. La Line List aprobada corre los correlativos 09-031, 09-032, 09-034, 09-035 y 09-036 para el servicio de antiscalante y salta el 09-033, de modo que la linea existe como geometria sin presión de diseno, presión de prueba ni NDE asignados. El patron (un correlativo saltado en la lista y presente en el modelo) apunta mas a una omisión de la Line List que a geometria espuria, aunque BW Water esta en mejor posición para decirlo. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0, servicio CHEMICAL: filas AS-PVC-DN25-09-031, AS-PVC-DN50-09-032, AS-PVC-DN15-09-034, AS-PVC-DN15-09-035 y AS-PVC-DN15-09-036; no existe fila 09-033. |
| **Que pide a BW Water** | State the function of line AS-PVC-DN25-09-033 and either add it to the Line List with its full design data (piping class, design and hydrotest pressure, NDE) or remove it from the model. |
| **Decisión** | |

### 🟡 MINOR · OBS-06 — El archivo entregado no se identifica como P22-DWG-09-005-007 Rev A

| | |
|---|---|
| **Donde** | Metadatos del NWD: titulo interno "V14 Taltal.nwd"; archivo original C:\Users\AhmadHaffizieBinRosl\...\14.3 3D Model\01 Navis\V14 Taltal.nwd |
| **Que dice** | El archivo se llama "V14 Taltal.nwd" y su titulo interno de documento es la misma cadena. Ni el código del documento ni el indice de revisión aparecen en ninguna parte del archivo; la unica referencia de versión que carga es la interna de BW Water, "V14", sin relacion con la Rev A. Fuera del sobre del submittal no hay forma de saber que revisión del modelo se esta abriendo. El Piping Layout, enviado en el mismo sobre, si declara "ADASACode: P22-DWG-09-005-004" y "Revision No.: C" en su encabezado, de modo que la convencion ya esta establecida para los entregables tipo DWG. |
| **Fuente que invoca** | Submittal Form 25007-0070, fila 2: "P22-DWG-09-005-007 | A | 3D MODEL | DWG | IFA"; sistema de codificacion del proyecto P22-TT-AA-DDD-NNN-R; encabezado del P22-DWG-09-005-004 Rev C entregado en el mismo submittal. |
| **Que pide a BW Water** | Name the deliverable file with its document code and revision (P22-DWG-09-005-007_Rev.B) and embed that code, the revision index and the issue date in a visible text entity inside the model, so that the file identifies itself outside the submittal form. |
| **Decisión** | |

### ⚪ NOTE · NOTE-01 — La identidad de linea vive en el nombre de capa y de archivo, no en una propiedad del objeto

| | |
|---|---|
| **Donde** | Sección "Categorias de propiedad presentes" y arbol del modelo (entidades 3D Solid sin nombre bajo capas de AutoCAD) |
| **Que dice** | El esquema de propiedades presente en el modelo incluye atributos de tuberia de AutoCAD Plant 3D (Class, Code, End Type, DesignStd, DesignPressureFactor, BOP, BOS, ActuatorType), de modo que parte del contenido si proviene de una aplicacion de tuberia. Sin embargo, la identidad que un revisor puede leer efectivamente es el nombre de la capa y el del archivo XREF: los solidos van sin nombre. Esa es justamente la razon por la que los desajustes entre capa y archivo del punto OBS-01 pudieron quedar en el archivo sin detectarse. La observacion es informativa sobre el método de modelado, no un requisito. |
| **Fuente que invoca** | Sin requisito contractual asociado; ADASA lo plantea como mejora del entregable para las revisiones sucesivas. |
| **Que pide a BW Water** | Consider carrying the line tag as an object property (Plant 3D line number or equivalent) in addition to the layer name, so the model can be checked automatically against the Line List instead of by reading layer names. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · NOTE-02 — Valor de propiedad ActuatorType = PNEUMATIC en un modulo sin servicio de aire de instrumentos

| | |
|---|---|
| **Donde** | Categoria de propiedad "AutoCAD", valor de ejemplo ActuatorType = PNEUMATIC |
| **Que dice** | Entre los valores de propiedad hallados en el modelo aparece ActuatorType = PNEUMATIC. La extraccion no ata el valor a un objeto determinado, de modo que bien puede ser un valor por defecto de catalogo arrastrado y no un dato del proyecto. Vale la pena confirmarlo, porque la Line List aprobada no contiene ningun servicio de aire de instrumentos (solo AS, DA, PE, CP y RD), de modo que una valvula de actuacion neumatica no tendria suministro de aire. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0 (sin servicio de aire de instrumentos); Technical Specification (P22-ET-09-000-001-0), Section 5.2.3 - Valves. |
| **Que pide a BW Water** | Confirm that no pneumatically actuated valve is within scope and, if catalogue default properties remain in the model, scrub them before issuing Rev B. |
| **Decisión** | |

### ⚪ NOTE · NOTE-03 — Capa "BASE STRUCTURE (TBA)" bajo la bomba HP en un modelo emitido For Approval

| | |
|---|---|
| **Donde** | XREF RO HP PUMP (BH-09-001).dwg, capa "BASE STRUCTURE (TBA)" (linea 2026 de la extraccion) |
| **Que dice** | El XREF de la bomba de alta presión contiene una capa marcada explicitamente TBA. En un modelo emitido For Approval conviene declarar si la geometria de la estructura base mostrada es indicativa o definitiva, ya que la base de la bomba apoya en el piso del contenedor y condiciona su anclaje. |
| **Fuente que invoca** | Submittal Form 25007-0070: el documento se emite For Approval (IFA), de modo que su contenido se revisa como definitivo salvo declaracion en contrario. |
| **Que pide a BW Water** | State whether the HP pump base structure shown is final. If it remains open, indicate when it will be closed and whether it affects the container floor loading already issued. |
| **Decisión** | |

### ⚪ NOTE · NOTE-04 — El modelo contiene la geometria de los cuatro puntos que siguen abiertos en el Piping Layout

| | |
|---|---|
| **Donde** | Capas EQUIPMENT ACCESS DOOR (linea 162), LATERAL ACCESS DOOR (231), EMERGENCY DOOR (154), TIE-IN BOX (402) y LCP (2927) |
| **Que dice** | Las capas de puerta de acceso a equipos, puerta lateral, puerta de emergencia, caja de tie-in y LCP llevan solidos, de modo que la geometria detras de las cuatro notas que el Piping Layout arrastra desde la revisión anterior (puertas no representadas, ruteo del LCP, bridas de limite de modulo y vista de elevacion del tie-in) ya existe en el modelo. Se registra como hallazgo positivo: la misma fuente permite cerrar esas notas en el plano al emitir Rev 0, y hace que el pedido de viewpoints del punto OBS-08 sea proporcionado y no una carga anadida. |
| **Fuente que invoca** | Notas abiertas sobre el P22-DWG-09-005-004 recogidas en la Consolidated Comment Sheet de la lamina 4 del Rev C (puertas, ruteo del LCP, bridas de limite, elevacion del tie-in). |
| **Que pide a BW Water** | Use the model as the source for the door, tie-in elevation and LCP routing views to be added to the Piping Layout at Rev 0, so that drawing and model remain consistent. |
| **Decisión** | |

### ⚪ NOTE · NOTE-05 — Prefijo de servicio de la linea 09-019: el plano usa CP-, la Line List y el modelo usan PE-

| | |
|---|---|
| **Donde** | Piping Layout Rev C, lamina 1 (rotulo "CP-PVC-DN80-09-019 (MAKE-UP CIP)"); modelo 3D, XREF PE-PVC-DN80-09-019.dwg y capa homonima |
| **Que dice** | El modelo lleva PE-PVC-DN80-09-019, que coincide con la fila de la Line List aprobada (MAKE-UP FOR CIP, permeate water, DN80). La lamina 1 del Piping Layout Rev C rotula la misma linea como CP-PVC-DN80-09-019, y ese prefijo también viajo a la propia observacion previa de ADASA reproducida en la hoja de respuesta a comentarios. No se imputa falta a nadie: el punto es unicamente alinear el plano con la Line List y con el modelo, que coinciden entre si. |
| **Fuente que invoca** | Line List P22-LI-09-009-003 Rev 0: "PE-PVC-DN80-09-019 | POLYVINYL CHLORIDE, SCH 80 | DN80 | 7.62 | MAKE-UP FOR CIP | PERMEATE WATER". |
| **Que pide a BW Water** | Correct the tag on the Piping Layout to PE-PVC-DN80-09-019 at Rev 0, matching the approved Line List and the 3D model. |
| **Decisión** | |

### ⚪ NOTE · OBS-07 — El NWD se guardo, no se publico: sin autor, fecha de publicacion ni destinatario

| | |
|---|---|
| **Donde** | Bloque de propiedades de publicacion del NWD (lectura devuelve referencia nula) |
| **Que dice** | El archivo no tiene propiedades de publicacion: la lectura lanza una referencia a objeto no establecida, es decir el bloque nunca se escribio. Faltan autor, fecha de publicacion, destinatario, asunto y control de caducidad; la unica traza de autoria es el usuario de último guardado en las propiedades de resumen y una ruta personal. Publicar un NWD es una operacion de un paso en Navisworks y es lo que convierte al archivo en un registro fechado y atribuible. ADASA no lo había exigido antes, de modo que se plantea como extensión del control documental que ya se aplica a los planos y no como apartamiento de un... |
| **Fuente que invoca** | No consta requisito previo de ET, PIE, BAE ni transmittal sobre publicacion del NWD; la base es el control documental aplicado a los demas entregables del submittal 25007-0070 (código, revisión, fecha y emisor declarados). |
| **Que pide a BW Water** | From Rev B onwards, publish the model instead of saving it, completing title (P22-DWG-09-005-007 3D Model), author, publication date and recipient (Aguas Antofagasta). |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · OBS-08 — El modelo no declara conjuntos de seleccion ni viewpoints

| | |
|---|---|
| **Donde** | Secciones "Conjuntos de seleccion declarados" y "Viewpoints guardados" de la extraccion: ninguno en ambas |
| **Que dice** | El modelo no declara conjuntos de seleccion ni vistas guardadas, de modo que no propone estructura por disciplina o sistema ni ningun punto de revisión. Quien lo abre parte de un arbol unico de 7.486 nodos sin puerta de entrada. Importa porque la geometria que permitiria zanjar los puntos aun abiertos del Piping Layout esta dentro del archivo (las capas EQUIPMENT ACCESS DOOR, LATERAL ACCESS DOOR, TIE-IN BOX y LCP tienen solidos), y sin viewpoints no hay forma de dirigir la revisión hacia ellos. Ni la ET ni transmittal previo alguno exigieron conjuntos ni vistas: se plantea como pedido nuevo de ADASA. |
| **Fuente que invoca** | No consta requisito previo de modelado en ET, PIE, BAE, Oferta Rev.1 ni transmittal; el modelo es item nuevo de primer ciclo. ADASA extiende el alcance para las revisiones sucesivas. |
| **Que pide a BW Water** | At Rev B, declare selection sets by system (RO, CIP, antiscalant, drains, container structure, instrumentation) and save viewpoints covering, as a minimum: the equipment access door and the lateral access door with the piping routed along those walls, the tie-in box in elevation, and the LCP with... |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

### ⚪ NOTE · OBS-09 — Ninguna valvula esta identificada en el modelo

| | |
|---|---|
| **Donde** | Arbol completo del modelo: cero capas u objetos con TAG de valvula (VE-09-xxx / VM-09-xxx) |
| **Que dice** | El modelo rotula los equipos (BOI-09-001 y 002, BH-09-001, BH-09-002, BDS-09-001 y 002, FIL-09-001 y 002, SIP-09-001 y 002, TK-09-001 y 002, MZE-09-001), la instrumentacion de campo (AE-09-001A y 001B hasta AE-09-006, CIT-09-001B hasta CIT-09-005, ORPIT-09-001A, PHIT-09-006) y las lineas, cada uno en su capa con nombre. Ninguna capa ni objeto lleva TAG de valvula. Los cuerpos de valvula aparecen como solidos sin nombre dentro de los XREF de linea, lo que deja al modelo sin poder responder aquello para lo que normalmente se abre un layout 3D: si cada valvula de actuacion eléctrica tiene espacio para operarse y... |
| **Fuente que invoca** | No consta requisito de ET ni de transmittal previo sobre identificacion de valvulas en el modelo 3D; la base es la propia convencion de rotulado del modelo para equipos e instrumentos, y el criterio de actuacion eléctrica en linea principal de la Technical Specification (P22-ET-09-000-001-0),... |
| **Que pide a BW Water** | At Rev B, place each valve on a layer named with its tag, following the convention already applied to equipment and instruments in this same model, at least for the electrically actuated valves on the main process lines. |
| **Encuadre** | ⚠️ **Pedido nuevo de ADASA**, no incumplimiento. Redactar como extensión |
| **Decisión** | |

---

## Como usar esto

Llena la fila **Decisión** de cada observacion con una de estas cuatro:

- **EMITIR** — va al transmittal tal como esta
- **BAJAR** — va, pero con severidad menor o como nota
- **ACLARACION** — se emite como pregunta, no como defecto
- **NO EMITIR** — se descarta

Lo que quede como EMITIR o BAJAR entra a las subsecciones 2.3, 2.4 y 2.5 del TM N30 y a los `CC_ADASA` de cada documento. Lo descartado no se menciona.
