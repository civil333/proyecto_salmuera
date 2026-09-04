#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera TRANSMITTAL N3 ADASA-LYA (flujo OOCC, espanol, para L&A).
Codigo P22-TM-00-010-003-0. ENTREGA 5 (cover L&A 067-032-032-COR-TT-006, 09-Jun-2026).
Fecha: 10-Jun-2026.

Transmittal de levantamiento: revisa la respuesta de L&A (ENTREGA 5) a los puntos
del Transmittal N2. Reconoce lo resuelto y lista lo que queda abierto.

Calibracion del usuario (10-Jun):
- MC-001 -> Codigo 2: el anclaje quedo preinstalado en el plano; la armadura @200 es
  aceptable si cumple cuantia minima de ACI 318 (la losa es fundacion de estanque PRFV
  apoyado, NO contencion de liquido), solo justificar el calculo (preferir Phi16@200);
  conciliar la designacion MC<->plano (retirar HAS-V-36 / empotramiento 40 vs 38 cm).
- ET-103 -> Codigo 2 duro: trasladar a la ET el esquema C5-M por capas que ya vive en
  la MC/nota general; exigir perneria protegida; sin nueva Rev intermedia.
- Anclaje postinstalado de la bomba BH-06-001 ACEPTADO (planos KSB): se retira la OBS.
- NO se invoca el limite del ciclo del TdR en este transmittal (queda 100% tecnico).

Recuento: 9 Codigo 2 + 10 Codigo 3 + 1 sin codigo (MC-002-003 no recibida).
Veredicto global: 3 - POR REVISAR. Determinantes: planos e Itemizados.
Comentarios como directivas (Defecto / Corregir: / Requisito:).
"""

import sys
import os

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N3 ADASA-LYA.docx")


def add_para(doc, runs):
    para = doc.add_paragraph()
    for item in runs:
        text = item[0]
        attrs = item[1] if len(item) > 1 else {}
        run = para.add_run(text)
        if attrs.get("bold"):
            run.bold = True
        if attrs.get("italic"):
            run.italic = True
    aplicar_arial_12(para)
    return para


def obs(doc, idtit, defecto, corregir, requisito=None):
    runs = [(idtit + " ", {"bold": True}), (defecto + " ",),
            ("Corregir: ", {"bold": True}), (corregir,)]
    if requisito:
        runs += [(" ",), ("Requisito: ", {"bold": True}), (requisito,)]
    add_para(doc, runs)


def add_bullet(doc, text):
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


def main() -> None:
    crear_documento_adasa(
        titulo=("TRANSMITTAL DE REVISIÓN TÉCNICA N3 — INGENIERÍA DE "
                "DETALLE OOCC MÓDULO RO 2DA ETAPA SALMUERA TALTAL"),
        codigo="P22-TM-00-010-003-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # =========================================================
    # 1. RESUMEN EJECUTIVO
    # =========================================================
    doc.add_heading("RESUMEN EJECUTIVO", level=1)

    add_para(doc, [
        ("VEREDICTO DEL TRANSMITTAL: 3 — POR REVISAR.", {"bold": True}),
        (" Revisión de la ENTREGA 5, que responde a los comentarios del "
         "Transmittal N2: seis Memorias de Cálculo (cinco en Rev 1), tres "
         "Especificaciones Técnicas en Rev 0, tres Itemizados en Rev C y los "
         "planos de obras civiles en Rev C, más el plano nuevo de Excavaciones "
         "(Rev B). Recuento: 9 Código 2 y 10 Código 3; el veredicto lo fijan "
         "los planos de obras civiles y los tres Itemizados.",),
    ])

    add_para(doc, [
        ("Códigos de respuesta (según los Términos de Referencia):",
         {"bold": True}),
    ])
    add_simple_table(doc, [
        ("Código", "Significado"),
        ("1 — Aprobado",
         "Sin observaciones; el documento avanza a Rev 0."),
        ("2 — Aprobado con comentarios",
         "Notas a incorporar directamente en Rev 0, sin nueva revisión "
         "intermedia."),
        ("3 — Por revisar",
         "Requiere nueva revisión incorporando las observaciones antes de "
         "Rev 0."),
        ("4 — Rechazado",
         "Requiere rehacer el documento con revisión completa."),
    ])

    add_para(doc, [
        ("Los documentos de la entrega que no aparezcan en el listado de "
         "respuesta se entienden Aprobados (Código 1).",),
    ])

    add_para(doc, [
        ("Entregables no recibidos o incompletos: ", {"bold": True}),
        ("la Memoria de Cálculo del Sistema de Drenajes (P22-MC-00-002-003) "
         "figura en la carta de transmisión pero su archivo no llegó; el "
         "archivo de la lámina 2 del plano de Fundación del Contenedor "
         "(P22-DWG-00-002-003) corresponde a la lámina 1 (falta el detalle del "
         "inserto INS-1); el plano de Canalizaciones (P22-DWG-00-002-006) "
         "anuncia tres láminas y se entregaron dos (falta el detalle típico de "
         "cámara); y el plano de Detalles de Anclaje y Conexiones "
         "(P22-DWG-00-002-005) sigue sin entregarse. Estos puntos se detallan "
         "en el correo de remisión.",),
    ])

    # =========================================================
    # 2. OBSERVACIONES POR DOCUMENTO
    # =========================================================
    doc.add_heading("OBSERVACIONES POR DOCUMENTO", level=1)

    # ---------- 2.1 Memorias ----------
    doc.add_heading("Memorias de Cálculo", level=2)

    doc.add_heading(
        "Fundación Estanque TK-06-001 — P22-MC-00-002-001 Rev 1 (Código 2)",
        level=3)
    add_para(doc, [
        ("El anclaje fue rediseñado a preinstalado colado en sitio, según se "
         "refleja en el plano de fundación. Para incorporar en Rev 0:",)])
    obs(doc, "OBS-01 — Coherencia memoria-plano del anclaje.",
        "La memoria declara el anclaje como preinstalado pero conserva la "
        "designación de varilla HAS-V-36 (producto de anclaje químico) y un "
        "empotramiento de 40 cm, mientras el plano de fundación especifica "
        "barra ASTM F1554 con tuerca y placa embebidas y un empotramiento de "
        "~38 cm.",
        "unificar la designación del perno preinstalado (barra ASTM F1554 con "
        "extremo embebido, sin nomenclatura de anclaje químico) y el "
        "empotramiento entre la memoria y el plano; mostrar la verificación "
        "por los modos de falla de anclaje preinstalado.",
        "ACI 318-19 Capítulo 17 y Sección 17.10; plano Exfibro EX-26005-F01 "
        "Rev C.")
    obs(doc, "OBS-02 — Justificación de la armadura de losa.",
        "La armadura de la losa pasó a Ø12@200 y se retiró la verificación "
        "asociada; el documento no muestra la cuantía resultante ni el espesor "
        "de losa.",
        "justificar el cálculo de la armadura de la losa verificando la "
        "cuantía mínima de ACI 318 y la flexión/corte con las solicitaciones "
        "del anclaje; se recomienda adoptar Ø16@200.",
        "ACI 318-19 (cuantía mínima de retracción y temperatura).")
    obs(doc, "NOTA-01 — Trazabilidad de las reacciones basales.",
        "La memoria adopta las reacciones corregidas por ADASA (Ez = ±3.357 "
        "kgf) pero cita como fuente la \"Memoria Estanque AFTA Taltal\".",
        "citar P22-IT-06-000-005-0 como fuente vinculante de las reacciones.",
        "P22-IT-06-000-005-0.")
    obs(doc, "NOTA-02 — Recubrimientos.",
        "No se declaran los recubrimientos mínimos.",
        "declarar los recubrimientos mínimos en ambas condiciones: 50 mm en "
        "elementos expuestos y 70 mm en contacto con el terreno.",
        "Términos de Referencia, Sección 3.3.4.")

    doc.add_heading(
        "Fundación Dinámica Bomba BH-06-001 — P22-MC-00-002-002 Rev 1 "
        "(Código 2)", level=3)
    add_para(doc, [
        ("El análisis dinámico es conforme y el anclaje postinstalado de la "
         "bomba se acepta conforme a los planos del fabricante (KSB). Pendiente "
         "para la Rev 0:",)])
    obs(doc, "NOTA-01 — Recubrimientos.",
        "La memoria declara el recubrimiento en contacto con terreno (70 mm) "
        "pero no el de elementos expuestos.",
        "declarar los recubrimientos mínimos en ambas condiciones: 50 mm en "
        "elementos expuestos y 70 mm en contacto con el terreno.",
        "Términos de Referencia, Sección 3.3.4.")

    doc.add_heading(
        "Fundación Contenedor RO — P22-MC-00-002-004 Rev 1 (Código 2)",
        level=3)
    add_para(doc, [
        ("La versión de ACI 318 quedó unificada a 318-19 y el peso del "
         "contenedor (17.334 tonf) se incorporó al modelo como valor "
         "conservador, por lo que se acepta. A corregir antes de Rev 0:",)])
    obs(doc, "NOTA-01 — Recubrimientos.",
        "No se declaran los recubrimientos mínimos.",
        "declarar los recubrimientos mínimos en ambas condiciones: 50 mm en "
        "elementos expuestos y 70 mm en contacto con el terreno.",
        "Términos de Referencia, Sección 3.3.4.")

    doc.add_heading(
        "Fundación Sistema CIP — P22-MC-00-002-005 Rev 1 (Código 2)",
        level=3)
    add_para(doc, [
        ("La memoria declara correctamente el diferimiento de los anclajes de "
         "los equipos CIP con la norma de referencia (queda en seguimiento "
         "hasta recibir los planos del proveedor BW Water; no condiciona la "
         "aprobación). Para la Rev 0:",)])
    obs(doc, "NOTA-01 — Recubrimientos.",
        "Se declara el recubrimiento en contacto con terreno (70 mm) pero no "
        "el de elementos expuestos.",
        "declarar los recubrimientos mínimos en ambas condiciones: 50 mm en "
        "elementos expuestos y 70 mm en contacto con el terreno.",
        "Términos de Referencia, Sección 3.3.4.")

    doc.add_heading(
        "Cubierta Metálica Sistema CIP Exterior — P22-MC-00-003-001 Rev 1 "
        "(Código 2)", level=3)
    add_para(doc, [
        ("Se incorporó el sistema de protección C5-M completo, se unificó el "
         "coeficiente sísmico vertical a 0,74 y los anexos quedaron integrados "
         "a la revisión vigente. Por incorporar en Rev 0:",)])
    obs(doc, "NOTA-01 — Recubrimientos y combinación de cargas.",
        "No se declaran los recubrimientos de los pedestales y la combinación "
        "de cargas se expresa como \"1,2D±E\".",
        "declarar los recubrimientos mínimos en ambas condiciones (50 mm en "
        "elementos expuestos y 70 mm en contacto con el terreno) y dejar "
        "explícita la combinación de cargas adoptada.",
        "Términos de Referencia, Sección 3.3.4; NCh 2369.")

    # ---------- 2.2 Especificaciones ----------
    doc.add_heading("Especificaciones Técnicas", level=2)
    add_para(doc, [
        ("Las tres Especificaciones quedan Código 2 — Aprobado con "
         "comentarios. Se particularizaron a Taltal y se incorporaron los "
         "recubrimientos duales, la impermeabilización y la referencia AWS "
         "D1.1. Comentarios a incorporar en Rev 0:",)])
    obs(doc, "OBS-01 (ET Movimiento de Tierra) — Tensión admisible del suelo.",
        "Se incorporaron las condiciones de mejoramiento de suelo, pero no se "
        "declara la tensión admisible de diseño.",
        "declarar la tensión admisible adoptada σ_adm ≤ 1,0 kg/cm² y eliminar "
        "la referencia residual a \"Municipalidad de Antofagasta\".",
        "Términos de Referencia (tensión admisible de diseño).")
    obs(doc, "NOTA-01 (ET Obras Civiles) — Código de portada.",
        "Los recubrimientos duales y la impermeabilización quedaron "
        "incorporados; la portada conserva un código tipo IT.",
        "corregir el código de portada a P22-ET-00-010-102-0.",
        "codificación del proyecto.")
    obs(doc, "OBS-02 (ET Estructura Metálica) — Esquema C5-M por capas y "
             "pernería.",
        "Se corrigió la referencia a AWS D1.1, pero la Especificación declara "
        "la clasificación C5-M sin el esquema por capas (preparación de "
        "superficie SSPC-SP10 + zinc + epóxico + poliuretano), ya "
        "desarrollado en la memoria de la cubierta, y no exige pernería "
        "protegida para ambiente expuesto.",
        "trasladar a la Especificación el esquema de protección por capas con "
        "su preparación de superficie y exigir pernería galvanizada en "
        "caliente o inoxidable; corregir el código tipo IT de la portada.",
        "Términos de Referencia, Sección 3.4.2; ISO 12944.")

    # ---------- 2.3 Itemizados ----------
    doc.add_heading("Itemizados de Presupuesto", level=2)
    add_para(doc, [
        ("Los tres Itemizados quedan Código 3; los comentarios del Transmittal "
         "N2 no fueron incorporados.",)])
    obs(doc, "OBS-01 — Clase de estimación.",
        "Los Itemizados no declaran la clase de estimación.",
        "declarar la clase de estimación acordada en la reunión de arranque, la "
        "Clase 2 AACE (Minuta 067-032-032-COR-MI-001).",
        "Minuta de reunión de arranque 067-032-032-COR-MI-001.")
    obs(doc, "OBS-02 — Tag de la fosa y pestaña ajena.",
        "El Itemizado de Movimiento de Tierra y el de Obras Civiles mantienen "
        "el tag de la fosa como TK-06-002 (que es el estanque CIP de BW "
        "Water), y las tres planillas conservan una pestaña \"Cuadro de "
        "Piezas Especiales Interconexión La Chimba\", ajena al proyecto.",
        "corregir el tag de la fosa a TK-06-004 y eliminar la pestaña de "
        "\"La Chimba\" en los tres Itemizados.",
        "codificación del proyecto.")
    obs(doc, "OBS-03 — Partidas faltantes.",
        "El Itemizado de Obras Civiles no incluye la impermeabilización de "
        "elementos enterrados, ya especificada en su Especificación, y el de "
        "Estructura Metálica no incluye la protección anticorrosiva (esquema "
        "C5-M) ni la soldadura.",
        "incorporar las partidas de impermeabilización, protección superficial "
        "y soldadura, en línea con las Especificaciones correspondientes.",
        "consistencia Especificación-Itemizado.")

    # ---------- 2.4 Planos ----------
    doc.add_heading("Planos de Obras Civiles", level=2)
    add_para(doc, [
        ("Comentarios a los planos (incorporar en la próxima revisión). Los "
         "identificadores OBS/NOTA coinciden con los del PDF anotado adjunto "
         "de cada lámina (CC_ADASA). Los puntos del Transmittal N2 que ya se "
         "resolvieron (anclaje del estanque en LAM2 de "
         "P22-DWG-00-002-002, cotas absolutas del contenedor en "
         "P22-DWG-00-002-003 y N.T.N. del Sistema CIP en P22-DWG-00-002-007) "
         "no se repiten.",)])
    add_simple_table(doc, [
        ("Plano / Lámina", "ID", "Comentario"),
        ("P22-DWG-00-001-001 LAM1\nExcavaciones y movimiento de tierra "
         "(nuevo)", "OBS-01",
         "El plano cubre solo las zanjas de drenaje: incorporar las "
         "excavaciones de las fundaciones (estanque, bomba, fosa, contenedor "
         "RO, Sistema CIP), los niveles de plataforma y el N.T.N. por zona, o "
         "declarar explícitamente el alcance parcial y referir los planos que "
         "lo cubren."),
        ("P22-DWG-00-001-001 LAM1", "OBS-02",
         "Los rellenos (\"arena limpia compactada\", \"relleno estructural\") "
         "no tienen especificación: referir la Especificación de Movimiento de "
         "Tierra y declarar granulometría, % de compactación y calidad del "
         "material (libre de sales, cloruros y sulfatos). Completar el cuadro "
         "de referencias."),
        ("P22-DWG-00-001-001 LAM2", "OBS-03",
         "Resolver la rasante de la red de drenaje: declarar la pendiente "
         "longitudinal de proyecto de la tubería por gravedad y la cota de "
         "empalme (invert) en la cámara de descarga existente."),
        ("P22-DWG-00-001-001 LAM1/LAM2", "NOTA-01",
         "Adoptar la nomenclatura CD-06-00N para las cámaras; rotular los tags "
         "de equipos y estructuras; declarar el recubrimiento mínimo sobre la "
         "tubería; corregir \"relleno estructural\"."),
        ("P22-DWG-00-002-001 LAM1\nImplantación general OOCC", "OBS-01",
         "Acotar el N.T.N. por zona, coincidente con los planos de montaje "
         "P22-DWG-06-005-101 / -103 / -105 y el Levantamiento DIO (el cuadro "
         "de coordenadas UTM ya fija el azimut)."),
        ("P22-DWG-00-002-001 LAM1", "NOTA-01",
         "Corregir el tag de la fosa a TK-06-004 (figura como TK-06-002) y la "
         "sigla del documento de la nota de protección C5-M (cita P22-IT, debe "
         "ser P22-ET-00-010-103-0)."),
        ("P22-DWG-00-002-002 LAM1\nFundaciones equipos exteriores", "OBS-01",
         "Agregar la nota con las condiciones de mejoramiento / tratamiento de "
         "suelo, conforme a la Especificación de Movimiento de Tierra."),
        ("P22-DWG-00-002-002 LAM4", "OBS-01",
         "Agregar la nota con las condiciones de mejoramiento / tratamiento de "
         "suelo."),
        ("P22-DWG-00-002-002 LAM2/LAM4", "NOTA-01",
         "Conciliar la designación de la marca de perno PA-1 (figura como "
         "preinstalado en una lámina y postinstalado en otra) y corregir la "
         "referencia al plano del proveedor (EX-26005-F01 Rev C)."),
        ("P22-DWG-00-002-003 LAM1\nFundación contenedor RO", "OBS-01",
         "Agregar la nota con las condiciones de mejoramiento de suelo (las "
         "cotas ya quedaron en N.T.N. absoluto)."),
        ("P22-DWG-00-002-004 LAM1\nFosa de drenajes", "OBS-01",
         "Declarar el mejoramiento de suelo (la capa \"M.H.A.\" graficada no "
         "está definida) y completar la impermeabilización de los elementos "
         "enterrados."),
        ("P22-DWG-00-002-004 LAM1", "NOTA-01",
         "Unificar el tag de la fosa a TK-06-004 (la lámina 2 conserva "
         "TK-006-002)."),
        ("P22-DWG-00-002-004 LAM2", "OBS-02",
         "Agregar y acotar las aperturas de rebalse del estanque; especificar "
         "la parrilla como pultruida de PRFV para tránsito liviano de "
         "personas (la designación ARS-5 corresponde a acero)."),
        ("P22-DWG-00-002-006 LAM1\nCanalizaciones y red de drenajes", "OBS-01",
         "Adoptar la nomenclatura CD-06-00N para las cámaras (las pendientes "
         "ya quedaron acotadas en el perfil)."),
        ("P22-DWG-00-002-006 LAM1/LAM2", "NOTA-01",
         "Incorporar el detalle típico de cámara prefabricada (anunciado como "
         "lámina 3, no entregada) y unificar la revisión del cajetín "
         "(coexisten Rev B y Rev C)."),
        ("P22-DWG-00-002-007 LAM1\nFundaciones equipos Sistema CIP", "OBS-01",
         "Agregar las notas de mejoramiento de suelo e impermeabilización (el "
         "N.T.N. ya se reconcilió a +6,000); corregir la fecha del cajetín "
         "(09/09/26)."),
        ("P22-DWG-00-002-007 LAM3", "OBS-01",
         "Agregar las notas de mejoramiento de suelo e impermeabilización."),
        ("P22-DWG-00-003-001 LAM1\nCubierta metálica Sistema CIP", "NOTA-01",
         "Corregir la sigla del documento citado en la nota de protección "
         "C5-M (cita P22-IT, debe ser P22-ET-00-010-103-0)."),
    ])

    # =========================================================
    # 3. ADJUNTOS
    # =========================================================
    doc.add_heading("ADJUNTOS", level=1)
    add_para(doc, [
        ("Las memorias, especificaciones y planos con observaciones llevan PDF "
         "anotado (CC_ADASA): las cinco Memorias de Cálculo en Rev 1, las tres "
         "Especificaciones Técnicas y los planos de obras civiles con "
         "comentario, incluido el plano nuevo de Excavaciones. Los tres "
         "Itemizados llevan el archivo Excel con notas.",)])

    # =========================================================
    # 4. RESUMEN DE RESPUESTA
    # =========================================================
    doc.add_heading("RESUMEN DE RESPUESTA", level=1)
    add_simple_table(doc, [
        ("Código Documento", "Título", "Rev", "Código de Respuesta"),
        ("P22-MC-00-002-001", "Fundación Estanque TK-06-001", "1",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-002-002", "Fundación Dinámica Bomba BH-06-001", "1",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-002-004", "Fundación Contenedor RO", "1",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-002-005", "Fundación Sistema CIP", "1",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-003-001", "Cubierta Metálica Sistema CIP Exterior", "1",
         "2 — Aprobado con comentarios"),
        ("P22-ET-00-010-101", "Especificación Movimiento de Tierra", "0",
         "2 — Aprobado con comentarios"),
        ("P22-ET-00-010-102", "Especificación Obras Civiles", "0",
         "2 — Aprobado con comentarios"),
        ("P22-ET-00-010-103", "Especificación Estructura Metálica", "0",
         "2 — Aprobado con comentarios"),
        ("P22-IT-00-010-101", "Itemizado Movimiento de Tierra", "C",
         "3 — Por revisar"),
        ("P22-IT-00-010-102", "Itemizado Obras Civiles", "C",
         "3 — Por revisar"),
        ("P22-IT-00-010-103", "Itemizado Estructura Metálica", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-001-001", "Excavaciones y movimiento de tierra", "B",
         "3 — Por revisar"),
        ("P22-DWG-00-002-001", "Implantación general OOCC", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-002", "Fundaciones equipos exteriores", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-003", "Fundación contenedor RO", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-004", "Fosa de drenajes", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-006", "Canalizaciones y red de drenajes", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-007", "Fundaciones equipos Sistema CIP", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-003-001", "Cubierta metálica Sistema CIP", "C",
         "2 — Aprobado con comentarios"),
    ])
    add_para(doc, [
        ("Veredicto global del transmittal: 3 — POR REVISAR.",
         {"bold": True}),
        (" Las seis Memorias de Cálculo y las tres Especificaciones Técnicas "
         "quedan aprobadas con comentarios a incorporar en Rev 0. El veredicto "
         "lo fijan los planos de obras civiles y los tres Itemizados. La "
         "Memoria de Cálculo del Sistema de Drenajes (P22-MC-00-002-003) y el "
         "plano de Detalles de Anclaje (P22-DWG-00-002-005) siguen pendientes "
         "de entrega; el archivo de la lámina 2 del plano de Fundación del "
         "Contenedor y la lámina de detalle de cámaras del plano de "
         "Canalizaciones llegaron incompletos. El N.T.N. por zona debe quedar "
         "acotado en la implantación, y las excavaciones de las fundaciones "
         "deben quedar respaldadas por su plano para dar sustento a las "
         "cubicaciones.",),
    ])

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    main()
