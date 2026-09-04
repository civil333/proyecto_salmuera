#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diff_trackers.py — Diff celda a celda del "Procurement tracking - BW Water" entre semanas.

Compara N versiones del tracker (misma plantilla: Weekly Dashboard (2) / Milestone Tracker /
Change Log / Legend) y emite un .md con SOLO lo que cambio, mas dos bloques de control:

  - SLIP SILENCIOSO: fecha que se movio sin la entrada correspondiente en el Change Log.
    El Change Log lo mantiene BW Water; si esta vacio mientras las fechas se mueven,
    esa ausencia es en si el hallazgo (ver feedback_silent_slip_detection).
  - ALTAS Y BAJAS: items de equipo que aparecen o desaparecen entre versiones.

Solo lectura sobre los .xlsx. Sin pandas. Re-ejecutable.

Uso:
    python diff_trackers.py                 # serie por defecto (13-Jul -> 03-Ago)
    python diff_trackers.py --out otro.md
"""
import argparse
import datetime
import os
import sys

import openpyxl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.abspath(__file__))

# (etiqueta, ruta relativa a BASE) en orden cronologico
SERIE = [
    ("13-Jul", os.path.join("SEMANA 13-07-26", "ZIP_EXTRAIDO", "Procurement tracking - BW Water 2906.xlsx")),
    ("20-Jul", os.path.join("SEMANA 20-07-26", "Copy of Procurement tracking - BW Water 2906.xlsx")),
    ("27-Jul", os.path.join("SEMANA 27-07-26", "Copy of Procurement tracking - BW Water 2906.xlsx")),
    ("03-Ago", os.path.join("SEMANA 03-08-26", "Copy of Procurement tracking - BW Water 2906.xlsx")),
]

HOJA_DASH = "Weekly Dashboard (2)"
HOJA_HITOS = "Milestone Tracker"
HOJA_LOG = "Change Log"
FILA_HEADER = 3  # 1-based: '#', 'Equipment', 'TAG', ...

CAMPOS_FECHA = ("PO Date", "Estimate Arrival Penang", "Actual Arrival Penang",
                "Baseline Date", "Estimate", "Actual")


def fmt(v):
    """Normaliza una celda a texto comparable. Fechas -> ISO; None -> ''."""
    if v is None:
        return ""
    if isinstance(v, datetime.datetime):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, datetime.date):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v).strip().replace("\n", " ")


def leer(ruta):
    """Devuelve dict con dashboard {clave: {campo: valor}}, hitos y n de filas del change log."""
    wb = openpyxl.load_workbook(ruta, read_only=True, data_only=True)

    ws = wb[HOJA_DASH]
    filas = [list(r) for r in ws.iter_rows(values_only=True)]
    cab = [fmt(c) for c in filas[FILA_HEADER - 1]]

    dash, orden = {}, []
    for r in filas[FILA_HEADER:]:
        num = fmt(r[0]) if r else ""
        if not num.isdigit():
            continue  # la leyenda pegada al final del dashboard no es un item
        equipo = fmt(r[1]) if len(r) > 1 else ""
        clave = "%s|%s" % (num, equipo)
        dash[clave] = {cab[i] if i < len(cab) and cab[i] else "col%d" % i: fmt(r[i])
                       for i in range(len(r))}
        orden.append(clave)

    hitos = {}
    if HOJA_HITOS in wb.sheetnames:
        fh = [list(r) for r in wb[HOJA_HITOS].iter_rows(values_only=True)]
        cabh = [fmt(c) for c in fh[1]] if len(fh) > 1 else []
        for r in fh[2:]:
            nombre = fmt(r[0]) if r else ""
            if not nombre:
                continue
            hitos[nombre] = {cabh[i] if i < len(cabh) and cabh[i] else "col%d" % i: fmt(r[i])
                             for i in range(len(r))}

    log = 0
    if HOJA_LOG in wb.sheetnames:
        for r in list(wb[HOJA_LOG].iter_rows(values_only=True))[2:]:
            if any(fmt(c) for c in r):
                log += 1

    wb.close()
    return {"dash": dash, "orden": orden, "hitos": hitos, "log": log, "cab": cab}


def tabla_cambios(titulo, snaps, etiquetas, extractor):
    """Construye las filas de una tabla de cambios: solo campos que varian en la serie."""
    claves = []
    for s in snaps:
        for k in extractor(s):
            if k not in claves:
                claves.append(k)

    out = []
    for k in claves:
        campos = []
        for s in snaps:
            d = extractor(s).get(k, {})
            for c in d:
                if c not in campos and c not in ("#",):
                    campos.append(c)
        for campo in campos:
            vals = [extractor(s).get(k, {}).get(campo, "<ausente>") for s in snaps]
            if len(set(vals)) <= 1:
                continue
            out.append((k, campo, vals))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(BASE, "SEMANA 03-08-26", "DIFF_TRACKERS.md"))
    args = ap.parse_args()

    snaps, etiquetas, faltan = [], [], []
    for et, rel in SERIE:
        p = os.path.join(BASE, rel)
        if not os.path.exists(p):
            faltan.append((et, rel))
            continue
        snaps.append(leer(p))
        etiquetas.append(et)

    if len(snaps) < 2:
        print("Se necesitan al menos 2 versiones. Faltan:", faltan)
        return 1

    L = []
    L.append("# Diff del Procurement Tracking de BW Water")
    L.append("")
    L.append("> Generado por `diff_trackers.py`. Solo se listan las celdas que cambiaron. "
             "Fechas normalizadas a ISO. Lectura sobre los `.xlsx` originales, sin escritura.")
    L.append("")
    L.append("**Versiones comparadas:** " + " -> ".join(etiquetas))
    if faltan:
        L.append("")
        L.append("**Advertencia — versiones no encontradas (cobertura incompleta):** " +
                 ", ".join("%s (`%s`)" % (e, r) for e, r in faltan))
    L.append("")

    # ---- Change Log ----
    L.append("## Change Log declarado por BW Water")
    L.append("")
    L.append("| Version | Filas con contenido |")
    L.append("|---|---|")
    for et, s in zip(etiquetas, snaps):
        L.append("| %s | %d |" % (et, s["log"]))
    L.append("")
    if all(s["log"] == 0 for s in snaps):
        L.append("**El Change Log esta vacio en las %d versiones.** Todo movimiento de fecha listado "
                 "abajo ocurrio sin declaracion del proveedor." % len(snaps))
    L.append("")

    # ---- Altas y bajas ----
    L.append("## Altas y bajas de items")
    L.append("")
    hubo = False
    for i in range(1, len(snaps)):
        prev, cur = set(snaps[i - 1]["dash"]), set(snaps[i]["dash"])
        altas, bajas = sorted(cur - prev), sorted(prev - cur)
        if altas or bajas:
            hubo = True
            L.append("**%s -> %s**" % (etiquetas[i - 1], etiquetas[i]))
            L.append("")
            for a in altas:
                L.append("- ALTA: `%s`" % a)
            for b in bajas:
                L.append("- BAJA: `%s`" % b)
            L.append("")
    if not hubo:
        L.append("Sin altas ni bajas: los %d items del dashboard se mantienen en toda la serie." %
                 len(snaps[0]["dash"]))
    L.append("")

    # ---- Dashboard ----
    cambios = tabla_cambios("dash", snaps, etiquetas, lambda s: s["dash"])
    L.append("## Weekly Dashboard - celdas que cambiaron")
    L.append("")
    if not cambios:
        L.append("Sin cambios.")
    else:
        L.append("| Item | Campo | " + " | ".join(etiquetas) + " |")
        L.append("|---|---|" + "---|" * len(etiquetas))
        for k, campo, vals in cambios:
            L.append("| %s | %s | %s |" % (k, campo, " | ".join(v or "-" for v in vals)))
    L.append("")

    # ---- Slip silencioso ----
    L.append("## Slip silencioso (fecha movida sin entrada en el Change Log)")
    L.append("")
    slips = []
    for k, campo, vals in cambios:
        if campo not in CAMPOS_FECHA:
            continue
        for i in range(1, len(vals)):
            a, b = vals[i - 1], vals[i]
            if a in ("", "<ausente>") or b in ("", "<ausente>") or a == b:
                continue
            try:
                da = datetime.date.fromisoformat(a)
                db = datetime.date.fromisoformat(b)
            except ValueError:
                continue
            d = (db - da).days
            if d:
                slips.append((k, campo, etiquetas[i - 1], etiquetas[i], a, b, d))
    if not slips:
        L.append("Ninguno detectado en los campos de fecha.")
    else:
        slips.sort(key=lambda t: -abs(t[6]))
        L.append("| Item | Campo | De | A | Fecha antes | Fecha despues | Dias |")
        L.append("|---|---|---|---|---|---|---|")
        for k, campo, e1, e2, a, b, d in slips:
            L.append("| %s | %s | %s | %s | %s | %s | %+d |" % (k, campo, e1, e2, a, b, d))
        L.append("")
        L.append("Total de movimientos de fecha no declarados: **%d**." % len(slips))
    L.append("")

    # ---- Hitos ----
    ch = tabla_cambios("hitos", snaps, etiquetas, lambda s: s["hitos"])
    L.append("## Milestone Tracker - celdas que cambiaron")
    L.append("")
    if not ch:
        L.append("Sin cambios.")
    else:
        L.append("| Hito | Campo | " + " | ".join(etiquetas) + " |")
        L.append("|---|---|" + "---|" * len(etiquetas))
        for k, campo, vals in ch:
            L.append("| %s | %s | %s |" % (k, campo, " | ".join(v or "-" for v in vals)))
    L.append("")
    L.append("### Estado de los hitos en la ultima version (%s)" % etiquetas[-1])
    L.append("")
    ult = snaps[-1]["hitos"]
    if ult:
        campos = ["Baseline Date", "Estimate", "Actual", "Status (C/E/D/N)"]
        L.append("| Hito | " + " | ".join(campos) + " |")
        L.append("|---|" + "---|" * len(campos))
        for h, d in ult.items():
            L.append("| %s | %s |" % (h, " | ".join(d.get(c, "") or "-" for c in campos)))
    L.append("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("Escrito:", args.out)
    print("  versiones:", " -> ".join(etiquetas))
    print("  celdas cambiadas:", len(cambios), "| slips de fecha:", len(slips),
          "| cambios en hitos:", len(ch))
    if faltan:
        print("  ADVERTENCIA - no encontradas:", faltan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
