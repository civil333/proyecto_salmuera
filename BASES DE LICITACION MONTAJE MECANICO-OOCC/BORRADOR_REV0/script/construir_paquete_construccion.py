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
  - Solo PDF, XLSX y el modelo NWD. Sin DWG, sin .bak, sin .md, sin .log.
  - Cada copia se verifica por SHA256 contra su fuente.
  - Una sola revision por codigo y lamina. Los superados se archivan, no se borran.
  - La cubierta metalica del sistema CIP quedo fuera de alcance el 18-Jun-2026 y sus
    documentos no entran al paquete.
"""
import hashlib, shutil, sys
from pathlib import Path

# La raiz se deriva de la ubicacion del script, que vive en
# <PROY>/BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/script/.
# Antes era un literal de macOS y el script no corria en los otros dos equipos.
PROY = Path(__file__).resolve().parents[3]
BL   = PROY / "BASES DE LICITACION MONTAJE MECANICO-OOCC"
REV0 = BL / "Bases REV 0"
PKG  = BL / "INGENIERIA VIGENTE PARA CONSTRUCCION"
BORR = BL / "BORRADOR_REV0"
SUP  = BORR / "_dossier_superseded_pre-REV1"
BLNE = BORR / "_bl_rev1_no_emitido"

MEC  = PROY / "INGENIERIA DE DETALLE MECANICA" / "ENTREGAS"
COMP = MEC / "COMPILADO REV 0"
E16  = MEC / "ENTREGA 16"
E17  = MEC / "ENTREGA 17" / "ISOS"
E15  = Path(sys.argv[1]) if len(sys.argv) > 1 else None   # carpeta con el ZIP NE°15 descomprimido
ENTOOCC = PROY / "INGENIERIA DE DETALLE OOCC" / "P22-TR-00-010-01-0" / "ENTREGAS"
OOCC12  = ENTOOCC / "ENTREGA 12 (ACTUALIZACION NPT)" / "2026-09-03 TT-013 GEN, PL+3D Rev.1" / "Planos"
OOCC13  = ENTOOCC / "ENTREGA 13" / "Plano"
OOCC14  = ENTOOCC / "ENTREGA 14" / "Planos"
OOCC    = OOCC12   # alias historico

errores, copiados = [], 0


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
    cp(E15 / "P22-LI-06-006-102-1 (LI Materiales).xlsx",
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
              "P22-DWG-06-009-105-0 (P&ID REACTIVOS MÓDULO 2da ETAPA SALMUERA)-06.pdf",
              "P22-ET-06-008-101-0 (HD Instrumentos).xlsx",
              "P22-IT-06-008-101-0 (Lógica).pdf"]:
        cp(src / n, pi)
    cp(E15 / "P22-LI-06-008-101-1 (LI Instrumentos).xlsx", pi)          # Rev 1

    me = o / "02_MECANICA"
    src = COMP / "02_MECANICA"
    for n in ["P22-DWG-06-005-101-0 (PL. MONTAJE - TK SALMUERA Y BBA ALIMENTACION SALMUERA).pdf",
              "P22-DWG-06-005-102-0 (PL. IMPLANTACIÓN GENERAL).pdf",
              "P22-DWG-06-005-104-0 (PL.DRENAJES).pdf",
              "P22-DWG-06-005-105-0 (PL.MONTAJE FOSA DE DRENAJES).pdf",
              "P22-LI-06-005-101-0 (LI Equipos).xlsx"]:
        cp(src / n, me)
    cp(E16 / "P22-DWG-06-005-103-1 (PL.MONTAJE - MÓDULO DESALACIÓN).pdf", me)   # Rev 1

    ca = o / "03_CANERIAS"
    src = COMP / "03_CANERIAS"
    for n in ["P22-DWG-06-006-105-0 (PL.UBICACIÓN SOPORTES PLANTA INTERCONEXIONES).pdf",
              "P22-DWG-06-006-106-0 (PL. UBICACIÓN DE SOPORTES- TK Y BBA SALMUERA - CORTES).pdf",
              "P22-ET-06-006-001-0 (ET Cañerías).pdf",
              "P22-LI-06-006-101-0 (LI Líneas).xlsx",
              "P22-LI-06-006-103-0 (LI Válvulas).xlsx"]:
        cp(src / n, ca)
    cp(E16 / "P22-DWG-06-006-101-1 (PL.CAÑERÍAS INTERCONEXIONES - PLANTA).pdf", ca)
    cp(E16 / "P22-DWG-06-006-102-1 (PL.CAÑERÍAS INTERCONEXIONES CORTES Y DETALLES).pdf", ca)
    # La E15 entrego 103 y 104 sin el sufijo de revision en el nombre; el cajetin dice Rev 1.
    cp(E15 / "P22-DWG-06-006-103 (PL. CAÑERÍAS - TK Y BBA SALMUERA - PLANTA).pdf", ca,
       "P22-DWG-06-006-103-1 (PL. CAÑERÍAS - TK Y BBA SALMUERA - PLANTA).pdf")
    cp(E15 / "P22-DWG-06-006-104 (PL. CAÑERÍAS - TK Y BBA SALMUERA - CORTES Y DETALLES).pdf", ca,
       "P22-DWG-06-006-104-1 (PL. CAÑERÍAS - TK Y BBA SALMUERA - CORTES Y DETALLES).pdf")
    cp(E15 / "P22-LI-06-006-102-1 (LI Materiales).xlsx", ca)            # Rev 1

    # Isometrias: se mantienen las Rev 0 salvo las cuatro que Van Doorn re-emitio
    iso = ca / "Cuadernillo_de_isometrias"
    superadas = ("06-006-005", "06-006-008", "06-006-009", "06-006-011")
    for f in sorted((src / "Cuadernillo_de_isometrias").glob("*.pdf")):
        if not any(s in f.name for s in superadas):
            cp(f, iso)
    for f in sorted(E17.glob("*.pdf")):
        cp(f, iso)

    cp(src / "Cuadernillo_de_soportes" / "P22-DWG-06-006-107-0 (CUADERNILLO DE SOPORTES.pdf",
       ca / "Cuadernillo_de_soportes")

    # Modelo 3D: los dos NWD publicados el 08-09-2026 reemplazan a la Maqueta Gral
    # del 23-04-2026, anterior al cambio de nivel del modulo. El de nube de puntos
    # pesa 6,4 GB y se entrega por enlace, no dentro del comprimido.
    for nwd in ("MODULO COMPLETO.nwd", "MODULO COMPLETO (nube puntos).nwd"):
        cp(MEC / nwd, o / "04_ MODELO")


# --------------------------------------------------------------------------- 2. OBRAS CIVILES
# Lamina Rev 0 del dossier -> (carpeta de origen, nombre en el origen, nombre en el paquete).
# El tercer campo va en None cuando el nombre del origen ya sigue la convencion del dossier,
# que es <codigo>_<rev> LAM<n>.pdf, con guion bajo antes de la revision y sin espacio en LAM.
REEMPLAZO_CIVIL = {
    # ENTREGA 12, carta 067-032-032-COR-TT-013 del 03-09-2026. El modulo sube 250 mm.
    "P22-DWG-00-002-002_0 LAM1.pdf": (OOCC12, "P22-DWG-00-002-002_1 LAM1.pdf", None),
    "P22-DWG-00-002-002_0 LAM4.pdf": (OOCC12, "P22-DWG-00-002-002_1 LAM4.pdf", None),
    "P22-DWG-00-002-003_0 LAM1.pdf": (OOCC12, "P22-DWG-00-002-003_1 LAM1.pdf", None),
    "P22-DWG-00-002-007_0 LAM1.pdf": (OOCC12, "P22-DWG-00-002-007_1 LAM1.pdf", None),
    "P22-DWG-00-002-007_0 LAM2.pdf": (OOCC12, "P22-DWG-00-002-007_1 LAM2.pdf", None),
    # ENTREGA 13, carta 067-032-032-COR-TT-014 del 07-09-2026. Actualiza las coordenadas
    # UTM de once de los trece vertices de replanteo.
    "P22-DWG-00-002-001_0.pdf": (OOCC13, "P22-DWG-00-002-001_1 LAM 1.pdf",
                                 "P22-DWG-00-002-001_1.pdf"),
    # ENTREGA 14, carta 067-032-032-COR-TT-015 del 08-09-2026, movimiento de tierra.
    # Entran con reparos declarados en el LEEME del dossier civil: sus cifras del contenedor y
    # de la zona CIP corrigen las de la revision 0, que estaban sobre el sello anterior, y a la
    # vez contradicen al 00-002-003 y al 00-002-007. Los siete puntos abiertos con el
    # proyectista viven en el transmittal P22-TM-00-010-005-0.
    "P22-DWG-00-001-001_0 LAM1.pdf": (OOCC14, "P22-DWG-00-001-001-1-LAM 1.pdf",
                                      "P22-DWG-00-001-001_1 LAM1.pdf"),
    "P22-DWG-00-001-001_0 LAM2.pdf": (OOCC14, "P22-DWG-00-001-001-1-LAM 2.pdf",
                                      "P22-DWG-00-001-001_1 LAM2.pdf"),
}


def dossier_civil():
    o = PKG / "2. OBRAS CIVILES"
    src = REV0 / "5. OBRAS CIVILES (A2)"
    for f in sorted((src / "ET").glob("*.pdf")):
        cp(f, o / "ET")
    for f in sorted((src / "PLANOS").glob("*.pdf")):
        if f.name in REEMPLAZO_CIVIL:
            carpeta, nombre, destino = REEMPLAZO_CIVIL[f.name]
            cp(carpeta / nombre, o / "PLANOS", destino)
            cp(f, SUP / "5. OBRAS CIVILES (A2) - PLANOS Rev 0 superadas")
        else:
            cp(f, o / "PLANOS")


def autochequeo():
    """Tres reglas duras del paquete de construccion, verificadas sobre el arbol final."""
    import re
    from collections import defaultdict

    # 1. Una sola revision por codigo y lamina
    rx = re.compile(r"(P22-(?:DWG|ET|LI|IT)-\d{2}-\d{3}-\d{3})[-_]?([0-9A-D])?\s*(LAM\s*\d|_H\.\d)?")
    vistos = defaultdict(set)
    for f in PKG.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in (".pdf", ".xlsx"):
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

    if not errores:
        print(f"Autochequeo OK: {len(vistos)} codigos, una revision cada uno; "
              f"sin cubierta; sin Bases ni Formato.")


if __name__ == "__main__":
    if E15 is None or not E15.exists():
        sys.exit("Uso: construir_paquete_construccion.py <carpeta con el ZIP NE°15 descomprimido>")
    for d in (dossier_mecanica, dossier_civil, dossier_et, dossier_control):
        d()
    print(f"Archivos copiados y verificados por SHA256: {copiados}")
    autochequeo()
    if errores:
        print(f"\nERRORES ({len(errores)}):")
        for e in errores:
            print("  -", e)
        sys.exit(1)
    print("Sin errores.")
