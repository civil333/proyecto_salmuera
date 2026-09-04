#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water: replica a la minuta de la weekly call del 07-Jul-2026.
Reclama los entregables vencidos y corrige el registro del acta de BW Water.

- Reply-All al thread de Eduardo Yamauchi "25007 Project Taltal - Weekly
  Coordination Call - Notes 07-Jul-2026" (07-Jul-2026, 16:13). Cadena SEPARADA
  de la del Transmittal N27 (CLAUDE.md 3.4).
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Tono contractual (global sec. 9.2): firme, NO acusatorio.
- Los repuestos se citan por NOMBRE + monto, sin numero de seccion de la oferta:
  la tabla itemizada los numera 3.12 (mandatorios) y 3.13 (2 anos), pero los
  correos del 26-Feb y 26-Mar citaron "Section 3.8". Se evita arrastrar el error.
- El cuerpo del correo vive hardcodeado en este script (patron correos §3.4). El
  contexto interno, la verificacion de fuentes y el checklist estan en
  2026-07-13_Weekly-Call-07Jul-Overdue-Commitments_Descripcion.md.
"""

import os
import sys

from docx import Document
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-13_Weekly-Call-07Jul-Overdue-Commitments.docx"
)
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
    """segments = [(texto, bold), ...] -> un parrafo con bold inline."""
    para = doc.add_paragraph()
    for text, bold in segments:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def add_bullet(doc, segments, size=11):
    """segments = [(texto, bold), ...] -> vineta con bold inline."""
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    bullet = para.add_run("•  ")
    bullet.font.name = "Arial"
    bullet.font.size = Pt(size)
    for text, bold in segments:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def blank(doc):
    doc.add_paragraph()


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ---- HEADER -------------------------------------------------------------
    fields = [
        ("Date:", "July 13, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Victor Gutierrez (ADASA); Jeryl F. Regulacion, "
            "Adzlan Bin Abd Rahim, Nick Huta, Sadeep Irugalbandara, "
            "Stephane Gehant, Lokman Hakim Bin Mat (BW Water)",
        ),
        (
            "Subject:",
            "RE: 25007 Project Taltal - Weekly Coordination Call - "
            "Notes 07-Jul-2026 — Overdue Commitments and Record Corrections",
        ),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / BWWA Ref. 20.24.6501.F Rev.1 / "
            "Submittals 25007-0063 and 25007-0064 / "
            "Transmittal N27 (P22-TM-09-000-027-0)",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # ---- APERTURA -----------------------------------------------------------
    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_para(
        doc,
        "Thank you for the notes of the 7 July coordination call. Submittals "
        "25007-0063 (10 July) and 25007-0064 (13 July) were received, the six "
        "documents are under review, and ADASA's disposition will issue in "
        "Transmittal N27. On our side, the three items owed by ADASA were "
        "closed on the day of the call: our reply to RFI 25007-RO-RFI-0002, "
        "our position on the PLC/LCP panel delay, and the third-party shop "
        "inspection notice issued under Technical Note P22-NT-09-000-002-0. "
        "The items below remain open on yours.",
    )
    blank(doc)

    # ---- 1. REPUESTOS -------------------------------------------------------
    add_segments(
        doc,
        [
            ("Spare parts quotation, still not received.", True),
            (
                " ADASA first requested this quotation on 26 February 2026 "
                "with a deadline of 7 March, and followed up on 26 March. "
                "BW Water has since committed to it three times in its own "
                "records: “to be released next Monday” (notes of 16 "
                "June, due 22 June); “BW Water to submit the complete "
                "two-year spare parts package by 03-Jul-2026” (notes of "
                "30 June); and Friday 10 July at last week's call. Nothing has "
                "been received. Your notes of 7 July now record only "
                "“waiting for final quotations from vendors”, with "
                "no date. Four and a half months after the original request, "
                "that is not an acceptable status. The package must contain:",
                False,
            ),
        ],
    )

    add_bullet(
        doc,
        [
            (
                "The Mandatory/Critical Spare Parts List (USD 17,310.00, "
                "already contracted) listed and priced separately from the "
                "Recommended Two-Year Spare Parts List (USD 43,790.00, EXW). "
                "The categorization of mandatory components against reserve "
                "items was identified at the call as the cause of the "
                "administrative delay, so the split must be explicit in the "
                "package and the two categories are not to be merged.",
                False,
            )
        ],
    )
    add_bullet(
        doc,
        [
            (
                "Service and wear kits for the energy recovery turbochargers "
                "SIP-09-001 and SIP-09-002, with part descriptions, "
                "manufacturer part numbers, recommended two-year quantities "
                "and unit prices. These were absent from the original list and "
                "have been pending since 26 February.",
                False,
            )
        ],
    )
    add_bullet(
        doc,
        [
            (
                "A firm price validity date, and confirmation that the scope "
                "has not changed since the offer of September 2025.",
                False,
            )
        ],
    )

    add_segments(
        doc,
        [
            (
                "ADASA has no further time to grant on this item. Send us today "
                "whatever figures you already hold: the mandatory list is "
                "contracted and its amount is known, and where a vendor "
                "quotation is still open, such as the turbocharger kits, "
                "preliminary or budgetary numbers are acceptable for now, "
                "against a stated date for the firm prices. ADASA needs these "
                "figures today to carry the spare-parts cost into the project "
                "budget. ",
                False,
            ),
            ("Deadline: end of business today, Monday, 13 July 2026.", True),
        ],
    )
    blank(doc)

    # ---- 2. OTROS VENCIDOS DEL 10-JUL ---------------------------------------
    add_segments(
        doc,
        [
            ("Other commitments due on 10 July.", True),
            (
                " None of the following was included in submittals 0063 or "
                "0064:",
                False,
            ),
        ],
    )

    add_bullet(
        doc,
        [("I/O List, which is your own target date of 10 July.", False)],
    )
    add_bullet(
        doc,
        [
            (
                "Updated project schedule incorporating the vendor delay and "
                "the module milestone of approximately 12 September.",
                False,
            )
        ],
    )
    add_bullet(doc, [("Weekly fabrication report.", False)])
    add_bullet(doc, [("Document status report.", False)])

    add_segments(
        doc,
        [
            (
                "Four engineering deliverables lapsed on the same date: "
                "Grounding Point and Power Panel Layout Rev F, the FAT and SAT "
                "comparison table, the three mechanical route drawings, and "
                "the Plant Control Philosophy child documents. Transmittal N27 "
                "restates them. ",
                False,
            ),
            ("Deadline for all of the above: Friday, 17 July 2026.", True),
        ],
    )
    blank(doc)

    # ---- 3. CORRECCIONES DE REGISTRO ----------------------------------------
    add_segments(
        doc,
        [
            ("Record corrections.", True),
            (" Three points require correction.", False),
        ],
    )

    add_bullet(
        doc,
        [
            ("Cause of the control panel delay.", True),
            (
                " Your notes state that the change from the original enclosure "
                "specification to NEMA 4X resulted in additional manufacturing "
                "time. ADASA does not accept that characterization and set out "
                "its position in our letter of the same date. NEMA 4X / IP66 "
                "in Stainless Steel 316L is what BW Water's own approved Local "
                "Control Panel Datasheet and IFC Single Line Diagram specify. "
                "The deviation was the Outline drawing, now corrected in Rev "
                "C. The enclosure requirement did not change, and our position "
                "stands.",
                False,
            ),
        ],
    )
    add_bullet(
        doc,
        [
            ("FAT duration.", True),
            (
                " The reduction from ten to five working days is recorded as a "
                "mitigation, and it was not agreed. Our letter of 7 July asked "
                "for written confirmation that the reduced FAT preserves the "
                "full test scope, and that confirmation is still outstanding. "
                "No reduction is accepted until ADASA has reviewed the revised "
                "FAT program against the approved procedures, and the "
                "third-party witness points are to be preserved in full.",
                False,
            ),
        ],
    )
    add_bullet(
        doc,
        [
            ("Fedco pump FAT location.", True),
            (
                " Bureau Veritas was engaged to witness the tests in Penang. A "
                "second site changes the scope of the inspection, and no "
                "inspector can be assigned until you confirm the factory. "
                "Please confirm by Friday, 17 July 2026.",
                False,
            ),
        ],
    )
    blank(doc)

    add_para(
        doc,
        "Two actions recorded by ADASA at the call do not appear in your "
        "notes: the final revision of the Piping Layout, Equipment Layout and "
        "updated 3D model, and the equipment anchoring system to the main "
        "frame with its seismic calculation. Please confirm that both remain "
        "on your action list, with dates.",
    )
    blank(doc)

    add_para(
        doc,
        "Please respond with a date against each item above. We look forward "
        "to your comments.",
    )
    blank(doc)

    # ---- CIERRE -------------------------------------------------------------
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA — Aguas de Antofagasta S.A."]:
        add_para(doc, line)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    # apply_core_properties solo escribe los campos no vacios, asi que el
    # default de python-docx en `comments` sobrevive si no se pasa uno propio.
    docx_metadata.apply_core_properties(
        doc,
        title="Weekly Call 07-Jul-2026 - Overdue Commitments and Record Corrections",
        author="ADASA",
        last_modified_by="ADASA",
        comments="Aguas de Antofagasta S.A. - Proyecto Taltal BAE 12803",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
