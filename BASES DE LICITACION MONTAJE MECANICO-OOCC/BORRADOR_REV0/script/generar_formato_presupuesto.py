"""
Genera Formato de Presupuesto_RevB.xlsx para las BL Montaje Mecanico + OOCC
del proyecto BAE 12803 Taltal SWRO.

Mantiene exactamente la estructura visual de Rev 0 (6 columnas, estilos, paleta)
y reemplaza los placeholders por TAGs y descripciones reales extraidas de:
  - P22-LI-06-006-001 Listado de Lineas (13 lineas HDPE)
  - P22-LI-06-006-002 Listado de Valvulas (mapeo valvulas in-line)
  - P22-LI-06-005-001 Listado de Equipos (TK-06-001, TK-06-004, BH-06-001)
  - P22-DWG-06-006-107 Rev 0 Cuadernillo de Soportes (11 tipos SP-XX, 67 unidades)
  - Memorias OOCC L&A P22-MC-00-002-001/002/004/005 (fundaciones)

Rev B (28-May-2026): amplia el Cap. 1 con 11 sub-partidas de soportes HDPE
(SP-01 a SP-11 con CANT del cuadernillo) y el Cap. 4 con 3 sub-partidas extra
de obras civiles (4.6 excavacion, 4.7 relleno+base, 4.8 sistema drenaje).

Restricciones:
  - 6 columnas EXACTAS (ITEM | PARTIDA | UNID. | CANT. | P.UNI. | TOTAL).
  - No agregar capitulos nuevos (4 capitulos del Rev 0).
  - Capitulo 4 (Obras Civiles) con CANT y P.UNI vacios excepto 4.8 (CANT=1 gl).
  - Sin notas en cursiva entre titulo de capitulo y sub-items.
  - Idempotente: cada corrida regenera el archivo.
"""

from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, Color
from openpyxl.utils import get_column_letter

# ---------- Rutas ----------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "Formato de Presupuesto_RevB.xlsx"

# ---------- Paleta y fuentes (extraidas del Rev 0) ----------
FONT_NAME = "Aptos Narrow"

# Banda de capitulo: theme=0 (Background/Light1) con tint -0.35 → gris oscuro
FILL_CAPITULO = PatternFill(
    fill_type="solid",
    start_color=Color(theme=0, tint=-0.3499862666707358),
    end_color=Color(theme=0, tint=-0.3499862666707358),
)

# Totalizadores principales (Costo Directo, Total General): theme=2 tint -0.25
FILL_TOTAL_PRINCIPAL = PatternFill(
    fill_type="solid",
    start_color=Color(theme=2, tint=-0.249977111117893),
    end_color=Color(theme=2, tint=-0.249977111117893),
)

# Sin fill (titulo, header fila 4, sub-items, GG/Util/IVA): patternType None
FILL_NONE = PatternFill(fill_type=None)

# Bordes
BORDER_MEDIUM_ALL = Border(
    top=Side(style="medium"), bottom=Side(style="medium"),
    left=Side(style="medium"), right=Side(style="medium"),
)
BORDER_THIN_ALL = Border(
    top=Side(style="thin"), bottom=Side(style="thin"),
    left=Side(style="thin"), right=Side(style="thin"),
)


def border_capitulo(col):
    """Bordes de fila de capitulo: medium top/bottom, sides solo en A y F."""
    if col == "A":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                      left=Side(style="medium"))
    if col == "F":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                      right=Side(style="medium"))
    return Border(top=Side(style="medium"), bottom=Side(style="medium"))


def border_header_fila4(col):
    """Bordes header fila 4 reproducen Rev 0: medium top/bottom, sides en A y F."""
    if col == "A":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                      left=Side(style="medium"), right=Side(style="thin"))
    if col == "F":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                      left=Side(style="thin"), right=Side(style="medium"))
    return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                  left=Side(style="thin"), right=Side(style="thin"))


def border_total_principal(col):
    if col == "A":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"))
    if col == "F":
        return Border(top=Side(style="medium"), bottom=Side(style="medium"),
                      right=Side(style="medium"))
    return Border(top=Side(style="medium"), bottom=Side(style="medium"))


# Formato de moneda usado en Rev 0
FMT_MONEDA_SUBITEM = '"$"\\ #,##0;[Red]\\-"$"\\ #,##0'
FMT_MONEDA_TOTAL = '_ "$"* #,##0_ ;_ "$"* \\-#,##0_ ;_ "$"* "-"_ ;_ @_ '


# ---------- Datos: 13 lineas HDPE (orden de presentacion) ----------
# Fuente: P22-LI-06-006-001 Listado de Lineas + P22-LI-06-006-002 Listado de Valvulas.
LINEAS_HDPE = [
    # (n, tag, servicio, valvulas_inline)
    ("1.1",  "SA-HDPE-DN110-PN10-001", "Salmuera mod. 11 l/s tie-in 3 -> SA-DN90-001",       "VM-06-001"),
    ("1.2",  "SA-HDPE-DN110-PN10-002", "Salmuera SA-001 -> TK-06-001 (entrada estanque)",     "VM-06-002"),
    ("1.3",  "SA-HDPE-DN110-PN10-003", "Salmuera TK-06-001 -> Fosa de Drenajes",              ""),
    ("1.4",  "SA-HDPE-DN63-PN10-001",  "Salmuera TK-06-001 -> Fosa de Drenajes (paralela)",   "VM-06-003"),
    ("1.5",  "SA-HDPE-DN110-PN10-004", "Salmuera TK-06-001 -> BH-06-001 (succion)",           "VM-06-004"),
    ("1.6",  "SA-HDPE-DN110-PN10-005", "Salmuera BH-06-001 -> tie-in 1 mod. 2da etapa",       "VM-06-005, VR-06-001"),
    ("1.7",  "SA-HDPE-DN110-PN10-006", "Salmuera BS-06-001 -> SA-007 (descarga sumergible)",  "VM-06-008, VR-06-002"),
    ("1.8",  "SA-HDPE-DN110-PN10-007", "Salmuera SA-DN90-002 -> drenaje original 11 l/s",     "VM-06-009, VR-06-003"),
    ("1.9",  "SA-HDPE-DN90-PN10-002",  "Salmuera tie-in 3 mod. 2da etapa -> SA-007",          ""),
    ("1.10", "SA-HDPE-DN90-PN10-003",  "Drenajes tie-in 4 mod. 2da etapa -> canaleta",        ""),
    ("1.11", "PE-HDPE-DN90-PN10-001",  "Permeado tie-in 2 mod. 2da etapa -> TK Producto N1/2","VM-06-007, VM-06-015"),
    ("1.12", "PE-HDPE-DN90-PN10-002",  "Permeado PE-001 -> Disolvedor de CO2",                "VM-06-016"),
    ("1.13", "PE-HDPE-DN90-PN10-003",  "Permeado fuera de spec. PE-001 -> SA-007",            "VM-06-006"),
]

# ---------- Datos: equipos cap. 2 y 3 ----------
# Fuente: P22-LI-06-005-001 + hojas de datos P22-ET-06-005-001/-002.
ESTANQUE = "Montaje de estanque PRFV TK-06-001 (10 m3, ASME RTP-1, suministro ADASA)"
ESTANQUE_TRASLADO = "Traslado de Antofagasta a Taltal (TK-06-001)"

BOMBA = ("Montaje de bomba centrifuga BH-06-001 KSB + motor WEH 11 kW "
         "(incluye pruebas electricas estaticas del motor; sin comisionamiento)")
BOMBA_TRASLADO = "Traslado de Antofagasta a Taltal (BH-06-001)"

# ---------- Datos: 11 soportes cap. 1 (Rev B) ----------
# Fuente: P22-DWG-06-006-107 Rev 0 (Cuadernillo de Soportes, 21 paginas).
# CANT por tipo = suma de sub-designaciones SP-XX-NN listadas en el cuadernillo.
# Total: 67 soportes individuales en 11 tipos. Aporte ADASA, contratista monta.
SOPORTES_HDPE = [
    ("1.14", "Montaje soporte tipo SP-01 (abrazadera sobre perfil UPE 80 + chapa; SP-01-01/02/03)", 21),
    ("1.15", "Montaje soporte tipo SP-02 (soporte simple; SP-02-01/02)", 3),
    ("1.16", "Montaje soporte tipo SP-03 - extremo a soldar en soporte existente Modulo 3 (WPS calificado; SP-03-01/02/03)", 24),
    ("1.17", "Montaje soporte tipo SP-04 (pedestal perfil cuadrado 100 mm sobre dado de hormigon + grout; SP-04-01)", 3),
    ("1.18", "Montaje soporte tipo SP-05 (pedestal con riostra diagonal sobre dado de hormigon + grout; SP-05-01)", 5),
    ("1.19", "Montaje soporte tipo SP-06 (pedestal con voladizo sobre dado de hormigon + grout; SP-06-01)", 1),
    ("1.20", "Montaje soporte tipo SP-07 (pedestal con diagonal; SP-07-01/02)", 4),
    ("1.21", "Montaje soporte tipo SP-08 (pedestal individual alto DN110; SP-08-01)", 1),
    ("1.22", "Montaje soporte tipo SP-09 - soldado a soporte existente (intervencion critica; SP-09-01)", 1),
    ("1.23", "Montaje soporte tipo SP-10 - extremo a soldar en terreno (chapa en radier nuevo o anclaje quimico; SP-10-01)", 2),
    ("1.24", "Montaje soporte tipo SP-11 (pedestal con doble nivel; SP-11-01/02)", 2),
]

# ---------- Datos: 5 fundaciones cap. 4 ----------
# Mapeo F1-F5 ↔ memorias L&A P22-MC-00-002-001/002/004/005 + correccion 4.5.
# F5 cambia de "camara carga" (Rev 0 con typo) a "camara de drenajes (TK-06-004)".
FUNDACIONES = [
    ("4.1", "Fundacion planta salmuera (F1) - radier de operacion"),
    ("4.2", "Fundacion compartida contenedor RO + sistema CIP (F2)"),
    ("4.3", "Fundacion dinamica bomba BH-06-001 (F3) - segun MC ACI 351"),
    ("4.4", "Fundacion estanque TK-06-001 (F4)"),
    ("4.5", "Fundacion camara de drenajes TK-06-004 (F5)"),
]

# ---------- Datos: 3 obras civiles extra cap. 4 (Rev B) ----------
# Fuente: planos OOCC P22-DWG-06-005-104 (planta drenajes) y P22-DWG-06-005-105-B
# (montaje fosa drenajes). Memorias L&A Rev B no traen cubicaciones — CANT vacia
# en 4.6 y 4.7; 4.8 con CANT=1 (sistema integral cotizado gl por oferente).
OBRAS_CIVILES_EXTRA = [
    # (codigo, descripcion, unidad, cantidad)
    ("4.6", "Excavacion comun + retiro de material - 5 fundaciones F1-F5 + zanjas de drenaje", "m3", None),
    ("4.7", "Relleno compactado con material seleccionado + base estabilizada (sello arena/hormigon pobre) bajo losas", "m3", None),
    ("4.8", "Sistema de drenaje del modulo (canaleta perimetral + sumideros + tuberia HDPE Ø63 corrugada + camaras de inspeccion + conexion a TK-06-004)", "gl", 1),
]


# ---------- Helpers de escritura ----------
def escribir_titulo(ws):
    ws.merge_cells("A2:F2")
    c = ws["A2"]
    c.value = "PRESUPUESTO DE MONTAJE DE EQUIPOS MECANICOS Y OBRAS CIVILES PLANTA TALTAL"
    c.font = Font(name=FONT_NAME, size=11, bold=False)
    c.alignment = Alignment(horizontal="center", vertical="center")
    for col in "ABCDEF":
        ws[f"{col}2"].border = BORDER_MEDIUM_ALL


def escribir_header(ws, row=4):
    """Cabecera fila 4: ITEM | PARTIDA | UNID. | CANT. | P.UNI. | TOTAL."""
    headers = [
        ("A", "ITEM",    10, "center"),
        ("B", "PARTIDA", 10, "center"),
        ("C", "UNID.",   10, "left"),
        ("D", "CANT.",   10, "left"),
        ("E", "P.UNI.",  12, "center"),
        ("F", "TOTAL",   12, "center"),
    ]
    for col, val, size, align in headers:
        c = ws[f"{col}{row}"]
        c.value = val
        c.font = Font(name=FONT_NAME, size=size, bold=True)
        c.alignment = Alignment(horizontal=align, vertical="center")
        c.border = border_header_fila4(col)
        c.fill = FILL_NONE


def escribir_fila_capitulo(ws, row, codigo, titulo, formula_total):
    """Banda gris oscura del capitulo. Cant/PU vacios, F con formula SUM."""
    values = {"A": codigo, "B": titulo, "C": None, "D": None, "E": None, "F": formula_total}
    for col, val in values.items():
        c = ws[f"{col}{row}"]
        c.value = val
        c.font = Font(name=FONT_NAME, size=11, bold=True)
        c.fill = FILL_CAPITULO
        c.border = border_capitulo(col)
        if col == "A":
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col == "B":
            c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        elif col == "F":
            c.alignment = Alignment(horizontal="right", vertical="center")
            c.number_format = FMT_MONEDA_SUBITEM


def escribir_subitem(ws, row, codigo, partida, unidad, cantidad, p_unitario_val):
    """Sub-item con bordes finos. p_unitario_val=None deja la celda vacia."""
    c_a = ws[f"A{row}"]; c_a.value = codigo
    c_b = ws[f"B{row}"]; c_b.value = partida
    c_c = ws[f"C{row}"]; c_c.value = unidad
    c_d = ws[f"D{row}"]; c_d.value = cantidad
    c_e = ws[f"E{row}"]; c_e.value = p_unitario_val
    c_f = ws[f"F{row}"]; c_f.value = f"=E{row}*D{row}"

    for col in "ABCDEF":
        c = ws[f"{col}{row}"]
        c.font = Font(name=FONT_NAME, size=10, bold=False)
        c.border = BORDER_THIN_ALL
        c.fill = FILL_NONE

    c_a.alignment = Alignment(horizontal="center", vertical="center")
    c_b.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    c_c.alignment = Alignment(horizontal="center", vertical="center")
    c_d.alignment = Alignment(horizontal="center", vertical="center")
    c_e.alignment = Alignment(horizontal="right", vertical="center")
    c_f.alignment = Alignment(horizontal="right", vertical="center")
    c_e.number_format = FMT_MONEDA_SUBITEM
    c_f.number_format = FMT_MONEDA_SUBITEM


def escribir_totalizadores(ws, row_inicio, ref_costo_directo_formula):
    """
    Escribe 6 filas: Costo Directo, GG %, Utilidades %, Total Parcial, IVA %, Total General.
    Reemplaza los valores hardcoded a 0 del Rev 0 por formulas funcionales.
    """
    r_cd  = row_inicio
    r_gg  = row_inicio + 1
    r_ut  = row_inicio + 2
    r_tp  = row_inicio + 3
    r_iva = row_inicio + 4
    r_tg  = row_inicio + 5

    # Fila COSTO DIRECTO (banda total principal)
    for col in "ABCDEF":
        c = ws[f"{col}{r_cd}"]
        c.font = Font(name=FONT_NAME, size=11, bold=(col == "B"))
        c.fill = FILL_TOTAL_PRINCIPAL
        c.border = border_total_principal(col)
        c.alignment = Alignment(horizontal="left" if col == "B" else "right",
                                vertical="center",
                                indent=1 if col == "B" else 0)
    ws[f"B{r_cd}"].value = "COSTO DIRECTO"
    ws[f"F{r_cd}"].value = ref_costo_directo_formula
    ws[f"F{r_cd}"].number_format = FMT_MONEDA_TOTAL

    # Filas intermedias GG %, UT %, TOTAL PARCIAL, IVA %
    def fila_intermedia(r, label, formula, has_pct):
        for col in "ABCDEF":
            c = ws[f"{col}{r}"]
            c.font = Font(name=FONT_NAME, size=11, bold=(col == "B"))
            c.fill = FILL_NONE
            c.alignment = Alignment(horizontal="left" if col == "B" else "center",
                                    vertical="center",
                                    indent=1 if col == "B" else 0)
            if col in "BCDEF":
                c.border = Border(top=Side(style=None), bottom=Side(style="thin"),
                                  left=Side(style="thin"), right=Side(style="thin"))
        ws[f"B{r}"].value = label
        if has_pct:
            ws[f"C{r}"].value = "%"
            ws[f"D{r}"].value = None  # el porcentaje se ingresa aqui
            ws[f"D{r}"].alignment = Alignment(horizontal="center", vertical="center")
            ws[f"D{r}"].number_format = "0.00"
        ws[f"F{r}"].value = formula
        ws[f"F{r}"].number_format = FMT_MONEDA_TOTAL
        ws[f"F{r}"].alignment = Alignment(horizontal="right", vertical="center")

    # Las formulas usan D{row} para leer el % editable del usuario
    fila_intermedia(r_gg,  "GASTOS GENERALES", f"=F{r_cd}*D{r_gg}/100",  True)
    fila_intermedia(r_ut,  "UTILIDADES",       f"=F{r_cd}*D{r_ut}/100",  True)
    fila_intermedia(r_tp,  "TOTAL PARCIAL",    f"=F{r_cd}+F{r_gg}+F{r_ut}", False)
    fila_intermedia(r_iva, "IVA",              f"=F{r_tp}*D{r_iva}/100", True)
    # Valor por defecto IVA 19%
    ws[f"D{r_iva}"].value = 19

    # Fila TOTAL GENERAL (banda total principal)
    for col in "ABCDEF":
        c = ws[f"{col}{r_tg}"]
        c.font = Font(name=FONT_NAME, size=11, bold=(col == "B"))
        c.fill = FILL_TOTAL_PRINCIPAL
        c.border = border_total_principal(col)
        c.alignment = Alignment(horizontal="left" if col == "B" else "right",
                                vertical="center",
                                indent=1 if col == "B" else 0)
    ws[f"B{r_tg}"].value = "TOTAL GENERAL"
    ws[f"F{r_tg}"].value = f"=F{r_tp}+F{r_iva}"
    ws[f"F{r_tg}"].number_format = FMT_MONEDA_TOTAL


# ---------- Generador principal ----------
def main():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Presupuesto"

    # Anchos de columna - B se ensancha para acomodar descripcion extendida cap. 1
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 70
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 10
    ws.column_dimensions["E"].width = 15
    ws.column_dimensions["F"].width = 18

    escribir_titulo(ws)
    escribir_header(ws, row=4)

    # ---- Capitulo 1: HDPE (13 lineas + 11 soportes = 24 sub-items) ----
    row = 6
    r_cap1 = row
    row += 1
    r_cap1_inicio = row
    # Bloque 1.1-1.13: lineas HDPE
    for codigo, tag, servicio, valvulas in LINEAS_HDPE:
        partida = f"Fabricacion y montaje linea {tag} - {servicio}"
        if valvulas:
            partida += f" (incluye montaje in-line: {valvulas})"
        escribir_subitem(ws, row, codigo, partida, "gl", 1, 0)
        ws.row_dimensions[row].height = 28  # altura suficiente para wrap text
        row += 1
    # Bloque 1.14-1.24: soportes HDPE (Rev B)
    for codigo, descripcion, cantidad in SOPORTES_HDPE:
        escribir_subitem(ws, row, codigo, descripcion, "un", cantidad, 0)
        ws.row_dimensions[row].height = 28
        row += 1
    r_cap1_fin = row - 1
    escribir_fila_capitulo(
        ws, r_cap1, 1,
        "FABRICACION Y MONTAJE DE TUBERIAS DE HDPE",
        f"=SUM(F{r_cap1_inicio}:F{r_cap1_fin})",
    )

    row += 1  # fila en blanco

    # ---- Capitulo 2: Estanque PRFV ----
    r_cap2 = row
    row += 1
    r_cap2_inicio = row
    escribir_subitem(ws, row, "2.1", ESTANQUE, "un", 1, 0); row += 1
    escribir_subitem(ws, row, "2.2", ESTANQUE_TRASLADO, "un", 1, 0); row += 1
    r_cap2_fin = row - 1
    escribir_fila_capitulo(
        ws, r_cap2, 2, "MONTAJE DE ESTANQUE PRFV",
        f"=SUM(F{r_cap2_inicio}:F{r_cap2_fin})",
    )

    row += 1  # fila en blanco

    # ---- Capitulo 3: Bomba centrifuga ----
    r_cap3 = row
    row += 1
    r_cap3_inicio = row
    escribir_subitem(ws, row, "3.1", BOMBA, "un", 1, 0); row += 1
    ws.row_dimensions[row - 1].height = 30  # descripcion larga
    escribir_subitem(ws, row, "3.2", BOMBA_TRASLADO, "un", 1, 0); row += 1
    r_cap3_fin = row - 1
    escribir_fila_capitulo(
        ws, r_cap3, 3, "MONTAJE DE BOMBA CENTRIFUGA",
        f"=SUM(F{r_cap3_inicio}:F{r_cap3_fin})",
    )

    row += 1  # fila en blanco

    # ---- Capitulo 4: Obras Civiles (5 fundaciones + 3 extra = 8 sub-items) ----
    r_cap4 = row
    row += 1
    r_cap4_inicio = row
    # Bloque 4.1-4.5: fundaciones (CANT y P.UNI VACIOS)
    for codigo, descripcion in FUNDACIONES:
        escribir_subitem(ws, row, codigo, descripcion, "m3", None, None)
        row += 1
    # Bloque 4.6-4.8: excavaciones y sistema de drenaje (Rev B)
    for codigo, descripcion, unidad, cantidad in OBRAS_CIVILES_EXTRA:
        escribir_subitem(ws, row, codigo, descripcion, unidad, cantidad, None)
        ws.row_dimensions[row].height = 28
        row += 1
    r_cap4_fin = row - 1
    escribir_fila_capitulo(
        ws, r_cap4, 4, "OBRAS CIVILES",
        f"=SUM(F{r_cap4_inicio}:F{r_cap4_fin})",
    )

    row += 1  # fila en blanco

    # ---- Totalizadores ----
    formula_cd = f"=F{r_cap1}+F{r_cap2}+F{r_cap3}+F{r_cap4}"
    escribir_totalizadores(ws, row, formula_cd)

    # Freeze panes: la cabecera fila 4 queda visible al scrollear
    ws.freeze_panes = "A5"

    # Print area: A1 hasta la ultima fila escrita
    ultima_fila = row + 5
    ws.print_area = f"A1:F{ultima_fila}"
    ws.page_setup.orientation = ws.ORIENTATION_PORTRAIT
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    wb.save(OUTPUT_PATH)

    cap1_n = len(LINEAS_HDPE) + len(SOPORTES_HDPE)
    cap4_n = len(FUNDACIONES) + len(OBRAS_CIVILES_EXTRA)
    n_subitems = cap1_n + 2 + 2 + cap4_n
    soportes_cant_total = sum(c for _, _, c in SOPORTES_HDPE)
    print(f"OK: {OUTPUT_PATH.name} generado ({n_subitems} sub-items en 4 capitulos)")
    print(f"    Ruta: {OUTPUT_PATH}")
    print()
    print("Verificaciones aplicadas (Rev B):")
    print(f"  - Capitulo 1: {cap1_n} sub-items = {len(LINEAS_HDPE)} lineas HDPE + {len(SOPORTES_HDPE)} soportes")
    print(f"    * Soportes: {soportes_cant_total} unidades individuales en {len(SOPORTES_HDPE)} tipos SP-XX")
    print(f"      (cuadernillo P22-DWG-06-006-107 Rev 0)")
    print(f"  - Capitulo 2: TK-06-001 (10 m3, ADASA) + traslado")
    print(f"  - Capitulo 3: BH-06-001 + motor WEH 11 kW + traslado (sin comisionamiento)")
    print(f"  - Capitulo 4: {cap4_n} sub-items = {len(FUNDACIONES)} fundaciones + {len(OBRAS_CIVILES_EXTRA)} obras civiles extra")
    print(f"    * 4.5 corregido: 'camara carga' (Rev 0 typo) -> 'camara de drenajes TK-06-004'")
    print(f"    * 4.6/4.7 con CANT vacia (m3); 4.8 sistema de drenaje gl=1")
    print(f"  - Totalizadores con formulas reales (Rev 0 las tenia hardcoded a 0)")
    print(f"  - Default IVA = 19 % editable en celda D del IVA")


if __name__ == "__main__":
    main()
