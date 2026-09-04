"""
agregar_comentarios_antiscalant_pump.py
Agrega anotaciones FreeText del TM N11 al PDF GA Antiscalant Dosing Skid Pump Rev A — P22-DWG-09-005-011.
Nota: Primera entrega. Plano con fuente cifrada — texto no extraible. Se usa page_fallback.
      Archivo fuente puede tener zero-width space en el nombre — se usa glob para encontrarlo.
Observaciones:
  NOTE-06 (NOTE): Datos de anclaje sismico no incluidos en primera entrega
"""
import sys, os, shutil, glob as glob_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
    ".claude", "skills", "doc-annotator"))
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-011_REV.A GA of Antiscalant Dosing Skid Pump.pdf")
PDF_OUT   = os.path.join(SCRIPT_DIR,
    "P22-DWG-09-005-011_REV.A GA of Antiscalant Dosing Skid Pump_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    entrega_19 = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 19"))
    matches = glob_module.glob(os.path.join(entrega_19, "P22-DWG-09-005-011*.pdf"))
    if matches:
        shutil.copy2(matches[0], PDF_LOCAL)
        print("PDF fuente copiado a COMENTARIOS (normalizado sin zero-width space).")
    else:
        print("ERROR: PDF no encontrado en ENTREGA 19 con patron P22-DWG-09-005-011*.pdf")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-06",
        "fill": NOTE,
        "search": None,
        "page_fallback": 1,
        "text": (
            "NOTE-06: Seismic anchor data not\n"
            "included in this first submission.\n"
            "Plant site: Seismic Zone 3 per NCh 2369.\n"
            "Rev B must provide:\n"
            "  (1) Anchor bolt layout plan\n"
            "      (diameter, spacing, embedment)\n"
            "  (2) Seismic base reactions Fx, Fy, Fz\n"
            "  (3) Equipment mass for load verification\n"
            "Technical Basis: ET — Structural and\n"
            "Civil Requirements; NCh 2369."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
