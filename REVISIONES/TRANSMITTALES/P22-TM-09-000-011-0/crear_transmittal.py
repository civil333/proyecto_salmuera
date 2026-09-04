#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N11 ADASA-BW_WATER
Entregas E19 (25007-0019) / E20 (25007-0020) / E21 (25007-0021): 10 documentos tecnicos
Fecha: 17-Mar-2026

Veredicto: 3 - TO BE REVISED

Documentos:
  - P22-LI-09-005-002 Rev C   Valve List                              -> 3 - To be Revised
  - P22-LI-09-005-001 Rev B   Equipment List                          -> 2 - Approved as Noted
  - P22-DWG-09-005-010 Rev A  GA of CIP Flushing Skid Pump            -> 2 - Approved as Noted
  - P22-DWG-09-005-011 Rev A  GA of Antiscalant Dosing Skid Pump      -> 2 - Approved as Noted
  - P22-ET-09-006-2 Rev B     Painting Specifications                  -> 1 - Approved
  - P22-ET-09-009-002 Rev D   Datasheet of RO HP Feed Pump            -> 2 - Approved as Noted
  - P22-ET-09-009-007 Rev D   Datasheet of Feed Turbocharger (SIP-09-001)      -> 2 - Approved as Noted
  - P22-ET-09-009-008 Rev D   Datasheet of Interstage Turbocharger (SIP-09-002) -> 2 - Approved as Noted
  - P22-DWG-09-007-003 Rev B  Grounding Point & Power Panel Location Layout    -> 3 - To be Revised (OBS-03)
  - P22-DWG-09-008-001 Rev B  Instrument Location Layout              -> 3 - To be Revised (OBS-04)

Observaciones cerradas en esta entrega:
  - TM N6 OBS-01: Coupling pressure (turbos + HP pump) -- Style S/X 1800 psi + Style H 2000 psi
  - TM N10 OBS-06: SIP-09-001 vibration mounting -- Datasheet Rev D row 38
  - TM N10 OBS-07: SIP-09-002 vibration mounting -- Datasheet Rev D row 38

Observaciones nuevas:
  - OBS-03 (MAJOR): Grounding Layout Rev B -- posiciones derivan de Piping Layout rechazado TM N7
  - OBS-04 (MAJOR): Instrument Location Layout Rev B -- posiciones derivan de Piping Layout rechazado TM N7
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
    output_file = "TRANSMITTAL N11 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N11 \u2014 SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-011-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    doc = Document(output_file)

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
        "Deliveries 19, 20, and 21 (25007-0019 / 25007-0020 / 25007-0021, received March 13\u201316, "
        "2026) submit 10 documents. Ten observations are raised \u2014 four MAJOR, six informational."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run("Key findings:").bold = True
    aplicar_arial_12(para)

    bullets = [
        (
            "Valve List Rev C (Code 3 \u2014 To be Revised):",
            " Corrects four prior duplicate TAGs but introduces two new ones (VE-09-007, PSV-09-002). "
            "Rev D required. Area-code error VM-07-005 persists.",
        ),
        (
            "Equipment Datasheets Rev D (Code 2 \u2014 Approved as Noted):",
            " TM N6 OBS-01 (coupling pressure) and TM N10 OBS-06/07 (vibration mounting) closed "
            "for HP Pump and both Turbochargers.",
        ),
        (
            "CCS review (17 items):",
            " 13 closed, 3 partial, 1 open. Valve List CCS item 2 remains OPEN.",
        ),
        (
            "Layout Drawings Rev B \u2014 Grounding Layout and Instrument Location Layout (Code 3 \u2014 To be Revised):",
            " Rev B reflects an equipment arrangement derived from the Piping Layout Rev A "
            "(P22-DWG-09-005-004), which was rejected in Transmittal N7 for exceeding the CIP "
            "external footprint limit. Progress on CCS items is acknowledged; revision required "
            "after Equipment Layout and Piping Layout are accepted.",
        ),
    ]
    for bold_part, normal_part in bullets:
        para = doc.add_paragraph()
        para.add_run("\u2022  ")
        run = para.add_run(bold_part)
        run.bold = True
        para.add_run(normal_part)
        aplicar_arial_12(para)

    # ===== 2. DETAILED OBSERVATIONS BY DOCUMENT =====
    doc.add_heading("DETAILED OBSERVATIONS BY DOCUMENT", level=1)

    # --- 2.1 Valve List Rev C ---
    doc.add_heading("Valve List Rev C \u2014 P22-LI-09-005-002", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev C corrects the four duplicate TAGs identified in Transmittal N6 OBS-01: VM-09-015 "
        "renumbered to VM-09-151, and VE-09-008, VE-09-009, and VM-09-065 each resolved to "
        "unique assignments. The consolidated comment sheet item 3 \u2014 confirming VM-09-015 "
        "item 18 is now MANUALLY ACTUATED VALVE per Transmittal N6 OBS-11 WITHDRAWN \u2014 is "
        "verified correct in the submitted document. These corrections are acknowledged."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev C does not achieve full TAG uniqueness. Two new duplicate TAGs are introduced "
        "that were not present in Rev B, as documented in OBS-01 and OBS-02 below."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-01 \u2014 New duplicate TAG: VE-09-007 appears in items 44 and 64 (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Item 44 and item 64 both carry the TAG VE-09-007. These are distinct physical valves "
        "with different sizes, materials, and service descriptions. Duplicate TAGs prevent "
        "unambiguous valve identification in the PLC and in field documentation."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The Consolidated Comment Sheet response \u201call valves have unique TAGs on Rev.\u00a0C\u201d "
        "is factually incorrect with respect to this item. BW Water must assign a unique TAG to "
        "one of these two valves in Valve List Rev D and update all project documents referencing "
        "the affected TAG (P&ID, Instrument List, I/O List)."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Technical Basis: ET \u2014 Valves and Piping (TAG uniqueness is a fundamental QA "
        "requirement for PLC addressability)."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-02 \u2014 New duplicate TAG: PSV-09-002 appears in items 105 and 112 (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Item 105 and item 112 both carry the TAG PSV-09-002. These are distinct safety relief "
        "valves at different process locations. Duplicate TAG assignment creates a safety "
        "documentation conflict that cannot be accepted in a submitted document."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must assign a unique TAG to item 112 in Valve List Rev D and update all "
        "referencing documents accordingly."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Technical Basis: ET \u2014 Valves and Piping; ET \u2014 Safety and Relief Valves."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-01 \u2014 Area-code error VM-07-005 persists (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Item 7 carries the TAG VM-07-005 (area 07). Area 07 does not correspond to any "
        "discipline boundary in this project. The correct area code for BW Water module equipment "
        "is 09, giving VM-09-005. This error was first identified in Transmittal N3 OBS-13 and "
        "was not corrected in Rev B or Rev C. BW Water should also verify and correct VM-07-031 "
        "and VE-07-009 if those TAGs persist with area 07 in the list."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Correct item 7 to VM-09-005 (and VM-09-031, VE-09-009 as applicable) in Valve List "
        "Rev D. Technical Basis: ET \u2014 Instrument and Equipment Identification; project "
        "TAG convention area 09 = BW Water module scope."
    )
    aplicar_arial_12(para)

    # --- 2.2 Equipment List Rev B ---
    doc.add_heading("Equipment List Rev B \u2014 P22-LI-09-005-001", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B addresses the single CCS item from Transmittal N6: TAG Static Mixer confirmed "
        "as MZE-09-001; CIP Tank volume confirmed at 6.1\u00a0m\u00b3; Antiscalant Tank volume "
        "confirmed at 0.27\u00a0m\u00b3 effective; Antiscalant Dosing Pump capacity confirmed at "
        "2.3\u00a0LPH; and HP Feed Pump shaft power confirmed at 125\u00a0hp = 93\u00a0kW. "
        "All five confirmations are verified in the submitted document. No new observations are "
        "raised. The proactive inclusion of the HP Pump power conversion by BW Water is noted "
        "as a value-added clarification."
    )
    aplicar_arial_12(para)

    # --- 2.3 GA CIP Pump Rev A ---
    doc.add_heading(
        "GA of CIP Flushing Skid Pump Rev A \u2014 P22-DWG-09-005-010", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "First submission. The general arrangement drawing is accepted for its initial revision."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-05 \u2014 Seismic anchor data not included in first submission (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The GA drawing does not include anchor bolt layout, anchor loads, or seismic reaction "
        "forces. The plant site is located in Seismic Zone 3 per NCh\u00a02369. For all "
        "skid-mounted equipment, seismic anchor data is required to confirm that the structural "
        "interface between the skid base and the building foundation is adequately designed."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "GA Rev B must include: (1) anchor bolt layout plan with bolt diameter, spacing, and "
        "embedment depth; (2) seismic base reaction forces (Fx, Fy, Fz) per NCh\u00a02369 "
        "Zone\u00a03 analysis; (3) equipment mass for load verification. "
        "Technical Basis: ET \u2014 Structural and Civil Requirements; NCh\u00a02369 \u2014 "
        "Seismic Design for Industrial Structures."
    )
    aplicar_arial_12(para)

    # --- 2.4 GA Antiscalant Pump Rev A ---
    doc.add_heading(
        "GA of Antiscalant Dosing Skid Pump Rev A \u2014 P22-DWG-09-005-011", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "First submission. The general arrangement drawing is accepted for its initial revision."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-06 \u2014 Seismic anchor data not included in first submission (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Same condition as NOTE-05 for the CIP Pump GA. Anchor bolt layout, seismic reaction "
        "forces (Fx, Fy, Fz), and equipment mass must be provided in GA Rev B per NCh\u00a02369 "
        "Zone\u00a03 requirements. Technical Basis: ET \u2014 Structural and Civil Requirements; "
        "NCh\u00a02369 \u2014 Seismic Design for Industrial Structures."
    )
    aplicar_arial_12(para)

    # --- 2.5 Painting Specifications Rev B ---
    doc.add_heading("Painting Specifications Rev B \u2014 P22-ET-09-006-2", level=2)

    para = doc.add_paragraph()
    para.add_run("Response Code: 1 \u2014 Approved").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B addresses both CCS items from Transmittal N6: the RAL\u00a05017 / RAL\u00a05012 "
        "distinction for container vs. structural steel is correctly maintained in the updated "
        "paint schedule; the DFT correction from 350\u00a0\u00b5m to 355\u00a0\u00b5m for the "
        "container system is verified. Structural steel item 4 also correctly shows "
        "355\u00a0\u00b5m total DFT (80 + 200 + 75\u00a0\u00b5m per coat). No new observations "
        "are raised. Document is approved."
    )
    aplicar_arial_12(para)

    # --- 2.6 HP Feed Pump Datasheet Rev D ---
    doc.add_heading(
        "Datasheet of RO HP Feed Pump Rev D \u2014 P22-ET-09-009-002", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev D attaches the Victaulic Coupling Style\u00a0H datasheet confirming a working "
        "pressure rating of 2000\u00a0psi for the DN25\u2013DN100 range. The operating discharge "
        "pressure of the HP Feed Pump (~710\u00a0psi) provides a margin of approximately 280\u00a0% "
        "over the coupling rating, which is accepted. Transmittal N6 OBS-01 (coupling pressure) "
        "is closed for this equipment."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Component Datasheet row 55 confirms 3-wire 100\u00a0Ohm Platinum RTDs for both bearings "
        "and windings, satisfying ET \u2014 Motors and Electrical Equipment. Vibration sensor "
        "mounting surface is confirmed, satisfying ET \u2014 Vibration Monitoring."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-02 \u2014 Motor manufacturer field inconsistency (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The HP Feed Pump Component Datasheet identifies the motor manufacturer as \u201cGE\u201d "
        "in the equipment data block, while the FEDCO pump data section lists "
        "\u201cABB or equivalent.\u201d These two fields describe the same motor. The discrepancy "
        "introduces uncertainty when procuring spare parts or conducting field maintenance."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must reconcile the motor manufacturer field across both data blocks in "
        "Datasheet Rev E and confirm the actual manufacturer once procurement is complete. "
        "Technical Basis: ET \u2014 Motors and Electrical Equipment (Spare Parts and "
        "Maintainability)."
    )
    aplicar_arial_12(para)

    # --- 2.7 Feed Turbocharger DS Rev D ---
    doc.add_heading(
        "Datasheet of Feed Turbocharger (SIP-09-001) Rev D \u2014 P22-ET-09-009-007",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev D attaches the Piedmont Coupling Style\u00a0S/X datasheet confirming a working "
        "pressure rating of 1800\u00a0psi for DN40 (1.5\u201d) and DN50 (2\u201d). The maximum "
        "operating inlet pressure for SIP-09-001 is approximately 1,008\u00a0psi, giving a "
        "safety margin of approximately 78\u00a0% above the rated coupling pressure. "
        "Transmittal N6 OBS-01 (coupling pressure) is closed for this equipment."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Datasheet row 38 confirms \u201cvibration sensor mounting surface\u201d for SIP-09-001, "
        "satisfying Transmittal N10 OBS-06. Transmittal N10 OBS-06 is closed."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-03 \u2014 Coupling style label inconsistency in outline drawing (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The HPB-60 outline drawing (page 6 of the datasheet package) references "
        "\u201cCUT GROOVE STYLE 77\u201d at the inlet and outlet connections. The attached "
        "coupling datasheet documents Style\u00a0S/X at 1800\u00a0psi, which is the accepted "
        "rating. Style\u00a077 is a different Victaulic product with a different pressure rating."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "The outline drawing label must be updated to \u201cStyle\u00a0S\u201d (or the appropriate "
        "Style\u00a0S/X designation) in the next datasheet revision to prevent field installation "
        "errors. Technical Basis: ET \u2014 Equipment Documentation Requirements; Victaulic "
        "product line differentiation Style\u00a077 vs. Style\u00a0S."
    )
    aplicar_arial_12(para)

    # --- 2.8 Interstage Turbocharger DS Rev D ---
    doc.add_heading(
        "Datasheet of Interstage Turbocharger (SIP-09-002) Rev D \u2014 P22-ET-09-009-008",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 2 \u2014 Approved as Noted").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev D attaches the same Piedmont Coupling Style\u00a0S/X datasheet confirming "
        "1800\u00a0psi for DN40 and DN50. The maximum operating inlet pressure for SIP-09-002 "
        "is approximately 1,208\u00a0psi, giving a safety margin of approximately 49\u00a0% "
        "above the rated coupling pressure. Transmittal N6 OBS-01 (coupling pressure) is closed "
        "for this equipment."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Datasheet row 38 confirms \u201cvibration sensor mounting surface\u201d for SIP-09-002, "
        "satisfying Transmittal N10 OBS-07. Transmittal N10 OBS-07 is closed."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Note NOTE-04 \u2014 Coupling style label inconsistency in outline drawing (MINOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Identical condition to NOTE-03 for SIP-09-001: the HPB-60 outline drawing references "
        "\u201cCUT GROOVE STYLE 77\u201d at process connections while the accepted coupling is "
        "Style\u00a0S/X at 1800\u00a0psi. BW Water must update the outline drawing label to "
        "\u201cStyle\u00a0S\u201d in the next revision to prevent field installation errors. "
        "Technical Basis: ET \u2014 Equipment Documentation Requirements."
    )
    aplicar_arial_12(para)

    # --- 2.9 Grounding Layout Rev B ---
    doc.add_heading(
        "Grounding Point & Power Panel Location Layout Rev B \u2014 P22-DWG-09-007-003",
        level=2,
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To Be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B addresses the TM N3 comments \u2014 confirmed by the Consolidated Comment Sheet. "
        "However, Rev B reflects an equipment arrangement that has changed from Rev A and is "
        "derived from the Piping Layout Rev A (P22-DWG-09-005-004), which was rejected in "
        "Transmittal N7 for exceeding the CIP external footprint limit established in "
        "Transmittal N5 (11,150\u00a0mm submitted vs. \u22643,500\u00a0mm required). Panel and "
        "grounding point positions cannot be accepted while the underlying equipment layout "
        "remains non-conforming."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-03 \u2014 Grounding and panel positions reflect a non-conforming "
        "equipment arrangement (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "Rev B panel and grounding point positions are derived from an equipment arrangement "
        "that has not been accepted by ADASA. The Piping Layout Rev A from which this "
        "arrangement originates was rejected in Transmittal N7 for exceeding the 3,500\u00a0mm "
        "CIP external footprint limit (submitted at 11,150\u00a0mm \u2014 more than three times "
        "the required limit). The same logic applied in Transmittal N7 Section 3.3 (Tie-In "
        "Point Layout rejected for dependency on the non-conforming Piping Layout) applies here."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must resubmit Grounding Point & Power Panel Location Layout as Rev C after "
        "Equipment Layout (P22-DWG-09-005-003) and Piping Layout (P22-DWG-09-005-004) are "
        "revised and accepted by ADASA. Update all referencing documents accordingly."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Technical Basis: Transmittal N5 (P22-TM-09-000-005-1) \u2014 CIP external footprint "
        "limit \u22643,500\u00a0mm; Transmittal N7 \u2014 Piping Layout Rev A rejected for "
        "non-conformance."
    )
    aplicar_arial_12(para)

    # --- 2.10 Instrument Layout Rev B ---
    doc.add_heading(
        "Instrument Location Layout Rev B \u2014 P22-DWG-09-008-001", level=2
    )

    para = doc.add_paragraph()
    para.add_run("Response Code: 3 \u2014 To Be Revised").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Rev B addresses all eight CCS items from Transmittal N3 \u2014 TAG FIT-09-001 "
        "corrected to FIT-09-002, vibration transmitter locations added "
        "(VT-09-001/002/003), motor RTD elements confirmed, CIT-09-004 corrected, "
        "LIT TAG unified. This progress is acknowledged."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "However, Rev B reflects an equipment arrangement derived from the Piping Layout "
        "Rev A (P22-DWG-09-005-004), rejected in Transmittal N7. The external CIP and "
        "antiscalant instrument positions shown in Rev B correspond to the non-conforming "
        "11,150\u00a0mm footprint \u2014 more than three times the 3,500\u00a0mm limit "
        "established in Transmittal N5. These positions cannot be accepted."
    )
    aplicar_arial_12(para)

    doc.add_heading(
        "Observation OBS-04 \u2014 Instrument positions in the CIP/antiscalant external area "
        "reflect a non-conforming equipment arrangement (MAJOR)",
        level=3,
    )

    para = doc.add_paragraph()
    para.add_run(
        "The instrument positions for CIP and antiscalant external equipment shown in Rev B "
        "are derived from the non-conforming Piping Layout arrangement (11,150\u00a0mm "
        "footprint, rejected in Transmittal N7). Acceptance of these positions would imply "
        "acceptance of an equipment arrangement that ADASA has not approved."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "BW Water must resubmit Instrument Location Layout as Rev C after Equipment Layout "
        "(P22-DWG-09-005-003) and Piping Layout (P22-DWG-09-005-004) are revised and "
        "accepted. Internal container instrument positions (22 items) may be preserved in "
        "Rev C if unchanged."
    )
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Technical Basis: Transmittal N5 (P22-TM-09-000-005-1) \u2014 CIP external footprint "
        "limit \u22643,500\u00a0mm; Transmittal N7 \u2014 Piping Layout Rev A rejected for "
        "non-conformance."
    )
    aplicar_arial_12(para)

    # ===== 4. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS =====
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    para = doc.add_paragraph()
    para.add_run(
        "The following observations issued in Transmittal N10 remain open pending BW Water "
        "response. The required documents \u2014 I/O List Rev C, Data Transfer List Rev B, "
        "written UPS autonomy confirmation, Antiscalant Tank GA Rev B, and HMI Screenshots "
        "\u2014 have not been received. Two observations from Transmittal N10 (OBS-06 and "
        "OBS-07) are closed in this transmittal and are documented in Sections 2.7 and 2.8 "
        "respectively."
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("Obs", "Document", "Description", "Outstanding Since", "Status"),
            (
                "TM N10\nOBS-01",
                "I/O List / Data Transfer List",
                "Motor temperature TAG inconsistency (TE vs TIT); TIT-09-003 service conflict",
                "TM N10\n(16-Mar-2026)",
                "OPEN \u2014 I/O List Rev C and Data Transfer List Rev B not received",
            ),
            (
                "TM N10\nOBS-02",
                "Data Transfer List",
                "Conductivity scaling ranges incompatible with brine conditions "
                "(CIT-09-001/004/005 at 0\u201320 mS/cm)",
                "TM N10\n(16-Mar-2026)",
                "OPEN \u2014 Data Transfer List Rev B not received",
            ),
            (
                "TM N10\nOBS-03",
                "Data Transfer List",
                "Level alarm Modbus addresses missing for LS-09-001 and LS-09-002; "
                "VE-09-014 DI confirmation pending",
                "TM N10\n(16-Mar-2026)",
                "OPEN \u2014 Data Transfer List Rev B not received",
            ),
            (
                "TM N10\nOBS-04",
                "Control Architecture",
                "UPS autonomy confirmation: 8-hour backup required per "
                "ET \u2014 Uninterruptible Power Supply",
                "TM N10\n(16-Mar-2026)",
                "OPEN \u2014 Written confirmation with calculation not received",
            ),
            (
                "TM N10\nOBS-05",
                "GA Antiscalant Tank",
                "Seismic anchor data missing for Antiscalant Tank (GA Rev B pending)",
                "TM N10\n(16-Mar-2026)",
                "OPEN \u2014 GA Rev B not received",
            ),
            (
                "TM N10\nNOTE-05",
                "HMI Screenshots\nP22-BREAD-09-008-001",
                "HMI display screenshots committed since Transmittal N4 \u2014 not yet submitted",
                "TM N4",
                "OPEN \u2014 Document not received",
            ),
        ],
    )

    # ===== 5. ATTACHMENTS =====
    doc.add_heading("ATTACHMENTS", level=1)

    para = doc.add_paragraph(
        "The following BW Water documents were reviewed and annotated by ADASA:"
    )
    aplicar_arial_12(para)

    add_simple_table(
        doc,
        [
            ("#", "Document Code", "Title", "Rev", "Annotations"),
            ("1", "P22-LI-09-005-002", "Valve List", "C", "OBS-01, OBS-02, NOTE-01"),
            ("2", "P22-ET-09-009-002", "Datasheet of RO HP Feed Pump", "D", "NOTE-02"),
            (
                "3",
                "P22-ET-09-009-007",
                "Datasheet of Feed Turbocharger (SIP-09-001)",
                "D",
                "NOTE-03",
            ),
            (
                "4",
                "P22-ET-09-009-008",
                "Datasheet of Interstage Turbocharger (SIP-09-002)",
                "D",
                "NOTE-04",
            ),
            ("5", "P22-DWG-09-005-010", "GA of CIP Flushing Skid Pump", "A", "NOTE-05"),
            (
                "6",
                "P22-DWG-09-005-011",
                "GA of Antiscalant Dosing Skid Pump",
                "A",
                "NOTE-06",
            ),
            (
                "7",
                "P22-DWG-09-007-003",
                "Grounding Point & Power Panel Location Layout",
                "B",
                "OBS-03",
            ),
            (
                "8",
                "P22-DWG-09-008-001",
                "Instrument Location Layout",
                "B",
                "OBS-04",
            ),
        ],
    )

    # ===== 6. RESPONSE SUMMARY =====
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            ("P22-LI-09-005-002", "Valve List", "C", "3 \u2014 To be Revised"),
            ("P22-LI-09-005-001", "Equipment List", "B", "2 \u2014 Approved as Noted"),
            (
                "P22-DWG-09-005-010",
                "GA of CIP Flushing Skid Pump",
                "A",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-DWG-09-005-011",
                "GA of Antiscalant Dosing Skid Pump",
                "A",
                "2 \u2014 Approved as Noted",
            ),
            ("P22-ET-09-006-2", "Painting Specifications", "B", "1 \u2014 Approved"),
            (
                "P22-ET-09-009-002",
                "Datasheet of RO HP Feed Pump",
                "D",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-ET-09-009-007",
                "Datasheet of Feed Turbocharger (SIP-09-001)",
                "D",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-ET-09-009-008",
                "Datasheet of Interstage Turbocharger (SIP-09-002)",
                "D",
                "2 \u2014 Approved as Noted",
            ),
            (
                "P22-DWG-09-007-003",
                "Grounding Point & Power Panel Location Layout",
                "B",
                "3 \u2014 To be Revised",
            ),
            (
                "P22-DWG-09-008-001",
                "Instrument Location Layout",
                "B",
                "3 \u2014 To be Revised",
            ),
        ],
    )

    para = doc.add_paragraph()
    para.add_run("Overall Transmittal Verdict: 3 \u2014 TO BE REVISED").bold = True
    aplicar_arial_12(para)

    para = doc.add_paragraph()
    para.add_run(
        "Valve List Rev D is required to correct OBS-01 (VE-09-007 duplicate) and OBS-02 "
        "(PSV-09-002 duplicate) and to address NOTE-01 (VM-07-005 area code). Grounding "
        "Layout Rev C and Instrument Location Layout Rev C must be resubmitted after "
        "Equipment Layout and Piping Layout are accepted by ADASA (OBS-03, OBS-04). "
        "All other documents are accepted at their submitted revision pending the noted "
        "corrections in future revisions."
    )
    aplicar_arial_12(para)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
