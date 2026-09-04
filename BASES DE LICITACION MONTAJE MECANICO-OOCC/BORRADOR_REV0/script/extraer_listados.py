"""Extrae LI Instrumentos area 06 y LI Lineas con codigo isometria, genera .md."""
import openpyxl
import os

BASE = r"C:\SynologyDrive\SynologyDrive\DESAROLLO PROYECTOS CLAUDE\MODULO DE SALMUERA TALTAL"
COMPILADO = os.path.join(BASE, "INGENIERIA DE DETALLE MECANICA", "ENTREGAS", "COMPILADO REV 0")
OUT = os.path.join(BASE, "BASES DE LICITACION MONTAJE MECANICO-OOCC", "BORRADOR_REV0", "tablas")

INSTR = os.path.join(COMPILADO, "01_PROCESOS_E_INSTRUMENTACION", "P22-LI-06-008-101-0 (LI Instrumentos).xlsx")
LINES = os.path.join(COMPILADO, "03_CANERIAS", "P22-LI-06-006-101-0 (LI Líneas).xlsx")

def read_table(path, sheet="Listado", header_row=11):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[sheet]
    headers = [str(ws.cell(header_row, c).value or "").strip().replace("\n", " ")
               for c in range(1, ws.max_column + 1)]
    headers = [h for h in headers if h]
    n_cols = len(headers)
    rows = []
    for r in range(header_row + 1, ws.max_row + 1):
        row = [ws.cell(r, c).value for c in range(1, n_cols + 1)]
        if all(v in (None, "") for v in row):
            continue
        rows.append(row)
    return headers, rows

# ---------------- LI INSTRUMENTOS ----------------
print("Procesando LI Instrumentos...")
h_i, rows_i = read_table(INSTR)
print(f"  Headers: {h_i}")
print(f"  Filas con datos: {len(rows_i)}")
# Filtrar por TAG con prefijo "06-" (area 06)
tag_idx = h_i.index("TAG")
area06 = [r for r in rows_i if r[tag_idx] and "06-" in str(r[tag_idx])]
print(f"  Filas area 06: {len(area06)}")

with open(os.path.join(OUT, "instrumentos_inline.md"), "w", encoding="utf-8") as f:
    f.write("# Instrumentacion in-line - Area 06 (Suministro ADASA / Instalacion Contratista)\n\n")
    f.write("Fuente: P22-LI-06-008-101-0 (LI Instrumentos), filtro TAG prefijo '06-'.\n\n")
    f.write(f"Total instrumentos area 06: **{len(area06)}**\n\n")
    f.write("| TAG | Tipo | Aplicacion / Servicio | P&ID | Rango | Hoja de Datos |\n")
    f.write("|-----|------|----------------------|------|-------|---------------|\n")
    cols = {h: i for i, h in enumerate(h_i)}
    for r in area06:
        tag = str(r[cols["TAG"]] or "").strip()
        tipo = str(r[cols["TIPO INSTRUMENTO"]] or "").strip()
        apli = str(r[cols.get("APLICACI N", cols.get("APLICACIN", -1))] or "").strip() if "APLICACI" in " ".join(cols.keys()) else ""
        # buscar columna que empiece con APLI
        for key in cols:
            if key.startswith("APLI"):
                apli = str(r[cols[key]] or "").strip()
                break
        pid = ""
        for key in cols:
            if "PID" in key.upper() or "P&ID" in key.upper():
                pid = str(r[cols[key]] or "").strip()
                break
        rango = str(r[cols.get("RANGO", -1)] or "").strip() if "RANGO" in cols else ""
        hd = ""
        for key in cols:
            if "HOJA" in key.upper():
                hd = str(r[cols[key]] or "").strip()
                break
        f.write(f"| {tag} | {tipo} | {apli} | {pid} | {rango} | {hd} |\n")
    f.write("\n**Scope contratista:** instalacion fisica in-line + amarre electrico hasta caja de paso.\n")
    f.write("**Fuera de scope:** calibracion, sintonia de lazo, commissioning.\n")
print(f"  -> instrumentos_inline.md OK")

# ---------------- LI LINEAS ----------------
print("\nProcesando LI Lineas...")
h_l, rows_l = read_table(LINES)
print(f"  Headers: {h_l}")
print(f"  Filas con datos: {len(rows_l)}")

# Agrupar por isometria
cols_l = {h: i for i, h in enumerate(h_l)}
iso_col = None
for key in cols_l:
    if "ISO" in key.upper() or "PLANO" in key.upper():
        iso_col = cols_l[key]
        break
print(f"  Col isometria: {iso_col} ({h_l[iso_col] if iso_col is not None else 'NO ENCONTRADA'})")

from collections import OrderedDict
iso_groups = OrderedDict()
for r in rows_l:
    iso = str(r[iso_col] or "SIN ISOMETRIA").strip()
    iso_groups.setdefault(iso, []).append(r)

with open(os.path.join(OUT, "oferta_economica_piping.md"), "w", encoding="utf-8") as f:
    f.write("# Anexo A9 - Itemizado Oferta Economica - Partida Piping\n\n")
    f.write("Fuente: P22-LI-06-006-101-0 (LI Lineas). Cotizacion por isometria.\n\n")
    f.write(f"Total isometrias identificadas: **{len(iso_groups)}** que cubren **{len(rows_l)}** lineas.\n\n")
    f.write("| Item | Codigo Isometria | Linea | Inicio | Termino | P&ID | Fluido | Espec Piping |\n")
    f.write("|------|-------------------|-------|--------|---------|------|--------|--------------|\n")
    item = 1
    for iso, lines in iso_groups.items():
        for r in lines:
            linea = str(r[cols_l.get("N de l nea", -1)] or "").strip() if "N de l nea" in cols_l else ""
            for key in cols_l:
                if "l" in key.lower() and "nea" in key.lower():
                    linea = str(r[cols_l[key]] or "").strip()
                    break
            inicio = str(r[cols_l.get("Inicio", -1)] or "").strip() if "Inicio" in cols_l else ""
            termino = str(r[cols_l.get("T rmino", -1)] or "").strip() if "T rmino" in cols_l else ""
            for key in cols_l:
                if "rmino" in key:
                    termino = str(r[cols_l[key]] or "").strip()
                    break
            pid = str(r[cols_l.get("P&ID", -1)] or "").strip() if "P&ID" in cols_l else ""
            fluido = ""
            for key in cols_l:
                if "lu" in key.lower() and "do" in key.lower():
                    fluido = str(r[cols_l[key]] or "").strip()
                    break
            espec = ""
            for key in cols_l:
                if "Espec" in key:
                    espec = str(r[cols_l[key]] or "").strip()
                    break
            f.write(f"| {item} | {iso} | {linea} | {inicio} | {termino} | {pid} | {fluido} | {espec} |\n")
            item += 1
    f.write("\n**Precio unitario por isometria** debe contemplar: suministro HDPE + accesorios + electrofusion + ensayo hidrostatico + flushing + protocolo.\n")
    f.write("Valvulas e instrumentos en items separados: 'Instalacion de valvula suministrada por ADASA' / 'Instalacion de instrumento suministrado por ADASA' (precio unitario por TAG).\n")
print(f"  -> oferta_economica_piping.md OK")
print("\nListo.")
