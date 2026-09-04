#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_radiography_revB.py
Anota el Radiography Examination Procedure Rev B (P22-BA-09-000-015) del
submittal 25007-0081 (ENTREGA 81). Veredicto del TM N35: Code 3 - To be revised.

len(COMENTARIOS) = 3, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N32. Solo cierre de los puntos del N32.
  OBS-01 del N32 (criterio en la clausula 23.0) -> CIERRE PARCIAL: la Tabla
      341.3.2-1 de B31.3-2024 si se incorporo como pagina nueva del anexo, pero
      la clausula conserva la lista de cinco codigos -> OBS-01
  OBS-02 del N32 (borrosidad geometrica)        -> NO CERRADA, sin un solo
      cambio. Es la que decide el codigo -> OBS-02
  OBS-03, OBS-04 y NOTE-01 del N32 (aseo)       -> NINGUNA atendida -> NOTE-01

EL RECONOCIMIENTO DE LA TABLA NO ES CORTESIA. La pagina 23 del anexo entra como
imagen y no aparece en la extraccion de texto: se verifico por render a 200 dpi.
Sin ese render se habria afirmado una ausencia falsa. Va escrito en la OBS-01
porque es el unico avance real de esta revision.

CITACION DEL LIMITE. Citar "ASME Section V, Article 2, T-274" SIN sufijo: el
rotulo "T-274.2" no se pudo confirmar en la edicion vigente y el texto emitido
en el TM N32 ya lo evita.

Reparto por pagina (indices 0-based):
    0   caratula                      -> NOTE-01
    12  clausula 12.1, borrosidad     -> OBS-02
    20  clausula 23.0                 -> OBS-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-015_B_Radiography_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-015_B_Radiography_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 81",
        "P22-BA-09-000-015_B_Radiography Examination Procedure.pdf",
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
        "search": "The acceptance and rejection criteria shall be",
        "page_fallback": 20,
        "text": (
            "OBS-01: the table was added, the list of\n"
            "five codes was not removed.\n"
            "Acknowledged: Table 341.3.2-1 of ASME B31.3\n"
            "2024 is now attached in full at the end of the\n"
            "procedure, which is what Transmittal N32 asked\n"
            "for.\n"
            "This clause, however, still opens with the\n"
            "formula that the criteria shall be in\n"
            "accordance with the specific contract\n"
            "specification, codes and standards, and still\n"
            "lists five of them. Three are pressure vessel\n"
            "and gas transmission codes that do not govern\n"
            "this scope, and the interpreter still chooses.\n"
            "Correct: state ASME B31.3 para. 341.3.2 and\n"
            "Table 341.3.2 as the acceptance criteria of\n"
            "this project, in place of the list."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "shall not exceed 1.8 mm",
        "page_fallback": 12,
        "text": (
            "OBS-02: unchanged since Rev A. This is\n"
            "the second time it is raised, and it is what\n"
            "governs the response code of this document.\n"
            "The only geometric unsharpness limit stated is\n"
            "1.8 mm, which is the dispensation of paragraph\n"
            "PW-51.1 of ASME Section I for items carrying\n"
            "the PP stamp, that is power piping to ASME\n"
            "B31.1. This module is process piping to ASME\n"
            "B31.3, whose paragraph 344.5.1 refers\n"
            "radiography wholly to Section V, Article 2,\n"
            "with no such dispensation.\n"
            "The lines carrying 10 percent radiography on\n"
            "the approved Line List are DN65, DN80 and\n"
            "DN100 of ASTM A790 UNS S32750, that is 6.02 to\n"
            "8.56 mm of wall. For that wall, T-274 of ASME\n"
            "Section V, Article 2 requires 0.020 in.\n"
            "As written the procedure admits an unsharpness\n"
            "three and a half times the code limit.\n"
            "Correct: state the T-274 limit applicable to\n"
            "the wall radiographed on this module."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Radiography Examination Procedure",
        "page_fallback": 0,
        "text": (
            "NOTE-01: the three tidying items of\n"
            "Transmittal N32 are unattended, and this\n"
            "revision carries no consolidated comment\n"
            "sheet.\n"
            "The scope of the attached procedure still does\n"
            "not declare the material and the thickness\n"
            "range of this project; the numbering still\n"
            "does not run, with each heading carrying\n"
            "sub-clauses one number behind it and clause\n"
            "15.0 appearing after clause 24.0; and the\n"
            "cover section still describes this document as\n"
            "a positive material identification procedure\n"
            "and cites Article 9 instead of Article 2.\n"
            "Correct: close the three items with Rev C and\n"
            "issue the comment sheet with it. They do not\n"
            "hold the re-issue."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
