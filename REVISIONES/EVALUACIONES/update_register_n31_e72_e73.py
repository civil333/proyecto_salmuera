#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n31_e72_e73.py
Incorpora al Master Deliverable Register la emision del TM N31, que cubre las
ENTREGAS 72 (submittal 25007-0072) y 73 (submittal 25007-0074).

CORRER SOLO CUANDO EL TRANSMITTAL SE HAYA ENVIADO. Mientras siga en BORRADOR,
escribir los veredictos afirmaria un acto que no ocurrio. Es el mismo criterio
con que se escribio el updater anterior de este slot.

EL update_register_n31.py QUE YA EXISTE EN ESTA CARPETA ESTA OBSOLETO: se
escribio para la ENTREGA 69, que termino absorbida en el TM N30, y su respaldo
_pre-N31.xlsx guarda el estado ANTERIOR al re-escopeo (50/28/6/0) cuando el
vigente es 50/29/7/0. No reutilizar ni su script ni su respaldo.

Idempotencia: el respaldo _pre-N31-E72-E73.xlsx conserva el estado limpio previo.
Al re-correr, RESTAURA SRC desde ese respaldo antes de aplicar.

NINGUN ITEM NUEVO. Los cinco documentos ya existen en el registro; lo que cambia
es revision, entrega, transmittal, veredicto y accion.

    fila  codigo                de            a
    43    P22-DWG-09-005-005    Rev A, N7, 3  Rev B, N31, 2-AN
    66    P22-BT-09-009-001     Rev E, N28, 2 Rev 0, N31, sin codigo
    67    P22-LI-09-008-016     Rev A, N22, 3 Rev B, N31, 2-AN
    75    P22-DWG-09-005-008    Rev A, N15, 2 Rev B, N31, 2-AN
    106   P22-BA-09-000-009     Rev C, N27, 2 Rev 0, N31, 1-Approved

Tally esperado despues: 51 Code 1 / 29 Code 2 / 5 Code 3 / 0 Code 4, mas un
documento sin codigo. Transmittals 30 -> 31. Entregas 70 -> 73. El total de
items (110) y de entregados (86) no cambia.

El bloque ITEMS BY SECTION del Summary arrastra un descuadre heredado. Este
script lo mide antes y despues y aborta si lo agranda.
"""
import os
import shutil
import sys

import openpyxl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N31-E72-E73.xlsx")

TM = "N31"

# code -> (rev, delivery, verdict, status, action)
UPDATES = {
    "P22-DWG-09-005-005": (
        "B", "E72", "2-AN", "Delivered",
        "State the design pressure at the brine feed tie-in point TP-DA P8-001 and "
        "complete the flange class and standard of TP-AS P11-001, at IFC Rev 0."),
    "P22-BT-09-009-001": (
        "0", "E72", "No code issued", "Delivered",
        "Four conditions of the TM N28 approval remain open: CIP pump winding and "
        "bearing tags, vibration pairs against the Alarm and Interlock List, winding "
        "trip against the motor insulation class, and the child documents pinned by "
        "code and revision. Close at the next issue."),
    "P22-LI-09-008-016": (
        "B", "E73", "2-AN", "Delivered",
        "Add the electrical-variable meter readings to the overview screen and "
        "reconcile six tags against the approved lists, at IFC Rev 0."),
    "P22-DWG-09-005-008": (
        "B", "E72", "2-AN", "Delivered",
        "Correct the three document references of notes 6, 7 and 8, at IFC Rev 0."),
    "P22-BA-09-000-009": (
        "0", "E72", "1-Approved", "Delivered",
        "None on this document. Calibration validity of certificate 26993 at the date "
        "of the test, and the gauge label on the test schematic, tracked in Section 3."),
}


def main():
    if os.path.exists(BAK):
        shutil.copyfile(BAK, SRC)
        print("Restaurado SRC desde el respaldo:", os.path.basename(BAK))
    else:
        shutil.copyfile(SRC, BAK)
        print("Respaldo creado:", os.path.basename(BAK))

    wb = openpyxl.load_workbook(SRC)
    mr = wb["Master Register"]
    sm = wb["Summary"]

    delta_previo = (
        sum(int(sm.cell(r, 2).value) for r in range(18, 23)) - int(sm["B4"].value),
        sum(int(sm.cell(r, 3).value) for r in range(18, 23)) - int(sm["B5"].value),
    )

    hdr = {mr.cell(1, c).value: c for c in range(1, mr.max_column + 1)}
    C_CODE, C_REV = hdr["Code / ET Reference"], hdr["Rev"]
    C_DEL, C_TM = hdr["Delivery"], hdr["TM"]
    C_VER, C_STA, C_ACT = hdr["Verdict"], hdr["Status"], hdr["Action Required"]

    aplicados = set()
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code not in UPDATES:
            continue
        rev, delivery, verdict, status, action = UPDATES[code]
        print("  fila %-4d %-20s  Rev %s -> %s | TM %s -> %s | %s -> %s"
              % (r, code, mr.cell(r, C_REV).value, rev,
                 mr.cell(r, C_TM).value, TM, mr.cell(r, C_VER).value, verdict))
        mr.cell(r, C_REV).value = rev
        mr.cell(r, C_DEL).value = delivery
        mr.cell(r, C_TM).value = TM
        mr.cell(r, C_VER).value = verdict
        mr.cell(r, C_STA).value = status
        mr.cell(r, C_ACT).value = action
        aplicados.add(code)

    faltan = set(UPDATES) - aplicados
    if faltan:
        raise SystemExit("ERROR: codigos no encontrados en el registro: %s" % faltan)

    # Recuento real desde el Master Register, no incremental.
    #
    # SE CUENTA SOLO Status == 'Delivered', que es el universo del bloque
    # VERDICT DISTRIBUTION del Summary ("Delivered Items") y el que reporta el
    # README. Barrer TODAS las filas da un Code 2 de mas y hace abortar la
    # guardia sin que haya nada malo en los datos: la fila 'Civil Requirements
    # Drawings' lleva veredicto 2-AN con Status 'Covered', no 'Delivered', de
    # modo que hay 87 veredictos numericos contra 86 entregados.
    tally = {"1": 0, "2": 0, "3": 0, "4": 0}
    for r in range(2, mr.max_row + 1):
        if str(mr.cell(r, C_STA).value or "").strip().upper() != "DELIVERED":
            continue
        v = str(mr.cell(r, C_VER).value or "").strip()
        if v[:1] in tally:
            tally[v[:1]] += 1
    print("  Tally recontado: %d Code 1 / %d Code 2 / %d Code 3 / %d Code 4"
          % (tally["1"], tally["2"], tally["3"], tally["4"]))
    if (tally["1"], tally["2"], tally["3"], tally["4"]) != (51, 29, 5, 0):
        raise SystemExit(
            "ERROR: el tally no cuadra con lo esperado (51/29/5/0). "
            "Revisar antes de guardar.")

    delta_post = (
        sum(int(sm.cell(r, 2).value) for r in range(18, 23)) - int(sm["B4"].value),
        sum(int(sm.cell(r, 3).value) for r in range(18, 23)) - int(sm["B5"].value),
    )
    if delta_post != delta_previo:
        raise SystemExit("ERROR: el descuadre heredado de ITEMS BY SECTION cambio: "
                         "%s -> %s" % (delta_previo, delta_post))
    print("  Descuadre heredado de ITEMS BY SECTION sin cambios: %s" % (delta_previo,))

    print("\nEDITAR A MANO en la hoja Summary, que esta hardcodeada:")
    print("  - VERDICT DISTRIBUTION a 51 / 29 / 5 / 0, y AGREGAR la fila")
    print("    'No code issued' con 1, o el bloque suma 85 contra 86 entregados:")
    print("    la Plant Control Philosophy sigue entregada pero ya no lleva codigo")
    print("  - Transmittals a 31 y entregas a 73")
    print("  - Status Date a 10-Aug-2026")

    wb.save(SRC)
    print("\nRegistro actualizado:", os.path.basename(SRC))


if __name__ == "__main__":
    main()
