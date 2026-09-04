"""
Traduce las anotaciones FreeText en español a inglés en los PDFs de Preliminar Layout.
Mantiene posición, tamaño y colores originales.

Uso: python3 traducir_comentarios_layout.py
"""

import fitz  # PyMuPDF
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TRANSLATIONS = {
    # Equipment Layout
    "Mover el estanque al lado contrario para poder acceder a cargar el quimico":
        "Move the tank to the opposite side to allow access for chemical loading",

    # Tie-In Point
    "No hay espacio para instalar un pipe rack, las conexiones deben salir directamente desde el container":
        "There is no space to install a pipe rack; connections must come directly from the container",

    "Mantener los tie-in de procesos":
        "Keep the process tie-ins",

    # Variante con espacio en "tie- in" (tal como está en el PDF)
    "Mantener los tie- in de procesos":
        "Keep the process tie-ins",

    "La carga del antiescalante debe ser directo hacia el estanque de dosificacion, no tengo presupuesto para una bomba de dosificacion carrier":
        "Antiscalant loading must go directly to the dosing tank; no budget available for a carrier dosing pump",

    "El estanque de dosificacion queda sin acceso,":
        "The dosing tank has no access,",

    "No veo las bridas de conexion para poder hacer el corte para el traslado del modulo":
        "Connection flanges for the module relocation cutover are not shown",

    "Necesito una elevacion para ver el detalle de como seran los tie-in":
        "An elevation view is needed to show the tie-in connection details",

    "Necesito ver la elevacion del container para ver donde estan ubicadas las bridas los tie-in, debe volver a la elevacion del container":
        "Container elevation is needed to locate the tie-in flanges; the detail must revert to the container elevation view",

    # Variante con doble espacio (tal como está en el PDF)
    "Necesito ver la elevacion del container para ver donde estan ubicadas las bridas los tie-in, debe volver a  la elevacion del container":
        "Container elevation is needed to locate the tie-in flanges; the detail must revert to the container elevation view",
}

PDFS = [
    "P22-DWG-09-005-003_Equipment Layout_Rev.B.pdf",
    "P22-DWG-09-005-005_Tie-In Point_Rev.B.pdf",
]


def traducir_pdf(filename):
    path = os.path.join(SCRIPT_DIR, filename)
    if not os.path.exists(path):
        print(f"  ERROR: archivo no encontrado: {filename}")
        return 0

    doc = fitz.open(path)
    changed = 0

    for page in doc:
        for annot in page.annots():
            content = annot.info.get("content", "").strip()
            if content in TRANSLATIONS:
                annot.set_info(content=TRANSLATIONS[content])
                annot.update()
                changed += 1

    tmp = path + ".tmp"
    doc.save(tmp)
    doc.close()
    os.replace(tmp, path)

    return changed


if __name__ == "__main__":
    total = 0
    for pdf in PDFS:
        n = traducir_pdf(pdf)
        print(f"{pdf}: {n} annotation(s) translated")
        total += n
    print(f"\nTotal: {total} annotations translated")
