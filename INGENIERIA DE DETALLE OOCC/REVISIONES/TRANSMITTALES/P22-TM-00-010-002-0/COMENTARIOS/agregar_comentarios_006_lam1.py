# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-006_B LAM1.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-006_B LAM1_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-006_B LAM1.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: Nomenclatura de camaras no normalizada.\n"
             "Las camaras figuran como 'Camara N1..N7'.\n"
             "Corregir: adoptar la nomenclatura CD-06-00N para las camaras.")},
    {"id":"NOTA-01","fill":MENOR,"search":None,"page_fallback":0,
     "text":("NOTA-01: Falta detalle tipico de camara y pendientes.\n"
             "Falta la lamina de detalle tipico de camara prefabricada y acotar las "
             "pendientes longitudinales.\n"
             "Corregir: incorporar detalle tipico de camara prefabricada y acotar pendientes "
             "longitudinales.\n"
             "Requisito: TR Seccion 6.2.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
