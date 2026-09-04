---
titulo: Modelo 3D Rev A — cruce de TAG contra los listados aprobados
codigo: E70-MODELO-CRUCE
fecha: 2026-08-05
estado: INTERNO — insumo de la subsección 2.5 del TM N30
second_brain: skip
---

# Modelo 3D `P22-DWG-09-005-007` Rev A — cruce contra los listados aprobados

> Reemplaza la revisión anterior del modelo. Aquella objetaba rigor BIM —propiedades de publicación, conjuntos de selección, viewpoints, objetos tipados— y **la ET no da base para exigir nada de eso**. Lo que sí es exigible, y es más fuerte, es que los TAG del modelo coincidan con los listados aprobados: tres de los cuatro están en Código 1.

## De dónde salen los datos

Los TAG **no se leyeron de los nombres de capa**. Se leyeron de la categoría `AutoCAD` de AutoCAD Plant 3D, en las propiedades de cada objeto, extraídas con un plugin in-process de Navisworks Manage: **3.435 objetos** con esa categoría, **161.699 filas** de propiedad volcadas.

| Qué | Propiedad del objeto |
|---|---|
| Líneas | `Line Number` |
| Equipos, válvulas e instrumentos | `Tag` |
| Tipo de elemento | `Class` |

**El modelo sí trae objetos tipados.** `Class` declara `Valve` en 81 TAG distintos, `InlineInstrument` en 19, `Vessel`, `Tank`, `Filter`, `Pump`, `GlobalEquipment` y `MixingEquipment`. La afirmación anterior de que solo había sólidos genéricos en capas era falsa y se retira, igual que la de que ninguna válvula estaba identificada.

## Cómo se leyó cada listado

Elegir mal la fuente produce un falso hallazgo masivo, así que cada listado se leyó por donde se lee bien:

| Listado | Rev | Veredicto | Fuente | TAG |
|---|---|---|---|---|
| Equipment List `P22-LI-09-005-001` | B | 2-AN (TM N11) | `.md`, TAG partido en celdas | 12 |
| Valve List `P22-LI-09-005-002` | D | **1-Approved** (TM N18) | **PDF** | **111** |
| Instrument List `P22-LI-09-008-003` | E | **1-Approved** (TM N20) | `.md`, TAG partido en celdas | 38 |
| Line List `P22-LI-09-009-003` | 0 | **1-Approved** (TM N29) | PDF | 34 |

Los 111 de la Valve List coinciden exactamente con los "111 items" que declara su propia hoja de respuesta a comentarios de la Rev D. Es la comprobación de que el parseo es correcto.

> **Defecto de datos interno, no del proveedor:** el `.md` almacenado de la Valve List Rev D **está corrupto**. Devuelve `VVVMMM---000999---` porque el PDF trae la capa de texto repetida y la extracción guardada la interleavó. Leído del PDF sale limpio. Cualquier análisis previo que haya usado ese `.md` está comprometido. En la Equipment List y la Instrument List pasa lo contrario: el PDF entrega el TAG partido en columnas y solo el `.md` conserva la estructura de celdas que permite recomponerlo.

---

## Resultado del cruce

### Líneas — `Line Number` contra Line List Rev 0

Modelo **35** · Line List **34** · coinciden **29**.

**En el modelo y no en la Line List aprobada (6):**
`AS-PVC-DN100-09-026` · `AS-PVC-DN25-09-033` · `CP-PVC-DN80-09-042` · `CP-SSD-DN100-09-015` · `CP-SSD-DN65-09-044` · `RD-PVC-DN15-09-001`

**En la Line List y sin aparecer en el modelo (5):**
`CP-PVC-DN100-09-026` · `CP-PVC-DN50-09-042` · `CP-SSD-DN80-09-015` · `CP-SSD-DN80-09-044` · `DA-PVC-DN65-09-016`

Tres pares delatan un mismo correlativo con atributo distinto, que es lo que hay que reconciliar:

| Correlativo | Line List aprobada | Modelo |
|---|---|---|
| 09-042 | `CP-PVC-**DN50**-09-042` | `CP-PVC-**DN80**-09-042` |
| 09-015 | `CP-SSD-**DN80**-09-015` | `CP-SSD-**DN100**-09-015` |
| 09-044 | `CP-SSD-**DN80**-09-044` | `CP-SSD-**DN65**-09-044` |
| 09-026 | `**CP**-PVC-DN100-09-026` | `**AS**-PVC-DN100-09-026` |

**Colisión de correlativo dentro del modelo (1):** el número `09-001` lo usan `DA-PVC-DN100-09-001` y `RD-PVC-DN15-09-001`. La Line List aprobada no tiene ninguna colisión, y `RD-PVC-DN15-09-001` tampoco figura en ella.

### Equipos — `Tag` contra Equipment List Rev B

Modelo **8** · Equipment List **12** · coinciden **7**.

- **`BOI-09-006`** está en el modelo y no en la Equipment List Rev B.
- La bomba de alta presión aparece como **`BH-009-002`**, con tres dígitos en el segmento de área. El listado la declara `BH-09-002`.
- Los recipientes RO se modelan con sufijo de posición —`BOI-09-001-1` a `-5` y `BOI-09-002-1` a `-4`— mientras el listado declara `BOI-09-001` y `BOI-09-002`. No es un error de identidad, pero el TAG del modelo no es el del listado.

### Válvulas — `Class = Valve` contra Valve List Rev D

Modelo **81** · Valve List **111** · coinciden **77**.

- **En el modelo y no en la Valve List:** `VM-09-131`, `VM-09-132`, `VM-09-133` y `VRP-09-001`.
- Una válvula lleva el TAG **`VM-09-094?`**, con un signo de interrogación pegado. `VM-09-094` sí existe en la lista.
- 34 válvulas de la lista no aparecen con TAG en el modelo.

### Instrumentos — `Class = InlineInstrument` contra Instrument List Rev E

Modelo **19** · Instrument List **38** · coinciden **17**.

- **`DPS-09-002` en el modelo**, cuando la Instrument List Rev E declara **`DPS-09-001`** — y el datasheet que viene en esta misma entrega, `P22-LI-09-008-006` Rev B, lleva `Component Tag No./s: DPS-09-001`. El modelo contradice al listado y al datasheet del mismo submittal.
- `PI-09-006` está en el modelo y no en la lista.
- 21 instrumentos de la lista no aparecen con TAG en el modelo, entre ellos los analizadores `CIT`, `ORPIT` y `PHIT`, los elementos de temperatura `TE`, los switches de nivel `LS` y los transmisores de vibración `VT`.

### Objetos sin identificar

**57 objetos llevan `Tag` con el valor literal `?`.**

---

## Qué se emite y qué no

**Se emite:**

1. **El archivo no se identifica como `P22-DWG-09-005-007` Rev A.** Es el comentario principal. El título interno del documento es `V14 Taltal.nwd` y su ruta de origen es la carpeta personal de un usuario. Un entregable sometido para aprobación tiene que llevar su código y su revisión, y se pide que lo remitan así en la emisión final.
2. **TAG malformados o sin resolver:** `BH-009-002`, `VM-09-094?` y los 57 objetos con `Tag = ?`.
3. **TAG que contradicen un listado aprobado:** `DPS-09-002` contra `DPS-09-001`, los tres pares de diámetro y el par de servicio de las líneas, `BOI-09-006`, y las cuatro válvulas fuera de la Valve List.
4. **Colisión del correlativo 09-001** entre `DA-PVC-DN100-09-001` y `RD-PVC-DN15-09-001`, más la ausencia de esta última en la Line List.

**No se emite:**

- Nada sobre propiedades de publicación, conjuntos de selección, viewpoints ni estructura de disciplinas: **la ET no lo exige**.
- Nada fundado en que un TAG del listado **no aparezca** en el modelo. Esa ausencia admite explicación legítima —alcance de modelado, elementos de skid no representados— y no hay requisito que fije qué debe estar modelado. Los conteos quedan registrados aquí como contexto, no como observación.
