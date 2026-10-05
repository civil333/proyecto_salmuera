"""
Tabla Comparativa de Hitos — Programa Base vs Actualizado vs Real
Proyecto: 12803 — Modulo de Salmuera Taltal | Contrato: C-4300
Generado por ADASA | Fecha: 23-Mar-2026

Programa Base  : "Project TalTal-Preliminary Taltal Schedule.pdf"  (Oct-2025, schedule ORIGINAL)
Programa Actual: "05.03.26_12803_Taltal Water Treatment Plant.pdf" (05-Mar-2026, catch-up)
Fechas Reales  : TM N1-N11 (16-Dic-2025 a 17-Mar-2026)

NOTA: "Taltal water treatment plant base schedule 090226.pdf" (09-Feb-2026) fue un schedule
intermedio presentado por BW Water que ADASA rechazo. No se usa como base de medicion.
"""

import os
from datetime import date
from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter

TODAY = date(2026, 3, 23)   # fecha de referencia para calcular vencimientos

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "TABLA-COMPARATIVA-HITOS.xlsx")

# ---------------------------------------------------------------------------
# Paleta de colores
# ---------------------------------------------------------------------------
COLOR_HEADER_BG    = "1F3864"   # azul oscuro ADASA
COLOR_SECCION_BG   = "2F4F7F"   # azul medio
COLOR_SECCION_FG   = "FFFFFF"
COLOR_COL_HEADER   = "D9E1F2"   # azul muy claro
COLOR_ATRASO       = "FFCCCC"   # rojo claro
COLOR_OK           = "CCFFCC"   # verde claro
COLOR_PENDIENTE    = "FFFACD"   # amarillo claro
COLOR_ALT_ROW      = "F5F7FA"   # gris muy claro
COLOR_RECHAZADO_FG = "C00000"
COLOR_A_REVISAR_FG = "E07000"
COLOR_APROBADO_N_FG= "1F6CC0"
COLOR_APROBADO_FG  = "196619"
COLOR_WHITE        = "FFFFFF"

# ---------------------------------------------------------------------------
# Datos: (num, categoria, hito, base_oct25, actualizado_mar26, fecha_real, estado, obs)
#
# base_oct25        : fecha del programa ORIGINAL Oct-2025 (Preliminary Schedule) — col D
#                     Seccion C procurement: se usa Finish del Datasheet como proxy,
#                     ya que el preliminary NO tiene fechas de PO individuales.
# actualizado_mar26 : fecha del programa Mar-2026 (05.03.26) — col E
#                     Seccion B ingenieria: None (Mar-2026 no desglosa por documento)
# fecha_real        : fecha real de entrega/cumplimiento — col F (None = "Pendiente")
# Atraso (col H)    : calculado como (fecha_real o TODAY si vencido) - base_oct25
# ---------------------------------------------------------------------------

HITOS = [
    # =========================================================================
    # A. HITOS GENERALES DEL PROYECTO
    # Fuente base: PROGRAMA-PRELIMINAR-BWWATER.md (Preliminary Taltal Schedule, Oct-2025)
    # =========================================================================
    ("A", "A. HITOS GENERALES DEL PROYECTO", None, None, None, None, None),

    (1,  "A", "Adjudicacion / NTP",
     date(2025,10,7),  # Preliminary: 07-Oct-2025
     date(2025,10,7),  # Mar-2026: sin cambio
     date(2025,10,7),  # Real: cumplido
     "Cumplido",
     "Inicio del contrato C-4300 con BW Water"),

    (2,  "A", "KOM (Kick-Off Meeting)",
     date(2025,10,9),  # Preliminary: 09-Oct-2025
     date(2025,10,9),  # Mar-2026: sin cambio
     date(2025,10,9),  # Real: cumplido
     "Cumplido",
     "Reunion de inicio del proyecto"),

    (3,  "A", "Fin Ingenieria — General",
     date(2025,12,30), # Preliminary: 30-Dic-2025 (barra General 61 dias)
     date(2026,2,20),  # Mar-2026: declara completado 20-Feb (cuestionado por ADASA)
     None,
     "Pendiente",
     "Base Oct-2025: 30-Dic-2025. Mar-2026 declara completado 20-Feb pero ~15 docs sin "
     "entregar y 14 con obs. abiertas al 23-Mar-2026"),

    (4,  "A", "Fin Ingenieria — Equipos y Compras",
     date(2026,1,5),   # Preliminary: 05-Ene-2026 (Engineering E&P Related, 65 dias total)
     date(2026,7,9),   # Mar-2026: extendido a 09-Jul-2026 (198 dias)
     None,
     "Pendiente",
     "Base Oct-2025: 05-Ene-2026 (65 dias). Mar-2026: 09-Jul-2026 (198 dias). "
     "+185 dias vs base (+205%). Schedule Feb-2026 rechazado: proponia 24-Abr-2026"),

    (5,  "A", "Fin Fabricacion (Penang)",
     date(2026,7,31),  # Preliminary: 31-Jul-2026 (181 dias desde 02-Ene)
     date(2026,8,1),   # Mar-2026: 01-Ago-2026 (+1 dia)
     None,
     "Pendiente",
     "Depende de aprobacion de Valve List Rev D, Piping Layout Rev B y Feed Turbocharger"),

    (6,  "A", "FAT — Prueba en Fabrica",
     date(2026,7,30),  # Preliminary: 30-31 Jul-2026 (2 dias)
     date(2026,7,25),  # Mar-2026: reinstaurado 25-Jul a 01-Ago-2026 (7 dias)
     None,
     "Pendiente",
     "Base Oct-2025: 30-31 Jul (2 dias). Eliminado en prog. Feb-2026 (rechazado). "
     "Reinstaurado en Mar-2026 (7 dias). ADASA debe confirmar presencia formal"),

    (7,  "A", "EXW / Listo para Embarque (Malasia)",
     date(2026,8,3),   # Preliminary: 03-Ago-2026 (milestone 0 dias, Malaysia)
     date(2026,8,2),   # Mar-2026: 02-03 Ago-2026 EXW Malasia
     None,
     "Pendiente",
     "Base Oct-2025: 03-Ago-2026 EXW Malasia. Prog. Feb-2026 (rechazado) indicaba "
     "shipping a Florida — no conforme contrato. Mar-2026 corrige a EXW Malasia"),

    (8,  "A", "Supervision Comisionamiento en Sitio",
     date(2026,9,26),  # Preliminary: 26-Sep a 16-Oct-2026 (21 dias)
     date(2026,9,18),  # Mar-2026: 18-Sep a 08-Oct-2026 (21 dias, adelantado 8 dias)
     None,
     "Pendiente",
     "Base Oct-2025: 26-Sep-2026 (21 dias). Eliminado en Feb-2026. "
     "Reinstaurado en Mar-2026: 18-Sep a 08-Oct-2026"),

    (9,  "A", "Capacitacion Operadores + Cierre Documental",
     date(2026,10,17), # Preliminary: 17-Oct-2026 (capacitacion 9d) + 26-Oct (cierre 30d)
     date(2026,10,9),  # Mar-2026: 09-Oct-2026 (capacitacion) + 18-Oct (cierre)
     None,
     "Pendiente",
     "Base Oct-2025: capacitacion 17-25 Oct + cierre 26-Oct a 24-Nov. "
     "Eliminado en Feb-2026. Reinstaurado en Mar-2026"),

    # =========================================================================
    # B. INGENIERIA — DOCUMENTOS CLAVE
    # base_oct25: fecha Finish del documento segun Preliminary Taltal Schedule
    # actualizado_mar26: None — el prog. Mar-2026 no desglosa documentos individuales
    #                    (solo barra general Engineering, fase General "completada" 20-Feb)
    # =========================================================================
    ("B", "B. INGENIERIA — DOCUMENTOS CLAVE", None, None, None, None, None),

    (10, "B", "Process Calculation",
     date(2025,10,28), # Preliminary: 07-Oct a 28-Oct-2025 (16 dias)
     None,             # Mar-2026: sin fecha individual (barra general)
     date(2025,12,16), # Real: E3 (16-Dic-2025)
     "Codigo 2 — Aprobado con notas (TM N2)",
     "Base: 28-Oct-2025. 1a entrega: E3 (16-Dic-2025). "
     "Atraso entrega: +49 dias vs base. Aprobado con obs. menores en TM N2"),

    (11, "B", "P&ID (Diagrama P&I)",
     date(2025,12,12), # Preliminary: 10-Oct a 12-Dic-2025 (46 dias)
     None,
     date(2026,3,11),  # Real: Rev B aprobada E17 (11-Mar-2026, TM N9)
     "Codigo 2 — Aprobado con notas (TM N9)",
     "Base: 12-Dic-2025. Rev A: E1 (10-Dic, TM N1 Code 3, 13 obs). "
     "Rev B aprobada: E17 (11-Mar-2026, TM N9). Atraso cierre: +89 dias"),

    (12, "B", "Plant Control Philosophy",
     date(2025,12,23), # Preliminary: 18-Nov a 23-Dic-2025 (26 dias)
     None,
     date(2026,3,6),   # Real: 1a entrega E14 (06-Mar-2026)
     "Codigo 3 — A revisar (TM N7)",
     "Base: 23-Dic-2025. 1a entrega: E14 (06-Mar-2026). Atraso: +73 dias. "
     "UPS 30 min vs 8h requeridas. Modbus TCP Memory Map ausente. Rev B pendiente"),

    (13, "B", "Instrument List",
     date(2025,12,26), # Preliminary: 03-Nov a 26-Dic-2025 (40 dias, incl. vendor docs)
     None,
     date(2026,3,9),   # Real: Rev B (E16, 09-Mar-2026) — 1a con VT y Pt-100 motores
     "Codigo 3 — A revisar (TM N8)",
     "Base: 26-Dic-2025. Rev A: E1 (10-Dic, incomplete). Rev B: E16 (09-Mar, TM N8). "
     "Rangos conductividad insuficientes (0-20 mS/cm vs 65-133 mS/cm esperado). Rev C pendiente"),

    (14, "B", "IO List",
     date(2025,12,11), # Preliminary: 13-Nov a 11-Dic-2025 (21 dias)
     None,
     date(2026,3,12),  # Real: Rev B E18 (12-Mar-2026, TM N10)
     "Codigo 2 — Aprobado con notas (TM N10)",
     "Base: 11-Dic-2025. Rev A: E1 (10-Dic, TM N3 Code 3). "
     "Rev B: E18 (12-Mar-2026, TM N10 Code 2). Faltan 7 puntos de IL Rev B. Atraso: +91 dias"),

    (15, "B", "Valve List",
     date(2025,12,26), # Preliminary: 03-Nov a 26-Dic-2025 (40 dias, incl. vendor docs)
     None,
     date(2026,3,13),  # Real: Rev C E19 (13-Mar-2026) — ultima version entregada
     "Codigo 3 — A revisar (TM N11)",
     "Base: 26-Dic-2025. Rev A: E2 (16-Dic). Rev B: E13 (26-Feb) Code 4 RECHAZADO. "
     "Rev C: E19 (13-Mar, TM N11 Code 3). 2 nuevos TAGs duplicados. Rev D pendiente"),

    (16, "B", "Control System Architecture",
     date(2025,11,3),  # Preliminary: 14-Oct a 03-Nov-2025 (15 dias)
     None,
     date(2026,3,12),  # Real: Rev C E18 (12-Mar-2026, TM N10)
     "Pendiente codigo final (TM N10)",
     "Base: 03-Nov-2025. Rev A: E1 (10-Dic). Rev C: E18 (12-Mar-2026). "
     "UPS capacidad y Modbus TCP pendientes. Atraso entrega: +129 dias"),

    (17, "B", "Equipment Layout",
     date(2025,12,5),  # Preliminary: 07-Oct a 05-Dic-2025 (44 dias)
     None,
     date(2026,2,20),  # Real: E12 (20-Feb-2026, TM N5)
     "Codigo 3 — A revisar (TM N5)",
     "Base: 05-Dic-2025. 1a entrega: E12 (20-Feb-2026). Atraso: +77 dias. "
     "CIP externo confirmado pero footprint 11,150 mm excede 3,500 mm maximo (TM N5)"),

    (18, "B", "Piping Layout",
     date(2025,12,30), # Preliminary: 19-Nov a 30-Dic-2025 (30 dias)
     None,
     date(2026,3,6),   # Real: E14 (06-Mar-2026, TM N7)
     "Codigo 3 — A revisar (TM N7)",
     "Base: 30-Dic-2025. 1a entrega: E14 (06-Mar-2026). Atraso: +66 dias. "
     "CIP-dosing separados 11,150 mm (3x el limite). Rev B prereq. de Grounding/Instr. Layout"),

    (19, "B", "A/C Thermal Calculation",
     date(2025,11,28), # Preliminary: 21-Oct a 28-Nov-2025 (29 dias)
     None,
     date(2026,3,6),   # Real: Rev B E14 (06-Mar-2026, TM N7)
     "Codigo 3 — A revisar (TM N7)",
     "Base: 28-Nov-2025. Rev A: E7 (14-Ene-2026, TM N4 Code 3). "
     "Rev B: E14 (06-Mar-2026, TM N7 Code 3). Falta configuracion n+1 (ET 5.1.11)"),

    (20, "B", "Modbus TCP Memory Map",
     date(2026,1,5),   # Preliminary: fin Engineering E&P = 05-Ene-2026 (prereq. logico)
     None,
     None,             # Real: NUNCA ENTREGADO al 23-Mar-2026
     "Pendiente — NUNCA ENTREGADO",
     "Base: 05-Ene-2026 (fin Engineering E&P preliminar). Requerido formalmente desde "
     "TM N2 (26-Ene-2026). NUNCA entregado. Bloquea integracion SCADA ADASA"),

    # =========================================================================
    # C. COMPRAS — EQUIPOS CRITICOS
    # base_oct25: Finish del Datasheet (+GA si aplica) en Preliminary Schedule
    #             El preliminary NO tiene fechas de PO individuales; se usa DS Finish
    #             como proxy del prerequisito de compra (cuando DS aprobado → PO posible)
    # actualizado_mar26: PO inicio segun prog. Mar-2026 (05.03.26, de Alertas 10-Mar-2026)
    # fecha_real: fecha real de PO emitida (None = pendiente)
    # =========================================================================
    ("C", "C. COMPRAS — EQUIPOS CRITICOS", None, None, None, None, None),

    (21, "C", "RO Membrane (UHPRO System)",
     date(2025,10,27), # Preliminary DS SWRO System: 14-Oct a 27-Oct-2025 (10 dias)
     date(2026,2,24),  # Mar-2026: PO inicio 24-Feb-2026
     date(2026,2,24),  # Real: PO emitida 24-Feb-2026 (confirmado)
     "Codigo 1 — Aprobado",
     "DS base: 27-Oct-2025. PO real: 24-Feb-2026 (+120 dias vs base). "
     "DS aprobado sin condiciones. Primer equipo con PO emitida"),

    (22, "C", "Bomba HP de Alta Presion (RO HP Pump)",
     date(2025,11,13), # Preliminary DS HP Pump: 17-Oct a 13-Nov-2025 (20 dias)
     date(2026,3,4),   # Mar-2026: PO inicio 04-Mar-2026
     None,             # Real: pendiente verificar
     "Codigo 2 — Aprobado con notas (TM N8)",
     "DS base: 13-Nov-2025. PO programada Mar-2026: 04-10 Mar. DS Rev C aprobado con nota "
     "de potencia (93 kW nameplate vs 78.5 kW absorbida). Verificar si PO fue emitida"),

    (23, "C", "Valvulas (All Valve)",
     date(2025,12,26), # Preliminary Valve List + vendor docs: hasta 26-Dic-2025
     date(2026,3,11),  # Mar-2026: PO inicio 11-Mar-2026
     None,
     "Codigo 3 — A revisar (TM N11)",
     "DS/Lista base: 26-Dic-2025. Valve List Rev C (13-Mar) Code 3: 2 nuevos TAGs duplicados "
     "(VE-09-007, PSV-09-002) + VM-07-005 area erronea. PO BLOQUEADA hasta Rev D aprobada"),

    (24, "C", "Instrumentacion (Instrument Set)",
     date(2025,12,26), # Preliminary Instrument List + vendor docs: hasta 26-Dic-2025
     date(2026,3,11),  # Mar-2026: PO inicio 11-Mar-2026
     None,
     "Codigo 3 — A revisar (TM N8)",
     "DS/Lista base: 26-Dic-2025. IL Rev B Code 3: rangos conductividad incorrectos. "
     "IO List sin actualizar 7 puntos nuevos. PO BLOQUEADA hasta IL Rev C + IO List Rev C"),

    (25, "C", "Feed Turbocharger (SIP-09-001)",
     date(2025,11,24), # Preliminary DS 1st Stage Turbo: 28-Oct a 24-Nov-2025 (20 dias)
     date(2026,4,1),   # Mar-2026: PO inicio 01-Abr-2026
     None,
     "Codigo 2 — Aprobado con notas (TM N11)",
     "DS base: 24-Nov-2025. Era Code 4 TM N6 (coupling 1,200 psi insuficiente). "
     "Rev D mejorado a Code 2 TM N11. Confirmacion FEDCO MAWP coupling pendiente"),

    (26, "C", "Interstage Turbocharger (SIP-09-002)",
     date(2025,11,24), # Preliminary DS 2nd Stage Turbo: 28-Oct a 24-Nov-2025 (20 dias)
     date(2026,4,24),  # Mar-2026: PO inicio 24-Abr-2026
     None,
     "Codigo 2 — Aprobado con notas (TM N11)",
     "DS base: 24-Nov-2025. Code 2 condicional: FEDCO debe confirmar por escrito "
     "MAWP coupling >= 1,845 psi en servicio salmuera concentrada"),

    (27, "C", "Container (Contenedor 40')",
     date(2025,11,3),  # Preliminary DS Container: 07-Oct a 03-Nov-2025 (20 dias)
     date(2026,3,18),  # Mar-2026: PO inicio 18-Mar-2026
     None,             # Real: pendiente verificar si PO emitida
     "Codigo 1 — Aprobado",
     "DS base: 03-Nov-2025. PO programada Mar-2026: 18-Mar. DS aprobado sin condiciones. "
     "Verificar si PO fue emitida"),

    (28, "C", "RO Pressure Vessel / Tubos de Presion",
     date(2025,10,27), # Preliminary DS SWRO System: 14-Oct a 27-Oct-2025 (10 dias)
     date(2026,3,31),  # Mar-2026: PO inicio 31-Mar-2026
     None,
     "Sin DS entregado",
     "DS base: 27-Oct-2025. Ningun datasheet especifico de Pressure Vessel entregado "
     "en TM N1-N11. PO programada 31-Mar en riesgo critico de atraso"),

    (29, "C", "Bomba Antiescalante (Antiscalant Dosing Pump)",
     date(2025,11,13), # Preliminary DS Antiscalant Pump: 17-Oct a 13-Nov-2025 (20 dias)
     date(2026,4,10),  # Mar-2026: PO inicio 10-Abr-2026
     None,
     "Codigo 1 — Aprobado",
     "DS base: 13-Nov-2025. PO programada Mar-2026: 10-Abr. DS Code 1 aprobado. "
     "Sujeto a respuesta CT-001 (dosis antiescalante 0.5 ppm vs 5 ppm real estimado)"),

    (30, "C", "Bomba CIP / Flushing (CIP Flushing Pump)",
     date(2025,11,13), # Preliminary DS CIP/Flushing Pump: 17-Oct a 13-Nov-2025 (ID 82)
     date(2026,3,25),  # Mar-2026: PO inicio 25-Mar-2026
     None,
     "Codigo 2 — Aprobado con notas (TM N8)",
     "DS base: 13-Nov-2025. PO programada Mar-2026: 25-Mar. DS Code 2 TM N8. "
     "Revisar nota de potencia y motor protection antes de emision PO"),

    (31, "C", "Filtro de Cartucho CIP (CIP Cartridge Filter)",
     date(2025,11,19), # Preliminary DS CIP Cartridge Filter: 23-Oct a 19-Nov-2025 (ID 94)
     date(2026,3,23),  # Mar-2026: PO inicio 23-Mar-2026
     None,
     "Codigo 2 — Aprobado con notas",
     "DS base: 19-Nov-2025. PO programada Mar-2026: 23-Mar. "
     "Verificar estado aprobacion DS antes de emision PO"),

    (32, "C", "Tanque CIP / Flushing (CIP Flushing Tank)",
     date(2025,11,27), # Preliminary DS CIP/Flushing Tank: 31-Oct a 27-Nov-2025 (ID 106)
     date(2026,3,27),  # Mar-2026: PO inicio 27-Mar-2026
     None,
     "Codigo 1 — Aprobado",
     "DS base: 27-Nov-2025. PO programada Mar-2026: 27-Mar. DS Code 1 aprobado."),

    (33, "C", "Tanque Antiescalante (Antiscalant Dosing Tank)",
     date(2025,11,27), # Preliminary DS Antiscalant Dosing Tank: 31-Oct a 27-Nov-2025 (ID 110)
     date(2026,4,7),   # Mar-2026: PO inicio 07-Abr-2026
     None,
     "Codigo 2 — Aprobado con notas",
     "DS base: 27-Nov-2025. PO programada Mar-2026: 07-Abr. DS Code 2."),

    (34, "C", "Calentador Tanque CIP (CIP Tank Heater)",
     date(2025,11,27), # Preliminary DS CIP Tank Heater: 31-Oct a 27-Nov-2025 (ID 114)
     date(2026,3,16),  # Mar-2026: PO inicio 16-Mar-2026
     None,
     "Codigo 1 — Aprobado",
     "DS base: 27-Nov-2025. PO programada Mar-2026: 16-Mar. DS Code 1 aprobado."),

    (35, "C", "Mezclador Estatico (Static Mixer)",
     None,             # Preliminary: equipo NO listado en preliminary schedule
     date(2026,5,1),   # Mar-2026: PO inicio 01-May-2026 (01/05/2026 en formato DD/MM/YYYY)
     None,
     "Codigo 2 — Aprobado con notas",
     "Sin DS en preliminary schedule (equipo no incluido). "
     "PO programada Mar-2026: 01-May-2026. Fabricacion termina 04-Jun-2026"),

    (36, "C", "Filtro de Cartucho RO Principal (RO Cartridge Filter)",
     date(2025,11,26), # Preliminary DS Cartridge Filter: 23-Oct a 26-Nov-2025 (ID 90)
     date(2026,5,4),   # Mar-2026: PO inicio 04-May-2026
     None,
     "Codigo 2 — Aprobado con notas",
     "DS base: 26-Nov-2025. PO programada Mar-2026: 04-May. "
     "Ultima PO del proyecto — ruta critica para fabricacion y FAT"),
]

# ---------------------------------------------------------------------------
# Estilos reutilizables
# ---------------------------------------------------------------------------
def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def thin_border():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)

def wrap_center():
    return Alignment(wrap_text=True, vertical="top", horizontal="center")

def wrap_left():
    return Alignment(wrap_text=True, vertical="top", horizontal="left")

# ---------------------------------------------------------------------------
# Helpers para color de estado
# ---------------------------------------------------------------------------
def color_estado(estado_str):
    """Devuelve (font_color, bold)"""
    if estado_str is None:
        return None, False
    s = estado_str.lower()
    if "rechazado" in s or "nunca entregado" in s or "sin ds" in s:
        return COLOR_RECHAZADO_FG, True
    if "a revisar" in s:
        return COLOR_A_REVISAR_FG, False
    if "aprobado con notas" in s:
        return COLOR_APROBADO_N_FG, False
    if "aprobado" in s and "notas" not in s:
        return COLOR_APROBADO_FG, False
    if "cumplido" in s:
        return COLOR_APROBADO_FG, False
    if "pendiente" in s:
        return COLOR_A_REVISAR_FG, False
    return None, False

def color_fecha_real(fecha_real, estado_str):
    """Fondo de la celda Fecha Real"""
    if fecha_real is None:
        return COLOR_PENDIENTE
    return None  # sin fondo especial (el delta lo maneja)

def color_atraso(base, real):
    """Fondo de celda Atraso"""
    if base is None:
        return "EEEEEE"   # gris — no aplica (hito no estaba en prog. Feb-2026)
    if real is None:
        if base < TODAY:
            return COLOR_ATRASO   # ya deberia estar listo → rojo
        return COLOR_PENDIENTE    # aun no vence → amarillo
    delta = (real - base).days
    return COLOR_ATRASO if delta > 0 else COLOR_OK

def calc_delta(base, real):
    """
    Calcula atraso en dias respecto al programa base (Oct-2025 Preliminary Schedule).
    - Si real conocido: real - base
    - Si real None y base ya vencio: TODAY - base (atraso acumulado)
    - Si real None y base aun no vence: None
    - Si base None: None (hito no tiene fecha en el prog. base)
    """
    if base is None:
        return None
    if real is not None:
        return (real - base).days
    if base < TODAY:
        return (TODAY - base).days   # vencido, aun no cumplido
    return None   # pendiente, no vencido aun

# ---------------------------------------------------------------------------
# Construccion del workbook
# ---------------------------------------------------------------------------
wb = Workbook()
ws = wb.active
ws.title = "Comparativa Hitos"

# Anchos de columna
col_widths = [5, 12, 44, 20, 22, 20, 35, 14, 50]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# ---------------------------------------------------------------------------
# Titulo general (fila 1)
# ---------------------------------------------------------------------------
ws.merge_cells("A1:I1")
c = ws["A1"]
c.value = "COMPARATIVA DE HITOS — PROGRAMA BASE vs. ACTUALIZADO vs. REAL"
c.font = Font(name="Calibri", bold=True, size=14, color=COLOR_WHITE)
c.fill = fill(COLOR_HEADER_BG)
c.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 30

# Subtitulo (fila 2)
ws.merge_cells("A2:I2")
c = ws["A2"]
c.value = (
    "Proyecto 12803 — Modulo de Salmuera Taltal  |  Contrato C-4300  |  "
    "BW Water vs. ADASA  |  Actualizado: 23-Mar-2026"
)
c.font = Font(name="Calibri", italic=True, size=10, color="FFFFFF")
c.fill = fill("2A4A7F")
c.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[2].height = 20

# ---------------------------------------------------------------------------
# Encabezados de columna (fila 3)
# ---------------------------------------------------------------------------
HEADERS = [
    "N°", "Cat.", "Hito / Partida",
    "Programa Base\n(Oct-2025)\nPreliminary Schedule",
    "Programa Actualizado\n(05-Mar-2026)\n05.03.26 pdf",
    "Fecha Real\n(Entrega / Cumplimiento)",
    "Estado",
    "Atraso vs Base\n(dias)",
    "Observaciones",
]
ws.row_dimensions[3].height = 36
for col_idx, header in enumerate(HEADERS, 1):
    c = ws.cell(row=3, column=col_idx, value=header)
    c.font = Font(name="Calibri", bold=True, size=10, color="1F3864")
    c.fill = fill(COLOR_COL_HEADER)
    c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
    c.border = thin_border()

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------
ROW = 4
alt = False

for item in HITOS:
    # Fila de seccion
    if item[0] in ("A", "B", "C"):
        _, seccion_label, *_ = item
        ws.merge_cells(f"A{ROW}:I{ROW}")
        c = ws[f"A{ROW}"]
        c.value = seccion_label
        c.font = Font(name="Calibri", bold=True, size=11, color=COLOR_SECCION_FG)
        c.fill = fill(COLOR_SECCION_BG)
        c.alignment = Alignment(horizontal="left", vertical="center",
                                indent=1)
        ws.row_dimensions[ROW].height = 22
        ROW += 1
        alt = False
        continue

    num, cat, hito, base, actualizado, fecha_real, estado, obs = item

    # Fondo alternado
    row_bg = COLOR_ALT_ROW if alt else COLOR_WHITE
    alt = not alt

    # --- N° ---
    c = ws.cell(row=ROW, column=1, value=num)
    c.font = Font(name="Calibri", size=9, bold=True)
    c.fill = fill(row_bg)
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Cat ---
    c = ws.cell(row=ROW, column=2, value=cat)
    c.font = Font(name="Calibri", size=9)
    c.fill = fill(row_bg)
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Hito ---
    c = ws.cell(row=ROW, column=3, value=hito)
    c.font = Font(name="Calibri", size=10, bold=True)
    c.fill = fill(row_bg)
    c.alignment = wrap_left()
    c.border = thin_border()

    # --- Programa Base ---
    c = ws.cell(row=ROW, column=4,
                value=base.strftime("%d-%b-%Y").upper() if base else "No desglosado")
    c.font = Font(name="Calibri", size=9)
    c.fill = fill(row_bg)
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Programa Actualizado ---
    if actualizado is None and cat == "B":
        act_val = "(Mostrado como completado\nsin fecha individual)"
    elif actualizado is None:
        act_val = "No desglosado"
    else:
        act_val = actualizado.strftime("%d-%b-%Y").upper()
    c = ws.cell(row=ROW, column=5, value=act_val)
    c.font = Font(name="Calibri", size=9)
    c.fill = fill(row_bg)
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Fecha Real ---
    fr_bg = color_fecha_real(fecha_real, estado)
    if fecha_real is None:
        fr_val = "Pendiente"
        fr_fill = fill(COLOR_PENDIENTE)
    else:
        fr_val = fecha_real.strftime("%d-%b-%Y").upper()
        fr_fill = fill(row_bg)
    c = ws.cell(row=ROW, column=6, value=fr_val)
    c.font = Font(name="Calibri", size=9,
                  bold=(fecha_real is None),
                  color=(COLOR_A_REVISAR_FG if fecha_real is None else "000000"))
    c.fill = fr_fill
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Estado ---
    fc, bold = color_estado(estado)
    c = ws.cell(row=ROW, column=7, value=estado or "")
    c.font = Font(name="Calibri", size=9, bold=bold,
                  color=(fc if fc else "000000"))
    c.fill = fill(row_bg)
    c.alignment = wrap_left()
    c.border = thin_border()

    # --- Atraso ---
    delta = calc_delta(base, fecha_real)
    d_fill_hex = color_atraso(base, fecha_real)
    d_fill = fill(d_fill_hex)

    if base is None:
        delta_val = "N/A"
        d_fill = fill("EEEEEE")
    elif delta is None:
        # pendiente, base aun no vence
        delta_val = "Pendiente"
        d_fill = fill(COLOR_PENDIENTE)
    elif delta > 0 and fecha_real is None:
        # vencido y no cumplido → atraso acumulado a hoy
        delta_val = f"Vencido\n+{delta} dias"
        d_fill = fill(COLOR_ATRASO)
    elif delta > 0:
        delta_val = f"+{delta}"
        d_fill = fill(COLOR_ATRASO)
    elif delta < 0:
        delta_val = str(delta)
        d_fill = fill(COLOR_OK)
    else:
        delta_val = "0"
        d_fill = fill(COLOR_OK)
    c = ws.cell(row=ROW, column=8, value=delta_val)
    c.font = Font(name="Calibri", size=9, bold=(isinstance(delta, int) and delta > 0))
    c.fill = d_fill
    c.alignment = wrap_center()
    c.border = thin_border()

    # --- Observaciones ---
    c = ws.cell(row=ROW, column=9, value=obs or "")
    c.font = Font(name="Calibri", size=9)
    c.fill = fill(row_bg)
    c.alignment = wrap_left()
    c.border = thin_border()

    ws.row_dimensions[ROW].height = 45
    ROW += 1

# ---------------------------------------------------------------------------
# Freeze panes y filtro
# ---------------------------------------------------------------------------
ws.freeze_panes = "A4"
ws.auto_filter.ref = f"A3:I{ROW-1}"

# ---------------------------------------------------------------------------
# Hoja 2: Leyenda
# ---------------------------------------------------------------------------
ws2 = wb.create_sheet("Leyenda")
ws2.column_dimensions["A"].width = 28
ws2.column_dimensions["B"].width = 60

leyenda_rows = [
    ("CODIGOS DE REVISION (BW WATER)", ""),
    ("Codigo 1 — Aprobado",
     "El documento cumple todos los requisitos. Procurement puede proceder sin restricciones."),
    ("Codigo 2 — Aprobado con notas",
     "El documento cumple los requisitos con observaciones menores. PO puede avanzar; obs. deben cerrarse antes del FAT."),
    ("Codigo 3 — A revisar",
     "El documento tiene observaciones que deben ser corregidas. BW Water debe reenviar revision. PO bloqueada."),
    ("Codigo 4 — Rechazado",
     "El documento incumple requisitos criticos. BW Water debe corregir y reenviar. PO bloqueada hasta Code 1 o 2."),
    ("", ""),
    ("COLUMNA 'ATRASO VS BASE (DIAS)'", ""),
    ("Base de calculo",
     "El atraso se calcula SIEMPRE contra el Programa Base Oct-2025 "
     "(archivo: Project TalTal-Preliminary Taltal Schedule.pdf). "
     "NOTA: El archivo 090226.pdf (09-Feb-2026) fue un schedule intermedio rechazado por ADASA — "
     "NO se usa como base de medicion. "
     "Para ingenieria: fecha Finish del documento segun el Preliminary Schedule. "
     "Para compras: Finish del Datasheet correspondiente (proxy, el preliminary no tiene PO individuales)."),
    ("Fondo ROJO — numero positivo",
     "La fecha real de entrega supera la fecha base. +N = N dias de atraso."),
    ("Fondo ROJO — 'Vencido +N dias'",
     "El hito no se ha cumplido Y ya deberia estar completado segun la fecha base. "
     "N = dias transcurridos desde la fecha base hasta hoy (23-Mar-2026)."),
    ("Fondo VERDE",
     "La fecha real es igual o anterior al programa base (a tiempo o adelantada). "
     "Numero negativo = entregado N dias antes de lo programado."),
    ("Fondo AMARILLO — 'Pendiente'",
     "Hito aun no vencido segun programa base. La fecha programada es posterior a hoy."),
    ("Fondo GRIS — 'N/A'",
     "El hito NO tiene fecha individual en el programa base Oct-2025 (no desglosado). "
     "No aplica calcular atraso contra una fecha inexistente."),
    ("", ""),
    ("FUENTES DE DATOS", ""),
    ("Programa Base (Oct-2025)",
     "Archivo: PROGRAMA y CONTRATO/CRONOGRAMAS/2025-10 a 2026-02 PROGRAMAS INICIALES/pdf/Project TalTal-Preliminary Taltal Schedule.pdf  "
     "Analisis: PROGRAMA y CONTRATO/CRONOGRAMAS/2025-10 a 2026-02 PROGRAMAS INICIALES/md/PROGRAMA-PRELIMINAR-BWWATER.md  "
     "NOTA: 090226.pdf (09-Feb-2026) = schedule intermedio rechazado por ADASA. No es la base de medicion."),
    ("Programa Actualizado (Mar-2026)",
     "Archivo: PROGRAMA y CONTRATO/CRONOGRAMAS/2026-03-05 CATCH-UP/05.03.26_12803_Taltal Water Treatment Plant.pdf "
     "Analisis: PROGRAMA y CONTRATO/CRONOGRAMAS/_ANALISIS/2026-03-06_Analisis-Catch-Up-Schedule-Mar2026.md"),
    ("Fechas Reales",
     "Transmittales TM N1 a TM N11 (16-Dic-2025 a 17-Mar-2026). "
     "Master Deliverable Register P22-IT-06-000-002-0."),
    ("", ""),
    ("NOTA — FORMATO DE FECHAS", ""),
    ("Programa Base (Col D)",
     "El archivo 'Project TalTal-Preliminary Taltal Schedule.pdf' usa formato US (M/D/YY). "
     "Ejemplo: '1/5/26' en el PDF = 05 de Enero 2026 (NO mayo 1). "
     "Verificado: NTP = 'Tue 10/7/25' = 07-Oct-2025 (confirmado por fecha contractual)."),
    ("", ""),
    ("Generado",    "23-Mar-2026 | Script: generar_tabla_hitos.py | Proyecto: 12803 — C-4300"),
    ("Preparado por", "Luis Rivera | ADASA"),
]

for i, (key, val) in enumerate(leyenda_rows, 1):
    ck = ws2.cell(row=i, column=1, value=key)
    cv = ws2.cell(row=i, column=2, value=val)
    ws2.row_dimensions[i].height = 28
    if key and val == "":  # cabecera de seccion
        ck.font = Font(name="Calibri", bold=True, size=10, color=COLOR_WHITE)
        ck.fill = fill(COLOR_SECCION_BG)
        ws2.merge_cells(f"A{i}:B{i}")
    else:
        ck.font = Font(name="Calibri", bold=True, size=9)
        cv.font = Font(name="Calibri", size=9)
        ck.alignment = Alignment(wrap_text=True, vertical="top")
        cv.alignment = Alignment(wrap_text=True, vertical="top")
        ck.border = thin_border()
        cv.border = thin_border()

# ---------------------------------------------------------------------------
# Guardar
# ---------------------------------------------------------------------------
wb.save(OUTPUT)
print(f"Generado: {OUTPUT}")
