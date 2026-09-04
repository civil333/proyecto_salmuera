#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N29 ADASA-BW_WATER.
Submittal 25007-0067 (E67). Fecha emision: 21-Jul-2026.

Veredicto global: 2 - APPROVED AS NOTED. Tally: 2 Code 2, 2 Code 1.
Cuatro documentos, todas re-revisiones (TM de recuperacion): cierra los dos
Code 3 vencidos (HP/LP Pressure Test de N27, UHPRO Structural Calc de N26) y
recibe el Outline y el Line List emitidos a IFC Rev 0.

- HP and LP Pressure Test Procedure Rev D (P22-BA-09-000-010): Code 2. El error
  critico de 75 bar sobre linea PVC (N27) esta resuelto y verificado; residual
  editorial = fijar edicion ASME.
- UHPRO Structural Calculation Report Rev B (P22-CD-09-005-001): Code 2. Responde
  los 7 comentarios del N26; corte basal NCh 2369:2003 Zona 3 = 41,62 kN,
  utilizacion max 0,454 < 1,0, norma 2003 (no 2025). Residual = housekeeping (PDF
  duplicado + CCS sin texto de comentarios).
- PLC/LCP Outline Panel Drawing Rev 0 IFC (P22-CD-09-008-001): Code 1. Incorpora
  la RFI-002 (SS316L exterior + gland plates, internos galvanizados, NEMA 4X/
  IP66) y cierra los 3 MINOR del N27; SLD reemitido Rev 1. Residuales cosmeticos.
- Line List Rev 0 IFC (P22-LI-09-009-003): Code 1. Correcto y consistente con el
  P&ID Rev D; correccion 50->2 bar en 09-016 verificada, a declarar en el
  historial de revision.

SIN numeros manuales en add_heading() (el template ADASA auto-numera H1/H2).
Referencias por NOMBRE de seccion. Cero simbolo de seccion.
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N29 ADASA-BW_WATER.docx")

DOWNLOAD_LINK = "https://lrg.synology.me:6501/d/s/199TcR9nfzQGBsdiqjFx1KBITOy7Czm5/IKYQplKAUYslUaQQSd6OflbA0m4xU-9--Vb9gGZr7XQ0"


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
# Section 2 (condensado). Orden: los dos Code 2 (recuperaciones) primero, luego
# los dos Code 1 (IFC). Sin tabla OBS: el detalle vive en cada CC_ADASA.
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="HP and LP Pressure Test Procedure Rev D — P22-BA-09-000-010",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Rev D closes the critical finding that returned Rev C as Code 3. The "
             "hydrostatic test pressures are now set per line and material through the "
             "attached Line List: the RO brine discharge line DA-PVC-DN65-09-016 (PVC) is "
             "corrected to a 3 bar hydrotest at 2 bar design, no PVC line is tested above "
             "7.5 bar, and the 135 bar test is confined to the Super Duplex lines; the body "
             "now states 135 bar for high pressure and 7.5 bar for low pressure and "
             "references the Line List by number and revision, and the clause-numbering gap "
             "is corrected. The four comment-sheet items from Transmittal N27 are closed "
             "and verified in the body. One editorial note remains: the ASME Section V and "
             "ASME B31.3 references are cited as \"applicable edition\" without fixing the "
             "edition and addenda. Itemised in "
             "P22-BA-09-000-010_D_HP_LP_Pressure_Test_CC_ADASA.pdf.",),
        ],
        action_paras=[
            [("Action — approved as noted, no new revision required:", {"bold": True}),
             (" state the applicable edition and addenda of ASME Section V and ASME B31.3 "
              "at the next issue (NOTE-01 on the annotated PDF). On that, the procedure is "
              "approved for the pressure tests; the high-pressure hydrostatic test remains "
              "a Hold Point.",)],
        ],
    ),
    dict(
        heading="UHPRO Structural Calculation Report Rev B — P22-CD-09-005-001",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Rev B resolves the finding that returned Rev A as Code 3. The report now "
             "carries the design seismic weight, the global base shear and the NCh 2369 "
             "base-shear check (operating base shear 41.62 kN, Zone 3), the governing skid "
             "utilization ratio (0.454, below the 1.0 limit), the material grades, the Site "
             "Class E basis and the container base reactions, and the load-combination typo "
             "is corrected. The seismic design uses IBC 2018 (ASCE 7-16) calibrated to the "
             "Chilean base shear with the NCh 2369:2003 check, correctly not adopting the "
             "2025 edition. Two documentation items remain: the PDF is a duplicated "
             "concatenation of the same report (about 58 MB), and the comment sheet records "
             "the replies without reproducing ADASA's original comment text. Itemised in "
             "P22-CD-09-005-001_B_Structural_Calc_CC_ADASA.pdf.",),
        ],
        action_paras=[
            [("Action — approved as noted, no new revision required:", {"bold": True}),
             (" issue a single, non-duplicated report file, and complete the comment sheet "
              "with ADASA's original comment text alongside each reply (NOTE-01 and NOTE-02 "
              "on the annotated PDF). The seismic calculation itself is accepted.",)],
        ],
    ),
    dict(
        heading="PLC/LCP Outline Panel Drawing Rev 0 — P22-CD-09-008-001",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Rev 0, issued for construction, closes the enclosure gate. It incorporates "
             "the RFI 25007-RO-RFI-0002 disposition in full: external body, door, roof, "
             "rear panel, plinth and gland plates in Stainless Steel 316L, internal "
             "mounting components in galvanized or cold-rolled steel, and NEMA 4X / IP66; "
             "and it closes the three minor items from Transmittal N27 (the cable-clamp "
             "sizes are stated, the communication gateway is labelled Ethernet/IP to "
             "Modbus TCP, and the cable-entry label is corrected). The Single Line Diagram "
             "has been re-issued to Rev 1 (\"SS316L Panel, NEMA 4X / IP66\"), closing the "
             "cross-document commitment carried since Transmittal N27. Two cosmetic "
             "inconsistencies remain and do not affect the drawing content: the \"Issued "
             "for Approval\" status stamp persists on a drawing revision-blocked as Rev 0 "
             "for construction, and the mounting-plate finish is described as zinc-plated "
             "on one sheet and hot-dip galvanized on another.",),
        ],
        action_paras=[
            [("Action: none on this document — accepted; issue at IFC Rev 0.", {"bold": True}),
             (" The two cosmetic labels (the status stamp and the plate-finish wording) may "
              "be tidied at the next natural issue; they do not affect construction. The "
              "related cross-document deliverable, the Single Line Diagram Rev 1, is already "
              "issued.",)],
        ],
    ),
    dict(
        heading="Line List Rev 0 — P22-LI-09-009-003",
        code="Response Code: 1 — Approved",
        status=[
            ("Status.", {"bold": True}),
            (" Rev 0, issued for construction, adds a hydrotest-pressure column at 1.5 "
             "times design and is consistent internally and with the P&ID Rev D and the "
             "Valve List Rev D. The one substantive change from the approved Rev C, the "
             "design pressure of the RO brine discharge line DA-PVC-DN65-09-016 reduced "
             "from 50 to 2 bar, is technically correct and verified against the P&ID Rev D: "
             "the line is PVC, downstream of the feed turbocharger, discharging brine to "
             "drain at near-atmospheric pressure, while the 50 bar belongs to the Super "
             "Duplex turbocharger lines. This correction was not declared in the comment "
             "sheet.",),
        ],
        action_paras=[
            [("Action: none on this document — accepted; issue at IFC Rev 0.", {"bold": True}),
             (" Please record the design-pressure correction on line DA-PVC-DN65-09-016 "
              "(50 to 2 bar) in the revision history, so the change from the approved Rev C "
              "is traceable.",)],
        ],
    ),
]

PENDING_OPEN = [
    ("TM N28",
     "Control family (Plant Control Philosophy Rev E, Alarm and Interlock List Rev C, "
     "Control and Sequence Chart Rev A)",
     "Each is correct in the content it governs, but the three disagree on tags and "
     "setpoints (winding/bearing sensor mapping and the RO HP pump vibration trip) that "
     "must align to the governing document",
     "OPEN: re-issue as a coordinated set at Rev 0 (target 31 July)"),
    ("TM N27",
     "Operating and Maintenance Manual (P22-BA-09-000-012 Rev A)",
     "Its control sequence, setpoints and HMI content are governed by the Control family "
     "and cannot close until that family issues at Rev 0 and the HMI Screenshots issue",
     "OPEN: re-issue as Rev B once the Control family closes"),
    ("TM N4",
     "HMI Screenshots (P22-LI-09-008-016 Rev A)",
     "The last undelivered control child; still incomplete, and it gates the Operating "
     "and Maintenance Manual",
     "OPEN: re-issue complete"),
]

PENDING_SUMMARY = (
    "the Equipment Layout Rev C (Code 3, RO cartridge filter still drawn horizontal; Rev "
    "D pending); the GA of the Antiscalant Dosing Tank Rev C; and the FAT Procedure "
    "(P22-PP-09-000-001) RTD protection sign-off, held from Transmittal N27 until the "
    "Plant Control Philosophy Rev 0 restores the winding and bearing mapping."
)

CROSS_DOC = (
    "the Single Line Diagram Rev 1 (\"SS316L Panel, NEMA 4X/IP66\") is now issued, closing "
    "the commitment carried on the Outline comment sheet since Transmittal N27; the "
    "container base-bolt interface remains an input to the OOCC foundation."
)

ATTACHMENTS = [
    ("HP and LP Pressure Test Procedure Rev D", "Code 2",
     "P22-BA-09-000-010_D_HP_LP_Pressure_Test_CC_ADASA.pdf", "NOTE-01"),
    ("UHPRO Structural Calculation Report Rev B", "Code 2",
     "P22-CD-09-005-001_B_Structural_Calc_CC_ADASA.pdf", "NOTE-01, NOTE-02"),
]

RESPONSE_SUMMARY = [
    ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "D",
     "2 — Approved as Noted"),
    ("P22-CD-09-005-001", "UHPRO Structural Calculation Report", "B",
     "2 — Approved as Noted"),
    ("P22-CD-09-008-001", "PLC/LCP Outline Panel Drawing", "0", "1 — Approved"),
    ("P22-LI-09-009-003", "Line List", "0", "1 — Approved"),
]


def main() -> None:
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: DOWNLOAD_LINK sin definir — reemplazar antes de emitir.")

    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N29 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-029-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 2 — Approved as Noted.", {"bold": True}),
        (" Four documents (submittal 25007-0067), all re-submittals. Tally: 2 Code 2, 2 "
         "Code 1.",),
    ])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    add_bullet(doc,
               "HP and LP Pressure Test Procedure Rev D — Code 2. State the applicable "
               "ASME Section V and B31.3 edition and addenda.")
    add_bullet(doc,
               "UHPRO Structural Calculation Report Rev B — Code 2. Issue a single, "
               "non-duplicated report file and complete the comment sheet.")
    add_bullet(doc,
               "PLC/LCP Outline Panel Drawing Rev 0 — Code 1. Issue at IFC Rev 0; tidy two "
               "cosmetic labels at the next issue.")
    add_bullet(doc,
               "Line List Rev 0 — Code 1. Record the DA-PVC-DN65-09-016 design-pressure "
               "correction in the revision history.")
    add_para(doc, [
        ("Why Approved as Noted — the two recoveries:", {"bold": True}),
        (" the two documents returned Code 3 in Transmittals N26 and N27 are now resolved "
         "and verified. The HP and LP Pressure Test Procedure sets the test pressure per "
         "line and material: the PVC brine discharge line is corrected from a rupturing 75 "
         "bar to a 3 bar hydrotest, and the 135 bar test is confined to the Super Duplex "
         "lines. The UHPRO Structural Calculation now carries the NCh 2369:2003 base-shear "
         "check (Zone 3, operating base shear 41.62 kN) and a governing skid utilization of "
         "0.454, below the 1.0 limit, and correctly does not adopt the 2025 edition. The "
         "residuals on both are editorial and documentation items, incorporated at the "
         "next issue with no new revision cycle. The Outline Panel Drawing and the Line "
         "List issue at IFC Rev 0: the Outline incorporates the RFI 25007-RO-RFI-0002 "
         "enclosure disposition in full and the Line List is consistent with the P&ID Rev "
         "D.",),
    ])
    add_para(doc, [
        ("Section 3 lists the pending observations from previous transmittals.",)])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        add_para(doc, sec["status"])
        for ap in sec["action_paras"]:
            add_para(doc, ap)

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [("The three most serious open items:", {"bold": True})])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [("Also open: ", {"bold": True}), (PENDING_SUMMARY,)])
    add_para(doc, [("Cross-document deliverables: ", {"bold": True}), (CROSS_DOC,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)
    add_para(doc, [(
        "The two Code 2 documents carry annotated PDFs. The two Code 1 documents (the "
        "Outline Panel Drawing Rev 0 and the Line List Rev 0) are approved and carry no "
        "annotated PDF.",)])
    dl = doc.add_paragraph()
    dl.add_run("Download — this transmittal and the annotated PDFs: ").bold = True
    aplicar_arial_12(dl)
    add_hyperlink(dl, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 2 — APPROVED AS NOTED.", {"bold": True}),
        (" Tally: 2 Code 2, 2 Code 1. This is a recovery transmittal: the two documents "
         "held at Code 3 (the HP and LP Pressure Test Procedure and the UHPRO Structural "
         "Calculation Report) are resolved and verified, and the Outline Panel Drawing and "
         "Line List are received at IFC Rev 0. Residuals are editorial and documentation "
         "items to incorporate at the next issue, with no new revision cycle. Documents "
         "not appearing in this response are unaffected by this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
