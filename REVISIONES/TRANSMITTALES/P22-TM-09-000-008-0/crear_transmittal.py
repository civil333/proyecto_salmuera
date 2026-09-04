#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N8 ADASA-BW_WATER
Entregas E15 (25007-0015) y E16 (25007-0016)
Fecha: 09-Mar-2026

Veredicto: 3 - TO BE REVISED
Documentos:
  - P22-LI-09-008-003 Rev B   Instrument List               → 3 - To be Revised
  - P22-LI-09-008-005 Rev A   Conductivity Analyzer DS      → 2 - Approved as Noted
  - P22-LI-09-008-006 Rev A   DP Switch DS                  → 1 - Approved
  - P22-LI-09-008-007 Rev A   Flow Transmitter DS           → 2 - Approved as Noted
  - P22-LI-09-008-008 Rev A   Level Switch DS               → 2 - Approved as Noted
  - P22-LI-09-008-009 Rev A   Level Transmitter DS          → 1 - Approved
  - P22-LI-09-008-010 Rev A   pH/ORP Analyzer DS            → 1 - Approved
  - P22-LI-09-008-011 Rev A   Pressure Gauge DS             → 1 - Approved
  - P22-LI-09-008-012 Rev A   Pressure Transmitter DS       → 2 - Approved as Noted
  - P22-DWG-09-007-005 Rev A  Power Works Installation DWG  → 3 - To be Revised
  - P22-LI-09-008-013 Rev A   Temperature Transmitter DS    → 3 - To be Revised
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
    """Genera el Transmittal N8 en formato ADASA"""

    output_file = "TRANSMITTAL N8 ADASA-BW_WATER.docx"

    # Crear documento base con template ADASA
    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N8 - SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-008-0",
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
    para.add_run("TRANSMITTAL VERDICT: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Eleven documents reviewed across Deliveries 15 and 16. Four approved; "
        "four approved as noted; three to be revised. Instrument List Rev B "
        "incorporates the vibration transmitters and motor RTDs requested in previous "
        "transmittals \u2014 two long-standing technical gaps now closed."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Three issues require revision. CIT-09-005 in the Instrument List specifies "
        "120VAC \u2014 every other instrument operates at 24VDC. The Power Works "
        "Installation Drawing (P22-DWG-09-007-005) contains no grounding or earthing "
        "specifications. The Temperature Transmitter datasheet covers TIT-09-003, a "
        "tag absent from Instrument List Rev B with no IO point assigned. IO List "
        "Rev B must be submitted incorporating the seven new instruments from this "
        "revision."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The three brine-side conductivity transmitters (CIT-09-001, CIT-09-004, "
        "CIT-09-005) specify a 20\u00a0mS/cm maximum range. Design feed TDS of "
        "43,000\u201353,000\u00a0mg/L implies expected conductivities well above "
        "this limit. BW Water must provide measured conductivity values for the "
        "Taltal brine and correct ranges in Rev C if the 20\u00a0mS/cm limit is "
        "insufficient."
    )
    aplicar_arial_12(para)

    # ===== 2. GENERAL INFORMATION =====
    doc.add_heading("GENERAL INFORMATION", level=1)

    add_simple_table(
        doc,
        [
            ("Field", "Value"),
            ("Submittal 1", "25007-0015"),
            ("Submittal 2", "25007-0016"),
            ("Delivery date", "09-Mar-2026"),
            ("Review completion", "09-Mar-2026"),
            ("Total documents in submittal", "11"),
            (
                "Response code summary",
                "4\u00d7 Code 1 (Approved), 4\u00d7 Code 2 (Approved as Noted), "
                "3\u00d7 Code 3 (To be Revised)",
            ),
            ("Contract", "C-4300 BW WATER SUPPLY-12803 V2"),
        ],
    )

    # ===== 3. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 3.1 Instrument List Rev B ---
    doc.add_heading(
        "Instrument List Rev B \u2014 P22-LI-09-008-003", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B adds seven instruments addressing observations raised in previous "
        "transmittals. The list now includes the required vibration transmitters and "
        "motor temperature sensors. One anomaly prevents acceptance."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Key additions confirmed in Rev B:").bold = True
    aplicar_arial_12(para)

    additions = [
        "VT-09-001 (ifm VTV122, 4-20mA): Vibration monitoring \u2014 HP Pump",
        "VT-09-002 (ifm VTV122, 4-20mA): Vibration monitoring \u2014 Feed Turbocharger",
        "VT-09-003 (ifm VTV122, 4-20mA): Vibration monitoring \u2014 Interstage Turbocharger",
        "TE-09-001 / TE-09-002 (Fedco Pt-100, 3-wire, DIN 44082): Bearing and winding temperature \u2014 HP Pump motor",
        "TE-09-003 / TE-09-004 (Grundfos Pt-100, 3-wire, DIN 44082): Bearing and winding temperature \u2014 CIP Pump motor",
    ]
    for item in additions:
        para = doc.add_paragraph(f"\u2022 {item}")
        aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Conductivity coverage is confirmed at all five locations required by "
        "ET \u2014 Conductivity Analyzers (feed, train permeate, Stage 2 permeate, "
        "Stage 1 reject, train reject). Electromagnetic flowmeters are confirmed at "
        "all five required locations. The duplicate FIT-09-001 TAG, which assigned "
        "the same number to two instruments in Rev A, has been corrected: the "
        "2nd Stage Permeate flow transmitter is now correctly identified as FIT-09-002."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 CIT-09-005 power supply: 120VAC inconsistent with "
        "project voltage distribution (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "Item 25 (CIT-09-005, RO Train Reject Conductivity Analyzer, Rosemount "
        "228/1056) specifies 120VAC power supply. Every other instrument in the "
        "list is 24VDC. The transmitter part number 1056-02-21-31-HT-UL confirms "
        "a deliberate AC-supply selection \u2014 the \u201c-02-\u201d position "
        "identifies the AC-powered variant of the 1056."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must confirm whether 220VAC was the intended supply voltage "
        "(correct the Instrument List accordingly) or provide the single-line "
        "diagram for a 120VAC distribution circuit within the module. Note: "
        "ADASA supplies 380VAC at the module terminals; 120VAC requires an "
        "additional step-down transformation not reflected in any submitted "
        "electrical drawing."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Voltages and Frequencies (380VAC module supply; "
        "220VAC/50Hz standard AC derivation; 24VDC instrument bus)"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 2 \u2014 IO List must be updated to reflect Rev B additions (MINOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "Rev B adds seven instrument points absent from IO List Rev A "
        "(VT-09-001, VT-09-002, VT-09-003, TE-09-001, TE-09-002, TE-09-003, "
        "TE-09-004) and revises two TAGs (FIT-09-002, LIT-09-002). "
        "IO List Rev B must be submitted incorporating all changes."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run("ET \u2014 Communication and Control System")
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 3 \u2014 Brine-side conductivity transmitters: range requires "
        "confirmation against actual process conductivity (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "CIT-09-001 (Module Feed Conductivity), CIT-09-004 (Stage 1 Reject "
        "Conductivity), and CIT-09-005 (RO Train Reject Conductivity) specify a "
        "maximum calibrated range of 20\u00a0mS/cm in Instrument List Rev B. "
        "ET \u2014 Feed Brine Quality establishes a design TDS range of "
        "43,000\u201353,000\u00a0mg/L for the module feed. At these concentrations, "
        "the expected conductivity of the feed brine is approximately 65\u201380\u00a0mS/cm "
        "\u2014 exceeding the 20\u00a0mS/cm upper limit of CIT-09-001. Reject streams "
        "carry more concentrated brine; the expected conductivities for CIT-09-004 "
        "and CIT-09-005 are higher still, in the range of 80\u2013140\u00a0mS/cm "
        "based on process mass balance."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must provide measured conductivity values for the Taltal brine "
        "at the three measurement points. If values exceed 20\u00a0mS/cm, correct "
        "the calibrated ranges for CIT-09-001, CIT-09-004, and CIT-09-005 in "
        "Instrument List Rev C."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Feed Brine Quality (design TDS 43,000\u201353,000\u00a0mg/L; "
        "conductivity-TDS relationship to be agreed); ET \u2014 Conductivity Analyzers"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 4 \u2014 Vibration transmitters: alarm and interlock setpoints "
        "not defined (MINOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "VT-09-001, VT-09-002, and VT-09-003 (ifm VTV122, 0\u201325\u00a0mm/s RMS, "
        "4-20mA) are correctly listed for the HP Pump and both turbochargers. "
        "The Instrument List does not define alarm or trip thresholds for any of the "
        "three points. BW Water must submit alarm and interlock setpoints for each; "
        "ISO 10816-3 provides standard reference values."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Vibration Transmitters: HP Pump and ERD units"
    )
    aplicar_arial_12(para)

    # --- 3.2 Conductivity Analyzer ---
    doc.add_heading(
        "Datasheet of Conductivity Analyzer Rev A \u2014 P22-LI-09-008-005",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The datasheet covers five conductivity analyzers: Rosemount 400 contacting "
        "sensor with 1056 transmitter (CIT-09-001 through CIT-09-004) and Rosemount "
        "228 toroidal sensor with 1056 transmitter (CIT-09-005, concentrated brine "
        "reject). Both configurations output 4-20mA HART. The toroidal sensor for "
        "the concentrated brine reject is technically appropriate for the service. "
        "Note: the transmitter part number for CIT-09-005 (1056-02-21-31-HT-UL vs. "
        "1056-03-20-30-HT-UL for the other four) confirms the AC-supply selection "
        "\u2014 this is the basis for \u00a73.1 Observation 1. No additional action "
        "required on this document."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 Cover page carries incorrect document code (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The title block on page 1 shows \u201cADASA Code: P22-LI-09-008-003.\u201d "
        "The correct code for this document is P22-LI-09-008-005. The technical "
        "content of the datasheet is not affected. BW Water should correct the "
        "document code in the next issued revision to maintain traceability."
    )
    aplicar_arial_12(para)

    # --- 3.3 DP Switch ---
    doc.add_heading(
        "Datasheet of Differential Pressure Switch Rev A \u2014 P22-LI-09-008-006",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Ashcroft 1132 differential pressure switch (DPS-09-001) provides an "
        "SPDT dry contact output (0\u201330 psi range) for cartridge filter differential "
        "pressure monitoring. The ON/OFF discrete output is appropriate for filter "
        "condition alarm and is consistent with the DI assignment in the Instrument "
        "List. Material (SS316L wetted parts) and ingress protection (NEMA 4X, IP66) "
        "are adequate for the service. No observations."
    )
    aplicar_arial_12(para)

    # --- 3.4 Flow Transmitter ---
    doc.add_heading(
        "Datasheet of Flow Transmitter Rev A \u2014 P22-LI-09-008-007",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "All five flow transmitters (FIT-09-001 through FIT-09-005) use the "
        "Rosemount 8750W electromagnetic flowmeter with 4-20mA and HART output, "
        "consistent with ET \u2014 Flowmeters (electromagnetic type, local "
        "indication, PLC transmission). The model selection (low-power DC variant) "
        "is compatible with the 24VDC instrument supply."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 FIT-09-004 electrode material: Hastelloy C-276 "
        "vs. SS316L for other FITs (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "FIT-09-001, 002, 003, and 005 specify SS316L electrodes. FIT-09-004 "
        "(RO Train Reject) specifies Hastelloy C-276 electrodes \u2014 "
        "appropriate for concentrated brine service. BW Water should update "
        "the Fluid/Medium field in the next revision to read \u201cConcentrated "
        "Brine\u201d to document the basis for the material upgrade."
    )
    aplicar_arial_12(para)

    # --- 3.5 Level Switch ---
    doc.add_heading(
        "Datasheet of Level Switch Rev A \u2014 P22-LI-09-008-008",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The IFM KQ6005 capacitive proximity switches (LS-09-001 and LS-09-002) "
        "provide high and low level detection for the antiscalant dosing tank. "
        "The PNP digital output is appropriate for level alarm service on the "
        "dosing tank, consistent with the DI assignment in the Instrument List."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 Datasheet incorrectly states output type as "
        "4-20mA HART (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Output/Communication field in the BW Water datasheet cover sheet "
        "reads \u201cCurrent Output, 4-20mA HART.\u201d The IFM KQ6005 is a "
        "discrete PNP digital proximity switch; its communication interface is "
        "IO-Link, not 4-20mA HART. The Instrument List Rev B correctly assigns "
        "IO type DI for LS-09-001 and LS-09-002. The datasheet field is a "
        "template error that does not affect the instrument selection. BW Water "
        "should correct this field in the next revision to prevent confusion "
        "during IO List verification and loop documentation."
    )
    aplicar_arial_12(para)

    # --- 3.6 Level Transmitter ---
    doc.add_heading(
        "Datasheet of Level Transmitter (Pressure Type) Rev A \u2014 "
        "P22-LI-09-008-009",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The VEGA VEGABAR 82 (CERTEC ceramic cell, gauge pressure, 4-20mA HART) "
        "provides continuous level measurement for the CIP tank (LIT-09-002). "
        "The FFKM (Kalrez) process seal is appropriate for CIP water service. "
        "The pressure-based measurement principle satisfies the ET requirement "
        "for a continuous level transmitter in the CIP wash tank. No observations."
    )
    aplicar_arial_12(para)

    # --- 3.7 pH/ORP Analyzer ---
    doc.add_heading(
        "Datasheet of pH/ORP Analyzer Rev A \u2014 P22-LI-09-008-010",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Rosemount 3900 sensor paired with the 1056 dual-channel transmitter "
        "covers both PHIT-09-001 (pH) and ORPIT-09-001 (ORP) on the CIP/flush "
        "circuit using two independent 4-20mA HART outputs. The instrument "
        "selection is consistent with the Instrument List Rev B and adequate "
        "for the CIP water service. No observations."
    )
    aplicar_arial_12(para)

    # --- 3.8 Pressure Gauge ---
    doc.add_heading(
        "Datasheet of Pressure Gauge Rev A \u2014 P22-LI-09-008-011",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Wika 233.50 Bourdon tube gauges cover PI-09-001 through PI-09-006. "
        "PI-09-001 and PI-09-002 are specified without diaphragm seal for filtered "
        "water service. PI-09-003 through PI-09-006 include the Wika 990.10 "
        "diaphragm seal with PTFE-lined wetted parts, appropriate for CIP and "
        "antiscalant service. No observations."
    )
    aplicar_arial_12(para)

    # --- 3.9 Pressure Transmitter ---
    doc.add_heading(
        "Datasheet of Pressure Transmitter Rev A \u2014 P22-LI-09-008-012",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Schneider Foxboro IGP05S transmitters (2-wire, loop-powered, 4-20mA "
        "HART) cover nine pressure points (PIT-09-001 through PIT-09-009). The "
        "datasheet applies two wetted material specifications: SS316L for "
        "PIT-09-001, 002, 003, 004, 005, and 009 (lower-pressure and permeate-side "
        "service), and Hastelloy C for PIT-09-006, 007, and 008."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 PIT-09-007 Hastelloy C material: confirm service "
        "conditions (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "PIT-09-006 (Stage 2 Reject) and PIT-09-008 (Train Reject) are on brine "
        "concentrate streams where Hastelloy C corrosion resistance is consistent "
        "with the service. PIT-09-007 (Interstage Turbo to Feed Turbocharger) "
        "is an inter-stage pressure point; its fluid composition should be "
        "confirmed to establish the basis for the Hastelloy C selection "
        "over SS316L."
    )
    aplicar_arial_12(para)

    # --- 3.10 Power Works DWG ---
    doc.add_heading(
        "Typical Installation Details of Power Works Rev A \u2014 "
        "P22-DWG-09-007-005",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The document covers seven standard electrical installation details: "
        "centrifugal pump motor wiring, dosing pump wiring, heater panel, "
        "PLC/LCP panel, and three cable tray mounting configurations (wall, "
        "ceiling, floor). Cable type specifications and tray segregation "
        "(power vs. I&C) are included and adequate."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 No grounding or earthing specifications (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The document contains no grounding or earthing specifications for any "
        "installation scenario \u2014 no equipment earth conductors, no tray "
        "bonding, and no shield termination guidance for instrument cables. "
        "Rev B must include:"
    )
    aplicar_arial_12(para)

    earthing_items = [
        "Equipment grounding conductor sizing and termination for centrifugal "
        "pump motors, dosing pump, and control panels.",
        "Cable tray bonding continuity requirements (HDG tray bonding or "
        "separate earth conductor).",
        "Analog/instrument cable shield termination method and grounding point.",
    ]
    for i, item in enumerate(earthing_items, 1):
        para = doc.add_paragraph(f"{i}. {item}")
        aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Motors and Electrical Equipment (motor protection requirements); "
        "ET \u2014 Electrical and Control Systems (grounding of control and "
        "instrumentation systems)"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 2 \u2014 No electrical installation standard cited (MINOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The drawing references \u201cinstallation standards\u201d without identifying "
        "the applicable code. BW Water must state the electrical installation "
        "standard governing the work \u2014 whether IEC 60364, IEC 61439, "
        "NFPA 70 (NEC), or the applicable Chilean standard \u2014 in the revision "
        "block or general notes of Rev B."
    )
    aplicar_arial_12(para)

    # --- 3.11 Temperature Transmitter DS ---
    doc.add_heading(
        "Datasheet of Temperature Transmitter Rev A \u2014 P22-LI-09-008-013",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The datasheet covers TIT-09-003 (CIP Tank Temperature Transmitter), "
        "comprising a Rosemount 214C RTD (Pt-100, 3-wire, SS316 sheath), "
        "Rosemount 114C thermowell (SS316/316L, tapered stem), and Rosemount "
        "644H transmitter (4-20mA HART, 24VDC, IP66). All three components "
        "satisfy ET \u2014 Instrumentation requirements for 4-20mA HART "
        "protocol and recognized manufacturers."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 1 \u2014 Document header carries incorrect type designation (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The cover page header reads \u201cDatasheet of Pressure Transmitter\u201d "
        "while the document is a Temperature Transmitter datasheet. The technical "
        "content is not affected. BW Water should correct the document type "
        "designation in the next revision."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 2 \u2014 TIT-09-003 not listed in Instrument List Rev B (MAJOR)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "TIT-09-003 (this datasheet) is not in Instrument List Rev B and has no "
        "IO assignment. IL Rev B item 28 lists TIT-09-001 as the only CIP Tank "
        "temperature transmitter. BW Water must:"
    )
    aplicar_arial_12(para)

    for i, item in enumerate(
        [
            "Add TIT-09-003 to the next Instrument List revision with its AI "
            "input point.",
            "Confirm whether TIT-09-001 and TIT-09-003 are distinct instruments "
            "at different locations, or whether one supersedes the other, and "
            "submit the datasheet for whichever tag remains unsubmitted.",
        ],
        1,
    ):
        para = doc.add_paragraph(f"{i}. {item}")
        aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Instrumentation (complete instrument registration); "
        "Instrument List Rev B item 28 (TIT-09-001 only)"
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation 3 \u2014 Sensor accuracy class not specified (NOTE)",
        level=3,
    )
    para = doc.add_paragraph()
    para.add_run(
        "The Rosemount 214C is available in standard (Class B) and Class A "
        "accuracy variants. The specification form does not indicate which "
        "accuracy class is required for TIT-09-003. For CIP process temperature "
        "measurement, the accuracy class should be documented to confirm the "
        "selected sensor meets the application requirement. BW Water should "
        "specify the required accuracy class in the next datasheet revision."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").bold = True
    para.add_run(
        "ET \u2014 Instrumentation (complete specification of instrument parameters)"
    )
    aplicar_arial_12(para)

    # ===== 5. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph(
        "The following BW Water documents were reviewed as part of this transmittal."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Attachment", "Document Code", "Title", "Rev"),
            ("1", "P22-LI-09-008-003", "Instrument List", "B"),
            ("2", "P22-LI-09-008-005", "Datasheet of Conductivity Analyzer", "A"),
            ("3", "P22-LI-09-008-006", "Datasheet of Differential Pressure Switch", "A"),
            ("4", "P22-LI-09-008-007", "Datasheet of Flow Transmitter", "A"),
            ("5", "P22-LI-09-008-008", "Datasheet of Level Switch", "A"),
            ("6", "P22-LI-09-008-009", "Datasheet of Level Transmitter (Pressure Type)", "A"),
            ("7", "P22-LI-09-008-010", "Datasheet of pH/ORP Analyzer", "A"),
            ("8", "P22-LI-09-008-011", "Datasheet of Pressure Gauge", "A"),
            ("9", "P22-LI-09-008-012", "Datasheet of Pressure Transmitter", "A"),
            ("10", "P22-DWG-09-007-005", "Typical Installation Details of Power Works", "A"),
            ("11", "P22-LI-09-008-013", "Datasheet of Temperature Transmitter", "A"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Annotated documents available at: ").bold = True
    para.add_run(
        "https://lrg.synology.me:6501/d/s/17OYEJDhTny4F9uWYd6uiudSdGkRMl9L/"
        "3pHSj9iAesPp2gfz0AMymx8byh_Rc5vY-CLMApYt-CQ0"
    )
    aplicar_arial_12(para)

    # ===== 6. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            ("P22-LI-09-008-003", "Instrument List", "B", "3 \u2014 To be Revised"),
            ("P22-LI-09-008-005", "Datasheet of Conductivity Analyzer", "A", "2 \u2014 Approved as Noted"),
            ("P22-LI-09-008-006", "Datasheet of Differential Pressure Switch", "A", "1 \u2014 Approved"),
            ("P22-LI-09-008-007", "Datasheet of Flow Transmitter", "A", "2 \u2014 Approved as Noted"),
            ("P22-LI-09-008-008", "Datasheet of Level Switch", "A", "2 \u2014 Approved as Noted"),
            ("P22-LI-09-008-009", "Datasheet of Level Transmitter (Pressure Type)", "A", "1 \u2014 Approved"),
            ("P22-LI-09-008-010", "Datasheet of pH/ORP Analyzer", "A", "1 \u2014 Approved"),
            ("P22-LI-09-008-011", "Datasheet of Pressure Gauge", "A", "1 \u2014 Approved"),
            ("P22-LI-09-008-012", "Datasheet of Pressure Transmitter", "A", "2 \u2014 Approved as Noted"),
            ("P22-DWG-09-007-005", "Typical Installation Details of Power Works", "A", "3 \u2014 To be Revised"),
            ("P22-LI-09-008-013", "Datasheet of Temperature Transmitter", "A", "3 \u2014 To be Revised"),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
