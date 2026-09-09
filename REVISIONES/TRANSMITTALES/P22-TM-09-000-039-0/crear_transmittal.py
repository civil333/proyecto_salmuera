#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_transmittal.py — Transmittal N39 (P22-TM-09-000-039-0)

Responde los submittals 25007-0091 (ENTREGA 91, emitido 4-Sep-2026) y
25007-0092 (ENTREGA 92, emitido 8-Sep-2026). TRES documentos.

VEREDICTO GLOBAL: 2 — Approved as noted. 1 Codigo 1 y 2 Codigo 2. CERO Codigo 3.

Mapa de subsecciones:
    2.1  Valve List Rev E                       P22-LI-09-005-002   Code 2
    2.2  GA of Antiscalant Dosing Tank Rev D    P22-DWG-09-005-015  Code 2
    2.3  Radiography Examination Procedure Rev 0 P22-BA-09-000-015  Code 1

================================================================================
REGLA DE ALCANCE — SOLO SE VERIFICA EL CIERRE DE LO PEDIDO

Los tres responden a comentarios previos, de modo que el universo de la revision
es la lista de lo exigido y nada mas. No se abren observaciones nuevas. El estado
es binario y cada cierre exige cita del cuerpo del documento: la respuesta de la
hoja de comentarios no cierra nada por si sola.

El procedimiento de radiografia llega en Rev 0 y sobre un Rev 0 solo caben
Codigo 1 o Codigo 3.

Lo que la revision encontro fuera de ese universo NO se convierte en observacion.
Queda en _ANALISIS_N39.md con la razon de por que no se emite.

================================================================================
DECISION DEL USUARIO, tomada antes de redactar

  - La tension de los actuadores de las trece valvulas motorizadas pasa de
    380/220 VAC a 230 VAC en la Rev E sin declararse, y el Electrical Load List
    Rev 0 dice 220 V. NO se emite: ADASA entrega en el gabinete principal a 380 V
    y la transformacion y distribucion interna del modulo es alcance de BW Water.
  - El GA llega como Rev D cuando el N36 pidio Rev 0. Se codifica igual, con
    constancia de que la revision intermedia no se requirio. Precedente del N34.

================================================================================
AVISOS DUROS

  - SIN cifras de multa y SIN invocar el umbral de atraso.
  - SIN codigos internos de seguimiento, sin el asesor interno, sin el saldo de
    jornadas del tercero inspector.
  - SIN numeros manuales en add_heading(): el template numera solo.
  - Referencias por NOMBRE de seccion; cero simbolo de seccion.
  - El enlace de descarga se verifica SIEMPRE sobre el .docx emitido, nunca sobre
    este script. Es el modo de falla del N30, N31, N32 y N38.

Fuente unica del contenido: P22-TM-09-000-039-0_TRANSMITTAL.md
"""
import os
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
    set_repeat_table_header,
)
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.opc.constants import RELATIONSHIP_TYPE as RT  # noqa: E402

from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N39 ADASA-BW_WATER.docx")

# Las cifras de la Seccion 3 NO se escriben a mano: salen del auditor, que
# clasifica los 113 items del Master Deliverable Register cruzandolo con los
# formularios de submittal y con el cajetin de cada PDF. Asi el transmittal y su
# correo de cobertura no pueden discrepar.
sys.path.insert(0, os.path.abspath(os.path.join(
    SCRIPT_DIR, "..", "..", "EVALUACIONES")))
from auditar_documentos_bw import auditar, leer_ddsr, separar  # noqa: E402

# Enlace de descarga de la carpeta COMENTARIOS del N39.
# Publicar la carpeta en Synology, pegar el enlace aqui y REGENERAR.
# VERIFICAR sobre el .docx y el .pdf emitidos, no sobre este script.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19ouwrb8KTtFJ7qFvEgPnwAIYi16Cd8a/ZiFTRPVQi9mpG630Th28RAvqLfORa14o-o7ngVeAgfg0"
)


# --------------------------------------------------------------------- helpers
def add_hyperlink(paragraph, url, text):
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    for tag, val in (("w:rFonts", None), ("w:sz", "24"), ("w:color", "0563C1")):
        el = OxmlElement(tag)
        if tag == "w:rFonts":
            el.set(qn("w:ascii"), "Arial")
            el.set(qn("w:hAnsi"), "Arial")
        else:
            el.set(qn("w:val"), val)
        rPr.append(el)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)
    return paragraph


def add_para(doc, runs):
    p = doc.add_paragraph()
    for item in runs:
        texto = item[0]
        fmt = item[1] if len(item) > 1 else {}
        r = p.add_run(texto)
        if fmt.get("bold"):
            r.bold = True
    return aplicar_arial_12(p)


def add_bullet(doc, text):
    return _add_bullet_native(doc, text, size=11, space_after_pt=12)


def add_quote(doc, texto):
    """Cita literal del proveedor: sangrada y en cursiva, como en el correo."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    r = p.add_run(texto)
    r.italic = True
    for run in p.runs:
        run.font.name = "Arial"
        run.font.size = Pt(10)
    return p


def _fijar_anchos(tabla, anchos):
    """Fija el ancho de columna en pulgadas.

    Setear cell.width NO basta: quien manda es el w:tblGrid del XML, que la skill
    ya escribio con su reparto proporcional, y el layout por defecto deja que Word
    recalcule por contenido. Hay que reescribir el grid Y declarar layout fijo.
    """
    tbl = tabla._tbl
    layout = tbl.tblPr.find(qn("w:tblLayout"))
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tbl.tblPr.append(layout)
    layout.set(qn("w:type"), "fixed")
    grid = tbl.find(qn("w:tblGrid"))
    for col, ancho in zip(grid.findall(qn("w:gridCol")), anchos):
        col.set(qn("w:w"), str(int(ancho * 1440)))   # twips
    for row in tabla.rows:
        for celda, ancho in zip(row.cells, anchos):
            celda.width = Inches(ancho)


def _no_partir_filas(tabla):
    """Impide que una fila se corte entre paginas.

    Sin esto la fila que cae en el borde se dibuja a medias y deja una linea
    vacia al empezar la pagina siguiente. Es la misma correccion que el conversor
    de la skill aplica a las filas del cajetin.
    """
    for row in tabla.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def add_audit_table(doc, headers, filas, anchos=None, size=8):
    """Tabla de la Seccion 3, sobre el helper de la skill.

    El estilo Table Grid NO existe en Template_ADASA.docx: la skill dibuja los
    bordes a mano, de modo que la tabla se arma con add_simple_table.

    ANCHOS A MANO. El reparto proporcional de la skill mide el largo del texto, y
    con una columna de condiciones de cien caracteres deja la de titulo tan
    angosta que parte palabras por la mitad y estira las filas a cinco lineas. Se
    pasan en pulgadas y suman 6,5, que es el ancho util de la caja.

    La fuente baja a 8 puntos y el encabezado se repite, porque la Tabla 1 lleva
    25 filas y cruza de pagina.
    """
    t = add_simple_table(doc, [tuple(headers)] + [tuple(f) for f in filas])
    set_repeat_table_header(t.rows[0])
    _no_partir_filas(t)
    if anchos:
        _fijar_anchos(t, anchos)
    for row in t.rows:
        for celda in row.cells:
            for para in celda.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)
    return t


# ------------------------------------------------------------------ SECCION 1
VERDICT = (
    "Submittals 25007-0091 and 25007-0092, three documents. Tally: 1 Code 1, "
    "2 Code 2, no Code 3 and no Code 4. No document returns to revision."
)

SCOPE_LEAD = ("All three are re-issues, and ADASA has reviewed each one only against "
              "the comments it raised before.")
SCOPE = (
    " Two of the three carry one open point each, and both are incorporated when the "
    "document is issued at Revision 0."
)

DISPOSITION_LEAD = "Disposition at a glance:"
DISPOSITION = [
    ("Valve List Rev E — Code 2.",
     " Declare the material of the valve on the CIP pump suction line against the "
     "approved Line List."),
    ("GA of Antiscalant Dosing Tank Rev D — Code 2.",
     " State the size and the elevation of the level marking row."),
    ("Radiography Examination Procedure Rev 0 — Code 1.",
     " State the document number of the procedure when the file is next touched."),
]

WHY_LEAD = "Why Code 2 — Valve List Rev E and GA of Antiscalant Dosing Tank Rev D:"
WHY = [
    "The CIP pump suction line CP-SS316-DN150-09-022 is 316L stainless steel on the Line "
    "List Rev 1 approved at Transmittal N38, and VM-09-065, the only DN150 valve of that "
    "circuit, is still listed with a PVC body, PVC trim and PVC disc. The valve is bought "
    "against this list.",
    "The LEVEL MARKING row of the nozzle specification table carries a dash in SIZE and a "
    "dash in ELEVATION, unchanged from Rev C, so the 0.27 cubic metre working volume of "
    "note 8 has no mark on the tank that materialises it.",
]

REV0_POINTER_LEAD = ("Beyond these three documents, Section 3 sets out the "
                     "engineering that ADASA has approved and BW Water has not "
                     "issued for construction:")
REV0_POINTER = (
    " {sin_emitir} of the {n_ing} engineering documents, {n_a} of them without a "
    "single open observation, to be issued at Revision 0 by Friday 11 September."
)
POINTER = "Section 4 lists the pending observations from previous transmittals."

# ------------------------------------------------------------------ SECCION 2
S21_TITLE = "Valve List Rev E — P22-LI-09-005-002"
S21_CODE = "Response Code: 2 — Approved as noted"
S21_STATUS = (
    "The re-issue was undertaken by BW Water for three changes, and two of them are done. "
    "The four valve tags absent from the approved lists are in: VM-09-131, VM-09-132 and "
    "VM-09-133 as manual valves on the first-stage reject, and VRP-09-001 as the "
    "self-actuated pressure regulating valve that replaces the orifice plate at "
    "CIT-09-004. All four are on the P&ID Rev 0. ADASA also records an improvement that "
    "was not asked for: VM-09-015 leaves the list, and that tag is not on the P&ID Rev 0 "
    "either. What is not done is the third change. The CIP pump suction line "
    "CP-SS316-DN150-09-022 is 316L stainless steel on the Line List Rev 1 approved at "
    "Transmittal N38, and the valve on that line, VM-09-065, is still listed in PVC with "
    "ANSI 150 lug ends. Itemised in P22-LI-09-005-002_E_Valve_List_CC_ADASA.pdf."
)
S21_ACTION_LEAD = "Action to issue at IFC Rev 0 — no new revision required:"
S21_ACTION = (
    " state the body, trim and seat material of VM-09-065 against the CIP pump suction "
    "line as the approved Line List defines it, and its end connection and rating "
    "(OBS-01 on the annotated PDF). ADASA accepts the document on the basis that this is "
    "incorporated at Rev 0."
)

S22_TITLE = "GA of Antiscalant Dosing Tank Rev D — P22-DWG-09-005-015"
S22_CODE = "Response Code: 2 — Approved as noted"
S22_STATUS = (
    "Of the two points that held this drawing at Code 2, one closes. The anchor hole is "
    "now labelled 14 mm and 35/64 inch, which are the same dimension, and both accept the "
    "M12 bolt declared in the same detail; at Rev C the pair read 14 mm and half an inch, "
    "which are not. The second point does not close. The nozzle specification table still "
    "carries the LEVEL MARKING row with a dash in SIZE and a dash in ELEVATION, unchanged "
    "from Rev C, so there is still no mark on the tank that materialises the 0.27 cubic "
    "metre working volume declared in note 8. The comment sheet of this revision answers "
    "that point with \"Level mark added with dimensions\". ADASA notes that this revision "
    "was not required: Transmittal N36 asked for the issue at Rev 0 without an "
    "intermediate approval revision. Itemised in "
    "P22-DWG-09-005-015_D_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf."
)
S22_ACTION_LEAD = "Action to issue at IFC Rev 0 — no new drawing revision required:"
S22_ACTION = (
    " state the size and the elevation of the level marking row, the elevation being the "
    "one that corresponds to the effective working volume of note 8 (OBS-01 on the "
    "annotated PDF). ADASA accepts the drawing on that basis. The reaction forces of note "
    "16 refer to a calculation report whose endorsement is tracked under Pending "
    "Observations from Previous Transmittals and does not modify this drawing."
)

S23_TITLE = "Radiography Examination Procedure Rev 0 — P22-BA-09-000-015"
S23_CODE = "Response Code: 1 — Approved"
S23_STATUS = (
    "The point that held this procedure at Code 2 is closed. The scope now reads the "
    "radiographic testing of duplex S32750 in walls of 6.02 to 8.56 mm with an Iridium "
    "192 source, which is the material and the range actually radiographed on this "
    "module, and from which the technique, the source size and the image quality "
    "indicator all follow. The two cross-references left behind by the renumbering are "
    "repointed, clause 11.6 to T-277.2 and clause 19.4 to T-282.1, and the comment sheet "
    "carries one row per comment for the first time. One housekeeping item remains: the "
    "cover reads DOC NO: RT PROV-PROC-RT-001, where the prefix changed and the number did "
    "not, and the procedure is still not identified by its own document number."
)
S23_ACTION_LEAD = "Action: none on this document — accepted; issue directly at IFC Rev 0."
S23_ACTION = (
    " Related item tracked in Section 4: the document number of this procedure, to be "
    "stated as P22-BA-09-000-015 when the file is next touched, together with the issue "
    "status, which the document does not declare anywhere."
)

SUBSECCIONES = [
    (S21_TITLE, S21_CODE, S21_STATUS, S21_ACTION_LEAD, S21_ACTION),
    (S22_TITLE, S22_CODE, S22_STATUS, S22_ACTION_LEAD, S22_ACTION),
    (S23_TITLE, S23_CODE, S23_STATUS, S23_ACTION_LEAD, S23_ACTION),
]

# ------------------------------------------------------------------ SECCION 3
# Emision para construccion de la ingenieria aprobada. Las filas de las cuatro
# tablas las produce el auditor; lo que vive aqui es la redaccion en ingles: la
# condicion abierta de cada Codigo 2, condensada a una clausula desde la columna
# Action Required del registro, y los titulos que el registro guarda en espanol.
CONDICIONES = {
    "P22-CD-09-009-001": "Complete the specific energy consumption calculation and "
                         "verify the recovery rate",
    "P22-ET-09-009-003": "Motor compatibility with the direct-on-line start",
    "P22-ET-09-009-010": "Minor datasheet notes",
    "P22-CD-09-005-001": "The calculation is accepted; the PDF is a duplicated "
                         "concatenation and the comment sheet omits ADASA's comment text",
    "P22-DWG-09-005-001": "Total weight of the modified container, and the make-up of "
                          "the RO skid operating weight, where the frame is in no row",
    "P22-DWG-09-005-004": "Tie-in schedule covers no CIP line and states no datum; "
                          "flange class missing at the antiscalant and CIP terminations; "
                          "two enclosures labelled LCP with no tag",
    "P22-DWG-09-005-011": "The per-bolt vertical reaction is twice the total force "
                          "divided by the ten bolts",
    "P22-DWG-09-005-014": "Nozzle schedule disagrees with the CIP Tank datasheet on the "
                          "top opening and on two nozzles",
    "P22-DWG-09-005-015": "Anchor hole dimensioned 14 mm and half an inch for an M12 "
                          "bolt; level marking row without size or elevation",
    "P22-CD-09-008-002": "CIP heater running has no terminal on any digital input sheet; "
                         "the bill of material still lists operator terminal "
                         "2711P-T10C21D8S",
    "P22-DWG-09-008-001": "The revision block repeats one description on its four rows "
                          "and the Rev C row was overwritten",
    "P22-LI-09-008-016": "PIT-09-003 and PIT-09-005 are crossed between the first and "
                         "second stage screens",
    "P22-DWG-09-005-007": "Fifty-seven pipe support tags declared corrected were not "
                          "touched; they are now seventy-two",
    "P22-BA-09-000-001": "Certification basis of the RO pressure vessels and the vessel "
                         "pressure test as a dated activity",
    "P22-BA-09-000-003": "Inspection matrix and FAT scope against the PIE Base",
    "P22-BA-09-000-007": "The super duplex PQR coupon qualifies to 5.54 mm against a WPS "
                         "declared to 14.02 mm",
    "P22-BA-09-000-009": "Vessel test scope and the waiver certification basis",
    "P22-BA-09-000-015": "Acceptance criterion of ASME B31.3 in the procedure clause",
    "P22-BA-09-000-016": "Cite Article 5, write the reference designations in full and "
                         "state the sound velocity",
    "P22-PP-09-000-001": "Submit the procedure separate from the record and close the "
                         "eight category A punch list items",
}

# Los diez datasheets de instrumentos comparten fecha de aprobacion y accion, de modo
# que van agrupados en una fila. El rango de codigos mantiene la trazabilidad.
AGRUPAR = {"P22-LI-09-008-005", "P22-LI-09-008-006", "P22-LI-09-008-007",
           "P22-LI-09-008-008", "P22-LI-09-008-009", "P22-LI-09-008-010",
           "P22-LI-09-008-011", "P22-LI-09-008-012", "P22-LI-09-008-013",
           "P22-LI-09-008-014"}

# El Project Schedule se retiro del ciclo de transmittals en el N36 y su seguimiento
# se lleva por la reunion semanal, de modo que no entra en un reclamo de emision.
FUERA_DEL_CICLO = {"P22-BA-09-000-001"}

# El registro guarda este titulo en espanol y el transmittal va integro en ingles.
TITULO_EN = {
    "P22-BA-09-000-005": "Non-Destructive Examination Plan (NDE) — Super Duplex",
}

NO_ENTREGADOS = [
    ("Seismic Calculation Report (NCh 2369)", "Section 7, page 28"),
    ("High-pressure line flexibility analysis", "Section 7, page 28"),
    ("3D model interoperable with the Autodesk suite", "Section 7, page 28"),
    ("High-pressure line isometric drawings", "Section 7, page 28"),
    ("Lifting beams and internal lifting points", "Section 7, page 28"),
    ("Modbus TCP communication system and memory map", "Section 5.4"),
    ("Valve and instrument specifications with brand and model (partial)",
     "Section 7, page 28"),
]

REV0_CITA = ('Description "Issued For Approval" remaining the same until the '
             'document/drawing is approved and then will change to "Issued For '
             'Construction - Rev0"')

REV0_RULE = (
    "The rule is BW Water's own. On the comment sheet issued with the Grounding Point "
    "and Power Panel Location Layout Rev E, document P22-DWG-09-007-003 of 12 May 2026, "
    "BW Water replied to ADASA:"
)
REV0_RULE_CLOSE = (
    "That drawing has been at Code 1 since 11 June. It is now on Rev F and its title "
    "block still reads ISSUED FOR APPROVAL. The Technical Specification "
    "(P22-ET-09-000-001-0), Section 7, says the same: it makes the coding standard "
    "P00-IT-00-000-101-0 binding, and under that standard Revision 0 is the construction "
    "revision and a document reviewed under Status 1 or 2 is to be issued at Revision 0."
)

MOVING_LEAD = "Three rows move with this transmittal."
MOVING = (
    " The Valve List is listed at Rev D and the GA of Antiscalant Dosing Tank at Rev C, "
    "which were the revisions on record when the audit closed; both are disposed here at "
    "Rev E and Rev D, and both are still on a letter. The Radiography Examination "
    "Procedure leaves Table 3 altogether, because it arrives at Rev 0 and is approved at "
    "Code 1 in this transmittal. It is the third of the three non-destructive testing "
    "procedures to reach the construction revision, and it shows that the migration works "
    "when it is undertaken."
)

DDSR_LEAD = "Why the status report does not show this."
CAJETIN_LEAD = "Title blocks that contradict the form."
CAJETIN = (
    " There are {n} documents that already carry a numeric revision and whose title block "
    "still reads ISSUED FOR APPROVAL. Three of them travelled in submittal 25007-0090 "
    "declared IFC on the form, at Rev 0, and say the opposite inside. What reaches the "
    "workshop is the document. Correcting the issue purpose is enough on these, without a "
    "new revision."
)

# ------------------------------------------------------------------ SECCION 4
PENDING_LEAD = "The three most serious items carried forward, none of them received:"
PENDING = [
    ("N30", "Shop fabrication set 25007-ME-PI-0901-0006 to -0016",
     "Eleven drawings across seventeen sheets, stamped for construction, removed from the "
     "Piping Layout at Rev D and never submitted as a deliverable of their own with an "
     "ADASA code and revision index. Their two pressure-containment findings are "
     "unanswered: threaded austenitic instrument branches on super duplex lines rated 60 "
     "to 90 barG design, and an undeclared specification break between the super duplex "
     "and PVC systems",
     "Open, and overdue against three nominated dates"),
    ("N25, N29, N30", "Fabrication and testing dossier",
     "Item 65 remains not delivered. The index has reached Rev B and returned at Code 3; "
     "no record has followed it. It sustains rows 8.3 and 8.4 of the Inspection and Test "
     "Plan, on which 40 per cent of payment depends",
     "Open, overdue"),
    ("N26, N30", "Endorsed structural calculation report P22-CD-09-005-001",
     "Issued at Rev 0 for construction carrying internal initials only. It has yet to be "
     "issued with the endorsement of a professional engineer registered in Chile, "
     "undertaken in writing three times. It governs the anchorage figures stated in note "
     "16 of the antiscalant tank drawing reviewed here",
     "Open, overdue"),
]

ENTERING_LEAD = "Entering the list with this transmittal:"
ENTERING = (
    " the material of VM-09-065 on the CIP pump suction line, to be declared against the "
    "approved Line List before that valve is bought; the size and elevation of the level "
    "marking row of the antiscalant tank; and the document number and issue status of the "
    "radiography procedure."
)

ALSO_OPEN_LEAD = "Also open:"
ALSO_OPEN = (
    " the overpressure and relief sizing analysis for the second PSV-09-002 removed at "
    "Valve List Rev D, carried since Transmittal N14; the liquid penetrant records of 7 "
    "August, examined five days before their procedure was submitted; the measurement "
    "point drawing required by row 7.8 of the Inspection and Test Plan; and the Pressure "
    "Test Record Chart as a controlled form."
)

CLOSING_LEAD = "Closing with this transmittal, and leaving the list:"
CLOSING = (
    " the four valve tags of the 3D model comment sheet, now on the Valve List and on the "
    "approved P&ID; the pressure reducing valve at CIT-09-004; the anchor hole dimension "
    "of the antiscalant tank; and the scope of the radiography procedure, which was the "
    "last of the three non-destructive testing procedures to close its acceptance point."
)

REVIEW_LEAD = "On the review periods."
REVIEW = (
    " These are the eighth and ninth consecutive submittals whose forms ask for return "
    "within three calendar days, against the seven working days of Clause 37.2. Under "
    "that clause the review periods of 25007-0091 and 25007-0092 expire on Tuesday 15 and "
    "Thursday 17 September respectively. ADASA returns both well inside the period. The "
    "native CAD file of the antiscalant tank drawing travelled with submittal 25007-0091 "
    "without being listed on its form."
)

# ------------------------------------------------------------------ SECCION 5
ATTACHMENTS = [
    ("Valve List Rev E", "2", "P22-LI-09-005-002_E_Valve_List_CC_ADASA.pdf"),
    ("GA of Antiscalant Dosing Tank Rev D", "2",
     "P22-DWG-09-005-015_D_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf"),
]
ATTACH_NOTE = (
    "All documents with open observations carry annotated PDFs, the two Code 2. The "
    "Code 1 — Approved document carries none."
)
DOWNLOAD_LEAD = "The annotated PDFs are available at the following download link: "

# ------------------------------------------------------------------ SECCION 6
RESPONSE_SUMMARY = [
    ("P22-LI-09-005-002", "Valve List", "E", "25007-0091", "2 — Approved as noted"),
    ("P22-DWG-09-005-015", "GA of Antiscalant Dosing Tank", "D", "25007-0091",
     "2 — Approved as noted"),
    ("P22-BA-09-000-015", "Radiography Examination Procedure", "0", "25007-0092",
     "1 — Approved"),
]


def fecha_en(d):
    return d["fecha_aprob"].strftime("%d-%b-%Y") if d["fecha_aprob"] else "-"


def auditoria_rev0():
    """Clasifica el registro y devuelve las filas y las cifras de la Seccion 3."""
    docs = auditar()
    ing, cal, _otros = separar(docs)

    a_ing = sorted([d for d in ing if d["cat"] == "A"], key=lambda d: -(d["dias"] or 0))
    b_ing = sorted([d for d in ing if d["cat"] == "B"], key=lambda d: -(d["dias"] or 0))
    c_ing = [d for d in ing if d["cat"] == "C"]
    cal_ab = sorted([d for d in cal if d["cat"] in "AB"
                     and d["codigo_real"] not in FUERA_DEL_CICLO],
                    key=lambda d: -(d["dias"] or 0))
    cal_d = [d for d in cal if d["cat"] == "D"]

    # Tabla 1: los diez datasheets de instrumentos van en una sola fila.
    filas1, grupo = [], [d for d in a_ing if d["codigo_real"] in AGRUPAR]
    for d in a_ing:
        if d["codigo_real"] in AGRUPAR:
            continue
        filas1.append((d["codigo_real"], d["titulo"], d["rev_real"], fecha_en(d),
                       d["dias"]))
    if grupo:
        dd = [d["dias"] for d in grupo if d["dias"] is not None]
        filas1.append(("P22-LI-09-008-005 to -014",
                       f"Instrument datasheets ({len(grupo)} documents)", "A to C",
                       "Mar-Apr 2026", f"{min(dd)} to {max(dd)}"))

    sin_cond = "None — approved without observation"
    filas2 = [(d["codigo_real"], d["titulo"], d["rev_real"],
               CONDICIONES.get(d["codigo_real"], sin_cond)) for d in b_ing]
    filas3 = [(d["codigo_real"], TITULO_EN.get(d["codigo_real"], d["titulo"]),
               d["rev_real"], d["verdicto"].split("-")[0].strip(),
               CONDICIONES.get(d["codigo_real"], sin_cond)) for d in cal_ab]

    # Lo que el registro del proveedor dice de estos mismos documentos. Se cuenta
    # sobre el DDSR y no sobre el cruce, porque se cita el documento del proveedor.
    filas_ddsr = leer_ddsr()
    plan_11 = [r for r in filas_ddsr.values() if r.get("planned") == "11-Sep-26"]
    cien = [d for d in docs if d["cat"] in ("A", "B")
            and (d["ddsr_peso"] or "").startswith("100")]
    dos_rev0 = [d for d in docs if d["ddsr_rev"] == "0" and d["cat"] in ("A", "B")]

    return dict(
        n_items=len(docs), n_ing=len(ing), n_a=len(a_ing), n_b=len(b_ing),
        n_cal=len(cal_ab), n_c=len(c_ing), sin_emitir=len(a_ing) + len(b_ing),
        cal_d=cal_d, cien=len(cien), dos_rev0=dos_rev0, plan_11=len(plan_11),
        filas1=filas1, filas2=filas2, filas3=filas3,
    )


if __name__ == "__main__":
    AUD = auditoria_rev0()

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N39 — SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-039-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )
    doc = Document(OUTPUT)

    # ---------------------------------------------------------- 1. Executive
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [("TRANSMITTAL VERDICT: 2 — Approved as noted. ", {"bold": True}),
                   (VERDICT,)])
    add_para(doc, [(SCOPE_LEAD, {"bold": True}), (SCOPE,)])
    add_para(doc, [(DISPOSITION_LEAD, {"bold": True})])
    for lead, rest in DISPOSITION:
        add_bullet(doc, lead + rest)
    add_para(doc, [(WHY_LEAD, {"bold": True})])
    for punto in WHY:
        add_bullet(doc, punto)
    add_para(doc, [(REV0_POINTER_LEAD, {"bold": True}),
                   (REV0_POINTER.format(**AUD),)])
    add_para(doc, [(POINTER,)])

    # ------------------------------------------------------- 2. Observations
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for titulo, codigo, status, action_lead, action in SUBSECCIONES:
        doc.add_heading(titulo, level=2)
        add_para(doc, [(codigo, {"bold": True})])
        add_para(doc, [("Status.", {"bold": True}), (" " + status,)])
        add_para(doc, [(action_lead, {"bold": True}), (action,)])

    # ------------------------------------------------------------ 3. Rev 0
    doc.add_heading("ISSUE FOR CONSTRUCTION OF THE APPROVED ENGINEERING", level=1)
    add_para(doc, [(
        "ADASA has audited the {n_items} items of the Master Deliverable Register one "
        "by one, against the submittal forms and against the title block of each PDF. "
        "Of the {n_ing} engineering documents, ".format(**AUD),),
        ("{sin_emitir} have never been issued for construction, and {n_a} of those "
         "carry no open observation at all".format(**AUD), {"bold": True}),
        (": ADASA approved them at Code 1 and they are still on a letter revision. The "
         "median age of those approvals is 184 days and the oldest four are 267, from "
         "Transmittal N1 of 16 December 2025.",)])
    add_para(doc, [(REV0_RULE,)])
    add_quote(doc, REV0_CITA)
    add_para(doc, [(REV0_RULE_CLOSE,)])

    add_para(doc, [(
        "Table 1. Engineering approved with no open observation, not issued for "
        "construction, {n_a} documents.".format(**AUD), {"bold": True}),
        (" Nothing is pending on ADASA's side for any of these, and none needs a "
         "change of content.",)])
    add_audit_table(doc, ["Document code", "Title", "Rev.", "Approved", "Days"],
                    AUD["filas1"], anchos=[1.6, 2.5, 0.5, 1.1, 0.8])

    add_para(doc, [(
        "Table 2. Engineering approved as noted, not issued for construction, "
        "{n_b} documents.".format(**AUD), {"bold": True}),
        (" Each one carries the condition stated in the transmittal that disposed it, "
         "and that condition is what the Revision 0 has to incorporate.",)])
    add_audit_table(doc, ["Document code", "Title", "Rev.", "Outstanding condition"],
                    AUD["filas2"], anchos=[1.5, 1.7, 0.45, 2.85])

    add_para(doc, [(
        "Table 3. Quality and fabrication documents approved and on a letter "
        "revision, {n_cal} documents.".format(**AUD), {"bold": True}),
        (" They are listed apart because they follow the fabrication cycle, and that "
         "package is already migrating to Revision 0, which is the point.",)])
    add_audit_table(
        doc, ["Document code", "Title", "Rev.", "Response", "Outstanding"],
        AUD["filas3"], anchos=[1.45, 1.75, 0.4, 0.7, 2.2])
    add_para(doc, [("Outside that table, "
                    + " and ".join(f"the {d['titulo']} at Rev {d['rev_real']}"
                                   for d in AUD["cal_d"])
                    + " remain at Code 3 and go to the next letter revision instead.",)])

    add_para(doc, [("Table 4. Deliverables of the Technical Specification not yet "
                    "received.", {"bold": True})])
    add_audit_table(doc, ["Deliverable", "Technical Specification reference"],
                    NO_ENTREGADOS, anchos=[4.3, 2.2])

    add_para(doc, [(MOVING_LEAD, {"bold": True}), (MOVING,)])
    add_para(doc, [(DDSR_LEAD, {"bold": True}), (
        " The Document and Drawing Status Report does not measure it. None of its "
        "twelve columns records whether a document has been issued for construction, "
        "and the strings IFC and Rev 0 do not appear anywhere in the report of 7 "
        "September. Its weighting gives 100 per cent to an approved document without "
        "looking at the revision it stopped at, so {cien} of the documents listed "
        "above sit there at 100 per cent.".format(**AUD),)])
    add_para(doc, [("Two entries go further. The report declares "
                    + " and ".join(f"{d['titulo']} ({d['codigo_real']})"
                                   for d in AUD["dos_rev0"])
                    + " at Rev 0, and ADASA holds "
                    + " and ".join(f"Rev {d['rev_real']}" for d in AUD["dos_rev0"])
                    + ". No later file exists on ADASA's side. BW Water is asked to "
                      "confirm whether those two were issued and not transmitted.",)])
    add_para(doc, [(CAJETIN_LEAD, {"bold": True}),
                   (CAJETIN.format(n=AUD["n_c"]),)])

    add_para(doc, [
        ("Action — issue at Revision 0 by Friday 11 September 2026.", {"bold": True}),
        (" The {n_a} documents of Table 1 need no change of content, only the revision "
         "number and the issue purpose of the title block. The {n_b} of Table 2 and the "
         "{n_cal} of Table 3 are to be issued at Revision 0 with their condition "
         "incorporated, and with no intermediate approval revision. The {n_c} documents "
         "that already carry a numeric revision need their title block corrected, and "
         "the seven deliverables of Table 4 remain to be submitted. Whatever cannot be "
         "issued by that date is to carry its committed issue date in the Document and "
         "Drawing Status Report of that same day, which already shows {plan_11} rows "
         "dated that Friday.".format(**AUD),)])

    # ----------------------------------------------------------- 4. Pending
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [(PENDING_LEAD,)])
    add_simple_table(doc, [("Origin TM", "Document", "Observation", "Status")] + PENDING)
    add_para(doc, [(ENTERING_LEAD, {"bold": True}), (ENTERING,)])
    add_para(doc, [(ALSO_OPEN_LEAD, {"bold": True}), (ALSO_OPEN,)])
    add_para(doc, [(CLOSING_LEAD, {"bold": True}), (CLOSING,)])
    add_para(doc, [(REVIEW_LEAD, {"bold": True}), (REVIEW,)])

    # -------------------------------------------------------- 5. Attachments
    doc.add_heading("ATTACHMENTS", level=1)
    _fijar_anchos(
        add_simple_table(doc, [("Document", "Code", "Annotated PDF")] + ATTACHMENTS),
        [2.1, 0.6, 3.8])
    add_para(doc, [(ATTACH_NOTE,)])
    p = doc.add_paragraph()
    r = p.add_run(DOWNLOAD_LEAD)
    r.bold = True
    aplicar_arial_12(p)
    add_hyperlink(p, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # ----------------------------------------------------- 6. Response Summary
    doc.add_heading("RESPONSE SUMMARY", level=1)
    _fijar_anchos(
        add_simple_table(
            doc,
            [("Document Code", "Title", "Rev", "Submittal", "Response Code")]
            + RESPONSE_SUMMARY,
        ),
        [1.45, 1.85, 0.5, 0.95, 1.75])

    doc.save(OUTPUT)
    print("Documento generado: " + OUTPUT)
    print("  Seccion 3, cifras del auditor: {sin_emitir} de {n_ing} sin emitir | "
          "tabla 1 {n_a} | tabla 2 {n_b} | tabla 3 {n_cal} | cajetines {n_c} | "
          "al 100% en el DDSR {cien} | filas al 11-Sep {plan_11}".format(**AUD))
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")
