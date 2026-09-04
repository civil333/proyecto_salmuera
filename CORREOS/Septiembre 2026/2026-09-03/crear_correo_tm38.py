#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_correo_tm38.py
Correo de cobertura del Transmittal N38 (P22-TM-09-000-038-0), sobre los
submittals 25007-0089 (ENTREGA 89) y 25007-0090 (ENTREGA 90), once documentos.

LO QUE HACE DISTINTO A ESTE CORREO

ENCABEZA CON EL COMPROMISO DE BW WATER, NO CON LA EXIGENCIA DE ADASA. Las dos
minutas lo dejan por escrito y con fecha, y citarlas es mas fuerte que repetir el
pedido propio:

  - Minuta del 26-Ago-2026: "P&ID / Line List: Amendments to correct wrongly
    mentioned line list items; fabrication drawings to be updated and sent by
    Friday, August 28, 2026."
  - Minuta del 01-Sep-2026, Next Arrangements: "Submit the complete documentation
    package (updated P&IDs, line list, ISO drawings) by tomorrow", o sea el 2-Sep.

TRES FECHAS Y NINGUNA CUMPLIDA: viernes 28-Ago y miercoles 2-Sep por compromiso
propio en minuta, y jueves 3-Sep por la exigencia del TM N37.

LA CONSECUENCIA ES OPERATIVA Y ES HOY. Las dos minutas fijan a Bureau Veritas
testificando ensayos el jueves y el viernes, y la del 1-Sep registra que ADASA
necesita "clear mapping of line numbers, pressures, and P&ID alignment to inform
BV". Ese mapeo es justo lo que el P&ID Rev 0 y la Line List Rev 1 dicen distinto.

EL CORREO ES EJECUTIVO: tres parrafos, toda la explicacion en el transmittal. No
reproduce la tabla de doce documentos ni el detalle de los codigos.

NO SE ESCRIBE LA FECHA DEL FAT. La Nota Tecnica P22-NT-09-000-003-0 dejo en disputa
cual ventana gobierna. Se dice "before the Factory Acceptance Test opens".

SIN cifras de multa y SIN invocar el umbral de treinta dias.

DISTRIBUCION: se reproduce la que el usuario fijo al enviar el N37.
  ATENCION: Allan Valentos quedo fuera del N37 y no se ha aclarado si fue
  deliberado. Confirmar antes de enviar.

Ingles. Document() directo, sin template ADASA. Estado: BORRADOR.
"""
import os
import sys

from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-03_Transmittal-N38.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace de descarga de la carpeta COMENTARIOS del N38. Publicar la carpeta,
# pegar el enlace y REGENERAR. Verificar sobre el .docx emitido, no aqui.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19k2hKXFFerUDkcqIAD9rTIMtlMiuCaV/1RLqel9vgvdO6k-x81qjr2m6te-xWOR7-O7kgscxYeg0"
)


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


def add_bullet_lead(doc, lead, rest, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    p.add_run("•  ")
    p.add_run(lead).bold = True
    p.add_run(rest)
    return aplicar_arial(p, size)


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
        ("Date:", "September 3, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi, Fitri Indriyani - BW Water; "
                "Victor Gutierrez, Ronald Pellejero, Jorge Guevara - ADASA"),
        ("CC:", "Jeryl F. Regulacion, Nick Huta, Sadeep Irugalbandara, "
                "David Chee Keat Swee, Andrew Sia, Adzlan Bin Abd Rahim, "
                "Tanya Figueroa, Ahmad Iqbal Bin Azam, Stephane Gehant - BW Water"),
        ("Subject:", "TALTAL - Transmittal N38 - outstanding submittals to be "
                     "closed with documents this week"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # --- Parrafo 1: el compromiso, en sus propias palabras y con sus fechas
    add_segments(doc, [
        ("At the meeting of 26 August BW Water undertook to correct the line list "
         "items and to send the updated P&ID, Line List and fabrication drawings by "
         "Friday 28 August. At the meeting of 1 September the same undertaking was "
         "recorded again: a complete, aligned documentation package, P&IDs, line list "
         "and ISO drawings, to be submitted the following day. ", False),
        ("The package is still not complete.", True),
        (" The fabrication drawings have not been submitted, the P&ID and the Line "
         "List arrived on separate days, and the two do not agree on the size of two "
         "spools.", False),
    ])
    blank(doc)

    # --- Parrafo 2: lo que bloquea hoy, y la exigencia
    add_segments(doc, [
        ("Bureau Veritas is witnessing hydrostatic tests today and tomorrow, and the "
         "mapping of line numbers to test pressures that ADASA has to give the "
         "inspector is precisely what those two documents state differently. ADASA has "
         "determined which of the two is correct and states the binding sizes in the "
         "attached transmittal. ", False),
        ("The outstanding submittals are to be closed with documents this week, as "
         "agreed.", True),
        (" What does not arrive within the week no longer fits a review cycle before "
         "the Factory Acceptance Test opens, and passes to the final dossier.", False),
    ])
    blank(doc)

    # --- Parrafo 3: el adjunto y el veredicto, en una linea
    add_segments(doc, [
        ("Attached is ", False),
        ("Transmittal N38 (P22-TM-09-000-038-0)", True),
        (", on the eleven documents received. ", False),
        ("Verdict: 2 \u2014 Approved as noted. Eight Code 1, three Code 2 and no "
         "Code 3.", True),
        (" Of the twelve documents required by today, seven arrived; Section 3 sets "
         "out the balance and the grounds.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the three annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Ultrasonic Thickness Procedure Rev C",
                    " — P22-BA-09-000-016_C_Ultrasonic_Thickness_CC_ADASA.pdf")
    add_bullet_lead(doc, "HMI Display Screenshot Rev C",
                    " — P22-LI-09-008-016_C_HMI_Display_Screenshot_CC_ADASA.pdf")
    add_bullet_lead(doc, "PLC/LCP FAT Procedure - Hardware Rev C",
                    " — P22-PP-09-000-001_C_PLC_LCP_FAT_Procedure_CC_ADASA.pdf")
    blank(doc)

    add_para(doc, "We remain at your disposal for any clarification.")
    blank(doc)
    add_para(doc, "Best regards,")
    blank(doc)
    p = doc.add_paragraph()
    p.add_run(CONTACTO).bold = True
    aplicar_arial(p)
    for line in ["Infrastructure Engineering Lead - ADASA - Aguas de Antofagasta S.A.",
                 "lrivera@aguasantofagasta.cl"]:
        add_para(doc, line)

    fijar_idioma(doc, LANG)

    # Metadatos explicitos: sin esto Word deja author='python-docx'.
    cp = doc.core_properties
    cp.title = "TALTAL - Transmittal N38 - submittals 25007-0089 and 25007-0090"
    cp.author = "Luis Rivera Gonzalez"
    cp.last_modified_by = "Luis Rivera Gonzalez"
    cp.category = "Correo de cobertura"
    cp.comments = ("Correo de cobertura del Transmittal N38. El saldo del cierre "
                   "consolidado del jueves 3 de septiembre encabeza: siete de doce. "
                   "Cadena de los transmittals.")
    doc.save(OUTPUT_FILE)
    print("Correo generado: " + OUTPUT_FILE)
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")


if __name__ == "__main__":
    crear_correo()
