"""Renderiza screenshots de planos y ortofotos via glob por codigo."""
import fitz
import glob
import os

BASE = r"C:\SynologyDrive\SynologyDrive\DESAROLLO PROYECTOS CLAUDE\MODULO DE SALMUERA TALTAL"
COMPILADO = os.path.join(BASE, "INGENIERIA DE DETALLE MECANICA", "ENTREGAS", "COMPILADO REV 0")
TR_LYA = os.path.join(BASE, "INGENIERIA DE DETALLE OOCC", "P22-TR-00-010-01-0", "P22-TR-00-010-01-1(Ingenieria OOCC Modulo Taltal).pdf")
OUT = os.path.join(BASE, "BASES DE LICITACION MONTAJE MECANICO-OOCC", "BORRADOR_REV0", "imagenes")

DPI = 200
MATRIX = fitz.Matrix(DPI/72.0, DPI/72.0)

JOBS = [
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-102*.pdf", 0, "05_pid_alimentacion_vandoorn.png"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-103*.pdf", 0, "06_pid_oi_tratamiento.png"),
    ("01_PROCESOS_E_INSTRUMENTACION", "P22-DWG-06-009-104*.pdf", 0, "07_pid_cip.png"),
    ("02_MECANICA",                   "P22-DWG-06-005-104*.pdf", 0, "09_drenajes_mecanico.png"),
    ("02_MECANICA",                   "P22-DWG-06-005-105*.pdf", 0, "10_fosa_drenajes_mecanico.png"),
    ("03_CANERIAS",                   "P22-DWG-06-006-105*.pdf", 0, "14_ubicacion_soportes_planta.png"),
]

for subdir, pat, page, out_name in JOBS:
    matches = glob.glob(os.path.join(COMPILADO, subdir, pat))
    if not matches:
        print(f"  FAIL no match: {pat}")
        continue
    pdf = matches[0]
    try:
        doc = fitz.open(pdf)
        if page >= len(doc):
            print(f"  SKIP {out_name}: PDF tiene {len(doc)} pag")
            doc.close()
            continue
        pix = doc[page].get_pixmap(matrix=MATRIX)
        out_path = os.path.join(OUT, out_name)
        pix.save(out_path)
        print(f"  OK   {out_name}  ({pix.width}x{pix.height})")
        doc.close()
    except Exception as e:
        print(f"  FAIL {out_name}: {e}")

print("Listo.")
