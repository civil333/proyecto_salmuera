#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Deliverable Register v4 — P22-IT-06-000-002-0
Genera Excel con 4 hojas:
  1. Master Register  — items con estado actual TM N20 + gaps ET (10-Jun-2026)
  2. Revision History — historial completo de cada documento a traves de TM N1-N20
  3. Summary          — metricas del proyecto calculadas dinamicamente
  4. Legend           — referencias actualizadas

Cambios vs v3:
  BLOQUE A — TM N16 (24-Apr-2026, E34, submittal 25007-0034):
    - 1 item nuevo (90 Civil and Loading Drawing Rev A, 2-AN)
    - Actualizada nota cruzada en item 82 (Equipment Layout) referenciando entrega de Civil & Loading
  BLOQUE B — TM N17 (05-May-2026, E35-E37, submittals 25007-0035/36/37):
    - 6 items actualizados con nuevas revisiones:
        27 Grounding Layout: Rev C -> Rev D (TM N17, 2-AN)
        31 IO List: Rev C -> Rev 0 IFC (TM N17, 2-AN)
        32 Instrument List: Rev C -> Rev D (TM N17, 2-AN)
        49 DS Pressure Transmitter: Rev A -> Rev B (TM N17, 2-AN)
        50 Power Works Drawing: Rev B -> Rev 0 IFC (TM N17, 2-AN)
        52 Data Transfer List (Modbus): Rev B -> Rev 0 IFC (TM N17, 2-AN)
    - 3 items nuevos:
        91 Project Quality Plan Rev A (3-To be revised, OBS-01/02 CRITICAL)
        92 Inspection and Test Plan Offsite Rev A (2-AN)
        93 Alarm and Interlock List Rev A (3-To be revised, OBS-01 CRITICAL unit error mS/cm vs uS/cm)
  BLOQUE C — Refresh inventario open observations al corte 05-May-2026 (Section 3 TM N17, 11 obs abiertas).
  BLOQUE E — TM N18 (18-May-2026, E38-E41, submittals 25007-0038/39/40/41):
    - Re-escopeado +P&ID Rev D (E41); RE-DISPOSICIONADO con criterio ejecutivo
      Code 1/2 (CLAUDE.md secciones 6.2/6.3 v6.11): 4 Code 1 + 1 Code 3.
        2  P&ID: Rev C -> Rev D (TM N18, 1-Approved; cierra TM N13 NOTE-01)
        16 A/C Thermal Calc: Rev C re-dispuesto (TM N18, 1-Approved; cierra TM N15 NOTE-02)
        33 Valve List: Rev D re-emitido c/ CCS (TM N18, 1-Approved)
        38 Line List: Rev B -> Rev C (TM N18, 1-Approved; cierra TM N12 NOTE-01/02)
        67 Control Philosophy: Rev B -> Rev C (TM N18, 3-To be revised; Rev D
           requerida; OBS-01 CRITICAL repite TM N15 NOTE-20)
    - Entregables Seccion 3 (docs Code 1): PSV-09-002, CIT-09-004, dual-value
      CIP Tank, AC margen efectivo, TM N16 NOTE-01. Correo notificacion ENVIADO
      18-May-2026.
  BLOQUE D — Cross-check ET (07-May-2026 / late session):
    - 4 items nuevos por gaps verificados en P22-ET-09-000-001-0:
        94 Mandatory Spare Parts Package (ET Sec.6 p.27 lineas 1462-1496) — parte del precio base
        95 Optional 2-Year Spare Parts List (ET Sec.6 p.27 lineas 1497-1501) — listado en propuesta tecnica
        96 Performance Tests Report (ET Sec.10.2 lineas 1941+) — mandatorio para Recepcion Provisional
        97 Acta de Recepcion Provisional (ET Sec.10) — milestone final del contrato
    - Nueva Section 5 'RECEPCION PROVISIONAL' (ET Chapter 10) con items 96-97
    - Refuerzos Hold Point textuales en items 73 (PIE Detallado) y 80 (Preservation/Packaging)
    - Item 75 reformulado: 'Modbus TCP Memory Map' -> 'Modbus TCP Communication System & Memory Map' con referencia exacta a ET Sec.5.4 linea 1075-1077
  BLOQUE F — TM N19 (25-May-2026, E42-E45, submittals 25007-0042/43/44/45, 13 docs):
    - Tally 3 Code 1 + 5 Code 2 + 5 Code 3. NT-001 emitida en paralelo (cross-ref Secciones 2.10/2.12/2.13).
    - Actualizados: 21 Electrical Load List Rev B (1), 26 Power Cable Schedule Rev B (2-AN),
      23 DS Power & Control Cable Rev B (1), 20 Single Line Diagram Rev B (2-AN),
      27 Grounding Layout Rev E (3-TBR, Rev F 14 dias), 28 Cable Tray Layout Rev C (1 — cierra
      herencia mas larga del proyecto: TM N4 OBS-06/07 110d + TM N15 OBS-04..08),
      50 Power Works Rev C (2-AN), 31 IO List Rev 1 IFC (2-AN condicional a Control Philosophy Rev D),
      91 PQP Rev B (2-AN — cierra 2 CRITICAL TM N17, prerequisito hito pago 40% BAE Cl.31),
      92 ITP Offsite Rev B (3-TBR — silencio ASME X, cross-ref NT-001 6.A/6.C),
      36 I&C Cable Schedule Rev 0 (3-TBR), 9 RO Cartridge Filter Rev D (3-TBR, H->V + Sysflo pre-NT-001),
      10 CIP Cartridge Filter Rev C (3-TBR).
  BLOQUE G — TM N20 (10-Jun-2026, E46 28-May 7 docs + E47 09-Jun 13 docs, submittals 25007-0046/47, 20 docs):
    - Tally 8 Code 1 + 7 Code 2 + 5 Code 3. Drivers: PLC-LCP Outline enclosure contradiction (gate
      fabricacion panel), Control Philosophy Rev D 4o ciclo (ventana 14d TM N19 vencida 08-Jun ->
      reversion I/O List a Code 3), NDE Plan silencio alcance vessels.
    - Actualizados: 32 Instrument List Rev E (1), 52 Data Transfer List Rev 1 (2-AN), 49 DS Pressure
      Transmitter Rev C (1), 93 Alarm & Interlock Rev B (3-TBR), 81 LCP Datasheet Rev B (2-AN),
      21/26/23/20/50 paquete electrico IFC Rev 0 (todos 1-Approved), 31 IO List Rev 2 (3-TBR reversion),
      36 I&C Cable Schedule Rev 1 (3-TBR), 59 Project Schedule Rev A (2-AN, baseline recovery adoptada
      con reservas carta 09-Jun), 84 NDE Plan Rev A entregado (3-TBR).
    - 6 items nuevos: 98 PLC-LCP Outline Panel Drawing Rev A (3-TBR), 99 PLC/LCP Schematic Rev A (2-AN),
      100 Organization Chart Rev A (1), 101 PMI Procedure Rev A (2-AN), 102 Welding Procedure Rev A (2-AN),
      103 Visual Procedure Rev A (2-AN).

Generado: 10-Jun-2026 (corte TM N20 — E47 09-Jun-2026)
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
# MASTER REGISTER DATA (99 items — incluye TM N19 + N20)
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
         "P22-DWG-09-009-002", "D", "E41", "N18", "1-Approved", "Delivered",
         "Rev D approved (TM N18, 18-May-2026). Drawing accepted as-is \u2014 no further P&ID revision required. TM N13 NOTE-01 CLOSED: CIP Tank TK-09-001 6.81/6.1 m\u00b3 resolved as total geometric 6.8 m\u00b3 vs effective usable 6.1 m\u00b3 (both annotated; Antiscalant Tank 0.34/0.27 m\u00b3). BW Water-initiated CIT-09-004 tapping change (orifice + needle valve) tracked to Section 3 as Instrument List Rev D + Line List Rev C deliverables + loop-response note. Dual-value convention vs CIP Tank datasheet/Equipment List tracked for IFC Rev 0.",
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

    # UPDATED TM N19: Rev C->D, E13->E45, N6->N19, 2-AN->3-TBR (H->V + Sysflo pre-NT-001)
    (9,  "DS RO Cartridge Filter",
         "P22-ET-09-009-005", "D", "E45", "N19", "3-To be revised", "Delivered",
         "Rev E required (TM N19, 25-May-2026), pending ADASA response to Technical Note P22-NT-09-000-001-0. Rev D closes the TM N3 flow-rate observation (22 cartridges at 2.23 m3/h, within envelope) and retains FRP per original offer, but materialises the horizontal-to-vertical configuration change (OBS-01 CRITICAL) and the Filtrek-to-Sysflo vendor substitution (OBS-02 MAJOR) before ADASA's formal position on the 22-May Mitigation Plan. OBS-03: updated container as-built drawing not delivered. Procurement on Sysflo pre-response at BW Water risk. NT-001 cycle: FAT/SAT table + remaining clarifications due 15-Jun-2026.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N19: Rev B->C, E6->E45, N2->N19, 2-AN->3-TBR (same H->V + Sysflo; pH 2-12)
    (10, "DS CIP Cartridge Filter",
         "P22-ET-09-009-006", "C", "E45", "N19", "3-To be revised", "Delivered",
         "Rev D required (TM N19, 25-May-2026), pending NT-001 response cycle. First standalone CIP filter datasheet; technical content compliant with ET — Cartridge Filter (31 cartridges at 1.84 m3/h, DN100 ASME B16.5 Cl 150, 7 bar). Same H-to-V configuration change (OBS-01 CRITICAL) and Sysflo vendor substitution (OBS-02 MAJOR) as the RO filter; OBS-03: FRP housing and gasket compatibility with CIP cycle pH 2-12 not documented; OBS-04: container as-built drawing not delivered. NT-001 cycle due 15-Jun-2026.",
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

    # UPDATED TM N18: re-disposed Code 1; E31->E40, N15->N18, 2-AN->1-Approved
    (16, "A/C Thermal Calculation",
         "P22-CD-09-005-002", "C", "E40", "N18", "1-Approved", "Delivered",
         "Rev C approved (TM N18, 18-May-2026). Calculation correct as-is \u2014 no revision required (heat load 6.24 kW = 1.774 TR, 15% margin 2.04 TR, selected 2.5 HP 2.01 TR = +13.3% over un-margined peak; n+1 confirmed, 1 duty + 1 standby). Closes TM N15 NOTE-02 and TM N2 OBS-02. Section 3 deliverable: state the effective post-selection margin explicitly (2.01 TR vs 1.774 TR = +13.3%) at IFC Rev 0 for design-basis traceability.",
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

    # UPDATED TM N20: Rev B (N19, 2-AN) -> Rev 0 IFC, E47, 1-Approved
    (20, "Single Line Diagram",
         "P22-CD-09-007-001", "0", "E47", "N20", "1-Approved", "Delivered",
         "IFC Rev 0 accepted (TM N20, 10-Jun-2026). Both TM N19 items incorporated under revision clouds on sheet 3: principal enclosure labelled 'P22-LCP-001 (METAL CLAD, NEMA4X/IP66, FLOOR STANDING TYPE)' and surge protection device on the 400 A incoming feeder (Uc 415 Vac, Imax 50 kA). CIP Heater branch reflects the Heater Control Panel arrangement. The NEMA 4X/IP66 label is part of the enclosure-consistency basis invoked against the PLC-LCP Outline Panel Drawing (item #98).",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev B (N19, Code 1) -> Rev 0 IFC, E47, 1-Approved
    (21, "Electrical Load List",
         "P22-LI-09-007-001", "0", "E47", "N20", "1-Approved", "Delivered",
         "IFC Rev 0 accepted (TM N20, 10-Jun-2026). 23 loads at 380 V 3-phase / 220 V single-phase 50 Hz, total 144.00 kW / 312 A with safety factor. Reproduced from Rev B (Code 1 in TM N19) without undeclared change. Section 3 deliverable: Pt-100 motor RTD declaration on the Motor Datasheet when issued.",
         "ET Sec.7: Max. 90 days from NTP"),

    (22, "DS Electrical Auxiliaries",
         "P22-ET-09-007-001", "A", "E1", "N1", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev B (N19, Code 1) -> Rev 0 IFC, E47, 1-Approved
    (23, "DS Power & Control Cable",
         "P22-ET-09-007-002", "0", "E47", "N20", "1-Approved", "Delivered",
         "IFC Rev 0 accepted (TM N20, 10-Jun-2026). Five cable families (power, grounding, control, instrument, Ethernet) with IEC 60228 / EN 50525 compliance and UL/CE/RoHS certifications, reproduced from Rev B (Code 1 in TM N19) without undeclared change.",
         "ET Sec.7: Max. 90 days from NTP"),

    (24, "DS Cable Tray",
         "P22-ET-09-007-003", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    (25, "DS Conduit & Flexible",
         "P22-ET-09-007-004", "A", "E9", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev B (N19, 2-AN) -> Rev 0 IFC, E47, 1-Approved
    (26, "Power Cable Schedule",
         "P22-LI-09-007-002", "0", "E47", "N20", "1-Approved", "Delivered",
         "IFC Rev 0 accepted (TM N20, 10-Jun-2026). TM N19 OBS-01 closed: REL-09-001 CIP Heater now defined as two explicit cable runs (feeder to Heater Control Panel; Heater Control Panel to heater element, 10 mm2 4G), consistent with the Heater Control Panel block on the Single Line Diagram Rev 0.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N21: Rev E->F, E42->E48, N19->N21, 3-TBR->1-Approved (schedule embedded; approved, issue at Rev 0)
    (27, "Grounding Layout",
         "P22-DWG-09-007-003", "F", "E48", "N21", "1-Approved", "Delivered",
         "Rev F approved (TM N21, 11-Jun-2026), returned ahead of the 17-Jun commitment. The grounding schedule is now embedded as a complete 48-conductor table (PE identifiers, cross-section per load, ring-main topology, equipotential bonding per NCh Elect. 4/2003 Seccion 10.0), closing the TM N11 OBS-03 item open ~88 days across three cycles; Cu-bare vs insulated distinction addressed. Note 5 relocation removed, main panel fixed, conductor sizing unified to IEC 60364-5-54, CCS legible. Approved as-is \u2014 issue directly at IFC Rev 0; complete the revision-history change descriptions + ECN per revision B-F as part of that issuance (documentation item from TM N19, no new revision required).",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N19: Rev B->C, E32->E42, N15->N19, 3-TBR->1-Approved (longest-open inheritance CLOSED)
    (28, "Cable Tray Layout",
         "P22-DWG-09-007-004", "C", "E42", "N19", "1-Approved", "Delivered",
         "Rev C approved (TM N19, 25-May-2026). Closes the LONGEST-OPEN INHERITANCE in the project: TM N4 OBS-06/07 (vibration transmitter and Pt-100 sensor locations, 110 days open) plus the five TM N15 OBS-04 to OBS-08, all with specific evidence on the Consolidated Comment Sheet. Drawing accepted as-is. Section 3 deliverable: consolidated table of S1 to S7 zone reference positions with minimum separation distances.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N21: Rev A->B, E1->E48, N1->N21, 2-AN->3-TBR (no HART acquisition path; RTD reconciliation)
    (29, "DS PLC & HMI",
         "P22-ET-09-008-001", "B", "E48", "N21", "3-To be revised", "Delivered",
         "Rev B to be revised (TM N21, 11-Jun-2026). Committed hardware: CompactLogix 5380 5069-L320ER, PanelView Plus 7 2711P-T10C22D9P, 5069-IB16/OB16/IF8/OF4-OF8 — selection accepted; TM N1 Modbus query answered via Control System Architecture Rev B (ProSoft PLX32-EIP-MBTCP gateway). OBS-01 (MAJOR): no HART acquisition path in the panel (5069-IF8 reads 4-20 mA only, no HART-capable AI nor HART multiplexer) while the Technical Specification requires 4-20 mA + HART instrumentation — provide HART acquisition or justify. OBS-02 (MINOR): module list omits the two 5069-IY4 RTD modules (8 motor Pt-100 channels) of the LCP Datasheet Rev B / Schematic — reconcile. NOTE-01: cover typo 'PD Tattal'. Rev C required.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N14: Rev D, E26, N14, 1-Approved
    (30, "Control Architecture",
         "P22-CD-09-004-001", "D", "E26", "N14", "1-Approved", "Delivered",
         "Rev D approved (TM N14). UPS 8h verified (40Ah \u00f7 4.35A = 9.2h). All TM N10 observations closed.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev 1 (N19, 2-AN condicional) -> Rev 2, E47, 3-TBR (reversion: Rev D not delivered)
    (31, "IO List",
         "P22-LI-09-008-001", "2", "E47", "N20", "3-To be revised", "Delivered",
         "REVERTED to Code 3 (TM N20, 10-Jun-2026): the TM N19 conditional acceptance lapsed by its own terms \u2014 Plant Control Philosophy Rev D was not delivered within the fourteen-day window (expired 08-Jun-2026). Rev 2 closes the technical items: analyser power supplies reconciled to 24 VDC vs Instrument List (closes TM N14 NOTE-02, ~96 days), VFD output frequency and accumulated energy added on Ethernet/IP for both pumps, dosing IN REMOTE declared as soft I/O from HMI faceplate. The register cannot consolidate IFC status until Rev D is issued and any signal divergence reconciled. Minor QA: item numbering gaps (127-129, 133-135), Rev 2 row missing in revision-history block, dosing RUNNING labelled DI while routed Ethernet/IP.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev D->E, E37->E46, N17->N20, 2-AN->1-Approved (all 4 TM N17 items closed)
    (32, "Instrument List",
         "P22-LI-09-008-003", "E", "E46", "N20", "1-Approved", "Delivered",
         "Rev E approved (TM N20, 10-Jun-2026). Closes all four TM N17 items: Wilcoxon range resolved on the rms basis (vendor full-scale 12.7 mm/s peak = 8.9 mm/s rms, consistent with 'mm/s rms' on items 7/18/19); material-upgrade procurement impact confirmed in writing as nil; vibration transmitter working-medium cells corrected; Comment Sheet header references the correct 25007 Taltal project. Instrument count unchanged at 38. Section 3 tracked item: written confirmation of the TIT-09-006 span configuration (0-600 C declared vs 0-100 C CIP operating range \u2014 plausible as Pt100 element range).",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N18: re-disposed Code 1; same Rev D re-issued w/ CCS; E27->E38, N14->N18
    (33, "Valve List",
         "P22-LI-09-005-002", "D", "E38", "N18", "1-Approved", "Delivered",
         "Rev D approved (TM N18, 18-May-2026). Same Rev D table (18-Mar-2026, 111 items, TAG uniqueness verified vs P&ID Rev C in TM N14) re-issued with a Consolidated Comment Sheet \u2014 table correct as-is, no revision required. Section 3 deliverable: PSV-09-002 overpressure / relief sizing analysis (protected volume, relief scenario, set pressure, required vs installed capacity) for the removed second PSV-09-002, prior to IFC Rev 0.",
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

    # UPDATED TM N20: Rev 0 (N19, 3-TBR) -> Rev 1, E47, stays 3-TBR (new register-integrity defects)
    (36, "I&C Cable Schedule",
         "P22-LI-09-008-002", "1", "E47", "N20", "3-To be revised", "Delivered",
         "Rev 2 (Issued for Approval) required (TM N20, 10-Jun-2026). Rev 1 closes the four TM N19 items (VFD comms now shielded 4-pair Ethernet/IP for both pumps; dosing assignments match the soft-I/O scheme; LSH/LSL identifiers; Full Tag column on every row) but introduces new register-integrity defects: OBS-01 (MAJOR) duplicate item numbers 54/55/56 on sheet 4 — unique cable identification broken for procurement and field termination; OBS-02 (MAJOR) copy-paste valve PWR descriptions ('RO 2ND STAGE CIP FEED MOTORIZED VALVE POWER' on non-CIP-feed valves); OBS-03 Function column 'PIT' on LIT/TIT rows; NOTE-01 RTD cable construction divergence HP vs CIP + VT09-001 remark conflict. Cannot reach IFC while Plant Control Philosophy Rev D remains undelivered.",
         "ET Sec.7: Max. 90 days from NTP"),

    (37, "Chemical Consumption List",
         "P22-LI-09-009-002", "A", "E7", "N3", "1-Approved", "Delivered",
         "None",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N18: Rev B->C, E23->E38, N12->N18, 2-AN->1-Approved
    (38, "Line List",
         "P22-LI-09-009-003", "C", "E38", "N18", "1-Approved", "Delivered",
         "Rev C approved (TM N18, 18-May-2026). Closes both outstanding TM N12 notes: NOTE-01 (line MAKE-UP FOR CIP now PE-PVC-DN80-09-019) and NOTE-02 (Super Duplex lines re-designated SCH80S per ASME B36.19M). No new observations; no further revision required.",
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

    # UPDATED TM N20: Rev B->C, E37->E46, N17->N20, 2-AN->1-Approved
    (49, "DS Pressure Transmitter",
         "P22-LI-09-008-012", "C", "E46", "N20", "1-Approved", "Delivered",
         "Rev C approved (TM N20, 10-Jun-2026). Closes both TM N17 items: Hastelloy C scope confirmed for PIT-09-001 through 008 with PIT-09-009 retained in SS316L, procurement impact confirmed in writing as nil; the implausible 'Sealing: Aluminium' entry resolved — row was mislabelled and now reads 'Material - Diaphragm', with Aluminium correctly confined to the housing. Ranges and tags cross-check clean against the Instrument List Rev E. Schneider Foxboro IGP05S, 4-20 mA HART, IP66/IP67, NEMA 4X, SIL3 retained.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev C (N19, 2-AN) -> Rev 0 IFC, E47, 1-Approved
    (50, "Power Works Drawing",
         "P22-DWG-09-007-005", "0", "E47", "N20", "1-Approved", "Delivered",
         "IFC Rev 0 accepted (TM N20, 10-Jun-2026). TM N19 note incorporated: sheet 8 carries the load-type to grounding-method mapping (METHOD 1-3 cable tray bonding variants, METHOD 4 skid and structural steel, METHOD 5 pumps and motors, METHOD 6 panels and junction boxes, METHOD 7 field instruments) with conductor sizing referenced to IEC 60364-5-54. Rev C (TM N19, Code 2) had closed the four TM N17 notes: IEC 60364-5-54 adopted replacing NEC, seven grounding methods shown, feed direction declared, W100xH100 tray space reserved for ADASA.",
         "ET Sec.7: Max. 90 days from NTP"),

    # CORRECTED TM N14: Rev A->B, E16->E28, N8->N14, 3-TBR->1-Approved
    (51, "DS Temperature Transmitter",
         "P22-LI-09-008-013", "B", "E28", "N14", "1-Approved", "Delivered",
         "Rev B approved (TM N14). TM N8 OBS-01/02/03 CLOSED. TIT-09-006 (CIP Tank): Rosemount 214C + 644, 4-20mA HART, flange DN40.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev 0->1, E35->E46, N17->N20, stays 2-AN
    (52, "Data Transfer List (Modbus TCP)",
         "P22-LI-09-008-004", "1", "E46", "N20", "2-AN", "Delivered",
         "Rev 1 approved as noted (TM N20, 10-Jun-2026). Closes both TM N17 notes: new Commissioning Reference header declares ADASA as Modbus master / BW RO PLC as slave, floating-point Big-Endian (AB-CD), word and byte swap OFF, PLC IP address; vibration register scaling matches the rms basis accepted on the Instrument List Rev E. OBS-01 (MAJOR): register 30019 (CIT09-002) declares scale 0-20 uS/cm \u2014 cannot represent the 200-1000 uS/cm permeate service nor the AHH 800 uS/cm setpoint; instrument span is 0-20000 uS/cm; harmonise registers 30019/30021 to a single declared span and unit at IFC Rev 0 (no new revision required). NOTE-01: confirm TIT09-006 span 0-600 C.",
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
    # UPDATED TM N20: Project Schedule Rev A formally submitted (E47) — recovery baseline adopted 09-Jun
    (59, "Detailed Schedule / Project Schedule",
         "P22-BA-09-000-001", "A", "E47", "N20", "2-AN", "Delivered",
         "Rev A approved as noted (TM N20, 10-Jun-2026). Formal submittal of the recovery schedule delivered by email 08-Jun-2026 and ADOPTED by ADASA as recovery baseline, with reservations, in the letter of 09-Jun-2026. Binding anchor milestones: vessels ex-works Spain 23-Jun, Penang arrival 02-Aug, module ex-works Penang 15-Aug, finish 19-Nov. OBS-01 (MAJOR): programme silent on the RO pressure vessel certification basis — the 23-Jun date corresponds to the non-stamped route per the ADASA waiver of 02-Jun-2026 and the schedule does not state it. OBS-02 (MAJOR): no vessel pressure-test activity visible (factory hydrostatic 1800 psi x 1.1 per Protec letter; pre-FAT system hydrostatics per ET — Inspections During Manufacturing). To incorporate at IFC Rev 0 — baseline adoption of 09-Jun not re-opened.",
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
         "ET Sec.7 p.28 línea 1546", "A", "E34", "N16", "2-AN", "Covered",
         "Cubierto por item #90 Civil and Loading Drawing Rev A (P22-DWG-09-005-001), entregado en TM N16 (24-Apr-2026), Code 2-AN. Tres láminas: layout pedestal, detalle seccional, tabla Equipment Load (15 ítems con pesos seco y operativo). NOTE-01 (weight disclosure de container modificado y RO Skid) tracked for Rev 0 IFC. No requiere documento separado.",
         "ET Sec.7: Max. 90 days from NTP"),

    (65, "Manufacturing and Testing Dossier",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "Prerequisite for factory acceptance",
         "ET Sec.7: Max. 90 days from NTP"),

    (66, "Valve/Instrument Specs (brands+models)",
         "ET Sec 7, p.28", "--", "--", "--", "--", "PARTIAL",
         "Lists delivered but brands/models incomplete for some items",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20 status: Rev D STILL NOT DELIVERED — 4th consecutive cycle, 14-day window expired 08-Jun
    (67, "Control Philosophy",
         "P22-BT-09-009-001", "C", "E39", "N18", "3-To be revised", "Delivered",
         "Rev D required (TM N18, 18-May-2026) — STILL NOT DELIVERED as of TM N20 (10-Jun-2026): FOURTH consecutive transmittal cycle. The fourteen-day window stated in TM N19 expired on 08-Jun-2026 with no delivery; the consequence has materialised — the I/O List conditional acceptance reverted to Code 3 (item #31), and the I&C Cable Schedule (#36), Alarm & Interlock List (#93) and PLC/LCP Schematic (#99) remain gated. ADASA's reservation of contractual remedies under Contract C-4300 stands. OBS-01 (CRITICAL, repeat of TM N15 NOTE-20): HP Pump start permissive 'VE-09-007 and VE-09-007' + 'VE-09-014 fully CLOSED'. OBS-02 (MAJOR): Sequence Charts / Alarm & Control Setpoint List / Control Matrix undelivered. OBS-03 (MAJOR): Salt Rejection formula uses CIT-09-005 instead of CIT-09-001B.",
         "ET Sec.7: Max. 90 days from NTP"),

    (68, "HMI Screen Design",
         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",
         "HMI Screenshots committed at TM N4 — never submitted. ~126 days outstanding as of 10-Jun-2026 (TM N20 Section 3): OLDEST OPEN COMMITMENT in the project. Operator interface undefined.",
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
         "ET \u00a77 l\u00ednea 1568-1616", "--", "--", "--", "--", "NOT DELIVERED",
         "HOLD POINT \u2014 Aprobaci\u00f3n por escrito por ADASA es requisito indispensable para autorizar inicio de fabricaci\u00f3n de componentes mayores y/o ensamblaje principal del m\u00f3dulo (ET \u00a77 l\u00ednea 1612-1614). El Proveedor debe tomar como base P22-IT-09-000-001-0 (PIE Base) y completar con valores num\u00e9ricos, tolerancias, frecuencias, tipo de intervenci\u00f3n (H/W/S/R) y evidencia documental por \u00edtem. Manufacturing prerequisite per contract.",
         "ET Sec.7: Max. 90 days from NTP \u2014 Prerequisite for manufacturing start"),

    # UPDATED: 103 days open as of 15-Apr-2026
    (75, "Modbus TCP Communication System & Memory Map",
         "ET \u00a75.4 l\u00ednea 1075-1077", "--", "--", "--", "--", "NOT DELIVERED",
         "Sistema de comunicaci\u00f3n Ethernet con protocolo Modbus TCP/IP exigido por ET \u00a75.4 (l\u00ednea 1075-1077): 'permita controlar y/o extraer datos en forma remota'. ACTUALIZACION TM N20 (10-Jun-2026): el Memory Map y los parametros de integracion quedan materialmente cubiertos por la Data Transfer List Rev 1 (item #52, 2-AN) con Commissioning Reference (ADASA Modbus master / BW PLC slave, Big-Endian AB-CD, swaps OFF, IP del PLC). Queda pendiente la demostracion del sistema de comunicacion como tal (FAT/comisionamiento) y la consolidacion final condicionada a Control Philosophy Rev D.",
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
         "ET \u00a77 p.30 l\u00ednea 1655-1669", "--", "--", "--", "--", "NOT DELIVERED",
         "HOLD POINT \u2014 Procedimiento debe ser aprobado por ADASA antes del embarque (BAE Cl. 41). Procedimiento detallado de preservaci\u00f3n, embalaje y preparaci\u00f3n para transporte mar\u00edtimo internacional.",
         "ET Sec.7 p.30: 1 month before end of contract \u2014 Required for equipment release to site"),

    # =========================================================
    # NEW TM N15 (22-Apr-2026) — Items 81, 82, 83
    # =========================================================
    # Consolidation: covers former item #74 MCC Datasheet (removed)
    # UPDATED TM N20: Rev A->B, E31->E46, N15->N20, 3-TBR->2-AN (TM N15 OBS-01/02 closed)
    (81, "Datasheet Local Control Panel (LCP)",
         "P22-ET-09-007-005", "B", "E46", "N20", "2-AN", "Delivered",
         "Rev B approved as noted (TM N20, 10-Jun-2026). Closes the two MAJOR TM N15 observations: enclosure fully specified at panel level (nVent Hoffman Type FS FS66S, Stainless Steel 316L, NEMA 4X/IP66, UL508A/IEC 60529, harsh and highly corrosive ambient); I/O module configuration declared (two 5069-IY4 universal analog modules = eight RTD-capable channels for motor Pt-100, three-wire on RTD1/RTD2 strips per PLC/LCP Schematic). OBS-01 (MINOR, TM N15 third observation partially closed): total panel power consumption still not declared — state the design consumption supporting SAI-09-001 2.0 kW (Load List Rev 0) at IFC Rev 0. THIS DATASHEET GOVERNS THE ENCLOSURE SPEC — the Outline Panel Drawing (item #98) must align to it. | Covers ETE Seccion 5.4 combined panel; no separate MCC Datasheet required.",
         "ET Sec.7: Max. 90 days from NTP"),

    # Consolidation: covers former items #60 (General Layouts) and #61 (Arrangement Drawings) bucket placeholders
    (82, "Equipment Layout",
         "P22-DWG-09-005-003", "B", "E32", "N15", "2-AN", "Delivered",
         "Rev B approved as noted (TM N15). Container 40 ft within ET envelope. 16-item equipment list consistent with P&ID Rev C. Section views confirm doors (pedestrian, equipment access, emergency, lateral sliding). Closes TM N5 OBS-03/04/05. NOTE-04 (MAJOR): Operating Weight table to embed in Rev 0 (IFC); BW Water Civil and Loading Drawing delivered Rev A in TM N16 (24-Apr-2026) — see item #90, NOTE-01 tracked for IFC. TM N5 OBS-02 partially open (imperial dimensions retained as primary on Rev 0). | Covers ETE Seccion 7 p.27 'Layouts' (general module arrangement) and p.28 'Planos de arreglo de equipos y canerias en planta y elevacion' (equipment scope).",
         "ET Sec.7: Max. 90 days from NTP"),

    (83, "GA of SWRO System Skid",
         "P22-DWG-09-005-008", "A", "E33", "N15", "2-AN", "Delivered",
         "Rev A approved as noted (TM N15). First revision. Two-sheet GA showing skid envelope, pressure vessel groupings, HP Pump, turbochargers, PSV and process valves. Consistent with Equipment Layout Rev B and Valve List Rev D. NOTE-11 (MAJOR): equipment and valve schedule not provided (vessels per stage, elements per vessel, manifold material/pressure rating, function-vs-tag matrix). NOTE-12 (MAJOR): design pressure and material schedule for skid piping not summarized (ANSI class per service, P-T ratings, wall thickness).",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # ET GAPS DETECTED (23-Apr-2026 cross-check) — Items 84-89
    # =========================================================
    # UPDATED TM N20: NDE Plan Rev A DELIVERED (E47) \u2014 Code 3, Rev B required (vessel scope absent)
    (84, "Plan de Ensayos No Destructivos (NDE) \u2014 Super Duplex",
         "P22-BA-09-000-005", "A", "E47", "N20", "3-To be revised", "Delivered",
         "Rev B required (TM N20, 10-Jun-2026). NDE Plan Rev A delivered in E47, partially responding to the TM N19 procedures item. Weld NDE coverage adequate for piping/structural scope: Super Duplex HP circuit 100% VT, 100% PT root+final, 10% RT butt welds, PMI >=10%; personnel SNT-TC-1A / ISO 9712; acceptance ASME B31.3 / AWS D1.1. OBS-01 (CRITICAL): NO RO PRESSURE VESSEL SCOPE \u2014 factory hydrostatic test (1800 psi x 1.1 per Protec Arisawa letter), the certification basis agreed in the ADASA waiver of 02-Jun-2026, the documentation dossier and the witness arrangement are absent (same gap flagged on the ITP in TM N19). OBS-02 (MAJOR): no ADASA witness/hold points declared (Punto W per ET \u2014 Inspections During Manufacturing). OBS-03: code editions left as placeholders; plan titled 'general'.",
         "ET Sec.8 p.31: Prerequisite for HP fabrication start"),

    (85, "Procedimiento FAT (Factory Acceptance Tests)",
         "ET Seccion 8.1, pp.31-33", "--", "--", "--", "--", "NOT DELIVERED",
         "Procedimiento detallado FAT propuesto por el Proveedor para aprobacion ADASA. Alcance minimo: aprobacion procedimiento, inspeccion visual y dimensional, integridad montaje mecanico, pruebas funcionales en seco, verificacion sistema I&C con simulacion dinamica de escenarios de fallo, revision documental preliminar, conformidad con normativa SEC Chile (Hold Point previo embarque). Pruebas hidrostaticas completadas como prerrequisito. ACTUALIZACION TM N20 (10-Jun-2026): SIGUE PENDIENTE \u2014 la entrega E47 trajo 4 de los procedimientos pedidos en TM N19 (NDE #84, PMI #101, Welding #102, Visual #103); faltan FAT, Hydrostatic y Preservation + ITP Rev C con fechas firmes.",
         "ET Sec.8.1: Prerequisite for factory acceptance and shipment"),

    (86, "Informe PMI (Positive Material Identification)",
         "ET Seccion 8, p.31", "--", "--", "--", "--", "NOT DELIVERED",
         "Identificacion Positiva de Materiales mediante metodo espectrografico en al menos 10% de componentes Super Duplex UNS S32750 del circuito de alta presion (tuberias, accesorios, cuerpos de valvula, bridas). Resultados deben confirmar conformidad con especificacion UNS S32750 y forman parte del Dossier de Calidad. ADASA se reserva derecho de testificar (Punto W). ACTUALIZACION TM N20: el PMI Procedure Rev A fue entregado (item #101, Code 2) \u2014 el INFORME de resultados PMI sigue siendo entregable de fase de fabricacion.",
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

    # =========================================================
    # NEW TM N16 (24-Apr-2026) — Item 90
    # =========================================================
    (90, "Civil and Loading Drawing",
         "P22-DWG-09-005-001", "A", "E34", "N16", "2-AN", "Delivered",
         "Rev A approved as noted (TM N16, single-document submittal 25007-0034). Three-sheet set: plinth layout, sectional detail, and Equipment Load table (15 items with dry and operating weights). Consistent with Equipment Layout Rev B (item #82). NOTE-01 (MAJOR): Weight disclosure to incorporate on Rev 0 (IFC) — (a) total weight of modified 40 ft container; (b) confirm RO Skid operating weight (items 6-7, 8,058 kg) fully accounts for interior piping (super-duplex HP + process), steel mass, fluid inventory, fittings, skid frame, pressure vessels and wet membranes; declare separately if any piping mass excluded. No new revision of Rev A required.",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # NEW TM N17 (05-May-2026) — Items 91, 92, 93
    # =========================================================
    # UPDATED TM N19: Rev A->B, E36->E44, N17->N19, 3-TBR->2-AN (2 CRITICALs closed; 40% milestone prerequisite)
    (91, "Project Quality Plan",
         "P22-BA-09-000-003", "B", "E44", "N19", "2-AN", "Delivered",
         "Rev B approved as noted (TM N19, 25-May-2026). Closes the two CRITICAL TM N17 observations on inspection matrix and FAT scope — a NECESSARY PREREQUISITE for the 40 percent payment milestone under BAE Clause 31, but not on its own sufficient: release remains gated on (a) ADASA validation of the FAT Approval Certificate format, (b) execution of the FAT and signature of the Acta de Aprobacion FAT, and (c) no contractual offsets. ITP procedure codes deferred to the ITP Offsite (item #92). NOTE-01 (MINOR): FAT Approval Certificate specimen template aligned with BAE Clause 31 tracked as deliverable for IFC Rev 0. ADASA rights under BAE Clause 31 reserved until the Acta is signed.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N19: Rev A->B, E36->E44, N17->N19, 2-AN->3-TBR (ASME X silence — Rev C required)
    (92, "Inspection and Test Plan Offsite",
         "P22-BA-09-000-004", "B", "E44", "N19", "3-To be revised", "Delivered",
         "Rev C required (TM N19, 25-May-2026). Rev B closes the operational TM N17 items (placeholder pressures, document control, PMI frequency) but is SILENT on the 'Test certification to ASME X' commitment of the BW Water Technical Offer Rev1 ITP (Section 12) for the RO Pressure Vessels — OBS-01 CRITICAL; the contracted scope cannot be revised by omission; cross-reference NT-001 clarifications 6.A/6.C. NOTE-01 (MAJOR): NDE Plan and other procedures deferred without delivery dates. STATUS AT TM N20 (10-Jun-2026): PARTIALLY ADVANCED — E47 delivered four procedures (NDE #84, PMI #101, Welding #102, Visual #103); STILL OUTSTANDING: ITP Rev C with the certification scope declared per the 02-Jun waiver, plus Hydrostatic, Preservation and FAT procedures with firm dates. The vessel test scope is absent from every document of the E47 set.",
         "ET Sec.7: Max. 90 days from NTP"),

    # UPDATED TM N20: Rev A->B, E37->E46, N17->N20, stays 3-TBR (TM N17 CRITICALs closed; new swap defects)
    (93, "Alarm and Interlock List",
         "P22-LI-09-008-015", "B", "E46", "N20", "3-To be revised", "Delivered",
         "Rev C required (TM N20, 10-Jun-2026). Rev B closes the two TM N17 CRITICALs (permeate conductivity reconciled to uS/cm with setpoints inside the permeate band; LS-09-002 corrected to LSL), harmonises the turbocharger vibration trip actions and adds the digital-alarms section (items 34-51), but is not consistent with the companion lists. OBS-01 (MAJOR): winding/bearing sensor assignment SWAPPED vs Instrument List Rev E on both pump trains (TE-09-001/002 and TE-09-003/004) — with different trip setpoints per sensor, the interlock acts on the wrong element. OBS-02 (MAJOR): vendor-confirmed 95 C bearing AHH not applied (item 27.1 retains 90.0 C, contradicting its own CCS). OBS-03 (MAJOR): PHIT-09-001 tag vs PHIT-09-006 in IL Rev E / DTL. NOTE-01/02: TIT-09-005 vs TIT-09-006 tag; LIT-09-002 range 0-10 m vs setpoints in percent. Rev C must be consistent with IL Rev E and with Control Philosophy Rev D once delivered.",
         "ET Sec.7: Max. 90 days from NTP"),

    # =========================================================
    # ET CROSS-CHECK GAPS (07-May-2026) — Items 94-97
    # =========================================================
    (94, "Mandatory Spare Parts Package",
         "ET Sec.6 p.27 línea 1462-1496", "--", "--", "--", "--", "NOT DELIVERED",
         "PARTE INTEGRAL DEL ALCANCE Y PRECIO BASE (Suma Alzada). ET Sec.6 línea 1462-1496 exige lote mínimo de repuestos críticos para fases de comisionamiento y puesta en marcha. Incluye como mínimo: (1) juego completo de cartuchos para filtro de seguridad; (1) set de fusibles de recambio; (1) transmisor de presión de repuesto (tipo crítico); (1) sensor/electrodo de conductividad; (1) kit de sellos/juntas de repuesto para conexión bridada o acople Victaulic del sistema de alta presión (ítem 5.2.2). Repuestos mandatorios deben entregarse junto con el módulo principal. Documento entregable: lista detallada con descripción + P/N fabricante + cantidad. Verificar inclusión en oferta técnica BW Water Rev1 — si ausente, reclamar formalmente.",
         "ET Sec.6: Delivery with main module — included in base price"),

    (95, "Optional 2-Year Spare Parts List",
         "ET Sec.6 p.27 línea 1497-1501", "--", "--", "--", "--", "NOT DELIVERED",
         "ÍTEM OPCIONAL Y SEPARADO DEL PRECIO BASE. ET Sec.6 línea 1497-1501 exige listado detallado y recomendado de repuestos para dos (2) años de operación normal. Lista debe incluir: descripción, número de parte del fabricante, cantidad recomendada. Cotización opcional separada. Debió presentarse en propuesta técnica BW Water Rev1 — verificar y reclamar si ausente.",
         "ET Sec.6: Required in Technical Proposal"),

    (96, "Performance Tests Report",
         "ET Sec.10.2 línea 1941+", "--", "--", "--", "--", "NOT DELIVERED",
         "PRERREQUISITO PARA RECEPCIÓN PROVISIONAL. ET Sec.10.2 declara que las Pruebas de Desempeño son mandatorias para Recepción Provisional (ET Sec.8.1 línea 1832-1833). Período efectivo de pruebas posterior a Puesta en Marcha. Si las pruebas no resultan satisfactorias, no se emite Acta de Recepción Provisional. Informe debe documentar resultados de todas las pruebas y verificaciones acordadas en el Protocolo de Pruebas de Desempeño.",
         "ET Sec.10.2: Final commissioning phase deliverable"),

    (97, "Acta de Recepción Provisional",
         "ET Sec.10", "--", "--", "--", "--", "NOT DELIVERED",
         "MILESTONE FINAL DEL CONTRATO. Documento emitido por ADASA tras finalización exitosa de Pruebas de Desempeño (item #96). Cierra la fase contractual de ejecución y marca inicio del período de garantía. Posterior a este documento se inicia eventualmente la Recepción Definitiva (post-período garantía).",
         "ET Sec.10: Issued post-Performance Tests success"),

    # =========================================================
    # NEW TM N20 (10-Jun-2026) — Items 98-103 (E46 + E47)
    # =========================================================
    (98, "PLC-LCP Outline Panel Drawing",
         "P22-CD-09-008-001", "A", "E46", "N20", "3-To be revised", "Delivered",
         "Rev B required (TM N20, 10-Jun-2026) — PANEL FABRICATION GATE, flagged urgent by BW Water email 10-Jun-2026 (enclosure ~6 weeks lead time). Dimensional definition complete and consistent (1000+800 W x 600 D x 2000 H mm, double front door); MCC and PLC bills of material sound. OBS-01 (CRITICAL): Panel Specification Sheet (sheet 2) declares SHEET STEEL painted GRAY RAL 7035, PROTECTION CLASS IP55, zinc-plated internals — CONTRADICTING the LCP Datasheet Rev B (FS66S, SS316L unpainted, NEMA 4X/IP66, highly corrosive ambient), the IFC Single Line Diagram label ('METAL CLAD, NEMA4X/IP66') and the ET — Constructive Characteristics of Cabinets (NEMA 4X or IP equivalent). OBS-02 (MAJOR): forced-air cooling incompatible with NEMA 4X/IP66 unless rated filter-fan assemblies; 'For Outdoor Use' vs installation inside the A/C container. OBS-03: PANEL WEIGHT row is a template placeholder. NOTE-01: title block typo 'PD Tattal' + ADASA code printed P22-ET-09-008-001. Enclosure fabrication release gated on Rev B aligned to the LCP Datasheet.",
         "ET Sec.7: Max. 90 days from NTP"),

    (99, "PLC/LCP Schematic Diagram",
         "P22-CD-09-008-002", "A", "E46", "N20", "2-AN", "Delivered",
         "Rev A approved as noted (TM N20, 10-Jun-2026). First submittal, 71 sheets. Wiring regulations consistent with the SLD (380 V 50 Hz 3PH+N+PE, 24 VDC control, 400 A main disconnect, SCCR 36 kA, 600 V cables). PLC rack fully defined: 5069-L320ER CPU, 2x IB16, 1x OB16, 2x IY4 universal analog (the eight RTD-capable channels, three-wire RTD1/RTD2 strips), 5x IF8, 2x OF4; signal assignments consistent with I/O List Rev 2; HP Pump drive PowerFlex 753 (205 A frame) adequate for the 93 kW motor. NOTE-01 (MAJOR): acceptance CONDITIONAL on Plant Control Philosophy Rev D — any signal divergence propagates to panel wiring and terminal assignments; confirm the I/O assignment after Rev D issue (same mechanism as the TM N19 I/O List).",
         "ET Sec.7: Max. 90 days from NTP"),

    (100, "Organization Chart",
         "P22-MTC-09-000-001", "A", "E47", "N20", "1-Approved", "Delivered",
         "Rev A approved (TM N20, 10-Jun-2026). First submittal. Full project organisation with named roles across both BW Water regions: sponsor, project manager and director, fabrication management, engineering disciplines, supply chain, quality (Quality Manager + QA/QC Manager), planning and document control, EHS and project control, with Americas-Asia communication channels declared. Accepted as-is.",
         "ET Sec.7: Max. 90 days from NTP"),

    (101, "PMI Procedure",
         "P22-BA-09-000-006", "A", "E47", "N20", "2-AN", "Delivered",
         "Rev A approved as noted (TM N20, 10-Jun-2026). LIBS technique (SciAps Z-200 / 902C+), API 578/582 basis, five technician certificates attached — sound. Generic subcontractor document scoped to refinery service categories. OBS-01 (MAJOR): add at IFC Rev 0 the project scoping clause mapping PMI to the Taltal Super Duplex HP circuit at 10 percent minimum with UNS S32750 conformity as acceptance basis and the ADASA witness right (Punto W) per ET — Inspections During Manufacturing. OBS-02: refinery clauses (HF acid, fired heaters) not applicable. NOTE-01: cover qualification clause copied from the NDE Plan — replace with the PMI operator qualification. Partially covers item #86 (the PMI results REPORT remains a fabrication-phase deliverable).",
         "ET Sec.8: Prerequisite for HP component release"),

    (102, "Welding Procedure (WPS/PQR)",
         "P22-BA-09-000-007", "A", "E47", "N20", "2-AN", "Delivered",
         "Rev A approved as noted (TM N20, 10-Jun-2026). ASME IX qualification of the two relevant arc-welded base materials: structural carbon steel (GMAW, S275JR) and Super Duplex HP piping (GTAW, SA-790 UNS S32750 with ER2594 and impact testing); six welders qualified 6G on Super Duplex. OBS-01 (MAJOR): thickness-range qualification — the Super Duplex PQR coupon (2.77 mm) qualifies up to 5.54 mm per ASME IX QW-451 while the WPS declares a range to 14.02 mm; provide the qualifying coupon for the upper range or restrict the WPS. OBS-02: low-pressure thermoplastic joining scope not addressed (NDE Plan cites DVS 2202-1 acceptance — state joining method and procedure). NOTE-01: no heat-input limits or ferrite-number acceptance for the Super Duplex WPS — corrosion-critical for the 45,000-55,000 ppm chloride brine service.",
         "ET Sec.8 p.31: Prerequisite for HP fabrication start"),

    (103, "Visual Inspection Procedure (VT)",
         "P22-BA-09-000-008", "A", "E47", "N20", "2-AN", "Delivered",
         "Rev A approved as noted (TM N20, 10-Jun-2026). Direct visual technique per ASME Section V Article 9 (600 mm, 30 degrees, 1000 lux minimum), acceptance per ASME B31.3 and AWS D1.1, records on controlled forms. OBS-01: VT inspector qualification not stated — align with the NDE Plan personnel basis (SNT-TC-1A VT Level II or ISO 9712). OBS-02: scope includes thermoplastic welds but no thermoplastic acceptance criteria cited — add DVS 2202-1 visual acceptance or exclude thermoplastics. NOTE-01: referenced QAM forms/procedures not attached — list as controlled external references.",
         "ET Sec.8: Prerequisite for fabrication QA"),
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
    (27, "Grounding Layout", "P22-DWG-09-007-003", "F", "E48", "25007-0048", "N21", "11-Jun-2026", "1-Approved", 5,
     "Schedule embedded (48 conductors), closing TM N11 OBS-03 (~88d); note 5 removed, IEC 60364-5-54 unified, CCS legible. Approved; issue at Rev 0, completing revision-history descriptions + ECN as part of issuance"),

    # --- Item 28: Cable Tray Layout ---
    (28, "Cable Tray Layout", "P22-DWG-09-007-004", "A", "E11", "25007-0011", "N4", "05-Feb-2026", "3-To be revised", 1,
     "Routing concerns, sizing, duplicate TAG FIT-09-001"),

    # --- Item 29: DS PLC & HMI ---
    (29, "DS PLC & HMI", "P22-ET-09-008-001", "A", "E1", "25007-0001", "N1", "16-Dec-2025", "2-AN", 1,
     "Minor notes (verify Modbus TCP/RTU availability)"),
    (29, "DS PLC & HMI", "P22-ET-09-008-001", "B", "E48", "25007-0048", "N21", "11-Jun-2026", "3-To be revised", 2,
     "Hardware fixed (CompactLogix 5380 5069-L320ER, PanelView Plus 7). OBS-01 MAJOR: no HART acquisition path vs ET 4-20mA+HART; OBS-02 MINOR: omits 5069-IY4 RTD modules; NOTE-01 typo. Modbus closed via Control Architecture Rev B. Rev C required"),

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

    # --- TM N16 (24-Apr-2026) ---
    (90, "Civil and Loading Drawing", "P22-DWG-09-005-001", "A", "E34", "25007-0034", "N16", "24-Apr-2026", "2-AN", 1,
     "First revision. NOTE-01 MAJOR: weight disclosure (modified container + RO Skid breakdown) for Rev 0 IFC"),

    # --- TM N17 (05-May-2026) — UPDATES to existing items ---
    (27, "Grounding Layout", "P22-DWG-09-007-003", "D", "E36", "25007-0036", "N17", "05-May-2026", "2-AN", 4,
     "OBS-01 MAJOR: wrong CC sheet (Cable Tray). NOTE-01/02 MAJOR. TM N11 OBS-03 schedule still NOT incorporated"),
    (31, "IO List", "P22-LI-09-008-001", "0", "E35", "25007-0035", "N17", "05-May-2026", "2-AN", 4,
     "Issued for IFC. 135 IO points. NOTE-01 MAJOR: Antiscalant Pumps lack IN REMOTE DI. NOTE-02/03 MINOR"),
    (32, "Instrument List", "P22-LI-09-008-003", "D", "E37", "25007-0037", "N17", "05-May-2026", "2-AN", 4,
     "Material upgrades (Monel, Nickel 276, Superduplex 2507, Hastelloy C). OBS-01 MAJOR: Wilcoxon range vs datasheet"),
    (49, "DS Pressure Transmitter", "P22-LI-09-008-012", "B", "E37", "25007-0036", "N17", "05-May-2026", "2-AN", 2,
     "Foxboro IGP05S. OBS-01 MAJOR: Hastelloy C extended to 7 PITs - confirm procurement impact"),
    (50, "Power Works Drawing", "P22-DWG-09-007-005", "0", "E36", "25007-0036", "N17", "05-May-2026", "2-AN", 3,
     "Issued for IFC. NOTE-01-04 MAJOR: NEC vs SEC/NCh, pump grounding method, feed direction, duct bank interface"),
    (52, "Data Transfer List (Modbus TCP)", "P22-LI-09-008-004", "0", "E35", "25007-0035", "N17", "05-May-2026", "2-AN", 3,
     "Issued for IFC. 185 mappings. NOTE-01/02 MAJOR: PLC role/byte order, vibration scaling vs Wilcoxon"),

    # --- TM N17 — NEW items ---
    (91, "Project Quality Plan", "P22-BA-09-000-003", "A", "E36", "25007-0036", "N17", "05-May-2026", "3-To be revised", 1,
     "Corporate template does NOT close PIE Base. OBS-01/02 CRITICAL (matrix, FAT). OBS-03/04 MAJOR. Bloquea Hold Points"),
    (92, "Inspection and Test Plan Offsite", "P22-BA-09-000-004", "A", "E36", "25007-0036", "N17", "05-May-2026", "2-AN", 1,
     "ITP 34 activities, 9 Hold Points OK. OBS-01 MAJOR: hydrostatic placeholders. OBS-02/03 MAJOR: doc control, NDE Plan"),
    (93, "Alarm and Interlock List", "P22-LI-09-008-015", "A", "E37", "25007-0037", "N17", "05-May-2026", "3-To be revised", 1,
     "33 instruments. OBS-01 CRITICAL: permeate conductivity unit error mS/cm vs uS/cm (CIT-09-002/003). OBS-02 CRITICAL: LS-09-002 logic"),

    # --- ET Cross-check gaps (07-May-2026) — Items 94-97 NOT DELIVERED ---
    (94, "Mandatory Spare Parts Package", "ET Sec.6 p.27", "--", "--", "--", "--", "--", "--", 0,
     "NOT DELIVERED. Required as integral part of base price (ET Sec.6 línea 1462-1496). Delivery with main module."),
    (95, "Optional 2-Year Spare Parts List", "ET Sec.6 p.27", "--", "--", "--", "--", "--", "--", 0,
     "NOT DELIVERED. Should have been included in BW Water Technical Offer Rev1 — verify and reclaim if absent."),
    (96, "Performance Tests Report", "ET Sec.10.2", "--", "--", "--", "--", "--", "--", 0,
     "NOT DELIVERED. Mandatory for Recepción Provisional (ET Sec.10.2 línea 1941+)."),
    (97, "Acta de Recepción Provisional", "ET Sec.10", "--", "--", "--", "--", "--", "--", 0,
     "NOT DELIVERED. Final contractual milestone — issued by ADASA post-Performance Tests success."),

    # --- TM N18 new Rev entries (18-May-2026, E38-E41, submittals 25007-0038/39/40/41) ---
    # Re-disposed under executive Code 1/2 criterion (CLAUDE.md secciones 6.2/6.3 v6.11): 4 Code 1 + 1 Code 3.
    (67, "Control Philosophy", "P22-BT-09-009-001", "C", "E39", "25007-0039", "N18", "18-May-2026", "3-To be revised", 3,
     "Rev D required (only Code 3 / verdict driver). OBS-01 CRITICAL repeat of TM N15 NOTE-20 (HP Pump permissive VE-09-007 dup + VE-09-014); OBS-02 child docs not delivered; OBS-03 salt rejection formula. Closed NOTE-14/15/18/19/21/23"),
    (33, "Valve List", "P22-LI-09-005-002", "D", "E38", "25007-0038", "N18", "18-May-2026", "1-Approved", 5,
     "Same Rev D re-issued with CCS; re-disposed Code 1 (table correct as-is). PSV-09-002 overpressure analysis tracked to Section 3"),
    (38, "Line List", "P22-LI-09-009-003", "C", "E38", "25007-0038", "N18", "18-May-2026", "1-Approved", 3,
     "Closes TM N12 NOTE-01 (line ID PE-PVC-DN80-09-019) and NOTE-02 (SCH80S per ASME B36.19M). No further revision required"),
    (16, "A/C Thermal Calculation", "P22-CD-09-005-002", "C", "E40", "25007-0040", "N18", "18-May-2026", "1-Approved", 4,
     "Re-disposed Code 1 (calc correct: 1.774 TR, +13.3% margin, n+1 confirmed). Closes TM N15 NOTE-02. Explicit margin statement tracked to Section 3"),
    (2, "P&ID", "P22-DWG-09-009-002", "D", "E41", "25007-0041", "N18", "18-May-2026", "1-Approved", 4,
     "Closes TM N13 NOTE-01 (CIP Tank total 6.8 / effective 6.1 m3, both annotated). Drawing accepted as-is. CIT-09-004 tapping change tracked to Section 3 (Instrument List + Line List + loop-response note)"),

    # --- TM N19 (25-May-2026, E42-E45, submittals 25007-0042/43/44/45, 13 docs) ---
    # Tally: 3 Code 1 + 5 Code 2 + 5 Code 3. NT-001 issued in parallel (Sections 2.10/2.12/2.13 cross-refs).
    (21, "Electrical Load List", "P22-LI-09-007-001", "B", "E42", "25007-0042", "N19", "25-May-2026", "1-Approved", 2,
     "Resubmittal of Rev A (Code 1 N3). 23 loads, 144 kW; matches SLD Rev B + Power/Control Cable DS. Pt-100 Motor DS declaration tracked Section 3"),
    (26, "Power Cable Schedule", "P22-LI-09-007-002", "B", "E42", "25007-0042", "N19", "25-May-2026", "2-AN", 2,
     "26 cable runs, voltage drop <3% (worst 1.62%). OBS-01 MINOR: REL-001 CIP Heater two-cable arrangement not aligned with SLD Rev B"),
    (23, "DS Power & Control Cable", "P22-ET-09-007-002", "B", "E42", "25007-0042", "N19", "25-May-2026", "1-Approved", 2,
     "Five cable families, IEC 60228 / EN 50525, UL/CE/RoHS. SEC compatibility supported. Accepted as-is"),
    (20, "Single Line Diagram", "P22-CD-09-007-001", "B", "E42", "25007-0042", "N19", "25-May-2026", "2-AN", 2,
     "First formal submittal at Rev B. 400 A main, MCCB 250 A 25 kA, 30 mA RCD. OBS-01: enclosure NEMA 4X/IP not declared; NOTE-01: SPDs not visible"),
    (27, "Grounding Layout", "P22-DWG-09-007-003", "E", "E42", "25007-0042", "N19", "25-May-2026", "3-To be revised", 5,
     "OBS-01 MAJOR: grounding schedule per NCh Elect. 4/2003 still missing (TM N11 OBS-03, ~70 days, 3rd consecutive cycle). Rev F required within 14 days; C-4300 escalation reserved"),
    (28, "Cable Tray Layout", "P22-DWG-09-007-004", "C", "E42", "25007-0042", "N19", "25-May-2026", "1-Approved", 3,
     "Closes 7 items: TM N4 OBS-06/07 (110 days) + TM N15 OBS-04..08 — longest-open inheritance CLOSED. S1-S7 zone table tracked Section 3"),
    (50, "Power Works Drawing", "P22-DWG-09-007-005", "C", "E42", "25007-0042", "N19", "25-May-2026", "2-AN", 4,
     "Closes TM N17 NOTE-01..04: IEC 60364-5-54 adopted (replacing NEC), 7 grounding methods shown, feed direction declared, W100xH100 ADASA tray space. NOTE-01: designate method per load type"),
    (31, "IO List", "P22-LI-09-008-001", "1", "E43", "25007-0043", "N19", "25-May-2026", "2-AN", 5,
     "CONDITIONAL Code 2: contingent on Control Philosophy Rev D + addendum if signal divergence. Closes TM N3 inherited items (110 days). OBS-01: analyser voltage (TM N14 NOTE-02) not addressed; OBS-02: IFC with Rev D under Code 3"),
    (91, "Project Quality Plan", "P22-BA-09-000-003", "B", "E44", "25007-0044", "N19", "25-May-2026", "2-AN", 2,
     "Closes TM N17 OBS-01/02 CRITICALs (inspection matrix, FAT scope) — prerequisite for 40% payment milestone BAE Cl.31 (release gated on FAT Certificate + Acta). NOTE-01: FAT Approval Certificate specimen"),
    (92, "Inspection and Test Plan Offsite", "P22-BA-09-000-004", "B", "E44", "25007-0044", "N19", "25-May-2026", "3-To be revised", 2,
     "Closes operational TM N17 items but SILENT on ASME X certification scope for RO PVs (Offer Rev1 ITP Sec.12) — OBS-01 CRITICAL, cross-ref NT-001 6.A/6.C. Rev C required + procedures delivery schedule"),
    (36, "I&C Cable Schedule", "P22-LI-09-008-002", "0", "E44", "25007-0044", "N19", "25-May-2026", "3-To be revised", 2,
     "First formal review of full schedule. OBS-01/02 MAJOR: VFD comms 'PANEL INTERIOR WIRE' unspecified; dosing pumps without IN REMOTE coherence. Rev 1 required; IFC gated by Control Philosophy Rev D"),
    (9, "DS RO Cartridge Filter", "P22-ET-09-009-005", "D", "E45", "25007-0045", "N19", "25-May-2026", "3-To be revised", 3,
     "Closes TM N3 flow-rate OBS (22 cartridges, 2.23 m3/h). OBS-01 CRITICAL: H-to-V change materialised pre-NT-001; OBS-02: Sysflo vendor substitution; OBS-03: container as-built missing. Rev E pending NT-001"),
    (10, "DS CIP Cartridge Filter", "P22-ET-09-009-006", "C", "E45", "25007-0045", "N19", "25-May-2026", "3-To be revised", 3,
     "First standalone CIP filter DS. Same H-to-V + Sysflo as RO filter; OBS-03: FRP/gasket pH 2-12 compatibility not documented; OBS-04: container as-built. Rev D pending NT-001"),

    # --- TM N20 (10-Jun-2026, E46 28-May 7 docs + E47 09-Jun 13 docs, submittals 25007-0046/47, 20 docs) ---
    # Tally: 8 Code 1 + 7 Code 2 + 5 Code 3. Drivers: Outline enclosure contradiction, Control Philosophy Rev D 4th cycle, NDE vessel silence.
    (32, "Instrument List", "P22-LI-09-008-003", "E", "E46", "25007-0046", "N20", "10-Jun-2026", "1-Approved", 5,
     "Closes all 4 TM N17 items: Wilcoxon rms basis (12.7 peak = 8.9 rms), nil procurement impact in writing, working-medium cells, CCS header 25007. 38 instruments. TIT-09-006 span confirmation tracked Section 3"),
    (52, "Data Transfer List (Modbus TCP)", "P22-LI-09-008-004", "1", "E46", "25007-0046", "N20", "10-Jun-2026", "2-AN", 4,
     "Closes both TM N17 notes (ADASA master / PLC slave, Big-Endian AB-CD, swaps OFF, PLC IP; rms scaling). OBS-01 MAJOR: register 30019 scale 0-20 uS/cm vs instrument span 0-20000 uS/cm — harmonise at IFC"),
    (49, "DS Pressure Transmitter", "P22-LI-09-008-012", "C", "E46", "25007-0046", "N20", "10-Jun-2026", "1-Approved", 3,
     "Closes both TM N17 items: Hastelloy C PIT-001..008 nil procurement impact in writing (PIT-009 SS316L); 'Sealing: Aluminium' row relabelled 'Material - Diaphragm'. Clean vs IL Rev E"),
    (93, "Alarm and Interlock List", "P22-LI-09-008-015", "B", "E46", "25007-0046", "N20", "10-Jun-2026", "3-To be revised", 2,
     "Closes both TM N17 CRITICALs (uS/cm reconciled; LS-09-002 = LSL) + digital alarms added. OBS-01 MAJOR: winding/bearing SWAPPED vs IL Rev E both pump trains; OBS-02: 95 C AHH not applied; OBS-03: PHIT tag. Rev C required"),
    (81, "Datasheet LCP", "P22-ET-09-007-005", "B", "E46", "25007-0046", "N20", "10-Jun-2026", "2-AN", 2,
     "Closes TM N15 OBS-01/02: FS66S SS316L NEMA 4X/IP66 + 2x 5069-IY4 = 8 RTD channels. OBS-01 MINOR: total panel power consumption to declare at IFC. Governs enclosure spec vs Outline (#98)"),
    (98, "PLC-LCP Outline Panel Drawing", "P22-CD-09-008-001", "A", "E46", "25007-0046", "N20", "10-Jun-2026", "3-To be revised", 1,
     "OBS-01 CRITICAL: Panel Spec Sheet (SHEET STEEL RAL 7035, IP55) contradicts LCP DS Rev B (SS316L NEMA 4X/IP66), SLD Rev 0 and ET — FABRICATION GATE (BW urgent 10-Jun). OBS-02: cooling vs IP66; OBS-03: weight TBD. Rev B required"),
    (99, "PLC/LCP Schematic Diagram", "P22-CD-09-008-002", "A", "E46", "25007-0046", "N20", "10-Jun-2026", "2-AN", 1,
     "First submittal, 71 sheets. Rack 5069-L320ER consistent with I/O List Rev 2; PowerFlex 753 adequate for 93 kW. NOTE-01 MAJOR: conditional on Control Philosophy Rev D signal stability"),
    (21, "Electrical Load List", "P22-LI-09-007-001", "0", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 3,
     "IFC issue of Rev B (Code 1 TM N19) without undeclared change. 23 loads, 144.00 kW / 312 A. IFC accepted"),
    (26, "Power Cable Schedule", "P22-LI-09-007-002", "0", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 3,
     "TM N19 OBS-01 incorporated: REL-09-001 two explicit cable runs via Heater Control Panel (10 mm2 4G). IFC accepted"),
    (23, "DS Power & Control Cable", "P22-ET-09-007-002", "0", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 3,
     "IFC issue of Rev B without undeclared change. IFC accepted"),
    (20, "Single Line Diagram", "P22-CD-09-007-001", "0", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 3,
     "Both TM N19 items incorporated under revision clouds: 'P22-LCP-001 (METAL CLAD, NEMA4X/IP66)' label + SPD Uc 415 Vac / Imax 50 kA. IFC accepted"),
    (50, "Power Works Drawing", "P22-DWG-09-007-005", "0", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 5,
     "TM N19 note incorporated: grounding method per load type (METHOD 1-7) with IEC 60364-5-54 conductor sizing. IFC accepted"),
    (31, "IO List", "P22-LI-09-008-001", "2", "E47", "25007-0047", "N20", "10-Jun-2026", "3-To be revised", 6,
     "Technical items closed (analysers 24 VDC closing TM N14 NOTE-02 ~96 days; VFD freq/energy; IN REMOTE soft I/O). TM N19 conditional acceptance LAPSED — Control Philosophy Rev D not delivered: REVERTS to Code 3"),
    (36, "I&C Cable Schedule", "P22-LI-09-008-002", "1", "E47", "25007-0047", "N20", "10-Jun-2026", "3-To be revised", 3,
     "All 4 TM N19 items closed (Ethernet/IP VFD comms, soft-I/O dosing, LSH/LSL, Full Tag column). NEW: duplicate item numbers 54/55/56 sheet 4 + copy-paste valve PWR descriptions. Rev 2 required; gated by Rev D"),
    (100, "Organization Chart", "P22-MTC-09-000-001", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "1-Approved", 1,
     "First submittal. Full organisation with named roles, Americas-Asia channels declared. Accepted as-is"),
    (59, "Project Schedule", "P22-BA-09-000-001", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "2-AN", 1,
     "Recovery baseline ADOPTED with reservations (ADASA letter 09-Jun): ex-works Spain 23-Jun, Penang 02-Aug, EXW Penang 15-Aug, finish 19-Nov. OBS-01/02: ASME waiver basis + vessel hydrostatic activities to state at IFC"),
    (84, "NDE Plan", "P22-BA-09-000-005", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "3-To be revised", 1,
     "Weld NDE coverage adequate (Super Duplex 100% VT/PT, 10% RT, PMI >=10%). OBS-01 CRITICAL: NO RO pressure vessel scope (hydrostatic 1800 psi x 1.1, 02-Jun waiver basis, dossier, witness absent). OBS-02: no ADASA Punto W. Rev B required"),
    (101, "PMI Procedure", "P22-BA-09-000-006", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "2-AN", 1,
     "LIBS SciAps Z-200/902C+, API 578/582, 5 certificates. OBS-01 MAJOR: Taltal Super Duplex >=10% scope + UNS S32750 acceptance + ADASA Punto W to add at IFC. Generic refinery clauses to delimit"),
    (102, "Welding Procedure", "P22-BA-09-000-007", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "2-AN", 1,
     "ASME IX WPS/PQR: S275JR GMAW + SA-790 UNS S32750 GTAW (ER2594); 6 welders 6G. OBS-01 MAJOR: PQR coupon 2.77 mm qualifies to 5.54 mm vs WPS 14.02 mm. OBS-02: thermoplastic joining scope. NOTE-01: heat input / ferrite"),
    (103, "Visual Procedure", "P22-BA-09-000-008", "A", "E47", "25007-0047", "N20", "10-Jun-2026", "2-AN", 1,
     "Direct VT per ASME V Art.9 (600 mm / 30 deg / 1000 lux), acceptance B31.3 + AWS D1.1. OBS-01: inspector qualification; OBS-02: thermoplastic criteria DVS 2202-1; NOTE-01: QAM references not attached"),
]


# ============================================================
# OPEN OBSERVATIONS (for Summary sheet)
# ============================================================
OPEN_OBSERVATIONS = [
    # ===== CARRY-FORWARD INVENTORY per TM N20 Section 3 (10-Jun-2026) =====
    ("TM N18 OBS-01/02/03 — 4th cycle", "Plant Control Philosophy Rev C", "Rev D NOT DELIVERED — FOURTH consecutive transmittal. The 14-day window stated in TM N19 EXPIRED 08-Jun-2026. OBS-01 CRITICAL HP Pump start permissive (repeat of TM N15 NOTE-20); OBS-02 Sequence Charts / Setpoint List / Control Matrix undelivered; OBS-03 salt rejection formula", "18-May-2026", "Consequence materialised at TM N20: I/O List reverted to Code 3; IC Cable Schedule, A&I List and PLC/LCP Schematic gated. ADASA reservation of remedies under Contract C-4300 stands"),
    ("TM N11 OBS-03 / TM N19 OBS-01", "Grounding Layout Rev E", "Grounding schedule per NCh Elect. 4/2003 Seccion 10.0 still missing — ~86 days, third consecutive cycle. Revision-history block + legible CCS also pending", "17-Mar-2026", "Rev F COMMITTED for Wednesday 17-Jun-2026 (clarification exchange 03-Jun). SEC compliance Hold Point remains gated"),
    ("TM N4 NOTE-05", "HMI Screenshots (P22-BREAD-09-008-001)", "Committed at TM N4 — never submitted. ~126 days: OLDEST open commitment in the project", "05-Feb-2026", "OPEN"),
    ("TM N19 OBS-01 CRITICAL (ITP)", "ITP Offsite Rev B", "Silent on the ASME X certification scope for RO Pressure Vessels (Technical Offer Rev1 ITP Sec.12) — cross-ref NT-001 6.A/6.C; vessel test scope absent from every E47 quality document", "25-May-2026", "OUTSTANDING: ITP Rev C with certification scope per the 02-Jun waiver + Hydrostatic, Preservation and FAT procedures with firm dates (E47 delivered NDE/PMI/Welding/Visual = 4 of 7)"),
    ("TM N19 Sections 2.12/2.13", "Cartridge Filters RO Rev D / CIP Rev C", "H-to-V configuration change + Filtrek-to-Sysflo vendor substitution materialised pre-NT-001; container as-built drawing missing; CIP pH 2-12 compatibility undocumented", "25-May-2026", "Rev E / Rev D PENDING NT-001 cycle — FAT/SAT table + remaining clarifications due 15-Jun-2026"),
    # ===== NEW OPEN at TM N20 (10-Jun-2026) =====
    ("TM N20 OBS-01 CRITICAL", "PLC-LCP Outline Panel Drawing Rev A", "Panel Specification Sheet (SHEET STEEL painted RAL 7035, IP55, zinc-plated internals) contradicts LCP Datasheet Rev B (SS316L, NEMA 4X/IP66), SLD Rev 0 IFC label and ET — Cabinets", "10-Jun-2026", "Rev B required — enclosure FABRICATION GATE (BW Water urgent request 10-Jun; ~6 weeks lead). OBS-02 cooling vs IP66; OBS-03 weight TBD"),
    ("TM N20 OBS-01/02/03 MAJOR", "Alarm & Interlock List Rev B", "Winding/bearing sensor assignment SWAPPED vs Instrument List Rev E on both pump trains; vendor-confirmed 95 C bearing AHH not applied; PHIT-09-001 vs PHIT-09-006 tag divergence", "10-Jun-2026", "Rev C required — consistent with IL Rev E and Control Philosophy Rev D once delivered"),
    ("TM N20 OBS-01 (I/O reversion)", "I/O List Rev 2", "TM N19 conditional acceptance lapsed (Control Philosophy Rev D not delivered) — register cannot consolidate IFC status until Rev D issued and signal divergence reconciled", "10-Jun-2026", "Deliver Rev D + re-issue Rev 3 (or confirm Rev 2 unchanged) within the same cycle; minor QA corrections noted"),
    ("TM N20 OBS-01/02 MAJOR", "I&C Cable Schedule Rev 1", "Duplicate item numbers 54/55/56 on sheet 4 + copy-paste valve PWR descriptions — unique cable identification broken for procurement and field termination", "10-Jun-2026", "Rev 2 (Issued for Approval) required; IFC gated by Control Philosophy Rev D"),
    ("TM N20 OBS-01 CRITICAL (NDE)", "NDE Plan Rev A", "No RO pressure vessel scope: factory hydrostatic (1800 psi x 1.1 per Protec letter), 02-Jun waiver certification basis, documentation dossier and witness arrangement absent", "10-Jun-2026", "Rev B required; OBS-02 add ADASA witness/hold points (Punto W); OBS-03 state code editions"),
    ("TM N20 OBS-01 MAJOR", "Welding Procedure Rev A", "Super Duplex PQR coupon (2.77 mm) qualifies up to 5.54 mm per ASME IX QW-451 vs WPS declared range to 14.02 mm", "10-Jun-2026", "Qualifying coupon for upper range or WPS restriction at IFC Rev 0; thermoplastic joining scope + ferrite/heat-input to state"),
    ("TM N20 OBS-01/02 MAJOR", "Project Schedule Rev A", "Certification basis of RO PVs (non-stamped route per 02-Jun waiver) not stated; no vessel pressure-test activity shown as dated activity", "10-Jun-2026", "Incorporate at IFC Rev 0 — recovery baseline adoption of 09-Jun-2026 not re-opened"),
    # ===== TRACKED for IFC Rev 0 (no new revision of the reviewed document) =====
    ("Tracked for IFC Rev 0 (TM N18-N19)", "Valve List / P&ID / AC Thermal / Motor DS / Cable Tray / PQP", "PSV-09-002 relief sizing analysis; P&ID CIP Tank dual-value convention; CIT-09-004 loop-response note; AC Thermal effective margin statement (+13.3%); Motor Datasheet Pt-100 declaration; Cable Tray S1-S7 zone table; PQP FAT Approval Certificate specimen (BAE Cl.31)", "25-May-2026", "NO ADVANCE in E46/E47 (TM N20 Section 3)"),
    ("Tracked for IFC Rev 0 (TM N20 new)", "Instrument List Rev E / Data Transfer List Rev 1 / LCP Datasheet Rev B", "TIT-09-006 span configuration written confirmation (0-600 C); DTL registers 30019/30021 conductivity span harmonisation; LCP total panel power consumption declaration", "10-Jun-2026", "Tracked for IFC Rev 0 — no new revision required"),
    # ===== PERSISTENT minor items from prior TMs =====
    ("TM N13 NOTE-02", "Cable Tray Layout drawings", "Internal cable routing not submitted \u2014 tracked in ADASA email 10-Apr-2026 (not part of the 7 items closed by Rev C at TM N19)", "06-Apr-2026", "~65 days outstanding"),
    ("TM N10 OBS-05", "GA Antiscalant Dosing Tank", "Working volume, body material, seismic anchor data (NCh 2369)", "12-Mar-2026", "GA Rev B required (~90 days outstanding)"),
    ("TM N5 OBS-02", "Equipment Layout Rev B", "Imperial dimensions retained as primary on Rev 0 \u2014 partially open", "23-Feb-2026", "~107 days outstanding (partial)"),
    ("TM N16 NOTE-01", "Civil and Loading Drawing Rev A", "Modified container weight + RO Skid weight breakdown disclosure", "24-Apr-2026", "Tracked for Rev 0 IFC (Code 2 \u2014 no new revision required)"),
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
     [i for i in list(range(1, 76)) + [81, 82, 83, 90, 91, 92, 93, 98, 99, 100] if i not in (60, 61, 65, 69, 74)]),
    ("2. HANDOVER — ET Chapter 7 (1 month before end of contract) + Spare Parts (ET Chapter 6)",
     [76, 77, 78, 79, 80, 94, 95]),
    ("3. FABRICATION & FAT — ET Chapter 8 (out of engineering scope)",
     [65, 84, 85, 86, 101, 102, 103]),
    ("4. COMMISSIONING — ET Chapter 9 (out of engineering scope)",
     [87, 88, 89]),
    ("5. RECEPCIÓN PROVISIONAL — ET Chapter 10 (final contractual milestones)",
     [96, 97]),
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
        ("Transmittals Issued", "21 (N1 through N21 — TM N5 issued in Rev 0 and Rev 1)"),
        ("Deliveries Received", "48 (E1 through E48)"),
        ("First Delivery Date", "10-Dec-2025 (E1)"),
        ("Latest Delivery Date", "09-Jun-2026 (E48)"),
        ("Status Date", "11-Jun-2026"),
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
        1: "Piping Spec, DS DP Switch, DS Level Transmitter, Civil & Loading (#90), Org Chart (#100), Project Schedule (#59), NDE Plan (#84), PMI/Welding/Visual (#101-103), Outline Panel (#98), Schematic (#99)",
        2: "Process Calc, DS UHPRO, DS CIP Pump, DS Vibration, PQP (#91 A\u2192B), ITP Offsite (#92 A\u2192B), A&I List (#93 A\u2192B), LCP Datasheet (#81 A\u2192B)",
        3: "DS HP Pump, DS Feed Turbocharger, SLD (#20 A\u2192B\u21920), Load List (#21 A\u2192B\u21920), Power Cable Schedule (#26 A\u2192B\u21920), Cable Tray (#28 A\u2192B\u2192C), Cartridge Filters (#9/#10), I&C Cable Schedule (#36 A\u21920\u21921), DS Pressure Trans (#49 A\u2192B\u2192C)",
        4: "P&ID (A\u2192D), Control Architecture (A\u2192D), A/C Thermal (#16), Data Transfer List (#52 A\u2192B\u21920\u21921)",
        5: "Valve List (A\u2192D+CCS), Grounding (#27 B\u2192C\u2192D\u2192E), Instrument List (#32 A\u2192B\u2192C\u2192D\u2192E), Power Works (#50 A\u2192B\u21920\u2192C\u21920)",
        6: "IO List (#31, A\u2192B\u2192C\u21920\u21921\u21922)",
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

    # --- TM N15-N20 Closures ---
    ws.cell(row=row, column=1, value="OBSERVATIONS CLOSED IN TM N15-N20 (inherited inventory per TM N19/N20 Section 3)").font = FONT_SECTION
    row += 1

    closures = [
        "TM N2 OBS-02 (180+ days): A/C Thermal Calc Rev C consolidates all container loads \u2014 resolved at TM N15",
        "TM N3 OBS-01/02/03: Instrument Location Layout Rev C aligned \u2014 resolved at TM N15",
        "TM N5 OBS-03/04/05: Equipment Layout Rev B (doors, emergency exit, lateral sliding) \u2014 resolved at TM N15",
        "TM N11 OBS-04: Instrument Location Layout Rev C aligned \u2014 resolved at TM N15",
        "WITHDRAWN TM N5 OBS-01 / TM N7 OBS-01: 3,500 mm footprint constraint \u2014 superseded by P22-DWG-06-006-101",
        "INCORPORATED TM N7 OBS-03/04: equipment access door + cabinet integration (Piping Layout NOTE-06/07 for Rev 0)",
        "TM N16: no closures (single-document submittal, NOTE-01 tracked for IFC Rev 0)",
        "TM N17: no closures of inherited observations \u2014 11 prior obs remained OPEN at that date",
        "TM N18: 4 closures \u2014 TM N12 NOTE-01 + NOTE-02 (Line List Rev C); TM N15 NOTE-02 (A/C Thermal Calc Rev C); TM N13 NOTE-01 (P&ID Rev D, CIP Tank capacity). Residuals re-tracked in Section 3 (PSV-09-002 / CIT-09-004 / AC margin / TM N16 NOTE-01)",
        "TM N19 (~14 historic closures): TM N4 OBS-06/07 + TM N15 OBS-04..08 \u2014 Cable Tray Rev C closes the LONGEST-OPEN INHERITANCE (110 days); TM N3 OBS-01/03/04/05 I/O List items (Rev 1, partial on VFD vars); TM N3 OBS-01 RO Cartridge flow rate (Rev D, 22 cartridges 2.23 m3/h); TM N17 PQP OBS-01/02 CRITICALs + OBS-04 (Rev B \u2014 40% milestone prerequisite); TM N17 ITP OBS-01/02/03 (Rev B; ASME X scope new finding); TM N17 Power Works NOTE-01..04 (Rev C); TM N17 I/O NOTE-01/02/03 (Rev 1, partial)",
        "TM N20: TM N14 NOTE-02 analyser voltage 24 VDC (~96 days, I/O List Rev 2); TM N15 OBS-01/02 LCP Datasheet (Rev B; OBS-03 partial); TM N17 Instrument List OBS-01 + NOTE-01/02/03 (Rev E); TM N17 Data Transfer List NOTE-01/02 (Rev 1); TM N17 Pressure Transmitter OBS-01 + NOTE-01 (Rev C); TM N17 A&I OBS-01/02/03 + NOTE-01 (Rev B; NOTE-02 not applied \u2014 now OBS-02); TM N19 electrical package FULLY CLOSED at IFC Rev 0 (PCS OBS-01, SLD OBS-01+NOTE-01, Typical NOTE-01); TM N19 I/O OBS-01 + NOTE-01/02 (Rev 2); TM N19 ICCS 4 items (Rev 1 \u2014 new defects raised)",
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
        ("TM NX",         "ADASA Transmittal number X (N1 through N20 — TM N5 issued in Rev 0 and Rev 1)"),
        ("EX",            "BW Water delivery number X (E1 through E47, 47 deliveries as of 09-Jun-2026)"),
        ("25007-XXXX",    "BW Water submittal form number (25007-0001 through 25007-0047)"),
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
        ("NOT DELIVERED",       "Document not submitted as of 10-Jun-2026"),
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
            value="P22-IT-06-000-002-0 | Date: 11-Jun-2026 | Prepared by: Luis Rivera | Updated: TM N21 (11-Jun-2026, E48, submittal 25007-0048, 2 docs: 1 Code 1 + 1 Code 3; Grounding Layout Rev F approved (issue at Rev 0), grounding schedule embedded closing TM N11 OBS-03 ~88d; Datasheet of PLC and HMI Panel Component Rev B to be revised: no HART acquisition path vs ET 4-20mA+HART + 5069-IY4 RTD reconciliation) + TM N19 (25-May-2026, E42-E45, 13 docs: 3 Code 1 + 5 Code 2 + 5 Code 3; NT-001 issued in parallel; Cable Tray Rev C closes longest-open inheritance 110 days; PQP Rev B closes 40% milestone CRITICALs) + TM N20 (10-Jun-2026, E46 28-May + E47 09-Jun, 20 docs: 8 Code 1 + 7 Code 2 + 5 Code 3; TM N19 electrical package fully closed at IFC Rev 0; drivers: PLC-LCP Outline enclosure contradiction = fabrication gate, Control Philosophy Rev D 4th consecutive cycle with 14-day window expired 08-Jun reverting the I/O List to Code 3, NDE Plan silent on RO vessel test scope). Project Schedule Rev A adopted as recovery baseline with reservations (letter 09-Jun). Cartridge Filters pending NT-001 (due 15-Jun). Prior: TM N16/N17/N18 + ET cross-check 07-May (#90-97).").font = FONT_NORMAL


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
    print(f"  Hoja 1 - Master Register: {len(DATA_MASTER)} items ({delivered} delivered, {not_del} pending) + ET cross-check items 94-97")
    print(f"  Hoja 2 - Revision History: {len(REVISION_HISTORY)} entries ({items_in_history} documents tracked)")
    print(f"  Hoja 3 - Summary: metricas calculadas")
    print(f"  Hoja 4 - Legend: actualizada TM N21 / E48 / 11-Jun-2026")


if __name__ == "__main__":
    generar_excel()
