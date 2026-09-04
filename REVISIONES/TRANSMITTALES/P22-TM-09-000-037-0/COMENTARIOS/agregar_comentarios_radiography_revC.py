#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_radiography_revC.py
Anota el Radiography Examination Procedure Rev C (P22-BA-09-000-015) del submittal
25007-0086 (ENTREGA 86). Veredicto del TM N37: Code 2 - Approved as noted.

len(COMENTARIOS) = 4, espejo 1:1 del bloque Action de la subseccion 2.2
("OBS-01 and NOTE-01 to NOTE-03 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N35, subseccion 2.4, Code 3. Solo se revisa
contra esa instruccion escrita.

  OBS-01 del N35, criterio unico en lugar de cinco codigos -> CERRADO. No se anota.
  OBS-02 del N35, reemplazar 1,8 mm por el limite T-274    -> CERRADO. No se anota.
  NOTE-01 (a) del N35, material y rango de espesor         -> NO CERRADO -> OBS-01
  NOTE-01 (b) del N35, renumerar sub-clausulas             -> CIERRE PARCIAL -> NOTE-02
  NOTE-01 (c) del N35, proposito y numero de documento     -> CIERRE PARCIAL -> NOTE-01

El determinante cerro en sus dos mitades: la lista de cinco codigos bajo a uno y el
limite de borrosidad geometrica de 1,8 mm —la dispensa del parrafo PW-51.1 de ASME
Seccion I para items con sello PP, que B31.3 no concede— fue reemplazado por los
0,020 in. de la Tabla T-274 del Articulo 2, con el texto reproducido integro.

La NOTE-03 es de calidad documental y sale de la revision de la hoja de comentarios:
la hoja trae dos filas, OBS-01 y OBS-02, y ninguna para la NOTE-01, de modo que los
tres items de aseo no se respondieron como fila.

VERIFICADO DIRECTAMENTE, no tomado del ledger: la clausula 15.0 de la Rev C es
DIRECTION OF RADIATION y la 17.3, Single-wall technique. Las dos referencias
cruzadas que quedaron sin corregir apuntan hoy a clausulas de otra materia.

AVISO DE CITACION INTERNO, que NO cruza al PDF ni al transmittal: con la
renumeracion el rotulo 12.1 cambio de dueño. Si el punto de borrosidad se vuelve a
citar, la referencia correcta es la clausula 13.0, Geometric Unsharpness.

Reparto por pagina (indices 0-based):
    1    portada del procedimiento adjunto  -> NOTE-01
    8    clausula 1.0 SCOPE                 -> OBS-01
    11   clausula 11.6                      -> NOTE-02
    28   hoja de comentarios consolidada    -> NOTE-03
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-015_C_Radiography.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 86",
        "P22-BA-09-000-015_C_Radiography Examination Procedure.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "up to 3-inch thickness",
        "page_fallback": 8,
        "page_min": 8,
        "text": (
            "OBS-01: the scope does not name the material or\n"
            "the wall thickness of this module.\n"
            "ADASA acknowledges the closure of the\n"
            "determinant: the list of five acceptance codes\n"
            "came down to ASME B31.3 para. 341.3.2 alone, and\n"
            "the geometric unsharpness limit of 1.8 mm was\n"
            "replaced by the 0.020 in. of Table T-274 with its\n"
            "text reproduced in full.\n"
            "This clause is unchanged. It reads Stainless,\n"
            "Carbon, low alloy and high alloy steel welds up\n"
            "to 3-inch thickness, which covers materials this\n"
            "module does not use and a thickness range far\n"
            "beyond the one radiographed here.\n"
            "The welds radiographed on this module are ASTM\n"
            "A790 UNS S32750 super duplex, in walls of 6.02 to\n"
            "8.56 mm. Radiographic technique, source size and\n"
            "the IQI selected all follow from that range, and\n"
            "a generic scope leaves them to the interpreter.\n"
            "Correct: state the material and the wall\n"
            "thickness range of this module in the scope when\n"
            "the procedure is issued at Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "PMI PROV-PROC-RT-001",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "NOTE-01: the document number belongs to a\n"
            "different procedure.\n"
            "The purpose clause closed: it now reads the\n"
            "procedure for radiographic examination.\n"
            "This page still reads DOC NO: PMI\n"
            "PROV-PROC-RT-001, which is the number of a\n"
            "positive material identification procedure.\n"
            "Correct: state the document number of this\n"
            "procedure at Rev 0."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "para 15.3",
        "page_fallback": 11,
        "page_min": 11,
        "text": (
            "NOTE-02: two cross-references were left behind by\n"
            "the renumbering.\n"
            "The renumbering itself is done: the headings run\n"
            "from 1.0 to 25.0 without a gap, each sub-clause\n"
            "matches its own heading, PACKING OF FILMS is back\n"
            "in place as 25.0, and the index was updated.\n"
            "Two internal references still point to their old\n"
            "numbers. Clause 11.6 sends the density\n"
            "requirements to para 15.3, and clause 15.0 is now\n"
            "DIRECTION OF RADIATION. Clause 19.4 sends the\n"
            "plus 30 percent density restriction to 17.3, and\n"
            "17.3 is now Single-wall technique.\n"
            "Correct: repoint both references to the clauses\n"
            "that carry the density requirements at Rev 0."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": "CONSOLIDATED COMM",
        "page_fallback": 28,
        "page_min": 28,
        "text": (
            "NOTE-03: the comment sheet answers two of the\n"
            "three points.\n"
            "The sheet carries a row for OBS-01 and a row for\n"
            "OBS-02, both answered Revised as per comment, and\n"
            "no row for NOTE-01. The three housekeeping items\n"
            "of that note were therefore not answered, and one\n"
            "of them, the scope, is the open point of this\n"
            "review.\n"
            "Correct: carry every comment of the previous\n"
            "transmittal as its own row, with the reply\n"
            "against each, on the comment sheet issued at\n"
            "Rev 0."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
