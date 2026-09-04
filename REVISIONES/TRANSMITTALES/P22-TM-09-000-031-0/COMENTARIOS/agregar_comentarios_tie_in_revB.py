#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_tie_in_revB.py
Anota el Tie-In Point Layout Rev B (P22-DWG-09-005-005), submittal 25007-0072
(E72). Veredicto del TM N31: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: solo los dos puntos del Codigo 3 del TM N7 que la Rev B no levanto.
Los tres que cerraron - redibujo sobre el layout consolidado, identificadores
de linea como TP tags, y las tres vistas de elevacion con la columna de cota -
no se anotan.

Estructura del archivo (indices 0-based):
    0   caratula A4
    1   lamina A1 apaisada, rotation 270, con la tabla de puntos de conexion
    2   Consolidated Comment Sheet

PAGINA ROTADA: la lamina tiene rotation=270. La skill v1.6 resuelve el caso con
text_rotate = original_rotation, de modo que NO se hardcodea 270. Cierre
obligatorio: verificar por render PNG que el ID y el texto se leen completos y
de izquierda a derecha, porque en paginas rotadas page.annots() devuelve 0
aunque la anotacion exista.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios  # noqa: E402

# --- Fast-save guard: 75.127 vectores en la lamina A1 ----------------------
import fitz  # noqa: E402
_orig_save = fitz.Document.save


def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)


fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-005_B_Tie_In_Point_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-005_B_Tie_In_Point_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 72", "25007-0072",
        "P22-DWG-09-005-005_B Tie-In Point Layout.pdf",
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
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: the tie-in table states TP-DA P8-001\n"
            "as FEED, 4 inch, class 150, ASME B16.5, and\n"
            "the sheet carries no design pressure for that\n"
            "interface. The point raised at Transmittal N7\n"
            "was not the flange class but the pressure at\n"
            "which the SWRO brine reaches the module\n"
            "battery limit, which has to be at or below\n"
            "19.6 barG at operating temperature for an\n"
            "ANSI 150# connection to be acceptable.\n"
            "Correct: state the design pressure at this\n"
            "tie-in point, on the sheet or in the table."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: row 1 of the tie-in table, TP-AS\n"
            "P11-001 ANTISCALANT 1 inch, carries a dash in\n"
            "the FLANGE # and FLANGE STD columns while the\n"
            "other four rows carry 150 and ASME B16.5.\n"
            "Correct: complete both cells, or state on the\n"
            "sheet that this connection is not flanged and\n"
            "how it is made."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
