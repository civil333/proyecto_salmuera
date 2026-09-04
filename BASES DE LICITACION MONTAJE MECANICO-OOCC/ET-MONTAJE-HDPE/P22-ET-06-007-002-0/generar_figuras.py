#!/usr/bin/env python3
"""
Genera los 9 PNG de figuras conceptuales para la ET de Montaje de Canerias
Plasticas P22-ET-06-007-002-0.

Salidas (todas a 300 dpi):
  figuras/fig-3-1.png  Almacenamiento tipico de tuberia HDPE
  figuras/fig-4-1.png  Secuencia operativa de electrofusion
  figuras/fig-5-3.png  Detalle union brida + stub end + lap joint
  figuras/fig-6-1.png  Tipologia de soportes (clip, anclaje fijo, guia)
  figuras/fig-6-2.png  Loop de dilatacion y brazo flexible
  figuras/fig-8-1.png  Anillos de identificacion y banderas RAL
  figuras/fig-9-1.png  Curva ASTM F2164 presion vs tiempo
  figuras/fig-11-1.png Diagrama de flujo del ITP

Diagramas conceptuales con matplotlib (primitivas Rectangle, FancyArrowPatch,
Polygon, Circle). Sin dependencias externas no estandar.
"""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import (
    FancyArrowPatch,
    Polygon,
    Rectangle,
    Circle,
    FancyBboxPatch,
    Arc,
)
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURAS_DIR = os.path.join(SCRIPT_DIR, "figuras")
os.makedirs(FIGURAS_DIR, exist_ok=True)


def save_fig(fig, name, dpi=300):
    path = os.path.join(FIGURAS_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [ok] {name}")


# ---------------------------------------------------------------------------
# Figura 3.1 - Almacenamiento HDPE
# ---------------------------------------------------------------------------
def fig_3_1_almacenamiento():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_aspect("equal")
    ax.axis("off")

    # Suelo (cunas de madera)
    for x in [0.5, 4, 7.5]:
        ax.add_patch(Rectangle((x, 0), 1.5, 0.2, facecolor="#a0522d", edgecolor="black"))
        ax.text(x + 0.75, -0.2, "Cuna\nmadera", ha="center", va="top", fontsize=8)

    # Apilamiento de tubos (DN100 abajo, DN80 medio, DN50 arriba)
    # Tubos DN100 (mayor)
    for i, x in enumerate([0.7, 1.4, 2.1]):
        ax.add_patch(Circle((x, 0.55), 0.35, facecolor="#262626", edgecolor="black"))
    ax.text(1.4, 0.55, "DN100", ha="center", va="center", fontsize=7, color="white", fontweight="bold")

    for i, x in enumerate([4.3, 4.9, 5.5]):
        ax.add_patch(Circle((x, 0.55), 0.3, facecolor="#262626", edgecolor="black"))
    ax.text(4.9, 0.55, "DN80", ha="center", va="center", fontsize=7, color="white", fontweight="bold")

    for x in [7.7, 8.1, 8.5]:
        ax.add_patch(Circle((x, 0.45), 0.2, facecolor="#262626", edgecolor="black"))
    ax.text(8.1, 0.45, "DN50", ha="center", va="center", fontsize=6, color="white", fontweight="bold")

    # Carpa opaca (linea curva por encima)
    xs = np.linspace(0, 10, 50)
    ys = 2.2 + 0.3 * np.cos(np.pi * (xs - 5) / 5)
    ax.plot(xs, ys, color="#3b6b3b", linewidth=3)
    ax.fill_between(xs, ys, ys + 0.05, color="#3b6b3b")
    ax.text(5, 2.55, "Carpa opaca anti-UV (almacenamiento > 30 dias)",
            ha="center", va="bottom", fontsize=10, fontweight="bold", color="#3b6b3b")

    # Tapas plasticas en extremos
    ax.add_patch(Circle((0.35, 0.55), 0.35, facecolor="#f0a020", edgecolor="black"))
    ax.text(0.35, 1.2, "Tapa\nplastica", ha="center", va="bottom", fontsize=7, color="#a05000")

    # Indicacion altura maxima
    ax.annotate(
        "", xy=(10.3, 0.2), xytext=(10.3, 0.9),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
    )
    ax.text(10.5, 0.55, "Altura max\nsegun fabricante\n(ref. 1,5 m DN100)",
            ha="left", va="center", fontsize=9, color="red", fontweight="bold")

    ax.set_xlim(-0.5, 13)
    ax.set_ylim(-0.8, 3.2)
    save_fig(fig, "fig-3-1.png")


# ---------------------------------------------------------------------------
# Figura 4.1 - Secuencia electrofusion
# ---------------------------------------------------------------------------
def fig_4_1_electrofusion():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    pasos = [
        ("1. Corte y\nraspado", "tubo"),
        ("2. Marca de\nprofundidad", "tubo_marca"),
        ("3. Ensamble en\naccesorio + ciclo", "ensamble"),
        ("4. Verificar\npop-ups + enfriar", "popups"),
    ]
    for ax, (titulo, kind) in zip(axes, pasos):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-1, 5)
        ax.set_ylim(-1, 4)
        ax.set_title(titulo, fontsize=11, fontweight="bold", pad=10)

        if kind == "tubo":
            # Tubo con raspador
            ax.add_patch(Rectangle((0, 1.5), 4, 1, facecolor="#3a3a3a", edgecolor="black"))
            ax.add_patch(Rectangle((0, 1.5), 0.05, 1, facecolor="#a0a0a0"))  # corte
            ax.add_patch(Rectangle((3.95, 1.5), 0.05, 1, facecolor="#a0a0a0"))
            # raspador
            ax.add_patch(Rectangle((1, 2.55), 0.6, 0.3, facecolor="#c00000", edgecolor="black"))
            ax.text(1.3, 3.2, "Raspador", ha="center", fontsize=8, color="#c00000")
            ax.text(2, 1.3, "Eliminar capa de oxido", ha="center", fontsize=8)

        elif kind == "tubo_marca":
            ax.add_patch(Rectangle((0, 1.5), 4, 1, facecolor="#3a3a3a", edgecolor="black"))
            # Marca de profundidad
            ax.plot([2.5, 2.5], [1.3, 2.7], color="red", linewidth=2)
            ax.text(2.5, 1.1, "Marca\nprofundidad", ha="center", fontsize=8, color="red")

        elif kind == "ensamble":
            # Accesorio (envolvente)
            ax.add_patch(Rectangle((0.5, 1), 3, 2, facecolor="#3a3a3a", edgecolor="black"))
            ax.add_patch(Rectangle((1, 1.4), 2, 1.2, facecolor="#ffd040", edgecolor="black"))
            ax.text(2, 2, "Accesorio EF\n(resistencia\nintegrada)",
                    ha="center", va="center", fontsize=8, fontweight="bold")
            # Cable a maquina
            ax.plot([0.5, -0.3], [3.0, 3.5], color="red", linewidth=2)
            ax.plot([3.5, 4.3], [3.0, 3.5], color="black", linewidth=2)
            ax.add_patch(Rectangle((3.8, 3.4), 0.8, 0.4, facecolor="#5b9bd5", edgecolor="black"))
            ax.text(4.2, 3.6, "Maquina\nEF", ha="center", va="center", fontsize=7,
                    color="white", fontweight="bold")

        elif kind == "popups":
            ax.add_patch(Rectangle((0.5, 1), 3, 2, facecolor="#3a3a3a", edgecolor="black"))
            ax.add_patch(Rectangle((1, 1.4), 2, 1.2, facecolor="#ffd040", edgecolor="black"))
            # Pop-ups
            ax.add_patch(Circle((1.5, 3.05), 0.12, facecolor="#c00000", edgecolor="black"))
            ax.add_patch(Circle((2.5, 3.05), 0.12, facecolor="#c00000", edgecolor="black"))
            ax.text(1.5, 3.4, "PUSH UP", ha="center", fontsize=8, color="red", fontweight="bold")
            ax.text(2.5, 3.4, "PUSH UP", ha="center", fontsize=8, color="red", fontweight="bold")
            ax.text(2, 0.6, "Ambos pop-ups emergidos = OK", ha="center", fontsize=8, fontweight="bold")

    fig.suptitle("Secuencia de electrofusion (4 pasos clave)", fontsize=12, fontweight="bold", y=1.02)
    save_fig(fig, "fig-4-1.png")


# ---------------------------------------------------------------------------
# Figura 5.3 - Union brida + stub end + lap joint
# ---------------------------------------------------------------------------
def fig_5_3_brida_stub():
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_aspect("equal")
    ax.axis("off")

    # Tubo HDPE 1
    ax.add_patch(Rectangle((0, 1.5), 4, 1.5, facecolor="#262626", edgecolor="black"))
    # Stub end 1 (con collar)
    ax.add_patch(Polygon([(4, 1.5), (4, 3.0), (4.4, 3.4), (4.4, 1.1)],
                         facecolor="#262626", edgecolor="black"))
    ax.add_patch(Rectangle((4.4, 1.0), 0.3, 2.5, facecolor="#262626", edgecolor="black"))
    # Brida loca 1
    ax.add_patch(Rectangle((4.0, 0.6), 0.4, 3.3, facecolor="#909090", edgecolor="black"))
    # Junta
    ax.add_patch(Rectangle((4.7, 1.0), 0.15, 2.5, facecolor="#ff6060", edgecolor="black"))
    # Brida loca 2
    ax.add_patch(Rectangle((4.85, 0.6), 0.4, 3.3, facecolor="#909090", edgecolor="black"))
    # Stub end 2
    ax.add_patch(Rectangle((4.85, 1.0), 0.3, 2.5, facecolor="#262626", edgecolor="black"))
    ax.add_patch(Polygon([(5.15, 1.1), (5.55, 1.5), (5.55, 3.0), (5.15, 3.4)],
                         facecolor="#262626", edgecolor="black"))
    # Tubo HDPE 2
    ax.add_patch(Rectangle((5.55, 1.5), 4, 1.5, facecolor="#262626", edgecolor="black"))

    # Pernos (esparragos pasando por las dos bridas)
    for y in [0.9, 1.4, 1.9, 2.4, 2.9, 3.4]:
        ax.plot([3.95, 5.30], [y, y], color="#404040", linewidth=2)
        ax.add_patch(Circle((3.95, y), 0.08, facecolor="#606060", edgecolor="black"))
        ax.add_patch(Circle((5.30, y), 0.08, facecolor="#606060", edgecolor="black"))

    # Etiquetas
    ax.annotate("Tubo HDPE PE100", xy=(2, 2.25), xytext=(2, 4.2),
                ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.annotate("Stub end (PE100,\nfusionado al tubo)", xy=(4.3, 2.0), xytext=(2.5, 0.0),
                ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.annotate("Lap joint\n(brida loca,\nacero)", xy=(4.2, 3.6), xytext=(3.0, 4.5),
                ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.annotate("Junta plana\nNBR/SBR 1/8\"\nFull Face", xy=(4.78, 2.25), xytext=(6.5, 4.5),
                ha="center", fontsize=9, color="red",
                arrowprops=dict(arrowstyle="->", color="red"))
    ax.annotate("Esparragos\nA193 Gr.B8M Cl.2\n(SS316)", xy=(5.30, 0.9), xytext=(7.5, 0.0),
                ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))

    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-1.0, 5.5)
    save_fig(fig, "fig-5-3.png")


# ---------------------------------------------------------------------------
# Figura 6.1 - Tipologia de soportes
# ---------------------------------------------------------------------------
def fig_6_1_soportes():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    titulos = [
        ("Clip deslizante", "deslizante"),
        ("Anclaje fijo", "fijo"),
        ("Guia direccional", "guia"),
    ]
    for ax, (titulo, kind) in zip(axes, titulos):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-1, 5)
        ax.set_ylim(-1, 5)
        ax.set_title(titulo, fontsize=12, fontweight="bold")

        # Estructura de soporte (arriba)
        ax.add_patch(Rectangle((-0.5, 4), 5, 0.3, facecolor="#5b5b5b", edgecolor="black"))

        # Tubo
        ax.add_patch(Rectangle((0, 1.8), 4.5, 1, facecolor="#262626", edgecolor="black"))

        if kind == "deslizante":
            # Clip que abraza pero no fija longitudinalmente
            ax.add_patch(Polygon([(1.7, 4), (1.7, 2.4), (1.4, 2.4),
                                  (1.4, 2.1), (3.0, 2.1), (3.0, 2.4),
                                  (2.7, 2.4), (2.7, 4)],
                                 facecolor="#a05000", edgecolor="black", alpha=0.7))
            # Flecha indicando movimiento longitudinal
            ax.annotate("", xy=(3.6, 2.3), xytext=(0.7, 2.3),
                        arrowprops=dict(arrowstyle="<->", color="blue", lw=2))
            ax.text(2.2, 1.2, "Permite movimiento\nlongitudinal", ha="center",
                    fontsize=9, color="blue")

        elif kind == "fijo":
            # Anclaje en forma de cuna con tornilleria
            ax.add_patch(Polygon([(1.5, 4), (1.5, 2.4), (1.2, 2.4),
                                  (1.2, 1.7), (3.2, 1.7), (3.2, 2.4),
                                  (2.9, 2.4), (2.9, 4)],
                                 facecolor="#c00000", edgecolor="black"))
            # Pernos
            ax.add_patch(Circle((1.5, 4.15), 0.08, facecolor="black"))
            ax.add_patch(Circle((2.9, 4.15), 0.08, facecolor="black"))
            # X de bloqueo
            ax.plot([0.7, 3.6], [2.3, 2.3], "x", color="red", markersize=15, markeredgewidth=3)
            ax.text(2.2, 1.2, "Restringe movimiento\nlongitudinal", ha="center",
                    fontsize=9, color="red")

        elif kind == "guia":
            ax.add_patch(Polygon([(1.7, 4), (1.7, 2.4), (1.4, 2.4),
                                  (1.4, 2.1), (3.0, 2.1), (3.0, 2.4),
                                  (2.7, 2.4), (2.7, 4)],
                                 facecolor="#3a8030", edgecolor="black", alpha=0.7))
            # Flecha permitida (longitudinal)
            ax.annotate("", xy=(3.6, 2.3), xytext=(0.7, 2.3),
                        arrowprops=dict(arrowstyle="<->", color="blue", lw=2))
            # Flecha prohibida (lateral)
            ax.plot(2.2, 3.3, "X", color="red", markersize=20, markeredgewidth=3)
            ax.text(2.2, 1.2, "Permite longitudinal,\nrestringe lateral", ha="center",
                    fontsize=9, color="#3a8030")

        # Suelo
        ax.add_patch(Rectangle((-0.5, -0.5), 5, 0.3, facecolor="#bdbdbd", edgecolor="black"))
        for x in np.linspace(-0.5, 4.5, 12):
            ax.plot([x, x + 0.2], [-0.5, -0.2], color="gray", linewidth=0.3)

    save_fig(fig, "fig-6-1.png")


# ---------------------------------------------------------------------------
# Figura 6.2 - Loop de dilatacion
# ---------------------------------------------------------------------------
def fig_6_2_loop():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.set_aspect("equal")
    ax.axis("off")

    # Tubo entrante
    ax.add_patch(Rectangle((0, 1.5), 3, 0.6, facecolor="#262626", edgecolor="black"))
    # Codos y brazos del loop
    # Codo subida
    ax.add_patch(FancyBboxPatch((3, 1.5), 0.6, 0.6,
                                 boxstyle="round,pad=0.02", facecolor="#262626", edgecolor="black"))
    # Brazo vertical 1
    ax.add_patch(Rectangle((3, 2.1), 0.6, 1.5, facecolor="#262626", edgecolor="black"))
    # Codo superior izq
    ax.add_patch(FancyBboxPatch((3, 3.6), 0.6, 0.6,
                                 boxstyle="round,pad=0.02", facecolor="#262626", edgecolor="black"))
    # Brazo horizontal superior
    ax.add_patch(Rectangle((3.6, 3.6), 3.5, 0.6, facecolor="#262626", edgecolor="black"))
    # Codo superior der
    ax.add_patch(FancyBboxPatch((7.1, 3.6), 0.6, 0.6,
                                 boxstyle="round,pad=0.02", facecolor="#262626", edgecolor="black"))
    # Brazo vertical 2
    ax.add_patch(Rectangle((7.1, 2.1), 0.6, 1.5, facecolor="#262626", edgecolor="black"))
    # Codo bajada
    ax.add_patch(FancyBboxPatch((7.1, 1.5), 0.6, 0.6,
                                 boxstyle="round,pad=0.02", facecolor="#262626", edgecolor="black"))
    # Tubo saliente
    ax.add_patch(Rectangle((7.7, 1.5), 3, 0.6, facecolor="#262626", edgecolor="black"))

    # Anclajes fijos (en los extremos del loop)
    for x in [0.3, 10.3]:
        ax.add_patch(Polygon([(x, 0.8), (x - 0.3, 1.3), (x + 0.3, 1.3)],
                             facecolor="#c00000", edgecolor="black"))
        ax.text(x, 0.5, "Anclaje\nfijo", ha="center", va="top", fontsize=8, color="red", fontweight="bold")

    # Cotas
    ax.annotate("", xy=(7.4, 4.5), xytext=(3.4, 4.5),
                arrowprops=dict(arrowstyle="<->", color="blue", lw=1.5))
    ax.text(5.4, 4.7, "Brazo horizontal (L_loop)", ha="center", fontsize=10, color="blue", fontweight="bold")

    ax.annotate("", xy=(8.2, 2.0), xytext=(8.2, 4.2),
                arrowprops=dict(arrowstyle="<->", color="blue", lw=1.5))
    ax.text(8.4, 3.1, "Brazo vertical", ha="left", fontsize=10, color="blue")

    # Dilatacion esquematica
    ax.annotate("", xy=(2.8, 1.0), xytext=(0.5, 1.0),
                arrowprops=dict(arrowstyle="->", color="green", lw=2))
    ax.text(1.6, 0.7, "Δ L = α·L·Δ T", ha="center", fontsize=10, color="green", fontweight="bold")

    ax.text(5.4, 0.0, "Loop de dilatacion absorbe Δ L entre anclajes fijos",
            ha="center", fontsize=11, fontweight="bold")

    ax.set_xlim(-0.5, 12)
    ax.set_ylim(-0.7, 5.5)
    save_fig(fig, "fig-6-2.png")


# ---------------------------------------------------------------------------
# Figura 8.1 - Anillos de identificacion y flechas direccionales
# (la tuberia HDPE NO se pinta; se identifica con anillos prefabricados y
#  flechas autoadhesivas en los colores RAL del servicio)
# ---------------------------------------------------------------------------
def fig_8_1_bandas():
    fig, ax = plt.subplots(figsize=(14, 6.5))
    ax.set_aspect("equal")
    ax.axis("off")

    # 3 servicios reales del proyecto Taltal (segun LI Lineas)
    servicios = [
        ("SA", "SALMUERA OI", "#4F7942", "Verde RAL 6018"),
        ("PE", "PERMEADO OI", "#8FBFC4", "Celeste RAL 6027"),
        ("DR", "DRENAJE", "#5C6266", "Gris RAL 7011"),
    ]
    y0 = 4
    for i, (codigo, leyenda, color, ral) in enumerate(servicios):
        y = y0 - i * 1.5
        # Tubo HDPE (color negro de fabrica con CB UV)
        ax.add_patch(Rectangle((1, y), 11, 0.7, facecolor="#262626", edgecolor="black"))

        # Anillo de identificacion (estrecho, aplicado sobre el tubo)
        anillo_x = 4.5
        anillo_w = 0.7
        ax.add_patch(Rectangle((anillo_x, y - 0.1), anillo_w, 0.9,
                                facecolor=color, edgecolor="black", linewidth=1.5))
        # Leyenda del fluido sobre el anillo (texto blanco)
        ax.text(anillo_x + anillo_w / 2, y + 0.35, codigo,
                ha="center", va="center",
                fontsize=11, color="white", fontweight="bold")

        # Flecha direccional autoadhesiva en el color del servicio,
        # contigua al anillo, integrada en una etiqueta blanca
        flecha_x0 = anillo_x + anillo_w + 0.3
        flecha_x1 = flecha_x0 + 2.2
        # Fondo blanco de la etiqueta de flecha
        ax.add_patch(Rectangle((flecha_x0, y + 0.05), flecha_x1 - flecha_x0, 0.6,
                                facecolor="white", edgecolor="black", linewidth=1))
        # Texto del fluido en el color del servicio
        ax.text(flecha_x0 + 0.7, y + 0.35, leyenda,
                ha="center", va="center",
                fontsize=8, color=color, fontweight="bold")
        # Flecha direccional en el color del servicio
        arrow = FancyArrowPatch(
            (flecha_x0 + 1.4, y + 0.35),
            (flecha_x1 - 0.1, y + 0.35),
            arrowstyle="->", mutation_scale=18, color=color, linewidth=2.5,
        )
        ax.add_patch(arrow)

        # Etiqueta lateral (codigo de servicio)
        ax.text(0.6, y + 0.35, codigo, ha="right", va="center",
                fontsize=11, fontweight="bold")
        # Etiqueta lateral derecha (RAL)
        ax.text(12.3, y + 0.35, ral, ha="left", va="center",
                fontsize=9, color="#404040")

    # Cota intervalo
    ax.annotate("", xy=(11.5, 5.3), xytext=(4.5, 5.3),
                arrowprops=dict(arrowstyle="<->", color="blue", lw=1.5))
    ax.text(8.0, 5.55, "Intervalo maximo 10 m entre anillos + en cada cambio de direccion",
            ha="center", fontsize=10, color="blue", fontweight="bold")

    # Nota inferior
    ax.text(7, -0.9,
            "La tuberia HDPE NO se pinta. Identificacion por anillos prefabricados "
            "(PVC u otro polimero compatible) o etiquetas\n"
            "autoadhesivas de polietileno con adhesivo de larga duracion, en el "
            "color RAL del servicio.",
            ha="center", fontsize=10, fontweight="bold")

    ax.set_xlim(-0.5, 15)
    ax.set_ylim(-1.5, 6)
    save_fig(fig, "fig-8-1.png")


# ---------------------------------------------------------------------------
# Figura 9.1 - Curva ASTM F2164
# ---------------------------------------------------------------------------
def fig_9_1_f2164():
    fig, ax = plt.subplots(figsize=(11, 6))

    PDO = 10
    PDP = 15
    P_recovery = 0.1 * PDO

    # Tiempo en horas
    t_init_end = 1.5      # 30 min a 3 h (uso 1.5 h tipico)
    t_test_end = t_init_end + 2.0   # 1 a 3 h (uso 2 h)
    t_recovery_start = t_test_end + 0.05  # transicion rapida
    t_recovery_end = t_recovery_start + 1.0

    t = [0, 0.3, t_init_end, t_test_end, t_recovery_start, t_recovery_end]
    p = [0, PDP, PDP, PDP * 0.97, P_recovery, P_recovery * 1.5]

    ax.plot(t, p, color="#c00000", linewidth=2.5, marker="o", markersize=7, label="Presion en la red")
    ax.fill_between(t, 0, p, color="#c00000", alpha=0.08)

    # Lineas horizontales de referencia
    ax.axhline(y=PDP, color="green", linestyle="--", linewidth=1)
    ax.axhline(y=PDO, color="blue", linestyle="--", linewidth=1)
    ax.axhline(y=P_recovery, color="purple", linestyle="--", linewidth=1)
    ax.text(t_recovery_end + 0.1, PDP, "PDP = 1.5 × PDO = 15 bar", va="center", fontsize=9, color="green")
    ax.text(t_recovery_end + 0.1, PDO, "PDO = 10 bar (PN10)", va="center", fontsize=9, color="blue")
    ax.text(t_recovery_end + 0.1, P_recovery, "0.1 × PDO = 1 bar", va="center", fontsize=9, color="purple")

    # Bandas verticales de fases
    ax.axvspan(0, t_init_end, alpha=0.1, color="orange", label="Initial Expansion (0.5 a 3 h)")
    ax.axvspan(t_init_end, t_test_end, alpha=0.1, color="green", label="Test Phase (1 a 3 h)")
    ax.axvspan(t_test_end, t_recovery_end, alpha=0.1, color="purple", label="Recovery (1 h)")

    ax.text(t_init_end / 2, 16.5, "Initial Expansion\n(make-up permitido)",
            ha="center", fontsize=9, fontweight="bold", color="#a05000")
    ax.text((t_init_end + t_test_end) / 2, 16.5, "Test Phase\n(sin make-up)",
            ha="center", fontsize=9, fontweight="bold", color="#306030")
    ax.text((t_test_end + t_recovery_end) / 2, 16.5, "Recovery\n(rebote ≥ 50%)",
            ha="center", fontsize=9, fontweight="bold", color="#604080")

    ax.set_xlabel("Tiempo (horas)", fontsize=11)
    ax.set_ylabel("Presion (bar)", fontsize=11)
    ax.set_title("Prueba hidrostatica ASTM F2164 — HDPE PE100 PN10", fontsize=12, fontweight="bold")
    ax.set_xlim(0, t_recovery_end + 2)
    ax.set_ylim(0, 18)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=9)

    save_fig(fig, "fig-9-1.png")


# ---------------------------------------------------------------------------
# Figura 11.1 - Diagrama de flujo ITP
# ---------------------------------------------------------------------------
def fig_11_1_itp():
    fig, ax = plt.subplots(figsize=(8, 11.5))
    ax.set_aspect("equal")
    ax.axis("off")

    hitos = [
        ("H1 — Movilizacion", "#bdd7ee"),
        ("H2 — WPS y PQR aprobados (CC)", "#ffc7ce"),
        ("H3 — Operadores calificados (CC)", "#ffc7ce"),
        ("H4 — Recepcion de materiales", "#bdd7ee"),
        ("H5 — Soporteria del tramo principal (CC)", "#ffc7ce"),
        ("H6 — Tramo principal HDPE DN100", "#bdd7ee"),
        ("H7 — Tramos secundarios HDPE/PVC", "#bdd7ee"),
        ("H8 — Hidrostatica ASTM F2164 aceptada (CC)", "#ffc7ce"),
        ("H9 — Flushing aceptado (CC)", "#ffc7ce"),
        ("H10 — Identificacion completada", "#bdd7ee"),
        ("H11 — Recepcion provisional + punch list", "#fff2cc"),
        ("H12 — Recepcion final con dossier as-built", "#c6e0b4"),
    ]

    n = len(hitos)
    y_top = 11
    y_bot = 0
    paso = (y_top - y_bot) / (n - 1)

    posiciones = []
    for i, (label, color) in enumerate(hitos):
        y = y_top - i * paso
        ax.add_patch(Rectangle((0.7, y - 0.32), 6.6, 0.6,
                               facecolor=color, edgecolor="black", linewidth=1.5))
        ax.text(4, y, label, ha="center", va="center", fontsize=10, fontweight="bold")
        posiciones.append(y)

    for i in range(n - 1):
        ax.annotate("", xy=(4, posiciones[i + 1] + 0.32),
                    xytext=(4, posiciones[i] - 0.32),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

    # Leyenda
    leyenda_y = -1.0
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.25), 0.5, 0.4,
                           facecolor="#ffc7ce", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "CC = Punto de retencion (Hold Point)",
            ha="left", va="center", fontsize=9)

    leyenda_y -= 0.6
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.25), 0.5, 0.4,
                           facecolor="#fff2cc", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "Recepcion provisional",
            ha="left", va="center", fontsize=9)

    leyenda_y -= 0.6
    ax.add_patch(Rectangle((0.5, leyenda_y - 0.25), 0.5, 0.4,
                           facecolor="#c6e0b4", edgecolor="black"))
    ax.text(1.2, leyenda_y - 0.05, "Recepcion final",
            ha="left", va="center", fontsize=9)

    ax.set_xlim(0, 8)
    ax.set_ylim(-3, 12)
    save_fig(fig, "fig-11-1.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Generando 8 figuras conceptuales...")
    fig_3_1_almacenamiento()
    fig_4_1_electrofusion()
    fig_5_3_brida_stub()
    fig_6_1_soportes()
    fig_6_2_loop()
    fig_8_1_bandas()
    fig_9_1_f2164()
    fig_11_1_itp()
    print("Listo.")


if __name__ == "__main__":
    main()
