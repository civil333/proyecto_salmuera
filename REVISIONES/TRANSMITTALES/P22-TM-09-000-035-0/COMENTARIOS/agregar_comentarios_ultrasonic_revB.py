#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_ultrasonic_revB.py
Anota el Ultrasonic Thickness Procedure Rev B (P22-BA-09-000-016) del submittal
25007-0081 (ENTREGA 81). Veredicto del TM N35: Code 3 - To be revised.

len(COMENTARIOS) = 3, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N32. Solo cierre de los puntos del N32.
  OBS-01 del N32 (criterio de aceptacion) -> NO CERRADA: cambio de "at the
      discretion by the client" a un criterio de MATERIAL, no de espesor.
      Es la que decide el codigo -> OBS-01
  OBS-02 del N32 (hoja de tecnica)        -> CERRADA con residuo: el material
      esta declarado en el alcance, en el Apendice 1 y en el bloque de
      calibracion. Falta la velocidad de propagacion -> NOTE-01
  OBS-03 del N32 (plano de puntos)        -> abierta con fecha propia, NO era
      condicion de la Rev B. NO se anota aqui: se sigue en la Seccion 3
  OBS-04 y OBS-05 del N32 (aseo)          -> cierre parcial -> NOTE-02

DE LOS TRES PROCEDIMIENTOS, ESTE ES EL QUE MAS TRABAJO: nueve cambios de
contenido contra los dos del de radiografia y el uno del de penetrantes, y cerro
una de sus dos bloqueantes. Se reconoce por escrito en la OBS-01 y en la
NOTE-01. Decirlo no debilita el codigo: lo hace mas dificil de discutir.

NO SE ANOTA como observacion propia, per la regla de alcance: el manual del
equipo Olympus 38DL PLUS dentro del anexo, que estaba en la Rev A y nunca se
pidio quitar. Las designaciones mal escritas (UNS2750 por UNS S32750, SA79M por
SA790M, S32250 que no existe) van como clausula de los puntos que si se emiten,
no como observaciones sueltas, para no inflar el conteo.

Reparto por pagina (indices 0-based):
    0   caratula                          -> NOTE-02
    12  clausula 4.1, bloque de calibracion -> NOTE-01
    14  clausula 9.0, criterio            -> OBS-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-016_B_Ultrasonic_Thickness_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-016_B_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 81",
        "P22-BA-09-000-016_B_Ultrasonic Thickness Procedure.pdf",
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
        "search": "Acceptance as per ASME Section II",
        "page_fallback": 14,
        "text": (
            "OBS-01: the clause changed, the criterion\n"
            "did not. This is the second time it is raised,\n"
            "and it is what governs the response code.\n"
            "Rev A left acceptance at the discretion of the\n"
            "client and Rev B now cites SA-790, which is the\n"
            "material specification of the pipe: chemistry,\n"
            "mechanical properties and supply tolerances.\n"
            "It does not state when a thickness reading is\n"
            "acceptable.\n"
            "The NDE Plan (P22-BA-09-000-005) Rev C,\n"
            "approved at Code 1, sets it: the measured\n"
            "thickness shall be equal to or greater than the\n"
            "minimum required thickness of the applicable\n"
            "design code and the engineering calculation.\n"
            "That is the comparison a fabrication baseline\n"
            "measurement has to resolve, and it is absent.\n"
            "The designation is also written UNS2750 here\n"
            "and SA79M in the reference list.\n"
            "Correct: state the NDE Plan criterion in this\n"
            "clause, and write the material as UNS S32750."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Calibration Block Material Grade",
        "page_fallback": 12,
        "text": (
            "NOTE-01: the technique sheet is closed.\n"
            "The scope of the attached procedure, the\n"
            "calibration block of this clause and Appendix 1\n"
            "now all declare UNS S32750, where Rev A was\n"
            "written for carbon steel. This closes the\n"
            "second blocking item of Transmittal N32.\n"
            "Two residual points, which do not hold the\n"
            "re-issue: the sound velocity of the material is\n"
            "still not stated as a value, although the\n"
            "procedure does describe the velocity\n"
            "calibration on a block of the material; and\n"
            "S32250 is not a UNS designation, most likely\n"
            "S32205 was intended.\n"
            "Correct: state the sound velocity used for\n"
            "UNS S32750 and correct the second grade."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "Ultrasonic Thickness Procedure",
        "page_fallback": 0,
        "text": (
            "NOTE-02: the tidying items are partly\n"
            "closed, and this revision carries no\n"
            "consolidated comment sheet.\n"
            "Closed: the edition is now stated as ASME\n"
            "Section V 2025 throughout, and the report form\n"
            "no longer carries the report and job numbers of\n"
            "a different contract.\n"
            "Open: the form still declares Wallpaper Paste\n"
            "as couplant, which matches neither clause 5.0\n"
            "nor the technique sheet; the reference list\n"
            "still cites ASME E 797, a designation that does\n"
            "not exist, and the in-service inspection codes\n"
            "API 510, 570 and 653; and the cover section\n"
            "still describes this document as a positive\n"
            "material identification procedure and cites\n"
            "Article 9 instead of Article 5.\n"
            "Correct: close these with Rev C and issue the\n"
            "comment sheet with it."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
