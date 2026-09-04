"""
agregar_comentarios_structural_calc.py
UHPRO Structural Calculation Report Rev B (TM N29, Code 2). 2 NOTE (housekeeping).
El calculo esta ACEPTADO (corte basal NCh 2369:2003 Zona 3 = 41,62 kN;
utilizacion max 0,454 < 1,0; norma 2003, no 2025). Residuales de documentacion.

PDF de ~58 MB / 1101 paginas (concatenacion duplicada) -> NO usar run_comentarios
(guarda con garbage=4 y cuelga en PDFs grandes, ver feedback_doc_annotator_
garbage4_pdf_grande). Anotador directo PyMuPDF con garbage=1, deflate=False,
guardando primero al scratchpad y luego copiando al destino.
"""
import os
import shutil
import fitz  # PyMuPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..", "ENTREGAS_BWWATER", "ENTREGA 67",
    "25007-0067", "P22-CD-09-005-001_B UHPRO Structural Calculation Report.pdf"))
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-005-001_B_Structural_Calc_CC_ADASA.pdf")
SCRATCH = ("C:/Users/luisr/AppData/Local/Temp/claude/"
           "C--SynologyDrive-SynologyDrive-DESAROLLO-PROYECTOS-CLAUDE-"
           "MODULO-DE-SALMUERA-TALTAL/1bd6de80-400c-4556-9eaf-13a3464919fc/scratchpad")

NOTE_FILL = (0.85, 0.92, 1.0)   # azul claro (NOTE)
NOTE_BORDER = (0.0, 0.0, 0.8)

NOTE_01 = ("NOTE-01: this PDF is a duplicated concatenation of the same report "
           "(about 58 MB, 1101 pages = two copies of the 549-page report). "
           "Correct: issue a single, non-duplicated report file. The seismic "
           "calculation itself is accepted (base shear NCh 2369:2003 Zone 3 = "
           "41.62 kN; governing skid utilization 0.454 < 1.0).")

NOTE_02 = ("NOTE-02: the comment sheet records BW Water's replies to the "
           "Transmittal N26 comments without reproducing ADASA's original "
           "comment text. Correct: complete the comment sheet with the client "
           "comment text alongside each reply, so each closure is traceable.")


def add_note(page, text, y_top=40):
    r = page.rect
    w = min(430, r.width - 80)
    rect = fitz.Rect(40, y_top, 40 + w, y_top + 120)
    annot = page.add_freetext_annot(
        rect, text, fontsize=9, fontname="helv",
        text_color=(0, 0, 0), fill_color=NOTE_FILL)
    try:
        annot.set_colors(stroke=NOTE_BORDER, fill=NOTE_FILL)
        annot.set_border(width=1.2)
    except Exception:
        pass
    annot.update()
    return annot


def find_ccs_page(doc):
    """Primera pagina (en la 2a mitad) cuyo texto parezca la comment sheet."""
    for i in range(len(doc) - 1, max(0, len(doc) - 120), -1):
        t = (doc[i].get_text() or "").lower()
        if ("comment" in t and ("reply" in t or "response" in t or "n26" in t
                                or "addressed" in t)):
            return i
    return min(548, len(doc) - 1)  # fallback: pag 549 (0-based 548)


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"ERROR: source no encontrado:\n  {SRC}")
    os.makedirs(SCRATCH, exist_ok=True)
    doc = fitz.open(SRC)

    # NOTE-01 en la portada (pag 1)
    add_note(doc[0], NOTE_01, y_top=40)

    # NOTE-02 en la pagina de la comment sheet
    ccs = find_ccs_page(doc)
    add_note(doc[ccs], NOTE_02, y_top=40)
    print(f"NOTE-01 en pag 1; NOTE-02 en pag {ccs + 1} (0-based {ccs}).")

    tmp = os.path.join(SCRATCH, "struct_calc_cc_build.pdf")
    doc.save(tmp, garbage=1, deflate=False)
    doc.close()
    # verificar que abre
    chk = fitz.open(tmp); n = chk.page_count; chk.close()
    shutil.copyfile(tmp, PDF_OUT)
    size_mb = os.path.getsize(PDF_OUT) / 1e6
    print(f"CC_ADASA generado: {PDF_OUT} ({n} pags, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
