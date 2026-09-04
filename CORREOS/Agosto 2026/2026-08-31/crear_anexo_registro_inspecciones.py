#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anexo del correo a Bureau Veritas Chile del 31-Ago-2026.

Consolida las nueve jornadas atestiguadas (BVM-IR001 a BVM-IR009) contrastadas
contra la ingenieria aprobada, el estado de las seis peticiones del 21-Ago y los
puntos de control documental que quedan abiertos.

Codigo: ADASA-BV-REGISTRO-INSPECCIONES-Rev0, siguiendo la convencion propia de este
frente (la Guia del Paquete es ADASA-BV-PAQUETE-INSPECCION-Rev1). NO se usa la serie
P22-IT-06, que es documentacion interna de ADASA.

REGLA DURA: este documento va a Bureau Veritas y NO NOMBRA AL FABRICANTE. Se escribe
"el taller" o "el fabricante". Barrido pre-emision: grep -i "bw.water" -> 0.

Espanol de Chile. Template ADASA. Estado: BORRADOR.
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import crear_documento_adasa, add_simple_table  # noqa: E402
import docx_metadata  # noqa: E402
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "Anexo_Registro_Inspecciones_IR001_IR009.docx")
LANG = "es-CL"


def add_para(doc, text, size=11):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    return p


def add_bold_lead(doc, lead, body, size=11):
    p = doc.add_paragraph()
    rl = p.add_run(lead)
    rl.bold = True
    rl.font.name = "Arial"
    rl.font.size = Pt(size)
    rb = p.add_run(body)
    rb.font.name = "Arial"
    rb.font.size = Pt(size)
    return p


def add_bullet(doc, text, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    r = p.add_run("•  " + text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    return p


def _set_lang(rPr, lang):
    el = rPr.find(qn("w:lang"))
    if el is None:
        el = OxmlElement("w:lang")
        rPr.append(el)
    el.set(qn("w:val"), lang)
    el.set(qn("w:eastAsia"), lang)
    el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(doc, lang=LANG):
    for p in doc.paragraphs:
        for r in p.runs:
            _set_lang(r._element.get_or_add_rPr(), lang)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        _set_lang(r._element.get_or_add_rPr(), lang)


def crear():
    crear_documento_adasa(
        titulo="REGISTRO DE INSPECCIONES DE TALLER — BVM-IR001 A BVM-IR009",
        codigo="ADASA-BV-REGISTRO-INSPECCIONES-Rev0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=False,
    )
    doc = Document(OUTPUT)

    # La portada del template arma el mes con la configuracion regional del equipo, que
    # aqui esta en ingles y deja "Antofagasta, August 2026" en un documento en espanol.
    # Se corrige en sitio, sin tocar la skill.
    for p in doc.paragraphs:
        if p.text.strip().startswith("Antofagasta,"):
            for r in p.runs:
                r.text = ""
            if p.runs:
                p.runs[0].text = "Antofagasta, agosto de 2026"
            else:
                p.add_run("Antofagasta, agosto de 2026")
            break

    # limpiar el placeholder del template
    borrar, hallado = [], False
    for p in doc.paragraphs:
        if p.style and p.style.name == "Heading 1" and not hallado:
            hallado = True
        if hallado:
            borrar.append(p)
    for p in borrar:
        p._element.getparent().remove(p._element)

    # 1. PROPOSITO
    doc.add_heading("PROPÓSITO", level=1)
    add_para(doc,
        "Este anexo consolida las nueve jornadas de inspección de taller atestiguadas "
        "entre el 28 de julio y el 28 de agosto de 2026, contrastadas contra la "
        "ingeniería aprobada por ADASA. Se emite como base común para la programación "
        "de las jornadas siguientes y para el cierre de los puntos planteados el 21 de "
        "agosto.")
    add_para(doc,
        "Las casillas de resultado de cada informe se verificaron por representación "
        "gráfica del formulario y no por extracción de texto, dado que el formulario "
        "GM-SI-101 INSP002-En Rev 3.1 dibuja sus casillas como elementos vectoriales.")

    # 2. JORNADAS
    doc.add_heading("JORNADAS ATESTIGUADAS", level=1)
    add_simple_table(doc, [
        ("N°", "Informe", "Fecha", "Alcance ejecutado", "Resultado del informe"),
        ("1", "BVM-IR001", "28-Jul-2026",
         "Inspección visual y dimensional del material y PMI sobre el 10 % mínimo del Plan de Inspección y Ensayos",
         "Satisfactorio"),
        ("2", "BVM-IR002", "07-Ago-2026",
         "Fabricación de carretes, líquidos penetrantes en raíz y peineta, marco del skid, revisión de WPS y calificación de soldadores",
         "Satisfactorio"),
        ("3", "BVM-IR003", "13-Ago-2026",
         "Preparación de pintura y visual del marco y del contenedor",
         "Satisfactorio"),
        ("4", "BVM-IR004", "14-Ago-2026",
         "Examen visual y dimensional de carretes. El ensayo de alta presión no se ejecutó",
         "Satisfactorio"),
        ("5", "BVM-IR005 Rev 01", "20-Ago-2026",
         "Ensayo de presión, dos carretes de super dúplex",
         "No satisfactorio"),
        ("6", "BVM-IR006 Rev 01", "21-Ago-2026",
         "Ensayo de presión, dos carretes de super dúplex",
         "No satisfactorio"),
        ("7", "BVM-IR007", "24-Ago-2026",
         "Perfil tras granallado y espesor de película seca del marco del skid",
         "Satisfactorio (ver observación)"),
        ("8", "BVM-IR008", "27-Ago-2026",
         "Ensayo de presión de baja, carrete de PVC",
         "Satisfactorio"),
        ("9", "BVM-IR009", "28-Ago-2026",
         "Ensayo de presión de baja, carrete de PVC",
         "Satisfactorio"),
    ])

    # 3. ENSAYOS DE PRESION
    doc.add_heading("ENSAYOS DE PRESIÓN CONTRA LA INGENIERÍA APROBADA", level=1)
    add_para(doc,
        "La presión de ensayo de cada línea es 1,5 veces su presión de diseño, según la "
        "columna de hidrostática de la Line List P22-LI-09-009-003 Rev 0, aprobada por "
        "ADASA en Código 1.")
    add_simple_table(doc, [
        ("Línea", "Informe", "Diseño barG", "Exigida barG", "Aplicada barG", "Estado"),
        ("DA-SSD-DN100-09-003", "BVM-IR005", "60", "90", "90", "Conforme"),
        ("CP-SSD-DN100-09-014", "BVM-IR005", "80", "120", "7,5", "No califica"),
        ("CP-SSD-DN80-09-015", "BVM-IR006", "90", "135", "7,5", "No califica"),
        ("CP-SSD-DN80-09-044", "BVM-IR006", "80", "120", "7,5", "No califica"),
        ("DA-PVC-DN100-09-002", "BVM-IR008", "5", "7,5", "7,6", "Conforme"),
        ("DA-PVC-DN100-09-001", "BVM-IR009", "5", "7,5", "7,5", "Conforme"),
    ])
    add_para(doc,
        "De las once líneas de super dúplex del proyecto, una tiene ensayo conforme, "
        "tres deben repetirse y siete no se han ensayado. La fila 5.2 del Plan de "
        "Inspección y Ensayos P22-BA-09-000-004 Rev 0 es Punto de Detención y sigue "
        "abierta.")

    # 4. ESTADO DE LAS PETICIONES DEL 21-AGO
    doc.add_heading("ESTADO DE LOS PUNTOS PLANTEADOS EL 21 DE AGOSTO", level=1)
    add_simple_table(doc, [
        ("Punto", "Estado", "Constancia"),
        ("Reemitir el BVM-IR005 y el BVM-IR006 con la presión de diseño de la Line List",
         "Cerrado",
         "La tabla de la sección E1 declara 80/120, 90/135 y 80/120, y las tres líneas quedan como no satisfactorias"),
        ("Contrastar cada ensayo contra el P&ID y la Line List antes de firmar",
         "Cerrado",
         "El P&ID P22-DWG-09-009-002 Rev D y la Line List entran a la sección B de los dos informes reemitidos"),
        ("Incorporar el P&ID y la Line List a la documentación de referencia de todo informe de presión",
         "Cerrado",
         "BVM-IR005 Rev 01, BVM-IR006 Rev 01, BVM-IR008 y BVM-IR009"),
        ("Fotografiar la marca de identificación del carrete en cada registro",
         "Cerrado",
         "Los informes del 27 y del 28 de agosto incorporan la fotografía de la identificación del carrete"),
        ("Levantar una No Conformidad que cubra los tres ensayos",
         "Abierto",
         "La sección G de los dos informes reemitidos permanece en N/A y la casilla de No Conformidades abiertas está marcada No"),
        ("Constancia de que la fila 5.2 es Punto de Detención y de que la retención sigue vigente",
         "Sin constancia",
         "Ningún informe posterior lo menciona"),
    ])

    # 5. CONTROL DOCUMENTAL
    doc.add_heading("PUNTOS DE CONTROL DOCUMENTAL", level=1)
    add_bold_lead(doc, "Contradicción interna de los informes reemitidos. ",
        "El BVM-IR005 Rev 01 y el BVM-IR006 Rev 01 marcan la casilla de resultado "
        "No Satisfactorio, que el propio formulario define como No Conformidad levantada "
        "durante la inspección, y tres líneas más abajo marcan No en la casilla de No "
        "Conformidades abiertas, con la sección G en N/A. Solicitamos conciliar ambas "
        "casillas emitiendo la No Conformidad y referenciándola en la sección G.")
    add_bold_lead(doc, "Identificación de la revisión. ",
        "Los dos informes reemitidos conservan Revisión N° 0 en su campo de revisión: la "
        "revisión 01 existe solo en el nombre del archivo. El dossier de fabricación no "
        "podrá distinguir cuál versión gobierna.")
    add_bold_lead(doc, "Número de informe en páginas interiores. ",
        "El BVM-IR006 Rev 01, el BVM-IR007 y el BVM-IR008 llevan BVM-IR005-20082026 en "
        "el encabezado de páginas interiores. En el BVM-IR007 son las cinco páginas "
        "interiores, de modo que solo la portada lleva su propio número.")
    add_bold_lead(doc, "BVM-IR007, casilla de resultado. ",
        "El informe marca Satisfactorio sin comentarios mientras su propio resumen "
        "declara el resultado no satisfactorio y su sección E1 registra que la parte "
        "inferior del marco no alcanza los 355 micrones exigidos. Deja además las "
        "casillas de No Conformidades y de punch list en No.")
    add_bold_lead(doc, "Certificado de calibración del BVM-IR008. ",
        "El archivo adjunto es idéntico al del BVM-IR009 y contiene el certificado "
        "PSPP-26605336, mientras su nombre declara PSPP-26605366. Los dos informes "
        "declaran en su sección D los manómetros PSPP-26605336 y PSPP-26605337, y el "
        "certificado del segundo no viene adjunto en ninguna de las dos jornadas.")

    # 6. DESEMPENO RECONOCIDO
    doc.add_heading("DESEMPEÑO EN TERRENO", level=1)
    add_para(doc,
        "El inspector asistió a las nueve jornadas, firmó y timbró los registros de "
        "ensayo, revisó los certificados de calibración y documentó los escalones de "
        "presión con su hora. La instrumentación está calibrada por laboratorio "
        "acreditado y con trazabilidad vigente. Los dos ensayos de baja presión del 27 y "
        "del 28 de agosto están correctamente ejecutados y correctamente registrados.")

    # 7. HISTORIAL
    doc.add_heading("HISTORIAL DEL DOCUMENTO", level=1)
    add_simple_table(doc, [
        ("Rev", "Fecha", "Descripción"),
        ("0", "31-Ago-2026",
         "Primera emisión. Consolida las jornadas BVM-IR001 a BVM-IR009 y el estado de "
         "los puntos planteados el 21 de agosto de 2026."),
    ])

    fijar_idioma_documento(doc, LANG)

    docx_metadata.apply_core_properties(
        doc,
        title="Registro de inspecciones de taller - BVM-IR001 a BVM-IR009",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Módulo RO Segunda Etapa - Taltal - registro consolidado de "
                "inspecciones de taller",
        comments="Anexo del correo a Bureau Veritas del 31 de agosto de 2026.",
        language="es-CL",
    )
    doc.save(OUTPUT)
    docx_metadata.fix_app_xml(OUTPUT, company="Aguas de Antofagasta S.A.")
    print("Anexo generado:", OUTPUT)


if __name__ == "__main__":
    crear()
