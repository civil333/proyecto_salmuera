#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N32 ADASA-BW_WATER.
Submittal 25007-0075 (ENTREGA 75). Fecha de emision: 12-Ago-2026.

Veredicto global: 3 - TO BE REVISED.
Tally: 2 Code 1 + 3 Code 3 + 2 documentos devueltos SIN CODIGO.

  2.1 PMI Procedure Rev 0            (P22-BA-09-000-006)  Code 1
  2.2 Visual Procedure Rev 0         (P22-BA-09-000-008)  Code 1
  2.3 HP and LP Pressure Test Rev 0  (P22-BA-09-000-010)  SIN CODIGO
  2.4 Painting Procedure Rev 0       (P22-BA-09-000-011)  SIN CODIGO
  2.5 Liquid Penetrant Rev A         (P22-BA-09-000-014)  Code 3
  2.6 Radiography Rev A              (P22-BA-09-000-015)  Code 3
  2.7 Ultrasonic Thickness Rev A     (P22-BA-09-000-016)  Code 3

DECISION DEL USUARIO (12-Ago): no se codifica 3 un documento que ADASA ya habia
dispuesto Codigo 2 y que el proveedor ya emitio a Rev 0 para construccion,
porque contradice la aprobacion propia. Los tres que no cerraron su condicion
vuelven SIN CODIGO, con sus puntos abiertos declarados integros en su
subseccion, que es el mecanismo que el TM N31 uso con la Plant Control
Philosophy Rev 0. Sin CC_ADASA: un documento sin codigo no se anota, y por eso
el detalle va integro en el texto. Los tres CC_ADASA ya generados para esos
documentos quedan como traza interna y NO se emiten.

Los tres procedimientos de ensayos no destructivos NO estan alcanzados por esa
decision: nunca estuvieron en Codigo 2, son primera emision en Rev A para
aprobacion, y ahi el Codigo 3 es el ciclo normal.

TRIAJE DEL 12-AGO contra la inspeccion de Bureau Veritas. Cada punto abierto se
contrasto con el texto literal de la observacion de ADASA y con la respuesta de
BW Water en la hoja de comentarios del propio documento:
  - PMI: contestaron las dos cosas que se les pidieron (declaracion de
    aplicabilidad al proyecto en la clausula 2.0 del frontispicio, base de
    aceptacion en la 13.4). Exigir ademas que la 8.1 y el Apendice 1 dejen de
    citar PTS era leer mas estricto que lo escrito -> Codigo 1, aseo a Seccion 3.
  - Pintura, espesor por capa: BW contesto "Actual product will update in actual
    report, attached report in this report just for sample". Leyeron "nominal
    values" como valores medidos: la peticion mezclo criterio con registro. Se
    replantea una vez con esa distincion, no se exige.
  - Pintura, color: ADASA escribio "state RAL 5012 here and in the Colour row of
    the inspection form" y contestaron "Revised as per comment" escribiendo
    RAL 5010. Sin ambiguedad -> se mantiene.
  - HP/LP, formulario del ensayo: se pidio SOLO por correo el 06-Ago y no se
    contesto (PRG-24 abierto). Va como confirmacion operativa antes del 13-Ago.
  - HP/LP, erratas: ADASA nunca las pidio; se sacan.
  - Visual, revision del formulario y registro de estructura: no se pidieron;
    van como aseo a la Seccion 3.
  - Los tres END: el bloque Action se parte en lo que bloquea al inspector y lo
    que se corrige en la misma emision, para que la Rev B salga en dias.

Los cuatro Rev 0 se juzgan SOLO por las peticiones del correo del 06-Ago-2026.
Cambios que introdujo la verificacion adversarial, todos comprobados contra la
fuente: el 1,8 mm de borrosidad geometrica es la dispensa del parrafo PW-51.1 de
ASME Seccion I para items con sello PP (power piping, B31.1), no una fila de
T-274 -citar T-274 sin sufijo-; en ASME VIII Div.1 el Apendice 6 es particulas
magneticas y el 8 es penetrantes; el rango de pared radiografiada es 6,02 a 8,56
mm (DN65/80/100 con 10% RT en la Line List), no 3,7 a 11 mm; el "Article 9" de
los frontispicios viene del NDE Plan Rev C que ADASA aprobo; y la Clausula 37.2
es un COMPROMISO de ADASA, no un derecho suyo.

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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N32 ADASA-BW_WATER.docx")

# Los tres PDF anotados que SI se emiten van por enlace de descarga.
# REEMPLAZAR por el enlace Synology real antes de emitir.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19RfyvmUCVljlSVMK7cE99bMNzRFanZn/"
    "7ZHTbwNjM-UohAkFjug-WoQAaZDT994X-gryAOZ8ZbA0"
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


# --- Resumen ejecutivo -----------------------------------------------------
DISPOSITION = [
    "PMI Procedure Rev 0 — Code 1. No action.",
    "Visual Procedure Rev 0 — Code 1. No action.",
    "HP and LP Pressure Test Procedure Rev 0 — no response code. Confirm the pressure test "
    "record before 13 August.",
    "Painting Procedure Rev 0 — no response code. The inspection form carries the wrong "
    "finish colour.",
    "Liquid Penetrant Examination Procedure Rev A — Code 3. State the ASME B31.3 "
    "acceptance criteria.",
    "Radiography Examination Procedure Rev A — Code 3. State the ASME B31.3 acceptance "
    "criteria and the geometric unsharpness limit of the code that governs this scope.",
    "Ultrasonic Thickness Procedure Rev A — Code 3. State an acceptance criterion and write "
    "the technique for the material of this module.",
]

NO_CODE = (
    "because they were approved as noted in earlier transmittals and then issued at Rev 0 "
    "for construction. ADASA does not return them to revision. One point remains open on "
    "each, and both fall due with the inspection of 13 and 14 August rather than with a "
    "revision cycle."
)

PRIORITY = (
    "The Painting Procedure inspection form was completed with RAL 5010 Gentian Blue, where "
    "Transmittal N27 asked to state RAL 5012 in the painting system and in the Colour row of "
    "the inspection form, and the comment sheet records that request as revised. RAL 5012 "
    "Luminous Blue is what the body of the same procedure and the Painting Specification "
    "(P22-ET-09-006-002) Rev C both set. Separately, the HP and LP Pressure Test Procedure "
    "still names a Pressure Test Report that no form in it produces, where row 5.2 of the "
    "Inspection and Test Plan requires a pressure against time graphic as the certificate of "
    "that hold point."
)

PT_7AUG = (
    "Inspection Request 002 lists as its second item the penetrant examination of root and "
    "capping passes on the super duplex welds, and the Liquid Penetrant Examination "
    "Procedure reaches ADASA for the first time in this submittal. Transmittal N30 stated "
    "that records produced under procedures not yet approved are not admissible into the "
    "fabrication and testing dossier. State which penetrant records exist to date and under "
    "which procedure and acceptance criteria they were evaluated."
)

WHY_NDE_LEAD = (
    "The Technical Specification (P22-ET-09-000-001-0), Section 8 - Inspections During "
    "Manufacturing, requires the non-destructive testing plan to state the acceptance "
    "criteria applicable under ASME B31.3, and the NDE Plan (P22-BA-09-000-005) Rev C "
    "approved at Transmittal N26 sets para. 341.3.2 for the super duplex high-pressure "
    "circuit. None of the three procedures does so:"
)

WHY_NDE = [
    "The Ultrasonic Thickness Procedure states no criterion at all: clause 9.0 leaves "
    "acceptance and rejection to the discretion of the client. Its technique sheet is also "
    "written for carbon steel, whose sound velocity is not that of UNS S32750, so a gauge "
    "calibrated on it reads a biased thickness.",
    "The Radiography Examination Procedure gives a list of five codes without stating which "
    "governs, and its only geometric unsharpness limit, 1.8 mm, is the dispensation of "
    "paragraph PW-51.1 of ASME Section I for items carrying the PP stamp, that is power "
    "piping to ASME B31.1. ASME B31.3 grants no such dispensation: its paragraph 344.5.1 "
    "refers radiography wholly to Section V, Article 2, where T-274 requires 0.020 in. for "
    "a wall under 2 in. The lines carrying 10 per cent radiography on the approved Line "
    "List are DN65, DN80 and DN100, between 6.02 and 8.56 mm of wall.",
    "The Liquid Penetrant Examination Procedure refers acceptance in its clause 13.0 to "
    "Appendix 6 of ASME Section VIII Div. 1, which is the appendix for magnetic particle "
    "examination, not for the method this procedure covers.",
]

WHY_NDE_TAIL = (
    "Each of the three actions in Section 2 separates what has to change before the "
    "procedure can be used from what is to be tidied at the same issue, so that a Rev B can "
    "be turned around without a full cycle."
)

REVISION_CONTROL = (
    "Two physically different documents carry the identification Rev 0 in each of the four "
    "re-issued procedures, dated 05-08-2026 and 11-08-2026. State which one governs, and "
    "confirm that the third-party inspector and the shop work against that revision at each "
    "attendance. The point is not academic: the two revisions of the Painting Procedure "
    "state different anchor profile criteria, 40 to 75 micrometres against 50 to 80."
)

REVIEW_PERIOD = (
    "Clause 37.2 of the Special Administrative Conditions (BAE 12803) records ADASA's "
    "undertaking to review and issue comments within seven working days of formal and "
    "complete receipt, which for this submittal falls on Friday 21 August. This transmittal "
    "is issued within that period, and not on the 15 August stated on the Submittal Form."
)

# --- Seccion 2 -------------------------------------------------------------
SECTIONS = [
    dict(
        heading="PMI Procedure Rev 0 — P22-BA-09-000-006",
        code="Response Code: 1 — Approved",
        paras=[
            [("Status.", {"bold": True}),
             (" The two points ADASA raised are answered. The project applicability "
              "requested at Transmittal N20 is now declared in the scope of the cover "
              "section, which states that ten per cent of the super duplex high-pressure "
              "piping components will be tested and witnessed by ADASA, and the bolt and nut "
              "sampling of Appendix 1 rose from five to ten per cent per lot for piping. The "
              "acceptance basis asked for on 6 August is stated in the new clause 13.4, on "
              "conformity to Super Duplex stainless steel, and the two clauses that referred "
              "approval and rejection to third-party refinery standards were deleted.",)],
            [("Action: none — accepted; issue directly at IFC Rev 0.", {"bold": True}),
             (" Two items of housekeeping are tracked in Section 3 for the next natural "
              "issue of this procedure.",)],
        ],
    ),
    dict(
        heading="Visual Procedure Rev 0 — P22-BA-09-000-008",
        code="Response Code: 1 — Approved",
        paras=[
            [("Status.", {"bold": True}),
             (" The point raised on 6 August is closed. Clause 5.8.1 now identifies the "
              "record as form AQ-QAM-F020, Piping Fabrication Inspection Report (Steel), and "
              "the form is included in the procedure at Rev. 0. It carries the fit-up, "
              "dimensional, visual and welding inspection columns with the result and the "
              "report number, which is the visual report that row 3.2 of the Inspection and "
              "Test Plan requires at a witness point for the super duplex high-pressure "
              "welds.",)],
            [("Action: none — accepted; issue directly at IFC Rev 0.", {"bold": True}),
             (" One item of housekeeping is tracked in Section 3 for the next natural issue "
              "of this procedure.",)],
        ],
    ),
    dict(
        heading="HP and LP Pressure Test Procedure Rev 0 — P22-BA-09-000-010",
        code="Response Code: none issued",
        paras=[
            [("Status.", {"bold": True}),
             (" The document was approved as noted at Transmittal N29 and issued at Rev 0 "
              "for construction, so no response code is stated. The point raised on 6 August "
              "is closed: clauses 5.5.2 and 5.6.3 now test to the ASME B31.3 2024 edition "
              "instead of to the latest edition, so the edition is fixed for the tests "
              "themselves as well as in the reference section, and no addenda exist against "
              "either publication cited. One point remains open, and it falls due with the "
              "test itself: clause 5.8.1 refers to a Pressure Test Report that is not part "
              "of this submittal and that no controlled form in the procedure produces, "
              "while row 5.2 of the Inspection and Test Plan requires a pressure against "
              "time graphic as the certificate of a hold point. The high-pressure test is "
              "scheduled for 13 and 14 August.",)],
            [("Action — confirm before 13 August, and close at the next issue of this "
              "document:", {"bold": True}),
             (" identify the form on which the high-pressure test is recorded, by number and "
              "revision, and make it available to the inspector for that attendance; then "
              "attach it to the procedure at its next issue. No annotated PDF accompanies "
              "this document, because it carries no response code; the point is stated in "
              "full here.",)],
        ],
    ),
    dict(
        heading="Painting Procedure Rev 0 — P22-BA-09-000-011",
        code="Response Code: none issued",
        paras=[
            [("Status.", {"bold": True}),
             (" The document was approved as noted at Transmittal N27 and issued at Rev 0 "
              "for construction, so no response code is stated. Two of the three conditions "
              "of that approval are met: the anchor profile now reads 50 to 80 micrometres "
              "throughout, and the product for each coat was written into the inspection "
              "form. The third was answered with a different value from the one requested. "
              "Transmittal N27 asked to state RAL 5012 in the painting system and in the "
              "Colour row of the inspection form; the comment sheet records that as revised, "
              "and the Colour row reads RAL 5010 Gentian Blue. Page 9 of the same procedure "
              "specifies RAL 5012 Luminous Blue for the third coat, and the Painting "
              "Specification (P22-ET-09-006-002) Rev C, approved at Code 1, sets RAL 5012 "
              "Luminous Blue for the frame support inside the container. RAL 5010 appears in "
              "no row of that specification. The painting preparation inspection is on 13 "
              "and 14 August.",)],
            [("Action — correct before the finish coat is applied, and close at the next "
              "issue of this document:", {"bold": True}),
             (" state RAL 5012 Luminous Blue in the Colour row of the inspection form, "
              "consistent with the body of the procedure and with the approved Painting "
              "Specification. On the nominal thickness per coat, ADASA notes the reply that "
              "the attached form is a sample and that actual values are entered in the "
              "actual report, and restates the request in those terms: what belongs printed "
              "on the blank form is the specified thickness of each coat, eighty, two "
              "hundred and seventy-five micrometres, as the criterion against which the "
              "measured values are compared; the measured values remain to be filled in at "
              "the time of inspection. No annotated PDF accompanies this document, because "
              "it carries no response code; the points are stated in full here.",)],
        ],
    ),
    dict(
        heading="Liquid Penetrant Examination Procedure Rev A — P22-BA-09-000-014",
        code="Response Code: 3 — To be revised",
        paras=[
            [("Status.", {"bold": True}),
             (" First issue, submitted in response to the request made at Transmittal N30. "
              "The technique is sound and the personnel qualification basis matches Section "
              "2.0 of the approved NDE Plan. The acceptance criteria are not those of this "
              "scope, and the document states two different ones: clause 13.0 refers to "
              "Appendix 6 of ASME Section VIII Div. 1, which is the appendix for magnetic "
              "particle examination, and the report form to Appendix 8, which is the "
              "penetrant appendix of the same pressure vessel code. The Technical "
              "Specification, Section 8, and the approved NDE Plan both set ASME B31.3 para. "
              "341.3.2 for this circuit. Itemised in "
              "P22-BA-09-000-014_A_Liquid_Penetrant_Procedure_CC_ADASA.pdf.",)],
            [("Action — re-issue as Rev B.", {"bold": True}),
             (" Before this procedure is used: state ASME B31.3 para. 341.3.2 and Table "
              "341.3.2 as the acceptance criteria for the super duplex high-pressure "
              "circuit, in clause 13.0 and on the report form, replacing the reference to "
              "Appendix 6, which does not correspond to this examination method. To be "
              "tidied at the same issue, without holding the re-issue: the purpose clause of "
              "the cover section and the document number, both of which describe this "
              "document as a positive material identification procedure; the revision index "
              "of the attached procedure, whose header alternates between Rev.00 and Rev.01; "
              "and the report form, which is to be issued blank, since it carries the job "
              "number, batch numbers and the examination result of a different contract "
              "(OBS-01 to OBS-04 and NOTE-01 on the annotated PDF).",)],
        ],
    ),
    dict(
        heading="Radiography Examination Procedure Rev A — P22-BA-09-000-015",
        code="Response Code: 3 — To be revised",
        paras=[
            [("Status.", {"bold": True}),
             (" First issue, submitted in response to the request made at Transmittal N30. "
              "The technique, the identification system, the film densities and the "
              "qualification of the radiographers, registered with the Malaysian atomic "
              "licensing board, are all adequate, and the reference clause of the attached "
              "procedure correctly fixes the 2025 edition of Article 2. Two items are not "
              "adequate: the acceptance criteria are given as a list of five codes without "
              "stating which governs this project, and the only geometric unsharpness limit "
              "stated belongs to a code regime that does not govern this module. Itemised in "
              "P22-BA-09-000-015_A_Radiography_Procedure_CC_ADASA.pdf.",)],
            [("Action — re-issue as Rev B.", {"bold": True}),
             (" Before this procedure is used: state ASME B31.3 para. 341.3.2 and Table "
              "341.3.2 as the acceptance criteria in clause 23.0, in place of the list of "
              "five codes; and replace the 1.8 mm of clause 12.1, which is the dispensation "
              "of paragraph PW-51.1 of ASME Section I for items carrying the PP stamp, with "
              "the limit that T-274 of ASME Section V, Article 2 requires for the wall "
              "radiographed here, 0.020 in. for a wall under 2 in. ASME B31.3 grants no such "
              "dispensation, since its paragraph 344.5.1 refers radiography wholly to that "
              "Article, and the lines carrying ten per cent radiography on the approved Line "
              "List are DN65, DN80 and DN100, between 6.02 and 8.56 mm of wall. To be tidied "
              "at the same issue, without holding the re-issue: declare the material and the "
              "thickness range radiographed on this project; correct the purpose clause of "
              "the cover section and the document number; and renumber the sub-clauses, "
              "which run one number behind their own headings throughout the body (OBS-01 to "
              "OBS-04 and NOTE-01 on the annotated PDF).",)],
        ],
    ),
    dict(
        heading="Ultrasonic Thickness Procedure Rev A — P22-BA-09-000-016",
        code="Response Code: 3 — To be revised",
        paras=[
            [("Status.", {"bold": True}),
             (" First issue, submitted in response to the request made at Transmittal N30. "
              "The document has no acceptance criterion: clause 9.0 leaves acceptance and "
              "rejection to the discretion of the client, where the approved NDE Plan sets "
              "the measured thickness against the minimum required thickness of the "
              "applicable design code. Its technique sheet is written for carbon steel, its "
              "reference codes are the in-service inspection codes API 510, 570 and 653, and "
              "the report form belongs to a different contract. Itemised in "
              "P22-BA-09-000-016_A_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf.",)],
            [("Action — re-issue as Rev B.", {"bold": True}),
             (" Before this procedure is used: state in clause 9.0 the criterion the "
              "approved NDE Plan sets, that the measured thickness shall be equal to or "
              "greater than the minimum required thickness of the applicable design code and "
              "the engineering calculation; and write the technique sheet for ASTM A790 UNS "
              "S32750, with the sound velocity and the calibration block for that material, "
              "since a gauge calibrated on carbon steel reads a biased thickness. "
              "Separately, and with its own date before the baseline measurement is taken, "
              "submit the measurement point drawing that row 7.8 of the Inspection and Test "
              "Plan requires alongside this procedure, or state in the procedure how the "
              "points are defined. To be tidied at the same issue, without holding the "
              "re-issue: the reference edition of ASME Section V, which the attached "
              "procedure states as 2023 and the cover section as 2025; the designation of "
              "the thickness measurement standard, cited as ASME E 797 where Section V "
              "adopts it as SE-797; the report form, which is to be issued blank; and the "
              "purpose clause of the cover section and the document number, both of which "
              "describe this document as a positive material identification procedure "
              "(OBS-01 to OBS-05 and NOTE-01 on the annotated PDF).",)],
        ],
    ),
]

PENDING_OPEN = [
    ("TM N19",
     "Fabrication and testing dossier",
     "The dossier required by the Technical Specification, Section 7, has not been "
     "delivered; it gates items 8.3 and 8.4 of the Inspection and Testing Base Plan",
     "OPEN — the index arrived at Transmittal N30 and the dossier itself did not"),
    ("TM N30",
     "Shop fabrication set 25007-ME-PI-0901-0006 to -0016",
     "Returned as not received; threaded austenitic branch connections on super duplex "
     "lines, and the super duplex to PVC boundary without a specification break",
     "OPEN — confirm in writing whether any of these spools has already been fabricated, "
     "before the pressure test of 13 and 14 August"),
    ("TM N31",
     "Plant Control Philosophy Rev 0",
     "The temperature sensor mapping remains reversed on the CIP pump against the "
     "Instrument List Rev E, and holds the Factory Acceptance Test Procedure sign-off on "
     "motor temperature protection",
     "OPEN — to be closed at the next issue of that document"),
]

HOUSEKEEPING = (
    "in the PMI Procedure, reconcile clauses 13.1 and 13.2 with the new 13.4 so that the "
    "acceptance basis is stated once, write the designation as UNS S32750, and align clause "
    "8.1 and the heading of Appendix 1 with the extent the cover section already declares; "
    "in the Visual Procedure, state in clause 5.8.1 the revision of form AQ-QAM-F020, which "
    "the form itself carries, and name the record for the structural welds, which the "
    "procedure and the NDE Plan both cover at one hundred per cent visual."
)

PENDING_SUMMARY = (
    "the Equipment Layout, which ADASA holds at Rev C, with the re-issue planned there for "
    "29 July; the GA of the Antiscalant Dosing Tank, held at Rev B, planned for 30 July; "
    "and the Instrument Location Layout, held at Rev C, planned for 2 August. None of the "
    "three has been submitted. The Fabrication and Testing Dossier Index Rev A remains at "
    "Code 3 from Transmittal N30, to be re-issued as Rev B."
)

ATTACHMENTS = [
    ("Liquid Penetrant Examination Procedure Rev A (Code 3)",
     "P22-BA-09-000-014_A_Liquid_Penetrant_Procedure_CC_ADASA.pdf"),
    ("Radiography Examination Procedure Rev A (Code 3)",
     "P22-BA-09-000-015_A_Radiography_Procedure_CC_ADASA.pdf"),
    ("Ultrasonic Thickness Procedure Rev A (Code 3)",
     "P22-BA-09-000-016_A_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf"),
]

RESPONSE_SUMMARY = [
    ("P22-BA-09-000-006", "PMI Procedure", "0", "25007-0075", "1 — Approved"),
    ("P22-BA-09-000-008", "Visual Procedure", "0", "25007-0075", "1 — Approved"),
    ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "0", "25007-0075",
     "No response code issued"),
    ("P22-BA-09-000-011", "Painting Procedure", "0", "25007-0075",
     "No response code issued"),
    ("P22-BA-09-000-014", "Liquid Penetrant Examination Procedure", "A", "25007-0075",
     "3 — To be revised"),
    ("P22-BA-09-000-015", "Radiography Examination Procedure", "A", "25007-0075",
     "3 — To be revised"),
    ("P22-BA-09-000-016", "Ultrasonic Thickness Procedure", "A", "25007-0075",
     "3 — To be revised"),
]


def main() -> None:
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en marcador de posicion. "
              "Reemplazar DOWNLOAD_LINK antes de emitir.")

    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N32 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-032-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To be revised.", {"bold": True}),
        (" This transmittal responds to BW Water submittal ",),
        ("25007-0075", {"bold": True}),
        (", received on 12 August with seven documents. Tally: 2 Code 1, 3 Code 3, and two "
         "documents returned without a response code. The four procedures re-issued at Rev 0 "
         "are reviewed only against the points ADASA raised on 6 August; the three "
         "non-destructive testing procedures are first issues and are reviewed in full.",),
    ])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for d in DISPOSITION:
        add_bullet(doc, d)
    add_para(doc, [
        ("Two documents carry no response code ", {"bold": True}), (NO_CODE,)])
    add_para(doc, [
        ("Act on this first, before 13 August. ", {"bold": True}), (PRIORITY,)])
    add_para(doc, [
        ("Penetrant testing was carried out on 7 August under a procedure submitted five "
         "days later. ", {"bold": True}), (PT_7AUG,)])
    add_para(doc, [
        ("Why Code 3 — the three non-destructive testing procedures. ", {"bold": True}),
        (WHY_NDE_LEAD,)])
    for b in WHY_NDE:
        add_bullet(doc, b)
    add_para(doc, [(WHY_NDE_TAIL,)])
    add_para(doc, [("Revision control. ", {"bold": True}), (REVISION_CONTROL,)])
    add_para(doc, [("Review period. ", {"bold": True}), (REVIEW_PERIOD,)])
    add_para(doc, [
        ("Section 3 lists the pending observations from previous transmittals.",)])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        for p in sec["paras"]:
            add_para(doc, p)
        if sec.get("bullets"):
            add_para(doc, [(sec["bullets_lead"], {"bold": True})])
            for b in sec["bullets"]:
                add_bullet(doc, b)
        if sec.get("closing"):
            add_para(doc, sec["closing"])

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [("The three most serious open items:", {"bold": True})])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [
        ("Housekeeping on the two documents accepted above, for the next natural issue of "
         "each and not as a condition: ", {"bold": True}), (HOUSEKEEPING,)])
    add_para(doc, [
        ("Also open, and overdue against BW Water's own Document and Drawing Status Report "
         "of 20 July: ", {"bold": True}),
        (PENDING_SUMMARY,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(doc, [("Document", "Annotated PDF")] + ATTACHMENTS)
    add_para(doc, [(
        "All documents with a response code and open observations carry an annotated PDF, "
        "with four exceptions stated here rather than left unexplained. The PMI Procedure "
        "and the Visual Procedure are Code 1 — Approved and therefore carry none. The HP and "
        "LP Pressure Test Procedure and the Painting Procedure carry none because they are "
        "returned without a response code; their open points are stated in full in Section "
        "2.",)])
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
        (" The three non-destructive testing procedures are to be re-issued as Rev B, with "
         "the items marked as blocking corrected before the procedures are used; records "
         "produced under them before they are approved are not admissible into the "
         "fabrication and testing dossier. The PMI Procedure and the Visual Procedure issue "
         "directly at IFC Rev 0. The two documents returned without a response code carry "
         "one open point each, both to be confirmed before the inspection of 13 and 14 "
         "August and closed at the next issue of each document. Documents not appearing in "
         "this response are unaffected by this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
