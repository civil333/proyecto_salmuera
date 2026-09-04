# -*- coding: utf-8 -*-
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios
PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-00-010-101-0_B.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-ET-00-010-101-0_B_CC_ADASA.pdf")
if not os.path.exists(PDF_LOCAL):
    src = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4/02 Documentos/PDF/P22-ET-00-010-101-0_B.pdf"
    shutil.copy2(src, PDF_LOCAL)
COMENTARIOS = [
    {"id":"OBS-07","fill":MAYOR,"search":None,"page_fallback":9,
     "text":("OBS-07: Mejoramiento de suelo diferido a obra, no especificado como condicion.\n"
             "El relleno estructural remite a un Informe de Mecanica de Suelos del proyecto que no existe; "
             "el mejoramiento/reemplazo de suelo queda diferido a obra (tema repetido de los planos).\n"
             "Corregir: especificar las condiciones de mejoramiento/tratamiento de suelo "
             "(material, espesor, % de compactacion) y referenciarlas desde los planos.\n"
             "Requisito: condiciones de fundacion definidas en la ET, no diferidas a obra.")},
    {"id":"NOTA-11","fill":MENOR,"search":None,"page_fallback":2,
     "text":("NOTA-11: Emplazamiento y referencias del documento.\n"
             "Declara emplazamiento en Antofagasta e invoca un Informe de Mecanica de Suelos inexistente; "
             "el codigo de portada es tipo IT.\n"
             "Corregir: particularizar a Taltal (ambiente marino), adoptar sigma_adm <= 1,0 kg/cm2 del TR "
             "y corregir el codigo a ET.")},
]
if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
