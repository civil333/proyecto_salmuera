# REVISION DE AVANCE DE INGENIERIA
## Proyecto: Modulo de Salmuera Taltal - BAE 12803 / Contrato C-4300

**Fecha de revision:** 06 de enero de 2026
**Revisor:** ADASA
**Proveedor:** BW Water Americas Inc.
**Tipo:** Revision de Avance de Ingenieria

---

## 1. ANTECEDENTES

Segun el programa preliminar de BW Water, la fase de ingenieria debia completarse el **05-Ene-2026** (65 dias desde NTP). Esta revision analiza el estado de avance de los entregables de ingenieria al dia siguiente de la fecha limite.

### Documentos de Referencia
- Programa Preliminar BW Water (Project TalTal-Preliminary Taltal Schedule.pdf)
- Especificacion Tecnica P22-ET-09-000-001-0, Seccion 7
- Contrato C-4300 BW Water

---

## 2. ENTREGAS RECIBIDAS

| Entrega | Submittal | Fecha Recepcion | Documentos | Veredicto Global |
|---------|-----------|-----------------|------------|------------------|
| Entrega 1 | 25007-0001 | 10-Dic-2025 | 13 | 4 - Rejected |
| Entrega 2 | 25007-0002 | 16-Dic-2025 | 7 | 3 - To be revised |
| Entrega 3 | 25007-0003 | 16-Dic-2025 | 1 | 2 - Approved as noted |
| Entrega 4 | 25007-0004 | 24-Dic-2025 | 1 | 2 - Approved as noted |
| **TOTAL** | | | **22** | |

---

## 3. ESTADO DE APROBACIONES

### 3.1 Distribucion por Veredicto (22 documentos recibidos)

| Veredicto | Cantidad | % | Descripcion |
|-----------|----------|---|-------------|
| 1 - Approved | 8 | 36% | Sin observaciones |
| 2 - Approved as noted | 4 | 18% | Con observaciones menores |
| 3 - To be revised | 7 | 32% | Requiere correccion |
| 4 - Rejected | 3 | 14% | Rechazado |

### 3.2 Documentos Listos para Fabricacion

Solo los documentos con veredicto **1 - Approved** o **2 - Approved as noted** permiten avanzar a fabricacion:

**Documentos aprobados:** 12 de 37 (**32%**)

---

## 4. ANALISIS POR CATEGORIA

### 4.1 Documentos de Proceso

| Documento | Estado |
|-----------|--------|
| Process Calculation | Recibido - To be revised |
| PFD / Mass Balance | Recibido - To be revised |
| P&ID | Recibido - **Approved as noted** |
| Utility Consumption List | **PENDIENTE** |
| Chemical and Consumption List | **PENDIENTE** |
| Plant Control Philosophy | **PENDIENTE** |

### 4.2 Documentos Electricos

| Documento | Estado |
|-----------|--------|
| Electrical Load List | Recibido - Rejected |
| Single Line Diagram | Recibido - Rejected |

### 4.3 Documentos de Control

| Documento | Estado |
|-----------|--------|
| Control System Architecture | Recibido - **Approved as noted** |
| I/O List | **PENDIENTE** |

### 4.4 Documentos Mecanicos

| Documento | Estado |
|-----------|--------|
| Line List | **PENDIENTE** |
| Instrument List | **PENDIENTE** |
| Valve List | **PENDIENTE** |
| A/C Thermal Calculation | **PENDIENTE** |
| Equipment Layout | **PENDIENTE** |
| Piping Layout | **PENDIENTE** |
| Stress & Flexibility Analysis | **PENDIENTE** |
| Maintenance Lifting Points | **PENDIENTE** |
| 3D Model | **PENDIENTE** |

### 4.5 Datasheets de Equipos

| Documento | Estado |
|-----------|--------|
| DS Container | Recibido - Rejected |
| DS SWRO System | Recibido - To be revised |
| DS RO HP Pump | Recibido - To be revised |
| DS CIP Pump | Recibido - To be revised |
| DS Antiscalant Dosing Pump | Recibido - **Approved** |
| DS PLC and HMI | Recibido - To be revised |
| DS Electrical Aux Component | Recibido - **Approved** |
| DS MCC | **PENDIENTE** |
| DS RO Cartridge Filter | Recibido - **Approved as noted** |
| DS CIP Cartridge Filter | Recibido - **Approved** |
| DS 1st Stage Turbo | Recibido - **Approved** |
| DS 2nd Stage Turbo | Recibido - **Approved** |
| DS CIP Tank | Recibido - **Approved** |
| DS Antiscalant Dosing Tank | Recibido - **Approved** |
| DS CIP Tank Heater | Recibido - **Approved as noted** |

### 4.6 Especificaciones

| Documento | Estado |
|-----------|--------|
| Piping Specifications | Recibido - To be revised |
| Painting Specifications | Recibido - To be revised |

### 4.7 Plan de Inspeccion y Ensayos

| Documento | Estado |
|-----------|--------|
| ITP (PIE Detallado) | **PENDIENTE** |

---

## 5. OBSERVACIONES CRITICAS PENDIENTES

### 5.1 Prioridad CRITICA (Asesor LH)

1. **Modelacion turbochargers:** Falta modelacion para ambas salinidades (43,000 y 53,000 mg/L TDS)
2. **Presiones de diseno:** Margen actual 4% vs 10% requerido (debe ser 83.9 bar minimo)
3. **Bomba HP:** Requiere redimensionamiento de TDH

### 5.2 Prioridad ALTA (ADASA)

4. **Contenedor:** No cumple requisitos ET 5.1.10 (puertas, accesos, rejilla PRFV)
5. **Material bomba HP:** Ambiguedad entre "Duplex" y "Super Duplex" requerido
6. **RTDs en bombas:** No mencionados en bombas HP y CIP

### 5.3 Prioridad MEDIA

7. **Protocolo Modbus TCP:** No especificado en PLC
8. **Flanges turbochargers:** No especificados (requerido Cl 900 lb)
9. **Codificacion:** 12 documentos usan "ITEM" en vez de "ET"

---

## 6. IMPACTO EN PROGRAMA

### 6.1 Hitos Afectados

| Hito | Fecha Programa | Estado |
|------|----------------|--------|
| Engineering Complete | 05-Ene-2026 | **ATRASADO** |
| Fabrication Start | 02-Ene-2026 | **EN RIESGO** |
| ITP Approval | 31-Dic-2025 | **ATRASADO** |
| Ready to Ship | 03-Ago-2026 | En riesgo |

### 6.2 Riesgo Contractual

Segun Contrato C-4300:
- **Multa por atraso en ingenieria/documentos:** 0.05% diario del monto neto
- **Monto base:** USD 613,991.00
- **Multa diaria estimada:** USD 307.00

---

## 7. CONCLUSIONES

1. **Avance de entregas:** 59% (22 de 37 documentos entregados)
2. **Avance de aprobaciones:** 32% (12 documentos listos para fabricacion)
3. **Documentos pendientes:** 15 documentos con atrasos de hasta 63 dias
4. **Estado general:** La fase de ingenieria NO se completo en la fecha comprometida

---

## 8. ACCIONES REQUERIDAS

1. BW Water debe entregar los 15 documentos pendientes de forma urgente
2. BW Water debe reemitir los 10 documentos con veredicto 3 y 4
3. Solicitar programa actualizado con plan de recuperacion
4. Convocar reunion de seguimiento urgente

---

## 9. TABLA RESUMEN DE ENTREGABLES

| Entregable | Entrega BW Water | Estado | Fecha Comprometida | Dias Atraso |
|------------|------------------|--------|-------------------|-------------|
| Process Calculation | Entrega 1 | 3 - To be revised | 28-Oct-2025 | 70 |
| PFD / Mass Balance | Entrega 1 | 3 - To be revised | 28-Oct-2025 | 70 |
| P&ID | Entrega 3 | 2 - Approved as noted | 12-Dic-2025 | 25 |
| Utility Consumption List | Pendiente | - | 04-Nov-2025 | 63 |
| Chemical and Consumption List | Pendiente | - | 06-Nov-2025 | 61 |
| Plant Control Philosophy | Pendiente | - | 23-Dic-2025 | 14 |
| Electrical Load List | Entrega 1 | 4 - Rejected | 05-Nov-2025 | 62 |
| Single Line Diagram | Entrega 1 | 4 - Rejected | 07-Nov-2025 | 60 |
| Control System Architecture | Entrega 4 | 2 - Approved as noted | 03-Nov-2025 | 64 |
| I/O List | Pendiente | - | 11-Dic-2025 | 26 |
| Line List | Pendiente | - | 14-Nov-2025 | 53 |
| Instrument List | Pendiente | - | 14-Nov-2025 | 53 |
| Valve List | Pendiente | - | 14-Nov-2025 | 53 |
| A/C Thermal Calculation | Pendiente | - | 28-Nov-2025 | 39 |
| Equipment Layout | Pendiente | - | 05-Dic-2025 | 32 |
| Piping Layout | Pendiente | - | 30-Dic-2025 | 7 |
| Stress & Flexibility Analysis | Pendiente | - | 29-Dic-2025 | 8 |
| Maintenance Lifting Points | Pendiente | - | 29-Dic-2025 | 8 |
| 3D Model | Pendiente | - | 29-Dic-2025 | 8 |
| DS Container | Entrega 1 | 4 - Rejected | 03-Nov-2025 | 64 |
| DS SWRO System (Vessel+Membrane) | Entrega 1 | 3 - To be revised | 27-Oct-2025 | 71 |
| DS RO HP Pump | Entrega 1 | 3 - To be revised | 13-Nov-2025 | 54 |
| DS CIP Pump | Entrega 1 | 3 - To be revised | 13-Nov-2025 | 54 |
| DS Antiscalant Dosing Pump | Entrega 1 | 1 - Approved | 13-Nov-2025 | 54 |
| DS PLC and HMI | Entrega 1 | 3 - To be revised | 13-Nov-2025 | 54 |
| DS Electrical Aux Component | Entrega 1 | 1 - Approved | 11-Nov-2025 | 56 |
| DS MCC | Pendiente | - | 19-Nov-2025 | 48 |
| DS RO Cartridge Filter | Entrega 2 | 2 - Approved as noted | 26-Nov-2025 | 41 |
| DS CIP Cartridge Filter | Entrega 2 | 1 - Approved | 19-Nov-2025 | 48 |
| DS 1st Stage Turbo | Entrega 2 | 1 - Approved | 24-Nov-2025 | 43 |
| DS 2nd Stage Turbo | Entrega 2 | 1 - Approved | 24-Nov-2025 | 43 |
| DS CIP Tank | Entrega 2 | 1 - Approved | 27-Nov-2025 | 40 |
| DS Antiscalant Dosing Tank | Entrega 2 | 1 - Approved | 27-Nov-2025 | 40 |
| DS CIP Tank Heater | Entrega 2 | 2 - Approved as noted | 27-Nov-2025 | 40 |
| Piping Specifications | Entrega 1 | 3 - To be revised | - | - |
| Painting Specifications | Entrega 1 | 3 - To be revised | - | - |
| ITP (PIE Detallado) | Pendiente | - | 31-Dic-2025 | 6 |

---

**Resumen Final:**

| Metrica | Valor |
|---------|-------|
| Total documentos requeridos | 37 |
| Documentos entregados | 22 (59%) |
| Documentos pendientes | 15 (41%) |
| Documentos aprobados (1 o 2) | 12 (32%) |
| Documentos por corregir (3 o 4) | 10 (27%) |
| Atraso maximo | 71 dias |
| Atraso promedio (docs entregados) | 52 dias |

---

*Documento generado el 06 de enero de 2026*
