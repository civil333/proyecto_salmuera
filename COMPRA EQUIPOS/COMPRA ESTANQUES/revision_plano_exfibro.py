"""
Revisión Plano de Fabricación EX-26005-F01 Rev A
Estanque de Salmuera TK-06-001 — Exfibro
Código: P22-IT-06-000-005-0
Fecha: 2026-03-06
"""
import sys, os
from docx import Document
from docx.shared import Pt

# --- Path a la skill ---
skill_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", ".claude", "skills", "template-adasa"
)
sys.path.insert(0, skill_path)

from ejemplo_documento import (
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
)

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "REVISION_EX-26005-F01-RevA_ADASA.docx")

# ============================================================
# 1. Crear documento base
# ============================================================
crear_documento_adasa(
    titulo="REVISIÓN PLANO DE FABRICACIÓN EX-26005-F01 REV A\nESTANQUE DE SALMUERA TK-06-001",
    codigo="P22-IT-06-000-005-0",
    output_filename=OUTPUT,
    incluir_toc=True,
    preparado_por="Luis Rivera",
    revisado_por="Luis Rivera",
    aprobado_por="Victor Gutierrez",
)

doc = Document(OUTPUT)

# ============================================================
# 2. INFORMACIÓN GENERAL
# ============================================================
doc.add_heading("INFORMACIÓN GENERAL", level=1)

info_rows = [
    ("Campo", "Detalle"),
    ("Plano revisado", "EX-26005-F01 Rev A"),
    ("Emisor", "Exfibro"),
    ("Equipo", "Estanque de Salmuera — Tag: TK-06-001"),
    ("Proyecto", "Planta Desaladora Taltal / Módulo Segunda Etapa"),
    ("Cliente", "Aguas Antofagasta (ADASA)"),
    ("Orden de Compra Exfibro", "N° 834750"),
    ("Fecha del plano", "Marzo 2026"),
    ("Fecha de revisión ADASA", "2026-03-06"),
    ("Revisión ADASA", "Rev 0"),
]
add_simple_table(doc, info_rows)

doc.add_heading("Documentos de Referencia", level=2)
ref_rows = [
    ("Código", "Documento", "Rev."),
    ("P22-ET-06-005-001", "Especificación Técnica — Estanque PRFV Taltal", "A"),
    ("P22-ET-06-005-002-0", "Hoja de Datos — Estanque de Salmuera TK-06-001", "0"),
    ("EX-26005-F01", "Plano de Fabricación — Exfibro (objeto de esta revisión)", "A"),
    ("ASME RTP-1 2017", "Standard for Reinforced Thermoset Plastic Corrosion-Resistant Equipment", "2017"),
    ("NCh.2369 Of.2003", "Diseño sísmico de estructuras e instalaciones industriales", "2003"),
    ("ASME B16.5", "Pipe Flanges and Flanged Fittings", "Vigente"),
]
add_simple_table(doc, ref_rows)

# ============================================================
# 3. RESUMEN EJECUTIVO
# ============================================================
doc.add_heading("RESUMEN EJECUTIVO", level=1)

p = doc.add_paragraph(
    "La revisión del plano de fabricación EX-26005-F01 Rev A identifica una observación "
    "de severidad Mayor y tres de severidad Menor que requieren respuesta de Exfibro "
    "antes de autorizar el inicio de fabricación. Las dimensiones generales del estanque "
    "(ø2,600 mm × H2,600 mm), el material FRP/PRFV, la barrera química de viniléster, "
    "la norma de diseño ASME RTP-1 2017 y la solución de venteo con codo 180° están "
    "correctamente declarados."
)
aplicar_arial_12(p)

doc.add_heading("Veredicto Global", level=2)
verd_rows = [
    ("Veredicto", "Descripción"),
    ("3 — REQUIERE REVISIÓN", "Una observación Mayor (pernos AISI 316L) y tres Menores que deben responderse previo a fabricación"),
]
add_simple_table(doc, verd_rows)

doc.add_heading("Hallazgos Críticos", level=2)
p = doc.add_paragraph(
    "OBS-01 — Pernos del manhole (MK5): material GALVANIZADO. "
    "La ET requiere acero inoxidable AISI 316L en todas las uniones bridadas.\n"
    "OBS-02 — Boquilla H: inconsistencia interna en el plano — LISTADO dice D.N.100 (4\"), "
    "tabla RTP-1 muestra d=150 mm (6\"). Se solicita aclaración documental."
)
aplicar_arial_12(p)

# ============================================================
# 4. TABLA DE VERIFICACIÓN
# ============================================================
doc.add_heading("TABLA DE VERIFICACIÓN", level=1)

p = doc.add_paragraph(
    "La tabla siguiente compara los 20 ítems de diseño contra los requisitos de la "
    "Especificación Técnica (ET) y la Hoja de Datos (HD)."
)
aplicar_arial_12(p)

verif_rows = [
    ("N°", "Ítem", "Requerimiento ET / HD", "Plano EX-26005-F01 Rev A", "Resultado"),
    ("1", "Tag equipo", "TK-06-001", "TK-06-001 (cajetín y vistas)", "OK"),
    ("2", "Orientación", "Vertical", "Vertical (Elevación Estanque Salmuera)", "OK"),
    ("3", "Diámetro interno", "2,600 mm", "MK1: D.N.2600 — ø2,600 mm", "OK"),
    ("4", "Altura cilindro", "2,600 mm (HD §5.2)", "MK1: 2,570 mm (manto neto, sin fondos)", "OK"),
    ("5", "Volumen útil declarado en plano", "10 m³ (HD §5.3)", "No declarado en cajetín ni notas", "OBS-02 (Menor)"),
    ("6", "Boquilla A — Manhole", "600 mm, ASME B16.5, 150# FF", "A: DN.600, tabla ANSI B16.5 150# confirmada", "OK"),
    ("7", "Boquilla B — Entrada salmuera", "4\", ASME B16.5, 150# FF", "B: DN.100 (4\"), ANSI B16.5-150#", "OK"),
    ("8", "Boquilla C — Transmisor nivel", "4\", ASME B16.5, 150# FF", "C: DN.100 (4\"), ANSI B16.5-150#", "OK"),
    ("9", "Boquilla D — Salida salmuera", "4\", ASME B16.5, 150# FF", "D: DN.100 (4\"), ANSI B16.5-150#", "OK"),
    ("10", "Boquilla E — Rebose", "4\", ASME B16.5, 150# FF", "E: DN.100 (4\"), ANSI B16.5-150#", "OK"),
    ("11", "Boquilla F — Drenaje", "2\", ASME B16.5, 150# FF", "F: DN.50 (2\"), ANSI B16.5-150#", "OK"),
    ("12", "Boquilla G — Switch de nivel", "4\", ASME B16.5, 150# FF", "G: DN.100 (4\"), ANSI B16.5-150#", "OK"),
    ("13", "Boquilla H — Venteo", "6\" (HD §6.8)", "CODO 180° D.N.100 FRP — venteo abierto a la atmósfera, sin brida", "OK"),
    ("14", "Material pernos — uniones bridadas", "AISI 316L (ET §6.3.2)", "MK5 (manhole): GALVANIZADO", "OBS-01 (Mayor)"),
    ("15", "Material sillas de anclaje", "AISI 316 (HD §9.8 pernos de anclaje)", "MK6: Acero A-36 + Pint. Epóxica", "OBS-03 (Menor)"),
    ("16", "Barrera química interior", "Viniléster ≥ 2.5 mm (HD §5.12)", "Materiales: VINILÉSTER; secuencia MMMV (ti≈3.5 mm en boquillas)", "OK (confirmar espesor manto principal)"),
    ("17", "Norma de diseño", "ASME RTP-1 (HD §7.1)", "Tabla dimensional: 'SEGÚN RTP-1 2017, Fig. 4-4 y 4-5'", "OK"),
    ("18", "Diseño sísmico", "NCh.2369 Of.2003 Zona 3 (ET §6.3)", "Tope sísmico presente; sin referencia explícita a NCh.2369 en plano", "OBS-04 (Menor)"),
    ("19", "Temperatura de diseño", "40°C (HD §4.8)", "No declarada en cajetín", "OBS-02 (Menor)"),
    ("20", "Presión de diseño", "Atmosférica / 0 bar man. (HD §4.9)", "No declarada en cajetín", "OBS-02 (Menor)"),
]
add_simple_table(doc, verif_rows)

# ============================================================
# 5. OBSERVACIONES
# ============================================================
doc.add_heading("OBSERVACIONES", level=1)

# OBS-01
doc.add_heading("OBS-01: Pernos del Manhole (MK5) — Material GALVANIZADO en lugar de AISI 316L", level=2)
obs03 = [
    ("Campo", "Detalle"),
    ("Ítem", "MK5 — Perno Completo Para (A), ø5/8\" × 4\""),
    ("Severidad", "Mayor"),
    ("Documentos involucrados", "EX-26005-F01 Rev A, ET P22-ET-06-005-001"),
]
add_simple_table(doc, obs03)
p = doc.add_paragraph(
    "Descripción: El Listado de Elementos consigna para MK5 (20 pernos del manhole A) "
    "el material GALVANIZADO. La ET establece que todas las uniones bridadas deben "
    "llevar pernos de acero 316L que sobrepasen 1 cm por encima de cada tuerca. El acero "
    "galvanizado no es equivalente a AISI 316L en servicio con salmuera (fluido corrosivo) "
    "y en ambiente marino, y compromete la vida útil de 25 años requerida."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Requisito: ET P22-ET-06-005-001 — Condiciones para tuberías: 'pernos metálicos en "
    "acero 316L'. Hoja de Datos §9.8/§9.9: Material pernos y tuercas de anclaje: AISI 316."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Acción requerida a Exfibro: Reemplazar la especificación de material de MK5 por "
    "AISI 316L (o AISI 316 como mínimo) en el plano Rev B. Extender la verificación a todos "
    "los pernos de las boquillas B-G."
)
aplicar_arial_12(p)

# OBS-02
doc.add_heading(
    "OBS-02: Placa de identificación — Condiciones de diseño ausentes en el plano "
    "y en el estanque construido",
    level=2
)
obs02 = [
    ("Campo", "Detalle"),
    ("Ítem", "Cajetín del plano y Placa de Identificación física (MK9)"),
    ("Severidad", "Menor"),
    ("Documentos involucrados", "EX-26005-F01 Rev A, ET P22-ET-06-005-001 §8.3"),
]
add_simple_table(doc, obs02)
p = doc.add_paragraph(
    "Descripción: El cajetín del plano no declara las condiciones de diseño del estanque: "
    "volumen útil (HD = 10 m³), temperatura de diseño (HD = 40°C) ni presión de diseño "
    "(HD = atmosférica). Esta información debe aparecer en el plano de fabricación para "
    "trazabilidad y control de calidad."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Adicionalmente, la ET §8.3 exige que cada estanque lleve una placa de características "
    "física, fijada permanentemente al cuerpo del equipo, que incluya como mínimo: tag del "
    "equipo (TK-06-001), nombre del fabricante, número de serie, fecha de fabricación, "
    "presión de diseño, volumen útil y código de diseño (ASME RTP-1). El plano Rev A "
    "incluye el ítem MK9 (Placa de Identificación, 200 mm × 3.0 mm, FRP) en el Listado "
    "de Elementos, pero no indica el contenido que debe llevar grabado ni confirma que "
    "todos los campos exigidos por la ET §8.3 estarán presentes en la placa física."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Requisito: ET P22-ET-06-005-001 §8.3 — Placa de características: tag, fabricante, "
    "número de serie, fecha de fabricación, presión de diseño, volumen útil, código de "
    "diseño. Material placa: AISI-316L."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Acción requerida a Exfibro: (a) Agregar tabla de condiciones de diseño en el plano "
    "Rev B: volumen útil = 10 m³, T diseño = 40°C, P diseño = atmosférica. "
    "(b) Incluir en el plano el detalle del contenido de la placa de identificación MK9 "
    "con todos los campos exigidos por la ET §8.3. "
    "(c) Confirmar que la placa física quedará instalada de forma permanente en el "
    "estanque construido, legible desde el suelo, en material AISI-316L según la ET."
)
aplicar_arial_12(p)

# OBS-03
doc.add_heading("OBS-03: Sillas de anclaje (MK6) en Acero A-36 — ambiente marino salino", level=2)
obs03b = [
    ("Campo", "Detalle"),
    ("Ítem", "MK6 — Sillas de Anclaje (8 unidades)"),
    ("Severidad", "Menor"),
    ("Documentos involucrados", "EX-26005-F01 Rev A, ET §6.1, HD §9.8"),
]
add_simple_table(doc, obs03b)
p = doc.add_paragraph(
    "Descripción: Las sillas de anclaje (MK6) están especificadas en Acero A-36 con "
    "protección de pintura epóxica. Operan en ambiente marino salino (ET §6.1) con una "
    "vida útil requerida de 25 años. La protección únicamente por pintura epóxica puede "
    "resultar insuficiente para ese horizonte temporal a la intemperie."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Acción requerida a Exfibro: Confirmar el sistema de protección anticorrosiva de las "
    "sillas de anclaje para 25 años en ambiente marino. Evaluar si aplica fabricación en "
    "AISI 316L o recubrimiento certificado para ambiente de alta salinidad."
)
aplicar_arial_12(p)

# OBS-04
doc.add_heading("OBS-04: Norma NCh.2369 no referenciada explícitamente en el plano", level=2)
obs04b = [
    ("Campo", "Detalle"),
    ("Ítem", "Notas técnicas y cajetín"),
    ("Severidad", "Menor"),
    ("Documentos involucrados", "EX-26005-F01 Rev A, ET §6.3"),
]
add_simple_table(doc, obs04b)
p = doc.add_paragraph(
    "Descripción: La ET §6.3 exige diseño sísmico conforme a NCh.2369 Of.2003 Zona 3. "
    "El plano incluye el detalle de 'Tope Sísmico' y las 'Sillas de Anclaje', confirmando "
    "que se consideró el sismo. Sin embargo, la norma NCh.2369 no está mencionada en las "
    "notas técnicas ni en el cajetín."
)
aplicar_arial_12(p)
p = doc.add_paragraph(
    "Acción requerida a Exfibro: Incluir la referencia 'NCh.2369 Of.2003 Zona 3' en las "
    "notas del plano Rev B para trazabilidad de la base normativa del diseño sísmico."
)
aplicar_arial_12(p)

# ============================================================
# 6. ACCIONES REQUERIDAS A EXFIBRO
# ============================================================
doc.add_heading("ACCIONES REQUERIDAS A EXFIBRO", level=1)

p = doc.add_paragraph(
    "Las siguientes acciones deben resolverse en la próxima revisión del plano (Rev B) "
    "antes de autorizar el inicio de fabricación:"
)
aplicar_arial_12(p)

acciones_rows = [
    ("N°", "Acción", "OBS", "Prioridad"),
    ("1", "Cambiar material de MK5 (pernos manhole A) de GALVANIZADO a AISI 316L. Verificar pernos de boquillas B-G.", "OBS-01", "Alta"),
    ("2a", "Agregar tabla de condiciones de diseño en el plano Rev B: Volumen útil = 10 m³, T diseño = 40°C, P diseño = Atmosférica.", "OBS-02", "Media"),
    ("2b", "Incluir en el plano el detalle del contenido de la placa de identificación MK9 con los campos exigidos por la ET §8.3.", "OBS-02", "Media"),
    ("2c", "Confirmar que la placa física MK9 quedará instalada de forma permanente en el estanque construido, en material AISI-316L, legible desde el suelo.", "OBS-02", "Media"),
    ("3", "Confirmar protección anticorrosiva de sillas de anclaje MK6 para 25 años en ambiente marino.", "OBS-03", "Media"),
    ("4", "Agregar referencia 'NCh.2369 Of.2003 Zona 3' en notas del plano.", "OBS-04", "Baja"),
]
add_simple_table(doc, acciones_rows)

# ============================================================
# 7. ANEXO: TABLA DE BOQUILLAS
# ============================================================
doc.add_heading("ANEXO: TABLA DE BOQUILLAS — COMPARATIVA PLANO vs. HD", level=1)

boquillas_rows = [
    ("Boquilla", "Servicio", "Diámetro HD", "Diámetro Plano", "Norma Plano", "Clase Plano", "Material Plano", "Resultado"),
    ("A", "Entrada Hombre (Manhole)", "600 mm", "DN.600 = 600 mm", "ASME B16.5", "150#", "FRP / RTP-1", "OK"),
    ("B", "Entrada Salmuera", "4\" (100 mm)", "DN.100 = 4\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("C", "Transmisor de Nivel", "4\" (100 mm)", "DN.100 = 4\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("D", "Salida Salmuera", "4\" (100 mm)", "DN.100 = 4\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("E", "Rebose", "4\" (100 mm)", "DN.100 = 4\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("F", "Drenaje", "2\" (50 mm)", "DN.50 = 2\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("G", "Switch de Nivel", "4\" (100 mm)", "DN.100 = 4\"", "ANSI B16.5", "150#", "FRP / ANSI B16.5-150#", "OK"),
    ("H", "Venteo", "6\" (HD §6.8)", "CODO 180° D.N.100 FRP — venteo abierto a la atmósfera", "No aplica", "No aplica", "FRP", "OK"),
]
add_simple_table(doc, boquillas_rows)

doc.add_heading("Notas a la Tabla de Boquillas", level=2)
p = doc.add_paragraph(
    "1. Las boquillas A a G son flanges rasantes (flat face, FF) según norma ANSI B16.5 "
    "clase 150#, confirmadas en la Tabla Dimensional del plano para estándar FRP.\n"
    "2. La boquilla H es un CODO 180° FRP (venteo abierto a la atmósfera, sin brida). "
    "Esta solución es aceptada para servicio de venteo. La Tabla Dimensional RTP-1 "
    "del plano indica d=150 mm para la penetración en el manto, lo que es coherente "
    "con la especificación 6\" de la HD.\n"
    "3. Los tipos de cara (FF) no están declarados explícitamente para B-H en el plano. "
    "Para FRP es convencional el uso de FF; sin embargo se recomienda indicarlo "
    "explícitamente en el plano Rev B para eliminar ambigüedad."
)
aplicar_arial_12(p)

# ============================================================
# 8. TABLA RESUMEN DE COMENTARIOS
# ============================================================
doc.add_heading("TABLA RESUMEN DE COMENTARIOS", level=1)

resumen_rows = [
    ("OBS", "Severidad", "Ítem", "Hallazgo", "Acción requerida a Exfibro"),
    (
        "OBS-01",
        "Mayor",
        "MK5 — Pernos manhole",
        "Material especificado: GALVANIZADO. La ET exige AISI 316L en todas las uniones bridadas.",
        "Corregir a AISI 316L en plano Rev B. Extender verificación a pernos de boquillas B-G.",
    ),
    (
        "OBS-02",
        "Menor",
        "MK9 — Placa de identificación y cajetín",
        "El cajetín no declara condiciones de diseño (Vol. útil, T, P). El plano no detalla el contenido de la placa física MK9 ni confirma que se instalará en el estanque.",
        "(a) Agregar en cajetín: Vol. útil = 10 m³, T diseño = 40°C, P diseño = Atm. "
        "(b) Indicar contenido de placa MK9 según ET §8.3. "
        "(c) Confirmar instalación permanente de la placa en el estanque, material AISI-316L.",
    ),
    (
        "OBS-03",
        "Menor",
        "MK6 — Sillas de anclaje",
        "Material: Acero A-36 + pintura epóxica. Ambiente marino salino, vida útil requerida 25 años.",
        "Confirmar sistema de protección anticorrosiva para 25 años en ambiente marino.",
    ),
    (
        "OBS-04",
        "Menor",
        "Notas del plano",
        "Norma NCh.2369 Of.2003 Zona 3 no referenciada en el plano, pese a que el tope sísmico está presente.",
        "Incluir referencia a 'NCh.2369 Of.2003 Zona 3' en notas del plano Rev B.",
    ),
]
add_simple_table(doc, resumen_rows)

doc.save(OUTPUT)
print(f"Documento generado: {OUTPUT}")
