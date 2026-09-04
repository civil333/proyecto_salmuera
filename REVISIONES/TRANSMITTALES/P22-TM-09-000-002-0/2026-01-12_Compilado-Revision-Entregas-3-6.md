---
titulo: "TECHNICAL REVIEW TRANSMITTAL N2"
subtitulo: "Second Stage RO Brine Module - Entregas 3, 4, 5, 6"
codigo: "P22-TM-09-000-002-0"
version: "PRELIMINAR"
autor: "ADASA + Asesor Van Doorn"
empresa: "ADASA"
nombre_planta: "TALTAL"
cliente: "BW Water Americas Inc."
preparado_por: "Luis Rivera"
revisado_por: "Asesor LH Van Doorn"
aprobado_por: "Pendiente"
tipo_documento: "Transmittal"
proyecto: "BAE 12803 - Modulo de Salmuera Taltal"
---

# COMPILADO DE REVISION TECNICA N°2 - ADASA

**Fecha:** 12 de enero de 2026
**Proyecto:** BAE 12803 - Modulo de Salmuera Taltal
**Revision:** ADASA + Asesor Van Doorn
**Estado:** PRELIMINAR - Pendiente respuesta BW Water a TM N°1

---

## 1. INFORMACION GENERAL

| Campo | Valor |
|-------|-------|
| **Submittal 0003** | 25007-0003 (16-Dic-2025) - 1 documento |
| **Submittal 0004** | 25007-0004 (24-Dic-2025) - 1 documento |
| **Submittal 0005** | 25007-0005 (06-Ene-2026) - 2 documentos |
| **Submittal 0006** | 25007-0006 (08-Ene-2026) - 3 documentos |
| **Total documentos** | 7 |
| **Response Codes** | 1=Approved, 2=Approved as noted, 3=To be revised as noted, 4=Rejected, 5=For Information |

---

## 2. RESUMEN EJECUTIVO

### 2.1 Estadisticas por Submittal

**Submittal 25007-0003 (Entrega 3):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 2 - Approved as noted | 1 | 100% |

**Submittal 25007-0004 (Entrega 4):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 2 - Approved as noted | 1 | 100% |

**Submittal 25007-0005 (Entrega 5):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 3 - To be revised | 2 | 100% |

**Submittal 25007-0006 (Entrega 6):**
| Response | Cantidad | Porcentaje |
|----------|----------|------------|
| 2 - Approved as noted | 2 | 67% |
| 3 - To be revised | 1 | 33% |

### 2.2 Observaciones Criticas Van Doorn

| # | Observacion | Documento | Gravedad |
|---|-------------|-----------|----------|
| 1 | **Lineas PVC en zona SDSS:** Hay lineas de PVC dentro del rectangulo definido como SDSS. Revisar consistencia de materiales. | P&ID | **ALTA** |
| 2 | **Limites de bateria:** Indicar claramente limites de suministro ADASA/BW Water con flanges en todos los puntos de conexion. | P&ID | **MEDIA** |
| 3 | **TAGs de lineas:** Indicar TAGs de lineas con diametros en todos los tramos. | P&ID | **MEDIA** |
| 4 | **Tabla membranas:** No se atendio el comentario de Rev A: Indicar cantidades de membranas para cada modelo/etapa. | UHPRO System | **MEDIA** |

---

## 3. TABLA CONSOLIDADA POR DOCUMENTO

| # | Submittal | Codigo | Descripcion | Comentarios | **Estado Final** |
|---|-----------|--------|-------------|-------------|------------------|
| 1 | 0003 | P22-DWG-09-009-002-A | P&ID | 8 obs Van Doorn + 6 obs ADASA. Pendiente Process Calc. | **2 - Approved as noted** |
| 2 | 0004 | P22-CD-09-004-001-A | Control Architecture | 6 obs ADASA. Pendiente PLC DS. | **2 - Approved as noted** |
| 3 | 0005 | P22-CD-09-005-002-A | A/C Thermal Calculation | Carga termica subdimensionada, falta config n+1. | **3 - To be revised** |
| 4 | 0005 | P22-ITEM-09-009-012-A | Static Mixer | Material FRP→PVC, dimensiones diferentes. Justificar. | **3 - To be revised** |
| 5 | 0006 | P22-ET-09-009-001-B | UHPRO System | 1 obs Van Doorn (tabla membranas). Codif corregida. | **2 - Approved as noted** |
| 6 | 0006 | P22-ET-09-009-003-B | CIP Pump | VFD→Partida directa, motor diferente. | **2 - Approved as noted** |
| 7 | 0006 | P22-ET-09-009-006-B | CIP Cartridge Filter | Cartuchos 19→17, tipo cierre diferente. | **3 - To be revised** |

---

## 4. ESTADISTICAS CONSOLIDADAS

### 4.1 Estados Finales Consolidados

| Veredicto | E3 | E4 | E5 | E6 | Total | % |
|-----------|----|----|----|----|-------|---|
| **1 - Approved** | 0 | 0 | 0 | 0 | 0 | 0% |
| **2 - Approved as noted** | 1 | 1 | 0 | 2 | **4** | 57% |
| **3 - To be revised** | 0 | 0 | 2 | 1 | **3** | 43% |
| **4 - Rejected** | 0 | 0 | 0 | 0 | 0 | 0% |
| **Total** | 1 | 1 | 2 | 3 | **7** | 100% |

### 4.2 Comparacion con Transmittal N°1

| Metrica | TM N°1 (E1+E2) | TM N°2 (E3-E6) | Tendencia |
|---------|----------------|----------------|-----------|
| Documentos | 20 | 7 | - |
| Approved | 20% | 0% | ↓ |
| Approved as noted | 15% | 57% | ↑↑ |
| To be revised | 40% | 43% | = |
| Rejected | 25% | 0% | ↓↓ |

**Conclusion:** Mejora significativa. Ningun documento rechazado. Mayor proporcion de aprobaciones con notas.

---

## 5. OBSERVACIONES ASESOR VAN DOORN (12-Ene-2026)

### 5.1 P&ID (P22-DWG-09-009-002-A) - 8 Observaciones

| # | Codigo | Observacion | Impacto |
|---|--------|-------------|---------|
| VD-01 | Limites bateria | Indicar limite de suministro ADASA/BW Water con flange | MEDIO |
| VD-02 | **PVC en zona SDSS** | Hay lineas de PVC dentro del rectangulo definido como SDSS. Revisar. | **ALTO** |
| VD-03 | TAGs de linea | Indicar TAG de linea | MEDIO |
| VD-04 | Drenaje | Debiera ir a drenaje esta corriente | MEDIO |
| VD-05 | Limite bateria | Indicar limite de suministro BW/ADASA con flange + TAG + diametro | MEDIO |
| VD-06 | Conexion CIP | Va al CIP TANK TK-09-001 | BAJO |
| VD-07 | Bomba HP | Incluir caracteristicas de esta bomba | MEDIO |
| VD-08 | Conexion etapas | Viene de 1 y 2 etapa en rigor | BAJO |

### 5.2 UHPRO System (P22-ET-09-009-001-B) - 1 Observacion

| # | Codigo | Observacion | Impacto |
|---|--------|-------------|---------|
| VD-01 | Tabla membranas | No se atendio el comentario de Rev A: Indicar cantidades de membranas para cada modelo/etapa. | **MEDIO** |

### 5.3 Static Mixer, CIP Pump, CIP Filter

**Van Doorn:** Sin comentarios tecnicos.

**Nota:** Esto NO es una contradiccion con ADASA. Van Doorn evalua desde perspectiva **TECNICA** (¿funciona?), mientras ADASA evalua desde perspectiva **CONTRACTUAL** (¿cumple la oferta?). Ambos enfoques son complementarios.

---

## 6. ANALISIS DE INCONSISTENCIAS ADASA vs VAN DOORN

### 6.1 Omision ADASA Detectada - VD-02 (P&ID)

> **AUTOCRITICA:** La observacion VD-02 de Van Doorn (lineas PVC en zona SDSS) identifica una inconsistencia grafica en el P&ID que **NO fue detectada** en la revision ADASA.

**Analisis:**
- ADASA verifico que la especificacion de materiales en la leyenda indica Super Duplex para lineas de alta presion
- Van Doorn detecto que existen lineas con simbologia PVC dibujadas DENTRO del area demarcada como zona SDSS
- Esto representa una inconsistencia entre la leyenda y el diagrama

**Leccion aprendida:** Futuras revisiones ADASA deben incluir verificacion grafica detallada de consistencia entre leyenda y simbologias del P&ID.

### 6.2 Brecha de Proceso - UHPRO Membranas

> **NOTA:** ADASA no tenia acceso a los comentarios de Van Doorn sobre Rev A al momento de emitir la revision v1.0.

**Contexto:**
- Van Doorn reviso Rev A y solicito tabla de cantidades de membranas
- BW Water emitio Rev B sin atender el comentario
- ADASA reviso Rev B verificando las cantidades correctas, pero no la PRESENTACION

**Accion de mejora:** Establecer protocolo donde Van Doorn envia comentarios ANTES de que ADASA emita revision.

---

## 7. ACCIONES REQUERIDAS BW WATER (CONSOLIDADAS)

### 7.1 Acciones Criticas (Prioridad ALTA)

| # | Accion | Documento | Responsable |
|---|--------|-----------|-------------|
| 1 | Revisar y corregir lineas PVC dentro de zona definida como SDSS | P&ID | BW Water |
| 2 | Completar calculo termico A/C con TODAS las cargas (real ~11-15 kW vs 5.96 kW calculado) | A/C Thermal Calc | BW Water |
| 3 | Incluir configuracion n+1 (2 unidades A/C segun ET 5.1.11 y Oferta) | A/C Thermal Calc | BW Water |
| 4 | Incluir tabla clara de cantidades membranas por modelo/etapa (6x7=42 UHP, 4x7=28 SR) | UHPRO System | BW Water |

### 7.2 Acciones Tecnicas (Prioridad MEDIA)

| # | Accion | Documento | Responsable |
|---|--------|-----------|-------------|
| 5 | Indicar limites de bateria con flanges en todos los puntos de conexion | P&ID | BW Water |
| 6 | Agregar TAGs de lineas con diametros | P&ID | BW Water |
| 7 | Justificar cambio material mezclador FRP→PVC | Static Mixer | BW Water |
| 8 | Confirmar eficiencia mezcla con nuevas dimensiones (velocidad 71% menor) | Static Mixer | BW Water |
| 9 | Justificar reduccion de cartuchos 19→17 | CIP Filter | BW Water |
| 10 | Confirmar tipo de cierre (Swing Bolts vs Rapido requerido) | CIP Filter | BW Water |

### 7.3 Acciones Administrativas (Prioridad BAJA)

| # | Accion | Documento | Responsable |
|---|--------|-----------|-------------|
| 11 | Confirmar equivalencia Koflo vs KOMAX | Static Mixer | BW Water |
| 12 | Nota tecnica sobre cambio orientacion Vertical→Horizontal | CIP Filter | BW Water |

---

## 8. PROTOCOLO DE REVISION PROPUESTO

### 8.1 Flujo Actual (Problematico)

```
BW Water → ADASA (revisa) → Van Doorn (revisa) → Transmittal
                                    ↑
                          ADASA no tiene acceso a Rev A de Van Doorn
```

### 8.2 Flujo Propuesto (Mejorado)

```
BW Water → Van Doorn (revisa) → ADASA (incorpora obs VD + revisa) → Transmittal
                    ↓
           Envia comentarios a ADASA ANTES de emitir revision
```

### 8.3 Acciones de Mejora de Proceso

1. **Solicitar a Van Doorn** copia de TODAS las revisiones previas (Rev A de todos los documentos)
2. **Establecer flujo:** Van Doorn envia comentarios → ADASA los incorpora → ADASA emite revision final
3. **Documentar:** Van Doorn = revision TECNICA, ADASA = revision CONTRACTUAL

---

## 9. REFERENCIAS

### 9.1 Documentos Fuente

| Entrega | Archivo | Version |
|---------|---------|---------|
| 3 | 2025-01-05_Revision-Tecnica-Entrega-3.md | **v3.2** |
| 4 | 2025-01-05_Revision-Tecnica-Entrega-4.md | v3.0 |
| 5 | 2026-01-06_Revision-Tecnica-Entrega-5.md | **v2.2** |
| 6 | 2026-01-08_Revision-Tecnica-Entrega-6.md | **v1.2** |

### 9.2 Comentarios Van Doorn

Ubicacion: `REVISIONES/REVISIONES VANDOORN/COMENTARIOS 12-01-26/`

---

*Compilado preparado por: ADASA*
*Fecha: 12 de enero de 2026*
*Incluye: Observaciones Asesor Van Doorn (12-Ene-2026)*
