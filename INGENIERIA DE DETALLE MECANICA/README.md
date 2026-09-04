# INGENIERIA DE DETALLE MECANICA

**Proyecto:** Módulo de Salmuera Taltal — P22
**Responsable ingeniería de detalle:** Van Doorn (contrato trato directo)
**Fecha última actualización:** 2026-02-28

---

## Propósito de la Carpeta

Contiene los documentos de ingeniería de detalle mecánica para:

1. **Infraestructura exterior de soporte del módulo** — estanque, bombas, válvulas y conexiones externas al módulo BW Water.
2. **Tie-in / interconexión con la infraestructura existente** en Taltal — conexión de la segunda etapa de salmuera con los sistemas existentes de la planta.

Esta carpeta es complementaria a los documentos del módulo BW Water (revisados en `REVISIONES/`). Aquí se gestiona la ingeniería **ADASA** del entorno exterior.

---

## Equipos Principales

| Equipo | Modelo / Referencia | Subcarpeta |
|--------|--------------------|-----------:|
| Bomba sumergible | KSB Amarex KRT F 065-215/4 4 S | `PLANOS BOMBA SUMERGIBLE/` |
| Bomba de alimentación | Ver datasheet CV406762-REV02 | `PLANO BOMBA ALIMENTACION/` |
| Válvulas mariposa | KSB ISORIA 10 — Oferta CV421060 Rev1 | `PLANOS VALVULAS/` |
| Estanque | AA-TalTal (plano 2026 0109-Vs01) | `PLANOS ESTANQUE/` |

---

## Documentos Formales P22 — Entrega 1

Entregados mediante **Nota de Envío N°1** (en subcarpeta `ENTREGAS/ENTREGA 1/`).

| Código | Título | Rev | Formato | Estado |
|--------|--------|-----|---------|--------|
| P22-DWG-06-009-101-B | PFD Módulo Segunda Etapa Salmuera | B | DWG | En revisión |
| P22-DWG-06-009-102-B | P&ID Alimentación Módulo 2da. Etapa Salmuera | B | DWG | En revisión |
| P22-IT-06-008-101-B | Lógica de Control | B | DOCX | **Bajo revisión — Rev C requerida** |
| P22-LI-06-000-101-B | Lista de Entregables | B | XLSX | En revisión |

### Estado Lógica de Control — P22-IT-06-008-101-B

> **Rev B bajo revisión formal desde 28-Feb-2026.**
>
> ADASA realizó revisión comparativa contra P13-IT-03-008-001-0 (Módulo 3, 2019) que fue el
> documento con el que se programó y comisionó exitosamente ese módulo. Se identificaron 7 gaps.
>
> **Gaps Mayor:** GAP-01 (secuencia de marcha incompleta), GAP-02 (secuencia de parada incompleta + error de tag BH-03 → BH-06).
>
> **Acción:** Consulta Técnica P22-CT-06-000-001-0 emitida a Van Doorn solicitando Rev C.
> Rev C requerida antes de que BW Water inicie la programación del PLC.
>
> **Documentos de soporte:**
> - `REVISIONES/EVALUACIONES/P22-IT-06-000-004-0_Evaluacion-Logica-Control_ADASA.docx` — evaluación interna ADASA
> - `REVISIONES/CONSULTAS_TECNICAS/P22-CT-06-000-001-0_Logica-Control-Gaps_ADASA.docx` — consulta formal a Van Doorn

---

## Documentos Técnicos por Subcarpeta

### PLANO BOMBA ALIMENTACION/

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| CV406762-REV02.pdf | Datasheet bomba de alimentación (5.7 MB) | PDF |
| GENERALARRANGEMENT (1).dwg | General Arrangement bomba alimentación | DWG |

### PLANOS BOMBA SUMERGIBLE/

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| Amarex KRT F 065-215_4 4 S Installation_front.dwg | Plano instalación — vista frontal | DWG |
| Amarex KRT F 065-215_4 4 S Installation_top.dwg | Plano instalación — vista superior | DWG |
| Amarex KRT F 065-215_4 4 S Installation_right.dwg | Plano instalación — vista lateral derecha | DWG |
| amarex krt f 065-215_4 4 s installation.rfa | Modelo BIM Revit 2021 | RFA |
| KSB_AmarexKRTF06521544SInstallation (1).zip | Paquete completo de instalación KSB | ZIP |

### PLANOS ESTANQUE/

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| 2026 0109-Vs01 AA-TalTal.pdf | Plano estanque AA-TalTal (94.2 KB) | PDF |
| FORMULARIO PROPUESTA TRATO DIRECTO.xlsx | Formulario cotización estanque | XLSX |

### PLANOS VALVULAS/

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| Oferta KSB CV421060 Rev1.pdf | Oferta válvulas KSB (3.8 MB) | PDF |
| MS_MC.PDF | Especificación técnica válvulas (4.3 MB) | PDF |
| ISORIA 10 844.1_11-30 folleto de la serie.pdf | Catálogo ISORIA 10 — válvulas mariposa | PDF |
| DWG-1206D-RV01.pdf | Plano dimensionado válvulas | PDF |
| ALS200 - C230.pdf | Datasheet actuador válvulas | PDF |
| RE CV421060 RE solicitud cotización 80598.msg | Email cotización válvulas | MSG |

---

## Contratos y Órdenes de Compra

| Documento | Descripción | Formato |
|-----------|-------------|---------|
| OC-834350.pdf | Orden de compra (85.8 KB) | PDF |
| Trato directo VANDOORN (...).xlsx | Contrato Van Doorn — ingeniería de detalle | XLSX |

### Propuestas Técnicas (Raíz)

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| Propuesta Tratamiento de Salmuera rev 0.pdf | Propuesta inicial (1.1 MB) | PDF |
| Propuesta Tratamiento de Salmuera rev 1.pdf | Propuesta revisada — vigente (1.1 MB) | PDF |

---

## Formatos Disponibles

| Formato | Herramienta requerida |
|---------|-----------------------|
| DWG | AutoCAD / DraftSight |
| RFA | Autodesk Revit 2021+ |
| PDF | Visor PDF estándar |
| XLSX | Excel / Google Sheets |
| DOCX | Word |
| MSG | Outlook |

---

## Notas

- Los archivos DWG y RFA contienen la geometría completa para fabricación e instalación.
- El modelo Revit (`.rfa`) de la bomba sumergible Amarex permite coordinación BIM.
- No existen archivos `.md` con contenido extraído en esta carpeta — para análisis técnico usar la skill `large-pdf-reader` sobre los PDFs relevantes.
- Van Doorn es asesor **interno de ADASA** — sus documentos no se envían directamente a BW Water (ver Regla Van Doorn en CLAUDE.md §3.9).
