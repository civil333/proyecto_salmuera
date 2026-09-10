#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correo a L&A Ingenieria y Proyectos: comentarios por plano a las entregas de las cartas
067-032-032-COR-TT-014 (implantacion general, 07-09-2026) y 067-032-032-COR-TT-015
(movimiento de tierra, 08-09-2026).

El cuerpo es espejo 1:1 de los cuatro PDF comentados que van adjuntos: mismos
identificadores, misma instruccion, por plano y lamina. Los PDF se generan con
generar_cc_adasa_entrega14.py, en la carpeta COMENTARIOS del P22-TM-00-010-005-0.

Reply-To al hilo de la carta 067-032-032-COR-TT-015.
Idioma del documento fijado en es-CL.
"""
import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "2026-09-09_LyA-Comentarios-Planos.docx")
CONTACTO = "Luis Rivera"
LANG = "es-CL"


def aplicar_arial(p, size=11):
    for r in p.runs:
        r.font.name = "Arial"; r.font.size = Pt(size)


def aplicar_arial_table(t, size=9):
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = "Arial"; r.font.size = Pt(size)


def _lang(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang"); rPr.append(el)
    el.set(qn("w:val"), lang); el.set(qn("w:eastAsia"), lang); el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    try:
        _lang(doc.styles["Normal"].element.get_or_add_rPr(), lang)
    except KeyError:
        pass
    for p in doc.paragraphs:
        for r in p.runs:
            _lang(r._element.get_or_add_rPr(), lang)
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        _lang(r._element.get_or_add_rPr(), lang)


def tabla(doc, headers, rows, anchos=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(headers):
        c = t.rows[0].cells[j]; c.text = h
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
    for i, fila in enumerate(rows, start=1):
        for j, v in enumerate(fila):
            t.rows[i].cells[j].text = str(v)
    if anchos:
        # python-docx no fija el ancho por si solo: hay que apagar el autofit, declarar
        # el layout fijo, reescribir la grilla de la tabla y ademas poner el ancho en
        # cada celda. Sin la grilla, Word y LibreOffice reparten las columnas a su gusto.
        t.autofit = False
        tblPr = t._tbl.tblPr
        layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed")
        tblPr.append(layout)
        tblW = OxmlElement("w:tblW")
        tblW.set(qn("w:w"), str(int(sum(anchos) * 1440))); tblW.set(qn("w:type"), "dxa")
        tblPr.append(tblW)
        grid = t._tbl.find(qn("w:tblGrid"))
        if grid is not None:
            t._tbl.remove(grid)
        grid = OxmlElement("w:tblGrid")
        for w in anchos:
            gc = OxmlElement("w:gridCol"); gc.set(qn("w:w"), str(int(w * 1440)))
            grid.append(gc)
        t._tbl.insert(list(t._tbl).index(tblPr) + 1, grid)
        for row in t.rows:
            for j, w in enumerate(anchos):
                row.cells[j].width = Inches(w)
    # el encabezado se repite si la tabla corta de pagina
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true")
    trPr.append(th)
    aplicar_arial_table(t, 9)
    return t


def parrafo(doc, texto, size=11, bold=False):
    p = doc.add_paragraph(); r = p.add_run(texto); r.bold = bold
    aplicar_arial(p, size); return p


def vineta(doc, texto):
    p = doc.add_paragraph(style="List Paragraph")
    p.paragraph_format.left_indent = Inches(0.3)
    p.add_run("• " + texto)
    aplicar_arial(p, 11); return p


# ------------------------------------------------------------------ los adjuntos
# El correo NO repite los comentarios: para eso van los planos comentados. Aqui solo
# el rango de identificadores de cada adjunto y su materia en una linea.
ANCHOS = [2.55, 1.30, 3.05]

ADJUNTOS = [
    ["P22-DWG-00-001-001-1-LAM 1_CC_ADASA.pdf", "OBS-01 a OBS-03",
     "Excavación de la zona del sistema CIP, del contenedor, y dos excavaciones que el "
     "cuadro no recoge"],
    ["P22-DWG-00-001-001-1-LAM 2_CC_ADASA.pdf", "OBS-04 y OBS-05",
     "Fondo de excavación del estanque TK-06-001 y de la fosa TK-06-004"],
    ["P22-DWG-00-002-003_1 LAM1_CC_ADASA.pdf", "OBS-06",
     "Cuadro de excavación del contenedor"],
    ["P22-DWG-00-002-007_1 LAM1_CC_ADASA.pdf", "OBS-07",
     "Cuadro de excavación de la zona del sistema CIP"],
]


def crear_correo():
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Inches(0.8)

    campos = [
        ("Fecha:", "9 de septiembre de 2026"),
        ("De:", f"{CONTACTO} — Aguas Antofagasta S.A. (lrivera@aguasantofagasta.cl)"),
        ("Para:", "Pablo Castillo (pcastillo@lyaingenieria.cl); Yohana Rodríguez Flores "
                  "(yrodriguez@aguasantofagasta.cl)"),
        ("CC:", "Nicolás Yanes, Cristian Sánchez, Jesús Alarcón, J. Cid (L&A); "
                "Dio Documentos, Luciano Méndez Huidobro, Víctor Gutiérrez Aqueveque, "
                "Jorge Guevara Lizana, Manuel Aguilera Orellana (ADASA)"),
        ("Asunto:", "ID Módulo RO 2da Etapa para Salmuera / TT-015 — Comentarios al "
                    "Movimiento de Tierra revisión 1, reemisión al viernes 11"),
        ("Ref:", "Cartas 067-032-032-COR-TT-014 del 07-09-2026 y 067-032-032-COR-TT-015 "
                 "del 08-09-2026"),
    ]
    for et, val in campos:
        p = doc.add_paragraph(); r = p.add_run(f"{et} "); r.bold = True; p.add_run(val)
        aplicar_arial(p, 11)

    doc.add_paragraph()
    parrafo(doc, "Estimado Pablo:")
    doc.add_paragraph()

    parrafo(doc,
        "Recibimos las dos entregas. La Implantación General P22-DWG-00-002-001 revisión 1 queda "
        "aceptada sin comentarios y ya incorporamos sus coordenadas de replanteo a la ingeniería "
        "vigente.")
    doc.add_paragraph()

    parrafo(doc,
        "Sobre el Movimiento de Tierra P22-DWG-00-001-001 revisión 1 les adjunto los planos "
        "comentados. Las siete observaciones son discrepancias entre planos vigentes: una misma "
        "excavación, o una misma cota, declarada con dos valores distintos. Adjunto también los dos "
        "planos de fundaciones donde están las cifras que no calzan.")
    doc.add_paragraph()

    tabla(doc, ["Adjunto", "Observaciones", "Materia"], ADJUNTOS, ANCHOS)
    doc.add_paragraph()

    parrafo(doc,
        "Les pido resolver las siete observaciones (OBS-01 a OBS-07) y reemitir en cada caso la "
        "lámina que corresponda corregir, de manera que cada excavación quede con una sola cifra y "
        "cada fondo con una sola cota.")
    doc.add_paragraph()

    parrafo(doc,
        "La obra está por iniciarse y estas cifras rigen la excavación, por lo que necesitamos la "
        "reemisión el viernes 11 de septiembre. Si algún punto no alcanza para esa fecha, avísenme "
        "hoy cuál es y lo vemos por separado.")
    doc.add_paragraph()

    parrafo(doc, "Quedo atento.")
    doc.add_paragraph()

    parrafo(doc, "Saludos Cordiales,")
    doc.add_paragraph()
    parrafo(doc, CONTACTO)
    parrafo(doc, "Departamento de Ingeniería y Optimización (DIO)")
    parrafo(doc, "Aguas Antofagasta S.A. — Grupo EPM")
    parrafo(doc, "lrivera@aguasantofagasta.cl")

    doc.core_properties.author = "Luis Rivera Gonzalez"
    doc.core_properties.company = "Aguas Antofagasta"
    doc.core_properties.comments = ("Comentarios por plano al Movimiento de Tierra revision 1, "
                                   "con los CC_ADASA adjuntos y reemision pedida al viernes 11")
    fijar_idioma_documento(doc)
    doc.save(OUTPUT_FILE)
    print(f"OK: {os.path.basename(OUTPUT_FILE)}")


if __name__ == "__main__":
    crear_correo()
