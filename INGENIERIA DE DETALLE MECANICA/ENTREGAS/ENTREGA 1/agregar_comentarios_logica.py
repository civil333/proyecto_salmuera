#!/usr/bin/env python3
"""
agregar_comentarios_logica.py
=====================================================================
Agrega 21 comentarios de revisión ADASA al documento:
  P22-IT-06-008-101-B (Lógica).docx  →  P22-IT-06-008-101-B_ADASA-Review.docx

Técnica: manipulación directa del XML interno del DOCX (zipfile + lxml).
No usa python-docx — su API no expone la estructura de comentarios Word.

Estructura XML utilizada:
  word/document.xml  — inserta w:commentRangeStart/End + annotationRef
  word/comments.xml  — agrega los 21 elementos w:comment nuevos

El archivo ya contiene 4 comentarios de Ronald Pellejero Salazar
(IDs grandes: 560356254, 986060982, 1890286742, 1839200811).
Los nuevos usan IDs 1-21 — sin colisión.

Historial:
  2026-02-28  GAP-01 a GAP-06: revisión técnica original
  2026-03-06  GAP-02 y GAP-03: actualizados — BS-06-001 confirmada eliminada (terreno)
              GAP-07 (nuevo): válvulas VM-06-001 / VM-06-002 no incluidas en lógica
  2026-03-19  RS-01 a RS-14: 14 comentarios Ronald Pellejero Salazar (18-Mar-2026)

Autor : Luis Rivera | ADASA
"""

import os
import shutil
import zipfile
from lxml import etree

# ── Rutas ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE_DIR, "P22-IT-06-008-101-B (Lógica).docx")
DST = os.path.join(BASE_DIR, "P22-IT-06-008-101-B_ADASA-Review.docx")

# ── Namespaces ─────────────────────────────────────────────────────────────────
W_NS  = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"

def wt(name):
    """Devuelve el tag en namespace Word: {W_NS}name."""
    return f"{{{W_NS}}}{name}"

# ── Datos de los 6 comentarios ADASA ──────────────────────────────────────────
AUTHOR   = "Luis Rivera"
INITIALS = "LR"
DATE     = "2026-03-01T00:00:00Z"

COMMENTS = [
    {
        "id": 1,
        "text": (
            "Secuencia de arranque incompleta. El documento lista los permisivos pero omite "
            "los pasos posteriores: frecuencia inicial del VFD en BH-06-001, timeout de "
            "confirmación de presión en PIT-06-001, timing del pulso a OI-06-003, y timeout "
            "de confirmación de marcha de OI-06-004. Requiere definición antes de la "
            "programación del PLC."
        ),
        # Para 211: "Encendido de Bomba de alimentación salmuera BH-06-001."
        "search": ["Encendido de Bomba de alimentación", "Encendido de Bomba"],
        "label": "Secuencia arranque (GAP-01)",
    },
    {
        "id": 2,
        "text": (
            "Error de tag: BH-03-001 no corresponde a este proyecto; el tag correcto es BH-06-001. "
            "Además, la secuencia de parada está incompleta: no se define el estado final de las "
            "válvulas (VM-06-001, VM-06-002 y cualquier válvula instrumentada), ni el timeout de "
            "confirmación de parada de OI-06-004. "
            "Nota ADASA (confirmado en terreno, 06-Mar-2026): BS-06-001 (bomba sumergible de "
            "drenajes) se elimina del proyecto. Los drenajes y rebalses de TK-06-001 se manejarán "
            "gravitacionalmente al descarte de salmuera del sector. La secuencia de parada en Rev C "
            "debe omitir toda referencia a BS-06-001 y documentar el manejo gravitatorio de drenajes."
        ),
        # Para 219: "Parada Bomba de bomba de alimentación BH-03-001." — único en el doc
        "search": ["BH-03-001"],
        "label": "Tag + secuencia parada (GAP-02)",
    },
    {
        "id": 3,
        "text": (
            "Tabla de bandas de nivel ausente para TK-06-001. Solo se define el permisivo "
            "de arranque (>70%). Se requiere documentar: rango operacional normal, bandas de "
            "alarma (LAH / LAL), umbral de desborde (~2%) y acción de control asociada a cada banda. "
            "Nota ADASA (confirmado en terreno, 06-Mar-2026): BS-06-001 se elimina del proyecto. "
            "Para la banda de desborde (~2%), la acción de control en Rev C debe indicar: parada "
            "de OI (señal OI-06-005 = stop) y desborde gravitatorio hacia descarte del sector, sin "
            "activación de bomba sumergible. No se requiere señal DI/DO para drenaje gravitatorio."
        ),
        # Para 198: "Nivel de TK-06-001 de salmuera mayor a 70%."
        "search": ["mayor a 70", "salmuera mayor", "TK-06-001 de salmuera"],
        "label": "Bandas nivel TK-06-001 (GAP-03)",
    },
    {
        "id": 4,
        "text": (
            "Consulta: el documento declara que el postratamiento no requiere acción desde el nuevo "
            "PLC, pero no especifica el detalle de la coordinación. Para documentar el límite de "
            "responsabilidades, confirmar en Rev C: (1) si LS-00-002 (nivel alto TK-00-001) tiene "
            "algún rol como interlock en la lógica del nuevo módulo ADASA, o si es exclusivamente "
            "una señal del sistema existente; (2) si existen señales inter-PLC entre el nuevo PLC "
            "ADASA y el PLC de planta existente, o si la coordinación ocurre únicamente a través "
            "del estanque físico TK-00-001."
        ),
        # Para 261: "...instalará un switch de alto nivel LS-00-002 en el estanque TK-00-001..."
        "search": ["LS-00-002"],
        "label": "Integración postratamiento (GAP-04)",
    },
    {
        "id": 5,
        "text": (
            "Lazo CTRL_BH06_001 definido de forma incompleta. Faltan: tipo de control "
            "(PI/PID), rango de frecuencia del VFD (Hz mín/máx), modo de fallback ante "
            "falla de PIT-06-001, y perfil de rampa de arranque. Información insuficiente "
            "para programar el lazo en el PLC."
        ),
        # Para 236: "...variador de frecuencia que será comandado por un lazo de control..."
        "search": ["CTRL_BH06_001", "CTRL_BH06"],
        "label": "Lazo control CTRL_BH06_001 (GAP-05)",
    },
    {
        "id": 6,
        "text": (
            "Falta incluir en el IO List la señal DI de falla de OI-06-003 (falla OI → "
            "interlock PLC ADASA). Respecto al reencendido: se requiere definir el "
            "procedimiento. El comportamiento esperado es que no exista señal de reset "
            "dedicada desde el PLC hacia la OI — el operador normaliza la falla en campo "
            "y reinicia el módulo desde la HMI ADASA."
        ),
        # Para 194: "Señal DI de falla de módulo de OI BW Water apagada. (OI-06-003)"
        # Esta es la lista de señales inter-PLC donde falta la señal de alarma
        "search": ["falla de módulo de OI BW Water", "OI BW Water apagada"],
        "label": "Señales inter-PLC (GAP-06)",
    },
    {
        "id": 7,
        "text": (
            "VM-06-001 y VM-06-002 ausentes de la lógica de control. "
            "Son válvulas manuales con finales de carrera en las líneas de interconexión "
            "fuera del módulo. "
            "Permisivos de arranque requeridos: VM-06-001 CERRADA; VM-06-002 ABIERTA. "
            "Rev C debe incluir: "
            "(1) señales DI de posición (abierta y cerrada) para ambas válvulas en el IO List; "
            "(2) criterio de permisivo en la tabla de arranque; "
            "(3) alarma y bloqueo de arranque de BH-06-001 si alguna válvula reporta "
            "posición incorrecta."
        ),
        # Anclar en la sección de permisivos de arranque (misma zona que GAP-01)
        "search": ["Encendido de Bomba de alimentación", "permisivos", "Permisivos"],
        "label": "Válvulas interconexión VM-06-001/002 (GAP-07)",
    },
    # --- Comentarios nuevos Ronald Pellejero Salazar 18-Mar-2026 ---
    {
        "id": 8,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:22:00Z",
        "text": (
            "Describir posibilidades local - remoto y/o manual - automático de tres sistemas: "
            "PLC BW Water, PLC Planta y HMI PC. Es mejor poner una tabla con las alternativas."
        ),
        "search": ["LOCAL - O - REMOTO", "llave selectora"],
        "label": "Tabla local/remoto 3 sistemas (RS-01)",
    },
    {
        "id": 9,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:31:00Z",
        "text": "Crear documento con estas pantallas",
        "search": ["Pantallas"],
        "label": "Crear doc pantallas (RS-02)",
    },
    {
        "id": 10,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:36:00Z",
        "text": "Incluir pantalla de variables eléctricas",
        "search": ["Pantalla de eventos y alarmas", "eventos y alarmas"],
        "label": "Pantalla variables eléctricas (RS-03)",
    },
    {
        "id": 11,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:26:00Z",
        "text": (
            "Adasa usa usuarios generales. Esto debido a que no existe un usuario administrador "
            "que tenga la función de crear u eliminar usuarios."
        ),
        "search": ["alarmas pueden ser reconocidas", "Queda registrado el nomb"],
        "label": "Usuarios generales ADASA (RS-04)",
    },
    {
        "id": 12,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:33:00Z",
        "text": (
            "Al PLC planta debemos integrar un MVE (Medidor de Variables Eléctricas) general, "
            "que nos permita obtener estas variables eléctricas y calcular el consumo especifico "
            "del sistema completo. Las variables y el calculo del consumo especifico deben ser "
            "una pantalla en HMI de PC sala control y HMI PLC planta"
        ),
        "search": ["Descripción de las áreas de proceso", "reas de proceso"],
        "label": "MVE consumo específico (RS-05)",
    },
    {
        "id": 13,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:29:00Z",
        "text": "Incluir TAG de TK de agua producto",
        "search": ["BDS-03-005", "Bomba Dosificadora Fluoruro"],
        "label": "TAG TK agua producto (RS-06)",
    },
    {
        "id": 14,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:48:00Z",
        "text": "Verifiquemos que esta señal de falla apagada venga desde PLC BW water con lógica segura.",
        "search": ["falla de módulo de OI BW Water", "OI BW Water apagada"],
        "label": "Señal falla lógica segura (RS-07)",
    },
    {
        "id": 15,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:06:00Z",
        "text": "Indicar Tag y si será por indicador de nivel o por TX de nivel.",
        "search": ["TK-01-001 de agua producto", "menor al 80"],
        "label": "TAG instrumento TK-01-001 (RS-08)",
    },
    {
        "id": 16,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:50:00Z",
        "text": (
            "Puede ser mantenido si la DO es del tipo DO de relé. "
            "Se debe pedir así a PLC planta."
        ),
        "search": ["presión medida por PIT-06-001 es la seteada", "PIT-06-001"],
        "label": "DO tipo relé PLC Planta (RS-09)",
    },
    {
        "id": 17,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T17:51:00Z",
        "text": "En HMI PC en sala de control o en HMI de PLC planta",
        "search": ["Cuando el operador lo requiera", "dar orden de parar"],
        "label": "HMI sala control vs PLC (RS-10)",
    },
    {
        "id": 18,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:18:00Z",
        "text": "Indicar como tabla y describir el lazo PID como en el ejemplo:",
        "search": ["CTRL_BH06_001", "CTRL_BH06"],
        "label": "Tabla lazo PID (RS-11)",
    },
    {
        "id": 19,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:18:00Z",
        "text": "Se elimina equipo",
        "search": ["Bomba sumergible de drenajes y fosa", "fosa de drenajes"],
        "label": "BS-06-001 eliminada sección drenajes (RS-12)",
    },
    {
        "id": 20,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:25:00Z",
        "text": (
            "No se conectaran PLC existentes con PLC Planta. El nuevo indicador de nivel "
            "LS-00-002 es lo único requerido como interlock o permisivo de partida."
        ),
        "search": ["LS-00-002", "switch de alto nivel"],
        "label": "No inter-PLC - LS-00-002 único interlock (RS-13)",
    },
    {
        "id": 21,
        "author": "Ronald Pellejero Salazar",
        "date": "2026-03-18T18:29:00Z",
        "text": "Comentario para ADASA: verificar que estén estas estas tres señales pedidas a BW water",
        "search": ["Señal de fallo módulo BW Water", "fallo módulo BW"],
        "label": "Verificar 3 señales BW Water (RS-14)",
    },
]


# ── Funciones auxiliares ───────────────────────────────────────────────────────

def para_text(p_elem):
    """Extrae el texto concatenado de todos los w:t dentro de un w:p."""
    return "".join(t.text or "" for t in p_elem.iter(wt("t")))


def find_para(all_paras, search_terms, start=0):
    """
    Devuelve (índice, párrafo) del primer párrafo que contenga alguno de los
    términos de búsqueda (búsqueda insensible a mayúsculas), empezando en start.
    Retorna (None, None) si no se encuentra ninguno.
    """
    for i, p in enumerate(all_paras[start:], start=start):
        txt = para_text(p).lower()
        for term in search_terms:
            if term.lower() in txt:
                return i, p
    return None, None


def make_comment_element(cdata):
    """
    Construye el elemento XML <w:comment> completo con su contenido de texto.

    Estructura:
      <w:comment w:id="N" w:author="..." w:date="..." w:initials="...">
        <w:p>
          <w:pPr><w:pStyle w:val="CommentText"/></w:pPr>
          <w:r>
            <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>
            <w:annotationRef/>
          </w:r>
          <w:r>
            <w:t xml:space="preserve">texto del comentario</w:t>
          </w:r>
        </w:p>
      </w:comment>
    """
    author   = cdata.get("author", AUTHOR)
    initials = "RS" if "Ronald" in author else INITIALS
    date     = cdata.get("date", DATE)

    nsmap = {"w": W_NS}
    comment = etree.Element(wt("comment"), nsmap=nsmap)
    comment.set(wt("id"),       str(cdata["id"]))
    comment.set(wt("author"),   author)
    comment.set(wt("date"),     date)
    comment.set(wt("initials"), initials)

    p = etree.SubElement(comment, wt("p"))

    pPr    = etree.SubElement(p, wt("pPr"))
    pStyle = etree.SubElement(pPr, wt("pStyle"))
    pStyle.set(wt("val"), "CommentText")

    # run de annotationRef (requerido por Word para mostrar el número de comentario)
    r_ref    = etree.SubElement(p, wt("r"))
    rPr_ref  = etree.SubElement(r_ref, wt("rPr"))
    rSt_ref  = etree.SubElement(rPr_ref, wt("rStyle"))
    rSt_ref.set(wt("val"), "CommentReference")
    etree.SubElement(r_ref, wt("annotationRef"))

    # run con el texto del comentario
    r_txt = etree.SubElement(p, wt("r"))
    t_elem = etree.SubElement(r_txt, wt("t"))
    t_elem.set(f"{{{XML_NS}}}space", "preserve")
    t_elem.text = cdata["text"]

    return comment


def anchor_comment_to_para(target_para, comment_id):
    """
    Ancla el comentario dentro del párrafo (estructura inline — igual a Word nativo):

      <w:p>
        <w:pPr>...</w:pPr>
        <w:commentRangeStart w:id="N"/>   ← después de pPr, antes de los runs
        <w:r>texto comentado</w:r>
        <w:commentRangeEnd w:id="N"/>     ← después del último run
        <w:r>                             ← marcador inline con ID
          <w:rPr><w:rStyle val="CommentReference"/></w:rPr>
          <w:commentReference w:id="N"/>
        </w:r>
      </w:p>

    Nota: w:commentReference (en document.xml) ≠ w:annotationRef (en comments.xml).
    """
    children = list(target_para)

    # Insertar commentRangeStart justo después de w:pPr (o al inicio si no hay pPr)
    pPr = target_para.find(wt("pPr"))
    if pPr is not None:
        insert_pos = children.index(pPr) + 1
    else:
        insert_pos = 0

    cs = etree.Element(wt("commentRangeStart"))
    cs.set(wt("id"), str(comment_id))
    target_para.insert(insert_pos, cs)

    # Recalcular children tras la inserción
    children = list(target_para)

    # Insertar commentRangeEnd después del último w:r existente
    runs = [c for c in children if c.tag == wt("r")]
    if runs:
        last_run_idx = children.index(runs[-1])
        ce = etree.Element(wt("commentRangeEnd"))
        ce.set(wt("id"), str(comment_id))
        target_para.insert(last_run_idx + 1, ce)
    else:
        ce = etree.Element(wt("commentRangeEnd"))
        ce.set(wt("id"), str(comment_id))
        target_para.append(ce)

    # Run de marcador inline con w:commentReference (NO w:annotationRef)
    r   = etree.SubElement(target_para, wt("r"))
    rPr = etree.SubElement(r, wt("rPr"))
    rSt = etree.SubElement(rPr, wt("rStyle"))
    rSt.set(wt("val"), "CommentReference")
    cr  = etree.SubElement(r, wt("commentReference"))
    cr.set(wt("id"), str(comment_id))


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    if not os.path.exists(SRC):
        print(f"[ERROR] No se encontró el archivo fuente:\n  {SRC}")
        return

    print(f"[1/4] Copiando original → {os.path.basename(DST)}")
    shutil.copy(SRC, DST)

    # ── Leer contenido del ZIP ─────────────────────────────────────────────────
    with zipfile.ZipFile(DST, "r") as zf:
        doc_xml      = zf.read("word/document.xml")
        zip_names    = set(zf.namelist())
        comments_xml = zf.read("word/comments.xml") if "word/comments.xml" in zip_names else None

    # ── Parsear document.xml ───────────────────────────────────────────────────
    doc_root  = etree.fromstring(doc_xml)
    all_paras = doc_root.findall(f".//{wt('p')}")
    print(f"[2/4] Párrafos en documento: {len(all_paras)}")

    # Diagnóstico: mostrar primeros párrafos no vacíos para orientación
    print("       — Primeros 10 párrafos con contenido:")
    shown = 0
    for i, p in enumerate(all_paras):
        txt = para_text(p).strip()
        if txt:
            print(f"         [{i:3d}] {txt[:80]}")
            shown += 1
            if shown >= 10:
                break

    # ── Parsear comments.xml ───────────────────────────────────────────────────
    if comments_xml:
        ctree    = etree.fromstring(comments_xml)
        existing = [c.get(wt("id"), "?") for c in ctree]
        print(f"[3/4] comments.xml cargado — IDs existentes: {existing}")
    else:
        ctree = etree.Element(wt("comments"), nsmap={"w": W_NS})
        print("[3/4] No había comments.xml — creando nuevo.")

    # ── Insertar cada comentario ───────────────────────────────────────────────
    print("\n       Procesando comentarios:")
    ok_count = 0
    for cdata in COMMENTS:
        idx, para = find_para(all_paras, cdata["search"], start=0)

        if para is None:
            print(f"  [!] {cdata['label']}: NO encontrado. Términos buscados: {cdata['search']}")
            continue

        preview = para_text(para).strip()[:80].replace("\n", " ")
        print(f"  [✓] {cdata['label']}")
        print(f"       Párrafo {idx}: \"{preview}\"")

        ctree.append(make_comment_element(cdata))
        anchor_comment_to_para(para, cdata["id"])
        ok_count += 1

    # ── Serializar ─────────────────────────────────────────────────────────────
    doc_xml_new      = etree.tostring(doc_root, xml_declaration=True,
                                      encoding="UTF-8", standalone=True)
    comments_xml_new = etree.tostring(ctree, xml_declaration=True,
                                      encoding="UTF-8", standalone=True)

    # ── Reescribir ZIP (copia temporal → rename atómico) ──────────────────────
    tmp_path = DST + ".tmp"
    with zipfile.ZipFile(DST, "r") as zin:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                if item == "word/document.xml":
                    zout.writestr(item, doc_xml_new)
                elif item == "word/comments.xml":
                    zout.writestr(item, comments_xml_new)
                else:
                    zout.writestr(item, zin.read(item))
            # Agregar comments.xml si no existía antes
            if "word/comments.xml" not in zip_names:
                zout.writestr("word/comments.xml", comments_xml_new)

    os.replace(tmp_path, DST)

    # ── Resumen ────────────────────────────────────────────────────────────────
    print(f"\n[4/4] ✓ Guardado: {os.path.basename(DST)}")
    print(f"       Comentarios ADASA insertados: {ok_count}/21")
    print(f"       Comentarios previos (Ronald feb):  4")
    print(f"       Total esperado en Word:            {ok_count + 4}")
    print()
    print("   Verificación en Word:")
    print("   1. Abrir P22-IT-06-008-101-B_ADASA-Review.docx")
    print("   2. Vista > Mostrar comentarios  (o panel de revisión)")
    print("   3. Confirmar 25 comentarios totales (7 LR + 14 Ronald mar + 4 Ronald feb)")
    print("   4. RS-13 (LS-00-002) junto a GAP-04 — Ronald responde la pregunta de coordinación")
    print("   5. RS-07 (lógica segura) y GAP-06 anclan en el mismo párrafo falla OI")
    print("   6. RS-11 (tabla PID) y GAP-05 anclan en el mismo párrafo CTRL_BH06_001")


if __name__ == "__main__":
    main()
