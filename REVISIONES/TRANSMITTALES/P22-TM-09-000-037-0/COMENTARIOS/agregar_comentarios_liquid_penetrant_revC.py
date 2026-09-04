#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_liquid_penetrant_revC.py
Anota el Liquid Penetrant Examination Procedure Rev C (P22-BA-09-000-014) del
submittal 25007-0086 (ENTREGA 86). Veredicto del TM N37: Code 2 - Approved as noted.

len(COMENTARIOS) = 4, espejo 1:1 del bloque Action de la subseccion 2.1
("OBS-01 to OBS-03 and NOTE-01 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N35, subseccion 2.3, Code 3, que a su vez
venia del TM N32. Solo se revisa contra esa instruccion escrita; no se introducen
observaciones nuevas.

  OBS-01 del N35, criterio unico en la clausula 13.0     -> CERRADO. No se anota.
  OBS-02 del N35, el mismo criterio en el formulario     -> CERRADO. No se anota.
  NOTE-01 (a) del N35, formulario en blanco              -> NO CERRADO -> OBS-01 y OBS-02
  NOTE-01 (b) del N35, indice de revision unico          -> CIERRE PARCIAL -> OBS-03
  NOTE-01 (c) del N35, proposito, numero de documento    -> CIERRE PARCIAL -> NOTE-01

El determinante cerro —la clausula 13.0 ofrece hoy un solo criterio y el formulario
que firma el examinador declara ese mismo criterio con su numero de parrafo— de modo
que el Code 3 ya no se sostiene. Lo que queda es el formulario, que es la hoja que
entra al dossier de calidad, y es la SEGUNDA vez que se levanta: la hoja de
comentarios responde "Revised as per comment" a un bloque que nombra textualmente
los datos del formulario de otro contrato, y ese formulario esta intacto.

Reparto por pagina (indices 0-based):
    1    portada del procedimiento adjunto       -> NOTE-01
    18   formulario de informe (pagina 19 de 22) -> OBS-01, OBS-02, OBS-03
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-014_C_Liquid_Penetrant.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 86",
        "P22-BA-09-000-014_C_Liquid Penetrant Examination Procedure.pdf",
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
        "search": "Report No",
        "page_fallback": 18,
        "page_min": 18,
        "text": (
            "OBS-01: the report form still carries the\n"
            "identifiers of another contract.\n"
            "This form is unchanged from Rev B. It reads\n"
            "Report No: XESSB-ITS-PT230601(Cth) and Job No:\n"
            "(Cth: ITS-PT230601), and it carries three\n"
            "consumable batch numbers, 2408019, 2405026 and\n"
            "2404074, from that same examination.\n"
            "This is the sheet that enters the fabrication\n"
            "and testing dossier of this module. Issued with\n"
            "another project already filled in, it cannot\n"
            "record an examination of this one.\n"
            "This point was raised at Transmittal N32 and\n"
            "again at Transmittal N35, and the comment sheet\n"
            "of this revision answers Revised as per comment\n"
            "to a block that names the report form data of\n"
            "another contract.\n"
            "Correct: issue the form blank, with the project\n"
            "and contract identification of this module, when\n"
            "the procedure is issued at Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "No Relevant Indication",
        "page_fallback": 18,
        "page_min": 18,
        "text": (
            "OBS-02: the observations column is pre-written\n"
            "with the result.\n"
            "The column reads No Relevant Indication Was\n"
            "Found During PT Examination Time before any\n"
            "examination has taken place.\n"
            "A form that states the outcome in advance is not\n"
            "a record: the examiner has nothing left to\n"
            "declare, and the signature below it certifies a\n"
            "sentence printed at the works.\n"
            "Correct: leave the observations column blank on\n"
            "the issued form, for the examiner to complete."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Rev.00",
        "page_fallback": 18,
        "page_min": 18,
        "text": (
            "OBS-03: the revision index inside the form does\n"
            "not match the document.\n"
            "ADASA acknowledges the closure across the body:\n"
            "the fifteen page headers of the attached\n"
            "procedure now read WI-OD-PT02, Rev.C uniformly,\n"
            "where Rev B alternated Rev.00 and Rev.01.\n"
            "The Procedure field inside this form still reads\n"
            "WI-OD-PT02, Rev.00, and it is the only Rev.00\n"
            "left in the file.\n"
            "Correct: align this field with the issued\n"
            "revision of the procedure at Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "PMI PROV-PROC-PT-001",
        "page_fallback": 1,
        "page_min": 1,
        "text": (
            "NOTE-01: the document number belongs to a\n"
            "different procedure.\n"
            "ADASA acknowledges what closed here: the purpose\n"
            "clause now reads the procedure for liquid\n"
            "penetrant examination, where it read positive\n"
            "material identification, and the code editions\n"
            "were aligned to ASME B31.3 2024.\n"
            "This page still reads DOC NO: PMI\n"
            "PROV-PROC-PT-001, which is the number of a\n"
            "positive material identification procedure.\n"
            "Correct: state the document number of this\n"
            "procedure at Rev 0."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
