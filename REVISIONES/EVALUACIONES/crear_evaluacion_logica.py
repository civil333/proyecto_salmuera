#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento ADASA de evaluacion comparativa logica de control.
Fecha: 28 de febrero de 2026
Codigo: P22-IT-06-000-004-0
Titulo: CONTROL LOGIC REVIEW — P22-IT-06-008-101-B Rev B vs P13 Benchmark (2019)
"""

import sys
import os

skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt

OUTPUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "P22-IT-06-000-004-0_Evaluacion-Logica-Control_ADASA.docx",
)


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def crear_documento():
    crear_documento_adasa(
        titulo="CONTROL LOGIC REVIEW: P22-IT-06-008-101-B Rev B vs P13-IT-03-008-001-0 (2019 BENCHMARK)",
        codigo="P22-IT-06-000-004-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # Eliminar contenido placeholder
    elementos_a_eliminar = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos_a_eliminar.append(para)
    for para in elementos_a_eliminar:
        p = para._element
        p.getparent().remove(p)

    # ============================================================
    # 1. PURPOSE AND SCOPE
    # ============================================================
    doc.add_heading("PURPOSE AND SCOPE", level=1)

    add_para(
        doc,
        "This document presents a comparative review of the Control Logic Description "
        "P22-IT-06-008-101-B (Rev B, 22-Feb-2026, Van Doorn) for the Second Stage Brine Module "
        "against the equivalent document P13-IT-03-008-001-0 (2019) used for Module 3. The 2019 "
        "document is used as the measurement benchmark because it was the document that "
        "successfully enabled PLC programming, plant commissioning, and coordination with the "
        "external supplier (Osmoflo) for Module 3.",
    )
    add_para(
        doc,
        "The objective of this review is to identify gaps in the current document before BW Water "
        "advances in PLC programming, preventing costly reprogramming cycles and ambiguities "
        "during commissioning.",
    )
    add_para(
        doc,
        "This document is ADASA internal. It supports the formal technical query P22-CT-06-000-001-0 "
        "directed to Van Doorn requesting a Rev C of P22-IT-06-008-101-B.",
    )

    # ============================================================
    # 2. REFERENCE DOCUMENTS
    # ============================================================
    doc.add_heading("REFERENCE DOCUMENTS", level=1)

    add_simple_table(doc, [
        ("#", "Code", "Document", "Rev", "Role"),
        ("1", "P22-IT-06-008-101-B",
         "Descriptivo L\u00f3gica de Control \u2014 M\u00f3dulo 2da Etapa Salmuera",
         "B (22-Feb-2026)",
         "Document under review"),
        ("2", "P13-IT-03-008-001-0",
         "Descriptivo L\u00f3gica de Control \u2014 M\u00f3dulo 3 (Taltal)",
         "0 (2019)",
         "Benchmark \u2014 successfully implemented"),
        ("3", "P22-CT-06-000-001-0",
         "Technical Query to Van Doorn \u2014 Control Logic Gaps",
         "0",
         "Formal action document derived from this review"),
    ])

    # ============================================================
    # 3. STRUCTURAL COMPARISON
    # ============================================================
    doc.add_heading("STRUCTURAL COMPARISON", level=1)

    add_para(
        doc,
        "The following table presents a quantitative comparison of both documents. The P13 "
        "metrics are derived from the 2019 implementation document; the P22 metrics from the "
        "current Rev B. The difference in depth is not attributable to a simpler process: the "
        "Second Stage module processes brine reject from an existing RO plant, which requires "
        "equally precise control logic for safe and reliable operation.",
    )

    add_simple_table(doc, [
        ("Metric", "P13 (2019 \u2014 Module 3)", "P22 (2026 \u2014 2nd Stage)", "Assessment"),
        ("Total paragraphs", "456", "235 (~50% fewer)", "Significant gap in depth"),
        ("Headings (sections)", "21", "15", "Missing subsections"),
        ("Process tables", "2 (revisions + level bands)", "1 (revisions only)", "Level bands absent"),
        ("Pretreatment subsections", "9 (filters, 5 dosing, pumps)", "2 (tank+pump, pit+submersible)", "Simplified; partly justified"),
        ("Post-treatment documented", "Yes \u2014 complete (5 systems)", "No \u2014 \u2018existing, not applicable\u2019", "Justified (independent PLC)"),
        ("Dosing formulas", "Yes \u2014 Q = flow \u00d7 dose / conc.", "No (dosing in BW Water scope)", "Justified (BW Water scope)"),
        ("Named control loops", "5+ (CTRL-DIS_001, CTRL_CO2_001\u2026)", "1 (CTRL_BH06_001)", "Gap \u2014 loop incomplete"),
        ("Start-up sequence (steps)", "Yes \u2014 numbered steps post-permissives", "Partial \u2014 permissives without sequence", "Gap \u2014 sequence missing"),
        ("Shutdown sequence", "5 complete steps", "3 steps + tag error", "Gap \u2014 incomplete + error"),
        ("Level band table (TK)", "Yes \u2014 4 bands with thresholds", "No", "Gap \u2014 operational reference missing"),
        ("Inter-PLC signals documented", "5 signals named", "4 signals (partial)", "Gap \u2014 possible missing signal"),
        ("Author compliance (ADASA)", "Not applicable", "L. Hughes (not ADASA protocol)", "Administrative gap"),
    ])

    # ============================================================
    # 4. WHY THE 2019 DOCUMENT IS THE BENCHMARK
    # ============================================================
    doc.add_heading("WHY THE 2019 DOCUMENT IS THE MEASUREMENT BENCHMARK", level=1)

    add_para(
        doc,
        "The P13-IT-03-008-001-0 was not merely a design document \u2014 it was the document that "
        "directly enabled the following outcomes for Module 3:",
    )
    add_para(doc, "\u2022  PLC programming without ambiguity: each control loop has a name, formula, and operating range.")
    add_para(doc, "\u2022  Plant operation: the level band table gave operators a direct reference for normal and alarm conditions.")
    add_para(doc, "\u2022  Coordination with external supplier (Osmoflo): named inter-PLC signals prevented integration surprises.")
    add_para(doc, "\u2022  ISO 22000 safety interlock closure: hypochlorite and fluoride tanks had clear conditions.")
    add_para(
        doc,
        "The P22-IT-06-008-101-B Rev B may serve as a concept document, but it does not yet "
        "provide sufficient detail for PLC programming or commissioning without resolving the "
        "gaps identified in Section 5.",
    )

    # ============================================================
    # 5. GAP ANALYSIS
    # ============================================================
    doc.add_heading("GAP ANALYSIS", level=1)

    # GAP-01
    doc.add_heading("GAP-01 \u2014 Incomplete Start-up Sequence", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Major"),
        ("Section in P22 Rev B", "Start-up sequence / permissives"),
        ("P13 equivalent", "Section: numbered steps post-permissives"),
    ])

    add_para(
        doc,
        "The document lists 16 start-up permissives but does not describe the sequence of steps "
        "once permissives are verified. The following questions are unanswered:",
    )
    add_para(doc, "\u2022  When does BH-06-001 start and at what initial frequency?")
    add_para(doc, "\u2022  How long does the system wait to confirm pressure at PIT-06-001?")
    add_para(doc, "\u2022  What happens if the required pressure is not reached within that time?")
    add_para(doc, "\u2022  When is the start pulse OI-06-003 sent to BW Water?")
    add_para(doc, "\u2022  How does the ADASA PLC confirm that the OI is actually running (OI-06-004)?")
    add_para(doc, "\u2022  What is the timeout for OI start confirmation?")
    add_para(
        doc,
        "Without this step-by-step sequence, the BW Water PLC programmer cannot implement "
        "the correct interlock logic between ADASA\u2019s feeding system and the RO module.",
    )

    # GAP-02
    doc.add_heading("GAP-02 \u2014 Incomplete Shutdown Sequence + Tag Error", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Major"),
        ("Section in P22 Rev B", "Shutdown sequence (3 steps)"),
        ("P13 equivalent", "Shutdown sequence (5 steps)"),
    ])

    add_para(
        doc,
        "The document contains 3 shutdown steps with one confirmed tag error. Step 3 references "
        "\u201cParada Bomba de alimentaci\u00f3n BH-03-001\u201d \u2014 the tag BH-03 corresponds to Module 3 "
        "(the 2019 plant), not the Second Stage module. The correct tag should be BH-06-001.",
    )
    add_para(doc, "Additionally, the following items are missing from the shutdown sequence:")
    add_para(doc, "\u2022  Disposition of BS-06-001 (drainage submersible pump) during shutdown.")
    add_para(doc, "\u2022  State of manual valves VM-06-001 and VM-06-002 at end of shutdown.")
    add_para(doc, "\u2022  Final state of instrumented valves.")
    add_para(doc, "\u2022  Timeout logic if OI-06-004 does not confirm shutdown within expected time.")

    # GAP-03
    doc.add_heading("GAP-03 \u2014 No Level Band Table for TK-06-001", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Minor"),
        ("Section in P22 Rev B", "Level conditions \u2014 permissive only"),
        ("P13 equivalent", "Formal table: 4 bands with thresholds and activated equipment"),
    ])

    add_para(
        doc,
        "The document mentions \u201clevel greater than 70%\u201d as a start-up permissive and \u201clow level\u201d "
        "as an interlock, but does not provide a formal band table defining operational behavior "
        "of the storage tank throughout its full range. The P13 document provided 4 level bands "
        "with associated equipment states, giving both operators and the PLC programmer a "
        "complete reference.",
    )
    add_para(doc, "The following is not defined for TK-06-001:")
    add_para(doc, "\u2022  At what level is an alarm activated?")
    add_para(doc, "\u2022  What is the normal operating range (% min/max)?")
    add_para(doc, "\u2022  How is intentional overflow (~2%) managed?")

    # GAP-04
    doc.add_heading("GAP-04 \u2014 Post-Treatment Integration Not Documented", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Minor"),
        ("Section in P22 Rev B", "Post-treatment: \u2018existing, no action required\u2019"),
        ("P13 equivalent", "Full post-treatment documentation (5 systems)"),
    ])

    add_para(
        doc,
        "The statement that post-treatment \u201calready operates and requires no action from the new "
        "PLC\u201d is correct operationally. However, the following coordination aspects are "
        "not documented:",
    )
    add_para(doc, "\u2022  How does the operator know the new module is contributing 25 m\u00b3/h to the existing post-treatment?")
    add_para(doc, "\u2022  Is the TK-00-001 high level interlock the only coordination point with the existing system?")
    add_para(doc, "\u2022  Are there signals between the new ADASA PLC and the existing PLC, or only a shared physical tank?")
    add_para(
        doc,
        "This gap does not affect PLC programming for the new module, but creates operational "
        "ambiguity during commissioning if operators need to verify that production is reaching "
        "the post-treatment stage.",
    )

    # GAP-05
    doc.add_heading("GAP-05 \u2014 Control Loop BH-06-001 Without Complete Definition", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Minor"),
        ("Section in P22 Rev B", "CTRL_BH06_001 \u2014 maintains 3 bar in PIT-06-001"),
        ("P13 equivalent", "Full loop definition: type, range, fallback"),
    ])

    add_para(
        doc,
        "The document documents that CTRL_BH06_001 maintains 3 bar at PIT-06-001, which is "
        "the correct design objective. The following parameters required for PLC implementation "
        "are absent:",
    )
    add_para(doc, "\u2022  Control type: PI or PID?")
    add_para(doc, "\u2022  VFD frequency range: Hz minimum / maximum.")
    add_para(doc, "\u2022  Fallback behavior if PIT-06-001 fails (sensor fault mode).")
    add_para(doc, "\u2022  Start-up ramp profile for BH-06-001.")

    # GAP-06
    doc.add_heading("GAP-06 \u2014 Fault Alarm Signal and Restart Procedure Not Documented", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Minor"),
        ("Section in P22 Rev B", "4 signals listed; no fault restart procedure"),
        ("P13 equivalent", "4 signals in table + fault restart procedure documented"),
    ])

    add_para(
        doc,
        "Direct comparison of the P13 signal section against P22 Rev B clarifies this gap. "
        "The P13 (Osmoflo interface) listed 4 signals in its dedicated signal section: "
        "Start order, Stop order, Fault alarm, Local/remote. A fifth signal (OI-03-004, "
        "\u2018running\u2019) appeared only in the start-up and shutdown sequences, not in the signal table. "
        "The P22 lists 4 signals explicitly (OI-06-002, OI-06-003, OI-06-004, OI-06-005). "
        "The signal counts are therefore equivalent.",
    )
    add_para(
        doc,
        "The real gap has two parts:",
    )
    add_para(
        doc,
        "\u2022  The fault alarm signal equivalent to OI-03-003 (fault alarm from OI to ADASA PLC) "
        "is not listed in the P22 signal table. This signal triggers plant shutdown and must "
        "be documented with its tag, type (DI), and interlock behavior.",
    )
    add_para(
        doc,
        "\u2022  The restart procedure after a fault is not documented. The P13 explicitly stated: "
        "\u2018the fault condition must be normalized and the system reset via HMI before the plant "
        "can restart \u2014 no dedicated reset signal to the OI module is required.\u2019 The P22 "
        "contains no equivalent statement, leaving the programmer without a defined restart "
        "logic after a BW Water OI fault.",
    )

    # GAP-07
    doc.add_heading("GAP-07 \u2014 Authorship Does Not Comply with ADASA Protocol", level=2)

    add_simple_table(doc, [
        ("Field", "Value"),
        ("Severity", "Administrative"),
        ("Section in P22 Rev B", "Title block \u2014 Revisions A and B"),
        ("ADASA protocol", "Prepared/Reviewed: Luis Rivera | Approved: Victor Gutierrez"),
    ])

    add_para(
        doc,
        "Revisions A and B of P22-IT-06-008-101-B show Prepared/Reviewed/Approved = L. Hughes "
        "(same person for all fields). Per ADASA document control protocol (CLAUDE.md \u00a73.3), "
        "formal ADASA-coded documents must carry ADASA authorship. This document requires "
        "re-issuance with the correct ADASA authorship fields in Rev C.",
    )

    # ============================================================
    # 6. JUSTIFIED DIFFERENCES
    # ============================================================
    doc.add_heading("JUSTIFIED DIFFERENCES (NOT GAPS)", level=1)

    add_para(
        doc,
        "The following differences between P22 and P13 are structurally justified by the "
        "different process scope of each module and do not represent gaps:",
    )

    add_simple_table(doc, [
        ("Difference", "Justification"),
        ("No section for sea water intake wells / submersible extraction pumps",
         "The Second Stage module uses brine reject from existing RO \u2014 no sea water wells."),
        ("No self-cleaning filters",
         "Brine from RO is already filtered; cartridge filters are in BW Water scope."),
        ("No post-treatment dosing documentation (CO2, calcite, hypochlorite, fluoride)",
         "Post-treatment is an independent system with its own PLC \u2014 correct to exclude."),
        ("No dispersant documentation at ADASA PLC level",
         "BDS-06-001 is part of the BW Water module scope."),
        ("Fewer submersible pumps",
         "Different process: no sea water extraction; only drainage pit BS-06-001."),
    ])

    # ============================================================
    # 7. CONCLUSION AND REQUIRED ACTIONS
    # ============================================================
    doc.add_heading("CONCLUSION AND REQUIRED ACTIONS", level=1)

    add_para(
        doc,
        "P22-IT-06-008-101-B Rev B represents a competent concept-level control logic document "
        "that correctly identifies the main permissives, interlocks, and the BH-06-001 control "
        "objective. However, it does not yet reach the level of detail required for PLC "
        "programming or unambiguous commissioning.",
    )
    add_para(
        doc,
        "Two gaps are classified as Major (GAP-01, GAP-02): these directly affect the ability "
        "of BW Water\u2019s programmer to implement the correct start-up and shutdown sequences "
        "without additional verbal clarification. If left unresolved, they will generate "
        "programming rework after the first commissioning attempt.",
    )
    add_para(
        doc,
        "Four gaps are classified as Minor (GAP-03 through GAP-06): these affect operational "
        "completeness and documentation quality, but do not block programming if verbal "
        "coordination occurs. They should be resolved in the same revision to avoid propagating "
        "ambiguities to the operation manual and training materials.",
    )
    add_para(
        doc,
        "One gap is Administrative (GAP-07): authorship correction required for ADASA document "
        "control compliance.",
    )

    add_simple_table(doc, [
        ("Gap", "Severity", "Action Required", "Target"),
        ("GAP-01", "Major", "Add step-by-step start-up sequence after permissive verification", "Van Doorn \u2014 Rev C"),
        ("GAP-02", "Major", "Complete shutdown sequence; correct BH-03-001 \u2192 BH-06-001 tag error", "Van Doorn \u2014 Rev C"),
        ("GAP-03", "Minor", "Add level band table for TK-06-001 (4 bands minimum with thresholds)", "Van Doorn \u2014 Rev C"),
        ("GAP-04", "Minor", "Document TK-00-001 high level as coordination signal; confirm inter-PLC signals", "Van Doorn \u2014 Rev C"),
        ("GAP-05", "Minor", "Complete CTRL_BH06_001 definition: control type, VFD range, fallback, ramp", "Van Doorn \u2014 Rev C"),
        ("GAP-06", "Minor", "Add fault alarm signal (OI-06-00X equivalent) to signal list; document restart procedure after OI fault via HMI", "Van Doorn \u2014 Rev C"),
        ("GAP-07", "Admin", "Re-issue with ADASA authorship: Prepared/Reviewed: L. Rivera | Approved: V. Gutierrez", "Van Doorn \u2014 Rev C"),
    ])

    add_para(
        doc,
        "Formal action: Technical Query P22-CT-06-000-001-0 has been issued to Van Doorn "
        "requesting Rev C of P22-IT-06-008-101-B addressing all gaps above. Rev C is required "
        "before ADASA approves the control logic document and before BW Water initiates "
        "PLC programming for the Second Stage module.",
    )

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
