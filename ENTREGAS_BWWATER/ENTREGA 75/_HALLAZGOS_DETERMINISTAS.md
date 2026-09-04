---
titulo: ENTREGA 75 — hallazgos verificados que NO se emiten
codigo: submittal 25007-0075
fecha: 2026-08-12
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# ENTREGA 75 — lo verificado que queda fuera del transmittal

Todo lo de abajo está comprobado contra el documento y su fuente. No se emite, y cada bloque dice por qué. Sirve para no repetir el modo de falla y para tener trazabilidad si el defecto reaparece en el dossier o en terreno.

## Regla que gobierna el filtro

Los cuatro documentos re-emitidos venían de un Código 2 y ya están emitidos para construcción. Se juzgan solo por si se incorporó lo que era condición de esa aprobación. Levantar hallazgos nuevos sobre ellos reabre una aprobación propia de ADASA y le entrega al proveedor la réplica de que el documento ya había sido aceptado. Que el defecto sea cierto y esté verificado no lo hace emitible.

Los tres procedimientos de ensayos no destructivos son primera emisión, así que **no les aplica este filtro**: ahí lo que decide qué se emite es si hay un requisito que sostenga la observación, no su antigüedad.

---

## HP and LP Pressure Test Procedure `P22-BA-09-000-010` Rev 0

Las tres regresiones que entraron en la Rev D siguen presentes en esta Rev 0. **No se reclaman: ADASA codificó 2 esa Rev D en el TM N29 sin detectarlas**, de modo que la revisión que las introdujo está aprobada.

| Defecto | Estado en esta Rev 0 |
|---|---|
| Cláusula 5.6.5, presente en la Rev C y ausente desde la D | Sigue ausente: el cuerpo salta de 5.6.4 a 5.6.6 en la página 8 |
| Formulario `AQ-QAM-F018` *"Pressure and Leak Test Report"*, que estaba en la página 13 de la Rev C | Sigue ausente. Se pidió como confirmación operativa en el correo del 06-Ago y no vino respuesta; por eso el punto sí se reclama, pero como pregunta operativa previa al ensayo, no como defecto del documento |
| Factor `1.5 x design pressure`, que estaba en el paso 5.5.12 de la Rev C | Sigue ausente |

**El cuerpo declara 135 bar de alta y 7,5 de baja y remite a la Line List.** La Line List adjunta prescribe seis presiones sobre 34 líneas: 135, 120, 90, 75, 7,5 y 3 bar, y la línea `DA-SSD-DN100-09-003` tiene diseño 60 bar con ensayo listado en 90. La relación hidrostática sobre diseño es 1,5 exacta en las 34 filas y ninguna línea plástica supera 7,5 bar, de modo que el hallazgo crítico del TM N27 sigue cerrado. Verificado en la ENTREGA 71 y no emitido entonces por la misma razón.

## PMI Procedure `P22-BA-09-000-006` Rev 0

El encuadre de refinería del anexo del subcontratista sigue en el documento más allá de las dos cláusulas de extensión que sí se reclaman: el programa retroactivo, las unidades de ácido fluorhídrico, los calentadores a fuego directo y la frase *"PMI is the responsibility of a refinery or fabricator"* de la cláusula 9.1. **No se emiten como observaciones separadas**: son la evidencia de que el anexo no está acotado al proyecto, que es la observación única que sí se levanta, y desglosarlas multiplicaría el conteo sin agregar exigencia.

La fila `Bolt & Nut` de `Pressure Vessel / Column` del Apéndice 1 sigue en 5% por lote. **No se reclama**: el circuito que gobierna la fila 2.4 del ITP es de cañería, y esa fila ya quedó en 10%.

## Visual Procedure `P22-BA-09-000-008` Rev 0

- La lista de referencias de la página 4 salta de 3.3 a 3.5, sin 3.4. Housekeeping documental, no degrada.
- La hoja de comentarios consolidada mantiene como respuesta a la nota sobre formularios *"Remove from procedure"*, cuando lo que el documento hizo fue reincorporar uno. La respuesta escrita quedó desactualizada respecto de lo que el documento hace; el documento manda, y lo que el documento hace es lo pedido.

## Painting Procedure `P22-BA-09-000-011` Rev 0

Fuera del formulario, el documento no cambió respecto de la Rev 0 del 05-Ago. El perfil de anclaje quedó en 50 a 80 micrones en el cuerpo y en el formulario, que era el punto que el correo del 06-Ago dio por cerrado.

## Los cuatro documentos, control de revisiones

El diferencial medido entre la Rev 0 del 05-Ago y la Rev 0 del 11-Ago es pequeño y no hay pérdidas de contenido: PMI +13 caracteres, HP y LP +44, Painting +99, Visual +647 y una página. El re-barrido completo, línea a línea, confirma que **ningún párrafo desapareció** en la re-emisión; todo lo quitado son las cláusulas que el propio comentario de ADASA pedía quitar. Esto se verificó a propósito, porque la lección de la ENTREGA 71 fue que una re-emisión puede perder contenido por el camino.

## Los tres procedimientos de ensayos no destructivos

Se emite lo que tiene requisito que lo sostenga. Queda fuera:

- **El rigor documental por sí mismo.** Los tres traen el procedimiento genérico del subcontratista con su propio formato, encabezados y datos de contacto. La ET no exige un formato de procedimiento, de modo que objetar la forma sin un requisito detrás es refutable.
- **La calificación del personal está correctamente declarada** en los tres, contra la Sección 2.0 del NDE Plan Rev C: práctica escrita del subcontratista basada en SNT-TC-1A, ISO 9712, PCN o CSWIP nivel II o III, con obligación de entregar los certificados antes de iniciar. En radiografía se suma el registro ante la Junta de Licenciamiento Atómico de Malasia. No hay observación que hacer ahí.
- **La extensión del examen** de los tres remite al plan de ensayos y a los planos, que es lo correcto: el NDE Plan Rev C aprobado es el que fija 100% de penetrantes en pase de raíz y último pase, 10% de radiografía en soldaduras a tope y la medición de espesores. No se les exige repetir la matriz.
- **Los parámetros de proceso** (tiempos de penetración y revelado, densidades de película, calibración del densitómetro, linealidad del equipo de ultrasonido) están dentro de lo que pide el código y no se comentan.

## Nota de administración de la entrega

El Submittal Form pide respuesta el **sábado 15-Ago-2026**, tres días corridos después de su emisión. El plazo de ADASA son siete días hábiles desde la recepción, per la Cláusula 37.2 de la BAE, que vencen el **viernes 21-Ago-2026**. Es la segunda vez seguida que el formulario del proveedor fija una fecha de retorno más corta que la contractual; en el TM N30 se dijo lo mismo y se emitió dentro del plazo real.
