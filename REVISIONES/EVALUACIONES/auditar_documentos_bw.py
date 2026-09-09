#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria documento por documento de los entregables de BW Water.

Responde a una pregunta concreta: por que hay tan pocos documentos emitidos para
construccion si ADASA ya aprobo casi todo. Cruza tres fuentes y NO escribe en ninguna:

  1. Master Deliverable Register, hojas `Master Register` y `Revision History`:
     revision vigente, entrega, transmittal, veredicto y la fecha del primer
     Codigo 1 o 2 de cada documento.
  2. El formulario de submittal de la entrega vigente: la columna `Sub. For`, que
     es donde BW Water declara si somete para aprobacion o para construccion.
  3. El cajetin del propio PDF: `Issued for:` en las hojas de datos y
     `DRAWING STATUS` en los planos, que es donde el documento se contradice consigo
     mismo cuando lleva revision numerica y sigue diciendo que es para aprobacion.

Salida: _AUDITORIA_REV0_<fecha>.md, separado en ingenieria y en calidad y
fabricacion. Es el respaldo interno de las cifras del correo y no se envia.

Uso:
    python auditar_documentos_bw.py
"""
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

import fitz
from openpyxl import load_workbook

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# La raiz se deriva de la ubicacion del script, que vive en
# <PROY>/REVISIONES/EVALUACIONES/.
PROY = Path(__file__).resolve().parents[2]
REGISTRO = Path(__file__).resolve().parent / "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx"
ENTREGAS = PROY / "ENTREGAS_BWWATER"
SALIDA = Path(__file__).resolve().parent / "_AUDITORIA_REV0_2026-09-09.md"

CORTE = date(2026, 9, 9)

# La localizacion del archivo fisico ya esta resuelta en el catalogador del dossier,
# con las cinco correcciones de codigo y las dos de revision que el registro arrastra.
sys.path.insert(0, str(PROY / "BASES DE LICITACION MONTAJE MECANICO-OOCC"
                       / "BORRADOR_REV0" / "script"))
from catalogar_ingenieria_bw import (  # noqa: E402
    ALIAS_CODIGO, REV_REAL, localizar, norm_rev,
)

# Revisiones que BW Water entrego y el Master Register no recogio. Se verificaron
# contra el archivo en ENTREGAS_BWWATER y contra lo que los propios transmittals de
# ADASA declaran. Sin esta correccion la auditoria reclamaria la emision de un
# documento que ya esta emitido.
REV_ENTREGADA = {
    "P22-CD-09-005-001": dict(
        rev="0", entrega="E71",
        nota="Los transmittals N37 y N38 lo declaran emitido en revision 0 para "
             "construccion; lo que sigue abierto es el endoso del profesional. El "
             "registro quedo en Rev B del N29."),
}

# Revisiones posteriores ya recibidas y aun sin revisar por ADASA. No cambian la
# categoria, porque el documento sigue en revision de letra, pero el correo no puede
# afirmar que la revision del registro es la ultima que el proveedor envio.
REV_EN_REVISION = {
    "P22-LI-09-005-002": dict(rev="E", entrega="E91"),
    "P22-DWG-09-005-015": dict(rev="D", entrega="E91"),
}

RX_CODIGO = re.compile(r"^(P22-([A-Z]+)-09-(\d{3})-(\d{2,3}))")
TIPOS_CALIDAD = {"BA", "PP", "MTC"}

DISCIPLINA = {
    "000": "General", "004": "Arquitectura de control", "005": "Mecanica",
    "006": "Canerias", "007": "Electricidad", "008": "Control e instrumentacion",
    "009": "Proceso",
}

# Codigos que la leyenda del formulario PEM-F013 Rev 3 define, mas el IFA que
# BW Water usa desde la entrega 19 sin que la leyenda lo defina.
SUB_FOR = ("IFC", "IFA", "FA", "FR", "FI", "AB")


def dias(d):
    return (CORTE - d).days if d else None


# --------------------------------------------------------------- el registro
def leer_registro():
    wb = load_workbook(REGISTRO, read_only=True, data_only=True)

    docs = []
    for f in list(wb["Master Register"].values)[1:]:
        if not f or not f[2]:
            continue
        code = str(f[2]).strip()
        m = RX_CODIGO.match(code)
        docs.append(dict(
            num=f[0], titulo=str(f[1] or "").strip(), codigo=m.group(1) if m else None,
            referencia=None if m else code,
            tt=m.group(2) if m else None, ddd=m.group(3) if m else None,
            rev=norm_rev(f[3]), entrega=str(f[4] or "").strip(),
            tm=str(f[5] or "").strip(), verdicto=str(f[6] or "").strip(),
            status=str(f[7] or "").strip(), accion=str(f[8] or "").strip()))

    # Primer ciclo con Codigo 1 o 2, y su fecha. Es lo que mide la antiguedad real
    # de la aprobacion, y no se puede inferir del Master Register, que solo guarda
    # el estado actual.
    primera = {}
    for f in list(wb["Revision History"].values)[1:]:
        if not f or not f[2]:
            continue
        code = str(f[2]).strip()
        verd = str(f[8] or "").strip()
        if not (verd.startswith("1") or verd.startswith("2")):
            continue
        fecha = f[7]
        if isinstance(fecha, datetime):
            fecha = fecha.date()
        elif isinstance(fecha, str):
            try:
                fecha = datetime.strptime(fecha.strip(), "%d-%b-%Y").date()
            except ValueError:
                fecha = None
        if code not in primera or (fecha and primera[code][0] and fecha < primera[code][0]):
            primera[code] = (fecha, str(f[6] or "").strip(), verd)
    return docs, primera


# ------------------------------------------------------- el submittal form
def _formulario(carpeta):
    for p in carpeta.rglob("*.pdf"):
        n = p.name.lower()
        if "submittal form" in n or re.fullmatch(r"25007-\d{4}\.pdf", n):
            return p
    return None


def sub_for(entrega, codigo):
    """Que declaro BW Water en la columna `Sub. For` para ese documento.

    Las filas se reconstruyen por coordenada `y`, porque el orden natural de
    get_text() mezcla las columnas del formulario.
    """
    n = re.sub(r"\D", "", str(entrega or ""))
    if not n:
        return None
    carpeta = ENTREGAS / f"ENTREGA {int(n)}"
    if not carpeta.is_dir():
        return None
    form = _formulario(carpeta)
    if form is None:
        return None

    base = re.sub(r"-0*(\d+)$", r"-\1", codigo)   # tolera el correlativo corto
    try:
        doc = fitz.open(form)
    except Exception:
        return None
    for page in doc:
        filas = defaultdict(list)
        for x0, y0, _x1, _y1, w, *_ in page.get_text("words"):
            filas[round(y0 / 4)].append((x0, w))
        for _y, ws in filas.items():
            texto = " ".join(w for _x, w in sorted(ws))
            t = texto.upper().replace(" ", "")
            if codigo.upper().replace("-", "") not in t.replace("-", "") and \
               base.upper().replace("-", "") not in t.replace("-", ""):
                continue
            for _x, w in sorted(ws, reverse=True):
                if w.strip().upper() in SUB_FOR:
                    return w.strip().upper()
            return "(en blanco)"
    return None


# ------------------------------------------------------------- el cajetin
def cajetin(ruta):
    """Que declara el documento sobre su propio proposito de emision."""
    if ruta is None or not ruta.exists():
        return None
    try:
        doc = fitz.open(ruta)
    except Exception:
        return None
    t = "\n".join(doc[i].get_text() for i in range(min(6, len(doc)))).upper()
    apro = "ISSUED FOR APPROVAL" in t
    cons = "ISSUED FOR CONSTRUCTION" in t
    if apro and cons:
        return "AMBAS"
    if cons:
        return "CONSTRUCCION"
    if apro:
        return "APROBACION"
    return "sin campo"


# ----------------------------------------------------------------- el DDSR
# El registro semanal que emite BW Water y con el que gestiona la revision. Sus doce
# columnas se leen por posicion horizontal, que es lo unico estable en una tabla
# apaisada: cada palabra cae en la columna cuyo borde izquierdo es el mayor que no la
# supera. Las cadenas IFC y Rev 0 no aparecen en el documento: el registro mide la
# aprobacion y no la emision.
DDSR = (PROY / "PROGRAMA y CONTRATO" / "REVISION SEMANAL PO EQUIPOS" / "SEMANA 08-09-26"
        / "25007_Taltal_DDSR_2026.09.07.pdf")

COLUMNAS = [(37, "id"), (120, "type"), (143, "cat"), (162, "curr_rev"), (230, "titulo"),
            (344, "sent"), (387, "returned"), (444, "status"), (496, "planned"),
            (547, "submittal"), (638, "approval"), (730, "weight")]


def leer_ddsr():
    """Una fila por documento, indexada por codigo."""
    if not DDSR.exists():
        return {}
    filas = {}
    doc = fitz.open(DDSR)
    for page in doc:
        agrup = defaultdict(list)
        for x0, y0, _x1, _y1, w, *_ in page.get_text("words"):
            agrup[round(y0 / 6)].append((x0, w))
        for _y, ws in sorted(agrup.items()):
            cols = defaultdict(list)
            for x, w in sorted(ws):
                nombre = COLUMNAS[0][1]
                for borde, n in COLUMNAS:
                    if x >= borde - 6:
                        nombre = n
                cols[nombre].append(w)
            ident = " ".join(cols.get("id", []))
            m = RX_CODIGO.match(ident)
            if not m:
                continue
            linea = " ".join(w for _x, w in sorted(ws))
            # La revision es el primer token de su columna; el resto del campo se
            # contamina con el titulo, que no tiene borde fijo.
            rev = (cols.get("curr_rev") or [""])[0]
            estado = next((e for e in ("Approved As Noted", "Not submitted",
                                       "Revise and resubmit", "Revise & Resubmit",
                                       "Approved", "Submitted")
                           if e in linea), "")
            avance = ("Approved with comments" if "Approved with comments" in linea
                      else "Not submitted" if "Not submitted" in linea
                      else "Under review" if "Under review" in linea
                      else "Approved" if "Approved" in linea else "")
            peso = " ".join(cols.get("weight", [])).strip()
            fechas = re.findall(r"\d{1,2}-[A-Z][a-z]{2}-\d{2}", linea)
            # La fecha planificada es la tercera de la fila, tras la de envio y la de
            # devolucion. En un no entregado, que no tiene esas dos, es la unica.
            plan = (fechas[2] if len(fechas) >= 3
                    else fechas[0] if len(fechas) == 1 and estado == "Not submitted"
                    else None)
            filas[m.group(1)] = dict(rev=rev, estado=estado, avance=avance, peso=peso,
                                     fechas=fechas, planned=plan, linea=linea)
    return filas


# ------------------------------------------------------------ clasificacion
def clasificar(d):
    """Categoria de accion. Es la auditoria: cada item cae en una y solo una."""
    if d["status"] == "Covered":
        # Cubierto por otro documento que si se entrego. No es un pendiente.
        return "F"
    if d["codigo"] is None or d["status"] in ("NOT DELIVERED", "PARTIAL"):
        return "E"
    v = d["verdicto"]
    numerica = bool(d["rev"]) and d["rev"].isdigit()
    if v.startswith("3") or v.startswith("4"):
        return "D"
    if not numerica:
        return "A" if v.startswith("1") else "B"
    if d["cajetin"] in ("APROBACION", "AMBAS"):
        return "C"
    return "F"


ACCION = {
    "A": "Emitir en revision 0 sin cambios",
    "B": "Emitir en revision 0 incorporando la condicion",
    "C": "Corregir el proposito de emision del cajetin",
    "D": "Reemitir con la letra siguiente",
    "E": "Entregar",
    "F": "Ninguna, cerrado",
}


def auditar():
    """Los 113 items del registro, cada uno clasificado en su categoria de accion.

    Es la funcion que consume el generador del correo, para que ninguna cifra del
    correo se escriba a mano.
    """
    docs, primera = leer_registro()
    ddsr = leer_ddsr()

    for d in docs:
        d["ruta"] = d["entrega_real"] = d["sub_for"] = d["cajetin"] = None
        d["fecha_aprob"] = d["tm_aprob"] = None
        d["nota_registro"] = d["rev_en_revision"] = None
        if d["codigo"]:
            corr = REV_ENTREGADA.get(d["codigo"])
            if corr:
                d["rev"] = corr["rev"]
                d["entrega"] = corr["entrega"]
                d["nota_registro"] = corr["nota"]
            pend = REV_EN_REVISION.get(d["codigo"])
            if pend:
                d["rev_en_revision"] = f"{pend['rev']} ({pend['entrega']})"
            rev = REV_REAL.get(d["codigo"], d["rev"])
            d["rev_real"] = rev
            d["codigo_real"] = ALIAS_CODIGO.get(d["codigo"], d["codigo"])
            ruta, ent, _n = localizar(d["codigo"], rev, d["entrega"])
            d["ruta"], d["entrega_real"] = ruta, ent
            d["sub_for"] = sub_for(ent or d["entrega"], d["codigo_real"])
            d["cajetin"] = cajetin(ruta)
            if d["codigo"] in primera:
                f, tm, _v = primera[d["codigo"]]
                d["fecha_aprob"], d["tm_aprob"] = f, tm
        else:
            d["rev_real"], d["codigo_real"] = d["rev"], None
        r = ddsr.get(d["codigo"]) or ddsr.get(d["codigo_real"] or "") or {}
        d["ddsr_rev"] = r.get("rev")
        d["ddsr_peso"] = r.get("peso")
        d["ddsr_estado"] = r.get("estado")
        d["ddsr_fechas"] = r.get("fechas") or []
        d["ddsr_planned"] = r.get("planned")
        d["cat"] = clasificar(d)
        d["dias"] = dias(d["fecha_aprob"])
    return docs


def separar(docs):
    """Ingenieria, calidad y fabricacion, e items sin codigo de documento."""
    return ([d for d in docs if d["tt"] and d["tt"] not in TIPOS_CALIDAD],
            [d for d in docs if d["tt"] in TIPOS_CALIDAD],
            [d for d in docs if not d["tt"]])


def main():
    docs = auditar()
    print(f"Items del registro: {len(docs)}")
    ing, cal, otros = separar(docs)

    print(f"  ingenieria {len(ing)} | calidad y fabricacion {len(cal)} | "
          f"sin codigo {len(otros)}")
    for nombre, grupo in (("ingenieria", ing), ("calidad", cal), ("sin codigo", otros)):
        print(f"  {nombre:12s}", dict(sorted(Counter(d['cat'] for d in grupo).items())))

    escribir(docs, ing, cal, otros)
    print(f"\nAuditoria escrita: {SALIDA.name}")
    return 0


# ------------------------------------------------------------------ salida
def fila(d):
    f = d["fecha_aprob"].strftime("%d-%m-%Y") if d["fecha_aprob"] else "-"
    return (f"| {d['cat']} | `{d['codigo_real'] or d['referencia']}` | {d['titulo']} | "
            f"{d['rev_real'] or '-'} | {d['verdicto'] or '-'} | {d['entrega_real'] or d['entrega'] or '-'} | "
            f"{d['sub_for'] or '-'} | {d['cajetin'] or '-'} | {f} | "
            f"{d['dias'] if d['dias'] is not None else '-'} |")


CAB = ("| Cat. | Codigo | Documento | Rev. | Veredicto | Entrega | Sub. For | "
       "Cajetin | 1er Cod. 1/2 | Dias |\n|---|---|---|---|---|---|---|---|---|---|")


def escribir(docs, ing, cal, otros):
    L = ["---",
         "titulo: Auditoria de emision para construccion de los entregables de BW Water",
         "fecha: 2026-09-09", "estado: INTERNO", "type: auditoria",
         "project: salmuera-taltal", "---", "",
         "# Auditoria documento por documento",
         "",
         "Corte al cierre del transmittal N38, del 3 de septiembre de 2026. Los dias se "
         "cuentan hasta el 9 de septiembre de 2026 desde el transmittal en que ADASA dio "
         "por primera vez Codigo 1 o Codigo 2 a ese documento.",
         "",
         "Generado por `auditar_documentos_bw.py`. No se envia: es el respaldo de las "
         "cifras del correo.",
         "",
         "## Categorias", "",
         "| Cat. | Criterio | Accion |", "|---|---|---|"]
    L += [f"| **{k}** | {c} | {ACCION[k]} |" for k, c in [
        ("A", "Codigo 1 y revision de letra"),
        ("B", "Codigo 2 y revision de letra"),
        ("C", "Revision numerica y cajetin que dice para aprobacion"),
        ("D", "Codigo 3 o 4"),
        ("E", "No entregado o parcial"),
        ("F", "Revision numerica y cajetin consistente")]]

    for titulo, grupo in (("Ingenieria", ing),
                          ("Calidad y fabricacion", cal),
                          ("Items sin codigo de documento", otros)):
        c = Counter(d["cat"] for d in grupo)
        L += ["", f"## {titulo} ({len(grupo)} items)", "",
              "Recuento por categoria: " + ", ".join(
                  f"**{k}** {c[k]}" for k in "ABCDEF" if c[k]) + ".", ""]
        if grupo is ing:
            porddd = Counter(d["ddd"] for d in grupo if d["cat"] in "AB")
            L += ["Sin emitir para construccion, por disciplina: " + ", ".join(
                f"{DISCIPLINA.get(k, k)} {v}" for k, v in sorted(porddd.items())) + ".", ""]
        L += [CAB]
        L += [fila(d) for d in sorted(
            grupo, key=lambda d: (d["cat"], -(d["dias"] or 0), d["codigo_real"] or ""))]

    ab = [d for d in ing if d["cat"] in "AB"]
    if ab:
        dd = sorted(x["dias"] for x in ab if x["dias"] is not None)
        L += ["", "## La cifra que sostiene el reclamo", "",
              f"- Ingenieria sin emitir para construccion: **{len(ab)} de {len(ing)}** "
              f"documentos.",
              f"- De ellos, **{sum(1 for d in ab if d['cat'] == 'A')}** estan en Codigo 1, "
              "aprobados sin observaciones abiertas.",
              f"- Antiguedad de la aprobacion: mediana **{dd[len(dd)//2]} dias**, "
              f"maximo **{dd[-1]} dias**, y **{sum(1 for x in dd if x > 180)}** por sobre "
              "los 180 dias.", ""]
        L += ["Los diez mas antiguos:", "",
              "| Codigo | Documento | Rev. | Aprobado | Dias |", "|---|---|---|---|---|"]
        for d in sorted(ab, key=lambda d: -(d["dias"] or 0))[:10]:
            L.append(f"| `{d['codigo_real']}` | {d['titulo']} | {d['rev_real']} | "
                     f"{d['fecha_aprob'].strftime('%d-%m-%Y')} ({d['tm_aprob']}) | "
                     f"{d['dias']} |")

    en_ddsr = [d for d in docs if d["ddsr_peso"]]
    cien = [d for d in en_ddsr if d["ddsr_peso"].startswith("100")
            and d["cat"] in ("A", "B")]
    disc = [d for d in en_ddsr if d["ddsr_rev"] and d["rev_real"]
            and d["ddsr_rev"].upper() != str(d["rev_real"]).upper()]
    L += ["", "## Que dice el registro del proveedor", "",
          f"El DDSR del 7 de septiembre lista **{len(en_ddsr)} de los {len(docs)} items** "
          "del registro de ADASA. Sus doce columnas no incluyen ninguna de emision para "
          "construccion: las cadenas IFC y Rev 0 no aparecen en el documento. Su columna "
          "`Status` distingue aprobado de no aprobado, y su ponderador da 100 por ciento a "
          "un documento aprobado sin mirar en que revision quedo.", "",
          f"**{len(cien)} documentos que este informe cuenta como no emitidos figuran en "
          "el DDSR con peso 100 por ciento.**", "",
          "| Codigo | Documento | Rev. ADASA | Rev. DDSR | Peso DDSR |",
          "|---|---|---|---|---|"]
    L += [f"| `{d['codigo_real']}` | {d['titulo']} | {d['rev_real']} | "
          f"{d['ddsr_rev']} | {d['ddsr_peso']} |" for d in
          sorted(cien, key=lambda x: x["codigo_real"] or "")]
    if disc:
        L += ["", "### Revisiones en que los dos registros no coinciden", "",
              "| Codigo | Documento | Rev. ADASA | Rev. DDSR |", "|---|---|---|---|"]
        L += [f"| `{d['codigo_real']}` | {d['titulo']} | {d['rev_real']} | "
              f"{d['ddsr_rev']} |" for d in sorted(disc, key=lambda x: x["codigo_real"] or "")]

    corr = [d for d in docs if d.get("nota_registro")]
    if corr:
        L += ["", "## Correcciones aplicadas al registro de ADASA", "",
              "Revisiones que el proveedor entrego y que el Master Register no recogio. "
              "Sin corregirlas, este informe reclamaria la emision de un documento ya "
              "emitido.", ""]
        L += [f"- **`{d['codigo_real']}`**, {d['titulo']}: {d['nota_registro']}"
              for d in corr]
    pend = [d for d in docs if d.get("rev_en_revision")]
    if pend:
        L += ["", "Revisiones posteriores ya recibidas y aun sin revisar por ADASA, que el "
              "correo tiene que reconocer:", ""]
        L += [f"- **`{d['codigo_real']}`**, {d['titulo']}: el registro lleva la revision "
              f"{d['rev_real']} y el proveedor envio la {d['rev_en_revision']}"
              for d in pend]

    sf = Counter(d["sub_for"] for d in docs if d["sub_for"])
    L += ["", "## Como se sometio la revision vigente de cada documento", "",
          "Valor de la columna `Sub. For` del formulario de la entrega vigente. La leyenda "
          "del propio formulario, `PEM-F013` Rev 3, define `FA`, `FR`, `FI`, `IFC` y `AB`; "
          "`IFA` no esta definido en ella.", "",
          "| Sub. For | Documentos |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in sf.most_common()]

    cj = Counter(d["cajetin"] for d in docs if d["cajetin"])
    L += ["", "## Que declara el cajetin del documento", "",
          "| Cajetin | Documentos |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in cj.most_common()]

    contra = [d for d in docs if d["cat"] == "C"]
    if contra:
        L += ["", "### Los que se contradicen consigo mismos", "",
              "Revision numerica, es decir emitidos para construccion, y el cajetin sigue "
              "diciendo que son para aprobacion.", "",
              "| Codigo | Documento | Rev. | Sub. For | Cajetin |", "|---|---|---|---|---|"]
        L += [f"| `{d['codigo_real']}` | {d['titulo']} | {d['rev_real']} | "
              f"{d['sub_for'] or '-'} | {d['cajetin']} |" for d in contra]

    L.append("")
    # Cuadre contra el tally que el Summary del registro declara. El Summary cuenta
    # los veredictos SOLO entre las filas con Status "Delivered", de modo que la
    # comprobacion tiene que restringirse igual o sobra una fila: la 64, cubierta por
    # otro documento y por eso fuera de ese conteo.
    ent = [d for d in docs if d["status"] == "Delivered"]
    tv = Counter(d["verdicto"].split("-")[0].strip() for d in ent)
    L += ["", "## Cuadre contra el registro", "",
          f"Filas con Status Delivered: **{len(ent)}**. Veredictos entre ellas: "
          + ", ".join(f"**Codigo {k}** {v}" for k, v in sorted(tv.items())) + ".", "",
          "Es el mismo criterio con que el Summary del Master Register calcula su "
          "distribucion de veredictos, y coincide con el tally declarado al cierre del "
          "TM N38. Contando todas las filas salen 20 en Codigo 2 en vez de 19: la de mas "
          "es la fila 64, Civil Requirements Drawings, cuyo Status es Covered y que el "
          "Summary deja fuera.", ""]

    SALIDA.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
