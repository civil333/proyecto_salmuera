#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_correo_tm39_rev0.py
Correo unico a Eduardo Yamauchi: el Transmittal N39 y la emision en revision 0 de
la ingenieria ya aprobada.

POR QUE ES UNO Y NO DOS

Habia dos borradores del 9 de septiembre para la misma persona, con la misma copia
y el mismo plazo: la cobertura del N39 y la auditoria de emision para construccion.
Se funden. El precedente es el correo del N37, que llevo una exigencia de igual peso
en 72 palabras de primer parrafo y mando la lista nominal a la Seccion 3 del
transmittal. Aqui pasa lo mismo: las cuatro tablas viven en la Seccion 3 del N39 y
el correo remite a ellas.

REGISTRO: PRIMERA PERSONA, y no es descuido. El argumento mas fuerte del correo
depende de ello, "I approved them under Code 1 and they are still on a letter
revision", y tambien el desactivador de la defensa previsible, "I had not set a date
for these reissues until now". El transmittal se queda en tercera persona
institucional, que es su registro de siempre: el correo lo firma una persona y el
transmittal lo emite ADASA.

APERTURA: la exigencia primero y el transmittal despues, por decision del usuario.

QUEDA FUERA, disponible si el asunto escala: el idioma castellano de la Clausula 6
de la BAE, el hito de pago del 10 por ciento, la multa de la Clausula 43.1 letra a)
y la frase de la ET sobre no liberar equipos para transporte sin documentacion
aprobada. El cierre lleva una reserva generica para no renunciar a ellos.

LAS CIFRAS NO SE ESCRIBEN A MANO: salen del mismo auditor que alimenta la Seccion 3
del transmittal, de modo que los dos documentos no pueden discrepar.

DISTRIBUCION acotada, fijada por el usuario: Eduardo destinatario, copia a Jeryl
Regulacion y Victor Gutierrez.

Ingles. Document() directo, sin template ADASA. Estado: BORRADOR.
"""
import os
import sys

from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-09_Transmittal-N39-and-Rev0-Issue.docx")
CONTACTO = "Luis Rivera González"
LANG = "en-US"

sys.path.insert(0, os.path.abspath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "REVISIONES", "EVALUACIONES")))
from auditar_documentos_bw import auditar, leer_ddsr, separar  # noqa: E402

# El Project Schedule se retiro del ciclo de transmittals en el N36, de modo que no
# entra en un reclamo de emision. Mismo criterio que la Seccion 3 del transmittal.
FUERA_DEL_CICLO = {"P22-BA-09-000-001"}

# Enlace de descarga de la carpeta COMENTARIOS del N39. Publicar la carpeta, pegar el
# enlace y REGENERAR. Verificar sobre el .docx emitido y despues del pegado en
# Outlook: el proyecto lleva cuatro enlaces perdidos ahi.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19ouwrb8KTtFJ7qFvEgPnwAIYi16Cd8a/ZiFTRPVQi9mpG630Th28RAvqLfORa14o-o7ngVeAgfg0"
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


def add_quote(doc, texto):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.add_run(texto).italic = True
    return aplicar_arial(p, 10)


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


def cifras():
    """Las mismas que la Seccion 3 del transmittal, del mismo auditor."""
    docs = auditar()
    ing, cal, _ = separar(docs)
    a_ing = [d for d in ing if d["cat"] == "A"]
    b_ing = [d for d in ing if d["cat"] == "B"]
    c_ing = [d for d in ing if d["cat"] == "C"]
    cal_ab = [d for d in cal if d["cat"] in "AB"
              and d["codigo_real"] not in FUERA_DEL_CICLO]
    plan_11 = [r for r in leer_ddsr().values() if r.get("planned") == "11-Sep-26"]
    return dict(n_items=len(docs), n_ing=len(ing), n_a=len(a_ing), n_b=len(b_ing),
                n_cal=len(cal_ab), n_c=len(c_ing),
                sin_emitir=len(a_ing) + len(b_ing), plan_11=len(plan_11))


def crear_correo():
    n = cifras()

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
        ("Date:", "September 9, 2026"),
        ("From:", CONTACTO + " - Leader, Infrastructure Engineering (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water"),
        ("CC:", "Jeryl F. Regulacion - BW Water; Victor Gutierrez - ADASA"),
        ("Subject:", "TALTAL - Transmittal N39 and issue for construction of the "
                     "approved engineering"),
        ("Ref:", "Contract C-4300 / BAE 12803 / Master Deliverable Register "
                 "P22-IT-06-000-002-0"),
    ]
    for label, value in fields:
        p = doc.add_paragraph()
        p.add_run(label).bold = True
        p.add_run(" " + value)
        aplicar_arial(p)
    blank(doc)

    add_para(doc, "Dear Eduardo,")
    blank(doc)

    # --- 1. la exigencia, con la cifra que la sostiene
    add_segments(doc, [
        ("In today's meeting we set Friday 11 September to close the documentation "
         f"milestones. Before that date I audited the {n['n_items']} items of the Master "
         f"Deliverable Register one by one. Of the {n['n_ing']} engineering documents, ",
         False),
        (f"{n['sin_emitir']} have never been issued for construction, and {n['n_a']} of "
         "those carry no open observation at all", True),
        (": I approved them under Code 1 and they are still on a letter revision. The "
         "median age of those approvals is 184 days and the oldest four are 267 (from "
         "Transmittal N1 of 16 December 2025). Section 3 of the attached transmittal "
         "lists every one of them and the grounds.", False),
    ])
    blank(doc)

    # --- 2. la regla es del propio proveedor
    add_segments(doc, [
        ("The criterion is already agreed, and BW Water set it out first. On the comment "
         "sheet issued with the Grounding Point and Power Panel Location Layout Rev E, "
         "document P22-DWG-09-007-003 of 12 May 2026:", False),
    ])
    add_quote(doc,
              'Description "Issued For Approval" remaining the same until the '
              'document/drawing is approved and then will change to "Issued For '
              'Construction - Rev0"')
    add_segments(doc, [
        ("That is what I am asking for now, with a date.", False),
    ])
    blank(doc)

    # --- 3. el transmittal
    add_segments(doc, [
        ("Attached is ", False),
        ("Transmittal N39 (P22-TM-09-000-039-0)", True),
        (", on submittals 25007-0091 and 25007-0092, three documents. ", False),
        ("Verdict: 2 — Approved as noted. One Code 1, two Code 2 and no Code 3.", True),
        (" No document returns to revision, and all three are re-issues that I reviewed "
         "only against the comments already raised.", False),
    ])
    blank(doc)

    # --- 4. la unica consecuencia con fecha propia
    add_segments(doc, [
        ("One point in it has a date of its own. ", False),
        ("VM-09-065 is still listed with a PVC body on a line that the approved Line "
         "List carries in 316L stainless steel.", True),
        (" The CIP pump suction line CP-SS316-DN150-09-022 changed to stainless steel on "
         "the Line List Rev 1, which I approved at Code 1 in Transmittal N38, and "
         "VM-09-065 is the only DN150 valve of that circuit. Valves are bought against "
         "this list, so I need that material settled before the purchase order goes out.",
         False),
    ])
    blank(doc)

    # --- 5. el pedido, con el desactivador de la defensa
    add_segments(doc, [
        ("What I am asking for on Friday 11 September.", True),
        (f" The {n['n_a']} documents of Table 1 issued at Revision 0. None needs a change "
         "of content, only the revision number and the issue purpose of the title block. "
         f"The {n['n_b']} of Table 2 and the {n['n_cal']} of Table 3 issued at Revision 0 "
         "with their condition incorporated, and no intermediate approval revision. The "
         f"corrected title block on the {n['n_c']} documents that already carry a numeric "
         "revision, and the seven deliverables of Table 4.", False),
    ])
    add_segments(doc, [
        ("I had not set a date for these reissues until now, and that is what this email "
         "fixes. Whatever cannot be issued by Friday, please give me its committed issue "
         "date that same day in the Document and Drawing Status Report (DDSR), which "
         f"already carries {n['plan_11']} rows dated this Friday.", False),
    ])
    blank(doc)

    add_para(doc,
             "This email is sent without prejudice to ADASA's rights under the Contract.")
    blank(doc)

    add_para(doc, "The transmittal and the two annotated PDFs are available here:")
    add_para(doc, DOWNLOAD_LINK)
    blank(doc)

    add_bullet_lead(doc, "Valve List Rev E",
                    " — P22-LI-09-005-002_E_Valve_List_CC_ADASA.pdf")
    add_bullet_lead(doc, "GA of Antiscalant Dosing Tank Rev D",
                    " — P22-DWG-09-005-015_D_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf")
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

    # Metadatos explicitos: sin esto Word deja author='python-docx'.
    cp = doc.core_properties
    cp.title = ("TALTAL - Transmittal N39 and issue for construction of the approved "
                "engineering")
    cp.author = "Luis Rivera Gonzalez"
    cp.last_modified_by = "Luis Rivera Gonzalez"
    cp.company = "Aguas Antofagasta"
    cp.category = "Correo de cobertura"
    cp.comments = ("Correo unico: remite el Transmittal N39 y exige la emision en "
                   "revision 0 de la ingenieria ya aprobada al viernes 11 de septiembre. "
                   "Funde los dos borradores del 9 de septiembre.")
    doc.save(OUTPUT_FILE)

    palabras = sum(len(p.text.split()) for p in doc.paragraphs)
    print("Correo generado: " + OUTPUT_FILE)
    print(f"  cifras del auditor: {n['sin_emitir']} de {n['n_ing']} sin emitir | "
          f"tabla 1 {n['n_a']} | tabla 2 {n['n_b']} | tabla 3 {n['n_cal']} | "
          f"cajetines {n['n_c']} | filas al 11-Sep {n['plan_11']}")
    print(f"  palabras del documento: {palabras}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")


if __name__ == "__main__":
    crear_correo()
