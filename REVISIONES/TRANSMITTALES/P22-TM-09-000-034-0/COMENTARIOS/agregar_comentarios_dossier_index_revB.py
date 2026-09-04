#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anota el Quality Dossier Index Rev B (P22-BA-09-000-013), submittal 25007-0077
(E77). Veredicto del TM N34: Code 3 - To be revised.

len(COMENTARIOS) = 5, espejo 1:1 del bloque Action de la subseccion 2.3.

ALCANCE. Unico documento de este transmittal que se revisa a fondo y no solo
por cierre de comentarios: su funcion es ser el checklist del dossier y un
capitulo que falta deja sin ubicacion un registro que gatilla pago.

De los diez puntos del TM N30 cierran cinco: OBS-02 (capitulos de despacho C9 y
C10), OBS-04 (D6 RO Pressure Vessel), OBS-05 (D1-D13 y E1-E3), OBS-06 (calif.
de personal en B3-B6 y calibracion en C18) y NOTE-04 (C19 y C20). NOTE-02 cerro
por otra via, con la E75. Quedan los cinco de abajo.

NO SE LEVANTAN, por regla anti-invencion: la eliminacion de los capitulos C1 a
C3 de la Rev A (planos GA, planos de fabricacion y P&ID), que ADASA nunca pidio
conservar y que la ET no exige dentro del dossier; y la cita ITP 7.9 en C19 y
C20, que sigue la que la propia NOTE-04 de ADASA uso.

Reparto por pagina (indices 0-based):
    0    caratula                 -> OBS-03
    1    encabezado, A, B, C1-C3  -> NOTE-02 (ancla C1)
    2    C4-C21, D1-D6            -> OBS-01 (ancla C21), NOTE-01 (ancla C10)
    3    D7-D13, E1-E3            -> OBS-02

OBS-02 va en la pagina 4 a proposito: es la unica con espacio en blanco, y las
Secciones D y E que muestra son justamente las que no traen ninguna de las dos
columnas. Colocarla sobre la tabla de la pagina 2 tapaba las dos columnas que la
observacion cita.
    4-5  Consolidated Comment Sheet
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-013_B_Quality_Dossier_Index.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-013_B_Quality_Dossier_Index_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 77",
        "P22-BA-09-000-013_B_Quality Dossier.pdf"))
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
        "search": "Certificate Release ADASA",
        "page_fallback": 2,
        "offset_y": -160,   # sube la caja para que NOTE-01 quepa debajo en la misma lamina
        "text": (
            "OBS-01: the comment sheet reports the FAT Approval\n"
            "Certificate as incorporated at C21. C21 is titled\n"
            "Certificate Release ADASA and points to row 8.4 of\n"
            "the Inspection and Test Plan, the Release for\n"
            "Dispatch. The FAT Approval Certificate is row 7.9,\n"
            "a hold point, and the Technical Specification\n"
            "(P22-ET-09-000-001-0), Section 8 - Inspections\n"
            "During Manufacturing, makes it an integral and\n"
            "indispensable part of the final quality dossier.\n"
            "It has no chapter here.\n"
            "Correct: add a chapter for it, distinct from C21."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "ELECTRICAL EQUIPMENT AND INSTRUMENTS",
        "page_fallback": 3,
        "text": (
            "OBS-02: the two columns asked for at Transmittal\n"
            "N30 are in place and largely empty. Section B\n"
            "carries a document number with no revision and no\n"
            "status and no Inspection and Test Plan row;\n"
            "Section C carries the plan row with no document\n"
            "number; Sections A, D and E carry neither. No line\n"
            "in the index carries an inclusion status.\n"
            "As issued the index still cannot serve as the\n"
            "checklist for the review that the Inspection and\n"
            "Testing Base Plan (P22-IT-09-000-001-0) assigns to\n"
            "ADASA.\n"
            "Correct: complete the document number, revision and\n"
            "inclusion status on every line, and the plan row on\n"
            "Sections A, B, D and E."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "Quality Dossier Index",
        "page_fallback": 0,
        "text": (
            "OBS-03: the Inspection and Test Plan provides for\n"
            "two indices with distinct names and distinct\n"
            "control levels: the preliminary index of row 7.6,\n"
            "which ADASA reviews, and the final index of row\n"
            "8.3, which is a hold point for both parties. This\n"
            "issue does not state which of the two it is, and\n"
            "the document title changed from Fabrication and\n"
            "Testing Dossier Index to Quality Dossier Index\n"
            "under the same code without saying so.\n"
            "Correct: state on the cover which of the two\n"
            "indices this document is, and keep the same chapter\n"
            "numbering in both."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Packaging report",
        "offset_y": 0,
        "page_fallback": 2,
        "text": (
            "NOTE-01: C9 and C10 close the dispatch chapter\n"
            "against rows 8.1 and 8.2. Two items of that\n"
            "request are not reflected: the packing list, which\n"
            "row 9.1 calls for at delivery, and the marking\n"
            "records.\n"
            "Correct: name both in the dispatch chapter."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "Material Traceability Report",
        "page_fallback": 1,
        "text": (
            "NOTE-02: C1 now carries the material traceability\n"
            "report against row 2.1 of the Inspection and Test\n"
            "Plan, which is the right location. The point raised\n"
            "at Transmittal N30 was the level of detail: the\n"
            "mill certificates of the super duplex material are\n"
            "to be identified spool by spool, with the PREN\n"
            "above 40 verification for UNS S32750 that row 2.1\n"
            "requires.\n"
            "Correct: state that identification in C1."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
