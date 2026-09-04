# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-004_0 (Contenedor RO) Rev 0 - TM N2 OOCC. Codigo 2.
Solo items ABIERTOS/NUEVOS: NOTA-04 (peso conservador aceptado), OBS-02 (ACI).
(NPT retirado: dato fijo del montaje, su plano ya lo refleja.)
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-004_0.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-MC-00-002-004_0_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-MC-00-002-004_0.pdf"
    shutil.copy2(src, PDF_LOCAL)

COMENTARIOS = [
    {"id":"NOTA-04","fill":MENOR,"search":None,"page_fallback":13,
     "text":("NOTA-04: Peso del contenedor.\n"
             "Adopta ~17,3 t (escrito 'tonf'), conservador\n"
             "frente al vinculante 14.934 kg del Transmittal\n"
             "N1; ADASA lo acepta como conservador.\n"
             "Corregir: rectificar la unidad/notacion y\n"
             "citar la fuente; si se mantiene 17,3 t,\n"
             "declararlo como adopcion conservadora.")},
    {"id":"OBS-02","fill":MENOR,"search":None,"page_fallback":23,
     "text":("OBS-02: Version ACI inconsistente.\n"
             "El diseno de pedestales cita ACI 318-10\n"
             "mientras el listado cita 318-19.\n"
             "Corregir: unificar a ACI 318-19.")},
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
