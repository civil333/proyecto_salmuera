#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anota el GA of Antiscalant Dosing Pump Skid Rev C (P22-DWG-09-005-011),
submittal 25007-0080 (E80). Veredicto del TM N34: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.4.

ALCANCE. Solo cierre de los puntos del TM N26. La OBS-01 pedia dos cosas:
rotular cada bloque como valor por perno o total del grupo, y conciliar el Fz
por perno. La primera cierra. La segunda no, por segunda vez consecutiva.

Aritmetica verificada por render a 300 dpi de la lamina, con 10 pernos (nota 7.2):
    total  Fx 1,0242 kN / 10 = 0,10242  vs por perno 0,102  -> concilia
    total  Fy 1,4632 kN / 10 = 0,14632  vs por perno 0,146  -> concilia
    total  Fz 1,0242 kN / 10 = 0,10242  vs por perno 0,205  -> factor 2,00

La NOTE-01 del TM N26 (informe de calculo endosado) es entregable de otro
documento y se sigue en la Seccion 3 del transmittal; no se anota aca.

Pagina 2 con rotacion 270: la skill dibuja en el content stream, de modo que
page.annots() devuelve 0 aunque el cuadro es visible. Cierre por render PNG.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-011_C_GA_Antiscalant_Pump_Skid.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-011_C_GA_Antiscalant_Pump_Skid_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 80", "25007-0080-1",
        "P22-DWG-09-005-011_C GA of Antiscalant Dosing Pump Skid.pdf"))
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
        "search": "WASHER",
        "page_fallback": 1,
        "text": (
            "OBS-01: the labelling half of the Transmittal N26\n"
            "item closes - each block is now identified as a\n"
            "total or as a per-bolt value. The reconciliation\n"
            "half does not, for the second consecutive issue,\n"
            "against a comment sheet that reports the reaction\n"
            "forces as updated.\n"
            "With the 10 bolts of note 7.2: Fx 1.0242/10 =\n"
            "0.102 and Fy 1.4632/10 = 0.146 both match the\n"
            "per-bolt block, but Fz 1.0242/10 = 0.102 against\n"
            "a per-bolt 0.205 - twice the quotient, where at\n"
            "Rev B the same pair differed by a factor of ten.\n"
            "Correct: state which of the two Fz figures governs\n"
            "and reconcile the per-bolt value with the total\n"
            "over the ten bolts, keeping each axis explicit."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
