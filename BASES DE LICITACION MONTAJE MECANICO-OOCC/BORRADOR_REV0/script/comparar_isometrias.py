#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara el Cuadernillo de Isometrias de la Rev 0 (COMPILADO) contra la revision vigente
del paquete INGENIERIA VIGENTE PARA CONSTRUCCION.

Por que existe: las isometrias NO tienen capa de texto util. Cada hoja trae unos 700
caracteres que son solo el cajetin; la geometria, las cotas y la Lista de Materiales de
la hoja estan vectorizadas. Todo lo que se afirme sobre el contenido sale de render.

Y sobre todo: entre revisiones LAS HOJAS SE CORRIERON. En P22-DWG-06-006-011 la Rev 2
inserta una lamina en la posicion H.2 y desplaza el resto, de modo que la H.2 de la
Rev 0 es la H.3 vigente. Comparar H.N contra H.N produce un diff enteramente falso, por
lo que las hojas se alinean por FIRMA de contenido y no por numero.

Uso:
    python3 comparar_isometrias.py                # mapeo + diff, salida a stdout
    python3 comparar_isometrias.py --render DIR   # ademas escribe los recortes PNG
"""
import argparse
import hashlib
import sys
from collections import defaultdict
from pathlib import Path

import fitz

RAIZ = Path(__file__).resolve().parents[3]
REV0 = RAIZ / "INGENIERIA DE DETALLE MECANICA/ENTREGAS/COMPILADO REV 0/03_CANERIAS/Cuadernillo_de_isometrias"
VIG = (RAIZ / "BASES DE LICITACION MONTAJE MECANICO-OOCC/INGENIERIA VIGENTE PARA CONSTRUCCION"
       / "1. ING. DETALLE MECANICA/03_CANERIAS/Cuadernillo_de_isometrias")

# Umbral de emparejamiento: dos hojas son la misma lamina si su firma difiere poco.
TOL_VECTORES = 0.25       # 25% de diferencia en conteo de vectores
DPI_FIRMA = 40            # render grueso para el hash perceptual
DPI_DIFF = 150            # render de comparacion


# --------------------------------------------------------------- identificacion
def codigo_y_hoja(p):
    """'P22-DWG-06-006-011-2 (SA-...)_H.3.pdf' -> ('P22-DWG-06-006-011', '2', 'H.3')."""
    stem = p.stem
    base = stem.split(" (")[0]
    partes = base.rsplit("-", 1)
    # La revision es UN solo caracter. Un ultimo segmento de tres digitos es parte del
    # codigo: 'P22-DWG-06-006-010' no es el plano 006 en revision 010.
    if len(partes) == 2 and partes[1].isdigit() and len(partes[1]) == 1:
        codigo, rev = partes[0], partes[1]
    else:
        codigo, rev = base, None          # isometrias sin sufijo de revision
    hoja = stem.split("_")[-1] if "_" in stem else "unica"
    return codigo, rev, hoja


def inventario(carpeta):
    out = defaultdict(dict)
    for p in sorted(carpeta.glob("*.pdf")):
        cod, rev, hoja = codigo_y_hoja(p)
        out[cod][hoja] = {"path": p, "rev": rev}
    return out


# ------------------------------------------------------------------- firmas
def firma(path):
    """Firma de contenido de una lamina: vectores, bbox del dibujo y hash perceptual."""
    d = fitz.open(path)
    pg = d[0]
    dr = pg.get_drawings()
    rects = [it["rect"] for it in dr if it.get("rect")]
    if rects:
        bbox = (round(min(r.x0 for r in rects)), round(min(r.y0 for r in rects)),
                round(max(r.x1 for r in rects)), round(max(r.y1 for r in rects)))
    else:
        bbox = (0, 0, 0, 0)
    pix = pg.get_pixmap(dpi=DPI_FIRMA, colorspace=fitz.csGRAY)
    phash = hashlib.sha256(pix.samples).hexdigest()[:16]
    # perfil de tinta por banda vertical: tolera cambios locales, distingue laminas
    ancho, alto = pix.width, pix.height
    bandas = []
    paso = max(1, ancho // 16)
    for x0 in range(0, ancho, paso):
        s = 0
        for y in range(0, alto, 2):
            fila = y * pix.stride
            s += sum(255 - pix.samples[fila + x] for x in range(x0, min(x0 + paso, ancho), 2))
        bandas.append(s)
    tot = sum(bandas) or 1
    perfil = [b / tot for b in bandas]
    d.close()
    return {"vec": len(dr), "bbox": bbox, "phash": phash, "perfil": perfil,
            "sha": hashlib.sha256(path.read_bytes()).hexdigest()}


def distancia(fa, fb):
    """0 = identicas. Combina conteo de vectores y perfil de tinta."""
    dv = abs(fa["vec"] - fb["vec"]) / max(fa["vec"], fb["vec"], 1)
    n = min(len(fa["perfil"]), len(fb["perfil"]))
    dp = sum(abs(fa["perfil"][i] - fb["perfil"][i]) for i in range(n)) / 2
    return 0.5 * dv + 0.5 * dp


def alinear(hojas_a, hojas_b, firmas_a, firmas_b):
    """Emparejamiento voraz por distancia minima. Devuelve pares, nuevas y retiradas."""
    pares, usados = [], set()
    cands = sorted(
        ((distancia(firmas_a[ka], firmas_b[kb]), ka, kb) for ka in hojas_a for kb in hojas_b))
    tomados_a = set()
    for dist, ka, kb in cands:
        if ka in tomados_a or kb in usados:
            continue
        if dist > TOL_VECTORES:
            continue
        pares.append((ka, kb, dist))
        tomados_a.add(ka)
        usados.add(kb)
    nuevas = [k for k in hojas_b if k not in usados]
    retiradas = [k for k in hojas_a if k not in tomados_a]
    return sorted(pares, key=lambda x: x[0]), nuevas, retiradas


# ----------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render", metavar="DIR", help="escribe recortes PNG de los pares que difieren")
    args = ap.parse_args()

    if not REV0.is_dir() or not VIG.is_dir():
        sys.exit(f"ERROR: no encuentro las carpetas.\n  {REV0}\n  {VIG}")

    inv0, inv1 = inventario(REV0), inventario(VIG)
    print(f"Rev 0 (COMPILADO): {sum(len(v) for v in inv0.values())} hojas en {len(inv0)} isometrias")
    print(f"Vigente          : {sum(len(v) for v in inv1.values())} hojas en {len(inv1)} isometrias")

    codigos = sorted(set(inv0) | set(inv1))
    resumen = []
    for cod in codigos:
        a, b = inv0.get(cod, {}), inv1.get(cod, {})
        rev_a = next((v["rev"] for v in a.values()), None)
        rev_b = next((v["rev"] for v in b.values()), None)
        print(f"\n{'='*78}\n{cod}   Rev {rev_a or 's/r'} ({len(a)} hojas)  ->  "
              f"Rev {rev_b or 's/r'} ({len(b)} hojas)")

        if not a or not b:
            print("  !! isometria presente en una sola revision")
            resumen.append((cod, rev_a, rev_b, "solo en una revision", 0, 0))
            continue

        # atajo: si toda la isometria es byte-identica, no hay nada que comparar
        sha_a = {h: hashlib.sha256(v["path"].read_bytes()).hexdigest() for h, v in a.items()}
        sha_b = {h: hashlib.sha256(v["path"].read_bytes()).hexdigest() for h, v in b.items()}
        if set(sha_a.values()) == set(sha_b.values()) and len(a) == len(b):
            print("  IDENTICA byte a byte en todas sus hojas.")
            resumen.append((cod, rev_a, rev_b, "identica (SHA256)", 0, len(a)))
            continue

        fa = {h: firma(v["path"]) for h, v in a.items()}
        fb = {h: firma(v["path"]) for h, v in b.items()}
        pares, nuevas, retiradas = alinear(list(a), list(b), fa, fb)

        movidas = sum(1 for ka, kb, _ in pares if ka != kb)
        iguales = 0
        for ka, kb, dist in pares:
            marca = ""
            if ka != kb:
                marca = "   <-- HOJA MOVIDA"
            if fa[ka]["sha"] == fb[kb]["sha"]:
                estado = "identica (SHA256)"
                iguales += 1
            elif fa[ka]["phash"] == fb[kb]["phash"]:
                estado = "identica al render"
                iguales += 1
            else:
                estado = f"DIFIERE (dist {dist:.3f}, vec {fa[ka]['vec']}->{fb[kb]['vec']})"
            print(f"  Rev0 {ka:5} -> Vig {kb:5}  {estado}{marca}")
        for k in nuevas:
            print(f"  {'':5}    -> Vig {k:5}  HOJA NUEVA")
        for k in retiradas:
            print(f"  Rev0 {k:5} ->           HOJA RETIRADA")
        if movidas:
            print(f"  >> {movidas} hoja(s) cambiaron de numero: comparar por numero daria diff falso")
        resumen.append((cod, rev_a, rev_b,
                        f"{len(pares)-iguales} difieren, {len(nuevas)} nuevas, {movidas} movidas",
                        len(pares) - iguales, len(a)))

    print(f"\n{'='*78}\nRESUMEN")
    print(f"{'Isometria':24} {'Rev0':>5} {'Vig':>5}  Estado")
    for cod, ra, rb, est, _, _ in resumen:
        print(f"{cod:24} {str(ra or '-'):>5} {str(rb or '-'):>5}  {est}")


if __name__ == "__main__":
    main()
