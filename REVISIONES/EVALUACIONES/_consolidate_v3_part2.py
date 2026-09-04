# -*- coding: utf-8 -*-
"""Continue consolidation - fix SECTIONS + Legend anchors that use real em-dash."""
import io

PATH = "generar_excel_registro_v3.py"
with io.open(PATH, "r", encoding="utf-8") as f:
    src = f.read()

EM = "—"  # real em-dash character

# -----------------------------------------------------------------------
# 8) Update SECTIONS[0] to remove IDs 60, 61, 69, 74
# -----------------------------------------------------------------------
old_sections = (
    '    ("1. ENGINEERING ' + EM + ' ET Chapter 7 (90 days from NTP) + ET Chapter 5",\n'
    '     list(range(1, 76)) + [81, 82, 83]),'
)
new_sections = (
    '    ("1. ENGINEERING ' + EM + ' ET Chapter 7 (90 days from NTP) + ET Chapter 5",\n'
    '     [i for i in list(range(1, 76)) + [81, 82, 83] if i not in (60, 61, 69, 74)]),'
)
assert old_sections in src, "SECTIONS block not found (retry)"
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
    '        ("ETE Seccion 7 p.28 \'Listado de entregables\'", "Controlled by ADASA via this Master Register (P22-IT-06-000-002). Former item #69 removed ' + EM + ' not required from BW Water."),\n'
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
assert old_legend in src, "Legend anchor not found (retry)"
src = src.replace(old_legend, new_legend)

# -----------------------------------------------------------------------
# 10) Footer update (em-dash version)
# -----------------------------------------------------------------------
old_footer = (
    'P22-IT-06-000-002-0 | Date: 23-Apr-2026 | Prepared by: Luis Rivera | Updated: TM N15 (E33) + ET cross-check + section grouping ' + EM + ' 23-Apr-2026'
)
new_footer = (
    'P22-IT-06-000-002-0 | Date: 23-Apr-2026 | Prepared by: Luis Rivera | Updated: TM N15 (E33) + ET cross-check + section grouping + consolidation ' + EM + ' 23-Apr-2026'
)
assert old_footer in src, "Footer not found (retry)"
src = src.replace(old_footer, new_footer)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(src)

print("Part 2 applied: SECTIONS + Legend consolidation block + footer")
