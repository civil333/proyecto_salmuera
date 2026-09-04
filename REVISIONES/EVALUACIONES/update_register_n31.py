#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n31.py
Incorpora la ENTREGA 69 (submittal 25007-0069, 1 documento) al Master Deliverable
Register. Modelado en update_register_n30.py.

Idempotencia: el backup _pre-N31.xlsx conserva el estado LIMPIO N30 (50/28/6/0).
Al re-correr, RESTAURA SRC desde ese backup antes de aplicar.

DIFERENCIA DE CRITERIO CON LOS UPDATERS ANTERIORES — leer antes de tocar:

  El TM N31 NO se ha emitido. El veredicto Codigo 3 sobre el Dossier Index esta
  analizado y propuesto, pero mientras el transmittal no salga, escribirlo en el
  registro afirmaria un acto que no ocurrio. Por eso:

    - el item nuevo #113 entra con Status 'Delivered' (la entrega SI ocurrio, el
      27-Jul) y Verdict 'Under review', que es el valor que la propia Legend del
      libro define como "Document delivered but evaluation pending";
    - la columna TM queda en '--' y el conteo de transmittals se mantiene en 30;
    - no se agrega fila a Revision History, que registra revisiones EMITIDAS.

  Al emitir el TM N31, un updater posterior cambia Verdict a '3-To be revised',
  pone TM='N31' y agrega la fila de Revision History.

OPCION HIBRIDA sobre el dossier (decidida en la revision de la E69):

    #113 NUEVO  P22-BA-09-000-013 Rev A  Fabrication and Testing Dossier Index
    #65  SE MANTIENE 'NOT DELIVERED'     Manufacturing and Testing Dossier

  El indice de 2 paginas no es el dossier. Declarar entregado el item 65
  debilitaria la posicion sobre los items 8.3 y 8.4 del PIE, que sostienen el
  40% del pago. Solo se reescribe su 'Action Required' para registrar que el
  indice llego.

Tally esperado tras la E69: 50 Code 1 / 28 Code 2 / 6 Code 3 / 0 Code 4 (sin
cambio, el nuevo item no lleva veredicto todavia); 109 items / 85 delivered;
30 TMs / 69 entregas. ITEMS BY SECTION, Seccion 3: 11 -> 12 total, 8 -> 9
delivered.
"""
import collections
import os
import shutil
import sys
from copy import copy

import openpyxl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N31.xlsx")

STATUS_DATE = "05-Aug-2026"

# --- item nuevo: el indice del dossier, entregado y pendiente de veredicto ---
NEW_ITEMS = [
    dict(
        document="Fabrication and Testing Dossier Index",
        code="P22-BA-09-000-013",
        rev="A", delivery="E69", tm="--", verdict="Under review",
        status="Delivered",
        action=(
            "Rev A delivered (E69, 27-Jul-2026, submittal 25007-0069, IFA). Issued in "
            "response to the first tranche of the 25-Jul dossier claim. Review complete, "
            "transmittal not yet issued; proposed verdict 3 - To be revised, re-issue as "
            "Rev B. The index lists 27 chapters with no document number, revision or "
            "inclusion status against any of them, so it cannot serve as the checklist for "
            "the preliminary documentation review that the Inspection and Testing Base Plan "
            "(P22-IT-09-000-001-0) assigns to ADASA at item 7.6. Missing chapters: "
            "preparation for dispatch (cleaning and preservation, packaging and marking "
            "records, packing list) per Inspection and Test Plan rows 8.1 and 8.2; the FAT "
            "Approval Certificate that the Technical Specification (P22-ET-09-000-001-0), "
            "Section 8, declares an integral part of the final dossier; inspection personnel "
            "qualifications and test equipment calibration per NDE Plan Section 3.0 and "
            "Inspection and Test Plan row 2.4; manufacturer certificates and factory test "
            "records of the main equipment per row 2.3; and a non-conformance and weld "
            "repair register. Chapters B3, B4 and B6 list ultrasonic, dye penetrant and "
            "radiography procedures that have never been submitted to ADASA for review, "
            "which the NDE Plan Section 2.0 requires: these are to be approved before "
            "welding starts, since records produced under unapproved procedures are not "
            "admissible into the dossier."),
        et_deadline="ET Sec.7: Max. 90 days from NTP",
    ),
]

# --- reescritura del Action Required del item 65 (sigue NOT DELIVERED) ---
# Clave por NUMERO DE ITEM, no por 'Code / ET Reference': los items 62, 63 y 65
# comparten la referencia 'ET Sec 7, p.28' y usarla como clave toca tres filas.
MR_ACTION_FIXES = {
    65: (
        "NOT DELIVERED. The Fabrication and Testing Dossier Index (P22-BA-09-000-013 Rev A) "
        "arrived on 27-Jul-2026 as item 113 of this register, but an index is not the "
        "dossier: no fabrication or testing record has been submitted to date. The second "
        "tranche of the 25-Jul claim - complete preliminary dossier structured against the "
        "index, due Friday 31-Jul-2026 - lapsed with no evidence of delivery. Contractual "
        "basis: Technical Specification (P22-ET-09-000-001-0), Section 7, maximum 90 days "
        "from award, including the manufacturing certificates of the special steels for the "
        "super duplex equipment. Prerequisite for factory acceptance and gating item 8.3 "
        "(final dossier approval, Hold) and item 8.4 (release for dispatch) of the "
        "Inspection and Testing Base Plan, which support the 40% payment milestone. Part of "
        "the Week 1 records reached ADASA through the third-party inspector's Annex A, not "
        "from the supplier."),
}


def style_row(ws, dst_row, ref_row, ncols):
    for c in range(1, ncols + 1):
        ws.cell(dst_row, c)._style = copy(ws.cell(ref_row, c)._style)


def main():
    if os.path.exists(BAK):
        shutil.copyfile(BAK, SRC)
        print("Restaurado SRC desde baseline limpio:", os.path.basename(BAK))
    else:
        shutil.copyfile(SRC, BAK)
        print("Baseline creado:", os.path.basename(BAK))

    wb = openpyxl.load_workbook(SRC)
    mr = wb["Master Register"]
    sm = wb["Summary"]

    # Descuadre HEREDADO de ITEMS BY SECTION, medido ANTES de tocar nada. El
    # bloque esta hardcodeado en el libro y se ha editado a mano durante meses;
    # al 05-Ago-2026 declara un entregado de mas respecto del propio registro.
    # No se corrige a ciegas porque la asignacion de seccion no es derivable de
    # ninguna columna (la referencia 'ET Deadline' no la determina). Lo que si
    # se exige es que este updater NO agrande el descuadre.
    delta_previo = (
        sum(int(sm.cell(r, 2).value) for r in range(18, 23)) - int(sm["B4"].value),
        sum(int(sm.cell(r, 3).value) for r in range(18, 23)) - int(sm["B5"].value),
    )

    ncols = mr.max_column
    hdr = {mr.cell(1, c).value: c for c in range(1, ncols + 1)}
    C_NUM, C_DOC, C_CODE = hdr["#"], hdr["Document"], hdr["Code / ET Reference"]
    C_REV, C_DEL, C_TM = hdr["Rev"], hdr["Delivery"], hdr["TM"]
    C_VER, C_STA, C_ACT = hdr["Verdict"], hdr["Status"], hdr["Action Required"]
    C_DDL = hdr["ET Deadline"]

    # 1) higiene del item 65: sigue NOT DELIVERED, solo se refresca su accion
    aplicados = set()
    for r in range(2, mr.max_row + 1):
        num = mr.cell(r, C_NUM).value
        num = int(num) if isinstance(num, (int, float)) else None
        if num in MR_ACTION_FIXES:
            if str(mr.cell(r, C_STA).value or "").strip().upper() != "NOT DELIVERED":
                raise SystemExit(
                    "ERROR: el item #%d ya no esta NOT DELIVERED; revisar antes de tocar"
                    % num)
            mr.cell(r, C_ACT).value = MR_ACTION_FIXES[num]
            aplicados.add(num)
            print("  MR action fix fila %d: item #%d '%s' sigue NOT DELIVERED"
                  % (r, num, mr.cell(r, C_DOC).value))
    faltan = set(MR_ACTION_FIXES) - aplicados
    if faltan:
        raise SystemExit("ERROR: items no encontrados en Master Register: %s" % faltan)

    # 2) items nuevos al final, con el estilo de la ultima fila
    ultima = max(r for r in range(2, mr.max_row + 1) if mr.cell(r, C_CODE).value)
    max_num = max(int(mr.cell(r, C_NUM).value) for r in range(2, mr.max_row + 1)
                  if isinstance(mr.cell(r, C_NUM).value, (int, float)))
    existentes = {str(mr.cell(r, C_CODE).value or "").strip()
                  for r in range(2, mr.max_row + 1)}

    for i, it in enumerate(NEW_ITEMS, start=1):
        if it["code"] in existentes:
            raise SystemExit("ERROR: %s ya existe en el registro" % it["code"])
        dst = ultima + i
        style_row(mr, dst, ultima, ncols)
        mr.cell(dst, C_NUM).value = max_num + i
        mr.cell(dst, C_DOC).value = it["document"]
        mr.cell(dst, C_CODE).value = it["code"]
        mr.cell(dst, C_REV).value = it["rev"]
        mr.cell(dst, C_DEL).value = it["delivery"]
        mr.cell(dst, C_TM).value = it["tm"]
        mr.cell(dst, C_VER).value = it["verdict"]
        mr.cell(dst, C_STA).value = it["status"]
        mr.cell(dst, C_ACT).value = it["action"]
        mr.cell(dst, C_DDL).value = it["et_deadline"]
        print("  MR nuevo item #%d fila %d: %s Rev %s (%s) -> %s"
              % (max_num + i, dst, it["code"], it["rev"], it["delivery"], it["verdict"]))

    # 3) Summary recomputado desde el Master Register
    stat, vd, total = collections.Counter(), collections.Counter(), 0
    for r in range(2, mr.max_row + 1):
        if str(mr.cell(r, C_CODE).value or "").strip():
            total += 1
            su = str(mr.cell(r, C_STA).value or "").strip().upper()
            stat[su] += 1
            if su == "DELIVERED":
                vd[str(mr.cell(r, C_VER).value or "").strip()] += 1
    delivered = stat.get("DELIVERED", 0)

    sm["B4"].value = total
    sm["B5"].value = delivered
    sm["B7"].value = stat.get("PARTIAL", 0)
    sm["B8"].value = stat.get("NOT DELIVERED", 0)
    sm["B9"].value = "30 (N1 through N30 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "69 (E1 through E69)"
    sm["B12"].value = "27-Jul-2026 (E69)"
    sm["B13"].value = STATUS_DATE

    # El denominador de la distribucion es la suma de veredictos emitidos, no
    # `delivered`: hay un item entregado y aun sin veredicto, y usar `delivered`
    # haria que los porcentajes no sumaran 100.
    con_veredicto = sum(vd[k] for k in
                        ("1-Approved", "2-AN", "3-To be revised", "4-Rejected"))

    def pct(n):
        return "%d%%" % round(100 * n / con_veredicto) if con_veredicto else "0%"

    for fila, clave in ((27, "1-Approved"), (28, "2-AN"),
                        (29, "3-To be revised"), (30, "4-Rejected")):
        sm.cell(fila, 2).value = vd.get(clave, 0)
        sm.cell(fila, 3).value = pct(vd.get(clave, 0))

    # 4) ITEMS BY SECTION — hardcodeada en el libro, se edita a mano.
    #    El indice del dossier pertenece a la Seccion 3 (FABRICATION & FAT),
    #    la misma del item 65.
    fila_s3 = None
    for r in range(18, 23):
        if str(sm.cell(r, 1).value or "").startswith("3. FABRICATION"):
            fila_s3 = r
            break
    if fila_s3 is None:
        raise SystemExit("ERROR: no se encontro la fila de la Seccion 3 en ITEMS BY SECTION")
    sm.cell(fila_s3, 2).value = int(sm.cell(fila_s3, 2).value) + len(NEW_ITEMS)
    sm.cell(fila_s3, 3).value = int(sm.cell(fila_s3, 3).value) + len(NEW_ITEMS)
    print("  Summary Seccion 3: total=%s delivered=%s"
          % (sm.cell(fila_s3, 2).value, sm.cell(fila_s3, 3).value))

    # Coherencia: el descuadre heredado no debe crecer por culpa de este updater
    suma_total = sum(int(sm.cell(r, 2).value) for r in range(18, 23))
    suma_deliv = sum(int(sm.cell(r, 3).value) for r in range(18, 23))
    delta_post = (suma_total - total, suma_deliv - delivered)
    if delta_post != delta_previo:
        raise SystemExit(
            "ERROR: este updater movio el descuadre de ITEMS BY SECTION de %s a %s"
            % (delta_previo, delta_post))
    if any(delta_post):
        print("  AVISO — descuadre HEREDADO en ITEMS BY SECTION, no introducido aqui: "
              "las secciones declaran %+d items y %+d delivered respecto del registro "
              "(secciones %d/%d contra totales %d/%d). Medido tambien sobre el backup "
              "limpio pre-N31. Corregirlo exige reasignar a mano la seccion de cada "
              "item, porque ninguna columna la determina."
              % (delta_post[0], delta_post[1], suma_total, suma_deliv, total, delivered))

    wb.save(SRC)
    print("\nGuardado:", os.path.basename(SRC))
    print("  %d items / %d delivered | veredictos %s | 1 sin veredicto (Under review)"
          % (total, delivered,
             "/".join(str(vd.get(k, 0)) for k in
                      ("1-Approved", "2-AN", "3-To be revised", "4-Rejected"))))
    print("  30 TMs / 69 entregas | ITEMS BY SECTION %d/%d (descuadre heredado %+d/%+d)"
          % (suma_total, suma_deliv, delta_post[0], delta_post[1]))


if __name__ == "__main__":
    main()
