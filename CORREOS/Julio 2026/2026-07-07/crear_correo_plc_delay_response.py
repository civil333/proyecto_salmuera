#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water: respuesta al Notice of Delay del panel PLC/LCP
(Eduardo Yamauchi, 07-Jul-2026). Reserva la posicion de ADASA sobre la
atribucion del atraso.

- Reply-To al thread de Eduardo (subject "RE: 25007 Taltal: PLC/LCP Panel
  Delivery - Notice of Delay"). Cadena SEPARADA de la NT de BV (correo D2).
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Tono contractual (global sec. 9.2): firme, NO acusatorio. Lidera con la
  contradiccion vs los documentos aprobados de BW Water (LCP Datasheet + IFC
  SLD), cita la ET NEMA 4X por nombre como soporte, NO afirma un requisito ET
  de material (CLAUDE.md sec. 7.6).
- Fuente unica del cuerpo: 2026-07-07_PLC-Panel-Delay-Position_Descripcion.md
"""

import os
import sys

from docx import Document
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-07_PLC-Panel-Delay-Position.docx"
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
    para = doc.add_paragraph()
    for text, bold in segments:
        run = para.add_run(text)
        run.bold = bold
        run.font.name = "Arial"
        run.font.size = Pt(size)
    return para


def add_bullet(doc, text, size=11):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    run = para.add_run("•  " + text)
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
        ("Date:", "July 7, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Victor Gutierrez, Ronald Pellejero, Jeryl F. Regulacion, "
            "David Chee Keat Swee, Nick Huta, Billy Tan, "
            "Lokman Hakim Bin Mat, Sadeep Irugalbandara, "
            "Elaine May Torres, Stephane Gehant",
        ),
        ("Subject:",
         "RE: 25007 Taltal: PLC/LCP Panel Delivery - Notice of Delay"),
        (
            "Ref:",
            "Contract C-4300 / BAE 12803 / "
            "BW Water Notice of Delay 07-Jul-2026 / "
            "Local Control Panel Datasheet P22-ET-09-007-005 / "
            "PLC-LCP Outline Drawing P22-CD-09-008-001 / "
            "Transmittal N20 (P22-TM-09-000-020-0) / "
            "Technical Note P22-NT-09-000-002-0 / "
            "RFI 25007-RO-RFI-0002 (ADASA reply 07-Jul-2026)",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    blank(doc)

    # ---- CUERPO -------------------------------------------------------------
    add_para(doc, "Dear Eduardo,")
    blank(doc)

    add_para(
        doc,
        "We acknowledge receipt of your Notice of Delay of 7 July 2026 for "
        "the PLC/LCP panel. ADASA does not accept the characterization of the "
        "NEMA 4X (IP66) enclosure rating as a new requirement, and reserves "
        "its position on the responsibility for this delay, for the following "
        "documented reasons:",
    )

    add_bullet(
        doc,
        "The NEMA 4X / IP66 rating was already fixed by BW Water's own "
        "approved Local Control Panel Datasheet (P22-ET-09-007-005, Rev 1), "
        "which specifies an nVent Hoffman Type FS FS66S enclosure with "
        "protection category NEMA 4X / IP66. The IP55 shown in the PLC/LCP "
        "Outline Drawing Rev A (P22-CD-09-008-001) was therefore a deviation "
        "from BW Water's own approved datasheet.",
    )
    add_bullet(
        doc,
        "The comment issued under Transmittal N20 flagged that internal "
        "contradiction; it did not introduce a new requirement. The "
        "“minimum IP54” indicated under Transmittal N15 is a floor, "
        "not a ceiling, and NEMA 4X / IP66 satisfies it. The Technical "
        "Specification (P22-ET-09-000-001-0), Section 5.4.1 - Constructive "
        "Characteristics, requires a protection class of NEMA 4X or its IP "
        "equivalent, not lower, from the outset.",
    )
    blank(doc)

    add_para(
        doc,
        "Separately and on the same date, ADASA has replied to RFI "
        "25007-RO-RFI-0002, confirming the enclosure material configuration "
        "(external body, door, roof, rear panel, plinth and gland plates in "
        "Stainless Steel 316L per the approved LCP Datasheet, with internal "
        "mounting components acceptable in galvanized or cold-rolled steel) "
        "and the correction to be reflected in the re-issued Outline Panel "
        "Drawing at NEMA 4X / IP66. The enclosure specification is therefore "
        "clarified and was available from the approved datasheet throughout.",
    )
    blank(doc)

    add_para(
        doc,
        "On this basis, the enclosure revision corrected a non-conforming "
        "drawing rather than a change introduced by ADASA. ADASA does not "
        "accept an extension of time attributable to ADASA for this cause and "
        "reserves its rights under the Bases Administrativas Especiales.",
    )
    blank(doc)

    add_para(doc, "We ask BW Water to provide:")
    add_bullet(
        doc,
        "a) a detailed recovery plan for the panel with firm dates, "
        "reconciling the stated recovery target of panel readiness by 10 "
        "August 2026 against the current forecast of manufacturing completion "
        "on 14 August 2026 and delivery to Penang around 28 August 2026, and "
        "committing to a single date;",
    )
    add_bullet(
        doc,
        "b) written confirmation that the workshop FAT reduced from ten to "
        "five working days preserves the full test scope, including panel "
        "termination and power-up, I/O loop testing, instrument configuration "
        "and functionality, and the software FAT;",
    )
    add_bullet(
        doc,
        "c) the reconciled impact on the module ready-for-shipment date "
        "(currently forecast 12 September 2026) and on the Factory Acceptance "
        "Test and inspection points, including how the panel schedule "
        "interacts with the arrival of the High Pressure Pump and "
        "turbochargers on the critical path (the panel recovery does not by "
        "itself restore the module date if those long-lead items remain "
        "governing), noting that the panel delivery governs part of the "
        "inspection schedule communicated in our Technical Note "
        "P22-NT-09-000-002-0.",
    )
    blank(doc)

    add_para(doc, "We look forward to your comments.")
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
    docx_metadata.apply_core_properties(
        doc,
        title="PLC-LCP Panel Delay - ADASA Position",
        author="ADASA",
        last_modified_by="ADASA",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
