#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Deliverable Register v3 — P22-IT-06-000-002-0
Genera Excel con 4 hojas:
  1. Master Register  — 89 items con estado actual TM N15 + gaps ET (23-Apr-2026)
  2. Revision History — historial completo de cada documento a traves de TM N1-N15
  3. Summary          — metricas del proyecto calculadas dinamicamente
  4. Legend           — referencias actualizadas

Cambios vs v2:
  BLOQUE A — Avances TM N15 (22-Apr-2026, E30-E33):
    - 7 items actualizados (16, 27, 28, 35, 40, 45, 67) con datos TM N15
    - 3 items nuevos (81 LCP, 82 Equipment Layout, 83 GA SWRO Skid)
    - Item 81 previo (Cable Tray Layout Drawings) eliminado — colapsado en item 28
    - 3500 mm constraint (TM N5 OBS-01 / TM N7 OBS-01) WITHDRAWN por ADASA
  BLOQUE B — Cross-check ET (6 gaps detectados en pp. 26-33):
    - Item 84: Plan de NDE (ET Seccion 8 p.31)
    - Item 85: Procedimiento FAT (ET Seccion 8.1 pp.31-33)
    - Item 86: Informe PMI Super Duplex (ET Seccion 8 p.31)
    - Item 87: Informe Final de Comisionamiento (ET Seccion 9 p.33)
    - Item 88: Informe Final de Puesta en Marcha (ET Seccion 9 p.33)
    - Item 89: Material de Capacitacion ADASA (ET Seccion 9 p.34)

Generado: 23-Apr-2026
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT = "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx"

# --- Colores por verdict ---
FILL_GREEN  = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
FILL_YELLOW = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
FILL_ORANGE = PatternFill(start_color="FCD5B4", end_color="FCD5B4", fill_type="solid")
FILL_RED    = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
FILL_GRAY   = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
FILL_BLUE   = PatternFill(start_color="BDD7EE", end_color="BDD7EE", fill_type="solid")
FILL_HEADER = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
FILL_SECTION = PatternFill(start_color="D6DCE4", end_color="D6DCE4", fill_type="solid")

FONT_HEADER = Font(name="Arial", size=10, bold=True, color="FFFFFF")
FONT_NORMAL = Font(name="Arial", size=9)
FONT_BOLD   = Font(name="Arial", size=9, bold=True)
FONT_TITLE  = Font(name="Arial", size=14, bold=True)
FONT_SECTION = Font(name="Arial", size=11, bold=True)
THIN_BORDER = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"),  bottom=Side(style="thin"),
)

FILL_DEADLINE_END      = PatternFill(start_color="FFB3B3", end_color="FFB3B3", fill_type="solid")
FILL_DEADLINE_NTP_LATE = PatternFill(start_color="FFE4B5", end_color="FFE4B5", fill_type="solid")

# ============================================================
# MASTER REGISTER DATA (81 items — corregido TM N14)
# ============================================================
HEADERS = ["#", "Document", "Code / ET Reference", "Rev", "Delivery", "TM",
           "Verdict", "Status", "Action Required", "ET Deadline"]

DATA_MASTER = [
    # =========================================================
    # DELIVERED (59 items)
    # =========================================================
    (1,  "PFD",
         "P22-DWG-09-009-001", "B", "E8", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (2,  "P&ID",
         "P22-DWG-09-009-002", "C", "E24", "N13", "2-AN", "Delivered",
         "Rev C approved as noted (TM N13, 06-Apr-2026). NOTE-01: TK-09-001 (CIP Tank) 6.81 m\u00b3 in P&ID vs 6.1 m\u00b3 in Equipment List Rev B \u2014 confirm and correct prior to IFC Rev 0. Title block code '-002' CLOSED (TM N9 NOTE-01).",
         "ET Sec.7: Max. 90 days from NTP"),

    (3,  "Process Calculation",
         "P22-CD-09-009-001", "B", "E7", "N2", "2-AN", "Delivered",
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

    # UPDATED TM N15: Rev B->C, E14->E31, N7->N15, 3-TBR->2-AN
    (16, "A/C Thermal Calculation",
         "P22-CD-09-005-002", "C", "E31", "N15", "2-AN", "Delivered",
         "Rev C approved as noted (TM N15, 22-Apr-2026). Closes TM N2 OBS-02 (180+ days) by consolidating all container loads in heat balance. NOTE-02 (MAJOR): selected 2.5 HP / 2.01 TR unit marginal vs 2.04 TR calculated demand (0.03 TR deficit); confirm n+1 \u2014 each unit 100% load independently \u2014 prior to IFC Rev 0.",
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

    # UPDATED TM N15: Rev B->C, E21->E31, N11->N15, 3-TBR->2-AN
    (27, "Grounding Layout",
         "P22-DWG-09-007-003", "C", "E31", "N15", "2-AN", "Delivered",
         "Rev C approved as noted (TM N15). Aligned to Piping Layout Rev B. TM N11 OBS-03 base CLOSED. NOTE-03 (MAJOR): grounding schedule completeness required (PE identifiers, conductor cross-section, ring main topology, equipotential bonding) per NCh Elec 4/2003 Seccion 10.0 \u2014 resolve prior to IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N15: Rev A->B, E11->E32, N4->N15, stays 3-TBR (new OBS-04/08)
    (28, "Cable Tray Layout",
         "P22-DWG-09-007-004", "B", "E32", "N15", "3-To be revised", "Delivered",
         "Rev C required (TM N15). Five new MAJOR observations: OBS-04 support S4 conflicts with TK-09-002; OBS-05 UNISTRUT anchoring not detailed; OBS-06 MAIN PANEL incoming routing not indicated; OBS-07 S3/S4 zoning ambiguous; OBS-08 CIP conflict. Plus TM N4 OBS-05/06/07 still open (78 days). Itemize closure on Rev C consolidated comment sheet.",
         "ET Sec.7: Max. 90 days from NTP"),

    (29, "DS PLC & HMI",
         "P22-ET-09-008-001", "A", "E1", "N1", "2-AN", "Delivered",
         "Minor notes",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N14: Rev D, E26, N14, 1-Approved
    (30, "Control Architecture",
         "P22-CD-09-004-001", "D", "E26", "N14", "1-Approved", "Delivered",
         "Rev D approved (TM N14). UPS 8h verified (40Ah \u00f7 4.35A = 9.2h). All TM N10 observations closed.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N14: Rev C, E28, N14, 2-AN
    (31, "IO List",
         "P22-LI-09-008-001", "C", "E28", "N14", "2-AN", "Delivered",
         "Rev C approved as noted (TM N14). NOTE-02 (MAJOR): analyzer power supply voltage discrepancy \u2014 220VAC in REMARKS vs 24VDC in IL/CCS/Rosemount 1056 DS. Resolve before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N14: Rev C, E28, N14, 2-AN
    (32, "Instrument List",
         "P22-LI-09-008-003", "C", "E28", "N14", "2-AN", "Delivered",
         "Rev C approved as noted (TM N14). TM N8 OBS-03 conductivity CLOSED (toroidal confirmed). NOTE-03: vibration calibrated range 0\u2013127 mm/s vs DTL 0\u201325 mm/s \u2014 align before IFC. NOTE-04: working medium labels show 'Filtered Water' for brine-side instruments \u2014 correct before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev C->D, E19->E27, N11->N14, 3-TBR->2-AN
    (33, "Valve List",
         "P22-LI-09-005-002", "D", "E27", "N14", "2-AN", "Delivered",
         "Rev D approved as noted (TM N14). All duplicates resolved. NOTE-01 (MAJOR): PSV-09-002 item 112 removed \u2014 overpressure protection analysis required, or reinstate with unique TAG prior to IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (34, "Equipment List",
         "P22-LI-09-005-001", "B", "E20", "N11", "2-AN", "Delivered",
         "Rev B approved as noted (TM N11). Minor notes.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N15: Rev B->C, E21->E32, N11->N15, 3-TBR->2-AN
    (35, "Instrument Location Layout",
         "P22-DWG-09-008-001", "C", "E32", "N15", "2-AN", "Delivered",
         "Rev C approved as noted (TM N15). Aligned to Piping Layout Rev B. Closes TM N3 OBS-01/02/03 and TM N11 OBS-04. NOTE-10 (MINOR): dependency on Equipment Layout Rev B and Piping Layout Rev B acceptance \u2014 no further action if both accepted as currently configured.",
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

    # UPDATED TM N15: Rev A->B, E14->E32, N7->N15, 3-TBR->2-AN (3500mm WITHDRAWN)
    # Consolidation: covers former item #61 (bucket placeholder removed)
    (40, "Piping Layout",
         "P22-DWG-09-005-004", "B", "E32", "N15", "2-AN", "Delivered",
         "Rev B approved as noted (TM N15). 3,500 mm CIP/dosing footprint constraint (TM N5 OBS-01 / TM N7 OBS-01) WITHDRAWN by ADASA \u2014 superseded by P22-DWG-06-006-101. NOTE-06 equipment access door / lateral sliding door not represented; NOTE-07 cabinet integration unclear (LCP routing); NOTE-08 antiscalant/CIP module-boundary flanges to confirm; NOTE-09 tie-in elevation view missing \u2014 all to incorporate in Rev 0. | Covers ETE Seccion 7 p.28 'Planos de arreglo de equipos y canerias en planta y elevacion' (piping scope).",
         "ET Sec.7: Max. 90 days from NTP"),

    (41, "Tie-In Point Layout",
         "P22-DWG-09-005-005", "A", "E14", "N7", "3-To be revised", "Delivered",
         "Rev B required after Piping Layout Rev B accepted. Preliminary Rev C received 14-Apr-2026 (PRELIMINAR LAYOUT 2) \u2014 formal submittal pending.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E15->E28, N8->N14, 2-AN->1-Approved
    (42, "DS Conductivity Analyzer",
         "P22-LI-09-008-005", "B", "E28", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). Toroidal (Rosemount 228) for brine, contacting (Rosemount 400) for permeate. TM N8 OBS-03 CLOSED.",
         "ET Sec.7: Max. 90 days from NTP"),

    (43, "DS DP Switch",
         "P22-LI-09-008-006", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E15->E29, N8->N14, 2-AN->1-Approved
    (44, "DS Flow Transmitter",
         "P22-LI-09-008-007", "B", "E29", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). Fluid medium corrected to Concentrated Brine for FIT-09-004. Power supply aligned to 12-42 VDC. TM N8 notes resolved.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N15: Rev A->B, E15->E30, N8->N15, 2-AN->1-Approved
    (45, "DS Level Switch",
         "P22-LI-09-008-008", "B", "E30", "N15", "1-Approved", "Delivered",
         "Rev B approved (TM N15). Capacitive IFM KQ6005 for LS-09-001/002 consistent with Instrument List Rev C and IO List Rev C. NOTE-01 (MINOR): communication interface label inconsistency (4-20 mA HART vs IO-Link per IFM KQ6005 PNP discrete) \u2014 align before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (46, "DS Level Transmitter",
         "P22-LI-09-008-009", "A", "E15", "N8", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E15->E28, N8->N14, 1-App->1-Approved
    (47, "DS pH/ORP Analyzer",
         "P22-LI-09-008-010", "B", "E28", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). TAG alignment: ORPIT-09-001\u2192ORPIT-09-001A, PHIT-09-001\u2192PHIT-09-006 per P&ID Rev C.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E15->E27, N8->N14, 1-App->1-Approved
    (48, "DS Pressure Gauge",
         "P22-LI-09-008-011", "B", "E27", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). Diaphragm seal changed to Wika 990.31 (PP/EPDM) for PVC piping compatibility in CIP/antiscalant service.",
         "ET Sec.7: Max. 90 days from NTP"),

    (49, "DS Pressure Transmitter",
         "P22-LI-09-008-012", "A", "E15", "N8", "2-AN", "Delivered",
         "Minor notes per TM N8.",
         "ET Sec.7: Max. 90 days from NTP"),

    (50, "Power Works Drawing",
         "P22-DWG-09-007-005", "B", "E25", "N13", "2-AN", "Delivered",
         "Rev B approved as noted (TM N13). TM N8 OBS-01/02 CLOSED. NOTE-01: grounding conductor sizing basis not cited per NEC 250.122. NOTE-02: Cable Tray Layout drawings not submitted. NOTE-03: ADASA duct bank interface data required.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E16->E28, N8->N14, 3-TBR->1-Approved
    (51, "DS Temperature Transmitter",
         "P22-LI-09-008-013", "B", "E28", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). TM N8 OBS-01/02/03 CLOSED. TIT-09-006 (CIP Tank): Rosemount 214C + 644, 4-20mA HART, flange DN40.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E18->E28, N10->N14, 2-AN->2-AN
    (52, "Data Transfer List (Modbus TCP)",
         "P22-LI-09-008-004", "B", "E28", "N14", "2-AN", "Delivered",
         "Rev B approved as noted (TM N14). TM N10 OBS-01/02/03 CLOSED. NOTE-05: vibration transmitter Modbus scaled range 0-25 mm/s may need updating for Wilcoxon PCH420V-M12 \u2014 align with IL before IFC Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    (53, "GA Antiscalant Dosing Tank",
         "P22-DWG-09-005-015", "A", "E18", "N10", "2-AN", "Delivered",
         "Approved as noted (TM N10). Minor notes.",
         "ET Sec.7: Max. 90 days from NTP"),

    (54, "GA Feed Turbocharger (SIP-09-001)",
         "P22-DWG-09-005-012", "B", "E18", "N10", "1-Approved", "Delivered",
         "Rev B approved (TM N10). Vibration transducer mounting resolved.",
         "ET Sec.7: Max. 90 days from NTP"),

    (55, "GA Interstage Turbocharger (SIP-09-002)",
         "P22-DWG-09-005-013", "B", "E18", "N10", "1-Approved", "Delivered",
         "Rev B approved (TM N10). Vibration transducer mounting resolved.",
         "ET Sec.7: Max. 90 days from NTP"),

    (56, "GA CIP/Flushing Pump",
         "P22-DWG-09-005-010", "A", "E20", "N11", "2-AN", "Delivered",
         "Approved as noted (TM N11).",
         "ET Sec.7: Max. 90 days from NTP"),

    (57, "GA Antiscalant Dosing Pump",
         "P22-DWG-09-005-011", "A", "E20", "N11", "2-AN", "Delivered",
         "Approved as noted (TM N11).",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E22->E28, N12->N14, 3-TBR->1-Approved
    (58, "DS Vibration Transmitter",
         "P22-LI-09-008-014", "B", "E28", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). Wilcoxon PCH420V-M12 replaces IFM VTV122. HART 7.0 confirmed. TM N12 OBS-01 CLOSED.",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # NOT DELIVERED / PARTIAL (22 items)
    # =========================================================
    (59, "Detailed Schedule",
         "ET Sec 7, p.27", "--", "--", "--", "Under review", "Delivered (deficient)",
         "Mar-2026 Baseline: FAT and commissioning reinstated (positive). STILL MISSING: document-level milestones. 15 pending deliverables and 14 open observations require individual dates. Recovery plan required for meeting 09-Mar-2026.",
         "ET Sec.7: Max. 15 days from NTP"),

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
         "Lists delivered but brands/models incomplete for some items",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N15: Rev A->B, E14->E33, N7->N15, stays 3-TBR (17 notes, 1 CRITICAL)
    (67, "Control Philosophy",
         "P22-BT-09-009-001", "B", "E33", "N15", "3-To be revised", "Delivered",
         "Rev C required (TM N15). 17 detailed findings (NOTE-13 to NOTE-29) from cross-check vs P&ID Rev C, Valve List Rev D, IO List Rev C, Instrument List Rev C and Technical Offer Rev1. NOTE-20 (CRITICAL): HP Pump start permissive contains erroneous TAGs (VE-09-007 duplicated; VE-09-014 antiscalant tank inlet wrongly included). Also MAJOR: SEC formula/contract guarantee alignment (NOTE-13), vibration setpoints (14), antiscalant dosing source flow (15), VE-09-002 modulating logic (16), CIP cycle valve sequence (17), FIT-09-001 TAG reuse (21), Salt Rejection formula (22), orphan TAGs (23), child document commitments (24), SEC monitoring bus (25), network redundancy (26), ET Seccion 5.4/Seccion 7 unmet requirements (27), off-spec routing interlocks (28).",
         "ET Sec.7: Max. 90 days from NTP"),

    (68, "HMI Screen Design",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "69 days outstanding since TM N4 commitment. Operator interface undefined.",
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

    # UPDATED: 103 days open as of 15-Apr-2026
    (75, "Modbus TCP Memory Map",
         "ET 5.4 + TM N2", "--", "--", "--", "--", "NOT DELIVERED",
         "103 days open as of 15-Apr-2026 \u2014 no progress reported since TM N2. Integration planning blocked. Required before Control Philosophy Rev B can be finalized.",
         "ET Sec.5.4: Max. 90 days from NTP"),

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

    # =========================================================
    # NEW TM N15 (22-Apr-2026) — Items 81, 82, 83
    # =========================================================
    # Consolidation: covers former item #74 MCC Datasheet (removed)
    (81, "Datasheet Local Control Panel (LCP)",
         "P22-ET-09-007-005", "A", "E31", "N15", "3-To be revised", "Delivered",
         "Rev B required (TM N15). First revision. Panel-level header not populated preventing validation against Control System Architecture Rev D. OBS-01 (MAJOR): I/O module configuration and motor RTD channel count not declared (8 Pt-100 channels required per Instrument List Rev C). OBS-02 (MAJOR): panel IP rating and ambient class not declared (IP54 minimum expected). OBS-03 (MINOR): power consumption inconsistency (Load List Rev A 1.0 kW vs AC Thermal Calc Rev C 0.14 kW). | Covers ETE Seccion 5.4 combined panel per vendor catalogs in Rev A: PLC/RIO/LCP enclosure (nVent Hoffman FS66S IP66 316L) + VFDs (ABB ACS580) + MCCBs (ABB XT1N/XT3N/XT5N). No separate MCC Datasheet required.",
         "ET Sec.7: Max. 90 days from NTP"),

    # Consolidation: covers former items #60 (General Layouts) and #61 (Arrangement Drawings) bucket placeholders
    (82, "Equipment Layout",
         "P22-DWG-09-005-003", "B", "E32", "N15", "2-AN", "Delivered",
         "Rev B approved as noted (TM N15). Container 40 ft within ET envelope. 16-item equipment list consistent with P&ID Rev C. Section views confirm doors (pedestrian, equipment access, emergency, lateral sliding). Closes TM N5 OBS-03/04/05. NOTE-04 (MAJOR): Operating Weight table to embed in Rev 0 (IFC); BW Water Civil Loading drawing committed for 23-Apr-2026 and accepted as separate supporting deliverable. TM N5 OBS-01/02 partially open (CIP numbering, imperial dimensions). | Covers ETE Seccion 7 p.27 'Layouts' (general module arrangement) and p.28 'Planos de arreglo de equipos y canerias en planta y elevacion' (equipment scope).",
         "ET Sec.7: Max. 90 days from NTP"),

    (83, "GA of SWRO System Skid",
         "P22-DWG-09-005-008", "A", "E33", "N15", "2-AN", "Delivered",
         "Rev A approved as noted (TM N15). First revision. Two-sheet GA showing skid envelope, pressure vessel groupings, HP Pump, turbochargers, PSV and process valves. Consistent with Equipment Layout Rev B and Valve List Rev D. NOTE-11 (MAJOR): equipment and valve schedule not provided (vessels per stage, elements per vessel, manifold material/pressure rating, function-vs-tag matrix). NOTE-12 (MAJOR): design pressure and material schedule for skid piping not summarized (ANSI class per service, P-T ratings, wall thickness).",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # ET GAPS DETECTED (23-Apr-2026 cross-check) — Items 84-89
    # =========================================================
    (84, "Plan de Ensayos No Destructivos (NDE) \u2014 Super Duplex",
         "ET Seccion 8, p.31", "--", "--", "--", "--", "NOT DELIVERED",
         "Plan de NDE detallado para todas las soldaduras del sistema de alta presion (Super Duplex UNS S32750). Debe especificar tipo de ensayo (RT, UT, PT, VT), porcentaje de cobertura por tipo de junta y criterios de aceptacion segun ASME B31.3. Minimo requerido: 100% VT, 100% PT (raiz y final), 10% RT/UT en circunferenciales criticas. Sujeto a aprobacion ADASA \u2014 requisito previo a fabricacion de alta presion.",
         "ET Sec.8 p.31: Prerequisite for HP fabrication start"),

    (85, "Procedimiento FAT (Factory Acceptance Tests)",
         "ET Seccion 8.1, pp.31-33", "--", "--", "--", "--", "NOT DELIVERED",
         "Procedimiento detallado FAT propuesto por el Proveedor para aprobacion ADASA. Alcance minimo: aprobacion procedimiento, inspeccion visual y dimensional, integridad montaje mecanico, pruebas funcionales en seco, verificacion sistema I&C con simulacion dinamica de escenarios de fallo, revision documental preliminar, conformidad con normativa SEC Chile (Hold Point previo embarque). Pruebas hidrostaticas completadas como prerrequisito.",
         "ET Sec.8.1: Prerequisite for factory acceptance and shipment"),

    (86, "Informe PMI (Positive Material Identification)",
         "ET Seccion 8, p.31", "--", "--", "--", "--", "NOT DELIVERED",
         "Identificacion Positiva de Materiales mediante metodo espectrografico en al menos 10% de componentes Super Duplex UNS S32750 del circuito de alta presion (tuberias, accesorios, cuerpos de valvula, bridas). Resultados deben confirmar conformidad con especificacion UNS S32750 y forman parte del Dossier de Calidad. ADASA se reserva derecho de testificar (Punto W).",
         "ET Sec.8: Prerequisite for HP component release"),

    (87, "Informe Final de Comisionamiento",
         "ET Seccion 9, p.33", "--", "--", "--", "--", "NOT DELIVERED",
         "Informe final separado para la fase de comisionamiento segun ET Seccion 9. Documenta actividades, registros y resultados. Periodo efectivo comisionamiento + puesta en marcha no debe exceder 21 dias corridos. Requiere Responsable Integracion Modulo y Procesista con 10+ anios experiencia c/u en RO modular.",
         "ET Sec.9: Post-installation phase deliverable"),

    (88, "Informe Final de Puesta en Marcha",
         "ET Seccion 9, p.33", "--", "--", "--", "--", "NOT DELIVERED",
         "Informe final separado para la fase de puesta en marcha segun ET Seccion 9. Incluye supervision del sistema hasta la entrada en regimen y pruebas de desempeno que corroboren el correcto funcionamiento. Prerrequisito para Recepcion Provisional (ET Seccion 10).",
         "ET Sec.9: Post-commissioning phase deliverable"),

    (89, "Material de Capacitacion Personal ADASA",
         "ET Seccion 9, p.34", "--", "--", "--", "--", "NOT DELIVERED",
         "Material de entrenamiento para personal ADASA a cargo de la operacion. Temario minimo: disenos avanzados de RO, cuantificacion de beneficios (huella de carbono, ROI, ahorro energia/agua), diseno y modelacion de membranas UHPRO, uso del software de proyeccion de membranas, analisis de datos para proyeccion de CIP de membranas UHPRO. Informe final separado de capacitacion.",
         "ET Sec.9: Training phase deliverable"),
]


# ============================================================
# REVISION HISTORY DATA
# ============================================================
# (item#, document, code, rev, delivery, submittal, TM, TM_date, verdict, cycle, observations)
HISTORY_HEADERS = ["#", "Document", "Code / ET Reference", "Rev", "Delivery",
                   "Submittal", "TM", "TM Date", "Verdict", "Cycle", "Key Observations"]

REVISION_HISTORY = [
    # --- Item 1: PFD ---
    (1, "PFD", "P22-DWG-09-009-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "4-Rejected", 1,
     "Rejected: missing turbocharger modeling, incomplete"),
    (1, "PFD", "P22-DWG-09-009-001", "B", "E8", "25007-0008", "N3", "28-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 2: P&ID ---
    (2, "P&ID", "P22-DWG-09-009-002", "A", "E3", "25007-0003", "N2", "26-Jan-2026", "2-AN", 1,
     "Battery limits incomplete, line TAGs missing"),
    (2, "P&ID", "P22-DWG-09-009-002", "B", "E17", "25007-0017", "N9", "11-Mar-2026", "2-AN", 2,
     "TM N2 OBS-01 to OBS-14 all CLOSED. Minor notes"),
    (2, "P&ID", "P22-DWG-09-009-002", "C", "E24", "25007-0024", "N13", "06-Apr-2026", "2-AN", 3,
     "NOTE-01: CIP Tank capacity discrepancy 6.81 vs 6.1 m3"),

    # --- Item 3: Process Calculation ---
    (3, "Process Calculation", "P22-CD-09-009-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "4-Rejected", 1,
     "Rejected: no turbocharger modeling, pressure margins insufficient"),
    (3, "Process Calculation", "P22-CD-09-009-001", "B", "E7", "25007-0007", "N2", "26-Jan-2026", "2-AN", 2,
     "Validates design: 10% pressure margin, BiTurbo model, 42.86% recovery"),

    # --- Item 4: DS UHPRO System ---
    (4, "DS UHPRO System", "P22-ET-09-009-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised: ITEM code, incomplete specs"),
    (4, "DS UHPRO System", "P22-ET-09-009-001", "B", "E6", "25007-0006", "N2", "26-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 5: DS HP Pump ---
    (5, "DS HP Pump", "P22-ET-09-009-002", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "4-Rejected", 1,
     "Rejected: ITEM code, missing Pt-100, incomplete specs"),
    (5, "DS HP Pump", "P22-ET-09-009-002", "C", "E13", "25007-0013", "N6", "27-Feb-2026", "2-AN", 2,
     "Pt-100 motor windings confirmed"),
    (5, "DS HP Pump", "P22-ET-09-009-002", "D", "E19", "25007-0019", "N11", "17-Mar-2026", "2-AN", 3,
     "FEDCO coupling datasheet pending. PO may proceed"),

    # --- Item 6: DS CIP Pump ---
    (6, "DS CIP Pump", "P22-ET-09-009-003", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "4-Rejected", 1,
     "Rejected: ITEM code, VFD vs direct start"),
    (6, "DS CIP Pump", "P22-ET-09-009-003", "B", "E6", "25007-0006", "N2", "26-Jan-2026", "2-AN", 2,
     "VFD to direct start accepted"),

    # --- Item 7: DS Antiscalant Pump ---
    (7, "DS Antiscalant Pump", "P22-ET-09-009-004", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "2-AN", 1,
     "Minor notes"),
    (7, "DS Antiscalant Pump", "P22-ET-09-009-004", "B", "E7", "25007-0007", "N3", "28-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 8: DS RO Container ---
    (8, "DS RO Container", "P22-ET-09-000-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "4-Rejected", 1,
     "Rejected: dimensions, door specs incomplete"),
    (8, "DS RO Container", "P22-ET-09-000-001", "B", "E8", "25007-0008", "N3", "28-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 9: DS RO Cartridge Filter ---
    (9, "DS RO Cartridge Filter", "P22-ET-09-009-005", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised"),
    (9, "DS RO Cartridge Filter", "P22-ET-09-009-005", "C", "E13", "25007-0013", "N6", "27-Feb-2026", "2-AN", 2,
     "12 cartridges justified"),

    # --- Item 10: DS CIP Cartridge Filter ---
    (10, "DS CIP Cartridge Filter", "P22-ET-09-009-006", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised"),
    (10, "DS CIP Cartridge Filter", "P22-ET-09-009-006", "B", "E6", "25007-0006", "N2", "26-Jan-2026", "2-AN", 2,
     "Minor notes"),

    # --- Item 11: DS Feed Turbocharger ---
    (11, "DS Feed Turbocharger", "P22-ET-09-009-007", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised: incomplete specs"),
    (11, "DS Feed Turbocharger", "P22-ET-09-009-007", "C", "E13", "25007-0013", "N6", "27-Feb-2026", "4-Rejected", 2,
     "REJECTED: coupling downgraded from 2000 to 1200 psi"),
    (11, "DS Feed Turbocharger", "P22-ET-09-009-007", "D", "E19", "25007-0019", "N11", "17-Mar-2026", "2-AN", 3,
     "Coupling pressure resolved. NOTE-03: coupling label pending"),

    # --- Item 12: DS Interstage Turbocharger ---
    (12, "DS Interstage Turbocharger", "P22-ET-09-009-008", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised: incomplete specs"),
    (12, "DS Interstage Turbocharger", "P22-ET-09-009-008", "C", "E13", "25007-0013", "N6", "27-Feb-2026", "2-AN", 2,
     "Approved as noted"),
    (12, "DS Interstage Turbocharger", "P22-ET-09-009-008", "D", "E19", "25007-0019", "N11", "17-Mar-2026", "2-AN", 3,
     "NOTE-04: coupling label update pending"),

    # --- Item 13: DS CIP Tank ---
    (13, "DS CIP Tank", "P22-ET-09-009-010", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised"),
    (13, "DS CIP Tank", "P22-ET-09-009-010", "B", "E7", "25007-0007", "N3", "28-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 14: DS Antiscalant Dosing Tank ---
    (14, "DS Antiscalant Dosing Tank", "P22-ET-09-009-011", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised"),
    (14, "DS Antiscalant Dosing Tank", "P22-ET-09-009-011", "B", "E10", "25007-0010", "N4", "05-Feb-2026", "2-AN", 2,
     "Minor notes"),

    # --- Item 15: DS CIP Tank Heater ---
    (15, "DS CIP Tank Heater", "P22-ET-09-009-014", "A", "E2", "25007-0002", "N1", "16-Dec-2025", "3-To be revised", 1,
     "To be revised"),
    (15, "DS CIP Tank Heater", "P22-ET-09-009-014", "B", "E8", "25007-0008", "N3", "28-Jan-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 16: A/C Thermal Calculation ---
    (16, "A/C Thermal Calculation", "P22-CD-09-005-002", "A", "E5", "25007-0005", "N2", "26-Jan-2026", "3-To be revised", 1,
     "Undersized: 5.96 kW vs 11-15 kW expected. No n+1 config"),
    (16, "A/C Thermal Calculation", "P22-CD-09-005-002", "B", "E14", "25007-0014", "N7", "08-Mar-2026", "3-To be revised", 2,
     "Thermal loads still incomplete. n+1 not established"),

    # --- Item 17: DS Static Mixer ---
    (17, "DS Static Mixer", "P22-ET-09-009-012", "A", "E5", "25007-0005", "N2", "26-Jan-2026", "3-To be revised", 1,
     "Material change FRP to PVC requires justification"),
    (17, "DS Static Mixer", "P22-ET-09-009-012", "B", "E13", "25007-0013", "N6", "27-Feb-2026", "2-AN", 2,
     "TAG MZE-09-001 vs P&ID to confirm"),

    # --- Item 18: Piping Specifications (single cycle) ---
    (18, "Piping Specifications", "P22-ET-09-005-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "1-Approved", 1,
     "Approved"),

    # --- Item 19: Painting Specifications ---
    (19, "Painting Specifications", "P22-ET-09-005-002", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "2-AN", 1,
     "Minor notes"),
    (19, "Painting Specifications", "P22-ET-09-005-002", "B", "E19", "25007-0019", "N11", "17-Mar-2026", "1-Approved", 2,
     "Approved"),

    # --- Item 20: Single Line Diagram (single cycle) ---
    (20, "Single Line Diagram", "P22-CD-09-007-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "1-Approved", 1,
     "Approved"),

    # --- Item 21: Electrical Load List (single cycle) ---
    (21, "Electrical Load List", "P22-LI-09-007-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "1-Approved", 1,
     "Approved"),

    # --- Item 22: DS Electrical Auxiliaries (single cycle) ---
    (22, "DS Electrical Auxiliaries", "P22-ET-09-007-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "1-Approved", 1,
     "Approved"),

    # --- Item 23: DS Power & Control Cable (single cycle) ---
    (23, "DS Power & Control Cable", "P22-ET-09-007-002", "A", "E9", "25007-0009", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 24: DS Cable Tray (single cycle) ---
    (24, "DS Cable Tray", "P22-ET-09-007-003", "A", "E9", "25007-0009", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 25: DS Conduit & Flexible (single cycle) ---
    (25, "DS Conduit & Flexible", "P22-ET-09-007-004", "A", "E9", "25007-0009", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 26: Power Cable Schedule (single cycle) ---
    (26, "Power Cable Schedule", "P22-LI-09-007-002", "A", "E9", "25007-0009", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 27: Grounding Layout ---
    (27, "Grounding Layout", "P22-DWG-09-007-003", "B", "E21", "25007-0021", "N11", "17-Mar-2026", "3-To be revised", 1,
     "OBS-04 MAJOR: based on non-conforming Piping Layout Rev A"),

    # --- Item 28: Cable Tray Layout ---
    (28, "Cable Tray Layout", "P22-DWG-09-007-004", "A", "E11", "25007-0011", "N4", "05-Feb-2026", "3-To be revised", 1,
     "Routing concerns, sizing, duplicate TAG FIT-09-001"),

    # --- Item 29: DS PLC & HMI (single cycle) ---
    (29, "DS PLC & HMI", "P22-ET-09-008-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "2-AN", 1,
     "Minor notes"),

    # --- Item 30: Control Architecture ---
    (30, "Control Architecture", "P22-CD-09-004-001", "A", "E4", "25007-0004", "N2", "26-Jan-2026", "2-AN", 1,
     "Modbus TCP pending, VFD fieldbus pending"),
    (30, "Control Architecture", "P22-CD-09-004-001", "B", "E11", "25007-0011", "N4", "05-Feb-2026", "2-AN", 2,
     "PLC 60Hz issue. A/C thermal pending"),
    (30, "Control Architecture", "P22-CD-09-004-001", "C", "E18", "25007-0018", "N10", "12-Mar-2026", "2-AN", 3,
     "UPS 8h not confirmed. TAG inconsistencies"),
    (30, "Control Architecture", "P22-CD-09-004-001", "D", "E26", "25007-0026", "N14", "15-Apr-2026", "1-Approved", 4,
     "UPS 8h verified (40Ah/4.35A=9.2h). All obs closed"),

    # --- Item 31: IO List ---
    (31, "IO List", "P22-LI-09-008-001", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "3-To be revised", 1,
     "Missing items, TAG inconsistencies"),
    (31, "IO List", "P22-LI-09-008-001", "B", "E18", "25007-0018", "N10", "12-Mar-2026", "2-AN", 2,
     "Motor temp TAGs, conductivity scaling, Modbus corrections"),
    (31, "IO List", "P22-LI-09-008-001", "C", "E28", "25007-0028", "N14", "15-Apr-2026", "2-AN", 3,
     "NOTE-02 MAJOR: analyzer voltage 220VAC vs 24VDC"),

    # --- Item 32: Instrument List ---
    (32, "Instrument List", "P22-LI-09-008-003", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "3-To be revised", 1,
     "Missing items, conductivity ranges wrong"),
    (32, "Instrument List", "P22-LI-09-008-003", "B", "E15", "25007-0015", "N8", "09-Mar-2026", "3-To be revised", 2,
     "CIT power supply, conductivity ranges still wrong"),
    (32, "Instrument List", "P22-LI-09-008-003", "C", "E28", "25007-0028", "N14", "15-Apr-2026", "2-AN", 3,
     "Conductivity CLOSED. NOTE-03/04: vibration range, working medium"),

    # --- Item 33: Valve List ---
    (33, "Valve List", "P22-LI-09-005-002", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "3-To be revised", 1,
     "Duplicate TAGs (VM-09-015, VE-09-008)"),
    (33, "Valve List", "P22-LI-09-005-002", "B", "E13", "25007-0013", "N6", "27-Feb-2026", "4-Rejected", 2,
     "REJECTED: new duplicates, false CCS compliance declaration"),
    (33, "Valve List", "P22-LI-09-005-002", "C", "E19", "25007-0019", "N11", "17-Mar-2026", "3-To be revised", 3,
     "2 new duplicates (VE-09-007, PSV-09-002), area-code errors"),
    (33, "Valve List", "P22-LI-09-005-002", "D", "E27", "25007-0027", "N14", "15-Apr-2026", "2-AN", 4,
     "All duplicates resolved. NOTE-01: PSV removal justification"),

    # --- Item 34: Equipment List ---
    (34, "Equipment List", "P22-LI-09-005-001", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "2-AN", 1,
     "Minor notes"),
    (34, "Equipment List", "P22-LI-09-005-001", "B", "E20", "25007-0020", "N11", "17-Mar-2026", "2-AN", 2,
     "Minor notes"),

    # --- Item 35: Instrument Location Layout ---
    (35, "Instrument Location Layout", "P22-DWG-09-008-001", "B", "E21", "25007-0021", "N11", "17-Mar-2026", "3-To be revised", 1,
     "OBS-03 MAJOR: based on non-conforming Piping Layout Rev A"),

    # --- Item 36: I&C Cable Schedule (single cycle) ---
    (36, "I&C Cable Schedule", "P22-LI-09-008-002", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 37: Chemical Consumption List (single cycle) ---
    (37, "Chemical Consumption List", "P22-LI-09-009-002", "A", "E7", "25007-0007", "N3", "28-Jan-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 38: Line List ---
    (38, "Line List", "P22-LI-09-009-003", "A", "E8", "25007-0008", "N3", "28-Jan-2026", "2-AN", 1,
     "Minor notes"),
    (38, "Line List", "P22-LI-09-009-003", "B", "E23", "25007-0023", "N12", "30-Mar-2026", "2-AN", 2,
     "NOTE-02: SCH80 vs SCH 80S pending IFC"),

    # --- Item 39: Utility Consumption List ---
    (39, "Utility Consumption List", "P22-LI-09-009-001", "A", "E10", "25007-0010", "N4", "05-Feb-2026", "3-To be revised", 1,
     "HP Pump power inconsistency, A/C pending"),
    (39, "Utility Consumption List", "P22-LI-09-009-001", "B", "E13", "25007-0013", "N6", "27-Feb-2026", "2-AN", 2,
     "A/C thermal calc Rev C still pending"),

    # --- Item 40: Piping Layout (single formal cycle) ---
    (40, "Piping Layout", "P22-DWG-09-005-004", "A", "E14", "25007-0014", "N7", "08-Mar-2026", "3-To be revised", 1,
     "CIP/dosing 11,150mm apart vs 3,500mm limit. Rev B preliminary 14-Apr"),

    # --- Item 41: Tie-In Point Layout (single formal cycle) ---
    (41, "Tie-In Point Layout", "P22-DWG-09-005-005", "A", "E14", "25007-0014", "N7", "08-Mar-2026", "3-To be revised", 1,
     "Antiscalant tie-in positions to change. Rev C preliminary 14-Apr"),

    # --- Item 42: DS Conductivity Analyzer ---
    (42, "DS Conductivity Analyzer", "P22-LI-09-008-005", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "2-AN", 1,
     "Toroidal type required for high-conductivity brine services"),
    (42, "DS Conductivity Analyzer", "P22-LI-09-008-005", "B", "E28", "25007-0028", "N14", "15-Apr-2026", "1-Approved", 2,
     "Toroidal confirmed (Rosemount 228). Contacting for permeate"),

    # --- Item 43: DS DP Switch (single cycle) ---
    (43, "DS DP Switch", "P22-LI-09-008-006", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 44: DS Flow Transmitter ---
    (44, "DS Flow Transmitter", "P22-LI-09-008-007", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "2-AN", 1,
     "Fluid medium and power supply notes"),
    (44, "DS Flow Transmitter", "P22-LI-09-008-007", "B", "E29", "25007-0029", "N14", "15-Apr-2026", "1-Approved", 2,
     "Fluid medium corrected. Power supply aligned. All resolved"),

    # --- Item 45: DS Level Switch (single cycle) ---
    (45, "DS Level Switch", "P22-LI-09-008-008", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "2-AN", 1,
     "Minor notes"),

    # --- Item 46: DS Level Transmitter (single cycle) ---
    (46, "DS Level Transmitter", "P22-LI-09-008-009", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "1-Approved", 1,
     "Approved"),

    # --- Item 47: DS pH/ORP Analyzer ---
    (47, "DS pH/ORP Analyzer", "P22-LI-09-008-010", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "1-Approved", 1,
     "Approved"),
    (47, "DS pH/ORP Analyzer", "P22-LI-09-008-010", "B", "E28", "25007-0028", "N14", "15-Apr-2026", "1-Approved", 2,
     "TAG alignment only (ORPIT-09-001A, PHIT-09-006)"),

    # --- Item 48: DS Pressure Gauge ---
    (48, "DS Pressure Gauge", "P22-LI-09-008-011", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "1-Approved", 1,
     "Approved. Wika 233.50 + 990.10 diaphragm seal"),
    (48, "DS Pressure Gauge", "P22-LI-09-008-011", "B", "E27", "25007-0027", "N14", "15-Apr-2026", "1-Approved", 2,
     "Seal changed to Wika 990.31 PP/EPDM for PVC compatibility"),

    # --- Item 49: DS Pressure Transmitter (single cycle) ---
    (49, "DS Pressure Transmitter", "P22-LI-09-008-012", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "2-AN", 1,
     "Minor notes"),

    # --- Item 50: Power Works Drawing ---
    (50, "Power Works Drawing", "P22-DWG-09-007-005", "A", "E15", "25007-0015", "N8", "09-Mar-2026", "3-To be revised", 1,
     "Grounding specs missing, installation standards absent"),
    (50, "Power Works Drawing", "P22-DWG-09-007-005", "B", "E25", "25007-0025", "N13", "06-Apr-2026", "2-AN", 2,
     "TM N8 OBS-01/02 CLOSED. NOTEs: conductor sizing, cable tray"),

    # --- Item 51: DS Temperature Transmitter ---
    (51, "DS Temperature Transmitter", "P22-LI-09-008-013", "A", "E16", "25007-0016", "N8", "09-Mar-2026", "3-To be revised", 1,
     "Header wrong, TAG wrong, accuracy class unspecified"),
    (51, "DS Temperature Transmitter", "P22-LI-09-008-013", "B", "E28", "25007-0028", "N14", "15-Apr-2026", "1-Approved", 2,
     "All TM N8 obs closed. Rosemount 214C+644 confirmed"),

    # --- Item 52: Data Transfer List (Modbus TCP) ---
    (52, "Data Transfer List (Modbus TCP)", "P22-LI-09-008-004", "A", "E18", "25007-0018", "N10", "12-Mar-2026", "2-AN", 1,
     "VE-09-014 duplicate in DI, LS missing from Modbus map"),
    (52, "Data Transfer List (Modbus TCP)", "P22-LI-09-008-004", "B", "E28", "25007-0028", "N14", "15-Apr-2026", "2-AN", 2,
     "TM N10 obs closed. NOTE-05: vibration Modbus scaling"),

    # --- Item 53: GA Antiscalant Dosing Tank (single cycle) ---
    (53, "GA Antiscalant Dosing Tank", "P22-DWG-09-005-015", "A", "E18", "25007-0018", "N10", "12-Mar-2026", "2-AN", 1,
     "Minor notes. Seismic anchor data pending"),

    # --- Item 54: GA Feed Turbocharger ---
    (54, "GA Feed Turbocharger", "P22-DWG-09-005-012", "A", "E18", "25007-0018", "N10", "12-Mar-2026", "3-To be revised", 1,
     "Vibration transducer mounting not shown"),
    (54, "GA Feed Turbocharger", "P22-DWG-09-005-012", "B", "E18", "25007-0018", "N10", "12-Mar-2026", "1-Approved", 2,
     "Vibration mounting resolved"),

    # --- Item 55: GA Interstage Turbocharger ---
    (55, "GA Interstage Turbocharger", "P22-DWG-09-005-013", "A", "E18", "25007-0018", "N10", "12-Mar-2026", "3-To be revised", 1,
     "Vibration transducer mounting not shown"),
    (55, "GA Interstage Turbocharger", "P22-DWG-09-005-013", "B", "E18", "25007-0018", "N10", "12-Mar-2026", "1-Approved", 2,
     "Vibration mounting resolved"),

    # --- Item 56: GA CIP/Flushing Pump (single cycle) ---
    (56, "GA CIP/Flushing Pump", "P22-DWG-09-005-010", "A", "E20", "25007-0020", "N11", "17-Mar-2026", "2-AN", 1,
     "Minor notes"),

    # --- Item 57: GA Antiscalant Dosing Pump (single cycle) ---
    (57, "GA Antiscalant Dosing Pump", "P22-DWG-09-005-011", "A", "E20", "25007-0020", "N11", "17-Mar-2026", "2-AN", 1,
     "Minor notes"),

    # --- Item 58: DS Vibration Transmitter ---
    (58, "DS Vibration Transmitter", "P22-LI-09-008-014", "A", "E22", "25007-0022", "N12", "30-Mar-2026", "3-To be revised", 1,
     "IFM VTV122: HART not documented. Quantity=1 vs 3 TAGs"),
    (58, "DS Vibration Transmitter", "P22-LI-09-008-014", "B", "E28", "25007-0028", "N14", "15-Apr-2026", "1-Approved", 2,
     "Wilcoxon PCH420V-M12, HART 7.0 confirmed, qty=3"),

    # --- Item 67: Control Philosophy ---
    (67, "Control Philosophy", "P22-BT-09-009-001", "A", "E14", "25007-0014", "N7", "08-Mar-2026", "3-To be revised", 1,
     "UPS 30min vs 8h, Pt-100 missing, Modbus TCP absent"),
    (67, "Control Philosophy", "P22-BT-09-009-001", "B", "E33", "25007-0033", "N15", "22-Apr-2026", "3-To be revised", 2,
     "17 notes (NOTE-13 to 29). NOTE-20 CRITICAL: HP Pump permissive TAGs. SEC/guarantee, VE-09-002 algorithm, network redundancy"),

    # --- TM N15 new Rev entries ---
    (16, "A/C Thermal Calculation", "P22-CD-09-005-002", "C", "E31", "25007-0031", "N15", "22-Apr-2026", "2-AN", 3,
     "Closes TM N2 OBS-02. NOTE-02 MAJOR: 0.03 TR deficit, confirm n+1 100% each unit"),
    (27, "Grounding Layout", "P22-DWG-09-007-003", "C", "E31", "25007-0031", "N15", "22-Apr-2026", "2-AN", 3,
     "Aligned to Piping Layout Rev B. TM N11 OBS-03 closed. NOTE-03 MAJOR: schedule PE completeness"),
    (28, "Cable Tray Layout", "P22-DWG-09-007-004", "B", "E32", "25007-0032", "N15", "22-Apr-2026", "3-To be revised", 2,
     "5 new OBS MAJOR + TM N4 OBS-05/06/07 open 78 days. Rev C required"),
    (35, "Instrument Location Layout", "P22-DWG-09-008-001", "C", "E32", "25007-0032", "N15", "22-Apr-2026", "2-AN", 3,
     "Aligned to Piping Layout Rev B. Closes TM N3 OBS-01/02/03 and TM N11 OBS-04"),
    (40, "Piping Layout", "P22-DWG-09-005-004", "B", "E32", "25007-0032", "N15", "22-Apr-2026", "2-AN", 2,
     "3500mm WITHDRAWN by ADASA. NOTE-06/07/08/09 for Rev 0"),
    (45, "DS Level Switch", "P22-LI-09-008-008", "B", "E30", "25007-0030", "N15", "22-Apr-2026", "1-Approved", 2,
     "IFM KQ6005 approved. NOTE-01 MINOR: interface label"),

    # --- Item 81: LCP Datasheet (first cycle) ---
    (81, "Datasheet LCP", "P22-ET-09-007-005", "A", "E31", "25007-0031", "N15", "22-Apr-2026", "3-To be revised", 1,
     "First revision. OBS-01/02/03 MAJOR: I/O config, IP rating, power load inconsistency"),

    # --- Item 82: Equipment Layout ---
    (82, "Equipment Layout", "P22-DWG-09-005-003", "A", "E5", "25007-0005", "N2", "26-Jan-2026", "3-To be revised", 1,
     "First formal review. Dimensions and equipment arrangement concerns"),
    (82, "Equipment Layout", "P22-DWG-09-005-003", "B", "E32", "25007-0032", "N15", "22-Apr-2026", "2-AN", 2,
     "Closes TM N5 OBS-03/04/05. NOTE-04 MAJOR: Operating Weight table for Rev 0"),

    # --- Item 83: GA SWRO System Skid ---
    (83, "GA of SWRO System Skid", "P22-DWG-09-005-008", "A", "E33", "25007-0033", "N15", "22-Apr-2026", "2-AN", 1,
     "First revision. NOTE-11/12 MAJOR: equipment/valve schedule and material schedule missing"),
]


# ============================================================
# OPEN OBSERVATIONS (for Summary sheet)
# ============================================================
OPEN_OBSERVATIONS = [
    ("TM N15 NOTE-20 CRITICAL", "Control Philosophy Rev B", "HP Pump permissive contains erroneous TAGs (VE-09-007 duplicated, VE-09-014 antiscalant)", "22-Apr-2026", "Rev C required"),
    ("TM N15 OBS-01", "LCP Datasheet Rev A", "I/O module config and motor RTD channels (8 Pt-100) not declared", "22-Apr-2026", "Rev B required"),
    ("TM N15 OBS-02", "LCP Datasheet Rev A", "Panel IP rating and ambient class not declared (IP54 expected)", "22-Apr-2026", "Rev B required"),
    ("TM N15 OBS-04/08", "Cable Tray Layout Rev B", "5 MAJOR routing/support/anchoring findings", "22-Apr-2026", "Rev C required"),
    ("TM N15 NOTE-13", "Control Philosophy Rev B", "SEC formula/guarantee alignment (4.8/5.0 vs Offer 4.71 kWh/m3)", "22-Apr-2026", "Rev C required"),
    ("TM N15 NOTE-22", "Control Philosophy Rev B", "Salt Rejection formula uses Stage 2 reject instead of feed conductivity", "22-Apr-2026", "Rev C required"),
    ("TM N15 NOTE-25", "Control Philosophy Rev B", "SEC monitoring on RO PLC panel meter, not MCC main breaker", "22-Apr-2026", "Rev C required"),
    ("TM N15 NOTE-26", "Control Philosophy Rev B", "Network lacks redundancy; PLX32 single point of failure", "22-Apr-2026", "Rev C required"),
    ("TM N15 NOTE-27", "Control Philosophy Rev B", "Three ET requirements unmet (manual mode, VFD ramp, rupture interlock)", "22-Apr-2026", "Rev C required"),
    ("TM N4 OBS-05/06/07", "Cable Tray Layout", "FIT/VT/TE locations missing", "05-Feb-2026", "78 days outstanding \u2014 itemize on Rev C comment sheet"),
    ("TM N10 OBS-05", "GA Antiscalant Dosing Tank", "Seismic anchor data (NCh 2369)", "12-Mar-2026", "GA Rev B pending"),
    ("TM N10 NOTE-05", "HMI Screenshots", "P22-BREAD-09-008-001 not submitted", "05-Feb-2026", "79 days outstanding"),
]

WITHDRAWN_BY_ADASA = [
    ("TM N5 OBS-01 / TM N7 OBS-01", "Equipment/Piping Layout", "3,500 mm CIP/dosing footprint constraint", "22-Apr-2026", "WITHDRAWN by ADASA \u2014 superseded by P22-DWG-06-006-101"),
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================
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


def apply_row_style(ws, row_idx, num_cols, verdict, status, font=FONT_NORMAL):
    """Apply verdict colors and status bold to a row."""
    fill = get_verdict_fill(verdict)
    is_bold = status in ("NOT DELIVERED", "PARTIAL")
    row_font = FONT_BOLD if is_bold else font
    for col_idx in range(1, num_cols + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.font = row_font
        cell.border = THIN_BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        if col_idx in (1, 4, 5, 6, 10) and num_cols == 11:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in (1, 4, 5, 6):
            cell.alignment = Alignment(horizontal="center", vertical="center")
        if fill and col_idx <= (num_cols - 1):
            cell.fill = fill


# ============================================================
# SHEET 1: MASTER REGISTER
# ============================================================
# ============================================================
# SECTIONS — reorder Master Register by ETE chapter/phase
# ============================================================
# Section 1: ENGINEERING — ET Chapter 7 (90 days from NTP) + ET Chapter 5 technical
# Section 2: HANDOVER    — ET Chapter 7 (1 month before end of contract)
# Section 3: FABRICATION & FAT — ET Chapter 8 (out of engineering scope)
# Section 4: COMMISSIONING     — ET Chapter 9 (out of engineering scope)
SECTIONS = [
    ("1. ENGINEERING — ET Chapter 7 (90 days from NTP) + ET Chapter 5",
     [i for i in list(range(1, 76)) + [81, 82, 83] if i not in (60, 61, 69, 74)]),
    ("2. HANDOVER — ET Chapter 7 (1 month before end of contract)",
     [76, 77, 78, 79, 80]),
    ("3. FABRICATION & FAT — ET Chapter 8 (out of engineering scope)",
     [84, 85, 86]),
    ("4. COMMISSIONING — ET Chapter 9 (out of engineering scope)",
     [87, 88, 89]),
]


def generar_master_register(wb):
    ws = wb.active
    ws.title = "Master Register"

    col_widths = [4, 38, 26, 5, 8, 5, 18, 18, 52, 38]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    for col, header in enumerate(HEADERS, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = THIN_BORDER

    ws.freeze_panes = "A2"

    # Index DATA_MASTER by item #
    by_id = {r[0]: r for r in DATA_MASTER}

    row_idx = 2
    for section_title, item_ids in SECTIONS:
        # Section header row: merged across all columns, styled
        ws.merge_cells(start_row=row_idx, start_column=1,
                       end_row=row_idx, end_column=len(HEADERS))
        hdr_cell = ws.cell(row=row_idx, column=1, value=section_title)
        hdr_cell.font = FONT_SECTION
        hdr_cell.fill = FILL_SECTION
        hdr_cell.alignment = Alignment(horizontal="left", vertical="center")
        hdr_cell.border = THIN_BORDER
        # Apply border to all merged cells
        for c in range(1, len(HEADERS) + 1):
            ws.cell(row=row_idx, column=c).border = THIN_BORDER
        ws.row_dimensions[row_idx].height = 22
        row_idx += 1

        # Data rows for this section
        for item_id in item_ids:
            if item_id not in by_id:
                continue
            row_data = by_id[item_id]
            for col_idx, value in enumerate(row_data, 1):
                cell = ws.cell(row=row_idx, column=col_idx, value=value)
                cell.font = FONT_NORMAL
                cell.border = THIN_BORDER
                cell.alignment = Alignment(vertical="center", wrap_text=True)
                if col_idx in (1, 4, 5, 6):
                    cell.alignment = Alignment(horizontal="center", vertical="center")

            verdict = str(row_data[6])
            fill = get_verdict_fill(verdict)
            if fill:
                for col_idx in range(1, 10):
                    ws.cell(row=row_idx, column=col_idx).fill = fill

            status_val = str(row_data[7])
            if status_val in ("NOT DELIVERED", "PARTIAL"):
                for col_idx in range(1, len(HEADERS) + 1):
                    ws.cell(row=row_idx, column=col_idx).font = FONT_BOLD

            deadline_val = str(row_data[9])
            deadline_cell = ws.cell(row=row_idx, column=10)
            deadline_cell.alignment = Alignment(vertical="center", wrap_text=True)
            if "1 month before end of contract" in deadline_val:
                deadline_cell.fill = FILL_DEADLINE_END
                deadline_cell.font = FONT_BOLD
            elif "NOT DELIVERED" in status_val or status_val == "PARTIAL":
                deadline_cell.fill = FILL_DEADLINE_NTP_LATE

            row_idx += 1

    # Filter covers data rows (including section headers — Excel handles gracefully)
    ws.auto_filter.ref = f"A1:J{row_idx - 1}"

    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0


# ============================================================
# SHEET 2: REVISION HISTORY
# ============================================================
def generar_revision_history(wb):
    ws = wb.create_sheet("Revision History")

    col_widths = [4, 32, 24, 5, 8, 14, 5, 14, 18, 6, 52]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    for col, header in enumerate(HISTORY_HEADERS, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = THIN_BORDER

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:K{len(REVISION_HISTORY) + 1}"

    prev_item = None
    for row_idx, row_data in enumerate(REVISION_HISTORY, 2):
        item_num = row_data[0]

        # Separator between different documents
        if prev_item is not None and item_num != prev_item:
            pass  # openpyxl handles row gaps via cell formatting

        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = FONT_NORMAL
            cell.border = THIN_BORDER
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if col_idx in (1, 4, 5, 7, 10):
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # Color by verdict (column 9)
        verdict = str(row_data[8])
        fill = get_verdict_fill(verdict)
        if fill:
            for col_idx in range(1, 12):
                ws.cell(row=row_idx, column=col_idx).fill = fill

        prev_item = item_num

    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0


# ============================================================
# SHEET 3: SUMMARY
# ============================================================
def generar_summary(wb):
    ws = wb.create_sheet("Summary")
    ws.column_dimensions["A"].width = 38
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 14
    ws.column_dimensions["D"].width = 50

    row = 1
    ws.cell(row=row, column=1, value="MASTER DELIVERABLE REGISTER \u2014 SUMMARY").font = FONT_TITLE
    row += 2

    # --- Project Metrics ---
    ws.cell(row=row, column=1, value="PROJECT METRICS").font = FONT_SECTION
    row += 1

    total = len(DATA_MASTER)
    delivered = sum(1 for r in DATA_MASTER if r[7] == "Delivered")
    deficient = sum(1 for r in DATA_MASTER if r[7] == "Delivered (deficient)")
    partial = sum(1 for r in DATA_MASTER if r[7] == "PARTIAL")
    not_delivered = sum(1 for r in DATA_MASTER if r[7] == "NOT DELIVERED")

    metrics = [
        ("Total Items", total),
        ("Delivered", delivered),
        ("Delivered (deficient)", deficient),
        ("Partial", partial),
        ("Not Delivered", not_delivered),
        ("Transmittals Issued", "15 (N1 through N15)"),
        ("Deliveries Received", "33 (E1 through E33)"),
        ("First Delivery Date", "10-Dec-2025 (E1)"),
        ("Latest Delivery Date", "22-Apr-2026 (E33)"),
        ("Status Date", "23-Apr-2026"),
    ]
    for label, value in metrics:
        c1 = ws.cell(row=row, column=1, value=label)
        c1.font = FONT_BOLD
        c1.border = THIN_BORDER
        c2 = ws.cell(row=row, column=2, value=value)
        c2.font = FONT_NORMAL
        c2.border = THIN_BORDER
        c2.alignment = Alignment(horizontal="center")
        row += 1

    row += 2

    # --- Items by Section (ETE Chapter) ---
    ws.cell(row=row, column=1, value="ITEMS BY SECTION (ETE Chapter)").font = FONT_SECTION
    row += 1

    by_id = {r[0]: r for r in DATA_MASTER}
    for hdr, col_idx in [("Section", 1), ("Total", 2), ("Delivered", 3), ("Progress", 4)]:
        c = ws.cell(row=row, column=col_idx, value=hdr)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.border = THIN_BORDER
        c.alignment = Alignment(horizontal="center")
    row += 1

    for section_title, item_ids in SECTIONS:
        items = [by_id[i] for i in item_ids if i in by_id]
        total_section = len(items)
        delivered_section = sum(1 for r in items if r[7] in ("Delivered", "Covered"))
        pct = f"{delivered_section / total_section * 100:.0f}%" if total_section > 0 else "0%"

        c1 = ws.cell(row=row, column=1, value=section_title)
        c1.font = FONT_BOLD
        c1.border = THIN_BORDER
        c1.alignment = Alignment(vertical="center", wrap_text=True)
        c2 = ws.cell(row=row, column=2, value=total_section)
        c2.font = FONT_NORMAL
        c2.border = THIN_BORDER
        c2.alignment = Alignment(horizontal="center")
        c3 = ws.cell(row=row, column=3, value=delivered_section)
        c3.font = FONT_NORMAL
        c3.border = THIN_BORDER
        c3.alignment = Alignment(horizontal="center")
        c4 = ws.cell(row=row, column=4, value=pct)
        c4.font = FONT_BOLD
        c4.border = THIN_BORDER
        c4.alignment = Alignment(horizontal="center")
        row += 1

    row += 2

    # --- Verdict Distribution (delivered items only) ---
    ws.cell(row=row, column=1, value="VERDICT DISTRIBUTION (Delivered Items)").font = FONT_SECTION
    row += 1

    # Count current verdicts for delivered items
    verdict_counts = {}
    for r in DATA_MASTER:
        if r[7] == "Delivered":
            v = r[6]
            verdict_counts[v] = verdict_counts.get(v, 0) + 1

    verdict_order = ["1-Approved", "2-AN", "3-To be revised", "4-Rejected"]
    verdict_fills = [FILL_GREEN, FILL_YELLOW, FILL_ORANGE, FILL_RED]

    for hdr, col_idx in [("Verdict", 1), ("Count", 2), ("%", 3)]:
        c = ws.cell(row=row, column=col_idx, value=hdr)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.border = THIN_BORDER
        c.alignment = Alignment(horizontal="center")
    row += 1

    for v, fill in zip(verdict_order, verdict_fills):
        count = verdict_counts.get(v, 0)
        pct = f"{count / delivered * 100:.0f}%" if delivered > 0 else "0%"
        c1 = ws.cell(row=row, column=1, value=v)
        c1.font = FONT_BOLD
        c1.fill = fill
        c1.border = THIN_BORDER
        c2 = ws.cell(row=row, column=2, value=count)
        c2.font = FONT_NORMAL
        c2.fill = fill
        c2.border = THIN_BORDER
        c2.alignment = Alignment(horizontal="center")
        c3 = ws.cell(row=row, column=3, value=pct)
        c3.font = FONT_NORMAL
        c3.fill = fill
        c3.border = THIN_BORDER
        c3.alignment = Alignment(horizontal="center")
        row += 1

    row += 2

    # --- Review Cycles Distribution ---
    ws.cell(row=row, column=1, value="REVIEW CYCLES DISTRIBUTION").font = FONT_SECTION
    row += 1

    # Count max cycle per item from revision history
    item_max_cycle = {}
    for r in REVISION_HISTORY:
        item_num = r[0]
        cycle = r[9]
        if item_num not in item_max_cycle or cycle > item_max_cycle[item_num]:
            item_max_cycle[item_num] = cycle

    cycle_counts = {}
    for item, max_c in item_max_cycle.items():
        cycle_counts[max_c] = cycle_counts.get(max_c, 0) + 1

    for hdr, col_idx in [("Review Cycles", 1), ("Documents", 2), ("Examples", 4)]:
        c = ws.cell(row=row, column=col_idx, value=hdr)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.border = THIN_BORDER
        c.alignment = Alignment(horizontal="center")
    ws.merge_cells(start_row=row, start_column=4, end_row=row, end_column=4)
    row += 1

    cycle_examples = {
        1: "Piping Spec, SLD, Load List, DS DP Switch, DS Level Transmitter",
        2: "P&ID (3 revs), Process Calc, DS UHPRO, DS CIP Pump, DS Vibration",
        3: "DS HP Pump, IO List, Instrument List, DS Feed Turbocharger",
        4: "Valve List (A\u2192D), Control Architecture (A\u2192D)",
    }

    for cycles in sorted(cycle_counts.keys()):
        c1 = ws.cell(row=row, column=1, value=f"{cycles} cycle{'s' if cycles > 1 else ''}")
        c1.font = FONT_BOLD
        c1.border = THIN_BORDER
        c2 = ws.cell(row=row, column=2, value=cycle_counts[cycles])
        c2.font = FONT_NORMAL
        c2.border = THIN_BORDER
        c2.alignment = Alignment(horizontal="center")
        c4 = ws.cell(row=row, column=4, value=cycle_examples.get(cycles, ""))
        c4.font = FONT_NORMAL
        c4.border = THIN_BORDER
        row += 1

    row += 2

    # --- Open Observations ---
    ws.cell(row=row, column=1, value="OPEN OBSERVATIONS").font = FONT_SECTION
    row += 1

    obs_headers = ["Observation", "Document", "Description", "Since"]
    for col_idx, hdr in enumerate(obs_headers, 1):
        c = ws.cell(row=row, column=col_idx, value=hdr)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.border = THIN_BORDER
        c.alignment = Alignment(horizontal="center")
    row += 1

    for obs in OPEN_OBSERVATIONS:
        for col_idx, val in enumerate(obs[:4], 1):
            c = ws.cell(row=row, column=col_idx, value=val)
            c.font = FONT_NORMAL
            c.border = THIN_BORDER
            c.fill = FILL_ORANGE
        row += 1

    row += 2

    # --- TM N14 Closures ---
    ws.cell(row=row, column=1, value="OBSERVATIONS CLOSED IN TM N15 (6 + 2 withdrawn + 2 incorporated)").font = FONT_SECTION
    row += 1

    closures = [
        "TM N2 OBS-02 (180+ days): A/C Thermal Calc Rev C consolidates all container loads \u2014 resolved",
        "TM N3 OBS-01/02/03: Instrument Location Layout Rev C aligned \u2014 resolved",
        "TM N5 OBS-03/04/05: Equipment Layout Rev B (doors, emergency exit, lateral sliding) \u2014 resolved",
        "TM N11 OBS-03: Grounding Layout Rev C aligned to Piping Layout Rev B \u2014 resolved",
        "TM N11 OBS-04: Instrument Location Layout Rev C aligned \u2014 resolved",
        "TM N13 NOTE-02: Cable Tray Layout drawings delivered as Rev B (pending Rev C \u2014 see item 28)",
        "WITHDRAWN TM N5 OBS-01: 3,500 mm footprint constraint \u2014 superseded by P22-DWG-06-006-101",
        "WITHDRAWN TM N7 OBS-01: 3,500 mm footprint constraint (restated) \u2014 superseded by P22-DWG-06-006-101",
        "INCORPORATED TM N7 OBS-03: Equipment access door + lateral sliding (Piping Layout NOTE-06 for Rev 0)",
        "INCORPORATED TM N7 OBS-04: Cabinet integration (Piping Layout NOTE-07 for Rev 0)",
    ]
    for closure in closures:
        c = ws.cell(row=row, column=1, value=closure)
        c.font = FONT_NORMAL
        c.fill = FILL_GREEN
        c.border = THIN_BORDER
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
        row += 1


# ============================================================
# SHEET 4: LEGEND
# ============================================================
def generar_legend(wb):
    ws = wb.create_sheet("Legend")
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 80

    legend_title   = Font(name="Arial", size=12, bold=True)
    legend_section = Font(name="Arial", size=10, bold=True)

    row = 1
    ws.cell(row=row, column=1, value="DOCUMENT STATUS REGISTER \u2014 LEGEND").font = legend_title
    row += 2

    # --- References ---
    ws.cell(row=row, column=1, value="REFERENCES").font = legend_section
    row += 1
    refs = [
        ("ET",            "Especificacion Tecnica P22-ET-09-000-001-0 (Technical Specification)"),
        ("ET Sec 5",      "Section 5 of the ET: technical requirements per equipment/system (MCC, Modbus, etc.)"),
        ("ET Sec 7",      "Section 7 of the ET: contractual engineering deliverables (pp. 27-30)"),
        ("ET Sec 7, p.XX","Reference to page XX within Section 7 of the ET (pp. 27-30)"),
        ("ET Sec 8",      "Section 8 of the ET: inspections during fabrication + FAT (pp. 30-33) — out of engineering scope"),
        ("ET Sec 9",      "Section 9 of the ET: commissioning and training (pp. 33-34) — out of engineering scope"),
        ("ET 5.X",        "Reference to specific technical requirement section within the ET"),
        ("TM NX",         "ADASA Transmittal number X (N1 through N15)"),
        ("EX",            "BW Water delivery number X (E1 through E33, 33 deliveries as of 22-Apr-2026)"),
        ("25007-XXXX",    "BW Water submittal form number (25007-0001 through 25007-0033)"),
        ("BAE Cl. XX",    "Bases Administrativas Especiales, clause XX"),
        ("NTP",           "Notice to Proceed (Notificacion de Adjudicacion)"),
    ]
    for term, desc in refs:
        ws.cell(row=row, column=1, value=term).font = FONT_BOLD
        ws.cell(row=row, column=2, value=desc).font = FONT_NORMAL
        row += 1

    row += 1

    # --- Verdicts ---
    ws.cell(row=row, column=1, value="REVIEW VERDICTS").font = legend_section
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
        c1 = ws.cell(row=row, column=1, value=verdict)
        c1.font = FONT_BOLD
        c1.fill = fill
        c2 = ws.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        row += 1

    row += 1

    # --- Deadlines ---
    ws.cell(row=row, column=1, value="CONTRACTUAL DEADLINES").font = legend_section
    row += 1
    deadlines = [
        ("Item #59 (Schedule)",  "Maximum 15 days from NTP (ET Section 7, p.27)"),
        ("Items #1-58",          "Maximum 90 days from NTP (ET Section 7, pp. 27-29)"),
        ("Items #76-80",         "1 month before end of contract (ET Section 7, pp. 29-30) \u2014 Prerequisite for equipment release to site"),
        ("PIE Detallado (#73)",  "90 days from NTP \u2014 Written approval required before manufacturing start (ET Sec.7 p.29)"),
    ]
    for term, desc in deadlines:
        c1 = ws.cell(row=row, column=1, value=term)
        c1.font = FONT_BOLD
        c2 = ws.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        if "76-80" in term:
            c1.fill = FILL_DEADLINE_END
            c2.fill = FILL_DEADLINE_END
        row += 1

    row += 1

    # --- Status values ---
    ws.cell(row=row, column=1, value="STATUS VALUES").font = legend_section
    row += 1
    statuses_legend = [
        ("Delivered",           "Document received from BW Water and reviewed by ADASA"),
        ("Delivered (deficient)","Document received but substantially incomplete"),
        ("PARTIAL",             "Requirement partially covered; key elements still missing"),
        ("Covered",             "Requirement covered by individually tracked items (see Action Required for cross-reference)"),
        ("NOT DELIVERED",       "Document not submitted as of 23-Apr-2026"),
    ]
    for term, desc in statuses_legend:
        ws.cell(row=row, column=1, value=term).font = FONT_BOLD
        ws.cell(row=row, column=2, value=desc).font = FONT_NORMAL
        row += 1

    row += 2
    ws.cell(row=row, column=1, value="DELIVERABLES CONSOLIDATED / ADASA-CONTROLLED").font = legend_section
    row += 1
    consolidated = [
        ("ETE Seccion 7 p.27 'Layouts'", "Covered by items #40 (Piping Layout), #41 (Tie-In), #82 (Equipment Layout). Former bucket item #60 removed."),
        ("ETE Seccion 7 p.28 'Planos de arreglo'", "Covered by items #40 + #82 (plan + elevation views). Former bucket item #61 removed."),
        ("ETE Seccion 5.4 MCC Datasheet", "Covered by item #81 LCP Datasheet Rev A (combined panel per ETE Seccion 5.4). Former item #74 removed."),
        ("ETE Seccion 7 p.28 'Listado de entregables'", "Controlled by ADASA via this Master Register (P22-IT-06-000-002). Former item #69 removed \u2014 not required from BW Water."),
    ]
    for term, desc in consolidated:
        c1 = ws.cell(row=row, column=1, value=term)
        c1.font = FONT_BOLD
        c2 = ws.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        row += 1

    row += 2
    ws.cell(row=row, column=1, value="MASTER REGISTER SECTIONS").font = legend_section
    row += 1
    sections_desc = [
        ("1. ENGINEERING",        "ET Chapter 7 (90 days from NTP) + ET Chapter 5 technical items (MCC, Modbus). Core engineering scope prior to IFC."),
        ("2. HANDOVER",           "ET Chapter 7 (1 month before end of contract). Manuals, software/licenses, preservation \u2014 prerequisite for equipment release to site."),
        ("3. FABRICATION & FAT",  "ET Chapter 8 (pp. 30-33). NDE plan, FAT procedure, PMI report. Out of engineering scope \u2014 listed for contractual traceability."),
        ("4. COMMISSIONING",      "ET Chapter 9 (pp. 33-34). Commissioning reports, training materials. Out of engineering scope \u2014 listed for contractual traceability."),
    ]
    for term, desc in sections_desc:
        c1 = ws.cell(row=row, column=1, value=term)
        c1.font = FONT_BOLD
        c1.fill = FILL_SECTION
        c2 = ws.cell(row=row, column=2, value=desc)
        c2.font = FONT_NORMAL
        row += 1

    row += 2
    ws.cell(row=row, column=1, value="Document:").font = FONT_BOLD
    ws.cell(row=row, column=2,
            value="P22-IT-06-000-002-0 | Date: 23-Apr-2026 | Prepared by: Luis Rivera | Updated: TM N15 (E33) + ET cross-check + section grouping + consolidation \u2014 23-Apr-2026").font = FONT_NORMAL


# ============================================================
# MAIN
# ============================================================
def generar_excel():
    wb = Workbook()
    generar_master_register(wb)
    generar_revision_history(wb)
    generar_summary(wb)
    generar_legend(wb)
    wb.save(OUTPUT)

    # Statistics
    delivered = sum(1 for r in DATA_MASTER if r[7] == "Delivered")
    not_del = sum(1 for r in DATA_MASTER if r[7] in ("NOT DELIVERED", "PARTIAL", "Delivered (deficient)"))
    items_in_history = len(set(r[0] for r in REVISION_HISTORY))

    print(f"Excel generado: {OUTPUT}")
    print(f"  Hoja 1 - Master Register: {len(DATA_MASTER)} items ({delivered} delivered, {not_del} pending)")
    print(f"  Hoja 2 - Revision History: {len(REVISION_HISTORY)} entries ({items_in_history} documents tracked)")
    print(f"  Hoja 3 - Summary: metricas calculadas")
    print(f"  Hoja 4 - Legend: actualizada TM N15 / E33 / 23-Apr-2026")


if __name__ == "__main__":
    generar_excel()
