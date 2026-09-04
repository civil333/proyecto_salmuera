#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_project_schedule_revB.py
Anota el Project Schedule Rev B (P22-BA-09-000-001) del submittal 25007-0084
(ENTREGA 84). Veredicto del TM N36: Code 3 - To be revised.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

ALCANCE. Re-emision que responde al TM N20, subseccion 2.16, Code 2, con dos
observaciones mayores. Las dos son el universo de esta revision.
  OBS-01 del N20, base de certificacion de los recipientes -> NO CERRADA
  OBS-02 del N20, ensayos de presion como actividades fechadas -> NO CERRADA
  Tercera clausula, no reabrir la adopcion de la linea base -> CUMPLIDA, y se
      reconoce por escrito dentro de OBS-01.

NO SE ANOTA, per la regla de alcance: la tarea 419 rotula ADISA en vez de
ADASA, y el documento no declara fecha de corte ni version de linea base.
Ninguno de los dos estaba en la accion del TM N20.

EL FONDO DEL CRONOGRAMA NO VA AQUI. El desplazamiento del ex-works y del fin
de programa es materia contractual y viaja por su propia cadena de correo. Este
PDF solo anota el cumplimiento de las dos observaciones documentales.

Reparto por pagina (indices 0-based):
    10  bloque RO Pressure Vessel / Tubes -> OBS-01
    13  tarea Factory Acceptance Test     -> OBS-02
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-001_B_Project_Schedule.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-001_B_Project_Schedule_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 84", "25007-0084",
        "P22-BA-09-000-001_B Project Schedule.pdf",
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
        "search": "RO Pressure Vessel",
        "page_fallback": 10,
        "page_min": 10,
        "text": (
            "OBS-01: the certification basis of the pressure\n"
            "vessels is still not stated.\n"
            "The words ASME, stamp, certification and waiver\n"
            "do not appear anywhere in the fourteen pages.\n"
            "This block runs PR/PO, drawing approval,\n"
            "manufacturing and shipping with no certification\n"
            "or release activity between them, and the\n"
            "ex-works date corresponds to the non-stamped\n"
            "route accepted under the ADASA waiver of\n"
            "02-Jun-2026.\n"
            "The vessels are now shown complete and received\n"
            "in Penang. Whatever documentary evidence\n"
            "replaced the code stamp has to be traceable in\n"
            "the programme that governs the works.\n"
            "The baseline adoption of 09-Jun-2026 is not\n"
            "re-opened by this: the Baseline1 column still\n"
            "carries its four anchor dates unchanged, and\n"
            "ADASA acknowledges that.\n"
            "Correct: state the certification basis of the\n"
            "vessels consistent with the 02-Jun-2026 waiver."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Factory Acceptance Test for System",
        "page_fallback": 13,
        "page_min": 13,
        "text": (
            "OBS-02: no pressure test appears anywhere in\n"
            "the programme.\n"
            "The words hydrostatic, pressure test and leak\n"
            "test have no occurrence in the fourteen pages.\n"
            "The only two tasks containing the word Test are\n"
            "this one and the Performance Test at site.\n"
            "This task carries no subtasks, so it does not\n"
            "hold the pre-FAT system hydrostatic tests\n"
            "either, and the factory hydrostatic test of the\n"
            "vessels is absent from the vessel block.\n"
            "Those tests feed the fabrication and testing\n"
            "dossier, which remains undelivered, and the\n"
            "hold points of the Inspection and Test Plan.\n"
            "A test that is not programmed cannot be\n"
            "witnessed.\n"
            "Correct: add the factory vessel hydrostatic test\n"
            "and the pre-FAT system hydrostatic tests as\n"
            "discrete, dated activities, and state which of\n"
            "them have already been executed."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
