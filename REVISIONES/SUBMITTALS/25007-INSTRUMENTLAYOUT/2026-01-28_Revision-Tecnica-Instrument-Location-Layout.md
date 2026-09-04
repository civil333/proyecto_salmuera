# REVISION TECNICA CRUZADA
## Instrument Location Layout - P22-DWG-09-008-001 Rev.A

---

| Campo | Valor |
|-------|-------|
| **Documento Revisado** | P22-DWG-09-008-001 Rev.A - Instrument Location Layout |
| **Submittal** | 25007-0009 |
| **Entrega** | ENTREGA 9 |
| **Fecha Revision** | 28 de Enero de 2026 |
| **Revisor** | ADASA - Direccion Tecnica |
| **Proyecto** | BAE 12803 - Modulo UHPRO Taltal |

---

## 1. RESUMEN EJECUTIVO

### 1.1 Veredicto

| Veredicto | Justificacion |
|-----------|---------------|
| **3 - TO BE REVISED** | El Layout hereda el TAG duplicado FIT-09-001 del Instrument List. Ademas, no incluye ubicaciones para instrumentos requeridos por ET (vibracion, Pt-100 motores). |

### 1.2 Estadisticas

| Metrica | Valor |
|---------|-------|
| Instrumentos en Layout | 32 |
| Instrumentos en Instrument List | 32 |
| Coincidencia Layout vs IL | 100% (32/32) |
| TAGs duplicados | 1 (FIT-09-001) |
| Instrumentos faltantes vs IO List | 2 (CIT-09-006, FIT-09-002) |
| Instrumentos faltantes vs ET | 5+ (vibracion, Pt-100) |

### 1.3 Observaciones por Severidad

| Severidad | Cantidad | Codigos |
|-----------|----------|---------|
| **CRITICAL** | 3 | OBS-ILL-01, OBS-ILL-02, OBS-ILL-03 |
| **MAJOR** | 3 | OBS-ILL-04, OBS-ILL-05, OBS-ILL-06 |
| **INFO** | 1 | OBS-ILL-07 |

---

## 2. ESTRUCTURA DEL DOCUMENTO

El PDF P22-DWG-09-008-001 Rev.A contiene 3 paginas:

| Pagina | Contenido | Proposito |
|--------|-----------|-----------|
| 1 | Caratula con logos ADASA/BW Water | Identificacion |
| 2 | Plan View - Layout grafico container | Ubicacion fisica instrumentos |
| 3 | Tabla de 32 instrumentos (5 columnas) | Lista de TAGs |

---

## 3. MATRIZ DE CRUCE COMPLETA

### 3.1 Instrumentos en Layout vs Instrument List

| # | TAG | Sistema | Descripcion | P&ID | En IL | Estado |
|---|-----|---------|-------------|------|-------|--------|
| 1 | DPS-09-001 | RO Cartridge Filter | Differential Pressure Switch | P8 | SI | OK |
| 2 | ORPIT-09-001 | RO Cartridge Filter | Discharge ORP analyzer | P8 | SI | OK |
| 3 | CIT-09-001 | RO Cartridge Filter | Discharge Conductivity analyzer | P8 | SI | OK |
| 4 | **FIT-09-001** | RO Cartridge Filter | Discharge Flow Transmitter | P8 | SI | **DUPLICADO** |
| 5 | PIT-09-001 | RO HP Pump | Feed Pressure Transmitter | P9 | SI | OK |
| 6 | PIT-09-002 | RO HP Pump | Discharge Pressure Transmitter | P9 | SI | OK |
| 7 | PI-09-001 | RO HP Pump | Discharge Pressure Gauge | P9 | SI | OK |
| 8 | PIT-09-003 | RO Stage 1 | Feed Pressure Transmitter | P9 | SI | OK |
| 9 | PIT-09-009 | RO Train | Combined Permeate Pressure | P9 | SI | OK |
| 10 | PIT-09-004 | RO Stage 1 | Reject Pressure Transmitter | P9 | SI | OK |
| 11 | FIT-09-003 | RO Train | Permeate Flow Transmitter | P9 | SI | OK |
| 12 | CIT-09-002 | RO Train | Permeate Conductivity analyzer | P9 | SI | OK |
| 13 | **FIT-09-001** | RO 2nd Stage | Permeate Flow Transmitter | P9 | SI | **DUPLICADO** |
| 14 | PIT-09-007 | Interstage Turbo | Pressure Transmitter | P9 | SI | OK |
| 15 | PIT-09-005 | RO Stage 2 | Feed Pressure Transmitter | P9 | SI | OK |
| 16 | PIT-09-006 | RO Stage 2 | Reject Pressure Transmitter | P9 | SI | OK |
| 17 | CIT-09-004 | RO Stage 1 | Reject Conductivity analyzer | P9 | SI | OK |
| 18 | CIT-09-003 | RO Stage 2 | Permeate Conductivity analyzer | P9 | SI | OK |
| 19 | PI-09-002 | RO Train | Reject Pressure Gauge | P9 | SI | OK |
| 20 | CIT-09-005 | RO Train | Reject Conductivity analyzer | P9 | SI | OK |
| 21 | FIT-09-004 | RO Train | Reject Flow Transmitter | P9 | SI | OK |
| 22 | PIT-09-008 | RO Train | Reject Pressure Transmitter | P9 | SI | OK |
| 23 | TIT-09-001 | CIP Tank | Temperature Transmitter | P10 | SI | OK |
| 24 | LIT-09-001 | CIP Tank | Level Transmitter | P10 | SI | **Discrepante** |
| 25 | PI-09-003 | CIP Pump | Discharge Pressure Gauge | P10 | SI | OK |
| 26 | PI-09-004 | CIP Cartridge Filter | Feed Pressure Gauge | P10 | SI | OK |
| 27 | PI-09-005 | CIP Cartridge Filter | Discharge Pressure Gauge | P10 | SI | OK |
| 28 | PHIT-09-001 | RO CIP/Flush | pH analyzer | P10 | SI | OK |
| 29 | FIT-09-005 | CIP Pump | Discharge Flow Transmitter | P10 | SI | OK |
| 30 | LS-09-001 | Antiscalant Tank | Level Switch High | P11 | SI | OK |
| 31 | LS-09-002 | Antiscalant Tank | Level Switch Low | P11 | SI | OK |
| 32 | PI-09-006 | Antiscalant Pump | Discharge Pressure Gauge | P11 | SI | OK |

**Resultado:** 32/32 instrumentos presentes en Layout (con 1 TAG duplicado)

### 3.2 Instrumentos en IO List NO en Layout

| TAG | Descripcion | En IO List | En IL | En Layout | Observacion |
|-----|-------------|------------|-------|-----------|-------------|
| CIT-09-006 | Interstage Turbo Conductivity | SI (item 28) | NO | **NO** | Faltante |
| FIT-09-002 | 2nd Stage Permeate Flow | SI (item 40) | NO* | **NO** | Deberia ser linea 13 |
| LIT-09-002 | CIP Tank Level | SI | NO* | **NO** | Layout usa LIT-09-001 |

*Nota: IO List usa FIT-09-002 y LIT-09-002, pero Instrument List y Layout usan FIT-09-001 (duplicado) y LIT-09-001

### 3.3 Instrumentos Requeridos por ET NO en Layout

| Requisito ET | Seccion | Instrumento Requerido | En Layout |
|--------------|---------|----------------------|-----------|
| Vibracion HP Pump | 5.5.7 L1390-1394 | VT-09-001 (o similar) | **NO** |
| Vibracion Feed Turbocharger | 5.5.7 L1390-1394 | VT-09-002 (o similar) | **NO** |
| Vibracion Interstage Turbocharger | 5.5.7 L1390-1394 | VT-09-003 (o similar) | **NO** |
| Pt-100 Motor HP Pump | 5.3 L1032-1033 | TE/TIT motor BH-09-001 | **NO** |
| Pt-100 Motor CIP Pump | 5.3 L1032-1033 | TE/TIT motor BH-09-002 | **NO** |
| RTD Rodamientos HP Pump | 5.1.1 L502 | RTD 3 hilos | **NO** (solo switch TE-09-001 en IO List) |
| RTD Rodamientos CIP Pump | 5.1.4 L581 | RTD 3 hilos | **NO** (solo switch TE-09-002 en IO List) |

### 3.4 Instrumentos Propuestos para Cumplimiento ET

Los siguientes instrumentos se proponen para cumplir con los requisitos de la ET no incluidos actualmente en el Layout:

#### 3.4.1 Transmisores de Vibracion (ET Sec. 5.5.7 L1390-1394)

| TAG Propuesto | Equipo | Tipo | Ubicacion Sugerida | Rango |
|---------------|--------|------|-------------------|-------|
| VT-09-001 | HP Pump (BH-09-001) | Transmisor vibracion 4-20mA+HART | Carcasa bomba, lado acople | 0-25 mm/s |
| VT-09-002 | Feed Turbocharger (SIP-09-001) | Transmisor vibracion 4-20mA+HART | Carcasa turbocompresor | 0-25 mm/s |
| VT-09-003 | Interstage Turbocharger (SIP-09-002) | Transmisor vibracion 4-20mA+HART | Carcasa turbocompresor | 0-25 mm/s |

**Requisito ET:**
> "Los equipos rotativos principales deberan contar con transmisores de vibracion para monitoreo continuo y alarmas de proteccion" (ET Sec. 5.5.7, L1390-1394)

#### 3.4.2 Sensores de Temperatura Motores (ET Sec. 5.3 L1032-1033)

| TAG Propuesto | Equipo | Ubicacion | Tipo | Senal |
|---------------|--------|-----------|------|-------|
| TE-09-003 | Motor HP Pump (87 kW) | Devanado U | Pt-100 3 hilos | AI 4-20mA |
| TE-09-004 | Motor HP Pump (87 kW) | Devanado V | Pt-100 3 hilos | AI 4-20mA |
| TE-09-005 | Motor HP Pump (87 kW) | Devanado W | Pt-100 3 hilos | AI 4-20mA |
| TE-09-006 | Motor HP Pump (87 kW) | Rodamiento DE | Pt-100 3 hilos | AI 4-20mA |
| TE-09-007 | Motor HP Pump (87 kW) | Rodamiento NDE | Pt-100 3 hilos | AI 4-20mA |
| TE-09-008 | Motor CIP Pump (15 kW) | Devanado fase | Pt-100 3 hilos | AI 4-20mA |

**Requisito ET:**
> "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos" (ET Sec. 5.3, L1032-1033)

**Nota:** Los TAGs TE-09-001 y TE-09-002 ya existen en IO List como switches digitales. Los TAGs propuestos TE-09-003 a TE-09-008 son para transmisores analogos adicionales que permitan monitoreo continuo.

---

## 4. ANALISIS DIMENSIONAL DEL CONTAINER

### 4.1 Dimensiones Container 40 ft

Segun Oferta Tecnica BW Water:

| Parametro | Valor |
|-----------|-------|
| Largo interno | ~12.0 m |
| Ancho interno | ~2.35 m |
| Alto interno | ~2.7 m |

### 4.2 Distribucion de Instrumentos (segun Plan View Pag 2)

| Zona | Instrumentos (numeros) | Cantidad | TAGs |
|------|------------------------|----------|------|
| Cartridge Filter (entrada) | 1, 2, 3, 4 | 4 | DPS, ORPIT, CIT, FIT |
| HP Pump | 5, 6, 7 | 3 | PIT-001, PIT-002, PI-001 |
| RO Stage 1 | 8, 9, 10, 11, 12, 17 | 6 | PIT, FIT, CIT |
| Turbochargers | 14 | 1 | Solo PIT-09-007 |
| RO Stage 2 | 13, 15, 16, 18 | 4 | PIT, FIT, CIT |
| Reject/Permeate | 19, 20, 21, 22 | 4 | PI, CIT, FIT, PIT |
| **DENTRO CONTAINER** | **1-22** | **22** | |
| CIP System (FUERA) | 23, 24, 25, 26, 27, 28, 29 | 7 | TIT, LIT, PI, PHIT, FIT |
| Antiscalant (FUERA) | 30, 31, 32 | 3 | LS, LS, PI |
| **FUERA CONTAINER** | **23-32** | **10** | |

### 4.3 Diagrama Esquematico de Zonas de Instrumentacion

```
+========================================================================+
|                         CONTAINER 40 ft (12.0m x 2.35m)                |
|                                                                        |
|  +-------------+  +-------------+  +--------------------------------+  |
|  | CARTRIDGE   |  |  HP PUMP    |  |         RO SKID                |  |
|  | FILTER      |  |             |  |  +------------+ +------------+ |  |
|  |             |  |  BH-09-001  |  |  |  STAGE 1   | |  STAGE 2   | |  |
|  | DPS-09-001  |  |  87 kW      |  |  | 6 vessels  | | 3 vessels  | |  |
|  | ORPIT-09-001|  |             |  |  +------------+ +------------+ |  |
|  | CIT-09-001  |  | PIT-09-001  |  |                                |  |
|  | FIT-09-001  |  | PIT-09-002  |  |  TURBOCHARGERS (SIP-09-001/002)|  |
|  |             |  | PI-09-001   |  |                                |  |
|  | (1-4)       |  | (5-7)       |  |  (8-22)                        |  |
|  +-------------+  +-------------+  +--------------------------------+  |
|                                                                        |
|  [*] FALTANTES DENTRO CONTAINER:                                       |
|      - VT-09-001 (HP Pump vibracion)                                   |
|      - VT-09-002/003 (Turbochargers vibracion)                         |
|      - TE-09-003 a TE-09-007 (Pt-100 motor HP Pump)                    |
|      - CIT-09-006 (Interstage Conductivity)                            |
+========================================================================+

      FUERA DEL CONTAINER
      ===================

+------------------+              +-------------------+
|    CIP SYSTEM    |              |   ANTISCALANT     |
|                  |              |                   |
|  TK-09-002       |              |   TK-09-003       |
|  BH-09-002       |              |                   |
|                  |              |   LS-09-001 (H)   |
|  TIT-09-001      |              |   LS-09-002 (L)   |
|  LIT-09-001      |              |   PI-09-006       |
|  PI-09-003/4/5   |              |                   |
|  PHIT-09-001     |              |   (30-32)         |
|  FIT-09-005      |              +-------------------+
|                  |
|  (23-29)         |    [*] FALTANTE: TE-09-008 (Pt-100 motor CIP Pump)
+------------------+
```

**Leyenda:**
- Numeros (1-32): Posicion en Layout original
- [*]: Instrumentos faltantes segun ET

### 4.4 Conclusiones Dimensionales

1. **Distribucion correcta:** Los 22 instrumentos del RO Skid caben dentro del container de 40 ft
2. **CIP/Antiscalant:** Los 10 instrumentos externos estan correctamente ubicados fuera
3. **Faltantes:** No hay espacio reservado para:
   - Transmisores de vibracion (3 unidades) - ET Sec 5.5.7
   - Sensores Pt-100 en motores (6 unidades HP + 1 CIP) - ET Sec 5.3
   - Conductivimetro CIT-09-006 en zona Interstage Turbocharger

---

## 5. OBSERVACIONES DETALLADAS

### OBS-ILL-01: TAG Duplicado FIT-09-001 (CRITICAL)

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-008-001 Rev.A |
| Pagina/Seccion | Pagina 3, Tabla (lineas 4 y 13) |
| Categoria | Tecnico |
| Severidad | **CRITICAL** |

**Descripcion:**
El TAG FIT-09-001 aparece dos veces en el Layout con diferentes especificaciones:
- **Linea 4:** RO Cartridge Filter Discharge Flow (DN100, 0-100 m3/h)
- **Linea 13:** RO 2nd Stage Permeate Flow (DN50, 0-18 m3/h)

**Impacto:**
- Imposible direccionar en PLC - dos transmisores con mismo TAG
- Conflicto de I/O addressing en sistema de control
- Error heredado del Instrument List P22-LI-09-008-003-A

**Requisito:**
Cada instrumento debe tener un TAG unico segun P00-IT-00-000-101 (Codificacion ADASA)

**Accion Requerida:**
Renombrar el instrumento de linea 13 a **FIT-09-002** consistente con IO List

---

### OBS-ILL-02: Ausencia Transmisores de Vibracion (CRITICAL)

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-008-001 Rev.A |
| Pagina/Seccion | Pagina 2 (Plan View) y Pagina 3 (Tabla) |
| Categoria | Tecnico |
| Severidad | **CRITICAL** |
| Ref. ET | Seccion 5.5.7, Lineas 1390-1394 |
| Ref. TM N3 | Obs #1, Seccion 2.2; Accion #1, Seccion 4.1 |

**Descripcion:**
El Layout no incluye ubicaciones para transmisores de vibracion requeridos por ET:
- HP Pump (BH-09-001) - 87 kW, equipo rotativo principal
- Feed Turbocharger (SIP-09-001) - equipo de recuperacion de energia
- Interstage Turbocharger (SIP-09-002) - equipo de recuperacion de energia

**Requisito (Cita Textual ET Sec. 5.5.7 L1390-1394):**
> "Los equipos rotativos principales deberan contar con transmisores de vibracion para monitoreo continuo y alarmas de proteccion. Los transmisores deberan ser tipo 4-20mA con protocolo HART para integracion con sistema de control."

**TAGs Propuestos:** Ver Seccion 3.4.1

**Accion Requerida:**
1. Agregar VT-09-001, VT-09-002, VT-09-003 al Instrument List con especificaciones
2. Incluir ubicacion de los transmisores en el Layout (zona HP Pump y Turbochargers)
3. Actualizar IO List con 3 senales AI (4-20mA+HART)

---

### OBS-ILL-03: Ausencia Pt-100 en Motores (CRITICAL)

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-008-001 Rev.A |
| Pagina/Seccion | Pagina 2 (Plan View) - Zona HP Pump y CIP Pump |
| Categoria | Tecnico |
| Severidad | **CRITICAL** |
| Ref. ET | Seccion 5.3, Lineas 1032-1033; Seccion 5.1.1 L502; Seccion 5.1.4 L581 |
| Ref. TM N3 | Obs #11-13, Seccion 2.2; Acciones #18-20, Seccion 4.1 |

**Descripcion:**
El Layout no muestra ubicacion de sensores de temperatura Pt-100 en los motores de:
- HP Pump (87 kW) - Motor ABB 125 HP con VFD - **Critico por potencia y VFD**
- CIP Pump (15 kW) - Motor estandar

**Requisitos (Citas Textuales ET):**

| Seccion | Linea | Texto |
|---------|-------|-------|
| 5.3 | 1032-1033 | "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos" |
| 5.1.1 | 502 | "RTDs a 3 hilos para temperatura de rodamientos" (Bomba HP) |
| 5.1.4 | 581 | "RTDs a 3 hilos para rodamientos" (Bomba CIP) |

**Situacion Actual:**
- IO List incluye TE-09-001 y TE-09-002 como switches digitales (DI)
- Los switches proveen proteccion ON/OFF pero NO monitoreo continuo
- ET Sec. 5.3 especifica "tipo Pt-100" - requisito mas exigente que RTD generico

**TAGs Propuestos:** Ver Seccion 3.4.2 (TE-09-003 a TE-09-008)

**Accion Requerida:**
1. Confirmar si Pt-100 estan incluidos en alcance BW Water (motor HP Pump y CIP Pump)
2. Si incluidos: Agregar ubicaciones al Layout para 6 sensores (3 devanados + 2 rodamientos HP, 1 CIP)
3. Si se mantienen solo switches (TSH): Justificar desviacion de ET Sec. 5.3 por escrito

---

### OBS-ILL-04: CIT-09-006 Faltante (MAJOR)

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-008-001 Rev.A vs P22-LI-09-008-001-A |
| Pagina/Seccion | Pagina 2 - Zona Interstage Turbocharger |
| Categoria | Tecnico |
| Severidad | **MAJOR** |

**Descripcion:**
El instrumento CIT-09-006 (Interstage Turbocharger Inlet Conductivity) aparece en IO List (item 28) pero:
- NO aparece en Instrument List
- NO aparece en Layout

**Impacto:**
- Conductivimetro requerido para monitoreo de calidad en punto intermedio
- Inconsistencia documental entre IO List y Layout

**Accion Requerida:**
1. Si CIT-09-006 es requerido: agregar a Instrument List y Layout
2. Si NO es requerido: eliminar de IO List
3. Justificar decision tecnica

---

### OBS-ILL-05: Discrepancia TAG LIT (MAJOR)

| Campo | Valor |
|-------|-------|
| Documento | Layout vs IO List |
| Pagina/Seccion | Pagina 3, Linea 24 |
| Categoria | Tecnico |
| Severidad | **MAJOR** |

**Descripcion:**
TAG del transmisor de nivel del tanque CIP discrepante:
- **Layout:** LIT-09-001
- **Instrument List:** LIT-09-001
- **IO List:** LIT-09-002

**Impacto:**
Inconsistencia de documentacion que puede generar confusiones en programacion PLC y comisionamiento

**Accion Requerida:**
Unificar nomenclatura - Decidir entre LIT-09-001 o LIT-09-002 y actualizar todos los documentos

---

### OBS-ILL-06: Temperature Switches vs Transmitters (MAJOR)

| Campo | Valor |
|-------|-------|
| Documento | Layout vs IO List vs ET |
| Categoria | Tecnico |
| Severidad | **MAJOR** |

**Descripcion:**
Los sensores de temperatura de las bombas (TE-09-001, TE-09-002) estan configurados como:
- **IO List:** Digital Inputs (DI) con contacto seco N.O.
- **Funcion:** Temperature Switches (TSH) - solo alarma ON/OFF

**Requisito:**
ET Seccion 5.5 requiere transmisores con protocolo 4-20mA + HART para instrumentacion

**Impacto:**
- Switches proveen proteccion adecuada
- PERO no permiten monitoreo continuo ni analisis de tendencias
- No cumplen estrictamente con ET Sec 5.5

**Accion Requerida:**
Evaluar cambio a transmisores TIT con 4-20mA+HART, o justificar configuracion actual

---

### OBS-ILL-07: Distribucion Dentro/Fuera Container (INFO)

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-008-001 Rev.A |
| Pagina/Seccion | Pagina 2 (Plan View) |
| Categoria | Informativa |
| Severidad | **INFO** |

**Descripcion:**
Distribucion de instrumentos segun Layout:
- Instrumentos 1-22: DENTRO del container (RO Skid)
- Instrumentos 23-32: FUERA del container (CIP y Antiscalant)

**Verificar:**
- Accesibilidad para mantenimiento
- Proteccion ambiental de instrumentos externos
- Cableado de senal a panel de control dentro del container

---

## 6. RELACION CON TRANSMITTAL N3 (P22-TM-09-000-003-0)

Esta revision del Instrument Location Layout esta directamente relacionada con el Transmittal N3 emitido el 28 de Enero de 2026. A continuacion se presenta la correlacion entre observaciones:

### 6.1 Matriz de Correlacion Observaciones Layout vs TM N3

| Obs Layout | Seccion TM N3 | Obs TM N3 | Descripcion | Estado |
|------------|---------------|-----------|-------------|--------|
| OBS-ILL-01 | 3.22 | OBS-01 | TAG duplicado FIT-09-001 | **CONFIRMADO** - Heredado de IL |
| OBS-ILL-02 | 3.22 | OBS-02 | Vibracion faltante en Layout | **CONFIRMADO** - Sin ubicacion |
| OBS-ILL-03 | 3.22 / 3.2 | OBS-03 + OBS-02 | Pt-100 motor faltante | **CONFIRMADO** - Sin ubicacion |
| OBS-ILL-04 | 3.22 | OBS-04 | CIT-09-006 ausente | **CONFIRMADO** - No en Layout ni IL |
| OBS-ILL-05 | 3.22 | OBS-05 | TAG LIT discrepante | **CONFIRMADO** - LIT-09-001 vs 002 |
| OBS-ILL-06 | 3.16 | OBS-01 | TE como switches DI | **CONFIRMADO** - Sin monitoreo continuo |

### 6.2 Acciones TM N3 Relacionadas con Layout

| Accion TM N3 | Seccion | Descripcion | Impacto en Layout |
|--------------|---------|-------------|-------------------|
| #5 | 4.1 | Eliminar duplicado FIT-09-001 → FIT-09-002 | Actualizar posicion 13 |
| #23 | 4.1 | Actualizar Layout con TAGs corregidos | Revision Layout obligatoria |
| #24 | 4.1 | Agregar ubicaciones VT en Layout | 3 nuevas posiciones |
| #25 | 4.1 | Unificar TAG LIT | Actualizar posicion 24 |
| #18-20 | 4.1 | Confirmar/incluir Pt-100 en motores | Hasta 7 nuevas posiciones |

### 6.3 Impacto en Cascada

El Instrument Location Layout es el **ultimo documento** en la cadena de instrumentacion:

```
P&ID → Instrument List → IO List → Layout
                    ↓
              (Errores heredados)
```

**Documentos afectados por correcciones del Layout:**

| Documento | TAG Afectado | Correccion Requerida |
|-----------|--------------|---------------------|
| P22-LI-09-008-003-A (Instrument List) | FIT-09-001 | Renombrar a FIT-09-002 |
| P22-LI-09-008-001-A (IO List) | LIT-09-002 | Unificar con IL |
| P22-DWG-09-009-09-B (P&ID P9) | FIT-09-001 | Verificar coherencia |
| Nuevo | VT-09-001/002/003 | Agregar a todos |
| Nuevo | TE-09-003 a TE-09-008 | Agregar a IL, IO, Layout |

---

## 7. RESUMEN DE ACCIONES REQUERIDAS

### 7.1 Acciones Criticas (Previo a re-emision)

| # | Accion | Documento Afectado |
|---|--------|-------------------|
| 1 | Corregir TAG duplicado: Renombrar linea 13 FIT-09-001 a FIT-09-002 | Layout + Instrument List |
| 2 | Agregar ubicacion transmisores vibracion (VT) para HP Pump y Turbochargers | Layout |
| 3 | Agregar ubicacion sensores Pt-100 motores (o confirmar alcance) | Layout |

### 7.2 Acciones Mayores (Para revision siguiente)

| # | Accion | Documento Afectado |
|---|--------|-------------------|
| 4 | Agregar CIT-09-006 al Layout o eliminar de IO List | Layout o IO List |
| 5 | Unificar TAG LIT-09-001 vs LIT-09-002 | Layout + IO List |
| 6 | Evaluar cambio TE switches a TIT transmitters | IO List + Layout |

### 7.3 Acciones Menores

| # | Accion | Documento Afectado |
|---|--------|-------------------|
| 7 | Confirmar dimensiones y escala del Layout | Layout |
| 8 | Verificar accesibilidad instrumentos externos | Layout |

---

## 8. ANEXOS GENERADOS

| Anexo | Archivo | Proposito |
|-------|---------|-----------|
| A | Esta revision | Documento principal de revision tecnica |
| B | Tabla cruce Layout vs IL | Seccion 3.1 de este documento |
| C | Tabla instrumentos faltantes vs ET | Seccion 3.3 de este documento |

---

## 9. FIRMAS Y APROBACION

| Rol | Nombre | Fecha | Firma |
|-----|--------|-------|-------|
| Preparado por | Luis Rivera | 2026-01-28 | |
| Revisado por | Direccion Tecnica ADASA | | |
| Aprobado por | Gerencia Tecnica ADASA | | |

---

*Documento preparado por ADASA - Aguas de Antofagasta S.A.*
*Proyecto: BAE 12803 - Modulo de Salmuera Taltal*
*Contrato: C-4300 BW Water Americas Inc.*
