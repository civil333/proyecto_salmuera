---
titulo: Nota Técnica P22-NT-06-000-001-0, Ingeniería vigente para construcción
codigo: P22-NT-06-000-001-0
revision: 0
fecha: 2026-09-09
destinatario: Equipo de proyecto de Aguas Antofagasta, revisión interna previa
emisor: Aguas Antofagasta S.A.
estado: BORRADOR
---

# Objeto de esta nota

Se remite al contratista el paquete Ingeniería Vigente para Construcción del Montaje
Mecánico y las Obras Civiles del Módulo de Segunda Etapa de Salmuera de la Planta Desaladora
Taltal, y se declara mediante esta nota qué cambió respecto de la ingeniería que sirvió de
base para cotizar, de modo que el contratista disponga por escrito del alcance de esos
cambios antes de iniciar las obras.

El paquete contiene 55 documentos de ingeniería de detalle mecánica, de obras civiles y de
especificaciones de montaje, distribuidos en 88 archivos. Esta nota identifica, documento por
documento, la revisión que rige y aquello que cambió.

Esta nota no modifica el Contrato ni ninguno de sus anexos.

# Contenido del paquete

El paquete se organiza en cuatro carpetas.

**0. CONTROL DE CAMBIOS.** Una copia de esta misma nota en PDF, de modo que el paquete viaje
siempre con el documento que lo explica. Esta nota es el único documento de control: declara la
revisión que rige para cada documento y la cantidad vigente de cada partida.

**1. ING. DETALLE MECANICA**, 59 archivos en cuatro subcarpetas. `00_GENERAL` lleva el listado de
entregables. `01_PROCESOS_E_INSTRUMENTACION` lleva el diagrama de flujo, los cuatro P&ID, las hojas
de datos y el listado de instrumentos, y la lógica de control. `02_MECANICA` lleva cinco planos de
montaje y el listado de equipos. `03_CANERIAS` lleva seis planos de cañerías y de ubicación de
soportes, el Cuadernillo de Isometrías (once isometrías en 31 hojas), el Cuadernillo de Soportes
(21 páginas), la especificación técnica de cañerías de fabricación P22-ET-06-006-001 y los listados
de líneas, materiales y válvulas. `04_ MODELO` lleva el modelo 3D en Navisworks, en dos archivos publicados el 8 de septiembre de 2026: `MODULO COMPLETO.nwd`, de 21 megabytes, que federa la maqueta mecánica y el modelo civil, y `MODULO COMPLETO (nube puntos).nwd`, el mismo conjunto con la nube de puntos del levantamiento de terreno. Este último pesa 6,4 gigabytes y se entrega por enlace, no dentro del comprimido. Para el trabajo corriente de coordinación basta el primero.

**2. OBRAS CIVILES**, 18 láminas y 2 especificaciones técnicas. Diez láminas están en revisión 0
apta para construcción y ocho en revisión 1: P22-DWG-00-001-001 LAM1 y LAM2, P22-DWG-00-002-001,
P22-DWG-00-002-002 LAM1 y LAM4, P22-DWG-00-002-003 LAM1, y P22-DWG-00-002-007 LAM1 y LAM2. Las dos especificaciones, de Movimiento de Tierra y de
Obras Civiles, van en revisión 1. Las memorias de cálculo de obras civiles no forman parte del
paquete.

**3. ET MONTAJE.** El anexo A12, de montaje electromecánico del estanque TK-06-001 y la bomba
BH-06-001, con sus anexos. El anexo A13, de montaje de cañerías HDPE PE100 por electrofusión,
cuyo anexo es el Listado de Materiales en revisión 1.

Los documentos van en PDF, los listados en Excel y el modelo en Navisworks. Los planos editables en
formato DWG no se incluyen y se entregan a pedido. Para distribuir el paquete conviene comprimirlo,
dado que algunas rutas internas del dossier mecánico son largas.

# Documentos de referencia

| Código | Documento | Revisión |
|---|---|---|
| P22-BL-06-000-001-0 | Bases de Licitación del Montaje Mecánico y Obras Civiles | Contractual |
| Anexo A9 | Formato de Presupuesto de Obras Civiles, Mecánica y Piping | Contractual |
| P22-ET-06-007-001-0 | Especificación técnica de montaje electromecánico | 0 |
| P22-ET-06-007-002-0 | Especificación técnica de montaje de cañerías HDPE | 0 |

# Qué gobierna el alcance y qué gobierna la construcción

El alcance contratado se fija en el Formato de Presupuesto (Anexo A9), el cual no se modifica
con esta entrega. Cada partida de dicho Formato define una obra y su forma de medición y pago.

La ingeniería vigente define cómo se construye ese alcance. Una revisión nueva de un plano
cambia la forma de ejecutar una partida, y en algunos casos su cantidad de obra, pero no
incorpora ni retira partidas.

De lo anterior se desprende el criterio con que se lee esta nota. Toda obra a ejecutar tiene
su partida en el Formato, por lo que un documento de ingeniería sin partida asociada no
constituye alcance contratado ni habilita cobro alguno, sin perjuicio de su valor como
antecedente de coordinación.

# Cambios de la ingeniería respecto de la que se cotizó

## La fundación del contenedor sube 250 milímetros

La cara superior de la fundación del contenedor del módulo pasa de la cota +6,050 a la cota
+6,300, y el sello de fundación de la +5,150 a la +5,400. La geometría y la armadura se
mantienen: diez pedestales de 1,00 por 1,00 metros dispuestos en cinco ejes separados 3,00
metros, unidos por vigas de 30 por 30 centímetros.

Con la fundación suben las cuatro cotas de conexión con el módulo.

| Punto de conexión | Cota cotizada | Cota vigente |
|---|---|---|
| P8-001, entrada de salmuera al módulo | +8,250 | +8,500 |
| P9-001, permeado | +8,593 | +8,850 |
| P9-002, permeado fuera de especificación | +8,593 | +8,850 |
| P9-003, salida de salmuera de rechazo | +8,583 | +8,850 |

Las conexiones con el módulo existente de 11 litros por segundo (tie-ins 1, 3 y 6) mantienen
su cota +6,204. Rigen los planos P22-DWG-00-002-003 LAM1, P22-DWG-06-005-103 y
P22-DWG-06-006-102, los tres en revisión 1.

## La fundación del sistema CIP se rediseña

La fundación de los equipos del sistema CIP se reduce de 4,13 a 2,63 metros cúbicos de
hormigón G25, con lo que el total de hormigón de la zona baja de 7,36 a 5,80 metros cúbicos
y la excavación de dicha zona de 5,01 a 1,60 metros cúbicos.

El rediseño incorpora una junta de dilatación entre elementos de fundación. Se ejecuta con
poliestireno expandido de 2,5 centímetros de espesor, sello Sikaflex 1A y primer VP-215
aplicado en ambas paredes. La disposición y las dimensiones de los pernos de anclaje quedan
definidas en el plano. Rige el P22-DWG-00-002-007 LAM1 en revisión 1, con su armadura en la
LAM2, también en revisión 1.

## El movimiento de tierra recoge el nivel nuevo

Con la fundación del contenedor 250 milímetros más alta, la excavación de esa zona baja de 38,02 a
20,95 metros cúbicos, sobre un área que pasa de 53,51 a 49,96 metros cuadrados. Rige el
P22-DWG-00-001-001 en revisión 1, con la planta en la LAM1 y las secciones en la LAM2.

Las cantidades de excavación que rigen para la obra son las siguientes, cada una tomada del plano que
gobierna su zona.

| Zona | Excavación | Plano |
|---|---|---|
| Trazado 1 | 5,22 m³ | P22-DWG-00-001-001 LAM1 |
| Trazado 2 | 34,91 m³ | P22-DWG-00-001-001 LAM1 |
| Fundación del estanque TK-06-001 | 4,22 m³ | P22-DWG-00-002-002 LAM1 |
| Fosa de drenajes TK-06-004 | 3,71 m³ | P22-DWG-00-002-004 LAM1 |
| Fundación de la bomba BH-06-001 | 0,62 m³ | P22-DWG-00-002-002 LAM4 |
| Fundación del sistema CIP | 1,60 m³ | P22-DWG-00-002-007 LAM1 |
| Fundación de la cubierta del sistema CIP | 4,25 m³ | P22-DWG-00-002-007 LAM3 |
| Fundación del contenedor | 20,95 m³ | P22-DWG-00-001-001 LAM1 |
| **Total excavado** | **75,48 m³** | |

El fondo de excavación se lleva hasta el nivel de sello de fundación menos el espesor de la capa que
va bajo el sello. Son las cotas 5,35 en el contenedor, 5,45 en el sistema CIP, 5,30 en el estanque
TK-06-001 y 4,155 en la fosa TK-06-004, donde el mejoramiento es de 15 centímetros y no el
emplantillado de 5 de las demás fundaciones.

Los rellenos no cambian: 9,00 metros cúbicos de relleno seleccionado de arena y 29,69 de relleno
estructural. Las cantidades de los cuadros son referenciales y se validan en terreno.

## El listado de materiales cambia accesorios y material de brida

El metraje de cañería no cambia y se mantiene en 335 metros, y tampoco cambian las cantidades
de codos, cuplas, tee, reducciones, espárragos y stub end. Los accesorios sí cambian, según el
listado P22-LI-06-006-102 en revisión 1.

Se retiran los dos accesorios de PVC-U, un codo de 90 grados de 4 pulgadas y una tee
reductora de 4 por 2 pulgadas, por lo que la instalación queda íntegramente en HDPE.

El buje de reducción en Súper Dúplex (UNS S32750) sube de 2 a 5 unidades y el spigot saddle
with cutter de 4 por 1 pulgada, de 2 a 5. Se incorporan tres uniones adaptador PE100 por Súper
Dúplex de 1 pulgada y se retira el back-up flange de 4 pulgadas. Las empaquetaduras bajan de
45 a 42 unidades.

La brida no cambia de tipo. En las dos revisiones es la misma pieza, un flange suelto de junta
solapada montado sobre stub end (FLANGE LJ, de Lap Joint), con perforaciones según ASME B16.5
clase 150. Lo que la revisión 1 del listado incorpora es su material, acero galvanizado por
inmersión, y la cantidad de 4 pulgadas pasa de 22 a 23 unidades. Dado que las isometrías no
declaran el material de la brida, para ese dato rige el listado.

El contratista debe verificar este listado antes de emitir las órdenes de compra de
accesorios y bridas.

## El cuadernillo de isometrías cambia poco y se renumeró

Siete de las once isometrías son idénticas a las de la revisión con la que se cotizó. Cambian de
revisión únicamente P22-DWG-06-006-005, P22-DWG-06-006-008, P22-DWG-06-006-009 y
P22-DWG-06-006-011, que aportan tres hojas nuevas entre las tres primeras y la última.

El cotejo contra el juego anterior debe hacerse por contenido y no por número de hoja. En
P22-DWG-06-006-011 entra una hoja nueva en la posición H.2 y las seis siguientes se desplazan, de
modo que la H.2 anterior es ahora la H.3 y la H.7 es la H.8. En P22-DWG-06-006-008 la antigua H.4
pasa a ser la H.5.

## Documentos que cambian de revisión

Once documentos del dossier mecánico están en una revisión posterior a la que sirvió para cotizar.
El resto se mantiene en la revisión con la que se cotizó.

| Código | Revisión | Documento |
|---|---|---|
| P22-DWG-06-005-103 | 1 | Plano de montaje del módulo |
| P22-DWG-06-006-101 | 1 | Cañerías de interconexiones, planta |
| P22-DWG-06-006-102 | 1 | Cañerías de interconexiones, cortes y detalles |
| P22-DWG-06-006-103 | 1 | Cañerías TK y bomba, planta |
| P22-DWG-06-006-104 | 1 | Cañerías TK y bomba, cortes y detalles |
| P22-DWG-06-006-005 | 2 | Isometría SA-HDPE-DN110-PN10-005, cinco hojas |
| P22-DWG-06-006-008 | 1 | Isometría PE-HDPE-DN90-PN10-001, cinco hojas |
| P22-DWG-06-006-009 | 1 | Isometría PE-HDPE-DN90-PN10-003, dos hojas |
| P22-DWG-06-006-011 | 2 | Isometría SA-HDPE-DN110-PN10-007, ocho hojas |
| P22-LI-06-006-102 | 1 | Listado de materiales de cañerías |
| P22-LI-06-008-101 | 1 | Listado de instrumentos |

En obras civiles cambian de revisión las cinco láminas ya indicadas y las dos especificaciones
técnicas.

# Efecto sobre las partidas del Formato de Presupuesto

Dos partidas del Capítulo 4 cambian su cantidad de obra debido a los cambios ya descritos.
Ambas se miden por unidad de obra, por lo que se pagan según la cubicación realmente ejecutada
y verificada en terreno por la inspección técnica de obra (ITO).

El documento emitido lleva aquí la tabla de las catorce partidas del Capítulo 4, con su unidad y
sus cantidades cotizada y vigente, importada de la lista `CUBICACIONES`. Las dos que cambian son
la 4.2 Fundación sistema CIP (F2b), de 7,36 a 5,80 metros cúbicos, y la 4.6 Excavación común en
fundaciones y zanjas de drenaje, de 115,10 a 90,58.

La cantidad de la partida 4.6 se mide con el mismo criterio con que se cotizó, esto es, sobre el volumen retirado con el veinte por ciento de esponjamiento que declaran los cuadros de excavación de los planos. El volumen excavado que la sustenta es de 75,48 metros cúbicos.

Las demás partidas del Capítulo 4 mantienen su cantidad. Las del Capítulo 1 tampoco cambian.
Los 67 soportes de los once tipos del cuadernillo P22-DWG-06-006-107 se mantienen, dado que
dicho cuadernillo y los planos de ubicación de soportes P22-DWG-06-006-105 y P22-DWG-06-006-106
conservan su revisión 0.

En el Corte D del plano P22-DWG-06-006-102 deja de aparecer la válvula VM-06-010, la cual la
revisión anterior rotulaba como proyectada y que no tiene partida en el Formato.

Se hace presente que el Formato de Presupuesto repite dos códigos de partida. Existen dos
partidas numeradas 4.3, correspondientes a la Fundación de la cubierta metálica del sistema
CIP (cobertizo) y a la Fundación dinámica bomba BH-06-001 (F3), y dos numeradas 4.7,
correspondientes a los Dados de hormigón G25 para pedestales de soportes a piso y al Relleno
compactado con material seleccionado y base estabilizada.

Debido a lo anterior, toda referencia a una partida debe consignar su número y su nombre
completo, tanto en esta nota como en los estados de pago.

# La cubierta metálica del sistema CIP

La fundación de la cubierta se ejecuta íntegra. Corresponde a la partida 4.3 Fundación de la
cubierta metálica del sistema CIP (cobertizo), cotizada en 2,38 metros cúbicos, la cual
incluye los 24 pernos de anclaje F-1554 de 3/4 de pulgada preinstalados y su protección
anticorrosiva interina hasta la recepción de la obra. Rige el plano P22-DWG-00-002-007 LAM3
en revisión 0.

La estructura metálica no tiene partida en el Formato y no forma parte del alcance
contratado. Aguas Antofagasta la ejecutará en una etapa posterior, sobre la fundación y los
pernos que se dejan preinstalados en esta obra.

Debido a lo anterior, se requiere especial cuidado en la verticalidad, el nivel y la posición
de los 24 pernos, según el plano, y en mantener su protección hasta la recepción. Un perno
fuera de tolerancia obliga a intervenir la fundación en la etapa posterior.

# Vigencia de la documentación

Para cada código y lámina rige la revisión que este paquete entrega, por lo que cualquier
revisión anterior del mismo documento, cualquiera sea la vía por la que el contratista la
haya recibido, queda reemplazada por la de esta entrega.

La tabla de vigencia lista los 55 documentos del paquete, uno por fila, con la revisión que rige
y el dossier donde se encuentra. Ante cualquier duda de vigencia prevalece esa tabla.

> La tabla de vigencia y la de cantidades del Formato **no se transcriben en este archivo**: el
> generador las importa de `BORRADOR_REV0/script/generar_ingenieria_vigente.py`, donde viven las
> listas `VIGENCIA` y `CUBICACIONES`. Ese mismo script las usa para el gate que contrasta lo
> declarado contra el árbol real del paquete, de modo que hay una sola fuente y no tres.

Se exceptúa el P&ID de alimentación P22-DWG-06-009-102, cuya revisión 1 el proyectista emitió
solo en formato editable. El paquete mantiene la revisión 0 y la revisión 1 se remitirá en
cuanto se reciba el ploteo.
