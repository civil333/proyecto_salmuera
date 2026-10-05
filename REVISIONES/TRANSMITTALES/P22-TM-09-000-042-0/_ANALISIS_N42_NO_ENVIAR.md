---
titulo: Análisis interno del Transmittal N42 — E96, E97, E99 y E100
fecha: 2026-10-05
estado: INTERNO
type: analisis
project: salmuera-taltal
second_brain: skip
---

# Análisis interno del Transmittal N42

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

El detalle de cada documento, con su evidencia, vive en el ledger de su entrega. Este archivo solo registra la disposición y las decisiones que la fijaron.

| Entrega | Llegó | Vence (Cl. 37.2) | Ledger |
|---|---|---|---|
| E96 (cuatro documentos) | 22-Sep | 1-Oct, vencida | `ENTREGAS_BWWATER/ENTREGA 96/_LEDGER_COMENTARIOS.md` |
| E97 (HMI) | 23-Sep | 2-Oct, vencida | `ENTREGAS_BWWATER/ENTREGA 97/_LEDGER_COMENTARIOS.md` |
| E99 (addendum de izaje) | 29-Sep | 8-Oct | `ENTREGAS_BWWATER/ENTREGA 99/_LEDGER_COMENTARIOS.md` |
| E100 (Valve List) | 1-Oct | 13-Oct | `ENTREGAS_BWWATER/ENTREGA 100/_LEDGER_COMENTARIOS.md` |

## Disposición

| Documento | Rev | Sub. For | Código | Determinante |
|---|---|---|---|---|
| GA of Module Lifting from Top (yugo) `P22-DWG-09-005-019`, página 13 del addendum, hoja 1 de 3 | A | fuera del formulario | 3 | Arreglo general que no permite fabricar: sin uniones, material, pesos ni datos de eslingas; faltan las hojas 2 y 3 |
| UHPRO Structural Calculation Report - Addendum `P22-CD-09-005-003` | A | IFA | 3 | Solo orejas: el marco y los esquineros sin verificar; código del Criterio de Diseño y tres marcas de revisión |
| Maintenance Lifting Points Layout and Details | A | IFA | 3 | Un solo izaje del motor, sin viga carrilera ni turbos (ET Sección 7, pág. 28) |
| GA of Antiscalant Dosing Tank | E | IFA | 2 | Fila LM en 3' 7" contra la vista 1 en 864 mm, tercer ciclo; ADASA declara 34" |
| Piping Layout | E | IFA | 1 | Las tres condiciones del N36 y su NOTE-01 cerradas |
| Valve List | 0 | IFC | 1 | La condición del N39 se cumple: la Rev 0 declara la VM-09-065 en PVC sobre la línea 316L |
| PLC/LCP FAT Procedure - Hardware | 0 | IFC | 1 | OBS-01 y OBS-02 del N38 cerradas |
| HMI Display Screenshot | 0 | IFC | 1 | OBS-01 del N38 cerrada |

**Recuento: 4 Código 1, 1 Código 2, 3 Código 3, ocho documentos. Veredicto: 3.**

## Decisiones que fijaron la disposición

1. **Reclamo del yugo con cita del correo del 15-Sep** (Luis, 5-Oct). Va en el resumen ejecutivo, en la Sección 2.1, en la Sección 3, en los cuadros OBS-02 y OBS-04 del plano del yugo y en la primera viñeta del correo.
2. **Reemisiones: solo levantamiento de comentarios anteriores** (Luis, 5-Oct): *"para las revisiones E debiésemos estar revisando que los comentarios hechos se levantaron, no incluir más nuevos a no ser que sean errores garrafales que no vimos antes"*. Con esa regla, el rótulo `CP-PVC-DN150-09-022` del Piping Layout no se emite y el plano queda en Código 1. La Sección 2 abre con la tabla de levantamiento de cada comentario anterior.
3. **El plano del yugo se codifica aparte** (Luis, 5-Oct: "¿por qué no veo el plano del Yugo en el transmittal?"). Aunque no está en el formulario, tiene código y revisión propios. Dentro del addendum el reclamo no se veía. Ahora tiene subsección 2.1, fila en el Response Summary y PDF anotado propio.
4. **Sin fecha para el paquete de izaje en el transmittal ni en el correo.** Queda a decisión de Luis.
5. **Sin el patrón de tres días** en la Sección 3 (Luis, 5-Oct).
6. **Verificación adversarial (agente con contexto fresco, 5-Oct).** Bajó la Valve List de Código 3 a Código 1: el N38 aceptó la línea 316L por disponibilidad de una reducción, y ninguna fuente exige la válvula en acero. Además pidió tensión de diseño y largo de eslinga en vez de WLL, porque el 11-Sep ADASA dejó la selección al contratista de izaje. Corrigió la cita del correo del 15-Sep, que no dice "cada uno con su diseño". Hizo que el cuadro de los puntos de izaje hable de "pumps" en plural, como la ET y el pendiente de la línea 09-001 del N36. Mantuvo el Piping Layout en Código 1.
7. **Perfiles nacionales, empalmes y combinaciones del yugo** (Luis, 5-Oct):
   - el W10x49 se consigue solo importado, así que se pide su equivalente soldado nacional IN o HN, con calidad según NCh203;
   - se piden el detalle de empalme de los largueros de 12.776 mm, las uniones de esquina y las vigas intermedias;
   - el addendum es ASD sin combinación declarada, así que se exigen como mínimo las combinaciones NCh3171 de la sección D del Criterio aprobado, más los factores 1,35D y 2,0D de su sección F.

   Las fuentes quedaron en `BASES TECNICAS/REFERENCIAS ACERO CHILE/`. El plano del yugo pasa a 5 observaciones.
8. **Viga intermedia, torsión y desangulación del yugo** (Luis, 5-Oct): *"no hay vigas intermedias, por lo que no hay ninguna certeza del comportamiento torsional de la maniobra o del pandeo de las vigas de 12 metros"*. El plano gana un cuadro propio sobre la vista en planta, con flecha al punto medio del larguero, y pide al menos una viga intermedia a medio largo. El cuadro de empalme deja de mencionar las vigas intermedias. El addendum gana un cuadro espejo (OBS-04, al pie de la página 4) que pide modelar el marco con esa viga y demostrar torsión, desangulación y pandeo. Plano del yugo con 6 observaciones, addendum con 4; recuento sin cambio. El matiz del modo traslacional queda en el ledger de la E99.

## Hallazgos internos que no se emiten

- Piping Layout Rev E: el rótulo de la línea 022 contra la Line List Rev 2, y desaparece `DA-SSD-DN65-09-009`.
- Valve List Rev 0: la VM-09-072 pasó a SS316L sin que se pidiera, coherente con su unión soldada a la línea de acero.
- Addendum: λ = 1,67 en fluencia contra el FS 2,0 del Criterio, sin efecto, porque con 2,0 todo queda bajo 0,65. Filetes del plano mayores que los del cálculo, del lado conservador. Formulario con nombre de archivo 0098.
- La ET cita "BAE Cl. 41" para el marcado del embalaje, pero el procedimiento vive en la Cláusula 38. El N42 cita la 38.

## Archivos

- Transmittal: `P22-TM-09-000-042-0_TRANSMITTAL.md` (fuente única). `crear_transmittal.py` lo lee y genera el Word con template-adasa. El PDF sale de Word con `_HERRAMIENTAS/exportar_pdf_word_mac.sh`.
- Cuadros: `COMENTARIOS/agregar_comentarios_*.py`. La ubicación en zona libre y el dibujo en láminas rotadas están en `COMENTARIOS/_cajas_fijas.py`.
- Anti-ia: `.anti-ia-2026-10-07/veredicto.md`, VERDE.
- Correo: `CORREOS/Octubre 2026/2026-10-07/`.
