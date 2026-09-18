#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_fat_modulo.py
Anota el Factory Acceptance Test Procedure Rev A del modulo (P22-BA-09-000-017),
submittal 25007-0095 (ENTREGA 95, recibido el 18-Sep-2026). Veredicto del TM N40:
Code 3 - To be revised, re-emitir como Rev B.

len(COMENTARIOS) = 12: diez OBS y dos NOTE, espejo 1:1 del bloque Action de la
subseccion 2.1 ("OBS-01 to OBS-10, NOTE-01 and NOTE-02 on the annotated PDF").

IDs SECUENCIALES POR ORDEN DE APARICION: los asigna _ajustar_cajas.asignar_ids_secuenciales
por (pagina, y del ancla) antes de anotar; el texto lleva el marcador {ID}. Reparto
resultante (paginas 1-based):
    2  DOC NO: PROV-PROC-FAT-001        -> OBS-01 (dos numeros de documento)
    4  1. PURPOSE                       -> OBS-02 (no es procedimiento detallado)
    4  2. SCOPE                         -> OBS-03 (responsabilidades)
    5  4. FAT REQUIREMENTS              -> OBS-04 (hidrostaticas como prerrequisito)
    5  Calibration Certificates         -> NOTE-01 (instrumentos de prueba)
    6  5.2 Full Dimensional             -> OBS-05 (documentos sin codigo, tolerancias)
    6  5.3 Dry Functional Testing       -> OBS-06 (secuencia y equipos)
    7  5.3.2 Acceptance Criteria        -> NOTE-02 (alcance en seco correcto)
    7  5.4 Control System Testing       -> OBS-07 (loop checks, simulacion, fallos)
    8  5.6 SEC                          -> OBS-08 (componentes y certificados)
    8  5.7 UT                           -> OBS-09 (procedimiento y plano de puntos)
    9  5.8 Certificate                  -> OBS-10 (Acta FAT vs Release for Dispatch)

Formato de cada cuadro (historial N37 a N39, ajustado el 18-Sep a pedido del usuario):
"ID: que esta mal. Correct: que hacer." Sin etiqueta de severidad (la da el color), sin
titulo, sin prosa de contexto. El texto se escribe en una linea y el helper lo envuelve a
44 caracteres. Tras anotar, ajustar_cajas() redimensiona cada caja al texto real y la
lleva al espacio libre de la pagina (junto a las listas de vinetas o al pie).
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, add_pdf_comments  # noqa: E402
from _ajustar_cajas import asignar_ids_secuenciales, ajustar_cajas  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-017_A_FAT_Procedure.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-017_A_FAT_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 95",
        "P22-BA-09-000-017_A Factory Acceptance Test Procedure.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MENOR,
        "search": "PROV-PROC-FAT-001", "page_fallback": 1, "page_min": 1,
        "text": "{ID}: two document numbers, P22-BA-09-000-017 on the cover and "
                "PROV-PROC-FAT-001 here; Section 3 cites no document by code and "
                "revision; the index reads REFERENT. Correct: ADASA code on every "
                "page, internal number once, every reference by code and revision.",
    },
    {
        "serie": "OBS", "fill": CRITICAL,
        "search": "PURPOSE", "page_fallback": 3, "page_min": 3,
        "text": "{ID}: not a detailed procedure. It restates ITP rows 7.2 to 7.9 as "
                "headings, with no test step, no acceptance value and none of the nine "
                "record forms of Section 8; ITP rows 7.3 to 7.5 refer those to this "
                "procedure (ET 8.1; ITP row 7.1, ADASA Hold Point). Correct: Rev B "
                "with step-by-step test sheets and blank record forms per activity "
                "5.1 to 5.8.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "SCOPE", "page_fallback": 3, "page_min": 3,
        "text": "{ID}: Section 1 promises responsibilities and no section says who "
                "performs, witnesses and signs each activity. Correct: add a "
                "responsibility matrix (BW Water QC, ADASA or its representative, "
                "third-party inspector). ADASA also requests the H or W code of each "
                "ITP row and the Clause 37 notice per activity.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "FAT REQUIREMENTS", "page_fallback": 4, "page_min": 4,
        "text": "{ID}: the hydrostatic tests are not a prerequisite. ET 8.1 requires "
                "the LP and HP tests (ITP 5.1, 5.2) completed and approved before the "
                "FAT opens. Correct: add the approved test reports, RO vessel included, "
                "to Section 4.",
    },
    {
        "serie": "NOTE", "fill": NOTE,
        "search": "Calibration Certificates", "page_fallback": 4, "page_min": 4,
        "text": "{ID}: the test instruments are not identified, although 5.2.1 requires "
                "calibrated equipment. State model, serial number and calibration "
                "validity of each instrument in Rev B.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "Full Dimensional Verification", "page_fallback": 5, "page_min": 5,
        "text": "{ID}: 5.1 and 5.2 cite document types without code or revision, state "
                "no tolerance and do not name the tie-in points; the checklists of ITP "
                "7.2 and 7.3 are not attached. Correct: cite P&ID Rev 0, GA of the skid "
                "Rev 0, Equipment Layout Rev D and Tie-In Point Layout Rev 0; state the "
                "tolerances; attach both checklists.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "Dry Functional Testing", "page_fallback": 5, "page_min": 5,
        "text": "{ID}: 5.3.1 refers to an approved FAT sequence that is not in the "
                "document and lists no equipment (ET 8.1; ITP 7.4). Correct: list every "
                "pump and valve by tag with its test step and criterion: free and correct "
                "rotation, valve actuation, limit switches.",
    },
    {
        "serie": "NOTE", "fill": NOTE,
        "search": "Equipment operates according to approved", "page_fallback": 6, "page_min": 6,
        "text": "{ID}: the dry test scope is correct (ET 8.1). Pump under load, RO "
                "performance and site interlocks belong to commissioning and the "
                "Performance Tests (ET 9 and 10.2). State this in Rev B.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "Control System Testing", "page_fallback": 6, "page_min": 6,
        "text": "{ID}: 5.4 has no loop check list, no forced-signal or simulator method, "
                "no fault scenarios and no HMI review to ISA 101; the four relay signals "
                "to the plant PLC (I/O List Rev 6) are not tested (ET 8.1; ITP 7.5). "
                "Correct: add the loop checks of the I/O List Rev 6 and the scenarios "
                "with the expected response per Control Philosophy Rev 1 and Alarm and "
                "Interlock List Rev 0; reference P22-PP-09-000-001 for the panel "
                "energisation.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "Chilean Electrical Regulations", "page_fallback": 7, "page_min": 7,
        "text": "{ID}: the SEC verification, a Hold Point under ET 8.1, lists no "
                "component and no certificate. Correct: list breakers, protections, VFDs, "
                "main cabling and panels with the certificate or declaration for each, "
                "plus the panel test record of ITP 6.2.",
    },
    {
        "serie": "OBS", "fill": MENOR,
        "search": "Base Measurement of High-Pressure Pipe Thickness", "page_fallback": 7, "page_min": 7,
        "text": "{ID}: 5.7 names a UT Measurement Plan that is not attached and cites no "
                "procedure. Correct: cite P22-BA-09-000-016 by revision and the "
                "measurement point drawing of ITP 7.8 by code.",
    },
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "FAT Approval Certificate Issuance", "page_fallback": 8, "page_min": 8,
        "text": "{ID}: 5.8 merges the FAT Approval Certificate (ITP 7.9) with the release "
                "for shipment (ITP 8.4; BAE 38 and 39; dossier of 8.3). Correct: separate "
                "them; add the written approval of ADASA or its representative on each "
                "Hold record, and the notice and attendance on each Witness record.",
    },
]

if __name__ == "__main__":
    assert len(COMENTARIOS) == 12, len(COMENTARIOS)
    orden = asignar_ids_secuenciales(PDF_LOCAL, COMENTARIOS)
    print("IDs por orden de aparicion:", orden)
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
    print("Ajuste de cajas:")
    ajustar_cajas(PDF_OUT, COMENTARIOS)
