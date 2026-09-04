#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Re: Transmittal N6 (Entrega 13) & URGENT Coordination Meeting
Respuesta a Andrew Zaske — Reunión reprogramada para 09-Mar-2026
Fecha: 03 de Marzo de 2026
"""

from docx import Document
from docx.shared import Pt, Inches

OUTPUT_FILE = "2026-03-03_Re-Meeting-Rescheduled-March9.docx"
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
        ("Date:", "March 03, 2026"),
        ("From:", f"{CONTACTO} \u2014 Contract Administrator (ADASA)"),
        ("To:", "Andrew Zaske (BW Water)"),
        ("CC:", (
            "Eduardo Yamauchi; Tanya Figueroa; Andrea Frezzi; "
            "Ronald Pellejero Salazar; Victor Gutierrez Aqueveque; "
            "Mauricio Vallejos Briones; Shane Banks; Fadey Kassim; "
            "Jorge Guevara Lizana"
        )),
        ("Subject:", "Re: Transmittal N6 (Entrega 13) & URGENT Coordination Meeting"),
        ("Ref:", "Contract C-4300 / BAE 12803"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # ── BODY ────────────────────────────────────────────────────────────────
    para = doc.add_paragraph("Dear Andrew,")
    aplicar_arial(para)
    doc.add_paragraph()

    # Párrafo 1 — Acuse + aceptación
    para = doc.add_paragraph(
        "Thank you for your quick reply. We understand Eduardo is in Malaysia this week "
        "and appreciate the context. We accept option 3 and propose "
    )
    para.add_run("Monday, March 9th, 2026, at 10:00 AM (Chile Time)").bold = True
    para.add_run(
        " as the confirmed date. Please let us know if that works for Eduardo and the team "
        "so we can send the Teams invite."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Párrafo 2 — Alternativa breve call esta semana (opcional, ejecutivo)
    para = doc.add_paragraph(
        "If any technical availability opens up before then, we would also welcome a short call "
        "this week (Wednesday or Thursday) focused solely on the HP coupling item, "
        "as that issue is currently blocking procurement on our side. "
        "That said, if it is not practical without Eduardo, the March 9th meeting works as the single session."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # Párrafo 3 — Agenda confirmada (solo títulos)
    para = doc.add_paragraph("The agenda for March 9th remains as outlined in our previous email:")
    aplicar_arial(para)

    items = [
        "HP Couplings \u2014 technical path forward",
        "CIP External System tie-in and updated Equipment Layout",
        "Catch-up Schedule",
    ]
    for item in items:
        para = doc.add_paragraph(style="List Bullet")
        para.add_run(item)
        aplicar_arial(para)

    doc.add_paragraph()

    # Cierre
    para = doc.add_paragraph(
        "Please confirm the date and send the Teams link at your earliest convenience."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # ── FIRMA ────────────────────────────────────────────────────────────────
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
