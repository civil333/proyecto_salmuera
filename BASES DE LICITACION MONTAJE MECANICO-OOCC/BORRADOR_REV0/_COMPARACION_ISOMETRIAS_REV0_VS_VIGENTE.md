---
titulo: Comparacion del Cuadernillo de Isometrias, Rev 0 contra la revision vigente
fecha: 2026-09-04
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Cuanto cambio realmente la tuberia entre la Rev 0 y la revision vigente

Verificacion pedida por el usuario al observar que el cambio de materiales reportado era
demasiado grande para una cañeria que no se movio ni un metro. **Tenia razon.**

Fuentes: `INGENIERIA DE DETALLE MECANICA/ENTREGAS/COMPILADO REV 0/03_CANERIAS/Cuadernillo_de_isometrias`
(28 hojas) contra el mismo cuadernillo del paquete `INGENIERIA VIGENTE PARA CONSTRUCCION`
(31 hojas). Scripts `script/comparar_isometrias.py` y `script/comparar_bom_isometrias.py`.

## Metodo, y por que no basta la capa de texto

Cada hoja trae unos 700 caracteres de texto y son **solo el cajetin**. La geometria, las cotas y la
Lista de Materiales de la hoja estan **vectorizadas**: entre 1.400 y 4.600 vectores por lamina, A3
apaisado de 1191 x 842 pt, `rotation = 0`. Todo lo que se afirma aca sobre contenido sale de render,
no de `get_text()`.

**Las hojas se corrieron entre revisiones y hubo que alinearlas por firma de contenido**, no por
numero. En `P22-DWG-06-006-011` la revision nueva inserta una lamina en la posicion H.2 y desplaza
las seis siguientes: la H.2 de la Rev 0 es la H.3 vigente. Comparar H.N contra H.N habria producido
un diff enteramente falso.

## Resultado: siete de once isometrias no cambiaron en absoluto

| Isometria | Rev 0 | Vigente | Estado |
|---|---|---|---|
| P22-DWG-06-006-001 | 0 (2 h) | 0 (2 h) | **identica byte a byte** |
| P22-DWG-06-006-002 | 0 (4 h) | 0 (4 h) | **identica byte a byte** |
| P22-DWG-06-006-003 | 0 (1 h) | 0 (1 h) | **identica byte a byte** |
| P22-DWG-06-006-004 | 0 (1 h) | 0 (1 h) | **identica byte a byte** |
| P22-DWG-06-006-006 | 0 (1 h) | 0 (1 h) | **identica byte a byte** |
| P22-DWG-06-006-010 | s/r (1 h) | s/r (1 h) | **identica byte a byte** |
| P22-DWG-06-006-012 | s/r (1 h) | s/r (1 h) | **identica byte a byte** |
| P22-DWG-06-006-005 | 0 (4 h) | **2** (5 h) | 4 hojas cambian, 1 nueva |
| P22-DWG-06-006-008 | 0 (4 h) | **1** (5 h) | 4 hojas cambian, 1 nueva, 1 movida |
| P22-DWG-06-006-009 | 0 (2 h) | **1** (2 h) | 2 hojas cambian |
| P22-DWG-06-006-011 | 0 (7 h) | **2** (8 h) | 7 hojas cambian, 1 nueva, **6 movidas** |

Once de las diecinueve hojas del cuadernillo estan intactas. Las tres hojas nuevas son `005 H.5`,
`008 H.4` y `011 H.2`.

## Los cambios de la Lista de Materiales son menores

Comparando el cuadro de materiales de cada par alineado, con la diferencia normalizada contra el
ruido de trazo del propio cuadro. **Calibracion:** el par `011 H.6 -> H.7` se verifico identico a
ojo y sirve de control; su 1,19% de pixeles distintos es ruido de re-exportacion (cambia el grosor
del texto en negrita y de las lineas de grilla, no el contenido).

Ejemplo representativo, `006-008 H.1`, leido sobre el render:

| ID | Rev 0 | Vigente |
|---|---|---|
| 6 | ESPARRAGOS 5/8" x **216**, cant. **8** | ESPARRAGOS 5/8" x **166**, cant. **4** |
| 7 | ESPARRAGOS 5/8" x **166**, cant. **8** | ESPARRAGOS 5/8" x **216**, cant. **8** |
| 8 | EMPAQUETADURA 3", cant. **4** | EMPAQUETADURA 3", cant. **3** |

Los dos largos de esparrago **intercambian su orden** en la lista, uno baja de 8 a 4 unidades y la
empaquetadura baja una unidad. Es del orden de lo que cambia en las demas hojas: reordenamientos y
ajustes de una o dos unidades, coherentes con las tres hojas nuevas.

## La brida: misma pieza, y el material lo declara solo el Listado

**Retractacion.** La primera version de este informe reporto que las isometrias y el Listado pedian
bridas distintas. **Es falso.**

| | Descripcion |
|---|---|
| Isometrias, las dos revisiones | `FLANGE LJ, 150 LB, FF, ASME B16.5` |
| Listado Rev 1 | `FLANGE SUELTO, PARA STUB END DIN 16963 PARTE 4 EN ACERO GALVANIZADO POR INMERSION. CARA PLANA Y PERFORACIONES SEGUN ASME B16.5 CLASE 150` |

**LJ es Lap Joint, que es exactamente un flange suelto.** Las perforaciones son ASME B16.5 clase 150
en los dos documentos, y el stub end DIN 16963 parte 4 que el Listado referencia ya esta
especificado con esa misma norma en la propia isometria. Es la misma pieza.

Lo unico que la revision 1 del Listado incorpora es **el material: acero galvanizado por inmersion**,
que las isometrias no declaran. Ese es el hallazgo real, y es mucho menor: no hay riesgo de comprar
la pieza equivocada, hay un requisito de material que vive en un solo documento.

El conteo por OCR sobre las 59 hojas se mantiene como dato (15 hojas Rev 0 y 13 vigentes dicen
`FLANGE LJ`, ninguna dice `FLANGE SUELTO`), pero **no significa contradiccion**: significa que las
isometrias usan la sigla del rubro y el Listado la escribe desarrollada.

**Decision del usuario:** el paquete declara que es la misma pieza y que para el material rige el
Listado Rev 1. Incorporado a la NT, el indice, el LEEME y la planilla.

**Leccion de metodo:** antes de afirmar que dos documentos piden cosas distintas, leer la
descripcion completa de ambos y expandir las abreviaturas del rubro. Una sigla sin traducir produjo
el tercer hallazgo sobredimensionado de la jornada, despues de los esparragos y los stub end.

## Otros dos puntos

**El estado de emision es inconsistente entre hojas de la misma revision.** En `006-011`, la H.1
declara la Rev 2 como `ACTUALIZADO DONDE SE INDICA` y la H.3 la declara `PARA CONSTRUCCION`.

**El COMPILADO REV 0 trae los 28 archivos nativos `.dwg`; el paquete vigente lleva solo PDF.** Es
decision de armado y es razonable no entregar nativos al contratista, pero queda registrado.

## Que queda pendiente de decidir

El hallazgo de la brida **no se ha llevado ni a la Nota Tecnica ni a ninguna comunicacion**, por
instruccion del usuario de reportar primero. Lo que corresponde evaluar es una consulta a Van Doorn
antes de que el contratista emita ordenes de compra de bridas.
