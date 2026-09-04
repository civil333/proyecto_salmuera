# Instructivo — Actualización de la BL Montaje y el Formato de Presupuesto con la Ingeniería OOCC Rev B

**Proyecto:** Módulo Segunda Etapa de Salmuera, Planta Desaladora Taltal (BAE 12803).
**Documentos a actualizar:** `BL_MONTAJE_TALTAL_REV0.md` y `Formato de Presupuesto.xlsx` (vía su generador).
**Fuente de la actualización:** ingeniería de detalle de Obras Civiles y Estructuras Metálicas **Rev B** — `INGENIERIA DE DETALLE OOCC/P22-TR-00-010-01-0/ENTREGAS/ENTREGA 4`.
**Estado de este instructivo:** para revisión y aprobación antes de ejecutar. Documento de gobierno interno (no se distribuye, no se captura al segundo cerebro).
**Fecha:** 01-Jun-2026.

> **Propósito.** Fijar por escrito los criterios, las fuentes, el mapeo de cantidades, las correcciones obligatorias y la mecánica de edición, para actualizar la BL y el Formato sin improvisar sobre la marcha. Cualquier cambio a estos documentos debe poder justificarse contra una regla de este instructivo.

> **Nota de actualización (18-Jun-2026) — descope de la cubierta metálica CIP.** Por cambio de alcance posterior, la **cubierta metálica (cobertizo) del sistema CIP no se construye en esta licitación** (solo su fundación, con los pernos F-1554 colados + protección interina; la estructura metálica la ejecuta ADASA en una etapa posterior). En consecuencia, **las partidas Rev B de estructura metálica de la cubierta propuestas en este instructivo (acero A36, panel PV-6, esquema C5-M) quedan sin efecto**; en el Formato vigente se eliminó la partida de acero de la cubierta y solo permanece su fundación (Cap. 4 ítem 4.3). El resto del instructivo (fundaciones, fosa, drenajes, impermeabilización, cámaras) sigue vigente. Ver README §9 (entrada 18-Jun-2026).

---

## 1. Objetivo y alcance

Incorporar la cubicación y las partidas de obra civil y estructura metálica que aporta la ENTREGA 4 (Rev B) al Cap. 4 del Formato de Presupuesto y, donde corresponda, a las secciones de obra civil de la BL. El montaje mecánico (Cap. 1 a 3 del Formato) **no** es alcance de esta actualización.

Esta ronda entrega **solo este instructivo y el diseño de la estructura**. No se editan el generador, el xlsx ni la BL, y **no se cargan cantidades**, hasta que el instructivo esté aprobado (ver Sección 11).

## 2. Fuentes y precedencia

Orden de prevalencia para cualquier dato:

1. **Términos de Referencia** `P22-TR-00-010-01-1` (alcance, partidas mínimas, clase de estimación).
2. **ENTREGA 4 Rev B**, en este orden de confiabilidad para cubicar: **Memorias de Cálculo** (dimensiones y armaduras verificadas) → **planos** → **Especificaciones Técnicas** → **Itemizados** (planillas de cubicación y precio referencial de L&A).
3. **BL Rev 0** (la versión vigente del documento que se actualiza).

> **Caveat Rev B (importante).** La ENTREGA 4 está **en revisión** — el Transmittal N2 (P22-TM-00-010-002-0) le dio veredicto **3 — Por revisar**. Por lo tanto, **las cubicaciones son referenciales y pueden cambiar en la Rev 0** de la ingeniería OOCC. Toda cantidad cargada se rotula "referencial, Clase 2 AACE, sujeta a Rev 0 de OOCC".

## 3. Qué es el Formato (y qué NO es)

- El **Formato de Presupuesto** es la **planilla de cotización de ADASA** para la licitación a **suma alzada**: ADASA entrega las **cantidades (CANT)**; el **oferente cotiza el precio unitario (P.UNI)**. Por eso en el Formato **P.UNI = 0/vacío** y los totales son fórmulas.
- Los **Itemizados de L&A** (P22-IT-00-010-101/102/103) son **referencia de cubicación** (traen además precios referenciales de L&A); **no** son el Formato. Se usan para extraer las cantidades, no para copiar precios.
- Clase de estimación: **Clase 2 AACE** (acordada en la reunión de arranque, Minuta `067-032-032-COR-MI-001`), no la Clase 1 del TR. El Formato lo declara como "presupuesto referencial Clase 2".

## 4. Regla dura: respetar el Formato actual

El Formato vigente se conserva como base. **No** se reinventa:

- **6 columnas exactas**: ITEM · PARTIDA · UNID. · CANT. · P.UNI. · TOTAL.
- **4 capítulos**; estilos, paleta y bordes Rev 0; fórmulas de totalizadores (Costo Directo, GG %, Utilidades %, Total Parcial, IVA 19 %, Total General).
- **Cap. 1 (HDPE + soportes), Cap. 2 (estanque) y Cap. 3 (bomba) quedan intactos.**
- Toda la actualización ocurre **dentro del Cap. 4 OBRAS CIVILES**, extendiéndolo con las partidas nuevas, sin alterar el formato visual.

## 5. Diseño propuesto del Cap. 4 (la "estructura")

Propuesta de partidas (numeración flat 4.x como en el Rev 0; **CANT en blanco en esta ronda**). Las fundaciones se cotizan por **m³ de hormigón G25** (el P.UNI incluye moldaje); el **emplantillado, la armadura y los pernos van en líneas separadas** (decisión del usuario). La columna "Fuente Rev B" indica de dónde se tomará la CANT cuando se cargue.

| Ítem | Partida (propuesta) | Unid. | Fuente Rev B (cubicación referencial) |
|------|---------------------|-------|----------------------------------------|
| **Movimiento de tierra** ||||
| 4.1 | Excavación común + retiro de excedentes (fundaciones + zanjas de drenaje) | m³ | IT-101 (exc ≈112,6 / retiro ≈24) |
| 4.2 | Relleno seleccionado/estructural compactado + base estabilizada bajo losas | m³ | IT-101 (≈91) |
| **Hormigones de fundación (G25, incluye moldaje)** ||||
| 4.3 | Fundación estanque TK-06-001 (F4) | m³ | IT-102 6,34 / MC-002-001 |
| 4.4 | Fundación dinámica bomba BH-06-001 (F3, ACI 351) | m³ | IT-102 0,945 / MC-002-002 |
| 4.5 | Fundación contenedor módulo RO (F2) | m³ | IT-102 7,76 / MC (verificar código) |
| 4.6 | Fundación sistema CIP (F2b) | m³ | IT-102 7,36 / MC (verificar código) |
| 4.7 | Fundación de la cubierta metálica CIP | m³ | IT-102 2,38 |
| 4.8 | Fosa de drenajes TK-06-004 (F5) | m³ | IT-102 1,66 |
| 4.9 | Fundación/radier planta salmuera (F1) - radier de operación | m³ | verificar fuente (no aparece explícito en IT-102; revisar planos -002-001/-001-001) |
| 4.10 | Emplantillado G10 (e=0,05) bajo fundaciones | m³ | IT-102 1,91 |
| **Acero, pernos y elementos embebidos (líneas separadas)** ||||
| 4.11 | Armadura de refuerzo A630-420H (todas las fundaciones) | kg | IT-102 ≈2.100 (ø16 820 + ø12 1.100 + ø10 180) |
| 4.12 | Pernos de anclaje preinstalados HAS-V F1554 (1" / 5/8" / 3/4") | un | IT-102 36 (8+4+24) |
| 4.13 | Conectores Nelson stud 5/8" | un | IT-102 40 |
| 4.14 | Malla Acma C-393 (fosa) | m² | IT-102 10,7 |
| 4.15 | Parrilla de piso PRFV pultruida (fosa, tránsito liviano de personas) | m² | IT-102 1,87 (TM N2: especificar PRFV) |
| **Cubierta metálica estructural (CIP)** ||||
| 4.16 | Estructura metálica cubierta CIP - perfiles ASTM A36 (vigas, columnas, conexiones) | kg | IT-103 ≈1.596 (perfiles 1.330 + conexiones 266) |
| 4.17 | Panel de cubierta PV-6 prepintado | m² | IT-103 25,2 |
| **Terminaciones y protecciones** ||||
| 4.18 | Impermeabilización de elementos enterrados (fosa + fundaciones en contacto con terreno) | m² o gl | ET-102 / DWG-00-002-004 / TM N2 (a cubicar) |
| 4.19 | Protección anticorrosiva C5-M de la estructura metálica (ISO 12944) | m² o gl | ET-103 / TM N2 (a cubicar) |
| **Sistema de drenaje** ||||
| 4.20 | Sistema de drenaje del módulo (canaleta + sumideros + HDPE Ø63 + cámaras CD-06-00N + conexión a TK-06-004) | gl | partida global (existente 4.9) |

> Esta tabla es una **propuesta para revisión**. El usuario puede fusionar, dividir o reordenar partidas antes de implementarla. El conteo crece respecto a los 9 ítems del Rev 0 porque se desglosa acero/pernos y se agregan las 4 familias acordadas; el **formato** (columnas, estilos, capítulos, Cap. 1-3) se mantiene.

## 6. Tabla de pendientes (gap analysis)

**Formato — Cap. 4:**

| Pendiente | Estado actual | Acción |
|-----------|---------------|--------|
| Cantidades de fundaciones | CANT vacía (4.1-4.6 actuales) | Cargar m³ de hormigón desde IT-102 / MC (Ronda C) |
| Excavación / relleno | CANT vacía | Cargar desde IT-101 (Ronda C) |
| Cubierta metálica estructural | **No existe partida** | Agregar 4.16-4.17 (Ronda B) |
| Impermeabilización | No existe partida | Agregar 4.18 (Ronda B) |
| Protección C5-M | No existe partida | Agregar 4.19 (Ronda B) |
| Acero / emplantillado / pernos / malla / parrilla | Implícitos en la fundación | Desglosar como líneas 4.10-4.15 (Ronda B) |
| Tag fosa | "TK-06-004" en el Formato (correcto); IT-102 de L&A dice "TK-06-002" | Mantener TK-06-004; no arrastrar el tag erróneo de L&A |
| Clase de estimación | No declarada en el Formato | Declarar "referencial Clase 2 AACE" |

**BL `.md` — obras civiles (Sección 6):** el texto de alcance ya está completo y corregido (fosa TK-06-004, cubierta metálica en la Sección 6.8, impermeabilización citada en el listado de planos, fundaciones independientes). La actualización Rev B del BL es **ligera**: opcionalmente citar que las cubicaciones de referencia provienen de la ingeniería OOCC Rev B (ENTREGA 4) y verificar coherencia de tags/pesos con el Formato. El BL describe **alcance**, no cantidades; las cantidades viven en el Formato.

## 7. Correcciones obligatorias a propagar

1. **Fosa = TK-06-004** (no TK-06-002). El Itemizado de L&A trae el tag erróneo; el Formato y la BL usan TK-06-004.
2. **No** incorporar la pestaña **"Interconexión La Chimba"** de los Itemizados de L&A (ajena al proyecto).
3. **Declarar Clase 2 AACE** (Minuta de arranque), presupuesto referencial.
4. **Verificar el mapeo de códigos** MC-004 / MC-005 ↔ Contenedor RO / Sistema CIP antes de asignar el m³ de cada fundación (hay etiquetas cruzadas entre fuentes: el inventario de ENTREGA 4 rotuló MC-004=CIP y MC-005=Contenedor RO, mientras el registro del proyecto los tenía al revés). Confirmar contra la portada de cada MC.

## 8. Regla de edición (dura)

- **El Formato se actualiza editando el generador** `script/generar_formato_presupuesto.py` y **regenerándolo** — **nunca** editando el `.xlsx` directo: el generador es idempotente y **sobreescribe** el archivo en cada corrida (perdería ediciones manuales). **Hacer copia de respaldo del `.xlsx` antes de regenerar.**
- **La BL se edita en el `.md`** (fuente única) y se regenera el Word con `python ~/.claude/skills/template-adasa/md_to_adasa_docx.py BL_MONTAJE_TALTAL_REV0.md`.
- Mantener los documentos en **Rev 0** (la BL sigue siendo Rev 0 borrador; aún no se distribuye).

## 9. Qué NO tocar

- Cap. 1, 2 y 3 del Formato (montaje mecánico).
- Formato visual: 6 columnas, estilos/paleta, fórmulas de totalizadores.
- Los PDF del dossier `Bases REV 0/` y los PDF de `COMENTARIOS/`, hasta que el usuario apruebe re-emitir.

## 10. Decisiones registradas (esta sesión)

- Respetar el Formato actual como base (no reinventar el formato).
- Agregar al Cap. 4: cubierta metálica estructural; impermeabilización; protección C5-M; acero de refuerzo y pernos como líneas separadas.
- No cargar cantidades en esta ronda (solo instructivo + estructura).

## 11. Procedimiento de ejecución (rondas futuras)

**Ronda B — estructura:**
1. Respaldar `Formato de Presupuesto.xlsx`.
2. En `generar_formato_presupuesto.py`, extender el Cap. 4 con las partidas de la Sección 5 (CANT vacía), respetando los helpers y el formato existentes.
3. Regenerar y verificar visualmente (6 columnas, estilos, Cap. 1-3 intactos, fórmulas).

**Ronda C — cantidades y BL:**
4. Confirmar el mapeo de códigos MC y la fuente de cada CANT (Sección 5, columna Fuente).
5. Cargar las CANT Rev B en el generador; declarar Clase 2 AACE; regenerar.
6. **Cuadrar cubicaciones** Formato ↔ Itemizados (hormigón total ≈26,5 m³, excavación ≈112,6 m³, acero ≈2.100 kg, perfiles A36 ≈1.596 kg, panel 25,2 m²).
7. Actualizar el BL `.md` (referencia a Rev B, coherencia de tags/pesos); regenerar Word; PDF al dossier solo si el usuario lo pide (Word COM + TOC).

**Checklist de cierre de cada ronda:**
- [ ] Cap. 1-3 sin cambios; formato/columnas/estilos intactos.
- [ ] Tag fosa = TK-06-004; sin pestaña "La Chimba"; Clase 2 declarada.
- [ ] Cubicaciones cuadran contra los Itemizados Rev B.
- [ ] Respaldo del `.xlsx` previo; edición hecha en el generador, no en el `.xlsx`.
- [ ] Sin referencias de sección con el símbolo de párrafo en `.md`/`.py`.
