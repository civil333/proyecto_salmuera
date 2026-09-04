#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water + Bureau Veritas sobre el informe de ensayo hidrostatico
del 20-Ago-2026 (`Taltal Hydrotest Report BV W 20Aug.pdf`, recibido ese mismo dia).
Reply-all al hilo del Request to witness inspection 004: cadena de las jornadas de
inspeccion, SEPARADA de la de transmittals. El Transmittal N35 va por su propia
cadena y su propio correo, por decision del usuario.

EL EJE: el informe trae dos ensayos y solo uno esta bien.

  Spool 2, `DA-SSD-DN100-09-003`, ensayado a 90 barG. La Line List P22-LI-09-009-003
  Rev 0 le asigna exactamente 90 barG. Escalonado 45 -> 67,5 -> 90, retencion de
  treinta minutos, caida nula, manometros de rango 0 a 160 bar. Conforme, y se
  dice asi.

  Spool 1, `DA-SSD-DN100-09-014`, ensayado a 7,5 barG con manometros de rango
  0 a 16 bar. Ninguna de las once lineas de super duplex del proyecto se ensaya a
  esa presion: el rango va de 75 a 135 barG. Y ese TAG no existe en la Line List;
  el correlativo 09-014 es `CP-SSD-DN100-09-014`, hidrostatica 120 barG.

POR QUE SE PREGUNTA Y NO SE IMPUTA (regla anti-invencion). El hecho de la presion
esta verificado y es duro, pero la identidad de la linea no: puede ser un TAG mal
transcrito de otra linea. El correo declara lo que el registro dice, lo contrasta
con la Line List aprobada, y pide identificar la linea antes de exigir la repeticion.
Si resulta ser super duplex, el ensayo no la califica.

LO QUE SE RECONOCE PRIMERO, y no es cortesia: Bureau Veritas asistio y firmo los
dos ensayos y el Inspection Request. Es la primera jornada de la serie con
constancia completa de asistencia, y cierra por los hechos el reclamo del 17-Ago
sobre pruebas ejecutadas sin testigo. Abrir con eso hace mas dificil de rebatir lo
que viene despues.

EL GRAFICO PRESION-TIEMPO SI SE PRODUCE. Las hojas de adjuntos traen el
`PRESSURE TEST RECORD CHART` con escalones, horas y firmas. Eso precisa la
observacion abierta sobre el procedimiento `P22-BA-09-000-010`: lo que falta no es
la practica sino el control documental de ese formulario, que no tiene numero ni
revision. Va como ultima vinieta, sin abrir aqui el veredicto del transmittal.

FUERA DEL CORREO, a proposito:
  - El veredicto del Transmittal N35 sobre los cinco procedimientos de la ENTREGA 81.
    Otra cadena y otro correo.
  - El plazo de entrega vencido el 03-Ago y la multa de la Clausula 43.1 letra b.
  - La hidrostatica de baja presion y la del RO Vessel que el Request 003 recorto:
    siguen en PRG-13 y no son el eje de hoy.
  - El formato manuscrito del grafico y la ausencia de Report No. en los formularios:
    aseo documental, se pide dentro de la correccion del registro y no como
    observacion propia.

Excepcion de correo conjunto: se nombra a BW Water aunque Bureau Veritas este entre
los destinatarios, igual que en los correos del 14 y del 17 de agosto de esta misma
cadena.

Ingles. Document() directo, sin template ADASA. Estado: BORRADOR.
"""
import os
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-20_Hydrotest-Report-20-Aug.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


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


def add_para(doc, text, size=11):
    p = doc.add_paragraph(text)
    aplicar_arial(p, size)
    return p


def add_segments(doc, segs, size=11):
    p = doc.add_paragraph()
    for text, bold in segs:
        r = p.add_run(text)
        r.bold = bold
        r.font.name = "Arial"
        r.font.size = Pt(size)
    return p


def add_bullet_lead(doc, lead, rest, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    r0 = p.add_run("•  " + lead)
    r0.bold = True
    r0.font.name = "Arial"
    r0.font.size = Pt(size)
    r1 = p.add_run(rest)
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    return p


def blank(doc):
    doc.add_paragraph()


# Las once lineas de super duplex de la Line List P22-LI-09-009-003 Rev 0, aprobada en
# Codigo 1 en el TM N29. Relacion 1,5 exacta entre diseno y prueba en las 34 filas.
# ESPEJO EXACTO de la tabla del Transmittal N35, subseccion 2.1: si una cambia, la otra
# tambien, o el proveedor recibe dos tablas distintas el mismo dia.
PRESSURE_TABLE = [
    ("DA-SSD-DN100-09-003", "RO HP Feed Pump Discharge", "60", "90"),
    ("DA-SSD-DN100-09-004", "1st Stage RO Feed", "80", "120"),
    ("DA-SSD-DN80-09-005", "1st Stage RO Reject", "80", "120"),
    ("DA-SSD-DN80-09-006", "2nd Stage RO Feed", "90", "135"),
    ("DA-SSD-DN65-09-007", "2nd Stage RO Reject", "90", "135"),
    ("DA-SSD-DN65-09-008", "Interstage Turbocharger Brine Outlet", "50", "75"),
    ("DA-SSD-DN65-09-009", "Feed Turbocharger Brine Outlet", "50", "75"),
    ("CP-SSD-DN100-09-014", "CIP Feed to 1st Stage RO", "80", "120"),
    ("CP-SSD-DN80-09-015", "CIP Feed to 2nd Stage RO", "90", "135"),
    ("CP-SSD-DN80-09-044", "1st Stage CIP Reject Out", "80", "120"),
    ("CP-SSD-DN65-09-045", "2nd Stage CIP Reject Out", "90", "135"),
]


def add_table_pressures(doc, size=10):
    headers = ("Line", "Description", "Design barG", "Test barG")
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(size)
    for row in PRESSURE_TABLE:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(value)
            run.font.name = "Arial"
            run.font.size = Pt(size)
    return table


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
        ("Date:", "August 20, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Mohd Adnin Bin Zulkaflee, Muhammad Fadhil Bin Abdul Wahid, "
                "Eduardo Yamauchi - BW Water"),
        ("CC:", "Stephane Gehant, Magdier Arias, Lokman Hakim Bin Mat - BW Water; "
                "Ahmad Hazwan, Carlo Montecinos, Wan Mohd Adli W Yahya, Emylia Rosli "
                "- Bureau Veritas; Victor Gutierrez, Jorge Guevara, Ronald Pellejero "
                "- ADASA"),
        ("Subject:", "RE: 25007 TALTAL - Request to witness inspection 004 - "
                     "hydrostatic test report of 20 August"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Adnin, Fadhil,")
    blank(doc)

    # VERSION EJECUTIVA. Cuatro parrafos, tabla y cinco viñetas. El correo dice el
    # hecho y la peticion; la fundamentacion documental completa vive en el analisis
    # interno y en el Transmittal N35.
    add_segments(doc, [
        ("We have received today's hydrostatic test report. The inspector attended and "
         "signed both records and the Inspection Request, which settles the point we "
         "raised on 17 August. ", False),
        ("Spool 2 is accepted:", True),
        (" line DA-SSD-DN100-09-003 tested at 90 barG, held thirty minutes with no "
         "pressure drop. Its design pressure is 60 barG on the approved Line List "
         "(P22-LI-09-009-003) Rev 0, and the test pressure is 1.5 times design, so "
         "90 barG is the correct value for that line.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Spool 1 is not.", True),
        (" It is recorded as line DA-SSD-DN100-09-014 and was tested at ", False),
        ("7.5 barG", True),
        (", on two gauges of 0 to 16 bar range. No super duplex line on this module "
         "tests below 75 barG. And that tag does not exist in the Line List "
         "(P22-LI-09-009-003) Rev 0: the line numbered 09-014 is CP-SSD-DN100-09-014, "
         "80 barG design and 120 barG test.", False),
    ])
    blank(doc)

    # Enfasis pedido por el usuario: la regla NO es una exigencia nueva de ADASA. Vive
    # en documentos aprobados, y el propio procedimiento de presion los cita por codigo
    # y revision. Nombrarlos con codigo es lo que hace la exigencia irrebatible.
    add_segments(doc, [
        ("None of this is new, and your own pressure test procedure says where it "
         "lives.", True),
        (" Clause 5.5.12 of the HP and LP Pressure Test Procedure "
         "(P22-BA-09-000-010) states in a single sentence that HP piping will test to "
         "135 bar and LP to 7.5 bar, and that the testing pressure will refer to the "
         "approved Line List. It names that Line List by number and revision: "
         "P22-LI-09-009-003 Rev 0, which prescribes six different values, not two. The "
         "1.5 factor appears nowhere in the procedure.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Both documents are approved.", True),
        (" The Line List (P22-LI-09-009-003) Rev 0 was issued by BW Water and approved "
         "by ADASA at Code 1 in Transmittal N29 of 21 July. The Inspection and Test "
         "Plan (P22-BA-09-000-004) Rev 0, approved at Code 1 in Transmittal N26, sets "
         "the test pressure of the high pressure system at 1.5 times design pressure in "
         "its row 5.2, as does row 5.2 of the Inspection and Testing Base Plan "
         "(P22-IT-09-000-001-0). The table below is those documents, not a new "
         "requirement.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("The exposure runs both ways.", True),
        (" Testing below the value leaves the test unqualified, which is what happened. "
         "Testing every super duplex line at 135 bar would over-pressurise seven of the "
         "eleven: the two turbocharger brine outlets at 2.7 times their design "
         "pressure, on the discharge of SIP-09-001 and SIP-09-002.", False),
    ])
    blank(doc)

    add_segments(doc, [
        ("Each line tests at 1.5 times its own design pressure, per P22-LI-09-009-003 "
         "Rev 0:", True),
    ])
    add_table_pressures(doc)
    blank(doc)

    add_para(doc, "What we ask for:")
    add_bullet_lead(
        doc, "No further super duplex test until you confirm each line's pressure in "
             "writing",
        " against P22-LI-09-009-003 Rev 0. Row 5.2 of the Inspection and Test Plan is a "
        "hold point.")
    add_bullet_lead(
        doc, "Identify Spool 1 by its Line List tag",
        ". If it is super duplex, repeat the test at the listed pressure, with written "
        "notice and the inspector present.")
    add_bullet_lead(
        doc, "Correct the record of 20 August",
        ", including checklist item 5 on gauge range against required test pressure.")
    add_bullet_lead(
        doc, "State the design pressure on every test record",
        ", alongside the test pressure. Form AQ-QAM-F018 has no such column.")
    add_bullet_lead(
        doc, "Send the plan for the remaining ten lines",
        ", with dates and pressures, and issue the Pressure Test Record Chart as a "
        "controlled form with a document number and revision.")
    blank(doc)

    add_segments(doc, [
        ("Please reply by ", False),
        ("tomorrow, Friday 21 August", True),
        (", so that any repeat test can still run inside the window now open in "
         "Penang.", False),
    ])
    blank(doc)

    add_para(doc, "Best regards,")
    blank(doc)

    p = doc.add_paragraph()
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in [
        "Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line)

    fijar_idioma(doc, LANG)

    docx_metadata.apply_core_properties(
        doc,
        title="Taltal - Hydrostatic test report of 20 August - Spool 1 test pressure",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Taltal SWRO - Hydrostatic testing, test pressure against approved "
                "Line List",
        comments="Aguas de Antofagasta S.A.",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas Antofagasta")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
