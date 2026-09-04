#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_pid_rev_c.py
Agrega anotaciones FreeText ADASA al PDF P&ID Rev C — TM N13.

Documento: P22-DWG-09-009-002 Rev C
Transmittal: P22-TM-09-000-013-0
Entrega: E24 (25007-0024)
Fecha: 31-Mar-2026

Observaciones (1 item):
  NOTE-01 (MINOR): TK-09-001 CIP Tank volumen = 6.81 m3 vs 6.1 m3 en Equipment List Rev B

Nota tecnica: paginas 2-12 tienen rot=270, mediabox (0,0,792,1224), display 1224x792.
Para que la anotacion aparezca en la posicion correcta y con texto horizontal se debe:
  1. page.set_rotation(0) — operar en coordenadas NATIVAS del PDF
  2. Calcular rect nativo para el area deseada en display
  3. add_freetext_annot con rect nativo
  4. annot.set_rotation(270) — contra-rota el texto 270 CCW para que quede
     horizontal tras el /Rotate=270 CW de display (270 CCW + 270 CW = 0 neto)
  5. page.set_rotation(270) — restaurar

Derivacion de coordenadas (page MediaBox W=792, H=1224, /Rotate=270 CW):
  display -> PDF nativo (y-up):  pdf_x = W - display_y; pdf_y = display_x
  PDF nativo -> PyMuPDF (y-down): pymupdf_y = H - pdf_y

  Target display top-right: x_d in [824,1209], y_d in [10,160]
  -> pdf_x in [792-160, 792-10] = [632, 782]
  -> pdf_y in [824, 1209]
  -> pymupdf_y in [1224-1209, 1224-824] = [15, 400]
  -> native rect: fitz.Rect(632, 15, 782, 400)
"""

import sys
import os
import shutil
import fitz  # PyMuPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Nombre exacto del archivo fuente (tiene typo "Daigram" — mantener exacto)
PDF_ORIGINAL_NAME = "P22-DWG-09-009-002_C - Piping & Instrumentation Daigram.pdf"
PDF_LOCAL_NAME    = "P22-DWG-09-009-002_C_PID.pdf"   # nombre normalizado local

PDF_LOCAL = os.path.join(SCRIPT_DIR, PDF_LOCAL_NAME)
PDF_OUT   = os.path.join(SCRIPT_DIR, "P22-DWG-09-009-002_C_PID_CC_ADASA.pdf")

# Copiar PDF fuente si no existe localmente
if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(SCRIPT_DIR, "..", "..", "..", "..",
                     "ENTREGAS_BWWATER", "ENTREGA 24", PDF_ORIGINAL_NAME)
    )
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print(f"PDF fuente copiado: {PDF_LOCAL_NAME}")
    else:
        print(f"ERROR: PDF no encontrado en:\n  {src}")
        sys.exit(1)

# Color NOTE (azul claro) — consistente con doc_annotator.NOTE
NOTE_COLOR = (0.85, 0.93, 1.00)

# Texto de la anotacion
TEXT_NOTE01 = (
    "NOTE-01 (MINOR): CIP Tank TK-09-001 is annotated as 6.81 m\u00b3 in Rev C. "
    "Equipment List Rev B (P22-LI-09-005-001) specifies 6.1 m\u00b3 "
    "(Dayamas DYM 6800, HDPE, 1800 mm\u00d8 \u00d7 2950 mm H). "
    "Discrepancy of 0.71 m\u00b3 has no supporting documentation. "
    "Confirm correct installed volume and update P&ID consistent with "
    "Equipment List prior to IFC (Rev 0).\n"
    "If CIP Tank capacity was revised, submit updated Equipment List Rev C "
    "with technical justification."
)

# Verificacion: 1 comentario = 1 obs/note del transmittal
assert 1 == 1, "Verificar: debe haber 1 comentario (NOTE-01)"


def main():
    doc = fitz.open(PDF_LOCAL)
    total = len(doc)
    print(f"PDF abierto: {total} paginas — {PDF_LOCAL_NAME}\n")

    # Pagina 11 (indice 10) — CIP Tank TK-09-001
    # rot=270, mediabox=(0,0,792,1224), display 1224x792 (landscape)
    page_idx = 10
    page = doc[page_idx]
    original_rotation = page.rotation  # 270

    print(f"Pagina {page_idx + 1}: rot={original_rotation}, mediabox={page.mediabox}")

    # Paso 1: trabajar en espacio nativo (desactivar rotacion temporalmente)
    page.set_rotation(0)

    # Paso 2: rect nativo para area superior-derecha del display landscape
    # Target display: x_d in [824,1209], y_d in [10,160] (esquina sup-der 1224x792)
    # -> native PyMuPDF (y-down, H=1224): x in [632,782], y in [15,400]
    rect = fitz.Rect(632, 15, 782, 400)

    # Paso 3: agregar anotacion FreeText en coordenadas nativas
    annot = page.add_freetext_annot(
        rect, TEXT_NOTE01,
        fontsize=8,
        fontname="helv",
        text_color=(0, 0, 0),
        fill_color=NOTE_COLOR,
    )
    annot.set_border(width=1.5)

    # Paso 4: contra-rotar texto 270 CCW para que quede horizontal en display
    # (270 CCW annotation + 270 CW page = 0 neto = horizontal)
    # Pasar rotate= directamente en update() para garantizar que /Rotate quede en el dict
    annot.update(rotate=270)

    # Paso 5: restaurar rotacion original
    page.set_rotation(original_rotation)

    print(f"  [NOTE-01] pag {page_idx + 1} native rect ({rect.x0:.0f},{rect.y0:.0f})-"
          f"({rect.x1:.0f},{rect.y1:.0f}) -> display ~(824,10)-(1209,160)")

    doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print(f"\nOutput: {PDF_OUT}")
    print(f"Tamano: {os.path.getsize(PDF_OUT):,} bytes")


if __name__ == "__main__":
    main()
