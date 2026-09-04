"""
Genera 'Formato de Presupuesto.xlsx' para las BL Montaje Mecanico + OOCC
del proyecto BAE 12803 Taltal SWRO.

Mantiene exactamente la estructura visual de Rev 0 (6 columnas, estilos, paleta)
y reemplaza los placeholders por TAGs/descripciones reales y P.UNI. valorizados.

FUENTE DE CANTIDADES:
  - Cap. 1 HDPE: P22-LI-06-006-001/-002 (lineas + valvulas) + cuadernillo de
    soportes P22-DWG-06-006-107 Rev 0.
  - Cap. 4 Obras Civiles: cubicacion de la Estimacion de Inversion OOCC de L&A
    (P22-IT-00-010-001-0_B, hoja BASE) + planos P22-DWG-00-002-006_C (camaras)
    y P22-DWG-00-002-007_C LAM3 (fundacion de la cubierta/cobertizo CIP, 2,38 m3).

FUENTE DE PRECIOS (P.UNI.):
  - Cap. 1-3: precios de montaje vigentes del entregable Rev 0 (Bases REV 0),
    embebidos aqui para que el script vuelva a ser la fuente unica.
  - Cap. 4: NO se usa el APU de L&A (material declarado ~5-9x sobre mercado en
    hormigon, tierra y acero). Los P.UNI. se anclan a mercado del norte de Chile
    con premium logistico de Taltal (benchmark MINVU DS-27 / CYPE / ONDAC):
      * Fundaciones 4.1-4.5  = CIV directo de L&A x 0,60.
      * Mov. de tierra 4.6/4.7 = mercado + premium remoto ($22.000 / $45.000 m3).
      * Drenaje 4.8 (red) y camaras 4.9 (6 un, del plano; L&A no las costeo).
      * Cubierta metalica CIP: la estructura de acero (antigua partida 4.10 all-in por kg)
        SALE del alcance (suministro+ereccion ADASA en etapa posterior); solo permanece su
        fundacion (item 4.3, obra civil). 4.11 insertos RO embebidos = suministro + colocacion
        ($3.000/kg, sin ereccion ni C5-M).
      * Impermeabilizacion 4.12/4.13 (fosa + hormigon enterrado; gap TM N3).
    Valores [Suposicion] de drenaje/impermeabilizacion a afinar en Rev 0 OOCC.

ADVERTENCIA: el script sobreescribe 'Formato de Presupuesto.xlsx' en cada corrida.
Si el archivo tiene ediciones manuales posteriores, se perderan; respaldar antes.

Restricciones de formato:
  - 6 columnas EXACTAS (ITEM | PARTIDA | UNID. | CANT. | P.UNI. | TOTAL).
  - 4 capitulos (sin capitulos nuevos). Totalizadores: COSTO DIRECTO, GG 20%,
    UTILIDADES 10%, TOTAL GENERAL (sin IVA, igual al entregable Rev 0).
  - Sin notas en cursiva entre titulo de capitulo y sub-items (la nota al pie va
    despues de TOTAL GENERAL).
  - Idempotente: cada corrida regenera el archivo desde cero.
"""

from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, Color
from openpyxl.utils import get_column_letter

# ---------- Rutas y modo de emision ----------
# Por defecto se genera la planilla QUE VIAJA AL OFERENTE: columna P.UNI. en blanco.
# Con --valorizado se genera la copia interna de ADASA, con los precios cargados,
# que NUNCA se incorpora al paquete de licitacion.
import sys
VALORIZADO = "--valorizado" in sys.argv
INCLUIR_PUNI = VALORIZADO

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / (
    "Formato de Presupuesto_VALORIZADO.xlsx" if VALORIZADO else "Formato de Presupuesto.xlsx"
)

# ---------- Paleta y fuentes (extraidas del Rev 0) ----------
FONT_NAME = "Aptos Narrow"

# Banda de capitulo: theme=0 (Background/Light1) con tint -0.35 -> gris oscuro
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

# Sin fill (titulo, header fila 4, sub-items, GG/Util): patternType None
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


# ---------- Datos: 12 lineas HDPE (Cap. 1) ----------
# Fuente: P22-LI-06-006-001/-002. P.UNI. = precios de montaje del entregable Rev 0.
# La linea SA-HDPE-DN110-PN10-006 (BS-06-001, descarga sumergible) fue eliminada
# del entregable (drenaje por gravedad, BS-06-001 omitida en planos).
LINEAS_HDPE = [
    # (n, tag, servicio, valvulas_inline, p_unitario)
    ("1.1",  "SA-HDPE-DN110-PN10-001", "Salmuera mod. 11 l/s tie-in 3 -> SA-DN90-001",        "VM-06-001",            1450320),
    ("1.2",  "SA-HDPE-DN110-PN10-002", "Salmuera SA-001 -> TK-06-001 (entrada estanque)",      "VM-06-002",            7151837),
    ("1.3",  "SA-HDPE-DN110-PN10-003", "Salmuera TK-06-001 -> Fosa de Drenajes",               "",                     1150300),
    ("1.4",  "SA-HDPE-DN63-PN10-001",  "Salmuera TK-06-001 -> Fosa de Drenajes (paralela)",    "VM-06-003",             780520),
    ("1.5",  "SA-HDPE-DN110-PN10-004", "Salmuera TK-06-001 -> BH-06-001 (succion)",            "VM-06-004",             987530),
    ("1.6",  "SA-HDPE-DN110-PN10-005", "Salmuera BH-06-001 -> tie-in 1 mod. 2da etapa",        "VM-06-005, VR-06-001", 3427960),
    ("1.7",  "SA-HDPE-DN110-PN10-007", "Salmuera SA-DN90-002 -> drenaje original 11 l/s",      "VM-06-009, VR-06-003",19592610),
    ("1.8",  "SA-HDPE-DN90-PN10-002",  "Salmuera tie-in 3 mod. 2da etapa -> SA-007",           "",                           0),
    ("1.9",  "SA-HDPE-DN90-PN10-003",  "Drenajes tie-in 4 mod. 2da etapa -> canaleta",         "",                           0),
    ("1.10", "PE-HDPE-DN90-PN10-001",  "Permeado tie-in 2 mod. 2da etapa -> TK Producto N1/2", "VM-06-007, VM-06-015", 3280795),
    ("1.11", "PE-HDPE-DN90-PN10-002",  "Permeado PE-001 -> Disolvedor de CO2",                 "VM-06-016",                  0),
    ("1.12", "PE-HDPE-DN90-PN10-003",  "Permeado fuera de spec. PE-001 -> SA-007",             "VM-06-006",            3780620),
]

# ---------- Datos: equipos cap. 2 y 3 ----------
ESTANQUE = "Montaje de estanque PRFV TK-06-001 (10 m3, ASME RTP-1, suministro ADASA)"
ESTANQUE_PU = 7850000
ESTANQUE_TRASLADO = "Traslado de Antofagasta a Taltal (TK-06-001)"
ESTANQUE_TRASLADO_PU = 1300000

BOMBA = ("Montaje de bomba centrifuga BH-06-001 KSB + motor WEH 11 kW "
         "(incluye pruebas electricas estaticas del motor; sin comisionamiento)")
BOMBA_PU = 7890000
BOMBA_TRASLADO = "Traslado de Antofagasta a Taltal (BH-06-001)"
BOMBA_TRASLADO_PU = 1300000

# ---------- Datos: 11 soportes cap. 1 ----------
# Fuente: P22-DWG-06-006-107 Rev 0 (67 soportes en 11 tipos). P.UNI. del entregable Rev 0.
SOPORTES_HDPE = [
    # (codigo, descripcion, cantidad, p_unitario)
    ("1.13", "Montaje soporte tipo SP-01 (mensula a muro/estructura existente con anclaje quimico, perfil UPE 80 + chapa; SP-01-01/02/03)", 21, 180200),
    ("1.14", "Montaje soporte tipo SP-02 (mensula a muro/estructura existente con anclaje quimico; SP-02-01/02)", 3, 97800),
    ("1.15", "Montaje soporte tipo SP-03 - mixto: SP-03-01/02 mensula a muro (anclaje quimico), SP-03-03 soldado a soporte existente Modulo 3 (WPS calificado)", 24, 236800),
    ("1.16", "Montaje soporte tipo SP-04 (pedestal perfil cuadrado 100 mm sobre dado de hormigon + grout; SP-04-01)", 3, 197200),
    ("1.17", "Montaje soporte tipo SP-05 (pedestal con riostra diagonal sobre dado de hormigon + grout; SP-05-01)", 5, 197200),
    ("1.18", "Montaje soporte tipo SP-06 (pedestal con voladizo sobre dado de hormigon + grout; SP-06-01)", 1, 200000),
    ("1.19", "Montaje soporte tipo SP-07 (pedestal con diagonal; SP-07-01/02)", 4, 200000),
    ("1.20", "Montaje soporte tipo SP-08 (pedestal individual alto DN110; SP-08-01)", 1, 210500),
    ("1.21", "Montaje soporte tipo SP-09 (pedestal perfil cuadrado 100 mm sobre dado de hormigon + grout, va a piso; SP-09-01)", 1, 175000),
    ("1.22", "Montaje soporte tipo SP-10 - extremo a soldar en terreno (chapa en radier nuevo o anclaje quimico; SP-10-01)", 2, 128000),
    ("1.23", "Montaje soporte tipo SP-11 (pedestal con doble nivel; SP-11-01/02)", 2, 197800),
]

# ---------- Datos: 6 fundaciones cap. 4 ----------
# CANT = m3 de hormigon G25 (Estimacion de Inversion L&A, hoja BASE; Clase 2 AACE).
# P.UNI. = CIV directo de L&A x 0,60 (mercado norte + premium Taltal; el hormigon
# colocado de L&A esta ~2x sobre mercado aun con premium). Incluye moldaje,
# emplantillado G10, armadura A630-420H y pernos/insertos embebidos.
# La fundacion del sistema CIP (9,74 m3) se desglosa en losa CIP (4.2 = 7,36 m3) y
# fundacion de la cubierta/cobertizo (4.3 = 2,38 m3, con 24 pernos F-1554 colados +
# proteccion interina). La estructura metalica de la cubierta sale del alcance (etapa
# posterior ADASA); solo su fundacion permanece costeada. Fuente del cobertizo:
# P22-DWG-00-002-007_C LAM3 (formas/armaduras/perno PA-1) + IT-00-010-102 item 17.
FUNDACIONES = [
    # (codigo, descripcion, cantidad_m3_G25, p_unitario)
    ("4.1", "Fundacion contenedor modulo RO (F2) - independiente del sistema CIP", 7.52, 739414),
    ("4.2", "Fundacion sistema CIP (F2b) - independiente del contenedor del modulo RO; incluye la junta de dilatacion entre elementos de fundacion (poliestireno expandido de 2,5 cm, sello Sikaflex 1A y primer VP-215 en ambas paredes) del plano P22-DWG-00-002-007 LAM1 Rev 1", 5.80, 654909),
    ("4.3", "Fundacion de la cubierta metalica del sistema CIP (cobertizo) - incluye 24 pernos de anclaje F-1554 3/4\" preinstalados (colados) y su proteccion anticorrosiva interina", 2.38, 654909),
    ("4.4", "Fundacion dinamica bomba BH-06-001 (F3) - segun ACI 351", 0.95, 706238),
    ("4.5", "Fundacion estanque TK-06-001 (F4)", 6.33, 607355),
    ("4.6", "Fundacion camara de drenajes TK-06-004 (F5)", 1.66, 812913),
]

# ---------- Datos: dados de soportes a piso + mov. tierra + drenaje + camaras cap. 4 ----------
# 4.7 dados de soportes a piso: SOLO los 17 soportes con planta de placa base cuadrada sobre dado
# (SP-04/05/06/07/08/09/11); pollo de hormigon 350x350x100 mm = 0,012 m3 c/u sobre placa de acero
# 200x200 (cuadernillo P22-DWG-06-006-107). Se cotiza POR UNIDAD (17 dados); P.UNI por pollo (vaciado
# pequeno + moldaje + nivelacion + grout + excavacion local) [Suposicion, premium Taltal]. SP-01/02 y
# SP-03-01/02 son mensulas a muro (sin dado); SP-03-03 y SP-10 sueldan a existente.
# 4.8/4.9 mercado + premium remoto Taltal. 4.10 red de drenaje (gl, [Suposicion]).
# 4.11 camaras prefabricadas: 6 un + radier G25 0,576 m3 (plano P22-DWG-00-002-006_C;
# L&A las dibujo pero NO las costeo en la Estimacion).
OBRAS_CIVILES_EXTRA = [
    # (codigo, descripcion, unidad, cantidad, p_unitario)
    ("4.7", "Dados de hormigon G25 para pedestales de soportes a piso (17 dados de 350x350x100 mm sobre placa de acero 200x200, segun cuadernillo P22-DWG-06-006-107: SP-04/05/06/07/08/09/11; incluye emplantillado G5, moldaje, nivelacion, grout y excavacion local; el anclaje quimico de la placa va en el montaje del soporte, Cap. 1)", "un", 17, 40000),
    ("4.8", "Excavacion comun en fundaciones y zanjas de drenaje + retiro y transporte de excedentes (retiro incluido en el P.UNI por m3 excavado)", "m3", 111.7, 22000),
    ("4.9", "Relleno compactado con material seleccionado + base estabilizada (sello arena/hormigon pobre) bajo losas", "m3", 91.5, 45000),
    ("4.10", "Sistema de drenaje del modulo (canaleta perimetral + sumideros + tuberia HDPE Ø63 corrugada + conexion a TK-06-004)", "gl", 1, 2700000),
    ("4.11", "Camaras de inspeccion prefabricadas (marca Grau, Budnik o equivalente) incluye radier G25 de base - 6 un + 0,576 m3 (plano P22-DWG-00-002-006)", "un", 6, 340000),
]

# ---------- Datos: estructura de acero embebida cap. 4 ----------
# La cubierta metalica del sistema CIP (estructura ASTM A36 + panel PV-6 + pintado C5-M)
# SALE del alcance de esta licitacion: la suministra e instala ADASA en una etapa
# posterior (la antigua partida 4.10 all-in por kg, ~1.668 kg @ $5.290, se elimina).
# Solo permanece su fundacion (cap. 4 item 4.3, costeada como obra civil). Se conserva el
# acero EMBEBIDO del contenedor RO, que no es de la cubierta:
# 4.12 insertos RO = acero embebido en la fundacion -> suministro + colocacion $3.000/kg
# (sin ereccion con grua ni esquema C5-M; el hormigon protege el acero embebido).
ESTRUCTURAS_ACERO = [
    # (codigo, descripcion, unidad, cantidad, p_unitario)
    ("4.12", "Insertos y estructura embebida del contenedor RO (perfiles L100x100x6 + atiesador PL20, ASTM A36); suministro y colocacion (embebido, sin ereccion ni C5-M)", "kg", 405.66, 3000),
]

# ---------- Datos: impermeabilizacion cap. 4 ----------
# 4.13 fosa: interior quimico-resistente (salmuera ~45-55k ppm Cl-) + exterior enterrado.
# 4.14 fundaciones: proteccion damp-proof/cristalizante del hormigon enterrado (~75% de la
# superficie en contacto con suelo). Areas [Suposicion] sin planos de detalle.
IMPERMEABILIZACION = [
    # (codigo, descripcion, unidad, cantidad, p_unitario)
    ("4.13", "Impermeabilizacion quimico-resistente interior de la fosa de drenajes TK-06-004 + proteccion exterior enterrada (ambiente salmuera)", "gl", 1, 604000),
    ("4.14", "Impermeabilizacion / proteccion del hormigon enterrado de las fundaciones (recubrimiento damp-proof / cristalizante)", "gl", 1, 775908),
]

# Nota al pie de la hoja (despues de TOTAL GENERAL, fuera de la grid de capitulos)
NOTA_CAP4 = (
    "Nota: las cantidades del Capitulo 4 - Obras Civiles son cubicacion referencial Clase 2 AACE "
    "segun la ingenieria de detalle OOCC vigente, en Rev 0 salvo las cinco laminas que pasaron a Rev 1 "
    "(P22-DWG-00-002-002 LAM1 y LAM4, P22-DWG-00-002-003 LAM1, P22-DWG-00-002-007 LAM1 y LAM2). "
    "La unica partida que cambia de cantidad respecto de la Rev 0 de estas Bases es la 4.2, que baja de "
    "7,36 a 5,80 m3 de hormigon G25 porque la Rev 1 reduce la fundacion de equipos del sistema CIP de "
    "4,13 a 2,63 m3 e incorpora una junta de dilatacion; la excavacion de esa zona baja de 5,01 a 1,60 m3 "
    "y se descuenta de la partida 4.8. La fundacion del contenedor sube 250 mm de cota (N.T.C. +6,300 y "
    "sello +5,400) sin que su cuadro de excavacion se modifique, de modo que las cantidades de movimiento "
    "de tierra de esa zona quedan sujetas a la verificacion del contratista en terreno. "
    "La excavacion (4.8) y el relleno (4.9) toman como "
    "respaldo el plano de Movimiento de Tierra P22-DWG-00-001-001 Rev 0, cuya tabla de cubicaciones es "
    "referencial, a validar por el contratista y sin esponjamiento; las cantidades de este Formato son "
    "iguales o superiores a las geometricas del plano (incorporan el esponjamiento y el relleno de "
    "fundaciones no tabulado en el plano). "
    "Los P.UNI. son valores de mercado del norte de Chile con premium logistico de Taltal (no el "
    "analisis de precios del consultor). Los items 4.1 a 4.6 incluyen moldaje, emplantillado G10, "
    "armaduras A630-420H y pernos/insertos embebidos; el item 4.3 (fundacion de la cubierta/cobertizo CIP) "
    "incluye ademas los 24 pernos de anclaje F-1554 colados y su proteccion anticorrosiva interina; el item "
    "4.7 son los 17 dados (cotizados por unidad) de los soportes que van a piso (SP-04/05/06/07/08/09/11 del "
    "cuadernillo; pollo de hormigon de 350x350x100 mm sobre placa de acero 200x200, referencial, sujeto a la "
    "memoria de calculo de soportes). La estructura metalica "
    "de la cubierta (perfiles ASTM A36, panel PV-6, pintado C5-M) NO forma parte de esta licitacion: la "
    "suministra e instala ADASA en una etapa posterior; solo su fundacion permanece costeada. Las camaras "
    "prefabricadas (4.11) y la impermeabilizacion (4.13/4.14) corresponden a alcance de obra no cuantificado "
    "en la Estimacion de Inversion. Las partidas 4.10, 4.13 y 4.14 son valores referenciales a confirmar "
    "por el contratista."
)


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
    c_e = ws[f"E{row}"]; c_e.value = p_unitario_val if INCLUIR_PUNI else None
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
    Escribe 4 filas (igual al entregable Rev 0):
    COSTO DIRECTO, GASTOS GENERALES 20%, UTILIDADES 10%, TOTAL GENERAL.
    """
    r_cd = row_inicio
    r_gg = row_inicio + 1
    r_ut = row_inicio + 2
    r_tg = row_inicio + 3

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

    # Filas GG % y UT %
    def fila_pct(r, label, pct, formula):
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
        ws[f"C{r}"].value = "%"
        ws[f"D{r}"].value = pct
        ws[f"D{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"D{r}"].number_format = "0"
        ws[f"F{r}"].value = formula
        ws[f"F{r}"].number_format = FMT_MONEDA_TOTAL
        ws[f"F{r}"].alignment = Alignment(horizontal="right", vertical="center")

    fila_pct(r_gg, "GASTOS GENERALES", 20, f"=F{r_cd}*D{r_gg}/100")
    fila_pct(r_ut, "UTILIDADES",       10, f"=F{r_cd}*D{r_ut}/100")

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
    ws[f"F{r_tg}"].value = f"=+F{r_cd}+F{r_gg}+F{r_ut}"
    ws[f"F{r_tg}"].number_format = FMT_MONEDA_TOTAL


# ---------- Generador principal ----------
def main():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Presupuesto"

    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 70
    ws.column_dimensions["C"].width = 10
    ws.column_dimensions["D"].width = 10
    ws.column_dimensions["E"].width = 15
    ws.column_dimensions["F"].width = 18

    escribir_titulo(ws)
    escribir_header(ws, row=4)

    # ---- Capitulo 1: HDPE (12 lineas + 11 soportes = 23 sub-items) ----
    row = 6
    r_cap1 = row
    row += 1
    r_cap1_inicio = row
    for codigo, tag, servicio, valvulas, precio in LINEAS_HDPE:
        partida = f"Fabricacion y montaje linea {tag} - {servicio}"
        if valvulas:
            partida += f" (incluye montaje in-line: {valvulas})"
        escribir_subitem(ws, row, codigo, partida, "gl", 1, precio)
        ws.row_dimensions[row].height = 28
        row += 1
    for codigo, descripcion, cantidad, precio in SOPORTES_HDPE:
        escribir_subitem(ws, row, codigo, descripcion, "un", cantidad, precio)
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
    escribir_subitem(ws, row, "2.1", ESTANQUE, "un", 1, ESTANQUE_PU); row += 1
    escribir_subitem(ws, row, "2.2", ESTANQUE_TRASLADO, "un", 1, ESTANQUE_TRASLADO_PU); row += 1
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
    escribir_subitem(ws, row, "3.1", BOMBA, "un", 1, BOMBA_PU); row += 1
    ws.row_dimensions[row - 1].height = 30
    escribir_subitem(ws, row, "3.2", BOMBA_TRASLADO, "un", 1, BOMBA_TRASLADO_PU); row += 1
    r_cap3_fin = row - 1
    escribir_fila_capitulo(
        ws, r_cap3, 3, "MONTAJE DE BOMBA CENTRIFUGA",
        f"=SUM(F{r_cap3_inicio}:F{r_cap3_fin})",
    )

    row += 1  # fila en blanco

    # ---- Capitulo 4: Obras Civiles (14 sub-items) ----
    r_cap4 = row
    row += 1
    r_cap4_inicio = row
    # Bloque 4.1-4.6: fundaciones (CANT = m3 G25; incluye fundacion de la cubierta 4.3)
    for codigo, descripcion, cantidad, precio in FUNDACIONES:
        escribir_subitem(ws, row, codigo, descripcion, "m3", cantidad, precio)
        ws.row_dimensions[row].height = 28
        row += 1
    # Bloque 4.7-4.11: dados de soportes a piso (un) + movimiento de tierra + drenaje + camaras
    for codigo, descripcion, unidad, cantidad, precio in OBRAS_CIVILES_EXTRA:
        escribir_subitem(ws, row, codigo, descripcion, unidad, cantidad, precio)
        ws.row_dimensions[row].height = 28
        row += 1
    # Bloque 4.12: acero embebido del contenedor RO (la cubierta salio del alcance)
    for codigo, descripcion, unidad, cantidad, precio in ESTRUCTURAS_ACERO:
        escribir_subitem(ws, row, codigo, descripcion, unidad, cantidad, precio)
        ws.row_dimensions[row].height = 28
        row += 1
    # Bloque 4.13-4.14: impermeabilizacion
    for codigo, descripcion, unidad, cantidad, precio in IMPERMEABILIZACION:
        escribir_subitem(ws, row, codigo, descripcion, unidad, cantidad, precio)
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

    # ---- Nota cubicacion referencial Cap. 4 (tras TOTAL GENERAL) ----
    r_nota = row + 5  # totalizadores ocupan 4 filas + 1 en blanco
    ws.merge_cells(f"A{r_nota}:F{r_nota}")
    c_nota = ws[f"A{r_nota}"]
    c_nota.value = NOTA_CAP4
    c_nota.font = Font(name=FONT_NAME, size=9, italic=True)
    c_nota.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws.row_dimensions[r_nota].height = 56

    # Freeze panes y print area
    ws.freeze_panes = "A5"
    ultima_fila = r_nota
    ws.print_area = f"A1:F{ultima_fila}"
    ws.page_setup.orientation = ws.ORIENTATION_PORTRAIT
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    wb.save(OUTPUT_PATH)

    cap1_n = len(LINEAS_HDPE) + len(SOPORTES_HDPE)
    cap4_n = (len(FUNDACIONES) + len(OBRAS_CIVILES_EXTRA) + len(ESTRUCTURAS_ACERO)
              + len(IMPERMEABILIZACION))
    n_subitems = cap1_n + 2 + 2 + cap4_n
    print(f"OK: {OUTPUT_PATH.name} generado ({n_subitems} sub-items en 4 capitulos)")
    print(f"    Ruta: {OUTPUT_PATH}")
    print()
    print(f"  - Capitulo 1: {cap1_n} sub-items ({len(LINEAS_HDPE)} lineas HDPE + {len(SOPORTES_HDPE)} soportes)")
    print(f"  - Capitulo 4: {cap4_n} sub-items (6 fundaciones + 5 obras civiles (dados de soportes 4.7 un +")
    print(f"      mov.tierra/drenaje/camaras) + 1 acero embebido RO + 2 impermeabilizacion)")
    print(f"  - P.UNI. Cap. 4 a mercado norte + premium Taltal (no el APU de L&A)")
    print(f"  - Dados de soportes a piso 4.7: 17 dados (un) de 350x350x100 mm x $40.000 = $680.000 [Suposicion]")
    print(f"  - Cubierta metalica CIP descopada (etapa posterior ADASA); fundacion 4.3 (2,38 m3) costeada")
    print(f"  - Gaps cerrados: 6 camaras prefab (plano), impermeabilizacion")
    print(f"  - Totalizadores: COSTO DIRECTO / GG 20% / UTILIDADES 10% / TOTAL GENERAL (sin IVA)")


if __name__ == "__main__":
    main()
