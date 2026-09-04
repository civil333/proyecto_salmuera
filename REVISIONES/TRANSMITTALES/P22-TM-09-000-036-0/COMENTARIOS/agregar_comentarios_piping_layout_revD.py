#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_piping_layout_revD.py
Anota el Piping Layout Rev D (P22-DWG-09-005-004) del submittal 25007-0083
(ENTREGA 83). Veredicto del TM N36: Code 3 - To be revised.

len(COMENTARIOS) = 4, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N30, subseccion 2.3, Code 2. Ese Code 2
fijo TRES condiciones y ese es el universo entero de esta revision.
  Condicion 1, tabla de tie-in     -> CIERRE PARCIAL: la tabla existe pero no
      cubre ninguna linea de CIP y las elevaciones no declaran datum -> OBS-01
  Condicion 2, clase de brida      -> NO CERRADA: antiscalante con guion y CIP
      ausente de la tabla -> OBS-02
  Condicion 3, uno o dos tableros  -> NO CERRADA: dos envolventes rotuladas LCP
      sin TAG y sin nota -> OBS-03
  Hoja de comentarios              -> transcribe una de las tres -> NOTE-01

NO SE ANOTA, per la regla de alcance:
  - La portada declara "Page 1 of 2" sobre cinco paginas. Housekeeping, y ya
    venia igual en la Rev C.
  - La columna TAG (PID) usa identificadores de punto de conexion y no TAG de
    linea. Va como clausula dentro de OBS-01, no como observacion suelta.
  - El conjunto de once planos de taller fue removido del archivo. Su reemision
    con codigo propio NO es condicion de este plano: vive en la subseccion 2.4
    del TM N30, que lo devolvio sin codigo de respuesta. Se sigue en la
    Seccion 3 del transmittal.

Reparto por pagina (indices 0-based). Se distribuyen entre las tres laminas
porque las tres cajas no caben en la lamina 1 sin tapar la tabla de tie-in ni
salirse del area util, y ademas cada comentario queda junto a su contenido:
    1   lamina 1, tabla de tie-in            -> OBS-01
    1   lamina 1, rotulos LCP                -> OBS-03
    3   lamina 3, seccion CIP y antiscalante -> OBS-02
    4   hoja de comentarios consolidada      -> NOTE-01

Paginas 1 a 3 tienen rotacion 270: la skill dibuja en el content stream y
page.annots() devuelve 0 aunque el cuadro sea visible. Cerrar por render PNG.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_D_Piping_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_D_Piping_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 83", "25007-0083-1",
        "P22-DWG-09-005-004_D Piping Layout.pdf",
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
        "search": "ELEVATION",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-01: the tie-in schedule was added and it\n"
            "does not yet do what it was asked to do.\n"
            "Transmittal N30 required it to cover every\n"
            "battery-limit connection, expressly including\n"
            "the CIP supply and return lines. The five rows\n"
            "cover antiscalant, feed, permeate and two\n"
            "concentrate connections. None of the seven CIP\n"
            "lines labelled on this sheet appears.\n"
            "The elevations are given as 1680, 2597, 2947,\n"
            "2947 and 2940 mm with no datum stated anywhere\n"
            "on the drawing: the NOTES block of all three\n"
            "sheets is empty. An elevation without an origin\n"
            "cannot be set out on site.\n"
            "Correct: add one row per CIP battery-limit\n"
            "connection, state the datum in the NOTES block,\n"
            "and identify each connection by its approved\n"
            "Line List tag as well as the tie-in point tag."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "CIP RECIRCULATION",
        "page_fallback": 3,
        "page_min": 3,
        "text": (
            "OBS-02: the flange class is still missing at\n"
            "the antiscalant and CIP terminations.\n"
            "Row 1, TP-AS P11-001, carries a dash in both\n"
            "FLANGE # and FLANGE STD, and the CIP\n"
            "terminations are not in the schedule at all.\n"
            "BW Water stated in the previous comment sheet\n"
            "that the antiscalant injection line connects to\n"
            "the static mixer through a flanged joint and\n"
            "that the CIP make-up line connects to the tank\n"
            "nozzle through a flanged joint. The drawing now\n"
            "contradicts that written answer.\n"
            "Correct: state the flange class and standard of\n"
            "the antiscalant and CIP battery-limit\n"
            "terminations, consistent with the approved Line\n"
            "List, or state the connection type if the\n"
            "termination is not flanged."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "NOTES",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-03: the module still shows two enclosures\n"
            "labelled LCP and no way to tell them apart.\n"
            "One sits next to the equipment access door and\n"
            "the other next to the dosing area. Neither\n"
            "carries a tag, and no note on any of the three\n"
            "sheets states how many local control panels the\n"
            "module has.\n"
            "The point was raised at Transmittal N30 and is\n"
            "not addressed in this revision. Cable routing,\n"
            "conduit penetrations and the scope of the\n"
            "Factory Acceptance Test all depend on the\n"
            "answer.\n"
            "Correct: state on the drawing whether the\n"
            "module carries one or two local control panels\n"
            "and tag each enclosure consistently with the\n"
            "approved Local Control Panel datasheet and the\n"
            "Single Line Diagram."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "CONSOLIDATED COMMENT SHEET",
        "page_fallback": 4,
        "text": (
            "NOTE-01: the comment sheet records one of the\n"
            "three conditions that were issued.\n"
            "Transmittal N30 returned this drawing at Code 2\n"
            "with three conditions and five identifiers. The\n"
            "Rev C row of this sheet transcribes only the\n"
            "tie-in point details. The flange class at the\n"
            "antiscalant and CIP terminations and the local\n"
            "control panel count do not appear in the client\n"
            "comment column at all.\n"
            "A reviewer working from this sheet cannot see\n"
            "what was asked, which is how two of the three\n"
            "conditions were missed.\n"
            "Correct: transcribe the three conditions in\n"
            "full and answer each one separately when the\n"
            "drawing is re-issued."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
