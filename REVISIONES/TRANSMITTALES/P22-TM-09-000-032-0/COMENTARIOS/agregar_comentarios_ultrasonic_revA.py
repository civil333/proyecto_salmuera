#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ultrasonic_revA.py
Anota el Ultrasonic Thickness Procedure Rev A (P22-BA-09-000-016) del submittal
25007-0075. Veredicto del TM N32: Code 3 - To be revised.

len(COMENTARIOS) = 6, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: primera emision, en respuesta al pedido de la Seccion 2 del TM N30.
El determinante es la clausula 9.0: el documento no tiene criterio de
aceptacion, lo deja "a discrecion del cliente". El NDE Plan Rev C aprobado lo
fija (espesor medido mayor o igual al minimo requerido por el codigo de diseño
y el calculo de ingenieria), y el proyecto ya califico en el TM N23 que un
procedimiento de ensayo sin su criterio vinculante no es ejecutable ni
testificable.

La fila 7.8 del ITP Rev 0 exige ademas un plano de puntos de medicion junto al
procedimiento, que no vino.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-016_A_Ultrasonic_Thickness_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-016_A_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-016_A_Ultrasonic Thickness Procedure.pdf",
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
        "fill": CRITICAL,
        "search": "Acceptance or rejection shall be the discretion by the client",
        "page_fallback": 13,
        "text": (
            "OBS-01 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "The procedure has no acceptance\n"
            "criterion. As written the examination cannot\n"
            "be executed or witnessed, because nothing\n"
            "states when a reading is acceptable.\n"
            "The NDE Plan (P22-BA-09-000-005) Rev C,\n"
            "approved at Code 1, sets it: the measured\n"
            "thickness shall be equal to or greater than\n"
            "the minimum required thickness of the\n"
            "applicable design code and the engineering\n"
            "calculation.\n"
            "Correct: state that criterion in clause 9.0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Material : Carbon Steel",
        "page_fallback": 14,
        "text": (
            "OBS-02 - BLOCKING, correct before this\n"
            "procedure is used.\n"
            "The technique sheet is written for\n"
            "carbon steel. The high-pressure piping of this\n"
            "module is ASTM A790 UNS S32750, whose sound\n"
            "velocity differs from that of carbon steel, so\n"
            "a gauge calibrated on a carbon steel block\n"
            "reads a biased thickness.\n"
            "Correct: write the technique sheet for\n"
            "UNS S32750, stating the sound velocity and the\n"
            "calibration block for that material."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        # Ancla en el alcance del anexo (pagina 9), no en la clausula 8.1: alli
        # el cuadro tapaba la lista de contenidos minimos del informe.
        "search": "any other configuration that requires a straight beam",
        "page_fallback": 8,
        "text": (
            "OBS-03 - separate, with its own date before\n"
            "the baseline measurement is taken.\n"
            "No measurement points are defined.\n"
            "Row 7.8 of the Inspection and Test Plan\n"
            "(P22-BA-09-000-004 Rev 0) requires the\n"
            "baseline thickness measurement to be performed\n"
            "at the points of a measurement point drawing\n"
            "submitted alongside this procedure, and that\n"
            "drawing has not been received.\n"
            "Correct: submit the measurement point drawing,\n"
            "or state in this procedure how the points are\n"
            "defined and recorded."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "AIR RECEIVER VERTICAL",
        "page_fallback": 15,
        "text": (
            "OBS-04 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The report form belongs to a different\n"
            "contract - job XIYIN-UG230601, item AIR\n"
            "RECEIVER VERTICAL, with the sketch of a\n"
            "vertical vessel and a couplant that the body\n"
            "of the procedure does not list.\n"
            "Correct: issue the form blank, for the piping\n"
            "of this module, with a single couplant\n"
            "declared consistently."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MENOR,
        "search": "as per ASME Sec. V 2023",
        "page_fallback": 5,
        "text": (
            "OBS-05 - to be tidied at the same issue; it\n"
            "does not hold the re-issue.\n"
            "The attached procedure states the 2023\n"
            "edition of ASME Section V while the cover\n"
            "section of this same document fixes the 2025\n"
            "edition.\n"
            "Correct: state one edition. Its reference list\n"
            "also cites ASME E 797, a designation that does\n"
            "not exist: Section V adopts that standard as\n"
            "SE-797 in Article 23. And the codes listed are\n"
            "the in-service inspection codes API 510, 570\n"
            "and 653; state the codes that govern a\n"
            "fabrication baseline measurement."
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
            "PROV-PROC-UT-001, where row 7.8 of the\n"
            "Inspection and Test Plan identifies the\n"
            "ultrasonic procedure. The reference clause\n"
            "cites Article 9 of ASME Section V, the visual\n"
            "examination article; that list is inherited\n"
            "from the reference section of the NDE Plan,\n"
            "which ADASA will align at its next issue.\n"
            "Correct: state the purpose and the document\n"
            "number of this procedure, and cite Article 5,\n"
            "Ultrasonic Examination Methods for Materials\n"
            "and Fabrication."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
