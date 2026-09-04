#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ga_swro_skid_rev0.py
Anota el GA of SWRO System Skid Rev 0 (P22-DWG-09-005-008) del submittal
25007-0084 (ENTREGA 84). Veredicto del TM N36: Code 3 - To be revised.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Rev 0 emitido para construccion que responde al TM N31, subseccion
2.4, Code 2. Ese Code 2 tuvo UNA sola accion, corregir tres referencias
documentales del bloque de notas, y ese es el universo entero de esta revision.
  Nota 7, Line List          -> CERRADA en las dos hojas. No se anota.
  Nota 8, codigo invalido    -> NO CERRADA -> OBS-01. Es la que fija el codigo.
  Nota 6, Instrument List    -> CIERRE PARCIAL: corregida en la Hoja 2 y no en
      la Hoja 1 -> OBS-02

NO SE ANOTA, per la regla de alcance:
  - El cajetin declara ISSUED FOR APPROVAL mientras la tabla de revisiones dice
    ISSUED FOR CONSTRUCTION, y las fechas de firma siguen en la Rev B.
    Housekeeping documental, observacion nueva.
  - La nota 5 cita la Valve List en Rev D. No estaba en el pedido de las tres
    referencias.

Reparto por pagina (indices 0-based):
    1   Hoja 1, bloque de notas -> OBS-01 y OBS-02 (las dos viven en la Hoja 1)
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_0_GA_SWRO_System_Skid.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_0_GA_SWRO_System_Skid_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 84", "25007-0084",
        "P22-DWG-09-005-008_0 GA of SWRO System Skid.pdf",
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
        "search": "NOMINAL THICKNESS",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-01: note 8 is unchanged on both sheets and\n"
            "the evidence submitted to justify it confirms\n"
            "the point instead of answering it.\n"
            "The note reads P22-ET-09-006-01, which is not a\n"
            "valid document code in the project numbering:\n"
            "the sequential field carries three digits. The\n"
            "comment sheet answers that a snapshot shows the\n"
            "number was submitted earlier in the project.\n"
            "That snapshot, attached as the last page of\n"
            "this file, writes the code as P22-ET-09-006-001\n"
            "and the row below it as P22-ET-09-006-002.\n"
            "This note is the one that points to the nominal\n"
            "wall thickness per pipeline, on a drawing issued\n"
            "for construction. As written, the fabricator\n"
            "cannot locate the specification that governs\n"
            "the thickness.\n"
            "Correct: write the Piping Material Specification\n"
            "as P22-ET-09-006-001 on both sheets, with its\n"
            "revision index."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "INSTRUMENT LIST REV.D",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "OBS-02: note 6 was corrected on one sheet only.\n"
            "Sheet 2 now reads P22-LI-09-008-003 INSTRUMENT\n"
            "LIST REV.E, which is the current revision. This\n"
            "sheet still reads REV.D, which is superseded.\n"
            "The comment sheet states that notes 6 and 7 were\n"
            "corrected accordingly; note 7 was corrected on\n"
            "both sheets and note 6 on one.\n"
            "Two sheets of the same drawing referring the\n"
            "same instrument function matrix to two different\n"
            "revisions is not resolvable by the reader.\n"
            "Correct: align note 6 on this sheet to REV.E,\n"
            "and check the remaining notes of both sheets\n"
            "against the current revision of each referred\n"
            "document before re-issuing."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
