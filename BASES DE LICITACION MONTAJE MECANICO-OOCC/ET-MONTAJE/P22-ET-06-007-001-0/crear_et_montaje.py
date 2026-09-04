#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la Especificacion Tecnica de Montaje Electromecanico
P22-ET-06-007-001-0 usando template-adasa v7.4.

Equipos en alcance:
    - TK-06-001 (Estanque de Salmuera PRFV, 10 m3)
    - BH-06-001 (Bomba de Alimentacion KSB + motor WEH 11 kW)

Salida:
    P22-ET-06-007-001-0_MONTAJE-ELECTROMECANICO_ADASA.docx
    (incluye figuras embebidas en el cuerpo y los 4 anexos paginados)

Path al skill: absoluto via ~/.claude/skills/template-adasa (CLAUDE.md S3,
Synology no soporta symlinks).
"""

import os
import sys

SKILL_PATH = os.path.expanduser("~/.claude/skills/template-adasa")
sys.path.insert(0, SKILL_PATH)

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    add_simple_table,
    add_bullet,
)
from docx import Document  # noqa: E402
from docx.shared import Cm, Inches, Pt  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.enum.section import WD_ORIENT  # noqa: E402

# Limpieza de metadatos (regla global S2.3)
try:
    from docx_metadata import apply_core_properties, fix_app_xml  # noqa: E402
    METADATA_DISPONIBLE = True
except ImportError:
    METADATA_DISPONIBLE = False
    print("[aviso] docx_metadata no disponible; metadatos no se limpiaran.")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURAS_DIR = os.path.join(SCRIPT_DIR, "figuras")
OUTPUT = os.path.join(
    SCRIPT_DIR,
    "P22-ET-06-007-001-0_MONTAJE-ELECTROMECANICO_ADASA.docx",
)


# ---------------------------------------------------------------------------
# Helpers de redaccion
# ---------------------------------------------------------------------------


def add_para(doc, text, size=11, justify=True):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    if justify:
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return para


def add_para_bold_lead(doc, lead, body, size=11):
    para = doc.add_paragraph()
    run_lead = para.add_run(lead)
    run_lead.bold = True
    run_lead.font.name = "Arial"
    run_lead.font.size = Pt(size)
    run_body = para.add_run(body)
    run_body.font.name = "Arial"
    run_body.font.size = Pt(size)
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return para


def add_titulo_tabla(doc, label):
    """Inserta un titulo de tabla (Tabla N.M — Nombre) centrado, negrita,
    Arial 10 pt. Llamar inmediatamente antes de add_simple_table()."""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(label)
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(10)
    return para


def add_figura(doc, filename, leyenda, ancho_cm=15):
    """Inserta figura centrada con leyenda en cursiva debajo."""
    path = os.path.join(FIGURAS_DIR, filename)
    if not os.path.exists(path):
        print(f"  [aviso] figura no encontrada: {filename}")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(path, width=Cm(ancho_cm))
    # Leyenda
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_run = cap.add_run(leyenda)
    cap_run.italic = True
    cap_run.font.name = "Arial"
    cap_run.font.size = Pt(10)


def add_anexo_paginado(doc, titulo, png_files, apaisado=True):
    """Inserta seccion de anexo con paginas como imagenes a pagina completa.
    Cambia orientacion a apaisada para que los planos quepan a mayor escala.
    """
    # Encabezado de anexo
    doc.add_heading(titulo, level=1)
    # Por cada pagina del anexo, una imagen tan grande como quepa
    for i, png in enumerate(png_files):
        path = os.path.join(FIGURAS_DIR, png)
        if not os.path.exists(path):
            print(f"  [aviso] {png} no encontrado")
            continue
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        # Ancho variable segun orientacion definida en la seccion contenedora
        run.add_picture(path, width=Cm(24 if apaisado else 16))
        if i < len(png_files) - 1:
            doc.add_page_break()


# ---------------------------------------------------------------------------
# Cuerpo del documento
# ---------------------------------------------------------------------------


def construir_seccion_generalidades(doc):
    doc.add_heading("GENERALIDADES", level=1)

    doc.add_heading("Introduccion", level=2)
    add_para(
        doc,
        "Aguas de Antofagasta S.A. (en adelante ADASA) ejecuta el proyecto "
        "Modulo de Salmuera Taltal, que incorpora a la planta de osmosis "
        "inversa existente un sistema de contencion e impulsion de salmuera "
        "dimensionado para alimentar el nuevo modulo UHPRO. Las obras civiles "
        "correspondientes (fundacion comun y radier perimetral) son entregadas "
        "por terceros, en estado terminado, antes del inicio de las actividades "
        "de la presente especificacion. El alcance que aqui se define cubre el "
        "montaje electromecanico de los dos equipos de proceso instalados sobre "
        "dicha fundacion.",
    )

    doc.add_heading("Objeto y Alcance", level=2)
    add_para(
        doc,
        "Este documento establece los requisitos tecnicos que debe cumplir el "
        "contratista de montaje (en adelante el Contratista) para ejecutar el "
        "montaje electromecanico de los siguientes equipos a entera satisfaccion "
        "de ADASA:",
    )
    add_bullet(doc, "Estanque de Salmuera TK-06-001 (Polimero Reforzado con Fibra de Vidrio, capacidad 10 m3).")
    add_bullet(doc, "Bomba de Alimentacion de Salmuera BH-06-001 (KSB, centrifuga horizontal, con motor electrico WEH 11 kW).")

    add_para(
        doc,
        "El alcance abarca la totalidad de los recursos, mano de obra, "
        "herramientas, consumibles y servicios requeridos para: recepcion y "
        "resguardo de los equipos en obra, posicionamiento, nivelacion, "
        "alineamiento, anclaje definitivo, conexionado de bridas, prueba "
        "hidrostatica del estanque y entrega documental del montaje en formato "
        "dossier as-built. La fabricacion, el transporte hasta obra, el montaje "
        "de canerias de proceso entre el estanque y la bomba, la instalacion "
        "electrica de fuerza desde el centro de control de motores hasta la "
        "bornera del motor, las pruebas electricas del motor, la verificacion "
        "del sentido de rotacion, el rodaje y la conexion de instrumentacion "
        "quedan fuera del alcance de esta especificacion: corresponden a las "
        "disciplinas de electricidad e instrumentacion y a la puesta en "
        "marcha, y se rigen por sus respectivos pliegos.",
    )
    add_para(
        doc,
        "Las actividades cumpliran con los estandares definidos por ADASA en la "
        "documentacion tecnica del proyecto y con las instrucciones de montaje, "
        "operacion y mantenimiento (IO&M) entregadas por los fabricantes de cada "
        "equipo.",
    )

    doc.add_heading("Documentos de Referencia", level=2)
    add_titulo_tabla(doc, "Tabla 1.1 — Documentos de Referencia.")
    add_simple_table(doc, [
        ("Codigo", "Documento", "Revision", "Emisor"),
        ("P22-ET-06-005-001", "Hoja de Datos — Bomba de Alimentacion Salmuera", "0", "Van Doorn / ADASA"),
        ("P22-ET-06-005-002", "Hoja de Datos — Estanque de Salmuera", "0", "Van Doorn / ADASA"),
        ("P22-IT-06-000-005-0", "Revision Memoria de Calculo Estanque TK-06-001 (analisis sismico y verificacion de anclaje)", "0", "ADASA"),
        ("P22-DWG-06-005-101-0", "Plano de Montaje — TK Salmuera y Bba Alimentacion Salmuera (emitido Apto para Construccion)", "0", "ADASA"),
        ("EX-26005-F01", "Plano dimensional Estanque de Salmuera", "0", "Fabricante PRFV"),
        ("KSB-AAF-KNCPP11-050+160M", "Plano dimensional Bomba KSB", "A", "KSB"),
        ("P04-ET-00-005-105", "ET Montaje Electromecanico PDA (referencia metodologica)", "0", "ADASA"),
    ])
    add_para(
        doc,
        "Las hojas de datos P22-ET-06-005-001 y P22-ET-06-005-002 definen el "
        "diseno funcional de los equipos. Esta especificacion define como se "
        "montan; no las sustituye ni las modifica.",
    )

    doc.add_heading("Normativa Aplicable", level=2)
    for norma in [
        "API 610 / ISO 13709 — Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries (clausulas de instalacion, nivelacion y alineamiento de bombas).",
        "ASME B16.5 — Pipe Flanges and Flanged Fittings (conexiones bridadas Clase 150 del estanque y la bomba).",
        "ASME RTP-1 — Reinforced Thermoset Plastic Corrosion-Resistant Equipment (fabricacion e inspeccion del estanque PRFV).",
        "ASTM A193 / A194 — Materiales para pernos y tuercas en servicio de proceso.",
        "NCh 2369 — Diseno Sismico de Estructuras e Instalaciones Industriales (criterios de anclaje sismico).",
        "Decreto Supremo N 594 / 2000 — Condiciones Sanitarias y Ambientales Basicas en los Lugares de Trabajo.",
        "Decreto Supremo N 132 / 2002 — Reglamento de Seguridad Minera (en lo aplicable a izaje y trabajos en altura).",
    ]:
        add_bullet(doc, norma)

    doc.add_heading("Jerarquia Contractual", level=2)
    add_para(
        doc,
        "En caso de discrepancia entre los documentos del Proyecto, prevalecera "
        "el siguiente orden, de mayor a menor jerarquia: contrato y bases "
        "administrativas; presente Especificacion Tecnica de Montaje "
        "Electromecanico; hojas de datos de los equipos; planos de montaje e "
        "ingenieria de detalle ADASA; documentacion de los fabricantes (IO&M, "
        "planos dimensionales); normas referenciadas. El Contratista informara "
        "por escrito y de inmediato a ADASA cualquier omision o discrepancia "
        "detectada antes del inicio de la actividad afectada, para que ADASA "
        "emita la aclaracion correspondiente.",
    )


def construir_seccion_suministros(doc):
    doc.add_heading("SUMINISTROS Y APORTES", level=1)

    doc.add_heading("Aportes de ADASA", level=2)
    add_para(
        doc,
        "ADASA entregara al Contratista en bodega de obra, contra acta de "
        "recepcion firmada, los siguientes elementos:",
    )
    for item in [
        "Estanque de Salmuera TK-06-001 con sus accesorios estructurales (sillas de anclaje, orejas de izaje incorporadas al manto, regleta de medicion de volumen y placa de identificacion).",
        "Pernos de anclaje, llaves de corte (topes) y tuercas de las sillas del estanque, en acero inoxidable AISI 316.",
        "Bomba de Alimentacion BH-06-001 con su motor electrico WEH montado y acoplado a fabrica, baseplate BD-0502-B, acoplamiento Normex E-97 con guardera, y los pernos de anclaje de la baseplate.",
        "Planos de montaje aprobados para construccion.",
        "Manuales de Instalacion, Operacion y Mantenimiento de cada equipo.",
        "Hojas de datos de los equipos.",
        "Certificados de origen, certificados de materiales y certificados de pruebas de fabrica de cada equipo.",
    ]:
        add_bullet(doc, item)
    add_para(
        doc,
        "La fundacion de hormigon armado, los embebidos de anclaje, el radier "
        "perimetral y la canalizacion para el drenaje de la zona de bombas se "
        "ejecutan dentro del alcance de obras civiles del mismo contrato "
        "(Bases de Licitacion de Montaje Mecanico y Obras Civiles). La "
        "superficie de la fundacion debe quedar lista para recibir grout, con "
        "la cota de terminacion de obra civil declarada en el plano de montaje "
        "y con los embebidos de anclaje correctamente posicionados, antes de "
        "iniciar el montaje del equipo respectivo.",
    )

    doc.add_heading("Aportes del Contratista", level=2)
    add_para(doc, "El Contratista contemplara el suministro de los siguientes recursos y consumibles:")
    for item in [
        "Mano de obra directa, indirecta y supervision tecnica en la cantidad y calificacion necesarias para cumplir los plazos y la calidad exigidos.",
        "Equipos de izaje (grua movil, eslingas, yugos, grilletes), de capacidad acreditada y con certificado de inspeccion vigente.",
        "Equipos topograficos (estacion total o nivel optico) con certificado de calibracion vigente.",
        "Alineador laser para alineamiento bomba-motor, con certificado de calibracion vigente.",
        "Llaves dinamometricas y multiplicadores de torque, en el rango requerido para los pernos de anclaje, en buen estado y con certificado de calibracion vigente.",
        "Placa de nivelacion de 16 mm mecanizada, lainas de precision en acero inoxidable AISI 316 y tornilleria auxiliar para nivelacion.",
        "Mortero de grout Sikagrout 214 (o equivalente expansivo de resistencia no inferior a 60 MPa a 28 dias, previa aprobacion de ADASA por escrito) y junta elastomera para la silla del estanque.",
        "Pintura de retoque (touch-up) compatible con el esquema original del estanque y de la baseplate, sello hidrofugo para boquillas y cinta de teflon o sellador para juntas de tuberias auxiliares.",
        "Andamios certificados, escaleras, lineas de vida y arnes para trabajos en altura.",
        "Carpas plasticas, cubiertas y vallas para proteccion de los equipos almacenados.",
        "Combustible y consumibles para la generacion electrica en obra, si fuera necesaria.",
    ]:
        add_bullet(doc, item)
    add_para(
        doc,
        "El Contratista sera responsable de toda falla derivada del uso, manejo "
        "o instalacion de los equipos, materiales, insumos, herramientas y "
        "maquinaria a su cargo.",
    )

    doc.add_heading("Equipos y Herramientas con Calibracion Vigente", level=2)
    add_para(
        doc,
        "Los equipos de medicion utilizados en hitos de aceptacion (nivel, "
        "alineamiento, torque) exigiran certificado de "
        "calibracion trazable a patron nacional, con vigencia no superior a "
        "doce meses contados desde la fecha de uso. El Contratista entregara "
        "copia de los certificados a la Inspeccion Tecnica de ADASA antes de "
        "iniciar la actividad correspondiente. Equipos sin calibracion vigente "
        "seran retirados de obra y la actividad se suspendera hasta su reemplazo.",
    )


def construir_seccion_recepcion(doc):
    doc.add_heading("RECEPCION Y ALMACENAMIENTO DE EQUIPOS", level=1)

    doc.add_heading("Inspeccion de Recepcion", level=2)
    add_para(
        doc,
        "El traslado del estanque y de la bomba desde la bodega de ADASA al "
        "lugar de montaje sera coordinado entre el Contratista y la Inspeccion "
        "Tecnica. A la llegada de cada equipo a obra, antes del descenso de los "
        "embalajes, se realizara en conjunto la siguiente verificacion:",
    )
    for v in [
        "Concordancia del equipo con su orden de compra y con su hoja de datos (TAG, fabricante, modelo, numero de serie, numero de fabricacion).",
        "Integridad fisica del embalaje y del equipo (golpes, rasgunos, deformaciones, pintura danada, humedad).",
        "Presencia de los accesorios listados en el packing list del fabricante (en el caso de la bomba: acoplamiento, guardera, pernos del baseplate, pliego de planos as-built).",
        "Coincidencia de las boquillas y conexiones con la hoja de datos (cantidad, diametro, orientacion, rating).",
    ]:
        add_bullet(doc, v)
    add_para(
        doc,
        "El resultado de la inspeccion quedara registrado en un protocolo de "
        "recepcion firmado por ambas partes. Si se detectaren faltantes o danos, "
        "ADASA decidira la accion correctiva: rechazo del equipo, recepcion "
        "condicionada con observaciones por levantar, o aceptacion con concesion "
        "documentada. Ningun equipo no aceptado podra montarse hasta que su "
        "condicion sea regularizada por ADASA.",
    )

    doc.add_heading("Almacenamiento Provisional", level=2)
    add_para(
        doc,
        "Mientras los equipos no se monten en su posicion definitiva, el "
        "Contratista los resguardara en una zona limpia, plana, con drenaje "
        "superficial, protegida del transito vehicular y de operaciones de "
        "construccion adyacentes. Las condiciones especificas son:",
    )
    add_para_bold_lead(
        doc, "Estanque PRFV. ",
        "Resguardar de la radiacion ultravioleta directa por periodos prolongados; "
        "el PRFV es sensible al envejecimiento por UV cuando no se cuenta con la "
        "barrera externa pigmentada en servicio. Si el estanque permaneciera en "
        "obra mas de treinta dias antes del montaje definitivo, se cubrira con "
        "una carpa opaca que permita ventilacion. Posicionar horizontal sobre "
        "cunas de madera o caucho, sin apoyar el manto sobre superficies duras o "
        "irregulares.",
    )
    add_para_bold_lead(
        doc, "Bomba con motor. ",
        "Mantener el conjunto sobre la baseplate original, en posicion horizontal, "
        "con cubierta impermeable y los flanges de succion y descarga protegidos "
        "con tapas plasticas. Conservar el sello mecanico libre de polvo y humedad. "
        "Rotar manualmente el eje al menos una vez por semana, en al menos dos "
        "vueltas completas, para impedir el asentamiento del lubricante en los "
        "rodamientos.",
    )
    add_para(
        doc,
        "El Contratista se mantendra responsable de los equipos desde la "
        "recepcion hasta la aceptacion final del montaje por parte de ADASA.",
    )

    doc.add_heading("Manipulacion e Izaje", level=2)
    add_para(
        doc,
        "Todas las maniobras de izaje seran planificadas en un procedimiento "
        "escrito de izaje aprobado por la prevencion de riesgos del Contratista "
        "y validado por la Inspeccion Tecnica de ADASA antes de su ejecucion. "
        "El procedimiento incluira: equipo de izaje seleccionado y su diagrama "
        "de carga, rigging plan con accesorios y angulos de eslingas, peso del "
        "equipo declarado por el fabricante, masa total de la carga incluido el "
        "rigging, ruta de la maniobra, zona de exclusion, comunicaciones, "
        "condiciones meteorologicas maximas admisibles, responsable del izaje y "
        "testigos.",
    )
    add_para_bold_lead(
        doc, "Estanque. ",
        "El levantamiento se realizara unicamente mediante las orejas de izaje "
        "integradas en el manto del estanque y con yugos o vigas distribuidoras "
        "cuando el angulo de eslinga lo requiera. No se aceptaran eslingados "
        "directos al manto, al fondo o a las boquillas. El estanque se levantara "
        "en posicion vertical o se rotara desde horizontal a vertical en el aire, "
        "segun lo defina el procedimiento, evitando flexiones del manto.",
    )
    add_para_bold_lead(
        doc, "Bomba. ",
        "El levantamiento se realizara por las orejas de izaje de la baseplate. "
        "Esta prohibido el levantamiento por las orejas de izaje del motor o de "
        "la voluta de la bomba para mover el conjunto montado en baseplate; "
        "estas orejas estan dimensionadas para el componente individual, no para "
        "el conjunto.",
    )
    add_para(
        doc,
        "Ningun equipo se dejara caer ni recibira golpes durante la maniobra. "
        "La descarga sobre la fundacion se realizara lentamente, controlando la "
        "orientacion con cuerdas guia operadas desde el suelo. La zona de "
        "exclusion bajo la carga suspendida se mantendra libre de personas "
        "durante toda la maniobra.",
    )


def construir_seccion_bases(doc):
    doc.add_heading("BASES DE HORMIGON Y ANCLAJES", level=1)

    doc.add_heading("Verificacion Topografica de las Bases", level=2)
    add_para(
        doc,
        "Antes del posicionamiento de cualquier equipo, el Contratista "
        "realizara un levantamiento topografico de la fundacion entregada por "
        "la obra civil, con el siguiente alcance minimo:",
    )
    for item in [
        "Verificacion de la cota absoluta de la cara superior de la fundacion contra la cota declarada en el Plano de Montaje — TK Salmuera y Bba Alimentacion Salmuera.",
        "Verificacion de la planimetria de la huella del estanque y de la huella de la baseplate de la bomba.",
        "Verificacion de la posicion planimetrica y altimetrica de los embebidos de anclaje (pernos quimicos prearmados, o casquillos para pernos mecanicos, segun lo dispuesto por la ingenieria de detalle).",
        "Verificacion de la rugosidad superficial de la zona de grout. La rugosidad debera garantizar adherencia adecuada entre el hormigon existente y el grout; si la superficie estuviera lisa por curado humedo prolongado o presencia de lechada, el Contratista la picara mecanicamente hasta exponer arido grueso (chipping ligero).",
    ]:
        add_bullet(doc, item)
    add_para(doc, "Las tolerancias de aceptacion previas al montaje son las siguientes:")
    add_titulo_tabla(doc, "Tabla 4.1 — Tolerancias de aceptacion de la fundacion entregada.")
    add_simple_table(doc, [
        ("Parametro", "Tolerancia"),
        ("Cota de la fundacion respecto a plano", "+/- 5 mm"),
        ("Planimetria (desnivel maximo de la huella del equipo)", "+/- 3 mm en cualquier direccion"),
        ("Posicion planimetrica de embebidos", "+/- 5 mm"),
        ("Posicion altimetrica de embebidos", "+/- 3 mm"),
    ])
    add_para(
        doc,
        "Si la fundacion no cumple alguna de estas tolerancias, el Contratista "
        "ejecutara las correcciones en su propia obra civil antes de iniciar "
        "el montaje y dejara registro del levantamiento topografico. La "
        "verificacion topografica conforme constituye un punto de control "
        "(hold point) interno previo al montaje, sujeto a la inspeccion de la "
        "Inspeccion Tecnica de ADASA; el montaje no comenzara hasta que la "
        "fundacion cumpla las tolerancias de la Tabla 4.1.",
    )

    doc.add_heading("Pernos de Anclaje del Estanque", level=2)
    add_para(
        doc,
        "Los pernos y topes de corte del estanque son aporte de ADASA, en acero "
        "inoxidable AISI 316. La cantidad, diametro, posicion y profundidad de "
        "anclaje estan definidos en el Plano de Montaje y en la verificacion de "
        "anclaje del documento Revision Memoria de Calculo Estanque TK-06-001 "
        "(referencia para los valores de torque y las cargas sismicas de "
        "diseno). El Contratista respetara rigurosamente esos valores; cualquier "
        "alternativa requerira aprobacion escrita previa de ADASA.",
    )
    add_figura(
        doc, "fig-4-1.png",
        "Figura 4.1 — Detalle de anclajes de las sillas del estanque "
        "(referencia: plano EX-26005-F01).",
        ancho_cm=15,
    )
    add_para(
        doc,
        "El apriete de los pernos de las sillas se ejecutara con llave "
        "dinamometrica calibrada, siguiendo un patron cruzado-radial que asegure "
        "el reparto uniforme de la carga entre todas las sillas. El apriete se "
        "realizara en al menos dos pasadas: una primera pasada al 50 % del "
        "torque nominal, una segunda pasada al 100 % del torque nominal. La "
        "verificacion final del torque quedara registrada perno por perno en el "
        "protocolo de torque del estanque.",
    )
    add_figura(
        doc, "fig-4-2.png",
        "Figura 4.2 — Patron cruzado-radial de apriete de pernos de sillas.",
        ancho_cm=12,
    )

    doc.add_heading("Pernos de Anclaje de la Bomba", level=2)
    add_para(
        doc,
        "La baseplate BD-0502-B de la bomba se anclara a la fundacion con los "
        "pernos suministrados por ADASA, conforme al plano dimensional "
        "KSB-AAF-KNCPP11-050+160M_A y al Plano de Montaje. El apriete final se "
        "realizara despues de la nivelacion, antes de la aplicacion de grout, "
        "con un primer apriete a punto, y se completara tras el fraguado del "
        "grout con apriete al torque definitivo. El procedimiento detallado se "
        "describe en la Seccion Montaje de la Bomba de Alimentacion.",
    )

    doc.add_heading("Punto de Control Previo al Montaje", level=2)
    add_para(
        doc,
        "La conformidad topografica de la fundacion es un punto de control "
        "(hold point) previo al inicio del montaje del equipo respectivo. El "
        "Contratista verifica el cumplimiento de las tolerancias de la Tabla "
        "4.1, ejecuta las correcciones que correspondan dentro de su propia "
        "obra civil y registra el resultado (mediciones, fotografias, "
        "observaciones) en el protocolo correspondiente, que queda sujeto a la "
        "inspeccion de la Inspeccion Tecnica de ADASA. Como la obra civil y el "
        "montaje se ejecutan bajo el mismo contrato, la verificacion es un "
        "control de calidad interno y no una aceptacion o rechazo entre "
        "partes.",
    )


def construir_seccion_estanque(doc):
    doc.add_heading("MONTAJE DEL ESTANQUE DE SALMUERA (TK-06-001)", level=1)

    doc.add_heading("Caracteristicas del Equipo", level=2)
    add_para(
        doc,
        "El estanque TK-06-001 es un recipiente vertical de polimero reforzado "
        "con fibra de vidrio fabricado conforme a ASME RTP-1, de 2.600 mm de "
        "diametro interno y 2.600 mm de altura cilindrica, con un volumen util "
        "de 10 m3. Cuenta con barrera quimica interna de resina vinilester con "
        "fibra de vidrio de espesor superior a 2,5 mm, y refuerzo mecanico "
        "exterior de resina ortoftalica con fibra de vidrio aplicada por "
        "enrollamiento mecanico. El fondo es plano y el techo es de doble radio "
        "o plano, segun lo definido por el fabricante.",
    )
    add_para(
        doc,
        "Las boquillas del estanque (todas en norma ASME B16.5, clase 150, "
        "cara Full Face) son las siguientes:",
    )
    add_titulo_tabla(doc, "Tabla 5.1 — Boquillas del Estanque de Salmuera TK-06-001.")
    add_simple_table(doc, [
        ("Identificacion", "Descripcion", "Diametro"),
        ("A", "Escotilla de Entrada de Hombre", "600 mm"),
        ("B", "Entrada de Salmuera", "4''"),
        ("C", "Transmisor de Nivel", "4''"),
        ("D", "Salida de Salmuera", "4''"),
        ("E", "Rebose", "4''"),
        ("F", "Drenaje", "2''"),
        ("G", "Switch de Nivel", "4''"),
        ("H", "Venteo", "6''"),
    ])
    add_figura(
        doc, "fig-5-1.png",
        "Figura 5.1 — Disposicion de boquillas del estanque "
        "(referencia: plano EX-26005-F01).",
        ancho_cm=15,
    )
    add_para(
        doc,
        "El estanque incluye sillas de anclaje, orejas de izado integradas al "
        "manto, regleta de medicion de volumen y placa de identificacion. La "
        "orientacion de las boquillas en obra debe coincidir con el Plano de "
        "Montaje y con el plano dimensional EX-26005-F01 del fabricante.",
    )

    doc.add_heading("Procedimiento de Montaje", level=2)

    doc.add_heading("Preparacion", level=3)
    add_para(
        doc,
        "El Contratista limpiara la zona de fundacion previa al posicionamiento, "
        "eliminando cualquier resto de material, polvo o lechada que pueda danar "
        "la cara inferior del estanque. La junta elastomera entre la silla y la "
        "fundacion, suministrada por el Contratista, se posicionara centrada "
        "sobre los embebidos de anclaje.",
    )

    doc.add_heading("Posicionamiento sobre la Fundacion", level=3)
    add_para(
        doc,
        "El estanque se izara en posicion vertical hasta alinear los pasadores "
        "de las sillas con los embebidos de la fundacion. La maniobra se "
        "controlara desde el suelo con cuerdas guia. El descenso final se "
        "realizara lentamente, milimetro a milimetro en los ultimos centimetros, "
        "verificando que cada perno entre limpiamente en su casquillo o aloje en "
        "la silla sin forzar. La orientacion angular del estanque debera hacer "
        "coincidir las boquillas con las direcciones declaradas en el Plano de "
        "Montaje, con una tolerancia angular maxima de 1 grado.",
    )
    add_figura(
        doc, "fig-5-2.png",
        "Figura 5.2 — Posicion de orejas de izaje del estanque "
        "(referencia: plano EX-26005-F01).",
        ancho_cm=15,
    )

    doc.add_heading("Verticalidad y Plomo", level=3)
    add_para(
        doc,
        "Una vez asentado el estanque, antes del apriete definitivo, se "
        "verificara la verticalidad del manto en al menos cuatro generatrices "
        "separadas 90 grados entre si. La desangulacion maxima admisible entre "
        "la base y el punto mas alto del manto es de 5 mm. Si la desangulacion "
        "supera ese valor, el Contratista corregira mediante lainas de acero "
        "inoxidable en las sillas afectadas hasta alcanzar la tolerancia. La "
        "medicion se registrara en el protocolo de verticalidad del estanque.",
    )

    doc.add_heading("Apriete de Pernos de Sillas", level=3)
    add_para(
        doc,
        "Una vez aceptada la verticalidad, se procedera al apriete de los "
        "pernos de las sillas conforme al patron cruzado-radial descrito en la "
        "Seccion Bases de Hormigon y Anclajes, con el torque establecido en el "
        "documento Revision Memoria de Calculo Estanque TK-06-001. La "
        "verificacion de torque se ejecutara perno por perno y se documentara "
        "en el protocolo correspondiente.",
    )

    doc.add_heading("Conexion de Boquillas", level=3)
    add_para(
        doc,
        "Las boquillas del estanque (entrada, salida, rebose, drenaje, venteo, "
        "transmisor de nivel, switch de nivel) se entregan ciegas o con tapas "
        "plasticas. La instalacion de las canerias de proceso conectadas a esas "
        "boquillas esta fuera del alcance del presente contrato; sin embargo, "
        "el Contratista garantizara que las tapas plasticas o ciegos permanezcan "
        "instalados hasta la prueba hidrostatica y que ninguna boquilla quede "
        "expuesta a la intemperie sin proteccion.",
    )
    add_para(
        doc,
        "La conexion de las canerias la ejecutara el contratista de tuberias, "
        "con la precaucion de no transmitir cargas mecanicas residuales a las "
        "boquillas del estanque. El Contratista de montaje, en su rol de "
        "receptor del equipo, dejara constancia escrita ante la Inspeccion "
        "Tecnica si detecta tensiones residuales o desalineamientos en las "
        "bridas de conexion al momento de su conexionado.",
    )

    doc.add_heading("Verificacion de Estanqueidad — Prueba Hidrostatica", level=3)
    add_para(
        doc,
        "Una vez completado el montaje, el apriete de los pernos y la conexion "
        "de la boquilla de salida con un ciego provisorio (si aun no se ha "
        "conectado la caneria de proceso), se ejecutara la prueba hidrostatica "
        "del estanque conforme al procedimiento aprobado del fabricante PRFV. "
        "El estanque se llenara progresivamente con agua limpia hasta su nivel "
        "de rebose en al menos tres etapas (33 %, 66 %, 100 %), con inspeccion "
        "visual del manto, del fondo y de las boquillas en cada etapa. Una vez "
        "alcanzado el llenado al 100 %, el estanque se mantendra lleno durante "
        "un periodo minimo de 24 horas. La aceptacion requiere ausencia total "
        "de fugas, exudaciones por la pared, deformacion permanente en la zona "
        "de sillas o filtraciones en las uniones bridadas. El descenso de nivel "
        "atribuible a evaporacion se cuantificara por separado y no sera "
        "computado como perdida.",
    )
    add_para(
        doc,
        "La prueba sera presenciada por la Inspeccion Tecnica de ADASA y por "
        "el representante del fabricante PRFV cuando este disponible; sus "
        "resultados se registraran en el protocolo de prueba hidrostatica del "
        "estanque.",
    )


def construir_seccion_bomba(doc):
    doc.add_heading("MONTAJE DE LA BOMBA DE ALIMENTACION (BH-06-001)", level=1)

    doc.add_heading("Caracteristicas del Equipo", level=2)
    add_para(
        doc,
        "La bomba BH-06-001 es una bomba centrifuga de voluta de instalacion "
        "horizontal, modelo KSB KNCPP 11-050 5A, accionada por un motor "
        "electrico WEH W22 trifasico de 11 kW (15 HP), 2 polos, 2.955 rpm, "
        "380 V / 50 Hz, IE3, IP55, carcasa 160M, apto para operacion con "
        "variador de frecuencia. La bomba opera con salmuera de osmosis inversa "
        "con densidad 1,05 kg/l, temperatura entre 13 C y 22 C, pH 8 a 9, "
        "solidos disueltos totales entre 50.000 y 60.000 mg/l y cloruros hasta "
        "33.000 mg/l. Sus condiciones nominales de operacion son caudal 48,2 "
        "m3/h, altura total de elevacion 40 m.c.a. y NPSH disponible 9 m.c.a.",
    )
    add_para(
        doc,
        "Los materiales de carcasa, impulsor y eje son acero inoxidable "
        "Superduplex con PREN superior a 40. El conjunto bomba-motor llega de "
        "fabrica acoplado mediante un acoplamiento Normex E-97 con guardera, "
        "montado sobre la baseplate BD-0502-B de acero al carbono ASTM A36. "
        "Las conexiones de proceso son: succion DN80 ASME B16.5 clase 150 RF, "
        "descarga DN50 ASME B16.5 clase 150 RF. Las cargas y momentos maximos "
        "admisibles en cada boquilla, segun el plano dimensional KSB, son Mx, "
        "My y Mz iguales o inferiores a 650 N m.",
    )

    doc.add_heading("Procedimiento de Montaje", level=2)

    doc.add_heading("Posicionamiento de la Baseplate", level=3)
    add_para(
        doc,
        "La baseplate se posicionara sobre la fundacion con los pernos de "
        "anclaje pasando libremente por sus agujeros, sin forzar. El conjunto "
        "descansara sobre tornillos de nivelacion (jackscrews) o sobre la placa "
        "de nivelacion de 16 mm mecanizada, dejando una separacion nominal de "
        "25 mm entre la cara inferior de la baseplate y la cara superior de la "
        "fundacion; ese espacio se rellenara con grout en una etapa posterior. "
        "El centro geometrico de la baseplate quedara alineado con las "
        "coordenadas indicadas en el Plano de Montaje, con una tolerancia de "
        "+/- 5 mm en planta.",
    )

    doc.add_heading("Nivelacion", level=3)
    add_para(
        doc,
        "La nivelacion se ejecutara conforme a API 610 / ISO 13709, parrafo "
        "6.3.3, que establece una tolerancia maxima de coplanaridad de la "
        "superficie superior de la baseplate de 0,002 in/ft (0,17 mm/m). La "
        "medicion se realizara con un nivel de precision calibrado (con "
        "sensibilidad minima de 0,02 mm/m) sobre la superficie mecanizada de la "
        "baseplate, en dos direcciones perpendiculares: longitudinal a la linea "
        "de centro del eje y transversal a ella. Si la coplanaridad excediere "
        "la tolerancia, el Contratista ajustara con lainas de precision en "
        "acero inoxidable colocadas entre la baseplate y la placa de nivelacion, "
        "hasta alcanzar el valor admisible. La medicion final se registrara en "
        "el protocolo de nivelacion.",
    )
    add_para(
        doc,
        "Adicionalmente, se verificara la condicion de pie cojo en la "
        "baseplate. El pie cojo maximo admisible es de 0,05 mm (2,0 mils), "
        "conforme a la Tabla de Tolerancia de Ejes de la ET PDA referencia. Si "
        "el pie cojo supera ese valor, se corregira con laina de precision en "
        "el pie afectado, en la cara opuesta del jack screw que produce la "
        "deflexion.",
    )

    doc.add_heading("Pre-grout y Aplicacion del Grout", level=3)
    add_para(doc, "Una vez aceptada la nivelacion, se procedera al pre-grout. El procedimiento sera:")
    for i, item in enumerate([
        "Limpiar la superficie de la fundacion bajo la baseplate con aire comprimido seco y aspirador; eliminar todo resto de polvo, aceite, hidrocarburo o lechada de hormigon.",
        "Humedecer la superficie de la fundacion durante un periodo minimo de dos horas previas al vertido del grout. La superficie debe estar saturada pero sin agua libre.",
        "Verificar el encofrado perimetral provisorio (formwork) que contendra el grout. El encofrado debera ser estanco, recto, con una altura tal que el nivel del grout supere la cara inferior de la baseplate en al menos 10 mm.",
        "Preparar el grout Sikagrout 214 conforme estrictamente a la hoja tecnica del fabricante (relacion agua/solidos, tiempo de mezclado, vida util de la mezcla). Aprobar la mezcla con la Inspeccion Tecnica antes de verterla.",
        "Verter el grout por un solo lado de la baseplate, dejando que fluya hacia el lado opuesto y desplace el aire atrapado, sin vibracion mecanica. Mantener el flujo continuo durante todo el vertido.",
        "Permitir el fraguado conforme a las recomendaciones del fabricante de Sikagrout. Como referencia indicativa, el tiempo minimo previo al apriete final de los pernos de anclaje no sera inferior a 24 horas a 20 C; en clima frio el tiempo se extendera conforme indique la hoja tecnica.",
        "Retirar el encofrado provisorio.",
    ], 1):
        add_bullet(doc, f"{i}. {item}")
    add_figura(
        doc, "fig-6-1.png",
        "Figura 6.1 — Esquema baseplate sobre fundacion: grout de 25 mm bajo "
        "el baseplate y relleno del frame metalico interno (Sikagrout 214 en "
        "ambos volumenes).",
        ancho_cm=16,
    )
    add_para(
        doc,
        "El espesor del grout entre la cara inferior de la baseplate y la cara "
        "superior de la fundacion sera de 25 mm nominales, conforme al criterio "
        "del PDA referencia y al alcance del fabricante del grout. No se "
        "aceptara disminucion de espesor por debajo de 20 mm en ningun punto. "
        "El frame metalico interno de la baseplate se rellena en su totalidad "
        "con el mismo Sikagrout 214 utilizado para la franja inferior; el "
        "relleno aporta masa, rigidiza el conjunto y reduce la transmision de "
        "vibraciones a la fundacion. La operacion se ejecuta en una sola etapa "
        "con la franja, o en una segunda etapa inmediatamente posterior, segun "
        "defina la hoja tecnica del grout para el espesor total a verter.",
    )

    doc.add_heading("Alineamiento Bomba-Motor", level=3)
    add_para(
        doc,
        "El conjunto bomba-motor se entrega acoplado y alineado de fabrica; no "
        "obstante, el transporte, el almacenamiento y la fijacion a la "
        "fundacion pueden alterar el alineamiento. El Contratista verificara el "
        "alineamiento del acoplamiento en tres oportunidades:",
    )
    for v in [
        "Despues de la nivelacion, antes del grout (primera medicion).",
        "Despues del fraguado del grout y del apriete final de los pernos de anclaje (segunda medicion).",
        "Despues de la conexion de las canerias de succion y descarga por parte del contratista de tuberias (tercera medicion), para detectar tensiones residuales transmitidas desde las canerias.",
    ]:
        add_bullet(doc, v)
    add_figura(
        doc, "fig-6-2.png",
        "Figura 6.2 — Setup esquematico de alineamiento laser bomba-motor.",
        ancho_cm=16,
    )
    add_para(
        doc,
        "El procedimiento de alineamiento utilizara un alineador laser con "
        "certificado de calibracion vigente y se realizara conforme al manual "
        "IO&M de la bomba KSB. En caso de que el manual no especifique "
        "tolerancias, se aplicaran las tolerancias maximas siguientes, "
        "expresadas como excentricidad medida cada 100 mm de diametro de "
        "acoplamiento, en funcion de la velocidad de operacion del eje:",
    )
    add_titulo_tabla(doc, "Tabla 6.1 — Tolerancias de paralelismo del acoplamiento bomba-motor por velocidad de eje.")
    add_simple_table(doc, [
        ("Velocidad del eje (rpm)", "Tolerancia aceptable (mm/100 mm)", "Tolerancia excelente (mm/100 mm)"),
        ("600 a 900", "0,19", "0,09"),
        ("1.200", "0,09", "0,06"),
        ("1.500", "0,06", "0,04"),
        ("1.800", "0,06", "0,03"),
        ("3.000 a 3.600", "0,03", "0,02"),
    ])
    add_para(
        doc,
        "Para el motor instalado a 2.955 rpm la tolerancia aplicable es la de "
        "la fila 3.000 a 3.600 rpm. El criterio excelente es el objetivo; el "
        "criterio aceptable se utilizara solo en caso de imposibilidad "
        "documentada de alcanzar el primero. El pie cojo se mantendra en todo "
        "momento por debajo de 0,05 mm. Cualquier modificacion en el "
        "alineamiento que se haya conseguido previamente con grout requerira la "
        "aprobacion escrita de la Inspeccion Tecnica antes de ejecutarse.",
    )
    add_para(
        doc,
        "Las lainas de correccion seran de acero inoxidable, de espesores "
        "trazables, y se mantendran bajo control del Contratista en obra "
        "durante todo el periodo de montaje.",
    )

    doc.add_heading("Apriete Final de Pernos", level=3)
    add_para(
        doc,
        "Una vez fraguado el grout y aceptado el alineamiento, el Contratista "
        "ejecutara el apriete final de los pernos de la baseplate con llave "
        "dinamometrica al torque indicado en el manual IO&M de la bomba KSB. "
        "Si el manual no especifica un valor de torque para los pernos "
        "suministrados por ADASA, se aplicara el torque correspondiente al "
        "grado del perno y a su diametro conforme a la norma ASTM A193 / ASTM "
        "A325, segun corresponda al material, lubricado con aceite ligero. La "
        "verificacion se registrara en el protocolo de torque de la bomba.",
    )
    add_para(
        doc,
        "Tras el apriete final se repetira la medicion de alineamiento del "
        "acoplamiento, conforme se describe en la Seccion Alineamiento "
        "Bomba-Motor.",
    )

    doc.add_heading("Conexiones de Bridas", level=3)
    add_figura(
        doc, "fig-6-3.png",
        "Figura 6.3 — Dimensiones de bridas y cargas/momentos maximos "
        "admisibles en boquillas (referencia: plano KSB).",
        ancho_cm=15,
    )
    add_para(
        doc,
        "La conexion de las canerias de succion y descarga a las bridas de la "
        "bomba la ejecutara el contratista de tuberias. El Contratista del "
        "presente montaje verificara, en presencia de la Inspeccion Tecnica, "
        "que las cargas y momentos transmitidos por las canerias a las "
        "boquillas de la bomba no excedan los limites del plano dimensional "
        "KSB (Mx, My, Mz iguales o inferiores a 650 N m por boquilla). Si "
        "despues de la conexion la medicion de alineamiento del acoplamiento "
        "sale de tolerancia, ello evidenciara tensiones residuales en la "
        "caneria y la Inspeccion Tecnica solicitara al contratista de tuberias "
        "que ajuste los soportes del tramo respectivo. El alineamiento se "
        "aceptara formalmente solo cuando se cumpla con la tolerancia con las "
        "canerias conectadas.",
    )


def construir_seccion_pruebas_motor(doc):
    doc.add_heading("PRUEBAS ELECTRICAS DEL MOTOR", level=1)
    add_para(
        doc,
        "Las pruebas electricas estaticas tienen por objeto validar que el "
        "motor llegue a obra en su estado de fabrica y que no haya sufrido "
        "dano durante el transporte, el almacenamiento o el montaje. Se "
        "ejecutan antes de la energizacion del motor desde el centro de "
        "control de motores, con el motor instalado sobre la baseplate y antes "
        "de la conexion de las canerias al sistema de proceso. El Contratista "
        "podra subcontratar la ejecucion de estas pruebas con una empresa "
        "especializada, manteniendo en todo caso la responsabilidad de "
        "planificacion, supervision y entrega documental.",
    )
    add_figura(
        doc, "fig-7-1.png",
        "Figura 7.1 — Esquema tipico de prueba Megger e Hipot sobre motor "
        "11 kW 380 V.",
        ancho_cm=15,
    )

    doc.add_heading("Resistencia de Devanado", level=2)
    add_para(
        doc,
        "Se medira la resistencia ohmica de cada devanado del estator con un "
        "microohmimetro o un puente Kelvin de baja resistencia. La medicion se "
        "realizara a temperatura ambiente medida y registrada. Los valores "
        "obtenidos se compararan con los de fabrica reportados en el "
        "certificado de pruebas del motor; la desviacion maxima admisible entre "
        "fases es de 5 % y la desviacion maxima respecto al valor de fabrica, "
        "corregida por temperatura, es de 10 %.",
    )

    doc.add_heading("Resistencia de Aislacion", level=2)
    add_para(
        doc,
        "Se medira la resistencia de aislacion entre cada devanado y la masa "
        "con un megger de tension 1.000 V de corriente continua conforme a "
        "IEEE 43. La duracion de la prueba sera de un minuto. La resistencia "
        "minima admisible a temperatura ambiente, corregida a 40 C, sera la "
        "indicada por la siguiente expresion referencial:",
    )
    add_para(doc, "R_min = (kV + 1) MOhm, donde kV es la tension nominal del motor expresada en kilovoltios.")
    add_para(
        doc,
        "Para un motor de 380 V (0,38 kV) el valor minimo es del orden de 1,4 "
        "MOhm. Valores tipicos en motores nuevos en condiciones normales de "
        "obra son del orden de cientos de megaohmios. Se rechazara todo valor "
        "inferior a 10 MOhm y, en valores entre 1,4 MOhm y 10 MOhm, se aplicara "
        "la prueba de Indice de Polarizacion descrita a continuacion para "
        "discriminar si la baja resistencia se debe a contaminacion superficial "
        "o a dano del aislamiento.",
    )

    doc.add_heading("Indice de Polarizacion", level=2)
    add_para(
        doc,
        "Sobre el mismo montaje de medicion de resistencia de aislacion, se "
        "ejecutara una prueba prolongada con megger de 1.000 V CC durante diez "
        "minutos. Se registrara el valor a los sesenta segundos (R60) y a los "
        "diez minutos (R600). El Indice de Polarizacion (PI) es la razon R600 "
        "/ R60. El criterio de aceptacion, conforme IEEE 43, es el siguiente:",
    )
    add_titulo_tabla(doc, "Tabla 7.1 — Criterios de aceptacion del Indice de Polarizacion (IEEE 43).")
    add_simple_table(doc, [
        ("Indice de Polarizacion", "Estado del aislamiento"),
        ("Mayor a 4", "Excelente"),
        ("2 a 4", "Bueno (aceptable)"),
        ("1 a 2", "Cuestionable (requiere analisis y decision de ADASA)"),
        ("Menor a 1", "Rechazado"),
    ])

    doc.add_heading("Rigidez Dielectrica (Prueba Hipot)", level=2)
    add_para(
        doc,
        "Se ejecutara prueba Hipot conforme al procedimiento aprobado del "
        "Contratista. La tension de prueba aplicada sera, salvo proposicion "
        "tecnicamente respaldada del Contratista aprobada por ADASA, dos veces "
        "la tension nominal de linea del motor mas mil volts, es decir, para "
        "un motor de 380 V:",
    )
    add_para(doc, "V_hipot = 2 x 380 + 1.000 = 1.760 V (minimo).")
    add_para(
        doc,
        "La duracion de aplicacion sera de un minuto y la modalidad podra ser "
        "corriente alterna o corriente continua, conforme al equipo Hipot "
        "disponible. La prueba se ejecutara con todos los devanados unidos "
        "entre si y la corriente de fuga se registrara. Cualquier descarga, "
        "rampa anomala de tension o corriente fuera de los limites del "
        "procedimiento causara el rechazo del motor, que sera informado de "
        "inmediato a ADASA.",
    )

    doc.add_heading("Verificacion de Sentido de Rotacion", level=2)
    add_para(
        doc,
        "Antes de la energizacion definitiva, se verificara el sentido de "
        "rotacion del motor desconectado mecanicamente de la bomba "
        "(acoplamiento separado, o motor solo, segun defina el procedimiento). "
        "Se energizara el motor por un periodo muy corto (toque electrico de "
        "aproximadamente un segundo) y se observara el sentido de rotacion del "
        "eje, que debera coincidir con la flecha indicada en la carcasa de la "
        "bomba. Si el sentido es contrario, se intercambiaran dos fases en la "
        "conexion del motor en la borna o en el centro de control de motores, "
        "segun corresponda. Repetir la verificacion hasta obtener el sentido "
        "correcto.",
    )
    add_para(
        doc,
        "Solamente con todas las pruebas anteriores aceptadas y el sentido de "
        "rotacion confirmado, se acoplara la bomba al motor y se autorizara la "
        "energizacion para la primera puesta en marcha y la verificacion "
        "operacional dentro del alcance del comisionamiento, que es ajeno al "
        "presente contrato.",
    )


def construir_seccion_protocolos(doc):
    doc.add_heading("PROTOCOLOS Y DOCUMENTACION ENTREGABLE", level=1)

    doc.add_heading("Matriz de Protocolos", level=2)
    add_para(
        doc,
        "El Contratista elaborara y entregara a la Inspeccion Tecnica los "
        "siguientes protocolos, todos en formato ADASA, firmados por el "
        "supervisor de montaje y por el representante de la Inspeccion Tecnica:",
    )
    add_titulo_tabla(doc, "Tabla 8.1 — Matriz de protocolos de montaje.")
    add_simple_table(doc, [
        ("Protocolo", "Cuando se ejecuta"),
        ("Recepcion de equipos", "A la llegada de cada equipo en obra"),
        ("Verificacion de la fundacion", "Antes del posicionamiento de cada equipo"),
        ("Verticalidad y plomo del estanque", "Despues del posicionamiento del estanque"),
        ("Apriete de pernos de sillas del estanque", "Despues del apriete final"),
        ("Prueba hidrostatica del estanque", "Despues del llenado y mantenimiento durante 24 h"),
        ("Nivelacion de baseplate de la bomba", "Despues de la nivelacion"),
        ("Aplicacion de grout", "Durante el vertido y al termino del fraguado"),
        ("Alineamiento bomba-motor (preliminar)", "Despues de la nivelacion, antes del grout"),
        ("Alineamiento bomba-motor (definitivo)", "Despues del apriete final"),
        ("Alineamiento bomba-motor (con canerias)", "Despues de la conexion de tuberias"),
        ("Apriete de pernos de baseplate", "Despues del fraguado del grout"),
        ("Recepcion provisional del montaje", "Al termino de todas las actividades, con punch list adjunto"),
    ])

    doc.add_heading("Plan de Inspeccion y Pruebas", level=2)
    add_para(
        doc,
        "El Contratista emitira un ITP integral que reuna las actividades "
        "anteriores, identificando para cada una el responsable, el criterio "
        "de aceptacion, los puntos de retencion (Hold Point — actividad "
        "detenida hasta inspeccion de ADASA), los puntos de presenciado "
        "(Witness Point — ADASA presencia pero no detiene la actividad), y los "
        "puntos de revision documental. Como punto de retencion mandatorio, "
        "ADASA fija al menos los siguientes:",
    )
    for item in [
        "Aceptacion de la fundacion previa al montaje (estanque y bomba, por separado).",
        "Aceptacion de la verticalidad del estanque antes del apriete definitivo.",
        "Aceptacion de la nivelacion de la baseplate antes del vertido de grout.",
        "Aceptacion del alineamiento bomba-motor definitivo.",
    ]:
        add_bullet(doc, item)
    add_para(
        doc,
        "El ITP final sera revisado y aprobado por ADASA antes del inicio de "
        "la primera actividad. Cualquier modificacion posterior sera coordinada "
        "y registrada formalmente.",
    )
    add_figura(
        doc, "fig-8-1.png",
        "Figura 8.1 — Diagrama de flujo del Plan de Inspeccion y Pruebas.",
        ancho_cm=13,
    )

    doc.add_heading("Dossier As-Built", level=2)
    add_para(
        doc,
        "A la terminacion del montaje, el Contratista entregara a ADASA un "
        "dossier as-built en formato digital con la siguiente estructura:",
    )
    for item in [
        "Seccion 1 — Informacion general (indice, equipo en alcance, contratista, fechas).",
        "Seccion 2 — Documentos de los fabricantes (manuales, certificados, planos as-built, certificados de calibracion utilizados).",
        "Seccion 3 — Protocolos completos firmados.",
        "Seccion 4 — Registros fotograficos por hito.",
        "Seccion 5 — Punch list final con cierre.",
        "Seccion 6 — Planos modificados en obra (red-line si aplica) y plano de implantacion as-built.",
    ]:
        add_bullet(doc, item)


def construir_seccion_hse(doc):
    doc.add_heading("SEGURIDAD Y MEDIO AMBIENTE", level=1)

    doc.add_heading("Disposiciones Generales", level=2)
    add_para(
        doc,
        "El Contratista cumplira la totalidad de la legislacion nacional "
        "aplicable y los procedimientos de seguridad de ADASA durante toda su "
        "permanencia en obra. Antes de iniciar cualquier actividad presentara, "
        "para revision y aprobacion de la Inspeccion Tecnica: matriz de "
        "identificacion de peligros y evaluacion de riesgos (IPER), "
        "procedimiento escrito de trabajo seguro por actividad relevante "
        "(izaje, trabajos en altura, espacio confinado), "
        "reglamento interno de orden, higiene y seguridad, charlas diarias de "
        "cinco minutos, y registros de capacitacion de su personal. El "
        "Contratista mantendra un prevencionista de riesgos calificado en obra "
        "durante toda la duracion de los trabajos.",
    )

    doc.add_heading("Trabajos en Altura e Izaje", level=2)
    add_para(
        doc,
        "Toda actividad por sobre 1,80 m de altura desde un punto de apoyo "
        "estable se considerara trabajo en altura y requerira uso obligatorio "
        "de arnes y linea de vida, andamios certificados, plataformas con "
        "barandas, y un procedimiento escrito especifico aprobado. Los izajes "
        "con grua movil se ejecutaran por personal calificado, con la zona "
        "delimitada por vallas y vigias; ninguna persona permanecera bajo "
        "carga suspendida ni en la zona de oscilacion de la carga durante la "
        "maniobra.",
    )

    doc.add_heading("Espacio Confinado", level=2)
    add_para(
        doc,
        "La inspeccion interna del estanque durante el montaje, la prueba "
        "hidrostatica y la entrega del dossier as-built constituye, conforme a "
        "la legislacion aplicable, una actividad en espacio confinado. Antes "
        "de ingresar al interior del estanque por la escotilla, se ejecutara "
        "el procedimiento de espacio confinado del Contratista que incluira, "
        "como minimo: aislacion de canerias de proceso del estanque (no aplica "
        "antes del comisionamiento, pero si cuando ya esten conectadas), "
        "medicion previa de atmosfera (oxigeno, gases inflamables, gases "
        "toxicos), monitoreo continuo durante la permanencia, ventilacion "
        "forzada si la medicion lo justifica, vigia permanente fuera del "
        "espacio confinado, comunicacion radial o sonora entre el vigia y el "
        "ingresante, equipo de rescate disponible.",
    )

    doc.add_heading("Gestion de Residuos", level=2)
    add_para(
        doc,
        "Los residuos generados durante el montaje (cartones, plasticos, "
        "restos de grout, panos, lainas no utilizadas, embalaje de los equipos) "
        "seran segregados, almacenados temporalmente en contenedores adecuados "
        "y retirados de obra por el Contratista. Los residuos peligrosos "
        "(panos con aceite, restos de pintura, lubricantes vencidos) se "
        "gestionaran como Residuos Industriales Peligrosos conforme a la "
        "legislacion vigente, con declaracion de transporte y disposicion "
        "final emitida por receptor autorizado, copia de la cual el "
        "Contratista entregara a ADASA.",
    )


def construir_seccion_hitos(doc):
    doc.add_heading("HITOS Y PUNCH LIST FINAL", level=1)

    doc.add_heading("Hitos de Avance", level=2)
    add_para(
        doc,
        "El programa detallado de obra (Programa Detallado de Construccion) "
        "sera emitido por el Contratista para revision y aprobacion de ADASA "
        "antes del inicio de los trabajos. El programa identificara al menos "
        "los siguientes hitos verificables:",
    )
    for item in [
        "H1 — Movilizacion a obra (recursos humanos, equipos, oficinas, instalaciones provisorias).",
        "H2 — Recepcion y aceptacion de la fundacion de obra civil.",
        "H3 — Posicionamiento del estanque sobre las sillas.",
        "H4 — Apriete final de pernos del estanque y aceptacion de verticalidad.",
        "H5 — Prueba hidrostatica del estanque aceptada.",
        "H6 — Nivelacion de baseplate de la bomba aceptada.",
        "H7 — Aplicacion de grout completa y aceptada.",
        "H8 — Alineamiento bomba-motor definitivo aceptado.",
        "H9 — Recepcion provisional del montaje (con punch list).",
        "H10 — Cierre del punch list y recepcion final.",
    ]:
        add_bullet(doc, item)

    doc.add_heading("Criterios de Cierre", level=2)
    add_para(
        doc,
        "Para cada hito el Contratista entregara a la Inspeccion Tecnica el "
        "protocolo correspondiente firmado, los registros de calibracion de "
        "los equipos de medicion utilizados, los registros fotograficos "
        "relevantes y, cuando aplique, los certificados de los materiales "
        "empleados. ADASA verificara el cumplimiento del criterio de "
        "aceptacion de cada hito y emitira su conformidad por escrito o, en "
        "caso contrario, las observaciones a levantar antes de aceptar el hito.",
    )

    doc.add_heading("Punch List", level=2)
    add_para(
        doc,
        "A la terminacion de las actividades el Contratista entregara a la "
        "Inspeccion Tecnica un acta de recepcion provisional acompanada de un "
        "punch list que enumere todas las observaciones pendientes, su "
        "responsable y su plazo de cierre comprometido. La recepcion final del "
        "montaje se concedera cuando todos los puntos del punch list esten "
        "cerrados a satisfaccion de la Inspeccion Tecnica y se haya entregado "
        "el dossier as-built completo y aceptado.",
    )


def construir_anexos(doc):
    """Inserta seccion 'ANEXOS' en orientacion apaisada con un plano por anexo."""
    # Cambio de orientacion a apaisada
    doc.add_section()
    section = doc.sections[-1]
    section.orientation = WD_ORIENT.LANDSCAPE
    nuevo_ancho = section.page_height
    nuevo_alto = section.page_width
    section.page_width = nuevo_ancho
    section.page_height = nuevo_alto

    doc.add_heading("ANEXOS", level=1)
    add_para(
        doc,
        "Los planos siguientes se reproducen como anexo de referencia. Las "
        "versiones controladas se rigen por el sistema documental ADASA.",
    )

    # Anexo A
    add_anexo_paginado(
        doc,
        "Anexo A — Plano de Montaje del Conjunto (P22-DWG-06-005-101-0, "
        "version definitiva emitida Apto para Construccion)",
        ["anexo-A-p01.png"],
    )
    doc.add_page_break()

    # Anexo B
    add_anexo_paginado(
        doc,
        "Anexo B — Plano del Estanque de Salmuera (EX-26005-F01)",
        ["anexo-B-p01.png"],
    )
    doc.add_page_break()

    # Anexo C
    add_anexo_paginado(
        doc,
        "Anexo C — Plano de la Bomba de Alimentacion (KSB-AAF-KNCPP11-050+160M)",
        ["anexo-C-p01.png"],
    )
    doc.add_page_break()

    # Anexo D — Formatos de Protocolos (texto-placeholder)
    doc.add_heading(
        "Anexo D — Formatos de Protocolos",
        level=1,
    )
    add_para(
        doc,
        "Los formatos en blanco de los protocolos identificados en la Matriz "
        "de Protocolos se entregan en archivo separado, en formato editable "
        "ADASA, junto con el dossier as-built. Su listado completo aparece en "
        "la Seccion Matriz de Protocolos del cuerpo de la presente "
        "especificacion.",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def crear_documento():
    crear_documento_adasa(
        titulo="ESPECIFICACION TECNICA DE MONTAJE ELECTROMECANICO",
        codigo="P22-ET-06-007-001-0",
        preparado_por="Luis Rivera",
        revisado_por="Luis Rivera",
        aprobado_por="Victor Gutierrez",
        nombre_planta="TALTAL",
        cliente="ADASA",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # Limpiar placeholder del template (idem patron crear_nota_tecnica.py)
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

    # Cuerpo
    construir_seccion_generalidades(doc)
    construir_seccion_suministros(doc)
    construir_seccion_recepcion(doc)
    construir_seccion_bases(doc)
    construir_seccion_estanque(doc)
    construir_seccion_bomba(doc)
    # construir_seccion_pruebas_motor(doc)  # RETIRADO Rev 0 (01-Jun): pruebas
    # electricas del motor fuera del alcance (electricidad e instrumentacion /
    # puesta en marcha). Funcion conservada como referencia, no se emite.
    construir_seccion_protocolos(doc)
    construir_seccion_hse(doc)
    construir_seccion_hitos(doc)

    # Anexos en orientacion apaisada
    construir_anexos(doc)

    # Metadatos limpios (regla global S2.3)
    if METADATA_DISPONIBLE:
        apply_core_properties(
            doc,
            title="Especificacion Tecnica de Montaje Electromecanico - Taltal",
            author="Luis Rivera",
            subject="P22-ET-06-007-001-0",
            keywords="ADASA Taltal Montaje TK-06-001 BH-06-001",
            category="Especificacion Tecnica",
            comments="",
        )

    doc.save(OUTPUT)

    if METADATA_DISPONIBLE:
        fix_app_xml(OUTPUT, application="Microsoft Office Word")

    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    crear_documento()
