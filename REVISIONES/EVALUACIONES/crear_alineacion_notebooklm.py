#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar documento ADASA de alineacion NotebookLM vs documentos oficiales.
Fecha: 25 de febrero de 2026
Codigo: P22-IT-06-000-003-0
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
    "P22-IT-06-000-003-0_Alineacion-NotebookLM_ADASA.docx",
)


def add_para(doc, text, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    return para


def crear_documento():
    crear_documento_adasa(
        titulo="TECHNICAL DATA ALIGNMENT: NOTEBOOKLM VS OFFICIAL PROJECT DOCUMENTS",
        codigo="P22-IT-06-000-003-0",
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
        "This document presents a formal alignment verification between the technical data "
        "published in ADASA\u2019s NotebookLM knowledge base (Taltal Brine Module) and the "
        "official BW Water engineering deliverables approved or under review as of February 2026.",
    )
    add_para(
        doc,
        "The NotebookLM material covers the BiTurbo\u2122 RO module fabricated by BW Water Americas "
        "Inc. (Job 25007) for the Taltal desalination plant. It includes presentation scripts, "
        "video scripts, and technical notes derived from the Process Calculation Rev B, equipment "
        "datasheets, and related deliverables. The purpose of this cross-check is to:",
    )
    add_para(doc, "\u2022  Confirm that data used for internal training and communication is consistent with controlled engineering documents")
    add_para(doc, "\u2022  Identify specific discrepancies that require clarification or formal action from BW Water")
    add_para(
        doc,
        "\u2022  Document the evidence base for two open findings: TM N4 OBS-08 (HP Pump power) "
        "and TM N3 OBS-02 (SEC calculation)",
    )
    add_para(
        doc,
        "The scope covers all numerical data in the NotebookLM presentation script (Slides 1\u201316) "
        "and video script (equipment detail), cross-referenced against five official BW Water "
        "documents at their latest approved revision.",
    )

    # ============================================================
    # 2. SOURCE DOCUMENTS REFERENCED
    # ============================================================
    doc.add_heading("SOURCE DOCUMENTS REFERENCED", level=1)

    add_simple_table(doc, [
        ("#", "Code", "Document", "Revision", "Delivery", "Verdict", "Role"),
        ("1", "NOTEBOOK LM", "Script Presentacion Modulo RO BiTurbo\u2122", "\u2014", "Internal", "Reference", "Primary source of NotebookLM data"),
        ("2", "NOTEBOOK LM", "Script Video Modulo RO BiTurbo\u2122", "\u2014", "Internal", "Reference", "Supplementary equipment detail"),
        ("3", "P22-CD-09-009-001", "Process Calculation", "Rev B", "E7", "2-AN", "10 operating scenarios, permeate quality, recovery"),
        ("4", "P22-ET-09-009-002", "Datasheet RO HP Pump", "Rev B", "E7", "2-AN (TM N4)", "HP Pump performance, motor and VFD data"),
        ("5", "P22-ET-09-009-007", "Datasheet Feed Turbocharger", "Rev B", "E8", "Under review", "HPB-60 efficiencies, bypass, turbo case analysis"),
        ("6", "P22-IT-06-000-001-0", "Evaluation of BW Water Responses TM N3/N4", "Rev 0", "ADASA internal", "\u2014", "Open findings OBS-02, OBS-08"),
        ("7", "P22-IT-06-000-002-0", "Document Status Register", "Rev 0", "ADASA internal", "\u2014", "Document inventory context"),
    ])

    # ============================================================
    # 3. CRITICAL FINDINGS
    # ============================================================
    doc.add_heading("CRITICAL FINDINGS", level=1)

    # 3.1
    doc.add_heading("HP Pump Power \u2014 Four Values in Circulation", level=2)

    add_para(
        doc,
        "The HP Pump (BH-09-001, FEDCO MSD-7016) has four distinct power values appearing "
        "across the official project documents and the NotebookLM material. These are not "
        "errors \u2014 they describe four different physical quantities of the same equipment, "
        "each correct in its own context.",
    )

    add_simple_table(doc, [
        ("Value", "Source", "Physical Meaning", "Correct Use"),
        ("83.1 kW",
         "DS Rev B, Technical Proposal section (p.3) / NotebookLM Slide 6",
         "Absorbed shaft power at design point (49 m\u00b3/h, 53k TDS, 24\u00b0C)",
         "SEC calculation \u2014 energy consumed by the pump"),
        ("87 kW",
         "DS Rev B, Motor Data section",
         "Electric power input to motor (83.1 kW \u00f7 \u03b7_motor 0.95 \u2248 87.5 kW)",
         "Motor electrical sizing"),
        ("90 kW",
         "DS Rev B, Drive Data section",
         "Rated electric power of VFD (Siemens SINAMICS G120X 110 kW model)",
         "VFD electrical circuit sizing"),
        ("125 HP (93 kW)",
         "DS Rev B, Motor nameplate",
         "Nominal motor rating including 1.15 service factor",
         "Motor procurement and MCC sizing"),
    ])

    add_para(
        doc,
        "The problem identified in TM N4 OBS-08 is not that these values are contradictory, "
        "but that BW Water has not documented in which context each value applies. Without this "
        "clarification, engineers reviewing the datasheet, MCC schedule, or SEC table may apply "
        "the wrong value in each calculation.",
    )
    add_para(
        doc,
        "NotebookLM alignment: The script uses 83.1 kW (absorbed power) for the SEC calculation "
        "context and states the motor is 125 HP / 93 kW as nameplate. This is the correct "
        "distinction. The 87 kW and 90 kW values are not mentioned in the NotebookLM material "
        "\u2014 a gap that, while acceptable for a training presentation, confirms that BW Water "
        "has not provided a consolidated power table with usage guidance.",
    )
    add_para(
        doc,
        "Required action: BW Water must deliver a clarification note or revised datasheet table "
        "specifying the applicable context for each of the four power values. This is prerequisite "
        "to HP Pump procurement approval (TM N4 OBS-08, open 18 days as of February 25, 2026).",
    )

    # 3.2
    doc.add_heading("SEC Calculation \u2014 Three Values, One Reference Condition Missing", level=2)

    add_para(
        doc,
        "The Specific Energy Consumption (SEC) of the BiTurbo\u2122 system has three distinct "
        "values in the project, each associated with a different operational reference condition. "
        "The contractual guarantee does not specify which condition applies.",
    )

    add_simple_table(doc, [
        ("SEC Value", "Source", "Reference Condition", "Status"),
        ("3.98 kWh/m\u00b3",
         "BW Water commercial claim / NotebookLM Slide 16",
         "53,000 mg/L TDS, 19\u00b0C, Y0 \u2014 highest salinity, maximum turbo energy recovery",
         "Stated as meeting guarantee"),
        ("4.84 kWh/m\u00b3",
         "NotebookLM Slide 12",
         "43,000 mg/L TDS, 19\u00b0C, Y0 \u2014 minimum salinity, lower turbo energy recovery",
         "Exceeds guarantee by 2.8%"),
        ("4.88 kWh/m\u00b3",
         "NotebookLM Slide 12",
         "43,000 mg/L TDS, 19\u00b0C, Y1 \u2014 1 year membrane aging",
         "Exceeds guarantee by 3.6%"),
        ("5.09 kWh/m\u00b3",
         "NotebookLM Slide 12",
         "43,000 mg/L TDS, 19\u00b0C, Y5 \u2014 5 year membrane aging",
         "Exceeds guarantee by 8.1%"),
        ("\u22644.71 kWh/m\u00b3",
         "Contractual guarantee",
         "Reference condition not specified in Process Calc Rev B",
         "Benchmark"),
    ])

    add_para(
        doc,
        "The 3.98 kWh/m\u00b3 value corresponds to the most favorable operating condition (53k TDS), "
        "where brine rejection pressure is highest (~83 bar), allowing the two HPB-60 turbines to "
        "recover the most energy. At 43k TDS, brine pressure drops to ~60 bar, the Interstage "
        "Turbocharger opens its bypass valve (1.4\u20131.5 m\u00b3/h), and the turbines recover less "
        "energy \u2014 increasing the SEC.",
    )
    add_para(
        doc,
        "The critical gap: Process Calculation Rev B (P22-CD-09-009-001-B) does not contain a SEC "
        "table covering the 10 operating scenarios. The 3.98 kWh/m\u00b3 figure appears in BW Water\u2019s "
        "commercial materials but its basis was not documented in the formal calculation. ADASA "
        "cannot verify whether the guarantee condition is 53k TDS (where the claim is met) or 43k "
        "TDS (where it may not be met).",
    )
    add_para(
        doc,
        "NotebookLM alignment: The script correctly presents both values (3.98 and 4.84\u20135.09 "
        "kWh/m\u00b3) and flags the discrepancy against the 4.71 kWh/m\u00b3 guarantee. This alignment "
        "is correct. The concern is that the underlying formal document (Process Calc Rev B) does "
        "not contain this analysis.",
    )
    add_para(
        doc,
        "Required action: BW Water must deliver a SEC table covering all 10 operating scenarios "
        "as part of the Process Calculation revision. This is prerequisite to closing TM N3 OBS-02 "
        "(open 28 days as of February 25, 2026).",
    )

    # ============================================================
    # 4. CONFIRMED PARAMETERS
    # ============================================================
    doc.add_heading("CONFIRMED PARAMETERS", level=1)

    add_para(
        doc,
        "The following table lists all technical parameters verified in the NotebookLM material "
        "against their respective official source document. All entries are confirmed as consistent.",
    )

    add_simple_table(doc, [
        ("#", "Parameter", "NotebookLM Value", "Official Document", "Official Value", "Match"),
        ("1", "Feed Turbocharger (SIP-09-001) efficiency", "70.3%", "DS Feed TC Rev B, Turbo Duty PT", "70.3% (Neff)", "YES"),
        ("2", "Interstage Turbocharger (SIP-09-002) efficiency", "73.1%", "DS Feed TC Rev B, Turbo Duty PT", "73.1% (Neff)", "YES"),
        ("3", "Auxiliary nozzle efficiency loss (both turbos)", "1.5%", "DS Feed TC Rev B, Turbo Duty PT", "0.015 (Aux noz eff loss)", "YES"),
        ("4", "Interstage bypass flow at 43k TDS", "1.4\u20131.5 m\u00b3/h", "DS Feed TC Rev B, rows 7\u201310", "1.4\u20131.5 m\u00b3/h (Qbyp)", "YES"),
        ("5", "Interstage Turbo brine valve at 43k TDS", "Open", "DS Feed TC Rev B, rows 7\u201310", "Open", "YES"),
        ("6", "HP Pump absorbed power (design point)", "83.1 kW", "DS HP Pump Rev B, Technical Proposal p.3", "83.1 kW (Absorbed Power)", "YES"),
        ("7", "HP Pump flow", "49.0 m\u00b3/h", "DS HP Pump Rev B, Technical Proposal p.3", "49.0 m\u00b3/h", "YES"),
        ("8", "HP Pump discharge pressure", "51.4 bar", "DS HP Pump Rev B, Technical Proposal p.3", "51.4 bar", "YES"),
        ("9", "HP Pump efficiency", "80.9%", "DS HP Pump Rev B, Technical Proposal p.3", "80.9%", "YES"),
        ("10", "Motor manufacturer", "ABB", "DS HP Pump Rev B, Motor Data", "ABB or equivalent", "YES"),
        ("11", "Motor power rating", "125 HP (93 kW), 380V/50Hz/3\u03c6", "DS HP Pump Rev B, Motor Data", "125.0 HP, 380V, 50Hz", "YES"),
        ("12", "Motor enclosure", "TEFC, IP66", "DS HP Pump Rev B, Motor Data", "Totally enclosed fan-cooled, IP66", "YES"),
        ("13", "Motor efficiency", "95%", "DS HP Pump Rev B, Motor Data", "95.0%", "YES"),
        ("14", "VFD manufacturer and model", "Siemens SINAMICS G120X 110 kW, 6SL3220-3YE46-0UF0", "DS HP Pump Rev B, Drive Data", "Siemens SINAMICS G120X 110 kW, 6SL3220-3YE46-0UF0", "YES"),
        ("15", "System recovery rate", "42.86%", "Process Calc Rev B", "42.86%", "YES"),
        ("16", "Feed / Permeate / Reject flow", "49 / 21 / 28 m\u00b3/h", "Process Calc Rev B", "49.0 / 21.0 / 28.0 m\u00b3/h", "YES"),
        ("17", "Permeate TDS at 43k Y0 (composite)", "165 mg/L", "Process Calc Rev B, LG Chem output", "165 mg/L (range 165\u2013229)", "YES"),
        ("18", "Turbocharger model", "FEDCO HPB-60 (Feed and Interstage)", "DS Feed TC Rev B", "HPB-60", "YES"),
        ("19", "Turbocharger weight", "27.7 kg each", "DS Feed TC Rev B", "27.7 kg", "YES"),
        ("20", "Turbocharger dimensions", "288\u00d7279\u00d7254 mm", "DS Feed TC Rev B", "288 mm L \u00d7 279.07 mm W \u00d7 254 mm H", "YES"),
        ("21", "Wetted parts material", "Super Duplex 2507", "DS Feed TC + DS HP Pump Rev B", "Super Duplex SS 2507 throughout", "YES"),
        ("22", "1st stage membrane configuration", "6 vessels \u00d7 7 = 42 elements (LG SW 400 SR)", "Process Calc Rev B", "6 vessel/unit, 7 element/vessel", "YES"),
        ("23", "2nd stage membrane configuration", "4 vessels \u00d7 7 = 28 elements (LG UHP)", "Process Calc Rev B", "4 vessel/unit, 7 element/vessel", "YES"),
        ("24", "Feed TDS operating range", "43,000\u201353,000 mg/L", "Process Calc Rev B, Design Basis", "43,000\u201353,000 mg/L", "YES"),
        ("25", "Feed temperature range", "19\u00b0C\u201324\u00b0C", "Process Calc Rev B, Design Basis", "19.0\u201324.0 \u00b0C", "YES"),
    ])

    # ============================================================
    # 5. 10 OPERATING SCENARIOS
    # ============================================================
    doc.add_heading("10 OPERATING SCENARIOS \u2014 PRESSURE VERIFICATION", level=1)

    add_para(
        doc,
        "The following table confirms that the pressure values in the NotebookLM presentation "
        "script (Slide 9) are identical to those in the BiTurbo\u2122 Performance table within "
        "DS Feed Turbocharger Rev B (P22-ET-09-009-007-B), which is itself derived from "
        "Process Calculation Rev B.",
    )

    add_simple_table(doc, [
        ("#", "TDS (ppm)", "Temp", "Membrane", "P Feed 1st (bar)", "P Feed 2nd (bar)", "P Reject 2nd (bar)", "HPP \u0394P (bar)", "Feed Boost (bar)", "IS Boost (bar)", "Match"),
        ("1",  "53,000", "19\u00b0C", "Y1+10%", "69.53", "84.81", "83.33", "48.9", "20.9", "16.8", "YES"),
        ("2",  "53,000", "19\u00b0C", "Y0+10%", "68.83", "84.11", "82.62", "48.5", "20.6", "16.8", "YES"),
        ("3",  "53,000", "19\u00b0C", "Y1",     "63.21", "77.10", "75.75", "44.8", "18.7", "15.4", "YES"),
        ("4",  "53,000", "19\u00b0C", "Y0",     "62.57", "76.46", "75.11", "44.5", "18.4", "15.4", "YES"),
        ("5",  "53,000", "24\u00b0C", "Y1",     "62.11", "76.01", "74.67", "44.2", "18.3", "15.4", "YES"),
        ("6",  "53,000", "24\u00b0C", "Y0",     "61.59", "75.49", "74.16", "43.8", "18.0", "15.4", "YES"),
        ("7",  "43,000", "19\u00b0C", "Y1",     "52.14", "62.03", "60.68", "37.7", "14.7", "11.4", "YES"),
        ("8",  "43,000", "19\u00b0C", "Y0",     "51.64", "61.53", "60.18", "37.5", "14.4", "11.4", "YES"),
        ("9",  "43,000", "24\u00b0C", "Y1",     "51.21", "61.11", "59.77", "37.3", "14.2", "11.4", "YES"),
        ("10", "43,000", "24\u00b0C", "Y0",     "50.82", "60.72", "59.38", "37.1", "14.0", "11.4", "YES"),
    ])

    add_para(
        doc,
        "All 10 scenarios match exactly. The pressure progression confirms the physical basis: "
        "higher TDS requires higher operating pressures due to greater osmotic pressure. The +10% "
        "safety margin scenarios (#1 and #2) bound the design envelope at maximum salinity. At "
        "43k TDS, the Interstage Turbocharger operates with bypass open (1.4\u20131.5 m\u00b3/h), "
        "consistent with Section 3.2 of this document.",
    )

    # ============================================================
    # 6. IMPLICATIONS FOR OPEN FINDINGS
    # ============================================================
    doc.add_heading("IMPLICATIONS FOR OPEN FINDINGS", level=1)

    add_para(
        doc,
        "The NotebookLM material provides independent supporting evidence for both open critical "
        "findings documented in the transmittal evaluation (P22-IT-06-000-001-0). The following "
        "table summarizes the connection.",
    )

    add_simple_table(doc, [
        ("Finding", "Ref", "Age (Feb 25)", "NotebookLM Evidence", "Implication", "Required Action"),
        ("HP Pump power inconsistency",
         "TM N4 OBS-08",
         "18 days",
         "Slide 6 uses 83.1 kW (absorbed); Slide 16 also uses 83 kW \u2014 correct for SEC. 87 kW and 90 kW from same DS not reconciled.",
         "NotebookLM applies correct value but DS discrepancy unresolved; procurement cannot proceed without unified power table.",
         "BW Water to deliver revised DS with clarification note distinguishing absorbed power, motor input, and nameplate rating."),
        ("SEC calculation incomplete",
         "TM N3 OBS-02",
         "28 days",
         "Slide 12 presents 4.84\u20135.09 kWh/m\u00b3 at 43k TDS vs 4.71 kWh/m\u00b3 guarantee; explicitly flags potential non-compliance.",
         "NotebookLM identifies the gap more clearly than Process Calc Rev B, which contains no SEC table.",
         "BW Water to deliver revised Process Calculation with SEC table covering all 10 scenarios and stating reference condition for 3.98 kWh/m\u00b3 claim."),
    ])

    # ============================================================
    # 7. SOURCE TRACEABILITY
    # ============================================================
    doc.add_heading("SOURCE TRACEABILITY", level=1)

    add_para(
        doc,
        "The NotebookLM presentation and video scripts were authored by ADASA engineering staff "
        "using data extracted exclusively from official BW Water deliverables. The primary "
        "derivation chain is as follows:",
    )
    add_para(
        doc,
        "All numerical values in Slides 3, 6, 7, 8, 9, 12, 13, 14, and 16 trace to Process "
        "Calculation Rev B (P22-CD-09-009-001-B), the BiTurbo\u2122 Performance table embedded in "
        "DS Feed Turbocharger Rev B (P22-ET-09-009-007-B), and the DS HP Pump Rev B "
        "(P22-ET-09-009-002-B). These three documents form the computational core of the module design.",
    )
    add_para(
        doc,
        "The LG Chem projection data (permeate quality table, Slide 14) derives from the LG Design "
        "v3.3 model output embedded in Process Calculation Rev B, Project 71332_LG_R2_rev B.",
    )
    add_para(
        doc,
        "The SEC values at 43k TDS (Slide 12) derive from the same BiTurbo\u2122 Performance sheet "
        "(Version 2.29-D, dated 01/13/2026) included in DS Feed Turbocharger Rev B. This sheet "
        "contains pump efficiency input fields (Pump eff, Mot eff, VFD eff) that are blank (0.00) "
        "in the current revision \u2014 confirming that the SEC calculation has not been formalized "
        "in the official document set.",
    )
    add_para(
        doc,
        "The 3.98 kWh/m\u00b3 value cited as the BW Water guarantee condition appears in BW Water\u2019s "
        "commercial materials and was included in the NotebookLM content for completeness, but does "
        "not appear in any formal calculation deliverable reviewed to date.",
    )
    add_para(
        doc,
        "The PDFs, videos, and structured notes in the NotebookLM knowledge base are derivative "
        "works for internal ADASA use only. They do not constitute official project documents and "
        "shall not be transmitted to BW Water or third parties. For any contractual or technical "
        "dispute, the official document versions listed in Section 2 of this document take precedence.",
    )

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
