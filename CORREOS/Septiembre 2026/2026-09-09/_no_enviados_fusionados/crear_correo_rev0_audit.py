#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo a Eduardo Yamauchi: auditoria de emision para construccion.

Dos ejes, por decision del usuario: la emision en revision 0 de lo que ADASA ya
aprobo, y los entregables de la Seccion 7 que no se han recibido. Quedan fuera el
idioma de la Clausula 6, el hito de pago y la liberacion de despacho; el cierre
lleva una reserva generica para no renunciar a ellos.

Las cifras y las tablas NO se escriben a mano: se importan de
REVISIONES/EVALUACIONES/auditar_documentos_bw.py, que clasifica los 113 items del
Master Deliverable Register cruzandolo con los formularios de submittal y con el
cajetin de cada PDF.

Idioma ingles (CLAUDE.md Seccion 3.4, BW Water 100% ingles).
"""
import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-09_Issue-for-Construction-Audit.docx")
CONTACTO = "Luis Rivera Gonzalez"

sys.path.insert(0, os.path.abspath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "REVISIONES", "EVALUACIONES")))
from auditar_documentos_bw import auditar, leer_ddsr, separar  # noqa: E402


# --------------------------------------------------------------------- helpers
def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def aplicar_arial_table(table, size=9):
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)


def parrafo(doc, texto, size=11, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.bold = bold
    aplicar_arial(p, size)
    return p


def add_table(doc, headers, rows, size=9):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(headers):
        c = t.rows[0].cells[j]
        c.text = h
        for para in c.paragraphs:
            for run in para.runs:
                run.bold = True
    for i, fila in enumerate(rows, start=1):
        for j, v in enumerate(fila):
            t.rows[i].cells[j].text = str(v)
    aplicar_arial_table(t, size)
    return t


# ------------------------------------------------------------------ contenido
# Lo que queda abierto en cada documento aprobado con observaciones, condensado a
# una clausula desde la columna Action Required del registro.
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
# que van agrupados para que la tabla quepa en un correo. El rango de codigos mantiene
# la trazabilidad.
AGRUPAR = {"P22-LI-09-008-005", "P22-LI-09-008-006", "P22-LI-09-008-007",
           "P22-LI-09-008-008", "P22-LI-09-008-009", "P22-LI-09-008-010",
           "P22-LI-09-008-011", "P22-LI-09-008-012", "P22-LI-09-008-013",
           "P22-LI-09-008-014"}

# El Project Schedule se retiro del ciclo de transmittals en el N36 y su seguimiento
# se lleva por la reunion semanal de coordinacion, de modo que no recibe codigo de
# respuesta y no entra en un reclamo de emision.
FUERA_DEL_CICLO = {"P22-BA-09-000-001"}

# El registro guarda este titulo en espanol y el correo va integro en ingles.
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


def fecha_es(d):
    return d["fecha_aprob"].strftime("%d-%b-%Y") if d["fecha_aprob"] else "-"


def crear_correo():
    docs = auditar()
    ing, cal, otros = separar(docs)

    a_ing = sorted([d for d in ing if d["cat"] == "A"], key=lambda d: -(d["dias"] or 0))
    b_ing = sorted([d for d in ing if d["cat"] == "B"], key=lambda d: -(d["dias"] or 0))
    c_ing = [d for d in ing if d["cat"] == "C"]
    cal_ab = sorted([d for d in cal if d["cat"] in "AB"
                     and d["codigo_real"] not in FUERA_DEL_CICLO],
                    key=lambda d: -(d["dias"] or 0))
    cal_d = [d for d in cal if d["cat"] == "D"]
    sin_emitir = len(a_ing) + len(b_ing)
    # Lo que el registro del proveedor declara sobre estos mismos documentos. Las
    # cifras del DDSR se cuentan sobre el DDSR y no sobre el cruce, porque el correo
    # cita el documento del proveedor.
    filas_ddsr = leer_ddsr()
    tot_ddsr = len(filas_ddsr)
    con_plan = [r for r in filas_ddsr.values() if r.get("planned")]
    plan_11 = [r for r in con_plan if r["planned"] == "11-Sep-26"]
    cien = [d for d in docs if d["cat"] in ("A", "B")
            and (d["ddsr_peso"] or "").startswith("100")]
    dos_rev0 = [d for d in docs if d["ddsr_rev"] == "0" and d["cat"] in ("A", "B")]

    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.7)
        s.left_margin = s.right_margin = Inches(0.7)

    campos = [
        ("Date:", "September 9, 2026"),
        ("From:", f"{CONTACTO}, Leader, Infrastructure Engineering (ADASA)"),
        ("To:", "Eduardo Yamauchi, BW Water Americas Inc."),
        ("CC:", "Victor Gutierrez (ADASA), Jeryl Regulacion (BW Water)"),
        ("Subject:", "Documentation close-out of Friday 11 September: issue for "
                     "construction status of the approved engineering"),
        ("Ref:", "Contract C-4300 / BAE 12803 / Master Deliverable Register "
                 "P22-IT-06-000-002-0"),
    ]
    for etiqueta, valor in campos:
        p = doc.add_paragraph()
        r1 = p.add_run(f"{etiqueta} ")
        r1.bold = True
        p.add_run(valor)
        aplicar_arial(p, 11)

    doc.add_paragraph()
    parrafo(doc, "Dear Eduardo,")
    doc.add_paragraph()

    # ------------------------------------------------------------ 1. hallazgo
    parrafo(doc,
        "In today's meeting we set Friday 11 September to close the documentation "
        "milestones. Before that date I audited the deliverables of the Master Deliverable "
        f"Register ({len(docs)} items) one by one, to see what closing them takes.")
    doc.add_paragraph()
    parrafo(doc,
        f"Of the {len(ing)} engineering documents, {sin_emitir} have never been issued "
        f"for construction, and {len(a_ing)} of those carry no open observation at all: "
        "I approved them under Code 1 and they are still on a letter revision. The median "
        "age of those approvals is 184 days and the oldest four are 267, from Transmittal "
        "N1 of 16 December 2025. The two tank drawings we went through today are part of "
        "that set.")
    doc.add_paragraph()

    # ------------------------------------------------------------- 2. la regla
    parrafo(doc,
        "The rule I am asking you to apply is your own. On the comment sheet issued with "
        "the Grounding Point and Power Panel Location Layout Rev E, document "
        "P22-DWG-09-007-003 of 12 May 2026, BW Water replied to ADASA:")
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    r = p.add_run('Description "Issued For Approval" remaining the same until the '
                  'document/drawing is approved and then will change to "Issued For '
                  'Construction - Rev0"')
    r.italic = True
    aplicar_arial(p, 10)
    parrafo(doc,
        "That drawing has been Code 1 since 11 June. It is now on Rev F and its title "
        "block still reads ISSUED FOR APPROVAL. The Technical Specification, Section 7, "
        "says the same: it makes the coding standard P00-IT-00-000-101-0 binding, and "
        "under that standard Revision 0 is the construction revision and a document "
        "reviewed under Status 1 or 2 is to be issued at Revision 0.")
    doc.add_paragraph()

    # ------------------------------------------------- el registro del proveedor
    parrafo(doc, "Why the register does not show it", bold=True)
    parrafo(doc,
        "The Document and Drawing Status Report (DDSR) does not measure this, because "
        "none of its twelve columns records "
        "whether a document has been issued for construction, and the strings IFC and "
        "Rev 0 do not appear anywhere in the report of 7 September. Its weighting gives "
        "100 per cent to an approved document without looking at the revision it stopped "
        f"at, so {len(cien)} of the documents listed below sit there at 100 per cent.")
    if dos_rev0:
        parrafo(doc,
            "Two entries go further. The register declares "
            + " and ".join(f"{d['titulo']} ({d['codigo_real']})" for d in dos_rev0)
            + " at Rev 0, and I hold "
            + " and ".join(f"Rev {d['rev_real']}" for d in dos_rev0)
            + ". No later file exists on our side. Please confirm whether those two were "
            "issued and not transmitted.")
    doc.add_paragraph()

    # ------------------------------- 3. tabla 1, aprobados sin observaciones
    parrafo(doc, f"Table 1. Engineering approved with no open observation, not "
                 f"issued for construction, {len(a_ing)} documents", bold=True)
    parrafo(doc, "Nothing is pending on my side for any of these, and none needs a "
                 "change of content.", size=10)
    filas = []
    grupo = [d for d in a_ing if d["codigo_real"] in AGRUPAR]
    for d in a_ing:
        if d["codigo_real"] in AGRUPAR:
            continue
        filas.append((d["codigo_real"], d["titulo"], d["rev_real"], fecha_es(d),
                      d["dias"]))
    if grupo:
        dd = [d["dias"] for d in grupo if d["dias"] is not None]
        filas.append(("P22-LI-09-008-005 to -014",
                      f"Instrument datasheets ({len(grupo)} documents)", "A to C",
                      "Mar-Apr 2026", f"{min(dd)} to {max(dd)}"))
    add_table(doc, ["Document code", "Title", "Rev.", "Approved", "Days"], filas)
    en_rev = [d for d in a_ing + b_ing if d.get("rev_en_revision")]
    if en_rev:
        parrafo(doc,
            "Two of them have a later revision already with me and not yet returned, "
            + " and ".join(f"the {d['titulo']} at Rev {d['rev_en_revision'].split()[0]}"
                           for d in en_rev)
            + ", and both of those are on a letter as well.", size=10)
    doc.add_paragraph()

    # ------------------------------ 4. tabla 2, aprobados con observaciones
    parrafo(doc, f"Table 2. Engineering approved as noted, not issued for "
                 f"construction, {len(b_ing)} documents", bold=True)
    parrafo(doc, "Each one carries the condition stated in the transmittal that "
                 "disposed it, and that condition is what the Revision 0 has to "
                 "incorporate.", size=10)
    add_table(doc, ["Document code", "Title", "Rev.", "Outstanding condition"],
              [(d["codigo_real"], d["titulo"], d["rev_real"],
                CONDICIONES.get(d["codigo_real"],
                                "None — approved without observation"))
               for d in b_ing])
    doc.add_paragraph()

    # --------------------------------------------- 5. tabla 3, calidad
    parrafo(doc, f"Table 3. Quality and fabrication documents approved and on a "
                 f"letter revision, {len(cal_ab)} documents", bold=True)
    parrafo(doc, "They are listed apart because they follow the fabrication cycle, and "
                 "that package is already migrating to Revision 0, which is the point.",
            size=10)
    add_table(doc, ["Document code", "Title", "Rev.", "Response", "Outstanding"],
              [(d["codigo_real"], TITULO_EN.get(d["codigo_real"], d["titulo"]),
                d["rev_real"], d["verdicto"].split("-")[0].strip(),
                CONDICIONES.get(d["codigo_real"],
                                "None — approved without observation"))
               for d in cal_ab])
    parrafo(doc,
        "Outside this table, "
        + " and ".join(f"the {d['titulo']} at Rev {d['rev_real']}" for d in cal_d)
        + " remain under Code 3 and go to the next letter revision instead.", size=10)
    doc.add_paragraph()

    # ----------------------------------------- 6. tabla 4, no entregados
    parrafo(doc, "Table 4. Section 7 deliverables not yet received", bold=True)
    add_table(doc, ["Deliverable", "Technical Specification reference"], NO_ENTREGADOS)
    doc.add_paragraph()

    # ------------------------------------------------ 7. los cajetines
    parrafo(doc,
        f"A separate point. There are {len(c_ing)} documents that already carry a numeric "
        "revision and whose title block still reads ISSUED FOR APPROVAL. Three of them "
        "travelled in submittal 25007-0090 declared IFC on the form, at Rev 0, and say "
        "the opposite inside. What reaches the workshop is the document. Correcting the "
        "issue purpose is enough on these, without a new revision.")
    doc.add_paragraph()

    # ------------------------------------------------------- 8. lo que se pide
    parrafo(doc, "What I am asking for on Friday 11 September", bold=True)
    parrafo(doc,
        f"The {len(a_ing)} documents of Table 1 issued at Revision 0. None needs a change "
        "of content, only the revision number and the issue purpose of the title block. "
        f"The {len(b_ing)} of Table 2 and the {len(cal_ab)} of Table 3 issued at Revision "
        "0 with their condition incorporated, and no intermediate approval revision. The "
        "corrected title block on the documents that already carry a numeric revision, "
        "and the seven deliverables of Table 4.")
    parrafo(doc,
        "I had not set a date for these reissues until now, and that is what this email "
        "fixes. Whatever cannot be issued by Friday, please give me its committed issue "
        f"date that same day in the DDSR, which already carries {len(plan_11)} rows "
        "dated this Friday.")
    doc.add_paragraph()

    parrafo(doc,
        "This email is sent without prejudice to ADASA's rights under the Contract.")
    doc.add_paragraph()

    parrafo(doc, "Best regards,")
    doc.add_paragraph()
    parrafo(doc, CONTACTO)
    parrafo(doc, "Leader, Infrastructure Engineering")
    parrafo(doc, "ADASA, Aguas de Antofagasta S.A.")

    doc.core_properties.author = "Luis Rivera Gonzalez"
    doc.core_properties.company = "Aguas Antofagasta"
    doc.core_properties.comments = (
        "Auditoria documento por documento de la emision para construccion de los "
        "entregables de BW Water, al cierre del TM N38")
    doc.save(OUTPUT_FILE)
    print(f"OK: {os.path.basename(OUTPUT_FILE)}")
    print(f"    tabla 1: {len(filas)} filas ({len(a_ing)} documentos) | "
          f"tabla 2: {len(b_ing)} | tabla 3: {len(cal_ab)} | "
          f"tabla 4: {len(NO_ENTREGADOS)} | contradicciones: {len(c_ing)}")


if __name__ == "__main__":
    crear_correo()
