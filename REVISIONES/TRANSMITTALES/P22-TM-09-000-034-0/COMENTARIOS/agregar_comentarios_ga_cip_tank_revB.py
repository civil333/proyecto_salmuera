#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anota el GA of CIP / Flushing Tank Rev B (P22-DWG-09-005-014), submittal
25007-0080 (E80). Veredicto del TM N34: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.5.

ALCANCE. Solo cierre de los puntos del TM N26.
  OBS-01 (TAG TK-09-001) -> CERRADA: la Rev A no lo traia en ninguna parte de la
         lamina y la Rev B lo incorpora. No se anota.
  OBS-02 (tabla de boquillas) -> NO CERRADA: las tres entradas en disputa son
         identicas a las de la Rev A y ningun documento fue reemitido -> OBS-01.
  NOTE-01 y NOTE-02 del TM N26 no exigian accion sobre el plano (entregable
         cruzado y verificacion positiva). No se anotan y su ausencia de la hoja
         consolidada NO es hallazgo.
RETIRADO. La caratula declara dos paginas y el archivo trae tres. Se habia
anotado como NOTE-01 y SALE: es una observacion NUEVA, ajena al universo de los
cuatro puntos del TM N26, sobre un documento que se revisa unicamente por cierre
de comentarios; y ademas es housekeeping documental, que no degrada. Queda en
_ANALISIS_N34.md, Seccion 9.

Pagina 2 con rotacion 270: cierre por render PNG.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-014_B_GA_CIP_Flushing_Tank.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-014_B_GA_CIP_Flushing_Tank_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 80", "25007-0080-1",
        "P22-DWG-09-005-014_B GA of CIP Flushing Tank.pdf"))
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
        "search": "DESIGNATION",
        "page_fallback": 1,
        "text": (
            "OBS-01: the comment sheet reports the nozzle\n"
            "schedule as reconciled with the datasheet. The\n"
            "three entries in dispute at Transmittal N26 are\n"
            "unchanged from Rev A, and neither document was\n"
            "re-issued: the top opening reads MH Manhole 533 mm\n"
            "internal diameter where the approved Datasheet of\n"
            "the CIP Tank (P22-ET-09-009-009) Rev B lists HH\n"
            "Handhole DN300, and N42 Spare and N97 Temperature\n"
            "Sensor have no counterpart in that schedule. The\n"
            "twelve remaining nozzles agree. The datasheet is\n"
            "not self-consistent either: its tank construction\n"
            "description calls for a welded conical cover with\n"
            "a manhole cover.\n"
            "Correct: state in writing which document governs\n"
            "these three entries, and align the other one."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
