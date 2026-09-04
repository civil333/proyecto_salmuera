---
titulo: Ledger de cierre de comentarios — ENTREGA 83 (submittal 25007-0083)
fecha: 2026-08-26
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 83

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0083`, emitido el viernes 21-Ago-2026, devolucion pedida el lunes 24-Ago-2026, plazo real de la Clausula 37.2 el martes 1-Sep-2026. Dos documentos: Piping Layout Rev D y 3D Model Rev B.

**Regla de alcance aplicada.** Los dos venian de Codigo 2 en el TM N30. Se verifica unicamente si las condiciones que ese transmittal fijo estan incorporadas. No se abren frentes nuevos.

---

## 1. Piping Layout Rev D — `P22-DWG-09-005-004`

Cinco paginas: portada, tres laminas (overall, secciones, seccion CIP) y hoja de comentarios. **El conjunto de once planos de taller que la Rev C traia embebido en diecisiete paginas ya no viene**: la Rev C tenia 22 paginas, la Rev D tiene 5.

### Hoja de comentarios: lo que transcribe y lo que omite

La hoja consolidada tiene tres filas. La fila de la Rev C dice, literal y completa:

> **Comment from Client:** "1. Tie-in point details to be added in the drawing."
>
> **Reply from BW:** "1. Tie-in point details added."

**El TM N30 emitio cinco identificadores sobre este plano** (OBS-02, OBS-03 y NOTE-01 a NOTE-03), agrupados en tres condiciones. La hoja transcribe **una** de las tres. Las otras dos no aparecen en la columna del cliente, de modo que quien revise la hoja no puede saber que se pidio.

### Cierre punto por punto

| Punto del TM N30 | Pedido, literal | Declarado en la hoja | Verificado en la Rev D | Estado |
|---|---|---|---|---|
| (a) Tabla de tie-in | "add a tie-in schedule listing, for every battery-limit connection, the line tag, nominal diameter, connection type and elevation referred to a datum declared on the drawing, **covering the permeate and CIP supply and return lines**" | "Tie-in point details added" | Tabla de 5 filas en la lamina 1: `NO / TAG (PID) / PROCESS / diametro / FLANGE # / FLANGE STD / ELEVATION`. Cubre antiscalante, alimentacion, permeado y dos de concentrado. **Ninguna linea de CIP figura**, pese a que la lamina rotula siete: `CP-PVC-DN80-09-019` (make-up), `CP-PVC-DN100-09-021` (retorno), `CP-PVC-DN150-09-022` (a bomba CIP), `CP-PVC-DN100-09-023` (desde bomba CIP), `CP-PVC-DN100-09-024` (alimentacion CIP), `CP-PVC-DN100-09-025` (recirculacion) y `CP-PVC-DN100-09-026` (a drenaje). Las cotas de elevacion (1680, 2597, 2947, 2947 y 2940 mm) **no declaran el datum**: los tres bloques `NOTES` de las tres laminas estan vacios | **Cierre parcial** |
| (b) Clase de brida | "annotate the flange class against the **CIP and antiscalant** battery-limit terminations consistent with the approved Line List" | no transcrito | La fila 1, `TP-AS P11-001` ANTISCALANT 1 pulgada, trae **guion** en `FLANGE #` y en `FLANGE STD`. Las terminaciones de CIP no estan en la tabla. Contradice la propia respuesta de BW Water del ciclo anterior: "The AS injection line connects to the static mixer using a flanged joint" | **No cerrado** |
| (c) Tableros locales | "state whether the module carries **one or two** local control panels, tagging each enclosure consistently with the approved Local Control Panel datasheet and the Single Line Diagram" | no transcrito | La lamina 1 rotula **dos** envolventes con la misma palabra `LCP`, una junto a la puerta de acceso de equipos y otra junto al area de dosificacion. Ninguna lleva TAG. Ningun bloque de notas lo declara. Verificado por render: `render/piping_D_p2.png` | **No cerrado** |

### Aparte: el conjunto de planos de taller

**No es condicion del Codigo 2 de este plano.** El pedido vive en la subseccion 2.4 del TM N30, que devolvio el conjunto **as not received**, sin asignarle codigo de respuesta, con identificadores propios (OBS-01, OBS-04, OBS-05 y OBS-06) sobre otro PDF anotado. Se registra aqui porque el vehiculo que lo traia era este archivo.

| Pedido, literal | Verificado | Estado |
|---|---|---|
| "either remove the shop fabrication set from P22-DWG-09-005-004 and submit it as a separate deliverable with its own ADASA code and revision index, or extend the cover sheet and the Submittal Form to declare it" | **Removido** del archivo. **Nunca reemitido** como entregable propio: no aparece en las submittals 0082 a 0085. Los dos hallazgos de contencion de presion que el TM N30 emitio sobre ese conjunto (conexiones roscadas austeniticas en super duplex y quiebre de especificacion sin declarar) siguen sin respuesta | Separacion resuelta; **el conjunto y sus dos hallazgos siguen abiertos**, y van a la Seccion 3 |

### Fuera de alcance (no se emite)

- La portada declara `Page: 1 of 2` y el archivo trae cinco paginas. Es el mismo defecto de conteo de la Rev C, que declaraba `Page 1 of 4` sobre 22 paginas. **Housekeeping documental: no degrada por si solo y no se emite.**
- La columna `TAG (PID)` de la tabla de tie-in usa identificadores de punto de conexion (`TP-AS P11-001`, `TP-DA P8-001`) y no los TAG de linea de la Line List aprobada. El TM N30 pidio "the line tag". Se computa dentro del cierre parcial de (a), no como punto nuevo.

---

## 2. 3D Model Rev B — `P22-DWG-09-005-007`

Archivo `P22-DWG-09-005-007.nwd`, 9,58 MB, mas el `.dwg` fuente de 168 MB. Verificado con el puente de automatizacion Navisworks (`revisar_modelo_nwd.ps1`, adaptado a Navisworks Manage 2027), volcado en `md/P22-DWG-09-005-007_3D-Model_RevB_extraccion.md` y `..._propiedades.csv`. **Todas las cifras de objetos de este ledger son de objetos unicos, no de filas del volcado**: 9.155 objetos en la Rev B contra 7.486 en la Rev A. Contraste contra el volcado del Rev A en `../ENTREGA 70/25007-0070/md/`.

**Trae hoja de comentarios propia**, `CCS - 3D Model.pdf`, que transcribe los dos comentarios de reconciliacion del TM N30 y responde con nueve items. **No transcribe el primer punto del TM N30**, el de identificacion del archivo por codigo y revision: no aparece ni en la columna del cliente ni en la respuesta.

### Cierre punto por punto

| Punto del TM N30 | Declarado en la hoja | Verificado en el modelo | Estado |
|---|---|---|---|
| Identificar el archivo por su codigo de documento **y su indice de revision en las propiedades del documento** | no responde este punto | El **nombre de archivo** ya es `P22-DWG-09-005-007.nwd`, contra el `V14 Taltal.nwd` de la Rev A. Pero las propiedades de publicacion del NWD siguen declarando **Titulo: `V16 TALTAL`**, autor `A.I.A`, publicado el 10-Ago-2026 para `BWWMY`. **No hay indice de revision en ninguna propiedad**, aunque el Submittal Form declara Rev B | **Cierre parcial** |
| Corregir `BH-009-002`, con tres digitos en el segmento de area | "BH-009-002 corrected to BH-09-002" | Cero ocurrencias de `BH-009-002`; el TAG `BH-09-002` esta presente y bien formado | **Cerrado** |
| Corregir `VM-09-094`, con signo de interrogacion al final | incluido en el item 1 | Objeto 5305: propiedad `AutoCAD / Tag` = `VM-09-094`, sin sufijo. **Cerraron los siete** TAG de valvula que llevaban interrogacion al final en la Rev A: `VM-09-076`, `-094`, `-095`, `-101`, `-102`, `-107` y `-117`, contra el unico que el TM N30 nombro | **Cerrado, con creces** |
| Resolver los **cincuenta y siete objetos** cuya propiedad TAG es un signo de interrogacion | "fifty-seven objects tags corrected with the question marks removed" | **La declaracion confunde dos puntos distintos.** Lo que corrigieron fueron los siete TAG de valvula del punto anterior. Los cincuenta y siete objetos con la propiedad TAG puesta en un signo de interrogacion son de tipo `ACPPSUPPORT`, soportes de caneria, **ninguno se toco y ahora son setenta y dos**: ningun soporte del modelo lleva TAG, ni en la Rev A ni en la Rev B. Nota de alcance: los soportes no figuran en ninguna lista aprobada, de modo que el punto vive del pedido del TM N30 que BW Water acepto y no de un requisito de la especificacion | **Declarado cerrado sin estarlo** |
| Reconciliar `DPS-09-002` contra `DPS-09-001` de la Instrument List Rev E | "DPS-09-002 corrected to DPS-09-001" | Una sola ocurrencia, `DPS-09-001` | **Cerrado** |
| Reconciliar `BOI-09-006`, ausente de la Equipment List aprobada | "BOI-09-006 corrected to BOI-09-001-6, where the equipment list will be resubmitted to align with the 3D model" | `BOI-09-006` ya no existe; aparece `BOI-09-001-6` | **Cerrado en el modelo; la reemision de la Equipment List es entregable cross-document — Seccion 3** |
| Reconciliar `VM-09-131`, `VM-09-132`, `VM-09-133` y `VRP-09-001`, ausentes de las listas aprobadas | "will be added in the valve list and resubmitted" | Los cuatro siguen en el modelo | **Entregable cross-document: reemision de la Valve List — Seccion 3.** No degrada al modelo |
| Reconciliar los recipientes RO, modelados `BOI-09-001-1` a `-5` y `BOI-09-002-1` a `-4` donde la Equipment List declara `BOI-09-001` y `BOI-09-002` | **la hoja no responde este punto** | El desglose persiste y ahora llega hasta `BOI-09-001-6` | **Entregable cross-document: reemision de la Equipment List — Seccion 3** |
| Linea `09-042`: DN80 en el modelo contra DN50 en la Line List | "corrected to DN50" | `CP-PVC-DN80-09-042` paso de nueve objetos a cero, y `CP-PVC-DN50-09-042` de cero a trece | **Cerrado** |
| Linea `09-015`: DN100 contra DN80 | "corrected to DN80" | Coexisten **`CP-SSD-DN100-09-015` (tres objetos)** y `CP-SSD-DN80-09-015` (diecinueve). En la Rev A eran veintiuno y diecinueve. Se corrigio casi todo y quedaron tres objetos en el diametro equivocado | **Cierre parcial** |
| Linea `09-044`: DN65 contra DN80 | "corrected to DN80" | `CP-SSD-DN65-09-044` paso de treinta y tres objetos a cero; queda `CP-SSD-DN80-09-044` con treinta y cinco | **Cerrado** |
| Linea `09-026`: servicio antiscalante contra CIP | "corrected to CIP" | `AS-PVC-DN100-09-026` paso de veintiseis objetos a cero; queda `CP-PVC-DN100-09-026` con veintisiete | **Cerrado** |
| Colision del correlativo `09-001` entre `DA-PVC-DN100-09-001` y `RD-PVC-DN15-09-001`, este ultimo ausente de la Line List | "RD-PVC-DN15-09-001 **will be** renamed to RD-PVC-DN25-09-046 and added into the line list which will be resubmitted" | `RD-PVC-DN25-09-046` **no existe** en el modelo. `RD-PVC-DN15-09-001` sigue, y crecio de **123 a 133 objetos**, coexistiendo con los **90** de `DA-PVC-DN100-09-001`. La colision persiste. El Piping Layout Rev D del mismo submittal rotula la misma linea en sus **tres** laminas | **No cerrado.** La respuesta esta en futuro y el cambio no se ejecuto |

### Fuera de alcance (no se emite)

- `VM-09-130` aparece en el modelo y no fue nombrada por el TM N30. Observacion nueva: **no se emite.**
- La Rev B introduce **diez valvulas nuevas con el TAG `?-?-?`**, inexistentes en la Rev A. Con ellas el universo de objetos sin identificar pasa de 64 a 82. Observacion nueva: **no se emite.**
- El modelo no declara conjuntos de seleccion y su unico viewpoint es "Vista 3D". La especificacion no lo exige; observacion refutable. **No se emite.**
- La ruta del archivo original apunta a `C:\Users\Ahmad Iqbal Azam\OneDrive - BW Water\...`. Dato de trazabilidad, sin requisito que lo sostenga. **No se emite.**

---

## Sintesis para la disposicion

**Piping Layout Rev D.** De tres condiciones de un Codigo 2, una cerro parcialmente y dos no cerraron, tras un ciclo completo de revision. La hoja de comentarios solo transcribe una de las tres.

**3D Model Rev B.** De trece puntos verificables, **seis cerraron**, **dos cerraron parcialmente** (la identificacion y la linea `09-015`), **uno se declaro cerrado sin estarlo** (los TAG de los soportes), **uno no cerro** (la colision del correlativo `09-001`) y **tres son entregables sobre otros documentos** que van a la Seccion 3. El punto declarado y no ejecutado es el de los soportes sin TAG, que empeoro de 57 a 72.
