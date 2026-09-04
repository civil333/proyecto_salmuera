---
titulo: Jornadas de inspección Bureau Veritas — 7 y 13-14 de agosto
codigo: Correo interno a Víctor Gutiérrez
fecha: 2026-08-07
estado: BORRADOR
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-08-07
---

# Correo interno a Víctor Gutiérrez — jornadas de inspección Bureau Veritas

**Destinatario:** Víctor Gutiérrez Aqueveque, Jefe Depto. Proyectos Desalación, ADASA (`vgutierrez@aguasantofagasta.cl`). Sin copia. Correo interno, español, sin plantilla ADASA.

**Artefactos:** `crear_correo_bv_jornadas_victor.py` → `2026-08-07_BV-Jornadas-Inspeccion.docx` (642 palabras, una página).

## Qué dice

Resume el alcance de las tres jornadas de inspección de taller en Penang que están en juego esta quincena, en una tabla, y enumera cuatro puntos abiertos.

**Jornada de hoy, viernes 7 de agosto**, de 09:00 a 17:00, per el Inspection Request 002 (formulario AQ-QAM-F027 Rev 0, emitido el 29 de julio a las 04:10): fabricación de spools de super dúplex, líquidos penetrantes de raíz y capping de la soldadura, fabricación del marco del skid, y revisión de las especificaciones de soldadura y calificación de soldadores. Esta última cierra el punto que Bureau Veritas preguntó el 24 de julio y que el taller movió del 28 de julio a esta fecha. Los adjuntos del Request son el ITP Rev 0 y el NDE Plan `P22-BA-09-000-005` Rev C, byte-idénticos a los aprobados.

**Jornadas del jueves 13 y viernes 14 de agosto**, per el Inspection Request 003 (en el repositorio desde el 5 de agosto a las 07:59): ensayo de presión de la tubería de alta y preparación de superficie para pintura.

**Los cuatro puntos abiertos:**

1. **El alcance del 13 y 14 se estrechó.** El Request 003 declara solo el ensayo de alta. La minuta del 4 de agosto ofrecía también el de baja presión, y el del RO Vessel no aparece en ninguna de las dos versiones. La Nota Técnica P22-NT-09-000-002-0, sección 3.2, exige los tres.
2. **Acción de ADASA antes del 14.** El inspector tiene el procedimiento de pintura en Rev B, cuyo formulario declara el perfil de anclaje en 40-75 µm mientras la Rev 0 lo deja en 50-80 en los dos lugares. Compromiso `BV-09`, abierto. La Rev 0 llegó con el submittal 25007-0071.
3. **Aviso de ocho días** contra los treinta de la BAE Cláusula 37; segunda notificación consecutiva fuera de plazo. Se menciona la contrapropuesta escrita del taller (tres a cinco días) y que aceptar jornadas puntuales no constituye precedente.
4. **Formulario de registro del ensayo hidrostático sin definir.** El procedimiento remite a un reporte de presión que el paquete ya no contiene; el ensayo es punto de detención y encadena con la liberación para despacho, de la que depende el 40 % del pago. Pedido en el correo del 6 de agosto, sin respuesta.

Cierra recordando que el informe de la jornada de hoy debería llegar en los próximos días, como llegó el de la primera visita.

## Verificación de fuentes

| Afirmación del correo | Fuente |
|---|---|
| Alcance y horario de la jornada del 7 de agosto | `REQUEST WITNESS INSPECTION/RWI 02/ZIP_EXTRAIDO/md/AQ-QAM-F027 Inspection Request_TALTAL project (002)_extracted.md` |
| Alcance y fechas del 13 y 14 de agosto | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 02/md/AQ-QAM-F027 Inspection Request_TALTAL project (003)_extracted.md` |
| Minuta del 4 de agosto ofrecía baja y alta presión los días 12 y 13 | `MINUTAS DE REUNION/md/MINUTA DE REUNION 04-08-26_extracted.md`; README Bitácora 2026-08-04 |
| Los tres ensayos exigidos (7,5 bar Witness / 135 bar Hold / RO Vessel Hold) | Nota Técnica P22-NT-09-000-002-0, sección 3.2 |
| Perfil de anclaje 40-75 vs 50-80 µm | README Estado Vigente, hallazgo del 6 de agosto; compromiso `BV-09` |
| Treinta días de antelación | BAE 12803, cuerpo de la Cláusula 37 (no la 37.2) |
| Contrapropuesta de tres a cinco días | Correo de Eduardo Yamauchi del 28 de julio, 15:31 |
| Aviso de nueve días del Request 002 y cuatro del 001 | Fechas de emisión de ambos formularios |
| 31 lecturas de PMI conformes, sin no conformidades | Informe `BVM-IR001-28072026` Rev 0 |
| Formulario del ensayo hidrostático pedido el 6 de agosto | `CORREOS/Agosto 2026/2026-08-06/`, compromiso `PRG-24` |

Fingerprints anti-IA: ninguno. Sin el símbolo de sección. Metadatos limpios (autor Luis Rivera González, sin rastro de `python-docx`). Idioma del documento en `es-CL`.

## Contexto Interno (No enviar)

- La fecha correcta es **13 y 14**, no 12 y 13 ni 11 y 12. El análisis del 4 de agosto tomó la fecha de la minuta verbal y esa versión llegó al correo del TM N30. El Request 003 escrito manda. Compromiso `PRG-13`.
- El correo **no menciona** que la confirmación de las visitas V2 a V6 a Bureau Veritas lleva vencida desde el 24 de julio, que es incumplimiento propio de ADASA (`INT-01`, criticidad crítica). Si Víctor pregunta por qué el taller notifica directo al inspector, ese es el motivo. Se dejó fuera para no diluir los cuatro puntos accionables; conviene tenerlo a mano.
- Tampoco menciona que la aritmética del FAT no cierra (del 15 al 18 de septiembre hay cuatro días para siete jornadas contratadas), ni el saldo de jornadas (4 de 25 ejecutadas o notificadas). Son frentes de otra conversación.
- El punto 2 es acción de ADASA, no del proveedor. Escrito como tal, sin trasladarle la responsabilidad a BW Water.

## Checklist pre-envío

- [ ] Revisión de Luis
- [ ] Confirmar si va con copia a Jorge Guevara o Ronald Pellejero (el borrador va sin copia)
- [ ] Enviar y dejar respaldo PDF o `.msg` en esta carpeta
- [ ] Cambiar `estado: BORRADOR` a `ENVIADO` en este archivo
- [ ] Entrada en la Bitácora del README

## Checklist post-envío

- [ ] Cerrar `BV-09`: enviar la Rev 0 del procedimiento de pintura a Bureau Veritas antes del 14 de agosto
- [ ] Seguir la respuesta de BW Water sobre el formulario del ensayo hidrostático (`PRG-24`)
