# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-004_B LAM2.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-004_B LAM2_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-004_B LAM2.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: Material de la parrilla.\n"
             "Dejar la parrilla en pultruida de PRFV, solo para transito liviano de personas.\n"
             "Corregir: especificar parrilla pultruida de PRFV para transito liviano.")},
    {"id":"OBS-02","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-02: Aperturas de rebalse no indicadas.\n"
             "Indicar las aperturas para el rebalse del estanque.\n"
             "Corregir: agregar y acotar las aperturas de rebalse del estanque.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
