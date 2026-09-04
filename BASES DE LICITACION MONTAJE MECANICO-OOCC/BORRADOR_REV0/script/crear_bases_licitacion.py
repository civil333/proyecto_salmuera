#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera Bases de Licitacion Montaje Mecanico + OOCC Modulo Salmuera Taltal Rev 0."""
import os
import sys
from datetime import datetime

# Path absoluto a la skill template-adasa (Synology no soporta symlinks)
sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from docx import Document
from docx.shared import Cm, Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from ejemplo_documento import (
    crear_documento_adasa,
    add_bullet,
    aplicar_arial_12,
)
from table_utils import add_simple_table

BASE = r"C:\SynologyDrive\SynologyDrive\DESAROLLO PROYECTOS CLAUDE\MODULO DE SALMUERA TALTAL"
OUT_DIR = os.path.join(BASE, "BASES DE LICITACION MONTAJE MECANICO-OOCC", "BORRADOR_REV0")
IMG = os.path.join(OUT_DIR, "imagenes")
OUTPUT = os.path.join(OUT_DIR, "BL_MONTAJE_TALTAL_REV0.docx")

TITULO = "Bases de Licitacion - Montaje Mecanico y Obras Civiles - Modulo Segunda Etapa de Salmuera"
CODIGO = "P22-BL-06-000-001-0"


def fijar_idioma(doc, lang="es-CL"):
    """Fija idioma del documento para que Word no marque tildes/n con rojo."""
    style = doc.styles["Normal"]
    rPr = style.element.get_or_add_rPr()
    for lang_el in rPr.findall(qn("w:lang")):
        rPr.remove(lang_el)
    lang_el = OxmlElement("w:lang")
    lang_el.set(qn("w:val"), lang)
    lang_el.set(qn("w:eastAsia"), lang)
    lang_el.set(qn("w:bidi"), lang)
    rPr.append(lang_el)


def add_picture_caption(doc, image_path, caption, width_cm=15.5):
    """Inserta imagen centrada con pie de figura debajo."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(image_path, width=Cm(width_cm))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = cap.add_run(caption)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.italic = True


def add_para(doc, text, bold=False, justify=True):
    p = doc.add_paragraph()
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.bold = bold
    return p


def add_para_bold_lead(doc, lead, rest):
    """Parrafo con primera frase en negrita."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r1 = p.add_run(lead)
    r1.font.name = "Arial"
    r1.font.size = Pt(11)
    r1.bold = True
    r2 = p.add_run(rest)
    r2.font.name = "Arial"
    r2.font.size = Pt(11)
    return p


# ============================================================================
# 1. Crear base ADASA
# ============================================================================
print("[BL] Generando base ADASA...")
crear_documento_adasa(
    titulo=TITULO,
    codigo=CODIGO,
    output_filename=OUTPUT,
    incluir_toc=True,
)

# ============================================================================
# 2. Cargar y poblar
# ============================================================================
print("[BL] Poblando contenido...")
doc = Document(OUTPUT)
fijar_idioma(doc, "es-CL")

# ---- Resumen Ejecutivo ----
doc.add_heading("Resumen Ejecutivo", level=1)
add_para(doc,
    "Aguas Antofagasta S.A. licita el montaje mecanico (mecanica de proceso, piping de "
    "interconexiones, drenajes exteriores, montaje de la bomba de alimentacion BH-06-001) y las "
    "obras civiles completas asociadas al nuevo Modulo de Segunda Etapa de Salmuera de la Planta "
    "Desaladora Taltal. El contrato adjudicado deja la totalidad de la obra civil terminada, todo "
    "el piping de interconexiones instalado hasta tie-ins definidos por el mandante, y la bomba "
    "de alimentacion BH-06-001 montada y alineada sobre su fundacion, en condicion lista para "
    "que en una fase posterior se instale el modulo de osmosis inversa (suministro BW Water) con "
    "su sistema CIP, su conexionado final y la puesta en marcha.")
add_para(doc,
    "El proyecto se desarrolla sobre el recinto operativo de la Planta Desaladora Taltal, en "
    "condicion brownfield, con interfaces a la planta existente de 11 l/s (Modulo 3) para tomar "
    "y devolver salmuera. La modalidad de contratacion es suma alzada. ADASA entrega cubicaciones "
    "completas a partir del Compilado Rev 0 de Ingenieria de Detalle Mecanica y del paquete civil "
    "L&A (en emision). Las cinco ideas que deben quedar grabadas por el oferente:")
add_bullet(doc, "Alcance acotado: mecanica perimetral, piping de interconexiones, drenajes, obra civil completa y montaje de la bomba BH-06-001. No se monta el modulo OI BW Water ni el sistema CIP.")
add_bullet(doc, "Suma alzada con cubicacion entregada: ADASA aporta planos, listas de lineas, listados de materiales, valvulas, equipos e instrumentos. El oferente cotiza por isometria y por tag.")
add_bullet(doc, "Suministros divididos: ADASA aporta soportes (fabricados por tercero), estanque TK-06-001, bomba BH-06-001, valvulas, instrumentacion in-line y todo lo del scope BW Water. El contratista aporta caneria HDPE/PE, accesorios, materiales civiles (hormigon, aridos, acero refuerzo) y pernos quimicos.")
add_bullet(doc, "Limite de bateria explicito: tie-ins documentados con su plano, cota y accion requerida (brida ciega, cap, valvula manual de aislacion o contrabrida).")
add_bullet(doc, "Coordinacion brownfield: las paradas del Modulo 3 existente las agenda ADASA con Aguas Antofagasta. El contratista ejecuta el tie-in dentro de la ventana acordada.")

# ============================================================================
# 1. CONTEXTO Y ALCANCE GENERAL
# ============================================================================
doc.add_heading("Contexto y Alcance General", level=1)

doc.add_heading("Antecedentes del proyecto", level=2)
add_para(doc,
    "La Planta Desaladora Taltal opera actualmente con un modulo de tratamiento de 11 l/s. "
    "Aguas Antofagasta encarga la implementacion de un segundo modulo en paralelo, dedicado a "
    "la segunda etapa de salmuera, que recibe la salmuera de rechazo del modulo existente y la "
    "procesa para incrementar la recuperacion de agua producto. La ingenieria de detalle mecanica "
    "fue desarrollada por Vandoorn Ingenieria en Aguas y se encuentra emitida en revision 0 "
    "(Compilado Rev 0 del paquete P22). La ingenieria civil y de estructuras metalicas esta siendo "
    "desarrollada por L&A Ingenieria y Proyectos sobre el terreno y se incorporara a esta "
    "licitacion una vez recibida en revision 0.")
add_picture_caption(doc,
    os.path.join(IMG, "00_ortofoto_recinto_taltal.png"),
    "Figura 1-1. Vista aerea del recinto Planta Desaladora Taltal (extracto del TR P22-TR-00-010-01-1).")
add_para(doc,
    "El emplazamiento es un recinto costero en Taltal, Region de Antofagasta, con ambiente marino "
    "corrosivo por exposicion directa a brisa salina. Las condiciones del sitio estan descritas en "
    "el apartado de Condiciones Ambientales del proyecto. El nuevo modulo se construye junto al "
    "area operativa del modulo de 11 l/s existente, con tres tie-ins mecanicos que requieren "
    "coordinacion con la operacion de Aguas Antofagasta.")

doc.add_heading("Ubicacion y layout general", level=2)
add_para(doc,
    "El layout del nuevo modulo se compone de tres zonas funcionales: zona del estanque de salmuera "
    "TK-06-001 y bomba de alimentacion BH-06-001, zona del contenedor del modulo OI con su sistema "
    "CIP adyacente, y zona de la fosa de drenajes TK-06-002 con su red de canalizaciones hacia las "
    "camaras existentes del sistema de drenajes.")
add_picture_caption(doc,
    os.path.join(IMG, "08_implantacion_general_compilado.png"),
    "Figura 1-2. Implantacion general del modulo de segunda etapa (P22-DWG-06-005-102).")
add_picture_caption(doc,
    os.path.join(IMG, "03_implantacion_general.png"),
    "Figura 1-3. Plano de canerias de interconexiones - vista de planta general con elementos del Modulo 3 existente identificados (extracto P22-DWG-06-006-101).")
add_para(doc,
    "El elemento 6 del plano de implantacion corresponde al Modulo 3 existente (planta de 11 l/s "
    "actualmente en operacion), del cual se toma la alimentacion de salmuera y al cual retorna la "
    "descarga de drenajes. Los tie-ins con el modulo existente quedan documentados en los Cortes D "
    "y E del plano P22-DWG-06-006-102.")

doc.add_heading("Alcance global de la licitacion", level=2)
add_para(doc, "Comprende tres familias de obras:")
add_bullet(doc, "Obra civil completa: excavaciones y movimiento de tierras, fundaciones de equipos exteriores, fundacion compartida entre el contenedor del modulo OI y el sistema CIP, fosa de drenajes TK-06-002 en hormigon armado, canalizaciones y red de drenajes, pavimentos y terminaciones, cubierta metalica del sistema CIP exterior, anclajes y conexiones a estructura existente.")
add_bullet(doc, "Montaje mecanico y piping: instalacion de la caneria HDPE/PE de interconexiones y drenajes, montaje del estanque TK-06-001 sobre su fundacion (suministro ADASA), instalacion de soportes de caneria (suministro ADASA por tercero), instalacion fisica de valvulas e instrumentacion in-line (suministro ADASA), pruebas hidrostaticas y flushing.")
add_bullet(doc, "Coordinacion con operacion existente: ejecucion de los tie-ins con el Modulo 3 dentro de ventanas de parada agendadas por ADASA.")
add_para(doc,
    "El alcance excluido (modulo OI, sistema CIP completo, bomba BH-06-001) y los limites de "
    "bateria se detallan en el capitulo de Alcance Excluido y Limite de Bateria.")

# ============================================================================
# 2. INFORMACION ADMINISTRATIVA
# ============================================================================
doc.add_heading("Informacion Administrativa", level=1)

doc.add_heading("Convocatoria", level=2)
add_para(doc,
    "La presente licitacion se convoca por invitacion a contratistas precalificados por Aguas "
    "Antofagasta S.A. para la ejecucion del Montaje Mecanico y Obras Civiles del Modulo de "
    "Segunda Etapa de Salmuera de la Planta Desaladora Taltal. Los oferentes deben presentar "
    "oferta economica y tecnica conforme al formato indicado en los Anexos.")

doc.add_heading("Modalidad de contratacion", level=2)
add_para_bold_lead(doc, "Suma Alzada segun Formato de Licitacion (Anexo A9)",
    " con cubicaciones entregadas por el mandante. El oferente completa la planilla del Anexo A9 "
    "con precios unitarios por partida y entrega un precio total cerrado.")
add_bullet(doc, "Partida Piping HDPE/PE (Anexo A9.1): cotizacion por codigo de isometria - una unidad por isometria con todas las hojas H.1, H.2, ... que la componen incluidas en el precio unitario.")
add_bullet(doc, "Cubicacion referencial por familia (Anexo A9.2): vista consolidada del LI Materiales P22-LI-06-006-102 (335 m totales de caneria HDPE PE100 PN10 + accesorios). Sin columna de precio - es referencia para que el oferente valide el desglose de su cotizacion por isometria.")
add_bullet(doc, "Partida Valvulas (Anexo A9.3): instalacion cotizada por TAG. Suministro ADASA; el contratista cotiza unicamente la mano de obra de instalacion.")
add_bullet(doc, "Partida Instrumentos in-line (Anexo A9.4): instalacion cotizada por TAG. Suministro ADASA, instalacion contratista, sin calibracion ni commissioning.")
add_bullet(doc, "Partida Montaje BH-06-001 (Anexo A9.5): cotizacion unica global del montaje de la bomba de alimentacion (anclaje, alineacion bomba-motor, conexion hidraulica, conexionado electrico, pruebas funcionales en vacio). Suministro ADASA del equipo KSB completo.")
add_bullet(doc, "Partida Obras Civiles (Anexo A9.6): itemizada por planos L&A (a emitir como Adenda Tecnica en complemento a estas Bases).")
add_bullet(doc, "Partida Coordinacion e ITO (Anexo A9.7): gastos generales del contratista durante las ventanas de parada del Modulo 3 cotizados como item aparte.")
add_bullet(doc, "Resumen general (Anexo A9.8): subtotal neto + IVA 19% + total con IVA.")
add_para(doc,
    "Las cantidades indicadas en los anexos son referenciales para uniformar la base de "
    "comparacion entre ofertas. En modalidad suma alzada, el riesgo de variacion menor de "
    "cantidades respecto del estado real es del contratista una vez adjudicado el contrato. "
    "Cambios sustantivos de alcance se gestionan via Orden de Cambio formal.")

doc.add_heading("Plazo de construccion", level=2)
add_para(doc,
    "El plazo total de construccion referencial es de 4 meses calendario desde la firma del "
    "contrato, conforme a la modalidad Suma Alzada segun Formato de Licitacion (Anexo A9). El "
    "programa detallado lo aporta el contratista adjudicado en su oferta tecnica conforme a los "
    "hitos criticos enumerados a continuacion.")
add_para_bold_lead(doc, "Hitos criticos referenciales:", "")
add_bullet(doc, "Movilizacion al sitio, cierre perimetral, bodegas y oficinas de obra.")
add_bullet(doc, "Excavaciones y movimiento de tierras conforme a planos L&A.")
add_bullet(doc, "Fundacion del estanque TK-06-001 lista para recepcion del estanque suministrado por ADASA.")
add_bullet(doc, "Fundacion de la bomba BH-06-001 lista, bomba KSB instalada con anclaje M16, alineacion bomba-motor segun procedimiento del fabricante y pruebas funcionales en vacio completadas.")
add_bullet(doc, "Fundacion compartida contenedor del modulo OI + sistema CIP terminada.")
add_bullet(doc, "Fosa de drenajes TK-06-002 terminada e impermeabilizada.")
add_bullet(doc, "Cubierta metalica del sistema CIP terminada.")
add_bullet(doc, "Piping de interconexiones HDPE/PE instalado hasta los tie-ins definidos en la Seccion 4.4.")
add_bullet(doc, "Tie-ins con el Modulo 3 ejecutados dentro de las ventanas de parada agendadas por ADASA (Seccion 7).")
add_bullet(doc, "Pruebas hidrostaticas y flushing completados con protocolos firmados.")
add_bullet(doc, "Recepcion mecanica de la obra.")
add_para(doc,
    "El cronograma detallado y vinculante se acuerda con el contratista adjudicado al inicio "
    "del contrato. La fecha de recepcion mecanica (4 meses desde firma) es contractual y no "
    "negociable salvo modificacion por Orden de Cambio formal.")

doc.add_heading("Condiciones de participacion", level=2)
add_para(doc, "El oferente debe acreditar:")
add_bullet(doc, "Inscripcion vigente en el Registro de Contratistas de Aguas Antofagasta S.A. en las especialidades de obras civiles y montaje mecanico.")
add_bullet(doc, "Experiencia comprobable en al menos dos proyectos de naturaleza equivalente (montaje en planta operativa, piping HDPE/PE, fundaciones de equipos) durante los ultimos cinco anos.")
add_bullet(doc, "Cumplimiento de normativa laboral, previsional, tributaria y de salud y seguridad ocupacional vigente.")
add_bullet(doc, "Sistema de Gestion de Calidad implementado y auditable; deseable certificacion ISO 9001:2015.")
add_bullet(doc, "Sistema de Gestion de Seguridad y Salud Ocupacional implementado; deseable certificacion ISO 45001 o equivalente.")

doc.add_heading("Garantias y seguros", level=2)
add_simple_table(doc, [
    ("Garantia", "Monto", "Vigencia"),
    ("Seriedad de la oferta", "1% del monto ofertado", "90 dias desde apertura"),
    ("Fiel cumplimiento del contrato", "10% del monto adjudicado", "Vigencia contrato + 90 dias"),
    ("Correcta ejecucion y calidad de obra", "5% del monto adjudicado", "12 meses post recepcion"),
    ("Anticipo (si aplica)", "100% del monto del anticipo", "Hasta amortizacion"),
])
add_para(doc,
    "Seguros minimos: responsabilidad civil general por monto a definir segun escala del contrato, "
    "todo riesgo construccion (TRC) por monto del contrato, accidentes personales del personal asignado.")

doc.add_heading("Forma de pago", level=2)
add_para_bold_lead(doc, "Moneda y reajuste: ",
    "Oferta en pesos chilenos (CLP). Reajuste por IPC del INE Chile sobre saldo no pagado, "
    "aplicable a partir del sexto mes desde adjudicacion si la obra excede dicho plazo. "
    "Alternativamente el oferente puede cotizar en UF (Unidad de Fomento), en cuyo caso el "
    "reajuste por IPC no aplica.")
add_para_bold_lead(doc, "IVA: ",
    "19% adicional al precio neto, conforme a la legislacion chilena vigente. La oferta "
    "economica del Anexo A9 distingue subtotal neto + IVA + total con IVA.")
add_para_bold_lead(doc, "Estado de pago: ",
    "mensual contra avance medido en obra, con criterio binario por item terminado:")
add_bullet(doc, "Piping: isometria instalada, probada hidrostaticamente y con protocolo de prueba firmado.")
add_bullet(doc, "Valvulas e instrumentos: TAG instalado, alineado y entregado con tag de identificacion visible.")
add_bullet(doc, "Obra civil: elemento terminado (fundacion hormigonada y curada con planos as-built, fosa impermeabilizada y aprobada por ITO, etc.).")
add_para_bold_lead(doc, "Plazo de pago: ",
    "30 dias corridos desde la aprobacion del estado de pago por el ITO ADASA y la recepcion de "
    "la factura conforme.")
add_para_bold_lead(doc, "Anticipo: ",
    "opcional, hasta 20% del monto adjudicado contra garantia bancaria a la vista por el 100% "
    "del anticipo. Amortizacion proporcional en los estados de pago hasta el 80% del avance.")
add_para_bold_lead(doc, "Retenciones: ",
    "retencion del 10% del estado de pago como garantia adicional de buena ejecucion, devolvible "
    "30 dias post recepcion provisoria. La retencion puede sustituirse por boleta de garantia "
    "bancaria a la vista del mismo monto.")

doc.add_heading("Multas", level=2)
add_bullet(doc, "Atraso en hito intermedio (no critico de ruta): 0,05% del monto del contrato por dia calendario.")
add_bullet(doc, "Atraso en hito critico (tie-in M3, recepcion mecanica): 0,10% del monto del contrato por dia calendario, con tope del 10% del monto del contrato.")
add_bullet(doc, "Incumplimiento de programa de calidad o de prevencion de riesgos: amonestacion escrita inicial; reiteracion configura causal de termino anticipado.")

doc.add_heading("Clausulas generales", level=2)
add_para(doc,
    "Propiedad intelectual de planos as-built: Aguas Antofagasta S.A. Confidencialidad estricta "
    "sobre la informacion del proyecto. Resolucion de controversias por arbitraje en la Camara de "
    "Comercio de Santiago. Causales de termino anticipado conforme a regimen general aplicable a "
    "contratos de construccion.")

doc.add_heading("Criterios de evaluacion de ofertas", level=2)
doc.add_heading("Ponderacion", level=3)
add_simple_table(doc, [
    ("Componente", "Ponderacion"),
    ("Oferta tecnica", "40%"),
    ("Oferta economica", "60%"),
])

doc.add_heading("Sub-criterios de la oferta tecnica (40 puntos)", level=3)
add_simple_table(doc, [
    ("Sub-criterio", "Puntos", "Como se evalua"),
    ("Programa de obra propuesto", "10", "Realismo del cronograma, ruta critica identificada, holguras consistentes con duracion de ventanas de parada del Modulo 3"),
    ("Organigrama y personal clave", "8", "CV del Jefe de Obra (min. 5 anos en obras industriales), Supervisor de Soldadura con calificacion WPS PE100 vigente, Prevencionista de Riesgos experto en planta operativa"),
    ("Plan de calidad", "8", "Procedimientos de electrofusion, pruebas hidrostaticas, recepcion de equipos suministro ADASA, registros de torque"),
    ("Plan de prevencion de riesgos", "8", "Matriz IPER especifica para obra brownfield, procedimiento LOTO, trabajos en altura, soldadura sobre estructura existente (SP-03/SP-09)"),
    ("Experiencia en obras equivalentes", "6", "Certificados de 2+ contratos terminados en ultimos 5 anos (instalacion HDPE/PE PN10 con monto >= 5.000 UF, en planta operativa)"),
])

doc.add_heading("Sub-criterios de la oferta economica (60 puntos)", level=3)
add_para(doc,
    "Formula: Puntaje = 60 x (Precio Minimo Ofertado / Precio del Oferente). La oferta de menor "
    "precio recibe 60 puntos; las demas recibiran puntaje inversamente proporcional.")

doc.add_heading("Formato de presentacion", level=3)
add_simple_table(doc, [
    ("Documento", "Contenido"),
    ("Sobre A - Oferta tecnica", "Programa, organigrama con CV firmados, plan de calidad, plan de prevencion, declaracion de experiencia con certificados, declaracion de aceptacion de las Bases"),
    ("Sobre B - Oferta economica", "Anexo A9 completo (A9.1 a A9.6) en formato Excel + PDF firmado por el representante legal"),
])

doc.add_heading("Calendario referencial", level=3)
add_simple_table(doc, [
    ("Hito", "Plazo (a definir en convocatoria)"),
    ("Publicacion de Bases", "T0"),
    ("Cierre de consultas", "T0 + 10 dias habiles"),
    ("Respuesta a consultas (Adenda)", "T0 + 15 dias habiles"),
    ("Cierre de recepcion de ofertas", "T0 + 25 dias habiles"),
    ("Apertura tecnica", "T0 + 25 dias habiles"),
    ("Evaluacion tecnica", "T0 + 35 dias habiles"),
    ("Apertura economica de oferentes calificados", "T0 + 36 dias habiles"),
    ("Notificacion de adjudicacion", "T0 + 45 dias habiles"),
    ("Vigencia minima de la oferta", "90 dias desde apertura economica"),
])

# ============================================================================
# 3. ALCANCE TECNICO INCLUIDO
# ============================================================================
doc.add_heading("Alcance Tecnico Incluido", level=1)

doc.add_heading("Alcance mecanico", level=2)
add_para(doc, "El contratista ejecuta:")
add_bullet(doc, "Instalacion fisica del estanque TK-06-001 (PRFV vertical 2.600 mm x H 2.570 mm, volumen util 10 m3, peso vacio aproximado 586 kg y peso en operacion con fluido aproximado 12.572 kg con gravedad especifica 1,05 - cargas segun memoria EX-26005-F01 Rev 0 del proveedor Exfibro). El estanque cuenta con orejas de izaje incorporadas segun plano del fabricante. El estanque y sus accesorios los suministra ADASA.")
add_picture_caption(doc,
    os.path.join(IMG, "16_estanque_TK06001_full.png"),
    "Figura 3-1. Estanque de salmuera TK-06-001 - vistas del fabricante Exfibro (plano EX-26005-F01 Rev 0). Vistas: planta superior con orejas de izaje, elevacion con conexiones y placa de identificacion, secuencia de izaje recomendada. Volumen 10 m3, peso vacio 586 kg, peso en operacion 12.572 kg.")
add_bullet(doc, "Montaje completo de la bomba de alimentacion de salmuera BH-06-001 (grupo KSB KNCPP 11-050 5A M en super duplex + motor WEG W22 15 HP / 11 kW 2P 380V / 50Hz IE3 IP55 + acoplamiento NORMEX E-97 + base de acero BD-0502-B; peso seco total 223,5 kg y peso en operacion aproximado 400 kg con fluido). Suministro ADASA - equipo completo segun plano KSB-AAF-KNCPP11-050+160M Rev A. El contratista ejecuta: izaje y posicionamiento sobre la fundacion L&A, anclaje con pernos M16 (suministro contratista; los pernos no vienen incluidos en el suministro KSB), alineacion bomba-motor segun procedimiento del fabricante, conexion hidraulica a la linea de succion SA-HDPE-DN110-PN10-004 via reduccion concentrica DN100x80 (suministro contratista, incluida en el LI Materiales), conexion hidraulica a la linea de descarga SA-HDPE-DN110-PN10-005 via reduccion concentrica DN100x50 e instalacion de las valvulas VM-06-004 (succion), VM-06-005 (descarga) y VR-06-001 (check Duo super duplex en descarga), conexionado electrico hasta caja de paso, y pruebas funcionales en vacio (rodaje sin carga, verificacion de sentido de giro, medicion de vibracion). El commissioning con agua de proceso queda fuera del scope del contratista.")
add_picture_caption(doc,
    os.path.join(IMG, "17_bomba_BH06001_KSB_plano_general.png"),
    "Figura 3-2. Bomba de alimentacion de salmuera BH-06-001 - plano general del fabricante KSB (plano KSB-AAF-KNCPP11-050+160M Rev A). Vistas: elevacion, perfil, inferior con detalle de pernos de anclaje M16; renderizado 3D isometrico; tabla de componentes con pesos individuales (bomba 66 kg + motor WEG 122 kg + base BD-0502-B 32 kg + acoplamiento NORMEX E-97 3,5 kg = 223,5 kg peso seco total). Bridas succion NPS 3 DN80 y descarga NPS 2 DN50.")
add_bullet(doc, "Instalacion de la caneria HDPE/PE PN10 conforme al Cuadernillo de Isometrias del Compilado Rev 0 (planos P22-DWG-06-006-001 a -011, con hojas H.1 a H.7 cuando aplica) hasta los tie-ins documentados en el capitulo de Alcance Excluido.")
add_bullet(doc, "Electrofusion, juntas bridadas y accesorios HDPE/PE segun procedimientos del fabricante y de la especificacion de piping vigente.")
add_bullet(doc, "Instalacion fisica de valvulas suministradas por ADASA (listado completo en P22-LI-06-006-103, LI Valvulas), con torque controlado, gaskets nuevas suministradas por contratista y alineamiento verificado.")
add_bullet(doc, "Instalacion fisica de instrumentacion in-line del Area 06 (listado en P22-LI-06-008-101, LI Instrumentos): caudalimetros, transmisores de presion y nivel, switches de nivel.")
add_bullet(doc, "Instalacion de soportes de caneria suministrados por ADASA (Cuadernillo de Soportes P22-DWG-06-006-107, 11 tipos SP-01 a SP-11). La instalacion incluye la construccion de la obra civil propia de cada soporte (fundacion nueva) o el anclaje a la estructura existente cuando aplique (caso especial de SP-03, SP-09 y SP-10, tratado en el capitulo de Especificaciones Tecnicas Mecanicas).")
add_bullet(doc, "Pruebas hidrostaticas segun ASME B31.3 o norma equivalente acordada, pruebas funcionales en vacio de valvulas e instrumentos, y limpieza interna por flushing con agua potable antes de la entrega.")

doc.add_heading("Alcance civil y obras complementarias", level=2)
add_para(doc, "El contratista ejecuta:")
add_bullet(doc, "Excavaciones y movimiento de tierras conforme al plano P22-DWG-00-001-001 (a emitir L&A).")
add_bullet(doc, "Fundaciones de equipos exteriores del Area 06 (TK-06-001 y BH-06-001) segun P22-DWG-00-002-002.")
add_bullet(doc, "Fundacion compartida entre el contenedor del modulo OI y el sistema CIP (P22-DWG-00-002-003), incluyendo los puntos de anclaje previstos para los equipos del sistema CIP que indique BW Water - los anclajes mismos los suministra ADASA conforme al plano P22-DWG-00-002-005.")
add_bullet(doc, "Fosa de drenajes TK-06-002 en hormigon armado, con capacidad util de 2.000 litros y dimensiones interiores referenciales 1,5 x 1,5 x 1,0 metros (a precisar por el calculo en funcion del dimensionamiento hidraulico). Cota de fondo referida al NPT de los planos mecanicos P22-DWG-06-005-104 y P22-DWG-06-005-105.")
add_bullet(doc, "Cubierta metalica del sistema CIP exterior segun P22-DWG-00-003-001.")
add_bullet(doc, "Canalizaciones, red de drenajes (camaras intermedias) y conexion a la red de drenajes existente segun P22-DWG-00-002-006.")
add_bullet(doc, "Pavimentos y terminaciones en el area del nuevo modulo.")

doc.add_heading("Suministros a cargo del contratista", level=2)
add_simple_table(doc, [
    ("Familia", "Detalle"),
    ("Caneria HDPE / PE PN10", "Toda la caneria de las lineas SA-HDPE-DN63/110, PE-HDPE-DN90 conforme al LI Lineas P22-LI-06-006-101"),
    ("Accesorios HDPE/PE", "Codos, tees, reducciones, bridas, contrabridas, gaskets nuevas para todas las uniones"),
    ("Pernos quimicos y anclajes", "Pernos de fijacion de placas base de soportes a fundaciones nuevas; anclaje quimico tipo HILTI HIT-RE 500 o equivalente cuando aplique"),
    ("Hormigon armado", "H30 / H35 segun especificacion del plano L&A correspondiente; aditivos para ambiente marino corrosivo"),
    ("Aridos, fierro, encofrado", "Materiales de construccion de la obra civil completa"),
    ("Acero estructural", "Para cubierta metalica CIP (perfiles, planchas, conectores) conforme a P22-DWG-00-003-001"),
    ("Soldaduras", "Electrodos, gases y consumibles para uniones soldadas en estructura metalica y en soportes con extension sobre existente"),
    ("Soportes provisorios", "Apuntalamientos y soportes temporales requeridos durante el montaje de canerias y equipos"),
    ("Equipos de izaje", "Gruas, plumas, equipos menores para manipulacion del TK-06-001 (peso vacio 586 kg para izaje al sitio; peso en operacion 12.572 kg para verificacion de fundacion) y traslado de soportes"),
])

doc.add_heading("Suministros entregados por ADASA al contratista en sitio", level=2)
add_para(doc,
    "Aguas Antofagasta entrega al contratista en bodega del recinto, contra inventario firmado, "
    "los siguientes elementos:")
add_simple_table(doc, [
    ("TAG / Familia", "Descripcion", "Plano / Referencia", "Estado al inicio de obra"),
    ("TK-06-001", "Estanque de salmuera PRFV 10 m3 (D 2.600 x H 2.570 mm), peso vacio 586 kg / peso operacion 12.572 kg (g.e. 1,05), proveedor Exfibro", "EX-26005-F01 Rev C", "Disponible en bodega ADASA"),
    ("BH-06-001", "Bomba de alimentacion de salmuera KSB KNCPP 11-050 5A M + motor WEG 15 HP / 11 kW + acoplamiento NORMEX E-97 + base BD-0502-B. Peso seco total 223,5 kg / peso en operacion ~400 kg con fluido. Bridas succion DN80, descarga DN50", "KSB-AAF-KNCPP11-050+160M Rev A", "Disponible. Pernos de anclaje M16 NO incluidos (suministro contratista)"),
    ("Soportes SP-01 a SP-11", "Cuadernillo de soportes, fabricados por tercero (perfil UPE 80 / cuadrado 100 mm / chapas A36)", "P22-DWG-06-006-107", "Disponible en bodega ADASA"),
    ("Valvulas (VM, VR, VE)", "Listado completo en LI Valvulas", "P22-LI-06-006-103", "Disponible en bodega ADASA"),
    ("Instrumentos in-line Area 06", "7 instrumentos: LSH-06-001/003, LSL-06-001, LIT-06-001, PI-06-001, PIT-06-001, FIT-06-001", "P22-LI-06-008-101 + P22-ET-06-008-101", "Disponible en bodega ADASA"),
    ("Scope BW Water", "Modulo OI 2da etapa, sistema CIP completo (TK-09-001, FIL-09-002, BH-09-002, REL-09-001 calentador electrico 16 kW segun TR L&A - el P&ID Vandoorn P22-DWG-06-009-104 indica 20 kW, discrepancia pendiente de reconciliacion con BW Water antes de IFC, TK-09-002 estanque de dispersante, BDS-09-001/002, paneles de control)", "Datasheets BW Water", "No disponible al inicio de obra; el contratista deja la fundacion compartida con la prevision de anclajes segun P22-DWG-00-002-005"),
])

doc.add_heading("Instrumentacion in-line - siete tags", level=3)
add_simple_table(doc, [
    ("TAG", "Tipo", "Servicio", "P&ID", "Rango"),
    ("LSH-06-001", "Interruptor de nivel alto", "Nivel salmuera TK-06-001", "P22-DWG-06-009-102", "-"),
    ("LSL-06-001", "Interruptor de nivel bajo", "Nivel salmuera TK-06-001", "P22-DWG-06-009-102", "-"),
    ("LIT-06-001", "Transmisor ultrasonico de nivel", "Nivel salmuera TK-06-001", "P22-DWG-06-009-102", "0 a 5 m"),
    ("LSH-06-003", "Interruptor de nivel alto", "Nivel fosa drenajes TK-06-002", "P22-DWG-06-009-102", "-"),
    ("PI-06-001", "Manometro", "Descarga bomba BH-06-001", "P22-DWG-06-009-102", "0 a 10 bar"),
    ("PIT-06-001", "Transmisor de presion", "Alimentacion de salmuera", "P22-DWG-06-009-102", "0 a 10 bar"),
    ("FIT-06-001", "Caudalimetro electromagnetico", "Alimentacion de salmuera", "P22-DWG-06-009-102", "0 a 100 m3/h"),
])
add_para(doc,
    "Hojas de datos detalladas: P22-ET-06-008-101. El contratista los recibe en bodega y los "
    "instala in-line sobre la caneria en la posicion que indique la isometria o el plano de "
    "montaje correspondiente. Scope del contratista: instalacion fisica del instrumento "
    "(montaje mecanico in-line, torque controlado en uniones, alineamiento, tag visible) y "
    "amarre del cableado desde la bandeja al instrumento cuando aplique. Fuera de scope: "
    "calibracion, sintonia de lazo, verificacion funcional con simulador, commissioning del "
    "instrumento (lo realiza ADASA / BW Water en fase posterior).")
add_picture_caption(doc,
    os.path.join(IMG, "05_pid_alimentacion_vandoorn.png"),
    "Figura 3-1. P&ID Vandoorn - Alimentacion al modulo de segunda etapa de salmuera (P22-DWG-06-009-102). Los siete instrumentos del Area 06 quedan identificados en este P&ID.")

# ============================================================================
# 4. ALCANCE EXCLUIDO Y LIMITE DE BATERIA
# ============================================================================
doc.add_heading("Alcance Excluido y Limite de Bateria", level=1)
add_para(doc,
    "Este capitulo es el mas importante de las Bases. Define con precision que no debe montar "
    "el contratista y donde termina su responsabilidad mecanica.")

doc.add_heading("Modulo de osmosis inversa de segunda etapa (suministro BW Water)", level=2)
add_para(doc,
    "El modulo OI 2da etapa de salmuera es suministrado e instalado por BW Water como sistema "
    "integrado dentro de un contenedor. El contratista de la presente licitacion deja la "
    "fundacion del contenedor lista (fundacion compartida con CIP) y termina las cuatro lineas "
    "de interconexion en tie-ins definidos por bridas ciegas o caps, posicionadas en las cotas "
    "y ubicaciones que se indican en el Corte A del plano P22-DWG-06-006-102.")
add_picture_caption(doc,
    os.path.join(IMG, "01_corte_a_tieins_modulo.png"),
    "Figura 4-1. Corte A - Tie-ins con el modulo OI: P8-001 entrada salmuera (+8.250 m), P9-001 permeado (+8.593 m), P9-002 permeado fuera de especificacion (+8.593 m), P9-003 salida salmuera (+8.583 m).")
add_picture_caption(doc,
    os.path.join(IMG, "06_pid_oi_tratamiento.png"),
    "Figura 4-2. P&ID Vandoorn - Sistema de tratamiento OI (P22-DWG-06-009-103). El modulo completo encerrado en el rectangulo del contenedor esta fuera del scope de esta licitacion.")

doc.add_heading("Sistema CIP (Clean-In-Place) - suministro BW Water", level=2)
add_para(doc,
    "Todo el sistema CIP (estanque TK-09-001 HDPE 6.800 L, filtro cartucho FIL-09-002, bomba CIP "
    "BH-09-002, calentador electrico REL-09-001 - potencia 16 kW segun TR L&A; el P&ID Vandoorn "
    "P22-DWG-06-009-104 indica 20 kW, discrepancia pendiente de reconciliacion con BW Water antes "
    "de IFC, estanque de dispersante TK-09-002, bombas dosificadoras BDS-09-001/002, paneles de "
    "control local y de calentador) esta fuera del scope de instalacion de esta licitacion. El "
    "sistema se monta sobre la fundacion compartida con el contenedor del modulo OI "
    "(P22-DWG-00-002-003) y queda bajo la cubierta metalica del sistema CIP (P22-DWG-00-003-001), "
    "ambas obras civiles si dentro del scope.")
add_picture_caption(doc,
    os.path.join(IMG, "07_pid_cip.png"),
    "Figura 4-3. P&ID Vandoorn - Sistema CIP (P22-DWG-06-009-104). Suministro e instalacion BW Water.")

doc.add_heading("Tabla maestra de tie-ins (limite de bateria)", level=2)
add_simple_table(doc, [
    ("Tie-in", "Plano de referencia", "Cota (m)", "Linea", "Accion del contratista", "Quien monta el otro lado"),
    ("P8-001 Entrada salmuera al modulo OI", "P22-DWG-06-006-102 Corte A", "+8.250", "SA-HDPE-DN110-PN10-005", "Brida ciega o cap de obturacion", "BW Water (modulo OI 2da etapa)"),
    ("P9-001 Permeado salida", "P22-DWG-06-006-102 Corte A", "+8.593", "SA-HDPE-DN110-PN10-007", "Brida ciega o cap", "BW Water"),
    ("P9-002 Permeado fuera de especificacion", "P22-DWG-06-006-102 Corte A", "+8.593", "Linea fuera de especificacion", "Brida ciega o cap", "BW Water"),
    ("P9-003 Salida salmuera de rechazo", "P22-DWG-06-006-102 Corte A", "+8.583", "PE-HDPE-DN90-PN10-001", "Brida ciega o cap", "BW Water"),
    ("Tie-in 1 (Modulo 3 existente)", "P22-DWG-06-006-102 Corte D", "+6,204", "PE-HDPE-DN160-PN10-001 existente", "Cap o tapon provisional sobre linea existente del M3 - dentro de ventana de parada agendada por ADASA", "ADASA / BW Water posterior"),
    ("Tie-in 3 (Modulo 3 existente)", "P22-DWG-06-006-102 Corte E", "+6,204", "Linea existente del M3", "Empalme con linea existente - dentro de ventana de parada agendada por ADASA", "ADASA agenda"),
    ("Tie-in 6 (Drenajes a fosa nueva)", "P22-DWG-06-006-102 Corte D", "+6,204", "AMF-HDPE-DN160-PN10-002 (nueva); empalme contra AMF-HDPE-DN160-PN10-001 existente del M3", "Empalme de la red de drenajes nueva a la Fosa TK-06-002 (mismo scope contratista). Linea AMF-HDPE-DN160 no figura en el LI Lineas P22-LI-06-006-101 vigente - pendiente actualizacion Vandoorn", "Contratista"),
])
add_para(doc,
    "Las conexiones de succion y descarga de la bomba BH-06-001 dejan de ser tie-ins de limite "
    "de bateria: la bomba esta dentro del scope del contratista (ver Seccion 3.1 y Figura 3-2). "
    "El montaje incluye la conexion hidraulica completa a las lineas SA-HDPE-DN110-PN10-004 "
    "(succion) y SA-HDPE-DN110-PN10-005 (descarga) via las reducciones DN100x80 y DN100x50 del "
    "LI Materiales.")
add_picture_caption(doc,
    os.path.join(IMG, "04_cortes_d_e_tieins_m3.png"),
    "Figura 4-5. Cortes D y E del plano P22-DWG-06-006-102 - tie-ins 1, 3 y 6 con el Modulo 3 existente.")

doc.add_heading("Alcance excluido - resumen consolidado", level=2)
add_para(doc, "El contratista NO ejecuta:")
add_bullet(doc, "Montaje del modulo OI BW Water ni de sus componentes internos (membranas, bombas HP, turbochargers, cartuchos, paneles).")
add_bullet(doc, "Montaje de los equipos del sistema CIP enumerados arriba.")
add_bullet(doc, "Calibracion, sintonia de lazo ni commissioning de la instrumentacion in-line (solo deja instalada fisicamente).")
add_bullet(doc, "Tendido electrico y de control desde la sala electrica hasta los instrumentos (scope de electricidad e instrumentacion, fuera de estas Bases).")
add_bullet(doc, "Llenado del estanque TK-06-001 con salmuera ni operacion con fluido del proceso.")
add_bullet(doc, "Pruebas FAT o SAT de equipos suministro ADASA o BW Water.")
add_bullet(doc, "Commissioning final con agua del proceso.")

# ============================================================================
# 5. ESPECIFICACIONES TECNICAS MECANICAS
# ============================================================================
doc.add_heading("Especificaciones Tecnicas Mecanicas", level=1)

doc.add_heading("Canerias y piping HDPE/PE", level=2)
add_para(doc,
    "Toda la caneria de proceso del nuevo modulo es HDPE PE100 PN10, conforme a la "
    "Especificacion Tecnica de Canerias P22-ET-06-006-001-0 (referenciada como Anexo A1) que "
    "define materiales, dimensionamiento, accesorios, normas de union y ensayos. El listado "
    "completo de lineas y materiales esta en los anexos:")
add_bullet(doc, "P22-ET-06-006-001-0 - ET Canerias (especificacion tecnica vinculante)")
add_bullet(doc, "P22-LI-06-006-101 - LI Lineas (12 lineas identificadas: 9 isometrias)")
add_bullet(doc, "P22-LI-06-006-102 - LI Materiales")
add_bullet(doc, "P22-LI-06-006-103 - LI Valvulas")

doc.add_heading("Cotizacion por isometria", level=3)
add_para(doc,
    "Cada isometria del Cuadernillo de Isometrias (planos P22-DWG-06-006-001 a -011 con sus "
    "hojas H.1 a H.7) corresponde a una linea individual del LI Lineas. El oferente cotiza una "
    "unidad por isometria, con todas las hojas incluidas en el precio unitario. El formato "
    "detallado esta en el Anexo A9.1.")

doc.add_heading("Union de canerias", level=3)
add_para(doc,
    "Electrofusion segun procedimiento del fabricante del polietileno (PE100), con calificacion "
    "previa del soldador (WPQ) y registros de cada electrofusion (parametros de equipo, "
    "temperatura ambiente, hora). Normativa aplicable: ISO 21307 (procedimientos de fusion a tope "
    "y electrofusion para PE) y DVS 2207 (soldadura de termoplasticos), conforme a lo establecido "
    "en P22-ET-06-006-001-0 (ET Canerias). Uniones bridadas con stub-end + brida loose y gaskets "
    "nuevas a torque controlado conforme tabla del fabricante.")

doc.add_heading("Pruebas hidrostaticas", level=3)
add_para(doc,
    "Pruebas hidrostaticas conforme a ASME B31.3 y a los procedimientos definidos en "
    "P22-ET-06-006-001-0 (ET Canerias). Presion de prueba = 1,5 x presion de diseno con duracion "
    "minima de 30 minutos sin caida de presion observable. Protocolo de prueba firmado por "
    "contratista e inspector tecnico ADASA. Las lineas del sistema de drenajes que operan a "
    "presion atmosferica se prueban por estanqueidad por columna de agua.")

doc.add_heading("Flushing previo a entrega", level=3)
add_para(doc,
    "Limpieza interna por flushing con agua potable de todas las lineas instaladas antes de la "
    "entrega, hasta verificar agua limpia a la salida. El protocolo de flushing queda registrado "
    "y firmado. Esto es critico porque la fase posterior incorpora membranas RO sensibles a "
    "particulas.")

doc.add_heading("Valvulas (suministro ADASA / instalacion contratista)", level=2)
add_para(doc,
    "El listado completo de valvulas del Area 06 esta en P22-LI-06-006-103. Todas las valvulas "
    "las suministra ADASA. El contratista las recibe en bodega contra inventario firmado e "
    "instala con torque controlado en uniones bridadas, gaskets nuevas (suministro contratista) "
    "y alineamiento verificado por ITO. Para las valvulas criticas en la descarga de bomba "
    "(VM-06-005, VR-06-001) y en la zona del estanque (VM-06-001, VM-06-002), el alineamiento se "
    "documenta con foto y registro de torque. Las valvulas mariposa wafer son marca KSB serie "
    "ISORIA 10 con accionamiento manual por reductor (gearbox MS/MC); las valvulas de retencion "
    "son tipo Duo Check en acero super duplex 2507. Especificaciones de materiales y "
    "procedimiento de instalacion: P22-ET-06-006-001-0 (ET Canerias).")

doc.add_heading("Pesos referenciales de las valvulas criticas para dimensionar herramientas de montaje", level=3)
add_simple_table(doc, [
    ("TAG", "Tipo", "DN", "Linea", "Peso cuerpo (kg)", "Reductor manual (kg)", "Total operacion (kg)"),
    ("VM-06-001", "Mariposa wafer CL150, fundicion nodular A536, asiento EPDM, accionamiento manual por reductor", "DN100 (4\")", "SA-HDPE-DN110-PN10-001", "3,9", "~8,5 (KSB MS100/MC100)", "~12-13"),
    ("VM-06-002", "Mariposa wafer CL150 (idem)", "DN100 (4\")", "SA-HDPE-DN110-PN10-002", "3,9", "~8,5", "~12-13"),
    ("VM-06-004", "Mariposa wafer CL150 (idem) - succion BH-06-001", "DN100 (4\")", "SA-HDPE-DN110-PN10-004", "3,9", "~8,5", "~12-13"),
    ("VM-06-005", "Mariposa wafer CL150 (idem) - descarga BH-06-001", "DN100 (4\")", "SA-HDPE-DN110-PN10-005", "3,9", "~8,5", "~12-13"),
    ("VR-06-001", "Check Duo wafer CL150, cuerpo/disco super duplex 2507 (A890 GR. 5A), resorte Inconel X-750, asiento EPDM", "DN100 (4\")", "SA-HDPE-DN110-PN10-005", "~7-9 (sin actuador, material mas denso)", "-", "~7-9"),
])
add_para(doc,
    "Pesos extraidos del catalogo KSB ISORIA 10 - folleto 844.1 (Tabla 'Tornilleria y peso para "
    "cuerpo anular wafer Tipo 1', DN100 = 3,9 kg) y catalogo KSB MS/MC Manual Actuators 8508.1 "
    "(MS100 con volante 400-500 mm = 8,5-9,2 kg). El peso final de cada conjunto se confirma con "
    "el datasheet especifico que ADASA entregue en bodega.")
add_para(doc,
    "Las restantes 8 valvulas del LI P22-LI-06-006-103 son de tamanos DN63, DN90 y DN100 (todas "
    "mariposas wafer CL150 + 1 check Duo) y caen en el mismo orden de peso que las criticas: las "
    "DN90 mariposas pesan aproximadamente 8-10 kg con reductor incluido; la DN63 mariposa pesa "
    "aproximadamente 6-7 kg; VR-06-003 (check DN100 super duplex) pesa 7-9 kg; VM-06-009 / "
    "VM-06-010 (mariposas DN100) pesan 12-13 kg igual que las criticas. No hay valvulas de "
    "venteo o drenaje pequenas (DN <= 50) en el listado - todo el conjunto se manipula "
    "manualmente con 1-2 operarios sin grua, pero requiere arneses de izaje y proteccion contra "
    "caidas durante la elevacion al spool de caneria.")

doc.add_heading("Instrumentacion in-line (suministro ADASA / instalacion contratista)", level=2)
add_para(doc,
    "Aplica a los siete instrumentos enumerados en el capitulo de Alcance Tecnico Incluido "
    "(LSH-06-001/003, LSL-06-001, LIT-06-001, PI-06-001, PIT-06-001, FIT-06-001).")
add_para(doc, "Reglas tecnicas de instalacion:")
add_bullet(doc, "Recepcion en bodega ADASA contra inventario firmado por contratista. Verificacion visual de danos de transporte previo a la firma; a partir de la firma, el riesgo de manipulacion es del contratista.")
add_bullet(doc, "Manipulacion con instructivo del fabricante de cada instrumento (instrumentos sensibles a vibracion e impacto, en particular el caudalimetro electromagnetico FIT-06-001 y el transmisor ultrasonico LIT-06-001).")
add_bullet(doc, "Instalacion con torque controlado en uniones bridadas; gaskets nuevas suministradas por contratista; alineamiento verificado.")
add_bullet(doc, "Conexionado electrico hasta caja de paso cuando el alcance llegue a bandeja electrica. No se exige el lazo completo hasta PLC (scope de electricidad e instrumentacion, fuera de la presente licitacion).")
add_bullet(doc, "Entrega con tag de identificacion visible y proteccion de las conexiones de proceso (caps plasticos en las tomas) hasta el llenado del sistema.")
add_para_bold_lead(doc, "Fuera de scope: ",
    "calibracion, sintonia de lazo, verificacion funcional con simulador, commissioning. "
    "Estas actividades las realiza ADASA o BW Water en la fase de puesta en marcha posterior al "
    "termino de la presente licitacion.")

doc.add_heading("Soportes de caneria", level=2)
add_para(doc,
    "Los 11 tipos de soportes (SP-01 a SP-11) estan definidos en el Cuadernillo de Soportes "
    "P22-DWG-06-006-107 (21 paginas). Su tipologia general es de pedestales fabricados con perfil "
    "UPE 80 o perfil cuadrado de 100 mm, con chapa de 6 a 10 mm y acero estructural ASTM A36. "
    "Todos los soportes los fabrica un tercero contratado directamente por ADASA y se entregan al "
    "contratista en bodega.")
add_para(doc, "Responsabilidad del contratista:")
add_bullet(doc, "Recepcion de los soportes en bodega ADASA contra inventario firmado.")
add_bullet(doc, "Construccion de la obra civil propia de cada soporte que requiera fundacion nueva (placa base sobre chapa empotrada en radier o sobre dado de hormigon nuevo, segun indique el plano de cada soporte). El radier o dado se cubica como item civil dentro del Anexo A9.")
add_bullet(doc, "Instalacion georeferenciada de cada soporte con la tolerancia que indique el procedimiento del contratista (referencial: +/- 10 mm en planta y +/- 5 mm en cota).")
add_bullet(doc, "Anclaje al hormigon mediante pernos quimicos (suministro contratista) cuando aplique, o mediante pernos de fijacion sobre chapa empotrada cuando este indicado.")
add_bullet(doc, "Pintura final del soporte conforme a la especificacion de pintura para ambiente marino corrosivo de la zona costera de Taltal (sistema de pintura a confirmar en complemento tecnico de estas Bases).")

doc.add_heading("Soportes con modificacion de estructura existente (caso critico)", level=3)
add_para(doc,
    "Tres soportes requieren intervencion sobre estructura preexistente del Modulo 3 en "
    "operacion. Cada uno tiene implicaciones contractuales que el oferente debe internalizar al "
    "cotizar:")

add_para_bold_lead(doc, "Soporte SP-03 - soldado a soporte existente. ",
    "Hoja 11 del cuadernillo. La nota explicita del plano indica 'EXTREMO A SOLDAR EN SOPORTE "
    "EXISTENTE'. El oferente debe inspeccionar in situ la condicion del soporte existente antes "
    "de presentar oferta. La verificacion estructural de que el soporte existente admite la "
    "carga adicional la entrega ADASA al momento de la apertura de obra; la responsabilidad de "
    "la soldadura conforme a procedimiento WPS calificado y la inspeccion visual del cordon es "
    "del contratista. Acceso al area del soporte existente requiere coordinacion con la "
    "operacion del Modulo 3, gestionada por ADASA.")
add_picture_caption(doc,
    os.path.join(IMG, "11_sp03_detalle_cuadernillo.png"),
    "Figura 5-1. SP-03 - detalle del soporte y nota explicita de soldadura sobre soporte existente del Modulo 3 (P22-DWG-06-006-107 pag. 11).")

add_para_bold_lead(doc, "Soporte SP-09 - soldado a soporte existente. ",
    "Hoja 18 del cuadernillo. Misma situacion que SP-03: requiere acceso a estructura del Modulo "
    "3 operativa y la condicion del soporte base condiciona la ejecucion. La inspeccion previa "
    "del soporte existente y la coordinacion de acceso siguen el mismo procedimiento que SP-03.")
add_picture_caption(doc,
    os.path.join(IMG, "12_sp09_detalle_cuadernillo.png"),
    "Figura 5-2. SP-09 - detalle del soporte y union soldada al soporte existente del Modulo 3 (P22-DWG-06-006-107 pag. 18).")

add_para_bold_lead(doc, "Soporte SP-10 - soldado en terreno. ",
    "Hoja 19 del cuadernillo. La nota indica 'EXTREMO A SOLDAR EN TERRENO'. Requiere preparacion "
    "de la base de terreno con chapa empotrada en radier nuevo o anclaje quimico, segun defina "
    "el plano y el procedimiento aprobado del contratista.")
add_picture_caption(doc,
    os.path.join(IMG, "13_sp10_detalle_cuadernillo.png"),
    "Figura 5-3. SP-10 - detalle del soporte con extremo a soldar en terreno (P22-DWG-06-006-107 pag. 19).")

doc.add_heading("Ubicacion georeferenciada - planos de referencia", level=3)
add_para(doc,
    "La ubicacion en planta y en corte de cada soporte esta documentada en los planos "
    "P22-DWG-06-006-105 (Ubicacion Soportes Planta Interconexiones) y P22-DWG-06-006-106 "
    "(Ubicacion Soportes TK y Bba Salmuera - Cortes).")
add_picture_caption(doc,
    os.path.join(IMG, "14_ubicacion_soportes_planta.png"),
    "Figura 5-4. Plano de ubicacion de soportes en planta - Interconexiones del modulo de segunda etapa (P22-DWG-06-006-105).")
add_picture_caption(doc,
    os.path.join(IMG, "15_ubicacion_soportes_cortes.png"),
    "Figura 5-5. Plano de ubicacion de soportes - Cortes en zona TK-06-001 y BH-06-001 (P22-DWG-06-006-106).")

doc.add_heading("Pruebas y entrega", level=2)
add_para(doc, "Antes de la recepcion mecanica de la obra el contratista debe acreditar:")
add_bullet(doc, "Pruebas hidrostaticas de todas las lineas nuevas, con protocolos firmados por isometria.")
add_bullet(doc, "Pruebas funcionales en vacio: apertura y cierre manual de cada valvula instalada, verificacion visual del posicionamiento de cada instrumento, verificacion de alineamientos de caneria, pruebas de rodaje en vacio de la bomba BH-06-001 (verificacion de sentido de giro, medicion de vibracion conforme a ISO 10816) y verificacion de las contrabridas dejadas listas para acople posterior del modulo OI.")
add_bullet(doc, "Flushing con agua potable de todas las lineas nuevas, con registro de turbidez del agua a la salida.")
add_bullet(doc, "Planos as-built firmados del piping ejecutado, con anotacion de cualquier desviacion menor respecto del Compilado Rev 0.")
add_bullet(doc, "Dossier de calidad consolidado: WPQ y WPS de soldadores, protocolos de electrofusion con parametros registrados, inventarios firmados de recepcion de equipos suministro ADASA, registros de torque de uniones bridadas criticas.")

# ============================================================================
# 6. ESPECIFICACIONES TECNICAS CIVILES
# ============================================================================
doc.add_heading("Especificaciones Tecnicas Civiles", level=1)
add_para(doc,
    "Las obras civiles del proyecto se ejecutan conforme a los criterios de diseno consolidados "
    "en el TR P22-TR-00-010-01-1 de L&A Ingenieria y Proyectos (referenciado como Anexo A6). El "
    "detalle constructivo de cada elemento (excavaciones, fundaciones, fosa, anclajes, "
    "canalizaciones, cubierta metalica) se entregara en los planos L&A Rev 0 que se incorporaran "
    "como Adenda Tecnica a estas Bases. Las especificaciones siguientes son vinculantes para la "
    "cotizacion suma alzada y prevalecen sobre cualquier informacion referencial del Compilado "
    "Mecanico Vandoorn cuando exista divergencia.")

doc.add_heading("Normativa aplicable y condiciones de sitio", level=2)
add_simple_table(doc, [
    ("Aspecto", "Norma / Valor de diseno"),
    ("Diseno sismico estructuras", "NCh 2369:2025 - Zona Sismica 3 (costa Region de Antofagasta)"),
    ("Diseno hormigon armado", "NCh 430:2008 / ACI 318-19"),
    ("Calidad del hormigon", "G-25 (NCh 170:2016), relacion a/c <= 0,50, cemento >= 340 kg/m3"),
    ("Acero de refuerzo", "A630-420H (NCh 204)"),
    ("Fundaciones equipos dinamicos", "ACI 351.3R - masa fundacion / masa equipo >= 3 para BH-06-001"),
    ("Proteccion anticorrosiva", "ISO 12944 categoria C5-M Alta (ambiente marino costero); clase de exposicion NCh 170 M2/C4"),
    ("Recubrimientos de armadura", "50 mm elementos expuestos / 70 mm en contacto con terreno"),
    ("Capacidad admisible del suelo", "1,0 kg/cm2 (100 kPa) referencial; verificar con el Informe Sismico LNS-ADASA-INF-040 Rev 0"),
    ("Levantamiento topografico", "Levantamiento DIO Abril 2026 (antecedente del proyecto)"),
])

doc.add_heading("Planos civiles L&A - Adenda Tecnica", level=2)
add_para(doc,
    "Los siguientes planos seran emitidos por L&A Ingenieria y Proyectos como Adenda Tecnica:")
add_simple_table(doc, [
    ("Codigo del plano", "Descripcion", "Subseccion de estas Bases"),
    ("P22-DWG-00-001-001", "Excavaciones y movimiento de tierras - planta general y cortes", "Excavaciones"),
    ("P22-DWG-00-002-001", "Implantacion general OOCC - planta georeferenciada con coordenadas", "Cabecera"),
    ("P22-DWG-00-002-002", "Fundaciones equipos exteriores Area 06 (TK-06-001, BH-06-001)", "Fundaciones equipos"),
    ("P22-DWG-00-002-003", "Fundacion compartida contenedor + sistema CIP", "Fundacion compartida"),
    ("P22-DWG-00-002-004", "Fosa de drenajes TK-06-002 - planta, cortes, armaduras e impermeabilizacion", "Fosa de drenajes"),
    ("P22-DWG-00-002-005", "Detalles de anclaje y conexiones - incluye prevision de pernos quimicos zona CIP", "Detalles de anclaje"),
    ("P22-DWG-00-002-006", "Canalizaciones y red de drenajes - L1 planta general; L2 camaras CD-06-001/002/003; L3 perfil longitudinal", "Canalizaciones"),
    ("P22-DWG-00-003-001", "Cubierta metalica sistema CIP - planta, elevaciones, cortes y detalles de conexion", "Cubierta metalica CIP"),
])

doc.add_heading("Excavaciones y movimiento de tierras", level=2)
add_para(doc,
    "Excavacion segun las cotas y profundidades del plano P22-DWG-00-001-001. Manejo del material "
    "excavado conforme al procedimiento ambiental del proyecto. Conformacion de subrasante para "
    "fundaciones y radieres.")

doc.add_heading("Fundaciones de equipos exteriores", level=2)
add_para(doc,
    "Fundaciones de los equipos suministrados por ADASA (TK-06-001 y BH-06-001) segun "
    "P22-DWG-00-002-002. Las cargas, dimensiones y requerimientos de anclaje estan indicados en "
    "la hoja de datos del proveedor de cada equipo, referenciadas en el TR L&A:")
add_bullet(doc, "TK-06-001: estanque vertical PRFV de 10 m3 (D 2.600 x H 2.570 mm), peso vacio aproximado 586 kg y peso en operacion con fluido 12.572 kg (gravedad especifica 1,05). Memoria de calculo Exfibro EX-26005-F01 Rev C, pagina 18: 8 pernos de anclaje de 1\" con B.C.D. D 2.755 mm, fuerzas sismicas Ex/Ey +/-4.617 kg y momentos Mx/My +/-431.846 kg.cm.")
add_bullet(doc, "BH-06-001: bomba centrifuga horizontal KSB modelo KNCPP 11/050+160M, 11 kW, 400 kg, en operacion a 11 kW. Diseno dinamico que considera vibraciones generadas por el equipo rotatorio conforme a criterios de ACI 351. Manual de la bomba KSB-AAF-KNCPP11-050+160M Rev A.")

doc.add_heading("Fundacion compartida contenedor + sistema CIP", level=2)
add_para(doc,
    "Sin perjuicio de que el modulo OI y los equipos del CIP estan adyacentes y se disena una "
    "fundacion unica, los puntos de anclaje de los equipos del sistema CIP estan definidos como "
    "detalles aparte en el plano P22-DWG-00-002-005. La fundacion debe permitir la instalacion "
    "posterior por BW Water de los equipos internos del modulo OI y del sistema CIP. El "
    "contenedor de 40 ft HC (dimensiones 12.192 x 2.438 x 2.896 mm) esta modificado con cuatro "
    "plinths longitudinales de 2,6 x 0,3 x 0,4 m bajo las vigas del contenedor. Los plinths bajo "
    "equipos CIP indicados en el mismo plano son: 1,0 x 0,4 x 0,3 m (skid mixer), 1,8 x 2,1 x 0,3 m "
    "(filtro cartucho, bomba HP, calentador, panel) y 2,5 x 2,5 x 0,3 m (estanque CIP). Los pesos "
    "de operacion a considerar en el dimensionamiento son los siguientes:")
add_simple_table(doc, [
    ("TAG / Equipo", "Descripcion", "Peso operacion (kg)"),
    ("Contenedor RO", "Modulo RO 40 ft HC modificado con equipos internos", "~14.934"),
    ("TK-09-001", "Estanque CIP HDPE 6.800 L", "10.470"),
    ("FIL-09-002", "Filtro cartucho CIP", "267,6"),
    ("BH-09-002", "Bomba CIP", "180"),
    ("REL-09-001", "Calentador electrico CIP (16 kW segun TR L&A; 20 kW segun P&ID Vandoorn - reconciliar antes de IFC)", "25"),
    ("TK-09-002", "Estanque de dispersante", "490"),
    ("BDS-09-001/002", "Bombas dosificacion de dispersante", "57,4"),
    ("Panel control local", "Panel de control local", "350"),
    ("Panel control calentador", "Panel de control calentador", "50"),
])
add_para(doc,
    "Los pesos estan tomados del plano BW Water P22-DWG-09-005-001 Rev A - Civil and Loading "
    "Layout. El contenedor de 40 ft HC esta modificado con plinths longitudinales definidos en "
    "el plano BW Water referenciado. Los puntos de anclaje preinstalados los coordina ADASA con "
    "BW Water antes de la emision de la Rev 0 del plano L&A.")

doc.add_heading("Fosa de drenajes TK-06-002", level=2)
add_para(doc,
    "Fosa de hormigon armado con capacidad util de 2.000 litros y dimensiones interiores "
    "referenciales 1,5 x 1,5 x 1,0 metros (a precisar por el calculo de L&A en funcion del "
    "dimensionamiento hidraulico). Cota de fondo referida al NPT de los planos mecanicos "
    "P22-DWG-06-005-104 (Pl. Drenajes) y P22-DWG-06-005-105 (Pl. Montaje Fosa de Drenajes). La "
    "evacuacion de la fosa por gravedad se desarrolla a traves de la linea SA-CPVC-DN200-PN10-001, "
    "definida en los planos de piping P22-DWG-06-006-103 (planta) y P22-DWG-06-006-104 (cortes y "
    "detalles); el alcance no incluye la bomba sumergible de la fosa. El caudal de diseno para "
    "el dimensionamiento hidraulico deriva de los drenajes de los equipos listados en el plano "
    "P22-DWG-09-005-001 Rev A de BW Water y en los planos de piping Vandoorn.")
add_picture_caption(doc,
    os.path.join(IMG, "09_drenajes_mecanico.png"),
    "Figura 6-1. Plano mecanico de drenajes (P22-DWG-06-005-104) - caudales y trazado de la red.")
add_picture_caption(doc,
    os.path.join(IMG, "10_fosa_drenajes_mecanico.png"),
    "Figura 6-2. Plano de montaje de la fosa de drenajes TK-06-002 (P22-DWG-06-005-105) - referencia mecanica para el dimensionamiento hidromecanico.")

doc.add_heading("Detalles de anclaje y conexiones", level=2)
add_para(doc,
    "Pernos quimicos post-instalados para los equipos CIP (suministro contratista, anclaje quimico "
    "con homologacion ETA tipo HILTI HIT-RE 500 o equivalente aprobado por ITO ADASA), conformes "
    "a ACI 355.4 Calificacion de Anclajes Adhesivos Post-Instalados, detallados en "
    "P22-DWG-00-002-005. Conexiones entre placas base y hormigon conforme al detalle de cada "
    "plano. La fundacion debe disenarse con armaduras y recubrimientos que permitan la "
    "instalacion posterior de los pernos quimicos. Los pernos quimicos para soportes de tuberias "
    "y bandejas portacables del sistema CIP estan dentro del alcance del contratista (la "
    "soportacion CIP queda fuera del alcance del consultor L&A segun TR §2.2).")

doc.add_heading("Canalizaciones y red de drenajes", level=2)
add_para(doc,
    "Red de drenajes desde los distintos puntos de captacion hasta la fosa TK-06-002 y desde la "
    "fosa hacia la camara existente del sistema de drenajes del recinto. Camaras intermedias de "
    "hormigon prefabricado o vaciado in situ segun defina L&A. Tendido de ductos subterraneos.")

doc.add_heading("Cubierta metalica del sistema CIP", level=2)
add_para(doc,
    "Cubierta metalica que protege el sistema CIP del ambiente marino corrosivo, segun "
    "P22-DWG-00-003-001. Estructura de perfiles laminados de acero ASTM A36 (o equivalente "
    "nacional), planchas de cubierta y conexion a la fundacion compartida CIP. Diseno sismico "
    "conforme a NCh 2369:2025 Zona 3.")
add_para_bold_lead(doc, "Sistema de proteccion anticorrosiva (ISO 12944 categoria C5-M Alta):", "")
add_simple_table(doc, [
    ("Capa", "Espesor seco", "Material"),
    ("Preparacion superficial", "-", "Granallado a metal casi blanco SSPC-SP10 / Sa 2.5 (ISO 8501-1)"),
    ("Primaria", "80 um", "Zinc-rico inorganico o epoxico rico en zinc"),
    ("Intermedia", "200 um", "Epoxico de altos solidos"),
    ("Terminacion", "75 um", "Poliuretano alifatico"),
    ("Espesor total", "355 um DFT", "Color final RAL 5012 (azul claro)"),
])
add_para(doc,
    "Aplicacion segun ficha tecnica del fabricante; ITO ADASA verifica espesor con medidor "
    "electronico (minimo 5 lecturas por sector). Retoques en obra siguen el mismo esquema.")

# ============================================================================
# 7. COORDINACION CON OPERACION DEL MODULO 3
# ============================================================================
doc.add_heading("Coordinacion con Operacion del Modulo 3", level=1)
add_para(doc,
    "La interconexion con la planta existente de 11 l/s (Modulo 3) requiere ventanas de parada "
    "para ejecutar los tie-ins 1 y 3 sobre lineas que conducen salmuera en operacion. La "
    "coordinacion con el operador (Aguas Antofagasta S.A.) la gestiona ADASA. El contratista "
    "ejecuta el tie-in dentro de la ventana acordada con un equipo de trabajo dimensionado y un "
    "procedimiento previamente revisado y aprobado.")

doc.add_heading("Procedimiento de tie-in", level=2)
add_bullet(doc, "Aviso anticipado: ADASA notifica al contratista la ventana de parada con un minimo de diez dias habiles de anticipacion.")
add_bullet(doc, "Revision de procedimiento: el contratista presenta el procedimiento de tie-in (HAZOP / Analisis de Riesgos / secuencia de actividades / lista de personal y herramientas) con un minimo de cinco dias habiles antes de la ventana. ADASA revisa y aprueba previo a la apertura del permiso de trabajo.")
add_bullet(doc, "Ejecucion dentro de la ventana: la operacion del Modulo 3 entrega la linea aislada, drenada y verificada por permiso de trabajo en planta operativa. El contratista ejecuta el corte, el empalme y la prueba de estanqueidad del nuevo tramo conectado.")
add_bullet(doc, "Entrega de la linea operativa: al termino de la ventana, el contratista entrega la linea probada y lista para repuesta en servicio. La reposicion de servicio la realiza la operacion de Aguas Antofagasta.")

doc.add_heading("Permisos de trabajo en planta operativa", level=2)
add_para(doc,
    "Todo el personal del contratista que ingrese al area del Modulo 3 debe contar con la "
    "induccion de seguridad del recinto vigente y portar el permiso de trabajo emitido por la "
    "operacion de Aguas Antofagasta. El supervisor de obra del contratista es el responsable de "
    "gestionar los permisos diarios y de cumplir los protocolos de aislamiento (LOTO), uso de "
    "elementos de proteccion personal especificos de planta operativa y bloqueo electrico cuando "
    "aplique.")

doc.add_heading("Tie-ins con el Modulo 3 (resumen)", level=2)
add_para(doc,
    "Los tie-ins 1 y 3 (Cortes D y E del plano P22-DWG-06-006-102) son los dos puntos que "
    "requieren intervencion sobre linea en operacion. El tie-in 6 es interno al alcance del "
    "contratista (drenajes nuevos a la fosa nueva) y no requiere coordinacion con la operacion.")

# ============================================================================
# 8. PROGRAMA REFERENCIAL DE OBRA
# ============================================================================
doc.add_heading("Programa Referencial de Obra", level=1)
add_para(doc,
    "Plazo total de construccion: 4 meses calendario desde la firma del contrato (ver Seccion 2.3). "
    "El programa detallado lo presenta el contratista adjudicado en su oferta tecnica conforme al "
    "Anexo A9 (Formato de Licitacion) y se ajusta al inicio del contrato considerando los hitos "
    "criticos siguientes:")
add_bullet(doc, "Recepcion en bodega de los suministros ADASA disponibles al inicio (TK-06-001, soportes, valvulas, instrumentos).")
add_bullet(doc, "Excavacion y fundaciones de equipos exteriores listas para recepcion del TK-06-001 y montaje de la bomba BH-06-001 sobre su fundacion, con alineacion bomba-motor y conexion hidraulica DN80/DN50 via reducciones HDPE.")
add_bullet(doc, "Fosa de drenajes TK-06-002 terminada e impermeabilizada.")
add_bullet(doc, "Fundacion compartida contenedor + sistema CIP y cubierta metalica del sistema CIP terminadas.")
add_bullet(doc, "Piping de interconexiones HDPE/PE instalado, probado hidrostaticamente y con flushing realizado hasta los tie-ins definidos en la Seccion 4.4.")
add_bullet(doc, "Tie-ins 1 y 3 con el Modulo 3 ejecutados dentro de las ventanas de parada agendadas por ADASA (Seccion 7).")
add_bullet(doc, "Recepcion mecanica de la obra dentro del plazo contractual de 4 meses.")
add_para(doc, "La fecha de recepcion mecanica es contractual y no negociable salvo Orden de Cambio formal.")

# ============================================================================
# 9. ANEXOS
# ============================================================================
doc.add_heading("Anexos", level=1)
add_simple_table(doc, [
    ("Anexo", "Contenido"),
    ("A1", "Listado completo de planos del Compilado Rev 0 (mecanica, instrumentacion, P&IDs, isometrias, ET de Canerias)"),
    ("A2", "Listado de planos esperados de L&A (8 planos civiles del TR P22-TR-00-010-01-1)"),
    ("A3", "Cuadernillo de Soportes P22-DWG-06-006-107 - referencia + tabla resumen con SP-03, SP-09 y SP-10"),
    ("A6", "TR Ingenieria Civil L&A Rev 1 (P22-TR-00-010-01-1) - referencia + tabla de contenido"),
    ("A8", "Listado consolidado de suministros ADASA con TAG y plano de referencia"),
    ("A9", "Formato de Licitacion (planilla de oferta economica): A9.1 piping por isometria, A9.2 cubicacion referencial por familia (335 m HDPE + accesorios), A9.3 valvulas por TAG, A9.4 instrumentos por TAG, A9.5 montaje BH-06-001, A9.6 obras civiles, A9.7 coordinacion e ITO, A9.8 resumen con IVA"),
    ("A10", "Bases administrativas - formato detallado de Aguas Antofagasta S.A."),
    ("A11", "Procedimiento de permisos de trabajo en planta operativa (Modulo 3)"),
])
add_para(doc,
    "Nota: Anexos A4, A5 y A7 omitidos. Los P&IDs Vandoorn, los planos de montaje y cortes de "
    "canerias y la ortofoto del recinto ya estan incrustados como Figuras dentro del cuerpo del "
    "documento (capitulos 1, 3, 4, 5 y 6).")

doc.add_heading("Anexo A1 - Listado de planos del Compilado Rev 0", level=2)
add_simple_table(doc, [
    ("Carpeta", "Plano", "Descripcion"),
    ("00_GENERAL", "P22-LI-06-000-101-0", "Listado de entregables"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-101-0", "PFD Modulo Segunda Etapa Salmuera"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-102-0", "P&ID Alimentacion"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-103-0", "P&ID OI Sistema de Tratamiento Salmuera"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-104-0", "P&ID CIP"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-105-0", "P&ID Reactivos"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-ET-06-008-101-0", "Hojas de Datos de Instrumentos"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-IT-06-008-101-0", "Logica de control"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-LI-06-008-101-0", "Listado de Instrumentos"),
    ("02_MECANICA", "P22-DWG-06-005-101-0", "Pl. Montaje TK Salmuera y Bba Alimentacion"),
    ("02_MECANICA", "P22-DWG-06-005-102-0", "Pl. Implantacion General"),
    ("02_MECANICA", "P22-DWG-06-005-103-0", "Pl. Montaje Modulo Desalacion"),
    ("02_MECANICA", "P22-DWG-06-005-104-0", "Pl. Drenajes"),
    ("02_MECANICA", "P22-DWG-06-005-105-0", "Pl. Montaje Fosa de Drenajes"),
    ("02_MECANICA", "P22-LI-06-005-101-0", "Listado de Equipos"),
    ("03_CANERIAS", "P22-DWG-06-006-101-0", "Pl. Canerias Interconexiones - Planta"),
    ("03_CANERIAS", "P22-DWG-06-006-102-0", "Pl. Canerias Interconexiones - Cortes y Detalles"),
    ("03_CANERIAS", "P22-DWG-06-006-103-0", "Pl. Canerias TK y Bba Salmuera - Planta"),
    ("03_CANERIAS", "P22-DWG-06-006-104-0", "Pl. Canerias TK y Bba Salmuera - Cortes y Detalles"),
    ("03_CANERIAS", "P22-DWG-06-006-105-0", "Pl. Ubicacion Soportes Planta Interconexiones"),
    ("03_CANERIAS", "P22-DWG-06-006-106-0", "Pl. Ubicacion Soportes TK y Bba Salmuera - Cortes"),
    ("03_CANERIAS", "P22-DWG-06-006-107-0", "Cuadernillo de Soportes (21 paginas)"),
    ("03_CANERIAS", "P22-DWG-06-006-001 a -011", "Isometrias de lineas HDPE/PE (9 isometrias con hojas H.1 a H.7)"),
    ("03_CANERIAS", "P22-ET-06-006-001-0", "ET Canerias - Especificacion Tecnica vinculante: materiales HDPE PE100 PN10, normas ASME B31.3, ISO 21307, DVS 2207, electrofusion, pruebas hidrostaticas, tablas de espesores y accesorios (14 paginas)"),
    ("03_CANERIAS", "P22-LI-06-006-101-0", "Listado de Lineas"),
    ("03_CANERIAS", "P22-LI-06-006-102-0", "Listado de Materiales"),
    ("03_CANERIAS", "P22-LI-06-006-103-0", "Listado de Valvulas"),
    ("04_MODELO", "Maqueta Gral.nwd", "Modelo 3D Navisworks general del proyecto"),
])

# ----------------- Anexo A9 -----------------
# ----------------- Anexo A2 -----------------
doc.add_heading("Anexo A2 - Listado de planos civiles esperados de L&A", level=2)
add_para(doc,
    "L&A Ingenieria y Proyectos entregara a ADASA los planos civiles que se listan a continuacion "
    "como parte del paquete que se incorporara a estas Bases como Adenda Tecnica al momento de la "
    "adjudicacion del contrato. El adjudicatario los incorpora a su programa de obra dentro de "
    "las primeras dos semanas desde la firma del contrato.")
add_simple_table(doc, [
    ("Codigo del plano", "Descripcion", "Seccion de las Bases que alimenta"),
    ("P22-DWG-00-001-001", "Excavaciones y movimiento de tierras - planta general y cortes", "6.2"),
    ("P22-DWG-00-002-001", "Implantacion general OOCC - planta georeferenciada con coordenadas", "6 cabecera"),
    ("P22-DWG-00-002-002", "Fundaciones equipos exteriores Area 06 (TK-06-001, BH-06-001)", "6.3"),
    ("P22-DWG-00-002-003", "Fundacion compartida contenedor + sistema CIP", "6.4"),
    ("P22-DWG-00-002-004", "Fosa de drenajes TK-06-002 - planta, cortes, armaduras e impermeabilizacion", "6.5"),
    ("P22-DWG-00-002-005", "Detalles de anclaje y conexiones - incluye prevision de pernos quimicos zona CIP", "6.6"),
    ("P22-DWG-00-002-006", "Canalizaciones y red de drenajes - L1 planta general; L2 camaras CD-06-001/002/003; L3 perfil longitudinal", "6.7"),
    ("P22-DWG-00-003-001", "Cubierta metalica sistema CIP - planta, elevaciones, cortes y detalles de conexion", "6.8"),
])

# ----------------- Anexo A3 -----------------
doc.add_heading("Anexo A3 - Cuadernillo de Soportes", level=2)
add_para(doc,
    "El Cuadernillo de Soportes P22-DWG-06-006-107 (21 paginas) se entrega como archivo digital "
    "adjunto a estas Bases. Contiene la geometria detallada, perfiles, chapas, soldaduras y "
    "anclajes de los 11 tipos de soportes que fabrica el tercero contratado por ADASA. La tabla "
    "siguiente resume los 11 tipos para que el oferente identifique los tres casos criticos que "
    "requieren intervencion sobre estructura existente del Modulo 3 operativo (marcados con asterisco).")
add_simple_table(doc, [
    ("TAG", "Linea servida", "Pagina del cuadernillo", "Tipo de fundacion / instalacion"),
    ("SP-01", "Caneria salmuera principal", "1-4", "Pedestal nuevo con placa base sobre dado de hormigon"),
    ("SP-02", "Caneria salmuera principal", "5-7", "Pedestal nuevo con placa base sobre dado de hormigon"),
    ("SP-03 *", "Caneria salmuera D3\"", "11", "Extremo a soldar en soporte existente del Modulo 3 - ver Seccion 5.4.1"),
    ("SP-04", "Caneria salmuera", "12-13", "Pedestal nuevo"),
    ("SP-05", "Caneria salmuera", "14", "Pedestal nuevo"),
    ("SP-06", "Caneria salmuera", "15", "Pedestal nuevo"),
    ("SP-07", "Caneria salmuera", "16", "Pedestal nuevo"),
    ("SP-08", "Caneria salmuera", "17", "Pedestal nuevo"),
    ("SP-09 *", "Caneria salmuera D3\"", "18", "Soldado a soporte existente del Modulo 3 - ver Seccion 5.4.1"),
    ("SP-10 *", "Caneria salmuera D1\"", "19", "Extremo a soldar en terreno - chapa empotrada en radier nuevo o anclaje quimico - ver Seccion 5.4.1"),
    ("SP-11", "Caneria salmuera", "20-21", "Pedestal nuevo"),
])
add_para(doc,
    "Tipologia general: 91% pedestales con perfil UPE 80 o cuadrado 100 mm, chapas 6-10 mm, acero "
    "estructural ASTM A36 (o equivalente nacional). Pintura sistema marino C5-M (ver Seccion 6.8).")

# ----------------- Anexo A6 -----------------
doc.add_heading("Anexo A6 - TR Ingenieria Civil L&A", level=2)
add_para(doc,
    "El Terminos de Referencia P22-TR-00-010-01-1 (Ingenieria OOCC Modulo Taltal) Rev 1 "
    "(24 paginas) emitido el 24-Abr-2026 se entrega como archivo digital adjunto a estas Bases. "
    "Es el documento base contractual del paquete civil - establece los criterios de diseno, "
    "alcance de obra, antecedentes del sitio y entregables de L&A Ingenieria y Proyectos. La "
    "tabla siguiente lista su estructura para orientar al oferente.")
add_simple_table(doc, [
    ("Capitulo", "Contenido"),
    ("1", "Introduccion - descripcion del proyecto, alcance de la consultoria civil"),
    ("2", "Alcance de la Consultoria - ingenieria de detalle obras civiles y estructuras metalicas"),
    ("2.1", "Alcance Ingenieria de Detalle de Obras Civiles (fundaciones, fosa drenajes, canalizaciones, pavimentos)"),
    ("2.2", "Alcance Ingenieria de Detalle de Estructuras Metalicas (cubierta metalica sistema CIP)"),
    ("2.3", "Exclusiones del alcance"),
    ("3", "Criterios de Diseno - normativa, condiciones de sitio, hormigon, estructuras metalicas"),
    ("3.1", "Normativa y codigos aplicables"),
    ("3.2", "Condiciones sismicas - NCh 2369:2025 Zona 3"),
    ("3.3", "Criterios de diseno de obras civiles (capacidad suelo, recubrimientos, hormigon G-25, ACI 351 BH-06-001)"),
    ("3.4", "Criterios de diseno de estructuras metalicas (sistema pintura 355 um RAL 5012)"),
    ("3.5", "Condiciones ambientales del sitio (ISO 12944 C5-M, NCh 170 M2/C4)"),
    ("4", "Desarrollo de Implantacion del Proyecto (layout general, equipos exteriores, modulo RO, equipos CIP, interferencias, banco ductos, modelo 3D)"),
    ("5", "Antecedentes (planos sitio, topograficos, mecanicos, piping, equipos, planos BW Water, modelo 3D Inv.)"),
    ("6", "Entregables por parte del Consultor (memorias de calculo, planos, especificaciones, cubicaciones y presupuesto)"),
    ("7", "Formato de documentos y planos"),
    ("8", "Plazos de ejecucion del consultor"),
    ("9", "Condiciones comerciales y contractuales"),
    ("10", "Matriz de responsabilidades (RACI)"),
    ("11", "Comunicacion y estados de avance"),
])

# ----------------- Anexo A8 -----------------
doc.add_heading("Anexo A8 - Listado consolidado de suministros ADASA", level=2)
add_para(doc,
    "ADASA entrega al contratista los siguientes elementos en bodega del recinto contra inventario "
    "firmado. La tabla consolida la informacion dispersa en las secciones 3.4, 5.2 y 5.4 del "
    "cuerpo del documento para facilitar al oferente la identificacion de que materiales NO debe "
    "cotizar como suministro propio.")
add_simple_table(doc, [
    ("TAG / Familia", "Descripcion", "Plano / Datasheet", "Estado al inicio de obra", "Seccion"),
    ("TK-06-001", "Estanque salmuera PRFV 10 m3 (D2.600 x H2.570 mm), peso vacio 586 kg / operacion 12.572 kg (g.e. 1,05), proveedor Exfibro", "EX-26005-F01 Rev 0", "Disponible", "3.1, 3.4, Fig 3-1"),
    ("BH-06-001", "Bomba alimentacion salmuera KSB KNCPP 11-050 5A M + motor WEG 15 HP / 11 kW + acople NORMEX E-97 + base BD-0502-B. Peso seco 223,5 kg / operacion ~400 kg con fluido. Bridas DN80/DN50", "KSB-AAF-KNCPP11-050+160M Rev A", "Disponible. Pernos M16 NO incluidos (contratista)", "3.1, Figura 3-2"),
    ("Soportes SP-01 a SP-11", "11 tipos pedestales perfil UPE 80 / cuadrado 100 mm / chapas A36, fabricados por tercero", "P22-DWG-06-006-107 (21 pag)", "Disponible", "3.4, 5.4, Anexo A3"),
    ("VM-06-001 a VM-06-016", "Valvulas mariposa wafer CL150 KSB ISORIA 10, fundicion nodular A536, asiento EPDM, accionamiento manual por reductor MS/MC. Peso conjunto DN100 ~12-13 kg", "Catalogo KSB ISORIA 10 / MS-MC; LI P22-LI-06-006-103", "Disponible", "5.2, 5.2.1"),
    ("VR-06-001, VR-06-003", "Valvulas check Duo wafer CL150 super duplex 2507, disco super duplex, resorte Inconel X-750, asiento EPDM. Peso DN100 ~7-9 kg", "LI P22-LI-06-006-103", "Disponible", "5.2, 5.2.1"),
    ("7 instrumentos in-line Area 06", "LSH-06-001/003, LSL-06-001, LIT-06-001, PI-06-001, PIT-06-001, FIT-06-001", "P22-LI-06-008-101 + P22-ET-06-008-101", "Disponible", "3.4, 5.3, Fig 3-1"),
    ("Scope BW Water - Contenedor RO 40 ft HC", "Modulo OI 2da etapa, peso ~14.934 kg", "P22-DWG-09-005-001 Rev A", "No disponible", "4.1, 6.4"),
    ("Scope BW Water - Sistema CIP", "TK-09-001 (10.470 kg), FIL-09-002 (267,6 kg), BH-09-002 (180 kg), REL-09-001 (16 kW TR L&A / 20 kW P&ID - reconciliar antes de IFC), TK-09-002 (490 kg), BDS-09-001/002 (57,4 kg), panel local (350 kg), panel calentador (50 kg)", "Datasheets BW Water + P22-DWG-09-005-001 Rev A", "No disponible", "4.2, 6.4"),
])
add_para(doc,
    "El contratista verifica el inventario al recibir cada lote en bodega; los danos de transporte "
    "detectados antes de la firma son responsabilidad de ADASA, los detectados despues son "
    "responsabilidad del contratista.")

# ----------------- Anexo A9 -----------------
doc.add_heading("Anexo A9 - Formato de Licitacion (Planilla de Oferta Economica)", level=2)
add_para(doc,
    "El oferente entrega su oferta economica completando las 7 sub-tablas siguientes. La "
    "cubicacion de las cantidades de caneria HDPE/PE y accesorios proviene del LI Materiales "
    "P22-LI-06-006-102 del Compilado Rev 0 (335 m totales de caneria + accesorios detallados). "
    "Las cantidades indicadas son referenciales para uniformar la base de comparacion entre "
    "ofertas; en modalidad Suma Alzada el riesgo de variacion menor respecto del estado real "
    "es del contratista una vez adjudicado el contrato.")

doc.add_heading("A9.1 - Partida Piping HDPE/PE (cotizacion por isometria)", level=3)
add_para(doc,
    "Una unidad por isometria. El precio unitario por isometria incluye: suministro del HDPE "
    "PE100 PN10 + accesorios + electrofusion + ensayo hidrostatico + flushing + protocolo de "
    "prueba. El oferente verifica las cantidades de su isometria contra el BOM (Bill of Materials) "
    "que cada isometria trae en el Cuadernillo P22-DWG-06-006-001 a -011 y contra la cubicacion "
    "referencial consolidada del A9.2.")
add_simple_table(doc, [
    ("Item", "Codigo Isometria", "Linea", "Hojas", "DN", "ML caneria (m)", "Spec", "Precio Unit. (CLP)", "Subtotal"),
    ("1", "P22-DWG-06-006-001", "SA-HDPE-DN110-PN10-001", "H.1, H.2", "DN100", "~45", "HDPE PE100 PN10", "", ""),
    ("2", "P22-DWG-06-006-002", "SA-HDPE-DN110-PN10-002", "H.1 a H.4", "DN100", "~60", "HDPE PE100 PN10", "", ""),
    ("3", "P22-DWG-06-006-003", "SA-HDPE-DN63-PN10-001", "(hoja unica)", "DN50", "1", "HDPE PE100 PN10", "", ""),
    ("4", "P22-DWG-06-006-004", "SA-HDPE-DN110-PN10-004", "(hoja unica)", "DN100", "~10", "HDPE PE100 PN10", "", ""),
    ("5", "P22-DWG-06-006-005", "SA-HDPE-DN110-PN10-005", "H.1 a H.4", "DN100", "~50", "HDPE PE100 PN10", "", ""),
    ("6", "P22-DWG-06-006-006", "SA-HDPE-DN110-PN10-003", "(hoja unica)", "DN100", "~15", "HDPE PE100 PN10", "", ""),
    ("7", "P22-DWG-06-006-008", "PE-HDPE-DN90-PN10-001", "H.1 a H.4", "DN80", "~80", "HDPE PE100 PN10", "", ""),
    ("8", "P22-DWG-06-006-009", "PE-HDPE-DN90-PN10-003", "H.1, H.2", "DN80", "~30", "HDPE PE100 PN10 (off-spec)", "", ""),
    ("9", "P22-DWG-06-006-011", "SA-HDPE-DN110-PN10-007", "H.1 a H.7", "DN150/DN100", "~44 (3+41)", "HDPE PE100 PN10", "", ""),
    ("10", "(a confirmar Vandoorn)", "AMF-HDPE-DN160-PN10-002 + SA-CPVC-DN200-PN10-001", "(cubicar Corte D)", "DN160/DN200", "(cubicar)", "HDPE PE100 + CPVC PN10", "", ""),
    ("", "", "", "", "Total ML ~335 m + Tie-in 6", "", "", "Subtotal Piping", ""),
])
add_para(doc,
    "Distribucion por DN segun LI Materiales: DN50=1m, DN80=151m, DN100=180m, DN150=3m. Los ML "
    "por isometria son estimaciones a partir del numero de hojas; el oferente valida contra el "
    "BOM de cada isometria.")

doc.add_heading("A9.2 - Cubicacion referencial consolidada por familia de materiales (sin precio)", level=3)
add_para(doc,
    "Vista agregada del LI Materiales P22-LI-06-006-102 para que el oferente valide el desglose "
    "de su cotizacion por isometria del A9.1. Esta tabla NO tiene columna de precio - es "
    "referencia tecnica.")
add_simple_table(doc, [
    ("Familia", "Item", "DN", "Cantidad", "Unidad"),
    ("Caneria HDPE PE100 PN10 (ISO 4427, SDR 17)", "DN50 (2\")", "DN50", "1", "m"),
    ("", "DN80 (3\")", "DN80", "151", "m"),
    ("", "DN100 (4\")", "DN100", "180", "m"),
    ("", "DN150 (6\")", "DN150", "3", "m"),
    ("", "Subtotal caneria", "", "335", "m"),
    ("Codos HDPE (electrofusion ISO 15494)", "Codo 45 grados DN100", "DN100", "11", "u"),
    ("", "Codo 45 grados DN80", "DN80", "6", "u"),
    ("", "Codo 90 grados DN100", "DN100", "40", "u"),
    ("", "Codo 90 grados DN80", "DN80", "32", "u"),
    ("", "Codo 90 grados DN150", "DN150", "1", "u"),
    ("", "Codo 90 grados DN50", "DN50", "1", "u"),
    ("", "Codo 90 grados transicion PE100 x super duplex DN25", "DN25", "2", "u"),
    ("Cuplas HDPE (electrofusion)", "DN100", "DN100", "25", "u"),
    ("", "DN80", "DN80", "35", "u"),
    ("", "DN150", "DN150", "1", "u"),
    ("", "DN50", "DN50", "4", "u"),
    ("", "DN65", "DN65", "1", "u"),
    ("Tees y reducciones HDPE", "Tee DN100", "DN100", "2", "u"),
    ("", "Tee DN80", "DN80", "2", "u"),
    ("", "Tee DN150", "DN150", "1", "u"),
    ("", "Reduccion concentrica DN100x80", "-", "3", "u"),
    ("", "Reduccion concentrica DN100x50", "-", "1", "u"),
    ("", "Reduccion concentrica DN80x65", "-", "1", "u"),
    ("", "Reduccion concentrica DN150x100", "-", "1", "u"),
    ("", "Reduccion excentrica DN100x80", "-", "1", "u"),
    ("Accesorios especiales", "Brunch Saddle DN150x80", "-", "1", "u"),
    ("", "Spigot Saddle DN100x25 (con cutter)", "-", "2", "u"),
    ("", "Buje reduccion 1\"x1/2\" super duplex SAF2507", "-", "2", "u"),
    ("", "Junta de desarme flangeada DN80", "DN80", "1", "u"),
    ("", "Back-up flange DN100 HDPE", "DN100", "1", "u"),
    ("Accesorios PVC-U (SCH 80, ASTM D2467)", "Codo PVC-U DN100", "DN100", "1", "u"),
    ("", "Reducing Tee PVC-U DN100x50", "-", "1", "u"),
    ("Bridas LJ ASME B16.5 150 LB", "DN100", "DN100", "22", "u"),
    ("", "DN80", "DN80", "19", "u"),
    ("", "DN50", "DN50", "4", "u"),
    ("", "DN65", "DN65", "1", "u"),
    ("Stub-ends HDPE PE100 (DIN 16963 P.4, PN10)", "DN100", "DN100", "23", "u"),
    ("", "DN80", "DN80", "19", "u"),
    ("", "DN50", "DN50", "4", "u"),
    ("", "DN65", "DN65", "1", "u"),
    ("Tornilleria (esparragos ANSI B16.5 150 LB, ASTM A193 Gr. B8 CL2, c/2 tuercas A194 Gr.8 + 2 golillas)", "1/2\"x85", "-", "4", "u"),
    ("", "5/8\"x110", "-", "8", "u"),
    ("", "5/8\"x160", "-", "12", "u"),
    ("", "5/8\"x170", "-", "64", "u"),
    ("", "5/8\"x175", "-", "16", "u"),
    ("", "5/8\"x190", "-", "16", "u"),
    ("", "5/8\"x210", "-", "4", "u"),
    ("", "5/8\"x220", "-", "28", "u"),
    ("", "5/8\"x230", "-", "72", "u"),
    ("", "5/8\"x245", "-", "8", "u"),
    ("", "Total esparragos", "", "232", "u"),
    ("Empaquetaduras flat ring NBR/SBR (ASME B16.21, 150 LB, espesor 1/8\")", "DN100", "DN100", "23", "u"),
    ("", "DN80", "DN80", "16", "u"),
    ("", "DN50", "DN50", "4", "u"),
    ("", "DN65", "DN65", "1", "u"),
    ("", "DN40", "DN40", "1", "u"),
    ("", "Total empaquetaduras", "", "45", "u"),
])

doc.add_heading("A9.3 - Partida Valvulas (instalacion de valvula suministrada por ADASA)", level=3)
add_para(doc,
    "El contratista cotiza unicamente la mano de obra de instalacion fisica (tornillos, gaskets "
    "nuevas, torque controlado, alineamiento, verificacion de posicion). El suministro es ADASA "
    "(marca KSB ISORIA 10 para mariposas + Duo Check super duplex para retenciones).")
add_simple_table(doc, [
    ("Item", "TAG Valvula", "Tipo", "DN", "Ubicacion", "Precio Unit. instalacion (CLP)"),
    ("V1", "VM-06-001", "Mariposa wafer CL150 manual c/reductor", "DN100", "Entrada TK-06-001", ""),
    ("V2", "VM-06-002", "Mariposa wafer CL150 manual c/reductor", "DN100", "Salida TK-06-001", ""),
    ("V3", "VM-06-003", "Mariposa wafer CL150 manual c/reductor", "DN63 (2\")", "Pre-tratamiento", ""),
    ("V4", "VM-06-004", "Mariposa wafer CL150 manual c/reductor", "DN100", "Succion BH-06-001", ""),
    ("V5", "VM-06-005", "Mariposa wafer CL150 manual c/reductor", "DN100", "Descarga BH-06-001", ""),
    ("V6", "VR-06-001", "Check Duo wafer CL150 super duplex", "DN100", "Descarga BH-06-001", ""),
    ("V7", "VM-06-006", "Mariposa wafer CL150 manual c/reductor", "DN90 (3\")", "Postratamiento", ""),
    ("V8", "VM-06-007", "Mariposa wafer CL150 manual c/reductor", "DN90 (3\")", "Postratamiento", ""),
    ("V9", "VM-06-009", "Mariposa wafer CL150 manual c/reductor", "DN100", "Postratamiento", ""),
    ("V10", "VM-06-010", "Mariposa wafer CL150 manual c/reductor", "DN100", "Postratamiento", ""),
    ("V11", "VM-06-015", "Mariposa wafer CL150 manual c/reductor", "DN90 (3\")", "Postratamiento", ""),
    ("V12", "VM-06-016", "Mariposa wafer CL150 manual c/reductor", "DN90 (3\")", "Postratamiento", ""),
    ("V13", "VR-06-003", "Check Duo wafer CL150 super duplex", "DN100", "Postratamiento", ""),
    ("", "", "", "", "Subtotal Valvulas", ""),
])

doc.add_heading("A9.4 - Partida Instrumentos in-line (instalacion suministrado por ADASA)", level=3)
add_para(doc,
    "Aplica a los 7 instrumentos in-line del Area 06. Scope: instalacion fisica + amarre del "
    "cableado hasta caja de paso. EXCLUYE: calibracion, lazo, sintonia, commissioning.")
add_simple_table(doc, [
    ("Item", "TAG Instrumento", "Tipo", "Servicio", "Precio Unit. instalacion (CLP)"),
    ("I1", "LSH-06-001", "Switch nivel alto", "TK-06-001", ""),
    ("I2", "LSL-06-001", "Switch nivel bajo", "TK-06-001", ""),
    ("I3", "LIT-06-001", "Transmisor ultrasonico de nivel", "TK-06-001", ""),
    ("I4", "LSH-06-003", "Switch nivel alto", "Fosa TK-06-002", ""),
    ("I5", "PI-06-001", "Manometro", "Descarga BH-06-001", ""),
    ("I6", "PIT-06-001", "Transmisor de presion", "Alimentacion de salmuera", ""),
    ("I7", "FIT-06-001", "Caudalimetro electromagnetico", "Alimentacion de salmuera", ""),
    ("", "", "", "Subtotal Instrumentos", ""),
])

doc.add_heading("A9.5 - Partida Montaje BH-06-001", level=3)
add_para(doc,
    "Cotizacion unica para el montaje completo de la bomba de alimentacion de salmuera. "
    "Suministro ADASA (equipo KSB completo + motor WEG + acoplamiento + base; peso seco 223,5 kg). "
    "El precio unitario incluye:")
add_simple_table(doc, [
    ("Item", "Concepto", "Cantidad", "Precio Unit. (CLP)", "Subtotal"),
    ("M1", "Montaje BH-06-001: recepcion en bodega contra inventario, izaje y posicionamiento sobre fundacion L&A, anclaje con 4 pernos M16x200 (suministro contratista), alineacion bomba-motor con relojes comparadores segun procedimiento KSB (tolerancias del fabricante), conexion hidraulica a la linea de succion SA-HDPE-DN110-PN10-004 via reduccion concentrica DN100x80, conexion hidraulica a la linea de descarga SA-HDPE-DN110-PN10-005 via reduccion concentrica DN100x50, conexionado electrico al motor WEG 15 HP / 11 kW hasta caja de paso, pruebas funcionales en vacio (rodaje sin carga, verificacion de sentido de giro, medicion de vibracion conforme a ISO 10816), entrega con protocolo firmado", "1 global", "", ""),
    ("", "", "", "Subtotal Montaje BH-06-001", ""),
])
add_para(doc,
    "Excluido: pernos M16 de anclaje ya estan en la tornilleria del LI Materiales A9.2. "
    "Commissioning con agua de proceso (lo realiza ADASA/BW Water en fase posterior).")

doc.add_heading("A9.6 - Partida Obras Civiles", level=3)
add_para(doc,
    "A itemizar contra los planos L&A Rev 0 cuando se emitan como Adenda Tecnica (excavaciones, "
    "fundacion TK-06-001, fundacion BH-06-001, fundacion compartida contenedor + CIP, fosa "
    "drenajes TK-06-002, canalizaciones, cubierta metalica CIP, anclajes y conexiones, pavimentos). "
    "El presente borrador deja la partida como 'a complementar con Adenda Tecnica L&A'; la "
    "proxima revision de estas Bases incluira las cubicaciones civiles por item (m3 de hormigon "
    "G-25 por elemento, m2 de impermeabilizacion, kg de acero A630-420H, m2 de cubierta metalica, "
    "etc.).")

doc.add_heading("A9.7 - Partida Coordinacion e ITO (gastos generales)", level=3)
add_para(doc,
    "Cotizacion por hora-cuadrilla o global para las actividades de coordinacion con ADASA y la "
    "operacion del Modulo 3 (preparacion de procedimientos de tie-in, gestion de permisos de "
    "trabajo, supervision durante ventanas de parada, preparacion de dossier de calidad y as-built).")
add_simple_table(doc, [
    ("Item", "Concepto", "Cantidad referencial", "Precio Unit. (CLP)", "Subtotal"),
    ("C1", "Tarifa hora-cuadrilla para ejecucion de tie-ins M3 (cuadrilla 4 personas)", "-", "", "-"),
    ("C2", "N de ventanas de parada coordinadas con M3", "2 ventanas", "", ""),
    ("C3", "Gestion documental: procedimientos, permisos, protocolos, as-built", "1 global", "", ""),
    ("", "", "", "Subtotal Coord./ITO", ""),
])

doc.add_heading("A9.8 - Resumen general de la oferta economica", level=3)
add_simple_table(doc, [
    ("Partida", "Subtotal (CLP)"),
    ("A9.1 Piping (cotizacion por isometria)", ""),
    ("A9.3 Valvulas (instalacion por TAG)", ""),
    ("A9.4 Instrumentos in-line (instalacion por TAG)", ""),
    ("A9.5 Montaje BH-06-001", ""),
    ("A9.6 Obras Civiles (a complementar con Adenda L&A)", ""),
    ("A9.7 Coordinacion e ITO", ""),
    ("Subtotal neto", ""),
    ("IVA 19%", ""),
    ("TOTAL OFERTA (CLP con IVA)", ""),
])
add_para(doc,
    "El oferente entrega esta planilla A9 firmada por el representante legal en formato Excel + "
    "PDF. La cubicacion referencial del A9.2 no aporta subtotal porque sus cantidades ya estan "
    "distribuidas entre las isometrias del A9.1.")

# ----------------- Anexo A10 -----------------
doc.add_heading("Anexo A10 - Bases administrativas", level=2)
add_para(doc,
    "Las clausulas administrativas detalladas vigentes para todo contrato de obra con Aguas "
    "Antofagasta S.A. se entregan como documento separado al adjudicar; los oferentes que ya "
    "mantienen contratos vigentes con el mandante cuentan con el formato en su poder. El "
    "presente capitulo 2 del cuerpo del documento (Informacion Administrativa) prevalece sobre "
    "el formato administrativo generico cuando exista divergencia respecto del alcance especifico "
    "de esta licitacion.")
add_para(doc, "Estructura del formato administrativo Aguas Antofagasta:")
add_simple_table(doc, [
    ("Capitulo", "Contenido"),
    ("1", "Convocatoria y precalificacion del oferente"),
    ("2", "Modalidad de contratacion y bases economicas"),
    ("3", "Plazos y programa contractual"),
    ("4", "Garantias y seguros"),
    ("5", "Forma de pago, moneda, reajuste e IVA"),
    ("6", "Multas y clausulas de incumplimiento"),
    ("7", "Criterios de evaluacion de ofertas"),
    ("8", "Subcontratacion"),
    ("9", "Seguridad y salud ocupacional"),
    ("10", "Calidad y aseguramiento"),
    ("11", "Proteccion del medio ambiente"),
    ("12", "Confidencialidad y propiedad intelectual"),
    ("13", "Resolucion de controversias"),
    ("14", "Causales de termino anticipado"),
])
add_para(doc,
    "Los oferentes que NO mantienen contrato vigente con Aguas Antofagasta solicitan el formato "
    "administrativo a la Subgerencia de Abastecimiento al recibir la invitacion a esta licitacion.")

# ----------------- Anexo A11 -----------------
doc.add_heading("Anexo A11 - Procedimiento de permisos de trabajo en planta operativa (Modulo 3)", level=2)
add_para(doc,
    "Aplica a todas las actividades del contratista dentro del area operativa del Modulo 3 "
    "(planta existente de 11 l/s). Los tie-ins 1 y 3 sobre lineas en operacion estan sujetos a "
    "este procedimiento conforme al capitulo 7 del presente documento.")

add_para_bold_lead(doc, "Etapa 1 - Solicitud del permiso (T-5 dias habiles): ",
    "el supervisor de obra del contratista presenta a la Subgerencia de Operacion de Aguas "
    "Antofagasta el procedimiento de trabajo con cinco dias habiles de anticipacion a la "
    "ventana de parada notificada por ADASA. La solicitud debe incluir:")
add_bullet(doc, "Descripcion de la actividad y resultado esperado")
add_bullet(doc, "Analisis de riesgos del trabajo (JHA / IPER especifica)")
add_bullet(doc, "Secuencia detallada de actividades con duraciones")
add_bullet(doc, "Lista nominal del personal asignado (con certificados de competencia y curso de induccion del recinto vigente)")
add_bullet(doc, "Listado de herramientas y equipos")
add_bullet(doc, "EPP especifico requerido (gafas, guantes, calzado de seguridad, casco, arnes cuando aplique)")
add_bullet(doc, "Plan de contingencia ante eventos imprevistos")

add_para_bold_lead(doc, "Etapa 2 - Aprobacion por la operacion (T-3 a T-1 dias habiles): ",
    "la Subgerencia de Operacion revisa el procedimiento, identifica interferencias con planta y "
    "emite el permiso de trabajo formal. Cualquier observacion se devuelve al contratista para "
    "incorporacion previa a la ejecucion.")

add_para_bold_lead(doc, "Etapa 3 - Apertura del permiso (T-0, dia de la ventana): ",
    "la operacion entrega la linea aislada, drenada y bloqueada (LOTO instalado) con verificacion "
    "firmada por el operador. El supervisor del contratista valida visualmente el aislamiento, "
    "instala su propio bloqueo personal (LOTO complementario) y firma la apertura del permiso. "
    "El permiso queda visible en el area de trabajo durante toda la jornada.")

add_para_bold_lead(doc, "Etapa 4 - Ejecucion dentro de la ventana: ",
    "el contratista ejecuta el corte, empalme y prueba de estanqueidad del tramo conectado, "
    "manteniendo en todo momento al supervisor de la operacion informado de avances y cualquier "
    "desviacion. Cualquier emergencia fuera del procedimiento aprobado obliga a detener trabajos "
    "y consultar con la Subgerencia de Operacion.")

add_para_bold_lead(doc, "Etapa 5 - Cierre del permiso: ",
    "al termino de la actividad, el contratista entrega la linea probada con protocolo firmado, "
    "retira herramientas y materiales, libera su LOTO complementario y firma el cierre del "
    "permiso. La operacion de Aguas Antofagasta repone el servicio segun su procedimiento interno.")

add_para_bold_lead(doc, "Penalidades por desviacion: ",
    "el incumplimiento del procedimiento o el exceso de la ventana sin causa justificada da "
    "lugar a la aplicacion de las multas del capitulo 2.7 (atraso en hito critico = 0,10% del "
    "monto del contrato por dia calendario, con tope del 10%).")

# ============================================================================
# Cierre
# ============================================================================
# Reaplicar idioma al final por si algun add_paragraph reseteo algo
fijar_idioma(doc, "es-CL")

doc.save(OUTPUT)
print(f"[BL] DOCX generado: {OUTPUT}")
