#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N21 ADASA-BW_WATER.
Submittal 25007-0048 (E48). Fecha emision: 11-Jun-2026.

Veredicto global: 3 - TO BE REVISED. Tally: 1 Code 2 + 1 Code 3.
Driver Code 3: Section 2.2 Datasheet of PLC and HMI Panel Component Rev B
(sin via de adquisicion HART para la instrumentacion 4-20mA+HART que exige
la ET; + reconciliar modulo RTD 5069-IY4; + typo portada).
Grounding Layout Rev F = Code 2 (schedule embebido cerrado; resta revision
history + ECN).

Adjuntos: 2 PDFs CC_ADASA (1 Code 3 + 1 Code 2).

Fuente unica de contenido: P22-TM-09-000-021-0_TRANSMITTAL.md.
Numeracion: SIN numeros manuales en add_heading() — el template ADASA
auto-numera H1 y H2.
"""

import os
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document  # noqa: E402


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N21 ADASA-BW_WATER.docx")


def add_para(doc, runs):
    """runs: lista de (texto,) o (texto, {bold, italic})."""
    para = doc.add_paragraph()
    for item in runs:
        text = item[0]
        attrs = item[1] if len(item) > 1 else {}
        run = para.add_run(text)
        if attrs.get("bold"):
            run.bold = True
        if attrs.get("italic"):
            run.italic = True
    aplicar_arial_12(para)
    return para


def add_bullet(doc, text):
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


# ---------------------------------------------------------------------------
# Section 2 content (data-driven).
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading=("Grounding Point & Power Panel Location Layout Rev F — "
                 "P22-DWG-09-007-003"),
        code="Response Code: 1 — Approved",
        paras=[
            "Resubmittal of Rev E (Code 3 in Transmittal N19), returned "
            "ahead of the 17-Jun commitment set in the clarification "
            "exchange of 03-Jun. The revision closes the substance of the "
            "review. The grounding schedule is now embedded on the drawing "
            "as a 48-conductor table with PE conductor identifiers, "
            "cross-section per load, ring-main topology and equipotential "
            "bonding declared on every row, per NCh Elect. 4/2003 Section "
            "10.0 — closing the schedule item carried open since "
            "Transmittal N11. The Cu-bare versus insulated distinction "
            "requested is addressed (tray-to-tray bonding shown as tinned "
            "flexible braided copper, with the Material Take-Off listing "
            "copper earth link, Cu/PVC and tinned braided copper as "
            "separate items). Note 5 (\"panel locations are indicative only "
            "and subject to relocation based on site condition\") has been "
            "removed and the main panel is fixed in the approved Equipment "
            "Layout position. The conductor-sizing basis is unified to IEC "
            "60364-5-54 across the drawing, with the NEC Table 250.122 "
            "reference removed. The Consolidated Comment Sheet is legible. "
            "The drawing is approved as-is.",
        ],
        action=[
            ("Action: none requiring a new revision — approved; issue "
             "directly at IFC Rev 0.", {"bold": True}),
            (" When the drawing is issued at Rev 0, complete the "
             "revision-history block with a one-line change description and "
             "the ECN reference per revision from Rev B to Rev F — the "
             "documentation item carried from Transmittal N19; the "
             "substantive content, including the embedded grounding "
             "schedule, is accepted.",),
        ],
    ),
    dict(
        heading=("Datasheet of PLC and HMI Panel Component Rev B — "
                 "P22-ET-09-008-001"),
        code="Response Code: 3 — To be revised",
        paras=[
            "Resubmittal of Rev A (Code 2 in Transmittal N1). Rev B fixes "
            "the panel hardware by marking the committed values: the "
            "controller is an Allen-Bradley CompactLogix 5380 5069-L320ER "
            "(2 MB, dual EtherNet/IP), the discrete I/O are 5069-IB16 and "
            "5069-OB16, the analog I/O are 5069-IF8 and 5069-OF4/OF8, and "
            "the operator interface is a PanelView Plus 7 Performance "
            "2711P-T10C22D9P 10-inch touch panel. The Transmittal N1 query "
            "on Modbus is satisfactorily answered: the Consolidated Comment "
            "Sheet refers to the Control System Architecture Rev B, which "
            "carries the ProSoft PLX32-EIP-MBTCP gateway providing the "
            "Modbus TCP/IP interface to the plant — no further action on "
            "that point. Two matters require revision. Detailed annotations "
            "on P22-ET-09-008-001_B_PLC_HMI_Datasheet_CC_ADASA.pdf.",
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "No HART acquisition path in the panel. The committed analog "
             "input module 5069-IF8 reads 4-20 mA but does not acquire the "
             "HART digital signal (the datasheet note adds a 250 ohm "
             "resistor only to allow an external HART device on the loop), "
             "and the rack carries no HART-capable analog input and no HART "
             "multiplexer. The Technical Specification — Instrumentation "
             "Specification requires the instrumentation signal protocol to "
             "be 4-20 mA + HART; as configured, the HART capability of the "
             "field instruments cannot be used by the control system. "
             "Provide a HART acquisition path (HART-capable analog input or "
             "HART multiplexer) or submit the engineering justification for "
             "its omission"),
            ("OBS-02", "MINOR",
             "Module population does not match the project rack: the "
             "datasheet lists the controller, 5069-IB16, 5069-OB16, "
             "5069-IF8 and 5069-OF4/OF8 but omits the two 5069-IY4 "
             "universal analog modules that provide the eight motor Pt-100 "
             "RTD channels declared in the Local Control Panel Datasheet "
             "Rev B and the PLC/LCP Schematic Diagram. Incorporate the "
             "5069-IY4 modules, or reference the Local Control Panel "
             "Datasheet for the project-specific configuration, so the "
             "component datasheet is consistent with the rack"),
            ("NOTE-01", "MINOR",
             "Cover title block: project name typo \"PD Tattal\" — correct "
             "to \"PD Taltal\" (the same typo was noted on the Outline Panel "
             "Drawing in Transmittal N20)"),
        ],
        action=[
            ("Action — re-issue as Rev C:", {"bold": True}),
            (" provide the HART acquisition path for the 4-20 mA + HART "
             "instrumentation, or the engineering justification for its "
             "omission; incorporate the two 5069-IY4 RTD modules so the "
             "module list reflects the project rack consistently with the "
             "Local Control Panel Datasheet Rev B; and correct the cover "
             "title block. The controller, HMI and discrete/analog I/O "
             "selections are otherwise accepted. The per-module power "
             "dissipation given in this datasheet supports the total panel "
             "power consumption tracked on the Local Control Panel "
             "Datasheet.",),
        ],
    ),
]


GLANCE = [
    ("Grounding Point & Power Panel Location Layout Rev F — Code 1.",
     "The grounding schedule (open since Transmittal N11, about 88 days, the "
     "longest-standing item of the electrical package) is embedded and "
     "complete; approved as-is — issue directly at IFC Rev 0, completing the "
     "revision-history descriptions as part of that issuance."),
    ("Datasheet of PLC and HMI Panel Component Rev B — Code 3.",
     "The Allen-Bradley CompactLogix 5380 and PanelView Plus 7 selection is "
     "sound, but the panel carries no HART acquisition for the 4-20 mA + "
     "HART instrumentation the specification mandates, and the module list "
     "omits the RTD modules that serve the motor Pt-100 protection."),
]


ATTACHMENTS = [
    ("Datasheet of PLC and HMI Panel Component Rev B", "Code 3",
     "P22-ET-09-008-001_B_PLC_HMI_Datasheet_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
]


RESPONSE_SUMMARY = [
    ("P22-DWG-09-007-003", "Grounding Point & Power Panel Location Layout",
     "F", "1 — Approved"),
    ("P22-ET-09-008-001", "Datasheet of PLC and HMI Panel Component", "B",
     "3 — To Be Revised"),
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N21 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-021-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # =========================================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(doc, [(
        "This transmittal reviews the two documents of submittal "
        "25007-0048: the Grounding Point & Power Panel Location Layout "
        "Rev F, returned ahead of its 17-Jun commitment with the grounding "
        "schedule now embedded, and the Datasheet of PLC and HMI Panel "
        "Component Rev B, which fixes the panel hardware selection.",)])

    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — TO BE REVISED.", {"bold": True}),
        (" Submittal 25007-0048. Tally: 1 Code 1, 1 Code 3. The verdict is "
         "driven by the PLC and HMI Panel Component Datasheet: the panel "
         "provides no path to acquire the HART signal that the Technical "
         "Specification requires of the field instrumentation.",),
    ])

    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for lead, rest in GLANCE:
        add_para(doc, [(lead + " ", {"bold": True}), (rest,)])

    add_para(doc, [
        ("Why Code 3 — Datasheet of PLC and HMI Panel Component Rev B. ",
         {"bold": True}),
        ("The committed analog input module (5069-IF8) reads 4-20 mA only; "
         "it does not acquire the HART digital signal, and the panel rack "
         "carries no HART-capable analog input and no HART multiplexer. The "
         "Technical Specification — Instrumentation Specification requires "
         "the instrumentation signal protocol to be 4-20 mA + HART, so the "
         "HART capability of the field instruments cannot be used by the "
         "control system. A HART acquisition path, or the engineering "
         "justification for its omission, must be provided. In addition, "
         "the datasheet omits the two 5069-IY4 universal analog modules "
         "that provide the eight motor Pt-100 RTD channels declared in the "
         "Local Control Panel Datasheet Rev B and the PLC/LCP Schematic "
         "Diagram — the module population shown does not match the project "
         "rack.",),
    ])

    add_para(doc, [(
        "Open observations from previous transmittals are inventoried in "
        "Section 3.",)])

    # =========================================================================
    # 2. OBSERVATIONS BY DOCUMENT
    # =========================================================================
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        for p in sec["paras"]:
            if isinstance(p, str):
                add_para(doc, [(p,)])
            else:
                add_para(doc, p)
        if sec.get("obs"):
            add_simple_table(
                doc, [("ID", "Severity", "Topic")] + list(sec["obs"]))
        add_para(doc, sec["action"])

    # =========================================================================
    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    # =========================================================================
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    add_para(doc, [("Items open as of 11-Jun-2026.",)])

    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status"),
        ("TM N18 Section 2.1",
         "Plant Control Philosophy Rev C (P22-BT-09-009-001)",
         "HP Pump start permissive; Sequence Charts / Setpoint List / "
         "Control Matrix; salt-rejection formula. Fifth consecutive cycle; "
         "the fourteen-day window of TM N19 expired 08-Jun-2026",
         "OPEN — Rev D not delivered. As recorded in Transmittal N20, the "
         "I/O List acceptance has reverted to Code 3 and the instrumentation "
         "cabling and alarm documents remain gated. ADASA's reservation of "
         "remedies under Contract C-4300 stands"),
        ("TM N20 Section 2.6",
         "PLC-LCP Outline Panel Drawing Rev A (P22-CD-09-008-001)",
         "Enclosure contradiction (sheet steel / IP55 versus SS316L / "
         "NEMA 4X-IP66) — fabrication gate",
         "OPEN — Outline Rev B with the aligned Panel Specification Sheet, "
         "actual panel weight and reconciled cooling awaited; the expedited "
         "release path stated in the response of 10-Jun applies"),
        ("TM N4 NOTE-05",
         "HMI Screenshots (P22-BREAD-09-008-001)",
         "Committed at Transmittal N4 — never submitted; about 127 days, "
         "oldest open commitment",
         "OPEN — the HMI hardware is now fixed in the datasheet of Section "
         "2.2 (PanelView Plus 7), but the HMI screen design remains "
         "outstanding"),
        ("TM N19 Section 2.10",
         "ITP Offsite (P22-BA-09-000-004) and vessel test procedures",
         "ASME certification scope; Hydrostatic, Preservation and FAT "
         "procedures; RO pressure-vessel test scope",
         "OPEN — ITP Rev C with the certification basis of the 02-Jun "
         "waiver, the vessel test scope and the named procedures remain "
         "outstanding (Transmittal N20 Section 2.17)"),
        ("TM N19 Sections 2.12/2.13",
         "Cartridge Filters (P22-ET-09-009-005/006)",
         "Rev E / Rev D pending the Technical Note P22-NT-09-000-001-0 "
         "cycle",
         "OPEN — FAT/SAT table and remaining clarifications due "
         "15-Jun-2026"),
    ])

    add_para(doc, [("Addressed in this transmittal:", {"bold": True})])
    for txt in [
        "TM N11 OBS-03 / TM N15 NOTE-03 / TM N19 OBS-01 — Grounding "
        "schedule completeness (about 88 days open across three cycles): "
        "the complete 48-conductor schedule is now embedded on the "
        "Grounding Layout Rev F (Section 2.1). The grounding SEC compliance "
        "hold point is no longer gated on the schedule; only the "
        "revision-history administrative item remains.",
        "TM N1 — Datasheet of PLC and HMI Panel Component Modbus query: "
        "answered by reference to the Control System Architecture Rev B "
        "Modbus TCP/IP gateway (Section 2.2).",
    ]:
        add_bullet(doc, txt)

    # =========================================================================
    # 4. ATTACHMENTS
    # =========================================================================
    doc.add_heading("ATTACHMENTS", level=1)

    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)

    add_para(doc, [(
        "The Code 3 document carries an annotated PDF. The Grounding Point & "
        "Power Panel Location Layout Rev F is Code 1 — Approved and carries "
        "no annotated PDF.",)])

    # =========================================================================
    # 5. RESPONSE SUMMARY
    # =========================================================================
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)

    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.",
         {"bold": True}),
        (" The Grounding Layout Rev F is approved: it closes the "
         "longest-standing electrical item, the grounding schedule, and "
         "issues directly at IFC Rev 0 (completing the revision-history "
         "descriptions as part of that issuance). The PLC and HMI Panel "
         "Component Datasheet drives "
         "the verdict: the committed hardware is sound and the Modbus "
         "question is answered, but the panel provides no means to acquire "
         "the HART signal that the Technical Specification requires of the "
         "instrumentation, and the module list omits the RTD modules of the "
         "project rack. Both points are document actions resolved at "
         "Rev C.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
