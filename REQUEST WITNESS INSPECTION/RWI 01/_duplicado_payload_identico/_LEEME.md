# ZIP duplicado por payload

Este ZIP llego por el hilo comercial de Bureau Veritas (asunto "SHOP INSPECTION MALASYA / COTIZACIONES Y CONSULTAS COMERCIALES") y su **contenedor** tiene un md5 distinto del que llego por el hilo del Request 001, porque Outlook recomprime al adjuntar. El **contenido es identico**: `Annex A.pdf` + `IR001-ADASA-BVM-28072026.pdf`.

| Archivo | md5 del contenedor |
|---|---|
| `RE_ SHOP INSPECTION ___ MALASYA ...zip` (este) | `a1efe98746fae1389315c1beb6b8cd1a` |
| `RE_ 25007 TALTAL - Request to witness inspection 001.zip` (canonico) | `0a8988fbf7c5129467bddbf1debfe26c` |

Se extrae **solo el canonico**. Se conserva este por trazabilidad del hilo de origen; no se borra.
