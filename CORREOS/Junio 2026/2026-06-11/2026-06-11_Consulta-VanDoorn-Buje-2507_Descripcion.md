# Consulta a Van Doorn — Inconsistencia de material en buje NPT (AISI 316 vs SAF2507)

**Estado:** BORRADOR
**Fecha:** 11 de junio de 2026
**De:** Luis Rivera — DIO ADASA
**Para:** [Contacto Van Doorn — completar nombre + correo]
**CC:** Víctor Gutiérrez (ADASA)
**Asunto:** Consulta — Material del buje NPT en conexión de instrumento (P22-DWG-06-006-005): AISI 316 vs SAF2507
**Output:** `2026-06-11_Consulta-VanDoorn-Buje-2507.docx`
**Script:** `crear_correo_vandoorn_buje_2507.py`

## Objeto

Consulta técnica (correo, no instrumento formal) a Van Doorn Ingeniería y Consultoría —autor de la
ingeniería de detalle mecánica (Cuadernillo de Isometrías, Compilado Rev 0)— por una incoherencia de
material en el buje de reducción de la toma de instrumento del plano P22-DWG-06-006-005.

## Hallazgo (verificado por render visual de las 26 láminas del cuadernillo)

- El buje `BUJE DE REDUCCIÓN, CABEZA HEXAGONAL, THDM NPT, AISI 316, ASME B16.11, CL3000`, tamaño
  `1"×1/2"`, aparece descrito como **AISI 316** pero su columna **SPEC** (misma fila) dice **SAF2507**.
- Ocurre idéntico en 2 láminas del plano -005:
  - **P22-DWG-06-006-005 — Lámina H.1, ítem 3** del cuadro LISTA DE MATERIALES.
  - **P22-DWG-06-006-005 — Lámina H.3, ítem 2** del cuadro LISTA DE MATERIALES.
- Las otras 24 láminas del cuadernillo son 100% HDPE PE100; no contienen 316 ni 2507.
- La incoherencia es **intra-fila** (descripción vs columna SPEC de la misma línea), no entre láminas.

## Posición ADASA (valor que se declara vinculante)

Para servicio de salmuera de rechazo concentrado rige **Super Duplex SAF2507 (UNS S32750)**; el AISI 316
es susceptible de picado por cloruro. El propio plano lo corrobora: el codo de transición inmediatamente
aguas arriba del buje (`PE100 × Super Duplex`, ítem 6 en H.1 e ítem 4 en H.3) ya está definido en Super
Duplex. Lectura: el valor correcto es SAF2507 y el "AISI 316" de la descripción es un arrastre de librería
genérica de fittings B16.11 CL3000. Se pide corregir la descripción a SAF2507 en ambas láminas (o
justificar si hubo intención distinta), incorporando el cambio en la próxima revisión del cuadernillo.

## Contexto Interno (No enviar)

- Van Doorn es el autor de la ingeniería de detalle mecánica del área 06 (ADASA). Esta consulta es
  coordinación interna ADASA↔su consultor de ingeniería; NO se envía a BW Water (regla Van Doorn interno).
- Caso semilla del usuario = lámina H.3 ítem 2 (su captura). Spot-check propio confirmó ambas filas.
- **Observación lateral NO incluida en este correo** (queda para una eventual segunda consulta): la
  columna SPEC del cuadro repite "HDPE ELECTRO FUSION" también en espárragos, válvulas y empaquetaduras
  (no es código de material confiable para esos ítems), y los espárragos figuran como `ASTM A193 Gr.B8`
  (= AISI 304) cuando el criterio del proyecto para salmuera es B8M (= 316). Confirmar con el usuario si
  se folda en esta consulta o se levanta aparte.
- Pendiente antes de enviar: completar destinatario Van Doorn (nombre + correo) y CC definitiva; correr
  `anti-ia revisar`.
