# CLAUDE.md

Instrucciones operativas para Claude Code en el proyecto Modulo de Salmuera Taltal.

**Version:** 6.14 | **Fecha:** 25-May-2026

> **Estado del proyecto, historial, baseline schedule y trazabilidad de documentos: ver [README.md](README.md)**

---

## 1. Reglas Criticas

### 1.1 PDFs - NUNCA Leer Directamente
- **PROHIBIDO:** Read tool en `.pdf`
- **PERMITIDO:** archivos `.md` en carpetas `/md/`
- **ALTERNATIVA:** skill `large-pdf-reader` si no existe `.md`

### 1.2 Scripts - Verificar con Glob Antes de Crear

```
REVISIONES/TRANSMITTALES/**/crear_transmittal.py
CORREOS/**/crear_correo.py
REVISIONES/EVALUACIONES/**/crear_*.py
INGENIERIA DE DETALLE MECANICA/**/agregar_comentarios*.py
```

Si existe -> actualizar. Si no -> crear siguiendo §3.

### 1.3 Versiones Vigentes
- **Oferta BW Water:** `OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md` (Rev1 = VIGENTE)
- **Cronogramas y baseline:** ver README.md

### 1.4 TOC - NUNCA Manualmente en Scripts

```
PROHIBIDO: TOC manual (fldChar/instrText) en scripts crear_*.py
PROHIBIDO: importar set_updatefields_true (la skill lo llama internamente)
CORRECTO:  crear_documento_adasa(..., incluir_toc=True/False)
```

`Template_ADASA.docx` ya contiene `w:sdt` TOC embebido. Un segundo TOC manual produce dos indices.

---

## 2. Redaccion Analitica Humana

**Sistema:** skill `anti-ia` v6. Antes de emitir transmittales/correos/consultas: invocar `anti-ia` modo `revisar`. Las secciones siguientes son reglas especificas del proyecto.

### 2.1 Frases-Firma IA Prohibidas

| Prohibido | Reemplazo |
|-----------|-----------|
| "Aqui surge la tension" | "Hay un problema critico" |
| "no es X, sino Y" | "A pesar de X, recomendamos Y porque..." |
| "no basta con X. Debemos Y" | Eliminar estructura binaria |
| "Asi de simple." | Eliminar |
| "No hay vuelta atras." | "Las consecuencias son dificiles de revertir" |
| Template identico entre secciones | Variar estructura |

**Test pre-envio:** `Ctrl+F` "surge"+"tension", "no es"+"sino", "Asi de simple" -> reformular/eliminar. Variar longitud de oraciones.

### 2.2 Apertura de Observaciones Tecnicas
- MAL: `"Missing Pt-100 motor windings"`
- BIEN: `"Missing Pt-100 motor windings - unless alternative protection is documented"`

### 2.3 Variacion Tonal por Seccion

| Seccion | Tono |
|---------|------|
| Contexto | Informativo neutral |
| Analisis | Tecnico denso |
| Riesgos | Cauteloso, con matices |
| Recomendaciones | Decisivo con alternativas |

### 2.4 Referencias a Secciones de Documentos

| Tipo de documento | Contexto INTERNO (ADASA) | Contexto EXTERNO (a BW Water) |
|-------------------|--------------------------|-------------------------------|
| ET, PIE, BAE | §5.2.2 (§N aceptado) | **Nombre completo de la seccion** |
| Oferta BW Water | Nombre completo | Nombre completo |
| Documentos BW Water (Control Phil., datasheets, listas) | §N.N aceptado | **Nombre descriptivo** |

**Prohibido a BW Water:** "ET §5.4", "BAE §43.2.c", "Control Philosophy §3.3.2", "§3.1 OBS-1/3" (referencias internas del propio transmittal).
**Correcto:** "ET — Communication and Control System (MODBUS TCP/IP)", "Section 3 — Detailed Observations by Document".

### 2.5 Referencias Internas dentro del Mismo Documento

**Prohibido en archivos persistidos** (Word, PDF, `.md`, scripts, planes, anotaciones, correos): `§NombreSeccion`, `§N`, `§N.N`.
**Correcto:** `Seccion N — Nombre Completo` (ej. `Section 3 — Pending Observations`).
**Permitido en chat conversacional** (no persistido): `§N` libre.

**Test:** `grep -Pn "§[A-Za-z0-9]" documento.md script.py` -> 0 coincidencias.

---

## 3. Generacion de Documentos DOCX

**Metodo unico:** scripts Python que importan desde `~/.claude/skills/template-adasa/ejemplo_documento.py` (path absoluto — **NO** `.claude/skills/...` del proyecto, Synology no soporta symlinks). `md_to_adasa_docx.py` documentado en SKILL.md **no existe**.

### 3.1 Patron Base

```python
import sys, os
sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))
from ejemplo_documento import crear_documento_adasa, aplicar_arial_12, add_simple_table

crear_documento_adasa(titulo="...", codigo="P22-XX-AA-DDD-NNN-R",
                     output_filename="output.docx", incluir_toc=True)
```

| Tipo documento | incluir_toc |
|----------------|-------------|
| Transmittales, Consultas, Evaluaciones | `True` |
| Correos | `False` (explicito) |

**Autoria fija:** Preparado=Luis Rivera, Revisado=Luis Rivera, Aprobado=Victor Gutierrez.

**Skill maneja automaticamente (NO duplicar):** anchos columna dinamicos, tablas con bordes/centrado, limpieza template, salto pagina post-cajetin, TOC, estilos Arial (Normal 11pt, H1 14pt, H2 12pt), header con logos/codigo/fecha.

> **NUNCA numeros manuales en `add_heading()`.** `Template_ADASA.docx` numera H1/H2/H3 automaticamente (numId=1): `add_heading("RESUMEN EJECUTIVO", level=1)` -> Word emite `1. RESUMEN EJECUTIVO`; `add_heading("Instrument List", level=2)` -> `3.1 Instrument List`. Texto numerico manual = doble numeracion (`1. 1. ...`). **Recurre al reescribir scripts** (confirmado TM N8 12-Mar y OOCC TM N1 19-May). Las referencias del cuerpo se escriben "Seccion N — Nombre" y siguen correctas porque el auto-numero respeta la secuencia. El `.md` fuente SI lleva numeros markdown (no auto-numera); divergencia .md<->script aceptada.

### 3.2 Transmittales

Carpeta: `REVISIONES/TRANSMITTALES/P22-TM-09-000-XXX-0/` con `crear_transmittal.py`, `P22-TM-XX_TRANSMITTAL.md` (ingles, BW Water), `Compilado-*.md` (interno, NO ENVIAR — incluye Van Doorn), output `TRANSMITTAL NX *.docx`.

**Flujo:** Revisiones -> SUBMITTALS/ -> Compilado interno -> .md ingles -> `python crear_transmittal.py` -> validar `anti-ia revisar`.

**Estructura de secciones** (NO incluir una seccion REQUIRED ACTIONS global aparte — duplica §3. SI incluir el bloque ejecutivo `Action to issue at IFC Rev 0` por documento dentro de su subseccion 2.x — ver §6.2; no duplica §3 porque §3 = pendientes de TMs previos y el bloque = ruta a Rev 0 de ese documento):
1. EXECUTIVE SUMMARY (veredicto + bullets, max ~100 palabras)
2. DETAILED OBSERVATIONS BY DOCUMENT (cada subseccion 2.x cierra con su bloque `Action to issue at IFC Rev 0`)
3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS (si aplica)
4. ATTACHMENTS (solo PDFs BW Water comentados por ADASA)
5. RESPONSE SUMMARY

**Disciplina del EXECUTIVE SUMMARY (§1) — ejecutivo, directo, sin repetición:**
1. **Una línea de veredicto** primero: `**TRANSMITTAL VERDICT: N — ...**` + n.º docs (submittals X a Y) + tally + driver, **una sola vez**.
2. **`Disposition at a glance:`** = una viñeta ultra-corta por documento: `**<Doc> <Rev> — Code <N>.** <una cláusula>`. Es el *qué notable* por documento; **distinto** del §5 RESPONSE SUMMARY (registro formal de códigos) — no lo duplica.
3. **`Why Code <N> — <doc>:`** + bullets **solo** del/los documento(s) que fijan el veredicto, tightened (lo esencial, no la prosa de análisis — esa vive en §2.x).
4. Una línea para observaciones previas abiertas → "Section 3 details the inventory".
5. El detalle por documento (entregables, cierres, justificaciones) vive en §2.x y §3, **NO se repite en §1**. Prosa ≤ ~100 palabras; **cero repetición** del mismo mensaje entre la línea de tally y los párrafos.

**No incluir:** Date/Project/From/To en GENERAL INFORMATION (ya en header), submittals 25007-XXXX en RESPONSE SUMMARY, documentos internos ADASA, footer, cierre `*End of document*`.

### 3.2.1 Stream OOCC / L&A (espanol)

Flujo espejo del de BW Water pero **100% espanol**, para L&A Ingenieria y Proyectos (Pablo Castillo). Codigo `P22-TM-00-010-NNN-0`. Ubicacion **separada**: `INGENIERIA DE DETALLE OOCC/REVISIONES/` (README + Hitos propios; NO el arbol `REVISIONES/` raiz, que es exclusivo BW Water ingles). Estructura: `TRANSMITTALES/P22-TM-00-010-NNN-0/` con `crear_transmittal.py`, `P22-TM-00-010-NNN-0_TRANSMITTAL.md` (espanol, se envia), `_ANALISIS_TRABAJO.md` (interno), `COMENTARIOS/` (`agregar_comentarios_mc_*.py` + `*_CC_ADASA.pdf`). Codigos de respuesta 1/2/3/4 = mismos del TdR P22-TR-00-010-01-1.

**Idioma — reglas duras (CLAUDE.md §3.4 "NO mezclar idiomas"):**
- **ID de punto de revision = `NOTA-XX`** (no `NOTE-XX`). `OBS-XX`, `OBS-NPT`, `PEND-XX` se mantienen (ya neutros/espanol). El `NOTE` que se importa de doc-annotator (§3.8) es la **constante de color azul de la skill** — symbol de API, NO el texto del ID; los scripts OOCC ni la importan (usan `MAYOR`/`MENOR`).
- **Purgar anglicismos de jerga ejecutiva** que se filtran del patron ingles BW Water al reescribir en modo ejecutivo: `Tally`->`Recuento`, `Drivers`->`Determinantes`, `Trackeado/tracked`->`Seguimiento / en seguimiento hasta`, `at a glance`->`de un vistazo`, `baseline/deadline/review` -> equivalente espanol. Barrido pre-emision: `grep -niE "\b(Tally|Drivers?|Trackeado|NOTE)\b"` sobre `.md`/`.py`/scripts -> 0.
- El stream BW Water sigue 100% ingles; no cruzar terminologia entre streams. Detalle vivo: memoria `project_stream_oocc_lya.md` + `feedback_oocc_lya_espanol.md`.

### 3.3 Consultas Tecnicas

Carpeta: `REVISIONES/CONSULTAS_TECNICAS/` con `P22-CT-09-000-XXX-0_*.md`, `crear_consulta.py`, output `*_ADASA.docx`.

Uso: pregunta abierta sobre un punto técnico específico (clarificación, justificación, equivalencia de marca). Una CT cierra cuando BW Water responde y ADASA evalúa la respuesta (típicamente con una Rev .1 de la misma CT que registra la evaluación).

### 3.3.1 Notas Tecnicas

Carpeta: `REVISIONES/NOTAS_TECNICAS/` con `P22-NT-09-000-XXX-0_*.md`, `crear_nota_tecnica.py`, output `P22-NT-09-000-XXX-0_*_ADASA.docx`.

Patron de script: idéntico a `crear_consulta.py` — importa de `~/.claude/skills/template-adasa` (path absoluto), `crear_documento_adasa(..., incluir_toc=True)`, limpia placeholder, helpers `add_para` / `add_para_bold_lead` / `add_bullet`, `add_simple_table` para tablas de Reference Documents y Document History.

**Uso (distinción vs CT vs TM):**

| Instrumento | Cuándo usarlo |
|---|---|
| **TM** Transmittal | Revisión sistemática de entregables BW Water (submittals N1, N2, ..., NN). Veredictos Code 1/2/3/4 por documento. Ciclo de revisión repetitivo |
| **CT** Consulta Técnica | Pregunta abierta sobre UN punto técnico específico. Espera respuesta puntual de la contraparte. Ciclo: query → respuesta → evaluación Rev.1 |
| **NT** Nota Técnica | Respuesta estructurada a un cambio significativo planteado por la contraparte (mitigation plan, change request, dispute técnica). Conjunto coordinado de contra-preguntas o posiciones agrupadas por items. ADASA NO pide una respuesta puntual sino una respuesta estructurada en múltiples sub-items. Reserva formal de posición hasta recibir la respuesta. Ciclo: NT → respuesta multi-punto → posición ADASA (acceptance/conditional/rejection/Change Order requirement) |

**Estructura mínima de una NT:**
1. Context and Purpose (background + estado actual + reserva de posición)
2. Reference Documents (tabla con códigos/rev/fecha + jerarquía contractual)
3. Technical Clarifications / Position Items (agrupadas por sub-tema con prosa intro + contra-preguntas o posiciones numeradas N.A / N.B / N.C ...)
4. Response Deadline (fecha firme + formato esperado de la respuesta)
5. ADASA Reservations (reserva de posición + work-at-own-risk si aplica + cascada baseline + precedentes registrados)
6. Document History

**Emisión vía correo de remisión**: la NT se adjunta a un correo ejecutivo y directo (~100 palabras) que acusa recibo, remite la NT como adjunto, fija deadline, sin proponer reunión. El correo NO repite sustancia de la NT — solo carta de cobertura.

**Cadena de correo separada — regla dura (CLAUDE.md §3.4 también)**: si la NT (o CT) responde a una cadena de correo específica del proveedor (ej. cover email que transmitió un Mitigation Plan), su correo de remisión es **Reply-To a esa cadena**, NO conjunto con un TM o instrumento de otra cadena. El riesgo procesal de "cross-references a un documento no recibido" se neutraliza enviando ambos el mismo día con códigos ADASA explícitos en las cross-references — no requiere fusionar en un solo correo. **Aprendido TM N19 + NT-001 25-May-2026**: se planteó inicialmente envío conjunto, el usuario corrigió porque responden a cadenas distintas (TM cadena regular transmittals; NT Reply-To cover Mitigation Plan).

**Numeración de sub-items**: contigua dentro de cada sub-sección (N.A, N.B, N.C, ...). Si durante revisión interactiva se descartan algunas contra-preguntas propuestas, renumerar consecutivamente antes de emitir (no dejar saltos tipo 2.A → 2.C que sugieran edición incompleta).

### 3.4 Correos

Carpeta: `CORREOS/[Mes YYYY]/YYYY-MM-DD/` con `crear_correo.py`, `*_Descripcion.md` (incluir "Contexto Interno (No enviar)"), output `*.docx`.

- Carpetas tematicas (`CORREO ENVIADOS POR TEMAS CONTRACTUALES/`, `CORREOS COMPRA EQUIPOS/`) en root de CORREOS — **NO mover**
- Al agregar correo: actualizar README.md tablas §2 y §9
- Correos usan `Document()` directo — sin template ADASA
- Tras envio: `BORRADOR` -> `ENVIADO` en `.md`, dejar respaldo (PDF/.msg) en carpeta, actualizar README.md
- **Fecha de carpeta == fecha del header del correo**: el path `CORREOS/[Mes YYYY]/YYYY-MM-DD/` debe coincidir con la `Date:` declarada en el `.docx`/`.md`. Si hay discrepancia (ej. carpeta `2026-05-26/` con body que dice "May 25, 2026"), mover los archivos a la carpeta de fecha correcta antes del envío y eliminar la carpeta vacía. **Aprendido NT-001 25-May**.
- **Cadena de correo separada por instrumento contractual** (ver también §3.3.1): TM responde a la cadena regular de transmittals; NT/CT que responden a un thread específico del proveedor (Mitigation Plan, Change Request, etc.) van como **Reply-To** a ese thread, NO conjunto con un TM. El riesgo procesal de cross-references a un documento no recibido se neutraliza enviando ambos el mismo día con códigos ADASA explícitos en las cross-references.

**Formato segun tipo:**

| Tipo | Formato | Patron |
|------|---------|--------|
| Notificacion transmittal (1-2 docs) | Bullets cortos con bold inline en ID | `crear_correo_tm17.py` |
| Cross-check N items vs baseline (procurement, trackers) | **3 tablas Word** `Table Grid`: CRITICAL/WARNING/OK + bottleneck | `crear_correo_procurement.py` |
| Transaccional (acuse, reunion, propuesta puntual) | Parrafo simple, sin tablas | ad-hoc |

**Tablas (helper `add_table_with_header` en `crear_correo_procurement.py`):** margenes `0.8"`, cuerpo Arial 11pt, celdas Arial 10pt. Status line antes: `"X OK, Y warning, Z critical out of N line items"`. CRITICAL/WARNING: 5 cols. OK: 4 cols (sin Action). Tras tablas: parrafo bottleneck + bullets ops + cierre con proximo hito.

**Correos en español (Anwo/Exfibro/KSB/AA/Ronald):**
1. Aplicar `fijar_idioma_documento(doc, "es-CL")` como ultima operacion antes de `doc.save()` — sin esto Word subraya tildes/eñes en rojo. Helper en correos en español ya emitidos.
2. Revisar tildes, `ñ`, conectores ("en consecuencia" no "por consecuencia"), comillas tipograficas, simbolos (σ τ Δ ≤ ≥ → ° ± — −).
3. NO mezclar idiomas — hispanohablante 100% español; BW Water 100% ingles.

### 3.5 Evaluaciones

Carpeta `REVISIONES/EVALUACIONES/`: scripts `crear_evaluacion.py` (P22-IT-06-000-001-0), `crear_registro.py` (-002 DOCX), `generar_excel_registro.py` (-002 Excel), `crear_alineacion_notebooklm.py` (-003), `crear_evaluacion_logica.py` (-004). Todos usan template ADASA.

### 3.6 Anotacion DOCX Existentes (Comentarios Word)

Para DOCX no generados por la skill (ej. Van Doorn). **Tecnologia:** `zipfile` + `lxml` directo. **NO python-docx** (no tiene API para comentarios Word). Patron XML:
- `document.xml`: `<w:commentRangeStart>`, `<w:r>texto</w:r>`, `<w:commentRangeEnd>`, run con `<w:commentReference>`
- `comments.xml`: `<w:annotationRef/>` (NO `w:commentReference` — ese va en document.xml)

Buscar parrafos por texto especifico (no indices fijos).

**Clasificacion contenido (Van Doorn vs ADASA):**

| Tipo | Accion |
|------|--------|
| Omision en doc Van Doorn | INCLUIR como observacion directa |
| Requerimiento ADASA no especificado a Van Doorn | ELIMINAR o reformular como consulta |
| Posicion Van Doorn que falta detalle | REFORMULAR como pregunta abierta |

**Lenguaje:** evitar jerga sin definicion previa. Ej: usar "señales DI de posicion (abierta y cerrada)" en lugar de "DI de ZSC y ZSO".

### 3.7 Regla Van Doorn

**Van Doorn = Asesor INTERNO de ADASA.** Aparece en compilado interno, **NO** en transmittals ni correos a BW Water.

**Alcance:** ingenieria perimetral area 06 (proceso/mecanica/tuberias): P&IDs, listados de lineas/valvulas/equipos, logica de control (P22-IT-06-008-xxx).

**NO cubre:** electricidad y control (E&C). IO List area 06 es scope E&C — su ausencia en entregas Van Doorn no es hallazgo.

**TAGs Area 06 — Equipos ADASA:**

| TAG | Descripcion | Nota |
|-----|-------------|------|
| TK-06-001 | Estanque Salmuera (PRFV 10.000 L, ADASA) | TAG estable desde Ing. Basica |
| TK-06-004 | Fosa Drenajes (hormigon 2.000 L, ADASA) | TAG correcto segun `P22-LI-06-005-001`. **TK-06-002 NO es Fosa Drenajes** — TK-06-002 = Estanque CIP BW Water. Ver `memory/feedback_tk06002_vs_tk06004_fosa_drenajes.md` |
| BH-06-001 | Bomba Alimentacion Salmuera | TAG estable |
| BS-06-001 | Bomba Sumergible Drenajes | **Omitida en planos Van Doorn** = cambio de ingenieria aprobado. Drenaje por gravedad via SA-CPVC-DN200-PN10-001. |

**Anotacion documentos Van Doorn:** misma metodologia que §3.8, archivos en subcarpeta `COMENTARIOS/` de cada entrega. Para Excel: `openpyxl.Comment()`. No aplica veredicto Code 1/2/3/4.

### 3.8 Anotaciones PDF — Documentos BW Water

**Skill:** `doc-annotator` v1.2 (PyMuPDF). Patron de script: ver `agregar_comentarios_*.py` existentes en `REVISIONES/TRANSMITTALES/P22-TM-09-000-XXX-0/COMENTARIOS/`. Importar `MAYOR, NOTE, run_comentarios`. Estructura `COMENTARIOS`: `{id, fill, search, page_fallback, text, page_min(opt)}`.

**Regla por veredicto:**

| Veredicto | Anotaciones PDF |
|-----------|----------------|
| Code 1 — Approved | **NO ANOTAR** — sin observaciones, no incluir CC_ADASA |
| Code 2 — Approved as Noted | **ANOTAR** las NOTEs/OBSs relevantes al documento. No items de otros docs |
| Code 3 / 4 | Anotar todas las OBS y NOTEs del documento |

> **Code 1 sin anotaciones de ningun tipo** — items cross-document se trackean en Section 3 del transmittal. Esto se aplica tambien a un documento correcto as-is cuyas notas son entregables sobre OTROS documentos: es Code 1 (ver criterio §6.2), sin CC_ADASA; el script de anotacion y su PDF, si se generaron, quedan como traza interna (no se emiten ni se adjuntan).

> **Code 2 SIEMPRE lleva CC_ADASA con sus OBS/NOTE propios** (regla recurrente — TM N19 25-May). El error tipico es generar solo CC_ADASA para Code 3 y dejar los Code 2 sin anotar, con el texto bajo la tabla Section 4 ATTACHMENTS diciendo "the Code 2 documents require no modification and carry no annotated PDF" — eso CONTRADICE la regla. Section 4 ATTACHMENTS debe listar TODOS los CC_ADASA generados (Code 2 + Code 3/4); el texto debe decir "All documents with open observations or notes carry annotated PDFs (X Code 3 + Y Code 2). Only the Z Code 1 — Approved documents carry no annotated PDF". Solo Code 1 carece de CC_ADASA.

**Colores por severidad (constantes):** CRITICAL (rojo, incumplimiento contractual) | MAYOR (naranja) | MENOR (amarillo) | NOTE (azul).

**Texto sin etiqueta de criticidad** — el color del rectangulo ya transmite severidad. Usar `"OBS-01: Wilcoxon model..."` (NO `"OBS-01 (MAJOR): ..."`). La columna "Severity" del `.md` SI mantiene `(MAJOR)/(MINOR)/(CRITICAL)` — inventario interno.

**Checklist OBLIGATORIO antes de generar:**
1. Leer tabla OBS/NOTE del transmittal `.md`
2. Para cada PDF: listar obs/notas que le aplican
3. **NOTEs cross-cutting** (multiples PDFs) -> entrada en CADA script afectado **(fuente mas frecuente de omisiones)**
4. `len(COMENTARIOS)` == obs+notes aplicables a ese PDF
5. IDs deben coincidir con IDs del transmittal

**Estructura:** `COMENTARIOS/` con `agregar_comentarios_[doc].py`, PDF fuente normalizado (sin zero-width spaces), output `[PDF]_CC_ADASA.pdf`.

### 3.9 Traduccion FreeText In-Place

Para traducir anotaciones existentes manteniendo posicion/tamaño/color: PyMuPDF directo (NO doc-annotator — solo crea nuevas). Por cada `annot`: si `content in TRANSLATIONS` -> `annot.set_info(content=...); annot.update()`. Guardar a `.tmp` y `os.replace()` (atomic).

Verificar contenido exacto con `repr(annot.info.get("content",""))` antes de armar el dict — pueden existir variantes con espacios o guiones diferentes.

### 3.10 Emision de Revisiones Sucesivas (Rev N → Rev N+1)

La revision previa se preserva fisicamente y visiblemente en el cajetin. Trazabilidad contractual.

**Protocolo:**
1. **Archivar Rev N** en subcarpeta `ARCHIVO_REVISIONES/` con sufijo `_RevN`. Los `.docx`/`.pdf` Rev N quedan intactos en la carpeta principal.
2. **Editar en sitio** `.md` (header Revision/Codigo/fecha) y `.py` (OUTPUT, codigo).
3. **Cajetin apilado:** la skill v7.3 hardcodea `"0"` en `cajetin.rows[2]`. Post-procesar tras `crear_documento_adasa(...)`: setear `cajetin.rows[2]` con Rev N historica (fecha original) y `cajetin.rows[1]` con Rev N+1 nueva. Leer fecha Rev N del `.docx`, no del timestamp.
4. **Documentos sin script generador:** patron **patcher** — abrir `.docx` Rev N como base, modificar in-place y guardar como Rev N+1. Usar `copy.deepcopy(source_row._tr)` para insertar filas preservando formato; actualizar header run-por-run para preservar Arial.

**Redistribucion de roles entre documentos:** si Rev N+1 cambia que documento asume un rol, actualizar descripciones en tablas de antecedentes/referencia para evitar duplicar autoridad.

---

## 4. Skills Disponibles

| Skill | Version | Uso |
|-------|---------|-----|
| **template-adasa** | v7.3 | Documentos Word formato ADASA |
| **large-pdf-reader** | v5.0 | Extraccion de PDFs grandes |
| **canvas-design** | - | Diagramas y arte visual |
| **anti-ia** | v6 | Escritura analitica y evaluacion textos IA. Modos: `escribir`, `evaluar`, `revisar`, `perfilar` |
| **playground** | - | Exploradores HTML interactivos |
| **doc-annotator** | v1.2 | FreeText Acrobat + cuadros+flechas P&ID + comentarios Word DOCX |

### 4.1 Template ADASA v7.3 — API

**Archivo unico:** `~/.claude/skills/template-adasa/ejemplo_documento.py`. `config_defaults.py`/`table_utils.py`/`md_to_adasa_docx.py` documentados en SKILL.md **no existen**.

| Funcion | Descripcion |
|---------|-------------|
| `crear_documento_adasa()` | DOCX base con portada, cajetin, TOC, estilos |
| `aplicar_arial_12()` | Arial 12pt en parrafo |
| `add_simple_table()` | Tabla con anchos dinamicos, bordes, centrado, header |
| `calcular_anchos_columnas()` | Anchos proporcionales |
| `set_table_borders()` | Bordes + centrado |
| `set_repeat_table_header()` | Header repetible por pagina |
| `set_updatefields_true()` | **Uso interno** — NO importar |

---

## 5. Sistema de Codificacion

```
P22-TT-AA-DDD-NNN-R
```

| Campo | Valores |
|-------|---------|
| TT (tipo) | ET, DWG, LI, CD, TM, CT, **NT**, IT |
| AA (area) | 06 (ADASA), 09 (BW Water), 10 (Neutral) |
| DDD (disciplina) | 000-999 |
| NNN (correlativo) | 001-999 |
| R (revision) | 0, A, B, C... |

---

## 6. Revisiones Tecnicas

### 6.1 Formato Observaciones

```markdown
### OBS-XX: [Titulo]
| Campo | Valor |
|-------|-------|
| Documento | [Nombre] |
| Severidad | [Critico/Mayor/Menor] |

**Descripcion:** [Hallazgo]
**Requisito:** [ET/Oferta/Norma]
**Accion:** [Que debe hacer BW Water]
```

### 6.2 Veredictos y Ciclo de Revision

| Regla | Veredicto | Proxima revision BW | Texto en transmittal |
|-------|-----------|---------------------|----------------------|
| ≥1 rechazado | 4 - Rejected | Nueva Rev (B → C) | "in Rev X" |
| ≥1 requiere revision | 3 - To be revised | Nueva Rev (B → C) | "in Rev X" |
| ≥1 con notas que exigen modificar el documento mismo en Rev 0 | 2 - Approved as noted | IFC directo (Rev 0) | "prior to IFC (Rev 0)" |
| Documento correcto as-is (notas son entregables cross-document / análisis separados) | 1 - Approved | IFC directo | "no modification to this document; deliverables tracked in Section 3" |
| Todos aprobados, sin pendientes | 1 - Approved | IFC directo | Sin texto de accion |

> **Prohibido:** "in Rev C" en documentos Code 2. Code 2 va directo a IFC (Rev 0).

> **Criterio Code 1 vs Code 2 (regla ejecutiva).** El código refleja el estado del **documento revisado en sí**, no acciones que pertenecen a otros documentos:
> - **Code 2 — Approved as noted:** solo si el **propio documento** debe modificarse para IFC Rev 0 (corregir un valor/unidad, declarar explícitamente un dato en su contenido) — sin nueva revisión intermedia. Ej: un datasheet con una unidad errónea que se corrige al emitir Rev 0.
> - **Code 1 — Approved:** el documento revisado es correcto as-is y **no requiere modificación a sí mismo**. Si quedan acciones, son entregables sobre OTROS documentos o análisis separados → se trackean en la Sección 3 del transmittal (consistente con §3.8: Code 1 sin CC_ADASA, items cross-document en Section 3). Una nota cuyo entregable vive fuera del documento revisado **no** lo degrada a Code 2.
> - Determinante: "¿este documento, en sí, debe cambiar para llegar a Rev 0?" No → Code 1 (entregables a Section 3). Sí → Code 2.

### 6.3 Bloque ejecutivo `Action to issue at IFC Rev 0`

Cada subseccion de documento en la Seccion 2 del transmittal cierra con un bloque ejecutivo, escaneable, que indica que debe hacer BW Water para llevar ese documento a IFC Rev 0. No reemplaza la prosa de analisis (que explica el *por que*); la complementa con el *que*. Formato por veredicto:

| Veredicto | Bloque de cierre de la subseccion |
|-----------|-----------------------------------|
| **1 - Approved (sin pendientes)** | `**Action: none — accepted; issue directly at IFC Rev 0.**` |
| **1 - Approved (con entregables cross-document)** | `**Action: none on this document — accepted; issue directly at IFC Rev 0.**` + `Related deliverables tracked in Section 3:` con la lista (no modifica el documento revisado) |
| **2 - Approved as noted** | `**Action to issue at IFC Rev 0 — no new [doc] revision required:**` + lista numerada de los cambios a incorporar **en el propio documento** + 1 linea de condicion de aceptacion ADASA |
| **3 / 4** | La accion `in Rev X` ya explicita por OBS/NOTE cumple — sin bloque adicional |

**Regla clave (consistente con el criterio §6.2):** declarar SIEMPRE de forma explícita si el documento revisado cambia o no. Caso típico (P&ID, listas, cálculos correctos): el documento se acepta as-is → **Code 1**, y la acción vive en OTROS entregables o análisis separados, trackeados en la Sección 3 (decirlo literal: "the drawing itself requires no change" / "no modification to this document"). Reservar Code 2 para cuando el propio documento lleva un cambio menor a incorporar en Rev 0. No inflar a Code 2 una nota cuyo entregable es externo al documento revisado.

### 6.4 Revision Cruzada

| Lista | Cruzar con |
|-------|------------|
| Valve List | P&ID, ET 5.2.3 |
| Instrument List | P&ID, IO List, ET 5.5 |
| Equipment List | P&ID, capacidades |
| IO List | Instrument List, Valve List |

**Criterio Valvulas ET §5.2.3 — funcional, no dimensional:**

| Funcion / Tamano | Rating | Actuacion |
|------------------|--------|-----------|
| Proceso en linea principal (cualquier DN) | ANSI 900# | **ELECTRICA** |
| Venteos y drenes (DN15-DN25) | ANSI 900# | Manual OK |
| Cualquier tamano | ANSI 150# | Manual OK |

**Ejemplos canonicos:**

| Valvula | DN | Rating | Funcion | Actuacion |
|---------|----|--------|---------|-----------|
| VM-09-015 | DN100 | 900# | Aislamiento descarga HP Pump | **ELECTRICA** |
| VM-09-012 | DN15 | 900# | Venteo sistema HP | Manual OK |
| VE-09-008 | DN80 | 900# | Proceso SWRO Reject 1st | **ELECTRICA** |

> **Error a evitar:** No aplicar "DN50+ ANSI 900# = ELECTRICA" como regla dimensional. Un venteo DN50 ANSI 900# no requiere actuacion electrica.

---

## 7. Requisitos Tecnicos Clave (ET)

**Referencias:** `BASES TECNICAS/md/` y `OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md`. Toda observacion debe citar seccion ET o Oferta Rev1.

### 7.1 Temperatura y Vibracion - Bombas y Motores

| Seccion ET | Requisito | Aplica a |
|------------|-----------|----------|
| 5.1.1 L502 | RTDs 3 hilos en rodamientos | Bomba HP |
| 5.1.4 L581 | RTDs 3 hilos en rodamientos | Bomba CIP |
| **5.3 L1032** | **Pt-100 en devanados Y rodamientos** | **TODOS los motores** |
| 5.5.7 L1390 | Transmisores de vibracion | HP Pump, Turbochargers |

### 7.2 Instrumentacion

| Requisito | Detalle |
|-----------|---------|
| Protocolo señal | 4-20mA + HART (obligatorio) |
| Switches temperatura (TSH) | Solo alarma ON/OFF — NO monitoreo continuo |
| Transmisores proceso | Verificar rango/unidades/tag contra IO List y P&ID |
| Entradas analogicas | Cada instrumento en IL debe tener punto IO |
| **Conductividad** | **Contacting** (Rosemount 400, SS316L): <20 mS/cm. **Toroidal** (Rosemount 228) **OBLIGATORIO >20 mS/cm** (salmuera, rechazo etapa 1/2). ET §5.5.5 NO aplica a rechazo concentrado segunda etapa RO (~85–135 mS/cm) — SS316L incompatible con 45,000–55,000 ppm Cl⁻ |

### 7.3 Tuberias y Valvulas (ET §5.2)

Criterio funcional: ver tabla §6.4.

**Verificacion Valve List:**
- Confirmar actuacion contra ET 5.2.3 **por funcion** (proceso principal vs venteo/drenaje)
- Verificar valvulas electricas en IO List (DO correspondiente)
- Cruzar TAG entre Valve List y P&ID — detectar duplicados
- Rating brida consistente entre Valve List, P&ID y datasheet
- **TAGs duplicados = falla QA critica** — impide identificacion en PLC

### 7.4 Motores Electricos (ET §5.3)

Pt-100 en devanados Y rodamientos obligatorio en TODOS los motores. RTDs 3 hilos. Verificar entradas de temperatura en IO List.

### 7.5 Revision por Disciplina

| Disciplina | Documentos BW Water | Verificar contra |
|------------|---------------------|------------------|
| Mecanica / Proceso | Equipment List, Pump Datasheets, P&ID | ET §5.1, P&ID |
| Instrumentacion | Instrument List, IO List | ET §5.5, P&ID, tags |
| Valvulas | Valve List | ET §5.2.3, P&ID, IO List |
| Electrica / Motores | Motor List, MCC Schedule | ET §5.3, IO List |
| General P&ID | P&ID | ET general, Oferta Rev1 |

**Precedencia de fuentes:** ET -> Oferta Rev1 -> Normas referenciadas (ASME, API, ISA) -> P&ID aprobado.

---

## 8. Ubicacion de Archivos .md

| Contenido | Carpeta |
|-----------|---------|
| Bases Tecnicas (ET, BAE, PIE) | `BASES TECNICAS/md/` |
| Ingenieria Basica | `BASES TECNICAS/INGENIERIA BASICA/md/` |
| Oferta Tecnica (Rev.1 VIGENTE) | `OFERTA TECNICA/md/` |
| Contrato C-4300 | `PROGRAMA y CONTRATO/md/` |
| Entregas BW Water | `ENTREGAS_BWWATER/ENTREGA X/md/` |

---

## 9. Propuestas Comerciales de Cambio (Change Orders)

### 9.1 Criterios de Evaluacion

**Responsabilidad de origen:**

| Situacion | Responsabilidad |
|-----------|----------------|
| BW Water entrega plano tarde y no conforme tras constraint ADASA escrito | **BW Water** |
| ADASA solicita modificacion nueva no prevista en contrato | ADASA |
| Cambio por error de coordinacion interna BW Water | **BW Water** |

**Technical Offer vs constraints ADASA:** la Technical Offer define configuracion general (ej. "CIP fuera del container"); los parametros especificos (footprint, distancias, cotas) los establece ADASA via transmittals. Si BW Water ignora un constraint formalizado, la correccion es responsabilidad de BW Water.

**Analisis de scope** — para cada documento facturado:
- ¿Hay dependencia tecnica trazable entre el cambio y ese documento?
- ¿El documento fue aprobado previamente? (Si fue aprobado y el cambio es externo al sistema que cubre, requiere justificacion)
- ¿El sistema cubierto esta en la misma zona fisica que el cambio?

**Historial documentado en correo de respuesta:** fecha comprometida vs real, advertencias formales ADASA pre-incumplimiento, deadlines incumplidos por BW Water, turnaround ADASA.

### 9.2 Estructura de Respuesta

```
§1 — Contexto + acuse recibo (sin posicion aun)
§2 — Cronologia documentada
§3 — Scope: documentos que ADASA acepta vs impugnados con razon tecnica
§4 — Posicion ADASA (contractual, no acusatoria — documentar hechos)
§5 — Solicitud de propuesta revisada (a, b, c con deadline)
```

Tono firme y contractual, no acusatorio. Deadline propuesta revisada ≥5 dias habiles. Destinatario Eduardo Yamauchi + CC completa. Archivo en `CORREOS/[Mes YYYY]/YYYY-MM-DD/`.

---

## 10. Listado Consolidado EVI

**Script:** `generar_listado_consolidado.py` (raiz). **Output:** `LISTADO-CONSOLIDADO-EVI.xlsx`. Datos hardcoded.

**EQUIPOS_06 = SOLO 4 items ADASA** (TK-06-001/002, BH-06-001, BS-06-001 — ver README §1). **NO duplicar equipos BW Water** (van en EQUIPOS_09 con fabricante/modelo/specs).

---

## 11. Revision de Procurement vs Baseline

**Carpeta:** `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA <DD-MM-YY>/`. **Baseline:** ver README §"Baseline Schedule (05-Mar-2026)".

**Status legend (BW Water tracker):** C=Committed (PO emitida), E=Enabled (Eng Code 1/2, PO pending), D=Delayed (PR/PO window cerrada sin PO, variance >10d, o blocker), N=Not in Window.

**Clasificacion ADASA (overlay):**

| Categoria | Criterio |
|-----------|----------|
| **OK** | En ventana o adelantado; EAP Penang ≤ baseline mfg finish |
| **WARNING** | Slip 10-30 dias vs baseline; recuperable con monitoreo |
| **CRITICAL** | Sin PO + ventana cerrada >7d, slip >30d, lead time TBC en long-lead, o vendor unico con concentracion |

**Output del cross-check:**
1. Tabla resumen items con clasificacion OK/Warning/Critical
2. Top-3 alertas (vendor, dias sin PO o slip, accion + deadline)
3. Bottleneck por vendor unico si aplica (ver Fedco en README)
4. Variances list (slip ≥20d) que requieren recovery plan
5. Operational notes (typos, change log desactualizado, items sin pickup date)
6. Correo ejecutivo a Eduardo Yamauchi formato 3 tablas — ver §3.4

**Frecuencia:** cada 2 semanas o con nuevo tracker. Nueva Rev del cronograma baseline -> actualizar referencia en README y re-validar EAPs.

---

## 12. Mantenimiento

- **README.md** se actualiza cuando cambia estado operativo: documentos entregados/pendientes, correos enviados, deadlines, metricas, baseline.
- **CLAUDE.md** se actualiza cuando cambia metodologia estable: generacion de documentos, skills, criterios tecnicos, codificacion, anti-IA.

> **Regla de oro:** Si la informacion tiene fecha especifica o puede quedar obsoleta en semanas, va al README. Si es una instruccion que Claude debe seguir siempre, va al CLAUDE.md.

---

*Version 6.14 — 25 de mayo de 2026*

> **v6.14 (25-May, TM N19 + NT-001):** §3.8 refuerzo Code 2 SIEMPRE lleva CC_ADASA con sus OBS/NOTE propios — Section 4 ATTACHMENTS lista TODOS los CC_ADASA (Code 2 + Code 3/4), solo Code 1 sin CC_ADASA. §3.3.1 + §3.4 regla cadena de correo separada por instrumento contractual (TM thread regular; NT/CT Reply-To al thread del proveedor que originó la solicitud). §3.4 regla fecha-carpeta == fecha-header del correo. Detalle vivo del proyecto en README §9.
>
> **v6.13:** §3.1 regla dura "NUNCA numeros manuales en add_heading()" (recurre al reescribir scripts — TM N8 + OOCC TM N1). §3.2.1 nueva — stream OOCC/L&A espanol: ID `NOTA-XX` (no `NOTE`), purga de anglicismos de jerga ejecutiva (Tally/Drivers/Trackeado), `NOTE` de doc-annotator es constante de color (no ID).*

> **Historial de cambios:** ver `git log CLAUDE.md`. Historial operativo del proyecto en [README.md](README.md).
