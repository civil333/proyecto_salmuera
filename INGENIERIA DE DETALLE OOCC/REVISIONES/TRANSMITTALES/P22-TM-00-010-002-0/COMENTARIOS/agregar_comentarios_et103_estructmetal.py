# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-00-010-103-0_B.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-ET-00-010-103-0_B_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-ET-00-010-103-0_B.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-08","fill":MAYOR,"search":None,"page_fallback":10,
     "text":("OBS-08: Sistema anticorrosivo y codigo de soldadura incompletos.\n"
             "Declara C5-M (ISO 12944) pero sin el esquema por capas: preparacion SSPC-SP10/Sa 2 1/2, "
             "zinc 80 um + epoxico 200 um + poliuretano 75 um; cita AWS A5.1/A5.17 (electrodos) "
             "en vez del codigo estructural AWS D1.1.\n"
             "Corregir: completar el esquema por capas y la preparacion de superficie, citar AWS D1.1 "
             "y exigir perneria galvanizada en caliente o inoxidable.\n"
             "Requisito: proteccion C5-M verificable en ambiente marino.")},
    {"id":"NOTA-11","fill":MENOR,"search":None,"page_fallback":2,
     "text":("NOTA-11: Emplazamiento y codigo del documento.\n"
             "Declara emplazamiento en Antofagasta; el codigo de portada es tipo IT.\n"
             "Corregir: particularizar a Taltal (ambiente marino) y corregir el codigo a ET.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
