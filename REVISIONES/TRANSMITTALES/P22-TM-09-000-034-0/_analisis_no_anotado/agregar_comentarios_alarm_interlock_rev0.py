#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anota la Alarm and Interlock List Rev 0 (P22-LI-09-008-015), submittal
25007-0073 (E73). Veredicto del TM N34: Code 3 - To be revised.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de la subseccion 2.1.

ALCANCE. Rev 0 que viene de un Code 2: revision binaria contra las cuatro
condiciones del TM N28, sin comentarios nuevos. Cierran OBS-02 (tag del
interruptor a P22-PLC01-XA001), NOTE-01 (a) (VIT -> VT-09-001) y las cuatro
partes de NOTE-02. Quedan los dos puntos de abajo.

Reparto por pagina (indices 0-based):
    0-1  caratula y encabezado de tabla
    2    fila 6.0 VT-09-001 con rango 0,0-12,0 mm/s  -> OBS-02
    7    filas 42.0 y 43.0 con los TAG sin guion      -> OBS-01
    8-9  Consolidated Comment Sheet
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-015_0_Alarm_Interlock_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-015_0_Alarm_Interlock_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 73",
        "P22-LI-09-008-015_Alarm & Interlock List_0.pdf"))
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
        "search": "VE09-014-XT001",
        "page_fallback": 7,
        "text": (
            "OBS-01: the four fault alarms added to close the\n"
            "Transmittal N28 note are here, but two carry a\n"
            "malformed tag: VE09-014-XT001 and VE09-016-XT001,\n"
            "without the hyphen that the thirteen other valve\n"
            "rows of this list and the IO List Rev 5 both use\n"
            "(VE-09-012, VE-09-013, BDS-09-001). As written\n"
            "they do not resolve against the IO List, which is\n"
            "the failure mode the breaker alarm item raised.\n"
            "Correct: write them as VE-09-014-XT001 and\n"
            "VE-09-016-XT001."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "RO HP Pump Vibration Transmitter",
        "page_fallback": 2,
        "text": (
            "OBS-02: Transmittal N28 offered two routes for the\n"
            "vibration trip. This list takes the second one:\n"
            "item 6.0 now ranges VT-09-001 at 0.0 to 12.0 mm/s\n"
            "and item 6.1 keeps the high-high trip at 10.0, so\n"
            "the trip fits. But that route required re-ranging\n"
            "the transmitter IN THE INSTRUMENT LIST, and the\n"
            "Instrument List (P22-LI-09-008-003) Rev E, approved\n"
            "at Code 1, still ranges VT-09-001 at 0.0 to 8.9\n"
            "mm/s rms on the Wilcoxon PCH420V-M12. Until it is\n"
            "re-issued the approved instrument saturates below\n"
            "the trip and 'Stop HP Pump' cannot fire.\n"
            "Correct: re-issue the Instrument List with\n"
            "VT-09-001 ranged 0 to 12 mm/s rms."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
