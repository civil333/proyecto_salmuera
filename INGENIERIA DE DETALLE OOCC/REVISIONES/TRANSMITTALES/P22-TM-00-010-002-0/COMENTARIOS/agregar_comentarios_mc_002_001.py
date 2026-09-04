# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-001_0 (Estanque TK-06-001) Rev 0 - TM N2 OOCC.
Solo items ABIERTOS/NUEVOS: OBS-01, NOTA-03, NOTA-10.
(NPT retirado: dato fijo del montaje, su plano ya lo refleja.)
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-001_0.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-MC-00-002-001_0_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-MC-00-002-001_0.pdf"
    shutil.copy2(src, PDF_LOCAL)

COMENTARIOS = [
    {"id":"OBS-01","fill":MAYOR,"search":None,"page_fallback":24,
     "text":("OBS-01: Anclaje del estanque.\n"
             "Sigue postinstalado adhesivo (HAS-V-36,\n"
             "HIT-RE 500), no redisenado a preinstalado\n"
             "colado; ya observado en el Transmittal N1.\n"
             "Ademas la losa se densifico a Phi16@100.\n"
             "Corregir: redisenar perno preinstalado\n"
             "colado en sitio (ASTM F1554) por ACI\n"
             "318-19 Cap.17 + Sec.17.10; reconciliar con\n"
             "plano Exfibro EX-26005-F01 Rev C.")},
    {"id":"NOTA-03","fill":MENOR,"search":None,"page_fallback":13,
     "text":("NOTA-03: Origen de reacciones.\n"
             "Adopta las reacciones corregidas por\n"
             "ADASA pero cita fuente Memoria AFTA.\n"
             "Corregir: citar P22-IT-06-000-005-0.")},
    {"id":"NOTA-10","fill":MENOR,"search":None,"page_fallback":24,
     "text":("NOTA-10: Designaciones erroneas.\n"
             "Dice ASTM F1553 (debe ser F1554) y\n"
             "HIR-RE 500 (debe ser HIT-RE 500).\n"
             "Corregir: rectificar designaciones y\n"
             "justificar el cambio de armadura de losa.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
