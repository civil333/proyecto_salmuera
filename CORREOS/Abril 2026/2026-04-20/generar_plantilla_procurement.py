"""
Plantilla Excel: Weekly Procurement Tracker - Project 12803 Taltal SWRO
Fecha: 21-Apr-2026
Salida: WEEKLY-PROCUREMENT-TRACKER_12803_v0.xlsx

Baseline: 05.03.26_12803_Taltal Water Treatment Plant.pdf (programa emitido por BW Water)
Alcance: 16 equipment lines (excluye RO Membrane que va bajo UHPRO separado).

ADASA pre-pobla solo datos contractualmente verificables:
  - Numero de linea, Equipment Line, TAG (del ET P22-ET-09-000-001-0), Baseline PR/PO Window.

BW Water completa cada semana las columnas restantes: PO Reference, PO Date, Supplier,
Country of Origin, Lead Time, ExWorks Date, Arrival Penang, Days vs Window, Status, Comment.

Esquema de status C/E/D/N (paralelo a Code 1/2/3/4 de revision de ingenieria).
"""

import os
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "WEEKLY-PROCUREMENT-TRACKER_12803_v0.xlsx")

# --- Paleta de colores ---
HEADER_FILL     = PatternFill("solid", fgColor="1F4E78")   # azul corporativo header
HEADER_FONT     = Font(bold=True, size=10, color="FFFFFF", name="Arial")
SUBHEADER_FILL  = PatternFill("solid", fgColor="D9E1F2")
INSTRUCTION_FILL = PatternFill("solid", fgColor="FFF2CC")  # amarillo suave instrucciones
BASELINE_FILL   = PatternFill("solid", fgColor="EDEDED")   # gris claro pre-poblado ADASA
BWW_FILL        = PatternFill("solid", fgColor="FFFFFF")   # blanco a llenar por BW Water
LEGEND_C_FILL   = PatternFill("solid", fgColor="C6EFCE")
LEGEND_E_FILL   = PatternFill("solid", fgColor="FFEB9C")
LEGEND_D_FILL   = PatternFill("solid", fgColor="FFC7CE")
LEGEND_N_FILL   = PatternFill("solid", fgColor="D9D9D9")

THIN = Side(style="thin", color="999999")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

ARIAL = "Arial"


# ============================================================================
#  HOJA 1 - WEEKLY DASHBOARD
# ============================================================================

DASHBOARD_HEADERS = [
    "#",                                       # A
    "Equipment Line",                          # B
    "TAG",                                     # C
    "Baseline PR/PO Window",                   # D
    "PO Reference",                            # E
    "PO Date",                                 # F
    "Supplier",                                # G
    "Country of Origin",                       # H
    "Lead Time (weeks)",                       # I
    "ExWorks Date",                            # J
    "Arrival Penang",                          # K
    "Days vs Window",                          # L
    "Status (C/E/D/N)",                        # M
    "Comment",                                 # N
]

DASHBOARD_COL_WIDTHS = [5, 34, 16, 22, 16, 12, 22, 14, 10, 13, 14, 14, 14, 55]

# 17 filas pre-poblates con Baseline Schedule issued by BW Water on 05-Mar-2026
# + RO Membranes (declarada en minuta BWW 20-Apr-2026). Ordenadas por fecha.
# Fuentes:
#   - estado_compras_09-03-26.md (programa BW Water 05-Mar-2026)
#   - LISTADO-CONSOLIDADO-EVI.xlsx (TAGs del ET P22-ET-09-000-001-0)
#   - Minuta BWW 20-Apr-2026 (respuesta Eduardo Yamauchi 10:24 AM):
#       * 9 items reportados con PO placed -> status C pre-poblado
#       * 3 items reportados como Upcoming -> status E pre-poblado
#       * Suppliers declarados: Fedco, Prominent
#       * RO Membranes: procurement en US, PO semana del 27-Apr (linea 17)
#
# Tuplas: (equipment, tag, window, supplier, origin, status, comment)
# supplier, origin, status, comment vacios donde BWW no se comprometio.

BWW_C = "PO placed per BWW 20-Apr-2026 meeting response. Awaiting PO reference and ExWorks date."
BWW_E_THIS = "PO target within the current week per BWW 20-Apr-2026 meeting response."
BWW_E_NEXT = "PO target next week per BWW 20-Apr-2026 meeting response."

EQUIPMENT_LINES = [
    # (equipment,                        tag,              window,             supplier,     origin, status, comment)
    ("RO High Feed Pump",                "BH-09-001",      "Mar 4 - 10",       "Fedco",      "",     "C",    BWW_C),
    ("Instrument Set",                   "",               "Mar 11 - 17",      "",           "",     "",     ""),
    ("All Valve Set",                    "",               "Mar 11 - 17",      "",           "",     "",     ""),
    ("CIP Heater",                       "REL-09-001",     "Mar 16 - 20",      "",           "",     "C",    BWW_C),
    ("Container (40 ft) + AC units",     "",               "Mar 18 - 24",      "",           "",     "C",    "PO placed per BWW 20-Apr-2026 meeting response (container + air conditioners). Awaiting PO reference and ExWorks date."),
    ("CIP / Flushing Cartridge Filter",  "FIL-09-002",     "Mar 23 - 27",      "",           "",     "E",    BWW_E_NEXT),
    ("CIP / Flushing Pumps",             "BH-09-002",      "Mar 25 - 31",      "",           "",     "E",    BWW_E_THIS),
    ("CIP / Flushing Tank",              "TK-09-001",      "Mar 27 - Apr 2",   "",           "",     "C",    BWW_C),
    ("RO Pressure Vessel / Tubes",       "BOI-09-001/002", "Mar 31 - Apr 6",   "",           "",     "C",    BWW_C),
    ("Feed Turbocharger",                "SIP-09-001",     "Apr 1 - 7",        "Fedco",      "",     "C",    BWW_C),
    ("Structural Frames / Supports",     "",               "Apr 6 - 10",       "",           "",     "",     ""),
    ("Antiscalant Dosing Tank",          "TK-09-002",      "Apr 7 - 13",       "",           "",     "C",    BWW_C),
    ("Antiscalant Dosing Pumps (Skid)",  "",               "Apr 10 - 16",      "Prominent",  "",     "C",    "PO placed per BWW 20-Apr-2026 meeting response. Supplier: Prominent. Awaiting PO reference and ExWorks date."),
    ("Interstage Turbocharger",          "SIP-09-002",     "Apr 24 - 30",      "Fedco",      "",     "C",    BWW_C),
    ("Static Mixer",                     "MZE-09-001",     "May 1 - 7",        "",           "",     "",     ""),
    ("RO Cartridge Filter",              "FIL-09-001",     "May 4 - 8",        "",           "",     "E",    BWW_E_NEXT),
    ("RO Membranes",                     "",               "Week of 27-Apr",   "",           "US",   "E",    "Procurement planned in US per BWW 20-Apr-2026 meeting response (PO by next week). Must be consolidated at Penang workshop before module ExWorks shipment."),
]


def build_dashboard(ws):
    # Fila 1: titulo del proyecto
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=14)
    c = ws.cell(row=1, column=1,
                value="Project 12803 - Taltal SWRO | Weekly Procurement Tracker")
    c.font = Font(bold=True, size=13, color="FFFFFF", name=ARIAL)
    c.fill = HEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 26

    # Fila 2: baseline + week ending
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=14)
    c = ws.cell(row=2, column=1,
                value=("Baseline: Schedule issued by BW Water on 05-Mar-2026  |  "
                       "Week ending: DD-MMM-YYYY  |  Template version: v0"))
    c.font = Font(bold=False, size=10, italic=True, name=ARIAL)
    c.fill = SUBHEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 18

    # Fila 3: nota de instrucciones + EXW Penang
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=14)
    c = ws.cell(row=3, column=1,
                value=("BW Water completes columns E-N each Monday by 10:00 AM Santiago time (CLT). "
                       "ADASA has pre-populated status C (Committed) and E (Enabled) where confirmed "
                       "by the BW Water meeting response of 20-Apr-2026 \u2014 BW Water to validate each line. "
                       "ExWorks reference point is BW Water Penang workshop, Malaysia: items procured "
                       "outside Malaysia (e.g. RO Membranes in US, Fedco equipment) must be consolidated "
                       "at Penang within lead time to support the Baseline FAT (25 Jul \u2013 1 Aug 2026)."))
    c.font = Font(bold=False, size=9, italic=True, name=ARIAL, color="7F6000")
    c.fill = INSTRUCTION_FILL
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[3].height = 56

    # Fila 4: header de columnas
    header_row = 4
    for col_idx, text in enumerate(DASHBOARD_HEADERS, start=1):
        c = ws.cell(row=header_row, column=col_idx, value=text)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[header_row].height = 32

    # Anchos de columna
    for col_idx, w in enumerate(DASHBOARD_COL_WIDTHS, start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    # Filas de datos (filas 5-21 para 17 lineas)
    start_data_row = 5
    # Color para celdas pre-pobladas por ADASA desde la minuta BWW 20-Apr
    # (supplier, origin, status, comment) - tono intermedio para distinguir
    # de baseline inmutable y de campos libres BWW.
    BWW_PREFILL = PatternFill("solid", fgColor="FFF9E6")  # amarillo muy suave

    for i, (equipment, tag, window, supplier, origin, status, comment) in enumerate(EQUIPMENT_LINES):
        r = start_data_row + i

        # Cols A-D: baseline (pre-poblado ADASA, fondo gris claro)
        ws.cell(row=r, column=1, value=i + 1)
        ws.cell(row=r, column=2, value=equipment)
        ws.cell(row=r, column=3, value=tag)
        ws.cell(row=r, column=4, value=window)
        for col in range(1, 5):
            cell = ws.cell(row=r, column=col)
            cell.fill = BASELINE_FILL
            cell.font = Font(bold=(col == 1), size=10, name=ARIAL)
            cell.alignment = Alignment(vertical="center",
                                       horizontal="center" if col in (1, 3) else "left",
                                       wrap_text=True)
            cell.border = BORDER

        # Pre-poblados desde minuta BWW 20-Apr (cols G, H, M, N cuando aplique)
        prefilled = {
            7: supplier,   # G Supplier
            8: origin,     # H Country of Origin
            13: status,    # M Status
            14: comment,   # N Comment
        }

        # A llenar por BW Water (cols E-N): base blanca, tintado suave si hay prefill
        for col in range(5, 15):
            val = prefilled.get(col, "") or None
            cell = ws.cell(row=r, column=col, value=val)
            if val:
                cell.fill = BWW_PREFILL  # amarillo suave = evidencia minuta BWW
                cell.font = Font(size=10, bold=(col == 13), name=ARIAL,
                                 color="000000" if col != 13 else "000000")
            else:
                cell.fill = BWW_FILL
                cell.font = Font(size=10, name=ARIAL)
            cell.alignment = Alignment(vertical="center",
                                       horizontal="center" if col in (6, 9, 10, 11, 12, 13) else "left",
                                       wrap_text=True)
            cell.border = BORDER

        # Altura mayor para filas con comentario pre-poblado (texto largo)
        ws.row_dimensions[r].height = 38 if comment else 22

    end_data_row = start_data_row + len(EQUIPMENT_LINES) - 1

    # Data validation: lista C/E/D/N en columna M
    dv = DataValidation(type="list", formula1='"C,E,D,N"', allow_blank=True,
                        showErrorMessage=True,
                        errorTitle="Invalid status",
                        error="Status must be one of: C, E, D, N (see Legend sheet).")
    dv.add(f"M{start_data_row}:M{end_data_row}")
    ws.add_data_validation(dv)

    # Formato condicional sobre Status (col M)
    status_range = f"M{start_data_row}:M{end_data_row}"
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"C"'], fill=LEGEND_C_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"E"'], fill=LEGEND_E_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"D"'], fill=LEGEND_D_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"N"'], fill=LEGEND_N_FILL))

    # Bloque de leyenda al pie (filas end_data_row+2 en adelante)
    legend_start = end_data_row + 2
    ws.merge_cells(start_row=legend_start, start_column=1, end_row=legend_start, end_column=14)
    c = ws.cell(row=legend_start, column=1,
                value="STATUS LEGEND  (aligned with ADASA engineering Codes 1 / 2 / 3 / 4)")
    c.font = Font(bold=True, size=11, name=ARIAL, color="FFFFFF")
    c.fill = HEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[legend_start].height = 22

    legend_rows = [
        ("C", "Committed",     "PO issued; supplier, reference and ExWorks date confirmed.",               LEGEND_C_FILL),
        ("E", "Enabled",       "Engineering Code 1 or 2; PO pending issuance.",                            LEGEND_E_FILL),
        ("D", "Delayed",       "PR/PO window closed without PO, variance >10 days, or blocker to downstream work. "
                               "Escalation to Fadey Kassim within 24 hours of detection.",                 LEGEND_D_FILL),
        ("N", "Not in Window", "Baseline window not yet reached; no action required.",                     LEGEND_N_FILL),
    ]
    for i, (letter, label, definition, fill) in enumerate(legend_rows):
        r = legend_start + 1 + i
        # Col A: letra
        c = ws.cell(row=r, column=1, value=letter)
        c.font = Font(bold=True, size=12, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = BORDER
        # Col B: label
        c = ws.cell(row=r, column=2, value=label)
        c.font = Font(bold=True, size=10, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="left", vertical="center")
        c.border = BORDER
        # Col C-N merged: definition
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=14)
        c = ws.cell(row=r, column=3, value=definition)
        c.font = Font(size=10, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        c.border = BORDER
        ws.row_dimensions[r].height = 22

    # Freeze panes bajo el header
    ws.freeze_panes = f"A{start_data_row}"


# ============================================================================
#  HOJA 2 - MILESTONE TRACKER
# ============================================================================

MILESTONE_HEADERS = [
    "Milestone", "Baseline Date",
    "Current Forecast", "Variance (days)", "Driver", "Status (C/E/D/N)",
]

MILESTONES = [
    ("Critical long-lead items arrival in Penang",   "Per line (see Weekly Dashboard)"),
    ("Fabrication start (Penang workshop)",          "Per Baseline 05-Mar-2026"),
    ("Factory Acceptance Test (FAT)",                "25 Jul - 1 Aug 2026"),
    ("Ready to Ship (EXW Penang)",                   "3 Aug 2026"),
    ("Shipment to Chile",                            "Per Baseline 05-Mar-2026"),
    ("Site arrival",                                 "Per Baseline 05-Mar-2026"),
    ("Site Supervision & Commissioning",             "18 Sep - 8 Oct 2026"),
    ("Operator Training",                            "9 Oct - 17 Oct 2026"),
    ("Final Documentation & Close out",              "18 Oct - 16 Nov 2026"),
]


def build_milestones(ws):
    # Titulo
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=6)
    c = ws.cell(row=1, column=1, value="Milestone Tracker - Baseline issued by BW Water on 05-Mar-2026")
    c.font = Font(bold=True, size=12, color="FFFFFF", name=ARIAL)
    c.fill = HEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 24

    # Header
    for col_idx, text in enumerate(MILESTONE_HEADERS, start=1):
        c = ws.cell(row=2, column=col_idx, value=text)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[2].height = 28

    # Anchos
    for col_idx, w in enumerate([42, 32, 22, 16, 36, 16], start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    start_row = 3
    for i, (name, baseline) in enumerate(MILESTONES):
        r = start_row + i
        ws.cell(row=r, column=1, value=name)
        ws.cell(row=r, column=2, value=baseline)
        for col in range(1, 3):
            cell = ws.cell(row=r, column=col)
            cell.fill = BASELINE_FILL
            cell.font = Font(size=10, bold=(col == 1), name=ARIAL)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            cell.border = BORDER
        for col in range(3, 7):
            cell = ws.cell(row=r, column=col, value=None)
            cell.fill = BWW_FILL
            cell.font = Font(size=10, name=ARIAL)
            cell.alignment = Alignment(vertical="center", horizontal="center")
            cell.border = BORDER
        ws.row_dimensions[r].height = 22

    end_row = start_row + len(MILESTONES) - 1

    # Data validation Status col F
    dv = DataValidation(type="list", formula1='"C,E,D,N"', allow_blank=True)
    dv.add(f"F{start_row}:F{end_row}")
    ws.add_data_validation(dv)

    status_range = f"F{start_row}:F{end_row}"
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"C"'], fill=LEGEND_C_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"E"'], fill=LEGEND_E_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"D"'], fill=LEGEND_D_FILL))
    ws.conditional_formatting.add(status_range,
        CellIsRule(operator="equal", formula=['"N"'], fill=LEGEND_N_FILL))

    ws.freeze_panes = "A3"


# ============================================================================
#  HOJA 3 - CHANGE LOG
# ============================================================================

CHANGE_LOG_HEADERS = [
    "Week ending", "Line #", "Equipment Line",
    "Field changed", "From", "To", "Reason", "Approved by",
]


def build_change_log(ws):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=8)
    c = ws.cell(row=1, column=1, value="Change Log - Weekly modifications across all sheets")
    c.font = Font(bold=True, size=12, color="FFFFFF", name=ARIAL)
    c.fill = HEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 24

    for col_idx, text in enumerate(CHANGE_LOG_HEADERS, start=1):
        c = ws.cell(row=2, column=col_idx, value=text)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[2].height = 28

    for col_idx, w in enumerate([14, 8, 30, 20, 22, 22, 34, 20], start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    # Instrucciones
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=8)
    c = ws.cell(row=3, column=1,
                value=("Add one row per modification. Purpose: auditability. If a baseline date or a PO "
                       "reference moves twice in the same month, this tab must make it visible."))
    c.font = Font(size=9, italic=True, name=ARIAL, color="7F6000")
    c.fill = INSTRUCTION_FILL
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[3].height = 24

    ws.freeze_panes = "A4"


# ============================================================================
#  HOJA 4 - LEGEND / STATUS CRITERIA
# ============================================================================

def build_legend(ws):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=3)
    c = ws.cell(row=1, column=1,
                value="Legend / Status Criteria  -  aligned with ADASA engineering Codes 1 / 2 / 3 / 4")
    c.font = Font(bold=True, size=12, color="FFFFFF", name=ARIAL)
    c.fill = HEADER_FILL
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 26

    headers = ["Letter", "Meaning", "Definition"]
    for col_idx, text in enumerate(headers, start=1):
        c = ws.cell(row=2, column=col_idx, value=text)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = BORDER
    ws.row_dimensions[2].height = 24

    for col_idx, w in enumerate([12, 22, 110], start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    legend_data = [
        ("C", "Committed",
         "Purchase order issued. Supplier, PO reference and ExWorks date confirmed in writing. "
         "Expected delivery aligned with the Baseline Schedule issued by BW Water on 05-Mar-2026. "
         "No action required beyond weekly confirmation that status is unchanged.",
         LEGEND_C_FILL),
        ("E", "Enabled",
         "Engineering review code allows procurement (Code 1 or Code 2 per the applicable Transmittal), "
         "but the purchase order has not yet been issued. BW Water must state in the Comment field the "
         "target PO date and any residual blocker.",
         LEGEND_E_FILL),
        ("D", "Delayed",
         "Baseline PR/PO window has closed without a confirmed purchase order, OR variance exceeds 10 "
         "calendar days against the baseline window, OR the line is blocking downstream engineering or "
         "fabrication. Triggers written escalation to Fadey Kassim (Senior VP Global Operations) within "
         "24 hours of detection, independent of the weekly report cadence.",
         LEGEND_D_FILL),
        ("N", "Not in Window",
         "The baseline PR/PO window has not yet been reached. No action required beyond keeping the line "
         "visible in the tracker. Transitions to E or C once the window opens.",
         LEGEND_N_FILL),
    ]

    for i, (letter, label, definition, fill) in enumerate(legend_data):
        r = 3 + i
        c = ws.cell(row=r, column=1, value=letter)
        c.font = Font(bold=True, size=14, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = BORDER

        c = ws.cell(row=r, column=2, value=label)
        c.font = Font(bold=True, size=11, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="left", vertical="center")
        c.border = BORDER

        c = ws.cell(row=r, column=3, value=definition)
        c.font = Font(size=10, name=ARIAL)
        c.fill = fill
        c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        c.border = BORDER
        ws.row_dimensions[r].height = 70

    # Nota final de correspondencia
    note_row = 3 + len(legend_data) + 1
    ws.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=3)
    c = ws.cell(row=note_row, column=1,
                value=("Cross-reference with engineering Codes - for context: "
                       "Code 1 (Approved) enables PO issuance same as C or E status.  "
                       "Code 2 (Approved as Noted) enables PO issuance in parallel with note resolution - status E.  "
                       "Code 3 (To Be Revised) holds procurement until next revision is approved.  "
                       "Code 4 (Rejected) holds procurement until corrective engineering is issued."))
    c.font = Font(size=9, italic=True, name=ARIAL, color="404040")
    c.fill = INSTRUCTION_FILL
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws.row_dimensions[note_row].height = 60


# ============================================================================
#  MAIN
# ============================================================================

def main():
    wb = openpyxl.Workbook()

    ws1 = wb.active
    ws1.title = "Weekly Dashboard"
    build_dashboard(ws1)

    ws2 = wb.create_sheet("Milestone Tracker")
    build_milestones(ws2)

    ws3 = wb.create_sheet("Change Log")
    build_change_log(ws3)

    ws4 = wb.create_sheet("Legend")
    build_legend(ws4)

    wb.save(OUTPUT)
    print(f"Plantilla generada: {OUTPUT}")


if __name__ == "__main__":
    main()
