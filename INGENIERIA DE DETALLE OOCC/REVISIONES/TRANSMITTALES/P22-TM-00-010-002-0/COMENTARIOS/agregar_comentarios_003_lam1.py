# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-003_B LAM1.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-003_B LAM1_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-003_B LAM1.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: Elevaciones no corresponden.\n"
             "El plano usa datum relativo (~0,00); estas elevaciones no corresponden.\n"
             "Corregir: expresar en N.T.N. absoluto de la zona contenedor coincidente con el "
             "plano de montaje P22-DWG-06-005-103.\n"
             "Requisito: coherencia de cotas con plano de montaje.")},
    {"id":"OBS-02","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-02: Inserto INS-1 sin referencia de plano.\n"
             "Indicar en que plano esta el inserto INS-1; el detalle esta en LAM2.\n"
             "Corregir: agregar el callout que remite al detalle de INS-1 en LAM2.")},
    {"id":"NOTA-01","fill":MENOR,"search":None,"page_fallback":0,
     "text":("NOTA-01: Mejoramiento de suelo no indicado.\n"
             "Indicar condiciones de mejoramiento del suelo.\n"
             "Corregir: agregar nota con las condiciones de mejoramiento del suelo.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
