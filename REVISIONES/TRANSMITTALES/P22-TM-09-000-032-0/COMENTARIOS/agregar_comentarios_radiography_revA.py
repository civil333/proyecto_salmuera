#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_radiography_revA.py
Anota el Radiography Examination Procedure Rev A (P22-BA-09-000-015) del
submittal 25007-0075. Veredicto del TM N32: Code 3 - To be revised.

len(COMENTARIOS) = 5, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: primera emision, en respuesta al pedido de la Seccion 2 del TM N30.
Los dos determinantes:
  1. La clausula 23.0 da un menu de cinco codigos sin fijar cual gobierna. El
     NDE Plan Rev C aprobado fija ASME B31.3 para. 341.3.2.
  2. La clausula 12.1 fija la borrosidad geometrica en 1,8 mm, que NO es una
     fila de la tabla de T-274 sino la DISPENSA del parrafo PW-51.1 de ASME
     Seccion I: alli T-274 se usa "as a guide" y se fija un umbral unico de
     rechazo de 0,07" para items con sello PP. El designador PP es power piping
     y su paquete de codigos incluye B31.1, no B31.3. Este modulo es canieria
     de proceso B31.3, cuyo parrafo 344.5.1 remite la radiografia INTEGRA al
     Articulo 2 de la Seccion V, sin dispensa, de modo que rige T-274: para
     pared bajo 2" el limite es 0,020" (0,51 mm). Las lineas con 10% RT en la
     Line List aprobada son DN65, DN80 y DN100, de 6,02 a 8,56 mm de pared;
     el rango 3,7 a 11 mm sale de la Piping Specification e incluye lineas
     de PVC sin END.
     Citar "ASME Seccion V, Articulo 2, T-274" SIN sufijo: el rotulo "T-274.2"
     no se pudo confirmar en una edicion vigente y existe un I-274.2 distinto
     en el apendice de radiografia en movimiento.

NO se objeta la tecnica, el sistema de identificacion, las densidades de
pelicula ni la calificacion de los radiografos, que estan correctas.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-015_A_Radiography_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-015_A_Radiography_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-015_A_Radiography Examination Procedure.pdf",
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
        "search": "ASME Section VIII Div. 1, Full RT UW-51",
        "page_fallback": 20,
        "text": (
            "OBS-01 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "The acceptance criteria are given as a\n"
            "list of five codes without stating which one\n"
            "governs this project, so the interpreter\n"
            "chooses. Three of the five are pressure vessel\n"
            "and gas transmission codes that do not apply\n"
            "to this scope.\n"
            "The NDE Plan (P22-BA-09-000-005) Rev C,\n"
            "approved at Code 1, sets ASME B31.3 para.\n"
            "341.3.2 for the super duplex high-pressure\n"
            "circuit.\n"
            "Correct: state ASME B31.3 para. 341.3.2 and\n"
            "Table 341.3.2 as the acceptance criteria."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "1.8 mm",
        "page_fallback": 12,
        "text": (
            "OBS-02 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "The only geometric unsharpness limit\n"
            "stated is the dispensation of paragraph\n"
            "PW-51.1 of ASME Section I, which allows T-274\n"
            "to be used as a guide and sets a single\n"
            "rejection threshold of 0.07 in. (1.8 mm) for\n"
            "items carrying the PP stamp, that is power\n"
            "piping to ASME B31.1.\n"
            "This module is process piping to ASME B31.3,\n"
            "whose paragraph 344.5.1 refers radiography\n"
            "wholly to Section V, Article 2, with no such\n"
            "dispensation. Under T-274 the unsharpness of a\n"
            "wall under 2 in. shall not exceed 0.020 in.\n"
            "(0.51 mm). The lines carrying 10% radiography\n"
            "on the approved Line List are DN65, DN80 and\n"
            "DN100, of ASTM A790 UNS S32750, that is 6.02\n"
            "to 8.56 mm of wall.\n"
            "Correct: state the T-274 limit applicable to\n"
            "the wall radiographed on this module."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "3-inch thickness using Gamma ray",
        "page_fallback": 8,
        "text": (
            "OBS-03 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The scope covers this module, whose\n"
            "radiographed welds are ASTM A790 UNS S32750 of\n"
            "6.02 to 8.56 mm of wall, on lines DN65, DN80\n"
            "and DN100 of the approved Line List. What is\n"
            "not stated is that this is the range examined.\n"
            "Correct: declare the material and the thickness\n"
            "range of this project, and confirm that the\n"
            "iridium 192 source, the source to object\n"
            "distances and the film class meet the image\n"
            "quality indicator sensitivity of ASME Section\n"
            "V, Article 2 over that range."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "PACKING OF FILMS",
        # page_min salta la tabla de contenidos del anexo (pagina 8), donde la
        # misma cadena aparece como linea de indice.
        "page_min": 20,
        "page_fallback": 21,
        "text": (
            "OBS-04 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The numbering does not run. Through\n"
            "the body each heading carries sub-clauses one\n"
            "number behind it - clause 12.0 with 11.1 to\n"
            "11.3, clause 13.0 with 12.1, clause 14.0 with\n"
            "13.1 to 13.5 - and clause 15.0 Packing of Films\n"
            "appears here after clause 24.0 Examination\n"
            "Records.\n"
            "Correct: renumber so that each clause can be\n"
            "cited without ambiguity, which matters when a\n"
            "report refers to it."
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
            "PROV-PROC-RT-001. The reference clause cites\n"
            "Article 9 of ASME Section V, the visual\n"
            "examination article; that list is inherited\n"
            "from the reference section of the NDE Plan,\n"
            "which ADASA will align at its next issue. The\n"
            "attached procedure correctly cites Article 2 at\n"
            "the 2025 edition.\n"
            "Correct: state the purpose and the document\n"
            "number of this procedure, and cite Article 2."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
