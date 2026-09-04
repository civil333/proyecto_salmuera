# Objects — registro de objetos del set «ENTREGA 78»

Generado: 2026-08-17 09:48
Objetos con cuadro: 0 · códigos sin cuadro: 15 · láminas: 3

> Confianza: `counted` = tag contado en el text layer (verificable) · `schedule` = leído de cuadro sin conteo · `scaled` = derivado de geometría a escala · `assumed` = inferencia LLM. Ante mismatch cuadro↔conteo se reportan ambos y manda el conteo.

## Envolvente del set (sanity check)

- No computada (requiere `--vectors` + escala detectada).

**Regla de sanity check:** toda medición derivada que exceda la envolvente, o sea <1% de ella, es sospechosa — reportarla con ambos valores y verificar contra la lámina fuente.

## Objetos por tipo

_Sin objetos con cuadro detectados._

## Códigos sin cuadro (verificar tipo)

| Tag | Tipo | Cant (contada) | Desglose |
|-----|------|---------------:|----------|
| MZE-09-009 | — | 0 | — |
| FIL-09-001 | — | 2 | DWG-09 p2: 2 |
| BH-09-001 | — | 2 | DWG-09 p2: 2 |
| SIP-09-001 | — | 2 | DWG-09 p2: 2 |
| SIP-09-002 | — | 2 | DWG-09 p2: 2 |
| BOI-09-001 | — | 2 | DWG-09 p2: 2 |
| BOI-09-002 | — | 2 | DWG-09 p2: 2 |
| TK-09-001 | — | 2 | DWG-09 p2: 2 |
| REL-09-001 | — | 1 | DWG-09 p2: 1 |
| BH-09-002 | — | 2 | DWG-09 p2: 2 |
| FIL-09-002 | — | 2 | DWG-09 p2: 2 |
| TK-09-002 | — | 2 | DWG-09 p2: 2 |
| BDS-09-001/002 | — | 2 | DWG-09 p2: 2 |
| MZE-09-001 | — | 2 | DWG-09 p2: 2 |
| M3 | — | 12 | DWG-09 p2: 12 |

> Regex de códigos con riesgo de falso positivo: confirmar contra la lámina antes de usar en QTO.

## Cómo consultar

1. Cantidad/dimensión de objeto → esta tabla / `objects.json`; citar siempre el nivel de confianza.
2. Confianza `scaled`/`assumed`, dato ausente o mismatch (≠) → abrir el `drawing.md` de la lámina fuente y de ahí el tile de la zona.
3. Toda medición derivada pasa el sanity check de envolvente antes de reportarse.
