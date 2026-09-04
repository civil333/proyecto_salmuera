#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N14 ADASA-BW_WATER (executive version)
Entregas E26 (25007-0026) + E27 (25007-0027) + E28 (25007-0028) + E29 (25007-0029)
Fecha: 15-Apr-2026

Veredicto global: 2 - APPROVED AS NOTED

Documentos (11):
  - P22-CD-09-004-001 Rev D   Control System Architecture        -> 1 - Approved
  - P22-LI-09-005-002 Rev D   Valve List                         -> 2 - Approved as Noted
  - P22-LI-09-008-011 Rev B   DS Pressure Gauge                  -> 1 - Approved
  - P22-LI-09-008-001 Rev C   I/O List                           -> 2 - Approved as Noted
  - P22-LI-09-008-003 Rev C   Instrument List                    -> 2 - Approved as Noted
  - P22-LI-09-008-004 Rev B   Data Transfer List (Modbus TCP/IP) -> 2 - Approved as Noted
  - P22-LI-09-008-005 Rev B   DS Conductivity Analyzer           -> 1 - Approved
  - P22-LI-09-008-010 Rev B   DS pH/ORP Analyzer                 -> 1 - Approved
  - P22-LI-09-008-013 Rev B   DS Temperature Transmitter         -> 1 - Approved
  - P22-LI-09-008-014 Rev B   DS Vibration Transmitter           -> 1 - Approved
  - P22-LI-09-008-007 Rev B   DS Flow Transmitter                -> 1 - Approved

Observaciones cerradas (12):
  - TM N10 OBS-01/02/03/04, TM N11 OBS-01/02/NOTE-01,
    TM N12 OBS-01/NOTE-01, TM N8 OBS-01/02/03

Notas nuevas (5): NOTE-01 thru NOTE-05
5 items heredados open.
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "..", ".claude", "skills", "template-adasa",
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
    output_file = "TRANSMITTAL N14 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N14 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-014-0",
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

    # ===================================================================
    # 1. EXECUTIVE SUMMARY
    # ===================================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    para = doc.add_paragraph()
    para.add_run("TRANSMITTAL VERDICT: 2 \u2014 APPROVED AS NOTED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Eleven documents reviewed from four deliveries (E26 April\u00a08, "
        "E27 April\u00a010, E28 April\u00a013, E29 April\u00a015). Seven "
        "approved without observations, four approved as noted. Twelve "
        "previous observations closed. Five remain open. Five notes raised "
        "\u2014 two major, three minor."
    )
    aplicar_arial_12(para)

    # Key findings bullets
    bullets = [
        "Vibration transmitters changed from IFM VTV122 to Wilcoxon "
        "PCH420V-M12; HART\u00a07.0 deficiency from Transmittal\u00a0N12 "
        "resolved.",
        "Conductivity sensor technology split confirmed: toroidal "
        "(Rosemount\u00a0228) for brine, contacting (Rosemount\u00a0400) "
        "for permeate.",
        "Valve List TAG uniqueness verified across 111 items; all previous "
        "duplicates resolved.",
        "Flow transmitter FIT-09-004 fluid medium corrected to "
        "\u201cConcentrated Brine\u201d; power supply aligned to "
        "12\u201342\u00a0VDC. Both Transmittal\u00a0N8 notes resolved.",
        "Analyzer power supply voltage discrepancy (220VAC vs 24VDC) "
        "requires alignment before IFC.",
        "Five previous observations remain open, three dependent on pending "
        "Equipment Layout Rev\u00a0B.",
    ]
    for b in bullets:
        para = doc.add_paragraph()
        para.add_run("\u2013 " + b)
        aplicar_arial_12(para)

    # ===================================================================
    # 2. DETAILED OBSERVATIONS BY DOCUMENT
    # ===================================================================
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # -------------------------------------------------------------------
    # 2.1 Control System Architecture Rev D
    # -------------------------------------------------------------------
    doc.add_heading(
        "Control System Architecture Rev\u00a0D \u2014 P22-CD-09-004-001",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-04 \u2014 CLOSED: ").bold = True
    para.add_run(
        "UPS battery module UPS-BAT\u00a0B/PU/FF/24DC/40AH confirmed, two "
        "units, 8-hour runtime at 4.35\u00a0A full load. Calculation: "
        "40\u00a0Ah / 4.35\u00a0A = 9.2\u00a0hours, exceeding the 8-hour "
        "ET requirement. UPS load breakdown should be documented in Control "
        "Philosophy Rev\u00a0B for commissioning reference."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.2 Valve List Rev D
    # -------------------------------------------------------------------
    doc.add_heading(
        "Valve List Rev\u00a0D \u2014 P22-LI-09-005-002", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "111 items verified for TAG uniqueness, area-code correctness, "
        "and actuation compliance."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N11 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "VE-09-007 no longer duplicated. Item\u00a044 retains VE-09-007 "
        "(DN80 butterfly, motorized, SWRO Reject 1st Stage). Former "
        "item\u00a064 reassigned to VM-09-120 (DN15 ball valve, manual, "
        "SWRO 2nd Stage Reject). Both verified against P&ID Rev\u00a0C."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N11 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run(
        "PSV-09-002 no longer duplicated. Item\u00a0104 retains PSV-09-002. "
        "Item\u00a0112 removed \u2014 list reduced from 112 to 111 items. "
        "See NOTE-01."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N11 NOTE-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Area-07 TAGs corrected. VM-07-005 \u2192 VM-09-005, "
        "VM-07-031 \u2192 VM-09-031, VE-07-009 \u2192 VE-09-009. "
        "No area-07 TAGs remain."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal\u00a0N6 Duplicate TAGs \u2014 CLOSED: "
    ).bold = True
    para.add_run(
        "Four original duplicates (VM-09-015, VE-09-008, VE-09-009, "
        "VM-09-065) fully resolved. Renamed TAGs verified against "
        "P&ID Rev\u00a0C."
    )
    aplicar_arial_12(para)

    # NOTE-01
    doc.add_heading(
        "NOTE-01 \u2014 Safety relief valve item 112 removal requires "
        "justification (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Item\u00a0112 (second PSV-09-002, safety relief valve) removed "
        "rather than assigned a unique TAG. BW\u00a0Water must provide the "
        "overpressure protection analysis confirming that the remaining PSV "
        "configuration is adequate for the antiscalant system, or reinstate "
        "the valve with a unique TAG prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").italic = True
    para.add_run("ET \u2014 Safety and Relief Valves").italic = True
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.3 Datasheet of Pressure Gauge Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of Pressure Gauge Rev\u00a0B \u2014 P22-LI-09-008-011",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Diaphragm seal changed from Wika\u00a0990.10 (SS lower body) to "
        "Wika\u00a0990.31 (polypropylene, EPDM/PTFE) for PI-09-003 through "
        "PI-09-006, for PVC piping compatibility in CIP and antiscalant "
        "service. Technically appropriate."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.4 I/O List Rev C
    # -------------------------------------------------------------------
    doc.add_heading(
        "I/O List Rev\u00a0C \u2014 P22-LI-09-008-001", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "141 items (was 112 in Rev\u00a0B). New additions: VE-09-015 "
        "(Feed TC Isolation, Ethernet/IP), TIT-09-006 (CIP Tank "
        "Temperature, AI), PHIT-09-006 (CIP pH Analyzer, AI)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Motor temperature tags remain TE, not TIT. BW\u00a0Water\u2019s "
        "justification accepted: the 5069-IY4 universal input module reads "
        "RTD resistance directly without a 4\u201320\u00a0mA transmitter "
        "loop, making TE (Temperature Element) the correct ISA designation. "
        "TIT-09-003 service conflict resolved \u2014 CIP Pump motor "
        "temperatures are now TE-09-003 (winding) and TE-09-004 (bearing); "
        "CIP Tank process temperature is TIT-09-006 (Rosemount\u00a0644 "
        "transmitter, 4\u201320\u00a0mA on 5069-IF8). All motor sensors "
        "specified as Pt-100, 3-wire RTD per ET \u2014 Motors and "
        "Electrical Equipment."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run("Verified in Data Transfer List Rev\u00a0B (Section\u00a02.6).")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-03 \u2014 CLOSED: ").bold = True
    para.add_run("Verified in Data Transfer List Rev\u00a0B (Section\u00a02.6).")
    aplicar_arial_12(para)

    # NOTE-02
    doc.add_heading(
        "NOTE-02 \u2014 Analyzer power supply voltage discrepancy (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "IO List REMARKS specifies \u201c220VAC Supply\u201d for "
        "ORPIT-09-001A, CIT-09-001B, CIT-09-004, CIT-09-005, and "
        "PHIT-09-006. Instrument List Rev\u00a0C specifies 24VDC for all "
        "instruments, confirmed by CCS. These five analyzers handle brine "
        "quality and pH monitoring \u2014 an incorrect voltage specification "
        "in either document will result in equipment damage or interface "
        "circuit redesign during commissioning. BW\u00a0Water must resolve "
        "this discrepancy and confirm the definitive supply voltage prior "
        "to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").italic = True
    para.add_run("ET \u2014 Instrumentation").italic = True
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.5 Instrument List Rev C
    # -------------------------------------------------------------------
    doc.add_heading(
        "Instrument List Rev\u00a0C \u2014 P22-LI-09-008-003", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "39 instruments. Vibration transmitters changed to Wilcoxon "
        "PCH420V-M12 (was IFM VTV122), HART\u00a07.0 confirmed. Motor "
        "temperature sensors registered: TE-09-001/002 (Fedco PT100, HP "
        "Pump), TE-09-003/004 (Grundfos PT100, CIP Pump), TIT-09-006 "
        "(Rosemount 214C+644, CIP Tank)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run("CIT-09-005 power supply corrected to 24VDC.")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run("IO List and Instrument List aligned.")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-03 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Conductivity ranges corrected. CIT-09-001B, CIT-09-004, "
        "CIT-09-005 now 0\u2013200\u00a0mS/cm with Rosemount\u00a0228 "
        "toroidal sensors. CIT-09-002 and CIT-09-003 (permeate) retain "
        "0\u201320\u00a0mS/cm with Rosemount\u00a0400 contacting sensors. "
        "Technology split is appropriate: toroidal for brine above "
        "20\u00a0mS/cm, contacting for permeate."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-04 \u2014 OPEN: ").bold = True
    para.add_run(
        "Vibration alarm setpoints deferred to separate \u201cAlarm and "
        "Interlock Setpoints\u201d document, not yet submitted. Tracked for "
        "IFC, not carried forward in Section\u00a03."
    )
    aplicar_arial_12(para)

    # NOTE-03
    doc.add_heading(
        "NOTE-03 \u2014 Vibration transmitter calibrated range (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Instrument List shows 0\u2013127\u00a0mm/s for VT-09-001/002/003. "
        "Data Transfer List uses 0\u201325\u00a0mm/s. Wilcoxon PCH420V-M12 "
        "supports programmable full-scale from 12.7 to 127\u00a0mm/s. "
        "BW\u00a0Water should confirm the intended PLC scaling and align "
        "both documents prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").italic = True
    para.add_run("ET \u2014 Vibration Transmitters").italic = True
    aplicar_arial_12(para)

    # NOTE-04
    doc.add_heading(
        "NOTE-04 \u2014 Working medium label for brine-side instruments (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "\u201cWorking Medium\u201d column shows \u201cFiltered Water\u201d "
        "for CIT-09-001B, CIT-09-004, CIT-09-005, PIT-09-007, PIT-09-006, "
        "FIT-09-004, and PIT-09-008. These instruments operate in "
        "concentrated brine service (TDS > 43,000\u00a0mg/L). Working "
        "medium designation should reflect actual service conditions prior "
        "to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").italic = True
    para.add_run("ET \u2014 Feed Brine Quality").italic = True
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.6 Data Transfer List (Modbus TCP/IP) Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Data Transfer List (Modbus TCP/IP) Rev\u00a0B \u2014 P22-LI-09-008-004",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "189 Modbus entries (digital + analog). New entries: VE-09-015 "
        "(Feed TC Isolation, 6 entries), TIT-09-006 (register 30028), "
        "PHIT-09-006 (register 30031), TE-09-003/004 (registers "
        "40077/40078)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Motor temperature tags consistent with IO List Rev\u00a0C. "
        "TE-09-001/002 (HP Pump) mapped to 5069-IY4 at holding registers "
        "40075\u201340076, REAL data type (direct RTD reading). "
        "TE-09-003/004 (CIP Pump) at registers 40077\u201340078, same "
        "architecture. TIT-09-006 (CIP Tank) mapped to 5069-IF8 at input "
        "register 30028, 4000\u201320000 scaling (4\u201320\u00a0mA "
        "transmitter). The TE/TIT distinction is architecturally consistent "
        "across all three instrumentation documents."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Conductivity scaling corrected. CIT-09-001B (register 30004): "
        "0\u2013200\u00a0mS/cm. CIT-09-004 (register 30015): "
        "0\u2013200\u00a0mS/cm. CIT-09-005 (register 30023): "
        "0\u2013200\u00a0mS/cm. Permeate instruments CIT-09-002 (register "
        "30019) and CIT-09-003 (register 30021): 0\u2013200\u00a0uS/cm "
        "\u2014 microsiemens, appropriate for low-conductivity permeate."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N10 OBS-03 \u2014 CLOSED: ").bold = True
    para.add_run(
        "VE-09-014 has four entries (DI: 10004.6 IN REMOTE, 10004.7 FAULT; "
        "Analog: 40039 feedback, 40071 control) \u2014 duplication resolved. "
        "LS-09-001 present at 10002.5, LS-09-002 at 10002.6 \u2014 "
        "omissions resolved."
    )
    aplicar_arial_12(para)

    # NOTE-05
    doc.add_heading(
        "NOTE-05 \u2014 Vibration transmitter Modbus scaling (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "VT-09-001/002/003 Modbus scaled range shows 0\u201325\u00a0mm/s "
        "(registers 30007, 30011, 30016). Consistent with previous IFM "
        "VTV122 specification but may need updating for Wilcoxon "
        "PCH420V-M12. Align with Instrument List calibrated range (see "
        "NOTE-03) prior to IFC (Rev\u00a00)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Technical Basis: ").italic = True
    para.add_run("ET \u2014 Instrumentation").italic = True
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.7 Datasheet of Conductivity Analyzer Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of Conductivity Analyzer Rev\u00a0B \u2014 P22-LI-09-008-005",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Two sensor technologies properly specified:")
    aplicar_arial_12(para)

    # Bullet: CIT-09-002/003 (permeate)
    para = doc.add_paragraph()
    para.add_run("CIT-09-002/003 (permeate): ").bold = True
    para.add_run(
        "Rosemount\u00a0400, contacting electrode, SS316/titanium, "
        "0.1\u00a0uS/cm to 2,000\u00a0uS/cm."
    )
    aplicar_arial_12(para)

    # Bullet: CIT-09-001B/004/005 (brine)
    para = doc.add_paragraph()
    para.add_run("CIT-09-001B/004/005 (brine): ").bold = True
    para.add_run(
        "Rosemount\u00a0228, toroidal non-contacting, Tefzel, "
        "0.1\u00a0uS/cm to 2,000,000\u00a0uS/cm. Fluid medium identified "
        "as \u201cRO Stage 1 & 2 Reject.\u201d"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The contacting-to-toroidal technology change for brine service "
        "addresses the concern raised in Transmittal\u00a0N8 OBS-03 and "
        "Transmittal\u00a0N10 OBS-02. Tefzel provides adequate resistance "
        "to concentrated chloride solutions (45,000\u201355,000\u00a0ppm "
        "Cl\u207b in second stage reject)."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.8 Datasheet of pH/ORP Analyzer Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of pH/ORP Analyzer Rev\u00a0B \u2014 P22-LI-09-008-010",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "TAG alignment changes only: ORPIT-09-001 renamed to "
        "ORPIT-09-001A, PHIT-09-001 renamed to PHIT-09-006, per "
        "P&ID Rev\u00a0C. Rosemount\u00a03900/1056 configuration unchanged."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.9 Datasheet of Temperature Transmitter Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of Temperature Transmitter Rev\u00a0B \u2014 P22-LI-09-008-013",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "TIT-09-006 (CIP Tank): Rosemount\u00a0214C RTD (PT100, Class\u00a0A, "
        "wire-wound RW) with 644 head-mount transmitter, 4\u201320\u00a0mA "
        "+ HART, flange DN40."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Header corrected from \u201cPressure Transmitter\u201d to "
        "\u201cTemperature Transmitter.\u201d"
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-02 \u2014 CLOSED: ").bold = True
    para.add_run(
        "TAG corrected from TIT-09-003 to TIT-09-006 per P&ID Rev\u00a0C. "
        "Aligned with Instrument List Rev\u00a0C and IO List Rev\u00a0C."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N8 OBS-03 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Accuracy Class\u00a0A specified. Part number in CCS indicates "
        "214CRWSSA1S3E0100SL (wire-wound RW, Class\u00a0A). Note: "
        "Instrument List Rev\u00a0C shows 214CRWSSA1S3E0120SL \u2014 the "
        "positional difference (0100 vs 0120) corresponds to sensor length "
        "(10\u201d vs 12\u201d). BW\u00a0Water should confirm the "
        "definitive part number before procurement."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.10 Datasheet of Vibration Transmitter Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of Vibration Transmitter Rev\u00a0B \u2014 P22-LI-09-008-014",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Model changed from IFM VTV122 to ")
    para.add_run("Wilcoxon PCH420V-M12").bold = True
    para.add_run(". Quantity corrected to 3 units.")
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N12 OBS-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Wilcoxon PCH420V-M12 provides 4\u201320\u00a0mA + HART\u00a07.0 "
        "as native capability. Three programmable analysis bands (PV, SV, "
        "TV). HART deficiency that caused Code\u00a03 in "
        "Transmittal\u00a0N12 is resolved."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Transmittal\u00a0N12 NOTE-01 \u2014 CLOSED: ").bold = True
    para.add_run(
        "Quantity field corrected from 1 to 3. Matches VT-09-001 (HP Pump), "
        "VT-09-002 (Feed Turbocharger), VT-09-003 (Interstage "
        "Turbocharger)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "ET compliance verified: 0\u2013127\u00a0mm/s programmable, "
        "10\u20131000\u00a0Hz, +/\u22125% accuracy, PZT shear, SS316L, "
        "IP67, 12\u201330\u00a0VDC."
    )
    aplicar_arial_12(para)

    # -------------------------------------------------------------------
    # 2.11 Datasheet of Flow Transmitter Rev B
    # -------------------------------------------------------------------
    doc.add_heading(
        "Datasheet of Flow Transmitter Rev\u00a0B \u2014 P22-LI-09-008-007",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Five Rosemount\u00a08750W electromagnetic flowmeters "
        "(FIT-09-001 through 005). Two specification sheets: page\u00a02 "
        "covers FIT-09-001/002/003/005 (filtered water and CIP service), "
        "page\u00a03 covers FIT-09-004 (train reject, concentrated brine "
        "service)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal\u00a0N8 Fluid/Medium note \u2014 RESOLVED: "
    ).bold = True
    para.add_run(
        "FIT-09-004 specification sheet now correctly identifies "
        "\u201cConcentrated Brine\u201d as the fluid medium. Rev\u00a0A "
        "carried \u201cFiltered/CIP Water,\u201d which was inconsistent "
        "with the actual service conditions (TDS 75,000\u201393,000\u00a0"
        "mg/L at second stage reject). The Nickel alloy\u00a0276 "
        "(Hastelloy\u00a0C-276) electrode selection for FIT-09-004 remains "
        "appropriate for this service. The four remaining flowmeters retain "
        "\u201cFiltered/CIP Water\u201d and SS316L electrodes, consistent "
        "with their actual service."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Transmittal\u00a0N8 Power Supply note \u2014 RESOLVED: "
    ).bold = True
    para.add_run(
        "Power supply field corrected from \u201c90 to 250\u00a0VDC\u201d "
        "(Rev\u00a0A) to \u201c12 to 42\u00a0VDC\u201d (Rev\u00a0B) on "
        "both specification sheets. Now aligned with IO List Rev\u00a0C "
        "(24\u00a0VDC, 4-wire) and the ordered variant prefix \u2018D\u2019 "
        "(low-power DC model)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "ET compliance confirmed: electromagnetic measurement, "
        "4\u201320\u00a0mA with HART, Rosemount (recognized manufacturer), "
        "PTFE lining, IP66, flanged process connections."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Note: Instrument List Rev\u00a0C still carries "
        "\u201cFiltered Water\u201d as Working Medium for FIT-09-004 \u2014 "
        "this is addressed in NOTE-04 (Section\u00a02.5) and remains "
        "applicable for the next IL revision."
    )
    aplicar_arial_12(para)

    # ===================================================================
    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    # ===================================================================
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "Twelve observations closed in this transmittal: TM\u00a0N10 "
        "OBS-01/02/03/04, TM\u00a0N11 OBS-01/02/NOTE-01, TM\u00a0N12 "
        "OBS-01/NOTE-01, TM\u00a0N8 OBS-01/02/03. Five remain open."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Obs", "Document", "Description", "Outstanding Since", "Status"),
            (
                "TM\u00a0N10\nOBS-05",
                "GA Antiscalant Dosing Tank",
                "Working volume, body material, seismic anchor data "
                "(NCh\u00a02369 Zone\u00a03) absent",
                "TM\u00a0N10\n(12-Mar-2026)",
                "PARTIALLY ADDRESSED \u2014 P&ID Rev\u00a0C shows "
                "0.34\u00a0m\u00b3. GA Rev\u00a0B still required",
            ),
            (
                "TM\u00a0N10\nNOTE-05",
                "HMI Screenshots\nP22-BREAD-09-008-001",
                "Committed at Transmittal\u00a0N4 \u2014 not submitted",
                "TM\u00a0N4\n(03-Feb-2026)",
                "OPEN \u2014 69\u00a0days outstanding",
            ),
            (
                "TM\u00a0N11\nOBS-03",
                "Grounding Point Layout Rev\u00a0B",
                "Equipment positions from rejected Piping Layout Rev\u00a0A",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending Equipment Layout Rev\u00a0B",
            ),
            (
                "TM\u00a0N11\nOBS-04",
                "Instrument Location Layout Rev\u00a0B",
                "Same basis as OBS-03",
                "TM\u00a0N11\n(17-Mar-2026)",
                "OPEN \u2014 pending Equipment Layout Rev\u00a0B",
            ),
            (
                "TM\u00a0N13\nNOTE-02",
                "Cable Tray Layout drawings",
                "Internal cable routing not submitted",
                "TM\u00a0N13\n(06-Apr-2026)",
                "OPEN \u2014 tracked in ADASA email 10-Apr-2026",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run(
        "Note: TM\u00a0N12 NOTE-02 (Line List SCH\u00a080S), TM\u00a0N13 "
        "NOTE-01 (P&ID CIP Tank capacity), and TM\u00a0N8 OBS-04 (vibration "
        "setpoints) are tracked for IFC Rev\u00a00."
    )
    aplicar_arial_12(para)

    # ===================================================================
    # 4. ATTACHMENTS
    # ===================================================================
    doc.add_heading("ATTACHMENTS", level=1)

    add_simple_table(
        doc,
        [
            ("Document", "Annotated File", "Annotations"),
            (
                "Valve List Rev\u00a0D",
                "P22-LI-09-005-002_D_Valve_List_CC_ADASA.pdf",
                "NOTE-01",
            ),
            (
                "I/O List Rev\u00a0C",
                "P22-LI-09-008-001_C_IO_List_CC_ADASA.pdf",
                "NOTE-02",
            ),
            (
                "Instrument List Rev\u00a0C",
                "P22-LI-09-008-003_C_Instrument_List_CC_ADASA.pdf",
                "NOTE-03, NOTE-04",
            ),
            (
                "Data Transfer List Rev\u00a0B",
                "P22-LI-09-008-004_B_Data_Transfer_List_CC_ADASA.pdf",
                "NOTE-05",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run(
        "Control System Architecture Rev\u00a0D, Datasheet of Pressure "
        "Gauge Rev\u00a0B, Datasheet of Conductivity Analyzer Rev\u00a0B, "
        "Datasheet of pH/ORP Analyzer Rev\u00a0B, Datasheet of Temperature "
        "Transmitter Rev\u00a0B, Datasheet of Vibration Transmitter "
        "Rev\u00a0B, and Datasheet of Flow Transmitter Rev\u00a0B are "
        "approved without annotations."
    )
    aplicar_arial_12(para)

    # ===================================================================
    # 5. RESPONSE SUMMARY
    # ===================================================================
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            (
                "P22-CD-09-004-001",
                "Control System Architecture",
                "D",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-005-002",
                "Valve List",
                "D",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-LI-09-008-011",
                "Datasheet of Pressure Gauge",
                "B",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-008-001",
                "I/O List",
                "C",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-LI-09-008-003",
                "Instrument List",
                "C",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-LI-09-008-004",
                "Data Transfer List (Modbus TCP/IP)",
                "B",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-LI-09-008-005",
                "Datasheet of Conductivity Analyzer",
                "B",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-008-010",
                "Datasheet of pH/ORP Analyzer",
                "B",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-008-013",
                "Datasheet of Temperature Transmitter",
                "B",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-008-014",
                "Datasheet of Vibration Transmitter",
                "B",
                "1 \u2014 Approved",
            ),
            (
                "P22-LI-09-008-007",
                "Datasheet of Flow Transmitter",
                "B",
                "1 \u2014 Approved",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run(
        "Overall Transmittal Verdict: 2 \u2014 APPROVED AS NOTED"
    ).bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Twelve observations closed (TM\u00a0N10 OBS-01/02/03/04, "
        "TM\u00a0N11 OBS-01/02/NOTE-01, TM\u00a0N12 OBS-01/NOTE-01, "
        "TM\u00a0N8 OBS-01/02/03). Five notes raised on E26\u2013E28 "
        "documents \u2014 two major (PSV removal justification, analyzer "
        "voltage discrepancy), three minor (vibration scaling, working "
        "medium labels, Modbus range alignment). Flow Transmitter Rev\u00a0B "
        "(E29) approved without observations \u2014 both Transmittal\u00a0N8 "
        "inline notes resolved. Five observations remain open per "
        "Section\u00a03."
    )
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
