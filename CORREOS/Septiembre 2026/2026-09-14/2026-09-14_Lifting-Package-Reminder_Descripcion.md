---
titulo: Recordatorio a BW Water del paquete de izaje y enlace de la reunión del 16 de septiembre
fecha: 2026-09-14
estado: ENVIADO
destinatario: Eduardo Yamauchi (BW Water)
cadena: transmittals
type: correo
project: salmuera-taltal
second_brain: capture
---

# Correo — Recordatorio del paquete de izaje y enlace de la reunión del miércoles 16

> **ENVIADO el lunes 14 de septiembre de 2026**, antes de que venza la fecha del martes 15. Hora pendiente de registrar desde el respaldo. Reply-All sobre el correo que ADASA envió el viernes 11 en la cadena del izaje.

**Archivo:** `2026-09-14_Lifting-Package-Reminder.docx` · **Script:** `crear_correo_izaje_recordatorio.py`
**Asunto:** `RE: TALTAL - Lifting package for the module and the scope of the structural review`
**Sin adjuntos.** Reply-All con To a Eduardo Yamauchi y CC a Stephane Gehant, Jeryl F. Regulacion, Lokman Hakim Bin Mat, Magdier Arias, Mohd Adnin Bin Zulkaflee, Sadeep Irugalbandara y Nick Huta (BW Water), más Victor Gutierrez (ADASA), los mismos del 11-Sep.

## Por qué sale hoy

BW Water no respondió nada al correo del 11 (confirmado por el usuario, porque la captura del correo entrante está detenida). La fecha última del paquete es el martes 15 y la reunión semanal de esta semana cae el miércoles 16, sin que haya llegado el enlace. Enviado hoy, el correo refuerza la fecha antes de que venza. Mañana ya serviría para constatar el incumplimiento.

## Resumen del cuerpo

106 palabras en dos párrafos, primera persona, sin tablas ni adjuntos.

1. **Recordatorio y lo pendiente.** Sin respuesta al correo del viernes 11. Mañana, martes 15, es la fecha última del paquete, y esa oración va en negrita. Quedan abiertos dos puntos de ese correo: que la revisión del profesional cubra el izaje del módulo, y la condición de izaje en sitio que BW Water designe, con el yugo o arreglo diseñado para ella. Pide confirmar ambos antes del 15.
2. **Reunión.** No llegó el enlace de la reunión de coordinación de esta semana, que debe ser el miércoles 16 a la hora habitual. Pide la invitación y que el paquete de izaje entre en la agenda.

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| Sin respuesta al correo del 11-Sep | Usuario, 14-Sep; `CORREOS/_RECIBIDOS/Septiembre 2026/` no registra correo posterior, con la captura en HOLD | Por el usuario |
| El 15-Sep es la fecha última del paquete | Cierre de `2026-09-11_Lifting-Package-Reply.docx`; `PRG-49` con `fecha_comprometida: 2026-09-15` | Sí |
| El alcance del profesional se pidió confirmar y no se confirmó | Correo del 11-Sep (*"Please confirm that scope"*); la respuesta de BW Water del 11-Sep 9:18 no lo menciona | Sí |
| La condición de izaje y el yugo o arreglo se pidieron | Correo del 11-Sep, viñeta *Yoke* | Sí |
| Días de la semana | `datetime`: 11 viernes, 14 lunes, 15 martes, 16 miércoles | Sí |
| La reunión suele ser el martes y la semana pasada fue el miércoles 9 | README, reunión semanal de los martes; `2026-09-08_Puntos-Revision-Reunion-09Sep_Descripcion.md` | Sí |
| A la hora habitual | Decisión del usuario, sin escribir la hora | No aplica |

## Contexto Interno (No enviar)

- **No reabre sustancia.** Sin secciones de la ET, sin BAE 43.1, sin Figura 15, sin cifras y sin reserva de derechos nueva, porque la del 11-Sep sigue en el hilo. Las palancas quedan para el `PRG-49` y la Sección 3 del próximo transmittal.
- **La reunión entra con propósito.** El paquete vence el día anterior, así que el correo pide que vaya en la agenda. Decisión del usuario: mismo correo y no uno aparte en la cadena del paquete semanal.
- **Se descartó el "please reply" genérico.** El correo nombra las dos confirmaciones que BW Water no dio.
- **Si el paquete no llega el 15**, no cuenta como reprogramación del `PRG-49` salvo que BW Water proponga otra fecha, que es la regla fijada el 11-Sep. El incumplimiento se anota en la nota del compromiso y se lleva a la reunión del 16.
- **Gate `anti-ia`: VERDE, confianza Baja por largo, Caso A sin cambios.** Veredicto en `.anti-ia-2026-09-14/veredicto.md`. Con seis oraciones la mediana (14,5 contra 18) y los paréntesis (0 contra 6,18) no son estables, por lo que no se alargó ni se agregó nada para calzar el perfil.

## Checklist pre-envío

- [x] ~~Gate `anti-ia revisar` sobre el `.docx`, veredicto persistido.~~ VERDE, Caso A.
- [x] ~~Reply-All sobre el enviado del 11-Sep, conservando los ocho destinatarios.~~ Enviado el 14-Sep, confirmado por el usuario.
- [ ] Confirmar sobre el respaldo que la oración del 15 conservó la negrita.

## Checklist post-envío

- [x] ~~`BORRADOR` a `ENVIADO` aquí.~~ Hecho el 14-Sep.
- [ ] Dejar el respaldo del enviado (PDF o `.msg`) en esta carpeta y anotar la hora.
- [x] ~~README: entrada del 14-Sep arriba en la Bitácora y línea del izaje en Estado Vigente.~~ Hecho el 14-Sep.
- [x] ~~`PRG-49`: recordatorio del 14-Sep sin sumar reprogramación, Excel regenerado y lint.~~ Recordatorio en la acción y en el historial de fechas, reprogramaciones en 0. Excel regenerado con respaldo previo en `_backups/` y `openpyxl_lint.py` sin hallazgos.
- [ ] Pendiente heredado del 11-Sep: archivar el respaldo de ese enviado con su hora.
