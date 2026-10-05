---
titulo: Convención de correo entrante — BW Water y Bureau Veritas
proyecto: salmuera-taltal
estado: VIGENTE
second_brain: skip
---

# Correo entrante — convención

> ## 🔴 EN HOLD desde el 06-Ago-2026
>
> **El barrido masivo por navegador está detenido.** Exige demasiada intervención humana para ser útil: la pestaña de Outlook Web se degrada cada quince o veinte operaciones y los clics dejan de registrarse **en silencio**, las descargas piden confirmación manual, y la sesión caduca.
>
> **La vía que lo reabre está identificada.** El puente COM de Outlook falla con `CO_E_SERVER_EXEC_FAILURE` por una sola causa: `HKCU:\Software\Microsoft\Office\16.0\Outlook\Preferences :: UseNewOutlook = 1`. Con esa marca, `OUTLOOK.EXE` redirige al Outlook nuevo y Classic nunca arranca. **Es un interruptor de usuario, no una política**, y Classic está intacto con la cuenta de ADASA declarada en el perfil. Volviendo a Classic, la skill `pst-extractor` hace la extracción entera por script, sin navegador. Ver `feedback_usenewoutlook_rompe_el_puente_com`.
>
> **Lo que sigue vigente:** la captura de **un correo puntual** por navegador funciona bien y está probada. Lo que no sirve es el barrido de decenas.
>
> Pendiente al momento del hold: 22 correos de BW Water del 3 al 6 de agosto, ya identificados uno por uno; el `_CONTACTOS.md`; y el modo `barrer` de la skill.

> Esta carpeta es el **domicilio único del correo recibido** de BW Water y Bureau Veritas. Antes de agosto de 2026 el proyecto no tenía ninguna regla de entrante: el correo recibido quedaba disperso en subcarpetas `RESPUESTA/`, suelto junto al saliente, o como PDFs llamados `Bandeja de entrada_ Luis Rivera Gonzalez - Outlook.pdf` — un nombre que aparece seis veces en seis carpetas distintas y no dice remitente, asunto ni fecha.

## Alcance

**Solo BW Water y Bureau Veritas.** El filtro es por dominio, no por lista de personas, porque las direcciones tienen capitalización inconsistente y hay alias cortos:

| Contraparte | Dominio | Nota |
|---|---|---|
| BW Water | `@bw-water.com` | Normalizar a minúsculas antes de comparar. Existe el alias `adzlan@` junto a `Adzlan.AbdRahim@` |
| Bureau Veritas | `@bureauveritas.com` | BV Chile (Luis Arcila, Carlo Montecinos) y BV Malasia (Emylia Rosli, Ahmad Hazwan, Wan Adli) |

Fuera de alcance por ahora: Van Doorn, L&A Ingeniería, Fedco, proveedores y el correo interno de Aguas Antofagasta. Se siguen archivando como hasta ahora.

## Regla de oro: se captura una vez, el payload va a su destino de siempre

El correo entra aquí. **Los adjuntos que tienen domicilio propio en el proyecto se mueven allá**, y el `_correo.md` deja el puntero. Así no se duplican los árboles que ya usan el Master Register, los transmittals y el registro de compromisos.

| Tipo | Cómo se reconoce | Los adjuntos van a |
|---|---|---|
| `submittal` | Asunto `TALTAL: DOCUMENT SUBMISSION 25007-00NN` | `ENTREGAS_BWWATER/ENTREGA NN/` |
| `rwi` | Asunto `Request to witness inspection 0NN` | Formulario de solicitud de BW: `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/03 SOLICITUDES BW (RWI)/RWI NNN AAAA-MM-DD/`. Registro de prueba del fabricante del día: la carpeta del informe BV de ese día en `04 INFORMES BV/`; si el informe aún no llega, queda en `adjuntos/` hasta que llegue |
| `informe-bv` | Remitente `@bureauveritas.com`, informes y coordinación | Informe y anexo: `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/04 INFORMES BV/IRNNN AAAA-MM-DD/`, y una fila nueva en su `_REGISTRO_INSPECCIONES_BV.md`. Coordinación sin informe: `05 CORREOS/` del mismo frente. El mapa completo está en el `_LEEME.md` del frente |
| `rfi` | Formulario `25007-RO-RFI-NNNN` | `PROGRAMA y CONTRATO/RFI/RFI N/` |
| `programa` | Cronograma, tracker de procura, Progress Update | La carpeta del frente que corresponda |
| `notificacion` | Avisos societarios, cambios de organización | Se quedan en `adjuntos/` |
| `comercial` | Cotizaciones, facturas, propuestas | La carpeta del frente, o `adjuntos/` |
| `otro` | Lo que no calce | Se quedan en `adjuntos/` |

> **`PAQUETE_INSPECCION_BV/` no se toca nunca.** Hay un enlace Synology publicado a Bureau Veritas desde el 21-Jul-2026; mover o renombrar esa carpeta rompe un enlace externo vivo. Si un correo trae una versión nueva de algo que está ahí, se deja en `adjuntos/` y se avisa — el reemplazo es decisión aparte.

## Estructura

```
CORREOS/_RECIBIDOS/
  _LEEME.md                                   ← este archivo
  _REGISTRO.md                                ← índice tabular, una fila por correo
  _REGISTRO.xlsx                              ← DERIVADO, se regenera, nunca se edita a mano
  scripts/
  [Mes YYYY]/
    YYYY-MM-DD_<remitente>_<asunto-slug>/
      _correo.md                              ← metadatos + cuerpo íntegro
      captura.png                             ← render del mensaje (opcional, evidencia visual)
      adjuntos/                               ← solo los que NO tienen destino propio
```

El nivel `[Mes YYYY]/` replica la convención del correo saliente, para que el árbol se lea igual en las dos direcciones.

**El nombre de la carpeta del mensaje lleva fecha, remitente y asunto.** Es exactamente lo que hoy falta en los archivos dispersos. Se construye con `sanitize()`: sin acentos, sin caracteres prohibidos por Windows, espacios a guion bajo. Si el nombre supera el límite de 260 caracteres de la ruta, el asunto se acorta a 40, luego a 20, y en último caso se usa la fecha más un hash corto.

## El `_correo.md`

Frontmatter con lo que permite deduplicar y buscar; el cuerpo íntegro después.

```yaml
---
mensaje_id: AAkALgAAAAAAHYQDEapmEc2byACqAC_EWg0A...   # de la URL de Outlook Web
fecha: 2026-05-26T09:00
remitente: Fadey Kassim <Fadey.Kassim@bw-water.com>
para: Luis Rivera Gonzalez
cc: Shane Banks; Eduardo Yamauchi
asunto: "Notification of the sale of BW Water to De Nora"
contraparte: BW WATER
tipo: notificacion
adjuntos:
  - archivo: "Notification of sale of BW Water-...pdf"
    tamano: "69 KB"
    destino: "adjuntos/"
enlaces:
  - https://denora.com/en/newsroom/press-releases/2026/De-Nora-to-acquire-BW-Water
second_brain: capture
type: correo
project: salmuera-taltal
date: 2026-05-26
---
```

Después del frontmatter va el cuerpo **íntegro**, no un resumen. Si el correo es parte de un hilo, se captura el mensaje que se está leyendo; el hilo completo no se reconstruye.

## Deduplicación

**La clave primaria es el `mensaje_id`**, que sale de la URL de Outlook Web (`.../mail/inbox/id/<id>`). Es estable: un correo ya capturado no se vuelve a capturar aunque cambie de carpeta, se marque como no leído o se reenvíe.

Se guarda **hasheado**, no crudo: `sha1(<id de la URL>)` truncado a 16 caracteres hexadecimales. Dos razones. La identificación es igual de buena para deduplicar, y el identificador crudo de Outlook es una cadena base64 larga que los filtros de seguridad del navegador bloquean al devolverla desde un script en la página. El hash se calcula en `capturar_correo.py`, que acepta el identificador crudo o el ya hasheado.

Clave secundaria, para el caso de que la URL no dé identificador: la tupla `(fecha_YYYY-MM-DD_HHMM, asunto en minúsculas truncado a 30)`, que es la misma que usa `pst-extractor`. No se usa el identificador interno de Outlook, que falla cuando el mismo correo está copiado en varias carpetas.

**Correr el barrido dos veces no debe crear nada la segunda vez.** Si lo hace, hay un defecto.

Para adjuntos, la regla del proyecto ya está escrita y se mantiene: **deduplicar por hash del contenido, nunca del contenedor.** Outlook recomprime los ZIP al reenviar, de modo que dos adjuntos con contenido idéntico dan md5 distinto. El duplicado se mueve a `_duplicado_payload_identico/` con un `_LEEME.md` que registre ambos hashes; no se borra.

## El `_REGISTRO.md`

Tabla, no narración. **La Bitácora del README es el único eje cronológico del proyecto** y este registro no puede ser un segundo eje: es un índice durable, del mismo género que el Índice de Transmittales.

Columnas: `Fecha | Contraparte | Remitente | Asunto | Tipo | Adj. | Destino | Carpeta`

Los correos que merezcan aparecer en la Bitácora se proponen aparte, uno por uno, y los aprueba el usuario antes de escribirse. Un correo capturado no genera entrada de Bitácora automáticamente.

El `.xlsx` es derivado: se regenera desde los frontmatter con `generar_registro.py` y **nunca se edita a mano**, igual que el registro de compromisos. Gate antes de darlo por bueno: `openpyxl_lint.py` en cero, y abrir el archivo renderizado — el defecto de formato numérico es visual y no aparece leyendo celdas.

## El procedimiento de captura

No hay vía programática al buzón. El conector de Microsoft 365 está autenticado con la cuenta de LRG Ingeniería, y el tenant de Aguas Antofagasta exige aprobación de administrador para la aplicación de Anthropic. El Outlook nuevo no expone COM ni deja caché local. **Queda la sesión autenticada de Outlook Web en Chrome**, que es la que se usa.

Pasos, con lo verificado sobre la interfaz:

1. **Sesión.** Chrome abierto en `outlook.office.com/mail/` con la cuenta de Aguas Antofagasta. Sin sesión viva no hay captura; esto no corre desatendido.
2. **Barrido.** Listar la bandeja y quedarse con los remitentes de los dos dominios del alcance. Descartar los que ya tengan su `mensaje_id` en el registro.
3. **Por cada correo nuevo, abrirlo y extraer:**
   - El `mensaje_id` de la URL.
   - Del árbol de accesibilidad: asunto, remitente, fecha y la lista de adjuntos **con nombre real y tamaño**.
   - El cuerpo **con un script en la página**. Es la única vía que funciona, y está verificada:

     ```js
     const el = document.querySelector('[aria-label="Cuerpo del mensaje"], [aria-label="Message body"], div[role="document"]');
     const texto   = el.innerText.replace(/ /g, ' ').trim();
     const enlaces = [...el.querySelectorAll('a[href^="http"]')].map(a => a.href);
     ```

     Las dos alternativas **no** sirven, y conviene no volver a intentarlas: el árbol de accesibilidad trunca cada párrafo alrededor de los cien caracteres, y el extractor de texto plano de la página falla con tiempo de espera agotado porque Outlook Web es una aplicación de página única que nunca alcanza el estado `document_idle`.
   - Los enlaces, que sí salen completos del árbol con su URL.
4. **Adjuntos.** Descargarlos es operación con permiso explícito del usuario, caso a caso, declarando nombre, origen y tamaño. Caen en la carpeta de descargas y desde ahí se mueven al destino que fije la tabla de ruteo.
5. **Escribir** con `capturar_correo.py` y regenerar el registro con `generar_registro.py`.

> **Nunca abrir el diálogo de impresión de Chrome.** Es una ventana modal que bloquea la automatización hasta que alguien la cierre a mano. Si hace falta un PDF del correo, lo imprime el usuario.

## Lo que no funciona en Outlook Web, verificado

Outlook Web es una aplicación de página única que nunca queda inactiva y que virtualiza la lista de mensajes. Eso rompe cuatro cosas que uno intentaría por instinto. Están anotadas para no volver a perder tiempo en ellas.

| Qué se intenta | Qué pasa | Qué usar en su lugar |
|---|---|---|
| Extractor de texto plano de la página | Falla siempre: espera el estado `document_idle` y agota los 45 segundos | Script en la página con `innerText` |
| Lector de estructura y buscador de elementos | Funcionan de forma intermitente, por la misma dependencia del estado inactivo | Script en la página; dejar el lector de estructura solo para localizar adjuntos |
| `.click()` sintético sobre una fila de la lista | No cambia el panel de lectura. La lista está virtualizada y solo responde a eventos de mouse reales | Clic real por coordenadas, tras una captura de pantalla para ubicar la fila |
| `await` largo dentro del script de página | Desconecta la extensión del navegador | Scripts cortos y sincrónicos; si hay que esperar, esperar entre llamadas |

| Eventos de mouse sintéticos completos (`pointerdown`, `mousedown`, `mouseup`, `click`) | Tampoco cambian el panel. Outlook exige eventos confiables, que un script no puede falsificar | Clic real por coordenadas |
| Navegar a `.../mail/inbox/id/<algo>` con un identificador construido | **Rompe la sesión y fuerza reautenticación.** El `id` de la fila de la lista tiene 28 caracteres y **no** es el identificador del mensaje | No construir URLs de mensaje. Entrar solo por `outlook.office.com/mail/` y navegar con la interfaz |

Además, la captura de pantalla falla con tiempo de espera agotado cuando la página está ocupada, **mientras el script en la página sigue funcionando**. Son dos vías de inyección distintas: que una falle no dice nada de la otra. **Dos fallos consecutivos de captura son señal de parar**, no de insistir.

**Cuando la sesión caduca no hay nada que hacer desde aquí.** La página redirige a `login.microsoftonline.com` y el re-login es del usuario: ingresar credenciales está fuera de lo que la automatización puede o debe hacer. La skill debe detectar el redirect y detenerse con un aviso claro, no intentar nada más.

## La pestaña se degrada: recargar cada 15 correos

**Outlook Web deja de responder a los clics después de unas quince o veinte operaciones de navegador seguidas.** No devuelve error: el clic se reporta como ejecutado y el panel de lectura simplemente no cambia. Observado dos veces, con el mismo cuadro clínico las dos.

Síntomas, en orden de aparición: la captura de pantalla empieza a agotar el tiempo de espera mientras el script de página sigue respondiendo · los clics dejan de cambiar el panel · el desplazamiento con rueda deja de mover la lista.

**La cura es recargar la pestaña.** Después de recargar, todo vuelve a funcionar de inmediato — la búsqueda, el clic, la rueda. No es un límite del método sino del estado acumulado de la aplicación.

**En el barrido:** recargar cada diez o quince correos, sin esperar a que falle. Y si dos extracciones seguidas devuelven el mismo asunto, es este problema: recargar antes de seguir, nunca persistir.

## Regla dura del barrido: verificar el asunto antes de persistir

**Cada extracción debe traer el encabezado, y el asunto del encabezado debe coincidir con el correo que se pretendía abrir.** Si no coincide, se descarta y se vuelve a localizar; no se persiste.

**Why:** es el modo de falla más peligroso del barrido y ya ocurrió. Al encadenar varios clic-y-extrae en una sola llamada usando coordenadas de una captura previa, **los tres clics devolvieron el mismo correo**: el diseño se movió tras el primero y los siguientes cayeron sobre filas equivocadas o sobre ninguna. Sin la comprobación del encabezado se habrían guardado tres copias del mismo mensaje bajo tres nombres distintos, cada una con su carpeta y su fila en el registro. La deduplicación no lo habría atrapado, porque las claves se construyen con el asunto que uno *creía* estar capturando.

**How to apply:**

- **Una captura de pantalla fresca antes de cada clic.** Las coordenadas envejecen en cuanto el panel de lectura cambia.
- **No encadenar varios clic-y-extrae** en una misma llamada por lotes. Sí se puede encadenar clic, espera y extracción de **un solo** correo; a partir del segundo hay que re-mirar.
- **Comparar el asunto del encabezado extraído contra el objetivo.** Solo si coinciden se arma el payload.
- Si el panel muestra *"Ver conversación"*, se está capturando el mensaje seleccionado del hilo, no el hilo entero. Es lo correcto, pero conviene saberlo.

## Los dos puntos que exigen a una persona

Todo lo demás de la cadena es determinista. Estos dos no, y conviene que la skill los anuncie en vez de quedarse colgada:

1. **Iniciar sesión** cuando caduca. Se detecta por el redirect a `login.microsoftonline.com`.
2. **Confirmar una descarga que Chrome retiene.** Los ZIP grandes quedan en la carpeta de descargas como `Sin confirmar NNNNNN.crdownload` con el tamaño completo, esperando que alguien pulse **Conservar** en la barra del navegador. Esa barra es interfaz del navegador, no contenido de la página, y `chrome://downloads` está bloqueado para la automatización. **No renombrar el `.crdownload` para saltarse la confirmación:** Chrome lo retiene por una razón y el archivo puede no estar finalizado.

La skill debe esperar el archivo final por un tiempo acotado y, si sigue en `.crdownload`, pedir la confirmación al usuario y reintentar, no dar el ZIP por perdido.

## Descarga de submittals que llegan por enlace

Desde el submittal `25007-0072` (06-Ago-2026) BW Water dejó de adjuntar los documentos y los publica en una carpeta de OneDrive propia (`heawater1-my.sharepoint.com/.../TALTAL/SUB OUT/<submittal>`). El enlace abre sin autenticación adicional si la sesión de Chrome ya tiene acceso.

**La carpeta suele traer más archivos de los que declara el cuerpo del correo.** En el 25007-0072 el correo lista cuatro documentos y la carpeta tiene siete: los cuatro PDF, el Submittal Form, y los **archivos nativos** de dos de los planos (15 y 38 MB), que el correo no menciona. Por eso el `_correo.md` se completa con la lista real de la carpeta, no con la tabla del remitente, y la diferencia se anota: es información de revisión, no ruido.

Procedimiento: abrir el enlace en pestaña aparte, pulsar `Descargar` sobre la carpeta —que baja todo en un ZIP—, esperar el archivo final, y desde ahí Python descomprime en `ENTREGAS_BWWATER/ENTREGA NN/` deduplicando **por hash del contenido, nunca del ZIP**.

**El identificador crudo del mensaje no se puede devolver desde un script de página**: los filtros de seguridad del navegador lo bloquean por parecer base64. Se lee de la URL de la pestaña, que sí es visible, y `capturar_correo.py` lo hashea.

## Verificación de cierre

- Barrido corrido dos veces: la segunda no crea carpetas ni filas.
- Cuerpo del `_correo.md` contrastado contra el mensaje en pantalla — la extracción trunca y hay que comprobar que no lo hizo.
- `openpyxl_lint.py` en cero sobre el `_REGISTRO.xlsx`.
- Adjuntos de un submittal en `ENTREGAS_BWWATER/ENTREGA NN/` y **no** duplicados aquí.
- `PAQUETE_INSPECCION_BV/` intacta: 43 archivos, mismo listado.
