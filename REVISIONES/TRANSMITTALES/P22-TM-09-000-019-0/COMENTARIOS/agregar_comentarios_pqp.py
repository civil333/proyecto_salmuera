"""
agregar_comentarios_pqp.py
Anota PDF Project Quality Plan Rev B (E44 / 25007-0044).

Checklist (CLAUDE.md Section 3.8):
  1. Tabla OBS/NOTE TM N19 Section 2.9: NOTE-01 = 1
  2. PDFs en submittal 25007-0044: 3 (este es 1 de los Code 2)
  3. Cross-cutting: vinculo BAE Clause 31 (40% payment milestone gate)
  4. len(COMENTARIOS) = 1
  5. ID coincide: Section 2.9 del transmittal TM N19

Veredicto: 2 - Approved as noted (Rev B cierra OBS-01/02 CRITICALs TM N17).
Color: fill MENOR (amarillo) — NOTE-01 severidad MINOR.
Texto sin etiqueta de criticidad (CLAUDE.md Section 3.8).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-003_B_PQP.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-003_B_PQP_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 44",
        "P22-BA-09-000-003_B_PQP.pdf",
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
        "fill": MENOR,
        "search": "FAT",
        "page_fallback": 0,
        "text": (
            "NOTE-01: FAT Approval Certificate format\n"
            "— provide a specimen template aligned\n"
            "with BAE Clause 31 as a tracked\n"
            "deliverable. Release of the 40 percent\n"
            "payment milestone remains gated on the\n"
            "cumulative satisfaction of (a) ADASA\n"
            "validation of the specimen template,\n"
            "(b) execution of the FAT and signature\n"
            "of the Acta de Aprobacion FAT by ADASA\n"
            "per BAE Clause 31, and (c) absence of\n"
            "contractual offsets from penalty clauses\n"
            "then in force. ADASA reserves all rights\n"
            "under BAE Clause 31 until the Acta is\n"
            "signed. No new PQP revision required."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
