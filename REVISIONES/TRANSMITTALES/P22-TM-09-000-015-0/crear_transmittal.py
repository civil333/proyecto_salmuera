#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar TRANSMITTAL N15 ADASA-BW_WATER (refinamiento v5 ejecutivo)
Entregas E30 (25007-0030) + E31 (25007-0031) + E32 (25007-0032) + E33 (25007-0033)
Fecha: 22-Apr-2026

Veredicto global: 3 - TO BE REVISED
Tally: 1 Code 1 + 6 Code 2 + 3 Code 3 (LCP A, Cable Tray B, Control Philosophy B)

Cambios v5 vs v3:
  - Section 2 ahora compacta: tabla ID/Sev/Topic por documento (sin parrafos extensos por NOTE)
  - NOTE-05 (Equipment Layout) REMOVIDA (vestigio post-withdrawal del footprint constraint)
  - Section 1 Executive Summary: bullets 1-liner (no parrafos largos)
  - Section 3 intro + nota final: comprimidos
  - Section 5 Final Summary: bullets (no parrafo denso)
  - Total anotaciones: 36 (vs 37 v3)
"""

import sys
import os

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, RGBColor


def add_hyperlink(paragraph, url, text):
    """Inserta un hipervinculo clickeable en un parrafo python-docx."""
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")

    rStyle = OxmlElement("w:rStyle")
    rStyle.set(qn("w:val"), "Hyperlink")
    rPr.append(rStyle)

    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Arial")
    rFonts.set(qn("w:hAnsi"), "Arial")
    rPr.append(rFonts)

    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "24")
    rPr.append(sz)

    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rPr.append(color)

    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)

    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink


def add_para(doc, runs):
    """runs es lista de (texto, kwargs) donde kwargs en {'bold': True, 'italic': True}."""
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
    para = doc.add_paragraph()
    para.add_run("– " + text)
    aplicar_arial_12(para)


# ======================================================================
# DATOS DE DOCUMENTOS (Section 2)
# Estructura: (sec, heading, response_code_txt, intro_paragraph, notes_rows, extra_para)
# notes_rows: lista de tuplas (id, sev, topic)
# ======================================================================

DOCS_DATA = [
    # 2.1 Level Switch B
    ("2.1",
     "Datasheet of Level Switch Rev B — P22-LI-09-008-008",
     "1 — Approved",
     "Capacitive level switch IFM KQ6005 for LS-09-001 and LS-09-002, "
     "consistent with Instrument List Rev C and IO List Rev C. "
     "Detailed comments: P22-LI-09-008-008_B_Level_Switch_CC_ADASA.pdf.",
     [
         ("NOTE-01", "MINOR",
          "Communication interface label inconsistency (4–20 mA HART "
          "vs IO-Link per IFM KQ6005 PNP discrete)"),
     ],
     None),

    # 2.2 AC Thermal Calc C
    ("2.2",
     "AC Thermal Calculation Rev C — P22-CD-09-005-002",
     "2 — Approved as Noted",
     "Closes Transmittal N2 OBS-02 (180+ days) by consolidating all "
     "container loads in the heat balance. Selected unit 2.5 HP / "
     "2.01 TR is marginal vs calculated 2.04 TR. Detailed "
     "comments: P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf.",
     [
         ("NOTE-02", "MAJOR",
          "Unit capacity margin (0.03 TR deficit vs calculated demand) "
          "and n+1 confirmation (each unit at 100% load independently)"),
     ],
     None),

    # 2.3 Grounding C
    ("2.3",
     "Grounding Point & Power Panel Location Layout Rev C — "
     "P22-DWG-09-007-003",
     "2 — Approved as Noted",
     "Rev C aligned to the Piping Layout Rev B in this "
     "submittal, closing Transmittal N11 OBS-03 basis. Detailed "
     "comments: P22-DWG-09-007-003_C_Grounding_Layout_CC_ADASA.pdf.",
     [
         ("NOTE-03", "MAJOR",
          "Grounding schedule completeness (PE identifiers, conductor "
          "cross-section, ring main topology, equipotential bonding) per "
          "NCh Elec 4/2003 §10.0"),
     ],
     None),

    # 2.4 LCP A
    ("2.4",
     "Datasheet of Local Control Panel (LCP) Rev A — "
     "P22-ET-09-007-005",
     "3 — To be revised",
     "First revision. Vendor catalog cuts (ABB, Phoenix Contact, "
     "Allen-Bradley, Mean Well, ProSoft) are reasonable, but the "
     "panel-level datasheet header is not populated, preventing "
     "validation against Control System Architecture Rev D. "
     "Detailed comments: P22-ET-09-007-005_A_LCP_Datasheet_CC_ADASA.pdf.",
     [
         ("OBS-01", "MAJOR",
          "I/O module configuration and motor RTD channel count not "
          "declared (8 Pt-100 channels required per Instrument "
          "List Rev C)"),
         ("OBS-02", "MAJOR",
          "Panel IP rating and ambient class not declared "
          "(IP54 minimum expected)"),
         ("OBS-03", "MINOR",
          "Power consumption inconsistency: Load List Rev A "
          "1.0 kW vs AC Thermal Calc Rev C 0.14 kW; LCP "
          "datasheet not declared"),
     ],
     None),

    # 2.5 Equipment Layout B (NOTE-05 REMOVIDA en v5)
    ("2.5",
     "Equipment Layout Rev B — P22-DWG-09-005-003",
     "2 — Approved as Noted",
     "Container 40 ft within ET envelope. 16-item equipment list "
     "consistent with P&ID Rev C. Section views confirm doors "
     "(pedestrian, equipment access, emergency, lateral sliding). "
     "Closes Transmittal N5 OBS-03/04/05. Detailed comments: "
     "P22-DWG-09-005-003_B_Equipment_Layout_CC_ADASA.pdf.",
     [
         ("NOTE-04", "MAJOR",
          "Operating Weight table to be embedded in Rev 0 (IFC); "
          "BW Water Civil Loading drawing committed for "
          "23-Apr-2026 and accepted as separate supporting deliverable"),
     ],
     "Items carried forward from Transmittal N5: OBS-01 "
     "(CIP numbering) and OBS-02 (imperial dimensions) remain "
     "partially open."),

    # 2.6 Piping Layout B (con WITHDRAWN inline)
    ("2.6",
     "Piping Layout Rev B — P22-DWG-09-005-004",
     "2 — Approved as Noted",
     "Five-sheet set coordinated with Equipment Layout Rev B. "
     "Detailed comments: P22-DWG-09-005-004_B_Piping_Layout_CC_ADASA.pdf.",
     [
         ("NOTE-06", "MAJOR",
          "Equipment access door (110° outward) and lateral sliding "
          "door not represented in piping views"),
         ("NOTE-07", "MAJOR",
          "Cabinet integration and FAT scope unclear (LCP shown as "
          "separate unit without cable routing and conduit penetrations)"),
         ("NOTE-08", "MAJOR",
          "Antiscalant and CIP module-boundary connections not "
          "confirmed as flanged"),
         ("NOTE-09", "MINOR",
          "Elevation view for tie-in points missing"),
     ],
     "_WITHDRAWN_PIPING"),  # sentinela para insertar parrafo especial

    # 2.7 Instrument Location C
    ("2.7",
     "Instrument Location Layout Rev C — P22-DWG-09-008-001",
     "2 — Approved as Noted",
     "Four-sheet drawing aligned with Piping Layout Rev B. "
     "Closes Transmittal N3 OBS-01/02/03 and Transmittal N11 "
     "OBS-04. Detailed comments: "
     "P22-DWG-09-008-001_C_Instrument_Location_CC_ADASA.pdf.",
     [
         ("NOTE-10", "MINOR",
          "Dependency on Equipment Layout Rev B and Piping Layout "
          "Rev B acceptance (no action if both are accepted as "
          "currently configured)"),
     ],
     None),

    # 2.8 Cable Tray B (Code 3)
    ("2.8",
     "Cable Tray Layout and Support Details Rev B — "
     "P22-DWG-09-007-004",
     "3 — To be revised",
     "Five-sheet drawing with tray routing and support zones S1–S6. "
     "Five ADASA review findings plus two from Transmittal N4 "
     "(78 days outstanding; consolidated comment sheet on Page 5 "
     "replies “has been revised” without itemizing closure). "
     "Detailed comments: P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf.",
     [
         ("OBS-04", "MAJOR",
          "Support S4 conflicts with antiscalant dosing tank TK-09-002 "
          "and adjacent components"),
         ("OBS-05", "MAJOR",
          "UNISTRUT anchoring to container steel not detailed "
          "(BW Water container scope)"),
         ("OBS-06", "MAJOR",
          "MAIN PANEL incoming routing not indicated"),
         ("OBS-07", "MAJOR",
          "S3/S4 zoning ambiguous between dosing skid and main panel"),
         ("OBS-08", "MAJOR",
          "Cable tray run conflicts with CIP system"),
     ],
     "Items remaining open from Transmittal N4: OBS-05 (FIT-09-001 "
     "duplicate, to verify in Rev C instrument schedule), OBS-06 "
     "(VT-09-001/002/003 missing), OBS-07 (TE-09-001..004 missing). "
     "Itemize closure on Rev C consolidated comment sheet."),

    # 2.9 GA SWRO Skid A
    ("2.9",
     "GA of SWRO System Skid Rev A — P22-DWG-09-005-008",
     "2 — Approved as Noted",
     "Two-sheet GA showing skid envelope, pressure vessel groupings, "
     "HP Pump, turbochargers, PSV, and process valves. Consistent with "
     "Equipment Layout Rev B and Valve List Rev D. First "
     "revision. Detailed comments: "
     "P22-DWG-09-005-008_A_GA_SWRO_Skid_CC_ADASA.pdf.",
     [
         ("NOTE-11", "MAJOR",
          "Equipment and valve schedule not provided (vessels per stage, "
          "elements per vessel, manifold material/pressure rating, "
          "function-vs-tag matrix)"),
         ("NOTE-12", "MAJOR",
          "Design pressure and material schedule for skid piping not "
          "summarized (ANSI class per service, pressure-temperature "
          "ratings, wall thickness)"),
     ],
     None),

    # 2.10 Control Philosophy B (Code 3)
    ("2.10",
     "Plant Control Philosophy Rev B — P22-BT-09-009-001",
     "3 — To be revised",
     "51-page document covering PLC platform, HMI, operator privileges, "
     "equipment-group control functions, and standardized control "
     "templates. Detailed cross-check against P&ID Rev C, "
     "Valve List Rev D, IO List Rev C, Instrument List Rev C and "
     "Technical Offer Rev1 raised seventeen findings "
     "(NOTE-13 to NOTE-29), one of them CRITICAL. "
     "Detailed comments: "
     "P22-BT-09-009-001_B_Control_Philosophy_CC_ADASA.pdf.",
     [
         ("NOTE-13", "MAJOR", "SEC formula and contractual guarantee not "
          "aligned (4.8/5.0 kWh/m³ vs Offer Rev1 "
          "4.71 kWh/m³ ±5%)"),
         ("NOTE-14", "MAJOR", "Vibration trip and alarm setpoints not numerical"),
         ("NOTE-15", "MAJOR", "Antiscalant dosing ratio source flow not "
          "aligned with P&ID Rev C"),
         ("NOTE-16", "MAJOR", "VE-09-002 modulating algorithm not defined"),
         ("NOTE-17", "MAJOR", "CIP cycle valve sequence not mapped to P&ID"),
         ("NOTE-18", "MINOR", "Motor RTD trip thresholds not stated"),
         ("NOTE-19", "MINOR", "Feed turbocharger isolation status not "
          "documented"),
         ("NOTE-20", "CRITICAL", "HP Pump start permissive contains erroneous "
          "TAGs (VE-09-007 duplicated; VE-09-014 antiscalant tank inlet "
          "wrongly included)"),
         ("NOTE-21", "MAJOR", "TAG FIT-09-001 reused between Section 3.1 "
          "(feed flow) and Section 3.3.4 (Stage 2 permeate)"),
         ("NOTE-22", "MAJOR", "Salt Rejection formula uses Stage 2 "
          "reject conductivity instead of feed conductivity"),
         ("NOTE-23", "MAJOR", "Orphan instruments and valves referenced "
          "without definition (TE-09-005, VE-09-006, VE-09-008)"),
         ("NOTE-24", "MAJOR", "Child documents referenced without formal "
          "delivery commitment (Alarm Setpoint List, RO/CIP Sequence "
          "Charts, Control Matrix)"),
         ("NOTE-25", "MAJOR", "SEC monitoring methodology measures wrong "
          "energy bus (RO PLC panel meter, not MCC main breaker)"),
         ("NOTE-26", "MAJOR", "Network architecture lacks redundancy and "
          "gateway fault management (unmanaged switches, PLX32 SPoF)"),
         ("NOTE-27", "MAJOR", "Three ET requirements unmet (manual mode "
          "without PLC §5.4, VFD ramp justification §5.4.6, "
          "low-pressure rupture interlock §7)"),
         ("NOTE-28", "MAJOR", "Off-spec routing without confirmed-closed "
          "interlock; bypass turbocharger OR-logic without cross-check"),
         ("NOTE-29", "MINOR", "Documentary quality: TAG format "
          "inconsistencies, triple AIT/CIT/AE nomenclature, template "
          "residue, page numbering, missing Consolidated Comment Sheet"),
     ],
     None),
]


def crear_transmittal():
    output_file = "TRANSMITTAL N15 ADASA-BW_WATER.docx"

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N15 — SECOND STAGE RO "
               "BRINE MODULE",
        codigo="P22-TM-09-000-015-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
        incluir_toc=True,
    )

    doc = Document(output_file)

    # Limpiar placeholder del template
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

    # ==================================================================
    # 1. EXECUTIVE SUMMARY
    # ==================================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(doc, [("TRANSMITTAL VERDICT: 3 — TO BE REVISED",
                    {"bold": True})])

    add_para(doc, [(
        "Ten documents reviewed from four deliveries (E30 to E33, "
        "April 16–22). Tally: 1 Code 1, 6 Code 2, "
        "3 Code 3 (LCP Datasheet Rev A, Cable Tray Rev B, "
        "Plant Control Philosophy Rev B require formal resubmittal). "
        "Detailed per-document comments in the attached CC_ADASA PDFs.",)])

    add_para(doc, [("Key findings:",)])

    BULLETS = [
        "3,500 mm CIP/dosing footprint constraint (TM N5/N7) — "
        "WITHDRAWN by ADASA, superseded by ADASA-side drawing "
        "P22-DWG-06-006-101.",
        "Equipment Layout Rev B: Operating Weight table to be embedded "
        "in Rev 0; BW Water Civil Loading drawing committed for "
        "23-Apr-2026.",
        "Cable Tray Rev B requires Rev C — 5 new observations "
        "(support interferences and routing errors) plus 2 inherited from "
        "TM N4, 78 days outstanding.",
        "Plant Control Philosophy Rev B elevated to Code 3 after "
        "detailed cross-check vs P&ID Rev C, Valve List Rev D, "
        "IO List Rev C and Technical Offer Rev1: 17 notes including "
        "1 CRITICAL (HP Pump permissive TAG errors).",
        "LCP Datasheet Rev A requires Rev B: cover sheet incomplete "
        "(IP rating, RTD channel count, dimensions, weight blank) preventing "
        "validation against Control System Architecture Rev D.",
    ]
    for b in BULLETS:
        add_bullet(doc, b)

    # ==================================================================
    # 2. OBSERVATIONS BY DOCUMENT
    # ==================================================================
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    for sec, heading, response_code, intro, notes_rows, extra in DOCS_DATA:
        doc.add_heading(heading, level=2)
        add_para(doc, [(f"Response Code: {response_code}", {"bold": True})])
        add_para(doc, [(intro,)])

        # WITHDRAWN inline special handling for §2.6
        if extra == "_WITHDRAWN_PIPING":
            add_para(doc, [
                ("Transmittal N7 OBS-01 / Transmittal N5 OBS-01 "
                 "— WITHDRAWN by ADASA: ", {"bold": True}),
                ("The 3,500 mm CIP/dosing footprint constraint is "
                 "hereby withdrawn. The CIP-to-dosing separation is "
                 "resolved on the ADASA side through the perimeter "
                 "interconnection drawing P22-DWG-06-006-101. The "
                 "11,150 mm separation in Piping Layout Rev B "
                 "is acceptable as drawn.",),
            ])

        # Tabla NOTE/OBS compacta
        rows = [("ID", "Severity", "Topic")]
        rows.extend(notes_rows)
        add_simple_table(doc, rows)

        # Parrafo extra (solo para 2.5 y 2.8)
        if extra and extra != "_WITHDRAWN_PIPING":
            add_para(doc, [(extra,)])

    # ==================================================================
    # 3. PENDING OBSERVATIONS
    # ==================================================================
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS",
                    level=1)

    add_para(doc, [(
        "Eight prior observations resolved: six closed (TM N3 "
        "OBS-01/02/03, TM N5 OBS-03/04/05, TM N11 OBS-04), "
        "two withdrawn by ADASA (TM N5 OBS-01, TM N7 OBS-01), "
        "and two from Transmittal N7 (OBS-03, OBS-04) incorporated "
        "as Rev 0 notes in Section 2.6. Items below remain open.",)])

    add_simple_table(
        doc,
        [
            ("Obs", "Document", "Description", "Outstanding Since", "Status"),
            ("TM N5\nOBS-01", "Equipment / Piping Layout",
             "3,500 mm CIP/dosing footprint constraint",
             "TM N5\n(23-Feb-2026)",
             "WITHDRAWN by ADASA — superseded by P22-DWG-06-006-101"),
            ("TM N7\nOBS-01", "Piping Layout",
             "CIP/dosing footprint 11,150 mm vs 3,500 mm",
             "TM N7\n(08-Mar-2026)",
             "WITHDRAWN by ADASA — superseded by P22-DWG-06-006-101"),
            ("TM N5\nOBS-02", "Equipment Layout",
             "Imperial dimensions retained as primary",
             "TM N5\n(23-Feb-2026)",
             "PARTIALLY OPEN — see Section 2.5"),
            ("TM N7\nOBS-03", "Piping Layout",
             "Equipment access door + lateral sliding door not "
             "represented",
             "TM N7\n(08-Mar-2026)",
             "INCORPORATED as Section 2.6 NOTE-06 for Rev 0"),
            ("TM N7\nOBS-04", "Piping Layout",
             "Cabinet integration unclear",
             "TM N7\n(08-Mar-2026)",
             "INCORPORATED as Section 2.6 NOTE-07 for Rev 0"),
            ("TM N4\nOBS-06", "Cable Tray Layout",
             "Vibration transmitter locations missing",
             "TM N4\n(05-Feb-2026)",
             "OPEN — 78 days outstanding"),
            ("TM N4\nOBS-07", "Cable Tray Layout",
             "Pt-100 motor sensor locations missing",
             "TM N4\n(05-Feb-2026)",
             "OPEN — 78 days outstanding"),
            ("TM N11\nOBS-03", "Grounding Layout",
             "Grounding schedule completeness",
             "TM N11\n(17-Mar-2026)",
             "PARTIALLY OPEN — see Section 2.3 NOTE-03"),
            ("TM N10\nOBS-05", "GA Antiscalant Dosing Tank",
             "Working volume, body material, seismic anchor data",
             "TM N10\n(12-Mar-2026)",
             "OPEN — GA Rev B still required"),
            ("TM N10\nNOTE-05", "HMI Screenshots\nP22-BREAD-09-008-001",
             "Committed at TM N4 — not submitted",
             "TM N4\n(03-Feb-2026)",
             "OPEN — 79 days outstanding"),
            ("TM N13\nNOTE-02", "Cable Tray Layout drawings",
             "Internal cable routing not submitted",
             "TM N13\n(06-Apr-2026)",
             "OPEN — tracked in ADASA email 10-Apr-2026"),
        ],
    )

    add_para(doc, [(
        "Tracked for IFC Rev 0: TM N12 NOTE-02 "
        "(Line List SCH 80S), TM N13 NOTE-01 (P&ID CIP Tank "
        "capacity), TM N8 OBS-04 (vibration setpoints).",)])

    # ==================================================================
    # 4. ATTACHMENTS
    # ==================================================================
    doc.add_heading("ATTACHMENTS", level=1)

    download_para = doc.add_paragraph()
    label_run = download_para.add_run("Download annotated PDFs (Synology Drive): ")
    label_run.bold = True
    aplicar_arial_12(download_para)
    download_url = (
        "https://lrg.synology.me:6501/d/s/"
        "17wnt7QrL3VJiw8tuKFZGva6q0ObmRAa/"
        "Yts9vGN_FJNnNnqy_yJKIaCINKKRJwlf-yruAehkPJA0"
    )
    add_hyperlink(download_para, download_url, download_url)

    add_simple_table(
        doc,
        [
            ("Document", "Annotated File", "Annotations"),
            ("Datasheet of Level Switch Rev B",
             "P22-LI-09-008-008_B_Level_Switch_CC_ADASA.pdf", "NOTE-01"),
            ("AC Thermal Calculation Rev C",
             "P22-CD-09-005-002_C_AC_Thermal_Calc_CC_ADASA.pdf", "NOTE-02"),
            ("Grounding Layout Rev C",
             "P22-DWG-09-007-003_C_Grounding_Layout_CC_ADASA.pdf",
             "NOTE-03"),
            ("LCP Datasheet Rev A",
             "P22-ET-09-007-005_A_LCP_Datasheet_CC_ADASA.pdf",
             "OBS-01, OBS-02, OBS-03"),
            ("Equipment Layout Rev B",
             "P22-DWG-09-005-003_B_Equipment_Layout_CC_ADASA.pdf",
             "NOTE-04"),
            ("Piping Layout Rev B",
             "P22-DWG-09-005-004_B_Piping_Layout_CC_ADASA.pdf",
             "NOTE-06, NOTE-07, NOTE-08, NOTE-09"),
            ("Instrument Location Layout Rev C",
             "P22-DWG-09-008-001_C_Instrument_Location_CC_ADASA.pdf",
             "NOTE-10"),
            ("Cable Tray Layout Rev B",
             "P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf",
             "OBS-04, OBS-05, OBS-06, OBS-07, OBS-08"),
            ("GA SWRO System Skid Rev A",
             "P22-DWG-09-005-008_A_GA_SWRO_Skid_CC_ADASA.pdf",
             "NOTE-11, NOTE-12"),
            ("Plant Control Philosophy Rev B",
             "P22-BT-09-009-001_B_Control_Philosophy_CC_ADASA.pdf",
             "NOTE-13 to NOTE-29 (17 annotations)"),
        ],
    )

    # ==================================================================
    # 5. RESPONSE SUMMARY
    # ==================================================================
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [
            ("Document Code", "Title", "Rev", "Response Code"),
            ("P22-LI-09-008-008", "Datasheet of Level Switch", "B",
             "1 — Approved"),
            ("P22-CD-09-005-002", "AC Thermal Calculation", "C",
             "2 — Approved as Noted"),
            ("P22-DWG-09-007-003",
             "Grounding Point & Power Panel Location Layout", "C",
             "2 — Approved as Noted"),
            ("P22-ET-09-007-005",
             "Datasheet of Local Control Panel (LCP)", "A",
             "3 — To be revised"),
            ("P22-DWG-09-005-003", "Equipment Layout", "B",
             "2 — Approved as Noted"),
            ("P22-DWG-09-005-004", "Piping Layout", "B",
             "2 — Approved as Noted"),
            ("P22-DWG-09-008-001", "Instrument Location Layout", "C",
             "2 — Approved as Noted"),
            ("P22-DWG-09-007-004",
             "Cable Tray Layout and Support Details", "B",
             "3 — To be revised"),
            ("P22-DWG-09-005-008", "GA of SWRO System Skid", "A",
             "2 — Approved as Noted"),
            ("P22-BT-09-009-001", "Plant Control Philosophy", "B",
             "3 — To be revised"),
        ],
    )

    add_para(doc, [("Overall Transmittal Verdict: 3 — TO BE REVISED",
                    {"bold": True})])

    FINAL_BULLETS = [
        "Tally: 1 Code 1 + 6 Code 2 + 3 Code 3.",
        "Closures: 6 OBS closed, 2 withdrawn by ADASA, 2 incorporated as "
        "Rev 0 notes.",
        "New findings: 28 notes and observations raised — breakdown "
        "per document in Section 2 tables; detail in attached "
        "CC_ADASA PDFs.",
        "Outstanding: 5 inherited from previous transmittals; TM N4 "
        "OBS-06/07 at 78 days require itemized closure on Cable Tray "
        "Rev C consolidated comment sheet.",
    ]
    for b in FINAL_BULLETS:
        add_bullet(doc, b)

    doc.save(output_file)
    print(f"Document generated successfully: {output_file}")


if __name__ == "__main__":
    crear_transmittal()
