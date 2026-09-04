#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate and reformat the user's existing FreeText annotation on the Civil
and Loading Drawing CC ADASA PDF into the formal English NOTE-01 of
Transmittal N16 (P22-TM-09-000-016-0).

Follows CLAUDE.md §3.11 pattern: PyMuPDF set_info(content=) + update() to
preserve rect, color, and font size of the original annotation.
"""

import os
import shutil
import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_SRC = os.path.normpath(os.path.join(
    SCRIPT_DIR, "..", "..", "..", "..",
    "ENTREGAS_BWWATER", "ENTREGA 34",
    "P22-DWG-09-005-001_A Civil and Loading Layout (CC ADASA).pdf",
))
PDF_OUT = os.path.join(
    SCRIPT_DIR,
    "P22-DWG-09-005-001_A_Civil_and_Loading_Layout_CC_ADASA.pdf",
)

ORIGINAL_ES = "Indicar el peso del container modificado"

NOTE_01_EN = (
    "NOTE-01 — Weight Disclosure\n"
    "\n"
    "Please include on Rev 0 (IFC):\n"
    "\n"
    "(a) Total weight of the modified 40 ft container.\n"
    "\n"
    "(b) Confirm the RO Skid operating weight "
    "(items 6-7, 8,058 kg) fully accounts for all "
    "interior piping (super-duplex HP + process), "
    "including steel mass, fluid inventory and fittings, "
    "together with skid frame, pressure vessels and wet "
    "membranes. If any piping mass is excluded, declare "
    "it separately."
)


def main() -> None:
    if not os.path.exists(PDF_SRC):
        raise SystemExit(f"Source PDF not found: {PDF_SRC}")

    shutil.copy2(PDF_SRC, PDF_OUT)
    print(f"Copied: {PDF_OUT}")

    doc = fitz.open(PDF_OUT)
    replaced = 0

    for page in doc:
        for annot in page.annots() or []:
            content = annot.info.get("content", "").strip()
            if content == ORIGINAL_ES:
                annot.set_info(content=NOTE_01_EN)
                annot.update()
                replaced += 1
                print(
                    f"  Replaced annotation on page {page.number + 1} "
                    f"rect={annot.rect}"
                )

    if replaced == 0:
        doc.close()
        raise SystemExit("ERROR: original Spanish annotation not found.")

    tmp = PDF_OUT + ".tmp"
    doc.save(tmp)
    doc.close()
    os.replace(tmp, PDF_OUT)

    print(f"Done. {replaced} annotation(s) replaced.")


if __name__ == "__main__":
    main()
