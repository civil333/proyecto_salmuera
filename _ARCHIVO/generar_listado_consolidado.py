"""
Listado Consolidado de Equipos, Valvulas e Instrumentos
Modulo de Salmuera Taltal — P22
Datos hardcoded desde:
  Area 06: P22-LI-06-005-001, P22-LI-06-006-002, P22-LI-06-008-001
  Area 09: P22-LI-09-005-001 Rev B, P22-LI-09-005-002 Rev C, P22-LI-09-008-003 Rev B
"""
import os
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "LISTADO-CONSOLIDADO-EVI.xlsx")

# ─── Styles ──────────────────────────────────────────────────────────────────
HEADER_FILL = PatternFill("solid", fgColor="BFBFBF")
A06_FILL    = PatternFill("solid", fgColor="FFFFFF")
A09_FILL    = PatternFill("solid", fgColor="DCE8F5")
ADASA_FILL  = PatternFill("solid", fgColor="D6F4D6")
BWW_FILL    = PatternFill("solid", fgColor="D6E8F4")
DUPLIC_FILL = PatternFill("solid", fgColor="FFD9D9")
NOTE_FILL   = PatternFill("solid", fgColor="FFF2CC")

THIN = Side(style="thin")
THIN_BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def apply_header(ws, headers):
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=1, column=col, value=h)
        c.fill = HEADER_FILL
        c.font = Font(bold=True, size=10)
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = THIN_BORDER
    ws.row_dimensions[1].height = 25


def write_row(ws, row_num, data, fill):
    for col, value in enumerate(data, 1):
        c = ws.cell(row=row_num, column=col, value=value)
        c.fill = fill
        c.font = Font(bold=(col == 1), size=10)
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = THIN_BORDER


def color_suministro(ws, row_num, col_idx, suministro):
    c = ws.cell(row=row_num, column=col_idx)
    c.fill = ADASA_FILL if suministro == "ADASA" else BWW_FILL


def set_col_widths(ws, widths):
    for col, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(col)].width = w


# ─── EQUIPOS ─────────────────────────────────────────────────────────────────
# TAG | Sistema | Descripcion | Fabricante | Modelo | Capacidad/Potencia | Suministro

EQUIPOS_06 = [
    ("TK-06-001",     "Area 06", "Estanque de Salmuera",                        "-",             "PRFV",                              "Vol: 10,000 L | Ø2,600 mm × H2,600 mm",           "ADASA"),
    ("TK-06-002",     "Area 06", "Fosa Drenajes",                               "-",             "Hormigon",                          "Vol: 2,000 L",                                     "ADASA"),
    ("BH-06-001",     "Area 06", "Bomba de Alimentacion Salmuera",              "-",             "Centrifuga",                        "Q: 13.4 l/s | TDH: 40 mca | Motor: 11 kW",        "ADASA"),
    ("BS-06-001",     "Area 06", "Bomba Sumergible Drenajes",                   "-",             "Sumergible",                        "Q: 13.4 l/s | TDH: 10 mca | Motor: 3 kW",         "ADASA"),
]

EQUIPOS_09 = [
    ("MZE-09-001",    "Area 09", "Static Mixer",                                "N-Spindle",     "NS11 80 100-750 A-I15",             "100 mm ID × 750 mmL",                              "BW Water"),
    ("FIL-09-001",    "Area 09", "RO Cartridge Filter",                         "Fil-Trek",      "FRPH12-012-4-4F-100",               "Q: 49.0 m3/h | 12\" D × 63.25\" L",               "BW Water"),
    ("BH-09-001",     "Area 09", "RO HP Feed Pump",                             "Fedco",         "MSD-7016",                          "Q: 49.0 m3/h | 46.9 bar | Motor: 93 kW",          "BW Water"),
    ("SIP-09-001",    "Area 09", "Feed Turbocharger (ERD Stage 1)",             "Fedco",         "HPB-60",                            "288mm L × 279mm W × 254mm H",                     "BW Water"),
    ("BOI-09-001",    "Area 09", "Stage 1: SWRO Membrane + Pressure Vessel",   "LG + Protec",   "LG SW 400 SR / BPV-8-1200-SP-7",   "6 PV × 7 memb. | Feed: 49.0 m3/h @ 69.5 bar",    "BW Water"),
    ("SIP-09-002",    "Area 09", "Interstage Turbocharger (ERD Stage 2)",       "Fedco",         "HPB-60",                            "288mm L × 279mm W × 254mm H",                     "BW Water"),
    ("BOI-09-002",    "Area 09", "Stage 2: UHPRO Membrane + Pressure Vessel",  "LG + Protec",   "LG SW 400R G2 UHP / BPV-8-1800-SP-7","4 PV × 7 memb. | Feed: 36.1 m3/h @ 84.8 bar", "BW Water"),
    ("TK-09-001",     "Area 09", "CIP Tank",                                    "Dayamas",       "DYM 6800",                          "Vol: 6.1 m3 | 1800mmD × 2950mmH",                 "BW Water"),
    ("REL-09-001",    "Area 09", "CIP Heater",                                  "Quantic Logic", "VEMA",                              "20 kW | 380V 3-ph",                                "BW Water"),
    ("BH-09-002",     "Area 09", "CIP Pump",                                    "Grundfos",      "CRN64-2 AGAE-HQQE",                 "Q: 57.0 m3/h | 4 bar | Motor: 11 kW",             "BW Water"),
    ("FIL-09-002",    "Area 09", "CIP Cartridge Filter",                        "Fil-Trek",      "S6GL14-019-4-4F-A-150",             "Q: 57.0 m3/h | 14.5\" OD × 61.63\" L",            "BW Water"),
    ("TK-09-002",     "Area 09", "Antiscalant Dosing Tank",                     "Promatics",     "PLC330",                            "Vol: 0.27 m3 | 630mmD × 1090mmH",                 "BW Water"),
    ("BDS-09-001/002","Area 09", "Antiscalant Dosing Pump (1 Duty + 1 Standby)","Prominent",    "GMXa 1602 PPT20000UA",              "Q: 2.3 LPH max | 24 W | 230V 1-ph",               "BW Water"),
]

# ─── VALVULAS ─────────────────────────────────────────────────────────────────
# TAG | Sistema | DN | Tipo | Rating | Actuacion | Servicio/Linea | Suministro | Notas

VALVULAS_06 = [
    ("VM-06-001", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-001", "ADASA", ""),
    ("VM-06-002", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-002", "ADASA", ""),
    ("VM-06-003", "Area 06", "DN63",  "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN63-PN10-001",  "ADASA", ""),
    ("VM-06-004", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-004", "ADASA", ""),
    ("VM-06-005", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-005", "ADASA", ""),
    ("VR-06-001", "Area 06", "DN100", "Check Valve (Duo)",     "ANSI 150#", "Auto",   "SA-HDPE-DN110-PN10-005", "ADASA", ""),
    ("VM-06-008", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-006", "ADASA", ""),
    ("VM-06-009", "Area 06", "DN100", "Butterfly Valve",       "ANSI 150#", "Manual", "SA-HDPE-DN110-PN10-007", "ADASA", ""),
    ("VM-06-006", "Area 06", "DN90",  "Butterfly Valve",       "ANSI 150#", "Manual", "PE-HDPE-DN90-PN10-003",  "ADASA", ""),
    ("VM-06-007", "Area 06", "DN90",  "Butterfly Valve",       "ANSI 150#", "Manual", "PE-HDPE-DN90-PN10-001",  "ADASA", ""),
    ("VM-06-015", "Area 06", "DN90",  "Butterfly Valve",       "ANSI 150#", "Manual", "PE-HDPE-DN90-PN10-001",  "ADASA", ""),
    ("VM-06-016", "Area 06", "DN90",  "Butterfly Valve",       "ANSI 150#", "Manual", "PE-HDPE-DN90-PN10-002",  "ADASA", ""),
    ("VR-06-002", "Area 06", "DN100", "Check Valve (Duo)",     "ANSI 150#", "Auto",   "SA-HDPE-DN110-PN10-006", "ADASA", ""),
    ("VR-06-003", "Area 06", "DN100", "Check Valve (Duo)",     "ANSI 150#", "Auto",   "SA-HDPE-DN110-PN10-007", "ADASA", ""),
]

VALVULAS_09 = [
    # Item 1-10: Cartridge Filter
    ("VM-09-001",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-002",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-007",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-003",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-004",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-008",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-005",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-006",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-110",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    ("VM-09-011",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "Cartridge Filter",                  "BW Water", ""),
    # Item 11-19: SWRO HPP
    ("VM-09-012",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-111",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-013",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-112",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-014",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-113",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VR-09-001",  "Area 09", "DN100", "Check Valve (Dual Flapper)", "ANSI 900#", "Auto",                 "SWRO HPP",                          "BW Water", ""),
    ("VM-09-151",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    ("VM-09-016",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO HPP",                          "BW Water", ""),
    # Item 20-22: Feed Turbocharger
    ("VM-09-021",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "Feed Turbocharger",                  "BW Water", ""),
    ("VM-09-114",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "Feed Turbocharger",                  "BW Water", ""),
    ("VM-09-022",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "Feed Turbocharger",                  "BW Water", ""),
    # Item 23-38: SWRO Permeate 1st Stage
    ("VM-09-141",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-142",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-143",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-144",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-145",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-146",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-042",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-041",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-043",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-044",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-045",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VM-09-115",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VR-09-003",  "Area 09", "DN80",  "Check Valve (Single Flapper)","ANSI 150#","Auto",                 "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VE-09-003",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 150#", "Motorized (ON/OFF)",   "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VE-09-004",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 150#", "Motorized (ON/OFF)",   "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VE-09-005",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 150#", "Motorized (ON/OFF)",   "SWRO Permeate 1st Stage",           "BW Water", ""),
    # Item 39-44: SWRO Reject 1st Stage
    ("VM-09-023",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 1st Stage",             "BW Water", ""),
    ("VM-09-116",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 1st Stage",             "BW Water", ""),
    ("VM-09-024",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 1st Stage",             "BW Water", ""),
    ("VM-09-025",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 1st Stage",             "BW Water", ""),
    ("VM-09-015",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 1st Stage",             "BW Water", ""),
    ("VE-09-007",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "SWRO Reject 1st Stage",             "BW Water", ""),
    # Item 45-47: 2nd Stage Turbocharger Feed
    ("VM-09-026",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "2nd Stage Turbocharger Feed",        "BW Water", ""),
    ("VM-09-038",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "2nd Stage Turbocharger Feed",        "BW Water", ""),
    ("VM-09-027",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "2nd Stage Turbocharger Feed",        "BW Water", ""),
    # Item 48-52: SWRO Permeate 2nd Stage
    ("VM-09-147",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 2nd Stage",           "BW Water", ""),
    ("VM-09-148",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 2nd Stage",           "BW Water", ""),
    ("VM-09-149",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 2nd Stage",           "BW Water", ""),
    ("VM-09-150",  "Area 09", "DN8",   "Labcock",                    "ANSI 150#", "Manual",               "SWRO Permeate 2nd Stage",           "BW Water", ""),
    ("VM-09-117",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "SWRO Permeate 2nd Stage",           "BW Water", ""),
    # Item 53-70: SWRO Reject 2nd Stage
    ("VM-09-031",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 2nd Stage",             "BW Water", ""),
    ("VM-09-119",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 2nd Stage",             "BW Water", ""),
    ("VM-09-032",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 2nd Stage",             "BW Water", ""),
    ("VM-09-033",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO Reject 2nd Stage",             "BW Water", ""),
    ("VE-09-008",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 150#", "Motorized (ON/OFF)",   "SWRO Permeate 1st Stage",           "BW Water", ""),
    ("VE-09-009",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VE-09-010",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "SWRO 1st Stage Reject",             "BW Water", ""),
    ("VE-09-002",  "Area 09", "DN25",  "V-Ball Valve",               "ANSI 900#", "Motorized (Modulating)","SWRO 2nd Stage Reject",            "BW Water", ""),
    ("VM-09-118",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-034",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VE-09-006",  "Area 09", "DN65",  "V-Ball Valve",               "ANSI 900#", "Motorized (Modulating)","RO Reject",                        "BW Water", ""),
    ("VE-09-017",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "1st Stage Reject to 2nd Stage",     "BW Water", ""),
    ("VM-09-120",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-035",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-036",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-121",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-037",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    ("VM-09-122",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 900#", "Manual",               "SWRO 2nd Stage Reject",             "BW Water", ""),
    # Item 71-93: CIP
    ("VE-09-012",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "CIP",                               "BW Water", ""),
    ("VE-09-013",  "Area 09", "DN80",  "Butterfly Valve",            "ANSI 900#", "Motorized (ON/OFF)",   "CIP",                               "BW Water", ""),
    ("VM-09-063",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-064",  "Area 09", "DN50",  "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-061",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-062",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-065",  "Area 09", "DN150", "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-072",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-073",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-123",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VR-09-004",  "Area 09", "DN100", "Check Valve (Single Flapper)","ANSI 150#","Auto",                 "CIP",                               "BW Water", ""),
    ("VM-09-074",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-075",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-076",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-081",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-082",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-124",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-085",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-083",  "Area 09", "DN25",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-084",  "Area 09", "DN25",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-086",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-125",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    ("VM-09-087",  "Area 09", "DN100", "Butterfly Valve",            "ANSI 150#", "Manual",               "CIP",                               "BW Water", ""),
    # Item 94-112: Antiscalant
    ("VE-09-016",  "Area 09", "DN25",  "Ball Valve",                 "ANSI 150#", "Motorized (ON/OFF)",   "Antiscalant",                       "BW Water", ""),
    ("VM-09-093",  "Area 09", "DN25",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-091",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-092",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-094",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-095",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-102",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-101",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-107",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-106",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-108",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("PSV-09-002", "Area 09", "DN15",  "Pressure Safety Valve",      "ANSI 150#", "Self-Actuated",        "Antiscalant (Dosing Pump pkg)",      "BW Water", ""),
    ("VM-09-103",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-104",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-105",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VM-09-126",  "Area 09", "DN15",  "Ball Valve",                 "ANSI 150#", "Manual",               "Antiscalant",                       "BW Water", ""),
    ("VE-09-014",  "Area 09", "DN25",  "Ball Valve",                 "ANSI 150#", "Motorized (ON/OFF)",   "Antiscalant",                       "BW Water", ""),
    ("VM-09-130",  "Area 09", "DN15",  "Injection Valve (Check)",    "ANSI 150#", "Self-Actuated",        "Antiscalant",                       "BW Water", ""),
    ("PSV-09-003", "Area 09", "DN15",  "Pressure Safety Valve",      "ANSI 150#", "Self-Actuated",        "RO Permeate",                       "BW Water", ""),
]

# ─── INSTRUMENTOS ─────────────────────────────────────────────────────────────
# TAG | Sistema | Funcion | Descripcion | Fabricante | Modelo | Rango | Suministro

INSTRUMENTOS_06 = [
    ("LSH-06-001",    "Area 06", "LSH",    "Interruptor Nivel Alto — salmuera TK-06-001",                  "-",   "-",                          "On/Off",           "ADASA"),
    ("LSH-06-002",    "Area 06", "LSH",    "Interruptor Nivel Alto — dispersante TK-06-003",               "-",   "-",                          "On/Off",           "BW Water"),
    ("LSH-06-003",    "Area 06", "LSH",    "Interruptor Nivel Alto — Fosa Drenajes TK-06-002",             "-",   "-",                          "On/Off",           "ADASA"),
    ("LSL-06-001",    "Area 06", "LSL",    "Interruptor Nivel Bajo — salmuera TK-06-001",                  "-",   "-",                          "On/Off",           "ADASA"),
    ("LSL-06-002",    "Area 06", "LSL",    "Interruptor Nivel Bajo — dispersante TK-06-003",               "-",   "-",                          "On/Off",           "BW Water"),
    ("LSL-06-003",    "Area 06", "LSL",    "Interruptor Nivel Bajo — Fosa Drenajes TK-06-002",             "-",   "-",                          "On/Off",           "ADASA"),
    ("LI-06-001",     "Area 06", "LI",     "Indicador Nivel — Estanque CIP TK-09-001",                     "-",   "-",                          "-",                "BW Water"),
    ("LIT-06-001",    "Area 06", "LIT",    "Transmisor Ultrasonico — salmuera TK-06-001",                  "-",   "-",                          "0-5 m",            "ADASA"),
    ("LIT-06-002",    "Area 06", "LIT",    "Transmisor Ultrasonico — Estanque CIP TK-09-001",              "-",   "-",                          "-",                "BW Water"),
    ("PI-06-001",     "Area 06", "PI",     "Manometro — Descarga BH-06-001",                               "-",   "-",                          "0-10 bar",         "ADASA"),
    ("PI-06-002",     "Area 06", "PI",     "Manometro — Descarga bomba alta presion",                      "-",   "-",                          "-",                "BW Water"),
    ("PI-06-003",     "Area 06", "PI",     "Manometro — Salida de salmuera",                               "-",   "-",                          "-",                "BW Water"),
    ("PI-06-004",     "Area 06", "PI",     "Manometro — Descarga bomba CIP",                               "-",   "-",                          "-",                "BW Water"),
    ("PI-06-005",     "Area 06", "PI",     "Manometro — Alimentacion filtro CIP",                          "-",   "-",                          "-",                "BW Water"),
    ("PI-06-006",     "Area 06", "PI",     "Manometro — Salida filtro CIP",                                "-",   "-",                          "-",                "BW Water"),
    ("PI-06-007",     "Area 06", "PI",     "Manometro — Descarga bomba dosificadora",                      "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-001",    "Area 06", "PIT",    "Transmisor Presion — Alimentacion de salmuera",                "-",   "-",                          "0-10 bar",         "ADASA"),
    ("PIT-06-002",    "Area 06", "PIT",    "Transmisor Presion — Succion bomba alta presion",              "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-003",    "Area 06", "PIT",    "Transmisor Presion — Descarga bomba alta presion",             "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-004",    "Area 06", "PIT",    "Transmisor Presion — Alimentacion rack 1ra Etapa",             "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-005",    "Area 06", "PIT",    "Transmisor Presion — Salmuera rack 1ra Etapa",                 "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-006",    "Area 06", "PIT",    "Transmisor Presion — Succion Turbo 1ra Etapa",                 "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-007",    "Area 06", "PIT",    "Transmisor Presion — Alimentacion rack 2da Etapa",             "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-008",    "Area 06", "PIT",    "Transmisor Presion — Salmuera rack 2da Etapa",                 "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-009",    "Area 06", "PIT",    "Transmisor Presion — Salida de permeado",                      "-",   "-",                          "-",                "BW Water"),
    ("PIT-06-010",    "Area 06", "PIT",    "Transmisor Presion — Salida de salmuera",                      "-",   "-",                          "-",                "BW Water"),
    ("FIT-06-001",    "Area 06", "FIT",    "Caudalimetro Mag — Alimentacion de salmuera",                  "-",   "-",                          "0-100 m3/h",       "ADASA"),
    ("FIT-06-002",    "Area 06", "FIT",    "Caudalimetro Mag — Permeado rack 2da Etapa",                   "-",   "-",                          "-",                "BW Water"),
    ("FIT-06-003",    "Area 06", "FIT",    "Caudalimetro Mag — Salida de permeado",                        "-",   "-",                          "-",                "BW Water"),
    ("FIT-06-004",    "Area 06", "FIT",    "Caudalimetro Mag — Salida de salmuera",                        "-",   "-",                          "-",                "BW Water"),
    ("FIT-06-005",    "Area 06", "FIT",    "Caudalimetro Mag — Salida filtro CIP",                         "-",   "-",                          "-",                "BW Water"),
    ("ORPIT-06-001",  "Area 06", "ORPIT",  "Analizador Redox — Entrada salmuera a OI",                     "-",   "-",                          "-",                "BW Water"),
    ("CLIT-06-001",   "Area 06", "CLIT",   "Analizador de Cloro — Entrada salmuera a OI",                  "-",   "-",                          "-",                "BW Water"),
    ("CONDIT-06-001", "Area 06", "CONDIT", "Analizador Conductividad — Salida de permeado",                "-",   "-",                          "-",                "BW Water"),
    ("TIT-06-001",    "Area 06", "TIT",    "Transmisor Temperatura — Estanque CIP TK-09-001",              "-",   "-",                          "-",                "BW Water"),
]

INSTRUMENTOS_09 = [
    ("DPS-09-001",   "Area 09", "DPS",   "Diff. Pressure Switch — RO Cartridge Filter",              "Ashcroft",          "1132",                       "0-2 bar",            "BW Water"),
    ("ORPIT-09-001", "Area 09", "ORPIT", "ORP Analyzer — Cartridge Filter Discharge",                "Rosemount",         "3900 / Tx: 1056",            "-1500 to +1500 mV",  "BW Water"),
    ("CIT-09-001",   "Area 09", "CIT",   "Conductivity Analyzer — Cartridge Filter Discharge",       "Rosemount",         "400 / Tx: 1056",             "0-2,000 uS/cm",      "BW Water"),
    ("FIT-09-001",   "Area 09", "FIT",   "Flow Transmitter (Mag) — Cartridge Filter Discharge",      "Rosemount",         "8750W",                      "0-100 m3/h",         "BW Water"),
    ("PIT-09-001",   "Area 09", "PIT",   "Pressure Transmitter — HP Pump Feed",                      "Schneider Foxboro", "IGP05S",                     "0-6 bar",            "BW Water"),
    ("PIT-09-002",   "Area 09", "PIT",   "Pressure Transmitter — HP Pump Discharge",                 "Schneider Foxboro", "IGP05S",                     "0-100 bar",          "BW Water"),
    ("VT-09-001",    "Area 09", "VT",    "Vibration Transmitter — HP Pump",                          "ifm",               "VTV122",                     "0-25 mm/s",          "BW Water"),
    ("TE-09-001",    "Area 09", "TE",    "Temp. Sensor Pt-100 — HP Pump Bearing",                    "Fedco",             "PT100 DIN 44082",            "60-180 \u00b0C",     "BW Water"),
    ("TE-09-002",    "Area 09", "TE",    "Temp. Sensor Pt-100 — HP Pump Winding",                    "Fedco",             "PT100 DIN 44082",            "60-180 \u00b0C",     "BW Water"),
    ("PI-09-001",    "Area 09", "PI",    "Pressure Gauge — HP Pump Discharge",                       "Wika",              "233.50",                     "0-100 bar",          "BW Water"),
    ("PIT-09-003",   "Area 09", "PIT",   "Pressure Transmitter — Stage 1 Feed",                      "Schneider Foxboro", "IGP05S",                     "0-150 bar",          "BW Water"),
    ("PIT-09-009",   "Area 09", "PIT",   "Pressure Transmitter — Combined Permeate",                 "Schneider Foxboro", "IGP05S",                     "0-2 bar",            "BW Water"),
    ("PIT-09-004",   "Area 09", "PIT",   "Pressure Transmitter — Stage 1 Reject",                    "Schneider Foxboro", "IGP05S",                     "0-150 bar",          "BW Water"),
    ("FIT-09-003",   "Area 09", "FIT",   "Flow Transmitter (Mag) — Combined Permeate",               "Rosemount",         "8750W",                      "0-40 m3/h",          "BW Water"),
    ("CIT-09-002",   "Area 09", "CIT",   "Conductivity Analyzer — Permeate Train",                   "Rosemount",         "400 / Tx: 1056",             "0-2,000 uS/cm",      "BW Water"),
    ("FIT-09-002",   "Area 09", "FIT",   "Flow Transmitter (Mag) — 2nd Stage Permeate",              "Rosemount",         "8750W",                      "0-18 m3/h",          "BW Water"),
    ("PIT-09-007",   "Area 09", "PIT",   "Pressure Transmitter — Interstage to Feed Turbo",          "Schneider Foxboro", "IGP05S",                     "0-100 bar",          "BW Water"),
    ("VT-09-002",    "Area 09", "VT",    "Vibration Transmitter — Feed Turbocharger",                "ifm",               "VTV122",                     "0-25 mm/s",          "BW Water"),
    ("VT-09-003",    "Area 09", "VT",    "Vibration Transmitter — Interstage Turbocharger",          "ifm",               "VTV122",                     "0-25 mm/s",          "BW Water"),
    ("PIT-09-005",   "Area 09", "PIT",   "Pressure Transmitter — Stage 2 Feed",                      "Schneider Foxboro", "IGP05S",                     "0-150 bar",          "BW Water"),
    ("PIT-09-006",   "Area 09", "PIT",   "Pressure Transmitter — Stage 2 Reject",                    "Schneider Foxboro", "IGP05S",                     "0-150 bar",          "BW Water"),
    ("CIT-09-004",   "Area 09", "CIT",   "Conductivity Analyzer — Stage 1 Reject",                   "Rosemount",         "400 / Tx: 1056",             "0-2,000 uS/cm",      "BW Water"),
    ("CIT-09-003",   "Area 09", "CIT",   "Conductivity Analyzer — Stage 2 Permeate",                 "Rosemount",         "400 / Tx: 1056",             "0-2,000 uS/cm",      "BW Water"),
    ("PI-09-002",    "Area 09", "PI",    "Pressure Gauge — RO Reject",                               "Wika",              "233.50",                     "0-1.6 bar",          "BW Water"),
    ("CIT-09-005",   "Area 09", "CIT",   "Conductivity Analyzer (Toroidal) — Train Reject",          "Rosemount",         "228 / Tx: 1056",             "0-20 mS/cm",         "BW Water"),
    ("FIT-09-004",   "Area 09", "FIT",   "Flow Transmitter (Mag) — Train Reject",                    "Rosemount",         "8750W",                      "0-60 m3/h",          "BW Water"),
    ("PIT-09-008",   "Area 09", "PIT",   "Pressure Transmitter — Train Reject",                      "Schneider Foxboro", "IGP05S",                     "0-2 bar",            "BW Water"),
    ("TIT-09-001",   "Area 09", "TIT",   "Temperature Transmitter — CIP Tank",                       "Rosemount",         "RTD: 214C / Tx: 644",        "0-100 \u00b0C",      "BW Water"),
    ("LIT-09-002",   "Area 09", "LIT",   "Level Transmitter (Pressure) — CIP Tank",                  "Vega",              "VEGABAR 82",                 "0-6.1 m",            "BW Water"),
    ("PI-09-003",    "Area 09", "PI",    "Pressure Gauge — CIP Pump Discharge",                      "Wika",              "233.50 / 990.10",            "0-4 bar",            "BW Water"),
    ("TE-09-003",    "Area 09", "TE",    "Temp. Sensor Pt-100 — CIP Pump Bearing",                   "Grundfos",          "PT100 DIN 44082",            "60-180 \u00b0C",     "BW Water"),
    ("TE-09-004",    "Area 09", "TE",    "Temp. Sensor Pt-100 — CIP Pump Winding",                   "Grundfos",          "PT100 DIN 44082",            "60-180 \u00b0C",     "BW Water"),
    ("PI-09-004",    "Area 09", "PI",    "Pressure Gauge — CIP Cartridge Filter Feed",               "Wika",              "233.50 / 990.10",            "0-4 bar",            "BW Water"),
    ("PI-09-005",    "Area 09", "PI",    "Pressure Gauge — CIP Cartridge Filter Discharge",          "Wika",              "233.50 / 990.10",            "0-4 bar",            "BW Water"),
    ("PHIT-09-001",  "Area 09", "PHIT",  "pH Analyzer — RO CIP/Flush",                               "Rosemount",         "3900 / Tx: 1056",            "0-14 pH",            "BW Water"),
    ("FIT-09-005",   "Area 09", "FIT",   "Flow Transmitter (Mag) — CIP Pump Discharge",              "Rosemount",         "8750W",                      "0-100 m3/h",         "BW Water"),
    ("LS-09-001",    "Area 09", "LS",    "Level Switch High — Antiscalant Dosing Tank",               "IFM",               "KQ6005",                     "-",                  "BW Water"),
    ("LS-09-002",    "Area 09", "LS",    "Level Switch Low — Antiscalant Dosing Tank",                "IFM",               "KQ6005",                     "-",                  "BW Water"),
    ("PI-09-006",    "Area 09", "PI",    "Pressure Gauge — Antiscalant Dosing Pump Discharge",       "Wika",              "233.50 / 990.10",            "0-4 bar",            "BW Water"),
]

# ─── Build Workbook ───────────────────────────────────────────────────────────
wb = openpyxl.Workbook()

# Sheet 1 — EQUIPOS
ws_eq = wb.active
ws_eq.title = "EQUIPOS"
apply_header(ws_eq, ["TAG", "Sistema", "Descripcion", "Fabricante", "Modelo", "Capacidad / Potencia", "Suministro"])
ws_eq.freeze_panes = "A2"
row = 2
for d in EQUIPOS_06:
    write_row(ws_eq, row, d, A06_FILL)
    color_suministro(ws_eq, row, 7, d[6])
    row += 1
for d in EQUIPOS_09:
    write_row(ws_eq, row, d, A09_FILL)
    color_suministro(ws_eq, row, 7, d[6])
    row += 1
set_col_widths(ws_eq, [16, 10, 44, 16, 34, 38, 10])

# Sheet 2 — VALVULAS
ws_val = wb.create_sheet("VALVULAS")
apply_header(ws_val, ["TAG", "Sistema", "DN", "Tipo", "Rating", "Actuacion", "Servicio / Linea", "Suministro", "Notas"])
ws_val.freeze_panes = "A2"
row = 2
for d in VALVULAS_06:
    write_row(ws_val, row, d, A06_FILL)
    color_suministro(ws_val, row, 8, d[7])
    row += 1
for d in VALVULAS_09:
    nota = d[8]
    fill = DUPLIC_FILL if "Proposed TAG" in nota else A09_FILL
    write_row(ws_val, row, d, fill)
    color_suministro(ws_val, row, 8, d[7])
    row += 1
set_col_widths(ws_val, [14, 10, 7, 26, 11, 24, 32, 10, 58])

# Sheet 3 — INSTRUMENTOS
ws_inst = wb.create_sheet("INSTRUMENTOS")
apply_header(ws_inst, ["TAG", "Sistema", "Funcion", "Descripcion", "Fabricante", "Modelo", "Rango", "Suministro"])
ws_inst.freeze_panes = "A2"
row = 2
for d in INSTRUMENTOS_06:
    write_row(ws_inst, row, d, A06_FILL)
    color_suministro(ws_inst, row, 8, d[7])
    row += 1
for d in INSTRUMENTOS_09:
    write_row(ws_inst, row, d, A09_FILL)
    color_suministro(ws_inst, row, 8, d[7])
    row += 1
set_col_widths(ws_inst, [16, 10, 8, 55, 20, 26, 18, 10])

wb.save(OUTPUT_FILE)

eq_total  = len(EQUIPOS_06) + len(EQUIPOS_09)
val_total = len(VALVULAS_06) + len(VALVULAS_09)
inst_total= len(INSTRUMENTOS_06) + len(INSTRUMENTOS_09)

print(f"Generado: {OUTPUT_FILE}")
print(f"  EQUIPOS:      {eq_total} filas  ({len(EQUIPOS_06)} Area 06 + {len(EQUIPOS_09)} Area 09)")
print(f"  VALVULAS:     {val_total} filas  ({len(VALVULAS_06)} Area 06 + {len(VALVULAS_09)} Area 09)")
print(f"  INSTRUMENTOS: {inst_total} filas  ({len(INSTRUMENTOS_06)} Area 06 + {len(INSTRUMENTOS_09)} Area 09)")
