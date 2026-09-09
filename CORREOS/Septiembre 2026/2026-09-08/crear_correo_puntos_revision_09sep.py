#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water. Puntos de revision para la reunion de coordinacion del
miercoles 9 de septiembre de 2026, que no se realizo el martes 8.

REPLY-ALL a la cadena de Eduardo Yamauchi "25007 Taltal: Project updates -
08-Sep-2026" (martes 8-Sep 12:41), verificada contra el PDF de la bandeja que vive
en SEMANA 08-09-26. Cadena separada de la de transmittals y de la de Bureau Veritas.

DECISION DEL USUARIO (8-Sep): ADASA mantiene el 28 de septiembre y pregunta en la
reunion. El correo NO declara que la fecha se cae, NO reitera la reserva de la Nota
Tecnica 003 (emitida el 31-Ago, no se repite) y NO fija plazos nuevos.

RESTRICCION HORARIA: la campana de ensayos abre el miercoles 9 a las 09:00 de
Penang, que son las 21:00 del martes 8 en Chile. El correo sale hoy o el Dia 1 corre
sin las respuestas.

--- LA APERTURA: LOS PLANOS DE TALLER, Y QUE BV LOS TENGA ---

Decision del usuario del 8-Sep, tras leer el borrador: el parrafo de apertura no
comunicaba nada. Estaba armado alrededor del historial documental, mezclaba dos
hallazgos tecnicos con una queja de control documental, y nunca nombraba que carrete
estaba en riesgo. Se reemplaza por UN solo asunto y UNA sola peticion, en 83 palabras
contra las 140 de la version anterior: no tenemos los planos de detalle de los
carretes, emitanlos, y que Bureau Veritas los tenga en cada una de las tres jornadas
para poder contrastar cada carrete contra su propio plano antes de presurizarlo.

El Testing Plan identifica cada carrete por su plano: los once de las lineas
originales son 25007-ME-PI-0901-0006 a -0016, devueltos como NO RECIBIDOS en el TM
N30 y nunca sometidos desde entonces, y los seis de los carretes nuevos de baja son
-0023 a -0028, que no aparecen en ningun submittal (el DDSR del 7-Sep lista 73
documentos y ninguno es un 25007-ME-PI).

FUERA DEL CORREO, por decision del usuario: los dos hallazgos de contencion de
presion del TM N30 (derivaciones roscadas austeniticas ANSI 150# y el limite super
duplex a PVC sin quiebre de especificacion) y la coincidencia entre esos carretes y
los ensayos que BV rechazo. Los tres ensayos Unsatisfactory del 20 y 21 de agosto
aplicaron 7,5 barG, que es justo la presion de ensayo del PVC, y uno de ellos es el
CP-SSD-DN80-09-044, uno de los dos carretes que los planos muestran con PVC SCH 80
dentro. Es coincidencia, no causa probada, y sin los planos no se sostiene: por eso
el correo pide los planos y no afirma nada. Se plantea verbalmente en la reunion si
el tema aparece.

--- EL HUECO DE COBERTURA DEL 09-044 ---

Verificado informe contra informe: el BVM-IR006 Rev 01 del 21-Ago rechaza el
CP-SSD-DN80-09-044 en las JUNTAS 03 Y 04, y el BVM-IR011 del 3-Sep reensaya las
JUNTAS 01 Y 02. Son juntas distintas y el Testing Plan da el carrete por terminado
con esa unica fecha. Las juntas que fallaron no aparecen reensayadas en ningun
informe. Va como frase propia despues de la tabla, porque no cabe en sus columnas.

--- EL CRUCE COMPLETO, 17 FILAS CONTRA LA LINE LIST REV 1 ---

Las 17 presiones del plan coinciden con la Line List y las 17 cumplen 1,5 x diseno.
Cero desviaciones de presion. Los desacuerdos son de rotulo, en cuatro filas:

  - Fila 7  plan CP-SSD-DN80-09-049 / LL CP-SSD-DN65-09-049 -> EL PLAN esta bien
  - Fila 11 plan CP-SSD-DN65-09-048 / LL CP-SSD-DN80-09-048 -> EL PLAN esta bien
    (ambos son los diametros vinculantes que ADASA declaro en el TM N38)
  - Fila 9  plan DA-SSD-DN100-09-005 / LL DA-SSD-DN80-09-005 -> LA LINE LIST
    (el BVM-IR011 del 3-Sep tambien la rotula DN80)
  - Fila 16 plan DA-SSD-DN65-09-016 / LL DA-PVC-DN65-09-016 -> LA LINE LIST
    (el plan rotula como super duplex una linea de PVC SCH80)

COBERTURA: el plan omite DA-SSD-DN100-09-050, succion de la bomba de alta, 5 barG de
diseno y 7,5 de ensayo, unica linea de super duplex sin ensayo programado. Y la fila
14 (DA-SSD-DN65-09-009) declara solo el Spool 2.

--- LAS PRESIONES ESTAN ZANJADAS, Y ESO DESCARGA UNA RETENCION ---

El parrafo que lo declara va ANTES de la tabla, por decision del usuario del 8-Sep: si
la tabla abre, el correo se lee como que las presiones estan en cuestion, y no lo
estan. La Line List Rev 1 llego con la columna de hidrostatica en el submittal
25007-0090 y ADASA la aprobo en Codigo 1 en el TM N38, cuya Seccion 2.5 declara que
"the hydrotest column of every line common to Rev 0 is unchanged".

Y hay mas: el TM N35 impuso una retencion sobre TODO el circuito, no solo sobre una
linea. Su texto literal: "No test of the super duplex circuit is to be run until BW
Water confirms in writing the pressure it will apply to each line against that table".
Vive en el PRG-34, CRITICA, vencida el 1 de septiembre. El Testing Plan ES esa
confirmacion escrita, de modo que el correo levanta la retencion del circuito completo
y no solo la de CP-SSD-DN65-09-045.

CONTROL DOCUMENTAL: NO se pide numero de documento para el Testing Plan. Justificarlo
en que "gobierna un punto de detencion" viste de obligacion del ITP una peticion nueva
de ADASA, porque el documento de referencia de la fila 5.2 es el procedimiento
P22-BA-09-000-010, en Codigo 1 desde el TM N35, no un cronograma. Se reitera en cambio
el PRG-35, abierto desde el 20-Ago: el Pressure Test Record Chart sin numero ni
revision, que es el formulario del certificado de presion contra tiempo que exigen las
filas 5.1 y 5.2.

SOBRE LA H DE LA FILA 5.2: el ITP Rev 0 la lleva en la columna C, que es la de ADASA,
y la leyenda define H como que el ensayo se ejecuta con el cliente o el tercero
presente. La presencia NO esta en discusion y por eso va Bureau Veritas, con el
inspector ya confirmado para las tres jornadas. El correo NO la menciona: no aporta y
subiria el tono. Que la presion este acordada y que ADASA deba estar presente son
cosas distintas.

--- REDACCION ---

Perfil de estilo, seccion 11.1 (correspondencia de proyecto): oracion mediana de 18
palabras con percentil 90 en 35, PRIMERA PERSONA y no impersonal, parentesis para la
aclaracion lateral, cero punto y coma, cero em dash, cero ornamento. Sin staccato: no
van tres oraciones seguidas bajo 10 palabras. Estructura ejecutiva (memoria
feedback_correos_ejecutivos): accion incomoda arriba en negrita, tabla compacta
cuando hay varios items, cierre con "We look forward to your comments" y sin proponer
reunion.

FUERA DEL CORREO a proposito: el plazo de entrega vencido y la multa de la Clausula
43.1 letra b; el saldo de jornadas contratadas a Bureau Veritas y sus tarifas; el
registro interno de la reunion del 1 de septiembre, que es un resumen automatico de
ADASA; y los cinco documentos del cierre consolidado del 3-Sep, que viven en la
Seccion 3 del Transmittal N38.

Ingles. Document() directo, sin template ADASA. Estado: ENVIADO el 8-Sep-2026.
"""
import os

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-09-08_Puntos-Revision-Reunion-09Sep.docx")
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
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        _set_lang(r._element.get_or_add_rPr(), lang)


def add_para(doc, text, size=11, space=6):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(space)
    aplicar_arial(p, size)
    return p


def add_segments(doc, segs, size=11, space=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space)
    for text, bold in segs:
        r = p.add_run(text)
        r.bold = bold
        r.font.name = "Arial"
        r.font.size = Pt(size)
    return p


def add_tema(doc, rotulo, texto, size=11):
    """Punto de agenda: rotulo corto en negrita y una sola oracion detras."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(4)
    r0 = p.add_run(rotulo + ": ")
    r0.bold = True
    r0.font.name = "Arial"
    r0.font.size = Pt(size)
    r1 = p.add_run(texto)
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    return p


def espaciador(doc):
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


# Cuatro filas, cruzadas una por una contra la Line List P22-LI-09-009-003 Rev 1
# (Codigo 1 en el TM N38). Las presiones NO entran en la tabla: las diecisiete
# coinciden y eso se dice en prosa, para que la tabla sea solo lo que hay que hacer.
CORRECCIONES = [
    ("Item 9, DA-SSD-DN100-09-005",
     "DA-SSD-DN80-09-005, 120 barG",
     "Correct the size on the record. The test pressure is right."),
    ("Item 16, DA-SSD-DN65-09-016",
     "DA-PVC-DN65-09-016, PVC SCH80",
     "Correct the material on the record. The line and the 3 barG are as approved."),
    ("Not listed",
     "DA-SSD-DN100-09-050, 7.5 barG",
     "The RO high pressure feed pump suction has no test day. Please confirm it."),
    ("Item 14, Spool 2 only",
     "DA-SSD-DN65-09-009, 75 barG",
     "Confirm whether a Spool 1 exists and when it is tested."),
]


def add_tabla_correcciones(doc, size=9):
    headers = ("Testing Plan", "Approved Line List", "Action")
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(size)
    for fila in CORRECCIONES:
        cells = table.add_row().cells
        for i, value in enumerate(fila):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(value)
            run.font.name = "Arial"
            run.font.size = Pt(size)
    return table


def crear_correo():
    doc = Document()
    fmt = doc.styles["Normal"].paragraph_format
    fmt.space_after = Pt(6)
    fmt.line_spacing = 1.0
    for s in doc.sections:
        s.top_margin = Inches(0.6)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    fields = [
        ("Date:", "September 8, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Stephane Gehant, Lokman Hakim Bin Mat, Jeryl F. Regulacion, "
                "Sadeep Irugalbandara, Nick Huta, Magdier Arias - BW Water; "
                "Victor Gutierrez, Jorge Guevara - ADASA"),
        ("Subject:", "RE: 25007 Taltal: Project updates - 08-Sep-2026 - review "
                     "points for the coordination meeting of 9 September"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    espaciador(doc)

    add_para(doc, "Dear Eduardo,")

    # APERTURA. Una oracion corta y una larga.
    add_para(
        doc,
        "Thank you for the Week 36 package. The points on this week's test campaign "
        "need your written answer before the sessions run, starting tonight our time, "
        "and I take the rest at the meeting.")

    # LOS PLANOS DE TALLER. Un solo asunto y una sola peticion, con la exigencia a
    # Bureau Veritas dentro de la misma frase, que es donde tiene efecto.
    add_segments(doc, [
        ("We still do not have the spool fabrication drawings.", True),
        (" The Testing Plan identifies every spool by drawings "
         "25007-ME-PI-0901-0006 to -0016, which were returned as not received at "
         "Transmittal N30 and have not been submitted since. Drawings -0023 to "
         "-0028 have never been submitted either. Please issue the set, and have it "
         "available to Bureau Veritas at each of the three sessions, so the "
         "inspector can check each spool against its own drawing before it is "
         "pressurised.", False),
    ])

    # LAS PRESIONES ESTAN ZANJADAS. Va ANTES de la tabla: si la tabla abre, el correo
    # se lee como que las presiones estan en cuestion, y no lo estan.
    add_segments(doc, [
        ("The test pressures are settled, and the plan applies them correctly.", True),
        (" All seventeen agree with the Line List Rev 1, which ADASA approved at Code "
         "1 at Transmittal N38, and every one of them is 1.5 times design. The plan "
         "is also the written confirmation of the pressure per line that Transmittal "
         "N35 required before any further super duplex test. The hold ADASA placed on "
         "the circuit on 20 August is therefore lifted, and the campaign may run as "
         "planned. The plan carries the binding sizes ADASA declared at Transmittal "
         "N38, so CP-SSD-DN80-09-049 and CP-SSD-DN65-09-048 are rows to correct in "
         "the Line List and not in the plan. The four items in the table below are "
         "corrections to the record, and none of them changes a test pressure.",
         False),
    ])

    # TABLA COMPACTA. Solo lo que hay que hacer.
    add_tabla_correcciones(doc)
    espaciador(doc)

    # HUECO DE COBERTURA DEL 09-044. Las juntas rechazadas el 21-Ago (03 y 04) no
    # son las que reensayo el BVM-IR011 del 3-Sep (01 y 02), y el plan da el carrete
    # por terminado. Se pregunta, no se afirma.
    add_para(
        doc,
        "Spool CP-SSD-DN80-09-044 was rejected on 21 August on joints 03 and 04. The "
        "retest of 3 September covered joints 01 and 02, and the plan shows the spool "
        "complete. Please confirm whether the rejected joints were retested, or give "
        "their day.")

    # PRG-35, abierto desde el 20-Ago. Sin rotulo en negrita: ya hay dos y CL-24
    # dispara sobre el 30 % de los parrafos de prosa.
    add_para(
        doc,
        "The Pressure Test Record Chart still carries no document number and no "
        "revision. It is the form that produces the pressure against time certificate "
        "required by rows 5.1 and 5.2 of the Inspection and Test Plan, and Transmittal "
        "N35 asked for it as a controlled form on 20 August. Three days of records "
        "start on it tomorrow.")

    # AGENDA. Un rotulo por frente, dos o tres oraciones cada uno.
    add_tema(
        doc, "Factory Acceptance Test",
        "which window governs, since Rev B places the test from 7 to 18 September "
        "and the Progress Update from 15 to 25 (point 1.A of Technical Note "
        "P22-NT-09-000-003-0). The issue date of the module FAT procedure required "
        "by the Technical Specification (P22-ET-09-000-001-0), Section 8.1 - "
        "Minimum Scope of Factory Acceptance Tests. Its approval is a hold point of "
        "row 7.1 of the Inspection and Test Plan and our review runs seven working "
        "days, so that date sets the earliest start. And the minimum scope with the "
        "order of the hold and witness points.")
    add_tema(
        doc, "Assembly and equipment",
        "the day by day sequence from 12 September to ready to ship, with assembly "
        "of spools, valves, instruments and electrical at zero in the Week 36 "
        "report. How the arrival of the high pressure pump and the two "
        "turbochargers on 10 September fits their installation on 9 and 10. And "
        "which of the two CIP tank statements governs, the one in the report or the "
        "one in the tracker.")
    add_tema(
        doc, "Schedule and shipment",
        "the updated project and fabrication schedules, both absent from this "
        "package. The Milestone Tracker still carries the Factory Acceptance Test "
        "baseline of 13 to 18 August and an ex-works date of 10 September in the "
        "Actual column. And the loading schedule with the vessel closing date, plus "
        "the membrane shipping date.")
    espaciador(doc)

    add_para(doc, "We look forward to your comments.")

    add_para(doc, "Best regards,", space=0)
    espaciador(doc)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in [
        "Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
        "lrivera@aguasantofagasta.cl",
    ]:
        add_para(doc, line, space=0)

    fijar_idioma(doc, LANG)

    # Metadatos explicitos: sin esto Word deja author='python-docx'.
    cp = doc.core_properties
    cp.title = "TALTAL - Review points for the coordination meeting of 9 September"
    cp.author = "Luis Rivera Gonzalez"
    cp.last_modified_by = "Luis Rivera Gonzalez"
    cp.subject = ("Taltal SWRO - Review points arising from the Week 36 package "
                  "for the coordination meeting of 9 September 2026")
    cp.category = "Correo de coordinacion"
    cp.comments = ("Puntos de revision para la reunion del miercoles 9 de "
                   "septiembre, derivados del paquete semanal Week 36 y del cruce "
                   "del Testing Plan del Request 007 contra la Line List Rev 1. "
                   "Reply-All a la cadena Project updates - 08-Sep-2026.")
    doc.save(OUTPUT_FILE)
    print("Correo generado: " + OUTPUT_FILE)


if __name__ == "__main__":
    crear_correo()
