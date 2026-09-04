# Revision Tecnica: IO List vs Valve List vs P&ID

**Proyecto:** Second Stage RO Module for Brine - PD Taltal
**Codigo Proyecto:** P22 / 25007
**Fecha:** 27 de Enero de 2026
**Revisor:** ADASA
**Version:** 1.0

---

## 1. Executive Summary

Esta revision tecnica identifica inconsistencias criticas entre el IO List (P22-LI-09-008-001 Rev.A) y el Valve List (P22-LI-09-005-002 Rev.A). Los hallazgos principales incluyen:

| Severidad | Cantidad | Descripcion |
|-----------|----------|-------------|
| **CRITICO** | 4 | TAGs de valvulas duplicados en IO List con diferentes funciones |
| **MAYOR** | 5 | Valvulas motorizadas sin senales I/O definidas |
| **MAYOR** | 4 | Inconsistencias de nomenclatura entre documentos |
| **MAYOR** | 3 | Errores de area en codificacion de TAGs |
| **MENOR** | 3 | Errores tipograficos en Valve List (area incorrecta) |

**Veredicto Recomendado:** **3 - To be revised**

Las discrepancias identificadas impiden la correcta programacion del sistema de control y deben resolverse antes de avanzar con la ingenieria de detalle.

---

## 2. Documentos Analizados

| Documento | Codigo ADASA | Revision | Fecha | Paginas |
|-----------|--------------|----------|-------|---------|
| IO List | P22-LI-09-008-001 | A | 11-Ene-2026 | 3 |
| Valve List | P22-LI-09-005-002 | A | 06-Ene-2026 | 2 |
| P&ID | P22-DWG-09-009-002 | A | 13-Nov-2025 | - |

**Referencia Normativa:** P00-IT-00-000-101 (Estandar de Codificacion ADASA)

---

## 3. Hallazgos Criticos

### OBS-01: DUPLICIDAD DE TAGS EN IO LIST

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-001 IO List |
| Pagina/Seccion | Paginas 2-3 |
| Categoria | Tecnico |
| Severidad | **CRITICO** |

**Descripcion:**

Los siguientes TAGs de valvulas motorizadas aparecen DUPLICADOS en el IO List con descripciones completamente diferentes, haciendo imposible la identificacion univoca en el sistema de control:

| TAG | Items | Descripcion 1 | Items | Descripcion 2 |
|-----|-------|---------------|-------|---------------|
| **VE09-007** | 29-32 | Interstage Turbocharger Isolation | 47-50 | RO 2nd Stage CIP Feed |
| **VE09-006** | 43-46 | RO 1st Stage CIP Feed | 66-69 | Concentrate Reject Discharge |
| **VE09-009** | 51-54 | RO 2nd Stage CIP Return | 80-83 | Antiscalant Dos. Tank Inlet |
| **VE09-010** | 55-58 | RO 1st Stage CIP Return | 94-97 | Antiscalant Dos. Pump Discharge |

**Impacto:**
- El PLC no puede direccionar correctamente las senales I/O
- Riesgo de operacion erronea de valvulas criticas
- Imposible realizar pruebas FAT/SAT

**Accion Requerida:**
BW Water debe asignar TAGs unicos a cada valvula motorizada y actualizar el IO List. Se sugiere revisar la numeracion secuencial de VE-09-XXX para evitar conflictos.

---

### OBS-02: VALVULAS MOTORIZADAS SIN SENALES I/O

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-001 IO List |
| Pagina/Seccion | Todo el documento |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

Las siguientes valvulas motorizadas aparecen en el Valve List pero NO tienen senales I/O definidas en el IO List:

| TAG Valve List | Servicio | Tipo | Tamano | Linea VL |
|----------------|----------|------|--------|----------|
| VE-09-003 | SWRO Permeate 1st Stage | Butterfly ON/OFF | DN80 | 36 |
| VE-09-004 | SWRO Permeate 1st Stage | Butterfly ON/OFF | DN80 | 37 |
| VE-09-005 | SWRO Permeate 1st Stage | Butterfly ON/OFF | DN80 | 38 |

**Impacto:**
- Valvulas motorizadas sin control automatico desde PLC
- Posible operacion manual no prevista
- Sistema de control incompleto

**Accion Requerida:**
BW Water debe agregar las senales I/O correspondientes para VE-09-003, VE-09-004 y VE-09-005, incluyendo:
- XB001 (Remote status)
- XT001 (Fault)
- SI001 (Position feedback) - si aplica
- SIC001 (Position control) - si aplica

---

### OBS-03: VALVULA MODULADORA VC-09-006 NO INTEGRADA

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-005-002 Valve List / P22-LI-09-008-001 IO List |
| Pagina/Seccion | Valve List linea 71 |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

La valvula **VC-09-006** esta definida en Valve List como:
- Servicio: SWRO 2nd Stage Reject
- Tipo: Gate Valve
- Modo: **MODULATING** (moduladora)
- Tamano: DN65
- I/O Type: Analog Input - Open/Close, Digital Output

Esta valvula requiere senales analogicas para control de posicion (AI para feedback, AO para setpoint), pero NO aparece en el IO List con este TAG.

**Nota:** Existe confision potencial con VE09-006 que aparece duplicado en IO List con diferentes funciones.

**Impacto:**
- Control de rechazo de 2da etapa sin lazo de control
- Imposible regular presion/flujo del sistema
- Afecta garantias de desempeno

**Accion Requerida:**
BW Water debe:
1. Agregar VC-09-006 al IO List con senales analogicas
2. Clarificar si VC-09-006 y algun VE09-006 son la misma valvula (error de tipo) o valvulas diferentes

---

### OBS-04: INCONSISTENCIAS DE NOMENCLATURA

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-001 vs P22-LI-09-005-002 |
| Pagina/Seccion | Multiples |
| Categoria | Tecnico |
| Severidad | **MAYOR** |

**Descripcion:**

Las descripciones de servicio no coinciden entre documentos para los mismos TAGs:

| TAG | IO List Descripcion | Valve List Descripcion | Coincide? |
|-----|---------------------|------------------------|-----------|
| VE-09-002 | Interstage Turbocharger Bypass | SWRO 2nd Stage Reject (DN25 Ball) | **NO** |
| VE-09-008 | RO 1st Stage Discharge CIP Return | SWRO Reject 1st (DN80 Butterfly) | **NO** |
| VE-09-009 | RO 2nd Stage CIP Return | SWRO 2nd Stage Reject (DN80 Butterfly) | **NO** |
| VE-09-010 | RO 1st Stage CIP Return | SWRO 1st Stage Reject (DN80 Butterfly) | **NO** |

**Impacto:**
- Confusion durante construccion y comisionado
- Riesgo de conexion erronea de senales
- Dificultad en verificacion cruzada P&ID

**Accion Requerida:**
BW Water debe unificar las descripciones de servicio entre IO List y Valve List, utilizando la nomenclatura del P&ID como referencia maestra.

---

## 4. Hallazgos Menores

### OBS-05: ERRORES DE AREA EN VALVE LIST

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-005-002 Valve List |
| Pagina/Seccion | Pagina 2, multiples lineas |
| Categoria | Editorial |
| Severidad | **MENOR** |

**Descripcion:**

Los siguientes TAGs tienen area incorrecta (07 en lugar de 09):

| Linea | Tag Erroneo | Tag Correcto | Servicio |
|-------|-------------|--------------|----------|
| 7 | VM-07-005 | VM-09-005 | Cartridge Filter Butterfly |
| 53 | VM-07-031 | VM-09-031 | SWRO Reject 2nd Stage |
| 93 | VE-07-009 | VE-09-009 | Antiscalant Valve |

**Nota:** En las columnas de System Code se indica "9" correctamente, pero el TAG escrito es "07".

**Accion Requerida:**
BW Water debe corregir los TAGs erroneos al area 09.

---

### OBS-06: FORMATO DE TAGS INCONSISTENTE

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-008-001 IO List |
| Pagina/Seccion | Todo el documento |
| Categoria | Editorial |
| Severidad | **MENOR** |

**Descripcion:**

El formato de TAGs en IO List no sigue consistentemente el estandar ADASA P00-IT-00-000-101:

| Tag en IO List | Formato Estandar ADASA |
|----------------|------------------------|
| VE09 - 007 | VE-09-007 |
| VE09 - 002 | VE-09-002 |
| VE09 - 006 | VE-09-006 |

Los espacios alrededor de guiones son inconsistentes y algunos TAGs omiten el primer guion.

**Accion Requerida:**
BW Water debe normalizar el formato de todos los TAGs al estandar ADASA: `VE-09-XXX`

---

### OBS-07: VALVULA VE-09-008 DUPLICADA EN VALVE LIST

| Campo | Valor |
|-------|-------|
| Documento | P22-LI-09-005-002 Valve List |
| Pagina/Seccion | Lineas 44 y 57 |
| Categoria | Tecnico |
| Severidad | **MENOR** |

**Descripcion:**

El TAG VE-09-008 aparece dos veces en Valve List con especificaciones diferentes:

| Linea | TAG | Servicio | Tipo | Tamano | Material |
|-------|-----|----------|------|--------|----------|
| 44 | VE-09-008 | SWRO Reject 1st | Butterfly ON/OFF | DN80 | CE3MN (SSDS) |
| 57 | VE-09-008 | SWRO Permeate 1st | Butterfly ON/OFF | DN65 | DI/Halar (PVC) |

**Impacto:** Dos valvulas fisicas diferentes con el mismo TAG.

**Accion Requerida:**
BW Water debe asignar TAGs unicos a cada valvula.

---

## 5. Resumen de Conteos

### 5.1 IO List - Valvulas Motorizadas (VE)

| Parametro | Valor |
|-----------|-------|
| Total registros VE | 40 (10 valvulas x 4 senales) |
| TAGs unicos declarados | 6 |
| TAGs duplicados | 4 (VE09-006, 007, 009, 010) |
| Valvulas reales estimadas | ~10 |

**Senales por valvula motorizada:**
- XB001: Remote status (DI)
- XT001: Fault (DI)
- SI001: Position feedback (AI)
- SIC001: Position control (AO)

### 5.2 Valve List - Valvulas Motorizadas

| Tipo | Cantidad | Protocolo |
|------|----------|-----------|
| VE (ON/OFF) | 11 | Ethernet/IP |
| VC (Moduladora) | 1 | Ethernet/IP |
| **Total Motorizadas** | **12** | - |

### 5.3 Discrepancia

| Documento | Valvulas Motorizadas |
|-----------|---------------------|
| Valve List | 12 |
| IO List (efectivas) | ~6-10 (con duplicados) |
| **Delta** | **2-6 valvulas sin I/O** |

---

## 6. Verificacion contra Estandar ADASA (P00-IT-00-000-101)

### 6.1 Formato de TAGs de Valvulas

**Formato correcto segun ADASA:**
```
[TIPO]-[AREA]-[CORRELATIVO]
Ejemplo: VE-09-007
```

| Campo | Valor Esperado | Cumple IO List? | Cumple Valve List? |
|-------|----------------|-----------------|-------------------|
| Tipo valvula | VE, VC, VM, VR, VS, VRP | SI | SI |
| Area | 09 (Osmosis Inversa 2da Etapa) | SI (sin guion) | Parcial (errores 07) |
| Correlativo | 3 digitos (001, 002...) | Parcial | Parcial |

### 6.2 Tipos de Valvula Verificados

| Tipo | Descripcion ADASA | Usado Correctamente |
|------|-------------------|---------------------|
| VM | Valvula manual | SI |
| VE | Valvula electrica (motorizada ON/OFF) | SI |
| VC | Valvula de control (moduladora) | SI |
| VR | Valvula de retencion (check) | SI |
| VRP | Valvula reductora de presion | SI |

---

## 7. Tabla de Cruce IO List vs Valve List

### Valvulas Motorizadas VE

| No. | Tag Valve List | Servicio VL | Tipo | En IO List? | Servicio IO List | Status |
|-----|----------------|-------------|------|-------------|------------------|--------|
| 1 | VE-09-002 | SWRO 2nd Stage Reject | Ball DN25 | SI | Interstage Turbo Bypass | **DIFERENTE** |
| 2 | VE-09-003 | SWRO Permeate 1st | Butterfly DN80 | **NO** | - | **FALTANTE** |
| 3 | VE-09-004 | SWRO Permeate 1st | Butterfly DN80 | **NO** | - | **FALTANTE** |
| 4 | VE-09-005 | SWRO Permeate 1st | Butterfly DN80 | **NO** | - | **FALTANTE** |
| 5 | VE-09-006 | 1st Stage CIP Feed | Butterfly DN100 | SI (dup) | CIP Feed / Conc. Reject | **DUPLICADO** |
| 6 | VE-09-007 | 2nd Stage CIP Feed | Butterfly DN80 | SI (dup) | CIP Feed / Turbo Isolation | **DUPLICADO** |
| 7 | VE-09-008 | SWRO Reject 1st | Butterfly DN80 | SI | 1st Stage CIP Return | **DIFERENTE** |
| 8 | VE-09-008 | SWRO Permeate 1st | Butterfly DN65 | - | - | **DUPLICADO VL** |
| 9 | VE-09-009 | SWRO 2nd Stage Reject | Butterfly DN80 | SI (dup) | CIP Return / Antiscalant | **DUPLICADO** |
| 10 | VE-09-010 | SWRO 1st Stage Reject | Butterfly DN80 | SI (dup) | CIP Return / Antiscalant | **DUPLICADO** |
| 11 | VE-09-010 | Antiscalant | Ball DN15 | SI (dup) | Antiscalant Pump Discharge | **OK** |
| 12 | VE-07-009 | Antiscalant | Ball DN25 | **NO** | - | **TAG ERRONEO** |

### Valvula Moduladora VC

| Tag | Servicio | Tipo | En IO List? | Observacion |
|-----|----------|------|-------------|-------------|
| VC-09-006 | SWRO 2nd Stage Reject | Gate DN65 Modulating | **NO** | Requiere AI/AO |

---

## 8. Acciones Requeridas para BW Water

### Acciones Inmediatas (Criticas)

| # | Accion | Observacion Ref. | Prioridad |
|---|--------|------------------|-----------|
| 1 | Eliminar duplicidad de TAGs VE09-006, 007, 009, 010 en IO List | OBS-01 | **CRITICA** |
| 2 | Agregar senales I/O para VE-09-003, 004, 005 | OBS-02 | **ALTA** |
| 3 | Agregar VC-09-006 al IO List con senales analogicas | OBS-03 | **ALTA** |
| 4 | Unificar descripciones de servicio entre documentos | OBS-04 | **ALTA** |

### Acciones Correctivas (Menores)

| # | Accion | Observacion Ref. | Prioridad |
|---|--------|------------------|-----------|
| 5 | Corregir TAGs con area 07 a 09 en Valve List | OBS-05 | MEDIA |
| 6 | Normalizar formato de TAGs en IO List | OBS-06 | BAJA |
| 7 | Eliminar duplicado VE-09-008 en Valve List | OBS-07 | MEDIA |

---

## 9. Veredicto

**Documento: P22-LI-09-008-001 IO List Rev.A**
**Veredicto: 3 - To be revised**

**Documento: P22-LI-09-005-002 Valve List Rev.A**
**Veredicto: 2 - Approved as noted**

**Justificacion:**

El IO List presenta deficiencias criticas que impiden su uso para programacion del PLC:
1. Duplicidad de TAGs hace imposible el direccionamiento univoco
2. Valvulas motorizadas sin senales I/O definidas
3. Inconsistencias con Valve List que generan confusion

El Valve List tiene errores menores corregibles pero es tecnicamente utilizable.

---

## 10. Anexos

### Anexo A: Extracto IO List - Valvulas VE (Items 29-97)

```
Item 29-32: VE09-007 - Interstage Turbocharger Isolation (DI, DI, AI, AO)
Item 33-36: VE09-002 - Concentrate Reject Interstage Turbo Bypass (DI, DI, AI, AO)
Item 43-46: VE09-006 - RO 1st Stage CIP Feed (DI, DI, AI, AO)
Item 47-50: VE09-007 - RO 2nd Stage CIP Feed (DI, DI, AI, AO) **DUPLICADO**
Item 51-54: VE09-009 - RO 2nd Stage CIP Return (DI, DI, AI, AO)
Item 55-58: VE09-010 - RO 1st Stage CIP Return (DI, DI, AI, AO)
Item 59-62: VE09-008 - RO 1st Stage Discharge CIP Return (DI, DI, AI, AO)
Item 66-69: VE09-006 - Concentrate Reject Discharge (DI, DI, AI, AO) **DUPLICADO**
Item 80-83: VE09-009 - Antiscalant Dos. Tank Inlet (DI, DI, AI, AO) **DUPLICADO**
Item 94-97: VE09-010 - Antiscalant Dos. Pump Discharge (DI, DI, AI, AO) **DUPLICADO**
```

### Anexo B: Extracto Valve List - Valvulas Motorizadas

```
Linea 36: VE-09-003 - SWRO Permeate 1st - DN80 Butterfly ON/OFF
Linea 37: VE-09-004 - SWRO Permeate 1st - DN80 Butterfly ON/OFF
Linea 38: VE-09-005 - SWRO Permeate 1st - DN80 Butterfly ON/OFF
Linea 44: VE-09-008 - SWRO Reject 1st - DN80 Butterfly ON/OFF
Linea 57: VE-09-008 - SWRO Permeate 1st - DN65 Butterfly ON/OFF **DUPLICADO**
Linea 58: VE-09-009 - SWRO 2nd Stage Reject - DN80 Butterfly ON/OFF
Linea 59: VE-09-010 - SWRO 1st Stage Reject - DN80 Butterfly ON/OFF
Linea 60: VE-09-002 - SWRO 2nd Stage Reject - DN25 Ball ON/OFF
Linea 63: VE-09-006 - 1st Stage CIP Feed - DN100 Butterfly ON/OFF
Linea 64: VE-09-007 - 2nd Stage CIP Feed - DN80 Butterfly ON/OFF
Linea 71: VC-09-006 - SWRO 2nd Stage Reject - DN65 Gate MODULATING
Linea 93: VE-07-009 - Antiscalant - DN25 Ball ON/OFF **TAG ERRONEO**
Linea 109: VE-09-010 - Antiscalant - DN15 Ball ON/OFF
```

---

**Fin del Documento**

*Preparado por: ADASA*
*Fecha: 27 de Enero de 2026*
