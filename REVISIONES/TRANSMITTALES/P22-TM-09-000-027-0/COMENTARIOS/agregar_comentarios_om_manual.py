"""
agregar_comentarios_om_manual.py
Anota Operating and Maintenance Manual Rev A (TM N27, Code 2). len = 4
(OBS-01 MENOR + OBS-02 MENOR + OBS-03 MENOR + NOTE-01). Documento de texto.

Paginas 1-based del PDF Rev A (31 pags):
  OBS-01 = pag 23 (4.3.5 CIP Procedures: infografico generico sin cruce a 4.4)
  OBS-02 = pag 17 (recovery 42% en la prosa vs 42.86% control sequence)
  OBS-03 = pag 13 (Table 2.1 membrana 1a etapa 'LG SW 400 SR')
  NOTE-01 = pag 23 (lenguaje de plantilla que describe mal el servicio)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-012_A_OM_Manual.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-012_A_OM_Manual_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 64",
        "P22-BA-09-000-012_A Operating and Maintenance Manual.pdf",
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
        "search": "refer to control Narrative",
        "page_fallback": 21,
        "text": (
            "OBS-01: Section 4 (control sequence 4.4,\n"
            "setpoints, HMI 4.5) reproduces logic the\n"
            "Control Philosophy assigns to the Operating\n"
            "Sequence Chart (017, not issued), the Alarm &\n"
            "Control Setpoint List (015, Rev B under\n"
            "review) and the HMI Screenshots (016, Rev A\n"
            "incomplete) - all open. The manual states\n"
            "control logic and setpoints with no approved\n"
            "source. Correct: reconcile Section 4 with those\n"
            "documents once issued; it cannot go to IFC\n"
            "until they close."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 23,
        "offset_y": 70,
        "text": (
            "OBS-02: Note 5 (this matrix) opens the turbo\n"
            "bypass VE-09-002 by TDS ('Low TDS value (SP 62\n"
            "Bar) will activate the bypass'). The approved\n"
            "Control Philosophy Rev D says the opposite:\n"
            "'TDS shall not directly initiate bypass; bypass\n"
            "modulation shall be governed by the pressure\n"
            "control loop'. The note also mixes TDS with\n"
            "pressure and calls VE-09-002 'Interstage' (CP:\n"
            "Feed Turbocharger Bypass).\n"
            "Correct: fix the bypass logic, basis and tag to\n"
            "the approved Control Philosophy."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "42% recovery rate",
        "page_fallback": 16,
        "text": (
            "OBS-03: the operating setpoints are\n"
            "inconsistent and diverge from the setpoint\n"
            "list: HP discharge 52 bar (prose) vs 55 bar\n"
            "(matrix) vs 51 bar (015); recovery 42% vs\n"
            "42.86%; matrix flows do not reconcile with 015.\n"
            "Correct: reconcile all setpoints against the\n"
            "approved Alarm & Control Setpoint List."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "Rockwell Automation default-built",
        "page_fallback": 26,
        "text": (
            "OBS-04: the HMI section is not configured - the\n"
            "faceplates (4.5.1) are default Rockwell library\n"
            "objects with placeholders, and the process\n"
            "screens and alarm history (4.5.2) are\n"
            "simulation data, not the project's tags,\n"
            "ranges and alarm setpoints.\n"
            "Correct: re-issue with the configured HMI once\n"
            "the HMI Screenshots close."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MENOR,
        "search": "Lockout/tagout pumps and valves",
        "page_fallback": 22,
        "text": (
            "OBS-05: housekeeping - subsection 4.3.5 CIP is\n"
            "a generic infographic not linked to the CIP\n"
            "matrices in Section 4.4 and states no recipe\n"
            "basis; confirm the 1st-stage membrane 'LG SW\n"
            "400 SR' (Table 2.1) vs the LG datasheet; and\n"
            "clean the generic template language ('potable/\n"
            "industrial/wastewater reuse', 'PASS RO unit')."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
