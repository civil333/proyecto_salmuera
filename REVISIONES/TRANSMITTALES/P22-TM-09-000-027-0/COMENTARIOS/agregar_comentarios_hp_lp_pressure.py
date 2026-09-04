"""
agregar_comentarios_hp_lp_pressure.py
Anota PDF HP and LP Pressure Test Procedure Rev C (TM N27, Code 3). len(COMENTARIOS) = 5
(OBS-01 CRITICAL + OBS-02 MAYOR + OBS-03 MENOR + OBS-04 MENOR + NOTE-01).
El fill transmite severidad; el texto FreeText arranca directo con "OBS-XX:" / "NOTE-01:".

Paginas 0-based del PDF Rev C (15 pags):
  OBS-01 = 10 (impresa 11, Line List embebida: DA-PVC-DN65-09-016 diseno 50 bar -> 75 bar)
  OBS-02 = 10 (impresa 11, cabecera "Rev. No: 0" de la misma Line List)
  OBS-03 =  6 (impresa 7, clausula 5.5.12 que defiere al line list)
  OBS-04 =  8 (impresa 9, subseccion 5.7.2 sin 5.7.2.2)
  NOTE-01 = 12 (impresa 13, Pressure and Leak Test Report form AQ-QAM-F018)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-010_C_HP_LP_Pressure_Test.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 63",
        "P22-BA-09-000-010_C HP and LP Pressure Test Procedure.pdf",
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
        "fill": CRITICAL,
        "search": "DA-PVC-DN65-09-016",
        "page_fallback": 10,
        "text": (
            "OBS-01: line DA-PVC-DN65-09-016 (RO Brine\n"
            "Discharge) is PVC SCH 80 DN65 operating at\n"
            "1 bar, yet it carries a 50 bar design pressure,\n"
            "so this column orders a 75 bar hydrostatic test\n"
            "on a plastic line with Class 150 flanges.\n"
            "Testing to this value would rupture the line.\n"
            "Correct: reconcile the piping class and the\n"
            "design pressure of this line per ET Section\n"
            "5.2.1 - Low-Pressure Piping, and re-derive the\n"
            "test pressure from the corrected value."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "Rev. No: 0",
        "page_fallback": 10,
        "text": (
            "OBS-02: this Line List is labelled Rev 0, a\n"
            "revision never transmitted. The revision ADASA\n"
            "approved is Rev C (Code 1, Transmittal N18),\n"
            "and it carries no HYDROTEST PRESS. column.\n"
            "Correct: transmit the corrected Line List\n"
            "revision as a submittal and cite it in the\n"
            "procedure body by number and revision."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": "Minimum test pressure 1.5 X design pressure",
        "page_fallback": 6,
        "text": (
            "OBS-03: the body still writes no numeric test\n"
            "pressure and states it as a minimum, not as the\n"
            "single value to apply.\n"
            "Correct: state the governing envelope per\n"
            "circuit (135 bar HP / 7.5 bar LP, per ITP rows\n"
            "5.2 and 5.1) and name the Line List revision\n"
            "that fixes the value line by line."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": "The weld joint must be clean and dry before re-welding",
        "page_fallback": 8,
        "text": (
            "OBS-04: subsection 5.7.2 still skips 5.7.2.2\n"
            "(5.7.2.1 jumps to 5.7.2.3). The gap at 5.6.5 is\n"
            "corrected; this one was reported as resolved in\n"
            "the previous reply and survives.\n"
            "Correct: renumber contiguously."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Pressure and Leak Test Report",
        "page_fallback": 12,
        "text": (
            "NOTE-01: the report form is now attached and\n"
            "carries no pre-printed pressure, which closes\n"
            "the Transmittal N26 note. It has no field for\n"
            "the required test pressure, only for the applied\n"
            "one.\n"
            "Correct: add a Required Test Pressure field\n"
            "referencing the approved Line List revision."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
