#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_ajustar_cajas.py — post-proceso de los CC_ADASA generados con doc-annotator.

Dos problemas de la skill que este helper corrige sin tocarla (vive en claude-memory y
la usan otros proyectos):

1. ALTO. `_calc_height` asume 45 caracteres por linea y cuenta cada linea logica mas
   larga como dos, con 11 pt por linea: una caja de 8 lineas sale con el doble de alto y
   la mitad inferior vacia. Aqui se mide cada linea con `fitz.get_text_length` y el alto
   queda en lineas reales x 1,25 x fontsize + 10 pt.

2. POSICION. `_calcular_rect` pone la caja a la derecha del texto encontrado y, si no
   cabe, debajo y alineada a su x0, encima del parrafo. Aqui se busca un rectangulo libre
   alineado al borde derecho de la columna de texto (o a `x1_max`), partiendo de la y del
   ancla y bajando de 6 en 6 pt; el primero que no toca ningun bloque de texto o imagen
   de la pagina, ninguna anotacion ajena ni otra caja de ADASA, gana. Si no hay sitio
   hacia abajo se busca hacia arriba; si tampoco, se deja donde la skill la puso.

Ademas `asignar_ids_secuenciales` numera OBS y NOTE por orden de aparicion (pagina, y
del ancla), que es el orden en que el lector los encuentra.

Uso en los scripts:
    from _ajustar_cajas import asignar_ids_secuenciales, ajustar_cajas
    asignar_ids_secuenciales(PDF_LOCAL, COMENTARIOS)      # antes de add_pdf_comments
    add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    ajustar_cajas(PDF_OUT, x1_max=None)                    # despues

Cada entrada de COMENTARIOS lleva, ademas de las claves de la skill, "serie" ("OBS" o
"NOTE") y un texto con el marcador {ID}, sin saltos de linea: este helper lo envuelve a
44 caracteres, que es lo que la skill cuenta como una linea.
"""
import os
import re
import textwrap

import fitz  # PyMuPDF

_A4_WIDTH = 595.0
_ANNOT_WIDTH = 210
_FONTSIZE = 8
_MARGIN = 10
_WRAP = 44
_LINE_FACTOR = 1.25
_PAD_Y = 10
_PAD_X = 4
_GAP = 4
_STEP = 6


def _scale(page):
    return min(max(1.0, page.rect.width / _A4_WIDTH), 2.0)


def envolver(texto, ancho=_WRAP):
    return textwrap.fill(" ".join(texto.split()), width=ancho, break_long_words=False,
                         break_on_hyphens=False)


def asignar_ids_secuenciales(pdf_in, comentarios):
    """Numera por (pagina, y del ancla) y sustituye {ID} en el texto, ya envuelto."""
    doc = fitz.open(pdf_in)
    for c in comentarios:
        pg = c.get("page_min", c.get("page_fallback", 0))
        hits = doc[pg].search_for(c["search"]) if c.get("search") else []
        c["_anchor"] = (pg, hits[0] if hits else None)
        c["_orden"] = (pg, hits[0].y0 if hits else 0.0)
    doc.close()
    contador = {}
    for c in sorted(comentarios, key=lambda k: k["_orden"]):
        s = c["serie"]
        contador[s] = contador.get(s, 0) + 1
        c["id"] = f"{s}-{contador[s]:02d}"
        c["text"] = envolver(c["text"].replace("{ID}", c["id"]))
    return [c["id"] for c in sorted(comentarios, key=lambda k: k["_orden"])]


def _alto_texto(texto, fontsize, ancho_util):
    lineas = 0
    for logica in texto.split("\n"):
        if not logica.strip():
            lineas += 1
            continue
        # word-wrap real dentro del ancho util
        actual = ""
        n = 1
        for palabra in logica.split(" "):
            prueba = (actual + " " + palabra).strip()
            if fitz.get_text_length(prueba, fontname="helv", fontsize=fontsize) <= ancho_util:
                actual = prueba
            else:
                n += 1
                actual = palabra
        lineas += n
    return lineas, lineas * fontsize * _LINE_FACTOR + _PAD_Y * (fontsize / _FONTSIZE)


def _obstaculos(page, propias):
    """Bloques de texto e imagen de la pagina mas anotaciones ajenas. Los bloques que
    caen dentro de una caja propia (la apariencia que la skill ya dibujo) se excluyen:
    get_text("blocks") incluye el texto de las anotaciones y, sin este filtro, la caja
    original se bloquea a si misma y empuja a todas hacia abajo."""
    obs = []
    propias_rects = [a.rect for a in propias]
    for b in page.get_text("blocks"):
        r = fitz.Rect(b[:4])
        if r.is_empty or r.width < 2 or r.height < 2:
            continue
        if any(pr.contains(r) or (pr.intersects(r) and abs(r & pr) > 0.6 * abs(r))
               for pr in propias_rects):
            continue
        obs.append(r)
    for a in page.annots() or []:
        if a in propias:
            continue
        obs.append(a.rect)
    return obs


def _libre(rect, obstaculos, colocadas, page_rect, gap=_GAP):
    if not page_rect.contains(rect):
        return False
    holgura = fitz.Rect(rect.x0 - gap, rect.y0 - gap, rect.x1 + gap, rect.y1 + gap)
    for o in obstaculos:
        if holgura.intersects(o):
            return False
    for o in colocadas:
        if holgura.intersects(o):
            return False
    return True


def _buscar_sitio(page, ancla, w, h, x1_max, obstaculos, colocadas):
    pr = page.rect
    sc = _scale(page)
    margen = _MARGIN * sc
    x1 = min(x1_max, pr.width - margen) if x1_max else pr.width - margen
    x0 = x1 - w
    y_ancla = ancla.y0 if ancla is not None else margen
    # hacia abajo
    y = y_ancla
    while y + h <= pr.height - margen:
        r = fitz.Rect(x0, y, x1, y + h)
        if _libre(r, obstaculos, colocadas, pr):
            return r
        y += _STEP
    # hacia arriba
    y = y_ancla - _STEP
    while y >= margen:
        r = fitz.Rect(x0, y, x1, y + h)
        if _libre(r, obstaculos, colocadas, pr):
            return r
        y -= _STEP
    print(f"    sin sitio: ancla y={y_ancla:.0f}, w={w:.0f}, h={h:.0f}, x0={x0:.0f}, "
          f"obstaculos={len(obstaculos)}")
    return None


def ajustar_cajas(pdf_out, comentarios, x1_max=None):
    """Redimensiona y reubica las cajas de ADASA en pdf_out. Devuelve la lista de
    (id, pagina 1-based, rect final, lineas, reubicada)."""
    anclas = {c["id"]: c.get("_anchor", (None, None)) for c in comentarios}
    doc = fitz.open(pdf_out)
    resultado = []
    for pno in range(len(doc)):
        page = doc[pno]
        propias = [a for a in (page.annots() or [])
                   if re.match(r"(OBS|NOTE)-\d\d", a.info.get("content", "") or "")]
        if not propias:
            continue
        sc = _scale(page)
        fontsize = _FONTSIZE * sc
        w = _ANNOT_WIDTH * sc
        obst = _obstaculos(page, propias)
        colocadas = []
        # ordenar por y del ancla para que la primera se lleve el sitio mas cercano
        def _y(a):
            aid = re.match(r"(OBS|NOTE)-\d\d", a.info["content"]).group(0)
            an = anclas.get(aid, (None, None))[1]
            return an.y0 if an is not None else a.rect.y0
        for a in sorted(propias, key=_y):
            aid = re.match(r"(OBS|NOTE)-\d\d", a.info["content"]).group(0)
            texto = a.info["content"]
            lineas, h = _alto_texto(texto, fontsize, w - 2 * _PAD_X * sc)
            ancla = anclas.get(aid, (None, None))[1]
            nuevo = _buscar_sitio(page, ancla, w, h, x1_max, obst, colocadas)
            reubicada = nuevo is not None
            if nuevo is None:
                r0 = a.rect
                nuevo = fitz.Rect(r0.x0, r0.y0, r0.x0 + w, r0.y0 + h)
                if not page.rect.contains(nuevo):
                    nuevo = fitz.Rect(r0.x0, page.rect.height - _MARGIN * sc - h,
                                      r0.x0 + w, page.rect.height - _MARGIN * sc)
            fill = a.colors.get("fill") or (1, 1, 1)
            a.set_rect(nuevo)
            a.set_border(width=1.5 * sc)
            a.update(fontsize=fontsize, text_color=(0, 0, 0), fill_color=fill)
            colocadas.append(nuevo)
            resultado.append((aid, pno + 1, nuevo, lineas, reubicada))
            print(f"  [{aid}] pag {pno + 1} -> ({nuevo.x0:.0f},{nuevo.y0:.0f})-"
                  f"({nuevo.x1:.0f},{nuevo.y1:.0f}) {lineas} lineas"
                  f"{'' if reubicada else '  (SIN SITIO LIBRE: posicion de la skill)'}")
    tmp = pdf_out + ".tmp"
    doc.save(tmp, deflate=True)
    doc.close()
    os.replace(tmp, pdf_out)
    return resultado
