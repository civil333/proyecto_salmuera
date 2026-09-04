#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de respuesta de ADASA a la respuesta de BW Water al Mitigation Plan.

v3 (REPLICA): respuesta directa, punto por punto, a la respuesta de BW Water
del 01-Jun-2026 (RESPUESTA BW WATERS/correo respuesta plan de mitigacion.pdf).
Cada bloque reacciona a lo que BW Water efectivamente respondio en sus
secciones 3.1-3.6. Se conserva arriba la exigencia del recovery schedule para
manana (Ma 02-Jun).

- Reply-To al thread de BW Water del 01-Jun (subject "RE: 25007 Taltal - Mitigation Plan").
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Postura: firme en ASME (Change Order + hito condicionado) y en el rechazo del
  30% FEDCO; reservada/flexible en FAT->SAT (a la espera de la tabla del 15-Jun).
- Fuente unica del cuerpo: 2026-06-01_Respuesta-Mitigation-Plan_Descripcion.md
"""

import os

from docx import Document
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-06-01_Respuesta-Mitigation-Plan.docx")
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def add_para(doc, text, size=11):
    para = doc.add_paragraph(text)
    aplicar_arial(para, size)
    return para


def add_segments(doc, segments, size=11):
    """Parrafo con segmentos (texto, bold?). segments = [(text, bool), ...]."""
    para = doc.add_paragraph()
    for text, bold in segments:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def add_bullet(doc, text, size=11):
    # 'List Bullet' style no existe en Document() vacio -> guion + sangria manual.
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.3)
    run = para.add_run(f"–  {text}")
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def add_block(doc, label, body):
    """Bloque de replica: rotulo en negrita + cuerpo en regular, mismo parrafo."""
    return add_segments(doc, [(label + " ", True), (body, False)])


def blank(doc):
    doc.add_paragraph()


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # =========================================================================
    # HEADER
    # =========================================================================
    fields = [
        ("Date:", "June 1, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Andrew Sia, Victor Gutierrez, Jeryl F. Regulacion, "
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Mauricio Vallejos, "
            "Jorge Valdes, Tanya Figueroa, Allan Valentos, Sadeep Irugalbandara, "
            "Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, "
            "Adzlan Bin Abd Rahim, Stephane Gehant, Shane Banks, Fadey Kassim",
        ),
        ("Subject:", "RE: 25007 Taltal - Mitigation Plan"),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / "
            "Technical Note P22-NT-09-000-001-0 (25-May-2026) / "
            "BW Water response 1-Jun-2026 / "
            "Mitigation Plan + Recovery Schedule 22-May-2026",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # =========================================================================
    # CUERPO (v3 - replica punto por punto a la respuesta BW Water)
    # =========================================================================
    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_para(
        doc,
        "Thank you for your response of 1-Jun-2026, which, as you note, "
        "addresses only part of the points raised in Technical Note "
        "P22-NT-09-000-001-0. Our reply to each item follows. One request comes "
        "first and overrides the rest:",
    )
    blank(doc)

    add_segments(
        doc,
        [
            ("We need, by tomorrow Tuesday 2-Jun-2026 at the latest, an updated "
             "recovery schedule that shows the real delay situation,", True),
            (" with vendor-confirmed dates and consistent across all your "
             "documents. The 22-May schedule no longer holds against your own "
             "answers below:", False),
        ],
    )
    add_bullet(
        doc,
        "It shows Pressure Vessel manufacturing from 20-May with no sign of the "
        "ASME six-week impact you report (completion now 31-Jul).",
    )
    add_bullet(
        doc,
        "It starts the Factory Acceptance Test on 27-Jul, while the RO Feed Pump "
        "is only installed on 11-Aug, so the integrated running test falls "
        "outside that window.",
    )
    add_bullet(
        doc,
        "It ships the CIP pump to site on 12-Sep, which does not match the "
        "11-week Ex-Works figure you now give.",
    )
    add_para(
        doc,
        "Every critical-path activity must be backed by a confirmed purchase "
        "order, a vendor-signed schedule, or a vendor letter. “Based on current "
        "estimation”, “around”, and “to be confirmed” are not a recovery "
        "baseline.",
    )
    blank(doc)

    add_block(
        doc,
        "Fedco FAT Execution Plan.",
        "You report that on 26-May Fedco made the start of documentation "
        "conditional on a 30% down payment, that this was not disclosed earlier, "
        "and that you are still engaging Fedco. A commercial condition between BW "
        "Water and Fedco is not a basis to move the delay to ADASA. Under the "
        "contract, payment runs against milestones (BAE Clause 31) and the "
        "optional 25% advance under Clause 32 was never requested. Sub-supplier "
        "delays are entirely BW Water's responsibility, and the delivery period "
        "is firm, with any supplier delay recovered at your own cost "
        "(Clauses 35, 46 and 27). Please resolve the Fedco "
        "condition at your cost and give us firm fabrication and pre-shipment "
        "documentation dates, with a contingency plan if Fedco slips further.",
    )
    blank(doc)

    add_block(
        doc,
        "CIP Pump.",
        "We take note of the NTK lead time of 18 to 22 weeks, the air-freight "
        "route to about 11 weeks Ex-Works Penang, and your decision to decouple "
        "the pump. We acknowledge the EX Works arrangement. Please confirm "
        "whether collection is at Penang or at the NTK facility, submit the FAT "
        "procedure with its acceptance criteria, give at least one month's notice "
        "for our witness, and send the SAT execution plan you offered. The "
        "11-week figure is your logistics target, not a contractual threshold, "
        "and the cost of any additional site personnel arising from the "
        "decoupling is reserved.",
    )
    blank(doc)

    add_block(
        doc,
        "UHPRO Skid Dry Testing.",
        "You confirm that the Performance and Running Test for the High Pressure "
        "Pump and turbochargers moves to a “Site Acceptance Test” at Taltal, with "
        "the Factory and Site test split due 15-Jun. Before we take a position, "
        "we need to understand how that site test is resourced. Your own Technical "
        "Offer (Section 18) staffs the site for installation supervision, "
        "commissioning and start-up, on-site performance testing and training "
        "within a 21-day window. A Field Service Engineer carries the "
        "commissioning and performance-testing scope over about twelve business "
        "days, and that on-site performance testing is the commissioning "
        "validation under Section 10.2 of the Specification. It is not a "
        "relocated factory Performance and Running Test of the pumps, and neither "
        "the Specification (Section 9) nor your offer contemplates a separate "
        "Site Acceptance Test. "
        "In the 15-Jun split, please state which personnel will execute the "
        "relocated Performance and Running Test and within which window. We "
        "confirm that dry testing at Penang will not start before our written "
        "approval, and we reserve our position on the transfer and its "
        "consequences until we have reviewed the split.",
    )
    blank(doc)

    add_block(
        doc,
        "EX Works Deferral.",
        "An arrival window of 8 to 12 August, still subject to Fedco "
        "confirmation, is not a firm date; we need a single confirmed date. We "
        "accept your commitment to carry the revised dates and the downstream "
        "impacts into the next tracker as the updated baseline, and the recovery "
        "schedule requested above is the instrument that must reflect them.",
    )
    blank(doc)

    add_block(
        doc,
        "Alternative Cartridge Filter.",
        "We note that both vertical filters remain in FRP, which closes the "
        "material concern, that the datasheet was submitted on 25-May, and that "
        "the purchase order will wait for our approval. We are reviewing the "
        "datasheet and await the general arrangement and mechanical layout "
        "drawings with the tie-in interfaces, together with a written attestation "
        "that the tie-ins remain identical to the approved design.",
    )
    blank(doc)

    # RO PV / ASME (con "formal Change Order" en negrita inline)
    add_segments(
        doc,
        [
            ("RO Pressure Vessels and ASME. ", True),
            ("The Protec Arisawa letter due today has not arrived. Our position "
             "is unchanged: dropping the ASME stamp is a scope change and "
             "requires a ", False),
            ("formal Change Order", True),
            (", not a schedule decision. The six weeks do not exhaust the buffer "
             "of over ten weeks between the 29-May arrival (PO M184) and the "
             "16-Aug Ex-Works. No fabrication under the modified method before we "
             "approve the updated Inspection and Testing Plan (due 15-Jun). We "
             "require the test evidence: the hydrostatic test at the operating "
             "rating, the non-destructive examination, and the dimensional and "
             "material records with their certificates. The certified-rating "
             "question against 1800 psi is still open, and the FAT and dispatch "
             "payment milestones stay conditioned. We also question why this "
             "applies at all. As we understand it, the 1800 psi vessel is a "
             "proven, standard Tier-1 product, not a special item; please confirm "
             "it is a catalogue model and, if so, explain the six-week "
             "certification and the rating doubt.", False),
        ],
    )
    blank(doc)

    add_block(
        doc,
        "Not yet addressed.",
        "Your response does not cover the pre-dispatch hold-point documentation: "
        "the SEC compliance verification, the Super Duplex material certificates "
        "and quality dossier, and the marine transport preservation and packing "
        "procedure. Please give the status and firm dates for each.",
    )
    blank(doc)

    add_segments(
        doc,
        [
            ("We need the updated recovery schedule by tomorrow.", True),
            (" This is urgent: we must report the situation to our management "
             "with official documentation. We cannot present the previous "
             "schedule, which still shows the 16-Aug Ex-Works and the downstream "
             "dates, together with the answers you give in this email, because "
             "the two no longer agree. The remaining items above, with the Protec "
             "Arisawa letter, we ask in writing by Friday 5-Jun-2026; the 15-Jun "
             "deliverables stay on that date, with a five-business-day review on "
             "our side. Our reservations stand, including the formal Change Order "
             "for the ASME change and the conditioned payment milestones.", False),
        ],
    )
    blank(doc)

    # =========================================================================
    # CIERRE
    # =========================================================================
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA — Aguas de Antofagasta S.A."]:
        add_para(doc, line)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
