---
titulo: Ledger de cierre de comentarios — ENTREGA 82 (submittal 25007-0082)
fecha: 2026-08-26
estado: INTERNO
type: ledger
project: salmuera-taltal
---

# Ledger de cierre — ENTREGA 82

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0082`, "UHPRO Structural Design Criteria", emitido el viernes 21-Ago-2026, devolucion pedida el lunes 24-Ago-2026, plazo real de la Clausula 37.2 el martes 1-Sep-2026. Un documento.

---

## UHPRO Structural Design Criteria Rev 0 (IFC) — `P22-CD-09-005-003`

Once paginas. Las paginas 2 a 11 son **imagen escaneada**: el texto se obtuvo por reconocimiento optico con Tesseract y toda cifra citada aqui se confirmo leyendo el render a 300 dpi de `render/p02.png` a `p11.png`. Extraccion en `md/P22-CD-09-005-003_0_UHPRO_Structural_Design_Criteria_extracted.md`.

**El documento no trae hoja de comentarios consolidada.** La Rev B si la traia, con nueve comentarios. Sin ella no hay declaracion escrita del proveedor que contrastar.

### Alcance: el codigo anterior fue Codigo 1

La Rev B quedo **Codigo 1 — Approved** en el TM N25, con la accion literal: *"Action: none on this criteria document — accepted; issue directly at IFC Rev 0, folding the editorial items at issue."*

Es decir: **la accion sobre este documento fue "ninguna"**. Los tres items de la NOTE-02 eran una peticion de aseo a incorporar al emitir, no una condicion de aprobacion. La revision de la Rev 0 es por tanto un **diferencial contra lo aprobado**: verificar que nada del cuerpo aprobado cambio ni desaparecio.

### Diferencial de contenido: el cuerpo tecnico es identico

Comparacion palabra a palabra del cuerpo de la Rev B (`../ENTREGA 55/P22-CD-09-005-003_B UHPRO Structural Design Criteria.pdf`, texto nativo) contra el reconocimiento optico de la Rev 0, con confirmacion sobre render de cada tabla numerica. **Nada del cuerpo cambio, nada desaparecio y nada contradice lo aprobado.** Verificados sin cambio:

- **Parametros sismicos**: zona 3, factor de importancia 1,0, factor de reduccion R = 3,0, aceleracion efectiva maxima 0,40 g, suelo tipo E, n = 1,80, amortiguamiento 0,03, limite inferior del coeficiente sismico 0,25 veces la aceleracion efectiva. Las siete filas siguen citadas a NCh 2369 Of.2003, con la nota de que la clasificacion de suelo se mantiene como envolvente conservadora a la espera del estudio geotecnico.
- **Combinaciones de carga**: los doce casos de tensiones admisibles, incluidos el 11 y el 12 citados a la clausula 4.5 de NCh 2369 Of.2003; los diez casos por factores de carga y resistencia; los dos casos de izaje.
- **Materiales**: NCh 203 / A36 con 248 MPa, NCh 204 / A440-280H con 280 MPa, NCh 204 / A630-420H con 420 MPa, NCh 170 / G25 con 25 MPa.
- **Viento**: velocidad basica 27 metros por segundo, exposicion D, factor topografico 1,05, direccionalidad 0,85, citados a NCh 432:2025.
- **Izaje**: API RP 2A-WSD, factores dinamicos 1,35 y 2,0, factor de seguridad 2,0 para el cancamo, carga lateral fuera del plano del 5 por ciento.

Los unicos cambios son de identificacion: el numero interno del consultor pasa de `P2616-STR-SPEC-001-IFA-RB` a `P2616-STR-SPEC-001-IFC-R0`, el encabezado del cuerpo de `REV. B 23-JUN-2026` a `REV. 0 11-AUG-2026`, y la tabla de revisiones suma la fila `0 / 11-AUG-2026 / FOR CONSTRUCTION`.

### Los tres items editoriales de la NOTE-02

| Item | Pedido, literal | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| Fecha | "reconcile the cover-block date against the 23-Jun-2026 body date" | La portada declara `Date: 18 Aug 26`; el encabezado del cuerpo, en las nueve paginas de cuerpo (de la 3 a la 11), declara `REV. 0 DATE: 11-AUG-2026`. La brecha crecio de un dia a siete. Si desaparecio una inconsistencia colateral que la Rev B tenia dentro de su propia portada (encabezado 24 Jun contra cajetin 24 Jul) | **No cerrado** |
| Tabla duplicada | "remove the duplicate table number" | Persiste. La tabla de combinaciones en estado de servicio sigue rotulada `Table 7 Allowable Resistance Design` y la de izaje, `Table 7 - Load combination for lifting analysis`. La secuencia del documento sigue siendo 1, 2, 3, 4, 5, 7, 6, 7 | **No cerrado** |
| Unidades de viento | "confirm the minimum wind pressures render as N/m2 on the issued PDF" | Leido sobre el render, no sobre el reconocimiento optico: `Vertical walls: 250 N/m2` y `Horizontal surfaces (Roofs): 130 N/m2`, con el exponente correctamente compuesto. Igual en la tabla de sobrecargas, `1.0 kN/m2` | **Cerrado** |

**Los dos items abiertos son housekeeping documental y nunca fueron condicion de aprobacion.** No degradan el documento por si solos.

### NOTE-01: criterios de izaje

El capitulo de izaje se conserva integro. El diseno final de izaje (calculo, plano con pesos y diseno del yugo) **sigue siendo entregable separado sobre otro documento**, seguido en la Seccion 3 del transmittal. No es accion sobre este documento.

### Dato factual: no hay endoso profesional

Ninguna pagina lleva timbre, sello ni declaracion de ingeniero profesional. Hay rubricas manuscritas sin nombre impreso, sin numero de registro y sin leyenda de responsabilidad: el cajetin registra `Prepared By AULEM`, `Reviewed By JFR`, `Checked By NOP`, `Approved By LPL`, y la fila de la revision 0 de la tabla del consultor lleva dos rubricas sobre `CSB` y `JCP`.

**No se emite como observacion sobre este documento.** El compromiso `PRG-32`, critico y vencido, exige el endoso de un ingeniero profesional chileno sobre el **informe de calculo sismico** `P22-CD-09-005-001`, no sobre este documento de criterios. Extenderlo aqui seria exigir mas de lo pedido. Se sigue en la Seccion 3, donde ya vive.

### Fuera de alcance (no se emite)

- El cajetin de la portada perdio las filas historicas A y B que la Rev B si apilaba; el historial queda solo en la tabla del consultor de la pagina 2. **Housekeeping.**
- La portada se rotula para construccion pero el cuerpo conserva la redaccion prospectiva de un documento de criterios. **Sin requisito que lo sostenga.**
- Se arrastran de la Rev B dos defectos de composicion de la portada: `ADASACode:` y `Page: 1of 11`, ambos sin espacio. **Venian en la revision aprobada: no se levantan.**
- La pagina 3 del cuerpo cierra un parrafo con el punto final en color rojo. **Marca de edicion, sin consecuencia.**
- El Submittal Form deja en blanco la columna de observaciones, sin marcar la procedencia de la revision anterior. **Housekeeping del formulario.**

---

## Sintesis para la disposicion

El documento venia de **Codigo 1** con accion "ninguna". El cuerpo tecnico llega a Rev 0 sin un solo cambio y sin contradecir nada de lo aprobado. Lo unico abierto son dos items de aseo que nunca fueron condicion. **La disposicion natural es Codigo 1, sin PDF anotado**, con los dos items declarados para ordenar en la proxima emision natural.
