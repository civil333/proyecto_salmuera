#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo ejecutivo a L&A Ingeniería (Pablo Castillo) devolviendo el Programa de
Servicio Rev B con veredicto Code 3 — To Be Revised y siete observaciones,
solicitando Rev C para el jueves 14 de mayo de 2026.

Versión 2 — formato ejecutivo (1 página densa, OBS en línea).
Idioma fijado en es-CL (CLAUDE.md §3.4 "Correos en español").
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
    "2026-05-12_LA_Programa_RevC_Observaciones.docx",
)
CONTACTO = "Luis Rivera"
LANG = "es-CL"


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


def add_table_with_header(doc, headers, rows, bold_row_indices=None):
    bold_row_indices = bold_row_indices or set()
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
        if (i - 1) in bold_row_indices:
            for cell in table.rows[i].cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True
    aplicar_arial_table(table, size=10)
    return table


def add_obs_line(doc, titulo, cuerpo):
    """OBS en una sola línea: '**OBS-N — Título.** cuerpo'."""
    para = doc.add_paragraph()
    para.add_run(f"{titulo}. ").bold = True
    para.add_run(cuerpo)
    aplicar_arial(para)


def crear_correo():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # =========================================================================
    # ENCABEZADO
    # =========================================================================
    fields = [
        ("Fecha:", "12 de mayo de 2026"),
        ("De:", f"{CONTACTO} — DIO ADASA (Aguas de Antofagasta S.A.)"),
        ("Para:", "Pablo Castillo — L&A Ingeniería y Proyectos"),
        (
            "CC:",
            "Macarena Vera, Lucas Molina, Cristhian Sánchez, Jesús Alarcón (L&A); "
            "Yohana Rodríguez, Víctor Gutiérrez (ADASA)",
        ),
        (
            "Asunto:",
            "Programa de Servicio Rev B — Observaciones ADASA y solicitud de Rev C",
        ),
        (
            "Ref:",
            "BAE 12803 / TdR P22-TR-00-010-01-1 / Minuta 067-032-032-COR-MI-001 / "
            "Programa 067-032-032-COR-PR-001 Rev B",
        ),
    ]
    for label, value in fields:
        para = doc.add_paragraph()
        para.add_run(label).bold = True
        para.add_run(f" {value}")
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # APERTURA — 2 frases
    # =========================================================================
    para = doc.add_paragraph("Estimado Pablo:")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Recibimos el lunes 11 de mayo el Programa de Servicio Rev B. Lo "
        "devolvemos con veredicto "
    )
    para.add_run("Code 3 — To Be Revised").bold = True
    para.add_run(
        ": el plazo total propuesto (entrega Rev 0 el 6 de julio) excede en 35 "
        "días la Sección 8 del TdR, y el ciclo A → B → B.1 → C → C.1 → 0 "
        "supera el máximo de dos iteraciones Rev B autorizado por la Sección 6."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Para el cálculo de plazos tomamos como T0 el "
    )
    para.add_run("lunes 4 de mayo de 2026").bold = True
    para.add_run(
        ", fecha en que ADASA aprobó formalmente el listado de entregables "
        "(minuta MI-001 ítem 1.3) y se realizó la primera reunión de trabajo "
        "(ítem 1.4) — operacionalmente equivalente a “adjudicación del "
        "contrato y recepción formal del paquete completo de antecedentes” "
        "que define la Sección 8 del TdR."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # TABLA H0-H5
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "Tabla 1 — Hitos del TdR (Sección 8) contados desde el kick-off del 4 "
        "de mayo de 2026"
    ).bold = True
    aplicar_arial(para)

    add_table_with_header(
        doc,
        headers=[
            "Hito",
            "Plazo TdR",
            "Fecha límite",
            "Entregable",
            "Programa L&A Rev B",
            "Δ",
        ],
        rows=[
            (
                "H0 — Inicio",
                "Semana 0",
                "jue 07-may",
                "Programa de trabajo",
                "lun 11-may",
                "+4 días",
            ),
            (
                "H1 — Revisión A",
                "Semana 1",
                "lun 11-may",
                "Memorias borrador + planos preliminares",
                "jue 14-may",
                "+3 días",
            ),
            (
                "H2 — Revisión B",
                "Semana 2",
                "lun 18-may",
                "Documentos completos para revisión ADASA",
                "mié 20-may → jue 28-may",
                "2 a 10 días",
            ),
            (
                "H3 — Incorporación comentarios",
                "Semana 3",
                "lun 25-may",
                "Documentos corregidos",
                "jue 28-may → jue 04-jun",
                "3 a 10 días",
            ),
            (
                "H4 — Revisión 0",
                "Semana 3,5",
                "jue 28-may",
                "Planos + ET Rev 0 para construcción",
                "lun 06-jul",
                "+39 días",
            ),
            (
                "H5 — Cierre",
                "Semana 4",
                "lun 01-jun",
                "Cubicaciones finales + presupuesto",
                "lun 06-jul (CAPEX)",
                "+35 días",
            ),
        ],
        bold_row_indices={4, 5},
    )
    doc.add_paragraph()

    # =========================================================================
    # PRIORIDAD OPERATIVA
    # =========================================================================
    para = doc.add_paragraph(
        "ADASA requiere los entregables H4 y H5 (planos, especificaciones "
        "técnicas y cubicaciones) en Rev 0 al "
    )
    para.add_run("1 de junio de 2026").bold = True
    para.add_run(
        " para iniciar la cotización de la construcción. Memoria de cálculo y "
        "CAPEX pueden desplazarse; identifiquen en la Rev C qué entregables "
        "mantienen al 01-jun y cuáles necesitan ajuste, con la justificación "
        "correspondiente."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # OBSERVACIONES — formato línea
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("Observaciones:").bold = True
    aplicar_arial(para)
    doc.add_paragraph()

    add_obs_line(
        doc,
        "OBS-1 — Plazo Rev 0 excede TdR Sección 8",
        "Programa entrega Rev 0 el 06-jul; el TdR fija 01-jun (4 semanas desde "
        "el kick-off). Slip de 35 días corridos. Re-secuenciar para entregar "
        "planos, ET y cubicaciones Rev 0 antes del 01-jun-2026.",
    )
    add_obs_line(
        doc,
        "OBS-2 — Hito de inicio no refleja la primera reunión",
        "Identificar H0 — Inicio en lun 04-may-2026 (minuta MI-001 ítem 1.4: "
        "“Se realiza primera reunión de trabajo”), fecha desde la cual corre "
        "el plazo contractual.",
    )
    add_obs_line(
        doc,
        "OBS-3 — Ciclo de revisiones excede TdR Sección 6",
        "Programa: A → B → B.1 → C → C.1 → 0 (cinco iteraciones). El TdR "
        "autoriza un máximo de dos Rev B; la tercera se trata como "
        "incumplimiento de control de calidad interno del consultor. Colapsar "
        "a A → B → B.1 → 0; comentarios ADASA sobre B.1 se incorporan a Rev 0 "
        "(Code 2) o gatillan rehacer (Code 3 / 4).",
    )
    add_obs_line(
        doc,
        "OBS-4 — Hitos H0 a H5 no integrados al cronograma",
        "Mapear cada paquete del programa al hito de Sección 8 y mostrarlos "
        "como gates con fecha en el Gantt — necesarios como referencia para "
        "Estados de Pago.",
    )
    add_obs_line(
        doc,
        "OBS-5 — Fundación CIP contradice la minuta MI-001 ítem 1.7",
        "El paquete “Fundación Compartida Contenedor + CIP” del programa "
        "(WBS 2.2.2.3.7 a 2.2.2.3.12, Rev.A a Rev.0) contradice la definición "
        "de la minuta del 04-may, que estableció fundación CIP independiente "
        "del contenedor. Separar la tarea en dos paquetes, ajustar la memoria "
        "de cálculo P22-MC-00-002-004 al nuevo alcance (dos fundaciones) y "
        "verificar el impacto sobre las cubicaciones. La modificación de "
        "alcance respecto al TdR Sección 6.1 se formalizará en acta "
        "complementaria.",
    )
    add_obs_line(
        doc,
        "OBS-6 — Faltante de ET de Hormigón Armado",
        "El TdR exige tres ET separadas: P22-ET-00-010-101-0 (Movimiento de "
        "Tierras), P22-ET-00-010-102-0 (Hormigón Armado) y P22-ET-00-010-103-0 "
        "(Estructura Metálica). El programa muestra dos paquetes: “ET "
        "OOCC” y “ET Estructuras”. Clarificar si “ET OOCC” fusiona "
        "Movimiento de Tierras con Hormigón Armado (separarlas) o si la "
        "P22-ET-00-010-102-0 falta del cronograma.",
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Adicionalmente, registramos como antecedente que el programa llegó "
        "dos días hábiles después del compromiso de la minuta MI-001 ítem "
        "1.12 (jue 07-may; recibido lun 11-may)."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # REV C DEBE INCORPORAR
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("La Rev C debe incorporar: ").bold = True
    para.add_run(
        "(a) fecha de inicio en lun 04-may-2026; (b) Rev 0 de planos, ET y "
        "cubicaciones al lun 01-jun-2026; (c) ciclo colapsado a A → B → B.1 → "
        "0; (d) hitos H0 a H5 visibles en el Gantt; (e) fundación CIP "
        "independiente del contenedor; (f) tres ET identificadas como "
        "entregables independientes."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SOLICITUD REV C
    # =========================================================================
    para = doc.add_paragraph(
        "Agradecemos recibir la Rev C el "
    )
    para.add_run("jueves 14 de mayo de 2026").bold = True
    para.add_run(
        " (2 días hábiles desde el envío de este correo). El alcance acotado "
        "del ajuste, que consiste en re-secuenciar el cronograma sin nuevos "
        "paquetes de ingeniería, permite una cadencia algo más breve que los "
        "3 días hábiles que la Sección 8 del TdR fijó para el primer "
        "programa."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # CIERRE
    # =========================================================================
    para = doc.add_paragraph("Quedamos atentos a sus comentarios.")
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

    # =========================================================================
    # IDIOMA es-CL — última operación antes de guardar
    # =========================================================================
    fijar_idioma_documento(doc, LANG)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")
    print(f"Idioma del documento: {LANG}")


if __name__ == "__main__":
    crear_correo()
