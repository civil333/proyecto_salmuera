---
titulo: Correo urgente a BW Water por el procedimiento FAT del módulo, con la trazabilidad desde mayo
fecha: 2026-09-16
estado: ENVIADO
destinatario: Eduardo Yamauchi (BW Water)
cadena: hilo nuevo
type: correo
project: salmuera-taltal
second_brain: capture
---

# Correo: el procedimiento FAT del módulo nunca se sometió y el FAT es la próxima semana

> **ENVIADO el miércoles 16 de septiembre de 2026**, confirmado por el usuario. Hora pendiente de registrar desde el respaldo. Hilo nuevo, con asunto propio, por decisión del usuario. Sin adjuntos.

**Archivo:** `2026-09-16_Module-FAT-Procedure-Required.docx` · **Script:** `crear_correo_procedimiento_fat_modulo.py`
**Asunto:** `URGENT - TALTAL: Module Factory Acceptance Test procedure required before the FAT`
**To:** Eduardo Yamauchi. **CC:** Stephane Gehant, Jeryl F. Regulacion, Lokman Hakim Bin Mat, Magdier Arias, Mohd Adnin Bin Zulkaflee, Sadeep Irugalbandara y Nick Huta (BW Water), más Victor Gutierrez (ADASA), los mismos del correo de izaje del 14-Sep.

## Por qué sale hoy

El barrido de las 93 entregas de BW Water, por nombre de archivo y por el texto de 390 PDF únicos con los comprimidos incluidos, confirma que el procedimiento FAT del módulo (`PROV-PROC-FAT-001`) nunca se sometió. Lo único que existe es el `P22-PP-09-000-001` Rev C, cuya sección 3 lo limita al hardware del tablero. El FAT es la próxima semana, según el usuario y según el Progress Update del 28 de agosto, que lo pone del 15 al 25 de septiembre. El Progress Report de la semana 37 sigue con el montaje entre 15 y 35 % y la inspección dimensional final en 0 %, lo que calza con que el 18 y el 19 todavía son ensayos y montaje.

## Resumen del cuerpo

216 palabras en cuatro párrafos más una tabla de nueve filas y el cierre. **Reordenado a pedido del usuario:** el borrador anterior abría con que el procedimiento nunca se sometió, y eso hacía parecer que ADASA recién se acordaba a días del ensayo.

1. **Obligación e historial.** La ET Section 8.1 exige el procedimiento detallado y ADASA lo levanta por escrito desde mayo. La tabla va a continuación como respaldo inmediato.
2. **Tabla de trazabilidad**, desde el TM N17 del 5 de mayo hasta el correo del 8 de septiembre.
3. **Estado y consecuencia.** Sigue sin recibirse y el FAT está planificado para la próxima semana. Su aprobación es punto de detención de ADASA en la fila 7.1 del ITP Rev 0, y las filas 7.2 a 7.5 y el Acta FAT de la 7.9 se ejecutan contra él. Cierra en negrita: el FAT no puede abrir formalmente hasta aprobar el procedimiento.
4. **El Rev C del tablero no cubre el requisito.** Su sección 3 excluye las pruebas funcionales de software y la verificación de lógica, y la Section 8.1 exige ambas en el FAT.
5. **Pedido en negrita:** someterlo a más tardar el viernes 18 de septiembre, con el alcance mínimo completo de la Section 8.1 y la secuencia de puntos de inspección de las filas 7.1 a 7.9. No menciona el plazo de revisión de ADASA.

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| El procedimiento FAT del módulo nunca se sometió | Barrido de `ENTREGAS_BWWATER/` E1 a E93: 933 archivos por nombre y 390 PDF únicos por texto, con los diez comprimidos | Sí |
| El FAT es la próxima semana | Usuario, 16-Sep; Progress Update del 28-Ago, tarea 419, del 15 al 25 de septiembre | Sí |
| Primer ítem de la ET Section 8.1: aprobación del procedimiento detallado | `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md`, líneas 1728 a 1739 | Sí |
| Fila 7.1 del ITP Rev 0 es punto de detención de ADASA | `ENTREGA 57/P22-BA-09-000-004_0_ITP.pdf`, página 5: fila 7.1 con `P M H` en las columnas V (sub-vendor), B (BW Water) y C (ADASA); leyenda H en la página 3 | Sí |
| Filas 7.2 a 7.5 y 7.9 se ejecutan contra el procedimiento | Misma página: 7.2, 7.3, 7.4 y 7.5 citan `FAT Procedure` o `PROV-PROC-FAT-001`; 7.9 exige el `Approved ... FAT Procedure`. La 7.6 cita el MDR y la 7.8 el procedimiento de UT, por eso quedan fuera | Sí |
| El Rev C se limita al hardware y excluye software y lógica | `ENTREGA 90/25007-0090/P22-PP-09-000-001_C ...pdf`, página 3: *"Software functional testing, process logic verification, and SAT are excluded from this Hardware FAT."* | Sí |
| 5 May 2026, TM N17, PQP Rev A, OBS-02 | `P22-TM-09-000-017-0_TRANSMITTAL.md:136`, dentro de la subsección 2.6, Project Quality Plan Rev A | Sí |
| 25 May 2026, TM N19, ITP Offsite Rev B | `P22-TM-09-000-019-0_TRANSMITTAL.md:164`, subsección 2.10 | Sí |
| 10 June 2026, TM N20 | `P22-TM-09-000-020-0_TRANSMITTAL.md:52`, Resumen Ejecutivo | Sí |
| 6 July 2026, TM N26, ITP Rev 0 en Código 1 | `P22-TM-09-000-026-0_TRANSMITTAL.md:200` | Sí |
| 18 August 2026, TM N34, Quality Dossier Index Rev B, B11 sin número | `ENTREGA 77/P22-BA-09-000-013_B_Quality Dossier.pdf`, página 2: B1 a B10 llevan código y B11 no | Sí |
| 28 August 2026, Progress Update, tarea 419, sin actividad de procedimiento | `PROGRAMA y CONTRATO/PROGRAMA DE SEGUIMIENTO RETRASOS/2026-08-28_..._Progress Update.pdf`, página 3; las únicas tareas de ensayo son la 419 y la 429 (Performance Test) | Sí |
| 31 August 2026, TM N37, Section 3, "Never delivered" | `P22-TM-09-000-037-0_TRANSMITTAL.md:121` | Sí |
| 3 September 2026, TM N38, Section 3, "Not received" | `P22-TM-09-000-038-0_TRANSMITTAL.md:145` | Sí |
| 8 September 2026, correo para la reunión del 9 | `CORREOS/Septiembre 2026/2026-09-08/crear_correo_puntos_revision_09sep.py`, líneas 330 a 337 | Sí |
| Días de la semana | `datetime`: 3-Sep jueves, 16-Sep miércoles, 18-Sep viernes | Sí |

## Contexto Interno (No enviar)

- **El Transmittal N39 dejó de arrastrar el faltante.** Solo registra el FAT del tablero y el alcance FAT del PQP. Hay que reponerlo en la Sección 3 del próximo transmittal.
- **No se cita la reunión del 9 de septiembre.** La minuta es transcripción automática y no es oponible, y según la Bitácora el procedimiento no se trató ahí. El FAT se conversó en el rango del 18 al 19 con referencia al 20.
- **No se afirma que el correo del 8 quedó sin respuesta.** La captura del correo entrante está en HOLD, así que la tabla dice solo que se pidió la fecha.
- **El DDSR no sirve de evidencia.** Ni el del 7 ni el del 14 de septiembre listan procedimientos de calidad, tampoco el del tablero, de modo que su silencio sobre este no prueba nada.
- **Plazo de revisión callado por decisión del usuario.** Bajo la Cláusula 37.2 la revisión dura siete días hábiles, y sometido el viernes 18 vencería el martes 29 contando solo fines de semana, después del embarque del 28. Si BW Water entrega el 18 y el FAT abre el lunes 21, la revisión tendrá que ser inmediata o el punto de detención chocará con el embarque.
- **El viernes 18 es feriado de Fiestas Patrias en Chile.** Para BW Water en Malasia es día hábil y el plazo se sostiene, pero la recepción del lado de ADASA cae en feriado. Si la revisión tiene que ser inmediata, se hará el fin de semana o el lunes 21.
- **Fuera de alcance a propósito:** el procedimiento de conservación y embalaje, también faltante desde el N37, y el segundo FAT del tablero en Penang que BW Water comprometió en la hoja de comentarios del Rev C.
- **Por qué no se abre con el faltante.** El primer borrador partía con *"has never been submitted, and the test is planned for next week"*, y leído primero sugiere que ADASA recién lo necesita. El orden actual pone la obligación y los pedidos desde mayo antes del estado, de modo que *"still not been received"* se lee como persistencia del proveedor.
- **Gate `anti-ia`: VERDE en las dos pasadas, confianza Baja por largo, Caso A.** Primera pasada: la negrita pasó de la apertura a la consecuencia (CL-24). Segunda pasada: reordenamiento del cuerpo. Veredicto en `.anti-ia-2026-09-16/veredicto.md`, validado con `inventory.py --check-veredicto`.

## Checklist pre-envío

- [x] ~~Gate `anti-ia revisar` sobre el `.docx`, veredicto persistido.~~ VERDE, Caso A.
- [x] ~~Cero símbolo de sección, cero grafía británica, cero em dash.~~
- [x] ~~Confirmar la distribución.~~ Enviado por el usuario el 16-Sep.
- [ ] Verificar sobre el respaldo que la tabla y las dos negritas sobrevivieron al pegado en Outlook.
- [x] ~~Revisión del usuario sobre el orden nuevo del cuerpo.~~ Aprobado y enviado.

## Checklist post-envío

- [x] ~~`BORRADOR` a `ENVIADO` aquí.~~ Hecho el 16-Sep; falta la hora.
- [ ] Dejar el respaldo del enviado (PDF o `.msg`) en esta carpeta.
- [x] ~~README: entrada arriba en la Bitácora y línea en Estado Vigente.~~ Hecho el 16-Sep.
- [x] ~~Registro de Compromisos: `PRG-50`, fecha 2026-09-18, origen `FIJADA ADASA`; Excel regenerado y `openpyxl_lint.py`.~~ Hecho el 16-Sep, lint sin hallazgos.
- [ ] Reponer el punto en la Sección 3 del próximo transmittal.
