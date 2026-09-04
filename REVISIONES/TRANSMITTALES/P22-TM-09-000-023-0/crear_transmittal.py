#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N23 ADASA-BW_WATER (version EJECUTIVA).
Submittals 25007-0051 (E51) + 25007-0052 (E52). Fecha emision: 18-Jun-2026.

Veredicto global: 3 - TO BE REVISED. Tally: 0 Code 1 + 1 Code 2 + 6 Code 3.
Driver: RO Vessel Hydrostatic Test Procedure Rev A (45,5 bar en el form vs los
1.980 psi del waiver/ITP). El ITP Rev C cierra materialmente el item de
fabricacion mas antiguo.

Formato ejecutivo: Section 1 con TABLA de disposicion (Documento/Codigo/Why/Path);
Section 2 lean (Status de 1 frase + tabla OBS con topics recortados + Action de
1 bloque). Hallazgos, IDs/conteo OBS-NOTE (1:1 con CC_ADASA), severidades,
veredictos y tally IDENTICOS a la version densa (respaldada en
*_TRANSMITTAL_detailed.bak.md).

Fuente unica de contenido: P22-TM-09-000-023-0_TRANSMITTAL.md.
Numeracion: SIN numeros manuales en add_heading() - el template ADASA
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N23 ADASA-BW_WATER.docx")


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
# Section 2 content (lean). heading, code, status[], obs[(id,sev,topic)], action[]
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="Inspection and Test Plan Rev C — P22-BA-09-000-004",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Materially closes the package's oldest open fabrication item:"
             "the waiver basis (1,800 psi x 1.1 vessel test, ADASA witness, "
             "dossier hold points) is captured; two edits fold into Rev 0. "
             "Annotations on P22-BA-09-000-004_C_ITP_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Row 2.2 reads only \"Manufacture to ASME X\"; it does not state "
             "the no-code-stamp basis (the negotiated waiver) in the document "
             "that governs acceptance and the 40 percent payment milestone"),
            ("OBS-02", "MAJOR",
             "The RO Vessel hydrostatic test (row 2.2) is coded Witness while "
             "the high-pressure system test (row 5.2) is a Hold Point; the "
             "vessel test should be a Hold Point"),
            ("NOTE-01", "NOTE",
             "The waiver basis is captured for the first time (rows 2.2, 2.4, "
             "7.6, 8.3); ASME Section X is correct for the FRP vessels; the "
             "stamp remains waived and is not reopened"),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new revision required:",
              {"bold": True}),
             (" declare the no-code-stamp basis in row 2.2 (ASME Section X "
              "without stamp per the 02-Jun-2026 waiver; hydrostatic 1,800 psi "
              "x 1.1, ADASA witness, dossier per rows 7.6 and 8.3) (OBS-01); "
              "raise the vessel test from Witness to Hold Point, consistent "
              "with row 5.2 (OBS-02). Accepted as noted; full closure also "
              "depends on the RO Vessel Hydrostatic Test Procedure "
              "(Section 2.2).",)],
        ],
    ),
    dict(
        heading="RO Vessel Hydrostatic Test Procedure Rev A — P22-BA-09-000-009",
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" The procedure that supports the Inspection and Test Plan "
             "undercuts it: no binding test pressure in the body and a 45.5 bar "
             "value on the report form, against the required 1,980 psi. "
             "Annotations on "
             "P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure_"
             "CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "CRITICAL",
             "No binding test pressure in the body (only a generic 1.1x ASME / "
             "1.43x CE rule), and the report form carries 45.5 bar (about 660 "
             "psi) against the 1,980 psi the Inspection and Test Plan and the "
             "waiver require; the CE 1.43x branch opens an unagreed "
             "certification path"),
            ("OBS-02", "MAJOR",
             "No ADASA witness or notification section, and instrumentation is "
             "a single calibrated gauge without certificate review (the HP and "
             "LP procedure requires QC certificate review and two gauges)"),
            ("OBS-03", "MINOR",
             "Hold time stated as at least one minute and ASME Section X RT-5 "
             "cited without its hold-time and pressure-drop values"),
            ("OBS-04", "MINOR",
             "The ADASA wrapper (Rev A) and the embedded Protec procedure "
             "(Rev 0, 09-10-2025) revisions are not tied"),
        ],
        action_paras=[
            [("Action — re-issue as Rev B:", {"bold": True}),
             (" state the project test value by model (BPV-8-1800-SP-7 = 1,980 "
              "psi; BPV-8-1200-SP-7 = 1,320 psi) on the body and the report "
              "form and delete the 45.5 bar default and the CE branch (OBS-01); "
              "add a witness and notification section and traceable "
              "instrumentation (OBS-02); declare the RT-5 hold time and "
              "criterion (OBS-03); tie the wrapper to the vendor revision "
              "(OBS-04).",)],
        ],
    ),
    dict(
        heading=("HP and LP Pressure Test Procedure Rev A — "
                 "P22-BA-09-000-010"),
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" The methodology is complete, but the procedure states no binding "
             "numeric test pressure and the high-pressure design pressure (90 "
             "versus up to 120 bar) is unreconciled. Annotations on "
             "P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "No numeric test pressure or ASME B31.3 factor stated (only a "
             "generic the required test pressure); the Inspection and Test Plan "
             "fixes 135 bar (high-pressure) and 7.5 bar (low-pressure), and the "
             "high-pressure design pressure (90 bar in the Inspection and Test "
             "Plan versus up to 120 bar in the Technical Specification) is "
             "unreconciled"),
            ("OBS-02", "MINOR",
             "The step numbering breaks in the pneumatic section (after 5.6.16 "
             "it reverts to 5.5.17 and 5.5.18; step 5.6.5 is missing)"),
        ],
        action_paras=[
            [("Action — re-issue as Rev B:", {"bold": True}),
             (" declare the design pressure per subsystem, the B31.3 factor and "
              "the resulting test pressure (135 bar and 7.5 bar) matching the "
              "Inspection and Test Plan, and reconcile the high-pressure design "
              "pressure with a cited source (OBS-01); renumber the pneumatic "
              "section (OBS-02).",)],
        ],
    ),
    dict(
        heading="NDE Plan Rev B — P22-BA-09-000-005",
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" The coverage is sound and matches the Technical Specification, "
             "but the governing code editions are still placeholders (the Rev A "
             "comment was not closed) and codes are mixed across joints. "
             "Annotations on P22-BA-09-000-005_B_NDE_Plan_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Every referenced code (ASME Section V Article 9, ASME Section II, "
             "ASME B31.3, AWS D1.1, DVS 2202-1) is listed without a controlling "
             "year; the Rev A comment on this point was not closed in Rev B"),
            ("OBS-02", "MINOR",
             "The acceptance criteria mix AWS D1.1 and DVS 2202-1 with the "
             "high-pressure Super Duplex circuit governed by ASME B31.3 without "
             "mapping each code to its joints; the UT column is a baseline "
             "thickness measurement, not a weld-NDE extent"),
        ],
        action_paras=[
            [("Action — re-issue as Rev C:", {"bold": True}),
             (" state the governing year and addenda for each code (OBS-01); "
              "map each code to its joints (ASME B31.3 for the high-pressure "
              "Super Duplex circuit, AWS D1.1 for the support structure, DVS "
              "2202-1 for the low-pressure thermoplastic joints), clarify the "
              "UT thickness column, and cite the B31.3 acceptance paragraph and "
              "fluid-service category (OBS-02).",)],
        ],
    ),
    dict(
        heading="Painting Procedure Rev A — P22-BA-09-000-011",
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" The layer architecture (80 / 200 / 75 = 355 micrometres, Sa "
             "2½) matches the Technical Specification, but the approved coating "
             "system is swapped without an equivalence justification and the "
             "marine C5-M durability is not demonstrated. Annotations on "
             "P22-BA-09-000-011_A_Painting_Procedure_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "A Jotun system replaces the Sherwin-Williams system fixed in the "
             "Painting Specifications Rev B (approved Code 1 at Transmittal "
             "N11) with no product-to-product equivalence justification"),
            ("OBS-02", "MAJOR",
             "Marine durability not demonstrated: the primer is certified for "
             "C5-I (industrial), not the C5-M (marine) the coastal site and the "
             "Technical Specification require"),
            ("OBS-03", "MAJOR",
             "The anchor profile is contradictory and below the Technical "
             "Specification: the body fixes 50 to 80 micrometres while the "
             "inspection form fixes 40 to 75 micrometres, the 40 micrometre "
             "bound below the 50 micrometre minimum"),
            ("OBS-04", "MINOR",
             "The finish colour RAL 5012 required by the Technical "
             "Specification is not stated in the scheme or the inspection "
             "form"),
            ("OBS-05", "MINOR",
             "The scope is not bounded to the ASTM A-36 carbon steel and does "
             "not exclude stainless steel and non-metallic surfaces (FRP, "
             "HDPE) from painting"),
            ("OBS-06", "MINOR",
             "The quality control lacks an adhesion test, the nominal DFT per "
             "coat in the inspection form, the ISO 2808 measurement method and "
             "the SSPC-SP10 / NACE No. 2 reference"),
            ("NOTE-01", "NOTE",
             "The 80 / 200 / 75 = 355 micrometre architecture and the Sa 2½ "
             "preparation match the Technical Specification and the approved "
             "Painting Specifications Rev B; the scheme concept is sound and "
             "recoverable by revision"),
        ],
        action_paras=[
            [("Action — re-issue as Rev B:", {"bold": True}),
             (" provide a product-to-product equivalence table and ADASA's "
              "approval of the Jotun system, or adopt the Sherwin-Williams "
              "system, reconciling the two documents (OBS-01); demonstrate "
              "C5-M high durability per ISO 12944-6 (OBS-02); unify the anchor "
              "profile to a single range with a lower bound of at least 50 "
              "micrometres (OBS-03); state the RAL 5012 finish colour (OBS-04); "
              "bound the scope to the ASTM A-36 carbon steel and exclude "
              "stainless steel and non-metallic surfaces (OBS-05); and complete "
              "the quality control with an adhesion test, the nominal DFT per "
              "coat, and the ISO 2808 and SSPC-SP10 references (OBS-06).",)],
        ],
    ),
    dict(
        heading="Instrument Location Layout Rev C — P22-DWG-09-008-001",
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" Rev C was re-used for changed content without bumping the "
             "revision letter, and its geometry is tied to a superseded "
             "Equipment Layout that is itself open at Code 3. Annotations on "
             "P22-DWG-09-008-001_C_Instrument_Location_Layout_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "Re-issued on 16-Jun-2026 with content changes (items 8, 9, 31 and "
             "32 and the CIP relocation) but the revision letter stays C with "
             "no new revision-history row, so two drawings share the identifier "
             "Rev C"),
            ("OBS-02", "MAJOR",
             "The geometry is aligned to the superseded Equipment Layout Rev B, "
             "open at Code 3 (RO Cartridge Filter still horizontal); BW Water "
             "concedes it cannot be issued for construction until the upstream "
             "layouts are approved"),
            ("OBS-03", "MINOR",
             "The front title-block code reads P22-DWG-09-008-01 (two-digit "
             "correlative) versus the three-digit P22-DWG-09-008-001 in the "
             "file name and the sheet cajetin"),
            ("OBS-04", "MINOR",
             "Rev C carries two issue dates: the front header dates it "
             "16/6/2026 and the revision block dates it in April"),
        ],
        action_paras=[
            [("Action — re-issue as Rev D:", {"bold": True}),
             (" add a Rev D revision-history row for the content changes "
              "instead of re-using the C identifier (OBS-01); re-align the "
              "instrument positions once the Equipment Layout is resolved to "
              "Code 1 or 2 with the RO Cartridge Filter shown vertical "
              "(OBS-02); correct the front title-block code (OBS-03); and set "
              "one consistent issue date (OBS-04).",)],
        ],
    ),
    dict(
        heading=("UHPRO Structural Design Criteria Rev A — "
                 "P22-CD-09-005-003"),
        code="Response Code: 3 — To be revised",
        status=[
            ("Status.", {"bold": True}),
            (" The seismic parameter values are correct for NCh 2369 Of.2003 "
             "(the Technical Specification edition), but the criteria omit the "
             "lifting load case and yoke design criteria the module Technical "
             "Specification requires, and the seismic standard is cited "
             "inconsistently. Annotations on "
             "P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria_"
             "CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "The parameter table and the load combinations cite a non-existent "
             "NCh 2369:2009 while the code list correctly cites NCh 2369 "
             "Of.2003, the edition the Technical Specification establishes; "
             "align every citation to Of.2003 (the values are already "
             "consistent with it)"),
            ("OBS-02", "MAJOR",
             "For allowable-stress design the governing seismic combinations "
             "are NCh 2369 Of.2003 clause 4.5 (the document's combinations 11 "
             "and 12); confirm these govern (the generic NCh 3171 combinations "
             "do not replace them) and correct the edition citation"),
            ("OBS-03", "MAJOR",
             "No lifting (transport and erection) load case or lifting-point "
             "and yoke design criteria, which the module Technical "
             "Specification requires as a deliverable (the lifting design is BW "
             "Water's scope; the crane and lifting equipment are ADASA's)"),
            ("OBS-04", "MINOR",
             "The revision identity is contradictory: the ADASA block reads "
             "Rev A (17-Jun) while the internal block reads Rev 00 / FOR "
             "APPROVAL (16-Jun), opposite lifecycle stages"),
            ("OBS-05", "MINOR",
             "Soil Type E is adopted without a cited site geotechnical basis; "
             "state it as a conservative envelope pending the geotechnical "
             "report"),
            ("OBS-06", "MINOR",
             "The design seismic weight P is not declared nor cross-referenced "
             "to the established operating weight"),
            ("OBS-07", "MINOR",
             "The minimum wind pressures are written in N/m where the correct "
             "unit is N/m2; confirm the NCh 432 edition cited"),
            ("NOTE-01", "NOTE",
             "The concrete grade label (NCh1170 / G25, f'c = 24.5 MPa) is to be "
             "confirmed (the Chilean standard is normally NCh 170 and a G25 "
             "grade is about 25 MPa); foundation/civil scope, marginal to the "
             "steel skid"),
        ],
        action_paras=[
            [("Action — re-issue as Rev B:", {"bold": True}),
             (" add the lifting and handling load case and the lifting-point "
              "and yoke design criteria, including the dynamic amplification "
              "factor (OBS-03); align every NCh 2369:2009 citation to NCh 2369 "
              "Of.2003 (OBS-01) and confirm the Of.2003 clause 4.5 combinations "
              "govern the seismic allowable-stress verification (OBS-02); "
              "reconcile the revision identity (OBS-04); state Soil Type E as a "
              "conservative envelope pending the geotechnical report (OBS-05); "
              "declare the design seismic weight P (OBS-06); correct the "
              "wind-pressure units to N/m2 and confirm the NCh 432 edition "
              "(OBS-07); and confirm the concrete standard label and grade "
              "(NOTE-01).",)],
        ],
    ),
]


# Section 3 — open items not re-submitted in this package.
ADDRESSED_TEXT = (
    "Transmittal N19 Section 2.10 / Transmittal N22 Section 3 (the Inspection "
    "and Test Plan and the vessel test procedures, the oldest open "
    "fabrication item) is materially closed by the Inspection and Test Plan "
    "Rev C, which now carries the vessel hydrostatic test at 1,800 psi x 1.1, "
    "the ADASA witness and the dossier Hold Points. Full closure remains "
    "subject to the two Rev 0 edits in the Inspection and Test Plan "
    "(Section 2.1) and the correction of the RO Vessel Hydrostatic Test "
    "Procedure (Section 2.2); the ASME stamp remains waived and is not "
    "reopened."
)

PENDING_OPEN = [
    ("TM N22 Section 2.1",
     "Plant Control Philosophy children: Operating Sequence Charts "
     "(P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) "
     "and Control Matrix, with the I/O List Rev 2 and the rest of the control "
     "cascade",
     "The operative numerical control logic remains in child documents not "
     "delivered",
     "OPEN: not delivered with this submittal; the sixth cycle with that "
     "logic outside the package"),
    ("TM N20 Section 2.6",
     "PLC-LCP Outline Panel Drawing (P22-CD-09-008-001)",
     "Enclosure contradiction (sheet steel / IP55 versus SS316L / NEMA "
     "4X-IP66) — fabrication gate",
     "OPEN: Outline Rev B with the aligned Panel Specification Sheet, actual "
     "panel weight and reconciled cooling awaited; the expedited release path "
     "of the 10-Jun response applies"),
    ("TM N22 Section 2.2",
     "Equipment Layout (P22-DWG-09-005-003)",
     "RO Cartridge Filter still drawn horizontal against its own vertical "
     "datasheet",
     "OPEN: to re-issue as Rev D with the RO Cartridge Filter vertical; this "
     "also gates the Instrument Location Layout (Section 2.6 OBS-02)"),
]

PENDING_PROCEDURAL = [
    "Grounding Point and Power Panel Location Layout Rev F, due 17-Jun-2026; "
    "not received with this submittal; tracked.",
    "FAT and SAT comparison table (due 15-Jun-2026): the FAT scope is "
    "captured in the Inspection and Test Plan (item 7), but the standalone "
    "comparison table is still tracked.",
    "Inspection and Test Plan Rev 0 conditions and RO Vessel Hydrostatic Test "
    "Procedure alignment (Sections 2.1 and 2.2) close the fabrication "
    "carry-forward in full.",
]


ATTACHMENTS = [
    ("Inspection and Test Plan Rev C", "Code 2",
     "P22-BA-09-000-004_C_ITP_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
    ("RO Vessel Hydrostatic Test Procedure Rev A", "Code 3",
     "P22-BA-09-000-009_A_RO_Vessel_Hydrostatic_Test_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, OBS-04"),
    ("HP and LP Pressure Test Procedure Rev A", "Code 3",
     "P22-BA-09-000-010_A_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02"),
    ("NDE Plan Rev B", "Code 3",
     "P22-BA-09-000-005_B_NDE_Plan_CC_ADASA.pdf",
     "OBS-01, OBS-02"),
    ("Painting Procedure Rev A", "Code 3",
     "P22-BA-09-000-011_A_Painting_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, OBS-06, NOTE-01"),
    ("Instrument Location Layout Rev C", "Code 3",
     "P22-DWG-09-008-001_C_Instrument_Location_Layout_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, OBS-04"),
    ("UHPRO Structural Design Criteria Rev A", "Code 3",
     "P22-CD-09-005-003_A_UHPRO_Structural_Design_Criteria_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, OBS-06, OBS-07, NOTE-01"),
]


RESPONSE_SUMMARY = [
    ("P22-BA-09-000-004", "Inspection and Test Plan", "C",
     "2 — Approved as Noted"),
    ("P22-BA-09-000-009", "RO Vessel Hydrostatic Test Procedure", "A",
     "3 — To Be Revised"),
    ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "A",
     "3 — To Be Revised"),
    ("P22-BA-09-000-005", "NDE Plan", "B", "3 — To Be Revised"),
    ("P22-BA-09-000-011", "Painting Procedure", "A", "3 — To Be Revised"),
    ("P22-DWG-09-008-001", "Instrument Location Layout", "C",
     "3 — To Be Revised"),
    ("P22-CD-09-005-003", "UHPRO Structural Design Criteria", "A",
     "3 — To Be Revised"),
]


def main() -> None:
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N23 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-023-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # =========================================================================
    # 1. EXECUTIVE SUMMARY
    # =========================================================================
    doc.add_heading("EXECUTIVE SUMMARY", level=1)

    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To Be Revised.", {"bold": True}),
        (" Seven documents (submittals 25007-0051 and 25007-0052). Tally: 0 "
         "Code 1, 1 Code 2, 6 Code 3. Driver: the RO Vessel Hydrostatic Test "
         "Procedure, whose report form carries 45.5 bar against the 1,980 psi"
         "(1,800 x 1.1) the ASME-waiver basis and the Inspection and Test Plan "
         "require. The per-document codes, observations and required actions "
         "are set out in Section 2; open items from previous transmittals are "
         "inventoried in Section 3.",),
    ])

    # =========================================================================
    # 2. OBSERVATIONS BY DOCUMENT
    # =========================================================================
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

    # =========================================================================
    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    # =========================================================================
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)

    add_para(doc, [(
        "This submittal delivered E51 and E52 only.",)])

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

    # =========================================================================
    # 4. ATTACHMENTS
    # =========================================================================
    doc.add_heading("ATTACHMENTS", level=1)

    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)

    add_para(doc, [(
        "All seven documents carry open observations or notes and are returned "
        "with annotated PDFs (6 Code 3 + 1 Code 2). No document is Code 1 — "
        "Approved in this transmittal.",)])

    # =========================================================================
    # 5. RESPONSE SUMMARY
    # =========================================================================
    doc.add_heading("RESPONSE SUMMARY", level=1)

    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)

    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.", {"bold": True}),
        (" Tally: 0 Code 1, 1 Code 2, 6 Code 3. The per-document codes, drivers "
         "and required actions are set out in Section 1 (Disposition) and "
         "Section 2; the RO Vessel Hydrostatic Test Procedure fixes the "
         "verdict. Documents not appearing in this response are unaffected by "
         "this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
