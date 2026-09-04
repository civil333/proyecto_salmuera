#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Nota Tecnica P22-NT-09-000-003-0
(Clarifications to Secure the Ex-Works Date of 28 September 2026)
usando el template-adasa. Idioma ingles. Destinatario: BW Water.

Codigo:  P22-NT-09-000-003-0
Fecha:   31-Ago-2026 (lunes)
Rev:     0

RESPONDE al aviso de Eduardo Yamauchi del 31-Ago-2026 15:29 hora de Chile, que corre
la System Readiness Shipping Date del 21 al 28 de septiembre alegando clima.

=======================================================================
VERSION SUAVE. Decision del usuario, 31-Ago: NO COMPROMETER LA ENTREGA DEL 28.
=======================================================================

Una primera version disputaba la fecha: diez puntos, citas literales de las
Clausulas 27 y 44, tabla de 44 y 51 dias de desviacion, plazo al viernes 4 y
reserva de la Clausula 49. NO SE EMITIO. El usuario pidio suavizarla porque el
objetivo pasa a ser ASEGURAR el 28 de septiembre, no disputarlo.

EL REENCUADRE QUE HACE QUE SUAVE Y UTIL SEAN LO MISMO: dos de los tres hallazgos
no atacan la fecha, la AMENAZAN. El cronograma del propio proveedor cierra el FAT
el 25 de septiembre y pone el ready-to-ship del 26 al 28, o sea tres dias; y
programa la instalacion de la bomba de alta el 9 y 10 mientras su flete aterriza
el 11. Preguntar por eso PROTEGE el 28.

LA TABLA HACE EL TRABAJO. Las cuatro fechas del propio adjunto, puestas en ORDEN
CRONOLOGICO, muestran solas que la bomba se instala antes de llegar y que quedan
tres dias entre el cierre del FAT y el embarque. Cero palabras acusatorias.

QUE SE RETIRO del documento y quedo SOLO en el registro interno, disponible si la
fecha vuelve a moverse:
  - Que el Project Schedule Rev B del 24-Ago ya daba el pintado del contenedor
    terminado el 21-Ago, al 0% y sin linea base en ninguna de las dos revisiones.
  - El interrogatorio de la Clausula 44 y su regla de aviso en 48 horas.
  - Las citas literales de la Clausula 27 y la tabla de desviaciones.
  - El plazo de ultimatum y la reserva de la Clausula 49.
Todo eso vive en la Bitacora del README, en PRG-41 y en las memorias del proyecto.

LO UNICO CON EFECTO CONTRACTUAL es la frase de la Seccion 4: tomar nota de la
fecha revisada no constituye aceptacion de una nueva fecha contractual ni renuncia
a los derechos del Contrato. SIN numeros de clausula, SIN la palabra multa, SIN
mencionar el 21 de septiembre. Va UNA sola vez y basta: sin ella, el 21 y el 28 se
consolidan por silencio y se pierde la posicion de PRG-07 y PRG-08.

SIN PLAZO DE ULTIMATUM: la respuesta se pide con el proximo reporte semanal y, en
todo caso, antes de que abra el FAT. El ancla es un evento del proyecto, no una
fecha impuesta.

Path al skill: absoluto via ~/.claude/skills/template-adasa segun CLAUDE.md Seccion 3
(Synology no soporta symlinks; NO usar .claude/skills/ del proyecto).

Fuente unica del contenido: P22-NT-09-000-003-0_Ex-Works-Date-Non-Acceptance.md

NOTA: el template numera H1/H2 automaticamente. NO escribir numeros en add_heading.
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    add_simple_table,
)
import docx_metadata  # noqa: E402
from docx import Document  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-NT-09-000-003-0_Ex-Works-Date-Non-Acceptance_ADASA.docx",
)


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_item(doc, tag, body, size=11):
    """Punto numerado: la etiqueta en negrita y el texto seguido."""
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(4)
    run_tag = para.add_run(tag + " — ")
    run_tag.bold = True
    run_tag.font.name = "Arial"
    run_tag.font.size = Pt(size)
    run_body = para.add_run(body)
    run_body.font.name = "Arial"
    run_body.font.size = Pt(size)
    return para


def crear_documento():
    crear_documento_adasa(
        titulo="TECHNICAL NOTE — CLARIFICATIONS TO SECURE THE EX-WORKS DATE "
        "OF 28 SEPTEMBER 2026",
        codigo="P22-NT-09-000-003-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
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
    # PURPOSE
    # =========================================================================
    doc.add_heading("PURPOSE", level=1)
    add_para(
        doc,
        "ADASA has taken note of the revised System Readiness Shipping Date of 28 "
        "September 2026 communicated on 31 August. This Note collects the points "
        "that need to be closed for that date to hold, so that both parties work "
        "from the same sequence over the coming four weeks.",
    )

    # =========================================================================
    # REFERENCE DOCUMENTS
    # =========================================================================
    doc.add_heading("REFERENCE DOCUMENTS", level=1)
    add_simple_table(doc, [
        ("Reference", "Description"),
        ("Recovery Schedule Rev A, 14 July 2026",
         "Ex-works Penang 9 to 10 September 2026"),
        ("P22-BA-09-000-001 Rev B, submittal 25007-0084",
         "Project Schedule issued 24 August 2026"),
        ("Progress Update, 28 August 2026",
         "Attachment to the notice of 31 August 2026"),
        ("Contract C-4300",
         "Supply of the Second Stage RO Brine Module"),
    ])

    # =========================================================================
    # POINTS TO CLOSE
    # =========================================================================
    doc.add_heading("POINTS TO CLOSE", level=1)
    add_para(
        doc,
        "The September sequence projected in the Progress Update, in chronological "
        "order:",
    )
    # La tabla hace el trabajo: en este orden se ve sola la incoherencia.
    add_simple_table(doc, [
        ("Activity", "Projected"),
        ("Equipment airfreight arrival, Penang", "11 September"),
        ("Installation of RO Feed Pump in container", "9 to 10 September"),
        ("Factory Acceptance Test", "15 to 25 September"),
        ("System ready to ship, ex-works Penang", "26 to 28 September"),
    ])

    doc.add_heading("Factory Acceptance Test window", level=2)
    add_item(
        doc, "1.A",
        "Confirm which window governs. Project Schedule Rev B places the Factory "
        "Acceptance Test between 7 and 18 September; the Progress Update places it "
        "between 15 and 25 September. The third-party inspection is booked through "
        "Bureau Veritas Chile with its Malaysia office, and a single date is "
        "needed to secure the inspector for the whole window.",
    )
    add_item(
        doc, "1.B",
        "Confirm the test scope covered within that window and how the three days "
        "between the close of the test and the ready-to-ship date are used, so that "
        "the 28 September is reached with the test complete.",
    )

    doc.add_heading("Equipment arrival and installation sequence", level=2)
    add_item(
        doc, "2.A",
        "Reconcile the arrival of the high pressure pump and the two turbochargers, "
        "projected in Penang on 11 September, with their installation inside the "
        "container, programmed for 9 and 10 September. The order in which those two "
        "activities are held determines whether the pre-assembly sequence closes on "
        "time.",
    )

    doc.add_heading("Shipping information required by ADASA", level=2)
    add_item(
        doc, "3.A",
        "Provide the loading schedule and the vessel closing date, requested on 21 "
        "July 2026. ADASA carries the transport from the BW Water yard under EX "
        "Works and needs both dates to have a vessel booked for the week of 28 "
        "September.",
    )
    add_item(
        doc, "3.B",
        "Confirm the positioning window for the three units: the 40 ft high cube of "
        "the containerised module, the 20 ft general purpose of the loose equipment, "
        "and the 20 ft flat rack of the CIP tank.",
    )

    # =========================================================================
    # SCHEDULE REFERENCES
    # ---- Lo unico del documento con efecto contractual. UNA sola vez, neutra,
    # ---- sin numeros de clausula y sin mencionar el 21 de septiembre.
    # =========================================================================
    doc.add_heading("SCHEDULE REFERENCES", level=1)
    add_para(
        doc,
        "ADASA is working with BW Water so that the 28 September date is met. Taking "
        "note of the revised date does not constitute acceptance of a new contractual "
        "date, nor a waiver of any right under the Contract.",
    )

    # =========================================================================
    # RESPONSE
    # =========================================================================
    doc.add_heading("RESPONSE", level=1)
    add_para(
        doc,
        "ADASA asks for the five points above with the next weekly progress update, "
        "or earlier if the information is available, and in any case before the "
        "Factory Acceptance Test opens.",
    )

    # =========================================================================
    # DOCUMENT HISTORY
    # =========================================================================
    doc.add_heading("DOCUMENT HISTORY", level=1)
    add_simple_table(doc, [
        ("Rev", "Date", "Description"),
        ("0", "31-Aug-2026",
         "First issue — clarifications required to secure the ex-works date of "
         "28 September 2026."),
    ])

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="Technical Note - Clarifications to Secure the Ex-Works Date of "
        "28 September 2026",
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
