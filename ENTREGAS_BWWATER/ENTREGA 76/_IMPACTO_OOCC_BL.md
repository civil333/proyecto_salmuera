---
titulo: ENTREGA 76 — impacto de la Rev B sobre las fundaciones L&A y sobre la BL Montaje
codigo: submittal 25007-0076
fecha: 2026-08-13
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# La Rev B del Civil and Loading Layout contra la ingeniería civil de ADASA

Trabajo contra documentos propios, no de BW Water. La Rev A de este plano es el antecedente que L&A tuvo a la vista (`INGENIERIA DE DETALLE OOCC/ANTECEDENTES/04_PLANOS_BW_WATER_VIGENTES/`) y sus fundaciones están emitidas en Rev 0, apto para construcción, en la ENTREGA 10 compilada. El paquete de licitación de montaje está publicado en Rev 0 con una tabla de pesos y de plintos tomada literalmente de esa misma Rev A.

## Lo primero: la Rev B es el insumo que L&A dejó declarado pendiente

La Nota Particular 2 del plano `P22-DWG-00-002-007` Rev 0, apto para construcción del 18-Jun-2026, dice:

> *"DISPOSICIÓN Y DIMENSIONES DE PERNOS DE ANCLAJE, PENDIENTES HASTA LA ENTREGA DE LOS PLANOS VENDOR DE LOS EQUIPOS."*

Los detalles de anclaje 3 a 7 de esta Rev B son ese dato. Llegan con dos contradicciones de diámetro que impiden usarlos tal cual:

| Equipo | Plano civil Rev B | Plano de detalle del equipo | Estado del plano de detalle |
|---|---|---|---|
| Bomba CIP BH-09-002 | M12, 4 pernos, patrón 200 × 266 mm | M14, 4 pernos, agujero Ø14, mismo patrón | En este mismo submittal, `P22-DWG-09-005-010` Rev B |
| Skid dosificación BDS-09-001/002 | M18, 10 pernos | M10, 10 pernos, empotramiento 120 mm | `P22-DWG-09-005-011` Rev B, Código 2 en el TM N26 |

En el caso de la bomba, el propio plano de la bomba resuelve la duda contra sí mismo: acota el agujero de la placa base en Ø14, que es el agujero de paso normal de un M12 y no admite un M14. En el caso del skid, el plano civil contradice un documento que ADASA ya aprobó.

Hasta que esto se fije, L&A no puede cerrar su Nota Particular 2 y los pernos post-instalados no se pueden ejecutar.

## Fundación del estanque CIP: 2,20 m construidos contra 2,50 m dibujados

| | Rev B de BW Water | `P22-DWG-00-002-007` Rev 0 de L&A |
|---|---|---|
| Forma | Octógono | Octógono |
| Lado a lado | **2.500 mm** | **2.200 mm** (con chaflanes 60/100/60) |
| Altura sobre terreno natural | 200 mm | 200 mm (N.T.C. +6,200 contra N.T.N. +6,000) |
| Profundidad total | no declarada | 700 mm hasta N.S.F. +5,500 |
| Anclaje | 4 pernos M18 en circunferencia Ø1940, a 30 y 60 grados | pendiente del plano vendor |

La altura coincide y la forma coincide. La planta difiere en 300 mm.

Sobre el octógono construido de 2.200 mm, una circunferencia de pernos de Ø1940 deja **130 mm** de distancia al borde en las caras rectas. Los propios planos de BW Water fijan como mínimo **150 mm**. El anclaje que la Rev B propone no cabe con su propia distancia de borde en la fundación que existe.

A esto se suma el espesor: 200 mm de plinto con pernos M18. Un anclaje adhesivo M18 pide del orden de 8 a 12 diámetros de empotramiento, entre 145 y 215 mm, y en 200 mm de hormigón no queda recubrimiento inferior. La fundación de L&A tiene 700 mm de profundidad total, así que el empotramiento sí cabe en el conjunto; lo que hay que declarar es el empotramiento requerido, no el espesor del plinto.

## Fundación de equipos CIP: un bloque a una cota contra cuatro plintos a cuatro cotas

L&A construyó un bloque en L de 3,00 × 2,30 m, cara superior a una sola cota (N.T.C. +6,200, es decir 200 mm sobre terreno natural) y 700 mm de profundidad.

La Rev B dispone sobre esa zona cuatro plintos de alturas distintas:

| Plinto | Equipo | Altura Rev B | Sobresale respecto de la cara construida |
|---|---|---|---|
| 3 | Filtro cartucho CIP FIL-09-002 | 0,30 m | +100 mm |
| 4 | Bomba CIP BH-09-002 | 0,26 m | +60 mm |
| 5 | Skid dosificación BDS-09-001/002 | 0,20 m | a nivel |
| 6 | Estanque dispersante TK-09-002 | 0,27 m | +70 mm |

La Sección B-B de la Rev B confirma que los plintos 3, 4 y 6 se dibujan como pedestales montados sobre la masa del 5. La obra construida es plana. Tres de los cuatro equipos quedan sin el pedestal que su plano pide.

## Fundación del contenedor: la malla coincide, el elemento no

| | Rev B de BW Water | `P22-DWG-00-002-003` Rev 0 de L&A |
|---|---|---|
| Apoyos a lo largo | 5 | 5 (ejes A a E) |
| Separación entre ejes | **3.000 mm** (300 de plinto más 2.700 de luz) | **3.000 mm** |
| Largo total apoyado | 12.300 mm sobre un contenedor de 12.192 | 12.000 mm entre ejes A y E |
| Elemento de apoyo | plinto continuo de 2.600 × 300 mm | dos pedestales de 1.000 × 1.000 mm por eje, a 2.240 mm entre sí |
| Cara superior | 300 mm sobre el cero del plano, y 322 mm en los tres centrales | 50 mm sobre terreno natural (N.T.C. +6,050 contra N.T.N. +6,000), uniforme |
| Fijación | posiciones de anclaje solo en los dos plintos extremos | inserto INS-1 en los 10 pedestales: placa PL500×500×20 con 2+2 Nelson stud 5/8" L=150 SAE 1020 y perfiles L100×100×6 |

La malla de 3,000 m coincide en los dos documentos, que es lo que gobierna el reparto de carga. Lo que no coincide es la forma del apoyo, su altura sobre el terreno y el sistema de fijación. El Cuadro de Materiales de L&A confirma los diez insertos: 2,50 m² de plancha de 20 mm, que son diez placas de 0,25 m², y 40 Nelson stud, que son diez por cuatro.

Los tres plintos centrales 22 mm más altos que los extremos no tienen contraparte en la obra construida, que está a una sola cota.

## La tabla de pesos de la BL Montaje Rev 0

La Sección 6.4 del paquete de licitación declara que sus cifras salen del plano Rev A. Cinco de sus nueve filas cambian con la Rev B:

| TAG / Equipo | BL Rev 0, de la Rev A | Rev B | Δ |
|---|---|---|---|
| Contenedor RO | ~14.934 kg | recalcular, ver abajo | — |
| TK-09-001 estanque CIP | 10.470 | 10.470 | sin cambio |
| FIL-09-002 filtro cartucho CIP | 267,6 | 270,0 | +2,4 |
| BH-09-002 bomba CIP | 180 | 180 | sin cambio |
| REL-09-001 calentador | 25 | 25 | sin cambio |
| TK-09-002 estanque dispersante | 490 | 517,5 | +27,5 |
| BDS-09-001/002 bombas dosificación | 57,4 | 100,0 | +42,6 |
| Panel de control local | 350 | 800,0 | **+450,0** |
| Panel de control calentador | 50 | 50 | sin cambio |

La fila del contenedor no se puede recalcular con lo que la Rev B entrega. El equipamiento interior en operación (mezclador estático, filtro cartucho RO, bomba de alta, dos turbochargers, recipientes a presión, panel local y aire acondicionado) suma 7.049,1 kg, y el contenedor aporta 3.700 kg. Las seis filas nuevas de cañerías, válvulas, instrumentos y soportes suman otros 8.167,9 kg, **sin decir qué parte está dentro del contenedor y qué parte en la zona CIP**, que son dos fundaciones separadas. El techo del rango, atribuyendo todas esas filas al contenedor, son 18.917,0 kg, un 27% sobre la cifra que la BL publica.

La BL también transcribe los plintos de la Rev A: *"cuatro plinths longitudinales de 2,6 × 0,3 × 0,4 m bajo las vigas del contenedor"* y los tres plintos CIP de 1,0 × 0,4 × 0,3, 1,8 × 2,1 × 0,3 y 2,5 × 2,5 × 0,3 m. Ninguno de esos cinco datos sobrevive a la Rev B, y ninguno corresponde tampoco a lo que L&A construyó.

## Acción que corresponde a ADASA

Ordenadas por urgencia. Ninguna se ejecuta en este trabajo.

1. **Fijar el diámetro de los pernos antes de que se dejen.** Es la condición para cerrar la Nota Particular 2 de L&A. Sale por el transmittal como confirmación operativa con fecha propia, anterior a la ejecución de los pernos post-instalados, y no como condición de la Rev 0: el plano se codifica 2 y la corrección del diámetro se incorpora al emitir, pero el dato lo necesita la obra antes de esa fecha.
2. **Reconciliar la fundación del estanque CIP.** Verificar si la circunferencia Ø1940 con distancia de borde de 130 mm es aceptable sobre el octógono de 2,20 m construido, o si el estanque acepta una circunferencia menor. Es cálculo de anclaje, no de fundación, y es rápido.
3. **Resolver los pedestales de los equipos CIP.** Decidir si se ejecutan los sobre-espesores de 60 a 100 mm sobre el bloque construido o si el equipo se cala con grouting. Afecta al alcance del montaje, no al de la obra civil ya ejecutada.
4. **Corregir la tabla de pesos y de plintos de la Sección 6.4 de la BL Montaje** antes de la próxima emisión del paquete. Cinco filas de pesos y los cinco datos de plintos. Mientras la BL siga en licitación con la cifra del contenedor tomada de la Rev A, el oferente cotiza sobre una base que el proveedor ya cambió.
5. **Pedir a BW Water el reparto de las seis filas nuevas** entre el interior del contenedor y la zona CIP, que es lo que permite asignar la carga a cada fundación. Va en el mismo transmittal.
6. **Declarar a L&A el estado de la interfaz**, para que la divergencia entre lo construido y el plano del proveedor quede registrada en el expediente del contrato de ingeniería y no aparezca como sorpresa en terreno.
