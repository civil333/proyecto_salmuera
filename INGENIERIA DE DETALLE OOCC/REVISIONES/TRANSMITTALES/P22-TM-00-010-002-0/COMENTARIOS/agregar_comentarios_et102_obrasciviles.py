# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-00-010-102-0_B.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-ET-00-010-102-0_B_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-ET-00-010-102-0_B.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-07","fill":MAYOR,"search":None,"page_fallback":7,
     "text":("OBS-07: Recubrimiento e impermeabilizacion incompletos.\n"
             "El TdR (Seccion 3.3.4) exige 50 mm en elementos expuestos y 70 mm en "
             "elementos en contacto con el terreno; la ET declara solo 70 mm y no "
             "especifica la impermeabilizacion de elementos enterrados.\n"
             "Corregir: declarar 50 mm expuesto / 70 mm en contacto con terreno "
             "y el sistema de impermeabilizacion de elementos enterrados.\n"
             "Requisito: TdR Seccion 3.3.4; durabilidad del hormigon en ambiente marino.")},
    {"id":"NOTA-11","fill":MENOR,"search":None,"page_fallback":2,
     "text":("NOTA-11: Emplazamiento y referencias del documento.\n"
             "Declara emplazamiento en Antofagasta e invoca un estudio de suelos inexistente; "
             "el codigo de portada es tipo IT.\n"
             "Corregir: particularizar a Taltal (ambiente marino) y corregir el codigo a ET.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
