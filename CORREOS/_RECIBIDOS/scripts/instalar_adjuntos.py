#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instala en su destino el ZIP de un submittal que llego por enlace de OneDrive.

Deduplica POR HASH DEL CONTENIDO, nunca del contenedor: un mismo payload
descargado dos veces da ZIP distinto, y un archivo ya presente con hash
identico no se vuelve a escribir. Es la regla que el proyecto ya tenia escrita
para los adjuntos de Outlook y aplica igual aqui.

Nunca sobrescribe. Si un archivo existe con hash DISTINTO, se detiene y lo
reporta: eso significa que el proveedor cambio el contenido sin cambiar el
nombre, que es un hallazgo, no algo que resolver en silencio.

Uso:
    python instalar_adjuntos.py <zip> --destino "ENTREGAS_BWWATER/ENTREGA 72"
    python instalar_adjuntos.py <zip> --destino "..." --dry-run
"""
import argparse
import hashlib
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROYECTO = RAIZ.parent.parent

INTOCABLE = "PAQUETE_INSPECCION_BV"


def md5_bytes(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()


def md5_archivo(p: Path) -> str:
    h = hashlib.md5()
    with p.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Instala un ZIP de submittal en su destino")
    ap.add_argument("zip", help="ruta del ZIP descargado")
    ap.add_argument("--destino", required=True,
                    help="ruta relativa al proyecto, p.ej. 'ENTREGAS_BWWATER/ENTREGA 72'")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if INTOCABLE in args.destino:
        print(f"ABORTA: {INTOCABLE} no se toca (enlace Synology publicado a Bureau Veritas).",
              file=sys.stderr)
        return 1

    z = Path(args.zip).expanduser()
    if not z.exists():
        print(f"ABORTA: no existe {z}", file=sys.stderr)
        return 1

    destino = (PROYECTO / args.destino).resolve()
    if PROYECTO not in destino.parents and destino != PROYECTO:
        print(f"ABORTA: el destino queda fuera del proyecto: {destino}", file=sys.stderr)
        return 1

    nuevos, ya_estaban, conflictos = [], [], []

    with zipfile.ZipFile(z) as f:
        for info in f.infolist():
            if info.is_dir():
                continue
            datos = f.read(info.filename)
            h = md5_bytes(datos)
            salida = destino / info.filename
            if salida.exists():
                if md5_archivo(salida) == h:
                    ya_estaban.append((info.filename, h[:12]))
                else:
                    conflictos.append((info.filename, md5_archivo(salida)[:12], h[:12]))
                continue
            nuevos.append((info.filename, h[:12], info.file_size, datos, salida))

    print(f"ZIP: {z.name} ({z.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"Destino: {args.destino}")
    print(f"  ya presentes con hash identico: {len(ya_estaban)}")
    print(f"  nuevos: {len(nuevos)}")
    print(f"  conflictos (mismo nombre, contenido distinto): {len(conflictos)}")

    for nombre, hd, hz in conflictos:
        print(f"  CONFLICTO  {nombre}\n     en disco {hd}  |  en el ZIP {hz}")
    if conflictos:
        print("\nABORTA: hay archivos con el mismo nombre y contenido distinto. "
              "El proveedor cambio el contenido sin cambiar el nombre: es un hallazgo "
              "de control de revisiones, no algo que resolver sobrescribiendo.",
              file=sys.stderr)
        return 1

    for nombre, h, tam, _datos, salida in nuevos:
        print(f"  + {tam / 1024 / 1024:7.2f} MB  {h}  {nombre}")

    if args.dry_run:
        print("\n[dry-run] no se escribio nada")
        return 0

    for _nombre, _h, _tam, datos, salida in nuevos:
        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_bytes(datos)

    print(f"\nInstalados {len(nuevos)} archivos nuevos. "
          f"{len(ya_estaban)} ya estaban y no se tocaron.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
