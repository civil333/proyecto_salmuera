#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ADASA -> BW Water: respuesta al plan de recuperacion del panel PLC/LCP
(Billy Tan via Eduardo Yamauchi, 20-Jul-2026).

- Reply-To al thread "RE: 25007 Taltal: PLC/LCP Panel Delivery - Notice of
  Delay". Cadena SEPARADA del correo de packing/EXW (mismo dia).
- Idioma: ingles (BW Water). Patron Document() directo per CLAUDE.md 3.4.
- Postura firme (global sec. 9.2 / 2.8): acusa el recovery como informacion SIN
  renunciar a la reserva de responsabilidad/EOT; exige (1) una fecha unica
  reconciliada, (2) prueba funcional de la bomba HP (no dry test) + confirmacion
  del alcance FAT, (3) RFS del modulo inclusiva de la bomba.
- Referencias a la ET por codigo + "Section 5.4.1 - ..." (CLAUDE.md 2.4); sin
  simbolo de seccion; sin citar Van Doorn ni codigos internos OBS/Code.
- Fuente unica del cuerpo: 2026-07-21_PLC-Panel-Recovery-Response_Descripcion.md
"""

import os
import sys

from docx import Document
from docx.shared import Inches, Pt

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR, "2026-07-21_PLC-Panel-Recovery-Response.docx"
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


def add_lead(doc, lead, rest, size=11):
    """Parrafo con un tramo inicial en bold (bold inline)."""
    para = doc.add_paragraph()
    r1 = para.add_run(lead)
    r1.bold = True
    r2 = para.add_run(rest)
    for run in (r1, r2):
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
        ("Date:", "July 21, 2026"),
        ("From:", f"{CONTACTO} - Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi - BW Water Americas Inc. (PMO Leader)"),
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
            "BW Water recovery plan 20-Jul-2026 / "
            "ADASA position 07-Jul-2026 / "
            "Local Control Panel Datasheet P22-ET-09-007-005 Rev 1 / "
            "PLC-LCP Outline Drawing P22-CD-09-008-001 / "
            "Transmittal N20 (P22-TM-09-000-020-0) / "
            "Technical Note P22-NT-09-000-002-0 / "
            "Technical Specification P22-ET-09-000-001-0 "
            "(Sections 8, 9 and 10.2) / "
            "Inspection and Test Plan P22-BA-09-000-004 Rev 0 "
            "(Sections 10 and 11) / "
            "RFI 25007-RO-RFI-0002",
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
        "Thank you for the recovery plan for the PLC/LCP panel provided on 20 "
        "July 2026, which we have registered as information. This reply does "
        "not waive ADASA's reservation on the responsibility for the delay, "
        "set out in our 7 July 2026 email responding to the Notice of Delay "
        "and in our reply to RFI 25007-RO-RFI-0002 of the same date. The "
        "recovery plan addresses the schedule but does not provide a basis "
        "that rebuts the documented "
        "reasons we gave: the NEMA 4X / IP66 rating remains one fixed by BW "
        "Water's own approved Local Control Panel Datasheet "
        "(P22-ET-09-007-005, Rev 1), not a requirement introduced by ADASA. "
        "ADASA's reservation of rights under the Bases Administrativas "
        "Especiales stands.",
    )
    blank(doc)

    add_para(doc, "We ask BW Water to close three points before the panel "
                  "proceeds:")
    blank(doc)

    add_lead(
        doc,
        "1. One committed date. ",
        "The plan gives two sequences that do not reconcile: panel "
        "ready-to-ship 7 August and at the BW Water workshop 23 August, "
        "against workshop FAT from 26 August to 5 September with ready-to-ship "
        "7 September. Please issue one dated recovery schedule (enclosure "
        "dispatch, arrival in Malaysia, workshop start, FAT window, panel "
        "completion and module hand-over) with a single committed date per "
        "milestone.",
    )
    blank(doc)

    add_lead(
        doc,
        "2. Dry FAT in Penang, functional acceptance on site. ",
        "We agree that the FAT is a dry test, in line with the Technical "
        "Specification (P22-ET-09-000-001-0), Section 8 - Factory Acceptance "
        "Tests, and that the tests with water (the high-pressure pump running "
        "under load and the RO performance run) belong to commissioning and "
        "the on-site Performance Tests at Taltal, per Section 9 - "
        "Commissioning and Start-up and Section 10.2 - Performance Tests, and "
        "per the approved Inspection and Test Plan (P22-BA-09-000-004, Rev 0), "
        "Section 10 - Commissioning and Section 11 - Performance Tests. On "
        "that basis, ADASA requires that:",
    )
    add_bullet(
        doc,
        "a) the dry FAT be executed in full per the approved Inspection and "
        "Test Plan (dry functional checks and the PLC/HMI control simulation, "
        "including the simulated pump trip under load) and recorded in the "
        "FAT report;",
    )
    add_bullet(
        doc,
        "b) the pump-dependent verifications that a dry FAT cannot close (the "
        "motor winding and bearing over-temperature trips, the high-pressure "
        "pump vibration trip, and the closed-loop control sequence: VFD ramp, "
        "pressure-control loop and turbocharger bypass) be carried to the "
        "on-site commissioning and Performance Tests and not closed at FAT; "
        "the detailed FAT procedure and the site Performance Test procedure, "
        "both subject to ADASA approval under the Inspection and Test Plan, "
        "shall reflect this split; and",
    )
    add_bullet(
        doc,
        "c) FAT completion and the Dispatch Release do not constitute "
        "functional or performance acceptance, which remains the on-site "
        "two-day Performance Test, mandatory for Provisional Acceptance.",
    )
    blank(doc)

    add_lead(
        doc,
        "3. A pump-inclusive ship date, with site acceptance kept separate. ",
        "BW Water confirms the 12 September 2026 ready-for-shipment date "
        "excludes the high-pressure pump and depends on its delivery. Please "
        "state the governing ship date with the pump installed, and track the "
        "panel and the pump / turbochargers as separate lines. The panel "
        "recovery does not by itself restore the module date while those "
        "long-lead items govern; the module ships once physically complete, "
        "and functional and performance acceptance follow at the on-site "
        "Performance Tests in Taltal.",
    )
    blank(doc)

    add_para(doc, "We look forward to the single recovery schedule and to your "
                  "comments.")
    blank(doc)

    # ---- CIERRE -------------------------------------------------------------
    add_para(doc, "Best regards,")
    blank(doc)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA - Aguas de Antofagasta S.A."]:
        add_para(doc, line)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    docx_metadata.apply_core_properties(
        doc,
        title="PLC-LCP Panel Recovery Plan - ADASA Response",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="PLC/LCP panel recovery plan - ADASA response",
        comments="Correo ADASA a BW Water - respuesta al recovery plan del "
                 "panel PLC/LCP (20-Jul-2026).",
        category="Correspondencia",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE, company="Aguas de Antofagasta S.A.")
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
