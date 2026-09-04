---
titulo: Correo conjunto por las inspecciones 3 y 4 del 13 y 14 de agosto
codigo: Recordatorio de jornadas y revisiones vigentes del paquete de inspección
fecha: 2026-08-12
estado: ENVIADO
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-08-12
---

# Correo conjunto — inspecciones 3 y 4, 13 y 14 de agosto

**Estado: ENVIADO** (12-Ago-2026, miércoles).

| Campo | Valor |
|---|---|
| Archivo | `2026-08-12_BV-Inspections-3-and-4.docx` · una página · inglés |
| Para | Eduardo Yamauchi, Magdier Arias (BW Water); Carlo Montecinos (Bureau Veritas) |
| CC | Mohd Adnin Bin Zulkaflee, Muhammad Fadhil Bin Abdul Wahid (BW Water); Ahmad Hazwan, Wan Mohd Adli W Yahya, Emylia Rosli (Bureau Veritas); Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero (ADASA) |
| Asunto | RE: 25007 TALTAL - Witness inspections 3 and 4, 13 and 14 August - governing revisions |
| Cadena | **Reply al hilo del `Request to witness inspection 003`.** Cadena de las jornadas, separada de la de transmittals, donde va el TM N32 |
| Adjuntos | `P22-BA-09-000-010_0 HP and LP Pressure Test Procedure.pdf` y `P22-BA-09-000-011_0 Painting Procedure.pdf` |
| Por enlace | El paquete completo, en la misma dirección publicada el 21-Jul |
| Script | `crear_correo_bv_jornada_13_14ago.py` |

Aplica la **excepción del correo conjunto**: se nombra a BW Water aunque Bureau Veritas esté entre los destinatarios.


## Envío

**ENVIADO el miércoles 12-Ago-2026 a las 15:20**, respaldo en `CORREO INSPECCION 13 Y 14.pdf`.

Asunto real: *"TALTAL - Witness inspections 3 and 4, 13 and 14 August - governing revisions"*.

**Distribución real, distinta de la que declaraba el script.** To: Eduardo Yamauchi y Magdier Arias (BW Water), Carlo Montecinos (Bureau Veritas). CC: Mohd Adnin Bin Zulkaflee, Lokman Hakim Bin Mat y Muhammad Farih Awang (BW Water), Megan Karin Almarza (Bureau Veritas Chile). No fueron Ahmad Hazwan, Wan Mohd Adli ni Emylia Rosli, y **el equipo interno de ADASA quedó sin copia**, que es el mismo patrón del reclamo del 25-Jul. Conviene reenviarlo a Gutiérrez, Guevara y Pellejero.

**El correo viajó completo.** Verificado sobre el respaldo: están los dos bloques de revisiones vigentes, el color de terminación, el certificado del ensayo, la tabla de las siete revisiones reemplazadas, la línea de adjuntos, el enlace del paquete y las tres peticiones de cierre.

## Cuerpo

1. **Recordatorio con las dos inspecciones separadas.** Inspección 3 el jueves 13, ensayo de presión de la cañería de alta; inspección 4 el viernes 14, preparación de pintura. Las dos de 9:00 a 17:00 en BW Water Penang, bajo el Inspection Request Form 003.
2. **Revisiones que gobiernan, una viñeta por día.** Para la 3, el procedimiento vigente es la Rev 0 y el paquete tiene la Rev D; se recuerda que el ensayo de alta es Punto de Detención de la fila 5.2 del ITP. Para la 4, el procedimiento vigente es la Rev 0 y el paquete tiene la Rev B, cuyo formulario declara `40-75 µm` en una celda y `50-80` en la fila de aceptación del mismo formulario. **El perfil que se acepta el 14 es de 50 a 80 micrones.**
3. **Color de terminación como valor vinculante.** `RAL 5012 Luminous Blue`, que fija la Painting Specification Rev C para el soporte estructural dentro del contenedor. Se dice que el formulario de la Rev 0 declara otro y que la corrección está en curso, sin entrar en el detalle, que vive en el TM N32.
4. **Certificado del ensayo de presión.** La fila 5.2 del ITP exige informe con gráfico presión contra tiempo. La cláusula 5.8.1 del procedimiento nombra un informe que ningún formulario del documento produce. Se pide identificarlo por número y revisión y tenerlo disponible el 13.
5. **Tabla de las siete revisiones repuestas** y el enlace del paquete, que se repite en el cuerpo.
6. **Tres peticiones:** confirmación de asistencia; un formulario y un resultado por inspección; y el formulario firmado más el informe de Bureau Veritas de cada día por separado, en el formato del `BVM-IR001-28072026`.

No propone reunión y no reitera el reclamo por los registros del 7 de agosto, que vive en el correo del 10-Ago y sigue abierto.

## Reposición del paquete, ya ejecutada

`PROGRAMA y CONTRATO/HITO BUREAU VERITAS/PAQUETE_INSPECCION_BV/`. La carpeta no se movió ni se renombró: tiene enlace publicado vivo desde el 21-Jul. Se reemplazaron siete archivos dentro y los superados quedaron en subcarpetas `_superseded/`, que es el patrón que la carpeta ya usaba para el Datasheet del PLC y HMI.

| Documento | En el paquete | Vigente | Origen |
|---|---|---|---|
| Painting Procedure `P22-BA-09-000-011` | Rev B | **Rev 0** | Submittal 25007-0075 |
| HP and LP Pressure Test `P22-BA-09-000-010` | Rev D | **Rev 0** | Submittal 25007-0075 |
| PMI Procedure `P22-BA-09-000-006` | Rev A | **Rev 0** | Submittal 25007-0075 |
| Visual Procedure `P22-BA-09-000-008` | Rev A | **Rev 0** | Submittal 25007-0075 |
| RO Vessel Hydrostatic Test `P22-BA-09-000-009` | Rev C | **Rev 0** | Submittal 25007-0072 |
| GA of SWRO System Skid `P22-DWG-09-005-008` | Rev A | **Rev B** | Submittal 25007-0072 |
| Plant Control Philosophy `P22-BT-09-009-001` | Rev E | **Rev 0** | Submittal 25007-0072 |

Recuento: 43 archivos antes, 50 después. Ninguno se perdió; los siete superados están en `_superseded/`. La revisión del cajetín de los siete repuestos se verificó abriendo cada PDF.

**Quedaron fuera del reemplazo** el `Alarm and Interlock List` y el `Control and Sequence Chart`, que llegaron en Rev 0 el 11 de agosto en el submittal 25007-0073 y que ADASA todavía no revisa. Reponerlos en el paquete del tercero inspector sería declararlos aprobados.

## Verificación de fuentes

| Afirmación | Fuente |
|---|---|
| Fecha, horario, lugar y alcances de las dos inspecciones | `AQ-QAM-F027 Inspection Request (003)`, en `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 02/` |
| El formulario 003 cubre los dos días en una sola casilla y no existe un Request 004 | Barrido del repositorio: solo hay formularios 002 y 003 |
| Perfil `40-75 µm` en el formulario de la Rev B contra `50-80` en la fila de aceptación | PDF de la Rev B del paquete, página 11, leído directamente |
| Perfil `50-80` en los dos lugares en la Rev 0 | Rev 0 del submittal 25007-0075, páginas 9 y 11 |
| `RAL 5012 Luminous Blue` para el soporte estructural | Painting Specification `P22-ET-09-006-002` Rev C, ítem 4 |
| El ensayo de alta es Punto de Detención con informe de gráfico presión-tiempo | ITP `P22-BA-09-000-004` Rev 0, fila 5.2 |
| Revisiones vigentes de los siete documentos | Master Deliverable Register `P22-IT-06-000-002-0` |
| Enlace del paquete | `crear_correo_bv_weekly_inspection.py` del 21-Jul-2026 |

## Contexto Interno (No enviar)

- **El enlace del paquete se envió el 21-Jul solo a Luis Rodrigo Arcila**, de Bureau Veritas Chile, con BW Water en copia. Los que atienden en Penang no estaban entre los destinatarios, así que no se puede suponer que lo tengan. Por eso el enlace se repite en el cuerpo y los dos procedimientos del caso van adjuntos.
- **El correo cierra `BV-09`** del registro de compromisos, que pedía reemitir al inspector la Rev 0 del PMI. Se cierra al enviar, no antes.
- **El color se declara como valor vinculante y no se pregunta.** El formulario de la Rev 0 dice `RAL 5010`; decirlo así, sin abrir la discusión, es lo que corresponde con la fecha de fabricación encima. El detalle documentado vive en el TM N32.
- **La inspección de preparación no mide color**, de modo que el punto no bloquea el día 14; el riesgo es la capa de terminación.
- **El Valve List del paquete tiene el nombre en Rev D y el cajetín en Rev A.** Es un defecto de portada del proveedor, ya identificado, y no toca estas dos inspecciones: no se menciona aquí para no diluir el correo.
- **Los tres procedimientos de ensayos no destructivos no se envían.** Llegaron ayer, están en Código 3 en el TM N32 y ninguno fija el criterio de aceptación de ASME B31.3. Mandarlos al inspector antes de que se corrijan sería entregarle criterios que ADASA está objetando.

## Checklist pre-envío

- [x] Los siete documentos repuestos en el paquete, superados a `_superseded/`, recuento 43 → 50 sin pérdidas
- [x] Revisión del cajetín verificada en los siete repuestos
- [x] Perfil de anclaje contrastado abriendo la Rev B y la Rev 0
- [x] Día de la semana verificado: 13-Ago-2026 es jueves y 14 es viernes
- [x] Inglés íntegro, sin símbolo de sección, sin la palabra "letter", sin códigos de observación ni referencias internas
- [x] Metadatos Word limpios (autor Luis Rivera Gonzalez, company Aguas Antofagasta, en-US)
- [ ] Abrir el enlace y confirmar que muestra los archivos nuevos antes de enviar
- [ ] Enviar como **reply al hilo del Request 003**, no como correo nuevo
- [ ] **Al pegar en Outlook, confirmar que el párrafo del enlace y los dos adjuntos viajan.** El párrafo del enlace se cayó del cuerpo en los dos últimos envíos
- [ ] Tras envío: BORRADOR → ENVIADO aquí y en el README, respaldo PDF o `.msg` en esta carpeta, entrada nueva arriba en la Bitácora, y `BV-09` a cerrado en `compromisos.yaml` con regeneración del `.xlsx`
