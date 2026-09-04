"""
agregar_comentarios_cable_tray_revB.py
Traduce ES->EN de las 5 anotaciones FreeText pre-existentes en el PDF Cable Tray Rev B
(comentadas por ADASA en E32/COMENTARIOS). Mantiene posicion, color y tamano (CLAUDE.md §3.11).

PDF fuente:  ENTREGAS_BWWATER/ENTREGA 32/COMENTARIOS/P22-DWG-09-007-004_B Cable Tray Layout and Support Details (CC ADASA).pdf
PDF salida:  P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf

Anotaciones ES->EN (5 items, mapping a OBS-04 .. OBS-08):
  OBS-04 — Support S4 conflicts with antiscalant tank
  OBS-05 — UNISTRUT anchoring to container steel not detailed
  OBS-06 — MAIN PANEL incoming routing not indicated
  OBS-07 — S3/S4 zoning ambiguous (dosing skid vs main panel)
  OBS-08 — Cable tray run conflicts with CIP system
"""
import sys
import os
import shutil

import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..",
    "ENTREGAS_BWWATER", "ENTREGA 32", "COMENTARIOS",
    "P22-DWG-09-007-004_B Cable Tray Layout and Support Details (CC ADASA).pdf",
))
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-004_B_Cable_Tray_CC_ADASA.pdf")

TRANSLATIONS = {
    "No queda claro que esto se pueda soportar con s4, sin intervenir con el tanque de dosificacion y el resto de los componentes":
        "antiscalant dosing tank TK-09-002 and\n"
        "adjacent components. Cannot be installed\n"
        "without intervening on the dosing skid.\n"
        "Clash check vs Equipment Layout Rev B and\n"
        "Piping Layout Rev B required.\n"
        "Relocate S4 or reposition equipment.\n"
        "See Transmittal N15 Section 2.8 / OBS-04.",

    "Indicar a la brevedad en los planos del MAIN PANEL como es el incoming, por lo que entiende deb ser por  debajo del panel":
        "ADASA interpretation: incoming should enter\n"
        "from below the panel.\n"
        "Confirm entry point and update cable tray\n"
        "routing, conduit penetrations and civil work\n"
        "coordination accordingly.\n"
        "See Transmittal N15 Section 2.8 / OBS-06.",

    "No se entiende si esto es para el skid de dosificacion quimica o para el panel principa. De acuerdo al plano en planta S3 es al interior del modulo":
        "Plan view places S3 inside the module,\n"
        "conflicting with this detail.\n"
        "Reconcile S3/S4 zoning legend; map each\n"
        "support zone (S1-S6) unambiguously to its\n"
        "supported equipment.\n"
        "See Transmittal N15 Section 2.8 / OBS-07.",

    "Esto tienen interferencias con todo el sistema CIP":
        "Clash detection vs Piping Layout Rev B\n"
        "required.\n"
        "Reroute the tray (lift above CIP elevation,\n"
        "go around CIP envelope, or use a structure\n"
        "that does not block CIP maintenance access).\n"
        "See Transmittal N15 Section 2.8 / OBS-08.",

    "COmo quedan los perfiles UNISTRUT anclados al acero del container, esto es alcance de BW WATERS y debe venir listo con el envio":
        "Notes show 'WELD/BOLTING' without anchor\n"
        "plate dimensions, weld type/length, bolt\n"
        "grade/torque or shell reinforcement.\n"
        "Container is BW Water scope: supports must\n"
        "ship pre-anchored with qualified attachment\n"
        "points to allow ADASA's structural review.\n"
        "See Transmittal N15 Section 2.8 / OBS-05.",
}


def main():
    if not os.path.exists(PDF_SRC):
        print(f"ERROR: source PDF not found:\n  {PDF_SRC}")
        sys.exit(1)

    shutil.copy2(PDF_SRC, PDF_OUT)
    print(f"Copied: {os.path.basename(PDF_OUT)}")

    doc = fitz.open(PDF_OUT)
    translated = 0
    not_found = []
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
