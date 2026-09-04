# P22-ET-06-007-002-0 — Especificación Técnica de Montaje de Cañerías HDPE

Documento técnico que define los procedimientos de montaje en obra de las cañerías HDPE PE100 SDR17 PN10 aéreas del Área 06 del proyecto Modulo de Salmuera Taltal, incluida la instalación en línea de las válvulas e instrumentos in-line aportados por ADASA. Se emite como Anexo Técnico del paquete de Bases de Licitación de Montaje Mecánico / OOCC.

## Fecha de emisión

27-May-2026 — Revisión 0 (Rev 0 inicial el 27-May; correcciones Rev2 aplicadas el mismo día).

## Alcance del sistema

- Tubería HDPE PE100 SDR17 PN10: 335 m totales (DN100 180 m + DN80 151 m + DN150 3 m + DN50 1 m).
- Accesorios HDPE: 75 codos 90°, 17 codos 45°, 5 tees, 66 manguitos EF, 7 reducciones, 46 bridas lap joint + 47 stub ends, 3 saddles.
- Pernería: 224 espárragos inoxidables Gr.B8M Cl.2 (SS316).
- Juntas planas NBR/SBR 1/8" ASME B16.21: 45 unidades.
- 100% uniones por electrofusión (sin butt fusion, sin PVC-U).

## Aportes ADASA vs Contratista (alineado con BL_MONTAJE_TALTAL §3.3 y §3.4)

**ADASA aporta** (entrega en bodega contra acta firmada): 13 válvulas mariposa KSB ISORIA 10 + 2 check duplex (VR-06-001, VR-06-003) + 7 instrumentos in-line (LSH, LSL, LIT, PI, PIT, FIT) + soportes fabricados SP-01 a SP-11 + planos isométricos y LI.

**El Contratista aporta** (regulado por la ET de Fabricación P22-ET-06-006-001-0): TODA la tubería HDPE, accesorios EF, bridas lap joint, stub ends, pernería inoxidable B8M y juntas NBR/SBR.

## Contenido de esta carpeta

| Archivo | Descripción |
|---|---|
| `P22-ET-06-007-002-0_MONTAJE-CANERIAS-HDPE.md` | Fuente Markdown del documento (14 capítulos + Anexos) |
| `crear_et_montaje_canerias.py` | Script generador del DOCX (importa template-adasa v7.4) |
| `generar_figuras.py` | Script matplotlib que produce los 8 PNG de figuras conceptuales |
| `figuras/` | PNG embebidos en el cuerpo (8 figuras) |
| `anexos/` | Anexo A — Listado de Materiales (xlsx) |
| `P22-ET-06-007-002-0_MONTAJE-CANERIAS-HDPE_ADASA.docx` | Documento Word generado |

## Estructura del documento (14 capítulos)

1. Generalidades (introducción, alcance, documentos de referencia, normativa, jerarquía contractual).
2. Suministros y Aportes (ADASA aporta válvulas + instrumentos + soportes; Contratista aporta todo el material de cañería).
3. Recepción, Almacenamiento y Manipulación.
4. Procedimientos de Fusión: WPS, PQR y Calificación de Operadores (ISO 12176-3/4, Fusion Log).
5. Procedimientos Constructivos por Tipo de Unión (solo electrofusión + bridas con stub end electrofundido).
6. Soportería, Anclajes y Dilatación Térmica (HDPE).
7. Tendido y Montaje en Obra.
8. Instalación de Válvulas e Instrumentos In-Line (aportes ADASA, partidas A9.3 y A9.4).
9. Identificación y Marcado en Obra (sin pintar el HDPE — anillos prefabricados y etiquetas autoadhesivas con flechas direccionales en RAL corporativo ADASA, 3 servicios reales: SA Salmuera, PE Permeado, DR Drenaje).
10. Pruebas Hidrostáticas conforme ASTM F2164.
11. Limpieza, Flushing y Puesta en Servicio Inicial.
12. Protocolos y Documentación Entregable (Fusion Log).
13. Seguridad y Medio Ambiente.
14. Hitos y Punch List Final.

Anexos: A — LI Materiales (xlsx) · B — Cuadernillo de Isometrías (referencia externa) · C — Formatos de Protocolos en blanco.

## Cambios respecto a la versión preliminar

- Aportes ADASA corregidos: ya no incluye tubería HDPE (eran error contractual; toda la cañería es aporte del Contratista).
- Butt fusion eliminado completamente: las isométricas confirman 100% electrofusión.
- PVC-U eliminado del alcance: el proyecto Taltal es 100% HDPE.
- Capítulo nuevo "Instalación de Válvulas e Instrumentos In-Line" para cubrir la integración de los aportes ADASA al sistema HDPE.

## Cómo regenerar el DOCX

```bash
cd "BASES DE LICITACION MONTAJE MECANICO-OOCC/ET-MONTAJE-HDPE/P22-ET-06-007-002-0/"
python3 generar_figuras.py          # regenera las 8 figuras conceptuales
python3 crear_et_montaje_canerias.py # regenera el DOCX
```

## Fuentes de referencia metodológica

- P04-ET-00-006-102 Rev 0 (ET Fabricación y Montaje de Cañerías PDA Antofagasta) — estructura, criterios de flushing, código de colores RAL corporativo ADASA.
- P22-ET-06-006-001-0 (ET Cañerías Taltal — Fabricación) — material, grado, presión nominal, servicios; jerárquicamente superior a esta ET en lo relativo a fabricación.
- P22-LI-06-006-102-0 (Listado de Materiales) — fuente cuantitativa al 100 %.
- BL_MONTAJE_TALTAL_REV0.md §3.3 y §3.4 — distribución exacta de aportes ADASA vs Contratista.
