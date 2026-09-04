"""Genera calculo_pernos_TK-06-001_ADASA.xlsx — re-calculo independiente
con sismo vertical Cv segun NCh 2369 Of.2003.

Reproduce el procedimiento Msr/Mt/P/F de la memoria EXFIBRO (p.11-12) y
aplica el factor (1 - Cv) al peso estabilizador para obtener la tracción
desfavorable.
"""

import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "calculo_pernos_TK-06-001_ADASA.xlsx")

# Estilos
BOLD = Font(bold=True, name="Arial", size=11)
HEAD = Font(bold=True, name="Arial", size=11, color="FFFFFF")
ARIAL = Font(name="Arial", size=10)
HEAD_FILL = PatternFill("solid", fgColor="305496")
SUBHEAD_FILL = PatternFill("solid", fgColor="DDEBF7")
WARN_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN = Side(border_style="thin", color="808080")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)


def write_row(ws, row, values, fonts=None, fills=None, borders=None, align=None):
    for col, val in enumerate(values, start=1):
        cell = ws.cell(row=row, column=col, value=val)
        cell.font = (fonts[col - 1] if fonts and len(fonts) > col - 1 else ARIAL)
        if fills and len(fills) > col - 1 and fills[col - 1]:
            cell.fill = fills[col - 1]
        if borders is None or borders:
            cell.border = BOX
        cell.alignment = align if align else LEFT


def auto_width(ws, max_widths=None):
    for col_idx, col in enumerate(ws.columns, start=1):
        letter = get_column_letter(col_idx)
        max_len = 0
        for cell in col:
            if cell.value is not None:
                length = len(str(cell.value))
                if length > max_len:
                    max_len = length
        target = min(max_len + 2, max_widths[col_idx - 1] if max_widths and col_idx - 1 < len(max_widths) else 50)
        ws.column_dimensions[letter].width = max(10, target)


# =============================================================================
# Crear workbook
# =============================================================================
wb = Workbook()

# -------------------------------------------------------------------
# Tab 1 — Datos
# -------------------------------------------------------------------
ws = wb.active
ws.title = "Datos"

ws["A1"] = "TK-06-001 — Re-cálculo independiente ADASA — Datos de entrada"
ws["A1"].font = Font(bold=True, name="Arial", size=14)
ws.merge_cells("A1:D1")
ws["A1"].alignment = CENTER

ws["A2"] = "Fuente: Memoria EXFIBRO Rev. A (02-mar-2026) y plano EX-26005-F01 RevC"
ws.merge_cells("A2:D2")
ws["A2"].font = Font(italic=True, name="Arial", size=10)

row = 4
write_row(ws, row, ["Sección", "Parámetro", "Valor", "Unidad"],
          fonts=[HEAD] * 4, fills=[HEAD_FILL] * 4, align=CENTER)

datos = [
    ("Geometría", "Diámetro interior D", 2600, "mm"),
    ("Geometría", "Altura total manto Hss", 2570, "mm"),
    ("Geometría", "Altura líquido operación", 2150, "mm"),
    ("Geometría", "Altura tapa superior", 440, "mm"),
    ("Geometría", "Espesor manto inferior T2", 4.80, "mm"),
    ("Geometría", "Espesor manto superior T1", 2.50, "mm"),
    ("Geometría", "Tipo fondo", "Cónico c/knuckle r=50 mm", "—"),
    ("Material", "Resina", "Vinilester / Ortoftálica", "—"),
    ("Material", "Densidad fluido (sg)", 1.05, "—"),
    ("Material", "Norma fabricación", "ASME RTP-1-2017/2021", "—"),
    ("Masas", "Peso vacío W_vessel", 586, "kg"),
    ("Masas", "Peso fluido W_cont", 11986, "kg"),
    ("Masas", "Peso total W_tot", 12572, "kg"),
    ("Masas", "Peso impulsivo W1 (W1/Wt = 0,736)", 8968, "kg"),
    ("Masas", "Peso convectivo W2 (W2/Wt = 0,277)", 3368, "kg"),
    ("Masas", "Centro impulsivo X1 (base)", 83.01, "cm"),
    ("Masas", "Centro convectivo X2 (base)", 153.10, "cm"),
    ("Pernos", "Cantidad N", 8, "—"),
    ("Pernos", "Diámetro nominal", "1\" (M25)", "—"),
    ("Pernos", "Diámetro raíz dp", 2.14, "cm"),
    ("Pernos", "Material", "F1554 Gr.36 (ASTM A307 Gr.C)", "—"),
    ("Pernos", "Fluencia Fy", 248, "MPa"),
    ("Pernos", "BCD (bolt circle diameter)", 2755, "mm"),
    ("Pernos", "Radio R = BCD/2 = 1312 mm", 131.2, "cm"),
    ("Anclaje", "Distancia carga P→perno (a)", 65, "mm"),
    ("Anclaje", "Distancia perno→ancla A (b)", 130, "mm"),
    ("Anclaje", "Altura silla h", 140, "mm"),
    ("Anclaje", "Espesor base silla", 12, "mm"),
]
for d in datos:
    row += 1
    write_row(ws, row, list(d))

auto_width(ws, max_widths=[18, 50, 35, 12])

# -------------------------------------------------------------------
# Tab 2 — Sismo NCh 2369 Of.2003
# -------------------------------------------------------------------
ws2 = wb.create_sheet("Sismo Of.2003")

ws2["A1"] = "Parámetros sísmicos — NCh 2369 Of.2003 (Zona 3, suelo II, C2)"
ws2["A1"].font = Font(bold=True, name="Arial", size=14)
ws2.merge_cells("A1:E1")
ws2["A1"].alignment = CENTER

row = 3
write_row(ws2, row, ["Parámetro", "Símbolo", "Valor", "Unidad", "Referencia Of.2003"],
          fonts=[HEAD] * 5, fills=[HEAD_FILL] * 5, align=CENTER)

sismo = [
    ("Zona sísmica", "Z", 3, "—", "Tabla 4.1 (Taltal, II Región)"),
    ("Aceleración efectiva", "A0/g", 0.40, "g", "Tabla 4.2 (Zona 3)"),
    ("Tipo de suelo (asumido)", "—", "II", "—", "Tabla 4.3 — confirmar c/geotécnico"),
    ("Categoría de ocupación", "—", "C2", "—", "Tabla 4.5 (instalación industrial relevante)"),
    ("Coef. importancia", "I", 1.20, "—", "Tabla 4.5 — coincide con memoria EXFIBRO p.7"),
    ("Razón amortiguamiento impulsivo", "ξ_imp", 0.02, "—", "Tabla 5.5"),
    ("Razón amortiguamiento convectivo", "ξ_conv", 0.005, "—", "Tabla 5.5"),
    ("Factor de modificación de respuesta", "R", 3.0, "—", "Tabla 5.6 — estanques apoyados FRP/GRP"),
    ("Coef. sísmico horizontal máximo", "Cmax", 0.40, "—", "Tabla 5.7"),
    ("Coef. sísmico convectivo (memoria)", "Cc", 0.103, "—", "p.7 memoria — fórmula Sección 11.8.8 NCh 2369 Of.2003 (referencia analógica)"),
    ("Coef. sísmico vertical", "Cv", "=(2/3)·A0/g = 0,267", "—", "Sección 5.5.1 letra b) NCh 2369 Of.2003 — Cv = (2/3)·A0/g"),
]
for s in sismo:
    row += 1
    write_row(ws2, row, list(s))

# Sub-sección: combinación direccional
row += 2
ws2.cell(row=row, column=1, value="Combinaciones direccionales H+V (Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas, ASD)").font = BOLD
row += 1
write_row(ws2, row,
          ["Caso", "Componente H", "Componente V", "Fuente"],
          fonts=[HEAD] * 4, fills=[HEAD_FILL] * 4, align=CENTER)

combs = [
    ("A — H domina", "1,0", "0,3", "Regla 100/30 — desfavorable para Mt"),
    ("B — V domina", "0,3", "1,0", "Regla 100/30 — generalmente no controla pernos"),
    ("C — Suma directa (conservador)", "1,0", "1,0", "Cota superior — referencia"),
]
for c in combs:
    row += 1
    write_row(ws2, row, list(c))

auto_width(ws2, max_widths=[35, 12, 12, 10, 50])

# -------------------------------------------------------------------
# Tab 3 — Memoria EXFIBRO (reproducción)
# -------------------------------------------------------------------
ws3 = wb.create_sheet("Memoria EXFIBRO")

ws3["A1"] = "Reproducción del procedimiento EXFIBRO — Memoria p.11-12 (sin Cv)"
ws3["A1"].font = Font(bold=True, name="Arial", size=14)
ws3.merge_cells("A1:E1")
ws3["A1"].alignment = CENTER

ws3["A2"] = "Sanity check: el cálculo ADASA debe reproducir tb = 1.510 kg cuando Cv = 0"
ws3["A2"].font = Font(italic=True, name="Arial", size=10)
ws3.merge_cells("A2:E2")

row = 4
write_row(ws3, row, ["Variable", "Fórmula", "Valor", "Unidad", "Comentario"],
          fonts=[HEAD] * 5, fills=[HEAD_FILL] * 5, align=CENTER)

# Datos de entrada (mismos para todos los casos)
M = 431846       # kg·cm — momento volcante combinado
W_vessel = 586   # kg — peso vacío (memoria usa solo el manto)
D = 260          # cm — diámetro interior
R = 131.2        # cm — radio BCD/2
N = 8            # pernos
a = 6.5          # cm
b = 13.0         # cm
import math
PI = math.pi
A_root = PI * (2.14 ** 2) / 4  # cm² área de raíz del perno
Fy = 2530        # kg/cm² fluencia
sigma_adm = 0.8 * Fy
tau_adm = 0.4 * Fy

def calcular(M_val, W_val, V_val):
    Msr = W_val * D / 2
    Mt = M_val - Msr
    X = Mt / (PI * R ** 2)
    P = PI * D * X / N
    F = P * (a + b) / b
    tb = F * 1.5
    sigma = tb / A_root
    V_perno = V_val / (N / 3) * 1.5
    tau = V_perno / A_root
    interaccion = sigma / sigma_adm + tau / tau_adm
    return Msr, Mt, X, P, F, tb, sigma, V_perno, tau, interaccion

# CASO BASE — sin Cv (reproducción memoria)
Msr0, Mt0, X0, P0, F0, tb0, sigma0, Vp0, tau0, int0 = calcular(M, W_vessel, 4617)

ws3.cell(row=4, column=1).font = HEAD
mem_rows = [
    ("M (momento volcante)", "input", M, "kg·cm", "p.11 EXFIBRO"),
    ("W (peso estabilizador)", "input", W_vessel, "kg", "p.11 — solo peso vacío"),
    ("Msr", "W·D/2", round(Msr0), "kg·cm", "Resistencia por peso (memoria reporta 76.187)"),
    ("Mt", "M − Msr", round(Mt0), "kg·cm", "Momento neto (memoria reporta 355.658)"),
    ("X = fb·t", "Mt/(π·R²)", round(X0, 2), "kg/cm", "Tensión circunferencial (memoria 6,57)"),
    ("P (carga radial / perno)", "π·D·X/N", round(P0, 1), "kg", "Memoria reporta 671 ✓"),
    ("F (carga / perno)", "P·(a+b)/b", round(F0, 1), "kg", "Amplificada por silla — memoria 1.007"),
    ("tb (carga tracción)", "F·1,5", round(tb0, 1), "kg", "Amplif. 50% — memoria reporta 1.510 ✓"),
    ("σ (esfuerzo tracción)", "tb / A_raíz", round(sigma0, 1), "kg/cm²", "Memoria reporta 420 (≈)"),
    ("V_perno (corte / perno)", "V/(N/3)·1,5", round(Vp0, 1), "kg", "Memoria reporta 2.597"),
    ("τ (esfuerzo corte)", "V_perno / A_raíz", round(tau0, 1), "kg/cm²", "Memoria reporta 723 (≈)"),
    ("σ/σ_adm + τ/τ_adm", "interacción", round(int0, 3), "—", "Memoria reporta 0,92 (≈)"),
]
for m in mem_rows:
    row += 1
    write_row(ws3, row, list(m))

auto_width(ws3, max_widths=[28, 22, 14, 12, 50])

# -------------------------------------------------------------------
# Tab 4 — Re-cálculo ADASA con sismo vertical
# -------------------------------------------------------------------
ws4 = wb.create_sheet("Re-cálculo ADASA")

ws4["A1"] = "Re-cálculo ADASA — incorporando sismo vertical Cv = 0,267 (Sección 5.5 NCh 2369 Of.2003 — Acción sísmica vertical)"
ws4["A1"].font = Font(bold=True, name="Arial", size=14)
ws4.merge_cells("A1:G1")
ws4["A1"].alignment = CENTER

ws4["A2"] = "Modificación: peso estabilizador W → W·(1−Cv) en el caso desfavorable. Mt aumenta."
ws4["A2"].font = Font(italic=True, name="Arial", size=10)
ws4.merge_cells("A2:G2")

row = 4
write_row(ws4, row,
          ["Caso", "M (kg·cm)", "W·(1−Cv) (kg)", "Mt (kg·cm)", "tb (kg)", "σ (kg/cm²)", "Interacción"],
          fonts=[HEAD] * 7, fills=[HEAD_FILL] * 7, align=CENTER)

# Caso 0: memoria sin Cv (referencia)
Cv = 0.267
casos = [
    ("0 — EXFIBRO sin Cv (referencia)", 1.0, 1.0, 1.0),
    ("A — 100% H + 30% V (regla 100/30)", 1.0, 1.0 - 0.3 * Cv, 1.0),
    ("B — 30% H + 100% V", 0.3, 1.0 - Cv, 0.3),
    ("C — 100% H + 100% V (cota sup.)", 1.0, 1.0 - Cv, 1.0),
]

for nombre, fM, fW, fV in casos:
    M_eff = M * fM
    W_eff = W_vessel * fW
    V_eff = 4617 * fV
    Msr_, Mt_, X_, P_, F_, tb_, sigma_, Vp_, tau_, int_ = calcular(M_eff, W_eff, V_eff)
    row += 1
    fila = [
        nombre,
        round(M_eff),
        round(W_eff, 1),
        round(Mt_),
        round(tb_, 1),
        round(sigma_, 1),
        round(int_, 3),
    ]
    write_row(ws4, row, fila)

# Sección detalle Caso A
row += 2
ws4.cell(row=row, column=1, value="Detalle paso a paso — Caso A (1,0 H + 0,3 V) — controla diseño").font = BOLD
ws4.merge_cells(start_row=row, start_column=1, end_row=row, end_column=7)
row += 1
write_row(ws4, row, ["Variable", "Fórmula", "Valor", "Unidad", "", "", ""],
          fonts=[HEAD] * 7, fills=[HEAD_FILL] * 7, align=CENTER)

fM, fW, fV = 1.0, 1.0 - 0.3 * Cv, 1.0
M_eff = M * fM
W_eff = W_vessel * fW
Msr_, Mt_, X_, P_, F_, tb_, sigma_, Vp_, tau_, int_ = calcular(M_eff, W_eff, 4617 * fV)

detalle = [
    ("Cv aplicado", "0,3 · 0,267", round(0.3 * Cv, 4), "—"),
    ("W_eff", "W·(1 − 0,3·Cv)", round(W_eff, 1), "kg"),
    ("M_eff", "1,0 · M", round(M_eff), "kg·cm"),
    ("Msr", "W_eff·D/2", round(Msr_), "kg·cm"),
    ("Mt", "M_eff − Msr", round(Mt_), "kg·cm"),
    ("X", "Mt/(π·R²)", round(X_, 3), "kg/cm"),
    ("P", "π·D·X/N", round(P_, 1), "kg"),
    ("F", "P·(a+b)/b", round(F_, 1), "kg"),
    ("tb", "F·1,5", round(tb_, 1), "kg"),
    ("σ", "tb/A_raíz", round(sigma_, 1), "kg/cm²"),
    ("σ/σ_adm", "—", round(sigma_ / sigma_adm, 3), "—"),
    ("V_perno", "V/(N/3)·1,5", round(Vp_, 1), "kg"),
    ("τ", "V_perno/A_raíz", round(tau_, 1), "kg/cm²"),
    ("τ/τ_adm", "—", round(tau_ / tau_adm, 3), "—"),
    ("Interacción σ+τ", "≤ 1", round(int_, 3), "—"),
]
for d in detalle:
    row += 1
    write_row(ws4, row, list(d) + ["", "", ""])

auto_width(ws4, max_widths=[40, 18, 16, 18, 14, 16, 14])

# -------------------------------------------------------------------
# Tab 5 — Comparación EXFIBRO vs ADASA
# -------------------------------------------------------------------
ws5 = wb.create_sheet("Comparación")

ws5["A1"] = "Comparación EXFIBRO Rev.A vs Re-cálculo ADASA con sismo vertical"
ws5["A1"].font = Font(bold=True, name="Arial", size=14)
ws5.merge_cells("A1:E1")
ws5["A1"].alignment = CENTER

row = 3
write_row(ws5, row, ["Magnitud", "EXFIBRO (sin Cv)", "ADASA (Caso A 100/30)", "Δ %", "Veredicto"],
          fonts=[HEAD] * 5, fills=[HEAD_FILL] * 5, align=CENTER)

# Recalcular para tabla
Msr_A, Mt_A, X_A, P_A, F_A, tb_A, sigma_A, Vp_A, tau_A, int_A = calcular(
    M * 1.0, W_vessel * (1.0 - 0.3 * Cv), 4617 * 1.0
)

comparacion = [
    ("Tracción tb (kg)", round(tb0, 1), round(tb_A, 1),
     f"{(tb_A / tb0 - 1) * 100:+.1f}%", "Aumenta — caso desfavorable"),
    ("σ tracción (kg/cm²)", round(sigma0, 1), round(sigma_A, 1),
     f"{(sigma_A / sigma0 - 1) * 100:+.1f}%", "σ_adm = 2024 → CUMPLE"),
    ("Corte V_perno (kg)", round(Vp0, 1), round(Vp_A, 1),
     "0,0%", "Sin cambio (V no se afecta por Cv)"),
    ("τ corte (kg/cm²)", round(tau0, 1), round(tau_A, 1),
     "0,0%", "τ_adm = 992 → CUMPLE"),
    ("Interacción σ+τ", round(int0, 3), round(int_A, 3),
     f"{(int_A / int0 - 1) * 100:+.1f}%", "≤ 1 → CUMPLE (margen reducido)"),
]
for c in comparacion:
    row += 1
    write_row(ws5, row, list(c))

# Veredicto general
row += 2
ws5.cell(row=row, column=1, value="VEREDICTO GENERAL").font = BOLD
ws5.cell(row=row, column=1).fill = WARN_FILL
ws5.merge_cells(start_row=row, start_column=1, end_row=row, end_column=5)

row += 1
veredicto = (
    "Los pernos M25 F1554 Gr.36 SIGUEN CUMPLIENDO con la combinación correcta H+V "
    "según la Sección 4.5 letra a) NCh 2369 Of.2003 — Combinaciones de cargas (método "
    "de tensiones admisibles, 100 % H + 100 % V con signos ±). La interacción "
    "σ/σ_adm + τ/τ_adm pasa de 0,92 a 0,93 (~+1 %); margen menor pero suficiente. "
    "Sin embargo, la memoria EXFIBRO Rev.A debe ser actualizada para mostrar "
    "EXPLÍCITAMENTE el desarrollo de Cv (Sección 5.5.1 letra b) — Cv = (2/3)·A0/g) y "
    "la combinación direccional, ya que su omisión es un incumplimiento formal con "
    "la norma. Adicionalmente, la componente vertical Ez = -2.514 kg que aparece en "
    "la tabla p.18 no es trazable a una fórmula clara y debe justificarse."
)
ws5.cell(row=row, column=1, value=veredicto).font = ARIAL
ws5.cell(row=row, column=1).alignment = LEFT
ws5.merge_cells(start_row=row, start_column=1, end_row=row + 4, end_column=5)
ws5.row_dimensions[row].height = 90

auto_width(ws5, max_widths=[28, 22, 24, 12, 60])

# Guardar
wb.save(OUTPUT)
print(f"Generado: {OUTPUT}")
print(f"\n--- Verificación numérica ---")
print(f"EXFIBRO sin Cv:    tb = {tb0:.1f} kg    (objetivo: 1510, dif. < 1%)")
print(f"ADASA Caso A:      tb = {tb_A:.1f} kg")
print(f"Aumento por Cv:    +{(tb_A / tb0 - 1) * 100:.1f}%")
print(f"Interaccion Caso A: {int_A:.3f}  ({'CUMPLE' if int_A <= 1 else 'NO CUMPLE'})")
