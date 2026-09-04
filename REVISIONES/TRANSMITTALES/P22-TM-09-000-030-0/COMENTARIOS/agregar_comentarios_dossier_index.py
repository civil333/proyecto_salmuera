#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_dossier_index.py
Anota el Fabrication and Testing Dossier Index Rev A (P22-BA-09-000-013), del
submittal 25007-0069 (E69). Veredicto del TM N30: Code 3 - To be revised.

len(COMENTARIOS) = 10 (OBS-01 a OBS-06 + NOTE-01 a NOTE-04), que es el rango
que cita la subseccion del Dossier Index en la Seccion 2 del transmittal.

El documento tiene solo 2 paginas A4: la 0 es portada y la 1 es el indice
completo, con 27 capitulos en secciones A a E. DIEZ anotaciones no caben en una
sola pagina: el primer intento apilo nueve cajas en la pagina del indice y las
ultimas quedaron fuera del alto de la hoja (y hasta 1725 en una pagina de 842
puntos), invisibles en el PDF emitido. Dos correcciones:

  1. El texto de cada anotacion es la INSTRUCCION y su FUENTE, en cinco a diez
     lineas. El argumento completo vive en la Seccion 2 del transmittal, no
     aqui; repetirlo desborda la hoja y tapa el propio indice que se comenta.
  2. Se reparten: las cuatro que aplican al documento completo van en la
     portada, escalonadas con offset_y; las seis especificas van ancladas al
     capitulo que les toca en el indice.

Los anclajes de busqueda se verificaron contra el PDF y todos devuelven UNA
sola ocurrencia. Cierre obligatorio: render PNG de las dos paginas para
comprobar que las diez cajas caen dentro de la hoja y no tapan texto util.

El color del recuadro transmite la severidad (MAYOR naranja, MENOR amarillo,
NOTE azul); el texto NO lleva etiqueta de criticidad.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-013_A_Dossier_Index.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-013_A_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    # La E69 NO tiene subcarpeta 25007-0069: el PDF cuelga de la raiz.
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 69",
        "P22-BA-09-000-013_A Fabrication and Testing Dossier Index_.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    # --- pagina 0, portada: lo que aplica al documento completo ---
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "OBS-01: add to every line the document\n"
            "number, revision and inclusion status, and\n"
            "cross-reference each chapter to the row of\n"
            "the Inspection and Test Plan\n"
            "(P22-BA-09-000-004) that generates the\n"
            "record. As issued the index cannot serve as\n"
            "the checklist for the review that the\n"
            "Inspection and Testing Base Plan\n"
            "(P22-IT-09-000-001-0) assigns to ADASA at\n"
            "item 7.6."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "offset_y": 190,
        "text": (
            "OBS-02: add a chapter for preparation for\n"
            "dispatch: cleaning and preservation records,\n"
            "packaging and marking records with their\n"
            "checklists and photographic evidence, and\n"
            "the packing list. Required by the Inspection\n"
            "and Test Plan, rows 8.1 and 8.2, and by the\n"
            "Technical Specification\n"
            "(P22-ET-09-000-001-0), Section 7. Those\n"
            "records support the release for dispatch at\n"
            "row 8.4."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "offset_y": 380,
        "text": (
            "OBS-03: add a chapter for the FAT Approval\n"
            "Certificate issued by ADASA. The Technical\n"
            "Specification (P22-ET-09-000-001-0),\n"
            "Section 8, makes both the supplier FAT\n"
            "protocol and that certificate an integral\n"
            "part of the final dossier. The index\n"
            "provides for the procedure and the report\n"
            "only."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 0,
        "offset_y": 540,
        "text": (
            "NOTE-01: the Inspection and Test Plan\n"
            "provides for two indices, a preliminary one\n"
            "at row 7.6 and a final one at row 8.3, the\n"
            "latter a hold point. State which of the two\n"
            "this document is, and keep the same chapter\n"
            "numbering in both."
        ),
    },
    # --- pagina 1, indice: cada una anclada a su capitulo ---
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "B3",
        "page_fallback": 1,
        "text": (
            "NOTE-02: none of the procedures of B3, B4\n"
            "and B6 has been submitted to ADASA. The NDE\n"
            "Plan (P22-BA-09-000-005), Section 2.0,\n"
            "requires them to be reviewed and approved\n"
            "by the client. Submit them before welding\n"
            "starts: records produced under unapproved\n"
            "procedures are not admissible."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MENOR,
        "search": None,
        "page_fallback": 1,
        "offset_y": 370,
        "text": (
            "OBS-04: state in which chapter the RO\n"
            "pressure vessel package is filed:\n"
            "certification to ASME Section X without\n"
            "code stamp and hydrostatic test at 1,800\n"
            "psi x 1.1. Row 2.2 of the Inspection and\n"
            "Test Plan holds that test as a hold point."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": None,
        "page_fallback": 1,
        "offset_y": 465,
        "text": (
            "NOTE-03: identify explicitly in C9, spool\n"
            "by spool, the mill certificates of the\n"
            "super duplex material. Row 2.1 of the\n"
            "Inspection and Test Plan requires\n"
            "verification of PREN above 40 for UNS\n"
            "S32750."
        ),
    },
    {
        "id": "NOTE-04",
        "fill": NOTE,
        "search": None,
        "page_fallback": 1,
        "offset_y": 560,
        "text": (
            "NOTE-04: no chapter for non-conformance\n"
            "reports and weld repair records. Row 7.9 of\n"
            "the Inspection and Test Plan makes their\n"
            "closure a condition for the ADASA approval\n"
            "certificate."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "offset_y": 650,
        "text": (
            "OBS-05: add a chapter for manufacturer\n"
            "certificates and factory test records of\n"
            "the main equipment: pumps, turbochargers,\n"
            "motors, drives, PLC and instruments, per\n"
            "row 2.3. D2 covers only a mechanical FAT\n"
            "report and E2 only electrical certificates,\n"
            "so the sub-vendor records have no location."
        ),
    },
    {
        "id": "OBS-06",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "offset_y": 660,
        "text": (
            "OBS-06: add a chapter for inspection\n"
            "personnel qualifications and test equipment\n"
            "calibration. The NDE Plan, Section 3.0,\n"
            "requires the technician certifications, and\n"
            "row 2.4 lists the PMI calibration\n"
            "certificate. E3 covers process instruments,\n"
            "not inspection equipment."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
