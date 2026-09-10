#!/usr/bin/env python3
"""
Construye `INGENIERIA VIGENTE PARA CONSTRUCCION`, el paquete de ingenieria que se
entrega al contratista adjudicado del montaje mecanico y las obras civiles de Taltal.

NO es un paquete de licitacion: el contrato esta adjudicado. No lleva Bases de
Licitacion ni Formato de Presupuesto. El documento contractual es el
`BL_MONTAJE_TALTAL_REV1` del 25-Jun-2026 que el contratista ya tiene.

Fuente unica de la composicion del paquete. Idempotente: se puede re-correr.
NO toca `Bases REV 0`, que queda como respaldo de lo que se licito.

Reglas:
  - PDF, XLSX, el modelo NWD y, desde el 10-09-2026, el DWG de cada plano. Sin .bak,
    sin .md, sin .log.
  - Cada plano viaja en PDF y en su archivo nativo DWG de la misma revision, en la misma
    carpeta y con el mismo nombre base. El DWG es el que viajo en la misma entrega que
    el PDF. Un DWG sin marca de lamina cubre todas las laminas del codigo (00-001-001);
    el cuadernillo de soportes lleva dos DWG para un solo PDF.
  - Cada copia se verifica por SHA256 contra su fuente.
  - Una sola revision por codigo y lamina. Los superados se archivan, no se borran.
  - La cubierta metalica del sistema CIP quedo fuera de alcance el 18-Jun-2026 y sus
    documentos no entran al paquete.

Uso: construir_paquete_construccion.py <carpeta con el NE°15.zip de Van Doorn descomprimido>
"""
import hashlib, re, shutil, sys, unicodedata
from pathlib import Path

# La raiz se deriva de la ubicacion del script, que vive en
# <PROY>/BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/script/.
PROY = Path(__file__).resolve().parents[3]
BL   = PROY / "BASES DE LICITACION MONTAJE MECANICO-OOCC"
REV0 = BL / "Bases REV 0"
PKG  = BL / "INGENIERIA VIGENTE PARA CONSTRUCCION"
BORR = BL / "BORRADOR_REV0"
SUP  = BORR / "_dossier_superseded_pre-REV1"
SUP15 = BORR / "_dossier_superseded_pre-E15" / "2. OBRAS CIVILES - PLANOS Rev 1 del 03 y 08-09-2026 superadas"
BLNE = BORR / "_bl_rev1_no_emitido"

MEC  = PROY / "INGENIERIA DE DETALLE MECANICA" / "ENTREGAS"
COMP = MEC / "COMPILADO REV 0"
E16  = MEC / "ENTREGA 16"
E17  = MEC / "ENTREGA 17" / "ISOS"
# Nota de Envio N15 de Van Doorn (mecanica), descomprimida. No confundir con la ENTREGA 15
# de L&A (civil), que es OOCC15.
NE15 = Path(sys.argv[1]) if len(sys.argv) > 1 else None
ENTOOCC = PROY / "INGENIERIA DE DETALLE OOCC" / "P22-TR-00-010-01-0" / "ENTREGAS"
OOCC10  = ENTOOCC / "ENTREGA 10 (COMPILADO)" / "Planos"      # DWG de las laminas civiles Rev 0
OOCC12  = ENTOOCC / "ENTREGA 12 (ACTUALIZACION NPT)" / "2026-09-03 TT-013 GEN, PL+3D Rev.1" / "Planos"
OOCC13  = ENTOOCC / "ENTREGA 13" / "Plano"
OOCC14  = ENTOOCC / "ENTREGA 14" / "Planos"
OOCC15  = ENTOOCC / "ENTREGA 15" / "2026-09-10 TT-016 CIV, Act. PL (coment.) Rev.1" / "Planos"

errores, copiados = [], 0
PARES = {}        # PDF de plano en el paquete -> lista de DWG que lo acompanan (rutas destino)


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def cp(src: Path, dst_dir: Path, nuevo_nombre: str = None):
    """Copia verificando por SHA256. Devuelve la ruta destino, o None si fallo."""
    global copiados
    if not src.exists():
        errores.append(f"FALTA FUENTE: {src}")
        return None
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / (nuevo_nombre or src.name)
    shutil.copy2(src, dst)
    if sha(src) != sha(dst):
        errores.append(f"SHA256 NO COINCIDE: {dst}")
        return None
    copiados += 1
    return dst


def base_plano(stem: str) -> str:
    """Nombre base de un plano mecanico: quita el sufijo de ploteo que Van Doorn agrega
    tras el parentesis ('-02', '-PFD', '-Model'). El DWG lleva el nombre sin ese sufijo."""
    return re.sub(r"\)-[^)]*$", ")", stem)


def cp_plano(src_pdf: Path, dst_dir: Path, nuevo_nombre: str = None, dwg=None):
    """Copia un plano en PDF y su DWG. `dwg`:
         None         -> el DWG con el mismo nombre base que el PDF, en la carpeta del PDF;
         (src, name)  -> DWG explicito y nombre destino;
         'cubierto'   -> este PDF lo cubre un DWG registrado con otra lamina;
         lista        -> varios (src, name), p.ej. el cuadernillo de soportes."""
    pdf = cp(src_pdf, dst_dir, nuevo_nombre)
    if pdf is None:
        return
    if dwg == "cubierto":
        PARES[pdf] = []
        return
    if dwg is None:
        src_dwg = src_pdf.with_name(base_plano(src_pdf.stem) + ".dwg")
        dwg = [(src_dwg, base_plano(pdf.stem) + ".dwg")]
    elif isinstance(dwg, tuple):
        dwg = [dwg]
    PARES[pdf] = []
    for src_dwg, nombre in dwg:
        d = cp(src_dwg, dst_dir, nombre)
        if d is not None:
            PARES[pdf].append(d)


# --------------------------------------------------------------------------- 3. ET MONTAJE
def dossier_et():
    o = PKG / "3. ET MONTAJE"
    a12 = REV0 / "3. ET MONTAJE" / "A12 - Montaje Electromecanico"
    cp(a12 / "P22-ET-06-007-001-0_MONTAJE-ELECTROMECANICO_ADASA.pdf", o / "A12 - Montaje Electromecanico")
    for f in sorted((a12 / "anexos").glob("*")):
        cp(f, o / "A12 - Montaje Electromecanico" / "anexos")
    a13 = REV0 / "3. ET MONTAJE" / "A13 - Montaje Canerias HDPE"
    cp(a13 / "P22-ET-06-007-002-0_MONTAJE-CANERIAS-HDPE_ADASA.pdf", o / "A13 - Montaje Canerias HDPE")
    # Anexo A del ET HDPE: el Listado de Materiales pasa a Rev 1
    cp(NE15 / "P22-LI-06-006-102-1 (LI Materiales).xlsx",
       o / "A13 - Montaje Canerias HDPE" / "anexos",
       "Anexo-A_P22-LI-06-006-102-1_LI-Materiales.xlsx")


# --------------------------------------------------------------------------- 0. CONTROL DE CAMBIOS
def dossier_control():
    """La Nota Tecnica es el unico documento de control del paquete: absorbio a la
    planilla P22-LI-06-000-002-1, que desde el 09-09-2026 queda como respaldo interno
    en BORRADOR_REV0 y no viaja."""
    nt = BL / "NOTAS_TECNICAS" / "P22-NT-06-000-001-0"
    cp(nt / "P22-NT-06-000-001-0_Ingenieria-Vigente-para-Construccion_ADASA.pdf",
       PKG / "0. CONTROL DE CAMBIOS")


# --------------------------------------------------------------------------- 1. ING. DETALLE MECANICA
def dossier_mecanica():
    o = PKG / "1. ING. DETALLE MECANICA"

    cp(COMP / "00_GENERAL" / "P22-LI-06-000-101-0 (LI Entregables).xlsx", o / "00_GENERAL")

    pi = o / "01_PROCESOS_E_INSTRUMENTACION"
    src = COMP / "01_PROCESOS_E_INSTRUMENTACION"
    for n in ["P22-DWG-06-009-101-0 (PFD Módulo Segunda Etapa Salmuera)-PFD.pdf",
              "P22-DWG-06-009-102-0 (P&ID ALIMENTACIÓN MÓDULO Sda.ETAPA SALMUERA)-02.pdf",
              "P22-DWG-06-009-103-0 (P&ID O.I. SIST.DE TRATAMIENTO SALMUERA)-03.pdf",
              "P22-DWG-06-009-104-0 (P&ID CIP MÓDULO 2da ETAPA SALMUERA)-02.pdf",
              "P22-DWG-06-009-105-0 (P&ID REACTIVOS MÓDULO 2da ETAPA SALMUERA)-06.pdf"]:
        cp_plano(src / n, pi)
    # El P&ID 102 se mantiene en Rev 0 en los dos formatos: la Rev 1 que Van Doorn emitio
    # solo en DWG (NE°15) NO entra, para no llevar un nativo en una revision distinta a la
    # del PDF. Se incorpora cuando llegue el ploteo.
    for n in ["P22-ET-06-008-101-0 (HD Instrumentos).xlsx", "P22-IT-06-008-101-0 (Lógica).pdf"]:
        cp(src / n, pi)
    cp(NE15 / "P22-LI-06-008-101-1 (LI Instrumentos).xlsx", pi)          # Rev 1

    me = o / "02_MECANICA"
    src = COMP / "02_MECANICA"
    for n in ["P22-DWG-06-005-101-0 (PL. MONTAJE - TK SALMUERA Y BBA ALIMENTACION SALMUERA).pdf",
              "P22-DWG-06-005-102-0 (PL. IMPLANTACIÓN GENERAL).pdf",
              "P22-DWG-06-005-104-0 (PL.DRENAJES).pdf",
              "P22-DWG-06-005-105-0 (PL.MONTAJE FOSA DE DRENAJES).pdf"]:
        cp_plano(src / n, me, dwg=(src / (n[:-4].replace("PL.DRENAJES", "PL. DRENAJES")
                                                        .replace("PL.MONTAJE FOSA", "PL. MONTAJE FOSA") + ".dwg"),
                                   n[:-4] + ".dwg"))
    cp(src / "P22-LI-06-005-101-0 (LI Equipos).xlsx", me)
    cp_plano(E16 / "P22-DWG-06-005-103-1 (PL.MONTAJE - MÓDULO DESALACIÓN).pdf", me)   # Rev 1

    ca = o / "03_CANERIAS"
    src = COMP / "03_CANERIAS"
    for n in ["P22-DWG-06-006-105-0 (PL.UBICACIÓN SOPORTES PLANTA INTERCONEXIONES).pdf",
              "P22-DWG-06-006-106-0 (PL. UBICACIÓN DE SOPORTES- TK Y BBA SALMUERA - CORTES).pdf"]:
        cp_plano(src / n, ca)
    for n in ["P22-ET-06-006-001-0 (ET Cañerías).pdf",
              "P22-LI-06-006-101-0 (LI Líneas).xlsx",
              "P22-LI-06-006-103-0 (LI Válvulas).xlsx"]:
        cp(src / n, ca)
    # E16: el DWG lleva un espacio tras "PL." que el PDF no tiene; el destino sigue al PDF.
    cp_plano(E16 / "P22-DWG-06-006-101-1 (PL.CAÑERÍAS INTERCONEXIONES - PLANTA).pdf", ca,
             dwg=(E16 / "P22-DWG-06-006-101-1 (PL. CAÑERÍAS INTERCONEXIONES - PLANTA).dwg",
                  "P22-DWG-06-006-101-1 (PL.CAÑERÍAS INTERCONEXIONES - PLANTA).dwg"))
    cp_plano(E16 / "P22-DWG-06-006-102-1 (PL.CAÑERÍAS INTERCONEXIONES CORTES Y DETALLES).pdf", ca,
             dwg=(E16 / "P22-DWG-06-006-102-1 (PL. CAÑERÍAS INTERCONEXIONES CORTES Y DETALLES).dwg",
                  "P22-DWG-06-006-102-1 (PL.CAÑERÍAS INTERCONEXIONES CORTES Y DETALLES).dwg"))
    # La NE°15 entrego 103 y 104 sin el sufijo de revision en el nombre; el cajetin dice Rev 1.
    for n in ["P22-DWG-06-006-103 (PL. CAÑERÍAS - TK Y BBA SALMUERA - PLANTA)",
              "P22-DWG-06-006-104 (PL. CAÑERÍAS - TK Y BBA SALMUERA - CORTES Y DETALLES)"]:
        con_rev = n.replace("-06-006-10", "-06-006-10").replace(" (", "-1 (", 1)
        cp_plano(NE15 / (n + ".pdf"), ca, con_rev + ".pdf", dwg=(NE15 / (n + ".dwg"), con_rev + ".dwg"))
    cp(NE15 / "P22-LI-06-006-102-1 (LI Materiales).xlsx", ca)            # Rev 1

    # Isometrias: se mantienen las Rev 0 salvo las cuatro que Van Doorn re-emitio
    iso = ca / "Cuadernillo_de_isometrias"
    superadas = ("06-006-005", "06-006-008", "06-006-009", "06-006-011")
    for f in sorted((src / "Cuadernillo_de_isometrias").glob("*.pdf")):
        if not any(s in f.name for s in superadas):
            cp_plano(f, iso)
    for f in sorted(E17.glob("*.pdf")):
        cp_plano(f, iso)

    # Cuadernillo de soportes: un PDF de 21 paginas y dos DWG (grupos 0 y 1), renombrados
    # a la convencion del dossier para que el token de revision quede antes del parentesis.
    cs = src / "Cuadernillo_de_soportes"
    cp_plano(cs / "P22-DWG-06-006-107-0 (CUADERNILLO DE SOPORTES.pdf", ca / "Cuadernillo_de_soportes",
             dwg=[(cs / "P22-DWG-06-006-107_GR 0-0 (CUADERNILLO DE SOPORTES.dwg",
                   "P22-DWG-06-006-107-0 (CUADERNILLO DE SOPORTES) GR0.dwg"),
                  (cs / "P22-DWG-06-006-107_GR 1-0 (CUADERNILLO DE SOPORTES.dwg",
                   "P22-DWG-06-006-107-0 (CUADERNILLO DE SOPORTES) GR1.dwg")])

    # Modelo 3D: los dos NWD publicados el 08-09-2026 reemplazan a la Maqueta Gral
    # del 23-04-2026, anterior al cambio de nivel del modulo. El de nube de puntos
    # pesa 6,4 GB y se entrega por enlace, no dentro del comprimido.
    for nwd in ("MODULO COMPLETO.nwd", "MODULO COMPLETO (nube puntos).nwd"):
        cp(MEC / nwd, o / "04_ MODELO")


# --------------------------------------------------------------------------- 2. OBRAS CIVILES
# Lamina Rev 0 del dossier -> (carpeta de origen, nombre PDF en el origen, nombre PDF en el
# paquete, nombre DWG en el origen, nombre DWG en el paquete). El PDF y el DWG salen de la
# misma entrega. Nombre destino None = el del origen ya sigue la convencion del dossier,
# que es <codigo>_<rev> LAM<n>, con guion bajo antes de la revision y sin espacio en LAM.
REEMPLAZO_CIVIL = {
    # ENTREGA 12, carta 067-032-032-COR-TT-013 del 03-09-2026. El modulo sube 250 mm.
    "P22-DWG-00-002-002_0 LAM4.pdf": (OOCC12, "P22-DWG-00-002-002_1 LAM4.pdf", None,
                                      "P22-DWG-00-002-002_1 LAM4.dwg", None),
    "P22-DWG-00-002-007_0 LAM2.pdf": (OOCC12, "P22-DWG-00-002-007_1 LAM2.pdf", None,
                                      "P22-DWG-00-002-007_1 LAM2.dwg", None),
    # ENTREGA 13, carta 067-032-032-COR-TT-014 del 07-09-2026. Actualiza las coordenadas
    # UTM de once de los trece vertices de replanteo.
    "P22-DWG-00-002-001_0.pdf": (OOCC13, "P22-DWG-00-002-001_1 LAM 1.pdf", "P22-DWG-00-002-001_1.pdf",
                                 "P22-DWG-00-002-001_1 LAM 1.dwg", "P22-DWG-00-002-001_1.dwg"),
    # ENTREGA 15, carta 067-032-032-COR-TT-016 del 10-09-2026: reemision en la misma Rev 1
    # de las cinco laminas comentadas el 09-09-2026 (reemplaza a las de TT-013 y TT-015).
    # El DWG del 00-001-001 es uno solo y contiene las dos laminas.
    "P22-DWG-00-002-002_0 LAM1.pdf": (OOCC15, "P22-DWG-00-002-002_1 LAM1.pdf", None,
                                      "P22-DWG-00-002-002_1 LAM1.dwg", None),
    "P22-DWG-00-002-003_0 LAM1.pdf": (OOCC15, "P22-DWG-00-002-003_1 LAM1.pdf", None,
                                      "P22-DWG-00-002-003_1 LAM1.dwg", None),
    "P22-DWG-00-002-007_0 LAM1.pdf": (OOCC15, "P22-DWG-00-002-007_1 LAM1.pdf", None,
                                      "P22-DWG-00-002-007_1 LAM1.dwg", None),
    "P22-DWG-00-001-001_0 LAM1.pdf": (OOCC15, "P22-DWG-00-001-001-1-LAM 1.pdf", "P22-DWG-00-001-001_1 LAM1.pdf",
                                      "P22-DWG-00-001-001-1.dwg", "P22-DWG-00-001-001_1.dwg"),
    "P22-DWG-00-001-001_0 LAM2.pdf": (OOCC15, "P22-DWG-00-001-001-1-LAM 2.pdf", "P22-DWG-00-001-001_1 LAM2.pdf",
                                      "cubierto", None),
}

# Carta con la que viajo la Rev 1 que el paquete tenia antes del 10-09-2026, por lamina.
# Sirve para archivarla con un sufijo que la distinga de la Rev 1 nueva.
CARTA_REV1_ANTERIOR = {
    "P22-DWG-00-002-002_1 LAM1.pdf": "TT-013", "P22-DWG-00-002-003_1 LAM1.pdf": "TT-013",
    "P22-DWG-00-002-007_1 LAM1.pdf": "TT-013",
    "P22-DWG-00-001-001_1 LAM1.pdf": "TT-015", "P22-DWG-00-001-001_1 LAM2.pdf": "TT-015",
}


def archivar_rev1_anterior(dst: Path, src: Path):
    """Si el paquete ya tiene una copia con el mismo nombre y otro contenido, la archiva
    en SUP15 con el sufijo de su carta antes de que la copia nueva la reemplace."""
    if dst.exists() and sha(dst) != sha(src):
        carta = CARTA_REV1_ANTERIOR.get(dst.name, "anterior")
        SUP15.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dst, SUP15 / f"{dst.stem}_{carta}{dst.suffix}")


def dwg_rev0_civil(nombre_pdf: str) -> Path:
    """DWG de una lamina civil Rev 0, en la ENTREGA 10 (compilado), cuyos PDF son byte a byte
    los del paquete. Los nombres del origen a veces llevan espacio en 'LAM 1'."""
    objetivo = nombre_pdf[:-4].replace(" ", "")
    for f in OOCC10.glob("*.dwg"):
        if f.stem.replace(" ", "") == objetivo:
            return f
    return OOCC10 / (nombre_pdf[:-4] + ".dwg")      # cp() reportara la falta


def dossier_civil():
    o = PKG / "2. OBRAS CIVILES"
    src = REV0 / "5. OBRAS CIVILES (A2)"
    for f in sorted((src / "ET").glob("*.pdf")):
        cp(f, o / "ET")
    for f in sorted((src / "PLANOS").glob("*.pdf")):
        if f.name in REEMPLAZO_CIVIL:
            carpeta, nombre, destino, dwg, destino_dwg = REEMPLAZO_CIVIL[f.name]
            archivar_rev1_anterior(o / "PLANOS" / (destino or nombre), carpeta / nombre)
            if dwg == "cubierto":
                cp_plano(carpeta / nombre, o / "PLANOS", destino, dwg="cubierto")
            else:
                cp_plano(carpeta / nombre, o / "PLANOS", destino,
                         dwg=(carpeta / dwg, destino_dwg or dwg))
            cp(f, SUP / "5. OBRAS CIVILES (A2) - PLANOS Rev 0 superadas")
        else:
            cp_plano(f, o / "PLANOS", dwg=(dwg_rev0_civil(f.name), f.stem + ".dwg"))


def autochequeo():
    """Cuatro reglas duras del paquete de construccion, verificadas sobre el arbol final."""
    from collections import defaultdict

    # 1. Una sola revision por codigo y lamina, en PDF, XLSX y DWG
    rx = re.compile(r"(P22-(?:DWG|ET|LI|IT)-\d{2}-\d{3}-\d{3})[-_]?([0-9A-D])?\s*(LAM\s*\d|_H\.\d)?")
    vistos = defaultdict(set)
    for f in PKG.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in (".pdf", ".xlsx", ".dwg"):
            continue
        m = rx.match(f.name)
        if m:
            clave = (m.group(1), (m.group(3) or "").replace(" ", ""))
            vistos[clave].add(m.group(2))
    for clave, revs in sorted(vistos.items()):
        if len(revs) > 1:
            errores.append(f"REVISION DUPLICADA: {clave[0]} {clave[1]} en revisiones {sorted(revs)}")

    # 2. Cero documentos de la cubierta, que salio de alcance el 18-Jun-2026
    for f in PKG.rglob("*"):
        if f.is_file() and any(x in f.name for x in ("00-003-001", "MC-00-003-001", "ET-00-010-103")):
            errores.append(f"DOCUMENTO DE LA CUBIERTA EN EL PAQUETE: {f.name}")

    # 3. Cero Bases de Licitacion y cero Formato de Presupuesto
    for f in PKG.rglob("*"):
        if f.is_file() and ("BL_MONTAJE" in f.name or "Formato de Presupuesto" in f.name):
            errores.append(f"DOCUMENTO DE LICITACION EN EL PAQUETE: {f.name}")

    # 4. Cada plano en PDF tiene su DWG apareado y no hay DWG huerfano. Las rutas se
    #    comparan normalizadas a NFC: el NAS devuelve los nombres con tilde en NFD y los
    #    literales del script van en NFC, y sin normalizar el mismo archivo parece dos.
    nfc = lambda q: unicodedata.normalize("NFC", str(q))
    pdfs = {nfc(f) for f in PKG.rglob("P22-DWG*.pdf")}
    dwgs = {nfc(f) for f in PKG.rglob("*.dwg")}
    declarados = {nfc(k): [nfc(d) for d in v] for k, v in PARES.items()}
    apareados = {d for lst in declarados.values() for d in lst}
    for p in sorted(pdfs - set(declarados)):
        errores.append(f"PLANO SIN DWG DECLARADO: {Path(p).name}")
    for p, lst in declarados.items():
        if not lst and not p.endswith("P22-DWG-00-001-001_1 LAM2.pdf"):
            errores.append(f"PLANO SIN DWG: {Path(p).name}")
        for d in lst:
            if d not in dwgs:
                errores.append(f"DWG DECLARADO Y AUSENTE: {Path(d).name}")
    for d in sorted(dwgs - apareados):
        errores.append(f"DWG HUERFANO EN EL PAQUETE: {Path(d).name}")

    if not errores:
        print(f"Autochequeo OK: {len(vistos)} codigos, una revision cada uno; sin cubierta; "
              f"sin Bases ni Formato; {len(pdfs)} planos PDF con {len(dwgs)} DWG apareados.")


if __name__ == "__main__":
    if NE15 is None or not NE15.exists():
        sys.exit("Uso: construir_paquete_construccion.py <carpeta con el NE°15.zip de Van Doorn descomprimido>")
    for d in (dossier_mecanica, dossier_civil, dossier_et, dossier_control):
        d()
    print(f"Archivos copiados y verificados por SHA256: {copiados}")
    autochequeo()
    if errores:
        print(f"\nERRORES ({len(errores)}):")
        for e in errores:
            print("  -", e)
        sys.exit(1)
    total = sum(1 for f in PKG.rglob("*") if f.is_file() and not f.name.startswith("."))
    tam = sum(f.stat().st_size for f in PKG.rglob("*") if f.is_file()) / 2**20
    print(f"Sin errores. Paquete: {total} archivos, {tam:,.0f} MB.")
