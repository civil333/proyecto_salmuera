# -*- coding: utf-8 -*-
"""
Genera los PDF/XLSX anotados (CC_ADASA) del TM N3 OOCC sobre la ENTREGA 5 de L&A.
Espejo 1:1 de los IDs de la tabla del transmittal (P22-TM-00-010-003-0).

Reglas (CLAUDE.md Seccion 3.8 + memorias):
- Codigo 2 y Codigo 3 llevan CC_ADASA; nunca Codigo 1.
- MC-002-003 NO se anota (archivo no recibido).
- Texto de anotacion ASCII-safe (sin tildes/n/simbolos): el FreeText delata glifos faltantes.
- page_fallback 0-based (pagina visible N -> page_fallback N-1). Planos = 1 lamina/PDF -> 0.
- Planos rotados: la skill dibuja directamente sobre la pagina rotada; verificar por render PNG aparte.
- Severidad por color del rectangulo (MAYOR naranja / MENOR amarillo); el texto NO la repite.
"""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

E5 = (r"C:/SynologyDrive/SynologyDrive/DESAROLLO PROYECTOS CLAUDE/MODULO DE SALMUERA TALTAL/"
      r"INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 5")
SRC_DOC = E5 + "/Documentos"
SRC_PLN = E5 + "/Planos"


def C(idc, fill, text, page_fallback=0):
    return {"id": idc, "fill": fill, "search": None,
            "page_fallback": page_fallback, "text": text}


# (nombre_archivo_fuente, carpeta_fuente, [comentarios])
PDFS = [
    # ===================== MEMORIAS DE CALCULO (Codigo 2) =====================
    ("P22-MC-00-002-001_1.pdf", SRC_DOC, [
        C("OBS-01", MAYOR,
          "OBS-01: Coherencia memoria-plano del anclaje.\n"
          "La memoria declara el anclaje preinstalado pero conserva la varilla HAS-V-36 "
          "(anclaje quimico) y empotramiento 40 cm; el plano de fundacion especifica barra "
          "ASTM F1554 con tuerca y placa embebidas y empotramiento ~38 cm.\n"
          "Corregir: unificar la designacion del perno preinstalado (barra ASTM F1554 embebida, "
          "sin nomenclatura de anclaje quimico) y el empotramiento memoria-plano; mostrar la "
          "verificacion por los modos de falla de preinstalado.\n"
          "Requisito: ACI 318-19 Cap.17 y Sec.17.10; plano Exfibro EX-26005-F01 Rev C.", 23),
        C("OBS-02", MAYOR,
          "OBS-02: Justificacion de la armadura de losa.\n"
          "La armadura paso a Phi12@200 y se retiro la verificacion asociada; no se muestra la "
          "cuantia resultante ni el espesor de losa.\n"
          "Corregir: justificar el calculo de la armadura verificando la cuantia minima de "
          "ACI 318 y la flexion/corte con las solicitaciones del anclaje; se recomienda Phi16@200.\n"
          "Requisito: ACI 318-19 (cuantia minima de retraccion y temperatura).", 32),
        C("NOTA-01", MENOR,
          "NOTA-01: Trazabilidad de las reacciones basales.\n"
          "Adopta las reacciones corregidas por ADASA (Ez = +/-3.357 kgf) pero cita como fuente "
          "la 'Memoria Estanque AFTA Taltal'.\n"
          "Corregir: citar P22-IT-06-000-005-0 como fuente vinculante de las reacciones.", 23),
        C("NOTA-02", MENOR,
          "NOTA-02: Recubrimientos.\n"
          "No se declaran los recubrimientos minimos.\n"
          "Corregir: declarar los recubrimientos minimos en ambas condiciones: "
          "50 mm en elementos expuestos y 70 mm en contacto con el terreno.\n"
          "Requisito: Terminos de Referencia, Seccion 3.3.4.", 32),
    ]),
    ("P22-MC-00-002-002_1.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Recubrimientos.\n"
          "La memoria declara el recubrimiento en contacto con terreno (70 mm), pero falta el "
          "de elementos expuestos. El anclaje postinstalado de la bomba se acepta conforme a "
          "los planos KSB.\n"
          "Corregir: declarar los recubrimientos minimos en ambas condiciones: 50 mm en "
          "elementos expuestos y 70 mm en contacto con el terreno.\n"
          "Requisito: Terminos de Referencia, Seccion 3.3.4.", 7),
    ]),
    ("P22-MC-00-002-004_1.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Recubrimientos.\n"
          "No se declaran los recubrimientos minimos.\n"
          "Corregir: declarar los recubrimientos minimos en ambas condiciones: 50 mm en "
          "elementos expuestos y 70 mm en contacto con el terreno.\n"
          "Requisito: Terminos de Referencia, Seccion 3.3.4.", 13),
    ]),
    ("P22-MC-00-002-005_1.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Recubrimientos.\n"
          "La memoria declara el recubrimiento en contacto con terreno (70 mm), pero falta el "
          "de elementos expuestos. El diferimiento de los anclajes CIP es conforme (queda en "
          "seguimiento hasta recibir los planos del proveedor).\n"
          "Corregir: declarar los recubrimientos minimos en ambas condiciones: 50 mm en "
          "elementos expuestos y 70 mm en contacto con el terreno.\n"
          "Requisito: Terminos de Referencia, Seccion 3.3.4.", 7),
    ]),
    ("P22-MC-00-003-001_1.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Recubrimientos y combinacion de cargas.\n"
          "No se declaran los recubrimientos de los pedestales y la combinacion de cargas se "
          "expresa como '1,2D+/-E'.\n"
          "Corregir: declarar los recubrimientos minimos en ambas condiciones (50 mm en "
          "elementos expuestos y 70 mm en contacto con el terreno) y dejar explicita la "
          "combinacion de cargas adoptada.\n"
          "Requisito: Terminos de Referencia, Seccion 3.3.4; NCh 2369.", 23),
    ]),
    # ===================== ESPECIFICACIONES TECNICAS (Codigo 2) =====================
    ("P22-ET-00-010-101-0_0.pdf", SRC_DOC, [
        C("OBS-01", MAYOR,
          "OBS-01: Tension admisible del suelo.\n"
          "Se incorporaron las condiciones de mejoramiento de suelo, pero no se declara la "
          "tension admisible de diseno.\n"
          "Corregir: declarar la tension admisible adoptada sigma_adm <= 1,0 kg/cm2 y eliminar "
          "la referencia residual a 'Municipalidad de Antofagasta'.\n"
          "Requisito: Terminos de Referencia (tension admisible de diseno).", 6),
    ]),
    ("P22-ET-00-010-102-0_0.pdf", SRC_DOC, [
        C("NOTA-01", MENOR,
          "NOTA-01: Codigo de portada.\n"
          "Los recubrimientos duales y la impermeabilizacion quedaron incorporados; la portada "
          "conserva un codigo tipo IT.\n"
          "Corregir: corregir el codigo de portada a P22-ET-00-010-102-0.\n"
          "Requisito: codificacion del proyecto.", 0),
    ]),
    ("P22-ET-00-010-103-0_0.pdf", SRC_DOC, [
        C("OBS-02", MAYOR,
          "OBS-02: Esquema C5-M por capas y perneria.\n"
          "Declara la clasificacion C5-M sin el esquema por capas (SSPC-SP10 + zinc + epoxico + "
          "poliuretano), que ya esta desarrollado en la memoria de la cubierta, y no exige "
          "perneria protegida para ambiente expuesto.\n"
          "Corregir: trasladar a la Especificacion el esquema por capas con su preparacion de "
          "superficie y exigir perneria galvanizada en caliente o inoxidable; corregir el codigo "
          "tipo IT de la portada.\n"
          "Requisito: Terminos de Referencia, Seccion 3.4.2; ISO 12944.", 10),
    ]),
    # ===================== PLANOS (Codigo 3, y -003-001 Codigo 2) =====================
    ("P22-DWG-00-001-001_B LAM 1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Alcance incompleto del plano.\n"
          "El plano cubre solo las zanjas de drenaje; faltan las excavaciones de las fundaciones "
          "(estanque, bomba, fosa, contenedor RO, Sistema CIP), los niveles de plataforma y el "
          "N.T.N. por zona.\n"
          "Corregir: incorporar las excavaciones de fundaciones y los niveles de plataforma, o "
          "declarar el alcance parcial y referir los planos que las cubren; declarar el N.T.N. "
          "por zona (montaje P22-DWG-06-005-103)."),
        C("OBS-02", MAYOR,
          "OBS-02: Rellenos sin especificacion.\n"
          "'Arena limpia compactada' y 'relleno estructural' sin granulometria, % de compactacion "
          "ni calidad del material; el cuadro de referencias esta vacio.\n"
          "Corregir: referir la Especificacion de Movimiento de Tierra P22-ET-00-010-101 y "
          "declarar granulometria, % Proctor y material libre de sales, cloruros y sulfatos; "
          "completar el cuadro de referencias."),
        C("NOTA-01", MENOR,
          "NOTA-01: Nomenclatura, tags y typos.\n"
          "Las camaras no usan la codificacion CD-06-00N; estanque/bomba/fosa/contenedores sin "
          "TAG; la tuberia sin tag de linea; typo 'relleno extructural'.\n"
          "Corregir: rotular CD-06-001 a CD-06-007, los TAGs de equipos y el tag de linea; "
          "declarar el recubrimiento minimo sobre la tuberia; corregir el typo."),
    ]),
    ("P22-DWG-00-001-001_B LAM 2.pdf", SRC_PLN, [
        C("OBS-03", MAYOR,
          "OBS-03: Rasante de la red de drenaje.\n"
          "No se declara la pendiente longitudinal de proyecto de la tuberia por gravedad ni la "
          "cota de empalme (invert) en la camara de descarga existente.\n"
          "Corregir: declarar la pendiente longitudinal de la linea por gravedad y la cota invert "
          "de empalme; verificar la pendiente minima."),
        C("NOTA-01", MENOR,
          "NOTA-01: Nomenclatura, tags y typos.\n"
          "Las camaras no usan la codificacion CD-06-00N; falta el recubrimiento minimo sobre la "
          "clave de la tuberia; sin barra de escala grafica.\n"
          "Corregir: rotular CD-06-001 a CD-06-007; declarar el recubrimiento minimo sobre la "
          "tuberia; agregar barra de escala grafica."),
    ]),
    ("P22-DWG-00-002-001_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: N.T.N. por zona sin acotar.\n"
          "La implantacion no acota el N.T.N. por zona; las llamadas solo remiten a los planos "
          "de fundacion (el cuadro de coordenadas UTM ya fija el azimut).\n"
          "Corregir: acotar el N.T.N. por zona, coincidente con los planos de montaje "
          "P22-DWG-06-005-101/-103/-105 y el Levantamiento DIO."),
        C("NOTA-01", MENOR,
          "NOTA-01: Tag de la fosa y sigla de la nota C5-M.\n"
          "La fosa figura como TK-06-002 y la nota de proteccion C5-M cita la sigla P22-IT.\n"
          "Corregir: corregir el tag de la fosa a TK-06-004 y la sigla del documento a "
          "P22-ET-00-010-103-0."),
    ]),
    ("P22-DWG-00-002-002_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nota de mejoramiento de suelo ausente.\n"
          "Las notas particulares solo remiten a las generales y al plano vendor; el relleno no "
          "esta especificado.\n"
          "Corregir: agregar la nota con las condiciones de mejoramiento/tratamiento de suelo, "
          "conforme a la Especificacion de Movimiento de Tierra P22-ET-00-010-101."),
    ]),
    ("P22-DWG-00-002-002_C LAM2.pdf", SRC_PLN, [
        C("NOTA-01", MENOR,
          "NOTA-01: Designacion del perno PA-1 y referencia vendor.\n"
          "La marca PA-1 figura como preinstalado en una lamina y postinstalado en otra; la "
          "referencia vendor aparece como EX-2600-F01.\n"
          "Corregir: conciliar la designacion de PA-1 entre laminas y corregir la referencia al "
          "plano del proveedor (EX-26005-F01 Rev C)."),
    ]),
    ("P22-DWG-00-002-002_C LAM4.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nota de mejoramiento de suelo ausente.\n"
          "Las notas particulares solo remiten a las generales y al plano vendor KSB; el relleno "
          "no esta especificado.\n"
          "Corregir: agregar la nota con las condiciones de mejoramiento/tratamiento de suelo."),
        C("NOTA-01", MENOR,
          "NOTA-01: Designacion del perno PA-1 y referencia vendor.\n"
          "La marca PA-1 figura como preinstalado en una lamina y postinstalado en otra; la "
          "referencia vendor aparece como EX-2600-F01.\n"
          "Corregir: conciliar la designacion de PA-1 entre laminas y corregir la referencia al "
          "plano del proveedor (EX-26005-F01 Rev C)."),
    ]),
    ("P22-DWG-00-002-003_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nota de mejoramiento de suelo ausente.\n"
          "Las cotas quedaron en N.T.N. absoluto, pero falta la nota de mejoramiento de suelo; "
          "el cuadro cuantifica relleno 30,03 m3 sin material/espesor/% compactacion.\n"
          "Corregir: agregar la nota con las condiciones de mejoramiento de suelo y especificar "
          "el relleno (P22-ET-00-010-101)."),
    ]),
    ("P22-DWG-00-002-004_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Mejoramiento de suelo e impermeabilizacion.\n"
          "La capa grafica 'M.H.A. e=15' bajo el sello no esta definida en notas ni leyenda; la "
          "impermeabilizacion de los elementos enterrados no esta completa en la lamina.\n"
          "Corregir: declarar el mejoramiento de suelo (definir 'M.H.A.') y completar la "
          "impermeabilizacion de los elementos enterrados."),
        C("NOTA-01", MENOR,
          "NOTA-01: Tag de la fosa.\n"
          "El cajetin de la lamina 1 dice TK-06-004 pero la lamina 2 conserva TK-006-002.\n"
          "Corregir: unificar el tag de la fosa a TK-06-004 en todas las laminas."),
    ]),
    ("P22-DWG-00-002-004_C LAM2.pdf", SRC_PLN, [
        C("OBS-02", MAYOR,
          "OBS-02: Rebalse y material de la parrilla.\n"
          "No se indican las aperturas de rebalse del estanque; el detalle conserva la "
          "designacion 'PARRILLA PISO ARS-5' (acero).\n"
          "Corregir: agregar y acotar las aperturas de rebalse; especificar la parrilla como "
          "pultruida de PRFV para transito liviano de personas."),
    ]),
    ("P22-DWG-00-002-006_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Nomenclatura de camaras.\n"
          "Las camaras siguen rotuladas 'CAMARA N1...N7 PROYECTADA' (las pendientes ya quedaron "
          "acotadas en el perfil).\n"
          "Corregir: adoptar la nomenclatura CD-06-001 a CD-06-00N para las camaras."),
        C("NOTA-01", MENOR,
          "NOTA-01: Detalle de camara y revision del cajetin.\n"
          "Falta el detalle tipico de camara prefabricada (anunciado como lamina 3, no entregada) "
          "y coexisten Rev B y Rev C en el cajetin.\n"
          "Corregir: incorporar el detalle tipico de camara prefabricada y unificar la revision "
          "del cajetin."),
    ]),
    ("P22-DWG-00-002-006_C LAM2.pdf", SRC_PLN, [
        C("NOTA-01", MENOR,
          "NOTA-01: Detalle de camara y revision del cajetin.\n"
          "Falta el detalle tipico de camara prefabricada (anunciado como lamina 3, no entregada) "
          "y coexisten Rev B y Rev C en el cajetin.\n"
          "Corregir: incorporar el detalle tipico de camara prefabricada y unificar la revision "
          "del cajetin."),
    ]),
    ("P22-DWG-00-002-007_C LAM1.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Mejoramiento de suelo, impermeabilizacion y fecha.\n"
          "El N.T.N. ya se reconcilio a +6,000, pero faltan las notas de mejoramiento de suelo e "
          "impermeabilizacion; el cajetin tiene la fecha 09/09/26.\n"
          "Corregir: agregar las notas de mejoramiento de suelo e impermeabilizacion; corregir la "
          "fecha del cajetin a 09/06/26."),
    ]),
    ("P22-DWG-00-002-007_C LAM3.pdf", SRC_PLN, [
        C("OBS-01", MAYOR,
          "OBS-01: Mejoramiento de suelo e impermeabilizacion.\n"
          "Faltan las notas de mejoramiento de suelo e impermeabilizacion; el cuadro de "
          "excavacion cuantifica relleno 1,96 m3 sin especificacion.\n"
          "Corregir: agregar las notas de mejoramiento de suelo e impermeabilizacion y "
          "especificar el relleno."),
    ]),
    ("P22-DWG-00-003-001_C LAM1.pdf", SRC_PLN, [
        C("NOTA-01", MENOR,
          "NOTA-01: Sigla del documento en la nota C5-M.\n"
          "La nota de proteccion C5-M cita la sigla P22-IT.\n"
          "Corregir: corregir la sigla del documento citado a P22-ET-00-010-103-0."),
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
    """IT Codigo 3: notas Excel via openpyxl (Codigo 3 -> CC_ADASA)."""
    import openpyxl
    from openpyxl.comments import Comment

    AUTOR = "ADASA"
    PRESUP = "Detalle Presupuesto"
    BOM = "BOM"

    cls = ("OBS-01: Clase de estimacion no declarada.\n"
           "Declarar la clase de estimacion acordada en la reunion de arranque: "
           "Clase 2 AACE (Minuta 067-032-032-COR-MI-001).")
    fosa = ("OBS-02: Tag de la fosa.\n"
            "Figura 'TK-06-002', que es el estanque CIP de BW Water.\n"
            "Corregir: corregir el tag de la fosa a TK-06-004.")
    chimba = ("OBS-02: Pestana ajena al proyecto.\n"
              "La hoja 'Cuadro de Piezas Especiales Interconexion La Chimba' no pertenece a "
              "este proyecto.\n"
              "Corregir: eliminar la pestana 'La Chimba' del libro.")
    imperm = ("OBS-03: Partida de impermeabilizacion faltante.\n"
              "La Especificacion de Obras Civiles ya especifica la impermeabilizacion (Sika Igol) "
              "pero el Itemizado no la presupuesta.\n"
              "Corregir: incorporar la partida de impermeabilizacion de elementos enterrados.")
    pintsold = ("OBS-03: Partidas de proteccion y soldadura faltantes.\n"
                "La Especificacion de Estructura Metalica declara la proteccion C5-M y la "
                "soldadura, pero el Itemizado no las presupuesta.\n"
                "Corregir: incorporar las partidas de proteccion superficial (C5-M) y soldadura.")

    # (archivo, [(hoja, celda, texto)])
    ITS = {
        "P22-IT-00-010-101-0_C.xlsx": [
            (PRESUP, "B5", cls), (PRESUP, "D23", fosa), (BOM, "A1", chimba)],
        "P22-IT-00-010-102-0_C.xlsx": [
            (PRESUP, "B5", cls), (PRESUP, "D23", fosa), (PRESUP, "B6", imperm),
            (BOM, "A1", chimba)],
        "P22-IT-00-010-103-0_C.xlsx": [
            (PRESUP, "B5", cls), (PRESUP, "B6", pintsold), (BOM, "A1", chimba)],
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
            cm.height = 160
            ws[celda].comment = cm
        wb.save(out)
        print(f"  OK  {os.path.basename(out)}  ({len(notas)} notas)")


if __name__ == "__main__":
    print("== PDF (MC + ET + planos) ==")
    anotar_pdfs()
    print("== XLSX (Itemizados) ==")
    anotar_itemizados()
    print("Listo.")
