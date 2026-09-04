# Correo de cobertura — Transmittal N35

**Estado:** **ENVIADO el jueves 20-Ago-2026 a las 11:16 de Chile**, dieciseis minutos
despues del correo de la hidrostatica, que salio por la otra cadena a las 11:00
**Fecha:** 20-Ago-2026 (jueves)
**Archivos:** `2026-08-20_Transmittal-N35.docx` · respaldo del enviado en
`TRANSMITTAL 35.pdf` (2 paginas)
**Generador:** `crear_correo_tm35.py`
**Cadena:** hilo de los submittals, la misma de los transmittals. **NO** es la cadena de
las jornadas de inspeccion, por la que el mismo dia salio el correo del ensayo
hidrostatico (`2026-08-20_Hydrotest-Report-20-Aug.docx`, misma carpeta). Decision del
usuario: los dos ejes van separados.

## Destinatarios y adjunto, segun el respaldo del enviado

El usuario ajusto la lista al enviar. Se registra lo que salio, no lo que proponia el
borrador.

- **To:** Victor Gutierrez, Ronald Pellejero, Jorge Guevara (ADASA); Eduardo Yamauchi,
  Fitri Indriyani (BW Water)
- **CC:** Jeryl F. Regulacion, Nick Huta, Sadeep Irugalbandara, David Chee Keat Swee,
  Andrew Sia, Adzlan Bin Abd Rahim, Tanya Figueroa, Ahmad Iqbal Bin Azam, Stephane Gehant
  (BW Water)
- **Asunto:** TALTAL - Transmittal N35 - submittal 25007-0081
- **Un adjunto, 210 KB:** el transmittal en PDF. Los tres `CC_ADASA` viajaron por el enlace
  de descarga.

**Diferencias respecto del borrador:** Allan Valentos, que el borrador ponia como
destinatario principal, quedo fuera; el equipo ADASA subio a **To**; y la copia de BW Water
se amplio de cuatro a nueve, incorporando a Regulacion, Huta, Irugalbandara, Chee, Sia,
Abd Rahim, Figueroa y Azam.

## Resumen del cuerpo

**212 palabras en cuatro parrafos, tres viñetas y el enlace, una pagina.** Version
ejecutiva a pedido del usuario. El correo no detalla el adjunto.

1. **Veredicto.** Transmittal N35, submittal 25007-0081, cinco documentos.
   3 — To be revised: 2 Codigo 1, 3 Codigo 3.
2. **Que vuelve a revision:** los tres procedimientos de ensayos no destructivos, por el
   mismo punto del N32, y los tres sin hoja de comentarios, que la Rev C debe traer. Los
   dos que llegan por sobre la Rev 0 son Codigo 1 y no requieren accion.
3. **Lo que exige atencion antes del proximo ensayo:** el transmittal fija la presion de
   cada linea de super duplex, 1,5 veces su diseño, y pide que no se ejecute ningun ensayo
   mas de ese circuito hasta que BW Water confirme los valores por escrito. Se señala que
   va en paralelo por la cadena de inspecciones.
4. **El plazo:** devolucion pedida al domingo 23; Clausula 37.2 al lunes 31.

**Lo que se saco a proposito:** el detalle tecnico de cada Codigo 3 (el Apendice 6 y el
Apendice 8, el limite de borrosidad, SA-790 contra el criterio de espesor) y la explicacion
de por que un registro bajo procedimiento no aprobado no entra al dossier. Todo eso es
contenido del transmittal y de los tres `CC_ADASA`.

**El unico item que el cuerpo destaca por sobre el adjunto es la presion de prueba**,
porque condiciona la ejecucion de los ensayos que vienen y no puede esperar a que alguien
abra el transmittal.

## anti-ia

Modo revisar. Cobertura: universales mas Claude, por la regla de autoria conocida (Opus 5).
**VERDE.** Cero marcadores, oracion maxima de 44 palabras, media 17,7. Los cuatro guiones
largos son estructurales, ninguno parentetico.

## La declaracion de la regla de presion de prueba

El transmittal lleva, en la subseccion del procedimiento de presion y en el Resumen
Ejecutivo, la **declaracion de que los 135 barG de la fila 5.2 del ITP son 1,5 veces la
presion de diseño de 90 barG**, la mas alta del circuito, y que cada linea se ensaya a 1,5
veces la suya segun la Line List Rev 0 aprobada en Codigo 1 en el TM N29. Incluye la
**tabla de las once lineas de super duplex** por TAG y la retencion: ningun ensayo del
circuito de alta hasta que BW Water confirme por escrito la presion de cada una.

Va en el transmittal y no solo en el correo porque es **disposicion documental**: cierra la
OBS-03 del TM N27, que pedia declarar la envolvente por circuito y nombrar la revision de
la Line List que fija el valor linea por linea. La Seccion 3 lleva la fila con origen
`N27, N35`.

**El veredicto no cambia por esto.** El procedimiento sigue en **Codigo 1**: remite a la
Line List aprobada, de modo que la regla existe, y lo que faltaba era que ADASA declarara
cual gobierna. Decision del usuario, coherente con no reabrir aprobaciones propias.

## Verificacion de fuentes

| Afirmacion del cuerpo | Verificado contra |
|---|---|
| Cinco documentos, 2 Codigo 1 y 3 Codigo 3 | Seccion 5 del transmittal y `_ANALISIS_N35.md` |
| Los tres NDE sin hoja de comentarios | Busqueda de "Comment Sheet" y "Comment from Client" en los cinco PDF: solo el `-010` y el `-011` la traen |
| El punto es el mismo del N32 | TM N32, subsecciones 2.5, 2.6 y 2.7; compromiso `PRG-25` |
| Registros bajo procedimiento no aprobado no admisibles | TM N30, Seccion 2, sobre el Dossier Index; ET `P22-ET-09-000-001-0` Seccion 8 |
| Devolucion pedida 23-Ago y Clausula 37.2 al 31-Ago | Submittal Form `25007-0081` y calculo de siete dias habiles desde el 20-Ago, verificado con `datetime` |
| El domingo 23 es domingo y el lunes 31 es lunes | `datetime`, verificado |
| **Enlace de descarga** | **Verificado sobre los `.docx` emitidos**, no sobre los scripts: texto visible correcto en los dos, destino del hipervinculo del transmittal coincidente caracter a caracter, y cero placeholder residual. En el correo va como texto plano, igual que en el N34, que es lo que sobrevive al pegado en Outlook |

## Contexto Interno (No enviar)

- **El correo de la hidrostatica del mismo dia** lleva el hallazgo del Spool 1, ensayado
  a 7,5 barG bajo un TAG de super duplex que no existe en la Line List. Es otra cadena y
  no se cruza aca.
- **El Codigo 1 del `-010` fue decision del usuario** contra una propuesta inicial de
  Codigo 3. El razonamiento quedo escrito en la Seccion 10 de `_ANALISIS_N35.md`.
- **Lo que se retiro y no se emite** esta en `ENTREGAS_BWWATER/ENTREGA 81/_HALLAZGOS_DETERMINISTAS.md`.

## anti-ia

Modo revisar. Cobertura: familias universales mas Claude, por la regla de autoria
conocida (Opus 5). **VERDE.** Cero marcadores criticos, oracion maxima de 44 palabras,
media 16,9, sigma 11,72. Los cuatro guiones largos son estructurales (el veredicto y las
tres viñetas de archivo), ninguno parentetico.

## Checklist pre-envio

- [x] Fecha de carpeta igual a la fecha del encabezado (20-Ago-2026)
- [x] Dias de la semana verificados (domingo 23, lunes 31)
- [x] Idioma `en-US` fijado; metadatos con autoria y compania
- [x] Cero simbolo de seccion
- [x] Los tres `CC_ADASA` nombrados en el cuerpo y presentes en la carpeta
- [x] Carpeta publicada y enlace pegado en los dos scripts, ambos regenerados
- [x] Enlace verificado **sobre los `.docx` emitidos** y sobre el `.pdf`: texto visible,
      destino del hipervinculo y cero placeholder
- [x] PDF del transmittal desde Word real (`exportar_pdf_word.py`, Word COM): **10 paginas,
      indice resuelto con numeros de pagina**, sin el placeholder de campo sin actualizar
- [x] Confirmar que la cadena es el hilo de submittals y no el de inspecciones

## Checklist post-envio

- [x] Cambiar BORRADOR por ENVIADO, con la hora de Chile tomada del respaldo
- [x] Archivar el respaldo del enviado en esta carpeta: `TRANSMITTAL 35.pdf`, 2 paginas, enviado 11:16
- [x] Master Deliverable Register con `update_register_n35.py`: 60 Codigo 1 / 22 Codigo 2 / 7 Codigo 3, cero sin codigo; 35 TMs / 81 entregas
- [x] Registro de compromisos: `PRG-27` cerrado, `PRG-25` reprogramado a la Rev C,
      `PRG-34` (CRITICA, vence 21-Ago) y `PRG-35` abiertos. Excel regenerado, gate
      `openpyxl_lint.py` en exit 0
- [x] Bitacora del README y Estado Vigente
