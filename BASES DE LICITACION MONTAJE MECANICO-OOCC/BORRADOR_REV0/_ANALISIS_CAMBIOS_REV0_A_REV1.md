---
titulo: BL Montaje Taltal - verificacion de los cambios de ingenieria entre la Rev 0 y la Rev 1 del paquete
codigo: P22-BL-06-000-001-1
fecha: 2026-09-04
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Que cambio en la ingenieria desde que se licito

Documento interno de respaldo del paquete Rev 1. No se envia a oferentes. Todo lo que sigue se verifico
sobre los archivos, no sobre las cartas de remision: ni Van Doorn ni L&A declaran que cambio en cada
revision.

## 1. El hallazgo que gobierna todo: el modulo subio 250 mm

La fundacion del contenedor del modulo de osmosis inversa sube 250 mm y con ella suben todas las cotas de
conexion. Se verifico por render, porque los planos son vectorizados y no traen capa de texto util.

| Cota | Rev 0 licitada | Rev 1 | Delta |
|---|---|---|---|
| Cara superior de la fundacion del contenedor (`P22-DWG-00-002-003` LAM1) | +6,050 | **+6,300** | +250 mm |
| Sello de fundacion del contenedor | +5,150 | **+5,400** | +250 mm |
| Tie-in P8-001, entrada de salmuera (`P22-DWG-06-006-102` Corte A) | +8,250 | **+8,50** | +250 mm |
| Tie-in P9-001, permeado | +8,593 | **+8,85** | +257 mm |
| Tie-in P9-002, permeado fuera de especificacion | +8,593 | **+8,85** | +257 mm |
| Tie-in P9-003, salida de salmuera | +8,583 | **+8,85** | +267 mm |
| Tie-in 1, 3 y 6 con el Modulo 3 (Cortes D y E) | +6,204 | +6,204 | sin cambio |

Los 250 mm son la altura de plinto que fija la Rev B del `P22-DWG-09-005-001` de BW Water, de modo que la
ENTREGA 12 de L&A y la ENTREGA 16 de Van Doorn son la misma decision aplicada en las dos ingenierias.

**Consecuencia para el paquete:** la tabla de tie-ins de la Seccion 4.3 de la BL Rev 0 publica las cuatro
cotas viejas. Es la cifra con la que el oferente dimensiona los spools de conexion.

## 2. Ingenieria civil, ENTREGA 12 de L&A (carta `067-032-032-COR-TT-013`, 03-Sep-2026)

Cinco de las 18 laminas del dossier civil pasan a Rev 1. Solo la zona CIP mueve cubicacion.

| Lamina | Que cambia | Cubicacion |
|---|---|---|
| `002-002` LAM1, fundacion del estanque | fecha y escala del cajetin | **sin cambio**: 6,03 m3 G25, 0,50 G10, excavacion 4,22 / retiro 5,06 |
| `002-002` LAM4, fundacion de la bomba | fecha del cajetin | **sin cambio**: 0,90 + 0,05 = 0,95 m3, excavacion 0,62 / retiro 0,75 |
| `002-003` LAM1, fundacion del contenedor | **cotas +250 mm**; geometria y armadura iguales | **sin cambio declarado**: 7,16 + 0,36 = 7,52 m3; excavacion 38,02 / retiro 45,62 / relleno 30,03 |
| `002-007` LAM1, zona CIP | fundacion de equipos rediseñada, mas chica y con junta de dilatacion (Sikaflex 1A sobre poliestireno expandido, primer VP-215); **desaparece la Nota Particular 2** que dejaba los pernos de anclaje pendientes del plano vendor | **cambia**, ver abajo |
| `002-007` LAM2, armaduras CIP | armadura renumerada completa, marcas 1201-1204 a 1211-1216 | rediseño real |

Cubicacion de la zona CIP, leida del cuadro del propio plano:

| Item | Rev 0 | Rev 1 |
|---|---|---|
| Fundacion equipos, G25 | 4,13 m3 | **2,63 m3** |
| Fundacion estanque, G25 | 2,88 m3 | 2,88 m3 |
| Perdida 5 % | 0,35 m3 | 0,28 m3 |
| **Total hormigon G25** | **7,36 m3** | **5,80 m3** |
| Emplantillado equipos, G10 | 0,30 m3 | 0,18 m3 |
| Emplantillado estanque, G10 | 0,21 m3 | 0,21 m3 |
| Excavacion | 5,01 m3 | **1,60 m3** |
| Retiro, con 20 % de esponjamiento | 6,01 m3 | **1,92 m3** |

**El bloque de 0,41 m3 que aparece en la Rev 1 no es un elemento nuevo.** Es el total del emplantillado
G10 (0,18 + 0,21 + 0,02 de perdida), que la Rev 0 no totalizaba. L&A lo rotulo "TOTAL HORMIGON G25", que
es un error de rotulo del plano: la tabla que lo contiene es la de hormigones G10.

**Cierre probable del compromiso `INT-11`.** La Nota Particular 2 de la Rev 0 decia que la disposicion y las
dimensiones de los pernos de anclaje quedaban pendientes hasta la entrega de los planos vendor. La Rev 1 ya
no la trae, lo que indica que L&A incorporo la Rev B de BW Water. Falta confirmar los diametros contra las
dos contradicciones registradas (M12 contra M14 en la bomba CIP, M18 contra M10 en el skid de dosificacion).

**Lo que la ENTREGA 12 no re-emitio.** Si el nivel de piso terminado se movio, arrastra cotas que viven en
laminas que no vinieron: `001-001` LAM1 y LAM2 (excavaciones, que porta la cota de plataforma, el sello y la
tabla de movimiento de tierra), `002-001` (implantacion general, con el N.T.N. por zona), `002-004` (fosa) y
`002-006` (drenajes). Refuerza la duda que el cuadro de excavacion de `002-003` no se haya movido pese a que
sus cotas subieron 250 mm.

## 3. Ingenieria mecanica, cuatro entregas de Van Doorn sin procesar

| Entrega | Fecha | Documentos |
|---|---|---|
| E14 | 16-Jun-2026 | isometrias `06-006-010` y `06-006-012` Rev 0, ya presentes en el compilado |
| E15 | 17-Jul-2026 | `06-006-103` y `-104` Rev 1; P&ID `06-009-102` Rev 1; isometrias `-005` y `-011` Rev 1; **Listado de Materiales Rev 1**; Listado de Instrumentos Rev 1 |
| E16 | 25-Ago-2026 | `06-005-103`, `06-006-101` y `06-006-102`, las tres en Rev 1 |
| E17 | 31-Ago-2026 | isometria `-005` **Rev 2** (5 hojas), `-008` **Rev 1** (5 hojas, tenia 4), `-009` **Rev 1**, `-011` **Rev 2** (8 hojas) |

Cambios medidos por render, comparando cada Rev 1 contra su Rev 0:

- **`06-005-103`, plano de montaje del modulo:** la tinta sube 33 % sin desplazamiento global. Los cambios se
  concentran en la planta de la izquierda y en una banda horizontal. Es el plano que porta el nivel del
  modulo.
- **`06-006-101`, cañerias interconexiones planta:** la tinta sube 10 %, con cambios localizados en seis
  zonas de la planta.
- **`06-006-102`, cañerias interconexiones cortes y detalles:** el Corte A se redibuja completo con las cotas
  nuevas, los equipos CIP pasan de bloques esquematicos a detalle real y aparece la nube de revision 1. En el
  Corte D desaparece la valvula `VM-06-010`, que la Rev 0 rotulaba "(PROYECTADA)".

### Listado de Materiales `P22-LI-06-006-102`, Rev 0 contra Rev 1

La cañeria no se mueve: 1 m de DN50, 151 m de DN80, 180 m de DN100 y 3 m de DN150, **335 m en total**, igual
que la Rev 0. Lo que cambia son los accesorios y las bridas.

| Item | Rev 0 | Rev 1 |
|---|---|---|
| Codo 90 grados PE100 DN100 | 40 | 41 |
| Codo 90 grados PE100 DN80 | 32 | 31 |
| Buje de reduccion Super Duplex UNS S32750, 1" x 1/2" | 2 | **5** |
| Spigot saddle with cutter 4" x 1" | 2 | **5** |
| Union adaptador PE100 x Super Duplex 1" | no existia | **3** |
| Flange LJ ASME B16.5 (4", 3", 2", 2 1/2") | 22 + 19 + 4 + 1 | reemplazado |
| Flange suelto para stub end DIN 16963 parte 4, acero galvanizado por inmersion | no existia | **23 + 19 + 4 + 1** |
| Back-up flange HDPE 4" | 1 | eliminado |
| Codo 90 grados **PVC-U** 4" | 1 | **eliminado** |
| Tee reductora **PVC-U** 4" x 2" | 1 | **eliminado** |

Los dos accesorios de PVC-U salen del listado, con lo que se cierra la contradiccion con la BL, que declara
la instalacion 100 % HDPE. El codo de transicion PE100 por Super Duplex ya existia en la Rev 0 con 2
unidades y se mantiene; lo nuevo es la union adaptador.

## 4. Estado de emision de los planos: dos defectos

**El primero, en lo que ya se licito.** El plano `P22-DWG-06-006-103` que viajo en el paquete Rev 0 declara
en su cajetin **"PARA REVISION DEL CLIENTE"**, no para construccion. Su Rev 1 del 17-Jul lo corrige a "PARA
CONSTRUCCION". Los demas planos mecanicos del paquete estan correctos: `005-101` a `005-105`, `006-101`,
`006-102`, `006-104`, `006-105` y `006-106` dicen "PARA CONSTRUCCION"; el PFD y los cuatro P&ID dicen
"REVISION FINAL"; las isometrias Rev 0 dicen "PARA CONSTRUCCION".

**El segundo, en lo que llega ahora.** Siete de las ocho laminas nuevas **no declaran su estado de emision**:
describen el cambio en vez de declarar para que se emite el documento.

| Documento | Descripcion de la fila Rev 1 |
|---|---|
| `06-005-103` Rev 1 | ACTUALIZADO |
| `06-006-101` Rev 1 | ACTUALIZADO DONDE SE INDICA |
| `06-006-102` Rev 1 | ACTUALIZADO DONDE SE INDICA |
| isometria `06-006-011` Rev 2 | ACTUALIZADO DONDE SE INDICA |
| `00-002-002` LAM1 y LAM4, `00-002-003` LAM1, `00-002-007` LAM1 y LAM2, Rev 1 | MODIFICACIONES INDICADAS |
| isometria `06-006-008` Rev 1 | PARA CONSTRUCCION |

El unico respaldo del estado es la carta de L&A, que declara los cinco planos civiles "Para Construccion".
El oferente lee el plano, no la carta.

## 5. Lo que no se puede incorporar

El P&ID `P22-DWG-06-009-102` Rev 1 llego **solo en DWG**, sin PDF. El paquete se distribuye en PDF, de modo
que ese documento se queda en Rev 0 hasta que Van Doorn entregue el ploteo.

---

# Adenda del 04-09-2026: el cotejo contra el paquete realmente licitado

Todo lo anterior se escribio auditando la copia `Bases REV 0` del repositorio. El mismo dia el usuario
aporto el paquete que efectivamente viajo,
`RESPALDO NUBE/ONE DRIVE ADASA/PLANTA DE SALMUERA TALTAL/FASE_06_CONTRUCCION/BASES_OOCC_MECANICA_PIPING`,
124 archivos. El cotejo corrige y agrega.

## Se retracta: al dossier mecanico no le faltaba nada

El paquete licitado lleva las 28 isometrias, el Cuadernillo de Soportes, el diagrama de flujo, los
cuatro P&ID y los seis planos de cañerias. El incompleto era el respaldo del repositorio. **Los 42
archivos comunes entre ambos son byte-identicos**: el repositorio es un subconjunto exacto de lo
enviado, salvo el BL y el Formato, que son ramas divergentes.

## Se confirma: el Formato viajo con precios

`Formato de Presupuesto Obras Civiles, Mecanica y Piping Taltal.xlsx`, editado a mano el 19-06-2026.
Precio en las 41 partidas y, en el Capitulo 4, **como formula visible**: el oferente vio el precio base
y el factor de 1,3 aplicado encima. Defectos propios de esa rama: los TAG `PE-HDPE-DN90-PN10-002` y
`-003` duplicados en dos partidas cotizadas por separado, los codigos `4.3` y `4.7` repetidos, gastos
generales al 35% y utilidad como markup, y sin nota al pie de cubicacion.

## Hallazgo nuevo: cuatro revisiones del mismo plano conviviendo

El dossier civil viajo con **48 laminas donde correspondian 18**. Tres tandas de copiado entre el 11 y
el 23 de junio, ninguna retirando a la anterior, y **sin indice** que declarara la vigencia.

| Revision | Laminas |
|---|---|
| Rev B | 3 |
| Rev C | 16 |
| Rev D | 9 |
| Rev 0 (vigente) | 18 |

Viajaron ademas `P22-DWG-00-003-001` LAM1 y LAM2 y la ET `P22-ET-00-010-103`, que son la cubierta
metalica del sistema CIP, descopada el 18-06-2026, y las revisiones 0 de las dos ET civiles que ya
estaban en revision 1. **33 documentos quedan sin efecto.**

## El BL contractual es una rama editada sobre el Word

`BL_MONTAJE_TALTAL_REV1.docx` del 25-06-2026, editado por Jorge Valdes. Agrega la Seccion 3.2
"Capacidad personal clave requerida" con la calificacion WPS/PQR de los operadores de electrofusion
aprobada por ADASA/ITO antes de intervenir, baja el plazo de construccion de 4 a 3 meses, renombra la
Seccion 4 a "Alcance Montaje Incluido" y suma la Tabla 10.3 y el analisis de riesgos. Su nombre y su
encabezado dicen revision 1; su codigo interno sigue en `-0`.

Regenerar desde el `.md` habria borrado todo eso. El BL Rev 1 generado el 04-09 quedo sin emitir en
`_bl_rev1_no_emitido/`.

---

# Adenda del 04-09-2026: el Formato es la fuente del alcance

Verificacion posterior sobre el Formato de Presupuesto realmente licitado
(`FASE_06_CONTRUCCION/BASES_OOCC_MECANICA_PIPING/2. FORMATO DE LICITACION (A9)/`), que corrige la
premisa con que se habia encuadrado la cubierta y que reordena el criterio de toda la entrega.

## La fundacion de la cubierta SI se cotizo

Partida literal del Formato contractual:

> **4.3** Fundacion de la cubierta metalica del sistema CIP (cobertizo), incluye 24 pernos de anclaje
> F-1554 3/4" preinstalados (colados) y su proteccion anticorrosiva interina.
> **m3 | 2,38 | $961.238,20 | $2.287.746,92**

La **estructura metalica no tiene partida en ninguna parte del Formato**. La unica partida de acero es
la 4.10, Insertos y estructura embebida del contenedor RO, 405,66 kg, que es del contenedor y no del
cobertizo.

De modo que la cubierta no requiere hablar de descope de cara al contratista: la fundacion esta
contratada y se ejecuta integra; el fierro nunca estuvo en el precio. Lo unico que hay que declarar
es el cuidado de los 24 pernos, porque los usara ADASA en la etapa posterior.

## El criterio que ordena la entrega

**El Formato fija el alcance contratado; la ingenieria vigente fija como se construye ese alcance.**

Un plano que viajo en el paquete sin partida asociada nunca fue alcance. Una revision anterior de un
plano cuya partida si existe no altera el alcance, solo el documento con que se construye. Con ese
encuadre la entrega se declara en positivo (que rige) y no queda ninguna necesidad de narrar como se
armo el paquete de licitacion, que es lo que el usuario pidio no exponer.

## Dos partidas bajan de cubicacion

| Partida del Formato | Cotizado | Vigente | Delta a P.U. contratado |
|---|---|---|---|
| 4.2 Fundacion sistema CIP (F2b) | 7,36 m3 | 5,80 m3 | -$1.499.531 |
| 4.6 Excavacion comun en fundaciones y zanjas | 115,10 m3 | 111,70 m3 | -$97.240 |

Costo directo -$1.596.771. Con gastos generales al 35,0% y utilidad al 11,1%, los factores del propio
Formato, del orden de **-$2,4 M** sobre un total de $226.654.489. Ambas se miden por unidad de obra,
por lo que se liquidan segun obra ejecutada y la NT lo declara sin abrir negociacion.

## Las cantidades del Capitulo 1 no cambian

Verificado: el Cuadernillo de Soportes `P22-DWG-06-006-107` y los planos de ubicacion
`P22-DWG-06-006-105` y `-106` estan en **revision 0 en los dos paquetes**, el licitado y el vigente.
Los 67 soportes de las partidas 1.13 a 1.23 se mantienen. Es la partida mas grande del capitulo
(~$32 M) y por eso se comprobo antes de redactar.

La valvula VM-06-010, que desaparece del Corte D del `P22-DWG-06-006-102` Rev 1, **no tiene partida en
el Formato**, por lo que su retiro no tiene efecto economico.

## Defecto del Formato contractual: dos codigos repetidos

El Formato numera **dos partidas 4.3** (Fundacion de la cubierta metalica y Fundacion dinamica bomba
BH-06-001) y **dos 4.7** (Dados de hormigon para soportes a piso y Relleno compactado). Citar "partida
4.3" es ambiguo al liquidar.

El Formato esta suscrito y no se enmienda. La NT lo declara y fija que toda referencia va por numero
mas nombre completo, en la nota y en los estados de pago. Callarlo habria producido la discusion en el
estado de pago, que es peor momento.

## Defecto propio corregido: la hoja Cubicaciones no era citable

La hoja Cubicaciones de la planilla usaba una numeracion corrida `4.1` a `4.14` que se desalineaba del
Formato a partir de la cuarta fila, justamente por los dos codigos repetidos. Quedo re-mapeada a la
numeracion literal del contrato, con el nombre completo de cada partida.

## Las 33 revisiones superadas, para el registro

Se conservan aca porque salen de los documentos externos y ya no viven en ningun artefacto que se
entregue. La hoja `Retirados` de la planilla se reemplazo por una hoja `Vigencia`, que declara en
positivo la revision que rige para cada uno de los 54 documentos del paquete.

- **28 laminas civiles** en revisiones B, C y D: `00-001-001` L1 y L2 en B y en C (4), `00-002-001` en
  C y en D (2), `00-002-002` L1 a L4 en C (4) y L1, L2 y L4 en D (3), `00-002-003` L1 a L3 en C (3) y
  L1 en D (1), `00-002-004` L1 y L2 en C (2) y en D (2), `00-002-006` L1 y L2 en C (2) y L3 en D (1),
  `00-002-007` L2 en B (1), L1 y L3 en C (2) y L1 en D (1).
- **2 ET civiles** en revision 0: `P22-ET-00-010-101` y `P22-ET-00-010-102`, ambas vigentes en
  revision 1.
- **3 documentos de la cubierta**: `P22-DWG-00-003-001` LAM1 y LAM2, y `P22-ET-00-010-103`.

La hoja Vigencia se contrasta contra el arbol real del paquete cada vez que corre el generador
(`comprobar_vigencia_contra_paquete`), y aborta si un codigo declarado no tiene archivo o lo tiene en
otra revision. Ese gate es lo que impide que el defecto de armado se repita.

---

# Adenda del 04-09-2026 (2): diff del Listado de Materiales, con dos retractaciones

Se comparo `P22-LI-06-006-102-0` (licitado) contra `-1` (vigente), hoja `Listado`. **La primera
version de esta adenda contenia dos cifras falsas y se reescribe entera.**

## Movimiento real por familia

| Familia | Rev 0 | Rev 1 | Delta |
|---|---|---|---|
| Cañeria | 335 m | 335 m | 0 |
| Codos | 91 | 91 | 0 |
| Cuplas | 66 | 66 | 0 |
| Tee | 5 | 5 | 0 |
| Reducciones | 4 | 4 | 0 |
| Esparragos | 232 | 232 | 0 |
| **Stub end** | **47** | **47** | **0** |
| Brunch saddle / junta de desarme / codo transicion SD | igual | igual | 0 |
| Flange LJ | 46 | 0 | -46 |
| Flange suelto para stub end | 0 | 47 | +47 |
| Empaquetaduras | 45 | 42 | -3 |
| Buje de reduccion Super Duplex | 2 | 5 | +3 |
| Spigot saddle with cutter | 5 | 8 | +3 |
| Union adaptador PE100 x Super Duplex | 0 | 3 | +3 |
| Accesorios PVC-U (codo 4", tee 4x2) | 2 | 0 | -2 |
| Back-up flange 4" | 1 | 0 | -1 |

**La Nota Tecnica describe esto correctamente.** Lo unico que su resumen omite son las
empaquetaduras (-3). Nada mas.

## Retractacion 1: los stub end NO se duplican

Se habia reportado que pasaban de **47 a 94**. Es falso: son **47 en las dos revisiones**.

**Causa.** El clasificador de familias recorria una lista de patrones y devolvia el primero que
coincidiera por subcadena, con `"STUB END"` **antes** que `"FLANGE SUELTO"`. La descripcion real del
item nuevo es `FLANGE SUELTO, PARA STUB END DIN 16963 PARTE 4...`, que contiene las dos cadenas. Los
47 flange sueltos cayeron en la familia "Stub end" y se sumaron a los 47 stub end reales.

En la Rev 0 el defecto no se manifestaba, porque ahi las bridas se llamaban `FLANGE LJ` y no
contenian la cadena `STUB END`. **Un clasificador puede estar bien en una revision y mal en la otra
justamente porque el proyectista cambio la descripcion**, que es lo que se estaba midiendo.

## Retractacion 2: los esparragos NO cambian

Se habia reportado `ESPARRAGOS PARA STUB-END 5/8" x 170` pasando de **8 a 64**. Es falso. La Rev 0
traia **dos filas duplicadas** de ese item, de 56 y de 8 unidades, que la Rev 1 consolido en una de
64. El total de esparragos es **232 en las dos revisiones**.

## La regla que faltaba

Las dos cifras falsas salieron del mismo trabajo y tienen dos causas distintas, de modo que hacen
falta las dos reglas:

1. **Agregar por familia y contrastar el total** antes de reportar un cambio de cantidad. Corrige el
   caso de las filas consolidadas o re-descritas.
2. **Ordenar los patrones del clasificador de mas especifico a mas generico**, y comprobar que
   ninguna descripcion caiga en dos familias. El agregado por familia **no** detecta este defecto:
   con el clasificador mal, agregar solo consolida el error.

Quien detecto el sintoma fue el usuario, observando que no podia haber tanto cambio en las tuberias
cuando la cañeria no se movio ni un metro. Ver [[feedback_diff_listado_agregar_por_familia]].

## Otras re-descripciones sin cambio real

La `JUNTA DE DESARME` pasa de "JUNTA DE DESARME, FLANGEADA, 150 LB, FF, ASME B16.5" a "JUNTA DE
DESARME" a secas, manteniendo 1 unidad, y una `EMPAQUETADURA` de 4" reordena los campos de su
descripcion.
