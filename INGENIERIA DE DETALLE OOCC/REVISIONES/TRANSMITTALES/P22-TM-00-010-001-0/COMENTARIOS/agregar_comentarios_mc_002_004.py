# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-004_B (Fundación Contenedor RO). Código 2.
Comentarios ejecutivos (Defecto / Corregir / Requisito), ≤ ~8 líneas.
6 comentarios: OBS-01/02/03 + NOTA-01/02/08 (sin NOTA-07 — alcance
contenedor; las cargas de dosificación van en MC-005).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-004_B.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-MC-00-002-004_B_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "P22-TR-00-010-01-0", "ENTREGAS", "ENTREGA 3",
        "P22-MC-00-002-004_B.pdf",
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
        "page_fallback": 0,  # portada / titulo
        "text": (
            "OBS-01: Codificacion y alcance.\n"
            "Cuerpo \"Contenedor RO\" vs cover\n"
            "\"Compartida + CIP\" vs TR \"Fundacion\n"
            "compartida\"; incluye cargas de\n"
            "dosificacion (Sistema CIP).\n"
            "Corregir: reconciliar titulo/codigo/\n"
            "alcance; formalizar el split y el codigo\n"
            "-005 via 067-032-032-COR-LI-001; retirar\n"
            "las cargas de dosificacion (van en\n"
            "MC-005, TR 2.1.2: TK-09-002=490 kg;\n"
            "BDS=57,4 kg).\n"
            "Requisito: TR Sec. 6; Minuta MI-001 1.7."
        ),
    },
    {
        "id": "OBS-02", "fill": MENOR, "search": None,
        "page_fallback": 23,  # diseno de pedestales (TOC p.24)
        "text": (
            "OBS-02: Version interna de ACI 318.\n"
            "Pedestales citan ACI 318-10; el listado\n"
            "de codigos cita ACI 318-14.\n"
            "Corregir: unificar la version y\n"
            "reconciliarla con el TR (ACI 318-19, ver\n"
            "NOTA-01).\n"
            "Requisito: TR (ACI 318-19)."
        ),
    },
    {
        "id": "OBS-03", "fill": MAYOR, "search": None,
        "page_fallback": 10,  # modelos computacionales (TOC p.11)
        "text": (
            "OBS-03: NPT no declarado ni verificado.\n"
            "Usa solo el Modelo Navis Referencial (de\n"
            "consulta; prevalecen los planos 2D).\n"
            "Corregir: declarar el NPT de\n"
            "P22-DWG-06-005-103/-101, reflejarlo en\n"
            "P22-DWG-00-002-001 y verificarlo contra\n"
            "el Levantamiento DIO antes de Rev A;\n"
            "declarar la cota de la zona (~+6.00).\n"
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
        "id": "NOTA-08", "fill": MENOR, "search": None,
        "page_fallback": 12,  # carga peso de equipo (TOC p.13)
        "text": (
            "NOTA-08: Peso del contenedor.\n"
            "La memoria no explicita el peso del\n"
            "contenedor RO.\n"
            "Corregir: emplear y declarar el peso\n"
            "vinculante 14.934 kg (casco >=5.000 +\n"
            "internos 9.934) per TR Sec. 2.1.2 y\n"
            "plano civil y de cargas\n"
            "P22-DWG-09-005-001 Rev A.\n"
            "Requisito: TR Sec. 2.1.2;\n"
            "P22-DWG-09-005-001 Rev A."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
