#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_skid_revB.py
Anota el GA of SWRO System Skid Rev B (P22-DWG-09-005-008), submittal
25007-0072 (E72). Veredicto del TM N31: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: NOTE-11 y NOTE-12 del TM N15 cerraron en sustancia - el bloque de
notas entrega recipientes por etapa, elementos por recipiente, material y clase
del manifold, y remite las matrices y los datos de presion a los listados que
los gobiernan. Lo unico que queda son las TRES referencias mal citadas dentro de
esas mismas notas nuevas, que van en una sola anotacion sobre el bloque.

Estructura del archivo (indices 0-based):
    0      caratula A4
    1, 2   laminas A1 con el bloque de notas 1 a 8
    3      Consolidated Comment Sheet

La anotacion va sobre la lamina 1 (indice 1), donde aparece el bloque de notas.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios  # noqa: E402

# --- Fast-save guard: 284.078 vectores en las dos laminas A1 ---------------
import fitz  # noqa: E402
_orig_save = fitz.Document.save


def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)


fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_B_GA_SWRO_Skid.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_B_GA_SWRO_Skid_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 72", "25007-0072",
        "P22-DWG-09-005-008_B GA of SWRO System Skid.pdf",
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
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: the three references added to close\n"
            "the Transmittal N15 notes point to documents\n"
            "that cannot be identified as written.\n"
            "Correct:\n"
            "1. Note 6 cites the Instrument List at Rev D.\n"
            "   The current revision is Rev E.\n"
            "2. Note 7 cites P22-LI-09-009-00. The approved\n"
            "   Line List is P22-LI-09-009-003.\n"
            "3. Note 8 cites P22-ET-09-006-01, which is not\n"
            "   a valid document code in the project\n"
            "   numbering. State the full code and\n"
            "   revision of the piping specification."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
