#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la consulta tecnica ADASA P22-CT-06-000-002-0 dirigida a Exfibro/Anwo
sobre el tratamiento del sismo vertical en la memoria del estanque TK-06-001.
"""

import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Skill global (path absoluto)
skill_path = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt, Cm

OUTPUT = os.path.join(SCRIPT_DIR, "P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx")
OUTPUT_CONSULTAS = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..",
    "REVISIONES", "CONSULTAS_TECNICAS",
    "P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx",
))


def add_para(doc, text, size=11, italic=False):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    if italic:
        run.italic = True
    return para


def add_quote(doc, text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Cm(0.75)
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.italic = True
    return para


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style=None)
        p.paragraph_format.left_indent = Pt(18)
        run = p.add_run("- " + item)
        run.font.name = "Arial"
        run.font.size = Pt(11)


def crear_documento():
    crear_documento_adasa(
        titulo="CONSULTA TECNICA: TRATAMIENTO DEL SISMO VERTICAL EN MEMORIA DE CALCULO ESTANQUE TK-06-001",
        codigo="P22-CT-06-000-002-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # Eliminar contenido placeholder
    elementos_a_eliminar = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos_a_eliminar.append(para)
    for para in elementos_a_eliminar:
        p = para._element
        p.getparent().remove(p)

    # ========================================================================
    # 1. ANTECEDENTES
    # ========================================================================
    doc.add_heading("ANTECEDENTES", level=1)

    add_para(doc,
        "ADASA ha revisado los antecedentes tecnicos del estanque de salmuera TK-06-001 "
        "entregados por Exfibro: el plano EX-26005-F01 Rev C y la memoria de calculo Memoria "
        "Estanque AFTA Taltal Rev. A (02-Mar-2026). La revision se enmarca en la preparacion "
        "de la licitacion de la ingenieria de detalle de obras civiles del proyecto Taltal.")

    add_para(doc,
        "La revision tecnica interna ADASA (P22-IT-06-000-005-0) confirma que los pernos M25 "
        "(1\") F1554 Gr.36 especificados cumplen las verificaciones de traccion, corte e "
        "interaccion incluso al incorporar la componente sismica vertical Cv = 0,267 con la "
        "combinacion 100/30 de NCh 2369 Of.2003. Sin embargo, se han identificado siete "
        "observaciones formales sobre la memoria que deben resolverse antes de que el documento "
        "pueda ser aceptado como antecedente final para el diseno de fundaciones por terceros.")

    add_para(doc,
        "La presente consulta solicita aclaraciones puntuales y la emision de una Rev B de la "
        "memoria que cierre estos aspectos.")

    # ========================================================================
    # 2. DOCUMENTOS DE REFERENCIA
    # ========================================================================
    doc.add_heading("DOCUMENTOS DE REFERENCIA", level=1)

    add_simple_table(doc, [
        ("#", "Codigo", "Documento", "Rev", "Rol"),
        ("1", "EX-26005-F01", "Plano vistas y detalles — Estanque vertical Diam. 2600 x H2570", "C", "Documento bajo consulta"),
        ("2", "—", "Memoria de calculo — Estanque Salmuera 10 m3", "A (02-Mar-2026)", "Documento bajo consulta"),
        ("3", "NCh 2369 Of.2003", "Diseno sismico de estructuras e instalaciones industriales", "—", "Norma de referencia"),
        ("4", "P22-IT-06-000-005-0", "Revision interna ADASA — Memoria TK-06-001", "0", "Analisis de soporte"),
    ])

    # ========================================================================
    # 3. CONSULTAS Y ACCIONES REQUERIDAS
    # ========================================================================
    doc.add_heading("CONSULTAS Y ACCIONES REQUERIDAS", level=1)

    # Q1
    doc.add_heading("Q1 — Origen del valor Ez = -2.514 kg en tabla de cargas basales (CRITICA)", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "La memoria reporta en la pagina 18, dentro de la tabla 'Cargas basales a nivel de "
        "fondo del equipo', la fila Ez con Fz = -2.514 kg, Mz = 0. El valor aparece sin "
        "desarrollo previo en el cuerpo de la memoria.")
    add_para(doc,
        "El cociente Ez / W_tot = 2.514 / 12.572 = 0,200 sugiere un coeficiente Cv = 0,20, "
        "valor que no corresponde a Cv = (2/3) Cmax con Cmax = 0,40 declarado en pagina 7 "
        "(lo cual daria Cv = 0,267 -> Ez = 3.357 kg).")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Mostrar explicitamente la formula utilizada para calcular Ez, incluyendo el coeficiente sismico vertical Cv y la masa o peso sobre el cual se aplica (W_total, W_impulsivo, W_vacio).",
        "Justificar normativamente el valor de Cv adoptado, citando la seccion de NCh 2369 que lo respalda.",
        "Si la formula correcta es Cv = (2/3) Cmax = 0,267, ratificar el valor de Ez en la tabla p.18 (deberia ser +/-3.357 kg, no -2.514).",
    ])

    # Q2
    doc.add_heading("Q2 — Version de NCh 2369 efectivamente aplicada (ALTA)", level=2)

    add_para(doc, "Estado actual:")
    add_bullets(doc, [
        "El plano EX-26005-F01 Rev C, en su cajetin, cita expresamente 'NCh 2369-2025'.",
        "La memoria de calculo Rev. A cita 'Nch 2369 y API STANDARD 650' sin indicar ano (pagina 7).",
        "Los parametros aplicados por la memoria (Cmax = 0,40 de tabla 5.7, R = 3 de tabla 5.6 con criterio 7.5 PRFV-GRP, xi_imp = 2 % y xi_conv = 0,5 % de tabla 5.5) corresponden a la estructura de NCh 2369 Of.2003.",
    ])

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Declarar explicitamente, en el documento Rev B, que version de NCh 2369 se aplico al diseno (Of.2003 o :2025).",
        "Si la respuesta es :2025, justificar por que los parametros de calculo son los de Of.2003 y reemplazarlos por los actualizados de :2025 (cuyos coeficientes Cmax y combinaciones direccionales difieren).",
        "Si la respuesta es Of.2003, modificar la nota del cajetin del plano EX-26005-F01 para que coincida con la memoria, o explicar formalmente la coexistencia de ambas referencias.",
    ])

    # Q3
    doc.add_heading("Q3 — Aplicacion del factor (1-Cv) al peso estabilizador en calculo de pernos (CRITICA)", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "En la pagina 11 de la memoria, bajo 'Diseno de anillo y sillas de anclaje', la "
        "traccion por perno se calcula como:")

    add_simple_table(doc, [
        ("Variable", "Calculo", "Valor"),
        ("Msr", "W D/2 con W = 586 kg (peso vacio)", "76.187 kg cm"),
        ("Mt", "M - Msr", "355.658 kg cm"),
        ("X", "Mt/(pi R^2)", "6,57 kg/cm"),
        ("P", "pi D X/N", "671 kg"),
        ("F", "P (a+b)/b", "1.007 kg"),
        ("tb", "F 1,5", "1.510 kg"),
    ])

    add_para(doc,
        "Esta formulacion NO incorpora el factor (1 - Cv) sobre el peso estabilizador W, que "
        "es el desarrollo exigido por NCh 2369 Of.2003 Sec. 5.5 para evaluar el caso "
        "desfavorable: el sismo vertical en su sentido descendente reduce la fuerza "
        "estabilizadora gravitatoria, lo que aumenta la traccion que reciben los pernos.")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Re-presentar el calculo de traccion de pernos aplicando explicitamente W -> W (1 - Cv) en la formula Msr = W (1 - Cv) D/2 para el caso desfavorable.",
        "Documentar el valor de Cv adoptado y su origen normativo.",
        "Reportar el nuevo valor de tb y la verificacion de esfuerzos resultante. ADASA ha realizado este calculo de manera independiente (memorando P22-IT-06-000-005-0) y obtiene tb = 1.537 kg con la combinacion 100/30; los pernos siguen cumpliendo, pero el desarrollo formal debe constar en la memoria.",
    ])

    # Q4
    doc.add_heading("Q4 — Peso estabilizador adoptado en el calculo de pernos (ALTA)", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "En la pagina 11 se utiliza W = 586 kg, que corresponde al peso vacio del estanque "
        "(manto + accesorios). El peso del fluido en operacion (11.986 kg) no se considera "
        "como estabilizador en la formula de traccion de pernos. Esta practica es habitual "
        "en estanques anclados PRFV cuando no se garantiza que el fluido este presente "
        "durante el sismo, pero no se declara explicitamente en la memoria.")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Declarar formalmente el criterio adoptado para el peso estabilizador: se considera estanque vacio en el caso desfavorable? se aplica el peso impulsivo W1 = 8.968 kg como masa que efectivamente acompana al estanque?",
        "Justificar la eleccion citando NCh 2369 Of.2003 Sec. 11 (estanques apoyados sobre el suelo) o la practica de ASME RTP-1 / API 650 Anexo E.",
    ])

    # Q5
    doc.add_heading("Q5 — Combinacion direccional H+V (MEDIA)", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "La memoria no documenta explicitamente como se combinan las componentes sismicas "
        "horizontal y vertical. Las cargas elementales (Ex, Ey, Ez) aparecen tabuladas en "
        "pagina 18 sin instruccion sobre como combinarlas para diseno de pernos o fundacion.")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Documentar en la memoria Rev B la combinacion direccional aplicada conforme NCh 2369 Of.2003 Sec. 5.5.2 (regla 100/30: 1,0 H +/- 0,3 V o 0,3 H +/- 1,0 V, la mas desfavorable).",
        "Indicar cual combinacion controla el diseno de pernos.",
    ])

    # Q6
    doc.add_heading("Q6 — Reparticion del corte basal entre pernos y topes sismicos (MEDIA)", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "El plano EX-26005-F01 Rev C muestra topes sismicos en la base del estanque, pero la "
        "memoria asume que los pernos toman todo el corte horizontal via la formula "
        "V_perno = V_basal/(N/3) 1,5, sin descontar la fraccion que tomarian los topes.")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Aclarar si los topes sismicos del plano son redundantes o si toman una fraccion del corte horizontal.",
        "Si toman corte, justificar la reparticion y revisar el calculo de V_perno en la memoria.",
        "Si son redundantes, indicarlo explicitamente para evitar interpretaciones contradictorias por terceros.",
    ])

    # Q7
    doc.add_heading("Q7 — Inconsistencia interna del factor de importancia I (MEDIA)", level=2)

    add_para(doc, "Estado actual:")
    add_bullets(doc, [
        "Memoria pagina 7 (verificacion sismica principal): 'Z = 3, I = 1,20'.",
        "Memoria pagina 16 (altura de ola por sloshing): 'Nch2369 I = 1,00'.",
    ])

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Resolver la inconsistencia adoptando un unico valor de I para todo el calculo del equipo.",
        "Justificar el valor adoptado citando Tabla 4.5 de NCh 2369 Of.2003 (categoria de ocupacion).",
    ])

    # Q8
    doc.add_heading("Q8 — Ratificacion de reacciones basales para ingenieria civil", level=2)

    add_para(doc, "Estado actual:")
    add_para(doc,
        "La tabla de cargas basales de pagina 18 sera utilizada por el consultor de obras "
        "civiles ADASA como entrada de diseno para la fundacion de hormigon armado y los "
        "topes/llaves de corte. Las observaciones Q1 a Q7 inciden directamente sobre los "
        "valores de esta tabla.")

    add_para(doc, "Accion requerida:")
    add_bullets(doc, [
        "Tras incorporar las correcciones Q1-Q7, ratificar o corregir formalmente la tabla de cargas basales p.18, incluyendo: cargas estaticas (peso propio, fluido), cargas sismicas Ex/Ey/Ez con signo +/- y valor numerico actualizado, y combinaciones recomendadas para diseno civil.",
        "Confirmar si la formula Mz (momento de torsion basal) es efectivamente cero o si debe calcularse para excentricidades del centro de masa.",
    ])

    # ========================================================================
    # 4. DOCUMENTOS A EMITIR
    # ========================================================================
    doc.add_heading("DOCUMENTOS A EMITIR", level=1)

    add_para(doc, "Se solicita a Exfibro/Anwo emitir, en respuesta a esta consulta:")

    add_simple_table(doc, [
        ("#", "Documento", "Accion"),
        ("1", "Memoria de calculo Rev. B", "Emision con correcciones Q1-Q7"),
        ("2", "Plano EX-26005-F01 Rev. D", "Si corresponde modificar la cita normativa del cajetin (Q2)"),
        ("3", "Tabla de reacciones basales actualizada", "Como anexo de Rev. B (Q8)"),
        ("4", "Respuesta narrativa", "Documento que aclare cada Q1-Q8 con referencia a paginas y secciones de la memoria Rev. B"),
    ])

    # ========================================================================
    # 5. PLAZOS
    # ========================================================================
    doc.add_heading("PLAZOS", level=1)

    add_para(doc,
        "ADASA solicita respuesta a esta consulta en un plazo de diez (10) dias habiles desde "
        "su emision, considerando que el material es antecedente directo para la licitacion "
        "de la ingenieria de detalle de obras civiles cuya emision esta prevista en el corto "
        "plazo.")

    # ========================================================================
    # 6. CONTACTO
    # ========================================================================
    doc.add_heading("CONTACTO", level=1)

    add_para(doc, "Para consultas tecnicas: Luis Rivera — luis.rivera@adasa.cl")

    add_quote(doc,
        "Esta consulta es emitida por ADASA y se traslada a Exfibro Ltda. a traves de Anwo "
        "(mandante del suministro). La trazabilidad documental se mantiene en "
        "REVISIONES/CONSULTAS_TECNICAS/P22-CT-06-000-002-0.")

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")

    # Copia trazable en CONSULTAS_TECNICAS
    if not os.path.exists(os.path.dirname(OUTPUT_CONSULTAS)):
        os.makedirs(os.path.dirname(OUTPUT_CONSULTAS))
    shutil.copy2(OUTPUT, OUTPUT_CONSULTAS)
    print(f"Copia: {OUTPUT_CONSULTAS}")


if __name__ == "__main__":
    crear_documento()
