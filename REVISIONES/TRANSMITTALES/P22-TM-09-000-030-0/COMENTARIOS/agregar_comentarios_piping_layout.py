#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_piping_layout.py
Anota el Piping Layout Rev C (P22-DWG-09-005-004), del submittal 25007-0070
(E70). Veredicto del TM N30: Code 2 - Approved as noted sobre las cuatro
paginas del documento, mas el conjunto de taller devuelto como no recibido.

UN SOLO PDF ANOTADO PARA DOS SUBSECCIONES DEL TRANSMITTAL. Los planos de taller
25007-ME-PI-0901-0006 a -0016 NO son un archivo aparte: son las paginas 5 a 21
de este mismo PDF. Por eso los IDs corren CORRELATIVOS a lo largo de todo el
archivo (OBS-01 a OBS-06, NOTE-01 a NOTE-03) y no se reinician por subseccion:
dos observaciones distintas no pueden compartir ID dentro de un mismo anotado.

len(COMENTARIOS) = 9.

Estructura del archivo, verificada pagina por pagina (indices 0-based):
    0        portada A4, cajetin "Page: 1 of 4", Rev C
    1, 2, 3  las tres laminas del Piping Layout, A1 apaisada, rotation 270
    4..20    once planos de taller de BW Water, numeracion 25007-ME-PI-0901-
             0006 a -0016, con sello FOR CONSTRUCTION en las 17 paginas:
               4 -> -0006   5 -> -0007   6,7 -> -0008   8,9 -> -0009
               10 -> -0010  11,12 -> -0011  13,14 -> -0012  15 -> -0013
               16 -> -0014  17,18 -> -0015  19,20 -> -0016
    21       lamina final A4 apaisada

PAGINAS ROTADAS: las laminas 1 a 3 tienen rotation=270. La skill v1.6 ya
resuelve el caso (text_rotate = original_rotation, con la matriz de
derotacion), de modo que NO se hardcodea 270. Cierre obligatorio: verificar por
render PNG que el ID y el texto se leen completos y de izquierda a derecha,
porque en paginas rotadas page.annots() devuelve 0 aunque la anotacion exista.

El color del recuadro transmite la severidad (CRITICAL rojo, MAYOR naranja,
MENOR amarillo, NOTE azul); el texto NO lleva etiqueta de criticidad.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

# --- Fast-save guard -------------------------------------------------------
# run_comentarios() guarda con garbage=4, deflate=True. Este PDF son 22 laminas
# A1 con 430.141 vectores y 13,9 MB: esa recompresion total no converge y el
# proceso se cuelga. Se fuerza un guardado equivalente y valido
# (garbage=1, deflate=False): mismas anotaciones, sin recomprimir streams.
import fitz  # noqa: E402
_orig_save = fitz.Document.save


def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)


fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_C_Piping_Layout.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-004_C_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 70", "25007-0070",
        "P22-DWG-09-005-004_Piping Layout_Rev.C-004.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    # ---------------- las cuatro paginas del documento ----------------
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-01: this cover declares the document as\n"
            "'Page 1 of 4' and the file contains 22\n"
            "pages. Pages 5 to 21 are eleven shop\n"
            "fabrication drawings under BW Water\n"
            "numbering 25007-ME-PI-0901-0006 to -0016,\n"
            "with their own revision index and a FOR\n"
            "CONSTRUCTION stamp, carrying no ADASA\n"
            "document code and absent from the Submittal\n"
            "Form. Either remove that set from\n"
            "P22-DWG-09-005-004 and submit it as a\n"
            "separate deliverable with its own ADASA\n"
            "code and revision index, or extend this\n"
            "cover and the Submittal Form to declare it.\n"
            "In both cases state the review status\n"
            "expected from ADASA for those sheets."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: two separate enclosures are\n"
            "labelled LCP on this sheet, one outside the\n"
            "container and one in the external CIP area,\n"
            "and neither carries an equipment tag while\n"
            "the process equipment does. State whether\n"
            "the module carries one or two local control\n"
            "panels, tag each enclosure consistently\n"
            "with the approved Local Control Panel\n"
            "datasheet and the Single Line Diagram, and\n"
            "show the routing between each panel and the\n"
            "equipment it serves, or identify by code\n"
            "and revision the drawing where that routing\n"
            "is defined. Outstanding since Transmittal\n"
            "N7."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 2,
        "text": (
            "OBS-03: tie-in elevations are dimensioned\n"
            "for the super duplex and drain lines only.\n"
            "Add a tie-in schedule listing, for every\n"
            "battery-limit connection, the line tag,\n"
            "nominal diameter, connection type and the\n"
            "elevation referred to a datum declared on\n"
            "the drawing, covering the permeate and CIP\n"
            "supply and return lines as well as the\n"
            "lines already dimensioned, and identify the\n"
            "Tie-In Point Layout drawing by code and\n"
            "revision in the reference list."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 3,
        "text": (
            "NOTE-01: the antiscalant and CIP\n"
            "battery-limit terminations are now resolved\n"
            "on the geometry, which closes the point\n"
            "carried from Transmittal N15. Annotate the\n"
            "flange class against those terminations at\n"
            "IFC Rev 0, consistent with the approved\n"
            "Line List P22-LI-09-009-003."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 3,
        "offset_y": 260,
        "text": (
            "NOTE-02: confirm that the anchorage of the\n"
            "container and of the external CIP and\n"
            "dosing area, with the corresponding loads\n"
            "and bolt layout for the ADASA concrete\n"
            "bases, is covered by the seismic\n"
            "calculation report and the civil\n"
            "requirements drawing, stating the code and\n"
            "issue date of both. The holding-down bolts\n"
            "for the externally mounted equipment are to\n"
            "be defined and supplied by the equipment\n"
            "manufacturer. Tracked as a cross-document\n"
            "deliverable, with no modification to this\n"
            "drawing."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": None,
        "page_fallback": 2,
        "offset_y": 260,
        "text": (
            "NOTE-03: the service description used for\n"
            "DA-SSD-DN65-09-009 on the callouts differs\n"
            "from the approved Line List. Use the line\n"
            "descriptions of the approved Line List, and\n"
            "show where DA-SSD-DN65-09-009 ends and\n"
            "DA-PVC-DN65-09-016 begins, so that the\n"
            "boundary between the super duplex line and\n"
            "the PVC discharge line is unambiguous."
        ),
    },
    # ---------------- conjunto de taller, paginas 5 a 21 ----------------
    {
        "id": "OBS-04",
        "fill": CRITICAL,
        "search": None,
        "page_fallback": 10,
        "text": (
            "OBS-04: the half-inch instrument tappings\n"
            "on this and six further sheets are resolved\n"
            "with ANSI 150# threaded half couplings in\n"
            "ASTM A182 Gr. F304 and F316L, on lines that\n"
            "the approved Line List rates at 60 to 90\n"
            "barG design and 90 to 135 barG hydrotest,\n"
            "in brine of 45,000 to 55,000 ppm chloride.\n"
            "The Technical Specification\n"
            "(P22-ET-09-000-001-0), Section 5.2.2 - High\n"
            "Pressure Piping, requires super duplex ASTM\n"
            "A182 F53 UNS S32750 with PREN above 40 and\n"
            "Class 900 rating. Replace them with welded\n"
            "super duplex branch fittings per MSS SP 97,\n"
            "as already used on other half-inch branches\n"
            "of these same sheets, confirm in writing\n"
            "that no austenitic, threaded or Class 150\n"
            "pressure-retaining component remains in the\n"
            "super duplex system, and state whether any\n"
            "of these branches has already been\n"
            "fabricated under the FOR CONSTRUCTION stamp."
        ),
    },
    {
        "id": "OBS-05",
        "fill": CRITICAL,
        "search": None,
        "page_fallback": 5,
        "text": (
            "OBS-05: the boundary between the super\n"
            "duplex system and the PVC system sits at an\n"
            "ANSI 150# flanged joint next to a single\n"
            "motorised butterfly valve, with no\n"
            "specification break symbol and no line\n"
            "number split. This spool and those on the\n"
            "neighbouring sheets incorporate PVC SCH 80\n"
            "pipe while the approved Line List\n"
            "classifies these lines as super duplex at\n"
            "80 to 90 barG design and 120 to 135 barG\n"
            "hydrotest, and rates the PVC lines at 5\n"
            "barG design and 7.5 barG hydrotest. Show\n"
            "the specification break explicitly, split\n"
            "the line numbers at that joint so the PVC\n"
            "segments carry their own line number,\n"
            "piping class, design pressure and hydrotest\n"
            "pressure, issue the corresponding addition\n"
            "to the Line List, and state how the PVC\n"
            "side is protected from the high-pressure\n"
            "side with the motorised valve closed."
        ),
    },
    {
        "id": "OBS-06",
        "fill": MENOR,
        "search": None,
        "page_fallback": 4,
        "text": (
            "OBS-06: the bills of materials designate\n"
            "the super duplex pipe as SCH80. Change the\n"
            "schedule designation to SCH 80S per ASME\n"
            "B36.19M on all super duplex pipe, on this\n"
            "and every other spool sheet, consistent\n"
            "with the Technical Specification\n"
            "(P22-ET-09-000-001-0), Section 5.2.2 - High\n"
            "Pressure Piping, and with the approved Line\n"
            "List. No dimensional change is implied for\n"
            "the NPS 1/2 to NPS 4 range."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
