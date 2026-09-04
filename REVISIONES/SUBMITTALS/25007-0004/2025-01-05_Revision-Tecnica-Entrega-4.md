# Revision Tecnica - Entrega 4 BW Water

**Submittal:** 25007-0004
**Fecha Emision:** 24-Dic-2025
**Fecha Revision:** 06-Ene-2026
**Revisor:** ADASA
**Version:** 3.0 (incluye revision critica y observaciones adicionales ET Sec 5.4)

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0004 |
| Fecha Emision | 24-Dic-2025 |
| Documentos | 1 |
| Tipo | DWG (Plano) |
| Submittal For | FA (For Approval) |

---

## 2. Documento Recibido

| # | Codigo | Rev | Titulo | Tipo | Paginas |
|---|--------|-----|--------|------|---------|
| 1 | P22-CD-09-004-001 | A | Control System Architecture | DWG | 3 |

---

## 3. Verificacion vs Ingenieria Basica ADASA

### 3.1 Verificacion de Equipos Controlados vs Lista de Equipos ADASA

**Referencia:** P22-LI-06-005-001 (Lista de Equipos Electromecanicos)

| TAG BW Water | TAG ADASA | Equipo | Control BW | Suministro ADASA | Estado |
|--------------|-----------|--------|------------|------------------|--------|
| BH-09-001 | BH-06-002 | RO HP Feed Pump | VFD | BW Water (225 kW) | **OK** |
| BH-09-002 | BH-06-005 | CIP Pump | VFD | BW Water (11 kW) | **OK** |
| REL-09-001 | - | CIP Heater | Feeder | BW Water | **OK** |
| BDS-09-001A/B | BDS-06-001 | Antiscalant Dosing Pump | Feeder | BW Water | **OK** |
| SAI-09-001 | - | Instrumentation | Feeder | BW Water | **OK** |
| SSAA-09-002 | - | A/C Unit | Feeder | BW Water | **OK** |
| SSAA-09-001A/B | - | Indoor/Outdoor Lights | Feeder | BW Water | **OK** |

**Observaciones Equipos:**
1. Bomba de alimentacion BH-06-001 (11 kW, suministro ADASA) NO aparece en arquitectura de control BW Water - **OK, externa al modulo**
2. Bomba sumergible BS-06-001 (3 kW, suministro ADASA) NO aparece - **OK, externa al modulo**
3. Turbochargers (BH-06-003, BH-06-004) no requieren control electrico - **OK**

### 3.2 Verificacion de Instrumentos vs Lista de Instrumentos ADASA

**Referencia:** P22-LI-06-008-001 (Lista de Instrumentos)

| Instrumento | Suministro ADASA | Incluido en BW Control | Estado |
|-------------|------------------|------------------------|--------|
| FIT-06-001 (Caudalimetro Alimentacion) | ADASA | No (externo) | **OK** |
| PIT-06-001 (Transmisor Presion) | ADASA | No (externo) | **OK** |
| LIT-06-001 (Nivel TK-06-001) | ADASA | No (externo) | **OK** |
| LSH/LSL-06-001 (Switches TK-06-001) | ADASA | No (externo) | **OK** |
| LSH/LSL-06-003 (Switches Fosa) | ADASA | No (externo) | **OK** |
| PIT-06-002 a 010 (9x Presion OI) | BW Water | Si (via PLC) | **OK** |
| FIT-06-002 a 005 (4x Caudal) | BW Water | Si (via PLC) | **OK** |
| ORPIT-06-001 (ORP) | BW Water | Si (via PLC) | **OK** |
| CLIT-06-001 (Cloro) | BW Water | Si (via PLC) | **OK** |
| CONDIT-06-001 (Conductividad) | BW Water | Si (via PLC) | **OK** |

**Observaciones Instrumentos:**
1. Instrumentos suministro ADASA (8 unidades) son externos al modulo BW Water - **CORRECTO**
2. Instrumentos suministro BW Water (28 unidades) deben conectarse al PLC del LCP - **OK**

### 3.3 Verificacion de Limites de Suministro

**Referencia:** ET P22-ET-09-000-001-0 Seccion 5.4/5.5

| Item | Suministro BW Water | Suministro ADASA/Otros | Estado |
|------|---------------------|------------------------|--------|
| LCP Panel completo | SI | - | **OK** |
| PLC + programacion | SI | - | **OK** |
| VFD bombas HP y CIP | SI | - | **OK** |
| Cables control internos | SI | - | **OK** |
| Cables potencia internos | SI | - | **OK** |
| CAT6/Ethernet interno | SI | - | **OK** |
| Fibra optica DCS-LCP | - | Otros | **OK** |
| Cable Ethernet LCP-DCS | - | Otros | **OK** |
| Cable potencia 380Vac 3F | - | Otros | **OK** |
| Cable potencia 220Vac 1F | - | Otros | **OK** |
| Instalacion campo | - | Otros | **OK** |

### 3.4 Verificacion de Potencias vs Lista de Equipos ADASA

| Equipo | Potencia ADASA | Control BW Water | Estado |
|--------|----------------|------------------|--------|
| BH-06-002 (HP Pump) | 225 kW | VFD | **OK** |
| BH-06-005 (CIP Pump) | 11 kW | VFD | **OK** |
| **Total VFD** | **236 kW** | - | - |
| CIP Heater | 20 kW (ref P&ID) | Feeder | **OK** |
| Dosing Pump | <1 kW | Feeder | **OK** |
| A/C, Lights, Instr. | ~5 kW | Feeder | **OK** |
| **Total Estimado** | **~261 kW** | - | - |

---

## 4. Verificacion vs ET P22-ET-09-000-001-0

### 4.1 Codificacion

| Aspecto | Requerido | Entregado | Cumple |
|---------|-----------|-----------|--------|
| Codigo documento | P22-CD-09-XXX-XXX | P22-CD-09-004-001 | **SI** |
| Area (09) | 09 - Osmosis Inversa | 09 | **SI** |
| Tipo (CD) | CD - Diagrama de Control | CD | **SI** |

**Veredicto Codificacion:** 1 - Approved

### 4.2 Contenido Tecnico

| Aspecto | Requerido (ET 5.4/5.5) | Mostrado | Cumple |
|---------|------------------------|----------|--------|
| PLC | Requerido | Si (en LCP) | **SI** |
| VFD bombas principales | Requerido | BH-09-001 (HP), BH-09-002 (CIP) | **SI** |
| Comunicacion Ethernet | Preferido | CAT6/Ethernet/IP | **SI** |
| Comunicacion DCS | Requerido | Fibra optica a DCS | **SI** |
| Voltaje 380Vac 3F | Requerido | Indicado (by Others) | **SI** |
| Voltaje 220Vac 1F | Requerido | Indicado (by Others) | **SI** |
| Protocolo Modbus TCP | ET 5.4 | No especificado | **FALTA** |
| Redundancia comunicacion | Buena practica | No indicado | **N/A** |

**Veredicto Tecnico:** 2 - Approved as noted (falta Modbus TCP)

---

## 5. Observaciones y Brechas Identificadas

### 5.1 Observaciones CRITICAS (Requieren Accion)

| # | Observacion | Referencia | Impacto |
|---|-------------|-----------|---------|
| 1 | **Protocolo Modbus TCP:** No se especifica disponibilidad para integracion SCADA ADASA. | ET 5.4 | ALTO |
| 2 | **Puertos Ethernet:** No se indican puertos disponibles en LCP para conexion a red ADASA. | Integracion | MEDIO |
| 3 | **UPS 8 horas:** ET Sec 5.4 requiere "UPS para mantener sistema de control activo minimo 8 horas". No se muestra en arquitectura. Confirmar inclusion y capacidad. | ET 5.4 | **ALTO** |
| 4 | **Codigo fuente editable:** ET Sec 5.4 requiere entrega de "codigo fuente PLC/HMI editable + documentacion". No indicado en entrega. Confirmar compromiso contractual. | ET 5.4 | **ALTO** |
| 5 | **MVE (Medidor Variables Electricas):** ET Sec 5.4 requiere MVE con capacidad de historico. No verificado en arquitectura. Confirmar inclusion. | ET 5.4 | MEDIO |
| 6 | **Switch Ethernet >= 5 bocas:** ET Sec 5.4 especifica switch con minimo 5 puertos. No indicado en arquitectura. Confirmar especificacion. | ET 5.4 | BAJO |

### 5.2 Observaciones MENORES (Informativas)

| # | Observacion | Referencia |
|---|-------------|-----------|
| 3 | Redundancia comunicacion DCS no indicada (buena practica, no obligatorio). | Buena practica |
| 4 | Direcciones IP del sistema no especificadas (pendiente para integracion). | Integracion |
| 5 | Lista de senales I/O detallada no incluida (pendiente en otros documentos). | DS PLC |

### 5.3 Verificaciones Positivas

| # | Aspecto | Estado |
|---|---------|--------|
| 1 | Arquitectura LCP centralizada | **CORRECTO** |
| 2 | VFD para bombas principales (HP y CIP) | **CUMPLE** ET |
| 3 | Comunicacion Ethernet/IP moderna | **CUMPLE** |
| 4 | Comunicacion DCS via fibra optica | **CUMPLE** |
| 5 | Limites de suministro claramente definidos | **CORRECTO** |
| 6 | Equipos controlados coinciden con Lista Equipos ADASA | **COINCIDE** |
| 7 | Instrumentos BW Water conectados al PLC | **CORRECTO** |

---

## 6. Veredicto Final

| Aspecto | Calificacion | Codigo |
|---------|--------------|--------|
| Cumplimiento Tecnico | Aprobado con notas | 2 |
| Codificacion | Aprobado | 1 |
| Verificacion vs IB ADASA | Aprobado | 1 |
| **VEREDICTO GLOBAL** | **2 - APPROVED AS NOTED** | **2** |

---

## 7. Acciones Requeridas BW Water

| # | Accion | Prioridad | Plazo |
|---|--------|-----------|-------|
| 1 | Confirmar disponibilidad protocolo Modbus TCP en PLC para integracion SCADA ADASA | ALTA | Proxima entrega |
| 2 | Indicar puertos Ethernet disponibles en LCP para conexion a red ADASA | MEDIA | Proxima entrega |
| 3 | Confirmar direccionamiento IP propuesto para integracion | BAJA | Previo FAT |
| 4 | **NUEVO:** Confirmar UPS incluido con autonomia minima 8 horas | **ALTA** | Proxima entrega |
| 5 | **NUEVO:** Confirmar entrega codigo fuente PLC/HMI editable + documentacion | **ALTA** | Clausula contractual |
| 6 | **NUEVO:** Confirmar MVE incluido con capacidad de historico | MEDIA | Proxima entrega |
| 7 | **NUEVO:** Confirmar switch Ethernet con minimo 5 puertos | BAJA | Proxima entrega |

---

## 8. Documentos de Referencia Utilizados

### Ingenieria Basica ADASA (Area 06)
- P22-LI-06-005-001: Lista Equipos Electromecanicos
- P22-LI-06-008-001: Lista de Instrumentos

### Especificacion Tecnica Modulo
- P22-ET-09-000-001-0: Especificacion Tecnica Modulo OI (Seccion 5.4/5.5)

### Documentos BW Water Relacionados
- P22-CD-09-007-001-A: Single Line Diagram (Aprobado)
- P22-ET-09-008-001-A: DS PLC & HMI (Aprobado con notas)
- P22-DWG-09-009-002-A: P&ID (Aprobado con notas)

---

## 9. Comparacion con Revisiones Anteriores

| Aspecto | Revision v1.0 | Revision v2.0 | Revision v3.0 |
|---------|---------------|---------------|---------------|
| Cruce vs IB ADASA | No | SI | SI |
| Verificacion equipos | Solo vs ET | vs Lista Equipos ADASA | vs Lista + ET completa |
| Verificacion instrumentos | Solo vs ET | vs Lista Instrumentos ADASA | SI |
| Verificacion limites suministro | Basico | Detallado | Detallado |
| Revision critica ET 5.4 | No | Parcial | **COMPLETA** |
| Observaciones criticas | 2 | 2 | **6** |
| Observaciones menores | 1 | 3 | 3 |
| Veredicto | 2 - Approved as noted | 2 - Approved as noted | 2 - Approved as noted |

---

## 10. Puntos Ciegos Identificados (Analisis Profundo)

### 10.1 Responsabilidades No Claras

| Item | Documento | Indica | Problema |
|------|-----------|--------|----------|
| Fibra optica DCS-LCP | Control Architecture | "By Others" | **No define si ADASA o contratista tercero** |
| Ethernet LCP-DCS | Control Architecture | "By Others" | **No define si ADASA o contratista tercero** |
| Patch Panel | Notas | "By Others" | **No define responsable** |
| Cable Tray | Notas | "By Others" | **No define responsable** |

**Recomendacion:** Solicitar a BW Water clarificacion especifica de quien es "Others" en cada caso.

### 10.2 Puntos Criticos Pendientes de Clarificar

| # | Item | Descripcion | Impacto | Referencia ET |
|---|------|-------------|---------|---------------|
| 1 | **Modbus TCP** | No especificado en arquitectura. ET 5.4 requiere integracion SCADA. | **CRITICO** | Sec 5.4 |
| 2 | **Puertos Ethernet** | No indicados cantidad disponible en LCP para expansion futura. | **CRITICO** | Sec 5.5 |
| 3 | **Direcciones IP** | No propuestas. Necesarias para integracion con red ADASA. | MEDIO | Integracion |
| 4 | **Redundancia DCS** | No indicada. Buena practica para continuidad operacional. | BAJO | Buena practica |

### 10.3 Verificacion de Potencias Detallada

| Equipo | Lista Equipos ADASA | Control Architecture | Delta |
|--------|---------------------|----------------------|-------|
| BH-06-002/BH-09-001 (HP Pump) | 225 kW | VFD (sin potencia indicada) | **Verificar** |
| BH-06-005/BH-09-002 (CIP Pump) | 11 kW | VFD (sin potencia indicada) | **Verificar** |
| REL-09-001 (Heater) | No listado | 20 kW (de P&ID) | OK |
| Total | 250 kW (Lista Equipos) | ~261 kW (estimado) | +11 kW |

**Nota:** La diferencia de +11 kW corresponde principalmente al heater CIP (20 kW), no listado en IB original. Es una **mejora** del sistema.

### 10.4 Comunicacion Dual Path

El documento muestra doble via de comunicacion al DCS:
1. **Fibra optica** - Via primaria
2. **Ethernet** - Via secundaria

**Observacion:** Esto es positivo para redundancia, pero no se indica si estan en modo activo-activo o activo-pasivo.

---

## 11. Requerimientos ET 5.4 No Verificados (Revision Critica v3.0)

La revision critica identifico los siguientes requerimientos de ET Seccion 5.4 que no fueron verificados en revisiones anteriores:

| # | Requerimiento ET 5.4 | Estado Verificacion | Prioridad |
|---|---------------------|---------------------|-----------|
| 1 | UPS autonomia 8 horas | **NO VERIFICADO** | CRITICA |
| 2 | Codigo fuente editable | **NO VERIFICADO** | CRITICA |
| 3 | MVE con historico | **NO VERIFICADO** | ALTA |
| 4 | Switch >= 5 puertos | **NO VERIFICADO** | MEDIA |
| 5 | Modbus TCP | NO VERIFICADO (ya en obs. 1) | CRITICA |
| 6 | Puertos Ethernet disponibles | NO VERIFICADO (ya en obs. 2) | ALTA |

### 11.1 Texto Exacto ET Seccion 5.4 (Referencia)

> *"El sistema de control incluira como minimo:*
> - *PLC con capacidad de expansion*
> - *UPS para mantener sistema de control activo minimo 8 horas*
> - *Switch Ethernet industrial con minimo 5 puertos*
> - *MVE (Medidor Variables Electricas) con capacidad de historico*
> - *Protocolo Modbus TCP para integracion SCADA*
> - *El codigo fuente del PLC y HMI sera entregado al Cliente en formato editable junto con documentacion completa"*

### 11.2 Impacto de Brechas

| Brecha | Impacto si no se resuelve |
|--------|---------------------------|
| UPS 8h | Perdida total de control en falla electrica prolongada |
| Codigo fuente | Dependencia perpetua de BW Water para modificaciones |
| MVE | Sin capacidad de medicion y registro de energia |
| Switch 5 puertos | Limitacion para expansion futura |

---

**Firma Revisor:** _____________________
**Fecha:** 06-Ene-2026

---

*Documento generado: 06-Ene-2026*
*Version: 3.0 - Incluye revision critica completa ET Seccion 5.4*
