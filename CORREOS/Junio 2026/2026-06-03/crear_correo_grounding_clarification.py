#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo de ADASA a BW Water — respuesta a la contra-pregunta sobre el Grounding
Point & Power Panel Location Layout (Rev E), Code 3 en el Transmittal N19.

- Reply-To al thread de Eduardo Yamauchi del 02-Jun ("RE: 25007 Taltal: Ground
  cable schedule clarification").
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Replica punto por punto a las 4 preguntas del comment.xlsx + 2 sub-puntos.
- Postura: dependencia de layout RESUELTA (Equipment + Piping Layout Code 2 desde
  TM N15); grounding schedule = entregable que cierra, formato del sample OK +
  completar embebido en Rev F; extension corta acotada del plazo a Mi 17-Jun sin
  renunciar a la reserva C-4300.
- Fuente unica del cuerpo: 2026-06-03_Grounding-RevF-Clarification_Descripcion.md
"""

import os
import sys

from docx import Document
from docx.shared import Inches, Pt

# Metadatos limpios (patron vendorizado de las skills template). Path absoluto
# per CLAUDE.md 3 (Synology no soporta symlinks).
sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
from docx_metadata import apply_core_properties, fix_app_xml  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-06-03_Grounding-RevF-Clarification.docx")
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
        ("Date:", "June 3, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Billy Tan, Adzlan Bin Abd Rahim, Jeryl F. Regulacion, "
            "Stephane Gehant, David Chee Keat Swee, Sadeep Irugalbandara, "
            "Nick Huta, Victor Gutierrez",
        ),
        ("Subject:", "RE: 25007 Taltal: Ground cable schedule clarification"),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / Technical Review Transmittal N19 "
            "(P22-TM-09-000-019-0, 25-May-2026) / Grounding Point & Power Panel "
            "Location Layout Rev E (P22-DWG-09-007-003)",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # =========================================================================
    # CUERPO (replica punto por punto)
    # =========================================================================
    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_para(
        doc,
        "Thank you for your message of 2-Jun-2026. We are glad to provide "
        "clarification on any of the Transmittal N19 comments, and we welcome "
        "these questions ahead of Rev F. Our position on each point raised on the "
        "Grounding Point & Power Panel Location Layout (Rev E) is set out below.",
    )
    blank(doc)

    # Punto 1 - dependencia de layout (aprobado + main panel fijo)
    add_segments(
        doc,
        [
            ("1. Dependency on the Equipment Layout. ", True),
            ("The Equipment Layout (P22-DWG-09-005-003) and the Piping Layout "
             "(P22-DWG-09-005-004) are ", False),
            ("both approved (Code 2)", True),
            (", issued in Transmittal N15 on 22-Apr-2026. This satisfied the "
             "condition set in Transmittal N11, under which the Grounding layout "
             "was to follow their acceptance, so the layout dependency is now "
             "closed and Rev F can proceed without further wait. A direct "
             "consequence follows: with the arrangement approved, ", False),
            ("the position of the main panel (LCP / Main Switchboard, P22-LCP-01) "
             "is fixed and must not be relocated in Rev F", True),
            (". We therefore do not accept note 5 of Rev E, which reads "
             "“panel locations are indicative only and subject to "
             "relocation based on site condition”: the main panel position "
             "is set by the approved Equipment Layout, and any change to it "
             "requires a revised layout approved by ADASA, not a site decision. "
             "Please prepare Rev F on the approved Equipment Layout (Rev B), "
             "keeping the main panel and the grounding points at the positions of "
             "that accepted arrangement. We have no record of a formal Equipment "
             "Layout Rev C; if you hold a later revision internally, submit it, "
             "but it does not block Rev F. The item that has stayed open since "
             "Transmittal N11 is the grounding schedule itself, which point 2 "
             "addresses.", False),
        ],
    )
    blank(doc)

    # Punto 2 - grounding schedule (reframe: sustancialmente completo + MTO)
    add_segments(
        doc,
        [
            ("2. Grounding schedule. ", True),
            ("Yes, the grounding schedule is the deliverable that closes this "
             "item, open since Transmittal N11 and carried through Transmittal "
             "N15 and Transmittal N17. The schedule you attached is the right "
             "format and is substantially complete: it lists the PE points, the "
             "conductor sizes, the ring-main topology, the equipotential bonding "
             "and the ADASA-scope main grounding connection. A separate "
             "template-approval step is therefore not necessary. To close the "
             "item, carry this schedule into Rev F, either on the drawing or as a "
             "referenced annex, and we will assess it formally when Rev F is "
             "reviewed. One refinement to fold in: the Cable Specification column "
             "shows Cu/PVC throughout, while the drawing’s own Material "
             "Take-Off already lists a copper earth link, tinned braided copper "
             "and a copper bar for the ring main and tray bonding. Reconcile the "
             "two so the schedule distinguishes the bare or braided copper of the "
             "earth electrode and ring main from the insulated PE conductors used "
             "for equipment bonding, consistent with the interconnection drawing "
             "P22-DWG-06-006-101 and with NCh Eléctrica 4/2003 Section 10.0.",
             False),
        ],
    )
    blank(doc)

    # Punto 3 - CCS description
    add_segments(
        doc,
        [
            ("3. Consolidated Comment Sheet description. ", True),
            ("Noted. With the description corrected to “Grounding Point & "
             "Power Panel Location Layout”, and the sheet now carrying the "
             "comment-closure record for this drawing rather than for the Cable "
             "Tray Layout, the Transmittal N17 observation closes when we review "
             "Rev F, provided the sheet is legible (see point 5).", False),
        ],
    )
    blank(doc)

    # Punto 4 - grounding method reference
    add_segments(
        doc,
        [
            ("4. Grounding method reference. ", True),
            ("The detail we asked for in Transmittal N17 is the resolution of the "
             "cross-reference printed on the drawing: confirm that the typical "
             "detail it points to is contained in the Typical Installation "
             "Details of Power Works (P22-DWG-09-007-005, Rev C). On top of that, "
             "designate which of the seven grounding methods shown on that drawing "
             "applies to each load type, following IEC 60364-5-54. If the "
             "cross-reference resolves and the method is designated, no detail "
             "different from Rev E is needed. While on this point, please align "
             "the conductor cross-section basis to IEC 60364-5-54 across the "
             "whole drawing: note 8 on page 2 still cites NEC Table 250.122, "
             "whereas page 3 already cites IEC 60364-5-54, and the basis adopted "
             "in Transmittal N17 is IEC 60364-5-54.", False),
        ],
    )
    blank(doc)

    # Punto 5 - revision history + screenshots
    add_segments(
        doc,
        [
            ("5. Revision history and screenshots. ", True),
            ("The status labels “Issued for Approval” (Rev A) and "
             "“Revised as per Comment” (Rev B onward) are correct as "
             "status, but they are not what our comment asks for. Add a one-line "
             "description of what actually changed in each revision from Rev B "
             "through Rev E, with the ECN reference where applicable, so the "
             "history block is traceable. On the screenshots: "
             "pasting captures from the Transmittal PDF into the Consolidated "
             "Comment Sheet is not prohibited. The point of our note was "
             "legibility, since the Rev E sheet came through partly unreadable. "
             "Issue the sheet from the electronic source at a resolution that "
             "reads clearly, regardless of where the content originates.", False),
        ],
    )
    blank(doc)

    # Punto 6 - plazo
    add_segments(
        doc,
        [
            ("6. Schedule. ", True),
            ("With the layout dependency resolved, there is no longer a basis to "
             "defer Rev F. As a one-time accommodation for raising these "
             "clarifications, we extend the Rev F due date set in Transmittal N19 "
             "to Wednesday 17-Jun-2026 (ten working days from this reply).", False),
        ],
    )
    blank(doc)

    add_para(doc, "We look forward to Rev F.")
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

    # =========================================================================
    # METADATOS LIMPIOS (antes / despues de save)
    # =========================================================================
    apply_core_properties(
        doc,
        title="RE: 25007 Taltal - Ground cable schedule clarification",
        author="Luis Rivera",
        subject="Grounding Layout Rev F clarification - Transmittal N19",
        category="Correspondence",
        comments="ADASA reply to BW Water clarification request on TM N19 Grounding comments",
        language="en-US",
        revision=1,
    )
    doc.save(OUTPUT_FILE)
    fix_app_xml(OUTPUT_FILE, application="Microsoft Office Word",
                company="ADASA - Aguas de Antofagasta S.A.")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
