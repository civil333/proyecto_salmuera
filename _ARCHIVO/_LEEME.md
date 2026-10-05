---
titulo: Archivos retirados de la raíz del proyecto
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# _ARCHIVO

Archivos que estaban sueltos en la raíz del proyecto y ya no se usan. Se retiraron el 5-Oct-2026 sin borrar nada.

| Archivo | Qué es | Por qué se retiró |
|---|---|---|
| `LISTADO ACTIVOS.xlsx` | Listado de activos del módulo: equipos (18 filas), válvulas (127) e instrumentos (75), al 15-Abr-2026 | Sin uso desde abril, por decisión del usuario. No está en git: esta es la única copia |
| `actualizar_listado_activos.py` | Aplicó al listado anterior los cambios del TM N14 y de Van Doorn | Ídem |
| `generar_listado_consolidado.py` | Generaba `LISTADO-CONSOLIDADO-EVI.xlsx`, que ya no existe en disco | Ídem. CLAUDE.md sección 10 lo declara archivado |
| `_INVENTARIO_PRE_HIGIENE_04AGO.json` | Inventario con md5 de los 30 archivos que se ordenaron en la limpieza del 4-Ago-2026 | Evidencia de una tarea cerrada |
| `movimientos_orden_raiz_y_programa_2026-10-05.json` | Registro archivo por archivo del orden del 5-Oct-2026 (raíz y `PROGRAMA y CONTRATO/`), con md5 de origen y destino | Traza del ordenamiento |

> **TAG erróneo en los dos scripts del listado.** `actualizar_listado_activos.py` y `generar_listado_consolidado.py` rotulan la fosa de drenajes como `TK-06-002`. El TAG correcto es `TK-06-004`; `TK-06-002` es el Estanque CIP de BW Water (CLAUDE.md sección 3.7). Si alguno se reactiva, corregirlo antes de generar.
