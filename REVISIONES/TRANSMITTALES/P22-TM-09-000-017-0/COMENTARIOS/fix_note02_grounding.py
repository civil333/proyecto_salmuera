"""
fix_note02_grounding.py
Corrige NOTE-02 en P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf:
  - rotation 0 -> 270 (matching page rotation, so text reads horizontally
    when viewing the page in landscape view)
  - fontsize incrementado para mejor legibilidad
  - rect ajustado para acomodar el texto re-orientado

Uso unico — la anotacion ya tiene la traduccion correcta.
"""
import fitz
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(SCRIPT_DIR, "P22-DWG-09-007-003_D_Grounding_Layout_CC_ADASA.pdf")

doc = fitz.open(PDF)
page = doc[2]
print(f"Page rotation: {page.rotation}")

for annot in page.annots() or []:
    if annot.type[1] != "FreeText":
        continue
    content = annot.info.get("content", "").strip()
    if "NOTE-02" not in content:
        continue

    # Page is rotated 270; with the same approach used for NOTE-01 (added by
    # script with rotate=270), reposition NOTE-02 in the cajetin area on the
    # right margin of the page in landscape view. Use generous rect so the
    # 14pt text fits without truncation.
    new_rect = fitz.Rect(580, 1740, 1100, 1940)
    annot.set_rect(new_rect)

    annot.update(
        fontsize=13,
        fontname="helv",
        text_color=(0, 0, 0),
        fill_color=(1.0, 1.0, 0.7),  # MENOR yellow (matches NOTE)
        rotate=270,
    )
    annot.set_border(width=1.2)
    print(f"  [OK] NOTE-02 fixed — rect={new_rect}, rotate=270, fontsize=13")
    break

tmp = PDF + ".tmp"
doc.save(tmp)
doc.close()
os.replace(tmp, PDF)
print(f"PDF saved: {PDF}")
