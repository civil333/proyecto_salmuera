#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de cobertura del Transmittal N37 (P22-TM-09-000-037-0), submittals
25007-0086, 25007-0087 y 25007-0088 (ENTREGAS 86 y 88). Cadena de los
transmittals.

🔴 LO QUE HACE DISTINTO A ESTE CORREO: la exigencia de cierre documental
consolidado al JUEVES 3 DE SEPTIEMBRE DE 2026 va como PRIMER PARRAFO, no al
final. Instruccion del usuario del 31-Ago-2026: por el estado de la construccion
y el atraso declarado, BW Water no puede seguir enviando documentos sueltos a
medida que construye, y esto debe quedar clarisimo y de manera tajante en el
correo y en el transmittal.

El correo NO reproduce la lista de doce documentos: remite a la Seccion 3 del
transmittal, que la trae completa con su origen. Reproducirla aqui duplicaria el
adjunto y diluiria la orden.

🔴 NO SE ESCRIBE LA FECHA DEL FAT. La Nota Tecnica P22-NT-09-000-003-0, emitida
el 31-Ago por la otra cadena, pregunta cual ventana gobierna: el Project Schedule
Rev B la pone del 7 al 18 de septiembre y el Progress Update del 28-Ago del 15 al
25. Se dice "before that test", que es cierto con cualquiera de las dos. Las
unicas fechas de septiembre del cuerpo son el plazo de la exigencia (3) y los
vencimientos de la Clausula 37.2 (7 y 8).

SE INCLUYE, porque anticipa la excusa mas probable: el O&M Manual ya no tiene
dependencia. Cerraron en Rev 0 y Codigo 1 en el TM N34 los dos documentos de
control que lo detenian.

FUERA DEL CORREO, a proposito: cifras de multa y el umbral de treinta dias
—INT-08 sigue abierto y la Notificacion de Adjudicacion no esta en el
repositorio—; el desplazamiento del embarque, que va por la cadena de la Nota
Tecnica; y el detalle tecnico de cada observacion, que es contenido del
transmittal y de los cinco CC_ADASA.

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
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-08-31_Transmittal-N37.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

# Enlace de descarga de la carpeta del N37. Publicar la carpeta, pegar el enlace
# y REGENERAR. Verificar SIEMPRE sobre el .docx emitido, no sobre este script.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19hY5AfCDswSNULyibAyAkLm46YnKjSb/Ndsy8yqJtB5k0V1z0TwcYNx4AiD_bgc--V7OAzaBpeA0"
)


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
        ("Date:", "August 31, 2026"),
        ("From:", CONTACTO + " - Infrastructure Engineering Lead (ADASA)"),
        ("To:", "Eduardo Yamauchi, Allan Valentos - BW Water"),
        ("CC:", "Fitri Indriyani, Stephane Gehant, Jeryl F. Regulacion, Andrew Sia - "
                "BW Water; Victor Gutierrez, Jorge Guevara, Ronald Pellejero - ADASA"),
        ("Subject:", "TALTAL - Transmittal N37 - submittals 25007-0086 to 25007-0088 "
                     "and consolidated close-out of outstanding documentation"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # --- LA EXIGENCIA, PRIMERO ---
    # El correo es carta de cobertura: NO repite la sustancia del transmittal.
    # Los tres hechos que sostienen la exigencia, el levantamiento de la
    # dependencia del O&M Manual y los vencimientos de la Clausula 37.2 viven en
    # el adjunto y salieron de aqui por instruccion del usuario del 31-Ago-2026.
    # Lo unico que se repite a proposito es la orden, porque tiene que leerse sin
    # abrir el adjunto.
    add_segments(doc, [
        ("BW Water is to stop submitting documents one at a time as construction "
         "proceeds.", True),
        (" Every outstanding engineering document, drawing and procedure is to reach "
         "ADASA in a single consolidated submission, ", False),
        ("no later than Thursday 3 September 2026", True),
        (". Section 3 of the attached transmittal lists the twelve documents and the "
         "grounds. ", False),
        ("What arrives after Thursday no longer fits a review cycle before the Factory "
         "Acceptance Test opens, and passes to the final dossier.", True),
    ])
    blank(doc)

    add_segments(doc, [
        ("Attached is ", False),
        ("Transmittal N37 (P22-TM-09-000-037-0)", True),
        (", on submittals 25007-0086 to 25007-0088, seven documents. ", False),
        ("Verdict: 3 — To be revised. Two Code 1, four Code 2 and one Code 3.", True),
        (" The Code 3 is the PLC/LCP FAT Procedure Rev B, the record of a panel test "
         "run on 3 to 5 August without notice to ADASA.", False),
    ])
    blank(doc)

    add_para(doc, "The transmittal and the five annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Liquid Penetrant Examination Procedure Rev C",
                    " — P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf")
    add_bullet_lead(doc, "Radiography Examination Procedure Rev C",
                    " — P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf")
    add_bullet_lead(doc, "PLC/LCP Schematic Diagram Rev B",
                    " — P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf")
    add_bullet_lead(doc, "Instrument Location Layout Rev D",
                    " — P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf")
    add_bullet_lead(doc, "PLC/LCP FAT Procedure - Hardware Rev B",
                    " — P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf")
    blank(doc)

    add_para(doc, "We remain at your disposal for any clarification.")
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
        title="TALTAL - Transmittal N37 - submittals 25007-0086 to 25007-0088",
        author="Luis Rivera Gonzalez",
        language="en-US",
        comments=("Correo de cobertura del Transmittal N37 y exigencia de cierre "
                  "documental consolidado al jueves 3 de septiembre. Cadena de los "
                  "transmittals."),
    )
    doc.save(OUTPUT_FILE)
    print("Correo generado:", OUTPUT_FILE)
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")


if __name__ == "__main__":
    crear_correo()
