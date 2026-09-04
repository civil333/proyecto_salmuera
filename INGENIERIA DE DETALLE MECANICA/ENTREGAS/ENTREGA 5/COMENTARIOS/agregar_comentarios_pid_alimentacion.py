"""
Anotaciones ADASA sobre P22-DWG-06-009-102-C
P&ID Alimentacion Modulo 2da Etapa Salmuera — Rev C

Hallazgos detectados en revision interna ADASA (14-Abr-2026):
  HAL-10 (MAYOR): Volumen Fosa TK-06-002 = 850 L en P&ID vs 2,000 L en Equipment List
  HAL-11 (MAYOR): ORPIT-06-001A en P&ID — debe ser ORPIT-09-001A (area 09, suministro BW Water)
"""

import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

skill_path = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)

from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-06-009-102-C (P&ID ALIMENTACION MODULO Sda.ETAPA SALMUERA)-02.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR,
    "P22-DWG-06-009-102-C (P&ID ALIMENTACION MODULO Sda.ETAPA SALMUERA)-02_CC_ADASA.pdf")

# Copiar PDF fuente si no existe localmente
if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(SCRIPT_DIR, "..",
        "P22-DWG-06-009-102-C (P&ID ALIMENTACIÓN MÓDULO Sda.ETAPA SALMUERA)-02.pdf"))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
    else:
        print(f"ERROR: No se encontro PDF fuente en {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "850",
        "page_fallback": 0,
        "text": (
            "Volumen TK-06-002 indicado como 850 L.\n"
            "Equipment List Rev B indica 2,000 L.\n"
            "Corregir volumen en P&ID."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "ORPIT",
        "page_fallback": 0,
        "text": (
            "TAG indica ORPIT-06-001A (area 06).\n"
            "Corregir a ORPIT-09-001A (area 09).\n"
            "Instrumento suministro BW Water."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "VM-06-001",
        "page_fallback": 0,
        "text": (
            "Incluir valvula adicional para\n"
            "dejar aislado el sistema."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": "SA-HDPE-DN110-PN10-002",
        "page_fallback": 0,
        "text": (
            "TAG de linea duplicado.\n"
            "Mismo TAG en P&ID 105 con\n"
            "destino distinto (Fosa Drenajes).\n"
            "Renumerar una de las lineas."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
