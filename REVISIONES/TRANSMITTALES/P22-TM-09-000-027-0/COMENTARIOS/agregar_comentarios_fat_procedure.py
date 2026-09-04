"""
agregar_comentarios_fat_procedure.py
Anota PLC/LCP FAT Procedure - Hardware Rev A (TM N27, Code 2 - Approved as Noted).
len = 5 (OBS-01 MAYOR + OBS-02 MENOR + OBS-03 MENOR + NOTE-01 + NOTE-02).
Documento de texto.

El RTD winding/bearing (antes OBS-02 MAYOR) se reclasifico a NOTE-02: el FAT esta
CORRECTO (= IO List Rev 4); el swap vive en el Alarm & Interlock List (abierto,
Seccion 3) -> es dependencia cruzada, no defecto del FAT. Los OBS-03/04 previos se
renumeraron a OBS-02/03 (consecutivo, §3.3.1).

Paginas 1-based del PDF Rev A (19 pags):
  OBS-01  = pag 4  (Reference Documents: codigo ET vs CD del Outline/Schematic)
  OBS-02  = pag 16 (AO Ch3 tag BDS-09-001 en vez de -002; + doc number; KA2/KA3)
  OBS-03  = pag 6  (mounting plate HDG vs zinc-plated; + soft-BOOL vs IO List)
  NOTE-01 = pag 3  (scope: cobertura completa y consistente con la ET)
  NOTE-02 = pag 14 (tabla RTD correcta; swap en el Alarm & Interlock List -> Sec 3)
El anclaje del OBS-01 usa page_min=3 para caer en la tabla de Reference Documents
(pag 4), no en el Drawing Reference de la pag 2 donde el mismo codigo aparece.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-PP-09-000-001_A_FAT_Procedure.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-PP-09-000-001_A_FAT_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 64",
        "P22-PP-09-000-001_A PLC-LCP FAT Procedure - Hardware.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "P22-ET-09-008-001",
        "page_min": 3,
        "page_fallback": 3,
        "text": (
            "OBS-01: the governing drawings are cited under\n"
            "wrong or not-issued references. The Outline is\n"
            "cited 'P22-ET-09-008-001' (real code\n"
            "P22-CD-09-008-001; the ET number is the PLC &\n"
            "HMI Datasheet). The Schematic is cited\n"
            "'P22-ET-09-008-002 Rev B', but it exists only\n"
            "at Rev A - Rev B does not exist.\n"
            "Correct: cite the correct CD codes and the\n"
            "issued Schematic revision before witnessing."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": "Antiscalant Dosing Pump 2 Speed Control",
        "page_fallback": 15,
        "text": (
            "OBS-02: AO Ch3 tag for Antiscalant Dosing\n"
            "Pump 2 reads 'BDS-09-001-SIC001' (Pump 1 tag);\n"
            "the IO List assigns '-002'. The project block\n"
            "gives the doc number 'P22-PP-000-001', missing\n"
            "the -09 segment. The local/remote DO label\n"
            "reads KA2 where the test verifies KA3.\n"
            "Correct at issue: fix the three."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Hot-Dip Galvanized",
        "page_fallback": 5,
        "text": (
            "OBS-03: two acceptance criteria differ from the\n"
            "approved documents: the mounting plate is\n"
            "'Hot-Dip Galvanized' vs the Outline's\n"
            "zinc-plated, and the dosing-pump running\n"
            "signals are tested as hardwired DI vs the IO\n"
            "List's soft Ethernet/IP (N20 scheme).\n"
            "Correct at issue: reconcile with the IO List;\n"
            "no signal-type change is required."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Software functional testing",
        "page_fallback": 2,
        "text": (
            "NOTE-01: the FAT's hardware coverage and\n"
            "acceptance criteria are complete and\n"
            "consistent with the approved IO List Rev 4 and\n"
            "the ET (four relay-contact DCS signals, Pt-100\n"
            "winding and bearing on both motors). The notes\n"
            "are documentary corrections to incorporate at\n"
            "issue, not gaps in the test."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "TE09-001-XQ001",
        "page_fallback": 13,
        "text": (
            "NOTE-02: this RTD table is correct\n"
            "(TE-09-001=winding, TE-09-002=bearing = the\n"
            "approved IO List Rev 4). The winding/bearing\n"
            "definition is swapped in the Alarm & Interlock\n"
            "List Rev B (open, tracked in Section 3); if\n"
            "programmed from that list, the bearing would\n"
            "run to 140C before tripping. This procedure\n"
            "needs no change here; the RTD protection tests\n"
            "are witnessed only after that list is\n"
            "reconciled to this mapping and the bearing AHH\n"
            "is set to the vendor-confirmed 95C."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
