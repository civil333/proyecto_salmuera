"""
P22-IT-06-000-005-0 — Análisis de Cronograma BW Water
Contraste Programa vs Entregas y Revisiones
Generado: 09-Mar-2026
"""
import sys
import os
import copy

skill_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "..", "..", ".claude", "skills", "template-adasa")
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "P22-IT-06-000-005-0_Analisis-Schedule-BWW.docx")

# ---------------------------------------------------------------------------
# PASO 1: Crear documento base con portada, cajetin y TOC
# ---------------------------------------------------------------------------
crear_documento_adasa(
    titulo="ANALISIS DE CRONOGRAMA BW WATER\nCONTRASTE PROGRAMA VS ENTREGAS Y REVISIONES",
    codigo="P22-IT-06-000-005-0",
    preparado_por="Luis Rivera",
    revisado_por="Luis Rivera",
    output_filename=OUTPUT,
    incluir_toc=True,
)

doc = Document(OUTPUT)


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def add_body(doc, text):
    """Agrega párrafo Normal con Arial 12."""
    p = doc.add_paragraph(text)
    aplicar_arial_12(p)
    return p


def add_bullet(doc, text, level=0):
    """Bullet point usando párrafo Normal con prefijo."""
    p = doc.add_paragraph(f"- {text}")
    aplicar_arial_12(p)
    p.paragraph_format.left_indent = Pt(18)
    return p


def shade_cell(cell, hex_color):
    """Aplica color de fondo a una celda."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def color_cell_text(cell, hex_color):
    """Aplica color al texto de una celda."""
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.color.rgb = RGBColor.from_string(hex_color)


def apply_semaforo(table, row_idx, col_idx, status):
    """
    Aplica color de fondo a celda según estado semáforo.
    BLOQUEADO=rojo, EN RIESGO=amarillo, VIABLE=verde
    """
    cell = table.rows[row_idx].cells[col_idx]
    if status == "BLOQUEADO":
        shade_cell(cell, "FF9999")
    elif status == "EN RIESGO":
        shade_cell(cell, "FFFF99")
    elif status == "VIABLE":
        shade_cell(cell, "CCFFCC")


# ---------------------------------------------------------------------------
# SECCIÓN 1: EXECUTIVE SUMMARY
# ---------------------------------------------------------------------------
doc.add_heading("EXECUTIVE SUMMARY", level=1)

add_body(doc, (
    "Al 09 de marzo de 2026, la ingeniería de BW Water presenta un retraso acumulado "
    "de 185 días respecto a la línea base contractual. El cierre real de ingeniería se "
    "proyecta al 09 de julio de 2026, con FAT reprogramado para el 25 de julio-01 de "
    "agosto y despacho EXW Malasia el 02-03 de agosto de 2026."
))

doc.add_heading("Hallazgos Críticos", level=2)
bullets_exec = [
    "2 ítems de procurement BLOQUEADOS: Valve List (V4-Rejected) y Feed Turbocharger "
    "(V4-Rejected, acople 1200 psi vs 2000 psi requerido por ET), con PR/PO programadas "
    "para 11 de marzo y 1 de abril respectivamente.",
    "2 ítems de procurement EN RIESGO: HP Pump (potencias inconsistentes, V3) e "
    "Instrument Set (IO List + Instrument List en V3), con PR/PO para el 04 y 11 de marzo.",
    "8 observaciones críticas acumuladas sin respuesta, con antigüedad de hasta 82 días "
    "(MCC Datasheet, abierto desde 28-Ene-2026).",
    "20 documentos contractualmente obligatorios no entregados al cierre de TM N7 "
    "(33% del total de obligaciones).",
    "Control Philosophy emitida en V3 (requiere revisión) con deficiencia 16x en "
    "autonomía UPS: 30 min entregado vs 8 horas requeridas por ET §5.4.",
]
for b in bullets_exec:
    add_bullet(doc, b)

doc.add_heading("Estado Global de Procurement", level=2)
procurement_summary = [
    ("Equipo", "PR/PO Programada", "Estado Ingeniería", "Semáforo"),
    ("All Valves", "11-Mar-2026", "Valve List — V4 REJECTED", "[BLOQUEADO]"),
    ("Feed Turbocharger", "01-Abr-2026", "Feed TC — V4 REJECTED", "[BLOQUEADO]"),
    ("RO High Feed Pump", "04-Mar-2026", "HP Pump DS — V3 (potencias inconsistentes)", "[EN RIESGO]"),
    ("Instrument Set", "11-Mar-2026", "IO List — V3 / Instrument List — V3", "[EN RIESGO]"),
    ("RO Membrane", "24-Feb-2026", "Process Calc — V2-AN / P&ID — V2-AN", "[VIABLE]"),
    ("Interstage Turbocharger", "24-Abr-2026", "DS — V2-AN", "[VIABLE]"),
    ("CIP Heater", "16-Mar-2026", "Utility List — V2-AN", "[VIABLE — margen minimo]"),
]
tbl_exec = add_simple_table(doc, procurement_summary)
semaforo_map = {
    "[BLOQUEADO]": "BLOQUEADO",
    "[EN RIESGO]": "EN RIESGO",
    "[VIABLE]": "VIABLE",
    "[VIABLE — margen minimo]": "VIABLE",
}
for i, row_data in enumerate(procurement_summary[1:], start=1):
    status = semaforo_map.get(row_data[3], "")
    apply_semaforo(tbl_exec, i, 3, status)


# ---------------------------------------------------------------------------
# SECCIÓN 2: CIERRE DE INGENIERÍA — PROGRAMA VS REALIDAD
# ---------------------------------------------------------------------------
doc.add_heading("CIERRE DE INGENIERIA — PROGRAMA VS REALIDAD", level=1)

add_body(doc, (
    "El programa BW Water (revisión Mar-2026) establece el cierre de la fase de "
    "engineering al 20 de febrero de 2026. La realidad de las revisiones técnicas "
    "emitidas por ADASA muestra que, al 09 de marzo, varias disciplinas permanecen "
    "abiertas. El cierre real de ingeniería se estima en el 09 de julio de 2026, "
    "representando un atraso de 185 días respecto a la línea base."
))

ing_data = [
    ("Disciplina", "Fecha Programada (BW Schedule)", "Veredicto ADASA", "Estado Real"),
    ("Mechanical Drawing (PFD)", "05-Ene-2026", "V1 — Approved", "CERRADO"),
    ("P&ID", "27-Ene-2026", "V2-AN (requiere update)", "PARCIAL"),
    ("Process Calculation", "29-Ene-2026", "V2-AN — Approved as noted", "CERRADO"),
    ("I/O List", "29-Ene-2026", "V3 — To be revised (44 dias abierto)", "ABIERTO"),
    ("Equipment List", "29-Ene-2026", "V2-AN (discrepancias menores)", "PARCIAL"),
    ("Electrical (SLD)", "05-Feb-2026", "V1 — Approved", "CERRADO"),
    ("Control Architecture", "05-Feb-2026", "V2-AN (UPS/Modbus pendiente)", "PARCIAL"),
    ("Utility Consumption List", "16-Feb-2026", "V2-AN — Approved as noted", "CERRADO"),
    ("Control Philosophy", "20-Feb-2026", "V3 — To be revised (TM N7, 08-Mar-2026)", "ABIERTO"),
    ("MCC Datasheet", "05-Feb-2026", "No entregado (82 dias)", "NO ENTREGADO"),
    ("HP Pump Datasheet", "29-Ene-2026", "V3 — To be revised (potencias)", "ABIERTO"),
    ("Feed TC Datasheet", "01-Mar-2026", "V4 — Rejected (acople 1200 psi)", "RECHAZADO"),
    ("Valve List", "11-Feb-2026", "V4 — Rejected (tags duplicados)", "RECHAZADO"),
    ("CIP Pump Datasheet", "19-Feb-2026", "V4 — Rejected", "RECHAZADO"),
    ("Modbus TCP Memory Map", "20-Feb-2026", "No entregado (65 dias)", "NO ENTREGADO"),
    ("A/C Thermal Calculation", "20-Feb-2026", "No entregado (65 dias)", "NO ENTREGADO"),
]
add_simple_table(doc, ing_data)

add_body(doc, (
    "Nota: Los estados 'CERRADO' corresponden a documentos con veredicto V1 o V2-AN "
    "sin observaciones abiertas. Los estados 'PARCIAL' indican V2-AN con observaciones "
    "menores pendientes de confirmación. Los estados 'ABIERTO' requieren nueva revisión "
    "por parte de BW Water."
))


# ---------------------------------------------------------------------------
# SECCIÓN 3: PROCUREMENT — MÁRGENES PROGRAMADOS VS ESTADO ACTUAL
# ---------------------------------------------------------------------------
doc.add_heading("PROCUREMENT — MARGENES PROGRAMADOS VS ESTADO ACTUAL", level=1)

add_body(doc, (
    "La tabla siguiente consolida los ítems de procurement del programa BW Water "
    "(Mar-2026) con el estado actual de la ingeniería de soporte. Los ítems marcados "
    "como BLOQUEADO no pueden iniciar PR/PO hasta que BW Water resuelva las "
    "observaciones V4 emitidas en los transmittales correspondientes."
))

proc_data = [
    ("Equipo", "PR/PO Prog.", "Docs Soporte", "Veredicto", "Estado", "Accion Requerida"),
    (
        "All Valves",
        "11-Mar-2026",
        "Valve List",
        "V4 — Rejected",
        "[BLOQUEADO]",
        "BW Water debe corregir 4 TAGs duplicados (VM-09-015, VE-09-008, VE-09-009, VM-09-065) "
        "y realizar revision sistematica de unicidad en toda la Valve List. "
        "La actuacion electrica de VM-09-015 fue confirmada en Rev B (RESOLVED)."
    ),
    (
        "Feed Turbocharger",
        "01-Abr-2026",
        "Feed TC Datasheet",
        "V4 — Rejected",
        "[BLOQUEADO]",
        "BW Water debe confirmar acople 2000 psi o proveer analisis justificando desviacion del acople 1200 psi"
    ),
    (
        "RO High Feed Pump",
        "04-Mar-2026",
        "HP Pump Datasheet Rev B",
        "V3 — To be revised",
        "[EN RIESGO]",
        "BW Water debe resolver inconsistencia de potencias (diferencia entre DS y oferta tecnica)"
    ),
    (
        "Instrument Set",
        "11-Mar-2026",
        "IO List / Instrument List",
        "V3 — To be revised",
        "[EN RIESGO]",
        "BW Water debe actualizar IO List con senales VFD y completar entradas DI/DO faltantes"
    ),
    (
        "RO Membrane",
        "24-Feb-2026",
        "Process Calc / P&ID",
        "V2-AN",
        "[VIABLE]",
        "Sin bloqueo. ADASA recomienda proceder con PR/PO."
    ),
    (
        "Interstage Turbocharger",
        "24-Abr-2026",
        "Interstage TC Datasheet",
        "V2-AN",
        "[VIABLE]",
        "Sin bloqueo. Margen suficiente hasta fecha programada."
    ),
    (
        "CIP Heater",
        "16-Mar-2026",
        "Utility Consumption List",
        "V2-AN",
        "[VIABLE]",
        "Sin bloqueo. Margen minimo — confirmar que no surjan observaciones en proxima entrega."
    ),
    (
        "CIP Pump",
        "04-Mar-2026",
        "CIP Pump Datasheet",
        "V4 — Rejected (TM N6)",
        "[BLOQUEADO]",
        "BW Water debe reenviar datasheet completo. Item Rejected en TM N6."
    ),
]
tbl_proc = add_simple_table(doc, proc_data)
semaforo_col = 4
for i, row_data in enumerate(proc_data[1:], start=1):
    status_text = row_data[4]
    if "BLOQUEADO" in status_text:
        apply_semaforo(tbl_proc, i, semaforo_col, "BLOQUEADO")
    elif "EN RIESGO" in status_text:
        apply_semaforo(tbl_proc, i, semaforo_col, "EN RIESGO")
    elif "VIABLE" in status_text:
        apply_semaforo(tbl_proc, i, semaforo_col, "VIABLE")


# ---------------------------------------------------------------------------
# SECCIÓN 4: OBSERVACIONES CRÍTICAS ACUMULADAS SIN RESPUESTA
# ---------------------------------------------------------------------------
doc.add_heading("OBSERVACIONES CRITICAS ACUMULADAS SIN RESPUESTA", level=1)

add_body(doc, (
    "Las observaciones técnicas emitidas por ADASA se clasifican en Criticas (impacto "
    "directo en procurement o seguridad del proceso), Mayores (incumplen ET o Oferta "
    "Tecnica Rev1) y Menores (discrepancias formales o aclaraciones). La tabla siguiente "
    "lista las observaciones sin respuesta al 09 de marzo de 2026, ordenadas por "
    "antigüedad descendente."
))

obs_data = [
    ("Observacion", "TM Origen", "Dias Abierto", "Severidad", "Descripcion"),
    (
        "MCC Datasheet no entregado",
        "TM N3 / TM N4",
        "82 dias",
        "Critico",
        "Documento no recibido desde 28-Ene-2026. Bloquea revision de protecciones electricas y motores."
    ),
    (
        "A/C Thermal Calculation incompleta",
        "TM N2",
        "65 dias",
        "Mayor",
        "Calculo presenta solo perdidas de calor de HP Pump. Faltan contribuciones de VFDs, transformadores y MCC."
    ),
    (
        "Modbus TCP Memory Map no entregado",
        "TM N2",
        "65 dias",
        "Mayor",
        "Documento requerido por ET — Communication and Control System (MODBUS TCP/IP). Sin entrega desde TM N2."
    ),
    (
        "IO List — senales VFD y DO/DI faltantes",
        "TM N3",
        "44 dias",
        "Mayor",
        "IO List no incluye senales de control y feedback de VFDs. Impacta revision de Instrument Set."
    ),
    (
        "Valve List — TAGs duplicados",
        "TM N3 / TM N6",
        "36 dias",
        "Critico",
        "4 TAGs duplicados confirmados en Valve List. Impide cierre de revision y bloquea PR/PO All Valves."
    ),
    (
        "Feed TC — acople 1200 psi vs 2000 psi",
        "TM N6",
        "11 dias",
        "Critico",
        "ET — High-Pressure Piping and Valves requiere rating 2000 psi. Datasheet indica acople 1200 psi. V4 Rejected."
    ),
    (
        "Control Philosophy — autonomia UPS 30 min vs 8 horas",
        "TM N7",
        "0 dias",
        "Critico",
        "ET §5.4 requiere 8 horas de autonomia UPS. Control Philosophy Rev1 indica 30 minutos. Deficiencia 16x."
    ),
    (
        "Control Philosophy — UPS no cubre sistema de control",
        "TM N7",
        "0 dias",
        "Mayor",
        "Control Philosophy no confirma cobertura del sistema de control completo por UPS. Alcance ambiguo."
    ),
]
add_simple_table(doc, obs_data)

add_body(doc, (
    "Total observaciones criticas abiertas: 4 — Total observaciones mayores abiertas: 4 — "
    "Las observaciones emitidas en TM N7 (0 dias) requieren respuesta de BW Water en el "
    "proximo ciclo de revisión."
))


# ---------------------------------------------------------------------------
# SECCIÓN 5: DOCUMENTOS NO ENTREGADOS
# ---------------------------------------------------------------------------
doc.add_heading("DOCUMENTOS NO ENTREGADOS", level=1)

add_body(doc, (
    "Al cierre de TM N7 (08 de marzo de 2026), 20 documentos contractualmente "
    "obligatorios no han sido recibidos por ADASA. Esto representa el 33% del total "
    "de obligaciones de entrega de BW Water. La tabla siguiente lista los documentos "
    "pendientes con referencia ET e impacto en procurement o ingeniería."
))

nd_data = [
    ("Documento", "Referencia ET", "Impacto", "Estado"),
    ("MCC Datasheet", "ET — Motors and Electrical Equipment", "Bloquea revision electrica", "No entregado (82 dias)"),
    ("Modbus TCP/IP Memory Map", "ET — Communication and Control System", "Bloquea revision SCADA/DCS", "No entregado (65 dias)"),
    ("A/C Thermal Calculation completa", "ET — HVAC and Cooling", "Bloquea revision climatizacion", "Entregado incompleto (65 dias)"),
    ("Electrical Single Line Diagram Rev actualizada", "ET — Electrical Distribution", "Referencia para revision MCC", "No entregado"),
    ("Motor List completa", "ET — Motors and Electrical Equipment", "Cruce con IO List y MCC", "No entregado"),
    ("VFD Datasheet (HP Pump)", "ET — Variable Frequency Drives", "Procurement VFDs", "No entregado"),
    ("VFD Datasheet (CIP Pump)", "ET — Variable Frequency Drives", "Procurement VFDs", "No entregado"),
    ("Control Narrative completo", "ET — Control and Instrumentation", "Base para Control Philosophy", "No entregado"),
    ("Instrument Datasheet — Pressure Transmitters", "ET — Instrumentation", "Procurement Instrument Set", "No entregado"),
    ("Instrument Datasheet — Flow Transmitters", "ET — Instrumentation", "Procurement Instrument Set", "No entregado"),
    ("Instrument Datasheet — Level Transmitters", "ET — Instrumentation", "Procurement Instrument Set", "No entregado"),
    ("Instrument Datasheet — Temperature Elements", "ET — Instrumentation", "Procurement Instrument Set", "No entregado"),
    ("Chemical Dosing System Datasheet", "ET — Chemical Dosing", "Procurement dosificacion", "No entregado"),
    ("Cleaning System (CIP) P&ID detalle", "ET — CIP System", "Revision proceso CIP", "No entregado"),
    ("Structural/Civil Drawings", "ET — Civil and Structural", "Ingenieria basica ADASA", "No entregado"),
    ("Electrical Earthing Layout", "ET — Electrical", "Ingenieria basica ADASA", "No entregado"),
    ("HAZOP Report", "ET — Safety", "Revision seguridad proceso", "No entregado"),
    ("Pressure Relief Valve Sizing", "ET — Safety and Relief", "Revision valvulas alivio", "No entregado"),
    ("Commissioning Procedure Draft", "ET — Commissioning", "Planificacion FAT/SAT", "No entregado"),
    ("Spare Parts List (2 years)", "ET — Spare Parts", "Procurement repuestos", "No entregado"),
]
add_simple_table(doc, nd_data)


# ---------------------------------------------------------------------------
# SECCIÓN 6: HISTORIAL DE TRANSMITTALES
# ---------------------------------------------------------------------------
doc.add_heading("HISTORIAL DE TRANSMITTALES ADASA (TM N1 — N7)", level=1)

add_body(doc, (
    "ADASA ha emitido 7 transmittales entre diciembre de 2025 y marzo de 2026. "
    "La tabla siguiente consolida el historial completo con fecha de emisión, "
    "submittals revisados, cantidad de documentos y veredicto global."
))

tm_data = [
    ("TM", "Codigo", "Fecha Emision", "Submittal(s) BW Water", "Docs Revisados", "Veredicto Global"),
    ("N1", "P22-TM-09-000-001-0", "16-Dic-2025", "25007-0001 / 25007-0002", "20", "4 — Rejected"),
    ("N2", "P22-TM-09-000-002-0", "26-Ene-2026", "25007-0003 a 25007-0007", "8", "2 — Approved as noted"),
    ("N3", "P22-TM-09-000-003-0", "28-Ene-2026", "25007-0007 a 25007-0009", "23", "3 — To be revised"),
    ("N4", "P22-TM-09-000-004-0", "05-Feb-2026", "25007-0010 / 25007-0011", "4", "3 — To be revised"),
    ("N5", "P22-TM-09-000-005-1", "23-Feb-2026", "25007-0012", "1", "3 — To be revised"),
    ("N6", "P22-TM-09-000-006-0", "27-Feb-2026", "25007-0013", "9", "4 — Rejected"),
    ("N7", "P22-TM-09-000-007-0", "08-Mar-2026", "25007-0014", "4", "3 — To be revised"),
]
add_simple_table(doc, tm_data)

doc.add_heading("Distribucion de Veredictos Acumulados (al 09-Mar-2026)", level=2)
verdict_data = [
    ("Veredicto", "Cantidad Docs", "Porcentaje", "Descripcion"),
    ("V1 — Approved", "18", "29%", "Documentos cerrados sin observaciones"),
    ("V2-AN — Approved as noted", "11", "18%", "Aprobados con observaciones menores confirmadas"),
    ("V3 — To be revised", "9", "15%", "Requieren revision y reenvio por BW Water"),
    ("V4 — Rejected", "3", "5%", "Feed TC Datasheet, Valve List, CIP Pump Datasheet"),
    ("No entregados", "20", "33%", "Documentos obligatorios pendientes de primera entrega"),
    ("TOTAL OBLIGACIONES", "~61", "100%", ""),
]
add_simple_table(doc, verdict_data)


# ---------------------------------------------------------------------------
# SECCIÓN 7: CONCLUSIONES Y PRÓXIMAS ACCIONES ADASA
# ---------------------------------------------------------------------------
doc.add_heading("CONCLUSIONES Y PROXIMAS ACCIONES ADASA", level=1)

doc.add_heading("Conclusiones", level=2)
add_body(doc, (
    "El análisis del programa BW Water contrastado con las revisiones técnicas "
    "emitidas por ADASA (TM N1 a N7) revela cuatro áreas de riesgo activo:"
))
conclusiones = [
    "Procurement bloqueado en 3 ítems críticos (Valve List, Feed TC, CIP Pump) con "
    "PR/PO en ventana inmediata (11-Mar a 01-Abr-2026). Estos ítems no pueden avanzar "
    "hasta que BW Water resuelva las observaciones V4 emitidas.",
    "La disciplina de control no está cerrada al 09-Mar-2026. Control Philosophy "
    "(V3) presenta deficiencia crítica de UPS (30 min vs 8 horas) que impacta el "
    "diseño del tablero MCC, cuyo datasheet tampoco ha sido entregado.",
    "El 33% de las obligaciones documentales de BW Water no han sido recibidas, "
    "con documentos estratégicos pendientes desde hace más de 82 días (MCC Datasheet).",
    "El cierre real de ingeniería, proyectado al 09-Jul-2026, deja un margen de "
    "solo 16 días hasta el inicio del FAT (25-Jul-2026), sin buffer para iteraciones "
    "adicionales de revisión.",
]
for c in conclusiones:
    add_bullet(doc, c)

doc.add_heading("Proximas Acciones ADASA (Prioridad Decreciente)", level=2)
acciones = [
    "[URGENTE — antes del 11-Mar] Notificar formalmente a BW Water el bloqueo de "
    "PR/PO All Valves por Valve List V4 Rejected. Solicitar corrección de TAGs "
    "duplicados (VM-09-015, VE-09-008, VE-09-009, VM-09-065) y realizar revision "
    "sistematica de unicidad. La actuacion electrica de VM-09-015 fue confirmada "
    "en Rev B y no es observacion abierta.",
    "[URGENTE — antes del 11-Mar] Confirmar con BW Water plan de acción para "
    "HP Pump Datasheet (V3) e Instrument Set (IO List V3). Establecer fecha límite "
    "para nueva revisión que no bloquee PR/PO.",
    "[URGENTE — antes del 15-Mar] Emitir respuesta formal a Control Philosophy Rev1 "
    "(TM N7 emitido 08-Mar-2026). Destacar deficiencia UPS como observación crítica "
    "que requiere respuesta de BW Water en máximo 5 días hábiles.",
    "[CORTO PLAZO — antes del 20-Mar] Solicitar entrega de MCC Datasheet (82 días "
    "sin entrega) y Modbus TCP Memory Map (65 días) mediante notificación formal. "
    "Referir a cláusula de entrega de documentación técnica del contrato.",
    "[MEDIANO PLAZO] Preparar evaluación de impacto en FAT/SAT derivada del "
    "retraso de ingeniería BW Water. Documentar como P22-CT (Consulta Técnica) si "
    "corresponde ajuste contractual de plazo.",
    "[MONITOREO CONTINUO] Actualizar Document Status Register (P22-IT-06-000-002-0) "
    "con cada nueva entrega de BW Water. Mantener README.md actualizado con "
    "métricas por entrega.",
]
for i, a in enumerate(acciones, start=1):
    p = doc.add_paragraph(f"{i}. {a}")
    aplicar_arial_12(p)
    p.paragraph_format.left_indent = Pt(18)

# ---------------------------------------------------------------------------
# GUARDAR
# ---------------------------------------------------------------------------
doc.save(OUTPUT)
print(f"Documento generado: {OUTPUT}")
