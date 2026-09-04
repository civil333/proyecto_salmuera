#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N9 ADASA-BW_WATER
Entrega E17 (25007-0017): P&ID Rev B
Fecha: 11-Mar-2026

Veredicto: 2 - APPROVED AS NOTED
Documentos:
  - P22-DWG-09-009-002 Rev B   P&ID   → 2 - Approved as Noted

Notas:
  NOTE-01 (MINOR): Codigo titulo -02 vs -002
  NOTE-02 (MINOR): TK-09-002 vol 0.27 m3 efectivo vs 0.34 m3 total
"""

import sys
import os

# Agregar la ruta del skill template-adasa
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    "..",
    ".claude",
    "skills",
    "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt


def crear_transmittal():
    """Genera el Transmittal N9 en formato ADASA"""

    output_file = "TRANSMITTAL N9 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N9 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-009-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    doc = Document(output_file)

    # Limpiar contenido de ejemplo del template
    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(
            x in texto
            for x in [
                "RESUMEN EJECUTIVO",
                "INTRODUCCION",
                "INTRODUCCI\u00d3N",
                "1. INTRO",
                "ESTE DOCUMENTO HA SIDO GENERADO",
                "AGREGUE AQUI EL CONTENIDO",
                "AGREGUE AQU\u00cd EL CONTENIDO",
            ]
        ):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== 1. EXECUTIVE SUMMARY =====
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 2 \u2014 APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water Delivery 17 (Submittal 25007-0017, received March 11, 2026) submits "
        "the Piping and Instrumentation Diagram Revision B (P22-DWG-09-009-002). "
        "This is the first P&ID revision since Transmittal N2, which identified "
        "13 open observations on Rev A. All 13 observations are addressed in Rev B, "
        "accompanied by a Consolidated Comment Sheet with BW Water\u2019s responses. "
        "ADASA acknowledges this as a substantive step forward."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B closes all outstanding Transmittal N2 observations: high-pressure lines "
        "confirmed in Super Duplex Stainless Steel; battery limits show flanged tie-in "
        "points with TAGs and diameters; 1st and 2nd stage labels added; valve and "
        "instrument TAGs completed per the project coding convention; and the legend "
        "revised. The Static Mixer TAG (MZE-09-001) is now consistent with the "
        "datasheet, closing an indirect observation from Transmittal N3."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Two minor notes prevent unconditional approval. The document code in the title "
        "block reads P22-DWG-09-009-02 (two-digit correlativo) where P22-DWG-09-009-002 "
        "is required. The antiscalant tank annotation shows 0.27\u00a0m\u00b3 (effective "
        "working volume) where 0.34\u00a0m\u00b3 (total installed volume per the accepted "
        "datasheet) is the correct P&ID annotation. Neither item affects the engineering "
        "content of the drawing."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Note on VM-09-015: ").bold = True
    para.add_run(
        "The P&ID correctly shows VM-09-015 (HP Pump to Feed Turbocharger isolation) "
        "as a manual valve. ADASA formally withdrew Transmittal N3 OBS-11 in its "
        "March 5, 2026 response after BW Water confirmed that this valve serves as a "
        "maintenance isolation point and is not a process control valve subject to "
        "ET \u2014 Valves and Piping electric actuation requirement. An unresolved "
        "inconsistency remains in the Valve List: Rev B item 18 records VM-09-015 as "
        "ON/OFF MOTORIZED, contradicting its confirmed manual function. "
        "Valve List Rev C must resolve this inconsistency."
    )
    aplicar_arial_12(para)

    doc.add_heading("Notes", level=2)

    add_simple_table(
        doc,
        [
            ("#", "Observation", "Severity"),
            (
                "NOTE-01",
                "Document code P22-DWG-09-009-02 in title block; correct code is "
                "P22-DWG-09-009-002 (three-digit correlativo).",
                "MINOR",
            ),
            (
                "NOTE-02",
                "TK-09-002 annotated as 0.27\u00a0m\u00b3 (effective volume); total "
                "installed volume per accepted datasheet is 0.34\u00a0m\u00b3.",
                "MINOR",
            ),
        ],
    )

    # ===== 2. GENERAL INFORMATION =====
    doc.add_heading("GENERAL INFORMATION", level=1)

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Submittal", "25007-0017"),
            ("Delivery date", "11-Mar-2026"),
            ("Review completion", "11-Mar-2026"),
            ("Total documents reviewed", "1"),
            ("Response code", "2 \u2014 Approved as Noted"),
            (
                "Response codes reference",
                "1=Approved, 2=Approved as Noted, "
                "3=To be Revised, 4=Rejected, 5=For Information",
            ),
            ("Contract", "C-4300 BW WATER SUPPLY-12803 V2"),
        ],
    )

    # ===== 3. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    doc.add_heading(
        "3.1 Piping and Instrumentation Diagram Rev B \u2014 P22-DWG-09-009-002",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B includes a Consolidated Comment Sheet covering the 13 open observations "
        "from Transmittal N2 (OBS-01 through OBS-14, excluding OBS-09 which was already "
        "closed by the Process Calculation review). All 13 observations are addressed."
    )
    aplicar_arial_12(para)

    doc.add_heading("TM N2 Observations \u2014 Status in Rev B", level=3)

    add_simple_table(
        doc,
        [
            ("TM N2 OBS", "Description", "BW Water Response", "ADASA Assessment"),
            ("OBS-01", "Battery limits with flange", "Added accordingly", "CLOSED"),
            (
                "OBS-02",
                "PVC lines within SDSS zone",
                "HP = SDSS; PVC only for LP (permeate, CIP)",
                "CONDITIONALLY CLOSED \u2014 see Note 1",
            ),
            ("OBS-03", "Line TAGs with diameter", "Added accordingly", "CLOSED"),
            ("OBS-04", "Drainage stream routing", "Revised accordingly", "CLOSED"),
            (
                "OBS-05",
                "Battery limit: flange + TAG + diameter",
                "Revised accordingly",
                "CLOSED",
            ),
            ("OBS-06", "CIP connection to TK-09-001", "Revised accordingly", "CLOSED"),
            (
                "OBS-07",
                "HP Pump characteristics (BH-09-001)",
                "Added accordingly",
                "CLOSED",
            ),
            ("OBS-08", "1st and 2nd stage labels", "Revised accordingly", "CLOSED"),
            ("OBS-09", "Design pressures", "Already closed in TM N2", "CLOSED (TM N2)"),
            (
                "OBS-10",
                "SDSS material confirmation in HP lines",
                "All HP lines shall be in SDSS",
                "CLOSED",
            ),
            (
                "OBS-11",
                "Valve TAGs",
                "Added; VE = motor actuated, VM = manual",
                "CLOSED",
            ),
            ("OBS-12", "Instrument TAGs", "Added per tagging procedure", "CLOSED"),
            ("OBS-13", "Flow direction arrows", "Added more arrows", "CLOSED"),
            ("OBS-14", "Legend update", "Legend revised", "CLOSED"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run(
        "Note 1 \u2014 OBS-02 Residual: "
    ).bold = True
    para.add_run(
        "BW Water confirmed the material policy: HP = SDSS; LP (permeate, CIP) = PVC. "
        "Physical routing segregation cannot be evaluated from the P&ID alone; the "
        "Piping Layout (P22-DWG-09-005-004 Rev B, pending since Transmittal N7 OBS-01) "
        "must confirm that PVC lines do not route through the HP equipment zone. "
        "The P&ID OBS-02 is conditionally closed pending Piping Layout Rev B."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note 1 \u2014 Document code truncated in title block (MINOR)", level=3
    )
    para = doc.add_paragraph()
    para.add_run(
        "The title block shows ADASA Code: P22-DWG-09-009-02. The project coding system "
        "requires three-digit correlativo: P22-DWG-09-009-002. The CCS itself correctly "
        "references P22-DWG-09-009-002 throughout, confirming this is a title block "
        "transcription error. Correct in Rev C."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note 2 \u2014 Antiscalant Tank TK-09-002: effective volume annotated "
        "rather than total installed volume (MINOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The P&ID annotates TK-09-002 as VOL: 0.27\u00a0m\u00b3. The accepted "
        "Antiscalant Dosing Tank Datasheet (P22-ET-09-009-010 Rev B, Transmittal N4) "
        "specifies total capacity 0.34\u00a0m\u00b3 and effective volume 0.27\u00a0m\u00b3. "
        "Transmittal N4 OBS-11 requested updating the P&ID to 0.34\u00a0m\u00b3 (total). "
        "Rev B was updated to 0.27\u00a0m\u00b3 (effective). P&ID convention is to annotate "
        "total installed tank volume. Update to 0.34\u00a0m\u00b3 in Rev C."
    )
    aplicar_arial_12(para)

    doc.add_heading("Indirect Observations \u2014 Status in Rev B", level=3)

    add_simple_table(
        doc,
        [
            ("Origin", "Observation", "Rev B Status"),
            (
                "TM N3 OBS-14 / TM N6 Note",
                "Static Mixer TAG: MZE-09-009 vs MZE-09-001",
                "CLOSED \u2014 Rev B shows MZE-09-001",
            ),
            (
                "TM N4 OBS-11",
                "Antiscalant Tank capacity: update P&ID from 0.25 m\u00b3 to 0.34 m\u00b3",
                "PARTIALLY CLOSED \u2014 updated to 0.27 m\u00b3 effective; "
                "0.34 m\u00b3 total required (NOTE-02)",
            ),
            (
                "TM N3 OBS-11",
                "VM-09-015 electric actuation",
                "WITHDRAWN \u2014 ADASA email 05-Mar-2026. "
                "Manual isolation valve (HP Pump to Feed Turbocharger); "
                "ET \u2014 Valves and Piping does not apply. "
                "P&ID correctly shows VM prefix.",
            ),
        ],
    )

    # ===== 4. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph(
        "The following BW Water document was reviewed as part of this transmittal. "
        "An ADASA-annotated copy is attached."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Attachment", "Document Code", "Title", "Rev"),
            ("1", "P22-DWG-09-009-002", "Piping and Instrumentation Diagram", "B"),
        ],
    )

    # ===== 5. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            (
                "P22-DWG-09-009-002",
                "Piping and Instrumentation Diagram",
                "B",
                "2 \u2014 Approved as Noted",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 2 \u2014 APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Notes to address in Rev C:").bold = True
    aplicar_arial_12(para)

    for i, item in enumerate(
        [
            "Correct document code P22-DWG-09-009-002 in title block (NOTE-01 \u2014 MINOR)",
            "Update TK-09-002 annotation to 0.34\u00a0m\u00b3 total installed volume "
            "(NOTE-02 \u2014 MINOR)",
        ],
        1,
    ):
        para = doc.add_paragraph(f"{i}. {item}")
        aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
