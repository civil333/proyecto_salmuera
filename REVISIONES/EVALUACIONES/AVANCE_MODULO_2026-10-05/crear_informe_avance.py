#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Informe interno de avance del modulo en Penang, 17-Sep al 5-Oct-2026, dia por dia a partir de los
correos, con fotos. Word plano (sin template ADASA, a pedido del usuario).

Fuentes: CORREOS/_RECIBIDOS/ (correos capturados), REVISIONES/EVALUACIONES/_PUESTA_AL_DIA_2026-10-05.md,
Progress Reports W37 a W39 de BW (PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/), informes BV IR016 a
IR018 (PROGRAMA y CONTRATO/HITO BUREAU VERITAS/04 INFORMES BV/) y Transmittal N41. Las fotos de img/ se
extrajeron como imagen nativa de esos PDF.

Uso: python crear_informe_avance.py
"""
import os
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

sys.path.insert(0, os.path.expanduser("~/.claude/skills/_shared"))
from docx_metadata import apply_core_properties, fix_app_xml  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "img")
OUT = os.path.join(BASE, "Avance_Modulo_Penang_17Sep-05Oct-2026.docx")
LANG = "es-CL"

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)
st.paragraph_format.space_after = Pt(4)


# ---------------------------------------------------------------- helpers
def p(texto="", negrita_inicial=None, italic=False, size=None, align=None):
    par = doc.add_paragraph()
    if negrita_inicial:
        r = par.add_run(negrita_inicial)
        r.bold = True
    r = par.add_run(texto)
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    if align:
        par.alignment = align
    return par


def vineta(texto, negrita_inicial=None):
    par = doc.add_paragraph(style="List Bullet")
    if negrita_inicial:
        r = par.add_run(negrita_inicial)
        r.bold = True
    par.add_run(texto)
    return par


def correo(hora, quien, asunto, texto, adjuntos=None):
    """Una entrada de correo: hora y remitente en negrita, asunto en cursiva, resumen y adjuntos."""
    par = doc.add_paragraph(style="List Bullet")
    r = par.add_run(f"{hora} · {quien}. ")
    r.bold = True
    if asunto:
        r = par.add_run(f"«{asunto}». ")
        r.italic = True
    par.add_run(texto)
    if adjuntos:
        r = par.add_run(" Adjuntos: " + "; ".join(adjuntos) + ".")
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


def _sin_bordes(tabla):
    tblPr = tabla._tbl.tblPr
    bordes = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "nil")
        bordes.append(e)
    tblPr.append(bordes)


def _leyenda(par_destino, texto):
    r = par_destino.add_run(texto)
    r.italic = True
    r.font.size = Pt(9)
    par_destino.alignment = WD_ALIGN_PARAGRAPH.CENTER


def fotos(items):
    """items: lista de (archivo, leyenda). Las verticales van de a dos por fila; las horizontales, solas."""
    vert = [(f, t) for f, t in items if Image.open(os.path.join(IMG, f)).height > Image.open(os.path.join(IMG, f)).width]
    horiz = [(f, t) for f, t in items if (f, t) not in vert]
    for f, t in horiz:
        par = doc.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ancho_px = Image.open(os.path.join(IMG, f)).width
        par.add_run().add_picture(os.path.join(IMG, f), width=Cm(14 if ancho_px >= 900 else 10))
        _leyenda(doc.add_paragraph(), t)
    for i in range(0, len(vert), 2):
        par_v = vert[i:i + 2]
        tabla = doc.add_table(rows=2, cols=len(par_v))
        tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
        _sin_bordes(tabla)
        for j, (f, t) in enumerate(par_v):
            c = tabla.rows[0].cells[j].paragraphs[0]
            c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            c.add_run().add_picture(os.path.join(IMG, f), height=Cm(9.5))
            _leyenda(tabla.rows[1].cells[j].paragraphs[0], t)
        doc.add_paragraph()


def tabla(encabezados, filas, anchos=None, size=9):
    t = doc.add_table(rows=1 + len(filas), cols=len(encabezados))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(encabezados):
        c = t.rows[0].cells[j]
        c.text = ""
        r = c.paragraphs[0].add_run(h)
        r.bold = True
        r.font.size = Pt(size)
    for i, fila in enumerate(filas, start=1):
        for j, v in enumerate(fila):
            c = t.rows[i].cells[j]
            c.text = ""
            r = c.paragraphs[0].add_run(str(v))
            r.font.size = Pt(size)
    if anchos:
        # Word obedece a la grilla (w:tblGrid), no solo al ancho de celda
        t.autofit = False
        for j, gc in enumerate(t._tbl.tblGrid.findall(qn("w:gridCol"))):
            gc.set(qn("w:w"), str(int(anchos[j] * 567)))
        for fila in t.rows:
            for j, w in enumerate(anchos):
                fila.cells[j].width = Cm(w)
    doc.add_paragraph()
    return t


def _set_lang(rPr, lang):
    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = OxmlElement("w:lang")
        rPr.append(lang_el)
    lang_el.set(qn("w:val"), lang)
    lang_el.set(qn("w:eastAsia"), lang)
    lang_el.set(qn("w:bidi"), lang)


def fijar_idioma_documento(lang=LANG):
    _set_lang(doc.styles["Normal"].element.get_or_add_rPr(), lang)
    pars = list(doc.paragraphs)
    for t in doc.tables:
        for fila in t.rows:
            for c in fila.cells:
                pars += c.paragraphs
    for par in pars:
        for r in par.runs:
            _set_lang(r._element.get_or_add_rPr(), lang)


# ---------------------------------------------------------------- contenido
doc.add_heading("Avance del módulo de salmuera en Penang", level=0)
p("Del jueves 17 de septiembre al lunes 5 de octubre de 2026, día por día según los correos. "
  "Uso interno de ADASA. Preparado por Luis Rivera González el 5 de octubre de 2026.", italic=True, size=10)
p("Horas de Chile. Las fotos son las que mandaron BW Water en sus informes semanales y Bureau Veritas en sus "
  "informes de inspección; se ubican en el día en que llegó el correo que las trajo. El último registro "
  "fotográfico del módulo es del 21 de septiembre: el 28, Eduardo Yamauchi respondió que no tenía fotos más "
  "nuevas, y al 5 de octubre no ha llegado el informe de la semana 40.", size=10)

doc.add_heading("1. Resumen", level=1)
vineta("el avance que declara BW Water subió de 77 % a 87 % en el sistema SWRO y de 68 % a 84 % en el CIP "
       "entre la semana 37 (al 13-Sep) y la 39 (al 27-Sep). Se terminó la fabricación de spools, todas las "
       "hidrostáticas de alta y la instalación del filtro de cartucho y de la bomba de alta. El antiincrustante "
       "sigue en 64 % las tres semanas.", "Montaje: ")
vineta("Bureau Veritas confirmó que los turbocargadores calzan con sus planos aprobados y que el problema era la "
       "interfaz de los spools. Los spools 004 y 008 se cortaron, se resoldaron, se reensayaron el 22 y el 23-Sep "
       "con el inspector presente y quedaron montados al turbocargador de alimentación al 27-Sep.", "Turbocargadores: ")
vineta("las once líneas de súper dúplex tienen al 23-Sep un ensayo atestiguado por BV y conforme a la presión de la "
       "Line List. Era el punto de detención de la fila 5.2 del ITP.", "Hidrostáticas: ")
vineta("sin fecha escrita. En la reunión del 24-Sep BW lo planificó del 5 al 7 de octubre; el 28-Sep Victor lo "
       "situó el 7-Oct en el mejor caso o la semana del 12. El procedimiento del FAT volvió en Código 3 el 2-Oct "
       "(Transmittal N41) y, como la fila 7.1 del ITP es punto de detención de ADASA, el FAT no puede abrir "
       "formalmente hasta que se apruebe.", "FAT: ")
vineta("el embarque que BW declaró para el 28-Sep no ocurrió. Al 5-Oct van 63 días sobre el plazo contractual "
       "del 3-Ago.", "Embarque: ")
vineta("inspección dimensional final, punch list, limpieza y embalaje siguen en 0 %; la documentación de "
       "ingeniería del SWRO sigue en 85 % y las membranas en 80 %, pendientes de LG, las tres semanas.",
       "Lo que no se movió: ")
vineta("las revisiones de las entregas E96 y E97 vencieron el 1 y el 2 de octubre (Cláusula 37.2, siete días "
       "hábiles); la E99 vence el jueves 8 y la E100 el martes 13.", "Pendiente de ADASA: ")

doc.add_heading("2. Dónde estaba el módulo el 14 de septiembre", level=1)
p("El informe de la semana 37 (7 al 13-Sep) dejaba el skid estructural con los recipientes de presión ya "
  "insertado en el contenedor, los spools, válvulas e instrumentos en montaje, y la bomba de alta con los dos "
  "turbocargadores recién llegados al taller. Avance declarado: SWRO 77 %, CIP 68 %, antiincrustante 64 %. El "
  "lunes 14 BW reportó en una línea que los spools de un turbocargador no calzaban con sus boquillas y el "
  "miércoles 16 lo explicó en reunión; la del jueves 17 fijó el plan de rectificación (corte el 18, raíz el 19, tintas penetrantes el 21, hidrostática "
  "el 22 y remontaje el 23) y dejó el FAT a reprogramar.")
fotos([("01_W37_contenedor_con_skid.jpg", "Contenedor del módulo con el skid y los recipientes de presión ya insertados. Informe semanal 37 de BW."),
       ("02_W37_recipientes_de_presion.jpg", "Recipientes de presión montados en el skid. Informe semanal 37."),
       ("03_14SEP_bomba_alta_presion.jpg", "Bomba de alta presión Fedco desembalada en Penang. Foto del 14-Sep.")])

doc.add_heading("3. Los correos, día por día", level=1)

doc.add_heading("Jueves 17 de septiembre", level=2)
correo("06:23", "Muhammad Fadhil (BW Water) a Bureau Veritas y ADASA", "RE: 25007 TALTAL - Request to witness inspection 008",
       "Manda el registro de inspección del día, primera de las dos jornadas de la solicitud 008 (ensayo de alta e "
       "instalación de equipos).", ["Taltal Hydrotest Report BV 17Sep.pdf"])
correo("08:30", "Reunión semanal de coordinación", None,
       "BW reconoce que solo dos spools de la conexión superior del turbocargador chocan y que el equipo cumple el "
       "modelo. ADASA acepta que se corte y suelde en paralelo con su revisión de los planos corregidos. El FAT "
       "queda a reprogramar con el cronograma posterior al retrabajo. Minuta P22-MI-10-000-002-0.")

doc.add_heading("Viernes 18 de septiembre (feriado en Chile)", level=2)
correo("07:01", "Muhammad Fadhil (BW Water) a Bureau Veritas y ADASA", "RE: 25007 TALTAL - Request to witness inspection 008",
       "Informe de la segunda jornada. Las fotos y el resultado de BV llegan el 23.", ["Taltal Inspection Report BV W 18SEP.pdf"])
correo("12:59", "Luis Rivera (ADASA) a BW Water", "Transmittal N40",
       "Devuelve en Código 3 el procedimiento del FAT del módulo, Rev A, recibido esa mañana: diez páginas que "
       "repiten las filas del ITP sin pasos de prueba ni valores de aceptación. Exige la Rev B al viernes 25.")
correo("15:59", "Microsoft Outlook", "Aviso de no entrega",
       "Aviso por el N40. El detalle del error nombra solo la casilla dada de baja de Adzlan Abd Rahim; el resto "
       "de los destinatarios de BW recibió.")
correo("22:41", "Mohd Adnin (BW Water) a Bureau Veritas", "25007 TALTAL - Request to witness inspection 009",
       "Pide al inspector para el ensayo de alta presión del martes 22.", ["Inspection Request (009) Day 1.pdf"])

doc.add_heading("Domingo 20 de septiembre", level=2)
correo("10:06", "Emylia Rosli (BV Malasia) a Mohd Adnin", "RE: Request to witness inspection 009",
       "Confirma que asiste el inspector Fakhrul Radzi el 22.")

doc.add_heading("Martes 22 de septiembre", level=2)
correo("00:45", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "Weekly Engineering Report",
       "Estado documental semanal.", ["25007_Taltal_DDSR_2026.09.21.pdf"])
correo("03:15", "Mohd Adnin (BW Water) a BV Malasia", "RE: Request to witness inspection 009",
       "Extiende la inspección al miércoles 23.", ["Inspection Request (009) Day 2.pdf"])
correo("03:36", "Emylia Rosli (BV Malasia) a Mohd Adnin", "RE: Request to witness inspection 009",
       "El mismo inspector sigue el 23.")
correo("06:32", "Mohd Adnin (BW Water) a todos", "RE: Request to witness inspection 009",
       "Registro del ensayo del día.", ["Taltal Hydrotest Report BV W 22Sep.pdf"])
correo("06:34", "Fitri Indriyani (BW Water) a ADASA", "TALTAL: DOCUMENT SUBMISSION 25007-0096",
       "Cuatro documentos por enlace: Piping Layout Rev E, Maintenance Lifting Points Rev A, GA del estanque de "
       "antiincrustante Rev E y el procedimiento FAT del tablero PLC/LCP Rev 0. La carpeta trae además los DWG de "
       "los tres planos, que el correo no declara.")
correo("11:36", "Victor Gutiérrez (ADASA) a Jaime Martínez (BV Chile)", "Turbocharger spool offset and inspection scope in Penang",
       "Pide los informes del levantamiento de los turbocargadores que Luis solicitó el 16.")
correo("15:10", "Jaime Martínez (BV Chile) a Victor Gutiérrez", "RE: Turbocharger spool offset",
       "Los pidió a BV Malasia y los reenviará al recibirlos.")

doc.add_heading("Miércoles 23 de septiembre", level=2)
correo("00:01", "Fitri Indriyani (BW Water) a ADASA", "TALTAL: DOCUMENT SUBMISSION 25007-0097",
       "HMI Display Screenshot Rev 0, emitido para construcción.")
correo("09:12", "Jaime Martínez (BV Chile) a Victor Gutiérrez", "Turbocharger spool offset … 17 y 18 de septiembre",
       "Informe IR016 de las dos jornadas. El inspector midió los turbocargadores y los encontró conformes a los "
       "planos aprobados en posición, orientación y dimensiones de boquillas; la discrepancia estaba en la "
       "interfaz con el spool, que BW ya había cortado. El ensayo de alta y la verificación de instalación no se "
       "hicieron porque spools y equipos no estaban listos; quedó una punch list para comparar las mediciones "
       "nuevas contra los planos aprobados.", ["IR-016-ADASA-BVM-(17-18092026).pdf"])
fotos([("04_IR016_medicion_turbo.jpg", "17-18 Sep: el inspector de BV mide la conexión del turbocargador Fedco. Informe IR016."),
       ("05_IR016_spool_cortado.jpg", "17-18 Sep: spool ya cortado, sobre caballetes, para su rectificación. Informe IR016."),
       ("06_IR016_turbo_con_spools.jpg", "Turbocargador con sus spools en el skid. Informe IR016.")])
correo("09:21", "Jaime Martínez (BV Chile) a Victor Gutiérrez", "RE: Turbocharger spool offset … 22 de septiembre",
       "Informe IR017: el spool DA-SSD-DN65-09-008 modificado se ensayó a 75 barG, satisfactorio. La foto muestra "
       "que se probó fuera del contenedor, sobre pallets, como había pedido ADASA el 16.",
       ["IR017-ADASA-BVM-22092026.pdf", "Annex 1 (22092026).pdf", "Taltal Hydrotest Report BV W 22Sep.pdf"])
fotos([("07_IR017_spool_008_prueba.jpg", "22-Sep: spool DA-SSD-DN65-09-008 en prueba hidrostática fuera del contenedor. Informe IR017.")])
correo("23:08", "Mohd Adnin (BW Water) a todos", "RE: Request to witness inspection 009",
       "Registro del ensayo del 23.", ["Taltal Hydrotest Report BV W 23SEP 2.pdf"])
correo("23:24", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "25007 TalTal Delco Motorized Valve Ethernet/IP Protocol",
       "RFI-003: trece actuadores Delco (cuatro modulantes y nueve on/off) llegaron sin conexión EtherNet/IP. "
       "Propone controlarlos por 4-20 mA con módulos 5069-IF8 y 5069-OF4, en 7 a 14 días.",
       ["RFI-003 Modulating Actuators 4- 20mA.docx"])

doc.add_heading("Jueves 24 de septiembre", level=2)
correo("09:37", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "Project report (Procurement and Fabrication) WEEK 38",
       "Informe de la semana 38 (14 al 20-Sep) con fotos: instalación y alineación de spools con válvulas e "
       "instrumentos, e instalación del filtro de cartucho RO y de la bomba de alta. SWRO 82 %, CIP 71 %.",
       ["25007 TALTAL PROGRESS REPORT (WEEK 38).pdf", "Copy of Procurement tracking - BW Water 2906.xlsx"])
fotos([("09_W38_equipos_exteriores.jpg", "Equipos del lado exterior del contenedor; el estanque de HDPE todavía embalado. Informe semanal 38."),
       ("10_W38_motor_y_filtro.jpg", "Motor de la bomba de alta y filtro de cartucho RO dentro del contenedor. Informe semanal 38."),
       ("11_W38_bomba_bajo_recipientes.jpg", "Bomba de alta presión instalada bajo los recipientes de presión. Informe semanal 38.")])
correo("09:40", "Resumen automático de la reunión semanal (Read AI)", "Weekly Coordination Call, 24-Sep",
       "Spools modificados con hidrostática aprobada por el inspector; FAT planificado del 5 al 7 de octubre; "
       "acción para BW: entregar las isométricas actualizadas de los spools 004 y 008. El acta completa exige "
       "cuenta en Read AI y no circuló minuta formal.")
correo("10:20", "Victor Gutiérrez (ADASA) a Eduardo Yamauchi", "RE: RFI-003",
       "ADASA acepta el control por 4-20 mA y deja escrito que no asume costo ni plazo.",
       ["RFI-003 Modulating Actuators 4- 20mA (ADASA).pdf"])
correo("12:00", "Victor Gutiérrez (ADASA) a Fitri Indriyani", "RE: DOCUMENT SUBMISSION 25007-0096",
       "Si los spools 004 y 008 modificados cambian el Piping Layout, emitir la Rev F; sin más comentarios. Pide "
       "las isométricas de los spools modificados.")
correo("22:34", "Mohd Adnin (BW Water) a Victor Gutiérrez", "RE: Project report WEEK 38",
       "Todas las hidrostáticas de alta, que son punto de detención del ITP, están hechas según su tracker; las de "
       "PVC de baja son solo de testigo y se hacen junto con la instalación de equipos. Pregunta si ADASA quiere a "
       "BV en ellas.", ["SSD Testing Progress Tracker Rev.0_5696.pdf"])

doc.add_heading("Viernes 25 de septiembre", level=2)
correo("06:42", "Fitri Indriyani (BW Water) a ADASA", "TALTAL: DOCUMENT SUBMISSION 25007-0098",
       "Procedimiento del FAT del módulo Rev B, dentro del plazo que fijó el N40.")
correo("10:03", "Victor Gutiérrez (ADASA) a Mohd Adnin y Eduardo Yamauchi", "RE: Project report WEEK 38",
       "No se requiere a BV en las hidrostáticas de PVC de baja; ADASA evaluará una visita de avance del montaje.")
correo("12:00", "Jaime Martínez (BV Chile) a Victor Gutiérrez", "Turbocharger spool offset … 23 de septiembre",
       "Informe IR018: el spool DA-SSD-DN100-09-004 se ensayó a 120 barG, satisfactorio. La foto muestra el spool "
       "probado montado en el skid y no en banco aparte, como el 008. El mismo spool ya figuraba ensayado y "
       "conforme en el informe IR013 del 9-Sep.",
       ["IR018-ADASA-BVM-23092026.pdf", "Annex 1 (23092026).pdf", "Taltal Hydrotest Report BV W 23SEP 2.pdf"])
fotos([("08_IR018_spool_004_prueba.jpg", "23-Sep 09:52: prueba del spool DA-SSD-DN100-09-004 con el spool montado en el skid. Informe IR018.")])

doc.add_heading("Lunes 28 de septiembre", level=2)
correo("11:26", "Victor Gutiérrez (ADASA) a Jaime Martínez (BV Chile)", "RE: Turbocharger spool offset",
       "La semana del 28 es solo de montaje: pide una visita el jueves o el viernes para un informe de avance. "
       "Estima el FAT el 7-Oct en el mejor caso o la semana del 12.")
correo("11:36", "Jaime Martínez (BV Chile) a Victor Gutiérrez", "RE: Turbocharger spool offset",
       "Acusa recibo y lo traspasa a BV Malasia. No hay registro posterior de esa visita.")
correo("14:11", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "Weekly Engineering Report",
       "Estado documental semanal.", ["25007_Taltal_DDSR_2026.09.28.pdf"])
correo("14:17", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "RE: Weekly Engineering Report",
       "Responde al pedido de Victor de fotos del skid RO: las últimas que tiene son del 21-Sep y pedirá nuevas a "
       "la fábrica.")

doc.add_heading("Martes 29 de septiembre", level=2)
correo("04:32", "Fitri Indriyani (BW Water) a ADASA", "TALTAL: DOCUMENT SUBMISSION 25007-0099",
       "Addendum Rev A del informe de cálculo estructural UHPRO. El formulario viene rotulado 0098 y pide "
       "devolución al 2-Oct.")
correo("09:21", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "Project report (Procurement and Fabrication) WEEK 39",
       "Informe de la semana 39 (21 al 27-Sep): spools 004 y 008 modificados y montados al turbocargador de "
       "alimentación; filtro de cartucho y bomba de alta instalados; sigue el PVC exterior y el posicionamiento de "
       "equipos. SWRO 87 %, CIP 84 %. Anuncia el tracker y no lo adjunta.",
       ["25007 TALTAL PROGRESS REPORT (WEEK 39).pdf"])
fotos([("16_W39_posicionamiento_exterior.jpg", "Posicionamiento de equipos exteriores, con grúa horquilla. Informe semanal 39."),
       ("12_W39_turbo_spools_modificados.jpg", "Turbocargador con los spools modificados y su instrumentación. Informe semanal 39."),
       ("13_W39_pvc_y_motor.jpg", "Cañería de PVC con válvulas junto al motor de la bomba, aún cubierto. Informe semanal 39."),
       ("14_W39_filtro_y_tablero.jpg", "Filtro de cartucho, cañería de PVC y tablero de instrumentos en la pared del contenedor. Informe semanal 39."),
       ("15_W39_colectores_pvc.jpg", "Colectores de PVC conectados a los recipientes de presión. Informe semanal 39.")])

doc.add_heading("Miércoles 30 de septiembre", level=2)
correo("14:37", "Jorge Guevara (ADASA) a Luis Rivera y Victor Gutiérrez", "RV: Orden de Compra Nro I-333",
       "Reenvía la OC I-333 de repuestos para dos años del módulo, emitida por Abastecimiento a las 14:11.", ["OC-I-333.pdf"])
correo("14:43", "Jorge Guevara (ADASA) a Matcargo", "RE: QTMC2450 Cotización Shipping Korea del Sur",
       "Pide unificar las monedas de la cotización del flete marítimo de las membranas LG desde Busan (dos pallets, "
       "carga consolidada).")
correo("14:50", "Victor Gutiérrez (ADASA) a Eduardo Yamauchi", "PO Spare Parts",
       "Remite la OC I-333 de repuestos.")
correo("15:29 y 16:50", "Matcargo y Jorge Guevara", "RE: QTMC2450",
       "Matcargo pide la factura comercial para asegurar la carga; Jorge responde que el contrato agrupa las "
       "membranas en una sola línea y no puede dar un valor.")
correo("21:44", "Eduardo Yamauchi (BW Water) a Victor Gutiérrez", "Re: PO Spare Parts",
       "Agradece la orden: «we will review and revert back».")

doc.add_heading("Jueves 1 de octubre", level=2)
correo("04:26", "Fitri Indriyani (BW Water) a ADASA", "TALTAL: DOCUMENT SUBMISSION 25007-0100",
       "Valve List Rev 0, emitida para construcción; pide devolución al 4-Oct.")
correo("08:47", "Victor Gutiérrez (ADASA) a Fitri Indriyani y Eduardo Yamauchi", "RE: DOCUMENT SUBMISSION 25007-0096",
       "Pide que respondan el hilo de la 0096 (Rev F del Piping Layout e isométricas de los spools). Sin respuesta al 5-Oct.")
correo("11:12", "Jaime Martínez (BV Chile) a Luis Rivera y Victor Gutiérrez", "Servicios de inspección fábrica BV Malasia",
       "Pide definir cómo facturar julio y agosto: lista una visita en julio y seis en agosto, y pregunta si manda "
       "un estado de pago o si ADASA emitirá una OC global o una por visita. La OC 836492 existe desde el 14-Jul y "
       "los informes de BV suman nueve jornadas en esos dos meses, no siete.")
correo("15:08", "Karina Robles (Matcargo) a Jorge Guevara y Luis Rivera", "QUOTE MC1098",
       "Cotización del flete de membranas en pesos chilenos; la tarifa se mantiene y falta el valor de la "
       "mercadería para el seguro.", ["Propuesta Comercial Matcargo COT MC1098 QTMC2450.pdf"])
correo("sin hora", "Ronald Pellejero, licitación 13037", "RV: listado personal licitación 13037",
       "En Taltal, IEC trabaja 60 días desde el lunes 5-Oct en el módulo de segundo paso; la primera partida es la "
       "malla de tierra, del 5 al 12-Oct, y pide despejar el sector.")

doc.add_heading("Viernes 2 de octubre", level=2)
correo("11:29", "Victor Gutiérrez (ADASA) a Eduardo Yamauchi y Fitri Indriyani", "Transmittal N41",
       "Devuelve en Código 3 el procedimiento del FAT Rev B: la mayoría de las observaciones de la Rev A siguen "
       "abiertas. Trae solo cuatro de los formularios de registro y ninguno con valores de aceptación, y las "
       "referencias no citan código ni revisión. Cerró el punto de las hidrostáticas como requisito previo.",
       ["TRANSMITTAL N41 ADASA-BW_WATER.pdf", "List of observations to Module Factory Acceptance Test Procedure Rev B.pdf"])
correo("12:15", "Karina Robles (Matcargo) a Jorge Guevara y Luis Rivera", "RE: QUOTE MC1098",
       "Programación de salidas desde Busan y agente en origen (Green Globe Line).")

doc.add_heading("Lunes 5 de octubre", level=2)
correo("02:57", "Mohd Adnin (BW Water) a Bureau Veritas", "25007 TALTAL - Request to witness inspection 010",
       "Pide al inspector el jueves 8 y el viernes 9 de octubre para la instalación de equipos. No es el FAT.",
       ["Inspection Request (010) Day 1.pdf", "Day 2.pdf"])

doc.add_heading("4. Avance por actividad, semanas 37 a 39", level=1)
p("Porcentajes declarados por BW Water en sus informes semanales, en el orden SWRO / CIP / antiincrustante.", size=10)
tabla(["Actividad", "Sem. 37 (al 13-Sep)", "Sem. 38 (al 20-Sep)", "Sem. 39 (al 27-Sep)"],
      [["Documentación de ingeniería", "85 / 100 / 100", "85 / 100 / 100", "85 / 100 / 100"],
       ["Compra de membranas RO", "80 / – / –", "80 / – / –", "80 / – / –"],
       ["Fabricación de spools", "95 / 95 / –", "95 / 95 / –", "100 / 100 / –"],
       ["Montaje de spools", "35 / 0 / 100", "75 / 15 / 100", "90 / 80 / 100"],
       ["Montaje de válvulas", "15 / 0 / 100", "75 / 0 / 100", "90 / 60 / 100"],
       ["Montaje de instrumentos", "15 / 0 / –", "15 / 0 / –", "90 / 60 / –"],
       ["Montaje eléctrico", "35 / 0 / –", "75 / 0 / –", "80 / 70 / –"],
       ["Hidrostática en taller", "75 / 55 / 100", "85 / 100 / 100", "100 / 100 / 100"],
       ["Inspección dimensional final", "0 / 0 / 0", "0 / 0 / 0", "0 / 0 / 0"],
       ["Punch list", "0 / 0 / 0", "0 / 0 / 0", "0 / 0 / 0"],
       ["Limpieza final y embalaje", "0 / 0 / 0", "0 / 0 / 0", "0 / 0 / 0"],
       ["Total", "77 / 68 / 64", "82 / 71 / 64", "87 / 84 / 64"]],
      anchos=[5.5, 3.5, 3.5, 3.5])
p("El antiincrustante figura con todas sus partidas en 100 % y un total de 64 % las tres semanas; el informe no "
  "explica la diferencia. Las tres partidas de cierre, que son las que preceden al FAT y al embarque, no tienen "
  "ningún avance declarado.")

doc.add_heading("5. Qué se atrasó y qué preocupa", level=1)
vineta("el procedimiento volvió dos veces en Código 3 (N40 y N41) y sin él aprobado el FAT no abre. Ninguna de "
       "las dos fechas que circularon, del 5 al 7-Oct en la reunión del 24 y el 7 o el 12-Oct en el correo del 28, "
       "llegó por escrito de BW. La solicitud que BW mandó a BV para el 8 y 9-Oct es de instalación de equipos.",
       "El FAT no tiene fecha posible esta semana: ")
vineta("el plazo de la Cláusula 27 de la BAE venció el 3-Ago y el embarque declarado del 28-Sep no ocurrió. A "
       "0,2 % diario (Cláusula 43.1 letra b), los 63 días suman 12,6 % y el tope de 15 % de la Cláusula 43.4 se "
       "alcanza el sábado 17 de octubre. El cálculo usa la adjudicación del 7-Oct-2025; antes de cursar la multa "
       "hay que confirmarla en la Notificación de Adjudicación.", "Plazo contractual: ")
vineta("el spool 004 se probó montado en el skid, aunque ADASA pidió el 16-Sep el reensayo fuera del contenedor; "
       "figura ensayado dos veces sobre las mismas juntas (IR013 del 9-Sep e IR018 del 23-Sep) sin explicación; "
       "y las isométricas de los spools modificados y la Rev F del Piping Layout no han llegado pese al pedido "
       "del 24-Sep y al recordatorio del 1-Oct.", "Spools del turbocargador: ")
vineta("inspección dimensional, punch list, limpieza y embalaje en 0 %, y sin fotos del módulo desde el 21-Sep.",
       "Cierre de taller sin arrancar: ")
vineta("la compra figura en 80 % pendiente de LG desde antes del período, y el flete desde Busan no se puede "
       "asegurar porque nadie ha fijado el valor de la carga.", "Membranas: ")
vineta("van 19 de las 25 jornadas contratadas, todas de acompañamiento. Si BV asiste el 8 y 9-Oct, quedan cuatro "
       "para las siete del FAT y faltan tres (USD 2.931 netos). BV además pidió facturar como si no existiera OC.",
       "Bureau Veritas: ")
vineta("las revisiones de la E96 y la E97 vencieron el 1 y el 2-Oct; Victor respondió la E96 en el hilo del "
       "correo, pero falta el transmittal.", "Plazos de ADASA: ")
vineta("en el buzón del período no hay un solo correo sobre el paquete de izaje, el endoso del cálculo sísmico "
       "ni los planos de taller oficiales de los spools, tres compromisos de BW que ya estaban vencidos.",
       "Sin noticias: ")

doc.add_heading("6. Plan propuesto", level=1)
tabla(["N°", "Acción", "Responsable", "Fecha"],
      [["1", "Transmittal N42 con E96 y E97 (vencidas), E99 y E100", "ADASA (Luis)", "Mié 7-Oct; E100 a más tardar el 13"],
       ["2", "Pedir por escrito a BW la fecha del FAT, la fecha de embarque, el informe de la semana 40 y fotos actuales del skid", "ADASA (Victor)", "Mar 6-Oct"],
       ["3", "Fijar a BW la Rev C del procedimiento FAT con formularios completos y valores de aceptación; el FAT abre solo con el procedimiento aprobado", "ADASA (Luis)", "Rev C al vie 9-Oct"],
       ["4", "Pedir las isométricas de los spools 004 y 008, la Rev F del Piping Layout y la explicación del doble ensayo del 004 y de su prueba montado en el skid", "ADASA (Luis)", "Mar 6-Oct, respuesta al vie 9-Oct"],
       ["5", "Decidir si BV asiste el 8 y 9-Oct (BV-29). Recomendación: una sola jornada, o ninguna, para no comerse las del FAT", "ADASA (Victor)", "Mié 7-Oct"],
       ["6", "Tramitar con Abastecimiento el aumento de la OC 836492 por al menos tres jornadas (BV-30)", "ADASA (Luis y Jorge Guevara)", "Antes de fijar el FAT"],
       ["7", "Responder a BV la facturación citando la OC 836492 y cerrando julio y agosto con nueve jornadas (BV-28)", "ADASA (Luis)", "Mié 7-Oct"],
       ["8", "Revisar la Notificación de Adjudicación y decidir la notificación de multa antes de que se alcance el tope", "ADASA (Victor)", "Antes del 17-Oct"],
       ["9", "Fijar el valor asegurable de las membranas (precio unitario de BW o factura de LG) y cerrar el flete con Matcargo", "ADASA (Jorge Guevara)", "Esta semana"],
       ["10", "Confirmar que BW acepta la OC I-333 de repuestos", "ADASA (Victor)", "Esta semana"],
       ["11", "Coordinar con IEC y Socoval el despeje del sector y la llegada del módulo cuando haya fecha de embarque", "ADASA (Jorge Valdés)", "Con la fecha de embarque"]],
      anchos=[1, 9.5, 3.5, 3.5])

# ---------------------------------------------------------------- cierre técnico
fijar_idioma_documento()
apply_core_properties(doc, title="Avance del módulo de salmuera en Penang, 17-Sep al 5-Oct-2026",
                      author="Luis Rivera González", language=LANG)
doc.core_properties.comments = ""
doc.core_properties.keywords = ""
doc.save(OUT)
fix_app_xml(OUT, company="Aguas Antofagasta")
print("Generado:", OUT)
