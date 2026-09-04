"""
agregar_comentarios_uhpro_structural.py
Anota el UHPRO Structural Calculation Report Rev A (TM N26, Code 3 - To Be
Revised). len(COMENTARIOS) = 7 (OBS-01..05 + NOTE-01 + NOTE-02). Colores: fill
transmite severidad. Texto sin etiqueta de criticidad; OBS con linea 'Correct:'.

Documento GRANDE (523 paginas PDF). El pie de pagina del reporte numera 'Page N'
= indice 0-based del PDF (la portada no se cuenta), por lo que page_fallback
(0-based) coincide con el numero impreso del pie. Paginas (0-based) verificadas
contra el .md extraido, ubicando el contenido real (no la tabla de contenidos):
  OBS-01 / NOTE-01 -> pag 18 (Bolt Design at the Base; tabla de 8 unidades
                       auxiliares; nota 'concrete ... by others')
  OBS-02           -> pag 13 (C. Design Results)
  OBS-03           -> pag 33 (lista de combinaciones; casos 224/225 == 226/227,
                       ambos EOZ; falta el caso EOX 0.9(DS+DO+FR))
  OBS-04           -> pag 15 (Figure 13 Utilization Ratio of the Skid Frame)
  OBS-05           -> pag 4  (Table 1 Material Properties; Corten A / S275JR)
  NOTE-02          -> pag 5  (Table 4 Seismic Parameters; 'Type of Soil E')
Se usa search=None + page_fallback para anclar sin ambiguedad en un documento de
523 paginas (el mismo texto de las cabeceras se repite en muchas paginas y la
tabla de contenidos duplica los titulos).
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios

# --- Fast-save guard -------------------------------------------------------
# run_comentarios() guarda con garbage=4, deflate=True. En este reporte de 523
# paginas con imagenes embebidas esa recompresion total no converge (>min). Se
# fuerza un guardado equivalente y valido (garbage=1, deflate=False): mismas
# anotaciones, sin recomprimir los streams ya comprimidos del documento.
import fitz
_orig_save = fitz.Document.save
def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)
fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-005-001_A_UHPRO_Structural_Calc.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-005-001_A_UHPRO_Structural_Calc_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 59",
        "P22-CD-09-005-001_A UHPRO Structural Calculation Report.pdf",
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
        "search": None,
        "page_fallback": 18,
        "text": (
            "OBS-01: the Bolt Design at the Base\n"
            "checks only 8 ancillary units and omits\n"
            "the main process equipment - HP pump\n"
            "BH-09-001, turbos SIP-09-001/002, RO\n"
            "filter FIL-09-001 and pressure vessels\n"
            "BOI-09-001/002 (4160 kg) - which the\n"
            "Technical Specification requires anchored\n"
            "for NCh 2369 Zone 3. Correct: add the\n"
            "anchor check for these, or document and\n"
            "certify their anchorage route via the\n"
            "skid frame."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 18,
        "text": (
            "NOTE-01: the container base bolts to the\n"
            "concrete are deferred 'to others'.\n"
            "Transmit the governing base-bolt\n"
            "tension/shear as an interface table for\n"
            "the OOCC foundation, and clarify that\n"
            "'concrete by others' applies to the\n"
            "container base, not the equipment-to-skid\n"
            "anchors."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 13,
        "text": (
            "OBS-02: Design Results does not state the\n"
            "consolidated design seismic weight, the\n"
            "global base shear or the NCh 2369\n"
            "base-shear check; these live only in the\n"
            "seismic-load attachment. Correct:\n"
            "summarise them in the body."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MENOR,
        "search": None,
        "page_fallback": 33,
        "text": (
            "OBS-03: in the load-combination list,\n"
            "cases 226/227 duplicate 224/225 (both Z)\n"
            "and the X-direction minimum-gravity case\n"
            "0.9(DS+DO+FR)+1.1 EOX+/-0.3 EV is absent.\n"
            "Correct: fix cases 226/227 to the EOX\n"
            "case."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": None,
        "page_fallback": 15,
        "text": (
            "OBS-04: the skid-frame utilization is\n"
            "shown only as a colour map (Figure 13)\n"
            "without the governing maximum value.\n"
            "Correct: state the maximum utilization\n"
            "ratio and confirm it is below 1.0."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 4,
        "text": (
            "OBS-05: confirm the frame material\n"
            "(Corten A fy=345, S275JR fy=275) against\n"
            "the approved Structural Design Criteria\n"
            "Rev B and reconcile with the ASTM A-36\n"
            "reference of the Technical Specification;\n"
            "unify the revision label (Rev A vs 'A1')\n"
            "and the page count."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 5,
        "text": (
            "NOTE-02: the soil is labelled 'Type E'\n"
            "(NCh 433) while NCh 2369 uses Types I-IV.\n"
            "Confirm the soil type against the site\n"
            "geotechnical report and the T' and n\n"
            "parameters."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
