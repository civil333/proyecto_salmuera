#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N30 ADASA-BW_WATER.
Submittals 25007-0068 (E68), 25007-0069 (E69) y 25007-0070 (E70).
Fecha de emision: 05-Ago-2026.

RE-ESCOPEADO. El N30 se redacto el 23-Jul con la sola E68 y quedo en BORRADOR
sin enviarse. Al llegar la E69 y la E70 antes de la emision se absorben las dos,
que es el precedente del TM N27 (re-escopeado de E63 a E63+E64 por la misma
razon). El N31 queda libre para la proxima entrega.

Veredicto global: 3 - TO BE REVISED. Tally: 2 Code 1 + 2 Code 2 + 1 Code 3,
mas un conjunto sin codificar devuelto como no recibido.

  2.1 Datasheet of PLC and HMI Panel Component Rev 0 (P22-ET-09-008-001) Code 1
      Sin cambios respecto del borrador del 23-Jul. Declaracion vinculante del
      terminal 2711P-T10C22D9P; los cuatro documentos con el -D8S se alinean via
      Seccion 3.
  2.2 Fabrication and Testing Dossier Index Rev A (P22-BA-09-000-013)    Code 3
      Fija el veredicto global. 6 OBS + 4 NOTE.
  2.3 Piping Layout Rev C (P22-DWG-09-005-004), las 4 paginas del documento
                                                                        Code 2
  2.4 Conjunto de taller 25007-ME-PI-0901-0006 a -0016      NO RECIBIDO
      NO se codifica. Sin codigo ADASA, ausente del Submittal Form, y la portada
      del documento que los contiene declara "Page 1 of 4". No se aprueba ni se
      rechaza lo que no fue sometido. Los dos CRITICAL se emiten contra ellos.
  2.5 3D Model Rev A (P22-DWG-09-005-007)                                Code 2
      Item NUEVO del registro. Revisado contra los listados aprobados leyendo la
      categoria AutoCAD de Plant 3D del propio modelo, NO los nombres de capa.
      NO se objeta rigor BIM (propiedades de publicacion, conjuntos de seleccion,
      viewpoints): la ET no lo exige y una observacion sin requisito que la
      sostenga es refutable.
  2.6 Datasheet of Differential Pressure Switch Rev B (P22-LI-09-008-006) Code 1
      Sin observaciones.

De las 62 observaciones que arrojo la revision de la E70 se emiten 14. Las 48
descartadas no se mencionan en ninguna parte de este documento.

CC_ADASA: Code 3 y Code 2 SIEMPRE anotan (CLAUDE.md Seccion 3.8). Excepcion
declarada en la Seccion 4: el modelo 3D es Code 2 y es un .nwd, que no admite el
formato de anotacion de los planos, de modo que sus observaciones van integras en
el texto de la subseccion 2.5.

SIN numeros manuales en add_heading() (el template ADASA auto-numera H1/H2).
Referencias por NOMBRE de seccion. Cero simbolo de seccion.
"""

import os
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.opc.constants import RELATIONSHIP_TYPE as RT  # noqa: E402


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N30 ADASA-BW_WATER.docx")

# Los dos PDF anotados pesan 14,3 MB juntos: van por enlace de descarga, no
# adjuntos. Al correo se adjunta solo el PDF del transmittal (0,21 MB).
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19Llot7JjfVf8lcyurHIZDfL6nZ13HIC/"
    "V4Ej-jY6AOk8cbU29kS4w7Z3SD8wrWSB-4r-gvdeEZw0"
)


def add_hyperlink(paragraph, url, text):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    rfonts.set(qn("w:ascii"), "Arial")
    rfonts.set(qn("w:hAnsi"), "Arial")
    rpr.append(rfonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "24")
    rpr.append(sz)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)
    return hyperlink


def add_para(doc, runs):
    para = doc.add_paragraph()
    for item in runs:
        text = item[0]
        attrs = item[1] if len(item) > 1 else {}
        run = para.add_run(text)
        if attrs.get("bold"):
            run.bold = True
        if attrs.get("italic"):
            run.italic = True
    aplicar_arial_12(para)
    return para


def add_bullet(doc, text):
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


# ---------------------------------------------------------------------------
# Seccion 2 condensada: por documento, Response Code + Status corto + Action,
# citando el RANGO de IDs del PDF anotado. Sin tabla de observaciones: ese
# detalle vive en el CC_ADASA (CLAUDE.md Seccion 3.2).
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="Datasheet of PLC and HMI Panel Component Rev 0 — P22-ET-09-008-001",
        code="Response Code: 1 — Approved",
        paras=[
            [("Status.", {"bold": True}),
             (" Rev 0 closes the Transmittal N26 cycle. The document code is aligned to "
              "P22-ET-09-008-001 on the cover and on all seven component headers, and the "
              "RTD-module quantity is confirmed as two 5069-IY4 units on the Control System "
              "Architecture Rev D, covering the four temperature elements of the I/O List "
              "Rev 5. No technical content changed between Rev C and Rev 0 and the datasheet "
              "requires no modification to itself.",)],
            [("Binding declaration — operator terminal.", {"bold": True}),
             (" The catalogue number of the operator terminal has differed between this "
              "datasheet and the control set since the first issue of both. ADASA declares "
              "the binding catalogue number to be 2711P-T10C22D9P, stated in this datasheet "
              "since Rev A and fixed at Transmittal N22 as the hardware basis for the HMI "
              "screen design. Per the manufacturer's technical data, catalogue number "
              "2711P-T10C21D8S provides one 10/100Base-T Ethernet port and 512 MB of RAM and "
              "therefore does not meet the two Ethernet RJ45 ports and 1 GB stated in the "
              "requirement rows of this datasheet. Should BW Water intend to supply the "
              "Standard terminal instead, state so in writing before procurement, "
              "demonstrating that it meets the requirement of the Technical Specification "
              "(P22-ET-09-000-001-0), Section 5.4 - Control System, to store historical data "
              "and display trends of the main process variables. The point is time-critical "
              "because the panel enters fabrication before the next document cycle.",)],
            [("Action: none on this document — accepted; the datasheet stands as issued at "
              "Rev 0.", {"bold": True}),
             (" Related deliverables tracked in Section 3: alignment of the PLC/LCP Outline "
              "Panel Drawing Rev 0, the PLC/LCP Schematic Diagram Rev A, the PLC/LCP FAT "
              "Procedure Rev A and the Control System Architecture Rev D to the binding "
              "catalogue number. Six documentation items are to be corrected at the next "
              "natural issue of this datasheet, none of them affecting its technical content: "
              "the consolidated comment sheet no longer carries the closure record of the "
              "three Transmittal N21 items and cites a revision that does not exist; the "
              "cover states 49 pages against the 50 issued; the seven component headers keep "
              "the Issued for Approval stamp on a submission for construction; the "
              "analog-output sheet carries the design intent of a digital output and leaves "
              "its model as 5069-OF4/OF8 where the Control System Architecture fixes two "
              "5069-OF4; and the component headers carry no revision index.",)],
        ],
    ),
    dict(
        heading="Fabrication and Testing Dossier Index Rev A — P22-BA-09-000-013",
        code="Response Code: 3 — To be revised",
        paras=[
            [("Status.", {"bold": True}),
             (" First issue of the index requested in ADASA's letter of 25 July. It arrived "
              "on Monday 27 July; the records that were to accompany it did not. As a "
              "document it cannot yet perform its function: it lists 27 chapters with no "
              "traceability and omits several chapters that its own governing documents "
              "require. Itemised in P22-BA-09-000-013_A_CC_ADASA.pdf.",)],
            [("Action — re-issue as Rev B:", {"bold": True}),
             (" add the document number, revision and inclusion status to every line with a "
              "cross-reference to the row of the Inspection and Test Plan that generates each "
              "record, and add the chapters for dispatch preparation, the FAT Approval "
              "Certificate, inspection personnel qualifications and test equipment "
              "calibration, main equipment manufacturer certificates, and the non-conformance "
              "and weld repair register (OBS-01 to OBS-06 and NOTE-01 to NOTE-04 on the "
              "annotated PDF). The three non-destructive testing procedures listed in "
              "chapters B3, B4 and B6 are to be submitted for ADASA review before welding "
              "starts, since records produced under procedures not yet approved are not "
              "admissible into the dossier.",)],
            [("This code applies to the index as a document.", {"bold": True}),
             (" The dossier as a deliverable of the Technical Specification "
              "(P22-ET-09-000-001-0), Section 7, has not been delivered and is unaffected by "
              "it: it remains outstanding and continues to gate items 8.3 and 8.4 of the "
              "Inspection and Testing Base Plan (P22-IT-09-000-001-0).",)],
        ],
    ),
    dict(
        heading="Piping Layout Rev C — P22-DWG-09-005-004",
        code="Response Code: 2 — Approved as noted",
        paras=[
            [("Status.", {"bold": True}),
             (" The document declares itself as four pages and those four are in order: the "
              "general arrangement, the two sections and the isometric views are consistent "
              "with the approved Line List and resolve the equipment access and lateral "
              "openings and the antiscalant and CIP battery-limit terminations carried from "
              "Transmittal N15. Two of the four items carried from Rev B remain partly open "
              "and are incorporable at IFC Rev 0 without a further revision. The file also "
              "contains eighteen pages that do not belong to this document; those are dealt "
              "with in the following subsection. Itemised in "
              "P22-DWG-09-005-004_C_CC_ADASA.pdf.",)],
            [("Action to issue at IFC Rev 0 — no new drawing revision required:", {"bold": True}),
             (" add a tie-in schedule listing, for every battery-limit connection, the line "
              "tag, nominal diameter, connection type and elevation referred to a datum "
              "declared on the drawing, covering the permeate and CIP supply and return "
              "lines; annotate the flange class against the CIP and antiscalant battery-limit "
              "terminations consistent with the approved Line List; and state whether the "
              "module carries one or two local control panels, tagging each enclosure "
              "consistently with the approved Local Control Panel datasheet and the Single "
              "Line Diagram (OBS-02, OBS-03 and NOTE-01 to NOTE-03 on the annotated "
              "PDF). ADASA "
              "accepts the drawing on the basis that these are annotations and schedules "
              "added to the existing geometry, with no change to the arrangement.",)],
            [("Tracked as a cross-document deliverable, with no modification to this "
              "drawing:", {"bold": True}),
             (" confirmation that the anchorage of the container and of the external CIP and "
              "dosing area, with the corresponding loads and bolt layout for the ADASA "
              "concrete bases, is covered by the seismic calculation report and the civil "
              "requirements drawing, stating the code and issue date of both. The "
              "holding-down bolts for the externally mounted equipment are to be defined and "
              "supplied by the equipment manufacturer.",)],
        ],
    ),
    dict(
        heading="Shop fabrication set 25007-ME-PI-0901-0006 to -0016",
        code="Returned — not received as a deliverable",
        paras=[
            [("Status.", {"bold": True}),
             (" Pages 5 to 21 of the file submitted under P22-DWG-09-005-004 Rev C are eleven "
              "shop fabrication drawings under BW Water's own numbering, with their own "
              "revision index, spool titles instead of a drawing title, and a FOR "
              "CONSTRUCTION stamp on all seventeen pages. They carry no ADASA document code, "
              "they are not listed in the Submittal Form, and the cover sheet of the document "
              "containing them declares Page 1 of 4. ADASA cannot approve or reject what was "
              "not submitted, so this set is returned as not received and carries no response "
              "code. Itemised in 25007-ME-PI-0901_CC_ADASA.pdf.",)],
            [("Two items require correction before any of these spools is built.",
              {"bold": True}),
             (" They are issued now, ahead of the formal submission, because the sheets are "
              "stamped for construction and dated 23 July.",)],
            [("Threaded austenitic branch connections on the highest-pressure super duplex "
              "lines.", {"bold": True}),
             (" The half-inch instrument tappings on sheets 11, 12, 14, 16, 17, 18 and 20 are "
              "resolved with ANSI 150# threaded half couplings in ASTM A182 Gr. F304 and "
              "F316L, on lines that the approved Line List rates at 60 to 90 barG design and "
              "90 to 135 barG hydrotest, in brine of 45,000 to 55,000 ppm chloride. The "
              "Technical Specification (P22-ET-09-000-001-0), Section 5.2.2 - High Pressure "
              "Piping, requires super duplex ASTM A182 F53 UNS S32750 with PREN above 40 and "
              "Class 900 rating for high-pressure components. The same sheets already use the "
              "correct detail on other half-inch branches, in super duplex sockolets to MSS "
              "SP 97.",)],
            [("Undeclared specification break between the super duplex and PVC systems.",
              {"bold": True}),
             (" On sheets 5, 6, 7 and 9 the boundary between the two systems sits at an ANSI "
              "150# flanged joint adjacent to a single motorised butterfly valve, with no "
              "specification break symbol and no line number split. The spools titled "
              "CP-SSD-DN65-09-045 and CP-SSD-DN80-09-044 incorporate PVC SCH 80 pipe while "
              "the approved Line List classifies both lines as super duplex at 80 to 90 barG "
              "design and 120 to 135 barG hydrotest, and rates the PVC lines at 5 barG design "
              "and 7.5 barG hydrotest.",)],
            [("Action:", {"bold": True}),
             (" either remove the shop fabrication set from P22-DWG-09-005-004 and submit it "
              "as a separate deliverable with its own ADASA code and revision index, or "
              "extend the cover sheet and the Submittal Form to declare it, stating in both "
              "cases the review status expected from ADASA. Replace the threaded austenitic "
              "couplings with welded super duplex branch fittings and confirm in writing that "
              "no austenitic, threaded or Class 150 pressure-retaining component remains "
              "anywhere in the super duplex system, stating whether any of these branches has "
              "already been fabricated. Show the specification break explicitly, split the "
              "line numbers at that joint so the PVC segments carry their own line number, "
              "piping class, design pressure and hydrotest pressure, issue the corresponding "
              "addition to the Line List, and state how the PVC side is protected from the "
              "high-pressure side with the motorised valve closed (OBS-01, OBS-04, OBS-05 "
              "and OBS-06 on the annotated PDF).",)],
        ],
    ),
    dict(
        heading="3D Model Rev A — P22-DWG-09-005-007",
        code="Response Code: 2 — Approved as noted",
        paras=[
            [("Status.", {"bold": True}),
             (" First issue of the model, submitted for approval. It is a federated "
              "Navisworks file built from a single AutoCAD Plant 3D source, in millimetres, "
              "with typed objects that carry engineering properties: line numbers, tags, "
              "classes, sizes and specifications. ADASA reviewed it against the approved "
              "Equipment, Valve, Instrument and Line Lists using those object properties. The "
              "model is coherent with the approved lists in the large majority of its "
              "content, and what requires correction is the identification of the file and a "
              "defined set of tag divergences.",)],
            [("Action to issue at IFC Rev 0 — no new model revision required:", {"bold": True}),
             (" identify the file by its document code P22-DWG-09-005-007 and its revision "
              "index in the document properties, and issue the final revision under that "
              "identity, since the file as received is titled V14 Taltal.nwd. Correct the "
              "malformed tags BH-009-002, which carries three digits in the area segment "
              "where the approved Equipment List states BH-09-002, and VM-09-094, which "
              "carries a trailing question mark. Resolve the fifty-seven objects whose tag "
              "property is set to a question mark.",)],
            [("Reconcile with the approved lists:", {"bold": True}),
             (" DPS-09-002 in the model against DPS-09-001 in the Instrument List Rev E and "
              "in the datasheet issued in this same submittal; BOI-09-006 and the valves "
              "VM-09-131, VM-09-132, VM-09-133 and VRP-09-001, which do not appear in the "
              "approved Equipment and Valve Lists; and the reverse osmosis vessels, modelled "
              "as BOI-09-001-1 to -5 and BOI-09-002-1 to -4 where the Equipment List declares "
              "BOI-09-001 and BOI-09-002. Reconcile four line numbers where the model and the "
              "approved Line List disagree on an attribute while sharing the sequential "
              "number: 09-042 as DN80 against DN50, 09-015 as DN100 against DN80, 09-044 as "
              "DN65 against DN80, and 09-026 as antiscalant service against CIP service. "
              "Resolve the reuse of sequential number 09-001 by both DA-PVC-DN100-09-001 and "
              "RD-PVC-DN15-09-001, the latter not appearing in the approved Line List. Where "
              "a divergence reflects a change of engineering rather than a modelling error, "
              "issue the corresponding revision of the affected list so that the model and "
              "the lists state the same thing.",)],
            [("No annotated PDF accompanies this document.", {"bold": True}),
             (" A Navisworks file cannot carry the annotation format used for drawings, so "
              "the observations above are stated in full here.",)],
        ],
    ),
    dict(
        heading="Datasheet of Differential Pressure Switch Rev B — P22-LI-09-008-006",
        code="Response Code: 1 — Approved",
        paras=[
            [("Status.", {"bold": True}),
             (" Rev B of a datasheet that ADASA approved at Rev A in Transmittal N8. The "
              "consolidated comment sheet declares the reason for the revision: the vendor "
              "could not pass the quality test for Monel wetted parts, so a diaphragm seal is "
              "added as the alternative, and the datasheet is extended with its information. "
              "ADASA accepts the change as declared.",)],
            [("Action: none — accepted; issue directly at IFC Rev 0.", {"bold": True})],
        ],
    ),
]

PENDING_OPEN = [
    ("N28",
     "Control family (Control Philosophy Rev E, Alarm & Interlock List Rev C, "
     "Control & Sequence Chart Rev A)",
     "each correct in what it governs, but the three disagree on tags and setpoints "
     "(winding and bearing mapping, HP pump vibration trip)",
     "OVERDUE: the coordinated re-issue at Rev 0 was due Friday 31 July and no "
     "revision has been received"),
    ("N22",
     "HMI Display Screenshot (P22-LI-09-008-016 Rev A)",
     "the electrical-variables and energy screen, the trending screen, the setpoint "
     "screen and several process zones are still missing",
     "OPEN: re-issue as Rev B. Oldest open commitment in the project"),
    ("N27",
     "Operating and Maintenance Manual (P22-BA-09-000-012 Rev A)",
     "governed by the Control family; cannot close until that set issues at Rev 0 and "
     "the HMI screenshots issue",
     "OPEN: Rev B after the Control family closes"),
]

PENDING_SUMMARY = (
    "the fabrication and testing dossier itself, outstanding against the Technical "
    "Specification, Section 7, and gating items 8.3 and 8.4 of the Inspection and Testing "
    "Base Plan; Equipment Layout Rev C (Code 3, RO cartridge filter orientation); GA of the "
    "Antiscalant Dosing Tank Rev B (Code 3, seismic anchor loads); Instrument Location "
    "Layout Rev C (Code 3, from Transmittal N23); Tie-In Point Layout Rev A (Code 3, from "
    "Transmittal N7, the longest-standing open item); and the FAT Procedure RTD protection "
    "sign-off, held from Transmittal N27 until the Control Philosophy issues at Rev 0."
)

CROSS_DOC = (
    "the operator-terminal catalogue number in the PLC/LCP Outline Panel Drawing Rev 0, the "
    "PLC/LCP Schematic Diagram Rev A, the PLC/LCP FAT Procedure Rev A and the Control System "
    "Architecture Rev D, to be corrected to 2711P-T10C22D9P."
)

REVIEW_PERIOD = (
    "The Submittal Form of 25007-0070 requests return by Saturday 8 August, three calendar "
    "days from issue. The standard documentary review period of the Special Administrative "
    "Conditions (BAE 12803), Clause 37.2, is seven working days, which for this submittal "
    "ends on Friday 14 August. This transmittal is issued within that period."
)

ATTACHMENTS = [
    ("P22-BA-09-000-013_A_CC_ADASA.pdf", "Fabrication and Testing Dossier Index Rev A"),
    ("P22-DWG-09-005-004_C_CC_ADASA.pdf", "Piping Layout Rev C — sheets 1 to 4"),
    ("25007-ME-PI-0901_CC_ADASA.pdf", "Shop fabrication set, sheets 5 to 21"),
]

RESPONSE_SUMMARY = [
    ("P22-ET-09-008-001", "Datasheet of PLC and HMI Panel Component (Major Component)",
     "0", "25007-0068", "1 — Approved"),
    ("P22-BA-09-000-013", "Fabrication and Testing Dossier Index",
     "A", "25007-0069", "3 — To be revised"),
    ("P22-DWG-09-005-004", "Piping Layout", "C", "25007-0070", "2 — Approved as noted"),
    ("P22-DWG-09-005-007", "3D Model", "A", "25007-0070", "2 — Approved as noted"),
    ("P22-LI-09-008-006", "Datasheet of Differential Pressure Switch",
     "B", "25007-0070", "1 — Approved"),
    ("25007-ME-PI-0901-0006 to -0016", "Shop fabrication set (17 sheets)",
     "1", "not submitted", "returned — not received"),
]

DISPOSITION = [
    "Datasheet of PLC and HMI Panel Component Rev 0 — Code 1. Align the four documents "
    "carrying the other terminal catalogue number.",
    "Fabrication and Testing Dossier Index Rev A — Code 3. Re-issue as Rev B with the "
    "missing chapters and full traceability per line.",
    "Piping Layout Rev C — Code 2. Add the tie-in schedule and the battery-limit flange "
    "class at Rev 0.",
    "Shop fabrication set 25007-ME-PI-0901-0006 to -0016 — not received. Submit as a "
    "deliverable in its own right and correct the two pressure-containment items.",
    "3D Model Rev A — Code 2. Identify the file by its code and revision and reconcile its "
    "tags with the approved lists.",
    "Datasheet of Differential Pressure Switch Rev B — Code 1. Issue directly at IFC Rev 0.",
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N30 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-030-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To be revised.", {"bold": True}),
        (" Five documents across three submittals. Tally: 2 Code 1, 2 Code 2, 1 Code 3, plus "
         "one uncoded set returned as not received. The Dossier Index fixes the verdict: it "
         "omits four chapters its own governing documents require and carries no document "
         "number or revision against any of its 27 lines, so it cannot serve as the checklist "
         "ADASA uses to review the dossier. Two pressure-containment items on the shop "
         "fabrication set require correction before those spools are built.",),
    ])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for d in DISPOSITION:
        add_bullet(doc, d)
    add_para(doc, [
        ("Section 3 lists the pending observations from previous transmittals.",)])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        for p in sec["paras"]:
            add_para(doc, p)

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [("The three most serious open items:", {"bold": True})])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [("Also open: ", {"bold": True}), (PENDING_SUMMARY,)])
    add_para(doc, [("Cross-document reconciliation carried from the first subsection of "
                    "Section 2: ", {"bold": True}), (CROSS_DOC,)])
    add_para(doc, [("Review period. ", {"bold": True}), (REVIEW_PERIOD,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(doc, [("Attachment", "Document")] + ATTACHMENTS)
    add_para(doc, [(
        "All documents with open observations carry an annotated PDF, with two exceptions "
        "stated here rather than left unexplained. The two Code 1 documents require no "
        "modification and carry none. The 3D Model is a Navisworks file that cannot carry the "
        "annotation format used for drawings, so its observations are stated in full in the "
        "corresponding subsection of Section 2.",)])
    dl = doc.add_paragraph()
    dl.add_run("Download — this transmittal and the annotated PDFs: ").bold = True
    aplicar_arial_12(dl)
    add_hyperlink(dl, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Submittal", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.", {"bold": True}),
        (" The Fabrication and Testing Dossier Index fixes the verdict and is to be re-issued "
         "as Rev B. The two pressure-containment items of the shop fabrication set are to be "
         "corrected before those spools are built, and that set is to be submitted as a "
         "deliverable in its own right. Documents not appearing in this response are "
         "unaffected by this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
