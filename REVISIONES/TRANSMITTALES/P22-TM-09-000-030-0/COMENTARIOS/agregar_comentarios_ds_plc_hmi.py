"""
agregar_comentarios_ds_plc_hmi.py
Anota el Datasheet of PLC and HMI Panel Component Rev 0 (TM N30, Code 2 -
Approved as Noted). len(COMENTARIOS) = 4 (OBS-01 + NOTE-01 a NOTE-03).
Colores: el fill transmite severidad (MAYOR = naranja, NOTE = azul). Texto sin
etiqueta de criticidad.

Paginas (0-based) verificadas por render contra el PDF de la ENTREGA 68:
  OBS-01  -> pag 46 (pagina 47 impresa: hoja del componente HMI, "4 Model -
             2711P-T10C22D9P"; las paginas 48-49 embeben la hoja NHP del
             PanelView Plus 7 Performance para ese numero de catalogo)
  NOTE-01 -> pag 0   (portada; cajetin "Page: 1of 49" con 50 paginas reales)
  NOTE-02 -> pag 1   (primera hoja de componente; "Issued for: ISSUED FOR
             APPROVAL" en una emision que el Submittal Form declara IFC)
  NOTE-03 -> pag 49 (pagina 50 impresa: Consolidated Comment Sheet)
Documento de 50 paginas.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, run_comentarios

# --- Fast-save guard -------------------------------------------------------
# run_comentarios() guarda con garbage=4, deflate=True. En este datasheet
# (Rockwell/Allen-Bradley embebido, imagenes ya comprimidas) esa recompresion
# total no converge. Se fuerza un guardado equivalente y valido
# (garbage=1, deflate=False): mismas anotaciones, sin recomprimir streams.
import fitz
_orig_save = fitz.Document.save
def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)
fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-ET-09-008-001_0_DS_PLC_HMI.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-ET-09-008-001_0_DS_PLC_HMI_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 68",
        "P22-ET-09-008-01_0 Datasheet of PLC and HMI Panel Component "
        "(Major Component).pdf",
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
        "search": None,
        "page_fallback": 46,
        "text": (
            "OBS-01: this sheet states 2711P-T10C22D9P\n"
            "and requires 2 x Ethernet RJ45 and 1 GB RAM\n"
            "(rows 15 and 18). The control set carries\n"
            "2711P-T10C21D8S: the panel bill of material\n"
            "of the Outline Panel Drawing Rev 0 issued\n"
            "for construction, the Schematic Rev A, the\n"
            "FAT Procedure Rev A and the Control System\n"
            "Architecture. Per the manufacturer data the\n"
            "'21' field is a single 10/100Base-T port and\n"
            "that terminal has 512 MB RAM, so it does not\n"
            "meet the two rows above. Declare the binding\n"
            "catalogue number and align the other set\n"
            "before the panel is built."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 0,
        "text": (
            "NOTE-01: the cover block reads\n"
            "'Page: 1 of 49' and the document has 50\n"
            "pages; Rev C declared 50. Correct the page\n"
            "count at the next issue."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 1,
        "text": (
            "NOTE-02: the seven component headers keep\n"
            "'Issued for: ISSUED FOR APPROVAL' while the\n"
            "Submittal Form 25007-0068 submits this\n"
            "revision for construction. Align the issue\n"
            "status of the sheets with the submission."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": None,
        "page_fallback": 49,
        "text": (
            "NOTE-03: the reply to NOTE-01 states the\n"
            "correction was made in 'P22-ET-09-008-001\n"
            "Rev D' while this issue is Rev 0. The\n"
            "delivered file name also keeps the former\n"
            "two-digit code. Correct both for traceability."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
