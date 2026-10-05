#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_transmittal.py — TRANSMITTAL N42 ADASA-BW_WATER (P22-TM-09-000-042-0).

Submittals 25007-0096 (ENTREGA 96, 22-Sep-2026), 25007-0097 (ENTREGA 97, 23-Sep),
25007-0099 (ENTREGA 99, 29-Sep) y 25007-0100 (ENTREGA 100, 1-Oct). Siete documentos.

VEREDICTO GLOBAL: 3 — To be revised. 4 Codigo 1, 1 Codigo 2, 3 Codigo 3 (ocho documentos, con el plano del yugo).
Determinantes: el paquete de izaje (addendum Rev A con el plano del yugo
P22-DWG-09-005-019 Rev A, hoja 1 de 3), los puntos de izaje de mantencion Rev A y la
Valve List Rev 0 (VM-09-065 en PVC sobre linea 316L).

DECISIONES DE LUIS (5-Oct-2026):
  - Un solo N42 con las cuatro entregas, a enviar el miercoles 7-Oct.
  - Reclamar el plano de detalle del yugo citando el correo del 15-Sep.
  - Reemisiones: solo levantamiento de los comentarios anteriores, sin comentarios
    nuevos salvo errores garrafales; tabla de levantamiento al inicio de la Seccion 2.
  - Sin el patron de devolucion a tres dias en la Seccion 3.

FUENTE UNICA: P22-TM-09-000-042-0_TRANSMITTAL.md. Este script LEE el .md y lo vuelca
al template ADASA, de modo que el Word no puede divergir del texto revisado con anti-ia.
Titulos sin numero (el template numera H1/H2); negritas **...** a runs en negrita;
tablas markdown a add_simple_table con anchos fijados en el tblGrid.
"""
import os
import re
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet,
    set_repeat_table_header,
)
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Inches, Pt  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(SCRIPT_DIR, "P22-TM-09-000-042-0_TRANSMITTAL.md")
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N42 ADASA-BW_WATER.docx")
TALLY_ESPERADO = (4, 1, 3)  # Codigo 1, 2, 3

# anchos de tabla (pulgadas) segun su encabezado
ANCHOS = {
    "Document|Comment|Raised in|Status": [1.55, 2.75, 0.95, 1.45],
    "Origin|Document|Observation|Status": [1.0, 1.45, 2.95, 1.3],
    "Document|Code|Annotated PDF": [2.75, 0.5, 3.45],
    "Document Code|Title|Rev|Submittal|Response Code": [1.45, 2.15, 0.4, 0.95, 1.75],
}


# --------------------------------------------------------------------- helpers
def _run(par, texto, bold, size):
    r = par.add_run(texto)
    r.bold = bold
    r.font.name = "Arial"
    if size:
        r.font.size = Pt(size)
    return r


def _runs(par, texto, size=None):
    """Agrega `texto` al parrafo convirtiendo **...** en runs en negrita. El guion de los
    ID (OBS-03, NOTE-01) va como guion no separable de Word (w:noBreakHyphen): sin eso
    Word corta la linea en el guion y el PDF muestra "(OBS-" y "03)" en lineas distintas."""
    for i, trozo in enumerate(re.split(r"\*\*", texto)):
        if not trozo:
            continue
        bold = (i % 2 == 1)
        pos = 0
        for m in re.finditer(r"\b(OBS|NOTE)-(\d\d)\b", trozo):
            if m.start() > pos:
                _run(par, trozo[pos:m.start()], bold, size)
            _run(par, m.group(1), bold, size)
            guion = _run(par, "", bold, size)
            guion._r.append(OxmlElement("w:noBreakHyphen"))
            _run(par, m.group(2), bold, size)
            pos = m.end()
        if pos < len(trozo):
            _run(par, trozo[pos:], bold, size)
    return par


def add_para(doc, texto):
    p = doc.add_paragraph()
    _runs(p, texto)
    return aplicar_arial_12(p)


def add_bullet_md(doc, texto):
    p = add_bullet(doc, "", size=11, space_after_pt=8)
    return _runs(p, texto, size=11)


def _fijar_anchos(tabla, anchos):
    """El ancho lo manda el w:tblGrid con layout fijo; cell.width solo no basta."""
    tbl = tabla._tbl
    layout = tbl.tblPr.find(qn("w:tblLayout"))
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tbl.tblPr.append(layout)
    layout.set(qn("w:type"), "fixed")
    grid = tbl.find(qn("w:tblGrid"))
    for col, ancho in zip(grid.findall(qn("w:gridCol")), anchos):
        col.set(qn("w:w"), str(int(ancho * 1440)))
    for row in tabla.rows:
        for celda, ancho in zip(row.cells, anchos):
            celda.width = Inches(ancho)


def _no_partir_filas(tabla):
    for row in tabla.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def add_table(doc, headers, filas, size=9):
    limpio = lambda s: s.replace("**", "")  # noqa: E731
    t = add_simple_table(doc, [tuple(headers)] + [tuple(limpio(c) for c in f) for f in filas])
    set_repeat_table_header(t.rows[0])
    _no_partir_filas(t)
    clave = "|".join(headers)
    if clave not in ANCHOS:
        raise KeyError(f"tabla sin anchos declarados: {clave}")
    _fijar_anchos(t, ANCHOS[clave])
    for i, row in enumerate(t.rows):
        for j, celda in enumerate(row.cells):
            fuente = headers[j] if i == 0 else filas[i - 1][j]
            if i > 0 and ("**" in fuente or re.search(r"\b(OBS|NOTE)-\d\d\b", fuente)):
                # re-escribir la celda con sus negritas
                par = celda.paragraphs[0]
                for r in list(par.runs):
                    r._r.getparent().remove(r._r)
                _runs(par, fuente, size=size)
            for para in celda.paragraphs:
                if i > 0:
                    # celdas de cuerpo a la izquierda: justificadas dejan huecos
                    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in para.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(size)
    return t


# --------------------------------------------------------------------- lector .md
def leer_md(ruta):
    texto = open(ruta, encoding="utf-8").read()
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)
    bloques, tabla, parrafo = [], None, []

    def cerrar_parrafo():
        if parrafo:
            bloques.append(("p", " ".join(parrafo)))
            parrafo.clear()

    for linea in texto.split("\n"):
        s = linea.rstrip()
        if s.startswith("|"):
            cerrar_parrafo()
            celdas = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in celdas):
                continue
            if tabla is None:
                tabla = {"headers": celdas, "filas": []}
                bloques.append(("t", tabla))
            else:
                tabla["filas"].append(celdas)
            continue
        tabla = None
        if not s:
            cerrar_parrafo()
            continue
        m = re.match(r"^(#{1,2}) (?:\d+(?:\.\d+)?\.? )?(.*)$", s)
        if m:
            cerrar_parrafo()
            bloques.append(("h%d" % len(m.group(1)), m.group(2)))
        elif s.startswith("- "):
            cerrar_parrafo()
            bloques.append(("b", s[2:]))
        else:
            parrafo.append(s)
    cerrar_parrafo()
    return bloques


def verificar(bloques):
    texto = " ".join(b[1] if isinstance(b[1], str) else str(b[1]) for b in bloques)
    assert "§" not in texto, "signo de seccion en el .md"
    for prohibida in ("Van Doorn", "PRG-", "BV-2", "INT-1", "Adzlan"):
        assert prohibida not in texto, f"referencia interna en el .md: {prohibida}"
    resumen = [b[1] for b in bloques if b[0] == "t"
               and b[1]["headers"][:2] == ["Document Code", "Title"]][0]
    tally = [0, 0, 0]
    for f in resumen["filas"]:
        tally[int(f[4][0]) - 1] += 1
    assert tuple(tally) == TALLY_ESPERADO, f"tally {tally} != {TALLY_ESPERADO}"
    return tally


if __name__ == "__main__":
    bloques = leer_md(MD)
    tally = verificar(bloques)

    crear_documento_adasa(
        titulo="TECHNICAL REVIEW TRANSMITTAL N42 — SECOND STAGE RO BRINE MODULE",
        codigo="P22-TM-09-000-042-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )
    doc = Document(OUTPUT)
    for tipo, contenido in bloques:
        if tipo == "h1":
            doc.add_heading(contenido.upper(), level=1)
        elif tipo == "h2":
            doc.add_heading(contenido, level=2)
        elif tipo == "p":
            add_para(doc, contenido)
        elif tipo == "b":
            add_bullet_md(doc, contenido)
        elif tipo == "t":
            add_table(doc, contenido["headers"], contenido["filas"])
    doc.save(OUTPUT)
    print("Documento generado: " + OUTPUT)
    print("  tally 1/2/3 = %s/%s/%s" % tuple(tally))
