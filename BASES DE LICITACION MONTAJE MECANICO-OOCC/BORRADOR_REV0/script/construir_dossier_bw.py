#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye el dossier de ingenieria de BW Water para el equipo de ADASA.

Fuente unica de la composicion: la lista VIGENCIA_BW de vigencia_bw.py, que produce
catalogar_ingenieria_bw.py desde el Master Deliverable Register. Idempotente: se
puede re-correr. NO toca ENTREGAS_BWWATER, que es el archivo de lo recibido.

Reglas:
  - Solo PDF. BW Water no entrego listados en formato nativo, de modo que no hay
    otra cosa que llevar.
  - Cada copia se verifica por SHA256 contra su fuente.
  - Una sola revision por codigo, la ultima aprobada por ADASA.
  - Nombre uniforme <codigo>_<rev> <titulo>, porque el proveedor usa seis grafias
    distintas para la revision y el dossier tiene que poder ordenarse.
  - Nada del paquete de calidad y fabricacion, ni archivos de trabajo interno.

Uso:
    python construir_dossier_bw.py
"""
import hashlib
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vigencia_bw import VIGENCIA_BW  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# La raiz se deriva de la ubicacion del script, que vive en
# <PROY>/BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/script/.
PROY = Path(__file__).resolve().parents[3]
BL = PROY / "BASES DE LICITACION MONTAJE MECANICO-OOCC"
ENTREGAS = PROY / "ENTREGAS_BWWATER"
PKG = BL / "INGENIERIA MODULO BW WATER"
NOTA = (BL / "NOTAS_TECNICAS" / "P22-NT-06-000-002-0"
        / "P22-NT-06-000-002-0_Ingenieria-Modulo-BW-Water_ADASA.pdf")

CONTROL = "0. CONTROL DE CAMBIOS"

errores, copiados = [], 0

# Caracteres que Windows no admite en un nombre de archivo.
RX_INVALIDO = re.compile(r'[<>:"/\\|?*]')


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def cp(src: Path, dst_dir: Path, nuevo_nombre: str = None):
    """Copia verificando por SHA256. Devuelve True si quedo igual a la fuente."""
    global copiados
    if not src.exists():
        errores.append(f"FALTA FUENTE: {src}")
        return False
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / (nuevo_nombre or src.name)
    shutil.copy2(src, dst)
    if sha(src) != sha(dst):
        errores.append(f"SHA256 NO COINCIDE: {dst}")
        return False
    copiados += 1
    return True


def nombre_destino(codigo, rev, titulo):
    """<codigo>_<rev> <titulo>.pdf, en una sola grafia para todo el dossier."""
    t = RX_INVALIDO.sub("-", titulo).strip()
    t = re.sub(r"\s+", " ", t)
    return f"{codigo}_{rev} {t}.pdf"


def limpiar(carpeta: Path):
    """Vacia el arbol de documentos para que la corrida sea idempotente.

    Se borran solo los PDF y los LEEME que el propio script escribe; nunca se
    toca nada fuera de PKG.
    """
    if not carpeta.is_dir():
        return
    for p in carpeta.rglob("*"):
        if p.is_file() and p.suffix.lower() == ".pdf":
            p.unlink()
        elif p.is_file() and p.name == "LEEME.txt":
            p.unlink()


def dossiers():
    """Copia cada documento a la carpeta de su especialidad."""
    for codigo, titulo, rev, _e, _tm, _v, dossier, ruta in VIGENCIA_BW:
        cp(ENTREGAS / ruta, PKG / dossier, nombre_destino(codigo, rev, titulo))


def dossier_control():
    """0. CONTROL DE CAMBIOS: la nota tecnica que explica el dossier."""
    if NOTA.exists():
        cp(NOTA, PKG / CONTROL)
    else:
        print(f"    (aun sin PDF de la nota tecnica en {NOTA.parent.name})")


# ---------------------------------------------------------------------------
# Lo propio de cada especialidad, en texto plano y sin tildes para que sobreviva a
# cualquier descompresor. Es lo unico que se escribe a mano; el resto del LEEME se
# arma desde el catalogo.
FECHA = "09-09-2026"

QUE_MIRAR = {
    "1. GENERAL": [
        "La hoja de datos del contenedor fija sus dimensiones y su peso de operacion,",
        "que son la entrada de la fundacion. La ingenieria civil ya recogio el cambio de",
        "nivel: el modulo subio 250 mm respecto de la que se cotizo.",
    ],
    "2. PROCESO": [
        "El P&ID en revision 0 y el listado de lineas en revision 1 son los dos documentos",
        "que gobiernan el proceso. Las presiones de diseno y de prueba de cada linea las",
        "fija el listado de lineas, no el plan de ensayos.",
        "",
        "La filosofia de control cambio de titulo al pasar a revision 1 y el proveedor la",
        "emite como Control Narrative. Es el mismo documento y el mismo codigo.",
    ],
    "3. MECANICA": [
        "El plano de necesidades civiles y cargas es el que alimenta la ingenieria de",
        "fundaciones. Esta en revision B y en codigo 2.",
        "",
        "El informe de calculo estructural del bastidor esta en revision B y en codigo 2, y",
        "no lleva endoso de un profesional inscrito en Chile. El proveedor lo comprometio",
        "por escrito y a la fecha no ha designado a quien lo firme.",
        "",
        "Los dos planos generales de los turbocargadores son revision A y llegaron una sola",
        "vez. El registro de ADASA los anota en revision B, que no existe en el repositorio;",
        "aqui rige lo que dice el cajetin de cada plano.",
    ],
    "4. CANERIAS": [
        "Son las dos especificaciones del proveedor: la de cañerias en revision A y la de",
        "pintura en revision C. El registro de ADASA las anota en la disciplina mecanica y",
        "el documento emitido dice cañerias; manda el documento.",
    ],
    "5. ELECTRICIDAD": [
        "El diagrama unifilar, el listado de cargas y el programa de cables de poder estan",
        "en revision 0, emitidos para construccion.",
        "",
        "La hoja de datos del tablero local fija su envolvente en acero inoxidable 316L sin",
        "pintar, NEMA 4X. Es el documento que gobierna la materialidad del exterior.",
    ],
    "6. CONTROL E INSTRUMENTACION": [
        "El listado de I/O en revision 6 y el listado de instrumentos en revision F son los",
        "que gobiernan la interfaz de control.",
        "",
        "El rango vinculante del transmisor de vibracion VT-09-001 es de 0 a 12 mm/s rms,",
        "declarado por ADASA. El listado de instrumentos todavia arrastra 8,9 y su correccion",
        "queda pendiente para la revision 0.",
    ],
}

TITULO_DOSSIER = {
    "1. GENERAL": "documentacion general",
    "2. PROCESO": "proceso y P&ID",
    "3. MECANICA": "mecanica, disposicion y calculo",
    "4. CANERIAS": "cañerias y pintura",
    "5. ELECTRICIDAD": "electricidad",
    "6. CONTROL E INSTRUMENTACION": "control e instrumentacion",
}


def escribir_leeme():
    """Un LEEME por especialidad, armado desde el catalogo."""
    for dossier in sorted({f[6] for f in VIGENCIA_BW}):
        filas = sorted([f for f in VIGENCIA_BW if f[6] == dossier], key=lambda f: f[0])
        c1 = sum(1 for f in filas if f[5] == "1")
        c2 = len(filas) - c1

        L = [f"{dossier} - ingenieria del modulo, {TITULO_DOSSIER[dossier]}",
             f"Fecha: {FECHA}", "=" * 80, "", "CONTENIDO",
             f"  {len(filas)} documentos, cada uno en la ultima revision que ADASA aprobo.",
             ""]
        ancho = max(len(f[0]) for f in filas)
        for codigo, titulo, rev, entrega, tm, _v, _d, _r in filas:
            L.append(f"  {codigo:<{ancho}}  rev {rev:<2}  {titulo}")
        L += ["", "QUE MIRAR"]
        L += ["  " + t if t else "" for t in QUE_MIRAR[dossier]]
        L += ["", "ESTADO DE EMISION"]
        if c2:
            L += [f"  {c1} en codigo 1, aprobados sin observaciones.",
                  f"  {c2} en codigo 2: aprobados con observaciones que el proveedor incorpora",
                  "  al emitir la revision 0. Un documento en codigo 2 rige, y va a cambiar en",
                  "  su detalle.",
                  "",
                  "  La nota tecnica de la carpeta 0 dice, documento por documento, cual es la",
                  "  observacion que queda abierta."]
        else:
            L += [f"  Los {c1} documentos estan en codigo 1, aprobados sin observaciones."]
        L.append("")
        (PKG / dossier).mkdir(parents=True, exist_ok=True)
        (PKG / dossier / "LEEME.txt").write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------------------
def gate_vigencia():
    """Contrasta lo declarado contra el arbol real, en los dos sentidos."""
    archivos = [p for p in PKG.rglob("*.pdf") if CONTROL not in p.parts]
    porcodigo = defaultdict(list)
    for p in archivos:
        m = re.match(r"(P22-[A-Z]+-09-\d{3}-\d{2,3})_([0-9A-Z]+)\s", p.name)
        if m:
            porcodigo[m.group(1)].append((m.group(2), p))
        else:
            errores.append(f"NOMBRE FUERA DE CONVENCION: {p.name}")

    declarados = set()
    for codigo, _t, rev, _e, _tm, _v, dossier, _r in VIGENCIA_BW:
        declarados.add(codigo)
        hallados = porcodigo.get(codigo, [])
        if not hallados:
            errores.append(f"{codigo}: declarado y sin archivo en el dossier")
            continue
        revs = {r for r, _p in hallados}
        if revs != {rev}:
            errores.append(f"{codigo}: se declara revision {rev} y el dossier tiene "
                           f"{sorted(revs)}")
        for _r, p in hallados:
            if p.parent.name != dossier:
                errores.append(f"{codigo}: declarado en {dossier} y esta en "
                               f"{p.parent.name}")

    for codigo in porcodigo:
        if codigo not in declarados:
            errores.append(f"{codigo}: en el dossier y no declarado en el catalogo")


def autochequeo():
    """Reglas duras del dossier, verificadas sobre el arbol final."""
    archivos = [p for p in PKG.rglob("*") if p.is_file() and p.name != "LEEME.txt"]

    for p in archivos:
        if p.suffix.lower() != ".pdf":
            errores.append(f"FORMATO QUE NO CORRESPONDE: {p.name}")
        if re.match(r"P22-(BA|PP|MTC)-", p.name):
            errores.append(f"DOCUMENTO DE CALIDAD Y FABRICACION: {p.name}")
        b = p.name.lower()
        for d in ("cc_adasa", "cc adasa", "_extracted", "_ocr", "_ccs", "client copy"):
            if d in b:
                errores.append(f"ARCHIVO DE TRABAJO INTERNO: {p.name}")

    for dossier, n in sorted(Counter(f[6] for f in VIGENCIA_BW).items()):
        reales = len(list((PKG / dossier).glob("*.pdf"))) if (PKG / dossier).is_dir() else 0
        if reales != n:
            errores.append(f"{dossier}: se declaran {n} documentos y hay {reales}")

    if not errores:
        docs = len({f[0] for f in VIGENCIA_BW})
        print(f"Autochequeo OK: {docs} codigos, una revision cada uno; solo PDF; "
              f"sin calidad y fabricacion; sin archivos de trabajo interno.")


def main():
    if not ENTREGAS.is_dir():
        sys.exit(f"ERROR: no existe {ENTREGAS}")
    limpiar(PKG)
    dossiers()
    dossier_control()
    escribir_leeme()
    print(f"Archivos copiados y verificados por SHA256: {copiados}")

    gate_vigencia()
    autochequeo()

    total = sum(1 for p in PKG.rglob("*") if p.is_file())
    print(f"Archivos en el dossier: {total}")

    if errores:
        print(f"\nERRORES ({len(errores)}):")
        for e in errores:
            print("  -", e)
        return 1
    print("Sin errores.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
