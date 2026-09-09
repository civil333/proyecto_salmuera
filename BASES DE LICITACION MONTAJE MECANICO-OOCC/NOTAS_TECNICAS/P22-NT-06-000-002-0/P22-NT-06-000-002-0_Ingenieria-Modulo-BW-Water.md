---
titulo: Nota Técnica P22-NT-06-000-002-0, Ingeniería del módulo RO de BW Water
codigo: P22-NT-06-000-002-0
revision: 0
fecha: 2026-09-09
destinatario: Equipo de proyecto de Aguas Antofagasta
emisor: Aguas Antofagasta S.A.
estado: BORRADOR
---

# Objeto de esta nota

Esta nota acompaña al dossier `INGENIERIA MODULO BW WATER` y explica qué contiene, con qué criterio
se eligió la revisión de cada documento y qué queda abierto. Se dirige al equipo de proyecto de Aguas
Antofagasta.

El dossier reúne **71 documentos de ingeniería del módulo de osmosis inversa**, todos en la última
revisión que ADASA aprobó, repartidos en seis carpetas por especialidad. Ocupa 340 megabytes.

Esta nota no modifica el Contrato ni ninguno de sus anexos, y tampoco constituye una emisión de
ingeniería. Es un instrumento de trabajo interno: pone en una sola carpeta lo que hoy vive repartido en
noventa carpetas de entrega.

# Contenido del dossier

**0. CONTROL DE CAMBIOS.** Una copia de esta misma nota en PDF, de modo que el dossier viaje siempre
con el documento que lo explica.

**1. GENERAL**, un documento. La hoja de datos del contenedor del módulo, que fija sus dimensiones y su
peso de operación.

**2. PROCESO**, diecinueve documentos. El diagrama de flujo y el P&ID, el cálculo de proceso, la
filosofía de control, los listados de líneas y de consumos, y las trece hojas de datos de los equipos:
el sistema UHPRO, la bomba de alta presión, la bomba CIP, la dosificadora de antiescalante, los dos
filtros de cartucho, los dos turbocargadores, los estanques CIP y de antiescalante, el calentador del
estanque CIP y el mezclador estático.

**3. MECANICA**, dieciséis documentos. El cálculo estructural del bastidor con sus criterios de diseño,
el cálculo térmico del aire acondicionado, el plano de necesidades civiles y cargas, los planos de
disposición de equipos y de cañerías, los puntos de conexión, los siete planos generales de los skids y
estanques, y los listados de equipos y de válvulas.

**4. CANERIAS**, dos documentos. Las especificaciones de cañerías y de pintura.

**5. ELECTRICIDAD**, once documentos. El diagrama unifilar, los planos de puesta a tierra, de bandejas
portacables y de obras de poder, las hojas de datos de los auxiliares eléctricos, los cables, la
bandeja, la canalización y el tablero local, y los listados de cargas y de cables de poder.

**6. CONTROL E INSTRUMENTACION**, veintidós documentos. La arquitectura del sistema de control, el plano
exterior y el esquemático del tablero PLC, el plano de ubicación de instrumentos, la hoja de datos del
PLC y la interfaz, los listados de entradas y salidas, de instrumentos, de cables, de transferencia
Modbus, de alarmas y enclavamientos, las diez hojas de datos de instrumentos, las pantallas de la
interfaz y la carta de secuencias.

Cada carpeta lleva un `LEEME.txt` con su listado y lo que conviene mirar de esa especialidad.

**Todo el dossier es PDF.** BW Water no ha entregado ningún listado en formato editable, de modo que los
listados de instrumentos, de líneas, de válvulas, de equipos y de entradas y salidas están en PDF y no
hay otra versión disponible. Los archivos nativos de AutoCAD que el proveedor sí entregó de algunos
planos quedan en su carpeta de entrega y no viajan en este dossier.

Los nombres de archivo se uniformaron a `código_revisión título`. El proveedor usa seis grafías
distintas para la revisión, que van desde `_A` hasta `_REV.B` pasando por `RevA` sin separador, y con
ellas el dossier no se puede ordenar. El código y la revisión de cada archivo son los del cajetín del
documento.

# Cómo se eligió la revisión de cada documento

El dossier lleva, para cada documento, **la última revisión que ADASA aprobó en Código 1 o Código 2**.
La fuente es el Registro Maestro de Entregables `P22-IT-06-000-002-0`, que es donde vive el estado de
cada entregable al cierre del último transmittal, el N38 del 3 de septiembre.

De los setenta y un documentos, **cincuenta y nueve están en Código 1** y **doce en Código 2**. En
ingeniería no hay ningún documento en Código 3 ni en Código 4, de modo que no hubo que elegir entre una
revisión aprobada y una posterior rechazada.

Un documento en Código 2 rige y hay que leerlo entendiendo que va a cambiar en el detalle que se indica.
La Sección siguiente los lista uno por uno.

## Cinco documentos donde el registro y el documento no coinciden

Al armar el dossier aparecieron cinco discrepancias entre el Registro Maestro y el documento emitido. En
todas manda el documento, que es el que el equipo va a tener en la mano, y el registro se corrige por
separado.

| Documento | El registro dice | El documento dice |
|---|---|---|
| Especificación de cañerías | `P22-ET-09-005-001` | `P22-ET-09-006-001` |
| Especificación de pintura | `P22-ET-09-005-002` | `P22-ET-09-006-002` |
| Hoja de datos del estanque CIP | `P22-ET-09-009-010` | `P22-ET-09-009-009` |
| Hoja de datos del estanque de antiescalante | `P22-ET-09-009-011` | `P22-ET-09-009-010` |
| Hoja de datos del calentador del estanque CIP | `P22-ET-09-009-014` | `P22-ET-09-009-011` |

Las dos especificaciones están codificadas en la disciplina de cañerías y el registro las anota en la de
mecánica. Las tres hojas de datos de estanques llevan el correlativo corrido en uno: el título y la
entrega del registro calzan exactos con el archivo, y lo único desplazado es el número.

**Los dos planos generales de los turbocargadores son revisión A.** El registro los anota en revisión B.
Llegaron una sola vez, en la entrega 14, y su cajetín dice *Revision No.: A*. No existe una revisión B
en el repositorio, de modo que el dossier lleva la única que hay.

**El plano de puntos de conexión aparece bajo una entrega que no existe.** El registro lo declara en la
entrega 87, que es el hueco de la serie del proveedor, y el archivo está en la entrega 88.

# Los doce documentos aprobados con observaciones

Estos son los documentos que rigen y que todavía van a cambiar. Se indica qué queda abierto en cada uno,
tal como quedó en el transmittal que lo dispuso.

| Documento | Rev. | Qué queda abierto |
|---|---|---|
| Cálculo de proceso | B | Completar el cálculo de consumo específico de energía y verificar la tasa de recuperación |
| Hoja de datos de la bomba CIP | B | Se aceptó el cambio de variador a partida directa, y queda pendiente la compatibilidad del motor |
| Hoja de datos del estanque de antiescalante | B | Observaciones menores de la hoja |
| Informe de cálculo estructural del bastidor | B | El cálculo se acepta. El PDF es una concatenación duplicada de unos 58 megabytes y la hoja de comentarios omite el texto original de ADASA |
| Plano de necesidades civiles y cargas | B | Las dos partes de la observación del transmittal N16 siguen abiertas: el peso total del contenedor modificado, y la composición del peso de operación del bastidor, donde el marco no aparece en ninguna fila |
| Plano de disposición de cañerías | D | Tres puntos por segundo ciclo: el cuadro de conexiones no cubre las siete líneas del sistema CIP y sus cotas no declaran nivel de referencia, falta la clase de brida en las terminaciones de antiescalante y CIP, y la lámina muestra dos gabinetes rotulados LCP sin TAG |
| Plano general de la bomba dosificadora de antiescalante | C | La reconciliación de las reacciones de anclaje no cierra por segundo ciclo: la fuerza vertical por perno es el doble del cociente de la fuerza total entre los diez pernos |
| Plano general del estanque de lavado CIP | B | El cuadro de boquillas no concuerda con la hoja de datos del estanque CIP: la abertura superior figura como manhole de 533 milímetros donde la hoja de datos declara handhole DN300, y dos boquillas no tienen equivalente |
| Plano general del estanque de antiescalante | C | Dos puntos menores del detalle nuevo: el agujero de anclaje está acotado en 14 milímetros y media pulgada para un perno M12, y la fila de marcación de nivel no lleva tamaño ni cota |
| Esquemático del tablero PLC | B | La señal de marcha del calentador CIP no tiene borne en ninguna lámina de entradas digitales, y la lista de materiales sigue nombrando el terminal de operador 2711P-T10C21D8S en lugar del modelo que ADASA declaró vinculante |
| Plano de ubicación de instrumentos | D | El bloque de revisiones repite la misma descripción en sus cuatro filas y la fila de la revisión C fue sobrescrita, de modo que no se distingue qué cambió en cada emisión |
| Pantallas de la interfaz de operación | C | Dos transmisores de presión quedaron cruzados entre la pantalla de primera y de segunda etapa, y se invierten al emitir la revisión 0 |

Hay un punto que no es una observación del documento y conviene tener presente al leer el cálculo
estructural: **el informe no lleva endoso de un profesional inscrito en Chile**. BW Water lo comprometió
por escrito el 20 de mayo, el 16 de junio y el 30 de junio, y el 17 de agosto informó que el ingeniero
que lo certificaba no está disponible. La revisión 0 del informe lleva solo iniciales internas.

# Lo que BW Water aún no entrega

El Registro Maestro marca seis entregables de ingeniería de la Sección 7 de la Especificación Técnica
como no recibidos. No están en el dossier porque no existen.

| Entregable | Referencia |
|---|---|
| Memoria de cálculo sísmico según NCh 2369 | Especificación Técnica, Sección 7, página 28 |
| Análisis de flexibilidad de líneas de alta presión | Especificación Técnica, Sección 7, página 28 |
| Maqueta 3D interoperable con la suite de Autodesk | Especificación Técnica, Sección 7, página 28 |
| Isometrías de líneas de alta presión | Especificación Técnica, Sección 7, página 28 |
| Vigas carrileras y puntos de izaje internos | Especificación Técnica, Sección 7, página 28 |
| Sistema de comunicación Modbus TCP y mapa de memoria | Especificación Técnica, Sección 5.4 |

La especificación de válvulas e instrumentos con marca y modelo figura como entrega parcial: las hojas
de datos individuales están en el dossier y el documento consolidado que pide la Sección 7 no se ha
emitido.

# El modelo tridimensional

El modelo federado del módulo existe, es el `P22-DWG-09-005-007` en revisión B, y está aprobado en
Código 2. No viaja en este dossier porque es un archivo de Navisworks y el dossier lleva solo formatos
de lectura. Se entrega por enlace a quien lo pida.

Sobre ese modelo hay un punto abierto que conviene conocer antes de usarlo para coordinación: la hoja de
comentarios de su última revisión declaró corregidos cincuenta y siete TAG de soportes de cañería que no
se tocaron, y hoy son setenta y dos. Los TAG de válvula sí cerraron.

# Vigencia de la documentación

La tabla siguiente lista los setenta y un documentos del dossier, uno por fila, con la revisión que
rige, la entrega en que llegó, el transmittal que la dispuso, el código de respuesta de ADASA y la
carpeta donde se encuentra. Ante cualquier duda de vigencia prevalece esta tabla.

> La tabla **no se transcribe en este archivo**: el generador la importa de
> `BORRADOR_REV0/script/vigencia_bw.py`, que produce `catalogar_ingenieria_bw.py` desde el Registro
> Maestro. Ese mismo catálogo alimenta al constructor del dossier y al gate que contrasta lo declarado
> contra el árbol real, de modo que hay una sola fuente y no tres.

Esta nota refleja el estado al cierre del transmittal N38, del 3 de septiembre de 2026. Cada transmittal
nuevo puede mover la revisión de uno o más documentos, y entonces el dossier se reconstruye corriendo
los dos scripts.
