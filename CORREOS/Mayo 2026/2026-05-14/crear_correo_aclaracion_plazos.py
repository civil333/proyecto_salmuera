#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo interno a Victor Gutierrez (Jefe Depto. Proyectos Desalacion ADASA) —
aclaracion sobre plazos de entrega y oportunidad del Estado de Pago EP-1 + EP-2.

Fecha: 14 de mayo de 2026.

Configuracion: idioma del documento Word fijado en es-CL (CLAUDE.md Seccion 3.4
v6.8) para que Word aplique correccion ortografica en espanol.
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
    "2026-05-14_Aclaracion-Plazos-EP1-EP2.docx",
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
    """Configura es-CL en todos los runs del documento y en el estilo Normal."""
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


def add_table_with_header(doc, headers, rows, bold_col=None):
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
            cell = table.rows[i].cells[j]
            cell.text = str(value)
            if bold_col is not None and j == bold_col:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True
    aplicar_arial_table(table, size=10)
    return table


# ---------------------------------------------------------------------------
# Cuerpo del correo
# ---------------------------------------------------------------------------
def crear_correo():
    doc = Document()

    # Margenes 0,8" para que las tablas quepan comodas
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # =========================================================================
    # ENCABEZADO
    # =========================================================================
    fields = [
        ("Fecha:", "14 de mayo de 2026"),
        ("De:", f"{CONTACTO} — DIO ADASA (Aguas de Antofagasta S.A.)"),
        (
            "Para:",
            "Víctor Gutiérrez Aqueveque — Jefe Depto. Proyectos Desalación, ADASA",
        ),
        ("CC:", "(a definir por destinatario)"),
        (
            "Asunto:",
            "PD Taltal — Aclaración plazos de suministros y oportunidad del Estado "
            "de Pago EP-1 + EP-2",
        ),
        (
            "Ref:",
            "Contrato C-4300 / BAE 12803 / Baseline Schedule 05-Mar-2026 / Tracker "
            "BW Water SEMANA 11-05-26",
        ),
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
    para = doc.add_paragraph("Estimado Víctor:")
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "El correo de Eduardo Yamauchi del 13-mayo-2026 confirma la emisión de "
        "la Orden de Compra de las Membranas RO (LG) y compromete la emisión de "
        "la Orden de Compra de los Filtros Cartucho (Fil-Trek) dentro de mayo. "
        "La consulta planteada se aborda separadamente en tres dimensiones: el "
        "plazo físico de fabricación y traslado hasta sitio Taltal, una alerta "
        "sobre el deslizamiento de Fedco detectado en el último tracker, y el "
        "hito de pago contractual asociado al avance del proyecto."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SECCION 1 — DISTINCION EX-WORKS PENANG VS LLEGADA A SITIO
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "1. Distinción entre Ex-Works Penang y llegada a sitio Taltal"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "El baseline contractual del 05-marzo-2026 establece como fecha de "
        "embarque “Ex-Works Malasia” el 03-agosto-2026. Esa fecha corresponde a "
        "la salida desde la planta de fabricación de BW Water en Penang, no a la "
        "llegada al sitio de obra en Taltal. Entre Penang y el sitio existen "
        "aproximadamente seis semanas y media de tránsito marítimo, despacho "
        "aduanero en Chile y transporte terrestre Antofagasta–Taltal, que el "
        "propio cronograma BW Water ya incorpora en sus hitos siguientes:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    add_table_with_header(
        doc,
        headers=["Hito del baseline 05-Mar-2026", "Fechas", "Ubicación"],
        rows=[
            ("Factory Acceptance Test (FAT)", "25-Jul a 01-Ago 2026", "Penang, Malasia"),
            ("Embarque Ex-Works", "02-Ago a 03-Ago 2026", "Salida Penang"),
            ("Sistema listo para despacho (Ex-work)", "03-Ago 2026", "Penang"),
            (
                "Site Supervision & Commissioning Supervision",
                "18-Sep a 08-Oct 2026",
                "Sitio Taltal",
            ),
            ("Operator Training", "09-Oct a 17-Oct 2026", "Sitio Taltal"),
            ("Final Documentation & Close out", "18-Oct a 16-Nov 2026", "—"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "En consecuencia, el montaje y la puesta en marcha en obra arrancan en la "
        "segunda quincena de septiembre. Comprar en mayo y tener equipo montado "
        "en agosto no es alcanzable con el baseline vigente. La fecha de agosto "
        "corresponde a la salida desde fábrica."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SECCION 2 — LEAD TIMES DEL TRACKER SEMANA 11-05-26
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "2. Lead times declarados en el tracker BW Water SEMANA 11-05-26"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "Del último tracker oficial emitido por BW Water (fecha de corte "
        "12-mayo-2026), los siete equipos de la Cláusula 31 BAE 12803 que "
        "gatillan el hito EP-2 figuran con los siguientes valores. Status se "
        "reporta según la leyenda del propio tracker: C = Committed (PO emitida, "
        "ExWorks confirmado), E = Enabled (Eng Code 1/2, PO pendiente), "
        "D = Delayed."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    add_table_with_header(
        doc,
        headers=[
            "Equipo",
            "Vendor",
            "Fecha OC",
            "Arribo Penang previsto",
            "Lead time declarado",
            "Status",
        ],
        rows=[
            (
                "Bomba RO de Alta Presión",
                "Fedco",
                "15-May-2026",
                "03-Ago-2026",
                "10–12 semanas",
                "D – Delayed",
            ),
            (
                "Turbocharger Feed",
                "Fedco",
                "15-May-2026",
                "03-Ago-2026",
                "10–12 semanas",
                "C",
            ),
            (
                "Turbocharger Interstage",
                "Fedco",
                "15-May-2026",
                "03-Ago-2026",
                "10–12 semanas",
                "C",
            ),
            (
                "Pressure Vessels",
                "Protec Arisawa",
                "20-Abr-2026",
                "29-May-2026",
                "5–6 semanas",
                "C",
            ),
            (
                "Heater CIP",
                "Quantic Logic",
                "26-Mar-2026",
                "26-May-2026",
                "8 semanas",
                "C",
            ),
            (
                "Filtros Cartucho RO",
                "Fil-Trek",
                "05-May-2026",
                "TBC (en negociación)",
                "TBC",
                "E",
            ),
            (
                "Filtros Cartucho CIP",
                "Fil-Trek",
                "14-May-2026",
                "TBC (en negociación)",
                "TBC",
                "E",
            ),
            (
                "Membranas RO",
                "LG",
                "13-May-2026 (correo Yamauchi)",
                "Sin confirmar vendor",
                "Sin confirmar",
                "E",
            ),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Cinco equipos ya están firmes con fechas vendor. Tres siguen pendientes "
        "de confirmación del proveedor: los dos Filtros Cartucho de Fil-Trek (en "
        "negociación de lead time) y las Membranas RO de LG (PO emitida según "
        "comunicación de Eduardo Yamauchi del 13-mayo, unpriced PDF aún pendiente "
        "de envío). El comentario “≤17-Jul” para Fil-Trek que circuló en el "
        "correo del 05-mayo fue una solicitud ADASA al proveedor, no un "
        "compromiso documental de Fil-Trek; sigue abierto."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SECCION 3 — ALERTA FEDCO SLIP
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "3. Alerta — Fedco: slip de 25 días en PO y 16 días en EAP entre las "
        "dos últimas semanas"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "Comparando el tracker SEMANA 04-05-26 con el tracker SEMANA 11-05-26, "
        "las tres POs de Fedco (Bomba RO Alta Presión, Turbocharger Feed, "
        "Turbocharger Interstage) se desplazaron de la siguiente forma:"
    )
    aplicar_arial(para)
    doc.add_paragraph()

    add_table_with_header(
        doc,
        headers=["Campo", "SEMANA 04-05-26", "SEMANA 11-05-26", "Slip"],
        rows=[
            ("Fecha OC", "20-Abr-2026", "15-May-2026", "+25 días"),
            ("Arribo Penang previsto", "18-Jul-2026", "03-Ago-2026", "+16 días"),
            ("Status Bomba RO", "C – Committed", "D – Delayed", "Reclasificada"),
        ],
    )
    doc.add_paragraph()

    para = doc.add_paragraph(
        "El comentario del tracker explica el cambio como “Technical discussion "
        "with supplier took longer than expected”. La consecuencia operacional "
        "es relevante: la nueva EAP del 03-agosto coincide con el embarque "
        "EXW del baseline contractual (también el 03-agosto). El FAT del sistema "
        "integrado, programado entre el 25-julio y el 01-agosto, se ejecuta "
        "antes de que los tres equipos Fedco lleguen a Penang."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "Esta situación admite tres lecturas posibles, ninguna de las cuales "
        "BW Water ha planteado formalmente: (a) shipping se atrasa para "
        "acomodar un FAT post-arribo Fedco; (b) el sistema se embarca con un "
        "FAT parcial que excluye los componentes Fedco; (c) Fedco se prueba "
        "individualmente fuera del sistema integrado. Conviene solicitar "
        "aclaración escrita a BW Water sobre el plan FAT para los componentes "
        "Fedco. La aclaración FAT corre por canal técnico y no condiciona el "
        "cierre del Estado de Pago EP-2, que es documental y procede con las "
        "POs vigentes; ambas líneas se tramitan en paralelo."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SECCION 4 — NATURALEZA DEL HITO EP-2
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run(
        "4. Naturaleza del hito EP-2 — pago documental, no entrega física"
    ).bold = True
    aplicar_arial(para)

    para = doc.add_paragraph(
        "El hito EP-2 equivale al 15 % del contrato. Se gatilla por la emisión "
        "de las siete Órdenes de Compra listadas en la Cláusula 31 de las BAE "
        "12803, evidenciadas mediante los PDFs sin precio (unpriced PO) que BW "
        "Water entrega a ADASA. Tomado en bundle con el EP-1 (10 % por "
        "aprobación formal de la ingeniería), totaliza 25 % del contrato. La "
        "cláusula no condiciona el pago a la llegada física de los equipos al "
        "sitio."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    para = doc.add_paragraph(
        "En la primera semana de junio, una vez recibidos los unpriced PDFs "
        "pendientes (Membranas LG según compromiso Yamauchi del 13-may; "
        "Filtros Cartucho Fil-Trek CIP con PO emitida 14-may según tracker), "
        "ADASA propondrá a BW Water tramitar el Estado de Pago en bundle "
        "EP-1 + EP-2 por el 25 % del contrato. El equipo, mientras tanto, "
        "seguirá su trayectoria normal de fabricación en Penang y arribará a "
        "sitio Taltal a mediados de septiembre."
    )
    aplicar_arial(para)
    doc.add_paragraph()

    # =========================================================================
    # SECCION 5 — RESUMEN PARA ARRIBA
    # =========================================================================
    para = doc.add_paragraph()
    para.add_run("5. Resumen para arriba").bold = True
    aplicar_arial(para)

    bullets = [
        "El supuesto de “comprar en mayo, montar en agosto” no se sostiene "
        "contra el baseline contractual: embarque desde Penang el 03-agosto, "
        "arribo a sitio Taltal a partir del 18-septiembre, puesta en marcha "
        "entre el 18-septiembre y el 08-octubre.",
        "Fedco presenta un slip silencioso entre los dos últimos trackers: PO "
        "desplazada 25 días (20-abril → 15-mayo) y EAP desplazada 16 días "
        "(18-julio → 03-agosto). La nueva EAP coincide con el embarque EXW y "
        "comprime el FAT. Falta plan formal de BW Water sobre cómo se ejecuta "
        "el FAT para los componentes Fedco.",
        "Filtros Cartucho de Fil-Trek y Membranas RO de LG figuran en el "
        "tracker con EAP y lead time pendientes de confirmación del vendor. No "
        "hay todavía compromiso documental sobre la fecha de arribo a Penang "
        "de estos tres equipos.",
        "ADASA propondrá a BW Water tramitar el bundle EP-1 + EP-2 en la "
        "primera semana de junio. Es un hito de pago documental gatillado por "
        "las Órdenes de Compra registradas en la Cláusula 31, independiente de "
        "la entrega física en obra y desacoplado de la aclaración técnica "
        "sobre el FAT Fedco, que avanza por canal separado.",
    ]
    for texto in bullets:
        para = doc.add_paragraph()
        para.paragraph_format.left_indent = Inches(0.25)
        para.add_run("• ")
        para.add_run(texto)
        aplicar_arial(para)

    doc.add_paragraph()

    # =========================================================================
    # CIERRE
    # =========================================================================
    para = doc.add_paragraph(
        "Quedo atento a cualquier antecedente adicional que sea útil para el "
        "reenvío hacia gerencia."
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

    # =========================================================================
    # IDIOMA es-CL — ultima operacion antes de guardar
    # =========================================================================
    fijar_idioma_documento(doc, LANG)

    doc.save(OUTPUT_FILE)
    print(f"Correo generado: {OUTPUT_FILE}")
    print(f"Idioma del documento: {LANG}")


if __name__ == "__main__":
    crear_correo()
