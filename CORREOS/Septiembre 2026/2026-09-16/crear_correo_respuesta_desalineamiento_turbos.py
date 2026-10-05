#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_correo_respuesta_desalineamiento_turbos.py
Respuesta a Eduardo Yamauchi por el desalineamiento de los spools de los
turbocargadores. Reply-All sobre "FW: 25007 Taltal: Project report (Procurement
and Fabrication) WEEK 37" (Yamauchi, lunes 14-Sep 18:41), con Victor Gutierrez
agregado en copia.

POR QUE SALE HOY, MIERCOLES 16

El reporte del 14 cerro con una sola linea: "connection pipe was offset and
require modification". En la reunion de hoy eso resulto ser un desalineamiento
vertical y horizontal de unos 50 mm en spools instalados y ensayados, que se
cortan, resueldan y reensayan, con reparacion al 23-Sep y listo para despacho al
12-Oct. Los planos de fabricacion oficiales nunca se emitieron: el juego de taller
25007-ME-PI-0901-0006 a -0016 se devolvio como no recibido en el TM N30, salio
del Piping Layout en la Rev D y no volvio pese a las exigencias del N37, N38, el
correo del 08-Sep, la reunion del 09-Sep y el N39. Ademas el Request to witness
inspection 008 tiene a Bureau Veritas el 17-Sep en ensayo de alta presion
(09:00 de Penang = 21:00 del 16 en Chile) y el 18-Sep en instalacion de equipos.

DECISIONES DEL USUARIO (16-Sep)

- Reply-All en la cadena del Week 37, respuesta fuerte.
- Encuadre (cuarta pasada): la ingenieria de canerias (Piping Layout) y el modelo
  3D SI se emitieron y cuadraban; lo no emitido son los planos de fabricacion
  oficiales de los spools. Captura del modelo 3D en el cuerpo.
- Version ejecutiva y directa (tercera pasada): 344 palabras, tabla de celdas
  cortas, la duda de los turbos en una oracion y el plazo en dos.
- Clausulas 27 y 43.1 b) de la BAE citadas SIN cifras de dias ni montos
  (INT-08: la Notificacion de Adjudicacion no esta en el repositorio).
- Ningun spool se corta antes de que ADASA reciba los planos.
- La visita de BV del 18 se reencauza a registrar el estado actual.
- El 12-Oct NO se rechaza: "not accepted" se leeria como que ADASA no quiere el
  despacho. Se toma nota, se declara que la prioridad es despachar en cuanto el
  modulo este listo, y la palanca queda como las acciones que permiten el
  Contrato y la BAE, incluida la Clausula 43.1 b).
- Los GA de los turbos (P22-DWG-09-005-012 y -013) se exigen SIN mencionar su
  Codigo 3 del TM N10 ni la Tabla 1 del TM N39, que los listo como aprobados
  por un error del Master Register. Por eso el correo no califica esos planos.

FUERA DEL CUERPO: la minuta del 16-Sep (transcripcion automatica, no oponible;
se cita la conversacion), el paquete desactualizado del inspector, la minuta
del 20-Abr y el correo del 07-May, y el FAT del modulo.

ORTOGRAFIA: en-US. Ingles, primera persona. Document() directo, sin template ADASA.
"""
import os

from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-16_Turbocharger-Spool-Offset-Response.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"
SUBJECT = "RE: FW: 25007 Taltal: Project report (Procurement and Fabrication) WEEK 37"
# Captura del modelo 3D con la zona de los turbos marcada (aportada por el usuario).
IMAGEN_MODELO = os.path.join(SCRIPT_DIR, "2026-09-16_Modelo3D_Zona_Turbos.png")

# Trazabilidad. Cada fila verificada contra su fuente; ver el _Descripcion.md.
TRACE_HEADERS = ("Date", "Record", "Status")
# Version ejecutiva (usuario, 16-Sep): celdas cortas, mismo contenido verificado.
TRACE_ROWS = [
    ("Contract", "Technical Specification, Section 7",
     "High-pressure isometric drawings within 90 days of award. Never submitted"),
    ("22 Apr 2026", "TM N15, Piping Layout Rev B", "Code 2"),
    ("28 Jul 2026", "BW Water email",
     "Fabrication drawings issued internally by BW Water on 24 July. Never issued "
     "as a deliverable"),
    ("5 Aug 2026", "TM N30, Piping Layout Rev C and 3D Model Rev A",
     "Code 2 on both. Shop drawings 25007-ME-PI-0901-0006 to -0016 returned as not "
     "received"),
    ("26 Aug 2026", "TM N36, Piping Layout Rev D and 3D Model Rev B",
     "Code 2 on both. Shop drawings removed from the layout, not resubmitted"),
    ("31 Aug 2026", "TM N37", "Shop drawings required by 3 September"),
    ("3 Sep 2026", "TM N38", "Not received"),
    ("8 Sep 2026", "My email", "Requested again"),
    ("9 Sep 2026", "Coordination meeting", "Committed for 11 September. Not received"),
    ("9 Sep 2026", "TM N39", "High-pressure isometric drawings not received"),
]

# Pedido para antes de la reunion del 17. Texto "1." en parrafo propio para que
# la numeracion sobreviva al pegado en Outlook.
REQUESTS = [
    [("1. Which turbochargers and spools are affected, by line and drawing number, "
      "with the measured offsets.", False)],
    [("2. The shop drawings and isometrics of those spools, as built and as "
      "corrected. ", False),
     ("No spool is to be cut before ADASA receives them.", True)],
    [("3. The root cause, comparing the certified Fedco outline with the delivered "
      "unit and with the 3D model.", False)],
    [("4. Confirmation that both turbochargers match their datasheets Rev 0 "
      "(P22-ET-09-009-007 and -008) in nozzle position, orientation, size and "
      "connection, with their General Arrangement drawings (P22-DWG-09-005-012 "
      "and -013) updated to the units delivered.", False)],
    [("5. The re-test plan for every high-pressure line connected to either "
      "turbocharger, in full, outside the container and witnessed by Bureau "
      "Veritas under row 5.2 of the Inspection and Test Plan.", False)],
    [("6. A day-by-day recovery schedule to ready to ship.", False)],
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
                "Mohd Adnin Bin Zulkaflee; Magdier Arias; Sadeep Irugalbandara; "
                "Nick Huta - BW Water; Victor Gutierrez - ADASA"),
        ("Subject:", SUBJECT),
        ("Ref:", "Contract C-4300 / BAE 12803 / Technical Specification "
                 "P22-ET-09-000-001-0"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # --- 1. lo reportado frente a lo informado hoy
    add_para(doc,
             "Your report of 14 September recorded the turbocharger issue in one line, "
             "as a connection pipe that was offset and required modification. At "
             "today's meeting it turned out to be an offset of about 50 mm on installed "
             "spools. They have to be cut, re-welded and re-tested, and ready to ship "
             "moves to 12 October.")
    blank(doc)

    # --- 1b. lo emitido cuadraba; lo no emitido son los planos de fabricacion.
    # Encuadre del usuario (16-Sep): "never submitted to ADASA" dejaba mal a ADASA.
    add_segments(doc, [
        ("The piping drawings, including the Piping Layout, and the 3D model were "
         "issued and reviewed, and in them the turbocharger connections line up with "
         "their spools, as the model shows below. ", False),
        ("The official spool fabrication drawings were never issued.", True),
    ])
    blank(doc)
    doc.add_picture(IMAGEN_MODELO, width=Inches(6.3))
    p = doc.add_paragraph()
    r = p.add_run("3D model P22-DWG-09-005-007, turbocharger area marked")
    r.italic = True
    aplicar_arial(p, size=9)
    blank(doc)

    # --- 2. trazabilidad
    add_para(doc, "Requests on record:")
    blank(doc)
    add_table(doc, TRACE_HEADERS, TRACE_ROWS)
    blank(doc)

    # --- 3. pedido. La duda de los turbos entra como una oracion y como punto 4;
    # sin calificar el codigo de los GA (decision del usuario).
    # Interetapa: lo entiende el usuario por las fotos (16-Sep). Presiones de las
    # hojas de datos Rev 0 (-008: salida de alimentacion 84,8 bar; -007: 69,53 bar)
    # y de la Line List Rev 1 (09-006: 90 barG diseno, 135 barG prueba).
    add_para(doc,
             "Your report names both turbochargers and today only one was said to be "
             "affected. From the photographs I understand it is the interstage "
             "turbocharger. That makes this more serious, because it runs at the "
             "highest pressure in the module. Its datasheet Rev 0 gives 84.8 bar at the "
             "feed outlet, on lines designed for 90 barG and tested at 135 barG. I also "
             "have no assurance that the units being installed match what was approved.")
    blank(doc)
    add_segments(doc, [
        ("Before tomorrow's meeting at 08:30 Chile time, please send:", True),
    ])
    for segs in REQUESTS:
        add_segments(doc, segs)
    blank(doc)

    # --- 4. Bureau Veritas, Request to witness inspection 008
    add_para(doc,
             "On Request to witness inspection 008, no line connected to either "
             "turbocharger is to be tested on 17 September. On 18 September, "
             "Bureau Veritas should record the as-found condition of both "
             "turbochargers and their spools before any cut.")
    blank(doc)

    # --- 5. plazo y derechos, sin cifras. La fecha no se rechaza: leido como
    # rechazo, parece que ADASA no quiere el despacho (usuario, 16-Sep).
    add_para(doc,
             "I take note of 12 October, and ADASA's priority is that the module ships "
             "as soon as it is ready. This does not waive any right, and ADASA will take "
             "the actions available to it under the Contract and the BAE, including "
             "Clauses 27 and 43.1 b).")
    blank(doc)

    # --- 6. traspaso
    add_para(doc,
             "From tomorrow Victor Gutierrez leads this matter for ADASA. Please "
             "address the report to both of us.")
    blank(doc)

    add_para(doc, "I look forward to your report.")
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
    # core_properties.comments admite maximo 255 caracteres.
    cp.comments = ("Respuesta del 16-Sep-2026 a BW Water: desalineamiento de spools de "
                   "turbos, planos de taller nunca sometidos, pedido para la reunion "
                   "del 17-Sep, visitas BV 17 y 18, reserva Cl. 27 y 43.1 b).")
    doc.save(OUTPUT_FILE)

    cuerpo = doc.paragraphs[8:-7]
    palabras_cuerpo = sum(len(p.text.split()) for p in cuerpo)
    palabras_tabla = sum(len(c.text.split()) for t in doc.tables
                         for row in t.rows for c in row.cells)
    print("Correo generado: " + OUTPUT_FILE)
    print(f"  palabras del cuerpo (sin encabezado, cierre ni firma): {palabras_cuerpo}")
    print(f"  palabras de la tabla: {palabras_tabla}")


if __name__ == "__main__":
    crear_correo()
