#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_hp_lp_rev0.py
Anota el HP and LP Pressure Test Procedure Rev 0 (P22-BA-09-000-010) del
submittal 25007-0075. Veredicto del TM N32: devuelto SIN CODIGO de respuesta.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

ALCANCE: dos peticiones del correo del 06-Ago tocaban este documento. La de la
edicion CERRO: las clausulas 5.5.2 y 5.6.3 pasaron de "the latest edition/
addenda of ASME B31.3" a "the ASME B31.3 2024 edition". La del formulario de
registro NO: la clausula 5.8.1 sigue nombrando un "Pressure Test Report" que no
viene en el submittal y que ningun formulario controlado de este procedimiento
produce, mientras la fila 5.2 del ITP Rev 0 exige un grafico presion-tiempo como
certificado de un Punto de Detencion, con el ensayo el 13 y 14 de agosto.

Este documento estuvo en Codigo 1 en el primer borrador del transmittal. La
verificacion adversarial lo volteo con dos argumentos comprobados contra la
fuente: la fila 5.2 del ITP exige el grafico, y es el mismo defecto que, cerrado,
le vale el Codigo 1 al Visual Procedure en este mismo transmittal.

TRIAJE DEL 12-AGO, dos consecuencias sobre este script:
  - El formulario del ensayo se pidio SOLO por correo el 06-Ago y no se contesto
    (PRG-24 abierto). Por eso la OBS-01 se plantea como CONFIRMACION OPERATIVA
    antes del 13-Ago, con el cierre documental en la proxima emision, y no como
    defecto que espera una revision.
  - La observacion de las ERRATAS se elimino. ADASA pidio "the applicable
    edition and addenda"; addenda no existen y las erratas nunca se pidieron:
    era hallazgo propio, no peticion incumplida.

TRAZA INTERNA - NO SE EMITE. El documento vuelve SIN CODIGO de respuesta y un
documento sin codigo no se anota: su punto abierto va integro en el texto de su
subseccion del transmittal.

Las tres regresiones que la Rev D introdujo -clausula 5.6.5, formulario
AQ-QAM-F018 y factor 1.5 x design pressure- NO se anotan: esa revision la
codifico 2 el TM N29 sin detectarlas, y reclamarlas ahora reabriria una
aprobacion propia. La peticion se limita a identificar el formulario, que si
estaba en el universo del correo del 06-Ago.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-010_0_HP_LP_Pressure_Test_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-010_0_HP_LP_Pressure_Test_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-010_0_ HP and LP Pressure Test Procedure.pdf",
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
        "search": "recorded in the Pressure Test Report",
        "page_fallback": 9,
        "text": (
            "OBS-01: the Pressure Test Report named here is\n"
            "not part of this submittal and no controlled\n"
            "form in this procedure produces it. Row 5.2 of\n"
            "the Inspection and Test Plan\n"
            "(P22-BA-09-000-004 Rev 0) requires a Pressure\n"
            "Test report with a pressure against time\n"
            "graphic as the certificate of a Hold Point, and\n"
            "the high-pressure test is on 13 and 14 August.\n"
            "As written the test cannot be certified.\n"
            "Confirm before 13 August: the form by number\n"
            "and revision, made available to the inspector\n"
            "for that attendance.\n"
            "Correct at the next issue: attach that form to\n"
            "this procedure, so that it produces the\n"
            "graphic record."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "the ASME B31.3 2024 edition . For the schematic",
        "page_fallback": 6,
        "text": (
            "NOTE-01: clauses 5.5.2 and 5.6.3 now test to a\n"
            "fixed edition instead of to the latest one,\n"
            "which was the point raised on 6 August. That\n"
            "point is closed."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
