#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el memorando ADASA P22-IT-06-000-005-0 — Revision de la memoria de
calculo del estanque TK-06-001 con foco en el tratamiento del sismo vertical
segun NCh 2369 Of.2003.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Skill global (path absoluto) - NO usar .claude/skills/ del proyecto
skill_path = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt

OUTPUT = os.path.join(SCRIPT_DIR, "P22-IT-06-000-005-0_Revision_Memoria_TK-06-001.docx")


def add_para(doc, text, size=11, italic=False):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    if italic:
        run.italic = True
    return para


def add_quote(doc, text):
    """Parrafo en cursiva con sangria izquierda — para notas y citas."""
    from docx.shared import Cm
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Cm(0.75)
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.italic = True
    return para


def crear_documento():
    crear_documento_adasa(
        titulo="REVISION DE MEMORIA DE CALCULO ESTANQUE TK-06-001 — TRATAMIENTO DEL SISMO VERTICAL SEGUN NCh 2369 OF.2003",
        codigo="P22-IT-06-000-005-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # Eliminar contenido placeholder del template
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

    # ============================================================
    # 1. ANTECEDENTES
    # ============================================================
    doc.add_heading("ANTECEDENTES", level=1)

    add_para(doc,
        "El estanque de salmuera TK-06-001 es de suministro ADASA para el Modulo de Salmuera "
        "de la Planta Desaladora Taltal. Es un estanque vertical de poliester reforzado con "
        "fibra de vidrio (PRFV), Diam. 2.625 mm x H 2.570 mm, volumen util 10 m3, peso vacio "
        "586 kg y peso en operacion con salmuera (gravedad especifica 1,05) de 12.572 kg.")

    add_para(doc,
        "El equipo es fabricado por Exfibro Ltda. bajo orden de compra Folio N. 834750. La "
        "memoria de calculo (Memoria Estanque AFTA Taltal.pdf, Rev. A, 02-Mar-2026) y el plano "
        "de fabricacion (EX-26005-F01 Rev C) acompanan al equipo y declaran las cargas que se "
        "transmiten a la fundacion de hormigon armado.")

    add_para(doc,
        "Durante la revision tecnica de los antecedentes para licitacion de la ingenieria de "
        "detalle de obras civiles, el equipo de ADASA identifico que el calculo de fuerzas en "
        "los pernos de anclaje no incorpora explicitamente la componente sismica vertical "
        "exigida por NCh 2369. El presente documento revisa la memoria EXFIBRO Rev. A contra "
        "los requisitos de NCh 2369 Of.2003 — norma con la que efectivamente se diseno el equipo, "
        "segun se desprende de los parametros aplicados (Z=3, I=1,2, Cmax=0,40, R=3, "
        "amortiguamiento impulsivo 2 % y convectivo 0,5 %) — y produce un re-calculo "
        "independiente para validar si los pernos especificados cumplen con la combinacion "
        "correcta H+V.")

    add_quote(doc,
        "Nota normativa: El plano EX-26005-F01 Rev C cita 'NCh 2369-2025' en su cajetin, "
        "mientras que los terminos de referencia de OOCC ADASA (P22-TR-00-010-01-1) exigen "
        "NCh 2369:2025. La memoria EXFIBRO no declara ano de la norma. La presente revision "
        "se realiza contra NCh 2369 Of.2003 por decision expresa del proyecto, en consideracion "
        "a que los parametros usados por EXFIBRO corresponden a esa version. La discrepancia "
        "normativa entre plano y memoria es por si misma una observacion que se traslada a "
        "EXFIBRO en la consulta tecnica P22-CT-06-000-002-0.")

    # ============================================================
    # 2. ALCANCE
    # ============================================================
    doc.add_heading("ALCANCE DE LA REVISION", level=1)

    add_para(doc,
        "La revision esta acotada al minimo critico: verificacion del par traccion/corte en "
        "los 8 pernos de anclaje M25 (1\") F1554 Gr.36 con la combinacion H+V correcta segun "
        "NCh 2369 Of.2003 articulos 5.5.2 y 5.5.3. No se rehace la cadena completa de "
        "Housner-momentos-fundacion civil; se acepta el calculo de masas impulsiva/convectiva, "
        "periodos y momentos volcantes horizontales reportados por EXFIBRO, y se modifica "
        "unicamente el peso estabilizador para reflejar el efecto vertical sismico.")

    add_para(doc, "Excluido del alcance:")
    for item in [
        "Revision de masa impulsiva/convectiva (modelo Housner)",
        "Revision de periodos T_imp / T_conv",
        "Revision de pandeo combinado del manto",
        "Diseno de fundacion civil (responsabilidad del consultor OOCC)",
        "Verificacion estructural de los topes sismicos del plano",
    ]:
        p = doc.add_paragraph(style=None)
        p.paragraph_format.left_indent = Pt(18)
        run = p.add_run("- " + item)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    # ============================================================
    # 3. DOCUMENTOS DE REFERENCIA
    # ============================================================
    doc.add_heading("DOCUMENTOS DE REFERENCIA", level=1)

    add_simple_table(doc, [
        ("#", "Codigo", "Documento", "Rev", "Origen"),
        ("1", "EX-26005-F01", "Plano vistas y detalles — Estanque vertical Diam. 2600 x H2570", "C", "Exfibro"),
        ("2", "—", "Memoria de calculo — Estanque Salmuera 10 m3", "A", "Exfibro"),
        ("3", "NCh 2369 Of.2003", "Diseno sismico de estructuras e instalaciones industriales", "—", "INN"),
        ("4", "ASME RTP-1", "Reinforced thermoset plastic corrosion-resistant equipment", "2017/2021", "ASME"),
        ("5", "API 650 Anexo E", "Welded tanks for oil storage — seismic design", "—", "API"),
        ("6", "P22-TR-00-010-01", "TdR Ingenieria de detalle OOCC y estructuras metalicas", "1", "ADASA"),
    ])

    # ============================================================
    # 4. DATOS DE ENTRADA
    # ============================================================
    doc.add_heading("DATOS DE ENTRADA", level=1)

    doc.add_heading("Geometria y masas (memoria EXFIBRO Rev. A)", level=2)
    add_simple_table(doc, [
        ("Parametro", "Valor", "Unidad"),
        ("Diametro interior D", "2.600", "mm"),
        ("Altura manto Hss", "2.570", "mm"),
        ("Altura liquido operacion", "2.150", "mm"),
        ("Espesor manto inferior T2", "4,80", "mm"),
        ("Peso vacio W_vessel", "586", "kg"),
        ("Peso fluido W_cont", "11.986", "kg"),
        ("Peso total W_tot", "12.572", "kg"),
        ("Masa impulsiva W1 (W1/Wt = 0,736)", "8.968", "kg"),
        ("Masa convectiva W2 (W2/Wt = 0,277)", "3.368", "kg"),
    ])

    doc.add_heading("Anclajes (plano EX-26005-F01 RevC + memoria p.11)", level=2)
    add_simple_table(doc, [
        ("Parametro", "Valor", "Unidad"),
        ("Cantidad de pernos N", "8", "—"),
        ("Diametro nominal", "1\" (M25)", "—"),
        ("Diametro raiz dp", "2,14", "cm"),
        ("Material", "F1554 Gr.36 (ASTM A307 Gr.C)", "—"),
        ("Fluencia Fy", "248", "MPa"),
        ("BCD (bolt circle diameter)", "2.755", "mm"),
        ("Radio R = BCD/2", "131,2", "cm"),
        ("Distancia carga P-perno (a)", "65", "mm"),
        ("Distancia perno-ancla A (b)", "130", "mm"),
        ("Altura silla h", "140", "mm"),
    ])

    doc.add_heading("Parametros sismicos NCh 2369 Of.2003 (verificados contra memoria)", level=2)
    add_simple_table(doc, [
        ("Parametro", "Simbolo", "Valor", "Referencia Of.2003"),
        ("Zona sismica", "Z", "3", "Tabla 4.1"),
        ("Aceleracion efectiva", "A0/g", "0,40 g", "Tabla 4.2 (Zona 3)"),
        ("Tipo de suelo (asumido)", "—", "II", "Tabla 4.3 — confirmar c/geotecnico"),
        ("Categoria de ocupacion", "—", "C2", "Tabla 4.5"),
        ("Coef. importancia", "I", "1,20", "Tabla 4.5 (consistente con memoria p.7)"),
        ("Razon amortiguamiento impulsivo", "xi_imp", "2 %", "Tabla 5.5"),
        ("Razon amortiguamiento convectivo", "xi_conv", "0,5 %", "Tabla 5.5"),
        ("Factor modificacion respuesta", "R", "3,0", "Tabla 5.6"),
        ("Coef. sismico horizontal maximo", "Cmax", "0,40", "Tabla 5.7"),
        ("Coef. sismico convectivo (memoria)", "Cc", "0,103", "p.7 memoria — formula Sec. 11.8.8 Of.2003"),
        ("Coef. sismico vertical (Of.2003 Sec. 5.5.3)", "Cv", "(2/3) Cmax = 0,267", "Sec. 5.5.3 Of.2003"),
    ])

    doc.add_heading("Cargas resultantes (memoria EXFIBRO p.7-8)", level=2)
    add_simple_table(doc, [
        ("Magnitud", "Valor", "Unidad"),
        ("Cortante basal V (combinado SRSS)", "4.617", "kg"),
        ("Momento volcante M_base (SRSS imp+conv)", "431.846", "kg cm"),
        ("M impulsivo (sobre base)", "380.871", "kg cm"),
        ("M convectivo (sobre base)", "213.158", "kg cm"),
        ("Fz reportado en tabla p.18", "-2.514", "kg"),
    ])

    # ============================================================
    # 5. HALLAZGOS
    # ============================================================
    doc.add_heading("HALLAZGOS DE LA REVISION", level=1)

    add_simple_table(doc, [
        ("#", "Hallazgo", "Severidad", "Pagina memoria"),
        ("H1",
         "Ez = -2.514 kg aparece en la tabla de cargas basales sin desarrollo previo. El cociente Ez/W_tot = 0,20 sugiere Cv = (2/3) 0,30, valor que no corresponde a Cmax = 0,40 declarado. Origen no trazable.",
         "CRITICA", "p.18"),
        ("H2",
         "La formula de traccion del perno tb = 1.510 kg (p.11-12) se construye como Msr = W D/2 -> Mt = M - Msr -> X = Mt/(pi R^2) -> P = pi D X/N -> F = P (a+b)/b -> tb = F 1,5. NO incluye factor (1-Cv) sobre el peso estabilizador W, que es el desarrollo exigido por NCh 2369 Of.2003 Sec. 5.5 para el caso desfavorable.",
         "CRITICA", "p.11-12"),
        ("H3",
         "Discrepancia de version normativa: plano EX-26005-F01 RevC cita 'NCh 2369-2025' en cajetin; la memoria solamente 'Nch 2369 y API STANDARD 650' sin ano, pero los parametros aplicados (Cmax = 0,40 de tabla 5.7, R = 3 de tabla 5.6 con criterio 7.5 PRFV-GRP, xi_imp/xi_conv = 2 %/0,5 %) son los de Of.2003. Posible incoherencia entre diseno y plano.",
         "ALTA", "Plano cajetin; mem. p.7"),
        ("H4",
         "Inconsistencia interna en factor de importancia: memoria p.7 usa I = 1,20; memoria p.16 (calculo de altura de ola por sloshing) usa I = 1,00. Los dos valores no pueden ser simultaneamente correctos para un mismo equipo.",
         "MEDIA", "p.7 vs p.16"),
        ("H5",
         "Combinacion direccional H+V no documentada explicitamente en la memoria. NCh 2369 Of.2003 Sec. 5.5.2 requiere aplicar la regla 100/30 (1,0 H +/- 0,3 V o 0,3 H +/- 1,0 V, la combinacion mas desfavorable).",
         "MEDIA", "p.7-8, p.18"),
        ("H6",
         "Verificacion de interaccion sigma/sigma_adm + tau/tau_adm reportada como 0,92 (p.12). El recalculo con los valores de la propia memoria da 0,21 + 0,73 = 0,94. Diferencia menor pero indica que el valor presentado no es trazable directamente. Debe rehacerse con la nueva traccion que incluya Cv.",
         "MEDIA", "p.12"),
        ("H7",
         "Peso estabilizador utilizado en Msr = W D/2 corresponde solo al peso vacio del manto W = 586 kg (p.11). Este valor es trazable pero conservador frente al uso del peso operacional total (12.572 kg). Es coherente con la practica habitual para estanques anclados PRFV; la memoria debe declararlo explicitamente.",
         "MEDIA", "p.11"),
    ])

    # ============================================================
    # 6. RE-CALCULO
    # ============================================================
    doc.add_heading("RE-CALCULO INDEPENDIENTE ADASA", level=1)

    doc.add_heading("Reproduccion del procedimiento EXFIBRO (sanity check)", level=2)
    add_para(doc,
        "Aplicando la formula textual de la memoria p.11 con los parametros declarados:")

    add_simple_table(doc, [
        ("Variable", "Formula", "Valor calculado", "Valor memoria"),
        ("Msr", "W D/2 = 586 260/2", "76.180 kg cm", "76.187 kg cm"),
        ("Mt", "M - Msr = 431.846 - 76.180", "355.666 kg cm", "355.658 kg cm"),
        ("X", "Mt/(pi R^2)", "6,58 kg/cm", "6,57 kg/cm"),
        ("P", "pi D X/N", "671,5 kg", "671 kg"),
        ("F", "P (a+b)/b", "1.007,3 kg", "1.007 kg"),
        ("tb", "F 1,5", "1.510,9 kg", "1.510 kg (OK)"),
    ])

    add_para(doc,
        "Reproduccion al 99,9 %. El procedimiento EXFIBRO queda confirmado. La diferencia es "
        "explicable por redondeos intermedios.")

    doc.add_heading("Aplicacion de Cv = 0,267 con regla 100/30 (Caso A)", level=2)

    add_para(doc,
        "El sismo horizontal dominante (1,0 H + 0,3 V) tipicamente controla el diseno de pernos "
        "en estanques anclados con baja relacion altura/diametro:")

    add_simple_table(doc, [
        ("Variable", "Calculo", "Valor"),
        ("Cv efectivo", "0,3 0,267", "0,080"),
        ("W_eff", "586 (1 - 0,080)", "539,1 kg"),
        ("M_eff", "1,0 431.846", "431.846 kg cm"),
        ("Msr_eff", "W_eff D/2", "70.080 kg cm"),
        ("Mt_eff", "M_eff - Msr_eff", "361.766 kg cm"),
        ("X_eff", "Mt_eff /(pi R^2)", "6,69 kg/cm"),
        ("P_eff", "pi D X_eff /N", "683,3 kg"),
        ("F_eff", "P_eff (a+b)/b", "1.024,9 kg"),
        ("tb_eff", "F_eff 1,5", "1.537 kg (+1,7 % vs 1.510)"),
    ])

    doc.add_heading("Verificacion de esfuerzos con Cv = 0,267", level=2)

    add_simple_table(doc, [
        ("Magnitud", "Valor", "Admisible", "Veredicto"),
        ("sigma traccion", "427 kg/cm2", "0,8 Fy = 2.024 kg/cm2", "CUMPLE (sigma/sigma_adm = 0,211)"),
        ("tau corte", "722 kg/cm2", "0,4 Fy = 992 kg/cm2", "CUMPLE (tau/tau_adm = 0,728)"),
        ("Interaccion sigma+tau", "0,939", "<= 1,0", "CUMPLE"),
    ])

    doc.add_heading("Comparacion EXFIBRO vs ADASA", level=2)
    add_simple_table(doc, [
        ("Magnitud", "EXFIBRO Rev.A (sin Cv)", "ADASA (Caso A 100/30)", "Delta %", "Veredicto"),
        ("Traccion tb", "1.510,9 kg", "1.537 kg", "+1,7 %", "Aumenta — caso desfavorable"),
        ("sigma traccion", "420 kg/cm2", "427 kg/cm2", "+1,7 %", "sigma_adm = 2.024 -> CUMPLE"),
        ("Corte V_perno", "2.597 kg", "2.597 kg", "0,0 %", "Sin cambio (V no afecta por Cv)"),
        ("tau corte", "723 kg/cm2", "723 kg/cm2", "0,0 %", "tau_adm = 992 -> CUMPLE"),
        ("Interaccion sigma+tau", "0,939", "0,939", "+0,0 %", "<= 1 -> CUMPLE"),
    ])

    doc.add_heading("Casos alternativos evaluados", level=2)
    add_simple_table(doc, [
        ("Caso", "Combinacion", "tb (kg)", "Comentario"),
        ("0", "EXFIBRO sin Cv (referencia)", "1.510,9", "—"),
        ("A", "1,0 H + 0,3 V (regla 100/30)", "1.537", "Controla diseno en este equipo"),
        ("B", "0,3 H + 1,0 V", "313,7", "No critico — el momento horizontal reducido domina"),
        ("C", "1,0 H + 1,0 V (suma directa)", "1.601", "Cota superior — no exigido por norma"),
    ])

    # ============================================================
    # 7. VEREDICTO
    # ============================================================
    doc.add_heading("VEREDICTO", level=1)

    add_para(doc,
        "Los 8 pernos M25 (1\") F1554 Gr.36 especificados por EXFIBRO siguen cumpliendo la "
        "verificacion de traccion, corte e interaccion aun cuando se incorpora la componente "
        "sismica vertical Cv = 0,267 con la combinacion 100/30 exigida por NCh 2369 Of.2003. "
        "La interaccion sigma/sigma_adm + tau/tau_adm se mantiene en 0,939, esencialmente sin "
        "cambio respecto al calculo original de EXFIBRO (0,939 tambien, dado que el corte por "
        "perno — que domina la interaccion — no se ve afectado por Cv).")

    add_para(doc,
        "Sin embargo, la memoria de calculo EXFIBRO Rev. A presenta incumplimientos formales "
        "que deben corregirse para una entrega definitiva:")

    for item in [
        "Falta el desarrollo explicito del coeficiente sismico vertical Cv segun NCh 2369 Of.2003 Sec. 5.5.3, con su formula Cv = (2/3) Ah y su aplicacion a las combinaciones de carga.",
        "La componente vertical Ez = -2.514 kg que aparece en la tabla de cargas basales (p.18) no es trazable a una formula explicita; el cociente Ez/W_tot = 0,20 sugiere Cv = (2/3) 0,30, pero la memoria declara Cmax = 0,40, lo que daria Cv = 0,267. La inconsistencia debe resolverse documentalmente.",
        "La formula de traccion del perno debe re-presentarse mostrando explicitamente como Cv afecta el peso estabilizador W -> W (1-Cv) en el caso desfavorable, conforme Sec. 5.5.",
        "La combinacion direccional H+V (regla 100/30 segun Sec. 5.5.2) debe documentarse explicitamente.",
    ]:
        p = doc.add_paragraph(style=None)
        p.paragraph_format.left_indent = Pt(18)
        run = p.add_run("- " + item)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    add_para(doc,
        "Estos incumplimientos no comprometen la integridad estructural del estanque tal como "
        "se ha disenado, pero impiden que la memoria sea aceptada como antecedente "
        "autocontenido para revision por terceros (ingeniero civil de OOCC, auditor externo, "
        "autoridad).")

    add_quote(doc,
        "Recomendacion: ADASA debe emitir consulta tecnica formal a EXFIBRO/Anwo "
        "(P22-CT-06-000-002-0) solicitando una revision de la memoria que: (a) declare "
        "explicitamente la version normativa aplicada (Of.2003), (b) muestre el calculo de "
        "Cv con su formula, (c) reporte la traccion de pernos con la combinacion 100/30 y "
        "(d) ratifique las reacciones basales que se entregan al ingeniero civil.")

    # ============================================================
    # 8. REACCIONES BASALES PARA INGENIERIA CIVIL
    # ============================================================
    doc.add_heading("REACCIONES BASALES PARA INGENIERIA CIVIL — VALORES CORREGIDOS", level=1)

    add_para(doc,
        "Las cargas que el consultor OOCC debe utilizar para el diseno de la fundacion de "
        "hormigon armado del estanque TK-06-001 deben incluir explicitamente la componente "
        "sismica vertical. Se presenta la tabla corregida a continuacion; la memoria EXFIBRO "
        "debe ratificar estos valores antes de su uso final.")

    doc.add_heading("Cargas estaticas", level=2)
    add_simple_table(doc, [
        ("Combinacion", "Fx (kg)", "Fy (kg)", "Fz (kg)", "Mx (kg cm)", "My (kg cm)"),
        ("Peso propio (estanque)", "0", "0", "-586", "0", "0"),
        ("Fluido en operacion", "0", "0", "-11.986", "0", "0"),
        ("Carga total estatica", "0", "0", "-12.572", "0", "0"),
    ])

    doc.add_heading("Cargas sismicas (NCh 2369 Of.2003 — Cmax = 0,40 ; Cv = 0,267 ; I = 1,20)", level=2)
    add_simple_table(doc, [
        ("Combinacion", "Fx (kg)", "Fy (kg)", "Fz (kg)", "Mx (kg cm)", "My (kg cm)"),
        ("Sismo Ex (100 % H)", "+/-4.617", "0", "0", "0", "+/-431.846"),
        ("Sismo Ey (100 % H)", "0", "+/-4.617", "0", "+/-431.846", "0"),
        ("Sismo Ez (100 % V — Cv W_tot)", "0", "0", "+/-3.357", "0", "0"),
    ])

    add_quote(doc,
        "Notas: (1) Ez corregido = +/- Cv W_tot = 0,267 12.572 = 3.357 kg (vs 2.514 declarado "
        "por EXFIBRO). El signo es +/-, no solo negativo: el caso desfavorable para traccion "
        "de pernos es +Cv (peso reducido); el caso desfavorable para compresion en losa es "
        "-Cv (peso aumentado). (2) La regla 100/30 entre componentes H y V debe aplicarla el "
        "ingeniero civil sobre estas cargas elementales. (3) Estas cargas no incluyen viento "
        "(NCh 432 / ASCE 7) ni cargas termicas, que deben evaluarse por separado conforme TdR "
        "OOCC.")

    # ============================================================
    # 9. RECOMENDACIONES
    # ============================================================
    doc.add_heading("RECOMENDACIONES", level=1)

    doc.add_heading("A EXFIBRO/Anwo (via consulta tecnica P22-CT-06-000-002-0)", level=2)
    for item in [
        "Emitir Rev B de la memoria de calculo declarando explicitamente: version NCh 2369 utilizada, formula de Cv, peso estabilizador adoptado, combinacion H+V aplicada (regla 100/30) y verificacion de pernos con la combinacion corregida.",
        "Aclarar el origen del valor Ez = -2.514 kg de la tabla p.18 y, si corresponde, ratificar o corregir las reacciones basales que recibe el ingeniero civil.",
        "Resolver la inconsistencia normativa entre plano (NCh 2369-2025) y memoria (parametros de Of.2003): declarar formalmente cual norma rige el diseno, modificando el plano si fuese necesario.",
        "Resolver la inconsistencia interna del factor de importancia I (1,20 en p.7 vs 1,00 en p.16).",
        "Documentar la reparticion del corte basal entre pernos y topes sismicos del plano, indicando que fraccion del esfuerzo horizontal toma cada elemento.",
    ]:
        p = doc.add_paragraph(style=None)
        p.paragraph_format.left_indent = Pt(18)
        run = p.add_run("- " + item)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    doc.add_heading("A ADASA — uso interno", level=2)
    for item in [
        "Trasladar al consultor de OOCC las cargas basales corregidas (con Ez = +/- 3.357 kg, no -2.514 kg) para el diseno de la fundacion.",
        "No aceptar la memoria EXFIBRO Rev. A como antecedente final hasta que se emita la Rev B con las correcciones formales.",
        "Verificar con Anwo si la fabricacion del estanque (en curso) refleja efectivamente el diseno con los parametros de Of.2003 declarados en la memoria, dado que el plano cita 'NCh 2369-2025'.",
    ]:
        p = doc.add_paragraph(style=None)
        p.paragraph_format.left_indent = Pt(18)
        run = p.add_run("- " + item)
        run.font.name = "Arial"
        run.font.size = Pt(11)

    # ============================================================
    # 10. ANEXOS
    # ============================================================
    doc.add_heading("ANEXOS", level=1)
    add_para(doc, "Anexo A — Planilla de calculo independiente: calculo_pernos_TK-06-001_ADASA.xlsx (5 hojas: Datos, Sismo Of.2003, Memoria EXFIBRO, Re-calculo ADASA, Comparacion).")
    add_para(doc, "Anexo B — Consulta tecnica formal: P22-CT-06-000-002-0_Sismo-Vertical-Pernos-Estanque.docx.")

    doc.save(OUTPUT)
    print(f"Generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
