---
titulo: Correo a Bureau Veritas por el desfase de los spools del turbo interetapa, con pedido de levantamiento en Penang e informe eléctrico aparte
fecha: 2026-09-16
estado: ENVIADO
destinatario: Jaime Martínez (Bureau Veritas Chile)
cadena: hilo nuevo
type: correo
project: salmuera-taltal
second_brain: capture
---

# Correo: Bureau Veritas, desfase de los spools del turbo y levantamiento en Penang

> **ENVIADO el miércoles 16 de septiembre de 2026**, confirmado por el usuario. Hora pendiente de registrar desde el respaldo. Reemplazó al borrador sobre el Request 008 que estaba para el 17, que se eliminó por decisión del usuario.

**Archivo:** `2026-09-16_BV-Survey-Turbocharger-Offset.docx` · **Script:** `crear_correo_bv_levantamiento_penang.py`
**Asunto:** `25007 TALTAL - Turbocharger spool offset and inspection scope in Penang`, hilo nuevo.
**To:** Jaime Martínez, Administrador de contrato de CESMEC-Bureau Veritas (`martinez.jaime@bureauveritas.com`). **CC:** Carlo Montecinos y Luis Rodrigo Arcila (Bureau Veritas), Magdier Arias, Eduardo Yamauchi y Lokman Hakim Bin Mat (BW Water Penang), y Victor Gutierrez (ADASA).
**Adjuntos:** nueve PDF y 16,9 MB en `ADJUNTOS_BV-Survey/`, solo lo esencial para entender el caso por decisión del usuario. Copias con md5 verificado, salvo el primero, que se exportó del `.docx` con Word:
1. Correo de ADASA a BW Water del 16 de septiembre, en PDF desde Word, dos páginas con la tabla y la captura del modelo 3D.
2. Correo de BW Water del 14 de septiembre con el reporte semanal.
3. Progress Report Week 37.
4. P&ID Rev 0.
5. Line List Rev 1.
6. Equipment List Rev 0.
7. Instrument List Rev F.
8. Hoja de datos del turbo de alimentación Rev 0.
9. Hoja de datos del turbo interetapa Rev 0.

## Por qué sale hoy

En la reunión de hoy BW Water informó el desfase de unos 50 mm entre los turbos y sus spools, y el nuevo listo para despacho al 12 de octubre. El usuario cambió el enfoque con Bureau Veritas. La prueba de alta del 17 se mantiene sin las líneas de los turbos, y Bureau Veritas hace desde el 18 un levantamiento independiente de la causa raíz, de los equipos, de los instrumentos y de otros temas constructivos, más un informe eléctrico aparte.

## Resumen del cuerpo

286 palabras en inglés, **versión ejecutiva en la voz de Luis** (registro de correspondencia, primera persona), pasada por `anti-ia` modo revisar. La versión anterior tenía 377.

1. **Lo que se supo hoy:** desfase de unos 50 mm, spools afectados a cortar, resoldar y reensayar, y listo para despacho al 12 de octubre. Por las fotos, el turbo interetapa, el de mayor presión de operación. Cierra diciendo que adjunta los antecedentes, incluido el correo a BW Water y su último reporte semanal (Progress Report Week 37).
2. **Prueba del 17** (Request 008): se mantiene sin las líneas de los turbos.
3. **Levantamiento desde el 18**, en negrita y en primera persona (*"I ask Bureau Veritas"*):
   - causa raíz con registro antes de cortar (fila 4.2 del ITP);
   - equipos contra la Equipment List Rev 0 y los dos turbos contra sus hojas de datos Rev 0 (4.1);
   - instrumentos contra la Instrument List Rev F y el P&ID Rev 0 (4.3 y 4.4);
   - otros temas constructivos.
4. **Informes y jornadas:** un informe de inspección y uno eléctrico aparte (6.1 a 6.3) con Flash Report, y la propuesta de jornadas para aprobación antes de movilizar más allá del 18.
5. **Acceso** del inspector, pedido a Magdier, Eduardo y Lokman.
6. **Ausencia y traspaso:** Luis estará fuera de la oficina las próximas dos semanas, y mientras tanto Victor Gutierrez lleva las comunicaciones de ADASA. Los informes van a los dos. La primera versión decía *"From tomorrow Victor Gutierrez leads this matter"* y el usuario objetó que sonaba a que se estaba escondiendo.
7. **Cierre con agradecimiento:** *"Thank you for coordinating this. I look forward to your confirmation."*

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| Desfase de unos 50 mm, cortar, resoldar y reensayar, 12 de octubre | `MINUTAS DE REUNION/MINUTA DE REUNION 16-09-26.pdf` p2 y p3 (transcripción automática; se cita la reunión) | Sí |
| Por las fotos, el turbo interetapa | Usuario, 16-Sep | Por el usuario |
| El interetapa trabaja a la presión más alta del módulo | Hojas de datos Rev 0: salida de alimentación de 84,8 bar en el interetapa y de 69,53 bar en el de alimentación | Sí |
| Request 008: el 17 es prueba de alta presión | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR 17 y 18}/RE__25007_TALTAL_-__Request_to_witness_inspection_008.zip` | Sí |
| Filas 4.1, 4.2, 4.3, 4.4 y 6.1 a 6.3 del ITP Rev 0 | `ENTREGAS_BWWATER/ENTREGA 57/md/P22-BA-09-000-004_0_ITP_extracted.md:81-97` | Sí |
| BW Water reporta todos los equipos en el taller | Correo de Eduardo Yamauchi del 14 de septiembre: *"With that the delivery of all the equipment are complete"* | Sí |
| Informe al día siguiente, Flash Report y jornadas de acompañamiento QA/QC contratadas | Oferta 600049 Rev 3, secciones 3, 3.1 y 3.2 e ítem 5.a (`PROGRAMA y CONTRATO/HITO BUREAU VERITAS/md/600049…Rev3_extracted.md`); no se cita en el correo | Sí |
| Jaime Martínez, administrador de contrato, con copia a Carlo Montecinos y Luis Rodrigo Arcila | Captura del correo de Bureau Veritas del 11-Sep (Request to witness inspection 014), aportada por el usuario | Sí |

## Contexto Interno (No enviar)

- **"Javier" es Jaime Martínez.** El usuario lo nombró Javier, y la firma de su correo del 11 de septiembre dice Jaime Andrés Martínez Sánchez.
- **Excepción de correo conjunto.** Se nombra a BW Water porque está en copia (`feedback_bv_no_nombrar_bw_water`). Por la misma razón no van la oferta, las tarifas ni el saldo de jornadas: la oferta tiene 18 jornadas de acompañamiento QA/QC y 7 de FAT.
- **Adjuntos acotados.** El Piping Layout, el modelo 3D y el resto de los planos se piden en el taller. No van los GA de los turbos Rev A, en Código 3 desde el TM N10 y dados por aprobados por error en el Master Register y en la Tabla 1 del TM N39, ni la Nota Técnica interna del dossier. El Request 008 ya lo tiene Bureau Veritas.
- **El PDF del correo a BW Water sale del `.docx`**, no del respaldo del enviado, que todavía no está archivado. Si el usuario editó el texto al pegarlo en Outlook, el adjunto puede no coincidir palabra por palabra.
- **Paquete de inspección desactualizado.** El paquete publicado a Bureau Veritas tiene el P&ID y las hojas de datos de los turbos en Rev D. Las Rev 0 van adjuntas en este correo, y la carpeta publicada no se toca.
- **El levantamiento pedido excede una visita de rutina.** Por eso se pide a Bureau Veritas proponer las jornadas y que ADASA las apruebe antes de movilizar, para que no haya cobro de jornadas sin aprobación.
- **Borrador eliminado.** El correo del 17 sobre el Request 008 (`CORREOS/Septiembre 2026/2026-09-17/`) se eliminó por decisión del usuario, sin enviarse. Su veredicto quedó registrado en `.anti-ia-2026-09-16/veredicto.md`.

## Checklist pre-envío

- [x] ~~Gate `anti-ia revisar`, veredicto persistido.~~ VERDE en dos pasadas; la segunda es la versión ejecutiva en la voz de Luis.
- [x] ~~Cero símbolo de sección, grafía británica, guiones largos, oferta ni tarifas.~~
- [x] ~~Hilo nuevo a Jaime Martínez con la copia indicada, y adjuntar los nueve PDF.~~
- [x] ~~Enviar.~~ Enviado el 16-Sep, confirmado por el usuario.

## Checklist post-envío

- [x] ~~`BORRADOR` a `ENVIADO` aquí.~~ Hecho el 16-Sep. Falta la hora y el respaldo del enviado.
- [x] ~~README: agregar el envío a la entrada de Bitácora del 16.~~ Hecho el 16-Sep.
- [x] ~~Registro de Compromisos.~~ `BV-26` para el levantamiento con la propuesta de jornadas, y `BV-27` para el informe eléctrico. Hecho el 16-Sep.
