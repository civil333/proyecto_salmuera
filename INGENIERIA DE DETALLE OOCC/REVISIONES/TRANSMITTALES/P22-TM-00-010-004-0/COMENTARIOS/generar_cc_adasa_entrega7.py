# -*- coding: utf-8 -*-
"""
Genera los PDF/XLSX anotados (CC_ADASA) del TM N4 OOCC sobre la ENTREGA 7 de L&A.
Espejo 1:1 de los IDs de la tabla del transmittal (P22-TM-00-010-004-0).
Solo se anotan los comentarios ABIERTOS tras la verificacion de levantamiento
(ver _ANALISIS_TRABAJO.md). Los puntos levantados en E7 no se re-anotan.

Reglas (CLAUDE.md Seccion 3.8 + memorias):
- Codigo 2 y Codigo 3 llevan CC_ADASA; nunca Codigo 1.
- MC-002-003 y DWG-002-005 NO se anotan (archivos no recibidos).
- Documentos Codigo 1 (3 MC + 3 ET + DWG-002-001) NO llevan CC_ADASA.
- Texto de anotacion ASCII-safe (sin tildes/n/simbolos): el FreeText delata glifos.
- page_fallback 0-based (pagina visible N -> page_fallback N-1). Planos = 1 lamina/PDF -> 0.
- Planos rotados: la skill dibuja sobre la pagina rotada; verificar por render PNG aparte.
- Severidad por color del rectangulo (MAYOR naranja / MENOR amarillo); el texto NO la repite.
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

E7 = (r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/"
      r"INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 7")
SRC_DOC = E7 + "/Documentos"
SRC_PLN = E7 + "/Planos"


def C(idc, fill, text, page_fallback=0, origin="N2"):
    # Etiqueta de procedencia: deja explicito que el comentario ya se emitio en un
    # transmittal anterior (no es nuevo). Se inserta tras el ID en la primera linea.
    text = text.replace(f"{idc}:", f"{idc} (Transmittal {origin}):", 1)
    return {"id": idc, "fill": fill, "search": None,
            "page_fallback": page_fallback, "text": text}


# (nombre_archivo_fuente, carpeta_fuente, [comentarios])
PDFS = [
    # ===================== MEMORIAS DE CALCULO (Codigo 2) =====================
    ("P22-MC-00-002-001_2.pdf", SRC_DOC, [
        C("OBS-01", MAYOR,
          "OBS-01: Coherencia memoria-plano del anclaje.\n"
          "La coherencia entre la memoria y el plano (designacion y empotramiento del perno "
          "preinstalado) sigue pendiente; el plano de Detalles de Anclaje P22-DWG-00-002-005 "
          "no se ha entregado.\n"
          "Corregir: unificar designacion y empotramiento del perno entre memoria y plano, y "
          "conciliarlos con el plano de Detalles de Anclaje al re-emitirse.\n"
          "Requisito: ACI 318-19 Cap.17 y Sec.17.10; plano Exfibro EX-26005-F01 Rev 0.", 24),
        C("OBS-02", MAYOR,
          "OBS-02: Justificacion de la armadura de losa.\n"
          "La armadura se mantiene en Phi12@200 sin la justificacion solicitada: no se "
          "muestra la cuantia minima ni la verificacion de flexion/corte con las "
          "solicitaciones del anclaje.\n"
          "Corregir: justificar el calculo verificando la cuantia minima de ACI 318 y la "
          "flexion/corte; se recomienda Phi16@200.\n"
          "Requisito: ACI 318-19 (cuantia minima de retraccion y temperatura).", 35),
    ]),
    ("P22-MC-00-002-004_2.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Notacion del peso del contenedor.\n"
          "La memoria mantiene la notacion '17.334 [tonf]' y no declara explicitamente su "
          "adopcion como valor conservador frente al peso vinculante (14.934 kg).\n"
          "Corregir: corregir la notacion del peso y declarar su adopcion conservadora "
          "respecto del peso vinculante del contenedor RO.", 13),
    ]),
    # ===================== PLANOS DE OBRAS CIVILES =====================
    ("P22-DWG-00-001-001_C LAM 1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Alcance incompleto del plano.\n"
          "El plano cubre solo las zanjas de drenaje; faltan las excavaciones de las "
          "fundaciones.\n"
          "Corregir: incorporar las excavaciones de las fundaciones y los niveles de "
          "plataforma, o declarar el alcance parcial y referir los planos que las cubren.",
          origin="N3"),
        C("OBS-02", MAYOR,
          "OBS-02: Rellenos sin especificacion.\n"
          "Los rellenos no estan especificados y el cuadro de referencias esta vacio.\n"
          "Corregir: referir la Especificacion de Movimiento de Tierra P22-ET-00-010-101 "
          "(granulometria, % Proctor, material) y completar el cuadro de referencias.",
          origin="N3"),
        C("NOTA-01", MENOR,
          "NOTA-01: Nomenclatura, tags y escala.\n"
          "Corregir: adoptar la nomenclatura CD-06-00N, rotular los tags y agregar la barra "
          "de escala; corregir el typo 'relleno extructural'.",
          origin="N3"),
    ]),
    ("P22-DWG-00-001-001_C LAM 2.pdf", SRC_PLN, [
        C("OBS-03", MAYOR,
          "OBS-03: Rasante de la red de drenaje.\n"
          "Corregir: declarar la pendiente longitudinal y la cota de empalme (invert) en la "
          "camara de descarga existente.",
          origin="N3"),
        C("NOTA-01", MENOR,
          "NOTA-01: Nomenclatura, recubrimiento y escala.\n"
          "Corregir: adoptar la nomenclatura CD-06-00N; declarar el recubrimiento minimo "
          "sobre la tuberia; agregar la barra de escala.",
          origin="N3"),
    ]),
    ("P22-DWG-00-002-002_D LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nota de mejoramiento de suelo ausente.\n"
          "Corregir: agregar la nota de mejoramiento/tratamiento de suelo conforme a la "
          "Especificacion de Movimiento de Tierra P22-ET-00-010-101."),
    ]),
    ("P22-DWG-00-002-002_D LAM2.pdf", SRC_PLN, [
        C("NOTA-01", MENOR,
          "NOTA-01: Referencia al plano del proveedor.\n"
          "Corregir: corregir la referencia al plano del proveedor a EX-26005-F01 Rev 0."),
    ]),
    ("P22-DWG-00-002-002_D LAM4.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nota de mejoramiento de suelo ausente.\n"
          "Corregir: agregar la nota de mejoramiento/tratamiento de suelo."),
    ]),
    ("P22-DWG-00-002-003_D LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Mejoramiento de suelo y relleno.\n"
          "Corregir: agregar la nota de mejoramiento de suelo y especificar el relleno "
          "(material, espesor, % compactacion)."),
    ]),
    ("P22-DWG-00-002-004_D LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Capa 'M.H.A.' sin definir.\n"
          "Corregir: definir en notas/leyenda la capa de mejoramiento de suelo 'M.H.A.'."),
        C("NOTA-01", MENOR,
          "NOTA-01: Tag de la fosa.\n"
          "Corregir: unificar el tag de la fosa a TK-06-004 en todas las laminas."),
    ]),
    ("P22-DWG-00-002-004_D LAM2.pdf", SRC_PLN, [
        C("OBS-02", MAYOR,
          "OBS-02: Rebalse y material de la parrilla.\n"
          "Corregir: indicar y acotar las aperturas de rebalse; especificar la parrilla como "
          "pultruida de PRFV para transito liviano."),
    ]),
    ("P22-DWG-00-002-006_D LAM 3.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nomenclatura de camaras.\n"
          "Las laminas 1 y 2 no se re-emitieron y conservan la nomenclatura antigua.\n"
          "Corregir: re-emitir las laminas 1 y 2 adoptando la nomenclatura CD-06-00N."),
    ]),
    ("P22-DWG-00-002-007_D LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Mejoramiento de suelo, impermeabilizacion y fecha.\n"
          "Corregir: agregar las notas de mejoramiento de suelo e impermeabilizacion y "
          "corregir la fecha del cajetin (la lamina 3, con la misma observacion, no se "
          "re-emitio)."),
    ]),
    ("P22-DWG-00-003-001_0 LAM1.pdf", SRC_PLN, [
        C("NOTA-01", MENOR,
          "NOTA-01: Sigla del documento en la nota C5-M.\n"
          "La nota de proteccion C5-M con la sigla a corregir vive en la lamina 2, no "
          "re-emitida en esta entrega.\n"
          "Corregir: re-emitir la lamina 2 con la sigla corregida a P22-ET-00-010-103-0."),
    ]),
]


def anotar_pdfs():
    for fn, src_dir, comentarios in PDFS:
        local = os.path.join(SCRIPT_DIR, fn)
        out = os.path.join(SCRIPT_DIR, os.path.splitext(fn)[0] + "_CC_ADASA.pdf")
        if not os.path.exists(local):
            shutil.copy2(os.path.join(src_dir, fn), local)
        run_comentarios(local, out, comentarios)
        print(f"  OK  {os.path.basename(out)}  ({len(comentarios)} anot.)")


def anotar_itemizados():
    """IT Codigo 2: notas Excel via openpyxl. Solo queda la Clase 2 AACE (los tres)
    y la partida de soldadura (IT-103)."""
    import openpyxl
    from openpyxl.comments import Comment

    AUTOR = "ADASA"
    PRESUP = "Detalle Presupuesto"

    aace = ("OBS-01 (Transmittal N2): Clase de estimacion no declarada.\n"
            "El Itemizado mantiene el rotulo 'presupuesto referencial' sin declarar la "
            "clase de estimacion.\n"
            "Corregir: declarar la clase de estimacion Clase 2 AACE "
            "(Minuta 067-032-032-COR-MI-001).")
    soldadura = ("OBS-02 (Transmittal N2): Partida de soldadura.\n"
                 "La proteccion C5-M se incorporo, pero la soldadura sigue absorbida en la "
                 "partida 'Conexiones' sin linea propia.\n"
                 "Corregir: incorporar la partida de soldadura como item explicito, en linea "
                 "con la Especificacion de Estructura Metalica.")

    # (archivo, [(hoja, celda, texto)])
    ITS = {
        "P22-IT-00-010-101-0_D.xlsx": [(PRESUP, "B5", aace)],
        "P22-IT-00-010-102-0_D.xlsx": [(PRESUP, "B5", aace)],
        "P22-IT-00-010-103-0_D.xlsx": [(PRESUP, "B5", aace), (PRESUP, "D17", soldadura)],
    }
    for fn, notas in ITS.items():
        local = os.path.join(SCRIPT_DIR, fn)
        out = os.path.join(SCRIPT_DIR, os.path.splitext(fn)[0] + "_CC_ADASA.xlsx")
        if not os.path.exists(local):
            shutil.copy2(os.path.join(SRC_DOC, fn), local)
        wb = openpyxl.load_workbook(local)
        for hoja, celda, texto in notas:
            ws = wb[hoja]
            cm = Comment(texto, AUTOR)
            cm.width = 320
            cm.height = 170
            ws[celda].comment = cm
        wb.save(out)
        print(f"  OK  {os.path.basename(out)}  ({len(notas)} notas)")


if __name__ == "__main__":
    print("== PDF (MC + planos) ==")
    anotar_pdfs()
    print("== XLSX (Itemizados) ==")
    anotar_itemizados()
    print("Listo.")
