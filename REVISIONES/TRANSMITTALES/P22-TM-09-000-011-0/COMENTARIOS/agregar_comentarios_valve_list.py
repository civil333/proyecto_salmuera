"""
agregar_comentarios_valve_list.py
Agrega anotaciones FreeText del TM N11 al PDF Valve List Rev C — P22-LI-09-005-002.
Observaciones:
  OBS-01 (MAYOR): TAG VE-09-007 duplicado en items 44 y 64
  OBS-02 (MAYOR): TAG PSV-09-002 duplicado en items 105 y 112
  NOTE-01 (NOTE): VM-07-005 area-07 persiste (TM N3 OBS-13 sin corregir)
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import MAYOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-LI-09-005-002_REV.C Valve List.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-LI-09-005-002_REV.C Valve List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_19 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 19"))
    matches = glob_module.glob(os.path.join(entrega_19, "P22-LI-09-005-002*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS.")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 19 con patron P22-LI-09-005-002*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "VE-09-007",
        "page_fallback": 2,
        "text": (
            "OBS-01 (MAJOR): TAG VE-09-007 is\n"
            "duplicated — appears in BOTH item 44\n"
            "and item 64. These are distinct valves.\n"
            "Assign a unique TAG to one item in\n"
            "Rev D. Update P&ID, Instrument List,\n"
            "and I/O List accordingly.\n"
            "CCS response 'all valves have unique\n"
            "TAGs' is factually incorrect."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "PSV-09-002",
        "page_fallback": 3,
        "text": (
            "OBS-02 (MAJOR): TAG PSV-09-002 is\n"
            "duplicated — appears in BOTH item 105\n"
            "and item 112. These are distinct safety\n"
            "relief valves at different locations.\n"
            "Assign a unique TAG to item 112 in\n"
            "Valve List Rev D and update all\n"
            "referencing documents."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "VM-07-005",
        "page_fallback": 0,
        "text": (
            "NOTE-01: TAG VM-07-005 uses area code\n"
            "'07' — no such area exists in this\n"
            "project. Correct to VM-09-005 in Rev D.\n"
            "Also verify VM-07-031 and VE-07-009.\n"
            "First raised in TM N3 OBS-13 —\n"
            "uncorrected in Rev B and Rev C."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
