#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diff_fabrication_schedule.py — Diff del "Fabrication schedule" (hoja `RO system`) entre versiones.

Estructura de la hoja: A=Actividad, B=etiqueta de estado, C=Progress (%), D=Days,
E=Remarks, F=Baseline Start, G=Baseline Finish; de H en adelante, grilla de calendario
(fila 2 = semana `wwNN`, fila 4 = fecha, fila 5 = dia).

Emite un .md con: altas y bajas de actividades, deltas de fecha y avance, extension del
calendario y el top de deslizamientos. Solo lectura, sin pandas.

Uso:
    python diff_fabrication_schedule.py
"""
import argparse
import datetime
import os
import sys

import openpyxl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)  # ...\PROGRAMA y CONTRATO

SERIE = [
    ("01-Jul", os.path.join(RAIZ, "PROGRAMA DE FABRICACION 01-07-26", "Fabrication schedule.xlsx")),
    ("03-Ago", os.path.join(BASE, "SEMANA 03-08-26", "Fabrication schedule.xlsx")),
]

HOJA = "RO system"
FILA_HEADER = 2  # 1-based: '', 'Completed', ['Progress (%)'], 'Days', 'Remarks', 'Baseline Start', 'Baseline Finish', 'wwNN'...
CAMPOS = ["Progress", "Days", "Remarks", "Baseline Start", "Baseline Finish"]
FECHAS = ("Baseline Start", "Baseline Finish")

# El layout NO es estable entre versiones: la columna `Progress (%)` no existe en la
# version de julio y desplaza una posicion a todas las siguientes. Por eso las columnas
# se resuelven leyendo la fila de encabezado, nunca por indice fijo.
ALIAS = {
    "progress (%)": "Progress",
    "progress": "Progress",
    "days": "Days",
    "remarks": "Remarks",
    "baseline start": "Baseline Start",
    "baseline finish": "Baseline Finish",
}


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, float):
        return ("%g" % v)
    return str(v).strip().replace("\n", " ")


def leer(ruta):
    wb = openpyxl.load_workbook(ruta, read_only=True, data_only=True)
    ws = wb[HOJA]
    filas = [list(r) for r in ws.iter_rows(values_only=True)]

    # --- mapa de columnas resuelto por encabezado, no por indice ---
    cab = filas[FILA_HEADER - 1] if len(filas) >= FILA_HEADER else []
    mapa = {}
    for i, c in enumerate(cab):
        n = ALIAS.get(fmt(c).lower())
        if n and n not in mapa:
            mapa[n] = i
    col_cal = max(mapa.values()) + 1 if mapa else 7  # primera columna de calendario

    calendario = []
    if len(filas) >= 4:
        calendario = [c for c in filas[3][col_cal:]
                      if isinstance(c, (datetime.datetime, datetime.date))]

    tareas, orden, vistos = {}, [], {}
    for row in filas[5:]:
        act = fmt(row[0]) if row else ""
        if not act:
            continue
        # clave estable: nombre + indice de repeticion (hay encabezados de seccion repetidos)
        vistos[act] = vistos.get(act, 0) + 1
        clave = act if vistos[act] == 1 else "%s #%d" % (act, vistos[act])
        tareas[clave] = {n: (fmt(row[i]) if i < len(row) else "") for n, i in mapa.items()}
        orden.append(clave)

    n_filas, n_cols = ws.max_row, ws.max_column
    wb.close()
    return {"tareas": tareas, "orden": orden, "cal": calendario, "mapa": mapa,
            "filas": n_filas, "cols": n_cols}


def dias(a, b):
    try:
        return (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(BASE, "SEMANA 03-08-26", "DIFF_FABRICATION_SCHEDULE.md"))
    args = ap.parse_args()

    snaps, etq, faltan = [], [], []
    for e, p in SERIE:
        if not os.path.exists(p):
            faltan.append((e, p))
            continue
        snaps.append(leer(p))
        etq.append(e)
    if len(snaps) < 2:
        print("Se necesitan 2 versiones. Faltan:", faltan)
        return 1

    a, b = snaps[0], snaps[-1]
    ea, eb = etq[0], etq[-1]

    L = []
    L.append("# Diff del Fabrication Schedule de BW Water")
    L.append("")
    L.append("> Generado por `diff_fabrication_schedule.py`. Hoja `%s`. Solo lectura sobre los `.xlsx`." % HOJA)
    L.append("")
    L.append("**Versiones:** %s -> %s" % (ea, eb))
    if faltan:
        L.append("")
        L.append("**Advertencia — no encontradas:** " + ", ".join("%s (`%s`)" % f for f in faltan))
    L.append("")
    L.append("Solo existen **%d versiones** de este archivo en el repositorio, de modo que la comparacion "
             "cubre el salto completo de un mes y no permite ver en que semana ocurrio cada movimiento." % len(snaps))
    L.append("")

    # --- dimensiones y calendario ---
    L.append("## Dimensiones y ventana de calendario")
    L.append("")
    L.append("| Version | Filas | Columnas | Primera fecha | Ultima fecha |")
    L.append("|---|---|---|---|---|")
    for e, s in zip(etq, snaps):
        c = s["cal"]
        L.append("| %s | %d | %d | %s | %s |" % (
            e, s["filas"], s["cols"],
            c[0].strftime("%Y-%m-%d") if c else "-",
            c[-1].strftime("%Y-%m-%d") if c else "-"))
    if a["cal"] and b["cal"]:
        d = (b["cal"][-1].date() - a["cal"][-1].date()).days
        L.append("")
        L.append("La grilla de calendario se extiende **%+d dias** (%+d columnas): el cronograma "
                 "amplia su horizonte, lo que por si solo ya indica que el fin de obra se corrio." %
                 (d, b["cols"] - a["cols"]))
    L.append("")

    # --- altas y bajas ---
    sa, sb = set(a["tareas"]), set(b["tareas"])
    altas, bajas = sorted(sb - sa), sorted(sa - sb)
    L.append("## Altas y bajas de actividades")
    L.append("")
    L.append("Actividades en %s: **%d** | en %s: **%d**" % (ea, len(sa), eb, len(sb)))
    L.append("")
    if altas:
        L.append("**Altas (%d):**" % len(altas))
        L.append("")
        for x in altas:
            t = b["tareas"][x]
            L.append("- `%s` - baseline %s a %s, %s, avance %s" % (
                x, t.get("Baseline Start", "-") or "-", t.get("Baseline Finish", "-") or "-",
                t.get("Days", "-") or "-", t.get("Progress", "-") or "-"))
        L.append("")
    if bajas:
        L.append("**Bajas (%d):**" % len(bajas))
        L.append("")
        for x in bajas:
            t = a["tareas"][x]
            L.append("- `%s` - tenia baseline %s a %s, %s" % (
                x, t.get("Baseline Start", "-") or "-", t.get("Baseline Finish", "-") or "-",
                t.get("Days", "-") or "-"))
        L.append("")
    if not altas and not bajas:
        L.append("Sin altas ni bajas.")
        L.append("")

    # --- cambio de esquema entre versiones ---
    solo_b = [c for c in b["mapa"] if c not in a["mapa"]]
    solo_a = [c for c in a["mapa"] if c not in b["mapa"]]
    L.append("## Cambio de esquema de la planilla")
    L.append("")
    L.append("| Version | Columnas de datos detectadas |")
    L.append("|---|---|")
    for e, s in zip(etq, snaps):
        L.append("| %s | %s |" % (e, ", ".join("`%s`" % c for c in s["mapa"])))
    L.append("")
    if solo_b or solo_a:
        if solo_b:
            L.append("Columnas **nuevas en %s**: %s. Antes no existian, de modo que su contenido "
                     "no tiene contraparte que comparar." % (eb, ", ".join("`%s`" % c for c in solo_b)))
        if solo_a:
            L.append("Columnas **retiradas** respecto de %s: %s." % (ea, ", ".join("`%s`" % c for c in solo_a)))
        L.append("")
        L.append("Las columnas se resuelven leyendo la fila de encabezado. Comparar por posicion "
                 "habria alineado mal toda la planilla y producido un diff enteramente falso.")
    else:
        L.append("Mismo esquema en ambas versiones.")
    L.append("")

    # --- cambios por actividad ---
    comunes = [c for c in CAMPOS if c in a["mapa"] and c in b["mapa"]]
    filas, desliz = [], []
    for k in b["orden"]:
        if k not in a["tareas"]:
            continue
        ta, tb = a["tareas"][k], b["tareas"][k]
        for c in comunes:
            va, vb = ta.get(c, ""), tb.get(c, "")
            if va == vb:
                continue
            extra = ""
            if c in FECHAS and va and vb:
                d = dias(va, vb)
                if d is not None:
                    extra = "%+d d" % d
                    desliz.append((k, c, va, vb, d))
            elif c in FECHAS and not va and vb:
                extra = "sin baseline previo"
            filas.append((k, c, va, vb, extra))

    L.append("## Cambios por actividad")
    L.append("")
    if not filas:
        L.append("Sin cambios.")
    else:
        L.append("| Actividad | Campo | %s | %s | Delta |" % (ea, eb))
        L.append("|---|---|---|---|---|")
        for k, c, va, vb, ex in filas:
            L.append("| %s | %s | %s | %s | %s |" % (k, c, va or "-", vb or "-", ex or ""))
    L.append("")

    # --- top deslizamientos ---
    L.append("## Mayores deslizamientos de fecha")
    L.append("")
    if not desliz:
        L.append("Ninguno.")
    else:
        desliz.sort(key=lambda t: -abs(t[4]))
        L.append("| # | Actividad | Campo | %s | %s | Dias |" % (ea, eb))
        L.append("|---|---|---|---|---|---|")
        for i, (k, c, va, vb, d) in enumerate(desliz[:10], 1):
            L.append("| %d | %s | %s | %s | %s | %+d |" % (i, k, c, va, vb, d))
        L.append("")
        pos = [d for *_, d in desliz if d > 0]
        if pos:
            L.append("Deslizamientos hacia adelante: **%d** de %d movimientos de fecha; "
                     "maximo **%+d dias**, mediana **%+d dias**." %
                     (len(pos), len(desliz), max(pos), sorted(pos)[len(pos) // 2]))
    L.append("")

    # --- foto de la ultima version ---
    L.append("## Cronograma vigente (%s)" % eb)
    L.append("")
    L.append("| Actividad | Avance | Dias | Baseline Start | Baseline Finish |")
    L.append("|---|---|---|---|---|")
    for k in b["orden"]:
        t = b["tareas"][k]
        if not (t.get("Baseline Start") or t.get("Days")):
            continue
        L.append("| %s | %s | %s | %s | %s |" % (
            k, t.get("Progress", "") or "-", t.get("Days", "") or "-",
            t.get("Baseline Start", "") or "-", t.get("Baseline Finish", "") or "-"))
    L.append("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("Escrito:", args.out)
    print("  actividades %s=%d %s=%d | altas %d | bajas %d | cambios %d | deslizamientos %d" %
          (ea, len(sa), eb, len(sb), len(altas), len(bajas), len(filas), len(desliz)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
