#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ultrasonic_revC.py
Anota el Ultrasonic Thickness Procedure Rev C (P22-BA-09-000-016) del submittal
25007-0090 (ENTREGA 90). Veredicto del TM N38: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de la subseccion 2.3
("OBS-01 and NOTE-01 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N35, subseccion 2.5, Code 3. Solo se
revisa contra esa instruccion escrita; no se introducen observaciones nuevas.

  OBS-01 del N35, criterio del NDE Plan en la clausula 9.0    -> CERRADO en lo esencial
  OBS-01 del N35, material como UNS S32750                    -> CERRADO. No se anota.
  NOTE-01 del N35, segundo grado S32250                       -> CERRADO. No se anota.
  NOTE-01 del N35, velocidad sonica como valor                -> NO CERRADO -> NOTE-01
  NOTE-02 del N35, acoplante del formulario                   -> CERRADO. No se anota.
  NOTE-02 del N35, ASME E 797 y API 510/570/653               -> CERRADO. No se anota.
  NOTE-02 del N35, designaciones SA790 y SA79M                -> NO CERRADO -> NOTE-01
  NOTE-02 del N35, caratula como procedimiento de PMI         -> CERRADO. No se anota.
  NOTE-02 del N35, Articulo 9 en vez de Articulo 5            -> NO CERRADO -> OBS-01
  NOTE-02 del N35, emitir con hoja de comentarios             -> CERRADO. No se anota.

El determinante cerro: la clausula 9.0 ya no cita la especificacion de material
sino el NDE Plan aprobado, de modo que el Code 3 no se sostiene. Lo que queda es
la cita del articulo, que es la SEGUNDA vez que se declara alineada sin estarlo,
y dos residuos de la lista de referencias.

Reparto por pagina (indices 0-based):
    3    clausula 4.0, lista de codigos de referencia  -> OBS-01
    8    lista de referencias                          -> NOTE-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-016_C_Ultrasonic_Thickness.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR,
                       "P22-BA-09-000-016_C_Ultrasonic_Thickness_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 90", "25007-0090",
        "P22-BA-09-000-016_C_Ultrasonic Thickness Procedure.pdf",
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
        "search": "Article 9",
        "page_fallback": 3,
        "page_min": 3,
        "text": (
            "OBS-01: the code article cited is the one for\n"
            "visual examination, and this is the second\n"
            "revision in which it is declared aligned.\n"
            "This clause cites ASME Section V, Article 9.\n"
            "Article 9 governs visual examination. Ultrasonic\n"
            "thickness measurement is governed by Article 5.\n"
            "The comment sheet of this revision answers\n"
            "Revised as per comment to the block that raised\n"
            "this point at Transmittal N35.\n"
            "ADASA acknowledges what did close here: the\n"
            "cover section no longer describes this document\n"
            "as a positive material identification procedure,\n"
            "and the edition is stated as 2025 throughout.\n"
            "Clause 9.0 also closed the point that governed\n"
            "the previous response code, and now refers\n"
            "acceptance to the NDE Plan Rev C instead of the\n"
            "material specification.\n"
            "Correct: at Rev 0 cite Article 5 of ASME Section\n"
            "V in this clause, and write the acceptance\n"
            "criterion of the NDE Plan in clause 9.0 rather\n"
            "than referring to it."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "SA790",
        "page_fallback": 8,
        "page_min": 8,
        "offset_y": 45,
        "text": (
            "NOTE-01: two residual items of the reference\n"
            "list and the sound velocity.\n"
            "ADASA acknowledges the closures: the couplant of\n"
            "the report form, the designation ASME E 797 and\n"
            "the in-service inspection codes API 510, 570 and\n"
            "653 are all gone, and the second grade of the\n"
            "calibration block was corrected.\n"
            "Two designations remain in this list, SA790 and\n"
            "SA79M. ASME designates that specification\n"
            "SA-790 and SA-790M.\n"
            "The sound velocity used for UNS S32750 is still\n"
            "not stated as a value, although the procedure\n"
            "does describe the velocity calibration on a\n"
            "block of the material.\n"
            "Correct: at Rev 0 write them as SA-790 and\n"
            "SA-790M, and state the sound velocity as a value."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
