#!/usr/bin/env python3
"""
Genera los PNG de figuras explicativas y de anexos para la ET de Montaje
Electromecanico P22-ET-06-007-001-0.

Salidas:
  figuras/fig-4-1.png   Detalle de anclajes (recorte plano estanque)
  figuras/fig-4-2.png   Patron cruzado-radial de apriete (diagrama nuevo)
  figuras/fig-5-1.png   Disposicion de boquillas TK (recorte plano estanque)
  figuras/fig-5-2.png   Orejas de izaje y angulo eslingas (recorte)
  figuras/fig-6-1.png   Baseplate sobre fundacion + grout 25 mm (diagrama)
  figuras/fig-6-2.png   Setup alineamiento laser bomba-motor (diagrama)
  figuras/fig-6-3.png   Dimensiones bridas y momentos maximos KSB (recorte)
  figuras/fig-7-1.png   Circuito de prueba Megger / Hipot motor (diagrama)
  figuras/fig-8-1.png   Diagrama de flujo del ITP (diagrama)
  figuras/anexo-A-pNN.png   Pagina N del plano de montaje
  figuras/anexo-B-pNN.png   Pagina N del plano del estanque
  figuras/anexo-C-pNN.png   Pagina N del plano de la bomba

Recortes de planos: renderiza la pagina completa del PDF a 300 dpi y la
guarda como PNG. Posteriormente el usuario puede definir crops puntuales si
los necesita; por ahora la pagina completa es el insumo de referencia.

Diagramas conceptuales: se generan con matplotlib usando primitivas
geometricas (sin dependencia de Visio o PowerPoint).
"""

import os

import fitz  # PyMuPDF
import matplotlib.pyplot as plt
from matplotlib.patches import (
    FancyArrowPatch,
    Polygon,
    Rectangle,
    Wedge,
)
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURAS_DIR = os.path.join(SCRIPT_DIR, "figuras")
ANEXOS_DIR = os.path.join(SCRIPT_DIR, "anexos")

os.makedirs(FIGURAS_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# 1) Render de paginas completas de los PDF de anexos a PNG (300 dpi).
# ---------------------------------------------------------------------------

PDF_FIGURAS = [
    # (pdf, identificador, prefijo)
    ("Anexo-A_P22-DWG-06-005-101-0.pdf", "anexo-A", "Plano de Montaje"),
    ("Anexo-B_EX-26005-F01-Rev0.pdf", "anexo-B", "Plano Estanque"),
    ("Anexo-C_KSB-KNCPP11-050.pdf", "anexo-C", "Plano Bomba KSB"),
]


def render_pdf_paginas(pdf_path, prefijo_out, dpi=300):
    paths = []
    doc = fitz.open(pdf_path)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out_path = os.path.join(
            FIGURAS_DIR, f"{prefijo_out}-p{i + 1:02d}.png"
        )
        pix.save(out_path)
        paths.append(out_path)
    doc.close()
    return paths


def generar_anexos_y_recortes_planos():
    """Renderiza paginas completas. Las figuras 4.1, 5.1, 5.2, 6.3 reutilizan
    el render de la pagina 1 del plano correspondiente (estanque o bomba).
    """
    rendered = {}
    for pdf_name, prefijo, _ in PDF_FIGURAS:
        pdf_path = os.path.join(ANEXOS_DIR, pdf_name)
        if not os.path.exists(pdf_path):
            print(f"  [skip] no existe {pdf_path}")
            continue
        paths = render_pdf_paginas(pdf_path, prefijo)
        rendered[prefijo] = paths
        print(f"  [ok] {prefijo}: {len(paths)} pagina(s)")

    # Figuras del cuerpo que son recortes/renders directos del plano
    mapping = {
        "fig-4-1.png": rendered.get("anexo-B", [None])[0],  # estanque pag 1
        "fig-5-1.png": rendered.get("anexo-B", [None])[0],
        "fig-5-2.png": rendered.get("anexo-B", [None])[0],
        "fig-6-3.png": rendered.get("anexo-C", [None])[0],  # bomba pag 1
    }
    for out_name, src in mapping.items():
        if src is None:
            print(f"  [skip] {out_name}: sin source")
            continue
        # copiar (en lugar de un crop especifico, hasta tener bboxes)
        dst = os.path.join(FIGURAS_DIR, out_name)
        with open(src, "rb") as f_src, open(dst, "wb") as f_dst:
            f_dst.write(f_src.read())
        print(f"  [ok] {out_name} <- {os.path.basename(src)}")


# ---------------------------------------------------------------------------
# 2) Diagramas conceptuales con matplotlib.
# ---------------------------------------------------------------------------


def save_fig(fig, name, dpi=300):
    path = os.path.join(FIGURAS_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [ok] {name}")


def fig_4_2_patron_apriete():
    """Patron cruzado-radial de apriete de pernos de sillas.
    Circulo con 8 pernos numerados en secuencia cruzada (1, 5, 3, 7, 2, 6, 4, 8).
    """
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect("equal")
    ax.axis("off")

    # Circulo base (representa la silla)
    circle = plt.Circle((0, 0), 1.0, fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(circle)

    n = 8
    # Secuencia cruzada estandar para 8 pernos
    secuencia = [1, 5, 3, 7, 2, 6, 4, 8]
    # Posicion de cada perno (en orden fisico, no de apriete)
    posiciones = {}
    for i in range(n):
        angle = -np.pi / 2 + 2 * np.pi * i / n
        x = 1.0 * np.cos(angle)
        y = 1.0 * np.sin(angle)
        posiciones[i + 1] = (x, y)
        ax.plot(x, y, "ko", markersize=18)
        ax.text(
            x * 1.18, y * 1.18,
            f"{secuencia.index(i + 1) + 1}",
            ha="center", va="center",
            fontsize=14, fontweight="bold", color="darkred",
        )

    # Flechas conectoras (orden de apriete)
    for k in range(len(secuencia) - 1):
        p1 = posiciones[secuencia[k]]
        p2 = posiciones[secuencia[k + 1]]
        arrow = FancyArrowPatch(
            p1, p2,
            arrowstyle="->", mutation_scale=18,
            color="gray", linewidth=1.0, alpha=0.5,
            connectionstyle="arc3,rad=0.0",
        )
        ax.add_patch(arrow)

    ax.text(
        0, -1.55,
        "Secuencia de apriete cruzado-radial (8 pernos).\n"
        "Aplicar dos pasadas: 50 % del torque nominal, luego 100 %.",
        ha="center", va="center", fontsize=10,
    )

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.8, 1.3)
    save_fig(fig, "fig-4-2.png")


def fig_6_1_baseplate_grout():
    """Esquema baseplate sobre fundacion: grout 25 mm bajo el baseplate y
    relleno del frame metalico interno con el mismo Sikagrout.
    """
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_aspect("equal")
    ax.axis("off")

    # ---- Fundacion de hormigon -------------------------------------------
    fund = Rectangle((0, 0), 10, 2, facecolor="#bdbdbd", edgecolor="black")
    ax.add_patch(fund)
    for y in np.linspace(0, 2, 8):
        ax.plot([0, 10], [y, y], color="gray", linewidth=0.4)

    # ---- Grout franja inferior (25 mm bajo el baseplate) -----------------
    grout_franja = Rectangle((1, 2), 8, 0.5, facecolor="#fff3a0", edgecolor="black")
    ax.add_patch(grout_franja)

    # ---- Frame metalico de la baseplate (U invertida) --------------------
    # El frame se compone de: pared inferior, dos paredes laterales y la
    # placa superior (top plate). El interior se rellena con Sikagrout.
    espesor_acero = 0.10  # espesor visual del acero del frame
    x_izq, x_der = 1, 9
    y_base_inf = 2.5  # cara superior del grout = cara inferior del frame
    y_base_sup = 4.0  # cara superior del top plate
    altura_top = 0.18  # espesor del top plate (donde montan bomba y motor)

    # Relleno interno con grout (mismo color que la franja)
    grout_interno = Rectangle(
        (x_izq + espesor_acero, y_base_inf),
        (x_der - x_izq) - 2 * espesor_acero,
        (y_base_sup - y_base_inf) - altura_top,
        facecolor="#fff3a0",
        edgecolor="none",
        zorder=1,
    )
    ax.add_patch(grout_interno)

    # Pared lateral izquierda del frame
    pared_izq = Rectangle(
        (x_izq, y_base_inf), espesor_acero, y_base_sup - y_base_inf,
        facecolor="#4a4a4a", edgecolor="black", zorder=2,
    )
    ax.add_patch(pared_izq)
    # Pared lateral derecha
    pared_der = Rectangle(
        (x_der - espesor_acero, y_base_inf), espesor_acero,
        y_base_sup - y_base_inf,
        facecolor="#4a4a4a", edgecolor="black", zorder=2,
    )
    ax.add_patch(pared_der)
    # Top plate (placa superior de acero, donde montan bomba y motor)
    top_plate = Rectangle(
        (x_izq, y_base_sup - altura_top), x_der - x_izq, altura_top,
        facecolor="#4a4a4a", edgecolor="black", zorder=2,
    )
    ax.add_patch(top_plate)

    # ---- Bomba y motor ---------------------------------------------------
    bomba = Rectangle((1.7, y_base_sup), 3.4, 2, facecolor="#5b9bd5", edgecolor="black")
    ax.add_patch(bomba)
    ax.text(3.4, y_base_sup + 1, "BOMBA",
            ha="center", va="center", fontsize=11, fontweight="bold", color="white")

    motor = Rectangle((5.5, y_base_sup), 3.0, 2, facecolor="#70ad47", edgecolor="black")
    ax.add_patch(motor)
    ax.text(7.0, y_base_sup + 1, "MOTOR",
            ha="center", va="center", fontsize=11, fontweight="bold", color="white")

    # ---- Pernos de anclaje (pasan por el frame hasta la fundacion) -------
    for x in [1.6, 4.7, 8.4]:
        # cuerpo del perno: pasa de la fundacion al top plate
        ax.plot([x, x], [0.6, y_base_sup], color="black", linewidth=2.5, zorder=3)
        # cabeza del perno por encima del top plate
        ax.plot(x, y_base_sup + 0.06, "k^", markersize=10, zorder=4)

    # ---- Cotas y etiquetas -----------------------------------------------
    # Cota franja inferior (25 mm)
    ax.annotate(
        "", xy=(0.3, 2), xytext=(0.3, 2.5),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
    )
    ax.text(-0.1, 2.25, "25 mm\n(grout)",
            ha="right", va="center", fontsize=10, color="red", fontweight="bold")

    # Cota del frame interno
    ax.annotate(
        "", xy=(0.3, y_base_inf), xytext=(0.3, y_base_sup - altura_top),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
    )
    ax.text(-0.1, (y_base_inf + y_base_sup - altura_top) / 2,
            "Frame\ninterno\n(grout)",
            ha="right", va="center", fontsize=10, color="red", fontweight="bold")

    # Cota fundacion
    ax.annotate(
        "", xy=(10.3, 0), xytext=(10.3, 2),
        arrowprops=dict(arrowstyle="<->", color="black", lw=1.0),
    )
    ax.text(10.5, 1, "Fundacion\nhormigon armado",
            ha="left", va="center", fontsize=9)

    # Etiquetas internas
    ax.text(5, 2.25, "Sikagrout 214 (25 mm nominal)",
            ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(5, (y_base_inf + y_base_sup - altura_top) / 2,
            "Sikagrout 214 — relleno del frame",
            ha="center", va="center", fontsize=10, fontweight="bold")
    # Indicar acero del frame
    ax.text(x_izq - 0.05, y_base_sup + 0.35,
            "Top plate / frame\nacero A36",
            ha="right", va="bottom", fontsize=9, color="#333333")
    # Flecha indicativa al acero
    ax.annotate(
        "", xy=(x_izq, y_base_sup - altura_top / 2),
        xytext=(x_izq - 0.5, y_base_sup + 0.35),
        arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8),
    )

    ax.set_xlim(-1.8, 13)
    ax.set_ylim(-0.5, 6.5)
    save_fig(fig, "fig-6-1.png")


def fig_6_2_alineamiento_laser():
    """Setup esquematico de alineamiento laser bomba-motor."""
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set_aspect("equal")
    ax.axis("off")

    # Bomba
    bomba = Rectangle((0.5, 1), 3, 1.5, facecolor="#5b9bd5", edgecolor="black")
    ax.add_patch(bomba)
    ax.text(2, 1.75, "BOMBA\nBH-06-001", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")

    # Eje bomba (saliente)
    ax.plot([3.5, 4.5], [1.75, 1.75], color="black", linewidth=4)

    # Acoplamiento
    acople_b = Rectangle((4.2, 1.45), 0.4, 0.6, facecolor="#fab619", edgecolor="black")
    ax.add_patch(acople_b)
    acople_m = Rectangle((5.4, 1.45), 0.4, 0.6, facecolor="#fab619", edgecolor="black")
    ax.add_patch(acople_m)
    ax.text(5, 0.9, "Acoplamiento\nNormex E-97",
            ha="center", va="top", fontsize=8)

    # Sensores laser (esquemato)
    ax.plot([4.4, 4.4], [2.1, 2.5], color="red", linewidth=2)
    ax.plot(4.4, 2.5, "rs", markersize=12)
    ax.text(4.4, 2.7, "Sensor A", ha="center", va="bottom",
            fontsize=8, color="red", fontweight="bold")

    ax.plot([5.6, 5.6], [2.1, 2.5], color="red", linewidth=2)
    ax.plot(5.6, 2.5, "rs", markersize=12)
    ax.text(5.6, 2.7, "Sensor B", ha="center", va="bottom",
            fontsize=8, color="red", fontweight="bold")

    # Haz laser entre sensores
    ax.annotate(
        "", xy=(5.5, 2.55), xytext=(4.5, 2.55),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5, ls="--"),
    )

    # Eje motor
    ax.plot([5.5, 6.5], [1.75, 1.75], color="black", linewidth=4)

    # Motor
    motor = Rectangle((6.5, 1), 3, 1.5, facecolor="#70ad47", edgecolor="black")
    ax.add_patch(motor)
    ax.text(8, 1.75, "MOTOR\nWEH 11 kW", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")

    # Baseplate
    baseplate = Rectangle((0.3, 0.5), 9.4, 0.4, facecolor="#4a4a4a", edgecolor="black")
    ax.add_patch(baseplate)
    ax.text(5, 0.7, "Baseplate BD-0502-B",
            ha="center", va="center", fontsize=9, color="white")

    # Tabla de tolerancias (caja al lado)
    tabla_text = (
        "Tolerancia paralelismo (2.955 rpm):\n"
        "  Excelente: 0.02 mm / 100 mm\n"
        "  Aceptable: 0.03 mm / 100 mm\n"
        "Pie cojo maximo: 0.05 mm"
    )
    ax.text(
        5, -0.5, tabla_text,
        ha="center", va="top", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#fff8d6", edgecolor="black"),
    )

    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1.8, 3.5)
    save_fig(fig, "fig-6-2.png")


def fig_7_1_megger_hipot():
    """Esquema de prueba Megger / Hipot sobre motor 11 kW 380 V."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_aspect("equal")
    ax.axis("off")

    # Motor (rectangulo con devanados)
    motor = Rectangle((4, 1.5), 3, 2.5, facecolor="#70ad47", edgecolor="black")
    ax.add_patch(motor)
    ax.text(5.5, 3.75, "MOTOR 11 kW\n380 V / 50 Hz",
            ha="center", va="center", fontsize=10, fontweight="bold", color="white")

    # Devanados (3 fases)
    for i, fase in enumerate(["U", "V", "W"]):
        ax.plot(4.5 + i * 1, 1.5, "ko", markersize=10)
        ax.text(4.5 + i * 1, 1.2, fase, ha="center", va="top", fontsize=10, fontweight="bold")
        # Cable hacia abajo
        ax.plot([4.5 + i * 1, 4.5 + i * 1], [1.5, 0.5], color="black", linewidth=1.5)
    # Punto comun (unir las 3 fases)
    ax.plot([4.5, 6.5], [0.5, 0.5], color="black", linewidth=1.5)
    ax.plot(5.5, 0.5, "ko", markersize=8)

    # Megger / Hipot (caja)
    megger = Rectangle((0.5, 0.5), 2.5, 1.5, facecolor="#ffc000", edgecolor="black")
    ax.add_patch(megger)
    ax.text(1.75, 1.25, "MEGGER\n1.000 V CC\no\nHIPOT 1.760 V",
            ha="center", va="center", fontsize=9, fontweight="bold")

    # Conector positivo de Megger -> punto comun
    ax.plot([3, 5.5], [1, 0.5], color="red", linewidth=2)
    ax.text(4.5, 0.7, "L+", color="red", fontsize=9, fontweight="bold")

    # Conector negativo Megger -> tierra (carcasa)
    ax.plot([3, 3.5], [1.5, 4.3], color="black", linewidth=2)
    ax.plot([3.5, 4], [4.3, 4.3], color="black", linewidth=2)
    ax.text(3.3, 3, "Masa\n(carcasa)", ha="center", va="center", fontsize=9)

    # Simbolo de tierra
    ax.plot([1.75, 1.75], [0.5, 0.2], color="black", linewidth=2)
    ax.plot([1.4, 2.1], [0.2, 0.2], color="black", linewidth=2.5)
    ax.plot([1.5, 2.0], [0.05, 0.05], color="black", linewidth=2)
    ax.plot([1.6, 1.9], [-0.1, -0.1], color="black", linewidth=2)
    ax.text(1.75, -0.4, "Tierra del banco",
            ha="center", va="center", fontsize=8)

    # Criterio
    ax.text(
        7.5, 1, "Criterio (IEEE 43):\nR_aisl > 1.4 MOhm\n(corregido a 40 C)\nPI = R600 / R60 > 2",
        ha="left", va="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff8d6", edgecolor="black"),
    )

    ax.set_xlim(-0.5, 11)
    ax.set_ylim(-1, 5)
    save_fig(fig, "fig-7-1.png")


def fig_8_1_itp_flujo():
    """Diagrama de flujo del ITP integrado (cajas + flechas)."""
    fig, ax = plt.subplots(figsize=(8, 11))
    ax.set_aspect("equal")
    ax.axis("off")

    hitos = [
        ("H1 — Movilizacion", "#bdd7ee"),
        ("H2 — Aceptacion de fundacion (CC)", "#ffc7ce"),
        ("H3 — Posicionamiento estanque", "#bdd7ee"),
        ("H4 — Verticalidad y apriete pernos (CC)", "#ffc7ce"),
        ("H5 — Prueba hidrostatica estanque (TP)", "#fff2cc"),
        ("H6 — Nivelacion baseplate bomba (CC)", "#ffc7ce"),
        ("H7 — Aplicacion grout 25 mm", "#bdd7ee"),
        ("H8 — Alineamiento bomba-motor (3 mediciones)", "#bdd7ee"),
        ("H9 — Recepcion provisional + punch list", "#fff2cc"),
        ("H10 — Recepcion final", "#c6e0b4"),
    ]

    n = len(hitos)
    y_top = 10
    y_bot = 0
    paso = (y_top - y_bot) / (n - 1)

    posiciones = []
    for i, (label, color) in enumerate(hitos):
        y = y_top - i * paso
        rect = Rectangle((1, y - 0.35), 6, 0.7,
                         facecolor=color, edgecolor="black", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(4, y, label, ha="center", va="center", fontsize=10, fontweight="bold")
        posiciones.append(y)

    # Flechas entre hitos
    for i in range(n - 1):
        ax.annotate(
            "", xy=(4, posiciones[i + 1] + 0.35),
            xytext=(4, posiciones[i] - 0.35),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
        )

    # Leyenda
    leyenda_y = -0.8
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.3), 0.5, 0.5,
                           facecolor="#ffc7ce", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "CC = Punto de retencion (Hold Point)",
            ha="left", va="center", fontsize=9)

    leyenda_y -= 0.7
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.3), 0.5, 0.5,
                           facecolor="#fff2cc", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "TP = Punto de presenciado (Witness Point)",
            ha="left", va="center", fontsize=9)

    leyenda_y -= 0.7
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.3), 0.5, 0.5,
                           facecolor="#bdd7ee", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "Actividad de ejecucion",
            ha="left", va="center", fontsize=9)

    ax.set_xlim(0, 8)
    ax.set_ylim(-3, 11)
    save_fig(fig, "fig-8-1.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Generando figuras...")
    print("  [paso 1] anexos y recortes de planos")
    generar_anexos_y_recortes_planos()
    print("  [paso 2] diagramas conceptuales")
    fig_4_2_patron_apriete()
    fig_6_1_baseplate_grout()
    fig_6_2_alineamiento_laser()
    # fig_7_1_megger_hipot()  # RETIRADO Rev 0: pruebas electricas fuera de alcance
    fig_8_1_itp_flujo()
    print("Listo.")


if __name__ == "__main__":
    main()
