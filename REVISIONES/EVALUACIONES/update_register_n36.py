#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n36.py

Actualiza el Master Deliverable Register con el Transmittal N36
(P22-TM-09-000-036-0), submittals 25007-0082, 25007-0083, 25007-0084 y
25007-0085 (ENTREGAS 82 a 85), recibidas entre el 21 y el 26 de agosto de 2026.

Idempotente: si existe el backup _pre-N36.xlsx, restaura SRC desde ese backup
antes de aplicar. Re-correr el script es seguro.

VEREDICTO GLOBAL: 2 - Approved as noted. Recuento del transmittal: 3 Codigo 1
y 5 Codigo 2 sobre los OCHO documentos dispuestos. Ningun documento vuelve a
revision. Ocho re-revisiones
con veredicto mas una entrega registrada sin codigo, ningun item nuevo.

Filas que se tocan, todas ya existentes en el register:
    #107  UHPRO Structural Design Criteria   P22-CD-09-005-003  (Rev B -> 0, 1 -> 1)
    #40   Piping Layout                      P22-DWG-09-005-004 (Rev C -> D, 2 -> 2)
    #114  3D Model                           P22-DWG-09-005-007 (Rev A -> B, 2 -> 2)
    #83   GA of SWRO System Skid             P22-DWG-09-005-008 (Rev B -> 0, 2 -> 1)
    #53   GA of Antiscalant Dosing Tank      P22-DWG-09-005-015 (Rev B -> C, 3 -> 2)
    #59   Project Schedule                   P22-BA-09-000-001  (Rev A -> B, SIN CODIGO)
    #5    Datasheet of RO HP Feed Pump       P22-ET-09-009-002  (Rev D -> E, 2 -> 1)
    #11   Datasheet of Feed Turbocharger     P22-ET-09-009-007  (Rev D -> E, 2 -> 2)
    #12   Datasheet of Interstage Turbo      P22-ET-09-009-008  (Rev D -> E, 2 -> 2)

EFECTO SOBRE EL TALLY. Tres filas cambian de codigo: el GA del skid sube de
Codigo 2 a Codigo 1, el GA del estanque antiscalante sube de Codigo 3 a Codigo 2
y el datasheet de la bomba sube de Codigo 2 a Codigo 1. Partiendo del cierre del
N35 (60 Codigo 1 / 22 Codigo 2 / 7 Codigo 3 / 0 Codigo 4, cero sin codigo), el
tally esperado tras el N36 es 62 / 21 / 6 / 0. El Summary se recomputa desde el
Master Register y no se hardcodea: contrastar contra ese numero al correr.

REGLA DE ALCANCE del N36. Los nueve documentos responden a comentarios previos,
de modo que cada uno se revisa solo contra la instruccion escrita del transmittal
anterior. La columna de emision del Submittal Form decide el codigo: un documento
sometido para aprobacion reitera la condicion en Codigo 2, y uno emitido para
construccion queda en Codigo 1 o en Codigo 3, porque sobre un Rev 0 el Codigo 2
no tiene mecanismo.

CORRER DESPUES DE ENVIAR el transmittal, no antes.

El bloque ITEMS BY SECTION arrastra un descuadre heredado de un entregado de mas.
El updater lo reporta en cada corrida y no lo agranda.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N36.xlsx")

TM = "N36"
TM_DATE = "26-Aug-2026"

MR_UPDATES = {
    "P22-CD-09-005-003": dict(
        rev="0", delivery="E82", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered for construction (E82, 21-Aug-2026, submittal 25007-0082). "
            "Code 1 - Approved (TM N36). Rev B was already Code 1 at TM N25 with the "
            "action declared as none, so the Rev 0 was reviewed as a differential "
            "against what had been approved. Every seismic parameter, load combination "
            "table, material grade, wind figure and lifting criterion is unchanged; "
            "nothing was removed and nothing contradicts the approved revision. Two of "
            "the three editorial items folded into the TM N25 note remain open, the "
            "cover date against the body date and the duplicate table number, and this "
            "revision also drops the consolidated comment sheet that Rev B carried. All "
            "three are documentary housekeeping and none was a condition of approval, "
            "so they do not degrade the document; they are stated in the transmittal "
            "text for tidying at the next natural issue. No annotated PDF (Code 1)."),
    ),
    "P22-DWG-09-005-004": dict(
        rev="D", delivery="E83", tm=TM, verdict="2-AN",
        action=(
            "Rev D delivered for approval (E83, 21-Aug-2026, submittal 25007-0083). "
            "Code 2 - Approved as noted (TM N36). Rev D removes the eleven shop "
            "fabrication drawings that Rev C carried across seventeen pages, and adds "
            "the tie-in schedule. The three conditions of the TM N30 Code 2 are "
            "reiterated because the revision was submitted for approval and they fall "
            "due at Rev 0: the schedule covers none of the seven CIP lines labelled on "
            "the same sheet and its five elevations state no datum, the notes block of "
            "all three sheets being empty; the flange class is absent at the antiscalant "
            "and CIP terminations; and the sheet still shows two enclosures labelled LCP "
            "with no tag on either. The comment sheet transcribes one of the three "
            "conditions. Second cycle with these points open. Annotated PDF issued."),
    ),
    "P22-DWG-09-005-007": dict(
        rev="B", delivery="E83", tm=TM, verdict="2-AN",
        action=(
            "Rev B delivered for approval (E83, 21-Aug-2026, submittal 25007-0083). "
            "Code 2 - Approved as noted (TM N36). Reviewed against the object property "
            "database. Most of the TM N30 reconciliation is done: BH-009-002 corrected, "
            "all seven valve tags with a trailing question mark clean where only one had "
            "been named, DPS-09-002 to DPS-09-001, BOI-09-006 to BOI-09-001-6, and line "
            "numbers 09-042, 09-044 and 09-026 matching the approved Line List. Three "
            "points reiterated at Rev 0: the publication properties still declare the "
            "title V16 TALTAL and carry no revision index; line number 09-001 is still "
            "used by both DA-PVC-DN100-09-001 and RD-PVC-DN15-09-001 and the announced "
            "rename was not made; and line 09-015 has three objects left at DN100. The "
            "comment sheet states that fifty-seven object tags were corrected: those "
            "objects are pipe supports, none was touched and there are now seventy-two. "
            "The re-issue of the Equipment List and of the Valve List that BW Water "
            "undertook in writing is tracked in Section 3. Navisworks file: no annotated "
            "PDF is possible, exception declared in Section 4."),
    ),
    "P22-DWG-09-005-008": dict(
        rev="0", delivery="E84", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered for construction (E84, 24-Aug-2026, submittal 25007-0084). "
            "Code 1 - Approved (TM N36). It is the only document of these submittals "
            "issued for construction, so the conditions of its TM N31 Code 2 fell due "
            "at this issue. That Code 2 was one action, correct three document "
            "references in the notes block, and ONLY ONE of the three was corrected: "
            "note 7 now cites the approved Line List on both sheets; note 6 was "
            "corrected on Sheet 2 and still reads Rev D on Sheet 1, so the same drawing "
            "refers the same instrument function matrix to two revisions; and note 8 is "
            "unchanged on both sheets, citing P22-ET-09-006-01, which is not a valid "
            "code in the project numbering, on the note that governs nominal wall "
            "thickness per pipeline. The reply given to note 8 is refuted by the annex "
            "BW Water attached to support it, which writes the code with three "
            "sequential digits. CODE 1 AND NOT 3 because the drawing is issued for "
            "construction and ADASA does not hold it: both documents referred to remain "
            "identifiable and neither error changes a dimension, a material, a rating "
            "or a quantity. The two corrections stand and are stated in full in the "
            "transmittal, with the correct code P22-ET-09-006-001 written out so it "
            "holds on the record whether or not the drawing is re-issued. No annotated "
            "PDF (Code 1); the one generated was withdrawn to "
            "ENTREGAS_BWWATER/ENTREGA 84/_skid_fuera_de_anotacion/."),
    ),
    "P22-DWG-09-005-015": dict(
        rev="C", delivery="E84", tm=TM, verdict="2-AN",
        action=(
            "Rev C delivered for approval (E84, 24-Aug-2026, submittal 25007-0084). "
            "Code 2 - Approved as noted (TM N36), up from Code 3 at TM N26. The "
            "substance of that Code 3 is closed: note 16 states the seismic reaction "
            "forces, note 15 the centre of gravity, a new Detail 4 gives the M12 bolt "
            "with its load and a minimum embedment consistent with the three anchor lugs "
            "of Detail 3, note 8 states the effective working volume and the title block "
            "carries the equipment tag TK-09-002. Two minor items remain on the detail "
            "that was added, incorporable at Rev 0: the anchor hole is dimensioned 14 mm "
            "and half an inch against an M12 bolt, and the level marking row carries its "
            "location but no size and no elevation. Note 16 refers the forces to a "
            "calculation report without stating its code and revision, and that report "
            "is still unendorsed; that dependency is tracked in Section 3 and does not "
            "degrade this drawing. Annotated PDF issued."),
    ),
    # El Project Schedule Rev B se RETIRO del Transmittal N36 (decision del usuario,
    # 26-Ago-2026): su seguimiento se lleva por la reunion semanal de coordinacion.
    # Se registra la ENTREGA, que si ocurrio, y se conservan el TM y el veredicto del
    # N20: este transmittal no le asigno codigo. Por eso tampoco entra al Revision
    # History, donde cada fila es un ciclo de revision con veredicto.
    "P22-BA-09-000-001": dict(
        rev="B", delivery="E84", tm="N20", verdict="2-AN",
        action=(
            "Rev B delivered for approval (E84, 24-Aug-2026, submittal 25007-0084). "
            "NOT DISPOSED at TM N36: the programme is followed through the weekly "
            "project coordination and the transmittal states so without assigning a "
            "response code. The two TM N20 observations remain open and were verified "
            "on this revision: no occurrence of ASME, stamp, certification or waiver in "
            "the fourteen pages, and no occurrence of hydrostatic, pressure test or leak "
            "test, with the pressure vessels already manufactured and received in "
            "Penang at one hundred per cent. The revision does respect the third clause "
            "of that action: the baseline column keeps its four anchor dates and the "
            "adoption of 09-Jun-2026 is not re-opened. Evidence retained in "
            "ENTREGAS_BWWATER/ENTREGA 84/_cronograma_fuera_de_transmittal/."),
    ),
    "P22-ET-09-009-002": dict(
        rev="E", delivery="E85", tm=TM, verdict="1-Approved",
        action=(
            "Rev E delivered for approval (E85, 26-Aug-2026, submittal 25007-0085). "
            "Code 1 - Approved (TM N36), up from Code 2 at TM N11. The single note open "
            "since TM N11 is closed in both of its clauses: the motor manufacturer now "
            "reads the same in the equipment data block, in the pump data section and on "
            "the outline drawing, the earlier alternative wording is gone, and the "
            "declaration of a concrete manufacturer on a revision issued after the "
            "purchase order answers the request to confirm it once procurement was "
            "complete. The outline drawing labels its process connections consistently "
            "with the coupling datasheet accepted at TM N11. No annotated PDF (Code 1). ADASA further requires this datasheet to be ISSUED AT REV 0 FOR CONSTRUCTION before the Factory Acceptance Test opens on 7 September 2026: the pump is purchased, built and programmed for installation inside the container within days, and its datasheet cannot keep circulating as an approval revision."),
    ),
    "P22-ET-09-009-007": dict(
        rev="E", delivery="E85", tm=TM, verdict="2-AN",
        action=(
            "Rev E delivered for approval (E85, 26-Aug-2026, submittal 25007-0085). "
            "Code 2 - Approved as noted (TM N36). The single note open since TM N11 "
            "closes only in half: it asked for the outline drawing label to be updated "
            "to Style S in order to eliminate the discrepancy with STYLE 77, a coupling "
            "of a different manufacturer and a different working pressure. Rev E adds "
            "PIEDMONT STYLE S to all four connection callouts and leaves STYLE 77 in "
            "place on all four, so each connection names two coupling models at once. "
            "The datasheet body specifies the process connections at Coupling 1800 psi, "
            "which is the Style S rating and the accepted one. Delete STYLE 77 at Rev 0. "
            "Annotated PDF issued. Delete STYLE 77 and ISSUE AT REV 0 FOR CONSTRUCTION before the Factory Acceptance Test opens on 7 September 2026. No intermediate approval revision is to be issued: the equipment is built and due at the workshop."),
    ),
    "P22-ET-09-009-008": dict(
        rev="E", delivery="E85", tm=TM, verdict="2-AN",
        action=(
            "Rev E delivered for approval (E85, 26-Aug-2026, submittal 25007-0085). "
            "Code 2 - Approved as noted (TM N36). Identical condition to the Feed "
            "Turbocharger and unchanged in form: PIEDMONT STYLE S was added to all four "
            "connection callouts and STYLE 77 was not removed from any of them, while "
            "the datasheet body specifies the process connections at Coupling 1800 psi. "
            "Delete STYLE 77 at Rev 0. Annotated PDF issued. Delete STYLE 77 and ISSUE AT REV 0 FOR CONSTRUCTION before the Factory Acceptance Test opens on 7 September 2026. No intermediate approval revision is to be issued: the equipment is built and due at the workshop."),
    ),
}

RH_NEW = [
    (None, "UHPRO Structural Design Criteria", "P22-CD-09-005-003", "0", "E82",
     "25007-0082", "1-Approved",
     "Issued for construction. Reviewed as a differential against the Rev B approved at "
     "TM N25, whose action was declared as none. Body unchanged in full. Two editorial "
     "items and the lost comment sheet are housekeeping and were never a condition."),
    (None, "Piping Layout", "P22-DWG-09-005-004", "D", "E83",
     "25007-0083", "2-AN",
     "Submitted for approval. The eleven shop drawings are out and the tie-in schedule "
     "is in, but it covers no CIP line and its elevations state no datum. Flange class "
     "and the two LCP enclosures still open. Second cycle."),
    (None, "3D Model", "P22-DWG-09-005-007", "B", "E83",
     "25007-0083", "2-AN",
     "Submitted for approval. Seven valve tags cleaned where one was named, three line "
     "numbers reconciled. Open: file properties still titled V16 TALTAL without revision "
     "index, line 09-001 collision, three objects on 09-015. The fifty-seven untagged "
     "supports were declared corrected and are now seventy-two."),
    (None, "GA of SWRO System Skid", "P22-DWG-09-005-008", "0", "E84",
     "25007-0084", "1-Approved",
     "Issued for construction, so the three references of the TM N31 Code 2 fell due, "
     "and only one was corrected. Note 8 still cites a code that does not exist and the "
     "annex submitted to defend it refutes the reply. Code 1 and not 3 because both "
     "documents remain identifiable and neither error changes the drawing content; the "
     "two corrections stand on the record."),
    (None, "GA of Antiscalant Dosing Tank", "P22-DWG-09-005-015", "C", "E84",
     "25007-0084", "2-AN",
     "Recovers from Code 3. Seismic reactions, centre of gravity, a new bolting detail, "
     "the effective working volume and the equipment tag all delivered. Residual: the "
     "anchor hole dual dimension against the M12 bolt and the level mark elevation."),
    (None, "Datasheet of RO HP Feed Pump", "P22-ET-09-009-002", "E", "E85",
     "25007-0085", "1-Approved",
     "The motor manufacturer reads the same in both data blocks and on the outline "
     "drawing, and the alternative wording is gone, which also answers the confirmation "
     "once procurement was complete."),
    (None, "Datasheet of Feed Turbocharger", "P22-ET-09-009-007", "E", "E85",
     "25007-0085", "2-AN",
     "PIEDMONT STYLE S added to the four connection callouts and STYLE 77 not removed "
     "from any, so each connection names two coupling models. The body specifies "
     "Coupling 1800 psi, the Style S rating."),
    (None, "Datasheet of Interstage Turbocharger", "P22-ET-09-009-008", "E", "E85",
     "25007-0085", "2-AN",
     "Identical condition to the Feed Turbocharger: Style S added, STYLE 77 kept on all "
     "four callouts."),
]


def style_row(ws, dst_row, ref_row, ncols):
    for c in range(1, ncols + 1):
        s = ws.cell(ref_row, c)
        d = ws.cell(dst_row, c)
        d._style = copy(s._style)


def main():
    if os.path.exists(BAK):
        shutil.copyfile(BAK, SRC)
        print(f"Restaurado SRC desde baseline limpio: {BAK}")
    else:
        shutil.copyfile(SRC, BAK)
        print(f"Baseline creado: {BAK}")

    wb = openpyxl.load_workbook(SRC)
    mr = wb["Master Register"]
    rh = wb["Revision History"]
    sm = wb["Summary"]

    ncols_mr = mr.max_column
    hdr = {mr.cell(1, c).value: c for c in range(1, ncols_mr + 1)}
    C_NUM = hdr["#"]; C_CODE = hdr["Code / ET Reference"]
    C_REV = hdr["Rev"]; C_DEL = hdr["Delivery"]; C_TM = hdr["TM"]
    C_VER = hdr["Verdict"]; C_STA = hdr["Status"]; C_ACT = hdr["Action Required"]

    # 1) updates (5 re-revisiones)
    seen = set()
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code in MR_UPDATES:
            u = MR_UPDATES[code]
            mr.cell(r, C_REV).value = u["rev"]
            mr.cell(r, C_DEL).value = u["delivery"]
            mr.cell(r, C_TM).value = u["tm"]
            mr.cell(r, C_VER).value = u["verdict"]
            mr.cell(r, C_STA).value = "Delivered"
            mr.cell(r, C_ACT).value = u["action"]
            seen.add(code)
            print(f"  MR update row {r}: {code} -> {u['verdict']} / {u['tm']} (Rev {u['rev']})")
    missing = set(MR_UPDATES) - seen
    if missing:
        raise SystemExit(f"ERROR: codigos N36 no encontrados en Master Register: {missing}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 2) Revision History (5 filas nuevas)
    rcols = rh.max_column
    rhh = {rh.cell(1, c).value: c for c in range(1, rcols + 1)}
    prior = collections.Counter(); rh_last = 1
    for r in range(2, rh.max_row + 1):
        cd = rh.cell(r, rhh["Code / ET Reference"]).value
        if cd:
            prior[str(cd).strip()] += 1; rh_last = r
    for i, row in enumerate(RH_NEW, start=1):
        dst = rh_last + i
        _num, doc, code, rev, dele, sub, ver, keyobs = row
        num = reg_num.get(code, "")
        cycle = prior[code] + 1; prior[code] += 1
        style_row(rh, dst, rh_last, rcols)
        rh.cell(dst, rhh["#"]).value = num
        rh.cell(dst, rhh["Document"]).value = doc
        rh.cell(dst, rhh["Code / ET Reference"]).value = code
        rh.cell(dst, rhh["Rev"]).value = rev
        rh.cell(dst, rhh["Delivery"]).value = dele
        rh.cell(dst, rhh["Submittal"]).value = sub
        rh.cell(dst, rhh["TM"]).value = TM
        rh.cell(dst, rhh["TM Date"]).value = TM_DATE
        rh.cell(dst, rhh["Verdict"]).value = ver
        rh.cell(dst, rhh["Cycle"]).value = cycle
        rh.cell(dst, rhh["Key Observations"]).value = keyobs
        print(f"  RH new row {dst}: #{num} {code} cycle {cycle} -> {ver}")

    # 3) Summary: recomputar total/delivered + verdicts desde MR
    stat = collections.Counter(); vd = collections.Counter(); total = 0
    for r in range(2, mr.max_row + 1):
        code = mr.cell(r, C_CODE).value
        if code and str(code).strip():
            total += 1
            su = str(mr.cell(r, C_STA).value or "").strip().upper()
            stat[su] += 1
            if su == "DELIVERED":
                vd[str(mr.cell(r, C_VER).value or "").strip()] += 1
    delivered = stat.get("DELIVERED", 0)
    not_delivered = stat.get("NOT DELIVERED", 0)
    partial = stat.get("PARTIAL", 0)
    print(f"  Summary recompute: total={total} delivered={delivered} "
          f"not_delivered={not_delivered} partial={partial} verdicts={dict(vd)}")

    sm["B4"].value = total
    sm["B5"].value = delivered
    sm["B7"].value = partial
    sm["B8"].value = not_delivered
    sm["B9"].value = "36 (N1 through N36 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "85 (E1 through E85; the submittal series has no missing numbers)"
    sm["B12"].value = "26-Aug-2026 (E85)"
    sm["B13"].value = "26-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 4) ITEMS BY SECTION: el N36 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N36 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    # El scratchpad es por equipo. En macOS se usa el temporal del sistema;
    # lo que importa es construir FUERA del volumen de red y verificar el zip
    # antes de copiar al destino, porque un guardado directo sobre SMB puede
    # dejar el .xlsx a medias.
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n36_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n36_build.xlsx")
    wb.save(tmp)
    if zipfile.ZipFile(tmp).testzip() is not None:
        raise SystemExit("ERROR: el build en scratchpad salio corrupto.")
    openpyxl.load_workbook(tmp).close()
    print(f"Build verificado en scratchpad: {tmp}")
    for intento in range(1, 6):
        shutil.copyfile(tmp, dst)
        try:
            if zipfile.ZipFile(dst).testzip() is None:
                openpyxl.load_workbook(dst).close()
                print(f"Guardado y verificado en destino (intento {intento}): {dst}")
                return
        except Exception as e:
            print(f"  intento {intento}: destino aun corrupto ({e}); recopiando...")
    raise SystemExit(f"ERROR: no se pudo dejar copia integra. Build en {tmp}.")


if __name__ == "__main__":
    main()
