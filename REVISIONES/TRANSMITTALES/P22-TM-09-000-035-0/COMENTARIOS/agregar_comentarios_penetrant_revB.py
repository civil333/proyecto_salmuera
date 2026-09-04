#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_penetrant_revB.py
Anota el Liquid Penetrant Examination Procedure Rev B (P22-BA-09-000-014) del
submittal 25007-0081 (ENTREGA 81). Veredicto del TM N35: Code 3 - To be revised.

len(COMENTARIOS) = 3, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N32. Se revisa SOLO el cierre de los
puntos del N32, sin observaciones nuevas.
  OBS-01 del N32 (criterio en la clausula 13.0) -> CIERRE PARCIAL: se agrego el
      bloque B31.3 pero se mantiene el Apendice 6, sin declarar cual gobierna
      -> OBS-01
  OBS-02 del N32 (criterio en el formulario)    -> NO CERRADA, sin un solo
      cambio -> OBS-02
  OBS-03, OBS-04 y NOTE-01 del N32 (aseo)       -> NINGUNA atendida -> NOTE-01,
      agrupadas en un solo comentario porque son el mismo lote que el N32 ya
      declaro que no retiene la reemision
La NOTE-01 lleva ademas la hoja de comentarios ausente, que se levanta en este
documento por ser el primero de los tres procedimientos de ensayos no
destructivos.

MATIZ QUE NO SE OMITE, y por eso va escrito en la OBS-01: los umbrales del
criterio B31.3 que se agrego coinciden digito a digito con los del Apendice 6.
El riesgo de un resultado distinto es nulo; lo que sostiene el codigo es el
codigo que citara el registro que entra al dossier.

NO SE ANOTA, per la regla de alcance: la clausula 9.2 duplicada y el limite de
cloro mas fluor enunciado para aceros austeniticos. Ninguno se pidio en el N32.
Ver ENTREGAS_BWWATER/ENTREGA 81/_HALLAZGOS_DETERMINISTAS.md.

Reparto por pagina (indices 0-based):
    0   caratula                      -> NOTE-01
    15  clausula 13.0                 -> OBS-01
    18  formulario del Apendice 1     -> OBS-02
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-014_B_Liquid_Penetrant_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-014_B_Liquid_Penetrant_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 81",
        "P22-BA-09-000-014_B_Liquid Penetrant Examination Procedure.pdf",
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
            "OBS-01: the acceptance criterion of\n"
            "Transmittal N32 was added, but the one it\n"
            "was meant to replace is still here.\n"
            "This clause now offers two criteria side by\n"
            "side, a. Appendix 6 of ASME Section VIII Div. 1\n"
            "and b. ASME B31.3, without stating which one\n"
            "governs, so the examiner still chooses. The\n"
            "B31.3 paragraph is not cited by its number.\n"
            "Acknowledged: the thresholds of the added\n"
            "text match those of Appendix 6 digit for\n"
            "digit, so no examination result changes. What\n"
            "does change is the code the record cites when\n"
            "it enters the fabrication dossier.\n"
            "Correct: state ASME B31.3 para. 341.3.2 and\n"
            "Table 341.3.2 as the single criterion, and\n"
            "delete the reference to Appendix 6, which\n"
            "belongs to another examination method."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "ASME VIII DIV.1 Appendix 8",
        "page_fallback": 18,
        "text": (
            "OBS-02: unchanged since Rev A. This is\n"
            "the second time it is raised.\n"
            "The report form still declares Appendix 8 of\n"
            "ASME Section VIII Div. 1. This is the form the\n"
            "examiner signs and the sheet that enters the\n"
            "dossier, and it cites the pressure vessel code\n"
            "for a piping circuit, differing as well from\n"
            "clause 13.0 of this same procedure.\n"
            "Correct: state ASME B31.3 para. 341.3.2 on\n"
            "this form, matching clause 13.0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Liquid Penetrant Examination Procedure",
        "page_fallback": 0,
        "text": (
            "NOTE-01: this revision carries no\n"
            "consolidated comment sheet.\n"
            "The three non-destructive testing procedures\n"
            "of this submittal are re-issued without stating\n"
            "how each comment of Transmittal N32 was\n"
            "answered, so ADASA verified the closure by\n"
            "comparing the text of Rev A against Rev B. The\n"
            "two procedures issued above Rev 0 in this same\n"
            "submittal do carry it.\n"
            "None of the three tidying items of Transmittal\n"
            "N32 was attended either: the report form still\n"
            "carries the job number, the batch numbers and\n"
            "the result of a different contract; the attached\n"
            "procedure still alternates Rev.00 and Rev.01\n"
            "within the same document; and the cover section\n"
            "still describes this document as a positive\n"
            "material identification procedure and cites\n"
            "Article 9 instead of Article 6.\n"
            "Correct: issue the comment sheet with Rev C\n"
            "and close the three items above at the same\n"
            "issue. They do not hold the re-issue."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
