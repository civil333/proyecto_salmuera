#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_plc_lcp_fat_procedure_revB.py
Anota el PLC/LCP FAT Procedure - Hardware Rev B (P22-PP-09-000-001) del submittal
25007-0088 (ENTREGA 88). Veredicto del TM N37: Code 3 - To be revised.
Es el documento que fija el codigo del transmittal.

len(COMENTARIOS) = 7, espejo 1:1 del bloque Action de la subseccion 2.7
("OBS-01 to OBS-05 and NOTE-01 to NOTE-02 on the annotated PDF").

🔴 DOCUMENTO FOTOGRAFIADO. Las paginas 2 a 16 son capturas CamScanner de un ejemplar
impreso y llenado a mano: once de las dieciseis devuelven 10 caracteres, que son la
marca de agua. La busqueda de texto NO sirve para anclar, de modo que todos los
comentarios van con search=None y page_fallback fijo, y el resultado SE VERIFICA POR
RENDER PNG, no por page.annots() ni por get_text().

ALCANCE. Re-emision que responde al TM N27, subseccion 2.5, Code 2, con cinco puntos.
  OBS-01 del N27, codigos y revision del esquematico ANTES de testificar
                                                    -> NO CERRADO y agravado -> OBS-03
  OBS-02 del N27, TAG, numero de documento, rotulo de rele
                                                    -> NO CERRADO en el numero -> NOTE-01
  OBS-03 del N27, dos criterios de aceptacion       -> CIERRE PARCIAL (la mitad quedo
                                                       superada por el RFI-002)
  NOTE-01 del N27, cobertura completa               -> CERRADO. No se anota.
  NOTE-02 del N27, visado RTD retenido              -> NO RESPETADO (dentro de OBS-01)

POR QUE CODE 3 Y NO CODE 2 REITERADO. La regla que reserva el Code 2 reiterado para
las emisiones sometidas a aprobacion supone que la condicion vence al emitir Rev 0.
Aqui el TM N27 amarro la condicion a un hito distinto y anterior, "before witnessing",
y ese hito ocurrio: el ensayo corrio del 3 al 5 de agosto sin incorporarlas.

🔴 EL ENCUADRE DEL AVISO, que hay que respetar. La leyenda del propio ITP aprobado
define la W como inspeccion que "requires notification" pero que "is performed as
scheduled, and even if the client or 3rd party is not present". BW Water PODIA
ejecutar el ensayo en su fecha. Lo que no podia era NO AVISAR. Reclamar por la
ejecucion es refutable con el propio ITP; reclamar por el aviso no lo es.

VERIFICADO POR RENDER PROPIO, no tomado del analisis interno:
  - p9: modulo -A2, canales 1 a 4 (DITB1 terminales 4, 6, 8 y 10), TAG XT001, XA002,
    XT002 y XT003, los cuatro visados como ensayo funcional.
  - I/O List Rev 6 (mismo lote): filas 13, 14 y 15 —XA002, XT002, XT003— en ROJO Y
    TACHADAS, indice de revision 6; y NO existe fila XT001 para el PLC01.
    Render en _render/IO6_XT002.png.
  - Esquematico Rev B, lamina 35: esos mismos cuatro TAG en las entradas 1 a 4 del
    mismo modulo, rotulados SPARE.
  - p10: salidas, canal 7 del modulo -A4 con el rele KA8 visado como SPARE; el
    esquematico Rev B cablea ahi el comando del calentador de CIP, que es el item 108
    de la I/O List Rev 6.

NO SE ESCRIBE LA FECHA DEL FAT DEL MODULO. La Nota Tecnica P22-NT-09-000-003-0 dejo
en disputa cual ventana gobierna.

Reparto por pagina (indices 0-based, todas escaneadas salvo la 0):
    1    cierre de FAT y punchlist            -> OBS-01, OBS-02
    4    caratula, informacion del proyecto   -> NOTE-01
    5    documentos de referencia y equipos   -> OBS-03, OBS-05
    9    entradas digitales                   -> OBS-04
    11   verificacion de HMI y comunicaciones -> NOTE-02
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 88",
        "P22-PP-09-000-001_B PLC-LCP FAT Procedure - Hardware.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": CRITICAL,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: the test was witnessed and accepted\n"
            "within the supply chain, and ADASA was not\n"
            "notified.\n"
            "This revision is not a procedure. It is the\n"
            "completed record of the hardware test run on 3\n"
            "to 5 August 2026 at the panel builder, submitted\n"
            "for approval twenty-three days later.\n"
            "On this sign-off, the box Witnessed by (Client /\n"
            "Third-Party Inspector) is signed by BW Water\n"
            "personnel, and the box Accepted by (BW Water) is\n"
            "signed by the panel supplier. Neither ADASA nor\n"
            "a third-party inspector took part.\n"
            "Row 6.2 of the Inspection and Test Plan\n"
            "P22-BA-09-000-004 Rev 0, approved at Code 1,\n"
            "assigns ADASA a witness point on the electrical\n"
            "test of panels, and its legend defines that\n"
            "point as requiring notification. Row 7.1 is a\n"
            "hold point on ADASA approval of the detailed\n"
            "test procedure, and this procedure was at\n"
            "Code 2 with conditions to be incorporated\n"
            "before witnessing.\n"
            "ADASA does not dispute that the test could run\n"
            "on its scheduled date: the same legend says so.\n"
            "What was not done was the notification, which\n"
            "Clause 37 of the Special Administrative\n"
            "Conditions also requires in advance.\n"
            "Correct: at Rev C, issue the procedure as a\n"
            "procedure, separate from any record, and give\n"
            "advance notice of every remaining witness and\n"
            "hold point of the Inspection and Test Plan."
        ),
    },
    {
        "id": "OBS-02",
        "fill": CRITICAL,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: eight category A findings are closed by\n"
            "nobody.\n"
            "The punch list defines category A as Must be\n"
            "resolved BEFORE panel dispatch. Ten items are\n"
            "marked A. Lines 9 and 12 carry their dates and\n"
            "read DONE. Lines 1 to 8, all raised by the BW\n"
            "Water engineer under a single bracket, carry\n"
            "target completion date, actual completion date\n"
            "and status blank.\n"
            "The closing block of the punch list, Rectified\n"
            "by, Witnessed by and Accepted by, is empty.\n"
            "The rectification report attached at the end\n"
            "declares the items done and tested with\n"
            "photographs, and it carries no signature, no\n"
            "date and no witness.\n"
            "Six of the eight are signals the approved I/O\n"
            "List has carried since revisions 3 and 4: the\n"
            "incoming breaker status, the power supply\n"
            "status, and the running, fault and speed signals\n"
            "of the high pressure pump drive.\n"
            "Correct: at Rev C, close each category A item\n"
            "with target date, actual date, status and\n"
            "signature, and have the closure witnessed."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 5,
        "text": (
            "OBS-03: the governing documents cited here do\n"
            "not exist.\n"
            "This table lists P22-ET-09-008-001 Rev. 3 and\n"
            "P22-ET-09-008-002 Rev. 5. Neither revision\n"
            "exists. The schematic diagram of this panel is\n"
            "P22-CD-09-008-002, and P22-ET-09-008-001 is the\n"
            "Datasheet of PLC and HMI Panel Component.\n"
            "Transmittal N27 asked for exactly this, and\n"
            "asked for it before witnessing. A row of the\n"
            "test then certifies that this same document set\n"
            "travels inside the panel.\n"
            "The temperature protection tests were also\n"
            "signed off on 3 to 5 August, while Transmittal\n"
            "N27 held that sign-off until the Alarm and\n"
            "Interlock List was reconciled; that list was\n"
            "reconciled when it was issued at Rev 0.\n"
            "Correct: at Rev C, cite the schematic diagram\n"
            "and the I/O List by their codes and by the\n"
            "revisions actually issued."
        ),
    },
    {
        "id": "OBS-05",
        "fill": MENOR,
        "search": None,
        "page_fallback": 5,
        "text": (
            "OBS-05: the test instruments are not identified.\n"
            "Five of the six rows of this table carry no\n"
            "model and no serial number, and none of the six\n"
            "carries a calibration certificate.\n"
            "Safety requirement 3 of this same document\n"
            "requires that all test instruments carry a valid\n"
            "calibration certificate traceable to national\n"
            "standards, and that their details be recorded in\n"
            "this section.\n"
            "Without it the readings signed off in section 8\n"
            "cannot be traced to an instrument.\n"
            "Correct: at Rev C, state model, serial number\n"
            "and calibration certificate for each instrument\n"
            "used."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 9,
        "text": (
            "OBS-04: three documents state three different\n"
            "things about the same terminals.\n"
            "This page signs off channels 1 to 4 of module\n"
            "-A2, terminals DITB1 4, 6, 8 and 10, as\n"
            "functional tests of tags XT001, XA002, XT002 and\n"
            "XT003, under the printed instruction All tags\n"
            "per approved I/O list.\n"
            "The I/O List Rev 6, issued for construction\n"
            "sixteen days later, shows XA002, XT002 and XT003\n"
            "struck through in red as deleted at revision 6,\n"
            "and carries no XT001 row for this panel.\n"
            "The schematic diagram Rev B, three days later\n"
            "again, keeps those same four tags on inputs 1 to\n"
            "4 of the same module and labels them SPARE.\n"
            "The same happens on outputs: channel 7 of module\n"
            "-A4 with relay KA8 is signed off here as spare,\n"
            "and the schematic wires the CIP heater on/off\n"
            "command, item 108 of the I/O List Rev 6, to that\n"
            "same channel and relay.\n"
            "This record cites no I/O List by code or by\n"
            "revision, so ADASA cannot tell which assignment\n"
            "the panel was built to.\n"
            "Correct: at Rev C, reconcile these terminals\n"
            "against the I/O List Rev 6 and the schematic\n"
            "Rev B, and state the code and revision of the\n"
            "list the test is run against."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": None,
        "page_fallback": 4,
        "text": (
            "NOTE-01: the document identifies itself in two\n"
            "ways.\n"
            "The native cover page reads P22-PP-09-000-001,\n"
            "Rev B. This page reads Document Number P22-ET-\n"
            "09-008 - FAT Procedure and Revision Rev. 0 -\n"
            "Issued for FAT.\n"
            "Transmittal N27 raised the document number and\n"
            "it is still open; the relay label, which was\n"
            "raised in the same observation, did close.\n"
            "Correct: at Rev C, carry one document number and\n"
            "one revision index throughout."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 11,
        "text": (
            "NOTE-02: the operator terminal installed is not\n"
            "the one ADASA declared binding.\n"
            "This page signs off the row that verifies HMI1,\n"
            "2711P-T10C21D8S, Allen-Bradley, installed on the\n"
            "inner door.\n"
            "At Transmittal N30 ADASA declared the\n"
            "2711P-T10C22D9P binding, on rows 15 and 18 of\n"
            "the approved datasheet, which require two\n"
            "Ethernet RJ45 ports and 1 GB.\n"
            "The point is recorded here as evidence and is\n"
            "answered on the schematic diagram, where OBS-02\n"
            "of this transmittal asks how BW Water proposes\n"
            "to close the gap."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
