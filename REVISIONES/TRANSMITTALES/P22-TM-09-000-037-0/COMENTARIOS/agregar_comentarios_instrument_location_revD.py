#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_instrument_location_revD.py
Anota el Instrument Location Layout Rev D (P22-DWG-09-008-001) del submittal
25007-0086 (ENTREGA 86). Veredicto del TM N37: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de la subseccion 2.4
("OBS-01 to OBS-02 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N23, subseccion 2.6, Code 3, con cuatro
observaciones. Solo se revisa contra esa instruccion escrita.

  OBS-01 del N23, la letra de revision reutilizada -> NO CERRADO -> OBS-01
  OBS-02 del N23, geometria amarrada al Equipment Layout superado
                                                   -> CERRADO en sustancia, pero la
                                                      declaracion no esta en el plano
                                                      -> OBS-02
  OBS-03 del N23, codigo del cajetin a dos digitos -> CERRADO. No se anota.
  OBS-04 del N23, dos fechas de emision            -> CERRADO. No se anota.

El determinante del Code 3 —la dependencia con un plano superado y abierto en
Code 3— cerro: el Equipment Layout Rev D quedo en Code 1 en el TM N33.

🔴 TODO LO QUE SE AFIRMA AQUI SE VERIFICO POR RENDER PROPIO, no por get_text ni
tomandolo del analisis interno. El cajetin y el cuadro de notas son vectores: el
texto extraible devuelve los rotulos y no el contenido de las filas.

  - El bloque REVISIONS NO esta vacio: trae cuatro filas, D AUG.24.26, C JUN.16.26,
    B FEB.27.26 y A JAN.17.26, todas BT/JFR, con la columna ECN. en blanco y la
    MISMA descripcion ISSUED FOR APPROVAL en las cuatro. El analisis interno decia
    "vacio" y estaba equivocado; el _LEDGER_COMENTARIOS.md de la ENTREGA 86 lo tenia
    bien. Renders en _render/ILL_sobre_revisions_p1.png.
  - La fila historica SI se reescribio: la Rev C emitida (ENTREGA 52) fecha esa fila
    APR.17.26 y la Rev D la fecha JUN.16.26. Render de contraste en
    _render/ILL_E52_revblock_p1.png.
  - El cuadro NOTES esta vacio: render en _render/ILL_notes_p1.png.
  - La cadena 005-003 aparece UNA sola vez en todo el archivo, en la pagina 4, que
    es la hoja de comentarios. No esta en ninguna de las dos laminas.

LA COLUMNA ECN. NO SE EXIGE y el texto lo dice: esta igualmente en blanco en el
Equipment Layout, de modo que es convencion del proyecto y no una omision. Exigirla
seria un pedido nuevo disfrazado de incumplimiento.

DEPENDENCIA QUE NO DEGRADA y va a la Seccion 3 del transmittal, no a este PDF: la
respuesta declara que la Rev D se basa en la Instrument List Rev E, que es la lista
cuya reemision ADASA exige con VT-09-001 rangeado de 0 a 12 mm/s rms.

Reparto por pagina (indices 0-based):
    1    lamina 1, bloque REVISIONS -> OBS-01 (aplica a las dos laminas)
    1    lamina 1, cuadro NOTES     -> OBS-02 (aplica a las dos laminas)
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-008-001_D_Instrument_Location_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 86",
        "P22-DWG-09-008-001_D Instrument Location Layout.pdf",
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
        # Anclado en el rotulo del titulo, no en el bloque REVISIONS: anclarlo ahi
        # deja la caja encima de las mismas filas que comenta y desborda el borde
        # inferior de la lamina. Verificado por render.
        "search": "INSTRUMENT LOCATION LAYOUT",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-01: the revision block does not say what\n"
            "changed, and the row of Rev C was rewritten.\n"
            "Applies to both sheets.\n"
            "The block carries four rows, D AUG.24.26, C\n"
            "JUN.16.26, B FEB.27.26 and A JAN.17.26, and all\n"
            "four repeat the same description, ISSUED FOR\n"
            "APPROVAL. No row states what changed at its\n"
            "issue.\n"
            "The row of Rev C reads JUN.16.26 here and reads\n"
            "APR.17.26 on the drawing issued at Rev C. The\n"
            "April issue was overwritten rather than a row\n"
            "added, so the two issues that carried the letter\n"
            "C are still not distinguishable, which is what\n"
            "the original observation was about.\n"
            "The change notice column is not required: it is\n"
            "blank on the Equipment Layout as well, so it is\n"
            "a project convention.\n"
            "Correct: describe what changed at each issue,\n"
            "and restore the April issue date on the row of\n"
            "Rev C, when the drawing is issued at Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "NOTES",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-02: the drawing does not declare the layout\n"
            "revision it is built on.\n"
            "Applies to both sheets.\n"
            "ADASA acknowledges the closure: the reply states\n"
            "that Rev D was updated on the approved\n"
            "P22-DWG-09-005-003 Equipment Layout Rev D, and\n"
            "that Equipment Layout reached Code 1 at\n"
            "Transmittal N33, so the dependency that held\n"
            "this drawing is lifted.\n"
            "That declaration lives only on the reply sheet.\n"
            "This notes box is empty, there is no reference\n"
            "document list, the originator drawing number\n"
            "reads a dash, and the string 005-003 appears\n"
            "once in the whole file, on the comment sheet.\n"
            "A drawing issued for construction has to carry\n"
            "on its face the revision of the layout it is\n"
            "coordinated against; the comment sheet does not\n"
            "travel with it to the field.\n"
            "Correct: state in this box the Equipment Layout\n"
            "code and revision the drawing is built on when\n"
            "it is issued at Rev 0."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
