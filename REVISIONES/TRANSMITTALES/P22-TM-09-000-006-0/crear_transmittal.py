#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N6 ADASA-BW_WATER
Entrega 13 (Submittal 25007-0013) - 9 documentos
Fecha: 27-Feb-2026

ESTRUCTURA ULTRA-EJECUTIVA (Aprobada):
1. EXECUTIVE SUMMARY (Foco único: Rechazo por downgrade de Turbochargers)
2. CRITICAL ROADBLOCK: FEED TURBOCHARGER COUPLING DOWNGRADE (Detalle técnico)
3. STATUS OF OTHER SUBMITTED DOCUMENTS (Tabla sintética para válvulas, bombas, etc.)
4. PENDING ACTIONS FROM PREVIOUS TRANSMITTALS (Tabla de referencia cruzada)
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
    """Genera el Transmittal N6 ultra-ejecutivo en formato ADASA"""

    output_file = "TRANSMITTAL N6 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N6 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-006-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    # Abrir documento y agregar contenido
    doc = Document(output_file)

    # Limpiar contenido de ejemplo generado por template ADASA
    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(
            x in texto
            for x in [
                "RESUMEN EJECUTIVO",
                "INTRODUCCION",
                "INTRODUCCIÓN",
                "1. INTRO",
                "ESTE DOCUMENTO HA SIDO GENERADO",
                "AGREGUE AQUI EL CONTENIDO",
                "AGREGUE AQUÍ EL CONTENIDO",
            ]
        ):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== 1. EXECUTIVE SUMMARY =====
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 4 - REJECTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water Delivery 13 carries a Transmittal Verdict of 4 \u2014 Rejected. "
        "Two of the seven submitted documents are formally rejected: the Feed "
        "Turbocharger Datasheet Rev C and the Valve List Rev B. The five remaining "
        "documents are approved as noted. ADASA acknowledges the resolution of "
        "several historical items (Pt-100 sensors, PLC 50Hz, A/C configuration) "
        "addressed in this delivery."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The rejection of the Feed Turbocharger datasheet is driven by a critical "
        "engineering regression: BW Water has unilaterally downgraded the HP "
        "coupling from the contractual baseline of 2,000 psi (138 bar) to 1,200 psi "
        "(82.7 bar) standard-RO rating. This reduction leaves a critically deficient "
        "19% safety margin over the operating pressure and introduces severe failure "
        "risks into the UHPRO circuit. Contractual design safety margins cannot be "
        "compromised to accommodate 'out of stock' logistical constraints."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The rejection of the Valve List Rev B is driven by a process QA failure: "
        "BW Water formally declared in the CCS that duplicate TAGs VM-09-015 and VE-09-008 "
        "had been resolved, yet neither correction was applied in the submitted document. "
        "Rev B additionally introduces two new duplicate TAGs (VE-09-009 items 58/93, "
        "VM-09-065 items 30/76). A systematic review of all 109 TAGs is required for Rev C "
        "before the document can support SCADA and control system design."
    )
    aplicar_arial_12(para)

    # ===== 2. CRITICAL ROADBLOCK: FEED TURBOCHARGER COUPLING DOWNGRADE =====
    doc.add_heading("CRITICAL ROADBLOCK: FEED TURBOCHARGER COUPLING DOWNGRADE", level=1)

    para = doc.add_paragraph()
    para.add_run("Document: ").bold = True
    para.add_run("Datasheet of Feed Turbocharger Rev C (P22-ET-09-009-007)\n")
    para.add_run("Status: ").bold = True
    para.add_run("REJECTED")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Datasheet Rev C reduces the coupling pressure rating from 2,000 psi (Rev B, "
        "confirmed in Technical Proposal Rev1 \u2014 Justification of Mechanical "
        "Couplings/Joints in High Pressure) to 1,200 psi, citing that "
        "2,000 psi couplings are 'out of stock and considered a rare item.' This "
        "change is rejected on the following grounds:"
    )
    aplicar_arial_12(para)

    # Ground 1
    doc.add_heading("Ground 1 — Insufficient safety margin for UHPRO-rated HP circuit service", level=2)

    para = doc.add_paragraph()
    para.add_run(
        "Technical Proposal Rev1 \u2014 Justification of Mechanical Couplings/Joints "
        "in High Pressure \u2014 established 2,000 psi (138 bar) couplings "
        "uniformly across all six HP joints. This baseline provides a 1.64x safety "
        "margin at the highest-pressure joint (Joint 4, 83.9 bar)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The proposed 1,200 psi (82.7 bar) coupling operates at a maximum of "
        "69.53 bar at the Feed Turbocharger. This leaves a margin of only 1.19x "
        "(19%) \u2014 completely insufficient for high-pressure concentrated brine "
        "service with transient pressure events. Furthermore, if applied to the "
        "2nd stage (Joints 4 or 5), the 1,200 psi coupling would operate below "
        "the physical pressure of the fluid, guaranteeing failure."
    )
    aplicar_arial_12(para)

    doc.add_paragraph()
    add_simple_table(
        doc,
        [
            ("Parameter", "Value"),
            ("Joint 2 max operating pressure (Feed Turbo outlet)", "69.53 bar = 1,009 psi"),
            ("Coupling rating Rev B baseline", "2,000 psi (138 bar)"),
            ("Coupling rating Rev C proposed", "1,200 psi (82.7 bar)"),
            ("Resulting safety margin", "1.19x (19%) — INADEQUATE"),
        ],
    )

    # Ground 2
    doc.add_heading("Ground 2 — Change of product class, not equivalent substitution", level=2)

    para = doc.add_paragraph()
    para.add_run(
        "The 2,000 psi coupling (Piedmont Style H) is specifically classified for "
        "'HPB Energy Recovery turbochargers'. The 1,200 psi coupling (Piedmont Style D) "
        "is classified for 'standard RO service'. BW Water is substituting a "
        "high-performance engineered component with a lower-tier product without "
        "technical justification."
    )
    aplicar_arial_12(para)

    # Ground 3 — Breach of prior formal commitment
    doc.add_heading(
        "Ground 3 \u2014 Breach of formal commitment in Submittal 25007-0002 CCS",
        level=2,
    )
    para = doc.add_paragraph()
    para.add_run(
        "In BW Water's own consolidated comment sheet for Submittal 25007-0002 "
        "(January 22, 2026, Entrega 8), BW Water formally responded to ADASA's "
        "observation requesting CL900 specification with the following commitment: "
        "'BW will provide coupling rated 2000 psi.' This statement applies to "
        "both the Feed Turbocharger and the Interstage Turbocharger. A formal "
        "commitment in a submitted CCS constitutes a contractual undertaking. "
        "Rev C violates this commitment without ADASA's approval."
    )
    aplicar_arial_12(para)

    # Actions
    doc.add_heading("Required Actions for Rev D (URGENT)", level=2)
    
    req_actions = [
        "Revert immediately to the coupling rated \u2265 2,000 psi with EPDM seals "
        "(Piedmont Style H or equivalent). Alternatively, propose flanged CL900 "
        "or welded connection as offered in Technical Proposal Rev1 \u2014 "
        "Justification of Mechanical Couplings/Joints in High Pressure.",
        "Confirm whether the HPB-60 delivered is the Standard model (MAWP 83 bar) "
        "or the Ultra model (MAWP 124 bar). Provide justification of equipment "
        "rating against the system design pressure of 120 bar.",
        "Explicitly document vibration sensor mounting provision in both Turbocharger "
        "datasheets per ET 5.5.7.",
    ]

    for i, action in enumerate(req_actions, 1):
        para = doc.add_paragraph(f"{i}. {action}")
        aplicar_arial_12(para)

    # Path to Resolution
    doc.add_heading("Path to Resolution \u2014 Feed Turbocharger (Code 4 \u2192 Code 2)", level=2)

    para = doc.add_paragraph()
    para.add_run(
        "ADASA confirms a technically acceptable path forward: upgrade the Feed TC coupling to "
        "\u2265 1,800 psi AND submit the coupling manufacturer\u2019s datasheet (model, MAWP, HPB service "
        "certification) for both turbochargers (SIP-09-001 and SIP-09-002). Under these conditions, "
        "ADASA would revise the verdict from Code 4 to Code 2. ADASA\u2019s preferred solution remains "
        "the return to 2,000 psi (Piedmont Style H), which constituted the contractual baseline."
    )
    aplicar_arial_12(para)

    # Actions - Valve List
    doc.add_heading("Required Actions for Valve List Rev C", level=2)

    valve_actions = [
        "Assign unique TAGs to all duplicate pairs: VM-09-015 (items 18 and 43), "
        "VE-09-008 (items 44 and 57), VE-09-009 (items 58 and 93), "
        "VM-09-065 (items 30 and 76). Each valve in the module must carry a "
        "unique instrument tag to enable unambiguous SCADA addressing and P&ID referencing.",
        "Perform a systematic review of all 109 valve entries to identify any "
        "additional duplicate TAGs or incorrect area codes before submitting Rev C.",
    ]
    for i, action in enumerate(valve_actions, 1):
        para = doc.add_paragraph(f"{i}. {action}")
        aplicar_arial_12(para)


    # ===== 3. STATUS OF OTHER SUBMITTED DOCUMENTS =====
    doc.add_heading("STATUS OF OTHER SUBMITTED DOCUMENTS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "The following table summarizes the evaluation of the remaining documents "
        "included in BW Water Delivery 13. Resolution of past items (Pt-100, 50Hz, "
        "A/C config) is noted and approved."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Verdict", "Key Notes / Action Required"),
            (
                "P22-LI-09-005-002",
                "Valve List",
                "B",
                "4 - REJECTED",
                "QA FAILURE — CCS declared VM-09-015 (items 18/43) and VE-09-008 (items 44/57) "
                "as resolved. Neither was corrected in Rev B. Two new duplicates introduced: "
                "VE-09-009 (items 58/93, ratings 900#/150#) and VM-09-065 (items 30/76). "
                "Rev C must assign unique TAGs to all 109 valves before document can be used "
                "for SCADA and P&ID finalization.",
            ),
            (
                "P22-ET-09-009-002",
                "DS RO HP Feed Pump",
                "C",
                "2 - APPROVED AS NOTED",
                "Pt-100 sensors and vibration mounting confirmed (CLOSED). Unify power "
                "rating references internally (93 kW nameplate vs 78.5 kW load).",
            ),
            (
                "P22-ET-09-009-008",
                "DS Interstage Turbo.",
                "C",
                "2 - APPROVED AS NOTED",
                "Coupling accepted at 1,800 psi (1.46x margin) conditional to FEDCO "
                "written confirmation of MAWP under service conditions. "
                "Coupling manufacturer's datasheet not included in Rev C submission — "
                "must be submitted with next revision (condition for maintaining Code 2).",
            ),
            (
                "P22-LI-09-009-001",
                "Utility Consumption",
                "B",
                "2 - APPROVED AS NOTED",
                "PLC 50Hz and A/C n+1 confirmed (CLOSED). A/C thermal calculation "
                "document remains pending.",
            ),
            (
                "P22-ET-09-009-005",
                "DS RO Cartridge Filter",
                "C",
                "2 - APPROVED AS NOTED",
                "12 cartridges justified. Nozzle orientation change must be reflected "
                "in layout/isometrics.",
            ),
            (
                "P22-ET-09-009-012",
                "DS Static Mixer",
                "B",
                "2 - APPROVED AS NOTED",
                "FRP material and dimensions accepted. Discrepancy with P&ID on TAG "
                "numbering must be resolved.",
            ),
        ],
    )


    # ===== 4. PENDING ACTIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING ACTIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water remains delinquent on the following critical observations "
        "transmitted in previous review cycles:"
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Item", "Origin", "Days Open", "Action Required"),
            (
                "Coupling Datasheets \u2014 Both TCs",
                "TM N6 (NEW)",
                "NEW",
                "Submit coupling manufacturer\u2019s datasheets for SIP-09-001 (Feed TC) and "
                "SIP-09-002 (Interstage TC): model number, MAWP, HPB service certification.",
            ),
            (
                "Modbus TCP Memory Map",
                "TM N2",
                "51 days",
                "Program not started. Delivery date required immediately.",
            ),
            (
                "A/C Thermal Calculation",
                "TM N2",
                "51 days",
                "Document required to validate A/C datasheet.",
            ),
            (
                "IO List Update",
                "TM N3",
                "30 days",
                "Incorporate Ethernet IP and digital stop coordination signals.",
            ),
            (
                "UPS in BOM",
                "TM N4",
                "22 days",
                "Confirm inclusion of 8h autonomy UPS in module scope.",
            ),
        ],
    )

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
