#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N24 ADASA-BW_WATER (version EJECUTIVA).
Submittals 25007-0053 (E53) + 25007-0054 (E54). Fecha emision: 23-Jun-2026.

Veredicto global: 2 - APPROVED AS NOTED. Tally: 3 Code 1 + 2 Code 2.
IO List Rev 3 Code 2: las 2 senales de interfaz que ADASA pidio (TM N3/N7,
cerradas en N19) estan presentes y correctas (relay contact). ADASA extiende la
interfaz con 2 senales adicionales (falla, local/remoto) como REQUISITO NUEVO,
no como incumplimiento (verificado en el historico: solo se pidieron 2). LCP Rev 0
Code 2 (menores + HART ruteado al Datasheet PLC/HMI). CIP Cartridge Filter Rev E
(E54) cierra el Code 3 del TM N22.

Formato ejecutivo: Section 1 un parrafo (sin tabla de disposicion); Section 2
lean por documento; Code 1 sin CC_ADASA. SIN numeros manuales en add_heading()
(el template ADASA auto-numera H1/H2).
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
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.opc.constants import RELATIONSHIP_TYPE as RT  # noqa: E402


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N24 ADASA-BW_WATER.docx")

# Enlace de descarga de los CC_ADASA (comentarios anotados) — archivos pesados.
COMMENTS_URL = (
    "https://lrg.synology.me:6501/d/s/18mDuECJ9rwHGbSp6ZCZNBc3KBwMRRpe/"
    "dEK7YHd3mP5mYptfUOc-8aQB2mRmL71i-Pr9gXPHxSw0"
)


def add_hyperlink(paragraph, url, text):
    """Inserta un hipervinculo externo clicable (Arial 12, azul subrayado)."""
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
    sz.set(qn("w:val"), "24")
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


def add_para(doc, runs):
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
# Section 2 content (lean). heading, code, status[], obs[(id,sev,topic)], action[]
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="IO List Rev 3 — P22-LI-09-008-001",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" The two module-to-external-PLC interface signals previously "
             "requested and closed at Transmittal N19 (external enable XA005, "
             "module running status YA001) are present and correctly typed as "
             "relay contacts. ADASA is extending the interface with two further "
             "signals (a new requirement, this transmittal). The field I/O "
             "scheme over Ethernet/IP is consistent with the approach accepted "
             "at Transmittal N20. Annotations on "
             "P22-LI-09-008-001_3_IO_List_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "NEW REQUEST",
             "ADASA extends the module-to-external-PLC interface to four "
             "hardwired relay-contact signals (see the table below). The two "
             "previously transmitted and closed at Transmittal N19 (external "
             "enable XA005, module running status YA001) are present and "
             "correct; the module fault status and the module local/remote "
             "status are to be added, so plant-level control can react to a "
             "module fault and confirm when its start command will be "
             "accepted. New requirement introduced in this transmittal"),
            ("OBS-02", "MINOR",
             "Items 130 and 135 (dosing-pump RUNNING) are missing the "
             "signal-type count cell carried by every other point"),
            ("NOTE-01", "NOTE",
             "Transmittal N20 housekeeping is incorporated (numbering; the "
             "soft-I/O relabel from DI to BOOL): the field-device I/O scheme "
             "over Ethernet/IP was accepted at Transmittal N20 and is not "
             "reopened; the hardwired relay interface applies to the external "
             "PLC signals only"),
            ("NOTE-02", "NOTE",
             "The Valve List and the P&ID needed to cross-check the VE-09 "
             "motorized-valve I/O are not part of this submittal; the cross-check "
             "is tracked in Section 3"),
        ],
        action_paras=[
            [("Action to issue at IFC — no new review cycle required:",
              {"bold": True}),
             (" incorporate the two additional interface signals ADASA now "
              "requires as Relay Contact Output — SYSTEM FAULT STATUS TO DCS "
              "(output) and SYSTEM LOCAL/REMOTE STATUS TO DCS (output) "
              "(OBS-01); complete the signal-type count cell in items 130 and "
              "135 (OBS-02). The two previously agreed interface signals are "
              "present and correct. Issue for construction also depends on the "
              "Plant Control Philosophy children (Section 3).",)],
        ],
        interface_lead=(
            "Module-to-external-PLC interface — the four hardwired relay-contact "
            "signals (DCS = external plant PLC; module = RO module PLC):"),
        interface_table=[
            ("1", "External enable / start command", "DCS to module", "DI",
             "Present — XA005, relay contact"),
            ("2", "Module running status", "module to DCS", "DO",
             "Present — YA001, relay contact"),
            ("3", "Module fault status", "module to DCS", "DO",
             "To add — new requirement"),
            ("4", "Module local/remote status", "module to DCS", "DO",
             "To add — new requirement"),
        ],
    ),
    dict(
        heading="Datasheet of Local Control Panel (LCP) Rev 0 — P22-ET-09-007-005",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" The panel enclosure reconfirms the correct marine specification "
             "(SS316L, NEMA 4X / IP66); two minor corrections fold into the IFC "
             "issue. Annotations on "
             "P22-ET-09-007-005_0_LCP_Datasheet_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MINOR",
             "The aggregated power list (sheet 114) covers only the thirteen "
             "valve feeders, not the panel's own internal consumption; the 2.0 "
             "kW figure is not tied to the UPS SAI-09-001 sizing"),
            ("OBS-02", "MINOR",
             "Code-type inconsistency: the cover page carries the ET code "
             "P22-ET-09-007-005 while sheets 114 and 115 carry a DWG code"),
            ("NOTE-01", "NOTE",
             "The enclosure declared here (SS316L, NEMA 4X / IP66) reconfirms "
             "the correct marine specification; the enclosure contradiction "
             "tracked since Transmittal N20 resides in the Outline Panel Drawing "
             "(P22-CD-09-008-001), not in this datasheet"),
        ],
        action_paras=[
            [("Action to issue at IFC — no new revision required:", {"bold": True}),
             (" reconcile the panel internal-consumption and UPS figure on sheet "
              "114 (OBS-01); unify the document code to P22-ET-09-007-005 across "
              "the body (OBS-02). The enclosure is accepted as declared. "
              "Accepted as noted.",)],
        ],
    ),
    dict(
        heading="Instrumentation & Control Cable Schedule Rev 2 — P22-LI-09-008-002",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Field-instrument coverage is one-to-one with the IO List and the "
             "cable types match the signal types (shielded instrument cable for "
             "4-20 mA plus HART, Ethernet for the Ethernet/IP devices, control "
             "cable for the hardwired I/O); the four corrections from Transmittal "
             "N20 are incorporated. No defect of this document.",),
        ],
        obs=[],
        action_paras=[
            [("Action: none — accepted; issue directly at IFC Rev 0.",
              {"bold": True})],
        ],
    ),
    dict(
        heading="Data Transfer List (Modbus TCP/IP) Rev 2 — P22-LI-09-008-004",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" The Modbus interface to the supervisory system is consistent; no "
             "module safety or start signal is carried by Modbus alone (the "
             "external start and run-status interface remains hardwired in the "
             "IO List); the conductivity-scale item raised at the previous cycle "
             "is closed in Rev 2.",),
        ],
        obs=[],
        action_paras=[
            [("Action: none on this document — accepted; issue directly at IFC "
              "Rev 0.", {"bold": True}),
             (" One related verification is tracked in Section 3: confirm, "
              "against the Control Matrix once delivered, that the RO HP Pump "
              "start respects the external hardwired ENABLE (XA005) rather than "
              "a Modbus bit.",)],
        ],
    ),
    dict(
        heading="Datasheet of CIP Cartridge Filter Rev E — P22-ET-09-009-006",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Materially closes the Transmittal N22 observation: the cartridge "
             "gasket is now EPDM and a material-compatibility statement for the "
             "FRP housing and the seal against the CIP fluid (pH 2 to 12) is "
             "attached; the previous minor items (component name, per-cartridge "
             "surface area and filtration rate) are corrected. Design pressure "
             "and temperature (7 bar / 45 C, hydrotest 8 bar) and the vertical "
             "configuration are consistent with the Technical Specification.",),
        ],
        obs=[
            ("NOTE-01", "NOTE",
             "Confirm at the IFC issue that the housing-cover gasket is also "
             "EPDM (the vendor's generic guide on page 3 cites standard nitrile); "
             "material certificates go to the vessel fabrication dossier"),
        ],
        action_paras=[
            [("Action: none on this document — accepted; issue directly at IFC "
              "Rev 0.", {"bold": True}),
             (" Confirm the cover-gasket elastomer (NOTE-01); material "
              "certificates are tracked to the fabrication dossier, not this "
              "datasheet.",)],
        ],
    ),
]


# Section 3 — open items.
ADDRESSED_TEXT = (
    "Transmittal N22 Section 2.4 (the CIP Cartridge Filter, gasket and FRP "
    "housing compatibility against the CIP fluid at pH 2 to 12) is materially "
    "closed by the CIP Cartridge Filter Datasheet Rev E, which now specifies an "
    "EPDM gasket and attaches the material-compatibility statement. The IO List, "
    "the Cable Schedule and the Modbus Data Transfer List are dispositioned in "
    "Section 2; the residual that remains open is the dependence of the control "
    "package on the Plant Control Philosophy children below. The 4-20 mA plus "
    "HART instrumentation requirement (ET Instrumentation Specification) is met "
    "by the offered transmitters, all 4-20 mA plus HART in the Technical Offer; "
    "the HART acquisition point carried from Transmittal N21 is closed."
)

PENDING_OPEN = [
    ("TM N22 Section 2.1",
     "Plant Control Philosophy children: Operating Sequence Charts "
     "(P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) "
     "and Control Matrix",
     "The operative numerical control logic remains in child documents not "
     "delivered; it also gates the IO List Rev 3 reaching issue for "
     "construction",
     "OPEN: not delivered with this submittal; the sixth cycle with that logic "
     "outside the package"),
    ("TM N20 Section 2.6",
     "PLC-LCP Outline Panel Drawing (P22-CD-09-008-001)",
     "Enclosure contradiction (sheet steel / IP55 versus SS316L / NEMA 4X-IP66); "
     "the LCP Datasheet Rev 0 reconfirms the correct SS316L / NEMA 4X-IP66 side, "
     "so the contradiction resides in the Outline drawing",
     "OPEN: Outline Rev B aligned to the datasheet enclosure awaited; the "
     "expedited release path of the 10-Jun response applies"),
    ("TM N22 Section 2.2",
     "Equipment Layout (P22-DWG-09-005-003)",
     "RO Cartridge Filter still drawn horizontal against its own vertical "
     "datasheet",
     "OPEN: to re-issue as Rev D with the RO Cartridge Filter vertical; this "
     "also gates the Instrument Location Layout"),
]

PENDING_PROCEDURAL = [
    "Control-logic verification: confirm, when the Control Matrix is delivered, "
    "that the RO HP Pump start respects the external hardwired ENABLE (XA005), "
    "not a Modbus bit (Section 2.4).",
    "Valve List and P&ID (P22-DWG-09-009-02) needed to cross-check the VE-09 "
    "motorized-valve I/O of the IO List (Section 2.1, NOTE-02).",
    "Grounding Point and Power Panel Location Layout Rev F (due 17-Jun-2026) and "
    "the FAT/SAT comparison table (due 15-Jun-2026): not received with this "
    "submittal; tracked. The Inspection and Test Plan Rev 0 conditions remain "
    "open; the ASME stamp remains waived and is not reopened.",
]


ATTACHMENTS = [
    ("IO List Rev 3", "Code 2",
     "P22-LI-09-008-001_3_IO_List_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01, NOTE-02"),
    ("Datasheet of Local Control Panel (LCP) Rev 0", "Code 2",
     "P22-ET-09-007-005_0_LCP_Datasheet_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
]


RESPONSE_SUMMARY = [
    ("P22-LI-09-008-001", "IO List", "3", "2 — Approved as Noted"),
    ("P22-ET-09-007-005", "Datasheet of Local Control Panel (LCP)", "0",
     "2 — Approved as Noted"),
    ("P22-LI-09-008-002", "Instrumentation & Control Cable Schedule", "2",
     "1 — Approved"),
    ("P22-LI-09-008-004", "Data Transfer List (Modbus TCP/IP)", "2",
     "1 — Approved"),
    ("P22-ET-09-009-006", "Datasheet of CIP Cartridge Filter", "E",
     "1 — Approved"),
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N24 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-024-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 2 — Approved as Noted.", {"bold": True}),
        (" Five documents (submittals 25007-0053 and 25007-0054). Tally: 3 Code "
         "1, 2 Code 2. The IO List Rev 3 and the Local Control Panel Datasheet "
         "are Approved as Noted, with minor items to fold into the construction "
         "issue. On the IO List, the two module-to-external-PLC interface "
         "signals previously requested are present and correct; ADASA extends "
         "the interface with two further hardwired signals (a new requirement). "
         "The Local Control Panel Datasheet enclosure reconfirms the correct "
         "marine specification, with two minor corrections noted. The Cable "
         "Schedule, the Modbus Data Transfer List "
         "and the CIP Cartridge Filter Datasheet (which closes the CIP "
         "fabrication item from Transmittal N22) are Approved. Per-document "
         "codes, observations and required actions are in Section 2; open items "
         "from previous transmittals are inventoried in Section 3.",),
    ])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        add_para(doc, sec["status"])
        if sec.get("obs"):
            add_simple_table(
                doc, [("ID", "Severity", "Topic")] + list(sec["obs"]))
        if sec.get("interface_table"):
            add_para(doc, [(sec["interface_lead"],)])
            add_simple_table(doc, [
                ("#", "Interface signal", "Direction", "Type",
                 "Status in IO List Rev 3")] + list(sec["interface_table"]))
        for ap in sec["action_paras"]:
            add_para(doc, ap)

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [(
        "This submittal delivered E53 and E54 only.",)])
    add_para(doc, [
        ("Addressed in this transmittal: ", {"bold": True}),
        (ADDRESSED_TEXT,)])
    add_para(doc, [
        ("Open from previous transmittals — the three most serious",
         {"bold": True}),
        (" (minor open items remain tracked in the Master Deliverable "
         "Register):",)])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [
        ("Open deliverables and procedural items (not document defects):",
         {"bold": True})])
    for txt in PENDING_PROCEDURAL:
        add_bullet(doc, txt)

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)
    add_para(doc, [(
        "Two documents carry notes and are returned with annotated PDFs "
        "(2 Code 2). The three Code 1 — Approved documents (Cable Schedule, "
        "Data Transfer List and CIP Cartridge Filter) require no modification "
        "and carry no annotated PDF.",)])

    link_para = doc.add_paragraph()
    link_para.add_run(
        "Given the file size, the annotated PDFs (CC_ADASA) are also available "
        "for download here: ")
    add_hyperlink(link_para, COMMENTS_URL, "Annotated comments (download)")
    aplicar_arial_12(link_para)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 2 — APPROVED AS NOTED.", {"bold": True}),
        (" Tally: 3 Code 1, 2 Code 2. The IO List Rev 3 and the Local Control "
         "Panel Datasheet carry minor notes to fold into the construction "
         "issue. Documents not appearing in this response are unaffected by "
         "this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
