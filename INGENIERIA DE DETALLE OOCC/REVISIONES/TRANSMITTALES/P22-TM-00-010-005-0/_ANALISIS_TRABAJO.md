---
titulo: Analisis de trabajo del Transmittal N5 a L&A - ENTREGA 14 y ENTREGA 13
codigo: P22-TM-00-010-005-0
fecha: 2026-09-09
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Analisis de trabajo - ENTREGA 14 (TT-015) y ENTREGA 13 (TT-014)

Documento interno de respaldo. No se envia a L&A.

## Que llego

| Entrega | Carta | Fecha | Documentos | Estatus declarado |
|---|---|---|---|---|
| ENTREGA 13 | 067-032-032-COR-TT-014 | 07-09-2026 | `P22-DWG-00-002-001` Rev 1 lamina 1; `P22-3D-00-002-001` Rev 1 | Para Construccion / Para Uso e Informacion |
| ENTREGA 14 | 067-032-032-COR-TT-015 | 08-09-2026 | `P22-DWG-00-001-001` Rev 1, laminas 1 y 2 | Para Construccion |

La ENTREGA 14 responde el pedido de ADASA del 04-09-2026, enviado como respuesta al hilo de la carta
TT-013. La ENTREGA 13 no fue pedida: el propio correo del 04-09 concluyo que el `00-002-001` no
requeria cambio.

## Metodo

Las dos laminas de la ENTREGA 14 son vectorizadas: la extraccion de texto devuelve 547 y 529
caracteres, todos del cajetin, y ningun valor de los cuadros. Todo lo que sigue se leyo por render en
PNG a 280 y 300 puntos por pulgada, comparando contra la revision que hoy rige en el paquete
`INGENIERIA VIGENTE PARA CONSTRUCCION`.

---

## 1. Cubicaciones del cuadro de la lamina 1

| Item | Descripcion | Rev 0 | Rev 1 | Diferencia |
|---|---|---|---|---|
| 1 | Excavacion trazado 1 | 5,22 | 5,22 | sin cambio |
| 2 | Excavacion trazado 2 | 34,91 | 34,91 | sin cambio |
| 3 | Relleno seleccionado arena trazado | 9,00 | 9,00 | sin cambio |
| 4 | Relleno estructural trazado | 29,69 | 29,69 | sin cambio |
| 5 | Excavacion fundacion TK salmuera | 4,22 (12,49 m2) | 4,22 (12,49 m2) | sin cambio |
| 6 | Excavacion fosa de drenaje | 3,71 (3,91 m2) | 3,71 (3,91 m2) | sin cambio |
| 7 | Excavacion TK CIP y equipos | 5,01 (12,45 m2) | **1,03** (4,85 m2) | -3,98 |
| 8 | Excavacion contenedor | 38,02 (53,51 m2) | **20,95** (49,96 m2) | -17,07 |

Excavacion total del cuadro: de 91,09 a **70,04** metros cubicos. Rellenos sin cambio, 38,69.

La reduccion del contenedor supera la estimacion de ADASA del 04-09, que fue de unos 13 metros
cubicos calculados como 53,51 metros cuadrados por 0,25 metros. La diferencia se explica porque
ademas del sello baja el area, de 53,51 a 49,96 metros cuadrados.

Las dos notas del cuadro se mantienen: las cubicaciones son referenciales y deben ser validadas por
el contratista, y no consideran esponjamiento de material retirado ni aportado.

## 2. Cotas de la lamina 2

| Seccion | Rev 0 | Rev 1 |
|---|---|---|
| A, excavacion TK salmuera | ancho 3,5 m, fondo EL. 5,35 | sin cambio |
| B, TK salmuera y fosa | ancho superior **3,4 m**, fondos EL. 5,35 y EL. 4,30 | ancho superior **3,7 m**, mismos fondos |
| C, fundacion TK CIP | ancho 2,2 m, fondo EL. 5,45 | sin cambio |
| D, fundacion equipos | ancho **2,3 m**, fondo EL. 5,45 | ancho **1,8 m**, mismo fondo |
| E, equipos y contenedor | equipos 3 m, cota intermedia 0,17, fondo **EL. 5,15** | equipos 2,2 m, cota intermedia 0,9, fondo **EL. 5,35** |
| F, contenedor | ancho 3,2 m, fondo **EL. 5,15** | ancho 3,2 m, fondo **EL. 5,35** |

Las diez secciones tipicas de zanja del encabezado mantienen sus cotas, de EL. 5,20 a EL. 5,16.

La correccion del ancho de la seccion B es una mejora: en la revision 0 el ancho superior de la
excavacion, 3,4 metros, era menor que el ancho de fondo, 3,5 metros, lo que es imposible con talud
2:1. Con el terreno natural a unos 5,75 y el fondo en 5,35, el talud aporta 0,20 metros por el lado
excavado y el ancho superior resulta 3,7 metros, que es lo que ahora declara.

---

## 3. Consistencia del sello de fundacion contra los planos de fundaciones

Cota del nivel de sello de fundacion leida de cada plano de fundacion en la revision que rige, contra
el fondo de excavacion que declara la lamina 2 nueva.

| Zona | Plano | Rev | N.S.F. | Capa bajo el sello | Fondo esperado | Fondo declarado | Estado |
|---|---|---|---|---|---|---|---|
| Contenedor | `00-002-003` LAM1 | 1 | +5,400 | emplantillado 5 cm | 5,35 | Secciones E y F: 5,35 | consistente |
| Sistema CIP | `00-002-007` LAM1 | 1 | +5,500 | emplantillado 5 cm | 5,45 | Secciones C y D: 5,45 | consistente |
| Estanque TK-06-001 | `00-002-002` LAM1 | 1 | +5,350 | emplantillado 5 cm | 5,30 | Secciones A y B: 5,35 | **5 cm alto** |
| Fosa TK-06-004 | `00-002-004` LAM1 | 0 | +4,305 | mejoramiento 15 cm | 4,155 | Seccion B: 4,30 | **14,5 cm alto** |
| Bomba BH-06-001 | `00-002-002` LAM4 | 1 | +5,405 | emplantillado 5 cm | 5,355 | sin seccion propia | **no representada** |
| Fundacion cubierta CIP | `00-002-007` LAM3 | 0 | +5,070 | emplantillado 5 cm | 5,02 | sin seccion propia | **no representada** |

**El criterio del fondo de excavacion quedo aplicado a medias.** Donde L&A rehizo el dibujo, que son
el contenedor y el sistema CIP, el fondo de excavacion baja el espesor de la capa que va bajo el
sello. Donde no lo rehizo, que son el estanque y la fosa, el fondo sigue coincidiendo con el propio
sello, que es el criterio de la revision 0 y el mismo que ADASA le observo para el contenedor. La
lamina usa dos criterios a la vez.

En la fosa el desfase llega a casi 15 centimetros. Bajo su sello va una capa de mejoramiento de 15,
rotulada M.H.A. e=15 en la elevacion de eje del propio plano, mientras las demas fundaciones llevan
emplantillado de 5.

---

## 4. Contradicciones entre planos vigentes

Cuadros de excavacion de los planos de fundacion, todos verificados por render.

| Plano | Rev | Excavacion | Retiro | Relleno |
|---|---|---|---|---|
| `00-002-002` LAM1, estanque TK-06-001 | 1 | 4,22 | 5,06 | sin dato |
| `00-002-002` LAM4, bomba BH-06-001 | 1 | 0,62 | 0,75 | sin dato |
| `00-002-003` LAM1, contenedor | 1 | **38,02** | 45,62 | 30,03 |
| `00-002-004` LAM1, fosa TK-06-004 | 0 | 3,71 | 1,90 | 2,13 |
| `00-002-007` LAM1, sistema CIP | 1 | **1,60** | 1,92 | sin dato |
| `00-002-007` LAM3, fundacion cubierta CIP | 0 | 4,25 | 5,1 | 1,96 |

De las cuatro fundaciones que el cuadro de la lamina 1 si cubica, dos coinciden exactamente con su
plano de fundacion, el estanque con 4,22 y la fosa con 3,71, y **dos no coinciden**:

| Zona | Plano de movimiento de tierra Rev 1 | Plano de fundacion vigente | Diferencia |
|---|---|---|---|
| Contenedor | 20,95 | `00-002-003` LAM1 Rev 1: **38,02** | 17,07 |
| Sistema CIP | 1,03 | `00-002-007` LAM1 Rev 1: **1,60** | 0,57 |

Que dos de las cuatro coincidan al centesimo y dos no, descarta que se trate de criterios de medicion
distintos: son desactualizaciones.

La del contenedor ya estaba consultada a L&A el 04-09 y sigue sin respuesta. La ENTREGA 14 la agrava,
porque ahora hay dos planos con estatus Para Construccion que declaran cifras distintas de la misma
excavacion. La del sistema CIP es nueva: ADASA pidio alinear el item 7 a los 1,60 metros cubicos del
`00-002-007` y L&A entrego 1,03.

**Dos excavaciones no estan cubicadas en el cuadro.** La fundacion de la bomba BH-06-001, con 0,62
metros cubicos, y la fundacion de la cubierta del sistema CIP, con 4,25. Esta ultima si se construye:
lo que quedo fuera de alcance el 18-06-2026 es la estructura metalica, no su fundacion, que se ejecuta
con sus 24 pernos F-1554 colados.

---

## 5. La cantidad de la partida 4.6 del Formato de Presupuesto

La partida contractual dice: *Excavacion comun en fundaciones y zanjas de drenaje mas retiro y
transporte de excedentes, retiro incluido en el precio unitario por metro cubico excavado*, unidad
metro cubico, cantidad **115,10**, precio unitario 22.000 por 1,3.

Esa cantidad **no tiene respaldo en el repositorio**. El generador del Formato la dejo sin valor el
28-05-2026 y el siguiente commit que la toca, del 04-09-2026, ya escribe 111,70. El 115,10 se escribio
a mano sobre el Excel, en la rama que se licito, y nunca paso por control de versiones.

**Se reconstruyo desde los planos y calza:**

```
  zanjas del 00-001-001        5,22 + 34,91                              =  40,13
  fundaciones, revision 0      4,22 + 0,62 + 38,02 + 3,71 + 5,01 + 4,25  =  55,83
                                                                  suma   =  95,96
  con 20 por ciento de esponjamiento          95,96 x 1,2                = 115,15
```

Contra los 115,10 del Formato. Ocho sumandos leidos de seis planos distintos que dan la cifra
declarada con el factor de esponjamiento que los propios cuadros consignan.

De aqui se sigue algo que conviene decir con claridad: **la cantidad de la partida se construyo como
volumen retirado esponjado, mientras la partida se mide y se paga por metro cubico excavado.** La
cantidad de referencia esta un veinte por ciento por sobre el volumen que se excava.

**Lo que la Nota Tecnica declara hoy no es coherente con eso.** El paso de 115,10 a 111,70 se obtuvo
restando 3,41, que es la baja de la zona CIP *sin* esponjar, a una cifra que si lo esta. Con el mismo
criterio la resta deberia haber sido 4,09 y el resultado 111,01.

**Cantidad que corresponde con la ingenieria vigente**, manteniendo el criterio con que se licito:

| Escenario | Excavado | Con esponjamiento | Contra 115,10 |
|---|---|---|---|
| Revision 0, como se licito | 95,96 | 115,15 | referencia |
| Revision 1, sistema CIP segun `00-002-007`, 1,60 | 75,48 | **90,58** | -24,5 |
| Revision 1, sistema CIP segun `00-001-001`, 1,03 | 74,91 | 89,89 | -25,2 |

Con el precio unitario contractual de 28.600 pesos por metro cubico, gastos generales de 35 por ciento
y utilidad de 11,1 por ciento, la baja es del orden de **1,05 millones de pesos**, no los 97.240 que
declara la Nota Tecnica en borrador.

Las dos cifras del escenario vigente dependen de cual valor se adopte para la zona CIP, que es
justamente una de las contradicciones abiertas con L&A.

---

## 6. Identificacion de las laminas y estado de emision

**La lamina 1 no se identifica como revision 1 en ninguna parte de su cajetin.** El campo de revision
del cajetin de Aguas Antofagasta dice REV. 0; el campo de revision del rotulo del proyectista lleva el
simbolo de nube en lugar del numero; y la fila nueva del cuadro de revisiones dice SE MODIFICA LO
INDICADO, con fecha 08/09/26, tambien sin numero. Solo el nombre del archivo y la carta de remision
declaran la revision 1. La lamina 2, en cambio, si declara REV. 1 en su cajetin.

**La fila de la revision 0 se reescribio hacia atras, en las dos laminas.** Donde la revision 0 vigente
dice APTO PARA CONSTRUCCION, las laminas nuevas dicen PARA USO E INFORMACION en esa misma fila. Es la
revision que hoy rige en el paquete entregado, degradada de manera retroactiva en su estado de emision.

Este es el punto de forma que ADASA ya observo el 04-09 sobre las cinco laminas de la ENTREGA 12. La
ENTREGA 14 no lo corrige y agrega la reescritura de la fila anterior.

## 7. Estado de los archivos recibidos

El comprimido `2026-09-07 TT-015 CIV, PL Mov. Tierra Rev.1.zip` trae cuatro archivos. Los tres PDF
estan integros y son identicos byte a byte a los que ya venian sueltos en la carpeta. El cuarto, el
archivo nativo `P22-DWG-00-001-001-1.dwg` de 25,1 megabytes, **falla la verificacion de integridad**:
su suma de comprobacion declarada no corresponde al contenido y no se puede extraer. El encabezado
del archivo es valido, AC1032, de modo que el problema esta en el cuerpo o en la generacion del
comprimido.

Hay que pedir el nativo de nuevo. Los dos PDF si sirven y no bloquean la revision.

## 8. La ENTREGA 13 y el replanteo

El `P22-DWG-00-002-001` revision 1 cambia **las coordenadas UTM de once de los trece vertices** de
replanteo. El desplazamiento mayor es el del vertice V13, que pasa de Norte 7.188.940,939 Este
350.112,089 a Norte 7.188.940,098 Este 350.118,124, unos 6 metros en el Este. Los vertices V04 y V05
no cambian.

El paquete de ingenieria vigente entrega hoy la revision 0 de esa lamina. Un contratista que replantee
con ella lo hara sobre coordenadas superadas.

Esto corrige una conclusion propia: el correo del 04-09 anoto que esa lamina no requeria cambio porque
solo acota el nivel de terreno natural por zona, que no se movio. La revision de las coordenadas no se
hizo entonces, y L&A si tenia motivo para reemitirla.

---

## 9. Los modelos tridimensionales

Extraidos con el puente de automatizacion de Navisworks. El clon del script vive en esta misma
carpeta y su salida en `md/`. Al clon se le hicieron dos ajustes. Primero, la version de Navisworks
se detecta sola: la instalacion 2026 de este equipo ya no trae las bibliotecas de la interfaz de
programacion, y la que responde es la 2027. Segundo, el titulo del volcado se deriva del archivo de
entrada, en lugar del que venia fijo del modelo de la ENTREGA 70 de BW Water.

### Que hay

| Archivo | Tamano | Fecha | Contenido |
|---|---|---|---|
| `MODULO COMPLETO.nwd` | 21,4 MB | 08-09-2026 15:00 | Federa `Maqueta Gral.nwc` y `P22-3D-00-001-001_1.nwd`, que a su vez contiene `AREA 6.nwc` |
| `MODULO COMPLETO (nube puntos).nwd` | 6,0 GB | 08-09-2026 | El mismo conjunto con la nube de puntos del levantamiento |
| `Maqueta Gral.nwd` | 12,1 MB | **23-04-2026** | El que el paquete entrega hoy |

**El modelo federado ya incorpora el modelo civil de L&A en revision 1**, el mismo que llego con la
ENTREGA 13. No hace falta copiarlo por separado al dossier civil.

**El modelo que el paquete entrega hoy es de abril**, cinco meses anterior a la subida de 250 milimetros
del modulo, a las cinco laminas civiles en revision 1 y a las cuatro entregas de Van Doorn de agosto.

### Identificacion

El archivo publicado **no declara titulo, autor ni responsable de la publicacion**; solo queda la fecha,
08-09-2026 a las 15:00. El nombre `MODULO COMPLETO.nwd` no lleva codigo de documento ni revision.

Es el mismo reparo que ADASA le hizo a BW Water por el `V14 Taltal.nwd` de la ENTREGA 70. Antes de que
estos modelos salgan hacia el contratista conviene aplicarse la misma vara.

### Contenido, sobre los 4.745 objetos con categoria AutoCAD de los 42.364 del modelo

Los TAG viven en la categoria `AutoCAD` de Plant 3D, en las propiedades `Tag` y `ANF630TAGISO`. Areas
declaradas: 06 con 497 objetos y 00 con 275.

**Doscientos trece objetos de soporte llevan el correlativo sin asignar**, con el signo de interrogacion
como marcador: `SP-01-01?` en 133 objetos, `SP-01-01/?` en 48, `SP-01-01 /?` en 22, mas `SP-01-01/002?`,
`SP-05-01?`, `SP-02-02?` y `SP-07-02?`. El cuadernillo `P22-DWG-06-006-107` define once tipos y 67
soportes con correlativo, de modo que el modelo no permite hoy identificar cual soporte es cual.

**Veintiseis objetos de caneria tienen el TAG incompleto**: once con `?`, siete con
`?-HDPE-DN?-PN10-001`, seis con `PE-HDPE-DN?-PN10-001`, uno con `?-CS-DN75-?-001` y uno con
`?-HDPE-DN?-?-001`. Les falta servicio, diametro o correlativo.

**La fosa de drenajes TK-06-004 no aparece entre los TAG de equipo.** Si estan TK-06-001, TK-09-001 y
TK-09-002. La bomba sumergible BS-06-001 tampoco aparece, lo que es correcto: se omitio por cambio de
ingenieria aprobado, con drenaje por gravedad.

### Lo que este puente no permite verificar

El volcado entrega el arbol, las categorias y las propiedades por objeto, y **no expone la geometria**.
La cota de la fundacion del contenedor en el modelo, que es el punto que interesaba cruzar contra el
sello +5,400, no se puede confirmar por esta via. Queda para verificacion visual en Navisworks o
midiendo sobre el modelo.

No se le exige rigor de modelado a estos archivos. La especificacion tecnica no pide propiedades de
publicacion, conjuntos de seleccion ni objetos tipados, y una observacion sin requisito que la sostenga
es refutable. Los TAG incompletos si son exigibles, porque el modelo se cruza contra listados
aprobados y contra el cuadernillo de soportes.

### Nota sobre el tamano

Los 6 gigabytes de la version con nube de puntos cambian la forma de entrega: el paquete deja de ser
algo que se comprime y se manda por correo. Ese archivo se entrega por enlace, y la Nota Tecnica tiene
que decirlo.

---

## Disposicion y decision tomada

| Documento | Rev | Codigo | Fundamento |
|---|---|---|---|
| `P22-DWG-00-001-001` LAM1 | 1 | **3, por revisar** | El cajetin no declara la revision; el cuadro contradice al `00-002-003` y al `00-002-007`; faltan dos excavaciones |
| `P22-DWG-00-001-001` LAM2 | 1 | **3, por revisar** | El fondo de excavacion del estanque y de la fosa quedo sobre el criterio anterior; falta la seccion de la bomba y la de la fundacion de la cubierta |
| `P22-DWG-00-002-001` LAM1 | 1 | **1, aprobado** | Actualiza el replanteo; sin observaciones |
| `P22-3D-00-002-001` | 1 | ver la seccion de los modelos | Federado dentro de `MODULO COMPLETO.nwd` |

**Las dos laminas del movimiento de tierra se incorporaron igual al paquete de ingenieria vigente**,
por decision del usuario del 09-09-2026. El criterio: sus cifras del contenedor y de la zona CIP son
las unicas dimensionadas sobre el sello vigente, de modo que dejar la revision 0 llevaria al
contratista a excavar 250 mm de mas. Las partidas de excavacion y relleno se miden por unidad de obra
y se pagan segun lo ejecutado, con lo que el riesgo de la cifra referencial es acotado.

Los `LEEME.txt` del paquete estan escritos **en positivo**: declaran que rige el cuadro del
`00-001-001`, que a el se suman las dos excavaciones de la bomba y de la cubierta, y hasta donde se
lleva el fondo de excavacion. No narran el defecto ni mencionan observaciones abiertas con el
proyectista, por decision expresa del usuario: la Nota Tecnica que acompana al paquete no le dice al
contratista que el plano tiene errores. El diagnostico completo vive en este documento y en el correo
a L&A.

## Puntos que van a L&A

Se enviaron como **comentarios sobre los planos**, con la metodologia habitual del stream: cuatro
`_CC_ADASA.pdf` con los recuadros sobre cada lamina, adjuntos al correo
`CORREOS/Septiembre 2026/2026-09-09/`, que va como respuesta al hilo de la carta TT-015. El transmittal
formal queda para cuando L&A reemita.

**Criterio: solo discrepancias entre planos.** Una misma excavacion o una misma cota declarada con dos
valores distintos en dos planos vigentes. La instruccion es siempre la misma, dejar una sola cifra.

**Numeracion: serie unica del envio, OBS-01 a OBS-07**, corrida por el orden en que se leen los planos.
Cada identificador es unico, de modo que la peticion se resume en una linea y las dos discrepancias
que aparecen en dos planos se citan entre si con un "Ver OBS-xx". Los identificadores son de este
paquete, del 09-09-2026, no del historial de cada plano: los OBS-01 a OBS-03 que el `00-001-001` uso
en sus revisiones B y C son otra cosa y quedaron cerrados al aceptarse la revision 0.

| ID | Documento | Un plano dice | El otro dice |
|---|---|---|---|
| OBS-01 | `00-001-001` LAM1 | Item 7: 1,03 m3 | `00-002-007` LAM1: 1,60 m3 |
| OBS-02 | `00-001-001` LAM1 | Item 8: 20,95 m3 | `00-002-003` LAM1: 38,02 m3 |
| OBS-03 | `00-001-001` LAM1 | El cuadro no las recoge | `00-002-002` LAM4: 0,62 m3 y `00-002-007` LAM3: 4,25 m3 |
| OBS-04 | `00-001-001` LAM2 | Secciones A y B: EL. 5,35 | `00-002-002` LAM1: sello +5,350 con emplantillado de 5 cm, fondo 5,30 |
| OBS-05 | `00-001-001` LAM2 | Seccion B: EL. 4,30 | `00-002-004` LAM1: sello +4,305 con mejoramiento de 15 cm, fondo 4,155 |
| OBS-06 | `00-002-003` LAM1 | El cuadro: 38,02 m3 | `00-001-001` LAM1: 20,95 m3. Par de la OBS-02 |
| OBS-07 | `00-002-007` LAM1 | El cuadro: 1,60 m3 | `00-001-001` LAM1: 1,03 m3. Par de la OBS-01 |

Siete observaciones sobre cuatro laminas, todas en naranja: no hay notas menores en este ciclo.

**El correo no repite los comentarios.** Lleva una tabla de cuatro filas, una por plano comentado, con
el rango de identificadores y la materia en una linea; el detalle vive en los recuadros. Son 340
palabras.

## Lo que se descarto, y por que

Estos puntos estan verificados y quedan en el registro interno, pero no se le piden a L&A.

| Punto | Motivo |
|---|---|
| El cajetin de la LAM1 declara REV. 0 | El cajetin ya identifica la revision 1 y las nubes de revision estan puestas. Decision del usuario, 09-09-2026 |
| La fila de la revision 0 dice PARA USO E INFORMACION en ambas laminas | Mismo motivo: control documental, no discrepancia de ingenieria |
| Faltan las secciones de excavacion de la bomba y de la cubierta CIP en la LAM2 | Es omision de dibujo, no discrepancia entre cifras. La cantidad si se reclama, en la OBS-03 |
| El archivo nativo del comprimido falla la verificacion de integridad | Se pedira al acusar la reemision, fuera de este correo |

## Plazo

La reemision esta pedida al **viernes 11 de septiembre**, el mismo dia en que se emite la Nota Tecnica
al contratista. Si algun punto no alcanza para esa fecha, se pidio a L&A avisar cual el mismo miercoles
para resolverlo por separado. Si la reemision no llega, la Nota Tecnica sale igual con las laminas ya
incorporadas y la correccion entra despues como actualizacion del paquete.
