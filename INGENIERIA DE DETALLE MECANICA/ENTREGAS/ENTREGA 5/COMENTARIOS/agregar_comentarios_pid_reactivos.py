"""
Anotaciones ADASA sobre P22-DWG-06-009-105-B
P&ID Reactivos Modulo 2da Etapa Salmuera — Rev B

Observacion:
  TAG SA-HDPE-DN110-PN10-002 duplicado (mismo TAG en P&ID 102 con destino TK-06-001)
"""

import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

skill_path = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)

from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-06-009-105-B (P&ID REACTIVOS MODULO 2da ETAPA SALMUERA)-06.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR,
    "P22-DWG-06-009-105-B (P&ID REACTIVOS MODULO 2da ETAPA SALMUERA)-06_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..",
        "P22-DWG-06-009-105-B (P&ID REACTIVOS MÓDULO 2da ETAPA SALMUERA)-06.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
    else:
        print(f"ERROR: No se encontro PDF fuente en {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "SA-HDPE-DN110-PN10-002",
        "page_fallback": 0,
        "text": (
            "TAG de linea duplicado.\n"
            "Mismo TAG en P&ID 102 con\n"
            "destino distinto (TK-06-001).\n"
            "Renumerar una de las lineas."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
