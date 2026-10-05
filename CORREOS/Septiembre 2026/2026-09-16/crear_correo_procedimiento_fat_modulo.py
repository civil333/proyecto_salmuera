#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_correo_procedimiento_fat_modulo.py
Correo urgente a Eduardo Yamauchi exigiendo el procedimiento FAT del modulo
(PROV-PROC-FAT-001), por hilo nuevo.

POR QUE SALE HOY, MIERCOLES 16

El barrido de las 93 entregas de BW Water (nombre de archivo y texto de 390 PDF
unicos, comprimidos incluidos) confirma que el procedimiento FAT del modulo
nunca se sometio. Lo unico que existe es el P22-PP-09-000-001 Rev C, que es
hardware del tablero y excluye por su Section 3 las pruebas funcionales de
software y la verificacion de logica. El FAT es la proxima semana (usuario, y
Progress Update del 28-Ago, tarea 419, del 15 al 25 de septiembre), y la fila
7.1 del ITP Rev 0 es Hold de ADASA sobre la aprobacion de ese procedimiento.
El Transmittal N39 dejo de arrastrar el faltante.

DECISIONES DEL USUARIO (16-Sep)

- Plazo: viernes 18 de septiembre.
- No se menciona el plazo de revision de ADASA (Clausula 37.2, siete dias
  habiles), aunque sometido el 18 venceria despues del embarque del 28.
- Hilo nuevo, no Reply-All a la cadena del 08-Sep.
- Directo y ejecutivo, con toda la trazabilidad en una tabla.
- No abrir con que nunca se sometio: el orden es obligacion e historial (con la
  tabla), estado y consecuencia, por que el Rev C del tablero no lo cubre, y el
  pedido. Cada parrafo retoma algo del anterior.

FUERA DEL CUERPO: la omision del N39, la minuta del 09-Sep (no oponible), el
DDSR (no lista ningun procedimiento de calidad), la ausencia de respuesta al
08-Sep (correo entrante en HOLD) y el procedimiento de conservacion y embalaje.

ORTOGRAFIA: en-US. Ingles, primera persona. Document() directo, sin template ADASA.
"""
import os

from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-16_Module-FAT-Procedure-Required.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"
SUBJECT = ("URGENT - TALTAL: Module Factory Acceptance Test procedure required "
           "before the FAT")

# Trazabilidad. Cada fila verificada contra su fuente primaria; ver la tabla de
# fuentes del _Descripcion.md.
TRACE_HEADERS = ("Date", "Record", "Status")
TRACE_ROWS = [
    ("5 May 2026", "Transmittal N17, Project Quality Plan Rev A",
     "No FAT scope and no FAT procedure (OBS-02)"),
    ("25 May 2026", "Transmittal N19, ITP Offsite Rev B",
     "Firm delivery dates requested for the Hydrostatic, Preservation and FAT "
     "procedures"),
    ("10 June 2026", "Transmittal N20",
     "Hydrostatic, Preservation and FAT procedures still undelivered"),
    ("6 July 2026", "Transmittal N26, Inspection and Test Plan Rev 0 approved at "
     "Code 1",
     "Row 7.1, approval of the detailed FAT procedure PROV-PROC-FAT-001, is an "
     "ADASA hold point"),
    ("18 August 2026", "Transmittal N34, Quality Dossier Index Rev B",
     "Chapter B11, FAT Procedure, is the only entry of its QA documents section "
     "without a document number"),
    ("28 August 2026", "BW Water Progress Update",
     "Task 419, Factory Acceptance Test for System, from 15 to 25 September; no "
     "activity for the procedure"),
    ("31 August 2026", "Transmittal N37, Section 3",
     "Required in the consolidated submission due Thursday 3 September; recorded "
     "as never delivered"),
    ("3 September 2026", "Transmittal N38, Section 3", "Not received"),
    ("8 September 2026", "My email ahead of the coordination meeting of "
     "9 September",
     "Issue date of the procedure requested"),
]


def aplicar_arial(paragraph, size=11):
    for r in paragraph.runs:
        r.font.name = "Arial"
        r.font.size = Pt(size)
    return paragraph


def _set_lang(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma(doc, lang=LANG):
    for p in doc.paragraphs:
        for r in p.runs:
            _set_lang(r._element.get_or_add_rPr(), lang)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        _set_lang(r._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11):
    p = doc.add_paragraph()
    p.add_run(text)
    return aplicar_arial(p, size)


def add_segments(doc, segs, size=11):
    p = doc.add_paragraph()
    for texto, bold in segs:
        r = p.add_run(texto)
        r.bold = bold
    return aplicar_arial(p, size)


def add_table(doc, headers, rows, size=10):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(size)
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(value)
            run.font.name = "Arial"
            run.font.size = Pt(size)
    return table


def blank(doc):
    return doc.add_paragraph()


def crear_correo():
    doc = Document()
    fmt = doc.styles["Normal"].paragraph_format
    fmt.space_after = Pt(0)
    fmt.line_spacing = 1.0
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    fields = [
        ("Date:", "September 16, 2026"),
        ("From:", CONTACTO + " - Leader, Infrastructure Engineering (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Stephane Gehant; Jeryl F. Regulacion; Lokman Hakim Bin Mat; "
                "Magdier Arias; Mohd Adnin Bin Zulkaflee; Sadeep Irugalbandara; "
                "Nick Huta - BW Water; Victor Gutierrez - ADASA"),
        ("Subject:", SUBJECT),
        ("Ref:", "Contract C-4300 / Technical Specification P22-ET-09-000-001-0 / "
                 "Inspection and Test Plan P22-BA-09-000-004 Rev 0"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # --- 1. la obligacion y su historial, con la tabla como respaldo inmediato.
    # No se abre con el faltante: leido primero, parece que ADASA recien se acuerda
    # a dias del ensayo (usuario, 16-Sep).
    add_para(doc,
             "The detailed Factory Acceptance Test procedure for the module is "
             "required by the Technical Specification (P22-ET-09-000-001-0), Section "
             "8.1 - Minimum Scope of Factory Acceptance Tests, and ADASA has raised "
             "it in writing since May:")
    blank(doc)
    add_table(doc, TRACE_HEADERS, TRACE_ROWS)
    blank(doc)

    # --- 2. el estado y su consecuencia. "still" lo lee como persistencia del
    # proveedor. Negrita en la consecuencia, al cierre y no al abrir (CL-24).
    add_segments(doc, [
        ("The procedure has still not been received, and the FAT is planned for "
         "next week. Its approval is a hold point for ADASA at row 7.1 of the "
         "Inspection and Test Plan Rev 0. Rows 7.2 to 7.5 and the FAT Approval "
         "Certificate at row 7.9 are carried out against it. ", False),
        ("The FAT cannot formally open until the procedure is approved.", True),
    ])
    blank(doc)

    # --- 3. el procedimiento del tablero no cubre ese requisito
    add_para(doc,
             "The PLC/LCP FAT Procedure - Hardware (P22-PP-09-000-001) Rev C does "
             "not cover this requirement. Its Section 3 limits it to the hardware of "
             "the control panel and excludes software functional testing and process "
             "logic verification. Section 8.1 requires both at the FAT.")
    blank(doc)

    # --- 4. el pedido, que retoma el alcance de la Section 8.1
    add_segments(doc, [
        ("Please submit the module FAT procedure by Friday 18 September 2026.", True),
        (" It should cover the full minimum scope of Section 8.1: visual, completeness "
         "and dimensional inspection, integrity of the mechanical assembly, dry "
         "functional tests, and the instrumentation and control checks, including "
         "loop checks and the advanced simulation with fault scenarios. It should "
         "also cover the preliminary documentation review, the SEC compliance "
         "check, and the sequence of inspection points of rows 7.1 to 7.9.", False),
    ])
    blank(doc)

    add_para(doc, "I look forward to your comments.")
    blank(doc)
    add_para(doc, "Best regards,")
    blank(doc)
    p = doc.add_paragraph()
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in ["Leader, Infrastructure Engineering",
                 "ADASA, Aguas de Antofagasta S.A.",
                 "lrivera@aguasantofagasta.cl"]:
        add_para(doc, line)

    fijar_idioma(doc, LANG)

    cp = doc.core_properties
    cp.title = SUBJECT
    cp.author = "Luis Rivera Gonzalez"
    cp.last_modified_by = "Luis Rivera Gonzalez"
    cp.company = "Aguas Antofagasta"
    cp.category = "Correo"
    cp.comments = ("Correo urgente del 16-Sep-2026 a BW Water: procedimiento FAT del "
                   "modulo nunca sometido, Hold de la fila 7.1 del ITP Rev 0, "
                   "trazabilidad desde el TM N17 y plazo al viernes 18-Sep.")
    doc.save(OUTPUT_FILE)

    cuerpo = doc.paragraphs[8:-7]   # tras los 6 campos + blanco + "Dear", hasta el cierre
    palabras_cuerpo = sum(len(p.text.split()) for p in cuerpo)
    palabras_tabla = sum(len(c.text.split()) for t in doc.tables
                         for row in t.rows for c in row.cells)
    print("Correo generado: " + OUTPUT_FILE)
    print(f"  palabras del cuerpo (sin encabezado, cierre ni firma): {palabras_cuerpo}")
    print(f"  palabras de la tabla: {palabras_tabla}")


if __name__ == "__main__":
    crear_correo()
