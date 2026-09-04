"""
Consolidates redundant items in v3 register:
  - Delete #60 (General Layouts), #61 (Arrangement Drawings),
           #69 (Detailed Deliverables List), #74 (MCC Datasheet)
  - Append coverage notes to #40, #81, #82
  - Remove those IDs from SECTIONS[0]
  - Update Legend
"""
import io, re

PATH = "generar_excel_registro_v3.py"
with io.open(PATH, "r", encoding="utf-8") as f:
    src = f.read()

# -----------------------------------------------------------------------
# 1) Append coverage note to #40 Piping Layout
# -----------------------------------------------------------------------
old_40 = (
    '    # UPDATED TM N15: Rev A->B, E14->E32, N7->N15, 3-TBR->2-AN (3500mm WITHDRAWN)\n'
    '    (40, "Piping Layout",\n'
    '         "P22-DWG-09-005-004", "B", "E32", "N15", "2-AN", "Delivered",\n'
    '         "Rev B approved as noted (TM N15). 3,500 mm CIP/dosing footprint constraint (TM N5 OBS-01 / TM N7 OBS-01) WITHDRAWN by ADASA \\u2014 superseded by P22-DWG-06-006-101. NOTE-06 equipment access door / lateral sliding door not represented; NOTE-07 cabinet integration unclear (LCP routing); NOTE-08 antiscalant/CIP module-boundary flanges to confirm; NOTE-09 tie-in elevation view missing \\u2014 all to incorporate in Rev 0.",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
new_40 = (
    '    # UPDATED TM N15: Rev A->B, E14->E32, N7->N15, 3-TBR->2-AN (3500mm WITHDRAWN)\n'
    '    # Consolidation note: covers former items #60, #61 (bucket placeholders removed)\n'
    '    (40, "Piping Layout",\n'
    '         "P22-DWG-09-005-004", "B", "E32", "N15", "2-AN", "Delivered",\n'
    '         "Rev B approved as noted (TM N15). 3,500 mm CIP/dosing footprint constraint (TM N5 OBS-01 / TM N7 OBS-01) WITHDRAWN by ADASA \\u2014 superseded by P22-DWG-06-006-101. NOTE-06 equipment access door / lateral sliding door not represented; NOTE-07 cabinet integration unclear (LCP routing); NOTE-08 antiscalant/CIP module-boundary flanges to confirm; NOTE-09 tie-in elevation view missing \\u2014 all to incorporate in Rev 0. | Covers ETE Seccion 7 p.28 \'Planos de arreglo de equipos y canerias en planta y elevacion\' (piping scope).",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
assert old_40 in src, "Item 40 block not found"
src = src.replace(old_40, new_40)

# -----------------------------------------------------------------------
# 2) Append coverage note to #81 LCP Datasheet
# -----------------------------------------------------------------------
old_81 = (
    '    (81, "Datasheet Local Control Panel (LCP)",\n'
    '         "P22-ET-09-007-005", "A", "E31", "N15", "3-To be revised", "Delivered",\n'
    '         "Rev B required (TM N15). First revision. Panel-level header not populated preventing validation against Control System Architecture Rev D. OBS-01 (MAJOR): I/O module configuration and motor RTD channel count not declared (8 Pt-100 channels required per Instrument List Rev C). OBS-02 (MAJOR): panel IP rating and ambient class not declared (IP54 minimum expected). OBS-03 (MINOR): power consumption inconsistency (Load List Rev A 1.0 kW vs AC Thermal Calc Rev C 0.14 kW).",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
new_81 = (
    '    # Consolidation note: covers former item #74 MCC Datasheet (removed) \n'
    '    (81, "Datasheet Local Control Panel (LCP)",\n'
    '         "P22-ET-09-007-005", "A", "E31", "N15", "3-To be revised", "Delivered",\n'
    '         "Rev B required (TM N15). First revision. Panel-level header not populated preventing validation against Control System Architecture Rev D. OBS-01 (MAJOR): I/O module configuration and motor RTD channel count not declared (8 Pt-100 channels required per Instrument List Rev C). OBS-02 (MAJOR): panel IP rating and ambient class not declared (IP54 minimum expected). OBS-03 (MINOR): power consumption inconsistency (Load List Rev A 1.0 kW vs AC Thermal Calc Rev C 0.14 kW). | Covers ETE Seccion 5.4 combined panel per vendor catalogs in Rev A: PLC/RIO/LCP enclosure (nVent Hoffman FS66S IP66 316L) + VFDs (ABB ACS580) + MCCBs (ABB XT1N/XT3N/XT5N). No separate MCC Datasheet required.",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
assert old_81 in src, "Item 81 block not found"
src = src.replace(old_81, new_81)

# -----------------------------------------------------------------------
# 3) Append coverage note to #82 Equipment Layout
# -----------------------------------------------------------------------
old_82 = (
    '    (82, "Equipment Layout",\n'
    '         "P22-DWG-09-005-003", "B", "E32", "N15", "2-AN", "Delivered",\n'
    '         "Rev B approved as noted (TM N15). Container 40 ft within ET envelope. 16-item equipment list consistent with P&ID Rev C. Section views confirm doors (pedestrian, equipment access, emergency, lateral sliding). Closes TM N5 OBS-03/04/05. NOTE-04 (MAJOR): Operating Weight table to embed in Rev 0 (IFC); BW Water Civil Loading drawing committed for 23-Apr-2026 and accepted as separate supporting deliverable. TM N5 OBS-01/02 partially open (CIP numbering, imperial dimensions).",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
new_82 = (
    '    # Consolidation note: covers former items #60 (General Layouts) and #61 (Arrangement Drawings) - bucket placeholders removed\n'
    '    (82, "Equipment Layout",\n'
    '         "P22-DWG-09-005-003", "B", "E32", "N15", "2-AN", "Delivered",\n'
    '         "Rev B approved as noted (TM N15). Container 40 ft within ET envelope. 16-item equipment list consistent with P&ID Rev C. Section views confirm doors (pedestrian, equipment access, emergency, lateral sliding). Closes TM N5 OBS-03/04/05. NOTE-04 (MAJOR): Operating Weight table to embed in Rev 0 (IFC); BW Water Civil Loading drawing committed for 23-Apr-2026 and accepted as separate supporting deliverable. TM N5 OBS-01/02 partially open (CIP numbering, imperial dimensions). | Covers ETE Seccion 7 p.27 \'Layouts\' (general module arrangement) and p.28 \'Planos de arreglo de equipos y canerias en planta y elevacion\' (equipment scope).",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),'
)
assert old_82 in src, "Item 82 block not found"
src = src.replace(old_82, new_82)

# -----------------------------------------------------------------------
# 4) Delete item #60
# -----------------------------------------------------------------------
old_60 = (
    '    # UPDATED TM N15: Equipment Layout Rev B and GA SWRO Skid Rev A formally delivered (see items 82, 83)\n'
    '    (60, "General Layouts (Equipment, GA)",\n'
    '         "ET Sec 7, p.27", "--", "--", "--", "--", "Covered",\n'
    '         "Covered by individual tracked items: Equipment Layout Rev B (item 82, 2-AN TM N15), GA SWRO Skid Rev A (item 83, 2-AN TM N15), GA Feed/Interstage Turbochargers Rev B (items 54/55, 1-Approved TM N10), GA CIP/Antiscalant Pumps (items 56/57). GA Antiscalant Dosing Tank Rev B still pending (item 53, TM N10 OBS-05 open).",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),\n\n'
)
assert old_60 in src, "Item 60 block not found"
src = src.replace(old_60, "")

# -----------------------------------------------------------------------
# 5) Delete item #61
# -----------------------------------------------------------------------
old_61 = (
    '    (61, "Equipment/Piping Arrangement Drawings",\n'
    '         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",\n'
    '         "Blocks civil design, piping procurement",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),\n\n'
)
assert old_61 in src, "Item 61 block not found"
src = src.replace(old_61, "")

# -----------------------------------------------------------------------
# 6) Delete item #69
# -----------------------------------------------------------------------
old_69 = (
    '    (69, "Detailed Deliverables List",\n'
    '         "ET Sec 7, p.28", "--", "--", "--", "--", "NOT DELIVERED",\n'
    '         "Cannot verify scope compliance",\n'
    '         "ET Sec.7: Max. 90 days from NTP"),\n\n'
)
assert old_69 in src, "Item 69 block not found"
src = src.replace(old_69, "")

# -----------------------------------------------------------------------
# 7) Delete item #74
# -----------------------------------------------------------------------
old_74 = (
    '    (74, "MCC Datasheet",\n'
    '         "ET 5.4", "--", "--", "--", "--", "NOT DELIVERED",\n'
    '         "MCC reportedly in fabrication without DS",\n'
    '         "ET Sec.5.4: Max. 90 days from NTP"),\n\n'
)
assert old_74 in src, "Item 74 block not found"
src = src.replace(old_74, "")

# -----------------------------------------------------------------------
# 8) Update SECTIONS[0] to remove IDs 60, 61, 69, 74
# -----------------------------------------------------------------------
old_sections = (
    '    ("1. ENGINEERING \\u2014 ET Chapter 7 (90 days from NTP) + ET Chapter 5",\n'
    '     list(range(1, 76)) + [81, 82, 83]),'
)
new_sections = (
    '    ("1. ENGINEERING \\u2014 ET Chapter 7 (90 days from NTP) + ET Chapter 5",\n'
    '     [i for i in list(range(1, 76)) + [81, 82, 83] if i not in (60, 61, 69, 74)]),'
)
assert old_sections in src, "SECTIONS block not found"
src = src.replace(old_sections, new_sections)

# -----------------------------------------------------------------------
# 9) Add consolidation block to Legend
# -----------------------------------------------------------------------
old_legend = (
    '    row += 2\n'
    '    ws.cell(row=row, column=1, value="MASTER REGISTER SECTIONS").font = legend_section\n'
)
new_legend = (
    '    row += 2\n'
    '    ws.cell(row=row, column=1, value="DELIVERABLES CONSOLIDATED / ADASA-CONTROLLED").font = legend_section\n'
    '    row += 1\n'
    '    consolidated = [\n'
    '        ("ETE Seccion 7 p.27 \'Layouts\'", "Covered by items #40 (Piping Layout), #41 (Tie-In), #82 (Equipment Layout). Former bucket item #60 removed."),\n'
    '        ("ETE Seccion 7 p.28 \'Planos de arreglo\'", "Covered by items #40 + #82 (plan + elevation views). Former bucket item #61 removed."),\n'
    '        ("ETE Seccion 5.4 MCC Datasheet", "Covered by item #81 LCP Datasheet Rev A (combined panel per ETE Seccion 5.4). Former item #74 removed."),\n'
    '        ("ETE Seccion 7 p.28 \'Listado de entregables\'", "Controlled by ADASA via this Master Register (P22-IT-06-000-002). Former item #69 removed \\u2014 not required from BW Water."),\n'
    '    ]\n'
    '    for term, desc in consolidated:\n'
    '        c1 = ws.cell(row=row, column=1, value=term)\n'
    '        c1.font = FONT_BOLD\n'
    '        c2 = ws.cell(row=row, column=2, value=desc)\n'
    '        c2.font = FONT_NORMAL\n'
    '        row += 1\n'
    '\n'
    '    row += 2\n'
    '    ws.cell(row=row, column=1, value="MASTER REGISTER SECTIONS").font = legend_section\n'
)
assert old_legend in src, "Legend anchor not found"
src = src.replace(old_legend, new_legend)

# -----------------------------------------------------------------------
# 10) Update footer date marker
# -----------------------------------------------------------------------
old_footer = (
    'P22-IT-06-000-002-0 | Date: 23-Apr-2026 | Prepared by: Luis Rivera | Updated: TM N15 (E33) + ET cross-check + section grouping \\u2014 23-Apr-2026'
)
new_footer = (
    'P22-IT-06-000-002-0 | Date: 23-Apr-2026 | Prepared by: Luis Rivera | Updated: TM N15 (E33) + ET cross-check + section grouping + consolidation \\u2014 23-Apr-2026'
)
assert old_footer in src, "Footer not found"
src = src.replace(old_footer, new_footer)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(src)

print("Consolidation applied: items 60, 61, 69, 74 removed; coverage notes appended.")
