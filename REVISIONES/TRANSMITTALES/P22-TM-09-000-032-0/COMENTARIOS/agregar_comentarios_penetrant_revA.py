#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_penetrant_revA.py
Anota el Liquid Penetrant Examination Procedure Rev A (P22-BA-09-000-014) del
submittal 25007-0075. Veredicto del TM N32: Code 3 - To be revised.

len(COMENTARIOS) = 5, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: primera emision, en respuesta al pedido de la Seccion 2 del TM N30
sobre el Dossier Index. Se revisa completo. Toda observacion cita el requisito
que la sostiene: el NDE Plan P22-BA-09-000-005 Rev C (Codigo 1, TM N26) fija
ASME B31.3 para. 341.3.2 como criterio de aceptacion del circuito de alta en
super duplex, y el frontispicio del propio documento fija las ediciones.

NO se objeta el formato del procedimiento del subcontratista ni la calificacion
del personal, que esta correctamente declarada contra la Seccion 2.0 del
NDE Plan.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-014_A_Liquid_Penetrant_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-014_A_Liquid_Penetrant_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-014_A_Liquid Penetrant Examination Procedure.pdf",
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
        "search": "ASME Section VIII Div. 1, Appendix 6",
        "page_fallback": 15,
        "text": (
            "OBS-01 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "Appendix 6 of ASME Section VIII Div. 1\n"
            "is the appendix for magnetic particle\n"
            "examination, not for liquid penetrant, so this\n"
            "clause cites the criteria of another method and\n"
            "of the pressure vessel code.\n"
            "The Technical Specification\n"
            "(P22-ET-09-000-001-0), Section 8 - Inspections\n"
            "During Manufacturing, and the NDE Plan\n"
            "(P22-BA-09-000-005) Rev C approved at Code 1\n"
            "both set ASME B31.3 para. 341.3.2 for the super\n"
            "duplex high-pressure circuit, which is piping.\n"
            "Correct: state ASME B31.3 para. 341.3.2 and\n"
            "Table 341.3.2 here."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "ASME VIII DIV.1 Appendix 8",
        "page_fallback": 18,
        "text": (
            "OBS-02 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "This form declares Appendix 8 of ASME\n"
            "Section VIII Div. 1, which is the penetrant\n"
            "appendix and therefore the right method, but\n"
            "still the pressure vessel code, and it differs\n"
            "from the Appendix 6 of clause 13.0. The\n"
            "examiner cannot know which applies.\n"
            "Correct: state on the form the same criterion\n"
            "required by OBS-01, ASME B31.3 para. 341.3.2."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Report No: XESSB-ITS-PT230601",
        "page_fallback": 18,
        "text": (
            "OBS-03 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The report form carries the data of a\n"
            "different contract - report and job number\n"
            "ITS-PT230601, the penetrant batch numbers -\n"
            "and the result is already written in the\n"
            "Remarks column before any examination.\n"
            "Correct: issue the form blank, with the\n"
            "project and contract identification of this\n"
            "module."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "WI-OD-PT02, Rev.01",
        "page_fallback": 14,
        "text": (
            "OBS-04 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The attached procedure carries two\n"
            "revision indices. Its header reads Rev.00 on\n"
            "pages 1 to 9 and on page 14, and Rev.01 on\n"
            "pages 10 to 13, within the same document.\n"
            "Correct: issue the procedure under a single\n"
            "revision index, with its revision record."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "The purpose of this document is to provide the procedure for positive material",
        "page_fallback": 3,
        "text": (
            "NOTE-01 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The cover section describes this\n"
            "document as a positive material identification\n"
            "procedure, and its document number reads PMI\n"
            "PROV-PROC-PT-001. The reference clause cites\n"
            "Article 9 of ASME Section V, the visual\n"
            "examination article; that list is inherited\n"
            "from the reference section of the NDE Plan,\n"
            "which ADASA will align at its next issue. The\n"
            "attached procedure correctly cites Article 6,\n"
            "and its own reference list gives the 2021\n"
            "edition of B31.3 where the cover fixes 2024.\n"
            "Correct: state the purpose and the document\n"
            "number of this procedure, cite Article 6, and\n"
            "align the editions."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
