# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-002_B (Fundación Dinámica Bomba BH-06-001). Código 2.
Comentarios ejecutivos (Defecto / Corregir / Requisito), ≤ ~8 líneas.
6 comentarios: OBS-01 + NOTA-01/02/05/06/07. IDs y page_fallback fijos.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-002_B.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-MC-00-002-002_B_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "P22-TR-00-010-01-0", "ENTREGAS", "ENTREGA 3",
        "P22-MC-00-002-002_B.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado.")
    else:
        print(f"ERROR: PDF fuente no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MAYOR, "search": None,
        "page_fallback": 9,  # modelos computacionales (TOC p.10)
        "text": (
            "OBS-01: NPT no declarado ni verificado.\n"
            "Usa solo el Modelo Navis Referencial (de\n"
            "consulta; prevalecen los planos 2D).\n"
            "Corregir: declarar el NPT de\n"
            "P22-DWG-06-005-101/-103, reflejarlo en\n"
            "P22-DWG-00-002-001 y verificarlo contra\n"
            "el Levantamiento DIO antes de Rev A;\n"
            "declarar la cota de la zona (~+5.75).\n"
            "Requisito: TR Sec. 3.3.1, 4.1 y 2.1.3."
        ),
    },
    {
        "id": "NOTA-01", "fill": MAYOR, "search": None,
        "page_fallback": 4,  # codigos y manuales (TOC p.5)
        "text": (
            "NOTA-01: Version de ACI 318.\n"
            "Verificacion con ACI 318-14; el TR exige\n"
            "ACI 318-19.\n"
            "Corregir: demostrar equivalencia o\n"
            "re-verificar con ACI 318-19.\n"
            "Requisito: TR (ACI 318-19)."
        ),
    },
    {
        "id": "NOTA-02", "fill": MENOR, "search": None,
        "page_fallback": 7,  # parametros de suelo (TOC p.8)
        "text": (
            "NOTA-02: Recubrimientos.\n"
            "No se declaran los recubrimientos\n"
            "minimos.\n"
            "Corregir: declarar 50 mm expuesto / 70 mm\n"
            "en contacto con terreno.\n"
            "Requisito: TR (ambiente marino)."
        ),
    },
    {
        "id": "NOTA-05", "fill": MENOR, "search": None,
        "page_fallback": 4,  # normativa (TOC p.5)
        "text": (
            "NOTA-05: Base normativa sismica.\n"
            "Lista NCh 2369:2003 y :2025.\n"
            "Corregir: declarar que las fuerzas (base\n"
            "2003) son acotadas o conservadoras frente\n"
            "a :2025, o reconciliarlas.\n"
            "Requisito: TR (NCh 2369:2025)."
        ),
    },
    {
        "id": "NOTA-06", "fill": MENOR, "search": None,
        "page_fallback": 21,  # masa/frecuencia (TOC p.22-23)
        "text": (
            "NOTA-06: Margen masa/frecuencia.\n"
            "Criterios (relacion >=3; frecuencia fuera\n"
            "de +/-20%) solo en figuras.\n"
            "Corregir: reportar los valores numericos\n"
            "efectivos (relacion de masa y margen de\n"
            "frecuencia).\n"
            "Requisito: ACI 351.3R."
        ),
    },
    {
        "id": "NOTA-07", "fill": MAYOR, "search": None,
        "page_fallback": 11,  # carga peso de equipo (TOC p.12)
        "text": (
            "NOTA-07: Peso de BH-06-001.\n"
            "La memoria no declara el peso adoptado.\n"
            "Corregir: emplear y declarar el peso\n"
            "operativo de la ficha tecnica KSB (KNCPP\n"
            "11-050+160M); divergencia montaje 250 kg\n"
            "vs TR ~400 kg: resolver con la ficha y\n"
            "rehacer ACI 351.3R. Si no cumple, escala\n"
            "a Codigo 3.\n"
            "Requisito: ficha tecnica KSB; ACI 351.3R."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
