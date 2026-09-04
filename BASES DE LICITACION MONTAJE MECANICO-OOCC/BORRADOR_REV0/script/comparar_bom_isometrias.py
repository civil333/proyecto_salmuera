#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara la LISTA DE MATERIALES de cada par de hojas alineado por comparar_isometrias.py.

Por que por imagen y no por OCR: en estas laminas el cuadro esta vectorizado, y un OCR
celda por celda exige detectar la grilla, cosa que aqui falla porque las verticales
internas del cuadro miden menos que los segmentos del marco de la lamina. Comparar el
recorte como imagen es exacto para responder "cambio o no cambio", y lo que cambia se
lee a ojo sobre el render, que es la unica lectura fiable de un cuadro vectorizado.

Salida: dice por par si el cuadro es identico, si cambio de tamano (cambio el numero de
filas) o si cambio su contenido, y escribe los PNG de los que difieren.
"""
import argparse
import hashlib
from pathlib import Path

import fitz

RAIZ = Path(__file__).resolve().parents[3]
REV0 = RAIZ / "INGENIERIA DE DETALLE MECANICA/ENTREGAS/COMPILADO REV 0/03_CANERIAS/Cuadernillo_de_isometrias"
VIG = (RAIZ / "BASES DE LICITACION MONTAJE MECANICO-OOCC/INGENIERIA VIGENTE PARA CONSTRUCCION"
       / "1. ING. DETALLE MECANICA/03_CANERIAS/Cuadernillo_de_isometrias")
DPI = 150
ALTO_FILA = 33.0     # una fila del cuadro mide ~33 pt
TOL_ALTO = 5.0       # menos que esto es ruido de redondeo, no cambio de filas
TOL_PIX = 0.002      # <0.2% de pixeles distintos = mismo contenido (antialiasing)

# Pares alineados por firma de contenido (ver comparar_isometrias.py).
# OJO: en 006-008 y 006-011 las hojas cambiaron de numero.
PARES = {
    "P22-DWG-06-006-005": [("H.1","H.1"), ("H.2","H.2"), ("H.3","H.3"), ("H.4","H.4")],
    "P22-DWG-06-006-008": [("H.1","H.1"), ("H.2","H.2"), ("H.3","H.3"), ("H.4","H.5")],
    "P22-DWG-06-006-009": [("H.1","H.1"), ("H.2","H.2")],
    "P22-DWG-06-006-011": [("H.1","H.1"), ("H.2","H.3"), ("H.3","H.4"), ("H.4","H.5"),
                           ("H.5","H.6"), ("H.6","H.7"), ("H.7","H.8")],
}
NUEVAS = {"P22-DWG-06-006-005": ["H.5"], "P22-DWG-06-006-008": ["H.4"],
          "P22-DWG-06-006-011": ["H.2"]}


def buscar(carpeta, codigo, hoja):
    for p in carpeta.glob("*.pdf"):
        if p.stem.startswith(codigo) and p.stem.endswith("_" + hoja):
            return p
    return None


def caja_bom(pg):
    W, H = pg.rect.width, pg.rect.height
    mejor, area_m = None, 0
    for it in pg.get_drawings():
        r = it.get("rect")
        if not r or r.x0 < W * 0.55 or r.y0 > H * 0.35:
            continue
        a = abs(r.x1 - r.x0) * abs(r.y1 - r.y0)
        if a < W * H * 0.03:
            continue
        if a > area_m:
            mejor, area_m = r, a
    return mejor


def render_bom(path, out=None):
    d = fitz.open(path)
    pg = d[0]
    caja = caja_bom(pg)
    if caja is None:
        d.close()
        return None, None, None
    pix = pg.get_pixmap(dpi=DPI, clip=caja, colorspace=fitz.csGRAY)
    if out:
        pix.save(str(out))
    alto = round(caja.y1 - caja.y0, 1)
    datos = (pix.width, pix.height, bytes(pix.samples))
    d.close()
    return datos, alto, None


def frac_distinta(a, b):
    """Fraccion de pixeles que difieren, sobre el area comun. None si no comparables."""
    (wa, ha, sa), (wb, hb, sb) = a, b
    if abs(wa - wb) > 2:
        return None
    w = min(wa, wb)
    h = min(ha, hb)
    dif = 0
    for y in range(0, h, 2):                       # muestreo cada 2 filas: 4x mas rapido
        fa, fb = y * wa, y * wb
        for x in range(0, w, 2):
            if abs(sa[fa + x] - sb[fb + x]) > 40:
                dif += 1
    tot = (h // 2 + 1) * (w // 2 + 1)
    return dif / max(tot, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None, help="carpeta donde escribir los PNG que difieren")
    args = ap.parse_args()
    out = Path(args.out) if args.out else None
    if out:
        out.mkdir(parents=True, exist_ok=True)

    difieren = []
    for cod in sorted(PARES):
        print(f"\n{'='*74}\n{cod}")
        for ha, hb in PARES[cod]:
            pa, pb = buscar(REV0, cod, ha), buscar(VIG, cod, hb)
            if not pa or not pb:
                print(f"  {ha:5} -> {hb:5}  !! falta archivo")
                continue
            fa, alto_a, _ = render_bom(pa)
            fb, alto_b, _ = render_bom(pb)
            movida = "  (hoja movida)" if ha != hb else ""
            d_alto = alto_b - alto_a
            if abs(d_alto) > TOL_ALTO:
                nf = round(d_alto / ALTO_FILA)
                signo = "+" if nf > 0 else ""
                print(f"  {ha:5} -> {hb:5}  CAMBIA: {signo}{nf} fila(s)  "
                      f"(alto {alto_a} -> {alto_b}){movida}")
                difieren.append((cod, ha, hb, pa, pb, f"{signo}{nf} filas"))
                continue
            fr = frac_distinta(fa, fb)
            if fr is None:
                print(f"  {ha:5} -> {hb:5}  no comparable{movida}")
            elif fr <= TOL_PIX:
                print(f"  {ha:5} -> {hb:5}  cuadro SIN CAMBIOS  "
                      f"({fr*100:.2f}% pixeles){movida}")
            else:
                print(f"  {ha:5} -> {hb:5}  CAMBIA el contenido, mismo numero de filas  "
                      f"({fr*100:.2f}% pixeles){movida}")
                difieren.append((cod, ha, hb, pa, pb, "mismo alto"))
        for h in NUEVAS.get(cod, []):
            pb = buscar(VIG, cod, h)
            _, alto_b, _ = render_bom(pb) if pb else (None, None, None)
            print(f"  {'':5}    {h:5}  HOJA NUEVA (alto del cuadro {alto_b})")
            if out and pb:
                render_bom(pb, out / f"{cod}_{h}_NUEVA.png")

    print(f"\n{'='*74}\nCuadros de materiales que cambian: {len(difieren)}")
    if out:
        for cod, ha, hb, pa, pb, _ in difieren:
            render_bom(pa, out / f"{cod}_{ha}_rev0.png")
            render_bom(pb, out / f"{cod}_{hb}_vig.png")
        print(f"PNG escritos en {out}")


if __name__ == "__main__":
    main()
