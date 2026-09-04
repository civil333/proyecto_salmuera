# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-003-001_B (Cubierta Metálica Sistema CIP). Código 3.
Comentarios ejecutivos (Defecto / Corregir / Requisito), ≤ ~8 líneas.
6 comentarios: OBS-01/02/03 + NOTA-01/02/09. IDs y page_fallback fijos.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-003-001_B.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-MC-00-003-001_B_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "P22-TR-00-010-01-0", "ENTREGAS", "ENTREGA 3",
        "P22-MC-00-003-001_B.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado.")
    else:
        print(f"ERROR: PDF fuente no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR, "search": None,
        "page_fallback": 5,  # parametros para analisis sismico (TOC p.6)
        "text": (
            "OBS-01: Clasificacion de suelo.\n"
            "Adopta suelo tipo D y Cv 0,74; las 4\n"
            "memorias de fundaciones adoptan tipo E y\n"
            "Cv 0,45 para el mismo emplazamiento.\n"
            "Corregir: reconciliar la clasificacion del\n"
            "sitio (unica, conforme al informe sismico)\n"
            "y re-verificar la demanda sismica de la\n"
            "cubierta.\n"
            "Requisito: informe sismico; NCh 2369:2025."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR, "search": None,
        "page_fallback": 4,  # materiales (TOC p.5)
        "text": (
            "OBS-02: Proteccion superficial.\n"
            "No aborda el sistema C5-M (ISO 12944)\n"
            "exigido para estructura metalica en\n"
            "ambiente marino.\n"
            "Corregir: declarar el sistema C5-M o\n"
            "referir a la ET de Estructura Metalica\n"
            "P22-ET-00-010-103-0.\n"
            "Requisito: TR (C5-M, ISO 12944)."
        ),
    },
    {
        "id": "OBS-03", "fill": MENOR, "search": None,
        "page_fallback": 3,  # normativa (TOC p.4)
        "text": (
            "OBS-03: Version de NCh 427/1.\n"
            "Normativa cita NCh 427/1 2006; el analisis\n"
            "cita NCh 427/1 2016 (AISC 360-2016).\n"
            "Corregir: unificar la version\n"
            "efectivamente aplicada.\n"
            "Requisito: TR (normativa estructural)."
        ),
    },
    {
        "id": "NOTA-01", "fill": MAYOR, "search": None,
        "page_fallback": 4,  # codigos y manuales (TOC p.5)
        "text": (
            "NOTA-01: Version de ACI 318.\n"
            "Verificacion con ACI 318-14; el TR exige\n"
            "ACI 318-19.\n"
            "Corregir: demostrar equivalencia o\n"
            "re-verificar las fundaciones con ACI\n"
            "318-19.\n"
            "Requisito: TR (ACI 318-19)."
        ),
    },
    {
        "id": "NOTA-02", "fill": MENOR, "search": None,
        "page_fallback": 30,  # diseno de fundaciones (TOC p.31)
        "text": (
            "NOTA-02: Recubrimientos.\n"
            "No se declaran los recubrimientos minimos\n"
            "de zapata/pedestal.\n"
            "Corregir: declarar 50 mm expuesto / 70 mm\n"
            "en contacto con terreno.\n"
            "Requisito: TR (ambiente marino)."
        ),
    },
    {
        "id": "NOTA-09", "fill": MENOR, "search": None,
        "page_fallback": 23,  # factores de utilizacion (TOC p.24)
        "text": (
            "NOTA-09: Conformidad estructural.\n"
            "Resistencia (FU max 57,5%), deformaciones\n"
            "y estabilidad de fundaciones conformes;\n"
            "las observaciones se acotan a suelo,\n"
            "proteccion y consistencia normativa."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
