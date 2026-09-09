#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CC_ADASA de la ENTREGA 14 (carta 067-032-032-COR-TT-015) y de los dos planos de
fundaciones con los que su cuadro de cubicaciones entra en contradiccion.

CRITERIO: solo se comentan DISCREPANCIAS ENTRE PLANOS, del tipo un plano declara X
y otro declara Y para la misma excavacion o la misma cota. La instruccion es siempre
la misma, dejar una sola cifra, y por eso cada recuadro cabe en pocas lineas. Los
puntos de control documental quedaron fuera: el cajetin ya identifica la revision 1
y las nubes de revision estan puestas.

NUMERACION: serie unica para todo el paquete de comentarios, OBS-01 a OBS-07, corrida
por el orden en que se leen los planos. Cada identificador es unico en el envio, de
modo que la peticion a L&A se resume en una linea y las dos discrepancias que
aparecen en dos planos se citan entre si. Los identificadores son de ESTE paquete,
del 09-09-2026, no del historial de cada plano: los OBS-01 a OBS-03 que el
P22-DWG-00-001-001 uso en sus revisiones B y C son otra cosa y quedaron cerrados al
aceptarse la revision 0.

Reglas del metodo (mismas del generar_cc_adasa_entrega5.py del Transmittal N3):
  - Solo se importa MAYOR. Las siete observaciones exigen correccion, de modo que no
    hay notas menores: el stream OOCC es 100 % espanol y su identificador de nota
    seria NOTA-XX.
  - Texto de las cajas en ASCII puro, sin tildes ni enes: el cuadro delata los
    glifos que faltan.
  - La severidad la da el color del rectangulo; el texto no la repite.
  - search=None y page_fallback=0: en planos la busqueda de texto no ancla, y las
    dos laminas del movimiento de tierra estan vectorizadas, sin capa de texto util.
  - Formato de cada comentario: "ID: Titulo." -> que dice cada plano -> "Corregir:".
  - Planos rotados: la skill dibuja en el flujo de contenido, de modo que
    page.annots() devuelve cero aunque el comentario sea visible. La verificacion
    de cierre es por render PNG y por extraccion de texto.
  - El alto util de estas laminas es el lado corto, 842 puntos, y la caja minima de
    la skill son 140: no caben mas de cuatro recuadros por lamina.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROY = r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL"
E14 = PROY + "/INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 14/Planos"
PKG = (PROY + "/BASES DE LICITACION MONTAJE MECANICO-OOCC/"
              "INGENIERIA VIGENTE PARA CONSTRUCCION/2. OBRAS CIVILES/PLANOS")


def C(idc, fill, text, page_fallback=0, offset_y=0):
    return {"id": idc, "fill": fill, "search": None,
            "page_fallback": page_fallback, "text": text, "offset_y": offset_y}


PDFS = [
    # ------------------------------------------------ P22-DWG-00-001-001 LAM 1
    ("P22-DWG-00-001-001-1-LAM 1.pdf", E14, [
        C("OBS-01", MAYOR,
          "OBS-01: Excavacion de la zona del sistema CIP.\n"
          "Este plano declara 1,03 m3 en el item 7. El P22-DWG-00-002-007 LAM1 "
          "rev. 1 declara 1,60 m3.\n"
          "Corregir: dejar una sola cifra en ambos planos. Ver OBS-07."),
        C("OBS-02", MAYOR,
          "OBS-02: Excavacion del contenedor.\n"
          "Este plano declara 20,95 m3 en el item 8. El P22-DWG-00-002-003 LAM1 "
          "rev. 1 declara 38,02 m3.\n"
          "Corregir: dejar una sola cifra en ambos planos. Ver OBS-06."),
        C("OBS-03", MAYOR,
          "OBS-03: Dos excavaciones que el cuadro no recoge.\n"
          "El P22-DWG-00-002-002 LAM4 declara 0,62 m3 para la fundacion de la bomba "
          "BH-06-001, y el P22-DWG-00-002-007 LAM3 declara 4,25 m3 para la fundacion "
          "de la cubierta del sistema CIP.\n"
          "Corregir: incorporar ambas al cuadro."),
    ]),

    # ------------------------------------------------ P22-DWG-00-001-001 LAM 2
    ("P22-DWG-00-001-001-1-LAM 2.pdf", E14, [
        C("OBS-04", MAYOR,
          "OBS-04: Fondo de excavacion del estanque TK-06-001.\n"
          "Las secciones A y B lo acotan en EL. 5,35. El P22-DWG-00-002-002 LAM1 "
          "rev. 1 fija el sello en +5,350 con emplantillado de 5 cm bajo el, de donde "
          "el fondo resulta 5,30.\n"
          "Corregir: dejar una sola cota en ambos planos."),
        C("OBS-05", MAYOR,
          "OBS-05: Fondo de excavacion de la fosa TK-06-004.\n"
          "La seccion B lo acota en EL. 4,30. El P22-DWG-00-002-004 LAM1 fija el "
          "sello en +4,305 con mejoramiento M.H.A. de 15 cm bajo el, de donde el "
          "fondo resulta 4,155.\n"
          "Corregir: dejar una sola cota en ambos planos."),
    ]),

    # ------------------------------------------------ P22-DWG-00-002-003 LAM 1
    ("P22-DWG-00-002-003_1 LAM1.pdf", PKG, [
        C("OBS-06", MAYOR,
          "OBS-06: Excavacion del contenedor.\n"
          "Este cuadro declara 38,02 m3. El P22-DWG-00-001-001 LAM1 rev. 1 declara "
          "20,95 m3.\n"
          "Corregir: dejar una sola cifra en ambos planos. Ver OBS-02."),
    ]),

    # ------------------------------------------------ P22-DWG-00-002-007 LAM 1
    ("P22-DWG-00-002-007_1 LAM1.pdf", PKG, [
        C("OBS-07", MAYOR,
          "OBS-07: Excavacion de la zona del sistema CIP.\n"
          "Este cuadro declara 1,60 m3. El P22-DWG-00-001-001 LAM1 rev. 1 declara "
          "1,03 m3.\n"
          "Corregir: dejar una sola cifra en ambos planos. Ver OBS-01."),
    ]),
]


def anotar_pdfs():
    total = 0
    for fn, src_dir, comentarios in PDFS:
        local = os.path.join(SCRIPT_DIR, fn)
        out = os.path.join(SCRIPT_DIR, os.path.splitext(fn)[0] + "_CC_ADASA.pdf")
        if not os.path.exists(local):
            shutil.copy2(os.path.join(src_dir, fn), local)
        run_comentarios(local, out, comentarios)
        print(f"  OK  {os.path.basename(out)}  ({len(comentarios)} anot.)")
        total += len(comentarios)
    print(f"\nTotal: {len(PDFS)} PDF, {total} comentarios.")


if __name__ == "__main__":
    anotar_pdfs()
