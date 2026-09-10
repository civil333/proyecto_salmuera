#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara las cinco laminas que L&A reemitio en la ENTREGA 15 (carta 067-032-032-COR-TT-016,
10-09-2026) contra la Rev 1 anterior de cada una (ENTREGA 12, TT-013, para las de fundaciones;
ENTREGA 14, TT-015, para las de movimiento de tierra). Las dos emisiones llevan la misma
revision, de modo que la unica forma de saber que cambio es superponer los renders.

Por lamina:
  - render de la version anterior y de la nueva al mismo tamano (150 dpi, con la rotacion
    de pagina aplicada, que es como se ve el plano);
  - superposicion: la anterior en rojo y la nueva en cian, asi lo que no cambio queda gris
    y lo que cambio aparece en color;
  - mascara de diferencia por cuadricula de 6 x 4 celdas, con la fraccion de pixeles que
    cambian en cada celda, y recorte de cada celda con cambio desde el render nuevo, para
    leer ahi el valor.

Salida en <ENTREGA 15>/md/diff/: <lamina>_overlay.png, <lamina>_zona_fC.png y RESUMEN_DIFF.md.
No toca el paquete ni las entregas. large-pdf-reader no compara revisiones (propuesta v9):
este script cubre ese hueco para este caso.
"""
import sys
from pathlib import Path

import fitz
from PIL import Image, ImageChops, ImageFilter

PROY = Path(__file__).resolve().parents[4]
ENT = PROY / "INGENIERIA DE DETALLE OOCC" / "P22-TR-00-010-01-0" / "ENTREGAS"
E12 = ENT / "ENTREGA 12 (ACTUALIZACION NPT)" / "2026-09-03 TT-013 GEN, PL+3D Rev.1" / "Planos"
E14 = ENT / "ENTREGA 14" / "Planos"
E15 = ENT / "ENTREGA 15" / "2026-09-10 TT-016 CIV, Act. PL (coment.) Rev.1" / "Planos"
OUT = E15.parent / "md" / "diff"

DPI = 150
DPI_RECORTE = 300      # los recortes de celda se sacan de un render mas fino, para leer cotas
GRID = (6, 4)            # columnas x filas
UMBRAL_PIXEL = 60        # diferencia de gris que cuenta como cambio
UMBRAL_CELDA = 0.0005    # fraccion de pixeles cambiados (ya dilatados) para declarar la celda

PARES = [
    # (anterior, nueva, rotulo)
    (E14 / "P22-DWG-00-001-001-1-LAM 1.pdf", E15 / "P22-DWG-00-001-001-1-LAM 1.pdf", "00-001-001 LAM1"),
    (E14 / "P22-DWG-00-001-001-1-LAM 2.pdf", E15 / "P22-DWG-00-001-001-1-LAM 2.pdf", "00-001-001 LAM2"),
    (E12 / "P22-DWG-00-002-002_1 LAM1.pdf", E15 / "P22-DWG-00-002-002_1 LAM1.pdf", "00-002-002 LAM1"),
    (E12 / "P22-DWG-00-002-003_1 LAM1.pdf", E15 / "P22-DWG-00-002-003_1 LAM1.pdf", "00-002-003 LAM1"),
    (E12 / "P22-DWG-00-002-007_1 LAM1.pdf", E15 / "P22-DWG-00-002-007_1 LAM1.pdf", "00-002-007 LAM1"),
]


def render(pdf: Path, dpi: int) -> Image.Image:
    page = fitz.open(pdf)[0]
    pm = page.get_pixmap(dpi=dpi, alpha=False)
    return Image.frombytes("RGB", (pm.width, pm.height), pm.samples)


def comparar(anterior: Path, nueva: Path, rotulo: str) -> list[str]:
    a = render(anterior, DPI).convert("L")
    b = render(nueva, DPI).convert("L")
    if a.size != b.size:
        return [f"## {rotulo}", f"Tamanos distintos: {a.size} contra {b.size}. No se compara.", ""]
    tag = nueva.stem.replace(" ", "_")

    # Superposicion: anterior en rojo, nueva en cian. Lo comun queda gris.
    Image.merge("RGB", (a, b, b)).save(OUT / f"{tag}_overlay.png")

    # Mascara: diferencia absoluta y umbral. Se prueban dos limpiezas y se elige segun el par:
    #   - dilatacion (MaxFilter): un digito cambiado pesa en su celda; sirve cuando las dos
    #     emisiones salen del mismo ploteo y lo comun es pixel-identico (fundaciones, Ghostscript);
    #   - erosion (MinFilter): borra los trazos finos; sirve cuando el ploteo nuevo viene
    #     desplazado o reescalado y la dilatacion declara cambio en toda la lamina.
    # Regla: si con dilatacion mas de la mitad de las celdas superan el 5 %, el par esta
    # desplazado y manda la erosion. Umbral calibrado contra las laminas de la ENTREGA 15.
    bruto = ImageChops.difference(a, b).point(lambda v: 255 if v > UMBRAL_PIXEL else 0)
    dil = bruto.filter(ImageFilter.MaxFilter(5))
    W, H = dil.size
    cols, filas = GRID
    cw, ch = W / cols, H / filas
    altas = 0
    for f in range(filas):
        for c in range(cols):
            celda = dil.crop((int(c * cw), int(f * ch), int((c + 1) * cw), int((f + 1) * ch)))
            if sum(1 for v in celda.getdata() if v) / (celda.size[0] * celda.size[1]) > 0.05:
                altas += 1
    if altas > cols * filas / 2:
        dif, metodo, umbral = bruto.filter(ImageFilter.MinFilter(3)), "erosion (par desplazado)", 0.002
    else:
        dif, metodo, umbral = dil, "dilatacion", UMBRAL_CELDA
    lineas = [f"## {rotulo}", "", f"Anterior: `{anterior.relative_to(ENT)}`  ", f"Nueva: `{nueva.relative_to(ENT)}`", "",
              f"Limpieza de la mascara: {metodo}.", "",
              "| Celda (fila, col) | Pixeles cambiados | Recorte |", "|---|---|---|"]
    total = 0
    color = render(nueva, DPI_RECORTE)
    k = DPI_RECORTE / DPI
    for f in range(filas):
        for c in range(cols):
            caja = (int(c * cw), int(f * ch), int((c + 1) * cw), int((f + 1) * ch))
            celda = dif.crop(caja)
            n = sum(1 for v in celda.getdata() if v)
            frac = n / (celda.size[0] * celda.size[1])
            if frac >= umbral:
                total += 1
                nombre = f"{tag}_zona_f{f + 1}c{c + 1}.png"
                color.crop(tuple(int(v * k) for v in caja)).save(OUT / nombre)
                lineas.append(f"| f{f + 1} c{c + 1} | {frac * 100:.2f} % | `{nombre}` |")
    if total == 0:
        lineas.append("| (ninguna) | - | - |")
    lineas += ["", f"Celdas con cambio: {total} de {cols * filas}. Cuadricula {cols} x {filas} sobre "
               f"{W} x {H} px a {DPI} dpi; celda de {int(cw)} x {int(ch)} px.", ""]
    return lineas


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    doc = ["# Comparacion de las laminas reemitidas en la ENTREGA 15 (TT-016) contra su Rev 1 anterior", "",
           "Generado por `comparar_reemision_e15.py`. La superposicion pinta la version anterior en rojo y la nueva "
           "en cian: lo que no cambio queda gris. Las celdas con cambio se recortan del render nuevo para leer el valor.", ""]
    for anterior, nueva, rotulo in PARES:
        if not anterior.exists() or not nueva.exists():
            doc += [f"## {rotulo}", f"Falta un archivo: {anterior.exists()} / {nueva.exists()}", ""]
            continue
        doc += comparar(anterior, nueva, rotulo)
        print("comparada", rotulo)
    (OUT / "RESUMEN_DIFF.md").write_text("\n".join(doc), encoding="utf-8")
    print("resumen en", OUT / "RESUMEN_DIFF.md")


if __name__ == "__main__":
    main()
