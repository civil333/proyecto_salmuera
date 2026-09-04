#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_transmittal.py — TRANSMITTAL N36 (P22-TM-09-000-036-0)

Submittals 25007-0082, 25007-0083, 25007-0084 y 25007-0085 (ENTREGAS 82 a 85),
recibidas entre el 21 y el 26 de agosto de 2026. Nueve documentos.

VEREDICTO GLOBAL: 3 — To be revised. 2 Codigo 1, 5 Codigo 2, 1 Codigo 3 sobre
los OCHO documentos que se disponen.

Mapa de subsecciones:
    2.1  UHPRO Structural Design Criteria Rev 0   P22-CD-09-005-003   Code 1
    2.2  Piping Layout Rev D                      P22-DWG-09-005-004  Code 2
    2.3  3D Model Rev B                           P22-DWG-09-005-007  Code 2
    2.4  GA of SWRO System Skid Rev 0             P22-DWG-09-005-008  Code 3
    2.5  GA of Antiscalant Dosing Tank Rev C      P22-DWG-09-005-015  Code 2
    2.6  Datasheet of RO HP Feed Pump Rev E       P22-ET-09-009-002   Code 1
    2.7  Datasheet of Feed Turbocharger Rev E     P22-ET-09-009-007   Code 2
    2.8  Datasheet of Interstage Turbocharger E   P22-ET-09-009-008   Code 2

RETIRADO DEL TRANSMITTAL, decision del usuario del 26-Ago-2026: el Project
Schedule Rev B (P22-BA-09-000-001), de la misma submittal 25007-0084. Su
seguimiento se lleva por la reunion semanal de coordinacion, de modo que NO
recibe codigo de respuesta aqui y su PDF anotado no se emite. El Resumen
Ejecutivo lo declara en una linea para que BW Water no quede esperando un codigo
que no va a llegar por esta via. El paquete retirado, con la evidencia que se
verifico, sale de esta carpeta y queda junto al documento que comenta, en
ENTREGAS_BWWATER/ENTREGA 84/_cronograma_fuera_de_transmittal/.

REGLA DE ALCANCE. Los nueve documentos responden a comentarios previos, de modo
que cada uno se revisa unicamente contra la instruccion escrita del transmittal
anterior. No se introducen observaciones nuevas.

LA COLUMNA DE EMISION DEL SUBMITTAL FORM DECIDE EL CODIGO. Un Codigo 2 dice
literal "Action to issue at IFC Rev 0 — no new revision required": su condicion
vence cuando el documento se emite en Rev 0, no antes. Un documento sometido
para aprobacion (IFA) reitera la condicion en Codigo 2 con constancia de
reincidencia; uno sometido para construccion (IFC) queda en Codigo 1 o en
Codigo 3, porque sobre un Rev 0 el Codigo 2 no tiene mecanismo.
El unico IFC del lote con condiciones sin cumplir es el GA of SWRO System Skid.

LO QUE SE RECONOCE POR ESCRITO: el modelo cerro siete TAG de valvula donde el
TM N30 nombro uno; el GA del estanque antiscalante entrego integras las tres
cosas de un Codigo 3; el cronograma no reabrio la adopcion de la linea base.

FUERA DEL TRANSMITTAL A PROPOSITO: el detalle itemizado de cada observacion
vive en su CC_ADASA, no en la subseccion.


SIN numeros manuales en add_heading(); referencias por NOMBRE de seccion; cero
simbolo de seccion.
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N36 ADASA-BW_WATER.docx")

# Enlace de descarga de la carpeta del N36. Pegar el enlace publicado y
# REGENERAR. El modo de falla del N30, N31 y N32 fue verificar el enlace sobre
# el script y no sobre el texto extraido del Word: verificar SIEMPRE sobre el
# .docx emitido.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19dMoFG6j2lfmhv8nD87B2xwNe8vqKSA/Iz1GrP4ez1f-thJcQYsIuJ7I0Qfwb2sS-D7yAe18rdQ0"
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


# --- Seccion 1 -------------------------------------------------------------
VERDICT = (
    "Submittals 25007-0082 to 25007-0085, nine documents of which this transmittal "
    "disposes eight; the Project Schedule Rev B carries no code here and is followed "
    "through the weekly coordination. Tally: 3 Code 1, 5 Code 2. No document returns "
    "to revision: none is wrong in its own content, and what stays open are conditions "
    "that fall due at Rev 0."
)

DISPOSITION = [
    "UHPRO Structural Design Criteria Rev 0 — Code 1. No action.",
    "Piping Layout Rev D — Code 2. State the datum of the tie-in elevations, add the "
    "CIP connections, tag the two enclosures.",
    "3D Model Rev B — Code 2. Carry the code and revision index in the file "
    "properties; resolve the reuse of line 09-001.",
    "GA of SWRO System Skid Rev 0 — Code 1. Not held; two note references stand "
    "corrected.",
    "GA of Antiscalant Dosing Tank Rev C — Code 2. Reconcile the anchor hole against "
    "the M12 bolt; state the level mark elevation.",
    "Datasheet of RO HP Feed Pump Rev E — Code 1. Issue at Rev 0 before the Factory "
    "Acceptance Test.",
    "Datasheet of Feed Turbocharger Rev E — Code 2. Delete STYLE 77 and issue at Rev 0 "
    "before the Factory Acceptance Test.",
    "Datasheet of Interstage Turbocharger Rev E — Code 2. Delete STYLE 77 and issue at "
    "Rev 0 before the Factory Acceptance Test.",
]

FEDCO_LEAD = "The three Fedco datasheets have to close."
FEDCO = (
    " The pump and the two turbochargers (BH-09-001, SIP-09-001 and SIP-09-002) were "
    "approved at Rev D at Transmittal N11; the equipment was bought and built on that "
    "basis, is now due at the workshop, and "
    "the pump is programmed for installation inside the container within days. Their "
    "datasheets still arrive as approval revisions. Issue the three at Rev 0 for "
    "construction before the Factory Acceptance Test opens on 7 September 2026. ADASA "
    "will not keep returning approval revisions for equipment on its way to assembly."
)

SKID_LEAD = "On the GA of SWRO System Skid Rev 0, ADASA is blunt."
SKID = (
    " It is the only document here issued for construction, so its three pending note "
    "references fell due at this issue; one of the three was corrected. Note 8 still "
    "cites a code that does not exist in the project numbering, on the note governing "
    "nominal wall thickness, and the correct code is P22-ET-09-006-001, which is how "
    "the snapshot attached to defend the reply writes it. The drawing is not held; "
    "both corrections stand."
)

HOUSEKEEPING_LEAD = "Two housekeeping matters."
HOUSEKEEPING = (
    " The conditions open on the Piping Layout and the 3D Model are reiterated for the "
    "second cycle, itemised on their annotated PDFs. And four of the eight documents "
    "arrive with no consolidated comment sheet, among them the UHPRO Structural Design "
    "Criteria, which carried one at Rev B and lost it at Rev 0."
)

RETURN_DATE = (
    "Clause 37.2 gives seven working days: 1 September for 25007-0082 and 25007-0083, "
    "2 September for 25007-0084, 4 September for 25007-0085. This transmittal is "
    "issued within all four. The forms asked for return three calendar days after "
    "issue, one of them on a Saturday."
)

POINTER = (
    "The items open from earlier transmittals are listed under Pending Observations "
    "from Previous Transmittals."
)

# --- Seccion 2 -------------------------------------------------------------
S21_STATUS = (
    "Rev B was approved at Transmittal N25 with no action, so Rev 0 was read as a "
    "differential against it. Every seismic parameter, load combination, material "
    "grade, wind figure and lifting criterion is unchanged, and nothing contradicts "
    "the approved revision. Two editorial items folded into the Transmittal N25 note "
    "remain: the cover date reads 18 August against a body date of 11 August, and the "
    "duplicate table number is still there. This revision also drops the consolidated "
    "comment sheet that Rev B carried."
)
S21_ACTION_LEAD = "Action: none — accepted."
S21_ACTION = (
    " Tidy the two editorial items and restore the comment sheet at the next issue.")

S22_STATUS = (
    "Rev D removes the eleven shop fabrication drawings that Rev C carried and adds "
    "the tie-in schedule, which does not cover what was asked: none of the seven CIP "
    "lines labelled on the same sheet appears in it, and its five elevations state no "
    "datum. The flange class is still absent at the antiscalant and CIP terminations, "
    "and the sheet still shows two enclosures labelled LCP with no tag on either. "
    "Second cycle with these points open; itemised in "
    "P22-DWG-09-005-004_D_Piping_Layout_CC_ADASA.pdf."
)
S22_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new drawing revision required:")
S22_ACTION = (
    " add one row per CIP battery-limit connection and state the datum of the "
    "elevations. State the flange class of the antiscalant and CIP terminations "
    "against the approved Line List. And state whether the module carries one or two "
    "local control panels, tagging each enclosure against the approved Local Control "
    "Panel datasheet and the Single Line Diagram (OBS-01 to OBS-03 and NOTE-01 on the "
    "annotated PDF). ADASA accepts on the basis that these are annotations on existing "
    "geometry."
)

S23_STATUS = (
    "Reviewed against the object property database, as at Rev A. Most of the "
    "reconciliation is done: BH-009-002 is corrected, the seven valve tags that "
    "carried a trailing question mark are clean where only one had been named, "
    "DPS-09-002 now reads DPS-09-001, BOI-09-006 now reads BOI-09-001-6, and lines "
    "09-042, 09-044 and 09-026 match the approved Line List. Three points remain. The "
    "publication properties still declare the title V16 TALTAL and carry no revision "
    "index, so the model cannot be identified as the revision the Submittal Form "
    "declares. Line 09-001 is still used by both DA-PVC-DN100-09-001 and "
    "RD-PVC-DN15-09-001, the second of which is not in the approved Line List, and the "
    "Piping Layout Rev D carries the same number on all three of its sheets. Line "
    "09-015 has three objects left at DN100 against nineteen at DN80."
)
S23_SHEET_LEAD = "On the comment sheet reply, ADASA is explicit:"
S23_SHEET = (
    " it states that fifty-seven object tags were corrected. What was corrected are "
    "the seven valve tags above. The fifty-seven objects whose tag property is a "
    "question mark are pipe supports; none was touched and there are now seventy-two, "
    "and no pipe support carries a tag at either revision."
)
S23_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new model revision required:")
S23_ACTION = (
    " carry the code and revision index in the file properties. Resolve the reuse of "
    "line 09-001 and issue the corresponding addition to the Line List, and correct "
    "the three remaining objects on line 09-015. And either tag the pipe supports or "
    "state in writing that they will not be tagged."
)
S23_NOPDF_LEAD = "No annotated PDF accompanies this document."
S23_NOPDF = (
    " A Navisworks file cannot carry the annotation format used for drawings, so its "
    "observations are stated in full here."
)

S24_STATUS = (
    "Reviewed against the single action of Transmittal N31, which was to correct three "
    "document references in the notes block; one of the three was corrected. Note 7 "
    "now cites the approved Line List by its full code on both sheets. Note 6 was "
    "corrected on Sheet 2 and left unchanged on Sheet 1, which still cites the "
    "Instrument List at Rev D, so the same drawing refers the same instrument function "
    "matrix to two revisions. Note 8 is unchanged on both sheets and cites "
    "P22-ET-09-006-01 (one digit short of a valid code in the project numbering) on "
    "the note governing nominal wall thickness. The annex submitted to defend that "
    "reply "
    "refutes it: the snapshot writes the code as P22-ET-09-006-001 and the row below "
    "it as P22-ET-09-006-002."
)
S24_WHY_LEAD = "Why Code 1 and not Code 3."
S24_WHY = (
    " The drawing is issued for construction and ADASA does not hold it: both "
    "documents referred to remain identifiable, and neither error changes a dimension, "
    "a material, a rating or a quantity. That is the reason for the code, not an "
    "acceptance of the point."
)
S24_ACTION_LEAD = "Action: the drawing is not held. Two corrections stand:"
S24_ACTION = (
    " write the Piping Material Specification as P22-ET-09-006-001, with its revision "
    "index, in note 8 of both sheets, and align note 6 of Sheet 1 to the current "
    "revision of the Instrument List. Confirm in writing which revision of the "
    "Instrument List governs the function-versus-tag matrix of this skid."
)

S25_STATUS = (
    "Rev C closes the substance of the Code 3 of Transmittal N26: the seismic reaction "
    "forces are in note 16, the centre of gravity in note 15, and a new Detail 4 gives "
    "the M12 bolt, its load and a minimum embedment, consistent with the three anchor "
    "lugs of Detail 3. The effective working volume is in note 8 and the tag TK-09-002 "
    "is on the title block. Two items remain on the detail that was added: the anchor "
    "hole is dimensioned 14 mm and half an inch, which are not the same dimension, "
    "against an M12 bolt; and the level marking row carries its location but no size "
    "and no elevation. Itemised in "
    "P22-DWG-09-005-015_C_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf."
)
S25_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new drawing revision required:")
S25_ACTION = (
    " reconcile the two values of the anchor hole against the M12 bolt, and state the "
    "elevation of the level mark (OBS-01 and NOTE-01 on the annotated PDF). Note 16 "
    "refers the reaction forces to a calculation report without stating its code and "
    "revision; that report (P22-CD-09-005-001) and its endorsement are tracked under "
    "Pending Observations from Previous Transmittals and do not modify this drawing."
)

S26_STATUS = (
    "Rev E closes the single note open on this document since Transmittal N11. The "
    "motor manufacturer (GE) now reads the same in both data blocks and on the outline "
    "drawing, with the earlier alternative wording gone, which also answers the "
    "request to confirm the manufacturer once procurement was complete."
)
S26_ACTION_LEAD = "Action: none on the content — accepted."
S26_ACTION = (
    " Issue at Rev 0 for construction before the Factory Acceptance Test opens on 7 "
    "September 2026; the pump is bought, built and programmed for installation inside "
    "the container within days."
)

S27_STATUS = (
    "Transmittal N11 asked for the outline drawing label to be updated to Style S, to "
    "eliminate the discrepancy with STYLE 77, a coupling of a different manufacturer "
    "and a different working pressure. Rev E adds PIEDMONT STYLE S to all four "
    "connection callouts and leaves STYLE 77 on all four, so each connection names two "
    "coupling models at once, while the datasheet body specifies the process "
    "connections at Coupling 1800 psi, which is the Style S rating. Itemised in "
    "P22-ET-09-009-007_E_Datasheet_Feed_Turbocharger_CC_ADASA.pdf."
)
S27_ACTION_LEAD = (
    "Action — issue at Rev 0 for construction before the Factory Acceptance Test opens "
    "on 7 September 2026:")
S27_ACTION = (
    " delete STYLE 77 from the four connection callouts, leaving the cut groove "
    "designation and PIEDMONT STYLE S (OBS-01 on the annotated PDF). No intermediate "
    "approval revision is required and none should be issued: this equipment is built "
    "and due at the workshop."
)

S28_STATUS = (
    "The same condition as the Feed Turbocharger, unchanged in form: PIEDMONT STYLE S "
    "was added to all four connection callouts and STYLE 77 was not removed from any, "
    "while the datasheet body specifies the process connections at Coupling 1800 psi. "
    "Itemised in P22-ET-09-009-008_E_Datasheet_Interstage_Turbocharger_CC_ADASA.pdf."
)
S28_ACTION_LEAD = "Action — same as the Feed Turbocharger:"
S28_ACTION = (
    " delete STYLE 77 from the four connection callouts and issue at Rev 0 for "
    "construction before the Factory Acceptance Test opens on 7 September 2026 "
    "(OBS-01 on the annotated PDF)."
)

# --- Seccion 3 -------------------------------------------------------------
PENDING = [
    ("N30",
     "Shop fabrication set 25007-ME-PI-0901-0006 to -0016",
     "Eleven sheets stamped for construction, removed from the Piping Layout at Rev D "
     "and never submitted as a deliverable of their own with an ADASA code and "
     "revision index. Their two pressure-containment findings are unanswered: threaded "
     "austenitic instrument branches on super duplex lines rated 60 to 90 barG design, "
     "and an undeclared specification break between the super duplex and PVC systems",
     "Open, aggravated by the withdrawal without re-submission"),
    ("N25, N29, N30",
     "Fabrication and testing dossier",
     "Item 65 remains NOT DELIVERED. The index has reached Rev B; no record has "
     "followed it. It sustains items 8.3 and 8.4 of the Inspection and Testing Base "
     "Plan, on which 40 per cent of payment depends",
     "Open, overdue"),
    ("N26, N30",
     "Endorsed structural calculation report P22-CD-09-005-001",
     "It governs the anchorage figures the GA of the Antiscalant Dosing Tank Rev C has "
     "just stated in its note 16, and the foundations already built at site. It has "
     "yet to be issued with the endorsement of a professional engineer registered in "
     "Chile",
     "Open, overdue, raised again here"),
]

ALSO_OPEN_LEAD = "Also open:"
ALSO_OPEN = (
    " the three non-destructive testing procedures returned at Code 3, awaiting their "
    "Rev C; the liquid penetrant records of 7 August, examined five days before their "
    "procedure was submitted; the measurement point drawing required by row 7.8 of the "
    "Inspection and Test Plan; and the Pressure Test Record Chart as a controlled "
    "form. Open with them: the test pressure of each super duplex line, to be "
    "confirmed in writing; the re-issue of the Equipment List and of the Valve List, "
    "undertaken in writing on the 3D Model comment sheet; the Instrument List Rev E "
    "with VT-09-001 ranged at 0 to 12 mm/s rms; the six tag reconciliation of the HMI "
    "Display Screenshot Rev B; and the design pressure at the brine feed tie-in point."
)

# --- Seccion 4 -------------------------------------------------------------
ATTACHMENTS = [
    ("Piping Layout Rev D", "2",
     "P22-DWG-09-005-004_D_Piping_Layout_CC_ADASA.pdf"),
    ("GA of Antiscalant Dosing Tank Rev C", "2",
     "P22-DWG-09-005-015_C_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf"),
    ("Datasheet of Feed Turbocharger Rev E", "2",
     "P22-ET-09-009-007_E_Datasheet_Feed_Turbocharger_CC_ADASA.pdf"),
    ("Datasheet of Interstage Turbocharger Rev E", "2",
     "P22-ET-09-009-008_E_Datasheet_Interstage_Turbocharger_CC_ADASA.pdf"),
]

ATTACH_NOTE = (
    "Every document with open observations carries an annotated PDF, with one "
    "exception stated here: the 3D Model Rev B is a Navisworks file and cannot carry "
    "the annotation format used for drawings, so its observations are in its own "
    "subsection. The three Code 1 documents carry none."
)
DOWNLOAD_LEAD = "The annotated PDFs are available at the following download link:"

# --- Seccion 5 -------------------------------------------------------------
RESPONSE_SUMMARY = [
    ("P22-CD-09-005-003", "UHPRO Structural Design Criteria", "0",
     "25007-0082", "1 — Approved"),
    ("P22-DWG-09-005-004", "Piping Layout", "D",
     "25007-0083", "2 — Approved as noted"),
    ("P22-DWG-09-005-007", "3D Model", "B",
     "25007-0083", "2 — Approved as noted"),
    ("P22-DWG-09-005-008", "GA of SWRO System Skid", "0",
     "25007-0084", "1 — Approved"),
    ("P22-DWG-09-005-015", "GA of Antiscalant Dosing Tank", "C",
     "25007-0084", "2 — Approved as noted"),
    ("P22-ET-09-009-002", "Datasheet of RO HP Feed Pump", "E",
     "25007-0085", "1 — Approved"),
    ("P22-ET-09-009-007", "Datasheet of Feed Turbocharger", "E",
     "25007-0085", "2 — Approved as noted"),
    ("P22-ET-09-009-008", "Datasheet of Interstage Turbocharger", "E",
     "25007-0085", "2 — Approved as noted"),
]

CLOSING_LEAD = "Overall Transmittal Verdict: 2 — APPROVED AS NOTED."
CLOSING = (
    " No document returns to revision. Two matters stay open: the two references of "
    "the GA of SWRO System Skid, issued for construction with one of three corrected; "
    "and the issue at Rev 0 of the three Fedco datasheets, for equipment already built "
    "and about to be installed."
)


if __name__ == "__main__":
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N36 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-036-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 2 — Approved as noted.", {"bold": True}),
        (" " + VERDICT,),
    ])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for item in DISPOSITION:
        add_bullet(doc, item)
    add_para(doc, [(FEDCO_LEAD, {"bold": True}), (FEDCO,)])
    add_para(doc, [(SKID_LEAD, {"bold": True}), (SKID,)])
    add_para(doc, [(HOUSEKEEPING_LEAD, {"bold": True}), (HOUSEKEEPING,)])
    add_para(doc, [("Return date.", {"bold": True}), (" " + RETURN_DATE,)])
    add_para(doc, [(POINTER,)])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    doc.add_heading(
        "UHPRO Structural Design Criteria Rev 0 — P22-CD-09-005-003", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S21_STATUS,)])
    add_para(doc, [(S21_ACTION_LEAD, {"bold": True}), (S21_ACTION,)])

    doc.add_heading("Piping Layout Rev D — P22-DWG-09-005-004", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S22_STATUS,)])
    add_para(doc, [(S22_ACTION_LEAD, {"bold": True}), (S22_ACTION,)])

    doc.add_heading("3D Model Rev B — P22-DWG-09-005-007", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S23_STATUS,)])
    add_para(doc, [(S23_SHEET_LEAD, {"bold": True}), (S23_SHEET,)])
    add_para(doc, [(S23_ACTION_LEAD, {"bold": True}), (S23_ACTION,)])
    add_para(doc, [(S23_NOPDF_LEAD, {"bold": True}), (S23_NOPDF,)])

    doc.add_heading("GA of SWRO System Skid Rev 0 — P22-DWG-09-005-008", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S24_STATUS,)])
    add_para(doc, [(S24_WHY_LEAD, {"bold": True}), (S24_WHY,)])
    add_para(doc, [(S24_ACTION_LEAD, {"bold": True}), (S24_ACTION,)])

    doc.add_heading(
        "GA of Antiscalant Dosing Tank Rev C — P22-DWG-09-005-015", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S25_STATUS,)])
    add_para(doc, [(S25_ACTION_LEAD, {"bold": True}), (S25_ACTION,)])

    doc.add_heading(
        "Datasheet of RO HP Feed Pump Rev E — P22-ET-09-009-002", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S26_STATUS,)])
    add_para(doc, [(S26_ACTION_LEAD, {"bold": True}), (S26_ACTION,)])

    doc.add_heading(
        "Datasheet of Feed Turbocharger Rev E — P22-ET-09-009-007", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S27_STATUS,)])
    add_para(doc, [(S27_ACTION_LEAD, {"bold": True}), (S27_ACTION,)])

    doc.add_heading(
        "Datasheet of Interstage Turbocharger Rev E — P22-ET-09-009-008", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S28_STATUS,)])
    add_para(doc, [(S28_ACTION_LEAD, {"bold": True}), (S28_ACTION,)])

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_simple_table(
        doc,
        [("Origin TM", "Document", "Observation", "Status")] + PENDING)
    add_para(doc, [(ALSO_OPEN_LEAD, {"bold": True}), (ALSO_OPEN,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Code", "Annotated PDF")] + ATTACHMENTS)
    add_para(doc, [(ATTACH_NOTE,)])
    p = doc.add_paragraph()
    r = p.add_run(DOWNLOAD_LEAD + " ")
    r.bold = True
    aplicar_arial_12(p)
    add_hyperlink(p, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Submittal", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [(CLOSING_LEAD, {"bold": True}), (CLOSING,)])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")
