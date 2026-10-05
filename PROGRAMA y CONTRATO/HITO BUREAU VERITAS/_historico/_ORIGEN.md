# Mapa de las tres carpetas del frente Bureau Veritas

El frente de inspección de taller vive en **tres árboles paralelos** que crecieron por hilo de correo, no por diseño. Ninguno se mueve: `PAQUETE_INSPECCION_BV` está publicado a Bureau Veritas por link Synology desde el 21-Jul-2026 y moverlo rompería un enlace ya enviado a un tercero. Este archivo declara qué vive en cada uno.

| Carpeta | Qué contiene | Rol |
|---|---|---|
| `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/` | NT-002 de designación, oferta BV 600049, calendario Hold/Witness, `PAQUETE_INSPECCION_BV/` (lo que BV tiene en mano), `CORREOS VBV-BW/` (hilo Request 001 y respuestas) | **Coordinación y documentación entregada al inspector.** Es el árbol canónico del hito |
| `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/` | ZIP y adjuntos del Request 001 tal como llegaron: `BW Water - PMI Witness NOI001.pdf` (Notice of Inspection) + `P22-BA-09-000-004_0_ITP.pdf` | **Adjuntos crudos del Request 001**, extraídos del correo |
| `REQUEST WITNESS INSPECTION/` (raíz) | `RWI 01/` (con el informe de inspección de BV, `IR001-ADASA-BVM-28072026.pdf`) y `RWI 02/` (segunda solicitud, con ITP Rev 0 + NDE Plan Rev C) | **Ciclo de solicitudes y resultados de inspección**, una carpeta por Request |

## Documentos con dos nombres

- `Annex A.pdf` (dentro del ZIP de `RWI 01`) es **byte-idéntico** a `BW Water - PMI Witness NOI001.pdf` (`md5 82aa5061…`) de `BV INSPECTION/INSPECTION 01/`. Canónico: el nombre del emisor, `BW Water - PMI Witness NOI001.pdf`. Se extrae una sola vez.
- `P22-BA-09-000-004_0_ITP.pdf` aparece en `BV INSPECTION/INSPECTION 01/` y dentro del ZIP de `RWI 02`. Ambos son **byte-idénticos al de la ENTREGA 57** (`md5 81f8dc64…`). No se re-extrae: la extracción vive en `ENTREGAS_BWWATER/ENTREGA 57/md/`.
- `P22-BA-09-000-005_C_ NDE Plan.pdf` (ZIP de `RWI 02`) es idéntico página a página al de la **ENTREGA 61**, sin anotaciones en ninguno de los dos.

## Regla de deduplicación

Los ZIP que llegan por hilos distintos tienen **md5 de contenedor distinto** aunque el payload sea el mismo: Outlook recomprime al adjuntar. **Deduplicar siempre por hash del contenido, nunca del ZIP.** Caso registrado en `RWI 01/_duplicado_payload_identico/_LEEME.md`.
