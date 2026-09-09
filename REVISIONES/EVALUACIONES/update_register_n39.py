#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n39.py — aplica el Transmittal N39 al Master Deliverable Register.

TM N39 (P22-TM-09-000-039-0), emitido el 9 de septiembre de 2026, sobre los
submittals 25007-0091 (ENTREGA 91, recibida el viernes 4-Sep) y 25007-0092
(ENTREGA 92, recibida el martes 8-Sep). TRES documentos, los tres re-revisiones.

IDEMPOTENCIA. Si existe el backup _pre-N39.xlsx, restaura SRC desde ese backup
antes de aplicar. Re-correr el script es seguro.

VEREDICTO GLOBAL: 2 — Approved as noted. 1 Codigo 1, 2 Codigo 2, CERO Codigo 3.

Filas que se tocan, todas ya existentes en el register:

  #33   Valve List                            P22-LI-09-005-002   (Rev D -> E,  1 -> 2)
  #53   GA Antiscalant Dosing Tank            P22-DWG-09-005-015  (Rev C -> D,  2 -> 2)
  #116  Radiography Examination Procedure     P22-BA-09-000-015   (Rev C -> 0,  2 -> 1)

  #108  UHPRO Structural Calculation Report   P22-CD-09-005-001   CORRECCION DE REGISTRO

EFECTO SOBRE EL TALLY, declarado ANTES de correr.

Se parte del cierre del TM N38: 68 / 19 / 2 / 0.

  Baja de Codigo 1 a Codigo 2 (uno):
    - Valve List. Venia en Codigo 1 desde el TM N18 sin condicion abierta. La Rev E
      la emitio BW Water por tres cambios que comprometio por escrito, y dos estan
      hechos. El tercero no: la succion de la bomba CIP, linea CP-SS316-DN150-09-022,
      es 316L en la Line List Rev 1 aprobada en Codigo 1 en el N38, y VM-09-065, que
      es la unica valvula DN150 de ese circuito, sigue en PVC.
  Sube de Codigo 2 a Codigo 1 (uno):
    - Radiography Examination Procedure. El determinante del Codigo 2 del N37 cerro:
      el alcance ya declara duplex S32750 en espesores de 6,02 a 8,56 mm con fuente
      de Iridio 192. Lo que queda, el numero de documento propio, es housekeeping y
      por regla del proyecto no degrada por si solo.
  Sin cambio de codigo (uno):
    - GA Antiscalant Dosing Tank. De los dos puntos del N36 cerro el del agujero de
      anclaje, y no cerro la fila LEVEL MARKING, que sigue con guion en SIZE y guion
      en ELEVATION.

  El tally esperado tras el N39 es 68 / 19 / 2 / 0. Uno entra y otro sale en cada
  categoria, de modo que las cifras no se mueven aunque tres filas cambien.

  El Summary se recomputa desde el Master Register y no se hardcodea.

CORRECCION DE REGISTRO, independiente del N39.

El register tiene el Informe de Calculo Estructural en Rev B, entrega E67 y TM N29,
mientras los transmittals N37 y N38 lo declaran emitido en Rev 0 para construccion
desde la E71. La auditoria de emision del 9 de septiembre destapo la discrepancia.
Se corrigen la revision y la entrega.

  EL VEREDICTO NO SE TOCA, y la razon importa. Sobre un Rev 0 solo caben Codigo 1 o
  Codigo 3, y la condicion de este documento, el endoso de un profesional inscrito en
  Chile, no se cumplio al emitir. Por esa regla correponderia Codigo 3. Pero la E71 se
  respondio por correo y sin codigos, de modo que ningun transmittal emitio veredicto
  sobre esa Rev 0: escribirlo aqui seria inventar un codigo que nadie emitio. Queda el
  2-AN heredado del N29 y el hecho se declara en Action Required. El pendiente sigue
  trazado en la Seccion 3 de los transmittals N37, N38 y N39.

  Por lo mismo NO se agrega fila a Revision History por esta correccion: el N39 no
  reviso este documento.

REGLA DE ALCANCE. Ningun item nuevo: los tres son re-revisiones de items ya
entregados. El total de items y el de entregados no se mueven.

🔴 CORRER DESPUES DE ENVIAR el transmittal, no antes.

AVISO. El bloque ITEMS BY SECTION arrastra un descuadre heredado de un entregado de
mas; el updater lo reporta en cada corrida y no lo agranda.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N39.xlsx")

TM = "N39"
TM_DATE = "09-Sep-2026"

# Tally esperado, declarado antes de correr (ver cabecera).
TALLY_ESPERADO = {"1-Approved": 68, "2-AN": 19, "3-To be revised": 2, "4-Rejected": 0}

MR_UPDATES = {
    "P22-LI-09-005-002": dict(
        rev="Rev E", delivery="E91", tm=TM, verdict="2-AN",
        action=("Rev E submitted for approval (E91, 04-Sep-2026, submittal 25007-0091). "
                "Code 2 - Approved as noted (TM N39). The re-issue was undertaken by BW "
                "Water for three changes and two are done: the four valve tags of the 3D "
                "model comment sheet are in, VM-09-131, VM-09-132, VM-09-133 and "
                "VRP-09-001, and all four are on the P&ID Rev 0, with VRP-09-001 as the "
                "pressure regulating valve replacing the orifice plate at CIT-09-004. "
                "VM-09-015 also leaves the list, which aligns it with the approved P&ID. "
                "Open: VM-09-065 is still listed with a PVC body, PVC trim, PVC disc and "
                "EPDM seat on the CIP pump suction line CP-SS316-DN150-09-022, which the "
                "Line List Rev 1 approved at Code 1 in TM N38 carries in 316L stainless "
                "steel. It is the only DN150 valve of that circuit. To be stated at Rev 0 "
                "against the approved Line List, together with the end connection and "
                "rating. Valves are bought against this list. The overpressure and relief "
                "sizing analysis for the second PSV-09-002, removed at Rev D and carried "
                "since TM N14, remains open in Section 3."),
    ),
    "P22-DWG-09-005-015": dict(
        rev="Rev D", delivery="E91", tm=TM, verdict="2-AN",
        action=("Rev D submitted for approval (E91, 04-Sep-2026, submittal 25007-0091). "
                "Code 2 - Approved as noted (TM N39). Of the two points that held the "
                "drawing at Code 2 in TM N36 one closes: the anchor hole is now labelled "
                "14 mm and 35/64 inch, which are the same dimension, and both accept the "
                "M12 bolt of the same detail; at Rev C the pair read 14 mm and half an "
                "inch, which are not. Open: the LEVEL MARKING row of the nozzle "
                "specification table still carries a dash in SIZE and a dash in "
                "ELEVATION, unchanged from Rev C, verified by render, so nothing on the "
                "tank materialises the 0.27 cubic metre working volume of note 8; the "
                "comment sheet answers the point with 'Level mark added with dimensions'. "
                "To be stated at Rev 0, with the elevation corresponding to that volume. "
                "ADASA records that this intermediate approval revision was not required: "
                "TM N36 asked for the issue at Rev 0. The reaction forces of note 16 rest "
                "on the structural calculation report, whose endorsement is tracked "
                "separately and does not modify this drawing."),
    ),
    "P22-BA-09-000-015": dict(
        rev="Rev 0", delivery="E92", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E92, 08-Sep-2026, submittal 25007-0092). "
                "Code 1 - Approved (TM N39). The determinant of the Code 2 of TM N37 "
                "closed: the scope now reads radiographic testing of duplex S32750 in "
                "walls of 6.02 to 8.56 mm with an Iridium 192 source, which is the "
                "material and the range actually radiographed on this module, and from "
                "which the technique, the source size and the image quality indicator all "
                "follow. The two cross-references left by the renumbering are repointed, "
                "clause 11.6 to T-277.2 and clause 19.4 to T-282.1, and the comment sheet "
                "carries one row per comment for the first time. Housekeeping tracked in "
                "Section 3, which does not degrade the code: the cover reads DOC NO: RT "
                "PROV-PROC-RT-001, so the procedure is still not identified by its own "
                "document number, and the document declares no issue status anywhere. "
                "Both to be stated when the file is next touched. Third and last of the "
                "non-destructive testing procedures to reach Rev 0."),
    ),
}

# Correccion de registro, no del N39. Solo revision y entrega; el veredicto se
# mantiene por la razon declarada en la cabecera.
MR_FIXES = {
    "P22-CD-09-005-001": dict(
        rev="Rev 0", delivery="E71",
        action=("REGISTER CORRECTION (09-Sep-2026): this report was issued at Rev 0 for "
                "construction with delivery E71, not at Rev B with E67 as the register "
                "previously recorded. Transmittals N37 and N38 both state the Rev 0. The "
                "verdict is left at the 2-AN inherited from TM N29 because delivery E71 "
                "was answered by e-mail without response codes, so no transmittal has "
                "issued a verdict on the Rev 0. The condition of that Code 2 was not met "
                "on issue: the report went out for construction carrying internal initials "
                "only, and it has yet to be endorsed by a professional engineer registered "
                "in Chile, undertaken in writing three times. It governs the anchorage "
                "figures of the antiscalant tank drawing. Open and overdue, tracked in "
                "Section 3 of TM N39."),
    ),
}

RH_NEW = [
    (None, "Valve List", "P22-LI-09-005-002", "Rev E", "E91", "25007-0091", "2-AN",
     "Submitted for approval. Re-issue undertaken for three changes, two done. The four "
     "valve tags of the 3D model comment sheet are in and all four are on the P&ID Rev 0, "
     "with VRP-09-001 replacing the orifice plate at CIT-09-004; VM-09-015 leaves the "
     "list. Open: VM-09-065 still in PVC on the CIP pump suction line, which the Line List "
     "Rev 1 approved at TM N38 carries in 316L. Only DN150 valve of that circuit, and the "
     "list governs the purchase."),
    (None, "GA Antiscalant Dosing Tank", "P22-DWG-09-005-015", "Rev D", "E91",
     "25007-0091", "2-AN",
     "Submitted for approval, a revision TM N36 did not require. The anchor hole closes: "
     "14 mm and 35/64 inch are the same dimension and both accept the M12 bolt. Open: the "
     "LEVEL MARKING row still carries a dash in SIZE and a dash in ELEVATION, unchanged "
     "from Rev C and verified by render, while the comment sheet reports the mark as "
     "added with dimensions."),
    (None, "Radiography Examination Procedure (RT)", "P22-BA-09-000-015", "Rev 0", "E92",
     "25007-0092", "1-Approved",
     "Issued for construction. The determinant closed: the scope declares duplex S32750 "
     "in 6.02 to 8.56 mm with an Iridium 192 source, the material and range actually "
     "radiographed. Cross-references repointed to T-277.2 and T-282.1, and one comment "
     "sheet row per comment for the first time. Housekeeping to Section 3: the cover still "
     "reads RT PROV-PROC-RT-001 and no issue status is declared. Third and last of the NDT "
     "procedures to reach Rev 0."),
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

    # 1) updates del N39 (3 re-revisiones)
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
            print(f"  MR update row {r}: {code} -> {u['verdict']} / {u['tm']} ({u['rev']})")
    missing = set(MR_UPDATES) - seen
    if missing:
        raise SystemExit(f"ERROR: codigos N39 no encontrados en Master Register: {missing}")

    # 2) correcciones de registro: revision y entrega, sin tocar veredicto ni TM
    seen_fix = set()
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code in MR_FIXES:
            f = MR_FIXES[code]
            antes = (mr.cell(r, C_REV).value, mr.cell(r, C_DEL).value)
            mr.cell(r, C_REV).value = f["rev"]
            mr.cell(r, C_DEL).value = f["delivery"]
            mr.cell(r, C_ACT).value = f["action"]
            seen_fix.add(code)
            print(f"  MR fix    row {r}: {code} {antes} -> ({f['rev']}, {f['delivery']}); "
                  f"veredicto sin tocar: {mr.cell(r, C_VER).value}")
    missing_fix = set(MR_FIXES) - seen_fix
    if missing_fix:
        raise SystemExit(f"ERROR: codigos a corregir no encontrados: {missing_fix}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 3) Revision History (3 filas nuevas; la correccion no genera fila)
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

    # 4) Summary: recomputar total/delivered + verdicts desde MR
    stat = collections.Counter(); vd = collections.Counter(); total = 0
    for r in range(2, mr.max_row + 1):
        if mr.cell(r, C_CODE).value:
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

    # Gate: el tally se declara antes de correr y se contrasta aqui.
    real = {k: vd.get(k, 0) for k in TALLY_ESPERADO}
    if real != TALLY_ESPERADO:
        print(f"  🔴 TALLY DISTINTO DEL ESPERADO: esperado {TALLY_ESPERADO}, real {real}")
    else:
        print(f"  Tally coincide con lo declarado: {real}")

    sm["B4"].value = total
    sm["B5"].value = delivered
    sm["B7"].value = partial
    sm["B8"].value = not_delivered
    sm["B9"].value = "39 (N1 through N39 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "92 (E1 through E92; the submittal series has no missing numbers)"
    sm["B12"].value = "08-Sep-2026 (E92)"
    sm["B13"].value = "09-Sep-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 5) ITEMS BY SECTION: el N39 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N39 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n39_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n39_build.xlsx")
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
