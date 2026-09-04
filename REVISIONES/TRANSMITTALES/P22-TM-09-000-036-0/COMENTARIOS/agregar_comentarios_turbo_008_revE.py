#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_turbo_008_revE.py
Anota el Datasheet of Interstage Turbocharger Rev E (P22-ET-09-009-008) del submittal
25007-0085 (ENTREGA 85). Veredicto del TM N36: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N11, subseccion 2.8, Code 2, que dejo
UNA sola nota abierta sobre este documento: la NOTE-04, que pedia actualizar el
rotulo de la lamina de contorno a Style S PARA ELIMINAR la discrepancia con el
STYLE 77. Ese es el universo entero de esta revision.
  NOTE-04 -> CIERRE PARCIAL: se agrego PIEDMONT STYLE S y no se borro STYLE 77.

NO SE ANOTA: nada mas. El resto del datasheet estaba aprobado desde la Rev D y
no se relee.

Reparto por pagina (indices 0-based):
    5   lamina de contorno HPB-60, las cuatro llamadas de conexion -> OBS-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-009-008_E_Datasheet_Interstage_Turbocharger.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-ET-09-009-008_E_Datasheet_Interstage_Turbocharger_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 85",
        "P22-ET-09-009-008-E_Datasheet of Interstage Turbocharger.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found: " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MENOR,
        "search": "STYLE 77",
        "page_fallback": 5,
        "page_min": 5,
        "text": (
            "OBS-01: the correct coupling was added and the\n"
            "wrong one was not removed.\n"
            "Transmittal N11 asked for the outline label to\n"
            "be updated to Style S so as to eliminate the\n"
            "discrepancy with STYLE 77, which is a different\n"
            "product with a different working pressure.\n"
            "PIEDMONT STYLE S is now on all four connection\n"
            "callouts of this sheet, and STYLE 77 is still\n"
            "there alongside it on all four. Each connection\n"
            "therefore names two coupling models at once,\n"
            "which is the condition the comment set out to\n"
            "remove, on a sheet the shop and the site will\n"
            "both work from.\n"
            "The datasheet body specifies the process\n"
            "connections of SIP-09-002 at Coupling 1800 psi,\n"
            "which is the Style S rating and the accepted\n"
            "one.\n"
            "Correct: delete STYLE 77 from the four callouts\n"
            "when the datasheet is issued at Rev 0, leaving\n"
            "the cut groove designation and PIEDMONT STYLE S."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
