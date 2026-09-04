# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-005_0 (Sistema CIP) Rev 0 - TM N2 OOCC. Codigo 2.
Solo items ABIERTOS/NUEVOS: NOTA-01 (recubrimientos), anclaje CIP diferido.
(NPT retirado: dato fijo del montaje, su plano ya lo refleja. Anclaje CIP =
dependencia aceptada por falta de datos del proveedor, como en el Transmittal N1.)
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-005_0.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-MC-00-002-005_0_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-MC-00-002-005_0.pdf"
    shutil.copy2(src, PDF_LOCAL)

COMENTARIOS = [
    {"id":"NOTA-01","fill":MENOR,"search":None,"page_fallback":5,
     "text":("NOTA-01: Recubrimientos no declarados.\n"
             "Corregir: declarar 50 mm expuesto /\n"
             "70 mm en contacto con terreno.")},
    {"id":"NOTA-02","fill":MENOR,"search":None,"page_fallback":33,
     "text":("NOTA-02: Anclajes CIP diferidos.\n"
             "Por falta de datos del proveedor; en\n"
             "seguimiento, no rechazo (como en el\n"
             "Transmittal N1).\n"
             "Corregir: completar con anclajes\n"
             "postinstalados (ACI 318-19 Cap.17/Sec.\n"
             "17.10, precalificados ACI 355.2/355.4)\n"
             "cuando lleguen los datos del proveedor.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
