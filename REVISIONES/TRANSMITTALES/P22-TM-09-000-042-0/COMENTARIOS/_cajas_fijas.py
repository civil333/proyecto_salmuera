#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_cajas_fijas.py — ubicacion de cuadros en zona libre para laminas de dibujo (N42).

`_ajustar_cajas.py` (N40) mueve las anotaciones FreeText despues de crearlas y mide
como obstaculo solo texto e imagenes. En una lamina de dibujo eso no basta, y en las
laminas rotadas la skill dibuja el cuadro en el contenido de la pagina, de modo que no
hay anotacion que mover. Aqui la posicion se decide ANTES de llamar a la skill:

1. `zona_libre` renderiza la pagina tal como se ve (con su rotacion), mide la tinta y
   devuelve el rectangulo vacio de ancho w y alto h mas cercano al ancla, en
   coordenadas de pantalla.
2. `fijar_rects` envuelve `doc_annotator._calcular_rect` para que, cuando el texto
   del comentario tenga un rectangulo fijado, devuelva ese y no el calculado. La skill
   no se toca; el envoltorio vive solo mientras corre el script.

El texto se re-envuelve al ancho real del cuadro y el alto se mide con el ancho de
glifo de Helvetica, de modo que la caja queda ajustada al texto.
"""
import textwrap

import fitz  # PyMuPDF
import numpy as np

_A4_WIDTH = 595.0
_FONTSIZE = 8
_LINE_FACTOR = 1.25
_PAD = 6


def escala(page):
    return min(max(1.0, page.rect.width / _A4_WIDTH), 2.0)


def ancla_pantalla(page, texto):
    """Primer hit de `texto` en coordenadas de pantalla (search_for devuelve las de la
    pagina sin rotar)."""
    hits = page.search_for(texto)
    if not hits:
        return None
    r = hits[0]
    if page.rotation:
        r = r * page.rotation_matrix
        r.normalize()
    return r


def envolver_a_ancho(texto, ancho_pt, fontsize):
    """Envuelve por palabras midiendo con Helvetica; devuelve (texto, n_lineas)."""
    util = ancho_pt - 2 * _PAD * fontsize / _FONTSIZE
    lineas, actual = [], ""
    for palabra in " ".join(texto.split()).split(" "):
        prueba = (actual + " " + palabra).strip()
        if fitz.get_text_length(prueba, fontname="helv", fontsize=fontsize) <= util:
            actual = prueba
        else:
            lineas.append(actual)
            actual = palabra
    lineas.append(actual)
    return "\n".join(lineas), len(lineas)


def alto_caja(n_lineas, fontsize):
    return n_lineas * fontsize * _LINE_FACTOR + 2 * _PAD * fontsize / _FONTSIZE + fontsize * 0.6


def _dilatar(mascara, r):
    """Dilatacion cuadrada de radio r pixeles, sin scipy."""
    out = mascara.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            out |= np.roll(np.roll(mascara, dy, axis=0), dx, axis=1)
    return out


def zona_libre(page, w, h, ancla, dpi=36, margen_pt=40, prohibidas=(), tinta_max=0.0,
               holgura_pt=8):
    """Rectangulo de pantalla de w x h pt sin tinta, el mas cercano a `ancla`.
    La tinta se mide con umbral 235 (el texto fino antialiasado queda gris claro) y se
    dilata `holgura_pt`, para que el cuadro no quede tocando una linea o un rotulo.
    `prohibidas` son rects de pantalla que no se pueden tapar (cajetin, otras cajas)."""
    pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w)
    k = dpi / 72.0
    tinta = _dilatar(img < 235, max(1, int(round(holgura_pt * k)))).astype(np.int32)
    for r in prohibidas:
        tinta[max(0, int(r.y0 * k)):int(r.y1 * k) + 1, max(0, int(r.x0 * k)):int(r.x1 * k) + 1] = 1
    integ = np.pad(tinta.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    wp, hp = int(np.ceil(w * k)) + 2, int(np.ceil(h * k)) + 2
    m = int(margen_pt * k)
    # suma de tinta de cada ventana wp x hp con esquina superior izquierda en (y, x)
    s = integ[hp:, wp:] - integ[:-hp, wp:] - integ[hp:, :-wp] + integ[:-hp, :-wp]
    libre = s <= tinta_max * wp * hp
    libre[:m, :] = False
    libre[:, :m] = False
    libre[max(0, pix.h - hp - m):, :] = False
    libre[:, max(0, pix.w - wp - m):] = False
    ys, xs = np.nonzero(libre)
    if len(ys) == 0:
        return None
    cx, cy = (ancla.x0 + ancla.x1) / 2 * k, (ancla.y0 + ancla.y1) / 2 * k
    d = (xs + wp / 2 - cx) ** 2 + (ys + hp / 2 - cy) ** 2
    i = int(np.argmin(d))
    x, y = int(xs[i]), int(ys[i])
    return fitz.Rect((x + 1) / k, (y + 1) / k, (x + 1) / k + w, (y + 1) / k + h)


def asignar_ids_pantalla(pdf_in, comentarios):
    """Numera OBS y NOTE por orden de lectura en pantalla: pagina, luego y y x del ancla
    ya rotada (asignar_ids_secuenciales ordena por la y sin rotar, que en una lamina
    rotada 270 grados es la x de pantalla)."""
    doc = fitz.open(pdf_in)
    for c in comentarios:
        pg = c.get("page_min", c.get("page_fallback", 0))
        a = ancla_pantalla(doc[pg], c["search"]) if c.get("search") else None
        if c.get("ancla_pantalla"):
            a = fitz.Rect(c["ancla_pantalla"])
        c["_orden"] = (pg, round(a.y0, -1) if a else 0.0, a.x0 if a else 0.0)
    doc.close()
    contador = {}
    for c in sorted(comentarios, key=lambda k: k["_orden"]):
        s = c["serie"]
        contador[s] = contador.get(s, 0) + 1
        c["id"] = f"{s}-{contador[s]:02d}"
        c["text"] = c["text"].replace("{ID}", c["id"])
    return [c["id"] for c in sorted(comentarios, key=lambda k: k["_orden"])]


def fijar_rects(doc_annotator_mod, rects_por_texto):
    """Envuelve _calcular_rect: si el texto tiene rect fijado, lo devuelve."""
    original = doc_annotator_mod._calcular_rect

    def _calcular_rect(page, found_rect, text):
        if text in rects_por_texto:
            return fitz.Rect(rects_por_texto[text])
        return original(page, found_rect, text)

    doc_annotator_mod._calcular_rect = _calcular_rect
    return original


def preparar(pdf_in, comentarios, ancho_base=210, prohibidas_por_pagina=None):
    """Para cada comentario con 'zona': True calcula ancho, re-envuelve el texto (ya
    con su ID), mide el alto y busca zona libre junto al ancla. Devuelve el dict
    texto -> rect que consume `fijar_rects`."""
    prohibidas_por_pagina = prohibidas_por_pagina or {}
    doc = fitz.open(pdf_in)
    rects = {}
    ocupadas = {}
    for c in comentarios:
        if not c.get("zona"):
            continue
        pg = c.get("page_min", c.get("page_fallback", 0))
        page = doc[pg]
        sc = escala(page)
        fs = _FONTSIZE * sc
        w = c.get("ancho", ancho_base) * sc
        texto, n = envolver_a_ancho(c["text"], w, fs)
        h = alto_caja(n, fs)
        ancla = ancla_pantalla(page, c["search"]) if c.get("search") else None
        if ancla is None:
            ancla = fitz.Rect(page.rect.width - 100, 100, page.rect.width - 90, 110)
        if c.get("ancla_pantalla"):
            ancla = fitz.Rect(c["ancla_pantalla"])
        prohib = list(prohibidas_por_pagina.get(pg, [])) + ocupadas.get(pg, [])
        r = zona_libre(page, w, h, ancla, prohibidas=prohib)
        if r is None:
            raise RuntimeError(f"{c.get('id')}: sin zona libre de {w:.0f}x{h:.0f} en pag {pg + 1}")
        c["text"] = texto
        rects[texto] = r
        ocupadas.setdefault(pg, []).append(fitz.Rect(r.x0 - 12, r.y0 - 12, r.x1 + 12, r.y1 + 12))
        print(f"  [{c.get('id')}] pag {pg + 1} rot {page.rotation}: {n} lineas, "
              f"cuadro ({r.x0:.0f},{r.y0:.0f})-({r.x1:.0f},{r.y1:.0f}) junto a "
              f"({ancla.x0:.0f},{ancla.y0:.0f})")
    doc.close()
    return rects


def reenvolver(texto, ancho=44):
    return textwrap.fill(" ".join(texto.split()), width=ancho, break_long_words=False,
                         break_on_hyphens=False)


def correr(pdf_in, pdf_out, comentarios, prohibidas_por_pagina=None, ancho_base=210):
    """IDs por orden de pantalla, zona libre para cada cuadro, skill doc-annotator con
    _calcular_rect envuelto, y restauracion del original al terminar."""
    import os
    import sys
    sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
    import doc_annotator as da
    import shutil
    orden = asignar_ids_pantalla(pdf_in, comentarios)
    print("IDs por orden de aparicion:", orden)
    rects = preparar(pdf_in, comentarios, ancho_base=ancho_base,
                     prohibidas_por_pagina=prohibidas_por_pagina)
    # El orden de lectura lo da donde quedo cada cuadro, no el ancla: un cuadro puede
    # terminar lejos de su ancla si alrededor no hay espacio libre. Se renumera por
    # (pagina, y, x) del cuadro final; "OBS-0N" conserva el largo, asi que el
    # envoltorio y el alto no cambian.
    orden_final = sorted(comentarios, key=lambda c: (
        c.get("page_min", c.get("page_fallback", 0)), round(rects[c["text"]].y0, -1),
        rects[c["text"]].x0))
    contador, nuevos = {}, {}
    for c in orden_final:
        s = c["serie"]
        contador[s] = contador.get(s, 0) + 1
        nuevo_id = f"{s}-{contador[s]:02d}"
        r = rects.pop(c["text"])
        c["text"] = c["text"].replace(c["id"], nuevo_id, 1)
        c["id"] = nuevo_id
        nuevos[c["text"]] = r
    rects = nuevos
    orden = [c["id"] for c in orden_final]
    print("IDs por posicion final del cuadro:", orden)
    doc = fitz.open(pdf_in)
    rot = {c["id"]: doc[c.get("page_min", c.get("page_fallback", 0))].rotation
           for c in comentarios}
    doc.close()
    planas = [c for c in comentarios if rot[c["id"]] == 0]
    rotadas = [c for c in comentarios if rot[c["id"]] != 0]
    r = None
    if planas:
        # paginas sin rotacion: anotacion FreeText nativa de la skill, en el rect fijado
        original = fijar_rects(da, rects)
        try:
            r = da.add_pdf_comments(pdf_in, pdf_out, planas)
        finally:
            da._calcular_rect = original
    else:
        shutil.copy2(pdf_in, pdf_out)
    if rotadas:
        dibujar_rotadas(pdf_out, rotadas, rects, da)
    return orden, rects, r


def dibujar_rotadas(pdf_out, comentarios, rects, da):
    """Mismo metodo que la rama rotada de doc_annotator.add_pdf_comments (rotacion a 0,
    rect de pantalla llevado a coordenadas sin rotar con derotation_matrix, rectangulo
    con relleno y borde, insert_textbox con rotate = rotacion original), con una
    diferencia: el texto va en un rect interior con relleno, para que no quede pegado
    al borde."""
    doc = fitz.open(pdf_out)
    for c in comentarios:
        pg = c.get("page_min", c.get("page_fallback", 0))
        page = doc[pg]
        sc = escala(page)
        rect = fitz.Rect(rects[c["text"]])
        rot0 = page.rotation
        derot = page.derotation_matrix
        page.set_rotation(0)
        pad = _PAD * sc
        interior = fitz.Rect(rect.x0 + pad, rect.y0 + pad * 0.6, rect.x1 - pad, rect.y1 - pad * 0.4)
        shape = page.new_shape()
        shape.draw_rect(rect * derot)
        shape.finish(fill=c["fill"], color=(0, 0, 0), width=1.5 * sc)
        shape.commit()
        sobra = page.insert_textbox(interior * derot, c["text"], fontsize=_FONTSIZE * sc,
                                    fontname="helv", color=(0, 0, 0), rotate=rot0)
        page.set_rotation(rot0)
        if sobra < 0:
            raise RuntimeError(f"{c['id']}: el texto no cabe en el cuadro ({sobra:.1f})")
        print(f"  [{c['id']}] pag {pg + 1} rot {rot0} -> ({rect.x0:.0f},{rect.y0:.0f})-"
              f"({rect.x1:.0f},{rect.y1:.0f}), holgura de texto {sobra:.1f} pt")
    tmp = pdf_out + ".tmp"
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    import os
    os.replace(tmp, pdf_out)


def cajetin_bw_a1():
    """Cajetin, bloque de revisiones y leyenda de propiedad de las laminas A1 de BW
    Water en coordenadas de pantalla (2384 x 1684 pt)."""
    return [fitz.Rect(1875, 1020, 2384, 1684)]
