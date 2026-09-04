"""
Comentarios ADASA sobre P22-LI-06-006-103-B
Listado de Valvulas — Rev B

Observacion:
  Incluir junta de expansion en succion BH-06-001 (linea SA-HDPE-DN110-PN10-004)
"""

import os
import shutil
import openpyxl
from openpyxl.comments import Comment

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

XLSX_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-LI-06-006-103-B (LI Valvulas)_CC_ADASA.xlsx")

# Copiar fuente
src = os.path.normpath(os.path.join(SCRIPT_DIR, "..",
    "P22-LI-06-006-103-B (LI Válvulas).xlsx"))
if os.path.exists(src):
    shutil.copy2(src, XLSX_LOCAL)
else:
    print(f"ERROR: No se encontro {src}")
    exit(1)

wb = openpyxl.load_workbook(XLSX_LOCAL)

# Buscar la hoja con el listado de valvulas
ws = None
for sn in wb.sheetnames:
    if "Listado" in sn or "Valv" in sn:
        ws = wb[sn]
        break

if ws is None:
    print("ERROR: No se encontro hoja de listado")
    exit(1)

print(f"Hoja: {ws.title}")

# Buscar celda con SA-HDPE-DN110-PN10-004 (linea succion bomba)
# o VM-06-004 (valvula en esa linea)
count = 0
for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
    for cell in row:
        val = str(cell.value).strip() if cell.value else ""

        if val == "VM-06-001":
            cell.comment = Comment(
                "Incluir valvula adicional para dejar\n"
                "aislado el sistema.",
                "ADASA - Luis Rivera",
                width=300,
                height=60,
            )
            count += 1
            print(f"  Comentario en {cell.coordinate} ({val})")

if count > 0:
    wb.save(XLSX_LOCAL)
    print(f"\n{count} comentario(s) agregado(s). Guardado: {XLSX_LOCAL}")
else:
    print("ADVERTENCIA: No se encontro VM-06-001. Agregando comentario en header.")
    header_cell = ws.cell(row=11, column=9)
    header_cell.comment = Comment(
        "Incluir valvula adicional para dejar\n"
        "aislado el sistema.",
        "ADASA - Luis Rivera",
        width=300,
        height=60,
    )
    wb.save(XLSX_LOCAL)
    print(f"  Comentario agregado en header ({header_cell.coordinate})")
    print(f"Guardado: {XLSX_LOCAL}")
