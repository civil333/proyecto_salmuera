---
titulo: Referencias de acero estructural en Chile — perfiles, calidades y combinaciones de carga
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# Referencias de acero estructural en Chile

Se reunieron el 5-Oct-2026 para el Transmittal N42. El N42 exige que el yugo de izaje (`P22-DWG-09-005-019` Rev A) se homologue a perfiles soldados de fabricación nacional, que se detallen los empalmes y que su cálculo use las combinaciones de la NCh3171. **Son catálogos de proveedor y referencias normativas, no documentos contractuales.** Ante BW Water se cita el Criterio de Diseño que BW Water emitió y ADASA aprobó, no estos catálogos.

## Archivos

| Archivo | Origen | md5 | Qué respalda |
|---|---|---|---|
| `pdf/Prodalam_Catalogo-Tecnico-Vigas-de-Acero_2019.pdf` | https://www3.prodalam.cl/wp-content/uploads/2019/07/catalog_vigas_acero.pdf | `13773627c263bb3abfbfb0e937b7b90c` | Ver detalle abajo |
| `pdf/Cintac_Tubos-y-Perfiles_Ed-Enero-2014.pdf` | https://ingenieria-civil.github.io/chile/catalogos/cintac/catalogo_tubos_perfiles.pdf (espejo; Cintac ya no lo publica) | `ce6ba368c09b3d79d7fa9dbbbacef479` | Tubos ASTM A500 y perfiles plegados (costaneras, canales, ángulos) en A270ES y A240ES. **Sin vigas soldadas ni perfiles W** |

Qué respalda el catálogo de Prodalam:
- El W 250 x 73,0 (= W 10 x 49) se vende **importado**, según norma ASTM A6, en **ASTM A572 grado 50** y en largo normal de 6 y 12 m (páginas 15 y 24; códigos SAP 29469 y 34417).
- La tabla de equivalencias europea contra americana lo empareja con el HEA 260 en ASTM A36.
- Las vigas soldadas IN y HN van según NCh 730 Of.71 y NCh 428 Of.57, en ASTM A-36 o A572 Gr. 50, en **"Largo normal Variables a pedido"** (páginas 26 a 37).

Extracción de texto en `md/` con PyMuPDF; los dos catálogos tienen capa de texto.

## Leído en línea y no descargado

| Fuente | URL | Qué dice (lectura) | Nivel |
|---|---|---|---|
| Cintac, catálogo de vigas soldadas IN | https://pdfcoffee.com/vigas-in-cintac-2-pdf-free.html (espejo; no hay PDF oficial) | Tolerancias según NCH 730.Of71 y soldaduras según AWS D 1.1. **"Largo: A pedido"**. **"Calidades normales: A36 - A572 G50"**. Producto fabricado a pedido según disponibilidad de materia prima. Serie desde IN 25X72,7 (H 250, B 200, t 20, e 6, Ix 11.070 cm⁴, Wx 886 cm³, según resumen) hacia abajo | Texto del espejo leído literal; propiedades de la IN 25 por resumen web |
| Cintac, página de vigas laminadas | https://www.cintac.cl/vigas-laminadas/ | "Linea de perfiles laminados Cintac, abarca 5 tipos de vigas: UPN, IPE, IPN, HEA, HEB [...] fabricado en medidas estándar de 6 y 12 metros." **Sin perfiles W** | Literal (5-Oct-2026). El sitio no publica catálogos técnicos en PDF |
| NCh203 Of.2006, *Acero para uso estructural - Requisitos* | https://pdfcoffee.com/nch-203-of2006-4-pdf-free.html | Ver detalle abajo | [Probable]: resumen web. **Verificar contra la copia licenciada de ADASA antes de citar cláusulas** |
| NCh3171, *Diseño estructural - Disposiciones generales y combinaciones de carga* | https://ecommerce.inn.cl/nch3171201760757 | Norma de combinaciones de carga, ASD y LRFD. La versión 2017 reemplazó a la de 2010. El Criterio de Diseño aprobado de BW Water cita la de 2010 (sección D, Tablas 6 y 7) | Ficha del INN |
| Manual ICHA de diseño en acero (2010) | https://pdfcoffee.com/manual-icha-2010pdf-pdf-free.html | Incluye las series norteamericanas AISC, *"especificados normalmente en los proyectos hechos para nuestro país por proveedores extranjeros"*. Trae perfiles soldados HR, H y PH que reemplazan a los W de AISC, con diferencia de peso de hasta 10 % (Tabla 2.1.3, "Perfiles soldados que reemplazan a perfiles W AISC - Secciones HR") | [Probable]: resumen web |

Qué dice la NCh203 Of.2006 según la lectura:
- **Alcance (1.3).** Perfiles laminados, plegados, conformados en frío o soldados.
- **Calidades.** Tabla 2: A240ES, A270ES, A345ES, M345ES, Y345ES. Tabla 3, para cargas sísmicas o dinámicas: A250ESP y A345ESP.
- **Anexo C (informativo).** ASTM A36 y A572 Gr50 *"corresponden a los similares A250ESP y A345ESP. La condición de similitud no necesariamente significa equivalencia"*. La Tabla C.1 indica las verificaciones de Fy/Fu, Fy y tenacidad para uso sísmico; el A992 Gr50 cumple.
- **5.2.1.** La certificación la otorga un organismo acreditado, con ensayos de laboratorio acreditado.

## Cómo se usó en el N42

- **Perfiles.** HEA, HEB y W son laminados importados. El equivalente de fabricación nacional es la viga soldada IN o HN (NCh 730). El comentario a BW Water pide IN o HN y no afirma diferencias de peso. El HEB 240 es más pesado para un módulo similar (83,2 kg/m y Wx 938, contra 72,7 kg/m y Wx 886 de la IN 25x72,7), pero el HEA 260 queda parejo.
- **Empalmes.** Las vigas soldadas se fabrican a largo variable a pedido, así que el comentario no afirma que se vendan en 12 m. Pide el detalle de empalme de los largueros de 12.776 mm, las uniones de esquina y las vigas intermedias, porque el plano no muestra ninguno.
- **Calidad y combinaciones.** Se citan contra el Criterio de Diseño `P22-CD-09-005-003` Rev 0 aprobado:
  - *"Structural steel shall conform to NCh203"*;
  - sección D, combinaciones NCh3171 en ASD (Tabla 7) y en LRFD (Tabla 6);
  - sección F, factores de izaje 1,35D y 2,0D.
