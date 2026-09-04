# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-002_B LAM4.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-00-002-002_B LAM4_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/03 Planos/PDF/P22-DWG-00-002-002_B LAM4.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-01: Tratamiento de suelo no indicado.\n"
             "Indicar las condiciones de mejoramiento / tratamiento del suelo.\n"
             "Corregir: agregar nota con las condiciones de mejoramiento del suelo.\n"
             "Requisito: ET-101.")},
    {"id":"OBS-02","fill":MAYOR,"search":None,"page_fallback":0,
     "text":("OBS-02: Anclaje de bomba BH-06-001 postinstalado adhesivo.\n"
             "El anclaje de la bomba BH-06-001 figura como postinstalado con adhesivo.\n"
             "Corregir: evaluar anclaje preinstalado o justificar el postinstalado adhesivo "
             "segun la categoria sismica.\n"
             "Requisito: ACI 318-19 Cap.17, categoria sismica del proyecto.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
