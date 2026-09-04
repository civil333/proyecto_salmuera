"""
agregar_comentarios_equipment_layout_revB.py
Anota PDF Equipment Layout Rev B (E32 / submittal 25007-0032).

Traduce ES->EN de la anotacion FreeText pre-existente (NOTE-04, weight table)
desde el PDF en E32/COMENTARIOS. Mantiene posicion, color y tamano (CLAUDE.md §3.11).

Checklist (CLAUDE.md §3.10):
  IDs en transmittal MD §2.5: NOTE-04 (MAJOR) = 1 total

v5: NOTE-05 (CIP Tank location) REMOVIDA — vestigio sin sentido tras
WITHDRAWAL del 3,500 mm footprint constraint (Section 2.6 TM N5/N7 OBS-01).

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..",
    "ENTREGAS_BWWATER", "ENTREGA 32", "COMENTARIOS",
    "P22-DWG-09-005-003_B Equipment Layout (cc adasa).pdf",
))
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-003_B_Equipment_Layout_CC_ADASA.pdf")

TRANSLATIONS = {
    "INCLUIR LA TABLA CON PESOS EN OPERACION DEL CONTAINER DE PLANTA Y TODOS LOS EQUIPOS EXTERIORES":
        "BW Water has confirmed delivery on\n"
        "23-Apr-2026 of a Civil Loading drawing;\n"
        "ADASA accepts it as a separate supporting\n"
        "deliverable.\n"
        "The Operating Weight table itself must be\n"
        "restored to this drawing in Rev 0 covering\n"
        "all equipment inside and outside the\n"
        "container (Rev A baseline 34,739 lb /\n"
        "15,758 kg plus CIP Heater REL-09-001).\n"
        "The Civil Loading drawing supplements but\n"
        "does not replace the embedded table.\n"
        "See Transmittal N15 Section 2.5 / NOTE-04.",
}


def main():
    if not os.path.exists(PDF_SRC):
        print(f"ERROR: source PDF not found:\n  {PDF_SRC}")
        sys.exit(1)

    shutil.copy2(PDF_SRC, PDF_OUT)
    print(f"Copied: {os.path.basename(PDF_OUT)}")

    doc = fitz.open(PDF_OUT)
    translated = 0
    for page in doc:
        for annot in page.annots() or []:
            content = (annot.info.get("content") or "").strip()
            if content in TRANSLATIONS:
                annot.set_info(content=TRANSLATIONS[content])
                annot.update()
                translated += 1

    tmp = PDF_OUT + ".tmp"
    doc.save(tmp)
    doc.close()
    os.replace(tmp, PDF_OUT)

    print(f"Translated {translated} annotation(s) ES -> EN.")
    if translated != len(TRANSLATIONS):
        print(f"WARNING: expected {len(TRANSLATIONS)} translations, got {translated}.")


if __name__ == "__main__":
    main()
