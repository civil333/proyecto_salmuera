#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Catalogo de la ingenieria de BW Water que va al dossier del equipo.

Lee el Master Deliverable Register, que es donde vive el estado actual de cada
entregable, se queda con la ingenieria y localiza el archivo fisico de la revision
vigente de cada documento dentro de ENTREGAS_BWWATER.

Emite `vigencia_bw.py` con la lista VIGENCIA_BW, que a partir de ahi es la fuente
unica del dossier: la usan el constructor y el generador de la nota tecnica.

Que se deja fuera y por que:
  - Tipos BA y PP: paquete de calidad y fabricacion, no es ingenieria.
  - Tipo MTC: el organigrama del proveedor.
  - El modelo 3D de Navisworks: es ingenieria y esta aprobado, pero el dossier
    lleva solo formatos finales de lectura.
  - Los archivos derivados de la revision de ADASA (_CC_ADASA, _extracted, _OCR,
    _CCS, Client Copy), que son trabajo interno y no entregables del proveedor.

Uso:
    python catalogar_ingenieria_bw.py            escribe vigencia_bw.py
    python catalogar_ingenieria_bw.py --informe  solo informa, no escribe
"""
import re
import sys
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook

# Algun nombre de archivo del proveedor trae espacios de ancho cero; la consola
# de Windows es cp1252 y aborta al imprimirlos.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# La raiz se deriva de la ubicacion del script, que vive en
# <PROY>/BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/script/.
PROY = Path(__file__).resolve().parents[3]
REGISTRO = (PROY / "REVISIONES" / "EVALUACIONES"
            / "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
ENTREGAS = PROY / "ENTREGAS_BWWATER"
SALIDA = Path(__file__).resolve().parent / "vigencia_bw.py"

# ---------------------------------------------------------------------------
# Dossiers, uno por disciplina de la Tabla 2-4 de la codificacion general del
# proyecto (P00-IT-00-000-101), que es la que asigna el campo DDD del codigo.
D_GEN = "1. GENERAL"
D_PRO = "2. PROCESO"
D_MEC = "3. MECANICA"
D_CAN = "4. CANERIAS"
D_ELE = "5. ELECTRICIDAD"
D_CTL = "6. CONTROL E INSTRUMENTACION"

DOSSIER_POR_DISCIPLINA = {
    "000": D_GEN,
    "009": D_PRO,
    "005": D_MEC,
    "006": D_CAN,
    "007": D_ELE,
    "008": D_CTL,
    "004": D_CTL,   # la arquitectura del sistema de control acompana a su disciplina
}

# Codigos en que el registro y el documento emitido difieren. Manda el documento
# emitido, que es el que el equipo va a tener en la mano; la nota tecnica lo declara.
#
#   Las dos especificaciones: el registro las anota en la disciplina mecanica y el
#   documento dice 006, canerias.
#
#   Los tres datasheets de estanques: el registro tiene la familia corrida en un
#   correlativo. Titulo y entrega del registro calzan exactos con el archivo, de
#   modo que lo unico desplazado es el codigo.
ALIAS_CODIGO = {
    "P22-ET-09-005-001": "P22-ET-09-006-001",   # Especificacion de canerias
    "P22-ET-09-005-002": "P22-ET-09-006-002",   # Especificacion de pintura
    "P22-ET-09-009-010": "P22-ET-09-009-009",   # Estanque CIP
    "P22-ET-09-009-011": "P22-ET-09-009-010",   # Estanque de antiescalante
    "P22-ET-09-009-014": "P22-ET-09-009-011",   # Calentador del estanque CIP
}

# Revisiones en que el registro y el cajetin del documento difieren. Los dos planos
# generales de los turbocargadores llegaron una sola vez, en la E18, y su cajetin dice
# "Revision No.: A" mientras el registro los anota en B. No hay revision B en el
# repositorio, de modo que lo que existe y lo que viaja es la A.
REV_REAL = {
    "P22-DWG-09-005-012": "A",   # Plano general del turbocargador de alimentacion
    "P22-DWG-09-005-013": "A",   # Plano general del turbocargador interetapa
}

# Ingenieria que no viaja, con el motivo.
EXCLUIDOS = {
    "P22-DWG-09-005-007": "modelo 3D de Navisworks, formato fuera del dossier",
}

TIPOS_FUERA = {"BA", "PP", "MTC"}   # calidad y fabricacion, y el organigrama

# Sufijos que delatan un archivo de trabajo interno de ADASA, no del proveedor.
DERIVADOS = ("_cc_adasa", "cc adasa", "(cc", "_extracted", "_ocr", "_ccs",
             "client copy", "_cc.", " cc.", "_comentado")

RX_CODIGO = re.compile(r"^(P22-([A-Z]+)-09-(\d{3})-(\d{2,3}))")


def norm_rev(v):
    """Revision en su forma canonica. El registro escribe '0', 'Rev 0', 'B' y 'Rev C'."""
    if v is None:
        return None
    s = str(v).strip().upper().replace("REV.", "").replace("REV", "").strip()
    return s or None


def variantes_codigo(codigo):
    """El codigo tal cual y su forma con correlativo de dos digitos.

    Cinco documentos llevan NNN de dos digitos en el nombre del archivo, entre
    ellos el PFD (P22-DWG-09-009-01), y el propio registro anota alguno asi.
    """
    v = [codigo]
    m = RX_CODIGO.match(codigo)
    if m:
        tt, ddd, nnn = m.group(2), m.group(3), m.group(4)
        tres = nnn.zfill(3)
        for alt in (f"P22-{tt}-09-{ddd}-{tres}",
                    f"P22-{tt}-09-{ddd}-{tres[1:]}",        # 001 -> 01
                    f"P22-{tt}-09-{ddd}-{tres.lstrip('0') or '0'}"):
            if alt not in v:
                v.append(alt)
    return v


def revs_en_nombre(stem, codigo):
    """Revisiones que el nombre del archivo declara despues del codigo.

    Seis grafias conviven en las entregas del proveedor: _A, -A, _Rev.C, RevA
    pegado, _REV.B, y el archivo que no la trae. Se devuelve el conjunto de
    candidatas para no depender de cual uso el proveedor ese dia. Se corta por la
    variante de codigo que aparece en el nombre, que no siempre es la del registro:
    hay archivos con el correlativo en dos digitos.
    """
    su = stem.upper()
    i, largo = -1, 0
    for v in variantes_codigo(codigo):
        j = su.find(v.upper())
        if j >= 0 and len(v) > largo:
            i, largo = j, len(v)
    resto = stem[i + largo:] if i >= 0 else stem
    cands = set()
    m = re.match(r"^[\s_.-]*(?:REV\.?\s*)?([0-9A-F])(?![0-9A-Z])", resto, re.I)
    if m:
        cands.add(m.group(1).upper())
    for m in re.finditer(r"REV\.?\s*([0-9A-F])(?![0-9A-Z])", resto, re.I):
        cands.add(m.group(1).upper())
    # Desde la E65 el proveedor tambien cierra el nombre con la revision: "_0", "_r1".
    # Se exige el guion bajo para no confundirla con el sufijo de exportacion "-006".
    m = re.search(r"_r?([0-9A-F])$", stem, re.I)
    if m:
        cands.add(m.group(1).upper())
    return cands


def es_derivado(nombre):
    b = nombre.lower()
    return any(d in b for d in DERIVADOS)


def candidatos(carpeta, codigo, recursivo=True):
    it = carpeta.rglob("*.pdf") if recursivo else carpeta.glob("*.pdf")
    variantes = variantes_codigo(codigo)
    return [p for p in it
            if any(v.upper() in p.stem.upper() for v in variantes)
            and not es_derivado(p.name)]


def elegir(cands, codigo, rev):
    """De los candidatos, el de la revision buscada. Devuelve (path, nota)."""
    if not cands:
        return None, ""
    exactos = [p for p in cands if rev in revs_en_nombre(p.stem, codigo)]
    if len(exactos) == 1:
        return exactos[0], ""
    if len(exactos) > 1:
        # Varias copias de la misma revision: se toma la de nombre mas corto,
        # que es la del proveedor sin sufijos agregados despues.
        return sorted(exactos, key=lambda p: len(p.name))[0], "habia mas de una copia"
    if len(cands) == 1:
        return cands[0], f"el nombre no declara la revision {rev}"
    return None, (f"{len(cands)} candidatos y ninguno declara la revision {rev}: "
                  + ", ".join(sorted(p.name for p in cands)[:3]))


def entrega_de(ruta):
    """Entrega a la que pertenece un archivo, leida de su carpeta."""
    for parte in ruta.relative_to(ENTREGAS).parts:
        m = re.match(r"ENTREGA (\d+)$", parte)
        if m:
            return f"E{int(m.group(1))}"
    return "-"


def localizar(codigo, rev, entrega):
    """Archivo PDF de esa revision del documento.

    Se busca primero en la entrega que declara el registro. Si ahi no esta, se
    barre el resto del arbol, porque el registro apunta al menos una vez a una
    entrega que no existe. Devuelve (path, entrega real, nota).
    """
    codigo = ALIAS_CODIGO.get(codigo, codigo)
    n = re.sub(r"\D", "", str(entrega or ""))
    carpeta = ENTREGAS / f"ENTREGA {int(n)}" if n else None

    if carpeta is not None and carpeta.is_dir():
        ruta, nota = elegir(candidatos(carpeta, codigo), codigo, rev)
        if ruta is not None:
            return ruta, entrega_de(ruta), nota

    # Barrido del arbol completo, saltando las carpetas de layouts preliminares,
    # que no son submittals.
    todos = [p for p in candidatos(ENTREGAS, codigo)
             if not p.relative_to(ENTREGAS).parts[0].upper().startswith("PRELIMINAR")]
    ruta, nota = elegir(todos, codigo, rev)
    if ruta is None:
        return None, None, nota or f"sin PDF de {codigo} en revision {rev}"
    real = entrega_de(ruta)
    extra = f"el registro lo declara en {entrega} y el archivo esta en {real}"
    return ruta, real, f"{extra}; {nota}" if nota else extra


def leer_registro():
    """Filas de ingenieria del Master Register, en el orden en que estan."""
    ws = load_workbook(REGISTRO, read_only=True, data_only=True)["Master Register"]
    docs = []
    for f in list(ws.values)[1:]:
        if not f or not f[2]:
            continue
        code = str(f[2]).strip()
        m = RX_CODIGO.match(code)
        if not m or m.group(2) in TIPOS_FUERA:
            continue
        docs.append(dict(codigo=m.group(1), tt=m.group(2), ddd=m.group(3),
                         titulo=str(f[1]).strip(), rev=norm_rev(f[3]),
                         entrega=str(f[4]).strip(), tm=str(f[5]).strip(),
                         verdicto=str(f[6]).strip()))
    return docs


def catalogar():
    docs = leer_registro()
    filas, sin_resolver, notas = [], [], []

    for d in docs:
        if d["codigo"] in EXCLUIDOS:
            continue
        real = ALIAS_CODIGO.get(d["codigo"], d["codigo"])
        if real != d["codigo"]:
            notas.append(f"{d['codigo']} se emitio como {real}; manda el documento")
        ddd = RX_CODIGO.match(real).group(3)
        dossier = DOSSIER_POR_DISCIPLINA.get(ddd)
        if dossier is None:
            sin_resolver.append((d["codigo"], f"disciplina {ddd} sin dossier"))
            continue

        rev = REV_REAL.get(d["codigo"], d["rev"])
        if rev != d["rev"]:
            notas.append(f"{real}: el registro lo declara en revision {d['rev']} y su "
                         f"cajetin dice {rev}; manda el documento")

        ruta, entrega, nota = localizar(d["codigo"], rev, d["entrega"])
        if ruta is None:
            sin_resolver.append((d["codigo"], nota))
            continue
        if nota:
            notas.append(f"{real}: {nota} -> {ruta.name}")

        codigo_verdicto = "1" if d["verdicto"].startswith("1") else \
                          "2" if d["verdicto"].startswith("2") else d["verdicto"]
        filas.append((real, d["titulo"], rev, entrega, d["tm"],
                      codigo_verdicto, dossier,
                      str(ruta.relative_to(ENTREGAS)).replace("\\", "/")))

    return filas, sin_resolver, notas


CABECERA = '''# -*- coding: utf-8 -*-
"""Ingenieria de BW Water que compone el dossier del equipo. GENERADO, no editar a mano.

Lo produce catalogar_ingenieria_bw.py desde el Master Deliverable Register. Es la
fuente unica del dossier: la usan construir_dossier_bw.py y el generador de la
Nota Tecnica P22-NT-06-000-002-0.

Cada fila:
  (codigo, titulo, revision vigente, entrega, transmittal, codigo de respuesta,
   dossier, ruta relativa a ENTREGAS_BWWATER)
"""

D_GEN = "1. GENERAL"
D_PRO = "2. PROCESO"
D_MEC = "3. MECANICA"
D_CAN = "4. CANERIAS"
D_ELE = "5. ELECTRICIDAD"
D_CTL = "6. CONTROL E INSTRUMENTACION"

_D = {D_GEN: "D_GEN", D_PRO: "D_PRO", D_MEC: "D_MEC",
      D_CAN: "D_CAN", D_ELE: "D_ELE", D_CTL: "D_CTL"}

VIGENCIA_BW = [
'''


def escribir(filas):
    orden = [D_GEN, D_PRO, D_MEC, D_CAN, D_ELE, D_CTL]
    sim = {D_GEN: "D_GEN", D_PRO: "D_PRO", D_MEC: "D_MEC",
           D_CAN: "D_CAN", D_ELE: "D_ELE", D_CTL: "D_CTL"}
    partes = [CABECERA]
    for dossier in orden:
        grupo = sorted([f for f in filas if f[6] == dossier], key=lambda f: f[0])
        partes.append(f"    # ---- {dossier} ({len(grupo)} documentos)\n")
        for c, t, r, e, tm, v, _d, ruta in grupo:
            partes.append(f'    ({c!r}, {t!r}, {r!r}, {e!r}, {tm!r}, {v!r}, '
                          f'{sim[dossier]},\n     {ruta!r}),\n')
    partes.append("]\n")
    SALIDA.write_text("".join(partes), encoding="utf-8")


def main():
    if not REGISTRO.exists():
        sys.exit(f"ERROR: no existe el registro en {REGISTRO}")
    filas, sin_resolver, notas = catalogar()

    print(f"Documentos de ingenieria catalogados: {len(filas)}")
    for k, v in sorted(Counter(f[6] for f in filas).items()):
        print(f"    {k:32s} {v}")
    print("    codigos de respuesta:",
          dict(sorted(Counter(f[5] for f in filas).items())))

    if notas:
        print(f"\nNotas de la busqueda ({len(notas)}):")
        for n in notas:
            print("  -", n)

    for c, m in EXCLUIDOS.items():
        print(f"\nExcluido a proposito: {c} — {m}")

    if sin_resolver:
        print(f"\nSIN RESOLVER ({len(sin_resolver)}):")
        for c, m in sin_resolver:
            print("  -", c, "|", m)

    if "--informe" in sys.argv:
        print("\n(--informe: no se escribio el catalogo)")
        return 1 if sin_resolver else 0

    escribir(filas)
    print(f"\nCatalogo escrito: {SALIDA.name}")
    return 1 if sin_resolver else 0


if __name__ == "__main__":
    sys.exit(main())
