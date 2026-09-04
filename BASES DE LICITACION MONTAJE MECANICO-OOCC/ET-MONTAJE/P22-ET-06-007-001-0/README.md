# P22-ET-06-007-001-0 — Especificación Técnica de Montaje Electromecánico

Documento técnico que define el "cómo se monta" del Estanque de Salmuera TK-06-001 (PRFV, 10 m³) y la Bomba de Alimentación BH-06-001 (KSB centrífuga + motor WEH 11 kW). Se emite como Anexo Técnico del paquete de Bases de Licitación de Montaje Mecánico / OOCC del proyecto Taltal.

## Fecha de emisión

27-May-2026 — Revisión 0.

## Contenido de esta carpeta

| Archivo | Descripción |
|---|---|
| `P22-ET-06-007-001-0_MONTAJE-ELECTROMECANICO.md` | Fuente Markdown del documento (10 capítulos + Anexos) |
| `crear_et_montaje.py` | Script generador del DOCX (importa template-adasa v7.4) |
| `generar_figuras.py` | Script PyMuPDF + matplotlib que renderiza los 9 PNG de figuras + 3 PNG de anexos |
| `figuras/` | PNG embebidos en el cuerpo (figuras 4.1 a 8.1) y en los anexos (anexo-A/B/C-p01.png) |
| `anexos/` | PDFs originales de los planos (copia de respaldo, sin modificar) |
| `P22-ET-06-007-001-0_MONTAJE-ELECTROMECANICO_ADASA.docx` | Documento Word generado |

## Estructura del documento

1. Generalidades (introducción, objeto, definiciones, documentos de referencia, normativa, jerarquía contractual).
2. Suministros y Aportes (ADASA, Contratista, equipos con calibración vigente).
3. Recepción y Almacenamiento de Equipos (inspección, almacenamiento, manipulación e izaje).
4. Bases de Hormigón y Anclajes (verificación topográfica, pernos estanque, pernos bomba, tolerancias).
5. Montaje del Estanque de Salmuera TK-06-001 (características, procedimiento completo, hidrostática).
6. Montaje de la Bomba de Alimentación BH-06-001 (baseplate, nivelación API 610, grout 25 mm, alineamiento láser por RPM, apriete, bridas).
7. Pruebas Eléctricas del Motor (devanado, aislación, índice de polarización, Hipot, sentido de rotación).
8. Protocolos y Documentación Entregable (matriz de protocolos, ITP, dossier as-built).
9. Seguridad y Medio Ambiente (HSE general, altura, izaje, espacio confinado, pruebas eléctricas, residuos).
10. Hitos y Punch List Final (H1 a H11, criterios de cierre).

Anexos A–D al final del DOCX, en orientación apaisada:
- A — Plano de Montaje del Conjunto (P22-DWG-06-005-101-0).
- B — Plano del Estanque (EX-26005-F01).
- C — Plano de la Bomba KSB (KSB-AAF-KNCPP11-050+160M).
- D — Formatos de Protocolos en blanco (entrega aparte en formato editable).

## Cómo regenerar el DOCX

```bash
cd "BASES DE LICITACION MONTAJE MECANICO-OOCC/ET-MONTAJE/P22-ET-06-007-001-0/"
python3 generar_figuras.py     # regenera figuras + recortes + páginas de anexos
python3 crear_et_montaje.py    # regenera el DOCX
```

## Fuentes de referencia metodológica

- P04-ET-00-005-105 Rev 0 (ET Montaje Electromecánico PDA — 22 capítulos, planta desaladora completa) — estructura, normativa (API 610 / ISO 13709, ASME, AWS), tolerancias de alineamiento por RPM, capítulo 22 Pruebas Estáticas Motores.
- Especificación Técnica Montaje Bombas Tocopilla Rev 0 — disciplina ejecutiva: protocolos, punch list, grout Sikagrout 214 en 25 mm.
- P22-IT-06-000-005-0 Rev 0 (Análisis sísmico TK-06-001) — torques de anclaje sísmico.
- Hojas de datos P22-ET-06-005-001 (HD bomba) y P22-ET-06-005-002 (HD tanque) — citadas como referencia funcional, no embebidas como anexo.
