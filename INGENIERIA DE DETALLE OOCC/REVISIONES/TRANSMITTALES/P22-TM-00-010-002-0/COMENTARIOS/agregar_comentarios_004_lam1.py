# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-004_B LAM1.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-004_B LAM1_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-004_B LAM1.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: Mejoramiento de suelo e impermeabilizacion no indicados.\n"
             "Indicar condiciones de mejoramiento de suelo e impermeabilizacion de los "
             "elementos enterrados.\n"
             "Corregir: agregar notas de mejoramiento de suelo e impermeabilizacion.")},
    {"id":"NOTA-01","fill":MENOR,"search":None,"page_fallback":0,
     "text":("NOTA-01: TAG de la fosa incorrecto.\n"
             "El tag de la fosa debe ser TK-06-004 (no TK-06-002, que es el estanque CIP de "
             "BW Water).\n"
             "Corregir: actualizar el tag de la fosa de drenajes a TK-06-004.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
