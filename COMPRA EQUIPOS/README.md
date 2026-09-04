# COMPRA EQUIPOS - BAE 12803 Modulo de Salmuera Taltal

> **Navegacion:** [← README Principal](../README.md) | [CLAUDE.md](../CLAUDE.md)

Procesos de compra directa de ADASA para equipos del proyecto.

---

## 1. Compra de Bombas

**Ubicacion:** `Compra de Bombas/`
**Estado:** En evaluacion tecnica

### Documentos Tecnicos
| Archivo | Codigo | Descripcion |
|---------|--------|-------------|
| P22-ET-06-005-001- HD Bbas Taltal.pdf | P22-ET-06-005-001 | Hoja de Datos - Bombas Taltal |
| SC80371-CV406762-REV1.pdf | SC80371-CV406762-REV1 | Cotizacion KSB Rev.1 (**Vigente**) |

### Documentos Administrativos
| Archivo | Descripcion |
|---------|-------------|
| PPTO PDA.xlsx/.pdf | Presupuesto PDA |
| SC PDA.xlsx/.pdf | Solicitud de Compra |

---

## 2. Compra de Valvulas

**Ubicacion:** `COMPRA DE VALVULAS/`
**Estado:** **KSB CV421060 Rev.1 - APPROVED** (31-Dic-2025)

### Cantidades Requeridas
| Tipo | DN | Cantidad |
|------|-----|----------|
| Mariposa | 4" (100mm) | 8 |
| Mariposa | 2" | 2 |
| Mariposa | 3" | 5 |
| Retencion (Check) | 4" (100mm) | 4 |
| **Total** | | **19** |

### Documentos Tecnicos
| Archivo | Codigo | Descripcion |
|---------|--------|-------------|
| P22-ET-06-006-002-0 Especificaciones valvulas Taltal | P22-ET-06-006-002-0 | Especificacion Tecnica |
| P22-LI-06-006-002-0 (LI Valvulas) +PR | P22-LI-06-006-002-0 | Lista de Valvulas con PR |

### Ofertas Recibidas y Evaluacion (29-Dic-2025)

| Proveedor | Codigo | Total USD | Cumple ET | Estado |
|-----------|--------|-----------|-----------|--------|
| **KSB** | CV421060 | 13.318* | **PARCIAL** | Consulta tecnica enviada |
| HMT | 1836 | 9.495 | **NO** | Rechazada |
| IMPOBAR | 351313 | ~834 | **NO** | No comparable |

*Presupuesto referencial ADASA: USD 11.431

### Resultado Evaluacion Tecnica

| Requisito | Especificacion | KSB | HMT | IMPOBAR |
|-----------|----------------|:---:|:---:|:-------:|
| Disco Ebonita (4"/2") | Requerido | OK | NO | NO |
| Disco CF8M (3") | Requerido | OK | NO | NO |
| Asiento EPDM | Requerido | OK | NO | NO |
| Super Duplex 2507 (PREN>40) | Requerido | OK (~42) | NO (~35) | NO |
| Limit switch mecanico | Requerido | ALS200 | NO | NO |
| Reductor manual | Requerido | OK | OK | NO (Palanca) |
| Repuestos PEM | Requerido | Incluido | NO | NO |
| Servicio terreno | Requerido | 2 dias | NO | NO |

**Deficiencias KSB a corregir:**
1. Items 7-8 (disco Rilsan) NO cumplen - Excluir de oferta
2. Falta 1 valvula mariposa 4" con disco ebonita
3. Incoterm Bodega Santiago - Requiere DDP Taltal
4. Confirmar API 594/598 y asiento EPDM en check valves

**Rechazo HMT:** Material Duplex 2205 (PREN ~35) no cumple requisito Super Duplex 2507 (PREN >40)

**Rechazo IMPOBAR:** Valvulas industriales basicas sin especificaciones tecnicas

### Archivos de Revision
| Archivo | Descripcion |
|---------|-------------|
| 2025-12-29_Revision-Ofertas-Valvulas.md | Checklist comparativo completo |
| OFERTAS/oferta HMT 1836_extracted.txt | Texto extraido oferta HMT |
| OFERTAS/Oferta KSB CV421060_extracted.txt | Texto extraido oferta KSB |

### Catalogos de Referencia
| Archivo | Descripcion |
|---------|-------------|
| ALS200 - C230.pdf | Catalogo actuadores ALS200 |
| ISORIA 10 844.1_11-30 folleto de la serie.pdf | Catalogo valvulas mariposa ISORIA |
| MS_MC.PDF | Catalogo general MS/MC |

### Documentos Administrativos
| Archivo | Descripcion |
|---------|-------------|
| PPTO PDA.xlsx/.pdf | Presupuesto PDA (USD 11.431) |
| SC PDA.xlsx/.pdf | Solicitud de Compra |

---

## Notas

- Los archivos `.xlsx` son editables, los `.pdf` son para distribucion
- PPTO PDA = Presupuesto Pedido de Adquisicion
- SC PDA = Solicitud de Compra Pedido de Adquisicion
- Archivos `*_extracted.txt` son textos extraidos de PDFs para analisis

---

## Proximos Pasos

1. **Bombas:** Esperar respuesta consulta tecnica KSB
2. **Valvulas:** Emitir orden de compra (oferta KSB Rev.1 aprobada)

---

## Documentos Relacionados

| Documento | Ubicacion |
|-----------|-----------|
| Lista Equipos ADASA | `BASES TECNICAS/INGENIERIA BASICA/md/P22-LI-06-005-001_LISTA-EQUIPOS.md` |
| Lista Valvulas ADASA | `BASES TECNICAS/INGENIERIA BASICA/md/P22-LI-06-006-002_LISTA-VALVULAS.md` |
| HD Bomba Alimentacion | `BASES TECNICAS/INGENIERIA BASICA/md/P22-ET-06-005-001_HD-BOMBA-ALIMENTACION.md` |
| README Principal | [../README.md](../README.md) |

---

*Ultima actualizacion: 28 de enero de 2026*
