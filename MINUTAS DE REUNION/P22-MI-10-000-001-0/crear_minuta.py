#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la minuta P22-MI-10-000-001-0
(Minutes of Meeting - Weekly Coordination Meeting of 16 September 2026)
usando el template-adasa. Idioma ingles. Destinatario: BW Water.

Codigo:  P22-MI-10-000-001-0  (tipo MI = minuta, area 10 neutral por ser reunion
         bilateral; primer documento de este tipo, decision del usuario 16-Sep)
Fecha:   16-Sep-2026 (miercoles)
Rev:     0

FUENTE: transcripcion Plaud "Project Meeting: Fedco Turbocharger Piping Misalignment
Delays Schedule" (file of_fa5768bc11226dbe9b2452f1c077c0aa, 29 min, 12:30 UTC =
09:30 Chile). El PDF `MINUTA DE REUNION 16-09-26.pdf` es el resumen automatico de
esa grabacion; su extraccion esta en `md/MINUTA DE REUNION 16-09-26_extracted.md`.

REGLAS DE CONTENIDO (usuario, 16-Sep):
  - Solo lo que se dijo en la reunion. NO se incluyen los bloques "Notes /
    Considerations" ni "General Considerations" del resumen: son consejos de la IA.
  - Donde el resumen y la transcripcion difieren, manda la transcripcion:
      * "Jerk packaging" = yoke / lifting package; "PH Chilian" = Chilean PE.
      * "Burubalitas" = Bureau Veritas.
      * Repetir la prueba de alta presion en toda la linea NO es accion de Luis:
        ADASA lo exigio y Eduardo lo confirmo como obligatorio para BW Water.
      * Donde hacer el retrabajo (fuera o dentro del contenedor) quedo SIN acuerdo:
        se registran las dos posiciones.
  - Sin nombres internos de BW Water (Pietri, Jerome, Sadeep, Billy, Nick).

Path al skill: absoluto via ~/.claude/skills/template-adasa segun CLAUDE.md Seccion 3.
NOTA: el template numera H1/H2 automaticamente. NO escribir numeros en add_heading.
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)
# docx_metadata vive en la carpeta compartida de skills, no en template-adasa
sys.path.insert(0, os.path.expanduser("~/.claude/skills/_shared"))

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    add_simple_table,
    add_bullet,
)
import docx_metadata  # noqa: E402
from docx import Document  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-MI-10-000-001-0_Minutes-Weekly-Meeting-16Sep2026_ADASA.docx",
)


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def ajustar_tabla(table, anchos=None):
    """Celdas alineadas a la izquierda (el justificado abre huecos en columnas
    angostas) y filas que no se parten entre paginas. Si se dan anchos (pulgadas),
    se escriben en el tblGrid y en cada celda: Word obedece al tblGrid."""
    if anchos:
        for col, ancho in zip(table._tbl.tblGrid.findall(qn("w:gridCol")), anchos):
            col.set(qn("w:w"), str(int(ancho * 1440)))
        for row in table.rows:
            for cell, ancho in zip(row.cells, anchos):
                cell.width = Inches(ancho)
    for row in table.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        for cell in row.cells:
            for para in cell.paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT


def crear_documento():
    crear_documento_adasa(
        titulo="MINUTES OF MEETING — WEEKLY COORDINATION MEETING OF "
        "16 SEPTEMBER 2026",
        codigo="P22-MI-10-000-001-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=False,
    )

    doc = Document(OUTPUT)

    # ---- limpiar placeholder ------------------------------------------------
    elementos_a_eliminar = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos_a_eliminar.append(para)
    for para in elementos_a_eliminar:
        p = para._element
        p.getparent().remove(p)

    # =========================================================================
    # MEETING INFORMATION
    # =========================================================================
    doc.add_heading("MEETING INFORMATION", level=1)
    ajustar_tabla(add_simple_table(doc, [
        ("Item", "Detail"),
        ("Project", "Second Stage RO Brine Module, Taltal (Contract C-4300)"),
        ("Date and time", "Wednesday 16 September 2026, 09:30 Chile time"),
        ("Format", "Video call, approximately 30 minutes"),
        ("ADASA", "Luis Rivera"),
        ("BW Water", "Eduardo Yamauchi, Stephane Gehant"),
        ("Remarks", "The Penang team did not attend due to a public holiday "
         "in Malaysia"),
    ]))

    # =========================================================================
    # DISCUSSION AND AGREEMENTS
    # =========================================================================
    doc.add_heading("DISCUSSION AND AGREEMENTS", level=1)

    # ---- 2.1 ----------------------------------------------------------------
    doc.add_heading("Equipment Delivery", level=2)
    add_para(
        doc,
        "BW Water reported that all equipment has been delivered, including the "
        "Fedco pumps, and considers the procurement tracker closed.",
    )

    # ---- 2.2 ----------------------------------------------------------------
    doc.add_heading("Turbocharger Piping Misalignment", level=2)
    add_para(
        doc,
        "During the installation of a turbocharger in the skid, the piping showed "
        "a vertical and a horizontal offset with respect to the turbocharger, "
        "estimated by BW Water at about 50 mm. The affected spools will be "
        "removed, cut, rewelded, retested and reassembled, and the material for "
        "the rework is available. The pressure tests already performed on the "
        "spools to be modified are no longer valid.",
    )
    add_para(
        doc,
        "Stephane Gehant stated that the turbocharger delivered by Fedco does not "
        "match the Fedco drawings, and that the pump and the turbocharger were "
        "received only last week. Eduardo Yamauchi stated that the specification "
        "and design of the turbocharger are not in question. He acknowledged that "
        "the 3D model and the isometrics used to fabricate the spools carried an "
        "offset with respect to the delivered equipment, identified this as the "
        "source of the issue, and added that accumulated length tolerances "
        "contributed to it.",
    )
    add_para(
        doc,
        "According to BW Water, only the spools connected to this turbocharger "
        "are affected, and the tie-in points and the rest of the layout remain "
        "valid. BW Water could not confirm during the meeting whether the unit is "
        "the feed or the interstage turbocharger, whether one or both units are "
        "involved, or how many spools must be modified.",
    )
    add_para(
        doc,
        "ADASA stated that the situation is unacceptable. The shop fabrication "
        "drawings and the isometrics of the spools have been requested at every "
        "weekly meeting and have not been received, and the piping was modeled in "
        "AutoCAD Plant 3D precisely to prevent this type of error.",
    )
    add_para(
        doc,
        "BW Water proposed correcting only the vertical and horizontal portions of "
        "the affected spools in place, with completion on 23 September 2026, and "
        "did not recommend removing them. ADASA requested that the rework and the "
        "high pressure test be carried out with the spools outside the container, "
        "since the test cannot be properly repeated with the spools installed. "
        "ADASA also required the high pressure test to be repeated for the whole "
        "of each affected line, and BW Water confirmed this as mandatory.",
    )
    add_para(
        doc,
        "It was agreed that BW Water will issue a report on 17 September 2026, to "
        "be reviewed that day in a meeting at 08:30 Chile time with Victor "
        "Gutierrez. The report is to cover:",
    )
    add_bullet(doc, "The root cause of the offset.")
    add_bullet(doc, "Which turbocharger is affected, and whether the issue "
               "involves one or both units.")
    add_bullet(doc, "The affected spools, identified individually.")
    add_bullet(doc, "The shop fabrication drawings of the spools, stating which "
               "are correct and which must be modified.")
    add_bullet(doc, "The status of the pipe layout.")

    # ---- 2.3 ----------------------------------------------------------------
    doc.add_heading("Schedule Impact", level=2)
    add_para(
        doc,
        "BW Water projects the system ready to ship on 12 October 2026. The piping "
        "rework is planned for completion on 23 September 2026, with the Penang "
        "team working until 22:00 every day and through the weekend. Asked about "
        "the delay in the schedule presented during the meeting, BW Water "
        "indicated a shift from 29 September to 9 October 2026.",
    )
    add_para(
        doc,
        "That schedule has not been sent to ADASA. BW Water stated that the "
        "procurement status, the weekly progress report and the documentation "
        "status report have been sent, and ADASA requested the schedule "
        "immediately.",
    )

    # ---- 2.4 ----------------------------------------------------------------
    doc.add_heading("Engineering Documentation Committed for 11 September", level=2)
    add_para(
        doc,
        "ADASA stated that none of the documentation committed for 11 September "
        "2026 has been received. According to Stephane Gehant, the 3D model, the "
        "line list and the pipe layout were submitted for BW Water internal "
        "approval on 14 September and should be sent to ADASA on 17 September. "
        "Eduardo Yamauchi will follow up with the engineering team and confirm the "
        "delivery date.",
    )
    add_para(
        doc,
        "ADASA stated that the pipe layout under internal approval is affected by "
        "the same misalignment, so its internal approval does not resolve the "
        "issue.",
    )

    # ---- 2.5 ----------------------------------------------------------------
    doc.add_heading("Lifting Package", level=2)
    add_para(
        doc,
        "BW Water expects the lifting drawings, including the yoke, to be "
        "finalized on Friday 18 September 2026 and sent to ADASA on Monday 21 or "
        "Tuesday 22 September. The purchase order with the Chilean Professional "
        "Engineer has been placed, and BW Water has requested that the complete "
        "lifting package be added to the scope of his review. No reply has been "
        "received yet, and BW Water will follow up on the delivery date.",
    )
    add_para(
        doc,
        "BW Water expects the lifting package and the certification to be "
        "resolved by the end of the week of 21 September 2026.",
    )

    # ---- 2.6 ----------------------------------------------------------------
    doc.add_heading("Factory Acceptance Test Procedure", level=2)
    add_para(
        doc,
        "ADASA stated that the Factory Acceptance Test procedure, requested by "
        "email on 16 September, has not been received. ADASA needs it to "
        "coordinate the third-party inspection with Bureau Veritas, and the "
        "documentation milestone should have been closed months ago. BW Water "
        "confirmed that the Factory Acceptance Test will not take place next week.",
    )
    add_para(
        doc,
        "BW Water acknowledged the delay and attributed it to the workload of the "
        "engineering team assigned to this scope. HMI simulations and program "
        "testing are ongoing, and the pending work is the compilation of the "
        "procedure. BW Water will escalate internally to complete the document. "
        "No delivery date was given during the meeting.",
    )

    # ---- 2.7 ----------------------------------------------------------------
    doc.add_heading("Membranes, Two-Year Spare Parts and Payments", level=2)
    add_para(
        doc,
        "BW Water asked to close the membranes item, including the arrangements "
        "for their pickup, and the two-year spare parts. ADASA expects to close "
        "both next week. BW Water confirmed receipt of the three payments last "
        "week.",
    )

    # ---- 2.8 ----------------------------------------------------------------
    doc.add_heading("ADASA Point of Contact", level=2)
    add_para(
        doc,
        "From 21 September to 2 October 2026, Victor Gutierrez will be in charge "
        "of ADASA's communication with BW Water. Luis Rivera returns on 5 October "
        "2026. BW Water will include Victor Gutierrez in the meeting of "
        "17 September.",
    )

    # =========================================================================
    # ACTION ITEMS
    # =========================================================================
    doc.add_heading("ACTION ITEMS", level=1)
    ajustar_tabla(add_simple_table(doc, [
        ("No.", "Action", "Responsible", "Due date"),
        ("1", "Send ADASA the schedule presented during the meeting",
         "BW Water", "16-Sep-2026"),
        ("2", "Send the invitation to the follow-up meeting, including Victor "
         "Gutierrez", "BW Water", "16-Sep-2026"),
        ("3", "Issue the report on the turbocharger piping misalignment, with the "
         "content listed in Section 2.2 - Turbocharger Piping Misalignment",
         "BW Water", "17-Sep-2026"),
        ("4", "Review the report in a follow-up meeting at 08:30 Chile time",
         "ADASA / BW Water", "17-Sep-2026"),
        ("5", "Send the 3D model, the line list and the pipe layout, and confirm "
         "the delivery date of the documentation committed for 11 September",
         "BW Water", "17-Sep-2026"),
        ("6", "Issue the Factory Acceptance Test procedure, as requested in "
         "ADASA's email of 16 September", "BW Water", "18-Sep-2026"),
        ("7", "Send the lifting drawings, including the yoke", "BW Water",
         "21 or 22-Sep-2026"),
        ("8", "Confirm the Professional Engineer's delivery date for the review "
         "of the lifting package", "BW Water", "Not stated"),
        ("9", "Complete the rework of the affected spools", "BW Water",
         "23-Sep-2026"),
        ("10", "Repeat the high pressure test for the whole of each affected line",
         "BW Water", "After the rework"),
        ("11", "Resolve the lifting package and the certification", "BW Water",
         "25-Sep-2026"),
        ("12", "Close the membranes, including pickup arrangements, and the "
         "two-year spare parts", "ADASA / BW Water", "21 to 25-Sep-2026"),
        ("13", "System ready to ship (BW Water projection)", "BW Water",
         "12-Oct-2026"),
    ]), anchos=[0.45, 3.05, 1.5, 1.5])

    # Sin seccion DOCUMENT HISTORY: decision del usuario, 16-Sep.

    # add_simple_table deja un parrafo vacio tras la tabla; al final del documento
    # sobra y puede abrir una pagina en blanco
    ultimo = doc.paragraphs[-1]
    if not ultimo.text.strip():
        ultimo._element.getparent().remove(ultimo._element)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="Minutes of Meeting - Weekly Coordination Meeting of "
        "16 September 2026",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Second Stage RO Brine Module - Taltal",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT)
    docx_metadata.fix_app_xml(OUTPUT, company="Aguas de Antofagasta S.A.")
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
