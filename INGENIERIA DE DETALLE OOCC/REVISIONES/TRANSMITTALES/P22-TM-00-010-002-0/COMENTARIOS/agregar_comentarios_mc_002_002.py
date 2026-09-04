# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-002_0 (Fundacion Bomba) Rev 0 - TM N2 OOCC. Codigo 2.
Solo items ABIERTOS/NUEVOS: NOTA-02 (recubrimientos).
(NPT retirado: dato fijo del montaje, su plano ya lo refleja.)
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-002_0.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-MC-00-002-002_0_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-MC-00-002-002_0.pdf"
    shutil.copy2(src, PDF_LOCAL)

COMENTARIOS = [
    {"id":"NOTA-02","fill":MENOR,"search":None,"page_fallback":5,
     "text":("NOTA-02: Recubrimientos no declarados.\n"
             "Corregir: declarar 50 mm expuesto /\n"
             "70 mm en contacto con terreno.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
