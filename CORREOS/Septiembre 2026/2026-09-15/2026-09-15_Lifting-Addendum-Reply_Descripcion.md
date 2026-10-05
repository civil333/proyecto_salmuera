---
titulo: Respuesta a BW Water sobre el addendum de izaje del 14 de septiembre
fecha: 2026-09-15
estado: ENVIADO
destinatario: Eduardo Yamauchi (BW Water)
cadena: transmittals
type: correo
project: salmuera-taltal
second_brain: capture
---

# Correo — El addendum de izaje no completa el paquete

> **ENVIADO el martes 15 de septiembre de 2026, versión ejecutiva.** Hora pendiente de registrar desde el respaldo. Reply-All sobre el correo de Eduardo Yamauchi del lunes 14 a las 23:04, capturado en `CORREOS/_RECIBIDOS/Septiembre 2026/2026-09-14_Eduardo_Yamauchi_RE__TALTAL_-_Lifting_package_for_the_module_and_the_scope_of/`.

**Archivo:** `2026-09-15_Lifting-Addendum-Reply.docx` · **Script:** `crear_correo_izaje_addendum.py`
**Asunto:** `RE: TALTAL - Lifting package for the module and the scope of the structural review`
**Destinatarios:** To Eduardo Yamauchi. CC Stephane Gehant, Jeryl F. Regulacion, Lokman Hakim Bin Mat, Magdier Arias, Mohd Adnin Bin Zulkaflee, Sadeep Irugalbandara y Nick Huta (BW Water), más Victor Gutierrez (ADASA), que no venía en la respuesta de Eduardo.
**Adjunto:** `BASES TECNICAS/pdf/P22-ET-09-000-001-0 (ET Módulo).pdf`, la ET completa de 41 páginas. La página 29 del PDF corresponde a la "29 de 41".
**Plazo fijado:** jueves 17 de septiembre de 2026 (decisión del usuario).

## Qué mandó BW Water

Eduardo escribe que recibió ese día el addendum de izaje, que la orden de compra esperaba "esta confirmación", que la orden se firmó y liberó el 14, y que pidió a "Eng. Thomas" incluirlo en su alcance, confirmación que espera. **"Eng. Thomas" es Thomas Engineers (Tomás Ávila)**, el profesional que ADASA recomendó el 18-Ago sin designarlo y al que BW Water colocó la orden según la minuta del 09-09-26.

El adjunto `P22-CD-09-005-003_UHPRO Structural Calculation Report - Addendum_RevA (1).pdf` tiene tres páginas: la portada ADASA, la portada de Aulem y una sola hoja técnica. Esa hoja trae un lifting frame de cuatro W10x49 en ASTM A36 soldados, un gancho único sobre la vertical del centro de gravedad, eslingas a 45° como mínimo e izaje de prueba. Completan la hoja la Figura 16 y la tabla de pesos (vacío 10.278,74 kg o 100,80 kN, operación 12.482,35 kg o 122,41 kN).

## Resumen del cuerpo

224 palabras en cinco párrafos y una lista de tres viñetas, primera persona, sin tablas. Reescrito en versión ejecutiva a pedido del usuario desde una primera versión de 432 palabras.

1. **Quién confirma.** Lee la confirmación pendiente como la aceptación del alcance de izaje por Thomas Engineers. Pide que cubra el paquete completo y que manden su fecha de entrega.
2. **El addendum no completa el paquete.** Su Figura 16 repite las reacciones de la Condición 1 del Rev 0 y agrega los W10x49 y un punto de gancho, sin cotas. ADASA fabrica el yugo en Chile y con ese documento no se construye.
3. **La ET, adjunta.** Section 7 - Engineering and Documentation to be Developed During the Assignment, page 29: los tres entregables del Manual de montaje, cada uno con su cita literal en español.
4. **Plano de fabricación.** El plano del yugo tiene que traer dimensiones, uniones y soldaduras, puntos de eslinga y la conexión a los esquineros superiores. La memoria sigue debiendo la verificación local de los puntos pedida el 11-Sep.
5. **Plazo.** Paquete completo el jueves 17, en negrita, para que la revisión de ADASA de la Sección 7, pág. 30, cierre antes de liberar el módulo para transporte.

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| La Figura 16 repite las reacciones de la Condición 1 del Rev 0 | Addendum pág. 3 contra `ENTREGAS_BWWATER/ENTREGA 71/md/P22-CD-09-005-001_0 UHPRO Structural Calculation Report_extracted.md`, líneas 1118-1159, nodos 126 a 129, combinación 401 | **Sí.** 44,112 / 65,318 / 37,223 / 54,948 kN contra 44,108 / 65,323 / 37,143 / 55,018 kN, diferencia máxima 0,08 kN |
| Agrega W10x49 y un punto de gancho | Addendum pág. 3, texto extraído | Sí |
| La Figura 16 no trae ninguna cota | Addendum pág. 3, imagen nativa de 916 x 680 px y render de la página | **Sí, por render** |
| Los tres entregables dentro del Manual de montaje, con "Memoria de Calculo" sin tilde | PDF de la ET, página 29, texto extraído del original | Sí, cita literal |
| Nombre de la Sección 7 en inglés | El mismo de los correos del 10 y del 11-Sep | Sí |
| No se liberan los equipos para transporte sin la aprobación de ADASA | ET Sección 7, pág. 30, `BASES TECNICAS/md/` líneas 1670-1672 | Sí |
| Verificación local de los puntos pedida el 11-Sep | `CORREOS/Septiembre 2026/2026-09-11/crear_correo_izaje_respuesta.py`, viñeta *Padeye* | Sí |
| Thomas Engineers es el profesional de la orden | Correo del 18-Ago y minuta del 09-09-26 | Sí |
| Días de la semana | `datetime`: 15 martes, 17 jueves | Sí |

## Contexto Interno (No enviar)

- **La orden al profesional recién se liberó el 14.** La minuta del 9 decía que se colocaba ese día. Los cuatro días de Thomas Engineers recién empiezan a correr, de modo que la revisión estructural tampoco llegó el 15. [Probable] La orden quedó retenida hasta tener el addendum para fijar el alcance de izaje.
- 🔴 **La ET no pide una "maniobra de izaje".** Pide la memoria de cálculo, el plano de izaje con puntos y pesos y el plano y diseño del yugo. Exigir la maniobra citando la ET sería refutable, y el correo del 11-Sep ya dejó el method statement del rigger del lado de ADASA.
- **El plazo del 17 va sin el cálculo de los siete días hábiles, por decisión del usuario.** Con el feriado del viernes 18, un paquete recibido el 17 cierra la revisión el martes 29, un día después del embarque. Los siete días son el máximo que la ET da a ADASA, así que puede revisar antes sin declararlo.
- **El plano de fabricación detalla un entregable que la ET nombra en una línea.** Dimensiones, uniones, puntos de eslinga y conexión son el contenido mínimo de un "plano y diseño del yugo" que se fabrica en Chile. No se exige norma de diseño (ni ASME BTH-1 ni AISC), porque la ET no fija ninguna y exigirla sería over-reach.
- **Salió en la versión ejecutiva y queda disponible.** Primero, la aritmética del peso vacío: la suma de las cuatro cargas, 201,6 kN, dividida por 2,0 da los 100,80 kN del addendum. Segundo, el pedido de código propio, porque el `P22-CD-09-005-003` es el de los Criterios de Diseño en Rev 0. Tercero, el largo de eslinga, el ángulo mínimo y el izaje de prueba dentro del plano de izaje. Por último, el embarque del 28 y la reserva de derechos, que sigue en el hilo desde el 11-Sep.
- **Para la Sección 3 del próximo transmittal.** El addendum dice Rev A en la portada y Rev B en la cabecera interna. Su hoja dice "Page 2 of 2" en un archivo de tres páginas. Lo preparó Aulem en estado "FOR REVIEW", sin pasar por el profesional. También quedan la BAE 43.1 a) y d), la Figura 15 y el código duplicado.
- [Suposición] **Los ángulos de eslinga implícitos en la Figura 16 parecen bajo el mínimo de 45°.** El cociente entre carga vertical y tensión de eslinga en cada esquina da entre 37,9° y 44,9°. El marco redistribuye carga entre esquinas y la figura no trae cotas, así que no se puede afirmar. Se verifica cuando llegue el plano con geometría.
- **`PRG-49` sin reprogramación.** La regla escrita el 11-Sep cuenta reprogramación solo si BW Water propone la fecha. El 17 lo fijó ADASA, así que el contador sigue en 0 y el 15 queda como incumplimiento de la fecha fijada. Si el usuario prefiere contarlo, basta con subir el contador y regenerar el Excel.
- **Gate `anti-ia`: VERDE, Caso B, en la voz del registro de correspondencia.** La versión de 432 palabras estaba en el borde de CL-19, con dos bloques eliminables. El primer borrador ejecutivo quedó bajo el perfil, con mediana 15,5 y dos oraciones de 5 y 7 palabras. La final mide mediana 20,5 contra 18, percentil 90 en 30,7 contra 35, 12,5 % sobre 30 palabras contra 14,3 %, y paréntesis en 5,9 por mil contra 6,18. Veredicto en `.anti-ia-2026-09-15/veredicto.md`.

## Checklist pre-envío

- [x] ~~Gate `anti-ia revisar` sobre el `.docx`, veredicto persistido.~~ VERDE, Caso B.
- [x] ~~Correo entrante del 14-Sep capturado, adjunto movido con hash verificado y registro regenerado con lint en cero.~~
- [x] ~~Reply-All sobre el correo de Eduardo del 14 a las 23:04.~~ Enviado el 15-Sep, confirmado por el usuario.

## Checklist post-envío

- [x] ~~`BORRADOR` a `ENVIADO` aquí.~~ Hecho el 15-Sep. Falta la hora.
- [ ] Dejar el respaldo del enviado (PDF o `.msg`) en esta carpeta y anotar la hora.
- [ ] Verificar sobre el respaldo que viajaron la ET adjunta y Victor Gutierrez en CC, y que la negrita del plazo, las viñetas y las comillas de las citas sobrevivieron al pegado en Outlook.
- [x] ~~README: entrada del 15-Sep arriba en la Bitácora y línea del izaje en Estado Vigente.~~ Hecho el 15-Sep, con la línea de compromisos al corte del 15.
- [x] ~~`PRG-49`: addendum incompleto, fecha del 17-Sep fijada por ADASA y criterio de cierre ajustado al plano de fabricación del yugo.~~ Reprogramaciones en 0 por la regla escrita, Excel regenerado con respaldo previo en `_backups/` y `openpyxl_lint.py` sin hallazgos.
- [x] ~~Memoria `project_izaje_yugo_modulo`.~~ Addendum, lo que repite del Rev 0, plazo del 17 y las tres lecciones.
- [ ] Si el paquete completo no llega el jueves 17, registrar el incumplimiento en la nota del `PRG-49` y llevarlo a la Sección 3 del próximo transmittal con la BAE 43.1 a) y d).
