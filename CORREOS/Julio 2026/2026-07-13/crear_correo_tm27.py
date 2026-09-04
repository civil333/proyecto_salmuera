#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo: Transmittal N27 (P22-TM-09-000-027-0). Submittals 25007-0063 (E63) +
25007-0064 (E64), 6 documentos. Fecha: 13 de Julio de 2026 (lunes).
Re-escopeado: al llegar la E64 con este correo aun en BORRADOR, se folded E64
en el N27 en vez de abrir un N28.
Veredicto TM N27: 3 - TO BE REVISED. Tally 4 Code 2 + 2 Code 3.
Driver unico: el HP/LP Pressure Test Procedure Rev C adjunta una Line List que
ordena 75 bar de hidrostatica sobre una linea de PVC (DA-PVC-DN65-09-016) ->
riesgo de seguridad; se pide detener cualquier prueba hasta reconciliar.
Dos gates cerrados: RO Vessel Hydrostatic Rev C (test a 1.1x diseno) y PLC-LCP
Outline Rev C (enclosure SS316L/NEMA 4X per RFI-002).

FORMATO EJECUTIVO (regla permanente): cuerpo compacto ~160 palabras. Lead con
veredicto; safety item = unica accion arriba en bold; cierres y pendientes en
una linea cada uno; sin parrafos que dupliquen. Entrega via link Synology.
English, BW Water. Sin reuniones. Cadena = thread regular de transmittals.
"""

import os
import sys

from docx import Document
from docx.shared import Pt, Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-07-13_Transmittal-N27.docx")
CONTACTO = "Luis Rivera"
# Reemplazar por el link de la carpeta Synology de ESTE transmittal antes de enviar.
DOWNLOAD_LINK = "https://lrg.synology.me:6501/d/s/192lEgkHowre9aB7Xq17uqPalvdU9v5Z/9VEOGTc569y_FeCJGzMrvq-gOm0IEV1o-4rWgl4DGWA0"


def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)
    # Espaciado compacto entre parrafos (reemplaza las lineas en blanco) para
    # que el correo ejecutivo quepa en 1 pagina.
    pf = paragraph.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(5)


def add_hyperlink(paragraph, url, text):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    rfonts.set(qn("w:ascii"), "Arial")
    rfonts.set(qn("w:hAnsi"), "Arial")
    rpr.append(rfonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "22")
    rpr.append(sz)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)
    return hyperlink


def add_runs(doc, runs):
    """runs = lista de items; cada item es un str (no-bold) o una tupla
    (texto, bold?). Aceptar str simple evita el bug de tupla-sin-coma."""
    para = doc.add_paragraph()
    for item in runs:
        if isinstance(item, str):
            text, bold = item, False
        else:
            text = item[0]
            bold = item[1] if len(item) > 1 else False
        r = para.add_run(text)
        if bold:
            r.bold = True
    aplicar_arial(para)
    return para


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    fields = [
        ("Date:", "July 13, 2026"),
        ("From:", f"{CONTACTO} — Project Engineer (ADASA)"),
        ("To:", "Eduardo Yamauchi — BW Water Americas Inc. (PMO Leader)"),
        (
            "CC:",
            "Cesar Malhue, Jorge Guevara, Ronald Pellejero, Victor Gutierrez, "
            "Mauricio Vallejos, Jorge Valdes, Tanya Figueroa, Allan Valentos, "
            "Jeryl F. Regulacion, Sadeep Irugalbandara, Andrew Sia, "
            "Ghazi Ozair, Nick Huta, Marjan Arsovic, Gerald Ross, "
            "Andrew Zaske, Adzlan Bin Abd Rahim",
        ),
        (
            "Subject:",
            "ADASA – Taltal Brine Module: Technical Review Transmittal N27 "
            "(25007-0063/0064) — safety item on the attached Line List",
        ),
        ("Ref:", "Contract C-4300 / BAE 12803 / P22-TM-09-000-027-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph("Dear BW Water Project Team,")
    aplicar_arial(para)

    # 1. Lead: veredicto (una frase)
    add_runs(doc, [
        ("Transmittal N27", True),
        (" (P22-TM-09-000-027-0) covers submittals 25007-0063 and 25007-0064 — six "
         "documents. "),
        ("Verdict: 3 — To Be Revised", True),
        (" (4 Code 2, 2 Code 3)."),
    ])

    # 2. Safety item = la unica accion, arriba, en bold
    add_runs(doc, [
        ("Safety item — please act before any pressure test. ", True),
        ("The HP and LP Pressure Test Procedure Rev C delegates its test pressure to "
         "an attached Line List that orders 75 bar on line DA-PVC-DN65-09-016, a PVC "
         "line rated far below that; a shop testing to it would rupture the line. "
         "Please confirm no line has been tested to those values and re-issue as Rev "
         "D; the high-pressure hydrostatic test remains a Hold Point."),
    ])

    # 3. Buenas noticias: 4 Code 2 (2 gates + FAT), condensado
    add_runs(doc, [
        ("Four documents are "),
        ("Approved as Noted", True),
        (" and issue at IFC Rev 0 with the items in Section 2, and two of them close "
         "gates open for months: the "),
        ("RO Vessel Hydrostatic Test Procedure Rev C", True),
        (" (now at the correct test pressures) and the "),
        ("PLC-LCP Outline Panel Drawing Rev C", True),
        (" (SS316L / NEMA 4X per the RFI-002 reply), releasing the panel fabrication "
         "gate. The "),
        ("PLC-LCP FAT Procedure", True),
        (" is complete and correct; it carries reference and tag corrections to "
         "incorporate at issue, and its RTD protection sign-off is held until the open "
         "Alarm and Interlock List is reconciled (Section 3)."),
    ])

    # 3b. El unico Code 3 nuevo (O&M) atado a los entregables de control abiertos
    add_runs(doc, [
        ("The Operating and Maintenance Manual is To Be Revised", True),
        (": its control sequence, setpoints and HMI depend on the still-open Control "
         "Philosophy children (Sequence Chart, Setpoint List, HMI Screenshots) and it "
         "contradicts the approved turbocharger-bypass control. It re-issues once those "
         "close."),
    ])

    # 4. Pendientes en una linea (punteo a Seccion 3, no re-enumerar)
    add_runs(doc, [
        ("Outstanding. ", True),
        ("The items open from the July 10 deadline are listed in Section 3 of the "
         "transmittal. Please deliver them by Friday, July 17, 2026, and send us the "
         "dates you commit to for anything you cannot meet."),
    ])

    # 5. Link + cierre (una linea)
    para = doc.add_paragraph()
    para.add_run("The transmittal and the six annotated PDFs are available at ")
    aplicar_arial(para)
    add_hyperlink(para, DOWNLOAD_LINK, "this Synology download link")
    para.add_run(". Please confirm receipt. We look forward to your comments.")
    aplicar_arial(para)

    para = doc.add_paragraph("Best regards,")
    aplicar_arial(para)

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in ["Project Engineer", "ADASA — Aguas de Antofagasta S.A."]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    # ---- metadatos limpios (global sec. 2.3) --------------------------------
    # apply_core_properties solo escribe los campos no vacios: `comments` debe
    # pasarse explicito o sobrevive el default 'generated by python-docx'.
    docx_metadata.apply_core_properties(
        doc,
        title="Transmittal N27 - Submittals 25007-0063 and 25007-0064",
        author="ADASA",
        last_modified_by="ADASA",
        comments="Aguas de Antofagasta S.A. - Proyecto Taltal BAE 12803",
        language="en-US",
    )
    doc.save(OUTPUT_FILE)
    docx_metadata.fix_app_xml(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: DOWNLOAD_LINK sin definir — reemplazar antes de enviar.")


if __name__ == "__main__":
    crear_correo()
