#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo cordial a Anwo/Exfibro — Consulta sobre tratamiento del sismo vertical
en la memoria de cálculo del estanque de salmuera TK-06-001.

Fecha: 6 de mayo de 2026

Configuración: idioma del documento Word fijado en es-CL (español de Chile)
para que Word aplique corrección ortográfica y gramatical en español.
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
    "2026-05-06_Consulta-Sismo-Vertical-Memoria-TK-06-001.docx",
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
    """Configura el idioma en todos los runs del documento (cuerpo + tablas)
    y en el estilo Normal, para que Word interprete el texto como español."""
    # Estilo Normal — afecta runs creados sin estilo explícito
    try:
        normal = doc.styles["Normal"]
        rPr = normal.element.get_or_add_rPr()
        _set_lang_in_rPr(rPr, lang)
    except KeyError:
        pass

    # Runs en párrafos del cuerpo
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            rPr = run._element.get_or_add_rPr()
            _set_lang_in_rPr(rPr, lang)

    # Runs dentro de tablas
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        rPr = run._element.get_or_add_rPr()
                        _set_lang_in_rPr(rPr, lang)


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

    # Márgenes 0,8" para que la tabla quepa cómoda
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
        ("De:", f"{CONTACTO} — Ingeniero de Proyecto (ADASA)"),
        ("Para:", "Anwo Ltda. — Departamento Técnico"),
        ("CC:", "Exfibro Ltda. (J. Aguilar / C. Salas), Víctor Gutiérrez (ADASA)"),
        (
            "Asunto:",
            "PD Taltal — Consulta sobre el tratamiento del sismo vertical en la "
            "memoria de cálculo del Estanque de Salmuera TK-06-001 (EX-26005-F01)",
        ),
        ("Ref:", "BAE 12803 / OC Folio 834750 / EX-26005 / P22-CT-06-000-002-0"),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # SALUDO Y APERTURA
    # =========================================================================
    para = doc.add_paragraph("Estimados:")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Junto con saludarles, en el marco de la preparación de la licitación de la "
        "ingeniería de detalle de obras civiles del proyecto Taltal, el equipo técnico "
        "de ADASA ha completado la revisión de los antecedentes del estanque de "
        "salmuera "
    )
    para.add_run("TK-06-001").bold = True
    para.add_run(
        " entregados por Exfibro: el plano EX-26005-F01 Rev C y la memoria de cálculo "
        "“Memoria Estanque AFTA Taltal” Rev. A."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "La revisión confirma que el modelo dinámico aplicado (Housner impulsivo y "
        "convectivo, parámetros NCh 2369, ASME RTP-1) es "
    )
    para.add_run("correcto y trazable").bold = True
    para.add_run(
        ", y que los pernos M25 (1\") F1554 Gr. 36 especificados resultan adecuados "
        "para las cargas sísmicas del proyecto."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Sin embargo, hemos identificado un punto que requiere rectificación formal "
        "de la memoria antes de que ADASA pueda trasladarla al consultor de obras "
        "civiles como antecedente final: "
    )
    para.add_run(
        "la fórmula de tracción de los pernos no incorpora explícitamente el efecto "
        "desfavorable del sismo vertical sobre el peso estabilizador"
    ).bold = True
    para.add_run(", conforme exige NCh 2369 Of.2003 §5.5.")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "A continuación presentamos el hallazgo numérico clave que ADASA ha "
        "verificado de manera independiente, con tres elementos: (1) el cálculo "
        "original de EXFIBRO tal como aparece en la página 11 de la memoria; "
        "(2) la tabla comparativa con el re-cálculo ADASA; y (3) el análisis "
        "paso a paso de las diferencias."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # CÁLCULO ORIGINAL EXFIBRO (REPRODUCCIÓN DE LA PÁGINA 11)
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "1) Cálculo original — EXFIBRO Rev. A (memoria página 11, "
        "“Load on Anchor Bolt”)"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "El bloque de cálculo emitido por Exfibro se reproduce a continuación "
        "(valores y fórmulas literales de la memoria):"
    )
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=["Variable", "Fórmula", "Valor", "Unidad"],
        rows=[
            ("Msr", "W · D / 2", "76.187", "kg·cm"),
            ("Mt", "M − Msr", "355.658", "kg·cm"),
            ("X", "fb · t = Mt / (π · R²)", "6,57", "kg/cm"),
            ("Y", "p · d / 4", "0", "kg/cm"),
            ("P", "π · D · (X + Y) / N", "671", "kg"),
            ("F", "P · (a + b) / b", "1.007", "kg"),
            ("Mt (Total moment at Base)", "—", "355.658", "kg·cm"),
            ("Load in Bolt", "F", "1.007", "kg (Allowable for 1\" Dia. Mín.)"),
            ("Load per anchor Dog", "P", "671", "kg/dog (C.S. A36)"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Sobre F = 1.007 kg, EXFIBRO aplica una amplificación adicional de 50 % "
        "(página 12) y reporta la tracción de diseño "
    )
    para.add_run("tb = 1.510 kg").bold = True
    para.add_run(
        ". El peso utilizado en la línea Msr es exclusivamente W = 586 kg "
        "(peso vacío del estanque, sin fluido). En este desarrollo, el "
        "coeficiente sísmico vertical Cv no aparece."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # TABLA COMPARATIVA
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("2) Tabla comparativa — solicitaciones del perno").bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=[
            "Magnitud",
            "Memoria EXFIBRO\n(sin Cv)",
            "Re-cálculo ADASA\n(Cv = 0,267 — regla 100/30)",
            "Δ",
        ],
        rows=[
            ("Peso estabilizador efectivo W·(1−Cv)", "586 kg", "539 kg", "−8,0 %"),
            ("Msr = W_eff · D / 2", "76.187 kg·cm", "70.080 kg·cm", "−8,0 %"),
            ("Mt = M − Msr", "355.658 kg·cm", "361.766 kg·cm", "+1,7 %"),
            ("Tensión circunferencial X", "6,57 kg/cm", "6,69 kg/cm", "+1,8 %"),
            ("Carga radial por perno P", "671 kg", "683 kg", "+1,8 %"),
            ("Carga por perno F = P·(a+b)/b", "1.007 kg", "1.025 kg", "+1,8 %"),
            ("Tracción tb (amplificada 50 %)", "1.510 kg", "1.537 kg", "+1,7 %"),
            ("σ tracción", "420 kg/cm²", "427 kg/cm²", "+1,7 %"),
            ("τ corte (sin variación)", "723 kg/cm²", "723 kg/cm²", "—"),
            ("Interacción σ/σ_adm + τ/τ_adm", "0,939", "0,939", "≤ 1 → CUMPLE"),
        ],
    )
    doc.add_paragraph()

    # =========================================================================
    # ANÁLISIS PASO A PASO
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "3) Análisis paso a paso — cómo cambia cada línea del procedimiento al "
        "introducir Cv"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "Aplicando el coeficiente sísmico vertical Cv = (2/3)·Cmax = 0,267 con la "
        "combinación 100/30 (1,0·H + 0,3·V), el efecto sobre cada línea del "
        "procedimiento original es el siguiente:"
    )
    aplicar_arial(para)

    pasos = [
        (
            "Peso estabilizador efectivo. ",
            "El peso vacío W = 586 kg se reemplaza por W_eff = W·(1 − 0,3·Cv) = "
            "586 · 0,920 = 539 kg (−8,0 %). Es la única variable que cambia "
            "directamente por efecto del sismo vertical.",
        ),
        (
            "Msr = W · D / 2. ",
            "Como Msr es lineal en W, el momento estabilizador disminuye en la "
            "misma proporción: 76.187 → 70.080 kg·cm (−8,0 %).",
        ),
        (
            "Mt = M − Msr. ",
            "El momento volcante M no cambia (sigue siendo 431.846 kg·cm), pero "
            "Msr es menor; por lo tanto el momento neto que llega a los pernos "
            "aumenta: 355.658 → 361.766 kg·cm (+1,7 %).",
        ),
        (
            "X = Mt / (π · R²). ",
            "La tensión circunferencial sobre el anillo de anclaje es proporcional "
            "a Mt; aumenta de 6,57 → 6,69 kg/cm (+1,8 %).",
        ),
        (
            "P = π · D · X / N. ",
            "La carga radial por perno es proporcional a X; pasa de 671 → 683 kg "
            "(+1,8 %).",
        ),
        (
            "F = P · (a + b) / b y tb = F · 1,5. ",
            "La amplificación geométrica de la silla y el factor 1,5 son "
            "constantes; F sube de 1.007 → 1.025 kg y la tracción de diseño "
            "tb pasa de 1.510 → 1.537 kg (+1,7 %).",
        ),
        (
            "Verificación de esfuerzos. ",
            "σ tracción aumenta de 420 → 427 kg/cm² (+1,7 %), muy por debajo del "
            "admisible de 2.024 kg/cm² (0,8·Fy). El corte τ no cambia (Cv no "
            "afecta la fuerza horizontal). La interacción σ/σ_adm + τ/τ_adm "
            "se mantiene en 0,939, dominada por el corte. Los pernos M25 "
            "F1554 Gr. 36 siguen cumpliendo con margen.",
        ),
    ]
    for negrita, texto in pasos:
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(negrita).bold = True
        para.add_run(texto)
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "En resumen, la corrección por sismo vertical actúa exclusivamente sobre "
        "el peso estabilizador del término Msr, y se propaga proporcionalmente al "
        "resto del procedimiento. El impacto numérico final es modesto (+1,7 % en "
        "tb) gracias a que en este equipo el peso vacío representa solo "
        "586/12.572 ≈ 4,7 % del peso total y Msr es pequeño frente a M; sin "
        "embargo, el desarrollo formal debe constar en la memoria por exigencia "
        "de NCh 2369 Of.2003 §5.5."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # CONTEXTO Ez Y NORMATIVA
    # =========================================================================
    para = doc.add_paragraph(
        "En consecuencia, el resultado físico no cambia —el diseño es seguro—, pero "
        "la memoria de cálculo no documenta hoy el desarrollo del Cv ni la "
        "combinación direccional, y el valor "
    )
    para.add_run("Ez = −2.514 kg").bold = True
    para.add_run(
        " que aparece en la tabla de cargas basales (página 18) no es trazable a "
        "una fórmula explícita: el cociente Ez / W_tot = 0,20 sugiere "
        "Cv = (2/3)·0,30, valor que resulta inconsistente con el Cmax = 0,40 "
        "declarado en página 7 (con el cual correspondería Cv = 0,267 → "
        "Ez = ±3.357 kg)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SOLICITUDES
    # =========================================================================
    para = doc.add_paragraph("Por lo anterior, solicitamos atentamente:")
    aplicar_arial(para)

    solicitudes = [
        (
            "Emisión de la Rev B de la memoria de cálculo que: (a) declare la "
            "versión de NCh 2369 efectivamente aplicada; (b) muestre el desarrollo "
            "del coeficiente sísmico vertical Cv y su origen normativo; (c) "
            "represente el cálculo de tracción de pernos aplicando explícitamente "
            "W → W·(1 − Cv) y la combinación 100/30; y (d) ratifique las "
            "reacciones basales (Ex, Ey, Ez, Mx, My) que se entregan al ingeniero "
            "civil para el diseño de la fundación."
        ),
        "Aclaración del valor Ez = −2.514 kg de la tabla de la página 18.",
        (
            "Resolución de la cita normativa del plano EX-26005-F01 Rev C "
            "(“NCh 2369-2025”), que difiere de los parámetros aplicados en la "
            "memoria (correspondientes a Of.2003)."
        ),
    ]
    for item in solicitudes:
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• " + item)
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # ADJUNTOS Y CIERRE
    # =========================================================================
    para = doc.add_paragraph("Como referencia técnica formal, adjuntamos:")
    aplicar_arial(para)

    adjuntos = [
        (
            "Consulta técnica P22-CT-06-000-002-0 — documento ADASA con las ocho "
            "preguntas (Q1 a Q8) detalladas."
        ),
        (
            "Memorando interno P22-IT-06-000-005-0 — desarrollo completo del "
            "re-cálculo independiente y trazabilidad numérica."
        ),
        (
            "Planilla calculo_pernos_TK-06-001_ADASA.xlsx — respaldo del re-cálculo "
            "(reproduce tb = 1.510 kg de la memoria al 99,9 % y aplica Cv según "
            "Of.2003)."
        ),
    ]
    for i, item in enumerate(adjuntos, start=1):
        para = doc.add_paragraph(style=None)
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run(f"{i}. {item}")
        aplicar_arial(para)

    doc.add_paragraph()

    para = doc.add_paragraph(
        "Quedamos atentos a su respuesta. Considerando que el material es "
        "antecedente directo para la licitación de obras civiles, agradeceríamos "
        "contar con la Rev B de la memoria en un plazo de "
    )
    para.add_run("diez (10) días hábiles").bold = True
    para.add_run(".")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Si surge alguna consulta de aclaración técnica antes de emitir la nueva "
        "revisión, no duden en contactarnos directamente."
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
        "Ingeniero de Proyecto",
        "ADASA — Aguas de Antofagasta S.A.",
        "luis.rivera@adasa.cl",
    ]:
        para = doc.add_paragraph(line)
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
