"""
agregar_comentarios_valve_list.py
Anota PDF Valve List Rev D (E38 / submittal 25007-0038, 3 paginas).

NOTA (re-disposicion 18-May-2026): Valve List Rev D = Code 1 - Approved.
Code 1 NO lleva CC_ADASA (regla CLAUDE.md section 3.8). Este script y su
_CC_ADASA.pdf NO se emiten ni se adjuntan al transmittal; se conservan como
traza interna de analisis. El entregable residual (analisis de sobrepresion
PSV-09-002) se trackea en la Seccion 3 del transmittal, no como anotacion.

Checklist (CLAUDE.md section 3.8):
  1. Tabla NOTE del transmittal Section 2.2: NOTE-01, NOTE-02 = 2
  2. PDFs en submittal 25007-0038: 2 (Valve List Rev D, Line List Rev C)
     Line List Rev C es Code 1 -> NO se anota (sin CC_ADASA)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 2
  5. IDs coinciden: Section 2.2 del transmittal TM N18

Veredicto: 2 - Approved as Noted (tabla de valvulas = Rev D ya Code 2 en TM N14;
CCS responde a TM N14). PDF con render de glifos triplicado -> search=None,
ancla por page_fallback (CLAUDE.md section 3.8, memoria doc_annotator).
Texto sin etiqueta de criticidad; fill transmite severidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_D_Valve_List.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-005-002_D_Valve_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 38",
        "P22-LI-09-005-002_D Valve List.pdf",
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
        "fill": MAYOR,
        "search": None,
        "page_fallback": 2,  # 0-based -> pagina 3 (Consolidated Comment Sheet)
        "text": (
            "NOTE-01: PSV-09-002 overpressure\n"
            "protection adequacy not demonstrated.\n"
            "TM N14 requested an overpressure /\n"
            "relief sizing analysis after the second\n"
            "PSV-09-002 was removed (112 -> 111), or\n"
            "reinstatement with a unique TAG. The CCS\n"
            "only states PSV-09-002 is at Item 104 --\n"
            "it confirms one device exists but does\n"
            "not demonstrate adequacy.\n"
            "\n"
            "Action to issue at IFC Rev 0 -- no new\n"
            "Valve List revision required:\n"
            "1) Submit the overpressure protection /\n"
            "   relief sizing analysis (protected\n"
            "   volume, relief scenario, set\n"
            "   pressure, required vs installed\n"
            "   relief capacity).\n"
            "2) Align future comment responses with\n"
            "   the revision protocol: advance the\n"
            "   revision letter when content changes;\n"
            "   do not re-issue the same revision\n"
            "   with only a Consolidated Comment\n"
            "   Sheet.\n"
            "ADASA accepts the Valve List at IFC\n"
            "Rev 0 once item 1 is submitted and\n"
            "reviewed."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 0,  # 0-based -> pagina 1 (revision history / title block)
        "text": (
            "NOTE-02: Revision control. Transmittal\n"
            "N14 comments answered by re-issuing the\n"
            "same Rev D (table dated 18-Mar-2026,\n"
            "unchanged) with an appended Consolidated\n"
            "Comment Sheet. For Code-2 documents ADASA\n"
            "notes are incorporated at IFC Rev 0\n"
            "without an interim re-issue of the same\n"
            "revision letter. Align future responses\n"
            "with the revision protocol -- advance the\n"
            "revision when content changes or carry\n"
            "the disposition to IFC Rev 0."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
