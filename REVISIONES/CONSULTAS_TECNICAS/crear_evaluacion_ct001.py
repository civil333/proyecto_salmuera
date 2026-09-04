#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar la Evaluacion de Respuesta CT-001 en formato ADASA.
Fecha: 16-Feb-2026

Genera P22-CT-09-000-001-1_Evaluacion-Respuesta-Antiescalante_ADASA.docx
"""

import sys
import os

# Agregar la ruta del skill template-adasa
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", ".claude", "skills", "template-adasa",
)
sys.path.insert(0, skill_path)

from ejemplo_documento import crear_documento_adasa, aplicar_arial_12
from docx import Document
from docx.shared import Pt, Inches, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import nsdecls, qn
from docx.oxml import parse_xml
from lxml import etree


def set_updatefields_true(doc):
    """Configura Word para actualizar TOC al abrir el documento."""
    settings = doc.settings.element
    update = settings.find(qn('w:updateFields'))
    if update is None:
        update = etree.SubElement(settings, qn('w:updateFields'))
    update.set(qn('w:val'), 'true')


def set_table_borders(table):
    """Aplica bordes a todas las celdas de una tabla y la centra."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml('<w:tblPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
    borders = parse_xml(
        '<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '  <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '  <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '  <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '</w:tblBorders>'
    )
    tblPr.append(borders)
    # Centrar tabla
    jc = parse_xml('<w:jc xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="center"/>')
    tblPr.append(jc)


def set_repeat_table_header(row):
    """Configura una fila para repetirse como header en cada pagina."""
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    tblHeader = trPr.makeelement(qn('w:tblHeader'), {qn('w:val'): 'true'})
    trPr.append(tblHeader)


def add_table(doc, data, col_widths=None):
    """
    Agrega una tabla con bordes y formato Arial 11pt.
    data: lista de tuplas. Primera tupla = header (bold).
    col_widths: lista de anchos en Inches (opcional).
    """
    if not data:
        return None
    rows = len(data)
    cols = len(data[0])
    table = doc.add_table(rows=rows, cols=cols)
    set_table_borders(table)

    # Establecer anchos de columna si se proporcionan
    if col_widths:
        for i, width in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Inches(width)

    for i, row_data in enumerate(data):
        for j, cell_text in enumerate(row_data):
            cell = table.rows[i].cells[j]
            cell.text = ""
            para = cell.paragraphs[0]
            run = para.add_run(str(cell_text))
            run.font.name = "Arial"
            run.font.size = Pt(10)
            if i == 0:  # Header row
                run.bold = True
                # Gray background for header
                shading = parse_xml(
                    f'<w:shd {nsdecls("w")} w:fill="D9E2F3" w:val="clear"/>'
                )
                cell._tc.get_or_add_tcPr().append(shading)

    # Repeat header row en cada pagina
    set_repeat_table_header(table.rows[0])

    return table


def add_para(doc, text, bold=False, size=11, space_after=6):
    """Agrega un parrafo con formato Arial."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.bold = bold
    para.paragraph_format.space_after = Pt(space_after)
    return para


def crear_evaluacion():
    """Genera la evaluacion de respuesta CT-001 en formato ADASA."""

    output_file = "P22-CT-09-000-001-1_Evaluacion-Respuesta-Antiescalante_ADASA.docx"

    # Crear documento base
    crear_documento_adasa(
        titulo="TECHNICAL QUERY CT-001 - RESPONSE EVALUATION",
        codigo="P22-CT-09-000-001-1",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=output_file,
    )

    # Abrir y limpiar contenido de ejemplo
    doc = Document(output_file)

    paragraphs_to_remove = []
    for para in doc.paragraphs:
        texto = para.text.upper()
        if any(x in texto for x in [
            "RESUMEN EJECUTIVO",
            "ESTE DOCUMENTO HA SIDO GENERADO",
            "REEMPLACE ESTE CONTENIDO",
            "1. INTRODUCCI",
            "AGREGUE AQU",
        ]):
            paragraphs_to_remove.append(para)

    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)

    # ===== CONTENIDO DEL DOCUMENTO =====
    # (page break ya incluido por crear_documento_adasa)
    # (TOC se actualiza automaticamente al abrir Word via set_updatefields_true)

    # Header info
    add_para(doc, "Date: February 16, 2026", size=11)
    add_para(doc, "Project: BAE 12803 - Second Stage RO Brine Module", size=11)
    add_para(doc, "From: ADASA - Aguas de Antofagasta S.A.", size=11)
    add_para(doc, "To: BW Water Americas Inc.", size=11)
    add_para(doc, "Reference: P22-CT-09-000-001-0 (issued February 05, 2026)", size=11)

    # ===== SECTION 1: RESPONSE EVALUATION =====
    doc.add_heading("RESPONSE EVALUATION", level=1)

    doc.add_heading("Summary", level=2)

    add_para(doc,
        "ADASA issued Technical Query CT-001 on February 05, 2026, requesting "
        "manufacturer validation of the 0.5 ppm antiscalant dosing rate for "
        "concentrate conditions with LSI 2.0-2.11 at 24\u00b0C. The response "
        "deadline was February 10, 2026."
    )

    add_para(doc,
        "BW Water submitted their response on February 13, 2026 (3 days past "
        "deadline) with the following documents:"
    )

    add_table(doc, [
        ("#", "Document", "Content"),
        ("1", "BW Water Memorandum", "Cover letter summarizing two independent assessments"),
        ("2", "AWC Projection (Pureflux SW)", "PROTON software simulation for Pureflux SW antiscalant"),
        ("3", "CREST Water Email", "Third-party opinion on scaling potential"),
    ], col_widths=[0.4, 2.3, 3.8])

    doc.add_heading("General Assessment", level=2)

    add_para(doc,
        "The AWC projection demonstrates that 0.5 ppm of Pureflux SW antiscalant "
        "is acceptable for the modeled conditions. The PROTON software simulation "
        "confirms dosing adequacy with positive safety margins for CaCO3, CaSO4, "
        "BaSO4, SrSO4, and silica scaling."
    )

    add_para(doc,
        "However, ADASA has identified four technical observations that require "
        "clarification or correction before CT-001 can be formally closed."
    )

    # ===== SECTION 2: DETAILED OBSERVATIONS =====
    doc.add_heading("DETAILED OBSERVATIONS", level=1)

    doc.add_heading("Observation 1: Antiscalant Projection Temperature", level=2)

    add_table(doc, [
        ("Field", "Value"),
        ("Document", "AWC Projection - Pureflux SW"),
        ("Severity", "Major"),
        ("Category", "Design Basis"),
    ], col_widths=[1.5, 5.0])

    add_para(doc, "")  # spacer

    add_para(doc,
        "Finding: The AWC PROTON simulation was run at a feed temperature of "
        "19\u00b0C. CT-001 specifically requested justification for worst-case "
        "conditions at 24\u00b0C, where scaling potential is highest.",
        bold=False
    )

    add_para(doc,
        "Requirement: The Technical Specification (P22-ET-09-000-001-0) Table 4-1 "
        "defines the brine feed water temperature range as 19-24\u00b0C. The "
        "Technical Offer Rev.1 Section 7 reports LSI values of 2.0-2.11 at 24\u00b0C "
        "concentrate conditions. Higher temperature increases LSI and accelerates "
        "CaCO3 precipitation kinetics."
    )

    add_para(doc,
        "Impact: The projection at 19\u00b0C represents the most favorable "
        "operating condition, not the worst case. The 5\u00b0C difference affects "
        "both saturation indices and crystal growth rates. While 0.5 ppm may still "
        "be adequate at 24\u00b0C, this has not been demonstrated."
    )

    add_para(doc,
        "Required Action: BW Water shall provide an AWC projection at 24\u00b0C "
        "feed temperature confirming that 0.5 ppm Pureflux SW remains sufficient, "
        "or alternatively, provide a technical justification explaining why the "
        "19\u00b0C projection is representative of worst-case scaling behavior.",
        bold=True
    )

    # ===== SECTION 2.2: OBSERVATION 2 =====
    doc.add_heading("Observation 2: Chemical Consumption List Internal Inconsistency", level=2)

    add_table(doc, [
        ("Field", "Value"),
        ("Document", "P22-LI-09-009-002-A (Chemical Consumption List)"),
        ("Severity", "Minor"),
        ("Category", "Documentation"),
    ], col_widths=[1.5, 5.0])

    add_para(doc, "")

    add_para(doc,
        "Finding: The Chemical Consumption List reports two values for antiscalant "
        "consumption that are not internally consistent:"
    )

    add_table(doc, [
        ("Parameter", "Listed Value", "Calculated Cross-Check"),
        ("Volumetric flow", "0.02 L/h", "0.59 kg/day \u00f7 24h \u00f7 1.031 = 0.0238 L/h"),
        ("Daily consumption", "0.59 kg/day", "0.02 L/h \u00d7 24h \u00d7 1.031 = 0.495 kg/day"),
    ], col_widths=[1.8, 1.8, 3.0])

    add_para(doc,
        "The AWC projection specifies a dosing rate of 0.396 mL/min, which "
        "translates to 0.0238 L/h and 0.589 kg/day. This confirms that 0.59 kg/day "
        "is the correct value and the volumetric flow should be 0.024 L/h "
        "(not 0.02 L/h)."
    )

    add_para(doc,
        "Impact: Minor documentation error. Does not affect system operation or "
        "equipment sizing, since the dosing pump has 115x capacity margin."
    )

    add_para(doc,
        "Required Action: Update Chemical Consumption List to correct the "
        "volumetric flow from 0.02 L/h to 0.024 L/h, or verify which value is "
        "the intended design basis.",
        bold=True
    )

    # ===== SECTION 2.3: OBSERVATION 3 =====
    doc.add_heading("Observation 3: AWC Projection Input Data \u2014 Verified Gaps", level=2)

    add_table(doc, [
        ("Field", "Value"),
        ("Document", "AWC Projection (PROTON) / CREST Water Email"),
        ("Severity", "Major"),
        ("Category", "Design Input"),
    ], col_widths=[1.5, 5.0])

    add_para(doc, "")

    add_para(doc,
        "Finding: ADASA has cross-checked the AWC PROTON simulation input data "
        "against the ANAM Laboratory brine characterization reports (Report Nos. "
        "240123822 and 240123823). Two gaps were confirmed:"
    )

    add_para(doc,
        "1. Strontium omitted. The AWC projection uses Sr = 0.00 mg/L as input. "
        "The ANAM characterization measured Sr at 10\u201311 mg/L across both "
        "sampling campaigns. Strontium is directly relevant for SrSO4 saturation "
        "index calculation, and its omission means the SrSO4 safety margin "
        "reported by PROTON has not been validated against actual brine chemistry."
    )

    add_para(doc,
        "2. Silica \u2014 worst case not used. The AWC projection uses SiO2 = "
        "2.1 mg/L, which corresponds to the first ANAM sampling only. The second "
        "sampling measured 6.4 mg/L. The projection does not reflect the "
        "worst-case silica concentration."
    )

    add_para(doc,
        "Additionally, CREST Water stated that heavy metals data was unavailable, "
        "which is incorrect \u2014 the ANAM reports include a comprehensive heavy "
        "metals analysis. This confirms that BW Water did not provide the complete "
        "characterization data to either assessor."
    )

    add_para(doc,
        "AWC Input vs ANAM Measured Data \u2014 Critical Parameters:",
        bold=True
    )

    add_table(doc, [
        ("Parameter", "AWC Input", "ANAM 1st Sampling", "ANAM 2nd Sampling", "Gap"),
        ("Sr (mg/L)", "0.00", "11.226", "10.067", "NOT INCLUDED"),
        ("SiO2 (mg/L)", "2.10", "2.1", "6.4", "Worst-case not used"),
        ("Ba (mg/L)", "0.00", "<0.01", "<0.01", "OK \u2014 below detection"),
        ("B (mg/L)", "7.48", "7.475", "6.739", "OK"),
    ], col_widths=[1.2, 0.8, 1.2, 1.2, 2.0])

    add_para(doc,
        "Impact: The SrSO4 saturation index in the AWC projection is based on "
        "zero strontium and therefore does not reflect actual brine conditions. "
        "While the PROTON report shows a positive safety margin for SrSO4, this "
        "margin was computed without the measured 10\u201311 mg/L Sr concentration. "
        "The silica margin may also be understated at higher SiO2 concentrations."
    )

    add_para(doc,
        "Required Action: BW Water shall provide a revised AWC PROTON projection "
        "incorporating the measured Sr concentration (10\u201311 mg/L) and "
        "worst-case SiO2 (6.4 mg/L) from the ANAM characterization, confirming "
        "that 0.5 ppm Pureflux SW remains adequate under corrected input data.",
        bold=True
    )

    # ===== SECTION 2.4: OBSERVATION 4 =====
    doc.add_heading("Observation 4: Contradictory Assessments Without Resolution", level=2)

    add_table(doc, [
        ("Field", "Value"),
        ("Document", "BW Water Memorandum"),
        ("Severity", "Major"),
        ("Category", "Design Decision"),
    ], col_widths=[1.5, 5.0])

    add_para(doc, "")

    add_para(doc,
        "Finding: BW Water presents two independent assessments that reach "
        "contradictory conclusions:"
    )

    add_table(doc, [
        ("Assessor", "Conclusion"),
        ("AWC (Pureflux SW)", "0.5 ppm antiscalant is sufficient; dosing is recommended"),
        ("CREST Water", "No antiscalant is needed for this application"),
    ], col_widths=[2.0, 4.5])

    add_para(doc,
        "The BW Water memorandum presents both assessments side by side but does "
        "not take a position on which evaluation forms the basis of design. It "
        "does not explain the technical reasons for the discrepancy or indicate "
        "which assessment was used to size the antiscalant system."
    )

    add_para(doc, "Impact: Without a clear statement of the adopted design basis, "
        "there is ambiguity regarding:"
    )
    add_para(doc, "\u2022 Whether the system is designed to operate with or without antiscalant")
    add_para(doc, "\u2022 Which scaling model governs the membrane warranty conditions")
    add_para(doc, "\u2022 What the recommended operating protocol will be during commissioning")

    add_para(doc,
        "Required Action: BW Water shall formally state which assessment is "
        "adopted as the design basis for the antiscalant system and provide a "
        "brief explanation for why the alternative assessment is not adopted.",
        bold=True
    )

    # ===== SECTION 3: REQUIRED ACTIONS =====
    doc.add_heading("REQUIRED ACTIONS", level=1)

    add_para(doc,
        "The following actions are required from BW Water to close CT-001:"
    )

    add_table(doc, [
        ("#", "Action", "Priority", "Ref."),
        ("1", "Provide AWC projection at 24\u00b0C feed temperature, or technical justification for 19\u00b0C", "High", "OBS-1"),
        ("2", "Correct Chemical Consumption List volumetric flow (0.02 \u2192 0.024 L/h)", "Low", "OBS-2"),
        ("3", "Provide revised AWC projection with measured Sr (10\u201311 mg/L) and worst-case SiO2 (6.4 mg/L)", "High", "OBS-3"),
        ("4", "State which assessment (AWC or CREST Water) is the adopted design basis", "High", "OBS-4"),
    ], col_widths=[0.3, 3.7, 0.7, 0.7])

    add_para(doc, "Response Deadline: February 20, 2026", bold=True)

    # ===== SECTION 4: CONCLUSION =====
    doc.add_heading("CONCLUSION", level=1)

    add_para(doc,
        "The AWC projection for Pureflux SW antiscalant provides reasonable "
        "technical justification for the 0.5 ppm dosing rate under the modeled "
        "conditions. ADASA accepts this dosing rate in principle, subject to "
        "satisfactory resolution of the four observations listed above."
    )

    add_para(doc,
        "The most significant concern is the projection temperature (19\u00b0C "
        "vs. the 24\u00b0C worst case specified in the Technical Specification). "
        "If the 24\u00b0C projection confirms adequate margins, CT-001 will be "
        'closed with status "Accepted with observations resolved."'
    )

    add_para(doc,
        "The substantial dosing pump capacity margin (115x) provides operational "
        "flexibility to increase the dosing rate if field conditions require it, "
        "which partially mitigates the residual risk."
    )

    # ===== SECTION 5: DOCUMENT HISTORY =====
    doc.add_heading("DOCUMENT HISTORY", level=1)

    add_table(doc, [
        ("Rev", "Date", "Description", "Author"),
        ("0", "16-Feb-2026", "Initial issue - Response evaluation", "L. Rivera"),
    ], col_widths=[0.5, 1.5, 3.5, 1.0])

    # ===== SECTION 6: REFERENCE DOCUMENTS =====
    doc.add_heading("REFERENCE DOCUMENTS", level=1)

    add_table(doc, [
        ("Document", "Code / Reference"),
        ("Technical Query CT-001", "P22-CT-09-000-001-0 (05-Feb-2026)"),
        ("Technical Specification", "P22-ET-09-000-001-0, Table 4-1"),
        ("Chemical Consumption List", "P22-LI-09-009-002-A"),
        ("Technical Offer Rev.1", "BW Water Proposal, Section 7"),
        ("Brine Characterization", "ANAM Lab Reports 240123822 / 240123823"),
        ("AWC Projection", "Pureflux SW - PROTON simulation"),
        ("BW Water Memorandum", "Response to CT-001 (13-Feb-2026)"),
        ("CREST Water Assessment", "Email included in BW Water response"),
    ], col_widths=[2.5, 4.0])

    # Configurar actualizacion de TOC al abrir
    set_updatefields_true(doc)

    # Guardar
    doc.save(output_file)
    print(f"Documento generado: {output_file}")


if __name__ == "__main__":
    crear_evaluacion()
