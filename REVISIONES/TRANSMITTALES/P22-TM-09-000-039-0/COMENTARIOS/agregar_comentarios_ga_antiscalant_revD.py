#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_antiscalant_revD.py
Anota el GA of Antiscalant Dosing Tank Rev D (P22-DWG-09-005-015) del submittal
25007-0091 (ENTREGA 91). Veredicto del TM N39: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.2
("OBS-01 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N36, subseccion 2.5, Code 2. Solo se revisa
contra esa instruccion escrita; no se introducen observaciones nuevas.

  OBS-01 del N36, las dos cotas del agujero contra el perno M12 -> CERRADO. No se anota.
  NOTE-01 del N36, elevacion de la marca de nivel               -> NO CERRADO -> OBS-01

El agujero pasa de "14 mm y media pulgada", que no son la misma medida, a
"Ø14 [Ø35/64"]", y 35/64 de pulgada son 13,89 mm: las dos unidades ya nombran la
misma dimension y ambas admiten el M12 del mismo detalle. La fila LEVEL MARKING de
la tabla de boquillas, en cambio, sigue con guion en SIZE y guion en ELEVATION,
identica a la Rev C, mientras la hoja de comentarios responde que la marca fue
agregada con dimensiones.

VERIFICACION OBLIGATORIA. La lamina esta ROTADA 270 grados: las coordenadas de
get_text() vienen sin rotar y hay que llevarlas al espacio de pagina con
page.rotation_matrix. La skill v1.6 dibuja en el content stream y page.annots()
devuelve cero aunque el cuadro sea visible, de modo que el cierre de esta anotacion
es por RENDER PNG, comprobando que el ID y la palabra Correct se leen completos y
de izquierda a derecha.

FUERA DE ALCANCE, en _ANALISIS_N39.md con su razon: el volumen total de 335 L
frente a los 0,34 metros cubicos del ciclo de la Rev A, que el N36 no repitio, y el
radio rotulado R74 [R3"], identico desde la Rev B.

Reparto por pagina (indices 0-based):
    1    tabla NOZZLE SPECIFICATIONS, fila LEVEL MARKING   -> OBS-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-015_D_GA_Antiscalant_Dosing_Tank.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-015_D_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 91",
        "P22-DWG-09-005-015_D GA of Antiscalant Dosing Tank.pdf",
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
        "search": "LEVEL MARKING",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-01: the level marking row is unchanged, and\n"
            "the comment sheet reports it as done.\n"
            "ADASA acknowledges the closure of the other\n"
            "point. The anchor hole is now labelled 14 mm and\n"
            "35/64 inch, which are the same dimension, and\n"
            "both accept the M12 bolt of Detail 4. At Rev C\n"
            "the pair read 14 mm and half an inch, which are\n"
            "not the same, and at Rev B 10 mm and half an\n"
            "inch.\n"
            "This row still reads a dash under SIZE and a dash\n"
            "under ELEVATION, with SIDE as its location. It is\n"
            "identical to Rev C. Note 8 declares an effective\n"
            "working volume of 0.27 cubic metres, and without\n"
            "an elevation on this row there is no mark on the\n"
            "tank that materialises that volume, so it cannot\n"
            "be verified in the field or used to set the level\n"
            "instrument.\n"
            "The comment sheet of this revision answers this\n"
            "point with Level mark added with dimensions.\n"
            "Correct: at Rev 0 state the size and the\n"
            "elevation of this row, the elevation being the\n"
            "one that corresponds to the working volume of\n"
            "note 8."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
