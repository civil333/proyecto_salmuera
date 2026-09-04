#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera Excel con tabla maestra de 81 entregables BW Water.
Combina documentos entregados (58 en seccion DELIVERED + 1 en seccion NOT DELIVERED) + no entregados/parciales (22).
Columna ET Deadline: plazo contractual por item segun ET Seccion 7.
  - Items #1    : Max. 15 days from NTP
  - Items #2-57 : Max. 90 days from NTP
  - Items #76-80: 1 month before end of contract (prerequisite for equipment release)

Actualizaciones 08-Mar-2026 (TM N7 — Entrega 14):
  - Item 16: A/C Thermal Calc actualizado a Rev B (E14, N7, Code 3)
  - Item 40: NUEVO — Piping Layout Rev A (E14, N7, Code 3)
  - Item 41: NUEVO — Tie-In Point Layout Rev A (E14, N7, Code 3)
  - Item 66: Control Philosophy — ENTREGADO (Rev A, E14, N7, Code 3). Era NOT DELIVERED.
  - Item 74: Modbus TCP Memory Map — 65 dias (era 51)
  - Eliminado item duplicado A/C Calc NOT DELIVERED (ya entregado en item 16)

Actualizaciones 23-Mar-2026 (TM N8-N11 — Entregas 15-21):
  - Items 2, 5, 11, 12, 19, 27, 30, 31, 32, 33, 34, 35: rev/veredicto actualizados
    Feed TC (11): 4-Rejected -> 2-AN (TM N11 Rev D)
    Valve List (33): 4-Rejected -> 3-To be revised (TM N11 Rev C)
    IO List (31): 3-To be revised -> 2-AN (TM N10 Rev B)
    Painting Spec (19): 2-AN -> 1-Approved (TM N11 Rev B)
    Grounding Layout (27) + Instrument Location (35): 2-AN / 3-TBR -> 3-TBR (TM N11 OBS-03/04)
  - Items 42-57: 16 NUEVOS entregados (E15-E21)
    42-50: DS instrumentos + Power Works Drawing (E15, N8)
    51: DS Temperature Transmitter (E16, N8)
    52-55: Data Transfer List + GA Antiscalant Tank + GA SIP-09-001/002 (E18, N10)
    56-57: GA CIP Pump + GA Antiscalant Pump (E20, N11)
  - Items NOT DELIVERED renumerados: 42-63 -> 58-79
  - Item 74: Modbus TCP Memory Map — 80 dias (era 65)

Actualizaciones 27-Mar-2026 (Reunion 26-Mar-2026 + Advanced copies):
  - Item 2:  P&ID — Rev C commitment by 31-Mar-2026 (meeting 26-Mar)
  - Item 33: Valve List — PO may proceed despite Code 3 (meeting 26-Mar)
  - Item 40: Piping Layout — linked advanced copies reviewed 27-Mar
  - Item 41: Tie-In Point — 5 ADASA observations on Rev B preliminary (27-Mar)
  - Item 59: General Layouts — Equipment Layout Rev B preliminary reviewed 27-Mar
  - Item 66: Control Philosophy — Nick Huta committed to issue Rev B (26-Mar)
  - Item 74: Modbus TCP Memory Map — 84 dias (era 80)

Actualizaciones 03-Apr-2026 (TM N12-N13 — Entregas 22-24):
  - Item 2:  P&ID Rev C entregado (E24, N13, Code 2-AN). Cerrado title block NOTE-01.
  - Item 38: Line List Rev B (E23, N12, Code 2-AN). NOTE-02 SCH80 vs SCH 80S pending IFC.
  - Item 58: NUEVO — DS Vibration Transmitter Rev A (E22, N12, Code 3-TBR). HART pendiente.
  - Items 58-79 -> 59-80: renumerados (+1 por insercion item 58 nuevo).
  - Item 75 (ex-74): Modbus TCP Memory Map — 91 dias (era 84).
  Total items: 80 (58 entregados + 22 no entregados/parciales).

Actualizaciones 06-Apr-2026 (TM N13 enviado — E25 Power Works Rev B):
  - Item 2:  P&ID Rev C — fecha corregida a 06-Apr-2026 (envio real TM N13); removido "pending sending".
  - Item 50: Power Works Rev A -> Rev B (E25, N13, Code 2-AN). 3 NOTEs nuevas incorporadas.
  - Item 75: Modbus TCP Memory Map — 94 dias (era 91, 06-Apr vs 03-Apr).
  - Item 81: NUEVO — Cable Tray Layout (NOT DELIVERED, identificado en TM N13 NOTE-02 como entregable requerido antes de IFC).
  Total items: 81 (58 entregados + 23 no entregados/parciales).

Actualizaciones 15-Apr-2026 (TM N14 — Entregas 26-29):
  - Item 30: Control Architecture Rev C -> Rev D (E26, N14, Code 1-Approved). UPS 8h verificado. Todas obs TM N10 cerradas.
  - Item 31: IO List Rev B -> Rev C (E28, N14, Code 2-AN). NOTE-02: discrepancia voltaje analizadores (220VAC vs 24VDC).
  - Item 32: Instrument List Rev B -> Rev C (E28, N14, Code 2-AN). OBS-03 conductividad CERRADA. NOTE-03/04 nuevas.
  - Item 33: Valve List Rev C -> Rev D (E27, N14, Code 2-AN). Todos duplicados resueltos. NOTE-01 PSV removal.
  - Item 42: DS Conductivity Analyzer Rev A -> Rev B (E28, N14, Code 1). Toroidal confirmado.
  - Item 44: DS Flow Transmitter Rev A -> Rev B (E29, N14, Code 1). TM N8 OBS-01/02 cerradas.
  - Item 47: DS pH/ORP Analyzer Rev A -> Rev B (E28, N14, Code 1).
  - Item 48: DS Pressure Gauge Rev A -> Rev B (E27, N14, Code 1). Wika 990.31 PP/EPDM.
  - Item 51: DS Temperature Transmitter Rev A -> Rev B (E28, N14, Code 1).
  - Item 52: Data Transfer List Rev A -> Rev B (E28, N14, Code 2-AN). NOTE-05: Modbus scaling vibration.
  - Item 58: DS Vibration Transmitter Rev A -> Rev B (E28, N14, Code 1). IFM -> Wilcoxon PCH420V-M12. TM N12 OBS-01 CERRADA.
  - Item 75: Modbus TCP Memory Map — 103 dias (era 94).
  - Legend actualizada: TM N14, E29, 15-Apr-2026.
  Total items: 81 (59 entregados + 22 no entregados/parciales). 12 obs previas cerradas, 5 notas nuevas.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT = "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx"

# --- Colores por verdict ---
FILL_GREEN  = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")   # V1
FILL_YELLOW = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")   # V2-AN
FILL_ORANGE = PatternFill(start_color="FCD5B4", end_color="FCD5B4", fill_type="solid")   # V3
FILL_RED    = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")   # V4
FILL_GRAY   = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")   # Not delivered
FILL_BLUE   = PatternFill(start_color="BDD7EE", end_color="BDD7EE", fill_type="solid")   # Under review
FILL_HEADER = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

FONT_HEADER = Font(name="Arial", size=10, bold=True, color="FFFFFF")
FONT_NORMAL = Font(name="Arial", size=9)
FONT_BOLD   = Font(name="Arial", size=9, bold=True)
THIN_BORDER = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"),  bottom=Side(style="thin"),
)

# ET Deadline fills
FILL_DEADLINE_END      = PatternFill(start_color="FFB3B3", end_color="FFB3B3", fill_type="solid")
FILL_DEADLINE_NTP_LATE = PatternFill(start_color="FFE4B5", end_color="FFE4B5", fill_type="solid")

# Columns: #, Document, Code/Reference, Rev, Delivery, TM, Verdict, Status, Action Required, ET Deadline
HEADERS = ["#", "Document", "Code / ET Reference", "Rev", "Delivery", "TM",
           "Verdict", "Status", "Action Required", "ET Deadline"]

DATA = [
    # =========================================================
    # DELIVERED (57 items: 41 original + 16 new from E15-E21)
    # =========================================================
    # (#, Document, Code/ET Ref, Rev, Delivery, TM, Verdict, Status, Action Required, ET Deadline)
    (1,  "PFD",
         "P22-DWG-09-009-001", "B", "E8", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (2,  "P&ID",
         "P22-DWG-09-009-002", "C", "E24", "N13", "2-AN", "Delivered",
         "Rev C approved as noted (TM N13, 06-Apr-2026). NOTE-01: TK-09-001 (CIP Tank) 6.81 m\u00b3 in P&ID vs 6.1 m\u00b3 in Equipment List Rev B \u2014 confirm and correct prior to IFC Rev 0. Title block code '-002' CLOSED (TM N9 NOTE-01).",
         "ET Sec.7: Max. 90 days from NTP"),

    (3,  "Process Calculation",
         "P22-CD-09-009-001", "B", "E7", "N3", "2-AN", "Delivered",
         "Complete SEC calc, verify recovery rate",
         "ET Sec.7: Max. 90 days from NTP"),

    (4,  "DS UHPRO System",
         "P22-ET-09-009-001", "B", "E6", "N2", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (5,  "DS HP Pump",
         "P22-ET-09-009-002", "D", "E19", "N11", "2-AN", "Delivered",
         "Rev D approved as noted (TM N11). NOTE-01: confirm FEDCO coupling datasheet received. PO may proceed per procurement schedule.",
         "ET Sec.7: Max. 90 days from NTP"),

    (6,  "DS CIP Pump",
         "P22-ET-09-009-003", "B", "E6", "N2", "2-AN", "Delivered",
         "VFD to Direct start accepted. Motor compatibility pending.",
         "ET Sec.7: Max. 90 days from NTP"),

    (7,  "DS Antiscalant Pump",
         "P22-ET-09-009-004", "B", "E7", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (8,  "DS RO Container",
         "P22-ET-09-000-001", "B", "E8", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (9,  "DS RO Cartridge Filter",
         "P22-ET-09-009-005", "C", "E13", "N6", "2-AN", "Delivered",
         "12 cartridges justified. Note piping isometrics.",
         "ET Sec.7: Max. 90 days from NTP"),

    (10, "DS CIP Cartridge Filter",
         "P22-ET-09-009-006", "B", "E6", "N2", "2-AN", "Delivered",
         "Minor notes",
         "ET Sec.7: Max. 90 days from NTP"),

    (11, "DS Feed Turbocharger",
         "P22-ET-09-009-007", "D", "E19", "N11", "2-AN", "Delivered",
         "Rev D approved as noted (TM N11). Coupling pressure resolved. NOTE-03: update coupling label \u2018Style 77\u2019 \u2192 \u2018Style S\u2019 in next GA revision.",
         "ET Sec.7: Max. 90 days from NTP"),

    (12, "DS Interstage Turbocharger",
         "P22-ET-09-009-008", "D", "E19", "N11", "2-AN", "Delivered",
         "Rev D approved as noted (TM N11). NOTE-04: coupling label update pending in next GA revision.",
         "ET Sec.7: Max. 90 days from NTP"),

    (13, "DS CIP Tank",
         "P22-ET-09-009-010", "B", "E7", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (14, "DS Antiscalant Dosing Tank",
         "P22-ET-09-009-011", "B", "E10", "N4", "2-AN", "Delivered",
         "Minor notes",
         "ET Sec.7: Max. 90 days from NTP"),

    (15, "DS CIP Tank Heater",
         "P22-ET-09-009-014", "B", "E8", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED 08-Mar-2026: Rev B delivered in E14, reviewed in TM N7
    (16, "A/C Thermal Calculation",
         "P22-CD-09-005-002", "B", "E14", "N7", "3-To be revised", "Delivered",
         "Rev C required: (1) itemize ALL thermal loads \u2014 HP pump motor (4.26 kW), VFD (1.70 kW), PLC/control panel, instruments, antiscalant dosing equipment, lighting; (2) explicitly state n+1 configuration \u2014 two units \u22652.5 HP, each covering 100% of verified total load independently.",
         "ET Sec.7: Max. 90 days from NTP"),

    (17, "DS Static Mixer",
         "P22-ET-09-009-012", "B", "E13", "N6", "2-AN", "Delivered",
         "TAG MZE-09-001 vs P&ID to confirm",
         "ET Sec.7: Max. 90 days from NTP"),

    (18, "Piping Specifications",
         "P22-ET-09-005-001", "A", "E1", "N1", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (19, "Painting Specifications",
         "P22-ET-09-005-002", "B", "E19", "N11", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (20, "Single Line Diagram",
         "P22-CD-09-007-001", "A", "E1", "N1", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (21, "Electrical Load List",
         "P22-LI-09-007-001", "A", "E1", "N1", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (22, "DS Electrical Auxiliaries",
         "P22-ET-09-007-001", "A", "E1", "N1", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (23, "DS Power & Control Cable",
         "P22-ET-09-007-002", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (24, "DS Cable Tray",
         "P22-ET-09-007-003", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (25, "DS Conduit & Flexible",
         "P22-ET-09-007-004", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (26, "Power Cable Schedule",
         "P22-LI-09-007-002", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (27, "Grounding Layout",
         "P22-DWG-09-007-003", "B", "E21", "N11", "3-To be revised", "Delivered",
         "Rev B carries Code 3 (TM N11 OBS-04 MAJOR) \u2014 arrangement based on non-conforming Piping Layout Rev A. Rev C required after Piping Layout Rev B accepted.",
         "ET Sec.7: Max. 90 days from NTP"),

    (28, "Cable Tray Layout",
         "P22-DWG-09-007-004", "A", "E11", "N4", "3-To be revised", "Delivered",
         "Routing concerns, sizing verification",
         "ET Sec.7: Max. 90 days from NTP"),

    (29, "DS PLC & HMI",
         "P22-ET-09-008-001", "A", "E1", "N1", "2-AN", "Delivered",
         "Minor notes",
         "ET Sec.7: Max. 90 days from NTP"),

    (30, "Control Architecture",
         "P22-CD-09-004-001", "D", "E26", "N14", "1-Approved", "Delivered",
         "Rev D approved (TM N14). UPS 8h verified (40Ah \u00f7 4.35A = 9.2h). All TM N10 observations closed.",
         "ET Sec.7: Max. 90 days from NTP"),

    (31, "IO List",
         "P22-LI-09-008-001", "C", "E28", "N14", "2-AN", "Delivered",
         "Rev C approved as noted (TM N14). NOTE-02 (MAJOR): analyzer power supply voltage discrepancy \u2014 220VAC in REMARKS vs 24VDC in IL/CCS/Rosemount 1056 DS. Resolve before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (32, "Instrument List",
         "P22-LI-09-008-003", "C", "E28", "N14", "2-AN", "Delivered",
         "Rev C approved as noted (TM N14). TM N8 OBS-03 conductivity CLOSED (toroidal confirmed). NOTE-03: vibration calibrated range 0\u2013127 mm/s vs DTL 0\u201325 mm/s \u2014 align before IFC. NOTE-04: working medium labels show 'Filtered Water' for brine-side instruments \u2014 correct before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (33, "Valve List",
         "P22-LI-09-005-002", "C", "E19", "N11", "3-To be revised", "Delivered",
         "Rev C: 4 prior duplicates resolved. 2 new duplicates remain (VE-09-007, PSV-09-002) + area-code error VM-07-005. Rev D required \u2014 blocks All Valve PO. Meeting 26-Mar-2026: valve PO may proceed despite Code 3 \u2014 tag corrections to be handled in engineering.",
         "ET Sec.7: Max. 90 days from NTP"),

    (34, "Equipment List",
         "P22-LI-09-005-001", "B", "E20", "N11", "2-AN", "Delivered",
         "Rev B approved as noted (TM N11). Minor notes.",
         "ET Sec.7: Max. 90 days from NTP"),

    (35, "Instrument Location Layout",
         "P22-DWG-09-008-001", "B", "E21", "N11", "3-To be revised", "Delivered",
         "Rev B carries Code 3 (TM N11 OBS-03 MAJOR) \u2014 arrangement based on non-conforming Piping Layout Rev A. Rev C required after Piping Layout Rev B accepted.",
         "ET Sec.7: Max. 90 days from NTP"),

    (36, "I&C Cable Schedule",
         "P22-LI-09-008-002", "A", "E8", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (37, "Chemical Consumption List",
         "P22-LI-09-009-002", "A", "E7", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (38, "Line List",
         "P22-LI-09-009-003", "B", "E23", "N12", "2-AN", "Delivered",
         "Rev B approved as noted (TM N12). NOTE-02: pipe class designation SCH80 vs SCH 80S \u2014 to be corrected prior to IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (39, "Utility Consumption List",
         "P22-LI-09-009-001", "B", "E13", "N6", "2-AN", "Delivered",
         "A/C thermal calc Rev C still pending",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 08-Mar-2026 — E14 / TM N7
    (40, "Piping Layout",
         "P22-DWG-09-005-004", "A", "E14", "N7", "3-To be revised", "Delivered",
         "Rev B required: consolidate CIP (TK-09-001, BH-09-002, REL-09-001, FIL-09-002) and antiscalant dosing (TK-09-002, BDS-09-001/002) within single external footprint \u2264 container width \u00d7 3.5m. Flanged terminations for all antiscalant/CIP connections at module boundary. Include elevation view showing all tie-in positions. [TM N5 OBS-01 condition \u2014 11,150mm separation in Rev A is 3\u00d7 the limit] Linked documents: Equipment Layout Rev B and Tie-In Point Rev B preliminary copies reviewed by ADASA 27-Mar-2026 \u2014 formal submittals pending. CIP Super Duplex piping on hold (lead time 3\u20134 months) pending CIP footprint confirmation.",
         "ET Sec.7: Max. 90 days from NTP"),

    (41, "Tie-In Point Layout",
         "P22-DWG-09-005-005", "A", "E14", "N7", "3-To be revised", "Delivered",
         "Rev B required after Piping Layout Rev B accepted: antiscalant tie-in positions N\u00b01/N\u00b02 will change. Complete tie-in N\u00b01 (tag, P&ID ref, flange standard). Confirm CIP make-up water source (external vs permeate). Confirm brine feed design pressure at ANSI 150# boundary. Include elevation view with flange positions and elevations. Preliminary Rev B advanced copy reviewed 27-Mar-2026 \u2014 ADASA observations: (1) no space for pipe rack, connections directly from container; (2) dosing tank has no access, relocation required; (3) antiscalant loading directly to tank, no carrier pump; (4) module relocation cutover flanges not shown; (5) container elevation view missing.",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 23-Mar-2026 — E15 / TM N8 (instrument datasheets)
    (42, "DS Conductivity Analyzer",
         "P22-LI-09-008-005", "A", "E15", "N8", "2-AN", "Delivered",
         "Toroidal type required for high-conductivity services (brine/reject >20\u00a0mS/cm). Contacting type acceptable for low-conductivity services.",
         "ET Sec.7: Max. 90 days from NTP"),

    (43, "DS DP Switch",
         "P22-LI-09-008-006", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (44, "DS Flow Transmitter",
         "P22-LI-09-008-007", "A", "E15", "N8", "2-AN", "Delivered",
         "Minor notes per TM N8.",
         "ET Sec.7: Max. 90 days from NTP"),

    (45, "DS Level Switch",
         "P22-LI-09-008-008", "A", "E15", "N8", "2-AN", "Delivered",
         "Minor notes per TM N8.",
         "ET Sec.7: Max. 90 days from NTP"),

    (46, "DS Level Transmitter",
         "P22-LI-09-008-009", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (47, "DS pH/ORP Analyzer",
         "P22-LI-09-008-010", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (48, "DS Pressure Gauge",
         "P22-LI-09-008-011", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (49, "DS Pressure Transmitter",
         "P22-LI-09-008-012", "A", "E15", "N8", "2-AN", "Delivered",
         "Minor notes per TM N8.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED 06-Apr-2026: Rev B received (E25, N13, Code 2-AN)
    (50, "Power Works Drawing",
         "P22-DWG-09-007-005", "B", "E25", "N13", "2-AN", "Delivered",
         "Rev B approved as noted (TM N13, 06-Apr-2026). TM N8 OBS-01 CLOSED (grounding: 7 methods, page 9). TM N8 OBS-02 CLOSED (NEMA VE-2, NEC 392.30(B), NEC 352 cited). NOTE-01: grounding conductor sizing basis (16mm\u00b2/4mm\u00b2) not cited per NEC 250.122 \u2014 incorporate in IFC Rev 0. NOTE-02: Cable Tray Layout drawings not submitted \u2014 routing from LCP/MCC to all endpoints required prior to IFC. NOTE-03: ADASA duct bank interface data required \u2014 confirm conduit count/diameter, terminal arrangement, conductor cross-section.",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 23-Mar-2026 — E16 / TM N8
    (51, "DS Temperature Transmitter",
         "P22-LI-09-008-013", "A", "E16", "N8", "3-To be revised", "Delivered",
         "Rev B required per TM N8 observations.",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 23-Mar-2026 — E18 / TM N10
    (52, "Data Transfer List (Modbus TCP)",
         "P22-LI-09-008-004", "A", "E18", "N10", "2-AN", "Delivered",
         "Approved as noted (TM N10). Modbus TCP Memory Map (separate item) still pending.",
         "ET Sec.7: Max. 90 days from NTP"),

    (53, "GA Antiscalant Dosing Tank",
         "P22-DWG-09-005-015", "A", "E18", "N10", "2-AN", "Delivered",
         "Approved as noted (TM N10). Minor notes.",
         "ET Sec.7: Max. 90 days from NTP"),

    (54, "GA Feed Turbocharger (SIP-09-001)",
         "P22-DWG-09-005-012", "A", "E18", "N10", "3-To be revised", "Delivered",
         "Rev B required (TM N10). NOTE-03: coupling label \u2018Style 77\u2019 \u2192 \u2018Style S\u2019.",
         "ET Sec.7: Max. 90 days from NTP"),

    (55, "GA Interstage Turbocharger (SIP-09-002)",
         "P22-DWG-09-005-013", "A", "E18", "N10", "3-To be revised", "Delivered",
         "Rev B required (TM N10). NOTE-04: coupling label update pending.",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 23-Mar-2026 — E20 / TM N11
    (56, "GA CIP/Flushing Pump",
         "P22-DWG-09-005-010", "A", "E20", "N11", "2-AN", "Delivered",
         "Approved as noted (TM N11).",
         "ET Sec.7: Max. 90 days from NTP"),

    (57, "GA Antiscalant Dosing Pump",
         "P22-DWG-09-005-011", "A", "E20", "N11", "2-AN", "Delivered",
         "Approved as noted (TM N11).",
         "ET Sec.7: Max. 90 days from NTP"),

    # NEW 03-Apr-2026 — E22 / TM N12
    (58, "DS Vibration Transmitter",
         "P22-LI-09-008-014", "A", "E22", "N12", "3-To be revised", "Delivered",
         "Rev B required (TM N12 OBS-01 MAJOR): IFM VTV122 \u2014 4-20mA+HART compliance not documented. ET requires HART for all field instruments. Provide HART evidence or propose formal deviation. NOTE-01: Quantity field = 1 vs 3 TAGs required (VT-09-001/002/003) \u2014 correct in Rev B.",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # NOT DELIVERED / PARTIAL (22 items)
    # =========================================================
    (59, "Detailed Schedule",
         "ET Sec 7, p.27", "--", "--", "--", "Under review", "Delivered (deficient)",
         "Mar-2026 Baseline: FAT and commissioning reinstated (positive). STILL MISSING: document-level milestones. 15 pending deliverables and 14 open observations require individual dates. Recovery plan required for meeting 09-Mar-2026.",
         "ET Sec.7: Max. 15 days from NTP"),

    (60, "General Layouts (Equipment, GA)",
         "ET Sec 7, p.27", "--", "--", "--", "--", "PARTIAL",
         "Only discipline-specific layouts received. Equipment Layout Rev B preliminary copy reviewed 27-Mar-2026 \u2014 ADASA observation: tank must be relocated to opposite side to allow chemical loading access. Formal submittal pending.",
         "ET Sec.7: Max. 90 days from NTP"),

    (61, "Equipment/Piping Arrangement Drawings",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Blocks civil design, piping procurement",
         "ET Sec.7: Max. 90 days from NTP"),

    (62, "Seismic Calculation (NCh 2369)",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Structural design blocked",
         "ET Sec.7: Max. 90 days from NTP"),

    (63, "HP Line Flexibility Analysis",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Piping stress verification pending",
         "ET Sec.7: Max. 90 days from NTP"),

    (64, "Civil Requirements Drawings",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Foundations design blocked",
         "ET Sec.7: Max. 90 days from NTP"),

    (65, "Manufacturing and Testing Dossier",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Prerequisite for factory acceptance",
         "ET Sec.7: Max. 90 days from NTP"),

    (66, "Valve/Instrument Specs (brands+models)",
         "ET Sec 7, p.28", "--", "--", "--", "--", "PARTIAL",
         "Lists delivered but brands/models incomplete",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED 08-Mar-2026: NOW DELIVERED (Rev A, E14, N7, Code 3-To be revised)
    (67, "Control Philosophy",
         "P22-BT-09-009-001", "A", "E14", "N7", "3-To be revised", "Delivered",
         "BW Water commitment (26-Mar-2026): Nick Huta to review ADASA comments and issue Rev B \u2014 blocking item for Modbus TCP and integration. Rev B required \u2014 7 corrections: (1) UPS autonomy: 30 min specified vs 8h required \u2014 CRITICAL, 16\u00d7 shortfall, include capacity calc; (2) AI Pt-100 motor temperature inputs for HP+CIP motors, windings+bearings \u2014 CRITICAL (TM N3 OBS-01, 44d); (3) Modbus TCP/IP section \u2014 91 days pending (TM N2); (4) Resolve tag VE-07-014 vs VE-09-014 (same valve, different area codes); (5) DO Module Status output (TM N3 OBS-04, 44d); (6) DI General Module Enable from plant (TM N3 OBS-05, 44d); (7) Replace \u201cBT\u201d type code with valid project code.",
         "ET Sec.7: Max. 90 days from NTP"),

    (68, "HMI Screen Design",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Operator interface undefined",
         "ET Sec.7: Max. 90 days from NTP"),

    (69, "Detailed Deliverables List",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Cannot verify scope compliance",
         "ET Sec.7: Max. 90 days from NTP"),

    (70, "3D Model (Autodesk interoperable)",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Clash detection blocked",
         "ET Sec.7: Max. 90 days from NTP"),

    (71, "HP Line Isometric Drawings",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Blocks piping fabrication",
         "ET Sec.7: Max. 90 days from NTP"),

    (72, "Lifting Beams and Crane Rails",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Structural/mechanical integration",
         "ET Sec.7: Max. 90 days from NTP"),

    (73, "Detailed PIE",
         "ET Sec 7, pp.28-29", "--", "--", "--", "--", "NOT DELIVERED",
         "Manufacturing prerequisite per contract",
         "ET Sec.7: Max. 90 days from NTP \u2014 Prerequisite for manufacturing start"),

    (74, "MCC Datasheet",
         "ET 5.4", "--", "--", "--", "--", "NOT DELIVERED",
         "MCC reportedly in fabrication without DS",
         "ET Sec.5.4: Max. 90 days from NTP"),

    # UPDATED 06-Apr-2026: 94 days open (was 91 days 03-Apr-2026)
    (75, "Modbus TCP Memory Map",
         "ET 5.4 + TM N2", "--", "--", "--", "--", "NOT DELIVERED",
         "94 days open as of 06-Apr-2026 \u2014 no progress reported since TM N2. Integration planning blocked. Required before Control Philosophy Rev B can be finalized.",
         "ET Sec.5.4: Max. 90 days from NTP"),

    # End-of-contract items (#76-80)
    (76, "Installation Manual (lifting calc, plan, yoke)",
         "ET Sec 7, p.29", "--", "--", "--", "--", "NOT DELIVERED",
         "Required for site mobilization planning",
         "ET Sec.7 p.29: 1 month before end of contract \u2014 Required for equipment release to site"),

    (77, "Commissioning Manual",
         "ET Sec 7, p.29", "--", "--", "--", "--", "NOT DELIVERED",
         "Prerequisite for startup planning",
         "ET Sec.7 p.29: 1 month before end of contract \u2014 Required for equipment release to site"),

    (78, "O&M Manual (PLC screens, TAGs, procedures)",
         "ET Sec 7, p.29", "--", "--", "--", "--", "NOT DELIVERED",
         "Required for operator training and handover",
         "ET Sec.7 p.29: 1 month before end of contract \u2014 Required for equipment release to site"),

    (79, "Final Software Package and Licenses",
         "ET Sec 7, p.29", "--", "--", "--", "--", "NOT DELIVERED",
         "PLC/HMI source code, perpetual licenses",
         "ET Sec.7 p.29: 1 month before end of contract \u2014 Required for equipment release to site"),

    (80, "Preservation, Packaging and Transport Proc.",
         "ET Sec 7, p.30", "--", "--", "--", "--", "NOT DELIVERED",
         "Must be approved before shipping (BAE Cl. 41)",
         "ET Sec.7 p.30: 1 month before end of contract \u2014 Required for equipment release to site"),

    # NEW 06-Apr-2026: identified in TM N13 NOTE-02 as required deliverable prior to IFC
    (81, "Cable Tray Layout Drawings",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "TM N13 NOTE-02: routing from LCP/MCC to all load endpoints (BH-09-001, BH-09-002, antiscalant dosing pump, CIP heater, instrumentation) not submitted. Separate deliverable from Power Works installation details. Required prior to IFC (Rev 0).",
         "ET Sec.7: Max. 90 days from NTP"),
]


def get_verdict_fill(verdict):
    v = str(verdict).strip()
    if v.startswith("1-"):
        return FILL_GREEN
    elif v.startswith("2-"):
        return FILL_YELLOW
    elif v.startswith("3-"):
        return FILL_ORANGE
    elif v.startswith("4-"):
        return FILL_RED
    elif v == "Under review":
        return FILL_BLUE
    elif v == "--" or v == "":
        return FILL_GRAY
    return None


def generar_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Master Register"

    # Column widths (#, Document, Code/ET Ref, Rev, Delivery, TM, Verdict, Status, Action Required, ET Deadline)
    col_widths = [4, 38, 26, 5, 8, 5, 18, 18, 52, 38]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # Header row
    for col, header in enumerate(HEADERS, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = THIN_BORDER

    # Freeze header
    ws.freeze_panes = "A2"

    # Auto-filter
    ws.auto_filter.ref = f"A1:J{len(DATA) + 1}"

    # Data rows
    for row_idx, row_data in enumerate(DATA, 2):
        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = FONT_NORMAL
            cell.border = THIN_BORDER
            cell.alignment = Alignment(vertical="center", wrap_text=True)

            # Center short columns
            if col_idx in (1, 4, 5, 6):
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # Color by verdict (column 7) — applies to columns 1-9
        verdict = str(row_data[6])
        fill = get_verdict_fill(verdict)
        if fill:
            for col_idx in range(1, 10):
                ws.cell(row=row_idx, column=col_idx).fill = fill

        # Bold "NOT DELIVERED" and "PARTIAL" status
        status_val = str(row_data[7])
        if status_val in ("NOT DELIVERED", "PARTIAL"):
            for col_idx in range(1, len(HEADERS) + 1):
                ws.cell(row=row_idx, column=col_idx).font = FONT_BOLD

        # Color column 10 (ET Deadline) by milestone type
        deadline_val = str(row_data[9])
        deadline_cell = ws.cell(row=row_idx, column=10)
        deadline_cell.alignment = Alignment(vertical="center", wrap_text=True)
        if "1 month before end of contract" in deadline_val:
            deadline_cell.fill = FILL_DEADLINE_END
            deadline_cell.font = FONT_BOLD
        elif "NOT DELIVERED" in status_val or status_val == "PARTIAL":
            deadline_cell.fill = FILL_DEADLINE_NTP_LATE

    # Print setup
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0

    # ============================================================
    # LEGEND sheet
    # ============================================================
    ws2 = wb.create_sheet("Legend")
    ws2.column_dimensions["A"].width = 25
    ws2.column_dimensions["B"].width = 80

    legend_title   = Font(name="Arial", size=12, bold=True)
    legend_section = Font(name="Arial", size=10, bold=True)

    row = 1
    ws2.cell(row=row, column=1, value="DOCUMENT STATUS REGISTER - LEGEND").font = legend_title
    row += 2

    # --- References ---
    ws2.cell(row=row, column=1, value="REFERENCES").font = legend_section
    row += 1
    refs = [
        ("ET",            "Especificacion Tecnica P22-ET-09-000-001-0 (Technical Specification)"),
        ("ET Sec 7",      "Section 7 of the ET: contractual engineering deliverables (pp. 27-30)"),
        ("ET Sec 7, p.XX","Reference to page XX within Section 7 of the ET (pp. 27-30)"),
        ("ET 5.X",        "Reference to specific technical requirement section within the ET"),
        ("TM NX",         "ADASA Transmittal number X (N1 through N11)"),
        ("EX",            "BW Water delivery number X (E1 through E21, 21 deliveries)"),
        ("BAE Cl. XX",    "Bases Administrativas Especiales, clause XX"),
        ("NTP",           "Notice to Proceed (Notificacion de Adjudicacion)"),
    ]
    for term, desc in refs:
        ws2.cell(row=row, column=1, value=term).font = FONT_BOLD
        ws2.cell(row=row, column=2, value=desc).font = FONT_NORMAL
        row += 1

    row += 1

    # --- Verdicts ---
    ws2.cell(row=row, column=1, value="REVIEW VERDICTS").font = legend_section
    row += 1
    verdicts_legend = [
        ("1-Approved",             "Document accepted. No further action required.",                     FILL_GREEN),
        ("2-AN (Approved as Noted)","Accepted with observations. Minor notes or significant obs. pending.", FILL_YELLOW),
        ("3-To be revised",        "Document requires corrections and resubmission.",                    FILL_ORANGE),
        ("4-Rejected",             "Document rejected. Complete resubmission required.",                 FILL_RED),
        ("Under review",           "Document delivered but evaluation pending.",                         FILL_BLUE),
        ("-- (Not applicable)",    "Document not yet delivered. No verdict possible.",                   FILL_GRAY),
    ]
    for verdict, desc, fill in verdicts_legend:
        c1 = ws2.cell(row=row, column=1, value=verdict)
        c1.font = FONT_BOLD
        c1.fill = fill
        c2 = ws2.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        row += 1

    row += 1

    # --- Deadlines ---
    ws2.cell(row=row, column=1, value="CONTRACTUAL DEADLINES").font = legend_section
    row += 1
    deadlines = [
        ("Item #58 (Schedule)",  "Maximum 15 days from NTP (ET Section 7, p.27)"),
        ("Items #1-57",          "Maximum 90 days from NTP (ET Section 7, pp. 27-29)"),
        ("Items #75-79",         "1 month before end of contract (ET Section 7, pp. 29-30) \u2014 Prerequisite for equipment release to site"),
        ("PIE Detallado (#56)",  "90 days from NTP \u2014 Written approval required before manufacturing start (ET Sec.7 p.29)"),
    ]
    for term, desc in deadlines:
        c1 = ws2.cell(row=row, column=1, value=term)
        c1.font = FONT_BOLD
        c2 = ws2.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        if "75-79" in term:
            c1.fill = FILL_DEADLINE_END
            c2.fill = FILL_DEADLINE_END
        row += 1

    row += 1

    # --- Status values ---
    ws2.cell(row=row, column=1, value="STATUS VALUES").font = legend_section
    row += 1
    statuses_legend = [
        ("Delivered",           "Document received from BW Water and reviewed by ADASA"),
        ("Delivered (deficient)","Document received but substantially incomplete"),
        ("PARTIAL",             "Requirement partially covered; key elements still missing"),
        ("NOT DELIVERED",       "Document not submitted as of 23-Mar-2026"),
    ]
    for term, desc in statuses_legend:
        ws2.cell(row=row, column=1, value=term).font = FONT_BOLD
        ws2.cell(row=row, column=2, value=desc).font = FONT_NORMAL
        row += 1

    row += 2
    ws2.cell(row=row, column=1, value="Document:").font = FONT_BOLD
    ws2.cell(row=row, column=2,
             value="P22-IT-06-000-002-0 | Date: 27-Mar-2026 | Prepared by: Luis Rivera | Updated: TM N11 (E21) + Meeting 26-Mar-2026 + Advanced copies 27-Mar-2026").font = FONT_NORMAL

    wb.save(OUTPUT)
    print(f"Excel generado: {OUTPUT}")
    print(f"  Total items: {len(DATA)}")
    print(f"  Delivered:   {sum(1 for r in DATA if r[7] not in ('NOT DELIVERED', 'PARTIAL', 'Delivered (deficient)') and r[7] != '--')}")
    print(f"  Not delivered / partial: {sum(1 for r in DATA if r[7] in ('NOT DELIVERED', 'PARTIAL', 'Delivered (deficient)'))}")


if __name__ == "__main__":
    generar_excel()
