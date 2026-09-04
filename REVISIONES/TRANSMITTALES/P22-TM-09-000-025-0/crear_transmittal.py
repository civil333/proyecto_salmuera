#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N25 ADASA-BW_WATER (version EJECUTIVA).
Submittals 25007-0055 (E55) + 25007-0056 (E56). Fecha emision: 29-Jun-2026.

Veredicto global: 3 - TO BE REVISED. Tally: 4 Code 1 + 1 Code 2 + 1 Code 3.
Driver unico: PLC-LCP Outline Panel Drawing Rev B Code 3 - la contradiccion de
material del enclosure (gate de fabricacion del TM N20) sigue abierta: COLOR
agrega "Exterior SUS316L" pero MATERIAL/FINISHING describen un enclosure de
sheet steel pintado RAL 7035. IO List Rev 4 Code 2 - las 4 senales de interfaz
con el PLC externo quedan correctas y completas (cierra OBS-01 N24); la unica
nota real es la celda de conteo de las dosificadoras (OBS-02 N24, menor, fold a
Rev 0). El esquema soft-I/O Ethernet/IP de campo fue aceptado en N20 y NO se
reabre (la OBS-01 anterior 'soft-BOOL = no feedback' era over-reach; ver
[[project_senales_interfaz]]).
Code 1: LCP Datasheet Rev 1 (cierra N24), UHPRO Structural Rev B (cierra N23
sismica + criterios de izaje), Static Mixer Rev 0 (item contratado Oferta Rev1),
Painting Spec Rev C (Jotun condicionado a equivalencia, abierta en el Procedure).

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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N25 ADASA-BW_WATER.docx")

# Los 2 CC_ADASA (IO List Code 2 + Outline Code 3, ~4.8 MB) se adjuntan directo al
# correo; no se usa link de descarga Synology (decision del usuario 29-Jun).


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
        heading="IO List Rev 4 — P22-LI-09-008-001",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" The four module-to-external-PLC interface signals are present and "
             "correctly typed as relay contacts — external enable XA005, running "
             "status YA001, and the two ADASA extended at Transmittal N24, system "
             "fault status YA002 and system local/remote status YA003. That request "
             "is closed; the interface is complete. The soft-I/O field scheme over "
             "Ethernet/IP accepted at Transmittal N20 is not reopened. Two minor "
             "items fold into the construction issue: the dosing-pump run-status "
             "count cell, and a confirmation that the run status reflects a verified "
             "pump feedback. Annotations on "
             "P22-LI-09-008-001_4_IO_List_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MINOR",
             "The dosing-pump RUNNING (items 131 and 136), typed BOOL, carry no "
             "signal-type count in any column, so the Transmittal N24 observation "
             "(the dosing-pump run status missing the count cell that every other "
             "point carries) persists; items 129 and 134, also typed BOOL, place "
             "their count in the DI column rather than the BOOL column"),
            ("NOTE-01", "NOTE",
             "Closure record: the four module-to-external-PLC interface signals are "
             "present and correctly typed as relay contacts. The two added at "
             "Transmittal N24 (fault status, local/remote status) are an ADASA "
             "extension of the interface and are correctly incorporated"),
            ("NOTE-02", "NOTE",
             "Confirm that the dosing-pump run status (items 131 and 136, BOOL over "
             "Ethernet/IP, shown FROM the HMI) reflects a verified feedback from the "
             "pump or its drive on the network, not an echo of the operator "
             "faceplate. The soft-I/O field scheme over Ethernet/IP accepted at "
             "Transmittal N20 is not reopened; this confirms the data source only"),
            ("NOTE-03", "NOTE",
             "The Valve List and the P&ID needed to cross-check the VE-09 "
             "motorized-valve I/O are not part of this submittal; the cross-check is "
             "tracked in Section 3. BW Water reports the tags are aligned (VE09 to "
             "VE-09; the pump tags to the P&ID and the Equipment List)"),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new review cycle required:",
              {"bold": True}),
             (" complete the signal-type count on items 131 and 136 and place the "
              "count in the BOOL column on items 129 and 134 (OBS-01); confirm the "
              "dosing-pump run-status source (NOTE-02). The four interface signals "
              "are present and correct. Issue for construction also depends on the "
              "Plant Control Philosophy children (Section 3).",)],
        ],
    ),
    dict(
        heading="Datasheet of Local Control Panel (LCP) Rev 1 — P22-ET-09-007-005",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Closes the Transmittal N24 cycle. Sheet 114 now reconciles the "
             "panel's own consumption with the UPS (thirteen VE-09 valve feeders "
             "at 1.56 kW plus the SAI-09-001 controller power supply at 0.24 kW, "
             "totalling 1.80 kW, and 2.00 kW with the design factor), and the "
             "conflicting DWG code in the body is removed and unified to "
             "P22-ET-09-007-005. The enclosure marine specification (SS316L, "
             "NEMA 4X/IP66) is reconfirmed; this datasheet governs the enclosure, "
             "and the Outline Panel Drawing must align to it (Section 2.4, still "
             "Code 3).",),
        ],
        obs=[
            ("NOTE-01", "NOTE",
             "The power-list document-number field on sheet 114 is left blank; "
             "populate it with P22-ET-09-007-005 at the IFC Rev 0 issue "
             "(housekeeping; no new revision required)"),
        ],
        action_paras=[
            [("Action: none on this datasheet — accepted; issue directly at IFC "
              "Rev 0,", {"bold": True}),
             (" populating the blank sheet-114 document number at issue. The "
              "enclosure-specification alignment lives in the Outline Panel Drawing "
              "(Section 2.4), not in this datasheet.",)],
        ],
    ),
    dict(
        heading="Datasheet of Static Mixer Rev 0 — P22-ET-09-009-012",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Closes the Transmittal N22 cycle. The Static Mixer datasheet "
             "(MZE-09-001) returns at Rev 0 and reconciles the design-condition and "
             "injection-rate discrepancy noted at Transmittal N22, adding a "
             "conservative-values remark. The mixer is a contracted item; the BW "
             "Water Technical Offer Rev1 lists a one-by-one-hundred-percent FRP "
             "static mixer for this duty. The vendor substitution from Komax to "
             "N-Spindle NS11 is permitted under the offer's \"or equal\", with a "
             "coefficient of variation of 0.05 demonstrating mixing equivalence; "
             "the FRP housing, the ANSI 150 connections and the design pressure and "
             "temperature are consistent with the antiscalant service.",),
        ],
        obs=[
            ("NOTE-01", "NOTE",
             "The Komax-to-N-Spindle NS11 substitution is permitted under the "
             "offer's \"or equal\"; the coefficient of variation of 0.05 "
             "demonstrates mixing equivalence"),
            ("NOTE-02", "NOTE",
             "The injection-port size (DN15) is smaller than the offer reference "
             "(one inch); it is ample for the antiscalant dosing rate"),
        ],
        action_paras=[
            [("Action: none on this datasheet — accepted; issue directly at IFC "
              "Rev 0.", {"bold": True}),
             (" Cross-document checks (the injection rate against the antiscalant "
              "dosing-pump duty; the tag and the line class at the injection point "
              "on the P&ID) are tracked in Section 3.",)],
        ],
    ),
    dict(
        heading="PLC-LCP Outline Panel Drawing Rev B — P22-CD-09-008-001",
        code="Response Code: 3 — To Be Revised",
        status=[
            ("Status.", {"bold": True}),
            (" The Transmittal N20 enclosure contradiction is only half-corrected, "
             "so the panel fabrication hold continues. Rev B adds an \"Exterior "
             "SUS316L\" colour line, replaces the forced-air cooling with a sealed "
             "NEMA 4X stainless-steel air-conditioning unit, and declares the panel "
             "weight (814 kg); these resolve the cooling and weight observations. "
             "The blocking item remains the substrate. The "
             "MATERIAL row still specifies 2.0 mm sheet steel for the enclosure "
             "frame, roof, rear panel and door; the FINISHING rows still paint those "
             "surfaces GRAY RAL 7035 and zinc-plate the bottom gland plate. A "
             "fabrication shop cutting from the MATERIAL row would build the painted "
             "sheet-steel enclosure raised at Transmittal N20, incompatible with the "
             "coastal site. Annotations on "
             "P22-CD-09-008-001_B_Outline_Panel_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "CRITICAL",
             "The MATERIAL row lists the enclosure frame, roof, rear panel, gland "
             "plates and door as sheet steel under a \"SHEET STEEL (INTERIOR ONLY)\" "
             "heading, and the FINISHING rows paint these weather-exposed surfaces "
             "GRAY RAL 7035 — internally contradicting the same sheet's \"Exterior "
             "SUS316L\" colour line. The drawing thereby specifies an enclosure "
             "below the approved documents that govern it: the LCP Datasheet Rev B "
             "(nVent Hoffman FS66S, unpainted SS316L, NEMA 4X/IP66, for highly "
             "corrosive environments) and the IFC Single Line Diagram Rev 0 "
             "(\"METAL CLAD, NEMA 4X/IP66\"). The Technical Specification — Power "
             "and Control Switchboards, Constructive Characteristics requires a "
             "NEMA 4X protection class or its IP equivalent, not lower; the SS316L "
             "enclosure material is fixed by the approved LCP Datasheet, to which "
             "the Outline must conform. This is the fabrication-gating decision"),
            ("OBS-02", "MAJOR",
             "The bottom gland plate is zinc-plated. Specify SS316L for the exterior "
             "bottom gland plate, or confirm in writing that it is shielded from the "
             "weather"),
            ("NOTE-01", "MINOR",
             "The protection class prints \"NEMA 4X\" without the IP66 figure; add "
             "\"/IP66\" to match the LCP Datasheet and the Single Line Diagram"),
            ("NOTE-02", "MINOR",
             "The title-block project title is misspelled (\"SECONDE STAGE\"), and "
             "the discipline field reads \"Process\" on a control-panel drawing"),
        ],
        action_paras=[
            [("Action — re-issue as Rev C:", {"bold": True}),
             (" declare SS316L on every weather-exposed surface (frame, roof, doors, "
              "sides, rear and the bottom gland plate) consistently across the "
              "COLOUR, MATERIAL and FINISHING rows, restricting sheet steel, "
              "zinc-plating and CRS hardware to internal components; add the IP66 "
              "figure to the protection class; and correct the title block. Closure "
              "threshold: panel fabrication release stays gated on a coherent SS316L "
              "specification consistent with the LCP Datasheet (Section 2.2), as set "
              "out in the expedited-path response of 10-Jun-2026.",)],
        ],
    ),
    dict(
        heading="UHPRO Structural Design Criteria Rev B — P22-CD-09-005-003",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Closes the Transmittal N23 cycle. Every seismic parameter and the "
             "allowable-stress and strength load combinations are now cited to "
             "NCh 2369 Of.2003, with the clause 4.5 combinations confirmed as "
             "governing the seismic allowable-stress verification, closing the "
             "edition and combination observations. The lifting load case is now "
             "included with its padeye and yoke design criteria (API RP 2A-WSD "
             "dynamic-amplification factors of 1.35 and 2.0, a padeye factor of "
             "safety of 2.0 with a 5% out-of-plane lateral, and a spreader-beam yoke "
             "approach). The final lifting design follows as a separate deliverable.",),
        ],
        obs=[
            ("NOTE-01", "NOTE",
             "The lifting load case, the padeye criteria and the spreader-beam yoke "
             "approach are present, closing the Transmittal N23 lifting observation "
             "at the criteria level. The final lifting design — the lifting "
             "calculation, the lifting drawing with weights, and the yoke design — "
             "is a separate deliverable tracked in Section 3"),
            ("NOTE-02", "NOTE",
             "Fold the editorial items at issue: reconcile the cover-block date "
             "against the 23-Jun-2026 body date and remove the duplicate table "
             "number; confirm the minimum wind pressures render as N/m2 on the "
             "issued PDF"),
        ],
        action_paras=[
            [("Action: none on this criteria document — accepted; issue directly at "
              "IFC Rev 0,", {"bold": True}),
             (" folding the editorial items at issue. The final lifting design and "
              "the seismic calculation memo are tracked in Section 3.",)],
        ],
    ),
    dict(
        heading="Painting Specification Rev C — P22-ET-09-006-002",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" This is the painting specification (ET level), distinct from the "
             "Painting Procedure that carries the Transmittal N23 Code 3. The "
             "specified system matches the marine coating architecture of the "
             "Technical Specification (80 / 200 / 75 = 355 micrometres total, "
             "Sa 2½ preparation), and the MAKE column names Sherwin-Williams "
             "products with generic equivalents; no buildable non-marine system is "
             "authorized by the specification itself.",),
        ],
        obs=[
            ("NOTE-01", "NOTE",
             "The brand list now reads \"Sherwin-Williams, Jotun or similar "
             "technically equivalent approved by ADASA\". This is not approval of a "
             "Jotun system: actual use of any non-Sherwin-Williams system still "
             "requires ADASA's documented product-to-product equivalence and the "
             "C5-M marine durability demonstration, which remain open at the "
             "Painting Procedure (Section 3)"),
            ("NOTE-02", "NOTE",
             "For the platform and the safety supports, verify the "
             "surface-preparation grade against the selected zinc primer's data "
             "sheet — an inorganic-zinc primer typically requires SSPC-SP10 rather "
             "than the SSPC-SP6 shown for those items"),
            ("NOTE-03", "NOTE",
             "The document code has changed from P22-ET-09-005-002 (Rev B, approved "
             "at Transmittal N11) to P22-ET-09-006-002 (Rev C). Confirm the "
             "re-coding is intentional and that this Rev C supersedes the "
             "Transmittal N11 approved Rev B, so the deliverable register can be "
             "aligned"),
        ],
        action_paras=[
            [("Action: none on this specification — accepted; issue directly at IFC "
              "Rev 0.", {"bold": True}),
             (" The Rev 0 issue should carry an explicit note that any "
              "non-Sherwin-Williams system is conditional on ADASA's pending "
              "equivalence approval (Section 3), holding the position taken at "
              "Transmittal N23. Confirm the document-code change (NOTE-03).",)],
        ],
    ),
]


# Section 3 — open items.
ADDRESSED_TEXT = (
    "Transmittal N24 (the LCP Datasheet panel-power and code items, and the four "
    "module-to-external-PLC interface signals on the IO List) and Transmittal N23 "
    "(the UHPRO Structural Design Criteria seismic citations and lifting criteria) "
    "are dispositioned in Section 2. The 4-20 mA plus HART acquisition point "
    "carried from Transmittal N21 stays closed (RFI-001, 24-Jun-2026); the CIP "
    "Cartridge Filter is closed (Transmittal N24); the ASME stamp remains waived "
    "and is not reopened."
)

PENDING_OPEN = [
    ("TM N22 Section 2.1",
     "Plant Control Philosophy children: Operating Sequence Charts "
     "(P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) "
     "and Control Matrix",
     "The operative numerical control logic remains in child documents not "
     "delivered; it gates the IO List reaching issue for construction",
     "OPEN and overdue: not delivered with this submittal; the sixth cycle with "
     "that logic outside the package"),
    ("TM N20 Section 2.6",
     "PLC-LCP Outline Panel Drawing (P22-CD-09-008-001)",
     "Enclosure material contradiction — see Section 2.4",
     "OPEN: re-issue as Rev C with a coherent SS316L specification; fabrication "
     "release remains gated"),
    ("TM N22 Section 2.2",
     "Equipment Layout (P22-DWG-09-005-003)",
     "RO Cartridge Filter still drawn horizontal against its own vertical "
     "datasheet",
     "OPEN: to re-issue as Rev D; no new revision in this delivery"),
    ("TM N23 Section 2",
     "Quality and fabrication package: NDE Plan (P22-BA-09-000-005), HP and LP "
     "Pressure Test Procedure (P22-BA-09-000-010), RO Vessel Hydrostatic Test "
     "Procedure (P22-BA-09-000-009), Painting Procedure (P22-BA-09-000-011)",
     "The four Code 3 procedures await new revisions; the Painting Procedure must "
     "provide the Jotun product-to-product equivalence and ADASA approval, "
     "demonstrate C5-M durability, and unify the anchor profile to a single range "
     "with a 50 micrometre lower bound",
     "OPEN: no new revisions in this delivery"),
]

OVERDUE = [
    "Grounding Point and Power Panel Location Layout Rev F — committed for "
    "17-Jun-2026, twelve days overdue.",
    "FAT and SAT comparison table — committed for 15-Jun-2026, fourteen days "
    "overdue.",
    "The three mechanical installation-route plans (Maintenance Lifting Points, "
    "3D Model, GA RO HP Pump) — committed for 26-Jun-2026, three days overdue.",
]

CROSS_DOC = [
    "IO List: the VE-09 motorized-valve I/O cross-check against the Valve List and "
    "the P&ID (P22-DWG-09-009-02).",
    "Static Mixer: the antiscalant injection rate against the accepted dosing-pump "
    "duty, and the MZE-09-001 tag and the line class at the injection point on the "
    "P&ID (P22-DWG-09-009-02-P8).",
    "Structural: the final lifting design (lifting calculation, lifting drawing "
    "with weights, yoke design), the numerical design seismic weight, and the "
    "seismic calculation memo confirming frame and anchor integrity under "
    "NCh 2369 Zone 3.",
]


ATTACHMENTS = [
    ("IO List Rev 4", "Code 2",
     "P22-LI-09-008-001_4_IO_List_CC_ADASA.pdf",
     "OBS-01, NOTE-01, NOTE-02, NOTE-03"),
    ("PLC-LCP Outline Panel Drawing Rev B", "Code 3",
     "P22-CD-09-008-001_B_Outline_Panel_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01, NOTE-02"),
]


RESPONSE_SUMMARY = [
    ("P22-LI-09-008-001", "IO List", "4", "2 — Approved as Noted"),
    ("P22-ET-09-007-005", "Datasheet of Local Control Panel (LCP)", "1",
     "1 — Approved"),
    ("P22-ET-09-009-012", "Datasheet of Static Mixer", "0", "1 — Approved"),
    ("P22-CD-09-008-001", "PLC-LCP Outline Panel Drawing", "B",
     "3 — To Be Revised"),
    ("P22-CD-09-005-003", "UHPRO Structural Design Criteria", "B",
     "1 — Approved"),
    ("P22-ET-09-006-002", "Painting Specification", "C", "1 — Approved"),
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N25 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-025-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To Be Revised.", {"bold": True}),
        (" Six documents (submittals 25007-0055 and 25007-0056). Tally: 4 Code 1, "
         "1 Code 2, 1 Code 3. The verdict rests on one document: the PLC-LCP "
         "Outline Panel Drawing Rev B only half-corrects the enclosure-material "
         "contradiction that gates panel fabrication — it adds an exterior SUS316L "
         "line and a sealed air-conditioning unit, yet the material and finishing "
         "rows still build a painted sheet-steel enclosure. The IO List Rev 4 "
         "incorporates the four module-to-external-PLC interface signals ADASA "
         "required and is Approved as Noted, with the dosing-pump count cell to "
         "complete at the construction issue. The remaining four documents are "
         "Approved: the LCP Datasheet Rev 1 "
         "closes the Transmittal N24 panel-power and code items, the UHPRO "
         "Structural Design Criteria Rev B closes the Transmittal N23 seismic and "
         "lifting-criteria items, the Static Mixer Datasheet Rev 0 closes the "
         "Transmittal N22 cycle on a contracted item, and the Painting "
         "Specification Rev C is accepted with the brand and document-code "
         "conditions noted. Per-document codes and required "
         "actions are in Section 2; open and overdue items from previous "
         "transmittals are inventoried in Section 3.",),
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
        for ap in sec["action_paras"]:
            add_para(doc, ap)

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [(
        "This submittal delivered E55 and E56 only.",)])
    add_para(doc, [
        ("Addressed in this transmittal: ", {"bold": True}),
        (ADDRESSED_TEXT,)])
    add_para(doc, [
        ("Open from previous transmittals — the most serious:", {"bold": True})])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [
        ("Overdue deliverables (today is 29-Jun-2026):", {"bold": True})])
    for txt in OVERDUE:
        add_bullet(doc, txt)
    add_para(doc, [
        ("Cross-document checks raised by this transmittal (not defects of the "
         "approved documents):", {"bold": True})])
    for txt in CROSS_DOC:
        add_bullet(doc, txt)

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)
    add_para(doc, [(
        "The two documents with open observations carry annotated PDFs (1 Code 2 + "
        "1 Code 3), attached to this transmittal. The four Code 1 — Approved "
        "documents (LCP Datasheet, Static Mixer Datasheet, UHPRO Structural Design "
        "Criteria and Painting Specification) require no modification and carry no "
        "annotated PDF.",)])

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.", {"bold": True}),
        (" Tally: 4 Code 1, 1 Code 2, 1 Code 3. The PLC-LCP Outline Panel Drawing "
         "fixes the verdict: the enclosure-material contradiction continues to gate "
         "panel fabrication. The IO List Rev 4 is Approved as Noted — the four "
         "module-to-external-PLC interface signals are present and correct, with "
         "the dosing-pump count cell to complete at the construction issue. The "
         "remaining four documents close the Transmittal N24 panel, the Transmittal "
         "N23 structural and the Transmittal N22 static-mixer cycles. Documents not "
         "appearing in this response are unaffected by this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
