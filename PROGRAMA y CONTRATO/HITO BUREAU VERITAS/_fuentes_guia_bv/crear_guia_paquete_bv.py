#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Guia del Paquete de Inspeccion para Bureau Veritas (espanol).
Template ADASA. Documento interno de coordinacion ADASA -> Bureau Veritas
(NO contiene costo BV, posicion sobre atrasos ni decisiones internas KVC).

Rev 1 (21-Jul-2026): actualizado a ultimas versiones tras TM N27/N28.

Fuente unica del contenido: este script (hardcoded).
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import crear_documento_adasa, add_simple_table  # noqa: E402
import docx_metadata  # noqa: E402  (metadatos limpios, global sec. 2.3)
from docx import Document  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "GUIA_PAQUETE_INSPECCION_BV.docx")


def add_para(doc, text, size=11):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    return p


def add_bold_lead(doc, lead, body, size=11):
    p = doc.add_paragraph()
    rl = p.add_run(lead); rl.bold = True; rl.font.name = "Arial"; rl.font.size = Pt(size)
    rb = p.add_run(body); rb.font.name = "Arial"; rb.font.size = Pt(size)
    return p


def add_bullet(doc, text, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    r = p.add_run("•  " + text)
    r.font.name = "Arial"; r.font.size = Pt(size)
    return p


def crear():
    crear_documento_adasa(
        titulo="GUÍA DEL PAQUETE DE INSPECCIÓN DE TALLER — BUREAU VERITAS",
        codigo="ADASA-BV-PAQUETE-INSPECCION-Rev1",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )
    doc = Document(OUTPUT)

    # limpiar placeholder
    borrar, hallado = [], False
    for p in doc.paragraphs:
        if p.style and p.style.name == "Heading 1" and not hallado:
            hallado = True
        if hallado:
            borrar.append(p)
    for p in borrar:
        p._element.getparent().remove(p._element)

    # 1. PROPOSITO Y ALCANCE
    doc.add_heading("PROPÓSITO Y ALCANCE", level=1)
    add_para(doc,
        "ADASA designó a Bureau Veritas como Tercero Inspector, conforme a las "
        "Bases Administrativas Especiales (Cláusula 37.1 — Intervención de "
        "Tercero Inspector), para la inspección de taller del Módulo RO Segunda "
        "Etapa fabricado por BW Water en Penang, Malasia. El alcance comprende "
        "seis visitas semanales de acompañamiento de aseguramiento de calidad "
        "durante la fabricación (tres visitas por semana) y el atestiguamiento "
        "del Factory Acceptance Test (FAT).")
    add_para(doc,
        "El documento gobernante de aceptación es el Plan de Inspección y "
        "Ensayos (P22-BA-09-000-004), Rev 0, aprobado por ADASA (Código 1). El "
        "inspector ejecuta y atestigua contra sus Puntos de Espera (Hold, H) y "
        "Puntos de Testimonio (Witness, W). Este paquete reúne, en su revisión "
        "vigente, la base contractual, el Plan de Inspección y Ensayos, los "
        "procedimientos de calidad, la ingeniería de referencia y el "
        "cronograma de fabricación.")
    add_para(doc,
        "Este paquete contiene los procedimientos, planos y datasheets en su "
        "revisión vigente. Los registros y reportes de fabricación "
        "(certificados de material y trazabilidad, reportes de PMI, END, "
        "hidrostática y DFT, certificados de calibración, informes de "
        "inspección y registros de preservación, embalaje y liberación de "
        "despacho) se generan durante la fabricación y se consolidan en el "
        "Manufacturer Record Book (MRB); se revisan en cada visita y se "
        "entregan en el dossier final, y no forman parte de este envío inicial.")
    add_para(doc,
        "El calendario detallado de las visitas y el protocolo de notificación "
        "se encuentran en la Nota Técnica P22-NT-09-000-002-0, incluida en la "
        "carpeta 00 de este paquete.")

    # 2. ORGANIZACION
    doc.add_heading("ORGANIZACIÓN DEL PAQUETE", level=1)
    add_para(doc, "El paquete se organiza en las siguientes carpetas:")
    for t in [
        "00_GUIA_Y_ALCANCE — esta guía y la Nota Técnica P22-NT-09-000-002-0 "
        "(designación y calendario).",
        "01_CONTRACTUAL — Especificación Técnica, Bases Administrativas "
        "Especiales, PIE Base y Oferta Técnica de BW Water Rev 1.",
        "02_PLAN_INSPECCION_ITP — Plan de Inspección y Ensayos Rev 0 (aprobado).",
        "03_PROCEDIMIENTOS_QA_APROBADOS — procedimientos de calidad en Código "
        "1/2 (incluye el procedimiento de FAT de hardware del tablero), "
        "utilizables como base de testificación.",
        "05_INGENIERIA_REFERENCIA — planos, listas y datasheets contra los "
        "cuales se verifica lo fabricado (Proceso/Mecánica e "
        "Instrumentación/Eléctrica), más la subcarpeta CONTROL_PENDIENTE_REV0 "
        "con la lógica de control para el FAT.",
        "06_CRONOGRAMA — cronograma del proyecto y programa de fabricación.",
    ]:
        add_bullet(doc, t)

    # 3. DOCUMENTOS DEL PAQUETE
    doc.add_heading("DOCUMENTOS DEL PAQUETE", level=1)
    add_para(doc,
        "Las tablas siguientes listan cada documento, su revisión vigente, su "
        "estado y la visita o punto de inspección que soporta "
        "(H = Punto de Espera, W = Punto de Testimonio).")

    doc.add_heading("Base contractual (carpeta 01)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-ET-09-000-001", "Especificación Técnica del Módulo", "0", "Vigente", "Criterios de aceptación y FAT — todas las visitas"),
        ("BAE 12803", "Bases Administrativas Especiales", "—", "Vigente", "Autoridad del inspector y protocolo H/W"),
        ("P22-IT-09-000-001", "PIE Base (plantilla de inspección)", "0", "Vigente", "Referencia del plan de inspección"),
        ("20.24.6501.F", "Oferta Técnica BW Water", "1", "Vigente", "Alcance comprometido (referencia)"),
    ])

    doc.add_heading("Plan de Inspección y Ensayos (carpeta 02)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-BA-09-000-004", "Inspection and Test Plan (ITP)", "0", "Aprobado (Cód. 1)", "Mapa de puntos H/W — todas las visitas"),
    ])

    doc.add_heading("Procedimientos de calidad aprobados (carpeta 03)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-BA-09-000-005", "NDE Plan", "C", "Aprobado (Cód. 1)", "Visita 2 — END/NDE (RT, PT, UT)"),
        ("P22-BA-09-000-003", "Project Quality Plan (PQP)", "B", "Aprobado c/notas (Cód. 2)", "Sistema de calidad — todas"),
        ("P22-BA-09-000-006", "PMI Procedure", "A", "Aprobado c/notas (Cód. 2)", "Visita 1 — PMI Super Duplex"),
        ("P22-BA-09-000-007", "Welding Procedure (WPS/PQR y soldadores)", "A", "Aprobado c/notas (Cód. 2)", "Visita 1 — calificación y soldadura"),
        ("P22-BA-09-000-008", "Visual Procedure", "A", "Aprobado c/notas (Cód. 2)", "Visita 1 — inspección visual de soldadura"),
        ("P22-BA-09-000-009", "RO Vessel Hydrostatic Test Procedure", "C", "Aprobado c/notas (Cód. 2)", "Visita 3 — hidrostática RO Vessel (H)"),
        ("P22-BA-09-000-011", "Painting Procedure", "B", "Aprobado c/notas (Cód. 2)", "Visitas 3-4 — preparación y recubrimiento"),
        ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "D", "Aprobado c/notas (Cód. 2) — TM N29", "Visita 3 — hidrostática 135/7,5 bar (H/W)"),
        ("P22-PP-09-000-001", "PLC/LCP FAT Procedure — Hardware", "A", "Aprobado c/notas (Cód. 2)", "FAT — pruebas de hardware del tablero"),
    ])

    doc.add_heading("Ingeniería de referencia — Proceso y Mecánica (carpeta 05)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-DWG-09-009-002", "P&ID", "D", "Vigente", "Trazado maestro — soldadura, hidrostática, montaje"),
        ("P22-LI-09-009-003", "Line List", "0", "Vigente (IFC) — Código 1 (N29)", "Visitas 2-3 — soldadura/hidrostática"),
        ("P22-ET-09-006-001", "Piping Specifications", "A", "Vigente", "Visitas 1-2 — materiales y soldadura"),
        ("P22-LI-09-005-001", "Equipment List", "B", "Vigente", "Visitas 1 y 5 — recepción y montaje"),
        ("P22-DWG-09-005-003", "Equipment Layout", "C", "Código 3 (Rev D pendiente)", "Visita 5 — montaje de equipos"),
        ("P22-DWG-09-005-008", "GA of SWRO System Skid", "A", "Vigente", "Visitas 2 y 5 — estructura y montaje"),
        ("P22-ET-09-006-002", "Painting Specification", "C", "Vigente", "Visitas 3-4 — recubrimiento"),
        ("P22-ET-09-009-002", "Datasheet RO HP Feed Pump (BH-09-001)", "D", "Vigente", "Visitas 1, 6 y FAT"),
        ("P22-ET-09-009-007", "Datasheet Feed Turbocharger (SIP-09-001)", "D", "Vigente", "Visitas 1 y 6"),
        ("P22-ET-09-009-008", "Datasheet Interstage Turbocharger (SIP-09-002)", "D", "Vigente", "Visitas 1 y 6"),
        ("P22-ET-09-009-001", "Datasheet UHPRO System (Membrana + Vessel)", "B", "Vigente (verificar)", "Visitas 1 y 3 — recepción e hidrostática"),
        ("P22-ET-09-009-005", "Datasheet RO Cartridge Filter (FIL-09-001)", "E", "Vigente", "Visitas 1 y 5"),
        ("P22-ET-09-009-006", "Datasheet CIP Cartridge Filter (FIL-09-002)", "E", "Vigente", "Visitas 1 y 5"),
    ])

    doc.add_heading("Ingeniería de referencia — Instrumentación y Eléctrica (carpeta 05)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-LI-09-008-003", "Instrument List", "E", "Vigente", "Visita 4 y FAT"),
        ("P22-LI-09-008-001", "IO List", "5", "Vigente (IFC)", "Visita 6 y FAT — lazo de control y software FAT"),
        ("P22-LI-09-005-002", "Valve List", "D", "Rev D vigente (portada BW en 'A')", "Visitas 4-5 y FAT"),
        ("P22-CD-09-007-001", "Single Line Diagram", "0", "Vigente (IFC) — Código 1", "Visitas 4, 6 y FAT — eléctrico"),
        ("P22-CD-09-008-001", "PLC/LCP Outline Panel Drawing", "0", "Vigente (IFC) — Código 1 (N29)", "Visita 6 — integración/terminación del tablero"),
        ("P22-ET-09-007-005", "Datasheet Local Control Panel (LCP)", "1", "Vigente (aprobado)", "Visita 6 y FAT — tablero"),
        ("P22-ET-09-008-001", "Datasheet PLC and HMI Panel Component", "C", "Vigente", "FAT — software FAT"),
        ("P22-CD-09-004-001", "Control Architecture", "D", "Vigente (aprobado)", "Visita 6 y FAT — lazo/control"),
    ])

    doc.add_heading("Familia de Control — pendiente Rev 0 (carpeta 05)", level=2)
    add_para(doc,
        "Los siguientes documentos de la lógica de control se incluyen como "
        "referencia para el atestiguamiento del FAT (prueba PLC/HMI con "
        "simulación de fallas). Están en Código 2 y BW Water debe reemitirlos "
        "como conjunto coordinado en Rev 0; se reemplazarán al emitirse.")
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-BT-09-009-001", "Plant Control Philosophy", "E", "Cód. 2 — pendiente Rev 0", "FAT — lógica de control"),
        ("P22-LI-09-008-015", "Alarm and Interlock List", "C", "Cód. 2 — pendiente Rev 0", "FAT — alarmas y enclavamientos"),
        ("P22-LI-09-008-017", "Control and Sequence Chart", "A", "Cód. 2 — pendiente Rev 0", "FAT — secuencia de control"),
    ])

    doc.add_heading("Cronograma (carpeta 06)", level=2)
    add_simple_table(doc, [
        ("Código", "Documento", "Rev", "Estado", "Aplica a"),
        ("P22-BA-09-000-001", "Project Schedule", "A", "Aprobado c/notas (Cód. 2)", "Planificación general"),
        ("—", "Fabrication Schedule (01-Jul-2026)", "—", "Vigente", "Ventanas de las visitas de inspección"),
    ])

    # 4. PENDIENTES
    doc.add_heading("PROCEDIMIENTOS PENDIENTES DE APROBACIÓN", level=1)
    add_para(doc,
        "Al 21-Jul-2026, tras los Transmittals N27 y N29, los tres "
        "procedimientos de prueba antes pendientes están aprobados (Código 2) y "
        "viven en la carpeta 03: el RO Vessel Hydrostatic Test Procedure (Rev "
        "C, TM N27), el Painting Procedure (Rev B, TM N27) y el HP and LP "
        "Pressure Test Procedure (Rev D, TM N29). La Rev D del HP/LP corrige el "
        "error de presión de prueba de la Rev C (75 bar sobre línea PVC), "
        "fijando las presiones por línea y material (LP 7,5 bar / HP 135 bar "
        "sobre Super Duplex).")
    add_para(doc,
        "No quedan procedimientos de calidad en Código 3. El ensayo "
        "hidrostático de alta presión sigue siendo un Punto de Espera del Plan "
        "de Inspección y Ensayos.")

    # 5. REQUERIDOS A BW WATER
    doc.add_heading("DOCUMENTOS POR REQUERIR A BW WATER", level=1)
    add_bold_lead(doc, "Isométricos de spools con juntas numeradas: ",
        "no fueron entregados a la fecha. Son necesarios para la testificación "
        "de soldadura y END de los spools de cañería en taller; se recomienda "
        "solicitarlos a BW Water antes de la Visita 1.")
    add_bold_lead(doc, "Datasheet del UHPRO System (Membrana + Vessel) Rev B: ",
        "es la última revisión encontrada y no evolucionó a emisión IFC como "
        "el resto de la ingeniería; conviene confirmar con BW Water que Rev B "
        "sigue siendo la referencia vigente para los pressure vessels.")
    add_bold_lead(doc, "Procedimiento de FAT de sistema/software: ",
        "el procedimiento de FAT de hardware del tablero (P22-PP-09-000-001 "
        "Rev A) está incluido en la carpeta 03; el procedimiento de FAT de "
        "sistema/software detallado aún no se entrega y es un punto de espera "
        "del Plan de Inspección y Ensayos, por requerir a BW Water antes del "
        "FAT.")
    add_bold_lead(doc, "Valve List (P22-LI-09-005-002) — campo de portada: ",
        "el archivo es la Rev D vigente (el historial de revisión y la hoja de "
        "comentarios lo confirman), pero el campo 'Revision No.' de la portada "
        "quedó en 'A'; se solicita a BW Water corregir el campo de portada a D "
        "en el próximo issue. La revisión gobernante es la D.")
    add_bold_lead(doc, "Cálculo estructural del skid (P22-CD-09-005-001): ",
        "es un documento de cálculo de la etapa de diseño (aprobado con notas "
        "en el Transmittal N29); queda fuera del alcance de la inspección de "
        "taller y no se incluye en este paquete. La verificación dimensional "
        "del skid se soporta con el plano GA (P22-DWG-09-005-008).")

    # 6. CALENDARIO Y PROTOCOLO
    doc.add_heading("CALENDARIO DE VISITAS Y PROTOCOLO DE NOTIFICACIÓN", level=1)
    add_para(doc,
        "El calendario indicativo comprende seis visitas semanales de "
        "acompañamiento, con tres visitas por semana (Semana 1: 27-31 jul; "
        "Semana 2: 3-7 ago; Semana 3: 10-14 ago; Semana 4: 17-21 ago; Semana "
        "5: 24-28 ago; Semana 6: 31 ago-4 sep) y el atestiguamiento del FAT "
        "(aprox. 7-12 sep). Las fechas son indicativas y se confirman contra "
        "las notificaciones formales de Puntos de Espera y de Testimonio que "
        "BW Water debe emitir para cada actividad, conforme a las Bases "
        "Administrativas Especiales (Cláusula 37.2), con el aviso previo mínimo "
        "establecido (30 días para inspecciones internacionales).")
    add_para(doc,
        "El detalle de la designación, el calendario por visita y el protocolo "
        "de notificación se encuentran en la Nota Técnica P22-NT-09-000-002-0 "
        "(carpeta 00).")

    # 7. HISTORIAL
    doc.add_heading("HISTORIAL DEL DOCUMENTO", level=1)
    add_simple_table(doc, [
        ("Rev", "Fecha", "Descripción"),
        ("0", "07-Jul-2026", "Primera emisión — guía del paquete de inspección para Bureau Veritas."),
        ("1", "21-Jul-2026", "Actualización a últimas versiones: Control Architecture D, PLC & HMI C, IO List 5, Line List 0 IFC, Outline del panel 0 IFC; RO Vessel Hydro (Rev C) y Painting (Rev B) reclasificados a aprobados; FAT de hardware agregado; familia de Control agregada (pendiente Rev 0); HP/LP Pressure Test (010) pendiente Rev D."),
    ])

    # metadatos limpios (global sec. 2.3)
    docx_metadata.apply_core_properties(
        doc,
        title="Guía del Paquete de Inspección de Taller - Bureau Veritas",
        author="Luis Rivera Gonzalez",
        last_modified_by="Luis Rivera Gonzalez",
        subject="Módulo RO Segunda Etapa - Taltal - paquete de inspección BV",
        comments="Guía del paquete de inspección de taller para Bureau Veritas "
                 "(Rev 1, 21-Jul-2026).",
        language="es-CL",
    )
    doc.save(OUTPUT)
    docx_metadata.fix_app_xml(OUTPUT, company="Aguas de Antofagasta S.A.")
    print("Guia generada:", OUTPUT)


if __name__ == "__main__":
    crear()
