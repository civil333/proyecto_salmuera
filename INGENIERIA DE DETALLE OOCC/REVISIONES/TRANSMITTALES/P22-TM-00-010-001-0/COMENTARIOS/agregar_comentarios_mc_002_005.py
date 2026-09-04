# -*- coding: utf-8 -*-
"""
Anota P22-MC-00-002-005_B (Fundación Sistema CIP). Código 2.
Comentarios ejecutivos (Defecto / Corregir / Requisito), ≤ ~8 líneas.
7 comentarios: OBS-01/02/03 + NOTA-01/02/05/07.
OBS-01 anclajes = diferido por datos del proveedor (NO rechazo).
NOTA-07 pesos dosificación = corregir a ≈550 kg.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-MC-00-002-005_B.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-MC-00-002-005_B_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "P22-TR-00-010-01-0", "ENTREGAS", "ENTREGA 3",
        "P22-MC-00-002-005_B.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF fuente copiado.")
    else:
        print(f"ERROR: PDF fuente no encontrado:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01", "fill": MENOR, "search": None,
        "page_fallback": 33,  # diseno de pernos de anclaje (TOC p.34)
        "text": (
            "OBS-01: Verificacion de anclajes diferida.\n"
            "Diferida por falta de planos/fichas\n"
            "finales del proveedor de equipos CIP;\n"
            "seran postinstalados. No es rechazo: OK\n"
            "si cumplen las solicitaciones.\n"
            "Corregir: completar con anclajes\n"
            "postinstalados dimensionados a las cargas\n"
            "por ACI 318-19 Cap. 17 + Sec. 17.10,\n"
            "precalificados sismicos (ACI 355.2/355.4\n"
            "Cat. 1, ESR ICC-ES), al recibir los datos\n"
            "(Seccion 3 PEND-03).\n"
            "Requisito: TR; ACI 318-19; ACI 355.2/.4."
        ),
    },
    {
        "id": "OBS-02", "fill": MAYOR, "search": None,
        "page_fallback": 0,  # portada / titulo
        "text": (
            "OBS-02: Codificacion.\n"
            "El codigo P22-MC-00-002-005 no esta\n"
            "previsto en el TR Sec. 6 (CIP dentro de\n"
            "-004 \"Fundacion compartida\").\n"
            "Corregir: formalizar el split y el nuevo\n"
            "codigo via 067-032-032-COR-LI-001 (ver\n"
            "subseccion 2.3, OBS-01).\n"
            "Requisito: TR Sec. 6."
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
        "page_fallback": 5,  # codigos y manuales (TOC p.6)
        "text": (
            "NOTA-01: Version de ACI 318.\n"
            "Verificacion con ACI 318-14; el TR exige\n"
            "ACI 318-19.\n"
            "Corregir: verificar anclajes con ACI\n"
            "318-19; resto del HA, demostrar\n"
            "equivalencia o re-verificar 318-19.\n"
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
        "page_fallback": 5,  # normativa (TOC p.6)
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
        "id": "NOTA-07", "fill": MENOR, "search": None,
        "page_fallback": 16,  # carga peso de equipo (TOC p.17)
        "text": (
            "NOTA-07: Pesos de dosificacion.\n"
            "La memoria asume 500 + 500 kg (~1000 kg).\n"
            "Corregir: declarar los pesos correctos\n"
            "del TR Sec. 2.1.2 -- TK-09-002 = 490 kg y\n"
            "BDS-09-001/002 = 57,4 kg (~550 kg total).\n"
            "El diseno actual (~1000 kg) es\n"
            "conservador y no requiere recalculo, pero\n"
            "el valor declarado debe corregirse a\n"
            "~550 kg.\n"
            "Requisito: TR Sec. 2.1.2."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
