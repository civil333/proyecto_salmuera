#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Especificacion Tecnica de Montaje de Canerias HDPE
P22-ET-06-007-002-0 Rev 1 usando template-adasa v7.4.

Alcance:
    - 100% HDPE PE100 SDR17 PN10 (335 m totales) - sin PVC, sin butt fusion
    - Solo uniones por electrofusion (cuplas, codos, tees, reducciones, stub ends)
    - Aportes ADASA: valvulas, instrumentos in-line, soportes fabricados
    - Suministros Contratista: TODA la tuberia y accesorios HDPE + perneria + juntas

Salida:
    P22-ET-06-007-002-0_MONTAJE-CANERIAS-HDPE_ADASA.docx
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    add_simple_table,
    add_bullet,
    add_numbered_item,
    add_numbered_list,
)
from docx import Document  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402

try:
    from docx_metadata import apply_core_properties, fix_app_xml  # noqa: E402
    METADATA_DISPONIBLE = True
except ImportError:
    METADATA_DISPONIBLE = False

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURAS_DIR = os.path.join(SCRIPT_DIR, "figuras")
OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-ET-06-007-002-0_MONTAJE-CANERIAS-HDPE_ADASA.docx",
)


def add_para(doc, text, size=11, justify=True):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p


def add_para_bold_lead(doc, lead, body, size=11):
    p = doc.add_paragraph()
    r1 = p.add_run(lead)
    r1.bold = True
    r1.font.name = "Arial"
    r1.font.size = Pt(size)
    r2 = p.add_run(body)
    r2.font.name = "Arial"
    r2.font.size = Pt(size)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p


def add_titulo_tabla(doc, label):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(label)
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    return p


def add_figura(doc, filename, leyenda, ancho_cm=15):
    path = os.path.join(FIGURAS_DIR, filename)
    if not os.path.exists(path):
        print(f"  [aviso] figura no encontrada: {filename}")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    r.add_picture(path, width=Cm(ancho_cm))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_r = cap.add_run(leyenda)
    cap_r.italic = True
    cap_r.font.name = "Arial"
    cap_r.font.size = Pt(10)


# ---------------------------------------------------------------------------
# 1 Generalidades
# ---------------------------------------------------------------------------


def construir_generalidades(doc):
    doc.add_heading("GENERALIDADES", level=1)

    doc.add_heading("Introduccion", level=2)
    add_para(
        doc,
        "Aguas de Antofagasta S.A. (en adelante ADASA) ejecuta el proyecto "
        "Modulo de Salmuera Taltal, que incorpora a la planta de osmosis "
        "inversa existente un sistema de proceso con canerias HDPE PE100 "
        "SDR17 PN10 tendidas en disposicion aerea sobre estructuras y "
        "soporteria metalica. Las obras civiles, la soporteria metalica "
        "fabricada por tercero y la fabricacion de los materiales son "
        "alcance de otros pliegos y otros contratistas; la presente "
        "especificacion cubre exclusivamente el montaje en obra de las "
        "canerias HDPE listadas en el Listado de Materiales "
        "P22-LI-06-006-102-0, incluidas la instalacion en linea de las "
        "valvulas e instrumentos in-line aportados por ADASA.",
    )

    doc.add_heading("Objeto y Alcance", level=2)
    add_para(
        doc,
        "Este documento establece los requisitos tecnicos que debe cumplir "
        "el contratista de montaje (en adelante el Contratista) para "
        "ejecutar la instalacion, las uniones por electrofusion, la "
        "soporteria, las pruebas hidrostaticas, el flushing, la "
        "instalacion de valvulas e instrumentos in-line y la entrega "
        "documental del sistema de canerias HDPE del Area 06 (aereo en "
        "proceso e interconexiones, y enterrado en el tramo de drenaje), a "
        "entera satisfaccion de ADASA.",
    )
    add_para(doc, "El alcance abarca:")
    for it in [
        "Tuberia HDPE PE100 SDR17 PN10 conforme ISO 4427-2, en DN50, DN80, DN100 y DN150, con un total de 335 m lineales segun el Listado de Materiales.",
        "Accesorios HDPE moldeados por electrofusion (codos 90 y 45, tees, manguitos, reducciones), bridas tipo lap joint con stub end electrofundido al tubo, accesorios saddle.",
        "Perneria en acero inoxidable AISI 316 (ASTM A193 Gr.B8M Cl.2) y juntas planas NBR/SBR conforme ASME B16.21.",
        "Instalacion en linea de valvulas mariposa, valvulas check e instrumentos in-line aportados por ADASA, con sus juntas y perneria del lado HDPE provistos por el Contratista.",
        "Instalacion del tramo enterrado de la red de drenaje (linea AMF-HDPE-DN160 y conexas): preparacion de la cama, bajada, relleno, compactacion y senalizacion, conforme al capitulo de Instalacion de Canerias Enterradas.",
    ]:
        add_bullet(doc, it)

    add_para(doc, "El alcance NO incluye:")
    for it in [
        "La proteccion anticorrosiva de canerias de acero enterradas (proteccion catodica, revestimiento epoxico AWWA C210, cintas anticorrosivas AWWA C209): no aplica al HDPE, que es inerte a la corrosion. El tramo de drenaje enterrado si esta dentro del alcance (ver el capitulo de Instalacion de Canerias Enterradas).",
        "Canerias metalicas y sus procesos de soldadura, NDT por radiografia, ultrasonido, particulas magneticas o liquidos penetrantes, ni pickling/pasivado.",
        "Canerias PVC-U; el sistema del proyecto Taltal es 100 % HDPE PE100 segun el Listado de Materiales.",
        "Termofusion a tope (butt fusion); todas las uniones tubo-tubo del proyecto se ejecutan por electrofusion, conforme a las isometrias y al Listado de Materiales.",
        "La fabricacion, suministro y certificacion de origen de los materiales de caneria, accesorios, bridas, perneria y juntas, que son aporte del Contratista regulado por la ET de Canerias de Fabricacion P22-ET-06-006-001-0.",
        "El montaje electromecanico de equipos rotativos y estanques, cubierto por la ET de Montaje Electromecanico P22-ET-06-007-001-0.",
        "El montaje de canerias y accesorios interiores del contenedor del modulo de osmosis inversa, alcance del proveedor del equipo.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Documentos de Referencia", level=2)
    add_titulo_tabla(doc, "Tabla 1.1 — Documentos de Referencia.")
    add_simple_table(doc, [
        ("Codigo", "Documento", "Revision", "Emisor"),
        ("BL_MONTAJE_TALTAL", "Bases de Licitacion de Montaje Mecanico y Obras Civiles", "0", "ADASA"),
        ("P22-ET-06-006-001-0", "Especificacion Tecnica de Canerias (Fabricacion)", "0", "ADASA"),
        ("P22-LI-06-006-102-0", "Listado de Materiales - Canerias Area 06", "0", "ADASA"),
        ("P22-ET-06-007-001-0", "Especificacion Tecnica de Montaje Electromecanico", "0", "ADASA"),
        ("P04-ET-00-006-102", "ET PDA Fabricacion y Montaje de Canerias (referencia metodologica)", "0", "ADASA / PDA"),
        ("Cuadernillo Isometrias", "P22-DWG-06-006-001 a -011", "0", "ADASA"),
    ])

    doc.add_heading("Normativa Aplicable", level=2)
    add_titulo_tabla(doc, "Tabla 1.2 — Normativa aplicable al montaje de canerias HDPE.")
    add_simple_table(doc, [
        ("Norma", "Aplicacion"),
        ("ISO 4427-2", "Tuberia HDPE PE100 - dimensiones y especificaciones"),
        ("ISO 4427-3", "Accesorios HDPE para sistemas de agua"),
        ("ISO 15494", "Accesorios HDPE para electrofusion (sistemas industriales)"),
        ("ISO 21307", "Procedimientos de fusion de PE (aplicacion: electrofusion)"),
        ("ISO 12176-3 / ISO 12176-4", "Calificacion de operadores de fusion de PE y codificacion de trazabilidad"),
        ("ISO 13954 / ISO 13955", "Ensayos de peel test para juntas electrofundidas"),
        ("ASTM F1055", "Electrofusion Type Polyethylene Fittings"),
        ("ASTM F2620", "Heat Fusion Joining of Polyethylene Pipe and Fittings (aplicacion: electrofusion)"),
        ("ASTM F2164", "Field Leak Testing of Polyethylene Pressure Piping Systems"),
        ("ASME B16.5", "Bridas Clase 150 - superficies de cara plana"),
        ("ASME B16.21", "Juntas planas no metalicas para bridas"),
        ("ASTM A193 / A194", "Perneria y tuercas inoxidables Grado B8M / 8M (SS316)"),
        ("PPI TN-38", "Bolt Torque for Polyethylene Flanged Joints"),
        ("DS N 594 / 2000", "Condiciones sanitarias y ambientales (Chile)"),
    ])

    doc.add_heading("Jerarquia Contractual", level=2)
    add_para(
        doc,
        "En caso de discrepancia entre los documentos del Proyecto, "
        "prevalecera el siguiente orden, de mayor a menor jerarquia: "
        "contrato y bases administrativas; presente Especificacion Tecnica; "
        "Especificacion Tecnica de Canerias de Fabricacion "
        "P22-ET-06-006-001-0; Listado de Materiales P22-LI-06-006-102-0; "
        "planos de implantacion e isometrias; documentacion de los "
        "fabricantes; normas referenciadas. El Contratista informara por "
        "escrito y de inmediato a ADASA cualquier omision o discrepancia "
        "detectada antes del inicio de la actividad afectada.",
    )


# ---------------------------------------------------------------------------
# 2 Suministros y Aportes
# ---------------------------------------------------------------------------


def construir_suministros(doc):
    doc.add_heading("SUMINISTROS Y APORTES", level=1)

    doc.add_heading("Aportes de ADASA", level=2)
    add_para(
        doc,
        "ADASA entregara al Contratista en bodega del recinto, contra "
        "inventario firmado, los siguientes elementos. La lista coincide con "
        "la Tabla de Suministros del BL_MONTAJE_TALTAL y reduce al minimo "
        "el aporte de ADASA al contratista de canerias (la tuberia, los "
        "accesorios y la perneria son aporte del Contratista).",
    )
    add_titulo_tabla(doc, "Tabla 2.1 — Aportes de ADASA al Contratista de canerias.")
    add_simple_table(doc, [
        ("Familia", "Detalle"),
        ("Valvulas mariposa", "Hasta 13 valvulas mariposa KSB ISORIA 10, DN50 a DN150, con TAGs VM-06-001 a VM-06-016 segun LI de Valvulas y P&ID"),
        ("Valvulas check", "2 valvulas check Duo super duplex (VR-06-001, VR-06-003)"),
        ("Instrumentos in-line", "7 instrumentos del Area 06: switches y transmisores de nivel (LSH, LSL, LIT), transmisor e indicador de presion (PI, PIT), transmisor de caudal (FIT)"),
        ("Soportes metalicos", "Soportes fabricados por tercero, tipos SP-01 a SP-11, en acero A36"),
        ("Documentacion de proyecto", "Planos isometricos aprobados para construccion (P22-DWG-06-006-001 a -011), LI de Materiales, LI de Lineas, P&ID aprobado"),
        ("Certificados", "Certificados de origen y de pruebas de fabrica de las valvulas e instrumentos entregados"),
    ])
    add_para(
        doc,
        "Los aportes ADASA enumerados se entregan en bodega del recinto "
        "contra acta firmada por el Contratista; el Contratista asume su "
        "custodia y responsabilidad desde la firma del acta hasta la entrega "
        "final del montaje.",
    )

    doc.add_heading("Suministros del Contratista", level=2)
    add_para(
        doc,
        "El Contratista aporta la totalidad de los materiales de caneria "
        "conforme al BL_MONTAJE_TALTAL y a la Especificacion Tecnica de "
        "Canerias P22-ET-06-006-001-0, y los recursos humanos, herramientas "
        "y consumibles necesarios para el montaje. Especificamente:",
    )
    add_para_bold_lead(doc, "Materiales de caneria y accesorios: ", "")
    for it in [
        "Toda la tuberia HDPE PE100 SDR17 PN10 conforme ISO 4427-2, en DN50 (1 m), DN80 (151 m), DN100 (180 m) y DN150 (3 m), totalizando 335 m lineales conforme al Listado de Materiales P22-LI-06-006-102-0.",
        "75 codos 90 HDPE para electrofusion (DN100: 41, DN80: 32, DN150: 1, DN50: 1).",
        "17 codos 45 HDPE para electrofusion (DN100: 11, DN80: 6).",
        "5 tees iguales HDPE para electrofusion (DN100: 2, DN80: 2, DN150: 1).",
        "66 cuplas / manguitos de electrofusion.",
        "7 reducciones HDPE.",
        "46 bridas Lap Joint + 47 stub ends HDPE para electrofusion.",
        "3 accesorios saddle (1 branch 6''x3'' + 2 spigot 4''x1'').",
        "224 esparragos inoxidables ASTM A193 Gr.B8M Cl.2 (SS316) + tuercas y golillas correspondientes.",
        "45 juntas planas NBR/SBR de 1/8'' conforme ASME B16.21.",
    ]:
        add_bullet(doc, it)

    add_para_bold_lead(doc, "Equipos, herramientas y consumibles: ", "")
    for it in [
        "Mano de obra directa, indirecta y supervision tecnica calificada para los trabajos de montaje de canerias HDPE.",
        "Maquina de electrofusion con codigo de barras y registro electronico, compatible con DN50 a DN150, con certificado de calibracion vigente.",
        "Herramientas para preparacion de uniones: corte recto, raspadores manuales y mecanicos del fabricante de los accesorios, panos limpios, alcohol isopropilico o limpiador especifico del fabricante.",
        "Eslingas de tela no metalica, balancines, gruas o pluma para la maniobra de tramos largos.",
        "Equipos de prueba hidrostatica: bomba con regulador de caudal, manometros calibrados con dos rangos (0-10 bar y 0-25 bar), registrador electronico de presion con resolucion minima 0,1 bar y muestreo no inferior a 1 lectura por minuto.",
        "Llaves dinamometricas y multiplicadores de torque para apriete de bridas, en el rango requerido para perneria M13 a M20 inoxidable, con certificado de calibracion vigente.",
        "Equipos topograficos y de medicion lineal para trazado y replanteo en obra.",
        "Pintura, anillos plasticos prefabricados y banderines para identificacion de lineas segun el codigo de colores del Capitulo Identificacion.",
        "Andamios certificados, escaleras, lineas de vida, arnes y demas elementos de proteccion colectiva e individual para trabajos en altura cuando aplique.",
    ]:
        add_bullet(doc, it)
    add_para(
        doc,
        "El Contratista sera responsable de toda falla derivada del "
        "suministro, uso, manejo o instalacion de los materiales y equipos "
        "a su cargo, asi como de la trazabilidad del lote contra el "
        "certificado de origen del fabricante.",
    )

    doc.add_heading("Equipos y Herramientas con Calibracion Vigente", level=2)
    add_para(
        doc,
        "La maquina de electrofusion, los manometros, los registradores de "
        "presion y las llaves dinamometricas exigiran certificado de "
        "calibracion trazable a patron nacional, con vigencia no superior "
        "a doce meses. El Contratista entregara copia de los certificados a "
        "la Inspeccion Tecnica antes de iniciar la actividad correspondiente; "
        "equipos sin calibracion vigente seran retirados de obra y la "
        "actividad se suspendera hasta su reemplazo.",
    )


# ---------------------------------------------------------------------------
# 3 Recepcion
# ---------------------------------------------------------------------------


def construir_recepcion(doc):
    doc.add_heading("RECEPCION, ALMACENAMIENTO Y MANIPULACION", level=1)

    doc.add_heading("Inspeccion de Recepcion de Materiales del Contratista", level=2)
    add_para(doc, "Cada lote de tuberia y accesorios HDPE adquiridos por el Contratista se inspeccionara en obra antes de su uso, en conjunto con la Inspeccion Tecnica:")
    for it in [
        "Concordancia entre el material recibido y el certificado de origen del fabricante: tipo (HDPE PE100), SDR, DN, lote, fecha de fabricacion, numero de orden de compra y conformidad con la Especificacion Tecnica de Canerias P22-ET-06-006-001-0.",
        "Marcado de fabrica visible sobre la tuberia conforme ISO 4427-1: fabricante, material, DN, SDR, presion nominal, fecha, numero de lote.",
        "Inspeccion visual del exterior y del interior de la tuberia: ausencia de rayaduras profundas, ovalizacion, abolladuras, contaminacion interior.",
        "Inspeccion visual de accesorios: ausencia de rebabas internas, ovalizacion, deformacion o dano en las zonas de electrofusion.",
        "Verificacion del estado de los codigos de barras de los accesorios electrofundibles (legibilidad para la maquina de electrofusion).",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Inspeccion de Recepcion de Aportes ADASA", level=2)
    add_para(
        doc,
        "Para valvulas, instrumentos y soportes entregados por ADASA: "
        "verificar contra el inventario firmado los TAGs, numeros de serie, "
        "certificados de pruebas de fabrica y la integridad del embalaje y "
        "de las caras de brida.",
    )
    add_para(
        doc,
        "El resultado de ambas inspecciones queda registrado en un "
        "protocolo de recepcion firmado. Si se detectan faltantes o danos, "
        "ADASA decide la accion correctiva: rechazo, recepcion condicionada "
        "con observaciones por levantar o aceptacion con concesion "
        "documentada.",
    )

    doc.add_heading("Almacenamiento Provisional", level=2)
    add_para(
        doc,
        "La tuberia HDPE y los accesorios plasticos son sensibles a la "
        "radiacion ultravioleta cuando se exponen durante periodos "
        "prolongados sin la proteccion del estabilizante negro de carbono "
        "o equivalente. Las condiciones especificas son:",
    )
    for it in [
        "Apilar la tuberia sobre cunas de madera o caucho, con apoyo continuo en toda su longitud y altura maxima de apilamiento conforme a la recomendacion del fabricante (referencial: 1,5 m de altura para DN100).",
        "Cubrir la tuberia con carpa opaca de polietileno o material equivalente cuando el almacenamiento supere los treinta dias.",
        "Mantener los extremos de la tuberia protegidos con tapas plasticas para evitar la entrada de polvo, animales y agua.",
        "Almacenar los accesorios de electrofusion en su embalaje original, protegidos de la radiacion solar, del polvo y de cualquier contacto que pueda danar las areas de fusion.",
    ]:
        add_bullet(doc, it)
    add_figura(doc, "fig-3-1.png",
               "Figura 3.1 — Almacenamiento tipico de tuberia HDPE: cunas, altura maxima por DN, carpa opaca anti-UV y tapas protectoras.",
               ancho_cm=16)

    doc.add_heading("Manipulacion", level=2)
    add_para(
        doc,
        "El movimiento de tuberia se realizara con eslingas de tela no "
        "metalica, evitando el uso de cables, cadenas o ganchos directos "
        "sobre el polietileno. Esta prohibido el arrastre de la tuberia "
        "sobre el suelo. La descarga desde el camion hasta el suelo se "
        "realizara controlada, sin caida libre. Para la maniobra de tramos "
        "largos prefabricados se utilizaran dos o mas puntos de apoyo "
        "distribuidos.",
    )


# ---------------------------------------------------------------------------
# 4 WPS/PQR/Calificacion
# ---------------------------------------------------------------------------


def construir_wps_pqr(doc):
    doc.add_heading("PROCEDIMIENTOS DE FUSION: WPS, PQR Y CALIFICACION DE OPERADORES", level=1)
    add_para(
        doc,
        "Antes de iniciar cualquier electrofusion en obra, el Contratista "
        "presentara a ADASA para revision y aprobacion los procedimientos "
        "de fusion escritos (WPS) de electrofusion, los registros de "
        "calificacion de procedimientos (PQR) y los certificados de "
        "calificacion de los operadores que ejecutaran las uniones.",
    )

    doc.add_heading("Procedimiento de Fusion Escrito (WPS) - Electrofusion", level=2)
    add_para(doc, "El Contratista emitira un WPS por cada rango de DN cubierto. El WPS declara, como minimo:")
    for it in [
        "Metodo de union: electrofusion.",
        "Material base (HDPE PE100, SDR17, PN10).",
        "Rango de DN cubierto.",
        "Marca y modelo de la maquina de electrofusion.",
        "Parametros del ciclo (lectura por codigo de barras; tension y tiempo de calentamiento administrados por la maquina; tiempo de enfriamiento sin movimiento declarado por el fabricante del accesorio).",
        "Condiciones ambientales admisibles (temperatura, humedad relativa, viento) y medidas de proteccion bajo condiciones desfavorables.",
        "Pasos secuenciales de preparacion (corte recto, raspado, marcado, limpieza, ensamble) y verificacion visual (pop-ups, profundidad de insercion, ausencia de quemaduras).",
        "Criterios visuales de aceptacion.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Calificacion del Procedimiento (PQR)", level=2)
    add_para(
        doc,
        "Cada WPS se califica mediante la ejecucion de probetas "
        "representativas que se ensayan segun ISO 13954 (peel decohesion "
        "para electrofusion, aplicable a DN >= 90 mm) e ISO 13955 (crushing "
        "decohesion para electrofusion, aplicable a DN < 90 mm). Los "
        "criterios de aceptacion minimos son: modo de falla ductil al 100 % "
        "de las probetas ensayadas, ausencia de despegue completo en peel "
        "decohesion (longitud de fractura fragil inferior al 25 % del area "
        "evaluada). La calificacion es responsabilidad del Contratista y se "
        "realiza en un laboratorio independiente acreditado, cuyo informe "
        "el Contratista entrega a ADASA.",
    )

    doc.add_heading("Calificacion de Operadores", level=2)
    add_para(
        doc,
        "Cada operador que ejecuta uniones en obra debe estar calificado "
        "conforme ISO 12176-3 (operator's badge para sistemas de fusion PE) "
        "e ISO 12176-4 (codificacion para trazabilidad), complementado con "
        "la practica del fabricante de la maquina (Frialen, Hurner, McElroy "
        "u otro). La vigencia maxima del certificado de calificacion es de "
        "doce meses, con registro de actividad mantenido por el empleador. "
        "La calificacion nombra al operador, identifica el rango de DN para "
        "el que esta calificado e identifica al organismo certificador.",
    )

    add_titulo_tabla(doc, "Tabla 4.1 — Esquema de calificacion de operadores y trazabilidad por Fusion ID.")
    add_simple_table(doc, [
        ("Elemento", "Requisito"),
        ("WPS de electrofusion aprobado por ADASA", "Antes de la primera electrofusion de cada rango de DN"),
        ("PQR de respaldo del WPS", "Emitido por laboratorio independiente acreditado; ensayos ISO 13954 / ISO 13955"),
        ("Certificado del operador", "Vigencia maxima 12 meses, conforme ISO 12176-3 + ISO 12176-4"),
        ("Fusion ID por union", "Numero correlativo unico; campos: fecha, hora, operador, maquina, ambiente, DN, accesorio, ciclo"),
        ("Trazabilidad de maquina", "Registro electronico de cada ciclo descargado por turno y archivado en el dossier as-built"),
    ])

    doc.add_heading("Sistema de Trazabilidad por Fusion ID", level=2)
    add_para(
        doc,
        "Cada union ejecutada en obra recibira un numero correlativo unico "
        "(Fusion ID) que el Contratista registra en el Fusion Log. El "
        "numero se marca fisicamente sobre la union con tinta indeleble "
        "compatible con HDPE, en una posicion visible y conservable. El "
        "Fusion Log forma parte del dossier as-built y es condicion de "
        "recepcion provisional del montaje.",
    )


# ---------------------------------------------------------------------------
# 5 Procedimientos constructivos
# ---------------------------------------------------------------------------


def construir_uniones(doc):
    doc.add_heading("PROCEDIMIENTOS CONSTRUCTIVOS POR TIPO DE UNION", level=1)
    add_titulo_tabla(doc, "Tabla 5.1 — Procedimientos de fusion por tipo de union aplicables al proyecto.")
    add_simple_table(doc, [
        ("Tipo de union", "Aplicacion en el proyecto", "Norma de referencia"),
        ("Electrofusion (accesorio + tubo)", "Codos, tees, manguitos, reducciones, saddles, empalmes tubo-tubo", "ISO 21307, ASTM F1055, ASTM F2620, ISO 15494"),
        ("Electrofusion del stub end al tubo", "Preparacion de la union bridada", "ISO 4427-3, ASTM F1055"),
        ("Brida + stub end + lap joint", "Conexion a equipos, valvulas e instrumentos in-line", "ASME B16.5, ISO 4427-3"),
    ])

    doc.add_heading("Electrofusion", level=2)
    add_para(doc, "Se aplica a accesorios moldeados con resistencia electrica integrada (codos, tees, manguitos, reducciones, saddles, stub ends). Pasos del ciclo:")
    add_numbered_list(doc, [
        "Corte recto perpendicular al eje, con herramienta dedicada que evite deformacion o calor excesivo.",
        "Marcado de la profundidad de insercion sobre el tubo, con plantilla del fabricante del accesorio.",
        "Raspado de la capa de oxido superficial del tubo en toda la zona de fusion, con raspador mecanico o manual del fabricante; eliminar todo el material desprendido.",
        "Limpieza con pano limpio y alcohol isopropilico o limpiador especifico del fabricante; permitir evaporacion completa antes del ensamble.",
        "Ensamble del tubo dentro del accesorio hasta la marca de profundidad; alinear con la herramienta de soporte que asegure coaxialidad y evite tensiones residuales.",
        "Lectura del codigo de barras del accesorio por la maquina de electrofusion.",
        "Ejecucion del ciclo automatico; no interrumpir el ciclo en ninguna circunstancia.",
        "Enfriamiento sin movimiento durante el tiempo minimo declarado en el WPS y en el accesorio.",
        "Verificacion visual de los indicadores de fusion (pop-ups o marcadores).",
        "Registro electronico del ciclo descargado de la maquina y asignacion del Fusion ID.",
    ])
    add_figura(doc, "fig-4-1.png",
               "Figura 5.1 — Secuencia operativa de electrofusion: corte, raspado, ensamble, ciclo automatico y enfriamiento.",
               ancho_cm=17)

    doc.add_heading("Bridas con Stub End y Lap Joint", level=2)
    add_para(doc, "Cubre las conexiones desmontables del sistema (conexion a equipos, valvulas e instrumentos in-line). Procedimiento operativo:")
    add_numbered_list(doc, [
        "Electrofusion del stub end al extremo del tubo HDPE conforme al procedimiento de electrofusion descrito en la Seccion anterior.",
        "Insercion del lap joint (brida loca) sobre el tubo antes de la electrofusion del stub end, con el sentido correcto.",
        "Una vez fundido el stub end y enfriado, presentacion de la union bridada con la contraparte (segundo stub end + lap joint para HDPE-HDPE, o brida metalica para valvula, instrumento o transicion a metal).",
        "Colocacion de la junta plana entre las caras de los stub ends; centrar y eliminar pliegues.",
        "Insercion de los esparragos inoxidables AISI 316 (ASTM A193 Gr.B8M Cl.2) con sus tuercas y golillas.",
        "Apriete cruzado en cuatro pasadas: pasada 1 al 30 % del torque, pasada 2 al 60 %, pasada 3 al 100 %, pasada 4 de verificacion al 100 % treinta minutos despues.",
    ])
    add_figura(doc, "fig-5-3.png",
               "Figura 5.2 — Detalle constructivo de union brida + stub end + lap joint con electrofusion del stub end al tubo.",
               ancho_cm=16)

    add_titulo_tabla(doc, "Tabla 5.2 — Torque base minimo de apriete para perneria inoxidable Gr.B8M Cl.2 en bridas ASME B16.5 Cl.150 cara plana sobre stub end de PE100.")
    add_simple_table(doc, [
        ("Diametro brida (NPS)", "Diametro perno", "Torque base minimo (N m)"),
        ("DN50 (2'')", "M16 (5/8'')", "70"),
        ("DN65 (2.5'')", "M16 (5/8'')", "80"),
        ("DN80 (3'')", "M16 (5/8'')", "90"),
        ("DN100 (4'')", "M16 (5/8'')", "105"),
        ("DN150 (6'')", "M20 (3/4'')", "190"),
    ])
    add_para(
        doc,
        "Los valores se calculan conforme PPI TN-38 para junta plana NBR/"
        "SBR de 1/8'' en stub end PE100 SDR17, con lubricante anti-seize "
        "aplicado en rosca y bajo la golilla, K-factor 0,18. El Contratista "
        "presentara a ADASA, antes de la primera union bridada, el torque "
        "definitivo calculado conforme PPI TN-38 con su lubricante y junta "
        "especificos; el valor calculado puede ser superior al de la tabla, "
        "nunca inferior, y debe respetar el limite de carga axial admisible "
        "del stub end declarado por el fabricante del accesorio.",
    )

    doc.add_heading("Tolerancias Visuales de Aceptacion", level=2)
    add_titulo_tabla(doc, "Tabla 5.3 — Tolerancias visuales de inspeccion de union electrofundida.")
    add_simple_table(doc, [
        ("Defecto", "Criterio de aceptacion"),
        ("Excentricidad de ensamble", "<= 2 mm respecto a la linea de marca de profundidad"),
        ("Material extruido o perdida de fundido por extremo del accesorio", "No admisible"),
        ("Pop-ups o indicadores", "Ambos pop-ups del accesorio deben emerger"),
        ("Profundidad de insercion visible", "Coincide con la marca realizada sobre el tubo"),
        ("Quemadura, decoloracion intensa", "No admisible"),
        ("Burbujas o porosidad visible en la zona de fundido", "No admisible"),
    ])


# ---------------------------------------------------------------------------
# 6 Soporteria
# ---------------------------------------------------------------------------


def construir_soporteria(doc):
    doc.add_heading("SOPORTERIA, ANCLAJES Y DILATACION TERMICA", level=1)
    add_para(
        doc,
        "El sistema HDPE aereo del proyecto presenta expansion y "
        "contraccion termica significativas por el coeficiente de "
        "dilatacion lineal del polietileno (alpha ~ 2,0 x 10^-4 /C, en "
        "torno a un orden de magnitud por sobre el del acero). El diseno "
        "de soportes es definido por la ingenieria de detalle (cuadernillo "
        "de isometrias); esta especificacion establece los criterios "
        "minimos de instalacion y de verificacion en obra.",
    )

    doc.add_heading("Espaciamiento Maximo entre Soportes", level=2)
    add_titulo_tabla(doc, "Tabla 6.1 — Espaciamiento maximo referencial entre soportes para tuberia HDPE PE100 SDR17 aerea, en metros, para servicio a 22 C con liquido.")
    add_simple_table(doc, [
        ("DN (mm)", "Espaciamiento maximo (m)"),
        ("50", "0,90"),
        ("80", "1,10"),
        ("100", "1,30"),
        ("150", "1,60"),
    ])
    add_para(doc, "A 35 C se reduce el espaciamiento un 20 %; en servicios verticales se admite incrementar un 30 %. Si la ingenieria de detalle establece valores distintos, prevalecen los del plano.")

    doc.add_heading("Tipologia de Soportes", level=2)
    for t in [
        ("Clip o abrazadera no restrictiva — ", "soporte deslizante que mantiene la caneria en su posicion pero permite el desplazamiento longitudinal por dilatacion termica. Es el soporte estandar entre puntos fijos."),
        ("Anclaje fijo — ", "soporte que restringe el movimiento longitudinal en una posicion concreta; se ubica en puntos seleccionados para forzar la dilatacion hacia tramos con flexibilidad."),
        ("Guia deslizante — ", "soporte que limita el movimiento lateral pero permite el longitudinal; se utiliza entre el anclaje fijo y el loop de dilatacion."),
    ]:
        add_para_bold_lead(doc, t[0], t[1])
    add_figura(doc, "fig-6-1.png",
               "Figura 6.1 — Tipologia de soportes para caneria HDPE aerea: clip deslizante, anclaje fijo y guia deslizante.",
               ancho_cm=17)

    doc.add_heading("Calculo de Dilatacion Termica", level=2)
    add_para(
        doc,
        "La dilatacion lineal estimada es Delta-L = L x alpha x Delta-T, "
        "donde L es la longitud del tramo entre puntos fijos, alpha es el "
        "coeficiente de dilatacion lineal del HDPE (alpha ~ 2,0 x 10^-4 /C) "
        "y Delta-T es la diferencia entre la temperatura maxima de "
        "operacion y la temperatura minima de montaje.",
    )
    add_titulo_tabla(doc, "Tabla 6.2 — Coeficiente de dilatacion lineal del HDPE y ejemplo de calculo para tramos tipicos del proyecto.")
    add_simple_table(doc, [
        ("Material", "alpha (/C)", "Tramo L=10 m con Delta-T=20 C"),
        ("HDPE PE100", "2,0 x 10^-4", "Delta-L = 40 mm"),
        ("Acero al carbono (referencia comparativa)", "1,2 x 10^-5", "Delta-L = 2,4 mm"),
    ])
    add_para(doc, "Los puntos fijos y los loops de dilatacion son obligatorios en el sistema HDPE aereo del proyecto.")
    add_figura(doc, "fig-6-2.png",
               "Figura 6.2 — Loop de dilatacion y brazo flexible; dimension minima del brazo en funcion del DN y de la dilatacion esperada.",
               ancho_cm=16)


# ---------------------------------------------------------------------------
# 7 Tendido
# ---------------------------------------------------------------------------


def construir_tendido(doc):
    doc.add_heading("TENDIDO Y MONTAJE EN OBRA", level=1)

    doc.add_heading("Trazado y Replanteo", level=2)
    add_para(
        doc,
        "El Contratista replantea cada tramo de caneria sobre la "
        "estructura de soporte conforme a los planos de implantacion y a "
        "las isometrias del cuadernillo. El replanteo establece la "
        "posicion exacta de los soportes, los anclajes fijos, los loops "
        "de dilatacion, los puntos de drenaje y los puntos de venteo, "
        "antes de iniciar la fabricacion de carretes.",
    )

    doc.add_heading("Prefabricacion de Carretes", level=2)
    add_para(
        doc,
        "Se prefabrican a pie de obra los tramos rectos largos por "
        "electrofusion, para luego ser elevados como unidad sobre la "
        "soporteria. La prefabricacion reduce la cantidad de "
        "electrofusiones realizadas en altura. La longitud maxima del "
        "carrete prefabricado se determina por la capacidad de la "
        "maniobra de izaje disponible.",
    )

    doc.add_heading("Conexion a Equipos", level=2)
    add_para(
        doc,
        "Las uniones a equipos rotativos y estanques se ejecutan con "
        "bridas, sin transmitir cargas mecanicas residuales a las "
        "boquillas del equipo. El Contratista verifica la coaxialidad y "
        "el paralelismo de las caras antes de apretar los pernos finales. "
        "Esta verificacion es coherente con el procedimiento de la ET de "
        "Montaje Electromecanico P22-ET-06-007-001-0.",
    )

    doc.add_heading("Cota de Pendiente", level=2)
    add_para(
        doc,
        "Los tramos que conducen fluidos con solidos o que requieren "
        "drenaje deben respetar la pendiente minima declarada en los "
        "planos. La verificacion se realiza con nivel optico durante el "
        "montaje, antes del apriete definitivo de los soportes.",
    )


# ---------------------------------------------------------------------------
# Instalacion de Canerias Enterradas (tramo de drenaje)
# ---------------------------------------------------------------------------


def construir_canerias_enterradas(doc):
    doc.add_heading(
        "INSTALACION DE CANERIAS ENTERRADAS (TRAMO DE DRENAJE)", level=1)
    add_para(
        doc,
        "El sistema de proceso e interconexiones es aereo; el tramo de la red "
        "de drenaje (linea AMF-HDPE-DN160 y conexas) se ejecuta enterrado. "
        "Los requisitos de zanja, cama y relleno siguen la seccion de "
        "Instalacion de Canerias Enterradas de la ET de referencia "
        "P04-ET-00-006-102, adaptados a tuberia HDPE. La excavacion de la "
        "zanja y la compactacion del relleno son obra civil del mismo "
        "contrato; este capitulo fija los requisitos que debe cumplir la "
        "zanja para recibir el tubo HDPE y la coordinacion con el montaje.",
    )

    doc.add_heading("Zanja", level=2)
    add_para(doc, "La zanja que aloja la caneria cumplira lo siguiente:")
    for it in [
        "Dimensiones segun los planos; el fondo debe quedar libre de piedras "
        "angulosas, trozos de madera o metal, escombros y materia organica o "
        "vegetal.",
        "Antes de excavar se preveera la presencia de instalaciones "
        "enterradas existentes (otras canerias, alcantarillados, conduit); "
        "cuando se crucen, la caneria se alojara a una distancia libre minima "
        "de 0,5 m y, en sus cercanias, la excavacion sera manual para evitar "
        "danos materiales y personales.",
        "El fondo debe estar seco; si la zanja esta inundada se drenara el "
        "agua antes de disponer la cama.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Cama de Apoyo", level=2)
    add_para(
        doc,
        "Sobre el fondo se colocara una capa de material fino (arena o "
        "material cribado de tamano maximo 1/2\") de espesor no inferior a "
        "10 cm. Antes de bajar el tubo se verificara que la cama este libre "
        "de tosca, malezas, piedras o cualquier elemento extrano.",
    )

    doc.add_heading("Bajada y Puesta en Piso", level=2)
    add_para(
        doc,
        "El tubo se bajara con un metodo que garantice que se acomode a la "
        "rasante de la cama, en su posicion correcta, evitando "
        "dislocamientos, deslizamientos, esfuerzos de flexion o torsion, "
        "deformaciones y oscilacion excesiva del tramo, atendiendo a la "
        "flexibilidad propia del HDPE.",
    )

    doc.add_heading("Relleno y Compactacion", level=2)
    for it in [
        "Relleno inicial con material cribado de tamano maximo 1/2\" hasta "
        "completar al menos 20 cm sobre la clave de la caneria, colocado en "
        "capas de 20 cm compactadas manualmente con precaucion para no danar "
        "el tubo.",
        "Relleno superior con material del propio terreno (tamano maximo 6\") "
        "en capas de espesor compactable, alcanzando el 90 % del Proctor "
        "modificado; el control de compactacion se hara capa a capa segun "
        "procedimiento aprobado por ADASA.",
        "Relleno final tipo lomo de toro de al menos 10 cm de altura, tambien "
        "al 90 % del Proctor modificado. No se usara agua para la "
        "compactacion, salvo la requerida para alcanzar la humedad optima.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Cinta de Senalizacion y Prueba", level=2)
    for it in [
        "Sobre el relleno se instalara una cinta detectora de senalizacion "
        "(banda de advertencia) que indique la presencia del servicio "
        "enterrado, segun el detalle de los planos.",
        "El tapado se hara inmediatamente despues de la bajada, dejando las "
        "uniones (electrofusion y bridas) a la vista hasta completar la "
        "prueba hidrostatica conforme ASTM F2164.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Proteccion Anticorrosiva: No Aplica", level=2)
    add_para(
        doc,
        "Las disposiciones de proteccion para corrosion de canerias "
        "enterradas de la ET de referencia (proteccion catodica, "
        "revestimiento anticorrosivo epoxico segun AWWA C210 y cintas "
        "anticorrosivas segun AWWA C209) aplican a canerias de acero. El "
        "tramo de drenaje del proyecto es HDPE, material inerte a la "
        "corrosion, por lo que no requiere proteccion anticorrosiva; la unica "
        "banda enterrada es la cinta detectora de senalizacion antes "
        "indicada.",
    )


# ---------------------------------------------------------------------------
# 8 Instalacion Valvulas e Instrumentos
# ---------------------------------------------------------------------------


def construir_valvulas_instrumentos(doc):
    doc.add_heading("INSTALACION DE VALVULAS E INSTRUMENTOS IN-LINE", level=1)
    add_para(
        doc,
        "ADASA entrega al Contratista las valvulas mariposa, valvulas "
        "check e instrumentos in-line listados en la Tabla 2.1 para su "
        "instalacion en linea conforme a los TAGs de las isometrias y a "
        "las partidas A9.3 (Valvulas) y A9.4 (Instrumentos in-line) del "
        "BL_MONTAJE_TALTAL. El suministro de juntas planas y perneria del "
        "lado HDPE es del Contratista.",
    )

    doc.add_heading("Recepcion en Bodega del Contratista", level=2)
    add_para(
        doc,
        "A la entrega de cada valvula o instrumento por ADASA al "
        "Contratista, se verifica contra el packing list y el LI: TAG, "
        "modelo, numero de serie, certificados de origen y de pruebas de "
        "fabrica, integridad del embalaje, conservacion de la lubricacion "
        "interna del actuador (en valvulas con actuador), integridad de "
        "las caras de brida y los tapones de proteccion.",
    )

    doc.add_heading("Almacenamiento Provisional", level=2)
    add_para(
        doc,
        "Las valvulas se mantienen en su embalaje original, en posicion "
        "declarada por el fabricante (tipicamente vertical para valvulas "
        "mariposa, con el disco en posicion intermedia para evitar "
        "deformacion del asiento), protegidas de la radiacion solar "
        "directa y del polvo. Los instrumentos in-line se mantienen en su "
        "caja original; los manometros con liquido amortiguador y los "
        "transmisores de presion se almacenan en orientacion vertical.",
    )

    doc.add_heading("Instalacion en Linea", level=2)
    for it in [
        "Verificar el TAG de la valvula o instrumento contra la isometrica antes de instalarlo.",
        "Orientar el dispositivo conforme la flecha de flujo del cuerpo o conforme a la indicacion del fabricante.",
        "Para valvulas mariposa: asegurar que la separacion entre el centro de la valvula y el codo o tee aguas arriba no sea inferior a 5 x D (referencial; respetar el criterio del fabricante cuando sea mas estricto).",
        "Para valvulas con actuador o volante: garantizar la accesibilidad del actuador o volante para operacion y mantenimiento; verificar que el cuadrante del actuador respete los topes mecanicos.",
        "Para instrumentos in-line (caudalimetros electromagneticos, transmisores de presion, switches de nivel): respetar la longitud minima de tramo recto aguas arriba y aguas abajo declarada por el fabricante (tipicamente 10 x D aguas arriba y 5 x D aguas abajo para caudalimetros electromagneticos).",
        "Apoyo de soporte independiente cuando el peso del dispositivo justifique no transmitir cargas a las bridas del tubo, especialmente en valvulas mariposa DN150 y mayores.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Conexion Bridada del Lado HDPE", level=2)
    add_para(
        doc,
        "La conexion valvula-tubo se ejecuta con stub end + lap joint del "
        "lado HDPE (electrofundido al tubo conforme a la Seccion "
        "Procedimientos Constructivos) contra la brida metalica de la "
        "valvula o instrumento. Se utilizan juntas planas NBR/SBR de "
        "1/8'' ASME B16.21 nuevas y perneria inoxidable Gr.B8M Cl.2 "
        "conforme la Tabla 5.2. El apriete sigue el procedimiento cruzado "
        "en cuatro pasadas descrito en la Seccion Bridas con Stub End y "
        "Lap Joint.",
    )

    add_titulo_tabla(doc, "Tabla 8.1 — Criterios de instalacion y verificacion de valvulas e instrumentos in-line.")
    add_simple_table(doc, [
        ("Aspecto", "Criterio"),
        ("Identificacion del TAG", "Coincide con isometrica y LI; etiqueta visible y permanente"),
        ("Orientacion de la flecha de flujo", "Conforme al cuerpo del dispositivo"),
        ("Tramo recto aguas arriba (instrumentos)", ">= 10 x D para caudalimetros (referencial)"),
        ("Tramo recto aguas abajo (instrumentos)", ">= 5 x D para caudalimetros (referencial)"),
        ("Separacion valvula mariposa al codo / tee aguas arriba", ">= 5 x D (referencial)"),
        ("Juntas", "NBR/SBR 1/8'' nuevas por cada lado"),
        ("Torque cruzado", "4 pasadas conforme procedimiento de la Seccion Bridas"),
        ("Soporte independiente", "Cuando el peso del dispositivo lo justifique"),
    ])
    add_para(doc, "El protocolo de instalacion y verificacion se entrega por TAG y se integra al dossier as-built.")


# ---------------------------------------------------------------------------
# 9 Identificacion
# ---------------------------------------------------------------------------


def construir_identificacion(doc):
    doc.add_heading("IDENTIFICACION Y MARCADO EN OBRA", level=1)
    add_para_bold_lead(
        doc,
        "La tuberia HDPE no se pinta. ",
        "El polietileno PE100 mantiene su color negro de fabrica como protector "
        "UV (negro de carbono incorporado al material); cualquier pintura sobre "
        "HDPE pierde adherencia en intemperie y compromete la barrera UV del "
        "material. La identificacion visual del servicio se ejecuta "
        "exclusivamente con anillos prefabricados, etiquetas autoadhesivas y "
        "flechas direccionales en los colores RAL declarados en la Tabla 9.1, "
        "aplicados en los puntos clave de la red.",
    )
    add_para(
        doc,
        "Los servicios montados por el Contratista de canerias HDPE en el "
        "Area 06 conforme al Listado de Lineas P22-LI-06-006-101-0 son los "
        "siguientes. Las lineas LQ (Limpieza Quimica) y DI (Dispersante) son "
        "parte del modulo aportado por BW Water y quedan fuera del alcance de "
        "esta especificacion; el codigo de colores adoptado es subconjunto del "
        "corporativo ADASA, restringido a los servicios efectivamente montados.",
    )

    add_titulo_tabla(doc, "Tabla 9.1 — Codigo de colores por servicio del Area 06 (aplicado al anillo y a la flecha, no al tubo).")
    add_simple_table(doc, [
        ("Servicio", "Codigo", "Color RAL del anillo / flecha", "Leyenda"),
        ("Salmuera de osmosis inversa", "SA", "Verde RAL 6018", "SALMUERA OI"),
        ("Permeado OI", "PE", "Celeste RAL 6027", "PERMEADO OI"),
        ("Drenajes", "DR", "Gris RAL 7011", "DRENAJE"),
    ])

    add_para(doc, "La identificacion se aplica con:")
    for it in [
        "Anillos de identificacion prefabricados (collares de PVC u otro polimero compatible con HDPE) o etiquetas autoadhesivas de polietileno con adhesivo de larga duracion, en el color RAL del servicio, ubicados en intervalos no superiores a 10 m en tramos rectos y en cada cambio de direccion (codos y tees), asi como junto a cada conexion a equipo, valvula o instrumento.",
        "Flechas direccionales del color del servicio (anillos o etiquetas con flecha incorporada), con la punta orientada al sentido del flujo, contiguas a cada anillo de identificacion.",
        "Leyenda con el nombre del fluido: texto blanco sobre el anillo de color cuando el anillo lleva fondo de color completo, o texto del color del servicio sobre fondo blanco cuando se usa etiqueta autoadhesiva blanca con la flecha incorporada. Altura minima de tipografia en funcion del diametro exterior conforme la tabla del PDA P04-ET-00-006-102 seccion 10: 15 mm para OD hasta 32 mm; 20 mm para OD 33 a 50 mm; 30 mm para OD 51 a 150 mm; 60 mm para OD 151 a 250 mm.",
    ]:
        add_bullet(doc, it)
    add_figura(doc, "fig-8-1.png",
               "Figura 9.1 — Disposicion de anillos de identificacion, etiquetas autoadhesivas y flechas direccionales sobre tuberia HDPE; la tuberia conserva su color negro de fabrica.",
               ancho_cm=17)


# ---------------------------------------------------------------------------
# 10 Hidrostatica
# ---------------------------------------------------------------------------


def construir_hidrostatica(doc):
    doc.add_heading("PRUEBAS HIDROSTATICAS CONFORME ASTM F2164", level=1)
    add_para(
        doc,
        "Una vez completado el montaje, la soporteria instalada y "
        "aceptada y la red purgada de aire, cada tramo aislable se somete "
        "a la prueba hidrostatica conforme ASTM F2164 para HDPE.",
    )

    doc.add_heading("Pre-test", level=2)
    for it in [
        "Aislar el tramo a probar con bridas ciegas o con valvulas cerradas y bloqueadas, etiquetadas como 'TRAMO EN PRUEBA — NO OPERAR'.",
        "Aislar todo equipo sensible (bombas, instrumentos, valvulas de control) con bridas ciegas.",
        "Inspeccionar visualmente todas las uniones, especialmente las electrofusiones recientes.",
        "Llenar el tramo con agua limpia desde el punto mas bajo, expulsando todo el aire por los puntos altos.",
        "Instalar dos manometros redundantes en el tramo (uno en punto alto, otro en punto bajo), calibrados.",
        "Conectar el registrador electronico de presion.",
    ]:
        add_bullet(doc, it)

    doc.add_heading("Procedimiento conforme ASTM F2164", level=2)
    add_titulo_tabla(doc, "Tabla 10.1 — Parametros de prueba hidrostatica para HDPE PN10 conforme ASTM F2164 vigente.")
    add_simple_table(doc, [
        ("Fase", "Duracion", "Presion", "Make-up de agua"),
        ("Initial Expansion", "30 min a 3 h", "PDP = 1,5 x PDO = 15 bar", "Permitido, registrado en planilla"),
        ("Test Phase", "1 a 3 h", "PDP = 15 bar", "No permitido"),
        ("Recovery", "1 h", "0,1 x PDO = 1 bar", "No permitido (la presion se descarga a 0,1 x PDO al inicio)"),
    ])
    add_para(
        doc,
        "Donde PDO es la presion de diseno de operacion (10 bar para PN10) "
        "y PDP es la presion de prueba (1,5 x PDO = 15 bar).",
    )
    add_para(doc, "Criterios de aceptacion conforme ASTM F2164:")
    for it in [
        "Fase Initial Expansion: completar con make-up de agua hasta estabilizar; el volumen acumulado debe ajustarse a los valores del Apendice X1 de la ASTM F2164.",
        "Fase Test Phase: la presion interna se monitorea sin make-up; la caida admisible no excedera la prevista por la curva de relajacion viscoelastica.",
        "Fase Recovery: descargar deliberadamente la presion hasta 0,1 x PDO; el criterio de aceptacion es una recuperacion elastica equivalente a no menos del 50 % de la caida registrada durante la Test Phase.",
    ]:
        add_bullet(doc, it)
    add_figura(doc, "fig-9-1.png",
               "Figura 10.1 — Curva ASTM F2164 presion vs tiempo: Initial Expansion + Test Phase + Recovery.",
               ancho_cm=16)

    doc.add_heading("Registro y Aceptacion", level=2)
    add_para(doc, "El Contratista entrega a la Inspeccion Tecnica el protocolo de hidrostatica por tramo, con:")
    for it in [
        "Identificacion del tramo (TAG inicial y final).",
        "Curva de presion vs tiempo descargada del registrador electronico.",
        "Volumen de make-up consumido por fase.",
        "Lecturas de los dos manometros redundantes a intervalos no superiores a 15 min.",
        "Lista de uniones del tramo con sus Fusion ID.",
        "Firma del supervisor del Contratista y del representante de la Inspeccion Tecnica.",
    ]:
        add_bullet(doc, it)
    add_para(
        doc,
        "Cualquier falla en la prueba obliga al Contratista a localizar y "
        "reparar la fuga, a re-fusionar la union defectuosa (con nuevo "
        "Fusion ID) y a repetir el procedimiento completo.",
    )


# ---------------------------------------------------------------------------
# 11 Flushing
# ---------------------------------------------------------------------------


def construir_flushing(doc):
    doc.add_heading("LIMPIEZA, FLUSHING Y PUESTA EN SERVICIO INICIAL", level=1)
    add_para(
        doc,
        "Tras la aceptacion de la prueba hidrostatica, cada linea se "
        "somete a flushing con agua limpia para eliminar virutas, polvo, "
        "restos de fundido y cualquier contaminante introducido durante "
        "el montaje.",
    )
    for it in [
        "Velocidad minima de flushing: 2,5 m/s (coherente con el criterio P04-ET-00-006-102 seccion 9).",
        "Duracion minima: 5 segundos por metro lineal de caneria del tramo, garantizando ademas al menos 3 cambios completos del volumen interno de la linea.",
        "Punto de descarga: hacia drenaje aprobado, evitando equipos sensibles aguas abajo.",
        "Criterio de aceptacion: agua a la salida visualmente limpia, sin solidos en suspension, con turbidez igual o inferior a la del agua de alimentacion.",
    ]:
        add_bullet(doc, it)


# ---------------------------------------------------------------------------
# 12 Protocolos
# ---------------------------------------------------------------------------


def construir_protocolos(doc):
    doc.add_heading("PROTOCOLOS Y DOCUMENTACION ENTREGABLE", level=1)

    doc.add_heading("Matriz de Protocolos", level=2)
    add_titulo_tabla(doc, "Tabla 12.1 — Matriz de protocolos del montaje de canerias HDPE.")
    add_simple_table(doc, [
        ("Protocolo", "Cuando se ejecuta"),
        ("Recepcion de tuberia y accesorios (Contratista)", "A la llegada de cada lote en obra"),
        ("Recepcion de aportes ADASA (valvulas, instrumentos, soportes)", "A la entrega de cada lote por ADASA"),
        ("Ensayos de pre-fusion por turno", "Diaria, antes de iniciar uniones, sobre probetas"),
        ("Calificacion PQR de procedimiento", "Una vez por WPS, previo al inicio de electrofusiones de produccion"),
        ("Registro individual por electrofusion (Fusion ID)", "En cada union electrofundida"),
        ("Inspeccion visual de uniones", "Posterior al enfriamiento de cada union"),
        ("Apriete de bridas con torque", "En cada union bridada"),
        ("Instalacion de valvulas e instrumentos por TAG", "En cada dispositivo aportado por ADASA"),
        ("Soporteria instalada", "Por tramo, antes de la prueba hidrostatica"),
        ("Prueba hidrostatica por tramo (ASTM F2164)", "Por cada tramo aislable"),
        ("Flushing", "Tras la aceptacion de la hidrostatica"),
        ("Recepcion provisional del montaje", "Al termino de todas las actividades, con punch list"),
    ])

    doc.add_heading("Plan de Inspeccion y Pruebas", level=2)
    add_para(
        doc,
        "El Contratista emite un ITP integral que reune las actividades "
        "anteriores, identificando responsable, criterio de aceptacion, "
        "punto de retencion (CC, Hold Point) o punto de presenciado (TP, "
        "Witness Point) por ADASA. Como punto de retencion mandatorio se "
        "fija al menos:",
    )
    for it in [
        "Aprobacion del WPS y del PQR antes de la primera electrofusion de produccion.",
        "Aceptacion de la soporteria instalada antes de presurizar.",
        "Aceptacion de la prueba hidrostatica antes del flushing.",
        "Aceptacion del flushing antes de la entrega al equipo de operacion.",
    ]:
        add_bullet(doc, it)
    add_figura(doc, "fig-11-1.png",
               "Figura 12.1 — Diagrama de flujo del Plan de Inspeccion y Pruebas del montaje de canerias.",
               ancho_cm=14)

    doc.add_heading("Dossier As-Built y Fusion Log", level=2)
    add_para(doc, "A la terminacion del montaje, el Contratista entrega a ADASA un dossier as-built en formato digital con la siguiente estructura:")
    for it in [
        "Seccion 1 — Informacion general, contratista, fechas, alcance.",
        "Seccion 2 — WPS y PQR aprobados; certificados de calificacion de operadores con vigencia al cierre.",
        "Seccion 3 — Fusion Log completo con todas las uniones del proyecto.",
        "Seccion 4 — Protocolos individuales firmados.",
        "Seccion 5 — Registros de calibracion de los equipos utilizados.",
        "Seccion 6 — Curvas de hidrostatica por tramo.",
        "Seccion 7 — Isometricas red-line y plano de implantacion as-built.",
        "Seccion 8 — Protocolos de instalacion por TAG de valvulas e instrumentos.",
        "Seccion 9 — Punch list final con cierre.",
    ]:
        add_bullet(doc, it)


# ---------------------------------------------------------------------------
# 13 HSE
# ---------------------------------------------------------------------------


def construir_hse(doc):
    doc.add_heading("SEGURIDAD Y MEDIO AMBIENTE", level=1)

    doc.add_heading("Disposiciones Generales", level=2)
    add_para(
        doc,
        "El Contratista cumple la legislacion nacional aplicable y los "
        "procedimientos de seguridad de ADASA durante toda su permanencia "
        "en obra. Antes del inicio de actividades presenta, para revision "
        "de la Inspeccion Tecnica: matriz IPER, procedimientos escritos de "
        "trabajo seguro por actividad relevante, reglamento interno, "
        "charlas diarias de cinco minutos, registros de capacitacion. "
        "Mantiene un prevencionista de riesgos calificado en obra durante "
        "toda la duracion de los trabajos.",
    )

    doc.add_heading("Manipulacion de Tramos Largos", level=2)
    add_para(
        doc,
        "Los carretes prefabricados de HDPE se levantan con eslingas de "
        "tela no metalica, con dos o mas puntos de apoyo y bajo "
        "procedimiento escrito de izaje aprobado. La zona de exclusion bajo "
        "la carga suspendida se mantiene libre de personas.",
    )

    doc.add_heading("Trabajos en Altura", level=2)
    add_para(
        doc,
        "Toda actividad por sobre 1,80 m de altura desde un punto de "
        "apoyo estable requiere uso obligatorio de arnes con doble cabo y "
        "linea de vida, andamios certificados, plataformas con barandas y "
        "procedimiento escrito aprobado.",
    )

    doc.add_heading("Equipos de Electrofusion", level=2)
    add_para(
        doc,
        "La maquina de electrofusion opera con tensiones de hasta 40 V CC "
        "en el accesorio durante el ciclo. El Contratista verifica la "
        "conexion a tierra del banco y la integridad del cable de "
        "alimentacion antes de cada uso.",
    )

    doc.add_heading("Gestion de Residuos", level=2)
    add_para(
        doc,
        "Los recortes de HDPE, los accesorios fallidos durante la "
        "calificacion, los panos usados con limpiador y los embalajes se "
        "segregan por tipo y se retiran de obra por el Contratista. Los "
        "residuos peligrosos se gestionan como Residuos Industriales "
        "Peligrosos conforme a la legislacion vigente, con declaracion de "
        "transporte y disposicion final emitida por receptor autorizado.",
    )


# ---------------------------------------------------------------------------
# 14 Hitos
# ---------------------------------------------------------------------------


def construir_hitos(doc):
    doc.add_heading("HITOS Y PUNCH LIST FINAL", level=1)

    doc.add_heading("Hitos de Avance", level=2)
    add_para(doc, "El programa detallado de obra emitido por el Contratista identifica al menos los siguientes hitos verificables:")
    for h in [
        "H1 — Movilizacion a obra.",
        "H2 — Aprobacion del WPS de electrofusion y PQR por ADASA.",
        "H3 — Calificacion de operadores aceptada por ADASA.",
        "H4 — Recepcion y aceptacion de los lotes de tuberia y accesorios HDPE adquiridos por el Contratista.",
        "H5 — Recepcion y aceptacion de aportes ADASA (valvulas, instrumentos, soportes).",
        "H6 — Soporteria instalada del tramo principal y aceptada.",
        "H7 — Prefabricacion e instalacion del tramo principal HDPE DN100 con sus electrofusiones registradas.",
        "H8 — Prefabricacion e instalacion de los tramos secundarios HDPE DN80, DN50, DN150.",
        "H9 — Instalacion de valvulas e instrumentos in-line por TAG completada y aceptada.",
        "H10 — Pruebas hidrostaticas ASTM F2164 aceptadas por tramo.",
        "H11 — Flushing completado y aceptado.",
        "H12 — Identificacion de lineas completada.",
        "H13 — Recepcion provisional del montaje con punch list.",
        "H14 — Cierre del punch list y recepcion final con dossier as-built completo.",
    ]:
        add_bullet(doc, h)

    doc.add_heading("Criterios de Cierre", level=2)
    add_para(
        doc,
        "Para cada hito el Contratista entrega a la Inspeccion Tecnica el "
        "protocolo correspondiente firmado, los registros de calibracion "
        "aplicables, los registros fotograficos relevantes y los "
        "certificados de los materiales empleados cuando aplique. ADASA "
        "verifica el cumplimiento del criterio de aceptacion y emite su "
        "conformidad por escrito o, en caso contrario, las observaciones "
        "a levantar.",
    )

    doc.add_heading("Punch List", level=2)
    add_para(
        doc,
        "A la terminacion de las actividades el Contratista entrega a la "
        "Inspeccion Tecnica el acta de recepcion provisional con el punch "
        "list. La recepcion final se concede cuando todos los puntos del "
        "punch list estan cerrados a satisfaccion de la Inspeccion Tecnica "
        "y se ha entregado el dossier as-built completo, incluido el "
        "Fusion Log de cada electrofusion del proyecto.",
    )


# ---------------------------------------------------------------------------
# Anexos
# ---------------------------------------------------------------------------


def construir_anexos(doc):
    doc.add_heading("ANEXOS", level=1)
    add_para(doc, "Los entregables siguientes acompanan a esta Especificacion como anexos de referencia.")

    doc.add_heading("Anexo A — Listado de Materiales (P22-LI-06-006-102-0)", level=2)
    add_para(
        doc,
        "Consolidado del sistema HDPE por DN y por tipo de accesorio. "
        "Entregado como archivo Excel separado en la carpeta de la "
        "presente especificacion.",
    )

    doc.add_heading("Anexo B — Cuadernillo de Isometrias", level=2)
    add_para(
        doc,
        "P22-DWG-06-006-001 a -011, entregado en archivo separado dentro "
        "del paquete de licitacion. No se embebe en esta especificacion "
        "para mantener la legibilidad.",
    )

    doc.add_heading("Anexo C — Formatos de Protocolos en blanco", level=2)
    add_para(
        doc,
        "Recepcion, registro de fusion (Fusion ID), calificacion PQR, "
        "soporteria, instalacion de valvulas e instrumentos por TAG, "
        "hidrostatica ASTM F2164, flushing, recepcion provisional. Se "
        "entregan en archivo separado en formato editable junto con el "
        "dossier as-built.",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def crear_documento():
    crear_documento_adasa(
        titulo="ESPECIFICACION TECNICA DE MONTAJE DE CANERIAS HDPE",
        codigo="P22-ET-06-007-002-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # Limpiar placeholder del template
    elementos = []
    encontrado = False
    for para in doc.paragraphs:
        if para.style and para.style.name == "Heading 1" and not encontrado:
            encontrado = True
        if encontrado:
            elementos.append(para)
    for para in elementos:
        p = para._element
        p.getparent().remove(p)

    construir_generalidades(doc)
    construir_suministros(doc)
    construir_recepcion(doc)
    construir_wps_pqr(doc)
    construir_uniones(doc)
    construir_soporteria(doc)
    construir_tendido(doc)
    construir_canerias_enterradas(doc)
    construir_valvulas_instrumentos(doc)
    construir_identificacion(doc)
    construir_hidrostatica(doc)
    construir_flushing(doc)
    construir_protocolos(doc)
    construir_hse(doc)
    construir_hitos(doc)
    construir_anexos(doc)

    if METADATA_DISPONIBLE:
        apply_core_properties(
            doc,
            title="Especificacion Tecnica de Montaje de Canerias HDPE - Taltal",
            author="Luis Rivera",
            subject="P22-ET-06-007-002-0",
            keywords="ADASA Taltal Montaje Canerias HDPE PE100 Electrofusion",
            category="Especificacion Tecnica",
            comments="",
        )

    doc.save(OUTPUT)

    if METADATA_DISPONIBLE:
        fix_app_xml(OUTPUT, application="Microsoft Office Word")

    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
