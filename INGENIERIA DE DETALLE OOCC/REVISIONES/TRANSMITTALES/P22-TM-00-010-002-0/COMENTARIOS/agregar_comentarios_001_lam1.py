# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-001_B LAM1.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-001_B LAM1_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-001_B LAM1.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"NOTA-01","fill":MENOR,"search":None,"page_fallback":0,
     "text":("NOTA-01: Orientacion del estanque sin fijar.\n"
             "Se requieren un par de coordenadas mas para fijar la orientacion del estanque.\n"
             "Corregir: agregar coordenadas adicionales que definan el azimut del estanque.")},
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: NPT por zona no acotado en el layout.\n"
             "El nivel de piso terminado por zona no esta acotado en la planta general.\n"
             "Corregir: declarar N.T.N. coincidente con planos de montaje "
             "P22-DWG-06-005-101 / -103 / -105 y el Levantamiento DIO.\n"
             "Requisito: coherencia de cotas con planos de montaje.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
