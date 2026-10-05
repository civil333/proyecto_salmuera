# Diff del Fabrication Schedule de BW Water

> Generado por `diff_fabrication_schedule.py`. Hoja `RO system`. Solo lectura sobre los `.xlsx`.

**Versiones:** 01-Jul -> 03-Ago

Solo existen **2 versiones** de este archivo en el repositorio, de modo que la comparacion cubre el salto completo de un mes y no permite ver en que semana ocurrio cada movimiento.

## Dimensiones y ventana de calendario

| Version | Filas | Columnas | Primera fecha | Ultima fecha |
|---|---|---|---|---|
| 01-Jul | 707 | 279 | 2026-05-31 | 2026-09-12 |
| 03-Ago | 706 | 301 | 2026-05-31 | 2026-10-03 |

La grilla de calendario se extiende **+21 dias** (+22 columnas): el cronograma amplia su horizonte, lo que por si solo ya indica que el fin de obra se corrio.

## Altas y bajas de actividades

Actividades en 01-Jul: **24** | en 03-Ago: **23**

**Bajas (1):**

- `SS316 Piping Spool Fabrication` - tenia baseline - a -, 6days

## Cambio de esquema de la planilla

| Version | Columnas de datos detectadas |
|---|---|
| 01-Jul | `Days`, `Remarks`, `Baseline Start`, `Baseline Finish` |
| 03-Ago | `Progress`, `Days`, `Remarks`, `Baseline Start`, `Baseline Finish` |

Columnas **nuevas en 03-Ago**: `Progress`. Antes no existian, de modo que su contenido no tiene contraparte que comparar.

Las columnas se resuelven leyendo la fila de encabezado. Comparar por posicion habria alineado mal toda la planilla y producido un diff enteramente falso.

## Cambios por actividad

| Actividad | Campo | 01-Jul | 03-Ago | Delta |
|---|---|---|---|---|
| STRUCTURE | Days | 16days | 16 days |  |
| STRUCTURE | Remarks | start after seismic calculation approved | - |  |
| RO Skid Frame | Remarks | - | Cutting, Fit up and Welding in progress |  |
| RO Skid Frame | Baseline Start | - | 2026-08-03 | sin baseline previo |
| RO Skid Frame | Baseline Finish | - | 2026-08-10 | sin baseline previo |
| Pipe support | Days | 2 days | 3 days |  |
| Pipe support | Baseline Start | - | 2026-08-05 | sin baseline previo |
| Pipe support | Baseline Finish | - | 2026-08-08 | sin baseline previo |
| Painting | Baseline Start | - | 2026-08-11 | sin baseline previo |
| Painting | Baseline Finish | - | 2026-08-18 | sin baseline previo |
| PIPING & INSTRUMENT | Days | 21days | 24 days |  |
| PVC Piping Spool Fabrication | Days | 10days | 22 days |  |
| PVC Piping Spool Fabrication | Remarks | - | Fabrication drawing not yet issue for fabrication. |  |
| PVC Piping Spool Fabrication | Baseline Start | - | 2026-07-30 | sin baseline previo |
| PVC Piping Spool Fabrication | Baseline Finish | - | 2026-08-21 | sin baseline previo |
| Super Duplex Spool Fabrication | Days | 14days | 24 days |  |
| Super Duplex Spool Fabrication | Remarks | - | Fabrication start after PMI Test. Grinding, bevelling and fit up of the pipe spool start on 29/7/2026. |  |
| Super Duplex Spool Fabrication | Baseline Start | - | 2026-07-24 | sin baseline previo |
| Super Duplex Spool Fabrication | Baseline Finish | - | 2026-08-17 | sin baseline previo |
| Hydro testing for piping fabrication | Days | 5days | 4 days |  |
| Hydro testing for piping fabrication | Baseline Start | - | 2026-08-10 | sin baseline previo |
| Hydro testing for piping fabrication | Baseline Finish | - | 2026-08-14 | sin baseline previo |
| Chemical Cabinet | Days | 10days | 10 days |  |
| Enclosure | Baseline Start | - | 2026-08-17 | sin baseline previo |
| Enclosure | Baseline Finish | - | 2026-08-24 | sin baseline previo |
| Piping system | Baseline Start | - | 2026-08-24 | sin baseline previo |
| Piping system | Baseline Finish | - | 2026-08-26 | sin baseline previo |
| Container Fabrication | Days | 75days | 120 days |  |
| Opening Cut for Container | Days | 28days | 42 days |  |
| Opening Cut for Container | Remarks | - | Marking anchoring for structural skid |  |
| Opening Cut for Container | Baseline Start | - | 2026-06-03 | sin baseline previo |
| Opening Cut for Container | Baseline Finish | - | 2026-07-15 | sin baseline previo |
| Painting Outside container | Days | 14days | 10 days |  |
| Painting Outside container | Baseline Start | - | 2026-08-10 | sin baseline previo |
| Painting Outside container | Baseline Finish | - | 2026-08-17 | sin baseline previo |
| Cable Tray installation | Days | 7days | 7 days |  |
| Cable Tray installation | Baseline Start | - | 2026-07-30 | sin baseline previo |
| Cable Tray installation | Baseline Finish | - | 2026-08-06 | sin baseline previo |
| Cable pulling | Days | 7days | 7 days |  |
| Cable pulling | Baseline Start | - | 2026-08-01 | sin baseline previo |
| Cable pulling | Baseline Finish | - | 2026-08-08 | sin baseline previo |
| Equipment positioning inside container | Days | 6days | 10 days |  |
| Equipment positioning inside container | Baseline Start | - | 2026-08-22 | sin baseline previo |
| Equipment positioning inside container | Baseline Finish | - | 2026-09-02 | sin baseline previo |
| CSC inspection | Days | 2days | 2 days |  |
| CSC inspection | Baseline Start | - | 2026-08-25 | sin baseline previo |
| CSC inspection | Baseline Finish | - | 2026-08-26 | sin baseline previo |
| HP Pump and turbo positioning in container | Days | 2days | 2 days |  |
| HP Pump and turbo positioning in container | Baseline Start | - | 2026-09-03 | sin baseline previo |
| HP Pump and turbo positioning in container | Baseline Finish | - | 2026-09-05 | sin baseline previo |
| Dry Test | Days | 2days | 11 days |  |
| Dry Test | Remarks | Can be carry out after delivery of panel on ETD on 12/8 to penang | Can be carry out after delivery of panel on ETD on 23/8 to penang |  |
| Dry Test | Baseline Start | - | 2026-09-07 | sin baseline previo |
| Dry Test | Baseline Finish | - | 2026-09-18 | sin baseline previo |
| Ready for shipment | Days | 2days | 2 days |  |
| Ready for shipment | Baseline Start | - | 2026-09-19 | sin baseline previo |
| Ready for shipment | Baseline Finish | - | 2026-09-21 | sin baseline previo |

## Mayores deslizamientos de fecha

Ninguno.

## Cronograma vigente (03-Ago)

| Actividad | Avance | Dias | Baseline Start | Baseline Finish |
|---|---|---|---|---|
| STRUCTURE | - | 16 days | - | - |
| RO Skid Frame | 0.25 | 7 days | 2026-08-03 | 2026-08-10 |
| Pipe support | 0 | 3 days | 2026-08-05 | 2026-08-08 |
| Painting | 0 | 7 days | 2026-08-11 | 2026-08-18 |
| PIPING & INSTRUMENT | - | 24 days | - | - |
| PVC Piping Spool Fabrication | 0 | 22 days | 2026-07-30 | 2026-08-21 |
| Super Duplex Spool Fabrication | 0.1 | 24 days | 2026-07-24 | 2026-08-17 |
| Hydro testing for piping fabrication | 0 | 4 days | 2026-08-10 | 2026-08-14 |
| Chemical Cabinet | - | 10 days | - | - |
| Enclosure | 0 | 7 days | 2026-08-17 | 2026-08-24 |
| Piping system | 0 | 3 days | 2026-08-24 | 2026-08-26 |
| Container Fabrication | - | 120 days | - | - |
| Opening Cut for Container | 1 | 42 days | 2026-06-03 | 2026-07-15 |
| Painting Outside container | 0 | 10 days | 2026-08-10 | 2026-08-17 |
| Cable Tray installation | 0 | 7 days | 2026-07-30 | 2026-08-06 |
| Cable pulling | 0 | 7 days | 2026-08-01 | 2026-08-08 |
| Equipment positioning inside container | 0 | 10 days | 2026-08-22 | 2026-09-02 |
| CSC inspection | 0 | 2 days | 2026-08-25 | 2026-08-26 |
| HP Pump and turbo positioning in container | 0 | 2 days | 2026-09-03 | 2026-09-05 |
| Dry Test | 0 | 11 days | 2026-09-07 | 2026-09-18 |
| Ready for shipment | 0 | 2 days | 2026-09-19 | 2026-09-21 |

