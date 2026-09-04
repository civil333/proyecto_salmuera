#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N6 (Entrega 13) & URGENT Coordination Meeting
Fecha: 02 de Marzo de 2026
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..",
    ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import set_table_borders, calcular_anchos_columnas

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT_FILE = "2026-03-02_Transmittal-N6-Rejection-Meeting.docx"
CONTACTO = "Luis Rivera"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ── HEADER ──────────────────────────────────────────────────────────────
    fields = [
        ("Date:", "March 02, 2026"),
        ("From:", f"{CONTACTO} — Contract Administrator (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc."),
        ("CC:", "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, Andrew Zaske, Adzlan Bin Abd Rahim"),
        ("Subject:", "ADASA - Taltal Brine Module: Transmittal N6 (Entrega 13) & URGENT Coordination Meeting"),
        ("Ref:", "Contract C-4300 / BAE 12803"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ── BODY ───────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please find attached the official Transmittal N6 corresponding to your Entrega 13, "
        "along with the updated Master Deliverable Register reflecting the current status of all project documentation."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "While we acknowledge the resolution of several historical items in this delivery, this engineering batch contains "
        "a document with a critical finding that results in "
    )
    para.add_run("rejection (Code 4)").bold = True
    para.add_run(", blocking a key procurement milestone:")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Unacceptable Downgrade of HP Couplings (Feed Turbocharger): \n").bold = True
    para.add_run(
        "Your proposal to downgrade the high-pressure couplings from the contractual baseline of 2,000 psi "
        "down to 1,200 psi based on the argument that the correct couplings are \"out of stock and considered a rare item\" "
        "is inadmissible. "
        "Furthermore, in BW Water's own formal response to ADASA's review comments "
        "(Submittal 25007-0002, January 22, 2026), BW Water explicitly stated: "
        "'BW will provide coupling rated 2000 psi.' This prior formal commitment "
        "cannot be unilaterally reversed citing logistical constraints. \n"
        "Logistical constraints do not justify compromising the safety margins of an "
        "Ultra High-Pressure RO (UHPRO) circuit. The 1,200 psi rating leaves a completely deficient 19% safety margin "
        "over operating pressure. \n"
    )
    para.add_run("Path to resolution: ").bold = True
    para.add_run(
        "ADASA confirms a technically acceptable path forward: upgrade the Feed TC coupling to "
        "\u2265 1,800 psi AND submit the coupling manufacturer\u2019s datasheet (model, MAWP, HPB service "
        "certification) for both turbochargers (SIP-09-001 Feed TC and SIP-09-002 Interstage TC). "
        "Under these conditions, ADASA would revise the Code 4 verdict to Code 2. "
        "ADASA\u2019s preferred solution remains the return to 2,000 psi (Piedmont Style H), "
        "which constituted the contractual baseline. "
        "Should BW Water be unable to supply a coupling rated \u2265 1,800 psi, a flanged CL900 or "
        "welded connection (as established in Technical Proposal Rev1 \u2014 Justification of Mechanical "
        "Couplings/Joints (Victaulic Type) in High Pressure) remains available as a last resort. "
        "Downgrading the safety class of the equipment is not an option."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Additional note \u2014 Interstage Turbocharger (Code 2, SIP-09-002): \n").bold = True
    para.add_run(
        "The Interstage TC Rev C, accepted as Code 2 at 1,800 psi, also does not include the "
        "coupling manufacturer\u2019s datasheet. The model number, MAWP, and HPB service classification "
        "must be submitted together with the Feed TC revision."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Schedule Impact & Catch-up Strategy").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "We are now facing severe delays across the board. As detailed in the attached Master Register, "
        "60% of the contractual engineering deliverables remain unresolved (either pending correction, partially delivered, or never submitted)."
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "Additionally, we note that the deadline for your response to our request for "
    )
    para.add_run("CIP External System Tie-in Definition and Updated Equipment Layout").bold = True
    para.add_run(
        " (sent 26-Feb-2026) expired today, March 2nd. We have yet to receive the revised layout confirming "
        "the CIP footprint (max. 3.5m extension) and the LQ alignment as discussed in our coordination meeting "
        "on February 18th. Please address this in Wednesday\u2019s meeting as well."
    )
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(
        "Furthermore, you have still not formally submitted the updated Catch-up Schedule, which was initially requested "
        "over a month ago on "
    )
    para.add_run("January 28th, 2026").bold = True
    para.add_run(", with a formal follow-up sent on ")
    para.add_run("February 9th, 2026").bold = True
    para.add_run(
        " (\"Catch-Up Schedule Request - Overdue Response Required\"). This lack of a formal recovery strategy "
        "is unacceptable given the current status of the engineering phase."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Mandatory Coordination Meeting").bold = True
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run("Given the critical nature of these roadblocks, we require a mandatory coordination meeting this ")
    para.add_run("Wednesday, March 4th, 2026, at 10:00 AM (Chile Time)").bold = True
    para.add_run(" to address:\n")
    para.add_run("• Immediate technical alternatives for the HP couplings.\n")
    para.add_run("• CIP External System tie-in definition and updated Equipment Layout.\n")
    para.add_run("• The formal presentation of the overdue Catch-up Schedule and a realistic path forward.")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Please confirm receipt of this transmittal and your attendance for Wednesday\u2019s meeting so we can send the Teams invite."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ─────────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Project Engineer",
        "ADASA \u2014 Aguas de Antofagasta S.A.",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_correo()
