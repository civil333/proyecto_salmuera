# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-001_B (Fundación Estanque TK-06-001). Código 3.
Comentarios ejecutivos (Defecto / Corregir / Requisito), ≤ ~8 líneas.
6 comentarios: OBS-01/02 + NOTA-01/02/03/04. IDs y page_fallback fijos.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-001_B.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-MC-00-002-001_B_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "P22-TR-00-010-01-0", "ENTREGAS", "ENTREGA 3",
        "P22-MC-00-002-001_B.pdf",
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
        "page_fallback": 23,  # verificacion de anclajes (TOC p.24)
        "text": (
            "OBS-01: Anclaje del estanque.\n"
            "F1554 + cabeza + 30 cm = preinstalado,\n"
            "pero se verifica como mecanico\n"
            "postinstalado (inviable: doble malla,\n"
            "patron fijo del estanque).\n"
            "Corregir: redisenar preinstalado (colado\n"
            "en sitio, F1554) por ACI 318-19 Cap. 17 +\n"
            "Sec. 17.10; reconciliar con plano Exfibro\n"
            "EX-26005-F01 Rev C.\n"
            "Requisito: TR (ACI 318-19); ACI 318-19."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR, "search": None,
        "page_fallback": 9,  # modelos computacionales (TOC p.10)
        "text": (
            "OBS-02: NPT no declarado ni verificado.\n"
            "Usa solo el Modelo Navis Referencial (de\n"
            "consulta; prevalecen los planos 2D).\n"
            "Corregir: declarar el NPT de\n"
            "P22-DWG-06-005-103/-101, reflejarlo en\n"
            "P22-DWG-00-002-001 y verificarlo contra\n"
            "el Levantamiento DIO antes de Rev A;\n"
            "declarar la cota de la zona (~+5.75).\n"
            "Requisito: TR Sec. 3.3.1, 4.1 y 2.1.3."
        ),
    },
    {
        "id": "NOTA-01", "fill": MAYOR, "search": None,
        "page_fallback": 5,  # codigos y manuales (TOC p.6)
        "text": (
            "NOTA-01: Version de ACI 318.\n"
            "Anclajes y hormigon armado con ACI\n"
            "318-14; el TR exige ACI 318-19.\n"
            "Corregir: anclaje redisenado directo por\n"
            "ACI 318-19; resto del HA, demostrar\n"
            "equivalencia o re-verificar 318-19.\n"
            "Requisito: TR (ACI 318-19)."
        ),
    },
    {
        "id": "NOTA-02", "fill": MENOR, "search": None,
        "page_fallback": 8,  # parametros de suelo (TOC p.9)
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
        "id": "NOTA-03", "fill": MENOR, "search": None,
        "page_fallback": 14,  # cargas sismicas (TOC p.15)
        "text": (
            "NOTA-03: Origen de reacciones basales.\n"
            "La memoria no declara la fuente.\n"
            "Corregir: emplear y declarar las\n"
            "reacciones corregidas por ADASA\n"
            "(Ez=+/-3.357 kgf; M=431.846 kgf-cm;\n"
            "V=4.617 kgf) citando P22-IT-06-000-005-0;\n"
            "ratificacion Exfibro Rev B la gestiona\n"
            "ADASA.\n"
            "Requisito: P22-IT-06-000-005-0."
        ),
    },
    {
        "id": "NOTA-04", "fill": MENOR, "search": None,
        "page_fallback": 5,  # normativa (TOC p.6)
        "text": (
            "NOTA-04: Base normativa sismica.\n"
            "Lista NCh 2369:2003 y :2025; adopta\n"
            ":2025.\n"
            "Corregir: declarar que las fuerzas\n"
            "heredadas (base 2003) son acotadas o\n"
            "conservadoras frente a :2025, o\n"
            "reconciliarlas.\n"
            "Requisito: TR (NCh 2369:2025)."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
