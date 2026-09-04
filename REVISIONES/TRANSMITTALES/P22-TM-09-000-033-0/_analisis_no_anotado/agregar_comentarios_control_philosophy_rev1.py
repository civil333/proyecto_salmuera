#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_control_philosophy_rev1.py
Anota el Control Philosophy Rev 1 (P22-BT-09-009-001), submittal 25007-0079
(E79). Veredicto del TM N33: Code 2 - Approved as noted.

len(COMENTARIOS) = 5 (OBS-01 a OBS-04 + NOTE-01), espejo 1:1 del bloque Action.

ALCANCE: SOLO los cuatro puntos que el TM N31 dejo abiertos. El TM N31 devolvio
la Rev 0 sin codigo, por estar emitida para construccion, y enumero cuatro
puntos "for closure at the next issue". No se hace lectura fresca de las 59
paginas: abrir frentes nuevos sobre una revision que responde a un alcance
acotado es exigir de mas.

ESTADO DE LOS CUATRO PUNTOS, verificado contra la fuente aprobada:
  1. Mapeo de sensores: CIERRA en la seccion de la bomba CIP y NO cierra en la
     de la bomba de alta -> OBS-01.
  2. Pares de vibracion: CIERRA. 7,0 y 10 mm/s en la bomba de alta y 4,5 y 6,0
     en los dos turbochargers coinciden exactamente con la Alarm and Interlock
     List Rev C. Solo queda el calificativo -> NOTE-01.
  3. Clase de aislacion: CIERRA. Clase F coincide con el datasheet vigente
     P22-ET-09-009-002 Rev D. NO se anota.
  4. Documentos hijos: PARCIAL, falta la revision -> OBS-02, OBS-03, OBS-04.

OBS-01 ES RECTIFICACION DE ADASA, NO INCUMPLIMIENTO DEL PROVEEDOR. El TM N31
declaro correcta la pagina de la bomba de alta. BW Water hizo exactamente lo que
se le pidio. El texto se redacta sin verbo de incumplimiento.

Documento de texto: los anclajes van por 'search', no por indice de pagina.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BT-09-009-001_1_Control_Philosophy.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BT-09-009-001_1_Control_Philosophy_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 79",
        "P22-BT-09-009-001_Control Narrative_r1.pdf",
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
        "search": "TE-09-001/003",
        "page_fallback": 38,
        "text": (
            "OBS-01: ADASA rectifies its own reading. Point 1\n"
            "of Transmittal N31 accepted this page as correct;\n"
            "it is not. The Instrument List P22-LI-09-008-003\n"
            "Rev E assigns two sensors per machine and states\n"
            "the supplier of each: TE-09-001 winding and\n"
            "TE-09-002 bearing on the HP pump, both Fedco;\n"
            "TE-09-003 winding and TE-09-004 bearing on the\n"
            "CIP pump, both Grundfos. The comment sheet of the\n"
            "Alarm and Interlock List P22-LI-09-008-015 Rev C\n"
            "records the same four assignments. These tables\n"
            "claim TE-09-003 and TE-09-004, the two CIP pump\n"
            "sensors, as if the HP pump had four; the winding\n"
            "trip is 140 C and the bearing trip 95 C, so a\n"
            "crossed tag acts on the wrong element.\n"
            "Correct: read TE-09-001 winding and TE-09-002\n"
            "bearing here and on the bearing table of the\n"
            "previous page. The CIP pump section, corrected at\n"
            "this revision, is right and stays as it is."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "P22-LI-09-008-017",
        "page_fallback": 7,
        "text": (
            "OBS-02: the reference table now pins the two child\n"
            "documents by code, which is half of what\n"
            "Transmittal N31 asked: it asked for code AND\n"
            "revision. Both are issued, as P22-LI-09-008-017\n"
            "Rev A and P22-LI-09-008-015 Rev C.\n"
            "Correct: add the revision to both rows."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Detailed setpoints are stated",
        "page_fallback": 41,
        "text": (
            "OBS-03: three paragraphs of the body still refer\n"
            "to \"a separate document (alarm and setpoint\n"
            "list)\" without code or revision, on the\n"
            "protection blocks of the HP pump, the feed\n"
            "turbocharger and the CIP system.\n"
            "Correct: pin each of the three by code and\n"
            "revision, as the reference table does."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "P22-DWG-09-009-0001",
        "page_fallback": 7,
        "text": (
            "OBS-04: two codes of this table carry a four digit\n"
            "sequential that the project numbering does not\n"
            "use, which is three digits: P22-DWG-09-009-0001\n"
            "for the Process Flow Diagram and\n"
            "P22-CD-09-004-0001 for the Control System\n"
            "Architecture.\n"
            "Correct: state both with the sequential of the\n"
            "project numbering system."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "subject to vendor confirmation",
        "page_fallback": 41,
        "text": (
            "NOTE-01: the six vibration setpoints of this\n"
            "revision match the Alarm and Interlock List Rev C\n"
            "exactly, on all three machines, which closes the\n"
            "point raised at Transmittal N31. The three blocks\n"
            "still carry the qualifier \"subject to vendor\n"
            "confirmation\", and those values are fixed by a\n"
            "document approved at Code 1.\n"
            "Correct: remove the qualifier at the next issue."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
