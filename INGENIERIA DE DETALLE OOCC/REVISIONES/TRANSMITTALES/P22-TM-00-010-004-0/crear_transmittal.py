#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera TRANSMITTAL N4 ADASA-LYA (flujo OOCC, espanol, para L&A).
Codigo P22-TM-00-010-004-0. ENTREGA 7 (cover L&A 067-032-032-COR-TT-008, 17-Jun-2026).
Fecha: 18-Jun-2026.

Transmittal de levantamiento: revisa la respuesta de L&A (ENTREGA 7) a los puntos
del Transmittal N3. Reconoce lo resuelto y lista lo que queda abierto.

Calibracion del usuario (18-Jun), tras verificacion de levantamiento E7 vs TM N3
(ver _ANALISIS_TRABAJO.md):
- MC-002-001 -> Codigo 2 (no regresion): mantener con condiciones duras a Rev 0
  (justificar armadura; reconciliar empotramiento memoria<->plano, hoy 30 cm en la
  memoria vs ~38 cm en el plano).
- Clase 2 AACE reclasificada MENOR (declaracion incorporable a Rev 0) -> los tres
  Itemizados SUBEN a Codigo 2 (ya levantaron tag de fosa, pestana ajena,
  impermeabilizacion y proteccion C5-M).
- Veredicto global Codigo 3 anclado SOLO en los planos de obras civiles.
- El correo de remision invoca el limite de ciclo del TdR (planos en Rev D sin
  converger; mejoramiento de suelo y plano rector de excavaciones sin levantar por
  2o-3er ciclo; 3a falta de entrega de MC-002-003 y DWG-002-005).

Recuento: 7 Codigo 1 + 6 Codigo 2 + 6 Codigo 3 (+ IT-001-0 insumo, no del paquete).
Veredicto global: 3 - POR REVISAR. Determinantes: planos de obras civiles.
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N4 ADASA-LYA.docx")


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
        titulo=("TRANSMITTAL DE REVISIÓN TÉCNICA N4 — INGENIERÍA DE "
                "DETALLE OOCC MÓDULO RO 2DA ETAPA SALMUERA TALTAL"),
        codigo="P22-TM-00-010-004-0",
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
        (" Revisión de la ENTREGA 7 (carta de transmisión 067-032-032-COR-TT-008, "
         "17-Jun-2026), que responde a los comentarios del Transmittal N3: cinco "
         "Memorias de Cálculo en Rev 2, tres Especificaciones Técnicas en Rev 1, "
         "tres Itemizados en Rev D y los planos de obras civiles en Rev D (más el "
         "plano de Excavaciones en Rev C). Recuento: 7 Código 1, 6 Código 2 y 6 "
         "Código 3. El ciclo cerró el grueso de las Memorias de Cálculo y las "
         "Especificaciones Técnicas; el veredicto lo fijan los planos de obras "
         "civiles.",),
    ])

    add_para(doc, [
        ("Este transmittal no incorpora observaciones nuevas. ", {"bold": True}),
        ("Cada comentario se emitió en un transmittal anterior y permanece sin "
         "levantar: la mayoría proviene del Transmittal N2 (es la tercera vez que "
         "se formulan) y el resto del Transmittal N3. Junto a cada identificador "
         "se indica entre paréntesis el transmittal de origen.",),
    ])

    add_para(doc, [
        ("Avances reconocidos en este ciclo: ", {"bold": True}),
        ("las cinco Memorias de Cálculo declaran los recubrimientos mínimos en "
         "ambas condiciones (50 mm expuestos / 70 mm en contacto con el terreno); "
         "las tres Especificaciones Técnicas quedan Aprobadas (tensión admisible "
         "σ_adm ≤ 1,0 kg/cm², esquema de protección C5-M por capas con pernería "
         "galvanizada o inoxidable, y códigos de portada corregidos); los tres "
         "Itemizados corrigieron el tag de la fosa a TK-06-004, eliminaron la "
         "pestaña ajena, e incorporaron la impermeabilización y la protección "
         "C5-M; la implantación general acotó el N.T.N. por zona; y se entregó el "
         "detalle típico de cámara prefabricada.",),
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
        ("la Memoria de Cálculo del Sistema de Drenajes (P22-MC-00-002-003) y el "
         "plano de Detalles de Anclaje y Conexiones (P22-DWG-00-002-005) siguen "
         "sin entregarse por tercera entrega consecutiva. Además, varios planos "
         "se re-emitieron de forma parcial, dejando láminas con comentarios "
         "abiertos sin re-emitir: el plano de Canalizaciones (P22-DWG-00-002-006) "
         "entregó solo la lámina 3; el de Fundación del Sistema CIP "
         "(P22-DWG-00-002-007), solo la lámina 1 (falta la lámina 3); y el de "
         "Cubierta Metálica (P22-DWG-00-003-001), solo la lámina 1. Estos puntos "
         "se detallan en el correo de remisión.",),
    ])

    # =========================================================
    # 2. OBSERVACIONES POR DOCUMENTO
    # =========================================================
    doc.add_heading("OBSERVACIONES POR DOCUMENTO", level=1)

    # ---------- 2.1 Memorias ----------
    doc.add_heading("Memorias de Cálculo", level=2)
    add_para(doc, [
        ("Las cinco Memorias incorporaron los recubrimientos mínimos y la "
         "trazabilidad de las reacciones. Tres quedan Código 1 — Aprobado "
         "(P22-MC-00-002-002 Fundación Bomba, P22-MC-00-002-005 Fundación "
         "Sistema CIP y P22-MC-00-003-001 Cubierta Metálica): el anclaje "
         "postinstalado de la bomba y el diferimiento de los anclajes del "
         "Sistema CIP quedan conformes y no se reabren. Dos quedan Código 2 con "
         "puntos a incorporar en Rev 0:",)])

    doc.add_heading(
        "Fundación Estanque TK-06-001 — P22-MC-00-002-001 Rev 2 (Código 2)",
        level=3)
    add_para(doc, [
        ("Se retiró la designación de anclaje químico y se citó la fuente "
         "vinculante de las reacciones. Quedan dos puntos a cerrar en Rev 0:",)])
    obs(doc, "OBS-01 (Transmittal N2) — Coherencia memoria-plano del anclaje.",
        "La coherencia entre la memoria y el plano (designación y empotramiento "
        "del perno preinstalado) sigue pendiente; el plano de Detalles de Anclaje "
        "(P22-DWG-00-002-005) no se ha entregado, por lo que no puede cerrarse.",
        "unificar la designación y el empotramiento del perno entre la memoria y "
        "el plano, y conciliarlos con el plano de Detalles de Anclaje al "
        "re-emitirse.",
        "ACI 318-19 Capítulo 17 y Sección 17.10; plano Exfibro EX-26005-F01 "
        "Rev 0.")
    obs(doc, "OBS-02 (Transmittal N2) — Justificación de la armadura de losa.",
        "La armadura de la losa se mantiene en Ø12@200 sin la justificación "
        "solicitada: no se muestra la cuantía mínima ni la verificación de "
        "flexión/corte con las solicitaciones del anclaje.",
        "justificar el cálculo de la armadura verificando la cuantía mínima de "
        "ACI 318 y la flexión/corte con las solicitaciones del anclaje; se "
        "recomienda adoptar Ø16@200.",
        "ACI 318-19 (cuantía mínima de retracción y temperatura).")

    doc.add_heading(
        "Fundación Contenedor RO — P22-MC-00-002-004 Rev 2 (Código 2)",
        level=3)
    add_para(doc, [
        ("Se incorporaron los recubrimientos mínimos. A corregir en Rev 0:",)])
    obs(doc, "NOTA-01 (Transmittal N2) — Notación del peso del contenedor.",
        "La memoria mantiene la notación \"17.334 [tonf]\" para el peso del "
        "contenedor y no declara explícitamente que se adopta como valor "
        "conservador frente al peso vinculante (14.934 kg).",
        "corregir la notación del peso y declarar su adopción como valor "
        "conservador respecto del peso vinculante del contenedor RO.",
        "consistencia con el peso vinculante del contenedor RO.")

    # ---------- 2.2 Especificaciones ----------
    doc.add_heading("Especificaciones Técnicas", level=2)
    add_para(doc, [
        ("Las tres Especificaciones Técnicas quedan Código 1 — Aprobado. Se "
         "declaró la tensión admisible σ_adm ≤ 1,0 kg/cm² y se eliminó la "
         "referencia residual a Antofagasta (Movimiento de Tierra); se trasladó "
         "a la Especificación el esquema de protección C5-M por capas con su "
         "preparación de superficie (SSPC-SP10) y se exigió pernería galvanizada "
         "en caliente o inoxidable AISI 316 (Estructura Metálica); y se "
         "corrigieron los códigos de portada. No quedan observaciones "
         "pendientes.",)])

    # ---------- 2.3 Itemizados ----------
    doc.add_heading("Itemizados de Presupuesto", level=2)
    add_para(doc, [
        ("Los tres Itemizados incorporaron las correcciones de fondo del "
         "Transmittal N3 (tag de la fosa a TK-06-004, eliminación de la pestaña "
         "ajena \"La Chimba\", impermeabilización y protección C5-M) y quedan "
         "Código 2 — Aprobado con comentarios. Resta incorporar en Rev 0:",)])
    obs(doc, "OBS-01 (Transmittal N2) — Clase de estimación.",
        "Los tres Itemizados no declaran la clase de estimación (mantienen el "
        "rótulo \"presupuesto referencial\").",
        "declarar la clase de estimación acordada en la reunión de arranque, la "
        "Clase 2 AACE.",
        "Minuta de reunión de arranque 067-032-032-COR-MI-001.")
    obs(doc, "OBS-02 (Transmittal N2) — Partida de soldadura (Itemizado de Estructura Metálica).",
        "El Itemizado de Estructura Metálica incorporó la protección C5-M, pero "
        "la soldadura sigue absorbida dentro de la partida \"Conexiones\" sin "
        "una línea propia.",
        "incorporar la partida de soldadura como ítem explícito, en línea con la "
        "Especificación de Estructura Metálica.",
        "consistencia Especificación-Itemizado.")

    # ---------- 2.4 Planos ----------
    doc.add_heading("Planos de Obras Civiles", level=2)
    add_para(doc, [
        ("Los planos repiten únicamente comentarios emitidos en transmittals "
         "anteriores que permanecen sin levantar; no se incorporan observaciones "
         "nuevas y los puntos ya resueltos no se listan. La columna Origen indica "
         "el transmittal donde se formuló cada comentario. Los identificadores "
         "OBS/NOTA coinciden con el PDF anotado (CC_ADASA) de cada lámina; cuando "
         "una lámina con comentario abierto no se re-emitió, el comentario se "
         "anota en la lámina entregada.",)])
    add_simple_table(doc, [
        ("Plano / Lámina", "ID", "Origen", "Comentario pendiente"),
        ("P22-DWG-00-001-001 L1", "OBS-01", "Transmittal N3",
         "Incorporar las excavaciones de las fundaciones (el plano cubre solo las "
         "zanjas de drenaje)."),
        ("P22-DWG-00-001-001 L1", "OBS-02", "Transmittal N3",
         "Especificar los rellenos (referir la Especificación de Movimiento de "
         "Tierra) y completar el cuadro de referencias."),
        ("P22-DWG-00-001-001 L2", "OBS-03", "Transmittal N3",
         "Declarar la pendiente longitudinal y la cota de empalme de la red de "
         "drenaje."),
        ("P22-DWG-00-001-001 L1/L2", "NOTA-01", "Transmittal N3",
         "Adoptar la nomenclatura CD-06-00N, rotular los tags y agregar la barra "
         "de escala; corregir el typo."),
        ("P22-DWG-00-002-002 L1 y L4", "OBS-01", "Transmittal N2",
         "Agregar la nota de mejoramiento de suelo."),
        ("P22-DWG-00-002-002 L2", "NOTA-01", "Transmittal N2",
         "Corregir la referencia al plano del proveedor a EX-26005-F01 Rev 0."),
        ("P22-DWG-00-002-003 L1", "OBS-01", "Transmittal N2",
         "Agregar la nota de mejoramiento de suelo y especificar el relleno."),
        ("P22-DWG-00-002-004 L1", "OBS-01", "Transmittal N2",
         "Definir la capa de mejoramiento de suelo (\"M.H.A.\")."),
        ("P22-DWG-00-002-004 L1/L2", "NOTA-01", "Transmittal N2",
         "Unificar el tag de la fosa a TK-06-004."),
        ("P22-DWG-00-002-004 L2", "OBS-02", "Transmittal N2",
         "Indicar y acotar el rebalse; especificar la parrilla como pultruida de "
         "PRFV."),
        ("P22-DWG-00-002-006 L1/L2", "OBS-01", "Transmittal N2",
         "Adoptar la nomenclatura CD-06-00N (re-emitir las láminas 1 y 2)."),
        ("P22-DWG-00-002-007 L1/L3", "OBS-01", "Transmittal N2",
         "Agregar las notas de mejoramiento de suelo e impermeabilización; "
         "corregir la fecha del cajetín."),
        ("P22-DWG-00-003-001 L2", "NOTA-01", "Transmittal N2",
         "Corregir la sigla del documento en la nota de protección C5-M "
         "(P22-ET-00-010-103-0)."),
    ])

    # =========================================================
    # 3. ADJUNTOS
    # =========================================================
    doc.add_heading("ADJUNTOS", level=1)
    add_para(doc, [
        ("Llevan PDF anotado (CC_ADASA) los documentos con observaciones "
         "abiertas: las Memorias de Cálculo P22-MC-00-002-001 y P22-MC-00-002-004 "
         "(Código 2), y los planos de obras civiles con comentario "
         "(P22-DWG-00-001-001, -002-002, -002-003, -002-004, -002-006, -002-007 "
         "y -003-001). Los tres Itemizados llevan el archivo Excel con notas. Las "
         "tres Memorias de Cálculo aprobadas y las tres Especificaciones Técnicas "
         "(Código 1) no llevan PDF anotado.",)])

    # =========================================================
    # 4. RESUMEN DE RESPUESTA
    # =========================================================
    doc.add_heading("RESUMEN DE RESPUESTA", level=1)
    add_simple_table(doc, [
        ("Código Documento", "Título", "Rev", "Código de Respuesta"),
        ("P22-MC-00-002-001", "Fundación Estanque TK-06-001", "2",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-002-002", "Fundación Dinámica Bomba BH-06-001", "2",
         "1 — Aprobado"),
        ("P22-MC-00-002-004", "Fundación Contenedor RO", "2",
         "2 — Aprobado con comentarios"),
        ("P22-MC-00-002-005", "Fundación Sistema CIP", "2",
         "1 — Aprobado"),
        ("P22-MC-00-003-001", "Cubierta Metálica Sistema CIP Exterior", "2",
         "1 — Aprobado"),
        ("P22-ET-00-010-101", "Especificación Movimiento de Tierra", "1",
         "1 — Aprobado"),
        ("P22-ET-00-010-102", "Especificación Obras Civiles", "1",
         "1 — Aprobado"),
        ("P22-ET-00-010-103", "Especificación Estructura Metálica", "1",
         "1 — Aprobado"),
        ("P22-IT-00-010-101", "Itemizado Movimiento de Tierra", "D",
         "2 — Aprobado con comentarios"),
        ("P22-IT-00-010-102", "Itemizado Obras Civiles", "D",
         "2 — Aprobado con comentarios"),
        ("P22-IT-00-010-103", "Itemizado Estructura Metálica", "D",
         "2 — Aprobado con comentarios"),
        ("P22-DWG-00-001-001", "Excavaciones y movimiento de tierra", "C",
         "3 — Por revisar"),
        ("P22-DWG-00-002-001", "Implantación general OOCC", "D",
         "1 — Aprobado"),
        ("P22-DWG-00-002-002", "Fundaciones equipos exteriores", "D",
         "3 — Por revisar"),
        ("P22-DWG-00-002-003", "Fundación contenedor RO", "D",
         "3 — Por revisar"),
        ("P22-DWG-00-002-004", "Fosa de drenajes", "D",
         "3 — Por revisar"),
        ("P22-DWG-00-002-006", "Canalizaciones y red de drenajes", "D",
         "2 — Aprobado con comentarios"),
        ("P22-DWG-00-002-007", "Fundaciones equipos Sistema CIP", "D",
         "3 — Por revisar"),
        ("P22-DWG-00-003-001", "Cubierta metálica Sistema CIP", "0",
         "3 — Por revisar"),
    ])
    add_para(doc, [
        ("Veredicto global del transmittal: 3 — POR REVISAR.",
         {"bold": True}),
        (" Las Memorias de Cálculo y las Especificaciones Técnicas convergieron "
         "(siete documentos Aprobados y dos Memorias con comentarios menores a "
         "Rev 0), y los tres Itemizados quedan Aprobados con comentarios. El "
         "veredicto lo fijan los planos de obras civiles: el plano de "
         "Excavaciones no incorpora las excavaciones de las fundaciones (sin lo "
         "cual las cubicaciones de los Itemizados no tienen sustento) y los "
         "planos de fundación mantienen ausente la nota de mejoramiento de suelo "
         "exigida por la Especificación de Movimiento de Tierra, con sus notas "
         "particulares sin cambios respecto de la revisión anterior. La Memoria "
         "de Cálculo del Sistema de Drenajes (P22-MC-00-002-003) y el plano de "
         "Detalles de Anclaje (P22-DWG-00-002-005) siguen pendientes de entrega "
         "por tercera vez consecutiva.",),
    ])

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    main()
