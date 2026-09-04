# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-003-001_0 (Cubierta) Rev 0 - TM N2 OOCC.
Solo items ABIERTOS/NUEVOS: OBS-02, OBS-05.
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-003-001_0.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-MC-00-003-001_0_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-MC-00-003-001_0.pdf"
    shutil.copy2(src, PDF_LOCAL)

COMENTARIOS = [
    {"id":"OBS-02","fill":MAYOR,"search":None,"page_fallback":4,
     "text":("OBS-02: Proteccion C5-M no declarada.\n"
             "Corregir: declarar C5-M o referir a la ET\n"
             "P22-ET-00-010-103-0 (ISO 12944).")},
    {"id":"OBS-05","fill":MENOR,"search":None,"page_fallback":21,
     "text":("OBS-05: Anexos en Rev B e inconsistencias.\n"
             "Coeficiente sismico vertical 0,74 (tabla)\n"
             "vs 0,67 (texto); factor 1,4E no declarado\n"
             "en combinaciones.\n"
             "Corregir: reemitir anexos a Rev 0,\n"
             "unificar el coeficiente y declarar la\n"
             "combinacion usada.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
