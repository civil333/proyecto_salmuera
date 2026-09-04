"""
traducir_anotaciones_manuales.py
Traduccion in-place de anotaciones manuales en espanol (3 anotaciones en 2 PDFs).
Patron: set_info(content=...)+update() (CLAUDE.md Section 3.11).
Preserva posicion, color y tamano. Homologa title a 'ADASA - Luis Rivera'.

Uso unico: tras correr este script, los PDFs quedan en ingles y NO se debe
re-generar con agregar_comentarios_*.py (borraria las anotaciones manuales).
"""
import fitz
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TARGETS = [
    {
        "pdf": "P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf",
        "translations": [
            {
                "es": "FALTA UN DETALLE DE ESTO CONFIRMAR QUE EL DETALLE ESTA EN EL PLANO (TYPICAL INSTALLATION DETAILS OF POWER WORKS)",
                "en": (
                    "NOTE-02: Detail missing — confirm that the detail "
                    "is included in the Typical Installation Details of "
                    "Power Works drawing (P22-DWG-09-007-005)."
                ),
            },
        ],
    },
    {
        "pdf": "P22-DWG-09-007-005_0_Typical_Power_Works_CC_ADASA.pdf",
        "translations": [
            {
                "es": "Esto va  hacia el modulo, esta considerado como la alimentacion de los consumidores aguas abajo, No queda claro, ya que el modulo esta del otro lado",
                "en": (
                    "NOTE-03: Diagram shows the feed routed towards the "
                    "module as the supply to downstream consumers. "
                    "Direction unclear — the module is on the opposite "
                    "side of the diagram. Reorient the typical detail "
                    "or annotate the flow direction explicitly."
                ),
            },
            {
                "es": 'Considerar que la alimentacion principaol el "incoming" sera por banco de ducto desde sala electrica (que es responsabilidad de adasa)',
                "en": (
                    "NOTE-04: The main incoming feed will be routed via "
                    "duct bank from the electrical room (ADASA scope). "
                    "Update the typical detail to reflect the actual "
                    "interface boundary between ADASA and BW Water."
                ),
            },
        ],
    },
]

NEW_TITLE = "ADASA - Luis Rivera"


def translate_pdf(pdf_path, translations):
    doc = fitz.open(pdf_path)
    matched = {t["es"]: False for t in translations}
    for page in doc:
        for annot in page.annots() or []:
            content = annot.info.get("content", "").strip()
            for t in translations:
                if content == t["es"].strip():
                    annot.set_info(
                        content=t["en"],
                        title=NEW_TITLE,
                    )
                    annot.update()
                    matched[t["es"]] = True
                    print(f"  [OK] page {page.number + 1}: '{content[:60]}...' -> translated")
                    break
    for es, ok in matched.items():
        if not ok:
            print(f"  [WARN] not matched: {es[:80]}...")
    tmp = pdf_path + ".tmp"
    doc.save(tmp)
    doc.close()
    os.replace(tmp, pdf_path)


if __name__ == "__main__":
    for target in TARGETS:
        path = os.path.join(SCRIPT_DIR, target["pdf"])
        print(f"=== {target['pdf']} ===")
        translate_pdf(path, target["translations"])
