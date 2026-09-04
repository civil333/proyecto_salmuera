"""
agregar_comentarios_io_list.py
Anota PDF IO List Rev 4 (TM N25, Code 2 - Approved as Noted). len(COMENTARIOS) = 4
(OBS-01 + NOTE-01 + NOTE-02 + NOTE-03). Colores: fill transmite severidad. Texto
sin etiqueta de criticidad. Paginas (0-based): senales interfaz=1, valvulas=2,
dosificadoras=3.

Re-verdict (29-Jun): las 4 senales de coordinacion con el PLC externo estan
cumplidas (cierra OBS-01 del N24); el esquema soft-I/O Ethernet/IP de campo fue
aceptado en N20 y NO se reabre -> se retiro la observacion 'soft-BOOL = no feedback'
(over-reach). Quedan: OBS-01 (celda de conteo, heredada del N24, menor) + NOTE-02
(confirmar la fuente del dato) + NOTE-01 (record de cierre) + NOTE-03 (cross-check).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_4_IO_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-008-001_4_IO_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 56",
        "P22-LI-09-008-001_4 IO List.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "SYSTEM ENABLE COMMAND FROM DCS",
        "page_fallback": 1,
        "text": (
            "NOTE-01: the four module-to-external-PLC\n"
            "interface signals are present and correctly\n"
            "typed as relay contacts - XA005 ENABLE (DI),\n"
            "YA001 RUNNING (DO), YA002 FAULT (DO),\n"
            "YA003 LOCAL/REMOTE (DO). Transmittal N24\n"
            "OBS-01 closed (an ADASA extension of the\n"
            "interface)."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": "MOTORIZED VALVE",
        "page_min": 2,
        "page_fallback": 2,
        "text": (
            "NOTE-03: the Valve List and the P&ID needed\n"
            "to cross-check the VE-09 motorized-valve I/O\n"
            "are not part of this submittal; the cross-check\n"
            "is tracked. BW Water reports the tags are\n"
            "aligned (VE09 to VE-09)."
        ),
    },
    {
        "id": "OBS-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 3,
        "offset_y": 470,
        "text": (
            "OBS-01: the dosing-pump RUNNING (items 131\n"
            "and 136, typed BOOL) carry no signal-type\n"
            "count in any column; items 129 and 134 place\n"
            "the count in the DI column rather than BOOL.\n"
            "The Transmittal N24 observation persists.\n"
            "Correct: complete the BOOL count cells."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 3,
        "offset_y": 470,
        "text": (
            "NOTE-02: confirm the dosing-pump run status\n"
            "(items 131/136, BOOL over Ethernet/IP, shown\n"
            "FROM the HMI) reflects a verified feedback from\n"
            "the pump or its drive, not an echo of the\n"
            "operator faceplate. The soft-I/O Ethernet/IP\n"
            "scheme accepted at Transmittal N20 is not\n"
            "reopened."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
