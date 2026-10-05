# CLAUDE.md

Instrucciones operativas para Claude Code en el proyecto Modulo de Salmuera Taltal.

**Version:** 6.34 | **Fecha:** 05-Oct-2026

> **Estado del proyecto, historial, baseline schedule y trazabilidad de documentos: ver [README.md](README.md)**

---

## 1. Reglas Criticas

### 1.1 PDFs - NUNCA Leer Directamente
- **PROHIBIDO:** Read tool en `.pdf`
- **PERMITIDO:** archivos `.md` en carpetas `/md/`
- **ALTERNATIVA:** skill `large-pdf-reader` si no existe `.md`. Ruta real del script: `C:/Users/luisr/.claude/skills/large-pdf-reader/pdf_reader.py` — la del `$HOME`, **NO** `.claude/skills/...` del proyecto, que no existe porque Synology no soporta symlinks. Crear la carpeta `md/` destino **en la misma llamada** o falla con `FileNotFoundError`.
- **Triar antes de extraer.** Medir por documento paginas, caracteres, paginas vacias, rotacion y vectores; la metrica decide el modo. **Texto 0 = escaneado -> `--ocr`** (Tesseract vive en `C:/Program Files/Tesseract-OCR/` pero **fuera del PATH**: anteponerlo en el proceso). Paginas vacias sueltas -> OCR solo sobre esas. A2+ apaisada con muchos vectores -> `--mode drawing` **mas render PNG** para leerlo uno mismo. Cierre de cola: ningun `*_extracted.md` bajo 500 bytes. Ver `feedback_pdf_escaneado_triaje_texto_cero`.
- **Deduplicar por payload, nunca por contenedor.** Outlook recomprime los adjuntos al reenviar, de modo que dos `.zip` con contenido identico dan md5 distinto. Hashear **cada archivo interno**. Vale en los dos sentidos: antes de imputar al proveedor que envio la revision equivocada, hashear su adjunto contra la copia aprobada — un adjunto byte-identico prueba lo contrario y convierte el hallazgo en un cierre. El duplicado se **mueve** a `_duplicado_payload_identico/` con un `_LEEME.md` que registre ambos md5; no se borra. Ver `feedback_zip_duplicado_payload_no_contenedor`.

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
| ET, PIE, BAE | §5.2.2 (§N aceptado) | **Codigo + "Section N.N - Nombre completo"** (no solo el nombre) |
| Oferta BW Water | Nombre completo | Nombre completo |
| Documentos BW Water (Control Phil., datasheets, listas) | §N.N aceptado | **Nombre descriptivo** |

**Prohibido a BW Water:** el simbolo `§` ("ET §5.4", "BAE §43.2.c", "§3.1 OBS-1/3") y las referencias internas del propio transmittal.
**Correcto (preferido para ET/PIE/BAE):** codigo del documento + numero de seccion **deletreado** + nombre — ej. *"the Technical Specification (P22-ET-09-000-001-0), Section 5.4.1 - Constructive Characteristics"*. El codigo va una vez (primera cita) y "Section N.N" en cada referencia. Otros: "ET — Communication and Control System (MODBUS TCP/IP)", "Section 3 — Detailed Observations by Document". Regla dura: nunca el simbolo `§`; "Section N.N" deletreado sí (ver §2.5). Ver memoria `feedback_cite_et_codigo_seccion`.

### 2.5 Referencias Internas dentro del Mismo Documento

**Prohibido en archivos persistidos** (Word, PDF, `.md`, scripts, planes, anotaciones, correos): `§NombreSeccion`, `§N`, `§N.N`.
**Correcto:** `Seccion N — Nombre Completo` (ej. `Section 3 — Pending Observations`).
**Permitido en chat conversacional** (no persistido): `§N` libre.

**Test:** `grep -Pn "§[A-Za-z0-9]" documento.md script.py` -> 0 coincidencias.

---

## 3. Generacion de Documentos DOCX

**Dos metodos validos (template-adasa):**
1. **Script Python que importa `ejemplo_documento.py`** (path absoluto `~/.claude/skills/template-adasa/ejemplo_documento.py` — **NO** `.claude/skills/...` del proyecto, Synology no soporta symlinks). Contenido hardcoded en Python. Usado por transmittales, consultas, NT, correos, etc.
2. **Conversor Markdown->Word `md_to_adasa_docx.py`** (SI existe en `~/.claude/skills/template-adasa/`): `python ~/.claude/skills/template-adasa/md_to_adasa_docx.py <doc.md> [out.docx]`. El `.md` (con frontmatter YAML + figuras via `<!-- FIGURA:slug:Caption -->` resueltas contra carpeta `diagramas_png/figura_<slug>.png`) es la **fuente unica**; el Word se regenera del `.md`. Usado por la **BL Montaje Taltal** (`BASES DE LICITACION MONTAJE MECANICO-OOCC/BORRADOR_REV0/BL_MONTAJE_TALTAL_REV0.md`). **Caveats del conversor:** (1) elimina em-dash (`—`) del texto — usar guion/parentesis en el `.md`; (2) el Resumen Ejecutivo debe ser `# Resumen Ejecutivo` (H1) para numerar "1." (si es `##` queda "1.1"); (3) el frontmatter `cliente` debe ser **corto** (sigla, p.ej. `cliente: ADASA`) — si es largo, la celda Cliente del cajetin envuelve a varias lineas y el cajetin no cabe en la portada y se parte a la Hoja 2. El conversor (v7.2+) ya aplica `cantSplit` a las filas del cajetin para que no se parta; **no** borrar parrafos de portada (eso descentra el titulo); (4) las referencias de seccion del cuerpo van por **nombre** (no numero), porque el conversor auto-numera y un desfase rompe las referencias numericas; (5) **(v7.7)** el conversor ajusta solo el ancho de las columnas con codigos largos (`P22-DWG-...` no se parten) y **encuadra las figuras** en `FIGURA_MAX_W x FIGURA_MAX_H` (5.2" x 5.8", tunables) para que no queden paginas a medias; al guardar emite `[CHEQUEO LAYOUT] OK`/advertencias. El render visual con `revisor-docx` queda de respaldo.

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

> **NUNCA numeros manuales en `add_heading()`.** `Template_ADASA.docx` numera H1/H2/H3 automaticamente (numId=1): `add_heading("RESUMEN EJECUTIVO", level=1)` -> Word emite `1. RESUMEN EJECUTIVO`; `add_heading("Instrument List", level=2)` -> `3.1 Instrument List`. Texto numerico manual = doble numeracion (`1. 1. ...`). **Recurre al reescribir scripts.** Las referencias del cuerpo se escriben "Seccion N — Nombre" y siguen correctas porque el auto-numero respeta la secuencia. El `.md` fuente SI lleva numeros markdown (no auto-numera); divergencia .md<->script aceptada.

### 3.2 Transmittales

Carpeta: `REVISIONES/TRANSMITTALES/P22-TM-09-000-XXX-0/` con `crear_transmittal.py`, `P22-TM-XX_TRANSMITTAL.md` (ingles, BW Water), `Compilado-*.md` (interno, NO ENVIAR — incluye Van Doorn), output `TRANSMITTAL NX *.docx`.

**Flujo:** Revisiones -> SUBMITTALS/ -> Compilado interno -> .md ingles -> `python crear_transmittal.py` -> validar `anti-ia revisar`.

**Estructura de secciones** (NO incluir una seccion REQUIRED ACTIONS global aparte — duplica §3. SI incluir el bloque ejecutivo `Action to issue at IFC Rev 0` por documento dentro de su subseccion 2.x — ver §6.2; no duplica §3 porque §3 = pendientes de TMs previos y el bloque = ruta a Rev 0 de ese documento):
1. EXECUTIVE SUMMARY (veredicto + bullets, max ~100 palabras)
2. OBSERVATIONS BY DOCUMENT (cada subseccion 2.x cierra con su bloque `Action to issue at IFC Rev 0`)
3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS (si aplica)
4. ATTACHMENTS (solo PDFs BW Water comentados por ADASA)
5. RESPONSE SUMMARY

**Disciplina de la SECCIÓN 2 (OBSERVATIONS BY DOCUMENT) — resumen, NO reproduccion itemizada:** cada subseccion 2.x es **solo** `Response Code` + `Status` corto (2-4 frases: que es el documento / si esta correcto / el headline; para Code 3, la frase del driver) + el bloque `Action` (§6.3). **NO** incluir la tabla `| ID | Severity | Topic |` con las descripciones de cada observacion: **ese detalle itemizado vive en el CC_ADASA** de cada documento (que es 1:1 con los IDs). El Status cierra apuntando al PDF ("Itemised in <archivo>_CC_ADASA.pdf") y el bloque Action cita el **rango de IDs** ("(OBS-01 to OBS-03 and NOTE-01 on the annotated PDF)") en vez de repetir el texto. Los NOTE clave (cierre de un critico, "el doc esta correcto — dependencia en Seccion 3") se mencionan como una clausula del Status, no como filas sueltas. Reproducir las tablas OBS = duplicar el CC_ADASA e inflar el transmittal (su eliminacion recorta varias paginas). Ver `feedback_transmittal_seccion2_condensada`.

**Disciplina del EXECUTIVE SUMMARY (§1) — ejecutivo, directo, SIN visión de proyecto:**
1. **Una línea de veredicto** primero: `**TRANSMITTAL VERDICT: N — ...**` + n.º docs (submittals X a Y) + tally, **una sola vez**; sin editorial en esa línea.
2. **`Disposition at a glance:`** = una viñeta ultra-corta por documento: `**<Doc> <Rev> — Code <N>.** <una cláusula = la acción que falta>`. La cláusula dice **qué debe hacer BW Water** (p.ej. "re-issue as Rev D", "state the binding pressures at Rev 0"), **NO narra lo resuelto** ("the 45.5 bar error is gone", "gate resolved", "close gates open for months"). Distinto del §5.
3. **`Why Code <N> — <doc>:`** + bullets **solo** del/los documento(s) que fijan el veredicto, tightened (lo esencial, no la prosa de análisis — esa vive en §2.x).
4. Una línea → "Section 3 lists the pending observations from previous transmittals".
5. **PROHIBIDO el párrafo narrativo de avance/cierres** ("two long-standing items close", "se agradece que levantaron X", "gates resolved", "panel fabrication no longer gated"): el usuario NO quiere enviar una visión de cómo va el proyecto. El código y los cierres por documento viven en §2.x (Status) y en §5; lo pendiente, en §3. Prosa ≤ ~100 palabras; cero repetición. El cierre del §5 tampoco narra cierres (solo veredicto + driver).

**Disciplina de la SECCIÓN 3 (PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS):** siempre una **tabla de los 3 pendientes MÁS GRAVES** (Origin TM / Document / Observation / Status). El resto, si hay, **resumido en una línea** (`**Also open:** ...`); los vencidos y los cross-document, **una línea cada uno**. **NO** el párrafo "Addressed in this transmittal" (narrar lo cerrado = visión de proyecto; los cierres van en §2.x). Ver `feedback_transmittal_version_ejecutiva`.

**No incluir:** Date/Project/From/To en GENERAL INFORMATION (ya en header), submittals 25007-XXXX en RESPONSE SUMMARY, documentos internos ADASA, footer, cierre `*End of document*`.

### 3.2.1 Stream OOCC / L&A (espanol)

Flujo espejo del de BW Water pero **100% espanol**, para L&A Ingenieria y Proyectos (Pablo Castillo). Codigo `P22-TM-00-010-NNN-0`. Ubicacion **separada**: `INGENIERIA DE DETALLE OOCC/REVISIONES/` (README + Hitos propios; NO el arbol `REVISIONES/` raiz, que es exclusivo BW Water ingles). Estructura: `TRANSMITTALES/P22-TM-00-010-NNN-0/` con `crear_transmittal.py`, `P22-TM-00-010-NNN-0_TRANSMITTAL.md` (espanol, se envia), `_ANALISIS_TRABAJO.md` (interno), `COMENTARIOS/` (`agregar_comentarios_mc_*.py` + `*_CC_ADASA.pdf`). Codigos de respuesta 1/2/3/4 = mismos del TdR P22-TR-00-010-01-1.

**Idioma — reglas duras (CLAUDE.md §3.4 "NO mezclar idiomas"):**
- **ID de punto de revision = `NOTA-XX`** (no `NOTE-XX`). `OBS-XX`, `OBS-NPT`, `PEND-XX` se mantienen (ya neutros/espanol). El `NOTE` que se importa de doc-annotator (§3.8) es la **constante de color azul de la skill** — symbol de API, NO el texto del ID; los scripts OOCC ni la importan (usan `MAYOR`/`MENOR`).
- **Purgar anglicismos de jerga ejecutiva** que se filtran del patron ingles BW Water al reescribir en modo ejecutivo: `Tally`->`Recuento`, `Drivers`->`Determinantes`, `Trackeado/tracked`->`Seguimiento / en seguimiento hasta`, `at a glance`->`de un vistazo`, `baseline/deadline/review` -> equivalente espanol. Barrido pre-emision: `grep -niE "\b(Tally|Drivers?|Trackeado|NOTE)\b"` sobre `.md`/`.py`/scripts -> 0.
- El stream BW Water sigue 100% ingles; no cruzar terminologia entre streams. Detalle vivo: memoria `project_stream_oocc_lya.md` + `feedback_oocc_lya_espanol.md`.

**Consistencia transmittal <-> CC_ADASA y convencion Codigo 1:**
- **El listado de comentarios a planos del transmittal es espejo 1:1 de los CC_ADASA**: mismos IDs `OBS-XX`/`NOTA-XX`, misma instruccion, por plano y lamina. Los `NOTA-XX` suelen ser los comentarios base que el usuario escribio a mano sobre el plano; los `OBS-XX`, los cruces ADASA. No consolidar varios comentarios de un plano en una sola celda sin IDs (rompe la trazabilidad con el PDF anotado y permite que la prosa del transmittal diga algo distinto al cuadro — p.ej. "el anclaje debe ser preinstalado" cuando el cuadro dice "evaluar o justificar"). Tabla del transmittal: `Plano / Lamina | ID | Comentario`.
- **Convencion Codigo 1**: incluir en el Resumen Ejecutivo, tras la leyenda de codigos, la linea "Los documentos de la entrega que no aparezcan en el listado de respuesta se entienden Aprobados (Codigo 1)". L&A no tiene incorporada la nomenclatura 1/2/3/4 -> declarar la leyenda y esta convencion explicitamente.

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

**Cadena de correo separada — regla dura (CLAUDE.md §3.4 también)**: si la NT (o CT) responde a una cadena de correo específica del proveedor (ej. cover email que transmitió un Mitigation Plan), su correo de remisión es **Reply-To a esa cadena**, NO conjunto con un TM o instrumento de otra cadena. El riesgo procesal de "cross-references a un documento no recibido" se neutraliza enviando ambos el mismo día con códigos ADASA explícitos en las cross-references — no requiere fusionar en un solo correo.

**Numeración de sub-items**: contigua dentro de cada sub-sección (N.A, N.B, N.C, ...). Si durante revisión interactiva se descartan algunas contra-preguntas propuestas, renumerar consecutivamente antes de emitir (no dejar saltos tipo 2.A → 2.C que sugieran edición incompleta).

### 3.4 Correos

Carpeta: `CORREOS/[Mes YYYY]/YYYY-MM-DD/` con `crear_correo.py`, `*_Descripcion.md` (incluir "Contexto Interno (No enviar)"), output `*.docx`.

**Un solo `.md` por correo — el `*_Descripcion.md`.** El cuerpo del correo vive **hardcodeado en el `crear_correo.py`** (patron Document() directo); NO mantener ademas un `.md` de cuerpo aparte (duplica el `.py` y crea un espejo con drift). El `*_Descripcion.md` es el unico markdown: resumen del cuerpo + verificacion de fuentes + "Contexto Interno (No enviar)" + checklist pre/post-envio.

- Carpetas tematicas (`CORREO ENVIADOS POR TEMAS CONTRACTUALES/`, `CORREOS COMPRA EQUIPOS/`) en root de CORREOS — **NO mover**
- Al agregar correo: entrada nueva en la **Bitacora Cronologica** del README (y, si es cobertura de un transmittal, la fila del **Indice de Transmittales**)
- Correos usan `Document()` directo — sin template ADASA
- Tras envio: `BORRADOR` -> `ENVIADO` en `.md`, dejar respaldo (PDF/.msg) en carpeta, actualizar README.md
- **Fecha de carpeta == fecha del header del correo**: el path `CORREOS/[Mes YYYY]/YYYY-MM-DD/` debe coincidir con la `Date:` declarada en el `.docx`/`.md`. Si hay discrepancia (ej. carpeta `2026-05-26/` con body que dice "May 25, 2026"), mover los archivos a la carpeta de fecha correcta antes del envío y eliminar la carpeta vacía.
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

**Skill:** `doc-annotator` v1.6 (PyMuPDF). Patron de script: ver `agregar_comentarios_*.py` existentes en `REVISIONES/TRANSMITTALES/P22-TM-09-000-XXX-0/COMENTARIOS/`. Importar `MAYOR, NOTE, run_comentarios`. Estructura `COMENTARIOS`: `{id, fill, search, page_fallback, text, page_min(opt)}`.

> **Planos rotados (`rotation != 0`): verificar SIEMPRE por render PNG, no por `get_text()`/`annots()`.** En paginas rotadas la skill dibuja en el content stream, asi que `page.annots()` = 0 aunque el comentario es visible, y `get_text()` devuelve el texto logico **sin revelar la orientacion visual**. Usar `text_rotate = original_rotation` (no hardcodear 270, que deja el texto boca abajo en `rotation=90`) y cuidar el alto de caja con word-wrap. Cierre de revision: render PNG del cuadro comprobando que el ID y `Corregir:` aparecen completos y que el texto lee de izquierda a derecha. Ver memoria global `feedback_doc_annotator_rotated_textbox`.

**Regla por veredicto:**

| Veredicto | Anotaciones PDF |
|-----------|----------------|
| Code 1 — Approved | **NO ANOTAR** — sin observaciones, no incluir CC_ADASA |
| Code 2 — Approved as Noted | **ANOTAR** las NOTEs/OBSs relevantes al documento. No items de otros docs |
| Code 3 / 4 | Anotar todas las OBS y NOTEs del documento |

> **Code 1 sin anotaciones de ningun tipo** — items cross-document se trackean en Section 3 del transmittal. Esto se aplica tambien a un documento correcto as-is cuyas notas son entregables sobre OTROS documentos: es Code 1 (ver criterio §6.2), sin CC_ADASA; el script de anotacion y su PDF, si se generaron, quedan como traza interna (no se emiten ni se adjuntan).

> **Entregable Code 2 que NO admite anotacion: declarar la excepcion, no omitirla.** Un formato que no acepta el `CC_ADASA` (modelo `.nwd`, planilla nativa, archivo binario) no puede llevar PDF anotado aunque su veredicto lo exija. En ese caso las observaciones van **integras en el texto de su subseccion de la Seccion 2** y la **Seccion 4 lo dice explicito** ("X is a Navisworks file that cannot carry the annotation format used for drawings, so its observations are stated in full in Section 2.N"). Dejar el hueco sin explicar contradice de cara al proveedor la regla de que todo Code 2 se anota. Ver `reference_navisworks_automation_windows`.

> **Code 2 SIEMPRE lleva CC_ADASA con sus OBS/NOTE propios** (regla recurrente). El error tipico es generar solo CC_ADASA para Code 3 y dejar los Code 2 sin anotar, con el texto bajo la tabla Section 4 ATTACHMENTS diciendo "the Code 2 documents require no modification and carry no annotated PDF" — eso CONTRADICE la regla. Section 4 ATTACHMENTS debe listar TODOS los CC_ADASA generados (Code 2 + Code 3/4); el texto debe decir "All documents with open observations or notes carry annotated PDFs (X Code 3 + Y Code 2). Only the Z Code 1 — Approved documents carry no annotated PDF". Solo Code 1 carece de CC_ADASA.

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
3. **Cajetin apilado:** la skill hardcodea `"0"` en `cajetin.rows[2]`. Post-procesar tras `crear_documento_adasa(...)`: setear `cajetin.rows[2]` con Rev N historica (fecha original) y `cajetin.rows[1]` con Rev N+1 nueva. Leer fecha Rev N del `.docx`, no del timestamp.
4. **Documentos sin script generador:** patron **patcher** — abrir `.docx` Rev N como base, modificar in-place y guardar como Rev N+1. Usar `copy.deepcopy(source_row._tr)` para insertar filas preservando formato; actualizar header run-por-run para preservar Arial.

**Redistribucion de roles entre documentos:** si Rev N+1 cambia que documento asume un rol, actualizar descripciones en tablas de antecedentes/referencia para evitar duplicar autoridad.

### 3.11 Paquete BL Montaje Mecanico-OOCC ("Bases REV 0") — composicion y alcance

Reglas estables del paquete de licitacion `BASES DE LICITACION MONTAJE MECANICO-OOCC/` (codigo P22-BL-06-000-001-0). Estado operativo (revisiones, conteos, totales, fechas) en README.md; aprendizajes con contexto en las memorias citadas.

- **Generacion:** el BL se regenera del `.md` fuente unico con `md_to_adasa_docx.py` (ver §3); el Formato (Anexo A9) con `generar_formato_presupuesto.py` (idempotente — respaldar el `.xlsx` antes de re-correr). Correr el `[CHEQUEO LAYOUT]` del conversor (v7.7: encuadre de figuras + anchos de columna) antes de distribuir; `revisor-docx` de respaldo. No re-iterar tamanos de figura ni anchos a mano (memoria `feedback_conversor_layout_check`).
- **Paquete `INGENIERIA VIGENTE PARA CONSTRUCCION` (contrato adjudicado): cada plano viaja en PDF y en su DWG** de la misma revision, en la misma carpeta y con el mismo nombre base. Lo arma `construir_paquete_construccion.py` (argumento: el ZIP de la entrega vigente de Van Doorn, descomprimido con nombres cp437 a cp850; ver `project_bl_montaje_rev0_paquete`) desde una tabla explicita de nativos: el DWG es el que viajo en la misma entrega que el PDF, nunca uno de otra revision (un nativo emitido solo en DWG queda fuera hasta que llegue su ploteo). Regla 4 del autochequeo: todo PDF con DWG apareado, cero DWG huerfanos, rutas comparadas en NFC (el NAS devuelve las tildes en NFD). El gate de vigencia de `generar_ingenieria_vigente.py` incluye `.dwg`. La Nota Tecnica de control lo declara en el contenido del paquete. Ver `project_bl_montaje_rev0_paquete`.
- **Reemision del proyectista con la misma revision y contenido distinto:** rige la emision de la carta mas reciente, identificada por carta y fecha en la NT y en los LEEME; la anterior se archiva en `BORRADOR_REV0/_dossier_superseded_pre-<entrega>/` con el sufijo de su carta para que dos revisiones iguales no colisionen de nombre. La numeracion se objeta solo si la version anterior ya salio al contratista. Comparar las dos emisiones por superposicion y diff de la capa de texto, no por el cajetin. Ver `project_tm_oocc_005_hallazgos`.
- **Cubierta metalica (cobertizo) CIP descopada:** en esta licitacion NO se construye la estructura metalica de la cubierta, **solo su fundacion** (24 pernos F-1554 3/4" colados + proteccion interina); el fierro lo ejecuta ADASA en etapa posterior. Los documentos del acero de la cubierta (DWG-00-003-001, MC-00-003-001, ET-00-010-103) quedan fuera del paquete (`_cubierta_excluida_del_paquete/`); la fundacion se mantiene en DWG-00-002-007 LAM3. Memoria `project_descope_cubierta_cip`.
- **Memorias de calculo / itemizados / estimacion del consultor OOCC NO van al paquete** (decision del mandante): el dossier `5. OBRAS CIVILES (A2)` lleva solo planos + ET; la planilla economica es el Formato (A9). El BL/INDICE/LEEME no los referencian. SI se citan las memorias de **equipos** (Exfibro, KSB = base de cargas) y las **normas** (ACI 351/318 = criterio de diseno). Memoria `feedback_mc_oocc_fuera_del_paquete`.
- **Soportes a piso:** solo los soportes con detalle de placa base cuadrada en planta van a piso (dado/pedestal de hormigon, partida Formato 4.7); el resto va anclado a muro (mensula) o a soporte existente, sin dado. Memoria `feedback_soportes_a_piso_placa_base`.
- **Fosa de drenajes = TK-06-004** en el BL (los planos L&A la rotulan TK-06-002; error a corregir en la ingenieria, ver §3.7).
- **Plano DWG-00-002-005:** no se emite; los detalles de anclaje viven en los planos de fundaciones (002-002/003/007). No referenciarlo en el BL.

### 3.12 Respuestas a RFI de BW Water (round-trip)

Un RFI de BW Water (form `25007-RO-RFI-NNNN`) se responde **llenando el mismo .docx** (patron patcher §3.10, NO regenerar el form), no creando un documento aparte. Ubicacion `PROGRAMA y CONTRATO/RFI/RFI N/`.

- **Preservar el original recibido** (copia `_ORIGINAL.docx.bak`); emitir `..._ADASA_REPLY.docx`. El form trae una tabla "Information Request" (pregunta de BW Water) + un bloque "Replied Information" (To/From + celda de cuerpo vacia) que es lo unico que ADASA rellena. Las filas de seccion suelen ser celdas combinadas (gridSpan): `python-docx` devuelve la misma celda dos veces; editar una sola.
- **To = emisor del RFI** (p.ej. Billy Tan / BW Water), **From = Luis Rivera / Aguas Antofagasta**; el form **no trae celda "Replied Date"** → va como primera linea (bold) del cuerpo. Texto **100% ingles** (§3.4), referencias a la ET por **codigo + numero de seccion + nombre** (§2.4, ej. "the Technical Specification (P22-ET-09-000-001-0), Section 5.4.1 - Constructive Characteristics"), sin referencias internas (Van Doorn, `§N`, codigos OBS/Code). **Metadatos Word limpios** (`docx_metadata`, autoria "Luis Rivera Gonzalez", company "Aguas Antofagasta", en-US).
- **Persistir** el texto fuente en un `.md` de registro interno (no se envia). **Verificar** el borrador antes de emitir (workflow adversarial: exactitud vs ET + fidelidad al historial de transmittals + fugas internas + estilo/anti-IA). Render del form (Word COM via `win32com` late binding si la PIA tipada falla → PDF → PNG) para confirmar layout y cableado To/From.
- **Emision:** correo de cobertura corto (§3.4, transaccional) **Reply-To al thread del propio RFI** (cadena separada de los transmittals, §3.3.1/§3.4); el cuerpo confirma en una linea y adjunta el form lleno, sin repetir la sustancia. Registrar en README (estado del evento), no en CLAUDE.md.
- **Patcher clonable `llenar_rfi_reply_002.py`** para un RFI con la misma estructura de form (`doc.tables[1]`, rows 5/6/7). Los RFI ya respondidos y su trazabilidad viven en la Bitácora del README y en las memorias del proyecto.

### 3.13 PDF final desde Word real (TOC/campos actualizados) — NO LibreOffice

El PDF de un documento con TOC (transmittal, NT, consulta) **se genera abriendo el `.docx` en Microsoft Word y guardando como PDF**, porque el TOC es un campo de Word que **LibreOffice headless (`--convert-to pdf`) NO actualiza** — deja el placeholder "Right-click and select 'Update Field'". LibreOffice sirve solo para render de control interno, nunca para el PDF que se emite.

- **Script (macOS):** `_HERRAMIENTAS/exportar_pdf_word_mac.sh`. Uso: `./_HERRAMIENTAS/exportar_pdf_word_mac.sh "<entrada.docx>" ["<salida.pdf>"]`. Abre el docx en Word via `osascript`, **actualiza todas las tablas de contenido y campos**, hace `save as ... file format format PDF` y cierra. Equivalente Windows: `_HERRAMIENTAS/exportar_pdf_word.py`, Word COM.
- **El directorio de paso debe ser una RUTA ESTABLE DENTRO DEL CONTENEDOR DE WORD**, `~/Library/Containers/com.microsoft.Word/Data/pdf_export`. Word corre en sandbox y ante cualquier ruta que el usuario no le haya autorizado levanta el dialogo Powerbox "Conceder acceso al archivo". Un `mktemp -d` produce una ruta nueva en cada corrida, de modo que la autorizacion nunca sirve para la siguiente y el dialogo aparece SIEMPRE; una carpeta fija en `/private/tmp` tampoco basta, porque sigue siendo ruta ajena al sandbox. Dentro de su contenedor Word entra sin pedir nada.
- **No confundir ese dialogo con los otros dos.** El de **automatizacion** ("X quiere controlar Microsoft Word") se concede una vez en Ajustes del Sistema, Privacidad y seguridad, Automatizacion. El de **volumenes de red** aparece solo si Word toca `/Volumes/...`; con la escala no lo toca. Para saber cual es: `sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "select service, client, auth_value from access where client like '%Word%';"`.
- **Por que sigue habiendo escala aunque este equipo monte el NAS por SMB.** Sobre `/Volumes/` Word SI abre y guarda directo, sin -1708 (a diferencia de `~/Library/CloudStorage/`, donde es imposible y por eso existe el rodeo en el MacBook Pro). Pero hacerlo cuesta un permiso mas, porque Word no tiene acceso a volumenes de red. La escala se mantiene como default y el modo directo queda tras `WORD_DIRECTO=1`. El PDF termina igual en la carpeta del proyecto: lo mueve el shell, que si tiene el permiso.
- **Gotchas (documentados en el script):** Word necesita permiso de Automation (System Settings > Privacy & Security > Automation) — la primera corrida puede pedir confirmacion; usar `open file name "<ruta posix>"` (no `open POSIX file`, que queda mudo); `save as` directo sobre `active document` (no via variable, da -1708); **espera activa a que aparezca el documento**, no un `delay` fijo, porque con Word arrancando en frio tres segundos no alcanzan; cerrar los documentos abiertos en Word antes de reconvertir.
- **NO intentar automatizar el refresh del TOC con el puente UNO de LibreOffice** (rabbit hole: lo resuelve Word real). Ver memoria global `reference_word_mac_pdf_export` (incluye el gotcha del lock `~$*.docx` ante -1712 y LibreOffice como fallback solo de medicion).

### 3.14 Revision de un entregable de modelo 3D (`.nwd`)

Un `.nwd` es binario propietario: **no trae XML legible**. Lo revisable es su **base de propiedades por objeto**, que se vuelca con el puente de automatizacion Navisworks (`revisar_modelo_nwd.ps1`, patron y gotchas en `reference_navisworks_automation_windows`).

- **Los TAG se leen de la propiedad, no del nombre de capa.** La categoria es **`AutoCAD`** de AutoCAD Plant 3D (`Code`, `Class`, `Area`, `AreaCode`, `DesignStd`, `End Type`, `ControlValve`, `ActuatorType`). Antes de asumir el nombre del campo, volcar **un objeto con todas sus propiedades** y ver cual lleva el TAG. Cruzar contra capas produce observaciones falsas que hay que retractar.
- **Se cruza contra los listados aprobados de BW Water** (Equipment, Valve, Instrument y Line List), en las dos direcciones: en el modelo y no en el listado · en el listado y no en el modelo · mismo TAG con atributo distinto · colisiones de correlativo. Los listados en Codigo 1 son linea base contractual, no opinion.
- **NO se le exige rigor BIM** — propiedades de publicacion, conjuntos de seleccion, viewpoints, objetos tipados: la ET no lo pide y una observacion sin requisito que la sostenga es refutable (misma regla anti-invencion de §6.2). **SI se exige** que el archivo se identifique por su **codigo de documento y su revision**.
- Veredicto: **Code 2** si lo unico que cambia es identificacion y reconciliacion de TAG, incorporables al emitir Rev 0. Escala a **3** solo si el modelo **contradice en sustancia** un listado aprobado en Codigo 1. Al ser Code 2 no anotable, aplica la excepcion declarada de §3.8.

### 3.15 Correo ENTRANTE — BW Water y Bureau Veritas

Esta seccion regula el correo **recibido**. La 3.4 regula el saliente y no aplica aqui.

**Domicilio unico:** `CORREOS/_RECIBIDOS/`, con la convencion completa en su `_LEEME.md`, que es la **fuente unica** — tabla de ruteo, plantilla del `_correo.md`, reglas de nombre y deduplicacion. Ante discrepancia entre este CLAUDE.md y ese archivo, manda el `_LEEME.md`. Skill de operacion: **`correo-taltal`** (global), con el procedimiento de navegador en su `references/`.

- **Alcance:** solo `@bw-water.com` y `@bureauveritas.com`, por dominio y no por lista de personas (las direcciones tienen capitalizacion inconsistente y hay alias cortos). Los scripts abortan con cualquier otro remitente.
- **Se captura una vez; el payload va a su domicilio de siempre.** El `_correo.md` queda en `_RECIBIDOS/` con el puntero, y los adjuntos se rutean: submittal a `ENTREGAS_BWWATER/ENTREGA NN/`, request to witness a `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/03 SOLICITUDES BW (RWI)/RWI NNN AAAA-MM-DD/`, informes BV a `HITO BUREAU VERITAS/04 INFORMES BV/IRNNN AAAA-MM-DD/` (mapa del frente en su `_LEEME.md`), RFI a `PROGRAMA y CONTRATO/RFI/RFI N/`. No se duplican los arboles que ya usan el Master Register y los transmittals.
- **`PAQUETE_INSPECCION_BV/` no se toca nunca.** Hay un enlace Synology publicado a Bureau Veritas; moverla o renombrarla rompe un enlace externo vivo. Si un correo trae version nueva de algo que esta ahi, queda en `adjuntos/` y se avisa.
- **La lista real de la carpeta manda sobre la tabla del correo.** Cuando el submittal llega por enlace de OneDrive, la carpeta suele traer mas archivos de los que declara el cuerpo — tipicamente los **archivos nativos** de los planos, que el correo omite. El `_correo.md` se completa con lo que hay en la carpeta y **la diferencia se anota**: es informacion de revision. Archivar segun el correo deja archivos fuera del proyecto sin que nadie lo note (ver `feedback_correo_entrante_lista_real_manda`).
- **Deduplicar por hash del contenido, nunca del contenedor** — misma regla que ya rige para los adjuntos de Outlook. `instalar_adjuntos.py` **se detiene** ante un archivo con mismo nombre y contenido distinto en vez de sobrescribir: eso es control de revisiones y es hallazgo.
- **El `_REGISTRO.md` es indice durable, no eje cronologico.** La Bitacora del README sigue siendo el unico eje. Un correo capturado **no** genera entrada de Bitacora automaticamente: se propone y la aprueba el usuario. El `.xlsx` es derivado, se regenera y nunca se edita a mano; gate `openpyxl_lint.py` antes de darlo por bueno.
- **No corre desatendido.** Requiere Chrome con la sesion de Outlook Web viva. El conector de Microsoft 365 exige aprobacion de administrador del tenant de ADASA, y el Outlook nuevo no expone COM ni deja cache local. Dos puntos exigen a una persona y hay que anunciarlos, no colgarse: **iniciar sesion** cuando caduca, y **confirmar en Chrome una descarga retenida** (nunca renombrar el `.crdownload` para saltarse la confirmacion).
- **Nunca abrir el dialogo de impresion de Chrome:** es modal y bloquea la automatizacion hasta que alguien lo cierre a mano.

---

## 4. Skills Disponibles

| Skill | Version | Uso |
|-------|---------|-----|
| **template-adasa** | v7.7 | Documentos Word formato ADASA |
| **large-pdf-reader** | v5.0 | Extraccion de PDFs grandes |
| **canvas-design** | - | Diagramas y arte visual |
| **anti-ia** | v6.1.6 | Escritura analitica y evaluacion textos IA. Modos: `escribir`, `evaluar`, `revisar`, `smoke` |
| **playground** | - | Exploradores HTML interactivos |
| **doc-annotator** | v1.6 | FreeText Acrobat + cuadros+flechas P&ID + comentarios Word DOCX |
| **correo-taltal** | v1.0 | Captura y archivo del correo entrante de BW Water y Bureau Veritas (ver §3.15) |

### 4.1 Template ADASA v7.7 — API

**Archivos:** `~/.claude/skills/template-adasa/ejemplo_documento.py` (API programatica) y `md_to_adasa_docx.py` (conversor Markdown->Word autonomo, SI existe — ver §3). `config_defaults.py`/`table_utils.py`/`docx_metadata.py` tambien existen y los usa el conversor.

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
| TT (tipo) | ET, DWG, LI, CD, TM, CT, **NT**, IT, **BA** (calidad/fabricacion BW Water: ITP, NDE Plan, procedimientos de prueba, pintura) |
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

> **Verificar la solicitud antes de codificar un incumplimiento (regla anti-invención).** Antes de levantar una observación como falta/incumplimiento de BW Water, verificar contra (a) el historial de transmittals previos, (b) la ET y (c) la Oferta Rev1, si ADASA realmente lo solicitó y con qué alcance. Si **nunca se pidió**, es un **PEDIDO NUEVO de ADASA** (extensión/clarificación), **no** un incumplimiento — framing y severidad distintos: redactar "ADASA extiende/requiere…" (no "missing/absent/agreed"), sin imputar falta a BW Water. Un requisito que vive solo en ingeniería interna de ADASA (p.ej. lógica de Van Doorn) puede fundar el pedido pero **no se cita a BW Water** (§3.7). Si BW Water cumplió lo acordado y solo se agrega alcance, el documento no se degrada por eso. Ver `feedback_comprometido_vs_solicitud`, `project_senales_interfaz`, `project_hart_precedente`.

### 6.3 Bloque ejecutivo `Action to issue at IFC Rev 0`

Cada subseccion de documento en la Seccion 2 del transmittal cierra con un bloque ejecutivo, escaneable, que indica que debe hacer BW Water para llevar ese documento a IFC Rev 0. Con el §2 condensado (§3.2: sin tablas OBS), el bloque Action, junto al Status corto, **es** la subseccion: enumera las acciones en **una frase** citando el **rango de IDs** que las detalla en el CC_ADASA ("(OBS-01 to OBS-03 and NOTE-01 on the annotated PDF)"), sin reproducir el texto de cada observacion. Formato por veredicto:

| Veredicto | Bloque de cierre de la subseccion |
|-----------|-----------------------------------|
| **1 - Approved (sin pendientes)** | `**Action: none — accepted; issue directly at IFC Rev 0.**` |
| **1 - Approved (con entregables cross-document)** | `**Action: none on this document — accepted; issue directly at IFC Rev 0.**` + `Related deliverables tracked in Section 3:` con la lista (no modifica el documento revisado) |
| **2 - Approved as noted** | `**Action to issue at IFC Rev 0 — no new [doc] revision required:**` + **una frase** con los cambios a incorporar **en el propio documento** + el rango de IDs (`... on the annotated PDF`) + 1 linea de condicion de aceptacion ADASA |
| **3 / 4** | `**Action — re-issue as Rev X:**` + **una frase** con lo que debe corregirse + el rango de IDs (`... on the annotated PDF`) |

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

### 6.5 Revision de la Hoja de Respuesta a Comentarios (CCS) — OBLIGATORIA

Todo documento **re-revisado** de BW Water trae al final una **Consolidated Comment Sheet (CCS / Comment Sheet)** que declara cómo respondió a cada comentario de ADASA de la revisión anterior (columnas típicas: N° de comentario / comentario ADASA / respuesta BW Water / status). Aparece embebida como última(s) hoja(s) del documento (como última hoja, con encabezado "Consolidated Comment Sheet", o marcada "(with CCS)" en el DDSR).

**Norma: revisar la CCS ítem-por-ítem es obligatorio en cada transmittal.** Por cada comentario declarado en la CCS:

1. **Mapearlo** a su OBS/NOTE del TM de origen (usar el Master Register / la memoria del TM).
2. **Verificar contra la fuente primaria** (el propio documento, la ET, la Oferta Rev1, el P&ID, la Line List aprobada) que el cambio **realmente se hizo** — NO tomar por buena la declaración "closed/addressed/complied" de BW Water.
3. **Clasificar:** `cerrado real` / `declarado sin estarlo` / `parcial`.

Un comentario **declarado cerrado sin estarlo** es hallazgo válido y **reincidente** — se levanta de nuevo citando que es la 2ª/3ª vez que se declara corregido. La revisión de la CCS **no reemplaza** la verificación adversarial de lo que el proveedor *agregó*: un dato nuevo que la CCS no destaca puede ser el que fija el código (ver `feedback_verificacion_adversarial_encuentra_el_driver`; precedentes en `project_tm27_state` y `project_tm29_state`). La CCS es además la fuente para poblar la columna "Responde a" de la disposición interna y para redactar el Status corto de la Sección 2 del transmittal (§3.2). Su ausencia en un documento que debía traerla es en sí una NOTE (calidad documental).

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
| Protocolo señal | 4-20mA + HART obligatorio **a nivel de instrumento** (cada instrumento de campo HART-capaz). La ET 5.5 pide que el protocolo de *la instrumentacion* sea 4-20mA+HART; **NO** exige decodificacion HART central en el PLC (multiplexor / HART-a-SCADA) salvo mencion explicita. Un PLC que lee 4-20mA con HART accesible por comunicador handheld de campo **cumple**. Instrumento solo-4-20mA sin HART = hallazgo valido; exigir HART central al PLC = **over-reach** (ver `project_hart_precedente`) |
| Switches temperatura (TSH) | Solo alarma ON/OFF — NO monitoreo continuo |
| Transmisores proceso | Verificar rango/unidades/tag contra IO List y P&ID |
| Entradas analogicas | Cada instrumento en IL debe tener punto IO |
| **Conductividad** | **Contacting** (Rosemount 400, SS316L): <20 mS/cm. **Toroidal** (Rosemount 228) **OBLIGATORIO >20 mS/cm** (salmuera, rechazo etapa 1/2). ET §5.5.5 NO aplica a rechazo concentrado segunda etapa RO (~85–135 mS/cm) — SS316L incompatible con 45,000–55,000 ppm Cl⁻ |
| **Esquema I/O / interfaz** | El esquema de I/O de campo **soft sobre Ethernet/IP** (tipo BOOL: instrumentos, valvulas VE-09, bombas dosificadoras) esta **aceptado**. Solo las **señales de coordinacion modulo↔PLC externo de planta (DCS)** son **hardwired relay-contact**: enable XA005, running YA001, fault status y local/remoto. **NO exigir hardwired** a un RUNNING/feedback de equipo de campo (p.ej. dosificadoras BOOL) = reabre el esquema soft-I/O ya aceptado = **over-reach**. El unico matiz valido es la **fuente** del dato (realimentacion de la bomba/VFD sobre la red, no eco del faceplate del HMI), no el tipo soft (ver `feedback_soft_io_ethernet_aceptado_n20`) |

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

### 7.6 Tableros de Fuerza y Control (ET §5.4)

- **Proteccion: NEMA 4X o IP equivalente, no inferior** (ET §5.4.1 Caracteristicas constructivas; reforzado por el PIE Base ITP 6.1). Una clase < NEMA 4X (p.ej. IP55) = incumplimiento ET duro y citable.
- **Material: la ET NO exige SS316L.** ET §5.4.3 (Terminaciones) **permite acero pintado** (3 capas: anticorrosiva + granallado a metal blanco + espesor total ≥100 µm) como alternativa al inoxidable. **NO fundar un hallazgo en "la ET exige SS316L para el tablero"** — es refutable.
- El **SS316L del PLC-LCP lo fija el LCP Datasheet aprobado** (nVent Hoffman FS66S, SS316L unpainted, NEMA 4X/IP66) y el IFC Single Line Diagram ("METAL CLAD, NEMA4X/IP66"). Al objetar un envolvente inferior en el Outline/plano, **liderar con la contradiccion vs los documentos aprobados de BW Water** (datasheet + SLD, irrebatible), citar la ET por **codigo + Section 5.4.1 - Constructive Characteristics** (NEMA 4X) como soporte (§2.4), y no afirmar un requisito ET de material. Generaliza la regla anti-invención §6.2: verificar que la fuente realmente exija lo objetado; si la ET permite una alternativa, el incumplimiento es vs el documento aprobado que gobierna, no vs la ET. Ver `reference_et_tableros_nema4x_no_ss316l`.
- **Materialidad interior vs exterior:** al reconciliar el material del enclosure, el **exterior** (cuerpo, puerta, techo, panel trasero, plinto, gland plates) va en SS316L per el datasheet aprobado; los **componentes internos de montaje** (mounting plate, swing door interna, frame interno) en galvanizado/laminado **son aceptables** — la propia ET Section 5.4.1 permite equipos montados dentro del gabinete "siempre que se mantenga NEMA 4X" y no bajan el rating. RAL7035 solo interno; exterior SS316L unpainted; el Outline se reemite alineado. Ver `project_plc_delay_rfi002_07jul`.

---

## 8. Ubicacion de Archivos .md

| Contenido | Carpeta |
|-----------|---------|
| Bases Tecnicas (ET, BAE, PIE) | `BASES TECNICAS/md/` |
| Ingenieria Basica | `BASES TECNICAS/INGENIERIA BASICA/md/` |
| Oferta Tecnica (Rev.1 VIGENTE) | `OFERTA TECNICA/md/` |
| Contrato C-4300 | `PROGRAMA y CONTRATO/CONTRATO C-4300/md/` |
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

### 9.3 Plazo y Multas — la Cita es Doble

| Que se cita | Clausula BAE |
|---|---|
| El **plazo** de entrega del modulo | **27** — Plazos de Ejecucion del Pedido (maximo 300 dias corridos desde la Notificacion de Adjudicacion; Plazo Contractual total 510 dias hasta Recepcion Provisional) |
| La **multa** por atraso EXW | **43.1 letra b)** — 0,2% diario del valor neto total del Contrato por dia calendario de exceso sobre el plazo de la Clausula 27 |
| El **tope** | **43.4** — 15% del monto neto, acumulado por cualquier concepto |

Otras letras de la 43.1: **c)** 0,1% diario por atraso en comisionamiento y puesta en marcha; **d)** 0,05% diario por no entrega de la documentacion final, cuya lista de "documentos principales" incluye el PIE detallado, la Filosofia de Control, los manuales, los As-Built y el **Dossier de Calidad Final de Fabricacion**.

> **Citar la Clausula 27 como fuente de la multa es refutable:** la 27 fija el plazo, la sancion vive en la 43.1. **Antes de cursar multa, leer la fecha de la Notificacion de Adjudicacion en el documento original de ADASA** — calcularla sobre el `Contract Award / NTP` que rotula el cronograma **del proveedor** deja el reclamo atacable, por sólida que sea la coincidencia. Aplicacion del mismo criterio anti-invencion de la Seccion 6.2. Ver `project_plazo_entrega_vencido_03ago`.

> **Aviso de inspeccion con tercero:** vive en el **cuerpo de la Clausula 37** (30 dias de antelacion para suministros internacionales, 10 para nacionales), **no en la 37.2**. La **37.1** es *Intervencion de Tercero Inspector* y la **37.2** son los plazos de revision y aprobacion que asume ADASA (7 dias habiles de revision documental).

---

## 10. Listado Consolidado EVI

**Archivado.** El listado EVI y el listado de activos ya no se usan; sus scripts y planillas estan en `_ARCHIVO/` con un `_LEEME.md`. Esos scripts rotulan la fosa de drenajes como TK-06-002: si alguna vez se reactivan, corregirla a TK-06-004 (ver Seccion 3.7).

---

## 11. Revision de Procurement vs Baseline

**Carpeta:** `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA <AAAA-MM-DD>/`. **Baseline:** ver README §"Baseline Schedule (05-Mar-2026)".

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

**El diff se automatiza, no se hace a ojo.** `diff_trackers.py` (Procurement tracking, hoja `Weekly Dashboard (2)`, clave = item de equipo) y `diff_fabrication_schedule.py` (hoja `RO system`) en la misma carpeta: `read_only=True`, sin pandas, salida `.md` re-ejecutable, cero escritura sobre los `.xlsx`. Ambos emiten solo lo que cambio mas un bloque **slip silencioso** (fecha movida sin entrada en el `Change Log`). **Que el `Change Log` siga vacio mientras las fechas se mueven es en si el hallazgo** y se reporta como tal.

> **El layout de estas planillas NO es estable entre versiones.** Resolver las columnas **leyendo la fila de encabezado** con un mapa de alias, y comparar solo las columnas presentes en ambas versiones. Comparar por indice de columna alinea mal toda la planilla y produce un diff enteramente falso (una columna ausente desplaza a todas las siguientes). El script debe reportar el cambio de esquema como seccion propia, y declarar las versiones que no encuentra en vez de saltarselas en silencio.

### 11.1 Registro de Compromisos (P22-IT-06-000-006-0)

Vive en `PROGRAMA y CONTRATO/SEGUIMIENTO COMPROMISOS/`. Sigue **quien debe que, para cuando y con que respaldo se puede exigir**, de las dos partes. Separado a proposito del Master Register: aquel es revision documental, este es administracion de contrato.

- **`compromisos.yaml` y `hitos.yaml` son la FUENTE UNICA**; el `.xlsx` es DERIVADO y **nunca se edita a mano** (se regenera con `generar_excel_compromisos.py` y la edicion manual se pierde). Un cambio de estado se escribe en el YAML.
- **Lo que cambia por un EVENTO va como valor; lo que cambia por el PASO DEL TIEMPO va como formula.** El `Estado` es valor; el `Semaforo` y los `Dias vs. compromiso` son formulas con `TODAY()` y el color lo pone el formato condicional. Un relleno fijado en generacion es correcto el dia de la corrida y falso al siguiente.
- **Ninguna fecha se infiere.** "Proxima semana" u "once ready" producen `SIN FECHA`, que se colorea: un compromiso sin vencimiento es un defecto de gestion, no un estado neutro.
- **`Origen de la fecha`** (`CONTRACTUAL` / `COMPROMISO ESCRITO BW` / `COMPROMISO VERBAL-MINUTA` / `FIJADA ADASA`) dice de antemano con que municion se reclama. **`Reprogramaciones`** cuenta desplazamientos de fecha, no menciones: es la prueba objetiva de un patron.
- **Gates:** `validar_fuente()` **aborta** (no advierte) · `openpyxl_lint.py` exit 0 sobre `.py` y `.xlsx` · render con **Excel COM real**, no LibreOffice (abre los `.xlsx` con el recalculo desactivado y mostraria vacias las columnas de formula). En un estilo diferencial (`dxf`) el relleno va con **`bgColor`**, no `start_color`, o la regla se aplica sin pintar nada — defecto que solo se ve al renderizar.
- **Regla anti-contradiccion:** si el README y el registro discrepan en una fecha vigente, **manda el registro**. Una fecha nunca se escribe dos veces como estado vivo.

Ver `project_registro_compromisos`.

---

## 12. Mantenimiento

- **README.md** se actualiza cuando cambia estado operativo: documentos entregados/pendientes, correos enviados, deadlines, metricas, baseline.
- **Estructura y formato del README (regla dura):** exactamente tres bloques `##`, en este orden. (1) **`## Estado Vigente`** — snapshot corto al inicio que se **pisa** en cada cambio (no se acumula): ultimo TM + veredicto, entregas recibidas, Master Register (tally + items/delivered + TMs/entregas), baseline, proximos hitos/deadlines, frentes abiertos. (2) **`## Bitacora Cronologica`** — el **UNICO eje cronologico**, **mas reciente primero**; toda entrada NUEVA se agrega **arriba** con el formato `### AAAA-MM-DD — Titulo — ESTADO` (fecha ISO; estado normalizado `ENVIADO` / `BORRADOR` / `RECIBIDO` / `GENERADO` / `DECIDIDO` / `INTERNO`) + descripcion concisa (documentos con ruta + veredicto/tally + cierres/pendientes). (3) **`## Referencias Durables`** al final: TODO lo estable como `###` (Informacion, Estructura, Baseline, Equipos, Contactos, **Indice de Transmittales** N1→Nx tabular, **Registro de Revisiones por item**, QA de nomenclatura, Adicionales, Revision BL). **PROHIBIDO crear un segundo eje cronologico/narrativo** (p.ej. "Transmittales historico" con detalle por carpeta, "Cronologia por fases"): el detalle de cada evento vive en su entrada de Bitacora; los indices de Referencias Durables son **tabulares** (una fila por item), no narran. Un evento se documenta UNA vez, en la Bitacora.
- **CLAUDE.md** se actualiza cuando cambia metodologia estable: generacion de documentos, skills, criterios tecnicos, codificacion, anti-IA. **Regla estable = instruccion atemporal**; su procedencia (por que/cuando se aprendio) va como `(ver \`memoria_slug\`)` o a la Bitacora del README, **NUNCA incrustada en la regla**. **Prohibido en CLAUDE.md:** `TM N<n>`, fechas `DD-Mmm(-AAAA)`, `Regla del usuario <fecha>`, `Aplicado: …`, `corregido/caso/calibrado en TM N/RFI <fecha>` — son citas de eventos que envejecen la regla. La trazabilidad datada vive en README.md, en `git log CLAUDE.md` y en las memorias. El footer solo lleva la version vigente, sin historial datado.
- **Memorias del proyecto** guardan los aprendizajes no obvios y la trazabilidad de decisiones con contexto.

- **El historial de README.md y CLAUDE.md vive en git, no en copias `.bak`.** Los dos estan versionados y **no se crean respaldos manuales antes de editarlos**: para eso esta el repositorio. Un documento vivo sin versionar acumula copias hasta que la raiz deja de leerse, de modo que **una pila de `.bak` es el sintoma de que falta control de versiones, y la correccion es versionar el archivo, no borrar las copias**. El `.gitignore` de la raiz excluye `.DS_Store`, `*.bak*`, los locks `~$*` de Office y las corridas `.multi-audit-*`.
- **Antes de borrar un respaldo, correr el gate de perdida.** Extraer del respaldo sus claves de contenido (en el README, los encabezados `### AAAA-MM-DD` de la Bitacora), comprobar que **cada una** tenga equivalente en el archivo vivo, e investigar toda diferencia antes de borrar y no despues. Un respaldo en un formato anterior que el gate no sepa leer se verifica a mano por piezas clave. Ver `feedback_readme_en_git_evita_los_bak`.
- **Se versiona la fuente y la documentacion, no el derivado.** El arbol del proyecto pesa del orden de 10 GB en PDF, planos y modelos: al repositorio van los `.md`, `.py`, `.sh`, `.yaml` y `.json`; los `.docx`, `.pdf` y `.xlsx` generados se regeneran de su fuente y no se agregan. Es la misma regla que ya rige entre el `.md` fuente y el Word que sale de el (Seccion 3).

> **Regla de oro:** Si la informacion tiene fecha especifica o puede quedar obsoleta en semanas, va al README. Si es una instruccion que Claude debe seguir siempre, va al CLAUDE.md.

---

*Version 6.34 — 5 de octubre de 2026. Historial de cambios de metodologia: ver `git log CLAUDE.md` (este footer NO acumula changelog datado, per Seccion 12).*

> **Historial de cambios de metodologia:** ver `git log CLAUDE.md`. Trazabilidad operativa del proyecto (eventos, fechas, correos, schedule): [README.md](README.md). Aprendizajes no obvios: memorias del proyecto.
