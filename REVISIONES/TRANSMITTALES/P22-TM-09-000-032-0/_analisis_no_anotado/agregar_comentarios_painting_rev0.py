#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_painting_rev0.py
Anota el Painting Procedure Rev 0 (P22-BA-09-000-011) del submittal 25007-0075.
Veredicto del TM N32: Code 3 - To be revised.

len(COMENTARIOS) = 3: la OBS-01 del color, que es lo unico vinculante, y dos NOTE.

ALCANCE: unica peticion del correo del 06-Ago sobre este documento - completar
el formulario de inspeccion con el color de terminacion y el producto por capa.
El producto por capa quedo correcto; el color quedo en RAL 5010 Gentian Blue
contra el RAL 5012 Luminous Blue del cuerpo (pagina 9) y de la Painting
Specification P22-ET-09-006-002 Rev C aprobada en Codigo 1 (item 4, frame
support inside the container, acero al carbono ASTM A-36). RAL 5010 no aparece
en ninguna fila de esa especificacion.

La inspeccion de preparacion de pintura es el 13 y 14 de agosto, y el tercero
inspector tiene una copia de este procedimiento: por eso la NOTE-01 pide
declarar cual revision gobierna.

Nota del triaje del 12-Ago: la OBS-02 de este script (espesor nominal por capa)
YA NO SE EXIGE. BW Water contesto que el formulario adjunto es una muestra y que
los valores reales se llenan en el informe del dia; la peticion de ADASA no
distinguia criterio de aceptacion de registro. El transmittal lo replantea una
vez con esa distincion, sin exigirlo. Lo unico vinculante es el color.

TRAZA INTERNA - NO SE EMITE. Por decision del usuario del 12-Ago este documento
vuelve SIN CODIGO de respuesta, y un documento sin codigo no se anota: sus puntos
abiertos van integros en el texto de su subseccion del transmittal. El PDF que
este script genera queda como respaldo del analisis y NO se adjunta ni se sube al
enlace de descarga.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-011_0_Painting_Procedure.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-011_0_Painting_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-011_0_ Painting Procedure.pdf",
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
        "search": "RAL 5010 Gentian Blue",
        "page_fallback": 10,
        "text": (
            "OBS-01: binding. The Colour row of the\n"
            "inspection form was completed with RAL 5010\n"
            "Gentian Blue. Page\n"
            "9 of this same procedure specifies RAL 5012\n"
            "Luminous Blue for the third coat, and the\n"
            "Painting Specification (P22-ET-09-006-002)\n"
            "Rev C sets RAL 5012 Luminous Blue for the\n"
            "frame support inside the container. RAL 5010\n"
            "appears in no row of that specification.\n"
            "Correct: state RAL 5012 Luminous Blue for the\n"
            "third coat on this form.\n"
            "Acknowledged: the product for each coat is\n"
            "correct and matches the body."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "355 µm Min",
        "page_fallback": 10,
        "text": (
            "NOTE-01: on the thickness per coat, ADASA\n"
            "notes the reply that this form is a sample and\n"
            "that actual values are entered in the actual\n"
            "report, and restates the request in those\n"
            "terms.\n"
            "What belongs printed on the blank form is the\n"
            "SPECIFIED thickness of each coat - 80, 200 and\n"
            "75 micrometres - as the criterion against which\n"
            "the measured values are compared. The measured\n"
            "values remain to be filled in at the time of\n"
            "inspection.\n"
            "Not a condition of this transmittal."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "RAL5012 LUMINOUS BLUE",
        "page_fallback": 8,
        "text": (
            "NOTE-02: two physically different documents\n"
            "are now identified as Rev 0 of this procedure,\n"
            "dated 05-08-2026 and 11-08-2026, and the\n"
            "third-party inspection package holds an\n"
            "earlier copy.\n"
            "Confirm: which revision governs the painting\n"
            "preparation inspection of 13 and 14 August."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
