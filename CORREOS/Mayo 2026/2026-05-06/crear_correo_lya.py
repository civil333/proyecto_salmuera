#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ejecutivo a L&A Ingeniería y Proyectos (Pablo Castillo) — cargas para
diseño de fundación del estanque TK-06-001 con efecto del sismo vertical
NCh 2369 Of.2003.

Fecha: 6 de mayo de 2026.

Configuración: idioma del documento Word fijado en es-CL para que Word aplique
corrección ortográfica y gramatical en español (CLAUDE.md Sección 3.6 v6.8).
"""

import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(
    SCRIPT_DIR,
    "2026-05-06_LyA-Sismo-Vertical-TK-06-001.docx",
)
CONTACTO = "Luis Rivera"
LANG = "es-CL"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def aplicar_arial(paragraph, size=11):
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(size)


def aplicar_arial_table(table, size=10):
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)


def _set_lang_in_rPr(rPr, lang):
    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = OxmlElement("w:lang")
        rPr.append(lang_el)
    lang_el.set(qn("w:val"), lang)
    lang_el.set(qn("w:eastAsia"), lang)
    lang_el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    """Configura es-CL en todos los runs del documento y en el estilo Normal,
    para que Word interprete el texto como español de Chile."""
    try:
        rPr = doc.styles["Normal"].element.get_or_add_rPr()
        _set_lang_in_rPr(rPr, lang)
    except KeyError:
        pass
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            _set_lang_in_rPr(run._element.get_or_add_rPr(), lang)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        _set_lang_in_rPr(run._element.get_or_add_rPr(), lang)


def add_table_with_header(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = header
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True
    for i, row_data in enumerate(rows, start=1):
        for j, value in enumerate(row_data):
            table.rows[i].cells[j].text = str(value)
    aplicar_arial_table(table, size=10)
    return table


# ---------------------------------------------------------------------------
# Cuerpo del correo
# ---------------------------------------------------------------------------
def crear_correo():
    doc = Document()

    # Márgenes 0,8" para que las tablas quepan cómodas
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # =========================================================================
    # ENCABEZADO
    # =========================================================================
    fields = [
        ("Fecha:", "6 de mayo de 2026"),
        ("De:", f"{CONTACTO} — DIO ADASA (Aguas de Antofagasta S.A.)"),
        (
            "Para:",
            "Pablo Castillo — L&A Ingeniería y Proyectos (pcastillo@lyaingenieria.cl)",
        ),
        (
            "CC:",
            "Yohana Rodríguez Flores, Cristhian Sánchez, Luciano Méndez Huidobro "
            "(L&A); Víctor Gutiérrez (ADASA)",
        ),
        (
            "Asunto:",
            "PD Taltal — Cargas para diseño de fundación TK-06-001: efecto del "
            "sismo vertical (NCh 2369 Of.2003)",
        ),
        ("Ref:", "BAE 12803 / TdR P22-TR-00-010-01-1 / EX-26005 / P22-IT-06-000-005-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # SALUDO Y CONTEXTO
    # =========================================================================
    para = doc.add_paragraph("Estimado Pablo:")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "En respuesta a tu consulta sobre el tratamiento del sismo vertical en la "
        "memoria de cálculo del estanque TK-06-001 (Exfibro Rev. A, plano "
        "EX-26005-F01 Rev C), ADASA realizó la revisión independiente y "
        "trasladamos las observaciones formales a Anwo/Exfibro solicitando la "
        "Rev B de la memoria. La buena noticia: "
    )
    para.add_run(
        "el efecto numérico es modesto y no es un bloqueante para que ustedes "
        "avancen con el dimensionamiento de la fundación"
    ).bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "A continuación el resumen de los dos cambios relevantes para el diseño "
        "civil."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # TABLA 1 — REACCIONES BASALES
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("1) Reacciones basales para diseño de la fundación").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=[
            "Componente",
            "Exfibro Rev. A",
            "ADASA validado\n(Cv = 0,267)",
            "Δ",
        ],
        rows=[
            ("Peso propio Fz", "−586 kg", "−586 kg", "0 %"),
            ("Fluido en operación Fz", "−11.986 kg", "−11.986 kg", "0 %"),
            ("Peso total estático Fz", "−12.572 kg", "−12.572 kg", "0 %"),
            ("Cortante basal Ex (sismo H)", "±4.617 kg", "±4.617 kg", "0 %"),
            ("Cortante basal Ey (sismo H)", "±4.617 kg", "±4.617 kg", "0 %"),
            ("Momento volcante Mx (sismo H)", "±431.846 kg·cm", "±431.846 kg·cm", "0 %"),
            ("Momento volcante My (sismo H)", "±431.846 kg·cm", "±431.846 kg·cm", "0 %"),
            ("Carga sísmica vertical Ez", "−2.514 kg", "±3.357 kg", "+33,5 % (signo ±)"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "El único valor que cambia es "
    )
    para.add_run("Ez").bold = True
    para.add_run(
        ". Exfibro lo reporta como −2.514 kg (Cv aparente ≈ 0,20 sin desarrollo "
        "trazable). El re-cálculo ADASA con Cv = (2/3)·A0/g = 0,267 según NCh "
        "2369 Of.2003 Sección 5.5.1 letra b), aplicado sobre el peso total, da "
    )
    para.add_run("Ez = ±Cv·W_tot = ±3.357 kg").bold = True
    para.add_run(
        ". La diferencia más relevante para el diseño civil no es la magnitud sino "
        "el "
    )
    para.add_run("signo ±").bold = True
    para.add_run(
        ": para diseño de losa hay que evaluar las dos direcciones (peso aumentado "
        "+Cv para compresión sobre la losa; peso reducido −Cv para tracción de "
        "pernos)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # TABLA 2 — SOLICITACIONES DEL PERNO
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("2) Solicitaciones del perno de anclaje").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=[
            "Magnitud",
            "Exfibro Rev. A\n(sin Cv)",
            "ADASA validado\n(Cv = 0,267 — combinación 1,0·H + 1,0·V con signos ±, ASD)",
            "Δ",
        ],
        rows=[
            ("Tracción tb por perno", "1.510 kg", "1.598 kg", "+5,8 % (+88 kg)"),
            ("Corte V por perno", "2.597 kg", "2.597 kg", "0 %"),
            ("σ tracción", "420 kg/cm²", "444 kg/cm²", "+5,7 %"),
            ("τ corte", "723 kg/cm²", "723 kg/cm²", "0 %"),
            ("σ / σ_adm (σ_adm = 2.024 kg/cm²)", "0,207", "0,219", "—"),
            ("τ / τ_adm (τ_adm = 1.011 kg/cm²)", "0,715", "0,715", "0 %"),
            ("Interacción σ/σ_adm + τ/τ_adm", "0,922", "0,934", "≤ 1 — CUMPLE"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Combinación aplicada: Sección 4.5 letra a) NCh 2369 Of.2003 — "
        "Combinaciones de cargas (método de tensiones admisibles)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Nota: τ_adm = 1.011 kg/cm² resulta de la conversión 99,2 MPa × 10,197 "
        "(factor exacto MPa → kg/cm²); la memoria Exfibro Rev. A reporta τ_adm = "
        "99,2 MPa."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Los pernos M25 (1\") F1554 Gr.36 siguen cumpliendo con margen. Para el "
        "embebido y arrancamiento del perno en el hormigón, la tracción de diseño "
        "se actualiza a "
    )
    para.add_run("1.598 kg/perno").bold = True
    para.add_run(
        " (en lugar de 1.510 kg de Exfibro Rev. A). "
    )
    para.add_run("Diferencia: +88 kg por perno (+5,8 %).").bold = True
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # RECOMENDACIÓN
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("3) Recomendación").bold = True
    aplicar_arial(para)

    bullets = [
        (
            "Pueden continuar con el dimensionamiento de la fundación",
            (
                " del estanque TK-06-001 usando las cargas de la columna "
                "“ADASA validado”. Los deltas son: +5,8 % en tracción del perno "
                "(1.510 → 1.598 kg) y cambio de signo en Ez (−2.514 → ±3.357 kg). "
                "El resto de las cargas basales no cambia."
            ),
        ),
        (
            "Para el cálculo de la losa:",
            (
                " aplicar la combinación direccional de la Sección 4.5 letra "
                "a) NCh 2369 Of.2003 — Combinaciones de cargas (método de "
                "tensiones admisibles, 100 % H + 100 % V con signos ±). El "
                "caso desfavorable para compresión bajo el estanque es "
                "1,0·Fz_total + 1,0·Ez (peso aumentado); para arrancamiento "
                "de pernos es 1,0·Fz − 1,0·Ez (peso reducido)."
            ),
        ),
        (
            "La Rev B de la memoria Exfibro está solicitada con plazo de 10 días "
            "hábiles.",
            (
                " No anticipamos cambios mayores sobre los valores de la columna "
                "“ADASA validado”, salvo que Exfibro justifique un Cv distinto "
                "al (2/3)·A0/g = 0,267 que estamos asumiendo conforme NCh 2369 "
                "Of.2003 Sección 5.5.1 letra b). Les avisaremos en cuanto llegue."
            ),
        ),
    ]
    for negrita, texto in bullets:
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(negrita).bold = True
        para.add_run(texto)
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # CIERRE
    # =========================================================================
    para = doc.add_paragraph(
        "Quedo atento a cualquier consulta adicional para no detener su diseño."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph("Saludos cordiales,")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run(CONTACTO).bold = True
    aplicar_arial(para)
    for line in [
        "Departamento de Ingeniería y Optimización (DIO)",
        "ADASA — Aguas de Antofagasta S.A.",
        "luis.rivera@adasa.cl",
    ]:
        para = doc.add_paragraph(line)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph()
    para.add_run("Adjunto opcional: ").bold = True
    para.add_run(
        "calculo_pernos_TK-06-001_ADASA.xlsx — planilla de respaldo del re-cálculo "
        "(reproduce tb = 1.510 kg de la memoria Exfibro al 99,9 % y aplica Cv = "
        "0,267 con la combinación de la Sección 4.5 letra a) NCh 2369 "
        "Of.2003 — Combinaciones de cargas, ASD pleno; resultado tb = "
        "1.598 kg)."
    )
    aplicar_arial(para)

    # =========================================================================
    # IDIOMA es-CL — última operación antes de guardar
    # =========================================================================
    fijar_idioma_documento(doc, LANG)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")
    print(f"Idioma del documento: {LANG}")


if __name__ == "__main__":
    crear_correo()
